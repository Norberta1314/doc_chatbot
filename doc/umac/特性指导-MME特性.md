# ZUF-78-01 移动性管理 
概述 :功能描述 :移动性管理功能用来控制UE在4G网络下的接入，以及跟踪UE当前的位置信息，即管理UE当前所在的跟踪区TA以及跟踪区列表TA List、UE当前所在MME等信息。移动性管理功能主要通过附着、分离、跟踪区更新等流程来实现。这些流程保证了在UE移动的时候，相关网络实体中UE位置信息的及时更新。
移动性管理通过EPS移动性状态以及EPS连接状态之间的切换，来表征不同的业务活动：
EPS移动性状态，包含EMM-DEREGISTERED以及EMM-REGISTERED。 
EPS连接状态，包含ECM-IDLE和ECM-CONNECTED。 
图1  UE中EMM状态模型

EPS移动性UE状态说明参见下表。 
状态名称|说明
---|---
EMM-DEREGISTERED|UE未附着到MME，或者UE之前附着到MME上但后续主动分离，或者UE长时间不活动被MME隐式分离。在此状态下，UE对MME来说不可达，因为EMM上下文中不包括用户的有效位置和路由信息。UE的部分上下文仍可保存在UE和MME中，这样避免了在每次附着的时候发起AKA过程（即鉴权过程）。
EMM-REGISTERED|UE可以通过一次成功的附着流程（ATTACH/TAU等）来进入此状态。这种状态下，MME知道UE的确切位置或者是用户所在的TA List。
图2  MME中EMM状态模型

EPS移动性UE状态说明参见下表。 
状态名称|说明
---|---
ECM-IDLE|UE与MME之间没有建立NAS信令连接，eNodeB内无用户上下文信息，包括用户面和信令面信息，此时核心网可以知道用户当前所在的跟踪区列表。
ECM-CONNECTED|UE和MME之间存在NAS信令连接，eNodeB内存在用户信令面和用户面信息，此时核心网可以知道当前用户所在的小区、跟踪区以及eNodeB ID。
功能特性简介 :为了应对各种场景下用户状态切换，以及位置变化，核心网提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
附着|MME网元附着流程是用户注册到EPS网络上的流程，是用户开机后的第一个过程，是后续所有流程的基础。在附着过程中，会为用户建立一个默认承载，也可以对用户进行鉴权（用户首次附着到EPS网络上必须鉴权）。附着流程完成之后，用户可以通过EPS网络访问数据业务和其他业务。|ZUF-78-01-001 附着
RAT内跟踪区更新|在跟踪区更新过程中，用户重新建立连接接入EPS网络，如果之前有RRC连接，RRC连接会被先断开，再重新建立RRC连接。另外，在跟踪区更新过程中，也可以把用户所有承载的E-RAB连接和空口RB连接再重新建立起来。跟踪区更新流程完成之后，如果已经为用户把所有承载的E-RAB连接和空口RB连接重新建立了，则用户可以通过EPS网络访问数据业务和其他业务。如果没有为用户把所有承载的E-RAB连接和空口RB连接重新建立，用户可以通过业务请求过程重新建立所有承载的E-RAB连接和空口RB连接，之后用户就可以继续通过EPS网络访问数据业务和其他业务。|ZUF-78-01-002 RAT内TAU
RAT间跟踪区更新|MME的跨RAT流程，指的是当UE从2/3G无线接入进入LTE无线接入，或者从LTE无线接入进入2/3G无线接入时，所涉及的跟踪区/路由区更新以及RIM流程。和RAT内跟踪区更新相比，本特性解决了如下关键问题：用户临时标识映射，即RAI+PTMSI和GUTI之间的相互转化QoS参数的映射，包括EPS Qos到Pre-R8 Qos的映射、Pre-R8 Qos到EPS Qos的映射|ZUF-78-01-003 跨RAT TAU
业务请求|业务请求流程是重建用户的S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接的流程。在业务请求流程中，用户的S1连接和E-RAB连接都被重建，空口的RRC连接和RB连接也会一并被重建，eNodeB保存用户的安全等信息，UE和MME中用户的ECM状态从空闲态变为连接态。业务请求流程完成之后，用户能继续通过EPS网络访问数据业务和其他业务。|ZUF-78-01-004 业务请求
S1连接释放|在S1释放流程中，用户的S1连接和E-RAB连接都被释放，空口的RRC连接和RB连接也会一并被释放，eNodeB不再保存用户的任何信息，UE和MME中用户的ECM状态从连接态变为空闲态，non-GBR承载会被保留，GBR承载根据运营商策略，可以被保留或去激活。S1释放流程完成之后，用户不能通过EPS网络访问数据业务和其他业务，只有通过业务请求流程，重建S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，才能继续通过EPS网络访问数据业务和其他业务。|ZUF-78-01-005 S1释放
去附着|分离流程是用户从EPS网络上注销的流程，包括UE发起的分离流程、MME发起的分离流程、HSS发起的分离流程。根据是否需要显示通知UE分离，分离流程又可以分为显示的分离流程和隐式的分离流程。MME和UE之间有分离消息时，此时为显示的分离流程。MME检测到UE长时间没有和EPS网络交互，MME触发分离流程，不通知UE，此时为隐式的分离流程。在分离过程中，会删除为用户建立的所有承载，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为注销态。分离流程完成之后，用户不能再通过EPS网络访问数据业务和其他业务。|ZUF-78-01-006 去附着
用户数据管理|当HSS中的签约数据发生变化时，HSS通知MME更新用户数据。当MME删除用户上下文时，通知HSS用户已经被清除。|ZUF-78-01-007 用户数据管理
UE可达性管理|当HSS需获知UE是否可达时，HSS可向MME发送通知请求。MME收到UE Activity Notification Request消息，且UE的状态为可达，MME则将UE的状态上报给HSS。|ZUF-78-01-008 UE可达性管理
跟踪区列表管理|跟踪区列表分配功能是指在UE附着或非周期性跟踪区更新等过程中，给UE分配或者重新分配一个TA的集合，这个特定的TA集合称之为TA List。TA List中必须包含当前UE所在TA，且必须是在为UE服务的SGW范围内的TA，同时必须是当前MME范围内的TA。根据UE的业务特性和位置，ZXUN uMAC还可以提供更为灵活的TA List分配策略。|ZUF-78-01-009 跟踪区列表管理
服务节点选择|当UE发起局间附着或TAU流程时，MME需从源局获取用户的上下文，并判断源局是SGSN局或MME局。MME支持通过下列三种方法进行判断。根据MME的Group ID的最大比特位值进行判断。如果最大比特位的值是0，源局为SGSN。如果最大比特位的值是1，源局为MME。消息携带的指示符指示源局为SGSN或MME。如果组网规划无法实现第一种方法，而消息也没有携带指示符，MME支持设置源局为SGSN和MME，执行DNS查询两次，再使用通过成功查询而获得的地址。|ZUF-78-01-010 服务节点选择
## ZUF-78-01-001 附着 
特性描述 :特性描述 :描述 :定义 :MME网元附着流程是用户注册到EPS网络上的流程，是用户开机后的第一个过程，是后续所有流程的基础。
在附着过程中，会为用户建立一个默认承载，也可以对用户进行鉴权（用户首次附着到EPS网络上必须鉴权）。 
附着流程完成之后，用户可以通过EPS网络访问数据业务和其他业务。 
应用场景 :附着流程是基本流程，用户想要通过EPS网络访问数据业务和其他业务，必须通过附着流程注册到EPS网络。具体常见场景包括： 
用户首次买卡开机。 
用户关机开机。 
用户从其他网络移动到LTE网络下发起附着。 
客户收益 :受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的EPS网络上，使运营商可以为用户提供各种数据业务和其他业务。运营商也可以通过在附着过程中对用户进行鉴权，拒绝非法用户接入EPS网络，避免用户非法使用网络资源。
移动用户|对终端用户不可见。
实现原理 :系统架构 :EPS网络架构如下图所示。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|触发附着流程，实现安全管理和承载管理功能。
eNodeB|对用户进行接入层安全管理，为用户选择MME，完成对用户无线资源管理功能。
MME|对用户进行接入控制和安全管理，完成SGW和PGW的选择，完成用户临时标识的分配，完成TA List的分配，完成MME或SGSN的选择，完成HSS的选择，完成承载管理功能。
HSS|将用户签约数据提供给MME，存储用户目前所接入的MME信息。
SGW|管理和存储UE的承载信息。
PGW|负责将UE接入PDN，分配用户IP地址，完成承载管理功能。
PCRF|对默认承载下发QoS策略和计费规则。
本网元实现 :附着流程属于基本业务流程，实现细节参见下面业务流程的具体描述。 
业务流程 :图2  附着流程

流程说明： 
UE通过发送Attach Request消息（包含选择的网络和老的GUMMEI的RRC参数）到eNodeB，发起附着流程。 
eNodeB通过RRC参数中的老的GUMMEI和指示的选择网络查找到MME。如果查找不到MME，就由MME选择功能选择MME。eNodeB将Attach
Request消息通过初始UE消息转发给新MME，其中包括接收到的选择网络和UE所在小区的TAI+ECGI标识。 
如果UE通过GUTI识别自己，并且自从去附着后服务UE的MME已经发生变化，新MME通过UE带上来的GUTI找到老MME/SGSN地址，再发送一个标识请求消息给老MME/SGSN以请求IMSI。如果消息发送到老MME，老MME通过NAS MAC验证，通过后给新MME回标识响应消息，其中包含IMSI和移动性上下文；如果消息发送到老SGSN，老SGSN通过P-TMSI签名验证，通过后给新MME回标识响应消息，其中包含移动性上下文；如果UE在老MME/SGSN中是未知的或如果Attach
Request消息完整性检查或P-TMSI签名检查失败，老MME/SGSN发送携带错误原因值的响应消息给新MME。
如果UE在老MME/SGSN和新MME中都不能被识别，新MME发送标识请求消息给UE以请求IMSI。UE使用包含IMSI的标识响应消息通知网络侧。 
如果网络侧没有UE上下文，如果Attach Request消息没有完整性保护，或如果完整性检查失败，鉴权和NAS安全建立以激活完整性保护和NAS加密是必须的，否则安全过程是可选的。从这步开始，后续的所有NAS消息都将使用NAS安全功能（加密和完整性保护）进行保护。 
从UE获取ME标识。ME标识应加密传输，除非是在紧急附着情况下且不能被认证时。为了最小化信令的延迟，ME标识获取可以合并在步骤5a中的NAS安全建立过程。MME可能发送ME标识检查请求消息给EIR。EIR给MME回ME标识检查应答消息，消息包含检查结果。MME根据检查结果决定是继续Attach流程还是拒绝UE。 
如果UE在Attach Request消息中设置了加密选项传输标识，像PCO或APN或者两者这样的加密选项，现在都可以从UE获取。这样的PCO选项中可能包含有用户的身份信息，例如用户名和口令。
如果在新MME上有用户激活的承载上下文（比如没有事先去附着就在同一个MME再次附着），新MME通过发送删除会话请求消息给GW删除承载。GW给MME回删除会话响应。如果部署了PCRF，PGW执行IP-CAN会话结束过程来指示释放资源。
如果从UE上次分离后MME改变了，或MME没有UE的有效的签约上下文，或ME标识改变，或如果UE提供的IMSI或者UE提供的老GUTI在MME没有关联到有效的上下文，MME发送更新位置请求消息给HSS。 
HSS发送取消位置消息给老MME。老MME回应取消位置应答消息，删除MM和承载上下文。如果ULR-Flags指示初始附着，并且HSS中包含有SGSN注册信息，HSS发送取消位置消息给老SGSN，取消类型指示老MME/SGSN释放旧SGW上的承载资源。 
如果在老MME上有用户激活的承载，老MME通过发送删除会话请求消息给GW删除承载。GW给MME回删除会话响应；如果部署了PCRF，PGW执行IP-CAN会话结束过程来指示释放资源。 
HSS发送更新位置应答消息给新MME，消息包含IMSI、签约数据等。签约数据包含一个或多个PDN签约上下文信息。每一个PDN签约上下文中包含EPS签约QoS参数和签约的APN-AMBR。新MME验证UE是否可在新TA中存在。如果由于区域签约限制或接入限制，不允许UE附着在该TA中，或者由于其他原因而致使签约检查失败，MME拒绝附着请求。如果检查成功，新MME给UE创建一个上下文。如果UE所提供的APN是签约所不允许的或HSS拒绝了更新位置，则新MME拒绝附着请求消息。 
MME选择PGW和SGW，MME向SGW发送创建会话请求消息。 
SGW在其EPS承载列表中创建一个条目，发送创建会话请求消息给之前选择的PGW。本步骤以后，SGW缓存任何从PGW接收的下行分组数据，直到收到第23步的修改承载请求消息，在这之前不能发送下行数据通知消息给MME。 
如果部署了动态PCC并且切换指示不存在，PGW执行IP-CAN会话建立过程，从而获得UE的默认PCC规则。 
如果部署了动态PCC并且切换指示存在，PGW执行IP-CAN会话修改过程。 
PGW在EPS承载上下文列表中创建一个新的条目，并生成一个计费标识。PGW返回创建会话响应消息给SGW。 
如果SGW接收到MS Info Change Reporting Action（start）指示，SGW存储并报告UE位置改变情况。SGW回复创建会话响应消息给新MME。 
新的MME存储MS Info Change Reporting Action（Start）信息并报告UE位置改变情况。MME根据缺省APN的签约APN-AMBR和签约UE-AMBR确定UE-AMBR。新MME发送Attach
Accept消息给eNodeB。如果新MME分配新的GUTI，则消息中包含GUTI。这条消息包含在S1-MME控制面初始上下文建立请求消息中。 
eNodeB发送包含EPS无线承载标识的RRC连接重配置消息及Attach Accept消息给UE。当UE接收到附着接受消息时，UE必须将TIN设置为GUTI。 
UE发送RRC连接重配置完成消息给eNodeB。 
eNodeB发送初始上下文响应消息给新MME。该消息包含eNodeB的TEID以及eNodeB的地址，该地址用于S1-U参考点的下行业务。 
UE发送直传消息给eNodeB，该消息包含Attach Complete消息。 
eNodeB通过上行NAS传输消息转发Attach Complete消息给新MME。 
新MME接收到第20步的初始上下文响应消息和第22步的Attach Complete消息，新MME发送修改承载请求消息给SGW。 
如果第23步包含切换指示，SGW发送修改承载请求消息给PGW，使其将报文从非3GPP接入切到3GPP接入，通过所建立的缺省承载或者专用EPS承载立即开始给SGW传送数据包。 
PGW向SGW发送修改承载响应消息。 
SGW向新MME发送修改承载响应消息。SGW可以发送缓存的下行报文。 
新MME接收到SGW发送的修改承载响应消息。如果请求类型没有指示切换，承载建立，签约数据指示用户被容许切换到非3GPP接入，并且如果MME选择的PGW不同于HSS签约PDN上下文的PGW标识，MME应发送通知请求消息给HSS，消息中包含APN和PGW标识。 
HSS保存APN和PGW标识，发送通知响应消息给MME。 
系统影响 :随着接入用户数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
应用限制 :该特性不涉及应用限制。 
特性交互 :由于附着流程是基本业务流程，是后续所有流程的基础，如果附着失败，则其他业务都无法使用。 
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"
3GPP TS 23.203: "Policy and charging control architecture"
3GPP TS 23.003: "Numbering, addressing and identification"
3GPP TS 24.007: "Mobile radio interface signalling layer3; General aspects"
特性能力 :名称|指标
---|---
附着流程完成用户的接入过程并同时激活了一个默认承载。|1个
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS|MME|PCRF
---|---|---|---|---|---|---
√|√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项|命令
---|---
EPC地址解析配置|ADD EPCHOST
SET EPCHOST|EPC地址解析配置
DEL EPCHOST|EPC地址解析配置
SHOW EPCHOST|EPC地址解析配置
ADD EPCHOST IPADDR|EPC地址解析配置
DEL EPCHOST IPADDR|EPC地址解析配置
性能统计 :测量类型|描述
---|---
附着流程测量|编号为43000开头的所有计数器
告警和通知 :告警和通知
---
2114060402 网关类节点不可达
2114060401 移动性管理类节点不可达
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现附着流程。 
调整特性 :配置是否获取IMEI。SET MOBILE MANAGEMENT:MMEGETIMEI="Get
IMEI" 
配置IMSI附着鉴权控制策略，局内GUTI附着时鉴权控制策略，局间Attach鉴权控制策略。设置默认策略：SET MME IMSI AUTH DEFAULT:SERVICETYPE="IMSIATTACH",AUTHTYPE="Frequency",AUTHTIMES=5,AUTHSELNUM=2根据IMSI号段配置鉴权策略：ADD MME IMSI AUTH:IMSI="4601199",SERVICETYPE="IMSIATTACH",AUTHTYPE="Frequency",AUTHTIMES=5,AUTHSELNUM=1 
EIR检查是否开启。SET SECURITY PARAMETER:MMECHECKIMEI="Need",MMEFAILIMEI="Continue" 
设置MME本局支持的完整性保护算法。SET NAS INTEGCTRL :INTEGALGO1="Support",INTEGALGO2="Support",INTEGALGO3="Support",PRIORINTEG1="4",PRIORINTEG2="5",PRIORINTEG3="6" 
查询预定义定时器。SHOW DEFPRETMR 
设置NAS消息等待时长等。SET DEFPRETMR:TIMER=201602,CURINTERVAL=50000 
设置等待S1消息响应时间。SET DEFPRETMR:TIMER=201613,CURINTERVAL=50000 
设置等待鉴权响应时间。SET DEFPRETMR:TIMER=201608,CURINTERVAL=50000 
设置NAS加密控制。SET NAS ENCRYCTRL:ENCRYPTION="Encrypt" 
Gateway选择是否考虑拓扑关系。SET PACKET DOMAIN PARAMETER:TOPOLOGY="YES" 
测试用例 :测试项目|附着流程
---|---
测试目的|UE发起附着流程。
预置条件|UE、MME、SGW、eNodeB、PGW等各网元工作正常。MME网管服务器、客户端连接正常；服务器与OMP连接正常。
测试过程|UE发起附着流程。
通过准则|附着流程成功。
测试结果|–
常见问题处理 :网管配置相关原因主要是由于OMM网管配置错误造成用户无法附着，根据原因值重点检查OMM网管配置数据，主要包括以下几个方面：用户在HSS中配置了区域限制，但在该区域之外的区域附着，附着会被拒绝。拒绝原因值为cause＝Tracking Area
not allowed。用户在网管未配置的区域内附着，附着会被拒绝。拒绝原因值为cause＝Tracking Area not allowed。用户在HSS内签约区域限制，并在签约的限制区域进行附着，但是网管安全变量配置里却设置为不支持区域签约限制，附着会被拒绝。拒绝原因值为cause＝Tracking
Area not allowed。MME对应的PLMN在HSS中配置为漫游禁止，附着时也会拒绝。拒绝原因值为cause＝PLMN not allowed。安全变量中打开或关闭IMEI流程，由于没有EIR设备，附着会被拒绝。拒绝原因值为cause＝Network failure。 
网络问题用户附着牵涉到的网元主要有无线侧的UE和eNodeB，核心网侧的MME、SGW、PGW、HSS。网络问题主要是由于MME到HSS/SGW/eNodeB/UE链路不通造成的，可以检查以下几个方面：HSS出现问题或与HSS的通讯出现异常，造成请求鉴权向量失败，附着会被拒绝。手机无响应（对鉴权请求无响应），附着会被拒绝。SGW出现问题或与SGW的通讯出现异常，造成默认承载建立失败，附着会被拒绝。 
和用户签约状况相关原因和用户签约状况相关的原因主要集中在HSS的签约数据是否正确，根据原因值重点检查用户在HSS里的签约数据
，主要包括以下几个方面：IMSI未在HLR里登记，附着会被拒绝。拒绝原因值为cause＝Illegal MS。未签约EPS业务的移动用户发起的EPS Attach，附着会被拒绝。拒绝原因值为cause＝EPS services
not allowed。在HSS客户受理端将用户报停，附着会被拒绝。拒绝原因值为cause＝Illegal MS。UE在HSS客户受理端将用户挂失，附着会被拒绝。拒绝原因值为cause＝Illegal MS。用户签约的是CAMEL用户，但是MME不支持CAMEL功能，或者支持的CAMEL功能版本过低，附着会被拒绝。拒绝原因值为cause＝PLMN
not allowed。 
其他原因对于造成用户无法附着的一些其他原因，可以主要检查以下几个方面：鉴权失败，用户鉴权算法和网络侧不一致，鉴权被拒绝，MME发送鉴权拒绝消息。对SECURITY MODE COMMAND响应不正确，安全模式失败，附着会被拒绝。由于更新HSS失败等原因造成跟踪区更新无法支持，附着会被拒绝。模块的CPU占用率超过安全变量里的过负荷控制点后，附着会被拒绝。超过容量配置里业务容量规划配置里的用户数，用户附着会被拒绝。默认承载建立不成功，失败观察报APN检查失败，用户附着会被拒绝。 
## ZUF-78-01-002 RAT内TAU 
特性描述 :特性描述 :描述 :定义 :MME网元跟踪区更新流程是用户从一个小区移动到另一个小区或从一种接入技术变成另一种接入技术时，用户重新建立连接，重新接入EPS网络的过程。
在跟踪区更新过程中，用户重新建立连接接入EPS网络，如果之前有RRC连接，RRC连接会被先断开，再重新建立RRC连接。另外，在跟踪区更新过程中，也可以把用户所有承载的E-RAB连接和空口RB连接再重新建立起来。
跟踪区更新流程完成之后，如果已经为用户把所有承载的E-RAB连接和空口RB连接重新建立了，则用户可以通过EPS网络访问数据业务和其他业务。如果没有为用户把所有承载的E-RAB连接和空口RB连接重新建立，用户可以通过业务请求过程重新建立所有承载的E-RAB连接和空口RB连接，之后用户就可以继续通过EPS网络访问数据业务和其他业务。 
应用场景 :跟踪区更新流程是基本流程，用户位置发生改变，或接入方式发生改变，或周期性位置更新定时器超时，或UE能力改变，或UE被网络侧卸载等，都会发生跟踪区更新流程。具体常见场景包括： 
用户移动到了未在网络中注册的跟踪区。 
处于ECM-IDLE态的用户，长时间驻留在网络中注册的跟踪区，周期性位置跟踪。 
UE之前在UTRAN下接入，小区重选到了E-UTRAN下的小区。 
UE之前在GERAN下接入，小区重选到了E-UTRAN下的小区。 
由于运营商对网络进行维护，把某个MME下的用户卸载，被卸载的用户会发起跟踪区更新流程注册到EPS网络的其它MME上。 
UE的能力发生改变。 
客户收益 :受益方|受益描述
---|---
运营商|保证用户在移动过程中，能继续注册到EPS网络，继续使用EPS网络访问数据业务和其他业务。
移动用户|对终端用户不可见。
实现原理 :系统架构 :EPS网络架构如下图所示。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|触发跟踪区更新流程，实现安全管理和承载管理功能。
eNodeB|对用户进行接入层安全管理，为用户选择MME，完成对用户无线资源管理功能。
MME|对用户进行接入控制和安全管理，判断SGW是否需要改变及如果改变对SGW的选择，完成用户临时标识的分配，完成TAList的分配，完成MME或SGSN的选择，完成HSS的选择，完成承载管理功能。
HSS|将用户签约数据提供给MME，存储用户目前所接入的MME信息，通知老局取消位置。
SGW|管理和存储UE的承载信息。
PGW|更新承载功能。
PCRF|根据用户接入方式和位置信息，完成IP-CAN会话修改过程。
本网元实现 :跟踪区更新属于基本业务流程，实现细节参见下面业务流程的具体描述。 
业务流程 :SGW改变的TAU流程
图2  SGW改变的TAU流程

流程说明： 
UE检测到触发TAU的条件满足，发起TAU过程。 
UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，消息中携带RRC参数（Selected
Network和old GUMMEI）。 
eNodeB从RRC参数中的old GUMMEI和指示的已选择网络参数得到MME，并向MME转发Tracking Area
Update Request消息。 
new MME通过GUTI获得old MME地址，并向old MME发送Context Request消息重新获取用户信息，消息中包括old
GUTI、MME Address、UE Validated、complete TAU Request message、P‑TMSI
Signature。 
old MME向new MME返回Context Response消息，消息包含：IMSI、IMEI、鉴权信息、EPS承载等参数。 
（可选）如果第2步完整性检查失败，则执行鉴权过程。 
new MME向old MME发送Context Acknowledge消息，old MME将SGW、PGW和HSS信息标记为不可用，从而保证当UE在本次TAU流程还未完成又发起回到old
MME的TAU流程时，old MME可以更新SGW、PGW和HSS信息。 
如果old MME在Context Response中没有返回承载上下文，new MME拒绝TAU请求。new MME根据从old
MME得到的承载上下文信息，对每个PDN连接重新选择SGW，通过Create Session Request消息通知SGW建立连接，消息中包括IMSI、bearer
contexts、MME Address and TEID for the control plane、RAT Type。 
new SGW向PGW发送Modify Bearer Request消息，其中包含Serving GW Address
and TEID、RAT type、Serving Network等信息。 
（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发起IP-CAN修改流程，把RAT
type等变化的信息发送给PCRF。 
PGW更新相关的承载上下文，并向new SGW返回Modify Bearer Response消息。 
new SGW更新承载上下文，并向new MME返回Create Session Response消息。消息中包括Serving
GW address and TEID for uplink traffic、MS Info Change Reporting Action。 
new MME向HSS发送Update Location Request消息告知其MME已变更，消息包含：MME ID、IMSI、ULR-Flags、MME
Capabilities。 
HSS向old MME发送Cancel Location消息，消息包含：IMSI、Cancellation type，Cancellation
type设置为Update Procedure。 
如果第4步中的定时器超时，old MME删除MM和承载上下文信息，否则需要等待定时器超时后再删除上下文。目的是为了防止用户在本次TAU过程未完成时又发起了新的TAU过程时，old
MME仍保留着MM上下文。上下文删除后，old MME向HSS响应Cancel Location Ack消息，消息包含：IMSI。 
HSS向new MME发送Update Location Ack，消息中包括IMSI、Subscription Data。 
当第4步的定时器超时时，old MME释放本地承载资源，并向old SGW发送Delete Session Request消息告知其释放承载资源。消息中包括Cause。 
old SGW向old MME返回Delete Session Response消息并丢弃为UE所缓存的所有数据包。 
new MME向UE发送Tracking Area Update Accept消息，消息中包括GUTI、TAI-list、EPS
bearer status等。 
（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking Area
Update Complete消息确认接收到了Tracking Area Update Accept消息。 
SGW没有改变的TAU流程
图3  SGW没有改变的TAU流程

流程说明： 
UE检测到触发TAU的条件满足，发起TAU过程。 
UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，消息中携带RRC参数（Selected
Network和old GUMMEI）。 
eNodeB从RRC参数中的老的GUMMEI和指示的已选择网络参数得到MME，并向MME转发Tracking Area
Update Request消息。 
new MME通过GUTI获得old MME地址，并向old MME发送Context Request消息重新获取用户信息，消息中包括old
GUTI、MME Address、UE Validated、complete TAU Request message、P‑TMSI
Signature。 
old MME向new MME返回Context Response消息，消息包含：IMSI、IMEI、鉴权信息、EPS承载等参数。 
（可选）如果第2步完整性检查失败，则执行鉴权过程。 
new MME向old MME发送Context Acknowledge消息，old MME将SGW、PGW和HSS信息标记为不可用，从而保证当UE在本次TAU流程还未完成又发起回到old
MME的TAU流程时，old MME可以更新SGW、PGW和HSS信息。 
如果old MME在Context Response中没有返回承载上下文，new MME拒绝TAU请求。new MME根据从old
MME得到的承载上下文信息，对每个PDN连接的SGW发送Modify Bearer Request消息，通知其更新承载信息，消息中包括new
MME address 和 TEID、RAT type。 
（可选）如果Modify bearer request消息携带的RAT type发生了变化，或者消息中携带有User
Location Information或UE Time Zone IE，SGW向PGW发送Modify Bearer Request消息。 
（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW将发起IP-CAN修改流程，把RAT type等变化的信息发送给PCRF。 
（可选）PGW更新相关的承载上下文，并向SGW返回Modify Bearer Response消息。 
SGW更新承载上下文，并向new MME返回Create Session Response消息。消息中包括Serving
GW address and TEID for uplink traffic、MS Info Change Reporting Action。 
new MME向HSS发送Update Location Request消息告知其MME已变更，消息包含：MME Id、IMSI、ULR-Flags、MME
Capabilities。 
HSS向old MME发送Cancel Location消息，消息包含：IMSI、Cancellation type，Cancellation
type设置为Update Procedure。 
如果第4步中的定时器超时，old MME删除MM和承载上下文信息，否则需要等待定时器超时后再删除上下文。目的是为了防止用户在本次TAU过程未完成时又发起了新的TAU过程时，old
MME仍保留着MM上下文。上下文删除后，old MME向HSS响应Cancel Location Ack消息，消息包含：IMSI。 
HSS向新的MME发送Update Location Ack，消息中包括IMSI、Subscription Data。 
new MME向UE发送Tracking Area Update Accept消息，消息中包括GUTI、TAI-list、EPS
bearer status等。 
（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking Area
Update Complete消息确认接收到了Tracking Area Update Accept消息。 
系统影响 :随着用户跟踪区更新的增加，系统资源占用会增大，CPU占用率会相应上升。 
应用限制 :该特性不涉及应用限制。 
特性交互 :由于跟踪区更新流程是基本业务流程，保证用户在移动过程中能继续注册到EPS网络，继续使用EPS网络访问数据业务和其他业务。如果跟踪区更新失败，则用户在移动过程中，不能继续通过EPS网络访问数据业务和其他业务，严重影响到用户使用数据业务和其他业务的体验。 
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"
3GPP TS 23.203: "Policy and charging control architecture"
3GPP TS 23.003: "Numbering, addressing and identification"
3GPP TS 24.007: "Mobile radio interface signalling layer3; General aspects"
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS|PCRF
---|---|---|---|---|---|---
√|√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :该特性不涉及命令的变化。 
性能统计 :测量类型|描述
---|---
跟踪区更新流程测量|编号为43001开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现TAU流程。 
调整特性 :配置TAU鉴权控制策略。设置默认策略：SET MME IMSI AUTH DEFAULT:SERVICETYPE="IERTAUIRARAT",AUTHTYPE="Frequency",AUTHTIMES=5,AUTHSELNUM=2根据IMSI号段配置策略：ADD MME IMSI AUTH:IMSI="4601199",SERVICETYPE="IERTAUIRARAT",AUTHTYPE="Frequency",AUTHTIMES=5,AUTHSELNUM=1 
配置MME本局支持的完整性保护算法。SET NAS INTEGCTRL:INTEGALGO1="Support",INTEGALGO2="Support",INTEGALGO3="Support",PRIORINTEG1="4",PRIORINTEG2="5",PRIORINTEG3="6" 
查询预定义定时器。SHOW DEFPRETMR 
设置NAS消息等待时长等。SET DEFPRETMR:TIMER=201602,CURINTERVAL=50000 
设置S1消息响应时间。SET DEFPRETMR:TIMER=201613,CURINTERVAL=50000 
设置鉴权响应时间。SET DEFPRETMR:TIMER=201608,CURINTERVAL=50000 
设置NAS加密控制。SET NAS ENCRYCTRL:ENCRYPTION="Encrypt" 
测试用例 :测试项目|RAT内TAU
---|---
测试目的|RAT内TAU流程
预置条件|UE、MME、SGW、eNodeB、PGW等各网元工作正常。MME网管服务器、客户端连接正常；服务器与OMP连接正常。UE附着成功。
测试过程|UE发起跟踪区更新流程。
通过准则|TAU流程成功。
测试结果|–
常见问题处理 :无。 
## ZUF-78-01-003 跨RAT TAU 
特性描述 :特性描述 :描述 :定义 :MME的跨RAT流程，指的是当UE从2/3G无线接入进入LTE无线接入，或者从LTE无线接入进入2/3G无线接入时，所涉及的附着、跟踪区/路由区更新、切换以及RIM流程。
背景知识 :3GPP的无线接入技术（RAT），经历了2G时代的GSM EDGE无线接入（GERAN）、3G时代的通用陆基无线接入（UTRAN）和LTE时代的演进的通用陆基无线接入（E-UTARN）三个阶段。在LTE网络的发展过程中，LTE将与2/3G并存，且有着不同的无线覆盖。如果LTE用户同时签约了2/3G业务，在LTE和2/3G覆盖之间移动，为了保证用户业务的延续性，则需要实现跨RAT的相关流程。 
跨RAT的方式
从无线侧的角度来讲，根据终端和网络的不同能力，以及终端当前所处的状态，实现跨RAT，有小区重选、小区重定向、小区改变指令（CCO）（包括网络辅助的小区改变NACC）和切换等不同的形式。涉及到MME的主要流程包括跟踪区/路由区更新和切换流程；其中NACC还涉及到使用核心网的RIM流程，用来传递对端无线节点系统信息；另外，在跟踪区更新过程中，如果用户没有承载或者无法在LTE下重建承载，跟踪区更新将失败，UE将采用重新附着的方式接入LTE网络。 
TAU/RAU方式和HO方式的比较参见下表。 
类型|TAU/RAU|HO
---|---|---
UE状态|空闲态或连接态—空闲态|连接态—连接态
空口互操作类型|小区重选/小区重定向/CCO/CCOwith NACC|切换
数据传输|可以有数据传输，但过程中数据传输会中断。|可以有数据传输，且数据传输不会中断。
适用上层业务类型|对PS业务无连续性要求的业务，例如CSFB、即时消息、下载等；对于转换时延有要求业务（如CSFB）的需要使用RIM流程。|对PS业务有连续性要求的业务，例如VoIP、流媒体等。
跨RAT的关键参数映射
用户临时标识的映射在2/3G网络，SGSN为UE分配的是临时标识是P-TMSI，而在LTE，MME为UE分配的临时标识是GUTI；所以UE在接入到目标网络的时候，就需要将之前网络分配的临时标识，转换为目标网络需要的格式。 
QoS参数的映射包括EPS Qos到Pre-R8 Qos的映射、Pre-R8 Qos到EPS Qos的映射。 
网元地址解析
对SGSN来说，采用的是GPRS的域名格式，使用A或AAAA来解析GGSN和目标或源SGSN。而对MME网元来说，采用的是EPC的域名格式，使用S-NAPTR过程来解析SGW、PGW、目标或源SGSN、目标或源MME和MSCVLR地址。 
跨RAT流程中，涉及的DNS域名解析和域名格式参见下表。 
GPRS域名格式|EPC域名格式
---|---
rncXXXX.mncYYY.mccZZZ.gprs|rnc<RNC>.rnc.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org
—|tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.tac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org
—|enb<eNodeB-ID.enb.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org
racYYYY.lacZZZZ.mnc001.mcc460.gprsnriXXXX.racYYYY.lacZZZZ.mnc001.mcc460.gprs|rac<RAC>.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.orgnri-sgsn<NRI>.rac<RAC>.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org
当SGSN不识别eNB时，源RNC将使用RNC ID来标识目标eNB。这样SGSN只需要根据RNC
ID来解析目标MME的地址，由目标MME将RNC ID映射为eNB ID。SGSN/MME支持扩展RNC ID。 
当SGSN识别eNB时，源RNC将使用eNB
ID来识别目标eNB。这样SGSN需要根据目标TA或目标eNB ID来解析目标MME的地址，由SGSN将eNB ID映射为RNC ID带给目标MME，目标MME再将RNC
ID映射回eNB ID。SGSN/MME支持扩展RNC ID。 
MME收到TAU消息后，判断出GUTI是由P-TMSI+RAI映射而来的，则反向映射获取P-TMSI+RAI，从而解析出老局SGSN的地址。 
PGW的锚定
EPC网络中的PGW具备内嵌GGSN的功能，所以在跨RAT的场景下，只要当SGSN选择的是PGW内嵌的GGSN，PGW就可以作为跨RAT的锚定点，从而保证用户业务的连续性。 
当网络中同时存在GGSN和PGW的场景下，考虑到负荷均衡，需要SGSN能够识别用户的LTE属性，只针对该类用户选择PGW，而其他普通的2/3G用户仍然选择GGSN。 
应用场景 :跨RAT流程主要应用于运营商新建的EPS网络需要和原有的GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。网络中的GGSN升级为PGW，HLR升级为HSS。
根据终端和网络的不同能力和状态以及不同业务场景的需要，跨RAT可能采用不同的方式，所涉及的MME的业务场景包括： 
3G到LTE的切换 
LTE到3G的切换 
2/3G到LTE的RIM 
2/3G到LTE的TAU 
LTE到2/3G的RIM 
LTE到2/3G的RAU 
客户收益 :受益方|受益描述
---|---
运营商|支持跨RAT流程，可以保证用户在不同RAT之间移动过程中业务的连续性，保证用户的业务体验，可以极大的增强用户对EPS网络使用的满意度。
移动用户|用户在移动的过程中，保证用户在不同RAT间的业务连续性。
实现原理 :系统架构 :在核心网方面，由Gn/Gp SGSN负责2/3G接入，而由MME负责LTE接入。跨RAT流程实际上涵盖了所有的Gn/Gp
SGSN和MME的交互流程。 
MME和Gn/Gp SGSN互通架构如[图1]所示。
图1  MME和Gn/Gp SGSN互通架构图

Gn/Gp SGSN负责传统的2/3G接入，与MME和HSS之间的接口也是基于GTP的Gn口和基于MAP的Gr口。在跨RAT流程中，对于Gn/Gp
SGSN并不需要识别出对接的网元是MME。 
涉及的网元 :跨RAT功能涉及UE、eNodeB、MME、SGW、PGW、SGSN、HSS和PCRF网元。 
网元|作用
---|---
UE|跨RAT流程触发，完成安全功能、承载管理、RRC连接和RAB连接的切换等功能。
eNodeB|为UE终端提供无线资源，进行接入层安全功能，完成MME的选择、用户无线资源管理、切换发起的决策和执行等功能。
MME|负责管理和存储UE相关信息，处理MME和UE之间的所有非接入层消息，对用户进行接入控制和安全功能，完成SGW的选择、用户临时标识的分配、TA List的分配，完成SGSN的选择，HSS的选择、承载管理等功能。
SGW|管理和存储UE的承载信息，进行非直接前转数据的转发。
PGW|完成更新承载的功能。
SGSN|负责管理和存储UE相关信息，为用户分配临时标识，完成用户安全功能，完成用户移动性管理功能和会话管理功能，处理SGSN和UE之间的所有非接入层消息。
RNC|为终端接入提供无线资源，完成LTE邻区的切换发起和消息处理，对无线承载资源的建立和删除等。
HSS|主要完成用户的签约数据插入和管理。
PCRF|根据用户接入方式和位置信息，完成IP-CAN会话修改过程。
业务流程 :TAU的流程参见“跟踪区更新流程”。
切换流程参见“切换管理”。
跨RAT跟踪区更新
跨RAT跟踪区更新流程如[图2]所示。
图2  跨RAT跟踪区更新流程

流程说明： 
UE从UTRAN覆盖区域移动到EUTRAN强信号覆盖区域，UE选择4G网络。UE检测到触发TAU的条件满足，UE发起TAU过程。 
UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，同时携带RRC参数指示所选择的网络以及old
GUMMEI，其中old GUMMEI的值从old GUTI中取得。由于UE之前在2G/3G网络，所以UE将保存的SGSN分配old
P-TMSI和old RAI映射为old GUTI。
eNodeB从RRC参数中的old GUMMEI和指示的已选择网络参数得到MME。如果不能得到MME，eNodeB就选择一个MME。eNodeB转发Tracking Area Update Request消息到new MME，并携带一个TAI+ECGI参数和所选择网络。
新的MME通过old RAI和old P-TMSI获取old SGSN，并发送SGSN Context Request消息给Gn/Gp
SGSN以请求用户的移动性管理和会话管理相关信息，消息包含：old RAI、P-TMSI、old P-TMSI Signature、new
MME Address。 
Gn/Gp SGSN给new MME回SGSN Context Response消息，消息包含：MM Context、PDP
Contexts。 
（可选）UE、MME和HSS可以完成鉴权和安全功能。如果TAU请求消息的完整性检查失败，鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 
new MME给Gn/Gp SGSN发送SGSN Context Acknowledge消息。通知Gn/Gp
SGSN，new MME准备好接收已激活的PDP上下文的数据包。
Gn/Gp SGSN将UE上下文中的GW网关和HSS相关信息标记为无效。其目的是如果此TAU过程未完成而发生一个新的RAU过程回退到Gn/Gp
SGSN时Gn/Gp SGSN能够更新GW网关和HSS。 
如果安全过程不能正确认证UE，必须拒绝TAU请求，并且new
MME向Gn/Gp SGSN发送拒绝指示。Gn/Gp SGSN继续服务UE。 
new MME完成PDP上下文到EPS承载的一对一映射，以及QoS参数的映射，建立EPS承载，并去活无法创建的EPS承载。MME根据从UE所接收到的EPS承载状态与从SGSN接收的承载上下文进行验证。MME将释放UE中非激活EPS承载的任何网络资源。如果根本就没有承载上下文，则MME拒绝TAU请求消息。 
new MME为每个PDN连接选择一个SGW，并向其发送Create Session Request消息，消息包含：IMSI、MME
Address and TEID、PDN GW address and TEID、EPS Bearer QoS、serving network
identity等信元。 
new SGW向PGW发送Modify Bearer Request消息，其中包含SGW Address and TEID、RAT
type、Serving Network等信息。 
PGW更新相关的承载上下文，并向new SGW返回Modify Bearer Response消息。  
（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发送CCR-U消息，发起IP-CAN修改流程，把RAT
type等变化的信息发送给PCRF。 
SGW更新了承载上下文后，回复Create Session Response消息给MME，消息中包括SGW
address and TEID, MS Info Change Reporting Action) at the PDN GW(s)
for uplink traffic。
new MME给HSS发送Update Location Request消息，携带单注册指示，以便Gn/Gp SGSN上的用户资源能够被删除。（单注册是指，只能同时在MME和SGSN一个局上注册） 
（可选）如果UE曾经在LTE注册过，且MME发生改变，则HSS发送Cancel Location消息给old MME，消息包含：IMSI、Cancellation
type，Cancellation type设置为Update Procedure。 
（可选）old MME删除移动性管理上下文。old MME发送Cancel Location Ack消息给HSS。 
HSS发送Cancel Location消息给Gn/Gp SGSN， Gn/Gp SGSN删除移动性管理上下文，消息包含：IMSI、Cancellation
type。Gn/Gp SGSN删除上下文。
（可选） Gn/Gp SGSN收到取消位置信息，如果用户的Iu连接也存在，则发送Iu Release Command消息给RNC。
（可选）当数据转发定时器超时，RNC向Gn/Gp SGSN响应Iu Release Complete消息。
Gn/Gp SGSN向HSS响应Cancel Location Ack消息，消息包含：IMSI。
HSS给new MME回Update Location Ack消息。如果更新位置请求被HSS拒绝，则MME拒绝来自UE的TAU请求并说明原因。如果所有检查通过，MME构造UE的移动性管理上下文。 
MME发送Tracking Area Update Accept消息给UE。如果分配了新的GUTI，则会在TAU接受消息中携带。 
如果在TAU接受消息中携带了GUTI，UE发送Tracking Area Update Complete确认接收到了TAU接受消息。如果在TAU请求消息没有携带“激活标识”，并且也不是ECM-CONNECTED态下发起的TAU过程，MME释放信令连接。 
如果映射的QoS参数与UE当前签约的QoS参数不一致，则MME发起签约QoS修改流程。 
跨RAT路由区更新
跨RAT路由区更新流程参见[图3]。
图3  跨RAT路由区更新

流程说明： 
UE从EUTRAN覆盖区域移动到UTRAN或GERAN强信号覆盖区域，UE选择3G或2G网络。 
UE 向new SGSN发送Routing Area Update Request消息，消息中携带的old
P‑TMSI、old RAI和old P‑TMSI由GUTI映射得到。
new SGSN发送SGSN Context Request消息给old MME以请求用户的移动性管理和会话管理相关信息。由GUTI映射的old
RAI和old P-TMSI可以唯一标识old MME。 
old MME给new SGSN回SGSN Context Response消息。对于new SGSN来说，并不需要识别老局是否是MME。 
由MME会将EPS承载按一对一映射到PDP上下文，同时也会完成QoS参数的映射。 
（可选）如果SGSN Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。 
new SGSN向old MME发送SGSN Context Acknowledge消息。 old MME将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还在进行中，UE向old
MME发起TAU流程时，old MME对GW和HSS的信息进行更新。 
new SGSN发送Update PDP Context Request消息到每个PDP上下文关联的PGW（内嵌GGSN）。
PGW更新PDP上下文中的对端用户面地址信息及QoS等，并向new SGSN返回Update PDP Context
Response消息。
New SGSN发送Update Location Request消息到HSS，指示为普通更新。
（可选）如果HSS有其他SGSN的注册信息，则发送Cancel Location消息到old SGSN，
Cancellation Type设置为Update Procedure。
（可选）old SGSN删除MM和PDP上下文，返回Cancel Location Ack消息给HSS。
HLR发送Insert Subscriber Data消息到new SGSN，带用户签约信息等。
new SGSN返回Insert Subscriber Data Ack消息到HSS。
HSS发送Update Location Ack消息到new SGSN。
New SGSN发送Routing Area Update Accept消息到UE，携带新分配的P-TMSI。
UE发现P-TMSI被重新分配，发送Routing Area Update Complete消息到new
SGSN。
old MME根据SGSN Context Request知道是UE移动到UTRAN，释放eNodeB侧和SGW侧资源，并向SGW发送Delete
Session Request消息告知其释放EPS承载资源，指示SGW不要向PGW发起承载删除流程。 
SGW向old MME响应Delete Session Response消息。 
（可选）如果old MME与UE之间有S1-MME连接，当收到new SGSN发送的SGSN Context Acknowledge消息，old
MME执行S1-AP Release。
RIM
RIM的流程如[图4]所示。
图4  RIM流程

流程说明： 
MME收到S1口eNodeB发过来的S1AP层的RIM消息，解析目的路由地址，转换为Gn接口的RIM消息后发往目的RAN节点归属的SGSN。 
SGSN收到Gn口的 RIM消息，解析目的路由地址为本局管理的RAN节点，转换为对应接口的RIM消息发往目的RAN节点。 
SGSN收到Gb/Iu口BSS/RNC发过来的BSSGP/RANAP层的RIM消息，解析目的路由地址。 
SGSN转换为Gn接口的RIM消息后发往目的RAN节点归属的MME。 
MME收到Gn口的 RIM消息，解析目的路由地址为本局管理的eNodeB，转换为对应接口的RIM消息发往目的eNodeB。 
系统影响 :随着用户跨RAT的增加，系统资源占用会增大，CPU占用率会相应上升。在进行配置计算时，话务模型需要给出具体的跨RAT的话务量，以便正确计入跨RAT对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
". 
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved
Packet System (EPS); Stage 3". 
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network
(E-UTRAN); S1 Application Protocol (S1AP)". 
3GPP TS 29.274: "General Packet Radio Service (GPRS); Evolved
GPRS Tunnelling Protocol (eGTP) for EPS". 
3GPP TS 29.272: " Mobility Management Entity (MME) and Serving
GPRS Support Node (SGSN) related interfaces based on Diameter protocol". 
3GPP TS 23.003: "Numbering, addressing and identification". 
特性能力 :跨RAT流程是完成接入用户在不同RAT之间移动过程中保证业务连续性的过程，跨RAT流程会把接入用户的资源，包括承载，切换到目的无线接入网络。 
MME支持最大1500万用户接入，支持最大3000万承载。 
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS|SGSN
---|---|---|---|---|---
-|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
支持跨RAT流程，需要RNC和eNB支持跨RAT切换和跨RAT小区重选等功能。需要在HSS支持用户同时签约2/3G和LTE业务的能力，以及满足不同RAT之间的管理能力。DNS需要增加相应的SGSN和MME的记录。PGW支持内嵌GGSN功能与SGSN互通。 
工程规划要求 :RNC的切换数据规划和配置。RNC需要根据无线规划和区域覆盖，进行LTE邻接小区的规划和配置。 
eNB的切换数据规划和配置。eNB需要根据无线规划和区域覆盖，进行3G邻接小区的规划和配置。 
RNC ID与eNB ID以及TAI和RAI的映射规划和配置。当SGSN不识别eNB时，需要统一规划目标eNB
ID、TAI与切换消息中目标ID的RNC ID、RAI的映射规则，对RNC和MME进行协同配置；当SGSN识别eNB时，需要统一规划无线切换消息中目标ID的eNB、TAI到Gn口切换消息中目标ID的RNC
ID、RAI的SGSN映射规则，以及Gn口切换消息中目标ID的RNC ID、RAI再到目标eNB ID、TAI的MME映射规则，对RNC、SGSN和MME进行协同配置。 
SGSN和MME的DNS解析地址数据规划和配置。在GPRS和EPC的DNS系统中，规划和配置相应的SGSN和MME地址解析数据。 
PGW的DNS解析地址数据规划和配置。在GPRS和EPC的DNS系统中，规划和配置APN解析PGW的数据，配置GW选择。 
SGSN的LAI、NRI和MME的MMEC、MMEGI规划配置。需要保证规划的LAC和MMEGI不重复，保证NRI和MMEC的特定关系，满足不同组网情况下，跨RAT是选择SGSN和MME的负荷均衡。 
O&M相关 :命令 :配置项新增命令配置项参见表1。表1  新增配置项配置项命令eNB和RNC之间的标识映射配置ADD ENB RNCSET ENB RNCDEL ENB RNCSHOW ENB RNCTAI和RAI之间的映射配置ADD TAI RAISET TAI RAIDEL TAI RAISHOW TAI RAIEPC地址解析配置ADD EPCHOSTSET EPCHOSTADD EPCHOST IPADDRDEL EPCHOST IPADDRDEL EPCHOSTSHOW EPCHOSTGPRS地址解析配置ADD SGSNHOSTSET SGSNHOSTADD SGSNHOST IPADDRDEL SGSNHOST IPADDRDEL SGSNHOSTSHOW SGSNHOST 
安全变量表2  新增安全变量安全变量命令ARP高优先级权重值SET PACKET DOMAIN PARAMETER:ARPHIGHPRIORITY=2,ARPMEDPRIORITY=6ARP中优先级权重值切换中MME支持非直接数据前转SET PACKET DOMAIN PARAMETER:MMEUNDIRECTFWD="YES" 
软件参数表3  新增软件参数软件参数ID软件参数名称65619SGSN支持标准eNB-ID逻辑域名解析65659支持扩展RNC-ID786683SGSN支持Target eNB-ID786684支持根据RA识别RNC65617MME支持RIM RNC-ID解析262283MME RIM流程获取目标SGSN IP时采用的域名格式65542SGSN是否支持RIM功能65569SGSN支持标准eNB-ID解析 
性能统计 :测量类型|描述
---|---
切换流程测量|C430110009 E-UTRAN到UTRAN局间切出请求次数
C430110010 E-UTRAN到UTRAN局间切出成功次数|切换流程测量
C430110011 UTRAN到E-UTRAN局间切入请求次数|切换流程测量
C430110012 UTRAN到E-UTRAN局间切入成功次数|切换流程测量
DNS测量|C430170025 切换时发起的DNS解析请求次数
C430170026 切换时由于域名错误导致DNS解析失败次数|DNS测量
C430170027 切换时由于服务器原因导致DNS解析失败次数|DNS测量
C430170028 切换时由于内部原因导致DNS解析失败次数|DNS测量
SGSN重定位测量|编号为C40511开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME支持跨RAT功能，需要配置跨RAT相关数据。 
配置前提 :eNodeB已与MME对接成功，相应TAI-FQDN解析完成，4G下能附着成功。 
BSC/RNC已与SGSN对接成功，相应APN-FQDN解析完成，2G/3G下能附着、激活。 
如果MME Group ID最高位为1，LAC最高位不为1，网元不支持“特定MME/SGSN选择方式”。如果网元支持“特定MME/SGSN选择方式”则RAU或TAU时的域名解析可能为GPRS/EPC格式。 
RNC/BSC与eNodeB无线网元之间的重选、切换配置均已完成。 
配置过程 :配置3G到4G的TAU信息。 
在DNS服务器上配置old RAI解析到SGSN的GTPC地址。 
配置4G到3G的RAU信息。在SGSN网元上配置MME地址解析。 
配置3G到4G的切换（Relocation Required携带Target RNC-ID）信息。 
配置切换目标地址解析 
配置eNB和和RNC之间的标识映射 
配置TAI和RAI之间的映射 
（可选）配置支持扩展RNC-ID。 
配置3G到4G的切换（Relocation Required携带Target eNB-ID）信息。 
配置eNB和和RNC之间的标识映射。 
配置TAI和RAI之间的映射。 
SGSN支持Target eNB-ID。 
SGSN支持标准eNB-ID逻辑域名解析，使用TAI解析目标MME。 
在DNS服务器上配置TAI-FQDN或eNB-FQDN解析到MME的GTPC地址。 
（可选）SGSN配置支持扩展RNC-ID。 
配置4G到3G的切换信息。 
在DNS服务器上配置RNC ID解析到SGSN的GTPC地址。 
配置3G到4G的RIM信息。 
配置SGSN支持RIM。 
配置SGSN支持3G到4G的RIM。 
配置MME地址域名解析格式为TA FQDN格式。 
DNS根据TAI FQDN解析到MME的GTPC地址。 
配置4G到3G的RIM信息。 
配置MME支持4G到3G的RIM。 
配置使用EPS格式的RNC ID FQDN解析SGSN地址。 
DNS根据RNCID FQDN解析到SGSN的GTPC地址。 
配置SGSN支持RIM。 
配置2G到4G的RIM信息。 
配置SGSN支持RIM。 
配置SGSN支持2G到4G的RIM。 
配置MME地址域名解析格式为TA FQDN格式。 
DNS根据TAI FQDN解析到MME的GTPC地址。 
配置4G到2G的RIM信息。 
配置使用EPS格式的RAI FQDN解析SGSN地址。 
DNS根据RAI FQDN解析到SGSN的GTPC地址。 
配置SGSN支持RIM。 
配置实例 :###### 3G到4G的TAU 
用户从SGSN下TAU至MME，用户在SGSN下的LAC为1001(十六进制)，RAC为01，PLMN为46011。 
在DNS服务器上配置old RAI解析到SGSN的GTPC地址： 
配置ZONE 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460 
`$TTL 3600
@  IN  SOA  jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
                    2013072800  ;Serial
                    3600  ;Refresh
                    900    ;Retry
                    604800  ;Expire
                    3600 )  ;Minimum
  IN  NS  jsdns1.mnc011.mcc460. 3gppnetwork.org.
  IN  NS  jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp  replacement 
$ORIGIN rac.epc.mnc011.mcc460.3gppnetwork.org.
rac0001.lac1001  IN   NAPTR  100    100    "a"   "x-3gpp-sgsn:x-gn:x-gp"   ""
    sgsn01.rac.epc.mnc011.mcc460.3gppnetwork.org.
sgsn01       IN    A    1.1.1.1` 
###### 4G到3G的RAU 
在SGSN网元上配置MME地址解析，逻辑名称为rac0001.lac8001.mnc011.mcc460.gprs，IP地址为2.2.2.2。 
[ADD SGSNHOST]:NAME="rac0001.lac8001.mnc011.mcc460.gprs",IPADDR="2.2.2.2"
###### 3G到4G的切换-Relocation Required携带Target RNC-ID 
RNC发起切换要求的Relocation Required消息中携带Target RNC-ID参数，其中RNC ID值为真实eNodeB
ID映射的虚拟值；RAI值为真实TAI映射的虚拟值。 eNodeB ID值为12345（十进制），RNC-ID为100(十进制)，PLMN为46011
TAC为8001（十六进制），LAC为1001（十六进制），RAC为01（十六进制） 
配置切换目标地址解析。 
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME；不使用本地解析的情况下，则在DNS服务器上进行配置域名解析。 
[ADD SGSNHOST]:NAME="rnc0064.mnc011.mcc460.gprs",IPADDR="2.2.2.2"
配置eNB和和RNC之间的标识映射。 
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME。 
[ADD ENB RNC]:MCC="460",MNC="11",RNC=100,ENB=12345
配置TAI和RAI之间的映射。 
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME。 
[ADD TAI RAI]:MCC="460",MNC="11",LAC="1001",RAC="01",TAC="8001"
（可选）SGSN配置支持扩展RNC-ID。 
[SET SOFTWARE PARAMETER]:PARAID=65659,PARAVALUE=1
 说明： 
在映射的RNC-ID不大于4095时，可不用配置。 
###### 3G到4G的切换-Relocation Required携带Target eNB-ID 
RNC发起切换要求的Relocation Required消息中携带Target eNB-ID参数，eNodeB ID值为123456（十进制），TAC为8001（十六进制），PLMN为46011
规划一个RNC ID值为真实eNodeB ID映射的虚拟值。 
RAI值为真实TAI映射的虚拟值： eNodeB ID值为123456（十进制），RNC-ID为100(十进制)，TAC为8001（十六进制），LAC为1001（十六进制），RAC为01（十六进制）。 
配置eNB和和RNC之间的标识映射。 
[ADD ENB RNC]:MCC="460",MNC="11",RNC=100,ENB=123456
配置TAI和RAI之间的映射。 
[ADD TAI RAI]:MCC="460",MNC="11",LAC="1001",RAC="01",TAC="8001"
SGSN支持Target eNB-ID。 
[SET SOFTWARE PARAMETER]:PARAID=786683,PARAVALUE=1
SGSN支持标准eNB-ID逻辑域名解析，使用TAI解析目标MME。 
[SET SOFTWARE
PARAMETER]:PARAID=65619,PARAVALUE=0
在DNS服务器上配置TAI-FQDN或eNB-FQDN解析到MME的GTPC地址。 
配置ZONE 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460 
`$TTL 3600
@	IN	SOA	 jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc011.mcc460. 3gppnetwork.org.
	IN	NS	jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp 	replacement 
$ORIGIN tac.epc.mnc011.mcc460.3gppnetwork.org.
tac-lb01.tac-hb80  IN   NAPTR  100   100    "a"   x-3gpp-mme:x-gn:x-gp"   "" 
	 mme01.tac.epc.mnc011.mcc460.3gppnetwork.org.
mme01     	IN	  A	  2.2.2.2
$ORIGIN enb.epc.mnc011.mcc460.3gppnetwork.org.
enb1e240  IN   NAPTR  100   100    "a"   x-3gpp-mme:x-gn:x-gp"   "" 
	 mme01.enb.epc.mnc011.mcc460.3gppnetwork.org.
mme01     	IN	  A	  2.2.2.2
` 
（可选）SGSN配置支持扩展RNC-ID。 
[SET SOFTWARE PARAMETER]:PARAID=65659,PARAVALUE=1
 说明： 
在映射的RNC-ID不大于4095时，可不用配置。 
###### 4G到3G的切换 
用户从MME下切换至SGSN，目标RNCID为200。 
在DNS服务器上配置RNC ID解析到SGSN的GTPC地址： 
配置ZONE。 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460。 
`$TTL 3600
@	IN	SOA	 jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc011.mcc460. 3gppnetwork.org.
	IN	NS	jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp 	replacement 
$ORIGIN rnc.epc.mnc011.mcc460.3gppnetwork.org.
rnc00c8  IN   NAPTR  100    100    "a"   "x-3gpp-sgsn:x-gn:x-gp"   "" 
	 sgsn01.rnc.epc.mnc011.mcc460.3gppnetwork.org.
sgsn01     	IN	  A	  1.1.1.2` 
###### 3G到4G的RIM 
RNC发起3G到4G的RIM流程，携带Target ID为目标eNodeB
ID，SGSN使用TA构造FQDN解析MME地址。eNodeB ID值为12345（十进制），TAC为8001（十六进制），PLMN为46011。 
配置SGSN支持RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65542,PARAVALUE=1
配置SGSN支持3G到4G的RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65569,PARAVALUE=3
配置MME地址域名解析格式为TA FQDN格式。 
[SET SOFTWARE PARAMETER]:PARAID=65619,PARAVALUE=0
DNS根据TAI FQDN解析到MME的GTPC地址。 
配置ZONE。 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460。 
`$TTL 3600
@	IN	SOA	 jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc011.mcc460. 3gppnetwork.org.
	IN	NS	jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp 	replacement 
$ORIGIN tac.epc.mnc011.mcc460.3gppnetwork.org.
tac-lb01.tac-hb80  IN   NAPTR  100    100    "a"  "x-3gpp-mme:x-gn:x-gp"   ""
 	 mme01.tac.epc.mnc011.mcc460.3gppnetwork.org.
mme01     	IN	  A	  1.1.1.3` 
###### 4G到3G的RIM 
eNodeB发起4G到3G的RIM流程，携带Target ID为目标RNC
ID，MME使用RNC ID的EPS域名格式解析SGSN地址。RNCID为200（十进制），PLMN为46011。 
配置MME支持4G到3G的RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65617,PARAVALUE=1
配置使用EPS格式的RNC ID FQDN解析SGSN地址。 
[SET SOFTWARE
PARAMETER]:PARAID=262283,PARAVALUE=1
DNS根据RNCID FQDN解析到SGSN的GTPC地址。 
配置ZONE。 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460。 
`$TTL 3600
@	IN	SOA	 jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc011.mcc460. 3gppnetwork.org.
	IN	NS	jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp 	replacement 
$ORIGIN rnc.epc.mnc011.mcc460.3gppnetwork.org.
rnc00c8  IN   NAPTR  100    100    "a"  "x-3gpp-sgsn:x-gn:x-gp"   "" 
	 sgsn01.rnc.epc.mnc011.mcc460.3gppnetwork.org.
sgsn01     	IN	  A	  1.1.1.4` 
配置SGSN支持RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65542,PARAVALUE=1
###### 2G到4G的RIM 
BSC发起2G到4G的RIM流程，携带Target ID为目标eNodeB
ID，SGSN使用TA构造FQDN解析MME地址。eNodeB ID值为12345（十进制），TAC为8001（十六进制），PLMN为46011。 
配置SGSN支持RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65542,PARAVALUE=1
配置SGSN支持2G到4G的RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65569,PARAVALUE=3
配置MME地址域名解析格式为TA FQDN格式。 
[SET SOFTWARE PARAMETER]:PARAID=65619,PARAVALUE=0
DNS根据TAI FQDN解析到MME的GTPC地址。 
配置ZONE 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460 
`$TTL 3600
@	IN	SOA	 jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc011.mcc460. 3gppnetwork.org.
	IN	NS	jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp 	replacement 
$ORIGIN tac.epc.mnc011.mcc460.3gppnetwork.org.
tac-lb01.tac-hb80  IN   NAPTR  100    100    "a"  "x-3gpp-mme:x-gn:x-gp"   "" 
	 mme01.tac.epc.mnc011.mcc460.3gppnetwork.org.
mme01     	IN	  A	  1.1.1.5
` 
###### 4G到2G的RIM 
eNodeB发起4G到2G的RIM流程，携带Target ID为目标Cell
ID，MME使用RAI的EPS域名格式解析SGSN地址。LAC为1001（十六进制），RAC为01（十六进制）。 
配置使用EPS格式的RAI FQDN解析SGSN地址。 
[SET SOFTWARE PARAMETER]:PARAID=262283,PARAVALUE=1
DNS根据RAI FQDN解析到SGSN的GTPC地址。 
配置ZONE。 
zone " mnc011.mcc460.3gppnetwork.org" { type master;
file "db.epc. mnc011.mcc460 "; }; 
配置RR，文件名为db.epc.mnc011.mcc460。 
`$TTL 3600
@	IN	SOA	 jsdns1.mnc011.mcc460.3gppnetwork.org.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc011.mcc460. 3gppnetwork.org.
	IN	NS	jsdns2.mnc011.mcc460. 3gppnetwork.org.
;    IN   NAPTR order  pref.  flag     service     regexp 	replacement 
$ORIGIN rac.epc.mnc011.mcc460.3gppnetwork.org.
rac0001.lac1001  IN   NAPTR  100    100    "a"  "x-3gpp-sgsn:x-gn:x-gp"   "" 
	 sgsn01.rac.epc.mnc011.mcc460.3gppnetwork.org.
sgsn01     	IN	  A	  1.1.1.5` 
配置SGSN支持RIM。 
[SET SOFTWARE PARAMETER]:PARAID=65542,PARAVALUE=1
测试用例 :###### 3G到4G的TAU 
测试项目|3G到4G的TAU
---|---
测试目的|验证SGSN、MME能正确处理3G到4G的TAU。
预置条件|LTE,3G网络内的所有网元运行正常，OM维护正常。用户在HSS/HLR开户，并签约2G/3G业务和LTE业务。打开消息跟踪。
测试过程|用户附着到3G网络。用户发起FTP业务，并一直保持。用户移动到LTE网络覆盖区域，发起TAU流程。检查网络侧用户信息和测试信令。
通过准则|用户在3G附着成功。用户正常进行FTP下载。TAU请求消息中携带GUTI等参数。创建缺省承载成功。MME/SGSN向HSS/HLR发起Update Location流程。HSS/HLR向MME/SGSN发起Cancel Location流程。用户在LTE附着成功。FTP业务能够继续。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
###### 4G到3G的RAU 
测试项目|4G到3G的RAU
---|---
测试目的|验证MME\SGSN正确处理UE发起的RAU。
预置条件|LTE,3G网络内的所有网元运行正常，OM维护正常。用户在HSS/HLR开户，并签约2G/3G业务和LTE业务。打开消息跟踪。
测试过程|用户附着到LTE网络。MME发起S1 Release流程。UE从LTE小区移动到3G小区，发起RAU流程。检查网络侧用户信息和测试信令。
通过准则|用户在LTE网络附着成功。用户转换为ECM-IDLE态。RAU请求消息携带P-TMSI等参数。MME/SGSN向HSS/HLR发起Update Location流程。HSS/HLR向MME/SGSN插入用户签约数据。用户在3G RAU成功。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
###### 3G到4G的切换 
测试项目|3G到4G的切换
---|---
测试目的|验证UTRAN到E-UTRAN的切换，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。RNC上配好了到EPS的Handover的相关配置。UE已经通过RNC附着到GPRS网络，至少激活了一个PDP上下文，且正在进行数据业务。在MME上建立S1接口跟踪，用户跟踪，GTPC跟踪。PDN GW支持GGSN功能。
测试过程|UE逐渐从RNC覆盖区移动到eNodeB覆盖区，Source RNC触发Handover流程。在网络侧查询用户的信息。
通过准则|Handover流程成功，MME选择了一个Serving GW。切换之后数据业务正常。Gn/Gp SGSN上没有用户的信息。MME上用户EMM状态为EMM-REGISTERED，ECM状态为ECM-CONNECTED。消息跟踪能够跟踪到相应的消息，流程正确  。
测试结果|–
###### 4G到3G的切换 
测试项目|4G到3G的切换
---|---
测试目的|验证 E-UTRAN到UTRAN的切换，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB上配好了到GPRS的Handover的相关配置。UE已经通过eNodeB附着到EPS网络，且正在进行数据业务。在MME上建立S1接口跟踪，用户跟踪，GTPC跟踪。PDN GW支持GGSN功能。
测试过程|UE逐渐从eNodeB覆盖区移动到RNC覆盖区，Source eNodeB触发Handover流程。在网络侧查询用户的信息。
通过准则|Handover流程成功。切换之后数据业务正常。MME上没有用户的信息，GnGp SGSN上用户状态为connected状态。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
###### 3G到4G的RIM 
测试项目|3G到4G的RIM
---|---
测试目的|验证UTRAN到E-UTRAN的RIM，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。RNC和SGSN上配好了到EPS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|RNC发起3G到4G的RIM流程，Target ID携带目标eNodeB ID。在MME和SGSN上检查信令流程。
通过准则|SGSN收到RNC的RIM消息后，通过解析获取目标MME地址，并将RIM消息转发给MME。MME收到SGSN的RIM消息，根据目标ID查找目标eNodeB，并将RIM消息转发给目标eNodeB。
测试结果|–
###### 4G到3G的RIM 
测试项目|4G到3G的RIM
---|---
测试目的|验证E-UTRAN到UTRAN的RIM，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB和MME上配好了到PS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|eNodeB发起4G到3G的RIM流程，Target ID携带目标RNC ID。在MME和SGSN上检查信令流程。
通过准则|MME收到eNodeB的RIM消息后，通过解析获取目标SGSN地址，并将RIM消息转发给SGSN。SGSN收到MME的RIM消息，根据目标ID查找目标RNC，并将RIM消息转发给目标RNC。
测试结果|–
###### 2G到4G的RIM 
测试项目|2G到4G的RIM
---|---
测试目的|验证GERAN到E-UTRAN的RIM，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。BSC和SGSN上配好了到EPS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|BSC发起2G到4G的RIM流程，Target ID携带目标eNodeB ID。在MME和SGSN上检查信令流程。
通过准则|SGSN收到BSC的RIM消息后，通过解析获取目标MME地址，并将RIM消息转发给MME。MME收到SGSN的RIM消息，根据目标ID查找目标eNodeB，并将RIM消息转发给目标eNodeB。
测试结果|–
###### 4G到2G的RIM 
测试项目|4G到2G的RIM
---|---
测试目的|验证E-UTRAN到GERAN的RIM，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB和MME上配好了到PS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|eNodeB发起4G到2G的RIM流程，Target ID携带目标Cell ID。在MME和SGSN上检查信令流程。
通过准则|MME收到eNodeB的RIM消息后，通过解析获取目标SGSN地址，并将RIM消息转发给SGSN。SGSN收到MME的RIM消息，根据目标ID查找目标BSC，并将RIM消息转发给目标BSC。
测试结果|–
## ZUF-78-01-004 业务请求 
特性描述 :特性描述 :描述 :定义 :业务请求流程
业务请求流程是重建用户的S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接的流程。
在业务请求流程中，用户的S1连接和E-RAB连接都被重建，空口的RRC连接和RB连接也会一并被重建，eNodeB保存用户的安全等信息，UE和MME中用户的ECM状态从空闲态变为连接态。
业务请求流程完成之后，用户能继续通过EPS网络访问数据业务和其他业务。 
寻呼流程
寻呼流程是通知用户有用户下行数据报文或下行信令消息要发送给用户的流程。 
在寻呼流程中，用户知道有下行数据报文或下行信令消息需要接收，会触发用户发起业务请求流程。 
寻呼流程完成之后，用户发起业务请求对寻呼进行响应，通过业务请求流程重建S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，业务请求流程完成之后用户能继续通过EPS网络访问数据业务和其他业务。 
应用场景 :###### 业务请求流程 
业务请求流程是基本流程，S1信令连接释放之后，用户想要通过EPS网络访问数据业务和其他业务，必须通过业务请求流程重建用户的S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，才能继续通过EPS网络访问数据业务和其他业务。具体常见场景包括： 
业务服务器定时发送业务数据报文给用户，如定时给用户发送MMS。 
用户使用数据业务，访问数据网络，如进行Web浏览。 
用户欠费或销卡。 
运营商对网络进行维护，主动把用户分离。 
###### 寻呼流程 
寻呼流程也是基本流程，是MME通知用户有用户下行数据报文或下行信令消息要发送给用户。具体常见场景包括： 
业务服务器定时发送业务数据报文给用户，如定时给用户发送MMS。 
用户欠费或销卡。 
运营商对网络进行维护，主动把用户分离。 
客户收益 :受益方|受益描述
---|---
运营商|支持S1连接释放，可以节约运营商的EPS网络资源，特别是无线资源。通过寻呼和业务请求，又可以使用户访问数据业务或其他业务不受影响。同时运营商也可以通过在业务请求过程中对用户进行鉴权，拒绝非法用户接入EPS网络，避免用户非法使用网络资源。
移动用户|对终端用户不可见。
实现原理 :系统架构 :EPS网络架构如下图所示。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|在业务请求过程中，具体功能包括：触发业务请求流程，完成无线资源的建立。在寻呼过程中，具体功能包括：接收寻呼消息，对寻呼进行响应。
eNodeB|在业务请求过程中，具体功能包括：对用户完成无线资源的建立，完成S1-MME与S1-U口资源的建立。在寻呼过程中，具体功能包括：在特定的区域，完成对用户的寻呼。
MME|在业务请求过程中，具体功能包括：重建S1信令连接和E-RAB连接。在寻呼过程中，具体功能包括：通知eNodeB对用户进行寻呼。
SGW|在业务请求过程中，具体功能包括：完成S1-U口资源的建立。
PGW|在业务请求过程中，具体功能包括：根据用户接入方式和位置信息，完成IP-CAN会话修改过程。
PCRF|在业务请求过程中，具体功能包括：根据用户接入方式和位置信息，完成IP-CAN会话修改过程。
本网元实现 :图2  寻呼策略流程

MME需要寻呼用户，先判断是否可以采用CSG寻呼，可以的话则MME按照Old GUTI+CSG进行寻呼。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI在CSG下寻呼用户，如果收到UE的寻呼响应（即业务请求消息），寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI+CSG发送寻呼消息给CSG对应的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI在CSG下寻呼用户，如果收到UE的寻呼响应（即业务请求消息），寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照Old GUTI+用户签约的CSGLIST进行寻呼，发送寻呼消息给MME下CSGLIST对应的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI+用户签约的CSGLIST进行寻呼，发送寻呼消息给MME下CSGLIST对应的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照Old GUTI进行寻呼，发送寻呼消息给UE最近一次所在的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI进行寻呼，发送寻呼消息给UE最近一次所在的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照Old GUTI进行寻呼，发送寻呼消息给UE最近几次所在的eNodeB（最多记录7次历史eNodeB信息），使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI进行寻呼，发送寻呼消息给UE最近几次所在的eNodeB（最多记录7次历史eNodeB信息），使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照Old GUTI进行寻呼，发送寻呼消息给UE最近一次所在TA下的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI进行寻呼，发送寻呼消息给UE最近一次所在TA下的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照Old GUTI进行寻呼，发送寻呼消息给UE最近几次TA下的eNodeB（最多记录3个历史TA），使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI进行寻呼，发送寻呼消息给UE最近几次TA下的eNodeB（最多记录3个历史TA），使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照Old GUTI进行寻呼，发送寻呼消息给系统分配给UE的TA List下的eNodeB（最多携带36个TA），使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME优先按照New GUTI进行寻呼，发送寻呼消息给系统分配给UE的TA List下的eNodeB，使用GUTI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用GUTI寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，根据运营商策略，判断是否可以继续使用IMSI对用户进行寻呼。如果可以使用IMSI进行寻呼，MME继续发送寻呼消息给用户所在的TA
List对应的每一个eNodeB，使用IMSI寻呼用户；如果不可以使用IMSI进行寻呼，寻呼流程失败，寻呼流程结束。 
如果eNodeB收到MME的寻呼消息，eNodeB使用IMSI在TA List下寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束。 
如果没有收到UE的寻呼响应，MME继续发送寻呼消息给MME下所有TA对应的eNodeB，使用IMSI寻呼用户。 
如果eNodeB收到MME的寻呼消息，eNodeB使用IMSI在MME下所有TA下寻呼用户，如果收到UE的寻呼响应，寻呼流程成功，寻呼流程结束；如果没有收到UE的寻呼响应，寻呼流程失败，寻呼流程结束。 
所有的寻呼策略都是可选的，通过配置对应的寻呼次数为0可以关闭该寻呼策略。当前寻呼策略下的重传次数未达到配置次数时，MME会触发寻呼重传，这样可方便各外场根据不同的网络情况组合不同的寻呼策略。 
在寻呼进行的过程中，如果收到了UE发起的附着请求、TA位置区更新、业务请求等流程，则强制终止正在进行中的寻呼流程，避免不必要的寻呼造成系统负荷增加。 
业务流程 :UE触发的业务请求流程
图3  UE触发的业务请求流程

UE发送RRC消息给eNodeB，RRC消息中包含UE发送给MME的业务请求消息。 
eNodeB发送初始化用户消息给MME，其中包括UE发送给MME的业务请求消息。如果MME不能处理该业务请求，则拒绝业务请求。 
根据营运商的策略，非接入层的鉴权/安全过程可以被执行。 
MME发送初始化上下文建立请求消息给eNodeB，激活所有EPS承载的无线承载和S1承载。 
eNodeB执行无线承载建立过程，并且建立用户面安全上下文。当用户面无线承载建立和业务请求过程完成，EPS承载状态在用户与网络侧同步之后，UE将删除没有无线承载的EPS承载。如果一个缺省EPS承载的无线承载没有建立，UE必须本地去激活与这个缺省承载相关联的所有EPS承载。 
UE发送的上行数据报文通过eNodeB发送给SGW，SGW再把上行数据报文发送给PGW。 
eNodeB发送初始化上下文建立完成消息给MME。 
MME按每PDN连接发送修改承载请求消息给SGW，SGW收到修改承载请求消息后，就能把下行数据报文发送给用户了。 
如果用户接入方式发生了改变或用户的位置信息发生了改变，SGW按每PDN连接发送修改承载请求消息给PGW。 
如果部署了动态PCC，根据用户接入方式，PGW和PCRF完成IP-CAN会话修改过程。如果没有部署动态PCC，PGW使用本地Qos策略。 
PGW发送修改承载响应消息给SGW。 
SGW发送修改承载响应消息给MME。 
网络侧信令触发的寻呼和业务请求流程
图4  网络侧信令触发的寻呼和业务请求流程

流程说明： 
MME收到SGW下行信令消息比如专有承载建立、承载修改等，或MME收到HSS触发的分离流程，或MME收到OMM的消息比如分离等，MME检测到不存在用户的S1信令连接，开始触发寻呼流程。 
如果UE在MME中注册了，MME发送寻呼消息给用户所在的TA List对应的每一个eNodeB。 
如果eNodeB收到MME的寻呼消息，eNodeB寻呼用户。 
如果用户从eNodeB收到寻呼消息，并且RRC连接不存在，则用户触发业务请求流程。 
MME继续处理SGW下行信令消息，或继续处理HSS触发的分离流程，或继续处理OMM的消息比如分离用户等。 
网络侧下行数据触发的寻呼和业务请求流程
图5  网络侧下行数据触发的寻呼和业务请求流程

流程说明： 
如果SGW收到下行数据报文，但是对应承载的S1-U资源被释放，SGW缓存下行数据报文。 
SGW发送下行数据通知消息给MME。 
MME发送下行数据通知确认消息给SGW，如果SGW又收到这个用户的数据报文，SGW缓存数据报文，不会再给MME发送下行数据通知消息。 
如果UE在MME中注册了，MME发送寻呼消息给用户所在TA List对应的每一个eNodeB。如果MME检测到用户的S1连接存在，则忽略步骤4~5。 
如果eNodeB收到MME的寻呼消息，eNodeB寻呼用户。 
如果用户从eNodeB收到寻呼消息，并且RRC连接不存在，则用户触发业务请求流程。如果MME检测到用户的S1连接存在，则直接从MME发送初始化上下文建立请求消息给eNodeB开始。 
如果SGW缓存了用户的下行数据报文，SGW把下行数据报文经过eNodeB发送给用户。 
系统影响 :随着业务请求和寻呼的增加，系统资源占用会一直增大，CPU占用率会相应上升，无线资源占用也会一直增大。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务请求流程是基本业务流程，用户S1连接释放之后，用户不能通过EPS网络访问数据业务和其他业务，只有通过业务请求流程，重建S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，才能继续通过EPS网络访问数据业务和其他业务。 
寻呼流程也是基本业务流程，用户S1连接释放之后，如果网络侧有用户下行数据报文要发送给用户，或下行信令消息要发送给用户，需要通过寻呼流通知用户，用户再通过业务请求流程，重建S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，才能接收下行数据报文或下行信令消息。 
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"
3GPP TS 23.203: "Policy and charging control architecture"
3GPP TS 23.003: "Numbering, addressing and identification"
3GPP TS 24.007: "Mobile radio interface signalling layer3; General aspects"
特性能力 :名称|指标
---|---
一个用户拥有的S1信令连接|1条
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME寻呼策略因子配置ADD MME PAGING POLICY FACTORSET MME PAGING POLICY FACTORDEL MME PAGING POLICY FACTORSHOW MME PAGING POLICY FACTORMME寻呼策略配置ADD MME PS PAGING POLICYSET MME PS PAGING POLICYDEL MME PS PAGING POLICYSHOW MME PS PAGING POLICYADD MME CS PAGING POLICYSET MME CS PAGING POLICYDEL MME CS PAGING POLICYSHOW MME CS PAGING POLICYADD MME SMS PAGING POLICYSET MME SMS PAGING POLICYDEL MME SMS PAGING POLICYSHOW MME SMS PAGING POLICYMME全局寻呼策略配置SET MME GLOBAL PS PAGING POLICYSHOW MME GLOBAL PS PAGING POLICYSET MME GLOBAL CS PAGING POLICYSHOW MME GLOBAL CS PAGING POLICYSET MME GLOBAL SMS PAGING POLICYSHOW MME GLOBAL SMS PAGING POLICY 
安全变量表2  新增安全变量安全变量命令寻呼失败时去活GBR承载SET PACKET DOMAIN PARAMETER 
软件参数表3  新增软件参数软件参数ID软件参数名称262260寻呼消息信令跟踪上报方式 
性能统计 :测量类型|描述
---|---
业务请求流程测量|编号为43002开头的所有计数器
寻呼流程测量|编号为43004开头的所有计数器
业务请求分网元测量|编号为46402开头的所有计数器
NSA业务请求流程测量|编号为46612开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现业务请求流程。 
调整特性 :设置数据业务全局寻呼策略。 
[SET MME GLOBAL PS PAGING POLICY]
设置分组域参数，寻呼失败时去活GBR承载。 
[SET PACKET DOMAIN PARAMETER]:DEACGBR="YES"
测试用例 :测试项目|UE主动发起业务请求
---|---
测试目的|测试UE主动发起业务请求
预置条件|UE、MME、SGW、eNodeB、PGW等各网元工作正常。MME网管服务器、客户端连接正常；服务器与OMP连接正常。UE附着成功，S1连接释放。
测试过程|UE发起业务请求。
通过准则|UE的业务请求成功。
测试结果|–
测试项目|网络侧下行数据触发的寻呼和业务请求
---|---
测试目的|测试网络侧下行数据触发的寻呼和业务请求
预置条件|UE、MME、SGW、eNodeB、PGW等各网元工作正常。MME网管服务器、客户端连接正常；服务器与OMP连接正常。UE附着成功，S1连接释放。
测试过程|SGW发送下行数据通知消息给MME。
通过准则|MME发起对UE的寻呼，UE回复业务请求，业务请求成功。
测试结果|–
常见问题处理 :无。 
## ZUF-78-01-005 S1释放 
特性描述 :特性描述 :描述 :定义 :S1释放流程是释放用户的S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接的流程，包括eNodeB触发的S1释放流程和MME触发的S1释放流程。
在S1释放流程中，用户的S1连接和E-RAB连接都被释放，空口的RRC连接和RB连接也会一并被释放，eNodeB不再保存用户的任何信息，UE和MME中用户的ECM状态从连接态变为空闲态，non-GBR承载会被保留，GBR承载根据运营商策略，可以被保留或去激活。
S1释放流程完成之后，用户不能通过EPS网络访问数据业务和其他业务，只有通过业务请求流程，重建S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，才能继续通过EPS网络访问数据业务和其他业务。
应用场景 :S1释放流程是基本流程，是释放用户的S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接的流程。EPS网络为了节省无线资源，会把不需要保留或暂时不需要保留的S1连接释放。具体常见场景包括： 
运营商对eNodeB或MME进行网络维护，主动把用户的S1连接释放。 
eNodeB检测到用户较长时间没有活动，eNodeB把用户的S1连接释放。 
用户进入信号极不好的地方，导致RRC连接断开，eNodeB把用户的S1连接释放。 
用户关机。 
客户收益 :受益方|受益描述
---|---
运营商|支持把较长时间没有活动或进入信号极差区域或注销的用户的S1连接释放，可以节约运营商的EPS网络资源，特别是无线资源。
移动用户|对终端用户不可见。
实现原理 :系统架构 :EPS网络架构如下图所示。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，比如用户标识、移动性管理状态、用户安全参数等。在S1释放过程中，具体功能包括：释放空口的RRC连接和RB连接，把用户的ECM状态从连接态变为空闲态。
eNodeB|为终端的接入提供无线资源，对用户提供接入层安全管理。在S1释放过程中，具体功能包括：释放用户的S1-MME口和S1-U口资源，释放空口的RRC连接和RB连接，eNodeB不再保存用户的任何信息。
MME|控制面功能实体，负责管理和存储UE相关信息，比如用户标识、移动性管理状态、用户安全参数等，为用户分配临时标识，对用户进行鉴权，处理MME和UE之间的所有非接入层消息。在S1释放过程中，具体功能包括：释放S1-MME口资源，把用户的ECM状态从连接态变为空闲态，non-GBR承载会被保留，GBR承载根据运营商策略，可以被保留或去激活。
SGW|用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE的下行数据。管理和存储UE的承载信息，比如IP承载业务参数和网络内部路由信息等。在S1释放过程中，具体功能包括：如果对GBR承载进行去激活，则负责删除GBR承载信息。
PGW|负责将UE接入PDN的网关，给用户分配IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。在S1释放过程中，具体功能包括：如果对GBR承载进行去激活，则负责删除GBR承载信息。
PCRF|该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的QoS规则以及计费规则。在S1释放过程中，具体功能包括：如果对GBR承载进行去激活，则释放GBR承载信息。
本网元实现 :S1释放流程属于基本业务流程，实现细节参见下面业务流程的具体描述。 
业务流程 :流程说明： 
（可选）eNodeB检测到需要释放用户的信令连接和RB连接，向MME发送S1 UE Context Release Request消息。 
MME发送Release Access Bearers Request消息给SGW，请求SGW释放承载的S1-U口资源。 
SGW删除所有与eNodeB相关的UE信息（eNodeB的用户面地址和TEID），给MME回Release Access
Bearers Response消息。该UE的SGW上下文的其它信息单元不受影响。SGW保留了其为该UE的承载所分配的S1-U配置。如果有给UE的下行数据分组包，SGW开始缓存下行给UE的分组包，并发起网络触发的业务请求过程。 
MME发送S1 UE Context Release Command给eNodeB，通知eNodeB释放S1信令连接。 
（可选）如果RRC连接还没有释放，eNodeB发送RRC Connection Release给用户，用户确认RRC连接释放后，eNodeB删除用户的所有相关信息。 
eNodeB发送S1 UE Context Release Complete消息给MME，确认S1连接的释放。MME删除与eNodeB有关的该UE的上下文信息（eNodeB地址和TEIDs），但保留UE的其余上下文信息，包括SGW的S1-U配置信息（SGW地址和TEIDs）。为UE建立的所有non-GBR
EPS承载被保存在MME和SGW内。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :S1释放流程是基本业务流程，S1释放流程完成之后，用户不能通过EPS网络访问数据业务和其他业务，只有通过业务请求流程，重建S1-MME口S1信令连接和S1-U口所有承载的E-RAB连接，才能继续通过EPS网络访问数据业务和其他业务。 
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"
3GPP TS 23.203: "Policy and charging control architecture"
3GPP TS 23.003: "Numbering, addressing and identification"
3GPP TS 24.007: "Mobile radio interface signalling layer3; General aspects"
特性能力 :名称|指标
---|---
一个用户最多拥有S1信令连接数|1条
MME支持最大用户接入数|1500万
MME支持最大承载数|3000万
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :软件参数表1  新增软件参数软件参数ID软件参数名称786479ENB失败时是否保留GBR承载 
动态管理S1连接释放：RELEASE S1。 
性能统计 :测量类型|描述
---|---
eNB 发起的S1释放流程测量|编号为46423开头的所有计数器
MME 发起的S1释放流程测量|编号为46424开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现S1释放流程。 
调整特性 :在MME侧手动发起S1释放过程。 
执行命令[RELEASE S1]，释放处在连接态的S1连接。
设置ENB失败时是否保留GBR承载。 
执行命令[SET SOFTWARE PARAMETER]。
测试用例 :测试项目|S1连接释放
---|---
测试目的|测试MME主动发起对用户S1连接的释放。
预置条件|UE、MME、SGW、eNodeB、PGW等各网元工作正常。MME网管服务器、客户端连接正常；服务器与OMP连接正常。UE附着成功，保持有S1连接。
测试过程|执行S1连接释放命令RELEASE S1。
通过准则|UE的S1连接被释放。
测试结果|—
常见问题处理 :无。 
## ZUF-78-01-006 去附着 
特性描述 :特性描述 :描述 :定义 :分离流程是用户从EPS网络上注销的流程，包括UE发起的分离流程、MME发起的分离流程、HSS发起的分离流程。
根据是否需要显示通知UE分离，分离流程又可以分为显示的分离流程和隐式的分离流程。 
MME和UE之间有显示的分离消息通知的分离流程为显示的分离流程。 
MME检测到UE长时间没有和EPS网络交互，触发MME发起的分离流程，不通知UE，为隐式的分离流程。 
在分离过程中，会删除为用户建立的所有承载，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为注销态。 
分离流程完成之后，用户不能再通过EPS网络访问数据业务和其他业务。 
应用场景 :分离流程是基本流程，是把用户从EPS网络上注销的流程。具体常见场景包括： 
用户关机。 
用户欠费停机。 
用户销卡。 
运营商进行网络维护，主动把用户从网络上强制分离。 
用户长时间驻留在无线信号极差的地方。 
客户收益 :受益方|受益描述
---|---
运营商|支持用户从运营商的EPS网络上注销，可以节约运营商的EPS网络资源，也可以通过对欠费用户或销卡用户进行强制分离，加强了运营商对用户的管理，避免欠费或销卡用户非法继续使用网络资源。
移动用户|对终端用户不可见。
实现原理 :系统架构 :EPS网络架构如下图。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|触发分离流程或处理MME发起的分离流程，完成无线资源的释放，删除建立的所有承载，删除移动性管理上下文或把移动性管理上下文状态置为注销态。
eNodeB|触发分离流程或处理MME发起的分离流程，完成无线资源的释放，删除建立的所有承载，删除移动性管理上下文或把移动性管理上下文状态置为注销态。
MME|触发分离流程或处理UE发起的分离流程或处理HSS发起的分离流程，删除用户建立的所有承载，释放S1信令连接，删除移动性管理上下文或把移动性管理上下文状态置为注销态。
HSS|用户欠费停机、销卡时，触发HSS发起的分离流程。
SGW|删除UE的会话和承载信息。
PGW|删除UE的会话和承载信息，回收已分配给用户的IP地址。
PCRF|释放EPS承载信息。
本网元实现 :分离流程属于基本业务流程，实现细节参见下面业务流程的具体描述。 
业务流程 :UE发起的分离流程
图2  UE发起的分离流程
流程说明： 
UE发送Detach Request给MME，消息中会携带GUTI和Switch Off参数。eNodeB会将UE所在的TAI+ECGI标识和该Detach
Request消息一起转发给MME。 
MME按每PDN连接发送删除会话请求消息（含TEID）给SGW，去激活SGW内该UE激活的EPS承载。如果PGW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。 
SGW释放相关承载信息，按每PDN连接发送删除会话请求消息（含TEID）给PGW。如果PGW请求了UE位置信息，则SGW在这个消息中包含用户位置信息。 
PGW给SGW回删除会话响应消息（含TEID）。 
如果部署了PCRF，PGW执行IP-CAN会话结束流程，指示PCRF释放EPS承载。 
SGW向MME发送删除会话响应消息（含TEID）。 
如果Switch Off参数指示分离不是关机引起的，MME发送Detach Accept给UE。 
MME发送S1释放命令给eNodeB，释放UE的S1-MME信令连接。 
MME发起的分离流程
图3  MME发起的分离流程

流程说明： 
MME可以发起显示或隐式分离。如果UE长时间没有和MME通讯，MME可以隐式分离UE。MME在隐式分离时，不发送Detach
Request消息给UE。MME发起显示分离时，如果UE处于ECM-CONNNECTED态，MME通过发送Detach Request消息给UE进行显示分离。如果UE处于ECM-IDLE态，MME寻呼UE，发送Detach
Request消息。 
MME按每PDN连接发送删除会话请求消息（含TEID）给SGW，去激活SGW内该UE激活的EPS承载。如果PGW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。 
SGW释放相关承载信息，按每PDN连接发送删除会话请求消息（含TEID）给PGW。如果PGW请求了UE位置信息，则SGW在这个消息中包含用户位置信息。 
PGW给SGW回删除会话响应消息（含TEID）。 
如果部署了PCRF，PGW执行IP-CAN会话结束流程，指示PCRF释放EPS承载。 
SGW向MME发送删除会话响应消息（含TEID）。 
UE在第1步之后的任何时间发送Detach Accept消息。eNodeB携带UE所在小区的TAI+ECGI标识与Detach
Accept消息一起转发给MME。 
MME接收到Detach Accept消息和删除会话响应消息，MME发送S1释放命令给eNodeB，释放UE的S1-MME信令连接。如果分离类型指示为UE重新Attach，UE可以在RRC连接释放完成后重新附着。 
HSS发起的分离流程
图4  HSS发起的分离流程

流程说明： 
如果HSS想请求立即删除签约MM上下文和EPS承载，HSS发送取消位置消息（含IMSI、取消类型）给MME，取消类型设置为签约撤销。 
如果取消类型设置为签约撤销，MME发送Detach Request消息通知处于ECM-CONNECTED态的UE分离。如果UE处于ECM-IDLE态，MME寻呼UE，进行去附着过程。 
MME按每PDN连接发送删除会话请求消息（含TEID）给SGW，去激活SGW内该UE激活的EPS承载。如果PGW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。 
SGW释放相关承载信息，按每PDN连接发送删除会话请求消息（含TEID）给PGW。如果PGW请求了UE位置信息，则SGW在这个消息中包含用户位置信息。 
PGW给SGW回删除会话响应消息（含TEID）。 
如果部署了PCRF，PGW执行IP-CAN会话结束流程，指示PCRF释放EPS承载。 
SGW向MME发送删除会话响应消息（含TEID）。 
UE在第1步之后的任何时间发送Detach Accept消息。eNodeB携带UE所在小区的TAI+ECGI标识与Detach
Accept消息一起转发给MME。 
MME确认MM上下文和EPS承载删除，发送取消位置应答消息给HSS。 
MME接收到Detach Accept消息和删除会话响应消息，MME发送S1释放命令给eNodeB，释放UE的S1-MME信令连接。如果分离类型指示为UE重新Attach，UE可以在RRC连接释放完成后重新附着。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :分离流程是基本业务流程，分离流程之后，用户从EPS网络上注销了，数据业务和其他业务都无法再使用。 
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"
3GPP TS 23.203: "Policy and charging control architecture"
3GPP TS 23.003: "Numbering, addressing and identification"
3GPP TS 24.007: "Mobile radio interface signalling layer3; General aspects"
特性能力 :名称|指标
---|---
分离流程删除用户的承载数|所有承载
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :安全变量表1  新增安全变量安全变量命令MME可达定时器时长(秒)SET MOBILE MANAGEMENTMME隐式分离定时器时长(秒)SET MOBILE MANAGEMENTMME MM上下文删除定时器时长(分钟)SET MOBILE MANAGEMENT 
动态管理通过网管发起分离流程：DETACH USER。 
性能统计 :测量类型|描述
---|---
去附着流程测量|编号为43003开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现去附着流程。 
调整特性 :配置可达定时器时长。SET MOBILE MANAGEMENT:REACHTIMER=300 
配置隐式分离定时器时长。SET MOBILE MANAGEMENT:IMPDETACHTIMER=300 
配置MM上下文删除定时时长。SET MOBILE MANAGEMENT:MMEUNREACHABLETIMER=300 
测试用例 :测试项目|MME发起的分离
---|---
测试目的|测试MME主动发起对用户的分离
预置条件|UE、MME、SGW、eNodeB、PGW等各网元工作正常。MME网管服务器、客户端连接正常；服务器与OMP连接正常。UE附着成功，保持有S1连接。
测试过程|执行MME分离命令DETACH USER。
通过准则|UE被分离。
测试结果|–
常见问题处理 :无。 
## ZUF-78-01-007 用户数据管理 
概述 :当HSS中的签约数据发生变化时，HSS通知MME更新用户数据。 
清除功能允许MME在删除一个分离MS的签约数据和MM上下文后通知HSS。 
收益 :本特性是移动终端的一个主要功能。 
MME通知HSS有关分离MS的信息，这样HSS能够及时获知MS信息并作出相应的标记。 
描述 :当HSS中的签约数据发生变化时，HSS通知MME更新用户数据。 
HSS向MME发送插入用户数据（Insert Subscriber Data）消息，并MME更新该用户的签约数据。 
通过清除功能，在删除一个分离MS的签约数据和MM上下文后，MME可通知HSS这一操作。作为一个执行选项，在UE进行隐式分离或显式分离后，MME可能立即删除该UE的签约数据和MM上下文。MME也可以保留分离UE的签约数据和MM上下文一段时间。这样在该UE后续附着时，MME无需访问HSS就可再次使用该UE的数据。 
## ZUF-78-01-008 UE可达性管理 
概述 :当HSS需获知UE是否可达时，HSS可向MME发送通知请求。 
如果MME收到UE Activity Notification Request消息，并且UE的状态为可达，MME将UE的状态上报给HSS。 
收益 :通过与HSS的协作，核心网可轻松的管理UE状态。 
描述 :当HSS需获知UE是否可达时，HSS向MME发送UE Reachability
Notification消息。MME将UE的状态上报给HSS.  
该流程可用于SMS over IP功能。 
如果MME收到UE Activity Notification Request消息，并且UE的状态为可达，MME向HSS发送UE
Activity Notification消息，通知UE的状态。 
该流程可用于SMS over IP功能。 
## ZUF-78-01-009 跟踪区列表管理 
特性描述 :特性描述 :术语 :术语|含义
---|---
拓扑值|根据TA的拓扑位置给用户分配TA List，给各跟踪区TA设置相应的横坐标和纵坐标的值。
区域编码|指运营商规划的允许用户接入区域（TAs）的集合。
描述 :定义 :TA List分配功能是指ZXUN uMAC在UE附着或非周期性跟踪区更新等过程中，给UE分配或者重新分配一个TA的集合，这个特定的TA集合称之为TA
List。
TA List中必须包含当前UE所在TA，且必须是在为UE服务的SGW范围内的TA，同时必须是当前MME范围内的TA。  
根据UE的业务特性和位置，ZXUN uMAC还可以提供更为灵活的TA List分配策略。
背景知识 :RA和TA List
GSM/UTMS分组域接入中，UE同一时间只会注册在一个RA（路由区）下。在一个RA内移动时，UE不需要路由区更新。只有UE跨RA移动时，才需要发起路由区更新过程，使SGSN可以及时知道UE所在的RA。当寻呼UE时，SGSN就在RA下寻呼UE。 
TA List是E-UTRAN中的概念。当UE注册到LTE网路，MME分配TA List给UE。 
UE从当前TA移动到TA
List中的其他TA，不需要发起跟踪区更新。只有UE从当前TA List移出，才需要发起位置更新。因此如果为UE分配的TA List以UE当前的位置为中心，就可以有效的减少UE立即发起TAU的概率。 
而另一方面，由于MME得知UE的准确位置是TA List，所以寻呼也是基于TA List范围的，为了控制寻呼量，TA List必须具备合理的大小，在TAU负荷和寻呼负荷之间取得平衡。 
TA List分配策略
TA List分配主要是考虑如下方面： 
LoadTA List不宜过大：寻呼与Talist包含的TA数及每个TA包含的eNB数密切相关，在寻呼较频繁的网络模型中，将明显增加网络负荷。TA List不宜过小：如果TAList中包含的TA很少，用户跨TAList移动的可能性增加，TAU更新频度增加，同样会增加网络负荷。TA List中的TA应尽量保证地理位置上的连续：不连续会导致用户在TA List内移动也可能移动到其他TA中，和TA
List范围过小是同样的效果，同样会增加网络负荷。 
TA List内各TA特性一致性各TA归属相同的MME：如果TA List中的TA属于不同的MME，MME寻呼时无法覆盖到TA List内的所有TA，可能引起寻呼失败
，导致触发寻呼业务失败（比如，VoLTE语音终呼、CS语音终呼等）。各TA归属相同的SGW：如果TA List中的不同TA属于不同的SGW，用户在TA List内跨TA移动不会重选SGW，原SGW将无法处理新的TA下的eNB的用户数据，导致用户断网。 各TA归属相同的LAI：如果TA List中的不同TA属于不同的LAI，用户在TA List内跨TA移动，可能引起CS域的始呼/终呼存在跨MSC交互，CS呼叫接通时延增加或呼叫失败。 
应用场景 :###### TA List动态分配策略的应用场景 
TA List动态分配有多种策略，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用，灵活应对各种场景。 
场景描述|TA List分配策略|TA List特性
---|---|---
网络中部署了CSFB业务。|开启属于同一LA策略。|TA List中的TA与同一个LA关联，属于同一个LA。
只为部分TA开通CSFB功能，或IMS VoPS功能。|开启需要相同CSFB能力和/或需要相同IMS VoPS能力策略。|TA List中的TA具备相同的CSFB能力和/或IMS VoPS能力。
MME管辖范围跨多个时区，有多个PLMN。|开启属于同一时区和属于同一PLMN策略。|TA List中的TA都只处于同一时区，PLMN都相同。
网络启用了移动性限制相关功能。|根据使用的移动性限制功能，开启签约ZoneCode允许和/或IMSI号段接入允许一致性策略。|TA List中的TA都在UE允许接入的TA内。
UE在比较固定的一些区域移动。|启用根据UE移动轨迹策略。|TA List中包括UE最近驻留的TA，以减少跟踪区更新次数。
SGW管理的TA较多。|启用根据TA间的拓扑优选策略。|TA List中的TA是相连。
每个TA规划的很大，每个TA和很多eNodeB关联。|配置TA List的最大TA数目。|TA List中包含的TA个数较小。
###### TA List静态分配策略的应用场景 
TA List静态分配，作为TA List动态分配的补充，在动态分配无法满足要求时，由运营商规划并静态配置。 
场景|应用场景说明|静态TA列表分配策略
---|---|---
客户已规划TA List，跨TA List移动频繁。|客户已规划好TA List，期望TA List分配时按固定配置分配，同时TA List边界用户移动频繁，希望尽量避免用户在TAList边界移动带来的频繁TAU。|开启Last TA优选功能，当用户跨TA List移动时，总是携带用户上一次访问的TA。
客户已规划TA List，跨TA List移动很少。|客户已规划好TA List，期望TA List分配时按固定配置分配，同时TA List边界设置为山川河流边界，用户活动稀少。|用户跨TA List移动很少，不需要开启Last TA优选功能。
客户收益 :收益者|收益描述
---|---
运营商|增加了TA List分配的灵活性，为TA的灵活规划提供了基础。合理的TA List分配可以使得TAU和寻呼保持合理的负荷。
终端用户|该功能对移动用户不可见。
实现原理 :涉及的网元 :本特性只涉及MME网元，MME网元在附着和非周期性跟踪区更新过程中，根据系统配置的策略为UE分配TA
List。 
本网元实现 :TA List分配有两种方式： 
动态分配：由MME根据网管中预先配置的策略动态分配。 
静态分配：由运营商手工规划全网的TA List，并将规划好的TA List在网管中配置。 
总的来说，动态分配策略更灵活，且不需要人工干预，建议默认使用动态分配策略，静态分配策略作为补充。 
比较点|动态分配TA List|静态分配TA List
---|---|---
易用性|无需人工干预。|易用性|需要运营商提前规划。
策略控制|TA List大小。|可根据策略动态调整。|配置后其大小即固定。
TA连续性。|策略控制|可根据移动轨迹、TA拓扑、与LAI的关联关系等保证连续性。|需要运营商根据规划保证。
TA List内的各TA是否归属同MME/SGW/LAI。|策略控制|由MME系统在为UE分配TA List时自行筛选。|需要运营商在TA List规划时保证。
TA List内的各TA的其他特性的一致性。|策略控制|由MME系统在为UE分配TA List时根据策略配置自行筛选。|需要运营商在TA List规划时保证。
业务流程 :Attach
Attach流程参见[图1]。
图1  Attach

UE发起附着请求，携带当前用户所在的TAI（Current TAI），以及上一次访问注册的TAI（Last visited
registered TAI）。 
MME使用UE的Current TAI以及Last TAI，根据配置的TA List分配策略，为UE分配新的TAI List，通过附着接受消息发送给UE。 
UE返回附着完成消息。 
Tracking Area Update
Tracking Area
Update流程参见[图2]。
图2  Tracking Area Update

UE发起TAU请求，携带当前用户所在的TAI（Current TAI），以及上一次访问注册的TAI（Last visited
registered TAI）。 
MME使用UE的Current TAI以及Last TAI，根据配置的TA List分配策略，为UE分配新的TAI List，通过TAU接受消息发送给UE。 
UE返回TAU完成消息。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :只有在相应移动性限制功能开启的情况下，TA List分配策略中要求区域接入允许的策略才能生效。 
遵循标准 :标准类别|章节
---|---
3GPP|3GPP TS 23.401: "GPRS enhancements for E-UTRAN access ".
3GPP TS 24.301:"Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS) Stage 3"|3GPP
特性能力 :规格名称|规格指标
---|---
一个TA List中的可以配置的最大TA个数|16
MME支持的最大TA数|65535
MME支持的最大静态TA List数|32768
每eNodeB支持的最大TA数|36
SGW管理区域配置|支持最多为1024个SGW配置其管理的TA，每个SGW最大关联128个TA Group
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :当MME采用静态分配TA
List功能时，该功能受到License的控制，对应License文件中的项目编号为7075，此编号配置为ON，表示MME支持静态分配TA
List功能。 
###### 组网规划要求 
当处于空闲状态UE需要被寻呼时，核心网必须在UE所在TAI list列表中的所有TAI所属的全部小区进行寻呼。 
TA规划大小需要和寻呼小区的寻呼能力以及MME的寻呼能力相匹配： 
如果TA规划得过大，则寻呼的负荷也较大，寻呼就会滞后，UE不能及时寻呼，延迟了端到端接续时长，直接影响用户感知。 
如果TA设置过小，TA/TAL边界较多，UE发起的跟TA更新（TAU）就会增加，TAU过程将占用无线空口的上行带宽资源和核心网的相关传输资源。频繁的TAU也将增加MME负荷和UE的电池耗电量，另外由于UE在TAU过程中不能响应寻呼，频繁的TAU也可能降低MME的寻呼成功率。 
因此，TA的合理规划和设置非常重要，必须根据网络部署情况对TA列表的大小进行限制，以避免浪费系统资源。 
对其他网元的要求 :UE|MME|eNodeB|SGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表4  新增配置项配置项命令跟踪区配置ADD TA动态跟踪区列表分配策略SET TALIST ASSIGN POLICYServing GW管理区域配置ADD SGW静态跟踪区列表分配策略SET TALIST POLICY静态跟踪区列表配置ADD TA LIST 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警和通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本节介绍如何配置TA List分配功能，包括动态TA List分配功能和静态TA List分配功能两种方式。 
配置前提 :类别|前提
---|---
动态TA List分配功能|如果MME管理的TA跨了多个时区，则需要知道每个TA的时区信息。
静态TA List分配功能|如果使用静态TA列表配置，必须开启Licence开关“MME支持TAL静态分配功能”。
配置过程 :类别|配置过程
---|---
动态TA List分配功能|配置MME管理的TA。配置SGW区域。配置TA列表分配策略。
静态TA List分配功能|配置MME管理的TA列表。配置静态TA列表分配策略。
配置实例 :###### 动态TA List分配功能配置实例1 
场景说明
TA List中允许包含的最大TA个数为16个，TA List中的TA与同一个LA关联，属于同一个LA，并且都在UE允许接入的TA内。 
运营商MME管辖的TA区域和每个TA关联的LA信息参见下表，每个TA有相同时区、PLMN、CSFB能力、IMS VoIP能力，TA组号1关联SGW1，组号2关联SGW2。 
跟踪区标识|组号|移动国家码|移动网号|跟踪区域码(HEX)|位置区名|跟踪区名
---|---|---|---|---|---|---
1|1|460|1|1001|LA1|TA1
2|1|460|1|1002|LA1|TA2
3|1|460|1|1003|LA1|TA3
4|1|460|1|1004|LA1|TA4
5|1|460|1|1005|LA1|TA5
6|1|460|1|1006|LA1|TA6
7|1|460|1|1007|LA1|TA7
8|1|460|1|1008|LA1|TA8
9|1|460|1|1009|LA2|TA9
10|1|460|1|1010|LA2|TA10
11|1|460|1|1011|LA2|TA11
12|1|460|1|1012|LA2|TA12
13|2|460|1|1013|LA2|TA13
14|2|460|1|1014|LA3|TA14
15|2|460|1|1015|LA3|TA15
16|2|460|1|1016|LA3|TA16
17|2|460|1|1017|LA3|TA17
18|2|460|1|1018|LA3|TA18
19|2|460|1|1019|LA3|TA19
20|2|460|1|1020|LA3|TA20
当UE（IMSI：460012221234567）在TA1接入，上一次在TA10接入时，MME分配的TA list应该为TA1、TA2、TA3、TA4、TA5、TA6、TA7。 
如果UE（IMSI：460023331234567）在TA15接入，上一次在TA20接入，MME分配的TA list应该为TA14、TA15、TA16、TA17、TA18、TA19、T20。 
配置步骤
配置步骤参见下表。 
配置说明|配置脚本
---|---
添加TA，配置TA的MNC、MCC、TAC等信息。这里关联的LA是已经配置好的LA。|ADD TA:TAID=1,GRPID=1,MCC="460",MNC="01",TAC="1001",LAI="LA1",NAME="TA1"ADD TA:TAID=2,GRPID=1,MCC="460",MNC="01",TAC="1002",LAI="LA1",NAME="TA2"ADD TA:TAID=3,GRPID=1,MCC="460",MNC="01",TAC="1003",LAI="LA1",NAME="TA3"ADD TA:TAID=4,GRPID=1,MCC="460",MNC="01",TAC="1004",LAI="LA1",NAME="TA4"ADD TA:TAID=5,GRPID=1,MCC="460",MNC="01",TAC="1005",LAI="LA1",NAME="TA5"ADD TA:TAID=6,GRPID=1,MCC="460",MNC="01",TAC="1006",LAI="LA1",NAME="TA6"ADD TA:TAID=7,GRPID=1,MCC="460",MNC="01",TAC="1007",LAI="LA1",NAME="TA7"ADD TA:TAID=8,GRPID=1,MCC="460",MNC="01",TAC="1008",LAI="LA1",NAME="TA8"ADD TA:TAID=9,GRPID=1,MCC="460",MNC="01",TAC="1009",LAI="LA2",NAME="TA9"ADD TA:TAID=10,GRPID=1,MCC="460",MNC="01",TAC="1010",LAI="LA2",NAME="TA10"ADD TA:TAID=11,GRPID=1,MCC="460",MNC="01",TAC="1011",LAI="LA2",NAME="TA11"ADD TA:TAID=12,GRPID=1,MCC="460",MNC="01",TAC="1012",LAI="LA2",NAME="TA12"ADD TA:TAID=13,GRPID=2,MCC="460",MNC="01",TAC="1013",LAI="LA2",NAME="TA13"ADD TA:TAID=14,GRPID=2,MCC="460",MNC="01",TAC="1014",LAI="LA3",NAME="TA14"ADD TA:TAID=15,GRPID=2,MCC="460",MNC="01",TAC="1015",LAI="LA3",NAME="TA15"ADD TA:TAID=16,GRPID=2,MCC="460",MNC="01",TAC="1016",LAI="LA3",NAME="TA16"ADD TA:TAID=17,GRPID=2,MCC="460",MNC="01",TAC="1017",LAI="LA3",NAME="TA17"ADD TA:TAID=18,GRPID=2,MCC="460",MNC="01",TAC="1018",LAI="LA3",NAME="TA18"ADD TA:TAID=19,GRPID=2,MCC="460",MNC="01",TAC="1019",LAI="LA3",NAME="TA19"ADD TA:TAID=20,GRPID=2,MCC="460",MNC="01",TAC="1020",LAI="LA3",NAME="TA20"
配置SGW管理跟踪区参数，SGW name为SGW，管理的跟踪区组为1、2。|ADD SGW:SGWNAME="SGW1",GRPLIST=1ADD SGW:SGWNAME="SGW2",GRPLIST=2
配置动态TA LIST分配策略，本实例中配置TA LIST携带个数为16，打开“TA List必须属于同一LA”和“TAList必须在IMSI号段允许的TA中”|SET TALIST ASSIGN POLICY:MAXTANUM=16,SAMELA="YES",IMSISEGALLOW="YES"
###### 动态TA List分配功能配置实例2 
场景说明
TA List中允许包含的最大TA个数为16个，TA List中的TA都只处于同一时区，并且PLMN都相同。 
运营商MME管辖的TA区域和每个TA关联的时区信息参见下表，每个TA有不同时区、PLMN，但有相同的CSFB能力、IMS
VoIP能力，TA组号1关联SGW1，组号2关联SGW2。 
跟踪区标识|组号|移动国家码|移动网号|跟踪区域码(HEX)|时区|跟踪区名
---|---|---|---|---|---|---
1|1|460|1|1001|GMT+08:00|TA1
2|1|460|1|1002|GMT+08:00|TA2
3|1|460|1|1003|GMT+08:00|TA3
4|1|460|1|1004|GMT+08:00|TA4
5|1|460|1|1005|GMT+08:00|TA5
6|1|460|1|1006|GMT+08:00|TA6
7|1|460|1|1007|GMT+08:00|TA7
8|1|460|1|1008|GMT+08:00|TA8
9|1|460|1|1009|GMT+08:00|TA9
10|1|460|1|1010|GMT+08:00|TA10
11|1|460|2|1011|GMT+08:00|TA11
12|1|460|2|1012|GMT+08:00|TA12
13|2|460|2|1013|GMT+09:00|TA13
14|2|460|2|1014|GMT+09:00|TA14
15|2|460|2|1015|GMT+09:00|TA15
16|2|460|2|1016|GMT+09:00|TA16
17|2|460|2|1017|GMT+09:00|TA17
18|2|460|2|1018|GMT+09:00|TA18
19|2|460|2|1019|GMT+09:00|TA19
20|2|460|2|1020|GMT+09:00|TA20
当UE在TA1接入，上一次在TA10接入时，MME分配的TA list应该为TA1、TA2、…、TA9。 
当UE在TA15接入，上一次在TA20接入，MME分配的TA list应该为TA13、TA14、…、TA20。 
配置步骤
配置步骤参见下表。 
配置说明|配置脚本
---|---
添加TA，配置TA的MNC、MCC、TAC等信息。这里关联的LA是已经配置好的LA。其中本例中TA的时区与MME的全局时区不一致，这里将“是否使用全局时区”设置为否，设置每个TA的时区。|ADD TA:TAID=1,GRPID=1,MCC="460",MNC="01",TAC="1001",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA1"ADD TA:TAID=2,GRPID=1,MCC="460",MNC="01",TAC="1002",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA2"ADD TA:TAID=3,GRPID=1,MCC="460",MNC="01",TAC="1003",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA3"ADD TA:TAID=4,GRPID=1,MCC="460",MNC="01",TAC="1004",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA4"ADD TA:TAID=5,GRPID=1,MCC="460",MNC="01",TAC="1005",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA5"ADD TA:TAID=6,GRPID=1,MCC="460",MNC="01",TAC="1006",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA6"ADD TA:TAID=7,GRPID=1,MCC="460",MNC="01",TAC="1007",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA7"ADD TA:TAID=8,GRPID=1,MCC="460",MNC="01",TAC="1008",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA8"ADD TA:TAID=9,GRPID=1,MCC="460",MNC="01",TAC="1009",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA9"ADD TA:TAID=10,GRPID=1,MCC="460",MNC="01",TAC="1010",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA10"ADD TA:TAID=11,GRPID=1,MCC="460",MNC="01",TAC="1011",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA11"ADD TA:TAID=12,GRPID=1,MCC="460",MNC="01",TAC="1012",GLOBALTZ="NO",TIMEZONE="GMT+08:00",NAME="TA12"ADD TA:TAID=13,GRPID=2,MCC="460",MNC="01",TAC="1013",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA13"ADD TA:TAID=14,GRPID=2,MCC="460",MNC="01",TAC="1014",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA14"ADD TA:TAID=15,GRPID=2,MCC="460",MNC="01",TAC="1015",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA15"ADD TA:TAID=16,GRPID=2,MCC="460",MNC="01",TAC="1016",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA16"ADD TA:TAID=17,GRPID=2,MCC="460",MNC="01",TAC="1017",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA17"ADD TA:TAID=18,GRPID=2,MCC="460",MNC="01",TAC="1018",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA18"ADD TA:TAID=19,GRPID=2,MCC="460",MNC="01",TAC="1019",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA19"ADD TA:TAID=20,GRPID=2,MCC="460",MNC="01",TAC="1020",GLOBALTZ="NO",TIMEZONE="GMT+09:00",NAME="TA20"
配置SGW管理跟踪区参数，SGW name为SGW，管理的跟踪区组为1、2。|ADD SGW:SGWNAME="SGW1",GRPLIST=1ADD SGW:SGWNAME="SGW2",GRPLIST=2
配置动态TA LIST分配策略，本实例中配置TA LIST携带个数为16，打开“TA List必须属于同一时区”开关，打开“TAList必须属于同一PLMN”开关。|SET TALIST ASSIGN POLICY:MAXTANUM=16,SAMETIMEZONE="YES",SAMEPLMN="YES"
###### 静态TA List分配功能配置实例1 
场景说明
客户已规划TA List，跨TA List移动频繁。 
静态TA列表配置说明：licence开关“MME支持TAL静态分配功能”必须开启。 
“打开Last TA优选功能”开关打开，一个静态TA列表ID允许配置的最大TA个数为15。同一个静态TA列表中的TA的组号必须相同，位置区名必须相同。同一个TA只能归属一个静态TA列表ID。 
运营商MME管辖的TA区域和每个TA关联的信息参见下表，TA组号1关联SGW1。 
跟踪区标识|组号|移动国家码|移动网号|跟踪区域码(HEX)|位置区名|跟踪区名|TA列表ID
---|---|---|---|---|---|---|---
1|1|460|1|1001|LA1|TA1|1
2|1|460|1|1002|LA1|TA2|1
3|1|460|1|1003|LA1|TA3|1
4|1|460|1|1004|LA1|TA4|1
5|1|460|1|1005|LA1|TA5|1
6|1|460|1|1006|LA1|TA6|2
7|1|460|1|1007|LA1|TA7|2
8|1|460|1|1008|LA1|TA8|2
9|1|460|1|1009|LA2|TA9|2
10|1|460|1|1010|LA2|TA10|2
当UE在TA5首次接入，MME携带给UE的TA List应该为TA1，TA2，TA3，TA4，TA5。 
当UE从TA5移动到TA6，MME携带给UE的TA List应该为TA5，TA6，TA7，TA8，TA9，TA10。 
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|打开开关“打开静态TA列表功能”和“打开Last TA优选功能”。|SET TALIST POLICY:TALIST="YES",LASTTA="YES"
2|添加静态TA列表。本实例中，TA列表ID1关联TA1，TA2……TA5，TA列表ID2关联TA6，TA7……TA10。|ADD TA LIST:TAID=1&2&3&4&5,TALID=1ADD TA LIST:TAID=6&7&8&9&10,TALID=2
###### 静态TA List分配功能配置实例2 
场景说明
客户已规划TA List，跨TA List移动很少。 
静态TA列表配置说明：licence开关“MME支持TAL静态分配功能”必须开启。 
“打开Last TA优选功能”开关关闭，一个静态TA列表ID允许配置的最大TA个数为16。同一个静态TA列表中的TA的组号必须相同，位置区名必须相同。同一个TA只能归属一个静态TA列表ID。 
运营商MME管辖的TA区域和每个TA关联的信息参见下表，TA组号1关联SGW1。 
跟踪区标识|组号|移动国家码|移动网号|跟踪区域码(HEX)|位置区名|跟踪区名|TA列表ID
---|---|---|---|---|---|---|---
1|1|460|01|1001|LA1|TA1|1
2|1|460|01|1002|LA1|TA2|1
3|1|460|01|1003|LA1|TA3|1
4|1|460|01|1004|LA1|TA4|1
5|1|460|01|1005|LA1|TA5|1
6|1|460|01|1006|LA1|TA6|2
7|1|460|01|1007|LA1|TA7|2
8|1|460|01|1008|LA1|TA8|2
9|1|460|01|1009|LA2|TA9|2
10|1|460|01|1010|LA2|TA10|2
当UE在TA5首次接入，MME携带给UE的TA List应该为TA1，TA2，TA3，TA4，TA5。 
当UE从TA5移动到TA6，MME携带给UE的TA List应该为TA5，TA6，TA7，TA8，TA9，TA10。 
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|打开开关“打开静态TA列表功能”和“打开Last TA优选功能”。|SET TALIST POLICY:TALIST="YES",LASTTA="NO"
2|添加静态TA列表。本实例中，TA列表ID1关联TA1，TA2……TA5，TA列表ID2关联TA6，TA7……TA10。|ADD TA LIST:TAID=1&2&3&4&5,TALID=1ADD TA LIST:TAID=6&7&8&9&10,TALID=2
测试用例 :###### 部署了CSFB业务 
测试项目|MME TA List分配功能测试
---|---
测试目的|TA List分配策略“TAList必须属于同一LA”测试。
预置条件|MME局管辖的20个TA。打开“TA List必须属于同一LA”开关。设置分配策略中分配的TA个数默认为16。
测试过程|460012221234567用户在TA1上线。460023331234567用户在TA15上线。
通过准则|460012221234567用户AttachAccept消息中下发的TA list为TA1、TA2、TA3、TA4、TA5、TA6、TA7。460012221234567用户AttachAccept消息中下发的TA list为TA14、TA15、TA16、TA17、TA18、TA19、T20。
###### TA有不同时区和PLMN 
测试项目|MME TA List分配功能测试
---|---
测试目的|TA List分配策略“TAList必须属于同一时区”的测试。TA List分配策略“TA List必须属于同一PLMN”的测试。
预置条件|MME局管辖的20个TA。打开“TA List必须属于同一时区”开关。打开“TA List必须属于同一PLMN”开关。设置分配策略中分配的TA个数默认为16。
测试过程|用户分别在TA1和TA15上线。
通过准则|当用户在TA1附着时，AttachAccept消息中下发的TA list为TA1、TA2、…、TA9。当用户在TA15附着时，Attach Accept消息中下发的TAlist为TA13、TA14、…、TA20。
###### 已规划TA List，跨TA List移动频繁 
测试项目|MME TA List分配功能测试
---|---
测试目的|TA List静态分配策略的测试。Last TA优选策略的测试。
预置条件|MME局管辖的10个TA。打开licence “MME支持TAL静态分配功能” 开关。设置静态TA列表分配策略中“打开静态TA列表功能”为是。设置静态TA列表分配策略中“打开Last TA优选功能”为否。配置静态TA列表ID1、列表ID2关联的TA。
测试过程|460012221234567用户在TA5上线。460023331234567用户从TA5移动到TA6。
通过准则|460012221234567用户AttachAccept消息中下发的TA list为TA1、TA2、TA3、TA4、TA5。460012221234567用户TAUAccept消息中下发的TA list为原配置TA5、TA6、TA7、TA8、TA9、TA10。
###### 已规划TA List，跨TA List移动很少 
测试项目|MME TA List分配功能测试
---|---
测试目的|TA List静态分配策略的测试。Last TA优选策略的测试。
预置条件|MME局管辖的10个TA如7.2.1节场景所示。打开licence “MME支持TAL静态分配功能” 开关。设置静态TA列表分配策略中“打开静态TA列表功能”为是。设置静态TA列表分配策略中“打开Last TA优选功能”为否。配置静态TA列表ID1、列表ID2关联的TA如7.2.1节场景所示。
测试过程|460012221234567用户在TA5上线。460023331234567用户从TA5移动到TA6。
通过准则|460012221234567用户AttachAccept消息中下发的TA list为TA1、TA2、TA3、TA4、TA5。460012221234567用户TAUAccept消息中下发的TA list为原配置TA6、TA7、TA8、TA9、TA10。
## ZUF-78-01-010 服务节点选择 
概述 :当UE发起局间附着或TAU流程时，MME需要获取从源局获取用户上下文。当接收到源局的IP地址后，本特性用于判断源局是SGSN局或MME局。 
收益 :在局间附着/TAU流程中，为获取用户的EMM上下文和承载上下文，MME判断源局是SGSN局或MME局。 
描述 :当UE发起局间附着或TAU流程时，MME需从源局获取用户的上下文，并判断源局是SGSN局或MME局。MME支持通过下列三种方法进行判断。 
根据MME的Group ID的最大比特位值进行判断。如果最大比特位的值是0，源局为SGSN。如果最大比特位的值是1，源局为MME。 
消息携带的指示符指示源局为SGSN或MME。  
如果组网规划无法实现第一种方法，而消息也没有携带指示符，MME支持设置源局为SGSN和MME，执行DNS查询两次，再使用通过成功查询而获得的地址。 
关于服务节点选择功能的详细信息，请参考3GPP 23.401中的4.3.9 Core Network Node Resolution。 
# 缩略语 
# 缩略语 
## E-RAB 
E-UTRAN Radio Access BearerE-UTRAN无线接入承载
## ECM 
EPS Connection ManagementEPS连接管理
eNodeB :Evolved NodeB演进的NodeB
EPS :Evolved Packet System演进的分组系统
## GBR 
Guaranteed Bit Rate保证比特率
GGSN :Gateway GPRS Support NodeGPRS网关支持节点
GPRS :General Packet Radio Service通用无线分组数据业务
## GUMMEI 
Globally Unique MME Identifier全球唯一移动性管理实体标识
GUTI :Globally Unique Temporary Identity全球唯一临时标识
HLR :Home Location Register归属位置寄存器
HSS :Home Subscriber Server归属用户服务器
## IP-CAN 
IP Connectivity Access NetworkIP连通接入网
LTE :Long Term Evolution长期演进
MME :Mobility Management Entity移动管理实体
NAS :Non-Access Stratum非接入层
## P-TMSI 
Packet Temporary Packet Temporary Mobile Subscriber Identity分组临时移动用户标识
## PCO 
Protocol Configuration Option协议配置选项
PCRF :Policy and Charging Rules Function策略和计费规则功能
PGW :PDN Gateway分组数据网网关
RAT :Radio Access Technology无线接入技术
## RB 
Radio Bearer无线承载
## RIM 
RAN Information Management无线接入网络信息管理
## RRC 
Radio Resource Control无线资源控制
SGSN :Serving GPRS Support Node服务GPRS支持节点
SGW :Serving Gateway服务网关
TA :Tracking Area跟踪区域
TAU :Tracking Area Update跟踪区域更新
UE :User Equipment用户设备
# ZUF-78-02 会话管理 
概述 :功能描述 :会话管理功能是UE与外部建立PDN连接，进行数据业务的基础。 
MME的会话管理功能包括：UE发起的会话管理和网络侧发起的会话管理。 
UE发起的会话管理包括：UE请求PDN连接、UE请求PDN去连接和UE发起的承载资源修改。 
网络侧是最终流程的发起端，网络侧发起的会话管理包括：EPS承载建立、修改和去激活。 
功能特性简介 :会话管理功能详细的特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
专有承载建立|专有承载的建立是为了满足用户业务特定QoS的需求。当需要在已建立的PDN下进行业务，但是该PDN下的承载无法满足QoS需求时，则建立专有承载。专有承载根据类型分为GBR承载和非GBR承载。专有承载建立的触发场景有：网络侧触发。UE承载资源修改触发。附着时默认承载建立同时触发。专有承载建立流程具体可参见3GPP 23.401协议5.4.1 Dedicated bearer activation章节和Annex F Dedicated bearer activation in combination with the default bearer activation at Attach and UE requested PDN connectivity procedures。|ZUF-78-02-001 专有承载建立
PGW触发的带QoS更新的承载修改|带QoS更新的承载修改流程可以修改一个或多个承载的QoS，但是不能修改承载类型，及不能将GBR承载修改为非GBR承载，也不能将非GBR承载修改为GBR承载。带QoS更新的承载修改流程可以修改的QoS参数包括：QCI、GBR、MBR、ARP和APN AMBR。带QoS更新的承载修改触发场景有：PGW触发QoS更新。HSS触发签约QoS修改。UE请求承载资源修改。带QoS更新的承载修改流程具体可参见3GPP 23.401协议5.4.2Bearer modification with bearer QoS update章节。|ZUF-78-02-002 PGW触发的带QoS更新的承载修改
PGW触发的不带QoS更新的承载修改|不带QoS更新的承载修改流程用于修改一个或多个承载的非QoS参数。可以修改参数有：修改默认承载或专有承载的TFT。修改APN-AMBR。不带QoS更新的承载修改触发场景有：PGW触发的不带QoS修改。UE请求承载资源修改。同时，不带QoS更新的承载修改可以获取或发送如下信息：从MME获取位置信息。通知PCO信息给UE。给MME下发指令，比如激活或去活位置上报。PGW触发不带QoS更新的承载修改流程具体可参见3GPP 23.401协议5.4.3PDN GW initiated bearer modification without bearer QoS update章节。|ZUF-78-02-003 PGW发起的无QoS更新的承载修改
承载去激活|承载去激活流程用于MME去激活一个或多个专有承载，或用于PGW去活一个专有承载或一个PDN连接的所有承载。承载去激活触发的场景有：PGW触发承载去激活。MME触发专有承载去激活。UE发起的承载资源修改。承载去激活流程具体可参见3GPP 23.401协议5.4.4 Bearer deactivation章节。|ZUF-78-02-004 承载去激活
UE发起的承载资源修改|当UE需要对承载资源发起改变时，UE发起承载资源修改流程。承载资源修改最终触发的业务流程由PCC/PGW根据业务而定，可能触发的流程有：网络侧发起专用承载激活。网络侧发起专用承载更新流程。网络侧发起专有承载删除流程。UE发起承载资源修改流程具体可参见3GPP 23.401协议5.4.5 UE requested bearer resource modification章节。|ZUF-78-02-005 UE发起的承载资源修改
UE请求PDN连接功能|UE发起PDN连接过程建立一条新的PDN连接，同时建立该PDN连接的默认承载。UE发起PDN连接过程按Request Type可分为：Initial RequestHandoveremergencyUE请求PDN连接流程具体可参见3GPP 23.401协议5.10.2 UE requested PDN connectivity章节。|ZUF-78-02-006 UE请求PDN连接功能
UE或MME请求PDN去连接功能|UE或MME发起PDN去连接过程删除一条PDN连接，去连接过程中该PDN的包括默认承载在内的所有承载被删除。当只有一个PDN连接时，不使用PDN去连接过程，而是使用去附着流程释放所有承载。UE或MME请求PDN去连接流程具体可参见3GPP 23.401协议5.10.3 UE or MME requested PDN disconnection章节。|ZUF-78-02-007 UE或MME请求PDN去连接
支持Local Breakout|用户发生漫游时，如果为漫游用户选择归属地PGW，会导致数据报文迂回，增加网络负担并增加时延，因此3GPP协议引入LBO，即MME为漫游用户选择拜访网络的PGW。在用户签约APN许可LBO且本地策略控制许可LBO时，MME为漫游用户选择拜访网络的PGW，即许可LBO。用户签约APN的VPLMN-Dynamic-Address-Allowed参数为1，则标识该APN许可拜访地接入。本地策略即MME上可以配置禁止LBO的漫游IMSI号段。|ZUF-78-02-008 本地路由疏导控制
PDN重建|对于本网用户，在发生SGW改变的TAU或切换后，MME对于满足特定条件的用户以及该用户当前的PDN连接，发起PDN重建，主要用于语音业务。MME通过向UE发送Detach(携带re-attach required)消息或者Deactivate EPS bearer context request（ESM Cause指示"0x27 Reactivation requested"）消息来发起PDN重建。PDN重建需要满足的条件包括：当前时间在PDN重建功能的生效时间内。用户连接的SGW和PGW不是同一个。特定APN。特定APN和计费特性。MME可以控制PDN重建的时机，在用户处于空闲态到达一定时长后发起PDN重建，或者立即PDN重建。立即PDN重建的场景又包括：用户当前的PDN连接中不存在QCI=1的专有承载，立即发起PDN重建。用户当前的PDN连接中存在QCI=1的专有承载，等待QCI=1的专有承载释放后立即发起PDN重建。|ZUF-78-02-009 PDN重建
## ZUF-78-02-001 专有承载建立 
特性描述 :特性描述 :术语 :术语|含义
---|---
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载。
专用承载|专用承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载。
APN‑AMBR|用来限制相同APN下所有非GBR承载的汇聚最大bit rate的QoS参数。
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载。
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载。
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|在UE和PDN间存在的联系，该联系中有一个IPv4、或一个IPv6地址、或者两者都有，代表一个UE。一个APN代表该PDN。
UE‑AMBR|用来限制每个UE所有非GBR承载的汇聚最大bit rate的QoS参数。
描述 :定义 :专有承载建立流程是用户注册到EPS网络上后，因建立的默认承载或其他专有承载不能满足需求，而由UE或网络侧触发建立专有承载。
由UE或网络侧触发专有承载建立过程中，MME为承载分配EPS承载标识，通知eNodeB，UE建立专有承载，并通知SGW专有承载建立响应，配合完成eNodeB和SGW间的用户面隧道建立。 
专有承载建立完成之后，用户可以通过EPS网络建立的专有承载访问数据业务和其他业务。 
应用场景 :专有承载激活流程是基本流程，用户因业务需求需要通过EPS网络建立的专有承载访问数据业务和其他业务，必须通过专有承载激活流程激活一个新的专有承载。具体常见场景包括： 
PGW发起的专有承载建立。 
用户因业务有特殊的QoS需求而通知MME资源修改，从而触发PGW发起的专有承载建立。 
客户收益 :受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的EPS网络上后，激活专有承载使运营商可以为用户提供各种数据业务和其他业务。
移动终端用户|终端用户因业务有特殊的QoS需求而通知MME资源修改来触发专有承载建立。
实现原理 :系统架构 :EPS网络架构如下图所示。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，比如用户标识、移动性管理状态、用户安全参数等。在专有承载建立过程中，具体功能包括：承载建立，并通知eNodeB，通知MME承载建立响应，发起承载资源修改触发专有承载建立。
eNodeB|为终端的接入提供无线资源，对用户提供接入层安全管理。在专有承载建立过程中，具体功能包括：对用户建立专有承载无线资源，并通知UE建立专有承载，通知MME建立专有承载无线资源响应，透传UE和MME的NAS专有承载建立消息。
MME|控制面功能实体，负责管理和存储UE相关信息，比如用户标识、移动性管理状态、用户安全参数等，为用户分配临时标识，对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。在专有承载建立过程中，具体功能包括：接收到SGW的专有承载请求后，为用户建立专有承载相关信息，并通知UE和eNodeB建立专有承载，给SGW发送专有承载请求响应。MME还处理UE发起的承载资源修改消息，通知到SGW/PGW触发专有承载建立流程。
SGW|用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE的下行数据。管理和存储UE的承载信息，比如IP承载业务参数和网络内部路由信息等。在专有承载建立过程中，具体功能包括：管理和存储UE的承载信息。
PGW|负责将UE接入PDN的网关，给用户分配IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。在专有承载建立过程中，具体功能包括：触发专有承载建立。
PCRF|该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的Qos规则以及计费规则。在专有承载建立过程中，具体功能包括：对专有承载下发QoS策略和计费规则。
本网元实现 :专有承载建立流程属于基本业务流程，实现细节参见下面业务流程的具体描述。 
业务流程 :专有承载激活流程
图2  专有承载激活流程

流程说明： 
如果部署了动态PCC，PCRF发送PCC策略消息给PGW，PCC策略消息中包括了QoS策略信息。如果没有部署动态PCC，PGW使用本地QoS策略。
PGW使用QoS策略为EPS承载分配QoS，包括QCI、APR、MBR和GBR。PGW发送创建承载请求消息给SGW。
SGW发送创建承载请求消息给MME，消息中包括EPS承载的QoS信息。如果UE处于空闲态，MME触发网络侧触发的业务请求流程。 
MME选择一个这个用户还没有使用的EPS Bearer ID。MME构造会话管理消息，消息中包括了EPS承载的QoS（但是不包含ARP）、TFT、PCO、EPS Bearer ID、LBI。MME发送承载建立请求消息给eNodeB，包括了会话管理消息。
eNodeB映射EPS承载的QoS为无线承载的QoS。eNodeB发送RRC连接重新配置消息给UE。 
UE返回RRC连接重新配置完成消息给eNodeB，确认无线承载的激活。
eNodeB返回承载建立响应消息给MME。 
UE构造会话管理响应消息，消息中包括EPS Bearer ID。UE发送直传消息给eNodeB，消息中包含了会话管理消息。 
eNodeB发送上行直传消息给MME，消息中包含了会话管理消息。 
当收到了第7步的从eNodeB发来的E-RAB建立响应消息和第9步的从UE发来的激活专有EPS承载上下文接受消息后，MME给SGW发送创建承载响应消息。 
SGW给PGW发送创建承载响应消息。 
如果是PCRF触发的专有承载建立，PGW给PCRF发送消息，将PCC策略执行的结果通知PCRF。 
UE请求资源修改触发的专有承载激活流程
图3  UE请求资源修改触发的专有承载激活流程

流程说明： 
UE发送请求承载资源修改消息给MME，消息中包括了对应的流的QoS。如果UE处于空闲态，则需要发起业务请求流程。 
MME发送承载资源命令消息给SGW，消息中包括了对应的流的QoS。 
SGW发送承载资源命令消息给PGW，消息中包括了对应的流的QoS。 
PGW可以使用本地配置的QoS策略，或者PGW和PCRF交互，触发PCRF的PCC策略。 
如果请求被接受了，专有承载建立流程被激活。 
如果第4步中，如果PGW和PCRF之间进行了交互，PGW发送消息通知PCRF：PCC策略是否被接受。 
系统影响 :随着专有承载激活数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
应用限制 :该特性不涉及应用限制。 
特性交互 :由于专有承载建立流程是基本业务流程，是后续所有承载相关流程的基础，如果专有承载建立失败，则需要承载在专有承载上的业务都无法使用。 
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"
3GPP TS 23.203: "Policy and charging control architecture"
3GPP TS 23.003: "Numbering, addressing and identification"
3GPP TS 24.007: "Mobile radio interface signalling layer3; General aspects"
特性能力 :名称|指标
---|---
专有承载激活流程完成后，激活了的专有承载数|1个
MME支持最大用户接入数|1500万
MME支持最大承载数|3000万
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :无。 
性能统计 :测量类型|描述
---|---
承载激活流程测量|编号为43007008~430070095的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现专有承载激活流程，详细配置参见初始配置
。
测试用例 :测试项目|PGW触发专有承载建立流程
---|---
测试目的|验证PGW触发专有承载建立流程是否可以顺利完成
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS等网元正常工作。网管可以正常使用。
测试过程|PGW发起专有承载建立。
通过准则|流程正常结束，专有承载建立成功。数据业务正常。用户ECM状态为ECM-CONNECTED，存在默认和专有承载上下文，QoS等信息正确。
测试结果|-
常见问题处理 :对于专有承载建立失败情况，一般是局配置的承载个数少于实际用户数。对于这种情况，需要扩容或者减少签约用户。 
## ZUF-78-02-002 PGW触发的带QoS更新的承载修改 
特性描述 :特性描述 :术语 :术语|含义
---|---
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载
专有承载|专有承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载
APN‑AMBR|用来限制相同APN下所有非GBR承载的汇聚最大bit rate的QoS参数
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程
UE‑AMBR|用来限制每个UE所有非GBR承载的汇聚最大bit rate的QoS参数
描述 :定义 :MME网元承载修改流程是用户注册到EPS网络上后，用户因业务需求需要对承载进行修改，MME配合完成对已经激活承载的QoS,APN-AMBR,或TFT进行修改，MME还完成因APN-AMBR修改而导致UE-AMBR的修改。
由PGW/HSS/UE触发的承载修改过程中，因承载的QoS,APN-AMBR,TFT的修改，或UE-AMBR的修改，MME通知eNB，UE承载的这些相关信息的修改，并通知SGW承载修改响应。被修改的承载可以是默认承载或专有承载。 
承载修改完成之后，用户可以通过EPS网络修改之后的承载访问数据业务和其他业务 
应用场景 :MME网元承载修改流程是基本流程，用户原有激活承载的QoS，APN-AMBR或TFT，用户UE-AMBR不再满足业务需求，可以通过EPS网络修改原有的承载来访问数据业务和其他业务。具体常见场景包括： 
PGW发起的QoS更新，可以修改QoS，APN-AMBR或UE-AMBR。 
HSS发起QoS修改，可以修改QoS，APN-AMBR或UE-AMBR。 
PDN GW发起非QoS更新，可以修改TFT，APN-AMBR或UE-AMBR 
UE请求资源修改触发的承载修改，可以修改QoS，APN-AMBR或UE-AMBR 
客户收益 :受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的EPS网络上激活了承载后，运营商可以修改用户的承载相关信息为用户提供各种数据业务和其他业务
移动终端用户|终端用户因业务有特殊的QoS需求而通知MME资源修改来触发承载修改
实现原理 :系统架构 :EPS网络架构图，如[图1]所示。
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在承载修改过程中具体功能包括承载修改，并通知eNB，MME承载修改响应，发起承载资源修改触发承载修改功能
eNodeB|为终端的接入提供无线资源，对用户提供接入层安全功能。在承载修改过程中具体功能包括修改用户承载的无线资源，并通知UE修改承载，通知MME修改承载无线资源响应，透传UE和MME的NAS承载修改消息
MME|控制面功能实体，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。在承载修改过程中具体功能包括接收到ServingGW的承载修改请求后，为用户修改承载相关信息，并通知UE，eNB修改承载，通知Serving GW的修改承载请求响应。MME还处理UE发起承载资源修改消息通知到PDNGW触发承载修改流程
HSS|永久存储用户签约数据。在承载修改过程中具体功能包括修改用户签约数据的QoS，APN-AMBR或UE-AMBR
SGW|用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。在承载修改过程中具体功能包括管理和存储UE的承载信息
PGW|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。在承载修改过程中具体功能包括触发承载修改
PCRF|该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的Qos(Quality ofService，服务质量)规则以及计费规则。在承载修改过程中具体功能包括对承载下发Qos策略
本网元实现 :本特性需要UE、eNB、MME、SGW、PGW和HSS等网元配合完成，详见业务流程。 
业务流程 :PGW发起的承载QoS更新流程
流程图如[图2]所示。
图2  PGW发起的承载QoS更新流程
流程说明： 
（可选）如果部署了动态PCC，当业务报文过滤器TFT或者APN-AMBR有变化时，PCRF向PGW发送RAR消息，触发承载更新流程。 
如果未部署动态PCC，则当PGW检测到QoS参数有变化时，触发承载更新流程。 
（可选）如果此流程由PCRF触发，则PGW向PCRF回送RAA消息。 
PGW向SGW发送Update Bearer Request消息，该消息中携带TFT、APN-AMBR等信息。 
SGW更新承载上下文，向MME发送Update Bearer Request消息。 
MME向eNodeB发送Downlink NAS Transport消息，消息中可能包括了APN-AMBR（如果APN-AMBR改变了，MME会重新计算UE-AMBR）、TFT和EPS
Bearer Identity和Session Management Request（Modify EPS bearer context
request），其中Session Management Request（Modify EPS bearer context request）是MME构造的消息。 
eNodeB向UE发送Direct Transfer，消息中包括了会话管理消息Session Management Request（Modify
EPS bearer context request）。UE使用uplink packet filter (UL TFT)来决定业务数据流service
data flows和无线承载radio bearer之间的映射关系。 
UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的会话管理响应消息Session
Management Response(Modify EPS bearer context accept)消息，消息包含：EPS Bearer
Identity。 
eNodeB向MME发送Uplink NAS Transport消息，消息包含会话管理消息Session Management
Response（Modify EPS bearer context accept）。 
MME给SGW发送更新承载响应消息Update Bearer Response，确认承载更新，消息包含：EPS Bearer
Identity。 
SGW向PGW响应Update Bearer Response消息确认承载修改，消息包含：EPS Bearer Identity。 
HSS发起的QoS修改流程
流程图如[图3]所示。
图3  HSS发起的QoS修改流程
流程说明： 
HSS发送插入用户数据消息给MME，消息中携带用户的IMSI和用户签约数据。用户签约数据中包含EPS签约的QoS（QCI和ARP）、签约的APN-AMBR和签约的UE-AMBR。
MME更新存储的用户签约数据，给HSS返回插入用户数据确认消息。 
如果仅仅签约的UE-AMBR发生改变，MME重新计算新的UE-AMBR。如果新的UE-AMBR发生改变，MME使用S1-AP
UE上下文修改流程完成UE-AMBR的更新。 
如果QCI、ARP、签约的APN-AMBR发生了改变，并且对应的有PDN连接激活，MME发送修改承载命令消息给SGW。 
SGW发送修改承载命令消息给PGW。 
如果部署了动态PCC，PGW通知PCRF更新后的EPS承载的QoS。 
PCRF给PGW新的PCC策略。 
PGW根据签约QoS的修改，更新每一个PDN连接对应默认承载的QoS。 
PGW发送更新承载请求消息给SGW。 
如果QCI、ARP修改了，可能触发PGW发起的承载QoS更新流程。 
如果QCI和ARP都没有修改，可能触发PGW发起承载非QoS更新流程。 
SGW发送更新承载响应消息给PGW。 
如果第6步中，PGW和PCRF之间交互了，PGW给PCRF发送消息，通知PCRF的PCC策略执行的结果。 
PGW发起承载非QoS更新流程
流程图如[图4]所示。
图4  PGW发起承载非QoS更新流程
流程说明： 
（可选）如果部署了动态PCC，当业务报文过滤器TFT或者APN-AMBR有变化时，PCRF向PGW发送RAR消息，触发承载更新流程。 
如果未部署动态PCC，则当PGW检测到QoS参数有变化时，触发承载更新流程。 
（可选）如果此流程由PCRF触发，则PGW向PCRF回送RAA消息。  
PGW向SGW发送Update Bearer Request消息，该消息中携带TFT、APN-AMBR等信息。 
SGW更新承载上下文，向MME发送Update Bearer Request消息。 
MME向eNodeB发送Downlink NAS Transport消息，消息中可能包括了APN-AMBR（如果APN-AMBR改变了，MME会重新计算UE-AMBR）、TFT和EPS
Bearer Identity和Session Management Request（Modify EPS bearer context
request），其中Session Management Request（Modify EPS bearer context request）是MME构造的消息。 
eNodeB向UE发送Direct Transfer，消息中包括了会话管理消息Session Management Request（Modify
EPS bearer context request）。UE使用uplink packet filter (UL TFT)来决定业务数据流service
data flows和无线承载radio bearer之间的映射关系。 
UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的会话管理响应消息Session
Management Response(Modify EPS bearer context accept)消息，消息包含：EPS Bearer
Identity。 
eNodeB向MME发送Uplink NAS Transport消息，消息包含会话管理消息Session Management
Response（Modify EPS bearer context accept）。 
MME给SGW发送更新承载响应消息Update Bearer Response，确认承载更新，消息包含：EPS Bearer
Identity。 
SGW向PGW响应Update Bearer Response消息确认承载修改，消息包含：EPS Bearer Identity。 
系统影响 :随着承载修改数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
应用限制 :该特性不涉及应用限制。 
特性交互 :由于承载修改流程是基本业务流程，是满足用户因业务需要而修改承载的流程，如果承载修改失败，则用户某些业务需求无法满足。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocolfor Evolved Packet System (EPS); Stage 3"|-
3GPP TS 36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)"|-
3GPP TS 29.274: "General Packet Radio Service(GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS"|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|-
3GPP TS 23.203: "Policy and charging control architecture"|-
3GPP TS 23.003: "Numbering, addressingand identification"|-
3GPP TS 24.007: "Mobile radio interface signallinglayer 3; General aspects"|-
特性能力 :名称|指标
---|---
MME支持最大用户接入数|1500万
MME支持最大承载数|3000万
承载修改流程成功完成后，总承载数|不改变
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :该特性不涉及命令的变化。 
性能统计 :测量类型|描述
---|---
承载修改流程测量|编号为C430080开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置即可。 
测试用例 :测试项目|P-GW触发承载修改流程
---|---
测试目的|验证P-GW触发承载修改流程是否可以顺利完成
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS网管可以正常使用
测试过程|UE完成附着流程，在网络侧建立2个专有承载（ID号为6、7）。P-GW通过S-GW向MME发送Update BearerRequest消息，修改Qos、MBR或GBR
通过准则|-
测试结果|流程正常结束，承载修改成功
测试项目|UE请求资源修改流程触发承载修改
---|---
测试目的|验证UE请求资源修改流程触发承载修改是否可以顺利完成
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS网管可以正常使用
测试过程|UE完成附着流程，在网络侧建立2个专有承载（ID号为6、7）。UE向MME发送Bearer resource modificationrequest，修改6号承载的Qos、MBR、GBR
通过准则|-
测试结果|MME向SGW发送modify Bearer Command，后续流程按照网络侧发起的QOS更新进行处理。
测试项目|HSS触发承载修改流程
---|---
测试目的|验证HSS触发承载修改流程是否可以顺利完成
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS网管可以正常使用
测试过程|UE完成附着流程，在网络侧建立2个专有承载（ID号为6、7）。HSS上修改对应APN的签约数据，修改范围包括UE-AMBR、APN-AMBR、Qos
通过准则|-
测试结果|HSS发出签约数据插入消息后， MME向S-GW发送modify Bearer Command，P-GW触发默认承载的修改流程，修改5号承载
## ZUF-78-02-003 PGW发起的无QoS更新的承载修改 
在MME的承载修改流程中，如果已经在EPS网络上注册的UE需要根据业务需求修改承载，MME修改已激活的承载的APN-AMBR或TFT。由于APN-AMBR修改，MME还需要进行UE-AMBR修改。
在由PDNGW/HSS/UE触发的承载修改过程中，当承载的APN-AMBR或TFT被修改或UE-AMBR被修改，MME通知eNB和UE与承载相关的修改内容，并且向服务GW发送承载修改响应。默认承载和专用承载都可修改。
当承载修改完成后，UE可通过修改的承载在EPS网络接入数据业务和其他业务。
## ZUF-78-02-004 承载去激活 
特性描述 :特性描述 :术语 :术语|含义
---|---
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载
专有承载|专有承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载。
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载。
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|在UE和PDN间存在的联系，该联系中一个IPV4或一个IPV6地址，或者两者都有代表一个UE；一个APN代表该PDN。
描述 :定义 :MME网元承载去激活流程是去活用户的专有承载，或者去活一个PDN连接中的所有承载。 
由PGW/MME/UE触发的承载去激活过程中，MME通知eNB，UE去激活承载，并通知SGW承载去激活响应。被去活的可以是专有承载或一个PDN连接的所有承载。 
承载去激活完成之后，用户不可以再通过EPS网络的被去活的承载访问数据业务和其他业务 
应用场景 :MME网元承载去激活流程是基本流程，用户不再想要通过EPS网络激活的承载访问数据业务和其他业务，可以通过去激活流程删除承载。具体常见场景包括： 
PGW发起的承载去激活，可以去活专有承载或一个PDN连接中的所有承载 
eNB因无线资源无法维持GBR承载，触发MME发起专有承载去激活 
从MME OMC操作发起专有承载去激活 
UE请求资源修改触发的承载去激活 
客户收益 :受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户在EPS网络上激活的承载不再需要时，去激活承载，节省EPS网络资源
移动终端用户|终端用户不可见
实现原理 :系统架构 :EPS网络架构图，如[图1]所示，其中包含了如下网元：
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在承载去激活过程中具体功能包括承载去激活，并通知eNB，MME承载去激活响应，发起承载资源修改触发承载去激活功能。
eNodeB|为终端的接入提供无线资源，对用户提供接入层安全功能。在承载去激活过程中具体功能包括释放用户承载的无线资源，并通知UE去激活承载，通知MME去活承载无线资源响应，透传UE和MME的NAS承载去激活消息。
MME|控制面功能实体，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。在承载去激活过程中具体功能包括接收到ServingGW的承载去激活请求后，去激活承载，并通知UE，eNB去激活承载，通知Serving GW的去活承载请求响应。MME还处理UE发起承载资源修改消息通知到PGW触发承载去激活流程。
HSS|永久存储用户签约数据。在承载去激活过程中具体功能包括删除动态保存的APN and PGW identity对。
SGW|用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。在承载去激活过程中具体功能包括管理和存储UE的承载信息。
PGW|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。在承载去激活过程中具体功能包括触发承载去活。
PCRF|该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的Qos(Quality ofService，服务质量)规则以及计费规则。在承载去激活过程中具体功能包括决策去激活承载。
本网元实现 :MME网元承载去激活特性需要UE、eNB、MME、SGW、PGW和HSS等网元配合完成，详见业务流程。 
业务流程 :PGW发起的承载去激活流程
PGW发起的承载去激活流程示意图如[图2]所示。
图2  PGW发起的承载去激活流程
流程说明如下： 
（可选）如果部署了动态PCC，当UE不再需要访问某些业务时，PCRF向PGW发送RAR消息触发IP-CAN承载修改。 
如果未部署动态PCC，业务结束或MME发起承载去激活请求均可触发PGW发起承载去激活流程。若此流程去激活的是默认承载，则PGW删除全部专有承载资源。 
（可选）PGW删除承载上下文。如果此流程由PCRF触发，则PGW向PCRF响应RAA消息。 
PGW向SGW发送Delete Bearer Request消息，该消息中携带PTI、Cause、EPS Bearer
Identity等信息，如果EPS Bearer Identity为默认承载的EBI，则表示删除整个PDN连接。 
SGW向MME发送Delete Bearer Request消息，消息中包括PTI、Cause、EPS Bearer
Identity等信息，如果EPS Bearer Identity为默认承载的EBI，则表示删除整个PDN连接。 
如果MME已经收到释放E-UTRAN承载的信令，跳过步骤5～13。 
如果释放的是UE的最后一个PDN连接，MME将向UE发送Detach Request消息发起显式去附着流程。如果UE处于ECM-IDLE状态，MME寻呼UE。直接执行11。 
如果释放的不是UE的最后一个PDN连接，MME将向eNodeB发送Deactivate Bearer Request消息，消息中包括EPS
Bearer Identity和Deactivate EPS Bearer Context Request，Deactivate EPS
Bearer Context Request是MME构造一个NAS层消息。 
eNodeB向UE发送RRC Connection Reconfiguration消息，其中包含要释放的EPS Radio
Bearer Identity和NAS Deactivate EPS Bearer Context Request消息。 
UE释放步骤6中RRC Connection Reconfiguration消息指示的无线承载，给eNodeB返回RRC连接重新配置完成消息RRC
Connection Reconfiguration Complete。 
eNodeB向MME响应Deactivate Bearer Response消息确认承载去激活，消息包含：EPS Bearer
Identity。  
UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Deactivate EPS
Bearer Context Accept消息，消息包含：EPS Bearer Identity。 
eNodeB向MME发送Deactivate EPS Bearer Context Accept消息。 
（可选）如果在8a中UE收到了分离请求消息Detach Request，则UE发送分离接受消息Detach Accept给MME。eNodeB连同UE使用的小区的TAI+ECGI信息通过该NAS消息一起透传给MME。 
（可选）如果该PDN连接是UE在某APN下的最后一个PDN连接且其全部承载均被去激活，同时用户签约可以切换到Non-3GPP网络，MME给HSS发送通知请求消息，用于通知HSS删除APN和PGW
ID的对应关系。如果释放PDN连接的原因为“从3GPP到非3GPP的接入方式的改变”，则不需要给HSS发送通知请求消息。 
可选：收到MME发送的Notify reques消息后，HSS删除APN和PGW的对应关系，给MME返回通知响应消息Notify
Response。  
MME删除承载上下文，给SGW发送删除承载响应消息Delete Bearer Response。 
SGW删除承载上下文，给PGW发送删除承载上下文消息Delete Bearer Response。 
（可选）如果UE被显式去附着，MME向eNodeB发送S1 Release Command消息释放与UE间的S1-MME信令连接。 
MME发起的专有承载去激活流程
MME发起的专有承载去激活流程示意图如[图3]所示。
图3   MME发起的专有承载去激活流程
流程说明如下： 
（可选）处于ECM-CONNECTED状态的UE，由于本地原因（例如非正常的资源限制或无线条件不允许eNodeB保持所有的GBR承载），eNodeB会向UE发送Radio
Bearer Release消息释放无线承载资源。UE删除与被释放的无线承载相关的承载上下文。 
当eNodeB释放了无线承载资源后，将发送承载释放指示消息给MME。该指示可能是发给MME的Bearer Release
Request消息，消息包含：EPS Bearer Identity，或者是Initial Context Setup Complete、Handover
Request Ack和UE Context Response消息，Path Switch Request消息也可以指示承载释放。 
MME向每个PDN连接的SGW发送删除承载命令消息Delete Bearer Command，消息包含EPS Bearer
Identity。EPS Bearer Identity是MME选择的需要释放的承载标识。 
SGW向PGW发送删除承载命令消息Delete Bearer Command，消息包含EPS Bearer Identity。 
（可选）如果部署了动态PCC，PGW通过PCEF初始化的IP-CAN会话修改流程，通知PCRF资源的释放。PCRF给PGW提供一个新的PCC策略。如果没有部署动态PCC，PGW采用本地配置的PCC策略。 
PGW向PCRF发送CCR-U消息，通知PCRF更新IP-CAN会话。PCRF授权并进行策略决策。 
PCRF向PGW返回CCA-U消息，包含更新的PCC策略。 
PGW发送删除承载请求消息Delete Bearer Request给SGW，消息包含EPS Bearer Identity。 
SGW发送删除承载请求消息Delete Bearer Request给MME，消息包含EPS Bearer Identity。 
如果是由无线侧触发的承载释放流程，则跳过8~16步骤；否则： 
如果释放的是UE的最后一个PDN连接，MME将向UE发送Detach Request消息，发起显式去附着流程。如果UE处于ECM-IDLE状态，MME寻呼UE。直接执行步骤14。 
如果释放的不是UE的最后一个PDN连接，MME将向eNodeB发送Deactivate Bearer Request消息，消息中包括EPS
Bearer Identity和Deactivate EPS Bearer Context Request，Deactivate EPS
Bearer Context Request是MME构造一个NAS层消息。 
eNodeB向UE发送RRC Connection Reconfiguration消息，其中包含要释放的EPS Radio
Bearer Identity和NAS Deactivate EPS Bearer Context Request消息。 
UE释放步骤9中RRC Connection Reconfiguration消息指示的无线承载，给eNodeB返回RRC连接重新配置完成消息RRC
Connection Reconfiguration Complete。 
eNodeB向MME响应Deactivate Bearer Response消息确认承载去激活，消息包含：EPS Bearer
Identity。 
UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Deactivate EPS
Bearer Context Accept消息，消息包含：EPS Bearer Identity。 
eNodeB向MME发送Deactivate EPS Bearer Context Accept消息。 
（可选）如果在8a中UE收到了分离请求消息Detach Request，则UE发送分离接受消息Detach Accept给MME。eNodeB连同UE使用的小区的TAI+ECGI信息通过该NAS消息一起透传给MME。 
（可选）如果该PDN连接是UE在某APN下的最后一个PDN连接且其全部承载均被去激活，同时用户签约可以切换到Non-3GPP网络，MME给HSS发送通知请求Notify
Request消息，用于通知HSS删除APN和PGW的对应关系。如果释放PDN连接的原因为“从3GPP到非3GPP的接入方式的改变（RAT
changed from 3GPP to Non-3GPP）”，则不需要给HSS发送通知请求消息Notify Request。 
（可选）收到MME发送的Notify request消息后，HSS删除APN和PGW的对应关系，给MME返回通知响应消息Notify
Response。 
MME删除承载上下文，给SGW发送删除承载响应消息Delete Bearer Response。 
SGW删除承载上下文，给PGW发送删除承载上下文消息Delete Bearer Response。 
UE请求资源修改触发的承载去活流程
UE请求资源修改触发的承载去活流程示意图如[图4]所示。
图4  UE请求资源修改触发的承载去活流程

流程说明如下： 
UE发送请求承载资源修改消息给MME，消息中包括了对应的流的QoS。 
如果UE处于空闲态，则需要发起业务请求流程 
MME发送Bearer Resources Command消息给SGW，消息中包括了对应的流的QoS。 
SGW发送Bearer Resources Command消息给PGW，消息中包括了对应的流的QoS。 
PGW可以使用本地配置的QoS策略，或者PGW和PCRF交互，触发PCRF的PCC策略。 
如果请求被接受了，PGW发起的承载去激活流程被激活，如[图2]所示的步骤2~9。
（可选）如果步骤4中，PGW和PCRF之间交互了，PGW发送消息通知PCRF PCC策略是否被接受。 
系统影响 :随着去激活承载数的增加，系统资源占用会一直减少，CPU占用率会相应下降。 
应用限制 :该特性不涉及应用限制。 
特性交互 :承载去激活流程是基本业务流程，承载去激活流程之后，用户不能再通过已去激活的承载访问数据业务和其他业务。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocolfor Evolved Packet System (EPS); Stage 3"|-
3GPP TS 36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)"|-
3GPP TS 29.274: "General Packet Radio Service(GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS"|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|-
l   3GPP TS 23.203: "Policy and chargingcontrol architecture"|-
l   3GPP TS 23.003: "Numbering, addressingand identification"|-
3GPP TS 24.007: "Mobile radio interface signallinglayer 3; General aspects"|-
特性能力 :名称|指标
---|---
MME支持最大用户接入数|1500万
MME支持最大承载数|3000万
承载去激活流程完成后，MME上的承载数|相应减少
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项 
配置项|命令
---|---
删除EPS承载|DELETE EPS BEAR
性能统计 :测量类型|描述
---|---
承载去激活流程测量|编号为C430090开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置即可。 
测试用例 :测试项目|P-GW触发承载去激活流程
---|---
测试目的|验证P-GW触发承载去激活流程是否可以顺利完成
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS网管可以正常使用
测试过程|PDN GW发起承载去激活
通过准则|-
测试结果|流程正常结束，承载去激活成功用户状态为EMM-DEREGISTERED
测试项目|MME触发承载去激活流程
---|---
测试目的|验证ECM-CONNECTED下MME发起专用承载去活，MME能够正确处理
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS网管可以正常使用
测试过程|在MME操作维护台上删除专用承载
通过准则|-
测试结果|流程正常结束，承载去激活成功用户状态为ECM-CONNECTED状态，有默认承载的信息
## ZUF-78-02-005 UE发起的承载资源修改 
特性描述 :特性描述 :术语 :无 
描述 :定义 :MME网元UE请求承载资源修改流程是用户因业务需求请求承载资源建立，修改，释放从而触发网络侧发起承载建立，修改或去激活过程。 
在UE请求承载资源修改过程中，MME通知SGW承载资源修改，触发PGW发起承载建立，修改或去激活过程，MME通知eNB和UE承载或建立，修改，或去激活。 
UE请求承载资源修改过程完成之后，用户可以通过EPS网络新建立的承载或修改后的承载来访问数据业务和其他业务，但不可以再通过被去活的承载访问数据业务和其他业务。 
应用场景 :MME网元的UE请求承载资源修改是基本流程，用户想要通过EPS网络请求承载资源建立，修改或释放，必须通过UE请求承载资源修改流程触发。具体常见场景包括： 
UE因业务请求承载资源分配触发网络侧发起专有承载建立。 
UE因业务请求承载资源修改触发网络侧发起承载修改。 
UE因业务请求承载资源释放触发网络侧发起承载去激活。 
客户收益 :受益方|受益描述
---|---
运营商|满足移动用户各种数据业务的需求。
移动用户|可以享受各种数据业务。
实现原理 :涉及的网元 :UE请求承载资源修改流程需要eNodeB、MME、HSS、SGW、PGW、PCRF的共同配合完成，涉及网元的功能说明如下。 
网元名称|网元作用
---|---
eNodeB|负责建立，修改或删除用户承载的无线资源，并通知UE建立，修改或删除承载，通知MME建立，修改或删除承载无线资源响应，透传UE和MME的NAS承载建立，修改，或删除消息。
HSS|负责删除动态保存的APN and PDN GW identity对。
SGW|负责管理和存储UE的承载信息。
PGW|负责触发承载建立，修改或删除。
PCRF|负责对承载下发Qos策略，决策去激活。
本网元实现 :在UE请求承载资源修改过程中具体功能包括接收到SGW的承载建立，修改或删除请求后，为用户建立，修改或删除承载相关信息，并通知UE，eNB建立，修改或删除承载，通知SGW建立，修改或删除承载请求响应。MME还处理UE发起承载资源修改消息通知到PDN
GW触发承载建立，修改或删除流程。 
业务流程 :UE请求承载资源修改流程示意图如[图2]所示。
图2  *UE请求承载资源修改流程示意图

UE发送请求承载资源修改消息给MME，消息中包括了对应的流的QoS。 
如果UE处于空闲态，则需要发起业务请求流程。 
MME发送承载资源命令消息给SGW，消息中包括了对应的流的QoS。 
SGW发送承载资源命令消息给PGW，消息中包括了对应的流的QoS。 
PGW可以使用本地配置的QoS策略，或者PGW和PCRF交互，触发PCRF的PCC策略。 
如果请求被接受了，专有承载建立流程或PGW发起的承载去激活流程或PGW发起的承载修改流程被激活。 
如果第4步中，PGW和PCRF之间交互了，PGW发送消息通知PCRF PCC策略是否被接受。 
系统影响 :随着UE请求承载资源修改数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocolfor Evolved Packet System (EPS); Stage 3".|-
3GPP TS 36.413: "Evolved Universal Terrestrial AccessNetwork (E-UTRAN); S1 Application Protocol (S1AP)".|-
3GPP TS 29.274: "General Packet Radio Service (GPRS);Evolved GPRS Tunnelling Protocol (eGTP) for EPS".|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".|-
3GPP TS 23.203: "Policy and charging control architecture"|-
3GPP TS 23.003: "Numbering, addressing and identification"|-
特性能力 :UE请求承载资源修改流程完成专有承载建立，或承载修改，或承载去激活。MME支持最大1500万用户接入，支持最大3000万承载。 
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :该特性不涉及命令的变化。 
性能统计 :测量类型|描述
---|---
UE请求承载资源流程测量|编号为43010开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :该功能属于基本功能，无需特别配置。 
## ZUF-78-02-006 UE请求PDN连接功能 
特性描述 :特性描述 :术语 :术语|含义
---|---
默认APN|默认APN是在签约数据中被标识为默认的APN，用于在附着过程中建立默认的PDN连接。
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载
专有承载|专有承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载
APN‑AMBR|用来限制相同APN下所有非GBR承载的汇聚最大bit rate的QoS参数
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程
PDN连接|在UE和PDN间存在的联系，该联系中一个IPV4或一个IPV6地址，或者两者都有代表一个UE；一个APN代表该PDN
描述 :定义 :MME支持UE发起的PDN连接建立，允许UE通过多PDN连接接入一个或多个PDN网络。UE发起的PDN连接流程是指当UE注册到EPS网络上后，UE可以同时激活到不同PGW或相同PGW的多个PDN连接过程。
PDN连接建立的流程与Attach过程中的默认承载建立过程类似，MME为UE选择接入的PGW，建立UE到PGW的PDN连接。多PDN连接流程完成之后，用户可以通过EPS网络申请多个IP地址，建立到不同PGW或相同PGW的多个PDN连接，访问数据业务和其他业务，当UE不再需要通过这个PDN连接访问数据业务和其他业务时，也可以通过去激活PDN连接，释放已申请的IP地址。 
应用场景 :MME网元多PDN连接流程是基本流程，用户可以通过EPS网络申请多个IP地址，建立到不同PGW或相同PGW的多个PDN连接，访问数据业务和其他业务，当用户不再需要通过这个PDN连接访问数据业务和其他业务时，也可以通过去激活PDN连接，释放已申请的IP地址。具体常见场景包括： 
用户请求PDN连接，MME可以为用户连接到不同PGW或相同PGW。 
用户请求PDN去连接，MME为用户去活PDN连接。 
MME请求PDN去连接。 
客户收益 :受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的EPS网络上后，运营商可以为用户激活到不同PDN GW或相同PDN GW的PDN连接提供各种数据业务和其他业务，运营商也可以去激活PDN连接
移动终端用户|对终端用户不可见
实现原理 :系统架构 :EPS网络架构图如[图1]所示。
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在多PDN连接过程中具体功能包括发起PDN激活或去激活流程，激活或去激活PDN连接。
eNodeB|为终端的接入提供无线资源，对用户提供接入层安全功能。在多PDN连接过程中具体功能包括对用户进行PDN连接建立时的承载资源分配，或PDN连接释放时的承载资源释放。
MME|控制面功能实体，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。在多PDN连接过程中具体功能包括完成P-GW的选择，完成PDN连接建立时承载建立，或PDN连接去激活是承载去激活。
HSS|永久存储用户签约数据。在多PDN连接过程中具体功能包括PDN连接建立时存储APN and PDN GW identity对，或PDN连接释放时删除动态保存的APNand PDN GW identity对。
S-GW|用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。在多PDN连接过程中具体功能包括管理和存储UE的承载信息。
PGW|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。在多PDN连接过程中具体功能包括负责UE接入PDN，分配用户IP地址，完成承载管理功能。
PCRF|该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的Qos(Quality ofService，服务质量)规则以及计费规则。在多PDN连接过程中具体功能包括对承载下发Qos策略和计费规则。
本网元实现 :UE请求PDN连接特性需要UE、eNB、MME、SGW、PGW和HSS等网元配合完成，详见业务流程。 
业务流程 :UE请求PDN连接流程
UE请求PDN连接流程示意图如[图2]所示。
图2  UE请求PDN连接流程
流程说明如下： 
UE向eNodeB发送PDN Connectivity Request消息请求建立PDN连接，消息包含：APN、PDN
Type、Protocol Configuration Options、Request Type。 
MME根据APN为UE选择接入的PGW，然后向SGW发送Create Session Request（创建会话请求）消息，请求建立缺省承载，此消息中携带PGW的地址（PDN
GW address）。 
SGW在EPS承载列表中创建一个新的EPS承载，并根据流程第2步中收到的PGW的地址（PDN GW address）向PGW发送Create
Session Request（创建会话请求）消息。 
此消息中包括IMSI, MSISDN, APN, Serving
GW Address for the user plane, Serving GW TEID of the user plane,
Serving GW TEID of the control plane, RAT type, Default EPS Bearer
QoS, PDN Type, PDN Address, subscribed APN-AMBR, EPS Bearer Identity,
Protocol Configuration Options, ME Identity, User Location Information
(ECGI), UE Time Zone等信息。此步流程以后，SGW将缓存从PGW接收的所有下行分组数据报文，直到收到13步的Modify
Bearer Request（修改承载请求）消息，在这之前不能发送下行数据给MME。  
（可选）如果分组核心网部署了动态PCC并且切换指示不存在（未收到Handover Indication信元），PGW发起IP-CAN会话建立过程流程，从而获得UE的默认PCC规则；如果部署了动态PCC并且切换指示存在（收到Handover
Indication信元），PGW发起的IP-CAN会话修改过程通报新的IP-CAN类型；如果未部署动态PCC，PGW使用本地配置的PCC策略。 
P-GW向PCRF发送CCR-I消息，通知PCRF建立IP-CAN会话。 
PCRF授权并进行策略决策。PCRF向P-GW返回CCA-I消息，包含选择的IP-CAN承载建立模式。 
PGW在EPS承载上下文列表中创建一个新的EPS承载，并生成一个计费标识（Charging ID）。PGW返回Create
Session Response（创建会话响应）消息给SGW，其中包括PDN GW Address for the user plane,
PDN GW TEID of the user plane, PDN GW TEID of the control plane, PDN
Type, PDN Address, EPS Bearer Identity, EPS Bearer QoS, Protocol Configuration
Options, Charging Id, APN Restriction, Cause, MS Info Change Reporting
Action (Start)等信息。 
如果SGW接收到MS Info Change Reporting Action(start)指示，SGW存储并报告UE位置改变情况。SGW回应Create
Session Response（创建会话响应）消息给新的MME，其中包括PDN Type, PDN Address, Serving
GW address for User Plane, Serving GW TEID for User Plane, Serving
GW TEID for control plane, EPS Bearer Identity, EPS Bearer QoSProtocol
Configuration Options, APN Restriction, Cause, MS Info Change Reporting
Action (Start), APN-AMBR等信息。 
MME构造激活默认EPS承载上下文请求，给eNodeB发送承载建立请求消息Bearer Setup Request，此消息还包含SGW用户面TEID及地址，其中包含需要发送给UE的PDN
Connectivity Accept消息。 
eNodeB发送RRC连接注册消息RRC Connection Reconfiguration给UE，请求分配空口资源，同时PDN
Connectivity Accept也通过本消息带给UE。 
UE向eNodeB发送RRC Connection Reconfiguration Complete消息。 
eNodeB发送Bearer Setup Response消息给MME，消息中携带了eNodeB的TEID和用于S1-U下行传输的IP地址。 
UE向eNodeB发送Direct Transfer消息，此消息携带PDN Connectivity Complete消息，还携带了EPS
Bearer Identity。 
eNodeB向MME转发PDN Connectivity Complete消息，消息包含：EPS Bearer Identity、NAS
sequence number、NAS-MAC。 
在发送PDN Connectivity Accept消息及UE获取一个PDN地址后，UE后续可以向连通了SGW和PGW的eNodeB发送上行数据包。 
当MME收到第10步的从eNodeB发送过来的Bearer Setup Response消息和第12步的从UE发送过来的PDN
Connectivity Complete消息后，MME给SGW发送Modify Bearer Request消息，消息包含：EPS
Bearer Identity、eNodeB address、eNodeB TEID、Handover Indication。 
如果第13步包含切换指示（Bearer Setup Response消息中携带了Handover Indication），SGW发送Modify
Bearer Request（修改承载请求）消息给PGW，使PGW将数据报文从Non-3GPP接入切换到3GPP接入，通过所建立的缺省承载或者专用EPS承载立即开始给SGW传送数据包。 
PGW向SGW发送Modify Bearer Response（修改承载响应）消息。 
SGW向MME发送Modify Bearer Response（修改承载响应）消息。SGW可以发送缓存的下行报文。 
（可选）MME收到Modify Bearer Response消息后，如果PDN连接请求消息中的“请求类型（Request
Type）”不是“切换”，并且EPS承载已经建立，用户的签约数据指示允许UE切换到Non-3GPP，激活的PDN连接是用户对应APN的第一个PDN连接，并且MME选择了一个不同于HSS中PDN签约上下文中指定的PGW，表明用户可以切换为Non-3GPP接入，MME发送Notify
Request消息给HSS，消息中携带APN和PGW Identity，还需携带PGW所属PLMN信息。通知HSS建立APN和PGW的对应关系。 
（可选）HSS存储APN和PGW的对应关系，给MME返回Notify Response消息。 
UE或MME请求PDN去连接流程
UE或MME请求PDN去连接流程如[图3]所示。
图3  UE或MME请求PDN去连接流程
流程说明如下： 
PDN去连接请求可以被以下情况触发。 
UE发送PDN Disconnection Request消息给MME触发PDN去连接过程。 
MME决定释放PDN连接。 
MME给SGW发送Delete Session Request消息，SGW删除发起去连接的UE的相关承载资源。 
SGW给PGW发送Delete Session Request消息。 
PGW返回Delete Session Response消息给SGW。 
（可选）如果部署了动态PCC，PGW使用PCEF触发的IP-CAN会话终止流程，通知 PCRF对应的IP-CAN会话被释放了。 
SGW返回Delete Session Response消息给MME。 
MME给eNodeB发送Deactivate Bearer Request消息，去活所有和这个PDN连接关联的 承载。 
eNodeB给UE发送RRC Connection Reconfiguration消息，通知UE释放对应的无线承 载资源。 
UE释放对应的无线承载资源，给eNodeB返回RRC Connection Reconfiguration Com-
plete消息。 
eNodeB发送Deactivate Bearer Response消息给MME。 
（可选）如果用户签约数据指示用户被允许从非3GPP到3GPP的切换，去激活的PDN连接也是用户的这个APN的最后一个PDN连接，MME发送Notify
Request消息给HSS，通知HSS删除APN和PGW ID的对应关系。 
（可选）HSS删除APN和PGW ID的对应关系，给MME返回Notify Response消息。 
 说明： 
23.401 R9协议开始，协议上已经没有要求MME发送通知请求消息给HSS了，MME实现时由开关“支持在PDN去连接时通知HSS”控制是否发送通知请求消息给HSS，默认不支持。以上步骤11和12是在开关“支持在PDN去连接时通知HSS”打开情况下的处理描述。 
系统影响 :随着激活PDN连接数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
随着去激活PDN连接数的增加，系统资源占用会逐渐减少，CPU占用率会相应下降。 
应用限制 :该特性不涉及应用限制。 
特性交互 :由于多PDN连接流程是基本业务流程，是满足用户激活到不同PGW或相同PGW来访问业务的流程，如果多PDN连接失败，则用户访问多个不同类型网络的需求无法满足。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocolfor Evolved Packet System (EPS); Stage 3".|-
3GPP TS 36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)"|-
3GPP TS 29.274: "General Packet Radio Service(GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS"|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".|-
3GPP TS 23.203: "Policy and charging control architecture"|-
3GPP TS 23.003: "Numbering, addressing and identification"|-
3GPP TS 24.007: "Mobile radio interface signallinglayer 3; General aspects"|-
特性能力 :名称|指标
---|---
MME支持最大用户接入|1500万
支持最大承载数，该承载可以是PDN连接建立的默认承载。|3000万
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项|命令
---|---
增加EPC APN HOST地址|ADD EPC APN IPADDR
删除EPC APN HOST地址|DEL EPC APN IPADDR
新增EPC APN HOST配置|ADD EPC APN
修改EPC APN HOST配置|SET EPC APN
删除EPC APN HOST配置|DEL EPC APN
查询EPC APN HOST配置|SHOW EPC APN
性能统计 :测量类型|描述
---|---
UE请求承载资源流程测量|编号为C430100开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置即可。 
测试用例 :测试项目|UE请求PDN连接建立流程
---|---
测试目的|验证UE请求PDN连接建立流程是否可以顺利完成
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS网管可以正常使用
测试过程|UE完成附着流程后建立一两个专有承载。UE发起PDN连接建立流程
通过准则|-
测试结果|流程正常结束，PDN连接建立成功。
## ZUF-78-02-007 UE或MME请求PDN去连接 
在MME多PDN连接过程中，当UE在EPS网络注册后，UE同时激活到多个PDNGW或一个固定PDNGW的PDN连接。另外，UE和MME也可去激活PDN连接。
PDN连接过程与附着过程中的默认承载建立过程相似。在这一过程中，选择供UE接入的PDNGW，并在UE和PDN之间建立PDN连接。
在UE或MME发起的PDN去连接过程中，MME通知服务GW和eNB删除PDN连接。
当多PDN连接流程完成后，UE可通过EPS网络申请多个IP地址，建立到不同PDNGW的多个PDN连接或到一个固定PDNGW的PDN连接。这样UE就可使用数据业务和其他业务。当UE不在需要通过PDN连接来使用数据业务和其他业务时，UE可去激活PDN连接，并释放申请的IP地址。
## ZUF-78-02-008 本地路由疏导控制 
概述 :MME控制是否允许漫游用户在VPLMN中选择PGW，而无论该用户的签约数据是否允许其接入VPLMN。 
收益 :MME控制是否允许漫游用户选择VPLMN中的PGW而不是归属PGW。该特性使得运营商可对漫游进行灵活本地路由疏导控制。 
描述 :当MS签约LBO数据时，该特性可使用。 
MME支持基于IMSI号段配置的漫游策略。通过本特性，MME可控制是否允许在一定IMSI号段范围内的漫游用户可在VPLMN中选择PGW，而无论该用户的签约数据是否允许其接入VPLMN。 
## ZUF-78-02-009 PDN重建 
特性描述 :特性描述 :描述 :定义 :PDN重建。是指MME在发现本网用户SGW改变时，对于满足特定条件的用户，发起PDN连接重建。 
背景知识 :一些运营商对国内漫游用户采用Local Breakout方式。用户漫游到外省时，在外省建立的PDN连接，会选择拜访地的PGW。 
由于PGW是锚定点，当用户从外省回到归属地后，还是会接入拜访地的PGW，但此时接入的SGW却是本地的，SGW和PGW之间较远，造成承载资源的浪费，特别是对VoLTE业务造成了语音的时延。 
为了节省承载资源，降低语音时延，对于本网用户，当MME发现用户的SGW发生改变时，会为用户重建PDN连接。重建时PGW就近选择，保证用户接入到本地合一的或距离最近的SGW和PGW。  
应用场景 :本特性有三种推荐的使用场景。 
漫游用户采用Local Breakout方式，在拜访地进行VoLTE语音呼叫，回到归属地后，在该用户处于“空闲态”一段时间后，重建IMS PDN连接。 
漫游用户采用Local Breakout方式，在拜访地进行VoLTE语音呼叫后结束通话，回到归属地后，对该用户立即重建IMS PDN连接。 
漫游用户采用Local Breakout方式，在拜访地进行VoLTE语音呼叫，通话过程中回到归属地，在该用户通话结束后，为其立即重建IMS PDN连接。 
客户收益 :受益方|受益描述
---|---
运营商|节省承载资源，降低语音时延
移动用户|提升VoLTE语音通话体验
实现原理 :系统架构 :PDN重建应用于LBO漫游方式，其组网架构如下图所示。 
图1  LBO漫游方式组网架构

涉及的网元 :网元名称|网元作用
---|---
UE|接受MME的消息指示，重建PDN连接。
eNodeB|建立无线承载，透传NAS消息。
MME|通知UE重建PDN连接；收到UE的PDN建立请求后，重新选择PGW，建立PDN连接。
SGW|基于MME的指示，通知PGW释放需重建的会话后重建会话。
PGW|释放需重建的会话后重建会话。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
S1|ZUF-76-07-009 S1AP
S11|ZUF-76-07-008 GTP
本网元实现 :MME在SGW改变的TAU和切换流程中，基于本地策略判断是否需重建PDN连接。 
MME基于本地策略，在用户处于“空闲态”到达一定时长后重建PDN，或者在TAU成功后立即重建PDN。 
业务流程 :对于本网用户，在发生SGW改变的TAU或切换后，MME对于满足特定条件的用户当前的PDN连接，发起PDN重建。 
MME通过向UE发送Detach(携带re-attach required)消息或者Deactivate EPS bearer context request（ESM Cause指示"0x27 Reactivation requested"）消息来发起PDN重建。 
MME判断PDN重建需要满足的条件，包括： 
当前时间在PDN重建功能的生效时间内 
用户连接的SGW和PGW不是同一个 
特定APN 
特定APN和计费特性 
MME在判断出需要重建PDN连接时，还可以控制PDN重建的时机，包括： 
在用户处于“空闲态”到达一定时长后，重建PDN连接； 
用户当前的PDN连接中不存在QCI=1的专有承载时，立即重建PDN连接； 
用户当前的PDN连接中存在QCI=1的专有承载，在QCI=1的专有承载释放后，立即重建PDN连接。 
PDN重建流程
PDN重建流程如下图所示。 
图2  PDN重建流程

流程说明如下： 
UE和eNodeB发起TAU和切换流程。MME在TAU和切换流程中判断出SGW改变，如果功能开关“支持默认承载重建”打开，则对每个PDN连接，根据配置的“默认承载重建策略”决策是否需要PDN重建。PDN是否重建的条件包括： 
当前时间在PDN重建功能的生效时间内 
用户连接的SGW和PGW不是同一个 
特定APN 
特定APN和计费特性 
TAU和切换流程结束后，MME根据软参“默认承载是否立即重建”决策PDN重建时机。如果不是立即重建，则执行步骤3；如果是立即重建，继续判断需重建的PDN连接中是否存在QCI为1的承载：如果不存在，则执行步骤5，触发PDN重建；如果存在，则执行步骤2。 
PGW触发承载去激活流程，释放QCI为1的承载。MME执行完承载去激活流程后，判断有需要重建的PDN连接，则执行步骤5，触发PDN重建。 
eNodeB或者MME触发S1释放流程，用户进入空闲态。 
MME在空闲态判断有需要重建的PDN连接，则触发业务请求流程。业务请求流程结束后，执行步骤5，触发PDN重建。 
MME对于每个需要重建的PDN连接，向SGW发送Delete Session Request消息。SGW与PGW交互完成会话释放后，向MME返回Delete Session Response消息。 
MME向UE通知PDN重建： 
如果需要重建所有的PDN连接，则MME向UE发送Detach Request消息，携带Re-attach required指示。 
如果需要重建部分PDN连接，则MME向eNodeB发送Deactivate Bearer Request消息，消息中包括Deactivate EPS Bearer Context Request，其中的ESM Cause指示"0x27 Reactivation requested"。 
eNodeB向UE发送RRC Connection Reconfiguration消息，UE释放RRC Connection Reconfiguration消息指示的无线承载，给eNodeB返回RRC连接重新配置完成消息RRC Connection Reconfiguration Complete。 
eNodeB向MME响应Deactivate Bearer Response消息确认承载去激活。 
UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Deactivate EPS Bearer Context Accept消息。 
eNodeB向MME发送Deactivate EPS Bearer Context Accept消息。 
（可选）如果在6a中UE收到了Detach Request，则UE发送Detach Accept给MME。 
（可选）如果该PDN连接是UE在某APN下的最后一个PDN连接，同时用户签约可以切换到Non-3GPP网络，MME给HSS发送通知请求消息，用于通知HSS删除APN和PGW ID的对应关系。HSS收到MME发送的Notify reques消息后，删除APN和PGW的对应关系，给MME返回通知响应消息Notify Response。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401（General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access）|5.10.3 UE or MME requested PDN disconnection
3GPP TS 24.301（Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3）|–
特性能力 :名称|指标
---|---
支持默认承载重建控制的最大APN个数|128（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为ZXUN-UMAC的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|SGW|PGW
---|---|---|---
√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令默认承载重建策略配置SET DEFAULT BEARER REBUILDSHOW DEFAULT BEARER REBUILD基于APN的默认承载重建控制配置ADD REBUILD BEARER APNSET REBUILD BEARER APNDEL REBUILD BEARER APNSHOW REBUILD BEARER APN 
安全变量无新增安全变量 
软件参数表2  新增软件参数软件参数名称用户存在QCI为1的专载时默认承载立即重建策略(787038) 
动态管理无新增动态命令 
性能统计 :性能计数器名称
---
C430090008 默认承载去激活请求次数(重建PDN连接原因)
C430030015 MME发起的EPS去附着请求次数(删除最后一个PDN)
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :通过配置默认承载开关和不同的承载策略，实现PDN重建功能。 
配置前提 :确认MME是否支持默认承载重建功能。如果设置为支持，MME才会启用默认承载重建功能。 
确认本地SGW和PGW的FQDN相同的label数。 
确认需要重建的APN，不同运营商的计费特性（Charging Characteristics）对APN重建要求不同。 
配置过程 :执行[SET DEFAULT BEARER REBUILD]命令，开启默认承载重建功能。
执行[ADD REBUILD BEARER APN]命令，增加重建的APN的策略。
配置实例 :场景说明 :VOLETE用户从外省漫游回本地，SGW改变后立刻对IMS APN进行重建。 
数据规划 :涉及的配置信息参见下表。 
配置项|参数名称|取值
---|---|---
设置MME默认承载重建重建策略|支持默认承载重建|是
起始时间|设置MME默认承载重建重建策略|00:00
结束时间|设置MME默认承载重建重建策略|00:00
空闲态时长(秒)|设置MME默认承载重建重建策略|60
SGW和PGW合一时FQDN相同的Label数|设置MME默认承载重建重建策略|8
新增基于APN的默认承载重建控制配置|APN名称|ims
是否根据CC判断默认承载重建|新增基于APN的默认承载重建控制配置|NO
设置软件参数配置|软件参数ID|786846
软件参数值|设置软件参数配置|1
配置步骤 :设置MME支持默认承载重建功能 
[SET DEFAULT BEARER REBUILD]:RESETBEAR="YES",STARTTIME="00:00",ENDTIME="00:00",IDLEDURATION=60,SAMELABELNUM=8
配置重建的APN 
[ADD REBUILD BEARER APN]:APNNAME="ims",IFREBUILDBASEDCC="NO"
设置立刻重建软参 
[SET SOFTWARE PARAMETER]:PARAID=786846,PARAVALUE=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|PDN重建
---|---
测试目的|当VOLTE用户进行SGW改变的TAU流程时，如果没有QCI为1的承载，在TAU完成后立即重建IMS APN。
预置条件|MME网元运行正常MME开启了IMS APN立即重建配置
测试过程|用户在MME1上建立一个普通APN连接，一个IMS APN连接用户移动到MME2，触发SGW改变的局间TAU，SGW与PGW非合设
通过准则|用户局间TAU后，MME对IMS PDN发起去激活，携带原因值为"Reactivation requested"
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## APR 
Automatic Power Reduction自动功率减小
## eNB 
Evolved Node B演进型基站
EPS :Evolved Packet System演进的分组系统
## GBR 
Guaranteed Bit Rate保证比特率
## GW 
GateWay网关
HSS :Home Subscriber Server归属用户服务器
IMSI :International Mobile Subscriber Identity国际移动用户标识
## MBR 
Maximum Bit Rate最大比特率
MME :Mobility Management Entity移动管理实体
PCC :Policy and Charging Control计费和策略控制
## PCO 
Protocol Configuration Option协议配置选项
PCRF :Policy and Charging Rules Function策略和计费规则功能
PDN :Packet Data Network分组数据网
## QCI 
QoS Class IdentifierQoS类别标识
QoS :Quality of Service服务质量
## RRC 
Radio Resource Control无线资源控制
## TFT 
Traffic Flow Template话务流量模型
UE :User Equipment用户设备
# ZUF-78-03 切换 
概述 :功能描述 :在UE移动过程中，基站根据UE上报的测量报告，确定是否需要切换UE到目标小区或者目标基站。如果需要切换，当切换完成后，UE的信令面和用户面，将切换到目标基站，原有基站的用户信息将被释放，UE可在新的无线接入网中继续使用数据业务和其他业务。源基站可以是E-UTRAN，也可以是UTRAN；目的基站可以是E-UTRAN，也可以是UTRAN。 
如下图所示展示了切换前后，用户的用户面和信令面数据流向变化。 
图1  切换前后数据流的变化

功能特性简介 :针对不同的组网场景、切换所发生的源站与目的站的接入类型不同，MME提供了多种的有效解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
基于X2切换|当源基站和目的基站均为E-UTRAN，且两者之间存在X2接口时，源基站和目的基站先通过X2接口完成用户信息的迁移，然后通知MME用户已经切换到目标基站，MME记录用户当前位置信息，并通知SGW将用户面切换到目标基站。当源基站与目标基站之间无法直接前转数据时，通过MME控制非直传隧道的创建与释放，从而保证切换过程中数据传输的连续性。当目标跟踪区不归属当前SGW管理时，MME根据目标跟踪区重新选择SGW。切换完成后，若UE检查当前移出了当前跟踪区列表，则触发跟踪区更新流程，MME重新给用户分配跟踪区列表，以及GUTI。|ZUF-78-03-001 基于X2切换
基于S1的切换|当源基站和目的基站均为E-UTRAN，两个基站之间无法通过X2接口完成用户信息切换，此时通过MME完成用户从源基站切换到目标基站。当源基站与目标基站之间无法直接前转数据时，通过MME控制非直传隧道的创建与释放，从而保证切换过程中数据传输的连续性。当目标跟踪区不归属当前SGW管理时，MME根据目标跟踪区重新选择SGW。当目标基站归属另外一个MME管理时，源MME通过目标跟踪区选择目标MME，然后通知目标MME用户切换到目标基站。当源站由于某些原因导致切换取消时，MME要释放切换过程中创建用户资源，恢复用户到切换前的状态。切换完成后，若UE检查当前移出了当前跟踪区列表，则触发跟踪区更新流程，MME重新给用户分配跟踪区列表，以及GUTI。|ZUF-78-03-002 基于S1的切换
LTE到3G的切换|MME判断数据前转方式为非直传隧道，通过MME控制非直传隧道的创建与释放，从而保证切换过程中数据传输的连续性。切换过程后，PDN连接对应的网关PGW保持不变。切换完成后，UE触发路由更新流程，SGSN为UE分配P-TMSI。|ZUF-78-03-003 LTE到3G的切换
3G到LTE的切换|MME判断数据前转方式为非直传隧道，通过MME控制非直传隧道的创建与释放，从而保证切换过程中数据传输的连续性。切换过程后，PDN连接对应的网关PGW保持不变。切换完成后，UE触发跟踪区更新流程，MME为UE分配跟踪区列表以及GUTI。|ZUF-78-03-004 3G到LTE的切换
## ZUF-78-03-001 基于X2切换 
特性描述 :特性描述 :术语 :术语|含义
---|---
MME池区|MME池区是指UE在其间移动不需要改变服务MME的区域。一个MME池区内有一个或多个对等的MME。MME池区是由多个TA汇聚。MME池区间可以有交迭。
SGW池区|SGW池区是指UE在其间移动不需要改变服务SGW的区域。一个SGW池区内有一个或多个对等的SGW。SGW池区是由多个TA汇聚。SGW池区间可以有交迭。
默认APN|默认APN是在签约数据中被标识为默认的APN，用于在附着过程中建立默认的PDN连接
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载
专用承载|专用承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载
AMBR|AMBR是用来限制每个UE所有非GBR承载的汇聚最大bit rate的QoS项。
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|在UE和PDN间存在的联系，该联系中一个IPV4或一个IPV6地址，或者两者都有代表一个UE；一个APN代表该PDN
描述 :定义 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。 
在切换过程中，用户的无线连接无缝切换到目的无线接入网络。 
切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。 
应用场景 :MME网元切换流程是基本流程，通过切换流程保证用户在移动过程中数据业务和其他业务不中断。具体常见场景包括： 
用户在有LTE信号的地方移动，MME和SGW不需要改变。 
用户在有LTE信号的地方移动，MME和SGW需要改变。 
用户在有LTE信号的地方移动，MME不需要改变，但SGW需要改变。 
用户在有LTE信号的地方移动，MME需要改变，但SGW不需要改变。 
客户收益 :受益方|受益描述
---|---
运营商|支持切换流程，可以保证用户在移动过程中业务的连续性，保证用户的业务体验，可以极大的增强用户对EPS网络使用的满意度。
移动终端用户|对终端用户不可见


实现原理 :



系统架构 :EPS网络架构图，如[图1]所示。
图1  EPS架构图






涉及的网元 :网元名称|网元作用
---|---
UE|在切换过程中具体功能包括完成无线测量报告，完成RRC连接和RB连接的切换
eNodeB|在切换过程中具体功能包括切换发起的决策，完成RRC连接和RB连接的切换。
MME|在切换过程中具体功能包括完成MME的选择，完成S-GW的选择，完成非直接前转资源的建立，完成承载管理功能
SGW|在切换过程中具体功能包括管理和存储UE的承载信息，进行非直接前转数据的转发。
PGW|是3GPP和非3GPP接入系统的移动性锚点，在切换过程中具体功能包括负责更新承载功能。


本网元实现 :本特性需要UE、eNB、MME、SGW、PGW和HSS等网元配合完成，详见业务流程。 


业务流程 :SGW没有改变的基于X2接口切换流程
SGW没有改变的基于X2接口切换流程示意图如[图2]所示。
图2  SGW 没有改变的基于X2接口切换流程




流程说明如下： 


Target eNodeB发送Path Switch Request消息给MME通知UE已经改变小区，消息中携带目标小区的小区全局标识（TAI+ECGI）以及需要切换路径的EPS承载列表，MME根据TAI确定SGW不需要改变。


MME按每PDN连接发送Modify Bearer Request消息给SGW，通知更新eNodeB用户面信息。


可选：如果SGW从MME收到了用户位置信息，则按每PDN连接给PGW发送Modify Bearer Request消息。消息包含：Serving
GW Address and TEID、User Location Information、和/或UE Time Zone、和/或Serving
Network。 


可选：PGW将Modify Bearer Request消息中变化的参数更新到承载上下文中，并向SGW返回Modify Bearer Response消息。


SGW用新接收的eNodeB地址和TEIDs开始发送下行数据报文给Target eNodeB，并给MME回Modify
Bearer Response消息。


为了辅助Target eNodeB中重排序功能，在路径切换完成之后，SGW立刻发送一个或多个“End Marker”报文给Source
eNodeB。 


MME给Target eNodeB发送Path Switch Request Acknowledge消息，确认路径切换请求完成。


Target eNodeB发送Release Resource消息给Source eNodeB，通知切换成功和触发源eNodeB资源释放。


当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 


SGW改变的基于X2接口切换流程
SGW改变的基于X2接口切换流程示意图如[图4]所示。
图3  SGW改变的基于X2接口切换流程




基于S1接口切换流程
图4  基于S1接口切换流程




流程说明： 


基于如下原因，Source eNodeB决定发起基于S1口的eNodeB间的切换流程。 

 
到Target eNodeB没有X2连接。 

 
Target eNodeB告知Source eNodeB之前的X2-based handover失败。 

 
Source eNodeB收到动态信息。 

 


Source eNodeB向Source MME发送Handover Required消息请求切换，消息中包含：Direct
Forwarding Path Availability、Source to Target transparent container、target
eNodeB Identity、CSG ID、CSG access mode、target TAI、S1AP Cause等参数，MME根据Target
eNodeB Identity判断MME不需要改变。


Source MME选择Target MME，然后向Target MME发送Forward Relocation
Request消息，消息中包括MME UE context, Source to Target transparent container,
RAN Cause, target eNodeB Identity, CSG ID, CSG Membership Indication,
target TAI, MS Info Change Reporting Action (if available), CSG Information
Reporting Action (if available), UE Time Zone, Direct Forwarding Flag,
Serving Network, Local Home Network ID等参数。
Target MME根据TAI判断SGW发生改变。 


Target MME按每PDN连接向Target SGW发送Create Session Request消息，消息包含：bearer context(s) with PDN GW addresses and TEIDs (for GTP-based
S5/S8) at the PDN GW(s) for uplink traffic、Serving Network等参数。


Target SGW向Target MME返回Create Session Response消息。


Target MME向Target eNodeB发送Handover Request消息，消息中包括(EPS
Bearers to Setup, AMBR, S1AP Cause, Source to Target transparent container,
CSG ID, CSG Membership Indication, Handover Restriction List等参数。Target
eNodeB收到消息后会创建UE上下文，包含承载信息和安全上下文。


Target eNodeB回复Handover Request Acknowledge消息，消息中包括EPS
Bearer Setup list, EPS Bearers failed to setup list Target to Source
transparent container等参数。如果UE-AMBR发生了变化，MME重新计算新UE-AMBR，并告知Target
eNodeB。
 说明： 
如果所有default EPS bearers都被目标eNodeB拒绝，则MME拒绝handover。 


可选：如果使用间接转发且S-GW重定位，Target MME向Target SGW发送Create
Indirect Data Forwarding Tunnel Request消息建立转发参数，消息包含：target eNodeB
addresses and TEIDs for forwarding。


可选：Target SGW向Target MME响应Create Indirect Data Forwarding
Tunnel Response消息，消息包含：target Serving GW addresses and TEIDs for
forwarding。


Target MME向Source MME发送Forward Relocation Response消息，消息中包括Cause,
Target to Source transparent container, Serving GW change indication,
EPS Bearer Setup List, Addresses and TEIDs等参数。


可选：如果使用间接转发，Source MME向Source SGW发送Create Indirect
Data Forwarding Tunnel Request消息，消息中包括addresses and TEIDs for
forwarding。


可选：Source SGW向Source MME回复Create Indirect Data Forwarding
Tunnel Response消息，消息中包括Serving GW addresses and TEIDs for forwarding。


Source MME向Source eNodeB发送Handover Command消息，消息中包括Target
to Source transparent container, Bearers subject to forwarding。Bearers
to Release等参数。Bearers subject to forwarding包含地址和用于转发的TEID列表。Bearers
to Release包含需要释放的承载列表。
Source eNodeB在Target to Source transparent
container中构造Handover Command消息，并发送给UE。在收到消息之后，UE将删除没有收到目标小区中相关EPS无线承载的EPS承载。


可选：Source eNodeB通过MME向Source MME发送eNodeB Status Transfer消息。如果没有E-RAB采用PDCP状态保存机制，则Source eNodeB可能不会发送此消息。
发生MME重定位时，Source
MME通过Forward Access Context Notification消息将此消息转发给目标MME。Target
MME向Source MME响应Forward Access Context Acknowledge消息后，向Target
eNodeB发送eNB Status Transfer消息。


Source eNodeB使用直接转发从Source eNodeB到Target eNodeB转发下行链路数据。 


Source eNodeB使用间接转发从Source eNodeB到Target eNodeB转发下行链路数据 


UE成功地同步到目标小区后，向Target eNodeB发送Handover Confirm消息。
从Source eNodeB转发的下行数据包可以发送给UE，同样，从UE发出的上行数据包可以转发给Target SGW，到达PGW。 


Target eNodeB发送Handover Notify给Target MME，消息中包括(TAI+ECGI,
Local Home Network ID等参数。


Target MME向Source MME回复Forward Relocation Complete Notification消息。


Source MME向Target MME响应Forward Relocation Complete Acknowledge消息，并启动定时器T4来监视Source eNodeB和Source
SGW的资源的释放情况。


Target MME为每个PDN连接向Target
SGW发送Modify Bearer Request消息，消息中包括eNodeB address and TEID allocated
at the target eNodeB for downlink traffic on S1 U for the accepted
EPS bearers等参数。
如果PGW请求了User Location Information或者User CSG
information（由UE上下文判断），MME也会在这条信息中包含这两个信元。如果UE的时区（Time Zone）发生了改变，MME在信息中包含UE
Time Zone信元。 


Target SGW为来自PGW的下行通道分配地址和TEIDs，并为每个PDN连接向PGW发送Modify bearer
request消息，消息包含：Serving GW addresses for user plane and TEID(s)、Serving
Network等参数。如果步骤[21]包含了User Location Information 信元、UE Time Zone信元或者User CSG
Information信元，SGW也会在此信息中包含。


PGW更新本地上下文并向Target SGW返回Modify Bearer Response消息。


Target SGW向Target MME发送Modify Bearer Response消息。


当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 


当步骤[20]中的定时器T4超时，Source MME向Source eNodeB发送UE Context Release
Command消息。


Source eNodeB释放与UE相关的资源并向Source MME响应UE Context Release
Complete消息。


当步骤[20]中的定时器超时，且Source MME在Forward Relocation Response消息中收到SGW改变指示，则Source
MME向Source SGW发送Delete Session Request消息删除EPS承载资源，消息包含：Cause,
LBI。Cause指示SGW变更及SGW不要向PGW发起承载删除流程。


Source SGW向Source MME响应Delete Session Response消息。


可选：如果使用间接转发且步骤[20]中的定时器T4超时，Source MME向Source SGW发送Delete Indirect Data
Forwarding Tunnel Request消息，释放为间接转发分配的临时资源。


可选：Source SGW向Source MME响应Delete Indirect Data Forwarding
Tunnel Session Response消息。


可选：如果使用间接转发且步骤[20]中的定时器T4超时，Target MME向Target SGW发送Delete Indirect Data
Forwarding Tunnel Request消息，释放为间接转发分配的临时资源。


可选：Target SGW向Target MME响应Delete Indirect Data Forwarding
Tunnel Session Response消息。






系统影响 :随着用户切换的增加，系统资源占用会增大，CPU占用率会相应上升。 
应用限制 :该特性不涉及应用限制。 
特性交互 :由于切换流程是基本业务流程，能保证用户在移动过程中，正在进行的数据业务和其他业务基本不中断，如果切换失败，则会严重影响到用户使用数据业务和其他业务的体验，增加用户对使用EPS网络的不满。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|-
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocolfor Evolved Packet System (EPS); Stage 3"|-
3GPP TS 36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)".|-
3GPP TS 29.274: "General Packet Radio Service(GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS".|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|-
3GPP TS 23.203: "Policy and charging control architecture"|-
3GPP TS 23.003: "Numbering, addressing and identification"|-
3GPP TS 24.007: "Mobile radio interface signallinglayer 3; General aspects"|-
特性能力 :名称|指标
---|---
一个用户最多S1信令连接数|一条
MME支持最大用户接入数|1500万
MME支持最大承载数|3000万
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|HSS|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项|命令
---|---
新增EPC地址解析配置|ADD EPCHOST
修改EPC地址解析配置|SET EPCHOST
删除EPC地址解析配置|DEL EPCHOST
查询EPC地址解析配置|SHOW EPCHOST
性能统计 :性能计数器名称
---
C430110001 E-UTRAN内局内切换(基于X2)请求次数
C430110002 E-UTRAN内局内切换(基于X2)成功次数
C430110005 E-UTRAN内局间切出请求次数
C430110006 E-UTRAN内局间切出成功次数
C430110007 E-UTRAN内局间切入请求次数
C430110008 E-UTRAN内局间切入成功次数
告警和通知 :告警和通知
---
2114060401 移动性管理类节点不可达
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置即可。 
测试用例 :无 
## ZUF-78-03-002 基于S1的切换 
MME切换过程用于将UE从一个小区切换到另一个小区，同时保证业务连续性。MME切换过程包括基于X2的切换和基于S1的切换。在切换过程中，UE可无缝切换到目的无线接入网。
在切换过程完成后，UE可在新的无线接入网中继续使用数据业务和其他业务。
## ZUF-78-03-003 LTE到3G的切换 
特性描述 :特性描述 :术语 :描述 :定义 :MME的跨RAT流程，指的是当UE从2/3G无线接入进入LTE无线接入，或者从LTE无线接入进入2/3G无线接入时，所涉及的附着、跟踪区/路由区更新、切换以及RIM流程。 
背景知识 :3GPP的无线接入技术（RAT），经历了2G时代的GSM EDGE无线接入（GERAN）、3G时代的通用陆基无线接入（UTRAN）和LTE时代的演进的通用陆基无线接入（E-UTARN）三个阶段；在LTE网络的发展过程中，LTE将与2/3G并存，且有着不同的无线覆盖；如果LTE用户同时签约了2/3G业务，在LTE和2/3G覆盖之间移动，为了保证用户业务的延续性，则需要实现跨RAT的相关流程。 
跨RAT的方式
从无线侧的角度来讲，根据终端和网络的不同能力，以及终端当前所处的状态，实现跨RAT，有小区重选、小区重定向、小区改变指令（CCO）（包括网络辅助的小区改变NACC）和切换等不同的形式。涉及到MME的主要流程包括跟踪区/路由区更新和切换流程；其中NACC还涉及到使用核心网的RIM流程，用来传递对端无线节点系统信息；另外，在跟踪区更新过程中，如果用户没有承载或者无法在LTE下重建承载，跟踪区更新将失败，UE将采用重新附着的方式接入LTE网络 
下表给出了TAU/RAU方式和切换方式的比较。 
项目|TAU/RAU方式|切换方式
---|---|---
UE状态|空闲态或连接态——空闲态|连接态——连接态
空口互操作类型|小区重选/小区重定向/CCO/CCO with NACC|切换
数据传输|可以有数据传输，但过程中数据传输会中断|可以有数据传输，且数据传输不会中断
适用上层业务类型|对PS业务无连续性要求的业务，例如CSFB、即时消息、下载等；对于转换时延有要求业务（如CSFB）的需要使用RIM流程|对PS业务有连续性要求的业务，例如VoIP、流媒体等
跨RAT的关键参数映射
用户临时标识的映射在2/3G网络，SGSN为UE分配的是临时标识是P-TMSI，而在LTE，MME为UE分配的临时标识是GUTI；所以UE在接入到目标网络的时候，就需要将之前网络分配的临时标识，转换为目标网络需要的格式；UE从2G/3G移动到LTEUE在2G/3G网络附着后，SGSN为其分配PTMSI+RAI，此用户移动到LTE网络，UE需要基于之前的PTMSI+RAI映射得到GUMMEI+M-TMSI上报给MME，映射规则如下图所示：图1  PTMSI+RAI映射得到GUTIeNodeB基于GUMMEI查找到MME发送消息，在新局MME中，MME采用以上反逻辑获得用户之前的PTMSI+RAI。UE从LTE移动到2G/3GUE在LTE网络附着后，MME为其分配GUMMEI+MTMSI，此用户移动到2G/3G网络，UE需要基于之前的GUMMEI+MTMSI映射得到PTMSI+RAI上报给SGSN，映射规则如下图所示：图2  GUMMEI+MTMSI映射得到PTMSI+RAIRNC使用P-TMSI中的NRI查找到SGSN。 
QoS参数的映射EPS Qos到Pre-R8 Qos的映射ARPEPS QoS ARP 由Pre-Rel8 QoS ARP 一对一映射表1  Mapping of EPS bearer ARP to pre-Rel-8 ARPEPS Bearer ARP Priority Value Pre-Rel-8 ARP Value1 to H1H+1 to M2M+1 to 153其中H以及M的值根据运营商的需求，在MME上可配置。MBR、GBR对于QCI为GBR的承载，MBR和GBR直接一对一映射。对于QCI为non-GBR的承载，按APN-AMBR除于该PDN连接下non-GBR承载个数进行映射（不能除尽时，取整） 
网元地址解析
对SGSN来说，采用的是GPRS的域名格式，使用A或AAAA来解析GGSN和目标或源SGSN。而对MME网元来说，采用的是EPC的域名格式，使用S-NAPTR过程来解析SGW、PGW、目标或源SGSN、目标或源MME和MSC
VLR地址。 
这里需要说明的是： 
当SGSN不识别eNB时，源RNC将使用RNC ID来标识目标eNB；这样SGSN只需要根据RNC
ID来解析目标MME的地址；由目标MME将RNC ID映射为eNB ID。注：SGSN/MME支持扩展RNC ID。 
当SGSN识别eNB时，源RNC将使用eNB
ID来识别目标eNB；这样SGSN需要根据目标TA或目标eNB ID来解析目标MME的地址；由SGSN将eNB ID映射为RNC ID带给目标MME；目标MME再将RNC
ID映射回eNB ID。注：SGSN/MME支持扩展RNC ID。 
MME收到TAU消息后，判断出GUTI是由P-TMSI+RAI映射而来的，则反向映射获取P-TMSI+RAI，从而解析出老局SGSN的地址。 
PGW的锚定
EPC网络中的PGW具备内嵌GGSN的功能，所以在跨RAT的场景下，只要当SGSN选择的是PGW内嵌的GGSN，PGW就可以作为跨RAT的锚定点，从而保证用户业务的连续性。 
当网络中同时存在GGSN和PGW的场景下，考虑到负荷均衡，需要SGSN能够识别用户的LTE属性，只针对该类用户选择PGW，而其他普通的2/3G用户仍然选择GGSN。 
应用场景 :跨RAT流程主要应用于运营商新建的EPS网络需要和原有的GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。网络中的GGSN升级为PGW，HLR升级为HSS。 
根据终端和网络的不同能力和状态以及不同业务场景的需要，跨RAT可能采用不同的方式，所涉及的MME的切换场景包括： 
3G到LTE的切换 
LTE到3G的切换 
客户收益 :受益方|受益描述
---|---
运营商|支持跨RAT流程，可以保证用户在不同RAT之间移动过程中业务的连续性，保证用户的业务体验，可以极大的增强用户对EPS网络使用的满意度。
移动用户|用户在移动的过程中，保证用户在不同RAT间的业务连续性
实现原理 :系统架构 :在核心网方面，由SGSN负责2/3G接入，而由MME负责LTE接入。所以，跨RAT流程实际上涵盖了所有的SGSN和MME的交互流程。 
MME和GnGp SGSN互操作架构如下图所示： 
图3  MME和Gn/Gp SGSN互操作架构图

图中的Gn/Gp SGSN负责传统的2/3G接入，与MME和HSS之间的接口也是基于GTP的Gn口和基于MAP的Gr口。在跨RAT流程中，对于Gn/Gp
SGSN来说，并不需要识别出对接的网元是MME。 
涉及的网元 :网元名称|网元作用
---|---
UE|跨RAT流程触发，完成安全功能、承载管理、RRC连接和RAB连接的切换等功能。
eNodeB|为UE终端提供无线资源，进行接入层安全功能，完成MME的选择、用户无线资源管理、切换发起的决策和执行等功能。
MME|负责管理和存储UE相关信息，处理MME和UE之间的所有非接入层消息，对用户进行接入控制和安全功能，完成SGW的选择、用户临时标识的分配、TAList的分配，完成SGSN的选择，HSS的选择、承载管理等功能。
SGW|管理和存储UE的承载信息，进行非直接前转数据的转发
PGW|完成更新承载的功能
SGSN|负责管理和存储UE相关信息，为用户分配临时标识，完成用户安全功能，完成用户移动性管理功能和会话管理功能，处理SGSN和UE之间的所有非接入层消息
RNC|为终端接入提供无线资源，完成LTE邻区的切换发起和消息处理，对无线承载资源的建立和删除等。
HSS|主要完成用户的签约数据插入和管理
PCRF|根据用户接入方式和位置信息，完成IP-CAN会话修改过程。
本网元实现 :本特性需要UE、eNB、MME、SGW、PGW和HSS等网元配合完成，详见业务流程。 
业务流程 :跨RAT切换
MME到Gn/Gp SGSN的硬切换和SRNC重定位流程流程示意图如图4所示。图4  MME到Gn/Gp SGSN的硬切换和SRNC重定位流程流程说明：源eNodeB决策发起向UTRAN的切换。此时，上下行用户数据通过如下承载进行传输：Bearer(s) between
UE and source eNodeB、 GTP tunnel(s) between source eNodeB and SGW
、GTP tunnel(s) between SGW and PGW。源eNodeB向old MME发送切换申请消息Handover Required，触发切换流程，消息中携带S1
AP Cause、Target RNC Identifier、Source eNodeB Identifier、Source to
Target Transparent Container。old MME根据Target ID判断不是intra-MME handover，根据Target ID选择new Gn/Gp
SGSN。 old MME向new Gn/Gp SGSN发送前转重定位请求消息Forward Relocation Request，触发切换资源分配流程，消息中携带IMSI、MM Context、PDP Context、Target Identification、RAN
Transparent Container、RANAP Cause。Old MME把承载上下文参数映射到PDP上下文。new Gn/Gp SGSN收到前转重定位请求消息Forward Relocation Request后，创建MM上下文和PDP上下文。new Gn/Gp SGSN向目标RNC发送重定位请求消息Relocation Request，请求建立承载，消息中携带Permanent
NAS UE Identity、Cause、Source RNC To Target RNC Transparent Container、RAB
To Be Setup。对每一个RAB，RAB to be Setup应该包含：RAB ID、RAB parameters、Transport
Layer Address、Iu Transport Association等信息。RAB ID信元对应NSAPI的值，RAB parameter信元提供RAB的QoS参数，Transport
Layer Address 上行用户面地址，Iu Transport Association上行用户面TEID。如果new Gn/Gp
SGSN在RNC和PGW间建立Direct Tunnel，Transport Layer Address为PGW的用户面地址， Iu
Transport Association为PGW的用户面TEID。目标RNC分配请求的资源，并向new Gn/Gp SGSN返回重定位请求确认消息Relocation Request
Acknowledge，消息中携带Target RNC To Source RNC Transparent Container、RABs
Setup、RABs Failed To Setup。每一个RAB to be setup都由一对Transport
Layer Address、Iu Transport Association组成。Transport Layer Address是RNC用户面地址，Iu
Transport Association为下行用户面TEID。Target RNC To Source RNC Transparent
Container包含UE切换所需的所有无线相关信息。目标RNC和new Gn/Gp SGSN间的资源分配过程完成后，new Gn/Gp SGSN向old MME发送前转重定位应答消息Forward Relocation Response，消息中携带Cause、RAN Transparent Container、RANAP
Cause、Target-RNC Information。这条消息指示目标RNC已准备好接收来自原eNodeB的转发下行PDU，即relocation
resource allocation流程成功完成。（可选）如果使用了“Indirect Forwarding”，old MME向SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、MME
Tunnel Endpoint Identifier for Control Plane、MME Address for Control
plane、Target RNC Address and TEID(s) for DL user plane。（可选）SGW创建数据转发隧道，返回创建间接数据转发隧道应答消息Create Indirect Data Forwarding
Tunnel Response，消息中携带Cause、SGW DL TEID(s)。old MME向源eNodeB发送切换命令消息Handover Command，通知其切换准备完成，消息中携带Target
to Source Transparent Container、Bearers Subject to Data Forwarding
List、S1AP Cause。（可选）基于QoS profile，源eNodeB为"Bearers Subject to Data Forwarding
List"中的承载发起数据转发消息Forwarding of Data，消息直接发给目标RNC或者发给SGW。源eNodeB和目标RNC之间的GTP-PDU数据交换是在源eNodeB进行复制，然后通过IP层路由给SGW/目标RNC。在目标RNC没有和UE建立RB之前，下行用户面数据到达时，目标RNC可能根据related QoS profile，缓存或者丢弃到达的下行GTP-PDUs。源eNodeB通过从E-UTRAN切换命令消息HO from E-UTRAN Command，向UE发送交接给目标接入网的命令。消息中携带transparent
container，是准备阶段目标RNC建立的无线侧的参数。UE重配置之后向目标RNC发送RRC消息RRC Message，如：Physical Channel Reconfiguration
Complete消息。目标RNC收到重定位执行触发消息后向new Gn/Gp SGSN发送重定位检测消息Relocation Detect。如果重定位类型为“UE involved”，重定位执行的触发点从Uu接口接收，即：目标RNC在底层探测到UE。Relocation
Detect发送完成后，目标RNC转变为UE的SRNC。目标RNC收到相应的RRC消息后，如：Physical Channel Reconfiguration Complete，即目标RNC和UE使用无线协议成功交换新的“SRNC-ID
+ S-RNTI”后，目标RNC向new Gn/Gp SGSN发送重定位完成消息Relocation Complete，通知核心网切换完成。new Gn/Gp SGSN在收到重定位完成消息Relocation Complete后，向old MME发送前转重定位完成消息Forward Relocation Complete，告知其切换完成。old MME收到消息后，返回前转重定位完成确认消息Forward Relocation Complete Acknowledge。old MME启动资源保护定时器，用于释放源eNodeB和SGW的资源。new Gn/Gp SGSN将用户面切换到目标RNC。new Gn/Gp SGSN向PGW发送更新PDP上下文请求消息Update PDP Context Request，通知下行用户面信息，消息中携带new Gn/Gp SGSN Address、SGSN
Tunnel Endpoint Identifier、QoS Negotiated、serving network identity。如果建立了Direct Tunnel，SGSN向PGW提供RNC's Address for User Plane and
TEID for Downlink data，并需要包含DTI用于指导PGW应用Direct Tunnel specific error
handling流程。PGW更新本地PDP上下文信息并返回更新PDP上下文应答消息Update PDP Context Response，消息中携带PGW Tunnel Endpoint Identifier、UE Info Change Reporting Action。UE发起RAU流程。new Gn/Gp SGSN确认是Inter-RAT Handover流程之后的RAU流程，只执行RAU流程的子集，也就是说，不执行new
Gn/Gp SGSN和old MME之间的上下文传输流程（context transfer procedures）。在RAU流程中new
Gn/Gp SGSN从HSS得到Subscribed QoS profile。当资源保护定时器超时，old MME向SGW发送删除会话请求消息Delete Session Request，请求删除EPS承载资源，消息中携带Cause、Indication。Indication指示SGW不要向PGW发起承载删除流程。SGW向old MME回复删除会话响应消息Delete Session Response，消息中携带Cause。old MME通知源eNodeB释放资源。old MME向源eNodeB发送释放资源消息Release Resources。当源eNodeB收到Release Resources消息，不再需要eNodeB转发数据时，源eNodeB释放其资源。 
Gn/Gp SGSN到MME的硬切换和SRNC重定位流程流程示意图如图5所示。图5  Gn/Gp SGSN到MME的硬切换和SRNC重定位流程流程说明：源RNC决策发起向E-UTRAN的切换。源RNC向old Gn/Gp SGSN发送重定位申请消息Relocation Required，触发重定位流程，消息中携带Relocation
Type、Cause、Source ID、Target ID、Source RNC To target eNodeB Transparent
Container。old Gn/Gp SGSN根据Target ID判断是inter-SGSN重定位，根据Target ID选择new
MME。 old Gn/Gp SGSN向new MME发送前转重定位请求消息Forward Relocation Request，触发重定位资源分配流程，消息中携带IMSI、MM Context、PDP Context、Target Identification、RAN
Transparent Container、RANAP Cause。new MME收到前转重定位请求消息Forward Relocation Request后，创建MM上下文和EPS承载上下文，把PDP上下文参数映射到EPS承载上下文参数。MME选择一个SGW，为每个PDN连接，向SGW发送一个创建会话请求消息Create Session Request，请求SGW创建会话，消息中携带bearer context(s) with
PGW addresses and TEIDs for uplink traffic、APN-AMBR、Serving Network。如果new
MME没有从old Gn/Gp SGSN收到APN-AMBR，将从MBR映射出APN-AMBR并提供给SGW。SGW向new MME返回创建会话应答消息Create Session Response，消息中携带SGW
addresses and uplink TEID(s) for user plane。new MME向目标eNodeB发送切换请求消息Handover Request，请求建立承载，消息中携带Cause、UE
Security Capabilities、Security Context、NAS Security Parameters to
E-UTRAN、EPS Bearers to be setup list、Source to Target Transparent
Container、UE-AMBR。目标eNodeB分配请求的资源，并向new MME返回切换请求确认消息Handover Request Acknowledge，消息中携带Target to Source Transparent Container、EPS Bearers setup list、EPS
Bearers failed to setup list、Cause。（可选）如果使用了“Indirect Forwarding”，new MME向SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、MME
Tunnel Endpoint Identifier for Control Plane、MME Address for Control
plane、Target eNB Address and TEID(s) for DL user plane。（可选）SGW创建数据转发隧道，返回创建间接数据转发隧道应答消息Create Indirect Data Forwarding
Tunnel Response，消息中携带Cause、SGW DL TEID(s)。目标eNodeB和new MME间的资源分配完成后，new MME向old Gn/Gp SGSN发送前转重定位应答消息Forward Relocation Response，消息中携带Cause、RAN Transparent Container、RANAP
Cause、Target-RNC Information。这条消息指示目标eNodeB已经准备好接收来自原RNC的转发下行PDU，即relocation
resource allocation流程成功完成。old Gn/Gp SGSN向源RNC发送重定位命令消息Relocation Command，通知其切换准备完成，消息中携带target
eNodeB To Source RNC Transparent Container、RABs To Be Released、RABs
Subject To Data Forwarding。（可选）基于QoS profile，源RNC进行数据转发，数据转发消息为Forwarding of Data。数据转发需要通过Iu接口进行，源RNC和目标eNodeB之间的GTP-PDU数据交换是在源RNC进行复制，然后通过IP层路由给SGW/目标eNodeB。每一个使用lossless
PDCP的无线承载，与传输相关的GTP-PDU但未被acknowledged PDCP-PDUs复制，并连同相关的下行 PDCP序列号，通过IP层路由给SGW/目标eNodeB。源RNC继续发送复制的下行数据和接收上行数据。在目标eNodeB没有和UE建立RB之前，下行用户面数据到达时，目标eNodeB可能根据related QoS profile，缓存或者丢弃到达的下行GTP-PDUs。转发功能只能用于下行用户数据的转发。在发送RRC消息之前，缺少发送顺序的RAB上下行数据将被缓存在源RNC中。 例如，RRC消息是Physical Channel
Reconfiguration for RNS to RNS relocation 或者Intersystem to UTRAN Handover
for BSS to RNS relocation 或者Handover from UTRAN Command for BSS relocation
或者Handover Command for BSS to BSS relocation。当源RNC准备好之后，源RNC将通过向UE发送RRC Message消息来触发执行relocation of SRNS，这条RRC消息来源于目标eNodeB到源RNC的transparent
container，如Physical Channel Reconfiguration消息，消息中应包括UE信息单元和CN消息单元。当UE完成重新配置之后，向目标SRNC发送RRC消息，如Physical Channel Reconfiguration Complete消息。如果收到带有序列号的Forward
SRNS Context消息，至此和UE的分组交换可以开始了。如果没有收到，目标eNodeB发起所有RAB的数据传输，此时不需要发送顺序。（可选）在UTRAN到E-UTRAN的切换过程中，没有RAN上下文传输。如果源RNC产生任何SRNC上下文，MME向SGSN响应该上下文的接收，而忽略消息的内容。 当UE成功接入目标eNodeB，目标eNodeB将向new MME发送切换通知消息Handover Notify，消息中携带TAI+ECGI。UE将得到从HO from UTRAN Command消息中尚未建立E-RAB的EPS承载，并且在本步骤中不发送NAS消息，在本地将其去激活。new MME在收到切换通知消息Handover Notify消息后，向old Gn/Gp SGSN发送前转重定位完成消息Forward Relocation Complete，告知重定位完成。old Gn/Gp SGSN向new MME响应前转重定位完成确认消息Forward Relocation Complete
Acknowledge。new MME收到消息后启动一个资源保护定时器。new MME为每个PDN连接向SGW发送修改承载请求消息Modify Bearer Request，消息中携带Cause、Tunnel
Endpoint Identifier Control Plane、MME Address for Control Plane、eNodeB
Address(es) and TEID(s) for User Traffic、RAT type、APN-AMBR。如果PGW请求了UE's
location或者User CSG information（由UE上下文决定），MME也会在这条信息中包含这两个信元。如果UE的时区（Time
Zone）发生了改变，MME在信息中包含UE Time Zone信元。SGW向PGW发送修改承载请求消息Modify Bearer Request，消息中携带SGW Address
and TEID、RAT type、Serving Network等信息。PGW更新相关的承载上下文，并向SGW响应修改承载应答消息Modify Bearer Response，消息中携带Default bearer id、APN Restriction。当UE从Gn/Gp
SGSN迁移到MME时，PGW向SGW发送每一个承载上下文的APN Restriction。SGW向new MME返回修改承载应答消息Modify Bearer Response，消息中携带Cause、Default
bearer id、APN restriction。SGW把收到的APN Restriction转发给MME，至此，UE、目标eNodeB、SGW和PGW之间所有承载的用户面路径完成建立。old Gn/Gp SGSN在收到前转重定位完成消息Forward Relocation Complete时，old
Gn/Gp SGSN给源RNC发送Iu连接释放命令消息Iu Release Command。当源RNC的数据转发定时器超时时，源RNC给old Gn/Gp SGSN返回Iu连接释放完成消息Iu Release
Complete。UE发起TAU流程。 new MME确认是Inter-RAT Handover流程之后的TAU流程，只执行TAU流程的子集，也就是说，不执行new
MME和old Gn/Gp SGSN之间的上下文传输流程（context transfer procedures）。在TAU流程中new
MME从HSS得到subscribed UE-AMBR value、subscribed APN-AMBR value和EPS Subscribed
QoS profile。new MME根据subscribed UE-AMBR计算used UE-AMBR，如果计算出的值与给目标eNodeB的值不同，或者subscribed
APN-AMBR与之前的APN-AMBR不同，或者默认承载的QoS与EPS Subscribed QoS profile不同，则new
MME发起HSS修改签约QoS，导致承载修改（HSS Initiated Subscribed QoS Modification）流程。（可选）当资源保护定时器超时，new MME向SGW发送删除间接数据转发隧道请求消息Delete Indirect
Data Forwarding Tunnel Request，请求删除数据转发隧道。（可选）SGW向new MME返回删除间接数据转发隧道应答消息Delete Indirect Data Forwarding
Tunnel Response。 
跨RAT跟踪区更新
跨RAT跟踪区更新主要是指Gn/Gp SGSN到MME的TAU流程，示意图如[图6]所示。
图6  Gn/Gp SGSN到MME的TAU流程

流程说明： 
UE从UTRAN覆盖区域移动到E-UTRAN强信号覆盖区域，UE选择4G网络。UE检测到触发TAU的条件满足，UE发起TAU过程。 
UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，同时携带RRC参数（所选择网络、旧GUMMEI）。如果这个TAU过程是由于负载重均衡而触发的，在RRC参数中不包含旧GUMMEI标识。
eNodeB从RRC参数中的老的GUMMEI和指示的已选择网络参数（Selected Network）得到MME。如果不能得到MME，eNodeB就选择一个MME，并向新的MME转发Tracking Area Update Request消息，并携带一个TAI+ECGI参数和所选择网络。
新的MME根据老的GUTI找到老的S4 SGSN地址，发送一个Context Request消息给老的S4
SGSN以请求用户的移动性管理和会话管理相关信息。如果MME指示它已经对UE进行了鉴权或者老的S4 SGSN对UE进行鉴权，那么老的S4
SGSN会启动一个定时器。
老的S4 SGSN给新的MME回Context Response消息。
（可选）UE、MME和HSS可以完成鉴权和安全功能。如果TAU请求消息的完整性检查失败，鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 
新的MME根据TAI决定SGW不需要改变。新的MME给老的S4 SGSN发送Context Acknowledge消息，携带SGW是否改变的信息。老的S4 SGSN将UE上下文中GW和HSS相关上下文信息标记为无效。这样可以确保如果UE在完成正在进行的TAU过程前回到老的S4
SGSN发起一个RAU过程时能够更新GW和HSS。
如果安全功能没有正确认证UE，则TAU被拒绝，MME将发送拒绝指示给老的S4 SGSN，老的S4 SGSN继续保持原有的UE上下文信息。 
新的MME接收来自老的S4 SGSN的承载上下文信息。MME按照所指定的顺序建立EPS承载，去激活不能建立的EPS承载。如果没有承载上下文，则MME拒绝TAU请求消息。 
新的MME按每PDN连接发送Modify Bearer Request消息给SGW。
（可选）若Modify Bearer Request消息携带的RAT Type发生了变化，或者消息中携带有User Location
Information或UE Time Zone IE，SGW向PGW发送Modify Bearer Request消息。 
（可选）PGW将Modify Bearer Request中变化的参数更新到承载上下文中，并向SGW返回Modify
Bearer Response消息。 
（可选）如果启用了动态PCC，并且PCRF订阅了RAT Type或者位置信息等事件，PGW将发起IP-CAN修改流程把这些信息发送给PCRF。 
SGW更新其承载上下文，给新的MME回Modify Bearer Response消息。SGW已经可以把上行数据报文发送给PGW了。
新的MME给HSS发送Update Location Request消息，获取用户的签约数据。
（可选）如果老的S4 SGSN接收到Context Acknowledge消息，并且用户的Iu连接也存在，老的S4
SGSN在第4步设置的定时器超时时，发送Iu Release Command消息给RNC。
（可选）RNC给老的GnGp SGSN回Iu Release Complete消息。
HSS给新的MME回Update Location Ack消息。如果更新位置请求被HSS拒绝，则MME拒绝来自UE的TAU请求并说明原因。如果所有检查通过，MME构造UE的移动性管理上下文。
MME发送Tracking Area Update Accept消息给UE。如果分配了新的GUTI，则会在Tracking
Area Update Accept消息中携带。如果在Tracking Area Update Request消息中携带了“激活标识”，用户面建立过程和Tracking
Area Update Accept消息发送一起执行。
（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking
Area Update Complete消息确认接收到了TAU接受消息。如果在Tracking Area Update Request消息中没有携带“激活标识”，并且也不是ECM-CONNECTED态下发起的TAU过程，MME释放信令连接。
跨RAT路由区更新
跨RAT路由区更新是指MME到Gn/Gp SGSN的RAU流程，示意图如[图7]所示。
图7  MME到Gn/Gp SGSN的RAU流程

UE从EUTRAN覆盖区域移动到UTRAN强信号覆盖区域，UE选择3G网络。 
UE 向new SGSN发送Routing Area Update Request消息，消息中携带的old
P‑TMSI、old RAI和old P‑TMSI由GUTI映射得到。
new SGSN发送SGSN Context Request消息给old MME以请求用户的移动性管理和会话管理相关信息。由GUTI映射的old
RAI和old P-TMSI可以唯一标识old MME。 
old MME给new SGSN回SGSN Context Response消息。对于new SGSN来说，并不需要识别老局是否是MME。 
由MME会将EPS承载按一对一映射到PDP上下文，同时也会完成QoS参数的映射。 
（可选）如果SGSN Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。 
new SGSN向old MME发送SGSN Context Acknowledge消息。 old MME将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还在进行中，UE向old
MME发起TAU流程时，old MME对GW和HSS的信息进行更新。 
new SGSN发送Update PDP Context Request消息到每个PDP上下文关联的PGW（内嵌GGSN）。
PGW更新PDP上下文中的对端用户面地址信息及QoS等，并向new SGSN返回Update PDP Context
Response消息。
New SGSN发送Update Location Request消息到HSS，指示为普通更新。
（可选）如果HSS有其他SGSN的注册信息，则发送Cancel Location消息到old SGSN，
Cancellation Type设置为Update Procedure。
（可选）old SGSN删除MM和PDP上下文，返回Cancel Location Ack消息给HSS。
HLR发送Insert Subscriber Data消息到new SGSN，带用户签约信息等。
new SGSN返回Insert Subscriber Data Ack消息到HSS。
HSS发送Update Location Ack消息到new SGSN。
New SGSN发送Routing Area Update Accept消息到UE，携带新分配的P-TMSI。
UE发现P-TMSI被重新分配，发送Routing Area Update Complete消息到new
SGSN。
old MME根据SGSN Context Request知道是UE移动到UTRAN，释放eNodeB侧和SGW侧资源，并向SGW发送Delete
Session Request消息告知其释放EPS承载资源，指示SGW不要向PGW发起承载删除流程。 
SGW向old MME响应Delete Session Response消息。 
（可选）如果old MME与UE之间有S1-MME连接，当收到new SGSN发送的SGSN Context Acknowledge消息，old
MME执行S1-AP Release。
RIM
2/3G到LTE的RIM 
图8  RIM

流程说明： 
MME收到S1口eNodeB发过来的S1AP层的RIM消息，解析目的路由地址，转换为Gn接口的RIM消息后发往目的RAN节点归属的SGSN。 
SGSN收到Gn口的RIM消息，解析目的路由地址为本局管理的RAN节点，转换为对应接口的RIM消息发往目的RAN节点。 
SGSN收到Gn/Iu口BSS/RNC发过来的BSSGP/RANAP层的RIM消息，解析目的路由地址，转换为Gn接口的RIM消息后发往目的RAN节点归属的MME。 
MME收到Gn口的RIM消息，解析目的路由地址为本局管理的eNodeB，转换为对应接口的RIM消息发往目的eNodeB。 
系统影响 :随着用户跨RAT的增加，系统资源占用会增大，CPU占用率会相应上升。在进行配置计算时，话务模型需要给出具体的跨RAT的话务量，以便正确计入跨RAT对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3".|
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"|
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS".|
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".|
3GPP TS 23.003: "Numbering, addressing and identification"|
特性能力 :名称|指标
---|---
MME支持最大用户接入数|1500万
MME支持最大承载数|3000万
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表2  新增配置项配置项命令新增eNB和RNC之间的标识映射配置ADD ENB RNC修改eNB和RNC之间的标识映射配置SET ENB RNC删除eNB和RNC之间的标识映射配置DEL ENB RNC查询eNB和RNC之间的标识映射配置SHOW ENB RNC新增TAI和RAI之间的映射配置ADD TAI RAI修改TAI和RAI之间的映射配置SET TAI RAI删除TAI和RAI之间的映射配置DEL TAI RAI查询TAI和RAI之间的映射配置SHOW TAI RAI新增EPC地址解析配置ADD EPCHOST修改EPC地址解析配置SET EPCHOST删除EPC地址解析配置DEL EPCHOST查询EPC地址解析配置SHOW EPCHOST新增SGSN地址解析配置ADD SGSNHOST修改SGSN地址解析配置SET SGSNHOST删除SGSN地址解析配置DEL SGSNHOST查询SGSN地址解析配置SHOW SGSNHOST 
安全变量表3  新增安全变量安全变量命令ARPHIGHPRIORITY：ARP高优先级权重值SET PACKET DOMAIN PARAMETER:ARPHIGHPRIORITY=2,ARPMEDPRIORITY=6ARPMEDPRIORITY：ARP中优先级权重值MMEUNDIRECTFWD：切换中MME支持非直接数据前转SET PACKET DOMAIN PARAMETER:MMEUNDIRECTFWD="YES" 
软件参数表4  新增软件参数软件参数ID软件参数名称65619SGSN支持标准eNB-ID逻辑域名解析65659支持扩展RNC-ID786683SGSN支持Target eNB-ID786684支持根据RA识别RNC65617MME支持RIM RNC-ID解析262283MME RIM流程获取目标SGSN IP时采用的域名格式65542SGSN是否支持RIM功能 65569SGSN支持标准eNB-ID解析 
性能统计 :测量类型|性能计数器
---|---
切换流程测量|编号为C430110009~C430110012的计数器、C430110021~C430110022的计数器
基于TA切换流程测量|编号为C440100011~C440100014的计数器、C440100023~C440100024的计数器
基于TA组切换流程测量|编号为C466410011~C466410014的计数器、C466410023~C466410024的计数器
基于域切换流程测量|编号为C450100011~C450100014的计数器、C450100023~C450100024的计数器
切换分网元测量|编号为C464080027~C464080040的计数器、C464080069~C464080082的计数器
基于QCI的切换流程测量|编号为C464140011~C464140014的计数器、C464140023~C464140024的计数器
基于QCI的切换分网元测量|编号为C464200029~C464200042的计数器
NSA切换流程测量|编号为C466070009~C466070012的计数器、C466070021~C466070022的计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME上通过开启相应的功能开关才能支持LTE到3G的切换。 
配置前提 :eNodeB已与MME对接成功，相应TAI-FQDN解析完成，4G下能附着成功。 
BSC/RNC已与SGSN对接成功，相应APN-FQDN解析完成，2G/3G下能附着、激活。 
MME Group ID最高位为1，LAC最高位不为1，网元不支持“特定MME/SGSN选择方式”。如果网元支持“特定MME/SGSN选择方式”则RAU或TAU时的域名解析可能为GPRS/EPC格式。 
配置过程 :详见实例配置 
配置实例 :###### 2G/3G到4G的TAU 
场景说明
用户从SGSN下TAU至MME，用户在SGSN下的LAC为1001(十六进制)，RAC为01，PLMN为46011。 
配置步骤
在DNS服务器上配置old RAI解析到SGSN的GTPC地址。 
解释说明
DNS根据old RAI解析到SGSN的GTPC地址。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { type master;file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@IN  SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (Serial3600 ;Refresh 900;Retry                                              604800       ;Expire                                              3600 )        ;Minimum         IN     NS    jsdns1.mnc011.mcc460.3gppnetwork.org.         IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.   IN   NAPTR order  pref.  flag     service     regexp      replacement$ORIGIN rac.epc.mnc011.mcc460.3gppnetwork.org.rac0001.lac1001  IN  NAPTR  100    100    "a"   "x-3gpp-sgsn:x-gn:x-gp"   ""     sgsn01.rac.epc.mnc011.mcc460.3gppnetwork.org.sgsn01       IN     A   1.1.1.1
###### 4G到2G/3G的RAU 
场景说明
用户从MME下RAU至SGSN，MME的PLMN为46011，MME Group ID为32769（十六进制为8001），MME
Code为01。 
配置步骤
在SGSN网元上配置MME地址解析。 
解释说明
解析MMECI映射的old RAI到MME的GTPC地址。
配置脚本
ADD SGSNHOST:NAME="rac0001.lac8001.mnc011.mcc460.gprs",IPADDR="2.2.2.2";
###### 3G到4G的切换 
Relocation Required携带Target
RNC-ID
场景说明RNC发起切换要求的Relocation Required消息中携带Target
RNC-ID参数，其中RNC ID值为真实eNodeB ID映射的虚拟值；RAI值为真实TAI映射的虚拟值。 
eNodeB
ID值为12345（十进制），RNC-ID为100(十进制)，PLMN为46011，TAC为8001（十六进制），LAC为1001（十六进制），RAC为01（十六进制）。 
配置步骤SGSN配置切换目标地址解析 
解释说明
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME；不使用本地解析的情况下，则在DNS服务器上进行配置域名解析。
配置脚本
ADD SGSNHOST:NAME="rnc0064.mnc011.mcc460.gprs",IPADDR="2.2.2.2";
MME配置eNB和和RNC之间的标识映射 
解释说明
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME。
配置脚本
ADD ENB RNC:MCC="460",MNC="11",RNC=100,ENB=12345;
MME配置TAI和RAI之间的映射 
解释说明
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME。
配置脚本
ADD TAI RAI:MCC="460",MNC="11",LAC="1001",RAC="01",TAC="8001";
SGSN配置支持扩展RNC-ID 
解释说明
本配置可选，在映射的RNC-ID不大于4095时，可不用配置。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65659,PARAVALUE=1;
Relocation Required携带Target eNB-ID
场景说明RNC发起切换要求的Relocation Required消息中携带Target eNB-ID参数，eNodeB
ID值为123456（十进制），TAC为8001（十六进制），PLMN为46011。 
规划一个RNC ID值为真实eNodeB
ID映射的虚拟值；RAI值为真实TAI映射的虚拟值： 
eNodeB ID值为123456（十进制）<--->RNC-ID为100(十进制) 
TAC为8001（十六进制）<--->LAC为1001（十六进制），RAC为01（十六进制） 
配置步骤SGSN、MME均配置eNB和和RNC之间的标识映射 
解释说明
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME。
配置脚本
ADD ENB RNC:MCC="460",MNC="11",RNC=100,ENB=123456;
SGSN、MME均配置TAI和RAI之间的映射 
解释说明
在SGSN网元上配置映射的RNC-ID的解析，目标地址为MME。
配置脚本
ADD TAI RAI:MCC="460",MNC="11",LAC="1001",RAC="01",TAC="8001";
SGSN设置支持Target eNB-ID 
解释说明
SGSN支持Target eNB-ID
配置脚本
SET SOFTWARE PARAMETER:PARAID=786683,PARAVALUE=1
SGSN支持标准eNB-ID逻辑域名解析 
解释说明
SGSN支持标准eNB-ID逻辑域名解析，使用TAI解析目标MME。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65619,PARAVALUE=0;
在DNS服务器上配置TAI-FQDN或eNB-FQDN解析到MME的GTPC地址 
解释说明
DNS根据TAI-FQDN或eNB-FQDN解析到MME的GTPC地址，软参65619决定使用TAI-FQDN还是eNB-FQDN。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { typemaster; file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@      IN     SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (                                               2013072800       ;Serial                                               3600 ;Refresh                                              900           ;Retry                                              604800       ;Expire                                              3600 )        ;Minimum        IN     NS    jsdns1.mnc011.mcc460. 3gppnetwork.org.        IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.    IN   NAPTRorder  pref.  flag     service     regexp      replacement $ORIGINtac.epc.mnc011.mcc460.3gppnetwork.org.tac-lb01.tac-hb80  IN   NAPTR 100   100    "a"   x-3gpp-mme:x-gn:x-gp"   ""       mme01.tac.epc.mnc011.mcc460.3gppnetwork.org.mme01     IN     A   2.2.2.2$ORIGIN enb.epc.mnc011.mcc460.3gppnetwork.org.enb1e240 IN   NAPTR  100   100    "a"   x-3gpp-mme:x-gn:x-gp"   ""    mme01.enb.epc.mnc011.mcc460.3gppnetwork.org.mme01      IN     A   2.2.2.2
SGSN配置支持扩展RNC-ID 
解释说明
本配置可选，在映射的RNC-ID不大于4095时，可不用配置。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65659,PARAVALUE=1;
###### 4G到3G的切换 
场景说明
用户从MME下切换至SGSN，目标RNCID为200。 
配置步骤
在DNS服务器上配置RNC ID解析到SGSN的GTPC地址。 
解释说明
DNS根据old RAI解析到SGSN的GTPC地址。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { typemaster; file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@      IN     SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (                                               2013072800       ;Serial                                               3600 ;Refresh                                              900           ;Retry                                              604800       ;Expire                                              3600 )        ;Minimum        IN     NS    jsdns1.mnc011.mcc460. 3gppnetwork.org.        IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.    IN   NAPTRorder  pref.  flag     service     regexp      replacement $ORIGINrnc.epc.mnc011.mcc460.3gppnetwork.org.rnc00c8  IN   NAPTR  100   100    "a"   "x-3gpp-sgsn:x-gn:x-gp"   ""     sgsn01.rnc.epc.mnc011.mcc460.3gppnetwork.org.sgsn01       IN     A   1.1.1.2
###### 3G到4G的RIM 
场景说明
RNC发起3G到4G的RIM流程，携带Target
ID为目标eNodeB ID，SGSN使用TA构造FQDN解析MME地址。eNodeB ID值为12345（十进制），TAC为8001（十六进制），PLMN为46011。 
配置步骤
在SGSN网元上打开RIM开关 
解释说明
配置SGSN支持RIM。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1;
在SGSN网元上打开支持3G到4G RIM开关 
解释说明
配置SGSN支持3G到4G的RIM。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65569,PARAVALUE=3;
在SGSN网元上配置MME地址域名解析格式 
解释说明
配置MME地址域名解析格式为TA FQDN格式。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65619,PARAVALUE=0;
在DNS服务器上配置TAI FQDN解析到MME的GTPC地址 
解释说明
DNS根据TAI FQDN解析到MME的GTPC地址。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { typemaster; file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@      IN     SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (                                               2013072800       ;Serial                                               3600 ;Refresh                                              900           ;Retry                                              604800       ;Expire                                              3600 )        ;Minimum        IN     NS    jsdns1.mnc011.mcc460. 3gppnetwork.org.        IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.    IN   NAPTRorder  pref.  flag     service     regexp      replacement $ORIGINtac.epc.mnc011.mcc460.3gppnetwork.org.tac-lb01.tac-hb80  IN   NAPTR 100    100    "a"  "x-3gpp-mme:x-gn:x-gp"   ""      mme01.tac.epc.mnc011.mcc460.3gppnetwork.org.mme01      IN     A   1.1.1.3
###### 4G到3G的RIM 
场景说明
eNodeB发起4G到3G的RIM流程，携带Target
ID为目标RNC ID，MME使用RNC ID的EPS域名格式解析SGSN地址。RNCID为200（十进制），PLMN为46011。 
配置步骤
在MME网元上打开支持4G到3G RIM开关 
解释说明
配置MME支持4G到3G的RIM。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65617,PARAVALUE=1;
在MME网元上配置使用EPS格式解析SGSN地址 
解释说明
配置使用EPS格式的RNC ID FQDN解析SGSN地址。
配置脚本
SET SOFTWARE PARAMETER:PARAID=262283,PARAVALUE=1;
在DNS服务器上配置RNCID FQDN解析到SGSN的GTPC地址 
解释说明
DNS根据RNCID FQDN解析到SGSN的GTPC地址。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { typemaster; file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@      IN     SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (                                               2013072800       ;Serial                                               3600 ;Refresh                                              900           ;Retry                                              604800       ;Expire                                              3600 )        ;Minimum        IN     NS    jsdns1.mnc011.mcc460. 3gppnetwork.org.        IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.    IN   NAPTRorder  pref.  flag     service     regexp      replacement $ORIGINrnc.epc.mnc011.mcc460.3gppnetwork.org.rnc00c8  IN   NAPTR  100   100    "a"  "x-3gpp-sgsn:x-gn:x-gp"   ""      sgsn01.rnc.epc.mnc011.mcc460.3gppnetwork.org.sgsn01       IN     A  1.1.1.4
在SGSN网元上打开RIM开关 
解释说明
配置SGSN支持RIM
配置脚本
SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1;
###### 2G到4G的RIM 
场景说明
BSC发起2G到4G的RIM流程，携带Target
ID为目标eNodeB ID，SGSN使用TA构造FQDN解析MME地址。eNodeB ID值为12345（十进制），TAC为8001（十六进制），PLMN为46011。 
场景说明
在SGSN网元上打开RIM开关 
解释说明
配置SGSN支持RIM。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1;
在SGSN网元上打开支持2G到4G RIM开关 
解释说明
配置SGSN支持2G到4G的RIM。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65569,PARAVALUE=3;
在SGSN网元上配置MME地址域名解析格式 
解释说明
配置MME地址域名解析格式为TA FQDN格式。
配置脚本
SET SOFTWARE PARAMETER:PARAID=65619,PARAVALUE=0;
在DNS服务器上配置TAI FQDN解析到MME的GTPC地址 
解释说明
DNS根据TAI FQDN解析到MME的GTPC地址。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { typemaster; file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@      IN     SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (                                               2013072800       ;Serial                                               3600 ;Refresh                                              900           ;Retry                                              604800       ;Expire                                              3600 )        ;Minimum        IN     NS    jsdns1.mnc011.mcc460. 3gppnetwork.org.        IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.    IN   NAPTRorder  pref.  flag     service     regexp      replacement $ORIGINtac.epc.mnc011.mcc460.3gppnetwork.org.tac-lb01.tac-hb80  IN   NAPTR 100    100    "a"  "x-3gpp-mme:x-gn:x-gp"   ""      mme01.tac.epc.mnc011.mcc460.3gppnetwork.org.mme01      IN     A   1.1.1.5
###### 4G到2G的RIM 
场景说明
eNodeB发起4G到2G的RIM流程，携带Target
ID为目标Cell ID，MME使用RAI的EPS域名格式解析SGSN地址。LAC为1001（十六进制），RAC为01（十六进制）。 
配置步骤
在MME网元上配置使用EPS格式解析SGSN地址 
解释说明
配置使用EPS格式的RAI FQDN解析SGSN地址。
配置脚本
SET SOFTWARE PARAMETER:PARAID=262283,PARAVALUE=1;
在DNS服务器上配置RAI FQDN解析到SGSN的GTPC地址 
解释说明
DNS根据RAI FQDN解析到SGSN的GTPC地址。
配置脚本
1、配置ZONEzone " mnc011.mcc460.3gppnetwork.org" { typemaster; file "db.epc. mnc011.mcc460 "; };2、配置RR，文件名为db.epc.mnc011.mcc460$TTL 3600@      IN     SOA jsdns1.mnc011.mcc460.3gppnetwork.org. . (                                               2013072800       ;Serial                                               3600 ;Refresh                                              900           ;Retry                                              604800       ;Expire                                              3600 )        ;Minimum        IN     NS    jsdns1.mnc011.mcc460. 3gppnetwork.org.        IN     NS    jsdns2.mnc011.mcc460. 3gppnetwork.org.    IN   NAPTRorder  pref.  flag     service     regexp      replacement $ORIGINrac.epc.mnc011.mcc460.3gppnetwork.org.rac0001.lac1001  IN   NAPTR 100    100    "a"  "x-3gpp-sgsn:x-gn:x-gp"   ""       sgsn01.rac.epc.mnc011.mcc460.3gppnetwork.org.sgsn01       IN     A   1.1.1.5
在SGSN网元上打开RIM开关 
解释说明
配置SGSN支持RIM
配置脚本
SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1;
调整特性 :无 
测试用例 :测试项目|3G到4G的TAU
---|---
测试目的|验证SGSN、MME能正确处理3G到4G的TAU
预置条件|LTE,3G网络内的所有网元运行正常，OM维护正常。用户在HSS/HLR开户，并签约2G/3G业务和LTE业务。打开消息跟踪。
测试过程|用户附着到3G网络。用户发起FTP业务，并一直保持。用户移动到LTE网络覆盖区域，发起TAU流程。检查网络侧用户信息和测试信令。
通过准则|用户在3G附着成功。用户正常进行FTP下载。TAU请求消息中携带GUTI等参数。创建缺省承载成功。MME/SGSN向HSS/HLR发起Update Location流程。HSS/HLR向MME/SGSN发起Cancel Location流程。用户在LTE附着成功。FTP业务能够继续。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|4G到3G的RAU
---|---
测试目的|验证MME\SGSN正确处理UE发起的RAU
预置条件|LTE,3G网络内的所有网元运行正常，OM维护正常。用户在HSS/HLR开户，并签约2G/3G业务和LTE业务。打开消息跟踪。
测试过程|用户附着到LTE网络。MME发起S1 Release流程。UE从LTE小区移动到3G小区，发起RAU流程。检查网络侧用户信息和测试信令。
通过准则|用户在LTE网络附着成功。用户转换为ECM-IDLE态。RAU请求消息携带P-TMSI等参数。MME/SGSN向HSS/HLR发起Update Location流程。HSS/HLR向MME/SGSN插入用户签约数据。用户在3G RAU成功。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|3G到4G的切换
---|---
测试目的|验证UTRAN到E-UTRAN的切换，SGSN、MME能够正确处理
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。RNC上配好了到EPS的Handover的相关配置。UE已经通过RNC附着到GPRS网络，至少激活了一个PDP上下文，且正在进行数据业务。在MME上建立S1接口跟踪，用户跟踪，GTPC跟踪。PDN GW支持GGSN功能。
测试过程|UE逐渐从RNC覆盖区移动到eNodeB覆盖区，Source RNC触发Handover流程。在网络侧查询用户的信息。
通过准则|Handover流程成功，MME选择了一个SGW。切换之后数据业务正常。GnGp SGSN上没有用户的信息。MME上用户EMM状态为EMM-REGISTERED，ECM状态为ECM-CONNECTED。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|4G到3G的切换
---|---
测试目的|验证E-UTRAN到UTRAN的切换，SGSN、MME能够正确处理
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB上配好了到GPRS的Handover的相关配置。UE已经通过eNodeB附着到EPS网络，且正在进行数据业务。在MME上建立S1接口跟踪，用户跟踪，GTPC跟踪。PDN GW支持GGSN功能。
测试过程|UE逐渐从eNodeB覆盖区移动到RNC覆盖区，Source eNodeB触发Handover流程。在网络侧查询用户的信息。
通过准则|Handover流程成功。切换之后数据业务正常。MME上没有用户的信息，GnGp SGSN上用户状态为connected状态。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|3G到4G的RIM
---|---
测试目的|验证UTRAN到E-UTRAN的RIM，SGSN、MME能够正确处理
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。RNC和SGSN上配好了到EPS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|RNC发起3G到4G的RIM流程，Target ID携带目标eNodeB ID。在MME和SGSN上检查信令流程。
通过准则|SGSN收到RNC的RIM消息后，通过解析获取目标MME地址，并将RIM消息转发给MME。MME收到SGSN的RIM消息，根据目标ID查找目标eNodeB，并将RIM消息转发给目标eNodeB。
测试结果|–
测试项目|4G到3G的RIM
---|---
测试目的|验证E-UTRAN到UTRAN的RIM，SGSN、MME能够正确处理
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB和MME上配好了到PS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|eNodeB发起4G到3G的RIM流程，Target ID携带目标RNC ID。在MME和SGSN上检查信令流程。
通过准则|MME收到eNodeB的RIM消息后，通过解析获取目标SGSN地址，并将RIM消息转发给SGSN。SGSN收到MME的RIM消息，根据目标ID查找目标RNC，并将RIM消息转发给目标RNC。
测试结果|–
测试项目|2G到4G的RIM
---|---
测试目的|验证GERAN到E-UTRAN的RIM，SGSN、MME能够正确处理
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。BSC和SGSN上配好了到EPS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|BSC发起2G到4G的RIM流程，Target ID携带目标eNodeB ID。在MME和SGSN上检查信令流程。
通过准则|SGSN收到BSC的RIM消息后，通过解析获取目标MME地址，并将RIM消息转发给MME。MME收到SGSN的RIM消息，根据目标ID查找目标eNodeB，并将RIM消息转发给目标eNodeB。
测试结果|–
测试项目|4G到2G的RIM
---|---
测试目的|验证E-UTRAN到GERAN的RIM，SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB和MME上配好了到PS的RIM的相关配置。在SGSN和MME上建立信令跟踪。
测试过程|eNodeB发起4G到2G的RIM流程，Target ID携带目标Cell ID。在MME和SGSN上检查信令流程。
通过准则|MME收到eNodeB的RIM消息后，通过解析获取目标SGSN地址，并将RIM消息转发给SGSN。SGSN收到MME的RIM消息，根据目标ID查找目标BSC，并将RIM消息转发给目标BSC。
测试结果|–
常见问题处理 :无 
## ZUF-78-03-004 3G到LTE的切换 
当用户从一种接入技术变为另一种接入技术时，MME的系统间切换过程保证用户业务的连续性。目前只支持LTE和3G网络之间的切换。
在系统间切换过程中，用户的无线连接可无缝切换到目的无线接入网。 
当系统间切换过程完成后，用户可在新的无线接入网继续使用数据业务和其他业务。 
# 缩略语 
# 缩略语 
## 3G 
The 3rd Generation Mobile Communications第三代移动通信
LTE :Long Term Evolution长期演进
MME :Mobility Management Entity移动管理实体
UE :User Equipment用户设备
# ZUF-78-05 网元选择 
概述 :功能描述 :网元选择功能用于MME选择业务处理网元，包括：SGW选择、PGW选择、SGSN选择、MME选择、AMF选择等。 
功能特性简介 :网元选择功能详细的特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
PGW选择|UE发起附着或PDN连接建立时，MME选择合适的PGW建立PDN连接。MME支持通过DNS解析和本地解析得到PGW。当有多个PGW符合必要条件时，可以根据多种策略进行优选，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用。拓扑：用于SGW和PGW合一或路由相近。优先级：用于PGW间互相备份。权重：用于PGW间负荷分担。地址优选：根据PGW地址或地址段进行优选。IMSI/MSISDN号段/签约计费特性：MME根据号段、签约计费特性、以及两者的组合方式选择PGW，用于将特定号段/计费特性的用户选择到指定的PGW上去。PGW选择策略具体参见3GPP 23.401协议4.3.8.1 PDN GW selection function (3GPP accesses)章节和3GPP 29.303协议。|ZUF-78-05-001 PGW选择
SGW选择|UE发起附着，或SGW改变的TAU，或发生SGW改变的切换，MME为用户选择合适的SGW。MME支持通过DNS解析和本地解析得到SGW，SGW的FQDN根据开关确定是用TAI还是eNodeBID来构造。SGW选择的必要条件是：SGW服务于用户当前位置区。SGW有效，即SGW运行正常。多个SGW符合必要条件时，有多种策略可以进行优选，不同的选择策略对应不同的应用场景，以下各优选策略可以组合使用。拓扑：用于SGW和PGW合一或路由相近。优先级：用于SGW间互相备份。权重：用于SGW间负荷分担。地址优选：根据SGW地址或地址段进行优选。IMSI/MSISDN号段：用于将特定号段的用户选择到指定的SGW上去。另外，当SGW是互备组网时，支持总是为用户选择服务于用户当前位置的主用SGW。SGW选择策略具体参见3GPP 23.401协议4.3.8.2 Serving GW selection function章节。|ZUF-78-05-002 SGW选择
SGSN选择|UE从E-UTRAN切换到2/3G网络时，需要MME选择SGSN，由SGSN为UE提供2/3G网络服务。SGSN选择的必要条件是：用户位置在SGSN服务区。SGSN是有效的。当多个SGSN符合必要条件时，根据负荷分担进行选择。另外，MME和SGSN为COMBO局时，可以优选COMBO的SGSN。具体选择规则参见3GPP 23.401协议4.3.8.4 SGSN selection function章节。|ZUF-78-05-003 SGSN选择
MME选择|UE在E-UTRAN内移动，目标区域不是当前UE所在MME的服务区时，需要根据目标区域选择新MME为UE提供服务。MME选择的必要条件是：用户位置在MME服务区。MME是有效的。当多个MME符合必要条件时，根据负荷分担进行选择。具体选择规则参见3GPP 23.401协议4.3.8.3 MME selection function章节。|ZUF-78-05-004 MME选择
HSS选择|UE在附着或TAU业务时，完成到HSS的登记，需要选择HSS。MME与HSS之间连接分为两种：MME与HSS直连。MME通过DRA中转连接HSS。HSS是否存在备份分为：无备用HSS。存在备用HSS。MME基于用户IMSI分析获得一个或多个HSS或DRA，优先使用主用HSS或DRA，当主用不可达时，选择备用HSS或DRA。|ZUF-78-05-005 HSS选择
MSC选择|在联合附着/TAU时，需要选择MSC，完成到MSC的登记。对于联合附着/TAU业务，MME连接多个MSC，MSC之间可以为非POOL或POOL组网：非POOL组网，MME基于TAI映射得到LAI，LAI+IMSI号码关联到MSC局向。POOL组网，MME基于TAI映射得到单个LAI，LAI关联到MSC POOL ID，在POOL再基于MSC的优先级和权重，选择到MSC局向。POOL组网，MME基于TAI映射得到多个不同PLMN的LAI，可以设置优选LAI，每个LAI关联到MSC POOL ID，在POOL再基于MSC的优先级和权重，选择到MSC局向。在优选LAI对应的MSC POOL不可用时，可以选择其他LAI。联合附着/TAU业务选择MSC的具体规则可参见3GPP 23.272协议4.3.2 MME章节。在SRVCC切换时，需要选择MSC，完成到将语音呼叫切换到MSC。对于SRVCC业务，MME根据切换目标位置构造FQDN进行DNS或本地解析，根据解析结果中优先级和权重选择，获得MSC的IP地址。SRVCC业务选择MSC的具体规则可参见3GPP 29.303协议5.7 Procedures for Discovering and Selecting an MSC Server章节。|ZUF-78-05-006 MSC选择
PGW重选|当收到PGW的会话建立失败，原因是运营商期望重选的原因时，选择其他PGW完成当前PDN连接建立。当前支持的期望原因包括：System failure (72)No resources available (73)Remote peer not responding (100)APN Congestion (113)|ZUF-78-05-007 PGW重选
AMF选择|UE从4G网络移动到5G网络，MME根据目标位置选择AMF，MME根据目标TA构造FQDN，通过DNS查询或本地解析获取到AMF列表，完全根据DNS查询或本地解析返回结果进行选择。当有多个AMF符合必要条件时，MME可以根据多种策略进行优选，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用。优先级：用于AMF间互相备份。权重：用于AMF间负荷分担。AMF选择策略具体参见3GPP 23.502协议4.11.1.2.2 EPS to 5GS handover using N26 interface和3GPP 29.303协议5.4A Procedures for Discovering and Selecting an AMF章节。|ZUF-78-05-008 AMF选择
## ZUF-78-05-001 PGW选择 
特性描述 :特性描述 :术语 :无 
描述 :定义 :GW选择功能包括SGW选择功能、PGW选择功能以及PGW不可达重选功能。 
SGW选择功能是为用户选择一个可用的SGW。SGW和eNodeB相连接，主要负责用户面处理，负责数据包的路由和转发等功能，eNodeB管理用户的位置，因此SGW管辖区域与用户位置相关。MME尽可能选择和eNodeB路径较短的SGW，以减少数据传输时延。 
PGW选择功能是为用户3GPP接入选择建立PDN连接的PGW。PGW是终结接连外部数据网络（如互联网、IMS等）的网关，是EPS的锚点，即是3GPP与non-3GPP网络间的用户面数据链路的锚点，负责管理3GPP和non-3GPP间的数据路由，用户使用不同的接入点名称连接到不同的PGW，访问不同类型的外部网络。MME尽可能选择和用户位置路径较短的PGW，以减少数据传输时延。 
PGW不可达重选功能。选择PGW/SGW后，如果接收到Create Session Response中原因值为“#100 Remote peer
not responding”，则从查询出来的地址中重新选一个含有效PGW地址的PGW/SGW对，向这个PGW再次发送，如果第二次查询仍不可达则不再尝试。选择PGW/SGW后，如果等待Create Session Response超时，则从查询出来的地址中重新选一个含有效PGW地址的PGW/SGW对，向这个PGW再次发送，如果第二次查询失败则不再尝试。 
背景知识 :SGW和PGW在现网有如下三种部署方式，MME根据SGW和PGW的实际部署确定具体的SGW选择和PGW选择策略。 
SGW的部署MME尽可能选择和eNodeB路径较短的SGW，以减少数据传输时延。SGW在中心城市和下级地市都可以部署。如果现网SGW资源比较多，各地区内有多套SGW，则多套SGW
POOL组网，负荷分担，MME根据用户位置选择就近的SGW POOL，再根据SGW在POOL内的权重选择SGW；如果现网SGW资源比较少，各地区内仅一两套SGW，则本地区内的SGW可以和其他地区的SGW
POOL组网，互相备份，MME根据用户位置选择就近的SGW POOL，再根据SGW在POOL内的优先级选择SGW。 
PGW的部署PGW是用户面数据链路的锚点，当用户发生移动时，PGW是不变的，如果PGW部署在各地市，用户跨地市移动时会明显拉远SGW和PGW间的用户面数据传送时间，增大时延，因此PGW一般都是集中在中心城市部署，不会下沉到地市部署。如果集中部署在中心城市的PGW有多套，则这多套PGW
POOL组网，负荷分担，MME根据用户使用的接入点名称选择就近的PGW POOL，再根据PGW在POOL内的权重选择PGW。 
SGW和PGW合一或就近部署中心城市部署的SGW和PGW，大都采用SGW和PGW合一或邻近，这样部署可以避免或大大减少SGW和PGW间的跨框流量。MME选择到SGW
POOL和PGW POOL后，根据POOL内SGW主机名和PGW主机名的匹配度高低，选择出匹配度最高最邻近的SGW/PGW。 说明：SGW和PGW合一是指，SGW和PGW在同一个机房里，SGW和PGW邻近指的是SGW和PGW不在同一个机房里，但是在同机房或邻近机房。 
应用场景 :按照SGW和PGW是否合一或邻近的原则将应用场景划分为如下三部分。 
###### SGW选择 
SGW间有两种组网方式：负荷分担组网和互备组网。 
SGW有两种部署方式：集中部署和下沉部署，即集中部署在中心城市和下沉部署在下级地市。 
因此在SGW和PGW不合一也不邻近的情况下，根据SGW的组网和部署方式，MME对SGW的选择分为如四种下场景。 
SGW负荷分担组网+SGW集中部署场景描述SGW部署在大区内的中心城市，大区内SGW间负荷分担，大区间SGW没有互相备份，SGW和PGW不合一也不邻近。举例某地分2个区，每个区内SGW集中部署，各区内的SGW间负荷分担；因为每个大区内SGW比较多，所以大区间不需要互相备份。组网图如下图所示： 说明：大区1和大区2间没有互备，DNS解析结果如下：用户在大区1下所在TA1 DNS解析出：SGW1、SGW2、SGW3。用户在大区2下所在TA2 DNS解析出：SGW4、SGW5、SGW6。SGW选择用户在大区1下附着，MME根据SGW的权重从大区1下的SGW1、SGW2、SGW3选出一个SGW。当用户移动到大区2，MME根据SGW的权重从大区2下的SGW4、SGW5、SGW6选出一个SGW。 
SGW负荷分担组网+SGW下沉部署场景描述PGW部署在中心城市（即集中部署），SGW部署在下级地市，地市内SGW间负荷分担，地市间SGW没有互相备份，SGW和PGW不合一也不邻近。举例某地有1个中心城市，2个地市，PGW部署在中心城市，SGW部署在2个地市；因为每个地市内SGW比较多，所以地市间不需要互相备份。组网图如下图所示： 说明：大区1和大区2间没有互备，DNS解析结果如下：用户在大区1下所在TA1 DNS解析出：SGW1、SGW2、SGW3。用户在大区2下所在TA2 DNS解析出：SGW4、SGW5、SGW6。SGW选择用户在地市1下附着，MME根据SGW的权重从地市1下的SGW1、SGW2中选出一个SGW。当用户移动到地市2，MME根据SGW的权重从地市2下的SGW3、SGW4中选出一个SGW。 
SGW互备组网+SGW集中部署场景描述SGW部署在大区内的中心城市，大区内：SGW间负荷分担，大区间SGW互相备份，SGW和PGW不合一也不邻近。举例某地分2个区，每个区内SGW集中部署，各区内的SGW间负荷分担；因为每个大区内SGW比较少，所以大区间需要互相备份。组网图如下图所示： 说明：大区1和大区2间互备，DNS解析结果如下：用户在大区1下所在TA1 DNS解析出：SGW1、SGW2，SGW3、SGW4，其中SGW1、SGW2的优先级为10，SGW3、SGW4的优先级为20。用户在大区2下所在TA2 DNS解析出：SGW1、SGW2，SGW3、SGW4，其中SGW1、SGW2的优先级为20，SGW3、SGW4的优先级为10。SGW选择用户在大区1下附着，MME根据SGW的优先级选出大区1下的SGW1、SGW2，再根据SGW的权重从SGW1、SGW2中选出一个SGW。当用户移动到大区2，MME预判SGW改变进行DNS查询，根据查询得到的SGW的优先级判定SGW改变，进行SGW重选，MME根据SGW的优先级选出大区2下的SGW3、SGW4，再根据SGW的权重从SGW3、SGW4中选出一个SGW。 
SGW互备组网+SGW下沉部署场景描述PGW部署在中心城市（即集中部署），SGW部署在下级地市，地市内SGW间负荷分担，地市间SGW互相备份，SGW和PGW不合一也不邻近。举例某地有1个中心城市，2个地市，PGW部署在中心城市，SGW部署在2个地市；因为每个地市内SGW比较少，所以地市间需要互相备份。组网图如下图所示： 说明：地市1和地市2间互备，DNS解析结果如下：用户在地市1下所在TA1 DNS解析出：SGW1、SGW2、SGW3、SGW4，其中SGW1、SGW2的优先级为10，SGW3、SGW4的优先级为20。用户在地市2下所在TA2 DNS解析出：SGW1、SGW2、SGW3、SGW4，其中SGW1、SGW2的优先级为20，SGW3、SGW4的优先级为10。SGW选择用户在地市1下附着，MME根据SGW的优先级选出地市1下的SGW1、SGW2，再根据SGW的权重选出SGW1、SGW2中的一个SGW。当用户移动到地市2，MME预判SGW改变进行DNS查询，根据查询得到的SGW的优先级判定SGW改变，进行SGW重选，MME根据SGW的优先级选出地市2下的SGW3、SGW4，再根据SGW的权重选出SGW3、SGW4中的一个SGW。 
###### PGW选择 
PGW间有两种组网方式：负荷分担组网和互备组网。 
PGW只有一种部署方式：集中部署，即集中部署在中心城市，PGW是用户面数据链路的锚点，当用户发生移动时，PGW是不变的，因此PGW一般不会下沉部署。 
因此在SGW和PGW不合一也不邻近的情况下，根据PGW的组网方式，MME对PGW的选择分为如下两种场景。 
PGW负荷分担组网场景描述PGW部署在大区内的中心城市，大区内PGW间负荷分担，大区间PGW没有互相备份，SGW和PGW不合一也不邻近。举例某地分2个区，每个区内PGW集中部署，各区内的PGW间负荷分担；因为每个大区内PGW比较多，所以大区间不需要互相备份。组网图如下图所示： 说明：大区1和大区2间互备，DNS解析结果如下：用户在大区1下APN DNS解析出：PGW1、PGW2、PGW3。用户在大区2下APN DNS解析出：PGW4、PGW5、PGW6。PGW选择用户在大区1下附着，MME根据PGW的权重选出大区1下PGW POOL：PGW1、PGW2、PGW3，再根据POOL内PGW权重选择一个PGW。用户移动到大区2，PGW是锚定点，PGW不改变。用户在大区2下附着，MME根据PGW的权重选出大区2下PGW POOL：PGW4、PGW5、PGW6，再根据POOL内PGW权重选择一个PGW。用户移动到大区1，PGW是锚定点，PGW不改变。 
PGW互备组网场景描述PGW部署在大区内的中心城市，大区内PGW间负荷分担，大区间PGW互相备份，SGW和PGW不合一也不邻近。举例某地分2个区，每个区内PGW集中部署，各区内的PGW间负荷分担；因为每个大区内PGW比较少，所以大区间需要互相备份。组网图如下图所示： 说明：大区1和大区2间互备，DNS解析结果如下：用户在大区1下APN DNS解析出：PGW1、PGW2、PGW3、PGW4，其中PGW1、PGW2优先级为10，PGW3、PGW4优先级为20。用户在大区2下APN DNS解析出：PGW1、PGW2、PGW3、PGW4，其中PGW1、PGW2优先级为20，PGW3、PGW4优先级为10。PGW选择用户在大区1下附着，MME根据PGW的优先级选出大区1下的PGW1、PGW2，再根据PGW的权重选出PGW1、PGW2中的一个PGW。并用户移动到大区2，PGW是锚定点，用户仍使用附着时选择的PGW。 
###### SGW和PGW合一或就近选择 
SGW和PGW合一或就近选择时有两种组网方式：负荷分担组网和互备组网。 
SGW和PGW合一或就近选择时有两种部署方式： 
SGW和PGW集中部署，即集中部署在中心城市。 
PGW集中部署，部分SGW集中部署，部分SGW下沉部署。 
因此在SGW和PGW合一或就近选择的情况下，根据PGW和SGW的组网方式，MME对SGW/PGW的选择分为如下四种场景。 
SGW/PGW负荷分担组网+集中部署场景描述SGW/PGW部署在大区内的中心城市，大区内SGW/PGW间负荷分担，大区间SGW/PGW没有互相备份，SGW和PGW合一或邻近。举例某地分2个区，每个区内SGW/PGW集中部署，各区内的SGW/PGW间负荷分担；因为每个大区内SGW/PGW比较多，所以大区间不需要互相备份。组网图如下图所示： 说明：大区1和大区2间没有互备，DNS解析结果如下：用户在大区1下所在TA1 DNS解析出：SGW1、SGW2、SGW3，APN DNS解析出：PGW1、PGW2、PGW3。用户在大区2下所在TA2 DNS解析出：SGW4、SGW5、SGW6，APN DNS解析出：PGW4、PGW5、PGW6。SGW/PGW选择用户在大区1下附着，MME根据SGW和PGW合一或邻近关系，选出大区1下合一或最近的一对或多对SGW/PGW，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW。当用户移动到大区2，PGW是锚定点，不发生改变。MME在大区2下选择SGW POOL：SGW4、SGW5、SGW6，再根据这些的负荷分担关系选择一个SGW。 
SGW/PGW负荷分担组网+非集中部署场景描述PGW集中部署在中心城市，部分SGW集中部署在中心城市，部分SGW下沉部署在下级地市，中心城市内的PGW间负荷分担、SGW间也负荷分担，地市内的SGW间负荷分担，中心城市和地市间以及地市间SGW没有互相备份，中心城市内的SGW和PGW合一或邻近。举例某地有1个中心城市，2个地市，PGW部署在中心城市，SGW部署在中心城市和2个地市；因为每个地市内SGW比较多，所以地市间不需要互相备份。组网图如下图所示： 说明：中心城市、地市1和地市2间没有互备，DNS解析结果如下：用户在中心城市下所在TA0 DNS解析出：SGW1、SGW2，APN DNS解析出：PGW1、PGW2。用户在地市1下所在TA1 DNS解析出：SGW3、SGW4，APN DNS解析出：PGW1、PGW2。用户在地市2下所在TA2 DNS解析出：SGW5、SGW6，APN DNS解析出：PGW1、PGW2。SGW/PGW选择根据用户的不同位置信息对SGW/PGW的选择参见下表。用户位置SGW/PGW选择用户在中心城市下附着，并移动到地市1或地市2用户在中心城市下附着，MME根据SGW和PGW合一或邻近关系，选出中心城市下一对或多对SGW/PGW，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW。当用户移动到地市1或地市2，PGW是锚定点不改变，MME根据SGW的负荷分担关系选择各地市自己的SGW。用户在地市1下附着，并移动到地市2用户在地市1下附着，MME根据PGW的权重选出PGW1、PGW2中的一个，根据SGW的负荷分担关系选出SGW3、SGW4中的一个。当用户移动到地市2，PGW是锚定点不改变，MME根据SGW的权重选出SGW POOL：SGW5、SGW6，再根据这些的负荷分担关系选择一个SGW。用户在地市1下附着，并移动到中心城市用户在地市1下附着，MME根据PGW的权重选出PGW1、PGW2中的一个，根据SGW的负荷分担关系选出SGW3、SGW4中的一个。当用户移动到中心城市，PGW是锚定点不改变，MME选出SGW1、SGW2中和PGW合一或最邻近的SGW。 
SGW/PGW互备组网+集中部署场景描述SGW/PGW集中部署，SGW和PGW合一或邻近，大区内：SGW间负荷分担，PGW间负荷分担，大区间也互相备份。举例某地分2个区，每个区内SGW/PGW集中部署，各区内的SGW/PGW间负荷分担；因为每个大区内SGW/PGW比较少，所以大区间需要互相备份。组网图如下图所示： 说明：大区1和大区2间互备，DNS解析结果如下：用户在大区1下所在TA1 DNS解析出：SGW1、SGW2（这2个SGW优先级为10），SGW3、SGW4（这2个SGW优先级为20），APN
DNS解析出：PGW1、PGW2（这2个PGW优先级为10），PGW3、PGW4（这2个PGW优先级为20）。用户在大区2下所在TA2 DNS解析出：SGW1、SGW2（这2个SGW优先级为20），SGW3、SGW4（这2个SGW优先级为10），APN
DNS解析出：PGW1、PGW2（这2个PGW优先级为20），PGW3、PGW4（这2个SGW优先级为10）。SGW/PGW选择用户在大区1下附着，MME根据SGW和PGW合一或邻近关系，选出中心城市下SGW1、SGW2和PGW1、PGW2中合一或最近的一对或多对SGW/PGW，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW。当用户移动到大区2，PGW是锚定点不改变，MME预判SGW改变进行DNS查询，根据查询得到的SGW的优先级判定SGW改变，进行SGW重选，MME根据SGW的优先级选出大区2下的SGW3、SGW4，再根据SGW的权重从SGW3、SGW4中选出一个SGW。 
SGW/PGW互备组网+非集中部署场景描述PGW集中部署在中心城市，部分SGW集中部署在中心城市，部分SGW下沉部署在下级地市，中心城市里PGW间负荷分担、SGW间也负荷分担，地市内SGW间负荷分担，中心城市和地市间以及地市间SGW也互相备份，中心城市里SGW和PGW合一或邻近。举例某地有1个中心城市，2个地市，PGW部署在中心城市，SGW部署在中心城市和2个地市；因为每个地市内SGW比较少，所以地市间需要互相备份。组网图如下图所示： 说明：中心城市、地市1和地市2间互备，DNS解析结果如下：用户在中心城市下所在TA0 DNS解析出：SGW1、SGW2（这2个SGW优先级为10），SGW3、SGW4（这2个SGW优先级为20），APN
DNS解析出：PGW1、PGW2。用户在地市1下所在TA1 DNS解析出：SGW3（这个SGW优先级为10），SGW1、SGW2、SGW4（这3个SGW优先级为20），APN
DNS解析出：PGW1、PGW2。用户在地市2下所在TA2 DNS解析出：SGW4（这个SGW优先级为10），SGW1、SGW2、SGW3（这4个SGW优先级为20）。SGW/PGW选择根据用户的不同位置信息对SGW/PGW的选择参见下表。用户位置SGW/PGW选择用户在中心城市下附着，并移动到地市1或地市2用户在中心城市下附着，MME根据SGW和PGW合一或邻近关系，选出中心城市下SGW1、SGW2和PGW1、PGW2中合一或最近的一对或多对SGW/PGW，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW。用户移动到地市1或地市2，PGW是锚定点不改变，MME预判SGW改变进行DNS查询，根据DNS查询得到SGW的优先级，MME根据该优先级选出地市1下的SGW3或地市2下的SGW4。用户在地市1下附着，并移动到地市2用户在地市1下附着，MME根据PGW的权重选出PGW1、PGW2中的一个，根据SGW的DNS解析选出SGW3。当用户移动到地市2，PGW是锚定点不改变，MME预判SGW改变进行DNS查询，根据DNS查询得到SGW的优先级，MME根据该优先级选出地市2下的SGW4。用户在地市1下附着，并移动到中心城市用户在地市1下附着，MME根据PGW的负荷分担关系选出PGW1、PGW2中的一个，根据SGW的DNS解析选出SGW3。当用户移动到中心城市，PGW是锚定点不改变，MME预判SGW改变进行DNS查询，根据查询得到SGW的优先级，MME根据该优先级选出SGW1、SGW2中和PGW合一或最邻近的SGW。 
客户收益 :受益方|受益描述
---|---
运营商|通过合理利用GW选择策略，运营商能获得如下收益：节约投资成本：通过拓扑选择，选择路径最短的SGW和PGW，从而减少了跨框、跨地域的业务流量。提高业务可靠性：优先级和权重、有效性选择等策略提高了业务可靠性。提高策略灵活性：基于IMSI/MSISDN号段选择SGW和PGW，基于签约计费特性选择PGW，提高了策略灵活性。
移动用户|减少数据传输时延：通过拓扑选择，选择路径最短的SGW和PGW，减少数据传输时延，提高终端用户体验，享受优质的网络服务。
实现原理 :涉及的网元 :网元名称|网元作用
---|---
DNS Server|记录APN-FQDN和PGW列表的对应关系，根据APN-FQDN返回查询到的PGW列表。记录TA-FQDN或eNB-FQDN和SGW列表的对应关系，根据TA-FQDN或eNB-FQDN返回查询到的SGW列表。
MME|使用S-NAPTR查询方式查询DNS服务器，获取到SGW/PGW列表。根据系统配置的SGW/PGW选择策略对SGW/PGW进行选择，确定最终的SGW/PGW节点及控制面交互的IP地址。
SGW|在检测到PGW故障时，应发送PGW重启通知消息通知MME。SGW支持通知MME发生SGW网元级动态负荷。
PGW|PGW支持通知MME发生PGW网元级动态负荷以及APN级负荷信息。
本网元实现 :目前MME中SGW和PGW的选择有多种策略，参见下表。不同的选择策略对应不同的SGW和PGW部署场景，各选择策略可以组合使用。 
Selection Policy|Policy Description|Application Scenario
---|---|---
拓扑|SGW和PGW之间的拓扑，是通过主机名表达的，当需要根据拓扑选择SGW和PGW时，按主机名字符从右到左顺序匹配SGW和PGW的主机名，匹配度最高的说明拓扑最相近。|SGW和PGW共框即合一，或者SGW和PGW路由相近。
有效性|SGW链路有效性SGW作为有效节点，MME与SGW间进行消息交互，SGW成功返回响应。PGW链路有效性MME根据PGW与SGW间的链路有效性选择SGW/PGW。|SGW链路故障冗余保护PGW链路故障冗余保护，当某个GW故障，可以选择其他正常的GW，实现容灾备份。
优先级|SGW/PGW优先级数值越小，优先级越高，MME优选高优先级的SGW/PGW。|SGW间互相备份。PGW间互相备份。
权重|MME根据SGW/PGW的权重因子，随机选择一个SGW/PGW，SGW/PGW权重因子的大小，决定其被选择的概率的大小。|SGW间负荷分担，PGW间负荷分担，网络中SGW/PGW的能力不一致，高能力的SGW/PGW配置的权重也高，其被选择到的机会多，达到SGW/PGW上的负荷均衡。
动态负荷|MME根据之前与SGW交互时保存的SGW的负荷，以及DNS返回的SGW的静态权重，共同决定SGW的有效负荷（（100-动态负荷）%×静态权重）来进行SGW选择。 MME根据之前与PGW交互时保存的PGW网元级负荷以及APN级负荷，以及DNS返回的当前APN解析的PGW的静态权重，共同决定当前APN的PGW的有效负荷（（100-PGW网元动态负荷）%×静态权重×APN级负荷）来进行PGW选择。|SGW和PGW动态负荷均衡。
IMSI/MSISDN号段|MME根据IMSI/MSISDN号码或号段选择SGW。|对新入网的SGW进行拨测，或定位SGW故障，将测试卡指向该SGW。将特定号段的用户选择到指定的SGW上去。
IMSI/MSISDN号段/签约计费特性|MME根据IMSI/MSISDN号段、签约计费特性、以及两者的组合方式选择PGW。|将特定号段/计费特性的用户选择到指定的PGW上去。
地址解析优先级|MME控制本地Host解析、DNS Server解析、DNS cache解析这三种查询方式的优先级。|DNS系统瘫痪且短时间无法恢复，切换到本地Host解析，快速恢复业务。
业务流程 :MME在如下流程中执行SGW选择： 
附着。 
SGW改变的TAU。 
SGW改变的Handover。 
MME在如下流程中执行PGW选择： 
附着。 
UE请求PDN连接。 
附着流程中的GW选择
附着流程中MME需要为UE选择SGW和PGW，流程示意图如[图1]所示。
图1  附着流程GW选择

如上图步骤3，MME准备给SGW发送Create
Session Request消息时，先根据SGW/PGW选择策略选择得到SGW和PGW，MME向SGW发送Create Session
Request消息并携带已选择的PGW地址。 
UE请求PDN连接流程中PGW选择
PDN连接建立的流程中，MME为UE选择接入的PGW，建立UE到PGW的PDN连接。流程示意图如[图2]所示。
图2  UE请求PDN连接流程中PGW选择
MME准备给SGW发送Create Session Request消息时，先根据PGW选择策略选择得到PGW，MME向SGW发送Create
Session Request消息并携带已选择的PGW地址。 
SGW改变的TAU流程中SGW选择
SGW改变的TAU流程中，PGW不会改变，MME需要为UE重新选择SGW。流程示意图如[图3]所示。
图3  SGW改变的TAU流程中SGW选择

MME准备给SGW发送Create Session Request消息时，先根据SGW选择策略选择得到SGW，MME向SGW发送Create
Session Request消息并携带PGW地址。 
SGW改变基于X2接口的Handover流程中SGW选择
SGW改变基于X2接口的切换流程中，PGW不会改变，MME需要为UE重新选择SGW。流程示意图如[图4]所示。
图4  GW Selection in SGW-Changed Handover Based on X2 Interface

如上图步骤2，MME准备给SGW发送Create Session Request消息时，先根据SGW选择策略选择得到SGW，MME向SGW发送Create
Session Request消息并携带PGW地址。 
SGW改变基于S1接口的Handover流程中SGW选择
SGW改变基于S1接口的切换流程中，PGW不会改变，MME需要为UE重新选择SGW。流程示意图如[图5]所示。
图5  GW Selection in SGW-Changed Handover Based on S1 Interface

如上图步骤3，目标MME准备给SGW发送创建会话请求消息时，先根据GW选择策略选择得到SGW，MME向SGW发送创建会话请求消息并携带PGW地址。 
系统影响 :SGW选择和PGW选择是基本功能，对系统性能无影响。 
应用限制 :在部署SGW/PGW 拓扑组网时，SGW/PGW的Hostname都存在，同时Host Name的命名规则需要遵循3GPP TS
29.303协议的定义。 
Host Name的命名规则：<"topon" | "topoff">.<single-label-interface-name>.<canonical-node-name> 
特性交互 :业务|交互
---|---
IPv6/IPv4双栈|如果GW的地址既有IPv4地址，也有IPv6地址，而本局也支持IPv6地址，则根据软参“与邻接网元交互时业务IP双栈优选的IP类型”和“与非邻接网元交互时业务IP双栈优选的IP类型”分别选择SGW和PGW的地址类型。
遵循标准 :协议|章节号及章节名称
---|---
3GPP TS23.401: "GPRS enhancements for E-UTRAN access "|5.3.2节:Attach procedure5.3.3节: Tracking Area Update procedures5.5节: Handover5.10.2节: UE requested PDN connectivity
3GPP TS29.303:"Domain Name System Procedures Stage 3"|全部
特性能力 :特性|能力
---|---
本地EPC地址解析配置|最多支持4096条FQDN解析数据，一个FQDN最多解析到8个SGW节点数据。
本地EPC APNHOST配置|最多支持4096条APNFQDN解析数据，一个APN FQDN最多解析到8个PGW节点数据。
本地EPC APN优选子网段配置|最多支持4096条EPCAPN优选子网段数据，一个APN FQDN最多支持10个优先级不同的IP子网。
本地EPC地址解析优选子网段配置|最多支持1024条EPC地址解析优选子网段数据，一个FQDN最多支持10个优先级不同的IP子网。
基于号段选择SGW配置|最多支持基于4096个用户号段选择SGW。
EPC扩展APN配置|基于用户号段、签约计费特性选择PGW，支持IMEI扩展、TA信息扩展和无感分流标识扩展，最多支持基于2048个用户号段选择PGW。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.22.20|EPC扩展APN配置新增IMEI扩展、TA信息扩展和无感分流标识扩展。
01|V7.19.13|首次发布。
License要求 :如果本特性不受license控制，用下面的固定句式： 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :根据SGW和PGW距离远近，合理部署SGW和PGW，对合一或邻近的SGW和PGW，要将SGW和PGW的主机名统一规范命名。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令EPC HOST配置ADD EPCHOSTEPC APN配置ADD EPC APNEPC PGW HOST配置ADD EPC PGWEPC地址解析优选子网段配置ADD HOST SUBNET PRIEPC APN优选子网段配置ADD EPC APN SUBNET PRIEPC扩展APN配置ADD EPC EXAPN基于号段选择S-GW配置ADD SGW SELECTION 
软件参数表2  新增软件参数软件参数ID软件参数名称65593MME地址解析优先级控制786516MME通过权重和优先级选择S-GW786519MME通过权重和优先级选择P-GW786548与邻接网元交互时业务IP双栈优选的IP类型786780拓扑选择方式786801支持SGW互备时MME识别SGW改变786549收到原因值为“Remote peer not responding”的次数786550PGW恢复有效的时长786601MME支持PGW Restart Notification786605MME支持Node Feature786842支持PGW重选 
特性配置 :特性配置 :#### SGWPGW优先级选择特性配置 
配置说明 :当SGW和PGW既不合一也不邻近时，需要配置SGW/PGW优先级选择。 
通过配置实现根据优先级进行SGW的就近选择，相同优先级下的SGW可以进行负荷分担选择，以及PGW的负荷分担选择。 
配置前提 :DNS服务器与MME的对接数据配置完整。 
TAI和eNodeB信息已规划好，APN信息已规划好。 
SGW/PGW的组网规划已确定。 
配置步骤 :（可选）配置DNS服务器。 当使用ZTE的DNS服务器时，需要进行本步骤的操作。 
配置使用TAI-FQDN解析SGW。 
关闭拓扑选择。 
配置使用优先级权重选择SGW/PGW 
（可选）当SGW互备组网时，需要设置支持SGW互备时MME识别SGW改变。 
配置TAI的归属不同GROUP ID。 
 说明： 
注：商用环境一般使用DNS服务器来解析SGW和PGW的主机名，本地不需要再配置数据。 
###### 配置实例-负荷分担组网+SGW下沉部署 
场景说明
某地分2个区，PGW集中部署，PGW有两个，各区内的SGW下沉部署。 
不使用拓扑选择，SGW之间是负荷分担选择，PGW之间也是负荷分担。 
因为每个大区内SGW比较多，所以大区间不需要互相备份。解析如下： 
用户在大区1下所在TA1 DNS解析出：SGW1、SGW2、SGW3。 
用户在大区2下所在TA2 DNS解析出：SGW4、SGW5、SGW6。 
用户在大区1下附着，MME根据TA1（460-00-0001）解析出SGW1、SGW2、SGW3，再根据权重选择其中的一个SGW，根据APN解析出PGW1和PGW2，根据权重选择出一个PGW。 
然后用户移动到大区2，MME根据TA2（460-00-0002）解析出大区2下SGW4、SGW5、SGW6，再根据权重选择其中的一个SGW。PGW为锚点，PGW不变。 
数据规划
本地EPC HOST和EPC APN不配置，使用DNS解析。 
规划的APN为cmnet.com，HSS签约动态PGW类型。 
使用TAI-FQDN解析SGW地址。 
TA1与TA2归属不同GROUP  ID。 
SGW与PGW的其他信息参见下表。 
XGW编号|XGW主机名|优先级|权重|地址
---|---|---|---|---
SGW1|topon.s5s8.sgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.1
SGW2|topon.s5s8.sgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.2
SGW3|topon.s5s8.sgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.3
SGW4|topon.s5s8.sgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.4
SGW5|topon.s5s8.sgw5.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.5
SGW6|topon.s5s8.sgw6.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.6
PGW1|topon.s5s8.pgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.1
PGW2|topon.s5s8.pgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.2
配置步骤
根据规划，进行如下配置： 
配置DNS上的数据步骤操作配置TAI-FQDN的第一步解析，即SGW的NAPTR查询配置ZONE。zone "tac.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epctai.sgw";};配置RR，文件名为db.epctai.sgw。$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
;                  IN   NAPTR order  pref.  flag 
    service                     regexp 	replacement 
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb02.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb02.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw5.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb02.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw6.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
保存文件。配置APN-FQDN的第一步解析，即PGW的NAPTR查询配置ZONE。zone "apn.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epcapn.pgw"; };配置RR，文件名为db.epcapn.pgw。$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
;                  IN   NAPTR order  pref.  
flag     service            regexp 	replacement 
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.pgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.pgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
保存文件。配置主机名的解析，即A类查询配置ZONEzone "node.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epchost.saegw"; };配置RR，文件名为db.epchost.saegw$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
topon.s5s8.sgw1.nj.js     	IN	A	10.1.1.1
topon.s5s8.sgw2.nj.js    	IN	A	10.1.1.2
topon.s5s8.sgw3.nj.js    	IN	A	10.1.1.3
topon.s5s8.sgw4.nj.js     	IN	A	10.1.1.4
topon.s5s8.sgw5.nj.js    	IN	A	10.1.1.5
topon.s5s8.sgw6.nj.js    	IN	A	10.1.1.6
topon.s5s8.pgw1.nj.js    	IN	A	20.1.1.1
topon.s5s8.pgw2.nj.js    	IN	A	20.1.1.2
保存文件。DNS服务器数据同步执行命令rndc reload。如果没有此命令，需停止DNS服务进程，然后再启动。 
配置MME上的数据步骤操作配置SGW的解析方式为TAI-FQDNSET PACKET DOMAIN PARAMETER:FQDNRESOLVESGW="TAI-FQDN";配置不使用拓扑选择SET PACKET DOMAIN PARAMETER:TOPOLOGY="NO";配置MME通过权重和优先级选择SGW/PGW设置MME通过权重和优先级选择SGW。SET SOFTWARE PARAMETER:PARAID=786516,PARAVALUE=1;设置MME通过权重和优先级选择PGWSET SOFTWARE PARAMETER:PARAID=786519,PARAVALUE=1;配置TAI归属不同的GROUP IDSET TA:TAID=1,GRPID=1;SET TA:TAID=2,GRPID=2;数据同步SYNA 
###### 配置实例-SGW互备组网+SGW下沉部署 
场景说明
某地分2个区，PGW集中部署，各区内的SGW下沉部署。 
因为每个大区内SGW比较少，所以大区间需要互相备份，不使用拓扑选择。解析如下： 
用户在大区1下所在TA1（460-00-0001）DNS解析出：SGW1、SGW2（这2个SGW优先级为10），SGW3、SGW4（这2个SGW优先级为20）。 
用户在大区2下所在TA2（460-00-0002）DNS解析出：SGW1、SGW2（这2个SGW优先级为20），SGW3、SGW4（这2个SGW优先级为10）。 
用户在大区1下附着，MME根据SGW的优先级选出大区1下的SGW1、SGW2，再根据SGW的权重选出SGW1、SGW2中的一个SGW。 
然后用户移动到大区2，MME预判SGW改变进行DNS查询，根据查询得到的SGW的优先级判定SGW改变，进行SGW重选，MME根据SGW的优先级选出大区2下的SGW3、SGW4，再根据SGW的权重选出SGW3、SGW4中的一个SGW。 
数据规划
本地EPC HOST和EPC APN不配置，使用DNS解析。 
规划的APN为cmnet.com，HSS签约动态PGW类型。 
使用TAI-FQDN解析SGW地址。 
TA1与TA2归属不同GROUP  ID。 
SGW与PGW的其他信息参见下表。 
TAI|XGW编号|XGW主机名|优先级|权重|地址
---|---|---|---|---|---
460-00-0001|SGW1|topon.s5s8.sgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.1
SGW2|460-00-0001|topon.s5s8.sgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.2
SGW3|460-00-0001|topon.s5s8.sgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|20|100|10.1.1.3
SGW4|460-00-0001|topon.s5s8.sgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|20|100|10.1.1.4
460-00-0002|SGW1|topon.s5s8.sgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|20|100|10.1.1.1
SGW2|460-00-0002|topon.s5s8.sgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|20|100|10.1.1.2
SGW3|460-00-0002|topon.s5s8.sgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.3
SGW4|460-00-0002|topon.s5s8.sgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.4
-|PGW1|topon.s5s8.pgw.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.1
配置步骤
根据规划，进行如下配置： 
配置DNS上的数据步骤操作配置TAI-FQDN的第一步解析，即SGW的NAPTR查询配置ZONE。zone "tac.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epctai.sgw"; };配置RR，文件名为db.epctai.sgw。$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
	
;                  IN   NAPTR order  pref.  flag
     service                  regexp 	replacement 
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  20    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  20    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.

tac-lb02.tac-hb00  IN   NAPTR  20    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb02.tac-hb00  IN   NAPTR  20    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb02.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb02.tac-hb00  IN   NAPTR  10    100    "a"
   "x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
保存文件。配置APN-FQDN的第一步解析，即PGW的NAPTR查询配置ZONE。zone "apn.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epcapn.pgw"; };配置RR，文件名为db.epcapn.pgw。$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
;  IN   NAPTR order  pref.  flag     service    
regexp 	replacement 
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.pgw.nj.js.node.epc.mnc000.mcc460.
3gppnetwork.org.
保存文件。配置主机名的解析，即A类查询配置ZONEzone "node.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epchost.saegw"; };配置RR，文件名为db.epchost.saegw$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
	
topon.s5s8.sgw1.nj.js     	IN	A	10.1.1.1
topon.s5s8.sgw2.nj.js    	IN	A	10.1.1.2
topon.s5s8.sgw3.nj.js    	IN	A	10.1.1.3
topon.s5s8.sgw4.nj.js     	IN	A	10.1.1.4
topon.s5s8.pgw.nj.js     	IN	A	20.1.1.1
保存文件。DNS服务器数据同步执行命令rndc reload。如果没有此命令，需停止DNS服务进程，然后再启动。 
配置MME上的数据步骤操作配置SGW的解析方式为TAI-FQDNSET PACKET DOMAIN PARAMETER:FQDNRESOLVESGW="TAI-FQDN";配置不使用拓扑选择SET PACKET DOMAIN PARAMETER:TOPOLOGY="NO";配置MME通过权重和优先级选择SGW/PGW设置MME通过权重和优先级选择SGW。SET SOFTWARE PARAMETER:PARAID=786516,PARAVALUE=1;设置MME通过权重和优先级选择PGWSET SOFTWARE PARAMETER:PARAID=786519,PARAVALUE=1;设置MME支持SGW互备时MME识别SGW改变SET SOFTWARE PARAMETER:PARAID=786801,PARAVALUE=1;配置TAI归属不同的GROUP IDSET TA:TAID=1,GRPID=1;SET TA:TAID=2,GRPID=2;数据同步SYNA 
 说明： 
其他场景参考[配置实例-负荷分担组网+SGW下沉部署]和[配置实例-SGW互备组网+SGW下沉部署]的配置，区别主要在于DNS服务器数据配置。
#### SGW/PGW拓扑选择特性配置 
配置说明 :当SGW和PGW合一或邻近时，需要配置SGW/PGW拓扑选择。 
通过配置实现PGW与SGW的合一选择或就近选择，即优先选择主机名相近的一组SGW与PGW。 
配置前提 :DNS服务器与MME的对接数据配置完整。 
TAI和eNodeB信息已规划好，APN信息已规划好。 
SGW/PGW的组网规划已确定。 
配置步骤 :（可选）配置DNS服务器。 当使用中兴通讯的DNS服务器时，需要进行本步骤的操作。 
配置使用TAI-FQDN解析SGW。 
配置开启拓扑选择。 
配置使用优先级权重选择SGW/PGW 
配置实例 :场景说明
大区内的SGW与PGW合一，集中部署在中心城市，SGW与PGW有4组。 
使用拓扑选择，SGW之间以及PGW之间是负荷分担选择。 
用户在大区内附着，根据TAI解析到SGW列表，根据APN解析出PGW列表，根据拓扑关系选择出多组SGW与PGW：SGW1与PGW1，SGW2与PGW2，SGW3与PGW3，SGW4与PGW4，然后再根据SGW权重选择一组SGW与PGW使用。 
数据规划
本地EPC HOST和EPC APN不配置，使用DNS解析。 
规划的APN为cmwap.com，规划的TAI为460-00-0001。 
SGW与PGW的其他信息参见下表。 
GW编号|GW主机名|优先级|权重|地址
---|---|---|---|---
PGW1|topon.s5s8.pgw.xgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.1
SGW1|topon.s5s8.sgw. xgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.1
PGW2|topon.s5s8.pgw.xgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.2
SGW2|topon.s5s8.sgw.xgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.2
PGW3|topon.s5s8.pgw.xgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.3
SGW3|topon.s5s8.sgw.xgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.3
PGW4|topon.s5s8.pgw.xgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|10.1.1.4
SGW4|topon.s5s8.sgw.xgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org|10|100|20.1.1.4
配置步骤
根据规划，进行如下配置： 
配置DNS上的数据步骤操作配置APN-FQDN的第一步解析，即PGW的NAPTR查询配置ZONE。zone "apn.epc.mnc000.mcc460.3gppnetwork.org"
 { type master; file "db.epcapn.pgw"; };配置RR，文件名为db.epcapn.pgw。$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
	
;                  IN   NAPTR order  pref.  flag     
service                       regexp 	replacement 
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.pgw.xgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw.xgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.pgw.xgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
cmwap.com  IN   NAPTR  10    100    "a"   
"x-3gpp-pgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.pgw.xgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
保存文件。配置TAI-FQDN的第一步解析，即SGW的NAPTR查询配置ZONE。zone "tac.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epctai.sgw";};配置RR，文件名为db.epctai.sgw。$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
	
;                  IN   NAPTR order  pref.  flag     
service                       regexp 	replacement 
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"   
"x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw.xgw1.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"   
"x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw.xgw2.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"   
"x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw.xgw3.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
tac-lb01.tac-hb00  IN   NAPTR  10    100    "a"   
"x-3gpp-sgw:x-s5-gtp:x-s8-gtp"   "" 	    
topon.s5s8.sgw.xgw4.nj.js.node.epc.mnc000.mcc460.3gppnetwork.org.
保存文件。配置主机名的解析，即A类查询配置ZONEzone "node.epc.mnc000.mcc460.3gppnetwork.org" 
{ type master; file "db.epchost.saegw"; };配置RR，文件名为db.epchost.saegw$TTL 3600
@	IN	SOA	 jsdns1.mnc000.mcc460.gprs.  . (
					2013072800	;Serial
					3600	;Refresh
					900  	;Retry
					604800	;Expire
					3600 )	;Minimum
	IN	NS	jsdns1.mnc000.mcc460.gprs.
	IN	NS	jsdns2.mnc000.mcc460.gprs.
	
topon.s5s8.pgw.xgw1.nj.js     	IN	A	10.1.1.1
topon.s5s8.pgw.xgw2.nj.js    	IN	A	10.1.1.2
topon.s5s8.pgw.xgw3.nj.js    	IN	A	10.1.1.3
topon.s5s8.pgw.xgw4.nj.js     	IN	A	10.1.1.4
topon.s5s8.sgw.xgw1.nj.js     	IN	A	20.1.1.1
topon.s5s8.sgw.xgw2.nj.js     	IN	A	20.1.1.2
topon.s5s8.sgw.xgw3.nj.js     	IN	A	20.1.1.3
topon.s5s8.sgw.xgw4.nj.js     	IN	A	20.1.1.4
保存文件。DNS服务器数据同步执行命令rndc reload。如果没有此命令，需停止DNS服务进程，然后再启动。 
配置MME上的数据步骤操作配置SGW的解析方式为TAI-FQDNSET PACKET DOMAIN PARAMETER:FQDNRESOLVESGW="TAI-FQDN";配置使用拓扑选择SET PACKET DOMAIN PARAMETER:TOPOLOGY="YES";配置MME通过权重和优先级选择SGW/PGW设置MME通过权重和优先级选择SGW。SET SOFTWARE PARAMETER:PARAID=786516,PARAVALUE=1;设置MME通过权重和优先级选择PGWSET SOFTWARE PARAMETER:PARAID=786519,PARAVALUE=1;数据同步SYNA 
调整特性 :无 
测试用例 :###### 根据优先级选择GW，SGW负荷分担组网 
测试项目|移动用户从E-UTRAN接入，根据TA规划选择本区域的S-GW
测试目的|验证SGW负荷分担组网时，MME选择本区域的S-GW。
预置条件|EPS网络中各网元系统及操作维护台运行正常。用户在HSS中已签约EPS业务。SGW负荷分担组网，在DNS上按照2.1.4.1做SGW、PGW的解析配置。在MME上建立S1接口跟踪，用户跟踪，GTPC接口跟踪。在MME上配置Gateway选择是否考虑拓扑关系为否。
测试过程|UE在TA1开机发起附着。移动到TA2，触发TAU流程。在网络侧查询用户的信息。
通过准则|UE附着成功，默认承载建立成功。TAU成功，SGW发生重选。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
###### 根据优先级选择GW，SGW互备组网 
测试项目|移动用户从E-UTRAN接入，根据优先级选择本区域的S-GW
测试目的|验证SGW互备组网时，MME选择本区域的S-GW。
预置条件|EPS网络中各网元系统及操作维护台运行正常。用户在HSS中已签约EPS业务。SGW互备组网，在DNS上按照2.1.4.2做SGW、PGW的解析配置。在MME上建立S1接口跟踪，用户跟踪，GTPC接口跟踪。在MME上配置Gateway选择是否考虑拓扑关系为否。在MME上开启软参786801。
测试过程|UE在TA1开机发起附着。移动到TA2，触发TAU流程。在网络侧查询用户的信息。
通过准则|UE是否附着成功，默认承载是否建立成功。TAU成功，SGW发生重选。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
###### 根据拓扑选择GW 
测试项目|移动用户从E-UTRAN发起附着请求，根据拓扑关系，选择地理位置最近的一组SGW和PGW
测试目的|验证EPS网络能够根据拓扑信息，选择地理位置最近SGW和PGW。
预置条件|EPS网络中各网元系统及操作维护台运行正常。用户在HSS中已签约EPS业务。在DNS上按照2.2.4做SGW、PGW的解析配置。在MME上建立S1接口跟踪，用户跟踪，GTPC接口跟踪。在MME上配置Gateway选择是否考虑拓扑关系为是。
测试过程|UE开机发起附着。在网络侧查询用户的信息。
通过准则|UE附着成功，默认承载建立成功。根据主机名的拓扑关系选择最近的SGW和PGW消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
###### PGW不可达重选 
测试项目|PGW不可达，选择新的可达PGW进行创建会话尝试
测试目的|验证附着或PDN建立流程，如果选择的PGW不可达，则重新选一个可达的PGW，进行第二次creat session request尝试。
预置条件|DNS解析出两个不同的PGW地址，第一个地址不可达，另一个可达。
测试过程|用户发起附着或PDN建立流程；DNS解析出不同的两个地址（拥有不同的优先级），其中第一个地址不可达，另一个可达；发送携带第一个地址的creat session request消息，收到响应带原因值“#100 Remote peernot responding”；
通过准则|MME重选PGW，再次发送creat session request消息，其中携带第二个PGW地址。
测试结果|-
常见问题处理 :问题描述|解决方法
---|---
GW选择错误|检查是否存在告警节点信息。检查DNS解析的SGW和PGW是否有变更。检查是否有本地特殊配置。
GW选择失败|检查携带的APN是否正确。检查DNS链路是否正常。检查DNS上配置数据是否被删除或改动。
## ZUF-78-05-002 SGW选择 
SGW选择功能为用户选择可用的SGW。SGW与eNodeB相连接，负责用户面数据路由处理和数据包转发，而eNodeB管理用户位置信息。因此，SGW管理的区域就与用户位置相关联。MME优先选取和eNodeB之间路径最短的SGW，以此减少数据传送延迟。
## ZUF-78-05-003 SGSN选择 
概述 :SGSN选择功能用于为UE选择一个可用的SGSN。 
收益 :SGSN选择功能用于为UE选择一个可用的SGSN。SGSN选择是在网络拓扑基础上进行的，即，选择的SGSN既服务于UE所在的位置又和SGSN的服务区域相重叠。优先选择带有服务区SGSN，以减少改变SGSN的可能性。当MME/SGSN选择目标SGSN时，SGSN选择功能在可能的目标SGSN间进行简单的负荷分担。 
描述 :SGSN选择功能用于为UE选择一个可用的SGSN。SGSN选择是在网络拓扑基础上进行的，即，选择的SGSN既服务于UE所在的位置又和SGSN的服务区域相重叠。优先选择带有服务区SGSN，以减少改变SGSN的可能性。当MME/SGSN选择目标SGSN时，SGSN选择功能在可能的目标SGSN间进行简单的负荷分担。 
当UE从E-UTRAN切换到2G/3G网络，MME需要选择一个SGSN为UE提供2G/3G业务。 
SGSN选择需要满足以下条件： 
UE位于SGSG服务区。 
SGSN可用。 
如果有多个SGSN符合条件，MME根据负荷分担进行选择。 
如果有MME和SGSN的Combo局，MME优先选择该SGSN。 
## ZUF-78-05-004 MME选择 
概述 :MME选择功能用于为UE选择一个可用的MME。 
收益 :MME选择功能用于为UE选择一个可用的MME。MME选择是在网络拓扑基础上进行的，即，选择的MME既服务于UE所在的位置又和MME的服务区域相重叠。优先选择带有服务区MME，以减少改变MME的可能性。当MME/SGSN选择目标MME时，MME选择功能在可能的目标MME间进行简单的负荷分担。 
描述 :MME选择功能用于为UE选择一个可用的MME。MME选择是在网络拓扑基础上进行的，即，选择的MME既服务于UE所在的位置又和MME的服务区域相重叠。优先选择带有服务区MME，以减少改变MME的可能性。当MME/SGSN选择目标MME时，MME选择功能在可能的目标MME间进行简单的负荷分担。 
当UE在E-UTRAN中移动时，如果目标区域不在当前MME的服务区中，MME需要根据此目标区域选择新的MME。 
MME选择需要满足以下条件： 
UE位于MME服务区。 
MME可用。 
如果有多个MME符合条件，MME根据负荷分担进行选择。 
## ZUF-78-05-005 HSS选择 
概述 :HSS选择功能用于为UE选择一个可用的HSS。 
收益 :本功能是一个基本功能。 
描述 :当UE发起附着或TAU过程，UE需要选择HSS进行注册。 
MME和HSS之间有两种连接： 
MME直接和HSS连接。 
MME通过DRA和HSS连接。 
对于备份： 
无备用HSS 
有备用HSS 
MME基于用户IMSI分析获得一个或多个HSS或DRA。MME优先选择主用HSS或DRA。当主用HSS或DRA不可用时，MME再选择备用HSS或DRA。  
## ZUF-78-05-006 MSC选择 
特性描述 :特性描述 :描述 :定义 :MSC选择，是指MME在MSC POOL中为UE选择一个可用的移动交换中心，该功能是实现CSFB和SRVCC的基础。MSC选择功能包括基于SGs口MSC选择功能和基于Sv口MSC选择功能。
背景知识 :MSC选择功能涉及两种场景。 
CSFBCSBF是在未部署IMS部署时，LTE用户使用语音业务的过渡方案。由于LTE网络只提供数据业务，因此当用户发起或者接收语音呼叫时，需回落到CS域进行处理。在此种场景下，运营商无需部署IMS，只需要升级MSC就可以支持语音业务。CSBF还可以解决LTE手机漫游场景的语音呼叫问题，即在拜访地网络没有部署IMS，或者IMS漫游协议尚未应用的情况下，CSFB可以为漫入的LTE用户提供语音业务。为完成CSFB业务，MME需要与多个MSC之间建立SGs口连接，因此MME需要对MSC进行选择，以完成用户在CS域的位置更新、注册、寻呼和短消息业务。 
SRVCCSRVCC是基于IMS的VoIP呼叫解决方案。SRVCC方案利用IMS核心网络提供LTE VoIP语音业务的路由、控制和业务触发，并提供LTE向2G/3G切换时的语音连续性保证。SRVCC的实现过程实质上就是一个切换过程：当终端在LTE网络中，通过IMS来实现语音功能。当终端离开LTE网络后，通过MSC切换到2G/3G 网络中从而实现在2G/3G网络中的语音功能。该方案可以解决两个问题：语音控制的连续性问题UE移动到CS网络切换时的语音连续性问题为完成SRVCC切换，MME需要与多个MSC之间使用Sv口连接，MME需要对MSC进行选择，以便将语音呼叫切换到MSC。 
应用场景 :MSC选择是实现CSFB和SRVCC的基础： 
CSFB采用基于SGs口的MSC选择方案。 
SRVCC采用基于Sv口的MSC选择方案。 
MME与MSC之间的组网，有多种形式。根据UE回落和切换后，MME是否与服务MSC相连，可将组网方式分为Proxy MSC方式和直连方式，具体参见[表1]。
组网方式|MSC升级方式|SGs口MSC选择方式|Sv口MSC选择方式
---|---|---|---
Proxy MSC方式|无需全网MSC升级，只需要新增一对支持CSFB和SRVCC的MSC。|Proxy MSC组网方式，UE位置变化时无需向MSC发起SGs口位置更新。|MME基于切换请求消息中的Target ID使用DNS进行域名解析，选择对应的Proxy MSC。
直连组网方式|需要全网MSC升级，方能支持CSFB和SRVCC。|直连组网方式，UE位置变化时，MME选择和TA同覆盖的MSC，发起SGs位置更新。|MME基于切换请求消息中的Target ID使用DNS进行域名解析，选择UE在CS域相连的MSC。
应用场景一：CSFB场景下的MSC选择
CSFB场景下，MME与MSC之间使用SGs口相连。MME与多个MSC连接，MSC之间采用负荷分担组网或者互备组网。 
SGs口MSC选择，负荷分担组网 
负荷分担的MSC基于各自的处理能力，会被分配不同数量的用户。一个LAI归属MSC POOL内的所有MSC。MME基于TAI映射到LAI，再根据LAI归属POOL内各个MSC的权重选择MSC；一旦有MSC宕机，MME将继续在可用的MSC中按权重选择合适的MSC。具体组网方式如[图1]所示。
图1  SGs口MSC选择负荷分担组网

SGs口MSC选择，多PLMN直连负荷分担组网 
LTE用户归属不同的2/3G网络，在回落时，处于同一区域的UE，选择各自归属的2/3G网络。MME基于用户号段和TAI映射到LAI，选择用户归属的MSC网络。具体组网方式如[图2]所示。
图2  多PLMN直连负荷分担组网

 
应用场景二：SRVCC场景下的MSC选择
SRVCC场景下，MME与MSC之间使用Sv口相连。MME与多个MSC连接，MSC之间采用负荷分担组网或者互备组网。 
Sv口MSC选择，负荷分担组网 
MSC部署在大区内的中心城市，大区内MSC间负荷分担，大区间MSC没有互相备份。当LTE用户移动到2/3G网络时，MME为其选择MSC网络，根据MSC POOL内MSC的权重选择MSC，具体组网方式如[图3]所示。
图3  Sv口MSC选择负荷分担组网

Sv口MSC选择，互备组网 
MSC部署在大区内的中心城市，大区内MSC间负荷分担，大区间MSC互相备份。当LTE用户移动到2/3G网络时，MME为其优选高优先级大区内的MSC网络；当高优先级大区内的MSC网络故障时，选择低优先级大区下的MSC网络。具体组网方式如[图4]所示。
图4  Sv口MSC选择互备组网

客户收益 :受益方|受益描述
---|---
运营商|提高业务可靠性：优先级、权重和有效性选择等策略提高了业务可靠性。提高策略灵活性：基于TA、IMSI/MSISDN和TA选择MSC，提高了策略灵活性。
移动用户|用户在LTE网络进行高速数据业务，同时可拨打或接听语音呼叫。LTE网络信号不佳时，仍可享受语音通话不受影响。
实现原理 :系统架构 :CSFB组网
EPS网络中CSFB组网如[图5]所示。
图5  CSFB组网图

SRVCC组网
EPS网络E-UTRAN与GERAN/UTRAN间SRVCC切换架构如[图6]所示。
图6  EPS网络E-UTRAN与GERAN/UTRAN间SRVCC切换架构

涉及的网元 :网元名称|网元作用
---|---
MME|CSFB场景下，当UE终端进行联合附着或联合TAU业务时，MME进行SGs口的MSC选择。如果MME基于RAI/RNCID进行MSC Server域名解析时，可使用DNS Server进行域名解析。SRVCC场景下，MME基于本地配置或者DNS Server进行Sv口的MSC选择。
MSC|CSFB场景下，MSC接收MME发送的位置更新消息，完成用户在CS域的位置更新、注册以及发起对UE的语音终呼和短消息业务。SRVCC场景下，MSC通过Sv口与MME连接，能够处理MME发起的基于SRVCC的呼叫切换，在SRVCC切换过程中完成用户语音业务到IMS域的切换。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
SGs|ZUF-78-16-007 SGs
Sv|ZUF-78-16-008 Sv
本网元实现 :SGs口MSC选择流程
根据用户的IMSI/MSISDN号段和TAI获取到映射的LAI，如[图7]所示，选中MSC POOL1。
图7  SGs口MSC选择流程 1

在同一个POOL内，根据优先级顺序，选择最高优先级的一组VLR，如[图8]所示，选中VLR11和VLR12。
图8  SGs口MSC选择流程 2

在选中的VLR中，按下面的顺序进行VLR选择： 
UE携带NRI对应的VLR。 
IMSI后三位值归属的VLR。 
MM上下文保存的VLR。 
如果上述VLR均不可用，则在可用VLR中，根据权重选择。 
如果在高优先级的组中没有可用的VLR，则会再次执行第2步，选择下一组优先级高的VLR，依次类推，如[图9]所示，选中VLR11'和VLR12'。
图9  SGs口MSC选择流程

Sv口MSC选择
根据Target ID构造FQDN。通常有以下几种构造格式： 
使用RNC ID例如：rnc<RNC>.rnc.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org 
使用RAITarget ID中包含有RAC例如：rac<RAC>.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.orgTarget ID中不包含有RAC例如：rac00FF.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org 
根据构造的FQDN去DNS解析或者本地地址解析，得到UE在CS域相连的MSC列表，剔除无效和告警地址后，在过滤后的有效地址中，继续选择MSC。 
根据优先级和权重选择MSC。在最高优先级的MSC列表中，按照权重选择到MSC。 
根据子网优先级选择MSC。选择具有高子网优先级的MSC地址；如果相同子网优先级的MSC地址有多个，随机选择到一个MSC地址。 
 说明： 
为了满足IMS通话状态下，UE回落到CS域完成特定CS业务而触发SRVCC的功能要求，MME在选择Sv口MSC时，优先选择同时具备以下两个特点的MSC： 
UE在联合附着流程或联合TAU流程中注册上的MSC。 
具备CSFB和SRVCC业务处理能力的MSC。 
MME根据Target ID获取MSC地址失败时，还可使用本地配置的缺省MSC。 
业务流程 :SGs口MSC选择涉及如下流程： 
联合附着 
联合TAU 
Sv口MSC选择涉及流程：从E-UTRAN发起的SRVCC的呼叫流程 
联合附着流程中的MSC选择
图10  联合附着流程中的MSC选择

流程说明如下： 
UE通过eNodeB发送Attach Request消息到MME，发起附着流程。 
MME根据3GPP 23.401协议的附着流程继续附着流程，直到接收到SGW发送的创建会话响应消息。 
MME根据TAI以及用户的IMSI/MSISDN，查询本地配置，获取映射的LAI，然后基于LAI得到LAI归属的MSC POOL，最后再根据POOL内各个MSC/VLR的优先级和权重以及NRI、IMSI得到MSC/VLR局向ID。 
MME确定MSC局向ID后，按照路由组→路由→链路的层级关系，选择可用的SGs链路，向此局向发送位置更新消息。 
同系统现有处理，MME继续完成后续的联合附着流程。 
联合TAU流程中的MSC选择
图11  联合TAU流程中的MSC选择

流程说明如下： 
UE通过eNodeB发送TAU Request消息到MME，发起联合TAU流程。 
MME根据3GPP 23.401协议进行TAU业务处理，从Old MME获得用户的上下文，在新的SGW完成承载建立。 
MME根据TAI以及用户的IMSI/MSIDN，查询本地配置，获取映射的LAI，然后基于LAI得到LAI归属的MSC POOL，最后再根据POOL内各个MSC/VLR的优先级和权重以及NRI、IMSI得到MSC/VLR局向ID。 
MME确定MSC局向ID后，按照路由组→路由→链路的层级关系，选择可用的SGs链路，向此局向发送位置更新消息。 
同系统现有处理，MME继续完成后续的联合TAU流程。 
SRVCC流程中的MSC选择
图12  SRVCC流程中的MSC选择

流程说明如下： 
源E-UTRAN基于UE的测量报告，决定触发到GERAN的SRVCC切换，发送Handover Required (Target ID, generic Source to Target Transparent Container, SRVCC HO Indication) 消息到源MME。 
同系统现有处理，根据语音承载的QCI（QCI 1）以及SRVCC HO Indication，源MME分离语音承载和其他PS承载。 
MME根据切换请求消息中的Target ID构造FQDN，进行DNS查询或者本地地址解析，并根据查询或解析返回的结果，按优先级和权重，选择MSC Server的IP地址，发送SRVCC PS to CS Request消息到MSC Server。 
同系统现有处理，MME继续完成后续的SRVCC流程。 
系统影响 :该特性是CSFB和SRVCC的基础，不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性是CSFB与SRVCC的基础，不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401：General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access|-
3GPP TS 23.272：Circuit Switched (CS) fallback in Evolved Packet System (EPS)|-
3GPP TS 29.118：Mobility Management Entity (MME) –Visitor Location Register (VLR) SGs interface specification|-
3GPP TS 23.216：Single Radio Voice Call Continuity (SRVCC)|-
特性能力 :名称|指标
---|---
SGs口MSC POOL最大个数|1024个
SGs口MSC POOL内的MSC/VLR局向最大个数|32个
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性对应的License项目为MME支持SRVCC功能，此项目显示为支持，表示支持SRVCC功能。 
该特性对应的License项目为MME支持CSFB功能，此项目显示为支持，表示支持CSFB功能。 
对其他网元的要求 :UE|eNodeB|MSC|HSS
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :SGs口对接参数规划：需要根据组网和无线覆盖，规划好TA和LA的对应关系，以及MSC对LA的管辖关系。需要规划好SGs口使用的VLR Name和MME Name。 
Sv口目标MSC地址解析，MME根据切换请求消息中的Target ID构造FQDN来解析目标MSC的地址，Target ID构造的FQDN，有以下几种格式：使用RNC ID：rnc<RNC>.rnc.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org使用RAI：Target ID中包含有RAC：rac<RAC>.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.orgTarget ID中不包含有RAC：rac00FF.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org 
O&M相关 :命令 :配置项|命令
---|---
MME配置支持SGs口|SET SGSFLAG
增加SGs偶联|ADD SCTP
增加SGs连接|ADD SGSCONN
增加SGs路由|ADD SGS ROUTE
增加SGs路由组|ADD SGS ROUTE GROUP
增加SGs局向路由组|ADD SGS OFFICE ROUTE
增加位置区配置|ADD LAI
配置TA和LA位置区关联|ADD TA
新增SGs口VLR局向配置|ADD VLROFFICE
新增SGs口VLR POOL配置|ADD VLRPOOL
SGs口选择VLR POOL配置|ADD LAIVLRPOOL
设置基于号段和TAI映射LAI策略|SET IMSITAITOLAI POLICY
新增基于号段和TAI映射LAI配置|ADD IMSITAITOLAI
新增LAI映射键值的号码分析|ADD MDNAL
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本特性无需特殊配置，完成初始配置后即可使用。 
配置前提 :MME与MSC之间物理链路是通路。 
配置过程 :使用[SHOW SGSFLAG]命令，检查MME是否支持SGs口。
使用[ADD SCTP]命令，增加SGs偶联。
使用[ADD SGSCONN]命令，增加SGs连接。
使用[ADD SGS ROUTE]命令，增加SGs路由。
使用[ADD SGS ROUTE GROUP]命令，增加SGs路由组。
使用[ADD SGS OFFICE ROUTE]命令，增加增加SGs局向路由组。
使用[ADD LAI]命令，增加位置区配置。
使用[ADD TA]命令，将TA与上面配置的LA位置区关联。
使用[ADD VLROFFICE]命令，新增SGs口VLR局向配置。
使用[ADD VLRPOOL]命令，新增SGs口VLR POOL配置。
使用[ADD LAIVLRPOOL]命令，新增SGs口选择VLR POOL配置。
使用[SET IMSITAITOLAI POLICY]命令，设置基于号段和TAI映射LAI策略。
使用[ADD IMSITAITOLAI]命令，新增基于号段和TAI映射LAI配置。
使用[ADD MDNAL]命令，新增LAI映射键值的号码分析。
配置实例 :场景说明 :若LTE用户归属于不同的2/3G网络，那么在语音回落时，处于同一区域的UE，需要选择各自归属的2/3G网络。 
MME可以通过以下两种方式为用户选择归属地MSC/VLR： 
基于IMSI号段选择用户归属地MSC/VLR 
基于MSISDN号段选择用户归属地MSC/VLR 
基于MSISDN号段选择用户归属地MSC/VLR如[图1]所示。
图1   MME基于MSISDN号段选择用户归属地MSC/VLR

数据规划 :命令|参数名称|取值|数据来源|说明
---|---|---|---|---
ADD SCTP|SCTP标识（ID）|111、112、121、122|本端规划|该参数为偶联的标识，在网元内标识唯一偶联，所有类型的SCTP偶联的SCTP标识均不能重复。
别名（NAME）|ADD SCTP|MSCSCTP111、MSCSCTP112、MSCSCTP121、MSCSCTP122|本端规划|该参数为偶联的别名，便于用户管理偶联。
本端端口（LOCPORT）|ADD SCTP|6001|本端规划|该参数为偶联的本端端口号。
对端端口（REMPORT）|ADD SCTP|6001|本端规划|本局与对端信令设备的对接参数之一，用于表示对端在承载协议消息中所使用的SCTP端口号。
VPNID1|ADD SCTP|2|本端规划|该参数为偶联第一对地址的VPNID。
本端IP地址1（LOCADDR1）|ADD SCTP|131.1.17.159|本端规划|该参数为偶联第一对地址的本端IP，具体地址值需与对端网元协商规划。本端IP地址1为必填参数。
对端IP地址1（REMADDR1）|ADD SCTP|40.40.1.1、40.40.1.2、40.40.2.1、40.40.2.2|本端规划|该参数为偶联第一对地址的对端IP，其值和对端保持一致。如果本偶联为动态偶联，且本端作为动态偶联服务端，则不要配置此参数。
应用属性（ROLE）|ADD SCTP|客户端|本端规划|该参数为偶联应用属性即本端做为偶联客户端或服务端。
应用协议类型（PROTOCALTYPE）|ADD SCTP|SGS|本端规划|该参数为偶联的归属上层协议类型，根据业务情况选择协议类型。
ADD SGSCONN|SGS连接编号（ID）|111、112、121、122|本端规划|该参数用于标识一条SGs连接，该标识要求全局唯一。
SCTP连接标识（SCTPID）|ADD SGSCONN|111、112、121、122|本端规划|目前MME同MSC/VLR交互的协议是承载在SCTP上的，该参数用于指示该SGs连接关联的SGs偶联。
SGS连接名称（NAME）|ADD SGSCONN|sgslink111、sgslink112、sgslink121、sgslink122|本端规划|该参数表示配置的SGs连接别名。
ADD SGS ROUTE|路由ID（ROUTEID）|11、12、21、22|本端规划|该参数用于标识一条SGs路由，该参数是全局唯一的。
分担方式（PARTAKEMODE）|ADD SGS ROUTE|PARTAKE|本端规划|该参数表明该SGs路由的负荷分担属性。
连接编号（CONNECTION）|ADD SGS ROUTE|111、112、121、122|本端规划|该参数用于指示该SGs路由关联的SGS连接编号。
用户别名（NAME）|ADD SGS ROUTE|SGSROUTE_11、SGSROUTE_12、SGSROUTE_21、SGSROUTE_22|本端规划|配置SGs路由的别名。
ADD SGS ROUTE GROUP|路由组ID（ROUTEGRPID）|11、12、21、22|本端规划|该参数用于标识一条SGs路由组，该标识要求全局唯一。
分担方式（PARTAKEMODE）|ADD SGS ROUTE GROUP|PARTAKE|本端规划|该参数表明该SGs路由组的负荷分担属性。取值含义如下所示。
路由ID（ROUTE）|ADD SGS ROUTE GROUP|111、112、121、122|本端规划|该参数用于指示该SGs路由组关联的SGs路由。
用户别名（NAME）|ADD SGS ROUTE GROUP|SGSRTGP_11、SGSRTGP_12、SGSRTGP_21、SGSRTGP_22|本端规划|配置SGs路由组的别名。
ADD SGS OFFICE ROUTE GROUP|局向ID（OFFICEID）|11、12、21、22|本端规划|该参数用于标识一个SGs局向，该参数要求全局唯一。
直达路由组ID（ROUTEGRPID）|ADD SGS OFFICE ROUTE GROUP|11、12、21、22|本端规划|该参数表明该SGs局向关联的SGs直达路由组，一个SGs局向只能关联一个SGs直达路由组。
用户别名（NAME）|ADD SGS OFFICE ROUTE GROUP|SGSOFC_11、SGSOFC_12、SGSOFC_21、SGSOFC_22|本端规划|配置的SGs局向的别名。
ADD LAI|位置区名（NAME）|LAI1、LAI2|本端规划|位置区名称为当前位置区的标识。该名称一般在网络建设时进行规划。
移动国家码（MCC）|ADD LAI|460|本端规划|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
移动网号（MNC）|ADD LAI|01|本端规划|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
位置区域码(HEX)（LAC）|ADD LAI|0111、0112|本端规划|位置区编码用于识别网络中的位置区。应该根据网络规划进行编码。
ADD TA|跟踪区标识（TAID）|1|本端规划|各TA在MME内部的标识，在MME中一个TAID对应一个跟踪区TA。
组号（GRPID）|ADD TA|1|本端规划|该参数标识TA归属的组号。
移动国家码（MCC）|ADD TA|460|本端规划|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
移动网号（MNC）|ADD TA|01|本端规划|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
跟踪区域码(HEX)（TAC）|ADD TA|0110|本端规划|跟踪区域码，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个跟踪区。
是否使用全局时区（GLOBALTZ）|ADD TA|YES|本端规划|该参数标识当前TA是否与MME的全局时区一致。
位置区名（LAI）|ADD TA|LAI1|本端规划|跟踪区对应的位置区名称。
跟踪区名称（NAME）|ADD TA|TA1|本端规划|用户自定义跟踪区名称，便于记忆和识别各跟踪区。
ADD VLROFFICE|VLR局向标识（VLROFFICEID）|11、12、21、22|本端规划|该参数用于指定SGs口VLR局向标识。
VLR名称（VLRNAME）|ADD VLROFFICE|mscvlr_11、mscvlr_12、mscvlr_21、mscvlr_22|本端规划|该参数用于指示SGs口VLR局向名称。
ADD VLRPOOL|VLR POOL标识（VLRPOOLID）|1、2|本端规划|该参数用于指定SGs口VLR POOL标识。
VLR局向标识（VLROFFICEID）|ADD VLRPOOL|11、12、21、22|本端规划|该参数用于指示SGs口VLR局向标识。
VLR级别（VLRLEVEL）|ADD VLRPOOL|LEVEL_1、LEVEL_2|本端规划|该参数用于指示SGs口VLR局向在VLR POOL中的优先级别, 数值越低优先级越高。
VLR权重（VLRWEIGHT）|ADD VLRPOOL|1000|本端规划|该参数用于指示SGs口VLR局向在VLR POOL中的权重。
ADD LAIVLRPOOL|位置区名（LAINAME）|LAI1、LAI2|本端规划|该参数用于指定SGs口VLR POOL 管理的位置区名。
VLR POOL标识（VLRPOOLID）|ADD LAIVLRPOOL|1、2|本端规划|该参数用于指示SGs口LAI关联的VLR POOL标识。
SET IMSITAITOLAI POLICY|支持基于MSISDN和TAI映射LAI（SUPMSISDNTAITOLAI）|YES|本端规划|该参数用于设置MME是否支持基于MSISDN和TAI映射LAI。
ADD IMSITAITOLAI|LAI映射键值索引（IDX）|1|本端规划|该参数用于指定一个IMSI或MSISDN号码分析的索引值。
跟踪区标识（TAIID）|ADD IMSITAITOLAI|1|本端规划|该参数用于指定要进行映射的跟踪区标识。
位置区名（LAINAME）|ADD IMSITAITOLAI|LAI2|本端规划|该参数用于指定映射后的位置区名。
ADD MDNAL|被分析号码（DGT）|86137|本端规划|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。
分析器入口（ENTR）|ADD MDNAL|DAS_MSISDN_LAI|本端规划|该参数用于指定号码分析对应的分析器入口。不同的分析器入口对应了不同的分析类型。
号码分析结果索引（RST）|ADD MDNAL|1|本端规划|该参数用于指定号码分析对应的号码分析结果索引。
配置步骤 :步骤|说明|操作
---|---|---
1|检查MME是否支持SGs口。|SHOW SGSFLAG
2|增加SGs偶联|ADD SCTP:ID=111,NAME="MSCSCTP111",LOCPORT=6001,REMPORT=6001,LOCADDR1="131.1.17.159",REMADDR1="40.40.1.1",PROTOCALTYPE="SGS"ADD SCTP:ID=112,NAME="MSCSCTP112",LOCPORT=6001,REMPORT=6001,LOCADDR1="131.1.17.159",REMADDR1="40.40.1.2",PROTOCALTYPE="SGS"ADD SCTP:ID=121,NAME="MSCSCTP121",LOCPORT=6001,REMPORT=6002,LOCADDR1="131.1.17.159",REMADDR1="40.40.2.1",PROTOCALTYPE="SGS"ADD SCTP:ID=122,NAME="MSCSCTP122",LOCPORT=6001,REMPORT=6002,LOCADDR1="131.1.17.159",REMADDR1="40.40.2.2",PROTOCALTYPE="SGS"
3|增加SGs连接|ADD SGSCONN:ID=111,SCTPID=111,NAME="sgslink111"ADD SGSCONN:ID=112,SCTPID=112,NAME="sgslink112"ADD SGSCONN:ID=121,SCTPID=121,NAME="sgslink121"ADD SGSCONN:ID=122,SCTPID=122,NAME="sgslink122"
4|增加SGs路由配置|ADD SGS ROUTE:ROUTEID=11,PARTAKEMODE="PARTAKE",CONNECTION="111",NAME="SGSROUTE_11"ADD SGS ROUTE:ROUTEID=12,PARTAKEMODE="PARTAKE",CONNECTION="112",NAME="SGSROUTE_12"ADD SGS ROUTE:ROUTEID=21,PARTAKEMODE="PARTAKE",CONNECTION="121",NAME="SGSROUTE_21"ADD SGS ROUTE:ROUTEID=22,PARTAKEMODE="PARTAKE",CONNECTION="122",NAME="SGSROUTE_22"
5|增加SGs路由组配置|ADD SGS ROUTE GROUP:ROUTEGRPID=11,PARTAKEMODE="PARTAKE",ROUTE="11",NAME="SGSRTGP_11"ADD SGS ROUTE GROUP:ROUTEGRPID=12,PARTAKEMODE="PARTAKE",ROUTE="12",NAME="SGSRTGP_12"ADD SGS ROUTE GROUP:ROUTEGRPID=21,PARTAKEMODE="PARTAKE",ROUTE="21",NAME="SGSRTGP_21"ADD SGS ROUTE GROUP:ROUTEGRPID=22,PARTAKEMODE="PARTAKE",ROUTE="22",NAME="SGSRTGP_22"
6|增加SGs局向路由组配置|ADD SGS OFFICE ROUTE GROUP:OFFICEID="11",ROUTEGRPID="11",NAME="SGSOFC_11"ADD SGS OFFICE ROUTE GROUP:OFFICEID="12",ROUTEGRPID="12",NAME="SGSOFC_12"ADD SGS OFFICE ROUTE GROUP:OFFICEID="21",ROUTEGRPID="21",NAME="SGSOFC_21"ADD SGS OFFICE ROUTE GROUP:OFFICEID="22",ROUTEGRPID="22",NAME="SGSOFC_22"
7|位置区配置|ADD LAI:NAME="LAI1",MCC="460",MNC="01",LAC="0111"ADD LAI:NAME="LAI2",MCC="460",MNC="01",LAC="0112"
8|跟踪区配置|ADD TA:TAID=1,GRPID=1,MCC="460",MNC="01",TAC="0110",GLOBALTZ="YES",LAI="LAI1",NAME="TA1"
9|新增SGs口VLR局向配置|ADD VLROFFICE:VLROFFICEID=11,VLRNAME="mscvlr_11"ADD VLROFFICE:VLROFFICEID=12,VLRNAME="mscvlr_12"ADD VLROFFICE:VLROFFICEID=21,VLRNAME="mscvlr_21"ADD VLROFFICE:VLROFFICEID=22,VLRNAME="mscvlr_22"
10|新增SGs口VLR POOL配置|ADD VLRPOOL:VLRPOOLID="1",VLROFFICEID="11",VLRLEVEL="LEVEL_1",VLRWEIGHT="1000"ADD VLRPOOL:VLRPOOLID="1",VLROFFICEID="12",VLRLEVEL="LEVEL_2",VLRWEIGHT="1000"ADD VLRPOOL:VLRPOOLID="2",VLROFFICEID="21",VLRLEVEL="LEVEL_1",VLRWEIGHT="1000"ADD VLRPOOL:VLRPOOLID="2",VLROFFICEID="22",VLRLEVEL="LEVEL_2",VLRWEIGHT="1000"
11|新增SGs口VLR局向配置|ADD LAIVLRPOOL:LAINAME="LAI1",VLRPOOLID=1ADD LAIVLRPOOL:LAINAME="LAI2",VLRPOOLID=2
12|设置基于号段和TAI映射LAI策略|SET IMSITAITOLAI POLICY:SUPMSISDNTAITOLAI="YES"
13|新增基于号段和TAI映射LAI配置|ADD IMSITAITOLAI:IDX=1,TAIID=1,LAINAME="LAI2"
14|新增LAI映射键值的号码分析|ADD MDNAL:DGT="86137",ENTR="DAS_MSISDN_LAI",RST=1
调整特性 :本特定不涉及调整特性。 
测试用例 :测试项目|基于MSISDN选择归属地MSC/VLR
---|---
测试目的|基于MSISDN选择归属地MSC/VLR
预置条件|1、系统正常运行。2、“支持基于IMSI和TAI映射LAI”配置为不支持；“支持基于MSISDN和TAI映射LAI”配置为支持。3、“基于号段和TAI映射配置”中正确配置LAI映射键值索引和跟踪区标识映射的位置区名。4、“移动号码分析”中配置MSISDN号段，号码分析器入口选择“MSISDN LAI映射键值分析”，号码分析索引为步骤3中配置的LAI映射键值索引。5、跟踪区配置中正确配置TAI映射的LAI。
测试过程|漫游用户联合附着/联合TAU
通过准则|MME基于MSISDN和TAI映射的LAI选择到用户归属地MSC/VLR
测试结果|-
常见问题处理 :无。 
## ZUF-78-05-007 PGW重选 
概述 :当PGW在Create Session Response消息中携带特定原因值时，MME支持选择其他PGW用于试图建立该会话。 
收益 :当某个PGW运行异常时，本特性可减少业务失败，提升用户体验。 
描述 :当MME接收到GW发送的Session Create Failure消息，并且该消息携带运营商期望重选的原因时。MME选择其他PGW用于建立当前的PDN连接。 
当前支持如下期望原因：系统失败（72）、无可用资源（73）、对端未响应（100）和APN拥塞（113）。 
## ZUF-78-05-008 AMF选择 
概述 :当UE从4G移动到5G网络时，MME选择可用的AMF为UE服务。 
收益 :本功能用于UE移动到5G网络时，选择可用的AMF。 
描述 :UE从4G网络移动到5G网络，MME根据目标位置选择AMF，MME根据目标TA构造FQDN，通过DNS查询或本地解析获取到AMF列表，完全根据DNS查询或本地解析返回结果进行选择。 
当有多个AMF符合必要条件时，MME可以根据多种策略进行优选，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用。 
优先级：用于AMF间互相备份。 
权重：用于AMF间负荷分担。 
AMF选择策略具体参见3GPP 23.502协议4.11.1.2.2 EPS to 5GS handover using N26 interface和3GPP 29.303协议5.4A Procedures for Discovering and Selecting an AMF章节。 
## ZUF-78-05-009 融合SMF选择 
特性描述 :特性描述 :描述 :定义 :融合SMF选择用于为具有4/5G能力的终端选择融合的PGW-C+SMF，是4/5G互操作的基础。包括融合SMF选择功能和融合SMF不可达重选普通PGW功能。
融合SMF选择功能：指具有4/5G能力的终端接入EPC网络时，MME选择融合的PGW-C+SMF。PGW是终结接连外部数据网络（如互联网、IMS等）的网关，是业务的锚点。所以在EPC中建立PDN连接时，需要选择融合SMF，以保证与5GS互操作过程中的业务连接性。 
融合SMF不可达重选普通PGW功能：指当MME检测出所有融合SMF均不可达时，选择普通的PGW。 
背景知识 :5G网络信号覆盖不全、VoNR业务不支持、网络过载等情况都有可能导致具有4/5G能力的UE在4G和5G网络间移动。移动过程中，会话连续性和业务中断时间会直接影响用户的业务体验，如语音类业务。 
为了保证4/5G互操作过程中的业务连续性，3GPP定义了4/5G融合网元。具有4/5G能力的UE在接入EPC网络建立PDN连接时，需要选择融合SMF。 
应用场景 :融合SMF的组网和部署方式与普通PGW相同。 
组网方式：负荷分担组网。互备组网。 
部署方式：与SGW合一部署。与SGW分开部署。 
根据组网和部署方式，融合SMF选择的应用场景如下： 
###### 场景一：融合SMF与SGW分开部署，MME选择融合SMF 
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，识别出融合SMF列表，基于优先级和权重选择出一个融合SMF。如[图1]所示。
图1  融合SMF与SGW分开部署，MME选择融合SMF

###### 场景二：融合SMF与SGW合一部署，MME选择融合SMF 
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，识别出融合SMF列表，根据SGW和融合SMF的合一或邻近关系，选出合一或拓扑最近的一对或多对SGW/SMF，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/SMF。如[图2]所示。
图2  融合SMF与SGW合一部署，MME选择融合SMF

###### 场景三：融合SMF与SGW分开部署，SMF均故障，MME选择普通PGW 
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，MME检测出所有的融合SMF均故障，在普通PGW列表中基于优先级和权重选择出一个普通PGW。如[图3]所示。
图3  融合SMF与SGW分开部署，SMF均故障，MME选择普通PGW

###### 场景四：融合SMF与SGW合一部署，合一SGW/SMF均故障，MME选择普通PGW 
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，MME检测出所有的SGW/SMF均故障，在普通PGW列表中根据SGW和PGW的合一或邻近关系，选出合一或拓扑最近的一对或多对SGW/PGW，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW。如[图4]所示。
图4  融合SMF与SGW合一部署，合一SGW/SMF均故障，MME选择普通PGW

客户收益 :受益方|受益描述
---|---
运营商|提高业务连续性：为具有4/5G能力的用户优先选择融合SMF，用户在4G和5G网络间移动时，业务不中断。提高业务可靠性：融合SMF故障时选择普通PGW，保证业务可靠性。
移动用户|保证业务连续性，提高终端业务体验。
实现原理 :系统架构 :本特性涉及的4/5G互操作架构图如[图5]所示。为了支持互操作，3GPP定义了4个4/5G合一的网元。
图5  4G和5G互操作架构图

涉及的网元 :网元名称|网元作用
---|---
UE|支持4/5G接入。
MME|使用S-NAPTR查询方式查询DNS服务器，为具有4/5G接入能力的终端选择融合SMF。检测出所有融合SMF均故障时，选择普通PGW。
SGW|在检测到PGW故障时，向MME发送PGW重启通知消息。
SMF|向MME发送PGW网元级动态负荷以及APN级负荷信息。
PGW|向MME发送PGW网元级动态负荷以及APN级负荷信息。
DNS Server|记录APN-FQDN和PGW列表的对应关系，根据APN-FQDN返回查询到的PGW列表。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
S1|ZUF-78-16-001 S1-MME
S6a|ZUF-78-16-002 S6a
S11|ZUF-78-16-003 S11
本网元实现 :融合SMF选择策略
融合SMF选择策略如[表1]所示，与普通PGW选择策略总体一致。有以下两点不同：
MME基于终端能力和签约信息，根据本地选择策略确定是否选择融合SMF。本地选择策略因子如下，选择策略是对这些因子的组合：终端能力：如果UE Network Capability中的N1 mode值为1，则选择融合SMF。签约信息：如果根据签约信息和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC，APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合SMF。终端能力和签约信息：如果UE Network Capability中的N1 mode值为1，并且根据签约信息和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC，APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合SMF。终端能力或签约信息：如果UE Network Capability中的N1 mode值为1，或者根据签约信息和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC以及APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合SMF。不选择融合SMF：对于终端能力或签约信息支持5G的用户，不选择融合SMF。 
当确定选择融合SMF时，根据不同的应用场景，使用表1中的策略因子进行选择。 
 说明： 
当本地策略为“不选择融合SMF”时，MME还可以根据软参786981控制普通PGW无效时，是否选择融合SMF。 
选择策略因子|策略说明|场景
---|---|---
终端能力|基于UE Network Capability中的N1 mode，根据本地策略决策是否选择融合SMF。|具有4/5G能力的终端接入EPC网络。
签约信息|基于签约信息中的Core Network Type Restrictions和APN对应的Interworking-5GS-Indicator，根据本地策略决策是否选择融合SMF。|具有4/5G能力的终端接入EPC网络。
拓扑|SGW和PGW之间的拓扑通过主机名表达。当需要根据拓扑选择SGW和PGW时，按主机名字符从右到左的顺序匹配SGW和PGW的主机名，匹配度最高的说明拓扑最相近。|SGW和PGW合一，或者SGW和PGW路由相近。
有效性|MME根据SGW与PGW间的链路有效性选择SGW/PGW。|PGW链路故障冗余保护，当某个PGW故障时，可以选择其他正常的PGW，实现容灾备份。
优先级|PGW优先级的数值越小，优先级越高，MME优选高优先级的PGW。|PGW间互相进行备份。
权重|MME根据PGW的权重因子，随机选择一个PGW。PGW权重因子的大小，决定其被选择的概率大小。|PGW间负荷分担，网络中PGW的能力不一致，高能力的PGW配置的权重也高，被选择的概率大，达到PGW的负荷均衡。
动态负荷|MME根据与PGW交互时保存的PGW网元级负荷、APN级负荷，以及DNS返回的当前APN解析的PGW的静态权重，共同决定当前APN的PGW的有效负荷（（100-PGW网元动态负荷）%×静态权重×APN级负荷）来进行PGW选择。|PGW动态负荷均衡。
地址解析优先级|MME控制本地Host解析、DNS Server解析、DNS cache解析这三种查询方式的优先级。|DNS系统瘫痪且短时间无法恢复，切换到本地Host解析，快速恢复业务。
融合SMF选择流程
融合SMF选择流程如[图6]所示，与普通PGW选择流程总体一致。有以下两点不同：
MME优先选择具有“nc-smf”标志位的PGW，即融合SMF。 
MME在检测出所有融合SMF均故障时，重选普通PGW。 
图6  融合SMF选择流程图

融合SMF选择流程如下： 
MME根据APN构造FQDN，service parameter为：x-3gpp-pgw:x-s5-gtp+nc-smf和x-3gpp-pgw:x-s8-gtp+nc-smf。根据构造的APN-FQDN，通过DNS查询或者本地解析，获取到PGW列表信息。 
MME从获取的PGW列表中，选择满足S5/S8协议类型且具有"nc-smf"标志位的PGW，即融合SMF。 
MME进行地址有效性检查。从[步骤2]选择的融合SMF列表中剔除无效和不可达的IP地址。
MME进行拓扑选择。如果获取到拓扑关系最邻近的SGW和融合SMF列表，则选择到拓扑最近的SGW和融合SMF，执行[步骤7]；否则，执行[步骤5]。
MME进行优先级和权重选择。根据优先级和权重选择一个融合SMF。 
MME进行子网优先级选择。基于[步骤1]中构造的APN-FQDN获取到本地配置的子网优先级，对融合SMF的每一个IP地址，都给予一个子网优先级值，并从高子网优先级的PGW地址中，根据配置开关选择一个IPv4或IPv6地址。
MME进行节点有效性选择。MME根据SGW与融合SMF间的链路有效性判断GW节点是否有效： 
若GW节点有效，则选定一个融合SMF及IP地址，流程结束。 
若GW节点无效，从步骤3中获取的SGW和融合SMF列表中，根据节点有效性重新选出新的融合SMF及IP地址，流程结束。 
业务流程 :融合SMF选择涉及如下流程： 
附着流程 
UE请求PDN连接流程 
附着流程中的融合SMF选择
图7  附着流程中的融合SMF选择

流程说明如下： 
具有4/5G能力的UE通过eNodeB发送Attach Request消息到MME。 
同系统现有处理，MME继续附着流程，直到向SGW发送Create Session Request消息创建会话。 
MME根据本地选择策略确定选择融合SMF，通过DNS查询或者本地解析进行选择。 
MME向SGW发送Create Session Request消息创建会话，携带选定的融合SMF地址信息。 
SGW向融合SMF发送Create Session Request消息创建会话，融合SMF返回Create Session Response消息。 
SGW返回Create Session Response消息给MME。 
同系统现有处理，MME继续完成后续的附着流程。 
UE请求PDN连接流程中的融合SMF选择
图8  UE请求PDN连接流程中的融合SMF选择

流程说明如下： 
具有4/5G能力的UE通过eNodeB发送PDN Connectivity Request消息到MME，请求建立PDN连接。 
同系统现有处理，MME继续UE请求PDN连接流程，直到向SGW发送Create Session Request消息创建会话。 
MME根据本地选择策略确定选择融合SMF，通过DNS查询或者本地解析进行选择。 
MME向SGW发送Create Session Request消息创建会话，携带选定的融合SMF地址信息。 
SGW向融合SMF发送Create Session Request消息创建会话，融合SMF返回Create Session Response消息。 
SGW返回Create Session Response消息给MME。 
同系统现有处理，MME继续完成后续的UE请求PDN连接流程。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
ZUF-78-19-001 4/5G用户接入EPC|具有4/5G能力的UE接入到EPC网络时，才需要选择融合SMF。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.502（Procedures for the 5G System）|4.11.0a.4 PGW Selection
3GPP TS 29.303（Domain Name System Procedures Stage 3）|5.12.3.2 PGW-C/SMF selection
特性能力 :名称|指标
---|---
EPC APN HOST配置|4096（条）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.20|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目参见下表，只有在License项目显示为“支持”时，MME才支持与5GS的互操作，进而才支持融合SMF选择功能。 
LICENSE项|归属NF|备注
---|---|---
MME支持N26互操作|SGSN&MME|MME部署了N26接口，支持4G和5G间有N26接口互操作
MME支持无N26互操作|SGSN&MME|MME没有部署N26接口，支持4G和5G间无N26接口互操作
对其他网元的要求 :UE|eNodeB|SGW|PGW|SMF|HSS+UDM
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :根据SGW和融合SMF之间的距离远近，合理部署SGW和融合SMF。对合一或邻近的SGW和融合SMF，要将SGW和融合SMF的主机名统一规范命名。 
O&M相关 :命令 :配置项表2  新增配置项配置项命令5GC互操作基本配置SET 5GC INTERWORKINGSHOW 5GC INTERWORKINGPGW地址解析配置ADD EPC APNDEL EPC APNSET EPC APNSHOW EPC APNSGW地址解析配置ADD EPCHOSTDEL EPCHOSTSET EPCHOSTSHOW EPCHOST 
软件参数表3  新增软件参数软件参数ID软件参数名称786981开启"不选择融合的PGW-C+SMF"功能后，如果PGW查询结果中没有有效的PGW，是否选择融合的PGW-C+SMF。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置，可以设置MME根据终端能力和签约信息选择融合SMF的策略，以及选择融合SMF失败后的策略。 
配置前提 :已开启“MME支持N26互操作”或“MME支持无N26互操作”的License功能。 
配置过程 :执行[SET 5GC INTERWORKING]命令，设置互操作模式、MME选择融合SMF的策略，以及MME选择融合SMF失败后的策略。
执行[ADD EPC APN]命令，进行PGW地址解析配置。
执行[ADD EPCHOST]命令，进行SGW地址解析配置。
配置实例 :###### 场景一：融合SMF与SGW分开部署，MME选择融合SMF 
场景说明
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，识别出融合SMF列表，基于优先级和权重选择出一个融合SMF。 
数据规划
配置项|参数|取值
---|---|---
5GC互操作基本配置|互操作模式|WITHN26
支持N26互操作|5GC互操作基本配置|SUPWITHN26
根据终端能力和签约信息选择融合的PGW-C+SMF策略|5GC互操作基本配置|ALLOFTHEM
PGW地址解析配置|APN名称|cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org
主机名|PGW地址解析配置|smf.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
IP地址|PGW地址解析配置|2.2.2.2
支持服务类别|PGW地址解析配置|x-3gpp-pgw
支持协议类型|PGW地址解析配置|"x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf"
支持DT功能|PGW地址解析配置|YES
 说明： 
PGW地址解析配置一个普通PGW和一个融合SMF。仅以融合SMF的数据规划作为示例。 
配置步骤
步骤|说明|操作
---|---|---
1|设置支持N26互操作和当前模式为有N26|SET 5GC INTERWORKING:MODE="WITHN26",SUPWITHN26="SUPWITHN26"
2|设置根据终端能力和签约信息选择融合的PGW-C+SMF策略为“终端能力和签约信息”|SET 5GC INTERWORKING:PGWCSMFSELECTPOLICY="ALLOFTHEM"
3|设置PGW地址解析|配置融合SMF地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="smf.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="2.2.2.2",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf",DTSPRT="YES"配置普通PGW地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp",DTSPRT="YES"
###### 场景二：融合SMF与SGW合一部署，MME选择融合SMF 
场景说明
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，识别出融合SMF列表，根据SGW和融合SMF的合一或邻近关系，选出合一或拓扑最近的一对或多对SGW/PGW-C+SMF，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW-C+SMF。 
数据规划
配置项|参数|取值
---|---|---
5GC互操作基本配置|互操作模式|WITHN26
支持N26互操作|5GC互操作基本配置|SUPWITHN26
根据终端能力和签约信息选择融合的PGW-C+SMF策略|5GC互操作基本配置|ALLOFTHEM
PGW地址解析配置|APN名称|cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org
主机名|PGW地址解析配置|smf2.saegw3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
IP地址|PGW地址解析配置|3.3.3.3
支持服务类别|PGW地址解析配置|x-3gpp-pgw
支持协议类型|PGW地址解析配置|"x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf"
支持DT功能|PGW地址解析配置|YES
SGW地址解析配置|逻辑名称|tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org
支持服务类别|SGW地址解析配置|x-3gpp-sgw
主机名|SGW地址解析配置|sgw1.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
IP地址|SGW地址解析配置|11.11.11.11
支持协议类型|SGW地址解析配置|x-s5-gtp
优先级|SGW地址解析配置|10
 说明： 
PGW地址解析配置一个普通PGW和两个融合SMF的记录。仅以融合SMF的数据规划作为示例。 
SGW地址解析配置三条记录。仅以融合SGW1的数据规划作为示例。 
配置步骤
步骤|说明|操作
---|---|---
1|设置支持N26互操作和当前模式为有N26|SET 5GC INTERWORKING:MODE="WITHN26",SUPWITHN26="SUPWITHN26"
2|设置根据终端能力和签约信息选择融合的PGW-C+SMF策略为“终端能力和签约信息”|SET 5GC INTERWORKING:PGWCSMFSELECTPOLICY="ALLOFTHEM"
3|设置PGW地址解析|配置融合SMF2地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="smf2.saegw3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="3.3.3.3",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf",DTSPRT="YES"配置融合SMF1地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="smf1.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="2.2.2.2",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf",DTSPRT="YES"配置普通PGW地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp",DTSPRT="YES"
4|设置SGW地址解析|配置融合SGW1地址解析。ADD EPCHOST:NAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw1.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="11.11.11.11",PROTOCOL="x-s5-gtp",NAPTRORDER=10配置融合SGW2地址解析。ADD EPCHOST:NAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw2.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="22.22.22.22",PROTOCOL="x-s5-gtp",NAPTRORDER=50配置融合SGW3地址解析。ADD EPCHOST:NAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw3.saegw3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="33.33.33.33",PROTOCOL="x-s5-gtp",NAPTRORDER=100
###### 场景三：融合SMF与SGW分开部署，PGW-C+SMF均故障，MME选择普通PGW 
场景说明
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，MME检测出所有的融合SMF均故障，在普通PGW列表中基于优先级和权重选择出一个普通PGW。 
数据规划
配置项|参数|取值
---|---|---
5GC互操作基本配置|互操作模式|WITHN26
支持N26互操作|5GC互操作基本配置|SUPWITHN26
根据终端能力和签约信息选择融合的PGW-C+SMF策略|5GC互操作基本配置|ALLOFTHEM
选择融合SMF失败后的策略|5GC互操作基本配置|PGW
PGW地址解析配置|APN名称|cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org
主机名|PGW地址解析配置|smf.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
IP地址|PGW地址解析配置|2.2.2.2
支持服务类别|PGW地址解析配置|x-3gpp-pgw
支持协议类型|PGW地址解析配置|"x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf"
支持DT功能|PGW地址解析配置|YES
 说明： 
PGW地址解析配置一个普通PGW和一个融合SMF的记录。仅以融合SMF的数据规划作为示例。 
配置步骤
步骤|说明|操作
---|---|---
1|设置支持N26互操作和当前模式为有N26|SET 5GC INTERWORKING:MODE="WITHN26",SUPWITHN26="SUPWITHN26"
2|设置根据终端能力和签约信息选择融合的PGW-C+SMF策略为“终端能力和签约信息”|SET 5GC INTERWORKING:PGWCSMFSELECTPOLICY="ALLOFTHEM"
3|设置选择融合SMF失败后的策略为“优选普通PGW”|SET 5GC INTERWORKING:PLYAFSELSMFFAIL="PGW"
4|设置PGW地址解析|配置融合SMF地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="smf.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="2.2.2.2",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf",DTSPRT="YES"配置普通PGW地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp",DTSPRT="YES"
###### 场景四：融合SMF与SGW合一部署，合一SGW/PGW-C+SMF均故障，MME选择普通PGW 
场景说明
具有4/5G能力的终端接入EPC网络，MME查询到融合SMF和普通PGW列表，MME检测出所有的SGW/PGW-C+SMF均故障，在普通PGW列表中根据SGW和PGW的合一或邻近关系，选出合一或拓扑最近的一对或多对SGW/PGW，如果是多对，则MME再根据SGW的优先级和权重选出一对SGW/PGW。 
数据规划
配置项|参数|取值
---|---|---
5GC互操作基本配置|互操作模式|WITHN26
支持N26互操作|5GC互操作基本配置|SUPWITHN26
根据终端能力和签约信息选择融合的PGW-C+SMF策略|5GC互操作基本配置|ALLOFTHEM
选择融合SMF失败后的策略|5GC互操作基本配置|PGW
PGW地址解析配置|APN名称|cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org
主机名|PGW地址解析配置|smf2.saegw3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
IP地址|PGW地址解析配置|3.3.3.3
支持服务类别|PGW地址解析配置|x-3gpp-pgw
支持协议类型|PGW地址解析配置|"x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf"
支持DT功能|PGW地址解析配置|YES
SGW地址解析配置|逻辑名称|tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org
支持服务类别|SGW地址解析配置|x-3gpp-sgw
主机名|SGW地址解析配置|sgw1.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
IP地址|SGW地址解析配置|11.11.11.11
支持协议类型|SGW地址解析配置|x-s5-gtp
优先级|SGW地址解析配置|10
 说明： 
PGW地址解析配置两个普通PGW和一个融合SMF的记录。仅以融合SMF的数据规划作为示例。 
SGW地址解析配置三条记录。仅以融合SGW1的数据规划作为示例。 
配置步骤
步骤|说明|操作
---|---|---
1|设置支持N26互操作和当前模式为有N26|SET 5GC INTERWORKING:MODE="WITHN26",SUPWITHN26="SUPWITHN26"
2|设置根据终端能力和签约信息选择融合的PGW-C+SMF策略为“终端能力和签约信息”|SET 5GC INTERWORKING:PGWCSMFSELECTPOLICY="ALLOFTHEM"
3|设置选择融合SMF失败后的策略为“优选普通PGW”|SET 5GC INTERWORKING:PLYAFSELSMFFAIL="PGW"
4|设置PGW地址解析|配置融合SMF地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="smf.saegw3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="3.3.3.3",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"&"x-s5-gtp+nc-smf"&"x-s8-gtp+nc-smf",DTSPRT="YES"配置普通PGW2地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw2.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="2.2.2.2",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp",DTSPRT="YES"配置普通PGW1地址解析。ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw1.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp",DTSPRT="YES"
5|设置SGW地址解析|配置融合SGW1地址解析。ADD EPCHOST:NAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw1.saegw1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="11.11.11.11",PROTOCOL="x-s5-gtp",NAPTRORDER=10配置融合SGW2地址解析。ADD EPCHOST:NAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw2.saegw2.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="22.22.22.22",PROTOCOL="x-s5-gtp",NAPTRORDER=50配置融合SGW3地址解析。ADD EPCHOST:NAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw3.saegw3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="33.33.33.33",PROTOCOL="x-s5-gtp",NAPTRORDER=100
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|融合SMF与SGW分开部署，MME选择融合SMF
---|---
测试目的|验证融合SMF与SGW分开部署时，MME可以选到融合SMF。
预置条件|MME支持N26互操作license打开。设置支持N26互操作，且当前模式为有N26。设置“根据终端能力和签约信息选择融合的PGW-C+SMF策略”为“终端能力和签约信息”。PGW地址解析配置中，配置一个普通PGW和一个融合SMF，普通PGW的地址为1.1.1.1，融合SMF的地址为2.2.2.2。
测试过程|5G用户附着接入EPC网络，UE网络能力支持N1 mode，UE请求的APN在HSS上签约了Interworking-5GS-Indicator。
通过准则|用户选择地址为2.2.2.2的融合SMF建立PDN连接。
测试结果|–
测试项目|融合SMF与SGW合一部署，MME选择融合SMF
---|---
测试目的|验证融合SMF与SGW合一部署时，MME可以选到融合SMF。
预置条件|MME支持N26互操作license打开。设置支持N26互操作，且当前模式为有N26。设置“根据终端能力和签约信息选择融合的PGW-C+SMF策”略为“终端能力和签约信息”。PGW地址解析配置中，配置一个普通PGW和两个融合SMF，普通PGW的地址为1.1.1.1，融合SMF1的地址为2.2.2.2，融合SMF2的地址为3.3.3.3。SGW地址解析配置中，配置SGW1地址为11.11.11.11，SGW2的地址为22.22.22.22，SGW3的地址为33.33.33.33。设置SGW1与PGW为融合，SGW2与SMF1为融合，SGW3与SMF2为融合。其中SGW1的NAPTR优先级为10，SGW2的优先级为50，SGW3的优先级为100。
测试过程|5G用户附着接入EPC网络，UE网络能力支持N1 mode，UE请求的APN在HSS上签约了Interworking-5GS-Indicator。
通过准则|用户选择地址为22.22.22.22的SGW2和地址为2.2.2.2的融合SMF1建立PDN连接。
测试结果|–
测试项目|融合SMF与SGW分开部署，PGW-C+SMF均故障，MME选择普通PGW
---|---
测试目的|验证融合SMF与SGW分开部署时，当融合的PGW-C+SMF故障时，MME可以选到普通PGW。
预置条件|MME支持N26互操作license打开。设置支持N26互操作且当前模式为有N26。设置“根据终端能力和签约信息选择融合的PGW-C+SMF策略”为“终端能力和签约信息”。设置选择融合SMF失败后的策略为“优选普通PGW”。PGW地址解析配置中，配置一个普通PGW和一个融合SMF，普通PGW的地址为1.1.1.1，融合SMF的地址为2.2.2.2，设置SMF地址2.2.2.2为不可达。
测试过程|5G用户附着接入EPC网络，UE网络能力支持N1 mode，UE请求的APN在HSS上签约了Interworking-5GS-Indicator。
通过准则|用户选择地址为1.1.1.1的普通PGW建立PDN连接。
测试结果|–
测试项目|融合SMF与SGW合一部署，合一SGW/PGW-C+SMF均故障，MME选择普通PGW
---|---
测试目的|验证融合SMF与SGW合一部署时，当合一SGW/PGW-C+SMF故障时，MME可以选到普通SGW/PGW。
预置条件|MME支持N26互操作license打开。设置支持N26互操作且当前模式为有N26。设置“根据终端能力和签约信息选择融合的PGW-C+SMF策略”为“终端能力和签约信息”。设置选择融合SMF失败后的策略为“优选普通PGW”。PGW地址解析配置中，配置两个普通PGW和一个融合SMF，普通PGW1的地址为1.1.1.1，普通PGW2的地址为2.2.2.2，融合SMF的地址为3.3.3.3。设置SMF与SGW3的地址为不可达。SGW地址解析配置中，配置SGW1地址为11.11.11.11，SGW2的地址为22.22.22.22，SGW3的地址为33.33.33.33；设置SGW1与PGW1为融合，SGW2与PGW2为融合，SGW3与SMF为融合。其中SGW1的NAPTR优先级为10，SGW2的优先级为50，SGW3的优先级为100。
测试过程|5G用户附着接入EPC网络，UE网络能力支持N1 mode，UE请求的APN在HSS上签约了Interworking-5GS-Indicator。
通过准则|用户选择地址为11.11.11.11的SGW1和地址为1.1.1.1的普通PGW1建立PDN连接。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## 5GS 
5G System5G系统
## CSFB 
Circuit Switched Fallback电路域回落
DNS :Domain Name Server域名服务器
EPC :Evolved Packet Core演进的分组核心网
## LAI 
Location Area Identity位置区标识
MME :Mobility Management Entity移动管理实体
MSC :Mobile Switching Center移动交换中心
PDN :Packet Data Network分组数据网
SGW :Serving Gateway服务网关
SMF :Session Management Function会话管理功能
## SRVCC 
Single Radio Voice Call Continuity单射频语音呼叫连续性
Single Radio Voice Call Continuity双模单待无线语音呼叫连续性
## VLR 
Visitor Location Register拜访位置寄存器
eNodeB :Evolved NodeB演进的NodeB
# ZUF-78-06 MME POOL 
概述 :功能描述 :MME Pool区域是指UE在其间移动不需要改变服务MME的区域，一个MME Pool区域内有两个或多个对等的MME，MME池区是由多个TA汇聚，Pool区域内的每个eNB都与所有的MME互联。
功能特性简介 :针对MME POOL的应用特点和应用场景，核心网为满足容灾备份的要求，提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
MME池区|支持多个MME组成POOL，用户在POOL内移动无需改变MME，减少了局间信令交互，同时POOL内MME具有相互容灾的能力。POOL内的MME具有不同的GUMMEI和权重，在S1 Setup流程中MME将GUMMEI和权重下发给eNobeB，eNobeB通过GUMMEI和权重选择MME。当某个MME故障时，eNodeB可选择其他POOL内的可用MME。|ZUF-78-06-001 MME池区
MME支持负荷重平衡功能|通过负荷重平衡功能，可以在MME需要升级或处理能力降低时，将其注册的用户迁移到其他MME，避免用户下线。MME可以支持多种负荷卸载方式，包括有：按用户比例卸载。按用户数卸载。按指定eNodeB卸载。按指定IMSI号段卸载。按指定MSISDN号段卸载。|ZUF-78-06-002 MME支持负荷重平衡功能
优选COMBO节点|在COMBO局组网时，通过优选COMBO节点功能，用户在SGSN和MME下跨RAT移动，可以减少局间信令，降低业务时延。用户进行附着、TAU/RAU或切换、RIM业务、SUSPEND业务时，RNC或eNodeB选择和老局同COMBO节点的SGSN或MME。|ZUF-78-06-003 优选COMBO节点
指定POOL中EPC网元节点拨测|EPC网元在开局、升级或者是割接过程中，需要通过拨测的方法来实际验证一下网元运行是否正常；另外在定位故障时，也需要指定网元节点或路径进行拨测以排查问题。当前国内外各个运营商都在加快LTE网络的建设和部署，所以各种开局、升级、割接的频度也越来越高，对于EPC网元拨测的需求也越来越迫切。MME通过EMS或OMM支持以下功能：单用户指定目标MME卸载。用户附着时指定PGW/SGW。|ZUF-78-06-004 指定POOL中EPC网元节点拨测
## ZUF-78-06-001 MME池区 
特性描述 :特性描述 :术语 :术语|含义
---|---
MME池区|MME池区是指UE在其间移动不需要改变服务MME的区域。一个MME池区内有一个或多个对等的MME。MME池区是由多个TA汇聚。MME池区间可以有交迭。
描述 :定义 :MME Pool区域是指UE在其间移动不需要改变服务MME的区域，一个MME
Pool区域内有一个或多个对等的MME，MME池区是由多个TA汇聚，Pool区域内的每个eNB都与所有的MME互联，如[图1]所示。
图1  MME Pool组网图

MME Pool的主要优点在于： 
由于UE在MME Pool内移动时，通常不需要切换MME节点，所以可以有效减少系统间的信令交互。 
可以有效实现MME网元级的容灾和负荷分担。 
MME Pool的功能主要包括三部分： 
MME Pool内负荷分担功能，使用户可以较均衡的分布在各个MME上，保证了在MME Pool内各个MME上的负荷和其处理能力的一致性。 
MME负荷重平衡功能，通过将某个MME的全部或部分特定用户迁移到Pool内其他MME的方式，以减少该MME下用户的数量，从而减少该MME升级或其它情况下对用户业务的影响。 
MME容灾功能，当Pool内某MME不可用后，Pool内其他MME能够支持故障MME下用户发起的业务。 
背景知识 :Pool功能最初是在2G/3G时代引入的。移动网络支持Pool功能后，一个RAN节点连接到多个SGSN节点，由RAN实现节点选择和路由功能。SGSN在分配新P-TMSI给用户时，包含了本SGSN节点的标识NRI，用户通过RAN节点接入到SGSN时，RAN从P-TMSI/TLLI中分离出NRI，根据NRI将信令消息路由到正确的SGSN节点上。
对于EPS网络来说，由于在网络设计之初就考虑的对Pool的必然支持，所以对Pool功能的支持又有了进一步的优化和增强，MME
Pool与SGSN Pool关键技术比较参见[表1]。
关键技术|MME Pool|SGSN Pool
---|---|---
节点标识|用户临时标识GUTI包含有完整的MME标识GUMMEI：<GUTI> = <GUMMEI><M-TMSI>|从P-TMSI中抠出4～10bit作为池内SGSN的特殊标识。缺点：NRI长度会影响用户标识的分配能力，NRI不是SGSN全局唯一的标识。
NNSF节点寻址方式|eNodeB从MME建立动态偶联，通过S1消息获取GUMMEI和权重，无需静态配置。|BSC/RNC需要静态配置NRI和SGSN的对应关系。需要静态配置SGSN的权重。缺点：静态配置增加运维工作，且各个RAN节点的一致性需要人为保证。
重平衡方式|通过特殊原因值的S1释放即可立即触发。UE通过不携带MME节点信息给eNodeB的方式，指示eNodeB重选。MME新局无特殊实现，根据UE上报的old GUTI可寻址老局。|需要增加NULL-NRI的规划和Non-broadcast RAI的规划。需要重新分配带NULL-NRI的P-TMSI和Non-broadcastRAI，以及很短的路由更新周期。需要利用周期性RAU触发。SGSN新局需要根据Non-broadcastRAI寻址老局。缺点：复杂，流程特殊，影响大。
应用场景 :###### MME POOL组建 
MME POOL是EPS网络具备的基本功能。通常情况下，一个无线连续覆盖的区域，比如多个邻近地区/城市组成的大区，或者是大城市本地组网，都可以组建MME
POOL。 
以三个MME组建MME POOL为例，组网图如[图2]所示。
图2  MME Pool内有三个MME的组网图

###### MME POOL的运维 
MME POOL通过权重修改和负荷重平衡（卸载），可应用于对MME
POOL组网和节点变更的维护，包括MME POOL内MME数目的变更、部分MME扩容、部分网络软硬件升级的场景。 
MME POOL内MME数目的变更需要修改、设置MME的权重，并通过卸载加快用户的迁移和负荷到达预期权重。以新增MME为例，原来Pool中两个MME的权重值分别为50和100，新增MME的权重为50，新增MME的权重值将下发到Pool内所有的eNB，如图3所示。图3  MME Pool内新增节点 
MME POOL内部分MME扩容需要修改、设置MME的权重，通过卸载加快用户的迁移和负荷到达预期权重。以MME扩容为例，原来Pool中三个MME的权重值分别为50、100和50，将第三个MME的权重由50调整为100，调整后的权重值将下发到Pool内所有的eNB，如图4所示。图4  MME Pool内节点扩容 
MME POOL内部分网络软硬件升级通过负荷重平衡的方式将受影响部分的用户迁移到其他MME，减少对用户业务的影响。以MME1升级为例，将MME的权重调整为0，并下发到Pool内所有的eNB。在MME1上执行负荷重平衡功能，将MME1的所有用户迁移到MME2和MME3，如图5所示。图5  MME Pool内负荷卸载 
MME Pool内MME拨测为了验证MME Pool内所有MME均能正常工作，可使用一个测试用户在Pool内依次接入所有MME，并进行业务流程测试。通过“单用户指定MME卸载”功能可以方便快速的将测试用户从一个测试完毕的MME迁移到下一个待测试的MME。 
客户收益 :受益方|受益描述
---|---
运营商|支持MME POOL功能，可以有效减少系统间的信令交互，实现MME网元级的容灾和负荷分担，保证整个系统的稳定和高效。MME POOL的负荷重平衡功能，可以在一些特殊情况，如MME进行软硬件升级，减少对用户业务的影响，从而提高用户对使用EPS网络的满意度。MME POOL内可以更加方便规划TA List，以减少UE发起的TAU，减少空口资源。
移动用户|信令减少降低终端的电力消耗。
实现原理 :涉及的网元 :MME网元POOL功能需要UE、eNodeB、MME的共同配合，网元作用参见[表2]。
网元|作用
---|---
UE|将当前服务MME的信息带给eNodeB，以便eNodeB能够将信令路由到当前用户服务的MME。根据RRC连接释放的原因值，触发TAU流程。
eNodeB|实现MME选择功能，即根据UE提供的信息选择UE当前服务的MME。在UE没有提供服务MME信息、或服务MME不可达时，根据MMEPOOL内MME的权重因子，选择MME。
MME|向eNodeB下发本MME的GUMMEI和权重因子。发起负荷重平衡过程。
业务流程 :Served GUMMEI及权重的配置和下发
将MME的标识GUMMEI和权重因子，并通过S1口消息下发给eNodeB，由eNodeB实现MME选择路由，完成负荷分担的先决条件。 
当eNodeB最初发起S1连接建立过程，与MME建立连接时，MME就在回复的响应中下发GUMMEI和权重因子。在后续MME配置的GUMMEI和/或权重因子发生变更时，MME使用MME配置更新流程通知eNodeB。 
S1连接建立过程
S1连接建立过程如[图6]所示。
图6  S1连接建立过程

流程说明： 
MME收到eNodeB 发送的S1 SETUP REQUEST消息。 
MME根据配置获取Served GUMMEI以及Relative MME Capacity值，向eNodeB发送S1
Setup Response消息，其中携带Served GUMMEI和Relative MME Capacity；eNodeB保存当前MME的GUMMEI和权重因子。 
MME配置更新过程
MME配置更新过程如[图7]所示。
图7  MME配置更新过程

流程说明： 
配置中MME网元的Served GUMMEI或Relative MME Capacity发生变化，MME向全部与本局已建立S1连接的eNodeB平滑发送MME
Configuration Update消息，其中携带了更新后的Served GUMMEI或Relative MME Capacity。 
eNodeB更新MME的Relative MME Capacity，向MME回MME Configuration Update
Acknowledge消息。 
eNodeB选择MME
在UE的S1口连接（S1AP上下文）尚未建立时，eNodeB需要根据UE提供的MME的标识信息，选择特定的MME，将消息发送到该MME，建立S1口连接。当S1口连接建立好以后，后继消息可使用当前S1连接发送到连接建立的同一个MME。 
初始UE消息过程
初始UE消息过程如[图8]所示。图8  初始UE消息过程

流程说明： 
UE向eNB发送RRC消息，携带NAS消息以及RRC参数。如果RRC参数中有S-TMSI或者Old GUMMEI，则eNodeB根据Old GUMMEI，在POOL内可用的MME中进行查询： 
如果找到该MME，则选择该MME。 
如果找不到，或者没有携带S-TMSI或者Old GUMMEI，则eNodeB根据POOL内可用的各个MME的权重因子，轮选一个MME。 
eNodeB向选择的MME发送S1AP的Initial UE Message。 
跨局切换时按照负荷分担原则选择MME过程
跨局切换时按照负荷分担原则选择MME过程如[图9]所示。
图9  跨局切换时按照负荷分担原则选择MME过程

下面只描述和目的MME选择相关的部分： 
流程2中，源MME收到eNodeB的Handover Required消息，根据Target eNodeB ID，确定是跨局切换，根据目的TAI，选择到了一组目的MME。 
流程3中，源MME先把源MME和目的MME之间链路异常的目的MME剔除。根据配置的各个目的MME的优先级，选择优先级高的目的MME，如果多个目的MME都有高优先级，则从高优先级的目的MME中随机选择其中一个目的MME。继续执行切换的后续流程。 
MME的负荷重平衡
MME的负荷重平衡的过程如[图10]所示。
图10  MME的负荷重平衡过程

流程说明： 
Old MME决定要发起对UE的负荷重平衡过程，向eNB发起S1连接释放，携带特定的原因值“load balancing
TAU required”。 
eNodeB发起RRC释放，携带原因值“load balancing TAU required”。 
eNB向MME返回S1释放完成响应消息。 
UE收到释放后，立即发起TAU流程，同时发给eNodeB在RRC消息中不携带S-TMSI和GUMMEI。 
因为没有指定的MME信息，eNodeB根据POOL内可用的各个MME的权重因子，轮选一个MME，向MME发送S1AP的Initial
UE Message消息，携带UE的TAU请求消息。 
 说明： 
S1释放发起的时机： 
处于流程处理中的UE，MME待流程结束后，发起S1释放流程。 
UE处于空闲态，寻呼UE，UE响应寻呼后，发起发起S1释放流程。 
OMM发起的MME负荷重平衡功能
由管理员在OMM上发起MME的负荷重平衡功能，是MME
POOL运维的重要工具，通过负荷重平衡功能，可以卸载部分或全部UE，使UE迁移到其他MME上。主要的功能包括： 
负荷重平衡 
负荷重平衡撤销 
负荷重平衡进度读取 
负荷重平衡过程
由管理员在OMM上发起MME的负荷重平衡，可以有多种不同的方式选择： 
指定的USMP上进行全部用户的卸载 
全局指定比例用户卸载 
全部用户的卸载 
按eNodeB进行负荷卸载 
按IMSI/MSISDN号码进行负荷卸载 
负荷重平衡的流程参见[图11]。
图11  OMM发起的MME负荷重平衡的流程

流程说明： 
运营商根据系统要求设置MME负载重平衡卸载优化策略，包括：卸载优化开关、令牌控制周期、投放策略、业务突发系数。然后从OMM发起负荷卸载过程，MME收到了OMM发送的负荷卸载消息，通知进行负荷卸载及策略。 
MME进入负荷重平衡状态，并给OMM回负荷重平衡响应消息，结果为接受。 
MME发送负荷重平衡告警通知给OMM。 
MME开始进行负荷卸载，卸载分为如下三个阶段。 
卸载预处理阶段：MME在设置的预处理时间范围内，等待UE主动发起附着、跟踪区更新、业务请求流程，在流程结束后，对UE发起S1连接释放进行卸载。卸载预处理阶段，MME根据卸载步长设置令牌控制周期内的卸载门限，在控制周期内卸载数量超过此门限，MME不再进行卸载，直到下个控制周期开始。 
周期性扫描卸载阶段：预处理时间结束后，MME周期性扫描需要卸载的UE，对UE发起卸载。如果UE处于某个业务流程处理中，则待流程处理完成后，对UE进行卸载。如果UE处于空闲态，寻呼UE，UE响应寻呼后，对UE进行卸载。否则直接对UE发起卸载。周期性扫描卸载阶段，MME根据卸载步长设置令牌控制周期内的卸载门限，在控制周期内卸载数量超过此门限，MME不再进行卸载，直到下个控制周期开始。 
完成阶段：进入下一步处理。 
MME检查需要卸载的用户都已经卸载，或者已经达到重平衡的最大保护时长，则结束卸载，进入正常工作状态。周期性检查本板卸载是否结束。 
MME发送负荷重平衡成功结束告警通知。 
负荷重平衡撤销过程
负荷重平衡撤销过程如[图12]所示。
图12  负荷重平衡撤销过程

流程说明： 
管理员决定发起负荷重平衡撤销过程，在OMM上向MME发送负荷重平衡撤销命令。 
MME设置为处于普通工作状态，清除负荷重平衡定时器，如果负荷重平衡预处理保护定时器有效，也清除负荷重平衡预处理保护定时器。 
MME向OMM回负荷重平衡撤销响应消息，结果为接受。 
MME发送取消MME负荷重平衡告警通知。 
负荷重平衡进度读取过程
负荷重平衡进度读取过程如[图13]所示。
图13  负荷重平衡进度读取过程

流程说明： 
OMM定时（1分钟）向MME发送负荷重平衡报告请求。 
MME向OMM发送负荷重平衡报告，包括负荷重平衡结束标志、当前LTE用户数、当前LTE用户数占SMP用户上下文容量的比例信息。 
用户指定迁移到POOL内某个MME
通常情况下在进行MME负荷重平衡时，对MME进行负荷卸载的过程中，为了使得eNodeB在轮选时，不再重选回负荷卸载的MME，需要将该MME的权重调为0；待负荷卸载结束后，再根据实际需要，将该MME的权重设置为合理的取值。 
如果需要将用户迁移到Pool内指定的MME，则需要为这些目标MME设置合理的权重，而将其他非目标MME的权重值调整为0，以达到批量用户迁移到指定MME的目的。 
单用户指定MME卸载
主要用于MME拨测，通过“单用户指定MME卸载”功能可以方便快速的将测试用户从一个测试完毕的MME迁移到下一个待测试的MME。单用户指定MME卸载流程如[图14]所示。
图14  单用户指定MME卸载流程

流程说明： 
MME通过动态管理命令指定用户IMSI及目标MME的GUMMEI，触发单用户在指定MME上卸载。 
如果用户处于ECM-IDLE态，需要对用户发起寻呼流程，触发用户进入ECM-CONNECTED状态。 
MME触发GUTI重分配流程，携带指定的GUMMEI。 
UE返回GUTI重分配完成消息。 
MME对用户发起Detach流程，并携带re-attach required指示。 
UE接受MME的分离流程。 
MME和eNodeB之间S1释放。 
UE根据分离请求中的re-attach required指示，使用最近一次GUTI重分配流程分配的GUTI，发起附着流程。 
eNodeB根据GUMMEI解析出对应的MME，并向该MME转发附着请求。用户在目标MME上附着成功。 
负荷重平衡过程详细信息的查询
负荷重平衡过程详细信息的查询过程如[图15]所示。
图15  负荷重平衡过程详细信息的查询过程

流程说明： 
OMM定时（如：5分钟）向MME发送负荷重平衡详细信息报告请求。 
MME向OMM发送负荷重平衡详细信息报告，包括：卸载初期总用户数、UE触发卸载用户数、扫描卸载用户数、用户活动次数等信息。 
负荷重平衡用户卸载过程
负荷重平衡用户卸载过程如[图16]所示。
图16  负荷重平衡用户卸载过程

流程说明： 
启动负荷重平衡卸载优化，从OMM发起负荷重平衡过程，MME启动令牌桶方式控制卸载速率， 以固定速率向桶内投放令牌。 
MME收到UE的附着、TAU、业务请求 或者周期性扫描卸载时，触发负荷卸载前，首先获取卸载令牌。 
UE活动卸载和扫描卸载时，在获取到卸载令牌后，MME对用户进行卸载。 
如果卸载时，未获取到卸载令牌，则不进行卸载。 
当卸载令牌控制周期结束后，清空剩余令牌，进入下个控制周期。 
系统影响 :MME网元支持MME POOL对性能基本无影响。MME POOL功能可减少系统间信令，提升MME的处理能力。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
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
特性能力 :MME POOL功能不会改变MME对接入用户数和承载的支持能力。 
MME最大支持65535个eNodeB接入，最大管理65535个TA。 
一个MME池中最多255个MME（按协议规定，POOL内MME的唯一标识MME CODE为一个字节）。 
可获得性 :对其他网元的要求 :MME网元POOL功能特性需要MME、eNodeB 以及UE配合完成。 
工程规划要求 :MMEGI规划要求
按协议要求，不同的MME POOL需要规划不同的MMEGI；同一个MME POOL内使用同一个MMEGI。 
按协议要求，MMEGI的规划不能和现网中2/3G的LAC重复。如果重复将会造成2/3G与LTE之间跨RAT的接入失败。 
MMEC规划要求
MMEC的规划要求主要包括以下内容： 
LTE到2/3G 网络RAU，RNC根据由MMEC映射的NRI选择SGSN。 
2/3G到LTE网络TAU，eNodeB根据由LAI和NRI映射的GUMMEI选择MME。 
SGSN和MME独立POOL，跨RAT要求随机选择，所以要求MMEC转换后的NRI值不要和现网NRI重复，推荐MMEC转换之后截取长度是SGSN
POOL的NULL NRI值，这样RNC找不到NRI对应的SGSN就会轮选，同时也保证了NRI转换后的MMEC不会和现网的MMEC重复，所以eNB找不到对应的MME也会轮选。 
SGSN/MME Combo POOL，跨RAT要求选择同一Combo节点，所以要求Combo的MME的MMEC转换后的NRI值只能是同节点Combo
SGSN的；同时需要把所有根据SGSN下LAI和NRI映射的GUMMEI都带给eNB。此种情况并不需要为本局配置多个GUMMEI。 
例如，现网NRI长度是4，SGSN NRI值为3，4，5，MMEC的高4个比特为NRI，低4个比特取值不确定，MMEC值是一个范围，NRI与MMEC的映射关系参见[表3]。
NRI|NRI长度|23-16bits值|转换MMEC值范围
---|---|---|---
3|4|0011 xxxx|48-63
4|4|0100 xxxx|64-79
5|4|0101 xxxx|80-95
如果需要随机选择（SGSN和MME独立Pool），MMEC可规划的范围是0～47和96～255。 
如果需要同节点选择（SGSN/MME Combo Pool），比如NRI=3的SGSN的Combo MME的MMEC可规划为48～63，同时需要将所有MMGI=LAC和MMEC48～63的GUMMEI带给eNB。 
 说明： 
对于SGSN/MME Combo POOL，如果要求跨RAT要求选择同一Combo节点，建议POOL内所有节点都是Combo局，且每个节点SGSN的权重和MME的权重相同，以保证POOL内负荷均衡。 
MME权重规划要求
MME权重是和MME的处理能力相关的，需要按照单个MME处理能力在POOL总处理能力的占比来计算权重，比如POOL中存在3个MME节点，分别能够处理200万、200万、100万用户的业务量，即占比为40%、40%、20%，那么权重就可以配置为40、40、20。 
O&M相关 :命令 :与Pool特性相关的配置项参见[表4]。
配置项|命令
---|---
MME卸载优化配置|SET MME UNLOAD OPT
SHOW MME UNLOAD OPT|MME卸载优化配置
设置负荷重平衡请求|EXEC REBALANCE
停止负荷重平衡|CANCEL REBALANCE
查询负荷重平衡状态|SHOW REBALANCESTATE
配置单用户指定MME卸载|UNLOAD MME USER
MME负荷重平衡信息查询|SHOW MME REBALANCE PROC
性能统计 :与Pool特性相关的性能统计参见[表5]。
计数器类型|计数器名称
---|---
用户数测量|C431000001 EPS平均附着用户数
承载数测量|C431010003 激活态的默认承载平均数
承载激活流程测量|C430070009 专有承载激活成功次数
寻呼流程测量|C430040002 EPS寻呼成功次数
告警和通知 :与Pool特性相关告警和通知参见[表6]。
告警和通知
---
2114060417 开始MME负荷重平衡通知
2114060418 取消MME负荷重平衡通知
2114060419 MME负荷重平衡成功结束通知
2114060420 MME负荷重平衡流程失败通知
特性配置 :特性配置 :配置前提 :待组POOL的每个MME与所有eNB地址互设正确，偶联建立，通讯正常。 
待组POOL MMEs与核心网侧其余网元，如xGW、HSS、MSC等通讯正常，DNS上配置关于TA到MME/SGW解析，GUMMEI到MME的解析，APN到xGW解析正确。 
规划好POOL中涉及到的MME数目以及POOL中关键参数值，MME GROUPID、MMENAME、MMECODE、MMEWEIGHT，具体要求参见可获得性。 
配置过程 :组建MME POOL。 
MME POOL新建过程只需设置每个MME节点上的本地移动数据即可。使用[SET COMBOCFG]命令，配置MME本地移动数据。
MME POOL中新增一个MME节点。 
新增的MME 节点需要对接现有MME POOL对接的所有外围网元，如eNB、HSS、xGW、MSC等，这些基本流程完成的情况下，需要按照如下步骤设置MME节点参数： 
设置新增MME节点本地移动数据，命令为SET COMBOCFG。 
如果需要MME POOL（包括新增MME）中所有MME短时间内达到负荷平衡状态，可以执行本操作，将POOL中原有MME的MME
WEIGHT设为0，并卸载一定比例的用户到新增的MME上。使用命令EXEC REBALANCE负荷重平衡请求。  
通过网管命令SHOW MMEUSER STATS来查询新增MME上接入的用户数，如果新增的MME上的用户数达到规划的状态，且通过命令SHOW REBALANCESTATE查询负荷重平衡的MME已经负荷重平衡结束。此时将原有MME的MME WEIGHT值修改为原有值。 
MME POOL中删除一个MME节点。 
设置待删除MME节点本地移动数据，命令为[SET COMBOCFG]，这里修改MME WEIGHT为0，禁止新用户接入该局。
负荷重平衡该局上所有用户，使用命令[EXEC REBALANCE]负荷重平衡请求。
通过命令[SHOW REBALANCESTATE]查询MME节点负荷重平衡状态。
如果状态提示为：系统没有处于重平衡状态，说明MME已经重平衡结束。通过命令[SHOW MMEUSER
STATS]查询用户数为0。
MME POOL中扩容某个MME节点。 
按照步骤3中的操作。将该MME上用户全部卸载，并禁止用户接入。 
增加物理单板，增加模块，配置模块负荷分担等，对MME进行扩容。 
使用命令[SET COMBOCFG]设置MME节点的本地移动参数，其中MME WEIGHT为扩容后计算的值。
MME POOL内MME拨测。 
主要是实现了“单用户指定MME卸载”功能，用于MME拨测时方便快速的将测试用户从一个测试完毕的MME迁移到下一个待测试的MME。 
使用[UNLOAD MME USER]命令，配置单用户指定MME卸载。
配置实例 :###### 配置实例-MME POOL组建 
数据规划
一个由3个MME节点组成的MME
POOL，其中MME节点1中规划用户数为100000。MME节点2中规划用户数为200000，MME节点3中规划用户数为100000。这里根据用户数可知MME1：MME2：MME3
=1:2:1，这里预先设置MME1权重为50则MME2为100，MME3为50。其余参数规划参见[表1]。
MME节点|MME节点1|MME节点2|MME节点3
---|---|---|---
MME Group ID|32774|32774|32774
MME Name|MME1|MME2|MME3
MME Code|1|2|3
MME Weight|50|100|50
Country Code|86|86|86
National Destination Code|186|186|186
Mobile Country Code|460|460|460
Mobile Network Code|16|16|16
Support Type|Null|Null|Null
Carrier Name|ZTE|ZTE|ZTE
配置过程
与xGW、eNB、DNS、HSS等外围网元的对接，这里默认已经设置完成。 
在MME1上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG:MMEGROUPID=32774,MMENAME="MME1",MMECODE=1,MMEWEIGHT=50,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME1配置MME CODE=1配置MME权重=50
在MME2上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG:MMEGROUPID=32774,MMENAME="MME2",MMECODE=2,MMEWEIGHT=50,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME2配置MME CODE=2配置MME权重=100
在MME3上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG:MMEGROUPID=32774,MMENAME="MME3",MMECODE=3,MMEWEIGHT=50,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME3配置MME CODE=3配置MME权重=50
###### 配置实例-MME POOL中新增一个MME节点 
数据规划
一个由2个MME节点组成的MME POOL，其中MME节点1中规划用户数为100000，MME节点2中规划用户数为200000。
这里需要在MME POOL中新增一个MME节点3，规划用户数为100000，并希望短时间内MME1和MME2上的用户能够按照权重负荷重平衡到MME3上。根据用户数可知MME1：MME2：MME3
=1:2:1，这里MME1权重为50，MME2为100，则MME3为50。其余参数规划参见[表2]。
MME节点|MME节点1|MME节点2|新增MME节点3
---|---|---|---
MME Group ID|32774|32774|32774
MME Name|MME1|MME2|MME3
MME Code|1|2|3
MME Weight|50|100|50
Country Code|86|86|86
National Destination Code|186|186|186
Mobile Country Code|460|460|460
Mobile Network Code|16|16|16
Support Type|Null|Null|Null
Carrier Name|ZTE|ZTE|ZTE
配置过程
与xGW、eNB、DNS、HSS等外围网元的对接，这里默认已经配置完成。 
设置MME节点3本地移动数据。 
在MME3上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME3",MMECODE=3,MMEWEIGHT=50,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME3配置MME CODE=3配置MME权重=50
设置MME1和MME2权重为0，禁止用户接入。 
在MME1上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME1",MMECODE=1,MMEWEIGHT=0,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MME权重=0
在MME2上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME2",MMECODE=2,MMEWEIGHT=0,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MME权重=0
按照全局比例负荷重平衡MME1和MME2。 
这里假设MME1上接入的用户数为50000，MME2上接入的用户数为100000。
MME1：MME2：MME3 = 1:2:1，则MME1上需要保留75%用户，MME2上需要保留75%用户。 
MME1全局按比例进行负荷重平衡，如下： 
命令脚本|说明
---|---
EXEC REBALANCE:ACT="BY_RATE",RATE=750,STEP=100,PRELTIME=1|配置根据保留用户千分比方式进行负荷重平衡，保留用户千分比例为750，设置扫描步长100，卸载预处理时间为1。
MME2全局按比例进行负荷重平衡，如下： 
命令脚本|说明
---|---
EXEC REBALANCE:ACT="BY_RATE",RATE=750,STEP=100,PRELTIME=1|配置根据保留用户千分比方式进行负荷重平衡，保留用户千分比例为750，设置扫描步长100，卸载预处理时间为1。
查询负荷重平衡状态和用户数。 
MME1和MME2上查询负荷重平衡状态，如下： 
命令脚本|说明
---|---
SHOW REBALANCESTATE|如果状态为“系统没有处于重平衡状态”说明负荷重平衡结束。
MME3上查询用户数，如下： 
命令脚本|说明
---|---
SHOW MMEUSER STATS|如果附着用户数为37500左右，则说明用户已经卸载到新MME上。
负荷重平衡结束，重新将MME1和MME2上权重恢复正常值，允许用户正常接入。 
在MME1上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME1",MMECODE=1,MMEWEIGHT=50,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME1配置MME CODE=1配置MME权重=50
在MME2上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME2",MMECODE=2,MMEWEIGHT=100,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME2配置MME CODE=2配置MME权重=100
###### 配置实例-MME POOL中删除一个MME节点 
数据规划
一个由3个MME节点组成的MME POOL，其中MME节点1中规划用户数为100000。 
MME节点2中规划用户数为200000，MME节点3中规划用户数为100000。这里MME
POOL中需要将MME3节点删除。其余参数规划参见[表3]。
MME节点|MME节点1|MME节点2|MME节点3
---|---|---|---
MME Group ID|32774|32774|32774
MME Name|MME1|MME2|MME3
MME Code|1|2|3
MME Weight|50|100|50
Country Code|86|86|86
National Destination Code|186|186|186
Mobile Country Code|460|460|460
Mobile Network Code|16|16|16
Support Type|Null|Null|Null
Carrier Name|ZTE|ZTE|ZTE
配置过程
禁止MME3节点用户接入，并将用户负荷重平衡至POOL中MME1和MME2节点。 
设置MME3权重为0，禁止用户接入。 
在MME3上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME3",MMECODE=3,MMEWEIGHT=0,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MME权重=0
按照全局比例负荷重平衡MME3，即将所有用户全部负荷卸载。 
MME3全局按比例进行负荷重平衡，如下： 
命令脚本|说明
---|---
EXEC REBALANCE:ACT="BY_RATE",RATE=0,STEP=20,PRELTIME=54|配置根据保留用户千分比方式进行负荷重平衡，保留用户千分比例为0，设置扫描步长20，卸载预处理时间为54。
查询负荷重平衡状态和用户数。 
MME3上查询负荷重平衡状态，如下： 
命令脚本|说明
---|---
SHOW REBALANCESTATE|如果状态为“系统没有处于重平衡状态”说明负荷重平衡结束。
MME3上查询用户数，如下： 
命令脚本|说明
---|---
SHOW MMEUSER STATS|如果附着用户数为0，则说明用户已经卸载完成。
###### 配置实例-MME POOL中某个MME节点扩容 
数据规划
一个由3个MME节点组成的MME POOL，其中MME节点1中规划用户数为100000，MME节点2中规划用户数为200000，MME节点3中规划用户数为100000。这里需要将MME节点3扩容至200000。MME1：MME2：MME3
=1:2:2，而MME1权重为50，MME2权重为100，则MME3权重为100。其余参数规划参见[表4]。
MME节点|MME节点1|MME节点2|MME节点3
---|---|---|---
MME Group ID|32774|32774|32774
MME Name|MME1|MME2|MME3
MME Code|1|2|3
MME Weight|50|100|100
Country Code|86|86|86
National Destination Code|186|186|186
Mobile Country Code|460|460|460
Mobile Network Code|16|16|16
Support Type|Null|Null|Null
Carrier Name|ZTE|ZTE|ZTE
配置过程
禁止MME3节点用户接入，并将用户负荷重平衡至POOL中MME1和MME2节点。 
设置MME3权重为0，禁止用户接入。 
在MME3上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME3",MMECODE=3,MMEWEIGHT=0,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MME权重=0
按照全局比例负荷重平衡MME3，即将所有用户全部负荷卸载。 
MME3全局按比例进行负荷重平衡，如下： 
命令脚本|说明
---|---
EXEC REBALANCE:ACT="BY_RATE",RATE=0,STEP=20,PRELTIME=54|配置根据保留用户千分比方式进行负荷重平衡，保留用户千分比例为0，设置扫描步长20，卸载预处理时间为54。
查询负荷重平衡状态和用户数。 
MME3上查询负荷重平衡状态，如下： 
命令脚本|说明
---|---
SHOW REBALANCESTATE|如果状态为“系统没有处于重平衡状态”说明负荷重平衡结束。
MME3上查询用户数，如下： 
命令脚本|说明
---|---
SHOW MMEUSER STATS|如果附着用户数为0，则说明用户已经卸载完成。
这里的扩容介绍只涉及MME Pool的相关操作，其余如增加单板，设置SMP模块，增加模块负荷分担，重启整局等，这里不做描述，默认在这步已经完成了操作。 
在MME3上设置本地移动数据，如下： 
命令脚本|说明
---|---
SET COMBOCFG: MMEGROUPID=32774,MMENAME="MME3",MMECODE=3,MMEWEIGHT=100,CC="86",NDC="186",MCC="460",MNC="16",SUPTYPE="NULL",MMEULICHGRPT="YES",MMESHARETYPE="NO"|配置MMEGROUPID=32774配置MMENAME=MME3配置MME CODE=3配置MME权重=100
###### 配置实例-MME POOL内MME拨测 
数据规划
一个由2个MME节点组成的MME
POOL，其中MME节点1中规划用户数为100000。MME节点2中规划用户数为200000。这里根据用户数可知MME1：MME2
=1:2，这里预先设置MME1权重为50, MME2为100。其余参数规划见下[表5]。
MME节点|MME节点1|MME节点2
---|---|---
MME Group ID|32774|32774
MME Name|MME1|MME2
MME Code|1|2
MME Weight|50|100
Country Code|86|86
National Destination Code|186|186
Mobile Country Code|460|460
Mobile Network Code|16|16
Support Type|Null|Null
Carrier Name|ZTE|ZTE
启用“单用户指定MME卸载”功能验证MEE POOL内所有MME是否均能正常工作，用户是否能快速的从MME1迁移到MME2。 
配置过程
用户在MME1上附着后网管执行[UNLOAD MME USER]命令将用户迁移到MME2。
命令脚本|说明
---|---
UNLOAD MME USER:IMSI="460160000000001",GUMMEI="460"-"16"-32774-2|将4601600000000001的用户迁移到MME2。
调整特性 :###### MME权重调整 
MME权重调整主要是通过设置本地移动数据来完成，命令为[SET COMBOCFG]。
###### 负荷重平衡调整 
可以根据现场的要求设置卸载类型、卸载预处理定时器时长和扫描步长，将指定USMP上部分MM上下文的状态不是Detach或者Implicit
Detach状态的UE进行负荷重平衡，使UE迁移到其他MME上（该MME和当前MME在同一MME POOL中），命令为[EXEC REBALANCE]。
###### 取消负荷重平衡 
当系统处于负荷重平衡状态，需要取消该状态，让MME不再对用户进行负荷重平衡，可以通过命令[CANCEL REBALANCE]来操作。
测试用例 :###### MME POOL组建 
测试项目|MME POOL组网测试
---|---
测试目的|验证MME POOL中MME负荷的平衡性。
预置条件|MME POOL组网配置正确。MME POOL与外围eNB、HSS、DNS等通讯正常。DNS上配置正确的到MME/xGW的DNS解析。
测试过程|eNB触发S1-Setup Requset到MME。批量用户上线。查询POOL中各个MME的用户数。
通过准则|第1步中，MME携带消息S1 setup response中参数Relative MME Capacity与该MME上设置的权重值一致。第3步后，批量用户按照设置的权重值在POOL中的MME上接入。
测试结果|–
###### MME POOL中新增一个MME节点 
测试项目|MME POOL中新增一个MME节点测试
---|---
测试目的|验证MME POOL中MME负荷的平衡性。MME POOL中负荷重平衡用户的有效性。
预置条件|MME POOL组网配置正确。MME POOL与外围eNB、HSS、DNS等通讯正常。DNS上配置正确的到MME/xGW的DNS解析。
测试过程|按照规范和规划在MME POOL中新增一个MME节点，对接的所有eNB向该MME发送送S1-Setup Request消息。批量用户上线。查询POOL中各个MME的用户数。
通过准则|新增MME通过S1-Setup Response下发参数Relative MME Capacity与该MME上设置的权重值一致。新增的MME上有用户接入，且接入的用户数遵循新增MME在MME POOL中的权重比。
测试结果|–
###### MME POOL中删除一个MME节点 
测试项目|MME POOL中删除一个MME节点测试
---|---
测试目的|验证MME POOL中MME负荷的平衡性。MME POOL中负荷重平衡用户的有效性。
预置条件|MME POOL组网配置正确。MME POOL与外围eNB、HSS、DNS等通讯正常。DNS上配置正确的到MME/xGW的DNS解析。
测试过程|批量用户上线。删除MME节点：将其中一个MME权重设为0，使用全局比例重平衡，将用户全部负荷重平衡至POOL中其余MME。查询负荷重平衡状态，查询各个MME上的用户数。
通过准则|第3步后，查询负荷重平衡的MME，用户数为0，且由“负荷重平衡状态”转入“系统没有处于重平衡状态”。多次查询被删除的MME上没有用户接入，用户按照权重接入MMEPOOL中的其余MME。
测试结果|–
###### MME POOL中某个MME节点扩容 
测试项目|MME POOL中某个MME节点扩容测试
---|---
测试目的|验证MME POOL中MME负荷的平衡性。MME POOL中负荷重平衡用户的有效性。
预置条件|MME POOL组网配置正确。MME POOL与外围eNB、HSS、DNS等通讯正常。DNS上配置正确的到MME/xGW的DNS解析。
测试过程|按照规范和规划在MME POOL中将一个MME节点扩容（MME权重调整）。批量用户上线。查询POOL中各个MME的用户数。
通过准则|扩容的MME向所有的eNB发送MME Configuration Update消息，消息中携带Relative MMECapacity与该MME上修改后的权重值一致。扩容的MME上有用户接入，且接入的用户数遵循扩容后MME在MME POOL中的权重比。
测试结果|–
###### MME POOL内MME拨测 
测试项目|MME POOL内MME拨测
---|---
测试目的|验证MME POOL内MME是否正常。
预置条件|MME POOL组网配置正确。MME POOL与外围eNB、HSS、DNS等通讯正常。DNS上配置正确的到MME/xGW的DNS解析。
测试过程|用户附着后执行UNLOAD MME USER，将用户迁移到其他MME。
通过准则|触发充分配流程携带指定的GUMMEI。MME对用户发起Detach流程，并携带re-attach required指示。UE接受MME的分离流程后，根据re-attach required指示，使用最近一次。GUTI重分配流程分配的GUTI，发起附着流程; eNodeB根据GUMMEI解析出对应的MME，并向该MME转发附着请求。用户在目标MME上附着成功。
测试结果|–
常见问题处理 :问题描述|解决方法
---|---
MME POOL内各网元负荷不均，与设置的各网元权重差异较大。|检查MME POOL内的各个eNB是否工作正常，是否都与POOL内的MME建立连接，且正确接收了各个MME的权重。根据MME POOL和SGSN POOL的组网形式（独立还是COMBO），检查SGSN POOL的NRI规划和MME POOL的MMEC规划是否合理。
## ZUF-78-06-002 MME支持负荷重平衡功能 
MME负载重平衡是指通过将一个MME上的全部或部分用户迁移在同一个资源池中的其他MME上，以减少该MME上的用户数。该功能也可减少在MME升级或其他情况下对用户业务的影响。 
## ZUF-78-06-003 优选COMBO节点 
当UE发起附着请求，TAU/RAU切换，RIM或SUSPEND业务时，RNC或eNodeB选择带有旧局相同COMBO节点的SGSN或MME。通过COMBO组网，当UE在SGSN和MME之间进行跨RAT移动时，优选COMBO节点功能可减少局间信令，降低业务延迟。 
## ZUF-78-06-004 指定POOL中EPC网元节点拨测 
在网络投入使用，升级或交换过程中，需要通过拨测来验证EPC网元是否运行正常。此外，为定位故障，也需指派NE节点或路径进行拨测。全球运营商正在加快LTE网络建设和部署，因此网络启用，升级或交换更为频繁。对于EPC网元节点拨测的需求也越来越迫切。 
因此，通过EMS或OMM，MME在以下几方面提供支持： 
单用户指派目标MME进行卸荷。 
在附着过程中用户指派PGW/SGW。 
# ZUF-78-07 移动性限制 
概述 :功能描述 :因用户业务需求或运营商本地控制策略，MME需要针对用户接入进行限制（比如限制用户在某种接入类型或区域下接入）。 
功能特性简介 :为满足不同的接入限制需求，MME提供了多种接入限制策略。详细的解决方案参见下表。 
方案特性|实现简述|特导链接
---|---|---
ARD限制|MME检查用户签约数据中的接入限制数据（ARD）字段，并决定是否该用户有权限通过正在使用的无线接入技术进行注册。|ZUF-78-07-001 ARD限制
ODB限制|MME检查用户签约数据中的ODB字段，判断用户是否禁止进行PS业务，或者禁止漫游接入。|ZUF-78-07-002 ODB限制
Zone Code限制|MME支持按号段配置跟踪区与Zone Code的对应关系，也支持仅配置跟踪区与Zone Code的对应关系。若用户在HSS签约了Zone Code，则MME根据本地配置的跟踪区与Zone Code的对应关系，检查当前接入跟踪区是否存在相关的Zone Code配置。若存在对应配置，则允许用户接入；否则，限制用户接入。|ZUF-78-07-003 Zone Code限制
区域限制|MME区域限制方式不依赖于HSS签约，是基于本地配置的策略，即可对特定区域下的特定用户进行接入控制（允许或禁止用户接入）。|ZUF-78-07-004 区域限制
## ZUF-78-07-001 ARD限制 
概述 :MME可灵活的根据RAT限制用户移动性。 
收益 :通过ARD限制功能，运营商可方便的根据接入类型控制用户移动性。 
描述 :在UE的附注或TAU过程中，MME检查用户签约数据中的接入限制数据（ARD）字段，并决定是否该用户有权限通过正在使用的无线接入技术进行注册。如果MS检查失败，MME拒绝该用户进行附着或跟踪区更新。 
## ZUF-78-07-002 ODB限制 
概述 :本特性允许网络运营商或业务提供者通过异常处理程序调节用户接入业务，限制某些面向MME分组的业务，或限制漫游。ODB可立即生效，并能终止和限制后续面向MME分组的业务。 
收益 :凭借HSS中的ODB用户数据，本功能可拒绝欲注册用户的业务。 
描述 :业务提供者通过与HSS的管理互动控制ODB应用。 
如下列分类所述，业务提供者可能在任何时候激活本特性，能终止任何正在进行的面向相应报文的业务，并通过下列限制分类限制后续面向分组的业务： 
禁止所有面向分组的业务 
禁止漫游用户接入HPLMN-AP 
禁止漫游用户接入VPLMN-AP 
## ZUF-78-07-003 Zone Code限制 
特性描述 :摘要描述应用场景客户收益实现原理系统影响特性交互遵循标准特性能力O&M相关 
描述 :定义
区域编码(Zone Code)被用来定义用户允许漫游到位置区域，在地区签约数据中，通常包含一个区域编码列表，MME根据这个列表来确定允许漫游的跟踪区。 
背景知识
uMAC支持多种方式的网络接入控制，一种是基于IMSI的跟踪区的接入控制，另外一种基于IMSI的区域编码的接入控制。 
基于IMSI的跟踪区的接入控制
MME提供“跟踪区允许接入”和“跟踪区限制接入”两种配置。
如果“跟踪区允许接入”配置是生效的，则用户当前接入跟踪区，必须配置在“跟踪区允许接入”的该用户IMSI号段中，并且没有配置在“跟踪区限制接入”的该用户IMSI号段中，才允许用户接入；否则，限制用户接入。 
如果“跟踪区允许接入”配置没有生效的，则用户当前接入跟踪区，没有配置在“跟踪区限制接入”的该用户IMSI号段中，才允许用户接入；否则，限制用户接入。 
对于“跟踪区限制接入”配置，还支持根据IMSI号段进行所有区域限制功能。 
对于限制接入的限制原因。如果“跟踪区允许接入”配置是生效，并且在“跟踪区允许接入”配置中没有匹配允许接入的跟踪区，则使用安全变量配置的拒绝原因作为限制原因；如果“跟踪区限制接入”配置中匹配到限制接入的跟踪区，则使用该IMSI号段配置的拒绝原因作为限制原因。 
基于IMSI的区域编码的接入控制
需要在HSS中为用户签约允许漫游的区域编码列表，用户当前接入跟踪区的区域编码在签约的区域编码列表中，就允许用户接入，否则就限制用户接入。 
MME优先使用用户IMSI号段中的跟踪区归属区域编码来确定是否限制接入，如果没有该用户IMSI对应的IMSI号段的跟踪区归属区域编码配置，就使用MME缺省的跟踪区归属区域编码来确定是否限制接入。 
对于限制接入的限制原因。如果根据IMSI匹配到IMSI号段，则使用该IMSI号段配置的拒绝原因作为限制原因；否则，以安全变量配置的拒绝原因作为限制原因。 
应用场景 :基于IMSI号段跟踪区接入控制和基于IMSI号段区域编码接入控制都是MME可选择功能。默认情况下，这两个功能是关闭的。 
基于IMSI号段区域编码接入控制 
通常，对本网非漫游用户，可以通过在HSS中签约地区签约数据，让用户在特定的区域接入，一旦漫游地跟踪区所属区域编码不在签约的区域编码列表中，则MME限制用户接入，这能很好满足非漫游用户的区域限制需求。 
基于IMSI号段跟踪区接入控制 
对于漫游用户，在归属HSS中签约的区域编码可能在漫游地MME不受控制，因此MME提供一种本地策略来限制用户区域接入，即根据用户IMSI号段进行跟踪区直接限制。 
客户收益 :收益者|收益描述
---|---
运营商|为运营商提供灵活的网络接入控制方式，提供用户接入区域精细化控制，避免用户访问网络非授权区域。
实现原理 :涉及的网元
HSS网元作用：在区域编码接入控制功能中，HSS向MME提供地区签约数据，地区签约数据有一组区域编码列表组成，其允许用户可以漫游该区域编码列表所归属的跟踪区中接入网络。 
MME网元作用：提供基于IMSI的跟踪区接入控制功能以及对应的数据配置。提供基于IMSI的区域编码接入控制功能以及对应的数据配置。 
业务流程
Attach流程网络接入控制处理
Attach流程网络接入控制处理的流程如[图1]所示。
图1  Attach流程网络接入控制处理的流程图


流程说明： 
UE向eNodeB发送Attach Request消息，请求Attach流程。 
eNodeB转发Attach Request消息给MME处理。 
MME判断用户该附着是局间附着，则MME向老局MME/SGSN获取IMSI等信息。 
如果向老局获取IMSI失败，MME向终端UE发起获取IMSI的ID流程。 
MME判断是否需要对UE进行鉴权，是否需要鉴权，则MME进行鉴权和安全过程。 
MME进入跟踪区接入控制判断，如果判断结果为限制接入，则MME向UE发送Attach
Reject消息；如果判断结果为允许接入，则MME继续后续的Attach流程。 
如果UE在Attach Request消息中携带了加密传送标志，则MME向UE获取PCO或APN信息。 
如果MME有上次附着残剩的承载上下文信息，则MME向所在SGW/PGW发起会话删除流程，通知其释放资源。 
如果MME中没有该用户的签约上下文，则MME向HSS发起位置更新流程。 
如果MME中没有该用户的签约上下文，则MME向HSS发起位置更新流程。 
如果MME中没有该用户的签约上下文，则MME向HSS发起位置更新流程。 
如果MME中没有该用户的签约上下文，则MME向HSS发起位置更新流程。 
MME进入区域编码接入控制判断，如果判断结果为限制接入，则MME向UE发送Attach
Reject消息；如果判断结果为允许接入，则MME继续后续的Attach流程。区域编码接入控制原理，参见3.2节SDL图描述。 
MME根据签约上下文信息，发起创建会话流程，建立默认承载上下文，完成网络侧承载建立。 
MME发起初始化上下文建立，完成空口承载建立。 
UE接受默认承载建立，通过Direct  Transfer消息发送Attach Complete消息给MME。 
eNodeB转发Attach Complete消息给MME。 
MME发起承载更新流程，通知SGW更新eNodeB的下行数据传递地址和隧道信息。 
TAU流程网络接入控制处理
TAU流程网络接入控制处理的流程如[图2]所示。
图2  TAU流程网络接入控制处理的流程图

流程说明： 
UE满足23401协议中5.3.3.0节TAU触发条件之一，触发TAU流程。 
UE向eNodeB发送TAU Request消息，请求TAU流程。 
eNodeB转发TAU Request消息给MME处理。 
MME根据old GUTI判断是局间TAU流程，MME向老局MME或SGSN发送Context Request消息，请求转移老局移动管理上下文和承载上下文信息。如果老局是MME，则老局完成Complete
TAU Request消息的NAS安全头完整性检查。如果老局是SGSN，则老局完成PTMSI Signature检查。老局MME或SGSN安全检查通过后，向新局MME发送Context
Response消息。该消息携带当前的安全上下文，未使用的鉴权向量。 
MME根据判断是否需要进行鉴权，如果需要，则完成鉴权和安全流程。 
MME进入跟踪区接入控制判断，如果判断结果为限制接入，则MME向UE发送TAU
Reject消息；如果判断结果为允许接入，则MME继续后续的TAU流程。 
MME向老局MME或SGSN发送Context Acknowlege消息，该消息指示老局SGW不改变。 
MME验证来自UE的承载上下文的承载状态，如果对应的承载上下文已经在UE中去活，则MME根据每个PDN连接向SGW发送Modify
Bearer Request消息，通知SGW/PGW释放相应的资源。 
MME向HSS完成位置更新，HSS向老局SGSN/MME发起位置取消，如果老局存在Iu连接，老局SGSN发起Iu释放流程。 
MME进入区域编码接入控制判断，如果判断结果为限制接入，则MME向UE发送TAU Reject消息；如果判断结果为允许接入，则MME继续后续的TAU流程。 
MME向UE发送TAU Accept消息，指示UE网络侧已经完成了TAU更新流程。 
如果MME在TAU Accept消息中分配了新的GUTI或TA LIST，则UE向MME发送TAU Complete消息。 
系统影响 :系统性能|影响程度|备注
---|---|---
内存占用|DB表|低|新增几个配置表，对系统内存占用较小
前台数据区|内存占用|无|无
CPU消耗|业务处理|低|无
增加进程|CPU消耗|无|无
增加消息交互|CPU消耗|无|无
通讯带宽|主备机带宽|不涉及|无
板间带宽|通讯带宽|低|无
结论：该功能对系统CPU、内存消耗、通讯带宽影响较小。|结论：该功能对系统CPU、内存消耗、通讯带宽影响较小。|结论：该功能对系统CPU、内存消耗、通讯带宽影响较小。|结论：该功能对系统CPU、内存消耗、通讯带宽影响较小。
特性交互 :开启了区域编码控制接入功能，在MME的TA LIST分配功能生成的TA LIST需要剔除掉不在签约Zone Code中允许接入的TA。涉及的流程有：分配TA
LIST的Attach流程，分配TA LIST的TAU流程，GUTI重分配流程。 
遵循标准 :本特性的参考资料清单如下： 
3GPP TS 23.401: " General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access" 
3GPP TS 29.272 " Mobility Management Entity (MME) and Serving
GPRS Support Node (SGSN) related interfaces based on Diameter protocol" 
3GPP TS 29.274 " Tunnelling Protocol for Control plane (GTPv2-C)" 
特性能力 :跟踪区接入控制功能，提供40000条IMSI号段记录配置。 
区域编码接入控制功能，配置最多256个不同的IMSI号段，每个IMSI号段最多配置64个不同的区域编码。 
O&M相关 :命令
配置项新增配置项参见表2。表2  新增配置项配置项命令MME限制区域配置ADD MME RESTRICT AREADEL MME RESTRICT AREASHOW MME RESTRICT
AREAMME IMSI号段LBO限制配置ADD MME IMSI RESTRICT LBOSET MME IMSI RESTRICT LBODEL MME IMSI
RESTRICT LBOSHOW MME IMSI RESTRICT LBO跟踪区区域编码配置ADD TAIZCSET TAIZCDEL TAIZCSHOW TAIZCIMSI号段对应的区域编码配置ADD MME IMSI TAIZCSET
MME IMSI TAIZCDEL MME IMSI TAIZCSHOW MME IMSI TAIZC 
安全变量新增安全变量参见表3。表3  新增安全变量安全变量命令支持基于IMSI号段的TAI区域限制SET MOBILE MANAGEMENT:SPTIMSITAIRST="YES"由于区域编码限制用户接入拒绝原因值SET MOBILE MANAGEMENT:MMEZONECODELIMIT="EPS
services not allowed" 
话单与计费
MME不需要出话单，因此不涉及到话单与计费。 
特性配置 :摘要配置特性测试用例 
配置特性 :配置过程
执行[ADD MME RESTRICT AREA]命令增加限制区区域。
执行[ADD MME IMSI RESTRICT LBO]命令增加基于IMSI号段LBO限制。
执行[ADD TAIZC]命令增加区域编码。
执行[ADD MME IMSI TAIZC]命令增加基于IMSI号段的区域编码。
执行[SET MOBILE MANAGEMENT]命令配置支持MME支持区域码限制。
在HSS授理台上签约区域限制业务。 
配置实例
配置命令|描述
---|---
ADD MME RESTRICT AREA:AREAID=255,TAID="1003"|配置MME限制区区域1003，区域标识为255。
ADD MME IMSI RESTRICT LBO:IMSI="46003000000026"|配置基于IMSI号码为46003000000026的LBO限制。
ADD TAIZC:NAME="ta4-zc2",TAID=4,ZC="0002"|增加用户别名为ta4-zc2的跟踪区区域配置，跟踪区TAI为4，区域编码0002。
ADD MME IMSI TAIZC:IMSI="46001",TAID=1,ZC="0001",CAUSE="TANotAllowed",NAME="imsiTAZC"|添加46001号段，跟踪区标识为1、区域编码0001的记录。归属此号段的签约了ZC的用户，因不在此配置范围内而接入失败，失败原因值为“TANotAllowed”。
SET MOBILE MANAGEMENT:MMELIMITZONESWITCH="YES"|设置支持MME支持区域码限制。
测试用例 :测试项目|配置限制部分区域接入记录，记录匹配
---|---
测试目的|MME能够限制部分区域接入。
预置条件|MME配置限制部分区域接入的记录。
测试过程|用户进行附着，IMSI及TAI和已配置的限制部分区域记录匹配。
通过准则|能够匹配到IMSI号段和TA值的用户，attach失败，拒绝原因是限制记录的原因值；没有匹配到的用户，允许接入。
测试结果|能够匹配到IMSI号段和TA值的用户，attach失败，拒绝原因是限制记录的原因值；没有匹配到的用户，允许接入。
测试项目|配置允许部分区域接入记录，记录匹配
---|---
测试目的|MME允许部分区域接入。
预置条件|MME配置允许部分区域接入的记录。
测试过程|用户进行附着，IMSI及TAI和已配置的允许部分区域记录匹配。
通过准则|能够匹配到IMSI号段和TA值的用户，允许接入，attach成功；没有匹配到的用户，限制接入，拒绝原因为移动性管理参数配置的原因值。
测试结果|能够匹配到IMSI号段和TA值的用户，允许接入，attach成功；没有匹配到的用户，限制接入，拒绝原因为移动性管理参数配置的原因值。
测试项目|配置限制全部区域接入记录，记录匹配。
---|---
测试目的|MME限制全部区域接入。
预置条件|MME配置限制全部区域接入的记录。
测试过程|用户进行附着，IMSI和已配置的限制全部区域记录匹配。
通过准则|能够匹配到IMSI号段的用户，attach失败，拒绝原因是限制记录的原因值；没有匹配到的用户，允许接入。
测试结果|能够匹配到IMSI号段的用户，attach失败，拒绝原因是限制记录的原因值；没有匹配到的用户，允许接入。
测试项目|匹配IMSI号段区域编码记录匹配，记录匹配
---|---
测试目的|匹配IMSI号段区域编码记录匹配，允许接入。
预置条件|配置IMSI号段区域编码。
测试过程|用户签约zone code，发起attach或者TAU，用户的IMSI和IMSI号段区域中的记录匹配。在用户的IMSI号段下，用户当前所在TAI对应的zonecode与签约的zone code匹配。
通过准则|能够匹配到IMSI号段区域编码记录，允许接入；没有匹配到IMS号段区域编码记录，限制接入，限制原因值为ADD MMEIMSI TAIZC配置的原因值。
测试结果|能够匹配到IMSI号段区域编码记录，允许接入；没有匹配到IMS号段区域编码记录，限制接入，限制原因值为ADD MMEIMSI TAIZC配置的原因值。
测试项目|匹配到缺省区域编码记录匹配，记录匹配
---|---
测试目的|匹配到缺省区域编码记录匹配，允许接入。
预置条件|配置缺省区域编码记录。
测试过程|用户签约zone code，发起attach或者TAU，能够匹配到缺省区域编码记录。
通过准则|能够匹配到缺省区域编码记录，允许接入；没有匹配到缺省区域编码记录，限制接入，拒绝原因值为安全变量-移动性管理参数配置中配置的原因值。
测试结果|能够匹配到缺省区域编码记录，允许接入；没有匹配到缺省区域编码记录，限制接入，拒绝原因值为安全变量-移动性管理参数配置中配置的原因值。
## ZUF-78-07-004 区域限制 
特性描述 :特性描述 :描述 :定义 :MME区域限制，是移动接入限制的一种方式，是指MME基于本地配置策略对特定区域下的特定用户进行接入控制。 
背景知识 :在移动通信网络中，运营商可以为不同的用户提供不同的接入控制方式，如拒绝其他运营商用户接入到本网络，或拒绝某些特定用户接入到某些特定区域。 
MME已经提供了多种接入限制方式，如：ARD限制、ZoneCode限制等。但是，ARD限制只能根据用户的接入类型进行控制，无法针对指定区域进行控制；ZoneCode限制只能控制用户在指定区域允许接入，无法控制用户在指定区域禁止接入；且这两种限制方式都基于用户HSS签约，当漫游用户接入拜访地网络时，如果该用户在归属地HSS没有签约接入限制，则拜访地网络将无法对这类用户进行接入控制。 
为此，MME提供另外一种移动接入方式：MME区域限制。使用MME区域限制方式，不依赖HSS签约，基于本地配置策略，即可对特定区域下的特定用户进行接入控制，允许接入或者禁止接入。 
应用场景 :MME区域限制，是对特定区域下的特定用户进行接入控制，主要应用场景及使用分析如下： 
应用场景|使用分析
---|---
场景一：指定区域，只允许特定用户接入|运营商希望划定某些管控区域，在这些区域下只允许特定用户接入。
场景二：指定区域，禁止特定用户接入|运营商希望限制某些漫游用户的接入区域，为此指定一些区域，在这些区域下，漫游用户禁止接入。
场景三：默认区域，禁止特定用户接入|运营商希望禁止某些特定用户接入其网络下的默认区域。
场景四：默认区域，只允许特定用户接入|运营商网络下的默认区域，只允许特定用户接入，从使用来看，并无实际使用价值。
由于场景四无实际使用价值，下面只描述前面三种应用场景。 
应用场景一：指定区域，只允许特定用户接入
指定区域下，只有特定用户允许接入，其他用户禁止接入；默认区域下，所有用户都可以接入。 
应用场景二：指定区域，禁止特定用户接入
指定区域下，特定用户禁止接入，其他用户允许接入；默认区域下，所有用户都可以接入。 
应用场景三：默认区域，禁止特定用户接入
默认区域下，特定用户禁止接入，其他用户允许接入；指定区域下，所有用户都可以接入。 

客户收益 :受益方|受益描述
---|---
运营商|提高策略灵活性：为运营商提供灵活的移动接入限制策略，提供用户接入区域精细化控制，避免用户访问网络非授权区域。
移动用户|此特性对终端用户不可见。
实现原理 :系统架构 :在E-UTRAN网络中，用户通过MME接入网络，组网架构如下图所示。UE在不同的区域接入网络时，MME可以对其进行接入控制。

涉及的网元 :网元名称|网元作用
---|---
MME|基于本地配置的区域限制策略，允许用户接入或者拒绝用户接入。
协议栈 :图1  UE-MME接口协议栈

本网元实现 :Attach和TAU流程，MME在获取到用户号码后，根据用户号码和当前接入区域，基于本地配置的区域限制策略，允许用户接入或者拒绝用户接入。用户号码类型，可以是IMSI、MSISDN或者IMEI。限制区域，可以是TA、PLMN或者是所有区域。
业务流程 :Attach流程区域限制
UE发起Attach流程，向eNodeB发送Attach Request消息。 
eNodeB向MME发送Attach Request消息。 
MME按照现有流程获取到用户号码后，进行区域限制判断。如果判断结果为限制接入，则向UE发送Attach Reject消息，携带配置的限制接入原因，流程结束；如果判断结果为允许接入，流程继续。 
系统原有处理，附着流程继续。 
TAU流程区域限制
UE发起TAU流程，向eNodeB发送Tau Request消息。 
eNodeB向MME发送Tau Request消息。 
MME按照现有流程获取到用户号码后，进行区域限制判断。如果判断结果为限制接入，则向UE发送Tau Reject消息，携带配置的限制接入原因，流程结束；如果判断结果为允许接入，流程继续。 
系统原有处理，TAU流程继续。 
系统影响 :新增配置对系统内存占用较小，该特性对系统几乎无影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401（General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access ）|全部
特性能力 :名称|指标
---|---
MME号段限制区域配置支持的最大记录数|40000条
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|-|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增配置项参见[表2]。
配置项|命令
---|---
MME限制区域配置|ADD MME RESTRICT AREA
DEL MME RESTRICT AREA|MME限制区域配置
SHOW MME RESTRICT AREA|MME限制区域配置
MME号段限制区域配置|SET MME NUMSEG RESTRICT AREA POLICY
SHOW MME NUMSEG RESTRICT AREA POLICY|MME号段限制区域配置
ADD MME NUMSEG RESTRICT AREA|MME号段限制区域配置
SET MME NUMSEG RESTRICT AREA|MME号段限制区域配置
DEL MME NUMSEG RESTRICT AREA|MME号段限制区域配置
SHOW MME NUMSEG RESTRICT AREA|MME号段限制区域配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知信息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置限制区域可以定义允许用户接入的跟踪区或者PLMN。
通过配置号段限制区域可以指定某个IMSI/IMEI/MSISDN号段的用户，在指定的限制区域内是否允许接入。
配置前提 :无。 
配置过程 :使用基于IMSI号段的区域限制 
执行[SET MME NUMSEG RESTRICT AREA POLICY]:MMESPTIMSISEGREST="YES";命令，将“支持基于IMSI号段的TAI区域限制”的开关打开。
执行[ADD MME RESTRICT AREA]命令，设置期望IMSI号段受限的区域，这里的区域可以是一组TA，也可以是一组PLMN。
执行[ADD MME NUMSEG RESTRICT AREA]命令，设置IMSI号段和受限区域的关联关系，以及在配置的受限区域内是否允许接入。
使用基于IMEI号段的区域限制 
执行[SET MME NUMSEG RESTRICT AREA POLICY]:MMESPTIMEISEGREST="YES";命令，将“支持基于IMEI号段的TAI区域限制”的开关打开。
执行[ADD MME RESTRICT AREA]命令，设置期望IMEI号段受限的区域，这里的区域可以是一组TA，也可以是一组PLMN。
执行[ADD MME NUMSEG RESTRICT AREA]命令，设置IMEI号段和受限区域的关联关系，以及在配置的受限区域内是否允许接入。
使用基于MSISDN号段的区域限制 
执行[SET MME NUMSEG RESTRICT AREA POLICY]:MMESPTMSISDNSEGREST="YES";命令，将“支持基于MSISDN号段的TAI区域限制”的开关打开。
执行[ADD MME RESTRICT AREA]命令，设置期望MSISDN号段受限的区域，这里的区域可以是一组TA，也可以是一组PLMN。
执行[ADD MME NUMSEG RESTRICT AREA]命令，设置MSISDN号段和受限区域的关联关系，以及在配置的受限区域内是否允许接入。
配置实例 :场景说明 :假设运营商希望在TAID为6001和6002的区域内只允许IMSI号段为“460110002”的用户接入。其他用户被限制接入，携带给终端的拒绝原因值为“TA Not Allowed”。 
数据规划 :配置项|参数|取值
---|---|---
MME限制区域配置|限制区域标识|1|1|1
跟踪区标识|MME限制区域配置|6001、6002|6001、6002|6001、6002
配置步骤 :步骤|说明|操作
---|---|---
1|将“支持基于IMSI号段的TAI区域限制”的开关打开。|SET MME NUMSEG RESTRICT AREA POLICY:MMESPTIMSISEGREST="YES"
2|创建一个限制区域标识为1 的限制区域，包括6001和6002两个TAID。|ADD MME RESTRICT AREA:AREAID=1,TAID=6001&6002
3|新增针对IMSI号段为"460110002"的用户的限制策略，限制范围为标识为1的区域，允许用户接入。|ADD MME NUMSEG RESTRICT AREA:NUMSEG="460110002",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="YES"
4|新增针对除了IMSI号段为"460110002"的用户的限制策略，限制范围为标识为1的区域，拒绝接入时携带给用户的原因为“TA Not Allowed”。这里需要将NUMSEG 1~9都配上。|ADD MME NUMSEG RESTRICT AREA:NUMSEG="1",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="2",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="3",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="4",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="5",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="6",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="7",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="8",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"ADD MME NUMSEG RESTRICT AREA:NUMSEG="9",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="TANotAllowed"
5|数据传表生效。|SYNA
场景说明 :假设运营商希望限制IMSI号段为“460110002”的用户在TAID为6001和6002的区域内接入，携带给终端的拒绝原因值为“EPS Service Not Allowed”。 
数据规划 :配置项|参数|取值
---|---|---
MME限制区域配置|限制区域标识|1|1|1
跟踪区标识|MME限制区域配置|6001、6002|6001、6002|6001、6002
配置步骤 :步骤|说明|操作
---|---|---
1|将“支持基于IMSI号段的TAI区域限制”的开关打开。|SET MME NUMSEG RESTRICT AREA POLICY:MMESPTIMSISEGREST="YES"
2|创建一个限制区域标识为1 的限制区域，包括6001和6002两个TAID。|ADD MME RESTRICT AREA:AREAID=1,TAID=6001&6002
3|新增针对IMSI号段为"460110002"的用户的限制策略，限制范围为标识为1的区域，拒绝接入时携带给用户的原因为“EPS Service Not Allowed”。|ADD MME NUMSEG RESTRICT AREA:NUMSEG="460110002",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NO",CAUSE="EPSServicesNotAllowed",EXEMMCAUSE="NOTCARRY"
4|数据传表生效。|SYNA
场景说明 :假设运营商希望IMSI号段为“460110002”的用户只能在TAID为6001和6002的区域内接入，在其他区域内都被限制接入，携带给终端的拒绝原因值为“EPS Service Not Allowed”。 
数据规划 :配置项|参数|取值
---|---|---
MME限制区域配置|限制区域标识|1|1|1
跟踪区标识|MME限制区域配置|6001、6002|6001、6002|6001、6002
配置步骤 :步骤|说明|操作
---|---|---
1|将“支持基于IMSI号段的TAI区域限制”的开关打开。|SET MME NUMSEG RESTRICT AREA POLICY:MMESPTIMSISEGREST="YES"
2|创建一个限制区域标识为1 的限制区域，包括6001和6002两个TAID。|ADD MME RESTRICT AREA:AREAID=1,TAID=6001&6002
3|新增针对IMSI号段为"460110002"的用户的限制策略，限制范围为当前MME管控的区域，拒绝接入时携带给用户的原因为“EPS Service Not Allowed”。|ADD MME NUMSEG RESTRICT AREA:NUMSEG="460110002",NUMTYPE="IMSI",ISALLTA="YES",AREAID=1,ACCESS="NO",CAUSE="EPSServicesNotAllowed"
4|新增针对IMSI号段为"460110002"的用户的限制策略，限制范围为标识为1的区域，允许用户接入。|ADD MME NUMSEG RESTRICT AREA:NUMSEG="460110002",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="YES"
5|数据传表生效。|SYNA
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|MME支持基于号段的区域限制
---|---
测试目的|测试在附着流程中，根据配置的IMSI号段对应的跟踪区限制，对用户进行移动性限制。
预置条件|将“支持基于IMSI号段的TAI区域限制”的开关打开。配置某个IMIS号段在指定的TA范围内限制接入的策略。号段内的某个用户在指定TA下发起附着流程。
测试过程|MME获取到用户IMSI之后，匹配到对应策略，使用该策略限制用户接入。
通过准则|附着流程被拒绝，用户被限制接入。附着拒绝消息中携带的原因值为匹配策略中的原因值。
测试结果|–
测试项目|MME支持基于号段的区域限制。
---|---
测试目的|测试在TAU流程中，根据配置的IMSI号段对应的跟踪区限制，对用户进行移动性限制。
预置条件|将“支持基于IMSI号段的TAI区域限制”的开关打开。配置某个IMIS号段在指定的TA范围内限制接入的策略。号段内的某个用户在指定TA下发起TAU流程。
测试过程|MME获取到用户IMSI之后，匹配到对应策略，使用该策略限制用户接入。
通过准则|TAU流程被拒绝，用户被限制接入。TAU拒绝消息中携带的原因值为匹配策略中的原因值。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## ARD 
Access Restriction Data	接入限制数据
IMEI :International Mobile Equipment Identity国际移动设备标识
IMSI :International Mobile Subscriber Identity国际移动用户标识
MME :Mobility Management Entity移动管理实体
MSISDN :Mobile Station International Subscriber Directory Number移动台国际用户目录号
## ODB 
Operator Determined Barring运营商闭锁
PLMN :Public Land Mobile Network公共陆地移动网
## PS 
Packet Switched分组交换
TA :Tracking Area跟踪区域
TAU :Tracking Area Update跟踪区域更新
UE :User Equipment用户设备
# ZUF-78-08 UE能力管理 
概述 :功能描述 :UE能力可分为UE无线能力和UE网络能力。 
MME保存UE无线能力并提供给RAN，可避免RAN在从空闲态向连接态转换时再次向UE索取UE无线能力信息，从而节省空口资源。 
MME保存UE网络能力，且基于UE网络能力做差异化的处理。 
功能特性简介 :针对用户的各种能力信息，核心网提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
UE无线能力处理|终端在附着或TAU时，携带UE无线能力信息，MME保存这些信息，并且在Init Context Request Setup消息中下发给eNodeB，eNodeB进行保存。具体可参见3GPP 23401协议的“5.11.2 UE Radio Capability Handling”章节。|ZUF-78-08-001 UE无线能力处理
UE核心网能力|UE网络能力参数包括非无线能力参数，比如NAS安全算法等信息。MME保存和处理UE网络能力信息。用户发生移动时，MME将UE网络能力信息传递给新的SGSN或MME。具体可参见3GPP 23401协议的“5.11.3 UE Core Network Capability”章节。|ZUF-78-08-002 UE核心网能力
DRX参数处理|终端在附着或TAU时携带DRX参数，MME保存此参数并下发给eNodeB，同时用户发生移动时，MME将此参数传递给新的MME或SGSN。MME或SGSN对用户进行寻呼时会携带DRX参数。DRX参数处理具体参见3GPP 23.401协议的“5.13 Discontinuous Reception and UE Specific DRX Parameter handling”章节。|ZUF-78-08-003 DRX参数处理
根据UE能力关闭SGs口关联|网络同时支持VoLTE和CSFB时，如果UE先在IMS注册，再发起联合位置更新并建立SGs口关联，MSC/VLR会向HSS进行位置更新。HSS会修改用户注册信息为MSC地址，语音业务、短消息终呼业务回落到CS域。如果让用户在IMS进行语音业务和短消息业务，针对以下几类UE，需要关闭SGs口关联：UE支持IMS VoPS并设置为“prefer IMS PS Voice with CS Voice as secondary”，MME在Attach Accept/TAU Accept消息中指示UE核心网支持“IMS VoPS”。UE支持IMS VoPS并设置为“IMS PS Voice Only”，MME在Attach Accep/TAU Accept消息中指示UE核心网支持“IMS VoPS”。UE支持IMS VoPS并设置为“prefer CS Voice with IMS PS Voice as secondary”， MME在Attach Accept/TAU Accept消息中指示UE核心网支持“IMS VoPS”且“CS Fallback not preferred”。UE支持IMS VoPS并设置为“prefer CS Voice with IMS PS Voice as secondary”， MME在Attach Accept/TAU Accept消息中指示UE核心网支持“IMS VoPS”且“SMS Only”。|ZUF-78-08-004 根据UE能力关闭SGs口关联
## ZUF-78-08-001 UE无线能力处理 
概述 :本特性使得MME可处理UE的无线能力。 
收益 :MME可根据UE的无线能力合理的管理UE。 
描述 :本特性使得MME可处理UE的无线能力。 
UE的无线能力包含该UE支持的RAT上的信息（例如功率类别和频段等），因此，信息量可能很庞大（例如大于50
octet），以至于每当UE从ECM IDLE态转移到ECM CONNECTED态时，通过无线接口发送该信息的效果难以满足需求。为避免这种额外的无线开销，MME保存UE在ECM
IDLE状态时的能力信息。MME在能获取UE能力信息的情况下，可以通过S1接口的INITIAL CONTEXT SETUP REQUEST消息向E-UTRAN发送最新的UE无线能力信息，除非UE通过附着或跟踪区更新用于“ERAN/UTRAN附着后的首次TAU”或“UE无线能力更新”。
## ZUF-78-08-002 UE核心网能力 
概述 :本特性使得MME可处理“UE核心网能力”这个字段。 
收益 :MME可根据“UE核心网能力”这个字段来合理的管理UE。 
描述 :“UE核心网能力”是一个字段，包括UE网络能力IE（主要包含E-UTRAN接入相关核心网参数）和MS网络能力IE（主要包含UTRAN/GERAN接入相关核心网参数）。并且包含非无线相关能力，例如NAS安全算法。UE网络能力IE和MS网络能力IE在核心网节点间传输，包括从MME到MME、从MME到SGSN。
## ZUF-78-08-003 DRX参数处理 
概述 :DRX参数用于指示UE是否使用DRX模式。 
描述 :在E-UTRAN的附着过程中，UE向核心网发送UE特定的DRX参数。 
在E-UTRAN，UE可指示其期望在RAN系统消息中使用DRX周期广播，或者UE可提出期望的DRX周期长度。MME应接受UE提议的长度值。 
如果MME接收到UE发送的专用消息（例如Tracking Area Update或Attach消息），并且消息中含有特定的DRX参数，该核心网节点使用UE提供的信息更新保存的UE信息，并且优先使用UE提供的信息，而不使用在同一过程中可能从其他核心网节点获取的任何信息。 
## ZUF-78-08-004 根据UE能力关闭SGs口关联 
概述 :如果UE同时支持IMS语音和CS语音，MME优先支持IMS语音。SGs口是指MME和MSCS之间的接口。
收益 :运营商可同时部署IMS语音业务和CSFB语音业务以实现相互补充。 
描述 :当网络同时支持VoLTE和CSFB，如果注册在IMS的UE进行联合位置更新以建立SGs口关联，那么MSC/VLR会向HSS发送位置更新请求。HSS将用户的注册信息修改为MSC的地址，这样语音业务和短消息终呼可回落到CS域。运营商希望在IMS域进行语音和短消息业务。 
对于下列UE的情况，MME需要关闭SGs口关联： 
UE支持IMS VoPS，并且设置为“IMS PS语音优先，CS语音备用”。MME在Attach Accept/TAU
Accept消息中指示该UE支持核心网的IMS VoPS。 
UE支持IMS VoPS，并设置为“仅IMS PS语音”。MME在Attach Accept/TAU Accept消息中指示该UE在核心网中支持IMS
VoPS。 
UE支持IMS VoPS，并且设置为“CS语音优先，IMS PS语音备用”。MME在Attach Accept/TAU
Accept消息中指示该UE在核心网中支持“IMS VoPS”和“不首选CS回落”。 
UE支持“IMS VoPS”，并且设置为“CS语音优先，IMS PS语音备用”。MME在Attach Accept/TAU
Accept消息中指示该UE在核心网中支持"IMS VoPS"和“仅短消息业务”。 
# ZUF-78-09 移动性管理扩展功能 
概述 :功能描述 :移动性管理扩展功能可满足如下移动性需求： 
MME向接入用户下发时区和网络信息 
多SIM（一号多卡） 
RAN间配置信息传递 
提高寻呼效率 
支持多PLMN 
功能特性简介 :为满足不同的移动性管理扩展功能，MME提供了多种解决方案，参见下表。 
方案特性|实现简述|特导链接
---|---|---
配置转发|配置转发应用于两个eNodeB在任何时间通过S1接口与核心网进行传送信息。这两个eNodeB可以归属同一个MME，也可以归属不同的MME。|ZUF-78-09-001 配置转发过程
智能寻呼|智能寻呼是MME基于用户类型和业务类型选择相应的寻呼规则，综合用户的位置信息选择合适的范围，对用户进行寻呼，可有效减少整个网络中eNodeB的寻呼负荷，节省网络资源。MME可以根据实际业务要求选择合适的策略进行寻呼。|ZUF-78-09-002 智能寻呼
RIM|RIM流程提供了一种RAN节点之间通过MME节点交互专有应用信息的通用机制。RAN节点应用信息封装在RIM容器中，MME无需解析，将RAN信息通过接口消息从源RAN节点透传到目的RAN节点。源/目的RAN节点包括：GERAN、UTRAN、E-UTRAN。|ZUF-78-09-003 RIM
多SIM|对于多SIM功能，UE有两个MSISDN：常用MSISDN和个人MSISDN。这两个MSISDN保存在HSS上。在HSS将用户数据插入MME的过程中，MME保存这两个MSISDN。MME通过SGW向PGW提供常用MSISDN和个人MSISDN。PGW提供常用MSISDN给Radius服务器或WAP GW。个人MSISDN被写入由PGW生成的话单中。计费中心将个人MSISDN映射到常用MSISDN，以便将处理后的话单发布给客户。|ZUF-78-09-004 多SIM
多PLMN|MME支持多个PLMN，用户IMSI中的PLMN只要和MME支持的多个PLMN中的任一个相同，则判断该用户是归属地接入。|ZUF-78-09-005 多PLMN
多EPLMN|MME在TAU Accept或者Attach Accept消息中将EPLMN列表带给UE。UE进行PLMN选择、小区选择/重选或者切换时，列表中的所有PLMN都认为是同等重要的。MME可以根据不同IMSI号段下发不同的EPLMN列表。|ZUF-78-09-006 对等PLMN
多GUMMEI|GUMMEI由PLMN标识、MME组标识和MME码组成，用于全球唯一标识MME。由于同一个运营商可以存在多个PLMN，或者不同运营商共享核心网，因此MME需要支持多个GUMMEI。|ZUF-78-09-007 多GUMMEI
NITZ|当终端注册到MME后，MME根据运营商策略向终端更新NI和/或TZ信息。|ZUF-78-09-008 NITZ
TA列表静态分配|运营商可规划和配置静态TA列表分配策略。在动态分配策略不能满足需求时，可使用静态TA列表分配策略。|ZUF-78-09-009 TAList静态分配
下发IMEISV参数给eNodeB|MME在得到终端的IMEISV参数时，把IMEISv参数通过MME与eNodeB之间的S1接口消息带给eNodeB。|ZUF-78-09-010 IMEISV下发eNodeB
## ZUF-78-09-001 配置转发过程 
概述 :配置转发特性是指两个eNodeB在任何时间通过S1接口和核心网传送信息。例如，为在eNodeB之间使用X2接口用于自优化网络而交换eNodeB的IP地址。 
描述 :通过S1接口和核心网，可在任何时间在两个eNodeB之间传送信息。 
## ZUF-78-09-002 智能寻呼 
特性描述 :特性描述 :描述 :定义 :策略寻呼是指MME基于用户类型、业务类型选择相应的寻呼规则，综合用户的移动性，选择合适的范围对用户进行寻呼，从而有效地减少整个网络中eNodeB的寻呼负荷，节省网络资源。 
MME可以根据不同业务要求，在保证一定寻呼成功率基础上，选择合适的策略进行寻呼。 
背景知识 :引入该特性的意义
4G终端与网络侧进行数据交互时，为了节电会进入IDLE状态。终端处于IDLE状态下，如果此时网络侧有数据需要向终端发送，可通过触发寻呼流程，使终端进入CONNECTED状态，恢复数据传输。 
LTE寻呼流程是指：MME向终端所在的一定的物理区域内的所有eNodeB发送寻呼请求，eNodeB在空口进行广播，当终端收到寻呼请求后，重新建立与网络侧的连接。 
随着数据业务爆发式增长，LTE寻呼面临着如下挑战： 
寻呼在话务模型中所占比重越来越大，寻呼数量呈指数级增长，极端情况下可能引起信令风暴。 
VoLTE语音业务对时延非常敏感，此类业务需要尽量缩短寻呼时延，提升用户体验。 
MME需要支持策略寻呼，以提供完善的解决方案来应对这些挑战。 
寻呼指标
衡量寻呼的三个关键指标为寻呼负荷、寻呼成功率和寻呼时延。 
寻呼负荷由于寻呼消息具有广播特征，因此需要合理规划寻呼范围，保持寻呼消息在合适范围内进行发送，可有效的降低寻呼负荷，在寻呼区域已合理规划的基础上，通过合理预测用户位置，缩小寻呼范围，可进一步降低寻呼负荷。 
寻呼成功率保证一定寻呼成功率，是业务稳定运行的基础。决定寻呼成功率的要素有：寻呼范围和寻呼次数。缩小寻呼范围可能导致寻呼失败，加大寻呼次数并扩大寻呼范围可提高成功率。 
寻呼时延对于时延敏感的业务（比如语音呼叫），寻呼时需要优先考虑时延影响。对于时延敏感的业务，需要寻呼能够尽快完成。使用TA
List寻呼可提高一次寻呼成功率，从而降低寻呼时延。 
TA List
MME基于TA List跟踪IDLE态下用户位置信息，TA
List包含若干TA，每一个TA包含若干个eNodeB，如[图1]所示。
图1  TA List

通过TA List的合理规划可有效降低寻呼负荷。 
如果TA List规划太小，会导致终端频繁触发TAU。 
如果TA List规划太大，会导致寻呼负荷呈指数级增长（一个TA List下包含N个TA，每个TA包含M个eNodeB，采用TA
List方式寻呼，一次下行数据触发的寻呼将导致MME发送N×M条寻呼请求消息给eNodeB）。 
寻呼范围
UE处于IDLE态下，MME基于分配给UE的TA List来管理用户位置，根据3GPP协议要求，寻呼范围为TA
List。如果MME能够根据UE的移动性预测UE当前的准确位置，则可以缩小寻呼范围，降低寻呼负荷。 
寻呼范围从小到大依次参见[表1]。
排序|范围大小|描述
---|---|---
1|最近访问的eNodeB|针对UE上次驻留的eNodeB发起寻呼。
2|最近访问的eNodeB列表|针对UE上次驻留的eNodeB及其相邻eNodeB的寻呼。
3|最近访问的TA|针对UE上次驻留的TA中所有的eNodeB发起寻呼。
4|最近访问的TA列表|针对UE上次驻留的TA及其相邻的TA中所有的eNodeB发起寻呼。
5|分配给UE的完整TA List|3GPP标准寻呼，对TA List下的所有eNodeB发起寻呼，此寻呼范围为MME的缺省寻呼范围。
根据UE移动性来预测UE准确位置的依据是：每几分钟触发一次寻呼，用户在几分钟时间内活动范围有限（大部分情况下用户处于低速移动或静止不动状态），结合用户最近的历史活动范围，可大致预测用户所在eNodeB/TA。 
应用场景 :概述 :常见的寻呼场景有三种，参见[表2]。在保证一定寻呼成功率基础上，根据不同场景选择不同的寻呼策略。
编号|应用场景|寻呼需求|寻呼策略
---|---|---|---
1|通用类业务的寻呼|对时延及寻呼负荷无特殊要求|智能寻呼
2|负荷敏感类业务的寻呼|寻呼负荷敏感、时延不敏感|精准寻呼
3|时延敏感业务类的寻呼|时延敏感|分业务寻呼
###### 智能寻呼 
场景分析
智能寻呼是指网络负荷不高，对寻呼时延没有特殊要求。在此种情况下，选择寻呼策略时可在时延及寻呼负荷间折衷。 
影响寻呼负荷及时延的关键因素是寻呼范围。寻呼范围过大影响寻呼负荷，寻呼范围过小影响一次寻呼成功率。因此，本场景下合适的寻呼范围是最近访问的TA。同时为保证一定的寻呼成功率，一次寻呼失败后需要扩大寻呼范围再次寻呼。
智能寻呼策略
根据场景分析，智能寻呼策略如下： 
一次寻呼范围：最近访问TA。 
二次寻呼范围：TA List。 
根据实际情况，对于TA List规划建议如下： 
TA List包含的TA数在5个左右。 
TA包含的eNodeB数在20个左右。 
###### 精准寻呼 
场景分析
精准寻呼是指网络负荷较高，同时需要保证一定寻呼成功率。 
网络负荷较高时，需要尽量降低寻呼负荷，一次寻呼的范围需要尽可能小。但缩小寻呼范围会导致寻呼成功率相对降低，如果一次寻呼失败，需要逐步扩大寻呼范围，在降低寻呼负荷的同时保证一定的寻呼成功率。 
精准寻呼策略
根据场景分析，精准寻呼策略如下： 
一次寻呼范围：最近访问eNodeB。 
二次寻呼范围：最近访问eNodeB列表。 
三次寻呼范围：TA List。 
根据实际情况，对于TA List规划建议如下： 
TA List包含的TA数在5个左右。 
TA包含的eNodeB数在20个左右。 
###### 分业务寻呼 
场景分析
在保证一定寻呼成功率基础上，不同业务对寻呼的要求不同： 
语音类业务：要求寻呼时延尽可能短。对于语音类时延敏感业务，通过TA List寻呼来降低一次寻呼失败率，达到降低寻呼时延的目的。 
普通数据业务时延不敏感，寻呼负荷要合适。对于普通数据业务，时延无过高要求，可根据系统负荷情况，选择智能寻呼或精准寻呼。 
分业务寻呼策略
根据场景分析，区分业务寻呼策略参见[表3]。
业务类型|系统负荷|寻呼范围
---|---|---
语音类业务|-|一次寻呼范围：TA List。
二次寻呼范围：TA List。|语音类业务|-
普通数据业务|系统负荷不高|一次寻呼范围：最近访问TA。
二次寻呼范围：TA List。|普通数据业务|系统负荷不高
系统负荷较高|普通数据业务|一次寻呼范围：最近访问eNodeB。
二次寻呼范围：最近访问eNodeB列表。|系统负荷较高|普通数据业务
三次寻呼范围：TA List。|系统负荷较高|普通数据业务
根据实际情况，对于TA List规划建议如下： 
TA List包含的TA数在5个左右。 
TA包含的eNodeB数在20个左右。 
客户收益 :收益者|收益描述
---|---
运营商|通过选择合理的寻呼策略，运营商能获得如下收益：节约投资成本：可在保证寻呼成功率及用户体验基础上，降低寻呼负荷，节省网络资源。语音类业务增值：通过差异化的处理，保障了语音业务质量。
终端用户|提升用户体验：语音呼叫快速接通，享受高效的语音通话服务。
实现原理 :系统架构 :策略寻呼整体架构包含如下几个部分： 
触发寻呼：各种触发寻呼的业务，包括：普通数据、VoLTE语音、CS语音、短消息等。 
选择策略寻呼：由MME根据不同业务选择合适的寻呼策略进行寻呼。 
执行寻呼：eNodeB根据MME的寻呼请求在空口向终端发起寻呼。 
涉及的网元 :MME网元策略寻呼功能需要MME和eNodeB的共同完成，各网元作用参见[表4]。
网元名称|网元作用
---|---
MME|根据业务类型，不同的网络场景等条件组合，配置合适的寻呼策略。用户触发寻呼时，可选择合适的寻呼策略对用户进行寻呼，在保证一定寻呼成功率前提下，在寻呼负荷及寻呼时延等要求间取得平衡。
eNodeB|在指定的区域内寻呼。
本网元实现 :寻呼策略是对寻呼过程进行细化控制的过程，通过调整寻呼策略参数（包括寻呼范围、寻呼次数及寻呼时间间隔），对寻呼的三个关键指标（寻呼负荷、寻呼成功率及寻呼时延）产生影响。需要根据不同场景下对寻呼指标（寻呼负荷、寻呼成功率、寻呼时延）的不同要求，选择合适的寻呼策略。 
寻呼范围
寻呼策略包括：寻呼次数、每次寻呼的寻呼类型（寻呼范围及寻呼标识）、每一次的寻呼超时时长。其中，寻呼范围是关键参数，可设置的寻呼范围参见[表5]。
编号|寻呼范围|详细描述
---|---|---
1|当前CSG ID寻呼|仅对CSG用户有效，MME向用户当前所在CSG ID对应的eNodeB发送寻呼，寻呼标识基于GUTI。
2|当前CSG List ID寻呼|仅对CSG用户有效，MME向用户签约的CSG List ID对应的eNodeB发送寻呼，寻呼标识基于GUTI。
3|最近访问的eNodeB|MME向用户最近一次访问的eNodeB发送寻呼，寻呼标识基于GUTI。
4|最近访问的eNodeB列表|MME向用户最近访问的eNodeB List范围内发送寻呼，寻呼标识基于GUTI。
5|最近访问的TA|MME向用户最近一次访问的TA范围内发送寻呼，寻呼标识基于GUTI。
6|最近访问的TA列表|MME向用户最近几次访问的TA列表范围内发送寻呼，寻呼标识基于GUTI。
7|GUTI标识TAI List寻呼|MME向用户所在的TA List范围内发送寻呼，寻呼标识基于GUTI。
8|IMSI标识TAI List寻呼|MME向用户所在的TA List范围内发送寻呼，寻呼标识基于IMSI。
9|GUTI标识全MME寻呼|向整个MME发送寻呼，寻呼标识基于GUTI。
10|IMSI标识全MME寻呼|向整个MME发送寻呼，寻呼标识基于IMSI。
寻呼策略因子
目前MME支持如下几种类型的业务过滤条件（寻呼策略因子）设置寻呼策略。包含三种维度：用户信息、位置信息、业务类型，三者组合形成完整的匹配规则，过滤出唯一的寻呼策略，如[图2]所示。
图2  寻呼策略

业务流程 :策略寻呼主要业务流程如下： 
各种上层应用通过SGW、MSC等触发寻呼。
MME收到寻呼触发消息，根据触发场景选择合适的寻呼策略。 
MME根据寻呼策略中的寻呼范围，向指定范围内的eNodeB(s)发起寻呼。 
如果寻呼无响应，则根据寻呼策略中下一次寻呼范围，向指定范围内的eNodeB(s)发起寻呼。 
如果寻呼无响应，则根据寻呼策略中下一次寻呼范围，向指定范围内的eNodeB(s)发起寻呼。 
系统影响 :开启策略寻呼后，可有效降低寻呼负荷，节约MME和eNodeB资源消耗。 
应用限制 :当网络拓扑发生变化或出现网络问题，静态路由不能自适应变化的网络拓扑结构，可能会导致路由不可达，通信中断，必须由网络管理员修改路由配置。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准类别|标准名称|章节
---|---|---
3GPP|3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|4.3.5.3 Tracking Area list management5.3.4.3 NetworkTriggered Service Request
3GPP TS 23.272: "Circuit Switched (CS) fallback inEvolved PacketSystem (EPS)"|3GPP|7.2 Mobile Terminating call in idle mode8.2.4 Mobileterminating SMS in idle mode
3GPP TS 24.301: " Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS)"|3GPP|5.6.2 Paging procedure
3GPP TS 29.274: " Evolved General Packet Radio Service (GPRS)Tunnelling Protocol for Control plane (GTPv2-C)"|3GPP|7.2.11 Downlink Data Notification messages
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"|3GPP|8.5 Paging
特性能力 :规格名称|规格指标
---|---
最近访问的eNodeB列表支持的最大eNodeB数|7（个）
最近访问的TA列表支持的最大TA数|3（个）
一次寻呼过程支持的最大重发次数|20（次）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性对应License文件中的项目为“7032 MME支持策略寻呼功能”，需要申请了License许可后，运营商才能获得该特性的服务。
对其他网元的要求 :UE|MME|eNodeB|SGW
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表6  新增配置项配置项命令MME寻呼策略配置ADD MME PS PAGING POLICYSET MME PS PAGING POLICYDEL MME PS PAGING POLICYSHOW MME PS PAGING POLICYADD MME CS PAGING POLICYSET MME CS PAGING POLICYDEL MME CS PAGING POLICYSHOW MME CS PAGING POLICYADD MME SMS PAGING POLICYSET MME SMS PAGING POLICYDEL MME SMS PAGING POLICYSHOW MME SMS PAGING POLICYADD MME IDR PAGING POLICYSET MME IDR PAGING POLICYDEL MME IDR PAGING POLICYSHOW MME IDR PAGING POLICYADD MME NBIOT PAGING POLICYSET MME NBIOT PAGING POLICYDEL MME NBIOT PAGING POLICYSHOW MME NBIOT PAGING POLICY 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参表7  新增软件参数软件参数ID软件参数名称262319MME是否支持Paging消息携带寻呼优先级 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警和通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :#### 配置分业务寻呼特性 
配置说明 :分业务寻呼可以通过寻呼策略因子来为不同的业务定制不同的寻呼策略。比如，VoLTE语音寻呼策略配置目的是通过语音业务寻呼策略的优化配置，提高VoLTE语音寻呼的寻呼成功率，减少寻呼时长。VoLTE语音寻呼策略的配置可以通过QCI、IMS
APN、PPI等信息来进行配置。 
配置前提 :配置VoLTE语音寻呼策略之前，需要完成用户ECP接入并注册到IMS域，IMS完成VoLTE呼叫相关的配置。 
配置过程 :[ADD MME PS PAGING POLICY]
配置寻呼策略Profile，可以配置寻呼方式、时间间隔，以及寻呼优先级。 
[ADD MME PAGING POLICY FACTOR]
配置寻呼策略因子，可以根据不同的组合信息关联不同的寻呼策略Profile。 
配置实例 :场景说明
假设VoLTE语音业务根据QCI=1或QCI=5获取寻呼策略，寻呼策略采用最近访问TAList寻呼方式，寻呼次数3次，寻呼时间间隔分别为2s、3s、4s，寻呼优先级为0。 
数据规划
根据假设的场景，VoLTE语音业务寻呼策略数据规划参见[表1]。
寻呼策略ID|寻呼方式|寻呼时间间隔|寻呼优先级
---|---|---|---
10|最近访问TAList寻呼|2s|0
最近访问TAList寻呼|10|3s|0
最近访问TAList寻呼|10|4s|0
根据假设的场景，策略寻呼因子数据规划参见[表2]。
QCI|寻呼策略ID
---|---
5|10
1|10
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置寻呼策略|创建寻呼策略ID为10的寻呼策略Profile：ADD MME PS PAGINGPOLICY:ID=10,PAGEPOLICY="LASTTALIST"-20-"PRIO_0"&"LASTTALIST"-30-"PRIO_0"&"LASTTALIST"-40-"PRIO_0"
2|配置QCI=1的寻呼策略因子|配置QCI为1的寻呼策略因子，引用寻呼策略10。ADD MME PAGING POLICYFACTOR:QCI=1,PGPOLICY="PS"-10
3|配置QCI=5的寻呼策略因子|配置QCI为5的寻呼策略因子，引用寻呼策略10。ADD MME PAGING POLICYFACTOR:QCI=5,PGPOLICY="PS"-10
4|配置软参262319|配置软参262319取值为1，开启MME支持S1口携带寻呼优先级信元。SET SOFTWARE PARAMETER:PARAID=262319,PARAVALUE=1
#### 配置智能寻呼特性 
配置说明 :智能寻呼策略配置目的是通过扩大寻呼范围，提高数据业务的寻呼成功率。 
配置前提 :配置智能寻呼策略之前，需要完成用户接入网络，数据业务可用。 
配置过程 :[ADD MME PS PAGING POLICY]
配置寻呼策略Profile，可以配置寻呼方式、时间间隔，以及寻呼优先级。 
[ADD MME PAGING POLICY FACTOR]
配置寻呼策略因子，可以根据不同的组合信息关联不同的寻呼策略Profile。 
[SET MME GLOBAL PS PAGING POLICY]
配置全局寻呼策略，如果MME不能通过策略寻呼因子获取到寻呼策略，就使用全局寻呼策略。 
配置实例 :场景说明
假设智能寻呼根据用户IMSI号段46001获取寻呼策略，寻呼策略采用最近eNodeBList寻呼方式，寻呼次数3次，寻呼时间间隔分别为2s、3s、4s，寻呼优先级分别为5、6。 
数据规划
根据假设的场景，智能寻呼策略数据规划参见[表3]。
寻呼策略ID|寻呼方式|寻呼时间间隔|寻呼优先级
---|---|---|---
12|最近访问eNodeB List寻呼|5s|5
最近访问eNodeB List寻呼|12|5s|6
根据假设的场景，策略寻呼因子数据规划参见[表4]和[表5]。
IMSI|IMSI Range Index
---|---
46001|1
IMSI Range Index|寻呼策略ID
---|---
1|12
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置寻呼策略|创建寻呼策略ID为12的寻呼策略Profile：ADD MME PS PAGINGPOLICY:ID=12,PAGEPOLICY="LASTENBLIST"-50-"PRIO_5"&"LASTENBLIST"-50-"PRIO_6"
3|配置全局寻呼策略|创建全局寻呼策略Profile：SET MME GLOBAL PS PAGINGPOLICY:PAGEPOLICY="LASTTA"-10-"PRIO_4"&"LASTTA"-20-"PRIO_5"&"LASTTALIST"-30-"PRIO_6"
4|配置46001号段的IMSI索引|配置46001号段的IMSI索引为1，分析器入口为IMSI寻呼策略分析选择子。ADDMDNAL:DGT="46001",ENTR="DAS_IMSI_PGPOLICY",RST=1
5|配置寻呼策略因子|配置IMSI号段索引为1的寻呼策略因子，寻呼策略为12。ADD MME PAGINGPOLICY FACTOR:USERNUMIDX=1,PGPOLICY="PS"-12
7|配置软参262319|配置软参262319取值为1，开启MME支持S1口携带寻呼优先级信元。SET SOFTWAREPARAMETER:PARAID=262319,PARAVALUE=1
#### 配置精准寻呼特性 
配置说明 :精准寻呼策略配置目的是通过缩小寻呼范围，减少寻呼延时。 
配置前提 :配置精准寻呼策略之前，需要完成用户接入网络，数据业务可用。 
配置过程 :[ADD MME PS PAGING POLICY]
配置寻呼策略Profile，可以配置寻呼方式、时间间隔，以及寻呼优先级。 
[ADD MME PAGING POLICY FACTOR]
配置寻呼策略因子，可以根据不同的组合信息关联不同的寻呼策略Profile。 
[SET MME GLOBAL PS PAGING POLICY]
配置全局寻呼策略，如果MME不能通过策略寻呼因子获取到寻呼策略，就使用全局寻呼策略。 
配置实例 :场景说明
假设精准寻呼根据用户接入的TAID获取寻呼策略，寻呼策略采用最近eNodeB
List寻呼方式，寻呼次数3次，寻呼时间间隔分别为2s、3s、4s，不携带寻呼优先级 
数据规划
根据假设的场景，智能寻呼策略数据规划参见[表6]。
寻呼策略ID|寻呼方式|寻呼时间间隔|寻呼优先级
---|---|---|---
12|最近访问eNodeB  List寻呼|5s|255
最近访问eNodeB List寻呼|12|5s|255
最近访问eNodeB List寻呼|12|5s|255
根据假设的场景，策略寻呼因子数据规划参见[表7]。
TAID|寻呼策略ID
---|---
1|12
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置寻呼策略|创建寻呼策略ID为11的寻呼策略Profile：ADD MME PS PAGINGPOLICY:ID=11,PAGEPOLICY="LASTENBLIST"-50-"PRIO_255"&"LASTENBLIST"-50-"PRIO_255"&"LASTENBLIST"-50-"PRIO_255"
2|配置全局寻呼策略|创建全局寻呼策略Profile：SET MME GLOBAL PS PAGINGPOLICY:PAGEPOLICY="LASTTA"-10-"PRIO_4"&"LASTTA"-20-"PRIO_5"&"LASTTALIST"-30-"PRIO_6"
3|配置寻呼策略因子|配置TAID为1的寻呼策略因子，寻呼策略为11。ADD MME PAGING POLICYFACTOR:TAID=1,PGPOLICY="PS"-11
测试用例 :测试项目|MME支持VOLTE语音寻呼和分组寻呼分别配置不同的寻呼策略
---|---
预置条件|MME和各邻接网元工作正常,MME策略寻呼license开启。MME配置数据业务寻呼策略：策略ID为100，在TA LIST范围内寻呼2次，第一次寻呼时长3s，第二次寻呼时长为5s。MME配置数据业务寻呼策略：策略ID为101，GUTI在TA LIST范围寻呼2次，第一次寻呼时长5s，第二次寻呼时长为5s。根据QCI分别配置QCI=5和QCI=9寻呼策略因子。QCI=5的寻呼策略因子关联策略ID为100的寻呼策略，QCI=9寻呼策略因子关联策略ID为101寻呼策略。
测试过程|开启信令跟踪。用户附着接入4G网络，建立QCI=9默认承载。用户发起IMS APN的PDN连接，建立QCI=5的默认承载。用户进入IDLE态。用户收到下行数据业务专有承载建立请求(QCI=9)，MME寻呼用户，用户无响应。用户收到下行VoLTE语音业务专有承载建立请求(QCI=5)，MME寻呼用户，用户无响应。
通过准则|验证MME支持VOLTE语音寻呼和分组寻呼分别配置不同的寻呼策略是否正确。
测试结果|数据寻呼无响应（手机拔电池或者放入屏蔽箱）,MME首次寻呼5s无响应后，MME再次进行，5s无响应后，寻呼终止。语音寻呼无响应（手机拔电池或者放入屏蔽箱）, MME首次寻呼3s无响应后，MME再次进行，5s无响应后，寻呼终止。
## ZUF-78-09-003 RIM 
特性描述 :特性描述 :描述 :定义 :RAN信息管理（下面简称RIM）流程提供了一种RAN节点之间通过核心网的SGSN/MME节点交互专有应用信息的通用机制。
RAN节点应用信息封装在RIM容器(RIM container)中，方便核心网（SGSN/MME）能够将RAN信息通过接口消息从源RAN节点透传到目的RAN节点而无需解析。源/目的RAN节点包括：GERAN，UTRAN，E-UTRAN。 
RIM流程涉及的接口包括：Gb(BSSGP)，Iu(RANAP)，S1(S1AP)，Gn(GTPv1)，S3(GTPv2)。 
背景知识 :RIM流程包括寻址、路由和转发三部分内容： 
寻址：用于标识RAN节点的地址，BSS的寻址标识是CGI(RAI+CI)，RNC的寻址标识是Global RNC-Id，eNodeB的寻址标识是eNodeB
Identifier。 
路由：源RAN节点通过对应的接口发送消息到归属的SGSN/MME，同时携带源/目的RAN节点地址；SGSN/MME节点（本文一般也称作中间节点）基于目的RAN地址解析出RAN节点归属的SGSN/MME，并通过Gn/S3口GTP消息发送到对应的SGSN/MME；目的RAN节点归属的SGSN/MME根据目的地址找到正确的目的RAN节点并发送下去； 
转发：SGSN/MME在路由过程中需要在不同的接口协议之间进行转换，包括BSSGP，RANAP，GTP，S1AP，这一过程称为转发。 
 说明： 
文中为了描述方便，源RAN节点归属的SGSN/MME，一般称作源侧中间节点（或者源侧SGSN/MME节点），目的RAN节点归属的SGSN/MME，一般称作目的侧中间节点（或者目的侧SGSN/MME节点） 
如果源RAN节点和目的RAN节点归属同一个SGSN/MME（或者同一个Combo局中的SGSN和MME），那么源侧和目的侧的中间节点就是同一个中间节点，为了描述方便，有的时候也会描述为源侧中间节点和目的侧中间节点，具体情况可根据语境（描述时的上下文）判断。 
应用场景 :RIM过程主要是应用于无线节点之间不支持切换，而又需要获取对端无线节点系统信息时一种辅助流程，比如NACC、SI3、MBMS data channel、SON
Transfer、UTRA SI(UTRA System Information)。
RIM功能主要服务于无线侧，核心网节点SGSN/MME作为中间路由节点需要支持RIM消息的路由和转发，且不关心其具体的无线侧的应用。 
SGSN/MME根据目的地址进行RIM消息的寻址、无状态路由及转发。 
RIM支持的无线节点包括： 
GERAN与GERAN之间的切换。 
UTRAN与UTRAN之间的切换。 
GERAN与UTRAN之间的切换。 
GERAN与E-UTRAN之间的切换。 
UTRAN与E-UTRAN之间的切换。 
客户收益 :受益方|受益描述
---|---
运营商|优化无线资源，降低用户跨RAN移动带来的影响。
移动终端用户|提升用户使用数据业务的体验。
实现原理 :系统架构 :GPRS网络架构图如[图1]所示。
图1  GPRS架构图

EPS网络架构图，如[图2]所示。
图2  EPS架构图

涉及的网元 :RIM流程需要BSC、RNC、eNodeB主导，SGSN/MME配合完成。 
其中，BSC需要支持Gb口的RIM消息的收发及解析，RNC需要支持Iu口的RIM消息的收发及解析，eNodeB需要支持S1口的RIM消息的收发及解析。 
网元名称|网元作用
---|---
SGSN/MME|作为RIM流程的中间转发节点，主要负责RIM消息寻址、无状态路由及转发。
BSC/RNC/eNodeB|作为RIM流程的源/目的RAN节点，将应用内容封装在RIM容器中，通过RIM流程，完成相关应用。
本网元实现 :SGSN负责接收和发送（路由转发）Gb/Iu/GTP口RIM消息。SGSN寻址方式是基于目的地址CGI、RNC
ID、eNodeB ID（或者TAI）构造逻辑域名通过本地查询或者DNS查询获取目的地IP地址。 
MME负责接收和发送（路由转发）S1/GTP口RIM消息。MME寻址方式是基于目的地址CGI、RNC
ID构造逻辑域名通过本地查询或者DNS查询获取目的地IP地址。（注：MME暂不支持S3/S10接口GTPv2的RIM消息转发）。 
业务流程 :Gb口RIM流程
图3  Gb口RIM流程

Gb口RIM流程简要介绍如下： 
SGSN收到Gb口BSC发过来的BSSGP层的RIM消息，解析目的路由地址成功后，转换为对应接口的RIM消息后发往本局管理的目的RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB），或者发往目的RAN节点归属的SGSN/MME。 
SGSN收到本局源RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB）或者源中间节点SGSN/MME的RIM消息，解析目的路由地址为本局管理的CGI，转换为BSSGP层的RIM消息，发往目的BSC。 
BSSGP层的RIM消息包括：RAN-Information-Request、RAN-Information、RAN-Information-ACK、RAN-Information-ERROR、RAN-Information-APPLICATION-ERROR。 
透传的内容封装在RIM消息中的RIM Container中，对应RIM消息不同，其Contianer的内容也不一样，分别为：RAN-Information-Request
RIM Container、RAN-Information RIM Container、RAN-Information-ACK RIM
Container、RAN-Information-ERROR RIM Container、RAN-Information-APPLICATION-ERROR
RIM Container。 
其他接口RIM中携带的RIM Container内容也是一样的。 
Iu口RIM流程
图4  Iu口RIM流程

Iu口RIM流程简要介绍如下： 
SGSN收到Iu口RNC发过来的RANAP层的RIM消息，解析目的路由地址成功后，转换为对应接口的RIM消息后发往本局管理的目的RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB），或者发往目的RAN节点归属的SGSN/MME。 
SGSN收到本局源RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB）或者源中间节点SGSN/MME的RIM消息，解析目的路由地址为本局管理的RNC-ID，转换为RANAP层的RIM消息，发往目的RNC。 
RANAP对应的RIM消息为DIRECT INFORMATION TRANSFER。 
S1口RIM流程
图5  S1口RIM流程

S1口RIM流程简要介绍如下： 
MME收到S1口eNodeB发过来的S1AP层的RIM消息，解析目的路由地址成功后，转换为对应接口的RIM消息后发往本局管理的目的RAN节点（比如：eNodeB，在Combo局还可能包含RNC或BSC），或者发往目的RAN节点归属的SGSN。 
MME收到本局源RAN节点（比如：eNodeB，在Combo局还可能包含RNC或BSC）或者源中间节点SGSN的RIM消息，解析目的路由地址为本局管理的eNodeB-ID，转换为S1AP层的RIM消息，发往目的eNodeB。 
S1AP层对应的RIM消息为：eNodeB DIRECT INFORMATION TRANSFER（eNodeB到MME），MME
DIRECT INFORMATION TRANSFER（MME到eNodeB）。 
Gn口RIM流程
图6  MME Gn口RIM流程

MME Gn口RIM流程简要介绍如下： 
MME将S1口收到的RIM消息通过Gn口GTPv1的RIM消息发往SGSN。 
MME收到Gn口的GTPv1 RIM消息，解析目的路由地址为本局管理的RAN节点，转换为对应接口的RIM消息发往目的RAN节点。 
对应的GTPv1的RIM消息为RAN Information Relay。 
系统影响 :RIM消息在SGSN/MME内部是用户无关的消息，一般无法根据用户标识（比如，IMSI、TEID、PTMSI+RAI等）进行负荷分担，而是通过局向链路/随机/轮询等保证系统内部的负荷分担均衡。 
RIM消息属于SGSN/MME无状态转发的消息，当无线侧触发的RIM消息量比较大的时候，MME/SGSN转发这些消息会加重系统的负荷，目前SGSN/MME没有对这类消息进行负荷控制，外场如果开启RIM功能，需要先向无线侧了解RIM的话务模型（RIM功能主控在无线侧，SGSN/MME无法给出对应话务模型），并根据下述性能影响进行合理评估（下面是实验室稳定环境下的测试结果，实际情况不保证完全一样，话务模型供参考）。 
根据本版本的实测结果，每模块每秒平均转发150条RIM消息，将会使CPU消耗增加1%，一般消息量与CPU消息呈线性比例关系。 
举例：SGSN有10个模块，根据无线话务模型及无线基站数量得出经由SGSN转发的RIM消息数（需要包括来回双向）为10000条/秒，那么会使得SGSN的CPU平均消耗增加10000/10/150≈6.7%。 
Gb口RIM流程在BVC链路建立时进行了协商，BSC或者SGSN支持RIM功能开关发生改变，无法立即生效，只有通过以后BSC或SGSN主动发起的信令BVC
Reset过程才能生效。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.003|Numbering, addressing and identification
3GPP TS 23.060|General Packet Radio Service (GPRS); Service description; Stage1
3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for EvolvedUniversal Terrestrial Radio Access Network (E-UTRAN) access
3GPP TS 25.413|UTRAN Iu Interface RANAP Signalling
3GPP TS 29.060|General Packet Radio Service (GPRS); GPRS Tunnelling Protocol(GTP)across the Gn and Gp Interface
3GPP TS 29.274|3GPP Evolved Packet System; Evolved GPRS Tunnelling Protocol(eGTP) for EPS; Stage 3
3GPP TS 36.413|Evolved Universal Terrestrial Access Network (E-UTRAN); S1Application Protocol (S1AP)
3GPP TS 48.018|General Packet Radio Service (GPRS); Base Station System (BSS)- Serving GPRS Support Node (SGSN); BSS GPRS Protocol (BSSGP)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
-|√|√|–|–|–
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令GPRS地址解析配置ADD SGSNHOSTSET SGSNHOSTDEL SGSNHOSTSHOW SGSNHOSTEPC地址解析配置ADD EPCHOSTSET EPCHOSTDEL EPCHOSTSHOW EPCHOSTEPC地址解析优选子网段配置ADD HOST SUBNET PRISET HOST SUBNET PRIDEL HOST SUBNET PRISHOW HOST SUBNET PRI 
安全变量该特性不涉及安全变量的变化。 
软件参数表3  新增软件参数软件参数ID软件参数名称65569SGSN支持标准eNB-ID解析65617MME支持RIM RNC-ID解析65619SGSN支持标准eNB-ID逻辑域名解析262283MME RIM流程获取目标SGSN IP时采用的域名格式65542SGSN是否支持RIM功能 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :增加了3G和LTE之间的RIM流程，增加了使用eNB-ID FQDN进行路由分析。 
配置前提 :MME或Combo局前后台连通。 
网管客户端和服务器间能够正常通信。 
配置过程 :条目|配置过程
---|---
SGSN解析配置|使用命令ADD SGSNHOST 配置到局间BSC/RNC的解析。如果软参262279 新局SGSN获取老局SGSN地址时的域名格式为EPS时，使用步骤2进行配置解析，解析逻辑名形式为rac0069.lac8052.rac.epc.mnc003.mcc460.3gppnetwork.org或rnc0042.rnc.epc.mnc001.mcc460.3gppnetwork.org。使用命令ADD EPCHOST配置到eNodeB的解析。使用命令ADD HOST SUBNET PRI配置解析地址优先级，该命令可用于配置EPCHOST和SGSNHOST的地址优先级。
MME解析配置|在MME中使用命令ADD EPCHOST 增加到SGSN的解析。如果软参262283 MME RIM流程获取目标SGSN IP时采用的域名格式为PS时，使用ADDSGSNHOST进行解析配置，配置的罗辑名格式为rac0001.lac3822. mnc001.mcc460.gprs或rnc0059.mnc003.mcc460.gprs。
配置实例 :###### 2G/3G到4G RIM 
使用场景
Combo 1局中SGSN收到Gb/Iu接口RIM流程到Combo 2局eNodeB。 
Combo 1局到Combo 2局MME的局间解析使用eNB ID构造FQDN。 
65618软参保持默认值：SGSN 支持标准eNB-ID解析格式设置为包括扩展位。 
65570软参保持默认值：MME Gn接口支持标准eNB-ID解析设置为包括扩展位。 
其余Combo 1局和Combo 2局物理环境参见[表2]。
交换局|物理环境
---|---
Combo 1局|>SGSN>>SGSN IP: 192.168.100.1>>RAI: 460(MCC)  01(MNC)  1500(LAC)  01(RAC)>>RNC>>>RNC ID:0x59   >>BSC   >>>Cell ID :  460(MCC)  01(MNC)  1500(LAC)  01(RAC)  0101(cell)
Combo 2局|>MME>>MME IP: 192.168.100.2>>>eNB>>>>TA :  460(MCC)  01(MNC)  2000(TAC)            >>>>eNB ID: 460(MCC)  01(MNC)  10025(eNB ID)
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|Combo 1局的SGSN开启RIM功能。|SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1
2|Combo 1局的SGSN开启2/3G到4G的软参开关。|SET SOFTWARE PARAMETER:PARAID=65569,PARAVALUE=3
3|Combo1局的SGSN处理收到Iu/Gb口RIM消息时，针对eNodeB解析的格式。|SET SOFTWARE PARAMETER:PARAID=65618,PARAVALUE=1
4|Combo 2局的MME Gn接口支持标准eNB-ID解析设置为包括扩展位|SET SOFTWARE PARAMETER:PARAID=65570,PARAVALUE=1
5|Combo 1局SGSN 支持标准eNB-ID解析格式设置为包括扩展位|SET SOFTWARE PARAMETER:PARAID=65619,PARAVALUE=1
6|Combo 1 局配置到Combo 2 MME的本地DNS解析|ADD EPCHOST:NAME="enb10025.enb.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="combo2",IPADDR="192.168.100.2",PROTOCOL="x-gn"&"x-gp"
###### 4G到2G/3G RIM 
使用场景
Combo 1局中MME收到S1口RIM流程到Combo 2局BSC/RNC。 
MME RIM流程使用EPS格式解析获取对端SGSN。 
其中Combo 1局和Combo 2局物理环境参见[表3]。
交换局|物理环境
---|---
Combo 1局|>MME>>MME IP: 192.168.100.1>>>eNB>>>>TA :  460(MCC)  01(MNC)  2000(TAC)            >>>>eNB ID: 460(MCC)  01(MNC)  10025(eNB ID)
Combo 2局|>SGSN>>SGSN IP: 192.168.100.2>>RAI: 460(MCC)  01(MNC)  1500(LAC)  01(RAC)>>RNC>>>RNC ID:0x59   >>BSC     >>>Cell ID : 460(MCC)  01(MNC)  1500(LAC)  01(RAC)  0101(cell)
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|Combo 1 局MME开启4-3 RIM功能|SET SOFTWARE PARAMETER:PARAID=65617,PARAVALUE=1
2|Combo 1局MME RIM流程使用EPS格式解析获取对端SGSN|SET SOFTWARE PARAMETER:PARAID=262283,PARAVALUE=1
3|Combo 2 局SGSN开启RIM功能|SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1
4|Combo 1 局配置到Combo 2 SGSN的本地DNS解析|4-3的RIM解析配置：ADD EPCHOST:NAME="rnc0059.rnc.epc.mnc003.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgsn",HOST="combo2",IPADDR="192.20.100.2",PROTOCOL="x-gn"&"x-gp"4-2的RIM解析配置：ADD EPCHOST:NAME="rac0001.lac1500.rac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgsn",HOST="combo2",IPADDR="192.168.100.2",PROTOCOL="x-gn"&"x-gp"
5|Combo 1局SGSN 支持标准eNB-ID解析格式设置为包括扩展位|SET SOFTWARE PARAMETER:PARAID=65619,PARAVALUE=1
6|Combo 1 局配置到Combo 2 MME的本地DNS解析|ADD EPCHOST:NAME="enb10025.enb.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="combo2",IPADDR="192.168.100.2",PROTOCOL="x-gn"&"x-gp"
调整特性 :无。 
测试用例 :无。 
常见问题处理 :无。 
## ZUF-78-09-004 多SIM 
概述 :MME支持多SIM功能。如果该特性被使能，多个使用常用MSISDN的UE可被激活并同时使用EPS业务。 
收益 :运营商可为用户部署定制业务。例如，用户可同时在不同设备上使用多个SIM卡，但是只使用一个MSISDN。或一组用户作为一个家庭或公司团队共享一个MSISDN号码，并使用该号码进行联系。在一些EPS业务中，MSISDN发挥重要作用。例如： 
WAP门户：门户应用为每个MSISDN创建多个配置文件用于提供定制内容。 
应用（如号码簿，消息备份和MSN):
大部分应用使用MSISDN作为登录名。  
推送邮件：邮件服务器可将常用MSISDN的邮件推送给最后登录的移动台。 
描述 :对于多SIM功能，UE有两个MSISDN：常用MSISDN和个人MSISDN。这两个MSISDN保存在HSS上。当HSS将用户数据插入MME的过程中，MME保存这两种MSISDN。MME通过专用消息格式向PGW提供常用MSISDN和个人MSISDN。但是PGW只提供常用MSISDN给Radius服务器或WAP GW。 
只有个人MSISDN被写入由PGW生成的话单中。计费中心将个人MSISDN映射到常用MSISDN，以便将处理后的话单发布给客户。 
## ZUF-78-09-005 多PLMN 
特性描述 :特性描述 :术语 :术语|含义
---|---
Equivalent PLMN List|由一系列PLMN组成，在进行PLMN选择时，列表中的PLMN都是同等重要的，优先级相同。
PLMN|公用陆地移动网络，由MCC+MNC组成，用于唯一标识一个移动网络，比如中国移动的PLMN为460 00，其中460为中国大陆的移动国家码(MCC)，00为中国大陆为中国移动分配的网络号。
GUMMEI|全球唯一移动管理实体标识，有MCC+MNC+MME Group ID+MME Code组成。
描述 :定义 :MME多PLMN功能，指MME支持多个PLMN，用户IMSI中的PLMN只要和MME支持的多个PLMN中的任一个相同，则该用户是归属地接入。 
EPLMN列表，是MME在TAU或者附着时，在TAU Accept或者Attach Accept消息中带给UE。UE进行PLMN选择、小区选择/重选或者切换的时候，列表中的所有PLMN都认为是同等重要的。MME可以根据不同IMSI号段下发不同的EPLMN列表。 
MME多GUMMEI功能，指MME可以配置多个不同的GUMMEI，这样对于同一个MME而言可以有不同的标识。 
背景知识 :PLMN，公用陆地移动网络，由移动国家码(MCC)和移动网络码(MNC)组成，用于唯一标识一个移动网络。其中MCC由国际标准机构按国家或者地区分配，全球唯一；而MNC则是由MCC对应的国家或者地区分配，在这个国家或地区内唯一。 
对于很多运营商而言，由于跨国运营，或者拥有多个不同的网络(2G\3G\LTE网络)，可能分配了多个PLMN，比如中国移动目前的PLMN由460
00、460 02、460 07等。同一个运营商下的用户，在不同国家或者地区，或者用户通过不同的接入技术接入该运营商网络，都应该属于归属地接入，而不是漫游。要达到这个要求，则需要网络能够支持多PLMN。 
EPLMN用于UE选网，EPLMN是与终端当前所选择的PLMN处于同等地位的PLMN。 
运营商可以规划多个PLMN或/和多个MME
Group ID或/和多个MME Code，MME支持多GUMMEI，能增加运营商组网的灵活性。 
应用场景 :场景一 :场景一： 
具有多个PLMN的运营商，比如跨国运营商或同一个运营商不同接入方式下使用不同的PLMN，用户的IMSI有多个PLMN，但无线就只有一个PLMN。 
该场景下，需配置多PLMN，多GUMMEI，EPLMN不需配置。 
场景二 :具有多个PLMN的运营商，比如跨国运营商或同一个运营商不同接入方式下使用不同的PLMN，用户的IMSI有多个PLMN，无线也配置了多个PLMN。 
该场景下，需配置多PLMN，多GUMMEI，EPLMN也需配置。 
客户收益 :受益方|受益描述
---|---
运营商|支持多PLMN，可以让不同网络的用户接入时，如同归属地接入一样，降低用户的费用，从而吸引更多的用户，增加了组网灵活性。
移动终端用户|一般来说，漫游接入与归属地接入相比，业务成功率相对低。在支持多PLMN网络的情况下，对于某些用户而言，业务成功率又相对较高。
实现原理 :涉及的网元 :网元名称|网元作用
---|---
UE|保存网络侧下发的EPLMN列表。在多个可用PLMN中选择一个合适的PLMN。
MME|UE接入时，只要和MME支持的任一PLMN相同，则属于归属地接入。TAU或者附着时，在TAU Accept或者Attach Accept消息中将配置的PLMN携带给UE。把配置的多GUMMEI投递给eNB，为UE分配GUTI时，GUTI中的PLMN为UE选择的PLMN。
eNB|如果配置了多GUMMEI，则在S1 Setup Response中带给eNodeB。多GUMMEI配置发生变更，比如增加一条配置或者删除一条配置时，MME通过MME Configuration Update消息，将更新后的多GUMMEI配置带给eNodeB。
本网元实现 :多PLMN 
UE附着和PDN连接建立时，MME需要判断UE是否归属地接入。用户IMSI中的PLMN只要和MME支持的多个PLMN中的任一个相同，则该用户是归属地接入。 
给UE分配GUTI时，GUTI中的GUMMEI中的PLMN，为UE选择的PLMN。 
收到S1 Setup Request消息，eNB支持的PLMN至少必须和MME支持的多PLMN中有一个相同，否则S1
Setup过程就会失败。 
EPLMN列表 
按IMSI号段配置EPLMN列表，如果IMSI号段没有配置，就使用缺省EPLMN列表。 
多GUMMEI 
在S1 Setup Response消息中，MME把多GUMMEI投递给eNB。 
MME支持的GUMMEI发生了改变，则MME通知eNB改变后的GUMMEI。 
MME为UE分配GUTI时，GUTI中的PLMN为UE选择的PLMN。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: " General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|-
3GPP TS 24.301 "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"|-
3GPP TS 36.413 "Evolved Universal Terrestrial Radio AccessNetwork (E-UTRAN);S1 Application Protocol (S1AP)"|-
特性能力 :名称|指标
---|---
对于MME多PLMN功能，包含移动数据中配置的PLMN，一个MME中最多可以配置PLMN数|17个
对于EPLMN列表，给每个UE下发的EPLMN列表中，最多可以包含不同的PLMN数|15个
对于EPLMN列表，可以按IMSI号段配置EPLMN列表，最多可以有IMSI号段数|80000个
对于多GUMMEI，GUMMEI个数为|512个
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|–|–|–
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令设置默认对等PLMNSET MME PLMN DEFAULT删除默认对等PLMNDEL MME PLMN DEFAULT查询默认对等PLMNSHOW MME PLMN DEFAULT新增对等PLMN Profile配置ADD MME PLMN PROFILE修改对等PLMN Profile配置SET MME PLMN PROFILE删除对等PLMN Profile配置DEL MME PLMN PROFILE查询对等PLMN Profile配置SHOW MME PLMN PROFILE新增MME IMSI对等PLMN配置ADD MME IMSI TAI PLMN修改MME IMSI对等PLMN配置SET MME IMSI TAI PLMN删除MME IMSI对等PLMN配置DEL MME IMSI TAI PLMN查询MME IMSI对等PLMN配置SHOW MME IMSI TAI PLMN设置移动管理参数SET MOBILE MANAGEMENT查询移动管理参数SHOW MOBILE MANAGEMENT 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME支持多个PLMN功能时，需要在MME上进行相应的配置。 
配置前提 :完成MME基本附着功能的数据配置。 
如果其他GUMMEI中的PLMN属于其他HPLMN，则需要先新增其他HPLMN，再配置其他GUMMEI。 
Global eNodeB ID中的PLMN以及eNodeB所支持的TA的PLMN，有一个PLMN和移动数据配置中的PLMN或者其他HPLMN配置中配置的某一个PLMN相同。 
配置过程 :在OMM命令终端上执行[ADD MME HPLMNCFG]命令增加其他HPLMN。
在OMM命令终端上执行[ADD GUMMEI]命令增加其他GUMMEI。
在OMM命令终端上执行[ADD MME PLMN PROFILE]命令增加EPLMN Profile。
在OMM命令终端上执行[ADD MME IMSI TAI PLMN]命令增加基于IMSI的EPLMN。
在OMM命令终端上执行[SET MME PLMN DEFAULT]命令增加默认对等EPLMN。
在OMM命令终端上执行[SET MOBILE MANAGEMENT]命令配置MME支持的EPLMN个数。
配置实例 :###### 实例场景1 
配置说明
MME支持的PLMN为46000、46004、46005、46006和46007，其中本局移动数据配置的PLMN为46000，MME
Group ID为32850，MME Code为1 
无线侧配置的TA的PLMN为46000 
配置场景
由于无线侧只支持46000的PLMN，MME侧只需要配置本局其他PLMN，不需要配置EPLMN和其他GUMMEI。 
配置实例
新增本局其他HPLMN 
[ADD MME HPLMNCFG]:MCC="460",MNC="04"
[ADD MME HPLMNCFG]:MCC="460",MNC="05"
[ADD MME HPLMNCFG]:MCC="460",MNC="06"
[ADD MME HPLMNCFG]:MCC="460",MNC="07"
###### 实例场景2 
配置说明
MME支持的PLMN为46000、46004、46005、46006和46007，其中本局移动数据配置的PLMN为46000，MME
Group ID为32850，MME Code为1 
无线侧配置的TA的PLMN为46000和46004 
对于IMSI号段为45400的用户，分配46000的EPLMN，让UE优先从46000接入；其它号段分配46000和46004的EPLMN 
配置场景
由于无线侧支持46000和46004，MME侧除了需要配置本局其他PLMN外，还需要根据eNodeB支持的PLMN配置其他GUMMEI和EPLMN，以便eNodeB根据GUMMEI选择MME，UE根据EPLMN选择接入的网络。 
配置实例
新增其他HPLMN 
命令： 
[ADD MME HPLMNCFG]:MCC="460",MNC="04"
[ADD MME HPLMNCFG]:MCC="460",MNC="05"
[ADD MME HPLMNCFG]:MCC="460",MNC="06"
[ADD MME HPLMNCFG]:MCC="460",MNC="07"
新增其他GUMMEI 
[ADD GUMMEI]:GUMMEI=1,PLMN="460"-"04",MMEGID=32850,MMEC=1
设置MME支持的EPLMN组数 
[SET MOBILE MANAGEMENT]:MMEEPLMNLISTNUM="15 EPLMNs"
设置EPLMN Profile 
[ADD MME PLMN PROFILE]:PROFILEID=1,PLMN="460"-"00"
设置基于IMSI的EPLMN 
[ADD MME IMSI TAI PLMN]:IMSI="45400",ISALLTA="YES",PROFILEID=1
 说明： 
命令中IMSI代表一个IMSI号段。如果在全部TA，都使用这个PLMN
Profile，则Apply All Tracking Area设置为Yes；如果只在部分使用，则Apply All Tracking
Area设置为No，并再Tracking Area ID中配置需要使用的TAID。 
设置默认EPLMN 
[SET MME PLMN DEFAULT]:PLMN="460"-"00"&"460"-"04"
 说明： 
当无对应PLMN Profile的用户接入时，MME将下发默认EPLMN。 
调整特性 :###### 调整命令 
功能|命令
设置其他GUMMEI|SET GUMMEI
设置PLMN Profile|SET MME PLMN PROFILE
设置基于IMSI的EPLMN|SET MME IMSI TAI PLMN
设置MME支持EPLMN个数|SET MOBILE MANAGEMENT
###### 调整实例 
设置其他GUMMEI，修改GUMMEI ID为1的记录配置： 
[SET GUMMEI]:GUMMEI=1,PLMN="460"-"08",MMEGID=32800,MMEC=30
设置PLMN Profile，修改Profile ID为1的记录配置： 
[SET MME
PLMN PROFILE]:PROFILEID=1,PLMN="460"-"09"
设置基于IMSI的EPLMN，修改460031号段的配置： 
[SET MME IMSI TAI
PLMN]:IMSI="460031",ISALLTA="YES"
设置MME不支持下发EPLMN： 
[SET MOBILE MANAGEMENT]:MMEEPLMNLISTNUM="NO"
测试用例 :测试项目|MME在S1 Setup流程中下发Served GUMMEI
---|---
测试目的|验证MME能够正确下发Served GUMMEI信息给eNodeB。
预置条件|MME和eNodeB连接正常MME中配置其他HPLMN和其他GUMMEI
测试过程|eNodeB发送S1 Setup Request消息给MME。
通过准则|MME回复的S1 Setup Response消息中携带Served GUMMEIs，包含本局移动数据中的GUMMEI和其他GUMMEI配置中的所有GUMMEI。
测试结果|–
测试项目|MME下发Served GUMMEI
---|---
测试目的|验证MME能够正确下发Served GUMMEI信息给eNodeB。
预置条件|MME和eNodeB连接正常MME中已经配置其他HPLMN和其他GUMMEI
测试过程|再新增一条其他GUMMEI记录。MME前后台同步。
通过准则|前后台同步后，MME发送MME CONFIGURATION UPDATE给eNodeB，携带Served GUMMEIs，包含本局移动数据中的GUMMEI和修改后的其他GUMMEI配置中的所有GUMMEI。
测试结果|–
测试项目|MME下发GUTI
---|---
测试目的|验证附着流程中MME正常分配GUTI。
预置条件|MME和HSS连接正常MME和SGW连接正常MME和eNodeB连接正常MME中本局移动数据中配置PLMN为PLMN1，并在其他HPLMN中配置PLMN2MME在其他GUMMEI配置中添加PLMN1和PLMN2对应的MME组ID和MME编码
测试过程|用户A附着，用户选择的PLMN是PLMN1。用户B附着，用户选择的PLMN是PLMN2。
通过准则|对于用户A，MME发送的Attach Accept中消息携带新分配的GUTI，其中GUTI中的PLMN为PLMN1，MME组ID和MME编码为PLMN1对应的MME组ID和MME编码中的一组。对于用户B，MME发送的Attach Accept中消息携带新分配的GUTI，其中GUTI中的PLMN为PLMN2，MME组ID和MME编码为PLMN2对应的MME组ID和MME编码中的一组。
测试结果|–
测试项目|MME下发EPLMN
---|---
测试目的|验证附着流程中MME下发正确的EPLMN给用户。
预置条件|MME和HSS连接正常MME和SGW连接正常MME和eNodeB连接正常MME中配置默认EPLMN，包含小于5个的PLMNMME配置IMSI号段1对应的EPLMN Profile，适用于所有TA，包含大于5个的PLMNMME中配置支持5个PLMN
测试过程|归属于IMSI号段1的用户A附着。不归属于IMSI号段1的用户B附着。
通过准则|对于用户A，MME发送的Attach Accept中消息携带EPLMN列表，其中EPLMN列表为IMSI号段1配置的EPLMN中的前5个。对于用户B，MME发送的Attach Accept中消息携带EPLMN列表，其中EPLMN列表为默认的EPLMN。
测试结果|–
常见问题处理 :无。 
## ZUF-78-09-006 对等PLMN 
概述 :可基于IMSI范围配置EPLMN列表。
收益 :不同的IMSI可使用不同的EPLMN列表。 
描述 :在成功附着或跟踪区更新过程中，可基于3GPP协议通知移动终端等效PLMN信息。 
在MME中，可基于如下维度配置等效PLMN： 
IMSI 
IMSI+跟踪区 
IMSI+PLMN 
当一位移动用户附着到该MME或通过跟踪区更新到该MME，可选择相应的EPLMN列表，并将列表发送给用户设备。 
## ZUF-78-09-007 多GUMMEI 
概述 :如同SGSN可能有多个NRI，MME也可能有多个GUMMEI，这个功能便于部署MME池。 
收益 :本特性便于部署MME池。 
描述 :GUMMEI由PLMN标识，MME组标识和MME码组成。 
MME支持多个GUMMEI。这些GUMMEI可能在其组成部分上各有不同，例如MME码和MME组标识。 
## ZUF-78-09-008 NITZ 
特性描述 :特性描述 :术语 :术语|含义
---|---
NI|Networks Identify网络标示，包括长指示和短指示两种，由运营商自由定义配置。
TZ|Time Zone时区。
MOCN|Multi-Operator Core Network多运营商网络共享的一种方式，共享无线接入网，核心网不共享。
GWCN|Gateway Core Network多运营商网络共享的一种方式，核心网网关不共享，共享移动性管理网元（比如SGSN或MME）。
描述 :定义 :NITZ为网络标识和时区总称，当终端注册到MME后，MME根据运营商策略向终端更新NI和/或TZ信息。
背景知识 :NITZ是一种用于自动配置本地的时间和日期的机制，同时也通过无线网向移动设备提供运营商信息，经常被用来自动更新移动电话的系统时钟。 
网络标识用于通知终端当前接入网络的运营商标识，当运营商开启网络共享时可能存在不同运营商需要配置不同的网络标识。 
MOCN网络共享架构如[图1]所示。
图1  MOCN网络共享架构

应用场景 :本功能的应用场景在于需要根据PLMN配置NI和TZ的场景，其中TZ可以根据TA或TA list来配置。 
MME下发NITZ场景包括如下几种情况，对于NI和TZ可分别指定场景。选择不发送时不可选择其他选项，否则可以复选多个场景进行发送。 
不发送即不发送EMM Information消息通知UE相关的NITZ信息。 
根据终端的业务流程IMSI附着局内GUTI附着RAT内局间GUTI附着RAT间局间GUTI附着局内普通TAU局内周期TAURAT内局间TAURAT间局间TAU局内切换后TAURAT内局间切换后TAURAT间局间切换后TAU业务请求 
当网络改变的标识NI（网络标识）其中任何一个字段变更，就认为网络标识改变。包括长名称或短名称以及对应的编码方式或长度发生改变。 
当DST（夏令时或时区）切入或切出当发生夏令时或时区改变时，会重发发送EMM Information消息。 
客户收益 :受益方|受益描述
---|---
运营商|方便使用MOCN/ GWCN功能。
移动用户|及时获知当前使用的PLMN和TZ信息。
实现原理 :涉及的网元 :本网元的功能是MME通知UE相关NITZ信息的过程，无网元间作用。 
本网元实现 :MME可以基于以下策略控制是否下发NITZ信息给UE： 
IMSI号段+业务种类 
全局开关+业务种类 
业务种类控制包括： 
IMSI附着 
局内GUTI附着 
RAT内局间GUTI附着 
RAT间局间GUTI附着 
局内普通TAU 
局内周期TAU 
RAT内局间TAU 
RAT间局间TAU 
局内切换后TAU 
RAT内局间切换后TAU 
RAT间局间切换后TAU 
业务请求 
网络标识改变时下发（附着、TAU或业务请求时） 
DST夏令时切入或切出时下发（附着、TAU或业务请求时） 
时区改变时下发（附着、TAU或业务请求时） 
NI可以根据如下策略设置： 
用户IMSI中的PLMN 
用户选择的PLMN 
全局设置 
TZ可以根据如下策略设置： 
根据TA设置 
全局设置 
业务流程 :图2  业务流程

一旦用户建立MM上下文，MME就可以下发0个、1个或者多个EMM INFORMATION消息，如果下发多个EMM
INFORMATION消息每个消息可以有不同内容。 
系统影响 :对系统来说开启NITZ功能，对系统影响不大。对于每个用户接入时均通知NITZ情况下，对CPU的影响预计在3%内。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 24.301：Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3|-
特性能力 :名称|指标
---|---
NI最大支持字节数，采用不同编码方式会影响实际使用名称长度|210个
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“NITZ Function”（license ID：7025），此项目显示为“支持”，表示ZXUN uMAC支持NITZ功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|–|–|–|–
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令新增基于PLMN的NI配置ADD PLMN NI修改基于PLMN的NI配置SET PLMN NI删除基于PLMN的NI配置DEL PLMN NI查询基于PLMN的NI配置SHOW PLMN NI新增跟踪区配置ADD TA修改跟踪区配置SET TA删除跟踪区配置DEL TA查询跟踪区配置SHOW TA设置MME全局NITZ配置SET MME NITZ查询MME全局NITZ配置SHOW MME NITZ新增MME基于IMSI号段的NITZ发送策略ADD MME IMSI NITZ修改MME基于IMSI号段的NITZ发送策略SET MME IMSI NITZ删除MME基于IMSI号段的NITZ发送策略DEL MME IMSI NITZ查询MME基于IMSI号段的NITZ发送策略SHOW MME IMSI NITZ 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :性能计数器名称
---
C465060016 发送EMM INFORMATION消息次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME支持NITZ功能时，需要进行相应的配置。 
配置前提 :MME与HSS连接正常 
MME与SAE-GW连接正常 
MME与eNB连接正常 
本局配置了合理的控制面地址 
本局配置了合理的负荷分担策略 
配置了本局所管理的TA  
NITZ功能license打开 
配置过程 :使用命令[ADD PLMN NI]增加PLMN对应的NI配置。
使用命令[ADD TA]配置TA对应的TZ配置。
使用命令[SET MME NITZ]或[ADD MME IMSI NITZ]配置NI、TZ的发送场景。
配置实例 :配置PLMN为46003的用户下发NITZ 
配置PLMN对应的NI 
命令脚本|解释说明
---|---
ADD PLMN NI:PLMN="460"-"03",ADDCI="NO",FULLNISTR="www",FULLNICODEPLAN="UCS2",SHORTNISTR="q",SHORTNICODEPLAN="UCS2"|配置PLMN对应的NI
配置TA对应的TZ 
命令脚本|解释说明
---|---
ADD TA:TAID=2301,MCC="460",MNC="03",TAC="2301",GLOBALTZ="NO",TIMEZONE="GMT+01:00",NAME="2301"|配置TA对应的TZ
配置NITZ的发送场景，可根据场景进行选择 
命令脚本|解释说明
---|---
SET MME NITZ:IFSENDNI="YES",SCENENI="IMSI",IFSENDTZ="YES",SCENETZ="IMSI",SENDTM="YES",ADDCNY="YES",LNAME="globalNI",LNAMECODE="BIT7",SNAME="global",SNAMECODE="BIT7"|配置全局NITZ的发送场景
ADD MME IMSI NITZ:IMSIIDX="46003",IFSENDNI="YES",SCENENI="IMSI"&"GUTI",IFSENDTZ="YES",SCENETZ="IMSI"&"GUTI",SENDTM="YES"|配置基于IMSI号段的NITZ的发送场景
调整特性 :无。 
测试用例 :测试项目|配置首次接入下发NITZ，IMSI Attach，下发NITZ
---|---
测试目的|验证配置首次接入时下发NITZ，IMSI Attach，下发NIZT正确。
预置条件|IDA消息中是否携带Last UE Activity Time开关打开。用户Attach成功。
测试过程|配置“终端在网络接入时”和“终端首次接入时”下发NITZ。IMSI Attach。
通过准则|附着成功。MME下发EMM information消息给UE。EMM information消息正确，解码正确。
测试结果|–
测试项目|配置当DST（夏令时）切入或切出时下发NIZT，业务请求，入夏令时，通知终端更新NITZ
---|---
测试目的|验证入夏令时下发NITZ正常。
预置条件|配置 “当DST（夏令时）切入或切出”下发NITZ。
测试过程|配置“当网络改变的标识”和“当DST（夏令时）切入或切出”下发NITZ。用户附着。入夏令时。用户发起业务请求。
通过准则|入夏令时后，不会下发NITZ，用户发起业务请求的时候，MME才下发NITZ。
测试结果|–
常见问题处理 :无。 
## ZUF-78-09-009 TAList静态分配 
运营商可规划和配置静态TA列表分配策略。在动态分配策略不能满足需求时，可使用静态TA列表分配策略。 
## ZUF-78-09-010 IMEISV下发eNodeB 
特性描述 :特性描述 :术语 :术语|含义
---|---
IMEI Sv|IMEISv由IMEI和Sv两个部分组成：IMEI是国际移动设备身份码的缩写，国际移动装备辨识码，是由15位数字组成的"电子串号"，IMEI与每台终端一一对应，而且该码是全世界唯一的。每一只终端在组装完成后都将被赋予一个全球唯一的一组号码，这个号码从生产到交付使用都将被制造生产的厂商所记录。Sv是该机的软件版本IMSISv可以作为终端的唯一编码。eNodeB可以根据终端的IMEISv来制定不同的策略。
描述 :定义 :IMEISV下发eNodeB是指MME在得到终端的IMEISV的时候，把IMEISV通过MME与eNodeB之间的S1接口消息带给eNodeB。
背景知识 :不同的厂家，不同的操作系统对于终端的无线处理方案不同，从而在接入到无线网络时有不同的方式，如果eNodeB针对所有的终端采取同一个策略，可能会造成部分终端接入失败或者接入不稳定。 
应用场景 :MME下发IMEISv给eNodeB主要应用于eNodeB针对不同类型的终端制定不同的策略，从而提供终端的接入成功率和无线网络的稳定性。 
客户收益 :受益方|受益描述
---|---
运营商|提高网络接通率。提高无线系统可靠性。提高用户满意度。
移动用户|减少无法接入无线网络的概率。提升终端用户体验。用户享受更稳定和更可靠的网络服务。
实现原理 :系统架构 :MME下发IMEISV给eNodeB特性利用现有网元消息接口，在现有的接口消息中新增参数字段达到目的，对系统架构无改变。 
涉及的网元 :网元名称|网元作用
---|---
MME|接收并保存UE带上的IMEISV，通过S1消息把IMEISV带给eNodeB。
eNodeB|接收并使用MME下发的IMEISV参数。
业务流程 :Initial Context Setup下发IMEISV的流程如[图1]所示。
图1  Initial Context Setup下发IMEISV的流程

MME在下发给eNodeB的INITIAL CONTEXT SETUP REQUEST的消息中把Masked IMEISV带给eNodeB。 
Handover Resource Allocation下发IMEISV的流程如[图2]所示。
图2  Handover Resource Allocation下发IMEISV的流程

MME在下发给eNodeB的HANDOVER REQUEST 的消息中把Masked IMEISV带给eNodeB。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)".|8.3.1 Initial Context Setup8.4.1 Handover Resource Allocation
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布
License要求 :该特性为uMAC的基本特性，无需License支持。 
对其他网元的要求 :MME下发IMEISv给eNodeB特性需要UE和eNodeB配合完成。 
其中，UE需要把IMEISv带给MME。eNodeB根据MME下发的MASK IMEISv执行不同的控制策略。 
UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项配置项命令移动管理参数配置SET MOBILE MANAGEMENTSHOW MOBILE MANAGEMENT 
安全变量该特性不涉及安全变量的变化。 
软件参数表1  新增软件参数软件参数ID软件参数名称262575MME支持下发IMEISV给eNodeB功能开关 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警和通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :当eNB需要用户的IMEISV对终端进行管理，对终端制定特殊的管理策略，需要MME把IMEISV传递给eNB。 
配置前提 :网元运行正常。 
配置过程 :MME上配置方法为：打开MME支持下发IMEISV给eNodeB功能开关：SET SOFTWARE PARAMETER:PARAID=262575,PARAVALUE=1MME开启获取IMEISV：SET MOBILE MANAGEMENT:MMEGETIMEI="Support ADD" 
SGSN上配置方法为：SGSN开启获取IMEISV：SET SOFTWARE PARAMETER:PARAID=262150,PARAVALUE=3 
配置实例 :###### 实例 1 
场景说明
MME能够在附着流程中下发IMEISV给eNB。 
配置步骤
进行如下配置： 
步骤|说明|示例
---|---|---
1|通过命令SET MOBILE MANAGEMENT配置MME获取IMEISV。|SET MOBILE MANAGEMENT:MMEGETIMEI="Support ADD"
2|打开软参262575，配置MME支持下发IMEISV给eNodeB功能。|SET SOFTWARE PARAMETER:PARAID=262575,PARAVALUE=1
###### 实例 2 
场景说明
3G切换4G，MME能够在HO Request消息中把IMEISV带给基站。 
配置步骤
进行如下配置： 
步骤|说明|操作
---|---|---
1|打开软参262150，配置SGSN支持下发IMEISV给eNodeB功能。|SET SOFTWARE PARAMETER:PARAID=262150,PARAVALUE=3
2|打开软参262575，配置MME支持下发IMEISV给eNodeB功能。|SET SOFTWARE PARAMETER:PARAID=262575,PARAVALUE=1
调整特性 :无。 
测试用例 :测试项目|MME支持下发IMEISV给eNB
---|---
测试目的|MME能够在INITIAL CONTEXT SETUP REQUEST消息中把IMEISV带给eNB。
预置条件|MME支持下发IMEISV功能开关打开。MME配置获取IMEISV。SGSN配置获取IMEISV。
测试过程|终端发起4G附着流程。
通过准则|MME能够在INITIAL CONTEXT SETUP REQUEST消息中把IMEISV带给eNB。
测试结果|–
测试项目|MME支持下发IMEISV给eNB
---|---
测试目的|MME能够在HO Request消息中把IMEISV带给eNB。
预置条件|MME支持下发IMEISV功能开关打开。MME配置获取IMEISV。SGSN配置获取IMEISV。
测试过程|3G到4G的切换流程。
通过准则|MME能够在HO Request消息中把IMEISV带给eNB。
测试结果|–
常见问题处理 :无。 
## ZUF-78-09-011 基于机器学习的智能寻呼 
特性描述 :描述 :定义 :基于机器学习的智能寻呼是指MME基于SON流程、X2/S1口切换等流程，自动学习eNodeB间邻接关系，当寻呼用户时，可以在用户最近一次接入的eNodeB及其邻接eNodeB寻呼，在保证寻呼成功率的提前下，减少寻呼时延和寻呼消息量。
邻接eNodeB，即物理上邻接的eNodeB。MME支持仅对中低速用户使用邻接eNodeB寻呼。 
背景知识 :4G终端与网络侧进行数据交互时，为了节电会进入IDLE状态。终端处于IDLE状态下，如果此时网络侧有数据需要向终端发送，可通过触发LTE寻呼流程，使终端进入CONNECTED状态，恢复数据传输。 
LTE寻呼流程是指：MME向终端所在的物理区域内的所有eNodeB发送寻呼请求，eNodeB在空口进行广播，当终端收到寻呼请求后，重新建立与网络侧的连接。 
随着数据业务的爆发式增长，LTE寻呼面临如下挑战： 
寻呼在话务模型中所占比重越来越大，寻呼数量呈指数级增长，极端情况下可能引起信令风暴。 
VoLTE语音业务对时延敏感，此类业务需要尽量缩短寻呼时延，提升用户体验。 
MME需要支持智能寻呼，以提供解决方案来应对这些挑战。 
寻呼指标
衡量寻呼的3个重要指标如下： 
指标|说明
---|---
寻呼负荷|由于寻呼消息具有广播特征，因此需要合理规划寻呼范围，保持寻呼消息在合适范围内进行发送，可有效降低寻呼负荷。在寻呼区域合理规划的基础上，通过合理预测用户位置，缩小寻呼范围，可进一步降低寻呼负荷。
寻呼成功率|保证一定寻呼成功率，是业务稳定运行的基础。决定寻呼成功率的要素有：寻呼范围和寻呼次数。缩小寻呼范围可能导致寻呼失败，增加寻呼次数并扩大寻呼范围可提高成功率。
寻呼时延|对于时延敏感的业务（比如语音呼叫），寻呼时需要优先考虑时延影响。使用TA List寻呼可提高一次寻呼成功率，从而降低寻呼时延。
寻呼范围
UE处于IDLE态下，MME基于分配给UE的TA List来管理用户位置。如果MME能够根据UE的移动性预测UE当前的准确位置，则可以缩小寻呼范围，降低寻呼负荷。 
寻呼范围从小到大依次参见下表。 
排序|范围大小|描述
---|---|---
1|最近访问的eNodeB|针对UE上次驻留的eNodeB发起寻呼。
2|最近访问的eNodeB列表或最近访问的eNodeB的邻接eNodeB列表|针对UE最近驻留的eNodeB列表或UE上次驻留的eNodeB及其相邻eNodeB列表发起寻呼。
3|最近访问的TA|针对UE上次驻留的TA中所有的eNodeB发起寻呼。
4|最近访问的TA列表|针对UE上次驻留的TA及其相邻的TA中所有的eNodeB发起寻呼。
5|分配给UE的完整TA List|3GPP标准寻呼，对TA List下的所有eNodeB发起寻呼，此寻呼范围为MME的缺省寻呼范围。
根据UE移动性来预测UE准确位置的依据是：每几分钟触发一次寻呼，用户在几分钟时间内活动范围有限（大部分情况下用户处于低速移动或静止不动状态），结合用户最近的历史活动范围，以及eNodeB间邻接关系，可大致预测用户所在eNodeB。 
应用场景 :在保证寻呼成功率的基础上，根据不同场景的特点，选择不同的寻呼策略。 
编号|应用场景|寻呼需求|邻接eNodeB寻呼策略
---|---|---|---
场景1|通用类业务的寻呼，如数据业务、信令。|对时延及寻呼负荷无特殊要求。|对于中低速移动的用户：一次寻呼范围：最近活动的eNodeB。二次寻呼范围：最近活动的eNodeB及其邻接eNodeB列表。三次寻呼范围：TA List。
场景2|负荷敏感类业务的寻呼，如抄表业务。|寻呼负荷敏感、时延不敏感。|对于中低速移动的用户：一次寻呼范围：最近活动的eNodeB。二次寻呼范围：最近活动的eNodeB及其邻接eNodeB列表。三次寻呼范围：TA List。
场景3|时延敏感业务类的寻呼，如语音业务。|时延敏感。|对于中低速移动的用户：一次寻呼范围：最近活动的eNodeB及其邻接eNodeB列表。二次寻呼范围：TA List。
客户收益 :受益方|受益描述
---|---
运营商|在保证寻呼成功率及用户体验的基础上，降低寻呼负荷，节省网络资源，节约投资成本；降低寻呼时延，保障语音业务质量。
移动用户|享受高效的语音通话服务，提升用户体验。
实现原理 :系统架构 :基于机器学习的智能寻呼系统架构如[图1]所示。
图1  系统架构

涉及的网元 :网元名称|网元作用
---|---
eNodeB|触发SON流程、X2口或S1口切换流程，携带两个相邻eNodeB的信息。
MME|MME根据SON流程、X2口或S1口切换流程，自动学习eNodeB间邻接关系；根据本地寻呼策略以及用户移动性（是否中低速移动用户），确定是否使用邻接eNodeB列表寻呼。
协议栈 :接口|协议栈信息参考
---|---
S1-MME|ZUF-78-16-001 S1-MME
本网元实现 :基于机器学习的智能寻呼包含如下几个部分： 
eNodeB邻接关系学习：根据SON流程、X2口或S1口切换流程，MME自动学习eNodeB间邻接关系。 
选择寻呼策略：由MME根据本地寻呼策略以及用户移动性，确定是否使用邻接eNodeB列表寻呼。对于中低速移动的用户，可以使用邻接eNodeB列表寻呼；对于高速移动的用户，不建议使用邻接eNodeB列表寻呼。 
执行寻呼：MME向UE最近驻留的eNodeB及其邻接eNodeB发送寻呼消息，eNodeB根据MME的寻呼请求在空口向终端发起寻呼。 
由于eNodeB邻接关系的学习是一个漫长的过程，为了避免长时间等待系统学习，MME支持手动配置导入eNodeB邻接关系（目前仅用于测试）。 
eNodeB邻接关系学习
MME通过SON流程、X2口或S1口切换流程学习eNodeB邻接关系。 
通过SON流程学习邻接关系：自组织网络SON流程实现了通过eNodeB Configuration Transfer和MME Configuration Transfer消息传递eNodeB的X2接口地址信息，及相关配置数据。当两个eNodeB通过X2接口进行SON流程时，则认为这两个eNodeB是相邻eNodeB。MME获取目标侧eNodeB ID方法：MME根据eNodeB Configuration Transfer消息中SON Configuration Transfer信元中的Target eNodeB ID得到目标eNodeB ID。MME获取源侧eNodeB ID方法：MME根据eNodeB Configuration Transfer消息中SON Configuration Transfer信元中的Source eNodeB ID得到源侧eNodeB ID。 
通过X2口切换流程学习邻接关系：相邻eNodeB间有X2接口，由目标侧eNodeB发起到MME的流程，MME通过Path Switch Request消息获取目标侧eNodeB与源侧eNodeB之间的邻接关系。MME获取目标侧eNodeB ID方法：Path Switch Request消息由目标侧eNodeB发起，MME收到此消息后，将发送此消息的eNodeB作为目标eNodeB，解析IP地址后根据IP地址找到目标侧eNodeB ID。MME获取源侧eNodeB ID方法：Path Switch Request消息中携带“Source MME UE S1AP ID”信元，MME根据此信元数值找到具有相同数值的“MME UE S1AP ID”MM上下文，此上下文保存的就是进行切换的用户信息，MM上下文中的“eNodeB Address in Use”即为源侧eNodeB的IP地址，MME根据此IP地址找到源侧eNodeB ID。 
通过S1口切换流程学习邻接关系：相邻eNodeB间无X2接口，或需变更MME，由源侧eNodeB发起到MME的流程，MME通过Handover Required消息获取目标侧eNodeB与源侧eNodeB之间的邻接关系。MME获取目标侧eNodeB ID方法：Handover Required消息中的Target ID即目标侧eNodeB ID。MME获取源eNodeB ID方法：Handover Required消息由源侧eNodeB发起，MME收到此消息后，将发送此消息的eNodeB作为源侧eNodeB，并根据IP地址找到源侧eNodeB ID。 
MME对中低速移动用户判断
MME对中低速移动用户判断，基于用户在最近驻留的eNodeB上驻留的时间。如果驻留的时间超过一定时长，就判定为中低速移动用户。 
业务流程 :该特性不涉及业务流程。 
系统影响 :该特性开启后，需要保存eNodeB间邻接关系，最大单VM需消耗200M左右内存。
MME通常需要约一周时间才能建立完整的eNodeB邻接关系表，此时长因网络环境不同会有差异。 
应用限制 :该特性不涉及应用限制。 
特性交互 :相关特性|交互关系
---|---
ZUF-78-09-002 智能寻呼|MME基于机器学习的智能寻呼，是在智能寻呼基础上的增强，必须提前开启智能寻呼功能。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|5.3.4.3 Network Triggered Service Request
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)"|8.5 Paging
特性能力 :名称|指标
---|---
单个eNodeB支持的最大邻接eNodeB数|64（个）
中心eNodeB和邻接eNodeB总数|192万（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.40|首次发布。
License要求 :该特性需要开启License，对应的License项目为“MME支持基于机器学习的智能寻呼”（license ID：7141），此项目显示为“支持”，标识MME支持基于机器学习的智能寻呼。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :开启本特性，对CMP所在的单VM最大可能需要额外消耗200M内存，请确认现网CMP所在单VM有足够的内存。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令eNB邻接关系配置ADD NEIGHBORENBDEL NEIGHBORENBDEL ALLNEIGHBORENBSHOW NEIGHBORENBMME全局寻呼策略配置SET NEIGHBOR ENB PAGING POLICYSHOW NEIGHBOR ENB PAGING POLICY 
修改配置项表2  修改配置项配置项命令修改参数MME寻呼策略配置ADD MME PS PAGING POLICY对于“寻呼方式”的枚举值：把“基于最近活动eNB列表寻呼”修改为“基于最近活动eNB列表或邻接eNB列表寻呼”。新增“eNB列表类型”，当寻呼方式为“基于最近活动eNB列表或邻接eNB列表寻呼”时有效。SET MME PS PAGING POLICYDEL MME PS PAGING POLICYSHOW MME PS PAGING POLICYADD MME CS PAGING POLICYSET MME CS PAGING POLICYDEL MME CS PAGING POLICYSHOW MME CS PAGING POLICYADD MME SMS PAGING POLICYSET MME SMS PAGING POLICYDEL  MME SMS PAGING POLICYSHOW MME SMS PAGING POLICYADD MME IDR PAGING POLICYSET MME IDR PAGING POLICYDEL  MME IDR PAGING POLICYADD MME IDR PAGING POLICYADD MME NBIOT PAGING POLICYSET MME NBIOT PAGING POLICYDEL  MME NBIOT PAGING POLICYSHOW MME NBIOT PAGING POLICY容灾恢复配置SET SERVRSTOCFG对于“寻呼方式”的枚举值：把“基于最近活动eNB列表寻呼”修改为“基于最近活动eNB列表或邻接eNB列表寻呼”。新增“eNB列表类型”，当寻呼方式为“基于最近活动eNB列表或邻接eNB列表寻呼”时有效。SHOW SERVRSTOCFGMME过负荷寻呼优化配置SET MME OVERLOAD PAGING POLICY对于“寻呼方式”的枚举值：把“基于最近活动eNB列表寻呼”修改为“基于最近活动eNB列表或邻接eNB列表寻呼”。新增“eNB列表类型”，当寻呼方式为“基于最近活动eNB列表或邻接eNB列表寻呼”时有效。SHOW MME OVERLOAD PAGING POLICY 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理表3  新增动态命令动态管理名称命令查询单个eNB邻接关系信息SHOW SINGLE ENB NEIGHBOR INFO 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :配置说明 :通过配置可以使用基于机器学习的智能寻呼功能，达到提升寻呼性能的目的。 
配置前提 :MME网元各项对接和业务配置完毕。 
配置过程 :场景一 :执行命令[SET NEIGHBOR ENB PAGING POLICY]命令，开启支持基于机器学习的智能寻呼功能。
执行命令[ADD MME PS PAGING POLICY]命令，新增数据业务寻呼策略。
执行命令[ADD MDNAL]命令，新增移动号码分析。
执行命令[ADD MME PAGING POLICY FACTOR]命令，新增MME寻呼策略因子。
场景二 :执行命令[SET NEIGHBOR ENB PAGING POLICY]命令，开启支持基于机器学习的智能寻呼功能。
执行命令[SET MME GLOBAL NBIOT PAGING POLICY]命令，设置全局的NB-IOT寻呼策略。
场景三 :执行命令[SET NEIGHBOR ENB PAGING POLICY]命令，开启支持基于机器学习的智能寻呼功能。
执行命令[ADD MME PS PAGING POLICY]命令，新增数据业务寻呼策略。
执行命令[ADD MDNAL]命令，新增移动号码分析。
执行命令[ADD MME PAGING POLICY FACTOR]命令，新增MME寻呼策略因子。
配置实例 :场景一 :场景说明
通用类业务的寻呼，如数据业务、信令。 
数据规划
配置项|参数名称|取值
---|---|---
修改邻接eNB寻呼策略|支持邻接eNB寻呼功能|是
新增数据业务寻呼策略|寻呼策略编号|55
寻呼类型|新增数据业务寻呼策略|自定义寻呼
寻呼策略|新增数据业务寻呼策略|参见表1。
新增移动号码分析|被分析号码|46011999
分析器入口|新增移动号码分析|IMSI寻呼策略分析
号码分析结果索引|新增移动号码分析|5
新增MME寻呼策略因子|IMSI/MSISDN号段索引|5
寻呼策略|新增MME寻呼策略因子|参见表2。
寻呼方式|寻呼时长(100ms)|寻呼优先级|eNB列表类型
---|---|---|---
最近一次活动eNB寻呼|50|N/A|最近活动eNB列表
最近活动eNB列表或邻接eNB列表寻呼|50|N/A|邻接eNB列表
GUTI在TA LIST范围寻呼|50|N/A|最近活动eNB列表
寻呼策略类型|策略编号
---|---
PS|55
配置步骤
步骤|说明|操作
---|---|---
1|开启支持基于机器学习的智能寻呼功能|SET NEIGHBOR ENB PAGING POLICY:SUPNEIENBPAGING="YES"
2|新增数据业务寻呼策略|ADD MME PS PAGING POLICY:ID=55,PAGETYPE=USER,PAGEPOLICY="LASTENB"-"50"-"PRIO_255"-"RECENBLIST"&"LASTENBLIST"-"50"-"PRIO_255"-"NEIGENBLIST"&"GUTITALIST"-"50"-"PRIO_255"-"RECENBLIST"
3|新增移动号码分析|ADD MDNAL:DGT="46011999",ENTR=DAS_IMSI_PGPOLICY,RST=5
4|新增MME寻呼策略因子|ADD MME PAGING POLICY FACTOR:USERNUMIDX=5,PGPOLICY="PS"-"55"
场景二 :场景说明
负荷敏感类业务的寻呼，如抄表业务。 
数据规划
配置项|参数名称|取值
---|---|---
修改邻接eNB寻呼策略|支持邻接eNB寻呼功能|是
设置NB-IoT业务全局寻呼策略|寻呼类型|自定义寻呼
寻呼策略|设置NB-IoT业务全局寻呼策略|参见表3。
寻呼方式|寻呼时长(100ms)|寻呼优先级|eNB列表类型
---|---|---|---
最近一次活动eNB寻呼|120|N/A|最近活动eNB列表
最近活动eNB列表或邻接eNB列表寻呼|120|N/A|邻接eNB列表
GUTI在TA LIST范围寻呼|120|N/A|最近活动eNB列表
配置步骤
步骤|说明|操作
---|---|---
1|开启支持基于机器学习的智能寻呼功能|SET NEIGHBOR ENB PAGING POLICY:SUPNEIENBPAGING="YES"
2|设置全局的NB-IOT寻呼策略|SET MME GLOBAL NBIOT PAGING POLICY:PAGETYPE=USER,PAGEPOLICY="LASTENB"-"120"-"PRIO_255"-"RECENBLIST"&"LASTENBLIST"-"120"-"PRIO_255"-"NEIGENBLIST"&"GUTITALIST"-"120"-"PRIO_255"-"RECENBLIST"
场景三 :场景说明
时延敏感业务类的寻呼，如语音。 
数据规划
配置项|参数名称|取值
---|---|---
修改邻接eNB寻呼策略|支持邻接eNB寻呼功能|是
新增数据业务寻呼策略|寻呼策略编号|55
寻呼类型|新增数据业务寻呼策略|自定义寻呼
寻呼策略|新增数据业务寻呼策略|参见表4。
新增移动号码分析|被分析号码|46011999
分析器入口|新增移动号码分析|IMSI寻呼策略分析
号码分析结果索引|新增移动号码分析|5
新增MME寻呼策略因子|IMSI/MSISDN号段索引|5
寻呼策略|新增MME寻呼策略因子|参见表5。
寻呼方式|寻呼时长(100ms)|寻呼优先级|eNB列表类型
---|---|---|---
最近活动eNB列表或邻接eNB列表寻呼|50|N/A|邻接eNB列表
GUTI在TA LIST范围寻呼|50|N/A|最近活动eNB列表
寻呼策略类型|策略编号
---|---
PS|55
配置步骤
步骤|说明|操作
---|---|---
1|开启支持基于机器学习的智能寻呼功能|SET NEIGHBOR ENB PAGING POLICY:SUPNEIENBPAGING="YES"
2|新增数据业务寻呼策略|ADD MME PS PAGING POLICY:ID=55,PAGETYPE=USER,PAGEPOLICY="LASTENBLIST"-"50"-"PRIO_255"-"NEIGENBLIST"&"GUTITALIST"-"50"-"PRIO_255"-"RECENBLIST"
3|新增移动号码分析|ADD MDNAL:DGT="46011999",ENTR=DAS_IMSI_PGPOLICY,RST=5
4|新增MME寻呼策略因子|ADD MME PAGING POLICY FACTOR:USERNUMIDX=5,PGPOLICY="PS"-"55"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|MME支持基于机器学习的智能寻呼，普通用户能够使用邻接eNodeB进行寻呼
---|---
测试目的|测试普通用户能够使用邻接eNodeB进行寻呼。
预置条件|MME与各网元对接成功，eNodeB1、eNodeB2都归属TA1和TA2。开启支持邻接eNodeB寻呼功能。新增PS寻呼策略，对应命令：ADD MME PS PAGING POLICY:ID=55,PAGETYPE=USER,PAGEPOLICY="LASTENB"-"50"-"PRIO_255"-"RECENBLIST"&"LASTENBLIST"-"50"-"PRIO_255"-"NEIGENBLIST"&"GUTITALIST"-"50"-"PRIO_255"-"RECENBLIST"。针对46011999号段，增加号码分析索引，对应命令：ADD MDNAL:DGT="46011999",ENTR=DAS_IMSI_PGPOLICY,RST=5。设置46011999号段的用户使用新增的寻呼策略，对应命令：ADD MME PAGING POLICY FACTOR:USERNUMIDX=5,PGPOLICY="PS"-"55"。
测试过程|46011999号段的用户从eNodeB1附着上线。eNodeB2发起TAU流程，分配的TA List为TA1和TA2。释放S1连接后，用户进入IDLE态。MME收到SGW下行数据通知，触发MME寻呼用户。
通过准则|MME共发起了三轮寻呼。第一轮只向eNodeB2发送寻呼消息。第二轮分别向eNodeB1、eNodeB2发送寻呼消息。第三轮分别向eNodeB1、eNodeB2发送寻呼消息。
测试结果|–
测试项目|MME支持基于机器学习的智能寻呼，NB用户能够使用邻接eNodeB进行寻呼
---|---
测试目的|测试NB用户能够使用邻接eNodeB进行寻呼。
预置条件|MME与各网元对接成功，eNodeB1、eNodeB2都归属TA1和TA2，并且RAT类型都是“NB”。开启支持邻接eNodeB寻呼功能。新增NB-IoT寻呼策略，对应命令：SET MME GLOBAL NBIOT PAGING POLICY:PAGETYPE=USER,PAGEPOLICY="LASTENB"-"120"-"PRIO_255"-"RECENBLIST"&"LASTENBLIST"-"120"-"PRIO_255"-"NEIGENBLIST"&"GUTITALIST"-"120"-"PRIO_255"-"RECENBLIST"。
测试过程|NB用户从eNodeB1附着上线。eNodeB2发起TAU流程，分配的TA List为TA1和TA2。释放S1连接后，用户进入IDLE态。MME收到SGW下行数据通知，触发MME寻呼用户。
通过准则|MME共发起了三轮寻呼。第一轮只向eNodeB2发送寻呼消息。第二轮分别向eNodeB1、eNodeB2发送寻呼消息。第三轮分别向eNodeB1、eNodeB2发送寻呼消息。
测试结果|–
测试项目|MME支持基于机器学习的智能寻呼，用户语音业务能够使用邻接eNodeB进行寻呼
---|---
测试目的|测试用户语音业务能够使用邻接eNodeB进行寻呼
预置条件|MME与各网元对接成功，eNodeB1、eNodeB2都归属TA1和TA2。开启支持邻接eNodeB寻呼功能。新增PS寻呼策略，对应命令：ADD MME PS PAGING POLICY:ID=55,PAGETYPE=USER,PAGEPOLICY="LASTENB"-"50"-"PRIO_255"-"RECENBLIST"&"LASTENBLIST"-"50"-"PRIO_255"-"NEIGENBLIST"&"GUTITALIST"-"50"-"PRIO_255"-"RECENBLIST"。针对46011999号段，增加号码分析索引，对应命令：ADD MDNAL:DGT="46011999",ENTR=DAS_IMSI_PGPOLICY,RST=5。设置46011999号段的用户使用新增的寻呼策略，对应命令：ADD MME PAGING POLICY FACTOR:USERNUMIDX=5,PGPOLICY="PS"-"55"。
测试过程|46011999号段的用户从eNodeB1附着上线。eNodeB2发起TAU流程，分配的TA List为TA1和TA2。释放S1连接后，用户进入IDLE态。SGW触发建立专有承载，触发MME寻呼用户。
通过准则|MME共发起了三轮寻呼。第一轮只向eNodeB2发送寻呼消息。第二轮分别向eNodeB1、eNodeB2发送寻呼消息。第三轮分别向eNodeB1、eNodeB2发送寻呼消息。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## BSSGP 
Base Station System GPRS ProtocolGPRS基站子系统协议
## CS 
Circuit Service电路域业务应用
## CSG 
Closed Subscriber Group闭合用户组
E-UTRAN :Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
## EPLMN 
Equivalent Public Land Mobile Network对等公用陆地移动网
## GERAN 
GSM/EDGE Radio Access NetworkGSM/EDGE无线接入网
GTP :GPRS Tunneling ProtocolGPRS隧道协议
## GUMMEI 
Globally Unique MME Identifier全球唯一移动性管理实体标识
GUTI :Globally Unique Temporary Identity全球唯一临时标识
IMEI :International Mobile Equipment Identity国际移动设备标识
## IMEISV 
International Mobile Equipment Identity and Software Version number国际移动设备识别码和软件版本号
IMSI :International Mobile Subscriber Identity国际移动用户标识
MME :Mobility Management Entity移动管理实体
## MOCN 
Multi-Operator Core Network多运营商核心网
MSC :Mobile Switching Center移动交换中心
## NACC 
Network Assisted Cell Change网络辅助小区式切换
## NITZ 
Network Identity and Time Zone网络标志和时区
PLMN :Public Land Mobile Network公共陆地移动网
RAN :Radio Access Network无线接入网
## RANAP 
Radio Access Network Application Protocol无线接入网应用协议
## RIM 
RAN Information Management无线接入网络信息管理
RAN Information ManagementRAN信息管理
## S1AP 
S1 Application ProtocolS1应用协议
SGW :Serving Gateway服务网关
## SI3 
System Information 3系统信息3
## SON 
Self-Organizing Network自组织网络
TA :Tracking Area跟踪区域
UTRAN :Universal Terrestrial Radio Access Network通用地面无线接入网络
VM :Virtual Machine虚拟机
## VoLTE 
Voice over LTELTE语音
# ZUF-78-10 APN 
概述 :功能描述 :APN是用户通过手机上网时必须配置的一个参数，它决定了用户的手机通过哪种接入方式来访问网络，同时在骨干网中用来标识要使用的外部PDN网络。APN由以下两部分组成： 
网络标识：这部分必选，是由网络运营者分配给ISP（互联网服务提供商，Internet Service Provider）或公司的，与其固定Internet域名一样的一个标识。 
运营商标识：这部分可选，其形式为“xxx.yyy.gprs”（如MNC.MCC.gprs）或”xxx.yyy.3gppnetwork.org”（ MNC.MCC. 3gppnetwork.org），用于标识归属网络。 
功能特性简介 :针对APN的应用场景，核心网提供了可靠、有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
APN更正|在UE的PDN请求中没有携带APN或请求APN不合法时，MME根据APN更正配置的策略更正为其他APN，用户使用更正后的APN激活EPS承载上下文访问数据业务和其他业务。MME支持基于IMSI号段确定APN更正方式，APN更正方式包括：MME上配置的APN。HSS签约的默认APN。|ZUF-78-10-001 APN更正
APN扩展|运营商在部署PGW时，可能需要考虑用户的号码和签约计费特性等因素。在APN NI中扩展用户信息，可以为运营商提供更准确的APN选择PGW的策略。MME判断是否对APN进行扩展的依据包括：用户号段（IMSI或MSISDN）APNAPN和用户号段是否漫游计费特性扩展的信息包括：用户IMSI号码段用户MSISDN号码段计费特性计费特性和IMSI号码段计费特性和MSISDN号码段IMEI号码段计费特性和IMEI号码段MME用扩展后的APN去构造FQDN进行解析，用于选择PGW。|ZUF-78-10-002 APN扩展
APN-OI替换|APN-OI替换是将APN OI替换为签约的APN-OI Repalcement，并通过解析得到PGW，仅用于归属网络的PGW选择。用户签约的APN-OI Replacement的级别可以分为：APN级APN-OI replacementUE级APN-OI replacementAPN级的APN-OI replacement优先级高于UE级的APN-OI replacement。APN-OI replacement具体定义可参见3GPP 29.272协议的“7.3.32 APN-OI-Replacement”章节。|ZUF-78-10-003 APN-OI替换
APN Restriction功能|MME比较PDN GW返回每个承载上下文建立消息中的APN Restriction值与保存的Maximum APN Restriction，MME需要根据Maximum APN Restriction限制PDN的连接请求。|ZUF-78-10-004 APN-OI限制功能
APN接入控制|MME支持APN黑白名单功能，便于限制漫游用户的接入。APN白名单：MME基于IMSI/PLMN配置许可APN。如果用户未签约许可APN，APN拒绝该用户的接入。APN黑名单：MME基于IMSI/PLMN配置禁止接入的APN。如果用户签约禁止接入的APN，MME拒绝该用户的接入。|ZUF-78-10-005 APN接入控制
PGW的APN拥塞控制|PGW在Create Session Failure消息中指示失败原因为“APN congestion”，并携带PGW退避时间（ Back-Off Time）。在退避时间内，MME对于相同APN的会话不选择该PGW，包括附着和创建PDN连接。当拥塞解除后，该PGW恢复为可选状态。具体参见3GPP 23.401协议的“ 4.3.7.5 PDN GW control of overload”章节。|ZUF-78-10-006 PGW的APN拥塞控制
## ZUF-78-10-001 APN更正 
特性描述 :特性描述 :描述 :定义 :MME网元APN更正是指，当用户接入EPC网络时，如果请求消息中携带的APN不合法，则MME对用户使用的APN按运营商的策略更正为其他APN，用户使用更正后的APN激活EPS承载上下文访问数据业务和其他业务。 
APN不合法通常是用户请求的APN和签约的APN不匹配，也可能是用户请求的APN格式错误。 
背景知识 :APN是用户通过手机上网时必须配置的一个参数，它决定了用户的手机通过哪种接入方式来访问网络，在骨干网中用来标识要使用的外部PDN网络。APN由以下两部分组成： 
网络标识：这部分必选，是由网络运营者分配给ISP（互联网服务提供商，Internet Service Provider）或公司的、与其固定Internet域名一样的一个标识。 
运营商标识：这部分可选，其形式为“xxx.yyy.gprs”（如MNC.MCC.gprs）或”xxx.yyy.3gppnetwork.org”（
MNC.MCC. 3gppnetwork.org），用于标识归属网络。 
当运营商间互相吞并或其他原因导致用户转网，如果用户原来的APN和转网后签约的APN不再匹配，则需要更正APN；而有些终端的APN是无法更正的，有些终端的APN虽然可以更正但不容易操作，因此运营商需要MME对某些号段的用户按照一定的策略更正APN。 
APN更正就是对网络标识的更正。APN网络标识通常作为用户签约数据存储在HSS中，用户在发起分组业务时也可向MME提供APN。MME根据APN通过DNS或本地域名解析得到PGW的IP地址。 
MME/SGSN都支持APN更正，MME支持2种APN更正方式，SGSN支持4种APN更正方式，参见下表。 
网元APN更正|APN更正方式
---|---
MME APN更正|指定APNMME根据用户IMSI号段对原来的APN进行更正，用更正后的APN进行PGW地址查询。HSS签约的默认APNMME根据用户IMSI号段用HSS签约的默认APN进行PGW地址查询。
SGSN APN更正|指定APNSGSN根据用户IMSI号段对原来的APN进行更正，用更正后的APN进行GGSN地址查询。更正为签约的第一个APNSGSN根据用户IMSI号段对原来的APN进行更正，用HLR签约信息中的第一个APN作为更正后的APN，如果签约的第一个APN为“*”，则使用“指定APN”作为更正后的APN。APN模糊匹配SGSN根据用户IMSI号段对原来的APN进行更正，SGSN先检查“指定APN”是否为HLR签约APN，如果是，则将原APN更正为“指定APN”；如果不是，则使用HLR签约信息中的第一个APN作为更正后的APN，如果签约的第一个APN为“*”，则使用“指定APN”作为更正后的APN。请求APN更正SGSN根据用户IMSI号段对原来的APN进行更正，SGSN先检查用户请求的APN（即原APN）是否为HLR的签约APN。如果是，则使用该用户请求的APN；如果不是，则使用HLR签约信息中的第一个APN作为更正后的APN，如果签约的第一个APN为“*”，则使用“指定APN”作为更正后的APN。
应用场景 :MME支持2种APN更正方式：“指定APN”和“HSS签约的默认APN”。这2种更正方式的使用场景如下面两节描述。 
###### APN更正为“指定APN” 
APN更正为“指定APN”的场景根据用户是否漫游又细分为如下两种场景。 
漫游用户对漫游用户来说，跨国或跨网运营商拥有多个网络，如果用户漫游到属于运营商的另外一个网络，运营商会要求用户拜访地接入，因为同一运营商的多个网络间不存在运营商间漫游计费结算的需要。这种场景下如果请求消息中携带的APN不合法，则MME对此类漫游号段的用户的APN使用更正方式“指定APN”。漫游用户APN更正应用场景如下图所示。 
本地用户对本地用户来说，用户都是本地接入，如果运营商认为HSS签约的默认APN可能会变更或不适合用于更正的APN，在请求消息中携带的APN不合法时，MME对本地号段用户的APN使用更正方式“指定APN”。本地用户APN更正应用场景如下图所示。 
综上所述，漫游用户或本地用户在EPC网络激活时，如果请求消息中携带的APN不合法，则MME根据用户的IMSI对原来APN
NI进行更正，使用指定的APN进行PGW地址查询，激活EPS承载上下文访问数据业务和其他业务。 
###### APN更正为“HSS签约的默认APN” 
APN更正为“HSS签约的默认APN”的场景根据用户是否漫游又细分为如下两种场景。 
漫游用户对漫游用户来说，非跨国或非跨网运营商一般要求用户回归属地接入，以便于收费和监控，这种场景下如果请求消息中携带的APN不合法，则MME对此类漫游号段的用户的APN使用更正方式“HSS签约的默认APN”。漫游用户APN更正应用场景如下图所示。 
本地用户对本地用户来说，用户都是本地接入，考虑尽可能减少DNS上的数据配置，如果请求消息中携带的APN不合法，则一般MME对本地号段用户的APN使用更正方式“HSS签约的默认APN”。本地用户APN更正应用场景如下图所示。 
综上所述，漫游用户或本地用户在EPC网络激活时，如果请求消息中携带的APN不合法，则MME根据用户的IMSI决策使用HSS签约的默认APN进行PGW地址查询，激活EPS承载上下文访问数据业务和其他业务。 
一种特殊场景说明：MME根据用户IMSI号段使用APN更正方式“指定APN”，如果指定APN没有签约，则MME会改用APN更正方式“HSS签约的默认APN”。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户接入成功率，提高用户使用数据业务和其他业务的成功率，从而提升用户对移动网络的满意度。
移动用户|享受优质的网络服务。
实现原理 :涉及的网元 :网元名称|网元作用
---|---
MME|附着和PDN连接请求流程中，MME检查APN失败，对用户使用的APN进行更正，使用更正后的APN进行PGW地址查询，激活EPS承载上下文访问数据业务和其他业务。
HSS|在APN更正功能中，HSS需要为用户提供签约的默认APN。
业务流程 :MME在附着和UE请求PDN连接请求流程中进行APN更正。 
附着流程
流程描述： 
UE发送附着请求消息给eNodeB，请求消息中携带的APN不合法。 
eNodeB发送附着请求消息给MME。 
MME收到附着请求，发送更新位置请求消息给HSS。 
HSS发送更新位置应答消息给MME，消息中携带IMSI和签约数据，包括签约的默认APN。 
执行APN更正。 
MME进行APN检查，如果APN检查失败且APN更正功能启用，则MME根据用户的IMSI对用户使用的APN进行更正。 
MME APN更正方式有两种：“指定APN”和“HSS签约的默认APN”。 
如果使用“指定APN”更正方式，则MME使用指定的APN进行更正，并使用更正后的APN构造APN-FQDN发起DNS查询或本地查询获取GW列表。 
如果使用“HSS签约的默认APN”更正方式，则MME使用HSS签约的默认APN进行更正，并使用更正后的APN构造APN-FQDN发起DNS查询或本地查询获取GW列表。 
DNS返回查询到GW列表或本地查询到GW列表。 
MME根据GW选择策略选择得到SGW和PGW，MME向SGW发送创建会话请求消息并携带已选择的PGW地址。 
SGW根据创建会话请求消息中的GW地址向PGW发送创建会话请求消息。SGW根据创建会话请求消息中的GW地址向PGW发送创建会话请求消息。 
继续附着其他处理过程。 
UE请求PDN连接流程
流程图说明如下。 
UE发起PDN连接请求，请求消息中携带的APN不合法。 
执行APN更正。 
MME收到UE发起的PDN连接请求，进行APN检查，如果APN检查失败且APN更正功能启用，则MME根据用户的IMSI对用户使用的APN进行更正。 
MME APN更正方式有两种：“指定APN”和“HSS签约的默认APN”。 
如果使用“指定APN” 更正方式，则MME使用指定的APN进行更正，并使用更正后的APN构造APN-FQDN发起DNS查询或本地查询获取GW列表。 
如果使用“HSS签约的默认APN”更正方式，则MME使用HSS签约的默认APN进行更正，并使用更正后的APN构造APN-FQDN发起DNS查询或本地查询获取GW列表。 
DNS返回查询到GW列表或本地查询到GW列表。 
MME根据GW选择策略选择得到SGW和PGW，MME向SGW发送创建会话请求消息并携带已选择的PGW地址。 
SGW根据创建会话请求消息中的GW地址向PGW发送创建会话请求消息。SGW根据创建会话请求消息中的GW地址向PGW发送创建会话请求消息。 
继续UE请求PDN连接其他处理过程。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :不涉及。 
特性能力 :名称|指标
---|---
支持APN拥塞控制的最大APN个数|256
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :本特性中的MME支持签约通配的APN更正功能需要LICENSE许可后才能获得，对应的License控制项编号为7070。 
对其他网元的要求 :UE|eNodeB|MME|HSS
---|---|---|---
-|-|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :要求HSS提供用户签约的默认APN。 
本地用户或跨国或跨网运营商的漫游用户的APN使用更正方式“指定APN”时，要求DNS上具备更正后的APN域名到PGW的解析数据。 
O&M相关 :命令 :配置项|命令
---|---
支持APN更正功能开关|SET MME APNMOD POLICY
SHOW MME APNMOD POLICY|支持APN更正功能开关
配置APN控制更正策略|ADD MME APN MODIFY POLICY
配置APN更正方式|ADD MME APN MODIFICATION
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置使得ZXUN uMAC可以执行相应的APN更正功能。
配置前提 :HSS提供用户签约的默认APN。 
本地用户或跨国或跨网运营商的漫游用户使用APN更正为“指定APN”的方式时，DNS上要具备更正后的APN域名到PGW的解析数据。 
配置过程 :使用[SET MME APNMOD POLICY]，配置ZXUN uMAC支持APN更正。
使用[ADD MME APN MODIFICATION]，配置某用户IMSI号段使用的APN更正方式。
配置实例 :##### APN更正为“指定APN” 
场景说明 :跨国或跨网运营商拥有多个网络时，针对漫游用户（IMSI开头为46011）访问网络时的APN更正方式需要设置为指定APN，指定的APN名称为zte.com。
配置步骤 :设置支持APN更正。 
[SET MME APNMOD POLICY]:APNMODIFY="YES"
配置APN更正方式为“指定APN”。 
[ADD MME APN MODIFICATION]:IMSI="46011",SUBWILDCHK="IGNORE",MODIFYMODE="Specified APN",APN="zte.com"
##### APN更正为“HSS签约的默认APN” 
场景说明 :非跨国或非跨网运营商拥有多个网络时，针对漫游用户（IMSI开头为46011）的APN更正方式需要设置为HSS签约的默认APN。
配置步骤 :设置支持APN更正。 
[SET MME APNMOD POLICY]:APNMODIFY="YES"
配置APN更正方式为“HSS签约的默认APN”。 
[ADD MME APN MODIFICATION]:IMSI="46011",SUBWILDCHK="IGNORE",MODIFYMODE="Default APN Signed
by HSS"
调整特性 :无。 
测试用例 :###### APN更正为指定APN 
测试项目|APN更正为指定APN。
---|---
测试目的|验证MME中检查不合法的APN可以更正为指定APN。
预置条件|用户在HSS中签约zte.com，IPV4类型，且不为默认APN，未签约zte.net。配置支持MME APN更正，且更正为名称为zte.com的APN，“用户是否签约通配”为“忽略”。
测试过程|用户附着建立PDN连接，请求的APN是zte.net，IPV4类型。
通过准则|使用zte.com为该用户建立PDN连接，检查发给SGW的APN为zte.com。
测试结果|–
###### APN更正为HSS签约的默认APN 
测试项目|APN更正为HSS签约的默认APN。
---|---
测试目的|验证MME中检查不合法的APN可以更正为HSS签约的默认APN。
预置条件|用户在HSS中签约zte.default，IPV4类型，默认APN，未签约zte.net。配置支持MME APN更正，且更正为HSS签约的默认APN，“用户是否签约通配”为“忽略”。
测试过程|用户附着建立PDN连接，请求的APN是zte.net，IPV4类型。
通过准则|使用zte.default为该用户建立PDN连接，检查发给SGW的APN为zte.default。
测试结果|–
常见问题处理 :无。 
## ZUF-78-10-002 APN扩展 
特性描述 :特性描述 :术语 :术语|含义
---|---
APN扩展|在原APN上增加新的信息
APN转换|替换原APN中的信息。
APN更正|修改原APN中不正确的信息
描述 :定义 :APN扩展是指MME在使用APN进行PGW选择时，对使用的APN（如果有APN更正或APN转换，则为更正后的APN或转换后的APN）根据配置的扩展方法对APN NI进行扩展。然后用扩展后的APN 获取服务的PGW，所以扩展目的为了更准确地获取到本次服务的PGW。
背景知识 :运营商在部署PGW时，有可能需要考虑用户的号码和签约计费特性等，如不同计费特性在不同PGW。在APN NI中扩展用户信息，可以为运营商提供更准确的PGW选择策略，从而运营商可以更灵活的规划网络。 
应用场景 :APN转换功能的应用场景如下： 
场景一：基于IMSI扩展APN的场景当根据IMSI段来区分不同PGW时，配置IMSI段的APN扩展。 
场景二：基于MSISDN扩展APN的场景当根据MSISDN段来区分不同PGW时，配置MSISDN段的APN扩展。 
场景三：基于IMEI扩展APN的场景当根据IMEI段来区分不同PGW时，配置IMEI段的APN扩展。 
场景四：基于计费特性扩展APN的场景当需要根据计费特性来区分不同PGW，配置APN对应的计费特性扩展。 
场景五：基于IMSI号段和计费特性扩展APN的场景当需要根据IMSI号段和计费特性来区分不同PGW时，则配置IMSI号段+计费特性的APN扩展。 
场景六：基于MSISDN号段和计费特性扩展APN的场景当需要根据MSISDN号段和计费特性来区分不同PGW时，配置MSISDN号段+计费特性的APN扩展。 
场景七：基于IMEI号段和计费特性扩展APN的场景当需要根据IMEI号段和计费特性来区分不同PGW时，配置IMEI号段+计费特性的APN扩展。 
场景八：基于TA信息扩展APN的场景当需要根据TA信息来区分不同PGW时，配置TA信息的APN扩展。 
客户收益 :收益者|收益描述
---|---
运营商|组网灵活，扩容方便。
终端用户|该特性对终端用户不可见。
实现原理 :涉及的网元 :为本网元的功能，无网元间作用。 
本网元实现 :MME根据如下信息确定是否对APN进行扩展： 
用户号段（IMSI或MSISDN） 
APN 
是否漫游 
计费特性 
扩展的信息包括： 
用户IMSI号码段 
用户MSISDN号码段 
计费特性 
计费特性和IMSI号码段 
计费特性和MSISDN号码段 
用户IMEI号码段 
计费特性和IMEI号码段 
在扩展APN的DNS解析失败后是否使用非扩展APN解析可以使用开关来控制，“本地HOST解析失败后是否使用非扩展APN解析”开关和“扩展APN解析失败后是否使用非扩展APN解析”开关，使用场景如下： 
“本地HOST解析失败后是否使用非扩展APN解析”开关，用于设置当MME使用扩展APN在本地解析PGW地址失败后，是否使用非扩展APN继续尝试解析PGW地址。 
“扩展APN解析失败后是否使用非扩展APN解析”开关，用于设置当MME使用扩展APN在本地解析和DNS解析PGW地址都失败后，是否使用非扩展APN继续尝试解析PGW地址。 
当软件参数“MME地址解析优先级”（ID：65593）取值为0-Host Local->DNS Cache->DNS Server或者1-Host Local->DNS Server时：  “扩展APN解析失败后是否使用非扩展APN解析”设置为“是”，根据该配置使用扩展APN在本地解析和DNS解析PGW地址都失败后，再使用非扩展APN继续尝试解析PGW地址。“扩展APN解析失败后是否使用非扩展APN解析”设置为“否”，根据“本地HOST解析失败后是否使用非扩展APN解析”控制使用扩展APN解析失败是否使用非扩展APN继续尝试解析。 
当软件参数“MME地址解析优先级”（ID：65593）取值为2-DNS Cache->DNS Server->Host Local或者3-DNS Server->Host Local时，仅使用“本地HOST解析失败后是否使用非扩展APN解析”开关控制使用扩展APN解析失败是否使用非扩展APN继续尝试解析。 
ZXUN uMAC可以设置对漫游用户是否进行APN扩展，可以设置当基于CC+IMEI扩展解析失败后是否支持CC扩展。
业务流程 :APN处理过程的完整流程如[图1]。
图1  APN处理流程

MME的扩展流程如[图2]所示。
图2  MME的APN扩展流程

系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准类别|标准名称|章节
---|---|---
3GPP|3GPP TS 23.060: " General Packet Radio Service (GPRS); Servicedescription "|Stage 1
特性能力 :规格|指标
---|---
APN扩展表容量|2048
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.22.20|新增基于TA和APN解析PGW。
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性对应的License项目为MME支持基于TA和APN解析PGW，此项目显示为支持，表示支持基于TA和APN解析PGW。
对其他网元的要求 :UE|MME|eNodeB|SGW
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :命令名称|描述
---|---
ADD SOFTWARE PARAMETER|增加软件参数配置
SET SOFTWARE PARAMETER|设置软件参数配置
DEL SOFTWARE PARAMETER|删除软件参数配置
SHOW SOFTWARE PARAMETER|查询软件参数配置
ADD EPC EXAPN|新增EPC扩展APN配置
SET EPC EXAPN|修改EPC扩展APN配置
DEL EPC EXAPN|删除EPC扩展APN配置
SHOW EPC EXAPN|查询EPC扩展APN配置
ADD TA|新增跟踪区配置
SET TA|修改跟踪区配置
DEL TA|删除跟踪区配置
SHOW TA|查询跟踪区配置
性能统计 :该特性不涉及计数器。 
告警和通知 :该特性不涉及告警和通知消息。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察。 
话单与计费 :该特性不涉及话单与计费。 
特性配置 :特性配置 :配置说明 :本节介绍如何配置APN扩展特性。 
配置前提 :网管客户端和服务器间能够正常通信。 
配置过程 :场景一 :设置根据计费特性的名称进行扩展 
在命令终端使用[SET SOFTWARE PARAMETER]命令。
设置基于MSISDN进行APN扩展 
在命令终端使用[SET SOFTWARE PARAMETER]命令，配置APN转换。
APN扩展配置 
在命令终端使用[ADD EPC EXAPN]命令，配置扩展APN。
场景二 :设置APN扩展跟踪区组名称 
在命令终端使用[SET TA]命令，配置APN扩展跟踪区组名称。
APN扩展配置 
在命令终端使用[ADD EPC EXAPN]命令，配置扩展APN。
配置实例 :场景一 :场景说明
IMSI号码为8613700006001的用户在HSS中签约的APN为test.com，PDN Type为IPv4，签约的第一个APN对应的计费特性为normal（普通计费），需要将创建会话请求的test.com转换成zte.com.normal.86137。 
数据规划
配置项|参数|取值
---|---|---
软件参数配置|软件参数ID|786485
软件参数值|软件参数配置|0
软件参数ID|软件参数配置|786485
软件参数值|软件参数配置|1
EPC扩展APN配置|APN名称|zte.com
IMSI/MSISDN号段|EPC扩展APN配置|8613700006001
扩展方式|EPC扩展APN配置|签约计费特性+MSISDN扩展
APN扩展位|EPC扩展APN配置|1-5
配置步骤
配置步骤|解释说明|配置脚本
---|---|---
1|配置软参根据计费特性的名称进行扩展。|SET SOFTWARE PARAMETER:PARAID=786485,PARAVALUE=0
2|配置软参基于MSISDN进行扩展。|SET SOFTWARE PARAMETER:PARAID=786565,PARAVALUE=1
3|配置APN扩展。|ADD EPC EXAPN:APNNAME="zte.com",IMSI="8613700006001",NUMBERTYPE="CHARGE+MSISDN",EXBIT=1-5
场景二 :场景说明
IMSI号码为8613700006001的用户在HSS中签约的APN为test.com，PDN Type为IPv4，对应的跟踪区配置了APN扩展跟踪区组名称。 
数据规划
配置项|参数|取值
---|---|---
跟踪区配置|跟踪区标识|1
APN扩展跟踪区组名称|跟踪区配置|gd.gzdq
EPC扩展APN配置|APN名称|zte.com
扩展方式|EPC扩展APN配置|TA信息扩展
TA信息扩展格式|EPC扩展APN配置|扩展TA组
配置步骤
配置步骤|解释说明|配置脚本
---|---|---
1|配置APN扩展跟踪区组名称，作为扩展到APN-FQDN的TA信息。|SET TA:TAID=1,APNEXTTAG="gd.gzdq"
2|配置APN扩展。|ADD EPC EXAPN:APNNAME="zte.com",NUMBERTYPE="TAINFOEXT",TAINFOFORMAT="TAGROUP"
测试用例 :测试项目|基于MSISDN的APN扩展
---|---
测试目的|验证基于MSISDN的APN扩展功能
预置条件|系统运行正常。设置软件参数786565“扩展APN的号码类型”为1（MSISDN）。配置APN+MSISDN的APN扩展，扩展模式是计费特性+MSISDN。
测试过程|使用配置号段MSISDN内的用户附着，使用APN激活。
通过准则|用户匹配到APN扩展中APN+MSISDN的记录，并且扩展方式是计费特性+MSISDN。
测试项目|基于TA信息的APN扩展
---|---
测试目的|验证基于TA信息的APN扩展功能
预置条件|打开License开关，uMAC_MME_7142 MME支持基于TA和APN解析PGW。配置APN扩展跟踪区组名称。配置APN扩展，扩展模式基于TA信息。
测试过程|使用配置的APN用户附着，使用APN激活。
通过准则|用户匹配到APN扩展中APN的记录，并且扩展方式是基于TA信息。
## ZUF-78-10-003 APN-OI替换 
概述 :当在非漫游场景和归属路由器漫游场景下构造APN和APN-FQDN用于DNS解析时，APN-OI Replacement功能用于使用域名来替换APN OI。 
收益 :APN-OI Replacement功能提高系统灵活性。 
根据APN-OI-Replacement字段，运营商可为相同APN使用不同的PGW。 
描述 :APN-OI Replacement指的是用签约APN-OI Replacement替换APN OI，并通过分析获取PGW。只用于在归属网络中用于选择PGW。 
签约APN-OI Replacement分为以下几级： 
APN级APN-OI Replacement 
UE级APN-OI Replacement 
APN级的APN-OI Replacement优先级高于UE级的APN-OI Replacement。 
## ZUF-78-10-004 APN-OI限制功能 
概述 :ZXUN uMAC（MME）可根据最大APN限制配置限制PDN连接。 
收益 :本功能用于决定是否允许一个MS建立多个EPS承载到其他APN。 
描述 :MME可支持最大APN限制。当MME收到APN限制值，MME保存该值用于承载上下文，并且将接收的最大APN限制值与保存的相比较，以确定两者之间没有冲突。如果检查结果导致PDN连接请求被拒绝，MME应发起承载去激活，并返回适当的错误原因。如果PDN连接请求被接受，MME应确定一个新的最大APN限制值。如果之前没有保存的最大APN限制值，MME将接收到的最大APN限制值保存为该值。  
APN限制值如下： 
最大APN限制值|APN类型|应用示例|允许建立的APN限制值
---|---|---|---
0|无现有上下文或限制|All|无现有上下文或限制
1|Public-1|WAP或MMS|1、2、3
2|Public-2|Internet或PSPDN|1、2
3|Private-1|公司（例如：使用MMS的公司）|1
4|Private-2|公司（例如：不使用MMS的公司）|无
## ZUF-78-10-005 APN接入控制 
概述 :MME支持基于用户签约数据进行APN接入控制。 
收益 :运营商可仅签约特定APN漫游协议。 
运营商可基于签约APN判断是否为漫游用户，并限制用户接入。 
描述 :MME支持APN黑白名单功能，便于限制漫游用户的接入。 
APN白名单：MME基于IMSI/PLMN配置许可APN。如果用户未签约许可APN，APN拒绝该用户的接入。 
APN黑名单：MME基于IMSI/PLMN配置禁止接入的APN。如果用户签约禁止接入的APN，MME拒绝该用户的接入。 
## ZUF-78-10-006 PGW的APN拥塞控制 
概述 :当PGW发生APN拥塞，在APN退避期间，MME支持在APN选择过程中不选择拥塞PGW。 
收益 :提供负荷控制测量，避免由PGW阻塞导致的业务失败影响用户体验。 
描述 :在Create Session Failure消息中，PGW指示“APN
congestion”失败原因，并携带PGW退避时间。在退避时间内，MME不会为相同APN的会话选择该PGW，包括附着和创建PDN连接。当拥塞恢复后，该PGW恢复为可选状态。 
# 缩略语 
# 缩略语 
APN :Access Point Name接入点名称
FQDN :Fully Qualified Domain Name全称域名
IMEI :International Mobile Equipment Identity国际移动设备标识
MME :Mobility Management Entity移动管理实体
PGW :PDN Gateway分组数据网网关
# ZUF-78-11 QoS 
概述 :功能描述 :QoS指一个网络能够利用各种基础技术，为指定的网络通信提供更好的服务能力，是网络质量保证技术，用来为用户提供优质网络服务。无线通信网络有QoS要求，需要将IP QoS映射到承载QoS。 
功能特性简介 :QoS功能详细的特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
EPS QoS和Pre-Rel8 QoS的映射|当UE从2/3G网络切换到EPS网络，MME将Pre-R8 QoS映射到EPS QoS；当UE从EPS网络切换到2/3G网络，MME将EPS QoS映射到Pre-R8 QoS。从Pre-Rel8 QoS映射到EPS QoS时，EPS QoS ARP的 pre-emption capability和pre-emption vulnerability由MME本地配置控制。QoS速率最大支持10 Gbps。映射规则具体可参见3GPP 23.401协议的“Annex E Mapping between EPS and Release 99 QoS parameters”章节。|ZUF-78-11-001 EPS QoS和Pre-Rel8 QoS的映射
支持EPS Bear和PDP的映射功能|当UE从EPS网络切换到2/3G网络，MME进行EPS承载到PDP的映射；当UE从2/3G网络切换到EPS网络时，MME进行PDP到EPS承载的映射。映射规则具体可参见3GPP 23.060协议的“9.2.1A Principles for mapping between PDP Contexts and EPS Bearers”章节。|ZUF-78-11-002 支持EPS Bear和PDP的映射功能
扩展QCI|3GPP协议标准中QCI的取值是0~255（0为无效）。QCI取值为1~4的承载为GBR（Guaranteed Bit Rate，保证比特速率）类承载QCI取值为5~9的承载为Non-GBR类承载QCI取值为10~255由运营商自定义MME支持扩展QCI，将在全部携带有QoS参数的消息中的QCI值从10扩展到255。对于QCI值为10~255的承载，当承载中MBR（Maximum Bit Rate，最大比特速率）和GBR的值都为0时，表示该承载为Non-GBR类承载。MME支持取值为10~255的QCI到Pre-R8 QoS的映射可配置。|ZUF-78-11-003 扩展QCI
本地QoS策略|为了控制漫游用户带宽消耗，保障本网用户业务感受，需要MME能够进行本地QoS上限控制。MME支持基于IMSI、APN、QCI和ARP四个维度，实现用户级QoS参数控制（UE-AMBR）、会话级QoS参数控制（APN-AMBR）和承载级QoS参数控制（GBR承载：MBR、GBR）。具体参见3GPP 23.401协议的“4.7.2.1 The EPS bearer in general”章节。|ZUF-78-11-004 本地QoS策略
## ZUF-78-11-001 EPS QoS和Pre-Rel8 QoS的映射 
特性描述 :特性描述 :描述 :定义 :EPS QoS功能： EPS网络提供端到端的网络服务，为了实现端到端的QoS，EPS系统从业务的起点到业务的终点都建立和使用了具有明确定义属性和功能的承载业务，QoS控制的基本粒度是承载，即不同类型承载上的所有数据流获得不同的QoS保障。针对EPS无线接入网络共享信道机制的特点，EPS网络承载QoS处理取消了2/3G网络实体间复杂的QoS协商机制，采用PCC机制。 
在EPS PCC架构下，MME将用户签约的QoS传递给PGW和PCRF，再将PCRF/PGW决策的QoS传递给无线侧和UE，即MME在上下行方向传递QoS；对签约QoS较高的漫游用户，在PCRF/PGW下发决策的QoS后MME根据本地策略进行QoS控制，将限制后的QoS下发给无线侧和UE。 
背景知识 :EPS QoS架构
QoS指一个网络能够利用各种基础技术，为指定的网络通信提供更好的服务能力，是网络质量保证技术，用来为用户提供优质网络服务。无线通信网络有QoS要求，需要将IP
QoS映射到承载QoS，3GPP为QoS定义了一整套系统。 
3GPP QoS是一个端到端的概念，涉及到核心网、无线接入网和手机终端等。EPS的端到端承载架构如[图1]所示。
图1  EPS QoS架构图

EPS的承载业务（UE到PGW）是一个分段的结构，即通过核心网、无线侧分段的QoS机制实现整个EPS QoS保证机制。同时EPS承载的QoS机制又是一个分层的结构，即每一段的QoS承载业务是使用下层的承载业务提供的服务保证上层自己的QoS服务。 
EPS承载类型
EPS承载类型参见[表1]。
承载类型|特征|典型用户业务
---|---|---
Non-GBR承载|用于承载无QoS要求的业务，资源分配无硬性要求，优先级低。|网页浏览、位置服务、Email、FTP文件下载等业务属于交互类或背景类，此类业务一般不要求保障型速率。
GBR承载|用于承载需要带宽保证的业务，资源分配的硬性要求保证比特速率（GBR），比特速率上限（MBR），优先级通常高于Non-GBR业务。|语音、可视电话、视频点播（无交互）和音频点播等业务属于会话类或流类，此类业务一般要求保障型速率。
EPS QoS参数
EPS的QoS参数说明参见[表2]。
分类|参数|说明
---|---|---
承载QoS|QCI|QCI是一个标量，是特定接入节点控制（如eNodeB）承载级数据转发功能的QoS参数索引标志，其具体索引标志含义由运营商预配置到特定接入节点中。其具体含义由标准化的特征量表示（资源类型、优先级、分组迟延预算和分组丢失率）。其用来表示控制承载级别的数据包传输处理的接入点参数包括调度权重、接入门限、队列管理门限、链路层协议配置等。这些参数决定了无线侧承载资源的分配。标准QCI特性参见表3。
ARP|承载QoS|ARP用于在资源限制的情况下决定接受还是拒绝承载的建立或者修改请求，用于在特殊的资源限制时，决定丢弃哪个承载。包含有优先级（prioritylevel）、抢占能力标志（pre-emption capability）)和被抢占能力（pre-emption vulnerability）。priority level：具有1-15级别。数字越小优先级越高。 pre-emption capability：该承载能否抢占具有更低优先级的资源标示。pre-emption vulnerability：该承载资源能否被具有更高优先级的承载抢占标示。
GBR|承载QoS|GBR承载能够提供的保证比特率。
MBR|承载QoS|MBR承载能够提供的最大比特率（Rel-8中MBR＝GBR）
承载集合级QoS|APN-AMBR|一个APN所对应的所有PDN Connection的所有Non-GBR Bearer的集合的最大速率。
UE-AMBR|承载集合级QoS|UE的所有Non-GBR Bearer的集合对应的最大速率，只对eNB有效。MME计算UE-AMBR时，取该用户所有PDN连接的APN-AMBR之和，和用户的签约UE-AMBR中的较小者。
QCI|资源类型|优先级|数据时延|数据丢包率
---|---|---|---|---
1|GBR|2|100 ms|10-2
2|4|GBR|150 ms|10-3
3|3|GBR|50 ms|10-3
4|5|GBR|300 ms|10-6
5|Non-GBR|1|100 ms|10-6
6|6|Non-GBR|300 ms|10-6
7|7|Non-GBR|100 ms|10-3
8)|8|Non-GBR|300 ms|10-6
9|9|Non-GBR|300 ms|10-6
EPS QoS决策机制
EPS网络提供端到端的网络服务，针对EPS无线接入网络共享信道机制的特点，EPS网络承载QoS处理取消了2G/3G网络实体间复杂的QoS协商机制，采用PCC机制。 
EPS默认承载的QoS参数根据用户签约数据和网络策略确定，PCRF可以对其进行修改。 
EPS专有承载的QoS参数由PCRF或PGW决定，E-UTRAN不能修改网络决定的QoS参数。 
与Pre-8不同，EPS不支持E-UTRAN发起的QoS重协商，即EPS不支持eNodeB发起的承载修改流程。如果eNodeB不能够维持已激活的GBR承载的GBR，eNodeB必须发起这个承载的去活流程。 
客户收益 :受益方|受益描述
---|---
运营商|提高运营成本效益：QoS机制为网络运营商提供了优化网络资源的有效手段，使得网络运营商能以最少量的网络资源满足更多终端用户的需求。获得新的收入增长点：QoS机制可使网络运营商提供更多增值业务，提高终端用户的满意度和忠诚度。
移动用户|更好的用户体验：QoS机制使终端用户使用复杂的应用成为可能，这类应用通常其QoS需求较高，保证高端用户得到比低端用户更好的服务。无缝连接的用户体验：用户跨RAT移到过程中，网络提供4G和2/3G QoS参数间的映射，保证无缝连接的用户体验。
应用场景 :描述 :EPS QoS是基于承载的QoS管理，承载分为两类： 保障速率承载和非保障速率承载，分别对应保障速率用户业务和非保障速率用户业务。在EPS QoS的PCC机制下，MME将用户签约的QoS传递给PGW和PCRF，再将PCRF/PGW决策的QoS传递给无线侧和UE，即MME在上下行方向传递QoS。 
另外，用户会在4G和2/3G网络间移动，需要MME支持跨RAT的端到端QoS保障，即用户跨RAT移到过程中，MME能实现4G和2/3G QoS参数间的映射，保证无缝的用户体验。 
因此本特性有如下2个应用场景： 
QoS传递 
用户跨RAT移动时QoS参数映射 
###### QoS传递 
保障速率的用户业务
保障速率的用户业务一般是语音、可视电话、视频点播（无交互）和音频点播等业务，此类业务属于会话类或流类。应用场景如[图2]所示。
图2  保障速率的用户业务应用场景
UE：语音、视频或音频点播等。 
MME：传递QCI（会话类或流类）、MBR、GBR、UE-AMBR、APN-AMBR和ARP。 
eNodeB和SGW：为用户业务分配带宽，保证最小带宽为GBR。 
PGW：为用户业务分配带宽，保证最小带宽为GBR。 
PCRF：下发QCI（会话类或流类）、MBR、GBR和ARP。 
场景说明如下： 
用户进行保障速率型业务（如语音、可视电话、视频点播（无交互）和音频点播等）时，MME将用户签约的默认承载的QoS(包含QCI，ARP)和APN-AMBR传递给GW。 
PCRF分析并确定业务需要的QoS，PGW建立专有承载，或PGW判断已经建立的承载不能够满足业务需要的QoS发起专有GBR承载修改，将相应承载的QoS（包括QCI、MBR、GBR、ARP等）和APN-AMBR在专有承载创建或修改请求中带给SGW，SGW传递给MME。 
MME根据APN-AMBR重新计算UE-AMBR，再将承载QoS（QCI、MBR、GBR、ARP）、APN-AMBR和UE-AMBR信息传递给UE和eNodeB。 
eNodeB根据QoS参数中的GBR大小，预留资源，保证这个ERAB的最小带宽为GBR（最大带宽为MBR），为用户业务分配带宽。 
非保障速率的用户业务
非保障速率的用户业务一般是网页浏览、位置服务、Email、FTP文件下载等业务，此类业务属于交互类或背景类。应用场景如[图3]所示。
图3  非保障速率的用户业务应用场景
UE：网页浏览或Email、FTP文件下载等。 
MME：传递QCI（会话类或流类）、ARP、APN-AMBR和UE-AMBR。 
eNodeB和SGW：为用户业务分配带宽，保证最小带宽为NBR。 
PGW和PCRF：根据业务分析出需要的QCI、ARP和APN-AMBR。 
场景说明如下： 
用户进行非保障速率型业务（如网页浏览、位置服务、Email、FTP文件下载等）时，MME将用户签约的默认承载的QoS(包含QCI，ARP)和APN-AMBR传递给GW。 
PCRF分析并确定业务需要的QoS，PGW建立NON-GBR承载，或PGW判断当前已有承载不能够满足业务需要的QoS发起NON-GBR承载修改，PGW将相应的QoS（包括QCI、ARP）和APN-AMBR在承载创建请求或承载修改请求中带给SGW和MME。 
MME根据APN-AMBR重新计算UE-AMBR，再将承载QoS（QCI和ARP）、APN-AMBR和UE-AMBR信息传递给UE和eNodeB。 
eNodeB发现QoS参数中的GBR为0，根据UE-AMBR控制业务总带宽。UE根据APN-AMBR控制业务带宽等。 
###### 用户跨RAT移动时QoS参数映射 
用户从4G移动到2/3G网络，MME将EPS QoS映射为pre-Rel-8 QoS带给2/3G网络的SGSN局，提供跨RAT的端到端QoS保障。 
EPS QoS到Pre-R8 QoS的映射
ARPEPS QoS ARP 由Pre-Rel8 QoS ARP 一对一映射，参见表4。表4  EPS QoS到Pre-R8 QoS的映射EPSPre-Rel-8Bearer ARP Priority ValueARP Value1 to H1H+1 to M2M+1 to 153其中H以及M的值根据运营商的需求，在MME上可配置。 
MBR、GBR对于QCI为GBR的承载，MBR和GBR直接一对一映射。对于QCI为non-GBR的承载，按APN-AMBR除于该PDN连接下non-GBR承载个数进行映射（不能除尽时，取整）。 
Traffic Class、Traffic Handling Priority、Signalling Indication、Source Statistics DescriptorEPS QoS QCI和Pre-Rel8 QoS Traffic Class参数的映射，以及与Traffic Handling Priority、Signalling Indication、Source Statistics Descriptor的关系参见表5。表5  QCI与Pre-Rel8 QoS参数的映射GPRS的QoS等级标识值UMTS的QoS参数Traffic ClassTHPSignalling IndicationSource Statistics Descriptor1Conversationaln/an/aspeech2Conversationaln/an/aunknown3Streamingn/an/aspeech4Streamingn/an/aunknown5Interactive1Yesn/a6Interactive1Non/a7Interactive2Non/a8Interactive3Non/a9Backgroundn/an/an/a 
Transfer Delay 、SDU Error RatioPre-Rel8 QoS中的Transfer Delay参数，SDU Error Ratio参数由相应EPS QoS QCI对应的Packet Delay Budget和Packet Loss Rate参数映射，参见表6。表6  QCI与Transfer Delay 、SDU Error Ratio的映射关系QCIPacket Delay BudgetPacket Loss Rate1(GBR)100 ms10-22(GBR)150 ms10-33(GBR)50 ms10-34(GBR)300 ms10-65 (non-GBR)100 ms10-66 (non-GBR)300 ms10-67 (non-GBR)100 ms10-38 (non-GBR)300 ms10-69 (non-GBR) 
Delivery order、Delivery of erroneous SDU、Maximum SDU size、Residual BER其他Pre-Rel8 QoS参数，包括Delivery order、Delivery of erroneous SDU、Maximum SDU size和Residual BER，由MME本地配置。 
MME在从EPC的QoS向Pre-R8的QoS映射时，标准的QCI到Pre-R8的QoS参数映射可配置，根据配置进行映射。如果获取配置失败，对于标准的QCI值，映射关系参见表5和表6。 
MME支持扩展的QCI，由系统开关“是否支持扩展QCI”控制。如果此开关打开，则支持如下各项：所有带QoS的消息中QCI的值可扩展为10到255。对于QCI大于9的承载，MME判断是否GBR承载的原则为GBR和MBR都不为0。MME在从EPC的QoS向Pre-R8的QoS映射时，扩展的QCI（即大于9的QCI）到Pre-R8的QoS参数映射可配置，根据配置进行映射。如果获取配置失败，对于大于9的QCI值，映射关系参见表5和表6。如果此开关关闭，限制了QCI小于10，对大于9的QCI值都修正为9进行处理。用户从2G/3G移动到4G网络，MME保存pre-Rel-8 QoS，并将pre-Rel-8 QoS映射为EPS QoS，在本局进行QoS传递或控制，提供跨RAT的端到端QoS保障。 
###### Pre-R8 QoS到EPS QoS的映射 
ARPEPS QoS ARP由Pre-Rel8 QoS ARP 一对一映射，参见表7。表7  Pre-R8 QoS到EPS QoS的映射Pre-Rel-8EPSARP ValueBearer ARP Priority Value112H+13M+1其中H以及M的值根据运营商的需求，在MME上可配置。 
MBR、GBR对于Pre-Rel8 QoS的Traffic为会话类或流类，GBR和MBR直接一对一映射。如果MBR和GBR不一致，修正为一致，且取MBR和GBR中值小者为修正后的值。对于Pre-Rel8 QoS的Traffic为交互类或背景类，MBR用于计算APN-AMBR。 
APN-AMBR、UE-AMBR对于APN-AMBR，MME取HSS签约的APN-AMBR与该APN下所有已激活的Traffic Class 为Interactive 、Background 的PDP上下文的MBR之和取小得到 APN-AMBR。对于UE-AMBR，MME取HSS签约的UE-AMBR和该用户所有APN-AMBR之和取小得到 UE-AMBR。 
EPS QoS QCI和Pre-Rel8 QoS Traffic Class、Traffic Handling Priority、 Signalling Indication、Source Statistics DescriptorGPRS的QoS等级标识值UMTS的QoS参数Traffic ClassTHPSignalling IndicationSource Statistics Descriptor1Conversationaln/an/aspeech(NOTE 1)2Conversationaln/an/aunknown3Streamingn/an/aspeech(NOTE 1)4Streamingn/an/aunknown5Interactive1Yesn/a6Interactive1Non/a7Interactive2Non/a8Interactive3Non/a9Backgroundn/an/an/a 
特性能力 :特性|能力
---|---
QoS速率|最大支持10 Gbps。
扩展QCI|扩展QCI范围10到255。
用户级QoS配置|支持8192条数据。
会话级QoS配置|支持8192条数据。
承载级QoS配置|支持8192条数据。
实现原理 :系统架构 :EPS网络中将用户业务流映射到对应的EPS承载进行传送，映射方式如[图4]所示。
图4  EPS QoS业务流图

EPS网络基于EPS承载粒度进行QoS管理： 
QoS控制粒度都是基于承载（Bearer）。 
一个承载一般包括一个或者多个业务数据流（SDF）。 
被映射到同一个EPS承载的业务将被采用相同的承载层包转发处理。若需要提供不同的承载层包转发处理，则需要将业务流映射到不同的EPS承载上。 
涉及的网元 :MME网元QoS功能需要UE、eNodeB、MME、HSS、SGW、PGW、PCRF的共同完成，各网元的作用参见[表8]。
网元名称|网元作用
---|---
UE|根据UL TFT进行上行包过滤。将应用层QoS参数映射成QCI、MBR、GBR等参数，发起资源重分配或修改流程，在Required traffic flowQoS中带给网络侧。对上行数据执行APN-AMBR。
eNodeB|将QCI映射成无线侧的QoS参数(Resource Type、Priority、PDB、PELR)。分配、修改、释放无线资源。在无线资源受限时，根据ARP进行资源的重分配。对上下行数据流执行UE-AMBR 。无线侧QoS执行。
MME|从HSS获取签约QoS参数，并提供给PGW。根据激活的APN-AMBR计算UE-AMBR。根据本地策略设置ARP中的pre-emption capability和pre-emption vulnerability。本地QoS上限控制。在与2G/3G切换过程中，负责EPS承载QoS和pre-Rel-8 QoS参数的映射。
HSS|把用户签约数据QoS，APN-AMBR，UE-AMBR提供给MME。
SGW|GTP-based S5/S8：参与专有承载激活、修改、去激活流程、传输用户的QoS给PGW和MME。
PGW|GTP-based S5/S8：发起专有承载激活、修改、去激活流程。设置相应的QoS参数，将SDF级别的QoS参数映射成承载级别的QoS参数。根据TFT将业务流绑定到相应的承载上传输。对上行、下行数据流执行APN-AMBR。
PCRF|制定基于SDF的QoS策略，提供给PGW/PCEF。根据SPR签约的APN-AMBR修改PGW上报的APN-AMBR。
业务流程 :QoS传递
QoS传递包括以下流程： 
移动性管理过程中的QoS处理 
会话管理过程中的QoS处理 
切换过程中的QoS处理 
附着流程图如[图5]所示。
图5  附着流程图

与移动性管理过程中的QoS处理的附着流程有关的说明如下： 
HSS发送更新位置应答消息给新MME，MME获取到HSS的签约数据，其中包含签约默认承载的QoS（包含QCI，ARP）和APN-AMBR，及签约的UE-AMBR。 
MME向SGW发送create session request消息，其中包含签约的默认承载的QoS（包含QCI，ARP）和APN-AMBR。 
SGW发送创建会话请求消息给PGW，其中将MME带过来的QoS带给PGW。 
如果部署了动态PCC，PGW执行IP-CAN会话相关过程，从而获得UE默认PCC规则。 
PGW返回创建会话响应消息给SGW，PGW将决策的QoS（包含QCI，ARP）和APN-AMBR带给SGW。 
SGW回创建会话响应消息给MME，其中将PGW带过来的QoS（包含QCI，ARP）和APN-AMBR带给MME。 
MME通过发送ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST消息（包含在attach
accept消息中）将EPS QoS（QCI）和APN-AMBR带给UE；另外MME计算UE-AMBR，在S1-MME控制面初始上下文建立请求消息中将计算出的UE-AMBR，默认承载的QoS（包含QCI，ARP）带给eNB。 
跟踪区更新流程，如[图6]所示。
图6  TAU流程图

与移动性管理过程中的QoS处理的跟踪区更新流程有关的说明如下： 
局内TAU过程中的QoS处理： 如果SGW改变，MME向New SGW发送create session request消息，将承载的QoS（包含QCI，ARP，如果有GBR承载，则还需MBR和GBR）和APN-AMBR带给New
SGW。如果TAU request消息带“Active flag”，MME计算UE-AMBR，在S1-MME控制面初始上下文建立请求消息中将计算的UE-AMBR，承载的QoS（包含QCI，ARP，如果有GBR承载，则还需MBR和GBR）带给eNB。 
局间TAU过程中的QoS处理：New MME向Old MME发送Context Request消息。Old MME向New MME发送Context Response消息，其中携带承载QoS（包含QCI，ARP，如果有GBR承载，则还需MBR和GBR）和APN-AMBR。如果SGW改变，MME向New SGW发送create session request消息，将承载的QoS（包含QCI，ARP，如果有GBR承载，则还需MBR和GBR）和APN-AMBR带给New
SGW。如果TAU request消息带“Active flag”，MME计算UE-AMBR，在S1-MME控制面初始上下文建立请求消息中将计算的UE-AMBR，承载的QoS（包含QCI，ARP，如果有GBR承载，则还需MBR和GBR）带给eNB。MME在非切换后的2/3G重选到4G的TAU完成后，无论TAU消息中是否携带“Active flag”，判断用户签约的APN-AMBR或PDN默认QoS和当前PDN连接中的不一致，且系统开关“从Gn/Gp SGSN到MME的TAU触发QoS重协商”打开，给SGW发送Modify Bearer Command消息，消息中携带用户签约PDN数据中的APN-AMBR和默认承载QoS，触发QoS重协商。MME在切换后的2/3G重选到4G的TAU完成后，判断系统开关“从Gn/Gp SGSN到MME的TAU触发QoS重协商”打开，如果安全算法和UE-AMBR没有下发过且UE-AMBR发生变化，则发送S1-MME控制面上下文修改消息，携带新的UE-AMBR；如果用户签约的APN-AMBR或PDN默认QoS和当前PDN连接中的不一致，给SGW发送Modify
Bearer Command消息，消息中携带用户签约PDN数据中的APN-AMBR和默认承载QoS，触发QoS重协商。 
业务请求流程如[图7]所示。
图7  业务请求流程

与移动性管理过程中的QoS处理的业务请求流程有关的说明如下： 
和TAU request消息带“Active
flag”一样，MME计算UE-AMBR，在S1-MME控制面初始上下文建立请求消息中将计算的UE-AMBR，承载的QoS（包含QCI、ARP，如果有GBR承载，则还需MBR和GBR）带给eNB。
会话管理过程中的QoS处理
专有承载激活流程如[图8]所示。
图8  专有承载激活流程

与会话管理过程中的QoS处理的专有承载激活流程有关的说明如下： 
如果部署了动态PCC，PCRF发送PCC策略消息给PGW，PCC策略消息中包括了QoS策略信息；如果没有部署动态PCC，PGW使用本地QoS策略。 
PGW使用QoS策略为EPS承载分配QoS，包括QCI、ARP、MBR和GBR。PGW发送创建承载请求消息给SGW。 
SGW发送创建承载请求消息给MME，消息中包括EPS承载的QoS信息。 
MME构造会话管理消息，消息中包括了EPS承载的QoS（但是不包含ARP）。MME发送承载建立请求消息给eNodeB，包括了会话管理消息。 
eNodeB映射EPS承载的QoS为无线承载的QoS。eNodeB发送RRC连接重新配置消息给UE。 
UE保存会话管理消息中的EPS承载的QoS，可能向处理业务流的应用（Application）提供EPS承载的QoS参数。UE不会根据会话管理消息中的EPS承载的QoS参数而拒绝RRC连接重配置消息。UE返回RRC连接重新配置完成消息给eNodeB，确认无线承载的激活。 
eNodeB返回承载建立响应消息给MME，确认被请求的EPS承载的QoS是否能够被分配。 
PGW发起的承载QoS更新流程如[图9]所示。
图9  PGW发起的承载QoS更新流程

与会话管理过程中的QoS处理的PGW发起承载QoS更新流程有关的说明如下： 
如果部署了动态PCC，PCRF发送PCC策略消息给PGW，PCC策略消息中包括了QoS策略信息。如果没有部署动态PCC，PGW使用本地QoS策略。 
PGW发送更新承载请求消息给SGW，消息中携带EPS承载的QoS和APN-AMBR。 
SGW发送更新承载请求消息给MME，消息中携带EPS承载的QoS和APN-AMBR。 
MME构造会话管理消息，消息中可能包括了EPS承载的QoS（但是不包含ARP）和APN-AMBR。如果APN-AMBR改变了，MME重新计算UE-AMBR。MME发送承载修改消息给eNodeB，包括了会话管理消息。 
eNodeB映射EPS承载的QoS为无线承载的QoS。eNodeB发送RRC连接重新配置消息给UE。 
UE保存会话管理消息中的EPS承载的QoS，可能向处理业务流的应用（Application）提供EPS承载的QoS参数。UE不会根据会话管理消息中的EPS承载的QoS参数而拒绝RRC连接重配置消息。UE返回RRC连接重新配置完成消息给eNodeB，确认无线承载的修改。 
eNodeB返回承载修改响应消息给MME，确认被请求的EPS承载的QoS是否能够被分配。 
PGW发起承载非QoS更新流程如[图10]所示。
图10  PGW发起承载非QoS更新流程

与会话管理过程中的QoS处理的PGW发起承载非QoS更新流程有关的说明如下： 
如果部署了动态PCC，PCRF发送PCC策略消息给PGW，PCC策略消息中包括了QoS策略信息。如果没有部署动态PCC，PGW使用本地QoS策略。 
PGW发送更新承载请求消息给SGW，消息中携带APN-AMBR。 
SGW发送更新承载请求消息给MME，消息中携带APN-AMBR。 
MME构造会话管理消息，消息中包括APN-AMBR。如果APN-AMBR改变了，MME重新计算UE-AMBR。MME发送下行直传消息给UE，包括了会话管理消息。 
eNodeB发送直传消息给UE，消息中包括了会话管理消息。 
PGW发起承载QoS或非QoS更新时，UE可能处于连接态或IDLE态，如果UE处于连接态，那么直接通过已经有的连接下发信息给UE，但是当UE处于IDLE态时，则需要寻呼UE，UE发起业务请求并建立连接后才能够给UE发QoS或APN-AMBR相关信息；为避免3/4G之间频繁切换TAU（UE处于IDLE态），导致寻呼量大增，对无线和网络造成冲击，现有系统开关“是否通知IDLE的UE修改QoS”，控制UE处于IDLE态时，网络侧更新是否通知到UE。即MME发现UE处于ECM-IDLE态时，且APN-AMBR或承载QoS变化，如果开关“是否通知IDLE的UE修改QoS”关闭，则直接保存APN-AMBR和承载QoS，给PGW返回承载更新成功响应；如果开关“是否通知IDLE的UE修改QoS”打开，则寻呼UE，UE发起业务请求并建立连接后给UE发QoS或APN-AMBR相关信息。
HSS发起的QoS修改的流程如[图11]所示。
图11  HSS发起的QoS修改流程

与会话管理过程中的QoS处理的HSS发起QoS修改流程有关的说明如下： 
HSS发送插入用户数据消息给MME，消息中携带用户的IMSI和用户签约数据。用户签约数据中包含EPS签约的QoS（QCI和ARP）、签约的APN-AMBR和签约的UE-AMBR。 
MME更新存储的用户签约数据，给HSS返回插入用户数据确认消息。 
如果仅仅签约的UE-AMBR发生改变，MME重新计算新的UE-AMBR。MME使用S1-AP UE上下文修改流程完成UE-AMBR的更新，HSS发起的签约QoS修改流程在UE上下文修改流程完成后结束。 
如果QCI和/或APR和/或签约的APN-AMBR发生改变了，并且对应的有PDN连接激活，MME发送修改承载命令消息给SGW。消息中包含由于签约数据改变而需要更新的EPS承载QoS
Profile。 
SGW发送修改承载命令消息给PGW。 
PGW对签约QoS改变的APN对应的每个PDN连接，更新其对应默认承载的QoS。PGW发送更新承载请求消息给SGW。 
如果QCI和/或ARP修改了，可能触发PGW发起的承载QoS更新流程；如果QCI和ARP都没有修改，可能触发PGW发起承载非QoS更新流程。 
UE发起的承载资源更新流程如[图12]所示。
图12  UE发起的承载资源更新流程

与会话管理过程中的QoS处理的UE发起承载资源更新有关的说明如下： 
UE发送请求承载资源修改消息给MME，消息中包括了对应的流的QoS。 
MME发送承载资源命令消息给SGW，消息中包括了对应的流的QoS。 
SGW发送承载资源命令消息给PGW，消息中包括了对应的流的QoS。 
如果请求被接受了，专有承载建立流程或PGW发起的承载去激活流程或PGW发起的承载修改流程被激活。 
UE请求PDN连接的流程：UE请求PDN连接QoS处理与附着过程中的QoS处理一致。 
切换过程中的QoS处理
X2口切换X2口切换过程Qos处理与局内TAU过程中的SGW改变的处理相同，如果SGW改变，MME向New
SGW发送create session request消息，将承载的QoS(包含QCI和ARP，如果有GBR承载，则还需MBR和GBR)和APN-AMBR带给New
SGW。 
基于S1接口切换局内S1口切换过程Qos处理：与局内TAU过程中的SGW改变的处理相同，如果SGW改变，MME向New SGW发送create session request消息，将承载的QoS(包含QCI，ARP，如果有GBR承载，则还需MBR和GBR)和APN-AMBR带给New
SGW。MME发起Handover Request消息给Target eNB，MME计算UE-AMBR，在Handover Request消息中将计算出的UE-AMBR，承载的QoS（包含QCI和ARP，如果有GBR承载，则还需MBR和GBR）带给eNB。局间S1口切换过程Qos处理：老局MME给新局MME发送 Forward Relocation Request消息，其中携带承载QoS（包含QCI和ARP，如果有GBR承载，则还需MBR和GBR）和APN-AMBR。与局内TAU过程中的SGW改变的处理相同，如果SGW改变，MME向New SGW发送create session request消息，将承载的QoS(包含QCI，ARP，如果有GBR承载，则还需MBR和GBR)和APN-AMBR带给New
SGW。MME发起Handover Request消息给Target eNB，MME计算UE-AMBR，在Handover Request消息中将计算出的UE-AMBR，承载的QoS（包含QCI和ARP）带给eNB。 
用户跨RAT移动时QoS参数映射
E-UTRAN到UTRAN/GERAN的RAU更新MME作为老局时，判断本地是否保存了pre-Rel-8
QoS，如果保存了，直接取保存的pre-Rel-8 QoS带给新局，如果MME本地没有保存pre-Rel-8 QoS，MME按照Mapping
between EPS and pre-Rel-8 QoS parameters，将EPS QoS映射为pre-Rel-8 QoS带给新局。 
UTRAN/GERAN到E-UTRAN的TAU更新MME作为新局时，MME按照Mapping between
EPS and pre-Rel-8 QoS parameters，将pre-Rel-8 QoS映射为EPS QoS，同时本地保存pre-Rel-8
QoS，后续处理同局间TAU过程中新局的QoS处理。 
E-UTRAN到UTRAN的Handover流程MME作为老局时，判断本地是否保存了pre-Rel-8
QoS，如果保存了，直接取保存的pre-Rel-8 QoS带给新局，如果MME本地没有保存pre-Rel-8 QoS，MME按照Mapping
between EPS and pre-Rel-8 QoS parameters，将EPS QoS映射为pre-Rel-8 QoS带给新局。 
UTRAN到E-UTRAN的Handover流程MME作为新局时，MME按照Mapping between
EPS and pre-Rel-8 QoS parameters，将pre-Rel-8 QoS映射为EPS QoS，同时本地保存pre-Rel-8
QoS，后续处理同局间S1切换过程中新局的QoS处理。 
系统影响 :MME QoS是基本功能，MME开启QoS功能，对系统性能无影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议|章节号
---|---
3GPP TS 23.401： "GPRS enhancements for E-UTRAN access "|5.3节： Authentication, security and location management5.4节： Session Management, QoS and interaction with PCC functionality5.5节： Handover
3GPP TS 24.301："Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3"|8节： Message functional definitions and contents9.9.4节：EPS Session Management (ESM) information elements
3GPP TS 36.413： "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"|8节：S1AP Procedures9.2.1.20节：UE Aggregate MaximumBit Rate
3GPP TS 29.274： "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"|7.2节： Tunnel Management Messages8.7节： Aggregate MaximumBit Rate (AMBR)8.15节： Bearer Quality of Service (Bearer QoS)
3GPP TS 29.272： "Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|7.3.37节： EPS-Subscribed-QoS-Profile7.3.41节： AMBR
3GPP TS 23.107： ” Quality of Service (QoS) concept and architecture”|全部
3GPP TS 23. 203： “Policy and charging control architecture”|全部
可获得性 :License要求 :MME本地QoS控制特性需要申请了License“MME支持用户QoS控制”许可后，运营商才能获得该特性的服务。 
O&M相关 :命令 :与QoS特性相关的配置项参见[表9].
配置项|命令|说明
---|---|---
Intra E-UTRAN QoS配置|SET EXQCI SPRT|用于设置MME是否支持扩展QCI。
ADD EXQCI|Intra E-UTRAN QoS配置|用于新增扩展QCI值到Pre-R8 QoS映射配置。
SET MCAQOSCTL|Intra E-UTRAN QoS配置|用于配置各个接口支持CA(载波聚合)技术。
跨RAT QoS配置|SET STANDARD QCI MAPPING|用于配置标准QCI到Pre-R8 QoS映射。
RESET DEFAULT STANDARD QCI MAPPING|跨RAT QoS配置|用于将标准QCI到Pre-R8 QoS映射配置还原为缺省值。
SET DEFAULT EXQCI TPLADD EXQCI TPL|跨RAT QoS配置|用于配置扩展QCI到Pre-R8 QoS映射模板。
###### 软件参数 
与QoS特性相关的软件参数参见[表10].
软参ID|软参名称
---|---
786573|从GnGp SGSN到MME的TAU触发QoS重协商
786574|是否通知IDLE的UE修改QoS
786575|是否UE-AMBR和安全算法同时下发给eNodeB
786589|跨RAT TAU时是否释放非签约的PDN
特性配置 :特性配置 :配置说明 :当需要根据用户在4G网络的QoS中的不同QCI映射出不同的2G、3G网络的QoS时，使用该功能。 
配置前提 :EPC QoS参数中的QCI参数，协议目前定义了QCI1~QCI9，称为标准QCI。同时协议也明确了QCI取值1~255，其中128~254留给运营商自定义
，10~127/255为保留。MME网管提供了标准/扩展QCI到Pre-R8 QoS映射配置。 
配置过程 :使用[SET STANDARD QCI MAPPING]命令，配置标准QCI到Pre-R8
QoS映射。通常情况下，标准QCI到Pre-R8 QoS映射配置不需要配置，MME已生成默认值。
 说明： 
可使用[RESET DEFAULT STANDARD QCI MAPPING]命令，将标准QCI到Pre-R8 QoS映射配置还原为缺省值。
使用[ADD EXQCI TPL]命令，新增扩展QCI到Pre-R8 QoS映射模板。
 说明： 
可使用[SET DEFAULT EXQCI TPL]命令，设置缺省扩展QCI到Pre-R8
QoS映射模板。
使用[SET EXQCI SPRT]命令，设置MME是否支持扩展QCI。
使用[ADD EXQCI]命令，新增扩展QCI值到Pre-R8 QoS映射。
配置实例 :###### 保障速率的用户业务 
场景|配置
---|---
资源充足情况下，用户开机附着成功，进行VoLTE语音通话。HSS上签约对应用户的语音承载QCI为1，信令承载QCI为5,。|MME的QoS参数取默认值配置，即可满足该场景。
资源紧张情况下，VIP用户和普通用户从eNodeB接入MME，HSS上对于VIP用户签约ARP为1，支持E-RAB抢占，不支持E-RAB被抢占；普通用户签约ARP为2，不支持E-RAB抢占，支持E-RAB被抢占。两用户分别进行视频点播业务，普通用户资源被抢占，业务中断，进入空闲态。|MME的QoS参数取默认值配置，即可满足该场景。
###### 非保障速率的用户业务 
场景|配置
---|---
资源充足情况下，用户开机附着成功，进行网页浏览业务。|MME的QoS参数取默认值配置，即可满足该场景。
资源紧张情况下，VIP用户和普通用户从eNodeB接入MME，HSS上对于VIP用户签约ARP为1，支持E-RAB抢占，不支持E-RAB被抢占；普通用户签约ARP为2，不支持E-RAB抢占，支持E-RAB被抢占。两用户分别进行FTP业务，普通用户资源被抢占，业务中断，进入空闲态。|MME的QoS参数取默认值配置，即可满足该场景。
###### QoS转换时的默认Pre-R8 QoS参数的配置 
命令|说明
---|---
SET PRER8 QOS DEFAULT:RELIACLASS=2,DELAYCLASS="Level 1",PRECECLASS="NORMAL",PEAK="16000 octet/s",MEAN="500 octet/h",DELIERRSDU="NotDetect",DELIORDER="Order",MAXSDUSIZE="50 octets",TRAFFCLASS="Conversational",MAXBITRATEUL="5 kbps",MAXBITRATEDL="26 kbps",SDUERRRATIO="1e-5",RESIDUALBER="1e-3",TRANSDELAY="850 ms",GUARBITRATEUL="5 kbps",GUARBITRATEDL="6 kbps",ARP=2,DSCPUL=2,DSCPDL=1,SRCSTADESCRIP="Speech"|设置QoS转换时的默认Pre-R8 QoS参数。可靠级为2，延迟级为1，优先级为normal，峰值吞吐量为16000octet/s，平均吞吐量为500 octet/h，发送错误数据为NotDetect，发送顺序为ORDER，最大业务数据单元配置范围为50octets，业务列别为Conversational，最大上行链路比特率为5 kbps，最大下行链路比特率为26 kbps，业务数据单元错误率1e-5，残余位出错率1e-3，传输时延850ms，保证上行链路比特率5 kbps，保证下行链路比特率6 kbps，缺省分配/保持优先级2，缺省上行DSCP 2， 缺省下行DSCP1，源统计描述器Speech。
RESET PRER8 QOS DEFAULT|设置QoS转换时的Pre-R8 QoS所有参数回到缺省值。
SHOW PRER8 QOS DEFAULT|查询QoS转换时的默认Pre-R8 QoS参数。
###### QoS转换的安全变量及ARP映射配置 
命令|说明
---|---
SET PACKET DOMAIN PARAMETER:ARPHIGHPRIORITY=6,ARPMEDPRIORITY=10,ERABPREEMPT="YES",ERABPREEMPTVUL="NO"|设置QoS转换的安全变量及ARP映射。设置支持E-RAB抢占，不支持E-RAB被抢占，H值为6，M值为10。
SHOW PACKET DOMAIN PARAMETER|查询QoS转换的安全变量及ARP映射。
测试用例 :###### 保障速率的用户业务 
资源充足时用户进行保障速率业务的测试用例参见[表1]。
测试项目|资源充足时，用户进行保障速率业务。
---|---
测试目的|验证GBR专有承载建立流程是否可以顺利完成，QoS参数是否携带正确。
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS。网管可以正常使用。UE完成附着流程。
测试过程|用户进行语音业务，触发P-GW发起GBR专有承载建立流程。
通过准则|专有承载建立成功，MME在Activate Dedicate EPS Bearer Context setuprequest消息中携带的承载QoS参数为P-GW提供的QoS，承载上下文中保存的QoS也是P-GW提供的QoS。EPS QoS字段中MBR和GBR不为0。
测试结果|—
资源紧张时不同类别用户进行保障速率业务的测试用例参见[表2]。
测试项目|资源紧张时，不同类型用户进行保障速率业务。
---|---
测试目的|验证VIP用户能够正常进行业务，QoS参数是否携带正确。
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS。网管可以正常使用。VIP用户和普通用户都完成附着流程。
测试过程|VIP用户和普通用户分别进行视频点播业务，触发PGW发起GBR专有承载建立。
通过准则|VIP用户的专有承载建立成功，MME在Activate Dedicate EPS Bearer Context setuprequest消息中携带的承载QoS参数为P-GW提供的QoS，承载上下文中保存的QoS也是P-GW提供的QoS。EPS QoS字段中MBR和GBR不为0。普通用户专有承载因无线资源受限而建立失败。
测试结果|-
###### 非保障速率的用户业务 
资源充足时用户进行非保障速率业务的测试用例参见[表3]。
测试项目|资源充足时，用户进行非保障速率业务。
---|---
测试目的|验证非GBR专有承载建立流程是否可以顺利完成，QoS参数是否携带正确。
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS。网管可以正常使用。UE完成附着流程。
测试过程|用户进行FTP业务，触发P-GW发起非GBR专有承载建立流程。
通过准则|专有承载建立成功，MME在Activate Dedicate EPS Bearer Context setuprequest消息中携带的承载QoS参数为P-GW提供的QoS，承载上下文中保存的QoS也是P-GW提供的QoS。EPS QoS字段中QCI为5-9，不携带MBR和GBR。
测试结果|—
资源紧张时不同类别用户进行非保障速率业务的测试用例参见[表4]。
测试项目|资源紧张时，不同类型用户进行非保障速率业务。
---|---
测试目的|验证VIP用户能够正常进行业务，QoS参数是否携带正确。
预置条件|测试环境正常可用，包括UE、eNodeB、MME、SGW、PGW、HSS。网管可以正常使用。VIP用户和普通用户都完成附着流程。
测试过程|VIP用户和普通用户分别进行FTP业务，触发PGW发起非GBR专有承载建立。
通过准则|VIP用户的专有承载建立成功，MME在Activate Dedicate EPS Bearer Context setuprequest消息中携带的承载QoS参数为P-GW提供的QoS，承载上下文中保存的QoS也是P-GW提供的QoS。EPS QoS字段中QCI为5-9，不携带MBR和GBR。普通用户专有承载因无线资源受限而建立失败。
测试结果|—
## ZUF-78-11-002 支持EPS Bear和PDP的映射功能 
概述 :MME提供Gn/Gp接口用于与Pre R8 SGSN互通。在流程被触发前，EPS承载（用于从E-UTRAN接入到EPS）的参数需要映射到PDP上下文（用于从UTRAN/GERAN接入到EPS）的Pre-Rel-8参数值，或从PDP上下文的Pre-Rel-8参数值映射到EPS承载的参数。 
收益 :EPS承载（用于从E-UTRAN接入到EPS）和Pre R8 PDP上下文（用于从UTRAN/GERAN接入到EPS）的参数之间的一对一映射。 
描述 :ZXUN uMAC（MME）支持EPS承载和PDP上下文之间一对一映射。 
在流程被触发前，根据EPS QoS和Pre Rel-8 QoS的映射关系，EPS承载（用于从E-UTRAN接入到EPS）的QoS参数需要映射到PDP上下文（用于从UTRAN/GERAN接入到EPS）的Pre-Rel-8 QoS参数值。 
EPS承载的ID需要映射到PDP上下文的NASPI。 
当UE从EPS网络切换到2/3G网络，MME将EPS承载映射到PDP上下文。当UE从2/3G网络切换到EPS网络，MME将PDP上下文映射到EPS承载。 
## ZUF-78-11-003 扩展QCI 
MME支持扩展QCI，将在全部携带有QoS参数的消息中的QCI值从10扩展到255。 
## ZUF-78-11-004 本地QoS策略 
概述 :MME支持本地QoS上限控制。 
收益 :灵活控制漫游用户的QOS，更好地保证本地用户体验。 
描述 :为了控制漫游用户带宽消耗，保障本网用户业务感受，需要MME能够进行本地QoS上限控制。 
MME支持基于IMSI，APN，QCI和ARP四个维度进行QoS控制： 
IMSI用来区分漫游和非漫游用户。 
APN用来区分普通业务和特殊业务（如语音）。 
QCI和ARP用来区分普通承载和特殊承载（IMS信令承载、IMS语音承载）。 
实现了以下三个层级的QoS参数控制： 
用户级QoS参数控制（UE-AMBR）。 
会话级QoS参数控制（APN-AMBR）。 
承载级QoS参数控制（GBR承载：MBR、GBR）。 
# 缩略语 
# 缩略语 
EPS :Evolved Packet System演进的分组系统
## QCI 
QoS Class IdentifierQoS类别标识
# ZUF-78-13 位置相关业务 
概述 :功能描述 :在移动网络中，用户所在的位置信息包括TAI、ECGI和地理位置信息等。MME从无线侧获得位置信息后可传递给核心网的其他网元。
与用户位置信息相关的应用包括： 
基于用户所在位置对用户采用不同的控制策略（比如计费策略、QoS策略、接入控制等）。 
通过用户所在位置为用户提供更好的服务（比如救援、导航、与位置相关的增值服务）。 
功能特性简介 :针对用户位置信息的应用需求，MME支持多种位置相关业务。详细的解决方案参见下表。 
方案特性|实现简述|特导链接
---|---|---
HSS位置信息请求上报|HSS下发消息指示MME上报保存的用户位置信息或用户当前最新位置信息。对于处于连接态的用户，MME直接返回保存的用户位置信息。对于处于IDLE态的用户，MME对用户进行寻呼，寻呼成功后上报位置信息给HSS。|ZUF-78-13-001 HSS位置信息请求上报
位置报告|由于某些业务（比如紧急呼叫、计费等）需要用户位置信息，PGW会指示MME上报位置信息。如果MME在附着或TAU过程中，检测出用户所在的TAI/ECGI/eNodeB ID发生变化，则在发送的Create Session Request、Modify Bearer Request或 Change Notification Request消息中携带新TAI/ECGI/eNodeB ID给PGW。具体业务流程参见3GPP 23.401协议的“5.9.2 Location Change Reporting Procedure”。|ZUF-78-13-002 位置报告
小区位置信息上报|由MME触发小区位置信息上报功能。MME下发Location Report Control通知eNodeB，要求eNodeB在用户小区位置发生变化时，上报Location Report通知MME。该功能使得MME能及时得到用户所在的最新小区，但会增加MME与eNodeB之间的信令负荷。具体业务流程参见3GPP 23.401协议的“5.9.1 Location Reporting Procedure”。|ZUF-78-13-003 小区位置信息上报
LCS|MME支持定位业务（LCS），用于UE或网络侧获得UE当前所在的位置信息。定位类型可分为：UE起呼的立即定位UE终呼的立即定位紧急呼叫定位对于上述的定位类型，MME支持两种模式：UE在连接态计算定位信息传递给E-SMLCUE在空闲态计算定位信息传递给E-SMLC定位业务具体流程可参见3GPP 23.271协议。MME的定位业务还支持以下功能：MME支持NB用户的延迟定位。MME根据GMLC的定位请求，要求对处于空闲态的NB用户缓存定位，待用户可达时，再进行定位。根据GMLC来选择E-SMLC。此功能属于定制需求。MME根据GMLC来配置选择对应的E-SMLC。对于同一个GMLC的定位，在对应的E-SMLC组中轮流选择执行定位的E-SMLC。|ZUF-78-13-004 LCS
PRA|PRA功能是即时感知用户进入或离开指定区域，以便对指定区域进行流量控制以及监控。在PCRF进行区域布控，通过PGW通知到MME。当用户在布控的区域活动时，MME上报事件到PGW，PGW将事件上报给PCRF。具体业务流程参见3GPP 23.401协议的“5.9.2 Location Change Reporting Procedure”和 3GPP 29.274协议的“7.3.14 Change Notification Request”章节。|ZUF-78-13-005 PRA
## ZUF-78-13-001 HSS位置信息请求上报 
特性描述 :特性描述 :描述 :定义 :在LTE网络中，用户所在的位置信息是一个重要的信息，网络获取用户所在的位置信息后可进行以下应用：
基于用户所在位置对用户采用不同的控制策略（比如不同计费策略、不同QoS策略、不同接入控制等）。 
通过用户所在位置为用户提供更好的服务（比如救援、导航、任意与位置相关的增值服务）。 
位置信息包括有TAI、ECGI和地理位置信息。
MME接收来自其他网元获取位置信息的请求，从无线eNodeB获得用户的位置信息，进行本地保存并上报给PGW/HSS/GMLC网元。
背景知识 :LTE网络位置信息有两种，位置标识和地理位置： 
位置标识包括无线规划的TAI和ECGI。 
地理位置包括经纬度和终端到无线eNodeB之间的距离。 
位置标识
在EPC网络中位置标识一般用在基于位置提供不同服务与计费策略。
位置标识来源于无线规划，MME从无线获得位置标识后可传递给其他网元。PCRF基于位置标识提供服务策略，计费中心基于位置提供计费策略。
地理位置
在EPC网络中地理位置一般应用于定位服务。 
地理位置来源于无线测量，MME接收来自用户或定位中心的定位请求，从无线获得用户地理位置后，上报给定位中心，定位中心再传递给终端用户或上层应用系统。 
应用场景 :EPC网络使用位置标识为用户提供不同的计费或服务策略，可以基于某个位置标识提供策略，也可以基于某组位置标识提供策略；EPC网络也可为用户提供地理位置信息，完成对用户的定位。 
应用场景|场景需求|解决方案
---|---|---
基于位置标识的计费/服务|对于计费需实时所在位置标识对于服务策略无需实时所在位置标识|位置报告HSS/PGW+小区位置上报位置报告PGW
客户收益 :受益方|受益描述
---|---
运营商|提高策略灵活性：基于用户位置标识为用户提供灵活的服务与计费策略。丰富业务功能：为用户提供定位能力，便于紧急呼叫时救援，以及方便开展各种与位置相关的增值服务。
移动用户|提高终端用户体验：用户在某些区域可获得更优费率或更好的服务质量，同时可获得终端定位能力，可使用各种与位置相关的增值服务。
实现原理 :系统架构 :LCS定位网络架构如[图1]所示。
图1  LCS定位网络架构图

LCS定位需要新增E-SMLC与GMLC网元支持，GMLC网元为定位中心，管理控制用户的定位业务。E-SMLC网元为定位计算单元，计算用户的地理位置。 
涉及的网元 :网元|作用
---|---
E-SMLC|定位测量用户所在的地理位置。
eNodeB|用户进行业务时eNodeB上报用户所在的位置标识（TAI/ECGI）信息。用户发生移动位置发生变化时，eNodeB上报最新位置标识（TAI/ECGI）信息给MME。接收定位请求，上报用户所在的地理位置信息。
GMLC|管理控制用户的定位业务，接收与下发用户所在的地理位置信息。
HSS|HSS处理AS定位服务器请求位置的要求，从MME获得位置标识后上报给AS定位服务器。
MME|MME从eNodeB获得用户所在位置标识，上报给PGW与HSS网元。MME获得用户所在位置标识，判断用户进入或离开某组位置标识并上报给PGW。MME接收GMLC的定位请求，查找用户对应的E-SMLC网元，转发定位请求到E-SMLC。
PGW|PGW通知MME上报位置标识信息。PGW下发一组位置标识到MME。PGW接收MME上报的位置标识或进入与离开某组位置标识的标示。
业务流程 :位置报告功能基于上报给PGW还是HSS可分为： 
位置报告PGW 
位置报告HSS 
同时MME可提取本地保存的位置标识信息上报，也可以向无线获取用户实时所在位置标识上报。当需从无线获取用户实时位置标识时，要启用小区位置上报功能。 
位置报告PGW
位置报告PGW功能涉及Attach、TAU、PDN连接、承载激活/修改及切换流程。具体流程参见信令流程
。
位置报告HSS
位置报告HSS流程参见[图2]。
图2  位置报告HSS流程图

流程说明： 
HSS向MME请求位置标识信息，发送Insert Subscriber Data Request消息。 
如HSS请求的为用户之前位置标识，MME提取记录的用户位置标识直接返回Insert Subscriber Data Answer消息。 
如HSS请求的为用户当前所在位置标识，如用户为IDLE态则寻呼用户，如用户为连接态则下发Location Report
Control消息。 
eNodeB返回响应后，MME向HSS发送Insert Subscriber Data Answer消息携带用户当前所在位置标识信息。 
系统影响 :在校园网和企业网场景下，由于需要用户精确实时的位置，需要eNodeB实时上报用户最新的ECGI信息，MME并上报给PGW。增加了无线与网络间消息量，会降低系统性能。如开启以上功能，能下降MME系统性能，PGW网元接收消息量增加，同时eNodeB上报的消息量增加，对eNodeB的性能要求更高。 
开启地理位置LCS定位功能，需增加无线与网络的消息量，对于MME系统性能有影响，当定位的用户越多性能影响越大。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议|章节号及章节名称
---|---
3GPP TS23.401: "General Packet Radio Service (GPRS) enhancements for EvolvedUniversal Terrestrial Radio Access Network (E-UTRAN) access".|5.3.2 Attachprocedure5.3.3 Tracking Area Update procedures5.3.4Service Request procedures5.4 Session Management, QoS and interactionwith PCC functionality5.5 Handover5.9 Interactions withother services
3GPP TS24.301: "Non-Access-Stratum (NAS) protocol for Evolved Packet System(EPS); Stage 3".|全部
3GPP TS23.271: Functional stage 2 description of Location Services (LCS)|全部
3GPP TS29.171: LCS Application Protocol (LCS-AP) between the Mobile ManagementEntity (MME) and Evolved Serving Mobile Location Centre (E-SMLC)|全部
3GPP TS29.172: Evolved Packet Core (EPC) LCS Protocol (ELP) between the GatewayMobile Location Centre (GMLC) and the Mobile Management Entity (MME)|全部
3GPP TS29.272: "Mobility Management Entity (MME) and Serving GPRS SupportNode (SGSN) related interfaces based on Diameter protocol".|5.2.2 SubscriberData Handling Procedures
3GPP TS29.274: "General Packet Radio Service (GPRS); Evolved GPRS TunnellingProtocol (eGTP) for EPS".|7.2.1 CreateSession Request7.2.4 Create Bearer Response7.2.8 ModifyBearer Response7.2.15 Update Bearer Request7.3.14 ChangeNotification Request
3GPP TS36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1Application Protocol (S1AP)".|8.11 LocationReporting Procedures
特性能力 :该特性不涉及规格指标。 
可获得性 :License要求 :该特性为MME的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项新增命令配置项参见表1。表1  新增命令配置项配置项命令Diameter连接配置ADD DIAMCONNSET DIAMCONNSET HOST DOMAINDEL DIAMCONNSHOW DIAMCONNDiameter链路组配置ADD DIAMLINKGROUPSET DIAMLINKGROUPDEL DIAMLINKGROUPSHOW DIAMLINKGROUPDiameter路由配置ADD DIAMROUTESET DIAMROUTEDEL DIAMROUTESHOW DIAMROUTEDiameter路由组配置ADD DIAMROUTEGROUPSET DIAMROUTEGROUPDEL DIAMROUTEGROUPSHOW DIAMROUTEGROUPDiameter局向路由配置ADD DIAMADJROUTESET DIAMADJROUTEDEL DIAMADJROUTESHOW DIAMADJROUTEDiameter局向配置ADD DIAMADJSET DIAMADJDEL DIAMADJSHOW DIAMADJDiameter邻接局分析结果索引ADD DIMOFC ANALYSISSET DIMOFC ANALYSISDEL DIMOFC ANALYSISSHOW DIMOFC ANALYSIS移动号码分析ADD MDNALSET MDNALDEL MDNALSHOW MDNALSHOW MDN2REALM 
软件参数新增软件参数参见表2。表2  新增软件参数软件参数ID软件参数名称65669发送Location Reporting Control消息262428是否携带支持位置改变上报指示位65644X2切换位置上报控制通知65648携带值为0的CRA到新MME262462忽略PGW下发的位置区改变上报指示262463忽略PGW下发的取值为Stop Reporting的位置区改变上报指示786708ULI顺从R11262455携带ULI方式 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :HSS主动向MME请求获取UE的位置信息，MME收到HSS的请求后，MME向enodeB获取用户当前的位置信息，传递给HSS。 
本场景下，MME不需要进行特殊配置，只要MME和HSS对接成功即可。 
配置前提 :MME和HSS网元运行正常。 
配置过程 :MME与HSS对接配置流程参见[表1]。
步骤|操作|操作说明
---|---|---
1|配置Diameter偶联|配置Diameter偶联实现签约数据和鉴权数据的传输。MME向HSS报告当前移动用户的位置，HSS向MME发送用户的签约数据。
2|配置偶联索引|配置偶联索引，用于配置业务需要关联的SCTP偶联。
3|配置Diameter连接路由|配置Diameter连接路由，包括以下几个子步骤。新增Diameter连接，是Diameter路由数据配置的前提，也是使用Diameter协议交互的前提条件。新增Diameter链路组，从逻辑上维护一组Diameter连接。新增Diameter路由，从逻辑上维护一组Diameter链路组。新增Diameter路由组，从逻辑上维护一组Diameter路由。新增Diameter局向路由，从逻辑上维护一组Diameter路由组。新增Diameter局向，从逻辑上维护一组Diameter局向路由。
4|配置移动号码分析数据|配置移动号码分析数据，实现根据用户IMSI寻址到归属的HSS的功能，包括以下几个子步骤。新增Diameter邻接局分析结果索引，实现移动号码段和Diameter邻接局的关联。新增移动号码分析，把移动号码段分析为对应Diameter邻接局向的索引。
配置实例 :在配置数据之前，应当完成MME与HSS对接的相关数据规划，数据规划示例参见[表2]。
参数名称|取值举例
---|---
SCTP标识|1
别名|HSS60
应用属性|CLT
本端IP地址1|40.1.136.200
本端端口|8001
本端IP地址2|40.1.136.60
对端端口|8060
偶联ID|1
偶联协议类型|Diameter
对端节点域名|epc.mnc002.mcc460.3gppnetwork.org
对端节点主机名|hss60.epc.mnc002.mcc460.3gppnetwork.org
Diameter链路组ID|10
Diameter链路组中Diameter链路的分担方式|负荷分担
Diameter路由ID|20
Diameter路由中Diameter链路组的路由属性|主备
Diameter路由组ID|100
Diameter路由组中Diameter路由的路由属性|主备
局向路由ID|1
Diameter路由组ID-Diameter路由组级别-Diameter路由组权重|100-1-1
局向域名|epc.mnc002.mcc460.3gppnetwork.org
Diameter局向号|15
号码分析结果索引|1
被分析号码|46002
分析器入口|DAS_IMSI_DIAMETER
根据规划，进行如下配置。 
新增SCTP偶联，命令如下。
[ADD SCTP]:ID=1,NAME="HSS60",LOCPORT=8001,REMPORT=8060,LOCADDR1="40.1.136.200",REMADDR1="40.1.136.60",PROTOCALTYPE=DIAMETER
配置偶联索引，命令如下。 
[ADD SCTPIDCFG]:SCTPID=1,TYPE=DIM
配置Diameter连接路由 
新增Diameter连接，命令如下。 
[ADD DIAMCONN]:ADJNAME="hss60.epc.mnc002.mcc460.3gppnetwork.org",ADJDOMAIN="epc.mnc002.mcc460.3gppnetwork.org",SCTPID=1
新增Diameter链路组，命令如下。 
[ADD DIAMLINKGROUP]:LINKGRPID=10,SCTPLINKID=1,PARTAKEMODE="PARTAKE"
新增Diameter路由，命令如下。 
[ADD DIAMROUTE]:ROUTEID=20,LINKGRPID=10,PROPERTY="BACKUP"
新增Diameter路由组，命令如下。 
[ADD DIAMROUTEGROUP]:ROUTEGRPID=100,ROUTEID=20,PROPERTY="BACKUP"
新增Diameter局向路由，命令如下。 
[ADD DIAMADJROUTE]:ADJROUTEID=1,ROUTEGROUP=100-1-1,REALM="epc.mnc002.mcc460.3gppnetwork.org",HOSTNAME="hss60.epc.mnc002.mcc460.3gppnetwork.org"
新增Diameter局向，命令如下。 
[ADD DIAMADJ]:ADJID=15,ADJROUTEID=1
配置移动号码分析数据。 
新增Diameter邻接局分析结果索引，命令如下。 
[ADD DIMOFC ANALYSIS]:IDX=1,DIAMGRPID=15
为IMSI前缀为46002的用户号段配置移动号码分析，对应的号码分析结果索引为1，命令如下。
[ADD MDNAL]:DGT="46002",ENTR="DAS_IMSI_DIAMETER",RST=1
测试用例 :测试项目|HSS向MME获取用户当前位置信息
测试目的|验证MME可以向HSS提供用户位置信息。
预置条件|EPS网络中各网元系统及操作维护台运行正常。用户在HSS中已签约EPS业务。在MME上建立用户跟踪。MME与HSS对接成功，链路正常。
测试过程|UE在EPC网络开机发起附着。HSS通过Insert-Subscriber-Data-Request消息请求UE位置信息。
通过准则|UE附着成功，默认承载建立成功。MME回复Insert-Subscriber-Data-Answer成功，携带UE当前位置信息。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|—
## ZUF-78-13-002 位置报告 
概述 :PGW请求MME上报UE的位置信息。在附着或TAU过程中，MME向PGW上报位置信息。 
MME上报位置信息的粒度分为： 
ECGI 
TAI 
eNodeB ID 
收益 :PGW获取到UE位置。 
描述 :由于某些业务，比如紧急呼叫或计费等，需要用户位置信息，PGW指示MME上报位置信息。在不再需要位置信息时，PGW指示MME停止位置上报；MME也可配置支持用户位置改变上报功能的P-GW地址列表。 
MME在进行附着/TAU/业务请求时，检测出用户所在的TAI/ECGI/eNodeB ID发生变化时，则在Create Session Request或Modify Bearer Request或 Change Notification Request消息携带新TAI或ECGI或eNodeB ID给PGW。 
## ZUF-78-13-003 小区位置信息上报 
特性描述 :特性描述 :描述 :定义 :为了实现EPC网络基于精确的位置计费，需要MME及时把用户的位置信息报告给PGW。
对于CS和LTE双注册终端，第三方MPS系统可以根据HSS提供的CS/LTE的ageOfLocation信息来确定用户的位置，即ageOfLocation时间最近的小区作为用户终端当前的位置。
在23401协议中，定义了E-UTRAN Cell Identity Age信息，当MPS通过HSS的insert
sub data request消息探测用户最新的位置信息，MME在寻呼未果的情况下，将E-UTRAN Cell Identity
Age返回给MPS（通过HSS），MPS根据其从CS获取的ageofLocation以及LTE返回的E-UTRAN Cell Identity
Age，来进一步确定用户目前所在精确位置。 
应用场景 :具体常见场景包括： 
EPC的基于精确的位置计费要求。 
位置定位系统，UE双注册CS/LTE网络时，确切知道用户最精确的所在小区。 
客户收益 :收益者|收益描述
---|---
运营商|实现基于位置的精确计费。用户定位。
终端用户|计费更精确。定位自己所处的位置。
实现原理 :各网元作用 :MME支持小区位置上报功能需要MME、SGW、PGW和eNodeB共同完成。 
网元名称|网元作用
---|---
eNodeB|负责上报用户的位置信息给MME。
MME|负责把用户的位置信息上报给SGW。
SGW|负责把MME上报的位置信息传给PGW，以及把PGW的上报类型通知MME
PGW|通知MME位置上报的类型以及接收MME上报的位置信息进行精准计费。
MME支持用户活动时间上报需要MME、HSS共同完成。 
网元名称|网元作用
---|---
MME|负责把用户最近的活动时间通知HSS。
HSS|负责接收MME上报的用户最近活动时间。
业务流程 :ATTACH流程
图1  ATTACH流程

UE发起附着流程。 
MME向SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Create Session Request请求转发给PGW。 
PGW返回Create Session Response响应给SGW。 
SGW向MME回送Create Session Response响应消息。 
如果支持小区位置上报功能开关打开，MME根据响应消息中的Change Reporting Action来决策是否发送Location
Reporting Control消息给eNodeB。 
MME向SGW发送Modify Bearer Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Modify Bearer Request请求转发给PGW。 
PGW返回Modify Bearer Response响应给SGW。 
SGW向MME回送Create Session Response响应消息。 
如果支持小区位置上报功能开关打开并且没有向eNodeB发送过Location Reporting Control消息，MME根据保存的Change
Reporting Action来决策是否发送Location Reporting Control。 
PDN连接流程
图2  PDN连接流程

UE发起PDN连接流程，MME向SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能 
MME向SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Create Session Request请求转发给PGW。 
PGW返回Create Session Response响应给SGW。 
SGW向MME回送Create Session Response响应消息。 
如果支持小区位置上报功能开关打开并且没有向eNodeB发送过Location Reporting Control消息，MME根据保存的Change
Reporting Action来决策是否发送Location Reporting Control消息给eNodeB 
MME向SGW发送Modify Bearer Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能 
MME向SGW发送Modify Bearer Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Modify Bearer Request请求转发给PGW。 
PGW返回Modify Bearer Response响应给SGW。 
SGW向MME回送Create Session Response响应消息。 
SGW改变的TAU流程
图3  SGW改变的TAU流程

UE发起TAU流程，MME判断SGW发生改变，则向新的SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
MME向SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Create Session Request请求转发给PGW。 
PGW返回Create Session Response响应给SGW。 
SGW向MME回送Create Session Response响应消息。 
如果支持小区位置上报功能开关打开，MME保存响应消息中的Change Reporting Action，TAU流程结束，MME根据保存的Change
Reporting Action来决策是否发送Location Reporting Control消息给eNodeB。 
SGW未改变的TAU流程
图4  SGW未改变的TAU流程

UE发起TAU流程，MME判断SGW未发生改变，则向SGW发送Modify Bearer Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
MME向SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Create Session Request请求转发给PGW。 
PGW返回Create Session Response响应给SGW。 
SGW向MME回送Create Session Response响应消息。 
如果支持小区位置上报功能开关打开，MME保存响应消息中的Change Reporting Action，TAU流程结束，MME根据保存的Change
Reporting Action来决策是否发送Location Reporting Control消息给eNodeB。 
UE业务请求流程
图5  UE业务请求流程

UE发起业务请求流程，MME则向SGW发送Modify Bearer Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW发送Modify Bearer Request请求给PGW。 
PGW返回Modify Bearer Response响应给SGW。 
SGW发Modify Bearer Response给MME。 
如果支持小区位置上报功能开关打开，MME保存响应消息中的Change Reporting Action。 
业务请求流程结束，MME根据保存的Change Reporting Action来决策是否发送Location Reporting
Control消息给eNodeB。 
专用承载激活流程
图6  专用承载激活流程

PGW发起专有承载激活流程，向SGW发送Create Bearer Request请求。 
SGW发送Create Bearer Request请求给MME。 
如果支持小区位置上报功能开关打开，MME保存消息中的Change Reporting Action。 
专有承载激活流程结束，MME根据保存的Change Reporting Action来决策是否发送Location Reporting
Control消息给eNodeB。 
专用承载修改流程
图7  专用承载修改流程

PGW发起专有承载修改流程，向SGW发送Update Bearer Request请求。 
SGW发送Update Bearer Request请求给MME。 
如果支持小区位置上报功能开关打开，MME保存消息中的Change Reporting Action。 
专有承载修改流程结束，MME根据保存的Change Reporting Action来决策是否发送Location Reporting
Control消息给eNodeB。 
X2切换SGW未改变流程
图8  X2切换SGW未改变流程

UE发起X2切换流程，目标eNodeB向MME发送Path Switch Request 
MME发送Modify Bearer Request请求给SGW，如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能 
SGW发送Modify Bearer Request请求给PGW。 
PGW返回Modify Bearer Response响应给SGW。 
SGW发Modify Bearer Response给MME。 
如果支持小区位置上报功能开关打开，MME保存响应消息中的Change Reporting Action，X2切换流程结束，MME根据保存的Change
Reporting Action来决策是否发送Location Reporting Control消息给eNodeB。 
X2切换SGW改变流程
图9  X2切换SGW改变流程

UE发起X2切换流程，目标eNodeB向MME发送Path Switch Request 
MME向SGW发送Create Session Request请求。如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW把Create Session Request请求消息转发给PGW。 
PGW向SGW回复Create Session Reponse响应消息。 
SGW把PGW回复Create Session Reponse响应消息转发给MME。如果支持小区位置上报功能开关打开，MME保存响应消息中的Change
Reporting Action。 
MME发送Modify Bearer Request请求给SGW，如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能 
SGW发送Modify Bearer Request请求给PGW。 
PGW返回Modify Bearer Response响应给SGW。 
SGW发Modify Bearer Response给MME。如果支持小区位置上报功能开关打开，MME保存响应消息中的Change
Reporting Action。 
X2切换流程结束，MME根据保存的Change Reporting Action来决策是否发送Location Reporting
Control消息给eNodeB。 
局间切换流程
图10  局间切换流程

UE发起局间切换流程，Source-eNodeB/RNC向Source-MME/SGSN发送Handover Required。 
Source-MME/SGSN发送Forward Relocation Request请求给目标MME，如果MME支持小区位置上报功能开关打开目的MME保存消息中的Change
Reporting Action 
目标MME如果判断SGW发送改变，则发送Create Session Request给目标SGW；如果不改变，则不发Create
Session Request消息，如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW回复Create Session Reponse响应消息给MME。 
目标MME发送Modify Bearer Request给目标SGW，如果MME支持小区位置上报功能开关打开，则在消息中携带CRSI，表明MME支持小区位置上报功能。 
SGW发送Modify Bearer Request请求给PGW。 
PGW返回Modify Bearer Response响应给SGW。 
SGW发Modify Bearer Response给MME。如果支持小区位置上报功能开关打开，MME保存响应消息中的Change
Reporting Action。 
如果支持小区位置上报功能开关打开，MME保存消息中的Change Reporting Action，切换流程结束，MME根据保存的Change
Reporting Action来决策是否发送Location Reporting Control消息给目标eNodeB。 
位置上报
图11  位置上报

MME发送Location Reporting Control消息给eNodeB。 
MME接受到eNodeB发送的Location Report消息。 
MME根据每个连接中保存的Change Reporting Action来决策发送一个或者多个Change Notification
Request消息给SGW。 
SGW把Change Notification Request消息发给PGW。 
PGW向SGW发送Change Notification Response消息。 
SGW把PGW的Change Notification Response消息转发给MME。 
MME收到Change Notification Response响应消息，保存消息中Change Reporting
Action。如果发现所有连接中的Change Reporting Action都为无效，则发送Location Reporting
Control消息给eNodeB要求停止上报。 
最近活动时间上报
图12  最近活动时间上报

HSS发送Insert Subscriber Data给MME 
MME回Insert Subscriber Data Ack消息给HSS，消息中携带用户最近活动的时间戳。 
系统影响 :开启本功能，SMP性能下降15%。 
应用限制 :特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准类别|标准名称
---|---
3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for EvolvedUniversal Terrestrial Radio Access Network (E-UTRAN) access
3GPPTS24.301|Non-Access-Stratum (NAS) protocol for Evolved Packet System(EPS); Stage3
3GPPTS24.007|Mobile radio interface signalling layer 3; General aspects
3GPP TS 29.274|Evolved General Packet Radio Service (GPRS) Tunnelling Protocolfor Control plane (GTPv2-C)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|MME|eNodeB|SGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  修改配置项配置项命令本局移动数据SET COMBOCFG中增加了支持用户位置信息变化上报配置 
安全变量表2  修改安全变量命令描述SET SYSTEM CONTROL增加了参数是否支持Last UE Activity Time功能 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :ID
---
C432010042 改变通知请求消息发送次数
C432010043 改变通知请求重发消息次数
C432010044 改变通知成功响应消息接收次数
C432010045 改变通知失败响应消息接收次数
告警和通知 :该特性不涉及告警和通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本节介绍如何配置上区位置信息上报特性。 
配置过程 :在OMM命令终端上执行[SET SYSTEM CONTROL]命令，配置IDR Flags为获取用户的位置信息时，IDA消息中是否携带Last
UE Activity Time。
在OMM命令终端上执行[SET COMBOCFG]命令，配置支持小区位置上报。
配置实例 :配置步骤|解释说明|配置脚本
---|---|---
1|配置IDR Flags为获取用户的位置信息时，IDA消息中是否携带Last UE Activity Time。|SET SYSTEM CONTROL:LATR="YES"
2|配置支持小区位置上报。|SET COMBOCFG:MMEULICHGRPT="YES"
测试用例 :测试项目|MME收到HSS发送的IDR消息，IDRFlags为获取用户的位置信息。
测试目的|验证MME保存用户的上行消息的时间，MME收到HSS发送的IDR消息，IDRFlags为获取用户的位置信息，支持携带Last UE Activity Time，IDA消息携带用户的Last UE ActivityTime。
预置条件|IDA消息中是否携带Last UE Activity Time开关打开。用户Attach成功。
测试过程|MME收到HSS发送的IDR消息。IDR Flags为获取用户的位置信息。
通过准则|MME发送IDA消息到HSS。IDA消息携带用户的Last UE Activity Time。
测试结果|MME发送IDA消息到HSS。IDA消息携带用户的Last UE Activity Time。
测试项目|Attach流程，CreateSession Response消息带Change Reporting Action字段为Start Reporting TAI 3
测试目的|验证MME支持小区位置上报。
预置条件|支持位置上报开关打开。
测试过程|Attach流程。SGW返回的Create Session Response消息携带Change Reporting Action字段为StartReporting TAI 3，Modify Bearer Response消息不携带Change Reporting Action字段。
通过准则|Attach成功。MME向SGW发送Create Session Request消息，Indication Flags中携带CRSI (ChangeReporting support indication)标记，保存该字段到PDN连接上下文；MME向SGW发送的Modify BearerRequest消息，Indication Flags中携带CRSI (Change Reporting support indication)标记。MME保存Change Reporting Action字段到PDN连接上下文。向eNodeB发送LOCATION REPORTING CONTROL消息，请求eNodeB实时上报用户的小区信息。向SGW发送Change Notification Request消息，参数正确。
测试结果|Attach成功。MME向SGW发送Create Session Request消息，Indication Flags中携带CRSI (ChangeReporting support indication)标记，保存该字段到PDN连接上下文；MME向SGW发送的Modify BearerRequest消息，Indication Flags中携带CRSI (Change Reporting support indication)标记。MME保存Change Reporting Action字段到PDN连接上下文。向eNodeB发送LOCATION REPORTING CONTROL消息，请求eNodeB实时上报用户的小区信息。向SGW发送Change Notification Request消息，参数正确。
## ZUF-78-13-004 LCS 
特性描述 :特性描述 :术语 :术语|含义
---|---
定位业务LCS|指确定终端所在的地理位置，以及由此所关联的业务。
SLg|MME和GMLC之间的接口。
SLs|MME和E-SMLC之间的接口。
描述 :定义 :LCS（定位业务）是一种提供移动用户位置信息的业务。提供的位置信息可以被网络内部使用，也可以被第三方使用。
LCS涉及的实体包括LCS服务方、LCS客户方、以及被定位的目标用户。 
应用场景 :该功能典型的应用包括： 
用于网络内部使用，如改善网络运行性能、网络维护、支持补充业务、支持移动智能业务等。用于商用的增值业务。如根据用户当前位置给予向导服务。 
MME用于紧急呼叫时确定起呼用户位置。 
用于经批准的安全部门跟踪用户位置。 
客户收益 :受益方|受益描述
---|---
运营商|支持LCS业务，吸引用户加入。
移动用户|适用LCS业务。
实现原理 :系统架构 :LCS业务的网络模型如[图1]所示。
图1  LCS业务的网络模型图

涉及的网元 :LCS业务的实现需要HSS、GMLC、E-SMLC、MME、eNodeB的共同配合。
网元名称|网元作用
---|---
HSS|存储用户的LCS签约信息，同时把用户拜访的MME提供给GMLC。
GMLC|发起用户的定位。
E-SMLC|完成用户的位置计算。
MME|完成各种信令的处理，以及数据的传递。
业务流程 :UE被动的正常定位
UE被动的正常定位流程如[图2]所示。
图2  UE被动的正常定位流程图

流程说明： 
外部的LCS客户端发起定位请求，消息发送给R-GMLC。消息中包括MSISDN（或者IMSI或者UE假名）和LCS 的QoS。对于呼叫相关的定位，包括被动号码。会话相关的定位，包括APN-NI。消息中还需要携带LCS的Service
ID，用于R-GMLC的客户端合法性检查。消息中有可能带H-GMLC的地址，如果没有，R-GMLC需要从网元PMD中读取。 
（可选）如果R-GMLC没有H-GMLC的地址，则发SEND_ROUTING_INFO_FOR_LCS到HSS要H-GMLC的地址；如果有H-GMLC的地址，则跳过此步骤。 
HSS返回MME的信息、H-GMLC的地址、IMSI/MSISDN、V-GMLC的地址、PPR的地址等信息。
如果R-GMLC和H-GMLC属于不同的网元，则R-GMLC发送定位请求给H-GMLC。 
隐私检查。在H-GMLC完成，或者通知PPR完成。 
（可选）如果H-GMLC不知道用户的IMSI/MSISDN、V-GMLC的地址、MME的地址等，则发SEND_ROUTING_INFO_FOR_LCS到HSS。如果知道上述的信息，则跳过此步。 
HSS返回MME的信息、H-GMLC的地址、IMSI/MSISDN、V-GMLC的地址、PPR的地址等信息。 
如果H-GMLC不知道V-GMLC的地址，或者H-GMLC与V-GMLC相同，或者运营商的要求，H-GMLC无需发消息给V-GMLC，否则H-GMLC发定位请求给V-GMLC。 
被动定位过程。 
V-GMLC回复定位响应给H-GMLC。 
进行隐私检查。 
如果隐私检查判断需要通知信息，则H-GMLC发定位请求给V-GMLC，同时指明仅仅是通知。 
通知发送过程。 
V-GMLC回复定位响应给H-GMLC。 
H-GMLC回复定位响应给R-GMLC。 
R-GMLC回复定位响应给LCS客户端。 
普通的立即定位
普通的立即定位的流程如[图3]所示。
图3  普通的立即定位的流程图

流程说明： 
LCS的客户端发起定位请求。 
GMLC发送Provide Subscriber Location消息给MME。消息携带IMSI、定位的类型、LCS的Qos、APN-NI等。 
如果GMLC在第2步指示支持delayed location reporting，并且MME支持用户临时不可达的延迟定位，同时用户处于临时不可达状态，则MME回Provide Subscriber Location ack给GMLC，同时携带原因值UE transiently not reachable。 
GMLC回复LCS Service Response给client。 
MME收到此消息后，先鉴权接入的GMLC是否合法：其他PLMN的GMLC或者其他国家的GMLC，如果不支持，则回复错误。如果PSL消息指示了隐私相关的动作，MME需要读取隐私相关的动作。如果PSL消息没有隐私相关的动作，则MME需要根据用户的Profile来拦截LCS的客户端，如果在拦截之列，则回复错误响应给GMLC。否则，如果处于空闲态，应发起网络寻呼触发的业务请求流程，用于UE与MME建立连接。 
如果用户的隐私要求通知UE，MME发送NAS Location Notification Invoke给用户，消息中包含LCS客户端类型、LCS的名称等。MME可以无须等待NAS Location Notification Return Result的响应消息，并行发起Location Request给E-SMLC 
UE判断和鉴权是否允许定位。如果不允许，MME回复错误的响应给GMLC。 
MME选择一个E-SMLC。发送Location Request消息给RAN，消息中包括定位类型、Qos以及其他参数。一旦MME选择好一个E-SMLC后，本次定位过程必须使用同一个E-SMLC。特别的，MME支持根据GMLC来选择ESMLC的定制功能。 
E-SMLC计算出UE的位置信息 
E-SMLC回复响应消息给MME，指明是否定位成功。如果不成功，携带失败原因 
如果2a步骤没有发生，如果MME没有进行隐私检查过程，则回复定位的响应给GMLC，包括位置信息、生存期等信息。否则，在收到UE的隐私检查允许时，仅回复位置信息和计算方法给GMLC。如果UE的隐私检查拒绝，MME回复失败响应给GMLC。如果定位过程失败，但隐私检查通过，同时LCS客户端要求了当前或者最后的位置信息，则MME把此信息发送给GMLC。 
如果2a步骤发生，MME把定位结果通过Subscriber Location Report消息发给GMLC。 
GMLC回复响应。 
通知和验证过程
通知和验证过程的流程如[图4]所示。
图4  通知和验证过程的流程图

流程说明： 
LCS的客户端发起通知和验证过程请求。 
GMLC发送Provide Subscriber Location消息给MME。消息指示notification only，并携带IMSI、定位的类型、LCS的Qos、APN-NI等。 
MME收到此消息后，先进行隐私鉴权等。如果处于空闲态，应发起网络寻呼触发的业务请求流程，用于UE与MME建立连接。 
MME发送通知消息给UE。 
UE通知用户，等待用户的允许或者拒绝。通知MME，指明同意或者拒绝。如果用户拒绝，MME回复错误的响应给GMLC。 
MME回复响应给GMCL。 
UE紧急定位
UE紧急定位的流程如所[图5]示。
图5  UE紧急定位的流程图

流程说明： 
外部的LCS客户端发起定位请求，消息发送给R-GMLC。消息中指明是紧急定位。 
（可选）如果R-GMLC没有MME的地址，则发SEND_ROUTING_INFO_FOR_LCS到HSS；如果有MME的地址，则跳过此步骤。 
HSS返回MME的地址等信息。 
如果R-GMLC和V-GMLC属于不同的网元，则R-GMLC发送定位请求给V-GMLC。 
被动定位过程。 
V-GMLC回复定位响应给R-GMLC。 
R-GMLC回复定位响应给LCS客户端。 
紧急的定位
紧急的定位的流程如[图6]所示。
图6  紧急的定位流程图

流程说明： 
LCS客户端发起紧急定位请求。 
GMLC根据之前的信息发送Provide Subscriber Location给MME，消息中带IMSI/MSISDN/IMEI、紧急定位的指示。 
MME判断是紧急被动定位，MME发送Location Request给E-SMLC。 
E-SMLC定位用户。 
E-SMLC返回位置信息。 
MME回复响应给GMLC，包含位置信息等。如果E-SMLC返回失败等，MME把用户的最后位置信息发给GMLC。 
LCS客户端收到紧急定位响应。 
MME触发的紧急的定位
MME触发的紧急的定位的流程如[图7]所示。
图7  MME触发的紧急的定位的流程图

流程说明： 
UE发起紧急附着、紧急PDN连接等，MME需要触发紧急定位流程。 
MME选择一个E-SMLC发送Location Request给E-SMLC。 
E-SMLC定位用户。 
E-SMLC返回位置信息。 
MME选择一个GMLC。MME发送Subscriber Location Report消息给GMLC，包含位置信息等。 
GMLC回复响应给MME。 
GMLC把信息转发给LCS客户端。 
切换的定位
切换的定位的流程如[图8]所示。
图8  切换的定位流程图

流程说明： 
UE触发紧急业务，比如：紧急附着、紧急PDN连接等。 
GMLC发起被叫定位。 
MME触发被叫定位过程。 
UE进行切换。 
原MME/SGSN发起切换。 
切换过程。 
如果定位过程没有结束，则原MME/SGSN停止定位过程。 
服务节点（MME）在切换完成后，发现是紧急业务，则触发定位业务，上报位置信息给GMLC。 
GMLC回复响应。 
UE主动的定位
UE主动的定位的流程如[图9]所示。
图9  UE主动的定位流程图

流程说明： 
UE需要发起定位，如果处于空闲态，则发起Service Request流程，同时可能有安全检查的过程；如果用户处于连接态，则跳过此步。 
UE发送MO-LR Request消息给MME。包括的定位类型：location estimate of the UE,
location estimate of the UE to be sent to an external LCS client,
location assistance data or broadcast assistance data message ciphering
keys。消息携带LPP参数等，当UE选择location estimate of the UE to be sent to an
external LCS client时，需要携带LCS的ID，GMLC的地址（可选）。同时MME需要分配V-GMLC的地址。 
MME选择一个E-SMLC，向此E-SMLC发送Location Request消息。 
E-SMLC定位用户。 
E-SMLC返回位置信息Lcation Report。 
如果定位成功，MME发Subscriber Location Report给V-GMLC，包含位置信息等。 
V-GMLC判断UE是否是location estimate of the UE to be sent to an external
LCS client的类型，如果外部的LCS客户端不可用，则回响应给SGSN；否则发消息给H-GMLC（从HLR得到H-GMLC的地址）。 
H-GMLC发消息给R-GMLC。 
R-GMLC发消息给LCS客户端。 
LCS客户端回复Location Information ack给R-GMLC，指明成功或者失败。 
R-GMLC回复Location Information ack给H-GMLC，指明成功或者失败。 
H-GMLC回复Location Information ack给V-GMLC，指明成功或者失败。 
V-GMLC回复Subscriber Location Report Ack给MME，指明成功或者失败。 
MME回复NAS MO-LR Response给UE，指明成功或者失败。同时计费。 
UE协助定位（E-SMLC的定位）
UE协助定位的流程如[图10]所示。
图10  UE协助定位的流程图

流程说明： 
E-SMLC发送Location Information Message给MME，携带下行的定位信息。 
MME把NAS Transport消息发给eNodeB。 
eNodeB把DL positioning Message消息发给UE。 
UE进行定位并计算出位置信息。 
UE返回结果。 
eNodeB把结果转发给MME。 
MME把结果转发给E-SMLC。 
网络侧协助定位（E-SMLC的定位）
网络侧协助定位的流程如[图11]所示。
图11  网络侧协助定位的流程图

流程说明： 
E-SMLC发送Location Information message给MME，携带下行的定位信息。 
MME把S1-AP Transport Message消息发给eNodeB。 
eNodeB获得相关的信息。 
eNodeB返回结果。 
MME把结果转发给E-SMLC。 
获取用户最新的位置信息
获取用户最新的位置信息的流程如[图12]所示。
图12  获取用户最新的位置信息流程图

流程说明： 
执行MT定位流程，在通知用户，得到响应。 
发送Location Report Control消息给eNodeB要用户的最新位置信息。 
eNodeB返回用户的最新位置信息。 
继续执行定位流程。 
 说明： 
如需启用该功能，需要将软件参数“786704
”
的值设置为1。
系统影响 :一般情况下，LCS业务对MME系统基本无影响。只有在大话务量、并且存在大量用户定位的情况下，会增加MP的CPU负荷。对其他业务无影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称
---
3GPP TS 23.271 Functional stage 2 description of Location Services(LCS)
3GPP TS 29.171 Location Services (LCS); LCS Application Protocol(LCS-AP) between the Mobile Management Entity (MME) and Evolved ServingMobile Location Centre (E-SMLC); SLs interface
3GPP TS 29.172 Location Services (LCS); Evolved Packet Core(EPC) LCS Protocol (ELP) between the Gateway Mobile Location Centre(GMLC) and the Mobile Management Entity (MME); SLg interface
3GPP TS 24.080 Mobile radio interface layer 3 supplementaryservices specification; Formats and coding
3GPP TS 29.002 Mobile Application Part (MAP) specification
3GPP TS 32.251 Telecommunication management; Charging management;Packet Switched (PS) domain charging
特性能力 :该特性不涉及规格指标。 
可获得性 :License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持LCS功能”（license ID：7088），此项目显示为“支持”，表示MME支持LCS功能。
对其他网元的要求 :UE|eNodeB|GLMC|E-SMLC|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项 
配置项|命令
---|---
MME VGMLC配置|ADD MME VGMLCSET MMEVGMLCDEL MME VGMLCSHOW MME VGMLC
E-SMLC配置|ADD ESMLCSET ESMLCDEL ESMLCSHOW ESMLC
E-SMLC组标识配置|ADD ESMLCGRPIDSET ESMLCGRPIDDEL ESMLCGRPID SHOW ESMLCGRPID
Diameter GMLC局向路由配置|ADD DIAMGMLCROUTESETDIAMGMLCROUTEDEL DIAMGMLCROUTESHOW DIAMGMLCROUTE
Diameter GMLC局向配置|ADD DIAMGMLCADJSET DIAMGMLCADJDEL DIAMGMLCADJSHOW DIAMGMLCADJ
Diameter GMLC分析结果索引配置|ADD DIMGMLC ANALYSISSETDIMGMLC ANALYSISDEL DIMGMLC ANALYSISSHOW DIMGMLC ANALYSIS
Diameter路由配置|ADD DIAMROUTESET DIAMROUTEDEL DIAMROUTESHOW DIAMROUTE
Diameter AVP profile配置|ADD DIM AVP PROFILESETDIM AVP PROFILEDEL DIM AVP PROFILESHOW DIM AVP PROFILESETDEFAULT DIM AVP PROFILECLEAR DEFAULT DIMAVP PROFILESHOW DEFAULT DIM AVP PROFILE
配置项|命令|新增参数
---|---|---
本局移动参数|SET COMBOCFGSHOW COMBOCFG|本局支持的LCS版本
移动号码分析|ADD MDNALSET MDNALDEL MDNALSHOW MDNAL|GMLC邻接局分析
分组域参数配置|SET PACKET DOMAIN PARAMETERSHOW PACKET DOMAIN PARAMETER|MME支持紧急定位参数
跟踪区配置|ADD TASET TADEL TASHOW TA|紧急GMLC号码
容量配置|SET CAPACITYSHOW CAPACITY|LCS资源容量(单模块)
软件参数 
新增软件参数。 
软件参数ID|软件参数名称
---|---
65835|MME支持LCS功能
性能统计 :测量类型|描述
---|---
LCS测量|编号为C43014开头的所有计数器
LCSAP消息测量|C432050001 定位请求消息发送次数C432050002 定位响应消息接收次数
Diameter消息测量|编号为C43202开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置，实现LCS业务功能。 
配置前提 :完成LTE业务基本配置，可以进行基本的EPC业务。 
配置过程 :设置license支持LCS功能，设置软参65835支持LCS功能。 
执行[ADD MME VGMLC]命令，增加MME VGMLC配置。
执行[ADD ESMLC]命令，增加E-SMLC配置。
执行[ADD DIAMGMLCROUTE]命令，增加Diameter GMLC局向路由配置。 
执行[ADD DIAMGMLCADJ]命令，增加Diameter GMLC局向配置。
执行[ADD DIMGMLC ANALYSIS]命令，增加Diameter GMLC分析结果索引配置。
执行[ADD DIAMROUTE]命令，增加Diameter路由配置。
执行[ADD DIM AVP PROFILE]命令，增加Diameter AVP Profile配置。
执行[ADD TA]命令，增加跟踪区配置。
执行[SET CAPACITY]命令，修改容量规划配置。
执行[SET PACKET DOMAIN PARAMETER]命令，设置支持紧急定位参数。
执行[ADD MDNAL]命令，增加移动号码分析。
配置实例 :MME VGMLC配置配置脚本配置说明ADD MME VGMLC:VGMLCADDR="192.0.1.165",NAME="test1"新增MME VGMLC配置 
E-SMLC配置配置脚本配置说明ADD SCTP:ID=4112,NAME="E-SMLC_1",ROLE="CLT",VPNID1=2,LOCADDR1="192.10.100.22",LOCPORT=49601,REMADDR1="192.10.51.1",REMPORT=49601,PROTOCALTYPE=28增LCSAP静态偶联配置ADD SCTPIDCFGSCTPID=4112,TYPE="LCSAP"新增偶联索引ADD ESMLC:ESMLCID=232,SCTPID=4112,NAME="test1"新增E-SMLC配置 
Diameter GMLC局向路由配置配置脚本配置说明ADD SCTP:ID=332,NAME="DIM332",ROLE="CLT",VPNID1=2,LOCADDR1="192.168.0.18",LOCPORT=11332,REMADDR1="192.168.0.133",REMPORT=11332,PROTOCALTYPE=29ADD SCTPIDCFG:SCTPID=332,TYPE="DIM"增Diameter偶联配置ADD DIAMCONN:ADJNAME="DIM332.zte.com.cn",ADJDOMAIN="zte.com.cn",SCTPID=332,NAME="DIM332"新增Diameter连接配置ADD DIAMLINKGROUP:LINKGRPID=332,SCTPLINKID=332,PARTAKEMODE="PARTAKE",USERLABEL="test1"
新增Diameter链路组配置ADD DIAMROUTE:ROUTEID=332,LINKGRPID=332,PROPERTY="PARTAKE",USERLABEL="test1"新增DIAMETER静态路由配置ADD DIAMROUTEGROUP:ROUTEGRPID=332,ROUTEID=332,PROPERTY="PARTAKE",USERLABEL="test1"新增DIAMETER路由组配置ADD DIAMGMLCROUTE:GMLCROUTEID=332,ROUTEGROUP=332,PROPERTY="PARTAKE",DFTROUTE="YES",REALM="zte.com.cn",HOSTNAME="DIM332.zte.com.cn",NAME="332"新增Diameter GMLC局向路由配置 
Diameter GMLC局向配置配置脚本配置说明ADD DIAMGMLCADJ:GMLCADJID=332,GMLCROUTEID=332,AVPPROFILEID=2,NAME="test1"新增Diameter GMLC局向配置 
Diameter GMLC分析结果索引配置配置脚本配置说明ADD DIMGMLC ANALYSIS:IDX=256,DIAMGMLCID=332,NAME="test1"新增Diameter GMLC分析结果索引配置 
Diameter AVP Profile配置配置脚本配置说明ADD DIM AVP PROFILE:PROFILEID=1,AVPCODE1="1034",MINDICATOR="YES",VINDICATOR="YES",
PINDICATOR="NO",VENDERID=0,COMMANDNAME="PLR",NAME="test1"新增Diameter AVP Profile配置 
跟踪区配置配置脚本配置说明ADD TA:TAID=168,GRPID=1,MCC="460",MNC="07",TAC="AAAA",TIMEZONE="GMT
+08:00",LISTID=0,GMLCNUM="8613900131",NAME="test1"新增跟踪区配置 
分组域参数设置配置脚本配置说明SET PACKET DOMAIN PARAMETER:OVERLOADINLCS="YES",MMESUPLCS="YES"设置分组域参数 
移动号码分析配置配置脚本配置说明ADD MDNAL:DGT="861390000321",ENTR="DAS_GMLC",RST=256,NAME="test1"新增移动号码分析 
设置容量规划配置脚本配置说明SET CAPACITY:BOARDTYPE="SBCJ",LCSNUM=2048,LCSMME=100000设置容量规划 
定位GMLC配置配置脚本配置说明ADD MME GMLC:GMLCNAME="CNGMLC"新增定位GMLC配置 
测试用例 :测试项目|MME-MT LCS
---|---
测试目的|验证MT定位功能
预置条件|各网元运行正常。License开启支持LCS功能，软参65835设置为支持LCS功能。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|用户已经附着成功，建立承载。MME收到GMLC发送来的PLR消息，携带定位类型、用户的标识、LCS客户端信息、LCS Qos、LCS的优先级等。
通过准则|MME发送Location Request消息给E-SMLC，消息中包括定位类型、QoS等参数。定位成功，MME收到Location Response。MME回复PLA给GMLC，包括位置信息、生存期等信息。信令跟踪、性能统计信息正确。
测试结果|-
测试项目|MME-PPNV
---|---
测试目的|验证PPNV功能
预置条件|各网元运行正常。License开启支持LCS功能，软参65835设置为支持LCS功能。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|用户已经附着成功，建立承载。GMLC发送PLR消息给MME。消息指示notification only，并携带IMSI、定位的类型、LCS的Qos、APN-NI等。
通过准则|MME发送通知消息给UE。MME回复PLA给GMLC。信令跟踪、性能统计信息正确。
测试结果|-
测试项目|MME-紧急定位
---|---
测试目的|验证紧急定位功能
预置条件|各网元运行正常。License开启支持LCS功能，软参65835设置为支持LCS功能,，MME支持紧急定位参数开关打开。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|用户通过紧急附着流程上线，附着成功之后触发紧急定位流程。
通过准则|MME发送Location Request给E-SMLC。MME收到Location Response消息后，发送LRR消息给GMLC，包含位置信息等。信令跟踪、性能统计信息正确；
测试结果|-
测试项目|MME-MO LCS
---|---
测试目的|验证MO定位功能
预置条件|各网元运行正常。License开启支持LCS功能，软参65835设置为支持LCS功能。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|UE发送MO定位消息给MME，包括定位类型、LPP参数等；
通过准则|MME向E-SMLC发送Location Request消息，E-SMLC定位用户成功。定位成功，MME发 Location Report Request给V-GMLC，包含位置信息等。V-GMLC返回Location Report Answer，定位成功。信令跟踪、性能统计信息正确。
测试结果|-
常见问题处理 :网管中已经添加LCS配置，但无法做LCS业务。处理建议：检查是否打开License开关及软参65835是否打开。 
从不支持LCS改为支持，每模块只能支持一个LCS用户。处理建议：不支持LCS功能时，容量设置每模块LCS用户为1。改为支持LCS时记得要修改容量的配置。 
MT定位失败。处理建议：MT定位时，SGSN/MME会判断GMLC是否在允许列表中，不在将导致定位失败。 
对于MME开启LCS功能后，由于MME在update location request消息携带的MME support
features包括了LCS能力，bit为18、20，可能有的HSS不支持该功能，导致用户附着失败。Supported-Features
            Feature-List
                Code:Feature-List(630)
                flags : [V]
                length:16
                Vendor: 3GPP(10415)
                Unsigned32 : 403963904
                    Bit 18 = LCS-BasicSelfLocation :  Set
                    Bit 20 = LCS-TransferToThirdParty :  Set
处理建议：可以通过开启软参262356，设置支持Support Feature协商，通过FEATURE再协商功能，再次发起更新时不再携带HSS不支持的Feature，保证与HSS对接成功。 
## ZUF-78-13-005 PRA 
特性描述 :特性描述 :描述 :定义 :PRA功能能立即感知UE进入或离开指定区域，便于在指定区域进行话务控制和拦截。本功能在PCRF上进行区域监视，并通过PGW通知MME。当UE在监控区域活动时，MME向PGW上报事件，PGW向PCRF上报事件。
背景知识 :在EPC网络中位置标识一般用在基于位置提供不同服务与计费策略。
位置标识来源于无线规划，MME从无线获得位置标识后可传递给其他网元。PCRF基于位置标识提供服务策略，计费中心基于位置提供计费策略。 
应用场景 :描述 :基于位置标识组网络提供计费和服务，可以分为： 
基于实时位置标识组计费 
基于位置标识组提供服务策略 
###### 基于实时位置标识组计费：PRA+小区位置上报 
场景特点：
系统基于用户进入或离开某位置标识组进行计费，由于涉及用户资费，对用户位置的实时性和精度均要求高，这样可以避免误判。 
具体的场景比如校园网：校园网由一组位置标识组成，用户进入或离开校园网范围时，采用不同的计费策略。 
解决方案：
PGW下发位置标识组到MME，MME本地保存，MME请求无线上报用户当前所在位置标识，MME基于下发的位置标识组判断用户是否离开或进入此区域，并将结果上报给PGW，PGW传递给PCC计费系统。
###### 基于位置标识组提供服务策略：PRA 
场景特点：
系统基于用户进入或离开某位置标识组进行服务策略，如果位置标识不准确导致提供非期望的服务质量，则对于企业网用户影响并不大，并且位置标识也能在用户进行业务时被修正，因此此场景对于用户位置的实时性和精度要求不高。 
具体的场景比如企业网：企业网由一组位置标识组成，用户进入或离开企业网范围时，采用不同的服务策略。 
解决方案：
PGW下发位置标识组到MME，MME本地保存，用户发起业务时MME从业务消息中得到用户的位置标识，同时MME基于下发的位置标识组判断用户是否离开或进入此区域，并将结果上报给PGW，PGW上报给服务策略系统。 
客户收益 :受益方|受益描述
---|---
运营商|提高策略灵活性：基于用户位置标识为用户提供灵活的服务与计费策略。丰富业务功能： 为用户提供定位能力，便于紧急呼叫时救援，以及方便开展各种与位置相关的增值服务。
移动用户|提高终端用户体验。用户在某些区域可获得更优费率或更好的服务质量，同时可获得终端定位能力，可使用各种与位置相关的增值服务。
实现原理 :系统架构 :LCS定位需要新增E-SMLC与GMLC网元支持，GMLC网元为定位中心，管理控制用户的定位业务。E-SMLC网元为定位计算单元，计算用户的地理位置。系统结构如[图1]所示。
图1  LCS定位网络架构图

涉及的网元 :网元名称|网元作用
---|---
eNodeB|用户进行业务时eNodeB上报用户所在的位置标识（TAI/ECGI）信息。用户发生移动位置发生变化时，eNodeB上报最新位置标识（TAI/ECGI）信息给MME。接收定位请求，上报用户所在的地理位置信息。
E-SMLC|定位测量用户所在的地理位置。
GMLC|管理控制用户的定位业务，接收与下发用户所在的地理位置信息。
HSS|HSS处理AS定位服务器请求位置的要求，从MME获得位置标识后上报给AS定位服务器。
MME|MME从eNodeB获得用户所在位置标识，上报给PGW与HSS网元。MME获得用户所在位置标识，判断用户进入或离开某组位置标识并上报给PGW。MME接收GMLC的定位请求，查找用户对应的E-SMLC网元，转发定位请求到E-SMLC。
PGW|PGW通知MME上报位置标识信息。PGW下发一组位置标识到MME。PGW接收MME上报的位置标识或进入与离开某组位置标识的标示。
业务流程 :PRA功能涉及Attach、TAU、PDN连接、承载激活/修改及切换流程。 
Attach流程
PRA功能Attach流程如[图2]所示。
图2  PRA功能Attach流程图

流程说明： 
UE发起附着流程。 
MME向SGW发送Create Session Request请求。SGW把Create Session Request请求转发给PGW。 
PGW返回Create Session Response响应给SGW，SGW转发Create Session Response给MME，其中携带PRA布控信息。 
MME向SGW发送Modify Bearer Request请求，其中携带用户是否离开或进入PRA区域。SGW把Modify
Bearer Request请求转发给PGW。 
PGW返回Modify Bearer Response响应给SGW，SGW转发Modify Bearer Response消息给MME。 
如需要获取用户实时所在位置标识，启用小区位置上报功能，MME下发Location Report Control消息给eNodeB。 
局间TAU
PRA功能局间TAU流程如[图3]所示。
图3  PRA功能局间TAU流程图

流程说明： 
UE发起TAU流程。 
New MME判断为局间TAU，发送Context Request向老局MME要用户上下文信息。 
老局MME返回Context Response消息给New MME，携带PRA布控信息。 
New MME基于PRA布控信息判断用户是否进入或离开PRA区域，向SGW发送Create Session Request其中携带是否进入或离开PRA区域信息。 
SGW返回Create Session Response消息给New MME。 
New MME向SGW发送Modify Bearer Request消息。SGW把Modify Bearer Request消息传给PGW。 
PGW返回Modify Bearer Response消息给SGW，SGW把Modify Bearer Response消息传给New
MME。 
如需要获取用户实时所在位置标识，启用小区位置上报功能，New MME下发Location Report Control消息给eNodeB。 
局内TAU/业务请求
PRA功能局内TAU/业务请求流程如[图4]所示。
图4  PRA功能局内TAU/业务请求流程图

流程说明： 
UE发起TAU或Service Request流程，MME判断TAU为局内TAU类型。 
根据SGW的情况，MME做如下选择： 
MME判断如SGW发生改变，则向新SGW发送Create Session Request，其中携带是否进入或离开PRA区域信息。SGW返回Create
Session Response消息给MME。 
MME判断如SGW发生未改变，则向新SGW发送Modify Bearer Request，其中携带是否进入或离开PRA区域信息。SGW返回Modify
Bearer Response消息给MME。 
如需要获取用户实时所在位置标识，启用小区位置上报功能，MME下发Location Report Control消息给eNodeB。 
局间S1切换
PRA功能局间S1切换流程如[图5]所示。
图5  PRA功能局间S1切换流程图

流程说明： 
eNodeB发起切换发送Handoff Required消息给MME。 
Source MME判断为局间切换，向目标MME发送Forward Relocation Request消息，携带PRA布控信息。 
Target MME基于PRA布控信息判断用户是否进入或离开PRA区域，向SGW发送Create Session Request其中携带是否进入或离开PRA区域信息。 
SGW返回Create Session Response消息给Target MME。 
New MME发起Modify Bearer流程，继续完成切换流程。 
如需要获取用户实时所在位置标识，启用小区位置上报功能，Target MME下发Location Report Control消息给eNodeB。 
局内S1/X2切换
PRA功能局内S1/X2切换流程如[图6]所示。
图6  PRA功能局内S1/X2切换流程图

流程说明： 
eNodeB发起切换，发送Handoff Required或Path Switch Request消息时MME判断为局内切换。 
根据SGW的情况，MME做如下选择： 
MME判断如SGW发生改变，则向新SGW发送Create Session Request，其中携带是否进入或离开PRA区域信息。SGW返回Create
Session Response消息给MME。 
MME判断如SGW发生未改变，则向新SGW发送Modify Bearer Request，其中携带是否进入或离开PRA区域信息。SGW返回Modify
Bearer Response消息给MME。 
如需要获取用户实时所在位置标识，启用小区位置上报功能，MME下发Location Report Control消息给eNodeB。 
系统影响 :在校园网和企业网场景下，由于需要用户精确实时的位置，需要eNodeB实时上报用户最新的ECGI信息，MME并上报给PGW。增加了无线与网络间消息量，会降低系统性能。如开启以上功能，对MME系统性能会下降，PGW网元接收消息量增加，同时eNodeB上报的消息量增加，对eNodeB的性能要求更高。 
开启地理位置LCS定位功能，需增加无线与网络的消息量，对于MME系统性能有影响，当定位的用户越多性能影响越大。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|5.3.2 Attach procedure5.3.3 Tracking Area Updateprocedures5.3.4 Service Request procedures5.4 Session Management, QoS and interaction with PCC functionality5.5 Handover5.9 Interactions with other services
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3".|全部
3GPP TS 23.271: Functional stage 2 description of LocationServices (LCS)|全部
3GPP TS 29.171: LCS Application Protocol (LCS-AP) between theMobile Management Entity (MME) and Evolved Serving Mobile LocationCentre (E-SMLC)|全部
3GPP TS 29.172: Evolved Packet Core (EPC) LCS Protocol (ELP)between the Gateway Mobile Location Centre (GMLC) and the Mobile ManagementEntity (MME)|全部
3GPP TS 29.272: "Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|5.2.2 Subscriber Data Handling Procedures
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"|7.2.1 Create Session Request7.2.4 Create Bearer Response7.2.8 Modify Bearer Response7.2.15 Update Bearer Request7.3.14 Change Notification Request
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"|8.11 Location Reporting Procedures
特性能力 :MME对一个会话最多支持两个PRA ID。 
可获得性 :License要求 :该特性对应License文件中的项目为ID=7085，名称为“MME支持PRA功能”，需要申请了License许可后，运营商才能获得该特性的服务。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :新增命令配置项参见[表1]。
配置项|命令
---|---
设置软件参数配置|SET SOFTWARE PARAMETER
批量新增PRA区域配置|ADD PRA AREA BATCH
传送数据|SYNA
###### 软件参数 
新增软件参数参见[表2]。
软件参数ID|软件参数名称
---|---
786797|MME支持局间消息携带PRA参数
786798|MME支持新局上报PRA的OPRA
786799|MME支持PRA个数The maximum number of PRA IDs supported by the MME PRA function
786800|PRA功能支持位置上报过程
特性配置 :特性配置 :配置说明 :对于动态PRA方式，MME只需要开启相应软参即可，不需要本地配置PRA区域。对于静态PRA方式，MME不仅要开启相应软参开关，还需要本地配置对应的PRA区域。 
配置前提 :MME已打开支持PRA功能的license。 
PGW与PCRF都已支持PRA功能。 
MME与SGW，PGW与PCRF之间的链路正常。 
配置过程 :打开PRA功能软参开关。 
根据与PCRF协商结果，决定是否需要本地配置PRA区域。 
配置实例 :###### 校园网计费 
场景说明
某高校针对本校学生开启校园优惠套餐，需要实时获取学生的位置信息来判断用户是否在校园网范围内，根据用户所在区域进行计费。 
同时PCRF与MME已协商，使用动态的PRA配置。 
配置步骤
步骤|操作|说明
---|---|---
1|SET SOFTWARE PARAMETER:PARAID= 786799,PARAVALUE=1或者SET SOFTWARE PARAMETER:PARAID= 786799,PARAVALUE=2|设置单个PDN支持PRA的个数，相当于打开功能开关
2|SET SOFTWARE PARAMETER:PARAID= 786797,PARAVALUE=1SET SOFTWARE PARAMETER:PARAID= 786798,PARAVALUE=1|开启辅助开关
3|SET SOFTWARE PARAMETER:PARAID= 786800,PARAVALUE=1|开启PRA实时判断的开关
4|SYNA|同步数据
###### 企业网高服务质量 
场景说明
某企业为本单位员工提供更高的服务质量，需要根据员工当前的位置信息来判断用户是否在企业网范围内，根据用户所在区域提供服务质量。允许有一些误差时延。 
同时PCRF与MME已协商，使用静态的PRA配置。 
假如企业网占用6个enodeB小区，小区ID即ECGI为32115001-
32115006\PRA ID为8388608\PLMN为460-11。 
配置步骤
步骤|操作|说明
---|---|---
1|SET SOFTWARE PARAMETER:PARAID= 786799,PARAVALUE=1或者SET SOFTWARE PARAMETER:PARAID= 786799,PARAVALUE=2|设置单个PDN支持PRA的个数，相当于打开功能开关
2|SET SOFTWARE PARAMETER:PARAID= 786797,PARAVALUE=1SET SOFTWARE PARAMETER:PARAID= 786798,PARAVALUE=1|开启辅助开关
3|ADD PRA AREA BATCH:AREAID=8388608,TYPE="ECGI",MCC="460",MNC="11",AREAINFOBEGIN=32115001,AREAINFOEND=32115006|本地配置PRA区域
4|SYNA|同步数据
测试用例 :测试项目|MME能够根据部署的PRA区域判断用户是否在该区域内。
测试目的|验证MME可以判断用户的PRA状态，并传递给PGW。
预置条件|EPS网络中各网元系统及操作维护台运行正常。用户在HSS中已签约EPS业务。在MME上建立用户跟踪。MME开启PRA功能，本地配置PRA区域。PCRF设置静态PRA类型。
测试过程|UE在EPC网络开机发起附着。
通过准则|UE附着成功，默认承载建立成功。MME在create session response中收到PRA ID，在modify bearer request消息中携带PRA状态出去。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|—
# 缩略语 
# 缩略语 
## CS 
Circuit Switched电路交换
## E-SMLC 
Evolved Serving Mobile Location Center演进的服务位置中心
## ECGI 
E-UTRAN Cell Global IdentifierE-UTRAN小区全球标识
eNodeB :Evolved NodeB演进的NodeB
EPC :Evolved Packet Core演进的分组核心网
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
HSS :Home Subscriber Server归属用户服务器
IMSI :International Mobile Subscriber Identity国际移动用户标识
## LCS 
LoCation Services定位业务
LTE :Long Time Evolution更长期发展
MME :Mobility Management Entity移动管理实体
## MPS 
Mobile Positioning System移动定位系统
MSISDN :Mobile Station International Subscriber Directory Number移动台国际用户目录号
PCC :Policy and Charging Control计费和策略控制
PCRF :Policy and Charging Rules Function策略和计费规则功能
PGW :PDN Gateway分组数据网网关
## PRA 
Presence Reporting Area出现上报区域
QoS :Quality of Service服务质量
SCTP :Stream Control Transmission Protocol流控制传输协议
## SMLC 
Serving Mobile Location Center服务移动定位中心
## TAI 
Tracking Area Identity跟踪区标识
TAU :Tracking Area Update跟踪区域更新
UE :User Equipment用户设备
# ZUF-78-14 非3GPP交互 
概述 :功能描述 :用户可以通过3GPP接入网络接入EPC，也可以通过non-3GPP接入网络接入EPC。 
UE可以在3GPP和non-3GPP网络间移动，会话保持不变。常见的non-3GPP包括CDMA接入、WLAN接入等。 
使用S2a或S2b接口的non-3GPP和3GPP互操作架构图如[图1]所示。
图1  non-3GPP和3GPP互操作架构图-S2a或S2b接口

使用S2c接口的non-3GPP和3GPP互操作架构图如[图2]所示。
图2  non-3GPP和3GPP互操作架构图-S2c接口

功能特性简介 :针对和非3GPP切换的应用特点和应用场景，核心网为满足用户的要求，提供了有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
E-UTRAN与CDMA2000之间非优化切换|对于支持CDMA2000和E-UTRAN的双模终端，网络可为其提供CDMA2000和E-UTRAN间的切换，以保证用户业务连续性。CDMA2000和E-UTRAN间切换分为非优化切换和优化切换。非优化切换是指UE先断开旧的连接，再捕获和接入目标网络。E-UTRAN与CDMA2000之间非优化切换的具体流程参见3GPP 23.402协议。|ZUF-78-14-001 E-UTRAN与CDMA2000之间非优化切换
E-UTRAN与CDMA2000之间优化切换|E-UTRAN与CDMA2000之间优化切换是指允许UE在离开E-UTRAN网络前，UE先预注册到切换目标网络，执行切换时，通知目标系统预留资源，再断开旧的连接，接入目标网络。优化切换可以最小化UE从E-UTRAN切换到CDMA2000时的业务中断时间。E-UTRAN与CDMA2000之间优化切换的具体流程参见3GPP 23.402协议。|ZUF-78-14-002 E-UTRAN与CDMA2000之间优化切换
3GPP与WLAN之间切换|对于支持WIFI和E-UTRAN的双模终端，网络可为其提供WIFI和E-UTRAN间的切换，以保证用户业务连续性。E-UTRAN与WIFI之间切换的具体流程参见3GPP 23.402协议。|ZUF-78-14-003 3GPP与WLAN之间切换
## ZUF-78-14-001 E-UTRAN与CDMA2000之间非优化切换 
特性描述 :特性描述 :术语 :术语|含义
---|---
MME池区|MME池区是指UE在其间移动不需要改变服务MME的区域。一个MME池区内有一个或多个对等的MME。MME池区是由多个TA汇聚。MME池区间可以有交迭。
SGW池区|SGW池区是指UE在其间移动不需要改变服务SGW的区域。一个SGW池区内有一个或多个对等的SGW。SGW池区是由多个TA汇聚。MME池区间可以有交迭。
默认APN|默认APN是在签约数据中被标识为默认的APN，用于在附着过程中建立默认的PDN连接。
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载。
专用承载|专用承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载。
AMBR|AMBR是用来限制每个UE所有非GBR承载的汇聚最大bit rate的QOS项。
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载。
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载。
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|在UE和PDN间存在的联系，该联系中一个IPV4或一个IPV6地址，或者两者都有代表一个UE；一个APN代表该PDN。
描述 :定义 :MME支持eHRPD接入和LTE接入间的非优化切换，主要包括：
在附着和PDN连接建立过程中，MME将新的PGW ID和APN等信息通过Notify流程通知HSS。
在附着和PDN连接建立过程中，如果Request Type为“Handover”，则直接使用HSS插入的PGW ID。 
MME给eNB下发切换限制列表时，“Forbidden inter RATs”既能根据签约数据获取，也可以直接取本地配置的值。
应用场景 :场景一 :UE从LTE移动到eHRPD网络下，EPS网络不支持LTE接入与eHRPD接入间的优化切换。 
场景二 :UE从eHRPD移动到LTE网络下，EPS网络不支持LTE接入与eHRPD接入间的优化切换。 
客户收益 :受益方|受益描述
---|---
运营商|对于有eHRPD网络的运营商来说，支持非优化切换，可以使eHRPD网络平滑地演进到LTE网络，尤其是在LTE建网初期。
移动用户|可以同时访问LTE网络和eHRPD网络。
实现原理 :系统架构 :非漫游架构
图1  非漫游场景下EPS通过S5-S2a进行移动性控制

图2  非漫游场景下EPS通过S5-S2c进行移动性控制

漫游架构
图3  漫游场景下EPS通过S8-S2a进行移动性控制(家乡路由)

图4  漫游场景下EPS通过S8-S2c进行移动性控制(家乡路由)

图5  漫游场景下EPS通过S8-S2a进行移动性控制 (Chained PMIP-based S8-S2a) (家乡路由)

图6  漫游场景下EPS通过S5-S2a进行移动性控制 (本地疏导)

图7  漫游场景下EPS通过S5-S2c进行移动性控制 (本地疏导)

关于S8-S2a漫游chain场景的说明： 
在3GPP定义了通过漫游地SGW统一支持非3GPP接入网络的场景称为S8-S2a
chain场景。同时，对该场景还定义了S8-S2a接口上基于PMIP协议的移动性管理流程。 
该场景的提出主要基于对简化网络漫游架构的考虑。从HSGW到(H)PGW的漫游接口经过漫游地SGW汇聚后一定程度上可以简化网络本身的架构。 
涉及的网元 :网元名称|网元作用
---|---
MME|PDN连接建立过程中，将新的APN/PGW ID信息通知HSS，如果Request Type为“Handover”，则直接使用HSS插入的PGWID。MME给eNB下发切换限制列表时，“Forbidden inter RATs”既能根据签约数据获取，也可以直接取本地配置的值
UE|支持eHRPD接入和LTE接入，支持eHRPD接入和LTE接入间的非优化切换
SGW|识别从eHRPD接入非优化切换到LTE接入
PGW|识别eHRPD接入和LTE接入间的非优化切换
HSS/AAA|记录APN/PGW ID信息，在插入用户签约数据给MME/HSGW时，也携带记录的APN/PGW ID信息
HSGW|支持eHRPD接入和LTE接入间的非优化切换
本网元实现 :附着或PDN连接建立过程中，如果Request type不是handover，签约数据允许用户切换到non-3GPP
，MME选择了一个新的PGW，则MME将新的APN/PGW ID信息通知HSS，PGW ID包含的内容通过软参“给HSS的PGW ID中包含的信息”控制： 
0：PGW ID包含PGW FQDN和IPv4地址。 
1：PGW ID包含PGW FQDN。 
2：PGW ID包含PGW IPv4地址。 
3：如果有PGW的IPv4地址，则PGW ID包含PGW IPv4地址，如果有PGW的IPv6地址，则PGW ID包含PGW
IPv6地址，如果有PGW的IPv4和IPv6地址，则PGW ID包含PGW IPv4和IPv6地址。 
4：PGW ID包含PGW FQDN和PGW的双栈地址（如果有双栈地址，则都包含，如果没有双栈地址，则包含PGW的单栈地址） 
附着或PDN连接建立过程中，如果Request type是handover，则直接使用HSS插入的PGW ID作为PGW。 
给eNB下发切换限制列表时，“Forbidden inter RATs”通过软参“切换限制列表中的被禁止的接入方式使用的策略”控制： 
0： Forbidden inter RATs取值为0（ALL）。 
1： Forbidden inter RATs取值为1（GERAN）。 
2： Forbidden inter RATs取值为2（UTRAN）。 
3： Forbidden inter RATs取值为3（CDMA2000）。 
4： Forbidden inter RATs取值为4（GERAN AND UTRAN）。 
5： Forbidden inter RATs取值为5（CDMA2000 and UTRAN）。 
6： Forbidden inter RATs为空。 
7：根据签约的ARD（Using subscribed access restriction data）的值获取Forbidden
inter RATs。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS); Servicedescription; Stage 1".|–
3GPP TS 23.402: "3rd Generation Partnership Project;TechnicalSpecification Group Services and System Aspects;Architecture enhancementsfor non-3GPP accesses"|-
特性能力 :名称|指标
---|---
可配置通知HSS的PGW ID包含的内容|可以仅包含PGW FQDN，或仅包含IP地址，或两者都包含。
可配置切换限制列表中的“Forbidden inter RATs”的策略|既能根据签约数据获取，也可以直接取本地配置的值。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V5.16.13|MME是V4.13.10及后续版本。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|–|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项该特性不涉及配置项的变化。 
安全变量该特性不涉及安全变量的变化。 
软件参数表1  新增软件参数软件参数ID软件参数名称786571给HSS的PGW ID中包含的信息786658是否忽略动态PGW ID的IP地址 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :配置3GPP与CDMA2000之间非优化切换。 
配置前提 :MME和周边网元接口通讯正常 
UE在MME上可以附着成功 
配置过程 :MME设置软参786571 给HSS的PGW ID中包含的信息值为1。
MME设置软参786658 是否忽略动态PGW ID的IP地址值为1。
配置实例 :设置软参“给HSS的PGW ID中包含的信息” 
命令脚本|解释说明
---|---
SET SOFTWARE PARAMETER:PARAID=786571,PARAVALUE=1|设置软参“给HSS的PGW ID中包含的信息”值为1
设置软参“是否忽略动态PGW ID的IP地址” 
命令脚本|解释说明
---|---
SET SOFTWARE PARAMETER:PARAID=786658,PARAVALUE=1;|设置软参“是否忽略动态PGW ID的IP地址”值为1
调整特性 :无 
测试用例 :测试项目|MME支持eHRPD接入和LTE接入间的非优化切换。
测试目的|验证MME在Notify Request消息携带的PGW ID正确。
预置条件|MME和邻接网元间通讯正常。软参“给HSS的PGW ID中包含的信息”设置为1。UE在HSS中签约动态PGW解析。
测试过程|UE开机发起附着流程。
通过准则|MME选择PGW成功，附着流程成功。MME发送Notify Request消息给HSS，消息中携带PGW ID只包含PGW FQDN。
测试结果|–
测试项目|MME支持eHRPD接入和LTE接入间的非优化切换。
测试目的|验证MME忽略动态PGW ID中的IP地址。
预置条件|MME和邻接网元间通讯正常。软参“给HSS的PGW ID中包含的信息”设置为1。UE在HSS中签约动态PGW解析。UE在eHPRD网管中接入成功，HSS中保存了接入PGW的FQDN和IP地址。
测试过程|UE在EPC网管发起附着，请求类型为Handover。HSS在ULA消息中将PGW的FQDN和IP地址都带给了MME。
通过准则|MME处理附着流程成功。MME根据PGW的FQDN进行解析PGW地址，不使用HSS携带的PGW IP地址。
测试结果|–
常见问题处理 :无 
## ZUF-78-14-002 E-UTRAN与CDMA2000之间优化切换 
特性描述 :特性描述 :描述 :定义 :对于支持eHRPD和E-UTRAN的双模终端，网络可为其提供eHRPD和LTE间的切换，以保证用户业务连续性。 
LTE与eHRPD间切换分为非优化切换和优化切换。 
非优化切换：UE先断开旧的连接，再捕获和接入目标网络。 
优化切换：UE在执行切换前，UE先预注册到切换目标网络，执行切换时，通知目标系统预留资源，再断开旧的连接，接入目标网络。 
无论非优化切换，还是优化切换，都是对数据业务的。 
背景知识 :不支持从LTE优化切换到eHRPD 
协议没有定义从eHRPD到LTE的优化切换的空口协议： 
从eHRPD到LTE的非优化切换时长很短（小于1秒）。 
一般eHRPD网络已全覆盖了。 
因此uMAC（MME）也仅实现了从LTE到eHRPD的优化切换，没有实现从eHRPD到LTE的优化切换。 
uMAC（MME）实现优化切换时，参考的2013年3月R11的3GPP协议和3GPP2协议。 
应用场景 :从eHRPD到LTE的优化切换没有需求，因此只需考虑从LTE到eHRPD的优化切换的应用场景 
eHRPD网络全覆盖，但LTE网络覆盖不充分，如LTE建网初期或LTE仅覆盖城区等 
应用场景图如下图所示： 
图1  应用场景示意图

应用场景说明： 
UE在区域B，eHRPD和LTE都覆盖，UE优选LTE接入并进行数据业务。 
UE从区域B移动到区域A或区域C，发生从LTE到eHRPD的优化切换。 
MME根据SECTORID中的eAN ID，确定eAN IP地址。 
MME从S1口接收到UL S1 CDMA2000 Tunneling消息，根据其中SECTORID中的eAN ID查找配置确定eAN
IP地址，向此IP地址发送S101消息。 
客户收益 :受益方|受益描述
---|---
运营商|在没有LTE网络提供服务的区域，快速的切换到eHRPD网络，既利用了原有eHRPD网络资源，又几乎没有影响用户的业务体验。
移动用户|用户移动时数据业务几乎不受影响
实现原理 :系统架构 :在3GPP 23.402-c00协议中，定义了eHRPD与LTE优化切换的框架，如[图2]所示。
图2  非漫游架构

图3  漫游架构，Home routed方式

优化切换需要MME网元和eAN网元互通，MME与IWS之间使用S101接口。 
 说明： 
对于漫游场景，3GPP
23.402-c00协议没有定义Local Breakout方式，只定义了Home Routed方式。 
涉及的网元 :网元名称|网元作用
---|---
UE|支持eHRPD和E-UTRAN的双模终端。需要支持从LTE到eHRPD的优化切换。
eNodeB|通知UE切换到eHRPD。接收DOWNLINK S1 CDMA2000 TUNNELING消息，提取其中封装CDMA2000层3信令透传给UE从UE接收CDMA2000层3信令封装在UPLINK S1 CDMA2000 TUNNELING 中发送给MME。
MME|接收UPLINK S1 CDMA2000 TUNNELING消息，提取其中内容封装在S101消息中发送给eAN。接收eAN下发的S101消息，提取其中内容封装在DOWNLINK S1 CDMA2000 TUNNELING消息中发送给eNodeB。记录用户选择的eAN的IP地址。处理从LTE到eHRPD的优化切换信令。
SGW|出S103接口，建立非直接数据前转隧道，在从LTE到eHRPD的优化切换过程中，把没有投递给UE的数据报文前转给HSGW。
PGW|从LTE到eHRPD的优化切换过程中，锚定PDN连接，把LTE下建立的PDN连接迁移到eHRPD下。在切换完成后，通知SGW和MME释放PDN连接。
eAN|处理从LTE到eHRPD的预注册信令。处理从LTE到eHRPD的优化切换信令。记录用户选择的MME的IP地址。
HSGW|处理从LTE到eHRPD的预注册信令。处理从LTE到eHRPD的优化切换信令。出S103接口，建立非直接数据前转隧道，在从LTE到eHRPD的优化切换过程中，接收从SGW前转过来的还没有投递给UE的数据报文。
协议栈 :S101接口协议栈 
MME与eAN之间采用S101接口，S101接口的协议栈如[图4]所示。
图4  S101接口协议栈

S101接口采用IP物理连接，S101接口消息承载在UDP协议上。 
本网元实现 :从LTE到eHRPD的优化切换时各网元的交互过程如[图5]所示。
图5  各网元的交互过程

UE在LTE下附着。 
UE通过LTE预注册到eHRPD。 
UE从LTE优化切换到eHRPD。 
业务流程 :概述
从LTE到eHRPD的优化切换包括两个阶段：预注册阶段和优化切换执行阶段。 
优化切换执行根据UE的状态不同，又分为两种方式： 
连接态下从LTE优化切换到eHRPD 
空闲态下从LTE优化切换到eHRPD 
预注册
图6  预注册

UE已经在LTE下附着，获得了IPv4地址或IPv6前缀，处于连接态，和PGW间的数据流经过eNB和SGW。 
由eNB进行触发，UE决定发起到目标eHRPD网络的预注册过程。 
UE通过eNB和MME透传，在eHRPD系统发起HRPD会话建立过程。 
eAN建立到HSGW的A10/A11接口信令关系，消息包含指示，说明是通过S101隧道接入，指示用于HSGW确定不需要PMIP绑定。 
完成对UE的鉴权。 
HSGW和PCRF间进行交互，建立网关控制会话。 
UE和HSGW交互VSNCP消息，建立在LTE下已激活的所有PDN。VSNCP配置请求（VSNCP-Configure-Request）消息设置附着类型（Attach
Type）为切换。UE在消息中包含通过LTE获得的IP地址。当UE完成切换到eHRPD，将完成PDN建立。 
UE和eAN间可能修改eHRPD会话配置，如UE移动到新的eAN。 
由于会话维护，PCRF或者HSGW可以发起PCRF交互。PCRF发起网关控制和QoS规则供应（Gateway Control
and QoS Rules Provision）过程，HSGW发起网关控制和QoS策略规则请求（Gateway Control and
QoS Policy Rules Request）过程。 
连接态下从LTE优化切换到eHRPD
图7  连接态下从LTE优化切换到eHRPD

UE已经在LTE下附着，且处于连接态。 
eNB收到UE的测量报告。 
eNB做出切换决定。 
eNB给UE发送E-UTRA切换准备请求（Handover from E-UTRA preparation request）消息，通知UE切换。 
UE给eNB发送上行切换准备传递（UL handover preparation transfer）消息（HRPD连接请求消息），指示eNB：UE已经响应从E-UTRA切换准备请求（Handover
from E-UTRA preparation request）消息，正在请求接入eHPRD业务信道。 
eNB发送上行S1 CDMA2000隧道（Uplink S1 CDMA2000 Tunneling）消息（HRPD消息，SectorID，CDMA2000切换请求指示）给MME。SectorID静态配置在eNB上。CDMA2000切换请求指示（CDMA2000
HO Required Indication）指示MME切换准备已经启动。 
MME把切换请求消息投递给eAN。 
eAN分配无线资源，并且通过A11信令，让HSGW分配对应的数据转发地址和GRE Key信息。A11请求消息中包含APN,
PGW IP和上行GRE key。A11响应消息包含S101转发的HSGW地址和GRE key信息。对于需要数据转发的每个PDN连接有一个GRE
key。 
eAN给MME 返回切换响应(S101会话ID，HRPD TCA消息，用于数据转发的HSGW地址和GRE key，CDMA2000切换状态)消息。 
子流程如下： 
如果需要创建数据前转隧道，则MME 创建S103接口数据前转隧道，给SGW发送创建前转隧道请求消息。 
SGW给MME返回创建隧道响应消息。 
MME把切换响应消息投递给eNodeB。 
eNB给UE发送从E-UTRA移动性（Mobility from E-UTRA）消息，投递HRPD消息给UE，UE解码HRPD消息为切换命令。eNB开始按每S1-U承载转发收到的下行数据给S-GW，S-GW按每PDN的S103隧道转发数据给HSGW。转发从eNB给UE发送E-UTRA移动性（Mobility
from E-UTRA）消息开始。 
UE重调谐到eHRPD网络并且执行业务信道捕获。 
UE发送HRPD业务信道完成（Traffic Channel Complete，TCC）消息给eAN。 
子流程如下： 
eAN收到TCC消息，触发数据传输路径切换。eAN给 HSGW发送 A11信令请求消息，开始配置用户面连接。 
HSGW给PGW发送代理绑定更新（PBU）消息。 
为了支持会话连续性，PGW基于NAI执行BCE（绑定缓存条目）存在性测试并且分配相同的IPv4家乡地址和/或IPv6家乡前缀给UE。PGW切换数据路径从SGW到HSGW，并给HSGW返回代理绑定确认（PBA）消息。 
HSGW给eAN返回A11信令响应消息。 
对所有使用新的IP-CAN类型建立的激活的IP会话，PGW执行PCEF发起的IP-CAN会话更改（PCEF-Initiated
IP-CAN Session Modification）过程，与PCRF进行交互，获取需要的PCC Rule。 
PGW通知AAA服务器APN/PGW ID，从AAA服务器获取授权信息。 
子流程如下： 
eAN发送通知请求（Notification Request）（切换完成,S101会话ID）消息给MME。 
MME给eAN返回通知响应（Notification Response）消息。如果创建了数据前转隧道，MME起资源保护定时器。 
子流程如下： 
如果没有起资源保护定时器，或资源保护定时器超时了，MME给eNodeB发送UE上下文释放命令消息。 
eNodeB返回UE上下文释放完成消息。 
子流程如下： 
如果资源保护定时器超时了，MME给SGW发送删除非直传前转隧道请求消息； 
SGW返回删除非直传前转隧道响应消息。 
子流程如下： 
如果没有起资源保护定时器，或资源保护定时器超时了，MME给SGW发送删除会话请求消息； 
SGW返回删除会话响应消息。 
PGW释放LTE接入下的资源。 
空闲态下从LTE优化切换到eHRPD
图8  空闲态下从LTE优化切换到eHRPD

UE已经在LTE下附着，且处于空闲态。UE已预注册到eHRPD或者以前在eHRPD附着过，在目标eAN有休眠eHRPD会话。 
UE决定执行小区重选到eAN。小区重选可以在UE一完成eHRPD预注册过程就进行，也可以在LTE下附着的任意时刻进行。 
UE按照3GPP2过程通知eAN执行跨技术间空闲态移动性事件，调谐到eHRPD。 
eAN给HSGW发送A11注册请求（A11-Registration Request）消息。A11-RRQ中包含隧道模式指示器（tunnelled
mode indicator）设为‘0’，指示UE工作在eHRPD无线。 
HSGW从AAA服务器获取所有已激活PDN连接的PGW
ID。 
对每一个PDN连接，HSGW给PGW发送PMIP绑定更新（PMIP Binding Update）消息。 
PGW给SGW返回PMIP绑定确认（PMIP Binding Ack）消息，返回分配给UE的IP地址。此时，PGW中用户面已经通过HSGW切换到eHRPD接入网络。 
对每PDN连接，PGW发送IP-CAN会话更改（IP-CAN Session Modification）消息给PCRF，以获取所有已激活会话的新的QoS策略和计费规则，PCRF返回所有已激活会话的新的QoS策略和计费规则。 
对每PDN连接，PGW通知AAA服务器APN/PGW ID，从AAA服务器获取授权信息。 
HSGW给eAN返回A11注册应答（A11-Registration Reply）消息。 
PGW发起LTE下承载去激活过程。 
系统影响 :本功能对于系统性能的影响取决于从LTE到eHRPD优化切换的发生频率。 
如果开通优化切换业务，需提供优化切换业务发生频率来评估对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "GPRS enhancements for E-UTRAN access "|-
3GPP TS 23.402: " Architecture enhancements for non-3GPPaccesses".|-
3GPPTS23.003: "Numbering, addressing and identification"|-
3GPPTS29.274: "3GPP Evolved Packet System (EPS);Evolved General Packet Radio Service (GPRS) Tunnelling Protocol forControl plane (GTPv2-C); Stage 3"|-
3GPPTS29.276: "3GPP Evolved Packet System (EPS);Optimized handover procedures and protocols between E-UTRAN accessand cdma2000 HRPD Access; Stage 3"|-
3GPPTS36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)"|-
3GPP2 C.S0024-B: "cdma2000 High Rate Packet Data Air InterfaceSpecification".|-
特性能力 :名称|指标
---|---
eAN个数|MME配置eAN ID解析eAN IP地址的记录数，4096。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V5.16.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持优化切换到eHRPD功能”（license ID：），此项目显示为“支持”，表示ZXUN uMAC支持MME支持优化切换到eHRPD功能。
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|√|√|–
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令设置MME Sx信令地址配置SET MME SX GTPC查询MME Sx信令地址配置SHOW MME SX GTPC 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理通过EMS查询用户信息，增加该UE是否存在S101接口及eAN地址的信息。 
性能统计 :测量类型|描述
---|---
S101消息测量|编号为C43210开头的所有计数器
S1AP消息测量|编号为C43200开头的所有计数器
GTPv2消息测量|编号为C43201开头的所有计数器
切换流程测量|编号为C43011开头的所有计数器
切换分网元测量|编号为C46408开头的所有计数器
告警和通知 :该特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :配置3GPP与CDMA2000之间优化切换。 
配置前提 :本功能使用License进行控制，MME需要打开License开关后才能支持优化切换到eHRPD功能 
配置过程 :网管命令终端界面，在配置管理-》业务管理-》优化切换到eHRPD的配置-》优化切换到eHRPD的策略配置下，使用命令SET
OPTMHOPO设置优化切换到eHRPD的策略 
网管命令终端界面，配置管理-》业务管理-》优化切换到eHRPD的配置-》获取eAN地址配置下，使用命令ADD EANIDTOIP配置获取eAN地址 
网管命令终端界面，配置管理-》系统管理-》交换局配置-》VRF配置下，使用命令SET VRFCFG配置S101口的VRF 
网管命令终端界面，配置管理-》系统配置-》交换局配置-》信令面参数配置-》MME Sx信令地址配置下，使用命令SET
MME SX GTPC配置S101接口地址 
以上步骤，没有顺序约束，若已有配置数据的可自行跳过相应步骤 
配置实例 :场景：用户在LTE附着后，从LTE优化切换到eHRPD网络 
UE在区域B（eHRPD和LTE都覆盖），UE优选LTE接入并进行数据业务。由eNB进行触发，UE决定发起到目标eHRPD网络的预注册过程，假设sectorID为01
02 0C 01 06 07 08 04 0C 02 02 02 02 02 02 02 (Hex)，eAN地址为192.20.1.1。 
UE从区域B移动到区域A（只有eHRPD覆盖），发生从LTE到eHRPD的优化切换过程。 
配置脚本 
打开到eHRPD的优化切换开关 
解释说明
设置到eHRPD优化切换开关为支持，其他配置取默认设置
配置脚本
SET OPTMHOPO:IFOPTMHO="YES";
设置基于sectorID获取eAN地址 
解释说明
ZTE eAN做了一个约定，默认MME取SectorID中的第73~80bit（从右往左），作为eAN ID，根据eANID解析eAN IP。根据场景中的sectorID，得到eANID为08
配置脚本
ADD EANIDTOIP:EANORCELLID=8,EANIP="192.20.1.1";
设置S101口的VRF 
解释说明
假设S101口的VRF已规划，通过此步骤配置，如果没有规划，可跳过此步
配置脚本
SET VRFCFG:S101VRF=51;
配置S101接口地址 
解释说明
从不支持本功能的版本升级到支持本功能的版本，默认从MME GTPC地址配置中复制数据到S101地址配置中，如果地址符合网络规划，可以跳过此步；如果需要修改，可通过此步修改
配置脚本
SET MME SX GTPC:S101IPADDR="192.20.2.2",S101IPV6ADDR="2FFF:0000:0000:0000:0001:0000:0001:0001";
调整特性 :无 
测试用例 :测试项目|MME支持CL优化切换功能
测试目的|验证UE从LTE能够优化切换到eHRPD网络
预置条件|License已开启，7.1场景中相关配置已配置完成
测试过程|用户附着在LTE 用户发起到eHRPD网络预注册用户移动到纯eHRPD网络，触发CL优化切换
通过准则|用户成功预注册到eHRPD网络，获取eAN地址，创建S101隧道用户从LTE成功切换到eHRPD网络，MME释放该用户EPC承载
测试结果|–
常见问题处理 :无 
## ZUF-78-14-003 3GPP与WLAN之间切换 
概述 :用户从LTE网络切换到WLAN网络。 
收益 :在有WIFI的地方用户可以切换到WIFI，在没有WIFI的地方切换到LTE，降低用户资费的同时，保证用户业务连续性，VOIP的语音连续，提升用户体验。 
描述 :对于支持WIFI和E-UTRAN的双模终端，可为其提供WIFI和E-UTRAN间的切换，以保证用户业务连续性。 
支持单连接模式的切换和多连接模式的切换。 
# 缩略语 
# 缩略语 
## eHRPD 
evolved High Rate Packet Data演进的高速分组数据
## eNB 
Evolved Node B演进型基站
PDN :Packet Data Network分组数据网
# ZUF-78-15 增强功能 
概述 :功能描述 :因组网、用户业务或运营商本地控制的需要，MME对用户除了提供基本的接入管理、安全管理、移动性管理、会话管理，还提供了一些可选的增强功能。 
功能特性简介 :核心网为满足用户的要求，提供了有效的解决方案。详细的解决方案特性如下。 
方案特性|实现简述|特导链接
---|---|---
MOCN|MOCN是指无线接入网络共享而核心网元不共享的一种网络共享方式。MOCN使得多个运营商共同出资建设共享的无线接入网络，分担网络建设成本，降低网络建设风险，提高建网速度。MME网元的MOCN功能包括在附着、TAU、局内S1切换以及局间切换业务流程中传递选择的PLMN标识和支持切换限制列表。|ZUF-78-15-002 MOCN
HeNB接入|HeNB是一种小型、低功率蜂窝基站，主要用于家庭及办公室等室内场所作为蜂窝网在室内覆盖的补充，为用户提供话音及数据服务。通过对HeNB接入的支持，为运营商提供了一种成本较低但能有效改善室内信号覆盖质量的方式，可以明显提高用户的宽带，提高用户数据和语音服务质量。一个家庭基站并不是为所有用户提供服务，而是只能为特定用户服务。因此提出了闭合用户群CSG的概念。CSG指的是允许接入一个或多个特定小区的一组签约用户。MME对用户CSG信息进行校验控制接入和移动管理。具体描述参见3GPP 23.401协议的“4.3.13 Closed Subscriber Group functions”章节。|ZUF-78-15-003 HeNB接入
Relay|Relay即中继技术，在下行方向，基站（DeNB）发给UE的信号不直接发给UE，而是先发给一个中继站，再由中继转发给UE；在上行方向，UE的上行信号也不直接发给基站（DeNB），而是先发给一个中继站，再由中继站转发给基站。通过中继技术可以扩大网络覆盖和提升系统容量。MME对ReLay节点进行识别、授权和为其建立管理通道。Relay功能的具体说明参见3GPP 23.401协议的“4.3.20 Relaying function”章节。|ZUF-78-15-004 Relay
LIPA|LIPA是用户的业务流数据直接从家庭基站进行接入，不经过运营商的核心网络。这部分业务直接从HeNB就分流出去，减轻了核心网络的负荷，同时降低了核心网络的传输成本。 为实现LIPA功能，MME支持识别、授权、建立和维护LIPA PDN连接。LIPA功能的具体说明参见3GPP 23.401协议的“4.3.16 Local IP Access (LIPA) function”章节。|ZUF-78-15-005 LIPA
eMBMS|eMBMS是一种利用LTE网络向多方用户同时广播的高效方式。这一新兴的LTE广播技术将大幅降低热门多媒体内容的发布成本。多媒体内容既可以选择流媒体播放，也可以在非高峰时段传送并存储至移动设备，以便事后随时访问。通过引入eMBMS，运营商可以更好地利用现有频谱并释放网络容量；运营商可以在向大量移动设备和机顶盒提供直播电视、视频点播、播客甚至软件升级服务时，实现效率最大化。eMBMS功能的具体说明参见3GPP 22.246协议和23.246协议。|ZUF-78-15-006 eMBMS
分权分域|分权分域分为分权和分域两部分功能。分域指用户能管理和操作的资源范围。运营商一般都是按设备节点或地域范围来划分用户的管理范围。分权指对用户的操作权限进行授权，控制用户只能执行哪些命令或操作集。限定用户只对一定区域的某些内容执行允许的操作，以保证网管系统的操作安全。分权是在分域条件下的权限控制行为，按设备节点或区域设置用户帐号。用户账号一般属于一个区域。该用户授予的操作权限只在所属区域有效，不能管理其他区域。根据运营商的组织体系和管理需要，某些特殊用户也可以设置为管理所有或多个区域。大本地网组网时，一个MME管辖多地市，为了各地市网络管理独立，MME支持根据TA进行分域，系统管理员对每个域分配不同的操作员以及相应的权限。每个操作员只能操作和查看本域的数据。|ZUF-78-15-007 分权分域
信令风暴抑制|信令风暴抑制是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。MME信令风暴抑制是用户级的且针对三种终端信令，包括附着请求信令、业务请求信令和PDN连接请求信令。当用户单位时间内的信令数超过门限值，用户将被加入信令黑名单，MME对其信令请求进行抑制。|ZUF-78-15-008 信令风暴抑制
PDN类型IPV6和双栈|MME支持UE地址为IPV4、IPv6和IPV4V6双栈。MME根据UE请求的PDN类型和签约的PDN类型进行协商。具体参见3GPP 23.401协议的“5.3.1 IP address allocation”章节。|ZUF-78-15-009 PDN类型IPV6和双栈
原因值可配置|用户终端向MME发送附着或跟踪区更新请求或者业务请求。MME拒绝用户接入，并根据运营商策略配置不同的EMM原因值。|ZUF-78-15-010 原因值可配置
MPS|MPS是一种端到端的多媒体优先级业务。MPS能够允许授权的“业务用户”在网络发生拥塞、会话建立受阻时，获取优先于其他用户的无线信道接入权利，能够优先发起、修改、保持、释放会话以及投递媒体报文。MPS被应用于PS域以及IMS域的语音、视频和数据承载业务，包括特殊Access Class的USIM、HSS签约、EPS承载优先业务、IMS优先业务、CSFB优先业务、空口优先级接入等。具体参见3GPP 23.401协议“4.3.18 Multimedia Priority Service”章节。|ZUF-78-15-011 MPS
无线资源管理|无线资源管理指基于特定用户上下文信息进行分配和维护无线通道。支持在HSS中为用户签约特定的RFSP索引。支持基于IMSI号段和语音参数在MME本地配置RFSP索引。如果本地配置的RFSP索引和签约的RFSP索引同时存在，MME可控制选用其中之一。MME将RFSP索引传递给eNodeB，eNodeB映射为对应的无线通道分配和管理策略。无线资源管理功能参见3GPP TS 23.401协议的“4.3.6 Radio Resource Management functions”章节。|ZUF-78-15-012 无线资源管理
载波聚合|CA是LTE-Advanced系统最为重要的关键技术之一，其通过将多个连续或非连续LTE载波聚合在一起，同时进行数据传输。从二载波聚合到三载波聚合，以及未来更多的载波聚合，可成倍提升网络传输速率。为了实现多载波聚合，需要对UE能力进行扩充，UE需要支持多频道。MME支持扩充后的UE能力的保存和传递，支持UE无线能力参数的最大长度为8188字节。|ZUF-78-15-013 载波聚合
双连接|双连接是指用户终端可以同时连接宏基站和微基站，其中只有宏基站用于实现控制平面的功能。数据业务可以选择由宏基站（又称为MeNB）或微基站（又称为SeNB）进行传输，也可以选择二者同时传输。双连接的优点及应用场景：增加热点区域容量。大型场所包括大规模的剧院、影城、展览馆、体育场、机场等设施。其场地开阔、容纳人数众多，通讯的特点为密度高、话务量大，仅依靠覆盖室外的宏基站难以解决。盲点覆盖。在宏站覆盖不到的地方，放置微基站来解决。降低成本。在人口非密集区，或者话务量很低的区域，放置微基站以节省降低成本。具体参见3GPP TS 23.401协议的“4.3.2a Support for Dual Connectivity”和“5.4.7 E-UTRAN initiated E-RAB modification procedure”章节。|ZUF-78-15-014 双连接
CS/PS协作|在共享网络的架构下，用户在CS域和PS域来回切换时，CS/PS协作保障用户始终在同一个PLMN下接入网络，解决用户跨PLMN计费和管理的问题，保证用户在CS域和PS域被同一运营商服务。|ZUF-78-15-015 CS/PS协作
3GPP和WLAN间基于无线辅助互操作|无线辅助参数包括E-UTRAN信令长度和质量门限、WLAN通道利用门限、WLAN回传数据率门限、WLAN标识列表和卸载优先指示OPI。UE使用这些无线辅助参数执行接入网选择和WLAN与3GPP之间的话务控制决策。MME在PDN连接中，提供是否可以负荷卸载到WLAN的信息给UE。该信息通过PDN连接的NAS信令给UE。|ZUF-78-15-016 3GPP和WLAN间基于无线辅助互操作
## ZUF-78-15-002 MOCN 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :网络共享是3GPP R6引入的概念，是指不同运营商进行共享核心网或共享无线网络，主要是多个运营商共同出资建设共享的网络，这是为分担网络建设成本、降低风险而采取的一种建网模式。 
MOCN，是指无线接入网络共享，核心网元不共享的一种网络共享方式，无线接入网络指eNodeB，即多个运营商共同出资建设共享的无线接入网络，分担网络建设成本，降低网络建设风险，提高建网速度。
图1  MOCN网络共享模式

MME网元MOCN功能包括在附着、TAU、局内S1切换以及局间切换业务流程中传递选择的PLMN标识和支持切换限制列表。
背景知识 :协议上对网络共享给出了两种网络架构，一种是MOCN：仅无线接入部分共享，核心网元不共享；另外一种是GWCN：除了共享的无线网络，核心网也在运营商间共享，组网方式如下图所示。
图2  GWCN网络共享模式

经常与网络共享一起被提到的术语还有MVNO，主要是指没有无线频谱资源，但有经营权，可以通过租用方式向终端用户提供移动通信服务，能够发行自己的SIM卡的机构或组织，采用了核心网共享技术，其实，这也属于网络共享。 
应用场景 :应用场景如下图所示： 
图3  LTE无线接入网络共享

应用场景说明
运营商A和运营商B共享LTE无线接入，运营商A拥有自己的核心网A和运营商B拥有自己的核心网B。 
UE接入过程
EPC网络中的终端都是支持网络共享的，即都是S-UE。因此本文提到的UE即S-UE。 
图4  UE接入过程

eNodeB通过系统信息（“System Information”）广播向UE发布某跟踪区中可用的网络信息（PLMN-id
List），eNodeB广播Cell ID、TAC、PLMN列表信息（如果eNodeB支持多PLMN，则PLMN列表信息包含eNodeB支持的所有PLMN）。  
UE获取eNodeB广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。UE根据“PLMN选择/重选”功能，选择一个PLMN（即Selected
PLMN）；UE根据“小区选择/重选”选择Selected PLMN下的一个小区，根据Selected PLMN+TAC得到TAI，从这个小区接入eNodeB。 
eNodeB根据UE选择的PLMN直接定位所服务的运营商，从而将该消息路由到相应的CN节点（如核心网A）。 
核心网A确定UE被允许接入网络，返回消息中携带切换限制列表。  
eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
客户收益 :受益方|受益描述
---|---
运营商|MME支持MOCN功能，可以为运营商提供更加灵活的网络建设方式，包括和其运营商分担网络建设成本，降低网络建设风险，提高建网速度等。
移动用户|对终端用户不可见。


实现原理 :



涉及的网元 :网元名称|网元作用
---|---
UE|具体负责携带Selected PLMN Identity。
eNodeB|通过系统信息广播向UE发布某跟踪区中可用的网络信息，根据用户选择的PLMN路由到正确的MME，根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。
MME|负责在附着、TAU、局内S1切换以及局间切换业务流程中传递选择的PLMN标识和支持切换限制列表。


本网元实现 :图5  本网元实现




MOCN功能各网元交互过程： 


(1) eNodeB通过系统信息（“System Information”）广播向UE发布某跟踪区中可用的网络信息（PLMN-id
List），eNodeB广播Cell ID、TAC、PLMN列表信息（如果eNodeB支持多PLMN，则PLMN列表信息包含eNodeB支持的所有PLMN）。对于同一个跟踪区中的所有小区，可用的网络信息是相同的。 


(1) UE获取eNodeB广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。UE根据“PLMN选择/重选”功能，选择一个PLMN（即Selected
PLMN）。UE根据“小区选择/重选”选择Selected PLMN下的一个小区，根据Selected PLMN+TAC得到TAI，从这个小区接入eNodeB。 
注：EPC网络相对于GPRS网络来说，不存在NS-UE（Pre-R6 UE）即不支持共享网络的终端，EPC全网都是S-UE支持共享网络的终端。 


eNodeB根据UE选择的PLMN直接定位所服务的运营商，从而将该消息路由到相应的CN节点MME A。 
另外： 

 
eNodeB根据UE接入的小区消息，可以确定TAC和Cell ID信息。 

 
eNodeB根据Selected PLMN+TAC得到TAI。 

 
eNodeB根据eNodeB的Global eNB ID+UE接入的Cell ID，生成ECGI。 

 
根据36.413协议： 

 
ECGI中的PLMN是Global eNB ID中的PLMN，而Global eNB ID中只能有一个PLMN，且是eNodeB支持的多PLMN中的一个，因此ECGI中的PLMN为eNodeB支持的多个PLMN中的一个固定PLMN。 

 
根据36.413协议，TAI中的PLMN是Selected PLMN，不同的UE有不同的Selected PLMN。 

 
因此ECGI中的PLMN和TAI中的PLMN可能是不一致的。 


在附着、路由更新等过程，eNodeB会携带ECGI和TAI给MME A，ECGI和TAI中的PLMN可能是不一致的。在切换过程中，Target
ID中包含Global eNB ID和TAI，Global eNB ID和TAI中的PLMN可能是不一致的。PLMN不一致的情况，
MME都可以处理。MME负责在附着、TAU、局内S1切换以及局间切换业务流程中传递选择的PLMN标识和支持切换限制列表。 
eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
切换限制列表说明：
切换限制列表主要包括Serving PLMN、EPLMN、禁止的TA列表、禁止的LA列表和Forbidden inter RATs。 

 
Serving PLMN源eNodeB发起切换请求时，请求消息的参数TAI/RAI中携带Selected
PLMN即Serving PLMN。如果目标小区支持该PLMN，则切换继续执行至完成。如果目标小区不支持该PLMN，则源eNodeB选择eNodeB预配置的或EPLMN作为Serving
PLMN。 

 
EPLMNEPLMN即对等PLMN，运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，之间可以实现通信网络资源共享。这样，在其归属的签约移动用户就可以自己选择在运营商为提供的不同EPLMN之间的驻留问题，也就是说允许用户可以自己选择利用其通信网络的资源来为提供服务。但是用户的归属PLMN
只有一个（UE从IMSI号码中提取），在多个网络同时为一个用户服务时，网络侧就可以通过对等PLMN列表告诉eNodeB和UE：当前网络与归属PLMN
是等同的。当MME给手机下发附着接受消息或跟踪区更新接受消息时，MME将相关的EPLMN列表下发给UE，UE将网络侧下发的EPLMN列表加上当前网络的网络号保存在SIM卡中，直到下次附着或跟踪区更新接受后被刷新。这样移动用户就可以有更多的选择。 

 
禁止的TA列表禁止的TA列表用于LTE内的漫游限制。 

 
禁止的LA列表禁止的LA列表用于3GPP无线接入网间的漫游限制。 

 
Forbidden inter RATs Forbidden inter RATs用于3GPP和3GPP2无线接入网间的接入限制。 EPC网络的切换限制列表相对于GPRS网络的SNA（Shared Network Area：共享网络区）来说，内容丰富了很多，切换限制列表用于无线接入网络共享的MOCN，但不仅仅用于MOCN功能，非MOCN的普通切换也使用切换限制列表，控制UE后续移动时的漫游限制、区域限制和接入限制。因此，MME支持切换限制列表，不受系统开关“MME支持MOCN功能”的控制。 

 




业务流程 :MOCN功能实现在如下业务流程中传递选择的PLMN标识和支持切换限制列表： 


附着。 


空闲态TAU。 


切换后的TAU。 


连接态非切换后的TAU。 


局内S1切换。 


Intra LTE局间切换。 


注：切换过程中支持MOCN功能，这里只描述了局内S1切换流程和Intra LTE局间切换，其跨RAT局间切换从MOCN功能实现来看是一样的，不再详述。 
下面各节流程中描述的MME下发的切换限制列表的内容填写规则为： 
参数|填写规则
---|---
Serving PLMN|eNodeB携带的Selected PLMN ID
EPLMN|MME对用户和该用户当前的TAI可配置对等PLMN，也可全局配置对等PLMN，MME先根据用户的IMSI和当前TAI获取配置的EPLMN，如果没有获得则获取全局配置的默认EPLMN。
Forbidden TAs|MME对用户和用户的签约Zone Code可配置允许的TA列表。如果签约的Zone Code个数为0，则禁止的TA列表为空。如果签约的Zone Code个数不为0，则MME根据用户的IMSI和签约Zone Code，获取用户允许接入的TAs，允许接入的TAs不要有重复的TA。MME根据本局管理的所有TA，剔除掉用户允许接入的TAs，得到用户ForbiddenTAs。
Forbidden LAs|如果“切换限制列表是否携带禁止的位置区”开关配置为不携带，则禁止的LA列表为空。如果“切换限制列表是否携带禁止的位置区”开关配置为携带，但签约的Zone Code个数为0，则禁止的LA列表为空。如果“切换限制列表是否携带禁止的位置区”开关配置为携带，但签约的Zone Code个数不为0，则根据每一个签约的ZoneCode，查询区域编码对应的禁止的LA配置，剔除掉重复的禁止的LAs，得到用户的Forbidden Las。
Forbidden inter RATs|MME根据软件参数“切换限制列表中禁止的接入方式策略”的取值填写Access-Restriction-Data：（使用本地策略--禁止所有接入）：则Forbidden inter RATs取值为0（ALL）（使用本地策略--禁止GERAN接入）：则Forbidden inter RATs取值为1（GERAN）（使用本地策略--禁止UTRAN接入）：则Forbidden inter RATs取值为2（UTRAN）（使用本地策略--禁止CDMA2000接入）：则Forbidden inter RATs取值为3（CDMA2000）（使用本地策略--禁止GERAN和UTRAN接入）：则Forbidden inter RATs取值为4（GERANAND UTRAN）（使用本地策略--禁止CDMA2000和UTRAN接入）：则Forbidden inter RATs取值为5（CDMA2000and UTRAN）（使用本地策略—不禁止任何接入）：则Forbidden inter RATs为空（使用签约的接入限制数据）：根据签约的ARD（Using subscribed access restrictiondata）的值填充Forbidden inter RATs
附着流程
附着流程如[图6]所示。
图6  附着流程




流程描述： 


UE获取eNodeB广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。选择到可以接入的PLMN后，发送附着请求消息给网络，并将Selected
PLMN ID信息携带给eNodeB。  


eNodeB根据UE指示的Selected PLMN ID选择MME，发送附着请求消息给选择的MME。 


MME在下发Attach Accept消息之前的处理保持不变。 


MME发送初始上下文建立请求消息给eNodeB，其中封装了Attach Accept消息。如果“是否携带切换限制列表”开关打开即携带，则初始上下文建立请求消息中携带切换限制列表。在携带切换限制列表时，如果“切换限制列表是否携带禁止的位置区”开关状态为“携带”，则切换限制列表中携带“禁止的位置区”。Selected
PLMN ID被包含在Handover Restriction List中的Serving PLMN。  


eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 


继续附着其处理过程。 


空闲态TAU流程
空闲态TAU流程如[图7]所示。
图7  空闲态TAU，携带激活标记




流程描述： 


UE获取eNodeB广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。UE判断需要发起TAU流程，比如UE进入新的TA且该TA不属于当前用户的TA
List中，选择到可以接入的PLMN后，发送Tracking Area Update请求消息给网络，并将Selected PLMN
ID信息携带给eNodeB。 2. 


eNodeB根据UE指示的Selected PLMN ID选择MME，发送Tracking Area Update请求消息给选择的MME。 


在下发TAU Accept之前的处理，MME保持不变。  


如果TAU请求消息中携带了激活标记，则下发初始上下文建立请求消息给eNodeB，消息中封装了TAU Accept消息，若“是否携带切换限制列表”开关打开即携带，则初始上下文建立请求消息中携带切换限制列表。携带切换限制列表时，若“切换限制列表是否携带禁止的位置区”开关状态为“携带”，则切换限制列表中携带“禁止的位置区”。Selected
PLMN ID被包含在Handover Restriction List中的Serving PLMN。 


eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 


TAU后续处理保持不变。 


切换后的TAU流程
切换后的TAU流程如[图8]所示。
图8  切换后的TAU




流程描述 


局间或局内切换后UE发起TAU流程，UE从PLMN ID候选列表执行网络选择，选择到可以接入的PLMN后，发送Tracking
Area Update请求消息给网络，并将Selected PLMN ID信息携带给eNodeB。 


eNodeB根据UE指示的Selected PLMN ID选择MME，发送Uplink NAS Transport消息给选择的MME，消息中封装了Tracking
Area Update请求消息。 


在下发TAU Accept之前的处理，MME保持不变。  


MME下发Downlink NAS Transport消息给eNodeB，消息中封装了TAU Accept消息。如果为局间切换后的TAU，或着局内切换后的TAU且签约的Zone
Code或Access-Restriction-Data发生改变，若“是否携带切换限制列表”开关打开，则Downlink NAS Tranport消息中携带切换限制列表。在携带切换限制列表时，若“切换限制列表是否携带禁止的位置区”开关状态为“携带”，则切换限制列表中携带“禁止的位置区”。Selected
PLMN ID被包含在Handover Restriction List中的Serving PLMN。 


eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。  


TAU后续处理保持不变。 


连接态非切换后的TAU流程
连接态非切换后的TAU流程如[图9]所示。
图9  连接态非切换后的TAU




流程描述： 


UE获取eNodeB广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。连接态UE判断需要发起TAU流程，比如UE进入新的TA且该TA不属于当前用户的TA
List中，选择到可以接入的PLMN后，发送Tracking Area Update请求消息给网络，并将Selected PLMN
ID信息携带给eNodeB。 


eNodeB根据UE指示的Selected PLMN ID选择MME，发送Uplink NAS Transport消息给选择的MME，消息中封装了Tracking
Area Update请求消息。 


在下发TAU Accept之前的处理，MME保持不变。 


MME下发Downlink NAS Transport消息给eNodeB，消息中封装了TAU Accept消息。如果签约的Zone
Code或Access-Restriction-Data发生改变，若“是否携带切换限制列表”开关打开，则Downlink NAS Tranport消息中携带切换限制列表。在携带切换限制列表时，若“切换限制列表是否携带禁止的位置区”开关状态为“携带”，则切换限制列表中携带“禁止的位置区”
。Selected PLMN ID被包含在Handover Restriction List中的Serving PLMN。 


eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 


TAU后续处理保持不变。 


局内S1切换
局内S1切换流程如[图10]所示。
图10  局内S1切换




流程描述： 


UE已经附着并且处于连接态。  


源eNodeB根据UE的测量报告，判断需要发起切换流程，发送Handover Required消息给MME，请求消息中携带的参数TAI/RAI中携带Selected
PLMN即Serving PLMN，同时携带了目标eNodeB的ID。如果目标小区支持该PLMN，则切换继续执行至完成。如果目标小区不支持该PLMN，则源eNodeB选择eNodeB预配置的或EPLMN作为Serving
PLMN。 


MME发送Handover Request消息给目标eNodeB，若“是否携带切换限制列表”的开关打开即携带，则在Handover
Request消息中携带切换限制列表。在携带切换限制列表时，若“切换限制列表是否携带禁止的位置区”开关状态为“携带”，则切换限制列表中携带“禁止的位置区”。Selected
PLMN ID被包含在Handover Restriction List中的Serving PLMN。 


目标eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。  


后续处理保持不变。 


Intra LTE局间切换
Intra LTE局间切换流程如[图11]所示。
图11   Intra LTE局间切换




流程描述： 


UE已经附着并且处于连接态。 


源eNodeB根据UE的测量报告，判断需要发起切换流程，发送Handover Required消息给MME，请求消息中携带的参数TAI/RAI中携带Selected
PLMN即Serving PLMN，同时携带了目标eNodeB的ID。如果目标小区支持该PLMN，则切换继续执行至完成。如果目标小区不支持该PLMN，则源eNodeB选择eNodeB预配置的或EPLMN作为Serving
PLMN。 


MME判断目标eNodeB不是本局MME管理的，则根据TA查找目标MME，发送Forward Relocation Request消息给目标MME。若“MME支持MOCN功能”开关打开，则Forward
Relocation Request消息中携带源eNodeB带上来的Selected PLMN ID带给Target MME。开关关闭，则不携带Selected
PLMN ID。 


目标MME收到Forward Relocation Request消息，保存消息中携带的Selected PLMN ID，若开关“局间切换时在切换请求消息中是否携带切换限制列表”打开即携带，则在Handover
Request消息中携带切换限制列表。在携带切换限制列表时，若“切换限制列表是否携带禁止的位置区”开关状态为“携带”，则切换限制列表中携带“禁止的位置区”。Selected
PLMN ID被包含在Handover Restriction List中的Serving PLMN。 


目标eNodeB根据切换限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 


后续处理保持不变。 






系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 23.251: "Network Sharing; Architecture and functionaldescription".|-
3GPPTS24.301: "Non-Access-Stratum (NAS) protocolfor Evolved Packet System (EPS); Stage3".|-
3GPPTS36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)".|-
3GPPTS29.274: "General Packet Radio Service(GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS".|-
3GPP TS 29.272: "Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".|-
3GPPTS23.003: "Numbering, addressing and identification".|-
3GPPTS24.007: "Mobile radio interface signallinglayer 3; General aspects".|-
特性能力 :名称|指标
---|---
多PLMN配置|最多支持16个PLMN。
对等PLMN配置|最多支持15个对等PLMN	。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
###### 对其网元的要求 
UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|–|–|–
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
###### 组网规划要求 
MOCN组网要求支持网络共享的eNodeB与各MME互通。 
MME与不同PLMN的eNodeB互通并支持多PLMN。 
MME上配置切换限制列表数据。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令软件参数配置SET SOFTWARE PARAMETERSHOW SOFTWARE PARAMETER移动管理参数配置SET MOBILE MANAGEMENTSHOW MOBILE MANAGEMENT跟踪区区域编码配置ADD TAIZCSET TAIZCDEL TAIZCSHOW TAIZCMME IMSI号段区域编码配置ADD MME IMSI TAIZCSET MME IMSI TAIZCDEL MME IMSI TAIZCSHOW MME IMSI TAIZC区域编码与禁止位置区映射配置ADD ZC BARRED LASET ZC BARRED LADEL ZC BARRED LASHOW ZC BARRED LA位置区配置ADD LAISET LAIDEL LAISHOW LAI默认对等PLMN配置SET MME PLMN DEFAULTDEL MME PLMN DEFAULTSHOW MME PLMN DEFAULT对等PLMN Profile配置ADD MME PLMNDEL MME PLMNADD MME PLMN PROFILESET MME PLMN PROFILEDEL MME PLMN PROFILESHOW MME PLMN PROFILEIMSI号段对等PLMN配置ADD MME IMSI TAI PLMNSET MME IMSI TAI PLMNDEL MME IMSI TAI PLMNSHOW MME IMSI TAI PLMNCombo本局移动数据配置SET COMBOCFGSHOW COMBOCFG跟踪区配置ADD TASET TADEL TASHOW TASGSN其HPLMNADD HPLMNCFGSET HPLMNCFGDEL HPLMNCFGSHOW HPLMNCFG本局支持的其GUMMEI配置ADD GUMMEISET GUMMEIDEL GUMMEISHOW GUMMEI设置MME切换限制列表策略SET MME HRLPLY 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MOCN相关配置主要如下： 
设置MME支持MOCN功能开关；  
设置MME支持切换限制列表功能开关；  
切换限制列表信息配置； 
MME与eNodeB对接配置； 
MME支持多PLMN配置； 
MME支持多GUMMEI配置 
配置前提 :MOCN组网要求支持网络共享的eNodeB与各MME互通。 
MME与不同PLMN的eNodeB互通并支持多PLMN。 
UE在HSS中签约了ZoneCode。 
配置过程 :在MME本局移动数据配置中将MOCN功能开关打开。 
将切换限制列表功能打开。 
配置切换限制列表。 
在实际配置MOCN功能时，经常会碰到把支持MOCN功能的eNodeB接入到已有的MME上，支持MOCN功能的eNodeB和MME下已连接的eNodeB可能属于不同的PLMN，因此补充下面两部分的内容： 
MME与eNodeB对接； 
MME支持多PLMN和GUMMEI配置； 
配置实例 :实例场景-MOCN组网下的UE接入 
支持MOCN功能的eNodeB与MME对接，MME支持的PLMN为46001，eNodeB的 PLMN为46011，支持的TA为460010001，IMSI号段为46001的UE从支持MOCN的eNodeB接入到MME，MME在附着过程中携带切换限制列表给eNodeB。 
调整特性 :测试用例 :测试项目|移动用户从支持MOCN的eNodeB发起附着接入到MME
测试目的|验证MME能正常处理UE的附着流程，并在附着过程中携带切换限制列表给eNodeB。
预置条件|EPS网络中各网元系统及操作维护台运行正常。用户在HSS中已签约EPS业务和ZC区域编码。MME根据配置过程完成相关配置在MME上建立用户跟踪。
测试过程|UE开机发起附着。在网络侧查询用户的信息。
通过准则|UE是否附着成功。MME在Initial Context Setup Request消息中是否携带了“Handover RestrictionList”，携带的相关内容是否正确；消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
常见问题处理 :问题描述|解决方法
局间S1切换，MME发送HORequest消息中没有携带切换限制列表|局间切换请求消息中是否携带切换限制列表是由软参“262259 局间切换时在切换请求消息中是否携带切换限制列表”单独控制，检查软参是否开启。
## ZUF-78-15-003 HeNB接入 
特性描述 :特性描述 :描述 :定义 :Femto小区接入，也称为家庭基站接入是毫微微小区，在3GPP组织中称为HNB/HeNB，而在3GPP2等其他标准组织中称为Femto，本质上是相同的。
一个家庭基站并不是为所有用户提供服务，而是只能为特定用户服务。因此提出了CSG的概念，表示允许接入一个或多个特定小区的一组签约用户，特定小区指的是Home
（e）NodeB所支持的小区。
功能范围：
只支持LTE制式的HeNB接入，如图1所示。 
所有网元所有接口协议对齐3GPP R9 2011.09。 
图1  接入示意图

MME支持CSG功能接口参见下表。 
接口|是否需要支持|备注
---|---|---
S1|支持|基本CSG接入控制。
S11|支持|SGW/PGW相关CSG信息通知功能。
S10|支持|局间CSG信息传递。
Gn|支持|局间CSG信息传递。
S6a|支持|获取CSG签约信息。
涉及MME功能参见下表。 
功能分类|功能详细分类|具体功能|概述
---|---|---|---
CSG基本功能|接入控制/移动管理|基本接入控制|按照3GPP协议支持CSG接入控制。ENodeB携带CSG信息给MME，MME在获取签约信息后，对CSG信息进行签约校验。
S1口切换（宏或HENB）|CSG基本功能|接入控制/移动管理|基本协议功能，ENodeB发出HANDOVER REQUIRED携带目的CSG信息，MME需要根据用户信息进行检查，有相应签约才能允许切换。
X2口切换|CSG基本功能|接入控制/移动管理|R10以后版本功能，为适应BT测试加入该功能。
MME支持HeNB-GW的HeNB S1口切换|CSG基本功能|接入控制/移动管理|在根据HeNB ID无法查找到对应的HeNB时，需要根据TAI再查找一次。
Paging优化|CSG基本功能|接入控制/移动管理|根据TAList查询出eNobeB，过滤出用户未签约CSG关联的eNobeB，对剩下的进行寻呼。寻呼不到再去掉Paging优化进行寻呼。
CSG信息更改|CSG基本功能|临时用户|基本协议功能，MME需对临时用户开启定时器，判定用户是否有时间权限，超过时限则进行成员身份改变流程。
UE 成员身份改变|CSG信息更改|CSG基本功能|基本协议功能，签约数据或临时用户导致CSG数据改变，通知eNodeB对用户切换或释放。
CSG更改上报|CSG信息更改|CSG基本功能|和位置改变类似，如果PGW要求CSG更改后上报，那么在改变后需要通知PGW。涉及切换，TAU等多个流程。
扩展功能|兼容性考虑|接口参数控制功能|可以控制接口上是否携带CSG相关IE。
CSG NAS失败原因修改|扩展功能|兼容性考虑|考虑某些终端不支持CSG信息，也可能不支持相应CSG失败原因，需要进行调整。
漫游用户CSG限制|扩展功能|漫游用户CSG限制|根据IMSI开关限制用户是否能使用CSG签约信息。
背景知识 :基本概念
家庭基站Home （e）NodeB是一种小型、低功率蜂窝基站，主要用于家庭及办公室等室内场所作为蜂窝网在室内覆盖的补充，为用户提供话音及数据服务。外形通常和Wi-Fi
AP类似，既可以单独使用，也可以集成在家庭网关中作为家庭网络的一部分。 
Home （e）NodeB通过用户的宽带连接接入核心网。为了保证安全性，需要建立IPSEC通道来保证通信安全性。同时核心网也需要支持设备认证，保证Home
（e）NodeB的合法性。 
Home （e）NodeB的功能受运营商控制。无线传输只能在通过运营商配置和授权后才能开启。 
CSG-ID 用于识别一组CSG用户，固定为27BIT。在同一PLMN内最少支持1.25亿个。 
HNB Name 是被HeNB广播的明文字符串，最多48个BYTE，便于人工识别出不同的CSG。 
CSG Type 是运营商设置在UE中的字段，通常用于提示用户计费信息。当CSG在UE中没有CSG TYPE时，UE会显示HNB
Name来代替。Allowed CSG List和Operator CSG list，这两个UE中的CSG列表独立维护，两个列表中CSG
，UE均可以接入，也叫做CSG白名单。其中Operator CSG list具有高优先级 。 
Home eNodeB的接入控制方式
HeNB支持3种接入方式：闭合、开放和混合方式。依靠CSGID和接入模式来判断。在S1消息中只有CSG
ID，就是闭合模式；带有CSG ID和接入模式字段，则是混合模式；而开放模式则没有相关的IE。 
闭合方式用于普通家庭主要给家庭成员使用。仅是HeNB关联的CSG的成员才能接入。对非CSG成员的用户，不允许接入。 
开放模式用于火车站、飞机场、运动场，同普通的宏基站一样允许所有用户接入，主要用于增强运营商公共网络的覆盖和容量。 
混合模式用于商场，企业等，除了允许HeNB关联的CSG的成员接入，其它用户也允许接入。不过HeNB可以对成员提供优先服务。这个场景可能在商场等环境使用，可以对内部员工提供优惠费率以及优先接入权；同时，也允许普通用户使用HeNB来接入，提高室内的无线覆盖范围。 
动态偶联的配置变化
HeNB业务量远远小于正常的eNB，但是网元数量却远远多于正常的eNB。为了在有限的内存资源中支持更多的HeNB数量，则需要对HeNB的偶联的配置更小的缓存（发送缓存6KByte，接收缓冲6Kbyte；普通eNB的发送缓存为256
Kbyte，接收缓存为128 Kbyte）。
如果HeNB都作为正常的eNB来配置，为了支持2.5万个eNB，每个模块支持256条动态偶联，那么需要配置98个模块即13对SMP单板。 
如果HeNB按缩小的偶联缓存配置（毕竟业务负荷轻），每模块最多可以支持2048条动态偶联，只需要配置13个模块即2对SMP单板就可以支持2.5万个HeNB。 
为了配置更多的HeNB偶联时，如果每模块支持的偶联数需要超过256条情况下，必须要打开独立缓存开关，并修改每模块支持的最大动态偶联数（最多2048）。  
开启独立缓存开关后，需要区分HeNB和普通的eNB，在动态偶联建立时可以使用不同的缓存大小。MME会对外暴露两个不同的动态偶联服务端地址，分别用于HeNB和普通的eNB的偶联接入。接入HeNB的服务端，将配置更小的收发缓存（发送缓存6KByte，接收缓冲6Kbyte）。 
开启独立缓存开关后，动态偶联服务端限制了每模块建立的偶联数量（默认只能建立一条偶联），不管是HeNB还是普通的eNB的服务端，都必须根据实际的规化，重新配置每模块上该动态偶联服务端需要支持的偶联数量。 
应用场景 :###### MME和HeNB直接建立安全通道的连接方式 
MME和HeNB直接建立安全通道的连接方式如[图2]所示。
图2  MME和HeNB直接建立安全通道的连接方式

MME和HeNB不需要通过SeGW提供IPSec隧道，HeNB的认证和自动配置等还是需要通过SeGW提供IPSec隧道。目的是减少SeGW的流量。最小成本部署HeNB。此时SeGW也需自己和HeNB建立IPSec隧道。
###### MME通过SeGW建立安全通道的连接方式 
MME使用SeGW和HeNB间建立IPSec安全通道，MME这边完全和宏eNB的组网一样，感知不到IPSec隧道加解密过程。HeNB的认证和自动配置可以和S1-MME使用同一条IPSec隧道。HeNB没有经过HeNB-GW汇接，MME这侧直接管理众多的HeNB。SeGW和HeNB的安全连接一般来说也是使用同一条IPSec隧道。 
###### MME通过HeNB-GW建立安全通道的连接方式 
MME通过HeNB-GW建立安全通道的连接方式如[图3]所示。
图3  MME通过HeNB-GW建立安全通道的连接方式

MME使用HeNB-GW/SeGW和HeNB间建立的IPSec安全通道。使用HeNB-GW时，一般来说SeGW和HeNB-GW是合一配置。MME这边完全和宏eNB的组网一样，感知不到IPSec隧道加解密过程，由于HeNB经过HeNB-GW汇接，MME这侧不能直接感知到HeNB，仅能看到HeNB-GW。HeNB-GW可以仅汇接HeNB的信令面（S1-MME），也可以汇聚HeNB的用户面（S1-U）。 
客户收益 :受益方|受益描述
---|---
运营商|提高服务质量：由于改善了室内信号覆盖质量，可以明显提高用户的宽带和语音服务质量。减少资本投入CAPEX：H(e)NB由用户购买，并且使用用户的宽带接入电路，减少了网络设备的扩容和相应基站链路的投资；减少运维成本OPEX，由于H(e)NB放置在用户家中，节省了机房、电源、空调和电路维护等运行成本；增加用户黏性，由于H(e)NB具有很好的室内覆盖特性和带宽，运营商再提供相应的家庭域服务套餐，可以给用户很好的业务体验，从而增加用户黏性和吸引其他网用户转网。增加每用户平均收入ARPU，由于室内覆盖性好和带宽高，用户将增加对多媒体服务的使用，从而增加ARPU。
终端用户|提高服务质量。
实现原理 :系统架构 :系统架构如[图4]所示。
图4  系统架构

涉及的网元 :网元名称|网元作用
---|---
H(e)NB|Home (e) NodeB, 将 EUTRAN无线接口上UE通过宽带IP接入运营商网络。
H(e)NB-GW|H(e)NB通过H(e)NB-GW接入运营商网络。通常包含汇聚功能。
SeGW|安全网关，所有连接都必须通过安全网关。
HMS|HeNB管理系统，可以支持HeNB的自动配置，升级等功能。
CSG List Server|管理用户CSG列表，通过OMA-DM/OTA接口更新手机中的CSG Allow list和Operater List。
MME|对用户CSG信息进行校验控制接入和移动管理。
HSS|提供用户的CSG签约信息。
PGW|根据MME通知的用户CSG信息进行计费。
本网元实现 :本网元的实现方式如[图5]所示。
图5  本网元实现

S1接口HeNB通知MME，用户接入的小区的CSG ID和接入模式；MME判断是否允许接入。 MME判断出用户是否是CSG的成员用户后，或用户的CSG成员身份发生改变，均会通知HeNB，HeNB根据用户是否是成员用户可以提供不同的服务。 
S10/Gn接口MME会向用户以前所在的网元请求上下文信息。MME在切换时，需要判断用户在目的小区是否是CSG的成员用户，如允许切换需告知目的网元相关的CSG信息。 
S6a接口获取用户CSG签约信息。 
S11接口MME通知SGW/PGW用户的CSG信息（UCI）。PGW可要求MME主动上报用户的CSG信息。 
业务流程 :CSG在移动管理，会话管理流程中均有体现，此处没有描述所有的CSG相关流程（参见协议23.401），仅描述常见的Attach、TAU、ServiceRequest、S1切换和CSG用户身份更改流程。 
Attach流程
Attach流程如[图6]所示。
图6  Attach流程

流程说明： 
UE发起Attach流程。 
HeNB会在S1消息INIT UE中携带自己的CSG ID和接入模式等信息。 
MME如果没有签约信息，则需要向HSS请求签约信息，包括CSG的签约信息。 
MME将HSS的CSG签约信息保存，并根据签约信息，判断当前用户是否是该CSG中的成员用户，是否允许接入该CSG。（闭合模式仅允许成员用户可以接入，混合模式可以接入，但成员用户会有更好服务。） 
MME在Create Session Req中将用户的CSG信息（CSG ID，是否是成员，接入模式等）都通知给SGW/PGW。 
MME需要保留Create Session Rsp中的CSG Change Action指示，用于判断后续是否能继续通知SGW/PGW相应的CSG信息。 
MME 将用户是否是该CSG的成员通知给HeNB（仅混合模式需要）。 
Attach成功。 
TAU流程
TAU流程如[图7]所示。
图7  TAU流程

流程说明： 
UE发起TAU流程，并指示Active标志。 
HeNB会在S1消息INIT UE中携带自己的CSG ID和接入模式等信息。 
如果是跨局TAU，那么MME将向OLD MME请求上下文，MME将保留上下文中CSG Change Action等字段。 
MME如果没有签约信息，则需要向HSS请求签约信息，包括CSG的签约信息。 
MME将HSS的CSG签约信息保存，并根据签约信息，判断当前用户是否是该CSG中的成员用户，是否允许接入该CSG。（闭合模式仅允许成员用户可以接入，混合模式可以接入，但成员用户会有更好服务。） 
如果CSG Change Action字段中指示需要上报CSG信息，MME在Create Session Req/Modify
Bear Req中将用户的CSG信息（CSG ID，是否是成员，接入模式等）都通知给SGW/PGW。 
MME需要保留Create Session Rsp/Modify Bear Rsp中的CSG Change Action指示，用于判断后续是否能继续通知SGW/PGW相应的CSG信息。 
MME 将用户是否是该CSG的成员通知给HeNB（仅混合模式需要）。 
TAU成功。 
 说明： 
如果TAU中没有Active flag，那么不需要通知SGW/PGW和HeNB相关的用户CSG信息。
Service
Request流程
Service Request流程如[图8]所示。
图8  Service Request流程

流程说明： 
UE发起Service Request流程。 
HeNB会在S1消息INIT UE中携带自己的CSG ID和接入模式等信息；MME根据签约信息，判断当前用户是否是该CSG中的成员用户，是否允许接入该CSG。（闭合模式仅允许成员用户可以接入，混合模式可以接入，但成员用户会有更好服务）。 
MME下发INITIAL Context Setup Request消息要求建立无线承载，如果是混合模式还需携带用户的CSG成员情况。 
HeNB会根据用户的CSG成员情况来建立无线承载。 
HeNB返回INITIAL Context Setup Response消息。 
如果之间保留的CSG Change Action字段中指示需要上报CSG信息，MME在Modify Bear Req中将用户的CSG信息（CSG
ID，是否是成员，接入模式等）都通知给SGW/PGW。 
MME需要保留Modify Bear Rsp中的CSG Change Action指示，用于判断后续是否能继续通知SGW/PGW相应的CSG信息。 
S1切换流程
S1切换流程如[图9]所示。
图9  S1切换流程

流程说明： 
source HeNB发起切换，source HeNB会在Handover Required消息中携带目的HeNB的CSGID和接入模式等信息。 
MME需根据签约信息，判断当前用户是否是Target HeNB的CSG中的成员用户，是否允许接入该CSG。（闭合模式仅允许成员用户可以接入，混合模式可以接入，但成员用户会有更好服务）允许接入就发送Forward
Relocation Request给Target MME，消息中包含CSG ID，是否是成员等信息。 
Target MME将接收到得CSG信息，通过Handover Request消息转发给HeNB。 
HeNB对CSG ID，接入模式等进行校验，如果不同则通过Handover Request Ack通知给MME。 后续同正常的切换流程，另外如果SGW/PGW请求CSG信息，那么需要通过Modify
Bear　Request消息将最新的用户CSG信息下发。 
CSG成员身份改变流程
闭合模式闭合模式流程如图10所示。图10  闭合模式流程说明： MME发起CSG用户身份改变流程。对于闭合模式，MME发送UE Context Modification
Request消息通知HeNB，成员身份改变。HeNB回应UE Context Modification Response消息。由于用户不是闭合CSG的成员用户，那么就不允许接入，HeNB就发起S1 Release流程或S1切换流程。如果HeNB没有发起S1 Release流程或S1切换流程，在一段时间后，MME强行发起S1 Release流程，不允许用户接入。 
混合模式混合模式流程如图11所示。图11  混合模式流程说明：MME发起CSG用户身份改变流程。对于混合模式，MME发送UE Context Modification
Request消息通知HENB，成员身份改变。HeNB回应UE Context Modification Response消息，对于非成员用户变为成员用户，HeNB需要提供更好服务标准；对于成员用户变为非成员用户，HeNB需要降低其服务标准。在通知HeNB同时，MME也需要发生Change Notification通知SGW/PGW，用户的成员身份发生改变，SGW/PGW可以根据最新的CSG信息来对用户计费。 
系统影响 :开启本功能时由于增加了对CSG信息的支持，对内存占用增加，因此在支持CSG用户的比例，以及平均的签约数量较大情况下，每个模块支持的用户数将会下降。 
CSG优化寻呼功能，涉及到复杂运算，对性能有部分影响。 
动态偶联配置影响，由于HeNB的偶联使用的缓冲大小和宏eNB的偶联使用的缓冲大小区别很大，需要区分服务端进行配置，并对每个动态偶联服务端配置缓冲大小和允许最大接入数量。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
与Paging功能|Paging优化需要在现有的Paging功能前进行，Paging优化结束或不要执行后才进行现有的Paging功能。
与位置上报功能|CSG更改上报功能和位置上报功能类型，基本上可以采用同样机制。但是位置上报和CSG更改触发的ChangeNotify通知可能同时发给SGW/PGW。
遵循标准 :标准名称
---
Evolved Universal Terrestrial Radio Access Network (E-UTRAN);S1 Application Protocol (S1AP)
General Packet Radio Service (GPRS);GPRS Tunnelling Protocol(GTP)across the Gn and Gp interface
3GPP Evolved Packet System (EPS); Evolved General PacketRadio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C)
Evolved Packet System (EPS); Mobility Management Entity(MME) and Serving GPRS Support Node (SGSN) related interfaces basedon Diameter protocol
General Packet Radio Service (GPRS) enhancements for EvolvedUniversal Terrestrial Radio Access Network (E-UTRAN) access
特性能力 :名称|默认容量指标|最大容量指标
---|---|---
支持的CSG用户比例|10%|100%
CSG用户平均签约的CSG数目|10|50
支持CSG的eNodeB数量|1万|2.5万
可获得性 :License要求 :该特性需要开启License，该特性需要申请了License许可后，运营商才能获得该特性的服务。 
对应的License项目为“MME支持CSG功能”（license ID：7023），此项目显示为“支持”，表示MME支持CSG功能。
对其他网元的要求 :HeNB|HSS|SGW|PGW|MME
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :新增命令配置项参见[表1]。
配置项|命令
---|---
CSG配置|SET CSGCFG
SHOW CSGCFG|CSG配置
基于IMSI号段限制CSG漫游配置|ADD IMSI CSG ROAM
SET IMSI CSG ROAM|基于IMSI号段限制CSG漫游配置
DEL IMSI CSG ROAM|基于IMSI号段限制CSG漫游配置
SHOW IMSI CSG ROAM|基于IMSI号段限制CSG漫游配置
性能统计 :新增性能计数器参见[表2]。
测量类型|描述
---|---
CSG测量|C430120001 闭合CSG小区附着请求次数
C430120002 闭合CSG小区附着成功次数|CSG测量
C430120003 混合CSG小区附着请求次数|CSG测量
C430120004 混合CSG小区附着成功次数|CSG测量
C430120005 闭合CSG小区跟踪区更新请求次数|CSG测量
C430120006 闭合CSG小区跟踪区更新成功次数|CSG测量
C430120007 混合CSG小区跟踪区更新请求次数|CSG测量
C430120008 混合CSG小区跟踪区更新成功次数|CSG测量
C430120009 闭合CSG小区业务请求次数|CSG测量
C430120010 闭合CSG小区业务请求成功次数|CSG测量
C430120011 混合CSG小区业务请求次数|CSG测量
C430120012 混合CSG小区业务请求成功次数|CSG测量
CSG用户数测量|C431030001 闭合CSG小区的平均成员用户数
C431030002 闭合CSG小区的最大成员用户数|CSG用户数测量
C431030003 混合CSG小区的平均成员用户数|CSG用户数测量
C431030004 混合CSG小区的最大成员用户数|CSG用户数测量
C431030005 混合CSG小区的平均普通用户数|CSG用户数测量
C431030006 混合CSG小区的最大普通用户数|CSG用户数测量
C431030007 签约的CSG用户数|CSG用户数测量
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME开通HeNB功能，需要开启MME支持HeNB功能的License，并对HeNB功能进行配置。
配置前提 :完成基本呼叫功能的数据配置、基本短消息业务配置。 
E-UTRAN、HSS、PGW、SGW等外接网元支持CSG功能。 
配置过程 :使用[SHOW LICENSE]命令，查看本局License是否支持CSG功能。如果不支持，需联系中兴通讯技术支持
获取License的支持。
使用[SET CSGCFG]命令，设置CSG配置信息。
使用[ADD IMSI CSG ROAM]命令，新增基于IMSI号段限制CSG漫游配置信息。
配置实例 :设置CSG配置，其中支持CSG功能的接口是S1口，签约CSG用户比例为50%，CSG用户平均签约CSG数目30，支持CSG的eNodeB数量为500，CSG寻呼消息不携带CSG
List，不支持CSG更改上报，不支持根据TAI查找HeNB-GW切换。命令如下： 
[SET CSGCFG]:INTERFACE="S1",SSCSGRAT=50,SSAVGCSG=30,CSGENBNUM=500,PGCSG="NO",CSGCHGRPT="NO",TAIHO="NO"
新增基于IMSI号段限制CSG漫游配置，其中IMSI号段为46001，CSG限制选项为使用签约的CSG。 
[ADD IMSI] CSG ROAM:IMSI="46001",LMTRES="USE"
调整特性 :通过[SET CSGCFG]命令修改CSG相关参数。
通过[SET IMSI CSG ROAM]命令修改基于IMSI号段限制CSG漫游配置。
## ZUF-78-15-004 Relay 
特性描述 :特性描述 :描述 :定义 :Relay即中继技术，在下行方向，基站发给UE的信号不直接发给UE，而是先发给一个中继站，再由中继转发给UE；在上行方向，UE的上行信号也不直接发给基站，而是先发给一个中继站，再由中继站转发给基站。
背景知识 :随着现在无线通信技术的不断发展，频谱资源已经变得格外紧张。为了获得3GPPLTE-A制定的高速无线宽带接入的设计目标，根据现有的频谱分配方案，大容量大宽带频谱在较高频段，而该频段路损和穿透损都较大，很难实现好的覆盖。中继技术作为LTE-Advanced系统的关键技术可以很好地解决这一问题，为小区带来更大的覆盖范围和系统容量。中继技术最终在R10中被引入到3GPP家族。
MME（RN）是指能够对ReLayNode进行识别、鉴权和建立管理通道的MME。
MME（UE）就是为LTE用户服务的MME。 
RelayNode即RN，就是中继节点，用于扩大无线覆盖和容量，RN支持eNB的功能，例如终结E-UTRA无线协议接口和S1和X2接口。RN也支持UE功能和协议的子集，用于无线连接到DeNB。
DeNB除支持eNB功能外，还内置和提供了SGW/PGW类似功能，用于RN的操作维护。包括为RN创建会话和管理EPS承载，以及终结和MME（RN）之间的S1-AP和S11接口。
ZXUN uMAC-MME同时实现了协议图中的MME（RN）和MME（UE）的功能，即物理上是合一网元。 
UE能够在RN下和eNodeB下接入，当移动到RN下时，使用RN的无线方式接入RN，RN再LTE接入到DeNB；当移动到eNodeB下时，使用LTE接入；对用户来说做到无缝移动。用户在RN下还是在eNodeB下对MME来说是不可见的，UE在同一个TA或TALIST下的RN之间移动对MME也是不可感知的。 
RN和DeNB间是无线连接的，RN是运营商的资源，运营商需要对其进行运维管理，所以将RN作为一个特殊的用户，RN附着时MME对其进行鉴权并为其建立运维管理的默认承载。
当需要对RN进行配置数据下发时，操作维护系统通过DeNB的内置GW建立专有承载，流程如[图1]所示。
图1  建立专有承载

当RN有告警需要上报或性能统计数据上报时，也会触发专有承载建立。 
应用场景 :Relay的主要作用是扩大小区的覆盖面积和提高系统容量：Relay可以为小区中阴影衰落严重的地区以及覆盖死角提供服务信号，同时如果中继站放置在原有小区覆盖范围内，如一些热点地区和室内也可以起到提高系统容量的作用。 
应用场景包括：农村区域覆盖、城市热点、盲区覆盖、室内热点区域等。 
客户收益 :受益方|受益描述
---|---
运营商|提高无线覆盖率，提升用户满意度
移动用户|业务使用更流畅
实现原理 :系统架构 :3GPP协议下的Relay架构如[图2]所示。
图2  3GPP协议下的Relay架构

涉及的网元 :网元名称|网元作用
---|---
RN|发起两种附着流程，一个是初始上电时，普通附着，得到初始配置数据后去附着，再发起RN附着请求，在RRC连接中指示RN；支持E-UTRA无线协议接口、S1和X2接口；支持UE能力子集。
DeNB|收到S1建立响应时记录MME的Relay能力；识别RN节点的RRC连接，并在给MME的初始UE消息中带上RN指示和内置的GW地址；和RN交互的能力。
MME|在S1建立响应中通知DeNB支持Relay；识别RN指示并进行鉴权，对通过鉴权的RN节点，根据DeNB给定GW地址为RN建立PDN连接。
HSS|能够为用户签约RN指示，能够将RN指示下发给MME。
本网元实现 :根据签约数据用户的RELAY能力授权处理原则参见下表。 
签约信息 “Relay-Node-Indicator”|eNodeB的Init UE带指示和地址|鉴权结果
---|---|---
NOT_RELAY_NODE(0)|带|附着拒绝
NOT_RELAY_NODE(0)|不带|执行普通附着
RELAY_NODE(1)|带|根据地址直接确定SGW和PGW，走Relay流程
RELAY_NODE(1)|不带|执行普通附着
根据本地配置的RELAY能力授权处理原则参见下表。 
网元级“RELAY_NODE ”|eNodeB的Init UE带指示和地址|鉴权结果
---|---|---
打开|带|根据地址直接确定SGW和PGW，走Relay流程
打开|不带|执行普通附着
关闭|带|附着拒绝
关闭|不带|执行普通附着
业务流程 :对支持RN的MME来说，只是RN的附着流程是特殊的：RN会进行两阶段的附着，第一阶段的RRC连接不会指示RN，DeNB和MME都做普通附着处理，此时请求的APN是特殊的APN，在附着后OAM下发初始配置数据给RN，RN再执行去附着，再进行第二阶段附着，此时RRC连接指示是RN，DeNB根据之前和MME的S1建立时的Relay指示，确定MME支持Relay，则在初始UE消息中带上RN指示和内置GW地址；MME收到后根据用户签约判断是否能够执行Relay附着，如果可以则直接根据DeNB给的GW地址建立PDN连接。 
RN的附着流程图如[图3]所示。
图3  RN的附着流程图

正常附着流程用于在以下异常情况下进行中继操作： 
按照TS33.401[41]协议的规定，RN和USIM-RN进行本地安全操作（例如，在RN和USIM-RN之间建一个安全通道）。 
RN从在阶段I中获得的列表中选择一个小区。 
RN与DeNB建立一个RRC连接，指示该连接是用于一个RN。 
DeNB获知支持RN功能的MME。当收到RN指示时，DeNB应确认当前、已选的或重选的MME支持RN功能。 
 说明： 
RN作为一个正常UE运行，例如RN的NAS可能使用IMSI或GUTI。同样，RN的NAS可能会或不会向RN的AS提供S-TMSI，因此RRCConnectionRequest消息可能包含S-TMSI或一个随机值。 
DeNB通过S1接口的Initial UE消息向MME发送RN指示。该消息也携带嵌入DeNB的S‑GW/PGW功能的IP地址。 
HSS向MME提供USIM-RN的签约数据。在该数据中，指示一个RN允许使用该签约。 
如果S1接口的Initial UE消息指示这是一个RN，但签约数据并没有表明该签约许可其作为RN运行，MME应拒绝NAS流程（例如：附着请求、跟踪区更新请求和业务请求等）并提供一个适当的原因。例如，USIM-RN避免在PLMN上进行重试，但不会影响突然进行PLMN重选的RN。 
 说明： 
可以预料的是，MME检查到USIM-RN的HPLMN已授权使得多个RN附着到该MME上。 
MME和RN执行正常的EPS鉴权流程。 
根据Initial UE消息中携带的IP地址，MME（或RN）从DeNB中为RN选择SGW/PGW（即在该阶段绕过了所有的GW选择和APN相关流程）。MME与位于DeNB的SGW/PGW通过S11接口进行信令交互。 
MME接受附着流程，并与DeNB一起建立S1上下文。 
系统影响 :RN对于MME来说一个特殊的用户，会占用MME的用户和承载资源。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
与IPv4IPv6双栈|DeNodeB带上来的GW（SGW和PGW合一）地址可以是双栈地址，MME不进行GW选择处理，只根据开关优先级、节点有效性来确定使用IPV4还是IPV6地址。
LIPA功能|Relay优先于LIPA，即如果初始UE消息中带RN指示和GW地址，则做Relay处理。
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network(E-UTRAN) access(Release 10)".
3GPP TS 29.272:"Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol(Release 10)"
3GPP TS 36.300:"Evolved Universal Terrestrial Radio Access(E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN)(Release 10)"
3GPP TS 36.413:"Evolved Universal Terrestrial Radio AccessNetwork(E-UTRAN);S1 Application Protocol (S1AP) (Release 10)"
特性能力 :功能受License开关控制。 
在HSS不支持Relay控制的情况下，MME可以进行本地控制是否容许RN节点接入。 
可获得性 :License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持Relay功能”（license ID：7030），此项目显示为“支持”，表示MME支持Relay功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :新增命令配置项参见[表1]。
配置项|命令
---|---
配置Relay|SET RELAYCFG
SHOW RELAYCFG|配置Relay
性能统计 :新增性能计数器参见[表2]。
测量类型名称|性能计数器名称
---|---
Relay节点数测量|C431040001 平均附着RN节点数
C431040002 最大附着RN节点数|Relay节点数测量
Relay测量|C430160001 RN节点附着请求次数
C430160002 RN节点附着成功次数|Relay测量
C430160003 RN节点发起的分离请求次数|Relay测量
C430160004 RN发起的分离成功次数|Relay测量
C430160005 MME发起的RN节点分离请求次数|Relay测量
C430160006 MME发起的RN节点分离成功次数|Relay测量
C430160007 HSS发起的RN节点分离请求次数|Relay测量
C430160008 HSS发起的RN节点分离成功次数|Relay测量
C430160009 RN专有承载激活请求次数|Relay测量
C430160010 RN节点专有承载激活成功次数|Relay测量
C430160011 RN节点专有承载去激活请求次数|Relay测量
C430160012 RN节点专有承载去激活成功次数|Relay测量
C430160013 RN节点请求承载资源分配请求次数|Relay测量
C430160014 RN节点请求承载资源分配成功次数|Relay测量
C430160015 RN节点请求承载资源修改请求次数|Relay测量
C430160016 RN节点请求承载资源修改成功次数|Relay测量
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :EMS中查询用户动态信息和签约信息可以显示RN节点指示。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :当MME支持Relay功能时，需要对Relay进行配置。 
配置前提 :MME license支持Relay功能。 
配置过程 :使用[SET RELAYCFG]设置Relay控制开关。
配置实例 :###### 实例场景-无线侧不支持RN 
配置说明
Relay功能开关关闭。 
配置脚本
命令脚本|解释说明
---|---
SET RELAYCFG:RELAY="LOCAL_CTRL_RELAY"&"BYPASS_APN_RELAY"|设置Relay控制开关，不选择“支持Relay”，本地Relay功能开关关闭。
###### 实例场景2–HSS支持Relay签约，无线侧支持Relay，不需要旁路APN检查 
配置说明
Relay功能开关打开。 
本地控制Relay开关不打开。 
旁路APN相关处理开关关闭。 
配置脚本
命令脚本|解释说明
---|---
SET RELAYCFG:RELAY="SUPPORT_RELAY"|设置Relay控制开关，仅选择“支持Relay”，其他两个开关不选择。
###### 实例场景3–HSS支持Relay签约，无线侧支持Relay，需要旁路APN检查 
配置说明
Relay功能开关打开。 
本地控制Relay开关不打开。 
旁路APN相关处理开关打开。 
配置脚本
命令脚本|解释说明
---|---
SET RELAYCFG:RELAY="SUPPORT_RELAY"&"BYPASS_APN_RELAY"|设置Relay控制开关，选择“支持Relay”和“支持旁路APN相关处理”；“支持本地控制Relay”开关不选择。
###### 实例场景4–HSS不支持Relay签约，无线侧支持Relay，不需要旁路APN检查 
配置说明
Relay功能开关打开。 
本地控制Relay开关打开。 
旁路APN相关处理开关关闭。 
配置脚本
命令脚本|解释说明
---|---
SET RELAYCFG:RELAY="SUPPORT_RELAY"&"LOCAL_CTRL_RELAY"|设置Relay控制开关，选择“支持Relay”和“支持本地控制Relay”；“支持旁路APN相关处理”开关不选择。
###### 实例场景5–HSS不支持Relay签约，无线侧支持Relay，需要旁路APN检查 
配置说明
Relay功能开关打开。 
本地控制Relay开关打开。 
旁路APN相关处理开关打开。 
配置脚本
命令脚本|解释说明
---|---
SET RELAYCFG:RELAY="SUPPORT_RELAY"&"LOCAL_CTRL_RELAY"&"BYPASS_APN_RELAY"|设置Relay控制开关，三个开关都打开。
测试用例 :测试项目|MME支持Relay功能，本地控制Relay功能关闭。
测试目的|验证MME支持Relay控制开关。
预置条件|MME和邻接网元运行正常。MME license支持Relay功能。MME网管使用命令SET RELAYCFG配置支持Relay开关关闭。
测试过程|MME给eNodeB的S1SETUP响应中不会带Relay能力。
通过准则|MME判断支持Relay功能开关关闭，给eNodeB的S1SETUP响应中不会带Relay能力。
测试结果|
测试项目|MME支持Relay功能，支持Relay功能打开。
测试目的|验证MME本地Relay控制开关。
预置条件|MME和邻接网元运行正常。MME license支持Relay功能。MME网管使用命令SET RELAYCFG配置支持Relay开关打开。
测试过程|MME给eNodeB的S1SETUP响应中携带Relay能力。
通过准则|MME判断支持Relay功能开关打开，给eNodeB的S1SETUP响应中带Relay能力。
测试结果|
## ZUF-78-15-005 LIPA 
特性描述 :特性描述 :描述 :定义 :LIPA即本地IP接入，是用户的业务流数据直接从家庭基站进行接入，不经过运营商的核心网络，相对于运营商的核心网络来说，这部分业务是直接从HeNB就分流出去了，从而减轻了核心网络的负荷和降低了核心网络的传输成本。
背景知识 :本地IP接入（LIPA）和IP数据分流（SIPTO）技术最初是基于家庭基站（HeNB）网络提出的。
如果通信系统中部署了HeNB，对于HeNB的用户，除了可以使用公众的Internet业务外，还可以与家庭网络中的其他节点进行联系，以共享家庭网络中的资源，并能与家庭网络中的拜访用户进行通信。如果引入LIPA技术，用户与家庭网络中其他节点间的数据传递完全可以直接通过HeNB实现，而无需再传递到核心网节点，这样既能减少数据传递时延，也能减少核心网元的信令负荷，降低核心网吞吐量和传输成本，并且运营商可将核心网资源最大化利用，为有价值的业务提供更好服务，提高用户体验。 
LIPA技术是对HeNB功能的增强，允许终端通过HeNB访问家庭/企业内部的IP资源。这为运营商基于HeNB，开发更多的家庭/企业特色的应用提供了可能。对于没有Wi-Fi能力的终端可以做到类似本地Wi-Fi访问的效果。同时，这种本地IP访问和Wi-Fi等的联合使用，通过一些新型的流移动性技术，可以提升用户的体验。 
应用场景 :在园区或中小企业部署家庭基站的场景下，为了使得用户能够对本地PDN网络内其他IP设备进行访问，可以在本地家庭基站网络内部署一个单独的本地网关来提供IP数据路由，如[图1]所示。通过这种部署架构，用户还能够在同一本地家庭基站网络内移动时保证本地访问业务不中断。当用户移动到其它的本地家庭基站网络或者宏基站网络时，不保证LIPA业务连续性。
图1  园区或企业本地网络

客户收益 :受益方|受益描述
---|---
运营商|用户的业务流数据直接从家庭基站进行接入，不经过运营商的核心网络，既能减少数据传递时延，也能减少核心网元的信令负荷，降低核心网吞吐量和传输成本，并且运营商可将核心网资源最大化利用，为有价值的业务提供更好服务，提高用户体验。
移动用户|享受优质的网络服务。
实现原理 :系统架构 :依据协议3GPP TS 23.401 R11 2012.06版本，LIPA网络架构如[图2]所示。
图2  LIPA架构

HeNB与LGW是合设的，本实现只考虑合设，不考虑HeNB与LGW分设即存在外部Sxx接口的情况。依据协议中该LIPA网络架构，[图2]中的HeNB视为普通eNodeB。
涉及的网元 :网元名称|网元作用
---|---
HeNB|通过Initial UE message或Uplink NAS transport消息携带LGW address，与LGW合设的HeNB建立与LGW的直接用户面通道，通过与LGW的直接用户面通道发送上行数据包给LGW。
MME|负责附着流程中LIPA PDN连接建立、UE请求LIPA PDN连接建立、业务请求激活LIPA承载、用户局内/局间跟踪区更新，MME先发起LIPAPDN去连接，再执行TAU、用户发生基于X2、S1和RAT间切换在LIPA PDN连接中的处理。
HSS|负责存储用户的LIPA签约信息，把用户的LIPA签约数据提供给MME。
SGW|管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。在LIPA功能中无特殊处理。
LGW|与HeNB合设，负责UE接入本地PDN，分配用户IP地址，完成承载管理功能。
本网元实现 :附着时默认LIPA PDN连接建立控制面流程如[图3]所示。
图3  附着时默认LIPA PDN连接建立控制面流程
Attach请求 
Initial UE带LGW地址 
创建会话请求带LGW地址 
创建会话请求 
创建会话响应 
创建会话响应，携带LGW TEIDU 
初始上下文建立请求，Correlation ID中携带LGW TEIDU 
初始上下文建立响应，携带eNodeB用户面地址和TEIDU 
修改会话请求，携带eNodeB用户面地址和TEIDU 
流程说明： 
UE发起附着请求。 
eNodeB发送Initial UE message，消息中GW Transport Layer Address参数携带LGW
address。 
MME根据用户APN的LIPA能力决定建立LIPA PDN连接，向SGW发送Create Session Request消息，消息中携带的PDN GW
address为LGW address。
SGW识别不出是LIPA PDN连接，其处理同已有实现，没有特殊处理。根据消息中携带的LGW address，向LGW发送Create
Session Request消息。 
LGW收到Create Session Request消息处理后，不会发送下行数据报文给SGW，在第7步执行后LGW通过与eNodeB的直接用户面通道发送这些下行数据包给eNodeB。 
SGW发送Create Session Response消息给MME，消息中携带的用户面PDN GW TEID (GTP-based
S5)是LGW的TEIDU，同时携带SGW的用户面地址和TEIDU。 
MME发送Initial Context Setup Request消息给eNodeB，消息中新增参数Correlation
ID携带LGW的TEIDU，同时携带SGW的用户面地址和TEIDU。 
eNodeB根据Correlation ID建立与LGW的直接用户面通道，建立后，eNodeB与LGW就可以互相传递上下行数据包了。eNodeB发送Initial
Context Response message给MME，消息中携带eNodeB的用户面地址和TEIDU，用于传递S1_U口 的下行数据包。 
MME通过修改会话请求将eNodeB的用户面地址和TEIDU带给SGW。 
LIPA PDN连接用户面数据流： 
上述步骤8执行后，eNodeB与LGW的直接用户面通道就建立了，用户的本地数据就直接通过本地网关LGW分流掉了，不再经过核心骨干网，如[图4]所示。
图4  LIPA PDN连接用户面数据流

上述步骤9执行后，eNodeB与SGW的S1-U口用户面通道也建立了，保留建立这个用户面通道的原因是，S1释放时MME保留LIPA
PDN连接，eNodeB通过内部信令通知合设的LGW释放到eNodeB的直接用户面通道。释放完成后，LGW接收到用户的下行数据包时，LGW会发送第一个下行用户数据包给SGW触发网络发起的业务请求。 
业务流程 :附着
本地用户APN的LIPA能力授权处理原则参见[表1]。
APN签约信息“LIPA-Permission”|eNodeB的LIPA能力|授权处理结果
---|---|---
LIPA-only|支持|执行LIPA PDN连接
LIPA-only|不支持|附着拒绝
LIPA-conditional|支持|执行LIPA PDN连接
LIPA-conditional|不支持|执行核心网PDN连接
LIPA-prohibited|—|执行核心网PDN连接
漫游用户的LIPA能力和其APN的LIPA能力授权处理原则参见[表2]。
用户签约信息“VPLMN-LIPA-Allowed”|APN签约信息 “LIPA-Permission”|eNodeB的LIPA能力|授权处理结果
---|---|---|---
允许|LIPA-only|支持|执行LIPA PDN连接
允许|LIPA-only|不支持|附着拒绝
允许|LIPA-conditional|支持|执行LIPA PDN连接
允许|LIPA-conditional|不支持|执行核心网PDN连接
允许|LIPA-prohibited|—|执行核心网PDN连接
不允许|—|—|执行核心网PDN连接
MME支持LIPA功能附着流程如[图5]所示。
图5  MME支持LIPA附着流程

正常过程： 本地用户的APN签约“LIPA-only”或“LIPA-conditional”，eNodeB提供LGW
address。
下面各步骤描述涉及附着流程改动和关键的步骤，其他步骤同现有系统附着流程处理，不再详述。 
附着流程图第2步，eNodeB通过Initial UE message发送Attach Request message给MME，LGW和eNodeB合设，Initial
UE message中的GW Transport Layer Address参数携带LGW address。 
附着流程图第11步，MME先识别eNodeB的LIPA能力，如果eNodeB在S1消息中携带GW Transport
Layer Address，则认为eNodeB支持LIPA。MME判断开关“是否使用本局配置的LIPA属性”关闭，附着请求携带的APN签约了“LIPA-only”或“LIPA-conditional”且eNodeB支持LIPA，则MME对此APN仅为用户选择本地的LGW提供LIPA业务，并且在会话上下文中保存LIPA
PDN连接标识。 
附着流程图第12步，MME选择SGW，使用Initial UE message中的GW Transport Layer
Address参数携带LGW address，发送Create Session Request消息给SGW，消息中携带的PDN GW
address 为LGW address。 
附着流程图第13步，SGW收到Create Session Request消息，根据消息中携带的LGW address，向LGW发送Create
Session Request消息。 
附着流程图第15步，LGW收到Create Session Request消息处理后，不会发送下行数据报文给SGW，在附着流程图第20步执行后，
LGW通过与eNodeB的直接用户面通道发送这些下行数据包给eNodeB。 
附着流程图第16步，SGW发送Create Session Response消息给MME，消息中携带的用户面PDN GW
TEID (GTP-based S5)是LGW的TEIDU，用于eNodeB通过与LGW的直接用户面通道发送上行数据包给LGW；消息中还携带其他参数与现有系统实现一样。 
附着流程图第17步，MME收到Create Session Response消息，发送Attach Accept，此消息通过Initial
Context Setup Request消息发送，对于LIPA PDN连接，Initial Context Setup Request消息中携带Correlation
ID，其值等于Create Session Response消息中携带用户面PDN GW TEID (GTP-based S5)即LGW的TEIDU，Correlation
ID使得eNodeB与LGW建立直接的用户面通道。其他参数与现有系统实现一样。 
附着流程图第20步，eNodeB使用Initial Context Setup Request消息中携带的Correlation
ID，建立与LGW的直接用户面通道，建立后，eNodeB与LGW就可以互相传递上下行数据包了。eNodeB发送Initial Context
Response message给MME，消息中携带eNodeB的用户面地址和TEIDU，用于传递S1_U口 的下行数据包。 
MME收到Initial Context Response message和Attach Complete消息，处理后发送Modify
Bearer Request消息给SGW，同现有系统实现。 
正常过程： 漫游用户的“VPLMN-LIPA-Allowed”签约“允许”，其APN签约“LIPA-only”或“LIPA-conditional”，eNodeB提供LGW
address。
漫游用户发起附着，下面各步骤描述涉及附着流程改动和关键的步骤，其他步骤同现有系统附着流程处理，不再详述。 
附着流程图第2步，eNodeB通过Initial UE message发送Attach Request message给MME，LGW和eNodeB合设，Initial
UE message中的GW Transport Layer Address参数携带LGW address。 
附着流程图第11步，MME先识别eNodeB的LIPA能力，如果eNodeB在S1消息中携带GW Transport
Layer Address，则认为eNodeB支持LIPA。MME判断是漫游用户，开关“是否使用本局配置的LIPA属性”关闭，“VPLMN-LIPA-Allowed”签约为“允许”，在附着请求携带的APN签约了“LIPA-only”或“LIPA-conditional”且eNodeB支持LIPA，则MME对此APN仅为用户选择本地的LGW提供LIPA业务，并且在会话上下文中保存LIPA
PDN连接标识。 
MME可能会与不支持LIPA签约数据的HSS对接，造成LIPA功能无法使用，MME支持能够在本地配置APN的LIPA属性（包括本地用户和漫游用户的）。需要设置LIPA配置支持配置“本局LIPA控制策略”和“APN的LIPA属性”。
UE请求PDN连接
UE请求LIPA PDN连接流程如[图6]所示。
图6  UE请求LIPA PDN连接流程图

本地用户或漫游用户发起PDN连接请求，下面各步骤描述涉及UE请求PDN连接流程改动和关键的步骤，其他步骤同现有系统UE请求PDN连接流程处理，不再详述。 
流程图第1步，eNodeB通过Uplink NAS transport发送PDN Connectivity Request消息给MME，LGW和eNodeB合设，Uplink
NAS transport消息中的GW Transport Layer Address参数携带LGW address。 
流程图第2步，如果MME要创建新的会话上下文，则执行LIPA属性授权处理：MME先识别eNodeB的LIPA能力，如果eNodeB在S1消息中携带GW
Transport Layer Address，则认为eNodeB支持LIPA。MME决策是否建立LIPA PDN连接，本地用户和漫游用户的LIPA授权处理同附着流程PDN连接过程描述，这里不再展开描述，决策结果有如下三种： 
执行LIPA PDN连接，在会话上下文中保存LIPA PDN连接标识。 
执行核心网PDN连接。 
拒绝PDN连接。 
如果MME找到已有会话上下文，则不再执行LIPA属性授权处理，如果会话上下文中的LIPA PDN连接标识无效，则执行核心网PDN连接处理；如果会话上下文中的LIPA
PDN连接标识有效，则执行LIPA PDN连接处理。 
MME使用Uplink NAS transport消息中的GW Transport Layer Address参数携带LGW
address，发送Create Session Request消息给SGW，消息中携带的PDN GW address 为LGW address。 
流程图第3步，SGW收到Create Session Request消息，根据消息中携带的LGW address，向LGW发送Create
Session Request消息。 
流程图第4步，LGW收到Create Session Request消息处理后，不会发送下行数据报文给SGW，在流程图第9步执行后，LGW通过与eNodeB的直接用户面通道发送这些下行数据包给eNodeB。 
流程图第5步，SGW发送Create Session Response消息给MME，消息中携带的用户面PDN GW TEID
(GTP-based S5)是LGW的TEIDU，用于eNodeB通过与LGW的直接用户面通道发送上行数据包给LGW；消息中还携带其他参数与现有系统实现一样。 
流程图第6步，MME收到Create Session Response消息，发送PDN Connectivity Accept，此消息通过E-RAB
SETUP REQUEST消息发送，对于LIPA PDN连接，E-RAB SETUP REQUEST消息中携带Correlation
ID，其值等于Create Session Response消息中携带用户面PDN GW TEID (GTP-based S5)即LGW的TEIDU，Correlation
ID使得eNodeB与LGW建立直接的用户面通道。E-RAB SETUP REQUEST消息中还携带其他参数与现有系统实现一样。 
流程图第9步，eNodeB使用E-RAB SETUP REQUEST消息中携带的Correlation ID，建立与LGW的直接用户面通道，建立后，eNodeB与LGW就可以互相传递上下行数据包了。eNodeB发送E-RAB
SETUP RESPONSE给MME，消息中携带eNodeB的用户面地址和TEIDU，用于传递S1_U口 的下行数据包。 
MME收到E-RAB SETUP RESPONSE和PDN Connectivity Complete消息，处理后发送Modify
Bearer Request消息给SGW，同现有系统实现。后续处理同现有系统，流程跳转至N0130。 
选择核心网PGW建立核心网PDN连接同现有系统实现。 
MME拒绝PDN连接，发送PDN Connectivity Reject消息，携带ESM cause为“Service
option not supported”。 
S1释放
在S1释放流程中，如果有LIPA PDN连接，eNodeB通过内部信令通知合设的LGW释放到eNodeB的直接用户面通道。释放完成后，LGW接收到用户的下行数据包时，LGW会发送第一个下行用户数据包给SGW触发网络发起的业务请求。MME在S1释放流程中，不涉及改动，根据eNodeB的指示同现有系统处理即可。 
业务请求
UE发起的业务请求
UE发起业务请求，MME有LIPA
PDN连接存在，可能还存在其他PDN连接，与LIPA承载一起激活。流程如[图7]所示。
图7  UE发起业务请求在LIPA PDN连接中的处理流程

用户发起业务请求，eNodeB通过Initial UE message发送Service Request消息给MME，Initial
UE message中的GW Transport Layer Address参数携带LGW address。 
MME收到业务请求，如果有LIPA PDN连接存在，且该消息中携带的LGW地址与MME初始建立LIPA PDN连接时保存的LGW地址一样，说明用户接入的小区与初始接入的LGW有连接，则同现有系统继续处理UE发起的业务请求流程。 
流程图第4步，MME发送Initial Context Setup Request消息，对于LIPA PDN连接该消息中携带Correlation
ID，其值为LGW的TEIDU，Correlation ID使得eNodeB与LGW建立直接的用户面通道。Initial Context
Setup Request消息中还携带其他参数与现有系统实现一样。 
eNodeB使用Initial Context Setup Request消息中携带的Correlation ID，建立与LGW的直接用户面通道，建立后，eNodeB与LGW就可以互相传递上下行数据包了。流程图第7步，eNodeB发送Initial
Context Setup Complete给MME。 
流程图第9、10步，SGW对LIPA PDN连接与LGW交互完成承载修改。 
网络侧下行数据触发的业务请求
网络侧下行数据触发的业务请求在LIPA PDN连接中的处理，流程如[图8]所示。
图8  网络侧下行数据触发业务请求在LIPA PDN连接中的处理流程

正常过程1处于IDLE态的用户，如果其LIPA PDN连接存在，LGW接收到用户的下行数据包时，LGW会发送第一个下行用户数据包给SGW，并缓存所有其他的下行用户数据包，SGW收到后触发MME寻呼用户。 
MME寻呼用户时，根据现有系统寻呼策略，配置优化寻呼策略。 
寻呼成功，UE发起业务请求。 
用户进入连接态，SGW还通过S1-U口下发数据包给eNodeB和用户，LGW通过与eNodeB的直接用户面通道发送缓存的下行数据包给eNodeB。 
正常过程2处于CONNECTED态的用户，如果其LIPA PDN连接存在，SGW下发下行数据通知。 
MME收到下行数据通知，MME发送Initial Context Setup Request消息，对于LIPA PDN连接该消息中携带Correlation
ID，其值为LGW的TEIDU，Correlation ID使得eNodeB与LGW建立直接的用户面通道。Initial Context
Setup Request消息中还携带其他参数与现有系统实现一样。 
eNodeB使用Initial Context Setup Request消息中携带的Correlation ID，建立与LGW的直接用户面通道，建立后，eNodeB与LGW就可以互相传递上下行数据包了。eNodeB发送Initial
Context Setup Complete给MME。 
MME对LIPA PDN连接与SGW、LGW交互完成承载修改。 
扩展业务请求
MME收到扩展业务请求，业务类型指示是起呼/终呼CSFB，MME有LIPA
PDN连接存在，可能还存在其他PDN连接，不带着LIPA PDN连接执行CSFB的切换。 
正常过程： MME在ECM-CONNECTED态，部分LIPA
PDN连接，部分其他PDN连接。
用户发起扩展业务请求，业务类型指示CSFB（低4个BIT位取值是0-mobile originating CS fallback
or 1xCS fallback、1-mobile terminating CS fallback or 1xCS fallback、2-mobile
originating CS fallback emergency call 、2-1xCS fallback emergency
call）。 
eNodeB通过UPLINK NAS TRANSPORT消息发送Extended Service Request消息给MME。 
MME收到扩展业务请求，同现有系统处理Extended Service Request。 
MME发送S1‑AP Request message（UE CONTEXT MODIFICATION REQUEST消息，携带CS
Fallback Indicator)到eNodeB包含CSFB指示。此消息中对LIPA没有特殊处理。 
eNodeB检测到UE不仅有LIPA PDN连接，还有其他PDN连接，仍然会发起切换Handover Required；eNodeB在发起切换前，先通过内部信令通知合设的LGW发起LIPA
PDN去连接，连接释放后再通知MME进行切换；如果eNodeB没有发起LIPA PDN去连接，MME收到切换请求，LIPA PDN连接存在，则切换失败。原则是不带着LIPA
PDN连接执行切换，后续主被叫CSFB处理同现有系统。 
跟踪区更新
局内TAU
如果有LIPA PDN连接存在，还存在其他PDN连接，MME先发起LIPA
PDN去连接，再执行TAU；处理流程如[图9]所示。
图9  LIPA PDN连接在局内TAU中的处理流程

正常过程：用户发起局内TAU。 
eNodeB通过Initial UE message或UPLINK NAS TRANSPORT消息发送TAU Request消息给MME，Initial
UE message或UPLINK NAS TRANSPORT消息中的GW Transport Layer Address参数携带LGW
address。 
MME收到TAU Request消息，鉴权和安全性处理完后，如果有LIPA PDN连接存在，还存在其他PDN连接，且该消息中携带的LGW地址与MME初始建立LIPA
PDN连接时保存的LGW地址不一样，说明用户接入的小区与初始接入的LGW无连接，则MME先发起LIPA PDN去连接。 
MME针对LIPA PDN连接，发送Delete Session Request消息给老的SGW。 
流程图第6步，MME收到Delete Session Response消息，释放该LIPA PDN连接的核心网资源；所有LIPA
PDN去连接后，则继续执行局内TAU流程。 
MME向新SGW发送Create Session Request消息，消息中不会携带LIPA承载。后续同现有系统处理。 
如果局内TAU执行成功，MME向UE发送TAU Accept消息，消息中无LIPA承载。 
局间TAU
如果有LIPA PDN连接存在，还存在其他PDN连接，老局MME先发起LIPA
PDN去连接，再向新局MME发送上下文请求响应，新局执行TAU；处理流程如[图10]所示。
图10  LIPA PDN连接在局间TAU中老局MME的处理流程

正常过程
用户发起局间TAU。 
新局MME收到TAU Request消息，向老局MME发送Context Request消息。 
老局MME收到Context Request消息，如果有LIPA PDN连接存在，还存在其他PDN连接，则MME先发起LIPA
PDN去连接。MME针对LIPA PDN连接，发送Delete Session Request消息给老的SGW。 
流程图第6步，老局MME收到Delete Session Response消息，释放该LIPA PDN连接的核心网资源；所有LIPA
PDN去连接后，则向新局MME发送Context Response消息，消息中不携带LIPA PDN连接。 
新局MME收到Context Response消息，鉴权和安全性处理成功后，向老局发送Context Acknowledge消息。接着新局向新SGW发送Create
Session Request消息，消息中不会携带LIPA承载。后续同现有系统处理。 
如果局间TAU执行成功，新局MME向UE发送TAU Accept消息，消息中不携带LIPA承载上下文。 
LGW发起的承载去激活
eNodeB通过内部信令请求LGW释放LIPA
PDN连接时，LGW发起承载去激活。流程如[图11]所示。
图11  LGW发起的承载去激活流程

MME释放LIPA PDN连接同现有系统PDN连接释放，这里不再详述。 
切换
存在LIPA PDN连接的切换，eNodeB在发起切换前，先通过内部信令通知合设的LGW发起LIPA PDN去连接，连接释放后再通知MME进行切换。因此，
MME收到切换请求，LIPA PDN连接应该已释放，协议23.401要求MME只需要检查是否存在LIPA PDN连接，如果不存在同现有系统执行切换；如果存在，则通知eNodeB切换失败。 
基于X2的eNodeB间的切换
用户发生基于X2的eNodeB间切换，如果MME存在LIPA PDN连接，则MME通知目标基站切换失败。流程如[图12]所示。
图12  X2切换，MME不支持发起LIPA PDN去连接

正常过程
用户发生基于X2的eNodeB间切换。 
流程图中第1步之前的处理各网元没有改变。 
MME收到X2切换请求Path Switch Request，如果MME LIPA PDN连接存在，则MME向目标基站发送切换失败消息Path
Switch Request Failure，携带Cause为“Handover Failure In Target EPC/eNB
Or Target System”。 
MME发起显式分离流程。其他同现有系统处理。 
基于S1的eNodeB间的切换
用户发生基于S1的eNodeB间切换，如果源MME存在LIPA
PDN连接，则源MME通知源基站切换准备失败。流程如[图13]所示。
图13  S1切换，MME不支持发起LIPA PDN去连接

正常过程
用户发生基于S1的eNodeB间切换。 
流程图中第1步及之前的处理各网元没有改变。 
源MME收到S1切换请求Handover Required。 
如果源MME存在LIPA PDN连接，则源MME向源eNodeB发送切换准备失败消息Handover Preparation
Failure，携带Cause为“Handover Failure In Target EPC/eNB Or Target System”。 
E-UTRAN到UTRAN Iu模式RAT间切换
用户发生E-UTRAN到UTRAN Iu模式RAT间切换，如果源MME存在LIPA
PDN连接，则源MME通知源基站切换准备失败。流程如[图14]所示。
图14  RAT间切换，MME不支持发起LIPA PDN去连接

正常过程
用户发生E-UTRAN到UTRAN Iu模式RAT间切换。流程图中第1步及之前的处理各网元没有改变。 
源MME收到切换请求Handover Required。 
如果源MME存在LIPA PDN连接，则源MME向源eNodeB发送切换准备失败消息Handover Preparation
Failure，携带Cause为“Handover Failure In Target EPC/eNB Or Target System”。 
以上三种切换流程，考虑兼容LGW在切换前没有释放LIPA PDN连接的情况，本功能使用开关“在切换中MME支持发起LIPA
PDN去连接”控制本局可以发起LIPA PDN去连接。 
专有承载建立和UE请求的承载资源修改
协议23.401上已明确，R11 2012.06协议版本LGW和PCRF之间没有接口，LIPA PDN连接上不支持建立专有承载，LGW会拒绝所有UE请求的承载资源修改。MME对此不作限制，根据LGW的指示进行处理。同现有系统专有承载建立和UE请求的承载资源修改处理。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
支持HeNB_CSG功能|LIPA遵从已有CSG实现，目前不支持CSGservice-selection参数，不考虑CSG中service-selection的APN NI关于LIPA属性的签约。
GW选择功能|LIPA PDNLGW和SGW的选择策略与已有的PGW和SGW选择策略不同，独立实现：LGW选择：eNodeB在InitialUE message和Uplink NAS transport消息中GW Transport Layer Address参数携带LGW的控制面地址，这个参数同时也被MME用来识别eNodeB的LIPA能力，因此LGW选择时直接使用消息中携带LGWaddress，无其他策略。 SGW选择：LIPA PDN连接建立时选择SGW，选择策略遵守以下几点，其他同已有SGW选择处理：不考虑SGW和LGW的拓扑关系。考虑LGW节点有效性，结合SGW和LGW选择出可用的SGW。
LTE紧急呼叫功能|紧急呼叫功能优先级高于LIPA功能，如果是紧急呼叫，则不再执行LIPA流程。
性能统计功能|新增MME LIPA测量；对现有系统已有的相关计数器，视LIPAPDN连接和LIPA承载为普通PDN连接和一般承载，同现有系统上报性能统计。
APN更正功能|如果发生APN更正，支持对更正后的APN执行LIPA能力授权处理，遵守本功能LIPAPDN处理原则。
业务IP双栈优选的IP类型功能|MME在LGW选择时直接使用InitialUE message和Uplink NAS transport消息中消息中携带LGW address，这个地址可能是IPV4，IPV6或IPV4&IPV6，如果MME不支持IPv6，则使用IPV4；如果MME支持IPv6，地址双栈时根据子网优先级进行处理，如果IPV4和IPV6同一子网优先级，再根据安全变量“与非邻接网元交互时业务IP双栈优选的IP类型”的设置，使用IPV4或IPV6。
UBAS功能|不为LIPA功能增加新的UBAS信息上报。
支持Relay功能|如果附着请求中带有RN节点指示，则为Relay节点；如果没有RN指示而只有GW地址，则根据LIPA的原则判断是否建立LIPAPDN连接。
插入用户数据功能|HSS插入用户数据时，MME检测发现LIPA属性改变，实时生效。
遵循标准 :标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network(E-UTRAN) access".
3GPPTS36.413: "Evolved Universal TerrestrialAccess Network (E-UTRAN); S1 Application Protocol (S1AP)".
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS".
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".
3GPP TS 36.300: " Evolved Universal Terrestrial Radio Access(E-UTRA)  and Evolved Universal Terrestrial Radio Access Network (E-UTRAN)".
3GPP TR 23.829: " Local IP Access and Selected IP TrafficOffload (LIPA-SIPTO) ".
3GPP TR 23.859: " LIPA Mobility and SIPTO at the Local Network".
3GPP TS 24.301: " Non-Access-Stratum (NAS) protocol  forEvolved Packet System (EPS)".
3GPP TS 24.008: " Mobile radio interface Layer 3 specification;Core network protocols; Stage 3 ".
特性能力 :该特性不涉及规格指标。 
可获得性 :License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持LIPA功能”（license ID：7031），此项目显示为“支持”，表示MME支持LIPA功能。
对其他网元的要求 :HeNB|MME|SGW|LGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
###### 组网规划要求 
支持LIPA的HeNB与LGW合设。 
支持LIPA的HeNB与MME、SGW互通。 
与HeNB合设的LGW与SGW互通。 
O&M相关 :命令 :新增命令配置项参见[表3]。
配置项|命令
---|---
本局LIPA控制策略配置|SET LOCAL LIPA CTRL
SHOW LOCAL LIPA CTRL|本局LIPA控制策略配置
APN的LIPA属性配置|ADD APN LIPA ATTR
SET APN LIPA ATTR|APN的LIPA属性配置
DEL APN LIPA ATTR|APN的LIPA属性配置
SHOW APN LIPA ATTR|APN的LIPA属性配置
性能统计 :新增性能计数器参见[表4]。
测量类型名称|性能计数器名称
---|---
LIPA承载数测量|C431050001 激活LIPA默认承载平均数
C431050002 激活LIPA默认承载最大数|LIPA承载数测量
LIPA测量|C430180001 LIPA PDN连接请求次数
C430180002 LIPA PDN连接成功次数|LIPA测量
C430180003 LIPA PDN连接失败次数(UE原因导致)|LIPA测量
C430180004 LIPA PDN连接失败次数(GW原因导致)|LIPA测量
C430180005 LIPA PDN连接失败次数(MME内部原因导致)|LIPA测量
C430180006 LIPA PDN连接失败次数(DNS原因导致)|LIPA测量
C430180007 UE请求的LIPA PDN去连接请求次数|LIPA测量
C430180008 UE请求的LIPA PDN去连接成功次数|LIPA测量
C430180009 LIPA PDN去连接请求次数|LIPA测量
C430180010 LIPA PDN去连接成功次数|LIPA测量
C430180011 默认LIPA承载激活请求次数|LIPA测量
C430180012 默认LIPA承载激活成功次数|LIPA测量
C430180013 默认LIPA承载激活失败次数(UE原因导致)|LIPA测量
C430180014 默认LIPA承载激活失败次数(eNodeB原因导致)|LIPA测量
C430180015 默认LIPA承载激活失败次数(MME内部原因导致)|LIPA测量
C430180016 默认LIPA承载激活失败次数(GW原因导致)|LIPA测量
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :可以通过EMS查询用户的LIPA签约信息，也可以通过EMS查询用户的动态信息，确认用户的PDN连接的LIPA属性。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :当MME支持LIPA功能时，需要对LIPA进行配置。 
配置前提 :支持LIPA的license已经开启。 
配置过程 :配置本局LIPA控制策略。 
（可选）配置APN的LIPA属性。 
 说明： 
如果第一步配置的控制策略有使用本局配置的LIPA属性，则需要配置第二步，否则不需要。 
配置实例 :###### 使用签约的LIPA属性 
设置LIPA控制策略为使用本局配置的LIPA属性和在切换中MME支持发起LIPA
PDN去连接，命令如下： 
[SET LOCAL LIPA CTRL]:LIPACTL="LOCAL"&"DISCON"
###### 使用MME配置的LIPA属性 
设置本局LIPA控制策略为使用本局配置的LIPA属性、漫游用户开启LIPA功能和在切换中MME支持发起LIPA PDN去连接，命令如下： 
[SET LOCAL LIPA CTRL]:LIPACTL="LOCAL"&"ROAMING"&"DISCON"
设置APN的LIPA属性，APN名称为zte.com、LIPA属性为LIPA条件签约，命令如下： 
[ADD APN LIPA ATTR]:APN="zte.com",LIPAATTR="CONDITIONAL"
测试用例 :测试项目|附着建立LIPA
测试目的|验证附着流程中建立LIPA连接。
预置条件|本地用户，请求的APN本局配置的LIPA属性为LIPA签约。
测试过程|用户发起4G附着，enodeb在initialUE中通过GW transport layer address参数携带LGW地址。
通过准则|按照LIPA PDN建立。MME发送的create session request中携带的PDN GW address为LGW address，收到的create session response携带的用户面PDN GW TEID (GTP-basedS5)是LGW的TEIDU，同时携带SGW的用户面地址和TEIDU。MME发送Initial Context Setup Request新增参数Correlation ID携带LGW的TEIDU，同时携带SGW的用户面地址和TEIDU（同现有填写）。MME发送ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST携带Connectivitytype，值为1。MME收到enodeb的Initial Context Response后，发送modify bearer request携带eNodeB的用户面地址和TEIDU带给SGW。新增LIPA相关统计项统计正确，新增外部接口参数信令跟踪解码正确。
测试结果|
测试项目|LIPA PDN的TAU
测试目的|验证局内TAU流程中MME对LIPAPDN处理的合理性。
预置条件|用户已经通过附着和PDN连接建立了到同一个APN的多个LIPAPDN。
测试过程|用户发起局内TAU，不跨SGW，有激活标记，LGW与初始LGW地址相同。
通过准则|TAU正常处理所有LIPA PDN的承载。MME发送Initial Context Setup Request新增参数Correlation ID携带LGW的TEIDU，同时携带SGW的用户面地址和TEIDU（同现有填写）。MME收到enodeb的Initial Context Response后，针对每个PDN发送modify bearerrequest携带eNodeB的用户面地址和TEIDU带给SGW。
测试结果|-
## ZUF-78-15-006 eMBMS 
特性描述 :特性描述 :描述 :定义 :eMBMS（增强型多媒体广播多播业务）技术是基于3GPP
R9协议规定的增强型广播多播技术，是移动领域最高效的视频承载技术之一，通过使用该技术极大地降低了LTE网络下多媒体业务的资源占用，提高了媒体业务收益。
背景知识 :移动视频技术的发展主要经历了三个阶段，MBMS（多媒体广播多播业务）出现之前的广播多播业务，MBMS阶段以及eMBMS阶段。
早在MBMS出现之前，移动通信网上的广播多播业务采用的是点到点的多次发送，即将数据传送到不同的用户，每个用户使用专用的管道，为全单播模式。采用小区广播（CBS，Cell
Broadcast Service），CBS的特点是即使没有用户，数据也在所有的小区广播，而且速率很低，CBS是基于消息的，不能承载多媒体内容。这些技术的缺点是资源利用率低，广播能力差，用户管理能力不强，多媒体支持能力弱。 
MBMS是3GPP R6中定义的多媒体广播组播功能。MBMS支持多媒体广播业务和组播业务两种模式，既可以将多媒体视频信息直接向所有用户广播，也可以发送给一组收费的签约用户收看，可以帮助运营商开展多媒体广告、免费和收费电视频道、彩信群发等多种商业应用，运营商以较低的网络部署成本就可开展手机电视业务。但由于3G带宽不够、移动视频产业链生态环境不成熟等原因没有发展起来。 
eMBMS技术是基于3GPP R9协议规定的增强型广播多播技术，是移动领域最高效的视频承载技术之一。与上一代MBMS视频承载技术相比，eMBMS技术能支持更大的带宽，这意味着能提供更多的频道和视频内容，同时视频画面更清晰流畅，用户体验更好。eMBMS也被称为LTE广播，是一种先进的移动数据传输技术，可以使运营商显著降低在LTE网络上同一时间向多个用户提供诸如视频、音频等高带宽内容的成本。 
单播和eMBMS方式比较如[图1]所示。
图1  单播和eMBMS方式比较

应用场景 :eMBMS根据业务类型分为流媒体业务、信息广播业务、交互类业务和数据下载业务。 
常见的场景包括： 
手机电视可以对电影、电视剧、音乐、体育赛事等播放中插播广告。 
频道出租可以租赁无线频道给媒体商，按频道带宽和使用进行收费。 
行业市场可以对出租车、公交、地铁等视频下载类业务进行后向收费。 
特定区域视频广播对商场广告、体育场赛事、企业园区宣传片等进行后向收费。 
客户收益 :受益方|受益描述
---|---
运营商|提高运营成本效益：在时间维度和业务维度上有效调配网络资源，帮助运营商更加高效的提供移动视频服务。节约投资成本：有效的缓解运营商网络扩容的压力。提高用户满意度：提高用户体验，提升用户忠诚度。
移动用户|提升终端用户体验：移动视频更流畅，提高终端用户体验，享受优质的网络服务。更低资费：视频点播业务不根据流量计费
实现原理 :系统架构 :3GPP 定义的eMBMS的系统架构如[图3]所示。
图3  eMBMS系统架构

 说明： 
MCE可和eNodeB合一，也可能分离。 
BMSC根据内容提供方的指示通过MBMS-GW、MME和MCE启动、修改或停止eMBMS会话，通过MBMS-GW和eNodeB下发视频等内容，并对eMBMS进行计费、鉴权等控制。 
涉及的网元 :网元名称|网元作用
---|---
UE|支持MBMS，能够处理广播的MBMS业务信息给用户选择，并可以激活去激活MBMS业务。
eNB|支持IP组播功能，能够接收MBMSGW组播的MBMS数据，负责MBMS数据在MBMS业务区的传递。
MCE|负责分配eMBMS业务所需时域、频域、MCS等无线资源。
MME|进行MBMS会话控制，支持连接多个MCE，支持根据MCE服务区和MBMS业务区确定会话应该在哪些MCE建立。
MBMSGW|使用IP多播协议通过M1接口传送用户面数据到eNB，通过MME节点发送会话控制信令到EUTRAN。
BM-SC|提供eMBMS业务操作、会话传输、安全控制、内容同步、分配组播目的IP地址以及传输的GTPU C-TEID等功能。
协议栈 :M3接口协议栈如[图4]所示。
图4   M3接口协议栈

Sm接口协议栈接口如[图5]所示。
图5  Sm接口协议栈

业务流程 :MME在eMBMS业务中的作用就是参与节目开始时的会话建立和节目结束时的会话停止，以及MCE的接入管理。 
eMBMS业务在用户层面对MME是不可见的，用户层面数据流量上对SGW/PGW也是不可见的。 
总体eMBMS业务流程如[图6]所示。
图6  eMBMS业务示意图

业务流程： 
比赛等在特定时间开播，内容提供商通过eMBMS网络发布该业务。
eMBMS网络为该业务分配必要的信息，如IP组播地址。并通过通告的方式通知到感兴趣的终端，通告方法可以是短消息、E-Mail、WAP推送、甚至是传统的媒体。通告的内容包括节目的组播地址、节目的开始结束时间、总的时长等信息。
终端用户根据通告决定是否收听/收看该节目，如果决定收听/收看该节目，则该终端可以加入该节目。 
节目开始，网络开始传送该节目的内容；收听该节目的终端可以收看/收听该节目内容。 
节目进行中，终端可以选择加入、退出该节目的收听/收看。 
节目结束，网络结束该节目的内容传送，业务结束。 
会话启动
详见3GPP协议23.246的8.3.2节。 
在BM-SC准备好发送数据时，就会发起eMBMS会话启动过程进行数据传输。通过该过程激活eMBMS数据传输所有必须的网络承载资源。并且通知感兴趣的UE数据的传输即将启动。
会话启动流程参见[图7]。
图7  会话启动流程

流程说明： 
BM-SC发送eMBMS会话启动请求消息给MBMS GW指示即将开始的传输，携带提供会话属性：TMGI、Flow Identifier、QoS、MBMS服务区、会话标识符、预估的会话持续时间、给MBMS
GW的MBMS控制平面节点（MMEs）列表、接入指示（Access indicator）等。 
Flow Identifier
：BM-SC可以为同一个MBMS业务（由TMGI标识）发起多个会话，多个会话包含不同的内容。此时，需要在会话启动请求中会包含流标识（Flow
Identifier）用来区分不同的子会话。 
Access indicator（接入指示）表示MBMS业务应该在哪种无线接入下播出，即UTRAN或E-UTRAN或两者兼而有之。接入指示可以包含在由MBSM
GW生成的计费信息中。 
下游节点列表：通知MBMS GW需要发送给哪些MME。 
MBMS服务区：供MME使用，与MCE的SETUP的服务区匹配。对于相同的区域，则向相应的MCE转发会话启动消息。 
MBMS GW处理后，向BM-SC回响应消息。 
MBMS GW发送eMBMS会话启动请求消息给MME，携带会话的属性：TMGI、 Flow Identifier、 QoS、
MBMS服务区、会话标识符、预估的会话持续时间、传输网络的IP多播地址、C-TEID等（消息中的详细参数参见29.274的定义）。 
MME收到会话启动请求消息，创建MBMS承载上下文，将会话属性保存在MBMS承载上下文中。根据会话请求消息中的MBMS服务区查询出相应的MCE列表，即：哪些MCE带了相同的MBMS服务区。根据开关的状态决策是向查询到的MCE列表还是所有的MCE发送会话启动请求消息，消息携带会话的属性：TMGI、
Flow Identifier、 QoS、 MBMS服务区、会话标识符、预估的会话持续时间、传输网络的IP多播地址、C-TEID等（消息中的详细参数参见36.444的定义），MME设置等待响应定时器。 
MCE创建MBMS承载上下文并存储会话信息后，向MME回复响应。 
MME收到一个成功的响应，立即回成功的响应给MBMS GW；收到所有的失败响应或者定时器超时，回失败的响应给MBMS
GW。 
MCE/E-UTRAN建立用于将MBMS数据传输到感兴趣的UE上所必须的无线资源。 
如果E-UTRAN节点接受IP多播分发，则加入MBMS GW分配的IP多播地址（包括多播源）组中， 并准备好接收MBMS数据。 
BM-SC的开始发送MBMS数据 
MBMS GW接收MBMS数据。 对所有加入多播组eNodeB，MBMS GW使用IP多播分发MBMS数据。 
会话停止
详见3GPP协议23.246的8.5.2节。 
BM-SC认为需要停止MBMS会话时，就会发起eMBMS会话停止过程。典型的情况就是一段时间内没有MBMS数据需要传输。 
会话停止流程如[图8]所示。
图8  会话停止流程

流程说明： 
BM-SC发送会话停止请求消息给MBMS GW指示会话结束和承载资源释放。 
MBMS GW发送eMBMS会话停止请求消息给会话对应的MME，释放相应的承载资源并设置承载上下文状态为Standby，释放MBMS广播承载业务的MBMS承载上下文，同时向BM-SC回响应消息。 
MME收到会话停止请求消息，向MBMS GW回复响应消息，并向相关的MCE（发送过start/update消息）转发会话停止消息。MME设置MBMS的承载上下文状态为Standby。收到所有MCE的响应（包括成功和失败），释放MBMS的承载上下文；定时器超时，释放MBMS的承载上下文。 
MCE/E-UTRAN释放被影响的资源和删除MBMS承载上下文。 
会话更新
详见3GPP协议23.246的8.8.4节。 
eMBMS会话更新过程由BM-SC触发。可以通过会话更新请求修改的属性包括：MBMS服务区，接入指示，MBMS控制平面节点列表。收到会话更新请求的节点通过比较消息中的属性与保存的对应MBMS承载上下文的属性来判断变化情况。 
会话更新流程如[图9]所示。
图9  会话更新流程

流程说明： 
在某个原因触发下，比如正在进行的MBMS会话的业务区需要修改时， BM-SC发送会话更新请求给MBMS GW，请求消息中包含（TMGI，Flow
Identifier，QoS，MBMS服务区，会话标识符（Session identifier），预估的会话持续时间，MBMS控制平面节点列表，接入指示。 
MBMS GW在MBMS承载上下文中保存新的会话属性并发送的会话更新响应消息给BM-SC。 
按照如下原则处理：向新加的MME发生启动消息，向需要删除的MME发生停止消息，向存在的MME列表发送更新消息。 
MME接收到MBMS会话更新请求消息，根据开关的状态决策是向查询到的MCE列表（start和update消息中位置区列表的并集）还是所有的MCE转发MBMS会话更新请求消息,
其中包括会话属性：TMGI， QoS，MBMS服务区，会话标识符，预估的会话持续时间，传输网络IP多播地址， 多播源地址，C-TEID等。 
如果MCE没有MBMS会话更新请求消息中TMGI对应的MBMS承载上下文，MCE创建MBMS承载上下文，否则MCE将保存在MBMS承载上下文服务区和最新的服务区进行比较，并作出相应的更新；并给MME回响应。 
MME按照如下原则处理：收到一个成功的响应，更新MBMS承载上下文属性并立即回成功的响应给MBMS GW；收到所有的失败响应或者定时器超时，回失败的响应给MBMS
GW 
MCE根据当前MBMS业务区建立和释放无线资源。 
eNodeB加入或退出IP组播。 
MBMS宕机或者重启
MBMS宕机或者重启流程如下图所示。 
MME通过echo检测MBMSGW是否正常。 
如果MBMSGW宕机，则没有echo响应；如果MBMSGW重启，则在echo响应中指示通知MME。 
MME判断出MBMSGW宕机或者重启，表示之前的会话已经失效。MME把和该MBMSGW有关的会话的找出来，然后发Session Stop Request通知MCE释放相应的会话。 
MCE释放完毕，回复Session Stop Response消息给MME。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 22.146 Multimedia Broadcast/Multicast Service(MBMS); Stage 1|_
3GPP TS 22.246 Multimedia Broadcast/Multicast Service(MBMS) user services; Stage 1|_
3GPP TS 23.246 Multimedia Broadcast/Multicast Service (MBMS);Architectureand functional description|_
3GPP TS 23.007 Restoration procedures|15A.3 MCE Failure15A.4M3AP path failure17A.1Restart of the MBMS GW
3GPP TS 26.346 Multimedia Broadcast/Multicast Service (MBMS);Protocolsand codecs|_
3GPP TS 29.274 Evolved General Packet Radio Service (GPRS)Tunnelling Protocol for Control plane (GTPv2-C); Stage 3|7.13 MBMS Messages
3GPP 36.444 M3 Application Protocol (M3AP)|_
特性能力 :名称|指标
---|---
MME支持并发MBMS会话数量|最大 4096
MME支持的MCE数量|最大2048
MME支持一个MCE可服务的MBMS Service Area个数|最大256
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License“MME支持eMBMS功能”许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持eMBMS功能”（license ID：7024），此项目显示为“支持”，表示MME支持eMBMS功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|-|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :软件参数 
新增软件参数参见[表1]。
软件参数ID|软件参数名称
---|---
65601|MME支持ARP参数
65852|MME是否支持eMBMS功能
性能统计 :该特性不涉及计数器的变化 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :执行[SHOW ALL MCE LINKS]命令在MCE管理中查询全部MCE连接。
执行[SHOW MCE LINKS]命令在MCE管理中查询单个MCE连接。
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :配置M3AP静态偶联或者动态偶联。只要配置一种就行了。 
配置M3AP静态偶联使用ADD SCTP命令增加M3AP静态偶联。M3AP偶联的上层协议采用M3AP，底层承载在SCTP协议上。 
配置M3AP动态偶联使用ADD SCTP命令增加M3AP动态偶联，当需要使用新的动态偶联传输M3AP协议数据时，使用该命令。M3AP动态偶联新增成功后，可以通过SHOW SCTP查询到该偶联配置。 
设置“MME支持ARP参数”和“MME是否支持eMBMS功能”软参为支持。
配置前提 :eMBMS功能需要License支持，对应的License项为：“MME支持eMBMS功能”。 
该配置的数据准备：静态偶联本端IP地址、本端端口、对端IP地址、对端端口等四个参数用于唯一标识一个SCTP偶联。配置M3AP偶联时应遵循以下配置原则：本端IP地址、本端端口、对端IP地址、对端端口属于SCTP协议的对接数据，需要双方协商一致。当本端IP地址与对端IP地址被确定以后，两信令设备之间的链路将由本端端口与对端端口两个参数组合确定。如果各偶联所使用的对端端口号相同，则本端端口号不能相同，反之亦然。建议划分端口号段，并分配给不同的SCTP用户（如：M2UA、M3UA和M3AP等）。例如，M2UA链路的SCTP端口号段3000～4000，M3UA链路的SCTP端口号段4001～5000，M3AP链路的SCTP端口号段9001～10000。这样可以避免不同链路类型使用相同SCTP端口。动态偶联本端IP地址、本端端口用于唯一标识一个M3AP动态偶联。 
配置过程 :配置M3AP静态偶联或者动态偶联。只要配置一种。 
配置M3AP静态偶联使用ADD SCTP命令新增M3AP静态偶联
。 
配置M3AP动态偶联使用ADD SCTP命令新增M3AP动态偶联。 
使用[SET SOFTWARE PARAMETER]命令设置软参“MME支持ARP参数”的值，一般为默认值。
使用[SET SOFTWARE PARAMETER]命令设置软参“MME支持eMBMS消息的能力”的值，一般为默认值。
配置实例 :###### 静态偶联连接方式 
数据规划
一个MCE配置一条静态偶联。 
根据假设的场景，数据规划参见下表。 
名称|模块|应用属性|本端IP|本端端口|对端IP|对端端口|SCTP标识
---|---|---|---|---|---|---|---
MCE3605|2|客户端|192.20.107.3|49605|192.20.182.122|49605|3605
MCE3606|3|客户端|192.20.107.3|49606|192.20.182.123|49606|3606
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置MCE3605的静态偶联|ADD SCTP:ID=3605,NAME="MME3605",ROLE="CLT",VPNID1=2,LOCADDR1="192.20.107.3",LOCPORT=49605,REMADDR1="192.20.182.122",REMPORT=49605,PROTOCALTYPE="M3AP"ADD SCTPIDCFG:SCTPID=3605,TYPE="M3AP"
2|配置MCE3606的静态偶联|ADD SCTP:ID=3606,NAME="MME3606",ROLE="CLT",VPNID1=2,LOCADDR1="192.20.107.3",LOCPORT=49606,REMADDR1="192.20.182.123",REMPORT=49606,PROTOCALTYPE="M3AP"ADD SCTPIDCFG:SCTPID=3606,TYPE="M3AP"
3|数据同步|SYNA
###### 动态偶联连接方式 
场景说明
对接MCE时，一般配置动态偶联。 
数据规划
一个MCE配置一条静态偶联。 
根据假设的场景，MME数据规划参见下表。 
名称|本端IP|本端端口|SCTP ID
---|---|---|---
MME7|192.0.100.7|49608|3805
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置MME侧动态偶联数据|ADD SCTP:ID=3805,NAME="MME7",VPNID1=2,LOCADDR1="192.0.100.7",LOCPORT=49608,PROTOCALTYPE="M3AP"ADD SCTPIDCFG:SCTPID=3805,TYPE="M3AP"
2|数据同步|SYNA
测试用例 :测试项目|MBMS-GW发起会话
测试目的|MME收到MBMS GW的会话开始消息的处理。
预置条件|EPS网络中各网元系统及操作维护台运行正常。MCE已经在MME中注册。
测试过程|MBMS GW向MME发起会话，发送MBMS Session Start Request消息。
通过准则|MME对MBMS Session Start Request消息中的服务区和注册的MCE的服务区进行匹配，如果匹配成功，MME向MCE发送MBMSSESSION START REQUEST。MME收到MCE的MBMS Session Start RESPONSE消息后向MBMS GW返回MBMS SessionStart Response消息。
测试结果|
测试项目|MBMS-GW发起会话修改。
测试目的|MME收到MBMS GW的会话修改消息的处理。
预置条件|EPS网络中各网元系统及操作维护台运行正常。MCE已经在MME中注册。
测试过程|MBMS GW向MME发起会话修改，发送MBMS Session Update Request消息。
通过准则|MME根据MBMS Session Start REQUEST和MBMS Session Update Request消息服务区匹配相同的MCE并向该MCE发送MBMSSESSION Update Request。MME收到MCE的MBMS Session Update RESPONSE消息后向MBMS GW返回MBMS SessionUpdate Response消息。
测试结果|
测试项目|MBMS-GW发起会话结束。
测试目的|MME收到MBMS GW的会话结束消息的处理。
预置条件|EPS网络中各网元系统及操作维护台运行正常。MCE已经在MME中注册。
测试过程|MBMS GW向MME发起会话结束，发送MBMS Session Stop Request消息。
通过准则|MME收到MBMS Session Stop Request消息后向MBMS GW回复MBMS Session StopResponse。MME向MCE发送MBMS SESSION STOP REQUEST消息停止会话。
测试结果|
## ZUF-78-15-007 分权分域 
特性描述 :特性描述 :术语 :术语|含义
---|---
域|资源的集合，每种资源的任何一个实例可以属于某个域，也可以不属于域，属于非域资源。但每种资源的任何一个实例都不能同时属于多个域。
分权|指对用户的操作权限进行授权，控制用户只能执行哪些命令或操作集。
分域|指用户能管理和操作的资源范围，一般运营商都是按设备节点或地域范围来划分用户的管理范围。
描述 :定义 :分权分域功能是网管系统的安全管理功能的主要构成部分，主要分为分权和分域两部分功能。 
分权：指对用户的操作权限进行授权，控制用户只能执行哪些命令或操作集。限定用户只对一定区域的某些内容执行允许的操作，以保证网管系统的操作安全。分权是在分域条件下的权限控制行为，一般按设备节点或区域设置用户帐号，用户账号一般只能属于一个区域，该用户授予的操作权限只在所属区域有效，不能管理其他区域。也可以根据运营商的组织体系和管理需要，某些特殊用户也可以设置为管理所有或多个区域。 
分域：指用户能管理和操作的资源范围，一般运营商都是按设备节点或地域范围来划分用户的管理范围。 
背景知识 :随着网络的发展，单网元能力的提高，在实际的部署中，一个MME控制的区域越来越大，有的时候一个MME同时兼具多个本地网的业务部署和开展。从而带来新的问题：对于各个本地网需要分开控制和管理。包括：
需要对网络进行分权限管理，即不同的管理人员有不同的管理权限，如每个本地网的管理人员只能控制其对应的本地网。 
需要对网络分区域监控，即各个本地网络可以独立监控，如各个本地网络有着本身的性能统计。 
为了解决大本地网组网引出新问题，引入了域概念，一个物理的MME分成多个逻辑的域，域完成各自虚拟区域的业务控制功能。 
如[图1]所示，3个本地网，承接该本地网的话务，在网络规划时可以把MME虚拟成3个域，一个域对应一个本地网。从网络运维角度来看，就需要实现分权分域管理功能，要求能按域为管理粒度进行权限分配和操作维护，各本地网的维护人员只具有其对应域部分的操作权限，只能够操作和维护自己本地网的网络，同时每个本地网都有各自独立的统计指标，各个本地网的维护人员只能看到相应的本地网统计数据。对于大本地网中心的管理人员，则可以具有整个MME网元的操作权限，负责管理和维护整个MME。
图1  把MME虚拟成3个域

应用场景 :###### 划分地域 
系统管理人员需要根据实际地域划分多个域，并为每个域分配域ID，并为每个域分配域所管理的资源。目前MME支持基于TA进行地域的划分。 
###### 划分权限 
系统管理人员对每个域分配不同的操作员，以及相应的权限。每个操作员只能操作和查看本域的数据。 
###### 域性能指标 
操作维护人员针对各个域的要求，激活需要监控的域性能统计指标。系统会定时上报相应的统计数据。 
客户收益 :受益方|受益描述
---|---
运营商|管理不同的维护操作人员划分不同的权限，便于管理。通过各个域的性能数据监控各本地网的运维情况。
实现原理 :涉及的网元 :网元名称|网元作用
---|---
EMS|支持分权。支持分域。支持基于域的性能统计，并支持在POOL组网时，合并各个域的性能统计统计数据。
本网元实现 :对于分权的流程，在EMS进行处理：配置域ID，并对操作人员进行权限的分配。 
对于分域的流程，系统内部实现如[图2]所示。
图2  分域的流程
EMS下发域的性能统计任务给MME 
MME把域的性能统计数据上报给EMS 
业务流程 :分权分域功能的业务流程，有以下2种：域性能统计任务激活以及域性能统计任务去活。 
域性能统计任务激活
域性能统计任务激活流程如[图3]所示。
图3  域性能统计任务激活

流程说明： 
EM激活对应域的性能统计任务，并下发给MME。
MME开始统计相应域的数据，并定时上报给EM。 
域性能统计任务去活
域性能统计任务去活流程如[图4]所示。
图4  域性能统计任务去活

EM去激活对应域的性能统计任务，并下发给MME。MME停止相应域的数据统计和上报。 
系统影响 :开启分权分域功能后，对系统的影响在于性能统计数据的上报数量，并随着域数量的增加而增加。 
对域的个数以及域的性能统计项的数目的指标有影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :该特性不涉及与公共协议的遵循标准。 
特性能力 :名称|指标
---|---
最大支持域的数量|32
最大支持操作人员|100
可获得性 :License要求 :本特性不受license控制。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS|EMS
---|---|---|---|---|---
-|-|-|-|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :新增命令配置项参见[表1]。
配置项|命令
---|---
分域配置|SET ASSIGNAREA SPRT
SHOW ASSIGNAREA SPRT|分域配置
地域配置|ADD AREA
SETAREA|地域配置
DEL AREA|地域配置
SHOW AREA|地域配置
资源分段配置|ADD RES
SET RES|资源分段配置
DEL RES|资源分段配置
SHOW RES|资源分段配置
角色授权地域配置|ADD ROLEAREA
DEL ROLEAREA|角色授权地域配置
SHOW ROLEAREA|角色授权地域配置
性能统计 :新增性能计数器参见[表2]。
测量类型|描述
---|---
基于域附着流程测量|编号为45000开头的所有计数器
基于域跟踪区更新流程测量|编号为45001开头的所有计数器
基于域业务请求流程测量|编号为45002开头的所有计数器
基于域去附着流程测量|编号为45003开头的所有计数器
基于域寻呼流程测量|编号为45004开头的所有计数器
基于域EMM通用流程测量|编号为45005开头的所有计数器
基于域承载激活流程测量|编号为45006开头的所有计数器
基于域承载修改流程测量|编号为45007开头的所有计数器
基于域承载去激活流程测量|编号为45008开头的所有计数器
基于域UE请求承载资源流程测量|编号为45009开头的所有计数器
基于域切换流程测量|编号为45010开头的所有计数器
基于域用户数测量|编号为45100开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME支持分权分域功能，需要对分权分域进行配置。 
配置前提 :EMS版本支持分权分域功能。 
地域规划准备：规划好需要划分的地域，以及如何将跟踪区归类为不同的地域。并对每个域分配不同的操作员，以及相应的权限。 
配置过程 :在OMM网管中配置分权分域配置。 
使用SET ASSIGNAREA SPRT命令设置支持分权分域。 
使用ADD AREA命令设置地域。 
使用ADD RES命令进行地域的资源分段配置。 
使用ADD ROLEAREA命令将规划好的地域授权给相关用户的角色。 
在EMS上创建角色和用户，并设置对地域1和地域2具有系统维护权限。 
在EMS上设置域性能指标监控。 
配置实例 :###### 划分地域 
实例场景
根据应用场景，根据实际地域划分多个域，并分配域ID，为每个域分配域所管理的资源。 
配置脚本
设置支持分权分域功能。 
SET ASSIGNAREA SPRT:ISASSIGNAREA="YES" 
增加地域，设置其地域编号和地域名称，地域编号可设置为1-65535之间的数值，地域名称建议设置为实际地域的缩写，比如NJ。 
ADD AREA:AREAID=1,AREANAME="NJ" 
###### 划分权限 
实例场景
根据应用场景，在EMS上对每个域分配不同的角色以及相应的权限。每个角色对应的用户只能新增、删除或者修改本域的数据。 
前提
EMS已开启集中安全，集中安全开启方法可参考EMS相关操作指导文档。 
uMAC网元侧已配置了地域资源，比如已配置了：地域NJ（1）、地域SZ（2）和地域WX（3）。 
过程
在EMS创建角色，对地域1和地域2具有系统维护权限。 
打开EMS客户端，选择菜单安全→角色管理
，打开角色管理窗口。
在左边导航树中，右击角色，选择快捷菜单新建角色，打开如[图1]所示的窗口。
图1  EMS创建角色

创建新角色，比如“test”。资源列表中将呈现当前已配置的地域。为该角色赋予NJ（1）和SZ（2）的系统维护权限，对WX（3）设置为无权限。 
单击确定按钮，完成角色的创建。
在EMS创建用户，对地域1和地域2具有系统维护权限。 
选择菜单安全→用户管理
，打开用户管理窗口。
在左边导航树中，右击根部门，在快捷菜单中选择新建用户，打开创建用户的窗口，如[图2]所示。
图2  创建用户

创建一新用户比如“test”，配置基本信息后，在权限设置页面，角色选择“test”。 
单击确定按钮，创建成功。则用户test只对地域1和地域2有维护权限。
###### 域性能指标监控 
实例场景-划分权限
激活需要监控的域性能统计指标。系统会定时上报相应的统计数据。 
过程
在EMS的性能管理中，新建域的测量任务。在任务管理中创建基于域的性能测量任务，如[图3]所示。
图3  创建基于地域的性能统计任务

在位置选择页面中，通配层次设置为选择到网元，并设置对应的网元，如[图4]所示。
图4  设置任务的通配层次

在基本信息页面中，粒度建议设置为1小时,，如[图5]所示。
图5  任务粒度设置为1小时

单击确定按钮。任务建立完成后，在粒度上报后，可查询到相关统计数据。
测试用例 :测试项目|划分地域
测试目的|验证划分地域功能无异常。
预置条件|OMM和前台运行正常。
测试过程|打开MML命令终端。添加地域，例如执行命令：ADD RES:AREAID=1,PREFIX="46003",BEGINVALUE="0010",ENDVALUE="0015"为地域分配资源段，例如执行命令：ADD AREA:AREAID=1,AREANAME="NJ"
通过准则|命令执行成功，并产生变化表，数据可成功同步到前台。性能统计可成功获取地域的测量对象。
测试结果|
测试项目|划分分域权限
测试目的|验证划分分域权限功能。
预置条件|OMM和前台运行正常。OMM和EMS对接正常。
测试过程|当前已配置地域，比如地域1、2、3。EMS已开启集中安全。在EMS安全管理中创建角色test，赋予系统维护权限，资源分配地域1和2的权限。比如已创建用户test，其角色设置为test。用户test登录系统后，检查该用户只可以对地域1和2包含的TA资源进行相关的增、删、修改操作，对地域1和2之外的资源没有增删改权限。
通过准则|操作执行成功，用户test只可以以对地域1和2包含的TA资源进行相关的增、删、修改操作，对地域1和2之外的资源没有增删改权限。
测试结果|
测试项目|域性能指标监控
测试目的|验证域性能指标监控功能。
预置条件|OMM和前台运行正常。当前已配置了地域，并划分了相关资源。
测试过程|在性能统计中创建基于域的测量任务，比如创建基于域附着流程测量任务。构造用户附着流程，检查统计粒度到达后，该测量类型的任务可正常上报数据，统计与实际一致。
通过准则|该测量类型的任务可正常上报数据，统计与实际一致。
测试结果|
常见问题处理 :分权分域的配置数据分别存放在配置库、性能库和安全库中，若备份分权分域的数据，需要将配置、性能统计和安全数据一起备份： 
1025 性能数据 
1026 安全数据 
1400000 基本配置数据 
对应命令： 
[BACKUP]:OUTPUTPATH="/home/backup",FILENAME="backup_area",SETID=1025&1026&1400000;
在恢复数据时，也需要三者一起恢复： 
[RESTORE]:FILENAME="/home/backup/backup_area.zip",SETID=1025&1026&1400000;
若全新安装了OMM服务端，需要恢复分权分域的数据。如果之前只备份了配置数据，在恢复数据后，则需要手工执行命令SET ASSIGNAREA SPRT:ISASSIGNAREA="YES" 开启分域的功能。对于权限数据，若对接了EMS，并且EMS开启了集中安全，则需要EMS重新下发下集中安全数据。 
## ZUF-78-15-008 信令风暴抑制 
特性描述 :特性描述 :术语 :术语|定义
---|---
信令风暴|由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至产生雪崩效应，导致网络不可用，这就是信令风暴。
Fake APN|假APN，该APN不在HSS签约，而是在MME本地配置。EPS网络用Fake APN为用户建立假的PDN连接，网络可以成功建立FakeAPN PDN连接，但用户使用此PDN连接无法上网。当用户终端信令请求对网络造成冲击时，EPS网络会拒绝终端信令请求，终端就会重发信令请求，此时建立FakeAPN PDN连接可以防止终端不停的重发信令请求，减轻网络信令负荷。
描述 :定义 :信令风暴抑制：是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
MME信令风暴抑制是用户级的抑制，针对终端发起的三种信令进行抑制，包括附着请求信令抑制、业务请求信令抑制和PDN连接请求信令抑制。 
背景知识 :引发信令风暴的原因有很多，主要包括如下原因： 
特殊事件：由于集会、节日、传输中断等导致短时间内大量用户发起业务，带来的信令冲击超过网络的处理能力。 
LTE核心网的设备故障、重启或用户卸载等场景触发大量用户同时重新连接网络，触发信令风暴。 
终端问题：因下述原因，终端业务连续失败后，终端会不断重发信令请求，附着请求/业务请求/PDN连接请求频繁发生。当一定时间内信令请求数很多，即将超过网络信令资源的处理能力，就会触发信令风暴。终端APN或其他参数错误终端中毒终端恶意攻击网络传输中断区域限制业务服务器Down其他原因 
不同原因导致的信令风暴，其抑制手段也不同： 
特殊事件：MME启用智能过负荷控制，保证发生信令风暴时正常服务。 
设备故障：MME启用智能过负荷控制，保证发生信令风暴时正常服务。 
终端问题：MME对附着请求/业务请求/PDN连接请求信令进行信令黑名单控制，避免网络拥塞，化解信令风暴。 
应用场景 :###### 总述 
本特性是对终端用户的三种信令引发的风暴进行识别和抑制，如[图1]所示，包括附着请求信令风暴的识别和抑制、业务请求信令风暴的识别和抑制、PDN连接请求信令风暴的识别和抑制。
图1  信令风暴的识别和抑制

###### 频繁的信令请求引发的信令风暴识别 
因终端/用户问题（参数错误、中毒、恶意攻击网络）或传输中断、区域限制等原因，导致在一定时间内，终端的附着请求/业务请求/PDN连接请求信令，多到影响网络信令资源的处理能力，MME需要进行信令风暴识别。 
MME统计单个终端在统计周期内产生的信令数：附着、业务请求和PDN连接请求信令分开统计，当统计周期内的信令总数超过门限值，则将该用户放入信令黑名单，启动用户信令黑名单管理时长。 
###### 频繁的信令请求引发的信令风暴抑制 
因终端/用户问题（参数错误、中毒、恶意攻击网络）或传输中断、区域限制等原因，导致在一定时间内，终端的附着请求/业务请求/PDN连接请求信令，多到影响网络信令资源的处理能力，MME识别出附着请求/业务请求/PDN连接请求信令风暴，就需要进行信令风暴抑制，避免部分信令异常终端影响网络。 
在用户信令黑名单管理时间内，对附着请求和PDN连接请求信令异常的终端，有四种手段抑制信令： 
拒绝接入请求：对于附着请求，MME发送Attach Reject消息给UE，其中携带附着拒绝原因值7-EPS service
not allowed；对于PDN连接请求，MME发送PDN Connectivity Reject消息给UE，其中携带PDN连接拒绝原因值55-Multiple
PDN connections not allowed。 
建立Fake APN PDN连接：MME给SGW发送Create Session Request消息。 
强制去附着：MME发送Detach Request消息给UE，其中携带的detach type为re-attach not
required。 
丢弃后续请求：MME丢弃后续收到的Attach Request消息。 
在用户信令黑名单管理时间内，对业务请求信令异常的终端，有三种手段抑制信令： 
拒绝业务请求：MME发送Service Reject消息给UE，其中携带拒绝原因值7-EPS service not
allowed。 
强制去附着：MME发送Detach Request消息给UE，其中携带的detach type为re-attach not
required。 
丢弃后续请求：MME丢弃后续收到的Service Request消息。 
用户信令黑名单管理时长到达后，用户从信令黑名单移除，可以正常上网。 
客户收益 :受益方|受益描述
---|---
运营商|确保网络设备安全运行：减轻网络信令压力，化解信令风暴，避免网络拥塞。提高用户满意度：保障用户使用数据业务和业务的成功率，从而提高用户满意度，增加收益。提升运营商KPI指标：抑制终端频繁发起信令请求导致的业务失败，提升了业务成功率。
移动用户|用户享受更稳定和更可靠的网络服务。
实现原理 :系统架构 :系统架构如[图2]所示。
图2  系统架构

涉及的网元 :信令风暴抑制由MME和GW配合完成，具体参见[表1]。
网元|功能
---|---
MME|MME信令风暴抑制，具体包括附着请求信令风暴抑制、业务请求信令风暴抑制和PDN连接请求信令风暴抑制。MME在各信令的每个统计周期内统计各信令数，如果统计的信令数大于最大信令数，则MME将用户加入信令黑名单，并启动黑名单定时器。在信令黑名单定时器管理时间内，MME拒绝或丢弃信令；或MME建立FAKEAPN PDN连接，用户使用此PDN连接无法上网。信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。
SGW/PGW|SGW/PGW支持FAKE APN PDN连接建立，用户使用此PDN连接无法上网。
本网元实现 :附着信令风暴抑制MME在附着信令单位统计周期内统计附着信令数，如果统计的附着信令数大于最大信令数，则MME将用户加入附着信令黑名单，并启动附着黑名单定时器。在附着信令黑名单定时器管理时间内，UE不断发起附着，MME进行如下处理：拒绝接入请求。建立Fake APN PDN连接。强制去附着。丢弃后续请求。附着信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
业务请求信令风暴抑制MME在业务请求信令单位统计周期内统计业务请求信令数，如果统计的业务请求信令数大于最大信令数，则MME将用户加入业务请求信令黑名单，并启动业务请求黑名单定时器。在业务请求信令黑名单定时器管理时间内，UE不断发起业务请求，MME进行如下处理：拒绝业务请求。强制去附着。丢弃后续请求。业务请求信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
PDN连接请求信令风暴抑制MME在PDN连接信令单位统计周期内统计附着信令数，如果统计的PDN连接信令数大于最大信令数，则MME将用户加入PDN连接信令黑名单，并启动PDN连接信令黑名单定时器。在PDN连接信令黑名单定时器管理时间内，UE不断发起PDN连接请求，MME进行如下处理：拒绝接入请求。建立Fake APN PDN连接。强制去附着。丢弃后续请求。PDN连接信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
业务流程 :附着请求信令抑制
附着请求信令抑制流程参见[图3]。
图3  附着请求信令抑制流程

附着请求信令抑制流程描述如下： 
UE发起附着请求。MME针对每个UE进行统计，记录统计周期T1内收到该UE的附着请求信令数。 
MME因终端参数错误、区域限制等原因，给UE返回附着拒绝。 
UE重发附着请求。MME针对每个UE进行统计，记录统计周期T1内收到该UE的附着请求信令数。 
MME因终端参数错误、区域限制等原因，给UE返回附着拒绝。 
UE多次重发附着请求。MME针对每个UE进行统计，记录统计周期T1内收到该UE的附着请求信令数。 
当UE在统计周期内的信令数没超过门限值N1时，MME按照正常流程处理该用户信令。当UE在统计周期内的信令数超过门限值N1时，MME对该用户的异常信令进行控制：MME将该用户加入黑名单，并给终端下发Attach
Reject消息，消息中携带原因值为7-EPS service not allowed（原因值可配置），并启动黑名单定时器TT1。如果直到TT1超时仍未收到Attach
Request消息，则将用户从黑名单移除，正常处理后续消息。 
如果在TT1超时前，UE继续发送Attach Request消息，则进入步骤8。 
网络对用户进行鉴权，观察用户是否能鉴权成功。 
是→步骤9 
否→步骤15 
EPS网络以fake APN让终端建立PDN连接成功，MME发送Create
Session Request消息给SGW，消息中携带fake APN。 
SGW发送Create Session Request消息给PGW，消息中携带fake APN。 
PGW返回Create Session Response消息给SGW。 
SGW返回Create Session Response消息给MME。 
MME返回附着接受给UE。 
（可选）如果直到TT1超时仍未收到Attach Request消息，MME则将用户从黑名单移除，并给UE发送Detach
Request消息，其中detach type为re-attach required。UE re-attach时使用正常APN。 
（可选）如果鉴权失败或在TT1超时前UE继续发送Detach Request/Attach Request消息，MME则给UE发送Detach
Request消息，其中detach type为re-attach not required。 
（可选）如果直到TT1超时仍未收到Attach Request消息，则将用户从黑名单移除，正常处理后续消息。如果在TT1超时前继续收到UE发送的Attach
Request消息，MME丢弃该用户的附着请求信令，对这部分丢弃的信令单独统计，待黑名单TT1超时后，再将用户从黑名单移除。 
业务请求信令抑制
业务请求信令抑制流程参见[图4]。
图4  业务请求信令抑制流程

业务请求信令抑制流程描述如下： 
UE发起业务请求。MME针对每个UE进行统计，记录统计周期T2内收到该UE的Service Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回业务请求拒绝。 
UE重发业务请求。MME针对每个UE进行统计，记录统计周期T2内收到该UE的Service Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回业务请求拒绝。 
UE多次重发业务请求。MME针对每个UE进行统计，记录统计周期T2内收到该UE的Service Request信令数。 
当UE在统计周期内的信令数没超过门限值N2时，MME按照正常流程处理该用户信令。当UE在统计周期内的信令数超过门限值N2时，MME对该用户的异常信令进行控制：MME将该用户加入黑名单，并给终端下发Service
Reject消息，消息中携带原因值为7-EPS service not allowed（原因值可配置），并启动黑名单定时器TT2。如果直到TT2超时仍未收到Service
Request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT2超时前，UE继续发送Service Request消息，则进入步骤8。 
（可选）MME给UE发送Detach Request消息，其中detach type为re-attach not required。如果直到TT2超时仍未收到Attach
Request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT2超时前，UE继续发送Attach Request消息。MME丢弃该用户的附着请求信令，对这部分丢弃的信令单独统计，黑名单TT2超时后，再将用户从黑名单移除。 
PDN连接请求信令抑制
PDN连接请求信令抑制流程参见[图5]。
图5  PDN连接请求信令抑制流程

UE发起PDN连接请求。MME针对每个UE进行统计，记录统计周期T3内收到该UE的PDN Connectivity Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回PDN连接请求拒绝。 
UE重发PDN连接请求。MME针对每个UE进行统计，记录统计周期T3内收到该UE的PDN Connectivity Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回PDN连接请求拒绝。 
UE多次重发PDN连接请求。MME针对每个UE进行统计，记录统计周期T3内收到该UE的PDN Connectivity
Request信令数（不包含Attach流程中的PDN Connectivity Request）。 
当UE在统计周期内的信令数没超过门限值N3时，MME按照正常流程处理该用户信令。当UE在统计周期内的信令数超过门限值N3时，MME对该用户的异常信令进行控制：MME将该用户加入黑名单，并给终端下发PDN
Connectivity Reject消息，消息中携带原因值为55-Multiple PDN connections not allowed（原因值可配置），并启动黑名单定时器TT3。如果直到TT3超时仍未收到PDN
Connectivity Request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT3超时前，UE继续发送PDN Connectivity Request消息，则进入步骤8。 
EPS网络以fake APN让终端建立PDN连接成功，MME发送Create
Session Request消息给SGW，消息中携带fake APN。 
SGW发送Create Session Request消息给PGW，消息中携带fake APN。 
PGW返回Create Session Response消息给SGW。 
SGW返回Create Session Response消息给MME。 
MME返回PDN连接请求接受给UE。如果直到TT3超时仍未收到PDN Connectivity Request消息，MME则将用户从黑名单移除。UE再发起PDN Connectivity Request时使用正常APN。 
如果在TT3超时前，UE继续发送PDN Connectivity Request消息，MME给UE发送Detach Request消息，其中detach type为re-attach not required。如果直到TT3超时仍未收到Attach
request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT3超时前，UE继续发送Attach Request消息。MME丢弃该用户的附着请求信令，对这部分丢弃的信令单独统计，黑名单TT3超时后，再将用户从黑名单移除。 
系统影响 :MME支持信令风暴抑制，减少了网络侧要处理的信令，信令抑制的功效是提高系统处理性能。 
应用限制 :该特性不涉及应用限制。 
特性交互 :特性|交互
---|---
紧急呼叫|如果附着请求、业务请求或PDN连接请求信令进入黑名单，MME对紧急呼叫放行，允许信令黑名单用户拨打紧急呼叫。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "GPRS enhancements for E-UTRAN access"|5.3.2节: Attach procedure5.3.4节: Service Request procedures5.10.2节: UE requested PDN connectivity
特性能力 :类型|能力
---|---
附着请求/业务请求/PDN连接请求信令统计周期|1-65535，单位：秒，默认值为。
附着请求/业务请求/PDN连接请求黑名单定时器时长|1-65535，单位：秒，默认值为。
黑名单用户容量|数量等同于MM上下文配置容量。
MME附着、业务请求和PDN连接请求信令统计的周期默认值都设置为12分钟，依据是24.301协议上对终端的要求是12分钟最多6次（5次重发），附着、业务请求和PDN连接请求黑名单定时器时长默认值都设置为20分钟，原则是比各信令统计周期略长，各信令单位时间内的信令门限的默认值设置原则参见下表。 
信令类型|信令统计周期|MME话务模型events/ peak SAU @BH（忙时每小时）|信令门限值
---|---|---|---
附着请求|12分钟|理论值：0.3现网经验值：0.2~0.4|话务模型中附着次数太小，24.301协议上对终端的要求是12分钟最多6次（5次重发），而附着成功建立的时长是毫秒级或秒级，因此设置为5的3倍，即15次。
业务请求|12分钟|理论值：6现网经验值：25左右|以现网经验值为准乘6的系数，即30次。
PDN连接请求|12分钟|无|考虑多PDN连接和IMS语音，比附着次数略小，即10次。
可获得性 :License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持信令风暴抑制”（license ID：7036），此项目显示为“支持”，表示MME支持信令风暴抑制功能。
对其他网元的要求 :SGW/PGW需支持FAKE APN PDN连接建立，控制用户使用此PDN连接无法上网。 
工程规划要求 :Fake APN需要全网规划。 
O&M相关 :命令 :配置项表2  新增配置项配置项命令MME信令风暴抑制配置SET SIGSRESTRAIN FLAGSHOW SIGSRESTRAIN FLAGSET SIGSRESTRAINSHOW SIGSRESTRAIN 
软件参数表3  新增软件参数软件参数ID软件参数名称262398MME隐式分离信令黑名单空闲态用户 
动态管理在“动态管理”下增加“MME信令风暴抑制管理”，具体参见下表。功能命令查询单用户信令状态SHOW SUBSCRIBER SIGSTATUS用户移出信令黑名单MOVE SUBSCRIBER BLACK查询信令黑名单用户SHOW BLACK SUBSCRIBER 
性能统计 :测量类型|描述
---|---
承载激活流程测量|编号为C430070037至C430070079的所有计数器。
信令风暴抑制流程测量|编号为C464350001至C464350011的所有计数器。
信令风暴抑制用户数测量|编号为C464360001至C464360006的所有计数器。
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性涉及的业务观察/失败观察，参见下表。 
失败原因码及名称|相关模块|波及业务|产生原因|处理建议
---|---|---|---|---
Signaling Stome Restrain Control Failed In Attach Proc（591）因信令风暴抑制控制使附着请求失败|Emm|附着|用户因频繁的附着进入附着信令黑名单，导致MME拒绝附着接入请求。|无需处理
Signaling Stome Restrain Control Failed In Service RequestProc(592)因信令风暴抑制控制使业务请求失败|Emm|业务请求|用户因频繁的业务请求进入业务请求信令黑名单，导致MME拒绝业务请求。|无需处理
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置信令风暴抑制功能，能够确保网络设备安全运行，减轻网络信令压力，化解信令风暴，避免网络拥塞。 
配置前提 :对于信令风暴抑制功能，ZTE根据经验，提供了各项门限值的经验数据。但是各地网络均有其话务模型的独特性，需要运营商和ZTE预先评估各项黑名单门限预设值是否需要修改。用户还需要预先规划Fake
APN。 
配置过程 :执行命令[SET SIGSRESTRAIN FLAG]，打开“MME支持信令风暴抑制”功能开关。
执行命令[SET SIGSRESTRAIN]，根据全网规划配置Fake APN名称。
执行命令[ADD EPC APN]，配置本地APN解析。Fake APN建议通过本地配置进行解析，而不是通过DNS进行解析。
（可选）执行命令[SET SIGSRESTRAIN]，根据各地实际话务模型，调整MME支持信令风暴抑制功能的各项门限值。
 说明： 
MME支持信令风暴抑制功能的门限默认值能够适应大多数地区的话务模型，如果运营范围内话务模型特殊，可以根据当地情况，酌情调整。 
配置实例 :MME支持信令风暴抑制功能，相关数据规划参见[表1]。
参数名称|取值举例
---|---
MME是否支持信令风暴抑制配置|MME支持信令风暴抑制|支持
MME信令风暴抑制配置|FAKE APN名称|zte.com
EPC APN HOST配置|APN名称|zte.com.apn.epc.mnc003.mcc460.3gppnetwork.org
主机名|EPC APN HOST配置|xgw
IP地址|EPC APN HOST配置|1.1.1.1
支持服务类别|EPC APN HOST配置|x-3gpp-pgw
支持协议类型|EPC APN HOST配置|x-s5-gtp & x-s8-gtp
配置脚本如下： 
打开“MME支持信令风暴抑制”功能开关。 
[SET SIGSRESTRAIN FLAG]:FLAG="YES"
配置Fake APN名称。 
[SET SIGSRESTRAIN]:FAKEAPN="zte.com"
配置对Fake APN的本地解析。将zte.com在本地进行解析，不建议通过DNS解析。 
[ADD EPC APN]:APN="zte.com.apn.epc.mnc003.mcc460.3gppnetwork.org",HOST="xgw",
IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"
调整特性 :不同运营范围的用户话务模型存在差异，如需调整信令统计周期和信令门限值，可参考以下配置示例。 
例如：修改附着请求信令统计周期为30分钟，附着请求最大信令数为50，附着请求黑名单定时器时长为30分钟。 
[SET SIGSRESTRAIN]:ATTSTATISPERD=1800,ATTMAXSIGNUM=50,ATTBLACKLISTDUR=1800;
业务请求和PDN连接请求信令抑制的调整方法与上述方法类似。 
测试用例 :测试项目|附着请求信令风暴抑制
测试目的|测试附着请求信令风暴抑制功能。
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME网元信令风暴抑制功能的license授权，并更新了license。
测试过程|开启信令风暴抑制功能开关，根据全网规划配置Fake APN。修改“附着请求最大信令数”参数为2。打开信令跟踪。用户连续发起6次Attach Request（6次附着请求在一个信令统计周期内）。等待10分钟后，查询用户黑名单状态。
通过准则|前两次Attach成功。第三次Attach失败，拒绝原因是“EPS service not allowed”，使用动态管理命令查询，用户被加入信令黑名单。第四次Attach成功，网络侧以Fake APN为用户建立PDN连接。第五次Attach时，网络侧发起Detach流程，Detach成功。第六次Attach时，用户消息被直接丢弃，不会触发后续流程。10分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|
常见问题处理 :问题描述|解决方法
---|---
信令风暴抑制不生效|检查是否打开License“MME支持信令风暴抑制”。检查是否打开配置开关“MME支持信令风暴抑制”。检查信令风暴的统计周期、信令门限是否设置，设置值是否合理。检查动态表R_MMESIGSRESTRAIN是否满容，如果满容，则需要现网扩容。
个别特殊用户没法在黑名单周期内移除黑名单|请使用动态命令MOVE SUBSCRIBER BLACK将此用户移除信令抑制黑名单控制。
## ZUF-78-15-009 PDN类型IPV6和双栈 
概述 :IPv6是下一代因特网协议，用于弥补IPv4地址的不足。3GPP选择了把IPv6作为分配给用户终端的一种地址。MME支持传递移动终端附着到IPv6/IPv4
PDN网络的请求和IPv6/IPv4类型的承载激活请求。 
### 优势 
从IPv4演进到IPv6是技术和市场的必经之路。支持用户IPv6请求可以在现在和将来为运营商带了更多的机会。 
描述 :IPv6是下一代因特网协议，用于弥补IPv4地址的不足。3GPP选择了把IPv6作为分配给用户终端的一种地址。MME支持传递移动终端附着到IPv6/IPv4
PDN网络的请求和IPv6/IPv4类型的承载激活请求。 
MME支持IPv4、IPv6或IPv4/IPv6双栈用户终端地址。MME根据用户终端所请求的PDN类型和所签约的PDN类型进行协商。 
## ZUF-78-15-010 原因值可配置 
概述 :用户终端向MME发送附着或跟踪区更新请求或者业务请求。MME拒绝用户接入，并根据运营商策略配置不同的EMM原因值。 
### 优势 
不同EMM原因对用户终端的行为有影响。 
当用户终端接入被拒绝时，EMM原因值配置提供了一种影响网络或控制用户行为的方法。 
描述 :MME支持配置多种原因，包括： 
S6a接口故障原因与接入拒绝原因中EMM原因值的映射可配置； 
对于接入失败的特定号码段的用户，其接入拒绝原因中的EMM原因值可配置； 
SGs接口故障原因与接入拒绝原因中EMM原因值的映射可配置； 
配置某些接入失败场景中的特殊接入拒绝原因中的EMM原因值； 
ARD触发分离的分离原因可配置； 
对于ARD导致的用户接入限制，接入拒绝原因可配置； 
ODB触发分离的分离原因可配置； 
对于ODB导致的用户接入限制，接入拒绝原因可配置； 
ZoneCode触发分离的分离原因可配置； 
对于ZoneCode导致的用户接入限制，接入拒绝原因可配置； 
取消位置请求触发分离原因可配置； 
对于本地限制导致的用户接入拒绝，接入拒绝原因可配置； 
对于IMSI号段范围限制导致的用户接入拒绝，接入拒绝原因可配置； 
对于安全模式导致的用户接入拒绝，接入拒绝原因可配置； 
对于认证超时导致的用户接入拒绝，接入拒绝原因可配置； 
S1接口切换取消原因与Sv接口切换取消原因的映射可配置； 
Sv接口故障取消原因与S1接口故障取消原因的映射可配置； 
配置某些场景中切换失败的特殊切换失败原因。 
## ZUF-78-15-011 MPS 
特性描述 :特性描述 :术语 :术语|含义
---|---
多媒体优先级业务|多媒体优先级业务允许被授权用户在网络发生拥塞会话建立受阻时，获取优先于其他用户的无线信道接入的权利。多媒体优先级业务支持端到端的优先级会话。多媒体优先级业务被应用于PS域以及IMS域的语音、视频和数据承载业务。
业务用户|被独立授权使用MPS业务，分配有特定的用户优先级等级，在移动网络运营商完成MPS签约的用户。
描述 :定义 :MPS是一种端到端的多媒体优先级业务。MPS能够允许授权的“业务用户”在网络发生拥塞、会话建立受阻时，获取优先于其他用户的无线信道接入权利，能够优先发起、修改、保持、释放会话以及投递媒体报文。
背景知识 :紧急情况（例如洪水、台风、地震、恐怖袭击等）下，政府及紧急管理官员等需要使用公众网络，但往往此时网络拥塞或部分受损，这就需要为这些特殊用户优先提供业务保证。 
在CS域，eMLPP业务可以提供端到端的CS语音呼叫的优先级业务；类似的，MPS业务将为授权的业务用户提供包括语音、视频、数据等多种媒体的高优先级通信会话；MPS除了提供PS域和IMS域的高优先级业务外，也提供与CS域互通时的优先级传递和端到端高优先业务的延续。
应用场景 :###### IMS多媒体优先级业务 
业务用户进行高优先级的IMS会话；EPC为用户提供高优先级的IMS信令承载、IMS媒体承载，以及终呼时的优先级寻呼，完成高优先级IMS业务。 
###### EPS多媒体优先级业务 
业务用户创建/修改高优先级的EPS承载；根据业务需求，提升现有的EPS承载优先级。 
###### CSFB多媒体优先级业务 
业务用户进行高优先级的CSFB会话；MME为用户提供高优先级的回落业务，以及终呼时的优先级寻呼，完成高优先级CSFB业务。 
客户收益 :受益方|受益描述
---|---
运营商|满足政府对EPC设备网络准入的基本要求。
移动用户|MPS主要为政府机构的特权用户提供通信保障，包括紧急和突发事件处理人员，避免因网络拥塞造成通信受阻。
实现原理 :系统架构 :EPS网络架构如下图所示。 
图1  EPS架构图

涉及的网元 :网元名称|网元作用
---|---
UE|USIM签约高接入 级别，发起高优先级业务。
eNB|支持高优先级连接建立、寻呼、切换和回落。
SGW/PGW|完成优先级业务的承载建立和修改，实现优先级业务的QoS升级和降级。
HSS|完成MPS CS priority和MPS EPS priority的签约和下发。
MSC/VLR|CSFB终呼时，将CS域的优先级业务（eMLPP）信息带给MME。SRVCC时，接收MME的优先级业务指示，完成优先级业务控制。
本网元实现 :MME完成MPS业务的权限检查和控制，根据业务优先级完成优先级寻呼；完成高优先级承载的创建、修改和删除，完成高优先级回落。 
业务流程 :IMS多媒体优先级业务
IMS开始呼叫
IMS开始呼叫流程如下图所示。 
图2  IMS开始呼叫流程

流程说明如下： 
RRC建立和业务请求。由于业务用户使用的接入级范围别是11-15，所以RRC连接建立请求中携带的建立原因为“highPriorityAccess”。此时MME
和eNodeB 优先处理该RRC连接请求，建立S1承载和无线资源。 
UE使用之前建立的EPS承载，发送INVITE消息给P-CSCF，通过消息中的MPS相关信息来通知P-CSCF当前是MPS业务。 
PCC交互。P-CSCF将会话信息发送给PCRF，PCRF识别当前是MPS会话，则按高优先级处理。 
P-CSCF将INVITE消息发送给S-CSCF。 
修改IMS/SIP信令使用的EPS承载。如果当前承载的ARP不适合完成MPS会话，则修改承载的ARP。 
IMS核心网收到"183 Progress"消息，P-CSCF识别当前是MPS业务。 
PCC交互。 P-CSCF将会话信息发送给PCRF，PCRF识别当前是MPS会话，则按高优先级处理。 
P-CSCF将183 Progress消息发送给UE。 
收到183 Progress消息后，UE返回PRACK消息。 
媒体承载建立。PCRF为MPS呼叫的媒体发起高优先级的专有承载建立。 
IMS呼叫建立流程继续。 
IMS终止呼叫
IMS终止呼叫流程如下图所示。 
图3  IMS终止呼叫流程

流程说明如下： 
P-CSCF收到携带MPS会话指示以及起呼业务用户的优先级级别的INVITE消息。 
P-CSCF向PCRF提供的业务信息中，包含有MPS的会话信息和业务用户的优先级级别；PCRF保存信息后返回应答给P-CSCF。 
PCRF判断如果当前承载的ARP不满足MPS会话要求，则发起承载修改。 
PGW发送Update Bearer Request消息给SGW，修改默认承载和IMS信令承载的ARP。 
SGW发送Update Bearer Request消息给MME，修改默认承载和IMS信令承载的ARP。 
P-CSCF发送SIP INVITE消息，作为下行数据报文到达PGW，PGW将其发送给SGW。 
SGW发现当前需要建立S1-U口的下行连接，则发送Downlink Data Notification 消息给MME，消息中携带优先级指示ARP。 
MME发送携带MPS会话对应的优先级指示的寻呼消息给eNB；如果已经处于低优先级的寻呼中，则需要再次下发高优先级的寻呼。 
eNodeB优先处理该寻呼，下发给UE。 
UE发起业务请求，建立承载；SGW向UE下发缓存的下行数据报文（INVITE消息）。 
MME发送Bearer Modify Request 给eNodeB。 
RRC/NAS信令流程。 
eNodeB回复Bearer Modify Response响应。 
MME发送Update Bearer Response给SGW。 
SGW发送Update Bearer Response给PGW。 
PGW发送应答给PCRF。 
IMS终呼流程继续。 
SRVCC
SRVCC流程如下图所示。
图4  SRVCC流程图

流程说明如下： 
eNodeB和MME识别出当前是IMS MPS会话，SCC AS也识别当前是IMS MPS会话。当UE完成测量后，会依照测量报告配置对报告条件进行评估，当设定条件满足时，UE会将测量结果填入Measurement
Report消息，发送给eNodeB。 
eNodeB执行HO决策。 
eNodeB发送Handover required message给MME。 
MME执行承载拆分。 
MME发送SRVCC PS to CS Request消息给MSC Server/MGW时，携带优先级指示ARP，target
RNC/BSS可根据其完成优先级处理。 
MSC server/MGW发送Prepare Handover Request消息给Target MSC，携带根据ARP映射的优先级指示。 
Target MSC发送“Relocation Request/Handover Request”消息给RNC/BSS；RNC/BSS根据优先级指示完成无线资源分配。 
PS域执行HO程序。 
Target RNC发送Relocation Request Acknowledge消息给Target MSC。 
Target MSC发送Prepare Handover Response消息携带优先级指示给MSC server。 
当MGW收到Handover Response后，与target MSC之间优先建立CS承载。 
MSC Server发送Initiation of Session Transfer消息携带优先级指示给IMS，IMS完成会话转移。 
MSC Server发送PS to CS Response给MME。 
MME发送 Handover from EUTRAN Command消息通过eNodeB给UE。 
UE发送Handover to UTRAN Complete消息给Target RNC。 
Target RNC发送Relocation Complete消息给Target MSC，完成PS到CS的切换。 
完成CS承载设置程序。 
完成PS承载设置程序。 
 EPS多媒体优先级业务
Always-On MPS签约的默认承载的Qos分配
当业务用户签约了始终开启的MPS业务，那么当用户附着的时候，用户建立默认承载时，用户的PDN连接就需要保证具备高优先级，即便发生拥塞也不能被抢占。 
PCRF从SPR下载的签约信息就携带了高优先级标志，PCRF根据这一标志，映射出满足MPS业务的QCI和ARP，完成EPS承载建立。 
Always On MPS签约的激活
当业务用户需要激活签约的始终开启的MPS业务，SPR会通知PCRF签约变化；PCRF收到这一通知后，就发起标准的会话修改流程，来完成相关QCI和ARP参数的变更。 
On demand MPS的优先级升级和降级
当业务用户根据需要使用MPS业务时，会引发PCRF发起标准的会话修改流程，来完成相关QCI和ARP参数的变更。 
CSFB多媒体优先级业务
CSFB初始呼叫
如果用户在CS域签约有eMLPP业务，那么在E-UTRAN附着时HSS会向MME下发CS优先级业务指示。 
如果UE处于空闲态，UE发起的RRC连接请求将携带“高优先级接入”的原因。 
UE发送扩展业务请求消息，其S1口将同样携带“高优先级接入”的建立原因；MME决策出需要优先处理CSFB业务，则在发给eNB的消息中指示回落并携带高优先级指示；MME可以对高优先级的CSFB业务进行签约检查。 
CSFB终止呼叫
MSC收到的IAM消息中携带有eMLPP的优先级，则MSC决策需要对用户进行优先级寻呼。 
MME收到MSC携带优先级的寻呼消息，决策当前业务按高优先级处理。 
MME发送携带优先级指示的寻呼给eNB。 
eNB优先寻呼用户。 
用户建立RRC连接。 
MME收到扩展业务请求，按高优先级业务处理。 
MSC收到UE的寻呼响应后，继续按高优先级呼叫处理。 
完成eMLPP的终呼建立。 
附着
如果UE在CS域签约了eMLPP业务，则MME在ULA中获取CS域高优先业务签约信息。 
VLR上报位置更新接受响应消息给MME。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
拥塞控制|MPS用户将不受网络侧拥塞控制的限制
负荷卸载|对于连接态的MPS用户不进行负荷卸载。
遵循标准 :3GPP TS 22.153: “Multimedia priority service”. 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access". 
3GPP TS 23.272: "Circuit Switched (CS) fallback in Evolved Packet System (EPS)". 
3GPP TS 23.216: " Single Radio Voice Call Continuity (SRVCC)". 
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3". 
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)". 
3GPP TS 29.274: "General Packet Radio Service (GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS". 
3GPP TS 29.272: " Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol". 
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持MPS功能”（license ID：7067），此项目显示为“支持”，表示ZXUN uMAC支持MPS功能。
UE|eNodeB|SGW|MME
---|---|---|---
-|√|√|√
UE|eNodeB|SGW|MME
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项|命令
---|---
MPS功能开关配置|SET MPSCFG
SHOW MPSCFG|MPS功能开关配置
ARP优先级到S1口寻呼优先级映射配置|ADD ARP S1PAGE PRI
SET ARP S1PAGE PRI|ARP优先级到S1口寻呼优先级映射配置
DEL ARP S1PAGE PRI|ARP优先级到S1口寻呼优先级映射配置
SHOW ARP S1PAGE PRI|ARP优先级到S1口寻呼优先级映射配置
eMLPP优先级到S1口寻呼优先级映射配置|ADD EMLPP S1PAGE PRI
SET EMLPP S1PAGE PRI|eMLPP优先级到S1口寻呼优先级映射配置
DEL EMLPP S1PAGE PRI|eMLPP优先级到S1口寻呼优先级映射配置
SHOW EMLPP S1PAGE PRI|eMLPP优先级到S1口寻呼优先级映射配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :配置MME实现MPS功能。 
配置前提 :license已设置支持MPS功能。 
已开启MPS功能。 
如果要使用ARP/eMLPP优先级到S1口寻呼优先级的映射，则需要提前配置id为262319软参为1，表示MME支持Paging消息携带寻呼优先级。 
如果需要配置ARP/eMLPP优先级到S1口寻呼优先级的映射，则需要提前规划优先级的映射关系。 
配置过程 :打开MPS功能。 
配置id为262319的软参值为1，支持S1口寻呼携带优先级。 
配置ARP优先级到S1口寻呼优先级的映射关系。 
配置eMLPP优先级到S1口寻呼优先级的映射关系。 
配置实例 :###### IMS的MPS功能 
设置支持MPS功能。 
[SET MPSCFG]:MPSFUNCSWITCH="YES"
新增ARP启用MPS功能及对应的寻呼优先级。 
[ADD ARP S1PAGE PRI]:ARPPRIORITY=4,ISMPS="YES",S1PAGEPRIORITY=2
###### EPS的MPS功能 
设置MPS功能开关为”支持”，是允许非MPS高优先级用户进行高优先级接入。 
[SET MPSCFG]:MPSFUNCSWITCH="YES",MPSCHECKFAILSTYLE="YES"
###### CSFB的MPS功能 
设置支持MPS功能。 
SET MPSCFG:MPSFUNCSWITCH="YES" 
新增eMLPP启用MPS功能及对应的寻呼优先级。 
ADD EMLPP S1PAGE PRI:EMLPPPRIORITY=4,ISMPS="YES",S1PAGEPRIORITY=1 
调整特性 :无 
测试用例 :测试项目|DDN消息触发寻呼带高优先级
测试目的|验证DDN消息中ARP映射寻呼优先级是否正确。
预置条件|设置MME支持MPS功能License为”支持”。设置MPS功能开关为”支持”。设置软参262319（MME是否支持Paging消息携带寻呼优先级）为1。设置ARP为4且为MPS对应的寻呼优先级为2，脚本如下：ADD ARP S1PAGE PRI:ARPPRIORITY=4,ISMPS="YES",S1PAGEPRIORITY=2;
测试过程|用户附着成功，释放s1连接。MME收到该用户的DDN消息，携带ARP为4。触发寻呼请求。
通过准则|寻呼请求优先级为2。
测试结果|-
测试项目|反向专有承载建立消息触发寻呼带高优先级
测试目的|验证反向承载建立触发寻呼携带承载映射的最高优先级是否正确。
预置条件|设置MME支持MPS功能License为”支持”。设置MPS功能开关为”支持”。设置软参262319（MME是否支持Paging消息携带寻呼优先级）为1。设置ARP为3且为mps对应的寻呼优先级为7；设置ARP为5且不为mps对应的寻呼优先级为3；设置ARP为8且为mps对应的寻呼优先级为4。ADD ARP S1PAGE PRI:ARPPRIORITY=3,ISMPS="YES",S1PAGEPRIORITY=7;ADD ARP S1PAGE PRI:ARPPRIORITY=5,ISMPS="NO",S1PAGEPRIORITY=3;ADD ARP S1PAGE PRI:ARPPRIORITY=8,ISMPS="YES",S1PAGEPRIORITY=4;
测试过程|用户附着成功，释放s1连接。MME收到反向专有承载建立消息，携带3个承载，其中ARP分别是3、5、8。触发寻呼请求。
通过准则|寻呼请求优先级为4。
测试结果|-
测试项目|反向承载修改消息触发寻呼带高优先级
测试目的|验证反向承载修改触发寻呼携带映射的最高优先级是否正确。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。设置软参262319（MME是否支持Paging消息携带寻呼优先级）为1。设置ARP为3且为MPS对应的寻呼优先级为7；设置ARP为5且为MPS对应的寻呼优先级为3；设置ARP为8且为MPS对应的寻呼优先级为4。ADD ARP S1PAGE PRI:ARPPRIORITY=3,ISMPS="YES",S1PAGEPRIORITY=7;ADD ARP S1PAGE PRI:ARPPRIORITY=5,ISMPS="YES",S1PAGEPRIORITY=3;ADD ARP S1PAGE PRI:ARPPRIORITY=8,ISMPS="YES",S1PAGEPRIORITY=4;
测试过程|用户附着成功，再建立2个专有承载，三个承载中的ARP分别为3、9、10。释放S1连接。MME收到承载修改消息，修改3个承载，其中后2个承载携带ARP分别是5、8。触发寻呼请求。
通过准则|寻呼请求优先级为4。
测试结果|-
测试项目|附着接入请求高优先级，但用户未签约高优先级，拒绝用户接入
测试目的|验证是否允许非MPS高优先级用户进行高优先级接入配置为“否”时拒绝用户接入。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。设置是否允许非MPS高优先级用户进行高优先级接入配置为“否”。设置拒绝原因为“非法UE”。用户签约数据未签约高优先级。
测试过程|用户发起附着连接，携带高优先级。
通过准则|附着拒绝，NAS原因值为“非法UE”。
测试结果|-
测试项目|用户发起CSFB MO流程，携带高优先级，CSFB Indicator带高优先级
测试目的|验证同时检查请求和签约高优先级，CSFB Indicator带高优先级的情况。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。设置是否允许非MPS高优先级用户进行高优先级接入配置为“是”。设置高优先级CSFB起呼判断方式为高优先级接入和MPS CS高优先级。用户签约数据签约高优先级。
测试过程|用户附着成功，释放S1连接。用户发起CSFB MO扩展业务请求，携带高优先级。
通过准则|扩展业务请求成功，CSFB Indicator携带高优先级。
测试结果|-
测试项目|用户发起CSFB MO流程，携带高优先级，CSFB Indicator不带高优先级
测试目的|验证同时检查请求和签约高优先级，CSFB Indicator不带高优先级的情况。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。设置是否允许非MPS高优先级用户进行高优先级接入配置为“是”。设置高优先级CSFB起呼判断方式为高优先级接入和MPS CS高优先级。用户签约数据未签约高优先级。
测试过程|用户附着成功，释放S1连接。用户发起CSFB MO扩展业务请求，携带高优先级。
通过准则|扩展业务请求成功，CSFB Indicator不携带高优先级
测试结果|-
测试项目|用户发起CSFB MO流程，携带高优先级，CSFB Indicator带高优先级
测试目的|验证同时检查请求和签约高优先级，CSFB Indicator带高优先级的情况。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。设置是否允许非MPS高优先级用户进行高优先级接入配置为“是”。设置高优先级CSFB起呼判断方式为高优先级接入或MPS CS高优先级。用户签约数据未签约高优先级。
测试过程|用户附着成功，释放S1连接。用户发起CSFB MO扩展业务请求，携带高优先级。
通过准则|扩展业务请求成功，CSFB Indicator携带高优先级。
测试结果|-
测试项目|用户发起CSFB MT流程触发寻呼携带高优先级
测试目的|验证CSFB MT消息中eMLPP映射寻呼优先级是否正确。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。
测试过程|用户附着成功，释放S1连接。用户发起CSFB MT触发寻呼。设置软参262319（MME是否支持Paging消息携带寻呼优先级）为1。设置eMLPP为3且为mps对应的寻呼优先级为7。，
通过准则|寻呼请求优先级为7。
测试结果|-
测试项目|用户发起CSFB MT流程触发寻呼携不带高优先级
测试目的|验证CSFB MT消息中eMLPP映射寻呼优先级是否正确。
预置条件|设置MME支持MPS功能License为“支持”。设置MPS功能开关为“支持”。
测试过程|用户附着成功，释放S1连接。用户发起CSFB MT触发寻呼。设置软参262319（MME是否支持Paging消息携带寻呼优先级）为1。设置eMLPP为3且不为mps对应的寻呼优先级为7。
通过准则|寻呼请求不带高优先级。
测试结果|-
常见问题处理 :无 
## ZUF-78-15-012 无线资源管理 
概述 :MME支持通过协作完成无线信道分配和维护。
收益 :运营商可灵活进行无线资源的分配和维护。 
描述 :无线资源管理即在特定用户信息的基础上分配和维护无线信道。 
支持在HSS签约特定的RFSP索引。 
支持在基于IMSI号段的本地MME上配置RFSP索引。 
如果本地配置的RFSP索引和签约的RFSP索引同时存在，MME可控制选用其中之一。 
MME支持通过区分本网用户和漫游用户的方式控制RFSP。 
MME向eNodeB发送RFSP索引，eNodeB将该索引映射到对应的无线信道分配和管理策略。 
## ZUF-78-15-013 载波聚合 
概述 :MME支持与LTE-A协作实现载波聚合功能。 
收益 :本特性提高LTE网络带宽，提升用户体验。 
描述 :载波聚合是LTE-A中的关键技术，支持连续或非连续载波聚合进行数据传输。该技术可将两到三个载波聚合在一起，在未来可实现更多载波的聚合，最终实现网络传输速度的指数级增长。对于多载波聚合，UE需支持多通道功能，并增加UE容量。MME支持保存和传递有关扩展UE能力的信息。 
特性描述 :特性描述 :术语 :无 
描述 :定义 :LTE支持最大20 MHz的系统带宽，而LTE-Advanced系统（以下简称LTE-A）提出支持最大100 MHz的系统带宽要求。为了达到LTE-A的这一要求，3GPP提出了CA（载波聚合，Carrier
aggregation）技术。 
载波聚合技术将多个LTE载波聚合成LTE-A系统的传输载波，使系统带宽突破20 MHz。 
载波聚合对MME的要求，MME在各个接口支持单用户的速率（包括MBR、GBR、APN-AMBR、UE-AMBR）大于256 Mbps。 
背景知识 :LTE目前支持最大20 MHz的系统带宽，下行峰值速率可以达到约300 Mbps。 
而LTE-A要求支持的系统带宽最小为20 MHz，最大带宽达到100 MHz，支持的下行峰值速率为1Gbps，上行峰值速率为500Mbps，下行频谱效率提高到30 bps/Hz，上行频谱效率提高到15 bps/Hz。 
从LTE到LTE-A系统的演进过程中，更宽频谱的需求将成为影响演进的最重要因素之一。考虑到现有的频谱分配方式和规划，很难找到足够的承载LTE-A系统100 MHz带宽的整段频带。因此，3GPP提出了使用载波聚合技术来解决LTE-A系统对频带资源的需求。 
载波聚合方式按照频谱的连续性，载波聚合可以分为连续载波聚合与非连续载波聚合，如[图1]图所示，5个连续的20 MHz频带聚合成一个100 MHz带宽，两个不连续的20MHz频带聚合成一个40 MHz带宽。
图1  连续载波聚合方式与非连续载波聚合

应用场景 :应用场景示意图如[图2]所示。
图2  应用场景
CA用户访问普通的网络浏览类业务。由于网络支持的带宽提高了，用户web网页浏览的响应速度得到了提升。 
CA用户访问高带宽要求的服务时（如视频、流媒体类），数据传输速度会更高，可以观看高清/超高清视频、拨打可视IP网络电话。 
CA用户可以给普通用户提供WiFi热点，让普通用户共享CA高带宽，提高带宽的利用率。 
客户收益 :受益方|受益描述
---|---
运营商|可有效利用更高带宽的频谱，也可为单用户提供达1Gbps的速率
移动用户|访问数据网络的速率可达1Gbps，业务使用更流畅
实现原理 :涉及的网元 :为支持CA功能，涉及UE、eNodeB、MME、SGW、PGW、PCRF、HSS，各网元作用如下： 
网元名称|网元作用
---|---
UE|可以调度多载波
eNodeB|可以调度多载波
MME|控制各个接口是否支持大于256Mbps速率。
SGW|支持大于256Mbps速率。
PGW|支持大于256Mbps速率。
PCRF|决策的QoS策略中的速率可以大于256Mbps速率。
HSS|签约的APN-AMBR和UE-AMBR速率可以大于256Mbps。
本网元实现 :MME支持CA功能之前，GBR、MBR、APN-AMBR、UE-AMBR的速率值最大为256Mbps，支持CA功能之后，GBR、MBR、APN-AMBR、UE-AMBR的速率值可以大于256Mbps。 
MME收到从其他网元发送的速率信息，直接保存。MME在给其他接口（包括S11、S10、S1-MME、NAS接口）发送消息时，如果需要携带速率信息，则根据各个接口的开关进行控制： 
如果该接口的开关“是否支持大于256Mbps速率”为“是”，则MME把保存的速率发送给其他网元。 
如果该接口的开关“是否支持大于256Mbps速率”为“否”，则分为如下两种情况。如果MME保存的速率大于256Mbps，则MME发送给其他网元的速率会修改为256Mbps如果MME保存的速率小于等于256Mbps，则MME把保存的速率发送给其他网元。 
MME在给Gn/Gp接口发送消息时，如果需要携带速率信息。 
如果MME保存的速率小于等于256Mbps，则MME把保存的速率发送给其他网元。 
如果MME保存的速率大于256Mbps，则MME发送给其他网元的速率会修改为256Mbps。 
业务流程 :波及流程包括专有承载建立、PGW发起的承载修改、HSS发起的QoS修改、UE发起的资源分配请求、UE发起的资源修改请求、PDN连接建立、附着、不跨RAT的跟踪区更新、不跨RAT的切换、跨RAT的跟踪区更新、跨RAT的切换等流程中的相关QoS参数传递。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 36.300: " Evolved Universal Terrestrial Radio Access(E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN);Overall description".|-
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)"|-
3GPP TS 29.274: "3GPP Evolved Packet System (EPS); EvolvedGeneral Packet Radio Service (GPRS) Tunnelling Protocol for Controlplane (GTPv2-C) "|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|-
3GPP TS 24.301: " Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS)"|-
特性能力 :名称|指标
---|---
|
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01||首次发布。
License要求 :对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :O&M相关 :命令 :配置项表1  新增配置项配置项命令设置MME支持大于256Mbps速率控制SET MCAQOSCTL 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置实现ZXUN uMAC支持CA载波聚合功能。
配置前提 :无 
配置过程 :通过[SET MCAQOSCTL]设置MME支持大于256Mbps速率控制。
配置实例 :场景描述 :设置MME的S11、S10、S1和NAS接口都支持CA，NAS接口Pre-R8
QoS不支持CA。 
配置步骤 :步骤|操作
---|---
设置MME的S11、S10、S1和NAS接口支持CA，NAS接口Pre-R8 QoS不支持CA|SET MCAQOSCTL: IFS11="YES", IFS10="YES",IFS1="YES",IFNAS="YES", IFPRER8="NO"
调整特性 :无 
测试用例 :测试项目|专有承载建立，NAS支持大于256M
测试目的|验证专有承载建立，NAS支持大于256M
预置条件|网管客户端服务端工作正常，前后台通讯正常。“NAS接口是否支持CA”设置为1-是。
测试过程|LTE用户附着、建立默认承载。接收到SGW的Create Bearer Request 消息，携带MBR或GBR或APN-AMBR大于256Mbps。
通过准则|ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息携带的MBR或GBR或APN-AMBR与上下文中一致。检查对应会话/承载上下文中保存的MBR或GBR或APN-AMBR大于256Mbps。检查性能统计大于256Mbps速率的承载/会话上下文数正确。
测试结果|–
常见问题处理 :无。 
## ZUF-78-15-014 双连接 
特性描述 :特性描述 :术语 :名称|说明
---|---
宏基站|Macro eNodeB或者MeNB，指的是铁塔式的基站，设备比较大，可以覆盖很大的范围。
微基站|Small eNodeB或者SeNB，指的是微型化的基站，设备比较小，覆盖范围小。
描述 :定义 :MME支持DUAL CONNECTIVITY功能，即双连接功能。双连接是指用户终端可以同时连接宏基站和微基站，其中控制面报文只通过宏基站传输，数据报文可以选择由宏基站传输，或者微基站传输，或者二者同时传输。 
背景知识 :近年来，随着智能终端的日益丰富，移动互联网迅猛发展，用户数据流量陡增，在很多热点价值区域，城市环境复杂、业务量大，基站建设的密度已经无法满足用户流量对网络的需求。 
为了应对未来数据流量陡增、满足容量增长需求，在宏基站网络层中，运营商通过布放大量低功率的微基站，来满足热点地区对容量的需求。一般来说，宏基站（又称为MeNB）覆盖较大区域，解决移动通信连续性的问题，微基站（又称为SeNB）设备所覆盖区域，吸收热点地区的数据量。 
上述情况，可以通过DUAL CONNECTIVITY技术来解决。DUAL CONNECTIVITY中微基站和MME是无连接，MME/SGW/PGW核心网不需要感知到微基站的存在，从而减少网络的部署和维护。DUAL
CONNECTIVITY功能的组网示意图如[图1]所示。
图1  DUAL CONNECTIVITY功能组网示意图

应用场景 :DUAL CONNECTIVITY功能有如下三种应用场景。 
需要保证热点覆盖的场景在大型场所，包括大规模的剧院、影城、展览馆、体育馆、机场等，其场地开阔、容纳人数众多，当开展活动时，话务模型密度高、话务量大，此时仅依靠覆盖在室外的宏基站难以解决话务量大的问题。此时通过临时放置微基站，微基站经过IP网连接到SGW/PGW，从而扩大热点区域的流量。 
需要保证盲点覆盖的场景在宏基站无法覆盖的地方，比如写字楼与宾馆酒店，因为写字楼与宾馆酒店一般位于大型、高层建筑内，高层楼宇在底部区域易出现移动信号覆盖弱甚至盲区，此时通过放置微基站来扩大网络的覆盖范围。 
需要降低建设成本的场景微基站在规格上远远小于宏基站，从而微基站的成本远远低于宏基站，使用微基站可以大大节约建设成本。 
客户收益 :受益方|受益描述
---|---
运营商|提高网络覆盖降低成本投入。提高热点区域的容量。提高终端的吞吐量。
移动用户|提高用户的网络速度以及覆盖范围，从而提高用户的感受。
实现原理 :系统架构 :DUAL CONNECTIVITY功能中系统架构如[图2]所示。
图2  DUAL CONNECTIVITY系统架构图

宏基站与MME存在控制面的连接，与SGW存在媒体面的连接。 
微基站与MME无连接，与SGW存在媒体面的连接。 
涉及的网元 :网元名称|网元作用
---|---
MME|MME能够支持DUAL CONNECTIVITY功能中eNodeB的要求迁移到微基站的承载通知SGW进行修改。
MeNB|宏基站MeNB对发生迁移到微基站的承载，通知MME进行修改。微基站SeNB对MME不可见。
SGW|MME与SGW间增加了Modify Bearer Request消息数量，SGW需要能够处理这些消息。
本网元实现 :MME能够支持DUAL CONNECTIVITY功能中eNodeB要求迁移到微基站的承载，并通知SGW进行修改。 
业务流程 :DUAL CONNECTIVITY功能涉及到UE、eNodeB和MME的业务流程的修改，对于SGW和PGW无变化，具体业务流程如[图3]所示。
图3  DUAL CONNECTIVITY功能业务流程图

流程简要描述如下： 
MeNB给MME发送E-RAB Modification Indication消息，携带E-RAB to be Modified
List和E-RAB not to be Modified List，包含提供给SGW的Secondary eNodeB下行用户面地址eNodeB
address(es) and TEIDs. 
MME将所有需要更新承载最新的下行用户面地址通过Modify Bearer Request消息带给SGW. 
SGW给MME发送Modify Bearer Response消息，携带Serving GW address 以及TEID.
SGW可以使用新的地址将下行数据发送给SeNB. 
MME给MeNB发送E-RAB Modification Confirm消息，携带请求消息中需要修改承载的修改结果（包括哪些承载修改成功，哪些承载修改失败，哪些承载需要释放）。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "GPRS enhancements for E-UTRANaccess".|章节5.4.7
特性能力 :该特性不涉及规格指标。 
可获得性 :License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性对应License文件中的项目为“MME支持双连接功能”，此项目显示为ON，表示ZXUN uMAC支持DUAL CONNECTIVITY接入功能。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :该特性不涉及命令的变化。 
性能统计 :测量类型|描述
---|---
S1AP消息测量|C432000081 E-RAB MODIFICATION INDICATION消息接收次数
C432000082 E-RAB MODIFICATION CONFIRM消息发送次数|S1AP消息测量
基于eNB局向的S1AP消息测量|C470020083 E-RAB MODIFICATION INDICATION消息接收次数
C470020084 E-RAB MODIFICATION CONFIRM消息发送次数|基于eNB局向的S1AP消息测量
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置支持双连接特性，实现用户终端同时连接宏基站和微基站，解决热点覆盖，盲点覆盖的问题。 
配置前提 :无 
配置过程 :打开软参786803
功能开关，支持双连接功能。
配置实例 :运营商需要使用双连接功能，这时只需要在MME上打开软参开关即可。 
步骤|操作
---|---
设置支持双连接功能。|SHOW SOFTWARE PARAMETER:PARAID=786803,FLAG="CHANGED"
调整特性 :无 
测试用例 :测试项目|多PDN多承载，双连接功能
---|---
测试目的|验证MME修改列表的承载ID和second enodeB用户面信息成功带给SGW。
预置条件|用户取得MME网元支持双连接功能的license授权，并更新了license。打开软参“支持双连接功能”开关。
测试过程|打开信令跟踪与性能统计。用户4G附着后，非GBR专有承载建立成功，PDN连接建立成功，多PDN多承载，Master eNodeB给MME发送E-RABModification Indication消息，携带E-RAB to be Modified List和E-RAB not tobe Modified List，包含提供给SGW的Secondary eNodeB下行用户面地址eNodeB address(es)and TEIDs。
通过准则|MME将所有需要更新承载最新的下行用户面地址通过Modify Bearer Request消息带给SGW。SGW给MME发送Modify Bearer Response消息，携带Serving GW address andTEID，SGW可以使用新的地址将下行数据发送给eNodeB。MME给eNodeB发送E-RAB Modification Confirm消息，携带请求消息中需要修改承载的修改结果（承载修改成功）。查看性能统计，S1AP消息测量与基于eNB局向的S1AP消息测量，E-RAB MODIFICATION INDICATION消息接收次数和E-RABMODIFICATION CONFIRM消息发送次数统计正确。
测试结果|–
常见问题处理 :无 
## ZUF-78-15-015 CS/PS协作 
特性描述 :特性描述 :术语 :术语|含义
---|---
MOCN|Multi-Operator Core Network，多运营商的核心网。通过MOCN网络，一套无线网络可以同时连接到多个运营商的核心网节点，实现多家运营商共享同一套无线网络。
描述 :定义 :ZXUN uMAC支持CS/PS Coordination特性，即CS/PS协作。通过本特性功能可以在MOCN共享网络中保证用户在CS域和PS域被同一运营商服务。
背景知识 :在传统的网络中，运营商一般既会部署CS网络又会部署PS网络，用户在CS域和PS域总是被同一运营商服务。但在MOCN共享网络中，如[图1]所示，运营商A、B、C共享无线接入，而单独部署各自的核心网元。为用户服务的运营商不止一个，当用户在CS和PS间来回移动或发起登记时，用户可能选择不同的运营商接入到CS和PS，存在跨PLMN的计费和用户管理等问题。
图1  MOCN共享网络组网示意图

因此，引入CS/PS Coordination特性，保障在共享网络的架构下，用户在CS域和PS域来回切换时，始终在同一个PLMN下接入网络，解决跨PLMN计费和用户管理问题。 
应用场景 :在多运营商共享网络架构中，CS/PS Coordination功能可保证用户在PS域和CS域被同一个运营商服务。通常应用在如下两个场景中。 
用户语音回落（CSFB）时，通过CS/PS Coordination功能保证用户回落到CS域时选择的PLMN和PS域的一致。 
用户移动语音连续性（SRVCC）时，通过CS/PS Coordination功能保证2/3G时选择的PLMN和LTE时选择的PLMN一致。 
客户收益 :受益方|受益描述
---|---
运营商|避免跨PLMN的计费，方便用户统计管理，降低运维成本。
用户|提升用户体验，保障用户利益。
实现原理 :系统架构 :CSFB业务场景中，CS/PS Coordination特性功能涉及的系统架构如[图2]所示。
图2  CSFB场景的系统架构

SRVCC业务场景中，CS/PS Coordination特性功能涉及的系统架构如[图3]所示。
图3  SRVCC场景的系统架构

涉及的网元 :网元名称|网元作用
---|---
MME|移动性管理网元，在用户联合附着或者联合TAU时将用户PS域的PLMN带给MSC Server。在HandOver流程中，将切换限制列表带给E-NodeB。
MSC|移动交换中心网元，接收并保存MME提供的PS域的PLMN，作为选择CS域PLMN的依据。
E-NodeB|演进的NodeB，在HandOver流程中，接收MME下发的切换限制列表，用于保障CS域和PS域的PLMN统一。
协议栈 :本特性涉及的接口协议栈说明如下： 
CSFB业务场景该场景涉及MME和MSC Server之间的SGs接口，在联合Attach和联合Tau时，为了保证用户CSFB时选择的是同一个运营商，MME通过SGs口向MSC发送Update
Location Request，通知其PS域的运营商。接口协议栈如图4所示。图4  SGs接口协议栈 
SRVCC业务场景该场景涉及eNodeB和MME之间的S1-MME接口，在HandOver流程中，为了保证用户SRVCC流程选择同一个运营商，MME通过S1-MME口向E-NodeB下发切换限制列表消息。接口协议栈如图5所示。图5  S1-MME接口协议栈 
本网元实现 :CSFB业务场景，用户语音回落在共享网络中终端接入PS域，当用户发起CSFB回落到CS域进行语音业务时，用户会重新选择CS域的PLMN进行接入，而用户可选择接入的PLMN可以有很多个，分属不同的运营商，因此选择的此PLMN可能和之前接入的PS域的PLMN不一致。开启了CS/PS Coordination功能后，在用户联合附着、联合位置更新流程中，ZXUN uMAC根据用户当前PS域的PLMN选择CS域的MSC/VLR，同时携带PS域的PLMN用于指示CS域选择PLMN，保证用户回落到CS域时选择的PLMN和PS域的一致。 
SRVCC，用户移动语音连续性用户进行语音呼叫在LTE网络和2/3G CS网络之间移动时，当有多个PLMN可用于CS域，2/3G时选择的PLMN可能和LTE时选择的PLMN不一致。开启了CS/PS Coordination功能后，用户切换流程中，在切换限制列表消息中会携带LTE语音时的PLMN，保证在SRVCC业务时选择的PLMN一致。 
业务流程 :本特性涉及的业务流程说明如下。 
联合Attach
CSFB业务场景中涉及联合附着流程，如[图6]所示。
图6  联合附着流程

UE通过eNodeB发送联合附着消息到MME。 
MME根据3GPP 23.401协议的附着流程继续附着流程，直到接收到SGW创建会话响应。
MME根据消息中TAI，以及用户的IMSI，查询本地配置，获取映射的LAI，基于LAI得到LAI归属的MSC POOL，再根据POOL内各个MSC/VLR的优先级和权重以及NRI、IMSI得到MSC/VLR局向ID。
MME确定MSC局向ID后，按照路由组-路由-链路的层级关系，选择可用的SGs链路，向此局向发送Location Update
Request位置更新消息。 
其中，Location Update Request消息中携带New location area
identifier和Selected CS domain operator两个字段，这两个字段的PLMN为PS域的PLMN。 
MME和MSC/VLR建立SGs接口关联。 
MSC/VLR完成CS域的位置更新流程。 
MSC/VLR发送位置更新响应消息给MME，携带位置更新结果以及为用户分配的TMSI。 
MME继续完成后续的附着流程。 
联合TAU
CSFB业务场景中涉及联合TAU流程，如[图7]所示。
图7  联合TAU业务流程

UE识别判断需要执行TAU流程。 
UE通过eNodeB发送联合TAU消息到MME。 
MME根据3GPP 23.401协议进行TAU业务处理，从Old MME获得用户的上下文，在新的SGW完成承载建立。 
MME根据消息中TAI，以及用户的IMSI，查询本地配置，获取映射的LAI，基于LAI得到LAI归属的MSC POOL，最后再根据POOL内各个MSC/VLR的优先级和权重以及NRI、IMSI，得到MSC/VLR局向ID。MME确定MSC局向ID后，按照路由组——路由——链路的层级关系，选择可用的SGs链路，向此局向发送位置更新消息，如MSC局向发送变化，MME与新的MSC建立SGs关联。 
MSC/VLR完成CS域的位置更新流程。 
其中，Location Update Request消息中携带New
location area identifier和Selected CS domain operator两个字段，这两个字段的PLMN为PS域的PLMN。 
MSC/VLR发送位置更新响应消息给MME，携带位置更新结果以及为用户分配的TMSI。 
MME向UE返回TAU Accept消息。 
UE向MME返回TAU Complete。 
基于S1的Handover流程
SRVCC业务场景涉及基于S1的Handover流程，如[图8]所示。
图8  基于S1的Handover流程

基于如下原因，Source eNodeB决定发起基于S1口的eNodeB间的切换流程。 
到Target eNodeB没有X2连接。 
Target eNodeB告知Source eNodeB之前的X2-based handover失败。 
Source eNodeB收到动态信息。 
Source eNodeB向Source MME发送Handover Required消息请求切换，消息中包含：Direct
Forwarding Path Availability、Source to Target transparent container、target
eNodeB Identity、CSG ID、CSG access mode、target TAI、S1AP Cause等参数，MME根据Target
eNodeB Identity判断MME不需要改变。 
Source MME选择Target MME，然后向Target MME发送Forward Relocation Request消息，消息中包括MME
UE context, Source to Target transparent container, RAN Cause, target
eNodeB Identity, CSG ID, CSG Membership Indication, target TAI, MS
Info Change Reporting Action (if available), CSG Information Reporting
Action (if available), UE Time Zone, Direct Forwarding Flag, Serving
Network, Local Home Network ID等参数。 
Target MME根据TAI判断SGW发生改变。 
Target MME按每PDN连接向Target SGW发送Create Session Request消息，消息包含：bearer
context(s) with PDN GW addresses and TEIDs (for GTP-based S5/S8) at
the PDN GW(s) for uplink traffic、Serving Network等参数。 
Target SGW向Target MME返回Create Session Response消息。 
Target MME向Target eNodeB发送Handover Request消息时，携带Handover Restrict
List（切换限制列表）给eNodeB，切换限制列表中包括目前Serving PLMN和Equivalent PLMNs，其中Serving
PLMN即为PS域的PLMN。 
后续的SRVCC流程，E-NodeB为用户选择CS域的PLMN时就会选择Handover Request时携带的PS域的PLMN。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 29118-d50 Selected CS domain operator|9.4.27
3GPP TS 23.251: Network Sharing|4.1，4.2
3GPP TS 29.118: Mobility Management Entity (MME) –VisitorLocation Register (VLR) SGs interface specification|5.1.3，5.2.2
特性能力 :该特性不涉及规格指标。 
可获得性 :License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持CS/PS协作”（license ID：7014），此项目显示为“支持”，表示ZXUN uMAC支持CS/PS协作特性。
对其他网元的要求 :CS/PS协作特性需要MSC/VLR、eNodeB配合完成。 
UE|MME|MSC|eNodeB
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项|命令
---|---
设置CS/PS协作控制策略|SET CSPS COORDI
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :运营商部署了MOCN，用户通过共享无线联合接入核心网，用户在CSFB或者SRVCC时有多个运营商可以选择。通过配置可以实现共享网络中的CS/PS
Coordination特性功能。
 说明： 
本功能涉及的CSFB和SRVCC两个业务场景的配置完全相同。 
配置前提 :运营商部署了MOCN，且打开了CS/PS协作的License。 
配置过程 :使用[SET CSPS COORDI]命令，配置开启CS/PS Coordination功能。
配置实例 :场景说明 :在共享网络中，运营商希望保证用户在CS域和PS域都被统一运营商服务。 
数据规划 :不涉及。 
配置步骤 :在联合Attach、联合TAU配置的基础上，增加配置，如[表1]所示。
步骤|操作
---|---
配置MME支持CS/PS协作|SET CSPS COORDI:MMESUPCSPSCOORDI="YES“
调整特性 :不涉及。 
测试用例 :测试项目|CSFB场景下，CS/PS协作功能。
---|---
测试目的|用户发生CSFB时，CS域选择的PLMN和PS域的PLMN相同
预置条件|加载CS/PS Coordination的License。打开CS/PS Coordination的开关。SET CSPS COORDI:MMESUPCSPSCOORDI="YES";
测试过程|用户进行联合附着流程。在信令跟踪中，查看Location Update Request消息中的New Location Area Identifier和SelectedCS Domain Operator中的PLMN为PS域的PLMN。用户发生CSFB业务。
通过准则|在CS域的网管信令跟踪中，查看RAI参数中选择的PLMN和Location Update Request中SelectedCS domain operator携带的PLMN相同。
测试结果|–
测试项目|SRVCC场景下，CS/PS协作功能。
---|---
测试目的|用户发生SRVCC时，CS域选择的PLMN和PS域的PLMN相同
预置条件|加载CS/PS Coordination的License。打开CS/PS Coordination的开关。SET CSPS COORDI:MMESUPCSPSCOORDI="YES";
测试过程|用户进行附着流程。用户发起基于S1的切换流程，MME下发切换限制列表给eNodeB，其中的PLMN为PS域的PLMN。用户发生SRVCC业务。
通过准则|在CS域的网管信令跟踪中，查看到CS域选择的PLMN和PS域的PLMN相同。
测试结果|–
常见问题处理 :特性未生效的几个可能原因如下： 
版本不支持，请升级到最新版本。 
License未打开。 
## ZUF-78-15-016 3GPP和WLAN间基于无线辅助互操作 
特性描述 :特性描述 :术语 :术语|含义
---|---
WLAN|无线本地接入网络
描述 :定义 :RAN-assisted WLAN interworking，即3GPP和WLAN之间基于无线辅助的互操作。无线辅助参数包括E-UTRAN信令长度和质量门限、WLAN通道利用门限、WLAN回传数据率门限、WLAN标识列表和卸载优先指示OPI。UE使用这些无线辅助参数执行接入网选择和WLAN与3GPP之间的话务控制决策，比如，MME可以提供PDN连接是否可以WLAN负荷卸载信息给UE。
背景知识 :尽管移动网络技术从电路域向分组域演进，从窄带技术逐步向宽带技术演进，从2G到3G再到LTE，空口的频谱带宽越来越宽、传输效率也得到大幅提升，但这并不能满足用户对移动互联网的迫切需求，尤其在一些热点地区。因此移动运营商为提高用户体验需要引入异构网作为移动网络的有效补充，以分担移动网络的高负荷分组数据业务。目前WLAN作为移动运营商优选的异构网络来部署，一方面是因为移动终端，尤其WLAN已经是智能终端标准配置；另一方面是因为WLAN的频谱免费开放、产业链成熟和部署灵活等优势，所以对于移动运营商来说，在热点地区部署WLAN网络作为移动蜂窝网络的有效补充，不但OPEX（Operating
Expense，运营成本）和CAPEX（Capital Expenditure，网络设备、计算机、仪器等一次性支出）较低，而且还提高了网络服务质量和用户满意度。
3GPP 23.402协议中就定义了非3GPP网络如何接入到EPC中，提供了一种WLAN无缝接入到EPC网络中的融合架构，支持移动IP流，并使得3GPP网络能够借助WLAN无缝进行流量卸载。
但在23401的R13版本中，提出RAN的应用规则会导致用户选择并且移动到不安全的WLAN网络里，从而影响用户体验。基于此，2015年9月的3GPP会议上提出一种解决方案，就是本特性实现的，由MME给UE下发一个无线辅助参数，用于UE来选择是否负荷卸载到WLAN。该参数是PDN级别的，即通过每个PDN连接的NAS信令传递给UE。 
23.402协议里的RAN的应用规则会导致用户选择并且移动到不安全的WLAN网络里，从而影响用户体验。基于此，2015年9月的3GPP会议上提出一种解决方案，就是由MME针对每个PDN连接，提供是否可以WLAN负荷卸载信息给UE，该信息通过每PDN连接的NAS信令给UE。 
应用场景 :在有运营商WLAN网络的地方，用户所有的业务都可以负荷卸载到WLAN。 
部分APN可以负荷卸载到WLAN。 
HSS还不支持RAN辅助的WLAN负荷卸载控制，运营商又想进行控制。 
运营商想对漫游用户进行本地控制。 
客户收益 :受益方|受益描述
---|---
运营商|方便运维管理：可以通过本地配置和签约等手段分别控制用户或者APN级别的WLAN负荷卸载信息。
用户|提升用户体验：用户可以使用该无线辅助参数执行接入网选择和WLAN与3GPP之间的话务控制决策。
实现原理 :系统架构 :系统架构如[图1]所示。
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
UE|支持保存和使用核心网下发的WLAN负荷卸载能力。
eNodeB|支持透传核心网下发的WLAN负荷卸载能力给UE。
HSS|负责对UE签约UE或PDN级的WLAN负荷卸载能力。
MME|针对每个PDN连接下发WLAN负荷卸载能力。
协议栈 :图2  NAS接口协议栈

图3  S6a口协议栈

图4  S1-MME接口协议栈

本网元实现 :针对每个PDN连接，提供是否可以负荷卸载到WLAN的信息给UE，该信息通过每个PDN连接的NAS信令给UE。 
业务流程 :在附着过程中，MME得到签约数据保存，当建立默认PDN连接的默认承载时，根据签约和本地策略确定下发的WLAN负荷卸载能力指示，在激活默认承载上下文请求中下发给UE。 
Attach中的WLAN负荷卸载控制如[图5]所示。
图5  Attach中的WLAN负荷卸载控制

WLAN offload indication决策过程如[图6]所示。
图6  WLAN offload indication决策过程

系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: General Packet Radio Service (GPRS) enhancementsforEvolved Universal Terrestrial Radio Access Network (E-UTRAN) access|Release 14
3GPP TS 23.402: Architecture enhancements for non-3GPP accesses|Release 14
3GPP TS 24.301: Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS)|Release 14
3GPP TS 29.272: Mobility Management Entity(MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol|Release 14
3GPP TS 29.274: Evolved General Packet Radio Service (GPRS)Tunnelling Protocol for Control plane (GTPv2-C)|Release 14
特性能力 :名称|指标
---|---
支持APN拥塞控制的最大APN个数|256（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要开启License，对应的License项目为“MME支持无线辅助的WLAN互操作”（license ID：7113），此项目显示为“支持”，表示ZXUN uMAC支持无线辅助的WLAN互操作功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 


O&M相关 :



命令 :
 
配置项表1  新增配置项

配置项
命令



无线辅助WLAN互操
SET WLAN INTERWORKING CONTROL SWITCH


SHOW WLAN INTERWORKING CONTROL SWITCH


无线辅助WLAN互操作本地策略配置
ADD WLAN INTERWORKING LOCAL POLICY


SET WLAN INTERWORKING LOCAL POLICY


DEL WLAN INTERWORKING LOCAL POLICY


SHOW WLAN INTERWORKING LOCAL POLICY

 

 
安全变量该特性不涉及安全变量的变化。 

 
软件参数该特性不涉及软件参数的变化。 

 


性能统计 :该特性不涉及计数器的变化。 


告警和通知 :该特性不涉及告警/通知消息的变化。 


业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 


话单与计费 :该特性不涉及话单与计费的变化。 




特性配置 :特性配置 :配置说明 :本地加载License，打开支持无线辅助的WLAN互操作开关，根据需要配置使用本地或签约的策略，来实现无线辅助的WLAN交互功能。 
配置前提 :运营商打开了“MME支持无线辅助的WLAN互操作”的License。
配置过程 :使用[SET WLAN INTERWORKING CONTROL SWITCH]命令，配置无线辅助WLAN互操作控制。设置是否支持RAN辅助的WLAN互操作，是否支持本地策略，是否在WLAN负荷卸载能力变化时立即通知UE；当需要对EPC业务卸载到WLAN进行控制时，使用该命令。
使用[ADD WLAN INTERWORKING LOCAL POLICY]命令，配置无线辅助WLAN互操作本地控制策略。需要根据用户或APN进行本地的WLAN负荷卸载能力控制时，使用该命令。
配置实例 :###### 实例场景1 
在有运营商WLAN网络的地方，用户所有的业务都可以负荷卸载到WLAN。 
运营商网络的WLAN和LTE支持的业务相同，比如同时支持VoWIFI和VoLTE，当用户处于同时具有WLAN和LTE的环境时，所有业务都可以负荷卸载到WLAN。 
配置步骤： 
步骤|命令|说明
---|---|---
1|SET WLAN INTERWORKING CONTROL SWITCH:MMESUPRANWLAN="YES",LOCWLANCTRLSUP="YES",DFTEUTRANPOLICY="OFFLOAD",DFTUTRANPOLICY="OFFLOAD",LOCALDFTPRIOR="LOCDEFPLYPRI"|设置支持RAN辅助的WLAN互操作，支持本地控制，默认的WLAN负荷卸载能力为支持，本地控制优先级高。
###### 实例场景2 
特定业务支持负荷卸载到WLAN。 
当用户处于运营商WLAN和LTE的重叠覆盖环境时，只有指定的业务（比如APN是zte.com）才允许被负荷卸载到WLAN。 
配置步骤： 
步骤|命令|说明
---|---|---
1|SET WLAN INTERWORKING CONTROL SWITCH:MMESUPRANWLAN="YES",LOCWLANCTRLSUP="YES"|设置支持RAN辅助的WLAN互操作，支持本地控制。
2|ADD WLAN INTERWORKING LOCAL POLICY:APN="zte.com",LOCALPRIOR="LOCPLYPRI",EUTRANPOLICY="YES",UTRANPOLICY="YES"|配置APN“zte.com”支持本地配置优先，并配置为WLAN负荷卸载能力为支持。
###### 实例场景3 
一类用户的所有业务支持负荷卸载到WLAN。 
配置步骤： 
步骤|命令|说明
---|---|---
1|SET WLAN INTERWORKING CONTROL SWITCH:MMESUPRANWLAN="YES",LOCWLANCTRLSUP="YES",DFTEUTRANPOLICY="NOTOFFLOAD",DFTUTRANPOLICY="NOTOFFLOAD",LOCALDFTPRIOR="LOCDEFPLYPRI"|设置支持RAN辅助的WLAN互操作，支持本地控制，默认的WLAN负荷卸载能力为不支持，本地控制优先级高。
2|ADD WLAN INTERWORKING LOCAL POLICY:IMSI="4601123456",APN="zte.com",LOCALPRIOR="LOCPLYPRI",EUTRANPOLICY="YES"|配置用户4601123456号段的所有业务，WLAN负荷卸载能力为支持。
###### 实例场景4 
一类用户的特定业务支持负荷卸载到WLAN。 
配置步骤： 
步骤|命令|说明
---|---|---
1|SET WLAN INTERWORKING CONTROL SWITCH:MMESUPRANWLAN="YES",LOCWLANCTRLSUP="YES"|设置支持RAN辅助的WLAN互操作，支持本地控制。
2|ADD WLAN INTERWORKING LOCAL POLICY:IMSI="4601123456",APN="zte.com",LOCALPRIOR="LOCPLYPRI",EUTRANPOLICY="YES"|配置用户4601123456号段的APN为“zte.com”的业务，WLAN负荷卸载能力为支持。
调整特性 :本特性暂不支持调整参数。 
测试用例 :测试项目|在有运营商WLAN网络的地方，用户所有的业务都可以负荷卸载到WLAN
---|---
测试目的|当用户处于同时具有WLAN和LTE的环境时，所有业务都可以负荷卸载到WLAN。
预置条件|打开了“MME支持无线辅助的WLAN互操作”的License。
测试过程|设置支持RAN辅助的WLAN互操作，支持本地控制，默认的WLAN负荷卸载能力为支持，本地控制优先级高。用户Attach。
通过准则|用户Attach成功。在激活默认承载上下文请求中带参数WLAN负荷卸载能力指示标识给UE，其中E-UTRAN的负荷卸载能力值为1。
测试结果|–
测试项目|部分APN可以负荷卸载到WLAN
---|---
测试目的|当用户处于运营商WLAN和LTE的重叠覆盖环境时，对可以卸载的业务才卸载到WLAN。
预置条件|打开了“MME支持无线辅助的WLAN互操作”的License。
测试过程|设置支持RAN辅助的WLAN互操作，支持本地控制。配置某APN比如“zte.com”支持本地配置优先，并配置为WLAN负荷卸载能力为支持。用户Attach以APN“zte.com”接入网络。
通过准则|用户Attach成功。在激活默认承载上下文请求中带参数WLAN负荷卸载能力指示标识给UE，其中E-UTRAN的负荷卸载能力值为1。
测试结果|-
测试项目|HSS还不支持RAN辅助的WLAN负荷卸载控制，运营商又想进行控制
---|---
测试目的|网络中网元支持能力不是同步升级时，HSS可能还没有升级到支持签约，但是网络中已经存在卸载到WLAN出了问题需要控制，就在MME上进行配置控制为不支持负荷卸载到WLAN。
预置条件|打开了“MME支持无线辅助的WLAN互操作”的License。
测试过程|设置支持RAN辅助的WLAN互操作，支持本地控制，默认的WLAN负荷卸载能力为不支持，本地控制优先级高。用户Attach
通过准则|用户Attach成功。在激活默认承载上下文请求中带参数WLAN负荷卸载能力指示标识给UE，其中E-UTRAN的负荷卸载能力值为0。
测试结果|-
测试项目|运营商想对漫游用户进行本地控制
---|---
测试目的|漫游用户归属网络可能还不支持负荷卸载签约，或者漫游用户没有签约，但是拜访网络想控制UE在有WIFI的地方回落或不回落，就在MME上进行配置控制。
预置条件|打开了“MME支持无线辅助的WLAN互操作”的License。
测试过程|设置支持RAN辅助的WLAN互操作，支持本地控制。配置某漫游用户号段比如“46023456”支持本地配置优先，并配置为WLAN负荷卸载能力为不支持。46023456号段用户Attach。
通过准则|用户Attach成功。在激活默认承载上下文请求中带参数WLAN负荷卸载能力指示标识给UE，其中E-UTRAN的负荷卸载能力值为0。
测试结果|-
常见问题处理 :无常见问题处理。 
# 缩略语 
# 缩略语 
3GPP :3rd Generation Partnership Project第三代合作伙伴计划
APN :Access Point Name接入点名称
## ARPU 
Average Revenue Per User每用户平均收入
## BM-SC 
Broadcast Multimedia–Service Center广播多媒体业务中心
## CA 
Carrier Aggregation载波聚合
## CAPEX 
Capital Expenditure资本性支出
## CSFB 
Circuit Switched Fallback电路域回落
## CSG 
Closed Subscriber Group闭合用户组
## DeNB 
Donor eNB施主基站
## E-UTRA 
Evolved Universal Terrestrial Radio Access演进通用陆地无线接入
E-UTRAN :Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
## ECGI 
E-UTRAN Cell Global IdentifierE-UTRAN小区全球标识
EM :Engineering Mode工程模式
## eMBMS 
Evolved Multimedia Broadcast Multicast Service演进的多媒体广播多播业务
## eMLPP 
enhanced Multi-Level Precedence and Pre-emption	增强型多级优先和占先业务
## eNB 
Evolved Node B演进型基站
eNodeB :Evolved NodeB演进的NodeB
EPC :Evolved Packet Core演进的分组核心网
## EPLMN 
Equivalent Public Land Mobile Network对等公用陆地移动网
EPS :Evolved Packet System演进的分组系统
GPRS :General Packet Radio Service通用无线分组数据业务
## GWCN 
Gateway Core Network网关核心网
## HeNB 
Home eNode BLTE家庭基站
## HNB 
Home Node B3G家庭基站
HSS :Home Subscriber Server归属用户服务器
## IPSec 
IP Security ProtocolIP安全协议
## LGW 
Local Gateway本地接入网关
## LIPA 
Local IP Access本地IP接入
LTE :Long Time Evolution更长期发展
## MBMS 
Multimedia Broadcast/Multicast Service多媒体广播/组播业务
## MBMSGW 
Multimedia Broadcast Multicast Service Gateway多媒体广播多播业务网关
## MCE 
Multi-cell/Multicast Coordination Entity多小区/多播协调实体标识
## MeNB 
Macro eNodeB与HeNB（LTE家庭基站）相对应
MME :Mobility Management Entity移动管理实体
## MOCN 
Multi-Operator Core Network多运营商核心网
## MPS 
Multimedia Priority Service多媒体优先业务
## NRI 
Network Resource Identifier网络资源标识
## OPEX 
Operating Expenditure运营性支出
PDN :Packet Data Network分组数据网
PGW :PDN Gateway分组数据网网关
PLMN :Public Land Mobile Network公共陆地移动网
## RFSP 
RAT/Frequency Selection Priority无线/频率选择优先级
## RN 
Radio Network无线网络
## SeGW 
Security Gateway安全网关
SGW :Serving Gateway服务网关
## SIPTO 
Selected IP Traffic Offload选定的IP流量分流 
## SNA 
Systems Network Architecture系统网络体系结构
## SRVCC 
Single Radio Voice Call Continuity双模单待无线语音呼叫连续性
## TAI 
Tracking Area Identity跟踪区标识
TAU :Tracking Area Update跟踪区域更新
UE :User Equipment用户设备
## WLAN 
Wireless Local Area Network无线局域网
# ZUF-78-16 逻辑接口 
概述 :功能描述 :MME在处理用户移动性管理业务、切换业务、PDN建立/修改/删除、定位业务、短消息业务、SGs口语音回落、事件暴露、4/5G互操作等业务时，通过逻辑接口和其他网元进行交互。 
MME和周边网元逻辑接口如[图1]所示。
图1  MME接口架构图

功能特性简介 :ZXUN uMAC相关的3GPP接口与协议定义了MME相关的逻辑接口，详细参见下表：
方案特性|实现简述|特导链接
---|---|---
S1-MME|eNodeB通过S1接口和MME完成无线接口的对接。|ZUF-78-16-001 S1-MME
S6a|MME通过S6a接口和HSS完成鉴权向量获取、位置功能更新等功能。|ZUF-78-16-002 S6a
S11|MME通过S11接口和SGW完成PDN创建、承载建立等功能。|ZUF-78-16-003 S11
S10|MME通过S10接口和MME完成局间切换以及局间TAU功能。|ZUF-78-16-004 S10
Gn/Gp|MME通过GnGp接口和SGSN完成跨RAT切换和更新。|ZUF-78-16-005 GnGp
S13|MME通过S13接口和EIR完成IMEI检查功能。|ZUF-78-16-006 S13
SGs|MME通过SGs接口和MSC for CSFB or SMS完成CSFB语音回落和SMS业务。|ZUF-78-16-007 SGs
Sv|MME通过Sv接口和MSC-S交互，以实现SRVCC功能，完成VoLTE语音切换。|ZUF-78-16-008 Sv
SLg|MME通过SLg协议接口和GMLC交互以完成LCS功能。|ZUF-78-16-009 SLg
SLs|MME通过SLs协议接口和E-SMLC交互以完成LCS功能。|ZUF-78-16-010 SLs
Sm|MME通过Sm协议接口和MBMS GW交互以完成eMBMS功能。|ZUF-78-16-011 Sm
M3|MME通过M3协议接口和MCE交互以完成eMBMS功能。|ZUF-78-16-012 M3
S3|MME通过S3接口与S3/S4 SGSN完成LTE与2/3G间跨RAT重选（包括RIM）、切换以及CSFB业务相关的网元间处理流程。|ZUF-78-16-013 S3
S102|MME提供S102协议接口用于MME和1xCS IWS之间的连接。|ZUF-78-16-014 S102
SGd|MME与SMC之间通过SGd协议接口互相连接。|ZUF-78-16-015 SGd
T6a|MME与SCEF之间通过T6a协议接口互相连接。|ZUF-78-16-016 T6a
## ZUF-78-16-001 S1-MME 
概述 :MME提供S1-MME接口用于MME和eNodeB之间的连接。 
收益 :MME通过S1-MME协议接口与eNodeB互连。 
描述 :该接口基于IP和S1AP。协议栈如[图1]所示。
图1  S1-MME接口协议栈

## ZUF-78-16-002 S6a 
特性描述 :特性描述 :术语 :无 
描述 :定义 :S6a口为MME与HSS之间接口，采用基于SCTP的Diameter协议栈。完成用户接入认证、插入用户签约数据、对用户接入PDN进行授权，与非3GPP系统互联时对用户的移动性管理消息的认证等功能。 
背景知识 :S6a口为MME与HSS网元之间的接口，采用IP物理连接，承载在SCTP偶联上。 
S6a口上Diameter消息包括有： 
位置更新消息(ULR/ULA) 
删除位置消息(CLR/CLA) 
清除用户消息(PUR/PUA) 
插入用户数据(IDR/IDA) 
删除用户数据(DSR/DSA) 
鉴权信息消息(AIR/AIA) 
重启消息(RSR/RSA) 
通知消息(NOR/NOA)  
应用场景 :概述 :MME与HSS之间可以直连，也可以通过DRA设备中转。MME与DRA、DRA与HSS之间同样采用Diameter协议。 
MME需作为SCTP偶联的客户端，DRA/HSS作为SCTP偶联的服务端。 
MME与HSS/EIR的组网一般可分为以下几种，以下组网可同时并存。 
组网模式|详细描述
---|---
无备份直连|MME与HSS网元直连，用户只关联一个主用HSS。
无备份通过DRA中转|MME发送消息通过DRA中转到达HSS，用户只关联一个主用HSS。
主备直连|MME与HSS/EIR网元直连，具有主备HSS，主用HSS故障时，消息发送给备用HSS。
主备通过DRA中转|MME发送消息通过DRA中转到达HSS，具有主备HSS，主用HSS故障时，消息发送给备用HSS。
###### 无备份直连 
无备份直连组网示意图如[图1]所示。
图1  无备份直连组网

UE发起业务，MME需向HSS/EIR发送Diameter消息，对用户IMSI1进行IMSI号码分析获得HSS局向，按照下面顺序依次查找，最终找到一条Diameter链路发送消息到HSS1。 
HSS局向-->Diameter局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路 
如到HSS1网元的链路都故障，则无法发送消息。 
###### 无备份通过DRA中转 
无备份通过DRA中转组网示意图如[图2]所示。
图2  无备份通过DRA中转示意图
UE发起业务，MME需向HSS/EIR发送Diameter消息，对用户IMSI1进行IMSI号码分析获得HSS局向，按照下面顺序依次查找，最终找到一条Diameter链路发送消息到DRA1，DRA1再进行转发，最后消息发送到HSS1。 
HSS局向-->Diameter局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路 
如到DRA1网元的链路都故障，则无法发送消息。 
###### 主备直连 
主备直连组网示意图如[图3]所示。
图3  主备直连组网示意图

UE发起业务，MME需向HSS/EIR发送Diameter消息，对用户IMSI1进行IMSI号码分析获得HSS局向，按照下面顺序依次查找，最终找到一条Diameter链路发送消息到主用HSS1。 
HSS局向-->Diameter局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路 
如到主用HSS1网元的链路都故障，则消息发送到备用HSS1。 
如到主用和备用HSS1网元链路都故障，则消息无法发送。 
###### 主备通过DRA中转 
主备通过DRA中转组网示意图如[图4]所示。
图4  主备通过DRA中转组网示意图

UE发起业务，MME需向HSS/EIR发送Diameter消息，对用户IMSI1进行IMSI号码分析获得HSS局向，按照下面顺序依次查找，最终找到一条Diameter链路发送消息到DRA1，DRA1再进行转发，最后消息发送到主用HSS1。 
HSS局向-->Diameter局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路 
如到DRA1网元的链路都故障，则消息发送到DRA3，DRA3再进行转发，最后消息发送到备用HSS1。 
如到DRA1和DRA3网元链路都故障，则消息无法发送。 
客户收益 :受益方|受益描述
---|---
运营商|MME使用S6a口与HSS共同完成对用户的鉴权认证，签约数据管理等。
移动用户|对终端用户不可见
实现原理 :涉及的网元 :本功能需要MME和HSS网元完成。 
网元名称|网元作用
---|---
MME|完成到HSS与EIR网元的Diameter链路的建立，在发送S6a消息时使用IMSI号码进行号码分析来获得HSS局向并向其发送Diameter消息，在发送S13消息时，只存在一个EIR局向直接向其发送Diameter消息。
HSS|存储用户的鉴权与签约数据，完成到MME之间Diameter链路的建立，为MME提供用户的鉴权和签约数据。
协议栈 :S6a口的协议栈如[图5]所示。
图5  S6a口协议栈

本网元实现 :ZXUN uMAC主要负责Diameter链路建立和发送Diameter消息两部分功能实现。
Diameter链路建立
Diameter链路建立示意图如[图6]所示。
图6  Diameter链路建立示意图

流程描述： 
MME发起SCTP偶联建立请求，完成与HSS/EIR/DRA之间的偶联建立。 
偶联建立成功后，MME发起Diameter链路建立能力交换请求，向HSS/EIR/DRA发送Diameter的CER消息，接收到对端的CEA响应
CEA响应可在Auth-Application-Id与Vendor-Specific-Application-Id字段中携带网元支持的能力，能力主要包括（支持S6a、S6d、S13或Relay能力），MME基于本地配置的能力与CEA响应中携带的能力取交集，如无交集则链路建立失败，如存在交集，本Diameter链路按照交集能力发送与接收Diameter消息，完成Diameter链路建立。 
Diameter链路建立后，MME定时发送Diameter的DWR消息，用于监测链路的状态。 
发送Diameter消息
发送Diameter消息示意图如[图7]所示。
图7  发送Diameter消息

流程描述： 
MME需要向HSS或EIR发送Diameter消息： 
如目标为HSS时，MME基于用户的IMSI进行号码分析得到HSS局向ID，再按照下面顺序依次查找，最终找到一条Diameter链路发送消息。HSS局向-->Diameter局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路如IMSI号码分析没有得到HSS局向ID，则使用默认Diameter局向路由发送消息。 
如目标为EIR时，之间从配置中获得EIR局向，同上逻辑获得Diameter链路发送消息。 
从Diameter链路上接收到响应消息，流程结束。 
业务流程 :位置更新流程
位置更新流程示意图如[图8]所示。
图8  位置更新流程

流程描述： 
UE发起附着或TAU流程，MME触发需到HSS进行位置更新流程，MME基于用户的IMSI进行号码分析得到HSS所在的Diameter链路，向HSS发送Update
Location Request消息。 
HSS发出Insert Subscription Data Request消息，将用户的签约数据通知给MME。 
MME本地保存签约数据，返回Insert Subscription Data Answer响应消息。 
HSS发送Update Location Answer消息，位置更新流程结束。 
鉴权流程
鉴权流程示意图如[图9]所示。
图9  鉴权流程

流程描述： 
UE发起附着或TAU流程，MME判断需要进行鉴权，向HSS发出Authentication Information Request消息申请用户的鉴权向量。 
HSS发出Authentication Information Answer响应消息，携带用户鉴权向量，MME保存在本地。 
故障恢复流程
故障恢复流程示意图如[图10]所示。
图10  故障恢复流程

流程描述： 
HSS发送故障恢复后，向MME发送Reset Request消息。 
MME记录下此HSS发生了重启，后续注册在此HSS中的用户发起业务时，MME触发位置更新流程到HSS，以便HSS重新获知用户当前所在的MME和位置信息。 
通知流程
通知流程示意图如[图11]所示。
图11  通知流程

流程描述： 
由于UE的终端信息发生改变，或UE所在PGW发生变化，MME构造Notify Request通知HSS。 
HSS记录携带的信息，返回Notify Answer消息，通知流程结束。 
IMEI检测流程
IMEI检测流程示意图如[图12]所示。
图12  IMEI检测流程

流程描述： 
UE发起附着或TAU流程，需检查IMEI的合法性，MME触发IMEI检测流程，向EIR发送ME Identity Check
Request消息。 
EIR检查IMEI的合法性，将结果在ME Identity Check Answer消息中携带通知MME，IMEI检测流程结束。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|-
3GPP TS 29.272: "Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".|-
RFC3588:"Diameter Base Protocol".|-
特性能力 :名称|指标
---|---
Diameter客户端|MME只支持作为Diameter客户端。
SCTP偶联|MME在S6a口和S13口中只支持作为SCTP偶联客户端。
HSS局向|MME最大支持1024个HSS局向。一个HSS局向最多有2个HSS邻接局路由，当配置2个邻接局路由时，这两个邻接局路由之间是主备关系。
EIR局向|MME只支持1个EIR局向。一个EIR局向最多有2个Diameter局向路由，当配置2个Diameter局向路由时，这两个局向路由之间是主备关系。
Diameter局向路由|MME最大支持1024个Diameter局向路由。一个Diameter局向路由中最多配置16个Diameter路由组，一个Diameter局向路由中支持基于优先级和权重选择Diameter路由组。
Diameter路由组|MME最大支持1024个Diameter路由组。一个Diameter路由组中最多配置2个Diameter路由，其中为主备或负荷分担关系。
Diameter路由|MME最大支持1024个Diameter路由。一个Diameter路由中最多配置2个Diameter链路组，其中为主备或负荷分担关系。
Diameter链路组|MME最大支持1024个Diameter链路组。一个Diameter链路组中最多配置16个Diameter链路，其中为N+M主备或负荷分担关系。如N+M主备时，配置的主用N的数目就是配置的链路中排在前面的N条链路，M条备用链路根据排列顺序优先级依次降低。
Diameter链路|MME最大支持2048个Diameter链路。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|-|-|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项表1  新增配置项配置项命令配置Diameter链路的SCTP承载链路ADD SCTPIDCFG配置Diameter连接ADD DIAMCONN配置Diameter链路组ADD DIAMLINKGROUP配置Diameter路由ADD DIAMROUTE配置Diameter路由组ADD DIAMROUTEGROUP配置Diameter邻接局路由ADD DIAMADJROUTE配置Diameter邻接局ADD DIAMADJ配置Diameter邻接局分析结果ADD DIMOFC ANALYSIS配置移动号码分析到HSS局向ADD MDNAL 
软件参数表2  新增软件参数软件参数ID软件参数名称65557是否开启主机名保存 
性能统计 :测量类型|描述
---|---
Diameter消息测量|编号为43202开头的所有计数器
告警和通知 :告警和通知
---
2114322677 Diameter路由不可用
2114322678 Diameter链路不可用
2114322545 收到HSS Reset
业务观察/失败观察 :能够查询到链路及路由状态，包括如下: 
使用SHOW DIMROUTE INFO命令查看路由组状态。Diameter链路状态：可用/不可用链路组状态：可用/不可用路由状态：可用/不可用，路由属性（是否支持3GPP能力\S6a\S13\Slg） 
使用CHG DIMCONNSTATUS命令可以对特定Diameter偶联进行释放和重建。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置实现S6a接口的正常通信。 
配置前提 :无 
配置过程 :本功能配置需按如下顺序依次执行： 
配置Diameter SCTP偶联 
配置Diameter链路 
配置Diameter链路组 
配置Diameter路由 
配置Diameter路由组 
配置Diameter邻接局路由 
配置Diameter邻接局 
配置Diameter邻接局分析结果索引 
配置到HSS局向的移动号码分析 
配置EIR局向 
配置HSS重启软参 
配置实例 :###### 无备份直连HSS 
场景描述
MME和一个HSS直接对接。 
配置步骤
步骤|操作
---|---
配置Diameter的SCTP链路|SIG模式下添加SCTP配置：ADD SCTP:ID=1,NAME="1",LOCPORT=3916,REMPORT=3916,VPNID1=2,LOCADDR1=40.33.150.6,REMADDR1=40.33.150.1,ROLE="CLT",PROTOCALTYPE="DIAMETER"MMESGSN模式下添加SCTP配置：ADD SCTPIDCFG:SCTPID=1,TYPE="DIM"
配置Diameter链路，并关联到已配置的SCTP链路|ADD DIAMCONN:ADJDOMAIN="zte.com.cn",SCTPID=1
创建Diameter信令链路组，将Diameter连接添加到Diameter链路组中|ADD DIAMLINKGROUP:LINKGRPID=1,SCTPLINKID=1,PARTAKEMODE="PARTAKE"
创建Diameter信令路由，将Diameter链路组添加到Diameter路由中|ADD DIAMROUTE:ROUTEID=1,LINKGRPID=1
创建Diameter信令路由组，将Diameter路由添加到Diameter路由组中|ADD DIAMROUTEGROUP:ROUTEGRPID=1,ROUTEID=1
创建Diameter局向路由，将Diameter路由组添加到局向路由中|ADD DIAMADJROUTE:ADJROUTEID=1,ROUTEGROUP=1-1-100,REALM="zte.com.cn"
创建Diameter局向，将Diameter局向路由中添加到邻接局中|ADD DIAMADJ:ADJID=1,ADJROUTEID=1
配置Diameter邻接局分析结果索引，为指定的HSS局向配置一个号码分析结果索引|ADD DIMOFC ANALYSIS:IDX=1,DIAMGRPID=1
配置归属到指定HSS局向的用户号段的号码分析|ADD MDNAL:DGT="45400",ENTR="DAS_IMSI_DIAMETER",RST=1
###### 主备HSS直连 
场景描述
MME和两个HSS直接对接，主备方式。 
配置步骤
步骤|操作
---|---
配置两条Diameter的SCTP链路|SIG模式下添加SCTP配置：ADD SCTP:ID=1,NAME="1",LOCPORT=3916,REMPORT=3916,VPNID1=2,LOCADDR1=40.33.150.6,REMADDR1=40.33.150.1,ROLE="CLT",PROTOCALTYPE="DIAMETER"ADD SCTP:ID=2,NAME="2",LOCPORT=3916,REMPORT=3916,VPNID1=2,LOCADDR1=40.33.150.7,REMADDR1=40.33.150.2,ROLE="CLT",PROTOCALTYPE="DIAMETER"MMESGSN模式下添加SCTP配置：ADD SCTPIDCFG:SCTPID=1,TYPE="DIM"ADD SCTPIDCFG:SCTPID=2,TYPE="DIM"
配置Diameter链路，并关联到已配置的SCTP链路|ADD DIAMCONN:ADJDOMAIN="zte.com.cn",SCTPID=1ADD DIAMCONN:ADJDOMAIN="zte.com.cn",SCTPID=2
创建Diameter信令链路组，将Diameter连接添加到Diameter链路组中|ADD DIAMLINKGROUP:LINKGRPID=1,SCTPLINKID=1,PARTAKEMODE="PARTAKE"ADD DIAMLINKGROUP:LINKGRPID=2,SCTPLINKID=2,PARTAKEMODE="PARTAKE"
创建Diameter信令路由，将Diameter链路组添加到Diameter路由中|ADD DIAMROUTE:ROUTEID=1,LINKGRPID=1ADD DIAMROUTE:ROUTEID=2,LINKGRPID=2
创建Diameter信令路由组，将Diameter路由添加到Diameter路由组中|ADD DIAMROUTEGROUP:ROUTEGRPID=1,ROUTEID=1ADD DIAMROUTEGROUP:ROUTEGRPID=2,ROUTEID=2
创建Diameter局向路由，将Diameter路由组添加到局向路由中|ADD DIAMADJROUTE:ADJROUTEID=1,ROUTEGROUP=1-1-100,REALM="zte.com.cn"ADD DIAMADJROUTE:ADJROUTEID=2,ROUTEGROUP=2-1-100,REALM="zte.com.cn"
创建Diameter局向，将Diameter局向路由中添加到邻接局中|ADD DIAMADJ:ADJID=1,ADJROUTEID=1&2
配置Diameter邻接局分析结果索引，为指定的HSS局向配置一个号码分析结果索引|ADD DIMOFC ANALYSIS:IDX=1,DIAMGRPID=1
配置归属到指定HSS局向的用户号段的号码分析|ADD MDNAL:DGT="45400",ENTR="DAS_IMSI_DIAMETER",RST=1
###### 无备份通过DRA中转 
场景描述
MME和HSS间通过DRA中转。 
配置步骤
步骤|操作
---|---
配置Diameter的SCTP链路|SIG模式下添加SCTP配置：ADD SCTP:ID=1,NAME="1",LOCPORT=3916,REMPORT=3916,VPNID1=2,LOCADDR1=40.33.150.6,REMADDR1=40.33.150.1,ROLE="CLT",PROTOCALTYPE="DIAMETER"MMESGSN模式下添加SCTP配置：ADD SCTPIDCFG:SCTPID=1,TYPE="DIM"
配置Diameter链路，并关联到已配置的SCTP链路，主机名配置为DRA局向的主机名|ADD DIAMCONN:ADJDOMAIN="dra.com.cn",SCTPID=1
创建Diameter信令链路组，将Diameter连接添加到Diameter链路组中|ADD DIAMLINKGROUP:LINKGRPID=1,SCTPLINKID=1,PARTAKEMODE="PARTAKE"
创建Diameter信令路由，将Diameter链路组添加到Diameter路由中|ADD DIAMROUTE:ROUTEID=1,LINKGRPID=1
创建Diameter信令路由组，将Diameter路由添加到Diameter路由组中|ADD DIAMROUTEGROUP:ROUTEGRPID=1,ROUTEID=1
创建Diameter局向路由，将Diameter路由组添加到局向路由中，注意此处的域名REALM为对接HSS的主机名域名|ADD DIAMADJROUTE:ADJROUTEID=1,ROUTEGROUP=1-1-100,REALM="zte.com.cn"
创建Diameter局向，将Diameter局向路由中添加到邻接局中|ADD DIAMADJ:ADJID=1,ADJROUTEID=1
配置Diameter邻接局分析结果索引，为指定的HSS局向配置一个号码分析结果索引|ADD DIMOFC ANALYSIS:IDX=1,DIAMGRPID=1
配置归属到指定HSS局向的用户号段的号码分析|ADD MDNAL:DGT="45400",ENTR="DAS_IMSI_DIAMETER",RST=1
###### 主备HSS通过DRA中转 
场景描述
MME和主备HSS间通过两个DRA直接对接，DRA负荷分担方式。 
配置步骤
步骤|操作
---|---
配置两条Diameter的SCTP链路|SIG模式下添加SCTP配置：ADD SCTP:ID=1,NAME="1",LOCPORT=3916,REMPORT=3916,VPNID1=2,LOCADDR1=40.33.150.6,REMADDR1=40.33.150.1,ROLE="CLT",PROTOCALTYPE="DIAMETER"ADD SCTP:ID=2,NAME="2",LOCPORT=3916,REMPORT=3916,VPNID1=2,LOCADDR1=40.33.150.7,REMADDR1=40.33.150.2,ROLE="CLT",PROTOCALTYPE="DIAMETER"MMESGSN模式下添加SCTP配置：ADD SCTPIDCFG:SCTPID=1,TYPE="DIM"ADD SCTPIDCFG:SCTPID=2,TYPE="DIM"
配置Diameter链路，并关联到已配置的SCTP链路，注意此处配置的主机名为DRA局向的主机名|ADD DIAMCONN:ADJDOMAIN="dra.com.cn",SCTPID=1ADD DIAMCONN:ADJDOMAIN="dra.com.cn",SCTPID=2
创建Diameter信令链路组，将Diameter连接添加到Diameter链路组中|ADD DIAMLINKGROUP:LINKGRPID=1,SCTPLINKID=1,PARTAKEMODE="PARTAKE"ADD DIAMLINKGROUP:LINKGRPID=2,SCTPLINKID=2,PARTAKEMODE="PARTAKE"
创建Diameter信令路由，将Diameter链路组添加到Diameter路由中|ADD DIAMROUTE:ROUTEID=1,LINKGRPID=1ADD DIAMROUTE:ROUTEID=2,LINKGRPID=2
创建Diameter信令路由组，将Diameter路由添加到Diameter路由组中|ADD DIAMROUTEGROUP:ROUTEGRPID=1,ROUTEID=1ADD DIAMROUTEGROUP:ROUTEGRPID=2,ROUTEID=2
创建Diameter局向路由，将Diameter路由组添加到局向路由中，注意此处的域名REALM为对接HSS的域名|ADD DIAMADJROUTE:ADJROUTEID=1,ROUTEGROUP=1-1-100,REALM="zte.com.cn"ADD DIAMADJROUTE:ADJROUTEID=2,ROUTEGROUP=2-1-100,REALM="zte.com.cn"
创建Diameter局向，将Diameter局向路由中添加到邻接局中|ADD DIAMADJ:ADJID=1,ADJROUTEID=1&2
配置Diameter邻接局分析结果索引，为指定的HSS局向配置一个号码分析结果索引|ADD DIMOFC ANALYSIS:IDX=1,DIAMGRPID=1
配置归属到指定HSS局向的用户号段的号码分析|ADD MDNAL:DGT="45400",ENTR="DAS_IMSI_DIAMETER",RST=1
###### HSS主叫名保存功能 
场景描述
开启MME的HSS主机名保存功能，MME接收到HSS响应消息，保存其中的HSS主机名，后续发送消息使用此主机名。 
配置步骤
步骤|操作
---|---
开启HSS主叫名保存功能开关|SET SOFTWARE PARAMETER:PARAID=65557,PARAVALUE=1
调整特性 :无 
测试用例 :###### 归属对接HSS的用户附着，无备份直连 
测试项目|归属对接HSS的用户附着，无备份直连
测试目的|对接的直连HSS在用户接入过程中能正常处理与MME的交互
预置条件|MME与HSS直连对接成功。用户在HSS上签约并签约了EPS业务。
测试过程|用户向MME发起附着请求。
通过准则|用户附着成功，附着过程中与HSS的鉴权请求和位置更新等交互正常完成
测试结果|–
###### 归属对接HSS的用户附着，无备份通过DRA转接 
测试项目|归属对接HSS的用户附着，无备份通过DRA转接
测试目的|对接的HSS在用户接入过程中能正常处理与MME的交互
预置条件|MME与HSS直连对接成功。用户在HSS上签约并签约了EPS业务。
测试过程|用户向MME发起附着请求。
通过准则|用户附着成功，附着过程中与HSS的鉴权请求和位置更新等交互正常完成
测试结果|–
常见问题处理 :链路不通 
一般都是配置错误引起，前台可以通过[SHOW SCTP]与[SHOW SCTPIDCFG]查看建链的数据与配置的是否一致。
若配置数据没问题，可以通过抓包工具或者前台提供的命令查看底层SCTP链路是否建立。 
常用命令：[SHOW ALLSCTPSTAT]可以查看底层SCTP是否建立成功。
使用DRA局向进行转接时，与HSS局向对接不通问题 
可以检查Diameter局向路由配置（[SHOW DIAMADJROUTE]）中“域名”和“主机名”参数是否与对接的HSS一致。此处注意不能配置为Diameter连接配置中的“域名”和“主机名”，这里的配置是用来和转接DRA局向对接的。
Diameter链路协商能力失败 
可以检查Diameter路由配置中（[SHOW DIAMROUTE]），”路由协商本端能力”是否合对端一致。
## ZUF-78-16-003 S11 
概述 :MME提供S11协议接口用于MME和SGW之间的连接。 
收益 :MME通过S11协议接口与SGW互连。 
描述 :该接口基于IP和GTPC。协议栈如[图1]所示。
图1  S11接口协议栈

## ZUF-78-16-004 S10 
概述 :MME提供S10协议接口用于MME间的连接。 
收益 :MME通过S10协议接口与其他MME互连。 
描述 :该接口基于IP和GTPC。协议栈如[图1]所示。
图1  S10接口协议栈

## ZUF-78-16-005 GnGp 
概述 :MME提供基于IP的Gn/Gp协议接口。 
收益 :MME通过基于IP的Gn/Gp协议接口与pre-R8 GSN互联以完成LTE用户在2G/3G网络的移动性功能。 
描述 :该接口基于IP和GTPC。协议栈如[图1]所示。
图1  GnGp接口协议栈

## ZUF-78-16-006 S13 
S13是MME和EIR之间的接口。该接口使用基于SCTP的Diameter协议栈。S13接口对UE进行IMEI合法性检测。 
## ZUF-78-16-007 SGs 
概述 :MME提供SGs协议接口用于MME和MSC-S之间的连接。 
收益 :MME通过SGs协议接口与MSC-S连接以完成CSFB功能。 
描述 :该接口基于IP、SCTP和SGsAP。协议栈如[图1]所示。
图1  SGs接口协议栈

## ZUF-78-16-008 Sv 
概述 :MME提供Sv协议接口用于MME和MSC-S之间的连接。 
收益 :MME通过Sv接口和MSC-S交互，以实现SRVCC功能，完成VoLTE语音切换。 
描述 :该接口基于IP，UDP和GTPv2。协议栈如[图1]所示。
图1  Sv接口协议栈

## ZUF-78-16-009 SLg 
概述 :MME提供SLg协议接口用于MME和GMLC之间的连接。 
收益 :MME通过SLg协议接口和GMLC交互以完成LCS功能。 
描述 :该接口基于IP、SCTP和Diameter。协议栈如[图1]所示。
图1  SLg接口协议栈

## ZUF-78-16-010 SLs 
概述 :MME提供SLs协议接口用于MME和E-SMLC之间的连接。 
收益 :MME通过SLs协议接口和E-SMLC交互以完成LCS功能。 
描述 :该接口基于IP、SCTP和LCS-AP。协议栈如[图1]所示。
图1  SLs接口协议栈

## ZUF-78-16-011 Sm 
概述 :MME提供Sm协议接口用于MME和MBMS GW之间的连接。 
收益 :MME通过Sm协议接口和MBMS GW交互以完成eMBMS功能。 
描述 :该接口基于IP、UDP和GTPv2。协议栈如[图1]所示。
图1  Sm接口协议栈

## ZUF-78-16-012 M3 
概述 :MME提供M3协议接口用于MME和MCE之间的连接。 
收益 :MME通过M3协议接口和MCE交互以完成eMBMS功能。 
描述 :该接口基于IP、SCTP和M3AP。协议栈如[图1]所示。
图1  M3接口协议栈

## ZUF-78-16-013 S3 
特性描述 :特性描述 :描述 :定义 :MME和S3/S4 SGSN之间的接口为S3接口，传输控制面信息。
S3接口主要应用于跨RAT流程中MME和S3/S4 SGSN的交互。跨RAT流程主要应用于运营商EPS网络与GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 
背景知识 :MME支持S3接口，即MME提供与S3/S4 SGSN之间的接口，完成LTE与2/3G间跨RAT重选（包括RIM）、切换以及CSFB业务相关的网元间处理流程。
应用场景 :###### 跨RAT重选 
GERAN/UTRAN与E-UTRAN之间的RAU/TAUUE在GERAN/UTRAN下由S3/S4 SGSN提供服务。UE由S3/S4 SGSN TAU到MME，以及从MME RAU到S3/S4 SGSN。 
MME与S4 SGSN之间的局间附着UE在GERAN/UTRAN下由S3/S4 SGSN提供服务。UE附着到MME，老局为S3/S4
SGSN；以及UE附着到S3/S4 SGSN，老局为MME。 
SGSN与MME间的RIMUE采用NACC的方式进行跨RAT重选，RAN侧通过S3/S4
SGSN和MME传递相关信息。 
###### 跨RAT切换 
UE在UTRAN下由S3/S4 SGSN提供服务；UE在UTRAN与E-UTRAN之间做跨RAT切换。 
###### CSFB/SRVCC 
UE在CSFB或SRVCC流程中回落到2/3G需要将数据业务挂起；S3/S4
SGSN发送SUSPEND消息给MME。 
客户收益 :受益方|受益描述
---|---
运营商|MME支持S3口，提高了网络互通性和兼容性，能够方便的与本网或者其他网的S3/S4SGSN对接，实现用户的跨RAT业务。
移动用户|对终端用户不可见。
实现原理 :系统架构 :EPS网络架构如[图1]所示。
图1  EPS网络架构图

涉及的网元 :名称|功能
---|---
UTRAN|UMTS陆地无线接入网|第三代移动通讯网络的无线接入网络，由RNC和NodeB组成，为终端的接入提供无线资源。
GERAN|GSM/EDGE无线接入网|GSM/EDGE的无线接入系统，由BSC和BTS组成，为终端的接入提供无线资源。
E-UTRAN|演进的通用陆地无线接入网络|E-UTRAN包含的设备是eNodeB，为终端的接入提供无线资源。可以提供更高的上下行速率，更低的传输延迟和更加可靠的无线传输。
HSS|归属用户服务器|HSS用于存储用户签约信息和鉴权数据。
MME|移动性管理实体|MME作为EPS系统中负责处理信令的功能实体，是临时存储用户数据的服务器，主要完成EPC网络的移动性管理、承载管理、切换管理、安全管理等功能，并协助eNodeB、SGW和PGW之间的分组数据转发。
SGW|服务网关|SGW是用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE下行数据；管理和存储UE的SAE承载上下文，是3GPP系统内部用户面的锚点。
PGW|分组数据网网关|PGW负责UE接入PDN，并为用户分配IP地址，同时也是3GPP和非3GPP接入系统的移动性锚点。
PCRF|策略和计费规则功能实体|PCRF主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的QoS规则以及计费规则，同时负责控制承载的建立和释放。
协议栈 :S3协议栈如[图2]所示。
图2  S3协议栈

S3口上的GTP-C消息包括有： 
业务类型|消息名称
---|---
切换|Forward Relocation Request
Forward Relocation Response|切换
Forward Relocation Complete Notification|切换
Forward Relocation Complete Acknowledge|切换
Relocation Cancel Request|切换
Relocation Cancel Response|切换
用户和承载信息传递|Context Request
Context Response|用户和承载信息传递
Context Acknowledge|用户和承载信息传递
Identification Request|用户和承载信息传递
Identification Response|用户和承载信息传递
无线信息传递|RAN Information Relay
挂起|Suspend Notification
Suspend Acknowledge|挂起
本网元实现 :MME通过S3口与S3/S4 SGSN共同完成UE的跨RAT业务流程；负责管理和存储和传递UE的相关信息，实现S3/S4
SGSN的选择等功能。 
业务流程 :E-UTRAN初始附着
E-UTRAN初始附着流程如[图3]所示。
图3  E-UTRAN初始附着

如果UE通过GUTI标识自身并且去附着后MME变了，新MME判断老节点的类型，使用UE发送的GUTI提取老SGSN的地址，向老SGSN发送Identification
Request获取IMSI。 
老SGSN使用P-TMSI签名验证 Attach Request消息，返回Identification Response。 
UTRAN/GERAN初始附着
UTRAN/GERAN初始附着流程如[图4]所示。
图4  UTRAN/GERAN初始附着

如果MS通过 P-TMSI标识自身并且去附着后MME变了，新SGSN向老MME发送Identification Request获取IMSI。 
老MME返回Identification Response。 
跨RAT跟踪区更新
跨RAT跟踪区更新流程如[图5]所示。
图5  跨RAT跟踪区更新

新MME识别出老节点类型，使用UE发送的GUTI提取老S3/S4 SGSN的地址，向老S3/S4 SGSN发送Context
Request消息获取用户信息。 
老S3/S4 SGSN返回Context Response。 
新MME发送Context Acknowledge消息给老S3/S4 SGSN。 
跨RAT路由区更新
跨RAT路由区更新流程如[图6]所示。
图6  跨RAT路由区更新

新S3/S4 SGSN判断老节点的类型，使用UE发送的老RAI提取老MME的地址，向老MME发送Context Request
消息获取该UE的上下文。 
老MME使用P-TMSI签名映射的NAS令牌来验证 Context Request。如果老MME验证通过该UE，老MME触发定时器，并返回Context
Response消息。 
新SGSN向老MME发送Context Acknowledge消息。当定时器结束时，老MME删除该UE所有的承载资源。 
RIM
MME从eNodeB收到RAN信息后，通过RAN Information Relay消息发送给S3/S4 SGSN，如[图7]所示。
图7  发送RAN Information Relay消息给S3/S4 SGSN

S3/S4 SGSN从BSS或RNS收到RAN信息后，通过RAN Information Relay消息发送给MME，如[图8]所示。
图8  发送AN Information Relay消息给MME

E-UTRAN到UTRAN Iu模式的RAT间切换
E-UTRAN到UTRAN Iu模式的RAT间切换流程如[图9]和[图10]所示。
图9  E-UTRAN到UTRAN Iu模式的RAT间切换（1）

源MME根据Target RNC Identifier信元判断切换类型为到UTRAN Iu模式的RAT间切换，向目标S3/S4
SGSN发送Forward Relocation Request消息发起切换资源分配流程。 
目标S3/S4 SGSN向源MME返回Forward Relocation Response消息。 
目标S3/S4 SGSN得知UE到达目标方后，通过Forward Relocation Complete Notification消息通知源MME。 
源MME向目标S3/S4 SGSN返回Forward Relocation Complete Acknowledge消息。 
图10  E-UTRAN到UTRAN Iu模式的RAT间切换（2）

源MME根据Target RNC Identifier信元判断切换类型为到UTRAN Iu模式的RAT间切换，向目标S3/S4
SGSN发送Forward Relocation Request消息发起切换资源分配流程。 
如果目标RNC向被请求的无线接入承载分配资源失败，目标RNC向目标S3/S4 SGSN发送Relocation Failure
(Cause)消息。目标S3/S4 SGSN收到该消息后，清除为该UE预留的所有资源，并向源MME发送Forward Relocation
Response (Cause)消息。 
UTRAN Iu模式到E-UTRAN的RAT间切换
UTRAN Iu模式到E-UTRAN的RAT间切换流程如[图11]和[图12]所示。
图11  UTRAN Iu模式到E-UTRAN的RAT间切换（1）

源S3/S4 SGSN根据Target eNodeB Identifier信元判断切换类型为到E-UTRAN的RAT间切换，向目标MME发送Forward
Relocation Request消息发起切换资源分配流程。 
目标MME向源S3/S4 SGSN返回Forward Relocation Response消息。 
目标MME得知UE到达目标方后，通过Forward Relocation Complete Notification消息通知源S3/S4
SGSN。 
源S3/S4 SGSN向目标MME返回Forward Relocation Complete Acknowledge消息。 
图12  UTRAN Iu模式到E-UTRAN的RAT间切换（2）

源S3/S4 SGSN根据Target eNodeB Identifier信元判断切换类型为到E-UTRAN的RAT间切换，向目标MME发送Forward
Relocation Request消息发起切换资源分配流程。 
如果目标eNodeB向被请求的EPS承载分配资源失败，目标eNodeB向目标MME发送Handover Failure
(Cause) 消息。目标MME收到该消息后，清除为该UE预留的所有资源，并向源S3/S4 SGSN发送Forward Relocation
Response (Cause) 消息。 
RAT间切换取消
RAT间切换取消流程如[图13]和[图14]所示。
图13  RAT间切换取消（1）

源MME向目标S3/S4 SGSN发送Forward Cancel Request消息终止向目标方的重定位，同时恢复对源方资源的操作。 
目标S3/S4 SGSN向源MME返回Forward Cancel Response (Cause) 消息，确认目标方的所有资源已经释放。 
图14  RAT间切换取消（2）

源S3/S4 SGSN向目标MME发送Forward Cancel Request消息终止向目标方的重定位，同时恢复对源方资源的操作。 
目标MME向源S3/S4 SGSN返回Forward Cancel Response (Cause)消息，确认目标方的所有资源已经释放。 
挂起
挂起流程如[图15]所示。
图15  挂起

UE在SRVCC或CS回落流程中触发挂起流程后，S3/S4 SGSN向MME发送 Suspend Notification消息。 
即使无法从P-TMSI和RAI对中获取GUTI，MME仍然向SGSN返回Suspend Acknowledge消息。 
系统影响 :S3接口主要涉及的是跨RAT业务。使用S3口对系统性能无额外的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
". 
3GPP TS 29.274: "3GPP Evolved Packet System (EPS); Evolved
General Packet Radio Service (GPRS) Tunnelling Protocol for Control
plane (GTPv2-C); Stage 3". 
特性能力 :MME并未对使用S3接口的GSN节点数目做特别限制。 
可获得性 :License要求 :License ID|License控制值|License描述
---|---|---
7055|ON|MME支持S3接口
对其他网元的要求 :网元|要求
---|---
MME|遵循3GPP 29.274协议，无特殊要求。
S3/S4 SGSN|遵循3GPP 29.274协议，无特殊要求。
工程规划要求 :通常情况下，MME可只配置一个GTP-C地址，但当需要隔离S3接口的业务网络、让接口信令/数据在不同的虚拟路由域内传输时，可以为S3接口配置独立的VRF。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令EPC地址解析配置ADD EPCHOSTSET EPCHOSTADD EPCHOST IPADDRDEL EPCHOST IPADDRDEL EPCHOSTSHOW EPCHOSTVRF配置SET VRFCFGSHOW VRFCFG 
安全变量该特性不涉及安全变量的变化。 
软件参数表2  新增软件参数软件参数ID软件参数名称65617MME支持RIM RNC-ID解析65542SGSN是否支持RIM功能262283MME RIM流程获取目标SGSN IP时采用的域名格式 
动态管理GSN节点链路检测目前GSN节点链路检测，可以指定源地址、目的地址、GTP协议版本号、接口类型，在原有动态命令的接口类型中增加了S3
的接口类型，具体命令如下：GTP ECHO:SRCIP="192.20.155.1",DESIP="192.20.191.1",GTPPRO="GTPV2",ITYPE="
S3"; DNS查询对前台发起DNS 查询流程，模拟MME业务发起DNS查询。DNS LOOKUP:MODULE=2,SERVERGROUP="EPC",DOMAINNAME="rnc000b.rnc.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgsn",PROTOCOL="x-s3"; 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :在MME侧配置支持S3接口信息。 
配置前提 :eNodeB已与MME对接成功，相应TAI-FQDN解析完成，4G下能附着成功。 
BSC/RNC已与S3/S4 SGSN对接成功，相应APN-FQDN解析完成，2G/3G下能附着、激活。 
RNC/BSC与eNodeB无线网元之间的重选、切换配置均已完成。 
配置过程 :配置2G/3G到4G的TAU信息。 
配置2G/3G到4G的局间附着信息。 
配置4G到3G的RIM信息。 
配置4G到2G的RIM信息。 
配置4G到3G的切换信息。 
配置实例 :###### 配置2G/3G到4G的TAU 
用户从S3/S4 SGSN下TAU至MME，用户在S3/S4
SGSN下的LAC为1001（十六进制）、RAC为01、PLMN为46011。 
DNS服务器已配置zone，包括： 
zone " rac.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file "zone.rac.epc.mnc011.mcc460 " } 
zone " node.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.node.epc.mnc011.mcc460 " } 
在DNS服务器上配置old RAI解析到S3/S4 SGSN的GTPC地址： 
在file “zone.rac.epc.mnc011.mcc460”中配置RR记录：
`IN   NAPTR order  pref.  flag     service     regexp 	replacement 
rac0001.lac1001  IN   NAPTR  100    100    "a"   "x-3gpp-sgsn:x-s3 "   "" 
 topoff.s3.sgsn01.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org.
` 
在file “zone.node.epc.mnc011.mcc460”中配置RR记录：
`topoff.s3.sgsn01.nj.js      IN   A   1.1.1.1` 
###### 2G/3G到4G的局间附着 
用户从S3/S4 SGSN下局间附着至MME，用户在S3/S4
SGSN下的LAC为1002（十六进制），RAC为02、PLMN为46011。 
DNS服务器已配置zone，包括： 
zone " rac.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.rac.epc.mnc011.mcc460 " } 
zone " node.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.node.epc.mnc011.mcc460 " } 
在DNS服务器上配置old RAI解析到S3/S4 SGSN的GTPC地址： 
在file “zone.rac.epc.mnc011.mcc460”中配置RR记录：
`IN   NAPTR order  pref.  flag     service     regexp 	replacement 
rac0002.lac1002  IN   NAPTR  100    100    "a"   "x-3gpp-sgsn:x-s3 "   "" 
 topoff.s3.sgsn02.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org.
` 
在file “zone.node.epc.mnc011.mcc460”中配置RR记录：
`topoff.s3.sgsn02.nj.js      IN   A   1.1.1.2` 
###### 4G到3G的RIM 
eNodeB发起4G到3G的RIM流程，携带Target ID为目标RNC
ID，MME使用RNC ID的EPS域名格式解析S3/S4 SGSN地址。RNCID为200（十进制）、PLMN为46011。 
DNS服务器已配置zone，包括： 
zone " rnc.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.rnc.epc.mnc011.mcc460 "} 
zone " node.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.node.epc.mnc011.mcc460 " } 
配置方法： 
在MME网元上打开支持4G到3G RIM开关： 
[SET SOFTWARE PARAMETER]:PARAID=65617,PARAVALUE=1
在MME网元上配置使用EPS格式解析S3/S4 SGSN地址： 
[SET SOFTWARE
PARAMETER]:PARAID=262283,PARAVALUE=1
在DNS服务器上配置RNCID FQDN解析到S3/S4 SGSN的GTPC地址。 
在file “zone.rac.epc.mnc011.mcc460”中配置RR记录：
`IN   NAPTR order  pref.  flag     service     regexp 	replacement 
rnc00c8  IN   NAPTR  100    100    "a"  "x-3gpp-sgsn:x-s3"   "" 
 topoff.s3.sgsn03.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org.
` 
在file “zone.node.epc.mnc011.mcc460”中配置RR记录：
`topoff.s3.sgsn03.nj.js      IN   A   1.1.1.3` 
###### 4G到2G的RIM 
eNodeB发起4G到2G的RIM流程，携带Target ID为目标Cell
ID，MME使用RAI的EPS域名格式解析S3/S4 SGSN地址。LAC为1003（十六进制）、RAC为03（十六进制）。 
DNS服务器已配置zone，包括： 
zone " rac.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.rac.epc.mnc011.mcc460 " } 
zone " node.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.node.epc.mnc011.mcc460 " } 
配置方法： 
配置使用EPS格式的RAI FQDN解析S3/S4 SGSN地址： 
[SET SOFTWARE
PARAMETER]:PARAID=262283,PARAVALUE=1
在DNS服务器上配置RAI FQDN解析到S3/S4 SGSN的GTPC地址： 
在file “zone.rac.epc.mnc011.mcc460”中配置RR记录：
`IN   NAPTR order  pref.  flag     service     regexp 	replacement 
rac0003.lac1003  IN   NAPTR  100    100    "a"   "x-3gpp-sgsn:x-s3 "   "" 
 topoff.s3.sgsn04.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org.
` 
在file “zone.node.epc.mnc011.mcc460”中配置RR记录：
`topoff.s3.sgsn04.nj.js      IN   A   1.1.1.4` 
在S3/S4 SGSN网元上打开RIM开关： 
[SET SOFTWARE PARAMETER]:PARAID=65542,PARAVALUE=1
###### 4G到3G的切换 
用户从MME下切换至S3/S4 SGSN，目标RNCID为200。 
DNS服务器已配置zone，包括： 
zone " rnc.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.rnc.epc.mnc011.mcc460 " } 
zone " node.epc.mnc011.mcc460.3gppnetwork.org" { type master;
file " zone.node.epc.mnc011.mcc460 " } 
在DNS服务器上配置RNC ID解析到S3/S4 SGSN的GTPC地址： 
在file “zone.rac.epc.mnc011.mcc460”中配置RR记录：
`IN   NAPTR order  pref.  flag     service     regexp 	replacement 
rnc00c8  IN   NAPTR  100    100    "a"  "x-3gpp-sgsn:x-s3"   "" 
 topoff.s3.sgsn05.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org.
` 
在file “zone.node.epc.mnc011.mcc460”中配置RR记录：
`topoff.s3.sgsn05.nj.js      IN   A   1.1.1.5` 
测试用例 :###### 3G到4G的TAU 
测试项目|3G到4G的TAU
测试目的|验证S3/S4SGSN、MME能正确处理3G到4G的TAU。
预置条件|LTE、3G网络内的所有网元运行正常，OMM维护正常。用户在HSS/HLR开户，并签约2G/3G业务和LTE业务。打开消息跟踪工具。
测试过程|用户附着到3G网络。用户发起FTP业务，并一直保持。用户移动到LTE网络覆盖区域，发起TAU流程。检查网络侧用户信息和测试信令
通过准则|用户在3G附着成功。用户正常进行FTP下载。TAU请求消息中携带GUTI等参数。创建缺省承载成功。MME/SGSN向HSS/HLR发起Update Location流程。HSS/HLR向MME/SGSN发起Cancel Location流程。用户在LTE附着成功。FTP业务能够继续。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|—
###### 3G到4G的局间附着 
测试项目|3G到4G的局间附着
测试目的|验证S3/S4SGSN、MME能正确处理3G到4G的局间附着。
预置条件|LTE,3G网络内的所有网元运行正常，OMM维护正常、用户在HSS/HLR开户，并签约2G/3G业务和LTE业务。打开消息跟踪。
测试过程|用户附着到3G网络。用户发起FTP业务，并一直保持。用户移动到LTE网络覆盖区域，发起局间附着流程。检查网络侧用户信息和测试信令。
通过准则|用户在3G附着成功。用户正常进行FTP下载。局间附着请求消息中携带GUTI等参数。创建缺省承载成功。MME/SGSN向HSS/HLR发起Update Location流程。HSS/HLR向MME/SGSN发起Cancel Location流程。用户在LTE附着成功。FTP业务能够继续。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|—
###### 4G到3G的RIM 
测试项目|4G到3G的RIM
测试目的|验证E-UTRAN到UTRAN的RIM，S3/S4SGSN、MME能够正确处理。
预置条件|EPS、GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB和MME上配好了到PS的RIM的相关配置。在S3/S4 SGSN和MME上建立信令跟踪。
测试过程|eNodeB发起4G到3G的RIM流程，Target ID携带目标RNC ID。在MME和S3/S4 SGSN上检查信令流程。
通过准则|MME收到eNodeB的RIM消息后，通过解析获取目标S3/S4 SGSN地址，并将RIM消息转发给S3/S4 SGSN。S3/S4 SGSN收到MME的RIM消息，根据目标ID查找目标RNC，并将RIM消息转发给目标RNC。
测试结果|—
###### 4G到2G的RIM 
测试项目|4G到2G的RIM
测试目的|验证E-UTRAN到GERAN的RIM，S3/S4SGSN、MME能够正确处理。
预置条件|EPS、GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB和MME上配好了到PS的RIM的相关配置。在S3/S4 SGSN和MME上建立信令跟踪。
测试过程|eNodeB发起4G到2G的RIM流程，Target ID携带目标Cell ID。在MME和S3/S4 SGSN上检查信令流程。
通过准则|MME收到eNodeB的RIM消息后，通过解析获取目标S3/S4 SGSN地址，并将RIM消息转发给SGSN。S3/S4 SGSN收到MME的RIM消息，根据目标ID查找目标BSC，并将RIM消息转发给目标BSC。
测试结果|—
###### 4G到3G的切换 
测试项目|4G到3G的切换
测试目的|验证E-UTRAN到UTRAN的切换，S3/S4SGSN、MME能够正确处理。
预置条件|EPS，GPRS网络中各网元系统及操作维护台运行正常。用户已经签约GPRS和EPS业务。eNodeB上配好了到GPRS的Handover的相关配置。UE已经通过eNodeB附着到EPS网络，且正在进行数据业务。在MME上建立S1接口跟踪，用户跟踪，GTPC跟踪。PDN GW支持GGSN功能。
测试过程|UE逐渐从eNodeB覆盖区移动到RNC覆盖区，Source eNodeB触发Handover流程。在网络侧查询用户的信息。
通过准则|Handover流程成功。切换之后数据业务正常。MME上没有用户的信息，S3/S4 SGSN上用户状态为connected状态。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|—
## ZUF-78-16-014 S102 
概述 :MME提供S102协议接口用于MME和1xCS IWS之间的连接。 
收益 :MME通过S102协议接口与1xCS IWS相连接。 
描述 :该接口基于IP、UDP和IOS A21。协议栈如[图1]所示。
图1  S102接口协议栈

## ZUF-78-16-015 SGd 
概述 :MME提供SGd协议接口，用来与为SMC进行连接。 
收益 :MME与SMC之间通过 SGD协议接口互相连接。 
说明 :该接口基于IP，SCTP和Diameter协议。 
## ZUF-78-16-016 T6a 
概述 :MME提供T6a协议接口，用于与SCEF之间进行连接。 
收益 :MME与SCEF之间通过 T6a协议接口互相连接。 
说明 :该接口基于IP和Diameter协议。 
## ZUF-78-16-017 SBc 
描述 :SBc接口是MME和CBC之间的接口，用于MME和CBC之间进行告警消息传递。
实现原理 :涉及的网元 :涉及的NF/网元参见[表1]。
NF/网元|说明
---|---
MME|接收CBC发送的告警发送、告警取消消息，并转发至eNodeB。接收eNodeB发送的PWS重启、故障指示消息，并转发至CBC。
CBC|向MME发送告警发送、告警取消消息。接收MME转发的PWS重启、故障指示消息。
协议栈 :SBc接口协议栈如[图1]所示。
图1  SBc接口协议栈

消息描述 :SBc接口支持的消息参见[表2]。
消息名称|方向|说明
---|---|---
WRITE-REPLACE WARNING REQUEST|CBC-> MME|CBC向MME发送告警发送请求消息。
WRITE-REPLACE WARNING RESPONSE|MME-> CBC|MME向CBC回复告警发送响应消息。
STOP WARNING REQUEST|CBC-> MME|CBC向MME发送告警停止请求消息。
STOP WARNING RESPONSE|MME-> CBC|MME向CBC回复告警停止响应消息。
WRITE REPLACE WARNING INDICATION|MME-> CBC|MME向CBC回复告警发送指示消息。
STOP WARNING INDICATION|MME-> CBC|MME向CBC回复告警停止指示消息。
PWS RESTART INDICATION|MME-> CBC|MME向CBC转发PWS重启指示消息。
PWS FAILURE INDICATION|MME-> CBC|MME向CBC转发PWS故障指示消息。
ERROR INDICATION|MME<-->CBC|错误指示，MME和CBC之间可以相互发送。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|23.041|Technical realization of Cell Broadcast Service (CBS)
3GPP|29.168|Cell Broadcast Center interfaces with the Evolved Packet Core
# 缩略语 
# 缩略语 
3GPP :3rd Generation Partnership Project第三代合作伙伴计划
## BSC 
Base Station Controller基站控制器
## BTS 
Base Transceiver Station基站收发信机
## CBC 
Cell broadcast center小区广播短消息中心
## CSFB 
Circuit Switched Fallback电路域回落
## E-SMLC 
Evolved Serving Mobile Location Center演进的服务位置中心
E-UTRAN :Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
## EDGE 
Enhanced Data rates for GSM EvolutionGSM用的增强型数据速率
EIR :Equipment Identity Register设备标识寄存器
EPC :Evolved Packet Core演进的分组核心网
EPS :Evolved Packet System演进的分组系统
## GERAN 
GSM/EDGE Radio Access NetworkGSM/EDGE无线接入网
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
## GSM 
Global System for Mobile Communications全球移动通信系统
HSS :Home Subscriber Server归属用户服务器
IMEI :International Mobile Equipment Identity国际移动设备标识
## LCS 
LoCation Services定位业务
LTE :Long Time Evolution更长期发展
## MBMS 
Multimedia Broadcast/Multicast Service多媒体广播/组播业务
MME :Mobility Management Entity移动管理实体
## NACC 
Network Assisted Cell Change网络辅助小区式切换
PCRF :Policy and Charging Rules Function策略和计费规则功能
PDN :Packet Data Network分组数据网
PGW :PDN Gateway分组数据网网关
## PWS 
Power System电源系统
QoS :Quality of Service服务质量
RAT :Radio Access Technology无线接入技术
## RAU 
Routing Area Update路由区更新
## RIM 
RAN Information Management无线接入网络信息管理
RNC :Radio Network Controller无线网络控制器
## SAE 
System Architecture Evolution系统架构演进
SGSN :Serving GPRS Support Node服务GPRS支持节点
SGW :Serving Gateway服务网关
SMS :Short Message Service短消息业务
TAU :Tracking Area Update跟踪区域更新
UE :User Equipment用户设备
## UMTS 
Universal Mobile Telecommunication System通用移动通讯系统
UTRAN :UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## eMBMS 
Evolved Multimedia Broadcast Multicast Service演进的多媒体广播多播业务
eNodeB :Evolved NodeB演进的NodeB
# ZUF-78-18 NSA(Option 3 and 3a and 3x) 
概述 :功能描述 :3GPP协议中根据是否存在双连接，将5G的组网方式区分为SA和NSA两大类。NSA是5G非独立组网模式。相对于SA，NSA可以利用现有的LTE无线网及核心网，通过主站（eNodeB/ng-eNB）和从站（gNB）双连接的方式支持5G终端的接入。5G建设初期，为降低成本，运营商可以先不新建5G核心网，只对现网核心网升级，5G使用E-UTRAN和NR的双连接接入EPC网络。
NSA中的Option3、Option3a、Option3x是一种在现有EPS网络中快速引入5G的部署方式，需要对EPC及周边网元进行升级，再新部署NR，即可完成5G部署。三种组网情况参见下图。 
Option3NR通过DCNR方式接入EPC，EPC把数据报文发送给eNB，eNB按比承载更小的粒度把部分或全部数据报文转发给NR（gNB），由NR投递给UE。eNB可以把一个承载中一部分或全部数据转发给NR。图1  Option3网络 
Option3aNR通过DCNR方接入EPC，EPC把数据报文发送给NR，由NR投递给UE。图2  Option3a网络 
Option3xNR通过DCNR方式接入EPC，EPC把数据报文发送给NR，NR按比承载更小粒度把部分或全部数据报文转发给eNB，由eNB投递给UE。该部署方式下，5G UE通过DCNR方式接入EPC。该方式可快速部署5G。图3  Option3x网络 
功能特性简介 :针对NSA的应用特点和应用场景，核心网为满足5G用户通过DCNR方式接入5G网络，提供了有效的解决方案。详细的解决方案参见下表：
方案特性|实现简述|特导链接
---|---|---
支持5G NR接入|MME支持5G NR接入，指通过NSA方式部署5G时，5G NR通过DCNR方式接入EPC。当UE通过DCNR方式接入5G(即Option 3/3a/3x)时，多方面功能会增强：QoS的最大速率可扩展到最大20 Gbps。GW选择时，可以选择支持NR接入的GW。保证UE 5G接入的安全。同时，MME可以提供DCNR接入用户的用量统计（包括用户数、会话数、承载数）和流程统计（包括附着、跟踪区更新、切换、eNB发起的E-RAB修改）。|ZUF-78-18-001 支持5G NR接入
5G NR接入限制|5G NR接入限制指MME可以根据本地策略和签约数据，限制具有5G能力的UE的NR接入。本地策略为根据IMSI号段指定限制5G NR接入的用户。|ZUF-78-18-002 5G NR接入限制
第二RAT用量数据上报|第二RAT用量数据上报指eNB把第二RAT用量数据通过控制面信令上报给MME，MME把其透传给SGW/PGW，SGW/PGW在CDR中区分不同RAT的用量。MME为临时存储用户数据的服务器，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。|ZUF-78-18-003 第二RAT用量数据上报
## ZUF-78-18-001 支持5G NR接入 
特性描述 :特性描述 :术语 :术语|含义
---|---
DCNR|eNB和gNB的双连接，指eNB作为主节点，gNB作为从节点的一种双连接方式。
描述 :定义 :MME支持5G NR接入，指通过NSA方式部署5G时，5G NR通过DCNR方式接入EPC。
背景知识 :NSA对应5G 3GPP Option3、Option3a、Option3x部署选项。
Option3、Option3a、Option3x是一种在现有EPS网络中快速引入5G的部署方式，仅需对现有EPS网络做软件升级，再新部署NR，即可完成5G部署。 
NR通过DCNR方式接入EPC，EPC把数据报文发送给eNB，eNB按比承载更小粒度把部分或全部数据报文转发给NR（gNB），由NR投递给UE。eNB可以把一个承载中一部分或全部数据转发给NR。图1  Option3网络 
Option3aNR通过DCNR方接入EPC，EPC把数据报文发送给NR，由NR投递给UE。图2  Option3a网络 
Option3xNR通过DCNR方式接入EPC，EPC把数据报文发送给NR，NR按比承载更小粒度把部分或全部数据报文转发给eNB，由eNB投递给UE。图3  Option3x网络该部署方式下，5G UE通过DCNR方式接入EPC。该方式可快速部署5G。 
应用场景 :5G NR接入EPC，典型场景就是Option3、Option3a、Option3x。 
客户收益 :受益方|受益描述
---|---
运营商|业务创新：快速的引入了5G网络，可以在高带宽、大连接、高可靠低时延的5G网络上进行更多的业务创新。投资保护：通过Option3/3a/3x部署方式引入5G，对现有网络影响小，不需新建5G核心网，最大的利用了现有EPC网络，节省了投资。
移动用户|本特性对终端不可见。
实现原理 :系统架构 :MME支持5G NR接入的系统架构如下图所示。 
图4  系统架构

涉及的网元 :网元名称|网元作用
---|---
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，完成无线资源管理功能，完成移动性管理功能，完成安全功能，完成承载管理功能。本特性中，UE支持通过DCNR方式的5G接入，处理DCNR支持标识，支持最大可达20Gbps的速率，5G安全能力等。
eNB|为UE的LTE接入提供无线资源。本特性中，eNB支持DCNR，支持限制UE 的DCNR，支持最大可达20Gbps的速率，支持5G安全能力。
gNB|为UE的5G接入提供无线资源。本特性中，gNB支持DCNR。
HSS|永久存储用户签约数据，产生用户鉴权数据。本特性中，HSS支持签约更高的速率，签约UE的DCNR接入限制等。
SGW|负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。本特性中，SGW支持最大可达20Gbps的速率，可以选择支持DCNR的SGW-U等。
PGW|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个PGW。本特性中，PGW支持最大可达20Gbps的速率，可以选择支持DCNR的PGW-U等。
PCRF|主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的Qos(Quality of Service，服务质量)规则以及计费规则。该功能实体也可以控制接入网中承载的建立和释放。本特性中，PCRF支持QoS规则中更高的速率等。
本网元实现 :临时存储用户数据的服务器，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。 
本特性中，MME支持UE的DCNR能力标识，支持最大可达20Gbps的速率，可以选择支持DCNR的SGW和PGW，支持处理5G安全能力等。 
业务流程 :UE 5G能力处理
UE 5G能力处理的附着流程如下图所示。 
图5  UE 5G能力处理的附着流程

流程说明： 
UE给MME发送Attach Request消息，对于支持5G的UE，则在Attach Request消息中携带支持5G的指示给MME。 
MME给UE发送Attach Accept消息，如果不限制UE的DCNR接入，则Attach Accept消息中携带不限制DCNR接入指示。 
UE 5G能力处理的TAU流程如下图所示。 
图6  UE 5G能力处理的TAU流程

流程说明： 
UE给MME发送TAU Request消息，对于支持5G的UE，则在TAU Request消息中携带支持5G的指示给MME。 
MME给UE发送TAU Accept消息，如果UE不限制UE的DCNR接入，则Attach Accept消息中携带不限制DCNR接入指示。 
5G QoS扩展
各流程中QoS速率处理方法参见下表。 
流程|接口|消息|参数|QoS处理
---|---|---|---|---
附着|NAS|ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST|APN-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S6a|附着|ULA|APN-AMBR、UE-AMBR|保存消息。
S11/S5/S8|附着|Create Session Request、Create Session Response|APN-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S1-MME|附着|Initial Context Setup Request|UE-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
业务请求|S1-MME|Initial Context Setup Request|UE-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
TAU|S6a|ULA|APN-AMBR、UE-AMBR|保存消息。
S11/S5/S8|TAU|Create Session Request、Create Session Response、Modify Bearer Request、Context Response|UE-AMBR、APN-AMBR、MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S1-MME|TAU|Initial Context Setup Request|UE-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
切换|S11/S5/S8|Create Session Request、Create Session Response、Modify Bearer Request、Forward Relocation Request|UE-AMBR、APN-AMBR、MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S1-MME|切换|Handover Request|UE-AMBR、MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
PDN连接建立|NAS|ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST|APN-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S11/S5/S8|PDN连接建立|Create Session Request、Create Session Response|APN-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S1-MME|PDN连接建立|E-RAB Setup Request|UE-AMBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
专有承载建立|NAS|ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST|MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S11/S5/S8|专有承载建立|Create Bearer Request|MBR、GBR|保存消息。
S1-MME|专有承载建立|E-RAB Setup Request|MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
承载修改|NAS|MODIFY EPS BEARER CONTEXT REQUEST|APN-AMBR、MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
S11/S5/S8|承载修改|Update Bearer Request|APN-AMBR、MBR、GBR|保存消息。
S1-MME|承载修改|E-RAB Modify Request|UE-AMBR、MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
UE请求的资源建立或修改|NAS|UE Requested Resouce Allocation、UE Requested Resource Modification|MBR、GBR|保存消息。
S11/S5/S8|UE请求的资源建立或修改|Bearer Resource Command|MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
HSS发起的承载更新|S6a|IDR|UE-AMBR、APN-AMBR、MBR、GBR|保存消息。
S11/S5/S8|HSS发起的承载更新|Modify Bearer Command|APN-AMBR、MBR、GBR|接口的QoS开关打开，透传消息。接口的QoS开关关闭，限速10Gbps。
GW选择扩展
GW选择扩展的附着流程如下图所示。 
图7  GW选择扩展的附着流程

流程说明： 
MME收到UE发送的Attach Request消息，消息中携带UE network capability（DCNR 标记位）信息。 
MME在解析PGW和SGW时，判断UE支持DCNR； 
MME解析SGW时，TA-FQDN/eNodeB ID-FQDN，"Service Parameters" 填充形式如下： 
"x-3gpp-sgw:x-s5-gtp+nc-nr:x-s11+nc-nr", "x-3gpp-sgw:x-s8-gtp+nc-nr:x-s11+nc-nr" 
MME解析PGW时，APN-FQDN，"Service Parameters" 填充形式如下： 
"x-3gpp-pgw:x-s5-gtp+nc-nr" , "x-3gpp-pgw:x-s8-gtp+nc-nr" 
MME根据解析的SGW列表和PGW列表，选择SGW和PGW。 
MME给SGW发送Create Session Request消息，携带UP Function Selection Indication Flags信息。 
SGW改变的TAU的流程如下图所示。 
图8  SGW改变的TAU的流程

流程说明： 
MME收到UE发送的TAU Request消息。 
MME在判断SGW是否需要改变时，判断UE支持DCNR。 
MME解析SGW时，TA-FQDN/eNodeB ID-FQDN，"Service Parameters" 填充形式如下： 
"x-3gpp-sgw:x-s5-gtp+nc-nr:x-s11+nc-nr", "x-3gpp-sgw:x-s8-gtp+nc-nr:x-s11+nc-nr" 
MME根据解析的SGW列表，确定SGW需要改变，选择一个SGW。 

MME给SGW发送Create Session Request消息，携带UP Function Selection Indication Flags信息。 
SGW改变的Path Switch的流程如下图所示。 
图9  SGW改变的Path Switch的流程

流程说明： 
MME收到Target eNB发送的Path Switch Request消息。 
MME判断SGW是否需要改变时，判断UE支持DCNR。 
MME解析SGW时，TA-FQDN/eNodeB ID-FQDN，"Service Parameters" 填充形式如下： 
"x-3gpp-sgw:x-s5-gtp+nc-nr:x-s11+nc-nr", "x-3gpp-sgw:x-s8-gtp+nc-nr:x-s11+nc-nr" 
MME根据解析的SGW列表，确定SGW需要改变，选择一个SGW。 
MME给SGW发送Create Session Request消息，携带UP Function Selection Indication Flags信息。 
SGW改变的Handover流程如下图所示。 
图10  SGW改变的Handover流程

流程说明： 
MME收到Source eNB发送的Handover Requried消息或收到Source SGSN/MME的Forward Relocation Request消息。 
MME在判断SGW是否需要改变时，判断UE支持DCNR。 
MME解析SGW时，TA-FQDN/eNodeB ID-FQDN，"Service Parameters" 填充形式如下： 
"x-3gpp-sgw:x-s5-gtp+nc-nr:x-s11+nc-nr", "x-3gpp-sgw:x-s8-gtp+nc-nr:x-s11+nc-nr" 
MME根据解析的SGW列表，确定SGW需要改变，选择一个SGW。 
MME给SGW发送Create Session Request消息，携带UP Function Selection Indication Flags信息。 
PDN连接建立流程如下图所示。 
图11  PDN连接建立流程

流程说明： 
MME收到UE发送的PDN Connection Request消息。 
MME在解析PGW和SGW时，判断UE支持DCNR。 
N0030 MME解析PGW时，APN-FQDN，"Service Parameters" 填充形式如下： 
"x-3gpp-pgw:x-s5-gtp+nc-nr" , "x-3gpp-pgw:x-s8-gtp+nc-nr" 
MME根据解析的PGW列表，选择PGW。 
MME给SGW发送Create Session Request消息，携带UP Function Selection Indication Flags信息。 
5G安全扩展
5G安全扩展的附着流程如下图所示。 
图12  5G安全扩展的附着流程

流程说明： 
MME收到UE发送的Attach Request消息，如果消息中携带了UE additional security capability信息，则MME保存。 
如果需要对UE进行AKA，则MME对UE进行鉴权；MME给UE发送Security mode command消息，如果MME保存了UE additional security capability信息，则消息中携带Replayed UE additional security capability信息。 

MME给eNB发送Initial UE Context Request消息，如果MME保存了UE additional security capability信息，则携带NR UE Security Capabilities信息。 
业务请求流程如下图所示。 
图13  业务请求流程

流程说明： 
MME收到UE发送的Service Request消息。 
如果需要对UE进行AKA，则MME对UE进行鉴权；MME给UE发送Security mode command消息，如果MME保存了UE additional security capability信息，则消息中携带Replayed UE additional security capability信息。 
MME给eNB发送Initial UE Context Request消息，如果MME保存了UE additional security capability信息，则携带NR UE Security Capabilities信息。 
系统影响 :支持NSA，会在现有消息中增加一些IE的处理，会消耗较小的系统资源。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
3GPP|3GPP TS 24.301|Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS) ; Stage 3
3GPP|3GPP TS 29.272|Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol
3GPP|3GPP TS 29.274|Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C) ; Stage 3
3GPP|3GPP TS 29.303|Domain Name System Procedures; Stage 3
3GPP|3GPP TS 36.413|Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“支持NSA”，此项目显示为“支持”，表示ZXUN uMAC支持NSA功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME NSA业务控制策略配置SET NSA CONTROL POLICYSHOW NSA CONTROL POLICYMME支持QoS速率扩展控制配置SET QOS RATE EXTCTRLSHOW QOS RATE EXTCTRL 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软参的变化。 
动态管理在原有动态管理命令SHOW MMEUSERDYN中增加Whether UE Support DCNR字段，表示UE是否支持DCNR接入。 
性能统计 :测量类型|描述
---|---
NSA用户数测量|编号为C46601开头的所有计数器。
NSA承载数测量|编号为C46604开头的所有计数器。
NSA附着流程测量|编号为C46605开头的所有计数器。
NSA跟踪区更新流程测量|编号为C46606开头的所有计数器。
NSA切换流程测量|编号为C46607开头的所有计数器。
NSA S1AP消息测量|编号为C46608开头的所有计数器。
NSA UE请求承载资源流程测量|编号为C46610开头的所有计数器。
NSA业务请求流程测量|编号为C46612开头的所有计数器。
NSA去附着流程测量|编号为C46613开头的所有计数器。
NSA寻呼流程测量|编号为C46614开头的所有计数器。
NSA承载激活流程测量|编号为C46617开头的所有计数器。
NSA承载修改流程测量|编号为C46618开头的所有计数器。
NSA承载去激活流程测量|编号为C46619开头的所有计数器。
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :配置MME支持5G NR接入。 
配置前提 :MME已支持NSA功能。 
配置过程 :使用[SET NSA CONTROL POLICY]命令，设置MME NSA业务控制策略。
使用[SET QOS RATE EXTCTRL]命令，设置MME支持QoS速率扩展控制。
配置实例 :###### UE 5G能力处理 
场景说明
MME支持UE 5G能力处理。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA|SET NSA CONTROL POLICY:SUPNSA="YES";
2|传送配置|SYNA;
###### 5G QoS扩展 
场景说明
具有5G能力的UE附着时，MME支持5G能力处理，用户在HSS上签约的AMBR大于65280 Mbps。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA|SET NSA CONTROL POLICY:SUPNSA="YES";
2|支持QoS扩展|SET NSA CONTROL POLICY:SUPQOSEXT="YES";
3|S11口支持QoS扩展|SET QOS RATE EXTCTRL:S11SUPQOSEXT="YES";
4|NAS口支持QoS扩展|SET QOS RATE EXTCTRL:NASSUPQOSEXT="YES";
6|S1口支持QoS扩展|SET QOS RATE EXTCTRL:S1SUPQOSEXT="YES";
7|传送配置|SYNA;
###### GW选择扩展 
场景说明
具有5G能力的UE附着时，MME支持5G能力处理，MME需要根据UE的5G能力选择SGW和PGW，且在选择SGW/PGW失败后需要根据不使用5G能力再解析一次。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA|SET NSA CONTROL POLICY:SUPNSA="YES";
2|支持选择NC-NR的SGW|SET NSA CONTROL POLICY:SUPSELNCNRSGW="YES";
3|支持选择NC-NR的PGW|SET NSA CONTROL POLICY:SUPSELNCNRPGW="YES";
4|选择NC-NR的SGW失败重选|SET NSA CONTROL POLICY:RESELSGWNCNRFAIL="SELECT_SGW_WITH_NC-NR";
5|选择NC-NR的PGW失败重选|SET NSA CONTROL POLICY:RESELPGWNCNRFAIL="NOT_RESELECT_PGW_WITHOUT_NC-NR";
6|传送配置|SYNA;
###### 5G安全扩展 
场景说明
MME支持UE 5G安全能力处理。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA|SET NSA CONTROL POLICY:SUPNSA="YES",SUPUE5GSECCAPA="YES";
2|传送配置|SYNA;
调整特性 :该特性不涉及调整特性。 
测试用例 :测试项目|MME支持5G NR接入
---|---
测试目的|MME支持5G NR接入功能。
预置条件|MME支持NSA。
测试过程|设置MME支持UE 5G能力处理。设置MME的5G QoS扩展功能。配置5G QoS扩展功能。配置5G安全扩展信息。执行SYNA;命令同步数据。
通过准则|UE与MME在5G网络下通讯正常。
测试结果|–
常见问题处理 :无 
## ZUF-78-18-002 5G NR接入限制 
特性描述 :特性描述 :术语 :术语|含义
---|---
DCNR|eNB和gNB的双连接。eNB作为主节点，gNB作为从节点的一种双连接方式。
NSA|非独立组网，指5G NR通过DCNR方式，接入EPC，完成5G网络的快速部署和使用。
描述 :定义 :5G NR接入限制指MME可以根据具有DCNR能力的UE的签约数据和本地策略，决策UE是否可以使用DCNR。本地策略包含了根据IMSI号段决策UE的DCNR使用。
背景知识 :NSA对应5G 3GPP Option3、Option3a、Option3x部署选项。
Option3、Option3a、Option3x是一种在现有EPS网络中快速引入5G的部署方式，仅需对现有EPS网络做软件升级，再新部署NR，即可完成5G部署。 
NR通过DCNR方式接入EPC，EPC把数据报文发送给eNB，eNB按比承载更小粒度把部分或全部数据报文转发给NR（gNB），由NR投递给UE。eNB可以把一个承载中一部分或全部数据转发给NR。图1  Option3网络 
Option3aNR通过DCNR方接入EPC，EPC把数据报文发送给NR，由NR投递给UE。图2  Option3a网络 
Option3xNR通过DCNR方式接入EPC，EPC把数据报文发送给NR，NR按比承载更小粒度把部分或全部数据报文转发给eNB，由eNB投递给UE。图3  Option3x网络该部署方式下，5G UE通过DCNR方式接入EPC。该方式可快速部署5G。 
应用场景 :5G接入限制是NSA重要功能，典型场景有以下几种。 
本地用户的5G NR接入限制场景只针对部分用户，在HSS上开通5G NR接入。HSS没有升级，MME通过本地限制限制用户5G NR接入。 
漫游用户的5G NR接入限制场景根据漫游协议，对不同的漫游用户，有不同的5G NR接入限制策略。 
客户收益 :受益方|受益描述
---|---
运营商|通过对特定用户的5G NR接入限制，可避免用户过度占用运营商网络资源。
移动用户|此特性对终端用户不可见
实现原理 :系统架构 :MME支持5G NR接入限制的系统架构如下图所示。 
图4  系统架构

gNB通过DCNR方式接入EPC。 
涉及的网元 :网元名称|网元作用
---|---
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，完成无线资源管理功能，完成移动性管理功能，完成安全功能，完成承载管理功能。本特性中，UE支持根据MME提供的DCNR限制信息，限制UE的DCNR。
eNB|为UE的LTE接入提供无线资源。本特性中，eNB支持根据MME提供的DCNR限制信息，限制UE的DCNR。
HSS|永久存储用户签约数据，产生用户鉴权数据。本特性中，HSS UE的DCNR接入限制等。
本网元实现 :临时存储用户数据的服务器，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。 
本特性中，MME支持对具有DCNR能力的UE，可以根据其签约的DCNR接入限制以及本地策略，确定是否需限制UE的DCNR。 
业务流程 :附着
附着流程如下图所示。 
图5  附着流程

流程说明： 
MME收到UE发送的Attach Request消息，如果消息中携带UE network capability（DCNR 标记位）信息，则MME保存。 
如果需要更新HSS，MME发送ULR消息，其中Feature-List中的NR as Secondary RAT置位。 
HSS返回ULA消息，如果消息中携带ARD（NR as Secondary RAT Not Allowed）信息，则MME保存。 
MME根据签约ARD和本地策略（根据IMSI号段确定策略或取默认策略），确定需要限制UE 5G接入。 
MME构造Attach Accept消息，EPS network feature support中的RestrictDCNR置位。 
MME给eNB发送Initial UE Context Request消息，Handover Restriction List中的NR Restriction置位。 
TAU
TAU流程处理基本同附着过程，MME根据签约ARD和本地策略（根据IMSI号段确定策略或取默认策略），确定需要限制UE 5G接入，则在TAU Accept和Initial Context Setup Request消息中分别通知UE和eNB。 
业务请求
业务请求流程中，MME根据签约ARD和本地策略（根据IMSI号段确定策略或取默认策略），确定需要限制UE 5G接入，则在Initial Context Setup Request消息中通知eNB。 
切换
切换流程中，MME根据签约ARD和本地策略（根据IMSI号段确定策略或取默认策略），确定需要限制UE 5G接入，则在Handover Request消息中通知eNB。 
系统影响 :支持NR接入限制，在UE接入时，需判断UE的NR接入限制，也在现有消息中增加了NR Restriction IE的处理，会消耗很少的系统资源。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
3GPP|3GPP TS 24.301|Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS) ; Stage 3
3GPP|3GPP TS 29.272|Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol
3GPP|3GPP TS 36.413|Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“支持NSA”，此项目显示为“支持”，表示ZXUN uMAC支持NSA功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项配置项命令MME NSA业务控制策略配置SET NSA CONTROL POLICYSHOW NSA CONTROL POLICYMME DCNR限制策略配置SET DCNR RESTRICT DEFAULT POLICYSHOW DCNR RESTRICT DEFAULT POLICYADD IMSI DCNR RESTRICT POLICYSET IMSI DCNR RESTRICT POLICYDEL IMSI DCNR RESTRICT POLICYSHOW IMSI DCNR RESTRICT POLICY 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及 软件参数的变化。 
动态管理在原有动态管理命令 SHOW MMEUSERSUB中增加Access Restriction字段。在原有动态管理命令 SHOW MMEUSERDYN中增加Whether DCNR Is Restricted字段，表示MME最终是否限制DCNR接入。 
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME根据支持5G的UE的号段策略、默认策略和HSS签约信息来决策是否支持5G NR接入限制。其中号段策略的优先级高于默认策略，只有在没有号段策略的前提下默认策略才会生效。 
配置前提 :已开启支持NSA的License功能。 
配置过程 :使用[SET NSA CONTROL POLICY]命令，打开NSA和DCNR限制开关。
使用[ADD IMSI DCNR RESTRICT POLICY]命令，新增基于号段配置DCNR限制策略。
使用[SET DCNR RESTRICT DEFAULT POLICY]命令，新增默认DCNR限制策略。
配置实例 :###### 部分IMSI为DCNR限制策略 
场景说明
配置部分IMSI为DCNR限制策略。 
数据规划
部分号段DCNR限制策略配置为限制。 
默认配置为不限制。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA，支持DCNR限制。|SET NSA CONTROL POLICY:SUPNSA="YES",SUPDCNRRESTRICT="YES";
2|部分号段DCNR限制策略配置为限制。|ADD IMSI DCNR RESTRICT POLICY:IMSI="46000",IMSIDCNRRESTRIC="LOCAL",IMSILOCALPOLICY="YES‍‍‍";
3|默认策略为不限制。|SET DCNR RESTRICT DEFAULT POLICY:DFTDCNR="LOCAL",LOCALPOLICY="NO";
4|传送配置。|SYNA;
###### 部分IMSI为DCNR不限制策略 
场景说明
配置部分IMSI为DCNR不限制策略。 
数据规划
部分号段DCNR限制策略配置为不限制。 
默认配置为限制。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA，支持DCNR限制。|SET NSA CONTROL POLICY:SUPNSA="YES",SUPDCNRRESTRICT="YES";
2|部分号段DCNR限制策略配置为不限制。|ADD IMSI DCNR RESTRICT POLICY:IMSI="46000",IMSIDCNRRESTRIC="LOCAL",IMSILOCALPOLICY="NO";
3|默认策略为限制。|SET DCNR RESTRICT DEFAULT POLICY:DFTDCNR="LOCAL",LOCALPOLICY="YES";
4|传送配置。|SYNA;
###### 部分用户根据签约决策 
场景说明
配置部分IMSI号段为根据签约信息决策，其他用户不配置策略，默认策略为不限制。 
数据规划
部分号段DCNR限制策略配置为根据签约信息决策。 
默认配置为不限制。 
配置步骤
步骤|说明|操作
---|---|---
1|支持NSA，支持DCNR限制。|SET NSA CONTROL POLICY:SUPNSA="YES",SUPDCNRRESTRICT="YES";
2|部分号段DCNR限制策略配置为根据签约信息决策。|ADD IMSI DCNR RESTRICT POLICY:IMSI="46000",IMSIDCNRRESTRIC="SUBSCRIPTION";
3|默认策略为不限制。|SET DCNR RESTRICT DEFAULT POLICY:DFTDCNR="LOCAL",LOCALPOLICY="NO";
4|传送配置。|SYNA;
调整特性 :该特性不涉及调整特性。 
测试用例 :测试项目|部分用户限制，其他用户不限制
---|---
测试目的|对部分的IMSI号段进行DCNR策略限制。
预置条件|MME支持NSA功能。
测试过程|使用SET NSA CONTROL POLICY命令，设置支持NSA，支持DCNR限制。使用ADD IMSI DCNR RESTRICT POLICY命令，设置部分号段DCNR限制策略为限制。使用SET DCNR RESTRICT DEFAULT POLICY命令，设置默认策略为不限制。使用SYNA命令，同步数据。
通过准则|对部分的IMSI号段进行DCNR策略限制。
测试结果|–
常见问题处理 :无 
## ZUF-78-18-003 第二RAT用量数据上报 
特性描述 :特性描述 :术语 :术语|含义
---|---
DCNR|eNB和gNB的双连接。eNB作为主节点，gNB作为从节点的一种双连接方式。
NSA|非独立组网，指5G NR通过DCNR方式，接入EPC，完成5G网络的快速部署和使用。
描述 :定义 :第二RAT用量数据上报指eNB把第二RAT用量数据通过控制面信令上报给MME，MME把其透传给SGW/PGW，SGW/PGW在CDR中区分不同RAT的用量。 
背景知识 :NSA对应5G 3GPP Option3、Option3a、Option3x部署选项。
Option3、Option3a、Option3x是一种在现有EPS网络中快速引入5G的部署方式，仅需对现有EPS网络做软件升级，再新部署NR，即可完成5G部署。 
NR通过DCNR方式接入EPC，EPC把数据报文发送给eNB，eNB按比承载更小粒度把部分或全部数据报文转发给NR（gNB），由NR投递给UE。eNB可以把一个承载中一部分或全部数据转发给NR。图1  Option3网络 
Option3aNR通过DCNR方接入EPC，EPC把数据报文发送给NR，由NR投递给UE。图2  Option3a网络 
Option3xNR通过DCNR方式接入EPC，EPC把数据报文发送给NR，NR按比承载更小粒度把部分或全部数据报文转发给eNB，由eNB投递给UE。图3  Option3x网络该部署方式下，5G UE通过DCNR方式接入EPC。该方式可快速部署5G。 
应用场景 :第二RAT用量数据上报是NSA重要功能，典型场景如下： 
本地用户PGW上报话单中区分第二RAT用量数据。 
漫出用户PGW上报话单中区分第二RAT用量数据。 
漫入用户SGW上报话单中区分第二RAT用量数据。 
客户收益 :受益方|受益描述
---|---
运营商|提高收益：收集第二RAT用量，用于计费，便于进行更多的业务创新。投资保护：通过Option 3、Option 3a、Option 3x部署方式引入5G，对5G上的用量，实现特殊计费，便于5G网络的投资回收。
移动用户|此特性对终端用户不可见。
实现原理 :系统架构 :MME支持第二RAT用量数据上报的系统架构如下图所示。 
图4  系统架构

gNB通过DCNR方式接入EPC。 
涉及的网元 :网元名称|网元作用
---|---
eNB|为UE的LTE接入提供无线资源。本特性中，eNB支持上报Secondary RAT usage。
gNB|为UE的5G接入提供无线资源。本特性中，gNB支持DCNR，支持上报Secondary RAT usage给eNB。
SGW|负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。本特性中，SGW支持上报Secondary RAT usage到话单等。
PGW|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个PGW。本特性中，PGW上报Secondary RAT usage到话单等。
本网元实现 :MME为临时存储用户数据的服务器，负责管理和存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。 
本特性中，MME支持把eNB上报的Secondary RAT usage信息透传给SGW/GPW。 
业务流程 :连接挂起
连接挂起流程如下图所示。 
图5  连接挂起

流程说明： 
如果MME收到eNB发送的UE Context Suspend Request消息，且消息中携带Secondary RAT Usage Report List信息，则MME保存。 
如果MME有Secondary RAT Usage Report List信息，且“是否支持PGW用量报告”开关开启，则向SGW发送Change Notification Request消息，消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW不置位，IR PGW置位。 
SGW返回Change Notification Response消息。 
MME向SGW发送Release Access Bearers Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位，IR PGW不置位。 
SGW返回Release Access Bearers Response消息。 
S1释放
S1释放流程如下图所示。 
图6  S1释放

流程说明： 
 说明： 
对于连接态下的用户，又收到UE的初始UE消息，此时MME先处理老的S1连接，获取Secondary RAT Usage信息，并上报给SGW和/或PGW后，再处理初始UE消息。 
如果MME收到eNB发送的S1 UE Context Release Request消息，且消息中携带Secondary RAT Usage Report List信息，则MME保存。 
MME向SGW发送Release Access Bearers Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位，IR PGW不置位。 
MME向eNB发送S1 UE Context Release Command消息。 
eNB返回S1 UE Context Release Complete消息，如果S1 UE Context Release Complete消息中携带了Secondary RAT Usage Report List信息，且MME没有收到S1 UE Context Release Request消息或S1 UE Context Release Request消息中没有携带Secondary RAT Usage Report List信息，则MME保存S1 UE Context Release Complete消息中Secondary RAT Usage Report List信息；如果S1 UE Context Release Complete消息中携带了Secondary RAT Usage Report List信息，但MME收到了S1 UE Context Release Request消息且S1 UE Context Release Request消息中携带了Secondary RAT Usage Report List信息，则MME忽略S1 UE Context Release Complete消息中Secondary RAT Usage Report List信息。 
MME判断本地保存了Secondary RAT Usage Report List信息，如果“是否支持SGW用量报告”开关开启且Release Access Bearers Request消息中没有携带Secondary RAT Usage Data Report信息，或“是否支持PGW用量报告”开关开启，则向SGW发送Change Notification Request消息，消息中携带Secondary RAT Usage Data Report，在“是否支持SGW用量报告”开关开启且Release Access Bearers Request消息中没有携带Secondary RAT Usage Data Report信息时Secondary RAT Usage Data Report中IR SGW置位，在“是否支持PGW用量报告”开关开启时IR PGW 置位。 
SGW返回Change Notification Response消息。 
分离
UE触发的Detach的流程如下图所示。 
图7  UE触发的Detach

流程说明： 
MME收到UE发送的Detach Request消息。 
MME判断配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，且UE支持DCNR，则确定需要eNB上报的Secondary RAT Usage Report List信息。 
MME确定把S1释放过程提前到删除会话之前，在应该给SGW发送删除会话请求时，先通知UE和eNB释放资源。 
MME给UE发送Detach Accept消息。 
MME向eNB发送S1 UE Context Release Command消息。 
eNB返回S1 UE Context Release Complete消息，如果S1 UE Context Release Complete消息中携带了Secondary RAT Usage Report List信息，则MME保存。 
MME向SGW发送Delete Session Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启），IR PGW置位（“是否支持PGW用量报告”开关开启）。 
SGW返回Delete Session Response消息。 
MME触发的Detach的流程如下图所示。 
图8  MME触发的Detach

流程说明： 
MME确定需要发起MME触发的Detach流程。 
MME判断配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，且UE支持DCNR，则确定需要eNB上报的Secondary RAT Usage Report List信息。 
如果UE处于连接态，MME确定把S1释放过程提前到删除会话之前，在应该给SGW发送删除会话请求时，先通知UE和eNB释放资源。 
MME给UE发送Detach Request消息。 
UE给MME返回Detach Accept消息。 
MME向eNB发送S1 UE Context Release Command消息。 
eNB返回S1 UE Context Release Complete消息，如果S1 UE Context Release Complete消息中携带了Secondary RAT Usage Report List信息，则MME保存。 
MME向SGW发送Delete Session Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启），IR PGW置位（“是否支持PGW用量报告”开关开启）。 
SGW返回Delete Session Response消息。 
承载去激活
GW发起的承载去激活的流程如下图所示。 
图9  GW发起的承载去激活

流程说明： 
SGW发送Delete Bearer Request消息。 
MME向eNB发送E-RAB Release Request消息，消息中携带NAS消息Deactivate dedicated bearer context request。 
eNB返回E-RAB Release Response消息，如果消息中携带了Secondary RAT Usage Report List信息，则MME保存。  
MME向SGW返回Delete Bearer Response消息，如果本地保存了Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启时置位），IR PGW置位（“是否支持PGW用量报告”开关开启时置位）。 
MME发起的承载去激活流程如下图所示。 
图10  MME发起的承载去激活

流程说明： 
如果MME收到eNB发送的E-RAB Release Indication消息，且消息中携带Secondary RAT Usage Report List信息，则MME保存。 
MME向SGW发送Delete Bearer Command消息，如果本地保存了Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启时置位），IR PGW置位（“是否支持PGW用量报告”开关开启时置位）。 
SGW发送Delete Bearer Request消息。 
MME向eNB发送E-RAB Release Request消息，消息中携带NAS消息Deactivate dedicated bearer context request。 
eNB返回E-RAB Release Response消息，如果E-RAB Release Response消息中携带了Secondary RAT Usage Report List信息，且E-RAB Release Indication消息中也携带了Secondary RAT Usage Report List信息，则忽略E-RAB Release Response消息中携带的Secondary RAT Usage Report List信息；如果E-RAB Release Response消息中携带了Secondary RAT Usage Report List信息，但没有收到E-RAB Release Indication消息或E-RAB Release Indication消息中没有携带Secondary RAT Usage Report List信息，则MME保存E-RAB Release Response消息中Secondary RAT Usage Report List信息。  
MME向SGW返回Delete Bearer Response消息，如果本地保存了Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启时置位），IR PGW置位（“是否支持PGW用量报告”开关开启时置位）。 
E-UTRAN发起的E-RAB修改
E-UTRAN发起的E-RAB修改的流程如下图所示。 
图11  E-UTRAN发起的E-RAB修改

流程说明： 
如果MME收到eNB发送的E-RAB MOdify Indication消息，且消息中携带Secondary RAT Usage Report List信息，则MME保存。 
MME向SGW发送Modify Bearer Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告” 开关开启，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启时置位），IR PGW置位（“是否支持PGW用量报告”开关开启时置位）。 
SGW返回Modify Bearer Response消息。 
PDN去连接
PDN去连接的流程如下图所示。 
图12  PDN去连接

流程说明： 
如果是UE发起的PDN去连接，则UE发送的PDN Disconnection Request消息。 
MME判断配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，且判断UE支持DCNR，则确定需要eNB上报的Secondary RAT Usage Report List信息。 
MME确定把E-RAB释放过程提前到删除会话之前，在应该给SGW发送删除会话请求时，先通知eNB释放资源。 
MME向eNB发送E-RAB Release Request消息，消息中携带NAS消息Deactivate default bearer context request。 
eNB返回E-RAB Release Response消息，如果消息中携带了Secondary RAT Usage Report List信息，则MME保存。  
MME向SGW发送Delete Session Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告”开关开启），IR PGW置位（“是否支持PGW用量报告”开关开启）。 
SGW返回Delete Session Response消息。 
切换
SGW不变的Path Switch流程如下图所示。 
图13  SGW不变的Path Switch

流程说明： 
eNB发送的SECONDARY RAT REPORT消息，消息中携带Handover Flag和Secondary RAT Usage Report List信息。 
MME缓存Secondary RAT Usage Report List信息。 
Target eNB发送的Path Switch Request消息。 
MME向SGW发送Modify Bearer Request消息，如果本地缓存了Secondary RAT Usage Report List信息，且“是否支持SGW用量报告” 开关开启或“是否支持PGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，IR SGW置位（“是否支持SGW用量报告” 开关开启），IR PGW置位（“是否支持PGW用量报告” 开关开启）。 
SGW返回Modify Bearer Response消息。 
SGW改变的Path Switch的流程如下图所示。 
图14  SGW改变的Path Switch

流程说明： 
Source eNB发送的SECONDARY RAT REPORT消息，消息中携带Handover Flag和Secondary RAT Usage Report List信息。 
MME缓存Secondary RAT Usage Report List信息。 
Target eNB发送的Path Switch Request消息。 
MME判断SGW需要改变，选择一个新的SGW。 
MME向SGW发送Create Session Request消息，如果本地缓存了Secondary RAT Usage Report List信息，且“是否支持PGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，IR SGW不置位，IR PGW置位。 
SGW返回Create Session Response消息。 
MME向Old SGW发送Delete Session Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，IR SGW置位，IR PGW不置位。 
Old SGW返回Delete Session Response消息。 
从E-UTRAN到UTRAN（Gn/Gp SGSN）的垮RAT切换流程如下图所示。 
图15  从E-UTRAN到UTRAN（Gn/Gp SGSN）的垮RAT切换

流程说明： 
Source eNB给Souce MME发送Handover Requried消息。 
Source MME给Source eNB发送Handover Command消息。 
Source eNB给Source MME发送Secondary RAT Report消息，消息中携带Secondary RAT Usage Report List信息。 
MME保存Secondary RAT Usage Report List信息。 
MME判断本地保存了Secondary RAT Usage Report List信息，且“是否支持PGW用量报告”开关开启，则通过GTPC向Source SGW发送Change Notification Request消息，消息中携带Secondary RAT Usage Data Report，IR SGW不置位，IR PGW置位。 
SGW返回Change Notification Response消息。 
MME向Source SGW发送Delete Session Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，中IR SGW置位，IR PGW不置位。 
RAU
RAU流程如下图所示。 
图16  RAU

流程说明： 
UE发送RAU Request消息给SGSN。 
SGSN给MME发送SGSN Context Request消息。 
MME给SGSN返回SGSN Context Response消息。 
MME的资源保护定时器超时后，判断配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，且判断UE支持DCNR，则确定需要eNB上报的Secondary RAT Usage Report List信息。 
MME确定把S1释放过程提前到删除会话之前，在应该给SGW发送删除会话请求时，先通知eNB释放资源。 
MME向eNB发送S1 UE Context Release Command消息。 
eNB返回S1 UE Context Release Complete消息，如果S1 UE Context Release Complete消息中携带了Secondary RAT Usage Report List信息，则MME保存。 
MME向SGW发送Delete Session Request消息，如果MME有Secondary RAT Usage Report List信息，且配置中“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告”开关开启，则消息中携带Secondary RAT Usage Data Report，IR SGW置位（“是否支持SGW用量报告”开关开启），IR PGW不置位（“是否支持PGW用量报告”开关开启）。 
SGW返回Delete Session Response消息。 
Secondary RAT用量数据上报
Secondary RAT用量数据上报的流程如下图所示。 
图17  Secondary RAT用量数据上报

流程说明： 
MME收到eNB发送的SECONDARY RAT REPORT消息。 
MME保存Secondary RAT Usage Report List信息。 
MME判断本地保存了Secondary RAT Usage Report List信息，且“是否支持SGW用量报告”开关开启或“是否支持PGW用量报告” 开关开启，则向New SGW发送Change Notification Request消息，消息中携带Secondary RAT Usage Data Report，Secondary RAT Usage Data Report中IR SGW置位（“是否支持SGW用量报告” 开关开启），IR PGW置位（“是否支持PGW用量报告” 开关开启）。 

SGW返回Change Notification Response消息。 
系统影响 :支持第二RAT用量数据上报，会新增Secondary RAT Usage上报消息，会在现有消息中增加一些IE的处理，会消耗较小的系统资源。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
3GPP|3GPP TS 29.274|Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C) ; Stage 3
3GPP|3GPP TS 36.413|Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“支持NSA”，此项目显示为“支持”，表示ZXUN uMAC支持NSA功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项配置项命令MME NSA业务控制策略配置SET NSA CONTROL POLICYSHOW NSA CONTROL POLICY 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :测量类型|描述
---|---
SECONDARY RAT流量测量|编号为C46602开头的所有计数器。
基于eNodeB SECONDARY RAT流量测量|编号为C46603开头的所有计数器。
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :对于支持5G的UE，MME不限制UE的5G接入时，MME可以将eNB提供的NR用量信息投递给SGW/PGW。 
配置前提 :已开启支持NSA的License功能。 
配置过程 :使用[SET NSA CONTROL POLICY]命令，配置开启支持SGW用量报告和支持PGW用量报告功能。
配置实例 :场景说明 :MME可以将eNB提供的NR用量信息投递给SGW/PGW。 
配置步骤 :步骤|说明|操作
---|---|---
1|支持NSA。|SET NSA CONTROL POLICY:SUPNSA="YES";
2|支持向SGW和PGW上报用量。|SET NSA CONTROL POLICY:SUPSGWUSEDATARPT="YES",SUPPGWUSEDATARPT="YES";
3|传送配置。|SYNA;
调整特性 :该特性不涉及调整特性。 
测试用例 :测试项目|MME支持第二RAT用量数据上报
---|---
测试目的|MME支持第二RAT用量数据上报。
预置条件|MME支持NSA功能。
测试过程|使用SET NSA CONTROL POLICY命令，配置持SGW用量报告和支持PGW用量报告功能。
通过准则|MME支持第二RAT用量数据上报。
测试结果|–
常见问题处理 :无 
# ZUF-78-19 45G互操作 
概述 :功能描述 :4/5G互操作是指在5G网络信号覆盖不全、VoNR业务不支持、网络过载等情况下可能导致的用户在4G和5G网络间移动。移动过程中会话不连续和业务中断直接影响用户的业务体验，如语音类业务。
为了支持4/5G互操作，3GPP定义了4个4G/5G合一网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U，如[图1]所示。具有4G/5G能力的UE，需要选择这四个合一网元。
图1  4G和5G互操作架构图

根据MME和AMF间的N26接口是否部署，可以分为：
支持N26接口的互操作：AMF和MME间支持N26接口，网络可为UE提供4/5G互操作，以保证用户业务连续性，用户的移动性管理上下文和会话管理上下文都可以切换。 
支持无N26接口的互操作：AMF和MME间不支持N26接口，网络可为UE提供4G和5G间的互操作，以保证用户业务连续性，会话管理上下文可以切换。 
功能特性简介 :针对4/5G互操作的应用特点和应用场景，核心网为满足用户的业务连续性要求，提供了有效的解决方案。详细的解决方案如下表： 
方案特性|实现简述|特导链接
---|---|---
4/5G用户接入EPC|具有4G/5G接入能力的用户，可以通过LTE接入EPC，并有后续移动到5G的能力。MME识别UE具有5G接入能力，则选择融合的NF，包括UDM+HSS、SMF+PGW-C等。|ZUF-78-19-001 4/5G用户接入EPC
支持N26接口互操作|AMF和MME间支持N26接口，网络可为UE提供4G和5G间的互操作，以保证用户业务连续性。有N26接口时用户为单注册模式，支持如下的互操作流程：连接态4G->5G切换空闲态4G->5G注册更新连接态5G->4G切换空闲态5G->4G跟踪区更新|ZUF-78-19-002 支持N26接口互操作
支持无N26接口互操作|网络不支持N26接口，网络可为UE提供4G和5G间的互操作，以保证用户业务连续性。无N26接口互操作可支持：单注册模式用户双注册模式用户|ZUF-78-19-003 支持无N26接口互操作
## ZUF-78-19-001 4/5G用户接入EPC 
特性描述 :特性描述 :术语 :术语|含义
---|---
单注册模式|终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一。
双注册模式|终端具有4G和5G能力，可以同时接入4G系统和5G系统。
描述 :定义 :4/5G用户接入EPC，指具有4G/5G能力的UE，接入到EPC网络。 
4G和5G互操作，指具有4G/5G能力的UE，在4G和5G间移动时（包括重新接入、重选、切换），能保证用户的会话连续性。 
根据MME和AMF间是否有N26接口，4G和5G互操作可分为： 
Interworking with N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换移动性管理状态及会话管理状态。 
Interworking without N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换会话管理状态，但不交换移动性管理状态。 
又根据UE的能力分为： 
单注册模式：终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一，终端仅维护一套4G或5G移动性管理上下文。 
双注册模式：终端具有4G和5G能力，可以同时接入4G系统和5G系统，终端可以同时维护4G和5G移动性上下文。 
背景知识 :在5G网络信号覆盖不全、VoNR业务不支持、网络过载等情况下，都有可能导致4G/5G能力用户在4G和5G网络间移动。移动过程中会话连续性和业务中断时间直接影响用户的业务体验，如语音类业务。 
为了支持4G和5G互操作，3GPP定义了4个4G/5G合一网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U，如[图1]所示。具有4G/5G能力的UE，需要选择这四个合一网元。
图1  4G和5G互操作架构图

应用场景 :从应用场景和组网场景看，互操作典型场景包括如下几种： 
场景一：4/5G用户，接入到EPC（有N26接口） 
场景二：4/5G用户，接入到EPC（无N26接口） 
###### 场景一：4/5G用户，接入到EPC（有N26接口） 
AMF和MME间部署了N26接口，4/5G用户在4G接入到EPC，MME不给UE下发“支持无N26互操作”指示。 
###### 场景二：4/5G用户，接入到EPC（无N26接口） 
AMF和MME间没有部署N26接口，4/5G用户在4G接入到EPC，MME给UE下发“支持无N26互操作”指示。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户业务体验：在5G信号受限区域，可以在4G下为用户提供服务。热点区域增加5G覆盖，用户业务体验更好。
移动用户|在热点区域部署5G，终端用户业务体验更好。
实现原理 :系统架构 :本特性涉及的互操作架构图如[图2]所示。
图2  4G和5G互操作架构图

为了支持互操作，3GPP定义了4个4G/5G合一的网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U。 
涉及的网元 :NF/网元名称|NF/网元作用
---|---
UE|支持4G/5G接入支持有N26接口或/和无N26接口的互操作在4G和5G下移动时可保持用户IP不变
eNodeB|支持通过Handover方式移动到5G下的小区支持通过重接入等方式，使UE移动到5G下的小区
NR|支持通过Handover方式移动到4G下的小区支持通过重接入等方式，使UE移动到4G下的小区
MME|支持给UE下发“支持无N26互操作”指示对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等无N26接口，位置更新时，指示UDM+HSS支持N26接口
AMF|支持给UE下发“支持无N26互操作”指示对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等。无N26接口，位置更新时，指示UDM+HSS。支持N26接口
PGW-C+SMF|对4G/5G接入能力的终端，可以选择融合NF，如UPF+PGW-U、PCF+PCRF等根据RAT，支持5G PDU Session和4G PDN Connection的互相转换根据RAT，支持5G QoS Flow和4G Bearer的互相转换
PGW-U+UPF|支持用户在4G或5G接入下的用户面数据报文转发支持用户在4G和5G间的切换
PCF+PCRF|可同时下发4G和5G QoS等
UDM+HSS|可同时对用户签约4G和5G2、无N26接口，位置更新时，指示UDM+HSS，UDM+HSS可通知UE同时在MME和AMF上注册
协议栈 :4G和5G互操作时，与MME相关接口涉及： 
与UE间NAS接口 
与eNodeB间S1-MME接口 
与HSS间S6a接口 
与AMF间N26接口（当4G和5G互操作基于N26部署时） 
本网元实现 :MME支持有4/5G能力的终端接入EPC，MME支持有N26接口和无N26接口的4G和5G互操作，支持UE的单注册，也支持UE的双注册。 
业务流程 :基于N26接口的互操作（EPC流程）
EPC流程：由于需要和5G互操作，4G多个流程被波及而需修改，主要修改内容包括： 
对4G/5G用户，MME需选择和锚定融合的PGW-C+SMF、HSS+UDM等。PGW-C+SMF需选择和锚定融合的PGW-U+UPF、PCRF+PCF等。 
MME需给UE指示是否支持N26。 
对4G/5G用户，UE在PDN连接建立时，会分配PDU Session ID并在PCO中通知给网络侧。Interworking with N26时，PGW-C+SMF会为QoS Flow分配S-NSSAI、5G QoS等参数。 
4G/5G用户初始附着EPC
普通用户附着，参考23.401 5.3.2 Attach procedure。 
相对于普通附着，4G/5G用户初始附着有如下不同点： 
UE发送Attach Request时： 
如果之前在5GS中注册，UE在AS信令中提供GUMMEI（mapped from the 5G-GUTI），并指示"Mapped from 5G-GUTI"。 
如果之前在5GS中注册，UE在Attach Request消息中携带GUTI（mapped from the 5G-GUTI），并指示从5GC移动过来。 
如果UE支持5GC NAS，则在UE Core Network Capability IE中指示给MME支持N1 mode。 
附着过程中若需要激活PDN连接，则UE分配PDU Session ID，并在PCO中携带给SMF+PGW-C。 
HSS+UDM收到MME的Update Location Request消息后，会向AMF发送Nudm_UECM_DeregistrationNotification，通知AMF注销3GPP接入。 
附着过程中若需要激活PDN连接，MME选择融合的PGW-C+SMF。 
PGW-C+SMF会分配S-NSSAI、5G QoS等信息，并在PCO中携带给UE。 
若UE支持5GC NAS并且MME支持N26互操作，则MME下发Attach Accept消息时，“支持无N26互操作”为“不支持”。附着过程中若需要激活PDN连接，收到Attach Accept(Activate EPS Defaulst Bearer Request)消息时，UE保存PDU Session ID与5G QOS Rules、S_NSSAI之间的关系，以便向5G切换时使用。 
4G/5G用户TAU
普通用户TAU，参考23.401 5.3.3 Tracking Area Update procedures。 
相对于普通TAU，4G/5G用户TAU有如下不同点： 
UE发送TAU Request时： 
如果之前在5GS中注册，UE在AS信令中提供GUMMEI（mapped from the 5G-GUTI），并指示"Mapped from 5G-GUTI"。 
如果之前在5GS中注册，UE在TAU Request消息中携带GUTI（mapped from the 5G-GUTI），并指示从5GC移动过来。 
如果之前在5GS中注册，UE使用5G安全上下文对TAU Request进行完整性保护。 
HSS+UDM收到MME的Update Location Request消息后，会向AMF发送Nudm_UECM_DeregistrationNotification，通知AMF注销3GPP接入。 
若UE支持5GC NAS并且MME支持N26互操作，则MME下发TAU Accept消息时，“支持无N26互操作”为“不支持”。 
4G/5G用户建立PDN连接
普通用户建立PDN连接，参考23.401 5.10.2 UE requested PDN connectivity。 
相对于普通建立PDN连接，4G/5G用户建立PDN连接有如下不同点： 
UE发起会话建立请求，在PCO中携带PDU Session ID。 
MME判断出是4G/5G用户，则选择PGW-C+SMF。 
PGW-C+SMF接收到Create Session Reqeust消息，保存PDU Session ID。 
PGW-C+SMF选择PCF。 
PGW-C+SMF向PCF并且请求会话策略；若PCF签约4G/5G QoS，则通过Condition Data将两份策略都下发给PGW-C+SMF。 
PGW-C+SMF收到会话策略后，进行承载绑定；若支持with N26互操作，则生成5G QOS Rules，并为UE分配S-NSSAI。 
PGW-C+SMF选择PGW-U+UPF，通知其建立N4会话，仅仅下发EPC的数据处理策略及隧道资源。 
PGW-C+SMF向MME返回Create Session Response消息，通过PCO将S_NSSAI和5G QoS携带给UE。 
UE收到Activate EPS Defaulst Bearer Request消息时，保存PDU Session ID与5G QOS Rules、S_NSSAI之间的关系，以便向5G切换时使用。 
4G/5G用户专有承载建立
普通用户专有承载建立，参考23.401 5.4.1 Dedicated bearer activation。 
相对于普通专有承载建立，4G/5G用户专有承载建立有如下不同点： 
某种条件触发PCF更新会话策略信息。 
PGW-C+SMF收到会话策略后，进行承载绑定；同时，若支持with N26互操，生成5G QoS Rules。 
PGW-C+SMF通知PGW-U+UPF更新N4会话。 
PGW-C+SMF向MME发送Create Bearer Request，若支持with N26互操作，通过PCO携带5G QoS Rules。 
MME向UE发送ACTIVATE EPS BEARER CONTEXT REQUEST消息，携带PCO（5G QoS Rules）。UE获取最新的5G QoS Rules，保存之，以便向5G切换时使用。 
4G/5G用户修改承载
普通用户修改承载，参考23.401 5.4.2 Bearer modification with bearer QoS update和5.4.3 PDN GW initiated bearer modification without bearer QoS update。 
相对于普通修改承载，4G/5G用户修改承载有如下不同点： 
某种条件触发PCF更新会话策略信息。 
PGW-C+SMF收到会话策略后，进行承载绑定，决策出需要更新承载QoS、TFT等；同时，若支持with N26互操，更新5G QoS Rules。 
PGW-C+SMF通知PGW-U+UPF更新N4会话。 
PGW-C+SMF向MME发送Update Bearer Request，若支持with N26互操作，通过PCO携带5G QoS Rules。 
MME向UE发送MODFIY EPS BEARER CONTEXT REQUEST消息，携带PCO（5G QoS Rules）。UE获取最新的5G QoS Rules，保存之，以便向5G切换时使用。 
4G/5G用户删除承载
普通用户删除承载，参考23.401 5.4.4.1 PDN GW initiated bearer deactivation。 
相对于普通删除承载，4G/5G用户删除承载有如下不同点： 
某种条件触发PCF更新会话策略信息。 
PGW-C+SMF收到会话策略后，进行承载绑定，决策出需要删除专有承载QoS、TFT等；同时，若支持with N26互操，更新5G QOS Rules。 
PGW-C+SMF通知PGW-U+UPF更新N4会话。 
PGW-C+SMF向MME发送Delete Bearer Request，通过PCO删除此专有承载对应的5G QoS Rules。 
MME向UE发送DEACTIVATE EPS BEARER CONTEXT REQUEST消息，携带PCO（5G QoS Rules）。UE删除去激活承载对应的5G QoS Rules。 
基于无N26接口的互操作（EPC流程）
由于需要和5G互操作，4G也有流程被波及而需修改，主要修改内容包括： 
对4G/5G用户，MME需选择和锚定融合的PGW-C+SMF、HSS+UDM等。PGW-C+SMF需选择和锚定融合的PGW-U+UPF、PCRF+PCF等。 
MME需给UE指示是否支持N26。 
对4G/5G用户，UE在PDN连接建立时，会分配PDU Session ID并在PCO中通知给网络侧。 
4G/5G用户初始附着EPC
普通用户附着，参考23.401 5.3.2 Attach procedure。 
相对于普通附着，4G/5G用户初始附着有如下不同点： 
UE发送Attach Request时：如果为单注册模式UE，UE指示从5GC移动过来，如果UE有native EPS GUTI ，则提供native EPS GUTI ，否则提供IMSI。如果为双注册模式UE，UE指示从5GC移动过来，提供native EPS GUTI。如果UE发送了TAU，且被MME因为不能获取UE标识信息拒绝了，则提供IMSI。如果附着消息中携带了PDN连接，且UE想继续保留该PDN连接的会话连续性，则把Request type 设置为"Handover"，并在PCO中携带PDU Session ID。 
HSS+UDM收到MME的Update Location Request消息后，不会向AMF发送Nudm_UECM_DeregistrationNotification通知AMF注销3GPP接入。 
若UE支持5GC NAS并且MME支持无N26互操作，则MME下发Attach Accept消息时，携带“支持无N26互操作”指示。 
如果PDN连接建立，则MME把APN和PGW ID对应关系通知给HSS+UDM。 
4G/5G用户TAU
普通用户TAU，参考23.401 5.3.3 Tracking Area Update procedures。 
相对于普通TAU，4G/5G用户TAU有如下不同点： 
UE发送TAU Request时： 
如果之前在5GS中注册，UE在TAU Request消息中携带GUTI（mapped from the 5G-GUTI），并指示从5GC移动过来。 
HSS+UDM收到MME的Update Location Request消息后，不会向AMF发送Nudm_UECM_DeregistrationNotification通知AMF注销3GPP接入。 
若UE支持5GC NAS并且MME支持N26互操作，则MME下发TAU Accept消息时，携带“支持无N26互操作”指示。 
4G/5G用户建立PDN连接
普通用户建立PDN连接，参考23.401 5.10.2 UE requested PDN connectivity。 
相对于普通建立PDN连接，4G/5G用户建立PDN连接有如下不同点： 
UE发起会话建立请求，在PCO中携带PDU Session ID。 
MME判断出是4G/5G用户，则选择PGW-C+SMF。 
PGW-C+SMF接收到Create Session Reqeust消息，保存PDU Session ID。 
PGW-C+SMF选择PCF。 
PGW-C+SMF向PCF并且请求会话策略。 
PGW-C+SMF收到会话策略后，进行承载绑定；若不支持with N26互操作，则不生成5G QOS Rules，也不需为UE分配S-NSSAI。 
PGW-C+SMF选择PGW-U+UPF，通知其建立N4会话，仅仅下发EPC的数据处理策略及隧道资源。 
MME把APN和PGW ID对应关系通知给HSS+UDM。 
网元选择
MME选择PGW-C+SMF
对4G/5G用户，MME需选择和锚定融合的PGW-C+SMF。 
可以根据配置，确定选择融合的PGW-C+SMF的策略。 
终端能力和签约信息。如果UE Network Capability中的N1 mode值为1，并且根据签约值和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC，APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合的PGW-C+SMF。 
签约信息。如果根据签约值和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC，APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合的PGW-C+SMF。 
终端能力。如果UE Network Capability中的N1 mode值为1，则选择融合的PGW-C+SMF。 
MME通过APN FQDN向DNS Server发现PGW-C+SMF。APN FQDN的'app-protocol'需要增加nc-smf： 
x-3gpp-pgw:x-s5-gtp+nc-smf和x-3gpp-pgw:x-s8-gtp+nc-smf。 
AMF选择PGW-C+SMF
PGW-C+SMF将PGW Node Name（PGW FQDN）上报给NRF。 
UE从4G网络迁移到5G网络后，MME将PGW Node Name传递给AMF，AMF根据该信息向NRF进行查询，发现该PGW-C+SMF。 
MME选择AMF
5G到4G TAU流程中，MME根据UE上报的映射4G GUTI中包含的AMF的GUAMI，查询AMF。可以根据配置，确定选择AMF的方式。 
MME-FQDN。MME把AMF的GUAMI，映射为MME-FQDN，把AMF看做MME进行DNS查询。 
映射后的MME-FQDN的格式为： 
mmec<MMEC>.mmegi<MMEGI>.mme.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。Service Parameter为"x-3gpp-mme:x-s10"。 
AMF-FQDN。MME直接使用AMF-FQDN，进行DNS查询。 
AMF-FQDN的格式为： 
pt<AMF Pointer>.set<AMF Set Id>.region<AMF Region Id>.amfi.5gc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。Service Parameter为"x-3gpp-amf:x-n26"。 
4G到5G的Handover流程中，MME通过Source eNB上报的Target 5G TAI信息构造5G TAI FQDN，5G TAI FQDN格式如下： 
tac-lb<TAC-low-byte>.tac-mb<TAC-middle-byte>.tac-hb<TAC-high-byte>.5gstac. 5gc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。Service Parameter为"x-3gpp-amf:x-n26"。如果UDM签约了UE Usage Type，则Service Parameter为"x-3gpp-amf:x-n26 +ue-<ue usage type>"。 
AMF选择MME
4G到5G注册区域更新流程中，AMF根据UE上报的映射5G GUTI中包含的GUAMI转换为GUMMEI构造FQDN进行DNS查询，FQDN的格式为：mmec<MMEC>.mmegi<MMEGI>.mme.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。Service Parameter为"x-3gpp-mme:x-s10"。 
5G到4G的Handover流程中，AMF通过Source gNB上报的Target 4G TAI信息构造4G TAI FQDN，4G TAI FQDN格式如下： 
tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.tac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。Service Parameter为"x-3gpp-mme:x-s10"。如果UDM签约了UE Usage Type，则Service Parameter为"x-3gpp-mme:x-s10 +ue-<ue usage type>"。 
系统影响 :4G与5G互操作，会增加跨RAT的流程，影响系统的话务模型。 
部署了N26接口时，从5G到4G的Handover流程和TAU流程。 
部署了N26接口时，从4G到5G的Handover流程和Registration Update流程。 
没有部署N26接口时，从5G到4G的TAU流程，附着流程，PDN连接建立流程，专有承载建立流程。 
没有部署N26接口时，从4G到5G的Registration流程，PDU Session建立流程，专有QoS flow建立流程。 
为了减少对系统的影响，需尽可能减少垮RAT互操作次数，重叠区要合理规划，避免频繁的跨RAT互操作。 
应用限制 :协议版本：2019年9月份。 
如果需支持N26接口的互操作，则MME需支持承载级的PCO/ePCO（通过PCO/ePCO携带5G QoS flow对应的S-NSSAI、5G QoS等）。 
4G MME的GUMMEI和5G AMF的GUAMI规划时尽量不重叠。如果重叠了，一方面RAN选择MME时，真实的GUMMEI和映射的GUMMEI都匹配，导致选择合一的CN节点可能失败，也会导致各个CN节点的负荷可能不均；另一方面，如果MME使用MME-FQDN选择AMF时，会导致可能选择错误的AMF，必须要求MME使用AMF-FQDN选择AMF才可以避免。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|System Architecture for the 5G System
3GPP|TS 23.502|Procedures for the 5G System
3GPP|TS 23.503|Policy and Charging Control Framework for the 5G System
3GPP|TS 29.274|Tunnelling Protocol for Control plane (GTPv2-C); Stage 3
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为下表所示，只有在License项目显示为“支持”时，MME才支持与5GS的互操作功能： 
LICENSE项|归属NF|备注
---|---|---
MME支持N26互操作|SGSN&MME|MME部署了N26接口，支持4G和5G间有N26接口互操作
MME支持无N26互操作|SGSN&MME|MME没有部署N26接口，支持4G和5G间无N26接口互操作
对其他网元的要求 :要求参与互操作的各网元功能，均依据3GPP协议规定。 
UE|eNodeB/gNodeB|SGW|PGW+SMF|HSS+UDM|AMF
---|---|---|---|---|---
-|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :规划基于N26接口互操作还是无N26接口互操作。 
如果基于N26接口互操作，需分别规划AMF和MME的N26接口的GTPC地址和VRF。 
如果基于N26接口互操作，DNS Server中需增加AMF的解析数据。需要确认解析AMF的方式，如果为根据MME-FQDN解析，则4G GUMMEI和5G GUAMI不能重叠。 
如果需要RAN选择合一的AMF+MME节点，则4G GUMMEI和5G GUAMI不能重叠。 
NR需配置4G邻接小区信息等，eNB需配置5G邻接小区信息等。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令45G互操作配置SHOW 5GC INTERWORKINGSET 5GC INTERWORKING表2  修改配置项配置项命令新增参数EPC地址解析ADD EPCHOSTSERVICE 和PROTOCOL类型增加MME本地解析APNADD EPC APNPROTOCOL类型增加根据PGW NAME解析PGWADD EPC PGWPROTOCOL类型增加N26VRF配置SET VRFCFGN26VRF 
性能统计 :性能计数器名称
---
C430000158 基于N26附着请求次数
C430000159 基于N26附着成功次数
C430000160 无N26接口附着请求次数
C430000161 无N26接口附着成功次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该配置过程实现支持4/5G用户接入EPC功能。 
配置前提 :已同时部署5GC和EPC系统 
AMF和MME之间存在N26接口 
各网元基本业务正常 
配置过程 :开启License中的“MME支持N26互操作”或“MME支持无N26互操作”。 
在EM客户端配置页面的左侧命令树中，展开MME节点，选择NFS_MMESGSN_0节点。
执行[SET 5GC INTERWORKING]命令，配置MME的互操作开关、互操作模式以及是否支持AMF FQDN查询。
执行[ADD EPCHOST]命令，增加协议类型为PROTOCOL=“x-s10”或PROTOCOL=”x-n26“,服务类型为SERVICE="x-3gpp-mme"或SERVICE="x-3gpp-amf"的解析配置。用来配置MME本地解析AMF的地址。
(如果SET 5GC INTERWORKING:IFSPRTAMFQUERY="YES"，则协议类型用“x-n26“，服务类型为SERVICE="x-3gpp-amf"，如果如果SET 5GC INTERWORKING:IFSPRTAMFQUERY="NO"，则协议类型用“x-s10"，服务类型为SERVICE="x-3gpp-mme")。 
执行[ADD EPC APN]命令，增加协议类型为“x-s5-gtp+nc-smf”和“x-s8-gtp+nc-smf”的解析配置。配置MME本地解析APN，选择合一的PGW+SMF的地址。
执行[ADD EPC PGW]命令，增加协议类型为“x-s5-gtp+nc-smf”和“x-s8-gtp+nc-smf”的解析配置。配置MME根据PGW NAME解析PGW的地址。
执行[SET VRFCFG]命令，配置N26接口的VRF。
配置实例 :场景说明 :4/5G用户接入EPC。 
数据规划 :配置项|参数名称|取值
---|---|---
5GC互操作基本配置|互操作模式|有N26（WITHN26）
支持N26互操作|5GC互操作基本配置|支持
支持无N26互操作|5GC互操作基本配置|支持
MME本地解析的AMF地址配置|AMF地址|6.6.6.6
FQDN|MME本地解析的AMF地址配置|mmec55.mmegi5555.mme.epc.mnc011.mcc460.3gppnetwork.org
APN解析|APN|cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org
合一的PGW+SMF地址|APN解析|192.20.53.100
PGW解析|PGWNAME|pgw.n26.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
PGW地址|PGW解析|192.20.51.36
N26口VRF配置|N26口的VRF|1
配置步骤 :步骤|说明|操作
---|---|---
1|配置MME支持N26模式|SET 5GC INTERWORKING:MODE="WITHN26",SUPWITHN26="SUPWITHN26",SUPWITHOUTN26="SUPWITHOUTN26"
2|配置MME本地解析AMF的地址:方式1-按MME FQDN格式解析|SET 5GC INTERWORKING:IFSPRTAMFQUERY="NO"ADD EPCHOST:NAME="mmec55.mmegi5555.mme.epc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="amfn26",IPADDR="6.6.6.6",PROTOCOL="x-n26",NAPTRORDER=0,NAPTRWEIGHT=200,UEUSAGETYPE="NORMAL"
配置MME本地解析AMF的地址:方式2-按AMF FQDN格式解析|2|SET 5GC INTERWORKING:IFSPRTAMFQUERY="YES"ADD EPCHOST:NAME="pt15.set155.region55.amfi.5gc.mnc011.mcc460.3gppnetwork.org",SERVICE="x-3gpp-amf",HOST="amfn26",IPADDR="6.6.6.6",PROTOCOL="x-n26",NAPTRORDER=0,NAPTRWEIGHT=200,UEUSAGETYPE="NORMAL"
3|配置MME本地解析APN，选择合一的PGW+SMF的地址|ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw.n26.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="192.20.53.100",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp+nc-smf&x-s8-gtp+nc-smf",NAPTRORDER=0,NAPTRWEIGHT=200,UEUSAGETYPE="NORMAL"
4|配置MME根据PGW NAME解析PGW的地址|ADD EPC PGW:PGWNAME="pgw.n26.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="192.20.51.36",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp+nc-smf&x-s8-gtp+nc-smf",UEUSAGETYPE="NORMAL"
5|配置N26口的VRF|SET VRFCFG:N26VRF=1;
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|无N26场景，用户接入EPC
---|---
测试目的|用户正常接入EPC。
预置条件|系统运行正常。MME支持无N26模式。
测试过程|UE之前在5G中注册，向EPC发起attach  request。Attach Request消息中携带GUTI（mapped from the 5G-GUTI），携带UE STATUS指示从5GC移动过来。并在UE网络能力中指示支持N1 MODE。MME执行正常的附着流程。MME判断是5G到4G的附着，且用户支持N1 MODE ,MME选择融合的SMF+PGW-C。MME在下发attach  accept时，指示支持无N26。
通过准则|用户正常接入EPC。
测试结果|–
测试项目|有N26场景，用户接入EPC
---|---
测试目的|用户正常接入EPC。
预置条件|系统运行正常。MME支持有N26模式。
测试过程|UE之前在5G中注册，向EPC发起attach  request。Attach Request消息中携带GUTI（mapped from the 5G-GUTI），携带UE STATUS指示从5GC移动过来。并在UE网络能力中指示支持N1 MODE。MME执行正常的附着流程。MME判断是5到4的附着，且用户支持N1MODE ,MME选择融合的SMF+PGW-C。MME在下发attach  accept时，指示不支持无N26。
通过准则|用户正常接入EPC。
测试结果|–
常见问题处理 :无。 
## ZUF-78-19-002 支持N26接口互操作 
特性描述 :特性描述 :术语 :术语|含义
---|---
单注册模式|终端具有4G和5G能力，但同时只能接入4G或者5G系统其中之一。
双注册模式|终端具有4G和5G能力，可以同时接入4G和5G系统。
描述 :定义 :4G和5G互操作，指具有4G/5G能力的UE，在4G和5G间移动时（包括重新接入、重选、切换），能保证用户的会话连续性。 
根据MME和AMF间是否有N26接口，4G和5G互操作可分为： 
Interworking with N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换移动性管理状态及会话管理状态。 
Interworking without N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换会话管理状态，但不交换移动性管理状态。 
又根据UE的能力分为： 
单注册模式：终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一，终端仅维护一套4G或5G移动性管理上下文。 
双注册模式：终端具有4G和5G能力，可以同时接入4G系统和5G系统，终端可以同时维护4G和5G移动性上下文。 
背景知识 :在5G网络信号覆盖不全、VoNR业务不支持、网络过载等情况下，都有可能导致4G/5G能力用户在4G和5G网络间移动。移动过程中会话连续性和业务中断时间直接影响用户的业务体验，如语音类业务。 
为了支持4G和5G互操作，3GPP定义了4个4G/5G合一网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U，如[图1]所示。具有4G/5G能力的UE，需要选择这四个合一网元。
图1  4G和5G互操作架构图

应用场景 :从应用场景和组网场景看，互操作典型场景包括如下几种： 
场景一：5G重新接入到4G或4G重新接入到5G（有N26接口） 
场景二：5G重选到4G或4G重选到5G（有N26接口） 
场景三：5G切换到4G或4G切换到5G（有N26接口） 
###### 场景一5G重新接入到4G或4G重新接入到5G（有N26接口） 
AMF和MME间部署了N26接口，UE之前在4G接入，因为各种原因（如登机关机等），UE重新接入到5G。或UE之前在5G接入，再重新接入到4G。 
该方式会话重新接入，AMF和MME间通过N26接口交换用户标识等信息。 
###### 场景二：5G重选到4G或4G重选到5G（有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。UE之前在4G接入，移动到5G无线覆盖区域，UE重选到5G。 
该互操作方式会话保持不变，业务中断时间较短， AMF和MME间通过N26接口交换移动性管理上下文和会话上下文等信息。 
###### 场景三：5G切换到4G或4G切换到5G（有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。UE之前在4G接入，移动到5G无线覆盖区域，eNB把UE从4G切换到5G。 
该互操作方式会话保持不变，业务不中断， AMF和MME间通过N26接口交换移动性管理上下文和会话上下文等信息。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户业务体验：在5G信号受限区域，可以在4G下为用户提供服务。热点区域增加5G覆盖，用户业务体验更好。
移动用户|在热点区域部署5G，终端用户业务体验更好。
实现原理 :系统架构 :本特性涉及的互操作架构图如[图2]所示。
图2  4G和5G互操作架构图

为了支持互操作，3GPP定义了4个4G/5G合一的网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U。 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
UE|支持4G/5G接入支持有N26接口或/和无N26接口的互操作在4G和5G下移动时可保持用户IP不变
eNodeB|支持通过Handover方式移动到5G下的小区支持通过重接入等方式，使UE移动到5G下的小区
NR|支持通过Handover方式移动到4G下的小区支持通过重接入等方式，使UE移动到4G下的小区
MME|支持给UE下发“支持无N26互操作”指示对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等无N26接口，位置更新时，指示UDM+HSS支持N26接口
AMF|支持给UE下发“支持无N26互操作”指示对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等。无N26接口，位置更新时，指示UDM+HSS。支持N26接口
PGW-C+SMF|对4G/5G接入能力的终端，可以选择融合NF，如UPF+PGW-U、PCF+PCRF等根据RAT，支持5G PDU Session和4G PDN Connection的互相转换根据RAT，支持5G QoS Flow和4G Bearer的互相转换
PGW-U+UPF|支持用户在4G或5G接入下的用户面数据报文转发支持用户在4G和5G间的切换
PCF+PCRF|可同时下发4G和5G QoS等
UDM+HSS|可同时对用户签约4G和5G、无N26接口，位置更新时，指示UDM+HSS，UDM+HSS可通知UE同时在MME和AMF上注册
协议栈 :4G和5G互操作时，与MME相关接口涉及： 
与UE间NAS接口 
与eNodeB间S1-MME 
与HSS间S6a接口 
与AMF间N26接口（当4G和5G互操作基于N26部署时） 
本NF/网元实现 :MME支持有N26接口和无N26接口的4G和5G互操作，支持UE的单注册，也支持UE的双注册。 
业务流程 :5G到4G的切换（N26）
本特性涉及的业务流程图如[图3]所示，流程协议详细描述可参见3GPP 23.502 4.11.1.2.1 5GS to EPS handover using N26 interface。
图3  N26接口5GS到EPS的切换

0. UE在5GS中注册，建立PDU Session和QoS Flow。 
1. NR确定发起到E-UTRAN的切换，给AMF发送Handover Required消息，携带Target eNB ID, Source to Target Transparent Container, inter system handover indication等信息。 
2. AMF根据Target eNB ID确定是到E-UTRAN的切换，选择一个合适的MME。AMF向PGW-C+SMF发送Nsmf_PDUSession_Context Request消息获取用户会话上下文，携带MME的non-IP PDN Type支持能力等信息，PGW-C+SMF向PGW-U+UPF触发N4 Session modification过程，建立EPS Bearer的CN隧道信息。PGW-C+SMF向AMF返回Nsmf_PDUSession_Context Response消息，携带PDU Session上下文等信息。如果PDU Session Type为Ethernet or Unstructured，则PGW-C+SMF把其设置为non-IP PDN Type。AMF仅对分配了EBI的PDU Session向PGW-C+SMF获取用户会话上下文。 
3. AMF发送Forward Relocation Request消息给MME。 
4. MME选择SGW，向SGW发送Create Session Request消息。SGW返回Create Session Response消息。 
5. MME向Target eNB发送Handover Request消息。 
6. Target eNB返回Handover Request Ack消息。 
7. 如果需要创建非直传隧道，MME通知SGW创建非直传隧道。MME设置定时器用于监测非直接数据前转隧道资源的释放。 
8 MME返回Forward Relocation Response消息。 
9. 如果非直接数据前转被使用，则AMF通知SMF建立非直接数据前转隧道。 
10. AMF发送Handover Command消息给NR，携带 Transparent container (radio aspect parameters that the target eNB has set-up in the preparation phase), CN tunnel info for data forwarding per PDU Session, QoS flows for Data Forwarding等信息。 
11. source NR发送HO Command消息给UE通知UE切换到目标接入网络。UE删除没有分配EBI的PDU Session和QoS flow。 
12. UE切换到目标小区，给eNB发送Handover Complete消息。 
13. eNB给MME发送Handover  Notify消息。 
14. MME通知AMF切换完成。 
15. AMF设置定时器用于监测NR和PGW-C+SMF的资源释放，给MME返回切换完成确认消息。 
16. MME给SGW发送Modify Bearer Request消息，通知eNB用户面隧道等信息。 
SGW给PGW-C+SMF发送Modify Bearer Request消息。 
PGW-C+SMF删除没有缺省QoS flow没有EBI的PDU Session。 
PGW-C+SMF向UPF+PGW-U触发N4 Session Modification过程，更新用户面路径。PGW-C+SMF向SGW返回Modify Bearer Response消息。 
SGW向MME返回Modify Bearer Response消息。 
17. UE发起TAU流程。在该流程中，AMF可以通知UDM退订签约数据改变事件，释放AMF和NR的相关资源。  
18. 对于non-GBR的QoS Flow，PGW-C+SMF可以发起专有承载建立流程。 
19. 如果资源保护监测定时器超时，且建立了非直接数据前转隧道，则MME通知SGW释放非直接数据前转隧道资源。 
20. 如果资源保护监测定时器超时，且建立了非直接数据前转隧道，则AMF通知PGW-C+SMF释放非直接数据前转隧道资源。 
4G到5G的切换（N26）
本特性涉及的业务流程图如下图所示，流程协议详细描述可参见3GPP 23.502 4.11.1.2.2 EPS to 5GS handover using N26 interface。 
切换流程分为切换准备阶段和切换执行阶段。 
切换准备阶段如下图所示。 
图4  准备阶段

切换准备阶段流程说明如下： 
1. eNB确定发起切换。 
2. eNB向MME发送Handover Required消息，携带Target ID, Source to Target Transparent Container等信息。 
3. MME根据Target ID确定是到NR的切换，选择一个AMF。MME给AMF发送Forward Relocation Request消息。AMF把EPS MM上下文转换为5GS MM上下文。AMF通过PGW-FQDN向NRF查询获取PGW-C+SMF。 
4. AMF发送Nsmf_PDUSession_CreateSMContext Request消息给PGW-C+SMF，携带UE EPS PDN Connection, AMF ID, Direct Forwarding Flag等信息。 
5. 如果动态PCC被部署，则PGW-C+SMF可以向PCF+PCRF触发SMF发起的SM策略修改。 
6. GW-C+SMF可以向PGW-U+UPF发送N4 会话修改。 
7. PGW-C+SMF返回Nsmf_PDUSession_CreateSMContext Response消息给AMF，携带PDU Session ID, S-NSSAI, N2 SM Information (PDU Session ID, S-NSSAI, QFI(s), QoS Profile(s), EPS Bearer Setup List, CN Tunnel-Info, cause code)等信息。 
8. AMF发送Handover Request消息给NR，携带Source to Target Transparent Container, N2 SM Information (PDU Session ID, S-NSSAI, QFI(s), QoS Profile(s), EPS Bearer Setup List, V-CN Tunnel Info)等信息。 
9. NR返回Handover Request Acknowledge消息给AMF，携带Target to Source Transparent Container, N2 SM response (PDU Session ID, list of accepted QFI(s) and AN Tunnel Info), T-RAN SM N3 forwarding info list (PDU Session ID, N3 Tunnel Info for data forwarding)等信息。 
10. AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU Session ID, N2 SM response (list of accepted QFI(s) and AN Tunnel Info), T-RAN SM N3 forwarding info list (PDU Session ID, N3 Tunnel Info for data forwarding)) 等信息。 
11. PGW-C+SMF向PGW-U+UPF 指示NR的N3 UP address和Tunnel ID等信息。 
12. PGW-C+SMF向AMF返回Nsmf_PDUSession_UpdateSMContext Response 消息，携带PDU Session ID, EPS Bearer Setup List, CN tunnel information for data forwarding等信息。 
13. AMF给MME返回Forward Relocation Response消息，携带Cause, Target to Source Transparent Container, Serving GW change indication, CN Tunnel Info for data forwarding, EPS Bearer Setup List, AMF Tunnel Endpoint Identifier for Control Plane, Addresses and TEIDs等信息。 
14. 如果非直接数据前转隧道被使用，则MME向SGW创建非直接数据前转隧道。 
切换执行阶段如下图所示。 
图5  执行阶段

流程说明如下： 
1. MME给eNB发送Handover Command消息，通知eNB切换。 
2. eNB给UE发送Handover Command消息，通知UE切换。 
3. UE切换到目标小区后，给NR发送Handover Confirm消息。 
4. NR给AMF发送Handover Notify消息，通知AMF切换完成，消息中携带 N2 SM Information (N3 DL AN Tunnel Info)等信息. 
5. AMF向MME发送Forward Relocation Complete Notification消息。 
6. MME向AMF返回Forward Relocation Complete Notification Ack消息。 
7. AMF向PGW-C+SMF发送Nsmf_PDUSession_UpdateSMContext Request 消息，携带Handover Complete indication for PDU Session ID等信息。  
8. PGW-C+SMF向PGW-U+UPF发起N4会话修改，指示用户面路径已切换到NR。 
9. 如果PCC被部署，则PGW-C+SMF通知PCF + PCRF信息改变，如RAT Type和UE Location等信息。 
10. PGW-C+SMF向AMF范湖Nsmf_PDUSession_UpdateSMContext Response消息，携带PDU Session ID等信息。  
11. UE完成切换后注册过程。 
12. MME释放源侧资源。 
5G到4G的重选（N26）
本特性涉及的业务流程图如下图所示，流程协议详细描述可参见3GPP 23.502 4.11.1.3.2 5GS to EPS Idle mode mobility using N26 interface。 
图6  5GS to EPS Idle mode mobility using N26 interface

流程说明如下： 
1. UE检测需发起RAT改变的TAU流程。 
2. UE发送TAU请求消息给eNB。 
3. eNB发送TAU请求消息给MME。 
4. MME选择合适的AMF，给AMF发送Context Request消息。 
5. AMF确定TAU请求消息后，向PGW-C+SMF发送 Nsmf_PDUSession_Context Request消息。如果CN Tunnel Info由PGW-U+UPF分配,则PGW-C+SMF发送N4 Session Modification Request消息给PGW-U+UPF，为EPS bearer建立隧道。PGW-C+SMF返回Nsmf_PDUSession_Context Response消息，携带mapped EPS bearer contexts等信息。 
6. AMF向MME返回Context Response消息，携带mapped MM context 、SM EPS UE Context (default and dedicated GBR bearers) 等信息。 
7. MME完成对UE的安全过程。 
8. MME向AMF返回Context Ack消息。 
9. MME选择合适的SGW，向SGW发送Create Session Request消息。 
10. SGW向PGW-C+SMF发送Modify Bearer Request消息。 
11 PGW-C+SMF向UPF+PGW-U触发N4 Session Modification过程。 
12. PGW-C+SMF向SGW返回Modify Bearer Response消息。 
13. SGW向MME返回Create Session Response消息。 
14. MME向UDM+HSS发送Location Update消息。 
15. UDM+HSS向AMF发送Nudm_UECM_DeregistrationNotification消息，通知AMF注销用户。 
16. UDM+HSS向MME返回Locaiton Update Ack消息。 
17. MME向UE发送TAU Accept消息，携带GUTI、TA List等信息。 
18. UE向MME返回TAU Complete消息。 
19. 对于non-GBR的QoS Flow，PGW-C+SMF可以发起专有承载建立流程。 
4G到5G的重选（N26）
本特性涉及的业务流程图如下图所示，流程协议详细描述可参见3GPP 23.502 4.11.1.3.3 EPS to 5GS Mobility Registration Procedure (Idle and Connected State) using N26 interface。 
图7  EPS to 5GS Mobility Registration Procedure (Idle and Connected State) using N26 interface

流程说明如下： 
1. UE移动到NR覆盖区域，检测到需发起注册流程。 
2. UE发送Registration Request消息给NR，携带registration type( set to "Mobility Registration Update")、5G-GUTI (mapped from EPS GUTI as the old GUTI)、native 5G-GUTI (if available) as additional GUTI 等信息。 
3. NR选择合适的AMF。 
4. NR向AMF转发Registration Request消息。 
5. AMF选择合适的MME，向MME发送Context Request消息。MME向AMF返回Context Response消息。 
6. 如果UE在注册请求消息中携带了5G-GUTI(5G-GUTI as Additional GUTI)，则Target AMF发送消息给Old AMF。Old AMF对注册请求消息进行完整性保护检查，如果通过，则给Target AMF返回UE的SUPI、MM Context等信息。 
7. AMF完成对UE的安全过程。 
8. AMF向MME返回Context Ack消息，携带Serving GW change indication等信息。 
9. 如果需对UE进行设备检查，则AMF完成对UE的Equipmet ID检查过程。 
10. AMF选择合适的UDM，向其发起注册过程。 
11. UDM向MME发送Cancel Location消息。 
12. MME返回Cancel Location Ack消息。 
13. 如果需向PCF建立AM Policy Association，则AMF向PCF发起AM Policy Association建立过程。 
14. AMF通知SMF更新信息。  
15. AMF向UE发送Registration Accept消息，携带5G-GUTI、TA List等信息。 
16. UE返回Registration Complete消息。 
系统影响 :4G与5G互操作，会增加垮RAT的流程，影响系统的话务模型。 
部署了N26接口时，从5G到4G的Handover流程和TAU流程。 

部署了N26接口时，从4G到5G的Handover流程和Registration Update流程。 
没有部署N26接口时，从5G到4G的TAU流程，附着流程，PDN连接建立流程，专有承载建立流程。 
没有部署N26接口时，从4G到5G的Registration流程，PDU Session建立流程，专有QoS flow建立流程。 
为了减少对系统的影响，需尽可能减少垮RAT互操作次数，重叠区要合理规划，避免频繁的跨RAT互操作。 
应用限制 :协议版本：2019年9月份。 
如果需支持N26接口的互操作，则MME需支持承载级的PCO/ePCO（通过PCO/ePCO携带5G QoS flow对应的S-NSSAI、5G QoS等）。 
4G MME的GUMMEI和5G AMF的GUAMI规划时尽量不重叠。如果重叠了，一方面RAN选择MME时，真实的GUMMEI和映射的GUMMEI都匹配，导致选择合一的CN节点可能失败，也会导致各个CN节点的负荷可能不均；另一方面，如果MME使用MME-FQDN选择AMF时，会导致可能选择错误的AMF，必须要求MME使用AMF-FQDN选择AMF才可以避免。 
特性交互 :无。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501-f60 System Architecture for the 5G System|全文
3GPP TS 23.502-f60 Procedures for the 5G System|全文
3GPP TS 23.503-f60 Policy and Charging Control Framework for the 5G System|全文
3GPP TS 29.274-f90 Tunnelling Protocol for Control plane (GTPv2-C); Stage 3|全文
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为下表所示，只有在License项目显示为“支持”时，MME才支持与5GS的互操作功能： 
LICENSE项|归属NF|备注
---|---|---
MME支持N26互操作|SGSN&MME|MME部署了N26接口，支持4G和5G间有N26接口互操作
MME支持无N26互操作|SGSN&MME|MME没有部署N26接口，支持4G和5G间无N26接口互操作
对其他网元的要求 :要求参与互操作的各网元功能，均依据3GPP协议规定。 
UE|eNodeB/gNodeB|SGW|PGW+SMF|HSS+UDM|AMF
---|---|---|---|---|---
-|√|√|√|√|√
工程规划要求 :规划基于N26接口互操作还是无N26接口互操作。如果基于N26接口互操作，需分别规划AMF和MME的N26接口的GTPC地址和VRF。如果基于N26接口互操作，DNS Server中需增加AMF的解析数据。需要确认解析AMF的方式，如果为根据MME-FQDN解析，则4G GUMMEI和5G GUAMI不能重叠。如果需要RAN选择合一的AMF+MME节点，则4G GUMMEI和5G GUAMI不能重叠。NR需配置4G邻接小区信息等，eNB需配置5G邻接小区信息等。 
O&M相关 :命令 :配置项|命令
---|---
AMF GTPC地址配置|SET AMFGTPCADDRCFG
SHOW AMFGTPCADDRCFG|AMF GTPC地址配置
MME地址解析配置|ADD MMEHOST
SET MMEHOST|MME地址解析配置
DEL MMEHOST|MME地址解析配置
SHOW MMEHOST|MME地址解析配置
AMF互操作配置|SET 5GINTERWORKCFG
SHOW 5GINTERWORKCFG|AMF互操作配置
特性配置 :特性配置 :配置说明 :该配置过程实现支持N26接口互操作功能。 
配置前提 :AMF和MME之间存在N26接口 
各网元基本业务正常 
配置过程 :开启License中的“AMF支持N26互操作”。 
通过[SET AMFGTPCADDRCFG]命令，配置AMF的GTPC地址和VRF。
通过[ADD MMEHOST]命令，配置MME的FQDN和地址之间的对应关系。
通过[SET 5GINTERWORKCFG]命令，配置支持N26互操作。
配置实例 :场景说明 :AMF和MME之间存在N26接口，用户在5G接入激活一个会话，移动到4G覆盖下，RAN发起5到4的切换，切换过程中进行数据业务。 
数据规划 :配置项|参数|取值
---|---|---
修改AMF GTPC地址配置|AMF GTPC地址|39.16.16.16
AMF N26 VRF|修改AMF GTPC地址配置|0
新增MME地址解析配置|FQDN|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org
主机名|新增MME地址解析配置|mme50.zte.com.cn
优先级|新增MME地址解析配置|1
权重|新增MME地址解析配置|50
地址池ID|新增MME地址解析配置|1
修改AMF互操作配置|支持N26互操作|支持N26互操作
支持无N26互操作|修改AMF互操作配置|不支持无N26互操作
互操作模式|修改AMF互操作配置|有N26
配置步骤 :修改AMF GTPC地址配置，命令如下。 
[SET AMFGTPCADDRCFG]:AMFGTPCADDRESS="39.16.16.16",AMFN26VRF=0
新增MME地址解析配置，命令如下。 
[ADD MMEHOST]:LOGICNAME="tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org",HOSTNAME="mme50.zte.com.cn",PRIORITY=1,WEIGHT=50,ADDRPOOLID=1
修改AMF互操作配置，命令如下。 
[SET 5GINTERWORKCFG]:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="NOSPRT",INTERWORKMODE="WITHN26"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|验证网络支持有N26互操作时5G到4G的切换
---|---
测试目的|用户从5G移动到4G覆盖下，RAN发起5G到4G的切换，业务不中断
预置条件|AMF和MME支持N26接口，UE已经在5G注册并激活了一个PDU会话，UE处于连接态
测试过程|用户从5G移动到4G覆盖下，RAN发起5G到4G的切换，HO Required中指示信息表明直传隧道可用切换的过程中，进行数据业务
通过准则|检查AMF根据Target ID中TAI选择目标MME正确检查AMF根据HO Required中指示信息表明直传隧道可用，AMF将不向SMF请求创建非直传隧道检查AMF将用户的移动性上下文及会话上下文等信息传递给MME检查MME收到源AMF的前转切换请求消息后，向SGW请求创建会话，消息正确，选择的PGW为与切换前相同检查N7口，SMF+PGW-C为切换的会话，向PCF进行策略更新，消息正确SMF+PGW-C将5G PDU连接切换为4G PDN会话，已分配给UE的IP地址保持不变检查UPF(PSA IP锚点)切换为PGW-U，所有流量路由到该PGW-U；UPF+PGW-U完成数据转发隧道的切换，释放N3/N9隧道资源，分配S5/S8-U or S1-U隧道资源检查计费报文发送正确切换过程中，数据通畅切换完成，检查所有5GC侧SMF、UPF会话及用户面资源被释放检查切换完成，UE使用映射的GUTI发起TAU流程，流程结束后：AMF中用户上下文被删除，UDM+HSS中只记录了MME的位置信息，AMF位置信息被清除，AMF与gNB间N2用户连接被释放，AMF与PCF间策略会话被删除
测试结果|–
测试项目|验证网络支持有N26互操作时4G到5G的切换
---|---
测试目的|网络支持有N26互操作，用户从4G移动到5G覆盖下，RAN发起4G到5G的切换，业务不中断
预置条件|AMF和MME之间存在N26接口，4/5G终端在4G初始注册并激活了一个PDN连接，RAN支持直传隧道
测试过程|UE从4G移动到5G覆盖下，RAN发起4G到5G的切换，HO Required中指示信息表明直传隧道可用，用户处于连接态，切换的过程中，进行数据业务，切换过程不需要重选UPF
通过准则|检查MME可以正确识别并处理UE发送的Handover Required消息的Handover Type、Target ID、Source to Target Container等字段检查AMF根据TAI选择SMF正确检查HO Required消息中有直传隧道指示可用。MME不创建非直传隧道检查MME发送Forward Relocation Request消息给AMF，携带IMSI、4G MM上下文、EPS PDN连接、Source To Target Container，各消息字段正确检查AMF选择PCF正确，向PCF发送的Npcf_AMPolicyControl_Create Request中携带SUPI、RAT Type、PLMN等字段正确检查AMF根据MME携带过来的PGW FQDN，通过NRF查询PGW FQDN对应SMF+PGW-C的服务化地址正确检查AMF针对每个PDN连接，发送Nsmf_PDUSession_UpdateSMContext Request给SMF+PGW-C，携带EPS PDN连接、AMF ID以及切换准备指示等字段正确检查N7口，SMF+PGW-C为切换的会话，向PCF进行策略更新消息正确检查SMF+PGW-C向AMF响应UpdateSMContext Response，携带包括PDU Session ID、S_NSSAI、n2SmContainer(PDU Session ID, S-NSSAI, QFI(s), QoS Profile(s), EPS Bearer Setup List）信息正确检查AMF和目标NR之间的Handover Request/Acknowledge消息中各字段正确检查SMF+PGW-C将4G PDN连接切换为5G PDU会话，已分配给UE的IP地址保持不变；并向UDM进行会话信息的注册，消息字段正确检查UPF+PGW-U完成数据转发隧道的切换，PGW-U隧道资源被释放，分配N3/N9隧道资源正确直传隧道前传报文转发是RAN间直接转检查成功切换的承载/QOSFlow，触发计费更新，话单正确切换的过程中，媒体面数据通畅检查切换后，EPC侧SGW、PGW 会话及用户面资源被释放，无资源挂死检查切换完成，UE使用映射的GUTI发起注册更新流程结束后，MME中用户上下文被删除，UDM+HSS中只记录了AMF的位置信息，MME位置信息被清除，MME与eNB间S1用户连接被释放，AMF与PCF间建立了策略会话关联
测试结果|–
常见问题处理 :无。 
## ZUF-78-19-003 支持无N26接口互操作 
特性描述 :特性描述 :术语 :术语|含义
---|---
单注册模式|终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一。
双注册模式|终端具有4G和5G能力，可以同时接入4G系统和5G系统。
描述 :定义 :4G和5G互操作，指具有4G/5G能力的UE，在4G和5G间移动时（包括重新接入、重选、切换），能保证用户的会话连续性。 
根据MME和AMF间是否有N26接口，4G和5G互操作可分为： 
Ø Interworking with N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换移动性管理状态及会话管理状态。 
Ø Interworking without N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换会话管理状态，但不交换移动性管理状态。 
又根据UE的能力分为： 
单注册模式：终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一，终端仅维护一套4G或5G移动性管理上下文。 
双注册模式：终端具有4G和5G能力，可以同时接入4G系统和5G系统，终端可以同时维护4G和5G移动性上下文。 
背景知识 :在5G网络信号覆盖不全、VoNR业务不支持、网络过载等情况下，都有可能导致4G/5G能力用户在4G和5G网络间移动。移动过程中会话连续性和业务中断时间直接影响用户的业务体验，如语音类业务。 
为了支持4G和5G互操作，3GPP定义了4个4G/5G合一网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U，如[图1]所示。具有4G/5G能力用户，需要选择这四个合一网元。
图1  4G和5G互操作架构图

应用场景 :从应用场景和组网场景看，互操作典型场景包括如下几种： 
场景一： 5G重新接入到4G或4G重新接入到5G（无N26，单注册） 
场景二： 5G重选到4G或4G重选到5G（无N26，单注册） 
场景三： 5G重新接入到4G或4G重新接入到5G（无N26，双注册） 
场景四：5G重选到4G或4G重选到5G（无N26，双注册） 
###### 场景一： 5G重新接入到4G或4G重新接入到5G（无N26，单注册） 
AMF和MME间没有部署N26接口，UE之前在4G接入，单注册，因为各种原因（如登机关机等），UE重新接入到5G。或UE之前在5G接入，再重新接入到4G。 
该方式会话重新接入，AMF和MME间无法通过N26接口交换用户标识等信息。 
###### 场景二： 5G重选到4G或4G重选到5G（无N26，单注册） 
AMF和MME间没有部署N26接口，UE之前在4G接入，单注册，移动到5G无线覆盖区域后，UE重选到5G。 
该互操作方式AMF和MME间无法通过N26接口交换移动性管理上下文，但会话保持不变。 
###### 场景三： 5G重新接入到4G或4G重新接入到5G（无N26，双注册） 
AMF和MME间没有部署N26接口，UE之前在4G和5G同时接入（双注册），因为各种原因（如登机关机等），UE重新接入到5G，或4G，或再同时接入到4G和5G。 
该方式会话重新接入，AMF和MME可能都有用户的移动性管理上下文。 
###### 场景四：5G重选到4G或4G重选到5G（无N26，双注册） 
AMF和MME间没有部署N26接口，UE之前在4G和5G同时接入（双注册），根据4G和5G无线信号覆盖，UE在4G和5G间重选。 
该互操作方式AMF和MME间无法通过N26接口交换移动性管理上下文，但会话保持不变。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户业务体验：在5G信号受限区域，可以在4G下为用户提供服务。热点区域增加5G覆盖，用户业务体验更好。
移动用户|在热点等区域部署了5G，终端用户业务体验更好。
实现原理 :系统架构 :本特性涉及的互操作架构图如[图2]所示。
图2  4G和5G互操作架构图

为了支持互操作，3GPP定义了4个4G/5G合一的网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U。 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
UE|支持4G/5G接入支持有N26接口或/和无N26接口的互操作在4G和5G下移动时可保持用户IP不变
eNodeB|支持通过Handover方式移动到5G下的小区支持通过重接入等方式，使UE移动到5G下的小区
NR|支持通过Handover方式移动到4G下的小区支持通过重接入等方式，使UE移动到4G下的小区
MME|支持给UE下发“支持无N26互操作”指示对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等无N26接口，位置更新时，指示UDM+HSS支持N26接口
AMF|支持给UE下发“支持无N26互操作”指示对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等无N26接口，位置更新时，指示UDM+HSS支持N26接口
PGW-C+SMF|对4G/5G接入能力的终端，可以选择融合NF，如UPF+PGW-U、PCF+PCRF等根据RAT，支持5G PDU Session和4G PDN Connection的互相转换根据RAT，支持5G QoS Flow和4G Bearer的互相转换
PGW-U+UPF|支持用户在4G或5G接入下的用户面数据报文转发支持用户在4G和5G间的切换
PCF+PCRF|可同时下发4G和5G QoS等
UDM+HSS|可同时对用户签约4G和5G2、无N26接口，位置更新时，指示UDM+HSS，UDM+HSS可通知UE同时在MME和AMF上注册
协议栈 :4G和5G互操作时，与MME相关接口涉及： 
与UE间NAS接口。 
与eNodeB间S1-MME接口 
与HSS间S6a接口。 
本NF/网元实现 :MME支持无N26接口的4G和5G互操作，支持UE的单注册，也支持UE的双注册。 
业务流程 :5G到4G的重选（无N26，单注册）
本特性涉及的业务流程图如[图3]所示，流程协议详细描述可参见3GPP 23.502 4.11.2.2 5GS to EPS Mobility。
图3  
5GS to EPS Mobility

流程说明如下： 
0. UE完成向5GS的注册，并建立PDU会话。建立PDU会话过程中，PGW-C+SMF 的S5/S8接口的FQDN会被SMF通知给UDM。 
1. 对于单注册模式UE，如果UE不需会话连续性（即IP连续性），则1-4被执行，否则不执行。UE检测到所有已激活的PDU Session都不需保持会话连续性，则发起RAT改变的TAU流程。 
2. UE发送TAU请求消息给eNB，携带GUTI（mapped from the 5G-GUTI）等信息。 
3. eNB发送TAU请求消息给MME。 
4. MME发现无法获取用户MM上下文等信息，给UE发送TAU Reject消息，携带EMM Cause（#9网络无法获取UE标识）等信息。 
5. UE发起附着过程，发送Attach Request消息，携带IMSI等信息。如果UE想在附着过程中建立PDN连接，则Attach Request消息中也包含PDN CONNECTIVITY Request消息。 PDN CONNECTIVITY Request中携带Request type ("Handover")、DNN/APN、PDU Session ID in PCO等信息。如果UE支持5GC NAS，则UE会在NAS indicator中指示。  
6. eNB发送Attach Request消息给MME。 
7. MME完成对UE的安全过程。 
8. 如果需进行Equipment ID检查，则MME完成对UE的Equipment ID检查过程。 
9. MME向HSS+UDM发送Location Update Request消息。MME不携带initial attach指示位，HSS+UDM不向old AMF发起取消登记流程； 
10. HSS+UDM向MME返回Location Update Ack消息，携带用户签约等信息。HSS+UDM如果保存了PGW-C+SMF FQDN，则会返回给MME。  
11. MME根据PGW-C+SMF FQDN确定PGW，并选择合适的SGW。 
12. MME完成向SGW/PGW创建会话过程。PGW-C+SMF根据PDU Session ID in PCO关联5G PDU Session。 
13. MME向eNB发送Initial Context Setup Request（Attach Accept）消息。如果UE指示支持5GC NAS，则MME在Attach Accept消息中携带interworking without N26指示给UE。 
14. eNB向UE发起RRC Connection Reconfiguration过程。 
15. eNB向MME返回Initial Context Setup Response消息。 
16. UE向MME返回Attach Complete消息。 
17. 如果附着过程中建立的PDN连接Request type 不是"Handover"，MME支持interworking without N26，则MME向HSS+UDM发送Notify Request消息，携带APN/DNN和PGW-C+SMF FQDN等信息。 
18. HSS+UDM向MME返回Notify Response消息。 
19. 如果UE还有其它PDU Session需切换到EPS，则UE发起UE requested PDN Connectivity 流程，Request Type设置为"handover" 。单注册模式UE在附着完成后立刻完成该流程，双注册模式UE可以在附着完成后任意时刻完成该流程。  
20. 针对已经切换完成的PDU会话，SMF+PGW-C触发5GC侧PDU会话释放，不通知UE。 
4G到5G的重选（无N26，单注册）
本特性涉及的业务流程图如[图4]所示，流程协议详细描述可参见3GPP 23.502 4.11.2.3 EPS to 5GS Mobility。
图4  EPS to 5GS Mobility

流程说明如下： 
0. UE在EPC附着。 
1. UE检测到需从4G移动到5G，发起注册流程，发送Registration  Request消息，携带Registration type( set to "mobility registration update")、5G-GUTI(mapped from the 4G-GUTI)、native 5G-GUTI (if available) as an Additional GUTI等信息。UE指示从EPC移动到5GC。 
2. NR选择一个合适的AMF。 
3. NR发送Registration  Request消息给AMF。如果Registration type为"mobility registration update"，UE指示从EPC移动到5GC，AMF支持5GS-EPS interworking procedure without N26 interface，则AMF把看看做 "initial Registration"，不做PDU Session状态同步。 
4. AMF根据5G-GUTI 查找不到UE的MM上下文等信息，发起向UE获取SUCI过程。 
5. AMF完成对UE的安全过程。 
6. AMF完成对UE的Equipment ID检查过程。 
7. AMF完成向UDM+HSS的注册过程。若UE从EPC移入且AMF支持无N26互操作，则携带UE已注册MME指示；若HSS+UDM支持同时在AMF和MME注册，则不会发送注销通知给MME，且在注册响应中携带支持UE在AMF和MME同时注册指示。HSS+UDM如果保存了PGW-C+SMF FQDN，则会返回给AMF。  
8. 如果需向PCF建立AM Policy Association，则AMF向PCF发起AM Policy Association建立过程。 
9. AMF通知SMF更新信息。 
10. AMF向UE发送Registration Accept消息，携带5G-GUTI、TA List等信息。如果HSS+UDM指示支持UE在AMF和MME同时注册，则AMF在Registration Accept消息中携带interworking without N26指示给UE。 
11. UE向AMF返回Registration  Complete消息。 
12. 如果UE想把4G中的PDN连接切换到5GS中，则发起UE requested PDU Session Establishment (Request Type to "Existing PDU Session" or "Existing Emergency PDU Session")流程。单注册模式UE在注册完成后立刻完成该流程，双注册模式UE可以在注册完成后任意时刻完成该流程。 
13. PGW-C+SMF完成EPC中PDN连接资源的释放。 
5G到4G的重选（无N26，双注册）
双注册模式下无N26接口的互操作和单注册无N26接口互操作类似，主要差异点： 
1、双注册模式下的终端，可以提前在另一个RAT下注册，缩短重选接入时延，在另一个RAT下注册成功后不用立即发起会话创建流程；单注册模式下的终端，在跨RAT移动时才会发起注册流程，并在注册后或注册中（有PDN附着）立即创建目标RAT下的PDN/PDU会话。 
2、双注册模式下，终端分别维护4G移动性管理和5G移动性管理，跨RAT移动不需要进行4/5G GUTI映射接入，直接使用各自Native GUTI接入；单注册模式下终端只维护一套移动性管理状态，跨RAT移动需要进行4/5G GUTI映射。 
4G到5G的重选（无N26，双注册）
双注册模式下无N26接口的互操作和单注册无N26接口互操作类似，主要差异点： 
1、双注册模式下的终端，可以提前在另一个RAT下注册，缩短重选接入时延，在另一个RAT下注册成功后不用立即发起会话创建流程；单注册模式下的终端，在跨RAT移动时才会发起注册流程，并在注册后或注册中（有PDN附着）立即创建目标RAT下的PDN/PDU会话。 
2、双注册模式下，终端分别维护4G移动性管理和5G移动性管理，跨RAT移动不需要进行4/5G GUTI映射接入，直接使用各自Native GUTI接入；单注册模式下终端只维护一套移动性管理状态，跨RAT移动需要进行4/5G GUTI映射。 
系统影响 :4G与5G互操作，会增加垮RAT的流程，影响系统的话务模型。 
部署了N26接口时，从5G到4G的Handover流程和TAU流程。 

部署了N26接口时，从4G到5G的Handover流程和Registration Update流程。 
没有部署N26接口时，从5G到4G的TAU流程，附着流程，PDN连接建立流程，专有承载建立流程。 
没有部署N26接口时，从4G到5G的Registration流程，PDU Session建立流程，专有QoS flow建立流程。 
为了减少对系统的影响，需尽可能减少垮RAT互操作次数，重叠区要合理规划，避免频繁的跨RAT互操作。 
应用限制 :协议版本：2019年9月份。 
4G MME的GUMMEI和5G AMF的GUAMI规划时尽量不重叠。如果重叠了，一方面RAN选择MME时，真实的GUMMEI和映射的GUMMEI都匹配，导致选择合一的CN节点可能失败，也会导致各个CN节点的负荷可能不均；另一方面，如果MME使用MME-FQDN选择AMF时，会导致可能选择错误的AMF，必须要求MME使用AMF-FQDN选择AMF才可以避免。 
特性交互 :无。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501-f60 System Architecture for the 5G System|全文
3GPP TS 23.502-f60 Procedures for the 5G System|全文
3GPP TS 23.503-f60 Policy and Charging Control Framework for the 5G System|全文
3GPP TS 29.274-f90 Tunnelling Protocol for Control plane (GTPv2-C); Stage 3|全文
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为下表所示，只有在License项目显示为“支持”时，MME才支持与5GS的互操作功能： 
LICENSE项|归属NF|备注
---|---|---
MME支持N26互操作|SGSN&MME|MME部署了N26接口，支持4G和5G间有N26接口互操作
MME支持无N26互操作|SGSN&MME|MME没有部署N26接口，支持4G和5G间无N26接口互操作
对其他网元的要求 :要求参与互操作的各网元功能，均依据3GPP协议规定。 
UE|eNodeB/gNodeB|SGW|PGW+SMF|HSS+UDM
---|---|---|---|---
-|√|√|√|√
工程规划要求 :规划基于N26接口互操作还是无N26接口互操作。如果基于N26接口互操作，需分别规划AMF和MME的N26接口的GTPC地址和VRF。如果基于N26接口互操作，DNS Server中需增加AMF的解析数据。需要确认解析AMF的方式，如果为根据MME-FQDN解析，则4G GUMMEI和5G GUAMI不能重叠。如果需要RAN选择合一的AMF+MME节点，则4G GUMMEI和5G GUAMI不能重叠。NR需配置4G邻接小区信息等，eNB需配置5G邻接小区信息等。 
O&M相关 :命令 :配置项表2  新增配置项配置项命令45G互操作配置SHOW 5GC INTERWORKINGSET 5GC INTERWORKING表3  修改配置项配置项命令新增参数MME本地解析APNADD EPC APNPROTOCOL类型增加根据PGW NAME解析PGWADD EPC PGWPROTOCOL类型增加 
性能统计 :性能计数器名称
---
C430010222 无N26接口跟踪区更新请求次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该配置过程实现支持无N26接口互操作功能。 
配置前提 :已同时部署5GC和EPC系统。 
配置过程 :开启License中的“MME支持无N26互操作”。 
在EM客户端配置页面的左侧命令树中，展开MME节点，选择 NFS_MMESGSN_0 节点。
执行[SET 5GC INTERWORKING]命令，配置MME的互操作开关为支持WITHOUTN26,且互操作模式为WITHOUTN26。
执行[ADD EPC APN]命令，增加协议类型为“x-s5-gtp+nc-smf”和“x-s8-gtp+nc-smf”的解析配置。配置MME本地解析APN，选择合一的PGW+SMF的地址。
执行[ADD EPC PGW]命令，增加协议类型为“x-s5-gtp+nc-smf”和“x-s8-gtp+nc-smf”的解析配置。配置MME根据PGW NAME解析PGW的地址。
配置实例 :场景说明 :无N26场景，5G用户重新接入到4G。或4G用户重新接入到5G。 
数据规划 :参数|取值
---|---
5GC互操作基本配置|互操作模式|有N26（WITHN26）
支持N26互操作|5GC互操作基本配置|支持
支持无N26互操作|5GC互操作基本配置|支持
APN解析|APN|cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org
合一的PGW+SMF地址|APN解析|192.20.53.100
PGW解析|PGWNAME|pgw.n26.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
PGW地址|PGW解析|192.20.51.36
配置步骤 :步骤|说明|操作
---|---|---
1|配置MME的互操作开关为支持WITHOUTN26，互操作模式为WITHOUTN26|SET 5GINTERWORKCFG:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="SPRT",INTERWORKMODE="WITHOUTN26"
2|配置MME本地解析APN，选择合一的PGW+SMF的地址|ADD EPC APN:APN="cmnet.apn.epc.mnc011.mcc460.3gppnetwork.org",HOST="pgw.n26.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="192.20.53.100",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp+nc-smf&x-s8-gtp+nc-smf",NAPTRORDER=0,NAPTRWEIGHT=200,UEUSAGETYPE="NORMAL"
3|配置MME根据PGW NAME解析PGW的地址|ADD EPC PGW:PGWNAME="pgw.n26.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org",IPADDR="192.20.51.36",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp+nc-smf&x-s8-gtp+nc-smf",UEUSAGETYPE="NORMAL"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|从5GC到EPC的移动性管理
---|---
测试目的|验证终端在空闲态位置更新，所有PDN连接迁移成功
预置条件|网络中各网元系统及操作维护台运行正常网络侧不支持N26接口，AMF和MME配置工作在无N26互操作模式UE已经激活1个PDU会话UE处于空闲态
测试过程|调节无线信号，触发终端在EPC网络发起TAU流程
通过准则|UE向MME发起TAU Request流程，GUTI映射成功，携带的old Native GUTI由5G-GUTI映射而来。并且UE携带N1 MODE。MME发送TAU reject给UE，因为不支持N26接口而拒绝用户接入。
测试结果|–
测试项目|从EPC到5GC的移动性管理
---|---
测试目的|验证终端在空闲态位置更新，所有PDN连接迁移成功
预制条件|网络中各网元系统及操作维护台运行正常UE处于单注册模式下，网络工作在无N26互操作模式，UE已收到IWK without N26指示AMF和MME均不支持N26接口，SMF+PGW-C融合，UPF+PGW-U融合，PCF+PCRF融合，HSS+UDM融合UE已经激活1个PDU会话UE处于空闲态
测试过程|调节无线信号，触发终端在5GC网络发起registration流程
通过准则|UE向AMF发起registration流程， registration type 携带为 "Mobility Registration Update，并且将EPC GUTI映射为5G GUTI，映射成功。AMF发送Identify Request给UE，请求用户SUCI。UE回复Identify Response，携带用户SUCI。执行鉴权、SMC、IMEI Check等过程。AMF 下发Registration accept给UE，携带分配的5G-GUTI。UE回复Registration Complete给AMF。UE发起PDU建立流程，type为 “Existing PDU Sesssion”。AMF进行SMF选择时，直接取该PDU会话对应DNN在UDM中登记的PGW-C+SMF ID，根据该ID向NRF查询SMF服务化地址；若该PDU会话未向UDM注册，则SMF+PGW-C发送Nudm_SDM_Registration给UDM，携带PDU会话ID、DNN以及PGW-C+SMF ID。5G中会话建立成功。
测试结果|–
常见问题处理 :无。 
# ZUF-78-20 拥塞及过负荷控制 
概述 :功能描述 :EPC网络在实际运行中，由于批量用户集中涌入、频繁的跨RAT切换、无线或核心网网元重启、节假日集中爆发业务等导致大量用户集中注册到网络，使网络负荷迅速增高。由于网络中不同类型网元的处理能力和资源不同，往往会出现由某个网元故障或宕机导致全网瘫痪。为了保证整个EPC网络的正常运行，需要各网元配合，从源头上对业务和用户实施控制，保障整个网络正常运行。
过负荷控制功能通过限制本网元接入的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致本网元或者邻接网元设备异常或崩溃。 
功能特性简介 :针对MME入向负荷控制和出向负荷控制的应用特点、接入方式和应用场景，核心网提供了可靠、有效的解决方案。详细的解决方案特性如下表：
方案特性|实现简述|特导链接
---|---|---
S1接口过载控制|当MME处于过负荷情况时，发送overload start消息通知eNodeB，eNodeB抑制UE发起的业务。在MME退出过负荷状态时，会发送overload stop消息给eNodeB，eNodeB正常接入业务。|ZUF-78-20-001 S1接口过载控制
NAS拥塞控制|当某一类业务过负荷但系统并没有整体过负荷时，通过控制UE发起业务，避免某类终端业务信令突发时对EPC网络的冲击。包括：基于APN识别出某类终端发起业务过多或过快，通知此类终端在一段时间内不再发起业务。基于Group ID识别出某类终端发起业务过多或过快，通知此类终端在一段时间内不再发起业务。基于APN+Group ID识别出某类终端发起业务过多或过快，通知此类终端在一段时间内不再发起业务。MME网元自身过负荷时，通知后续接入此MME的用户一段时间内不再发起业务。基于RAT的NAS拥塞控制，MME按照接入类型进行NAS拥塞控制，接入类型区分NB接入和WB接入，支持如下拥塞控制条件：承载建立数、承载建立速率、接收NAS MM信令速率、接收NAS SM信令速率。在设置CPU拥塞门限时，WB用户的门限可以高于NB用户的门限。当发生NAS拥塞控制时，MME向UE发送Attach Reject或TAU Reject消息， 携带T3448（“Control Plane data back-off timer”）参数，UE收到消息后，设定定时器， 时长为T3448参数指定时长，超时后重新发起业务接入网络。、|ZUF-78-20-002 NAS拥塞控制
S6a接口拥塞控制|MME可以根据周边网元能力进行负荷控制，HSS相关的过负荷功能如下：MME支持HSS过负荷功能，发生过负荷的HSS，通过扩展的OC-OLR AVP，将包含有控制比例和有效时间等详细过负荷信息的“过负荷报告”传递给MME。MME根据过负荷报告，按比例降低到该HSS的业务负荷，完成网元间的过负荷控制。避免对过负荷HSS的冲击。MME支持ALC（auto load control）功能，在业务过负荷期间，MME根据到HSS的业务成功率，自动控制使用到HSS的业务（附着，局间TAU等），成功率高就允许更多的业务通过。反之则降低通过的业务数量。|ZUF-78-20-003 S6a接口拥塞控制
GTP-C接口拥塞控制|MME可以根据周边网元能力进行负荷控制，GW网元相关的过负荷功能如下：SGW网元过负荷：MME收到SGW的过载信息OCI后，有业务请求时（PDN创建、承载创建、其他业务上报等），MME根据OCI要求的比例来减少选择拥塞SGW的次数，减少发送给SGW的请求消息数。PGW网元级过负荷：MME收到PGW的过载信息OCI后，附着或PDN建立，MME根据OCI要求的比例来减少选择拥塞PGW的次数，减少发送给PGW的请求消息数。PGW网元APN级过负荷，有两种方式：方式一：MME收到PGW的APN过载信息OCI后，过负荷信息完成过负荷控制；在信息有效时长内，按减少百分比，根据业务的优先级，减少到该PGW上该APN的业务负荷。方式二：MME收到PGW响应消息，原因值为APN拥塞，在Back-off Timer时间内不选择该PGW。|ZUF-78-20-004 GTP-C接口拥塞控制
终端异常信令管控|终端异常信令管控是指当终端在不停的尝试业务，但是却一直异常时，MME会采取一定的措施，减少终端触发的信令，避免引起网络拥塞。MME信令风暴抑制是用户级操作，且针对三种终端信令，包括附着请求信令、业务请求信令和PDN连接请求信令。当用户单位时间内的信令数超过门限值，用户将被加入信令黑名单，MME对其信令请求进行抑制。|ZUF-78-20-005 终端异常信令管控
## ZUF-78-20-001 S1接口过载控制 
特性描述 :特性描述 :术语 :术语|含义
---|---
过载控制|又称过负荷控制，限制接入的业务量，来降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。
描述 :定义 :S1接口过载控制是MME在自身负荷较高时，通知部分eNodeB减少发给本MME的业务量，避免因本网元负荷过高导致设备异常或崩溃。 
背景知识 :过载控制是保障网元安全运行的重要措施，在实际应用中，经常会出现因为某些特定的原因，导致用户短时间内暴发超过正常话务模型的业务。这些原因包括：网元重启、传输网故障、用户大量移动、节假日以及特殊事件等。此时如果不进行过载控制，网元的处理能力、资源以及接口带宽都可能达到极限，最终导致网元崩溃，并形成雪崩效应使得整个网络瘫痪。 
根据过载发生的范围和控制的层次，过载控制分为以下几种： 
面向终端和应用的端到端过载控制。 
面向EPC网络的网元间动态过载控制。 
针对单一网元的网元自身过载控制。 
终端和应用的端到端过载控制
随着物联网终端的广泛应用，大量的物联网终端接入EPS网络后，更容易因为物联网服务器故障、终端的特殊应用以及突发事件等原因导致短时间内业务量急剧增加，因此对过载控制的要求更高。尤其是当人和物接入同一个EPS网络后，需要能够区分人与物以及不同的业务和应用，分别实施控制，保证不会因某类用户或某项应用占用大量的网络资源，而对其他用户的正常使用产生影响。 
网元间的动态过载控制
EPC核心网在实际运行中，有多种造成EPC网络信令负荷增高的原因，例如：特定区域大批用户涌入引发的注册信令、频繁的跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等。一旦出现过载，由于网络中不同类型的网元处理能力和资源各不相同，往往会出现由某个网元故障或宕机导致的全网瘫痪。因此为了保证整个EPC网络的正常运行，就需要各网元配合，从源头上对业务和用户实施控制，来完成整个网络的过载控制。
网元自身的过载控制
MME是EPC网络中的移动性管理网元，也是终端的控制面接入点，一旦遇到业务量突然增加的情况，MME将更加直接地受到冲击，自身资源（包括处理能力、内部资源、外部接口带宽等）将迅速耗尽。如果MME网元宕机，将会对整个EPC网络造成巨大的影响。因此，MME网元需要保障自身正常运行的机制，实现自身的过载控制。 
应用场景 :当本MME负荷较高时，通过S1接口过载控制，限制部分eNodeB发给本MME的业务，使本MME的负荷稳定在一个正常的范围。负荷“削峰”，可以保证业务成功率，从而平滑地接入用户业务。 
S1接口过载控制可以用于以下场景： 
遭遇突发业务场景ZXUN uMAC网元突然接入超过估算话务模型的业务量，CPU占用量陡增。例如，举办大型赛事，大量外地用户涌入。 
ZXUN uMAC设备升级场景在设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会快速重新附着，导致单位时间内的用户附着数过高。 
客户收益 :受益方|受益描述
---|---
运营商|防止网元设备被突发大量业务冲击，在突发大话务的情况下，不会异常或者崩溃，提高网络的稳定性。
移动用户|网元设备被大量业务冲击造成网络瘫痪，移动用户无法接入网络， 通过S1接口过载控制，限制部分eNodeB的用户业务，逐步放行，保证用户能平滑地接入网络。
实现原理 :系统架构 :S1接口过载控制网络结构如[图1]所示。
图1  S1接口过载控制网络结构

涉及的网元 :网元名称|网元作用
---|---
MME|当MME过载时，向部分eNodeB发送Overload Start消息；当MME负荷恢复时，向eNodeB发送Overload Stop消息。
eNodeB|收到Overload Start消息后，限制发给MME的业务量；收到Overload Stop消息后，恢复发给MME的业务量。
协议栈 :S1接口协议栈如[图2]所示。
图2  S1接口协议栈

本网元实现 :MME定时检测本网元的负荷。 
当负荷过高时，选择部分eNodeB发送Overload Start消息，支持eNodeB个数可配置。 
当负荷恢复时，向已经发送Overload Start消息的eNodeB发送Overload Stop消息。 
业务流程 :业务流程如[图3]所示。
图3  业务流程

MME检测到本网元负荷过高时，选择部分eNodeB发送Overload Start消息。 
MME检测到本网元负荷恢复时，向已经发送Overload Start消息的eNodeB发送Overload Stop消息。 
系统影响 :收到MME发送Overload Start消息的eNodeB，会限制发给该MME的业务，其限制行为可配置。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 36.413 S1 Application Protocol (S1AP)|8.7.6 Overload Start8.7.7 Overload Stop
特性能力 :名称|指标
---|---
通过Overload Start消息通知的eNodeB最大个数|65535（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.30|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME过负荷参数配置SET MME OVERLOAD PARASHOW MME OVERLOAD PARAMME接口消息控制配置SET INTERFACE MSG OVERLOADSHOW INTERFACE MSG OVERLOAD 
安全变量不涉及 
软件参数不涉及 
动态管理表2  新增动态管理配置项命令通知单个eNodeB过负荷NOTIFY SINGLE ENB OVERLOAD通知所有eNodeB过负荷NOTIFY ALL ENB OVERLOAD停止单个eNodeB过负荷STOP SINGLE ENB OVERLOAD停止所有eNodeB过负荷STOP ALL ENB OVERLOAD 
性能统计 :测量类型|描述
---|---
S1口负荷控制测量（43300）|编号为C43300开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本配置用于实现S1接口过载控制。MME负荷较高时，通过S1接口过载控制，限制部分eNodeB发给本MME的业务量，使本MME的负荷稳定在一个正常的范围内。 
配置前提 :MME S1接口消息负荷过高，需要开启过载控制功能。 
配置过程 :执行[SET MME OVERLOAD PARA]命令，配置MME过负荷参数。
配置实例 :场景说明 :MME负荷较高时，开启S1接口过载控制，限制部分eNodeB发给本MME的业务量，使MME的负荷稳定在一个正常的范围内。 
数据规划 :配置项|参数名称|取值
---|---|---
MME过负荷参数配置|S1接口发送Overload Start的策略|根据CPU负荷发送
发送Overload Start的CPU低门限（%）|MME过负荷参数配置|60
低门限Overload Start消息中的Overload Action信元设置|MME过负荷参数配置|拒绝非紧急情况终端发起数据传输的所有RRC连接建立
低门限Traffic Load Reduction Indication信元设置|MME过负荷参数配置|1
配置步骤 :步骤|说明|命令
---|---|---
1|配置S1接口发送Overload Start的策略为“根据CPU负荷发送”，并根据MME网元实际负荷能力，配置发送Overload Start消息的CPU低门限，低门限Overload Start消息中的Overload Action信元和低门限Traffic Load Reduction Indication信元。|SET MME OVERLOAD PARA:S1OLCTRL="BYCPU",CPULOWTHD=60,LOWTHDACT="REJECTNOEMERG",LOWTHDTLRI=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|MME S1接口过载控制
---|---
测试目的|测试MME S1接口过载控制功能。
预置条件|MME S1接口消息负荷过高，开启过载控制功能。
测试过程|配置MME过负荷开关，设置S1接口发送Overload Start的策略为“根据CPU负荷发送”。根据MME网元的实际负荷能力，配置发送Overload Start的CPU低门限、低门限Overload Start消息中的Overload Action信元设置，低门限Traffic Load Reduction Indication信元设置等参数。
通过准则|当MME CPU占用率超过配置的“发送Overload Start的CPU低门限”值时，MME向eNodeB发送Overload Start消息，消息中携带的参数与配置保持一致。
测试结果|–
常见问题处理 :无。 
## ZUF-78-20-002 NAS拥塞控制 
特性描述 :特性描述 :描述 :定义 :基于RAT的NAS拥塞控制是指根据用户的接入类型采取不同的拥塞控制策略，当NB-IoT网络出现拥塞时，可以进行拥塞控制。
背景知识 :MME支持基于RAT类型进行NAS拥塞门限配置、拥塞判断和拥塞控制。如可控制NB-IoT RAT类型用户的附着请求消息和CPSR消息，当NB-IoT用户的拥塞门限低于大网用户的拥塞门限时，NB-IoT用户优先被控制。
应用场景 :###### 场景一：基于接入类型进行NAS拥塞控制 
NB-IoT用户有更低的拥塞控制门限，优先于大网用户被控制。MME区分WB用户和NB-IoT用户，对其分别进行NAS拥塞控制。 
###### 场景二：基于APN进行拥塞控制时区分WB和NB-IoT分别控制 
NB-IoT用户有更低的拥塞控制门限，优先于大网用户被控制。MME区分WB用户和NB-IoT用户，对其分别进行APN拥塞控制判定，可以对WB用户和NB-IoT用户下发不同的Back off Timer。 
###### 场景三：基于MTC进行拥塞控制时区分WB和NB-IoT分别控制 
NB-IoT用户有更低的拥塞控制门限，优先于大网用户被控制。MME区分WB用户和NB-IoT用户，对其分别进行MTC拥塞控制判定，可以对WB用户和NB-IoT用户下发不同的Back off Timer。 
###### 场景四：基于APN和MTC的组合进行拥塞控制时分NB-IoT和WB分别控制。 
NB-IoT用户有更低的拥塞控制门限，优先于大网用户被控制。MME区分WB用户和NB-IoT用户，对其分别进行APN和MTC组合拥塞控制判定，可以对WB用户和NB-IoT用户下发不同的Back off Timer。 
客户收益 :受益方|受益描述
---|---
运营商|能够在对用户进行拥塞控制时区分WB用户和NB-IoT用户，并且能够达到先对NB-IoT用户进行拥塞控制的目的，提高WB用户的服务体验。
终端用户|享受到更好的服务体验。
实现原理 :###### 按接入类型进行NAS拥塞控制 
按接入类型进行NAS拥塞控制，区分NB-IoT接入和WB接入。现网应用中，可以设置WB的拥塞门限高于NB-IoT的拥塞门限。 
按接入类型进行NAS拥塞控制，拥塞控制条件有如下5个： 
最大建立承载数 
最大建立承载速率 
最大接收NAS SM信令速率 
最大接收NAS MM信令速率 
CPU占用率 
拥塞控制[条件1]和[条件2]，适用于以下业务流程。如果MME检测到NB-Iot或WB接入类型下建立承载数或承载速率超过配置门限，则拒绝该接入类型下的以下业务流程。
附着 
PDN连接请求 
承载资源申请 
承载资源修改 
拥塞控制[条件3]，适用于以下业务流程。如果MME检测到NB-Iot或WB接入类型下接收用户NAS SM信令速率超过配置门限，则拒绝该接入类型下的以下业务流程。
PDN连接请求 
承载资源申请 
承载资源修改 
拥塞控制[条件4]，适用于以下业务流程。如果MME检测到NB-Iot或WB接入类型下接收用户NAS MM信令速率超过配置门限，则拒绝该接入类型下的以下业务流程。
附着 
TAU 
业务请求 
拥塞控制[条件5]，适用于以下业务流程。如果MME检测到CPU占用率超过NB-IoT或WB接入类型下的配置门限，则拒绝该接入类型下的以下业务流程。
附着 
业务请求 
PDN连接建立 
专有承载建立 
承载修改 
寻呼 
TAU 
切换 
###### 基于APN进行拥塞控制时区分WB和NB-IoT分别控制 
基于APN进行拥塞控制，MME可配置NB-IoT接入用户的拥塞控制，包括： 
可保障建立承载数 
可保障建立承载速率 
可保障接收NAS MM信令速率拥塞控制策略同按接入类型进行NAS拥塞控制。如果需要携带Back-off Timer，则在如下两个值之间取一个随机值。低优先级拒绝时携带的Back-off Timer最小取值（秒）低优先级拒绝时携带的Back-off Timer最大取值（秒） 
###### 基于MTC进行拥塞控制时区分WB和NB-IoT分别控制 
基于MTC进行拥塞控制，MME可配置NB-IoT接入用户的拥塞控制，包括： 
可保障接收NAS MM信令速率 
可保障接收NAS SM信令速率拥塞控制策略同按接入类型进行NAS拥塞控制。如果需要携带Back-off Timer，则在如下两个值之间取一个随机值。低优先级拒绝时携带的Back-off Timer最小取值（秒）低优先级拒绝时携带的Back-off Timer最大取值（秒） 
###### 基于MTC+APN的组合进行拥塞控制时区分WB和NB-IoT分别控制 
基于MTC+APN的组合进行拥塞控制，MME可配置NB-IoT接入用户的拥塞控制，包括： 
可保障建立承载数 
可保障接收NAS MM信令速率 
可保障接收NAS SM信令速率拥塞控制策略同按接入类型进行NAS拥塞控制。如果需要携带Back-off Timer，则在如下两个值之间取一个随机值。低优先级拒绝时携带的Back-off Timer最小取值（秒）低优先级拒绝时携带的Back-off Timer最大取值（秒） 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: “General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”|4.3.7.4 MME control of overload
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性为uMAC产品的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
-|-|√|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无。 
O&M相关 :命令 :配置项新增配置项参见表4。表4  新增配置项配置项命令RAT拥塞控制开关SET RAT CONGESTION SWITCHSHOW RAT CONGESTION SWITCHRAT拥塞控制策略配置ADD RAT CONGESTION POLICYSET RAT CONGESTION POLICYDEL RAT CONGESTION POLICYSHOW RAT CONGESTION POLICY基于APN拥塞控制开关SET APN CONGESTION SWITCHSHOW APN CONGESTION SWITCHAPN拥塞控制策略配置ADD APN CONGESTION POLICYSET APN CONGESTION POLICYDEL APN CONGESTION POLICYSHOW APN CONGESTION POLICY基于MTC用户的MME网元拥塞控制开关SET MTCMME CONGESTION SWITCHSHOW MTCMME CONGESTION SWITCHMTC用户的MME网元拥塞控制策略配置ADD MTCMME CONGESTION POLICYSET MTCMME CONGESTION POLICYDEL MTCMME CONGESTION POLICYSHOW MTCMME CONGESTION POLICY基于MTC用户的APN拥塞控制开关SET MTCAPN CONGESTION SWITCHSHOW MTCAPN CONGESTION SWITCHMTC用户的APN拥塞控制策略配置ADD MTCAPN CONGESTION POLICYSET MTCAPN CONGESTION POLICYDEL MTCAPN CONGESTION POLICYSHOW MTCAPN CONGESTION POLICY 
安全变量无新增安全变量。 
软件参数无新增软件参数 
动态管理无新增动态管理。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :告警和通知
---
2114584631 业务拥塞告警
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :按接入类型进行NAS拥塞控制功能默认关闭，可根据实际情况决定是否开启该功能。 
基于APN进行拥塞控制时区分NB-IoT独立控制功能默认关闭，可根据情况决定是否开启该功能，该功能生效需要基于APN的拥塞控制功能生效。 
基于MTC进行拥塞控制时区分NB-IoT独立控制功能默认关闭，可根据情况决定是否开启该功能，该功能生效需要基于MTC的拥塞控制功能生效。 
基于MTC+APN进行拥塞控制时区分NB-IoT独立控制功能默认关闭，可根据情况决定是否开启该功能，该功能生效需要基于MTC+APN的拥塞控制功能生效。 
配置前提 :开启基于APN拥塞控制时区分NB独立控制功能时，需要基于APN的拥塞控制功能生效。 
开启基于MTC拥塞控制时区分NB独立控制功能时，需要基于MTC的拥塞控制功能生效。 
开启基于MTC+APN拥塞控制时区分NB独立控制功能时，需要基于MTC+APN的拥塞控制功能生效。 
配置过程 :按接入类型进行NAS拥塞控制。 
执行以下命令，开启基于RAT的NAS拥塞控制功能。
[SET RAT CONGESTION SWITCH]
执行以下命令，增加基于RAT的NAS拥塞控制策略。 
[ADD RAT CONGESTION POLICY]
基于APN进行拥塞控制时区分NB独立控制。 
执行以下命令，开启基于APN的NAS拥塞控制功能，并设置NB-IoT接入使用低接入优先级控制。 
[SET APN CONGESTION SWITCH]
执行以下命令，增加基于APN的NAS拥塞控制策略。 
[ADD APN CONGESTION POLICY]
基于MTC进行拥塞控制时区分NB独立控制。 
执行以下命令，开启基于MTC的NAS拥塞控制功能，并设置NB-IoT接入使用低接入优先级控制。 
[SET MTCMME CONGESTION SWITCH]
执行以下命令，增加基于MTC的NAS拥塞控制策略。 
[ADD MTCMME CONGESTION POLICY]
基于MTC+APN进行拥塞控制时区分NB独立控制。 
执行以下命令，开启基于MTC+APN的NAS拥塞控制功能，并设置NB-IoT接入使用第优先级控制。 
[SET MTCAPN CONGESTION SWITCH]
执行以下命令增加基于MTC+APN的NAS拥塞控制策略。 
[ADD MTCAPN CONGESTION POLICY]
#### 配置实例 
###### 基于接入类型进行NAS拥塞控制 
场景说明
基于接入类型进行NAS拥塞控制。 
配置步骤
配置|说明
---|---
SET RAT CONGESTION SWITCH:SUPNBRATCON="YES"|打开基于RAT进行NAS拥塞控制的开关。
ADD RAT CONGESTION POLICY:ACCESSTYPE="NB-IOT",CTLTYPE="RATE_BEARER_ACTIVATIONS",MAXRATE=100,REJECTRATE=100,BACKOFFTIMESTART=300,BACKOFFTIMEEND=600|设置针对NB-IoT接入的用户进行拥塞控制，拥塞控制类型为承载建立速率，拥塞控制的域值为承载建立速率100个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为300秒到600秒之间的随机值。
###### 基于APN进行拥塞控制时区分WB和NB-IoT分别控制 
场景说明
基于APN进行拥塞控制时区分WB和NB-IoT分别控制。
配置步骤
配置|说明
---|---
SET APN CONGESTION SWITCH:NBUSELPACAPN="USE"|打开基于APN拥塞控制开关，对于用户NB-IoT RAT接入时，使用低接入优先级拥塞控制参数进行拥塞控制。
ADD APN CONGESTION POLICY:APN="zte.com.nmnc001.mcc460.gprs",TYPE="BEARERRATE",PERIOD="SECOND",MAXRATE=100,MINDELAY=300,MAXDELAY=600,REJECTRATE=100,DEACTBEAR="NO",LOWMIN=600,LOWMAX=1800|设置对于APN为zte.com.nmnc001.mcc460.gprs建立的承载进行拥塞控制，拥塞控制类型为承载建立速率，拥塞控制的域值为承载建立速率100个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间普通用户为300秒到600秒之间的随机值，低优先级用户为600秒到1800秒之间的随机值。
###### 基于MTC进行拥塞控制时区分WB和NB-IoT分别控制 
场景说明
基于MTC进行拥塞控制时区分WB和NB-IoT分别控制。
配置步骤
配置|说明
---|---
SET MTCMME CONGESTION SWITCH:NBUSELPACMTC="USE"|打开基于MTC用户的MME网元拥塞控制开关，对于用户NB-IoT RAT接入时，使用低接入优先级拥塞控制参数进行拥塞控制。
ADD MTCMME CONGESTION POLICY:MTCGRPID="460"-"01"-"1",TYPE="NASMMRATE",MAXNASMM=100,MINDELAY=300,MAXDELAY=600,REJECTRATE=100,DEACTBEAR="NO",LOWMIN=600,LOWMAX=1800|设置对于签约MTC GroupID为460-01-1的用户进行拥塞控制，拥塞控制类型为接收NAS MM信令速率，拥塞控制的域值为最大接收NAS MM信令速率为100个每秒，超过此阈值后用户NAS MM信令拒绝比例为100%，下发的拒绝消息中携带的backoff time时间普通用户为300秒到600秒之间的随机值，低优先级用户为600秒到1800秒之间的随机值。
###### 基于MTC+APN的组合进行拥塞控制时分NB-IoT和WB分别控制 
场景说明
基于APN和MTC的组合进行拥塞控制时分NB-IoT和WB分别控制。
配置步骤
配置|说明
---|---
SET MTCAPN CONGESTION SWITCH:NBUSELPACMTCAPN="USE"|打开基于MTC用户的APN拥塞控制开关，对于用户NB-IoT RAT接入时，使用低接入优先级拥塞控制参数进行拥塞控制。
ADD MTCAPN CONGESTION POLICY:MTCGRPID="460"-"01"-"1",APN="zte.com",TYPE="NASMMRATE",MAXNASMM=100,MINDELAY=300,MAXDELAY=600,DEACTBEAR="NO",LOWMIN=600,LOWMAX=1800|设置对于签约MTC GroupID为460-01-1以及签约了zte.com的用户进行拥塞控制，拥塞控制类型为接收NAS MM信令速率，拥塞控制的域值为最大接收NAS MM信令速率为100个每秒，超过此阈值后用户NAS MM信令拒绝比例为100%，下发的拒绝消息中携带的backoff time时间普通用户为300秒到600秒之间的随机值，低优先级用户为600秒到1800秒之间的随机值。
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|基于RAT的承载建立速率控制
---|---
测试目的|验证MME能根据RAT进行拥塞控制，在承载建立速率高于阈值时，控制承载建立速率。
预置条件|uMAC网元运行正常。开启基于RAT的NAS拥塞控制功能。
测试过程|新增RAT拥塞控制策略：在NB-IoT网络中，指定最大承载速率为50个每秒，超过此阈值后，承载建立拒绝比例为50%。
通过准则|达到拥塞门限时，MME拒绝用户业务，拒绝原因值正确，携带的Back-off Timer正确，按比例拒绝。未达到拥塞门限，MME不会因拥塞拒绝用户业务。按照RAT TYPE+拥塞控制类型进行控制，查看相关性能统计正确。达到拥塞门限则上报告警，低于拥塞门限则告警恢复。
测试结果|-
常见问题处理 :无。 
## ZUF-78-20-003 S6a接口拥塞控制 
特性描述 :特性描述 :术语 :术语|含义
---|---
过负荷控制|限制接入的业务量，来降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。
S6a过负荷控制|根据HSS的负荷报告，控制到HSS的业务，达到降低HSS的负荷的目的。控制S6a口的接收和发送消息速率，避免本局和HSS网元因负荷过高而拥塞。
Back-off Timer|在负荷控制过程中拒绝UE的业务接入时，会携带此参数。UE会延时接入网络，降低网络负荷。
描述 :定义 :过负荷控制功能指在设备处理的业务量超过了规定值时，需要采取保护措施以限制处理的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。 
S6a口过负荷控制指MME网元根据HSS网元的负荷拥塞报告进行出向负荷控制，从而控制到HSS网元的业务量，以保护HSS网元正常工作。当突发业务增多，在MME网元处理能力很强的情况下，对MME网元自身影响不大，但是如果HSS网元处理能力弱或设备老旧，HSS网元会发生负荷拥塞，严重的会导致系统崩溃。 
背景知识 :拥塞和过负荷控制是网元运行安全保障的重要措施。在现网的实际应用中，经常会出现因为某些特定的原因导致用户短时间内暴发超过正常话务模型的业务。这些原因包括：网元重启、传输网故障、用户大量移动、节假日以及特殊事件等。此时，如果不进行拥塞控制，网元的处理能力、资源以及接口带宽都可能达到极限，最终导致网元崩溃，并形成雪崩效应使得整个网络瘫痪。 
根据拥塞和过负荷发生的范围和控制的层次，拥塞和过负荷控制分为： 
面向终端和应用的端到端拥塞控制。 
面向EPC网络的网元间动态过负荷控制。 
针对单一网元的网元自身过负荷控制。 
特定业务和用户的拥塞控制
随着物联网终端的广泛应用，大量的物联网终端接入EPS网络后，由于物联网服务器故障、终端特殊应用、突发事件等会产生短时间内业务量的急剧增加的现象，因此对于拥塞控制的要求更高。特别是当人和物接入同一个EPS网络后，需要对人与物、以及不同的业务和应用，分别实施控制，保证不会因某类用户或某项应用挤占大量的网络资源，而对其他用户的正常业务产生影响。 
网元间的动态过负荷控制
EPC核心网在实际运行中，有多种造成EPC网络信令负荷增高的原因，例如：特定区域大批用户涌入引发的注册信令、频繁的跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等。一旦出现过负荷，由于网络中不同类型的网元处理能力和资源各不相同，往往会出现由某个网元故障或宕机导致的全网瘫痪；所以为了保证整个EPC网络的正常运行，需要各网元配合，从源头上对业务和用户实施控制，来完成整个网络的过负荷控制。 
网元自身的过负荷控制
MME网元是EPC网络中的移动性管理网元，也是终端的控制面接入点。一旦MME网元遭遇到突发业务量增加的情况，MME将直接受到冲击，自身资源（包括处理能力、内部资源、外部接口带宽等）将迅速趋于耗尽；如果MME网元宕机，对整个EPC网络的影响巨大。因此，MME网元需要增加保障自身正常运行的机制，实现自身的过负荷控制。 
MME网元提供的负荷控制功能参见[表1]。 
功能名称|功能概述
---|---
入向业务总量控制|控制单位时间内允许通过的业务总量。业务总量的计算为各个单项业务的加权叠加。
入向单项业务控制|控制单位时间内通过的各个单项业务量。
CPU拥塞控制|在MP上根据CPU拥塞情况对各类业务限制一定的通过率，保护MP的CPU不会冲高。
出向单向业务控制|对于本系统发起的到其他网元（比如HSS、EIR）的业务，限制一定的业务量，保护对方网元不会被冲击。
信令拥塞控制|信令处理MP按照信令链路拥塞情况，保护信令链路（例如：到HSS的偶联链路）。
应用场景 :###### 遭遇突发业务场景 
uMAC网元接入超过估算话务模型的业务量，CPU占用陡升，例如：举办大型赛事、大量外地用户涌入。 
uMAC网元可采用以下过负荷控制功能来保证自身安全： 
入向业务总量控制功能 
入向业务单项控制功能 
CPU拥塞控制功能 
按网元拥塞控制功能 
 说明： 
开启“CPU拥塞控制功能”（该功能默认开启）时，CPU的过载门限为75%，高过载门限为85%。过载拥塞时只对低优先级业务（默认为Attach、Service Request等）进行控制。在CPU高过载时，对所有业务进行控制，包括高优先级业务（默认为TAU/RAU、HO）。 
如果持续出现过负荷告警，建议通过扩容来降低uMAC设备的负荷。 
###### 设备升级场景 
在uMAC设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。 
uMAC网元可采用以下过负荷控制功能来保证自身安全： 
入向业务总量控制功能 
入向业务单项控制功能 
CPU拥塞控制功能 
按网元拥塞控制功能 
 说明： 
建议除了使用默认开启的“CPU拥塞控制功能”外，开启“入向业务单项控制功能”对Attach业务进行限制。 
限制的数值为1小时内所有用户接入的速率，即全部接入的用户数/MP模块数/3600。例如：本局有100万用户，16个模块，则需要限制Attach接入业务数为1000000/16/3600=17次。 
###### 邻接网元处理能力弱场景 
由于HLR/HSS是老旧网元或未完成扩容，整体处理能力弱。在SGSN/MME业务繁忙时，无法处理位置更新业务，甚至出现了宕机重启的情况。 
uMAC网元提供了如下功能来保护邻接网元： 
出向单项业务控制功能 
信令拥塞控制功能 
 说明： 
除默认开启“信令拥塞控制功能”外，还建议开启“出向单项业务控制功能”，对SGSN/MME发出的业务进行控制。例如，如果HLR/HSS最多处理1000条/秒位置更新业务消息，则可以在出向单项业务控制功能中配置本局到该HLR/HSS局向最多发送1000条/秒位置更新业务消息。 
客户收益 :受益方|受益描述
---|---
运营商|在突发大话务情况下，防止uMAC设备异常或者崩溃，提高网络的稳定性。通过特定局向的负荷控制，保障HSS网元的稳定性。
移动用户|在大量突发业务冲击的场景下，使得移动用户可以接入网络，用户业务不受影响。
实现原理 :系统架构 :S6a接口拥塞控制功能的系统架构如[图1]所示。
图1  系统架构图-S6a接口拥塞控制

涉及的网元 :网元名称|网元作用
---|---
MME|通知eNB、MME设备发生拥塞。通知SGW/PGW、MME设备发生拥塞。接收HSS的过负荷通知，完成拥塞控制。接收SGW/PGW的过负荷通知，完成拥塞控制。接收PGW的APN拥塞指示，完成拥塞控制。完成基于APN和MTC Group Identifier的拥塞控制。完成MME过负荷控制。
eNB|接收MME的过负荷通知消息，并进行拥塞控制。
HSS|通知MME、HSS设备发生拥塞。为MTC用户签约特定的Group ID。
UE|接收MME的拒绝消息，启动back-off timer，超时前不发起业务。
协议栈 :eNodeB与MME之间的协议栈如[图2]所示。
图2  eNodeB与MME协议栈

HSS与MME之间的协议栈如[图3]所示。
图3  MME与HSS协议栈

本网元实现 :uMAC过负荷控制功能控制的是用户业务流程的首个消息，对后续消息放行。在系统负荷允许的范围内通过尽量多的业务。用户业务被拒绝后，通过重新尝试，可以逐渐平滑的接入进来。 
uMAC过负荷控制流程如[图4]所示。
图4  uMAC负荷控制流程图

 说明： 
默认情况下，uMAC系统已开启CPU负荷控制和信令拥塞控制，未开启业务流量控制（包括出向和入向）和网元拥塞控制。在默认配置下已经能很好地保护自身网元，同时对邻接网元开启了基本保护。 
HSS网元过负荷控制
由于网络故障引发大量UE和MTC设定重新附着，或者因节假日业务激增等原因，引发HSS在短时间内突发大量的业务，发生过负荷。 
HSS将包含序列号、有效时长和减少百分比等信息的过负荷报告发送至MME。 
MME根据过负荷报告的信息以及业务的优先级，减少到HSS的业务负荷。 
MME网元自身的过负荷控制
当MME发现自身CPU负荷过高，处理能力不足的情况下，可以有选择地拒绝来自UE以及GW、MSC等各项业务的接入。 
MME在实施控制时，针对业务流程的首个消息实施控制，而对后续消息放行。这样可以保证业务在第一时间受控，尽可能减少对系统负荷的影响；同时，也能保证系统具备一定的通过数，防止因大量业务积压后反复尝试而造成雪崩效应，使得过负荷状态无法恢复。 
针对UE的上行业务，MME在拒绝时，通过返回在一定范围内随机化的Back-Off Timer的方式，可以有效地控制UE后继的业务重试，将业务洪峰在一段时间内离散化，使得UE的业务接入更加平滑，确保MME在高负载状态下的业务处理。 
MME由于受到话务冲击，接收的附着和TAU消息量陡然增加时，会对HSS产生冲击，通过控制MME到HSS的消息量来降低HSS的负荷。 
业务流程 :HSS过负荷，S6a口拥塞控制
MME和HSS业务交互过程中，HSS在过负荷情况时，会在响应消息中携带OC-Supported-Features和OC-OLR通知HSS已经发生拥塞。如[图5]所示。
图5  HSS拥塞通知

MME在位置更新、鉴权向量获取、Purge用户、HSS通知业务过程中， 收到HSS的响应消息， 消息中携带OC-Supported-Features和OC-OLR过负荷参数。 
HSS将包含序列号、有效时长和减少百分比等信息的过负荷报告通知MME。  
MME根据HSS的过负荷报告完成过负荷控制。 
MME控制HSS局向拥塞
MME和HSS业务交互过程中，由于MME触发的位置更新和鉴权向量获取导致HSS过负荷拥塞，MME产生业务失败。MME根据HSS的负荷，开启HSS局向消息控制功能，减少到HSS的消息数量，降低HSS的业务负荷，消息流程如[图6]所示。
图6  MME控制HSS局向拥塞

MME控制从S6a口接收和发送的消息数量
MME和HSS业务交互过程中，MME为保护自身网元不被冲击，设置单位时间内从S6a口接收和发送的消息数量，以达到控制MME负荷和HSS负荷的目的。在EM上执行[SET INTERFACE MSG OVERLOAD]命令来设置S6a口收发消息数量。消息流程如[图7]所示。
图7  S6a口接收/发送消息控制

MME可以通过控制从HSS接收的消息数量，降低MME的负荷。 
MME可以控制发送给HSS的消息数量，降低HSS的负荷。 
系统影响 :开启拥塞和过负荷控制功能后，当系统处于拥塞或过负荷的情况下，MME会采用简单有效的方法拒绝部分业务处理，从而降低系统负荷。 
负荷控制对终端的接入有一定时间延时。拥塞控制功能本身对系统处理能力和资源消耗的影响可以忽略。 
应用限制 :如果UE不支持退避时间（Back-off Time）的处理，将会一定程度上弱化拥塞控制的效果。虽然MME可以对处于退避时间内的UE实施持续的接入控制，但是如果UE在短时间内多次发起尝试，还是对网络处理能力和资源有少许消耗。 
如果HSS不支持拥塞报告（OC-OLR AVP），将会一定程度上弱化拥塞控制的效果。虽然MME可以根据自身附着\TAU成功率以及失败统计来判断HSS发生拥塞，但是时间上会有延时，还是会对网络处理能力和资源有少许消耗。 
特性交互 :相关特性|交互关系
---|---
紧急呼叫|紧急呼叫在拥塞控制中，具备最高优先级，作为最后被限制的业务。
MPS业务|MPS在拥塞控制中，具备最高优先级，作为最后被限制的业务。
遵循标准 :标准名称|章节
---|---
GPP TS 23.401: “General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”|4.3.7.4 MME control of overload
3GPP TS 29.272: ”Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol”|Annex D (Informative): Diameter overload control node behaviour
3GPP TS 36.413: " S1 Application Protocol (S1AP)|8.7.6 Overload Start8.7.7 Overload Stop
特性能力 :名称|指标
---|---
支持HSS过负荷控制的最大HSS节点数|2048（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请License许可后，运营商才能获得该特性的服务。 
该特性对应License文件中的项目为：“MME支持HSS过负荷控制功能”，显示为ON，表示uMAC支持相应的过负荷控制功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
SGW/PGW需要支持GTP-C过负荷控制功能。 
HSS需要支持Diameter过负荷控制功能。 
UE需要支持Back-off Timer。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项相关的配置项参见下表。配置项命令HSS过负荷控制配置SET HSS OVERLOAD CONTROLSHOW HSS OVERLOAD CONTROL 
安全变量该特性不涉及安全变量的变化。 
软件参数软件参数ID软件参数名称262573diameter对端指示too busy过载时长262572diameter对端指示too busy过载业务缩减百分比率 
动态管理动态管理项命令说明查询HSS负荷信息SHOW HSS OVERLOAD INFO该命令用于查询MME接收到的不同HSS返回的过负荷信息。过负荷信息包括HSS主机名/域、过负荷信息序列号、报告类型、有效时间和缩减比例。 
性能统计 :新增性能计数器参见下表。 
测量类型|描述
---|---
Diameter接口负荷控制测量|编号为C43302开头的所有计数器
告警和通知 :通知
---
2114060424 HSS过负荷发生通知|2114060424 HSS过负荷发生通知
业务观察/失败观察 :失败原因|波及业务|产生原因|处理建议
---|---|---|---
Adjacent Office is Overload|位置更新与获取鉴权向量|MP模块每秒向Diameter局向发送的位置更新业务数或者获取鉴权向量数超过设定的最大值。HSS发生拥塞，MME根据HSS的拥塞报告进行控制， 控制发送到HSS的业务消息量。为防止HSS拥塞， 减少位置更新或鉴权向量获取次数。|检查是什么原因导致MME业务量突然增加。检查HSS为何产生负荷拥塞。
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本配置用于实现S6a口拥塞控制。当HSS网元过负荷时，需要开启S6a口拥塞控制功能，防止大量用户接入。配置完成后，MME根据HSS的负荷报告，控制S6a口的接收和发送消息速率，避免本局和HSS网元因负荷过高而拥塞。 
配置前提 :License开启"MME支持HSS过负荷控制"。 
配置过程 :在EM执行[SET HSS OVERLOAD CONTROL]命令，开启HSS过负荷控制开关，并设置拒绝携带的back-off timer的最大值和最小值。
配置实例 :场景说明 :因网元故障或升级造成网元重启，大量用户重新接入，HSS因无法承受突发的大量业务而发生过负荷。 
数据规划 :配置项|参数名称|取值
---|---|---
设置HSS过负荷控制|支持HSS过负荷|支持
HSS过负荷发生时，拒绝携带的Back-off Timer最小值（秒）|设置HSS过负荷控制|0~1116000
HSS过负荷发生时，拒绝携带的Back-off Timer最大值（秒）|设置HSS过负荷控制|0~1116000
配置步骤 :步骤|说明|命令
---|---|---
1|开启HSS过负荷控制开关，并设置拒绝携带的Back-off Timer的最小值和最大值分别为1 s和2 s。|SET HSS OVERLOAD CONTROL:OVERLOAD="YES",MIN=1,MAX=2
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|HSS过负荷控制
---|---
测试目的|测试HSS主机过负荷
预置条件|环境运行正常，License开启支持“MME支持HSS过负荷控制功能”。在EM上配置支持HSS过负荷控制，并设置back-off timer。当前HSS局向协议版本号为R12。
测试过程|大量用户接入，MME收到HSS发送的消息中携带过载业务缩减百分比为100，失败原因为DIAMETER_TOO_BUSY（3004）。
通过准则|-
测试结果|MME可以发送AIR（Authentication-Information-Request）、ULR（Update-Location-Request）消息到备用HSS，NOR(Notify-Request)、PUR(Purge-UE-Request)消息无法发送到备用HSS。
测试项目|Diameter too busy拥塞控制
---|---
测试目的|测试Diameter too busy拥塞控制
预置条件|环境运行正常，License开启支持“MME支持HSS过负荷控制功能”。在EM上配置支持HSS过负荷控制，并设置back-off timer。配置软参“diameter对端指示too busy过载业务缩减百分比率（262572）”的业务缩减百分比。配置软参“diameter对端指示too busy过载时长（262573）”的过载持续时长。当前HSS局向协议版本号为R12。
测试过程|MME收到HSS发送的消息中携带OC_OLR，过负荷有效时长为10 s，过载业务缩减百分比100，失败原因为DIAMETER_TOO_BUSY（3004）。MME向UE发送拒绝消息，携带diameter too busy映射原因值和配置的back-off timer。MME产生2114060424 HSS过负荷发生通知，在有效时长（10 s）内，MME不再向HSS发送消息。
通过准则|-
测试结果|HSS在过负荷情况下，MME不发送请求消息到该HSS。
常见问题处理 :无 
## ZUF-78-20-004 GTP-C接口拥塞控制 
特性描述 :特性描述 :术语 :术语|
---|---
过负荷控制（OL）|限制接入的业务量，用来降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。
MPS|MPS是一种端到端的多媒体优先级业务。MPS能够允许授权的“业务用户”在网络发生拥塞、会话建立受阻时，获取优先于其他用户的无线信道接入权利，能够优先发起、修改、保持、释放会话以及投递媒体报文。
GTP-C接口|MME和SGSN网元存在的GTP-C接口：SGSN (Gn/Gp、Ga)      MME(  Sv   S11  S10  Gn/Gp S3 )
描述 :定义 :GTP-C接口拥塞控制指由于网络故障或者节假日导致业务激增，引发相关GTP-C接口业务大量增加，MME在相关的GTP-C接口上进行控制，从而保障MME和周边GTP-C接口网元处理正常。 
背景知识 :拥塞和过负荷控制是网元运行安全保障的重要措施。在现网的实际应用中，网元重启、传输网故障、用户大量移动、节假日以及特殊事件等原因会导致用户短时间内暴发。此时，如果不进行拥塞控制，网元的处理能力、资源以及接口带宽都可能达到极限，最终导致自身和周边网元崩溃，并形成雪崩效应使得整个网络瘫痪。 
根据拥塞和过负荷发生的范围和控制的层次，拥塞和过负荷控制分为： 
面向终端和应用的端到端拥塞控制。 
面向EPC网络的网元间动态过负荷控制。 
针对单一网元的网元自身过负荷控制。 
面向终端和应用的端到端拥塞控制
大量的物联网终端接入EPS网络后，物联网服务器故障、终端特殊应用、突发事件等原因会导致短时间内业务量急剧增加，因此对拥塞控制的要求也就更高。 
当人和物接入同一个EPS网络后，需要对不同的业务和应用分别实施控制，保证不会因某类用户或某项应用挤占大量的网络资源，而对其他用户的正常业务产生影响。 
面向EPC网络的网元间动态过负荷控制
实际运行中，造成EPC网络信令负荷增高的原因有多种，例如：特定区域大批用户涌入引发的注册信令、频繁的跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等。一旦出现过负荷现象，由于网络中不同类型的网元处理能力不同，可能出现某个网元故障或宕机导致全网瘫痪的现象。为了保证整个EPC网络的正常运行，需要各网元相互配合，从源头上对业务和用户实施控制，完成对整个网络的过负荷控制。 
针对单一网元的网元自身过负荷控制
MME是EPC网络中的移动性管理网元，也是终端的控制面接入点，一旦遭遇到业务量突发增加的情况，MME将更加直接的受到冲击，自身资源（包括处理能力、内部资源、外部接口带宽等）将迅速趋于耗尽。如果MME网元宕机，对整个EPC网络的影响也十分巨大。因此，MME网元需要增加保障自身正常运行的机制，实现对自身的过负荷控制。 
应用场景 :uMAC网元拥塞告警的场景如下： 
遭遇突发业务场景 
uMAC网元短时间内接入超过估算话务模型的业务量，CPU占用陡升。例如，举办大型赛事，大量外地用户涌入。 
uMAC设备升级场景 
设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。 
邻接的网元处理能力弱场景 
由于老的网元或未完成扩容，整体处理能力弱，在SGSN/MME业务繁忙时，导致外部网元负荷增加，导致拥塞，甚至出现了宕机重启的情况。 
EPC核心网GTP-C接口拥塞过负荷控制，提供了如下功能保护自身和外部网元： 
出向业务控制功能 
信令拥塞控制功能 
###### 场景一：SGW/PGW网元过负荷 
因网元故障或升级造成网元重启，会有大量用户重新接入，造成短时间内全网负荷激增。 
EPC核心网网元过负荷主要体现在SGW、PGW等网元，因无法承受突发的大量业务而发生过负荷。 
下游网元（如SGW\PGW）自身难以有效控制业务接入，简单拒绝反而会造成更大量的业务重试，形成雪崩效应，所以需要采用网元间动态的过负荷控制机制。将下游网元的过负荷情况通知到上游网元（如MME），要求上游网元从源头实施控制；同时下游网元根据控制结果实时向上游网元反馈当前的过负荷情况，实现闭环控制，从而保证整个核心网长期稳定运行，有效应对短时间内业务激增的情况。 
MME需要根据SGW/PGW网元在交互消息中返回的过负荷信息，完成对相关网元的过负荷控制。 
此外也可以通过配置MME的S11\S10\SV\gn等接口消息控制功能限制向SGW/PGW发送消息，避免对SGW/PGW的冲击。 
###### 场景二：MME自身过负荷 
因无线节点故障或重启造成大量用户重新接入，或者节假日集中爆发的业务，造成MME短时间内负荷激增。 
MME自身过负荷主要体现在MME自身资源（包括处理能力、内部资源、外部接口带宽等）使用接近极限。此时MME网元出于保障自身正常运行的需要，根据接入业务类型和优先级以及用户类型实施过负荷控制，同时向SGW/PGW发送过负荷信息。MME需要根据接入业务类型和优先级以及用户类型实施过负荷控制。 
客户收益 :受益方|受益描述
---|---
运营商|防止设备被大量突发业务冲击，在突发大话务情况下，不会异常或者崩溃，提高网络的稳定性。另外通过特定局向负荷控制，保障相关网元 （SGW/PGW/MSC等）的稳定性。
移动用户|网元设备被大量业务冲击造成网络瘫痪后，移动用户将无法接入网络。 MME通过负荷控制功能控制入向和出向业务，使得移动用户在突发场景导致业务暴增的情况下， 能够逐步接入网络，从而保障移动用户的业务不受影响。
实现原理 :系统架构 :本特性涉及的系统架构如[图1]所示。
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
MME|通知eNB，MME设备发生拥塞。通知SGW/PGW，MME设备发生拥塞。接收HSS的过负荷通知，完成拥塞控制。接收SGW/PGW的过负荷通知，完成拥塞控制。接收PGW的APN拥塞指示，完成拥塞控制。完成基于APN的拥塞控制和基于MTC Group Identifier的拥塞控制。完成MME过负荷控制。完成GTP接口的接收和发送消息速率控制。包括：S11\SV\S10\Gn逻辑接口。
SGW|通知MME，SGW设备发生拥塞。接收MME的过负荷通知，完成拥塞控制。
PGW|通过SGW通知MME，PGW设备发生拥塞。接收MME的过负荷通知，完成拥塞控制。
UE|接收MME的拒绝消息，启动back-off timer，超时前不发起业务。
协议栈 :MME与SGW之间的协议栈如[图2]所示。
图2  S11接口协议栈

MME与MME之间的协议栈如[图3]所示。
图3  S10接口协议栈

MME与MSC SRVCC切换之间的协议栈如[图4]所示。
图4  SV接口协议栈

MME与SGSN接口协议栈如[图5]所示。
图5  MME与GnGp SGSN接口协议栈

本网元实现 :MME GTP-C接口过负荷控制功能控制的是用户业务流程中，从GTP接口接收到对端网元的业务，以及向GTP接口的相关网元发起业务时，MME对MME自身以及外部GTP网元进行负荷控制，在系统负荷允许的范围内通过尽量多的业务。进行负荷控制时，用户业务被拒绝后，通过重新尝试，可以逐渐平滑的接入网络。 
MME GTPC网元过负荷控制功能说明如[图6]所示。
图6  GTPC网元负荷控制

业务流程 :基于业务类型和用户类型的信令拥塞控制： 
基于APN的拥塞控制
针对特定的APN，MME可控制用户发起业务，避免对APN对应的PGW POOL造成信令与承载冲击。 
MME可基于下面4个条件判断是否拒绝业务： 
业务使用的APN在MME已建立承载数超过配置门限。 
业务使用的APN在MME建立承载速率超过配置门限。 
签约此APN的用户发送NAS MM信令速率超过门限。 
该APN对应的PGW指示APN拥塞，且在有效期内。 
MME将在拒绝消息中携带Back-Off Timer，通知用户在一段时间内不再发起移动性管理或会话管理业务，减小发送到PGW的信令数，减少PGW承载资源占用。 
其中，满足[条件1]和[条件2]控制的会话管理类流程包括：
附着，流程说明参见协议3GPP TS 23.401中的“附着流程”。 
PDN连接请求，流程说明参见协议3GPP TS 23.401中的“多PDN连接流程”。 
承载资源申请，流程说明参见协议3GPP TS 23.401中的“专有承载建立流程”。 
承载资源修改，流程说明参见协议3GPP TS 23.401中的“承载修改流程”。 
满足[条件3]控制的移动性管理类流程包括：
附着，流程说明参见协议3GPP TS 23.401中的“附着流程”。 
TAU，流程说明参见协议3GPP TS 23.401中的“跟踪区更新流程”。 
业务请求，流程说明参见协议3GPP TS 23.401中的“业务请求和寻呼流程”。 
满足[条件4]控制的会话管理类流程包括：
附着，流程说明参见协议3GPP TS 23.401中的“附着流程”。 
PDN连接请求，流程说明参见协议3GPP TS 23.401中的“多PDN连接流程”。 
基于MTC用户的拥塞控制
MME可控制签约了特定Group ID的用户，拒绝此类用户发起的业务。同时MME也可以控制签约了特定Group ID与使用某APN或签约某特定APN的用户，拒绝此类用户发起业务，以便APN对应的PGW POOL保留资源提供给其他用户。 
MME在拒绝消息中携带BackOff Time，通知用户在一段时间内不再发起业务，以避免对MME网元造成冲击。 
MME接收到此类用户发起的业务，一旦发现： 
MME中签约此Group ID的这类用户发送NAS信令速率超过门限，MME将限制相关的移动性管理与会话管理业务。包括以下业务流程： 
附着，流程说明参见协议3GPP TS 23.401中的“附着流程” 
TAU业务，流程说明参见协议3GPP TS 23.401中的“跟踪区更新流程” 
业务请求，流程说明参见协议3GPP TS 23.401中的“业务请求和寻呼流程” 
PDN连接请求，流程说明参见协议3GPP TS 23.401中的“多PDN连接流程” 
承载资源申请，流程说明参见协议3GPP TS 23.401中的“专有承载建立流程” 
承载资源修改，流程说明参见协议3GPP TS 23.401中的“承载修改流程” 
MME中签约此Group ID与使用此APN的这类用户建立承载数超过门限，MME将限制签约了特性Group ID的用户不再发起此APN相关的会话管理业务。包括以下业务流程： 
附着，流程说明参见协议3GPP TS 23.401中的“附着流程” 
PDN连接请求，流程说明参见协议3GPP TS 23.401中的“多PDN连接流程” 
承载资源申请，流程说明参见协议3GPP TS 23.401中的“专有承载建立流程” 
承载资源修改，流程说明参见协议3GPP TS 23.401中的“承载修改流程” 
MME中签约此Group ID与签约此APN的这类用户发送NAS信令速率超过门限，MME将限制签约此Group ID与签约此APN的用户不再发起移动性管理业务。包括以下业务流程： 
附着，流程说明参见协议3GPP TS 23.401中的“附着流程” 
TAU业务，流程说明参见协议3GPP TS 23.401中的“跟踪区更新流程” 
业务请求，流程说明参见协议3GPP TS 23.401中的“业务请求和寻呼流程” 
网元间的动态过负荷控制
SGW网元过负荷控制 
由于网络故障引发大量UE和M2M设定重新附着，或者因节假日业务激增以及大量用户反复在空闲态和连接态切换等原因，引发SGW短时间内突发大量的业务，发生过负荷。 
SGW发生过负荷后，将包含序列号、有效时长和减少百分比等信息的过负荷信息通知MME。 
MME根据过负荷信息完成过负荷控制：在信息有效时长内，按减少百分比，根据业务的优先级，减少到该SGW的业务负荷。 
PGW网元的网元级过负荷控制 
由于网络故障引发大量UE和M2M设定重新附着，或者因节假日业务激增以及大量用户反复在空闲态和连接态切换等原因，引发PGW短时间内突发大量的业务，发生过负荷。 
PGW发送过负荷后，将包含序列号、有效时长和减少百分比等信息的过负荷信息通过SGW通知MME。 
MME根据过负荷信息完成过负荷控制：在信息有效时长内，按减少百分比，根据业务的优先级，减少到该PGW的业务负荷。 
PGW网元的APN级过负荷控制 
由于PGW为不同的APN分配的可用资源不同，而某个APN因某种原因引发短时间内突发大量的业务，造成该APN资源不足发生过负荷；当PGW的某个APN发生过负荷后，PGW有两种方式实施基于APN的拥塞和过负荷控制。 
PGW将包含APN、序列号、有效时长和减少百分比等信息的过负荷信息通知MME，MME根据过负荷信息完成过负荷控制：在信息有效时长内，按减少百分比，根据业务的优先级，减少到该PGW上该APN的业务负荷。 
PGW收到该APN的创建会话请求后返回拒接，携带“APN拥塞”的拒绝原因，以及退避时间（back-off time）。MME收到拒绝后，在退避时间，该APN的PDN链接都不再选择该PGW。 
上述两种方式，同一时间有一种生效。 
MME网元过负荷通知 
MME发生过负荷后，MME将过负荷信息通过SGW通知给PGW，由PGW根据过负荷信息，完成过负荷控制，降低到MME的专有承载建立/修改等业务负荷。 
MME发生过负荷后，MME在DDN响应消息中向SGW返回控制门限和延迟时间，由SGW完成对DDN消息的控制。 
MME发生过负荷后，MME通过S1口消息将自身的过负荷情况通知eNB，要求eNB按一定比例缩减到此发生过负荷的MME的业务量，完成过负荷控制。 
MME网元自身的过负荷控制功能
当MME发现自身CPU负荷过高，处理能力不足的情况下，可以有选择的拒绝来自UE以及GW、MSC等各项业务接入。 
MME在实施控制时，针对业务流程的首个消息实施控制，而对后续消息放行。这样可以保证业务在第一时间受控，尽可能的减少对系统负荷的影响；同时，也能保证系统具备一定的通过数；防止大量业务积压反复尝试造成雪崩效应，使得过负荷状态无法恢复。 
针对UE的上行业务，MME在拒绝时，通过返回在一定范围内随机化的Back-Off Timer的方式，可以有效的控制UE后继的业务重试，更好的将业务洪峰在一段时间内离散化，使得UE的业务接入更加平滑，更好的确保MME在高负载状态下的业务处理。 
系统影响 :开启拥塞和过负荷控制功能后，当系统处于拥塞或过负荷的情况下，会采用简单有效的方法拒绝部分业务，从而降低系统负荷。拥塞控制功能本身对系统处理能力的影响和资源消耗可以忽略。 
当SGW/PGW网元处于拥塞或者过负荷状态，SGW/PGW会向MME发送通知，MME会根据负荷情况降低发送到SGW/PGW的消息数量， 从而降低负荷。对系统处理能力的影响和资源消耗可以忽略。 终端的会话接入有一定时间延时。 
在GTP-C的各个网元接口上， MME控制接收消息和发送消息的速率， 保障MME和对端网元的状态。 
应用限制 :如果UE不支持退避时间（Backoff Time）的处理，一定程度上会弱化拥塞控制的效果。虽然MME可以对处于退避时间内的UE实施持续的接入控制，但如果UE在短时间内多次发起尝试，还是会消耗网络处理能力和资源。 
如果SGW/PGW不携带负荷报告（包括：SGW OVERLOAD、PGW OVERLOAD），MME无法判断出SGW/PGW的负荷信息，无法快速应对SGW/PGW的拥塞，将会一定程度上弱化拥塞控制的效果。但是MME可以根据自身附着TAU成功率以及失败统计来判断SGW/PGW的拥塞状况，但是时间上会有延时，对网络处理能力和资源有少许消耗。 
特性交互 :相关特性|交互关系
---|---
ZUF-78-12-003 LTE IMS紧急会话支持|紧急呼叫在拥塞控制中，具备最高优先级，作为最后被限制的业务。
ZUF-78-15-011 MPS|MPS在拥塞控制中，具备较高优先级，作为最后被限制的业务之一。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: “General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”|4.3.7.1a GTP-C signalling based Load and Overload Control；4.3.7.4 MME control of overload4.3.7.5 PDN GW control of overload
3GPP TS 36.413: "S1 Application Protocol (S1AP)”|全部
3GPP TS 29.274: “Tunnelling Protocol for Control plane (GTPv2-C)”|12 GTP-C load & overload control mechanism
特性能力 :名称|指标
---|---
支持GTP-C过负荷控制的最大GTP-C节点数|2048（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性对应License文件中的项目为： 
MME支持GTP-C负荷控制功能 
MME支持GTP-C过负荷控制功能 
MME支持基于APN拥塞控制功能 
MME支持基于MTC用户拥塞控制功能 
MME支持PGW的APN拥塞功能 
对应项目显示为ON，表示ZXUN uMAC支持相应的过负荷控制功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|-
 说明： 
SGW/PGW需要支持GTP-C过负荷控制功能。 
UE需要支持Back-off Timer 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME通用业务控制配置SET MME OVERLOAD PARASHOW MME OVERLOAD PARA到GW的过负荷配置SET MME OVERLOAD INFO TO GWSHOW MME OVERLOAD INFO TO GWMME接口消息控制配置SET INTERFACE MSG OVERLOADSHOW INTERFACE MSG OVERLOADSGW过负荷控制的配置信息SET SGW OVERLOAD CONTROLSHOW SGW OVERLOAD CONTROLPGW过负荷控制的配置信息SET PGW OVERLOAD CONTROLSHOW PGW OVERLOAD CONTROL基于APN拥塞控制开关SET APN CONGESTION SWITCHSHOW APN CONGESTION SWITCHAPN拥塞控制策略配置ADD APN CONGESTION POLICYSET APN CONGESTION POLICYDEL APN CONGESTION POLICYSHOW APN CONGESTION POLICY基于MTC用户的MME网元拥塞控制开关SET MTCMME CONGESTION SWITCHSHOW MTCMME CONGESTION SWITCHMTC用户的MME网元拥塞控制策略配置ADD MTCMME CONGESTION POLICYSET MTCMME CONGESTION POLICYDEL MTCMME CONGESTION POLICYSHOW MTCMME CONGESTION POLICY基于MTC用户的APN拥塞控制开关SET MTCAPN CONGESTION SWITCHSHOW MTCAPN CONGESTION SWITCHMTC用户的APN拥塞控制策略配置ADD MTCAPN CONGESTION POLICYSET MTCAPN CONGESTION POLICYDEL MTCAPN CONGESTION POLICYSHOW MTCAPN CONGESTION POLICY下行数据通知延迟配置SET DDN DELAYSHOW DDN DELAY 
安全变量该特性不涉及安全变量。 
软件参数表2  相关软件参数软件参数ID软件参数名称262493TAU业务是否支持NAS拥塞控制262494业务请求是否支持NAS拥塞控制262495承载修改是否支持NAS拥塞控制262496已下发移动性管理BackOff Time再次接入拒绝携带原因262497已下发会话管理BackOff Time再次接入拒绝携带原因262498MME过负荷控制是否拒绝连接态TAU 
动态管理表3  SGW/PGW相关动态管理动态管理项命令说明查询SGW负荷信息SHOW SGW LOAD INFO用于查询MME接收到的不同SGW返回的动态负荷信息。负荷信息包括SGW主机名、负荷信息序列号、负荷值查询PGW负荷信息SHOW PGW LOAD INFO用于查询MME接收到的不同PGW返回的网元级或APN级的动态负荷信息。负荷信息包括PGW主机名和APN NI、负荷信息序列号、负荷值。查询SGW过负荷信息SHOW SGW OVERLOAD INFO用于查询MME接收到的不同SGW返回的过负荷信息。过负荷信息包括SGW主机名、过负荷信息序列号、有效时间和缩减值。查询PGW过负荷信息SHOW PGW OVERLOAD INFO用于查询MME接收到的不同PGW返回的网元级或APN级的动态负荷信息。过负荷信息包括PGW主机名和APN NI、过负荷信息序列号、有效时间和缩减值。 
性能统计 :性能计数器名称
---
C433010001 由于负荷控制拒绝的专有承载激活请求消息个数
C433010002 由于负荷控制丢弃的专有承载激活请求消息个数
C433010003 由于负荷控制拒绝的承载更新请求消息个数
C433010004 由于负荷控制丢弃的承载更新请求消息个数
C433010005 由于负荷控制拒绝的下行数据通知消息个数
C433010006 由于负荷控制丢弃的下行数据通知消息个数
C433010007 由于负荷控制拒绝的切换请求消息个数
C433010008 由于负荷控制丢弃的切换请求消息个数
C433010009 因负荷控制而丢弃的Configuration Transfer Tunnel消息个数
告警和通知 :告警和通知
---
2114060432 SGW过负荷发生通知
2114060444 SGW过负荷解除通知
2114060445 PGW过负荷发生通知
2114060446 PGW过负荷解除通知
2114060422 PGW APN拥塞发生通知
2114060423 PGW APN拥塞解除通知
3305504772 业务过负荷告警
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置GTP-C接口拥塞控制功能，能够确保网络设备安全运行，减轻网络信令压力，避免网络拥塞。 
主要涉及MME到GW的过负荷配置、SGW过负荷控制配置和PGW过负荷控制配置。 
配置前提 :用户需要获取MME支持GTP-C过负荷控制功能的license权限。 
配置过程 :执行以下命令，打开支持SGW过负荷控制功能，按需设置Back-off Timer时长。 
[SET SGW OVERLOAD CONTROL]
执行以下命令，打开支持PGW过负荷控制功能，打开支持PGW Back-off time控制功能，按需设置Back-off Timer时长。 
[SET PGW OVERLOAD CONTROL]
执行以下命令，打开向PGW发送过负荷信息的控制开关，合理设置发送过负荷信息的CPU门限。 
[SET MME OVERLOAD INFO TO GW]
配置实例 :###### MME的SGW/PGW网元过负荷控制 
场景说明
由于网元故障或升级导致网元重启，大量用户重新接入，造成SGW/PGW网元负荷激增。 
数据规划
配置项|参数名称|取值
---|---|---
设置SGW过负荷控制|支持SGW过负荷控制|支持
拒绝时携带的Back-off Timer最小值(秒)|设置SGW过负荷控制|3600
拒绝时携带的Back-off Timer最大值(秒)|设置SGW过负荷控制|18000
设置PGW过负荷控制|支持PGW过负荷控制|支持
支持PGW Back-off time控制|设置PGW过负荷控制|支持
拒绝时携带的Back-off Timer最小值(秒)|设置PGW过负荷控制|3600
拒绝时携带的Back-off Timer最大值(秒)|设置PGW过负荷控制|18000
配置步骤
步骤|说明|命令
---|---|---
1|打开支持SGW过负荷控制功能|SET SGW OVERLOAD CONTROL:OVERLOAD="YES"
2|打开支持PGW过负荷控制功能|SET PGW OVERLOAD CONTROL:OVERLOAD="YES",PGWBACKTIME="YES"
###### MME自身过负荷通知SGW/PGW 
场景说明
因无线节点故障或重启造成大量用户重新接入，或者节假日集中爆发的业务，造成MME短时间负荷激增。 
数据规划
配置项|参数名称|取值
---|---|---
设置到GW的过负荷|发送过负荷信息的CPU门限|70
过负荷信息发送周期(秒)|设置到GW的过负荷|600
向PGW发送过负荷信息的控制开关|设置到GW的过负荷|只向本PLMN的PGW发送(PLMN)
配置步骤
步骤|说明|命令
---|---|---
1|打开向PGW发送过负荷信息的控制开关|SET MME OVERLOAD INFO TO GW:TOPGW="PLMN"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|SGW过负荷控制
---|---
测试目的|测试SGW过负荷控制功能。
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME支持GTP-C过负荷控制功能的license授权，并更新了license。开启支持SGW过负荷控制功能。
测试过程|大量用户综合业务接入，SGW过负荷。SGW给MME发送本SGW的过负荷信息。批量用户从相同TA接入，该TA解析到多个SGW都过负荷。
通过准则|MME按照缩减比随机对接入用户进行拒接。MME带给被拒绝用户backoff时间，其数值在网管配置的最大值和最小值之间。
测试结果|–
测试项目|PGW过负荷控制
---|---
测试目的|测试PGW过负荷控制功能。
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME支持GTP-C过负荷控制功能的license授权，并更新了license。开启支持PGW过负荷控制功能，支持PGW Backoff time控制。
测试过程|大量用户综合业务接入，PGW过负荷。SGW携带该PGW的过负荷信息给MME。批量用户使用同一APN接入，该APN解析到多个PGW全部过负荷。
通过准则|MME按照缩减比随机对接入用户进行拒接。被缩减的用户，返回给用户backoff时间，其数值在网管配置的最大值和最小值之间。
测试结果|–
测试项目|MME过负荷控制
---|---
测试目的|测试MME过负荷时会通知PGW。
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME支持GTP-C过负荷控制功能的license授权，并更新了license。向PGW发送过负荷信息的控制开关配置为只向本PLMN的PGW发送。
测试过程|大量用户综合业务接入MME，MME负荷达到发送负荷信息的CPU门限。本地用户附着接入。国际漫游用户附着接入。
通过准则|对于本地用户，MME发给本地PGW的GTP消息携带MME的过负荷信息。对于国际漫游用户，MME发给归属地PGW的GTP消息不携带MME的过负荷信息。
测试结果|–
常见问题处理 :无。 
## ZUF-78-20-005 终端异常信令管控 
特性描述 :特性描述 :描述 :定义 :终端异常信令管控是指当终端在不停的尝试业务，但是却一直异常时，MME会采取一定的措施，减少终端触发的信令，避免引起网络拥塞。
信令风暴抑制是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
MME信令风暴抑制是用户级的抑制，针对终端发起的三种信令进行抑制，包括附着请求信令抑制、业务请求信令抑制和PDN连接请求信令抑制。 
背景知识 :引发信令风暴的原因有很多，主要包括如下原因： 
特殊事件：由于集会、节日、传输中断等导致短时间内大量用户发起业务，带来的信令冲击超过网络的处理能力。 
设备故障：LTE核心网的设备故障、重启或用户卸载等场景触发大量用户同时重新连接网络，触发信令风暴。 
终端问题：因下述原因，终端业务连续失败后，终端会不断重发信令请求，附着请求/业务请求/PDN连接请求频繁发生。当一定时间内信令请求数很多，即将超过网络信令资源的处理能力，就会触发信令风暴。终端APN或其他参数错误终端中毒终端恶意攻击网络传输中断区域限制业务服务器Down其他原因 
不同原因导致的信令风暴，其抑制手段也不同： 
特殊事件：MME启用智能过负荷控制，保证发生信令风暴时正常服务。 
设备故障：MME启用智能过负荷控制，保证发生信令风暴时正常服务。 
终端问题：MME对附着请求/业务请求/PDN连接请求信令进行信令黑名单控制，避免网络拥塞，化解信令风暴。 
应用场景 :###### 总述 
本特性是对终端用户的三种信令引发的风暴进行识别和抑制，如[图1]所示，包括附着请求信令风暴的识别和抑制、业务请求信令风暴的识别和抑制、PDN连接请求信令风暴的识别和抑制。
图1  信令风暴的识别和抑制

###### 频繁的信令请求引发的信令风暴识别 
因终端/用户问题（参数错误、中毒、恶意攻击网络）或传输中断、区域限制等原因，导致在一定时间内，终端的附着请求/业务请求/PDN连接请求信令，多到影响网络信令资源的处理能力，MME需要进行信令风暴识别。 
MME统计单个终端在统计周期内产生的信令数：附着、业务请求和PDN连接请求信令分开统计，当统计周期内的信令总数超过门限值，则将该用户放入信令黑名单，启动用户信令黑名单管理时长。 
###### 频繁的信令请求引发的信令风暴抑制 
因终端/用户问题（参数错误、中毒、恶意攻击网络）或传输中断、区域限制等原因，导致在一定时间内，终端的附着请求/业务请求/PDN连接请求信令，多到影响网络信令资源的处理能力，MME识别出附着请求/业务请求/PDN连接请求信令风暴，就需要进行信令风暴抑制，避免部分信令异常终端影响网络。 
在用户信令黑名单管理时间内，对附着请求和PDN连接请求信令异常的终端，有四种手段抑制信令： 
拒绝接入请求：对于附着请求，MME发送Attach Reject消息给UE，其中携带附着拒绝原因值7-EPS service
not allowed；对于PDN连接请求，MME发送PDN Connectivity Reject消息给UE，其中携带PDN连接拒绝原因值55-Multiple
PDN connections not allowed。 
建立Fake APN PDN连接：MME给SGW发送Create Session Request消息。 
强制去附着：MME发送Detach Request消息给UE，其中携带的detach type为re-attach not
required。 
丢弃后续请求：MME丢弃后续收到的Attach Request消息。 
在用户信令黑名单管理时间内，对业务请求信令异常的终端，有三种手段抑制信令： 
拒绝业务请求：MME发送Service Reject消息给UE，其中携带拒绝原因值7-EPS service not
allowed。 
强制去附着：MME发送Detach Request消息给UE，其中携带的detach type为re-attach not
required。 
丢弃后续请求：MME丢弃后续收到的Service Request消息。 
用户信令黑名单管理时长到达后，用户从信令黑名单移除，可以正常上网。 
客户收益 :受益方|受益描述
---|---
运营商|确保网络设备安全运行：减轻网络信令压力，化解信令风暴，避免网络拥塞。提高用户满意度：保障用户使用数据业务和业务的成功率，从而提高用户满意度，增加收益。提升运营商KPI指标：抑制终端频繁发起信令请求导致的业务失败，提升了业务成功率。
移动用户|用户享受更稳定和更可靠的网络服务。
实现原理 :系统架构 :系统架构如[图2]所示。
图2  系统架构

涉及的网元 :信令风暴抑制由MME和GW配合完成，具体参见[表1]。
网元|功能
---|---
MME|MME信令风暴抑制，具体包括附着请求信令风暴抑制、业务请求信令风暴抑制和PDN连接请求信令风暴抑制。MME在各信令的每个统计周期内统计各信令数，如果统计的信令数大于最大信令数，则MME将用户加入信令黑名单，并启动黑名单定时器。在信令黑名单定时器管理时间内，MME拒绝或丢弃信令；或MME建立FAKEAPN PDN连接，用户使用此PDN连接无法上网。信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。
SGW/PGW|SGW/PGW支持FAKE APN PDN连接建立，用户使用此PDN连接无法上网。
本网元实现 :附着信令风暴抑制MME在附着信令单位统计周期内统计附着信令数，如果统计的附着信令数大于最大信令数，则MME将用户加入附着信令黑名单，并启动附着黑名单定时器。在附着信令黑名单定时器管理时间内，UE不断发起附着，MME进行如下处理：拒绝接入请求。建立Fake APN PDN连接。强制去附着。丢弃后续请求。附着信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
业务请求信令风暴抑制MME在业务请求信令单位统计周期内统计业务请求信令数，如果统计的业务请求信令数大于最大信令数，则MME将用户加入业务请求信令黑名单，并启动业务请求黑名单定时器。在业务请求信令黑名单定时器管理时间内，UE不断发起业务请求，MME进行如下处理：拒绝业务请求。强制去附着。丢弃后续请求。业务请求信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
PDN连接请求信令风暴抑制MME在PDN连接信令单位统计周期内统计附着信令数，如果统计的PDN连接信令数大于最大信令数，则MME将用户加入PDN连接信令黑名单，并启动PDN连接信令黑名单定时器。在PDN连接信令黑名单定时器管理时间内，UE不断发起PDN连接请求，MME进行如下处理：拒绝接入请求。建立Fake APN PDN连接。强制去附着。丢弃后续请求。PDN连接信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
业务流程 :附着请求信令抑制
附着请求信令抑制流程参见[图3]。
图3  附着请求信令抑制流程

附着请求信令抑制流程描述如下： 
UE发起附着请求。MME针对每个UE进行统计，记录统计周期T1内收到该UE的附着请求信令数。 
MME因终端参数错误、区域限制等原因，给UE返回附着拒绝。 
UE重发附着请求。MME针对每个UE进行统计，记录统计周期T1内收到该UE的附着请求信令数。 
MME因终端参数错误、区域限制等原因，给UE返回附着拒绝。 
UE多次重发附着请求。MME针对每个UE进行统计，记录统计周期T1内收到该UE的附着请求信令数。 
当UE在统计周期内的信令数没超过门限值N1时，MME按照正常流程处理该用户信令。当UE在统计周期内的信令数超过门限值N1时，MME对该用户的异常信令进行控制：MME将该用户加入黑名单，并给终端下发Attach
Reject消息，消息中携带原因值为7-EPS service not allowed（原因值可配置），并启动黑名单定时器TT1。如果直到TT1超时仍未收到Attach
Request消息，则将用户从黑名单移除，正常处理后续消息。 
如果在TT1超时前，UE继续发送Attach Request消息，则进入步骤8。 
网络对用户进行鉴权，观察用户是否能鉴权成功。 
是→步骤9 
否→步骤15 
EPS网络以fake APN让终端建立PDN连接成功，MME发送Create
Session Request消息给SGW，消息中携带fake APN。 
SGW发送Create Session Request消息给PGW，消息中携带fake APN。 
PGW返回Create Session Response消息给SGW。 
SGW返回Create Session Response消息给MME。 
MME返回附着接受给UE。 
（可选）如果直到TT1超时仍未收到Attach Request消息，MME则将用户从黑名单移除，并给UE发送Detach
Request消息，其中detach type为re-attach required。UE re-attach时使用正常APN。 
（可选）如果鉴权失败或在TT1超时前UE继续发送Detach Request/Attach Request消息，MME则给UE发送Detach
Request消息，其中detach type为re-attach not required。 
（可选）如果直到TT1超时仍未收到Attach Request消息，则将用户从黑名单移除，正常处理后续消息。如果在TT1超时前继续收到UE发送的Attach
Request消息，MME丢弃该用户的附着请求信令，对这部分丢弃的信令单独统计，待黑名单TT1超时后，再将用户从黑名单移除。 
业务请求信令抑制
业务请求信令抑制流程参见[图4]。
图4  业务请求信令抑制流程

业务请求信令抑制流程描述如下： 
UE发起业务请求。MME针对每个UE进行统计，记录统计周期T2内收到该UE的Service Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回业务请求拒绝。 
UE重发业务请求。MME针对每个UE进行统计，记录统计周期T2内收到该UE的Service Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回业务请求拒绝。 
UE多次重发业务请求。MME针对每个UE进行统计，记录统计周期T2内收到该UE的Service Request信令数。 
当UE在统计周期内的信令数没超过门限值N2时，MME按照正常流程处理该用户信令。当UE在统计周期内的信令数超过门限值N2时，MME对该用户的异常信令进行控制：MME将该用户加入黑名单，并给终端下发Service
Reject消息，消息中携带原因值为7-EPS service not allowed（原因值可配置），并启动黑名单定时器TT2。如果直到TT2超时仍未收到Service
Request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT2超时前，UE继续发送Service Request消息，则进入步骤8。 
（可选）MME给UE发送Detach Request消息，其中detach type为re-attach not required。如果直到TT2超时仍未收到Attach
Request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT2超时前，UE继续发送Attach Request消息。MME丢弃该用户的附着请求信令，对这部分丢弃的信令单独统计，黑名单TT2超时后，再将用户从黑名单移除。 
PDN连接请求信令抑制
PDN连接请求信令抑制流程参见[图5]。
图5  PDN连接请求信令抑制流程

UE发起PDN连接请求。MME针对每个UE进行统计，记录统计周期T3内收到该UE的PDN Connectivity Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回PDN连接请求拒绝。 
UE重发PDN连接请求。MME针对每个UE进行统计，记录统计周期T3内收到该UE的PDN Connectivity Request信令数。 
MME因终端参数错误、区域限制等原因，给UE返回PDN连接请求拒绝。 
UE多次重发PDN连接请求。MME针对每个UE进行统计，记录统计周期T3内收到该UE的PDN Connectivity
Request信令数（不包含Attach流程中的PDN Connectivity Request）。 
当UE在统计周期内的信令数没超过门限值N3时，MME按照正常流程处理该用户信令。当UE在统计周期内的信令数超过门限值N3时，MME对该用户的异常信令进行控制：MME将该用户加入黑名单，并给终端下发PDN
Connectivity Reject消息，消息中携带原因值为55-Multiple PDN connections not allowed（原因值可配置），并启动黑名单定时器TT3。如果直到TT3超时仍未收到PDN
Connectivity Request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT3超时前，UE继续发送PDN Connectivity Request消息，则进入步骤8。 
EPS网络以fake APN让终端建立PDN连接成功，MME发送Create
Session Request消息给SGW，消息中携带fake APN。 
SGW发送Create Session Request消息给PGW，消息中携带fake APN。 
PGW返回Create Session Response消息给SGW。 
SGW返回Create Session Response消息给MME。 
MME返回PDN连接请求接受给UE。如果直到TT3超时仍未收到PDN Connectivity Request消息，MME则将用户从黑名单移除。UE再发起PDN Connectivity Request时使用正常APN。 
如果在TT3超时前，UE继续发送PDN Connectivity Request消息，MME给UE发送Detach Request消息，其中detach type为re-attach not required。如果直到TT3超时仍未收到Attach
request消息，则将用户从黑名单移除，正常处理后续消息。 
（可选）如果在TT3超时前，UE继续发送Attach Request消息。MME丢弃该用户的附着请求信令，对这部分丢弃的信令单独统计，黑名单TT3超时后，再将用户从黑名单移除。 
系统影响 :MME支持信令风暴抑制，减少了网络侧要处理的信令，信令抑制的功效是提高系统处理性能。 
应用限制 :该特性不涉及应用限制。 
特性交互 :特性|交互
---|---
紧急呼叫|如果附着请求、业务请求或PDN连接请求信令进入黑名单，MME对紧急呼叫放行，允许信令黑名单用户拨打紧急呼叫。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "GPRS enhancements for E-UTRAN access"|5.3.2节: Attach procedure5.3.4节: Service Request procedures5.10.2节: UE requested PDN connectivity
特性能力 :类型|能力
---|---
附着请求/业务请求/PDN连接请求信令统计周期|1-65535，单位：秒，默认值为。
附着请求/业务请求/PDN连接请求黑名单定时器时长|1-65535，单位：秒，默认值为。
黑名单用户容量|数量等同于MM上下文配置容量。
MME附着、业务请求和PDN连接请求信令统计的周期默认值都设置为12分钟，依据是24.301协议上对终端的要求是12分钟最多6次（5次重发），附着、业务请求和PDN连接请求黑名单定时器时长默认值都设置为20分钟，原则是比各信令统计周期略长，各信令单位时间内的信令门限的默认值设置原则参见下表。 
信令类型|信令统计周期|MME话务模型events/ peak SAU @BH（忙时每小时）|信令门限值
---|---|---|---
附着请求|12分钟|理论值：0.3现网经验值：0.2~0.4|话务模型中附着次数太小，24.301协议上对终端的要求是12分钟最多6次（5次重发），而附着成功建立的时长是毫秒级或秒级，因此设置为5的3倍，即15次。
业务请求|12分钟|理论值：6现网经验值：25左右|以现网经验值为准乘6的系数，即30次。
PDN连接请求|12分钟|无|考虑多PDN连接和IMS语音，比附着次数略小，即10次。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
V1.0|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持信令风暴抑制”（license ID：7036），此项目显示为“支持”，表示MME支持信令风暴抑制功能。
对其他网元的要求 :SGW/PGW需支持FAKE APN PDN连接建立，控制用户使用此PDN连接无法上网。 
工程规划要求 :Fake APN需要全网规划。 
O&M相关 :命令 :配置项表2  新增配置项配置项命令MME信令风暴相关配置SET SIGSRESTRAIN FLAGSHOW SIGSRESTRAIN FLAGSET SIGSRESTRAINDEL SIGSRESTRAIN FAKE APNSHOW SIGSRESTRAIN 
动态管理 在“动态管理”下增加“MME信令风暴抑制管理”，具体参见下表。表3  动态管理功能命令查询单用户信令状态SHOW SUBSCRIBER SIGSTATUS用户移出信令黑名单MOVE SUBSCRIBER BLACK查询信令黑名单用户SHOW BLACK SUBSCRIBER 
性能统计 :测量类型|描述
---|---
信令风暴抑制流程测量|编号为C46435开头的所有计数器
信令风暴抑制用户数测量|编号为C46436开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性涉及的业务观察/失败观察，参见下表。 
失败原因码及名称|相关模块|波及业务|产生原因
---|---|---|---
591-附着信令风暴拒绝|移动性管理模块EMM|附着|附着信令风暴抑制。
592-业务请求信令风暴拒绝|移动性管理模块EMM|业务请求|业务请求信令风暴抑制。
110-ESM处理失败|会话管理模块ESM|PDN连接请求|PDN连接请求信令风暴抑制。
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置信令风暴抑制功能，能够确保网络设备安全运行，减轻网络信令压力，化解信令风暴，避免网络拥塞。 
配置前提 :对于信令风暴抑制功能，ZTE根据经验，提供了各项门限的经验数据。但是各地网络均有其话务模型的独特性，需要运营商和ZTE预先评估各项黑名单门限预设值是否需要修改。用户还需要预先规划FAKE APN。 
已获取信令风暴抑制的LICENSE权限。 
配置过程 :执行命令[SET SIGSRESTRAIN FLAG]，打开“MME支持信令风暴抑制”功能开关。
执行命令[SET SIGSRESTRAIN]，根据全网规划配置Fake APN名称。
执行命令[ADD EPC APN]，配置本地APN解析。Fake APN建议通过本地配置进行解析，而不是通过DNS进行解析。
（可选）执行命令[SET SIGSRESTRAIN]，根据各地实际话务模型，调整MME支持信令风暴抑制功能的各项门限值。
 说明： 
MME支持信令风暴抑制功能的门限默认值能够适应大多数地区的话务模型，如果运营范围内话务模型特殊，可以根据当地情况，酌情调整。 
配置实例 :###### 异常附着信令，引起信令风暴 
场景说明
在此场景下，如果大量异常终端反复发起附着请求，引起网络信令风暴，影响正常终端的附着，则需要进行对附着请求信令进行抑制，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
设置MME是否支持信令风暴抑制配置|MME支持信令风暴抑制|支持
设置MME信令风暴抑制配置|附着请求信令统计周期(秒)|600
附着请求最大信令数|设置MME信令风暴抑制配置|20
附着拒绝原因值|设置MME信令风暴抑制配置|7
附着请求黑名单定时器时长(秒)|设置MME信令风暴抑制配置|300
配置步骤
步骤|说明|命令
---|---|---
1|启用MME支持信令风暴抑制。|SET SIGSRESTRAIN FLAG:FLAG="YES"
2|设置附着信令抑制策略。|SET SIGSRESTRAIN:ATTSTATISPERD=600,ATTMAXSIGNUM=20,ATTREJCAUSE=7,ATTBLACKLISTDUR=300
###### 异常业务请求信令，引起信令风暴 
场景说明
在此场景下，如果大量异常终端反复发起业务请求，引起网络信令风暴，则需要进行对业务请求信令进行抑制，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
设置MME是否支持信令风暴抑制配置|MME支持信令风暴抑制|支持
设置MME信令风暴抑制配置|业务请求信令统计周期(秒)|600
业务请求最大信令数|设置MME信令风暴抑制配置|40
业务请求拒绝原因值|设置MME信令风暴抑制配置|7
业务请求黑名单定时器时长(秒)|设置MME信令风暴抑制配置|300
配置步骤
步骤|说明|命令
---|---|---
1|启用MME支持信令风暴抑制。|SET SIGSRESTRAIN FLAG:FLAG="YES"
2|设置业务请求信令抑制策略。|SET SIGSRESTRAIN:SERVSTATISPERD=600,SERVMAXSIGNUM=40,SERVREJCAUSE=7,SERVBLACKLISTDUR=300
###### 异常PDN连接请求信令，引起信令风暴 
场景说明
在此场景下，如果大量异常终端反复发起PDN请求，引起网络信令风暴，则需要进行对PDN请求信令进行抑制，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
设置MME是否支持信令风暴抑制配置|MME支持信令风暴抑制|支持
设置MME信令风暴抑制配置|PDN连接请求信令统计周期(秒)|600
PDN连接请求最大信令数|设置MME信令风暴抑制配置|100
PDN连接拒绝原因值|设置MME信令风暴抑制配置|55
PDN连接请求黑名单定时器时长(秒)|设置MME信令风暴抑制配置|300
FAKE APN名称|设置MME信令风暴抑制配置|fake.apn.com
新增EPC APN HOST配置|APN名称|fake.apn.com.mnc003.mcc460.3gppnetwork.org
主机名|新增EPC APN HOST配置|xgw
IP地址|新增EPC APN HOST配置|1.1.1.1
支持服务类别|新增EPC APN HOST配置|x-3gpp-pgw
支持协议类型|新增EPC APN HOST配置|x-s5-gtp"&"x-s8-gtp
配置步骤
步骤|说明|命令
---|---|---
1|启用MME支持信令风暴抑制。|SET SIGSRESTRAIN FLAG:FLAG="YES"
2|设置PDN请求信令抑制策略。|SET SIGSRESTRAIN:PDNSTATISPERD=600,PDNMAXSIGNUM=100,PDNREJCAUSE=55,PDNBLACKLISTDUR=300,FAKEAPN="fake.apn.com"
3|设置FAKE APN的本地解析配置。|ADD EPC APN:APN="fake.apn.com.mnc003.mcc460.3gppnetwork.org",HOST="xgw",IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"&"x-s8-gtp"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|附着请求信令风暴抑制
---|---
测试目的|测试附着请求信令风暴抑制功能。
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME网元信令风暴抑制功能的license授权，并更新了license。
测试过程|开启信令风暴抑制功能开关，根据全网规划，配置Fake APN。修改“附着请求最大信令数”参数为2。打开信令跟踪。用户连续发起15次attach（15次附着请求在一个信令统计周期内）。等待12分钟后，查询用户黑名单状态。
通过准则|前两次attach成功。第三次attach失败，拒绝原因是“EPS  service  not allowed”，使用动态管理命令查询，用户被加入信令黑名单。第四次attach成功，网络侧以fake apn为用户建立PDN连接。第五次attach时，网络侧发起detach流程。detach成功。第六次attach时，用户消息被直接丢弃，不会触发后续流程。12分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|–
测试项目|业务请求信令风暴抑制
---|---
测试目的|测试业务请求信令风暴抑制功能.
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME网元信令风暴抑制功能的license授权，并更新了license。用户已经attach成功。
测试过程|开启信令风暴抑制功能开关，根据全网规划，配置Fake APN。修改“业务请求最大信令数”参数为2。打开信令跟踪。用户连续发起4次业务请求（4次业务请求在一个信令统计周期内）。用户发起attach。等待10分钟后，查询用户黑名单状态。
通过准则|前两次业务请求成功。第三次业务请求失败，拒绝原因是“EPS  service  not allowed”，使用动态管理命令查询，用户被加入信令黑名单。第四次业务请求时，网络侧发起detach流程。detach成功。用户attach时，用户消息被直接丢弃，不会触发后续流程。10分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|–
测试项目|PDN连接请求信令风暴抑制
---|---
测试目的|测试PDN连接请求信令风暴抑制功能。
预置条件|MME网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得MME网元信令风暴抑制功能的license授权，并更新了license。用户已经attach成功。
测试过程|开启信令风暴抑制功能开关，根据全网规划，配置Fake APN。修改“PDN连接请求最大信令数”参数为2。打开信令跟踪。用户连续发起5次PDN连接请求（5次业务请求在一个信令统计周期内）。用户发起attach。等待10分钟后，查询用户黑名单状态。
通过准则|前两次PDN连接请求成功。第三次PDN连接请求失败，拒绝原因是“Cause #55 – Multiple PDN connections for a given APN not allowed”，使用动态管理命令查询，用户被加入信令黑名单。第四次PDN连接请求时，网络侧以fake apn为用户建立PDN连接。第五次PDN连接请求时，网络侧发起detach流程。detach成功。用户attach时，用户消息被直接丢弃，不会触发后续流程。10分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|-
常见问题处理 :无 
## ZUF-78-20-006 动态流控 
特性描述 :特性描述 :描述 :定义 :过负荷控制功能指在设备处理的业务量超过了规定值时，需要采取保护措施以限制处理的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。 
动态流控功能是指MME周边网元（HSS、MSC/VLR、SGW/PGW）存在过载风险时，MME根据周边网元返回的响应消息，计算到周边网元的业务成功率，判断周边网元拥塞程度，再通过自动调节S1口接收的Attach、Inter TAU、Inter RAT  TAU处理速率，从而控制向周边网元放通的业务请求数，最终达到保护周边网元的目的，并保证用户以最大的速率接入网络。 
背景知识 :
拥塞和过负荷控制是保障网元运行安全的重要措施。EPC核心网在实际运行中，特定区域大批用户涌入引发的注册信令、频繁跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等造成单位时间业务量陡增，一旦出现过负荷，由于网络中不同类型的网元处理能力和资源各不相同，往往会出现由某个网元故障或宕机导致的全网瘫痪。因此为保障网络运行正常，需要从源头上对业务和用户实施控制，来完成整个网络的过负荷控制。 
随着网络部署越来越集中、网络应用越来越广泛，用户量在不断增加，MME各周边接口和网元拥塞的可能性也越来越大，经常会出现因为某些特定的原因导致用户短时间内暴发超过正常话务模型的业务，为了保证周边网元的安全，保证用户接通率和接续时长，改善用户体验，引入本特性（即动态流控功能）。 
应用场景 :动态流控功能应用于EPC网络运行中，当MME周边网元（HSS、MSC\VLR、SGW\PGW）发生拥塞时，通过自动调节S1侧的ATTACH、Inter TAU、Inter RAT TAU业务速率，减少到周边网元的信令，从而保护周边网元。 
动态流控场景示意图，如下图所示。 
应用场景包括： 
场景一：升级过程中系统重启升级过程中，大量用户重新附着，用户到周边网元的请求同时发起。动态流控可以预防周边S6a、S11、SGs接口网元发生拥塞和瘫痪。 
场景二：系统异常掉电重启系统异常掉电重启，突发大量业务，MME到周边网元请求消息数量也突增，会导致周边网元接口链路拥塞、网元过载，业务成功率明显下降。MME使用动态流控功能，动态降低S1口的业务放通率，减小信令拥塞对周边网元的影响。 
场景三：特定业务和用户的拥塞造成NAS短暂业务高峰拥塞随着物联网终端的广泛应用，大量的物联网终端接入EPS网络，对拥塞控制要求较高。由于物联网服务器故障、终端特殊应用、突发事件等会产生短时间内业务量急剧增加。物联网终端批量定时接入网络并传输数据，造成MME出现短时业务高峰。 
场景四：举办大型赛事、节假日、传输网中断等造成大量用户发起业务，对网络造成短暂的冲击此场景下，MME短时间内会接入超过估算话务模型的业务量，MME自身CPU占用率上升的同时，到周边网元的信令也会增加很多，会导致周边网元拥塞。 
场景五：网络运行中，周边网元能力因扩容增强时，可动态增加放通率，最大速率接入用户，减少用户接续时长此场景下，随着网络运行以及用户容量扩容，网元能力发生变化，动态流控可以动态监测周边网元能力，动态调整到周边网元的放通率，既保护周边网元，同时不影响用户的接入。 
场景六：网络部署时，同一地区部署多个HSS，MME接入多个HSS，在拥塞控制时区分局向进行控制此场景下，MME会接入多个HSS网元，在拥塞控制上需要分别进行控制，动态自动流控在S6a口可分局向控制，即可以区分不同HSS局向分别设置拥塞控制策略，单独控制。 
客户收益 :受益方|受益描述
---|---
运营商|通过动态流控，保障HSS网元的稳定性。提高UE整网接入成功率，减少周边网元的拥塞或过载瘫痪，提高网络的稳定性，从而提高用户满意度，增加收益。
移动用户|在大量突发业务冲击的场景下，减少因周边网元链路拥塞或过载而导致的用户不能使用业务的问题，动态提高周边网元拥塞时用户的接通率，更大程度的提高用户满意度，享受稳定可靠的网络服务。
实现原理 :系统架构 :系统架构如下图所示。 
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
MME|动态监测S6a、SGs、S11接口的业务成功率。根据周边网元接口成功率判断是否拥塞，启动动态流控。流控期间，根据周边网元业务成功率，动态调整Attach、Inter TAU、 RAT TAU业务的放通率。周边网元成功率超过门限，解除拥塞控制。
SGW/PGW|SGW/PGW设备发生拥塞时，返回失败的响应，MME动态监测SGW/PGW的业务成功率。
HSS|HSS设备发生拥塞时，返回失败的响应，MME动态监测HSS的业务成功率。
MSC/VLR|MSC/VLR设备发生拥塞时，返回失败的响应，MME动态监测MSC/VLR的业务成功率。
UE|接收MME的拒绝消息，启动back-off timer，超时前不发起业务。
协议栈 :MME与HSS之间的协议栈如下图所示。 
图2  S6a接口协议栈

MME与SGW之间的协议栈如下图所示。 
图3  S11接口协议栈

MME与MSC/VLR之间的协议栈如下图所示。 
图4  SGs接口协议栈

本网元实现 :动态流控原理
在系统升级重启、重大节日活动、容灾、周边网元故障等情况下，大量用户短时间内进行重新附着和跨局TAU，MME各周边接口网元的请求消息快速增加，可能会导致接口拥塞或周边网元设备过载。 
为了保证周边网元安全以及用户接入成功率和接续时长，通过动态流控功能，自动调节S1接口的Attach、Inter TAU、Inter
RAT TAU业务消息的接入速率，从而避免周边接口拥塞或网元过载。 
动态流控原理示意图如下图所示。 
动态流控原理说明如下： 
设置周边网元（HSS、SGW/PGW、MSC/VLR）负荷拥塞控制的启控初始门限和启控最大门限等参数。 
当MME接收到UE的Attach、Inter TAU、Inter RAT TAU业务消息的速率超过“启控初始门限”，动态流控系统监测周边网元的业务成功率，通常情况下，周边网元还未过载。 
当业务消息速率不断增加，超过“启控最大门限”时， 开始控制S1口业务消息速率，控制发往周边网元的业务请求消息。 
流控周期内，发现周边网元未过载，业务成功率高于设置的门限，动态根据步长增加Attach、Inter TAU、Inter
RAT TAU业务放通率。 
后续流控周期内，如果周边网元业务成功率依然高于设置的门限，则继续加大业务放通率，保证用户快速接入网络。 
当系统调整的接入速率超过周边网元的处理能力，检测到流控周期内周边网元业务成功率低于设置的门限，则向下调整业务放通率，
减少向相邻网元的业务量，保护周边网元。 
随着业务量下降，周边网元恢复正常，保持当前业务放通率。 
随着用户持续接入网络，Attach、Inter TAU、Inter RAT TAU业务速率持续下降，网络恢复正常，再等待保护时长后，解除本次拥塞流控。 
动态流控参数的设置
动态流控功能开启前需要计算设置 “触发拥塞的接入业务通过数量”、“初始限制的接入业务最大数量”、“允许通过的接入业务最大数量”。包括如下两种计算方法： 
根据实际用户数计算评估计算根据整个系统所有用户，在运营商期望的时间内全部接入的原则来计算动态流控的参数数据。初始限制的接入业务最大数量（启控最大门限） = 系统实际用户数 / 期望接入时长（秒） / 模块数量（SC）。触发拥塞的接入业务通过数量（启控初始门限） = 初始限制的接入业务最大数量 / 系数[1.5～2 ]允许通过的接入业务最大数量
= 初始限制的接入业务最大数量 × 系数[1.2~1.5]说明：这里的用户数指的是注册在MME下的用户数，不包括2G、3G用户。举例：系统4G用户数为100万，需要在15分钟内接入，部署50个CMP，各参数设置如下：初始限制的接入业务最大数量（启控最大门限）
= 100 万/ 900 / 50 = 22 个/秒 。触发拥塞的接入业务通过数量（启控初始门限） = 22 / [1.5～2
] = [11～15] 个/秒允许通过的接入业务最大数量 = 22× [1.2~1.5] = [26~33] 个/秒 
根据周边网元能力评估计算已知周边网元处理能力时，需要评估DRA/HSS、SGW/PGW、MSC网元中处理能力最弱的网元，并根据此网元能力来设置拥塞控制参数。初始限制的接入业务最大数量（启控最大门限） = 最弱的周边网元最大处理能力 × 波动系数（1.1） / 模块数量（SC）。触发拥塞的接入业务通过数量（启控初始门限） = 初始限制的接入业务最大数量 / 系数[1.5～2 ]允许通过的接入业务最大数量
= 初始限制的接入业务最大数量 ×系数 [1.2~1.5]举例：周边网元DRA/HSS能力最弱，映射到UE附着、Inter
TAU处理速率为3000 caps。MME部署了100个CMP模块。初始限制的接入业务最大数量（启控最大门限） = 3000
caps × 1.1 / 100 = 33 个/秒 。触发拥塞的接入业务通过数量（启控初始门限） = 33 / [1.5～2
] = [16～22] 个/秒 。允许通过的接入业务最大数量 = 33 × [1.2~1.5] = [39～50] 个/秒
。 
评判控制周期内流控策略
在动态流控启动后，在控制周期内，采用令牌桶方式进行消息流控。根据如下策略进行控制： 
设置令牌控制周期为评判周期的1/3，令牌投放周期为流控控制周期。 
根据控制周期内的业务放通率和令牌控制周期，计算出总的令牌数。 
系统按照固定的令牌投放周期，定期往桶内投放固定的令牌数量。 
为解决业务速率不均衡问题，根据需要，设置业务速率突发倍数，令牌桶内无令牌时，根据突发倍数，增加令牌投放， 最大程度的放通业务。 
令牌桶流控示意图如下图： 

业务流程 :动态流控流程
动态流控流程如下图所示。 
流程说明： 
由于系统升级或异常重启、重大节日、物联网用户集中触发业务等场景，导致大量用户发起Attach或Inter TAU。 
MME收到大量Attach、Inter TAU、Inter RAT TAU业务请求，业务速率达到动态流控的启控初始门限，开始判断周边网元的处理能力，处理如下： 
周边网元业务成功率低于门限，开始动态流控，限制部分用户接入，防止周边网元拥塞过载。 
周边网元业务成功率高于门限，不限制用户接入，随着业务量上升，超过系统允许的启控最大门限，则开始限制超过门限的用户接入，将业务放通率控制在一定范围之内，防止周边网元拥塞。 
对于被限制接入的附着或TAU业务请求，系统根据配置策略选择丢弃或拒绝，拒绝业务时，向UE返回Attach Reject或TAU
Reject消息，并携带失败原因值：“#22 Congestion”，携带Back-off Timer。 
通过动态流控，控制系统业务的放通率， 在保护周边网元的同时，最大程度的放通业务，使得用户快速的接入网络，提高用户体验。 
系统处理Attach和TAU的后续流程，如果UE通过GUTI进行附着或TAU，处理如下： 
附着流程：附着的MME与上次Detach时的MME不同，则通过GUTI获取old MME/SGSN的地址，向old MME/SGSN发送Identification
Request消息获取用户的IMSI。如果获取不到则向手机侧获取IMSI。 
TAU流程：new MME向old MME发送Context Request消息获取上下文，old MME返回Context
Response。 
系统完成附着或TAU的后续业务流程，MME统计周边网元（HSS、SGW\PGW、MSC\VLR）接口的业务成功率。 
MME向UE发送Attach、Inter TAU接受消息，用户接入成功。 
S6a口分局向流控流程
根据部署场景， MME会接入多个HSS，因此MME在动态流控时，需要S6a口分局向动态流控。 
S6a口分局向动态流控流程如下图所示。 
流程说明： 
系统开启S6a口分局动态流控，由于MME系统升级或异常重启、重大节日、物联网用户集中触发业务等场景，导致大量用户发起Attach或Inter
TAU。 
MME收到大量Attach、Inter TAU、Inter RAT TAU业务请求，先获取用户的IMSI，附着流程和TAU流程的处理如下： 
附着流程：附着的MME与上次Detach时的MME不同，则通过GUTI获取old MME/SGSN的地址，向old MME/SGSN发送Identification
Request消息获取用户的IMSI。如果获取不到则向手机侧获取IMSI。 
TAU流程：new MME向old MME发送Context Request消息获取上下文，old MME返回Context
Response。 
获取到用户IMSI，根据IMSI查询S6a口动态流控策略配置。如果用户不在配置中，则不进行控制。如果用户在S6a口动态流控配置中，则根据S6a口动态流控策略判断当前用户是否被限制，处理如下： 
HSS1网元发生拥塞，处理成功率低于门限，并且业务速率达到HSS1的启控初始门限，则进行HSS1局向的动态流控，限制部分用户接入HSS1，防止HSS1网元拥塞过载。 
HSS2网元运行正常，周边网元业务成功率高于门限，则不进行HSS2局向的动态流控。 
对于HSS1局向动态流控限制接入的附着或TAU业务请求，系统根据配置策略选择丢弃或拒绝，拒绝业务时，向UE返回Attach
Reject或TAU Reject消息，并携带失败原因值：“#22 Congestion”，携带Back-off Timer。 
S6a局向HSS1发生拥塞，S6a局向动态流控系统控制业务的放通率， 在保护HSS1网元的同时，最大程度的放通业务，使得用户快速的接入网络，提高用户体验。 
系统完成附着或TAU的后续业务流程，MME统计HSS1网元的业务成功率。 
MME向归属于HSS1网元的UE发送Attach、Inter TAU接受消息，用户接入成功。 
HSS2网元运行正常，没有拥塞，同时到HSS2网元的业务速率未超过启控最大门限，S6a分局向动态流控系统不对用户进行控制，归属于HSS2的用户完成附着或TAU的后续业务流程，同时MME统计HSS2网元的业务成功率。 
MME向归属于HSS2网元的UE发送Attach、Inter TAU接受消息，用户接入成功。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :当通常周边网元设备与多个MME相连，保护该周边网元需要所有的MME开启动态流控功能， 否则达不到保护周边网元的目的。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :该特性不涉及标准内容。 
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.20|首次发布。
License要求 :该特性为ZXUN uMAC产品的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|-|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :动态流控功能中，S6a动态流控默认开启，S11动态流控、SGS动态流控、S6a口分局向动态流控根据现网需求开启，可分别设置控制策略参数。 
流控参数的设置策略，参见实现原理中的[动态流控参数的设置]。
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME自动业务控制基本参数SET MME AUTOCTL BASIC PARASHOW MME AUTOCTL BASIC PARAS6a统一ALC流控策略SET MME AUTO CNGCTLSHOW MME AUTO CNGCTLS11统一ALC流控策略SET S11 ALCPLYSHOW S11 ALCPLYSGS统一ALC流控策略SET SGS ALCPLYSHOW SGS ALCPLYS6a ALC局向流控策略配置ADD S6A ALCOFC POLICYSET S6A ALCOFC POLICYDEL S6A ALCOFC POLICYSHOW S6A ALCOFC POLICYS6a ALC局向IMSI号段配置ADD S6A ALCOFC IMSICFGSET S6A ALCOFC IMSICFGDEL S6A ALCOFC IMSICFGSHOW S6A ALCOFC IMSICFG 
动态管理表2  新增动态命令动态管理名称命令查询MME自动过负荷信息SHOW MME AUTO CNG INFO查询S6a ALC局向负荷控制信息SHOW S6A ALCOFC CNG INFOMME自动过负荷日志上报START MME AUTO CNG LOGRPT停止MME自动过负荷日志上报STOP MME AUTO CNG LOGRPT 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置过程可以完成MME动态流控功能，当MME周边网元（HSS、MSC\VLR、SGW\PGW）发生拥塞或者在特定HSS处理能力比较弱时，通过自动调节S1侧的ATTACH、Inter TAU、Inter RAT TAU业务速率，减少到周边网元的信令，从而达到保护周边网元的目的。 
通过该配置使动态ALC在控制上更加合理、控制过程可视化便于分析、尽可能避免误告警。 
配置前提 :EPC网络运行正常，与周边网元（HSS、MSC\VLR、SGW\PGW）通信正常。 
配置过程 :执行命令[SET MME AUTOCTL BASIC PARA]，设置MME自动业务控制基本参数，包括：控制周期、评判周期以及当拥塞控制时是否上报日志等。
执行命令[SET MME AUTO CNGCTL]，设置S6a口局向统一ALC业务流控策略，包括：是否开启控制功能，限制接入业务量、触发拥塞的业务成功率等。
执行命令[SET S11 ALCPLY]，设置S11口局向统一ALC业务流控策略，包括：是否开启控制功能，限制接入业务量、触发拥塞的业务成功率等。
执行命令[SET SGS ALCPLY]，设置SGs口局向统一ALC业务流控策略，包括：是否开启控制功能，限制接入业务量、触发拥塞的业务成功率等。
执行命令[ADD S6A ALCOFC POLICY]，新增S6a接口ALC局向流控策略配置，包括：局向索引，局向名称，是否开启控制功能，限制业务量以及触发拥塞的业务成功率等。
可以通过[SET S6A ALCOFC POLICY]/[DEL S6A ALCOFC POLICY]命令进行配置的修改/删除。
执行命令[ADD S6A ALCOFC IMSICFG]，新增S6a接口ALC局向关联的IMSI号段。
可以通过[SET S6A ALCOFC IMSICFG]/[DEL S6A ALCOFC IMSICFG]命令进行配置的修改/删除。
配置实例 :###### 配置实例一 
场景说明
升级、系统异常重启或者大型赛事、节假日等场景大量用户发起业务，对网络造成短暂冲击。 
数据规划
配置项|参数|取值
---|---|---
设置MME自动业务控制基本参数|业务控制周期(100ms)|10
评判周期(s)|设置MME自动业务控制基本参数|3
拥塞控制时是否上报日志|设置MME自动业务控制基本参数|NO
hss成功率统计包含NOR/NOA|设置MME自动业务控制基本参数|NO
hss成功率统计包含PUR/PUA|设置MME自动业务控制基本参数|NO
周边网元无过载成功率（%）|设置MME自动业务控制基本参数|95
临过载时向上步长缩减比例（%）|设置MME自动业务控制基本参数|60
允许业务突发系数（%）|设置MME自动业务控制基本参数|150
设置S6a统一ALC流控策略|是否开启|YES
触发拥塞的接入业务通过数量(单模块每秒)|设置S6a统一ALC流控策略|20
初始限制的接入业务最大数量(单模块每秒)|设置S6a统一ALC流控策略|50
允许通过的接入业务最大数量(单模块每秒)|设置S6a统一ALC流控策略|300
触发拥塞的业务成功率(%)|设置S6a统一ALC流控策略|85
接入业务控制步长|设置S6a统一ALC流控策略|5
控制持续时间(分钟)|设置S6a统一ALC流控策略|5
设置S11统一ALC流控策略|是否开启|YES
触发拥塞的接入业务通过数量(单模块每秒)|设置S11统一ALC流控策略|20
初始限制的接入业务最大数量(单模块每秒)|设置S11统一ALC流控策略|50
允许通过的接入业务最大数量(单模块每秒)|设置S11统一ALC流控策略|300
触发拥塞的业务成功率(%)|设置S11统一ALC流控策略|85
接入业务控制步长|设置S11统一ALC流控策略|5
控制持续时间(分钟)|设置S11统一ALC流控策略|5
设置SGS统一ALC流控策略|是否开启|YES
触发拥塞的接入业务通过数量(单模块每秒)|设置SGS统一ALC流控策略|20
初始限制的接入业务最大数量(单模块每秒)|设置SGS统一ALC流控策略|50
允许通过的接入业务最大数量(单模块每秒)|设置SGS统一ALC流控策略|300
触发拥塞的业务成功率(%)|设置SGS统一ALC流控策略|85
接入业务控制步长|设置SGS统一ALC流控策略|5
控制持续时间(分钟)|设置SGS统一ALC流控策略|5
配置步骤
步骤|说明|操作
---|---|---
1|设置MME自动业务控制基本参数。|SET MME AUTOCTL BASIC PARA:CTRLTIMER=10,JUDGETIMER=3,ISLOG="NO",HSSSUCCRATEWITHNOR="NO",HSSSUCCRATEWITHPUR="NO",SUCCRATENOCON=95,REDUCRATECLOSETOCON=60,TOKENBKTRADIO=150
2|设置S6a统一ALC流控策略|SET MME AUTO CNGCTL:FLG="YES",STARTCAPS=20,LIMTCAPS=50,MAXCAPS=300,SUCCRATE=85,STEP=5,LASTTIME=5
3|设置S11统一ALC流控策略|SET S11 ALCPLY:FLG="YES",STARTCAPS=20,LIMTCAPS=50,MAXCAPS=300,SUCCRATE=85,STEP=5,LASTTIME=5
4|设置SGS统一ALC流控策略|SET SGS ALCPLY:FLG="YES",STARTCAPS=20,LIMTCAPS=50,MAXCAPS=300,SUCCRATE=85,STEP=5,LASTTIME=5
###### 配置实例2 
场景说明
同一地区部署多个HSS，MME接入多个HSS，区分局向进行拥塞控制。 
数据规划
配置项|参数|取值
---|---|---
设置MME自动业务控制基本参数|业务控制周期(100ms)|10
评判周期(s)|设置MME自动业务控制基本参数|3
拥塞控制时是否上报日志|设置MME自动业务控制基本参数|NO
hss成功率统计包含NOR/NOA|设置MME自动业务控制基本参数|NO
hss成功率统计包含PUR/PUA|设置MME自动业务控制基本参数|NO
周边网元无过载成功率（%）|设置MME自动业务控制基本参数|95
临过载时向上步长缩减比例（%）|设置MME自动业务控制基本参数|100
允许业务突发系数（%）|设置MME自动业务控制基本参数|100
新增S6a ALC局向流控策略配置|局向索引|1
局向名称|新增S6a ALC局向流控策略配置|HSS_OFC1
是否开启|新增S6a ALC局向流控策略配置|YES
触发拥塞的接入业务通过数量(单模块每秒)|新增S6a ALC局向流控策略配置|20
初始限制的接入业务最大数量(单模块每秒)|新增S6a ALC局向流控策略配置|50
允许通过的接入业务最大数量(单模块每秒)|新增S6a ALC局向流控策略配置|300
触发拥塞的业务成功率(%)|新增S6a ALC局向流控策略配置|85
接入业务控制步长|新增S6a ALC局向流控策略配置|5
控制持续时间(分钟)|新增S6a ALC局向流控策略配置|5
新增S6a ALC局向IMSI号段配置|IMSI|460119990020xxx460119990021xxx
局向索引|新增S6a ALC局向IMSI号段配置|1
配置步骤
步骤|说明|操作
---|---|---
1|设置MME自动业务控制基本参数|SET MME AUTOCTL BASIC PARA:CTRLTIMER=10,JUDGETIMER=3,ISLOG="NO",HSSSUCCRATEWITHNOR="NO",HSSSUCCRATEWITHPUR="NO",SUCCRATENOCON=95,REDUCRATECLOSETOCON=100,TOKENBKTRADIO=100
2|新增S6a ALC局向流控策略配置|ADD S6A ALCOFC POLICY:OFCIDX=1,OFCNAME="HSS_OFC1",OFCAUTOCTLSWITCH="YES",STARTCAPS=20,LIMTCAPS=50,MAXCAPS=300,SUCCRATE=85,STEP=5,LASTTIME=5
3|新增S6a ALC局向IMSI号段配置|ADD S6A ALCOFC IMSICFG:IMSI="460119990020",OFCIDX=1ADD S6A ALCOFC IMSICFG:IMSI="460119990021",OFCIDX=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|S6a统一ALC流控基本功能验证
---|---
测试目的|验证S6a统一ALC功能机制正常运作，动态管理命令显示内容正确。
预置条件|EPC系统运行正常。MME自动业务控制基本参数配置中，将“临过载时向上步长缩减比例”以及“允许业务突发系数”均设置成100%。S6a统一ALC流控策略中，S6a统一ALC流控功能开启，其余配置保持默认。S11统一ALC流控功能关闭，SGs统一ALC流控功能关闭。
测试过程|批量4G用户发起EPC附着，初始速率保持70单模块每秒，HSS业务成功率保持大于95%。2分钟后降低用户附着速率保持30每模块每秒，HSS业务成功率依然大于95%。观察告警信息以及使用动态命令SHOW MME AUTO CNG INFO查看控制过程。
通过准则|初始允许接入数量被控制到50每模块每秒，部分用户附着失败，1分钟后经过4次调整，所有用户均能够通过，没有业务失败。查看告警信息有产生“业务过负荷告警”，其中过负荷原因为MME S6a自动过负荷。6分钟后退出控制状态，告警正常消除。动态命令数据记录准确。
测试结果|–
测试项目|S11统一ALC流控基本功能验证
---|---
测试目的|验证S11统一ALC功能机制正常运作，动态管理命令显示内容正确。
预置条件|EPC系统运行正常。MME自动业务控制基本参数配置中，将“临过载时向上步长缩减比例”以及“允许业务突发系数”均设置成100%。S11统一ALC流控策略中，S11统一ALC流控功能开启，其余配置保持默认。S6a统一ALC流控功能关闭，SGs统一ALC流控功能关闭。
测试过程|批量4G用户发起EPC附着，初始速率保持70单模块每秒，SGW业务成功率保持大于95%。2分钟后降低用户附着速率保持30每模块每秒，SGW业务成功率依然大于95%。观察告警信息以及使用动态命令SHOW MME AUTO CNG INFO查看控制过程。
通过准则|初始允许接入数量被控制到50每模块每秒，部分用户附着失败，1分钟后经过4次调整，所有用户均能够通过，没有业务失败。查看告警信息有产生“业务过负荷告警”，其中过负荷原因为MME S11自动过负荷。6分钟后退出控制状态，告警正常消除。动态命令数据记录准确。
测试结果|–
测试项目|SGs统一ALC流控基本功能验证
---|---
测试目的|验证SGs统一ALC功能机制正常运作，动态管理命令显示内容正确。
预置条件|EPC系统运行正常。MME自动业务控制基本参数配置中，将“临过载时向上步长缩减比例”以及“允许业务突发系数”均设置成100%。SGs统一ALC流控策略中，SGs统一ALC流控功能开启，其余配置保持默认。S6a统一ALC流控功能关闭，S11统一ALC流控功能关闭。
测试过程|批量4G用户发起联合附着，初始速率保持70单模块每秒，MSC/VLR业务成功率保持大于95%。2分钟后降低用户附着速率保持30每模块每秒，MSC/VLR业务成功率依然大于95%。观察告警信息以及使用动态命令SHOW MME AUTO CNG INFO查看控制过程。
通过准则|初始允许接入数量被控制到50每模块每秒，部分用户附着失败，1分钟后经过4次调整，所有用户均能够通过，没有业务失败。查看告警信息有产生“业务过负荷告警”，其中过负荷原因为MME SGs自动过负荷。6分钟后退出控制状态，告警正常消除。动态命令数据记录准确。
测试结果|–
测试项目|统一ALC流控优化基本功能验证
---|---
测试目的|验证统一ALC流控优化基本功能生效。
预置条件|EPC系统运行正常。MME自动业务控制基本参数配置中评判周期为3秒，允许业务突发系数为150%。S6a统一ALC流控策略中，S6a统一ALC流控功能开启，其余配置保持默认。S11统一ALC流控功能关闭，SGs统一ALC流控功能关闭。
测试过程|批量4G用户EPC附着，初始速率保持低于50单模块每秒（例如：40单模块每秒），HSS业务成功率保持大于95%。系统运行过程中，突然增加业务量到70单模块每秒，持续时长2秒，后降低业务速率低于50单模块每秒，HSS业务成功率继续保持大于95%。
通过准则|业务量短暂增加，但因为设置了允许业务突发，且持续时间短，没有业务失败。
测试结果|–
测试项目|S6a ALC局向流控基本功能验证
---|---
测试目的|验证S6a局向流控功能机制正常运作，动态管理命令显示内容正确，动态命令查询MME自动过负荷日志上报成功。
预置条件|EPC系统运行正常，并且配置多个HSS与MME相连。MME自动业务控制基本参数配置中，将“临过载时向上步长缩减比例”以及“允许业务突发系数”均设置成100%。S6a统一ALC流控功能关闭。S6a ALC局向流控策略配置中新增局向索引为“1”，局向名称为“HSS_OFC1”，流控开关是否开启为“是”，其余保持默认的配置记录。S6a ALC局向IMSI号段配置中新增IMSI号段为“46011”，局向索引为“1”的配置（即假设46011对应的HSS需要被流控）。支持系统日志上报功能。
测试过程|IMSI号段为“46011”以及“46003”的批量用户同时发起4G EPC附着，初始速率都保持70单模块每秒，对接的HSS业务成功率保持大于95%。2分钟后降低46011号段用户附着速率保持30每模块每秒，HSS业务成功率依然大于95%。观察告警信息以及使用动态命令SHOW S6A ALCOFC CNG INFO查看控制过程。执行命令START MME AUTO CNG LOGRPT:LOGTIME=2，上报过负荷日志。
通过准则|对于IMSI号段为“46011”的用户，系统判断初始速率(70)大于“初始限制的接入业务最大数量” 50时，允许接入数量被控制到50每模块每秒，部分用户附着失败。IMSI号段为“46003”的用户不受限制，业务全部通过。1分钟后，经过4次调整，IMSI号段为“46011”的用户也没有业务被控制，所有用户附着均成功。查看告警信息有产生"业务过负荷告警"，其中过负荷原因为MME S6a自动过负荷并且显示控制的局向名称“HSS_OFC1”。6分钟后退出控制状态，告警正常消除。动态命令查询数据正确，日志内容记录准确。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## AIR 
Authentication-Information-Request鉴权信息检索请求
## M2M 
Machine to Machine机器对机器
## NOR 
Notify-Request通知请求
## OC 
Overload Control过负荷控制
## OLR 
Organic Loading Rate有机负荷率
## PUR 
Purge-UE-RequestPurge UE请求
## ULR 
Update-Location-Request位置更新请求
