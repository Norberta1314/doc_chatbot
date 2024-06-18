# 概述 
## 功能描述 
安全管理功能解决了系统和用户的安全问题，包括： 
用户身份合法性校验，防止非法用户接入网络，也防止用户接入非法网络。 
终端设备合法性校验，拒绝非法设备接入网络。 
用户号码保护，尽量减少用户IMSI、IMEI等信息在空口的传递。 
用户数据完整性保护。 
用户信令或数据的私密性保护。 
跨系统移动时，安全上下文转换。 
## 功能特性简介 
MME提供的安全解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
鉴权|用户接入通信网络，首先需要通过鉴权来确认身份合法。整个鉴权过程既包含了网络对于用户的鉴权，也包含了用户对于网络的鉴权。MME支持按号段以及业务场景配置鉴权策略，比如支持配置IMSI附着鉴权策略为强制鉴权、不鉴权、系统判断、按频次鉴权。|ZUF-78-04-001 鉴权
二次鉴权|若UE鉴权失败且失败原因值为"synch failure"，则MME会直接重新触发鉴权。若NAS请求消息中携带GUTI，当UE鉴权失败且失败原因值为"MAC failure"或"non-EPS authentication unacceptable"时，则MME首先向UE请求用户标识，然后检查UE返回的用户标识与上下文中保存的用户标识是否一致，若不一致则重新触发鉴权。|ZUF-78-04-002 二次鉴权
NAS层加密|NAS层加密用于保护NAS消息不被攻击者获取，支持下行NAS消息的加密和上行NAS消息的解密。支持的加密算法如下：EEA0（空算法，未加密）EEA1（SNOW 3G算法）EEA2（AES算法）EEA3（ZUC算法）根据UE携带上来的安全能力以及本地配置的安全能力，MME协商NAS加密算法，并通过Security Mode Command过程通知到UE。|ZUF-78-04-003 NAS层加密
NAS层完整性保护|根据UE携带上来的安全能力以及本地配置的安全能力，MME协商NAS完整性保护算法，并通过Security Mode Command过程通知到UE。无卡用户或者用户认证失败，执行紧急业务时，协商的完整性保护算法只能为EIA0。|ZUF-78-04-004 NAS层完整性保护
AS层安全模式过程|AS层安全模式命令过程用于RRC级安全。当用户从空闲态转连接态时，MME根据初始密钥KASME以及上行NAS COUNT消息生成KeNB秘钥，并根据KeNB推演临时参数NH（Next Hop），并将NCC设置为1。随后在Initial Context Setup Request消息中，将生成的KeNB以及用户安全能力携带给RAN侧。S1切换过程中，MME推导新的NH，并将NCC加1。随后在Handover Request消息中携带新生成的NH和NCC，以及UE安全能力。X2切换过程中，MME推导新的NH，并将NCC加1。随后在Path Switch Acknowledge消息中携带新生成的NH和NCC。|ZUF-78-04-005 AS层安全模式过程
GUTI重分配|用户永久标识IMSI，涉及到用户隐私和安全性。为了减少IMSI在空口的传输，引入临时标识GUTI。用户附着时，MME分配一个全球唯一的临时标识GUTI给UE。后续UE使用该临时标识，与网络侧进行业务。MME通过本地配置，决策临时标识分配策略，比如周期性跟踪区更新时是否分配GUTI等。|ZUF-78-04-006 GUTI重分配
IMEI检查|IMEI检查用于检查用户设备是否合法。MME通过S13接口将设备号发送给EIR，由后者进行设备检查并返回结果。若检查结果显示该设别在灰名单或黑名单内，则设备所有人或被警告或被禁止接入网络。|ZUF-78-04-007 IMEI检查
ADD|ADD是指MME把UE终端的IMEISV信息带给HSS，HSS根据IMEISV来检测终端。开启ADD功能后，MME首先向UE请求IMEISV，获取IMEISV成功后，将该IMEISV通知给HSS。|ZUF-78-04-008 ADD
USIM卡安全密钥转换|在2/3G与4G互操作过程中，MME支持将EPS安全上下文映射为UMTS安全上下文，或者将UMTS安全上下文映射为EPS安全上下文。|ZUF-78-04-009 USIM卡安全密钥转换
# ZUF-78-04-001 鉴权 
## 特性描述 
## 特性描述 
### 术语 
无。 
### 描述 
##### 定义 
随着移动通信的普及，移动通信中的安全问题正受到越来越多的关注，人们对移动通信中的信息安全也提出了更高的要求，在LTE网络中，3GPP组织为LTE网络定义了网络安全架构，为用户提供安全可靠的服务，防止用户相关数据被窃听和篡改。 
##### 背景知识 
GPRS网络在GPRS网络（2G）中，网络侧对用户鉴权防止未经授权的接入。但GPRS网络存在一些安全隐患，如使用的128bit的密钥容易被破解，不支持数据的完整性保护，难以发现数据被篡改，用户无法对网络进行鉴权。 
UMTS网络UMTS网络（3G）在GPRS网络的基础上进行了改进，采用基于Milenage算法的AKA鉴权，实现了终端和网络间的双向认证，定义了强制的完整性保护和可选的加密保护，提供了更好的安全性保护。 
LTE网络LTE网络（4G）采用UMTS网络相同的安全架构，也使用AKA鉴权算法，也支持对数据的完整性保护和加密，但信令的完整性保护和加密由MME完成，减少eNodeB网元的处理工作。相对于2/3G网络安全，LTE网络安全的区别如下表：表1  LTE网络与2/3G网络的安全机制区别项目2G3G4G鉴权算法A3AKAAKA鉴权向量三元组RAND、SRES、Kc 五元组RAND, XRES, AUTN, CK, IK 四元组 RAND, XRES, AUTN, Kasme 密钥Kc CK、IK Kasme 用户临时标识TTLI（等同于PTMSI） PTMSI GUTI 支持卡类型支持SIM/USIM卡 支持SIM/USIM卡仅支持USIM卡 NAS完保无完保 RNC完保 MME完保 完保算法 无 UIA0(不加密),UIA1, (Kasumi),UIA2(SNOW 3G) EIA0(不加密),EIA1 (SNOW 3G),EIA2 (AES) 完保密钥 无 IK由SGSN在SMC消息发送给RNC Knasint由MME通过Kasme生成 NAS加密 SGSN加密 RNC加密 MME加密 加密算法GEA0(不加密),GEA1(R12后废弃，不推荐),GEA2,GEA3,GEA4(128位加密算法,必须使用UMTS安全上下文,根据CK及IK生成)UEA0(不加密),UEA1, (Kasumi),UEA2(SNOW 3G) EEA0(不加密),EEA1 (SNOW 3G),EEA2 (AES) 加密密钥 Kc/Kc128，Kc128由IK和CK生成 CK由SGSN在SMC消息发送给RNC Knasenc由MME通过Kasme生成。 媒体报文加密SGSN进行解密 RNC进行解密 eNodeB进行解密 是否启动鉴权通过比较CKSN一致，可不启动鉴权。 KSI一致和PTMSI-signature校验成功可不启动鉴权 eKSI一致和NAS Token校验成功可不启动鉴权  
### 应用场景 
MME启用对用户鉴权MME网元为用户提供鉴权服务，按照不同业务选择不同的鉴权策略。在设定通用鉴权策略基础上，如需对某些用户提供不同的安全策略，可再基于IMSI号段为其配置专门的鉴权策略。MME可按照下面的业务种类来选择鉴权策略：业务详细分类附着IMSI附着局内GUTI附着RAT内局间GUTI附着跨RAT局间GUTI附着TAU局内EPS TAU局内周期TAURAT内局间TAU跨RAT局间TAU局内切换后TAURAT内切换后局间TAU跨RAT切换后局间TAU业务请求业务请求分离分离鉴权策略可分为：鉴权策略详细描述强制鉴权慎重使用该选项，该鉴权类型会导致对应业务类型流程每执行一次就触发一次鉴权，当用户业务类型流量较大时，会加重网络负担。强制不鉴权鉴于EPC网络非常强调网络安全和用户隐私保护，在商用局中不推荐使用“强制不鉴权”选项。系统判断MME检测到UE和MME之间没有安全环境或安全环境被破坏，则MME自动触发对UE鉴权，以建立新的安全环境，保障后续的信令消息在可靠的安全环境中传输。可以理解“系统判断”是在“需要”时鉴权，不“需要”时不鉴权。频次鉴权该鉴权类型是对“系统判断”类型的补充。频次鉴权是基于流程的，即流程每被执行N次，就触发一次鉴权。如果有一组用户执行同一个业务类型流程，那么发生在每个用户身上的鉴权概率是不均等的。单用户频次鉴权该鉴权类型是对“系统判断”类型的补充。另外，具有频次鉴权类型的一切优点，是针对用户级别的。其避免了频次鉴权对用户鉴权不均匀，即每个用户每执行N次该业务类型流程，就对该用户进行一次鉴权。 
MME对NAS消息进行完整性保护和加密如需支持对NAS消息进行完整性保护和加密，需启动对用户鉴权后，按照下面方式对于MME支持完整性保护和加密算法设置。完整性保护算法是否支持级别EIA3不支持(一般UE终端都不支持)N/AEIA2支持2（高）EIA1支持1（低）EEA3不支持(一般UE终端都不支持)N/AEEA2支持2（高）EEA1支持1（中）EEA0支持（实际为不进行加密）0（低） 
MME启用对用户IMEI检查IMEI检查的作用是用于检查终端设备是否合法，目前一般情况并不启用。启用IMEI检查分为两种场景：对所有用户IMEI检查。只对一些特定号段的IMSI进行IMEI检查。具体选择哪种需基于现场实际需求来定。 
MME为用户分配GUTI用户进行附着或TAU业务，MME为用户分配临时标识GUTI，用户保存下来，在下次业务使用此GUTI作为用户标识。 
MME启用4G到2G重定向安全保护MME支持按TA粒度控制UE是否对到GERAN的重定向消息进行完整性保护，如果进行完整性保护，UE对重定向到GERAN的命令进行完整性保护校验，校验成功后才可以向GERAN重定向，校验失败则丢弃消息。 
### 客户收益 
受益方|受益描述
---|---
运营商|运营商可以对接入到EPS网络过程中对用户进行鉴权，拒绝非法用户接入EPS网络，避免用户非法使用网络资源，并对后续用户的信令安全进行保护，防止用户相关数据被窃听和篡改等威胁到网络安全的行为。
移动用户|终端用户可以对接入的EPS网络进行鉴权，避免使用到非法或损害用户利益的网络，终端用户还可以对信令和数据安全进行保护，防止用户相关数据被窃听和篡改等威胁到用户安全的行为。
### 实现原理 
##### 系统架构 
组网架构如[图1](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__LTE%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%9E%B6%E6%9E%84-EB441EBD)所示。
图1  LTE网络安全架构
[]images/EPC%E7%BB%84%E7%BD%91%E6%9E%B6%E6%9E%84%E5%9B%BE.png)
##### 涉及的网元 
网元名称|网元作用
---|---
UE|对网络进行鉴权及对NAS信令、AS信令和数据进行完整性保护与加密。
eNodeB|对用户提供接入层安全功能，对AS信令和数据完整性保护与加密。
MME|从HSS或老局MME/SGSN获取到鉴权向量，根据运营商策略对用户进行鉴权，启用安全上下文，并对后续的NAS消息进行安全保护。和EIR网元配合完成IMEI检查。为用户分配临时标识，并将生成的eNB密钥带给eNB。在与2/3G切换/TAU/RAU过程中，负责EPS安全上下文和UMTS安全上下文的转换。MME控制UE是否对到GERAN的重定向消息进行完整性保护。
HSS|配置生成UE的鉴权数据，并提供给MME。
EIR|配置UE的IMEI数据，并检查UE的IMEI是否合法。
##### 本网元实现 
本特性需要UE、eNB、MME、SGW、PGW和HSS等网元配合完成，详见业务流程。 
##### 业务流程 
用户鉴权
附着业务鉴权，如图2所示。图2  附着业务鉴权流程图流程说明：UE向MME发起附着业务。MME基于用户IMSI和当前附着业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权MME从HSS获得用户UE的鉴权数据，其中包括多组四元鉴权向量（RAND、XRES、AUTN和KASME）。MME向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，MME再对用户UE进行鉴权。MME完成鉴权后，选择完整性保护和加密算法通知到UE。MME计算生成Kenb密钥，及完整性保护和加密算法通知到eNodeB。 
TAU业务鉴权，如图3所示。图3  TAU业务鉴权流程图流程说明：UE向MME发起TAU业务。MME从老局MME获得用户的MM上下文和鉴权信息。MME基于用户IMSI和当前TAU业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权MME向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，MME再对用户UE进行鉴权。MME完成鉴权后，选择完整性保护和加密算法通知到UE。MME计算生成Kenb密钥，及完整性保护和加密算法通知到eNodeB。 
业务请求鉴权，如图4所示。图4  业务请求鉴权流程图流程说明：UE向MME发起业务请求。MME基于用户IMSI和当前业务请求业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权MME向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，MME再对用户UE进行鉴权。MME完成鉴权后，选择完整性保护和加密算法通知到UE。MME计算生成Kenb密钥，及完整性保护和加密算法通知到eNodeB。 
分离业务鉴权，如图5所示。图5  分离业务鉴权流程图流程说明：UE向MME发起分离业务。MME基于用户IMSI和当前分离业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权MME向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，MME再对用户UE进行鉴权。MME完成鉴权后，选择完整性保护和加密算法通知到UE。MME计算生成Kenb密钥，及完整性保护和加密算法通知到eNodeB。 
NAS消息完整性保护和加密
SMC流程，如图6所示。图6  SMC流程图流程说明：MME完成对用户UE的鉴权后，向UE发送 security mode command消息，该消息中包含eKSI、完整性保护和加密算法。UE接受完整性保护和加密的算法，向MME发送Security mode complete消息。 
NAS消息完整性保护机制图7  NAS层完整性保护机制流程说明：MME发送下行NAS消息时，对NAS消息进行完整性保护，MME将NAS下行序列号、方向位(下行)、承载标识、NAS消息、NAS信令的完整性保护密钥KNASint作为输入通过完整性保护算法获取MAC(message
authentication code)放在发送的消息中。MME接收到上行NAS消息时，对NAS消息进行完整性检查，MME将NAS上行序列号、方向位(上行)、承载标识、NAS消息、NAS信令的完整性保护密钥KNASint作为输入通过完整性保护算法计算XMAC，并与接收的消息中的MAC进行比较，如果一致，则完整性检查成功。 
NAS消息加解密机制图8  NAS层加解密机制流程说明：MME发送下行NAS消息时，对NAS消息进行加密，MME将NAS下行序列号、方向位(下行)、承载标识、NAS消息位长度、NAS信令的加密密钥KNASenc作为输入通过加密算法计算密钥流，MME将获取的密钥流对NAS消息明文进行加密获取NAS消息密文。MME接收到上行NAS消息时，对NAS消息进行解密，MME将NAS上行序列号、方向位(上行)、承载标识、NAS消息位长度、NAS信令的加密密钥KNASenc作为输入通过加密算法计算密钥流，将其对接收的加密NAS消息进行解密获取NAS消息明文。 
IMEI检查
流程图如[图9](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__IMEI%E6%A3%80%E6%9F%A5%E6%B5%81%E7%A8%8B%E5%9B%BE-EB580628)所示。
图9  IMEI检查流程图
[]images/ZUF-78-04-001-IMEI%E6%A3%80%E6%9F%A5%E6%B5%81%E7%A8%8B.png)
流程说明： 
MME向UE发送Identity Request消息，消息中Identity Type指示请求IMEISV。 
UE向MME响应Identity Response消息携带IMEISV。  
用户UE给MME返回UE的IMEI或IMEISV，MME向EIR发送EIR Check Request消息。 
EIR网元检查UE的IMEI，将检查结果在EIR Check Respond消息中通知到MME，MME基于检查结果放行业务或拒绝业务。 
用户标识分配
流程图如[图10](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E7%94%A8%E6%88%B7%E6%A0%87%E8%AF%86%E5%88%86%E9%85%8D%E6%B5%81%E7%A8%8B-EB586456)所示。
图10  用户标识分配流程
[]images/ZUF-78-04-001-%E7%94%A8%E6%88%B7%E6%A0%87%E8%AF%86%E5%88%86%E9%85%8D%E6%B5%81%E7%A8%8B.png)
流程说明： 
用户UE向MME发起Attach或TAU请求。 
MME为用户UE分配GUTI在Attach Accept或TAU Accept消息中携带。 
用户UE接受新的GUTI，给MME返回Attach Complete或TAU Complete消息。 
4G到2G重定向安全保护
流程说明： 
用户UE向MME发起Attach或TAU请求。 
MME给UE发送Attach Accept或TAU Accept消息。MME根据UE当前接入TA的配置确定是否置位"Unsecured redirection to GERAN not allowed"。如果置位，则表示UE对到GERAN的重定向消息进行完整性保护，如果进行完整性保护，UE对重定向到GERAN的命令进行完整性保护校验，校验成功后才可以向GERAN重定向，校验失败则丢弃消息。 
### 系统影响 
鉴权策略的不同可能会导致MME与HSS之间信令增加，以及增加业务时延，故在设定鉴权策略时需考虑对于S6a接口的影响以及业务时延是否可以接受。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
由于安全流程是基本业务流程，是后续所有的流程的基础，如果选择需要进行安全流程却无法使用，则其他业务都无法使用。 
### 遵循标准 
标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|-
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3".|-
3GPP TS 23.003: "Numbering, addressing and identification"|-
3GPP TS 33.401: "3GPP System Architecture Evolution: SecurityArchitecture".|-
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)".|-
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS"|-
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol"|-
### 特性能力 
名称|指标
---|---
基于IMSI号段配置鉴权策略|最大可配置256×6个IMSI号段
基于IMSI号段进行IMEI检查|最大可配置1024个IMSI号段
MME支持多PLMN|最大支持17个PLMN
MME支持多GUMMEI|最大支持9×9×9=729个GUMMEI（9个PLMN、9个MME Group ID和9个MME Code）
### 可获得性 
##### License要求 
该特性为ZXUN uMAC的基本特性，无需License支持。
##### 对其他网元的要求 
UE|eNodeB|MME|SGW|PGW|HSS
---|---|---|---|---|---
√|√|√|–|–|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
### O&M相关 
##### 命令 
配置项表2  新增配置项配置项命令新增MME IMSI鉴权配置ADD MME IMSI AUTH修改MME IMSI鉴权配置SET MME IMSI AUTH删除MME IMSI鉴权配置DEL MME IMSI AUTH查询MME IMSI鉴权配置 SHOW MME IMSI AUTH设置默认MME IMSI鉴权配置SET MME IMSI AUTH DEFAULT查询默认MME IMSI鉴权配置SHOW MME IMSI AUTH DEFAULT新增IMSI号段IMEI检查配置ADD MME IMEI CHECK删除IMSI号段IMEI检查配置DEL MME IMEI CHECK查询IMSI号段IMEI检查配置SHOW MME IMEI CHECK新增本局MME其他HPLMN配置ADD MME HPLMNCFG修改本局MME其他HPLMN配置SET MME HPLMNCFG删除本局MME其他HPLMN配置DEL MME HPLMNCFG查询本局MME其他HPLMN配置SHOW MME HPLMNCFG新增本局其他GUMMEI配置ADD GUMMEI修改本局其他GUMMEI配置SET GUMMEI删除本局其他GUMMEI配置DEL GUMMEI查询本局其他GUMMEI配置SHOW GUMMEI 
安全变量表3  新增安全变量安全变量命令EUTRANAUTHNUMSET SECURITY PARAMETERMMECHECKIMEIMMEFAILIMEIENCRYPTIONSET NAS ENCRYCTRLEEA0EEA1EEA2EEA3PRIORENCRY0PRIORENCRY1PRIORENCRY2PRIORENCRY3INTEGALGO1SET NAS INTEGCTRLINTEGALGO2INTEGALGO3PRIORINTEG1PRIORINTEG2PRIORINTEG3 
软件参数表4  新增软件参数软件参数ID软件参数名称262227MME是否基于IMSI号段IMEI检查 
##### 性能统计 
该特性不涉及性能统计的变化。 
##### 告警和通知 
该特性不涉及告警/通知消息的变化。 
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
无。 
### 配置前提 
UE、MME、SGW、eNodeB、PGW等各网元工作正常。 
MME网管服务器、客户端连接正常；服务器与OMP连接正常。 
MME已经配置好相关的本地配置。 
### 配置过程 
使用命令[SET SECURITY PARAMETER](../../MMESGSN\zh-CN\mml\1268035.html)设置MME安全参数 
例如： 
[SET SECURITY PARAMETER](../../MMESGSN\zh-CN\mml\1268035.html):EUTRANAUTHNUM=3,MMECHECKIMEI="Need",MMEFAILIMEI="Continue"
使用命令[SET NAS ENCRYCTRL](../../MMESGSN\zh-CN\mml\1268041.html)设置NAS加密控制参数 
例如： 
[SET NAS ENCRYCTRL](../../MMESGSN\zh-CN\mml\1268041.html):ENCRYPTION="Encrypt",EEA0="Support",EEA1="Support",EEA2="Support",EEA3="Not
support",PRIORENCRY0="2",PRIORENCRY1="1",PRIORENCRY2="0"
使用命令[SET NAS INTEGCTRL](../../MMESGSN\zh-CN\mml\1268047.html)设置NAS完整性保护参数 
例如： 
[SET NAS INTEGCTRL](../../MMESGSN\zh-CN\mml\1268047.html):INTEGALGO1="Support",INTEGALGO2="Support",INTEGALGO3="Not
support",PRIORINTEG1="1",PRIORINTEG2="0"
使用[ADD MME IMSI AUTH](../../MMESGSN\zh-CN\mml\1261155.html) 命令增加基于IMSI以及IMSI range鉴权配置
例如： 
[ADD MME IMSI AUTH](../../MMESGSN\zh-CN\mml\1261155.html):IMSI="46000",SERVICETYPE="IMSIATTACH",AUTHTYPE="Force"
使用[SET MME IMSI AUTH DEFAULT ](../../MMESGSN\zh-CN\mml\1261277.html)命令设置MME默认的鉴权配置 
例如： 
[SET MME IMSI AUTH DEFAULT](../../MMESGSN\zh-CN\mml\1261277.html):SERVICETYPE="IMSIATTACH",AUTHTYPE="System"
使用[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html)命令打开基于IMSI的IMEI检查功能
例如： 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262227,PARAVALUE=1
使用[ADD MME IMEI CHECK](../../MMESGSN\zh-CN\mml\1261600.html)命令增加基于IMSI的IMEI检查配置 
例如： 
[ADD MME IMEI CHECK](../../MMESGSN\zh-CN\mml\1261600.html):IMSI="4600100"
使用[SET COMBOCFG](../../MMESGSN\zh-CN\mml\1260006.html)命令设置MME本局GUMMEI
例如： 
Combo局：[SET COMBOCFG](../../MMESGSN\zh-CN\mml\1260006.html):MMEGROUPID=32768,MMCC="460",MMNC="00",MMECODE=1
使用[ADD MME HPLMNCFG ](../../MMESGSN\zh-CN\mml\1260235.html)命令设置MME本局支持的其他HPLMN
例如： 
[ADD MME HPLMNCFG](../../MMESGSN\zh-CN\mml\1260235.html):MCC="460",MNC="01"
使用[ADD GUMMEI](../../MMESGSN\zh-CN\mml\1260370.html) 命令设置MME本局支持的其他GUMMEI 
例如： 
[ADD GUMMEI](../../MMESGSN\zh-CN\mml\1260370.html):GUMMEI=1,PLMN="460"-"01",MMEGID=32768,MMEC=1
### 配置实例 
##### 鉴权控制 
场景说明
某运营商要求在对EPS用户鉴权向HSS获取鉴权向量时，一次获取3组鉴权向量，并要求IMSI为46000号段的用户在IMSI附着时强制鉴权，其他号段用户在IMSI附着时系统判断。 
配置步骤
配置鉴权时获取的鉴权向量组数： 
解释说明
配置MME获取E-UTRAN鉴权向量组数为3组。
配置脚本
SET SECURITY PARAMETER:EUTRANAUTHNUM=3
配置46000号段的用户业务类型为“IMSI附着”的鉴权类型为“强制鉴权” 
解释说明
配置46000号段IMSI附着强制鉴权。
配置脚本
ADD MME IMSI AUTH:IMSI="46000",SERVICETYPE="IMSIATTACH",AUTHTYPE="Force"
配置MME默认的业务类型为“IMSI附着”的鉴权类型为“强制鉴权” 
解释说明
配置IMSI附着默认鉴权类型为系统判断。
配置脚本
SET MME IMSI AUTH DEFAULT:SERVICETYPE="IMSIATTACH",AUTHTYPE="System"
##### NAS加密和完整性保护 
场景说明
某运营商对EPS用户使用加密算法0、1和2，优先使用算法2，其次算法1，算法0优先级最低；完整性保护算法使用算法1和2；优先使用算法2，其次算法1。 
配置步骤
配置NAS支持的加密算法 
解释说明
配置NAS加密支持算法0、1和2，算法2优先级最高，算法0优先级最低。
配置脚本
SET NAS ENCRYCTRL:ENCRYPTION="Encrypt",EEA0="Support",EEA1="Support",EEA2="Support",EEA3="Notsupport",PRIORENCRY0="2",PRIORENCRY1="1",PRIORENCRY2="0"
配置NAS支持的完整性保护算法 
解释说明
配置NAS完整性保护支持算法1和2，算法2优先级最高。
配置脚本
SET NAS INTEGCTRL:INTEGALGO1="Support",INTEGALGO2="Support",INTEGALGO3="Notsupport",PRIORINTEG1="1",PRIORINTEG2="0"
##### IMEI检查 
场景1
场景说明某运营商开启IMEI检查，需要对所有用户进行IMEI检查，向终端获取IMEI，在IMEI检查为黑名单时限制用户接入；如果IMEI获取失败，或IMEI检查流程失败，流程继续，不限制用户接入。 
配置步骤配置获取用户IMEI 
解释说明
配置MME获取IMEI。
配置脚本
SET MOBILE MANAGEMENT:MMEGETIMEI="GetIMEI"
配置IMEI检查 
解释说明
配置MME开启IMEI检查，IMEI获取失败或检查失败流程继续。
配置脚本
SET SECURITY PARAMETER:MMECHECKIMEI="Need",MMEFAILIMEI="Continue"
场景2
场景说明某运营商开启IMEI检查，需要根据IMSI对部分号段的用户进行IMEI检查，4600100号段的用户进行IMEI检查，其他号段的用户不进行IMEI检查。 
配置步骤配置获取用户IMEI 
解释说明
配置MME获取IMEI。
配置脚本
SET MOBILE MANAGEMENT:MMEGETIMEI="GetIMEI"
开启基于IMSI的IMEI检查功能 
解释说明
配置MME支持基于IMSI的IMEI检查功能。
配置脚本
SET SOFTWARE PARAMETER:PARAID=262227,PARAVALUE=1
配置IMEI检查的IMSI号段 
解释说明
配置需要IMEI检查的IMSI号段。
配置脚本
ADD MME IMEI CHECK:IMSI="4600100"
##### GUTI分配 
场景说明
某局用户容量较大，超过200万，MME配置一个GUMMEI不能满足容量要求，需要配置多个GUMMEI。本局移动配置PLMN为46000，MME
GroupID为32768，MME Code为1；MME支持的其他GUMMEI配置PLMN为46000，MME GroupID为32768，MME
Code为2。 
配置步骤
配置本局移动支持的GUMMEI 
解释说明
配置本局移动支持的GUMMEI。
配置脚本
Combo局：SET COMBOCFG:MMEGROUPID=32768,MMCC="460",MMNC="00",MMECODE=1
配置MME支持的其他GUMMEI 
解释说明
配置MME支持的其他GUMMEI。
配置脚本
ADD GUMMEI:GUMMEI=1,PLMN="460"-"00",MMEGID=32768,MMEC=2
### 调整特性 
S1消息响应时间SET DEFPRETMR:TIMER=201613,CURINTERVAL=50000 
鉴权响应时间SET DEFPRETMR:TIMER=201603,CURINTERVAL=50000 
### 测试用例 
测试项目|鉴权控制
---|---
测试目的|验证MME能正确处理鉴权控制
预置条件|LTE网络内的所有网元运行正常，OM维护正常。用户在HSS开户，并签约LTE业务。打开消息跟踪。MME配置获取3组鉴权向量，并对IMSI号段为4600010的用户设置局内GUTI附着强制鉴权；设置默认局内GUTI附着鉴权类型为系统判断。
测试过程|4600010号段用户和4600020号段用户分别多次附着到MME。检查网络侧用户信息和测试信令。
通过准则|MME对4600010号段的用户每次GUTI附着都进行鉴权，向HSS发送的AIR消息中请求E-UTRAN鉴权向量组数为3组。MME对4600020号段的用户除了初次附着鉴权后，后续GUTI局内附着都不进行鉴权消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|NAS加密和完整性保护
---|---
测试目的|验证MME能正确处理NAS加密和完整性保护
预置条件|LTE网络内的所有网元运行正常，OM维护正常。用户在HSS开户，并签约LTE业务。打开消息跟踪。MME配置支持加密算法0、1和2；支持完整性保持算法1和2；优先使用加密算法2和完整性保护算法2。UE支持加密算法2和完整性保护算法2。
测试过程|用户开机发起附着检查网络侧用户信息和测试信令。
通过准则|MME发送Security Mode Command消息中选择的加密算法和完整性算法都为2。UE附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|IMEI检查
---|---
测试目的|验证MME能正确处理IMEI检查
预置条件|LTE网络内的所有网元运行正常，OM维护正常。用户在HSS开户，并签约LTE业务；签约IMEI为白名单。打开消息跟踪。MME开启获取用户IMEI和IMEI检查功能。MME配置EIR，与EIR间链路正常。
测试过程|用户开机发起附着。检查网络侧用户信息和测试信令。
通过准则|MME向UE获取IMEI，并发起IMEI检查流程。EIR返回IMEI检查结果为白名单，MME允许UE接入。UE附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|基于IMSI号段的IMEI检查
---|---
测试目的|验证MME能正确处理基于IMSI号段的IMEI检查
预置条件|LTE网络内的所有网元运行正常，OM维护正常。用户在HSS开户，并签约LTE业务；签约IMEI为白名单。打开消息跟踪。MME开启获取用户IMEI和IMEI检查功能。MME配置EIR，与EIR间链路正常。
测试过程|4600100和4600101号段的2个用户开机发起附着。检查网络侧用户信息和测试信令。
通过准则|MME向2个UE都获取IMEI，对于4600100号段的用户发起IMEI检查流程；对于4600101号段的用户不发起IMEI检查流程。EIR返回IMEI检查结果为白名单，MME允许4600100号段的UE接入。2个UE都附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|GUTI分配
---|---
测试目的|验证MME能正确处理GUTI分配
预置条件|LTE网络内的所有网元运行正常，OM维护正常。用户在HSS开户，并签约LTE业务。打开消息跟踪。MME在本局移动中配置的GUMMEI为46000-8000-01；其他GUMMEI中配置的GUMMEI为46000-8000-02。
测试过程|用户多次进行附着检查网络侧用户信息和测试信令
通过准则|在不同的附着流程，MME发送的Attach Accept消息中分配的GUTI中既有46000-8000-01的GUMMEI，也有46000-8000-02的GUMMEI。UE附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
### 常见问题处理 
无。 
# ZUF-78-04-002 二次鉴权 
## 概述 
移动终端只有在鉴权成功后才能接入网络。 
## 收益 
本特性保障网络安全，阻止未授权用户接入网络。 
## 描述 
当UE发起业务，如果MME对UE的第一次鉴权失败后，MME再次从HSS获取鉴权矢量，进行二次鉴权。 
# ZUF-78-04-003 NAS层加密 
在LTE网络，MME为NAS信令提供加密和解密功能。MME支持如下加密算法：
EEA0（未加密） 
EEA1（SNOW 3G算法） 
EEA2（AES算法） 
EEA3（ZUC算法） 
可在MME上配置这些算法的优先级。MME优先使用高优先级的算法。 
MME基于MME和UE所共同支持的算法进行算法选择。 
详细说明参见[描述](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842494)。
# ZUF-78-04-004 NAS层完整性保护 
在LTE网络，MME为NAS信令提供完整性保护。MME支持如下完整性包括算法：
EIA0（空算法） 
EIA1（SNOW 3G算法） 
EIA2（AES算法） 
EIA3（ZUC算法） 
可在MME上配置这些算法的优先级。MME优先使用高优先级的算法。 
MME根据MME和UE所共同支持的完整性保护算法进行算法选择。 
空算法EIA0仅用于无卡或者认证失败用户发起紧急呼叫业务过程中。 
详细说明参见[描述](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842494)。
# ZUF-78-04-005 AS层安全模式过程 
## 概述 
AS层安全模式命令过程用于RRC级安全。 
## 收益 
AS层安全模式命令过程使能UP话务加密以及RRC信令的加密和完整性保护。 
## 描述 
MME通过向eNodeB发送需要的安全参数触发RRC级AS安全模式命令过程。 
该过程使能UP话务加密以及RRC信令的加密和完整性保护。  
# ZUF-78-04-006 GUTI重分配 
UE和MME间的信令连接建立后，MME可随时发起GUTI重分配流程，为UE重分配一个新的GUTI。GUTI也可在附着或TAU流程中进行重分配。
MME向UE发送GUTI Reallocation Command消息，消息包含GUTI。 
UE向MME响应GUTI Reallocation Complete消息。 
详细说明参见[描述](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842494)。
# ZUF-78-04-007 IMEI检查 
移动设备身份检查流程允许MME的操作员检查移动设备的身份（例如检查某个移动手机是否被盗或验证某个移动手机是否有故障）。 
MME可将设备号通过S13接口发送给EIR，由EIR检测设备是否合法，MME分析EIR返回的响应，并根据该响应决定后续操作（例如，如果EIR指示该移动设备被盗，则MME发送附着拒绝消息）。 
如果通过移动设备身份检查发现某移动设备在灰名单或黑名单内，设备所有人或被警告或被禁止接入网络。 
MME根据EIR检查结果决策是否拒绝用户接入处理详细参见下表。 
EIR检查结果|MME处理策略
---|---
EIR返回黑名单|配置控制，默认拒绝
EIR返回未知设备|配置控制，默认不拒绝
EIR返回灰名单|配置控制，默认不拒绝
EIR超时无响应|配置控制，默认不拒绝
EIR返回其他失败|配置控制，默认不拒绝
获取EIR局向失败|配置控制，默认不拒绝
根据IMSI号段范围，MME可进行移动设备身份检查或跳过该检查。 
详细说明参见[描述](ZUF-78-04-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842494)。
# ZUF-78-04-008 ADD 
## 特性描述 
摘要术语描述应用场景客户收益实现原理系统影响应用限制遵循标准特性能力可获得性O&M相关 
### 术语 
术语|含义
---|---
MME池区|MME池区是指UE在其间移动不需要改变服务MME的区域。一个MME池区内有一个或多个对等的MME。MME池区是由多个TA汇聚。MME池区间可以有交迭。
SGW池区|SGW池区是指UE在其间移动不需要改变服务SGW的区域。一个SGW池区内有一个或多个对等的SGW。SGW池区是由多个TA汇聚。MME池区间可以有交迭。
默认APN|默认APN是在签约数据中被标识为默认的APN，用于在附着过程中建立默认的PDN连接。
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载。
专用承载|专用承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载。
AMBR|AMBR是用来限制每个UE所有非GBR承载的汇聚最大bit rate的QoS项。
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载。
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载。
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|在UE和PDN间存在的联系，该联系中一个IPV4或一个IPV6地址，或者两者都有代表一个UE；一个APN代表该PDN。
### 描述 
定义
ADD（Automatic Device Detection），是指MME把UE终端的IMEISV信息带给HSS，HSS根据IMEISV来检测终端是否合法。
背景知识
EPS网络架构图，如下图所示，其中包含了如下网元：
图1  EPS架构图
[]images/1587639005635.png)
UE（User Equipment，用户设备）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，完成无线资源管理功能，完成移动性管理功能，完成安全功能，完成承载管理功能。 
E-UTRAN（Evolved UTRAN，演进的无线接入网）：可以提供更高的上下行速率，更低的传输延迟和更加可靠的无线传输。E-UTRAN中包含的网元是eNodeB（Evolved
NodeB），为终端的接入提供无线资源。 
HSS（Home Subscriber Server，归属用户服务器）：永久存储用户签约数据。 
EPC（ E-Packet Core，演进的分组核心网）：提供了更低的延迟，并允许更多的无线接入系统接入。包含了如下网元： 
MME（Mobility Management Entity，移动管理实体）：控制面功能实体，临时存储用户数据的服务器，负责管理和存储UE
相关信息，比如UE/用户 标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。 
Serving GW（Serving  Gateway，服务网关）：用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。 
PDN GW（PDN Gateway，分组数据网网关）：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个PDN
GW。在物理上，Serving GW和PDN GW可能合一。 
### 应用场景 
具体见场景包括：要求MME支持ADD的局点。 
### 客户收益 
受益方|受益描述
---|---
运营商|实现ADD功能
移动终端用户|N/A
### 实现原理 
涉及的网元
MME支持小区位置上报功能需要MME、HSS和eNodeB共同完成。 
网元|功能
---|---
MME|负责把获取用户的IMEISV，同时把IMEISV信息上报给HSS。
HSS|负责接收并处理MME上报的IMEISV信息。
业务流程
安全流程的ADD功能
图2  安全流程的ADD功能
[]images/1587639005785.png)
如果TAU流程中MME没有用户的IMEISV信息，或在Attach流程MME判断支持ADD功能，并且需要对用户进行安全流程处理。
MME向UE发送Security mode command消息，消息中携带获取IMEISV指示信息。 
MME收到UE的Security mode complete消息，消息中携带UE的IMEISV信息。 
如果UE以前没有在MME中注册，则MME向HSS发送的Update Location Request消息，消息中包含IMEISV信息。 
HSS向MME回的Update Location Answer消息。 
如果UE以前在MME中注册，则MME比较从UE获取的IMEISV是否与MME中存储的IMEISV一致，如果不一致，且MME判断支持ADD功能。如果MME需要向HSS发送位置更新，则MME向HSS发送的Update
Location Request消息，消息中包含IMEISV信息；如果MME不需要向HSS发送位置更新，则在向HSS发送的Notify
Request消息中携带IMEISV。 
ID流程的ADD功能
图3  ID流程的ADD功能
[]images/1587639005935.png)
如果TAU流程中MME没有用户的IMEISV信息，或在Attach流程MME判断支持ADD功能，但不需要对用户安全流程处理。 
MME向UE发送Identity Request消息，消息中携带获取IMEISV指示信息。 
MME收到UE的Identity Response消息，消息中携带UE的IMEISV信息。 
如果UE以前没有在MME中注册，则MME向HSS发送的Update Location Request消息，消息中包含IMEISV信息。 
HSS向MME回的Update Location Answer消息。 
如果UE以前在MME中注册，则MME比较从UE获取的IMEISV是否与MME中存储的IMEISV一致，如果不一致，且MME判断支持ADD功能：如果MME需要向HSS发送位置更新，则MME向HSS发送的Update
Location Request消息，消息中包含IMEISV信息；如果MME不需要向HSS发送位置更新，则在向HSS发送的Notify
Request消息中携带IMEISV。 
### 系统影响 
本功能对MME的性能影响很小。 
### 应用限制 
要求MME支持ADD的局点。 
### 遵循标准 
3GPP TS 23.060 
3GPP TS 23.401 
### 特性能力 
本功能对MME的特性能力无影响。 
### 可获得性 
对其他网元的要求
eNodeB、MME以及HSS能够按照3GPP23.060和23.401协议处理。
### O&M相关 
命令
配置项 
修改配置项参见[表3](#T_201512301723953__%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE%E9%A1%B9-24E0C7F6)。
配置项|命令|修改的参数
---|---|---
移动管理参数配置|SET MOBILE MANAGEMENT|增加参数：MME支持ADD功能
## 特性配置 
MME支持ADD功能配置特性 
### MME支持ADD功能配置特性 
配置前提
业务已经配置完成。 
MME和HSS链路正常。 
MME支持ADD功能。 
配置过程
使用命令[SET MOBILE MANAGEMENT](../../MMESGSN\zh-CN\mml\1268008.html)配置MME支持ADD功能。
配置实例
配置步骤|配置说明
---|---
SET MOBILE MANAGEMENT:MMEGETIMEI="Support ADD"|配置MME支持ADD功能
# ZUF-78-04-009 USIM卡安全密钥转换 
## 概述 
当UE在E-UTRAN和GREAN/UTRAN之间切换时，需要将转换EPS安全密钥Kasme以及3G安全密钥CK和IK。 
## 收益 
本特性对于UE在E-UTRAN和GRAN/UTRAN之间移动是一个必要功能。 
## 描述 
当UE从E-UTRAN切换到GREAN/UTRAN，MME将EPS安全密钥Kasme转换成CK和IK密钥。 
当UE从GREAN/UTRAN切换到E-UTRAN，MME将CK和IK密钥转换成EPS安全密钥。 
 缩略语 
 缩略语 
# 3GPP 
3rd Generation Partnership Project第三代合作伙伴计划
# ADD 
Automatic Device Detection自动设备检测
# AMBR 
Aggregate Maximum Bit Rate聚合最大比特率
# APN 
Access Point Name接入点名称
# eNodeB 
Evolved NodeB演进的NodeB
# EPS 
Evolved Packet System演进的分组系统
# GBR 
Guaranteed Bit Rate保证比特率
# GUTI 
Globally Unique Temporary Identity全球唯一临时标识
# HSS 
Home Subscriber Server归属用户服务器
# IMEISV 
International Mobile Equipment Identity and Software Version number国际移动设备识别码和软件版本号
# IMSI 
International Mobile Subscriber Identity国际移动用户标识
# LTE 
Long Term Evolution长期演进
# MME 
Mobility Management Entity移动管理实体
# NAS 
Non-Access Stratum非接入层
# NCC 
Next Hop Chaining Counter下一跳链接计数器
# PDN 
Packet Data Network分组数据网
# PGW 
PDN Gateway分组数据网网关
# QoS 
Quality of Service服务质量
# SGW 
Serving Gateway服务网关
# TA 
Tracking Area跟踪区域
# TAU 
Tracking Area Update跟踪区域更新
# UE 
User Equipment用户设备
# UTRAN 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
