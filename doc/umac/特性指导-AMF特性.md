# ZUF-79-01 融合AMF&MME&SGSN 
## ZUF-79-01-001 融合AMF&MME&SGSN 
特性描述 :特性描述 :描述 :定义 :融合AMF&MME&SGSN，是指同时具备AMF、MME和SGSN协议功能的融合网元，通过3GPP标准协议接口与网络中其他网元交互。融合AMF&MME&SGSN同时支持2/3/4/5G接入，当移动终端在同一个融合网元内跨RAT移动时，AMF/MME/SGSN间的信令直接在融合网元内部完成，不需要对外暴露标准接口信令。
背景知识 :3GPP标准定义的5GC与EPC互操作架构图如[图1]所示。
图1  5GC与EPC互操作架构

UDM和HSS融合以保证跨RAT用户签约数据一致，SMF和PGW-C融合以保证跨RAT用户会话锚定，UPF和PGW-U融合以保证跨RAT用户的用户面数据锚定，PCF和PCRF融合以保证跨RAT用户策略一致，协议没有强制要求AMF和MME融合。
 说明： 
协议没有强制要求AMF和MME融合的原因：用户跨RAT移动时，AMF和MME之间有N26接口时，可以通过N26接口传递用户上下文；AMF和MME之间无N26接口时，可以通过UDM&HSS存储SMF&PGW-C地址保证会话锚定。 
AMF和MME的融合可以带来如下的优势， 
降低管理成本：可有效降低需要管理的网元数，节约网络管理成本。 
降低使用成本：提供2/3/4/5G统一接入，支持4G到5G的平滑演进，节约网络维护及升级成本。 
提升用户体验：基于N26的互操作，特别是语音回落时，可有效降低N26接口传输时延，缩短语音接通时延。 
节约系统资源：互操作过程中涉及的GTP、DNS等资源可共享，支持合一的管理维护虚机、数据处理虚机、IP路由虚机、SCTP链路处理虚机和业务主处理虚机。 
应用场景 :融合AMF&MME&SGSN支持全接入，可灵活适应多种部署场景，主要的使用场景如下： 
###### 场景1：2/3/4/5G全接入，系统平滑演进 
现网ZXUN uMAC版本通过软件升级支持融合AMF&MME&SGSN功能，支持2G/3G/4G/5G全接入，保证网络的平滑演进，如[图2]所示。
图2  平滑演进

###### 场景2：AMF&MME&SGSN融合组Pool 
AMF、MME和SGSN可以融合组Pool，通过融合节点选择功能保证跨RAT移动时选择同一融合节点，缩短互操作时延，示意图如[图3]所示（图中未体现SGSN）。
图3  融合组Pool

客户收益 :受益方|受益描述
---|---
运营商|降低管理成本：可有效降低需要管理的网元数，节约网络管理成本。降低使用成本：提供2/3/4/5G统一接入，支持4G到5G的平滑演进，节约网络维护及升级成本。节约系统资源：互操作过程中涉及的GTP、DNS等资源可共享，支持合一的管理维护虚机、数据处理虚机、IP路由虚机、SCTP链路处理虚机、业务主处理虚机。
终端用户|提升用户体验：基于N26的互操作，特别是语音回落时，可有效降低N26接口传输时延，缩短语音接通时延。
实现原理 :系统架构 :融合AMF&MME&SGSN组网如[图4]所示。AMF&MME&SGSN作为一个融合网元，涵盖AMF、MME及SGSN协议网元功能，并通过标准协议接口与周边网元对接。
图4  融合AMF组网

融合AMF&MME&SGSN内部架构如[图5]所示，统一数据和管理，业务独立，其中：
通过统一数据服务，实现用户2/3/4/5G数据融合及统一管理。 
通过统一网管服务，实现AMF&MME&SGSN服务的统一编排、部署和操作维护。 
通过公共服务，实现通用功能（如：SCTP、IPU）在融合网元内的共享。 
通过统一平台，融合网元提供统一的内部通讯、虚机管理等平台服务。 
通过IaaS资源池，为融合网元提供提供统一的虚拟化资源池。 
图5  融合AMF架构

涉及的NF/网元 :融合AMF&MME&SGSN对外仍然体现的是AMF、MME、SGSN协议网元功能，不涉及其他NF/网元。 
协议栈 :融合AMF&MME&SGSN对外仍然体现的是AMF、MME、SGSN协议网元功能，对外接口及协议栈无变化。 
本NF/网元实现 :融合AMF&MME&SGSN主要实现如下功能： 
AMF、MME和SGSN的管理、数据、公共服务的架构融合，对外呈现为一个融合网元。 
支持UE在2/3G与4G间、4G与5G间跨RAT移动时，选择统一的融合网元。融合AMF&MME&SGSN 除了公共服务外，业务处理服务（MME&SGSN控制面业务、AMF Communication业务）也支持合一虚机部署，共享CPU资源。虚机说明融合说明OMU操作管理单元网元操作维护处理GSU-CK1通用业务处理单元-CK1MME&SGSN控制面业务处理和AMF Communication业务处理GSU-CK2通用业务处理单元-CK2AMF MT服务处理GSU-CK3通用业务处理单元-CK3AMF EventExposure业务处理GSU-CK4通用业务处理单元-CK4AMF Location业务处理GSU-UK1通用业务处理单元-UK1SGSN用户面处理GSU-RK1通用业务处理单元-RK1资源管理GSU-LK1通用业务处理单元-CK1SCTP链路和负载均衡处理GSU-LK2通用业务处理单元-CK2HTTP链路和负载均衡处理IPUIP处理单元IP路由处理CDU云数据单元统一数据处理 
业务流程 :架构融合不涉及业务流程变化。[图6]描述如何实现融合节点的选择。
图6  融合节点选择

流程描述如下： 
在RNC/BSC中配置基于MME Code映射而来的NRI并指向该融合节点的SGSN。
MME收到eNodeB的S1 Setup Request消息，向eNode发送S1 Setup Response消息时，同时将融合节点中SGSN配置的全部TA与NRI组合映射为GUMMEI列表，以及融合节点中AMF
GUAMI列表全部映射为GUMMEI列表，一并下发给eNodeB。 
AMF收到gNodeB的NG Setup Request消息，向gNodeB发送NG Setup Response消息时，同时将融合节点中MME
GUMMEI列表全部映射为GUAMI列表下发给gNodeB。 
当用户跨RAT移动，从2/3G移动到4G，从4G移动到5G，或者反之，BSC/RNC/eNodeB/gNodeB根据步骤1~3中配置或核心网下发的AMF/MME/SGSN网元映射标识选择融合节点（即融合的AMF&MME&SGSN网元）。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准名称|章节
---|---|---
3GPP|TS 38.413 NG Application Protocol (NGAP)|9.2.6.2 NG SETUP RESPONSE
3GPP|TS 36.413 S1 Application Protocol (S1AP)|9.1.8.5 S1 SETUP RESPONSE
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.20.20|添加控制用户的License
01|V7.19.10|首次发布
License要求 :系统中对于用户数有不同的License。以下License用于控制2G/3G/4G/5G的用户之和： 
uMAC_Common_7126：总注册用户数 
uMAC_Common_7127：总在线用户数 
工程规划要求 :根据运营商资源情况，MME GTP-C地址和AMF GTP-C地址可分可合。 
O&M相关 :命令 :配置项|命令
---|---
AMF融合配置|SET CONVERGENCECFG
SHOW CONVERGENCECFG|AMF融合配置
MME主机解析配置|ADD ADDRPOOL
DEL ADDRPOOL|MME主机解析配置
SHOW ADDRPOOL|MME主机解析配置
ADD MMEHOST|MME主机解析配置
SET MMEHOST|MME主机解析配置
DEL MMEHOST|MME主机解析配置
SHOW MMEHOST|MME主机解析配置
ADD HOSTSUBNETPRI|MME主机解析配置
SET HOSTSUBNETPRI|MME主机解析配置
DEL HOSTSUBNETPRI|MME主机解析配置
SHOW HOSTSUBNETPRI|MME主机解析配置
AMF互操作配置|SET 5GINTERWORKCFG
SHOW 5GINTERWORKCFG|AMF互操作配置
AMF GTPC地址配置|SET AMFGTPCADDRCFG
SHOW AMFGTPCADDRCFG|AMF GTPC地址配置
EBI分配基本配置|SET 5GEBIASSIGNPOLICY
SHOW 5GEBIASSIGNPOLICY|EBI分配基本配置
EBI抢占优先级配置|SET 5GDEFAULTEBIASSIGNPRIORITY
SHOW 5GDEFAULTEBIASSIGNPRIORITY|EBI抢占优先级配置
SET 5GEBIPRIOMATCHORDER|EBI抢占优先级配置
SHOW 5GEBIPRIOMATCHORDER|EBI抢占优先级配置
ADD 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
MOD 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
DEL 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
SHOW 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
EPC加密配置|SET EPC NAS ENCRYPT CONFIG
SHOW EPC NAS ENCRYPT CONFIG|EPC加密配置
EPC完保配置|SET EPC NAS INTEGRATE CONFIG
SHOW EPC NAS INTEGRATE CONFIG|EPC完保配置
性能统计 :测量类型|描述
---|---
4/5G切换分NF测量|编号为51032开头的所有计数器
N26接口测量|l编号为51059开头的所有计数器
性能计数器名称
---
C510020037 N26口的互操作流程注册请求次数
C510020038 N26口的互操作流程注册成功次数
C510020039 无N26接口的互操作流程注册请求次数
C510020040 无N26口的互操作流程注册成功次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置实现AMF、MME和SGSN功能的融合，可以同时支持2/3/4/5G的接入。 
系统中对于用户数有不同的License。以下License用于控制2G/3G/4G/5G的用户之和： 
uMAC_Common_7126：总注册用户数 
uMAC_Common_7127：总在线用户数 
配置前提 :已同时部署5GC和EPC系统。 
配置过程 :通过[SET CONVERGENCECFG]命令配置系统是合一运行还是独立运行。
通过[SET 5GINTERWORKCFG]命令配置互操作模式。
配置AMF本地解析的MME地址。 
通过[ADD ADDRPOOL]命令配置地址池的IP地址。
通过[ADD MMEHOST]命令配置MME地址解析记录。
通过[ADD HOSTSUBNETPRI]命令配置MME地址解析优选子网段。
通过[SET AMFGTPCADDRCFG]命令配置AMF GTPC地址。
通过[SET 5GEBIASSIGNPOLICY]命令配置EBI分配基本配置。
通过[SET 5GEBIPRIOMATCHORDER]命令配置配置EBI优先级匹配顺序。
通过[SET 5GDEFAULTEBIASSIGNPRIORITY]命令配置默认的EBI分配优先级。
通过[ADD 5GEBIASSIGNPRIORITY]命令配置EBI分配优先级。
通过[SET EPC NAS ENCRYPT CONFIG]命令配置EPC加密策略。
通过[SET EPC NAS INTEGRATE CONFIG]命令配置EPC完保策略。
配置实例 :场景说明 :某局点支持跨系统移动，AMF支持有N26的4G/5G互操作，SMF eMBB切片支持N26方式的4G/5G互操作。 
数据规划 :参数|取值
---|---
AMF融合配置|运行模式|CONVERGENCE（合一运行）
AMF支持的互操作模式和当前互操作模式|支持N26互操作|支持（SPRT）
支持无N26互操作|AMF支持的互操作模式和当前互操作模式|支持（SPRT）
互操作模式|AMF支持的互操作模式和当前互操作模式|有N26（WITHN26）
AMF本地解析的MME地址配置|FQDN|tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org
MME地址|AMF本地解析的MME地址配置|8.8.8.8
主机名|AMF本地解析的MME地址配置|mme1
子网地址|AMF本地解析的MME地址配置|1.1.1.0
掩码长度|AMF本地解析的MME地址配置|24
AMF本局的GTPC地址|AMF GTPC地址|6.6.6.6
AMF N26 VRF|AMF本局的GTPC地址|1
EBI分配基本配置|同一DNN多SMF时EBI分配策略|抢占（EMPTION）
EBI资源不足时EBI分配策略|EBI分配基本配置|抢占（EMPTION）
EBI优先级匹配顺序配置|EBI优先级匹配顺序|S-NSSNI优先
EBI优先级默认优先级配置|EBI分配默认优先级|5
基于S-NSSAI和ARP的优先级配置|EBI分配优先级标识|1
ARP优先级|基于S-NSSAI和ARP的优先级配置|1
ARP抢占能力|基于S-NSSAI和ARP的优先级配置|抢占（YES）
ARP被抢占能力|基于S-NSSAI和ARP的优先级配置|被抢占（YES）
SNSSAI SST|基于S-NSSAI和ARP的优先级配置|eMBB（eMBB）
SNSSAI SD|基于S-NSSAI和ARP的优先级配置|1
EBI分配优先级|基于S-NSSAI和ARP的优先级配置|1
EPC NAS加密配置|4G EA0算法开关|支持（EPCEA0SUPPORT）
4G EA0算法优先级|EPC NAS加密配置|1
4G EA1算法开关|EPC NAS加密配置|不支持（EPCEA1NOSUPPORT）
4G EA1算法优先级|EPC NAS加密配置|1
4G EA2算法开关|EPC NAS加密配置|不支持（EPCEA2NOSUPPORT）
4G EA2算法优先级|EPC NAS加密配置|1
4G EA3算法开关|EPC NAS加密配置|不支持（EPCEA3NOSUPPORT）
4G EA3算法优先级|EPC NAS加密配置|1
EPC NAS完保配置|4G IA1算法开关|支持（EPCIA1SUPPORT）
4G IA1算法优先级|EPC NAS完保配置|1
4G IA2算法开关|EPC NAS完保配置|不支持（EPCIA2NOSUPPORT）
4G IA2算法优先级|EPC NAS完保配置|1
4G IA3算法开关|EPC NAS完保配置|不支持（EPCIA3NOSUPPORT）
4G IA3算法优先级|EPC NAS完保配置|1
配置步骤 :步骤|说明|操作
---|---|---
1|配置AMF运行模式为合一运行|SET CONVERGENCECFG:MODE="CONVERGENCE"
2|配置AMF支持互操作模式和当前互操作模式|SET 5GINTERWORKCFG:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="SPRT",INTERWORKMODE="WITHN26"
3|配置AMF本地解析的MME地址|ADD ADDRPOOL:IPTYPE="IPV4",IPADDR="8.8.8.8",ADDRPOOLID=1ADD MMEHOST:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org", HOSTNAME="mme1", PRIORITY=1, WEIGHT=50, ADDRPOOLID=1ADD HOSTSUBNETPRI:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org", SUBNETADDR="1.1.1.0", MASKLEN=24, PRIORITY=1
4|配置AMF本局的GTPC地址|SET AMFGTPCADDRCFG:AMFGTPCADDRESS="6.6.6.6",AMFN26VRF=1
5|EBI分配基本配置|SET 5GEBIASSIGNPOLICY:EBIASSIPLYFORSEVSMF="EMPTION",EBIASSIPLYFORINRSC="EMPTION"
6|配置EBI优先级匹配顺序|SET 5GEBIPRIOMATCHORDER:PRIOMATCHORD="SNSSNIPRIO"
7|配置EBI优先级默认优先级|SET 5GDEFAULTEBIASSIGNPRIORITY:DEFAULTPRIORITY=5
8|配置基于S-NSSAI和ARP的优先级|ADD 5GEBIASSIGNPRIORITY:EBIASSIGNPRIID=1,ARPPRILEV=1,ARPEMPTIONCAP="YES",ARPEMPTIONVUL="YES",PRIORITY=5
9|配置EPC NAS加密配置|SET EPC NAS ENCRYPT CONFIG:EPC_EA0="EPCEA0SUPPORT",EPC_EA0ALGPRIORITY=1,EPC_EA1="EPCEA1NOSUPPORT",EPC_EA1ALGPRIORITY=1,EPC_EA2="EPCEA2NOSUPPORT",EPC_EA2ALGPRIORITY=1,EPC_EA3="EPCEA3NOSUPPORT",EPC_EA3ALGPRIORITY=1
10|配置EPC NAS完保配置|SET EPC NAS INTEGRATE CONFIG:EPC_IA1="EPCIA1SUPPORT",EPC_IA1ALGPRIORITY=1,EPC_IA2="EPCIA2NOSUPPORT",EPC_IA2ALGPRIORITY=1,EPC_IA3="EPCIA3NOSUPPORT",EPC_IA3ALGPRIORITY=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|UE从4G通过N26接口跨系统移动到5G
---|---
测试目的|验证UE成功从4G跨系统移动到5G
预置条件|MME和AMF都支持N26接口，且当前在支持N26接口的模式
测试过程|UE在4G附着后进入空闲态，移动到5G发起注册。
通过准则|UE在5G注册成功。N26接口有Context Request和Context Response消息。会话切换到5G。
测试结果|–
常见问题处理 :无 
# 缩略语 
# 缩略语 
AMF :Access and Mobility Management Function接入和移动管理功能
DNS :Domain Name Server域名服务器
GTP :GPRS Tunneling ProtocolGPRS隧道协议
HSS :Home Subscriber Server归属用户服务器
MME :Mobility Management Entity移动管理实体
## NRI 
Network Resource Identifier网络资源标识
PCF :Policy Control Function策略控制功能
PCRF :Policy and Charging Rules Function策略和计费规则功能
## PGW-C 
PDN Gateway Control plane functionPGW控制面网关
## PGW-U 
PDN Gateway User plane functionPGW用户面网关
RAT :Radio Access Technology无线接入技术
SCTP :Stream Control Transmission Protocol流控制传输协议
SGSN :Serving GPRS Support Node服务GPRS支持节点
SMF :Session Management Function会话管理功能
UDM :Unified Data Management统一数据管理
UPF :User Plane Function用户平面功能
# ZUF-79-02 服务化架构 
## ZUF-79-02-001 5G服务化架构 
特性描述 :特性描述 :术语 :术语|含义
---|---
SOA|Service-oriented architecture，面向服务的架构，是一个软件架构模型。服务是一个可以通过网络进行远程访问的独立功能单元，可以独立运作和升级。面向服务的架构要求以服务形态呈现功能，通过网络和定义良好的接口，将特定功能发布给用户或其他组件使用。
MSA|Microservice architecture，微服务架构，一种软件架构模型，是SOA架构的一种变化。在微服务架构中，服务被精细分割，使用轻量级的接口和网络传输协议。通过将应用切分成更小粒度的服务，可以提高模块化程度，并使得服务更容易被理解，更容易部署和测试，更多的可靠性和弹性。微服务架构支持功能持续发布和集成。
TMSP|Telecom Microservices Platform，电信级微服务平台，提供微服务运行环境，支持微服务生命周期管理。
描述 :定义 :SBA（Service Based Architecture，服务化架构）是3GPP定义的基于服务的架构体系，是全新的电信业务部署架构。SBA明确定义了5GC中需要呈现的服务，以及需要集中管理的数据上下文。
3GPP标准定义了SBA架构的如下内容。 
适当粒度的NF Service（将NF的功能进行服务化，简称NFS），以及关键数据的存储和访问模型。 
NF Service之间的交互由SBI接口完成。 
ZXUN uMAC采用SBA部署AMF，来实现核心网软件化、灵活化、开放化和智能化。
背景知识 :SBA是5G标准引入的新架构模型，在SOA和MSA之间取了平衡，其服务和数据对象的划分粒度位于两者之间，避免服务的功能集太庞大，业务变更困难；也避免服务的功能集划分过细，导致性能损失。
SBA更符合电信领域的业务部署要求，在提供功能独立性、重用性、弹性、健壮性、安全性的同时，也保证了业务处理性能。 
ZXUN uMAC实现符合3GPP SBA的要求，基于3GPP的定义提供服务，并提供了下列主要的服务化特性：
NF Service独立管理，NF Service之间无耦合，独立部署。 
NF Service自组织（self-contained），内部具备多并发，冗余，弹性，无状态特征，提供最大程度的鲁棒性。 
NF Service可重用性，业务逻辑独立，可以在用户接入流程变更和增强时保持NF Service重用。 
SBA的主要功能为： 
基于NF Service的版本管理。 
基于NF Service的编排。 
基于NF Service的资源管理。 
应用场景 :本特性无应用场景限制，适用于所有的5GC网络。 
客户收益 :受益方|受益描述
---|---
运营商|SBA细分了核心网的功能，统一接口协议，提供服务的动态发现和通告机制，简化网络运维管理复杂度，提升网络开放性，助力新业务部署。
终端用户|此特性对终端用户不可见。
实现原理 :系统架构 :3GPP标准规范定义的5GC服务化架构示意图如[图1]所示。
图1  5GC服务化架构

ZXUN uMAC相关的NF参见下表。
NF|说明
---|---
NSSF|网络切片选择功能，用于为用户选择为其提供网络服务的网络切片实例，如eMBB切片。
PCF|策略控制功能，支持统一策略控制框架，提供策略规则给其他NF，进行接入和移动性策略控制、会话策略控制、授权AF资源请求等处理。
NRF|NF存储功能，维护已部署NF信息，对NF发现请求进行应答。
UDM|统一数据管理，用于管理和存储签约及鉴权数据。
AMF|接入及移动性管理功能，完成用户的移动性管理，维护用户注册及连接状态、NAS SM信令路由、安全处理等。
SMF|会话管理功能，终结NAS SM信令，完成会话管理、UE IP地址分配及管理、UPF选择、会话策略控制等。
UPF|用户面转发功能，完成用户数据报文在RAN和外部网络间的转发。
AUSF|鉴权服务器功能，为其他NF提供用户鉴权功能。
NEF|网络能力暴露功能，为第三方、应用功能、边缘计算等提供5GC NF能力暴露。
UDSF|非结构化数据存储功能。
业务流程 :SBA架构下，ZXUN uMAC提供基于NF Service的编排和实例化，涉及的业务流程如[图2]所示。
图2  SBA架构编排流程图

流程说明如下。 
管理员将ZXUN uMAC的版本包上载到版本仓库中，版本包以服务/微服务粒度区分。
管理员在MANO的编排界面上创建NF。 
NFS编排功能从版本库中获取服务/微服务信息，用作编排。 
管理员根据版本库中可用的服务/微服务，编排NF内的服务化架构。 
管理员发起NF和NFS的实例化。 
MANO根据编排结果，从版本库中提取版本，实例化NF和NFS。
SBA架构下，实例化的服务和微服务各自具备独立的弹性和冗余可靠性。 
NF实现 :针对5GC架构，在NF层次下，3GPP协议进一步细分了NF对外提供的服务（NF Service）。 
为实现SBA架构的要求，ZXUN uMAC提供了服务化架构平台TMSP，平台支持服务和微服务粒度的部署与管理，并提取一些共性功能作为公共微服务，以协助各类服务的部署。
ZXUN uMAC对服务和微服务的定义如下：
服务的定义： 3GPP规范定义的NF Service，或厂商扩展的NF Service，能通过NRF完成注册和发现的网络服务，对外提供服务化接口，具备3GPP定义的服务特征。 
微服务的定义：基于云原生架构和电信业务特征，具备独立性和自组织能力的单一功能体，称之为微服务。微服务通过TMSP内部高效消息总线提供业务能力，协助NF
Service提供完整的服务功能。微服务是NF Service的组成部分，可被3GPP定义的NF Service专享或共享。 
ZXUN uMAC中NF的服务和微服务参见各个NF实现说明，ZXUN uMAC中提供的公共微服务参见[表1]。
公共微服务|说明
---|---
HTTP LB|支持SBI接口协议层的处理和负载均衡分发。
SIG LB|支持非SBI接口的各类信令协议处理和负载均衡分发，当网元支持2/3/4/5G业务融合部署时，SIG LB微服务也提供2/3/4G主要信令消息的处理和负载均衡分发。
IPS (IP Interface)|支持IP接口和路由转发功能。
AMF实现 :图3  AMF SBA架构图

AMF涉及的服务/微服务参见下表。 
服务/微服务|说明
---|---
服务|Communication|为其他NF提供访问UE和AN的能力。支持SMF发起的EBI分配请求，以便支持和EPS的互操作。
MT|服务|允许NF确认UE是可达的。
Event Exposure|服务|允许其他NF订阅并获取事件和统计信息通知，这些事件和统计与用户移动性相关。
Location|服务|向Communication服务和MT服务提供UE位置信息订阅和通知服务。
微服务|公共微服务|包括IPS微服务、HTTP LB微服务、SIG LB微服务，具体参见表1。
Resource Management|微服务|允许向Communication服务和MT服务提供NF内部资源管理，以及状态扫描和通知服务。
协议栈 :SBI接口使用HTTP/2协议，统一了信令接口的协议和操作行为，提供了接口功能扩展能力、接口访问性能自适应调整能力，以及接口安全互操作能力。
SBI接口协议栈如[图4]所示。
图4  SBI接口协议栈

系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
RFC|7540|Hypertext Transfer Protocol Version 2 (HTTP/2)
3GPP|23.501|System Architecture for the 5G System
3GPP|29.500|Technical Realization of Service Based Architecture
3GPP|29.501|Principles and Guidelines for Services Definition
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性是ZXUN uMAC的基本特性，无需License的支持。
对其他网元的要求 :该特性对其他网元无特殊要求。 
工程规划要求 :本特性对工程规划无特殊要求。 
O&M相关 :配置命令 :本特性不涉及配置命令的变化。 
定时器 :本特性不涉及定时器的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该特性不涉及配置。 
## ZUF-79-02-002 NF服务管理 
特性描述 :特性描述 :术语 :术语|含义
---|---
NF|在网络中，由3GPP采用或3GPP定义的处理功能，包括3GPP定义的功能行为和接口。
NF Service|是NF（NF服务生产者）通过基于服务的接口公开向其他授权NF（NF服务消费者）公开的一种能力。简单来说，NF服务向授权消费者提供了一种能力。
描述 :定义 :NF服务管理，是指： 
NF（例如：AMF）向NRF注册/更新/去注册，使NRF能正确地维护可用的NF实例及其支持的服务的信息； 
NF（例如：AMF）向NRF订阅其他NF的状态。 
背景知识 :在服务化架构下，5GC网络控制面的每一个NF（网络功能）都是基于“生产-消费”模型作为服务对授权的消费者（或者5GC网络内其他NF）提供业务能力。 
一个NF可以针对不同的消费者提供不同的功能，因此一个NF可以包含多个NF服务，同时这些NF服务是独立、可重用和可自我管理的。 
NRF是服务化架构的核心，通过NRF实现NF及NF服务的统一管理、互相发现及信息变更通知，整个过程全动态自动完成，无需人工参与。 
AMF作为5GC网络控制面中的一个NF，提供服务管理功能。AMF利用NRF统一管理AMF实例及其支持的服务，AMF也能向NRF订阅其他NF的状态。 
应用场景 :场景一：AMF通过向NRF注册/更新/去注册，由NRF为其统一提供管理服务。 
场景二：AMF通过向NRF订阅，从NRF获取其他NF/NFS实例信息变化的通知。 
客户收益 :受益方|受益描述
---|---
运营商|网络功能服务自动注册发现，简化网络配置，降低运维成本。
移动用户|此特性对终端用户不可见。
实现原理 :系统架构 :5GC网络中NF服务注册及发现架构，如[图1]所示。在该架构下AMF向NRF注册，NRF为AMF提供服务管理。
图1  NF服务注册及发现架构

涉及的NF/网元 :NF/网元名称|功能
---|---
AMF|向NRF自动注册/更新/去注册向NRF订阅其他NF的状态
NRF|接受AMF的注册/更新/去注册接收AMF的状态订阅，向AMF通知其订阅的其他NF的状态
协议栈 :接口|协议栈信息参考
---|---
Nnrf|ZUF-79-19-010 Nnrf
本NF/网元实现 :AMF实现的功能： 
向NRF注册/更新/去注册 
向NRF订阅其他NF的状态 
业务流程 :AMF服务注册
AMF服务注册流程参见[图2]。
图2  AMF服务注册流程

流程说明如下： 
AMF向NRF发送Nnrf_NFManagement_NFRegister_Request消息，请求注册AMF实例信息及支持的服务实例。 
NRF保存AMF实例信息及支持的服务实例信息，并标识该AMF可用。 
NRF向AMF返回Nnrf_NFManagement_NFRegister_Response消息。 
AMF服务更新
AMF服务更新流程参见[图3]。
图3  AMF服务更新流程

流程说明如下： 
AMF向NRF发送Nnrf_NFManagement_NFUpdate_Request消息，请求服务信息更新。 
NRF更新保存的AMF实例信息。 
NRF向AMF返回Nnrf_NFManagement_NFUpdate_Response消息，接受本次更新。 
AMF服务去注册
AMF服务去注册流程参见[图4]。
图4  AMF服务去注册流程

流程说明如下： 
AMF实例准备退出服务，向NRF发送Nnrf_NFManagement_NFDeregister_Request服务，请求去注册。 
NRF接受AMF退出服务的请求，标记该AMF不可用。 
NRF向AMF返回Nnrf_NFManagement_NFDeregister_Response消息，AMF退出服务。 
AMF状态订阅
AMF状态订阅流程参见[图5]。
图5  AMF状态订阅流程

流程说明如下： 
AMF向NRF发送Nnrf_NFManagement_NFStatusSubscribe_Request消息，请求订阅NF实例及包含服务的注册/更新/去注册。 
NRF保存订阅信息。 
NRF向AMF返回Nnrf_NFManagement_NFStatusSubscribe_Response消息。 
订阅NF实例及包含服务信息变更时，NRF向AMF发送Nnrf_NFManagement_NFStatusNotify_Request消息。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准名称|章节
---|---|---
3GPP|TS 23.501（System Architecture for the 5G System）|7.1.5
3GPP|TS 23.502（Procedures for the 5G System）|4.175.2.7
3GPP|TS 29.510（Network function repository services; Stage 3）|-
特性能力 :名称|指标
---|---
AMF上可配置的NRF地址最大个数|20（个）
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :NRF|NR
---|---
√|-
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项表1  新增配置命令配置项命令NRF心跳时长配置SET NRFHEARTBEATTIMERSHOW NRFHEARTBEATTIMERSERVICE关联HTTP服务端模板配置ADD ASSOCIATED HTTPSERVERPROFILEIDDEL ASSOCIATED HTTPSERVERPROFILEIDSHOW ASSOCIATED HTTPSERVERPROFILEIDSERVICE基本配置ADD SERVICECFGSET SERVICECFGDEL SERVICECFGSHOW SERVICECFGPLMN白名单配置ADD ALLOWEDPLMNSSET ALLOWEDPLMNSDEL ALLOWEDPLMNSSHOW ALLOWEDPLMNSNF类型白名单配置ADD ALLOWEDNFTYPESSET ALLOWEDNFTYPESDEL ALLOWEDNFTYPESSHOW ALLOWEDNFTYPESNF域白名单配置ADD ALLOWEDNFDOMAINSSET ALLOWEDNFDOMAINSDEL ALLOWEDNFDOMAINSSHOW ALLOWEDNFDOMAINSNF更新方式配置SET NFUPDATEMODESHOW NFUPDATEMODENRF地址配置ADD NRFNODECFGDEL NRFNODECFGSET NRFNODECFGSHOW NRFNODECFGNRF策略配置SET NRFPOLICYCFGSHOW NRFPOLICYCFG订阅有效时长配置SET NFSUBSCRIBEVALIDITYTIMESHOW NFSUBSCRIBEVALIDITYTIME 
动态管理表2  新增动态管理命令命令树配置项命令NRF相关NRF注册NRF REGISTRATIONNRF去注册NRF DEREGISTRATIONNRF更新NRF UPDATE 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过NF服务管理的相关配置，实现AMF向NRF注册/更新/去注册以及订阅功能。 
配置前提 :AMF各项对接和业务配置完毕。 
配置过程 :1.执行[ADD NRFNODECFG]命令配置NRF地址。
2. 执行[SET NRFPOLICYCFG]命令修改NRF策略。
3.执行[SET NFSUBSCRIBEVALIDITYTIME]命令修改NF订阅有效时长，时长范围为10~60000分钟。
4. 执行[SET NRFHEARTBEATTIMER]命令修改NRF心跳时长，时长范围为0~65535秒。
5. 执行[ADD ASSOCIATED HTTPSERVERPROFILEID]命令配置服务类型与HTTP服务端模板的关联关系。
6. 执行[ADD SERVICECFG]命令新增服务基本信息。
7. 执行[ADD NSIID]命令新增AMF NSI配置。
8. 执行[ADD ALLOWEDPLMNS]命令配置PLMN白名单。
9. 执行[ADD ALLOWEDNFTYPES]命令配置NF类型白名单。
10.执行[ADD ALLOWEDNFDOMAINS]命令配置NF域白名单。
11. 执行[SET NFUPDATEMODE]命令修改NF更新方式。
配置实例 :场景说明 :1. AMF部署完成，向NRF注册。 
2. AMF配置变更，向NRF发起更新。 
3. AMF向NRF去注册。 
4. AMF向NRF订阅。 
数据规划 :参数|取值
---|---
NRF地址|192.168.35.105
NF有效时长|600 s
NRF心跳时长|300 s
PLMN白名单|46011
网络切片实例|NSIID=1
配置步骤 :步骤|说明|操作
---|---|---
1|配置NRF地址|ADD NRFNODECFG:NRFNODELISTID=1,TYPECHOICE="ACTIVE",IPTYPE="IPV4",IPV4ADDR=192.168.35.105,PRIORITY=0,PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
2|配置NRF策略|SET NRFPOLICYCFG:LOCALAGINGTIME=5,NRFSWITCH=YES
3|配置NF订阅有效时长|SET NFSUBSCRIBEVALIDITYTIME:NFSUBVALIDITYTIME=600
4|配置NRF心跳时长|SET NRFHEARTBEATTIMER:NRFHEARTBEATTIMER=300
5|配置服务类型与HTTP服务端模板ID的关联关系|ADD ASSOCIATED HTTPSERVERPROFILEID:SERVICETYPE="COMMUNICATION",HTTPSERVERPROFILEID=5
6|配置服务基本信息|ADD SERVICECFG:SERVICETYPE="COMMUNICATION",VERSION=1,IPADDRTYPE="IPV4",PRIORITY=1,PRIORITYFLG="INVALID",CAPACITYFLG="INVALID"
7|配置网络切片实例|ADD NSIID:NSIID="1",NSSIID="1"
8|配置PLMN白名单|ADD ALLOWEDPLMNS:ID=1,SERVICETYPE="COMMUNICATION",MCC="460",MNC="11"
9|配置NF类型白名单|ADD ALLOWEDNFTYPES:ID=1,SERVICETYPE="COMMUNICATION",NFTYPE="AMF"
10|配置NF域白名单|ADD ALLOWEDNFDOMAINS:ID=1,SERVICETYPE="COMMUNICATION",NFDOMAIN="1"
11|配置NF更新方式|SET NFUPDATEMODE:UPDATEMETHOD="PUT",TRIGGERMODE="AUTOMATIC"
调整特性 :本特性不涉及调整特性。 
测试用例 :无 。 
常见问题处理 :无。 
## ZUF-79-02-003 NF服务发现 
特性描述 :特性描述 :术语 :术语|含义
---|---
网络切片|网络切片，是指提供特定网络功能和网络特征的逻辑网络。本质上就是将运营商的物理网络划分成多个虚拟网络，每一个虚拟网络根据不同的服务需求，比如延时、带宽、安全性和可靠性等来划分，以灵活地应对不同的网络应用场景。
NF|在网络中，由3GPP采用或3GPP定义的处理功能，包括3GPP定义的功能行为和接口。
NF服务|是NF（NF服务生产者）通过基于服务的接口公开向其他授权NF（NF服务消费者）公开的一种能力。简单来说，NF服务向授权消费者提供了一种能力。
NF服务操作|NF服务操作是NF服务组成的基本单位。
NF服务发现|5G核心网络内的NF可以通过其基于服务的接口将其能力展现为服务，之后可以由其他NF重新使用。NF服务发现使得NF能够发现提供期望的NF服务的NF实例。
NRF|网络仓储功能，负责服务发现、维护可用NF实例的信息及支持的服务。
描述 :定义 :NF服务发现：一个NF（AMF）作为消费者准备去消费另一个NF服务时，通过NF服务发现去发现NF服务提供者，并可以通过服务改变订阅通知向NRF订阅NF服务提供者的后续信息变化通知。 
背景知识 :在服务化架构下，5GC网络控制面的每一个NF都是基于“生产-消费”模型作为服务对授权的消费者（或者5GC网络内其他NF）提供业务能力。
一个NF可以针对不同的消费者提供不同的功能，因此一个NF可以包含多个NF服务，同时这些NF服务是独立、可重用和可自我管理的。 
NRF是服务化架构的核心，通过NRF实现NF及NF服务的统一管理、互相发现及信息变更通知，整个过程全动态自动完成，无需人工参与。NRF是NF的仓储功能，提供以下功能。
维护可用的NF实例信息及支持的NF服务。 
为其他NF提供目标NF或NF服务的发现服务。 
为其他NF提供信息变更的订阅通知服务。 
ZXUN uMAC在5GC网络内通过NRF可以实现与各个NF或NF服务间的动态发现，从而简化网络配置。
实现过程如[图1]所示。
NF服务注册：NRF通过本地配置或NF动态注册的方式获取各个NF实例及支持的NF服务的信息。 
NF服务发现：一个NF作为消费者准备去消费另一个NF服务时，通过NF服务发现去发现NF服务提供者，并可以通过服务改变订阅通知向NRF订阅NF服务提供者的后续信息变化通知。 
消费者将发现的NF服务缓存到本地。 
NF服务调用：一个NF成功发现NF服务提供者实例后，通过服务化接口来消费服务。 
图1  服务生产消费模型

应用场景 :###### 场景1：网络中NF的管理 
3GPP网络内的NF通过注册/更新/去注册流程，由NRF统一提供管理服务。 
NRF为其他NF（如：AMF）提供NF/NFS实例信息变化的订阅通知服务。 
###### 场景2：网络中NF/NFS的发现 
根据NRF提供服务层次的不同，可以提供如下三个层次的发现服务： 
PLMN级维护基于PLMN的NF/NF服务信息，为本PLMN内的NF（如：AMF）或其他PLMN的NF（如：AMF）提供发现服务。 
多切片共享级维护归属一组切片的NF/NF服务信息，为本组切片内的NF（如：AMF）或外部NF（如：AMF）提供发现服务。 
切片专属级维护某一个特定切片专属的NF/NF服务信息，为本切片内的NF（如：AMF）或外部NF（如：AMF）提供发现服务。 
客户收益 :受益方|受益描述
---|---
运营商|网络功能服务自动注册发现，简化网络配置，降低运维成本。
终端用户|此特性对终端用户不可见。
实现原理 :系统架构 :5GC网络中NF服务注册及发现架构，如[图2]所示。
图2  NF服务注册及发现架构

该架构下5GC网络中的NF服务向NRF注册，NRF为这些NF服务提供互相发现的服务，N27接口是拜访网络NRF和归属网络NRF之间的接口。 
涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|NRF|接受网络中其他NF的注册/更新/去注册。为其他NF提供发现服务。服务消费者与服务提供者分别部署在不同的PLMN时，通过NRF进行中转。
AMF|NF|向NRF自动注册/更新/去注册。作为消费者向NRF请求发现服务提供者。
业务流程 :####### NF服务注册流程 
图3  NF服务注册流程（NF service registration）

流程说明如下： 
NF Service Consumer（AMF）向NRF发送Nnrf_NFManagement_NFRegister_Request消息，请求注册本NF Service Consumer（AMF）实例信息及支持的NF服务实例。 
NRF保存NF Service Consumer（AMF）实例信息及支持的AMF服务实例信息，并标识该NF Service Consumer（AMF）可用。
NRF向NF Service Consumer（AMF）发送Nnrf_NFManagement_NFRegister_Response消息。 
####### NF服务更新流程 
图4  NF服务更新流程（NF service update）

流程说明如下： 
NF Service Consumer（AMF）向NRF发送Nnrf_NFManagement_NFUpdate_Request消息，请求服务信息更新。 
NRF更新保存的NF Service Consumer（AMF）实例信息。
NRF向NF Service Consumer（AMF）发Nnrf_NFManagement_NFUpdate_Response消息，接受本次更新。 
####### NF服务去注册流程 
图5  NF服务去注册流程（NF service deregistration）

流程说明如下： 
NF Service Consumer（AMF）实例准备退出服务，向NRF发送Nnrf_NFManagement_NFDeregister_Request消息，请求去注册。 
NRF接受NF Service Consumer（AMF）退出服务的请求，标记该NF Service Consumer（AMF）不可用。
NRF向AMF发Nnrf_NFManagement_NFDeregister_Response消息，NF Service Consumer（AMF）退出服务。 
####### NF或NF服务的发现流程 
图6  NF或NF服务发现流程（NF/NF service discovery）

流程说明如下： 
NF Service Consumer（AMF）需要发现目标NF服务，向NRF发送Nnrf_NFDiscovery_Request消息，请求发现目标NF服务。 
如果NRF的服务PLMN与归属PLMN不一致，服务PLMN中的NRF根据请求消息中携带的PLMN来获取归属PLMN的NRF地址，将该发现请求转发给归属PLMN的NRF，归属PLMN中的NRF基于请求的服务参数查询到匹配的NF服务实例，向请求NRF发送Nnrf_NFDiscovery_Response消息。 
服务PLMN中的NRF向请求NF Service Consumer（AMF）发送Nnrf_NFDiscovery_Response消息。 
####### NF或NF服务的状态订阅通知流程 
图7  NF或NF服务状态订阅通知流程（NF/NF service status subscribe/notify）

流程说明如下： 
服务PLMN中的NF Service Consumer（AMF）向NRF发送Nnrf_NFManagement_NFStatusSubscribe_Request消息，请求订阅NF实例及包含服务的注册/更新/去注册。 
如果NRF的服务PLMN与归属PLMN不一致，服务PLMN中的NRF根据请求消息中携带的PLMN来获取归属PLMN的NRF地址，将该请求转发给归属PLMN的NRF，归属PLMN中的NRF保存订阅信息，向请求NRF发送Nnrf_NFManagement_NFStatusSubscribe_Response消息。 
服务PLMN中的NRF向请求NF Service Consumer（AMF）发送Nnrf_NFManagement_NFStatusSubscribe_Response消息。 
订阅NF实例及包含服务信息变更时，NRF向订阅NF Service Consumer（AMF）发送Nnrf_NFManagement_NFStatusNotify_Request消息。 
NF实现 :####### NRF实现 
AMF实现 :对外提供NF管理服务。 
对外提供NF发现服务。 
NRF指定了以下NF服务，参见[表1]。
服务名称|描述
---|---
Nnrf_NFManagement|为NF、NF服务提供注册表、注销和更新服务的支持。向消费者提供新注册的NF及其NF服务的通知。
Nnrf_NFDiscovery|使一个NF服务消费者发现具有特定NF服务或目标NF类型的一组NF实例。还允许一个NF服务发现特定的NF服务。
向NRF注册/更新/去注册网络功能服务，用于NRF对AMF进行统一管理。 
向NRF请求发现其他网络功能服务，用于NF间通讯。 
协议栈 :####### Nnrf接口协议栈 
Nnrf接口是NRF和其他NF（如：AMF）或NRF和NRF之间的接口，用于网络功能服务管理及发现，接口协议栈如[图8]所示。
图8  Nnrf接口协议栈

系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501 System Architecture for the 5G System|7.1.3 Network Function Service discovery
3GPP|3GPP TS 23.502 Procedures for the 5G System|4.17.4 NF/NF service discovery by NF service consumer in the same PLMN4.17.5 NF/NF service discovery across PLMNs in the case of discovery made by NF service consumer
3GPP|3GPP TS 29.510 Network function repository services|5.3 Nnrf_NFDiscovery Service
特性能力 :名称|指标
---|---
单NRF支持注册NF的实例数|10000（个）
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :NRF|NR
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :在一个NRF的管理域内，规划的NF数目不能超过10000条。
O&M相关 :配置命令 :新增配置命令配置项命令NRF发现AUSF参数配置SET NRFDISCAUSFPARACFGSHOW NRFDISCAUSFPARACFGNRF发现PCF参数配置SET NRFDISCPCFPARACFGSHOW NRFDISCPCFPARACFGNRF发现SMF参数配置SET NRFDISCSMFPARACFGSHOW NRFDISCSMFPARACFGNRF发现UDM参数配置SET NRFDISCUDMPARACFGSHOW NRFDISCUDMPARACFGNRF发现AMF参数配置SET NRFDISCAMFPARACFGSHOW NRFDISCAMFPARACFGNRF发现SMSF参数配置SET NRFDISCAMFPARACFGSHOW NRFDISCSMSFPARACFGNF发现模式配置SET NFDISCOVERYMODE CONFIGSHOW NFDISCOVERYMODE CONFIG查询结果缓存配置SHOW NFDISCOVERYRESULTCACHEDSET NFDISCOVERYRESULTCACHED 
动态管理配置项命令NF发现NF DISCOVERY 
定时器 :本特性不涉及定时器的变化。 
性能统计 :告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该特性无需配置即可实现。 
特殊场景下根据需要执行可选步骤（参见配置过程），以实现AMF发现其它NF时采用特定的发现模式，并控制是否携带特定参数。
配置前提 :NF和NRF运行正常。 
#### 配置过程（可选） 
（可选）通过[SET NFDISCOVERYMODE CONFIG]命令，修改NF发现模式。
（可选）通过[SET NRFDISCAUSFPARACFG]命令，修改AMF通过NRF发现AUSF的参数配置。
（可选）通过[SET NRFDISCPCFPARACFG]命令，修改AMF通过NRF发现PCF的参数配置。
（可选）通过[SET NRFDISCSMFPARACFG]命令，修改AMF通过NRF发现SMF的参数配置。
（可选）通过[SET NRFDISCUDMPARACFG]命令，修改AMF通过NRF发现UDM的参数配置。
（可选）通过[SET NRFDISCAMFPARACFG]命令，修改AMF通过NRF发现AMF的参数配置。
（可选）通过[SET NRFDISCSMSFPARACFG]命令，修改AMF通过NRF发现SMSF的参数配置。
（可选）通过[SET NFDISCOVERYRESULTCACHED]命令，修改发现结果是否缓存。
配置实例 :场景说明 :AMF选择SMF时，需要选择与AMF部署在同一数据中心的SMF。 
数据规划 :无。 
配置步骤 :步骤|说明|操作
---|---|---
1|配置AMF发现SMF参数，设置携带LOCALITY为支持。|SET NRFDISCSMFPARACFG:CARRYLOCALITY="SupLocality"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|服务注册
---|---
测试目的|验证AMF能够正确发现SMF。
预置条件|NF部署成功NRF状态正常SMF已注册成功
测试过程|NF实例正常后，SMF注册成功后，AMF携带相关参数向NRF发现SMF。
通过准则|根据NRF返回的发现结果，验证是否符合预期，即发现的SMF所支持的参数与发现请求所携带的信息一致。
测试结果|-
常见问题处理 :无。 
# 缩略语 
# 缩略语 
5GC :5G Core Network5G核心网
AMF :Access and Mobility Management Function接入和移动管理功能
AUSF :Authentication Server Function鉴权服务器功能
## EBI 
EPS Bearer IDEPS承载标识
EPS :Evolved Packet System演进的分组系统
## MSA 
Micro Service Architecture微服务架构
NEF :Network Exposure Function网络开放功能
NF :Network Function网络功能
NFS :Network Function Service网络功能服务
NRF :NF Repository Function网络功能仓储
## NSI 
Network Slice Instance网络切片实例
NSSF :Network Slice Selection Function网络切片选择功能
PCF :Policy Control Function策略控制功能
PLMN :Public Land Mobile Network公共陆地移动网
## SBA 
Service Based Architecture基于服务的架构
## SBI 
Service Based Interface基于服务的接口
SMF :Service Management Function业务管理功能
## SOA 
Service Oriented Architecture面向服务的架构
## TMSP 
Telecom Microservices Platform电信级微服务平台
UDM :Unified Data Management统一数据管理
UDSF :Unstructured Data Storage Function非结构化数据存储功能
UPF :User Plane Function用户平面功能
# ZUF-79-03 注册及移动性管理 
## ZUF-79-03-001 注册 
特性描述 :特性描述 :术语 :本特性不涉及相关术语。 
描述 :定义 :注册流程包括初始注册和移动注册更新两个过程： 
初始注册是指用户为了使用5G业务需要先注册到5GS并获得授权的过程。 
移动注册更新是初始注册完成后，进行注册信息更新的过程。通过移动注册更新过程，保持5G网络对用户进行移动性跟踪并保证用户可达性。 
背景知识 :注册流程对于5G网络有着重要意义，体现在以下几个方面： 
注册流程是一切5G业务的基础：5G终端为享受5G丰富多彩的业务，需要通过授权接入5GS，这一过程通过注册流程实现。 
注册流程是持续提供5G服务的基础：在注册过程中5GC会为UE分配注册区域（跟踪区域列表，即TA List）。当5G终端移动出注册区域时，需要主动发起注册更新流程，使5GC为UE分配新的注册区域。通过注册更新流程实现对用户的移动性跟踪，保证5G网络可持续为终端提供服务。 
注册流程是保证用户可达的基础：注册完成后，无业务需要处理时，为了节电，终端可能会释放与5G网络的连接。为避免终端与网络失去联系，终端需要周期性触发注册更新流程，网络侧可以在需要时与终端联系，保证终端可达。 
应用场景 :注册流程是5G基本流程，典型场景包括如下四种： 
###### 场景1：初始注册，接入5G网络 
终端插入新的SIM卡并开机触发的初始注册。 
终端重新开机触发的初始注册。 
终端从其他网络重选到5G网络触发的初始注册。 
###### 场景2：周期性注册，保证用户可达 
为避免终端与网络失去联系，终端与网络协商周期性更新定时器，定时器超时触发周期性注册更新。 
###### 场景3：用户移动，更新注册区域 
终端移动出5G网络为其分配的注册区域时触发移动注册更新，更新注册区域，保证5G网络可持续为用户提供服务。 
###### 场景4：终端能力更新 
终端能力发生改变（比如，开启了IMS语音功能）触发移动注册更新，网络基于最新的终端能力为用户提供服务。 
客户收益 :受益方|受益描述
---|---
运营商|本特性支持合法的本地用户/漫游用户注册到运营商网络，是运营商向用户提供数据/语音业务的基础条件。通过注册过程中的终端合法性认证，可避免非法用户占用运营商网络资源。
终端用户|此特性对终端用户不可见。
实现原理 :

系统架构 :



终端接入5GC网络注册过程的组网结构如[图1]所示。


图1  系统架构






注册流程涉及的NF/网元参见下表。 


NF/网元名称|说明
---|---
NF|AMF|注册流程主处理NF，与UE/RAN/UDM/UDR/PCF/SMF/UPF协作完成注册过程。
NF|AUSF|鉴权服务处理NF，注册过程中与UE/AMF/UDM/UDR协作完成用户的鉴权过程。
NF|UDM|用户签约信息处理NF，注册过程中与UDR配合向AUSF/AMF等提供用户签约数据。
NF|EIR|设备标识检查NF，用于检查终端设备标识PEI是否合法。
NF|PCF|用户策略控制NF，注册过程中与UDR配合向AMF提供用户策略控制数据。
NF|SMF|用户会话管理NF，注册更新过程中，如果存在用户会话上下文，可根据UE指示触发用户面隧道建立。
NF|UPF|用户数据转发NF，注册更新过程中，如果存在用户会话上下文，可根据SMF指示建立用户面隧道。
NF|NRF|网络功能数据仓储NF，注册过程中提供NF发现功能。
NF|NSSF|网络切片选择NF，注册过程中提供切片选择功能。
网元|(R)AN|无线接入网络，注册过程中与UE建立无线连接，与AMF建立N2连接，用于中转N1 NAS信令。注册更新过程中，如果存在用户会话上下文，可根据SMF指示建立与UPF间的用户面隧道。
网元|UE|支持5G接入的终端，注册流程的发起方。




业务流程 :####### 普通注册流程 
普通注册流程如[图2]所示。
图2  普通注册流程

流程说明如下： 
UE发送Registration Request到(R)AN，消息中包含注册类型、用户标识、UE的5GC能力及可选的Requested NSSAI等参数。
(R)AN接收到消息，根据用户临时标识或Requested NSSAI选择合适的AMF，如果(R)AN无法选择到合适的AMF，则将Registration Request发送给缺省AMF，由缺省AMF进行AMF选择过程。
(R)AN将Registration Request消息转发给AMF。 
（可选）如果Registration Request中携带的是5G-GUTI，并且AMF检测到5G-GUTI不是本局分配的，AMF会调用Old AMF的服务化接口Namf_Communication_UEContextTransfer请求用户的SUPI和MM Context，请求消息中包含完整的注册请求NAS消息，Old AMF对请求消息中携带的NAS消息进行完整性检查。
（可选）Old AMF响应New AMF调用的服务化接口Namf_Communication_UEContextTransfer，参数包括SUPI、UE上下文等信息。 
（可选）如果UE没有提供SUCI，也没有从Old AMF处获取到SUPI，AMF向UE发送Identity Request消息请求获取SUCI。
（可选）UE向AMF返回Identity Response消息，消息中包含SUCI。
（可选）如果AMF没有用户上下文，或者Registration
Request消息没有被完整性保护，或者完整性检查失败，AMF会调用AUSF服务发起UE鉴权过程。这时AMF会根据routing ind选择一个AUSF。
AUSF执行对UE的鉴权过程。
（可选）如果AMF改变，New AMF调用Old AMF的服务化接口Namf_Communication_RegistrationCompleteNotify，通知Old
AMF收到MM Context。 
（可选）AMF向UE发送Identity Request消息，请求获取PEI。UE向AMF返回Identity Response消息包含PEI。 
（可选）AMF通过服务化接口消息N5g-eir_EquipmentIdentityCheck_Get向EIR发起IMEI检查过程，EIR向AMF返回检查结果响应。
（可选）如果第14步需要执行，则New AMF根据SUPI选择一个UDM实例。
New AMF及Old AMF分别执行如下操作： 
如果AMF改变，或者如果AMF没有用户的有效的上下文，AMF需要向UDM注册并获取签约数据。AMF调用UDM的服务化接口Nudm_UECM_Registration向UDM注册，以及订阅当UDM去注册这个AMF时UDM向AMF发送的变更通知。 
AMF调用UDM的服务化接口Nudm_SDM_Get获取签约数据。 
AMF获取签约数据成功后，通过Nudm_SDM_Subscribe向UDM订阅签约数据变更通知。 
New AMF向UDM注册成功后，UDM向Old AMF发送Nudm_UECM_DeregistrationNotify通知，携带通知原因值。 
Old AMF调用UDM的服务化接口Nudm_SDM_Unsubscribe取消签约数据订阅。 
（可选）如果AMF决定与PCF通信，则AMF选择一个PCF实例。
（可选）New AMF向PCF发起一个策略关联建立过程。 
（可选）PCF调用AMF的服务化接口Namf_EventExposure_Subscribe向AMF请求订阅该UE移动性管理相关的事件变化通知。
（可选）如果AMF改变或UE的PDU Session Status与AMF保存的不一致，AMF调用SMF的服务化接口Nsmf_PDUSession_UpdateSMContext通知SMF更新AMF信息或释放不一致的PDU会话。 
（可选）如果Old AMF已与PCF建立关联且没有将PCF ID传递给New AMF，AMF发起策略关联终止过程。 
New AMF向UE发送Registration Accept消息，接受UE发起的注册请求。如果New AMF为UE分配了新的5G-GUTI，则需要在本消息中携带。 
（可选）如果AMF为UE分配了新的5G-GUTI，则UE向New AMF发送Registration Complete消息。 
####### AMF重分配流程 
AMF重分配流程如[图3]所示。
图3  AMF重分配流程

流程说明如下： 
对应[普通注册流程]的步骤1~3，Initial AMF已经收到Registration Request消息。
（可选）如果需要执行安全流程，则对应[普通注册流程]的步骤4~9。
（可选）如果Initial AMF需要根据UE签约数据判断是否需要重分配AMF，且Initial AMF没有从Old
AMF获取到切片签约信息，但需要基于切片签约信息进行AMF切片选择，则： 
Initial AMF选择一个合适的UDM。
Initial AMF调用UDM的服务化接口Nudm_SDM_Get向UDM请求获取签约切片选择信息。 
UDM向AMF返回签约切片选择信息，包含签约的一组S-NSSAI。
（可选）如Initial AMF果已获取到签约的切片信息，则： 
Initial AMF调用NSSF的服务化接口Nnssf_NSSelection_Get进行切片选择。 
NSSF向Intial AMF返回Allowed NSSAI及支持这些NSSAI的对应的AMF Set或AMF地址列表。
（可选）Initial AMF向old AMF发送Namf_Communication_RegistrationCompleteNotify消息并携带失败指示。 
Initial AMF根据NSSF返回的AMF Set或AMF地址列表判断需要将NAS消息（Registration Request）重路由给其他AMF处理。
Initial AMF向Old AMF发送拒绝指示，通知UE在Initial AMF处的注册流程还未完全结束。Old AMF保持没有收到Namf_Communication_UEContextTransfer消息之前的状态不变。 
（可选）如果NSSF没有返回AMF地址列表，且Initial AMF准备将NAS消息直接路由给Target AMF，则： 
Initial AMF调用NRF的服务化接口Nnrf_NFDiscovery_Request（包含AMF
Set信息）请求获取Target AMF地址列表。
NRF返回对应的Target AMF列表及对应的地址。 
(A) 如果AMF基于本地策略决定将NAS消息直接路由给Target AMF，则： 

a. Initial
AMF调用Target AMF的服务化接口Namf_Communication_N1MessageNotify将NAS消息传递给Target
AMF，通过步骤8在Target AMF发送给(R)AN的第一条消息中更新N2端点信息。 
(B)如果AMF基于本地策略决定将NAS消息通过(R)AN路由给Target
AMF，则： 
Initial AMF向(R)AN发送Reroute NAS Request消息并包含NAS消息。 
(R)AN通过Initial UE Message将NAS消息传递给Target AMF。 
如果Target AMF已经从initial AMF获取到UE上下文，则继续执行[普通注册流程]的步骤9，11~21；如果Target AMF没有从initial AMF获取到UE上下文，则继续执行[普通注册流程]的步骤4~21。


NF实现 :



AMF实现 :
 
与UE交互，完成注册消息交互。 

 
与NR-RAN交互，完成NAS消息的传递。 

 
AMF间交互，完成UE上下文传递。 

 
与PCF交互，完成PCF策略关联。 

 
与SMF交互，完成PDU会话更新。 

 
与AUSF交互，完成鉴权。 

 
与UDM交互，完成UE注册/去注册及签约信息获取。 

 




协议栈 :该特性涉及的接口协议栈参见[表1]。
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N12|ZUF-79-19-005 N12
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15
N22|ZUF-79-19-008 N22
系统影响 :该特性不涉及对系统的影响。 
应用限制 :暂不支持non-3GPP接入方式。 
暂不支持与5G-EIR交互进行IMEI检查过程。 
特性交互 :相关特性|交互关系
---|---
ZUF-79-09-001 支持用户接入网络切片|注册过程中，如果AMF没有获取到切片签约信息，需要触发AMF切片选择流程。
ZUF-79-10-001 SMF选择ZUF-79-10-003 UDM选择ZUF-79-10-004 PCF选择|注册过程中，如果AMF没有其他NF的地址信息，需要触发NRF发现流程。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|System Architecture for the 5G System
TS 23.502|3GPP|Procedures for the 5G System
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
TS 29.502|3GPP|Session Management Services; Stage 3
TS 29.503|3GPP|Unified Data Management Services; Stage 3
TS 29.507|3GPP|Access and Mobility Policy Control Service; Stage 3
TS 29.509|3GPP|Authentication Server Services; Stage 3
TS 29.510|3GPP|Network function repository services; Stage 3
TS 29.511|3GPP|Equipment Identity Register Services; Stage 3
TS 29.514|3GPP|Policy Authorization Service; Stage 3
TS 29.531|3GPP|Network Slice Selection Services; Stage 3
TS 29.518|3GPP|5G System; Access and Mobility ManagementServices
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需license支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及。 
O&M相关 :配置命令 :新增的配置命令参见下表。 
配置项|命令
---|---
AMF本局配置|SET AMFLOCALOFFICECFG
SHOW AMFLOCALOFFICECFG|AMF本局配置
NRF地址配置|ADD NRFNODECFG
DEL NRFNODECFG|NRF地址配置
SET NRFNODECFG|NRF地址配置
SHOW NRFNODECFG|NRF地址配置
NRF地址模板配置|ADD NRFNODETEMPCFG
DEL NRFNODETEMPCFG|NRF地址模板配置
SET NRFNODETEMPCFG|NRF地址模板配置
SHOW NRFNODETEMPCFG|NRF地址模板配置
AMF支持切片选择配置|SET AMFSUPPOTSLICESELECT
SHOW AMFSUPPOTSLICESELECT|AMF支持切片选择配置
定时器 :本特性不涉及定时器的变化。 
性能统计 :新增性能计数器参见下表。 
测量类型|描述
---|---
初始注册流程测量|编号为51001开头的所有计数器
注册更新流程测量|编号为51002开头的所有计数器
注册流程分NF测量|编号为51030开头的所有计数器
基于TA初始注册流程测量|编号为51100开头的所有计数器
用户数测量|编号为51350开头的所有计数器
基于SNSSAI初始注册流程测量|编号为51143开头的所有计数器
基于SNSSAI注册更新流程测量|编号为51144开头的所有计数器
基于SNSSAI的用户数测量|编号为51355开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本特性无需特殊配置，完成初始配置后即可使用。 
测试用例 :测试项目|初始注册
---|---
测试目的|AMF支持初始注册流程
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5G模式，并处于RM-DEREGISTERED状态
测试过程|UE开机发起注册流程
通过准则|UE发起初始注册流程，Registration request中包含的Registration type应为InitialRegistrationUE注册成功，用户处于RM-REGISTERED状态AMF分配5G-GUTI给UE
测试结果|-
测试项目|移动性注册更新
---|---
测试目的|AMF支持移动性注册更新流程
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5G模式，并已成功注册到AMF
测试过程|UE移动到新的TA后，发起移动性注册更新流程
通过准则|UE发起移动性注册更新流程，Registration request中包含的Registration type应为MobilityRegistration UpdateUE移动性注册成功，用户处于RM-REGISTERED状态AMF正确更新UE的位置信息
测试结果|-
测试项目|周期性更新
---|---
测试目的|AMF周期性注册更新流程
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5G模式，并已成功注册到AMF
测试过程|UE周期性定时器到期后，发起周期性注册更新流程
通过准则|UE发起周期性注册更新流程，Registration request中包含的Registration type应为PeriodRegistration UpdateUE周期性注册成功，用户处于RM-REGISTERED状态
测试结果|-
## ZUF-79-03-002 去注册 
特性描述 :特性描述 :术语 :本特性不涉及相关术语。 
描述 :定义 :去注册流程是指用户从5G网络上注销的流程。在去注册过程中，会删除为用户建立的所有PDU会话，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为去注册态。 
从发起去注册流程的主体角度来说，去注册流程包括UE发起的去注册流程、网络侧发起的去注册流程。 
UE发起的去注册：用户不再使用5G业务，从5GC网络上注销的过程。 
网络侧发起的去注册：核心网不再让UE使用5G业务，把UE从5GC网络上注销的过程。 
从是否需要显式通知UE分离的角度来说，去注册流程包括显式去注册流程和隐式去注册流程。 
显式去注册流程：核心网和UE之间有显式的去注册消息通知。 
隐式去注册流程：AMF检测到UE长时间没有和5GC网络交互，触发网络侧发起的去注册流程，不通知UE。 
去注册流程完成之后，用户不能再通过5GC网络访问数据业务和其他业务。 
背景知识 :去注册流程是5GC网络的基本功能，对于5GC网络有着重要意义，体现在： 
节约网络资源：支持用户从运营商的5G网络上注销，可以节约运营商的5G网络资源。 
加强用户管理：可以通过对欠费用户或销卡用户进行强制注销，加强运营商对用户的管理，避免欠费或销卡用户非法继续使用网络资源。 
应用场景 :去注册流程是5G基本流程，典型场景包括如下五种： 
用户关机。 
用户欠费停机。 
用户注销/销卡。 
运营商进行网络维护，把用户强制从5GC网络上去注册。 
用户长时间驻留在无线信号极差的地方。 
客户收益 :受益方|受益描述
---|---
运营商|节省资源：将不再需要使用5G网络的用户注销，避免接入5G网络的用户无限膨胀。用户管理：对欠费用户或销卡用户进行强制注销，加强运营商对用户的管理，避免欠费或销卡用户非法继续使用网络资源。
终端用户|此特性对终端用户不可见。
实现原理 :

系统架构 :



本特性涉及的系统架构如[图1]所示。


图1  系统架构






去注册流程涉及的NF/网元参见下表。 


NF/网元名称|说明
---|---
NF|AMF|去注册流程主处理NF，与UE/RAN/UDM/UDR/PCF/SMF/UPF协作完成去注册过程。
NF|UDM|用户签约信息处理NF，去注册过程中被通知不再订阅用户签约数据改变等事件。
NF|PCF|用户策略控制NF，去注册过程中该用户的AMF与PCF间会话被释放。
NF|SMF|用户会话管理NF，去注册过程中，如果存在用户会话上下文，则释放存在的PDU会话资源。
NF|UPF|用户数据转发NF，去注册过程中，如果存在用户会话上下文，则释放用户面资源。
网元|(R)AN|无线接入网络，去注册过程中释放与UE建立的无线连接。
网元|UE|支持5G接入的终端，去注册流程的发起方之一。






业务流程 :



####### UE发起的去注册流程 
UE发起的去注册流程如[图2]所示。
图2  UE发起的去注册




流程说明如下： 


UE发送去注册请求消息给AMF，消息中携带5G-GUTI、Deregistration type、Access Type等信息。Deregistration
type指示是否关机。Access Type指示是3GPP接入下去注册、非3GPP接入下去注册，或者两种接入方式下都去注册。 


如果UE在需要去注册的Access Type下没有已建立的PDU会话，则跳过第2步至第5步。 
如果UE在需要去注册的Access
Type下有已建立的PDU会话，则AMF给SMF发送Nsmf_PDUSession_ReleaseSMContext Request消息，消息中携带SUPI、PDU
Session ID等信息。 


SMF释放PDU会话资源（如IP address / Prefix(es)和会话上下文），并通知UPF释放用户面资源。 


SMF给UPF发送N4会话释放请求消息，消息中携带N4 Session ID等信息。UPF将丢弃所有该PDU会话的缓存报文，释放PDU会话相关的所有资源。 


UPF给SMF返回N4会话释放响应消息。 




SMF给AMF返回Nsmf_PDUSession_ReleaseSMContext Response消息。 


SMF释放与PCF间会话资源，退订UDM会话管理签约数据改变通知事件。 


如果动态PCC被应用，SMF完成会话管理策略终止过程。 


SMF通过Nudm_SDM_Unsubscribe服务，通知UDM退订会话管理签约数据改变通知事件。 


SMF通过Nudm_UECM_Deregistration服务，通知UDM删除SMF标识、SMF地址、DNN、PDU
Session ID等信息。 




AMF释放与PCF间会话资源，退订UDM签约数据改变通知事件。 


如果存在该UE与PCF的会话，且UE在任何接入下已不再注册到网络，则AMF完成AMF发起的AM策略关联终止过程，删除该UE与PCF的会话。


如果存在该UE与PCF的会话，且UE在任何接入下已不再注册到网络，则AMF完成AMF发起的UE策略关联终止过程，删除该UE与PCF的会话。




如果Deregistration type指示不是关机，则AMF给UE发送去注册接受消息。 
如果Deregistration
type指示为关机，则AMF不会向UE发送去注册接受消息。 


AMF通知(R)AN释放N2 UE上下文。 




####### 网络侧发起的去注册流程 
网络侧发起的去注册流程如[图3]所示。
图3  网络侧发起的去注册




流程说明如下： 


UDM请求删除用户注册管理上下文和PDU会话，则UDM将发送Nudm_UECM_DeregistrationNotification消息给AMF，消息中携带SUPI，Access Type，Removal Reason等信息。
Access Type指示是3GPP接入下去注册、非3GPP接入下去注册，或者两种接入方式下都去注册。Removal Reason指示销户。 


如果是UDM触发的去注册，AMF执行去注册流程。AMF发起的去注册过程可以是显式去注册或隐式去注册。 

 
对于隐式去注册，AMF不给UE发送去注册请求消息。 

 
如果UE处于连接态，AMF使用显式去注册方式，给UE发送去注册请求消息，消息中携带Deregistration type，Access
Type等信息。Deregistration type指示UE在去注册后是否需要重注册。 

 
如果UE处于空闲态，AMF使用显式去注册方式，则AMF寻呼UE。 

 


如果去注册流程由UDM触发，那么AMF向UDM返回Nudm_UECM_DeRegistrationNotification确认消息。 
3a. AMF通过Nudm_SDM_Unsubscribe服务，通知UDM退订接入和移动签约数据改变通知事件、SMF选择签约数据改变通知事件。 


如果UE在需去注册的Access Type下已建立PDU会话，则执行UE发起的去注册流程的第2步到第5步。 


如果存在该UE的与PCF的会话，且UE在任何接入下已不再注册到网络，则： 


AMF完成AMF发起的AM策略关联终止过程，删除该UE与PCF的会话。 


AMF完成AMF发起的UE策略关联终止过程，删除该UE与PCF的会话。 




如果UE收到了去注册请求消息，则UE给AMF返回去注册接受消息。 


AMF通知(R)AN释放N2 UE上下文。 






协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15


NF实现 :



AMF实现 :
 
与UE交互，完成去注册消息交互。 

 
与(R)AN交互，完成NAS消息的传递和N2 UE上下文释放。 

 
与PCF交互，释放PCF策略关联。 

 
与SMF交互，释放PDU会话。 

 
与UDM交互，完成退订用户签约数据变更通知事件或UDM触发的去注册通知。 

 




系统影响 :该特性不涉及对系统的影响。 
应用限制 :暂不支持non-3GPP接入方式。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|System Architecture for the 5G System
TS 23.502|3GPP|Procedures for the 5G System
TS 23.503|3GPP|Policy and Charging Control Framework for the 5G System (R15)
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage3
TS 29.502|3GPP|Session Management Services; Stage 3
TS 29.503|3GPP|Unified Data Management Services; Stage 3
TS 29.504|3GPP|5G System; UnifiedData Repository Services; Stage 3
TS 29.505|3GPP|5G System; Usageof the Unified Data Repository services for Subscription Data; Stage3
TS 29.507|3GPP|Access and Mobility Policy Control Service; Stage 3
TS 29.508|3GPP|5G System; SessionManagement Event Exposure Service; Stage 3
TS 29.512|3GPP|5G System; SessionManagement Policy Control Service; Stage 3
TS 29.513|3GPP|5G System; Policyand Charging Control signalling flows and QoS parameter mapping; Stage3
TS 29.518|3GPP|5G System; Access and Mobility Management Services
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需license支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及。 
O&M相关 :配置命令 :本特性不涉及配置命令的变化。 
定时器 :本特性不涉及计数器的变化。 
性能统计 :####### AMF性能统计 
测量类型|描述
---|---
去注册流程测量|编号为51003开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本特性无需特殊配置，完成初始配置后即可使用。 
测试用例 :测试项目|UE通过非关机方式发起去注册流程
---|---
测试目的|AMF支持UE发起的去注册流程
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5G模式，并已成功注册到AMF
测试过程|UE通过非关机方式发起去注册流程
通过准则|UE发起去注册流程，且Deregistration type应为normal deregistrationUE去注册成功，用户处于RM-DEREGISTERED状态
测试结果|-
测试项目|UE通过关机方式发起去注册流程
---|---
测试目的|AMF支持UE发起的去注册流程
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5G模式，并已成功注册到AMF
测试过程|UE通过关机方式发起去注册流程
通过准则|UE发起去注册流程，且Deregistration type应为Switch offUE去注册成功，用户处于RM-DEREGISTERED状态
测试结果|-
测试项目|网络侧发起的去注册
---|---
测试目的|AMF支持网络侧发起的去注册流程
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5G模式，并已成功注册到AMF
测试过程|通过UDM或AMF触发对UE的去注册流程
通过准则|UE去注册成功，用户处于RM-DEREGISTERED状态
测试结果|-
## ZUF-79-03-003 注册区域管理 
概述 :本特性提供一种合理管理AMF中跟踪区域的方法以减少更新注册的次数。 
客户收益 :通过跟踪区域列表管理功能，AMF可以对TA进行合理高效的管理。 
说明 :注册区域管理是指为UE分配和重新分配注册区域。当UE通过3GPP接入注册到网络时，AMF为UE分配一个TAI列表，包含一组作为注册区域的跟踪区域，所以UE在TA列表中移动时不需要更新移动注册。 
## ZUF-79-03-004 用户数据管理 
概述 :当UDM中的签约数据发生变化时，UDM通知AMF更新用户数据。 
AMF在删除了已注销MS的签约数据和MM上下文后将结果通知给UDM。 
客户收益 :本特性是移动终端的基本功能。 
说明 :AFM支持UDM插入和删除用户数据。根据不同触发点，用户数据管理分为以下两种： 
1.UDM触发点：UDM将数据插入AMF，修改或删除AMF中存储的数据。 
2.AMF触发点：AMF删除用户上下文和数据时，通知UDM用户数据已经删除。 
## ZUF-79-03-005 UE配置更新 
特性描述 :特性描述 :术语 :本特性不涉及相关术语。 
描述 :定义 :UE配置更新是指核心网的参数发生变化时，需要通知UE更新或者删除这些参数，以触发新业务的流程。 
背景知识 :在2G/3G/4G时，核心网与UE之间的参数传递一般是通过信令流程来完成，涉及到多个流程。但在5GC中，统一通过UE配置更新流程来完成核心网与UE之间的参数交互，大大减少了流程的复杂度。 
应用场景 :UE配置更新的应用场景包括由AMF触发的UE配置更新和由PCF触发的UE配置更新。 
###### AMF触发 
由AMF触发的UE配置更新包括以下场景： 
5G-GUTI配置更新导致AMF触发的UE配置更新。 
NITZ配置更新导致AMF触发的UE配置更新。 
NSSAI配置更新导致AMF触发的UE配置更新。 
TAI List配置更新导致AMF触发的UE配置更新。 
移动性限制配置更新导致AMF触发的UE配置更新。 
MICO配置更新导致AMF触发的UE配置更新。 
###### PCF触发 
UE的策略更新导致PCF触发的UE配置更新。 
客户收益 :受益方|受益描述
---|---
运营商|通过配置更新的流程，AMF/PCF可以对相关UE设置相应参数，通知UE开展新的业务。
终端用户|此特性对终端用户不可见。
实现原理 :

系统架构 :



本特性涉及的系统架构如[图1]所示。


图1  系统架构图






涉及的NF/网元参见下表。 


NF/网元|说明
---|---
NF|AMF|配置管理功能主处理NF，与UE/(R)AN/PCF协作完成UE配置管理功能。
NF|SMF|用户会话管理NF，注册更新过程中，如果存在用户会话上下文，可根据UE指示触发用户面隧道建立。
NF|PCF|用户策略控制NF，UE配置管理功能中通过AMF完成PCF的UE策略更新。
网元|(R)AN|无线接入网络，UE配置管理功能中在用户处于连接态时，控制用户目标小区的选择。
网元|UE|支持5G接入的终端，接收AMF下发的配置管理参数，并触发相应的业务。




业务流程 :####### AMF触发的UE配置更新业务流程 
AMF触发的UE配置更新业务流程如[图2]所示。
图2  AMF触发的UE配置更新业务流程

由于各种原因（例如：UE移动性改变，来自UDM的用户数据更新通知的接收，网络切片配置的改变）或UE需要执行注册过程，AMF确定UE配置更新的必要性。如果UE处于CM-IDLE，则AMF将触发网络触发的业务请求。 
AMF发送配置更新消息给UE。消息中携带相应的参数，主要包括：5G-GUTI, TAI List, Allowed NSSAI,
Mapping Of Allowed NSSAI, Configured NSSAI for the Serving PLMN, Mapping
Of Configured NSSAI, rejected S-NSSAIs, NITZ, Mobility Restrictions,
LADN Information, MICO, Configuration Update Indication等。其中Configuration
Update Indication的作用是指示UE是否需要回复ACK或者重新注册。 
如果UE配置更新指示需要确认UE配置更新命令，则UE将向AMF发送UE配置更新完成消息。除NITZ外，AMF应请求对所有UE配置更新的确认消息。如果不需要注册过程，跳过步骤3a，3b，3c，3d和步骤4的过程。
如果配置更新指示需要注册过程，则根据UE配置更新命令中包含的参数执行以下步骤。 
如果在UE配置更新命令消息中包括了MICO，则UE应在确认之后立即发起注册过程，与网络重新协商MICO模式。后续跳过步骤3b，3c，3d和步骤4。
如果由AMF向UE提供的新的Allowed NSSAI或新的Mapping Of Allowed NSSAI或新的Configured
NSSAI不影响到切片的现有连接，则AMF在步骤2中接收到确认消息后不需要为UE释放NAS信令连接，也不需要立即注册。UE可以立即使用新的Allowed
NSSAI或新的Mapping Of Allowed NSSAI映射。跳过步骤3c和3d。 
如果AMF向UE提供的新的Allowed NSSAI或新的Mapping Of Allowed NSSAI映射或新的Configured
NSSAI影响到网络片的现有连接，则AMF会在UE配置更新命令消息中包括新的Allowed NSSAI以及相关的Mapping Of
Allowed NSSAI（如果可用），以及UE在执行注册过程时不应在接入层信令中提供5G-GUTI的指示。在步骤2中接收到确认之后，AMF将释放UE的NAS信令连接，除非存在与紧急服务相关联的已建立的PDU会话。跳过步骤3d。 
如果在订阅的S-NSSAI更新之后AMF不能确定新的Allowed NSSAI，则AMF不在UE配置更新命令消息中包括任何Allowed
NSSAI，而是指示UE在执行注册过程时不提供Access Stratum信令中的5G-GUTI。 在步骤2中接收到确认消息之后，AMF将释放UE的NAS信令连接，除非存在与紧急服务相关联的已建立的PDU会话。 
在UE进入CM-IDLE状态之后发起注册过程，并且根据从AMF接收的指示在接入层信令中包含5G-GUTI。 如果存在与紧急服务相关联的已建立的PDU会话并且UE已经接收到执行注册过程的指示，则UE将仅在与紧急服务相关联的PDU会话被释放之后才发起注册过程。 
在UE成功完成所需的注册过程之前，AMF应拒绝来自UE的任何NAS消息(携带用于非紧急PDU会话的PDU会话建立请求)。 
####### PCF触发的UE配置更新业务流程 
PCF触发的UE配置更新业务流程如[图3]所示。
图3  PCF触发的UE配置更新业务流程

AMF从PCF接收到Npcf_AMPolicyControl_Create响应（接入和移动性相关信息或UE策略容器（UE接入和PDU会话选择相关信息）或两者皆有）。 
AMF从PCF接收到Npcf_AMPolicyControl_UpdateNotify（接入和移动性相关信息或UE策略容器（UE接入和PDU会话选择相关信息）或两者皆有）。 
如果UE处于CM-IDLE态，则AMF触发网络触发的服务请求，如果UE不可达，AMF向PCF报告UE策略容器不能被提供给UE。如果UE处于CM-CONNECTED，则AMF透明地将从PCF接收的UE策略容器（UE接入和PDU会话选择相关信息）传送到UE。UE策略容器包括PSI（Policy
Section ID）列表，用于通知UE添加、移除或修改一个或多个PSI。 
UE执行PSI操作并将结果发送到AMF。AMF将结果透明地传输给PCF。如果一个或多个PSI操作失败，则UE包括UE策略容器（存储的PSI列表）。 
如果AMF接收到UE策略容器并且PCF订阅了UE策略容器的接收通知，则AMF通过Npcf_AMPolicyControl_Update将UE的响应转发到PCF，该Npcf_AMPolicyControl_Update包括关于策略控制请求触发条件的信息。 
PCF确认AMF接收到Npcf_AMPolicyControl_Update。 
NF实现 :AMF实现 :####### PCF实现 
与UE交互，完成配置更新消息交互。 
与PCF交互，完成策略交互。 
更新UE的策略时，通知AMF进行UE配置更新流程。 
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
N15|ZUF-79-19-007 N15
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|System Architecture for the 5G System
TS 23.502|3GPP|Procedures for the 5G System
TS 29.518|3GPP|5G System; Access and Mobility Management Services
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布
可获得性 :License要求 :该特性为5G产品的基本特性，无需license支持。 
对其他网元的要求 :UE|gNB/ng-eNB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :配置命令 :AMF新增的配置命令如下。 
配置项|命令
---|---
网络标识和时区配置|SET NITZCFG
SHOW NITZCFG|网络标识和时区配置
定时器 :本特性不涉及定时器的变化。 
性能统计 :####### AMF性能统计 
序号|性能计数器名称
---|---
1|C510500012 发送Configuration Update Command次数
2|C510500013 接收Configuration Update Complete次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :在AMF可灵活配置“UE配置更新消息”携带NITZ。
配置前提 :无 
配置过程 :通过[SET NITZCFG]命令，修改网络标识和时区配置。
配置实例 :配置场景 :在初始注册流程、跨AMF流程、跨RAT流程、周期性注册流程、局内移动性注册流程中，UE配置更新消息携带NITZ。 
数据规划 :参数|取值
---|---
携带NI|携带网络名称
携带TZ|携带时区
初始注册流程是否携带NITZ|初始注册流程携带NITZ
跨AMF流程是否携带NITZ|跨AMF流程携带NITZ
跨RAT流程是否携带NITZ|跨RAT流程携带NITZ
周期性注册流程是否携带NITZ|周期性注册流程携带NITZ
局内移动性注册流程是否携带NITZ|局内移动性注册流程携带NITZ
携带国家名缩写|携带国家名缩写
长网络名称编码方式|长网络名称编码用UCS2
长网络名称|china mobile
短网络名称编码方式|短网络名称编码用UCS2
短网络名称|cmcc
配置步骤 :步骤|说明|操作
---|---|---
1|配置全局NITZ|SET NITZCFG:CARRYNI="CARRYNI",CARRYTZ="CARRYTZ",INTIALREG="CARRYININTIALREG",INTERAMF="CARRYININTERAMFREG",INTERRAT="CARRYININTERRAT",PERIODICREG="CARRYINPERIODICREG",INTRAAMFMOBILEREG="CARRYININTRAAMFMOBILEREG",ADDCI="CARRYCI",FULLNICODEPLAN="FULLUSEUCS2",FULLNI="china mobile",SHORTNICODEPLAN="SHORTUSEUCS2",SHORTNI="cmcc"
测试用例 :测试项目|UE配置更新
---|---
测试目的|验证UE配置更新流程，AMF灵活下发NITZ。
预置条件|RAN，各NF运行正常。用户已开户，且已签约5G业务。AMF配置初始注册下发NITZ。
测试过程|UE开机发起注册流程。UE发起PDU会话建立，持续进行数据业务。发起Configuration Update流程，如用户签约的NSSAI变更。
通过准则|AMF向UE发起UE配置更新流程，如：用户签约的NSSAI变更，AMF重新下发NSSAI，通过ConfigurationUpdate Command消息发送给UE。AMF向UE发起UE配置更新流程，携带NITZ。
测试结果|-
## ZUF-79-03-006 移动性限制 
特性描述 :特性描述 :术语 :术语|含义
---|---
Allowed area|允许区域，用户在该区域中可以正常的进行语音和数据业务。
Non-Allowed area|不允许区域，用户可以在该区域注册，但不能在该区域进行其他业务。
Forbidden area|禁止区域，用户不允许在该区域注册。
描述 :定义 :移动性限制是指限制UE的移动性或限制UE业务接入。移动性限制由UE、无线接入网和核心网完成，包括如下几个方面： 
RAT restriction定义了在一个PLMN下UE禁止接入的3GPP RAT。 
Forbidden Area定义了UE禁止接入的区域。 
Service Area Restriction定义了UE业务接入受限的区域，包含两种区域类型：Allowed Area：UE可以正常的进行数据和语音业务，UE业务接入不受限制。Non-Allowed Area：UE仅能通过业务请求响应寻呼，不能主动发起业务请求或其他会话管理信令消息用于进行数据和语音业务。 
Core Network type restriction定义了UE是否被允许在该PLMN下接入到5GC。 
 说明： 
移动性限制仅用于3GPP接入，不用于non-3GPP接入。 
背景知识 :在2G/3G/4G网络中，也存在移动性限制功能，主要包括RAT restriction和Forbidden
Area。 
面对万物互联的5G时代，用户类型多样，用户业务需求多样，5G网络中移动性限制内容更加丰富，对UE的移动性和业务接入的限制更加灵活。 
项目|2G|3G|4G|5G
---|---|---|---|---
RAT restriction|是|是|是|是
Forbidden Area|是|是|是|是
Service Area Restrictions|否|否|否|是
Core Network type|否|否|否|是
应用场景 :移动性限制是5GC的重要功能，典型场景包括如下几种。 
###### 场景一：漫游用户 
漫游用户，根据用户签约信息或漫游协议，仅能接入特定的RAT或区域。 
###### 场景二：网络共享 
网络共享时，控制用户对PLMN的选择。 
###### 场景三：特殊业务用户 
使用特殊业务的用户，对其移动性进行限制，例如： 
校园网用户，用户仅能在校园内使用业务。 
智能井盖，仅能在某个地方静止不动，不能发生位置移动。 
客户收益 :受益方|受益描述
---|---
运营商|业务创新：通过对用户更灵活的移动性限制管理，便于用户业务上的创新，如推出更多基于位置限制的业务。投资保护：通过对特定用户的移动性限制，可避免非法用户占用运营商网络资源。
终端用户|此特性对终端用户不可见。
实现原理 :

系统架构 :



本特性涉及的系统架构如[图1]所示。


图1  系统架构图






[图1]描述了5GC网络对移动终端进行移动性限制过程的组网结构。


移动性限制功能涉及的NF/网元参见下表。 


NF/网元|说明
---|---
NF|AMF|移动性限制功能主处理NF，与UE/RAN/UDM/UDR/PCF协作完成移动性限制功能。
NF|UDM|用户签约信息处理NF，移动性限制功能中与UDR配合向AMF等提供用户移动性限制签约数据。
NF|UDR|用户签约数据存储NF，移动性限制功能中与UDM/PCF配合向AMF等提供用户移动性限制功能签约数据。
NF|PCF|用户策略控制NF，移动性限制功能中与UDR配合向AMF提供UE的业务接入限制数据。
网元|(R)AN|无线接入网络，移动性限制功能中在用户处于连接态时，控制用户目标小区的选择。
网元|UE|支持5G接入的终端，移动性限制功能中用户处于空闲态时，控制用户目标小区的选择。




业务流程 :####### 注册拒绝流程 
注册拒绝流程如[图2]所示。
图2  注册拒绝

流程说明如下： 
UE判断需要发起注册流程时，发送注册请求消息。 
NG-RAN收到注册请求消息后，如果消息中有5G-GUTI，则根据5G-GUTI选择AMF，如果消息中没有5G-GUTI，则根据消息中Requested
NSSAI信息，选择一个合适的AMF。 
NG-RAN向AMF发送注册请求消息。 
AMF处理注册请求消息，包括获取用户信息，安全过程等。 
AMF为了向UDM获取用户签约数据，向UDM发送Nudm_SDM_Get消息。 
UDM向AMF返回Nudm_SDM_Get响应消息，消息中携带ratRestrictions、forbiddenAreas、serviceAreaRestriction、coreNetworkTypeRestrictions等用户签约信息。 
AMF根据用户签约数据及本地策略，确定UE的移动性限制策略，决定拒绝用户接入。 
AMF向UE发送注册拒绝消息，消息中携带5GMM Cause等信息。如果Core Network type为不允许接入5GC，则5GMM
Cause值设置为“N1 mode not allowed”。 
####### 注册流程 
注册流程如[图3]所示。
图3  注册流程

流程说明如下： 
UE判断需要发起注册流程时，发送注册请求消息给NG-RAN。 
NG-RAN收到注册请求消息，如果消息中携带5G-GUTI，则根据5G-GUTI选择AMF，如果消息中没有5G-GUTI，则根据消息中Requested
NSSAI信息，选择一个合适的AMF。 
NG-RAN向AMF发送注册请求消息。 
AMF处理注册请求消息，包括向Old AMF获取用户信息，向UE获取用户信息，安全过程等。 
AMF向UDM发送Nudm_SDM_Get消息，向UDM获取用户签约数据。 
UDM向AMF返回Nudm_SDM_Get响应消息，消息中携带ratRestrictions、forbiddenAreas、serviceAreaRestriction、coreNetworkTypeRestrictions等用户签约信息。 
继续处理注册过程，如确定UE是否需重定向等。 
AMF向PCF发送Npcf_AMPolicyControl_Create消息，获取用户接入和移动性策略。 
PCF向AMF返回Npcf_AMPolicyControl_Create响应消息，消息中携带Service Area
Restrictions等信息。 
AMF根据用户签约数据、PCF提供的Service Area Restrictions数据以及本地策略，确定UE的移动性限制策略。 
AMF继续处理注册流程，包括更新PDU会话等，直到AMF向UE发送注册接受消息。 
AMF向UE发送注册接受消息，消息中携带Service Area List等信息。如果需要向(R)AN发送初始上下文建立请求消息，则在请求消息中携带Mobility
Restriction List等信息。 
继续处理注册流程，直到注册流程结束。 
####### 配置更新流程 
配置更新流程如[图4]所示。
图4  配置更新

流程说明如下： 
由于用户签约数据改变、PCF提供的UE业务接入限制数据改变、本地策略改变，导致用户移动性限制策略改变，需要把新的用户移动性限制策略通知UE。 
AMF向UE发送UE配置更新命令消息，消息中携带新的Service Area List等信息。 
UE更新Service Area List信息后，向AMF返回UE配置更新命令完成消息。 
####### 业务请求流程 
业务请求流程如[图5]所示。
图5  业务请求

流程说明如下： 
UE判断需要发起业务请求流程，向NG-RAN发送业务请求消息。 
NG-RAN收到注册请求消息后，向AMF发送业务请求消息。 
AMF处理业务请求消息，包括安全过程、更新PDU会话等。 
AMF向NG-RAN发送初始上下文建立请求消息，在请求消息中携带Mobility Restriction List等信息。 
AMF继续处理业务请求，直到流程结束。 
####### 基于N2的局内切换流程 
基于N2的局内切换流程如[图6]所示。
图6  基于N2的局内切换

流程说明如下： 
Source NG-RAN判断需要发起基于N2的切换时，发送切换需求消息。 
AMF处理切换需求消息，确定AMF不需改变。 
AMF向NG-RAN发送切换请求消息，在请求消息中携带Mobility Restriction List等信息。 
AMF继续处理切换，直到流程结束。 
####### 基于N2的局间或跨RAT切换流程 
基于N2的局间或跨RAT切换流程如[图7]所示。
图7  基于N2的局间或跨RAT切换

流程说明如下： 
基于N2的跨AMF的切换处理完成或垮RAT切换处理完成，且切换过程中Target AMF在Handover Request消息中不携带Mobility
Restriction List信息。 
UE发起切换后的注册流程，向NG-RAN发送注册请求消息。 
NG-RAN向AMF发送注册请求消息。 
AMF处理注册请求消息，包括安全过程、获取签约数据、更新PCF等。 
AMF根据用户签约数据、PCF提供的Service Area Restrictions数据以及本地策略，确定UE的移动性限制策略。 
AMF构造注册接受消息，消息中携带Service area list等信息。AMF向NG-RAN发送DNT消息，消息中携带Mobility
Restriction List和注册接受等信息。 
NG-RAN向UE发送注册接受消息，UE更新Service area list等信息。 
继续处理注册流程，直到注册流程结束。 
NF实现 :AMF实现 :和UDM交互，获取用户ratRestrictions、forbiddenAreas、serviceAreaRestriction、coreNetworkTypeRestrictions等信息。 
和PCF交互，获取用户的Service Area Restrictions等信息。 
和RAN交互，通知其Mobility Restriction List信息，完成用于连接态下移动性限制的控制。 
和UE交互，通知其Service area list信息。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N15|ZUF-79-19-007 N15
系统影响 :移动性限制功能需AMF决策移动性限制策略，会消耗一定的系统资源。 
应用限制 :暂不支持non-3GPP接入方式。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|System Architecture for the 5G System
TS 23.502|3GPP|Procedures for the 5G System
TS 23.503|3GPP|Policy and ChargingControl Framework for the 5G System
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage3
TS 29.502|3GPP|Session Management Services; Stage 3
TS 29.503|3GPP|Unified Data Management Services; Stage 3
TS 29.507|3GPP|Access and Mobility Policy Control Service; Stage 3
TS 29.514|3GPP|Policy Authorization Service; Stage 3
TS 29.518|3GPP|5G System; Access and Mobility Management Services
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需license支持。
对其他网元的要求 :要求参与移动性限制的各网元功能，均依据3GPP协议规定。 
UE|gNB/ng-eNB|PCF|UDM
---|---|---|---
√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :移动性限制，需全局规划。 
O&M相关 :配置命令 :AMF新增的配置命令如下。 
配置项|命令
---|---
AMF移动性配置|SET AMFMOBCFG
SHOW AMFMOBCFG|AMF移动性配置
定时器 :本特性不涉及定时器变化。 
性能统计 :本特性不涉及性能统计变化。 
告警和通知 :本特性不涉及告警和通知变化。 
话单与计费 :本特性不涉及话单与计费变化。 
特性配置 :特性配置 :配置说明 :AMF配置仅涉及区域限制功能开关。 
配置前提 :用户在UDM上签约了禁止区域 
RAN和各NF基本业务正常 
配置过程 :通过[SET AMFMOBCFG]命令，修改AMF移动性配置。
配置实例 :配置场景 :用户在UDM签约限制的区域，AMF支持区域限制功能，用户从限制的区域注册，AMF可以拒绝用户注册。 
数据规划 :参数|取值
---|---
支持MICO|不支持MICO
支持禁止区域限制|支持禁止区域限制
AMF是否获取IMEI(SV)|不支持获取IMEI或IMEISV
配置步骤 :步骤|说明|操作
---|---|---
1|修改AMF移动性配置|SET AMFMOBCFG:SUPTMICO="NOTSUPTMICO",SUPTFORBIDDENAREA="SUPTFORBIDDENAREA",AMFGETIMEI="NOTGETIMEIORIMEISV"
调整特性 :无。 
测试用例 :测试项目|签约禁止区域接入限制
---|---
测试目的|验证由于签约禁止区域接入限制，UE发起初始注册失败。
预置条件|RAN，各NF运行正常。用户UE已开户，签约数据中禁止用户从部分区域接入。
测试过程|设置AMF支持区域限制功能。UE从签约的禁止接入区域开机发起注册流程。
通过准则|AMF向UDM获取签约，UDM向AMF返回获取签约数据响应，携带禁止区域。UE发起初始注册流程失败，AMF向UE发送Registration Reject。
测试结果|--
常见问题处理 :无 
## ZUF-79-03-007 对等PLMN 
概述 :EPLMN列表可根据SUPI范围和位置信息进行配置。 
客户收益 :不同的SUPI和位置可以使用不同的EPLMN列表。 
说明 :EPLMN与当前业务网络对等。AMF将EPLMN列表通知给UE，以便UE在网络选择时选择EPLMN。 
在成功注册过程中，根据3GPP协议将EPLMN信息通知给移动终端。 
EPLMN可根据AMF中SUPI范围和位置信息进行配置。移动用户注册到AMF时，会选择相应的EPLMN列表并发送给用户设备。 
## ZUF-79-03-008 多个GUAMI 
概述 :AMF可能有多个GUAMI，该功能有利于AMF Set的部署。 
客户收益 :该功能使AMF Set的部署更加灵活。 
说明 :<GUAMI> := <MCC> <MNC> <AMF Region ID> <AMF Set ID> <AMF Pointer> 
AMF支持多个GUAMI，这些不同GUAMI的字段值可能不同，如AMF Region ID等。 
## ZUF-79-03-009 多PLMN 
特性描述 :特性描述 :术语 :术语|含义
---|---
Equivalent PLMN List|由一系列PLMN组成，在进行PLMN选择时，列表中的PLMN都是同等重要的，优先级相同。
PLMN|公用陆地移动网络，由MCC+MNC组成，用于唯一标识一个移动网络，比如中国移动的PLMN为460 00，其中460为中国大陆的移动国家码(MCC)，00为中国大陆为中国移动分配的网络号。
描述 :定义 :AMF多PLMN功能指AMF支持多个PLMN，用户SUPI中的PLMN只要和AMF支持的多个PLMN中的任一个相同，则判断该用户是归属地接入。
EPLMN列表是AMF在注册时，在Registration Accept消息中带给UE。UE进行PLMN选择、小区选择/重选或者切换的时候，EPLMN列表中的所有PLMN都认为是同等重要的。AMF可以根据不同SUPI号段下发不同的EPLMN列表。
背景知识 :PLMN是公用陆地移动网络，由移动国家码(MCC)和移动网络码(MNC)组成，用于唯一标识一个移动网络。其中MCC由国际标准机构按国家或者地区分配，全球唯一；而MNC则是由MCC对应的国家或者地区分配，在这个国家或地区内唯一。 
对于很多运营商而言，由于跨国运营，或者拥有多个不同的网络（2G\3G\4G\5G网络），可能分配了多个PLMN。同一个运营商下的用户，在不同国家或者地区，或者用户通过不同的接入技术接入该运营商网络，都应该属于归属地接入，而不是漫游。要达到这个要求，则需要网络能够支持多PLMN。 
EPLMN用于UE选网，EPLMN是与UE当前所选择的PLMN处于同等地位的PLMN。 
应用场景 :场景一 :具有多个PLMN的运营商，比如跨国运营商或多个运营商合并而形成的新的运营商，用户的SUPI有多个PLMN，但无线只有一个PLMN。 
该场景下，需配置多PLMN，EPLMN不需配置。 
场景二 :具有多个PLMN的运营商，比如跨国运营商或多个运营商合并而形成的新的运营商，用户的SUPI有多个PLMN，无线也配置了多个PLMN。 
该场景下，需配置多PLMN，EPLMN也需配置。 
场景三 :具有多个PLMN的运营商，比如运营商不同接入方式的无线有不同的PLMN，用户的SUPI只有一个PLMN，无线配置了多个PLMN。 
该场景下，不需配置多PLMN，EPLMN需配置。 
客户收益 :受益方|受益描述
---|---
运营商|支持多PLMN，可以让不同网络的用户接入时，如同归属地接入一样，降低用户的费用，从而吸引更多的用户； 增加了组网灵活性。
终端用户|一般来说，漫游接入与归属地接入相比，业务成功率相对低。因此，在支持多PLMN网络的情况下，对于某些用户而言，资费可以相对较低，业务成功率又相对较高。
实现原理 :涉及的网元 :网元名称|网元作用
---|---
UE|保存网络侧下发的EPLMN列表。在多个可用PLMN中选择一个合适的PLMN。
eNB|注册时，AMF在移动限制列表信息中把EPLMN携带给RAN。切换时，只在Serving PLMN和EPLMN中切换。
本网元实现 :多PLMNUE注册和PDU会话建立时，AMF需要判断UE是否归属地接入。用户SUPI中的PLMN只要和AMF支持的多个PLMN中的任一个相同，则判断该用户是归属地接入。 
EPLMN列表按SUPI号段配置EPLMN列表，如果SUPI号段没有配置，就使用缺省EPLMN列表。在Registration Accept消息中将配置的EPLMN携带给UE，在移动限制列表信息中把EPLMN携带给RAN。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2(Release 15)"|-
3GPP TS 23.502: "Procedures for the 5G System;Stage 2(Release 15)"|-
3GPP TS 24.501 "Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3"|-
3GPP TS 38.413 "NG-RAN; NG Application Protocol (NGAP)"|-
特性能力 :名称|指标
---|---
对于AMF多PLMN功能，包含移动数据中配置的PLMN，一个AMF中最多可以配置PLMN数|17个
对于EPLMN列表，给每个UE下发的EPLMN列表中，最多可以包含不同的PLMN数|15个
对于EPLMN列表，可以按SUPI号段配置EPLMN列表，最多可以有SUPI号段数|80000个
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNodeB|AMF|SMF|PCF|UDM
---|---|---|---|---|---
√|√|√|–|–|–
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令修改AMF本局配置SET AMFLOCALOFFICECFG查询AMF本局配置SHOW AMFLOCALOFFICECFG新增GUAMI配置ADD GUAMICFG修改GUAMI配置SET GUAMICFG删除GUAMI配置DEL GUAMICFG查询GUAMI配置SHOW GUAMICFG增加Guami标识ADD LOCALGUAMI删除Guami标识DEL LOCALGUAMI查询Guami标识SHOW LOCALGUAMI新增PLMN配置ADD PLMNCFG修改PLMN配置SET PLMNCFG删除PLMN配置DEL PLMNCFG查询PLMN配置SHOW PLMNCFG 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :运营商由于各种原因，可能拥有多个PLMN。 
跨国运营商。 
同一地区的多个运营商合并为一个运营商。 
同一国家不同地区的PLMN不同，且不同RAT（Radio Access Technology，无线接入技术）网络的PLMN不同。 
而同一个运营商，不同PLMN的用户，接入本运营商网络，即使国家或者地区或者RAT不相同，也应该都属于归属地接入，而不是漫游接入。因此对于拥有多个PLMN的运营商，需要移动网络支持多PLMN。 
在5GC网络中，运营商新部署了一个AMF时，需要配置AMF的身份信息（包括缺省的本局PLMN），便于AMF能在5GC网络中提供服务。如果该运营商有多个PLMN，还需要配置其他支持的PLMN。 
配置前提 :无线支持多个PLMN无线支持多个PLMN，并通知给AMF，AMF可以处理无线多个PLMN对应的TA。 
本地接入用户有多个PLMN本地接入用户有多个PLMN，这些用户都属于归属地接入，AMF可以为其分配Selected PLMN对应的5G-GUTI和TA List。 
配置过程 :使用[SET AMFLOCALOFFICECFG]命令，AMF本局配置，配置AMF本局缺省的PLMN信息，包含移动国家码和移动网络码。
使用[ADD GUAMICFG]命令，GUAMI配置，在GUAMI池内配置AMF本局所支持的的全部GUAMI信息，包含GUAMI详细信息和其所对应的唯一标识。
GUAMI = MCC + MNC + AMF Identifier，本局支持的全部GUAMI就携带了本局支持的多个PLMN信息。 
使用[ADD LOCALGUAMI]命令，本局GUAMI配置，将GUAMI池内配置好的GUAMI和AMF本局关联起来。
使用[ADD PLMNCFG]命令，AMF其他PLMN配置，配置AMF本局支持的其他PLMN信息，包含移动国家码和移动网络码。
配置实例 :配置说明 :AMF支持的PLMN为46001、46002和46003，其中本局缺省配置的PLMN为46001，支持的其他PLMN为46002和46003。 
AMF支持三个本局GUAMI，对应每个GUAMI中的PLMN分别是46001、46002和46003。 
数据规划 :用户从46002的PLMN上来，AMF基于支持的多PLMN信息判定用户属于归属地接入，向用户分配的GUTI选用PLMN为46002的GUAMI。 
用户从46011的PLMN上来，AMF基于支持的多PLMN信息判定用户不属于归属地接入，向用户分配的GUTI通过轮询选用支持的GUAMI中的一个。 
NG Setup和RAN配置更新过程中带给NR的支持的PLMN信息包含46001、46002和46003。 
配置步骤 :步骤|说明|命令
---|---|---
1|设置本局缺省PLMN信息|SET AMFLOCALOFFICECFG:MCC="460",MNC="01"
2|新增本局支持的GUAMI信息|ADD GUAMICFG:GUAMIID=1,MCC="460",MNC="01",REGIONID=1,SETID=2,POINTID=3ADD GUAMICFG:GUAMIID=2,MCC="460",MNC="02",REGIONID=1,SETID=2,POINTID=4ADD GUAMICFG:GUAMIID=3,MCC="460",MNC="03",REGIONID=1,SETID=2,POINTID=5ADD LOCALGUAMI:GUAMIID=1;ADD LOCALGUAMI:GUAMIID=2;ADD LOCALGUAMI:GUAMIID=3;
3|新增本局支持的其他PLMN信息|ADD PLMNCFG:PLMNID=1,MCC="460",MNC="02"ADD PLMNCFG:PLMNID=1,MCC="460",MNC="03"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF在NG SETUP流程中下发Served GUAMI
---|---
测试目的|验证AMF能够正确下发Served GUAMI信息给(R)AN。
预置条件|AMF和(R)AN连接正常。AMF中配置其他HPLMN和其他GUAMI。
测试过程|(R)AN发送NG SETUP Request消息给AMF。
通过准则|AMF回复的NG SETUP Response消息中携带Served GUAMIs，包含本局移动数据中的GUAMI和其他GUAMI配置中的所有GUAMI。
测试结果|–
测试项目|AMF下发Served GUAMI
---|---
测试目的|验证AMF能够正确下发Served GUAMI信息给(R)AN。
预置条件|AMF和(R)AN连接正常。AMF中已经配置其他HPLMN和其他GUAMI。
测试过程|再新增一条其他GUAMI记录。AMF前后台同步。
通过准则|前后台同步后，AMF发送AMF CONFIGURATION UPDATE给(R)AN，携带Served GUAMIs，包含本局移动数据中的GUAMI和修改后的其他GUAMI配置中的所有GUAMI。
测试结果|–
测试项目|AMF下发GUTI
---|---
测试目的|验证附着流程中AMF正常分配GUTI。
预置条件|AMF和HSS连接正常。AMF和SGW连接正常。AMF和(R)AN连接正常。AMF中本局移动数据中配置PLMN为PLMN1，并在其他HPLMN中配置PLMN2。AMF在其他GUAMI配置中添加PLMN1和PLMN2对应的AMF组ID和AMF编码。
测试过程|用户A附着，用户选择的PLMN是PLMN1。用户B附着，用户选择的PLMN是PLMN2。
通过准则|对于用户A，AMF发送的Attach Accept中消息携带新分配的GUTI，其中GUTI中的PLMN为PLMN1，AMF组ID和AMF编码为PLMN1对应的AMF组ID和AMF编码中的一组。对于用户B，AMF发送的Attach Accept中消息携带新分配的GUTI，其中GUTI中的PLMN为PLMN2，AMF组ID和AMF编码为PLMN2对应的AMF组ID和AMF编码中的一组。
测试结果|–
测试项目|AMF下发EPLMN
---|---
测试目的|验证附着流程中AMF下发正确的EPLMN给用户。
预置条件|AMF和HSS连接正常。AMF和SGW连接正常。AMF和(R)AN连接正常。AMF中配置默认EPLMN，包含小于5个的PLMN。AMF配置IMSI号段1对应的EPLMN Profile，适用于所有TA，包含大于5个的PLMN。AMF中配置支持5个PLMN。
测试过程|归属于IMSI号段1的用户A附着。不归属于IMSI号段1的用户B附着。
通过准则|对于用户A，AMF发送的Attach Accept中消息携带EPLMN列表，其中EPLMN列表为IMSI号段1配置的EPLMN中的前5个。对于用户B，AMF发送的Attach Accept中消息携带EPLMN列表，其中EPLMN列表为默认的EPLMN。
测试结果|–
常见问题处理 :无 
## ZUF-79-03-010 NITZ 
特性描述 :特性描述 :术语 :术语|含义
---|---
NITZ|Network Identity and Timezone，网络标识和时区。
NI|Network Identity，网络标识。
TZ|Timezone，时区。
DST|Daylight Saving Time，夏令时。
描述 :定义 :NITZ，指网络侧将网络标识和时区信息（如时区、时间、夏令时）传递给UE，UE可以根据网络侧下发的信息进行自动更新。
AMF可以在UE注册到5G网络后，给UE下发NITZ信息。
背景知识 :NITZ是3GPP在22.042协议中定义的功能特性，要求用户在接入3GPP网络后，网络可以将网络标识和时区传递给UE。 
当用户在2/3G网络下接入时，通常由MSC给UE下发网络标识和时区。 
当用户在4G网络下接入时，由MME给UE下发网络标识和时区。 
当用户在5G网络接入时，由AMF给UE下发网络标识和时区。 
应用场景 :###### 场景一：UE接入网络 
UE首次接入AMF时，AMF将NITZ信息传递给UE。
###### 场景二：运营商规划的NITZ信息发生变化 
若运营商规划的NITZ信息发生变化，AMF将向UE传递新规划的NITZ信息。 
 说明： 
为了不过度消耗网络资源，AMF并不是实时地向UE传递更新NITZ信息，而是待用户活动后，再将变化后的NITZ信息传递给UE。 
客户收益 :受益方|受益描述
---|---
运营商|将运营商网络标识传递给UE并呈现给用户，将当前接入运营商的名称友好自动地告知用户，方便用户知晓接入运营商名称的同时，也能提升运营商的广告价值和品牌价值。将时间和时区信息传递给UE，UE自动更新终端系统时间，根据时区调整终端系统时间，将时区和时间信息准确友好地呈现给用户，提升用户的满意度。
移动用户|移动用户能获知当前接入运营商的名称。漫游用户在接入到漫游地运营商后，能自动获知漫游接入的运营商名称，得知接入运营商发生了变化，给用户带来友好的体验。移动用户能够从网络侧自动更新用户当前的时区和时间。UE自动刷新终端系统时钟，自动维护终端系统时钟的正确性，避免了用户手动调整时区时间的麻烦，提升用户的满意度。
实现原理 :系统架构 :AMF通过N1接口将NITZ信息传递给UE，UE接受和存储NITZ信息，并根据时区调整UE时钟，再将网络标识、时区、时间信息友好准确地呈现给用户。
图1  AMF向UE传递网络标识和时区信息

涉及的网元 :NF名称|网元作用
---|---
AMF|AMF通过N1接口将NITZ信息传递给UE。
UE|UE接受和存储NITZ信息，并根据时区调整UE时钟，再将网络标识、时区、时间信息友好准确地呈现给用户。
协议栈 :接口|描述|协议栈
---|---|---
N1|UE与AMF间逻辑接口|ZUF-79-19-001 N1
本网元实现 :在NITZ功能中，AMF通过N1接口将NITZ信息传递给UE。
业务流程 :图2  AMF发起UE配置更新流程

UE注册到AMF后，AMF可以向UE发起配置更新过程，在UE配置更新命令中，将网络标识和时区信息传递给UE。 
如果仅仅只传递网络标识和时区信息给UE，则AMF不需要等待UE的确认。 
如果还同时通知了其他信息（如注册区域、GUTI等），则AMF还需要等待UE的确认过程。 
网络标识和时区信息包括网络长标识、网络短标识、时区、时间、夏令时，这些参数都是可选的，AMF可以通过配置和需求，灵活地下发一个或者多个信息给UE。 
系统影响 :AMF开启NITZ特性后，会发送配置更新命令消息携带NITZ信息给UE，由于触发话务很低，预估对系统性能影响较小。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 24.501: "Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3"|5.4.4Generic UE configuration update procedure
3GPP TS 22.042: "Network Identity and TimeZone (NITZ);Service description; Stage 1"|-
特性能力 :名称|指标
---|---
网络标识名称长度限制|采用UCS2编码方式时，支持104个字符。采用“GSM default alphabet”编码方式时，支持208个字符。如果网路名称中包含非英文字符（如中文字符），则只允许配置采用UCS2编码方式。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.21|首次发布。
License要求 :该特性无需License支持。 
对其他网元的要求 :UE|AMF
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
全局NITZ配置|SET NITZCFG
SHOW NITZCFG|全局NITZ配置
性能统计 :该特性不涉及计数器的变化。
告警和通知 :该特性不涉及告警/通知消息的变化。
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :全局NITZ配置可以灵活控制不同流程中AMF是否给终端下发NITZ信息。 
配置前提 :5GC中AMF网元运行正常。 
配置过程 :当需要给终端下发NI或者TZ时，执行[SET NITZCFG]命令，哪些流程期望下发NITZ，则设置该流程对应的参数值携带NITZ。
配置实例 :场景说明 :场景一：
UE首次接入AMF时，AMF将NITZ信息传递给UE。
场景二：
运营商规划的NITZ信息发生变化，AMF将向UE传递新规划的NITZ信息。 
为了不过度消耗网络资源，AMF并不是实时地向UE传递更新NITZ信息，而是待用户活动后，再将变化后的NITZ信息传递给UE。 
数据规划 :场景|配置项|参数|取值
---|---|---|---
UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|携带NI|携带网络名称
携带TZ|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|携带时区
初始注册流程是否携带NITZ|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|初始注册流程携带NITZ
携带国家名缩写|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|携带国家名缩写
长网络名称编码方式|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|长网络名称编码用UCS2
长网络名称|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|chinamobile
短网络名称编码方式|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|短网络名称编码用UCS2
短网络名称|UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|cmcc
UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|携带NI|携带网络名称
携带TZ|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|携带时区
跨AMF流程是否携带NITZ|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|跨AMF流程携带NITZ
携带国家名缩写|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|携带国家名缩写
长网络名称编码方式|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|长网络名称编码用UCS2
长网络名称|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|chinamobile
短网络名称编码方式|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|短网络名称编码用UCS2
短网络名称|UE移动到新的时区时，AMF通知UE更新TZ信息。|修改网络标识和时区配置|cmcc
配置步骤 :场景|说明|操作
---|---|---
UE首次接入AMF时，AMF将NITZ信息传递给UE|修改网络标识和时区配置|SET NITZCFG:CARRYNI="CARRYNI",CARRYTZ="CARRYTZ",INTIALREG="CARRYININTIALREG",ADDCI="CARRYCI",FULLNICODEPLAN="FULLUSEUCS2",FULLNI="chinamobile",SHORTNICODEPLAN="SHORTUSEUCS2",SHORTNI="cmcc"
运营商规划的NITZ信息发生变化，AMF将向UE传递新规划的NITZ信息。|修改网络标识和时区配置|SET NITZCFG:CARRYNI="CARRYNI",CARRYTZ="CARRYTZ",INTERAMF="CARRYININTERAMFREG",ADDCI="CARRYCI",FULLNICODEPLAN="FULLUSEUCS2",FULLNI="chinamobile",SHORTNICODEPLAN="SHORTUSEUCS2",SHORTNI="cmcc"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|UE首次接入网络，AMF将NITZ信息下发给UE
---|---
测试目的|UE首次接入AMF时，AMF将NITZ信息下发给UE。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|终端向AMF发起初始注册，AMF设置“初始注册流程是否携带NITZ”为“初始注册流程携带NITZ”。
通过准则|检查AMF下发的Configuration update command消息包含NITZ信息。
测试结果|–
测试项目|UE发起跨局移动，AMF将NITZ信息下发给UE
---|---
测试目的|UE跨局接入AMF时，AMF将NITZ信息下发给UE。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|终端跨AMF移动性注册，AMF设置“跨AMF流程是否携带NITZ”。
通过准则|AMF在Configuration update command消息给终端下发NITZ信息。
测试结果|–
测试项目|UE发起跨RAT移动，AMF将NITZ信息下发给UE
---|---
测试目的|验证UE跨RAT接入AMF时，AMF能否将NITZ信息下发给UE。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|终端从4G移动性注册到5G，AMF设置“跨RAT流程是否携带NITZ”。
通过准则|AMF在Configuration update command消息给终端下发NITZ信息。
测试结果|–
测试项目|UE发起周期性注册，AMF将NITZ信息下发给UE
---|---
测试目的|验证UE在AMF进行周期性注册，AMF能否将NITZ信息下发给UE。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|终端在AMF进行周期性注册，AMF设置“周期性注册流程是否携带NITZ”。
通过准则|AMF在Configuration update command消息给终端下发NITZ信息。
测试结果|–
测试项目|UE发起局内移动，AMF将NITZ信息下发给UE
---|---
测试目的|验证UE在AMF内局内注册，AMF能否将NITZ信息下发给UE。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|终端在AMF内局内注册，AMF设置“局内移动性注册流程是否携带NITZ”。
通过准则|AMF在Configuration update command消息给终端下发NITZ信息。
测试结果|–
常见问题处理 :无。 
## ZUF-79-03-011 区域限制 
特性描述 :描述 :定义 :AMF区域限制是移动接入限制的一种方式，是指AMF基于本地配置策略对特定区域下的特定用户进行接入控制。
背景知识 :在移动通信网络中，运营商可以为不同的用户提供不同的接入控制方式，如拒绝其他运营商用户接入到本网络，或拒绝某些特定用户接入到某些特定区域。 
在5G协议中，明确定义了如下三种接入限制方式：RAT限制（RAT Restriction ）、核心网络类型限制（Core Network Type Restriction）、禁止区域（Forbidden Area）。但是，这三种方式还有如下一些缺点：
RAT限制只能根据用户的无线接入类型进行控制，无法针对指定区域进行控制。 
核心网络类型限制只能根据用户的接入核心网络类型进行控制，无法针对指定区域进行控制。 
Forbidden Area限制只能控制用户在指定区域限制接入，无法控制用户在指定区域允许接入。 
这三种限制方式都基于用户UDM签约，当漫游用户接入拜访地网络时，如果该用户在归属地UDM没有签约接入限制，则拜访地网络将无法对这类用户进行接入控制。 
这三种限制方式都基于用户UDM签约，需要UDM通过获取签约数据接口，将每个用户的签约数据都传递给AMF，增加了接口带宽消耗。特别是针对Forbidden Area限制区域，如果限制区域包含的区域特别多，UDM传递给AMF时将大大增加接口带宽消耗。 
为此，AMF提供另外一种接入限制控制方式：AMF区域限制。使用AMF区域限制方式不依赖UDM签约，基于AMF本地配置策略，即可对特定区域下的特定用户进行接入控制（允许接入或者禁止接入）。 
应用场景 :AMF区域限制的应用场景： 
指定区域，只允许特定用户接入。运营商希望划定某些管控区域，在这些区域下只允许特定用户接入。指定区域下，只有特定用户允许接入，其他用户禁止接入；默认区域下，所有用户都可以接入。如图1所示。图1  指定区域，只允许特定用户接入 
指定区域，禁止特定用户接入运营商希望限制某些漫游用户的接入区域，为此指定一些区域，在这些区域下，漫游用户禁止接入。指定区域下，特定用户禁止接入，其他用户允许接入；默认区域下，所有用户都可以接入。如图2所示。图2  指定区域，禁止特定用户接入 
默认区域，禁止特定用户接入运营商希望禁止某些特定用户接入其网络下的默认区域。默认区域下，特定用户禁止接入，其他用户允许接入；指定区域下，所有用户都可以接入。图3  默认区域，禁止特定用户接入 
客户收益 :受益方|受益描述
---|---
运营商|为运营商提供灵活的移动接入限制策略，精细化控制用户接入区域，避免用户访问网络中非授权区域。
移动用户|此特性对终端用户不可见。
实现原理 :系统架构 :在5G网络中，用户通过AMF接入网络，组网架构如[图1]所示。UE在不同的区域接入网络时，AMF可以对UE进行接入控制。
图1  组网架构

涉及的网元 :网元名称|网元作用
---|---
UE|UE识别AMF下发的区域限制，接收到返回的消息中有特定的5GMM原因消息，将当前区域加入禁止区域，后续不再在该区域继续尝试接入AMF。
协议栈 :该特性涉及的接口协议栈参见表1。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
本网元实现 :在初始注册和注册更新流程中，AMF在获取到用户号码后，根据用户号码和当前接入区域，基于本地配置的区域限制策略，进行接入限制判断，允许用户接入或者拒绝用户接入。 
用户号码类型，可以是SUPI、GPSI、PEI。 
限制区域，可以是TA区域、PLMN区域、整个AMF区域。 
业务流程 :本特性的业务流程如[图2]所示。
图2  业务流程

流程说明： 
UE发起注册流程，向AMF发送Registration request消息。 
AMF获取到用户号码。 
AMF对用户的号段区域限制接入判断。 
根据判断结果返还给UE。 
如果判断结果为限制接入，则向UE发送Registration reject消息，携带配置的限制接入原因，流程结束。 
如果判断结果为允许接入，流程继续，最终接入成功，给UE发送Registration
accept消息，消息中携带AMF给UE分配的注册区域（TA List），该注册区域不包含限制接入区域。 
系统影响 :AMF区域限制功能开启后，AMF需要根据用户号段和区域进行查询匹配决策用户接入策略，会消耗一定的系统资源。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议编号|协议名称
---|---
TS 23.501|System Architecture for the 5G System
TS 23.502|Procedures for the 5G System
TS 24.501|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage3
TS 29.503|Unified Data ManagementServices; Stage 3
TS 38.413|NG Application Protocol(NGAP)
特性能力 :名称|指标
---|---
SUPI号段区域限制区域最大个数|1024个区域
SUPI号段区域限制配置最大记录数|200000条记录
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.40|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
√|√|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增的配置项参见[表1]。
配置项|命令
---|---
限制区域配置|ADD RESTRICTAREACFG
SET RESTRICTAREACFG|限制区域配置
DEL RESTRICTAREACFG|限制区域配置
SHOW RESTRICTAREACFG|限制区域配置
号段区域限制策略配置|SET NUMSEGRESTAREADEFPOLICFG
SHOW NUMSEGRESTAREADEFPOLICFG|号段区域限制策略配置
号段区域限制配置|ADD NUMSEGRESTAREACFG
SET NUMSEGRESTAREACFG|号段区域限制配置
DEL NUMSEGRESTAREACFG|号段区域限制配置
SHOW NUMSEGRESTAREACFG|号段区域限制配置
##### 计数器 
新增的计数器参见[表2]。
测量类型|描述
---|---
基于接入类型附着流程测量|编号为46501开头的所有计数器。
基于接入类型跟踪区更新流程测量|编号为46502开头的所有计数器。
告警和通知 :新增的告警和通知参见[表3]。
告警和通知
---
2114322676 SGs口VLR局向不可达
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :待补充
配置说明 :为支持区域限制功能，需要根据限制需要，配置某些号段到号段区域限制配置中。 
该区域限制配置关联到一个或多个限制区域，这些限制区域在限制区域配置中，每个区域定义了一组限制区域。 
该功能包含的配置为： 
限制区域配置：用于配置一个或一组区域，可以基于该区域来指定用户在这些区域是否接入受限。 
号段区域限制策略配置：用于配置该功能的开关，对IMSI、ISDN、IMEI这三种类型分别给出开关控制是否支持基于该号码类型的接入限制。同时还给出支持限制但没有匹配到号段时的默认限制策略。还有策略配置在后面的章节详述。 
号段区域限制配置：用于配置某个号段在哪些区域是否受限。号段区分号码类型、区域也区分区域类型。通过关联的限制区域配置的某个区域来决定是否受限。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
配置过程 :配置功能开关和默认策略。 
执行[SET NUMSEGRESTAREADEFPOLICFG]命令，配置是否启用某类号码是否支持区域限制，以及缺省的限制策略等。
配置限制区域的TA组。 
执行ADD TAGROUPCFG命令，配置TA组，该组会该限制区域配置关联，用于定义区域限制的区域范围。 
执行ADD RESTRICTAREACFG命令，配置一个限制区域，该区域可以是全网范围、单个PLMN、TA组配置所配的某个TA组。 
配置号段区域限制。 
执行[ADD NUMSEGRESTAREACFG]命令，配置号段区域限制，该配置将某个号段跟限制区域关联，并指定该号段在该区域是否受限，以及受限的原因值。
配置实例 :概述 :本配置涉及到不同的号码类型，不同的区域类型，是否受限。还提供了通配号段，默认限制策略，分配注册区域时剔除SUPI、GPSI、PEI号段接入限制区域。配置非常灵活，支持各种区域限制配置。该数据时应当严格按照规划数据进行配置。 
本功能的配置实例，仅给出几类主要的配置方式，作为参考，并不代表其它配置方式不支持。 
##### 配置SUPI号段在TA组受限 
场景说明
支持基于SUPI号段的区域限制。 
SUPI号段关联一个TA组的区域，在该区域受限，指定限制的原因，和性能统计计数器。 
数据规划
配置项|参数|取值
---|---|---
修改号段区域限制策略配置|是否支持基于SUPI号段的区域限制|是
配置TA组|跟踪区组标识|1
移动国家码|配置TA组|460
移动网络码|配置TA组|01
跟踪区码|配置TA组|000001
跟踪区码起始|配置TA组|000002
跟踪区终止|配置TA组|000003
跟踪区组类型|配置TA组|COMMONTYPE
配置限制区域|限制区域标识|1
限制区域类型|配置限制区域|TA组区域
移动国家码|配置限制区域|FFF
移动网络码|配置限制区域|FFF
跟踪区组标识|配置限制区域|1（关联TA组配置里的TA组）
配置号段区域限制|号段|46001
号段类型|配置号段区域限制|SUPI
限制区域标识|配置号段区域限制|1（关联配置限制区域配置里的限制区域标识）
接入限制策略|配置号段区域限制|限制
接入限制原因|配置号段区域限制|3 - Illegal UE
计数归类|配置号段区域限制|3
配置步骤
步骤|说明|操作
---|---|---
1|配置支持基于SUPI号段的区域限制。|SET NUMSEGRESTAREADEFPOLICFG:SUPPAREARESTSUPI="SUPPAREARESTSUPI"
2|配置TA组。|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="01",TAC="000001",TACST="000002",TACEND="000003",TAGRPTYPE="COMMONTYPE"
3|配置限制区域。|ADD RESTRICTAREACFG:RESAREAID=1,RESAREATYPE="TAGROUPAREA",MCC="FFF",MNC="FFF",TAGRPID=1
4|配置号段区域限制|ADD NUMSEGRESTAREACFG:NUMBERSEG="46001",NUMBERTYPE="ACCESSRESTNUMSUPI",RESAREAID=1,ACCRESTPOLICY="RESTACCESSAREA",ACCRESTCAUSE="ILLEGALUE",COUNTER=3
##### 配置GPSI号段在PLMN不受限 
场景说明
支持基于GPSI号段的区域限制。 
GPSI号段关联一个PLMN区域，在该区域不受限。 
数据规划
配置项|参数|取值
---|---|---
修改号段区域限制策略配置|是否支持基于GPSI号段的区域限制|是
配置限制区域|限制区域标识|2
限制区域类型|配置限制区域|PLMN区域
移动国家码|配置限制区域|460
移动网络码|配置限制区域|01
跟踪区组标识|配置限制区域|0
配置号段区域限制|号段|86138
号段类型|配置号段区域限制|GPSI
限制区域标识|配置号段区域限制|2
接入限制策略|配置号段区域限制|不限制
接入限制原因|配置号段区域限制|3 - Illegal UE
计数归类|配置号段区域限制|3
配置步骤
步骤|说明|操作
---|---|---
1|配置支持基于GPSI号段的区域限制。|SET NUMSEGRESTAREADEFPOLICFG:SUPPAREARESTGPSI="SUPPAREARESTGPSI"
2|配置限制区域。|ADD RESTRICTAREACFG:RESAREAID=2,RESAREATYPE="PLMNAREA",MCC="460",MNC="01",TAGRPID=0
3|配置号段区域限制。|ADD NUMSEGRESTAREACFG:NUMBERSEG="86138",NUMBERTYPE="ACCESSRESTNUMGPSI",RESAREAID=2,ACCRESTPOLICY="NOTRESTACCESSAREA",ACCRESTCAUSE="ILLEGALUE",COUNTER=3
##### 配置PEI号段的通配号段在全网范围内受限 
场景说明
支持基于PEI号段的区域限制。 
PEI号段的通配号段关联一个全网的区域，在该区域受限，指定限制的原因，和性能统计计数器。 
通配号段是指所有PEI号码均匹配。号段配置为NULL。 
数据规划
配置项|参数|取值
---|---|---
修改号段区域限制策略配置|是否支持基于PEI号段的区域限制|是
配置限制区域|限制区域标识|3
限制区域类型|配置限制区域|整个AMF区域
移动国家码|配置限制区域|FFF
移动网络码|配置限制区域|FFF
跟踪区组标识|配置限制区域|0
配置号段区域限制|号段|NULL（表明是通配号码，所有号码均匹配上）
号段类型|配置号段区域限制|PEI
限制区域标识|配置号段区域限制|3（关联配置限制区域配置里限制区域标识）
接入限制策略|配置号段区域限制|限制
接入限制原因|配置号段区域限制|27 - N1 mode not allowed
计数归类|配置号段区域限制|27
配置步骤
步骤|说明|操作
---|---|---
1|配置支持基于PEI号段的区域限制。|SET NUMSEGRESTAREADEFPOLICFG:SUPPAREARESTPEI="SUPPAREARESTPEI"
2|配置限制区域。|ADD RESTRICTAREACFG:RESAREAID=3,RESAREATYPE="AllAMFAREA",MCC="FFF",MNC="FFF",TAGRPID=0
3|配置号段区域限制。|ADD NUMSEGRESTAREACFG:NUMBERSEG="NULL",NUMBERTYPE="ACCESSRESTNUMPEI",RESAREAID=3,ACCRESTPOLICY="RESTACCESSAREA",ACCRESTCAUSE="N1MODENOTALLOWED",COUNTER=27
##### 配置GPSI号段不在号段区域限制配置里，默认限制策略为限制 
场景说明
支持基于GPSI号段的区域限制。 
ISDN号段关联一个PLMN区域，在该区域不受限。 
当前ISDN号码（86138XXXX）并不在配置的ISDN号段86135内，默认GPSI限制策略为限制。 
数据规划
配置项|参数|取值
---|---|---
修改号段区域限制策略配置|是否支持基于GPSI号段的区域限制|是
缺省的基于GPSI号段的区域限制策略|修改号段区域限制策略配置|限制
缺省的基于GPSI号段的区域限制原因|修改号段区域限制策略配置|27 - N1 mode not allowed
缺省的GPSI区域限制计数归类|修改号段区域限制策略配置|27
配置限制区域|限制区域标识|4
限制区域类型|配置限制区域|PLMN区域
移动国家码|配置限制区域|460
移动网络码|配置限制区域|01
跟踪区组标识|配置限制区域|0
配置号段区域限制|号段|86135
号段类型|配置号段区域限制|GPSI
限制区域标识|配置号段区域限制|4
接入限制策略|配置号段区域限制|不限制
接入限制原因|配置号段区域限制|3 - Illegal UE
计数归类|配置号段区域限制|3
配置步骤
步骤|说明|操作
---|---|---
1|修改号段区域限制策略配置。|SET NUMSEGRESTAREADEFPOLICFG:SUPPAREARESTGPSI="SUPPAREARESTGPSI",DFTAREARESTPOLIGPSI="DEFRESTAREAGPSI",DFTAREARESCAUSEGPSI="N1MODENOTALLOWED",COUNTERGPSI=27
2|配置限制区域。|ADD RESTRICTAREACFG:RESAREAID=4,RESAREATYPE="PLMNAREA",MCC="460",MNC="01",TAGRPID=0
3|配置号段区域限制。|ADD NUMSEGRESTAREACFG:NUMBERSEG="86135",NUMBERTYPE="ACCESSRESTNUMGPSI",RESAREAID=4,ACCRESTPOLICY="NOTRESTACCESSAREA",ACCRESTCAUSE="ILLEGALUE",COUNTER=3
##### 配置TA根据号段受限后从分配的注册区域列表中剔除 
场景说明
支持基于GPSI号段的区域限制。 
ISDN号段关联一个TA组区域，在该区域受限。 
当前ISDN号码（86138XXXX）跟当前TA不在受限区域，但当前TA所在注册区域里的其它TA有的处于受限区域依据剔除策略，将受收的TA从分配的注册区域列表中剔除。 
数据规划
配置项|参数|取值
---|---|---
修改号段区域限制策略配置|是否支持基于GPSI号段的区域限制|是
分配注册区域时剔除GPSI号段接入限制区域|修改号段区域限制策略配置|是
缺省的基于GPSI号段的区域限制原因|修改号段区域限制策略配置|27 - N1 mode not allowed
缺省的GPSI区域限制计数归类|修改号段区域限制策略配置|27
配置TA组|跟踪区组标识|1、5
移动国家码|配置TA组|460
移动网络码|配置TA组|01
跟踪区码|配置TA组|000001、000004
跟踪区码起始|配置TA组|000002、000005
跟踪区终止|配置TA组|000003、000006
跟踪区组类型|配置TA组|COMMONTYPE
增加注册区域|注册区域ID|1、1
跟踪区标识|增加注册区域|1、5
配置限制区域|限制区域标识|5
限制区域类型|配置限制区域|TA组区域
移动国家码|配置限制区域|FFF
移动网络码|配置限制区域|FFF
跟踪区组标识|配置限制区域|5（关联TA组配置里的）
配置号段区域限制|号段|86135
号段类型|配置号段区域限制|GPSI
限制区域标识|配置号段区域限制|5
接入限制策略|配置号段区域限制|限制
接入限制原因|配置号段区域限制|3 - Illegal UE
计数归类|配置号段区域限制|3
配置步骤
步骤|说明|操作
---|---|---
1|修改号段区域限制策略配置。|SET NUMSEGRESTAREADEFPOLICFG:SUPPAREARESTGPSI="SUPPAREARESTGPSI",DFTAREARESTPOLIGPSI="DEFRESTAREAGPSI",DFTAREARESCAUSEGPSI="N1MODENOTALLOWED",COUNTERGPSI=27
2|配置TA组。|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="01",TAC="000001",TACST="000002",TACEND="000003",TAGRPTYPE="COMMONTYPE"ADD TAGROUPCFG:TAGROUPID=5,MCC="460",MNC="01",TAC="000004",TACST="000005",TACEND="000006",TAGRPTYPE="COMMONTYPE"
3|增加注册区域。|ADD REGAREA TAIDLIST:REGAREAID=1,TAID=1ADD REGAREA TAIDLIST:REGAREAID=1,TAID=5
4|配置限制区域。|ADD RESTRICTAREACFG:RESAREAID=5,RESAREATYPE="PLMNAREA",MCC="FFF",MNC="FFF",TAGRPID=5
5|配置号段区域限制。|ADD NUMSEGRESTAREACFG:NUMBERSEG="86135",NUMBERTYPE="ACCESSRESTNUMGPSI",RESAREAID=5,ACCRESTPOLICY="NOTRESTACCESSAREA",ACCRESTCAUSE="ILLEGALUE",COUNTER=3
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|配置SUPI号段在TA组受限
---|---
测试目的|根据SUPI号段和TA组区域配置用户受限
预置条件|修改号段区域限制策略配置，支持基于SUPI号段的区域限制。配置当前TA所在的TA组到限制区域。配置号段区域限制中，配置用户SUPI号码的号码段关联所配限制区域，策略为受限。
测试过程|用户发起初始注册。
通过准则|注册流程失败，UE收到注册拒绝，带的拒绝原因值为号段区域限制中所配原因值。
测试结果|–
测试项目|配置GPSI号段在PLMN区域不受限
---|---
测试目的|根据GPSI号段和PLMN区域区域配置用户不受限
预置条件|修改号段区域限制策略配置，不支持基于GPSI号段的区域限制。配置当前PLMN区域到限制区域。配置号段区域限制中，配置用户GPSI号码的号码段关联所配限制区域，策略为不受限。
测试过程|用户发起初始注册。
通过准则|注册流程成功。
测试结果|–
测试项目|配置PEI号段在全网范围受限
---|---
测试目的|根据PEI号段和全网区域配置用户受限。
预置条件|修改号段区域限制策略配置，支持基于PEI号段的区域限制。配置全网区域到限制区域。配置号段区域限制中，配置用户PEI号码的号码段关联所配限制区域，策略为受限。
测试过程|用户发起初始注册。
通过准则|注册流程失败，UE收到注册拒绝，带的拒绝原因值为号段区域限制中所配原因值。
测试结果|–
测试项目|配置GPSI号段不在限制区域，默认策略为受限
---|---
测试目的|根据GPSI号段以默认策略来控制接入受限。
预置条件|修改号段区域限制策略配置，支持基于GPSI号段的区域限制，GPSI默认策略为受限。GPSI号段关联一个PLMN区域，在该区域不受限。配置号段区域限制中，配置用户GPSI号码的号码段关联所配限制区域，策略为不受限。
测试过程|用户发起初始注册。
通过准则|注册流程失败，UE收到注册拒绝，带的拒绝原因值为GPSI默认策略中所配原因值。
测试结果|–
测试项目|配置TA根据号段受限后，从分配的注册区域列表中剔除
---|---
测试目的|TA根据号段受限后，从分配的注册区域列表中剔除。
预置条件|修改号段区域限制策略配置，支持基于GPSI号段的区域限制为，支持分配注册区域时剔除GPSI号段接入限制区域。配置两个TA组，其中当前TA所在的TA组不在受限区域，而注册区域中另一TA组在受限区域。配置号段区域限制中，配置用户GPSI号码的号码段关联所配限制区域，策略为受限。
测试过程|用户发起初始注册
通过准则|注册流程成功，注册接受分配注册区域时，只包含当前TA，不包含注册区域中因接入受限而被剔除的TA。
测试结果|–
常见问题处理 :无 
## ZUF-79-03-012 ODB限制 
特性描述 :特性描述 :描述 :定义 :ODB即运营商决策的限制，运营商能够通过设置ODB参数，来对用户的某些类别的业务或者全部业务进行限制。
背景知识 :业务限制分为是用户签约限制、运营商决策限制（ODB）两种。 
用户签约限制是用户和运营商没有签约某些业务，导致运营商限制用户使用这些业务。 
运营商决策限制是用户和运营商之间签约了业务，但是满足某些条件时（比如用户欠费），运营商决策需要对用户业务进行限制。ODB限制业务将立即生效，用户当前受限业务被实时终止，用户后续触发受限业务将被拒绝。ODB限制可以降低运营商的财务风险，对于欠费用户予以进行实时的业务限制，避免欠费用户继续使用业务。 
应用场景 :运营商通过设置ODB参数，来对用户的某些类别的业务或者全部业务进行限制，支持的限制类型如下：
禁止所有分组业务当签约用户欠费时，运营商可以设置ODB参数为“ 支持禁止所有分组业务”，禁止用户使用任何分组业务，避免用户恶意欠费使用业务。 
禁止漫游用户HPLMN接入业务 
禁止漫游用户VPLMN接入业务当签约用户漫游到其他运营商网络时，归属运营商可以设置ODB参数为“支持禁止漫游用户HPLMN接入业务”或者“支持禁止漫游用户VPLMN接入业务”，便于运营商之间的费用结算，减少不必要的话费纠纷。 
客户收益 :受益方|受益描述
---|---
运营商|运营商可以根据用户状态设置ODB参数，灵活限制用户部分业务或者全部业务，避免用户欠费使用业务，降低运营财务风险。
移动用户|移动用户签约业务但是欠费后，运营商可以主动触发ODB限制，限制用户继续使用业务，避免用户在不知情的状况下继续使用业务，导致高额欠费。
实现原理 :系统架构 :本特性涉及的系统架构如[图1]所示。
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
UDM|签约ODB参数，将ODB参数传递给AMF。
AMF|接受UDM传递的ODB参数，根据ODB指示实施ODB限制。
SMF|接受AMF的PDU释放请求指示，发起PDU释放流程。
协议栈 :接口|描述|协议栈
---|---|---
N1|UE与AMF间逻辑接口|ZUF-79-19-001 N1
N8|UDM与AMF间逻辑接口|ZUF-79-19-003 N8
N11|SMF与AMF间逻辑接口|ZUF-79-19-004 N11
本网元实现 :AMF接受UDM下发的ODB签约参数，根据ODB签约指示，实施ODB业务限制。 
ODB指示禁止所有分组业务：AMF根据本地策略，可以拒绝用户接入，也可以允许用户接入。如果允许用户接入，AMF将通知SMF去激活已经存在的PDU会话，拒绝UE后续发起的PDU激活流程。 
ODB指示禁止漫游用户HPLMN接入业务：对于漫游用户接入HPLMN的PDU会话，AMF通知SMF发起释放流程；对于漫游用户新发起的接入HPLMN的PDU激活流程，AMF做拒绝处理。 
ODB指示禁止漫游用户VPLMN接入业务：对于漫游用户接入VPLMN的PDU会话，AMF通知SMF发起释放流程；对于漫游用户新发起的接入VPLMN的PDU激活流程，AMF做拒绝处理。 
业务流程 :UDM通过签约变更下发ODB限制
UDM通过签约变更下发ODB限制的流程如[图2]所示。
图2  UDM通过签约变更下发ODB限制流程

运营商签约ODB限制，UDM向AMF发起签约变更通知，携带ODB限制签约数据，指示AMF实施ODB业务限制。 
AMF根据ODB限制进行决策。 
如果ODB限制用户接入，AMF发起网络侧去注册流程。 
如果ODB允许用户接入，AMF通知SMF释放满足ODB条件的PDU会话。 
UE发起注册流程时的ODB限制处理
UE发起注册流程时的ODB限制处理流程如[图3]所示。
图3  UE发起注册流程时的ODB限制处理流程

UE向AMF发起注册流程。 
（可选）AMF从UDM上获取到签约数据，发现有ODB业务限制指示。 
AMF根据ODB限制进行决策。 
如果ODB限制用户接入，AMF向UE返回注册拒绝消息，拒绝用户接入。 
如果ODB允许用户接入，AMF向UE返回注册接受消息，并通知SMF释放满足ODB条件的PDU会话。 
UE发起PDU激活时的ODB限制处理
UE发起PDU激活时的ODB限制处理流程如[图4]所示。
图4  UE发起PDU激活时的ODB限制处理流程

UE发起PDU激活流程，向AMF发送UL NAS TRANSPORT消息，携带PDU激活请求消息。 
AMF检查到用户有ODB限制签约数据，如果用户激活的PDU会话满足ODB限制条件，则AMF拒绝UE发起的PDU激活流程。AMF向UE返回DL NAS TRANSPORT消息，携带PDU激活请求消息及EMM Cause。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :本特性需要和UDM配合完成，要求UDM支持ODB签约信息，能够将ODB签约数据传递给AMF。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准名称
---|---
3GPP|TS 23.015 Technical realization of Operator Determined Barring (ODB)
TS 22.041 Operator Determined Barring|3GPP
TS 29.503 5G System; Unified Data Management Services|3GPP
TS 29.571 5G System; Common Data Types for Service Based Interfaces|3GPP
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.40|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|SMF|UDM
---|---|---|---|---|---
-|-|-|-|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项|命令
---|---
ODB配置|SET 5GODBCFG
SHOW 5GODBCFG|ODB配置
###### 性能统计1 
性能计数器名称
---
C510260007 由于ODB限制拒绝的会话请求个数
C510070009 发送 Nsmf_PDUSession_Update SM Context Request携带释放指示次数（ODB原因）
C510010090 初始注册失败次数（27.ODB-N1模式不允许_ODB原因）
C510010091 紧急注册失败次数（27.ODB-N1模式不允许_ODB原因）
C510010092 初始注册（语音中心）失败次数（27.ODB-N1模式不允许_ODB原因）
C510010093 初始注册（数据中心）失败次数（27.ODB-N1模式不允许_ODB原因）
C510020068 移动性注册失败次数（27.ODB-N1模式不允许_ODB原因）
C510020069 周期性注册失败次数（27.ODB-N1模式不允许_ODB原因）
C510030007 UDM发起的去注册请求次数（ODB原因）
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :运营商通过设置ODB参数，对用户的某些类别的业务或者全部业务进行限制。
分组数据业务的ODB限制，由UDM和AMF两者配合实现。要求UDM支持ODB签约信息，能够根据签约数据决定是否触发ODB业务。如果UDM签约对分组数据业务进行ODB限制，AMF也配置了支持ODB限制功能，则AMF实施对应分组业务的ODB限制。 
通过AMF ODB配置，结合UDM ODB签约信息，AMF可以进行以下类别的ODB限制。 
禁止所有分组业务 
禁止漫游用户HPLMN接入业务 
禁止漫游用户VPLMN接入业务 
配置前提 :AMF以及周边网元运行正常 
AMF网管能正常连接 
配置过程 :根据场景需求，执行[SET 5GODBCFG]命令，设置ODB参数。
配置实例 :场景一 :场景说明
当签约用户欠费时，运营商可以设置ODB参数为“支持禁止所有分组业务”，禁止用户使用任何分组业务，避免用户恶意欠费。 
AMF支持所有分组业务受限，且AMF禁止所有分组业务时，用户接入策略为禁止用户接入，UDM对该用户设置基于分组业务的ODB限制，类型为限制所有分组业务。 
如果用户发起PDU激活流程，则AMF予以拒绝。 
如果用户在配置修改前已经成功激活PDU会话，则AMF对该用户发起PDU释放，向SMF发送Nsmf_PDUSession_UpdateSMContext消息，携带Release Indication指示以及Cause（取值为REL_DUE_TO_SUBSCRIPTION_CHANGE）。 
如果用户发起注册请求，则AMF拒绝用户接入，向UE返回注册拒绝消息。 
如果用户已经注册，则AMF会收到UDM的去注册通知，AMF执行去注册UE。 
数据规划
配置项|参数名称|取值
---|---|---
ODB配置|支持禁止所有分组业务|是
禁止所有分组业务时用户接入策略|ODB配置|禁止用户接入
配置步骤
步骤|说明|操作
---|---|---
1|修改ODB配置|SET 5GODBCFG:BARALLPS="YES", BARALLPSREGISTSTRY="FORBID"
场景二 :场景说明
当签约用户欠费时，运营商可以设置ODB参数为“支持禁止所有分组业务”，禁止用户使用任何分组业务，避免用户恶意欠费。 
AMF支持所有分组业务受限，且AMF禁止所有分组业务时，用户接入策略为允许用户接入，UDM对该用户设置基于分组业务的ODB限制，类型为限制所有分组业务。 
如果用户发起注册请求，则AMF继续允许用户接入。 
如果用户已经注册，则AMF会收到UDM的去注册通知，AMF仍然保持UE在线。 
数据规划
配置项|参数名称|取值
---|---|---
ODB配置|支持禁止所有分组业务|是
禁止所有分组业务时用户接入策略|ODB配置|允许用户接入
配置步骤
步骤|说明|操作
---|---|---
1|修改ODB配置|SET 5GODBCFG:BARALLPS="YES",BARALLPSREGISTSTRY="ALLOW"
场景三 :场景说明
当签约用户欠费时，运营商可以设置ODB参数为“支持禁止所有分组业务”，禁止用户使用任何分组业务，避免用户恶意欠费。 
AMF支持所有分组业务受限，且AMF禁止所有分组业务时，用户接入策略为根据业务判断，UDM对该用户设置基于分组业务的ODB限制，类型为限制所有分组业务。 
如果用户发起注册请求且携带激活短消息业务，则AMF继续允许用户接入。 
如果用户已经注册且激活了短消息业务，则AMF会收到UDM的去注册通知，AMF仍然保持UE在线。 
数据规划
配置项|参数名称|取值
---|---|---
ODB配置|支持禁止所有分组业务|是
禁止所有分组业务时用户接入策略|ODB配置|根据业务判断
配置步骤
步骤|说明|操作
---|---|---
1|修改ODB配置|SET 5GODBCFG:BARALLPS="YES",BARALLPSREGISTSTRY="JUDGEBYSERVICE"
###### 场景四 
场景说明
当签约用户漫游到其他运营商网络时，归属运营商可以设置ODB配置参数为“支持禁止漫游用户VPLMN接入业务”，以便运营商之间的费用结算，减少不必要的话费纠纷。 
运营商在UDM上配置用户的基于分组业务的ODB限制，类型为限制漫游用户接入拜访地业务；AMF配置ODB参数为“支持禁止漫游用户VPLMN接入业务”。 
用户漫游到其他运营商网络，UE发起PDU激活流程，在PDU激活过程中接入拜访地SMF，PDU激活失败后，AMF限制UE激活该PDU会话，向UE返回拒绝消息。 
用户漫游到其他运营商网络，UE发起PDU激活流程，在PDU激活过程中接入用户归属地SMF，PDU激活成功后，AMF接受UE激活该PDU会话。 
漫游用户在配置修改前，已经PDU激活成功并连接到拜访地SMF，则AMF对该用户发起PDU释放流程，向SMF发送Nsmf_PDUSession_UpdateSMContext消息，携带Release Indication指示以及Cause（取值为REL_DUE_TO_SUBSCRIPTION_CHANGE）。 
数据规划
配置项|参数名称|取值
---|---|---
ODB配置|支持禁止漫游用户VPLMN接入业务|是
配置步骤
步骤|说明|操作
---|---|---
1|修改ODB配置|SET 5GODBCFG:BARROAMVPLMN="YES"
###### 场景五 
场景说明
当签约用户漫游到其他运营商网络时，归属运营商可以设置ODB配置参数为“支持禁止漫游用户HPLMN接入业务”，以便运营商之间的费用结算，减少不必要的话费纠纷。 
运营商在UDM上配置用户的基于分组业务的ODB限制，类型为限制漫游用户接入归属地业务；AMF配置ODB参数为“支持禁止漫游用户HPLMN接入业务”。 
用户漫游到其他运营商网络，UE发起PDU激活流程，在激活过程中接入归属地SMF，PDU激活失败后，AMF限制UE激活该PDU会话，向UE返回拒绝消息。 
用户漫游到其他运营商网络，UE发起PDU激活流程，在激活过程中接入拜访地SMF，PDU激活成功后，AMF接受UE激活该PDU会话。 
漫游用户在配置修改前，已经PDU激活成功并连接到其归属地的SMF，则AMF对该用户发起PDU释放流程，向SMF发送Nsmf_PDUSession_UpdateSMContext消息，携带Release Indication指示以及Cause（取值为REL_DUE_TO_SUBSCRIPTION_CHANGE）。 
数据规划
配置项|参数名称|取值
---|---|---
ODB配置|支持禁止漫游用户HPLMN接入业务|是
配置步骤
步骤|说明|操作
---|---|---
1|修改ODB配置|SET 5GODBCFG:BARROAMHPLMN="YES"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF支持所有分组业务受限，限制用户激活PDU
---|---
测试目的|所有分组业务受限的用户发起PDU激活时，AMF予以拒绝。
预置条件|运营商在UDM上设置了用户的基于分组业务的ODB限制，类型为限制所有分组业务。用户签约了短消息业务。AMF配置支持所有分组业务的ODB限制。AMF配置所有分组业务限制时，根据业务判断是否允许用户接入。UE发起注册请求成功。
测试过程|AMF接受用户接入网络，用户成功注册。用户发起PDU激活流程。
通过准则|用户发起PDU激活流程，AMF予以拒绝。
测试结果|–
测试项目|AMF支持所有分组业务受限，释放已经激活的PDU
---|---
测试目的|对已经激活PDU并且所有分组业务受限的用户发起PDU释放流程。
预置条件|用户注册成功且PDU建立成功。
测试过程|运营商在UDM上设置了用户的基于分组业务的ODB限制，类型为限制所有分组业务。AMF配置支持所有分组业务的ODB限制。
通过准则|AMF对该用户发起PDU释放流程，向SMF发送Nsmf_PDUSession_UpdateSMContext消息，携带Release Indication指示以及Cause（取值为REL_DUE_TO_SUBSCRIPTION_CHANGE）。
测试结果|–
测试项目|AMF支持所有分组业务受限，限制用户接入
---|---
测试目的|限制新注册用户接入。
预置条件|系统运行正常。
测试过程|运营商在UDM上设置了用户的基于分组业务的ODB限制，类型为限制所有分组业务。AMF配置支持所有分组业务的ODB限制。
通过准则|UE发起注册流程，AMF向UE回复注册拒绝。
测试结果|–
测试项目|AMF支持所有分组业务受限，主送触发UE下线
---|---
测试目的|拒绝已注册用户在线。
预置条件|UE已注册成功。
测试过程|运营商在UDM上设置用户的基于分组业务的ODB限制，类型为限制所有分组业务。AMF配置支持所有分组业务的ODB限制。
通过准则|AMF向UE发起去注册流程，使UE下线。
测试结果|–
测试项目|AMF支持拜访地业务受限，限制拜访地PDU激活
---|---
测试目的|运营商开启漫游用户接入拜访地业务限制，UE新激活的PDU访问拜访地SMF业务受限。
预置条件|运营商在UDM上设置了用户的基于分组业务的ODB限制，类型为限制漫游用户接入拜访地业务。AMF配置ODB参数为“支持禁止漫游用户VPLMN接入业务”。
测试过程|用户漫游到其他运营商网络，UE发起PDU激活，在PDU激活过程中接入拜访地SMF。用户漫游到其他运营商网络，UE发起PDU激活，在PDU激活过程中接入用户归属地SMF。
通过准则|用户接入拜访地SMF的PDU激活失败，AMF限制UE激活该PDU会话，向UE回复激活拒绝消息。用户接入归属地SMF的PDU激活成功，AMF接受UE激活该PDU会话。
测试结果|–
测试项目|AMF支持拜访地业务受限，释放已经接入到拜访地的PDU
---|---
测试目的|运营商开启漫游用户接入拜访地业务限制，对已经激活PDU会话且接入到拜访地SMF的用户发起PDU释放流程。
预置条件|漫游用户注册成功且PDU激活并连接到拜访地SMF成功。
测试过程|运营商在UDM上设置用户的基于分组业务的ODB限制，类型为限制漫游用户接入拜访地业务。AMF配置ODB参数为“支持禁止漫游用户VPLMN接入业务”。
通过准则|AMF对该漫游用户发起PDU释放流程，向SMF发送Nsmf_PDUSession_UpdateSMContext消息，携带Release Indication指示以及Cause（取值为REL_DUE_TO_SUBSCRIPTION_CHANGE）。
测试结果|–
测试项目|AMF支持归属地地业务受限，限制归属地PDU激活
---|---
测试目的|运营商开启漫游用户接入归属地业务限制，UE激活PDU会话后，访问归属地SMF业务受限。
预置条件|运营商在UDM上设置了用户的基于分组业务的ODB限制，类型为限制漫游用户接入归属地业务。AMF配置ODB参数为“支持禁止漫游用户HPLMN接入业务”。
测试过程|用户漫游到其他运营商网络，UE发起PDU激活流程，在PDU激活过程中接入用户归属地SMF。用户漫游到其他运营商网络，UE发起PDU激活流程，在PDU激活过程中接入拜访地SMF。
通过准则|用户接入归属地SMF的PDU激活失败，AMF限制UE激活该PDU会话，向UE回复PDU拒绝消息。用户接入拜访地SMF的PDU激活成功，AMF接受UE激活该PDU会话。
测试结果|–
测试项目|AMF支持归属地业务受限，释放已经接入到归属地的PDU
---|---
测试目的|运营商开启漫游用户接入归属地业务限制，对已经激活PDU会话且接入到归属地SMF的用户发起PDU释放流程。
预置条件|漫游用户注册成功且PDU并连接到归属地SMF成功。
测试过程|运营商在UDM上设置用户的基于分组业务的ODB限制，类型为限制漫游用户接入归属地业务。AMF配置ODB参数为“支持禁止漫游用户HPLMN接入业务”。
通过准则|AMF对该漫游用户发起PDU释放流程，向SMF发送Nsmf_PDUSession_UpdateSMContext消息，携带Release Indication指示以及Cause（取值为REL_DUE_TO_SUBSCRIPTION_CHANGE）。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## 5G-GUTI 
5G Globally Unique Temporary Identity5G全球唯一临时标识
5GC :5G Core Network5G核心网
## 5GS 
5G System5G系统
AMF :Access and Mobility Management Function接入和移动管理功能
## AN 
Access Network接入网
AUSF :Authentication Server Function鉴权服务器功能
EIR :Equipment Identity Register设备标识寄存器
## EPLMN 
Equivalent Public Land Mobile Network对等公用陆地移动网
GPSI :Generic Public Subscription Identifier一般公共用户标识
## MICO 
Mobile Initiated Connection Only仅限移动发起连接
## MM 
Mobility Management移动性管理
MME :Mobility Management Entity移动管理实体
MSC :Mobile Switching Center移动交换中心
NAS :Network Access Service网络接入服务
## NI 
Network Identifier网络标识
## NITZ 
Network Identity and Time Zone网络标志和时区
NRF :NF Repository Function网络功能仓储
## NSSAI 
Network Slice Selection Assistance Information网络切片选择辅助信息
NSSF :Network Slice Selection Function网络切片选择功能
PCF :Policy Control Function策略控制功能
PDU :Packet Data Unit分组数据单元
## PEI 
Permanent Equipment Identifier永久设备标识
PLMN :Public Land Mobile Network公共陆地移动网
RAT :Radio Access Technology无线接入技术
S-NSSAI :Single Network Slice Selection Assistance Information单个网络切片选择辅助信息
SMF :Session Management Function会话管理功能
## SUCI 
Subscription Concealed Identifier用户匿名标识
SUPI :Subscriber Permanent Identifier用户永久标识
TA :Tracking Area跟踪区域
UDM :Unified Data Management统一数据管理
UDR :Unified Data Repository统一数据存储
UE :User Equipment用户设备
UPF :User Plane Function用户平面功能
# ZUF-79-04 连接管理 
## ZUF-79-04-001 AN释放 
特性描述 :特性描述 :术语 :术语|含义
---|---
AN|AN是连接UE和5GC的接入网络，可以通过空口广播网络信息。
QoS Flow|QoS Flow是一个或多个业务数据流SDF的逻辑集合，用于保证和区分不同业务的服务质量（QoS），相似的业务可以映射到同一个QoSFlow上以获得相同的服务质量。
GBR QoS Flow|GBR QoS Flow是运营商需要保证承载其上业务数据速率的一类QoS Flow。
non-GBR QoS Flow|non-GBR QoS Flow是运营商无需保证承载其上业务数据速率的一类QoS Flow。
描述 :定义 :AN释放UE上下文是指释放用户N2接口信令连接、N3接口用户面连接、RRC信令连接和资源的过程，包括(R)AN触发的AN释放UE上下文和AMF触发的AN释放上下文。
背景知识 :对于无线通信系统而言，不论是EPS或者是5GS，无线资源通常都是十分有限的，因此通信系统需要将没有使用或者暂时没有使用的无线资源释放，以提高无线资源的利用效率。
在AN释放UE上下文中，用户的N2连接和N3用户面均被释放，空口的RRC连接和RB连接也会一并被释放，RAN不再保存用户的任何信息，UE和AMF中用户的ECM状态从连接态变为空闲态，non-GBR
QoS Flow会被保留，GBR QoS Flow根据运营商策略，可以被保留或去激活。
AN释放UE上下文之后，用户不能通过5GC网络访问数据业务和其他业务，只有通过业务请求流程，重建用户面通道，才能继续通过5GC网络访问数据业务和其他业务。
应用场景 :常见应用场景如下： 
(R)AN检测到较长时间没有用户活动，主动将N2连接释放。 
用户进入信号极不好的区域，导致RRC连接中断，(R)AN释放N2连接。 
客户收益 :受益方|受益描述
---|---
运营商|可以释放无用或者暂时无用的用户资源，提高系统资源的利用率，特别是无线资源的利用率。
终端用户|该特性对终端客户不可见。
实现原理 :

系统架构 :



AN释放UE上下文的系统架构如[图1]所示。


图1  AN释放UE上下文的系统架构图






涉及的NF/网元参见下表。 


NF/网元|说明
---|---
NF|UPF|负责拆除N3用户面隧道。
NF|SMF|通知UPF删除N3用户面隧道。
NF|AMF|释放N2连接上下文，并通知SMF释放用户面隧道。
网元|(R)AN|释放用户上下文，包括N2连接、RRC连接以及N3用户面隧道。
网元|UE|释放RRC侧无线连接。




业务流程 :AN释放UE上下文流程如[图2]所示。
图2  AN释放UE上下文

流程说明如下。 
(R)AN检测到需要释放UE上下文，则发送UE Context Release Request消息给AMF，携带释放原因值。 
AMF收到(R)AN的UE Context Release Request消息，或者AMF主动释放N2信令连接，则发送UE
Context Release Command消息给(R)AN。 
若UE和(R)AN间存在RRC连接，则(R)AN通知UE释放RRC连接。 
(R)AN回复UE Context Release Complete给AMF进行响应。 
若用户已激活了PDU会话上下文，则AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、导致AN释放UE上下文的原因。 
SMF发送PFCP Session Modification Request消息给UPF，通知UPF释放N3用户面隧道。 
UPF回复PFCP Session Modification Response消息给SMF。 
SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF进行响应。 
NF实现 :AMF实现 :####### SMF实现 
####### UPF实现 
在AN释放UE上下文的特性中，AMF承担如下功能： 
AN释放UE上下文后，AMF负责更新用户在核心网的状态。 
释放核心网侧与N2连接相关的上下文，包括N2连接上下文、AS安全上下文。 
通知SMF释放N3用户面隧道，携带导致释放AN UE上下文的原因。 
在AN释放UE上下文的特性中，SMF承担如下功能： 
通知UPF释放N3用户面隧道。 
若AN释放UE上下文的原因为用户不活动或者UE重定向，则在释放UE上下文后，SMF发起GBR QoS Flow的释放流程。 
在AN释放UE上下文的特性中，UPF承担如下功能： 
接受SMF通知，删除N3用户面隧道。 
缓存后续的下行报文，并发送下行数据通知给SMF，触发网络侧业务请求流程。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP|3GPP TS 23.502|Procedures for the 5G System
3GPP|3GPP TS 29.500|Technical Realization of Service Based Architecture
3GPP|3GPP TS 29.502|Session Management Services
3GPP|3GPP TS 38.413|NGApplication Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性对于工程规划无特别要求。 
O&M相关 :配置命令 :本特性不涉及配置命令的变化。 
定时器 :本特性不涉及定时器的变化。 
性能统计 :新增性能计数器参见下表。 
序号|性能计数器名称
---|---
1|C510510013 收到UE CONTEXT RELEASE REQUEST次数
2|C510510014 发送UE CONTEXT RELEASE COMMAND次数
3|C510510015 收到UE CONTEXT RELEASE COMPLETE次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :本特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现AN释放流程。 
测试用例 :测试项目|RAN发起AN释放
---|---
测试目的|验证AMF正确处理RAN发起的AN释放。
预置条件|RAN，各NF运行正常。
测试过程|UE开机发起注册流程。触发RAN发起AN释放流程。
通过准则|UE注册流程成功。RAN发起的AN释放流程成功，UE处于CM-IDLE状态。
测试结果|-
常见问题处理 :无 
## ZUF-79-04-002 业务请求 
特性描述 :特性描述 :术语 :术语|含义
---|---
PSA|PSA是PDU会话锚点，在5GC中作为UPF，对外出N6接口，充当网关角色。
I-UPF|I-UPF是中间UPF，对gNB出N3接口，对PSA出N9接口，充当中间转发UPF角色。
5G-S-TMSI|5G-S-TMSI是属于5G-GUTI的一部分，在寻呼及业务请求流程中用于无线空口更高效的识别用户，格式如下：<5G-S-TMSI> := <AMF Set ID> <AMF Pointer> <5G-TMSI>
描述 :定义 :业务请求流程用于恢复UE与网络间信令或数据连接。UE在空闲态时可通过业务请求流程建立安全信令连接或数据连接以发送信令、用户数据或响应网络寻呼，UE在连接态时可通过业务请求以激活某个PDU会话的用户面连接和响应网络通知消息。 
ZXUN uMAC通过业务请求功能在UE功耗降低的同时保证了用户的业务体验。
背景知识 :为了降低UE的功耗，当UE无数据业务时，需要释放UE与网络之间的信令和数据连接。 
当UE需要传递信令或数据时，UE会主动触发业务请求流程以恢复与网络的连接。 
当网络侧需要传递信令或数据时，网络侧会主动触发业务请求流程以恢复与UE的连接。 
应用场景 :业务请求的目的是为了恢复网络与UE间的信令或数据连接，用于后续的信令或数据交互。 
具体可分为如下几种场景： 
UE主动信令/数据交互当UE在空闲态下有信令需要发送时（例如UE有短消息需要发送），UE发起业务请求流程与网络侧建立安全连接发送信令。当UE有数据需要发送（例如UE发起语音呼叫），但用户面连接未建立，UE发起业务请求流程激活用户面连接发送数据。 
网络侧触发信令/数据交互当网络侧有信令需要发送给空闲态下的UE时（例如UE有短消息需要接收），网络侧通过寻呼触发业务请求流程与网络侧建立安全连接发送信令。当网络侧有数据需要发送（例如UE作为语音被叫），但用户面连接未建立，网络侧通过寻呼触发业务请求流程激活用户面连接发送数据。 
客户收益 :受益方|受益描述
---|---
运营商|通过业务请求可快速恢复业务，保证用户体验。
终端用户|此特性对终端用户不可见。
实现原理 :系统架构 :本特性涉及的系统架构如[图1]所示。
图1  系统架构

涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|业务请求主处理NF，负责在业务请求过程中建立安全的N2连接及寻呼，并中转与SMF相关的N1/N2消息用于恢复PDU会话的用户面隧道。
AUSF|NF|鉴权服务处理NF，完成用户合法性认证并分配安全秘钥。
SMF|NF|用户会话管理NF，负责在业务请求过程中，完成UE请求或网络侧期望的PDU会话的用户面隧道。
PCF|NF|用户策略控制NF，负责业务请求过程中，因为用户位置变化导致会话策略的更新。
UPF|NF|用户数据转发NF，负责无N3隧道时下行数据缓存并触发寻呼，以及与SMF配合完成用户面隧道恢复。
网元|(R)AN|无线接入网络，业务请求过程中负责寻呼UE、与UE建立无线连接，与AMF建立N2连接并用于中转N1 NAS信令及N3隧道的恢复。
业务流程 :####### UE触发业务请求流程 
UE触发业务请求流程[图2]所示。
图2  UE触发业务请求流程

流程说明如下： 
UE发送Service Request消息给RAN。如果仅用于建立信令连接，则不携带"Uplink data status"字段。如果用于数据连接恢复，则通过"Uplink
data status"字段指示期望恢复的PDU Session。"PDU Session Status"指示UE侧可用的PDU Session。 
RAN侧基于RRC流程中的5G-S-TMSI选择正确的AMF，将Service Request消息发送给AMF。 
AMF对业务请求消息进行合法性校验，如果该消息没有完整性保护或消息完整性保护校验失败，则AMF需要发起安全流程。如果业务请求流程仅用于信令连接建立，则后续步骤4~11及步骤15~22跳过。 
如果Service Request包含"Uplink data status"，AMF调用SMF的服务化接口Nsmf_PDU
Session_Update SM Context Request请求SMF为对应的PDU会话建立用户面连接。 
SMF基于用户位置信息进行UPF选择，决策继续使用当前UPF或重选/新建/删除I-UPF。 
如果CN隧道由UPF分配，且CN隧道信息发生改变，SMF向PSA（Anchor UPF）发送N4 Session Modification
Request消息，请求更新N3及N9及前转隧道信息。如果CN隧道由SMF分配则在步骤7中处理。如果SMF重选或新插入I-UPF，SMF向new
I-UPF发送N4 Session Establishment Request消息请求建立N3/N9及前传隧道端点信息。new I-UPF申请用户面隧道资源成功后向SMF发送N4
Session Establishment Response消息。 
如果SMF重选或新插入I-UPF，SMF向PSA（Anchor UPF）发送N4 Session Modification
Request消息，请求更新N9及前转隧道信息，如果之前A-UPF有下行缓存数据则发送给new I-UPF。如果SMF删除I-UPF，则PSA需要开始缓存N6口下行数据数据报文，并建立前转隧道，为接收从old
I-UPF转发的数据报文做准备。PSA向SMF发送N4 Session Modification Response消息。 
如果SMF重选或删除I-UPF，SMF向old I-UPF发送N4 Session Modification Request消息，携带新的前转隧道端点信息用于old
I-UPF前转数据，同时通知old I-UPF删除N3隧道信息。I-UPF向SMF发送N4 Session Modification
Response消息。 
如果I-UPF改变，且old I-UPF有缓存数据，则old I-UPF向new I-UPF前转数据。 
如果I-UPF删除，且old I-UPF有缓存数据，old I-UPF向PSA前转数据。 
SMF向AMF发送Nsmf_PDU Session_Update SM Context Response响应消息，包含N2
SM信息用于通知RAN更新N3隧道信息。 
AMF向RAN发送N2 Request消息包含N2 SM信息用于RAN侧更新N3隧道信息。 
RAN与UE交互重建用户面承载。 
RAN向AMF发送N2 Request Ack消息包含N2 SM信息用于UPF更新N3隧道RAN侧端点信息。 
AMF调用SMF的服务化接口Nsmf_PDU Session_Update SM Context Request透传N2
SM信息。 
可选的，如果PCF已订阅SMF位置变化信息且UE的位置改变，SMF触发SM策略修改流程。 
如果SMF重选或新插入I-UPF，SMF向new I-UPF发送N4 Session Modification Request消息更新N3隧道RAN侧端点信息，此时I-UPF可以向RAN发送下行数据。new
I-UPF向SMF发送N4 Session Modification Response消息。 
如果SMF删除I-UPF，SMF向PSA发送N4 Session Modification Request消息更新N3隧道RAN侧端点信息，此时PSA可以向RAN发送下行数据。PSA向SMF发送N4
Session Modification Response消息。 
SMF向AMF发送Nsmf_PDU Session_Update SM Context Response响应消息。 
如果new I-UPF已建立前转隧道，且前转隧道定时器超时，SMF向new I-UPF发送N4 Session Modification
Request消息释放前转隧道信息，new I-UPF向SMF发送N4 Session Modification Response消息。 
如果PSA已建立前转隧道，且前转隧道定时器超时，SMF向PSA发送N4 Session Modification Request消息释放前转隧道信息，PSA向SMF发送N4
Session Modification Response消息。 
如果SMF继续使用old I-UPF，SMF向old I-UPF发送N4 Session Modification Request消息更新N3隧道RAN侧端点信息。如果SMF更新或删除I-UPF，SMF在资源保持定时器超时后向old
I-UPF发送N4 Session Release Request消息请求释放用户面资源。old I-UPF向SMF发送N4 Session
Modification Response/N4 Session Release Response消息。 
####### 网络触发业务请求流程 
网络触发业务请求流程如[图3]所示。
图3  网络触发业务请求流程

流程说明如下： 
UPF收到下行数据报文但没有建立N3隧道，UPF本地缓存下行数据报文。 
UFP向SMF发送N4 Data Notification消息，携带下行数据报文对应的QoS Flow信息。SMF向UFP发送N4
Data Notification Ack消息。 
SMF调用AMF的服务化接口Namf_Communication_N1 N2 MessageTransfer携带对应的PDU
Session ID及N2 SM信息。AMF响应SMF的服务化接口调用请求。 
根据UE状态不同，AMF进行不同的处理： 
如果UE处于连接状态，AMF不需要发起寻呼流程，后续流程同[UE触发业务请求流程]步骤3及步骤12~22。
如果UE处理空闲态，AMF向UE所在注册区域内的所有gNB发送寻呼消息。 
AMF启动寻呼流程定时器，如果超时未收到UE响应，AMF向SMF发送Namf_Event Exposure_Notify消息通知寻呼失败，SMF通知UPF。 
UE收到寻呼请求后，发起业务请求流程，同[UE触发业务请求流程]。
UPF向RAN侧传送下行报文。 
NF实现 :AMF实现 :与UE交互，完成业务请求NAS消息交互。 
与NG-RAN交互，完成与UE间NAS的传递及SM信息的转发。 
与SMF交互，完成PDU会话更新及寻呼触发。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N12|ZUF-79-19-005 N12
N22|ZUF-79-19-008 N22
系统影响 :###### AMF系统影响 
AMF需要把寻呼消息发送到注册区域（TAList）下的所有NG-RAN，注册区域中的NG-RAN数越多，寻呼带来的系统负荷越大，TAList/TA范围需要规划合理。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP|3GPP TS 23.502|Procedures for the 5G System
3GPP|3GPP TS 24.501|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage3
3GPP|3GPP TS 29.502|Session ManagementServices; Stage 3
3GPP|3GPP TS 29.518|Access and Mobility Management Services; Stage 3
3GPP|3GPP TS 29.244|Interface between the Control Plane and the User Plane nodes
3GPP|3GPP TS 38.413|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :本特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性对于工程规划无特殊要求。 
O&M相关 :配置命令 :####### AMF配置命令 
配置项|命令
---|---
寻呼策略配置|ADD PAGINGPOLICYCFG
DELETE PAGINGPOLICYCFG|寻呼策略配置
SET PAGINGPOLICYCFG|寻呼策略配置
SHOW PAGINGPOLICYCFG|寻呼策略配置
全局寻呼策略配置|SET GLOBALPOLICY
SHOW GLOBALPOLICY|全局寻呼策略配置
寻呼因子配置|ADD PAGEFACTORCFG
SET PAGEFACTORCFG|寻呼因子配置
DELETE PAGEFACTORCFG|寻呼因子配置
SHOW PAGEFACTORCFG|寻呼因子配置
定时器 :####### AMF定时器 
本特性不涉及AMF定时器变化。 
####### SMF定时器 
本特性不涉及SMF定时器变化。 
####### UPF定时器 
本特性不涉及UPF定时器变化。 
性能统计 :####### AMF性能统计 
测量类型|描述
---|---
业务请求流程测量|编号为51004开头的所有计数器
寻呼流程测量|编号为51301开头的所有计数器
告警和通知 :本特性不涉及告警和通知的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :场景|配置说明
---|---
UE侧触发的业务请求|无需特别配置，只需完成初始配置（含5G安全配置），即可实现业务请求流程。
连接态时网络侧触发的业务请求|无需特别配置，只需完成初始配置（含5G安全配置），即可实现业务请求流程。
空闲态时网络侧触发的业务请求|涉及寻呼流程，需要配置数据，包括寻呼策略配置、全局寻呼策略配置、寻呼因子配置。
 说明： 
5G安全配置用于设置AMF的安全配置，包括注册流程、业务请求流程、去注册流程中鉴权策略和AMF所支持的完整性算法、加密算法及各算法对应的优先级。本特性只涉及5G安全配置中的业务请求控制开关，用于修改业务请求是否鉴权。 
配置过程 :通过[ADD PAGINGPOLICYCFG]命令增加寻呼策略配置。策略内容包括寻呼方式、寻呼消息发送间隔、寻呼的重发次数、批量寻呼发送的个数、用于填写寻呼消息字段中的寻呼优先级。
通过[SET GLOBALPOLICY]命令修改全局寻呼策略配置，全局寻呼策略ID对应的策略内容在寻呼策略配置中查找。
通过[ADD PAGEFACTORCFG]命令增加一条寻呼因子配置，可以使用寻呼因子5QI、PPI、DNN进行任何组合，通过关联寻呼策略ID在寻呼策略配置中查找策略内容。
配置实例 :配置场景 :空闲态时网络侧触发业务请求，且业务请求需鉴权。 
数据规划 :配置|参数|取值|说明
---|---|---|---
寻呼策略配置|PAGINGPOLICYID|1|寻呼策略ID
PAGINGSTYLE|寻呼策略配置|LASTNR|基于最近活动RAN寻呼
PAGINGINTERVAL|寻呼策略配置|50 ms|寻呼间隔
PAGINGTIMES|寻呼策略配置|1|重发次数
BATCHPAGINGNUM|寻呼策略配置|64|批量发送个数
PAGINGPRIORITY|寻呼策略配置|1|寻呼优先级
寻呼因子配置|PAGINGFACTORID|1|寻呼因子ID
FIVEQIFLG|寻呼因子配置|1|5QI
PAGINGPOLICYINDI|寻呼因子配置|2|PPI
DNN|寻呼因子配置|zte.com.cn|DNN
配置步骤 :步骤|说明|操作
---|---|---
1|新增寻呼策略|ADD PAGINGPOLICYCFG:PAGINGPOLICYID=1,PAGINGSTYLE="LASTNR",PAGINGINTERVAL=50,PAGINGTIMES=1,BATCHPAGINGNUM=64,PAGINGPRIORITY=1
2|修改全局寻呼策略|SET GLOBALPOLICY:PAGINGSRVTYPE=DATA,PAGINGTYPE=SMART_PAGING,GLOBALPOLICYGRPID=1
3|新增寻呼因子策略|ADD PAGEFACTORCFG:PAGINGFACTORID=1,PAGINGPOLICYID=1,FIVEQIFLG="WITHFLAG",FIVEQI=1,PPIFLG="WITHFLAG",PAGINGPOLICYINDI=2,DNNFLG="WITHFLAG",DNN="zte.com.cn"
测试用例 :测试项目|UE发起的业务请求
---|---
测试目的|验证UE能够成功发起业务请求过程
预置条件|RAN，各NF运行正常。用户注册成功后释放AN连接，UE处于CM-IDLE状态。
测试过程|UE触发业务请求流程。
通过准则|业务请求流程成功。UE处于CM-CONNECTED状态。
测试结果|-
测试项目|网络侧发起的业务请求
---|---
测试目的|验证网络能够成功发起业务请求过程
预置条件|RAN，各NF运行正常。用户注册，PDU会话建立成功后释放AN连接，UE处于CM-IDLE状态。
测试过程|网络接收到下行数据，触发业务请求流程。
通过准则|网络触发业务请求流程。网络寻呼该UE。业务请求成功，UE处于CM-CONNECTED状态。用户面连接被成功建立，数据业务正常。
测试结果|-
常见问题处理 :无 
## ZUF-79-04-003 智能寻呼 
特性描述 :特性描述 :术语 :术语|含义
---|---
CM-IDLE|5G网络中，用户处于空闲状态时的状态名称。
CM-CONNECTED|5G网络中，用户处于连接状态时的状态名称。
描述 :定义 :策略寻呼是指AMF基于用户类型、业务类型选择相应的寻呼规则，综合用户的移动性，选择合适的范围对用户进行寻呼，从而有效地减少整个RAN的寻呼负荷，节省网络资源。
AMF可以根据不同业务要求，在保证一定寻呼成功率基础上，选择合适的策略进行寻呼。 
背景知识 :引入该特性的意义
5G终端与网络侧进行数据交互时，为了节电会进入IDLE状态。终端处于IDLE状态下，如果此时网络侧有数据需要向终端发送，可通过触发寻呼流程，使终端进入CM-CONNECTED状态，恢复数据传输。 
5G寻呼流程是指：AMF向终端所在的一定的物理区域内的所有gNodeB发送寻呼请求，gNodeB在空口进行广播，当终端收到寻呼请求后，重新建立与网络侧的连接。 
随着5G各种业务爆发式增长，5G寻呼面临着如下挑战： 
寻呼在话务模型中所占比重越来越大，寻呼数量呈指数级增长，极端情况下可能引起信令风暴。 
VoNR语音业务对时延非常敏感，此类业务需要尽量缩短寻呼时延，提升用户体验。 
AMF需要支持策略寻呼，以提供完善的解决方案来应对这些挑战。 
寻呼指标
衡量寻呼的三个关键指标为寻呼负荷、寻呼成功率和寻呼时延。 
寻呼负荷由于寻呼消息具有广播特征，因此需要合理规划寻呼范围，保持寻呼消息在合适范围内进行发送，可有效的降低寻呼负荷，在寻呼区域已合理规划的基础上，通过合理预测用户位置，缩小寻呼范围，可进一步降低寻呼负荷。 
寻呼成功率保证一定寻呼成功率，是业务稳定运行的基础。决定寻呼成功率的要素有：寻呼范围和寻呼次数。缩小寻呼范围可能导致寻呼失败，加大寻呼次数并扩大寻呼范围可提高成功率。 
寻呼时延对于时延敏感的业务（比如语音呼叫），寻呼时需要优先考虑时延影响。对于时延敏感的业务，需要寻呼能够尽快完成。使用TA List寻呼可提高一次寻呼成功率，从而降低寻呼时延 
TA List
AMF基于TA List跟踪CM-IDLE态下用户位置信息，TA List包含若干TA，每一个TA包含若干个gNodeB，如[图1]所示。
图1  TA List

通过TA List的合理规划可有效降低寻呼负荷。 
如果TA List规划太小，会导致终端频繁触发注册更新。 
如果TA List规划太大，会导致寻呼负荷呈指数级增长（一个TA List下包含N个TA，每个TA包含M个gNodeB，采用TA List方式寻呼，一次下行数据触发的寻呼将导致AMF发送N×M条寻呼请求消息给gNodeB）。 
寻呼范围
UE处于CM-IDLE态下，AMF基于分配给UE的TA List来管理用户位置，根据3GPP协议要求，寻呼范围为TA List。如果AMF能够根据UE的移动性预测UE当前的准确位置，则可以缩小寻呼范围，降低寻呼负荷。 
寻呼范围从小到大依次参见[表1]。
序号|寻呼范围|描述
---|---|---
1|最近访问的gNodeB|针对UE上次驻留的gNodeB发起寻呼。
2|最近访问的gNodeB列表|针对UE上次驻留的gNodeB及其相邻gNodeB的寻呼。
3|最近访问的TA|针对UE上次驻留的TA中所有的gNodeB发起寻呼。
4|最近访问的TA列表|针对UE上次驻留的TA及其相邻的TA中所有的gNodeB发起寻呼。
5|分配给UE的完整TA List|3GPP标准寻呼，对TA List下的所有gNodeB发起寻呼，此寻呼范围为AMF的缺省寻呼范围。
根据UE移动性来预测UE准确位置的依据是：每几分钟触发一次寻呼，用户在几分钟时间内活动范围有限（大部分情况下用户处于低速移动或静止不动状态），结合用户最近的历史活动范围，可大致预测用户所在gNodeB/TA。 
应用场景 :概述 :常见的寻呼场景有三种，参见[表2]。在保证一定寻呼成功率基础上，根据不同场景选择不同的寻呼策略。
编号|应用场景|寻呼需求|寻呼策略
---|---|---|---
1|通用类业务的寻呼|对时延及寻呼负荷无特殊要求|智能寻呼
2|负荷敏感类业务的寻呼|寻呼负荷敏感、时延不敏感|精准寻呼
3|时延敏感业务类的寻呼|时延敏感|分业务寻呼
###### 智能寻呼 
场景分析
智能寻呼用于网络负荷不高，对寻呼时延没有特殊要求的情况。在此种情况下，选择寻呼策略时可在时延及寻呼负荷间折衷。 
影响寻呼负荷及时延的关键因素是寻呼范围。寻呼范围过大影响寻呼负荷，寻呼范围过小影响一次寻呼成功率。因此，本场景下合适的寻呼范围是最近访问的TA。同时为保证一定的寻呼成功率，一次寻呼失败后需要扩大寻呼范围再次寻呼。
智能寻呼策略
根据场景分析，智能寻呼策略如下： 
一次寻呼范围：最近访问TA。 
二次寻呼范围：TA List。 
根据实际情况，对于TA List规划建议如下： 
TA List包含的TA数在5个左右。 
TA包含的gNodeB数在20个左右。 
###### 精准寻呼 
场景分析
精准寻呼用于网络负荷较高，同时需要保证一定寻呼成功率的情况。 
网络负荷较高时，需要尽量降低寻呼负荷，一次寻呼的范围需要尽可能小。但缩小寻呼范围会导致寻呼成功率相对降低，如果一次寻呼失败，需要逐步扩大寻呼范围，在降低寻呼负荷的同时保证一定的寻呼成功率。 
精准寻呼策略
根据场景分析，精准寻呼策略如下： 
一次寻呼范围：最近访问gNodeB。 
二次寻呼范围：最近访问gNodeB列表。 
三次寻呼范围：TA List。 
根据实际情况，对于TA List规划建议如下： 
TA List包含的TA数在5个左右。 
TA包含的gNodeB数在20个左右。 
###### 分业务寻呼 
场景分析
在保证一定寻呼成功率基础上，不同业务对寻呼的要求不同： 
语音类业务：要求寻呼时延尽可能短。对于语音类时延敏感业务，通过TA List寻呼来降低一次寻呼失败率，达到降低寻呼时延的目的。 
普通数据业务时延不敏感，寻呼负荷要合适。对于普通数据业务，时延无过高要求，可根据系统负荷情况，选择智能寻呼或精准寻呼。 
分业务寻呼策略
根据场景分析，区分业务寻呼策略参见[表3]。
业务类型|系统负荷|寻呼范围
---|---|---
语音类业务|-|一次寻呼范围：TA List
二次寻呼范围：TA List|语音类业务|-
普通数据业务|系统负荷不高|一次寻呼范围：最近访问TA
二次寻呼范围：TA List|普通数据业务|系统负荷不高
系统负荷较高|普通数据业务|一次寻呼范围：最近访问gNodeB
二次寻呼范围：最近访问gNodeB列表|系统负荷较高|普通数据业务
三次寻呼范围：TA List|系统负荷较高|普通数据业务
根据实际情况，对于TA List规划建议如下： 
TA List包含的TA数在5个左右。 
TA包含的gNodeB数在20个左右。 
客户收益 :受益方|受益描述
---|---
运营商|通过选择合理的寻呼策略，运营商能获得如下收益：节约投资成本：可在保证寻呼成功率及用户体验基础上，降低寻呼负荷，节省网络资源。语音类业务增值：通过差异化的处理，保障了语音业务质量。
移动用户|提升用户体验：语音呼叫快速接通，享受高效的语音通话服务。
实现原理 :系统架构 :策略寻呼整体架构包含如下几个部分： 
触发寻呼：各种触发寻呼的业务，包括：普通数据、VoNR语音、短消息等。 
选择策略寻呼：由AMF根据不同业务选择合适的寻呼策略进行寻呼。 
执行寻呼：gNodeB根据AMF的寻呼请求在空口向终端发起寻呼。 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
gNodeB|gNodeB根据AMF的要求，在指定的区域内寻呼UE。
AMF|根据业务类型、用户类型、不同的网络场景等条件组合，配置合适的寻呼策略。用户触发寻呼时，可选择合适的寻呼策略对用户进行寻呼，在保证一定寻呼成功率前提下，在寻呼负荷及寻呼时延等要求间取得平衡。
SMF|SMF提供PPI、ARP等信息给AMF，用于AMF选择合适的寻呼策略。
协议栈 :接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
本NF/网元实现 :寻呼策略是对寻呼过程进行细化控制的过程，通过调整寻呼策略参数（包括寻呼范围、寻呼次数及寻呼时间间隔），对寻呼的三个关键指标（寻呼负荷、寻呼成功率及寻呼时延）产生影响。需要根据不同场景下对寻呼指标（寻呼负荷、寻呼成功率、寻呼时延）的不同要求，选择合适的寻呼策略。 
寻呼范围
寻呼策略包括：寻呼次数、每次寻呼的寻呼类型（寻呼范围及寻呼标识）、每一次的寻呼超时时长。其中，寻呼范围是关键参数，可设置的寻呼范围参见[表4]。
编号|寻呼范围|详细描述
---|---|---
1|最近访问的gNodeB|AMF向用户最近一次访问的gNodeB发送寻呼，寻呼标识基于5G-GUTI。
2|最近访问的gNodeB列表|AMF向用户最近访问的gNodeB List范围内发送寻呼，寻呼标识基于5G-GUTI。
3|最近访问的TA|AMF向用户最近一次访问的TA范围内发送寻呼，寻呼标识基于5G-GUTI。
4|最近访问的TA列表|AMF向用户最近几次访问的TA列表范围内发送寻呼，寻呼标识基于5G-GUTI。
5|5G-GUTI标识TAI List寻呼|AMF向用户所在的TA List范围内发送寻呼，寻呼标识基于5G-GUTI。
6|5G-GUTI标识全AMF寻呼|向整个AMF发送寻呼，寻呼标识基于5G-GUTI。
寻呼策略因子
目前AMF支持如下几种类型的业务过滤条件（即寻呼策略因子）设置寻呼策略。包含三种维度：用户信息、位置信息、业务类型，三者组合形成完整的匹配规则，过滤出唯一的寻呼策略，如[图2]所示。
图2  寻呼策略

业务流程 :策略寻呼主要业务流程如下： 
各种上层应用通过SMF、SMSF等触发寻呼。 
AMF收到寻呼触发消息，根据触发场景选择合适的寻呼策略。 
AMF根据寻呼策略中的寻呼范围，向指定范围内的gNodeB(s)发起寻呼。 
如果寻呼无响应，则根据寻呼策略中下一次寻呼范围，向指定范围内的gNodeB(s)发起寻呼。 
系统影响 :开启策略寻呼后，可有效降低寻呼负荷，节约AMF和gNodeB资源消耗。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System"|5.3.3 Connection Management
3GPP TS 23.502: "Procedures for the 5G System"|4.2.3 Service Request procedures
3GPP TS 38.413: "NG Application Protocol (NGAP)"|8.5 Paging Procedures
特性能力 :名称|指标
---|---
最近访问的gNodeB列表支持的最大gNodeB数|7（个）
最近访问的TA列表支持的最大TA数|3（个）
一次寻呼过程支持的最大重发次数|20（次）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“7211 AMF支持智能策略寻呼功能”，此项目显示为“支持”，表示AMF支持智能寻呼功能。 
对其他网元的要求 :UE|NR|SMF
---|---|---
-|√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :主要包括寻呼范围（TA List）、寻呼策略的规划。 
O&M相关 :命令 :新增配置项参见[表5]。
配置项|命令
---|---
MT基础寻呼|SET MTBASICCFG
SHOW MTBASICCFG|MT基础寻呼
全局寻呼策略配置|SET GLOBALPOLICY
SHOW GLOBALPOLICY|全局寻呼策略配置
寻呼策略配置|ADD PAGINGPOLICYCFG
SET PAGINGPOLICYCFG|寻呼策略配置
DELETE PAGINGPOLICYCFG|寻呼策略配置
SHOW PAGINGPOLICYCFG|寻呼策略配置
寻呼因子配置|ADD PAGEFACTORCFG
SET PAGEFACTORCFG|寻呼因子配置
DELETE PAGEFACTORCFG|寻呼因子配置
SHOW PAGEFACTORCFG|寻呼因子配置
寻呼优先级配置|SET PAGINGPRIORITY
SHOW PAGINGPRIORITY|寻呼优先级配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :#### 配置分业务寻呼特性 
配置说明 :分业务寻呼可以通过寻呼策略因子来为不同的业务定制不同的寻呼策略。 
配置前提 :配置VoNR语音寻呼策略之前，需要完成用户ECP接入并注册到IMS域，IMS完成VoLTE呼叫相关的配置。
配置过程 :[ADD PAGINGPOLICYCFG]
配置寻呼策略Profile，可以配置寻呼方式、时间间隔以及寻呼优先级。 
[ADD PAGEFACTORCFG]
配置寻呼策略因子，可以根据不同的组合信息关联不同的寻呼策略Profile。 
配置实例 :场景说明
假设VoNR语音业务根据5QI=5获取寻呼策略，寻呼策略采用最近访问TAList寻呼方式，寻呼次数3次，寻呼时间间隔为5s，寻呼优先级为0。 
数据规划
根据假设的场景，VoNR语音业务寻呼策略数据规划参见[表1]。
寻呼策略ID|寻呼方式|寻呼时间间隔|寻呼优先级
---|---|---|---
10|最近访问TAList寻呼|5s|0
11|最近访问TAList寻呼|5s|0
12|最近访问TAList寻呼|5s|0
根据假设的场景，策略寻呼因子数据规划参见[表2]。
5QI|寻呼策略ID
---|---
5|10~12
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置寻呼策略|创建寻呼策略ID为10~12的寻呼策略Profile。ADD PAGINGPOLICYCFG:PAGINGPOLICYID=10,PAGINGSTYLE="LASTTALIST",PAGINGINTERVAL=50,PAGINGTIMES=1,BATCHPAGINGNUM=64,PAGINGPRIORITY=0;ADD PAGINGPOLICYCFG:PAGINGPOLICYID=11,PAGINGSTYLE="LASTTALIST",PAGINGINTERVAL=50,PAGINGTIMES=1,BATCHPAGINGNUM=64,PAGINGPRIORITY=0;ADD PAGINGPOLICYCFG:PAGINGPOLICYID=12,PAGINGSTYLE="LASTTALIST",PAGINGINTERVAL=50,PAGINGTIMES=1,BATCHPAGINGNUM=64,PAGINGPRIORITY=0;
2|配置5QI=5的寻呼策略因子|配置5QI=1的寻呼策略因子，引用寻呼策略10~12。ADD PAGEFACTORCFG:PAGINGFACTORID=1,PAGINGPOLICYID=10,FIVEQIFLG="WITHFLAG",FIVEQI=5,PPIFLG="WITHOUTFLAG",DNNFLG="WITHOUTFLAG";ADD PAGEFACTORCFG:PAGINGFACTORID=2,PAGINGPOLICYID=11,FIVEQIFLG="WITHFLAG",FIVEQI=5,PPIFLG="WITHOUTFLAG",DNNFLG="WITHOUTFLAG";ADD PAGEFACTORCFG:PAGINGFACTORID=3,PAGINGPOLICYID=12,FIVEQIFLG="WITHFLAG",FIVEQI=5,PPIFLG="WITHOUTFLAG",DNNFLG="WITHOUTFLAG";
#### 配置智能寻呼特性 
配置说明 :智能寻呼策略配置目的是通过扩大寻呼范围，提高数据业务的寻呼成功率。 
配置前提 :配置智能寻呼策略之前，需要完成用户接入网络，数据业务可用。 
配置过程 :[SET MTBASICCFG]
寻呼基础配置，用于配置是否支持寻呼区分，信令跟踪类型及批量寻呼消息发送间隔。 
[ADD PAGINGPOLICYCFG]
配置寻呼策略Profile，可以配置寻呼方式、寻呼时长，寻呼次数，批量寻呼消息发送个数以及寻呼优先级。 
[ADD PAGEFACTORCFG]
配置寻呼策略因子，可以根据不同的组合信息关联不同的寻呼策略Profile。 
[SET GLOBALPOLICY]
配置全局寻呼策略，如果AMF/MME不能通过策略寻呼因子获取到寻呼策略，就使用全局寻呼策略。 
[SET PAGINGPRIORITY]
配置寻呼优先级，该配置通过网络侧下发消息中的ARP可以查询寻呼优先级。 
配置实例 :场景说明
假设智能寻呼根据用户DNN获取寻呼策略，寻呼策略采用最近TA、TAList寻呼方式，寻呼次数2次，批量寻呼消息发送个数为64，寻呼时间间隔分别为5s，寻呼优先级分别为5、6。 
数据规划
根据假设的场景，智能寻呼策略数据规划参见[表3]。
寻呼策略ID|寻呼方式|寻呼时长|寻呼重发次数|批量寻呼消息发送个数|寻呼优先级
---|---|---|---|---|---
10|最近访问TA寻呼|5s|2|64|5
11|最近访问TA List寻呼|5s|2|64|6
根据假设的场景，策略寻呼因子数据规划参见[表4]。
配置步骤
DNN|寻呼策略ID
---|---
zte.com.cn|10~11
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置寻呼基础配置|打开支持灵活寻呼策略配置开关，信令跟踪全部跟踪，批量发送的间隔为50 ms。SET MTBASICCFG:SUPPORTPAGINGDIFF="SUPTPAGINGDIFF",PAGINGTRACESTYLE="TRACE_ALL",BATCHPAGINGINTERVAL=50
2|配置寻呼策略|创建寻呼策略ID为10~11的寻呼策略Profile。ADD PAGINGPOLICYCFG:PAGINGPOLICYID=10,PAGINGSTYLE="LASTTA",PAGINGINTERVAL=50,PAGINGTIMES=2,BATCHPAGINGNUM=64,PAGINGPRIORITY=5ADD PAGINGPOLICYCFG:PAGINGPOLICYID=11,PAGINGSTYLE="LASTTALIST",PAGINGINTERVAL=50,PAGINGTIMES=2,BATCHPAGINGNUM=64,PAGINGPRIORITY=6
4|配置全局寻呼策略|创建全局寻呼策略Profile。SET GLOBALPOLICY:PAGINGSRVTYPE=DATA,PAGINGTYPE=SMART_PAGING,GLOBALPOLICYGRPID=10SET GLOBALPOLICY:PAGINGSRVTYPE=DATA,PAGINGTYPE=SMART_PAGING,GLOBALPOLICYGRPID=11
6|配置寻呼策略因子|配置DNN为zte.com.cn的寻呼策略因子，寻呼策略为10~11。ADD PAGEFACTORCFG:PAGINGFACTORID=1,PAGINGPOLICYID=10,FIVEQIFLG="WITHOUTFLAG",PPIFLG="WITHOUTFLAG",DNNFLG="WITHFLAG",DNN="zte.com.cn"ADD PAGEFACTORCFG:PAGINGFACTORID=2,PAGINGPOLICYID=11,FIVEQIFLG="WITHOUTFLAG",PPIFLG="WITHOUTFLAG",DNNFLG="WITHFLAG",DNN="zte.com.cn"
8|配置寻呼优先级|配置ARP值为1对应的寻呼优先级为5。SET PAGINGPRIORITY:ARP=1,PAGINGPRIORITY=5
#### 配置精准寻呼特性 
配置说明 :精准寻呼策略配置目的是通过缩小寻呼范围，减少寻呼延时。 
配置前提 :配置精准寻呼策略之前，需要完成用户接入网络，数据业务可用。 
配置过程 :[ADD PAGINGPOLICYCFG]
配置寻呼策略Profile，可以配置寻呼方式、时间间隔以及寻呼优先级。 
[ADD PAGEFACTORCFG]
配置寻呼策略因子，可以根据不同的组合信息关联不同的寻呼策略Profile。 
[SET GLOBALPOLICY]
配置全局寻呼策略，如果AMF不能通过策略寻呼因子获取到寻呼策略，就使用全局寻呼策略。 
配置实例 :场景说明
假设精准寻呼根据用户接入的DNN获取寻呼策略，寻呼策略采用最近gNodeB、最近gNodeB
List、最近TA List寻呼方式，寻呼次数3次，寻呼时间间隔分别为2s、3s、4s，不携带寻呼优先级 
数据规划
根据假设的场景，智能寻呼策略数据规划参见[表5]。
寻呼策略ID|寻呼方式|寻呼时间间隔|寻呼优先级
---|---|---|---
10|最近访问gNodeB 寻呼|2s|0
11|最近访问gNodeB List寻呼|3s|0
12|最近访问TA List寻呼|4s|0
根据假设的场景，策略寻呼因子数据规划参见[表6]。
DNN|寻呼策略ID
---|---
zte.com.cn|10~12
配置步骤
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|配置寻呼策略|创建寻呼策略ID为10~12的寻呼策略Profile。ADD PAGINGPOLICYCFG:PAGINGPOLICYID=10,PAGINGSTYLE="LASTNR",PAGINGINTERVAL=50,PAGINGTIMES=1,BATCHPAGINGNUM=64,PAGINGPRIORITY=0;ADD PAGINGPOLICYCFG:PAGINGPOLICYID=11,PAGINGSTYLE="LASTNRLIST",PAGINGINTERVAL=50,PAGINGTIMES=3,BATCHPAGINGNUM=64,PAGINGPRIORITY=0;ADD PAGINGPOLICYCFG:PAGINGPOLICYID=12,PAGINGSTYLE="LASTTALIST",PAGINGINTERVAL=50,PAGINGTIMES=1,BATCHPAGINGNUM=64,PAGINGPRIORITY=0
3|配置全局寻呼策略|创建全局寻呼策略Profile。SET GLOBALPOLICY:PAGINGSRVTYPE=DATA,PAGINGTYPE=ACCURATE_PAGING,GLOBALPOLICYGRPID=10SET GLOBALPOLICY:PAGINGSRVTYPE=DATA,PAGINGTYPE=ACCURATE_PAGING,GLOBALPOLICYGRPID=11SET GLOBALPOLICY:PAGINGSRVTYPE=DATA,PAGINGTYPE=ACCURATE_PAGING,GLOBALPOLICYGRPID=12
4|配置寻呼策略因子|配置DNN为zte.com.cn的寻呼策略因子，寻呼策略为10~12。ADD PAGEFACTORCFG:PAGINGFACTORID=1,PAGINGPOLICYID=10,FIVEQIFLG="WITHOUTFLAG",PPIFLG="WITHOUTFLAG",DNNFLG="WITHFLAG",DNN="zte.com.cn"ADD PAGEFACTORCFG:PAGINGFACTORID=2,PAGINGPOLICYID=11,FIVEQIFLG="WITHOUTFLAG",PPIFLG="WITHOUTFLAG",DNNFLG="WITHFLAG",DNN="zte.com.cn"ADD PAGEFACTORCFG:PAGINGFACTORID=3,PAGINGPOLICYID=12,FIVEQIFLG="WITHOUTFLAG",PPIFLG="WITHOUTFLAG",DNNFLG="WITHFLAG",DNN="zte.com.cn"
测试用例 :测试项目|AMF支持语音寻呼和分组寻呼分别配置不同的寻呼策略
预置条件|AMF和各邻接局工作正常。配置分业务寻呼策略：策略ID为100，在TA LIST范围内寻呼2次，第一次寻呼时长3s，第二次寻呼时长为5s。配置分业务寻呼策略：策略ID为101，在TA LIST范围寻呼2次，第一次寻呼时长5s，第二次寻呼时长为5s。根据5QI分别配置5QI=5和5QI=9寻呼策略因子。5QI=5的寻呼策略因子关联策略ID为100的寻呼策略，5QI=9寻呼策略因子关联策略ID为101寻呼策略。
测试过程|开启信令跟踪。用户注册接入5G网络。用户建立5QI=5和5QI=9的承载。用户进入IDLE态。用户收到下行数据业务专有承载建立请求(5QI=9)，AMF寻呼用户，用户无响应。用户收到下行VoNR语音业务专有承载建立请求(5QI=5)，AMF寻呼用户，用户无响应。
通过准则|验证AMF支持VoNR语音寻呼和分组寻呼分别配置不同的寻呼策略是否正确。
测试结果|数据寻呼无响应（手机拔电池或者放入屏蔽箱），AMF首次寻呼5s无响应后，AMF再次进行寻呼，5s无响应后，寻呼终止。语音寻呼无响应（手机拔电池或者放入屏蔽箱）， AMF首次寻呼3s无响应后，AMF再次进行寻呼，5s无响应后，寻呼终止。
## ZUF-79-04-004 UE可达性管理 
特性描述 :特性描述 :术语 :术语|含义
---|---
RRC Inactive|RRC Inactive是5G系统引入的一种特殊的用户连接状态，当用户处于该状态时，仅空口连接被释放，核心网仍旧处于连接状态。
无线通知区域|无线通知区域是由(R)AN分配给UE的一组小区。处于RRC Inactive状态下，UE在该区域中移动时，无需通知(R)AN。当UE移出该区域时，需要通知(R)AN。
描述 :定义 :连接态下的UE可达性，是指UE处于RRC Inactive状态时UE可达性的管理，比如周期性位置更新、寻呼等。
在5G系统中，为了RRC连接释放后，能够快速恢复用户业务，3GPP引入了RRC Inactive状态。在该状态下，RRC连接被释放，但N2连接仍旧存在。当数据业务需要恢复时，仅需恢复RRC连接即可，从而降低业务恢复时延。
背景知识 :在移动通讯网络中，从网络侧来看，空口资源属于一种高价值资源，当长时间没有数据或者没有信令传输时，系统需要能够主动释放空口资源，UE进入待机状态。从终端侧看，设备的待机时长是衡量一个设备优劣的一个参考指标，当无信令或数据传输时，终端需要支持主动释放空口连接，进入待机状态。 
高可靠低时延通讯业务是5G系统的一项关键业务，包括VR、远程医疗、自动驾驶等应用场景。这些应用场景对于时延有着苛刻的要求，包括纯数据传输的时延，以及UE离开待机状态进入活跃状态的时延。 
如边缘计算，通过将UPF下沉到无线，从而减少数据在传输网中的传输时延。 
通过引入新的连接状态CM-CONNECTED RRC Inactive，在这种状态终下空口连接被释放，从而满足提高空口资源利用效率以及终端节电的目的。同时，从CN侧来看，用户面、信令连接仍旧保持，UE仍旧处于连接状态，数据可以直接下发。 
应用场景 :本特性适用于对于时延要求非常高的业务，应用场景如下： 
远程医疗 
虚拟现实 
自动驾驶 
客户收益 :受益方|受益描述
---|---
运营商|降低业务时延，提升网络服务竞争力，同时为开展5G特有的URLLC业务提供了基础。
终端用户|终端设备节电。
实现原理 :系统架构 :本特性涉及的系统架构如[图1]所示。
图1  系统架构

涉及的NF/网元参见下表。
NF/网元|说明
---|---
NF|AMF|负责下发RRC Inactive Assistance Information给(R)AN，处理UDM下发的UE可达性请求，并向UDM上报UE活动通知。
UDM|NF|负责下发UE可达性请求给AMF，以及处理AMF上报的UE活动通知。
网元|(R)AN|负责RRC Inactive状态下UE移动性管理、协助恢复RRC连接。
UE|网元|RRC Inactive状态下，周期性向(R)AN侧更新；当存在上行数据或者信令需要传递时，触发RRC连接建立过程。
业务流程 :概述 :连接态下的UE可达性，涉及核心网的流程包括RRC Inactive Assistance
Information消息的下发、UE可达性通知请求、UE活动通知、RRC连接恢复。 
####### RRC Inactive Assistance Information的下发 
RRC
Inactive Assistance Information由AMF下发给(R)AN，涉及流程如下： 
业务请求 
基于Xn接口的切换 
基于N2接口的切换 
RRC Inactive Assistance Information下发给(R)AN的流程如[图2]所示。
图2  RRC Inactive Assistance Information下发给(R)AN的流程图

流程说明如下： 
业务请求流程中，AMF通过Initial Context Setup Request，将RRC Inactive Assistance
Information带给(R)AN。 
基于Xn接口的切换流程中，AMF通过Path Switch Acknowledge，将RRC Inactive Assistance
Information带给(R)AN。 
基于N2接口的切换流程中，AMF通过Handover Request，将RRC Inactive Assistance
Information带给(R)AN。 
####### UE可达性通知请求 
UE可达性通知请求流程如[图3]所示。
图3  UE可达性通知请求流程图

流程说明如下： 
在注册或者签约更新流程中，通过Nudm_UECM_Registration或者Nudm_SubscriberData_Update两个服务操作，UDM将授权进行UE可达性请求的网络功能实体ID，通知给AMF。 
若一个业务相关的实体需要请求UE可达性，则发送请求消息给UDM。 
UDM设置URRP_AMF标记，并下发Namf_EventExposure_subscribe请求给AMF。 
网络功能实体也可以直接向AMF请求UE可达性，通过下发Namf_EventExposure_subscribe请求给AMF。 
AMF收到UE可达性请求后，先校验请求UE可达性的网络功能实体是否被授权，再设置URRP_AMF标记。 
若UE处于连接态，则AMF发起N2 Notification过程，向(R)AN查询UE可达性状态。 
####### UE活动通知 
UE活动通知流程如[图4]所示。
图4  UE活动通知流程图

流程说明如下： 
若AMF发起N2 Notification流程，则(R)AN回复UE Notification。或者UE移动到其他(R)AN，触发其他(R)AN发送Path
Switch Request给AMF。AMF收到UE Notification或者Path Switch Request后，表示UE处于活动状态。 
根据不同情况，执行以下流程： 
AMF判断URRP_AMF标记有效，且UDM发起了UE可达性请求，则发送Namf_EventExposure_Notify给UDM，通知UDM
UE可达，UDM将该通知转发给真正请求UE可达性状态的NF。 
若UE可达性请求为其他NF发起，则AMF直接发送Namf_EventExposure_Notify给NF，通知NF UE可达。 
####### RRC连接恢复 
RRC连接恢复流程如[图5]所示。
图5  RRC连接恢复流程图

流程说明如下： 
处于RRC Inactive状态的UE，检测到存在上行数据或者信令需要发送，则发送RRC连接建立请求给(R)AN。 
若当前接入的(R)AN与源(R)AN之间存在Xn接口，则当前接入的(R)AN通过Xn接口，向源(R)AN请求UE上下文。 
当前接入的(R)AN获取UE上下文成功后，发起Path Switch流程。 
当前接入的(R)AN下发RRC建立成功响应给UE，此时UE进入RRC连接状态。 
NF实现 :AMF实现 :UDM :AMF在连接态下UE可达性管理中，承担如下功能： 
下发RRC Inactive Assistance Information消息给(R)AN。 
处理UE可达性请求。 
处理UE活动通知。 
协助(R)AN恢复RRC连接。 
UDM在连接态下UE可达性管理中，承担如下功能： 
下发UE可达性请求给AMF。 
处理AMF发送的UE活动通知。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :相关特性|交互关系
---|---
ZUF-79-05-001 基于Xn切换|RRC连接恢复时，RAN侧触发Path Switch流程。
ZUF-79-05-002 基于N2切换|RRC连接恢复时，RAN侧触发Path Switch流程。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP TS 23.502|3GPP|Procedures for the 5G System
3GPP TS 29.500|3GPP|Technical Realization of Service Based Architecture
3GPP TS 29.503|3GPP|Unified Data Management Services; Stage 3
3GPP TS 29.518|3GPP|Access and Mobility Management Services
3GPP TS 38.413|3GPP|NGApplication Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :该特性无特殊的工程规划要求。 
O&M相关 :配置命令 :本特性不涉及配置命令的变化。 
定时器 :本特性不涉及定时器的变化。 
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置即可。 
测试用例 :测试项目|UE可达性管理
---|---
测试目的|验证UE可达性管理功能正常
预置条件|(R)AN，各NF运行正常。用户注册，PDU会话建立成功后释放AN连接，用户处于CM-IDLE状态。
测试过程|UE触发数据类型的业务请求。
通过准则|业务请求成功。Initial Context Setup Request消息中携带RRC Inactive Assistance Information给(R)AN。
测试结果|-
常见问题处理 :无 
## ZUF-79-04-005 MICO 
概述 :UE和AMF在初始注册过程中协商MICO模式，并且在后续的每个注册过程中重新协商MICO模式。当UE处于连接态时，AMF可以通过UE Configuration Update流程触发Registration Update流程去激活MICO模式。 
客户收益 :在MICO模式下，空闲态UE不支持寻呼，从而获得更好的节电能力。 
说明 :UE在初始注册和注册更新请求中根据本地策略和用户数据指示MICO优先。 
本地策略 
用户数据 
AMF确定是否允许MICO，并指示UE。当UE处于连接态时，AMF可以通过UE Configuration Update流程触发Registration Update流程去激活MICO模式。 
MICO模式下的空闲态UE不可达。收到网络的业务请求时，AMF返回UE不可达。 
## ZUF-79-04-006 连接态下的RRC-Inactive 
概述 :AMF根据网络配置可向NG-RAN提供辅助信息，以协助NG-RAN决定UE是否可以进入RRC Inactive状态。 
客户收益 :AMF协助NG-RAN决定UE是否可以进入RRC Inactive状态。 
说明 :物联网终端处于RRC Inactive状态时，为了帮助终端节电，NR-RAN负责终端的移动性管理，如寻呼、周期注册更新等。 
AMF根据网络配置可向NG-RAN提供辅助信息，以协助NG-RAN决定UE是否可以进入RRC Inactive状态。 
RRC Inactive Assistance Information包括: 
UE特定的DRX值 
提供给UE的注册区域 
周期注册更新定时器 
表明UE处于MICO模式的指示，如果AMF为UE开启了MICO模式 
UE永久标识的信息，允许RAN计算UE的RAN寻呼次数 
上述RRC
Inactive Assistance Information由AMF在（新）服务NG-RAN节点激活N2时提供（即，在注册、业务请求、切换过程中），协助NG RAN决定UE是否可以进入RRC Inactive状态。 
## ZUF-79-04-007 N2配置及TNLA绑定管理 
概述 :AMF支持与NG-RAN建立一个或多个TNL关联，支持NG-RAN增加或删除TNL关联关系。AMF支持建立、更新和释放UE的AMF
NGAP ID和TNLA的绑定关系。 
客户收益 :用户的信令由AMF和NG-RAN之间的绑定TNLA转发。 
说明 :AMF与NG-RAN之间的连接需要容灾保障。AMF支持与NG-RAN建立多个TNL关联。如果一条链路断开，其他链路就接管用户的信令。实现多条链路之间的负荷分担。 
AMF支持与NG-RAN建立一个或多个TNL关联，支持NG-RAN增加或删除TNL关联关系。AMF为NG-RAN提供与每个TNL相关的权重因子，以及与UE相关/无关的信令处理能力。 
AMF支持建立、更新和释放UE的AMF NGAP ID和TNLA的绑定关系。 
.AMF支持将连接态UE的AMF NGAP ID与TNLA绑定，该UE的信令始终由TNLA下发。涉及以下流程： 
注册 
业务请求 
切换 
AMF支持更新AMF本身或NG-RAN触发的NGAP UE-TNLA绑定。 
AMF支持主动释放NGAP UE-TNLA绑定并保持UE N3连接。 
## ZUF-79-04-008 IMEISV下发gNodeB 
特性描述 :特性描述 :描述 :定义 :IMEISV下发gNodeB指当AMF得到终端的IMEISV时，AMF对IMEISV的SNR的后4位数进行掩码，把掩码后的Masked IMEISV通过N2接口（AMF与gNodeB之间的接口）消息带给gNodeB。
背景知识 :不同的厂家和操作系统对终端的无线处理方案不同，从而终端接入到无线网络时有不同的方式。如果gNodeB针对所有的终端采取同一个策略，可能会造成部分终端接入失败或不稳定。 
应用场景 :gNodeB针对不同类型的终端制定不同的策略，从而提高终端的接入成功率和无线网络的稳定性。 
客户收益 :受益方|受益描述
---|---
运营商|提高网络接通率。提高无线系统可靠性。提高用户满意度。
移动用户|提升终端用户体验，享受更稳定和更可靠的网络服务。
实现原理 :系统架构 :本特性利用网元现有消息接口，在接口消息中新增参数字段，对系统架构无改变。 
涉及的网元 :网元名称|网元作用
---|---
AMF|AMF接收并保存UE带上的IMEISV，通过N2口消息把Masked IMEISV带给gNodeB。
gNodeB|gNodeB接收并使用AMF下发的Masked IMEISV参数。
协议栈 :本特性涉及到的协议栈参见下表。 
接口|相关链接
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N14|ZUF-79-19-006 N14
本网元实现 :AMF根据运营商策略，控制是否对用户IMEISV的SNR后4位数进行掩码，并将掩码后的Masked IMEISV下发给gNodeB。相关业务流程如下： 
注册/注册更新流程 
UE发起业务请求流程 
网络触发业务请求流程 
切换流程（N2切换\AMF内） 
切换流程（N2切换\AMF间） 
PDU会话激活流程 
4/5G互操作，UE在4G网络附着后，重新接入或重选到5G网络。 
4/5G互操作且有N26接口时，UE在4G网络附着后，从4G网络切换到5G网络。 
业务流程 :下发Masked IMEISV的流程如[图1]和[图2]所示。
图1  下发IMEISV的流程-Initial Context Setup Request

图2  下发Masked IMEISV的流程-Handover Request

流程说明： 
AMF下发Initial Context Setup Request或Handover Request消息给gNodeB，消息中携带Masked IMEISv。 
gNodeB根据AMF下发的Masked IMEISV执行不同的控制策略。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 38.413: NG-RAN; NG Application Protocol (NGAP)|9.2.2.1 INITIAL CONTEXT SETUP REQUEST9.2.3.4 HANDOVER REQUEST
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.30|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。 
对其他网元的要求 :UE|gNodeB
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增配置项参见[表1]。
配置项|命令
---|---
Masked IMEISV参数配置|SET AMFMASKEDIMEISVCFG
SHOW AMFMASKEDIMEISVCFG|Masked IMEISV参数配置
性能统计 :该特性不涉及计数器的变化。
告警和通知 :该特性不涉及告警/通知消息的变化。
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过如下两个开关，可以控制AMF给gNodeB下发的Handover Request消息和Initial Context Setup Request消息中允许携带Masked IMEISV。 
Handover Request中携带Masked IMEISV 
Initial Context Setup Request中携带Masked IMEISV 
如果支持Masked IMEISV，gNodeB可通过IMEISV对终端进行管理（例如，对部分终端指定特殊的策略）。 
配置前提 :无 
配置过程 :执行如下命令，开启“AMF是否获取IMEI(SV)”开关。配置成功后，AMF可通过注册等流程获取到IMEISV。 
[SET AMFMOBCFG]:AMFGETIMEI="GETIMEISV"
执行[SET AMFMASKEDIMEISVCFG]命令，开启“HANDOVER REQUEST中携带Masked IMEISV”和“INITIAL CONTEXT SETUP REQUEST中携带Masked IMEISV”开关，设置AMF给NG-RAN下发的消息中允许携带Masked IMEISV。
配置实例 :场景说明 :在Handover Request消息中携带Masked IMEISV。 
在Initial Context Setup Request消息中携带Masked IMEISV。 
数据规划 :配置名称|参数项|取值
---|---|---
AMF移动性配置|AMF是否获取IMEI(SV)|获取IMEISV获取IMEI不获取IMEI或IMEISV|获取IMEISV获取IMEI不获取IMEI或IMEISV|获取IMEISV获取IMEI不获取IMEI或IMEISV
Masked IMEISV参数配置|HANDOVER REQUEST中携带Masked IMEISV|支持masked Imeisv不支持masked Imeisv|支持masked Imeisv不支持masked Imeisv|支持masked Imeisv不支持masked Imeisv
INITIAL CONTEXT SETUP REQUEST中携带Masked IMEISV|Masked IMEISV参数配置|支持masked Imeisv不支持masked Imeisv|支持masked Imeisv不支持masked Imeisv|支持masked Imeisv不支持masked Imeisv
配置步骤 :步骤|说明|操作
---|---|---
1|配置AMF允许获取IMEISV|SET AMFMOBCFG:AMFGETIMEI="GETIMEISV"
2|配置在Handover Request消息中允许携带Masked IMEISV|SET AMFMASKEDIMEISVCFG:HOCARRYIMEISV="SupMskImeiSv"
3|配置在Initial Context Setup Request消息中允许携带Masked IMEISV|SET AMFMASKEDIMEISVCFG:INITCTXSCARRYIMEISV="SupMskImeiSv"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|注册流程携带Masked IMEISV
---|---
测试目的|在Initial Context Setup Request消息携带Masked IMEISV。
预置条件|UE、gNodeB、AMF网元正常。“AMF是否获取IMEI(SV)”开关配置为“获取IMEISV”。"INITIAL CONTEXT SETUP REQUEST中携带Masked IMEISV"开关配置为“支持masked Imeisv”。
测试过程|用户”460011234567890“ 发起初始注册流程。AMF通过Identity Request消息获取到UE的IMEISV。
通过准则|AMF给gNodeB下发Initial Context Setup Request消息，且消息中携带Masked IMEISV。
测试结果|–
测试项目|N2局内切换流程携带Masked IMEISV
---|---
测试目的|在Handover Request消息中携带Masked IMEISV。
预置条件|UE、gNodeB、AMF网元正常。“AMF是否获取IMEI(SV)”开关配置为“获取IMEISV”。"Handover Request消息携带Masked IMEISV"开关配置为“支持masked Imeisv”。
测试过程|用户”460011234567890“ 发起初始注册流程。AMF通过Identity Request消息获取到UE的IMEISV。UE发起局内切换。
通过准则|AMF给gNodeB发送Handover Request消息，且消息中携带Masked IMEISV。
测试结果|–
常见问题处理 :无 
## ZUF-79-04-009 基于机器学习的智能寻呼 
特性描述 :特性描述 :描述 :定义 :基于机器学习的智能寻呼是指AMF基于SON流程、Xn/N2口切换等流程，自动学习gNodeB间邻接关系，当寻呼用户时，可以在用户最近一次接入的gNodeB及其邻接gNodeB寻呼，在保证寻呼成功率的提前下，减少寻呼时延和寻呼消息量。
邻接gNodeB，指物理上邻接的gNodeB。AMF可以仅对中低速用户使用邻接gNodeB寻呼。 
背景知识 :5G终端与网络侧进行数据交互时，为了节电会进入IDLE状态。终端处于IDLE状态下，如果此时网络侧有数据需要向终端发送，可通过触发寻呼流程，使终端进入CM-CONNECTED状态，恢复数据传输。 
5G寻呼流程是指：AMF向终端所在的物理区域内的所有gNodeB发送寻呼请求，gNodeB在空口进行广播，当终端收到寻呼请求后，重新建立与网络侧的连接。 
随着5G各种业务爆发式增长，5G寻呼面临着如下挑战： 
寻呼在话务模型中所占比重越来越大，寻呼数量呈指数级增长，极端情况下可能引起信令风暴。 
VoNR语音业务对时延敏感，此类业务需要尽量缩短寻呼时延，提升用户体验。 
AMF需要支持策略寻呼，以提供解决方案来应对这些挑战。 
寻呼指标
衡量寻呼的3个重要指标参见下表。 
指标|说明
---|---
寻呼负荷|由于寻呼消息具有广播特征，因此需要合理规划寻呼范围，保持寻呼消息在合适范围内进行发送，可有效降低寻呼负荷。在寻呼区域合理规划的基础上，通过合理预测用户位置，缩小寻呼范围，可进一步降低寻呼负荷。
寻呼成功率|保证一定寻呼成功率，是业务稳定运行的基础。决定寻呼成功率的要素有：寻呼范围和寻呼次数。缩小寻呼范围可能导致寻呼失败，增加寻呼次数并扩大寻呼范围可提高成功率。
寻呼时延|对于时延敏感的业务（比如语音呼叫），寻呼时需要优先考虑时延影响。使用TA List寻呼可提高一次寻呼成功率，从而降低寻呼时延。
寻呼范围
UE处于CM-IDLE态下，AMF基于分配给UE的TA List来管理用户位置，根据3GPP协议要求，寻呼范围为TA List。如果AMF能够根据UE的移动性预测UE当前的准确位置，则可以缩小寻呼范围，降低寻呼负荷。 
寻呼范围从小到大依次参见下表。 
序号|寻呼范围|描述
---|---|---
1|最近访问的gNodeB|针对UE上次驻留的gNodeB发起寻呼。
2|最近访问的gNodeB列表或最近访问的gNodeB的邻接gNodeB列表|针对UE最近驻留的gNodeB列表或UE上次驻留的gNodeB及其相邻gNodeB列表的寻呼。
3|最近访问的TA|针对UE上次驻留的TA中所有的gNodeB发起寻呼。
4|最近访问的TA列表|针对UE上次驻留的TA及其相邻的TA中所有的gNodeB发起寻呼。
5|分配给UE的完整TA List|3GPP标准寻呼，对TA List下的所有gNodeB发起寻呼，此寻呼范围是AMF的缺省寻呼范围。
根据UE移动性来预测UE准确位置的依据是：每几分钟触发一次寻呼，用户在几分钟时间内活动范围有限（大部分情况下用户处于低速移动或静止不动状态），结合用户最近的历史活动范围，以及gNodeB间邻接关系，可大致预测用户所在gNodeB。 
应用场景 :在保证寻呼成功率的基础上，根据不同场景的特点，选择不同的寻呼策略，具体参见下表。 
应用场景|寻呼需求|邻接gNodeB寻呼策略
---|---|---
通用类业务的寻呼，如数据业务、信令。|对时延及寻呼负荷无特殊要求。|对于中低速移动的用户：一次寻呼范围：最近访问的gNodeB。二次寻呼范围：最近访问的gNodeB及其邻接gNodeB列表。三次寻呼范围：TA List。
负荷敏感类业务的寻呼，如抄表业务。|寻呼负荷敏感、时延不敏感。|对于中低速移动的用户：一次寻呼范围：最近访问的gNodeB。二次寻呼范围：最近访问的gNodeB及其邻接gNodeB列表。三次寻呼范围：TA List。
时延敏感类业务的寻呼，如语音业务。|时延敏感。|对于中低速移动的用户：一次寻呼范围：最近访问的gNodeB及其邻接gNodeB列表。二次寻呼范围：TA List。
客户收益 :受益方|受益描述
---|---
运营商|在保证寻呼成功率及用户体验的基础上，降低寻呼负荷，节省网络资源，节约投资成本；降低寻呼时延，保障语音业务质量。
移动用户|享受高效的语音通话服务，提升用户体验。
实现原理 :系统架构 :基于机器学习的智能寻呼系统架构如[图1]所示。
图1  系统架构

涉及的网元 :NF名称|网元作用
---|---
gNodeB|触发SON流程、Xn口或N2口切换流程，携带两个相邻gNodeB的信息。
AMF|AMF根据SON流程、Xn/N2口切换流程，自动学习gNodeB间邻接关系；根据本地寻呼策略以及用户移动性（是否中低速移动用户），确定是否使用邻接gNodeB列表寻呼。
协议栈 :接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
本网元实现 :基于机器学习的智能寻呼包含如下几个部分： 
gNodeB邻接关系学习：根据SON流程、Xn/N2口切换流程，AMF自动学习gNodeB间邻接关系。 
选择寻呼策略：由AMF根据本地寻呼策略以及用户移动性，确定是否使用邻接gNodeB列表寻呼。对于中低速移动用户，可以使用邻接gNodeB列表寻呼；对于高速移动用户，建议不使用邻接gNodeB列表寻呼。 
执行寻呼：AMF向UE最近驻留的gNodeB及其邻接gNodeB发送寻呼消息，gNodeB根据AMF的寻呼请求在空口向终端发起寻呼。 
由于gNodeB邻接关系的学习是一个漫长的过程，为了避免长时间等待系统学习，AMF支持手动配置导入gNodeB邻接关系（目前仅用于测试）。 
gNodeB邻接关系学习
通过SON流程学习邻接关系：自组织网络SON流程实现了通过Uplink RAN Configuration Transfer消息传递gNodeB的Xn接口地址信息给AMF，自动获得配置相关数据。当两个gNodeB通过Xn接口进行SON流程时，则认为这两个gNodeB是相邻gNodeB。AMF获取源侧gNodeB ID方法：AMF根据SON Configuration Transfer信元中的Source gNodeB ID得到源侧gNodeB ID。AMF获取目标侧gNodeB ID方法：AMF根据SON Configuration Transfer信元中的Target gNodeB ID得到目标gNodeB ID。 
通过Xn口切换流程学习邻接关系：相邻gNodeB间有Xn接口，由目标侧gNodeB发起到AMF的流程，AMF接收Path Switch Request消息获取源侧gNodeB和目标侧gNodeB之间的邻接关系。AMF获取源侧gNodeB ID方法：Path Switch Request消息中携带Source AMF UE NGAP ID信元，表示AMF在源gNodeB为用户分配的连接信息，可以根据此信元找到MM上下文，根据上下文中存储的源gNodeB的IP地址找到源侧gNodeB ID。AMF获取目标侧gNodeB ID方法：Path Switch Request消息由目标侧gNodeB发起，AMF收到此消息后，解析该gNodeB的IP地址后根据IP地址找到目标侧gNodeB ID。 
通过N2口切换流程学习邻接关系：相邻gNodeB间无Xn接口，或需改变AMF，由源侧gNodeB发起到AMF的流程，AMF通过Handover Required消息获取目标侧gNodeB与源侧gNodeB之间的邻接关系。AMF获取源侧gNodeB ID方法：Handover Required消息由源侧gNodeB发起，AMF收到此消息后，将发送此消息的gNodeB作为源侧gNodeB，并根据IP地址找到源侧gNodeB ID。AMF获取目标侧gNodeB ID方法：Handover Required消息中的Target ID就是目标侧gNodeB ID。 
AMF对中低速移动用户判断
AMF对中低速移动用户判断，基于用户在最近驻留的gNodeB上驻留的时间。如果驻留的时间超过一定时长，就判定为中低速移动用户。 
业务流程 :该特性不涉及业务流程。 
系统影响 :该特性开启后，需要保存gNodeB间邻接关系，最大单VM可能消耗40M左右内存。 
AMF通常需要约一周时间才能完整建立好gNodeB邻接关系表，此时长因网络环境不同会有差异。 
应用限制 :该特性不涉及应用限制。 
特性交互 :相关特性|交互关系
---|---
ZUF-79-04-003 智能寻呼|AMF基于机器学习的智能寻呼，是在智能寻呼基础上的增强，必须提前开启智能寻呼功能。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System"|5.3.3 Connection Management
3GPP TS 23.502: "Procedures for the 5G System"|4.2.3 Service Request procedures
3GPP TS 38.413: "NG Application Protocol (NGAP)"|8.5 Paging Procedures
特性能力 :名称|指标
---|---
单个中心gNodeB支持的最大邻接gNodeB数|64（个）
支持的邻接gNodeB最大数量|192万（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.22.10|首次发布。
License要求 :该特性需要开启License，对应的License项目为“AMF支持基于机器学习的智能寻呼”（license ID：7248），此项目显示为“支持”，标识AMF支持基于机器学习的智能寻呼。 
对其他网元的要求 :UE|gNodeB|SMF|AUSF|UDM
---|---|---|---|---
-|√|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :开启本特性，Communication和MT服务所在的单VM可能需要额外消耗最多40M内存，请确认现网Communication和MT服务所在单VM有足够的内存。 
O&M相关 :命令 :配置项|命令
---|---
邻接gNodeB寻呼策略配置|SET NEIGHBOR GNB PAGING POLICY
SHOW NEIGHBOR GNB PAGING POLICY|邻接gNodeB寻呼策略配置
寻呼策略模板配置|ADD PAGINGPOLICYCFG
SET PAGINGPOLICYCFG|寻呼策略模板配置
DELETE PAGINGPOLICYCFG|寻呼策略模板配置
SHOW PAGINGPOLICYCFG|寻呼策略模板配置
寻呼策略组配置|ADD PAGINGPOLICYGROUPCFG
SET PAGINGPOLICYGROUPCFG|寻呼策略组配置
DELETE PAGINGPOLICYGROUPCFG|寻呼策略组配置
SHOW PAGINGPOLICYGROUPCFG|寻呼策略组配置
全局寻呼策略配置|SET GLOBALPOLICY
SHOW GLOBALPOLICY|全局寻呼策略配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置可以实现基于机器学习的智能寻呼功能。 
配置前提 :AMF网元各项对接和业务配置完毕。 
开启License项目“AMF支持基于机器学习的智能寻呼”（license ID：7248）。 
配置过程 :###### 场景一：通用类业务的寻呼 
执行[SET NEIGHBOR GNB PAGING POLICY]命令，打开基于机器学习的智能寻呼开关。
执行[ADD PAGINGPOLICYCFG]命令，根据通用类业务寻呼策略规划，新增寻呼策略模板，包括最近活动的基站、邻接基站列表、TA List（已有默认配置记录）。
执行[ADD PAGINGPOLICYGROUPCFG]命令，新增寻呼策略组用于通用类业务寻呼使用，并关联步骤2配置的寻呼策略模板。
执行[SET GLOBALPOLICY]命令，配置通用类业务关联步骤3新增的寻呼策略组。
###### 场景二：负荷敏感类业务的寻呼 
执行[SET NEIGHBOR GNB PAGING POLICY]命令，打开基于机器学习的智能寻呼开关。
执行[ADD PAGINGPOLICYCFG]命令，根据负荷敏感类业务寻呼策略规划，新增寻呼策略模板，包括最近活动的基站、邻接基站列表、TA List（已有默认配置记录）。
执行[ADD PAGINGPOLICYGROUPCFG]命令，新增寻呼策略组用于负荷敏感类业务寻呼使用，并关联步骤2配置的寻呼策略模板。
执行[SET GLOBALPOLICY]命令，配置负荷敏感类业务关联步骤3新增的寻呼策略组。
###### 场景三：时延敏感类业务的寻呼 
执行[SET NEIGHBOR GNB PAGING POLICY]命令，打开基于机器学习的智能寻呼开关。
执行[ADD PAGINGPOLICYCFG]命令，根据时延敏感类业务寻呼策略规划，新增寻呼策略模板，包括邻接基站列表、TA List（已有默认配置记录）。
执行[ADD PAGINGPOLICYGROUPCFG]命令，新增寻呼策略组用于时延敏感类业务寻呼使用，并关联步骤2配置的寻呼策略模板。
执行[SET GLOBALPOLICY]命令，配置时延敏感类业务关联步骤3新增的寻呼策略组。
配置实例 :场景一 :场景说明
通用类业务的寻呼，如数据业务、信令。 
数据规划
配置项|参数|取值|数据来源|说明
---|---|---|---|---
SET NEIGHBOR GNB PAGING POLICY|支持邻接gNodeB寻呼功能|是|本端规划|-
ADD PAGINGPOLICYCFG|寻呼策略模板ID|1|本端规划|-
寻呼方式|ADD PAGINGPOLICYCFG|基于最近活动RAN寻呼|本端规划|-
寻呼时长(100ms)|ADD PAGINGPOLICYCFG|35|本端规划|-
寻呼次数|ADD PAGINGPOLICYCFG|1|本端规划|-
ADD PAGINGPOLICYCFG|寻呼策略模板ID|2|本端规划|-
寻呼方式|ADD PAGINGPOLICYCFG|基于RAN列表寻呼|本端规划|-
RAN列表类型|ADD PAGINGPOLICYCFG|邻接RAN列表|本端规划|-
寻呼时长(100ms)|ADD PAGINGPOLICYCFG|30|本端规划|-
寻呼次数|ADD PAGINGPOLICYCFG|1|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|1|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|2|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|205|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
SET GLOBALPOLICY|寻呼业务类型|信令业务|本端规划|-
寻呼类型|SET GLOBALPOLICY|自定义寻呼|本端规划|-
全局寻呼策略组ID|SET GLOBALPOLICY|1|已配置数据中获取|引用ADD PAGINGPOLICYGROUPCFG命令中配置的寻呼策略组ID，可通过SHOW PAGINGPOLICYGROUPCFG查询。
配置步骤
步骤|说明|操作
---|---|---
1|打开基于机器学习的智能寻呼开关|SET NEIGHBOR GNB PAGING POLICY:SUPNEIGNBPAGING="YES"
2|配置寻呼策略模板|ADD PAGINGPOLICYCFG:PAGINGPOLICYID=1,PAGINGSTYLE="LASTNR",PAGINGINTERVAL=35,PAGINGTIMES=1ADD PAGINGPOLICYCFG:PAGINGPOLICYID=2,PAGINGSTYLE="LASTNRLIST",RANLISTTYPE="NERGHBORRANLIST",PAGINGINTERVAL=30,PAGINGTIMES=1
3|配置寻呼策略组|ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=1,PAGINGPRIORITY="NULL"ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=2,PAGINGPRIORITY="NULL"ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=205,PAGINGPRIORITY="NULL"
4|配置信令关联的寻呼策略组|SET GLOBALPOLICY:PAGINGSRVTYPE="SIGNAL",PAGINGTYPE="CUSTOMIZED_PAGING",GLOBALPOLICYGRPID=1
场景二 :场景说明
负荷敏感类业务的寻呼，如抄表、定位业务。 
数据规划
配置项|参数|取值|数据来源|说明
---|---|---|---|---
SET NEIGHBOR GNB PAGING POLICY|支持邻接gNodeB寻呼功能|是|本端规划|-
ADD PAGINGPOLICYCFG|寻呼策略模板ID|1|本端规划|-
寻呼方式|ADD PAGINGPOLICYCFG|基于最近活动RAN寻呼|本端规划|-
寻呼时长(100ms)|ADD PAGINGPOLICYCFG|35|本端规划|-
寻呼次数|ADD PAGINGPOLICYCFG|1|本端规划|-
ADD PAGINGPOLICYCFG|寻呼策略模板ID|2|本端规划|-
寻呼方式|ADD PAGINGPOLICYCFG|基于RAN列表寻呼|本端规划|-
RAN列表类型|ADD PAGINGPOLICYCFG|邻接RAN列表|本端规划|-
寻呼时长(100ms)|ADD PAGINGPOLICYCFG|30|本端规划|-
寻呼次数|ADD PAGINGPOLICYCFG|1|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|1|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|2|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|205|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
SET GLOBALPOLICY|寻呼业务类型|LCS业务|本端规划|-
寻呼类型|SET GLOBALPOLICY|自定义寻呼|本端规划|-
全局寻呼策略组ID|SET GLOBALPOLICY|1|已配置数据中获取|引用ADD PAGINGPOLICYGROUPCFG命令中配置的寻呼策略组ID，可通过SHOW PAGINGPOLICYGROUPCFG查询。
配置步骤
步骤|说明|操作
---|---|---
1|打开基于机器学习的智能寻呼开关|SET NEIGHBOR GNB PAGING POLICY:SUPNEIGNBPAGING="YES"
2|配置寻呼策略模板|ADD PAGINGPOLICYCFG:PAGINGPOLICYID=1,PAGINGSTYLE="LASTNR",PAGINGINTERVAL=35,PAGINGTIMES=1ADD PAGINGPOLICYCFG:PAGINGPOLICYID=2,PAGINGSTYLE="LASTNRLIST",RANLISTTYPE="NERGHBORRANLIST",PAGINGINTERVAL=30,PAGINGTIMES=1
3|配置寻呼策略组|ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=1,PAGINGPRIORITY="NULL"ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=2,PAGINGPRIORITY="NULL"ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=205,PAGINGPRIORITY="NULL"
4|配置定位业务关联的寻呼策略组|SET GLOBALPOLICY:PAGINGSRVTYPE="LCS",PAGINGTYPE="CUSTOMIZED_PAGING",GLOBALPOLICYGRPID=1
场景三 :场景说明
时延敏感类业务的寻呼，如语音业务。 
数据规划
配置项|参数|取值|数据来源|说明
---|---|---|---|---
SET NEIGHBOR GNB PAGING POLICY|支持邻接gNodeB寻呼功能|是|本端规划|-
ADD PAGINGPOLICYCFG|寻呼策略模板ID|1|本端规划|-
寻呼方式|ADD PAGINGPOLICYCFG|基于RAN列表寻呼|本端规划|-
RAN列表类型|ADD PAGINGPOLICYCFG|邻接RAN列表|本端规划|-
寻呼时长(100ms)|ADD PAGINGPOLICYCFG|30|本端规划|-
寻呼次数|ADD PAGINGPOLICYCFG|1|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|1|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
ADD PAGINGPOLICYGROUPCFG|寻呼策略组ID|1|本端规划|-
寻呼策略模板ID|ADD PAGINGPOLICYGROUPCFG|205|已配置数据中获取|引用ADD PAGINGPOLICYCFG命令中配置的寻呼策略模板ID，可通过SHOW PAGINGPOLICYCFG查询。
寻呼优先级|ADD PAGINGPOLICYGROUPCFG|NULL|本端规划|-
SET GLOBALPOLICY|寻呼业务类型|语音业务|本端规划|-
寻呼类型|SET GLOBALPOLICY|自定义寻呼|本端规划|-
全局寻呼策略组ID|SET GLOBALPOLICY|1|已配置数据中获取|引用ADD PAGINGPOLICYGROUPCFG命令中配置的寻呼策略组ID，可通过SHOW PAGINGPOLICYGROUPCFG查询。
配置步骤
步骤|说明|操作
---|---|---
1|打开基于机器学习的智能寻呼开关|SET NEIGHBOR GNB PAGING POLICY:SUPNEIGNBPAGING="YES"
2|配置寻呼策略模板|ADD PAGINGPOLICYCFG:PAGINGPOLICYID=1,PAGINGSTYLE="LASTNRLIST",RANLISTTYPE="NERGHBORRANLIST",PAGINGINTERVAL=30,PAGINGTIMES=1
3|配置寻呼策略组|ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=1,PAGINGPRIORITY="NULL"ADD PAGINGPOLICYGROUPCFG:PAGINGPOLICYGRPID=1,PAGINGPOLICYID=205,PAGINGPRIORITY="NULL"
4|配置语音业务关联的寻呼策略组|SET GLOBALPOLICY:PAGINGSRVTYPE="VOICE",PAGINGTYPE="CUSTOMIZED_PAGING",GLOBALPOLICYGRPID=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|通用类业务按规划寻呼策略进行寻呼，并最终使用邻接RAN列表寻呼成功
---|---
测试目的|通用类业务（以信令为例）按规划寻呼策略进行寻呼，并最终使用邻接RAN列表寻呼成功。
预置条件|用户接入成功。开启License项目“AMF支持基于机器学习的智能寻呼”（license ID：7248）。打开基于机器学习的智能寻呼开关。按照通用类业务的配置实例配置寻呼策略。
测试过程|用户注册，PDU建立。N2释放，用户进入空闲态。UDM触发去注册流程。用户寻呼。
通过准则|用户按规划的寻呼策略进行寻呼。用户先根据最近活动的基站寻呼，终端在3s内未接入业务请求则继续使用邻接RAN列表寻呼，观察信令跟踪和性能统计是否符合预期。
测试结果|-
测试项目|负荷敏感类业务按规划寻呼策略进行寻呼，并最终使用邻接RAN列表寻呼成功
---|---
测试目的|负荷敏感类业务（以定位为例）按规划寻呼策略进行寻呼，并最终使用邻接RAN列表寻呼成功。
预置条件|用户接入成功。开启License项目“AMF支持基于机器学习的智能寻呼”（license ID：7248）。打开基于机器学习的智能寻呼开关。按照负荷敏感类业务的配置实例配置寻呼策略。
测试过程|用户注册，PDU建立。N2释放，用户进入空闲态。GMLC触发MT-LR定位。用户寻呼。
通过准则|用户按规划的寻呼策略进行寻呼。用户先根据最近活动的基站寻呼，终端在3s内未接入业务请求则继续使用邻接RAN列表寻呼，观察信令跟踪和性能统计是否符合预期。
测试结果|-
测试项目|时延敏感类业务按规划寻呼策略进行寻呼，并最终使用邻接RAN列表寻呼成功
---|---
测试目的|时延敏感类业务（以语音为例）按规划寻呼策略进行寻呼，并最终使用邻接RAN列表寻呼成功。
预置条件|用户接入成功。开启License项目“AMF支持基于机器学习的智能寻呼”（license ID：7248）。打开基于机器学习的智能寻呼开关。按照时延敏感类业务的配置实例配置寻呼策略。
测试过程|用户注册，PDU建立。N2释放，用户进入空闲态。SMF触发N1N2Transfer请求指示PDU建立。用户寻呼。
通过准则|用户根据邻接RAN列表寻呼，观察信令跟踪和性能统计是否符合预期。
测试结果|-
常见问题处理 :无。 
# 缩略语 
# 缩略语 
3GPP :3rd Generation Partnership Project第三代合作伙伴计划
5GC :5G Core Network5G核心网
## 5GS 
5G System5G系统
## 5QI 
5G QoS Indicator5G QoS指示
AMF :Access and Mobility Management Function接入和移动管理功能
## AN 
Access Network接入网
## ARP 
Allocation and Retention Priority分配保持优先级
AUSF :Authentication Server Function鉴权服务器功能
## CN 
Core Network核心网
DNN :Data Network Name数据网名称
## ECM 
EPS Connection ManagementEPS连接管理
## ECP 
Enterprise Communications Portal企业通信门户
EPS :Evolved Packet System演进的分组系统
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
GUTI :Globally Unique Temporary Identity全球唯一临时标识
## IMEISV 
International Mobile Equipment Identity and Software Version number国际移动设备识别码和软件版本号
NAS :Network Access Service网络接入服务
NF :Network Function网络功能
PCF :Policy Control Function策略控制功能
PDU :Packet Data Unit分组数据单元
## PPI 
Paging Policy Indication寻呼策略指示
## PSA 
PDU Session AnchorPDU会话锚点
RAN :Radio Access Network无线接入网
## RB 
Radio Bearer无线承载
## RRC 
Radio Resource Control无线资源控制
SMF :Service Management Function业务管理功能
Session Management Function会话管理功能
## SON 
Self-Organizing Network自组织网络
TA :Tracking Area跟踪区域
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
UPF :User Plane Function用户平面功能
## URLLC 
Ultra Reliable Low Latency Communication超高可靠超低时延通信
# ZUF-79-05 切换 
## ZUF-79-05-001 基于Xn切换 
特性描述 :特性描述 :术语 :术语|含义
---|---
PSA|PSA是PDU会话锚点，在5GC中作为UPF，对外出N6接口，充当网关角色。
I-UPF|I-UPF是中间UPF，对gNB出N3接口，对PSA出N9接口，充当中间转发UPF角色。
描述 :定义 :5GC切换流程是用户从一个无线基站移动到另一个无线基站时保证用户业务连续性的过程，包括基于Xn口和N2口的切换。在切换过程中，用户的无线连接无缝切换到目的无线接入网络。切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。
本特性对应Xn切换。基于Xn接口的切换是指当目标NR与源NR之间存在Xn接口时，源NR先将用户切换到目标NR，再通知核心网，更新N3用户面隧道。
背景知识 :在移动通信网络中，移动性是最基本的用户特征。在移动过程中，UE接入的无线基站可能发生变化，引入切换流程后，5GC系统可以保证当UE接入的无线基站发生变化时，用户业务不会中断。
应用场景 :用户从一个无线基站移动到另一个无线基站，两个无线基站之间存在Xn接口。 
客户收益 :受益方|受益描述
---|---
运营商|保证用户体验，用户业务不会因为位置移动而导致业务中断。
终端用户|此特性对终端用户不可见。
实现原理 :系统架构 :切换流程相关的系统架构如[图1]所示。
图1  系统架构

若Source NR与Target NR归属同一个AMF管理，则Source AMF与Target AMF所指同一个AMF。 
若切换过程中I-UPF（Intermediate UPF）没有变化，则Source I-UPF和Target I-UPF所指同一个I-UPF。 
若切换前用户面路径中不存在I-UPF，则Source I-UPF即为UPF（PSA）。 
若切换后用户面路径中不存在I-UPF，则Target I-UPF即为UPF（PSA）。 
涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|接口消息处理：负责处理N2接口以及Namf/Nsmf服务化接口消息。Target AMF选择：根据TargetID选择Target AMF。
SMF|NF|UPF重选：当UE不在UPF服务区时，SMF为用户重新选择UPF。用户面隧道维护：给新选择的UPF分配隧道地址和TEID，通知UPF更新RAN侧N3隧道信息等。接口消息处理：负责处理Nsmf服务化接口消息。
UPF|NF|用户面功能，完成PDU会话用户面数据转发，QoS及策略执行，用量上报，计费信息上报等功能。
网元|NR|流程触发：根据UE测量报告，决策是否需要发起切换流程。N3隧道维护：更新UPF的N3隧道信息。数据前转：通过非直传隧道，将需要前转的数据，前转给UE。
业务流程 :根据切换过程中，是否存在I-UPF改变，基于Xn接口的切换划分如下三种场景： 
基于Xn口的切换，无I-UPF变化。基于Xn口的切换，无I-UPF变化的流程如图2所示。图2  基于Xn口的切换，无I-UPF变化的流程图流程说明如下：Target NR发送Path Switch Request消息给AMF，携带Source AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU Session To Be Switched in Downlink List等信息。AMF收到Path Switch Request消息后，针对PDU Session To Be Switched in Downlink List的每一个会话，发送Nsmf_PDUSession_UpdateSMContext Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。SMF根据ueLocation判断UPF可以继续服务于UE，发送PFCP Session Modification Request消息给UPF，携带Target NR N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF，携带UPFN3隧道信息。SMF收到UPF响应后，回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF，携带UPFN3隧道信息。AMF收到SMF响应后，回复Path Switch Acknowledge消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU Session To Be Switched in Uplink List等信息。 
基于Xn口的切换，重选I-UPF。基于Xn口的切换，重选I-UPF的流程如图3所示，当切换前PDU会话的用户面路径中无I-UPF，此时Source I-UPF就是UPF（PSA）。图3  基于Xn口的切换，重选I-UPF的流程图流程说明如下：Target NR发送Path Switch Request消息给AMF，携带Source AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU Session To Be Switched in Downlink List等信息。AMF收到Path Switch Request后，针对PDU Session To Be Switched in Downlink List的每一个会话，发送Nsmf_PDUSession_UpdateSMContext Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。SMF收到Nsmf_PDUSession_UpdateSMContext Request后，根据ueLocation检测到用户位置发生变化，调用UPF选择功能重新选择I-UPF，最终选择的I-UPF与原有的I-UPF不同。SMF发送PFCP Session Establishment Request消息给新选择的Target I-UPF，携带Target NR N3隧道信息以及UPF（PSA） N9隧道信息。Target I-UPF回复PFCP Session Establishment Response消息给SMF，携带Target I-UPF N3隧道信息以及N9隧道信息。SMF发送PFCP Session Modification Request消息给UPF（PSA），携带Target I-UPF N9隧道信息。UPF（PSA）回复PFCP Session Modification Response消息给SMF，携带UPF（PSA） N9隧道信息。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF，携带Target I-UPF N3隧道信息，并启动资源保护定时器。AMF收到SMF响应后，回复Path Switch Acknowledge消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU Session To Be Switched in Uplink List等信息。如果步骤7中启动的定时器超时后，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source I-UPF释放用户上下文。Source I-UPF释放用户上下文，回复PFCP Session Release Response给SMF。 
基于Xn口的切换，移除I-UPF。基于Xn口的切换，移出I-UPF的流程如图4所示。图4  基于Xn口的切换，移出I-UPFF的流程图流程说明如下：Target NR发送Path Switch Request消息给AMF，携带Source AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU Session To Be Switched in Downlink List等信息。AMF收到Path Switch Request消息后，针对PDU Session To Be Switched in Downlink List每一个会话，发送Nsmf_PDUSession_UpdateSMContext Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。SMF收到Nsmf_PDUSession_UpdateSMContext Request消息后，根据ueLocation检测到用户位置发生改变，调用UPF选择功能重新选择I-UPF，最终选择的I-UPF为UPF（PSA）。SMF发送PFCP Session Modification Request消息给UPF（PSA），携带Target NR的N3隧道信息。启动定时器，该定时器超时后通知Source I-UPF释放资源。UPF（PSA）回复PFCP Session Modification Response消息给SMF，携带UPF（PSA） N3隧道信息。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF，携带UPF（PSA） N3隧道信息。AMF收到SMF响应后，回复Path Switch Acknowledge给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU Session To Be Switched in Uplink List等信息。步骤3启动的定时器超时后，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source I-UPF释放用户上下文。Source I-UPF释放用户上下文，回复PFCP Session Release Response给SMF。 
NF实现 :AMF实现 :AMF作为移动性管理NF，为该特性提供如下支持：
终结N2接口：N2接口的收发均通过AMF，包括SMF下发N2接口消息。 
位置登记：AMF记录用户当前位置信息。 
Target AMF选择：当Target NR与Source NR归属不同的AMF管理时，Source
AMF负责选择管理Target NR的AMF。 
对外提供服务化操作接口：包括转发SMF下发的N2接口消息、Source AMF通知Target AMF创建UE上下文。 
流程控制：记录切换业务所处的流程状态，基于流程状态，通知NR、SMF进行后续的操作。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性为基本业务流程，不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP TS 23.502|3GPP|Procedures for the 5G System
3GPP TS 29.500|3GPP|Technical Realization of Service Based Architecture
3GPP TS 29.502|3GPP|Session Management Services
3GPP TS 29.518|3GPP|Access and Mobility Management Services
3GPP TS 29.244|3GPP|Interface between the Control Plane and the User Plane Nodes
3GPP TS 38.413|3GPP|NGApplication Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性对于工程规划无特殊要求。 
O&M相关 :配置命令 :本特性不涉及配置命令的变化。 
定时器 :本特性不涉及定时器的变化。 
性能统计 :####### AMF性能统计 
测量类型|描述
---|---
切换流程测量|编号为51005开头的所有计数器
切换流程分NF测量|编号为51031开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现切换流程。 
测试用例 :测试项目|5GC切换
---|---
测试目的|AMF支持Xn口切换
预置条件|5G全网系统正常。RAN1和RAN2都已对接到AMF上，且RAN1和RAN2之间支持Xn口。UE已成功注册到5GC，并已创建了PDU会话。
测试过程|UE从RAN1覆盖区移动到RAN2覆盖区
通过准则|切换成功，数据业务不中断
测试结果|-
常见问题处理 :无 
## ZUF-79-05-002 基于N2切换 
特性描述 :特性描述 :术语 :术语|含义
---|---
PSA|PSA是PDU会话锚点，在5GC中作为UPF，对外出N6接口，充当网关角色。
I-UPF|I-UPF是中间UPF，对gNB出N3接口，对PSA出N9接口，充当中间转发UPF角色。
描述 :定义 :5GC切换流程是用户从一个无线基站移动到另一个无线基站时保证用户业务连续性的过程，包括基于Xn口和N2口的切换。在切换过程中，用户的无线连接无缝切换到目的无线接入网络。切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。
本特性对应N2切换。基于N2接口的切换是指当目标NR与源NR之间不存在Xn接口时，源NR需要借助核心网，将用户切换到目标NR。 
背景知识 :在移动通信网络中，移动性是最基本的用户特征。在移动过程中，UE接入的无线基站可能发生变化，引入切换流程后，5GC系统可以保证当UE接入的无线基站发生变化时，用户业务不会中断。
应用场景 :用户从一个无线基站移动到另一个无线基站，两个无线基站之间无Xn接口，此时采用N2接口切换。 
客户收益 :受益方|受益描述
---|---
运营商|保证用户体验，用户业务不会因为位置移动而导致业务中断。
终端用户|此特性对终端用户不可见。
实现原理 :系统架构 :切换流程相关的系统架构如[图1]所示。
图1  系统架构

若Source NR与Target NR归属同一个AMF管理，则Source AMF与Target AMF所指同一个AMF。 
若切换过程中I-UPF（Intermediate UPF）没有变化，则Source I-UPF和Target I-UPF所指同一个I-UPF。 
若切换前用户面路径中不存在I-UPF，则Source I-UPF即为UPF（PSA）。 
若切换后用户面路径中不存在I-UPF，则Target I-UPF即为UPF（PSA）。 
涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|接口消息处理：负责处理N2接口以及Namf/Nsmf服务化接口消息。Target AMF选择：根据TargetID选择Target AMF。
SMF|NF|UPF重选：当UE不在UPF服务区时，SMF为用户重新选择UPF。用户面隧道维护：给新选择的UPF分配隧道地址和TEID，通知UPF更新RAN侧N3隧道信息等。接口消息处理：负责处理Nsmf服务化接口消息。
UPF|NF|用户面功能，完成PDU会话用户面数据转发，QoS及策略执行，用量上报，计费信息上报等功能。
网元|NR|流程触发：根据UE测量报告，决策是否需要发起切换流程。N3隧道维护：更新UPF的N3隧道信息。数据前转：通过非直传隧道，将需要前转的数据，前转给UE。
业务流程 :概述 :本特性涉及的切换流程，包括基于N2接口的切换流程以及基于N2接口的切换取消流程。 
####### 基于N2接口的切换 
根据切换过程中是否存在I-UPF的变化，基于N2接口的切换可以划分为如下场景： 
基于N2接口的切换，无I-UPF变化。基于N2接口的切换，无I-UPF变化的流程如图2所示。图2  基于N2接口的切换，无I-UPF变化 说明：若用户面路径中不存在I-UPF，则UPF指UPF（PSA）。若用户面路径中存在I-UPF，则UPF指I-UPF。若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。流程说明如下：Source NR检测到用户需要切换到Target NR，发送Handover Required消息给Source AMF，携带Handover
Type、Target ID、Source To Target Transparent Container等信息。Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target
AMF。若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext
Request消息给Target AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source
To Target Transparent Container等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带用户位置、Target
AMF ID、切换准备状态等信息。SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF仍旧为切换前的UPF。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF，携带PDU会话ID、SM
N2 Information。Target AMF下发Handover Request消息给Target NR，携带Handover Type、SM
N2 Information List、UE AMBR、Security Context、UE Security Capabilities。Target NR回复Handover Request Acknowledge消息给Target AMF，携带PDU
Session Admitted List、Target To Source Transparent Container等信息，其中PDU
Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、SM
N2 Information。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。Target AMF发送Namf_Communication_CreateUEContext Response消息给Source
AMF，携带Target To Source Transparent Container。Source AMF发送Handover Command消息给Source NR，携带Target To Source
Transparent Container；Source NR收到Handover Command消息后，通过空口通知UE向目标小区切换。UE切换到Target NR后，Target NR发送Handover Notify消息给Target AMF，通知Target
AMF用户已经成功切换到目标小区。Target AMF收到Handover Notify消息后，发送Namf_Communication_N2InfoNotify消息给Source
AMF，通知Source AMF用户已经切换成功。Source AMF启动定时器，在定时器释放后，通知Source NR释放资源。Source NR回复Namf_Communication_N2InfoNotify
Ack消息给Target AMF。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换完成指示。SMF发送PFCP Session Modification Request消息给UPF，携带Target NR的N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF。SMF回复Nsmf_PDUSession_UpdateSMContext Response给AMF。步骤15启动的定时器超时后，Source AMF发送UE Context Release Command消息给Source
NR，通知Source NR释放用户上下文。Source NR释放用户上下文，回复UE Context Release Complete消息给Source AMF。 
基于N2接口的切换，重选I-UPF。基于N2接口的切换，重选I-UPF的流程如图3所示。图3  基于N2接口的切换，重选I-UPF的流程图 说明：若切换前，用户面路径中不存在I-UPF，则Source I-UPF就是UPF（PSA）。若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。流程说明如下：Source NR检测到用户需要切换到Target NR，发送Handover Required消息给Source AMF，携带Handover
Type、Target ID、Source To Target Transparent Container等信息。Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target
AMF。若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext
Request消息给Target AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source
To Target Transparent Container等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带用户位置、Target
AMF ID、切换准备状态等信息。SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF为Target I-UPF。SMF发送PFCP Session Establishment Request消息给Target I-UPF，通知Target
I-UPF创建PDU会话，携带UPF（PSA）的N9隧道信息。Target I-UPF回复PFCP Session Establishment Response消息给SMF，携带Target
I-UPF的N3隧道信息。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF，携带PDU会话ID、SM
N2 Information。Target AMF下发Handover Request消息给Target NR，携带Handover Type、SM
N2 Information List、UE AMBR、Security Context、UE Security Capabilities。Target NR回复Handover Request Acknowledge消息给Target AMF，携带PDU
Session Admitted List、Target To Source Transparent Container等信息，其中PDU
Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、SM
N2 Information。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。Target AMF发送Namf_Communication_CreateUEContext Response消息给Source
AMF，携带Target To Source Transparent Container。Source AMF发送Handover Command消息给Source NR，携带Target To Source
Transparent Container；Source NR收到Handover Command消息后，通过空口通知UE向目标小区切换。UE切换到Target NR后，Target NR发送Handover Notify消息，通知Target AMF用户已经成功切换到目标小区。Target AMF收到Handover Notify消息后，发送Namf_Communication_N2InfoNotify消息给Source
AMF，通知Source AMF用户已经切换成功。Source AMF启动定时器，在定时器释放后，通知Source NR释放资源，回复Namf_Communication_N2InfoNotify
Ack消息给Target AMF。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换完成指示。SMF发送PFCP Session Modification Request消息给UPF，携带Target NR的N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF。SMF回复Nsmf_PDUSession_UpdateSMContext Response响应消息给Target AMF。若切换前用户面路径中存在I-UPF，则启动定时器。如果步骤17启动的定时器超时后，Source AMF发送UE Context Release Command消息给Source
NR，通知Source NR释放用户上下文。Source NR释放用户上下文，回复UE Context Release Complete消息给Source AMF。如果步骤21启动的定时器超时，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source
I-UPF释放PDU会话。Source I-UPF回复PFCP Session Release Response消息给SMF。 
基于N2接口的切换，移出I-UPF。基于N2接口的切换，移出I-UPF的流程如图4所示。图4  基于N2接口的切换，移出I-UPF的流程图 说明：若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source
AMF指同一个AMF。流程说明如下：Source NR检测到用户需要切换到Target NR，发送Handover Required消息给Source AMF，携带Handover
Type、Target ID、Source To Target Transparent Container等信息。Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target
AMF。若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext
Request消息给Target AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source
To Target Transparent Container等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带用户位置、Target
AMF ID、切换准备状态等信息。SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF为UPF（PSA）。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF，携带SM
N2 Information。Target AMF下发Handover Request消息给Target NR，携带Handover Type、SM
N2 Information List、UE AMBR、Security Context、UE Security Capabilities。Target NR回复Handover Request Acknowledge消息给Target AMF，携带PDU
Session Admitted List、Target To Source Transparent Container等信息，其中PDU
Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、SM
N2 Information。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。Target AMF发送Namf_Communication_CreateUEContext Response消息给Source
AMF，携带Target To Source Transparent Container。Source AMF发送Handover Command消息给Source NR，携带Target To Source
Transparent Container。Source NR收到Handover Command消息后，通过空口通知UE向目标小区切换。UE切换到Target NR后，Target NR发送Handover Notify消息，通知Target AMF用户已经成功切换到目标小区。Target AMF收到Handover Notify消息后，发送Namf_Communication_N2InfoNotify消息给Source
AMF，通知Source AMF用户已经切换成功。Source AMF启动定时器，在定时器释放后，通知Source NR释放资源，回复Namf_Communication_N2InfoNotify
Ack消息给Target AMF。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换完成指示。SMF发送PFCP Session Modification Request消息给UPF，携带Target NR的N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF。SMF回复Nsmf_PDUSession_UpdateSMContext Response响应消息给Target AMF。启动定时器，带定时释放后通知I-UPF释放资源。如果步骤15启动的定时器超时，Source AMF发送UE Context Release Command消息给Source
NR，通知Source NR释放用户上下文。Source NR释放用户上下文，回复UE Context Release Complete消息给Source AMF。如果步骤19启动的定时器超时，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source
I-UPF释放PDU会话。Source I-UPF回复PFCP Session Release Response消息给SMF。 
####### 基于N2接口的切换取消 
基于N2接口的切换取消流程如[图5]所示。
图5  基于N2接口的切换取消流程图

 说明： 
若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source
AMF指同一个AMF。 
流程说明如下： 
在N2切换过程中，Source NR检测到需要取消切换，发送Handover Cancel消息给Source AMF，携带切换取消原因。 
若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_ReleaseUEContext
Request消息给Target AMF，通知Target AMF终止切换。 
若Target AMF已经下发Handover Request消息给Target NR，则发送UE Context Release
Command消息给Target NR，通知Target NR释放用户上下文。 
Target NR回复UE Context Release Complete消息给Target AMF。 
Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换取消指示。 
若已经重选了新的I-UPF，则发送PFCP Session Release Request消息给新选择的Target
I-UPF。 
Target I-UPF回复PFCP Session Release Response消息给SMF。 
SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。 
Target AMF回复Namf_Communication_ReleaseUEContext Response消息给Source
AMF。 
Source AMF回复Handover Cancel Acknowledge消息给Source NR。 
NF实现 :AMF实现 :AMF作为移动性管理NF，为该特性提供如下支持：
终结N2接口：N2接口的收发均通过AMF，包括SMF下发N2接口消息。 
位置登记：AMF记录用户当前位置信息。 
Target AMF选择：当Target NR与Source NR归属不同的AMF管理时，Source
AMF负责选择管理Target NR的AMF。 
对外提供服务化操作接口：包括转发SMF下发的N2接口消息、Source AMF通知Target AMF创建UE上下文。 
流程控制：记录切换业务所处的流程状态，基于流程状态，通知NR、SMF进行后续的操作。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性为基本业务流程，不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP TS 23.502|3GPP|Procedures for the 5G System
3GPP TS 29.500|3GPP|Technical Realization of Service Based Architecture
3GPP TS 29.502|3GPP|Session Management Services
3GPP TS 29.518|3GPP|Access and Mobility Management Services
3GPP TS 29.244|3GPP|Interface between the Control Plane and the User Plane Nodes
3GPP TS 38.413|3GPP|NGApplication Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性对于工程规划无特殊要求。 
O&M相关 :配置命令 :本特性不涉及配置命令的变化。 
定时器 :本特性不涉及定时器的变化。 
性能统计 :###### AMF性能统计 
测量类型|描述
---|---
切换流程测量|编号为51005开头的所有计数器
切换流程分NF测量|编号为51011开头的所有计数器
告警和通知 :该特性不涉及AMF告警/通知消息的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现切换流程。 
测试用例 :测试项目|5GC切换
---|---
测试目的|AMF支持N2口切换
预置条件|5G全网系统正常。RAN1和RAN2都已对接到AMF上，且RAN1和RAN2之间不支持Xn口。UE已成功注册到5GC，并已创建了PDU会话。
测试过程|UE从RAN1覆盖区移动到RAN2覆盖区
通过准则|切换成功，数据业务不中断
测试结果|-
常见问题处理 :无 
# 缩略语 
# 缩略语 
5GC :5G Core Network5G核心网
AMF :Access and Mobility Management Function接入和移动管理功能
NF :Network Function网络功能
## NR 
New Radio新无线
## PSA 
PDU Session AnchorPDU会话锚点
RAN :Radio Access Network无线接入网
SMF :Session Management Function会话管理功能
## TEID 
Tunnel Endpoint Identifier隧道端点标识
UE :User Equipment用户设备
UPF :User Plane Function用户平面功能
# ZUF-79-06 AMF辅助会话管理 
## ZUF-79-06-003 AMF辅助SM消息传输 
概述 :AMF通过N1/N2和N11接口透明传输NAS和AS消息以及与会话管理相关的信息。 
客户收益 :AMF透明传输会话管理相关消息和信息。 
说明 :AMF通过N1/N2和N11接口透明传输NAS和AS消息以及与会话管理相关的信息。流程包括： 
PDU会话建立 
PDU会话更改 
PDU会话释放 
## ZUF-79-06-004 UE-AMBR管理 
概述 :AMF从UDM获得UE签约的UE-AMBR，通过N2消息下发给RAN。 
客户收益 :基于不同的QoS需求，为用户提供差异化服务。 
灵活控制漫游用户的UE-AMBR，更好地保证本地用户体验。 
说明 :为了控制漫游用户带宽消耗，保障本网用户业务感受，AMF支持本地QoS策略。AMF可以基于SUPI号段确定UE-AMBR策略，根据SUPI号段无法确定UE-AMBR策略时，则使用缺省的UE-AMBR策略。 
本地策略，包括如下几种： 
签约：使用签约的UE-AMBR。 
本地配置：使用本地配置的UE-AMBR。 
签约与本地配置取小：如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地UE-AMBR策略，使用签约的UE-AMBR。 
## ZUF-79-06-005 DNN更正 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :DNN更正指当用户接入5GC网络时，如果请求消息中携带的DNN不合法，则AMF对用户使用的DNN按运营商的策略更正为其他DNN，用户使用更正后的DNN激活PDU会话，访问数据业务和其他业务。 
DNN不合法通常是用户请求的DNN和签约的DNN不匹配，也可能是用户请求的DNN格式错误。 
背景知识 :DNN是用户通过手机上网时必须配置的一个参数，它决定了用户的手机通过哪种接入方式来访问网络，在骨干网中用来标识要使用的外部PDN网络。DNN由以下两部分组成： 
网络标识（必选）：由网络运营者分配给ISP或公司，与其固定Internet域名相同的一个标识。 
运营商标识（可选）：其形式为“xxx.yyy.gprs”（如MNC.MCC.gprs）或”xxx.yyy.3gppnetwork.org”（ MNC.MCC. 3gppnetwork.org），用于标识归属网络。 
当运营商间因互相吞并或其他原因导致用户转网，如果用户原来的DNN和转网后签约的DNN不再匹配，则需要更正DNN。有些终端的DNN无法更正，有些终端的DNN虽然可以更正但难以操作。因此，需要AMF对某些号段的用户按照一定的策略更正DNN。 
DNN更正就是对网络标识的更正。DNN网络标识通常作为用户签约数据存储在UDM中，用户在发起分组业务时也可向AMF提供DNN。AMF根据DNN和用户切片通过NRF或本地域名解析得到SMF的IP地址。 
应用场景 :###### DNN更正方式为“指定DNN” 
对漫游用户，跨国或跨网运营商拥有多个网络时，如果用户漫游到隶属于该运营商的另一个网络，运营商会要求用户在拜访地接入。同一运营商的多个网络之间不存在运营商间的漫游计费结算。在这种场景下，如果请求消息中携带的DNN不合法，则AMF对此类漫游号段用户的DNN使用更正方式为“指定DNN”。
对本地用户来说，用户都是本地接入，如果运营商决策UDM签约的默认DNN可能会变更或不适合用于更正的DNN，则当请求消息中携带的DNN不合法时，AMF对本地号段用户使用的DNN更正方式为“指定DNN”。 
总之，漫游用户或本地用户在5GC网络激活时，如果请求消息中携带的DNN不合法，则AMF根据用户的SUPI对原来DNN NI进行更正，使用指定的DNN进行SMF地址查询，激活PDU会话访问数据业务和其他业务。
###### DNN更正方式为“签约DNN” 
对漫游用户，非跨国或跨网运营商一般要求用户回归属地接入，以便于计费。在这种场景下，如果请求消息中携带的DNN不合法，则AMF对此类漫游号段用户使用的DNN更正方式为“签约DNN”。 
对本地用户来说，用户都是本地接入，如果请求消息中携带的DNN不合法，则AMF对本地号段用户的DNN使用更正方式为“签约DNN”。 
总之，漫游用户或本地用户在5GC网络激活时，如果请求消息中携带的DNN不合法，则AMF根据用户的SUPI决策，使用UDM签约的默认DNN进行SMF地址查询，激活PDU会话访问数据业务和其他业务。 
 说明： 
AMF根据用户SUPI号段使用DNN更正方式“指定DNN”，如果指定DNN没有签约，则AMF会使用默认签约的DNN。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户接入成功率，提高用户使用数据业务和其他业务的成功率，从而提升用户对移动网络的满意度。
移动用户|享受优质的网络服务。
实现原理 :系统架构 :5G系统架构如[图1]所示。
图1  系统架构

涉及的网元 :网元名称|网元作用
---|---
AMF|AMF对用户使用的DNN进行更正，使用更正后的DNN进行SMF地址查询，建立PDU会话。
UDM|在DNN更正功能中，UDM需要为用户提供签约的默认DNN。
协议栈 :本特性涉及的接口说明参见[表1]。
接口|描述|协议栈
---|---|---
N1|UE与AMF间逻辑接口|ZUF-79-19-001 N1
N2|NG-RAN与AMF间逻辑接口|ZUF-79-19-002 N2
N8|AMF和UDM间逻辑接口|ZUF-79-19-003 N8
本网元实现 :AMF实现
UE请求PDU会话建立流程中，AMF检查DNN失败，对用户使用的DNN进行更正。
UDM需要为用户提供签约的默认DNN。 
AMF使用更正后的DNN进行SMF地址查询，激活PDU会话访问数据业务和其他业务。
DNN更正流程
DNN更正流程如[图2]所示。
图2  DNN更正流程

AMF基于SUPI/S-NSSAI获取DNN更正策略： 
指定DNN：如果指定的DNN在签约DNN范围中，则使用指定的DNN；否则，使用“签约DNN”策略。 
签约DNN：如果存在签约默认DNN，则使用签约的默认DNN；否则，使用签约的非默认DNN。 
业务流程 :UE发起PDU会话建立请求，DNN更正的流程如[图3]所示。
图3  UE请求PDU会话建立DNN更正

流程说明： 
在UE注册流程中，AMF向UDM获取UE的签约信息（包括签约的DNN）。 
UE发起PDU会话建立请求，请求消息中携带的DNN不合法。 
AMF收到UE发起的PDU会话建立请求，进行DNN检查。如果DNN检查失败，且DNN更正功能启用，则AMF根据用户的SUPI/S-NSSAI对用户使用的DNN进行更正。
AMF DNN更正有两种方式： 
如果使用“指定DNN” 更正方式，则AMF优先使用指定的DNN进行更正。 
如果使用“签约DNN”更正方式，则AMF使用UDM签约的DNN进行更正。 
AMF使用更正后的DNN和用户切片选择SMF。 
AMF根据SMF选择策略选择得到SMF，向SMF发送PDU会话创建请求消息并携带已选择的SMF地址。
 说明： 
UE发起PDU会话建立请求流程的其他处理过程同现有系统。 
AMF向SMF发送PDU会话创建请求消息时，可以灵活控制仅携带更正后的DNN、或者同时携带UE请求的DNN和AMF更正后的DNN。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :无。  
特性能力 :名称|指标
---|---
DNN更正配置|AMF最多支持基于4096个用户SUPI号段进行DNN更正。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.20|对DNN的实现原理进行更新。
01|V7.19.12|首次发布。
License要求 :该特性为基本特性，无需License支持。 
对其他网元的要求 :UE|NR|UDM|SMF
---|---|---|---
√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增命令参见[表2]。
配置项|命令
---|---
DNN更正策略|SET DNNCORRECT POLICY
SHOW DNNCORRECT POLICY|DNN更正策略
DNN更正配置|ADD DNNCORRECT CONFIG
MOD DNNCORRECT CONFIG|DNN更正配置
DEL DNNCORRECT CONFIG|DNN更正配置
SHOW DNNCORRECT CONFIG|DNN更正配置
DNN相关参数设置|SET DEFAULT DNNPARACONFIG
SHOW DEFAULT DNNPARACONFIG|DNN相关参数设置
ADD PLMN DNNPARACONFIG|DNN相关参数设置
SET PLMN DNNPARACONFIG|DNN相关参数设置
DEL PLMN DNNPARACONFIG|DNN相关参数设置
SHOW PLMN DNNPARACONFIG|DNN相关参数设置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :DNN更正功能涉及的配置如下： 
配置支持DNN更正策略。 
配置DNN更正方式。 
配置DNN相关参数配置。当选择DNN与请求DNN不同时，需要设置DNN的携带策略。 
配置前提 :已完成初始配置。 
配置过程 :执行[SET DNNCORRECT POLICY]命令，开启DNN更正功能。
执行[ADD DNNCORRECT CONFIG]命令，新增DNN更正配置。对于不正确的DNN，先按SUPI号段+切片信息（SST+SD）进行DNN更正方式的查询，如果查询失败，再按照SUPI号段+无效切片（SST=0，SD=NULL）进行查询。遍历从最长的SUPI号段开始，依次缩短1位查询，直到查出结果。DNN更正方式有两种，分别是”签约DNN“和”指定DNN“。
执行[ADD PLMN DNNPARACONFIG]命令，新增基于PLMN的DNN携带策略。如果未配置基于PLMN的DNN相关参数配置，AMF会读取“DNN相关参数配置”里面的默认配置[SET DEFAULT DNNPARACONFIG]命令，来决策当“选择DNN”与“请求DNN”不同时，根据默认的DNN携带策略来执行流程。
配置实例 :场景说明 :
当本地用户接入5GC网络时，如果请求消息中携带的DNN和签约的DNN不匹配或者用户请求的DNN格式错误，则AMF对本地号段用户使用的DNN按运营商的策略更正为其他DNN。用户使用更正后的DNN激活PDU会话访问数据业务和其他业务。 
数据规划 :参数|取值
---|---
DNN更正策略配置|支持DNN更正功能|支持DNN更正
DNN更正配置|SUPI号段|46011
SST|DNN更正配置|0
SD|DNN更正配置|NULL
DNN更正方式|DNN更正配置|签约DNN
DNN|DNN更正配置|zte.com.cn
基于PLMN的DNN相关参数配置|移动国家码|460
移动网络码|基于PLMN的DNN相关参数配置|11
选择DNN与请求DNN不同时DNN携带策略|基于PLMN的DNN相关参数配置|1-携带dnn和selectedDnn
DNN相关参数配置|选择DNN与请求DNN不同时DNN携带策略|1-携带dnn和selectedDnn
配置步骤 :步骤|说明|操作
---|---|---
1|打开DNN更正策略。|SET DNNCORRECT POLICY:DNNCORRECTPOLICY="SUPDNNCORRECT"
2|增加本地用户号段的DNN更正策略为“签约DNN”。|ADD DNNCORRECT CONFIG:SUPI="46011",SST="0",SD="NULL",DNNCORRECTPOLICY="SUBSCRIBEDNN",DNN="zte.com.cn"
3|设置基于PLMN的DNN相关参数配置。|ADD PLMN DNNPARACONFIG:MCC="460",MNC="11",DNNCARRYPOLICYONPLMN="CARRYDNNANDSELECTEDDNN"
4|设置DNN相关参数配置。|SET DEFAULT DNNPARACONFIG:DNNCARRYPOLICY="CARRYDNNANDSELECTEDDNN"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF根据用户SUPI对使用的DNN进行更正
---|---
测试目的|验证AMF对用户不合法的DNN按运营商的策略更正为其他DNN。
预置条件|5G网络中各NF系统及操作维护台运行正常。用户在UDM中已签约5G业务。在AMF上建立用户信令跟踪。UE已经注册到5G网络。在AMF上配置本地用户号段的DNN更正策略为“签约DNN”。在AMF上配置基于PLMN的DNN参数携带策略，策略为携带ddn和selectedDnn。
测试过程|UE在5G网络开机发起PDU建立流程，携带不合法的DNN。
通过准则|UE使用更正后的DNN成功激活PDU会话业务。用户信令跟踪能够跟踪到相应的消息，信令流程正确。并且在CreateSmContextRequest消息中，能观察到同时携带了dnn和selectedDnn。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## A-SMF 
Anchor-SMF锚点SMF
AMF :Access and Mobility Management Function接入和移动管理功能
DNN :Data Network Name数据网名称
## I-SMF 
Intermediate-SMF中间SMF
## ISP 
Internet Service Provider因特网业务提供者
## NI 
Network Identifier网络标识
PDU :Packet Data Unit分组数据单元
SMF :Session Management Function会话管理功能
SUPI :Subscriber Permanent Identifier用户永久标识
UDM :Unified Data Management统一数据管理
# ZUF-79-07 安全管理 
## ZUF-79-07-001 5G AKA鉴权 
特性描述 :特性描述 :术语 :术语|含义
---|---
鉴权|鉴权指对用户是否合法进行鉴定，包括网络对用户进行鉴权和用户对网络进行鉴权。
完整性保护|完整性保护是指对用户信令或数据进行校验，在信令或数据后面增加校验码，防止被中间节点撰改。
加密性保护|加密性保护是指对用户信令或数据进行加密后再传输，防止被中间节点窃听。
描述 :定义 :5G-AKA流程是指5GC网络对UE进行鉴权的一种方式，采用基于Milenage算法的AKA鉴权，实现UE和网络间的双向认证。
5GC对用户鉴权完成之后，用户才可以注册到5G网络，并通过5G网络访问数据业务和其他业务。 
背景知识 :在GPRS网络（2G）中，网络侧对用户鉴权以防止未经授权的接入。但GPRS网络存在一些安全隐患，例如使用的128 bit的密钥容易被破解，不支持数据的完整性保护，难以发现数据被篡改，用户无法对网络进行鉴权。 
UMTS网络（3G）在GPRS网络的基础上进行了改进，采用基于Milenage算法的AKA鉴权，实现了终端和网络间的双向认证，定义了强制的完整性保护和可选的加密保护，提供了更好的安全性保护。 
LTE网络（4G）采用UMTS网络相同的安全架构，也使用AKA鉴权算法，也支持对信令和数据的完整性保护和加密，但NAS信令的完整性保护和加密由MME完成，AS信令的完整性保护和加密由eNodeB完成。
相对4G而言，5G网络在安全性方面进行了以下几个方面的增强： 
通过SUCI方案，解决了以往4G安全协议中，用户号码IMSI在首条明文消息中传递的问题； 
通过鉴权确认机制，解决了漫游场景下拜访网络对于归属网络接入欺骗问题； 
统一了3GPP和non-3GPP鉴权方式，UE和5GC必须支持5G AKA和EPA AKA’两种认证方式。 
应用场景 :AMF启用对用户鉴权当用户触发注册、业务请求或去注册流程时，AMF根据本地配置决策是否为用户提供鉴权服务。若需要进行鉴权，则AMF调用AUSF服务，通知AUSF对UE进行鉴权。为了达到精细化控制鉴权策略的目的，AMF将注册过程进行了场景细分，并按照细分后的场景分别进行鉴权策略的配置。细分后的业务场景参见表1。表1  业务场景业务场景场景说明SUCI初始注册UE触发初始注册，注册请求消息中携带的用户标识为SUCI。局内GUTI初始注册UE曾经在某AMF下注册过，再在该AMF下重新注册，注册请求消息中携带的用户标识为该AMF在上次UE注册时为其分配的临时标识5G GUTI。RAT内局间GUTI初始注册UE曾经在AMF1下注册过，然后在AMF2下重新注册，注册请求消息中携带的用户标识为上次注册时AMF1为其分配的临时标识5G GUTI。RAT间GUTI初始注册UE曾经在4G附着过，然后在5G下重新发起初始注册，注册请求消息中携带的用户标识是由4G MME为UE分配的临时标识4G GUTI转化而来的5G GUTI。周期性注册更新UE周期性定时器到达，触发注册过程，注册类型为“periodic registration updating”。局内移动性注册更新UE已经注册到AMF，位置移动时，比如UE进入一个跟踪区，该跟踪区归属于用户所注册的AMF管理，但不在该AMF为其分配的跟踪区列表中，则UE触发注册类型为“mobility registration updating”的注册过程。RAT内局间移动性注册更新UE已经注册到AMF1，位置移动时，比如UE进入一个跟踪区，该跟踪区不归属于用户所注册的AMF1管理，而是归属于AMF2管理，则UE触发注册类型为“mobility registration updating”的注册过程到AMF2。RAT间局间移动性注册更新UE已经在4G网络附着，位置移动到5G跟踪区下，或者用户打完VoLTE电话后根据自身配置需要再次回到5G网络，则UE触发注册类型为“mobility registration updating”的注册过程到AMF。局内切换后移动性注册更新用户已经注册到AMF并且处于连接态，由于位置移动从一个5G基站切换到另一个5G基站，切换前后两个5G基站均归属于用户所注册的AMF管理。切换成功后，UE进入一个跟踪区，该跟踪区归属于用户所注册的AMF管理，但不在该AMF为其分配的跟踪区列表中，则UE触发注册类型为“mobility registration updating”的注册过程。RAT内局间切换后移动性注册更新用户已经注册到AMF1并且处于连接态，由于位置移动从一个5G基站切换到另一个5G基站，切换目标5G基站归属另外一个AMF2管理。切换成功后，UE进入一个跟踪区，该跟踪区并不归属于用户所注册的AMF1管理，而是归属于AMF2管理，则UE触发注册类型为“mobility registration updating”的注册过程到AMF2。RAT间局间切换后移动性注册更新用户已经注册到4G网络并且处于连接态，由于位置移动从一个4G基站切换到一个5G基站，切换成功后，UE触发注册类型为“mobility registration updating”的注册过程到AMF。业务请求-去注册请求-鉴权策略的详细描述参见表2。表2  鉴权策略鉴权策略详细描述强制鉴权慎重使用该选项，该鉴权类型会导致对应业务类型流程每执行一次就触发一次鉴权，当用户业务类型流量较大时，会加重网络负担。强制不鉴权鉴于5GC网络非常强调网络安全和用户隐私保护，不推荐使用“强制不鉴权”。系统判断AMF检测到UE和AMF之间没有安全环境或安全环境被破坏，则AMF自动触发对UE鉴权，以建立新的安全环境，保障后续的信令消息在可靠的安全环境中传输。可以理解“系统判断”在“需要”时鉴权，“不需要”时不鉴权。 
AMF对NAS消息进行完整性保护和加密启用对用户鉴权后，按照表3方式设置AMF支持完整性保护和加密算法。表3  完整性保护和加密算法完整性保护算法是否支持级别NIA3不支持（一般UE终端都不支持）N/ANIA2支持2（高）NIA1支持1（低）NEA3不支持（一般UE终端都不支持）N/ANEA2支持2（高）NEA1支持1（中）NEA0支持（实际为不进行加密）0（低） 
AMF为用户分配5G-GUTI用户进行注册，AMF为用户分配临时标识5G-GUTI，用户保存下来，在下次业务使用此5G-GUTI作为用户标识。 
客户收益 :受益方|受益描述
---|---
运营商|拒绝非法用户接入，防止用户相关数据被窃听和篡改。
终端用户|避免使用到非法或损害用户利益的网络。
实现原理 :系统架构 :5GC组网架构如[图1]所示。
图1  系统架构

AKA鉴权涉及的网元参见下表。 
网元名称|网元作用
---|---
UE|对网络进行鉴权及对NAS信令、AS信令和数据进行完整性保护与加密。
RAN|对用户提供接入层安全功能，对AS信令和数据完整性保护与加密。
AMF|确定是否对用户进行鉴权，完成对NAS信令的完整性保护和加解密保护。
AUSF|AMF确定对UE鉴权后，调用AUSF的接口，通知AUSF对用户鉴权。AUSF通过5G-AKA或EPA AKA’方式完成对用户的鉴权。
UDM|生成用户的鉴权向量。
业务流程 :AKA鉴权流程
5G AKA鉴权流程如[图2]所示。
图2  5G AKA鉴权流程图

流程说明： 
在注册/去注册/业务请求流程中，AMF根据本地策略判定用户是否需要鉴权。如果需要鉴权，则AMF发起5G-AKA鉴权流程。 
AMF向AUSF发送Nausf_UEAuthentication_Authenticate Request消息，携带用户标识，并通知AUSF对用户进行鉴权。 
AUSF向UDM发送Nudm_UEAuthentication_Get Request消息，请求获取鉴权向量5G HE AV。 
UDM生成5G HE AV。 
UDM给AUSF返回Nudm_UEAuthentication_Get Response消息，携带鉴权向量5G HE AV信息。 
AUSF根据UDM返回的鉴权向量5G HE AV，根据消息中的5G HE AV重新进行组装、计算，生成5G AV（RAND/HXRES*/AUTN/KASME*）。 
AUSF给AMF返回Nausf_UEAuthentication_Authenticate Response消息，携带5G AV和Confirm Needed等信息。 
AMF给UE发送Authentication Request消息，携带RAND/AUTN/HXRES*等参数。 
UE根据HXRES*完成对网络鉴权后，返回Authentication Response消息，携带XRES*等信息。 
UE生成Kamf等信息。 
AMF生成Kamf等信息。 
当AUSF指示需要鉴权确认时，AMF向AUSF发送Nausf_UEAuthentication_Authenticate Confirm消息，携带XRES*、用户标识等信息。 
AUSF检查XRES*等信息。 
SMC流程
安全模式命令（SMC）流程如[图3]所示。AMF和UE协商使用安全算法。
图3  安全模式命令流程图

AMF完成对用户的鉴权后，向UE发送Security Mode Command消息。该消息中包含ngKSI、完整性保护和加密算法。 
UE接受完整性保护和加密的算法，向AMF发送Security Mode Complete消息。 
NAS消息完整性保护机制
NAS消息完整性保护机制： 
AMF发送下行NAS消息时，对NAS消息进行完整性保护。 
AMF将NAS下行序列号、方向位(下行)、承载标识、NAS消息、NAS信令的完整性保护密钥KNASint作为输入，通过完整性保护算法获取MAC（Message Authentication Code），并将MAC放入发送的消息中。 
AMF接收到上行NAS消息时，对NAS消息进行完整性检查。 
AMF将NAS上行序列号、方向位(上行)、承载标识、NAS消息、NAS信令的完整性保护密钥KNASint作为输入，通过完整性保护算法计算XMAC，并与接收的消息中的MAC进行比较。如果一致，则完整性检查成功。 
NAS消息加解密保护机制
NAS消息加解密保护机制： 
AMF发送下行NAS消息时，对NAS消息进行加密。 
AMF将NAS下行序列号、方向位(下行)、承载标识、NAS消息位长度、NAS信令的加密密钥KNASenc作为输入，通过加密算法计算密钥流。AMF根据密钥流对NAS消息明文进行加密，获取NAS消息密文。 
AMF接收到上行NAS消息时，对NAS消息进行解密。 
AMF将NAS上行序列号、方向位(上行)、承载标识、NAS消息位长度、NAS信令的加密密钥KNASenc作为输入，通过加密算法计算密钥流。AMF根据密钥流对接收到的NAS消息密文进行解密，获取NAS消息明文。 
用户标识分配
用户在注册过程中，AMF会为用户分配5G-GUTI，流程图如[图4]所示。
图4  用户临时标识分配流程图

流程说明： 
UE向AMF发起注册请求。 
AMF为用户分配5G-GUTI，并在注册接受消息中将5G-GUTI携带给UE。 
UE接受5G-GUTI，并向AMF返回注册完成消息。 
NF实现 :本特性需要UE、RAN、AMF、AUSF、UDM等网元配合完成。 
与UE交互，完成UE和5GC的双向鉴权。 
与RAN交互，完成UE和5GC鉴权相关消息的传递。 
与AUSF交互，完成通知AUSF对UE开启5G-AKA等过程。 
与UDM交互，完成获取用户鉴权向量信息。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N12|ZUF-79-19-005 N12
系统影响 :鉴权策略的不同可能会导致AMF与AUSF/UDM之间信令增加以及业务时延增大。 
对用户信令进行完整性保护和加密保护，对AMF的性能会有一定影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :安全流程是基本业务流程，是后续所有的流程的基础。如果选择需要进行安全流程却无法使用，则其他业务都无法使用。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP TS 23.502|3GPP|Procedures for the 5G System
3GPP TS 33.501|3GPP|Security architecture and procedures for 5G system
3GPP TS 24.501|3GPP|-
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|RAN|AMF|AUSF|UDM
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :网络需规划好支持哪些安全算法，安全算法的优先级 
鉴权控制策略 
O&M相关 :命令 :新增配置项参见下表。 
配置项|命令
---|---
缺省鉴权策略配置|SHOW DEFAUTHSTRATEGY
SET DEFAUTHSTRATEGY|缺省鉴权策略配置
基于SUPI号段的鉴权策略配置|ADD SUPIAUTHSTRATEGY
SET SUPIAUTHSTRATEGY|基于SUPI号段的鉴权策略配置
DEL SUPIAUTHSTRATEGY|基于SUPI号段的鉴权策略配置
SHOW SUPIAUTHSTRATEGY|基于SUPI号段的鉴权策略配置
加密完保配置|SET ENCRYANDINTEG
SHOW ENCRYANDINTEG|加密完保配置
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :该配置过程实现5G鉴权过程，包括： 
AMF根据业务种类和配置策略启用对用户鉴权过程： 
强制鉴权：不管用户之前是否是合法用户，都做鉴权过程。 
系统判断：根据实际情况判断用户是否要做鉴权过程。 
强制不鉴权：不管用户之前是否是合法用户，都不做鉴权过程，允许用户接入。 
AMF根据完整性保护和加密的配置方式以及UE支持的安全能力，协商出用户的加密和完整性保护的安全算法。 
根据配置的算法支持能力和终端的安全能力取交集，得到一个候选算法列表。 
根据本地配置的算法优先级，选出高优先级的算法。如果同优先级有好几个算法，随机选一个算法。 
配置前提 :AMF运行正常。 
AMF网管能正常连接。 
配置过程 :使用[SET DEFAUTHSTRATEGY]命令，设置缺省的鉴权策略。
使用[SET ENCRYANDINTEG]命令，设置加密和完整性保护算法。
配置实例 :场景说明 :某运营商要求对5G用户的鉴权策略如下： 
对注册/去注册流程采取强制鉴权，对业务请求流程采取系统判断方式。 
加密算法使用算法0、算法1和算法2，算法优先级从高到底依次为：算法2>算法1>算法0。 
完整性保护算法使用算法1和算法2，优先使用算法2。 
数据规划 :无 
配置步骤 :步骤|说明|操作
---|---|---
1|配置对注册/去注册流程采取强制鉴权方式，对业务请求流程采取系统判断方式|SET DEFAUTHSTRATEGY:SERVICETYPE="SUCIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="INTRAGUTIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="INTERGUTIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="RATGUTIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="DEREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="SERVICEREQ",AUTHSTRATEGY="SYSTEMDEFINE"
2|配置加密算法使用算法0、算法1和算法2，算法优先级从高到底依次为：算法2>算法1>算法0。配置完整性保护算法使用算法1和算法2，优先使用算法2。|SET ENCRYANDINTEG:EA0="EA0SUPPORT",EA0ALGPRIORITY=0,EA1="EA1SUPPORT",EA1ALGPRIORITY=1,EA2="EA2SUPPORT",EA2ALGPRIORITY=2,IA1="IA1SUPPORT",IA1ALGPRIORITY=1,IA2="IA2SUPPORT",IA2ALGPRIORITY=0
调整特性 :使用[SET DEFPRETIMER]命令修改AMF有名定时器时长。
鉴权响应时间对应的有名定时器ID为4，修改时长取值为5000 ms。命令如下：SET DEFPRETIMER:ID=4,VALUE=5000 
等待AUSF鉴权响应时间对应的有名定时器ID为17，修改时长取值为5000 ms。命令如下：SET DEFPRETIMER:ID=17,VALUE=5000 
测试用例 :测试项目|鉴权控制
---|---
测试目的|验证AMF能正确处理鉴权控制。
预置条件|5G网络内的所有网元运行正常，EM连接正常。用户签约5G业务。打开信令跟踪。AMF配置注册/去注册时强制鉴权；设置业务请求时为系统判断。
测试过程|用户分别多次注册到AMF。检查网络侧用户信息和测试信令。
通过准则|AMF对用户每次的注册/去注册都进行鉴权。AMF对用户的业务请求流程不进行鉴权。检查网络侧用户信息和测试信令。信令跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
测试项目|NAS加密和完整性保护
---|---
测试目的|验证AMF能正确处理NAS加密和完整性保护。
预置条件|5G网络内的所有网元运行正常，EM维护正常。用户签约5G业务。打开信令跟踪。AMF配置支持加密算法0、算法1和算法2；支持完整性保持算法1和算法2；优先使用加密算法2和完整性保护算法2。UE支持加密算法2和完整性保护算法2。
测试过程|用户开机发起注册。检查网络侧用户信息和测试信令。
通过准则|AMF发送的Security Mode Command消息中选择的加密算法和完整性算法都为算法2。UE注册成功，业务流程正常。信令跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
常见问题处理 :无 
## ZUF-79-07-002 EAP-AKA'鉴权 
特性描述 :特性描述 :描述 :定义 :EAP-AKA'流程是5GC网络对UE进行鉴权的一种方式，同5G AKA一样，可以实现UE和网络间的双向认证。 
5GC对用户鉴权完成之后，用户才可以注册到5G网络，并通过5G网络访问数据业务和其他业务。 
背景知识 :在GPRS网络（2G）中，网络侧对用户鉴权以防止未经授权的用户接入。但GPRS网络存在一些安全隐患，例如使用的128 bit的密钥容易被破解，不支持数据的完整性保护，难以发现数据被篡改，用户无法对网络进行鉴权。 
UMTS网络（3G）在GPRS网络的基础上进行了改进，采用基于Milenage算法的AKA鉴权，实现了终端和网络间的双向认证，定义了强制的完整性保护和可选的加密保护，提供了更好的安全性保护。 
LTE网络（4G）采用UMTS网络相同的安全架构，也使用AKA鉴权算法，也支持对信令和数据的完整性保护和加密，但NAS信令的完整性保护和加密由MME完成，AS信令的完整性保护和加密由eNodeB完成。
相对4G而言，5G网络在安全性方面进行了以下几个方面的增强： 
通过SUCI方案，解决了以往4G安全协议中，用户号码IMSI在首条明文消息中传递的问题。 
通过鉴权确认机制，解决了漫游场景下拜访网络对于归属网络接入欺骗问题。 
统一了3GPP和non-3GPP鉴权方式，UE和5GC必须支持5G AKA和EPA AKA’两种认证方式。 
应用场景 :当用户触发注册、业务请求或去注册流程时，AMF根据本地配置决策是否为用户提供鉴权服务。若需要进行鉴权，则AMF调用AUSF服务，通知AUSF对UE进行鉴权。
为了达到精细化控制鉴权策略的目的，AMF将注册过程进行了场景细分，并按照细分后的场景分别进行鉴权策略的配置。细分后的业务场景参见[表1]。
业务场景|场景说明
---|---
SUCI初始注册|UE触发初始注册，注册请求消息中携带的用户标识为SUCI。
局内GUTI初始注册|UE曾经在某AMF下注册过，再在该AMF下重新注册，注册请求消息中携带的用户标识为该AMF在上次UE注册时为其分配的临时标识5G GUTI。
RAT内局间GUTI初始注册|UE曾经在AMF1下注册过，然后在AMF2下重新注册，注册请求消息中携带的用户标识为上次注册时AMF1为其分配的临时标识5G GUTI。
RAT间GUTI初始注册|UE曾经在4G附着过，然后在5G下重新发起初始注册，注册请求消息中携带的用户标识是由4G MME为UE分配的临时标识4G GUTI转化而来的5G GUTI。
周期性注册更新|UE周期性定时器到达，触发注册过程，注册类型为“periodic registration updating”。
局内移动性注册更新|UE已经注册到AMF，位置移动时，比如UE进入一个跟踪区，该跟踪区归属于用户所注册的AMF管理，但不在该AMF为其分配的跟踪区列表中，则UE触发注册类型为“mobility registration updating”的注册过程。
RAT内局间移动性注册更新|UE已经注册到AMF1，位置移动时，比如UE进入一个跟踪区，该跟踪区不归属于用户所注册的AMF1管理，而是归属于AMF2管理，则UE触发注册类型为“mobility registration updating”的注册过程到AMF2。
RAT间局间移动性注册更新|UE已经在4G网络附着，位置移动到5G跟踪区下，或者用户打完VoLTE电话后根据自身配置需要再次回到5G网络，则UE触发注册类型为“mobility registration updating”的注册过程到AMF。
局内切换后移动性注册更新|用户已经注册到AMF并且处于连接态，由于位置移动从一个5G基站切换到另一个5G基站，切换前后两个5G基站均归属于用户所注册的AMF管理。切换成功后，UE进入一个跟踪区，该跟踪区归属于用户所注册的AMF管理，但不在该AMF为其分配的跟踪区列表中，则UE触发注册类型为“mobility registration updating”的注册过程。
RAT内局间切换后移动性注册更新|用户已经注册到AMF1并且处于连接态，由于位置移动从一个5G基站切换到另一个5G基站，切换目标5G基站归属另外一个AMF2管理。切换成功后，UE进入一个跟踪区，该跟踪区并不归属于用户所注册的AMF1管理，而是归属于AMF2管理，则UE触发注册类型为“mobility registration updating”的注册过程到AMF2。
RAT间局间切换后移动性注册更新|用户已经注册到4G网络并且处于连接态，由于位置移动从一个4G基站切换到一个5G基站，切换成功后，UE触发注册类型为“mobility registration updating”的注册过程到AMF。
业务请求|-
去注册请求|-
鉴权策略的详细说明参见[表2]。
鉴权策略|详细说明
---|---
强制鉴权|慎重选用该策略。该鉴权策略会导致对应的业务流程每执行一次就触发一次鉴权。当用户业务流程的流量较大时，会加重网络负担。
强制不鉴权|5GC关注网络安全和用户隐私保护，不推荐使用该策略。
系统判断|由系统判断是否需要进行鉴权。AMF检测到UE和AMF之间没有安全环境或安全环境被破坏，则AMF自动触发对UE鉴权，以建立新的安全环境，保障后续的信令消息在可靠的安全环境中传输。
客户收益 :受益方|受益描述
---|---
运营商|拒绝非法用户接入，防止用户相关数据被窃听和篡改。
移动用户|避免使用到非法或损害用户利益的网络。
实现原理 :系统架构 :5GC组网架构如[图1]所示。
图1  5GC系统架构

涉及的网元 :网元名称|网元作用
---|---
UE|对网络进行鉴权。
RAN|RAN透传UE和核心网之间的鉴权信令。
AMF|AMF判定是否对用户进行鉴权，在UE和AUSF之间传递EAP-AKA‘鉴权信令。
AUSF|AUSF向UDM请求鉴权向量和鉴权方式（EAP-AKA’或5G AKA），执行与UE之间的EAP-AKA'鉴权流程。
UDM|UDM生成用户的鉴权向量，根据配置或用户签约确定鉴权方式为EAP-AKA'。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N12|ZUF-79-19-005 N12
本网元实现 :对于EAP-AKA‘鉴权流程，本网元支持如下功能： 
根据本地配置以及用户当前安全校验状态，判定是否针对用户触发鉴权。 
当判定需要鉴权时，调用AUSF服务，通知其对用户进行鉴权。 
执行在UE和AUSF之间传递EAP-AKA’鉴权信令。 
当AUSF通知AMF EAP-AKA‘鉴权成功时，根据AUSF返回的KSEAF推演KAMF秘钥。 
业务流程 :EAP-AKA'认证方式中，网络侧鉴权功能由AUSF负责，AMF只参与AUSF和UE之间鉴权信息的传递，以及最终KAMF密钥的推演。完整的EAP-AKA‘认证流程如[图2]所示。
图2  EAP-AKA‘认证流程

流程说明： 
UE触发注册、业务请求，或去注册请求等流程，发送NAS请求消息给AMF，消息中携带5G GUTI或SUCI。 
如果NAS请求消息中携带5G GUTI，但根据5G GUTI查找用户上下文失败，则AMF向UE发送Identity Request消息，请求用户标识。 
UE向AMF返回Identity Response，消息中携带SUCI。 
AMF根据当前业务类型匹配到的本地鉴权策略配置以及NAS请求消息校验结果，判断是否启用鉴权过程。若需要启动鉴权流程，则AMF发送Nausf_UEAuthentication_Authenticate Request消息给AUSF，携带SUCI或SUPI，以及服务网络名称。 
AUSF发送Nudm_Authentication_Get Request消息给UDM，携带SUCI或SUPI，以及服务网络名称。 
如果请求消息中携带SUCI，UDM解密SUCI后得到SUPI。UDM根据用户签约或者本地配置，确定鉴权方式为EAP-AKA’。 
UDM生成EAP-AKA' AV，包含RAND、AUTN、XRES、CK'、IK'。UDM发送Nudm_Authentication_Get Response消息给AUSF，消息中携带鉴权参数，同时指示选择的认证方式为EAP-AKA'。另外，如果AMF向AUSF发送的Nausf_UEAuthentication_Authenticate Request消息（步骤4）中携带了SUCI，则在UDM返回的响应消息中携带SUPI给AUSF。 
AUSF返回Nausf_UEAuthentication_Authenticate Response消息给AMF，消息中携带EAP Request/AKA' Challenge。 
AMF通过Authentication Request消息将EAP Request/AKA' Challenge参数透传给UE，同时在请求消息中携带ABBA、ngKSI等参数。 
UE校验EAP Request/AKA' Challenge的AUTN，包括MAC、序列号等信息，完成对网络侧的鉴权。校验通过后，计算鉴权响应RES。UE向AMF返回Authentication Response消息，在消息中携带EAP Response/AKA' Challenge。 
AMF通过Nausf_UEAuthentication_Authenticate Request消息透传UE侧的EAP Response/AKA' Challenge给AUSF。 
AUSF校验鉴权响应，完成网络侧对UE的鉴权。校验通过后，AUSF根据CK’和IK‘推演EMSK，并将EMSK的高256比特位作为KAUSF，继续推演得到KSEAF。AUSF向AMF返回Nausf_UEAuthentication_Authenticate Response消息，在消息中携带EAP Success、KSEAF。如果AMF向AUSF发送的Nausf_UEAuthentication_Authenticate Request消息（步骤4）中携带SUCI，则此响应消息中携带SUPI。 
AMF通过N1消息将EAP Success透传给UE，EAP-AKA'鉴权流程完成。 
系统影响 :鉴权策略的不同可能会导致AMF与AUSF/UDM之间信令增加，业务时延增大。 
应用限制 :该特性不涉及应用限制。 
特性交互 :安全流程是基本业务流程，是后续所有的流程的基础。如果选择需要进行安全流程却无法使用，则其他业务都无法使用。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501(System Architecture for the 5G System; Stage 2)|5.10 Security aspects
3GPP TS 23.502(Procedures for the 5G System (5GS);Stage 2)|4.2.2.2Registration procedures4.2.2.3Deregistration procedures4.2.3 Service Request procedures4.6 Security procedures
3GPP TS 33.501(Security Architecture and Procedures for 5G System)|6.1.2 Initiation of authentication and selection of authentication method6.1.3.1 Authentication procedure for EAP-AKA'
3GPP TS 24.501(Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3)|5.4.1.2 EAP based primary authentication and key agreement procedure8.2.1 Authentication request8.2.2 Authentication response8.2.3 Authentication result
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|RAN|AMF|AUSF|UDM
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :网络需要规划好鉴权策略。 
O&M相关 :命令 :新增配置项参见下表。 
配置项|命令
---|---
缺省鉴权策略配置|SHOW DEFAUTHSTRATEGY
SET DEFAUTHSTRATEGY|缺省鉴权策略配置
基于SUPI号段的鉴权策略配置|ADD SUPIAUTHSTRATEGY
SET SUPIAUTHSTRATEGY|基于SUPI号段的鉴权策略配置
DEL SUPIAUTHSTRATEGY|基于SUPI号段的鉴权策略配置
SHOW SUPIAUTHSTRATEGY|基于SUPI号段的鉴权策略配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :本配置用于实现5G鉴权过程。AMF根据业务种类和配置策略启用对用户鉴权过程。 
鉴权策略包括： 
强制鉴权：不管用户是否为合法用户，都做鉴权过程。 
系统判断：根据实际情况判断用户是否需要做鉴权过程。 
强制不鉴权：不管用户是否为合法用户，都不做鉴权过程，允许用户接入。 
配置前提 :AMF运行正常。 
EM网管能正常连接。 
配置过程 :使用[SET DEFAUTHSTRATEGY]命令，设置缺省的鉴权策略。
配置实例 :场景说明 :运营商要求对5G用户的鉴权策略如下： 
对注册/去注册流程采取强制鉴权方式，对业务请求流程采取系统判断方式。 
数据规划 :无 
配置步骤 :步骤|说明|操作
---|---|---
1|配置对注册/去注册流程采取强制鉴权方式，对业务请求流程采取系统判断方式。|SET DEFAUTHSTRATEGY:SERVICETYPE="SUCIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="INTRAGUTIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="INTERGUTIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="RATGUTIINITREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="DEREG",AUTHSTRATEGY="FORCEAUTH"SET DEFAUTHSTRATEGY:SERVICETYPE="SERVICEREQ",AUTHSTRATEGY="SYSTEMDEFINE"
调整特性 :使用[SET DEFPRETIMER]命令修改AMF有名定时器时长。
等待UE鉴权响应时间对应的有名定时器ID为4，修改时长取值为5000 ms。命令如下：SET DEFPRETIMER:ID=4,VALUE=5000 
等待AUSF鉴权响应时间对应的有名定时器ID为17，修改时长取值为5000 ms。命令如下：SET DEFPRETIMER:ID=17,VALUE=5000 
测试用例 :测试项目|鉴权控制
---|---
测试目的|验证AMF能正确处理EAP-AKA'鉴权流程。
预置条件|5G网络内的所有网元运行正常，EM连接正常。用户签约5G业务。打开信令跟踪。AMF配置注册/去注册时，鉴权策略为强制鉴权；设置业务请求时，鉴权策略为系统判断。
测试过程|用户分别多次注册到AMF。检查网络侧用户信息和测试信令。
通过准则|AMF对用户每次的注册/去注册都进行鉴权。AMF对用户的业务请求流程不进行鉴权。检查网络侧用户信息和测试信令。信令跟踪能够跟踪到相应的消息，流程正确。
测试结果|–
常见问题处理 :无 
## ZUF-79-07-003 秘钥派生与传递 
概述 :鉴权成功后，根据鉴权矢量中的IK和CK，5GC派生NAS和AS使用的加解密秘钥和完整性保护秘钥。 
客户收益 :保证5G网络安全，禁止未授权用户接入5G网络。 
说明 :5GS中，秘钥分级生成如下图所示。 
图1  5GS中秘钥分级生成

鉴权相关的秘钥包括：K, CK/IK。EAP-AKA’时，秘钥CK’和IK’来自CK和IK。 
秘钥等级结构包括如下秘钥：KAUSF、KSEAF、KAMF、K、KNASint、KNASenc、KgNB、KRRCint、KRRCenc、KUPint和KUPenc。
AMF的秘钥： 
KAMF是由ME和SEAF从KSEAF派生出的秘钥。KAMF由ME和源AMF在进行水平秘钥派生时进一步推导。
网络节点5G秘钥传递和派生方案如下图所示。 
图2  5G秘钥传递和派生方案

AMF从SEAF或其他AMF接收KAMF。
AMF应从KAMF派生出一个秘钥K'AMF，用于在AMF间移动性中传递给另一个AMF。接收方AMF应使用K'AMF作为其KAMF。
AMF应生成用于保护NAS层的秘钥KNASint和KNASint。
AMF应从KAMF生成针对接入网的秘钥。
特别地， 
AMF应生成KgNB并传递给gNB。 
AMF应生成NH并随相应的NCC值一起传递给gNB。AMF也可能将NH秘钥连同对应的NCC值传递给另一个AMF。 
详见3GPPP 33.501中6.2节“秘钥派生与传递方案”。 
## ZUF-79-07-004 AS算法选择 
概述 :AS算法选择用于RRC级安全。 
客户收益 :AS算法选择使RRC级安全得到加密和完整性保护。 
说明 :在5G网络中，AMF提供UE支持的AS加解密和完整性算法信息，帮助基站选择AS安全算法。 
AMF支持UE的AS加解密算法如下： 
NEA0（非加密） 
NEA1（SNOW 3G算法） 
NEA2（AES算法） 
NEA3（ZUC算法） 
AMF支持UE的AS完整性保护算法如下： 
NEA0（非加密） 
NEA1（SNOW 3G算法） 
NEA2（AES算法） 
NEA3（ZUC算法） 
## ZUF-79-07-005 NAS信令加密 
概述 :UE和AMF之间的NAS消息应该加密保护。 
客户收益 :NAS信令的加密保护可以保证NAS消息的安全性。 
说明 :在5G网络中，AMF为NAS信令提供加解密功能。AMF支持如下加密算法： 
NEA0（非加密） 
NEA1（SNOW 3G算法） 
NEA2（AES算法） 
NEA3（ZUC算法） 
这些算法的优先级可以在AMF中配置。优先采用优先级高的算法。 
AMF根据UE支持的加密算法与AMF支持的算法的交集选择要使用的算法。 
详见3GPP33.501中6.4.4节“NAS保密机制”。 
## ZUF-79-07-006 NAS信令完整性保护 
概述 :AMF为NAS数据块提供完整性保护。 
客户收益 :NAS信令的完整性保护可以保证NAS消息的安全性。 
说明 :在5G网络中，AMF为NAS信令提供完整性保护业务。AMF支持如下完整性保护算法 
NIA1（SNOW 3G算法） 
NIA2（AES算法） 
NIA3（ZUC算法） 
这些算法的优先级可以在AMF中配置。优先采用优先级高的算法。 
AMF根据UE支持的完整性保护算法和AMF支持的算法的交集选择要使用的算法。 
详见3GPP33.501中6.4.3节“NAS完整性机制”。 
## ZUF-79-07-007 4/5G互操作安全上下文映射 
概述 :当UE在4G和5G之间移动时，5G安全秘钥KAMF和4G安全秘钥KASME需要迁移。 
客户收益 :UE在5G和4G之间移动是一项基本功能。 
说明 :从EPS安全派生出一个映射的5G安全上下文的方法如下： 
作为秘钥KAMF、秘钥KAMF’应使用空闲模式移动时的当前EPS NAS
Uplink COUNT值或切换时的NH值从秘钥KASME派生出来。 
新派生的秘钥KAMF的ngKSI应这样定义，比如取值字段取自eKSI，类型字段设置为表示映射的安全上下文。 
映射的5G安全上下文中的5G NAS COUNT值应设置为0。 
5G NAS算法选择由AMF进行，切换时在NAS Container中指示UE，或空闲模式移动时在NAS SMC中指示UE。 
从5G安全上下文派生出映射的EPS安全上下文的方法如下： 
作为秘钥KASME、秘钥KASME’应使用空闲模式移动时的当前EPS NAS
Uplink COUNT值或或切换时的5G NAS Downlink COUNT值从秘钥KAMF派生出来。 
新派生的秘钥KASME的eKSI应这样定义，比如，取值字段取自ngKSI，类型字段设置为表示映射的安全上下文。 
映射上下文中的EPS NAS COUNT值应设置为5G上下文中的COUNT值。 
所选择的EPS NAS算法应设置为发送NAS SMC前早期鉴权过程中AMF向UE指示的EPS算法。 
当需要改变算法时，目标MME发起NAS SMC来选择其他算法。 
## ZUF-79-07-008 加密用户标识SUCI 
概述 :加密用户标识SUCI是一个隐私保护标识，包含加密的SUPI，防止SUPI在空口以明文传输。AMF将加密的SUCI路由到UDM，UDM解密该SUCI并转发解密的SUPI给AMF。 
客户收益 :SUCI用于支持用户身份保密，增强用户的安全性。 
说明 :在5G系统中，全球唯一5G签约永久标识称为SUPI。SUCI是一个隐私保护标识，包含加密的SUPI。SUPI是通过SUCI实现空中传输隐私保护的。 
UE使用含有原始公钥的保护方案生成SUCI，该原始公钥用于可靠地控制归属网络。保护方案应为附录C规定的保护方案或HPLMN规定的保护方案。 
UE应根据保护方案的规定，从SUPI的签约标识部分构造方案输入物（scheme-input）。UE输入方案输入物执行保护方案，并将输出作为方案输入物（scheme-output）。 
UE不应隐藏归属网络标识，如，移动国家码（MCC），或移动网络码（MNC）。 
UE应使用以下数据域构造SUCI： 
保护方案标识，表示附件C规定的保护方案或HPLMN规定的保护方案。 
归属网络公钥标识，表示HPLMN提供的公钥。如果使用空方案，该数据字段应设置为空。 
归属网络标识。 
方案输出物。 
UE只需要在以下5G NAS消息中携带SUCI。 
如果UE向PLMN发送的初始注册类型的Registration Request消息不包含5G-GUTI，UE应该在Registration Request消息中携带SUCI，或者 
如果UE向PLMN发送的刷新注册类型的Registration Request消息包含5G-GUTI，并且UE收到Identity Request消息，UE应在Identity Response消息携带一个新的SUCI。 
只有在以下情况下，UE才需要使用空方案(null-scheme)生成SUCI。 
如果UE正在进行未认证的紧急会话，并且没有发送5G-GUTI到所选的PLMN，或者 
如果归属网络已经配置了空方案，或者 
如果归属网络没有提供生成SUCI所需的公钥。 
详见3GPP 33.501中的6.12.2节“加密用户标识”。 
## ZUF-79-07-009 初始NAS消息保护 


概述 :由于初始NAS消息无法加密，5GC采用以下方式防止初始NAS消息中的用户敏感信息泄露：如果存在安全上下文，5GC加密包含敏感和非敏感信息在内的整个NAS消息，然后通过NAS容器发送到AMF。如果没有安全上下文，则在建立安全连接时，5GC把包含敏感和非敏感信息在内的整个NAS请求消息将通过NAS容器以未加密的安全模式完成（Security
Mode Complete）消息直接传发送到AMF。 


客户收益 :初始NAS保护可防止UE在CM-IDLE状态下触发初始NAS消息。因为初始NAS消息无法加密，UE可能泄漏消息中包含的用户敏感信息。 


说明 :5GS遵循3GPPTS33.501 [24]支持初始NAS消息保护。初始NAS消息保护适用于注册请求（
REGISTRATION REQUEST ）和服务请求（SERVICE REQUEST）。实现方式如下： 

 
如果UE没有有效的5G NAS安全上下文，UE发送仅包含明文信元的注册请求消息。如果在安全模式控制流程中激活了5G NAS安全上下文：
如果UE需要发送非明文信元，则UE应发送NAS层的注册请求完整消息（包含明文和非明文信元），并发送NAS层的安全模式完成消息。
如果UE不需要发送非明文信元，则UE应发送NAS层的注册请求完整消息（仅包含明文信元），并发送NAS层的安全模式完成消息。
 

 
如果UE具有有效的5G NAS安全上下文，并且需要通过注册请求或服务请求消息发送非明文信元，则UE需要对NAS消息容器信元的值进行加密，并把NAS消息容器信元包含在注册请求或服务请求消息（包含明文和非明文信元）中进行发送。 

 
如果初始NAS消息是注册请求消息，明文信元包括： 

 
Extended protocol discriminator 

 
Security header type 

 
Spare half octet 

 
Registration request message identity 

 
5GS registration type 

 
ngKSI 

 
5GS mobile identity 

 
UE security capability 

 
Additional GUTI 

 
UE status 

 
EPS NAS message container 

 
如果初始NAS消息是服务请求消息，明文信元包括： 

 
Extended protocol discriminator 

 
Security header type 

 
Spare half octet 

 
ngKSI 

 
Service request message identity 

 
Service type 

 
5G-S-TMSI 

 
UE发送包含NAS消息容器信元的注册请求或服务请求消息时，UE应将初始NAS消息的security header type设置为“完整性保护”。 
如果UE不需要通过初始NAS消息发送非明文信元，UE应发送只包含明文信息元的注册请求或服务请求，即初始NAS消息中不包含NAS消息容器信息元。 
如果AMF收到完整性受保护的初始NAS消息即包含NAS消息容器信元，AMF会对NAS消息容器信元解密。AMF认为从NAS消息容器信元获得的NAS消息是触发流程的初始NAS消息。 
如果初始NAS消息是注销请求消息，UE发送的NAS消息一般不加密。 


## ZUF-79-07-010 PEI检查 
特性描述 :特性描述 :术语 :术语|含义
---|---
PEI|终端设备永久标识，用于唯一标识一个终端设备。
5G-EIR|5G网络终端设备状态寄存器，存储终端设备状态。
描述 :定义 :PEI检查特性是指用户发起注册流程时，AMF向5G-EIR发起PEI检查以确认终端设备的合法性，从而禁止非法终端进入网络。
背景知识 :用户使用非法终端（如盗窃终端、山寨机终端）接入网络时，一些国家或者运营商希望可以识别这种终端，限制其接入网络。 
这就需要AMF提供PEI检查特性，检查终端设备合法性，限制非法终端接入网络。 
应用场景 :当运营商需要检查用户终端设备合法性时，可以开启本特性。 
客户收益 :受益方|受益描述
---|---
运营商|增加网络安全性，限制非法终端接入网络。
移动用户|限制用户非法权益，保护用户合法权益。
实现原理 :系统架构 :PEI检查的系统架构如[图1]所示。
图1  PEI检查系统架构

涉及的网元 :网元名称|网元作用
---|---
UE|向AMF提供终端设备标识。
5G-EIR|向AMF提供设备标识检查结果。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N17|ZUF-79-19-015 N17
本网元实现 :向UE请求用户设备标识。 
向5G-EIR发起设备标识检查，根据检查结果限制或者放行用户接入。 
业务流程 :PEI检查的流程如[图2]所示。
图2  PEI检查流程
流程说明： 
UE发起注册流程。 
如果流程中有SMC过程，且“AMF是否获取IMEI(SV)”配置为“获取IMEISV”，则AMF通过SMC过程向UE请求IMEISV。 
如果没有通过SMC过程获取IMEISV，“AMF是否获取IMEI(SV)”配置为“获取IMEISV”或者“获取IMEI”，则AMF通过ID请求过程，向UE请求IMEISV或者IMEI。 
AMF根据流程类型判断是否向5G-EIR发起PEI检查，系统默认对初始注册和局间注册更新发起PEI检查，局内注册更新不发起PEI检查。 
如果判决发起PEI检查，AMF向5G-EIR发送N5geir_EquipmentIdentityCheck_GetEquipmentStatus Request消息，请求检查PEI的合法性。该消息中包含PEI，可选的包含用户SUPI、GPSI。 
5G-EIR根据存储的终端设备状态属性，向AMF返回N5geir_EquipmentIdentityCheck_GetEquipmentStatus Response消息。AMF收到5G-EIR的响应后，根据检查结果和本地策略决定是否拒绝用户接入，具体参见下表。 
PEI检查结果|AMF处理策略
---|---
5G-EIR返回黑名单|配置控制，默认拒绝
5G-EIR返回未知设备|配置控制，默认拒绝
5G-EIR返回灰名单|配置控制，默认不拒绝
5G-EIR超时无响应|配置控制，默认不拒绝
5G-EIR返回其他失败|配置控制，默认不拒绝
发现5G-EIR失败|配置控制，默认不拒绝
如果AMF根据PEI检查结果和本地策略决定拒绝用户接入，则给UE发送注册拒绝消息，携带5GMM原因。5GMM原因可根据5G-EIR返回结果进行NAS原因映射配置，默认原因参见下表。 
HTTP status code|Application Error|5GMM cause
---|---|---
200：200 OK|65531：PEI在灰名单中/PEI Is Greylisted|6：6 - Illegal ME
200：200 OK|65532：PEI在黑名单中/PEI Is Blacklisted|6：6 - Illegal ME
404：404 Not Found|XXX：ERROR_EQUIPMENT_UNKNOWN|6：6 - Illegal ME
65531：向UE获取IMEI(SV)失败/IMEI(SV) Get Failed|65534：无关/Not Applicable|111：111 – Protocol error, unspecified
65533：等待HTTP响应超时/Wait HTTP Response Timeout|65534：无关/Not Applicable|111：111 – Protocol error, unspecified
65532：5G-EIR发现失败/5G-EIR Discovery Failed|65534：无关/Not Applicable|111：111 – Protocol error, unspecified
65535：通配/Any HTTP status code|65535：通配/Any Application Error|111：111 – Protocol error, unspecified
如果AMF根据PEI检查结果和本地策略决定放行用户接入，后续流程处理成功，AMF给UE发送注册接受消息。 
系统影响 :AMF增加与5G-EIR交互处理，AMF系统性能会下降。 
网络传输增加了AMF与5G-EIR间的信令流量，网络性能会下降。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.502: "Procedures for the 5G System (5GS)".|4.2.2.2 Registration procedures4.7 ME Identity check procedure
3GPP TS 29.511: "Equipment Identity Register Services".|全部
3GPP TS 23.003: "Numbering, addressing and identification".|6 International Mobile Station Equipment Identity, Software Version Number and Permanent Equipment Identifier
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.40|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。 
对其他网元的要求 :UE|5G-EIR
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令PEI检查配置SET PEICHECKCONFIGSHOW PEICHECKCONFIGNeir 原因值映射配置 ADD NEIRCAUSEMAPPINGCFG SET NEIRCAUSEMAPPINGCFG DEL NEIRCAUSEMAPPINGCFG SHOW NEIRCAUSEMAPPINGCFG默认5G-EIR配置 SET DFT 5G EIR CONFIG SHOW DFT 5G EIR CONFIG表2  修改配置项配置项命令新增参数NF发现模式配置SET NFDISCOVERYMODE CONFIG增加"5G-EIR发现模式"字段,默认记录增加对应字段。紧急业务策略配置SET EMERGSRVPLY取消隐藏的两个参数"紧急注册检查PEI"、"PEI检查失败放行紧急业务"。增加 "向UE获取IMEI(SV)失败限制接入时放行紧急业务"字段。SHOW EMERGSRVPLYCommunication定时器配置SET DEFPRETIMER增加默认记录：AMF等待5G-EIR响应定时器时长(46）。SHOW DEFPRETIMERSBI出向业务容量配置ADD OLOUTPUTSBISRVCFG"业务类型" 增加枚举值：5 PEICHECK。SET OLOUTPUTSBISRVCFGDEL OLOUTPUTSBISRVCFGSHOW OLOUTPUTSBISRVCFGEMS+功能开关配置SET AMFCHRFUNC
"上报特殊日志功能开关"复选框增加“上报PEI黑名单日志”、“上报PEI灰名单日志”及”上报PEI未知设备日志”三个类型。SHOW AMFCHRFUNC 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
性能统计 :测量类型|描述
---|---
N17接口测量|新增编号为51062开头的所有计数器
Communication服务负荷控制测量|新增C510280048 由于SBI口出向过负荷控制而丢弃的发向5G-EIR的请求个数
告警和通知 :告警和通知
---
2114060544 灰/黑名单用户告警通知
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置过程，运营商可以达到检查用户终端设备合法性的目的。 
配置前提 :AMF环境运行正常。 
EM网管能正常连接并登录。 
与5G-EIR之间链路状态正常。 
配置过程 :执行[SET PEICHECKCONFIG]命令，设置AMF是否支持PEI检查、初始注册等各个流程是否进行PEI检查、AMF给EIR携带的参数、是否限制灰\黑名单\未知设备接入、是否发送用户灰/黑名单状态告警通知等配置项，以便灵活地控制PEI检查过程。可执行[SHOW PEICHECKCONFIG]命令，查询PEI检查配置信息。
执行[ADD NEIRCAUSEMAPPINGCFG]命令，新增Neir原因值映射配置，制定个性化的“HTTP状态码+应用层错误码”到“5GMM原因值+计数归类”的映射配置。可执行[SHOW NEIRCAUSEMAPPINGCFG]命令，查询默认的Neir原因值映射配置。
（可选）执行[SET DFT 5G EIR CONFIG]命令，设置本地发现EIR时使用的5G-EIR的IP地址、端口号等。可执行[SHOW DFT 5G EIR CONFIG]命令，查询默认5G-EIR配置。
执行[SET NFDISCOVERYMODE CONFIG]命令，修改5G-EIR的发现模式。可执行[SHOW NFDISCOVERYMODE CONFIG]命令，查询5G-EIR发现模式，默认“通过NRF发现NF”。
执行[SET EMERGSRVPLY]命令，设置紧急业务策略。可执行[SHOW EMERGSRVPLY]命令，查询紧急用户PEI检查相关策略配置。
执行[SET DEFPRETIMER]命令，修改AMF有名定时器时长配置。可执行[SHOW DEFPRETIMER]命令，查询"AMF等待5G-EIR响应定时器时长“配置。
（可选）执行[ADD OLOUTPUTSBISRVCFG]命令，增加”业务类型“为 PEI检查类型的SBI出向业务配置。可执行[SHOW OLOUTPUTSBISRVCFG]命令，查询SBI出向业务配置。
（可选）执行[SET AMFCHRFUNC]命令， 在"上报特殊日志功能开关”复选框中，根据需要选择勾选“上报PEI黑名单日志”、“上报PEI灰名单日志”、”上报PEI未知设备日志”。可执行[SHOW AMFCHRFUNC]命令，查询EMS+上报功能配置。
（可选）执行[SET AMFMOBCFG]命令，修改AMF移动性配置。可执行[SHOW AMFMOBCFG]命令， 了解"是否获取IMEI(SV)"的当前取值。此配置参数会影响UE侧安全模式及ID请求流程，也会影响PEI检查带给EIR的参数。
配置实例 :###### 初始注册PEI检查 
场景说明
用户初始注册，在获取签约数据前进行PEI检查，本地解析EIR，携带SUPI、IMEISV给EIR，EIR回复响应“黑名单”，注册成功，上报用户黑名单状态告警通知，上报接收N5g-eir响应（黑名单）性能统计。 
数据规划
配置名称|参数项|取值
---|---|---
PEI检查配置|AMF是否支持PEI检查|支持
初始注册流程是否进行PEI检查|PEI检查配置|是
AMF携带IMEI还是IMEISV给EIR|PEI检查配置|携带IMEISV
AMF是否携带SUPI给EIR|PEI检查配置|携带
AMF是否携GPSI给EIR|PEI检查配置|携带
AMF是否在获取签约数据之后进行PEI检查|PEI检查配置|否
AMF是否限制黑名单设备接入|PEI检查配置|否
AMF是否发送用户灰/黑名单状态告警通知|PEI检查配置|发送黑名单告警
Neir 原因值映射配置|HTTP状态码|404 Not Found
应用层错误码|Neir 原因值映射配置|USER_NOT_FOUND
5GMM 原因值|Neir 原因值映射配置|6 - Illegal ME
计数归类|Neir 原因值映射配置|27
默认5G-EIR配置|是否启用|启用
IP地址|默认5G-EIR配置|192.168.100.17
端口号|默认5G-EIR配置|8080
URI scheme|默认5G-EIR配置|HTTPS
API版本|默认5G-EIR配置|V1
NF发现模式配置|5G-EIR发现模式|通过本地配置发现NF
紧急业务策略配置|紧急注册检查PEI|是
PEI检查失败放行紧急业务|紧急业务策略配置|是
向UE获取IMEI(SV)失败限制接入时放行紧急业务|紧急业务策略配置|否
SBI出向业务容量配置|业务类型|PEI检查
SBI口出向业务每秒每实例最大通过量|SBI出向业务容量配置|1000
EMS+功能开关配置|功能开关|特殊日志
上报特殊日志功能开关|EMS+功能开关配置|上报PEI黑名单日志、上报PEI灰名单日志、上报PEI未知设备日志
Communication定时器配置|ID|46
当前时长(ms)|Communication定时器配置|3500
数据配置
步骤|说明|操作
---|---|---
1|设置PEI检查配置。|SET PEICHECKCONFIG:SUPPORT="SUPPORT_YES",CHKINITREG="INITREG_YES",CARRYIMEISV="CARRYIMEISV",CARRYSUPI="CARRYSUPI_YES",CARRYGPSI="CARRYGPSI_YES",CHKAFTERSUBDATA="AFTERSUBDATA_NO",LIMITBLACK="BLACKLIST_NO",SENDSTATEALARM="ONLY_BLACK"
2|新增Neir 原因值映射配置。|ADD NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_404",APPLICATIONERROR="USER_NOT_FOUND",EIRMMCAUSE="ILLEGALME",COUNTER=27
3|修改默认5G-EIR配置。|SET DFT 5G EIR CONFIG:ENABLE="ENABLE",IPADDRESS="192.168.100.17",PORT=8080,URISCHEMA="HTTPS",APIVERSION="V1"
4|修改EIR发现模式配置。|SET NFDISCOVERYMODE CONFIG:DISCOVERYEIRMODE="DiscNfByLocal"
5|设置紧急业务策略PEI检查相关配置。|SET EMERGSRVPLY:PEICHECKEMERGREGIST="YES",PASSPEICHECKFAIL="YES",PASSPEIGETFAIL="NO"
6|增加业务类型为"PEI检查"的SBI出向业务容量配置。|ADD OLOUTPUTSBISRVCFG:SRVTYPE="PEICHECK",OLMAXNUM=1000
7|设置PEI检查上报特殊日志功能开关。|SET AMFCHRFUNC:FLG="SPECIAL",SPECIALFUNCFLG="PEI_BLACK_LIST"&"PEI_GRAY_LIST"&"PEI_UNKNOWN_EQUIPMENT"
8|设置AMF等待5G-EIR响应定时器时长。|SET DEFPRETIMER:ID=46,VALUE=3500
###### 紧急注册PEI检查 
场景说明
用户紧急注册，在获取签约数据后进行PEI检查，向NRF发现EIR，携带SUPI、IMEI、GPSI给EIR，EIR回复失败响应，EIR返回失败时AMF限制接入，但PEI检查限制接入时放行紧急业务，紧急注册成功，上报接收N5g-eir失败响应性能统计。 
数据规划
配置名称|参数项|取值
---|---|---
PEI检查配置|AMF是否支持PEI检查|支持
初始注册流程是否进行PEI检查|PEI检查配置|是
AMF携带IMEI还是IMEISV给EIR|PEI检查配置|携带IMEI
AMF是否携带SUPI给EIR|PEI检查配置|携带
AMF是否携GPSI给EIR|PEI检查配置|携带
AMF是否在获取签约数据之后进行PEI检查|PEI检查配置|是
EIR返回失败时AMF是否限制接入|PEI检查配置|是
Neir 原因值映射配置|HTTP状态码|404 Not Found
应用层错误码|Neir 原因值映射配置|USER_NOT_FOUND
5GMM 原因值|Neir 原因值映射配置|6 - Illegal ME
计数归类|Neir 原因值映射配置|27
默认5G-EIR配置|是否启用|启用
IP地址|默认5G-EIR配置|192.168.100.17
端口号|默认5G-EIR配置|8080
URI scheme|默认5G-EIR配置|HTTPS
API版本|默认5G-EIR配置|V1
NF发现模式配置|5G-EIR发现模式|通过NRF发现NF
紧急业务策略配置|紧急注册检查PEI|是
PEI检查失败放行紧急业务|紧急业务策略配置|是
向UE获取IMEI(SV)失败限制接入时放行紧急业务|紧急业务策略配置|否
SBI出向业务容量配置|业务类型|PEI检查
SBI口出向业务每秒每实例最大通过量|SBI出向业务容量配置|1000
EMS+功能开关配置|功能开关|特殊日志
上报特殊日志功能开关|EMS+功能开关配置|上报PEI黑名单日志、上报PEI灰名单日志、上报PEI未知设备日志
Communication定时器配置|ID|46
当前时长(ms)|Communication定时器配置|3500
数据配置
步骤|说明|操作
---|---|---
1|设置PEI检查配置。|SET PEICHECKCONFIG:SUPPORT="SUPPORT_YES",CHKINITREG="INITREG_YES",CARRYIMEISV="CARRYIMEI",CARRYSUPI="CARRYSUPI_YES",CARRYGPSI="CARRYGPSI_YES",CHKAFTERSUBDATA="AFTERSUBDATA_YES",LIMITEIRRETURNFAIL="EIRRETFAIL_YES"
2|新增Neir 原因值映射配置。|ADD NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_404",APPLICATIONERROR="USER_NOT_FOUND",EIRMMCAUSE="ILLEGALME",COUNTER=27
3|修改默认5G-EIR配置。|SET DFT 5G EIR CONFIG:ENABLE="ENABLE",IPADDRESS="192.168.100.17",PORT=8080,URISCHEMA="HTTPS",APIVERSION="V1"
4|修改EIR发现模式配置。|SET NFDISCOVERYMODE CONFIG:DISCOVERYEIRMODE="DiscNfByNrf"
5|设置紧急业务策略PEI检查相关配置。|SET EMERGSRVPLY:PEICHECKEMERGREGIST="YES",PASSPEICHECKFAIL="YES",PASSPEIGETFAIL="NO"
6|增加业务类型为"PEI检查"的SBI出向业务容量配置。|ADD OLOUTPUTSBISRVCFG:SRVTYPE="PEICHECK",OLMAXNUM=1000
7|设置PEI检查上报特殊日志功能开关。|SET AMFCHRFUNC:FLG="SPECIAL",SPECIALFUNCFLG="PEI_BLACK_LIST"&"PEI_GRAY_LIST"&"PEI_UNKNOWN_EQUIPMENT"
8|设置AMF等待5G-EIR响应定时器时长。|SET DEFPRETIMER:ID=46,VALUE=3500
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|初始注册PEI检查
---|---
测试目的|初始注册可以正确进行用户设备检查。
预置条件|AMF环境运行正常。与EIR之间的链路状态正常。已按配置实例中的相应场景的执行步骤完成EM上的配置。AMF license及配置支持EMS+上报。
测试过程|用户初始注册。
通过准则|向UDM获取签约数据前，读取默认5G-EIR配置的IP地址和端口号等信息，本地解析5G-EIR。AMF向5G-EIR发送PEI检查请求消息，携带IMEISV、SUPI(因尚未获取签约，无GPSI，故不携带)。5G-EIR回复成功响应，显示Status-BlackList。流程继续，注册成功。在EM告警中，有2114060544 灰/黑名单用户告警通知上报。计数器C510620006 接收N5g-eir_EquipmentIdentityCheck_Get响应次数（黑名单）中会上报一次数据。上报用户黑名单的EMS+特殊日志 。
测试结果|–
测试项目|紧急用户PEI检查
---|---
测试目的|紧急注册进行用户设备检查，响应失败后可以通过配置开关放行。
预置条件|AMF环境运行正常。与EIR之间的链路状态正常。已按配置实例中的相应场景的执行步骤完成EM上的配置。
测试过程|用户紧急注册。
通过准则|向UDM获取签约数据后，向NRF发现5G-EIR。AMF向5G-EIR发送PEI检查请求消息，携带IMEI、SUPI、GPSI。5G-EIR回复失败响应，httpRspCode-404，应用错误USER_NOT_FOUND。紧急注册流程继续，注册成功。计数器C510620003 接收N5g-eir_EquipmentIdentityCheck_Get失败响应次数中会上报一次数据。
测试结果|–
常见问题处理 :无 
# 缩略语 
# 缩略语 
## AKA 
Authentication and Key Agreement鉴权和密钥协商
AMF :Access and Mobility Management Function接入和移动管理功能
AUSF :Authentication Server Function鉴权服务器功能
EIR :Equipment Identity Register设备标识寄存器
GUTI :Globally Unique Temporary Identity全球唯一临时标识
NAS :Network Access Service网络接入服务
## PEI 
Permanent Equipment Identifier永久设备标识
RAN :Radio Access Network无线接入网
## SUCI 
Subscription Concealed Identifier签约的隐藏标识符
Subscription Concealed Identifier用户匿名标识
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
# ZUF-79-08 消息透明路由 
## ZUF-79-08-003 UE Policy透明路由 
特性描述 :特性描述 :术语 :术语|含义
---|---
UE Policy|UE策略，包含URSP和ANDSP。
ANDSP|接入网发现和选择策略，用于辅助UE在non-3GPP下的选网。
URSP|UE路由选择策略，用于用户业务数据流的PDU Session选择。
描述 :定义 :PCF可以为UE订制URSP等UE Policy，AMF在UE和PCF之间透传UE Policy。
用户注册时，AMF为UE建立与PCF间的UE Policy连接。PCF在UE Policy连接建立后，通过AMF，把UE Policy投递给UE。 
背景知识 :在2G/3G/4G时，UE上业务流使用的路由策略，是通过例如OTA配置、UE上直接写入、用户直接在终端上设置参数（如设置流媒体的APN等）等方式控制的。如果要新增一种应用，修改手机侧的路由策略，非常不灵活。 
5G网络引入切片、SSC模式、统一3GPP和non-3GPP后，UE上对业务流的路由选择策略更加复杂，一方面非专业为用户很难修改，通过在USIM卡预先写入（但已放号的USIM卡无法写）或其他非标准方式实现UE路由选择策略的修改，代价大。另一方面因为引入切片等，和4G相比修改频度会增加。
因此由网络侧灵活地更改用户路由策略的手段，将更加便于业务创新和网络维护。 
应用场景 :###### 场景一：URSP 
用户接入5G网络，PCF通过AMF给UE提供URSP，用于用户数据的路由选择。 
###### 场景二：ANDSP 
用户接入5G网络，PCF通过AMF给UE提供ANDSP，用于用户非3GPP接入时的选网。 
客户收益 :受益方|受益描述
---|---
运营商|便于业务创新：引入新业务更简单，新业务上线周期更短，成本更低。提高用户满意度：根据网络状况，灵活的调整UE侧的配置，提升用户体验。
移动用户|满足用户的多样业务需求，提升终端用户体验。
实现原理 :系统架构 :本特性涉及的系统架构如下图所示。 
图1  UE Policy架构图

涉及的网元 :NF|网元作用
---|---
UE|支持5G接入的终端，PCF通过AMF把UE Policy提供给UE后，UE使用UE Policy，如根据URSP选择对应业务流的PDU Session，根据ANDSP选择对应non-3GPP下的PLMN。
AMF|向PCF提供UE接入信息，从PCF获取UE Policy后，透传给UE。
PCF|用户策略控制NF，UE向5G注册后通过AMF向UE提供UE Policy等数据。
UDR|向PCF提供用户的策略签约信息，并允许PCF将动态生成的UE Policy数据保存在UDR中。
业务流程 :初始注册过程
初始注册流程中UE Policy的处理如下图所示。 
图2  初始注册过程中的UE Policy处理

流程说明如下： 
UE检测到需发起注册流程，则向AMF发送注册请求，消息中可能携带UE Policy Container（UE STATE INDICATION including UPSI list）。 
AMF收到UE的注册请求消息，正常处理，直到向UE发送注册接受消息。 
AMF向UE发送注册接受消息。 
AMF给UE发送了注册接受消息后，向PCF发起UE Policy Association建立过程。AMF给PCF发送Npcf_UEPolicyControl Create Request消息，携带SUPI, Access Type and RAT、 PEI、ULI、UE time zone、Serving Network、UE Policy Container （UE STATE INDICATION including UPSI list）等信息。 
UE向AMF返回注册接受完成消息。 
PCF向UDR获取用户签约数据，并向UDR订阅签约数据改变事件。 
PCF根据用户签约数据、本地策略等，决策UE Policy。 
PCF给AMF返回Npcf_UEPolicyControl Create Response消息。 
PCF给AMF发送Namf_Communication_N1N2MessageSubscribe Request消息，携带后续AMF透传UE的UE Policy Container给PCF需使用的URI。AMF给PCF返回Namf_Communication_N1N2MessageSubscribe Response消息。 
PCF构造Manage UE policy command消息，携带URSP等UE Policy信息。PCF给AMF发送Namf_ Communication_N1N2MessageTransfer Request消息，消息中携带Manage UE policy command消息。AMF给PCF返回Namf_ Communication_N1N2MessageTransfer Response消息。PCF给UE发送DL NAS Transport消息，消息中携带Manage UE policy command消息。 
UE保存URSP信息。 
UE构造Manage UE policy Complete消息，向PCF确认已收到UE Policy信息。UE向AMF发送UL NAS Transport消息，消息中携带Manage UE policy Complete消息。AMF向PCF发送Namf_Communication_N1MessageNotify Request消息，携带Manage UE policy Complete消息。PCF向AMF返回Namf_Communication_N1MessageNotify Response消息。 
PCF重复第9步到第11步，直到把所有UE Policy下发给UE了。 
PCF给UDR发送Nudr_DataRepository_Update Request消息，把相关UE Policy信息保存到UDR中。UDR返回Nudr_DataRepository_Update Response消息。 
AMF发起的UE Policy关联修改
事件订阅触发时，AMF发起的UE Policy关联修改的处理如下图所示。 
图3  AMF触发的UE Policy关联更新

流程说明如下： 
AMF检测到用户订阅事件，则AMF确定发起UE Policy Association更新过程。 
AMF给PCF发送Npcf_UEPolicyControl Update Request消息，携带SUPI, the Policy Control Request Trigger met等信息。 
PCF收到消息后，给AMF返回Npcf_UEPolicyControl Update Response消息。 
PCF根据用户签约数据、本地策略等，决策是否需更新UE Policy，如果需更新，则决策新的UE Policy。 
（可选）如果PCF确定需要更新Policy Control Request Trigger(s)，则给AMF发送Npcf_UEPolicyControl_UpdateNotify Request消息。 
（可选）AMF给PCF返回Npcf_UEPolicyControl_UpdateNotify Response消息。 
PCF构造Manage UE Policy Command消息，携带URSP信息。PCF给AMF发送Namf_ Communication_N1N2MessageTransfer Request消息，消息中携带Manage UE Policy Command消息。AMF给PCF返回Namf_ Communication_N1N2MessageTransfer Response消息。AMF给UE发送DL NAS Transport消息，消息中携带Manage UE Policy Command消息。 
UE保存URSP信息。 
UE构造Manage UE Policy Complete消息，向PCF确认已收到URSP信息。UE向AMF发送UL NAS Transport消息，消息中携带Manage UE Policy Complete消息。AMF向PCF发送Namf_Communication_N1MessageNotify Request消息，携带Manage UE Policy Complete消息。PCF向AMF返回Namf_Communication_N1MessageNotify Response消息。 
PCF重复第7步到第9步，直到把所有UE Policy下发给UE了。 
PCF给UDR发送Nudr_DataRepository_Update Request消息，把相关UE Policy信息保存到UDR中。UDR返回Nudr_DataRepository_Update Response消息。 
PCF发起的UE Policy关联修改
签约数据修改时，PCF发起的UE Policy关联修改的处理如下图所示。 
图4  PCF触发的UE Policy关联修改

流程说明如下： 
PCF向UDR订阅了用户签约的policy data 改变通知，当用户签约的policy data 改变时，UDR向PCF发送Nudr_DM_Notify消息，携带Notification correlation Id、 Policy Data、SUPI等信息，通知PCF用户签约的policy data改变了；或者PCF根据本地策略决定需更新UE policy data。 
PCF确定更新UE policy data。 
（可选）如果PCF确定需要更新Policy Control Request Trigger(s)，则给AMF发送Npcf_UEPolicyControl_UpdateNotify Request消息。 
（可选）AMF给PCF返回Npcf_UEPolicyControl_UpdateNotify Response消息。 
PCF构造Manage UE Policy Command消息，携带URSP信息。PCF给AMF发送Namf_ Communication_N1N2MessageTransfer Request消息，消息中携带Manage UE Policy Command消息。 
AMF的Communication给PCF返回Namf_ Communication_N1N2MessageTransfer Response消息。 
如果用户处于IDLE态，则AMF寻呼用户，并完成网络侧触发的业务请求流程。 
AMF给UE发送DL NAS Transport消息，消息中携带Manage UE policy command消息。 
UE保存URSP信息。 
UE构造Manage UE Policy Complete消息，向PCF确认已收到URSP信息。UE向AMF发送UL NAS Transport消息，消息中携带Manage UE policy Complete消息。AMF向PCF发送Namf_Communication_N1MessageNotify Request消息，携带Manage UE policy Complete消息。PCF向AMF返回Namf_Communication_N1MessageNotify Response消息。 
PCF重复第5步到第10步，直到把所有UE Policy下发给UE了。 
PCF给UDR发送Nudr_DataRepository_Update Request消息，把相关UE Policy信息保存到UDR中。UDR返回Nudr_DataRepository_Update Response消息。 
NF实现 :AMF可以配置是否向PCF获取UE策略。 
在用户注册到5G后，AMF维护与PCF的UE Policy关联，包括UE Policy的建立，修改，删除。 
AMF与PCF的UE Policy关联建立后，AMF可以透传PCF与UE间的UE Policy信息。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N15|ZUF-79-19-007 N15
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|标准名称
---|---
3GPP 23.501|System Architecture for the 5G System (R15)
3GPP 23.502|Procedures for the 5G System (R15)
3GPP 23.503|Policy and Charging Control Framework for the 5G System (R15)
3GPP 29.507|Access and Mobility Policy Control Service(R15)
3GPP 29.525|5G System; UE Policy Control Service(R15)
特性能力 :名称|指标
---|---
可控制是否支持UE Policy的投递|开关
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“支持UE Policy投递”，此项目显示为“支持”，表示ZUNN-uMAC支持UE Policy投递功能。 
对其他网元的要求 :UE|gNodeB|AMF|PCF|UDR
---|---|---|---|---
√|-|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
缺省向PCF获取AM和UE策略的策略配置|SET DEFASUPTPCFPOLICY
SHOW DEFASUPTPCFPOLICY|缺省向PCF获取AM和UE策略的策略配置
基于号段和切片向PCF获取AM和UE策略的策略配置|ADD SEGSLISUPTPCFPOLICY
SET SEGSLISUPTPCFPOLICY|基于号段和切片向PCF获取AM和UE策略的策略配置
DEL SEGSLISUPTPCFPOLICY|基于号段和切片向PCF获取AM和UE策略的策略配置
SHOW SEGSLISUPTPCFPOLICY|基于号段和切片向PCF获取AM和UE策略的策略配置
局间流程PCF策略配置|SET INTERAMFPCFCFG
SHOW INTERAMFPCFCFG|局间流程PCF策略配置
投递UE策略结束时长|SET UEPOLICY DELIVER DURATION
SHOW UEPOLICY DELIVER DURATION|投递UE策略结束时长
性能统计 :性能计数器名称
---
C510560010 发送Npcf_UEPolicyControl_Create请求次数
C510560011 接收Npcf_UEPolicyControl_Create响应次数
C510560012 接收Npcf_UEPolicyControl_UpdateNotify次数
C510560013 发送Npcf_UEPolicyControl_UpdateNotify响应次数
C510560014 发送Npcf_UEPolicyControl_Delete请求次数
C510560015 接收Npcf_UEPolicyControl_Delete响应次数
C510560016 发送Npcf_UEPolicyControl_Update请求次数
C510560017 接收Npcf_UEPolicyControl_Update响应次数
C510560018 接收Npcf_UEPolicyControl_Create失败响应次数（失败响应码Temporary Redirect）
C510560020 接收Npcf_UEPolicyControl_Terminate请求次数
C510560022 发送Npcf_UEPolicyControl_Terminate响应次数
C510560029 接收Npcf_UEPolicyControl_Create失败响应次数（失败响应码429）
C510560030 接收Npcf_UEPolicyControl_Create失败响应次数（失败响应码503）
C510560031 接收Npcf_UEPolicyControl_Delete失败响应次数（失败响应码429）
C510560032 接收Npcf_UEPolicyControl_Delete失败响应次数（失败响应码503）
C510560033 接收Npcf_UEPolicyControl_Update失败响应次数（失败响应码429）
C510560034 接收Npcf_UEPolicyControl_Update失败响应次数（失败响应码503）
C510560035 发送 Namf_Communication_N1N2MessageTransfer失败响应次数（失败响应码429）
C510560036 发送 Namf_Communication_N1N2MessageTransfer失败响应次数（失败响应码503）
C510560037 发送 Namf_Communication_N1N2MessageSubscriber失败响应次数（失败响应码429）
C510560038 发送 Namf_Communication_N1N2MessageSubscriber失败响应次数（失败响应码503）
C510560041 发送Npcf_UEPolicyControl_UpdateNotify失败响应次数（失败响应码429）
C510560042 发送Npcf_UEPolicyControl_UpdateNotify失败响应次数（失败响应码503）
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :PCF决策UE Policy，AMF在UE和PCF间透传UE Policy Container，UE使用UE Policy。AMF上通过相关配置，实现PCF和UE之间的用户策略路由。 
配置前提 :系统运行正常。 
配置过程 :###### AMF配置过程 
通过[SET DEFASUPTPCFPOLICY]命令，设置AMF是否向PCF获取UE策略的默认策略。
 说明： 
此命令是AM策略和UE策略共用命令，可通过独立字段设置各自的默认策略，此处只描述UE策略相关配置。 
通过[ADD SEGSLISUPTPCFPOLICY]命令，设置UE策略的用户号段类型/用户号段/切片多维度匹配策略， 以及决策匹配成功后是否向PCF获取UE/AM策略。
通过[SET INTERAMFPCFCFG]命令，设置局间注册更新、切换、重定向等流程中老局是否携带PCF信息（PCFid，UE策略的Uri，AM策略的Uri，等）及新局是否重选PCF的策略。
通过 [SET UEPOLICY DELIVER DURATION]命令，设置AMF为PCF及UE透传上下行的UE Policy 消息的持续时长（默认1s）。
 说明： 
步骤2和步骤3中描述的命令，为AM策略和UE策略共用命令，其中命令[ADD SEGSLISUPTPCFPOLICY]可通过独立字段分别设置匹配成功时是否向PCF获取AM/UE策略；命令[SET INTERAMFPCFCFG]中的配置内容对AM/UE策略统一生效，此处只关注UE策略相关配置。
配置实例 :配置场景 :本配置适用于当用户需要向PCF建立UE策略关联，通过AMF实现PCF和UE之间的UE Policy Data传递。 
数据规划 :参数|示例
---|---
缺省向PCF获取AM策略和UE策略的策略配置|向PCF获取AM策略|支持AM策略
向PCF获取UE策略|缺省向PCF获取AM策略和UE策略的策略配置|支持UE策略
基于号段和切片向PCF获取AM策略和UE策略的策略配置|用户号段类型|SUPI
用户号段|基于号段和切片向PCF获取AM策略和UE策略的策略配置|460113
NSSAI Profile标识|基于号段和切片向PCF获取AM策略和UE策略的策略配置|1
向PCF获取AM策略|基于号段和切片向PCF获取AM策略和UE策略的策略配置|支持AM策略
向PCF获取UE策略|基于号段和切片向PCF获取AM策略和UE策略的策略配置|支持UE策略
局间流程PCF策略配置|老局携带PCF信息策略|携带PCF信息
新局重选PCF策略|局间流程PCF策略配置|重选PCF
投递UE策略结束时长|投递UE策略结束时长(ms)|2000
配置步骤 :步骤|说明|操作
---|---|---
1|打开缺省向PCF获取（AM策略和）UE策略开关|SET DEFASUPTPCFPOLICY:IFAMPOLICY="AMPOLICYSUPT",IFUEPOLICY="UEPOLICYSUPT"
2|增加基于号段和切片向PCF获取（AM策略和）UE策略的策略配置|ADD SEGSLISUPTPCFPOLICY:SEGMENTTYPE="SUPISEGMENT",USERSEGMENT="460113",NSSAIPROFILEID=1,IFAMPOLICY="AMPOLICYSUPT",IFUEPOLICY="UEPOLICYSUPT"
3|设置局间流程PCF老局携带PCF信息及新局重建UE策略和AM策略的规则|SET INTERAMFPCFCFG:OLDAMFCARRYPCFINFO="CARRY",NEWAMFRESELECTPCF="RESELECT"
4|设置AMF一次性连续进行上下行投递UE策略数据的结束时长|SET UEPOLICY DELIVER DURATION:UEPOLICYDELIVERDURA=2000
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|用户在老局建立（AM策略和）UE策略，局间注册更新，携带（AM策略和）UE策略信息，新局重选PCF，重新建立（AM策略和）UE策略关联
---|---
测试目的|测试UE策略关联的建立。测试UE策略在AMF局间流程中的处理。测试AMF可以在PCF和UE间传递上下行UE策略Data。
预置条件|5GC部署成功，各个NF均成功接入EM。各个NF配置完成，UDM放号完成。AMF1和AMF2上均已完成前述配置实例中所述的UE策略相关配置。
测试过程|用户（SUPI ：460113000001234）开机，在AMF1发起5G注册流程。在AMF2上发起注册更新，携带1中分配的5G GUTI，AMF2成功从AMF1获取用户上下文，局间流程成功。新PCF下发Manage UE Policy Command消息给UE，UE回复Manage UE Policy Complete消息给PCF，AMF透传上下行消息。
通过准则|用户在老局成功建立（AM策略和）UE策略。局间注册更新，携带（AM策略和）UE策略信息。新局重选PCF，重新建立（AM策略和）UE策略关联。AMF2 在 PCF和UE之间成功透传上下行消息。
测试结果|基于号段和切片向PCF获取AM和UE策略的策略配置无法匹配到SUPI及GPSI号段，使用“缺省向PCF获取AM和UE策略的策略配置”配置，即“支持UE策略”，故老局成功建立UE及AM策略。“局间流程PCF策略配置”老局策略为“携带PCF信息”，局间上下文响应中老局携带PCF信息给新局。“局间流程PCF策略配置”新局策略为“重选PCF”，新局强制重新选择PCF ，并重新建立（AM策略和）UE策略关联。“投递UE策略结束时长”为2000ms，可以在这个时间段内完成PCF和UE之间的上下行消息透传。
常见问题处理 :无。 
# 缩略语 
# 缩略语 
3GPP :3rd Generation Partnership Project第三代合作伙伴计划
AMF :Access and Mobility Management Function接入和移动管理功能
## ANDSP 
Access Network Discovery & Selection Policy接入网发现和选择策略
PCF :Policy Control Function策略控制功能
## SSC 
Session and Service Continuity会话与业务连续性
UE :User Equipment用户设备
## URSP 
UE Route Selection PolicyUE路由选择策略
# ZUF-79-09 网络切片 
## ZUF-79-09-001 支持用户接入网络切片 
特性描述 :特性描述 :适用网元 :AMF 
描述 :定义 :支持用户接入网络切片是指用户注册过程中，5GC需为UE确定Allowed NSSAI、Configured NSSAI和Rejected NSSAI，选择支持Allowed NSSAI的AMF，并把Allowed
NSSAI等信息通知UE和RAN。
背景知识 :随着社会的发展和时代的进步，人们对5GC网络提出了更多的需求，这些需求在不同场景下可能相互矛盾，比如uRLLC需要提供超高可靠低时延服务；mMTC要求海量的连接数，但是数据量比较小，且对时延要求不高；eMBB则要求高带宽、大数据量的服务。
在传统的以人为中心的单一网络基础上，继续进行融合和优化，已经很难满足千差万别的需求，而如果每一种场景都建设专网，又会增加建网和运营成本，造成大量的资源浪费。 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的端到端逻辑网络，适配各种类型服务的不同特征及需求，且每个网络切片在逻辑上隔离。 
网络切片是一个完整的逻辑网络，包含一系列能够提供一定网络能力和网络特性的网络功能和相应资源。网络切片有三个关键特征： 
端到端的逻辑网络：网络切片至少包含接入网、承载网、核心网，也可以包含第三方应用。 
按需定制的逻辑网络：网络切片可按需提供网络业务，按需提供容量，按需提供切片生命周期，按需分布式部署。 
切片之间的隔离：包括安全隔离、资源隔离、操作维护隔离。切片之间相互隔离，一个切片的异常不会影响到其它切片。 
相关术语参见下表。 
术语|含义
---|---
NSI|网络切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。
S-NSSAI|单个网络切片选择辅助信息，用于标识一个网络切片。由两部分组成：SST：业务或切片类型，如eMBB、mMTC、uRLLC，后续可以继续扩展。SD：其它可以区分切片的信息，比如区域信息，租户信息等。
NSSAI|网络切片选择辅助信息，代表了一系列S-NSSAI的合集。
Subscribed S-NSSAI|签约切片表示网络侧授权用户可以接入的切片列表，由运营商在用户放号或者签约变更时确定。
Configured NSSAI|配置NSSAI，表示网络配置给UE使用的切片列表，列表中最多包含16个切片。网络会在注册接受消息（Registration Accept）的“Configured NSSAI” IE带给UE。按照3GPP标准，配置NSSAI既可以由AMF确定，也可以由NSSF确定。AMF支持如下配置NSSAI来源策略：本地配置：下发给UE的配置NSSAI为本地配置的配置NSSAI与签约切片的交集。签约：下发给UE的配置NSSAI来源于用户签约切片。NSSF优先：若NSSF切片选择过程中，NSSF返回了配置NSSAI给AMF，则下发给UE的配置NSSAI取NSSF返回的配置NSSAI；若NSSF未返回配置NSSAI，则取用户签约切片作为配置NSSAI，下发给UE。
Requested NSSAI|请求NSSAI，由UE在注册请求消息（Registration Request）中携带给AMF，表示UE期望提供服务的所有切片列表，根据当前3GPP标准，列表中最多包含8个切片。UE携带请求NSSAI的逻辑如下：若当前选择的PLMN，终端无Allowed NSSAI和Configured NSSAI，则取默认Configured NSSAI；若也无默认Configured NSSAI，则不携带请求NSSAI。若当前选择的PLMN，终端无Allowed NSSAI，但有Configured NSSAI，则取Configured NSSAI或者其子集。若当前选择的PLMN，终端有Allowed NSSAI，但无Configured NSSAI，则取Allowed NSSAI或者其子集。若当前选择的PLMN，终端有Allowed NSSAI和Configured NSSAI，则取Allowed NSSAI、或者Allowed NSSAI子集、或者Allowed NSSAI+Configured NSSAI/Configured NSSAI子集、或者Allowed NSSAI子集+Configured NSSAI/Configured NSSAI子集。请求NSSAI中的切片不能包含在Rejected NSSAI中。
Allowed NSSAI|允许NSSAI，由网络侧下发给UE的允许其使用的网络切片列表，根据当前3GPP标准，列表中最多包含8个网络切片。若注册请求中携带了请求切片，则允许NSSAI为请求切片、用户签约切片以及本网支持切片的交集；若注册请求未携带请求切片，则允许切片为用户签约的默认切片以及本网支持切片的交集。按照3GPP标准，允许NSSAI既可以由AMF决策，也可以由NSSF决策。当AMF不支持切片协商时，AMF调用NSSF的Nnssf_NSSelection服务，获取允许NSSAI。
Rejected NSSAI|拒绝NSSAI，表示UE请求的NSSAI中，哪些S-NSSAI被网络拒绝了。网络会在注册接受消息（Registration Accept）的“Rejected NSSAI” IE带给UE。
应用场景 :在基于切片部署的组网内，为了支持用户接入网络切片，需要开启本特性。 
客户收益 :受益方|受益描述
---|---
运营商|提高运营成本效益：在时间维度和业务维度上有效调配网络资源，运营商可以更加高效地提供业务。便于业务创新：引入新业务更简单，新业务上线周期更短，成本更低。节约投资成本：多种业务共用同一套硬件基础设施，不用为每一种业务创建专有的硬件基础设施。提高用户满意度：满足用户的多样业务需求，提升用户体验。
终端用户|满足用户的多样业务需求，提升终端用户体验。
实现原理 :系统架构 :用户接入网络切片的组网结构如[图1]所示。
图1  系统架构

涉及的网元 :网元名称|说明
---|---
UDM|用户签约信息处理NF，注册过程中与UDR配合向AMF等提供用户Subscribed NSSAI等数据。
PCF|用户策略控制NF，注册过程中与UDR配合向AMF提供网络切片选择策略/用户路由选择策略（路由选择策略中包含网络切片选择策略）等数据。
NRF|网络功能仓储NF，注册过程中提供NF发现功能。
NSSF|网络切片选择NF，在注册过程中，完成以下功能：根据Requested NSSAI和Subscribed NSSAI等信息，决策UE的Allowed NSSAI和Rejected NSSAI。确定AMF Set或AMF Candidate。
(R)AN|无线接入网络，在注册过程中根据UE请求的NSSAI或5G-GUTI选择Initial AMF。
UE|支持5G接入的终端，在注册请求消息中提供请求的NSSAI，并完成Allowed NSSAI和Rejected NSSAI的更新。
本网元实现 :AMF在本特性中实现以下功能。 
和UDM交互，获取用户Subscribed NSSAI等信息。 
和NSSF交互，获取用户的Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate等信息。 
和NRF交互，根据AMF Set等信息获取AMF Candidate。 
和其他AMF交互，完成AMF重定向。 
和RAN交互，完成AMF重定向。 
和PCF交互，获取用户的切片选择策略等信息。 
切片选择整体流程如[图2]所示。
图2  切片选择

业务流程 :注册流程中切片信息处理
注册流程中切片信息处理流程如[图3]所示。
图3  注册过程中切片信息处理

流程说明如下： 
UE判断需要发起注册流程时，发送注册请求消息，消息中携带Requested NSSAI。 
NG-RAN收到注册请求消息后，如果消息中有5G-GUTI，则根据5G-GUTI选择AMF；如果消息中没有5G-GUTI，则根据消息中Requested NSSAI信息，选择一个合适的AMF（Initial AMF）。 
NG-RAN向Initial AMF发送注册请求消息。 
Initial AMF处理注册请求消息，包括获取用户信息、安全过程等。 
Initial AMF向UDM发送Nudm_SDM_Get消息，向UDM获取用户签约数据。 
UDM向Initial AMF返回Nudm_SDM_Get响应消息，消息中携带Subscribed NSSAI等用户签约信息。 
（可选）Initial AMF按照如下规则确定是否需要向NSSF发送Nnssf_NSSeleciton_Get消息，消息中携带Requested NSSAI、Subscribed NSSAI、用户接入的TA、SUPI等信息。 
若用户上下文中存在Allowed NSSAI：当“本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务”配置为“支持切片选择”时，Initial AMF判断本AMF是否支持Requested NSSAI和Subscribed NSSAI的交集，若不支持则向NSSF发送Nnssf_NSSeleciton_Get消息，若支持则本AMF可以为用户服务，无需发送Nnssf_NSSeleciton_Get消息给NSSF，Initial AMF确定Allowed NSSAI、Rejected NSSAI等信息，跳转到步骤14；当“本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务”配置为“不支持切片选择”时，向NSSF发送Nnssf_NSSeleciton_Get消息。 
若用户上下文中不存在Allowed NSSAI：当“本地无Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务”配置为“支持切片选择”时，Initial AMF判断本AMF是否支持Requested NSSAI和Subscribed NSSAI的交集，若不支持则向NSSF发送Nnssf_NSSeleciton_Get消息，若支持则本AMF可以为用户服务，无需发送Nnssf_NSSeleciton_Get消息给NSSF，Initial AMF确定Allowed NSSAI、Rejected NSSAI等信息，跳转到步骤14；当“本地无Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务”配置为“不支持切片选择”时，Initial AMF向NSSF发送Nnssf_NSSeleciton_Get消息。 
（可选）NSSF根据Requested NSSAI、Subscribed NSSAI等信息，以及本地策略，确定Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate。NSSF给Intial AMF返回Nnssf_NSSeleciton_Get响应消息，消息中携带Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate等信息。 
（可选）如果NSSF返回了AMF Set，则Initial AMF向NRF发送Nnrf_NFDiscovery_Request消息，消息中携带AMF Set等信息。 
（可选）NRF向Initial AMF返回Nnrf_NFDiscovery_Request响应消息，消息中携带AMF Candidate等信息。 
Initial AMF根据AMF Candidate等信息，确定AMF是否需要重定向。 
（可选）如果AMF需要重定向，则Intial AMF从AMF Candidate中选择一个AMF作为Target AMF。Intial AMF和Target AMF间完成AMF重定向过程。 
继续处理注册过程。 
Intial AMF（AMF没有进行重定向）或Target AMF（AMF进行了重定向）向PCF发送Npcf_AMPolicyControl_Create消息。 
PCF向AMF返回Npcf_AMPolicyControl_Create响应消息，消息中携带URSP等信息，URSP信息中包含NSSP信息。 
AMF继续处理注册流程，包括更新PDU会话等，直到AMF向UE发送注册接受消息。 
AMF向UE发送注册接受消息，消息中携带Allowed NSSAI、Rejected NSSAI等信息。 
继续处理注册流程，直到注册流程结束。 
签约切片变更流程中切片信息处理
签约切片变更流程中切片信息处理如[图4]所示。
图4  签约切片变更流程中切片信息处理

流程说明如下： 
用户已注册到5GC，签约切片数据发生变化，UDM发送Nudm_SDM_Notification消息给AMF。 
（可选）AMF按照如下规则确定是否需要向NSSF发送Nnssf_NSSeleciton_Get消息，消息中携带Requested NSSAI、Subscribed NSSAI、用户接入的TA、SUPI等信息。 
当“本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务”配置为“支持切片选择”（可通过命令SHOW AMFSUPPOTSLICESELECT查看）时，AMF判断自身否支持Requested NSSAI和Subscribed NSSAI的交集，若不支持则向NSSF发送Nnssf_NSSeleciton_Get消息；若支持则本AMF可以为用户服务，无需发送Nnssf_NSSeleciton_Get消息给NSSF，AMF确定Allowed NSSAI、Rejected NSSAI等信息，执行步骤4。 
当“本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务”配置为“不支持切片选择”时，AMF向NSSF发送Nnssf_NSSeleciton_Get消息。 
（可选）NSSF根据Requested NSSAI、Subscribed NSSAI等信息，以及本地策略，确定Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate。NSSF向AMF返回Nnssf_NSSeleciton_Get  Response消息，消息中携带Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate等信息。 
（可选）AMF满足如下条件之一，则下发Configuration Update Command消息。 
若Allowed NSSAI改变，则Configuration Update Command消息携带Allowed NSSAI等信息。若Allowed NSSAI存在当前AMF不支持的切片，则Configuration Update Command消息携带RED和ACK标记，要求UE回复Configuration Update Complete消息，且重新触发注册流程。 
若Rejected NSSAI改变，则Configuration Update Command消息携带Rejected NSSAI等信息。 
若Configured NSSAI改变，则Configuration Update Command消息携带Configured NSSAI等信息。 
（可选）Configuration Update Command消息携带ACK标记，则UE回复Configuration Update Complete消息。 
（可选）Configuration Update Command消息携带RED标记，则UE触发注册流程。 
系统影响 :注册过程中处理网络切片信息，会消耗一定的系统资源。 
应用限制 :AMF把自身支持的切片通知到RAN时，需考虑RAN最大支持的切片数量。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准名称
---|---
3GPP|3GPP TS 23.501 Technical Specification Group Services and System Aspects;System Architecture for the 5G System; Stage 2
3GPP TS 23.502 Technical Specification Group Services and SystemAspects; Procedures for the 5G System; Stage 2|3GPP
3GPP TS 23.503 Policy and Charging Control Framework for the 5G System|3GPP
3GPP TS 24.501 Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3|3GPP
3GPP TS 29.503 Unified Data Management Services; Stage 3|3GPP
3GPP TS 29.504 5G System; Unified Data Repository Services; Stage 3|3GPP
3GPP TS 29.507 Access and Mobility Policy Control Service; Stage 3|3GPP
3GPP TS 29.510 Network function repository services; Stage 3|3GPP
3GPP TS 29.531 Network Slice Selection Services; Stage 3|3GPP
3GPP TS 38.413 NG Application Protocol (NGAP)|3GPP
特性能力 :名称|指标
---|---
单个UE支持的最大S-NSSAI数|8（每个UE支持的网络切片最多8个）
AMF支持的最大S-NSSAI个数|1024（每个AMF支持的网络切片最多1024个）
AMF授权的最大S-NSSAI个数|1024（每个AMF的授权网络切片最多1024个）
5GC支持的最大NSI个数|4096（每个5GC最多支持4096个网络切片实例）
单一NSI内单一NF实例数目|64（每个网络切片实例最多支持64个同一种类的NF实例）
可获得性 :版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
03|V7.22.20|新增切片选择整体流程说明和签约切片变更流程中的切片信息处理业务流程。
02|V7.21.20|修改特性能力、新增设置NF注册参数配置及设置N2 Setup参数配置。
01|V7.19.10|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB|UDM|NSSF|NRF|PCF
---|---|---|---|---|---
√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :需要规划如何对网络进行切片。 
例如规划按切片类型/业务类型对网络进行切片，则需规划每个网络切片实例（NSI）的服务对象，如每一个NSI服务的S-NSSAIs。
O&M相关 :命令 :配置项|命令
---|---
网络切片策略配置|SET AMFSUPPOTSLICESELECT
SHOW AMFSUPPOTSLICESELECT|网络切片策略配置
AMF支持的SNSSAI配置|ADD AMFSNSSAI
DEL AMFSNSSAI|AMF支持的SNSSAI配置
SET AMFSNSSAI|AMF支持的SNSSAI配置
SHOW AMFSNSSAI|AMF支持的SNSSAI配置
互操作SNSSAI配置|SET INTERWORKINGSNSSAI
SHOW INTERWORKINGSNSSAI|互操作SNSSAI配置
紧急业务SNSSAI配置|SET EMERGSRVSNSSAI
SHOW EMERGSRVSNSSAI|紧急业务SNSSAI配置
SNSSAI统计对象配置|ADD PMSNSSAI
SET PMSNSSAI|SNSSAI统计对象配置
DEL PMSNSSAI|SNSSAI统计对象配置
SHOW PMSNSSAI|SNSSAI统计对象配置
AMF互操作配置|SET 5GINTERWORKCFG
SHOW 5GINTERWORKCFG|AMF互操作配置
Configured NSSAI下发策略配置|SET CONFIGNSSAICONTROL
SHOW CONFIGNSSAICONTROL|Configured NSSAI下发策略配置
Configured SNSSAI配置|ADD CONFIGUREDSNSSAI
SET CONFIGUREDSNSSAI|Configured SNSSAI配置
DEL CONFIGUREDSNSSAI|Configured SNSSAI配置
SHOW CONFIGUREDSNSSAI|Configured SNSSAI配置
按号段Configured SNSSAI来源策略配置|ADD CONFIG SNSSAI SUPI
SET CONFIG SNSSAI SUPI|按号段Configured SNSSAI来源策略配置
DEL CONFIG SNSSAI SUPI|按号段Configured SNSSAI来源策略配置
SHOW CONFIG SNSSAI SUPI|按号段Configured SNSSAI来源策略配置
按号段Configured SNSSAI列表配置|ADD SUPI CONFIG SNSSAIID LIST
DEL SUPI CONFIG SNSSAIID LIST|按号段Configured SNSSAI列表配置
SHOW SUPI CONFIG SNSSAIID LIST|按号段Configured SNSSAI列表配置
默认Configured NSSAI来源策略配置|SET DEFAULT CONFIG SNSSAI POLICY
SHOW DEFAULT CONFIG SNSSAI POLICY|默认Configured NSSAI来源策略配置
默认Configured SNSSAI列表配置|ADD DEFAULT CONFIG SNSSAI ID
DEL DEFAULT CONFIG SNSSAI ID|默认Configured SNSSAI列表配置
SHOW DEFAULT CONFIG SNSSAI ID|默认Configured SNSSAI列表配置
网络切片实例配置|ADD NSIID
DEL  NSIID|网络切片实例配置
SHOW NSIID|网络切片实例配置
NF注册参数配置|SET NFREGPARACFG
SHOW NFREGPARACFG|NF注册参数配置
N2 Setup参数配置|SET N2SETUPPARACFG
SHOW N2SETUPPARACFG|N2 Setup参数配置
性能统计 :测量类型|描述
---|---
基于SNSSAI注册更新流程测量|编号为C51144开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息。 
业务观察/失败观察 :本特性不涉及业务观察/失败观察的变化。 
话单与计费 :本特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过相关配置，实现支持用户接入网络切片功能。 
配置前提 :5GC网络切片已经实例化成功。 
网络切片中各个NF的HTTP服务化接口地址已经配置并且互通正常。 
5GC网络切片的各个NF已经成功接入EMS。 
配置过程 :###### 基本配置 
执行[SET AMFSUPPOTSLICESELECT]命令，配置网络切片策略。
执行[ADD AMFSNSSAI]命令，配置本AMF的S-NSSAI。
执行[SET 5GINTERWORKCFG]命令，设置AMF互操作配置。
执行[SET INTERWORKINGSNSSAI]命令，配置互操作使用的切片。
执行[SET EMERGSRVSNSSAI]命令，配置紧急业务切片。
执行[ADD PMSNSSAI]命令，配置基于SNSSAI测量的统计对象，其中SNSSAI数据引用自[ADD AMFSNSSAI]命令。
###### 可选配置 
如果需要协商携带给UE的ConfiguredNSSAI时，需要执行以下配置步骤： 
执行[SET CONFIGNSSAICONTROL]命令，配置Configured NSSAI下发策略。
执行[ADD CONFIGUREDSNSSAI]命令，配置Configured SNSSAI资源池。
执行[ADD CONFIG SNSSAI SUPI]命令，配置Configured NSSAI匹配的号段以及来源。
执行[ADD SUPI CONFIG SNSSAIID LIST]命令，为每个SUPI号段增加关联的Congfigured SNSSAI ID 。每个号段最多配置16个SNSSAI，SNSSAI ID需要先通过[ADD CONFIGUREDSNSSAI]命令增加。
执行[SET DEFAULT CONFIG SNSSAI POLICY]命令，配置当UE的SUPI无法匹配到所增加的SUPI号段时，AMF下发Congfigured NSSAI使用的默认策略。
执行[ADD DEFAULT CONFIG SNSSAI ID]命令，配置使用默认策略时使用的Congfigured SNSSAI ID。
网络切片其它可选配置： 
如果一个AMF被多个网络切片实例共享，则需要配置多个网络切片实例： 
执行[ADD NSIID]命令，增加AMF支持的NSI。
配置NRF注册和更新消息中携带的AMF支持切片和授权切片的最大个数，以及切片是否支持SD Range： 
执行[SET NFREGPARACFG]命令，修改NF注册参数配置。
配置N2 Setup和Configuration Update消息中每个PLMN下携带的最大切片数： 
执行[SET N2SETUPPARACFG]命令，修改N2 Setup参数配置。
配置实例 :配置场景 :本配置适用于当用户需要接入网络切片的场景。配置完成后，用户可以注册接入网络切片。 
数据规划 :命令|参数名称|取值|数据来源|说明
---|---|---|---|---
SET AMFSUPPOTSLICESELECT|本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务|支持切片选择|本端规划|-
本地无Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务|SET AMFSUPPOTSLICESELECT|支持切片选择|本端规划|-
PDU会话建立支持切片选择|SET AMFSUPPOTSLICESELECT|不支持切片选择|本端规划|-
是否支持注册拒绝携带reject NSSAI|SET AMFSUPPOTSLICESELECT|不支持注册拒绝携带RejectNssai|本端规划|-
切片选择失败后处理|SET AMFSUPPOTSLICESELECT|不放行|本端规划|-
ADD AMFSNSSAI|SNSSAI标识|2CeMBB|本端规划|-
SST|ADD AMFSNSSAI|1-eMBB|本端规划|根据运营商规划配置。编号0-127为标准SST， 编号128-255为运营商自定义的SST。
SD|ADD AMFSNSSAI|NULL|本端规划|根据运营商规划配置。SD格式为6位十六进制。
SET 5GINTERWORKCFG|支持N26互操作|支持N26互操作|本端规划|-
支持无N26互操作|SET 5GINTERWORKCFG|不支持无N26互操作|本端规划|-
互操作模式|SET 5GINTERWORKCFG|有N26|本端规划|-
AMF支持非直接数据前转|SET 5GINTERWORKCFG|支持|本端规划|-
互操作是否需要UE签约支持|SET 5GINTERWORKCFG|不需要UE签约支持互操作|本端规划|-
GTP重发队列间隔(秒)|SET 5GINTERWORKCFG|3|本端规划|-
支持空闲态模式下4G移动5G时V-SMF或I-SMF重选|SET 5GINTERWORKCFG|不支持|本端规划|-
空闲态模式下互操作S-NSSAI获取策略|SET 5GINTERWORKCFG|智能推导|本端规划|-
GTP重发队列次数|SET 5GINTERWORKCFG|5|本端规划|-
S1 mode to N1 mode NAS transparent container中是否携带 EPS UE security capability|SET 5GINTERWORKCFG|否|本端规划|-
AMF是否支持5G的Return Preferred|SET 5GINTERWORKCFG|不支持5G的Return Preferred|本端规划|-
AMF是否支持4G的Return Preferred|SET 5GINTERWORKCFG|不支持4G的Return Preferred|本端规划|-
向SMF请求会话上下文时是否携带MME能力|SET 5GINTERWORKCFG|是|本端规划|-
支持DNN格式容错|SET 5GINTERWORKCFG|不支持||
SET INTERWORKINGSNSSAI|SST|1-eMBB|本端规划|根据运营商规划配置。编号0-127为标准SST， 编号128-255为运营商自定义的SST。
SD|SET INTERWORKINGSNSSAI|NULL|本端规划|根据运营商规划配置。SD格式为6位十六进制。
SET EMERGSRVSNSSAI|紧急业务SST|1-eMBB|本端规划|根据运营商规划配置。编号0-127为标准SST， 编号128-255为运营商自定义的SST。
紧急业务SD|SET EMERGSRVSNSSAI|NULL|本端规划|根据运营商规划配置。SD格式为6位十六进制。
ADD PMSNSSAI|ID|1|本端规划|-
SST|ADD PMSNSSAI|1-eMBB|本端规划|根据运营商规划配置。编号0-127为标准SST， 编号128-255为运营商自定义的SST。
SD|ADD PMSNSSAI|NULL|本端规划|根据运营商规划配置。SD格式为6位十六进制。
（可选）如果需要协商携带给UE的ConfiguredNSSAI，数据规划参见下表。 
命令|参数名称|取值|数据来源|说明
---|---|---|---|---
SET CONFIGNSSAICONTROL|Configured NSSAI下发控制|系统判断|本端规划|-
ADD CONFIGUREDSNSSAI|SNSSAIID|1|本端规划|-
SST|ADD CONFIGUREDSNSSAI|eMBB|本端规划|-
SD|ADD CONFIGUREDSNSSAI|ABCDEF|本端规划|-
ADD CONFIG SNSSAI SUPI|SUPI号段|46001112200|本端规划|-
Configured NSSAI策略|ADD CONFIG SNSSAI SUPI|本地配置|本端规划|-
ADD SUPI CONFIG SNSSAIID LIST|SUPI号段|46001112200|本端规划|-
Supi号段配置SNSSAI标识|ADD SUPI CONFIG SNSSAIID LIST|3|本端规划|-
SET DEFAULT CONFIG SNSSAI POLICY|Configured NSSAI默认策略|本地配置|本端规划|-
ADD DEFAULT CONFIG SNSSAI ID|默认Configured SNSSAI标识|1|本端规划|-
（可选）网络切片其它可选配置的数据规划参见下表。 
命令|参数名称|取值|数据来源|说明
---|---|---|---|---
ADD NSIID|网络切片实例|1|本端规划|-
子切片|ADD NSIID|2CeMBB|本端规划|-
SET NFREGPARACFG|Nnrf接口中切片是否支持SD Range|不支持SD Range|本端规划|-
携带的授权切片的最大个数|SET NFREGPARACFG|8|本端规划|-
携带的AMF支持的切片的最大个数|SET NFREGPARACFG|1024|本端规划|-
SET N2SETUPPARACFG|单PLMN下携带的最大切片数|64|本端规划|-
配置步骤 :用户接入网络切片的基本配置参见下表。 
步骤|说明|操作
---|---|---
1|配置AMF是否支持本地切片选择|SET AMFSUPPOTSLICESELECT:IFSERVEUEWITHALLOWED="AMFSUPTSLICESELECT",IFSERVEUEWITHOUT="AMFSUPTSLICESELECT",PDUSUPSLICESELECT="AMFNOTSUPTSLICESELECT",PROCESSAFTERFAIL="NOTPASS",REGREJCARRYREJNSSAI="NOTCARRYREJECTNSSAIINREGREJ"
2|配置本AMF的S-NSSAI|ADD AMFSNSSAI:SNSSAINAME="2CeMBB",SST="eMBB",SD="NULL"
3|AMF互操作配置|SET 5GINTERWORKCFG:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="NOSPRT",INTERWORKMODE="WITHN26",GTPRETRYTIMES=5,GTPRETRYINTERVAL=3,SUPINDFWDTUNNEL="INDFWDSPRT",SELPOLIFORCOMBSMF="NONEED",CARRYEPSUESECCAP="NO",SPRT5GREPREFI="NOSPRT",SPRT4GREPREFI="NOSPRT",CARRYMMECAPA="CARRY",SUPIVSMFRESELIDLE="NOSPRT",IDLEIWKSNSSAIPLY="INTELLIGENTDEDUCTION",SUPDNNFAULT="NOSPRT"
4|配置互操作切片|SET INTERWORKINGSNSSAI:SST="eMBB",SD="NULL"
5|配置紧急呼叫切片|SET EMERGSRVSNSSAI:EMGSST="eMBB",EMGSD="NULL"
6|配置基于SNSSAI测量的统计对象|ADD PMSNSSAI:ID=1,SST="eMBB",SD="NULL"
（可选）如果需要协商携带给UE的ConfiguredNSSAI，配置步骤参见下表。 
步骤|说明|操作
---|---|---
1|设置Congfigured NSSAI下发策略。|SET CONFIGNSSAICONTROL:CONFIGNSSAICONTROL="SYSTEMDEFI"
2|配置Configured SNSSAI资源池。|ADD CONFIGUREDSNSSAI:SNSSAIID=1,SST="eMBB",SD="ABCDEF"
3|配置Configured NSSAI匹配的号段以及来源。|ADD CONFIG SNSSAI SUPI:SUPISEGMENT="46001112200",CONFISNSSAIPOLICY="LOCALCONFIGURED"
4|为每个SUPI号段增加关联的Congfigured SNSSAI ID。|ADD SUPI CONFIG SNSSAIID LIST:SUPISEGMENT="46001112200",SUPICONFIGSNSSAIID=3
5|配置当UE的SUPI无法匹配到所增加的SUPI号段时，AMF下发Congfigured NSSAI使用的默认策略。|SET DEFAULT CONFIG SNSSAI POLICY:DEFACONFISNSSAIPOL="LOCALCONFIGURED"
6|配置使用默认策略时使用的Congfigured SNSSAI ID。|ADD DEFAULT CONFIG SNSSAI ID:DEFACONFISNSSAIID=1
（可选）网络切片其它可选配置参见下表。 
步骤|说明|操作
---|---|---
7|增加网络切片实例配置|ADD NSIID:NSIID="1",NSSIID="2CeMBB"
8|设置NF注册参数配置|SET NFREGPARACFG:IFSDRANGE="NOTSUPPORTSDRANGE",MAXALLOWEDNSSAISNUM=8,MAXSNSSAISNUM=1024
9|设置N2 Setup参数配置|SET N2SETUPPARACFG:MAXNSSAINUM=64
调整特性 :无。 
测试用例 :测试项目|AMF支持Allowed NSSAI不重定向的注册流程
---|---
测试目的|AMF支持持Allowed NSSAI，本局提供服务。
预置条件|AMF支持切片1_NULL。AMF支持本地切片协商。
测试过程|用户发起注册请求，注册请求消息不携带切片。用户签约了切片1_NULL。Allowe Nssai为1_NULL，本局提供服务。
通过准则|用户在本AMF注册成功，注册接受消息携带Allowed NSSAI为切片1_NULL。
测试结果|-
测试项目|AMF不支持Allowed NSSAI重定向的注册流程
---|---
测试目的|AMF不支持Allowed NSSAI，可以重定向到其他AMF。
预置条件|AMF支持切片2_NULL。AMF支持本地切片协商。
测试过程|用户发起注册请求，注册请求消息不携带切片。用户签约了切片1_NULL。Allowe NSSAI为1_NULL，本局不能提供服务。
通过准则|本局通过NSSF发现更合适的AMF2，重定向到AMF2。
测试结果|-
常见问题处理 :无。 
## ZUF-79-09-002 AMF支持NSSAI inclusion mode 
特性描述 :特性描述 :描述 :定义 :AMF支持NSSAI inclusion mode功能是指UE在注册过程中，AMF返回UE的Registration Accept消息中携带NSSAI Inclusion Mode参数。UE收到NSSAI Inclusion Mode参数后，在后续与接入层建立连接中，根据以下情况来判断UE是否携带NSSAI信息。 
以下情况下可携带NSSAI信息：当UE在服务请求、周期性注册更新或用于更新UE能力的注册过程中建立接入层连接时，UE应包含可用的NSSAI信息。当UE在业务请求过程中建立接入层连接时，UE应包含对应NSSAI信息。 
以下情况下可不携带NSSAI信息：当UE在业务请求、定期注册更新或用于更新UE能力的注册过程中建立接入层连接时，UE不包含任何NSSAI信息。UE不在接入层提供NSSAI，即归属和拜访网络可以不管UE建立RRC连接的过程是什么，指示UE在接入层中永远不提供NSSAI。 
背景知识 :单一网络基础已经不能满足现有的需求， 因此引入了网络切片，网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的端到端逻辑网络，用来适配各种类型服务的不同特征及需求。 
NSSAI是网络切片选择辅助信息，代表了一系列S-NSSAI的合集。
S-NSSAI是单个网络切片选择辅助信息，用于标识一个网络切片。由两部分组成：
SST：业务或切片类型，例如eMBB、mMTC、uRLLC。 
SD：其它可以区分切片的信息，例如区域信息、租户信息。 
应用场景 :###### 场景1：初始注册 
终端插入新的SIM卡开机触发的初始注册过程中，AMF在REGISTRATION ACCEPT消息中，根据运营商策略携带NSSAI inclusion mode参数。 
###### 场景2：周期性注册更新和移动性注册更新 
终端移动出5GC为其分配的注册区域时触发移动注册更新或者周期性注册更新过程中，AMF在REGISTRATION ACCEPT消息中，根据运营商策略携带NSSAI inclusion mode参数。 
###### 场景3：紧急注册 
终端紧急注册过程中，AMF在REGISTRATION ACCEPT消息中，根据运营商策略携带NSSAI inclusion mode参数。 
客户收益 :受益方|受益描述
---|---
运营商|降低运营成本，提高效益：根据策略控制终端在接入时切片的选择模式，在时间维度和业务维度上有效调配网络资源，运营商可以更加高效地提供业务。提高用户满意度：满足用户的多样业务需求，提升用户体验。
移动用户|满足用户的多样业务需求，提升终端用户体验。
实现原理 :系统架构 :本特性的组网结构如[图1]所示。
图1  组网结构

涉及的网元 :涉及切片信息处理的NF/网元参见下表。 
NF/网元名称|说明
---|---
NF|AMF|接入和移动性管理NF，在注册过程中，完成以下功能：从UDM获取Subscribed NSSAI Inclusion Allowed信息。AMF在Registration Accept消息中根据运营商策略，携带NSSAI inclusion mode信息给UE。
UDM|NF|用户签约信息处理NF，注册过程中与UDR配合向AMF等提供用户Subscribed NSSAI inclusion mode信息。
网元|(R)AN|无线接入网络，在注册过程中根据UE请求的NSSAI或5G-GUTI选择Initial AMF。
UE|网元|支持5G接入的终端，在注册请求消息中根据NSSAI inclusion mode，提供请求的NSSAI，并完成Allowed NSSAI和Rejected NSSAI的更新。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15
N22|ZUF-79-19-008 N22
本网元实现 :AMF和UDM交互，获取用户Subscribed NSSAI Inclusion Allowed等信息。 
AMF和RAN交互，完成注册更新。 
AMF和UE交互，完成注册更新流程，在注册接受消息中携带NSSAI inclusion mode给UE。 
业务流程 :详细的注册更新流程如[图2]所示。
图2  注册更新流程

流程说明： 
UE开机、周期性定时器超时、移动时发起注册请求，向RAN发送AN消息包括AN parameters消息和Registration Request消息 (包括Registration type, SUCI或5G-GUTI)。UE发送的AN Parameters和Registration Request消息中，包括Requested NSSAI。 
NG-RAN收到注册请求消息后，RAN若无法通过5G-S-TMSI或者GUAMI选择对应的AMF（可选），RAN根据Requested NSSAI选择到对应的AMF。如果RAN不能选择NSSAI对应的AMF, 注册请求被转发到RAN配置的default AMF上，由default AMF做AMF选择。 
NG-RAN向Initial AMF发送注册请求消息。 
Initial AMF处理注册请求消息，包括获取用户信息，安全过程等。 
Initial AMF向UDM发送Nudm_SDM_Get消息，向UDM获取用户签约数据NSSAI Inclusion Allowed。
UDM向Initial AMF返回Nudm_SDM_Get响应消息，消息中携带Subscribed NSSAI等用户签约信息。 
Initial AMF向NSSF发送Nnssf_NSSeleciton_Get消息，消息中携带Requested NSSAI、Subscribed NSSAI、用户接入的TA、SUPI等信息。 
NSSF根据Requested NSSAI、Subscribed NSSAI等信息，以及本地策略，确定Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate。NSSF给Intial AMF返回Nnssf_NSSeleciton_Get响应消息，消息中携带Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate等信息。 
如果NSSF返回了AMF Set，则Initial AMF向NRF发送Nnrf_NFDiscovery_Request消息，消息中携带AMF Set等信息。 
NRF向Initial AMF返回Nnrf_NFDiscovery_Request响应消息，消息中携带AMF Candidate等信息。 
Initial AMF根据AMF Candidate等信息，确定AMF是否需要重定向。 
如果AMF需要重定向，则Intial AMF从AMF Candidate中选择一个AMF作为Target AMF。Intial AMF和Target AMF间完成AMF重定向过程。 
继续处理注册过程。 
Intial AMF（AMF没有进行重定向）或Target AMF（AMF进行了重定向）向PCF发送Npcf_AMPolicyControl_Create消息。 
PCF向AMF返回Npcf_AMPolicyControl_Create Response消息，消息中携带URSP等信息，URSP信息中包含NSSP信息。 
AMF继续处理注册流程，包括更新PDU会话等，直到AMF向UE发送注册接受消息。 
AMF向UE发送Registration Accept消息，消息中携带(5G-GUTI, Registration Area，Allowed NSSAI、NSSAI inclusion mode)等信息。之后，UE会向AMF返回Registration Complete消息。
继续处理注册流程，直到注册流程结束。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准编号|标准名称
---|---
TS 23.501|Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2
TS 23.502|3GPP TS 23.502 Technical Specification Group Services and System Aspects; Procedures for the 5G System; Stage 2
TS 23.503|Policy and Charging Control Framework for the 5G System
TS 24.501|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
TS 29.503|Unified Data Management Services; Stage 3
TS 29.504|5G System; Unified Data Repository Services; Stage 3
TS 29.507|Access and Mobility Policy Control Service; Stage 3
TS 29.510|Network function repository services; Stage 3
TS 29.531|Network Slice Selection Services; Stage 3
TS 38.413|NG Application Protocol (NGAP)
特性能力 :名称|指标
---|---
支持基于号段NSSAI inclusion mode策略个数|4096个
支持缺省NSSAI inclusion mode策略个数|1个
可获得性 :版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.20.20|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为AMF支持NSSAI inclusion mode功能，此项显示为“支持”，表示AMF支持NSSAI inclusion mode功能。
对其他网元的要求 :UE|gNodeB|UDM
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :需要规划终端在接入层连接建立时的切片包含模式，以便对网络进行合理的切片选择。 
O&M相关 :命令 :配置项|命令
---|---
基于号段NSSAI inclusion mode策略配置|ADD SUPI NIM POLICY
SET SUPI NIM POLICY|基于号段NSSAI inclusion mode策略配置
DEL SUPI NIM POLICY|基于号段NSSAI inclusion mode策略配置
SHOW SUPI NIM POLICY|基于号段NSSAI inclusion mode策略配置
缺省NSSAI inclusion mode策略配置|SET DEFAULT NIM POLICY
SHOW DEFAULT NIM POLICY|缺省NSSAI inclusion mode策略配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :NSSAI inclusion mode可以基于SUPI号段的NSSAI inclusion mode策略和缺省NSSAI inclusion mode策略进行配置。 
配置前提 :AMF环境运行正常。 
EM网管能正常连接并登录。 
配置过程 :###### 基于号段NSSAI inclusion mode策略配置 
执行[ADD SUPI NIM POLICY]命令，新增基于SUPI号段NSSAI inclusion mode策略配置。
###### 缺省NSSAI inclusion mode策略配置 
执行[SET DEFAULT NIM POLICY]命令，设置缺省NSSAI inclusion mode策略，即SUPI号段无法匹配时的NSSAI inclusion mode策略。
配置实例 :###### 场景1 
场景说明
终端插入新的SIM卡开机触发的初始注册过程中，在Registration Accept消息中，AMF根据运营商策略携带NSSAI inclusion mode。 
数据规划
参数|取值
---|---
SUPI号段|46001
是否携带NSSAI inclusion mode|YES
NSSAI inclusion mode|NSSAIINCLUMODE_D
配置步骤
步骤|说明|操作
---|---|---
1|新增基于SUPI号段NSSAI inclusion mode策略配置。|ADD SUPI NIM POLIC:SUPISEGMENT="46001",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_D"
###### 场景2 
场景说明
终端移动出5GC为其分配的注册区域时，触发移动注册更新或者周期性注册更新过程中，在Registration Accept消息中，AMF根据运营商策略携带NSSAI inclusion mode。 
数据规划
参数|取值
---|---
SUPI号段|46001
是否携带NSSAI inclusion mode|YES
NSSAI inclusion mode|NSSAIINCLUMODE_A
配置步骤
步骤|说明|操作
---|---|---
1|新增基于SUPI号段NSSAI inclusion mode策略配置。|ADD SUPI NIM POLIC:SUPISEGMENT="46001",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_A"
###### 场景3 
场景说明
终端紧急注册过程，在Registration Accept消息中，AMF根据缺省策略携带NSSAI inclusion mode。 
数据规划
参数|取值
---|---
是否携带NSSAI inclusion mode|YES
NSSAI inclusion mode|NSSAIINCLUMODE_D
配置步骤
步骤|说明|操作
---|---|---
1|修改缺省NSSAI inclusion mode策略配置。|SET DEFAULT NIM POLICY:IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_D"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|初始注册流程中下发NSSAI inclusion mode策略正确
---|---
测试目的|初始注册流程中，按照已配置的基于SUPI号段NSSAI inclusion mode策略，正确下发NSSAI inclusion mode策略。
预置条件|UE、NG-RAN、AMF各网元正常。号段为“46011”的用户支持下发NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”，其它号段不支持携带。
测试过程|号码为“460119990012345”的用户发起初始注册流程。号码为“460029990012345”的用户发起初始注册流程。
通过准则|号码为“460119990012345”的用户的Registration Accept消息中携带NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”。号码为“460029990012345”的用户的Registration Accept消息中不携带NSSAI inclusion mode。
测试结果|–
测试项目|周期性注册更新流程中下发NSSAI inclusion mode策略正确
---|---
测试目的|周期性注册更新流程中，按照已配置的基于SUPI号段NSSAI inclusion mode策略，正确下发NSSAI inclusion mode策略。
预置条件|UE、NG-RAN、AMF各网元正常。号段为“46011”的用户支持下发NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”，其它号段不支持携带。
测试过程|号码为“460119990012345”的用户发起周期性注册更新流程。号码为“460029990012345”的用户发起周期性注册更新流程。
通过准则|号码为“460119990012345”的用户的Registration Accept消息中携带NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”。号码为“460029990012345”的用户的Registration Accept消息中不携带NSSAI inclusion mode。
测试结果|–
测试项目|紧急注册流程中下发NSSAI inclusion mode策略正确
---|---
测试目的|紧急注册流程中，按照已配置的基于SUPI号段NSSAI inclusion mode策略，正确下发NSSAI inclusion mode策略。
预置条件|UE、NG-RAN、AMF各网元正常。号段为“46011”的用户支持下发NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”，其它号段不支持携带。
测试过程|号码为“460119990012345”的用户发起紧急注册流程。号码为“460029990012345”的用户发起紧急注册流程。
通过准则|号码为“460119990012345”的用户的Registration Accept消息中携带NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”。号码为“460029990012345”的用户的Registration Accept消息中不携带NSSAI inclusion mode。
测试结果|–
测试项目|移动性注册更新流程中下发NSSAI inclusion mode策略正确
---|---
测试目的|移动性注册更新流程中，按照已配置的基于SUPI号段NSSAI inclusion mode策略，正确下发NSSAI inclusion mode策略。
预置条件|UE、NG-RAN、AMF各网元正常。号段为“46011”的用户支持下发NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”，其它号段不支持携带。
测试过程|号码为“460119990012345”的用户发起移动性注册更新流程。号码为“460029990012345”的用户发起移动性注册更新流程。
通过准则|号码为“460119990012345”的用户的Registration Accept消息中携带NSSAI inclusion mode，携带的模式为“NSSAI inclusion mode D”。号码为“460029990012345”的用户的Registration Accept消息中不携带NSSAI inclusion mode。
测试结果|–
常见问题处理 :无。 
## ZUF-79-09-003 切片选择策略 
特性描述 :特性描述 :描述 :定义 :切片选择策略是指AMF在用户协商Allowed NSSAI、Configured NSSAI时所采用的策略，比如AMF是否支持本地切片选择、是否启用切片可用性等。从网络切片管理范围角度考虑，可以将切片选择策略划分为如下三类： 
基于全局的切片选择：网络切片在整个移动网络有效，具体可参考ZUF-79-09-001 支持用户接入网络切片。 
基于PLMN的切片选择：网络切片仅在某个或者某几个PLMN有效。AMF基于用户当前的PLMN配置支持的切片，为用户决策Allowed NSSAI。AMF基于PLMN粒度配置Configured NSSAI，为用户决策Configured NSSAI。 
基于TA的切片选择：网络切片仅在一个或者多个区域（TA）有效，AMF基于本地保存的当前TA的切片可用信息，包括当前TA所支持的网络切片列表、网络切片限制列表等信息，结合AMF本地策略，决策用户的Allowed NSSAI。 
背景知识 :随着社会的发展和时代的进步，人们对5GC网络提出了更多的需求，这些需求在不同场景下可能相互矛盾，比如uRLLC需要提供超高可靠低时延服务；mMTC要求海量的连接数，但是数据量比较小，且对时延要求不高；eMBB则要求高带宽、大数据量的服务。
在传统的以人为中心的单一网络基础上，继续进行融合和优化，已经很难满足千差万别的需求，而如果每一种场景都建设专网，又会增加建网和运营成本，造成大量的资源浪费。 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的端到端逻辑网络，适配各种类型服务的不同特征及需求，且每个网络切片在逻辑上隔离。网络切片可以归属整个PLMN，或者归属PLMN下的一个或者多个区域(TA)。 
网络切片是一个完整的逻辑网络，包含一系列能够提供一定网络能力和网络特性的网络功能和相应资源。网络切片有三个关键特征： 
端到端的逻辑网络：网络切片至少包含接入网、承载网、核心网，也可以包含第三方应用。 
按需定制的逻辑网络：网络切片可按需提供网络业务，按需提供容量，按需提供切片生命周期，按需分布式部署。 
切片之间的隔离：包括安全隔离、资源隔离、操作维护隔离。切片之间相互隔离，一个切片的异常不会影响到其它切片。 
应用场景 :本特性应用场景包括如下： 
根据网络规划和业务需要，按照区域或者PLMN部署网络切片。 
根据网络规划和业务需要，按照区域或者PLMN限制网络切片。 
客户收益 :受益方|受益描述
---|---
运营商|灵活部署网络切片，有助于网络业务创新。
用户|快速接入到所需要的网络切片。
实现原理 :系统架构 :用户接入网络切片的组网结构如[图1]所示。
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
NSSF|接受AMF上报的切片可用信息，并给AMF返回符合本地策略要求的切片可用信息。接受AMF切片可用信息订阅，当检测到切片可用信息变化时，通知订阅的AMF。
gNB|上报切片可用信息，即TA下所支持的网络切片列表给AMF。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N22|ZUF-79-19-008 N22
本网元实现 :对于基于TA的切片选择，AMF实现如下功能： 
存储gNB侧上报的切片可用信息，即每TA所支持的网络切片列表。 
当切片可用信息有变更时，比如收到RAN侧上报的切片可用信息时，AMF检查发现携带了新的TA，或者消息中某TA支持的网络切片列表与本地保存的不一致，则向NSSF更新切片可用信息。 
存储NSSF返回的切片可用信息。 
支持基于TA的网络切片限制本地策略配置。 
向NSSF订阅切片可用信息，当NSSF检测到切片可用信息变更后，触发订阅通知给AMF。 
向NSSF去订阅切片可用信息。 
基于切片可用信息决策用户的Allowed NSSAI，确保Allowed NSSAI中的每个S-NSSAI，属于当前接入TA下的supportedSnssaiList但不属于restrictedSnssaiList。 
基于切片可用信息为用户分配TA List，确保列表中的每个TA都支持Allowed NSSAI。 
对于基于PLMN的切片选择，AMF实现如下功能： 
支持按PLMN配置支持的切片。 
支持按PLMN配置Configured NSSAI。 
NRF注册时，支持按PLMN携带支持的切片。 
NRF查询时，支持按PLMN携带支持的切片。 
本地决策Allowed NSSAI时，本局支持的切片为当前PLMN配置支持的切片。 
基于用户号段配置切片限制策略。 
引入基于TA的切片选择以及基于PLMN的切片选择后，切片选择整体流程[图2]所示。
图2  切片选择

###### 基于TA的切片选择业务流程 
AMF向NSSF更新切片可用信息
AMF在如下场景，需要调用NSSF切片可用服务接口，向NSSF更新切片可用信息。 
收到gNB的NG Setup Request或RAN Configuration Update消息，AMF检查消息中携带了新的TAI Slice Support List信息，且本地配置"AMF向NSSF同步TA下supportedSnssaiList"为"是"，则向NSSF同步RAN侧的TA下TAI Slice Support List信息。 
AMF的配置开关“AMF向NSSF同步TA下supportedSnssaiList”从“否”修改为“是”。 
AMF退服后重新进入服务状态。 
AMF向NSSF更新切片可用信息的流程如下图所示。 
图3  AMF向NSSF更新切片可用信息流程

流程说明： 
AMF发送Nssf_NSSAIAvailability_Update Request消息给NSSF，携带supportedSnssaiList、TAI、TA列表(TAIList或者TAIRangeList)。 
NSSF返回Nssf_NSSAIAvailability_Update Response响应消息给AMF，响应消息中携带TAI、TA列表(TAIList或者TAIRangeList)，以及NSSF根据AMF请求消息中的信息，结合本地配置策略，生成的supportedSnssaiList以及restrictedSnssaiList等切片可用信息，AMF保存NSSF返回的切片可用信息。若restrictedSnssaiList中roamingRestriction为true，则把对应S-NSSAI中NSSF提供的对应的PLMN忽略，直接设置为全F；若roamingRestriction为false或没有携带roamingRestriction，则存储对应S-NSSAI中NSSF提供的对应的PLMN。 
AMF向NSSF订阅切片可用信息
AMF在如下场景，需要调用NSSF切片可用服务接口，向NSSF订阅切片可用信息。 
AMF上电。 
AMF退服后重新进入服务状态。 
AMF支持的TA发生变更。 
将开关“AMF支持切片可用性功能”从OFF修改为ON。 
切片可用信息订阅的有效期到达，AMF本地删除切片可用信息订阅记录，重新向NSSF订阅切片可用信息。 
AMF向NSSF订阅切片可用信息的流程如下图所示。 
图4  AMF向NSSF订阅切片可用信息流程

流程说明： 
AMF发送Nssf_NSSAIAvailability_Subscribe Request给NSSF，消息中携带nfNssaiAvailabilityUri,AMF支持的TA列表、expiry等信息。 
NSSF回复Nssf_NSSAIAvailability_Subscribe Response给AMF，携带subscriptionId、expiry以及切片可用信息authorizedNssaiAvailabilityData，AMF保存NSSF返回的切片可用信息。authorizedNssaiAvailabilityData中包含supportedSnssaiList以及restrictedSnssaiList等信息。若restrictedSnssaiList中roamingRestriction为true，则把对应S-NSSAI中NSSF提供的对应的PLMN忽略，直接设置为全F；若roamingRestriction为false或没有携带roamingRestriction，则存储对应S-NSSAI中NSSF提供的对应的PLMN。 
AMF向NSSF去订阅切片可用信息
AMF在如下场景，需要向NSSF去订阅切片可用信息。 
AMF退服。 
AMF支持的TA配置发生改变了，重新订阅前AMF需要取消之前的切片可用信息订阅。 
配置开关“AMF支持切片可用性功能”从ON到OFF。 
AMF向NSSF去订阅切片可用信息的流程如下图所示。 
图5  AMF向NSSF去订阅切片可用信息流程

流程说明： 
AMF发送Nssf_NSSAIAvailability_Unsubscribe Request消息给NSSF，通知NSSF取消切片可用信息订阅。 
NSSF返回Nssf_NSSAIAvailability_Unsubscribe Response响应给AMF。 
NSSF通知AMF变更的切片可用信息
当AMF订阅了切片可用信息后，NSSF检测到存在变更时，发送订阅通知消息给AMF，流程如下图所示。 
图6  NSSF通知AMF变更的切片可用信息流程

流程说明： 
AMF收到NSSF切片可用信息变更通知请求消息Nssf_NSSAIAvailability_Notify Request，保存消息中携带的变更后的切片可用信息。 
AMF回复Nssf_NSSAIAvailability_Notify Response。 
AMF基于切片可用信息确定用户的Allowed NSSAI
AMF在UE触发流程或者用户签约数据变更时，基于切片可用信息为用户确定Allowed NSSAI，策略是保证Allowed NSSAI中的每个S-NSSAI，属于当前接入TA下的supportedSnssaiList但不属于restrictedSnssaiList。 
AMF判断S-NSSAI归属当前接入TA下的supportedSnssaiList逻辑如下图所示。 
AMF判断S-NSSAI归属当前接入TA下的restrictedSnssaiList逻辑如下图所示。 
AMF基于切片可用信息为用户分配TAList
AMF在UE触发注册流程或者用户签约数据发生变更流程中，需要给用户分配TAList时，需要保证TA List中的每个TA都支持Allowed NSSAI，即对于TA List中的每个TA，获取该TA下的supportedSnssaiList和restrictedSnssaiList，然后把Allowed NSSAI中的每一个S-NSSAI，确定在supportedSnssaiList中，且不在restrictedSnssaiList限制范围内。 
确定S-NSSAI是否归属supportedSnssaiList以及restrictedSnssaiList，参考"AMF基于切片可用信息确定用户的Allowed NSSAI"流程。另外，用户当前TA因为已经在[AMF基于切片可用信息确定用户的Allowed NSSAI]流程中考虑过，因此无需再次进行确认。
###### 基于PLMN的切片选择业务流程 
AMF基于当前PLMN支持的切片决策用户Allowed NSSAI
AMF在UE触发流程或者签约变更时，进行本地切片选择的过程中，基于用户当前PLMN配置支持的网络切片，为用户确定Allowed NSSAI。策略是需要保证其中的每一个切片，都属于当前PLMN所支持的切片，且不在用户所归属号段限制的切片中。 
AMF基于当前PLMN支持的切片决策用户Allowed NSSAI判断逻辑如下图所示。 
AMF基于当前PLMN为用户决策Configured NSSAI
AMF在UE触发流程或者签约变更过程中，需要重新协商Configured NSSAI时，若Configured NSSAI来源策略配置为本地配置，则根据本地配置的Configured NSSAI以及用户签约切片信息，获取最终下发给UE的Configured NSSAI。获取本地配置Configured NSSAI的处理逻辑如下图所示。 
AMF向NRF发起注册或者更新流程
若 “NF注册更新请求中是否携带PLMN粒度切片”取值为“是”，则AMF向发起NRF注册或者更新时，请求消息中携带perPlmnSnssaiList，其中包含了本局配置的PLMN粒度的SNSSAI。 
 
AMF向NRF发起NF查询流程
若“NF发现请求中是否携带PLMN粒度切片”取值为“是”，则查询请求中携带requester-plmn-specific-snssai-list，其中包含配置的本AMF所支持的PLMN粒度切片。 
NSSF故障，AMF向NRF查询可用AMF
当NSSF故障，AMF根据本地配置策略，触发向NRF查询可用AMF。AMF从查询响应中选择支持Allowed NSSAI切片最多的AMF，每个可用AMF所支持的切片按如下逻辑获取： 
若“是否支持PLMN粒度切片”取值为“否”，则取NRF返回的NF查询响应中携带的NF Profile中的sNssai。 
若“是否支持PLMN粒度切片”取值为“是”，当NRF返回的NF查询响应中携带NF Profile中的perPlmnSnssaiList时，取NRF返回的NF查询响应中携带的NF Profile中的perPlmnSnssaiList，否则取sNssai。 
系统影响 :开启基于TA的切片选择功能后，预计引起CPU性能下降3%左右。 
应用限制 :本特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2
TS 23.502|3GPP|3GPP TS 23.502 Technical Specification Group Services and System Aspects; Procedures for the 5G System; Stage 2
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
TS 29.503|3GPP|Unified Data Management Services; Stage 3
TS 29.531|3GPP|Network Slice Selection Services; Stage 3
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.40|新增基于PLMN的切片选择策略。
01|V7.20.20|首次发布。
License要求 :该特性为的基本特性，无需License支持。 
对其他网元的要求 :UE|gNB|NSSF
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :TA下所支持的网络切片列表信息属于网元间信息，对所有用户生效，对可靠性要求极高，因此建议1+1备份AMF，即工程上建议至少两个AMF向NSSF同步。 
同一个AMF Set下，由于AMF故障/恢复、AMF退服/重新进入服务状态、AMF向TA（由NSSF同步RAN侧提供）所支持的网络切片列表信息配置开关变更，需要人工调整，建议保证至少两个AMF向NSSF同步。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令切片可用性策略配置SET 5GSLICEAVAILPLYSHOW 5GSLICEAVAILPLYRestrictedSnssai模板配置ADD RSTRNSSAIDEL RSTRNSSAISHOW RSTRNSSAITA下RestrictedSnssai配置ADD 5GTARSTRNSSAISET 5GTARSTRNSSAIDEL 5GTARSTRNSSAISHOW 5GTARSTRNSSAI跟踪区组配置ADD TAGROUPCFGDEL TAGROUPCFGSHOW TAGROUPCFG支持PLMN粒度切片策略配置SET PLMNSNSSAIPLYSHOW PLMNSNSSAIPLYAMF其他PLMN配置ADD PLMNCFGSET PLMNCFGDEL PLMNCFGSHOW PLMNCFG基于PLMN的AMF支持的SNSSAI配置ADD PLMNAMFSNSSAISET PLMNAMFSNSSAIDEL PLMNAMFSNSSAISHOW PLMNAMFSNSSAI切片可用性策略配置SET 5GSLICEAVAILPLYSHOW 5GSLICEAVAILPLY基于SUPI号段的RestrictedSnssai配置ADD 5GSUPIRSTRNSSAISET 5GSUPIRSTRNSSAIDEL 5GSUPIRSTRNSSAISHOW 5GSUPIRSTRNSSAI 
安全变量本特性不涉及安全变量的变化。 
软件参数本特性不涉及软件参数的变化。 
性能统计 :性能计数器名称
---
C510570019 发送Nnssf_NSSAIAvailability_Delete次数
C510570020 接收Nnssf_NSSAIAvailability_Delete响应次数
C510570021 发送Nnssf_NSSAIAvailability_Options次数
C510570022 接收Nnssf_NSSAIAvailability_Options响应次数
告警和通知 :本特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :切片选择策略分为三类：基于全局的切片选择、基于TA的切片选择、基于PLMN的切片选择。基于全局的切片选择配置参见ZUF-79-09-001 支持用户接入网络切片
。本特性对后两类切片选择策略进行配置。
基于TA的切片选择策略：通过对切片可用性策略配置、RestrictedSnssai模板配置、跟踪区组配置、TA下的RestrictedSnssai配置，来建立 “TAI + S-NSSAI + PLMN ”的映射关系。 
基于PLMN的切片选择策略：通过对基于SUPI号段的RestrictedSnssai配置，来建立 “SUPI+SNSSAI ”的映射关系。 
配置前提 :无。 
配置过程 :###### 基于TA的切片选择策略 
执行[SET 5GSLICEAVAILPLY]命令，配置切片可用性策略，包括：
AMF是否支持切片可用性功能 
AMF是否向NSSF同步RAN提供的TA下supportedSnssaiList信息 
NSSF可用性订阅信息到期时长 
执行[ADD RSTRNSSAI]命令，配置RestrictedSnssai模板。
逐条增加模板配置。对于同一个模板标识，可按规划建立一组或多组 “切片S-NSSNAI与PLMN” 的对应关系进行配置。 
每个模板标识一组S-NSSAI，可以与使用的漫游用户的PLMN之间成对应关系。模板标识为非唯一索引，即同一个模板标识，可以对应多个对应关系的配置。这些模板标识供"TA下RestrictedSnssai配置" 引用。 
执行[ADD TAGROUPCFG]命令，配置跟踪区组。增加用于本功能的TAI集合。
执行[ADD 5GTARSTRNSSAI]命令，配置TA下的RestrictedSnssai，建立 “TAI + S-NSSAI + PLMN ”的映射关系。
配置具体的TA区域和其对应的RestrictedSnssai信息。 
“跟踪区组号”引用自步骤3中配置的跟踪区组类型为“4:切片可用性” 的跟踪区组标识。 
“限制切片信息Profile ID”为步骤2中增加的模板标识。 
###### 基于PLMN的切片选择策略 
执行[SET PLMNSNSSAIPLY]命令，配置PLMN粒度切片策略，包括：
AMF是否支持PLMN粒度切片功能 
AMF是否支持NRF注册携带PLMN粒度切片 
AMF是否支持NRF查询携带PLMN粒度切片 
执行[ADD PLMNCFG]命令，配置PLMN。
执行[ADD PLMNAMFSNSSAI]命令，配置PLMN粒度切片，增加基于PLMNID的切片信息。
执行[SET 5GSLICEAVAILPLY]命令，配置切片可用性策略。
执行[ADD 5GSUPIRSTRNSSAI]命令，增加基于SUPI号段的RestrictedSnssai配置，即逐条增加限制切片配置。对于同一个用户SUPI号段，可按规划一个或者多个限制的 “切片S-NSSNAI” 。
#### 配置实例一（基于TA的切片选择策略） 
场景说明 :场景描述|说明
---|---
非漫游用户注册接受下发AllowedNssai。|非漫游用户初始注册，下发AllowedNssai时，不对“TA下RestrictedSnssai配置”里的配置记录做限制过滤。
漫游用户注册接受下发AllowedNssai。|漫游用户初始注册，下发AllowedNssai时，需要依次对“TA下RestrictedSnssai配置”里匹配的配置记录做限制过滤。被限制的S-NSSAI，不可以在AllowedNssai中携带。
非漫游用户注册接受分配注册区域。|非漫游用户注册更新，分配注册区域时， 不对“TA下RestrictedSnssai配置"里的TA做剔除。
漫游用户注册接受分配注册区域。|漫游用户注册更新，分配注册区域时， 需根据已经获取的AllowedNssai，结合“TA下RestrictedSnssai配置"的情况对TA依次做限制过滤。被限制的TAI，不可以在注册区域中携带。
数据规划 :配置名称|参数项|取值
---|---|---
切片可用性策略配置|AMF支持切片可用性功能|是|是|是|是|是
AMF支持向NSSF同步TA下supportedSnssaiList|切片可用性策略配置|是|是|是|是|是
AMF向NSSF订阅切片可用性的有效时长|切片可用性策略配置|3600|3600|3600|3600|3600
RestrictedSnssai模板配置|RestrictedSnssai模板标识|1|1|2|2|3
SST|RestrictedSnssai模板配置|0|2|0|1|1
SD|RestrictedSnssai模板配置|123456|111111|123456|ABCDEF|ABCDEF
移动国家码|RestrictedSnssai模板配置|FFF|460|460|460|460
移动网络码|RestrictedSnssai模板配置|FFF|12|11|12|12
漫游限制标识|RestrictedSnssai模板配置|是|否|否|否|否
跟踪区组配置|跟踪区组标识|1|-|2|-|3
移动国家码|跟踪区组配置|460|-|460|-|460
移动网络码|跟踪区组配置|11|-|11|-|11
跟踪区码|跟踪区组配置|100001|-|100002|-|100003
跟踪区码起始|跟踪区组配置|000000|-|000000|-|000000
跟踪区码终止|跟踪区组配置|000000|-|000000|-|000000
跟踪区组类型|跟踪区组配置|SLICEAVAILABILITY|-|SLICEAVAILABILITY|-|SLICEAVAILABILITY
别名|跟踪区组配置|tagroup1|-|tagroup2|-|tagroup3
TA下RestrictedSnssai配置|跟踪区组号|1|-|2|-|3
限制切片信息Profile ID|TA下RestrictedSnssai配置|1|-|2|-|3
别名|TA下RestrictedSnssai配置|tanssai1|-|tanssai2|-|tanssai3
配置步骤 :步骤|说明|操作
---|---|---
1|配置切片可用性策略。|SET 5GSLICEAVAILPLY:IFSLICEAVAIL="YES",IFUPDTASPRTSLICE="YES",EXPIRYTIME=3600
2|添加多条RestrictedSnssai模板。|ADD RSTRNSSAI:PROFILEID=1,SST="0",SD="123456",MCC="FFF",MNC="FFF",ROAMRESTR="YES"ADD RSTRNSSAI:PROFILEID=1,SST="2",SD="111111",MCC="460",MNC="12",ROAMRESTR="NO"ADD RSTRNSSAI:PROFILEID=2,SST="0",SD="123456",MCC="460",MNC="11",ROAMRESTR="NO"ADD RSTRNSSAI:PROFILEID=2,SST="1",SD="ABCDEF",MCC="460",MNC="12",ROAMRESTR="NO"ADD RSTRNSSAI:PROFILEID=3,SST="1",SD="ABCDEF",MCC="460",MNC="12",ROAMRESTR="NO"
3|增加切片可用性类型的跟踪区组。|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="11",TAC="100001",TACST="000000",TACEND="000000",TAGRPTYPE="SLICEAVAILABILITY",ALIAS="tagroup1"ADD TAGROUPCFG:TAGROUPID=2,MCC="460",MNC="11",TAC="100002",TACST="000000",TACEND="000000",TAGRPTYPE="SLICEAVAILABILITY",ALIAS="tagroup2"ADD TAGROUPCFG:TAGROUPID=3,MCC="460",MNC="11",TAC="100003",TACST="000000",TACEND="000000",TAGRPTYPE="SLICEAVAILABILITY",ALIAS="tagroup3"
4|增加TA下RestrictedSnssai。|ADD 5GTARSTRNSSAI:TAGRPID=1,RSTRNSSAI=1,ALIAS="tanssai1"ADD 5GTARSTRNSSAI:TAGRPID=2,RSTRNSSAI=2,ALIAS="tanssai2"ADD 5GTARSTRNSSAI:TAGRPID=3,RSTRNSSAI=3,ALIAS="tanssai3"
经过上述四个配置步骤，最终会生成5条“TAI+切片+PLMN”的对应关系："460-11-100001" +"0-123456" +"FFF-FFF""460-11-100001" +"2-111111" +460-12""460-11-100002" +"0-123456" +460-11""460-11-100002" +"1-ABCDEF" +460-12""460-11-100003" +"1-ABCDEF" +460-12"漫游用户注册接受下发AllowedNssai及分配TAIlist（注册区域）时，将按功能逻辑过滤及筛选对应的切片或TA。|经过上述四个配置步骤，最终会生成5条“TAI+切片+PLMN”的对应关系："460-11-100001" +"0-123456" +"FFF-FFF""460-11-100001" +"2-111111" +460-12""460-11-100002" +"0-123456" +460-11""460-11-100002" +"1-ABCDEF" +460-12""460-11-100003" +"1-ABCDEF" +460-12"漫游用户注册接受下发AllowedNssai及分配TAIlist（注册区域）时，将按功能逻辑过滤及筛选对应的切片或TA。|经过上述四个配置步骤，最终会生成5条“TAI+切片+PLMN”的对应关系："460-11-100001" +"0-123456" +"FFF-FFF""460-11-100001" +"2-111111" +460-12""460-11-100002" +"0-123456" +460-11""460-11-100002" +"1-ABCDEF" +460-12""460-11-100003" +"1-ABCDEF" +460-12"漫游用户注册接受下发AllowedNssai及分配TAIlist（注册区域）时，将按功能逻辑过滤及筛选对应的切片或TA。
#### 配置实例二（基于PLMN的切片选择策略） 
场景说明 :场景描述|说明
---|---
AMF支持NRF注册携带PLMN粒度切片|NRF发送注册或者更新请求时，需要携带PLMN粒度切片、携带切片的个数。
AMF支持NRF查询携带PLMN粒度切片|NRF发送发现请求时，需要携带PLMN粒度切片、携带切片的个数。
AMF基于当前PLMN支持的切片决策用户Allowed NSSAI|开启PLMN粒度切片功能时，优先看AMF在对应的PLMN下支持哪些切片。
数据规划 :配置名称|参数项|取值
---|---|---
支持PLMN粒度切片策略配置|是否支持PLMN粒度切片|是|是|是
是否支持PLMN粒度Configured NSSAI|支持PLMN粒度切片策略配置|否|否|否
NF注册更新请求中是否携带PLMN粒度切片|支持PLMN粒度切片策略配置|是|是|是
NF发现请求中是否携带PLMN粒度切片|支持PLMN粒度切片策略配置|是|是|是
NF注册更新请求中携带的每PLMN切片列表中PLMN最大个数|支持PLMN粒度切片策略配置|12|12|12
NF注册更新请求中携带的每PLMN切片列表中每个PLMN下支持的切片的最大个数|支持PLMN粒度切片策略配置|1024|1024|1024
NF发现请求中携带的每PLMN切片列表中PLMN最大个数|支持PLMN粒度切片策略配置|12|12|12
NF发现请求中携带的每PLMN切片列表中每个PLMN下支持的切片的最大个数|支持PLMN粒度切片策略配置|1024|1024|1024
NF注册更新请求中是否携带sNssais|支持PLMN粒度切片策略配置|是|是|是
NF发现请求中是否携带requester-snssais|支持PLMN粒度切片策略配置|是|是|是
是否支持PLMN粒度NSSAI Inclusion Mode|支持PLMN粒度切片策略配置|否|否|否
告警附加信息中是否携带PLMN粒度切片|支持PLMN粒度切片策略配置|否|否|否
NF发现请求消息携带的PLMN粒度切片是否支持SD Range|支持PLMN粒度切片策略配置|否|否|否
基于PLMN的AMF支持的SNSSAI配置|移动国家码|460|460|460
移动网络码|基于PLMN的AMF支持的SNSSAI配置|11|11|11
SNSSAI标识|基于PLMN的AMF支持的SNSSAI配置|10|11|12
SST|基于PLMN的AMF支持的SNSSAI配置|eMBB|eMBB|eMBB
SD|基于PLMN的AMF支持的SNSSAI配置|123456|111111|222222
新增PLMN配置|PLMN标识|1|1|1
移动国家码|新增PLMN配置|460|460|460
移动网络码|新增PLMN配置|11|11|11
切片可用性策略配置|AMF支持切片可用性功能|是|是|是
基于SUPI号段的RestrictedSnssai配置|SUPI号段|46002|46002|46002
SST|基于SUPI号段的RestrictedSnssai配置|eMBB|eMBB|eMBB
SD|基于SUPI号段的RestrictedSnssai配置|111111|111111|111111
配置步骤 :步骤|说明|操作
---|---|---
1|打开支持PLMN粒度切片策略配置。|SET PLMNSNSSAIPLY:supPlmnGrdSlice="ISVALID",supPlmnCfgNssai="INVALID",carryPlmnSlcInNFReg="ISVALID",carryPlmnSlcInNFDis="ISVALID",maxPlmnNumInReg=12,maxSlcNumPerPlmnReg=1024,maxPlmnNumInDis=12,maxSlcNumPerPlmnDis=1024,carrySnssaisInReg="ISVALID",carrySnssaisInDis="ISVALID",supPlmnNssaiIncMode="INVALID",carryPlmnSlcInAlarm="INVALID",ifSdrangeInDis="INVALID"
2|添加三条基于PLMN的AMF支持的SNSSAI配置。|ADD PLMNAMFSNSSAI:MCC="460",MNC="11",SNSSAINAME="10",SST=eMBB,SD="123456"ADD PLMNAMFSNSSAI:MCC="460",MNC="11",SNSSAINAME="11",SST=eMBB,SD="111111"ADD PLMNAMFSNSSAI:MCC="460",MNC="11",SNSSAINAME="12",SST=eMBB,SD="222222"
3|添加PLMN配置。|ADD PLMNCFG:PLMNID=1,MCC="460",MNC="11"
4|切片可用性策略配置|SET 5GSLICEAVAILPLY:IFSLICEAVAIL="YES"
5|添加基于SUPI号段的RestrictedSnssai配置|ADD 5GSUPIRSTRNSSAI:SUPISEG="46002",SST="eMBB",SD="111111"
经过上述配置步骤，最终NRF注册更新和发现消息中会携带基于PLMN为460和11的SST为eMBB，SD为123456的切片，AMF针对46002漫游用户限制1-111111切片，AMF在PLMN46011下支持三个切片，分别是1-111111,1-222222,1-123456。|经过上述配置步骤，最终NRF注册更新和发现消息中会携带基于PLMN为460和11的SST为eMBB，SD为123456的切片，AMF针对46002漫游用户限制1-111111切片，AMF在PLMN46011下支持三个切片，分别是1-111111,1-222222,1-123456。|经过上述配置步骤，最终NRF注册更新和发现消息中会携带基于PLMN为460和11的SST为eMBB，SD为123456的切片，AMF针对46002漫游用户限制1-111111切片，AMF在PLMN46011下支持三个切片，分别是1-111111,1-222222,1-123456。
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|非漫游用户初始注册下发AllowedNssai
---|---
测试目的|测试非漫游用户初始注册，下发AllowedNssai时，不对“TA下RestrictedSnssai配置 "里的配置记录做限制过滤。
预置条件|按配置实例场景一中的配置步骤1~4完成切片可用性配置。AMF环境运行正常。NgSetUp建立的允许 "TAI---切片“列表里，包含但不限于如下记录：TAI:  "460-11-100001 " + S-NSSAI:  "0-123456 "TAI: "460-11-100001 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100001 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100002 " + S-NSSAI:  "0-123456 "TAI: "460-11-100002 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100002 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100003 " + S-NSSAI:  "0-123456 "TAI: "460-11-100003 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100003 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100004 " + S-NSSAI:  "0-123456 "TAI: "460-11-100004 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100004 " +S-NSSAI:  "2-111111 "
测试过程|用户 "460111234567890“ 从TAI “460-11-100001 "发生初始注册。注册请求携带三个RequestedNSSAI： "0-123456 "、“1-ABCDEF "、 "2-111111 "，且全部在用户签约NSSAI中及AMF配置的NSSAI中存在。
通过准则|AMF给UE下发注册接受消息。注册接受消息中下发的AllowedNssai包含三个S-NSSAI： "0-123456 "、“1-ABCDEF "、 "2-111111 "。
测试结果|–
测试项目|漫游用户初始注册下发AllowedNssai
---|---
测试目的|测试漫游用户初始注册，下发AllowedNssai时，需要依次对“TA下RestrictedSnssai配置 "里匹配的配置记录做限制过滤。被限制的S-NSSAI需要剔除掉，不在AllowedNssai中携带。
预置条件|按配置实例场景一中的配置步骤1~4完成切片可用性配置。AMF环境运行正常。NgSetUp建立的允许 "TAI---切片“列表里，包含但不限于如下记录：TAI: "460-11-100001 " + S-NSSAI:  "0-123456 "TAI: "460-11-100001 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100001 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100002 " + S-NSSAI:  "0-123456 "TAI: "460-11-100002 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100002 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100003 " + S-NSSAI:  "0-123456 "TAI: "460-11-100003 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100003 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100004 " + S-NSSAI:  "0-123456 "TAI: "460-11-100004 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100004 " +S-NSSAI:  "2-111111 "
测试过程|用户 "460121234567890“ 从TAI “460-11-100001 "发生初始注册。注册请求携带三个RequestedNSSAI： "0-123456 "、“1-ABCDEF "、 "2-111111 "，且全部在用户签约NSSAI及AMF配置的NSSAI里。
通过准则|AMF给UE下发注册接受消息。注册接受消息中AllowedNssai仅包含1个S-NSSAI: "1-ABCDEF "。依据配置实例中的配置步骤1~4，TAI匹配的配置记录有两条："460-11-100001 " + "0-123456 " + "FFF-FFF "，配置了漫游限制，因此，该切片对所有的漫游用户都限制，故 "0-123456 "需要被剔除。"460-11-100001 " + "2-111111 " +460-12 ", 对归属PLMN为460-12的漫游用户限制，而用户号码为 "460121234567890“ ，故"2-111111 "需要被剔除。因此，注册接受下发的AllowedNssai仅包含1个S-NSSAI: "1-ABCDEF "。
测试结果|–
测试项目|非漫游用户注册接受分配注册区域
---|---
测试目的|测试非漫游用户注册更新，分配注册区域时， 不对“TA下RestrictedSnssai配置 "里的配置记录做TAI剔除。
预置条件|按配置实例场景一中的配置步骤1~4完成切片可用性配置。AMF环境运行正常。NgSetUp建立的允许 "TAI---切片“列表里，包含但不限于如下记录：TAI:  "460-11-100001 " + S-NSSAI:  "0-123456 "TAI: "460-11-100001 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100001 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100002 " + S-NSSAI:  "0-123456 "TAI: "460-11-100002 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100002 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100003 " + S-NSSAI:  "0-123456 "TAI: "460-11-100003 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100003 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100004 " + S-NSSAI:  "0-123456 "TAI: "460-11-100004 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100004 " +S-NSSAI:  "2-111111 "TAI: "460-11-100001 "、 "460-11-100002 "、 "460-11-100003 "、 "460-11-100004 " 均在 "TA配置 "中配置，且在“注册区域配置“中均关联同一 "注册区域ID“。
测试过程|用户 "460111234567890“ 从TAI “460-11-100001 "发生初始注册。注册请求携带三个RequestedNSSAI： "0-123456 "、“1-ABCDEF "、 "2-111111 "，且全部在用户签约NSSAI及AMF配置的NSSAI里。
通过准则|AMF给UE下发注册接受消息。注册接受分配的注册区域包含包括当前TAI在内的四个TAI：  "460-11-100001 "、  "460-11-100002 "、  "460-11-100003 "、 "460-11-100004 "。
测试结果|–
测试项目|漫游用户注册接受分配注册区域
---|---
测试目的|测试漫游用户注册更新，分配注册区域时， 需根据已经获取的AllowedNssai，结合“TA下RestrictedSnssai配置 "的情况对TA依次做限制过滤。被限制的TAI，不可以在注册区域中携带。
预置条件|按配置实例场景一中的配置步骤1~4完成切片可用性配置。AMF环境运行正常。NgSetUp建立的允许 "TAI---切片“列表里，包含但不限于如下12条记录：TAI:  "460-11-100001 " + S-NSSAI:  "0-123456 "TAI: "460-11-100001 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100001 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100002 " + S-NSSAI:  "0-123456 "TAI: "460-11-100002 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100002 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100003 " + S-NSSAI:  "0-123456 "TAI: "460-11-100003 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100003 " +S-NSSAI:  "2-111111 "TAI:  "460-11-100004 " + S-NSSAI:  "0-123456 "TAI: "460-11-100004 " + S-NSSAI:  "1-ABCDEF " + TAI: "460-11-100004 " +S-NSSAI:  "2-111111 "TAI: "460-11-100001 "、 "460-11-100002 "、 "460-11-100003 "、 "460-11-100004 " 均在 "TA配置 "中配置，且在“注册区域配置“中均关联同一 "注册区域ID“。
测试过程|用户 "460121234567890“ 从TAI “460-11-100001 "发生初始注册。注册请求携带三个RequestedNSSAI： "0-123456 "、“1-ABCDEF "、 "2-111111 "，且全部在用户签约NSSAI及AMF配置的NSSAI里。
通过准则|AMF给UE下发注册接受消息。注册接受分配的注册区域包含两个TAI：当前TA  "460-11-100001 "及TAI： "460-11-100004 "。依据配置实例中的配置步骤1~4的配置数据，及测试用例2的测试结果为 注册接受下发的AllowedNssai仅包含1个S-NSSAI: "1-ABCDEF"，一次对四个TAI做剔除判断："460-11-100001 "： 为当前TAI，下发注册区域必须携带。"460-11-100002 " ：依据配置 "460-11-100002 " + "1-ABCDEF " +460-12 "， 460-12的漫游用户在此TA 下的S-NSSAI: "1-ABCDEF "中受限，因此， "460-11-100002"需剔除。"460-11-100003 " ：依据配置 "460-11-100003 " + "1-ABCDEF " +460-12 "， 460-12的漫游用户在此TA 下的S-NSSAI: "1-ABCDEF "中受限，因此， "460-11-100003"需剔除。"460-11-100004 " ：配置中并没有此TA的切片限制配置，即没有明确指示S-NSSAI: "1-ABCDEF "在此TA下受限，无需在注册区域中剔除。因此，注册接受分配的注册区域仅包含当前TA "460-11-100001 "及TAI： "460-11-100004 " 共两个TAI。
测试结果|–
测试项目|AMF是否支持NRF注册携带PLMN维度切片
---|---
测试目的|测试NRF注册更新消息是否携带PLMN维度切片。
预置条件|按配置实例场景二中的配置步骤1~3完成相关配置。AMF环境运行正常。
测试过程|AMF触发NRF注册或者更新。
通过准则|AMF向NRF发送NRF注册消息或更新消息。NRF注册消息或更新消息中携带perPlmnSnssaiList字段，字段中包含一个PLMN维度切片，该PLMN维度切片的plmnId为"460-11"，并且plmnId对应"1-111111"，"1-123456"，"1-222222"这三个切片。
测试结果|–
测试项目|AMF是否支持NRF发现携带PLMN维度切片
---|---
测试目的|测试NRF发现消息是否携带PLMN维度切片。
预置条件|按配置实例场景二中的配置步骤1~3完成相关配置。AMF环境运行正常。
测试过程|AMF触发NRF发现。
通过准则|AMF向NRF发送NRF发现消息。NRF发现消息中携带requester-plmn-specific-snssai-list字段，字段中包含一个PLMN维度切片，该PLMN维度切片的plmnId为"460-11"，并且plmnId对应"1-111111"，"1-123456"，"1-222222"这三个切片。
测试结果|–
测试项目|本地协商AllowedNssai-结合基于用户号段配置切片限制策略
---|---
测试目的|本地协商AllowedNssai采用了plmn支持的切片粒度，并且剔除了限制的切片。
预置条件|按配置实例场景二中的配置步骤1~5完成相关配置。AMF环境运行正常。
测试过程|46002漫游用户进行正常的注册流程。其中：用户的注册请求携带了1-111111、1-222222、1-333333、1-123456四个切片。用户签约了1-111111、1-222222、1-123456三个切片。
通过准则|AMF不和NSSF进行切片选择消息交互，本局直接提供服务。AMF给UE下发注册接受消息中，allowedNssai字段包括两个切片，1-222222和1-123456。AMF给UE下发注册接受消息中，rejectNssai字段包括两个切片，1-333333和1-111111，其中1-333333是PLMN拒绝的切片，1-111111是TA拒绝的切片。
测试结果|–
常见问题处理 :无。 
## ZUF-79-09-004 4G/5G互操作场景下的切片增强 
特性描述 :特性描述 :描述 :定义 :切片增强是指在用户从4G网络移动到5G网络的过程中，当默认的V-SMF/I-SMF或初始选择的AMF，无法继续为用户提供服务时，需要执行V-SMF/I-SMF重选或AMF重定向，来选择合适的V-SMF/I-SMF或AMF，继续为该用户提供服务。 
ZXUN uMAC支持UE从4G移动到5G过程中，重新选择V-SMF/I-SMF和AMF，从而保证用户移动到5G网络后，业务不中断。 
背景知识 :当具备4/5G能力的终端激活会话时，SMF+PGW-C为该会话关联一个切片，并通过响应消息中的PCO信元传递给终端，如下图所示。 
当用户从4G覆盖的区域移动到5G覆盖，或者在4G完成语音呼叫后，触发用户从4G移动到5G，移动到5G的方式可以是切换或者重选，如下图所示。 
重选方式下，终端根据已激活会话关联的切片，生成请求切片，基站根据终端提供的请求切片选择接入的AMF。若终端不支持切片，或者终端提供给基站的请求切片不正确，则基站选择接入的AMF无法保证支持所有已激活会话的切片，导致释放不支持切片所关联的会话，从而引起用户从4G移动到5G时业务中断，无法保证业务的连续性。 
切换方式下，MME依据源4G基站提供的目标位置信息，查询到目标AMF信息，但是选择的目标AMF无法保证支持所有已激活会话的切片，和重选方式类似，此时也无法保证用户从4G移动到5G的业务连续性。 
无论重选或者切换方式下，当用户接入为HR漫游接入时，AMF依据本地配置的互操作切片，为用户选择默认V-SMF。当用户非漫游接入或LBO漫游接入且当前位置超出SMF+PGW-C服务区域时，AMF依据本地配置的互操作切片，为用户选择默认I-SMF。但是本地配置的互操作切片，无法保证PDU会话所关联的切片一致。
应用场景 :本特性适用于如下场景。 
场景1：用户以切换方式从4G移动到5G 
场景2：HR漫游，存在默认V-SMF 
场景3：非漫游或者LBO漫游，存在默认I-SMF 
###### 场景1：用户以切换方式从4G移动到5G 
切换方式下用户从4G移动到5G，MME根据源基站切换请求消息中携带的目标位置，选择目标AMF。目标AMF判断不支持已激活会话的切片时，启用本特性，在切换准备阶段，执行AMF重选，如下图所示。 

###### 场景2：HR漫游，存在默认V-SMF 
HR漫游场景下，用户从4G移动到5G，AMF根据本地配置的互操作切片选择默认V-SMF。AMF收到H-SMF返回的归属网络切片后，得到映射的服务网络切片，并且AMF判断该切片与本地网络配置的互操作切片不一致时，启用本特性。 
当默认V-SMF不支持映射的切片时，AMF基于映射的切片重新选择V-SMF，触发V-SMF变更流程，如下图所示。 
当默认V-SMF支持映射的切片时，AMF通知默认V-SMF更新切片，如下图所示。 

###### 场景3：非漫游或者LBO漫游，存在默认I-SMF 
用户非漫游或者LBO漫游时，用户当前位置超出了SMF+PGW-C管理区域，则在4G移动到5G过程中，AMF根据本地配置的互操作切片，选择默认I-SMF。AMF收到A-SMF返回会话所归属的切片，判断本地配置的互操作切片与会话所归属的切片不一致，且默认I-SMF不支持会话所归属的切片，则启用本特性。AMF根据A-SMF返回的会话归属切片，重新选择I-SMF，触发I-SMF变更流程，如下图所示。 

客户收益 :受益方|受益描述
---|---
运营商|增强4/5G互操作时业务连续性，提升网络服务质量。
移动用户|该特性对用户不可见。
实现原理 :系统架构 :本特性涉及的系统架构图如[图1]、[图2]所示。
图1  HR漫游场景下系统架构图

图2  非漫游或LBO漫游场景下系统架构

涉及的网元 :网元名称|网元作用
---|---
UE|支持4G/5G接入。支持有N26接口或/和无N26接口的互操作。在4G和5G下移动时可保持用户IP不变。
NG-RAN|用户从4G重选到5G时，选择接入的AMF。
AMF|支持用户从4G移动到5G。支持用户从4G移动到5G的过程中，AMF重定向。支持用户从4G移动到5G的过程中，执行V-SMF/I-SMF重选。归属地漫游场景下，支持4G移动到5G过程中，通知V-SMF更新切片。
V-SMF/I-SMF|支持会话管理。
MME|支持用户从4G移动到5G。用户从4G切换到5G时，选择Target AMF。
SMF+PGW-C|作为用户从4G移动到5G过程中的会话锚点。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
N14|ZUF-79-19-006 N14
N22|ZUF-79-19-008 N22
N26|ZUF-79-19-009 N26
本网元实现 :本特性需要AMF与NSSF、SMF等NF交互配合完成如下功能。 
支持用户以重选或者切换方式，从4G移动到5G。 
支持用户从4G移动到5G过程中，AMF重选。 
支持用户从4G重选到5G过程中，V-SMF/I-SMF重选。 
支持用户从4G切换到5G过程中，V-SMF/I-SMF重选。 
支持用户从4G移动到5G过程中，归属地漫游场景下，通知V-SMF更新会话关联归属地切片所映射的服务网络切片。 
业务流程 :本特性涉及如下业务流程。 
 说明： 
目前仅支持： 
4G切换到5G，AMF重选。 
4G重选到5G，V-SMF/I-SMF重选。 
4G切换到5G，AMF重选。 
4G重选到5G，V-SMF/I-SMF重选。 
4G切换到5G，V-SMF/I-SMF重选。 
4G重选到5G，更新V-SMF会话切片信息。 
4G切换到5G，更新V-SMF会话切片信息。 
4G切换到5G，AMF重选
4G切换到5G，AMF重选流程如[图3]所示。
图3  4G切换到5G，AMF重选流程

用户接入EPC系统。 
eNodeB检测到用户需要切换到5G，发送Handover Required消息给MME，携带目标gNB的Target ID。 
MME根据Target ID查询DNS得到Initial AMF的地址，通过N26接口发送Forward Relocation Request，携带用户移动和会话上下文信息。 
Initial AMF根据MME携带的PGW FQDN，查询到SMF+PGW-C地址信息，发送Nsmf_PDUSession_CreateSMContext Request消息给SMF+PGW-C，通知SMF+PGW-C用户准备切换到5G。 
SMF+PGW-C处理成功后，回复Nsmf_PDUSession_CreateSMContext Response给Initial AMF，并携带该PDU会话的SNSSAI。 
Initial AMF判断本局不能全部支持SMF+PGW-C返回的SNSSAI，则启动AMF重选过程。Initial AMF发送Nudm_SDM_Get Request给UDM，请求用户签约切片信息。 
UDM回复Nudm_SDM_Get Response，携带用户签约切片信息。 
Initial AMF触发NSSF切片选择过程，发送Nnssf_NSSelection_Get Request给NSSF，其中携带的requestedNssai信元中包含SMF+PGW-C返回的PDU会话的SNSSAI。 
NSSF执行切片选择，回复Nnssf_NSSelection_Get Response给Initial AMF，携带Allowed NSSAI以及待选择的AMF列表。 
Initial AMF判断本AMF不在待选择的AMF列表中，触发AMF重选。从NSSF返回的待选择AMF列表中，选择一个Target AMF，发送Namf_Communication_RelocateUEContext Request给Target AMF，携带PDU会话上下文、MM上下文、Target ID等信息。 
Target AMF发送Handover Request给gNB。 
gNB回复Handover Request Acknowledge，携带需要AMF透传给SMF+PGW-C的N2 SM Information； 
Target AMF发送Nsmf_PDUSession_UpdateSMContext Request给SMF+PGW-C，携带gNB回复的N2 SM Information、GUAMI等信息。 
SMF+PGW-C处理成功后，回复Nsmf_PDUSession_UpdateSMContext Response给Target AMF。 
Target AMF回复Namf_Communication_RelocateUEContext Response给Initial AMF，Initial AMF终止切换流程。 
Target AMF通过N26接口回复Forward Relocation Response给MME。 
继续后续的4G到5G切换流程。 
4G重选到5G，V-SMF/I-SMF重选流程
4G重选到5G，V-SMF/I-SMF重选流程如[图4]所示。
图4  4G重选到5G，V-SMF/I-SMF重选流程

终端处于空闲态模式，在用户从4G覆盖进入5G覆盖等场景下，发送Registration Request给AMF，携带4G GUTI映射的5G GUTI、TAU Request等信息。 
AMF根据映射的5G GUTI查找到老局MME，并从老局MME获取用户上下文，包括安全上下文、会话上下文等信息。 
AMF获取互操作切片，支持直接取本地配置的互操作切片，或者根据会话所归属的DNN、用户签约切片信息以及本地配置的互操作切片进行推导。当采用推导方式时，其推导策略如下： 
根据会话所使用的DNN以及用户签约切片信息，获取本会话对应的可能切片集合。 
若注册请求消息中携带了请求切片，则与步骤a取交集，如果交集包含有多个切片，则优选默认切片；若与步骤a的切片集合交集为空，则执行步骤c。 
注册请求中未携带请求切片，则选取该会话所使用DNN的签约默认切片，如果存在多个，则选择第一个；若无默认切片，则取该PDU会话DNN的普通切片，如果存在多个，则选择第一个。 
若会话所使用的DNN无签约切片，则直接取本地配置的互操作切片。 
AMF根据步骤3获取的互操作切片，向NSSF以及NRF查询得到默认V-SMF/I-SMF信息。 
AMF发送Nsmf_PDUSession_CreateSMContext Request给默认V-SMF/I-SMF，携带互操作切片，以及MME返回的EPS PDN Connection。 
默认V-SMF/I-SMF发送Nsmf_PDUSession_Create Request给SMF+PGW-C，消息中包含该会话的EPS承载信息。 
SMF+PGW-C返回Nsmf_PDUSession_Create Response，携带PDU Session ID以及该PDU会话所归属的切片。 
默认V-SMF/I-SMF返回Nsmf_PDUSession_CreateSMContext Response响应给AMF，携带PDU Session ID以及该PDU会话所归属的切片。 
AMF判断默认V-SMF/I-SMF不支持SMF+PGW-C返回的PDU会话归属切片，则根据TAI、会话归属切片等信息，重新选择V-SMF/I-SMF。 
AMF发送Nsmf_PDUSession_CreateSMContext Request给新选择的V-SMF/I-SMF，携带PDU Session ID以及会话归属切片，对于归属地漫游场景，会话归属切片为SMF+PGW-C返回切片在服务网络中映射的切片。 
新V-SMF/I-SMF与默认V-SMF/I-SMF、SMF+PGW-C交互，将会话由默认V-SMF/I-SMF切换到新V-SMF/I-SMF。 
新V-SMF/I-SMF返回Nsmf_PDUSession_CreateSMContext Response响应给AMF。 
继续4G重选到5G后续流程。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准编号|标准名称
---|---
3GPP TS 23.501|System Architecture for the 5G System
3GPP TS 23.502|Procedures for the 5G System
3GPP TS 24.501|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
3GPP TS 29.274|Tunnelling Protocol for Control plane (GTPv2-C); Stage 3
3GPP TS 29.502|Session Management Services; Stage 3
3GPP TS 29.531|Network Slice Selection Services; Stage 3
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
03|V7.22.20|新增AMF切片重定向功能。
02|V7.21.40|新增4G切换到5G，AMF重选流程。
01|V7.21.20|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|SMF|NSSF
---|---|---
-|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令|修改参数
---|---|---
AMF互操作配置|SET 5GINTERWORKCFG|新增参数“支持空闲态模式下4G移动5G时V-SMF或I-SMF重选”、"空闲态模式下互操作S-NSSAI获取策略"、”支持4G到5G切换过程中AMF重选“、”支持4G到5G切换过程中本地切片选择“。
性能统计 :测量项|描述
---|---
N14接口测量|新增编号为C510550054~C510550067的计数器
4/5G切换分NF测量|新增计数器C510320026 4G到5G切入失败次数(重定向目标AMF原因)
基于TA4/5G切换分NF测量|新增计数器C511060028 4G到5G切入失败次数(重定向目标AMF原因)
基于TA组4/5G切换分NF测量|新增计数器C512580028 4G到5G切入失败次数(重定向目标AMF原因)
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过相关配置，实现以下功能。 
4G到5G的切换流程中，目标AMF判断不支持已激活会话的切片时，可以配置是否支持重选AMF、以及本地切片选择。切换过程中源基站由于某些原因取消切换，若已经发生了AMF重定向，源局可以向目标局发起切换取消流程。 
4G到5G的注册更新过程中，当在4G上存在PDU会话时，用户移动到5G会进行会话恢复，可以根据签约的DNN信息、签约的切片信息以及会话具体的DNN信息，智能推导出建立会话需要的切片。 
4G到5G的注册更新过程中，当在4G上存在PDU会话时，用户移动到5G会进行会话恢复，此时可能会进行I-SMF或者V-SMF建立（已有功能）。但是AMF和I-SMF或者V-SMF交互时，I-SMF或者V-SMF的响应消息中携带的切片和AMF向SMF发送请求中的切片不一致时，需要进行I-SMF或者V-SMF重选。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
配置过程 :执行命令[SET 5GINTERWORKCFG]，开启I-SMF/V-SMF重选、切片智能推导、4G到5G切换过程中AMF重选和4G到5G切换过程中本地切片选择功能。
配置实例 :场景一 :场景说明
用户在从4G网络到5G网络的切换流程中，支持重选AMF。 
数据规划
配置项|参数|取值
---|---|---
修改AMF互操作配置|支持4G到5G切换过程中AMF重选|是
支持4G到5G切换过程中本地切片选择|修改AMF互操作配置|是
配置步骤
步骤|说明|操作
---|---|---
1|配置支持4G到5G切换过程中AMF重选，并且支持4G到5G切换过程中本地切片选择。|SET 5GINTERWORKCFG:AMFREALLOCIN4TO5HO="YES",LOCALSLICESEIN4TO5HO="YES"
场景二 :场景说明
HR漫游用户，进行4G到5G的注册更新，存在V-SMF。 
数据规划
配置项|参数|取值
---|---|---
修改AMF互操作配置|支持空闲态模式下4G移动5G时V-SMF或I-SMF重选|支持
空闲态模式下互操作S-NSSAI获取策略|修改AMF互操作配置|智能推导
配置步骤
步骤|说明|操作
---|---|---
1|配置支持空闲态模式下4G移动5G时V-SMF或I-SMF重选，并且空闲态模式下互操作S-NSSAI获取策略是智能推导。|SET 5GINTERWORKCFG:SUPIVSMFRESELIDLE="SPRT",IDLEIWKSNSSAIPLY="INTELLIGENTDEDUCTION"
场景三 :场景说明
非漫游或者LBO用户，进行4G到5G的注册更新，存在默认I-SMF。 
数据规划
配置项|参数|取值
---|---|---
AMF互操作配置|支持空闲态模式下4G移动5G时V-SMF或I-SMF重选|支持
空闲态模式下互操作S-NSSAI获取策略|AMF互操作配置|智能推导
配置步骤
步骤|说明|操作
---|---|---
1|配置支持空闲态模式下4G移动5G时V-SMF或I-SMF重选，并且空闲态模式下互操作S-NSSAI获取策略是智能推导。|SET 5GINTERWORKCFG:SUPIVSMFRESELIDLE="SPRT",IDLEIWKSNSSAIPLY="INTELLIGENTDEDUCTION"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|4G到5G的切换流程中AMF重定向以及取消(场景一)
---|---
测试目的|4G到5G的切换流程中，目标AMF判断不支持已激活会话的切片时，支持重选AMF。
预置条件|“AMF支持N26互操作功能”License项已打开。设置AMF互操作配置，支持4G到5G切换过程中AMF重选，支持4G到5G切换过程中本地切片选择。切换过程中源基站由于某些原因取消切换。
测试过程|4G到5G的切换流程中，SMF响应后获取请求的切片，所有的PDU请求切片被UDM部分签约，或者目标AMF部分支持。
通过准则|发生AMF重定向，目标AMF选取了新的AMF。选取的新AMF继续为用户服务。MME通知源AMF切换取消，源AMF通知重定向的目标AMF切换取消。
测试结果|–
测试项目|V-SMF的会话重建（场景二）
---|---
测试目的|4G到5G的注册更新过程中，当需要恢复V-SMF的会话时，可以智能推导出创建会话需要的切片，并且根据NRF响应结果，进行V-SMF的重选流程。
预置条件|配置支持空闲态模式下4G移动5G时V-SMF或I-SMF重选，并且空闲态模式下互操作S-NSSAI获取策略是智能推导。设置互操作的SNSSAI配置，SSD为"MIoT"，SD为"NULL"。
测试过程|漫游用户触发4G到5G的注册更新流程。注册更新流程中，注册请求携带切片s1，AMF向NSSF获取签约信息时，得到用户签约的切片s1，并且DNN1的默认切片包含切片s1，待建立会话的DNN信息为DNN1。AMF用推导出的切片s1与V-SMF交互时，V-SMF的响应提示会话建立需要切片s2。
通过准则|AMF智能推导出切片s1，AMF向V-SMF发送PDU会话建立请求消息时携带切片s1。AMF触发V-SMF重选流程，根据新的NRF响应，进行会话的重建或更新。
测试结果|–
测试项目|I-SMF的会话重建(场景三)
---|---
测试目的|4G到5G的注册更新过程中，当需要恢复I-SMF的会话时，可以智能推导出创建会话需要的切片，并且根据NRF响应结果，进行I-SMF的重选流程。
预置条件|配置支持空闲态模式下4G移动5G时V-SMF或I-SMF重选，并且空闲态模式下互操作S-NSSAI获取策略是智能推导。设置互操作的SNSSAI配置，SSD为"MIoT"，SD为"NULL"。
测试过程|非漫游用户或者LBO漫游用户触发4G到5G的注册更新流程。注册更新流程中，注册请求携带切片s1，AMF向NSSF要签约信息时，得到用户签约的切片s1，并且DNN1的默认切片包含切片s1，待建立会话的DNN信息为DNN1。AMF用推导出的切片s1与I-SMF交互时，I-SMF的响应提示会话建立需要切片s2。
通过准则|AMF智能推导出切片s1，向I-SMF发送会话建立请求消息时携带切片s1。AMF触发I-SMF的重选流程，根据新的NRF响应，进行会话的重建或更新。
测试结果|–
常见问题处理 :无。 
## ZUF-79-09-005 PDU会话建立切片选择 
特性描述 :特性描述 :描述 :定义 :PDU会话建立切片选择是指UE发起PDU会话建立流程时，AMF对UE是否携带S-NSSAI进行判断，如果UE未携带S-NSSAI，或者携带的S-NSSAI不在Allowed NSSAI范围内时，则为PDU会话建立选择合适的S-NSSAI。 
背景知识 :5G网络需要承载多类型的业务场景，不再使用一张网络提供服务，而是利用网络切片技术，在同一套硬件基础设施上按需切分出多个虚拟的端到端逻辑网络，适配各类服务的不同特征及需求，并且每个网络切片在逻辑上隔离。网络切片是一个完整的逻辑网络，包含一系列能够提供一定网络能力和网络特性的网络功能和相应资源。 
UE发起注册时，5GC为UE确定Allowed NSSAI、Configured NSSAI和Rejected NSSAI，选择支持Allowed NSSAI的AMF，并将Allowed NSSAI等信息通知UE和RAN。如果支持URSP，PCF会下发URSP策略给UE，其中包含了NSSP（Network Slice Selection Policy，网络切片选择策略）。
UE发起PDU会话建立流程时，如果根据APP的信息在NSSP（Network Slice Selection Policy，网络切片选择策略）中选择到合适的S-NSSAI，则携带S-NSSAI；如果无法获取NSSP，则不携带S-NSSAI。AMF对UE携带的S-NSSAI进行判断，为PDU会话建立选择合适的S-NSSAI，基于选择的S-NSSAI选择DNN，以及合适的SMF，建立PDU会话。
应用场景 :###### 场景一：UE发起PDU会话建立，携带S-NSSAI 
UE发起PDU会话建立，根据APP的信息在NSSP中选择合适的S-NSSAI并携带，AMF对UE携带的S-NSSAI进行判断，如果不在Allowed NSSAI范围内时，则拒绝PDU会话建立请求。 
###### 场景二：UE发起PDU会话建立，未携带S-NSSAI和DNN 
UE发起PDU会话建立，根据APP的信息未选择到合适的S-NSSAI，未携带S-NSSAI和DNN，AMF选择合适的S-NSSAI，基于选择的S-NSSAI选择DNN，建立PDU会话。 
###### 场景三：UE发起PDU会话建立，未携带S-NSSAI，携带DNN 
UE发起PDU会话建立，根据APP的信息未选择到合适的S-NSSAI，未携带S-NSSAI，但是携带了DNN，AMF基于DNN选择合适的S-NSSAI，建立PDU会话。 
客户收益 :受益方|受益描述
---|---
运营商|为用户灵活选择网络切片，提高服务质量。
移动用户|享受优质的网络服务。
实现原理 :系统架构 :5G系统架构如[图1]所示。
图1  5G系统架构

涉及的网元 :网元名称|网元作用
---|---
AMF|AMF对UE携带的S-NSSAI进行判断，如果UE未携带S-NSSAI，或者携带的S-NSSAI不在Allowed NSSAI范围内，则为PDU会话建立选择合适的S-NSSAI。
UDM|UDM为用户提供签约的默认S-NSSAI。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
本网元实现 :AMF功能
UE请求PDU会话建立流程中，AMF对UE携带的S-NSSAI进行判断，为PDU会话建立选择合适的S-NSSAI。 
AMF基于已选定的S-NSSAI选择DNN，以及合适的SMF，建立PDU会话。 
切片选择策略
场景一：UE携带S-NSSAI，切片选择策略如[图2]所示。
图2  切片选择策略（UE携带S-NSSAI）

AMF判断UE携带的S-NSSAI是否在Allowed NSSAI范围内。 
UE携带的S-NSSAI在Allowed NSSAI范围内，则使用UE携带的S-NSSAI。 
UE携带的S-NSSAI不在Allowed NSSAI范围内，则拒绝PDU会话建立。 
场景二：UE未携带S-NSSAI和DNN，切片选择策略如[图3]所示。
图3  切片选择策略（UE未携带S-NSSAI和DNN）

AMF基于SUPI获取切片选择策略。 
指定切片：如果指定的S-NSSAI在Allowed NSSAI范围内，则使用指定的S-NSSAI；否则，使用“签约切片”策略。 
签约切片：如果Allowed NSSAI内存在签约默认S-NSSAI，则使用签约的默认S-NSSAI；否则，使用签约的非默认S-NSSAI。 
场景三：UE未携带S-NSSAI，携带DNN，切片选择策略如[图4]所示。
图4  UE未携带S-NSSAI携带DNN的切片选择策略

AMF基于SUPI获取切片选择策略。 
指定切片：如果携带的DNN签约在Allowed NSSAI下，且指定的S-NSSAI在DNN签约的切片范围内，则使用指定的S-NSSAI；否则，使用“签约切片”策略。如果携带的DNN未签约在Allowed NSSAI下，且指定的S-NSSAI在Allowed NSSAI范围内，则使用指定的S-NSSAI；否则，使用“签约切片”策略。 
签约切片：如果携带的DNN签约在Allowed NSSAI下，且签约在默认切片下，则使用DNN签约的默认S-NSSAI；否则，使用DNN签约的非默认S-NSSAI。如果携带的DNN未签约在Allowed NSSAI下，且Allowed NSSAI内存在签约默认S-NSSAI，则使用签约的默认S-NSSAI；否则，使用签约的非默认S-NSSAI。 
 说明： 
UE未携带S-NSSAI携带DNN，切片选择时，AMF判断携带的DNN是否签约在Allowed NSSAI下，可以基于本地策略控制是否忽略签约通配。 
UE未携带S-NSSAI携带DNN，基于“签约切片”策略选择切片，AMF判断携带的DNN未签约在Allowed NSSAI下时，可以基于本地策略控制“基于DNN更正策略选择更正后的DNN”及其签约的S-NSSAI，或者基于Allowed NSSAI，先选择S-NSSAI再选择DNN。 
业务流程 :UE发起PDU会话建立请求，切片选择流程如[图5]所示。
图5  PDU会话建立切片选择流程

流程说明： 
UE发起PDU会话建立请求，向AMF发送NAS消息，该消息中包括S-NSSAI、DNN、PDU session ID、Requested PDU Session Type（Request Type）等信息。 
AMF收到UE发起的PDU会话建立请求，对UE携带的S-NSSAI进行判断，执行切片选择。 
UE携带S-NSSAI：如果S-NSSAI在Allowed NSSAI范围内，则使用UE携带的S-NSSAI；否则，拒绝PDU会话建立。 
UE未携带S-NSSAI和DNN：AMF根据用户的SUPI获取切片选择策略，选择S-NSSAI。 
UE未携带S-NSSAI，携带DNN：AMF根据用户的SUPI获取切片选择策略，基于DNN选择S-NSSAI。 
AMF基于已选定的S-NSSAI选择DNN。 
AMF基于已选定的S-NSSAI和DNN选择SMF。 
AMF向SMF发送Nsmf_PDUSession_CreateSMContext Request消息请求创建SM上下文。 
同PDU会话建立现有流程。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
ZUF-79-06-005 DNN更正|UE发起PDU会话建立，未携带S-NSSAI，携带DNN，请求的DNN未签约在任何切片下时，AMF可以基于DNN更正策略获得更正后的DNN签约的切片。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.502（Procedures for the 5G System (5GS)）|4.3.2.2.1 Non-roaming and Roaming with Local Breakout
特性能力 :名称|指标
---|---
切片选择策略配置的最大SUPI号段个数|4096（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.20|首次发布。
License要求 :该特性为ZXUN-uMAC的基本特性，无需License支持。 
对其他网元的要求 :UE|gNodeB|UDM
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
缺省切片选择策略配置|SET DEFAULT SLICE SELECTION POLICY
SHOW DEFAULT SLICE SELECTION POLICY|缺省切片选择策略配置
切片选择策略配置|ADD SLICE SELECTION POLICY
SET SLICE SELECTION POLICY|切片选择策略配置
DEL SLICE SELECTION POLICY|切片选择策略配置
SHOW SLICE SELECTION POLICY|切片选择策略配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过切片选择策略配置，在用户发起PDU会话建立时，选择合适的切片，为用户提供相应的网络资源。 
配置前提 :无。 
配置过程 :执行[SET DEFAULT SLICE SELECTION POLICY]命令，配置缺省切片选择策略。
执行[ADD SLICE SELECTION POLICY]命令，新增切片选择策略配置。
配置实例 :场景说明 :UE发起PDU会话建立，根据APP的信息未选择到合适的S-NSSAI，且未携带S-NSSAI和DNN，AMF选择合适的S-NSSAI，基于选择的S-NSSAI选择DNN，建立PDU会话。 
此配置方法三种场景均适用。 
数据规划 :配置项|参数|取值
---|---|---
缺省切片选择策略配置|缺省切片选择策略|仅签约切片
SST|缺省切片选择策略配置|0
SD|缺省切片选择策略配置|NULL
忽略通配DNN|缺省切片选择策略配置|不忽略
支持基于DNN更正策略选择切片|缺省切片选择策略配置|不支持
切片选择策略配置|SUPI号段|46011123
切片选择策略|切片选择策略配置|指定切片优先
SST|切片选择策略配置|eMBB
SD|切片选择策略配置|010101
忽略通配DNN|切片选择策略配置|忽略
配置步骤 :步骤|说明|操作
---|---|---
1|配置缺省切片选择策略|SET DEFAULT SLICE SELECTION POLICY:SLICESELPOLICY="ONLYSUBSCRIBEDSNSSAI",SST="0",SD="NULL",IGNOREWILDCARD="NOTIGNORE",BASEDNNCORRECT="NO"
2|新增切片选择策略配置|ADD SLICE SELECTION POLICY:SUPI="46011123",SLICESELPOLICY="SPECIFICSNSSAIPRIOR",SST="eMBB",SD="010101",IGNOREWILDCARD="IGNORE"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|UE发起PDU会话建立，携带S-NSSAI
---|---
测试目的|UE发起PDU会话建立，根据APP的信息在NSSP中选择合适的S-NSSAI并携带，AMF对UE携带的S-NSSAI进行判断。
预置条件|系统环境正常。
测试过程|UE发起注册时，AMF和UE协商确定Allowed NSSAI，并把Allowed NSSAI等信息通知给UE。UE发起PDU会话建立时，携带S-NSSAI。
通过准则|AMF对UE携带的S-NSSAI进行判断。如果UE携带的S-NSSAI不在Allowed NSSAI范围内，则AMF拒绝用户的PDU建立请求。如果UE携带的S-NSSAI在Allowed NSSAI范围内，则AMF允许建立PDU会话。
测试结果|–
测试项目|UE发起PDU会话建立，未携带S-NSSAI和DNN
---|---
测试目的|UE发起PDU会话建立，根据APP的信息未选择到合适的S-NSSAI，未携带S-NSSAI和DNN，AMF选择合适的S-NSSAI，基于选择的S-NSSAI选择DNN，建立PDU会话。
预置条件|系统环境正常。根据配置实例，配置缺省切片选择策略和切片选择策略。
测试过程|UE发起注册时，AMF和UE协商确定Allowed NSSAI，并把Allowed NSSAI等信息通知给UE。UE发起PDU会话建立时，未携带S-NSSAI和DNN。
通过准则|对于在切片选择策略配置号段内的用户，如果切片选择策略配置中指定的S-NSSAI在该用户的Allowed NSSAI范围内，则AMF为该用户选择指定的S-NSSAI，否则在Allowed NSSAI内为其选择一个S-NSSAI（优先选择默认S-NSSAI）。对于不在切片选择策略配置号段内的用户，AMF在Allowed NSSAI内为其选择一个S-NSSAI（优先选择默认S-NSSAI）。
测试结果|–
测试项目|UE发起PDU会话建立，未携带S-NSSAI，携带DNN
---|---
测试目的|UE发起PDU会话建立，未携带S-NSSAI，但是携带了DNN，AMF基于DNN选择合适的S-NSSAI，建立PDU会话。
预置条件|系统环境正常。根据配置实例，配置缺省切片选择策略和切片选择策略。
测试过程|UE发起注册时，AMF和UE协商确定Allowed NSSAI，并把Allowed NSSAI等信息通知给UE。UE发起PDU会话建立时，携带DNN，未携带S-NSSAI。
通过准则|对于在切片选择策略配置号段内的用户，如果切片选择策略配置中指定的S-NSSAI和UE携带的DNN与用户签约上下文匹配，则AMF为该用户选择指定的S-NSSAI，否则在用户签约上下文中根据用户携带的DNN为其选择合适的S-NSSAI。对于不在切片选择策略配置号段内的用户，AMF在用户签约上下文中根据用户携带的DNN为其选择合适的S-NSSAI。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## 5G-GUTI 
5G Globally Unique Temporary Identity5G全球唯一临时标识
AMF :Access and Mobility Management Function接入和移动管理功能
DNN :Data Network Name数据网名称
## HR 
Home Routed本地路由
## LBO 
Local Breakout本地路由疏导
NF :Network Function网络功能
NRF :NF Repository Function网络功能仓储
## NSI 
Network Slice Instance网络切片实例
## NSSAI 
Network Slice Selection Assistance Information网络切片选择辅助信息
NSSF :Network Slice Selection Function网络切片选择功能
PCF :Policy Control Function策略控制功能
RAN :Radio Access Network无线接入网
S-NSSAI :Single Network Slice Selection Assistance Information单个网络切片选择辅助信息
## SD 
Slice Differentiator切片差异区分器
## SST 
Slice/Service Type切片/服务类型
TA :Tracking Area跟踪区域
UDM :Unified Data Management统一数据管理
UDR :Unified Data Repository统一数据存储
UE :User Equipment用户设备
## URSP 
UE Route Selection PolicyUE路由选择策略
## eMBB 
Enhanced Mobile Broadband增强移动宽带
## mMTC 
Massive Machine Type Communication海量机器类通信
## URLLC 
Ultra Reliable Low Latency Communication超高可靠超低时延通信
# ZUF-79-10 网络功能发现选择 
## ZUF-79-10-001 SMF选择 
特性描述 :特性描述 :描述 :定义 :SMF选择功能是指AMF为5G用户接入选择建立PDU会话的SMF。 
背景知识 :用户使用不同的切片和数据网络名称连接到不同的SMF，再通过UPF访问不同类型的外部网络。 
SMF是用户会话的锚点，当用户发生移动时，SMF不变，因此SMF一般不会下沉部署。 
作为控制面NF，SMF一般集中部署在中心城市，便于管理，节省控制面交互。如果中心城市部署了多套SMF，则这些SMF组POOL进行容灾，AMF根据用户使用的切片和数据网络名称选择SMF POOL，并根据SMF在POOL内的优先级和权重选择SMF。 
应用场景 :SMF一般部署在中心城市，且会同时部署多个SMF，因此SMF间需要组POOL进行容灾，POOL内负荷分担。AMF选择SMF的典型应用场景如下： 
某地分为2个大区，每个大区内SMF集中部署，各区内的SMF间负荷分担。由于每个大区内SMF较多，所以大区间不需要互相备份，如[图1]所示。
图1  大区内SMF负荷分担组网图

大区1和大区2间没有互备，NRF发现结果如下： 
用户在大区1，基于DNN、切片和TAI信息获取到SMF列表：SMF1、SMF2、SMF3。 
用户在大区2，基于DNN、切片和TAI信息获取到SMF列表：SMF4、SMF5、SMF6。 
用户注册，SMF的选择结果如下： 
用户在大区1下注册，发起PDU会话建立。AMF根据用户切片、DNN和TAI信息选出大区1下SMF POOL：SMF1、SMF2、SMF3。根据POOL内SMF的优先级和权重选择一个SMF。用户移动到大区2，SMF是锚定点，SMF不改变。 
用户在大区2下注册，发起PDU会话建立。AMF根据用户切片、DNN和TAI信息选出大区2下SMF POOL：SMF4、SMF5、SMF6。根据POOL内SMF的优先级和权重选择一个SMF。用户移动到大区1，SMF是锚定点，SMF不改变。 
客户收益 :受益方|受益描述
---|---
运营商|提高业务可靠性：优先级和权重、动态负荷选择等策略提高了业务可靠性。提高策略灵活性：基于SUPI/MSISDN号段选择SMF，提高了策略灵活性。
终端用户|减少数据传输时延，提高终端用户体验，使用户享受优质的网络服务。
实现原理 :系统架构 :该特性涉及的系统架构有三种： 
非漫游场景下，AMF选择本地SMF，系统架构如图2所示。图2  Non-Roaming 5G System architecture 
Local breakout漫游场景下，AMF选择VPLMN的SMF，系统架构如图3所示。图3  Roaming 5G System architecture- local breakout scenario in service-based interface representation 
Home routed漫游场景下，AMF选择HPLMN的SMF，系统架构如图4所示。图4  Roaming 5G System architecture - home routed scenario in service-based interface representation 
涉及的NF/网元 :NF名称|NF作用
---|---
NRF|支持SMF注册，保存SMF注册信息。根据S-NSSAI、PLMN ID、DNN和NSI ID查询匹配的SMF列表，携带发现的SMF实例或SMF服务实例的SMFIP地址的集合，例如FQDN或IP地址，以及与S-NSSAI相对应的所选网络切片实例的NSI ID给AMF。
AMF|查询NRF服务器，获取到SMF列表。根据SMF选择策略对SMF进行选择，确定最终的SMF节点及控制面交互的IP地址。当选择出的SMF节点仅携带FQDN而非IP地址时，AMF可以基于FQDN查询DNS获取到IP地址。
SMF|通知AMF其NF级动态负荷信息。
DNS Server|记录FQDN和SMF IP地址的对应关系，根据FQDN返回查询到的SMF IP地址。
协议栈 :AMF与SMF之间的N11接口协议栈，基于HTTP RESTful服务化接口提供服务，如[图5]所示。
图5  N11接口协议栈

###### 本NF实现 
AMF在通过NRF进行SMF选择的过程中主要实现以下功能： 
AMF查询NRF服务器，获取到SMF列表。 
AMF根据SMF选择策略对SMF进行选择，确定最终的SMF节点及控制面交互的IP地址。 
当选择出的SMF节点仅携带FQDN而非IP地址时，AMF可以基于FQDN查询DNS获取到IP地址。 
SMF选择有多种策略，不同的选择策略对应不同的SMF组网场景，参见[表1]。各选择策略可以组合使用。
选择策略|策略说明|场景
---|---|---
优先级|SMF优先级数值越小，优先级越高，AMF优选高优先级的SMF。|SMF间互相备份。
权重|AMF根据SMF的权重因子，随机选择一个SMF，SMF权重因子的大小，决定其被选择的概率的大小。|SMF间负荷分担。网络中SMF的能力不一致，高能力的SMF配置的权重高，其被选择到的几率大，以达到SMF上的负荷均衡。
动态负荷|SMF网元动态负荷，由SMF向NRF注册时，将动态负荷在NRF保存；AMF进行SMF选择时，NRF给AMF返回各SMF的静态权重和动态负荷。SMF有效负荷的计算公式为：SMF有效负荷=（100-SMF网元动态负荷）%×静态权重。|SMF动态负荷均衡。
SUPI/MSISDN号段|AMF根据SUPI/MSISDN号码或号段选择SMF。|将特定号段的用户选择到指定的SMF上去。
签约smfList|AMF根据签约的smfList选择SMF。|基于用户签约的smfList，将此类用户选择到支持静态IP地址分配的SMF上，为此类用户分配签约的静态IP地址，使其享受指定的服务，比如企业用户定制服务。
locality|locality，即位置信息，表示NF可以服务的物理区域（例如：地理位置、DC等）。SMF在向NRF注册时携带locality。AMF根据locality选择与本地位置或指定位置相同的SMF。具体策略详细说明参见表2。|SMF跨DC负荷分担，AMF基于locality优选与本地位置相同（例如，同一个DC内）的SMF，避免跨DC的路由迂回。SMF跨DC负荷分担，本地SMF设备升级维护不再进行业务，AMF基于locality优选指定位置的SMF。
DNS查询优先级|AMF控制DNS Server查询和DNS cache查询这两种查询方式的优先级。|当AMF通过NRF解析选择出的SMF节点仅携带FQDN而非IP地址时，AMF基于FQDN查询DNS获取到IP地址。
同一个UE多个PDU Session选择同一个SMF|如果同一个UE发起的多个PDU Session具有相同DNN和S-NSSAI，则AMF可以选择同一个SMF。如果同一个UE发起的多个PDU Session具有相同DNN和不同S-NSSAI，则AMF可以选择同一个SMF。如果同一个UE发起的多个PDU Session具有不同的DNN，则AMF可以选择同一个SMF。|互操作场景下，同一个UE在5G网络发起的多个PDU  Session，AMF选择到同一个PGW-C+SMF。UE移动到4G网络后，所有的PDN连接都选择到同一个PGW-C+SMF，MME选择到与PGW-C+SMF合一或者拓扑邻近的SGW，避免路由迂回。
TAI|当SMF只服务于特定跟踪区时，SMF在向NRF注册时携带支持的跟踪区信息。AMF根据UE当前位置（TAI）选择特定SMF。基于TAI选择SMF有如下两种情况：基于TAI优选A-SMFNRF优选：AMF通过NRF发现SMF时携带preferred-tai参数，NRF使用该参数进行SMF发现。本地优选：AMF通过NRF发现SMF不携带preferred-tai参数或者NRF不支持preferred-tai特性时，AMF本地基于TAI优选SMF。基于TAI选择H-SMFAMF通过NRF发现SMF时携带TAI参数，NRF使用该参数进行SMF发现。|非漫游或者Local-Breakout漫游，AMF基于TAI优选本地A-SMF。异网漫游（即国家码相同网络码不同，采用Home routed方式的跨PLMN漫游），AMF基于TAI就近选择本地H-SMF。
servingScope|servingScope，即服务范围，表示NF可以服务的逻辑区域。当SMF只为某些区域服务时，SMF在向NRF注册时携带支持的服务范围。AMF根据servingScope选择服务于特定区域的SMF。|AMF和SMF服务范围一致，例如：AMF和SMF按大区/省集中部署，AMF基于servingScope就近选择本大区/省SMF。AMF服务范围大于SMF服务范围，例如：AMF按大区/省集中部署，SMF按地市下沉部署，AMF基于servingScope就近选择本地市SMF。
选择策略|详细说明
---|---
基于Locality选择SMF|基于Locality选择SMF的策略|基于Locality选择SMF有如下两种策略，通过发现SMF参数配置组内命令中的携带preferred-locality参数和支持基于Locality优选参数控制使用的策略：NRF优选：AMF通过NRF发现SMF时携带preferred-locality参数，NRF使用该参数进行SMF发现。本地优选：AMF通过NRF发现SMF时不携带preferred-locality参数，此时使用本地基于Locality选择SMF的策略。AMF基于Locality选择SMF时，选择策略只能使用NRF优选和本地优选中的一种；在同时配置的情况下，以本地优选的优先级为高。
本地基于Locality选择SMF的策略|基于Locality选择SMF|AMF本地基于Locality选择SMF时，可以通过ADD PREFER LOCALITY命令控制本地Locality选择策略，具体策略如下。位置选择优先级AMF根据“Locality→优先级→权重”的顺序进行匹配，选择合适的SMF。AMF根据“优先级→Locality→权重”的顺序进行匹配，选择到合适的SMF。位置匹配策略全匹配：AMF根据Locality执行全字符匹配。按Label最长匹配：适用于点分格式编码的Locality，此类型的Locality内包含多个label。AMF按照从左向右的顺序，匹配SMF中的Locality参数，执行Label个数最长匹配，即匹配Label个数最多的SMF会被选择（Label内执行全字符匹配，完全匹配则认为该Label匹配）。容灾策略SMF容灾采用跨DC异地容灾或地理容灾的方式，当其中一个DC内多个SMF发生故障无法提供服务时，为保证另外一个DC能接管业务，可以通过“NF位置优选策略配置”中的“位置优选是否支持容灾”参数控制本地不启用Locality选择SMF功能，优先保证SMF容灾功能。
 说明： 
当基于TAI和Locality选择SMF策略同时开启时，策略如下： 
如果启用基于TAI和基于Locality的NRF优选策略，AMF通过NRF发现SMF时同时携带preferred-tai和preferred-locality参数，由NRF控制TAI和Locality的匹配顺序，进行SMF发现。 
如果启用基于TAI和基于Locality的本地优选策略，AMF通过NRF发现SMF时不携带preferred-locality参数，由AMF按照“TAI→Locality”的匹配顺序，选择合适的SMF。 
如果启用基于TAI的NRF优选策略和基于Localiy的本地优选策略，AMF通过NRF发现SMF时携带preferred-tai参数，不携带preferred-locality参数，NRF使用preferred-tai参数进行SMF发现；AMF在NRF返回的SMF列表中，再根据Locality选择合适的SMF。 
业务流程 :SMF选择功能是在UE请求PDU会话的流程中执行的，参见[UE请求PDU会话建立流程中SMF选择]。
在非漫游、LBO漫游以及HR漫游场景下，SMF选择的具体执行步骤有所区别，参见以下两个业务流程：
本地用户接入或漫游用户拜访地接入时SMF选择：本地用户或漫游用户在拜访地接入时，AMF执行SMF选择。 
漫游用户本地接入时SMF选择：漫游用户在本地接入时，AMF执行SMF选择。 
UE请求PDU会话建立流程中SMF选择
UE向AMF发起PDU会话建立请求。 
AMF根据SMF选择策略选择得到SMF（参见[表1]），AMF向SMF发送Nsmf_PDUSession_CreateSMContext
Request消息并携带已选择的SMF地址。
SMF向UDM获取或更新签约信息，创建会话。 
SMF处理成功，向AMF返回Nsmf_PDUSession_CreateSMContext
Response。 
继续PDU会话建立流程。 
本地用户接入或漫游用户拜访地接入时SMF选择
图6  SMF selection for non-roaming and roaming with local breakoutscenarios

（可选）本地用户或漫游用户发起PDU会话建立流程，AMF向NSSF发送Nnssf_NSSelection_Get Request消息，携带S-NSSAI、SUPI中的PLMN ID、TA等信息，从NSSF处获取NRF和NSI ID。。 
（可选）NSSF返回Nnssf_NSSelection_Get Response消息，将选择的NSI ID（即：网络切片实例）和用于NF选择的NRF发送给AMF。 
AMF根据用户请求和签约数据为用户选择相应的DNN，本地用户DNN的OI部分取自SUPI，漫游用户DNN的OI部分取自拜访地运营商的PLMN。如果AMF已经从NSSAI存储了S-NSSAI的NSI ID，AMF向服务PLMN的NRF发送Nnrf_NFDiscovery_Request，携带S-NSSAI、SUPI中的PLMN
ID、DNN和NSI ID。 
服务PLMN的NRF查询匹配的SMF列表，向AMF返回响应，携带发现的SMF实例或SMF服务实例的端点地址的集合（例如，FQDN或IP地址），以及与S-NSSAI相对应的所选网络片实例的NSI
ID。 
如果同一个UE发起的多个PDU会话具有相同DNN和S-NSSAI，并且UE签约支持EPS互操作，则多个PDU会话应选择同一个SMF；如果UE未签约支持EPS互操作，则可以选择不同的SMF。 
漫游用户本地接入时SMF选择
当vPLMN和hPLMN均部署NSSF，使用本方式。图7  Option 1 for SMF selection for home-routed roaming scenarios漫游用户发起PDU会话建立流程，AMF向vNSSF发送Nnssf_NSSelection_Get消息，携带允许NSSAI的S-NSSAI、映射到VPLMN的NSSAI的HPLMN S-NSSAI、SUPI的PLMN ID和UE的TAI，以及PDU会话建立过程中的home-routed漫游场景指示，获取NRF和NSI ID。如果HPLMN的S-NSSAI配置信息不可用（如NSSF没有缓存信息），vNSSF根据SUPI的PLMN ID向hNSSF发送Nnssf_NSSelection_Get，携带HPLMN S-NSSAI。hNSSF在Nnssf_NSSelection_Get response中返回NSI ID，S-NSSAI和hNRF。vNSSF在Nnssf_NSSelection_Get response中返回hNSSF返回的所有信息，包括NSI ID，S-NSSAI和hNRF。AMF调用Nnrf_NFDiscovery_Request查询vNRF，携带HPLMN（取自SUPI）、DNN、HPLMN S-NSSAI、HPLMN NSI ID。vNRF根据vNSSF提供的信息识别hNRF，调用Nnrf_NFDiscovery_Request查找hNRF。hNRF查询匹配的SMF列表，通过Nnrf_NFDiscovery_Request response中向vNRF提供发现的SMF实例或SMF服务实例的端点地址集合（例如，FQDN或IP地址），以及与S-NSSAI相对应的所选网络切片实例的NSI ID。vNRF发送Nnrf_NFDiscovery_Request response给AMF，AMF获取到匹配的SMF列表，AMF根据SMF选择策略选择得到SMF。 
当HPLMN没有部署NSSF，则VPLMN的AMF依据本地配置获取hNRF，或者使用如下方式。图8  Option 2 for SMF selection for home-routed roaming scenariosAMF依据配置查询vNRF，携带SUPI的PLMN ID、serving PLMN的PLMN ID、DNN、从服务PLMN允许的NSSAI映射的HPLMN S-NSSAI、NSI ID和DNN。vNRF通过SUPI的PLMN ID识别hNRF，调用Nnrf_NFDiscovery_Request查询hNRF，NF信息依然携带AMF ID。hNRF根据配置和可用信息，执行步骤3(A)或3(B)。a. hNRF根据携带HPLMN（取自SUPI）、DNN、HPLMN S-NSSAI、HPLMN NSI ID查询匹配的SMF列表，通过vNRF在Nnrf_NFDiscovery_Request response中给AMF提供，发现的SMF实例或SMF服务实例的端点地址的集合，例如，FQDN或IP地址，以及与S-NSSAI相对应的所选网络片实例的NSI ID。b~d. hNRF代表AMF查询HPLMN的一个本地NRF（如一个切片级的NRF）。这个本地NRF根据携带HPLMN（取自SUPI）、DNN、HPLMN S-NSSAI、HPLMN NSI ID查询匹配的SMF列表。最终通过hNRF和vNRF，在Nnrf_NFDiscovery_Request response中向AMF提供发现的SMF实例或SMF服务实例的端点地址的集合（例如，FQDN或IP地址），以及与S-NSSAI相对应的所选网络片实例的NSI ID。AMF根据SMF选择策略选择得到SMF。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :相关特性|交互关系
---|---
ZUF-79-12-001 支持N26接口互操作|UE请求建立PDU会话时，AMF识别UE能力支持S1 mode，AMF通过NRF选择SMF时，选择支持PGW能力（NFProfile中包含pgwFQDN信息）的SMF+PGW-C。
ZUF-79-12-002 支持无N26接口互操作|AMF根据MME携带过来的PGW FQDN，通过NRF查询PGW FQDN对应SMF+PGW-C的服务化地址。
ZUF-76-05-004 IPv4IPv6双栈|如果SMF的地址既有IPv4地址，也有IPv6地址，而本局也支持IPv6地址，则根据软参“SMF IP双栈优选的IP类型”选择SMF的地址类型。
ZUF-76-12-004 AMF周边网元拨测|AMF根据SUPI/MSISDN号码或号段选择SMF，将特定号段的用户选择到指定的SMF上，对SMF进行拨测。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2".|6.3.2: SMF discovery and selection
3GPP TS 23.502: "Procedures for the 5G System;Stage2".|4.3.2.2.3: SMF selection
特性能力 :名称|指标
---|---
支持的AMF服务范围最大配置个数|128
支持的SMF服务范围组最大配置个数|4096
每个SMF服务范围组支持的服务范围最大配置个数|128
支持的SMF服务范围跟踪区组最大配置个数|65535
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
05|V7.22.20|增加基于TAI选择SMF策略增加基于servingScope选择SMF策略
04|V7.22.10|部分配置变更。
03|V7.21.40|实现原理更新：增加本地基于Locality选择SMF策略描述
02|V7.21.20|实现原理更新。增加签约smfList选择策略增加locality选择策略增加同一个UE多个PDU Session选择同一个SMF策略
01|V7.19.10|首次发布。
License要求 :该功能需要申请了License许可后，运营商才能获得该功能的服务。 
该功能对应的License项目为AMF支持基于servingScope选择SMF，此项目显示为ON，表示支持基于servingScope选择SMF。
对其他网元的要求 :NRF|SMF
---|---
√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :无。 
#### OM相关 
命令 :配置项
命令名称|描述
---|---
SET NRFDISCSMFPARACFG|修改NRF发现A-SMF参数配置
SHOW NRFDISCSMFPARACFG|查询NRF发现A-SMF参数配置
ADD SMFIPPOOLCFG|新增SMF IP POOL配置
DEL SMFIPPOOLCFG|删除SMF IP POOL配置
SHOW SMFIPPOOLCFG|查询SMF IP POOL配置
SET RESOLVESMFPOLICY|修改解析SMF策略配置
SHOW RESOLVESMFPOLICY|查询解析SMF策略配置
ADD RESOSMFPLYBASEDUSER|增加用户级解析SMF策略配置
SET RESOSMFPLYBASEDUSER|修改用户级解析SMF策略配置
DEL RESOSMFPLYBASEDUSER|删除用户级解析SMF策略配置
SHOW RESOSMFPLYBASEDUSER|查询用户级解析SMF策略配置
ADD RESOLASMFCFG|新增基于号段解析A-SMF配置
SET RESOLASMFCFG|修改基于号段解析A-SMF配置
DEL RESOLASMFCFG|删除基于号段解析A-SMF配置
SHOW RESOLASMFCFG|查询基于号段解析A-SMF配置
ADD RESOLIVSMFCFG|新增基于号段解析I-SMF和V-SMF配置
SET RESOLIVSMFCFG|修改基于号段解析I-SMF和V-SMF配置
DEL RESOLIVSMFCFG|删除基于号段解析I-SMF和V-SMF配置
SHOW RESOLIVSMFCFG|查询基于号段解析I-SMF和V-SMF配置
SET ASMFSELPOLICY|修改 A-SMF选择策略配置
SHOW ASMFSELPOLICY|查询 A-SMF选择策略配置
SET AMFSUPPORTISMF|修改AMF是否支持I-SMF配置
SHOW AMFSUPPORTISMF|查询AMF是否支持I-SMF配置
ADD PLMN NRFDISCSMFPARA|新增基于PLMN的NRF发现A-SMF参数配置
SET PLMN NRFDISCSMFPARA|修改基于PLMN的NRF发现A-SMF参数配置
DEL PLMN NRFDISCSMFPARA|删除基于PLMN的NRF发现A-SMF参数配置
SHOW PLMN NRFDISCSMFPARA|查询基于PLMN的NRF发现A-SMF参数配置
ADD PREFER LOCALITY|新增优选位置配置
SET PREFER LOCALITY|修改优选位置配置
DEL PREFER LOCALITY|删除优选位置配置
SHOW PREFER LOCALITY|查询优选位置配置
SET NFADDRCHOICEPOLICYCFG|修改NF地址选择策略配置
SHOW NFADDRCHOICEPOLICYCFG|查询NF地址选择策略配置
SET NFSELECTPOLICY|修改NF选择策略配置
SHOW NFSELECTPOLICY|查询NF选择策略配置
软件参数
软件参数ID|软件参数名称
---|---
119|选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选
144|发现SMF时携带requester-plmn-list是否从本局支持的PLMN配置中获取
198|移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :AMF发现SMF的方法可以分为如下三种： 
NRF发现：AMF向NRF请求发现SMF，NRF向AMF返回SMF列表。AMF可根据返回的SMF列表进一步通过条件进行优选。 
本地发现：AMF本地发现SMF。AMF可根据选择的SMF列表进一步通过条件进行优选。 
号段解析场景：AMF在本地基于号段进行拨测，包括基于号段解析A-SMF和基于号段解析I-SMF和V-SMF配置。 
完成本配置过程，可以通过以上三种方式进行SMF选择。 
配置前提 :AMF与周边NF对接成功。 
SMF的组网规划已经确定。 
配置过程 :###### NRF发现和本地发现配置 
AMF通过NRF发现方式和通过本地发现方式获取SMF的配置过程均可参考以下配置。 
服务发现方式配置
发现方式|配置过程
---|---
NRF发现|执行ADD SBISRVDISCOVERYMODE命令，新增服务发现方式相关配置。将DISCOVERYMODE配置为DYNAMIC_ONLY或DYNAMIC_FIRST。
本地发现|执行ADD SBISRVDISCOVERYMODE命令，新增服务发现方式相关配置。将DISCOVERYMODE配置为STATIC_ONLY或DYNAMIC_FIRST。
（可选）发现A-SMF参数配置
当需要通过NRF发现方式或本地发现方式发现A-SMF时，执行以下配置过程。 
执行[SET NRFDISCSMFPARACFG]命令， 修改发现A-SMF参数配置。
执行[ADD PLMN NRFDISCSMFPARA]命令， 新增基于PLMN的发现A-SMF参数配置。
（可选）发现I-SMF/V-SMF参数配置
当需要通过NRF发现方式或本地发现方式发现I-SMF/V-SMF时，执行以下配置过程。 
执行[SET AMFSUPPORTISMF]命令，修改AMF是否支持I-SMF相关参数配置。需要配置AMF支持I-SMF。
执行[SET NRFDISCIVSMFPARACFG]命令，修改发现I-SMF/V-SMF参数配置。
执行[ADD PLMN NRFDISCIVSMFPARA]命令，新增基于PLMN的发现I/V-SMF参数配置。
SMF选择策略配置
（可选）执行[SET NFSELECTPOLICY]命令，修改NF选择策略配置。当AMF需要根据选择策略从NRF返回的SMF或本地发现的SMF中选出一个SMF时，使用本命令设置SMF选择策略。
###### 发现策略配置 
本过程配置的发现策略适用于NRF发现和本地发现。 
基于签约SMF List选择A-SMF配置
执行[SET ASMFSELPOLICY]命令，通过SUPSELSMFBYSUBSMFID参数设置是否基于签约SMF ID选择A-SMF。
基于Locality优选SMF配置
执行[ADD PLMN NRFDISCSMFPARA]命令，新增基于PLMN的发现A-SMF参数配置。
执行[SET NRFDISCSMFPARACFG]命令，修改发现A-SMF参数配置。
（可选）本地优选时配置本命令。执行[ADD PREFER LOCALITY]命令，新增优选位置配置。当AMF已通过NRF发现SMF，需要基于位置信息优先选择特定位置的SMF时，使用本命令配置指定的位置信息。
基于ServingScope选择SMF配置
执行[ADD SMF SERVSCOPE GRP]命令，新增SMF服务范围组配置。
（可选）本地优选时配置本命令。执行[ADD SMF SERVSCOPE TA GRP]命令，新增SMF服务范围跟踪区组配置。当AMF需要基于跟踪区映射出服务范围选择服务于特定区域的SMF时，使用本命令配置跟踪区和服务范围的映射关系。
执行[SET NRFDISCSMFPARACFG]命令， 修改发现A-SMF参数配置。
执行[ADD PLMN NRFDISCSMFPARA]命令，新增基于PLMN的发现A-SMF参数配置。
同一用户的多个会话选择相同SMF配置
执行[SET ASMFSELPOLICY]命令，通过AMFSELSAMEASMFBYDNN参数设置相同DNN的多PDU会话是否选择同一个A-SMF。
基于TAI选择SMF配置
（可选）本地优选时配置本命令。执行[SET ASMFSELPOLICY]命令，通过AMFSELASMFBYTA参数设置AMF本地是否基于TAI优选SMF。
执行[SET NRFDISCSMFPARACFG]命令，修改NRF发现A-SMF参数配置。
执行[ADD PLMN NRFDISCSMFPARA]命令，新增基于PLMN的NRF发现A-SMF参数配置。
###### 基于SUPI/MSISDN号段选择SMF配置 
执行[SET RESOLVESMFPOLICY]命令， 修改解析SMF策略相关参数配置。
执行[ADD RESOSMFPLYBASEDUSER]命令， 增加用户级解析SMF策略相关参数配置。
（可选）执行[ADD SMFIPPOOLCFG]命令， 新增SMF地址池相关参数配置。当现网没有部署NRF或者NRF不可用时，运营商希望通过AMF本地配置SMF解析数据，发现和选择SMF时，使用本命令配置SMF地址池。
（可选）执行[ADD RESOLASMFCFG]命令， 新增基于号段解析A-SMF相关参数配置。当需要在割接或拨测场景下，让某一部分测试用户选择到指定的A-SMF时，使用本命令新增基于号段解析A-SMF配置。
（可选）执行[ADD RESOLIVSMFCFG]命令， 新增基于号段解析I-SMF和V-SMF相关参数配置。当需要在割接或拨测场景下，让某一部分测试用户选择到指定的I-SMF或V-SMF时，使用本命令新增基于号段解析I-SMF和V-SMF配置。
###### 本地配置 
本地发现NF时，需通过以下过程本地配置相应的SMF。 
服务发现方式配置
执行[ADD SBISRVDISCOVERYMODE]命令，新增服务发现方式相关配置。当需要新增发现特定目的SMF的方式时，使用该命令。将DISCOVERYMODE配置为STATIC_ONLY或DYNAMIC_FIRST。
PLMN ID配置
执行[ADD SBIPLMNID]命令，新增PLMN ID配置。PLMN ID配置用于配置服务提供者的公共陆地移动网的移动国家码和移动网号，当启用本地NRF功能时，需要配置该组命令。
执行[ADD SBIPLMNIDARRID]命令，新增PLMN ID组编号配置。一个PLMN ID组下面可以包含若干个PLMN ID组参数。当启用本地NRF功能时，需要配置该组命令。
执行[ADD SBIPLMNIDARRPARAM]命令，新增PLMN ID组参数配置。当PLMN ID配置需要归属于一个PLMN ID组时，使用该命令。命令执行成功后，PLMN ID组就可以包含PLMN ID配置。
PLMN NID配置
执行[ADD SBIPLMNNID]命令，新增PLMN NID配置。当本地NRF配置中所配置的对端SMF Profile需要携带使用公共陆地移动网和网络标识共同标识的独立专网信息时，使用该命令。
（可选）执行[ADD SBIPLMNNIDARRID]命令，新增PLMN NID组编号配置。一个PLMN NID组包含了若干个PLMN NID组参数。当启用本地NRF功能时，需要配置该组命令。
（可选）执行[ADD SBIPLMNNIDARRPARAM]命令，新增PLMN NID组参数配置。当一个PLMN NID配置需要归属于一个PLMN NID组时，使用该命令。命令执行成功后，PLMN NID组就可以包含PLMN NID配置。
S-NSSAI配置
执行[ADD SBISNSSAI]命令，新增S-NSSAI配置。当本地NRF配置中所配置的对端SMF Profile需要添加携带切片/服务类型和切片区分符的单个网络切片选择协助信息时，使用该命令。
执行[ADD SBISNSSAIARRID]命令，新增S-NSSAI组编号配置。该命令用于配置一个S-NSSAI组，一个S-NSSAI组包含了若干个S-NSSAI组参数。当启用本地NRF功能时，需要配置该组命令。
执行[ADD SBISNSSAIARRPARAM]命令，新增S-NSSAI组参数配置。当S-NSSAI配置需要归属于一个S-NSSAI组时，使用该命令。命令执行成功后，S-NSSAI组就可以包含S-NSSAI配置。
PLMN S-NSSAI配置
（可选）执行[ADD SBIPLMNSNSSAI]命令，新增PLMN S-NSSAI配置。当本地NRF配置中所配置的对端SMF Profile需要携带使用SNPN（Standalone Non-Public Network，独立专网）和S-NSSAI组编号共同标识的PLMN S-NSSAI时，使用该命令。
（可选）执行[ADD SBIPIMNSNSSAIARRID]命令，新增PLMN S-NSSAI组编号配置。该命令用于配置一个PLMN S-NSSAI组，一个PLMN S-NSSAI组包含了若干个PLMN S-NSSAI组参数。当启用本地NRF功能时，需要配置该组命令。
（可选）执行[ADD SBIPIMNSNSSAIARRPARAM]命令，新增PLMN S-NSSAI组参数配置。当一个PLMN S-NSSAI配置需要归属于一个PLMN S-NSSAI组时，使用该命令。命令执行成功后，PLMN S-NSSAI组就可以包含PLMN S-NSSAI配置。
NSI组配置
（可选）执行[ADD SBINSIARRID]命令，新增NSI组编号配置。当本地NRF配置的对端SMF Profile需要携带一组NSI时，使用该命令。命令执行成功后，NSI组编号可以被NSI组参数配置及对端NF基本信息配置引用。
（可选）执行[ADD SBINSIARRPARAM]命令，新增NSI组参数配置。当一个NSI配置需要归属于一个NSI组时，使用该命令。命令执行成功后，NSI组就可以包含NSI配置。
域组配置
（可选）执行[ADD SBIDOMAINARRID]命令，新增域组编号配置。当本地NRF配置中所配置的对端SMF Profile需要携带一组域时，使用该命令。命令执行成功后，域组编号可以被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。
（可选）执行[ADD SBIDOMAINARRPARAM]命令，新增域组参数配置。当一个域配置需要归属于一个域组时，使用该命令。命令执行成功后，域组就可以包含域配置。
NF类型组配置
（可选）执行[ADD SBINFTYPEARRID]命令，新增NF类型组编号配置。当本地NRF配置中所配置的对端SMF Profile需要携带一组NF类型时，使用该命令。命令执行成功后，NF类型组编号可以被NF类型组参数配置和对端NF基本信息配置引用。
（可选）执行[ADD SBINFTYPEARRPARAM]命令，新增NF类型组参数配置。当一个NF类型配置需要归属于一个NF类型组时，使用该命令。命令执行成功后，NF类型组就可以包含NF类型配置。
服务范围组配置
（可选）执行[ADD SBISERVSCOPEARRID]命令，新增服务范围组编号配置。当本地NRF配置中所配置的对端SMF Profile需要携带一组服务范围时，使用该命令。命令执行成功后，服务范围组编号可以被服务范围组参数配置和对端NF基本信息配置引用。
（可选）执行[ADD SBISERVSCOPEARRPARAM]命令，新增服务范围组参数配置。当一个服务范围配置需要归属于一个服务范围组时，使用该命令。命令执行成功后，服务范围组就可以包含服务范围配置。
NF集标识组配置
（可选）执行[ADD SBINFSETIDARRID]命令，新增NF集标识组编号配置。当本地NRF配置中所配置的对端SMF Profile需要携带一组NF集标识时，使用该命令。命令执行成功后，NF集标识组编号可以被“NF集标识组参数配置”及“对端NF基本信息配置”引用。
（可选）执行[ADD SBINFSETIDARRPARAM]命令，新增NF集标识组参数配置。当一个NF集标识配置需要归属于一个NF集标识组时，使用该命令。命令执行成功后，NF集标识组就可以包含NF集标识配置。
IPv4地址和IPv6地址配置
执行[ADD SBIIPV4ADDR]命令，新增IPv4地址配置。当启用本地NRF功能时，需要执行此命令增加服务提供者（对端）网络功能（NF）的IPv4地址。命令执行成功后，新增的IPv4地址编号可以被IPv4地址组参数配置、IP端点配置引用。
执行[ADD SBIIPV4ADDRARRID]命令，新增IPv4地址组编号配置。当启用本地NRF功能，且需要添加一个新的IPv4地址组编号时，使用该命令。命令执行成功，再将对端网络功能（NF）的IPv4地址加入新增的IPv4地址组后，IPv4地址组编号可以被对端NF基本信息配置引用。
执行[ADD SBIIPV4ADDRARRPARAM]命令，新增IPv4地址组参数配置。当开启本地NRF功能，且需要在Pv4地址组中增加对端NF的IPv4地址时使用该命令。新增的IPv4地址组，需要使用本命令在组内添加一个或者多个IPv4地址才可以被对端NF基本信息配置引用。
执行[ADD SBIIPV6ADDR]命令，新增IPv6地址配置。当启用本地NRF功能时，需要执行此命令增加服务提供者（对端）网络功能（NF）的IPv6地址。命令执行成功后，新增的IPv6地址编号可以被IPv6地址组参数配置、IP端点配置引用。
执行[ADD SBIIPV6ADDRARRID]命令，新增IPv6地址组编号配置。当启用本地NRF功能，且需要添加一个新的IPv6地址组编号时，使用该命令。命令执行成功，再将对端网络功能（NF）的IPv6地址加入新增的IPv6地址组后，IPv6地址组编号可以被对端NF基本信息配置引用。
执行[ADD SBIIPV6ADDRARRPARAM]命令，新增IPv6地址组参数配置。当开启本地NRF功能，且需要在IPv6地址组中增加对端NF的IPv6地址时使用该命令。新增的IPv6地址组，需要使用本命令在组内添加一个或者多个IPv6地址才可以被对端NF基本信息配置引用。
IP端点配置
执行[ADD SBIIPENDPOINT]命令，新增IP端点配置。当启用本地NRF功能时，执行该命令。命令执行成功后，本配置可以被IP端点组参数配置引用。
执行[ADD SBIIPENDPOINTARRID]命令，新增IP端点组编号配置。当启用本地NRF功能时，需要配置该组命令。本配置被对端NF服务实例配置引用，最终呈现在本地NRF配置的对端SMF Profile的ipEndPoints数组中。如果不配置，则对端SMF Profile缺少ipEndPoints数组，本端如果需要请求对端提供的服务，服务请求无法发送成功。
执行[ADD SBIIPENDPOINTARRPARAM]命令，新增IP端点组参数配置。当启用本地NRF功能时，执行该命令。命令执行成功后，本配置被IP端点组参数配置引用。命令执行成功后，服务使用者如果需要使用服务提供者提供的服务，则根据配置的组信息向服务提供者发送服务请求。
NF服务版本组配置
执行[ADD SBINFSVERSIONARRID]命令，新增NF服务版本组编号配置。本配置被对端NF服务实例配置引用，最终呈现在本地NRF配置出来的对端SMF Profile的versions数组中。如果不配置，则对端SMF Profile缺少versions数组，本端如果需要请求对端提供的服务，服务请求的URI不能携带正确的版本号，可能导致服务请求发送失败以及业务流程失败。
执行[ADD SBINFSVERSIONARRPARAM]命令，新增NF服务版本组参数配置。当启用本地NRF功能时，执行该命令。命令执行成功后，当服务使用者从NRF获取到服务提供者的服务版本组时，把其中一个的API URI版本号作为本次服务请求的URI中使用的版本号。
NF服务集标识组配置
（可选）执行[ADD SBINFSETIDARRID]命令，新增NF集标识组编号配置。本配置被对端NF服务实例配置引用，最终呈现在本地NRF配置出来的对端SMF Profile的nfServiceSetIdList数组中。如果不配置，则对端SMF Profile缺少nfServiceSetIdList数组，本端选择的对端NF服务出现故障时，只能尝试切换到其他的非共享上下文的NF服务，不能在同一个NF服务集中选择负荷分担的服务继续使用，可能造成业务中断。
（可选）执行[ADD SBINFSETIDARRPARAM]命令，新增NF集标识组参数配置。如果不配置NF服务集标识组参数，则NF服务集标识组没有具体内容，本端无法获取对端的NF服务集标识，本端选择的对端NF服务出现故障时，只能尝试切换到其他的非共享上下文的NF服务，不能在同一个NF服务集中选择负荷分担的服务继续使用，可能造成业务中断。
GUAMI组配置
（可选）执行[ADD SBIGUAMIARRID]命令，新增GUAMI组编号配置。当AMF需要新增限定可以支持的GUAMI列表、用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表时，使用该命令。命令执行成功后，GUAMI组编号可以被“GUAMI组参数配置”及“AMF信息配置”引用。
（可选）执行[ADD SBIGUAMIARRPARAM]命令，新增GUAMI组参数配置。当AMF已配置可以服务的GUAMI组编号，需要新增归属于该GUAMI组编号的参数时，使用该命令。命令执行成功后，AMF新增了可以服务的该组GUAMI信息。
TAC配置
（可选）执行[ADD SBITACRANGEARRID]命令，新增TAC范围组编号配置。当需要新增TAI范围组用于限定NF（SMF、AMF、NWDAF）可以服务的TAI范围时，使用该命令。执行成功后，可以在TAI范围组参数配置中关联该TAC范围组编号。
（可选）执行[ADD SBITACRANGEARRPARAM]命令，新增TAC范围组参数配置。用于表示一个具体的TAC范围，被TAI范围组参数配置引用。当需要新增TAI范围组参数配置且需要引用的TAC范围不存在时，执行该命令。
TAI配置
执行[ADD SBITAIARRID]命令，新增TAI组编号配置。当SMF、AMF、UPF、NWDAF四个NF需要新增限定可以服务的TAI列表时，使用该命令。执行成功后，可以在上述四个NF配置信息中关联该组编号。
执行[ADD SBITAIARRPARAM]命令，新增TAI组参数配置。当某个TAI组中需要增加NF（SMF、AMF、UPF、NWDAF）可以服务的TAI时，使用该命令在TAI组内增加TAI组参数。命令执行成功后，关联该TAI组的NF（SMF、AMF、UPF、NWDAF）对新增的TAI提供服务。
（可选）执行[ADD SBITAIRANGEARRID]命令，新增TAI范围组编号配置。当NF（SMF、AMF、NWDAF）需要新增可以服务的TAI范围组时，使用该命令。执行成功后，可以在NF扩展信息配置中关联该TAI范围组编号。
（可选）执行[ADD SBITAIRANGEARRPARAM]命令，新增TAI范围组参数配置。当NF（SMF、AMF、NWDAF）已配置可以服务的TAI范围组编号，需要新增归属于该TAI范围组编号的参数时，使用该命令。执行成功后，NF（SMF、AMF、NWDAF）新增了可以服务的该范围组参数的TAI信息。
DNN配置
执行[ADD SBIDNNARRID]命令，新增DNN组编号配置。当NF需要新增可以服务的DNN组时，使用该命令。执行成功后，可以在NF扩展信息配置中关联该DNN组编号。
执行[ADD SBIDNNARRPARAM]命令，新增DNN组参数配置。当NF已配置可以服务的DNN组编号，需要新增归属于该DNN组编号的参数时，使用该命令。执行成功后，NF（PCF、BSF等）新增了可以服务的该范围组参数的DNN信息。
API版本组配置
（可选）执行[ADD SBIAPIVERSIONARRID]命令，新增API版本组编号配置。当缺省通知端点组配置需要新增限定默认通知类型所支持的API版本组时，使用该命令。执行成功后，可以在缺省通知端点组配置中关联该API版本组编号。
（可选）执行[ADD SBIAPIVERSIONARRPARAM]命令，新增API版本组参数配置。当缺省通知端点组参数配置需要新增可以提供服务的API版本时，使用该命令配置API版本组参数，该参数配置API版本信息以及归属的API版本组。执行成功后，缺省通知端点组参数配置新增了一个可以服务的API版本信息。
缺省通知端点组配置
（可选）执行[ADD SBIDLFTNOTEENDPOINTARRID]命令，新增缺省通知端点组编号配置。当需要新增对端NF支持的缺省通知端点组时，使用该命令。执行成功后，可以在缺省通知端点组参数配置、对端NF基本信息配置和对端NF服务实例配置中关联该缺省通知端点组编号。
（可选）执行[ADD SBIDLFTNOTEENDPOINTARRPARAM]命令，新增缺省通知端点组参数配置。当服务使用者（本端）在订阅时，未在请求中显式地携带回调URI，那么服务提供者（对端）在需要发送通知时，需要使用缺省回调URI将通知消息发往本端，可以使用该命令新增缺省通知端点组参数，该参数配置缺省通知端点信息以及归属的缺省通知端点组。
对端NF配置
执行[ADD SBIPEERNFBASEINFO]命令，新增对端NF基本信息配置。当本地NRF配置中所配置的对端SMF Profile需要携带基本信息字段时，使用该命令。命令执行成功后，本地NRF配置中会新增一个对端SMF Profile及其基本信息字段。该配置中的“对端NF基本信息编号”可以被对端NF扩展信息配置及对端NF服务实例配置引用。
执行[ADD SBIPEERNFEXTINFO]命令，新增对端NF扩展信息配置。当本地NRF配置中所配置的对端SMF Profile需要携带扩展信息字段时，使用该命令。命令执行成功后，在本地NRF发现的对端SMF Profile中将包含NF扩展信息字段。
对端NF服务实例配置
执行[ADD SBIPEERNFSERVICEINSTANCE]命令，新增对端NF服务实例配置。当本地NRF配置的NF实例需要增加可以为5GC网络中其他NF提供的服务时，使用该命令。执行成功后，该NF实例新增了一个可以提供的服务，该服务在被其他NF服务发现时进行匹配和使用。
SMF扩展信息配置
执行[ADD SBISMFINFO]命令，新增SMF信息配置。当本地NRF配置中所配置的对端SMF Profile需要携带SMF信息时，使用该命令。命令执行成功后，SMF信息编号可以被对端NF扩展信息配置引用。
执行[ADD SBISNSSAISMFINFOARRID]命令，新增S-NSSAI SMF信息组编号配置。当新增SMF扩展信息时，使用该命令。执行成功后，可以在SMF扩展信息配置中关联该S-NSSAI SMF信息组编号。
执行[ADD SBISNSSAISMFINFOARRPARAM]命令，新增S-NSSAI SMF信息组参数配置。当SMF已配置可以服务的S-NSSAI SMF信息组编号，需要新增归属于该S-NSSAI SMF信息组编号的参数时，使用该命令。执行成功后，SMF新增了可以服务的该S-NSSAI SMF信息组参数的DNN和S-NSSAI信息。
#### 配置实例一（NRF发现） 
场景说明 :配置支持AMF通过NRF发现SMF。 
数据规划 :命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD SBISRVDISCOVERYMODE|目标NF类型|SMF|本端规划|-
发现方式|ADD SBISRVDISCOVERYMODE|动态|本端规划|-
SET AMFSUPPORTISMF|AMF是否支持I-SMF|支持|本端规划|-
SET NRFDISCSMFPARACFG|DNN携带OI|不支持OI|本端规划|-
携带SNSSAI|SET NRFDISCSMFPARACFG|支持SNNAI|本端规划|-
携带目标PLMN|SET NRFDISCSMFPARACFG|不支持PLMN|本端规划|-
携带切片实例号|SET NRFDISCSMFPARACFG|不支持切片实例号|本端规划|-
携带preferred-locality|SET NRFDISCSMFPARACFG|不携带|本端规划|-
携带pgw-ind标识|SET NRFDISCSMFPARACFG|支持携带pgw-ind标识|本端规划|-
支持基于Locality优选|SET NRFDISCSMFPARACFG|不支持|本端规划|-
携带Preferred跟踪区标识|SET NRFDISCSMFPARACFG|携带|本端规划|必须在AMF支持I-SMF功能时才能携带该标识。
携带跟踪区标识|SET NRFDISCSMFPARACFG|不携带|本端规划|-
携带servingScope|SET NRFDISCSMFPARACFG|不携带|本端规划|-
服务范围组标识|SET NRFDISCSMFPARACFG|0|本端规划|-
服务范围扩展策略|SET NRFDISCSMFPARACFG|不扩展|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|必须要和SMF的DNN一致。
携带preferred-locality|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
支持基于Locality优选|ADD PLMN NRFDISCSMFPARA|不支持|本端规划|-
携带Preferred跟踪区标识|ADD PLMN NRFDISCSMFPARA|携带|本端规划|必须在AMF支持I-SMF功能时才能携带该标识。
携带跟踪区标识|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
携带servingScope|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
服务范围组标识|ADD PLMN NRFDISCSMFPARA|0|本端规划|-
服务范围扩展策略|ADD PLMN NRFDISCSMFPARA|不扩展|本端规划|-
配置步骤 :根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|设置AMF发现目标SMF的方式。|ADD SBISRVDISCOVERYMODE:TARGETNFTYPE="SMF_TYPE",DISCOVERYMODE="DYNAMIC_ONLY",IPSELECTMODE="RANDOM",DEFAULTPORTFORHTTP=80,DEFAULTPORTFORHTTPS=443
2|设置AMF是否支持I-SMF配置。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
3|设置NRF发现SMF参数配置。|SET NRFDISCSMFPARACFG:CARRYOIINDNN="NotCarryOI",CARRYSNSSAI="SupSnssai",CARRYPLMN="NotSupPlmn",CARRYNSIID="NotSupNsiId",CARRYLOCALITY="NotSupLocality",CARRYPGWIND="SupCarryPgwInd",SUPPLOCALITYSEL="NOTSUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="NotSupTai",CARRYSERVINGSCOPE="NotSupCarryServingScope",SERVSCOPEGRPID=0,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
4|新增基于PLMN的NRF发现SMF参数配置。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn",CARRYPRELOCALITY="NOTCARRY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="NotSupTai",CARRYSERVINGSCOPE="NotSupCarryServingScope",SERVSCOPEGRPID=0,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
#### 配置实例二（本地发现） 
场景说明 :配置支持AMF通过本地解析方式发现SMF。 
数据规划 :本地发现SMF的数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD SBISRVDISCOVERYMODE|目标NF类型|SMF|本端规划|-
发现方式|ADD SBISRVDISCOVERYMODE|静态|本端规划|-
SET AMFSUPPORTISMF|AMF是否支持I-SMF|支持|本端规划|-
SET NRFDISCSMFPARACFG|DNN携带OI|不支持OI|本端规划|-
携带SNSSAI|SET NRFDISCSMFPARACFG|支持SNNAI|本端规划|-
携带目标PLMN|SET NRFDISCSMFPARACFG|不支持PLMN|本端规划|-
携带切片实例号|SET NRFDISCSMFPARACFG|不支持切片实例号|本端规划|-
携带preferred-locality|SET NRFDISCSMFPARACFG|不携带|本端规划|-
携带pgw-ind标识|SET NRFDISCSMFPARACFG|支持携带pgw-ind标识|本端规划|-
支持基于Locality优选|SET NRFDISCSMFPARACFG|不支持|本端规划|-
携带Preferred跟踪区标识|SET NRFDISCSMFPARACFG|携带|本端规划|该标识仅在AMF支持I-SMF功能时携带。
携带跟踪区标识|SET NRFDISCSMFPARACFG|不携带|本端规划|-
携带servingScope|SET NRFDISCSMFPARACFG|不携带|本端规划|-
服务范围组标识|SET NRFDISCSMFPARACFG|0|本端规划|-
服务范围扩展策略|SET NRFDISCSMFPARACFG|不扩展|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|必须要和SMF的DNN一致。
携带preferred-locality|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
支持基于Locality优选|ADD PLMN NRFDISCSMFPARA|不支持|本端规划|-
携带Preferred跟踪区标识|ADD PLMN NRFDISCSMFPARA|携带|本端规划|必须在AMF支持I-SMF功能时才能携带该标识。
携带跟踪区标识|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
携带servingScope|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
服务范围组标识|ADD PLMN NRFDISCSMFPARA|0|本端规划|-
服务范围扩展策略|ADD PLMN NRFDISCSMFPARA|不扩展|本端规划|-
ADD SBISRVDISCOVERYMODE|目标NF类型|SMF|本端规划|-
发现方式|ADD SBISRVDISCOVERYMODE|静态|本端规划|-
地址选择方式|ADD SBISRVDISCOVERYMODE|随机|本端规划|-
http默认端口|ADD SBISRVDISCOVERYMODE|80|全网规划|-
https默认端口|ADD SBISRVDISCOVERYMODE|443|全网规划|-
本地配置SMF数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD SBIIPV4ADDR|IPv4地址编号|1|本端规划|-
IP地址|ADD SBIIPV4ADDR|192.168.20.100|全网规划|-
ADD SBIIPV4ADDRARRID|IPv4地址组编号|1|本端规划|-
ADD SBIIPV4ADDRARRPARAM|配置索引|1|本端规划|-
IPv4地址组编号|ADD SBIIPV4ADDRARRPARAM|1|本端规划|该参数值引用自ADD SBIIPV4ADDRARRID命令中的ARRAYID参数，必须通过ADD SBIIPV4ADDRARRID命令预先配置。
IPv4地址编号|ADD SBIIPV4ADDRARRPARAM|1|本端规划|该参数值引用自ADD SBIIPV4ADDR命令中的ID参数，必须通过ADD SBIIPV4ADDR命令预先配置。
ADD SBIIPENDPOINT|IP端点编号|1|本端规划|-
IPv4地址编号|ADD SBIIPENDPOINT|1|本端规划|该参数值引用自ADD SBIIPV4ADDR命令中的ID参数，必须通过ADD SBIIPV4ADDR命令预先配置。
端口|ADD SBIIPENDPOINT|8080|全网规划|-
ADD SBIIPENDPOINTARRID|IP端点组编号|1|本端规划|-
ADD SBIIPENDPOINTARRPARAM|配置索引|1|本端规划|-
IP端点组编号|ADD SBIIPENDPOINTARRPARAM|1|本端规划|该参数值引用自ADD SBIIPENDPOINTARRID命令中的ARRAYID参数，必须通过ADD SBIIPENDPOINTARRID命令预先配置。
IP端点编号|ADD SBIIPENDPOINTARRPARAM|1|本端规划|该参数值引用自ADD SBIIPENDPOINT命令中的INDEX参数，必须通过ADD SBIIPENDPOINT命令预先配置。
ADD SBIPLMNID|PLMN ID编号|1|本端规划|-
移动国家码|ADD SBIPLMNID|460|全网规划|-
移动网号|ADD SBIPLMNID|11|全网规划|-
ADD SBIPLMNIDARRID|PLMN ID组编号|1|本端规划|-
ADD SBIPLMNIDARRPARAM|配置索引|1|本端规划|-
PLMN ID组编号|ADD SBIPLMNIDARRPARAM|1|本端规划|该参数值引用自ADD SBIPLMNIDARRID命令中的ARRAYID参数，必须通过ADD SBIPLMNIDARRID命令预先配置。
PLMN ID编号|ADD SBIPLMNIDARRPARAM|1|本端规划|该参数值引用自ADD SBIPLMNID命令中的INDEX参数，必须通过ADD SBIPLMNID命令预先配置。
ADD SBIPLMNNID|PLMN NID编号|1|本端规划|-
PLMN ID编号|ADD SBIPLMNNID|1|本端规划|该参数值引用自ADD SBIPLMNID命令中的INDEX参数，必须通过ADD SBIPLMNID命令预先配置。
网络标识|ADD SBIPLMNNID|1|本端规划|-
ADD SBITAIARRID|TAI组编号|1|本端规划|-
ADD SBITAIARRPARAM|配置索引|1|本端规划|-
TAI组编号|ADD SBITAIARRPARAM|1|本端规划|该参数值引用自ADD SBITAIARRID命令中的ARRAYID参数，必须通过ADD SBITAIARRID命令预先配置。
TAC|ADD SBITAIARRPARAM|150000|本端规划|-
PLMN NID编号|ADD SBITAIARRPARAM|1|本端规划|该参数值引用自ADD SBIPLMNID命令中的INDEX参数，必须通过ADD SBIPLMNID命令预先配置。
ADD SBIDNNARRID|DNN组编号|1|本端规划|-
ADD SBIDNNARRPARAM|配置索引|1|本端规划|-
DNN组编号|ADD SBIDNNARRPARAM|1|本端规划|该参数值引用自ADD SBIDNNARRID命令中的ARRAYID参数，必须通过ADD SBIDNNARRID命令预先配置。
数据网络标识|ADD SBIDNNARRPARAM|zte.com.cn|全网规划|-
ADD SBINFSVERSIONARRID|NF服务版本组编号|1|本端规划|-
ADD SBINFSVERSIONARRPARAM|配置索引|1|本端规划|-
NF服务版本组编号|ADD SBINFSVERSIONARRPARAM|1|本端规划|该参数值引用自ADD SBINFSVERSIONARRID命令中的ARRAYID参数，必须通过ADD SBINFSVERSIONARRID命令预先配置。
API URI版本号|ADD SBINFSVERSIONARRPARAM|v1.0|全网规划|-
API完整版本号|ADD SBINFSVERSIONARRPARAM|1.0.0.alpha-1|全网规划|-
ADD SBISNSSAI|S-NSSAI编号|1|本端规划|-
切片/服务 类型|ADD SBISNSSAI|1|本端规划|-
切片区分符|ADD SBISNSSAI|C02001|本端规划|-
ADD SBISNSSAIARRID|S-NSSAI组编号|1|本端规划|-
ADD SBISNSSAIARRPARAM|配置索引|1|本端规划|-
S-NSSAI组编号|ADD SBISNSSAIARRPARAM|1|本端规划|该参数值引用自ADD SBISNSSAIARRID命令中的ARRAYID参数，必须通过ADD SBISNSSAIARRID命令预先配置。
S-NSSAI编号|ADD SBISNSSAIARRPARAM|1|本端规划|该参数值引用自ADD SBISNSSAI命令中的INDEX参数，必须通过ADD SBISNSSAI命令预先配置。
ADD SBISNSSAISMFINFOARRID|S-NSSAI SMF信息组编号|1|本端规划|-
ADD SBISNSSAISMFINFOARRPARAM|配置索引|1|本端规划|-
S-NSSAI SMF信息组编号|ADD SBISNSSAISMFINFOARRPARAM|1|本端规划|该参数值引用自ADD SBISNSSAISMFINFOARRID命令中的ARRAYID参数，必须通过ADD SBISNSSAISMFINFOARRID命令预先配置。
S-NSSAI编号|ADD SBISNSSAISMFINFOARRPARAM|1|本端规划|该参数值引用自ADD SBISNSSAI命令中的INDEX参数，必须通过ADD SBISNSSAI命令预先配置。
DNN组编号|ADD SBISNSSAISMFINFOARRPARAM|1|本端规划|该参数值引用自ADD SBIDNNARRID命令中的ARRAYID参数，必须通过ADD SBIDNNARRID命令预先配置。
ADD SBISMFINFO|SMF信息编号|1|本端规划|-
S-NSSAI SMF信息组编号|ADD SBISMFINFO|1|本端规划|该参数值引用自ADD SBISNSSAISMFINFOARRID命令中的ARRAYID参数，必须通过ADD SBISNSSAISMFINFOARRID命令预先配置。
TAI组编号|ADD SBISMFINFO|1|本端规划|该参数值引用自ADD SBITAIARRID命令中的ARRAYID参数，必须通过ADD SBITAIARRID命令预先配置。
优先级|ADD SBISMFINFO|65535|本端规划|-
ADD SBIPEERNFBASEINFO|对端NF信息编号|1|本端规划|-
NF实例标识|ADD SBIPEERNFBASEINFO|80444fc1-e4c1-8880-be5f-111111111111|本端规划|-
NF类型|ADD SBIPEERNFBASEINFO|SMF|本端规划|-
NF状态|ADD SBIPEERNFBASEINFO|REGISTERED|本端规划|-
S-NSSAI组编号|ADD SBIPEERNFBASEINFO|1|本端规划|该参数值引用自ADD SBISNSSAIARRID命令中的ARRAYID参数，必须通过ADD SBISNSSAIARRID命令预先配置。
IPv4地址组编号|ADD SBIPEERNFBASEINFO|1|本端规划|该参数值引用自ADD SBIIPV4ADDRARRID命令中的ARRAYID参数，必须通过ADD SBIIPV4ADDRARRID命令预先配置。
优先级|ADD SBIPEERNFBASEINFO|0|本端规划|-
ADD SBIPEERNFEXTINFO|对端NF信息编号|1|本端规划|-
SMF信息编号|ADD SBIPEERNFEXTINFO|1|本端规划|该参数值引用自ADD SBISMFINFO命令中的ID参数，必须通过ADD SBISMFINFO命令预先配置。
ADD SBIPEERNFSERVICEINSTANCE|配置索引|1|本端规划|-
归属NF编号|ADD SBIPEERNFSERVICEINSTANCE|1|本端规划|该参数值引用自ADD SBIPEERNFEXTINFO命令ID参数，必须通过ADD SBIPEERNFEXTINFO命令预先配置。
服务实例标识|ADD SBIPEERNFSERVICEINSTANCE|1|本端规划|-
服务名称|ADD SBIPEERNFSERVICEINSTANCE|NSMF_PDUSESSION|本端规划|-
服务版本组编号|ADD SBIPEERNFSERVICEINSTANCE|1|本端规划|该参数值引用自ADD SBIPEERNFEXTINFO命令中的ID参数，必须通过ADD SBIPEERNFEXTINFO命令预先配置。
协议模式|ADD SBIPEERNFSERVICEINSTANCE|HTTP|本端规划|-
服务实例状态|ADD SBIPEERNFSERVICEINSTANCE|REGISTERED|本端规划|-
容量|ADD SBIPEERNFSERVICEINSTANCE|65535|本端规划|-
优先级|ADD SBIPEERNFSERVICEINSTANCE|65535|本端规划|-
S-NSSAI组编号|ADD SBIPEERNFSERVICEINSTANCE|1|本端规划|该参数值引用自ADD SBISNSSAIARRID命令中的ARRAYID参数，必须通过ADD SBISNSSAIARRID命令预先配置。
配置步骤 :根据规划，进行如下配置。 
本地发现SMF参数
步骤|说明|操作
---|---|---
1|设置AM发现目标SMF的方式。|ADD SBISRVDISCOVERYMODE:TARGETNFTYPE="SMF_TYPE",DISCOVERYMODE="STATIC_ONLY",IPSELECTMODE="RANDOM",DEFAULTPORTFORHTTP=80,DEFAULTPORTFORHTTPS=443
2|设置AMF是否支持I-SMF配置。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
3|设置NRF发现SMF参数配置。|SET NRFDISCSMFPARACFG:CARRYOIINDNN="NotCarryOI",CARRYSNSSAI="SupSnssai",CARRYPLMN="NotSupPlmn",CARRYNSIID="NotSupNsiId",CARRYLOCALITY="NotSupLocality",CARRYPGWIND="SupCarryPgwInd",SUPPLOCALITYSEL="NOTSUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="NotSupTai",CARRYSERVINGSCOPE="NotSupCarryServingScope",SERVSCOPEGRPID=0,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
4|新增基于PLMN的NRF发现SMF参数配置。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn",CARRYPRELOCALITY="NOTCARRY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="NotSupTai",CARRYSERVINGSCOPE="NotSupCarryServingScope",SERVSCOPEGRPID=0,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
5|新增服务发现方式配置，目标NF为SMF，发现方式为静态。|ADD SBISRVDISCOVERYMODE:TARGETNFTYPE="SMF_TYPE",DISCOVERYMODE="STATIC_ONLY",IPSELECTMODE="RANDOM",DEFAULTPORTFORHTTP=80,DEFAULTPORTFORHTTPS=443
本地配置SMF配置
步骤|说明|操作
---|---|---
1|新增IPv4地址配置。|ADD SBIIPV4ADDR:ID=1,IP=192.168.20.100
2|新增IPv4地址组编号配置。|ADD SBIIPV4ADDRARRID:ARRAYID=1
3|新增IPv4地址组参数配置。|ADD SBIIPV4ADDRARRPARAM:INDEX=1,ARRAYID=1,IPV4=1
4|新增IP端点配置。|ADD SBIIPENDPOINT:INDEX=1,IPV4=1,PORT=8080
5|新增IP端点组编号配置。|ADD SBIIPENDPOINTARRID:ARRAYID=1
6|新增IP端点组参数配置。|ADD SBIIPENDPOINTARRPARAM:INDEX=1,ARRAYID=1,IPENDPOINT=1
7|新增PLMN ID配置。|ADD SBIPLMNID:INDEX=1,MCC=460,MNC=11
8|新增PLMN ID组编号配置。|ADD SBIPLMNIDARRID:ARRAYID=1
9|新增PLMN ID组参数配置。|ADD SBIPLMNIDARRPARAM:INDEX=1,ARRAYID=1,PLMNID=1
10|新增PLMN NID配置。|ADD SBIPLMNNID:INDEX=1,PLMNID=1,NID="1"
11|新增TAI组编号配置。|ADD SBITAIARRID:ARRAYID=1
12|新增TAI组参数配置。|ADD SBITAIARRPARAM:INDEX=1,ARRAYID=1,TAC=150000,PLMNNID=1
13|新增DNN组编号配置。|ADD SBIDNNARRID:ARRAYID=1
14|新增DNN组参数配置。|ADD SBIDNNARRPARAM:INDEX=1,ARRAYID=1,DNN="zte.com.cn"
15|新增NF服务版本组编号配置。|ADD SBINFSVERSIONARRID:ARRAYID=1
16|新增NF服务版本组参数配置。|ADD SBINFSVERSIONARRPARAM:INDEX=1,ARRAYID=1,APIVERSIONINURI="v1.0",APIFULLVERSION="1.0.0.alpha-1"
17|新增S-NSSAI配置。|ADD SBISNSSAI:INDEX=1,SST=1,SD="C02001"
18|新增S-NSSAI组编号配置|ADD SBISNSSAIARRID:ARRAYID=1
19|新增S-NSSAI组参数配置。|ADD SBISNSSAIARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=1
20|新增S-NSSAI SMF信息组编号配置。|ADD SBISNSSAISMFINFOARRID:ARRAYID=1
21|新增S-NSSAI SMF信息组参数配置。|ADD SBISNSSAISMFINFOARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=1,DNNARRAY=1
22|新增SMF信息配置，关联TA配置。|ADD SBISMFINFO:ID=1,SNSSAISMFINFOARRAY=1,TAIARRAY=1,PRIORITY=65535
23|新增对端NF基本信息配置，配置对应NF INSTANCE ID，设置NF类型为SMF。|ADD SBIPEERNFBASEINFO:ID=1,NFINSTANCEID="80444fc1-e4c1-8880-be5f-111111111111",NFTYPE="SMF_TYPE",NFSTATUS="REGISTERED",SNSSAIARRAY=1,IPV4ARRAY=1,PRIORITY=0
24|新增对端NF扩展信息配置。|ADD SBIPEERNFEXTINFO:ID=1,SMFINFO=1
25|新增对端NF服务实例配置，关联S-NSSAI配置。|ADD SBIPEERNFSERVICEINSTANCE:INDEX=1,NFINDEX=1,SRVINSTANCEID="1",SERVICENAME="NSMF_PDUSESSION",SERVICEVERSIONARRAY=1,SCHEME="HTTP",NFSERVICESTATUS="REGISTERED",IPENDPOINTARRAY=1,CAPACITY=65535,PRIORITY=65535,SNSSAIARRAY=1
#### 配置实例三（号段解析） 
###### 配置实例1 
场景说明
运营商拨测场景下，配置基于号段选择A-SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET RESOLVESMFPOLICY|支持基于号段选择A-SMF|支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
支持基于号段本地解析A-SMF地址|SET RESOLVESMFPOLICY|支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
ADD RESOSMFPLYBASEDUSER|用户号码|46000999003|本端规划|-
号码类型|ADD RESOSMFPLYBASEDUSER|SUPI|本端规划|-
支持基于号段本地解析A-SMF地址|ADD RESOSMFPLYBASEDUSER|支持|本端规划|-
支持基于号段本地解析I-SMF和V-SMF地址|ADD RESOSMFPLYBASEDUSER|不支持|本端规划|-
号段选择失败后是否重选A-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
号段选择失败后是否重选I-SMF和V-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
ADD SMFIPPOOLCFG|地址池标识|1|本端规划|-
IP地址|ADD SMFIPPOOLCFG|2409:802F:5003:1715::1102:101|全网规划|-
端口号|ADD SMFIPPOOLCFG|80|全网规划|-
ADD RESOLASMFCFG|编号|1|本端规划|-
用户号码|ADD RESOLASMFCFG|46000999003|本端规划|-
号码类型|ADD RESOLASMFCFG|SUPI|本端规划|-
A-SMF FQDN|ADD RESOLASMFCFG|app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org|全网规划|-
地址池标识|ADD RESOLASMFCFG|1|本端规划|-
优先级|ADD RESOLASMFCFG|0|本端规划|-
权重|ADD RESOLASMFCFG|200|本端规划|-
URI scheme|ADD RESOLASMFCFG|HTTP|本端规划|-
API版本|ADD RESOLASMFCFG|V1版本|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",LOCALRESOLVEASMF="NOSPRT"
2|新增用户级解析SMF策略配置。|ADD RESOSMFPLYBASEDUSER:NUMBER="46000999003",NUMTYPE="SUPI",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="NOSPRT",RSASMFANUMFAIL="NORESELECT",RSIVSMFANUMFAIL="NORESELECT"
3|新增SMF 地址池配置。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS="2409:802F:5003:1715::1102:101",PORT=80
4|新增基于号段解析A-SMF配置。|ADD RESOLASMFCFG:ID=1,NUMBER="46000999003",NUMTYPE="SUPI",HOST="app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org",IPPOOLID=1,SCHEMEAPIVERSION="HTTP",APIVERSION="V1"
###### 配置实例2 
场景说明
运营商拨测场景下，配置基于号段选择I/V-SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET RESOLVESMFPOLICY|支持基于号段选择I-SMF和V-SMF|支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
支持基于号段本地解析I-SMF和V-SMF地址|SET RESOLVESMFPOLICY|支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
ADD RESOSMFPLYBASEDUSER|用户号码|46000999003|本端规划|-
号码类型|ADD RESOSMFPLYBASEDUSER|SUPI|本端规划|-
支持基于号段本地解析A-SMF地址|ADD RESOSMFPLYBASEDUSER|不支持|本端规划|-
支持基于号段本地解析I-SMF和V-SMF地址|ADD RESOSMFPLYBASEDUSER|支持|本端规划|-
号段选择失败后是否重选A-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
号段选择失败后是否重选I-SMF和V-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
ADD SMFIPPOOLCFG|地址池标识|1|本端规划|-
IP地址|ADD SMFIPPOOLCFG|2409:802F:5003:1715::1102:101|全网规划|-
端口号|ADD SMFIPPOOLCFG|80|全网规划|-
ADD RESOLIVSMFCFG|编号|1|本端规划|-
用户号码|ADD RESOLIVSMFCFG|46000999003|本端规划|-
号码类型|ADD RESOLIVSMFCFG|SUPI|本端规划|-
A-SMF FQDN|ADD RESOLIVSMFCFG|app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org|全网规划|-
地址池标识|ADD RESOLIVSMFCFG|1|本端规划|-
优先级|ADD RESOLIVSMFCFG|0|本端规划|-
权重|ADD RESOLIVSMFCFG|200|本端规划|-
URI scheme|ADD RESOLIVSMFCFG|HTTP|本端规划|-
API版本|ADD RESOLIVSMFCFG|V1版本|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEIVSMF="NOSPRT"
2|新增用户级解析SMF策略配置。|ADD RESOSMFPLYBASEDUSER:NUMBER="46000999003",NUMTYPE="SUPI",LOCALRESOLVEASMF="NOSPRT",LOCALRESOLVEIVSMF="SPRT",RSASMFANUMFAIL="NORESELECT",RSIVSMFANUMFAIL="NORESELECT"
3|新增SMF 地址池配置。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS="2409:802F:5003:1715::1102:101",PORT=80
4|新增基于号段解析I-SMF和V-SMF配置。|ADD RESOLIVSMFCFG:ID=1,NUMBER="46000999003",NUMTYPE="SUPI",HOST="app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org",IPPOOLID=1,SCHEMEAPIVERSION="HTTP",APIVERSION="V1"
###### 配置实例3 
场景说明
运营商割接场景下，配置基于号段选择A-SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET RESOLVESMFPOLICY|支持基于号段选择A-SMF|支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
支持基于号段本地解析A-SMF地址|SET RESOLVESMFPOLICY|不支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
ADD RESOSMFPLYBASEDUSER|用户号码|46000999003|本端规划|-
号码类型|ADD RESOSMFPLYBASEDUSER|SUPI|本端规划|-
支持基于号段本地解析A-SMF地址|ADD RESOSMFPLYBASEDUSER|不支持|本端规划|-
支持基于号段本地解析I-SMF和V-SMF地址|ADD RESOSMFPLYBASEDUSER|不支持|本端规划|-
号段选择失败后是否重选A-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
号段选择失败后是否重选I-SMF和V-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
ADD RESOLASMFCFG|编号|1|本端规划|-
用户号码|ADD RESOLASMFCFG|46000999003|本端规划|-
号码类型|ADD RESOLASMFCFG|SUPI|本端规划|-
SMF FQDN|ADD RESOLASMFCFG|app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org|全网规划|割接模式根据FQDN在NRF发现结果中匹配指定SMF，FQDN配置需与预期选择SMF的FQDN一致。
地址池标识|ADD RESOLASMFCFG|1|本端规划|-
优先级|ADD RESOLASMFCFG|0|本端规划|-
权重|ADD RESOLASMFCFG|200|本端规划|-
URI scheme|ADD RESOLASMFCFG|HTTP|本端规划|-
API版本|ADD RESOLASMFCFG|V1版本|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",LOCALRESOLVEASMF="NOSPRT"
2|新增用户级解析SMF策略配置。|ADD RESOSMFPLYBASEDUSER:NUMBER="46000999003",NUMTYPE="SUPI",LOCALRESOLVEASMF="NOSPRT",LOCALRESOLVEIVSMF="NOSPRT",RSASMFANUMFAIL="NORESELECT",RSIVSMFANUMFAIL="NORESELECT"
3|新增基于号段解析A-SMF配置。|ADD RESOLASMFCFG:ID=1,NUMBER="46000999003",NUMTYPE="SUPI",HOST="app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org",IPPOOLID=1,SCHEMEAPIVERSION="HTTP",APIVERSION="V1"
###### 配置实例4 
场景说明
运营商割接场景下，配置基于号段选择I/V-SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET RESOLVESMFPOLICY|支持基于号段选择I-SMF和V-SMF|支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
支持基于号段本地解析I-SMF和V-SMF地址不支持|SET RESOLVESMFPOLICY|不支持|本端规划|该命令的配置结果优先级低于ADD RESOSMFPLYBASEDUSER命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了ADD RESOSMFPLYBASEDUSER。如果其中一个号码能够匹配成功，则使用ADD RESOSMFPLYBASEDUSER命令的配置结果。如果两个号码均没有匹配成功，则使用SET RESOLVESMFPOLICY命令的配置结果。
ADD RESOSMFPLYBASEDUSER|用户号码|46000999003|本端规划|-
号码类型|ADD RESOSMFPLYBASEDUSER|SUPI|本端规划|-
支持基于号段本地解析A-SMF地址|ADD RESOSMFPLYBASEDUSER|不支持|本端规划|-
支持基于号段本地解析I-SMF和V-SMF地址|ADD RESOSMFPLYBASEDUSER|不支持|本端规划|-
号段选择失败后是否重选A-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
号段选择失败后是否重选I-SMF和V-SMF|ADD RESOSMFPLYBASEDUSER|不重选|本端规划|-
ADD RESOLIVSMFCFG|编号|1|本端规划|-
用户号码|ADD RESOLIVSMFCFG|46000999003|本端规划|-
号码类型|ADD RESOLIVSMFCFG|SUPI|本端规划|-
SMF FQDN|ADD RESOLIVSMFCFG|app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org|全网规划|割接模式根据FQDN在NRF发现结果中匹配指定SMF，FQDN配置需与预期选择SMF的FQDN一致。
地址池标识|ADD RESOLIVSMFCFG|1|本端规划|-
优先级|ADD RESOLIVSMFCFG|0|本端规划|-
权重|ADD RESOLIVSMFCFG|200|本端规划|-
URI scheme|ADD RESOLIVSMFCFG|HTTP|本端规划|-
API版本|ADD RESOLIVSMFCFG|V1版本|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEIVSMF="NOSPRT"
2|新增用户级解析SMF策略配置。|ADD RESOSMFPLYBASEDUSER:NUMBER="46000999003",NUMTYPE="SUPI",LOCALRESOLVEASMF="NOSPRT",LOCALRESOLVEIVSMF="NOSPRT",RSASMFANUMFAIL="NORESELECT",RSIVSMFANUMFAIL="NORESELECT"
3|新增基于号段解析I-SMF和V-SMF配置。|ADD RESOLIVSMFCFG:ID=1,NUMBER="46000999003",NUMTYPE="SUPI",HOST="app-hdnjihjxsmf001bzx-05azx011.nc.jx.node.5gc.mnc000.mcc460.3gppnetwork.org",IPPOOLID=1,SCHEMEAPIVERSION="HTTP",APIVERSION="V1"
#### 配置实例四（基于签约SMF List选择A-SMF） 
场景说明 :AMF基于UDM签约的SMF ID，通过NRF发现获取A-SMF列表并进行选择，若选择失败可基于DNN重选SMF。 
数据规划 :命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET ASMFSELPOLICY|支持基于签约SMF ID选择A-SMF|支持|本端规划|-
基于签约SMF ID选择失败后是否重选A-SMF|SET ASMFSELPOLICY|是|本端规划|-
配置步骤 :根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|设置支持基于签约的SMF ID选择A-SMF，如果选择失败，重选SMF。|SET ASMFSELPOLICY:SUPSELSMFBYSUBSMFID="SUPPORT",RESELSMFBYSUBSMFID="YES"
#### 配置实例五（基于Locality选择SMF） 
###### 配置实例1 
场景说明
在有多个SMF的情况下，优先选择同DC的SMF接入，尽量避免跨DC的信令交互。 
使用NRF优选方式选择SMF，AMF通过NRF发现SMF时携带preferred-locality参数，NRF使用该参数进行SMF发现。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|-
携带preferred-locality|ADD PLMN NRFDISCSMFPARA|携带|本端规划|-
支持基于Locality优选|ADD PLMN NRFDISCSMFPARA|不支持|本端规划|-
SET NRFDISCSMFPARACFG|携带preferred-locality|携带|本端规划|-
支持基于Locality优选|SET NRFDISCSMFPARACFG|不支持|本端规划|-
ADD PREFER LOCALITY|NF类型|SMF|本端规划|-
优选位置|ADD PREFER LOCALITY|nanjing.dc|本端规划|-
指定位置无效是否使用本地位置|ADD PREFER LOCALITY|是|本端规划|-
配置步骤
步骤|说明|操作
---|---|---
1|基于PLMN的NRF发现A-SMF时，携带preferred-locality，不支持基于Locality优选。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="NULL",CARRYPRELOCALITY="CARRY",SUPPLOCALITYSEL="NOTSUPPORT"
2|AMF通过NRF发现A-SMF时，携带preferred-locality，不支持基于Locality优选。|SET NRFDISCSMFPARACFG:CARRYLOCALITY="SupLocality",SUPPLOCALITYSEL="NOTSUPPORT"
3|AMF通过NRF发现SMF时，优选支持包含"nanjing.dc"locality的SMF。|ADD PREFER LOCALITY:NFTYPE="SMF",PRELOCALITY="nanjing.dc",USELOCLOACLITY="YES"
###### 配置实例2 
场景说明
在有多个SMF的情况下，优先选择同DC的SMF接入，尽量避免跨DC的信令交互。 
使用本地优选方式选择SMF，AMF通过NRF发现SMF时不携带preferred-locality参数，本地基于Locality在NRF返回的SMF中选择SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|-
携带preferred-locality|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
支持基于Locality优选|ADD PLMN NRFDISCSMFPARA|支持|本端规划|-
SET NRFDISCSMFPARACFG|携带preferred-locality|不携带|本端规划|-
支持基于Locality优选|SET NRFDISCSMFPARACFG|支持|本端规划|-
ADD PREFER LOCALITY|NF类型|SMF|本端规划|-
优选位置|ADD PREFER LOCALITY|nanjing.dc|本端规划|-
指定位置无效是否使用本地位置|ADD PREFER LOCALITY|是|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|基于PLMN的NRF发现A-SMF时，不携带preferred-locality，支持基于Locality优选。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="NULL",CARRYPRELOCALITY="NOTCARRY",SUPPLOCALITYSEL="SUPPORT"
2|AMF通过NRF发现A-SMF时，不携带preferred-locality，支持基于Locality优选。|SET NRFDISCSMFPARACFG:CARRYLOCALITY="NotSupLocality",SUPPLOCALITYSEL="SUPPORT"
3|AMF通过NRF发现SMF时，优选支持包含"nanjing.dc"locality的SMF。|ADD PREFER LOCALITY:NFTYPE="SMF",PRELOCALITY="nanjing.dc",USELOCLOACLITY="YES"
#### 配置实例六（基于ServingScope选择SMF） 
###### 配置实例1 
场景说明
当SMF只为某些区域服务时，SMF在向NRF注册时携带支持的服务范围。AMF可以根据ServingScope选择服务于特定区域的SMF。 
AMF和SMF服务范围一致（例如：按大区/省集中部署），需要AMF基于ServingScope就近选择本大区/省SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD SMF SERVSCOPE GRP|服务范围组标识|1|本端规划|-
服务范围|ADD SMF SERVSCOPE GRP|Nanjing|本端规划|-
SET NRFDISCSMFPARACFG|携带SNSSAI|支持SNSSAI|本端规划|-
携带servingScope|SET NRFDISCSMFPARACFG|携带|本端规划|-
服务范围组标识|SET NRFDISCSMFPARACFG|1|本端规划|该参数值引用自ADD SMF SERVSCOPE GRP命令中的SERVSCOPEGRPID参数，必须通过ADD SMF SERVSCOPE GRP命令预先配置。
服务范围扩展策略|SET NRFDISCSMFPARACFG|不扩展|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|zte.com.cn|全网规划|-
携带servingScope|ADD PLMN NRFDISCSMFPARA|携带|本端规划|-
服务范围组标识|ADD PLMN NRFDISCSMFPARA|1|本端规划|该参数值引用自ADD SMF SERVSCOPE GRP命令中的SERVSCOPEGRPID参数，必须通过ADD SMF SERVSCOPE GRP命令预先配置。
服务范围扩展策略|ADD PLMN NRFDISCSMFPARA|不扩展|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|新增SMF服务范围组配置，服务范围组标识为1，服务范围为Nanjing。|ADD SMF SERVSCOPE GRP:SERVSCOPEGRPID=1,SERVINGSCOPE="Nanjing"
2|AMF通过NRF发现A-SMF时携带ServingScope。|SET NRFDISCSMFPARACFG:CARRYSNSSAI="SupSnssai",CARRYSERVINGSCOPE="SupCarryServingScope",SERVSCOPEGRPID=1,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
3|基于PLMN的NRF发现A-SMF时携带ServingScope。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn",CARRYSERVINGSCOPE="SupCarryServingScope",SERVSCOPEGRPID=1,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
###### 配置实例2 
场景说明
当SMF只为某些区域服务时，SMF在向NRF注册时携带支持的服务范围。AMF可以根据servingScope选择服务于特定区域的SMF。 
AMF服务范围大于SMF服务范围（例如：AMF按大区/省集中部署，SMF按地市下沉部署），需要AMF基于ServingScope就近选择本地市SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
ADD SMF SERVSCOPE GRP|服务范围组标识|1|本端规划|-
服务范围|ADD SMF SERVSCOPE GRP|Nanjing|本端规划|-
ADD SMF SERVSCOPE TA GRP|跟踪区组标识|1|本端规划|-
移动国家码|ADD SMF SERVSCOPE TA GRP|460|本端规划|-
移动网络码|ADD SMF SERVSCOPE TA GRP|11|本端规划|-
跟踪区码|ADD SMF SERVSCOPE TA GRP|000000|本端规划|-
跟踪区码起始|ADD SMF SERVSCOPE TA GRP|000100|本端规划|-
跟踪区码终止|ADD SMF SERVSCOPE TA GRP|000200|本端规划|-
服务范围组标识|ADD SMF SERVSCOPE TA GRP|1|本端规划|该参数值引用自ADD SMF SERVSCOPE GRP命令中的SERVSCOPEGRPID参数，必须通过ADD SMF SERVSCOPE GRP命令预先配置。
SET NRFDISCSMFPARACFG|携带SNSSAI|支持SNSSAI|本端规划|-
携带Preferred跟踪区标识|SET NRFDISCSMFPARACFG|携带|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|zte.com.cn|全网规划|-
携带servingScope|ADD PLMN NRFDISCSMFPARA|携带|本端规划|-
服务范围扩展策略|ADD PLMN NRFDISCSMFPARA|基于TA信息映射|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|新增SMF服务范围组配置，服务范围组标识为1，服务范围为Nanjing。|ADD SMF SERVSCOPE GRP:SERVSCOPEGRPID=1,SERVINGSCOPE="Nanjing"
2|新增SMF服务范围跟踪区组配置，配置一组TA关联一个SMF服务范围。|ADD SMF SERVSCOPE TA  GRP:TAGROUPID=1,MCC="460",MNC="11",TAC="000000",TACST="000100",TACEND="000200",SERVSCOPEGRPID=1
3|AMF通过NRF发现A-SMF时携带ServingScope。|SET NRFDISCSMFPARACFG:CARRYSNSSAI="SupSnssai",CARRYPREFERREDTAI="SupPreferredTai"
4|基于PLMN的NRF发现A-SMF时携带ServingScope。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn",CARRYSERVINGSCOPE="SupCarryServingScope",SERVSCOPEEXTPLY="SupServScopeExtPly"
#### 配置实例七（同一用户的多个会话选择相同SMF） 
场景说明 :为了减少5G切4G场景下不同DC间的S5口流量，AMF在选择SMF时，同一个用户的多个会话锚定在同一个SMF上。 
数据规划 :命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET ASMFSELPOLICY|A-SMF选择支持优选TA|不支持|本端规划|-
相同DNN选择同一ASMF|SET ASMFSELPOLICY|不支持|本端规划|-
支持不同DNN的多PDU会话选择同一个A-SMF|SET ASMFSELPOLICY|支持|本端规划|-
支持基于签约SMF ID选择A-SMF|SET ASMFSELPOLICY|不支持|本端规划|-
基于签约SMF ID选择失败后是否重选A-SMF|SET ASMFSELPOLICY|否|本端规划|-
配置步骤 :根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|支持同一用户的多个会话选择相同SMF|SET ASMFSELPOLICY:AMFSELASMFBYTA="NOTSUPPORT",AMFSELSAMEASMFBYDNN="NOTSUPPORT",SUPSAMESMFDIFFDNN="SUPPORT",SUPSELSMFBYSUBSMFID="NOTSUPPORT",RESELSMFBYSUBSMFID="NO"
#### 配置实例八（基于TAI选择SMF） 
###### 配置实例1 
场景说明
当SMF只服务于特定跟踪区时，SMF在向NRF注册时携带支持的跟踪区信息。AMF根据UE当前位置（即TAI）选择特定SMF。
AMF通过NRF发现A-SMF时携带preferred-tai参数，NRF使用该参数进行SMF发现。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET NRFDISCSMFPARACFG|携带Preferred跟踪区标识|携带|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|-
携带Preferred跟踪区标识|ADD PLMN NRFDISCSMFPARA|携带|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|AMF通过NRF发现A-SMF时携带Preferred跟踪区标识。|SET NRFDISCSMFPARACFG:CARRYPREFERREDTAI="SupPreferredTai"
2|基于PLMN的NRF发现A-SMF时携带Preferred跟踪区标识。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="NULL",CARRYPREFERREDTAI="SupPreferredTai"
###### 配置实例2 
场景说明
当SMF只服务于特定跟踪区时，SMF在向NRF注册时携带支持的跟踪区信息。AMF根据UE当前位置（即，TAI）选择特定SMF。 
AMF通过NRF发现A-SMF时不携带preferred-tai参数或者NRF不支持preferred-tai时，AMF基于TAI从NRF返回的结果中优选SMF。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET ASMFSELPOLICY|A-SMF选择支持优选TA|支持|本端规划|-
SET NRFDISCSMFPARACFG|携带Preferred跟踪区标识|不携带|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|-
携带Preferred跟踪区标识|ADD PLMN NRFDISCSMFPARA|不携带|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|AMF选择支持优选TA。|SET ASMFSELPOLICY:AMFSELASMFBYTA="SUPPORT"
2|AMF通过NRF发现A-SMF时不携带Preferred跟踪区标识。|SET NRFDISCSMFPARACFG:CARRYPREFERREDTAI="NotSupPreferredTai"
3|基于PLMN的NRF发现A-SMF时不携带Preferred跟踪区标识。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="NULL",CARRYPREFERREDTAI="NotSupPreferredTai"
###### 配置实例3 
场景说明
基于TAI选择SMF：当SMF只服务于特定跟踪区时，SMF在向NRF注册时携带支持的跟踪区信息。AMF根据UE当前位置（即，TAI）选择特定SMF。 
AMF通过NRF发现H-SMF时携带tai参数，NRF使用该参数进行SMF发现。 
数据规划
命令|参数名称|取值样例|数据来源|说明
---|---|---|---|---
SET NRFDISCSMFPARACFG|携带跟踪区标识|携带|本端规划|-
ADD PLMN NRFDISCSMFPARA|移动国家码|460|全网规划|-
移动网络码|ADD PLMN NRFDISCSMFPARA|11|全网规划|-
DNN|ADD PLMN NRFDISCSMFPARA|NULL|全网规划|-
携带跟踪区标识|ADD PLMN NRFDISCSMFPARA|携带|本端规划|-
配置步骤
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|AMF通过NRF发现A-SMF时携带跟踪区标识。|SET NRFDISCSMFPARACFG:CARRYTA="SupTai"
2|基于PLMN的NRF发现A-SMF时携带跟踪区标识。|ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="NULL",CARRYTA="SupTai"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF根据优先级选择SMF
---|---
测试目的|验证SMF互备组网时，AMF根据优先级选择本地区域SMF
预置条件|用户在UDM中已签约5G业务。SMF采用互备组网，并向NRF注册完成。在AMF上按照配置实例一（NRF发现）的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU会话建立成功。SMF选择成功，选择优先级高的SMF。通过信令跟踪能够跟踪到相应的消息，流程正确。
测试结果|-
测试项目|AMF通过本地解析方式选择SMF
---|---
测试目的|AMF根据本地配置能够选择正确的SMF
预置条件|用户在UDM中已签约5G业务。在AMF上按照配置实例二（本地发现）的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU会话建立成功。通过信令跟踪功能，确认SMF选择过程中，未向NRF发出发现请求消息，AMF进行SMF本地解析。SMF选择成功，选择优先级高的SMF。
测试结果|-
测试项目|拨测场景下，AMF基于用户号段选择SMF
---|---
测试目的|验证AMF能够在拨测场景下选择正确的SMF
预置条件|用户在UDM中已签约5G业务。在AMF上按照配置实例三（号段解析）中配置实例1的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU会话建立成功。成功选择新入网的SMF。通过信令跟踪功能，确认AMF没有向NRF发出的发现请求消息，其他消息及流程正确。
测试结果|-
测试项目|割接场景下，AMF基于用户号段选择SMF
---|---
测试目的|验证AMF能够在割接场景下选择正确的SMF
预置条件|用户在UDM中已签约5G业务。在AMF上按照配置实例三（号段解析）中配置实例3的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU会话建立成功。部分号段用户迁入正确的SMF。通过信令跟踪功能，确认AMF没有向NRF发出的发现请求消息，其他消息及流程正确。
测试结果|-
测试项目|AMF根据UDM签约的SMF ID选择SMF
---|---
测试目的|验证AMF基于UDM签约的SMF ID选择正确的SMF
预置条件|用户在UDM中已签约5G业务和SMF ID。在AMF上按照配置实例四（基于签约SMF List选择A-SMF）中的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的信息。
通过准则|UE注册成功，PDU会话建立成功。通过信令跟踪功能，确认NRF发现SMF时使用的是用户签约的SMF ID。
测试结果|-
测试项目|AMF基于Locality优先选择同DC的SMF
---|---
测试目的|验证在有多个SMF的情况下，AMF基于Locality优先选择同DC的SMF接入，避免跨DC的信令交互
预置条件|在AMF上按照配置实例五（基于Locality选择SMF）中的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU会话建立成功。通过信令跟踪功能，确认AMF向NRF发起发现SMF的请求时，携带了preferred-locality参数。NRF向AMF返回的响应中携带匹配preferred-locality的SMF列表。
测试结果|-
测试项目|AMF基于ServingScope选择SMF
---|---
测试目的|验证AMF基于ServingScope选择服务于特定区域的SMF
预置条件|在AMF上按照配置实例六（基于ServingScope选择SMF）中的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU建立成功。通过信令跟踪功能，确认AMF向NRF发起发现SMF的请求时，携带了ServingScope参数。NRF向AMF返回的响应中携带匹配ServingScope的SMF列表。
测试结果|-
测试项目|AMF支持为同一用户的多个会话选择相同的SMF
---|---
测试目的|验证AMF在选择SMF时，为同一个用户的多个会话选择同一个SMF
预置条件|在AMF上按照配置实例七（同一用户的多个会话选择相同SMF）中的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程，使用名称为“cmnet”的DNN建立PDU会话1，使用名称为“ims”的DNN建立PDU会话2。在网络侧查询用户的会话信息。
通过准则|2个PDU会话建立成功，并且2个会话选择同一个SMF。
测试结果|-
测试项目|AMF支持基于TAI优选正确的SMF
---|---
测试目的|验证AMF基于TAI选择服务于特定跟踪区的SMF
预置条件|在AMF上按照配置实例八（基于TAI选择SMF）中的数据规划和配置步骤执行成功。为SMF设置不同的优先级。在AMF上建立用户信令跟踪。
测试过程|UE开机，发起注册流程。UE发起PDU会话建立流程。在网络侧查询用户的会话信息。
通过准则|UE注册成功，PDU会话建立成功。AMF成功选择到服务于特定跟踪区的SMF。通过信令跟踪能够跟踪到相应的消息，流程正确。
测试结果|-
常见问题处理 :无。 
## ZUF-79-10-002 AMF选择 
概述 :AMF选择功能选择可用的AMF为UE服务。根据网络拓扑进行选择，即，所选的AMF服务于UE所在的区域，对于服务区重叠的AMF，优先选择服务区内AMF更换概率小的AMF。 
客户收益 :本特性选择可用的AMF为UE服务。 
说明 :当UE在5G网络中移动，且目标区域不再是当前为UE服务的AMF的服务区时，需要根据目标区域选择新的AMF为该UE服务。 
AMF携带以下信息向NRF查询获取新的AMF。 
S-NSSAI 
源AMF集ID（Source AMF Set ID） 
源AMF区域ID（Source AMF Region ID） 
目标区域（Target location） 
NRF根据以上信息在目标AMF区域的目标AMF集合中提供目标AMF列表，AMF根据NRF返回的结果选择新的AMF。 
当多个AMF满足这些必要条件时，AMF可以根据多个策略选择一个AMF。不同的应用场景使用不同的选择策略，可以组合使用如下策略： 
优先级：AMF间互备 
权重：AMF间负荷分担 
动态负荷：AMF实时负荷调整 
## ZUF-79-10-003 UDM选择 
概述 :UDM选择功能选择可用的UDM为UE服务。 
客户收益 :本特性选择可用的UDM为UE服务。 
说明 :当UE在网络注册时，需要选择UDM进行注册。AMF携带如下信息，用于从NRF查询获取UDM： 
PLMN 
SUPI 
preferred-locality 
NRF根据上述信息匹配UDM列表，AMF根据NRF返回的结果选择UDM。 
当多个UDM满足这些必要条件时，AMF可以根据多个策略选择一个UDM。不同的应用场景使用不同的选择策略，可以组合使用如下策略： 
优先级：UDM间互备 
权重：UDM间负荷分担 
动态负荷：UDM实时负荷调整 
locality：UDM跨DC负荷分担，AMF基于locality优选与本地位置或指定位置相同的UDM。 
## ZUF-79-10-004 PCF选择 
概述 :PCF选择功能选择可用的PCF为UE服务。 
客户收益 :本特性选择可用的PCF为UE服务。 
说明 :当UE在网络注册时，AMF选择一个PCF为UE建立策略关联。AMF携带以下信息向NRF查询获取PCF： 
PLMN 
SUPI 
NRF根据上述信息匹配PCF列表，AMF根据NRF返回的结果选择PCF。 
当多个PCF满足这些必要条件时，AMF可以根据多个策略选择一个PCF。不同的应用场景使用不同的选择策略，可以组合使用如下策略： 
优先级：PCF间互备 
权重：PCF间负荷分担 
动态负荷：PCF实时负荷调整 
## ZUF-79-10-005 MME选择 
概述 :当UE从5G网络移动到4G网络时，AMF选择可用的MME为UE服务。 
客户收益 :本特性选择一个可用的MME为移动到4G网络的UE提供服务。 
说明 :当UE从5G网络移动到4G网络时，AMF根据目标位置选择MME。AMF根据目标TA从DNS查询获取MME列表，并根据DNS返回的结果选择MME。 
当多个MME满足这些必要条件时，AMF可以根据多个策略选择一个MME。不同的应用场景使用不同的选择策略，可以组合使用如下策略： 
优先级：MME间互备 
权重：MME间负荷分担 
## ZUF-79-10-006 NSSF选择 
概述 :当UE注册或发起PDU会话建立时，AMF选择可用的NSSF为UE服务。
客户收益 :本特性选择可用的NSSF为UE服务。 
说明 :当UE注册或发起PDU会话建立时，AMF在本地配置NSSF地址并选择合适的NSSF获取UE的网络切片信息。 
## ZUF-79-10-007 NRF选择 
概述 :当UE注册或发起PDU会话建立时，AMF选择可用的NRF为UE服务。
客户收益 :本特性选择可用的NRF为UE服务。 
说明 :当UE注册或发起PDU会话建立时，AMF选择合适的NRF进行注册和发现。 
AMF可以在本地配置NRF地址，选择合适的NRF，并支持NSSF指定NRF。 
## ZUF-79-10-008 SMSF选择 
概述 :SMSF选择功能为UE选择可用的SMSF。
客户收益 :该功能为UE选择可用的SMSF。 
说明 :当UE在网络中注册并发送NAS消息时，AMF将选择合适的SMSF进行短消息传输。AMF可以从旧的AMF或UDM获得服务PLMN中的SMSF信息。AMF携带SUPI/GPSI，从NRF查询获取SMSF；或者AMF使用SUPI通过本地配置查询获取SMSF。NRF/AMF根据以上信息匹配SMSF列表，并且根据NRF或本地配置返回的结果选择SMSF。 
当多个SMSF满足这些条件时，AMF可以根据多个策略选择一个SMSF。不同的应用场景下，AMF可选以下策略： 
优先级：SMSF间互备 
权重：SMSF间负荷分担 
动态负荷：SMSF实时负荷调整 
## ZUF-79-10-009 AUSF选择 
概述 :AUSF选择功能用于选择可用的AUSF为UE服务。
客户收益 :该功能用于为UE选择可用的AUSF。 
说明 :UE在注册时，如果AMF要执行与UE的鉴权过程，则需要选择AUSF。AMF通过NRF查询得到AUSF，查询时携带： 
SUPI 
routing-indicator 
preferred-locality 
NRF根据查询条件匹配到AUSF列表，AMF完全根据NRF返回结果进行选择。 
当NRF不可用或没有部署时，AMF提供本地配置解析AUSF，本地支持配置SUPI、routing-indicator对应的AUSF列表，AMF根据查询结果进行选择。 
当有多个AUSF符合必要条件时，AMF可以根据多种策略进行优选，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用。 
优先级：用于AUSF间互相备份。 
权重：用于AUSF间负荷分担。 
locality：AUSF跨DC负荷分担，AMF基于locality优选与本地位置或指定位置相同的AUSF。 
AUSF选择策略具体参见3GPP 23.501协议6.3.4 AUSF discovery and selection章节。 
## ZUF-79-10-010 GMLC选择 
概述 :GMLC选择功能用于选择可用的GMLC为UE服务。
客户收益 :本功能用于为UE选择可用的GMLC。 
说明 :定位流程中，AMF需要选择GMLC。AMF通过NRF查询得到GMLC，查询时携带locality。 
NRF根据查询条件匹配到GMLC列表，AMF完全根据NRF返回结果进行选择。 
当NRF不可用或没有部署时，AMF提供本地配置GMLC列表，AMF根据查询结果进行选择。 
当有多个GMLC符合必要条件时，AMF可以根据多种策略进行优选，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用。 
优先级：用于GMLC间互相备份。 
权重：用于GMLC间负荷分担。 
## ZUF-79-10-011 LMF选择 
概述 :LMF选择功能用于选择可用的LMF为UE服务。
客户收益 :本功能用于为UE选择可用的LMF。 
说明 :定位流程中，AMF需要选择LMF。AMF通过NRF查询得到LMF，查询时携带locality。 
NRF根据查询条件匹配到LMF列表，AMF完全根据NRF返回结果进行选择。 
当NRF不可用或没有部署时，AMF提供本地配置LMF列表。AMF根据SUPI和GPSI做匹配查询，根据查询结果进行选择。 
当有多个LMF符合必要条件时，AMF可以根据多种策略进行优选，不同的选择策略对应不同的应用场景，以下各选择策略可以组合使用。 
优先级：用于LMF间互相备份。 
权重：用于LMF间负荷分担。 
# 缩略语 
# 缩略语 
AUSF :Authentication Server Function鉴权服务器功能
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
## LMF 
Location Management Function定位管理功能
NRF :NF Repository Function网络功能仓储
NSSF :Network Slice Selection Function网络切片选择功能
## SMSF 
Short Message Service Function短消息服务功能
# ZUF-79-11 UE能力及无线资源管理 
## ZUF-79-11-001 UE无线能力处理 


概述 :本特性使AMF能够处理UE的无线能力。 


客户收益 :AMF根据UE的无线能力对UE进行合理的管理。 


说明 :当UE接入网络时，将其无线能力信息携带给AMF。AMF保存这些信息并在后续流程中提供给NR，因此NR不必在各个流程获取这些信息，从而节省空口资源。 


## ZUF-79-11-002 UE核心网能力处理 


概述 :本特性使AMF能够处理UE的核心网能力。 


客户收益 :AMF根据UE的核心网能力对UE进行合理的管理。 


说明 :UE MM核心网能力包括UE网络能力、5GMM能力和非无线相关能力。UE网络能力在所有CN节点之间进行转发。5GMM能力仅在AMF更换为其他AMF时进行转发。 


## ZUF-79-11-003 DRX 


概述 :不连续接收（DRX）参数用于指示UE是否使用DRX模式。 


客户收益 :本特性使UE选择DRX模式以节省UE功耗。 


说明 :DRX持续时间由UE和AMF协商确定，用于RRC-Inactive的CM-IDLE和CM-CONNECTED状态。 
如果UE想要使用特定的DRX参数，UE应在所有初始注册和移动性注册过程中始终包含其首选值。 
AMF应根据接收到的UE特定的DRX参数确定Accepted DRX参数，AMF应接受UE请求的值，但AMF根据运营商策略可以改变UE请求的值。 


## ZUF-79-11-004 配置传输 
概述 :AMF将一个5G-RAN的无线信息转发给另一个5G-RAN。 
客户收益 :本特性减少RAN之间的直连接，并在RAN之间转发参数。 
说明 :当RAN之间没有直连接口，而RAN之间又需要传输无线信息时，AMF可以在RAN之间传输无线信息，比如SON。 
## ZUF-79-11-005 RFSP 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :RFSP是3GPP协议定义的概念，是指NG-RAN进行无线资源管理时所采用的策略。
RFSP索引（Index to RAT/Frequency Selection Priority，接入方式/频率选择优先级索引），定义了UE对不同接入方式/频率的选择优先级，不同的接入方式/频率选择优先级可以使用不同的RFSP索引取值来表示。
5G网络中，在UE进行注册、业务请求等流程时，通过AMF将使用的RFSP索引下发给NG-RAN，NG-RAN可以根据RFSP索引实施无线资源管理策略，灵活控制UE的行为策略，例如指定UE驻留和切换频段的优先级等。 
背景知识 :3GPP协议中定义了无线资源管理，即在特定用户信息的基础上分配和维护无线信道，由NG-RAN完成。 
为了支持NG-RAN的无线资源管理，AMF应支持通过协作完成无线信道的分配和维护。 
AMF应支持将使用的RFSP索引下发给NG-RAN，NG-RAN通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。 
终端根据此列表信息，辅助NG-RAN进行驻留优先级控制，切换控制到适宜的小区，以减少网络中的无用信令，提升网络资源利用率，并提高终端用户体验。 
应用场景 :为语言业务为主用户降低时延。5G部署初期，语音为主的用户只能回落到LTE网络进行语音业务，但是通过LTE网络进行语音，接入时延会增加1~2秒。针对此类以语音业务为主的用户，优先驻留在E-UTRA网络，解决接入时延的问题。 
区分用户群，保证用户体验。某城市用户多，频谱资源紧张，通过RFSP策略控制资源使用，区分不同用户群，保证优质用户的体验。 
满足不同网络切片提供个性化服务要求5G网络切片使运营商在同一套硬件基础设施上可以按需切分出多个虚拟的端到端逻辑网络，适配各种类型服务的不同特征及需求，通过RFSP索引区分不同的网络切片，满足高带宽、低时延、超大连接等不同业务对资源的要求。  
客户收益 :受益方|受益描述
---|---
运营商|避免反复的小区重选和切换，减少网络信令。便于运营商灵活分配和维护无线资源，提高整个网络或特定用户的体验。
移动用户|优先驻留和切换到最适宜的小区，有利于终端省电。减少终端接入的时延。
实现原理 :系统架构 :在5G网络中，AMF通过N8接口从UDM获取签约的RFSP索引，通过N15接口将签约的RFSP索引传递给PCF并从PCF获取授权的RFSP索引，结合本地策略获得使用的RFSP索引，通过N2接口向(R)AN提供RFSP索引。(R)AN通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。
RFSP涉及的组网架构如下图所示。 
图1  RFSP涉及的组网架构

涉及的网元 :NF名称|NF作用
---|---
UE|接收NG-RAN下发的频段优先级列表。
NG-RAN|接收AMF下发的RFSP索引，通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。
AMF|从UDM接收签约的RFSP索引，将签约的RFSP索引传递给PCF并从PCF接收授权的RFSP索引。在注册、业务请求、签约或者授权的RFSP索引变更流程中，基于签约的RFSP索引、授权的RFSP索引以及本地策略，决策出使用的RFSP索引，传递给NG-RAN。在局间注册更新、局间N2切换流程中，源AMF向目标AMF传递签约和使用的RFSP索引，目标AMF基于签约的RFSP索引、授权的RFSP索引以及本地策略，决策出新的供使用的RFSP索引，传递给NG-RAN。
UDM|将用户签约的RFSP索引下发给AMF。
PCF|接收AMF传递的签约的RFSP索引，基于本地策略决策出授权的RFSP索引，下发给AMF。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N15|ZUF-79-19-007 N15
本网元实现 :AMF在注册流程中，从UDM接收签约的RFSP索引，将签约的RFSP索引传递给PCF并从PCF接收授权的RFSP索引。 
AMF在注册、业务请求、签约或者授权的RFSP索引变更流程中，基于签约的RFSP索引、授权的RFSP索引以及本地策略，决策出使用的RFSP索引，传递给NG-RAN。 
在局间注册更新、局间N2切换流程中，从源AMF向目标AMF传递签约和使用的RFSP索引，目标AMF基于签约的RFSP索引、授权的RFSP索引以及本地策略，决策出新的使用的RFSP索引，传递给NG-RAN。 
业务流程 :AMF在注册流程中，从UDM接收签约的RFSP索引，将签约的RFSP索引传递给PCF并从PCF接收授权的RFSP索引。在如下业务流程中基于本地策略协商获得使用的RFSP索引，传递给NG-RAN： 
注册 
业务请求 
签约或授权的RFSP变更 
局间注册更新 
局间N2切换 
AMF可以基于如下因素确定本地策略： 
SUPI 
UE's usage setting 
允许的NSSAI 
根据SUPI号段、UE's usage setting和/或Allowed NSSAI无法确定本地策略时，则使用默认的本地策略。 
UE's usage setting，有下面两种方式： 
Voice centric：UE的现有状态必须能提供语音业务，如果不能提供语音业务，UE会重新选择新的RAT接入移动网络。 
Data centric：UE的现有状态必须能提供数据业务，如果不能提供数据业务，UE会重新选择新的RAT接入移动网络。 
本地策略，包括如下几种： 
不携带RFSP：不下发RFSP给NG-RAN。 
本地配置：使用本地配置的RFSP。 
授权/签约：如果PCF下发了授权RFSP，则使用PCF下发的授权RFSP；如果PCF没有下发授权RFSP，则使用签约RFSP。 
授权/签约与本地配置取小：如果本地RFSP和授权/签约RFSP值均有效，则比较本地RFSP和授权/签约RFSP，使用较小的值；否则，不下发RFSP给NG-RAN。 
授权/本地配置：如果PCF下发了授权RFSP，则使用PCF下发的授权RFSP；如果PCF没有下发授权RFSP，则使用本地配置的RFSP。 
注册
注册流程如下图所示。 
图2  注册流程中的RFSP传递

流程说明如下： 
UE发起注册流程，向NG-RAN发送Registration Request消息。 
NG-RAN向AMF发送Registration Request消息。 
（可选）如果Registration Request中携带的是5G-GUTI，并且AMF检测到5G-GUTI不是本局分配的，则AMF调用Old AMF的服务化接口Namf_Communication_UEContextTransfer请求用户的SUPI和UE上下文。 
（可选）Old AMF响应new AMF调用的服务化接口Namf_Communication_UEContextTransfer，参数包括SUPI、UE上下文等信息，UE上下文中携带签约的RFSP索引subRfsp和使用的RFSP索引usedRfsp。 
new AMF在向UDM获取签约数据之前的处理和普通的注册流程一致。 
new AMF调用UDM的服务化接口Nudm_SDM_Get获取签约数据，保存签约的RFSP索引。 
new AMF在向PCF发起策略关联建立过程之前的处理和普通的注册流程一致。 
（可选）new AMF向PCF发起策略关联建立过程，调用PCF的服务化接口Npcf_AMPolicyControl_Create获取AM策略，保存授权的RFSP索引。 
new AMF在向NG-RAN下发Initial Context Setup Request消息之前的处理和普通的注册流程一致。 
new AMF发送Initial Context Setup Request消息给NG-RAN，其中封装了Registration Accept消息。如果License“AMF支持本地RFSP协商功能”和功能开关“支持RFSP协商”打开，则AMF基于签约的RFSP索引、授权的RFSP索引以及本地策略，协商获得使用的RFSP索引，通过参数Index to RAT/Frequency Selection Priority传递给NG-RAN。 
后续处理和普通的注册流程一致。NG-RAN通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。 
业务请求
业务请求流程如下图所示。 
图3  业务请求流程中的RFSP传递

流程说明如下： 
UE发起业务请求流程，向NG-RAN发送Service Request消息。 
NG-RAN向AMF发送Service Request消息。 
AMF在向NG-RAN下发Initial Context Setup Request消息之前的处理和普通的业务请求流程一致。 
AMF发送Initial Context Setup Request消息给NG-RAN，其中封装了Service Accept消息。如果License“AMF支持本地RFSP协商功能”和功能开关“支持RFSP协商”打开，则AMF基于签约的RFSP索引、授权的RFSP索引以及本地策略，协商获得使用的RFSP索引，通过参数Index to RAT/Frequency Selection Priority传递给NG-RAN。 
后续处理和普通的业务请求流程一致。NG-RAN通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。 
授权的RFSP变更
授权的RFSP变更流程如下图所示。 
图4  授权RFSP变更

流程说明如下： 
用户在连接态，PCF向AMF发送Npcf_AMPolicyControl_UpdateNotify消息通知AM策略变更，AMF保存新的授权RFSP索引。 
如果License“AMF支持本地RFSP协商功能”和功能开关“支持RFSP协商”打开，则AMF基于签约的RFSP索引、新的授权的RFSP索引以及本地策略，协商获得新的使用的RFSP索引，与当前使用的RFSP比较，如果改变，则发送Ue Context Modification Request消息给NG-RAN，将新的使用的RFSP索引通过参数Index to RAT/Frequency Selection Priority传递给NG-RAN。 
后续处理和普通的业务流程一致。NG-RAN通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。 
局间N2切换流程
局间N2切换流程如下图所示。 
图5  局间N2切换流程中的RFSP传递

UE已经注册并且处于连接态。源NG-RAN根据UE的测量报告，判断需要发起切换流程，发送Handover Required消息给AMF。 
AMF判断目标NG-RAN不是本局AMF管理的，按照AMF选择功能选择目标AMF，发送Namf_Communication_CreateUEContext Request消息给目标AMF，在UE上下文中携带签约的RFSP索引subRfsp和使用的RFSP索引usedRfsp。 
目标AMF按照普通的切换流程进行切换，切换成功。 
UE判断需要发起连接态下的移动性注册流程，通过目的NG-RAN向目标AMF发送Registration Request消息。 
目标AMF按照普通的注册更新流程进行注册更新。 
AMF发送Downlink NAS Transport消息给NG-RAN，其中封装了Registration Accept消息。如果“NAS透传消息参数配置”中的“携带RFSP”指示携带RFSP，且License“AMF支持本地RFSP协商功能”和功能开关“支持RFSP协商”打开，则AMF基于签约的RFSP索引、授权的RFSP索引以及本地策略，协商获得使用的RFSP索引，通过参数Index to RAT/Frequency Selection Priority传递给NG-RAN。 
后续处理和普通的注册更新流程一致。NG-RAN通过本地配置将RFSP索引映射到对应的频段优先级列表，并将此列表下发给终端。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System (5GS)）|5.3.4.3 Radio Resource Management functions
3GPP TS 36.300（Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN);Overall description）|Annex I (informative): SPID ranges and mapping of SPID values to cell reselection and inter-RAT/inter frequency handover priorities
3GPP TS 38.300（NR and NG-RAN Overall Description）|Annex D (informative): SPID ranges and mapping of SPID values to cell reselection and inter-RAT/inter frequency handover priorities
3GPP TS 38.413（NG Application Protocol (NGAP)）|9.2 Message Functional Definition and Content 9.3 Information Element Definitions
3GPP TS 29.518（5G System; Access and Mobility Management Services）|6.1.6 Data Model
3GPP TS 29.503（5G System; Unified Data Management Services）|6.1.6 Data Model
3GPP TS 29.507（5G System; Access and Mobility Policy Control Service）|4.2 Service Operations
特性能力 :名称|指标
---|---
基于SUPI的RFSP策略配置最大记录数|2048（条）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“AMF支持本地RFSP协商功能”。 
对其他网元的要求 :UE|gNB|AMF|PCF|UDM
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
缺省RFSP策略配置|SET DEFARFSPPOLICY
SHOW DEFARFSPPOLICY|缺省RFSP策略配置
基于SUPI的RFSP策略配置|ADD SUPISEGRFSPPOLICY
SET SUPISEGRFSPPOLICY|基于SUPI的RFSP策略配置
DEL SUPISEGRFSPPOLICY|基于SUPI的RFSP策略配置
SHOW SUPISEGRFSPPOLICY|基于SUPI的RFSP策略配置
NAS透传消息参数配置|SET DNTPARA
SHOW DNTPARA|NAS透传消息参数配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :AMF支持根据签约的RFSP索引、本地配置的运营商策略、允许的NSSAI以及AMF上可用的UE相关上下文信息（包括UE’s usage setting），来选择正使用的RFSP索引。 
具体来说是通过配置的用户SUPI号段、允许NSSAI及UE’s usage setting信息，来查找最佳匹配的RFSP索引，下发给(R)AN。 
配置前提 :AMF网元运行正常。 
配置过程 :执行[SET DEFARFSPPOLICY]命令，设置缺省RFSP策略。“缺省RFSP策略配置”用于设置AMF全局的缺省RFSP策略。
执行[ADD SUPISEGRFSPPOLICY]命令，新增基于SUPI或SUPI、UE使用设置和允许切片的RFSP策略配置。
配置实例 :场景说明 :本配置可以基于AMF本地策略协商RFSP，通过N2接口提供参数RFSP索引给RAN，从而协助RAN侧进行无线资源管理，为客户提供更为灵活的RFSP获取方式，提升客户的满意度。 
数据规划 :参数|取值
---|---
缺省RFSP策略配置|支持本地RFSP协商|支持RFSP协商
协商策略|缺省RFSP策略配置|签约_授权与本地配置取小
RFSP索引|缺省RFSP策略配置|99
基于SUPI号段的RFSP策略配置|SUPI号段|"4""46""4600118""460011128""460011128""4600111228""4600111220005""460011122000008"
UE使用设置|基于SUPI号段的RFSP策略配置|数据中心、语音中心、任意设定
NSSAI Profile标识|基于SUPI号段的RFSP策略配置|0(无效)、1、2
协商策略|基于SUPI号段的RFSP策略配置|仅本地配置、授权_本地配置、签约_授权
RFSP索引|基于SUPI号段的RFSP策略配置|22、11、88、0、8、33、55
NAS透传消息参数配置|是否携带RFSP|携带RFSP
配置步骤 :步骤1、2、3为三个配置示例共同使用的配置。 
步骤|说明|操作
---|---|---
1|打开缺省RFSP策略配置开关，设置全局默认协商策略，及全局默认的RFSP索引|SET DEFARFSPPOLICY:SUPRFSPNEGO="RFSPNEGOSUPT",POLICY="SMALLER",RFSP=99
2|增加NssaiProfile配置|ADD NSSAI PROFILE:PROFILEID=1,SST="eMBB",SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=2,SST="URLLC",SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=3,SST="MIoT",SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=4,SST="V2X",SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=5,SST=5,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=6,SST=6,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=7,SST=7,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=8,SST=8",SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=9,SST=9,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=10,SST=10,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=11,SST=11,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=12,SST=12,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=13,SST=13,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=14,SST=14,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=15,SST=15,SD="ABCDEF"ADD NSSAI PROFILE:PROFILEID=16,SST=16,SD="ABCDEF"
3|设置NAS透传消息参数为支持DNT消息携带RFSP|SET DNTPARA:TAKERFSP="TAKERFSP"
配置示例1步骤4。 
步骤|说明|操作
---|---|---
4|增加多条基于SUPI号段的RFSP策略配置|ADD SUPISEGRFSPPOLICY:SUPI="4600118",USAGESET="DATA",NSSAIPROFILEID=1,POLICY="NOTCARRYRFSP",RFSP=88ADD SUPISEGRFSPPOLICY:SUPI="460011128",USAGESET="DATA",NSSAIPROFILEID=1,POLICY="LOCAL",RFSP=0ADD SUPISEGRFSPPOLICY:SUPI="460011128",USAGESET="DATA",NSSAIPROFILEID=2,POLICY="LOCAL",RFSP=8ADD SUPISEGRFSPPOLICY:SUPI="4600111228",USAGESET="DATA",NSSAIPROFILEID=3,POLICY="LOCAL",RFSP=33ADD SUPISEGRFSPPOLICY:SUPI="4600111220005",USAGESET="DATA",NSSAIPROFILEID=5,POLICY="SMALLER",RFSP=55ADD SUPISEGRFSPPOLICY:SUPI="460011122000008",USAGESET="DATA",NSSAIPROFILEID=4,POLICY="AUTHSUB",RFSP=33
配置示例2步骤4。 
步骤|说明|操作
---|---|---
4|增加多条基于SUPI号段的RFSP策略配置|ADD SUPISEGRFSPPOLICY:SUPI="4",USAGESET="ARBITARY",NSSAIPROFILEID=0,POLICY="LOCAL",RFSP=22ADD SUPISEGRFSPPOLICY:SUPI="46",USAGESET="ARBITARY",NSSAIPROFILEID=10,POLICY="LOCAL",RFSP=11ADD SUPISEGRFSPPOLICY:SUPI="460",USAGESET="DATA",NSSAIPROFILEID=4,POLICY="LOCAL",RFSP=44ADD SUPISEGRFSPPOLICY:SUPI="4600118",USAGESET="DATA",NSSAIPROFILEID=1,POLICY="NOTCARRYRFSP",RFSP=88ADD SUPISEGRFSPPOLICY:SUPI="460011128",USAGESET="DATA",NSSAIPROFILEID=1,POLICY="LOCAL",RFSP=0ADD SUPISEGRFSPPOLICY:SUPI="460011128",USAGESET="DATA",NSSAIPROFILEID=2,POLICY="LOCAL",RFSP=8ADD SUPISEGRFSPPOLICY:SUPI="4600111228",USAGESET="DATA",NSSAIPROFILEID=3,POLICY="LOCAL",RFSP=33ADD SUPISEGRFSPPOLICY:SUPI="4600111220005",USAGESET="DATA",NSSAIPROFILEID=5,POLICY="SMALLER",RFSP=55ADD SUPISEGRFSPPOLICY:SUPI="460011122000008",USAGESET="DATA",NSSAIPROFILEID=4,POLICY="AUTHSUB",RFSP=33
配置示例3步骤4。 
步骤|说明|操作
---|---|---
4|增加多条基于SUPI号段的RFSP策略配置|ADD SUPISEGRFSPPOLICY:SUPI="46",USAGESET="ARBITARY",NSSAIPROFILEID=10,POLICY="SMALLER",RFSP=20ADD SUPISEGRFSPPOLICY:SUPI="46",USAGESET="ARBITARY",NSSAIPROFILEID=9,POLICY="LOCAL",RFSP=21ADD SUPISEGRFSPPOLICY:SUPI="46",USAGESET="ARBITARY",NSSAIPROFILEID=8,POLICY="SMALLER",RFSP=22ADD SUPISEGRFSPPOLICY:SUPI="46",USAGESET="ARBITARY",NSSAIPROFILEID=7,POLICY="LOCAL",RFSP=23ADD SUPISEGRFSPPOLICY:SUPI="460",USAGESET="DATA",NSSAIPROFILEID=4,POLICY="LOCAL",RFSP=44ADD SUPISEGRFSPPOLICY:SUPI="4600118",USAGESET="DATA",NSSAIPROFILEID=1,POLICY="NOTCARRYRFSP",RFSP=88ADD SUPISEGRFSPPOLICY:SUPI="460011128",USAGESET="DATA",NSSAIPROFILEID=1,POLICY="LOCAL",RFSP=0ADD SUPISEGRFSPPOLICY:SUPI="460011128",USAGESET="DATA",NSSAIPROFILEID=2,POLICY="LOCAL",RFSP=8ADD SUPISEGRFSPPOLICY:SUPI="4600111228",USAGESET="DATA",NSSAIPROFILEID=3,POLICY="LOCAL",RFSP=33ADD SUPISEGRFSPPOLICY:SUPI="4600111220005",USAGESET="DATA",NSSAIPROFILEID=5,POLICY="SMALLER",RFSP=55ADD SUPISEGRFSPPOLICY:SUPI="460011122000008",USAGESET="DATA",NSSAIPROFILEID=4,POLICY="AUTHSUB",RFSP=33
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|所有SUPI号段均不匹配,  InitCtxSetup携带RFSP，为缺省RFSP配置
---|---
测试目的|测试本地(基于网管配置)协商RFSP功能测试本地协商出的RFSP可以通过InitCtxSetup消息带给RAN侧
预置条件|5GC部署成功，各个NF均成功接入EM各个NF配置完成，UDM放号完成本地策略协商RFSP License打开AMF上已完成配置实例中所述示例1中步骤1-4的RFSP相关配置
测试过程|用户（SUPI ：460113000001234）开机，在AMF上发起5G初始注册流程注册请求携带“UE使用设置”字段，取值为“数据中心”注册过程中AMF向NSSF选择切片获取用户的允许NSSAI，NSSF返回响应携带8个SNSSAI：1-ABCDEF、2-ABCDEF、3-ABCDEF、4-ABCDEF、5-ABCDEF、6-ABCDEF、7-ABCDEF、8-ABCDEF。
通过准则|UE注册成功AMF下发InitCtxSetup的Registration Accept消息，N2层携带RFSP索引值为99。
测试结果|–
测试项目|DNT携带RFSP，为按照SUPI号段+UE使用设置+切片维度（空记录）匹配获取的本地策略协商的RFSP索引
---|---
测试目的|测试 基于SUPI号段能够匹配 为前提的本地RFSP策略查找测试SUPI号段+UE使用设置+切片多维度匹配原则测试本地协商出的RFSP可以通过DNT消息带给RAN侧
预置条件|5GC部署成功，各个NF均成功接入EM各个NF配置完成，UDM放号完成本地策略协商RFSP License 打开AMF上已完成配置实例中所述示例2中步骤1-4的RFSP相关配置，包括支持DNT携带RFSP等
测试过程|用户（SUPI ：460113000001234）开机，在AMF上发起5G初始注册流程用户发起移动性注册注册请求不携带UE使用设置字段注册过程向NSSF选择切片获取用户允许NSSAI，NSSF返回响应携带8个SNSSAI：1-ABCDEF、2-ABCDEF、3-ABCDEF、4-ABCDEF、5-ABCDEF、6-ABCDEF、7-ABCDEF、8-ABCDEF
通过准则|UE移动性注册成功AMF 下发.DNT的Registration Accept消息，N2层携带RFSP索引值为RFSP=22
测试结果|–
测试项目|InitCtxSetup携带RFSP，为按照SUPI号段+UE使用设置+切片维度（非空记录)匹配获取的本地策略协商的RFSP索引，用户签约RFSP、PCF授权RFSP也参与协商
---|---
测试目的|测试基于SUPI号段能够匹配为前提的本地RFSP策略查找测试SUPI号段+UE使用设置+切片(非空记录)多维度匹配原则测试协商策略(如：签约_授权与本地取小)的逻辑正确性测试本地协商出的RFSP可以通过 InitCtxSetup消息带给RAN侧
预置条件|5GC部署成功，各个NF均成功接入EM各个NF配置完成，UDM放号完成本地策略协商RFSP License打开AMF上已完成配置实例中所述示例3中步骤1-4的RFSP相关配置，包括支持DNT携带RFSP等用户签约RFSP为10
测试过程|用户（SUPI ：460113000001234）开机，在AMF上发起5G初始注册流程用户发起移动性注册注册请求不携带UE使用设置字段注册过程向NSSF选择切片获取用户允许NSSAI，NSSF返回响应携带8个SNSSAI：1-ABCDEF、2-ABCDEF、3-ABCDEF、4-ABCDEF、5-ABCDEF、6-ABCDEF、7-ABCDEF、8-ABCDEFAMF策略建立响应，PCF带给AMF的用户授权RFSP为12
通过准则|UE初始注册成功AMF 下发InitCtxSetup的Registration Accept消息，N2层携带RFSP索引值为RFSP=10
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## E-UTRA 
Evolved Universal Terrestrial Radio Access演进通用陆地无线接入
## NG-RAN 
Next Generation Radio Access Network下一代无线接入网
## NSSAI 
Network Slice Selection Assistance Information网络切片选择辅助信息
PCF :Policy Control Function策略控制功能
## RFSP 
RAT/Frequency Selection Priority无线/频率选择优先级
## RRM 
Radio Resource Management无线资源管理
SUPI :Subscriber Permanent Identifier用户永久标识
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
# ZUF-79-12 4G5G互操作 
## ZUF-79-12-001 支持N26接口互操作 
特性描述 :特性描述 :术语 :术语|含义
---|---
单注册模式|终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一。
双注册模式|终端具有4G和5G能力，可以同时接入4G系统和5G系统。
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
5G重新接入到4G(重附着) （有N26接口） 
5G重选到4G（TAU） （有N26接口） 
4G到5G注册更新 （有N26接口） 
5G切换到4G （有N26接口） 
4G切换到5G （有N26接口） 
###### 5G重新接入到4G(重附着)   （有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。 
或UE之前在5G接入，因为各种原因关机，当用户再次开机时处于4G网络中，UE重新接入到4G。 
该方式会话重新接入，AMF和MME间通过N26接口交换用户标识等信息。 
###### 5G重选到4G（TAU）         （有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。UE之前在5G接入，移动到4G无线覆盖区域，UE重选到4G。 
该互操作方式会话保持不变，业务中断时间较短， AMF和MME间通过N26接口交换移动性管理上下文和会话上下文等信息。 
###### 4G到5G注册更新                （有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。UE之前在4G接入，移动到5G无线覆盖区域，UE重选到5G。 
AMF和MME间通过N26接口交换移动性管理上下文和会话上下文等信息。 
###### 5G切换到4G                       （有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。UE之前在5G接入，移动到4G无线覆盖区域，gNB把UE从4G切换到5G。 
该互操作方式会话保持不变，业务不中断， AMF和MME间通过N26接口交换移动性管理上下文和会话上下文等信息。 
###### 4G切换到5G                       （有N26接口） 
AMF和MME间部署了N26接口，使用有N26接口的互操作。UE之前在4G接入，移动到5G无线覆盖区域，eNB把UE从4G切换到5G。 
该互操作方式会话保持不变，业务不中断， AMF和MME间通过N26接口交换移动性管理上下文和会话上下文等信息。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户业务体验：在5G信号受限区域，可以在4G下为用户提供服务。热点区域增加5G覆盖，用户业务体验更好。
移动用户|在热点区域部署5G，终端用户业务体验更好。
实现原理 :系统架构 :本特性涉及的互操作架构图如[图2]所示。
为了支持互操作，3GPP定义了4个4G/5G合一的网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U。 
图2  4G和5G互操作架构图

涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
UE|支持4G/5G接入。支持有N26接口或/和无N26接口的互操作。在4G和5G下移动时可保持用户IP不变。
eNodeB|支持通过Handover方式移动到5G下的小区。支持通过重接入等方式，使UE移动到5G下的小区。
NR|支持通过Handover方式移动到4G下的小区。支持通过重接入等方式，使UE移动到4G下的小区。
MME|支持给UE下发“支持无N26互操作”指示。对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等。无N26接口，位置更新时，指示UDM+HSS。支持N26接口。
AMF|支持给UE下发“支持无N26互操作”指示。对4G/5G接入能力的终端，可以选择融合NF，如SMF+PGW-C、UDM+HSS等。无N26接口，位置更新时，指示UDM+HSS。支持N26接口。
PGW-C+SMF|对4G/5G接入能力的终端，可以选择融合NF，如UPF+PGW-U、PCF+PCRF等。根据RAT，支持5G PDU Session和4G PDN Connection的互相转换。根据RAT，支持5G QoS Flow和4G Bearer的互相转换。
PGW-U+UPF|支持用户在4G或5G接入下的用户面数据报文转发。支持用户在4G和5G间的切换。
PCF+PCRF|可同时下发4G和5G QoS等。
UDM+HSS|可同时对用户签约4G和5G2、无N26接口，位置更新时，指示UDM+HSS，UDM+HSS可通知UE同时在MME和AMF上注册。
协议栈 :4G和5G互操作时，与AMF相关接口如下： 
与UE间N1接口 
与gNodeB间N2接口 
与UDM间N8接口 
与PCF间N15接口 
与MME间N26接口（当4G和5G互操作基于N26部署时） 
4G和5G互操作时，与MME相关接口涉及： 
与UE间NAS接口 
与eNodeB间S1-MME接口 
与HSS间S6a接口 
与AMF间N26接口（当4G和5G互操作基于N26部署时） 
本NF/网元实现 :AMF和MME支持有N26接口和无N26接口的4G和5G互操作，支持UE的单注册，也支持UE的双注册。 
业务流程 :基于N26接口的互操作（EPC流程）
EPC流程：由于需要和5G互操作，4G多个流程被波及而需修改，主要修改内容包括： 
对4G/5G用户，MME需选择和锚定融合的PGW-C+SMF、HSS+UDM等。PGW-C+SMF需选择和锚定融合的PGW-U+UPF、PCRF+PCF等。对于具有N1-Mode能力的终端，MME选择融合的PGW-C+SMF。 
MME需给UE指示是否支持N26。 
对4G/5G用户，UE在PDN连接建立时，会分配PDU Session ID并在PCO中通知给网络侧。Interworking with N26时，PGW-C+SMF会为QoS Flow分配S-NSSAI、5G QoS等参数。 
4G/5G用户初始附着EPC
普通用户附着，参考23.401 5.3.2 Attach procedure。 
相对于普通附着，4G/5G用户初始附着有如下不同点： 
UE发送Attach Request时： 
如果之前在5GS中注册，UE在AS信令中提供GUMMEI（mapped from the 5G-GUTI），并指示"Mapped from 5G-GUTI"。 
如果之前在5GS中注册，UE在Attach Request消息中携带GUTI（mapped from the 5G-GUTI），并指示从5GC移动过来。 
如果UE支持5GC NAS，则在UE Core Network Capability IE中指示给MME。 
附着过程中若需要激活PDN连接，则UE分配PDU Session ID，并在PCO中携带给SMF+PGW-C。 
HSS+UDM收到MME的Update Location Request消息后，会向AMF发送Nudm_UECM_DeregistrationNotification，通知AMF注销3GPP接入。 
附着过程中若需要激活PDN连接，MME选择融合的PGW +SMF。 
PGW-C+SMF会分配S-NSSAI、5G QoS等信息，并在PCO中携带给UE。 
若UE支持5GC NAS并且MME支持N26互操作，则MME下发Attach Accept消息时，“支持无N26互操作”为“不支持”。 
附着过程中若需要激活PDN连接，收到Attach Accept(Activate EPS Defaulst Bearer Request)消息时，UE保存PDU Session ID与5G QOS Rules、S_NSSAI之间的关系，以便向5G切换时使用。 
4G/5G用户TAU
普通用户TAU，参考23.401 5.3.3 Tracking Area Update procedures。 
相对于普通TAU，4G/5G用户TAU有如下不同点： 
UE发送TAU Request时： 
如果之前在5GS中注册，UE在AS信令中提供GUMMEI（mapped from the 5G-GUTI），并指示"Mapped from 5G-GUTI"。 
如果之前在5GS中注册，UE在TAU Request消息中携带GUTI（mapped from the 5G-GUTI），并指示从5GC移动过来。 
如果之前在5GS中注册，UE使用5G安全上下文对TAU Request进行完整性保护。 
HSS+UDM收到MME的Update Location Request消息后，会向AMF发送Nudm_UECM_DeregistrationNotification，通知AMF注销3GPP接入。 
若UE支持5GC NAS并且MME支持N26互操作，则MME下发Attach Accept消息时，“支持无N26互操作”为“不支持”。 
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
MME向UE发送ACTIVATE EPS BEARER CONTEXT REQUEST消息，携带PCO（5G QoS Rules）。 
UE获取最新的5G QoS Rules，保存之，以便向5G切换时使用。 
4G/5G用户修改承载
普通用户修改承载，参考23.401 5.4.2 Bearer modification with bearer QoS update和5.4.3 PDN GW initiated bearer modification without bearer QoS update。 
相对于普通修改承载，4G/5G用户修改承载有如下不同点： 
某种条件触发PCF更新会话策略信息。 
PGW-C+SMF收到会话策略后，进行承载绑定，决策出需要更新承载QoS、TFT等；同时，若支持with N26互操，更新5G QoS Rules。 
PGW-C+SMF通知PGW-U+UPF更新N4会话。 
PGW-C+SMF向MME发送Update Bearer Request，若支持with N26互操作，通过PCO携带5G QoS Rules。 
MME向UE发送MODFIY EPS BEARER CONTEXT REQUEST消息，携带PCO（5G QoS Rules）。 
UE获取最新的5G QoS Rules，保存之，以便向5G切换时使用。 
4G/5G用户删除承载
普通用户删除承载，参考23.401 5.4.4.1  PDN GW initiated bearer deactivation。 
相对于普通删除承载，4G/5G用户删除承载有如下不同点： 
某种条件触发PCF更新会话策略信息。 
PGW-C+SMF收到会话策略后，进行承载绑定，决策出需要删除专有承载QoS、TFT等；同时，若支持with N26互操，更新5G QOS Rules。 
PGW-C+SMF通知PGW-U+UPF更新N4会话。 
PGW-C+SMF向MME发送Delete Bearer Request，通过PCO删除此专有承载对应的5G QoS Rules。 
MME向UE发送DEACTIVATE EPS BEARER CONTEXT REQUEST消息，携带PCO（5G QoS Rules）。 
UE删除去激活承载对应的5G QoS Rules。 
基于N26接口的互操作（5GC流程）
由于需要和4G互操作，5G多个流程被波及而需修改，主要修改内容包括： 
对4G/5G用户，AMF需选择和锚定融合的PGW-C+SMF、HSS+UDM等。PGW-C+SMF需选择和锚定融合的PGW-U+UPF、PCRF+PCF等。 
AMF需给UE指示是否支持N26。 
Interworking with N26时，对4G/5G用户，UE在PDU Session建立时， PGW-C+SMF会请求AMF为QoS Flow分配EBI，并把EBI、4G QoS等参数投递给UE和RAN。 
4G/5G用户注册过程
用户注册过程，参考23.502 4.2.2.2 Registration procedures。 
相对于普通注册，4G/5G用户初始注册有如下不同点： 
若UE支持EPC NAS并且AMF支持无N26互操作，则AMF下发Registration Accept消息时， “支持无N26互操作”为“不支持”。 
4G/5G用户建立PDU会话
用户建立PDU会话，参考23.502 4.3.2.2 UE Requested PDU Session Establishment。 
图3  PDU会话建立流程图

UE发起PDU Session建立请求。 
AMF判断出是4G/5G用户，则选择PGW-C+SMF。 
PGW-C+SMF接收到Nsmf_SMCreateRequest消息，判断出是4G/5G用户。 
PGW-C+SMF选择PCF。 
PGW-C+SMF向PCF请求会话策略。若PCF签约4G/5G QoS，则通过Condition Data将两份策略都下发给PGW-C+SMF。 
PGW-C+SMF收到会话策略后，进行QoS Flow绑定；若支持with N26互操作，生成Mapped 4G QoS及TFT。 
PGW-C+SMF选择PGW-U+UPF，通知其建立N4会话，仅仅下发5G的数据处理策略及隧道资源。 
若支持with N26互操作，PGW-C+SMF向AMF发送Namf_EBIAssign消息请求分配EBI，携带PDU Session ID、 ARPList等信息，其中ARPList是已经绑定成功QoS Flow所使用的ARPs。 
AMF分配EBIs后响应PGW-C+SMF。 
PGW-C+SMF构造Nsmf_N1N2Transfer消息，通知AMF更新转发N1N2接口，其中，N1 Contaniner 5G QoS Rules中携带mapped 4G QoS、TFT、EBIs，N2 Contaniner QOS Profile中携带EBI。 
AMF收到Nsmf_N1N2Transfer消息后，构造N2 Session Request消息，携带N2 info（QoS Profile.EBI）及NAS信令PDU SESSION ESTABLISH ACCEPT（QOS Rules&mapped 4G QoS、TFT 、EBI）。 
RAN保存QoS Profile中的EBI信息，以便UE向4G切换时使用；同时，构造AN消息，向UE转发NAS信令。 
UE接收处理NAS信息，保存PDU Session ID、5G QoS Rules、mapped 4G QoS&TFT、EBI的关联关系，以便向4G切换时使用。 
4G/5G用户修改PDU会话
4G/5G用户因为建立/修改/删除QoS flow而出发PDU会话修改。用户修改PDU会话，参考23.502 4.3.3 PDU Session Modification。 
图4  PDU会话修改流程图

某种条件触发PCF更新会话策略信息。 
PGW-C+SMF收到会话策略后，进行QOSFlow绑定；若支持with N26互操作，生成Mapped 4G QOS及TFT。 
PGW-C+SMF通知PGW-U+UPF更新N4会话，仅波及5G的数据处理策略及隧道资源。 
如果是创建新的QoS flow，则PGW-C+SMF向AMF发送Namf_EBIAssign消息请求分配EBI；如果是删除QoS flow，则PGW-C+SMF向AMF发送Namf_EBIAssign消息请求删除EBI。 
AMF分配/删除EBIs后响应PGW-C+SM。 
PGW-C+SMF构造Nsmf_N1N2Transfer消息，通知AMF更新N1N2接口，其中，N1 Contaniner  add 5G QOS Rules中携带mapped 4G QOS、TFT、EBIs，N2 Contaniner QOS Profile中携带EBI。 
AMF收到Nsmf_N1N2Transfer消息后，构造N2 Session Request消息，携带N2 info（QOS Profile、EBI）及NAS信令PDU SESSION MODIFICATION COMMAND（add QOS Rules（mapped 4G QOS、TFT 、EBI））。 
RAN保存QOS Profile中的EBI信息，以便UE向4G切换时使用；同时，构造AN消息，向UE转发NAS信令。 
UE接收处理NAS信息，保存PDU Session ID、5G QOS Rules、mapped 4G QOS&TFT、EBI的关联关系，以便向4G切换时使用。 
5G到4G的切换（N26）
本特性涉及的业务流程图如[图5]所示，流程协议详细描述可参见3GPP 23.502 4.11.1.2.1 5GS to EPS handover using N26 interface。
图5  N26接口5GS到EPS的切换

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
17. UE发起TAU流程。在该流程中，AMF可以通知UDM退订签约数据改变事件，释放AMF和NR的相关资源。若MME判断需要更换安全算法，比如目的MME配置的安全算法与AMF侧配置的EPS安全算法不一致，导致用户在4G侧协商的安全算法与5G侧协商的EPS安全算法不一致，则触发Security Mode Command过程。为了减少信令，AMF上EPS安全算法配置，建议与MME上安全算法配置保持一致。 
18. 对于non-GBR的QoS Flow，PGW-C+SMF可以发起专有承载建立流程。 
19. 如果资源保护监测定时器超时，且建立了非直接数据前转隧道，则MME通知SGW释放非直接数据前转隧道资源。 
20. 如果资源保护监测定时器超时，且建立了非直接数据前转隧道，则AMF通知PGW-C+SMF释放非直接数据前转隧道资源。 
4G到5G的切换（N26）
本特性涉及的业务流程图如下图所示，流程协议详细描述可参见3GPP 23.502 4.11.1.2.2 EPS to 5GS handover using N26 interface。 
切换流程分为切换准备阶段和切换执行阶段。 
图6  准备阶段

切换准备阶段，流程说明如下： 
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
切换执行阶段： 
图7  执行阶段

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
图8  5GS to EPS Idle mode mobility using N26 interface

流程说明如下： 
1. UE检测需发起RAT改变的TAU流程。 
2. UE发送TAU请求消息给eNB。 
3. eNB发送TAU请求消息给MME。 
4. MME选择合适的AMF，给AMF发送Context Request消息。 
5. AMF确定TAU请求消息后，向PGW-C+SMF发送 Nsmf_PDUSession_Context Request消息。如果CN Tunnel Info由PGW-U+UPF分配,则PGW-C+SMF发送N4 Session Modification Request消息给PGW-U+UPF，为EPS bearer建立隧道。PGW-C+SMF返回Nsmf_PDUSession_Context Response消息，携带mapped EPS bearer contexts等信息。 
6. AMF向MME返回Context Response消息，携带mapped MM context 、SM EPS UE Context (default and dedicated GBR bearers) 等信息。 
7. MME完成对UE的安全过程。若MME判断需要更换安全算法，比如目的MME配置的安全算法与AMF侧配置的EPS安全算法不一致，导致用户在4G侧协商的安全算法与5G侧协商的EPS安全算法不一致，则触发Security Mode Command过程。为了减少信令，AMF上EPS安全算法配置，建议与MME上安全算法配置保持一致。 
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
图9  EPS to 5GS Mobility Registration Procedure (Idle and Connected State) using N26 interface

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
5G到4G的重新接入（N26）
同“基于N26接口的互操作（EPC流程）”。 
4G到5G的重新接入（N26）
同“基于N26接口的互操作（5GC流程）”。 
系统影响 :4G与5G互操作，会增加垮RAT的流程，影响系统的话务模型。 
部署了N26接口时，从5G到4G的Handover流程和TAU流程。 

部署了N26接口时，从4G到5G的Handover流程和Registration Update流程。 
没有部署N26接口时，从5G到4G的TAU流程，附着流程，PDN连接建立流程，专有承载建立流程。 
没有部署N26接口时，从4G到5G的Registration流程，PDU Session建立流程，专有QoS flow建立流程。 
为了减少对系统的影响，需尽可能减少垮RAT互操作次数，重叠区要合理规划，避免频繁的跨RAT互操作。 
应用限制 :协议版本：N26接口版本为2019年9月份。 
如果需支持N26接口的互操作，则MME需支持承载级的PCO/ePCO（通过PCO/ePCO携带5G QoS flow对应的S-NSSAI、5G QoS等）。 
4G MME的GUMMEI和5G AMF的GUAMI规划时尽量不重叠。如果重叠了，一方面RAN选择MME时，真实的GUMMEI和映射的GUMMEI都匹配，导致选择合一的CN节点可能失败，也会导致各个CN节点的负荷可能不均；另一方面，如果MME使用MME-FQDN选择AMF时，会导致可能选择错误的AMF，必须要求MME使用AMF-FQDN选择AMF才可以避免。 
特性交互 :无。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501-f20 System Architecture for the 5G System|全文
3GPP TS 23.502-f20 Procedures for the 5G System|全文
3GPP TS 23.503-f20 Policy and Charging Control Framework for the 5G System|全文
3GPP TS 29.274-f90 Tunnelling Protocol for Control plane (GTPv2-C); Stage 3|全文
特性能力 :该特性不涉及规格指标。 
  
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :该特性需要开启License，对应的License项目为： 
LICENSE项|归属NF|备注
---|---|---
AMF支持N26互操作|AMF|AMF部署了N26接口，支持4G和5G间有N26接口互操作
AMF支持无N26互操作|AMF|AMF没有部署N26接口，支持4G和5G间无N26接口互操作
MME支持N26互操作|SGSN&MME|MME部署了N26接口，支持4G和5G间有N26接口互操作
MME支持无N26互操作|SGSN&MME|MME没有部署N26接口，支持4G和5G间无N26接口互操作
对其他网元的要求 :要求参与互操作的各网元功能，均依据3GPP协议规定。 
工程规划要求 :规划基于N26接口互操作还是无N26接口互操作。 
如果基于N26接口互操作，需分别规划AMF和MME的N26接口的GTPC地址和VRF。 
NR需配置4G邻接小区信息等，eNB需配置5G邻接小区信息等。 
如果基于N26接口互操作，DNS Server中需增加AMF的解析数据。需要确认解析AMF的方式，如果为根据MME-FQDN解析，则4G GUMMEI和5G GUAMI不能重叠。 
如果需要RAN选择合一的AMF+MME节点，则4G GUMMEI和5G GUAMI不能重叠。 
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
执行[SET 5GINTERWORKCFG]命令，配置支持N26互操作。
执行[SET AMFGTPCADDRCFG]命令，配置AMF的GTPC地址和VRF。
执行[SET MMESELECTPOLICYCFG]命令，配置MME地址选择策略。
执行[ADD ADDRPOOL]命令，配置ADD MMEHOST命令里面的地址池ID对应的MME地址。
执行[ADD MMEHOST]命令，配置MME的FQDN、主机名、地址池、权重和优先级之间的对应关系。其中地址池标识参数与[ADD ADDRPOOL]命令中的地址池标识参数互相关联。
配置实例 :###### 实例1 
场景说明
AMF和MME之间存在N26接口： 
连接态下5G->4G的切换用户在5G注册，并建立若干个PDU，其中包含IMS语音PDU。 移动到4G覆盖下，RAN发起5到4的切换，切换过程中进行数据业务。 在向4G切换时，AMF需要通过切换的目标TAI查询MME的地址，便于向MME发送FowardLocaitonRequest消息。 
空闲态下用户从4G->5G的重选用户在4G注册、建立PDN，当用户向5G重选时，UE将用户4G-GUTI映射为5G-GUTI，向AMF发起Registration Request(Mobility类型)。 AMF将5G-GUTI映射为4G GUTI，通过其中的GUMMEI信息选择 old MME，便于向MME获取用户的移动性和会话上下文。 
数据规划
配置项|参数|取值
---|---|---
修改AMF GTPC地址配置|AMF GTPC地址|39.16.16.16|39.16.16.16|39.16.16.16
AMF N26 VRF|修改AMF GTPC地址配置|0|0|0
新增MME地址解析配置|FQDN|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org （连接态下5G->4G的切换）或 mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org （空闲态4G->5G重选）|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org （连接态下5G->4G的切换）或 mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org （空闲态4G->5G重选）|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org （连接态下5G->4G的切换）或 mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org （空闲态4G->5G重选）
主机名|新增MME地址解析配置|mme50.zte.com.cn|mme50.zte.com.cn|mme50.zte.com.cn
优先级|新增MME地址解析配置|1|1|1
权重|新增MME地址解析配置|50|50|50
地址池ID|新增MME地址解析配置|1|1|1
新增地址池配置|地址类型|IPV4|IPV4|IPV4
IP地址|新增地址池配置|192.168.22.22|192.168.22.22|192.168.22.22
地址池标识|新增地址池配置|1|1|1
新增MME地址解析优选子网配置|FQDN|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org（连接态下5G->4G的切换） 或者mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org（空闲态4G->5G重选）|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org（连接态下5G->4G的切换） 或者mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org（空闲态4G->5G重选）|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org（连接态下5G->4G的切换） 或者mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org（空闲态4G->5G重选）
IP类型|新增MME地址解析优选子网配置|IPV4|IPV4|IPV4
子网地址|新增MME地址解析优选子网配置|192.168.22.0|192.168.22.0|192.168.22.0
掩码长度|新增MME地址解析优选子网配置|24|24|24
优先级|新增MME地址解析优选子网配置|1|1|1
设置MME选择策略配置|优选IP类型|IPv4|IPv4|IPv4
支持通过权重和优先级选择切换目标MME|设置MME选择策略配置|支持|支持|支持
修改AMF互操作配置|支持N26互操作|支持N26互操作|支持N26互操作|支持N26互操作
支持无N26互操作|修改AMF互操作配置|不支持无N26互操作|不支持无N26互操作|不支持无N26互操作
互操作模式|修改AMF互操作配置|有N26|有N26|有N26
配置步骤
修改AMF GTPC地址配置，命令如下： 
[SET AMFGTPCADDRCFG]:AMFGTPCADDRESS="39.16.16.16",AMFN26VRF=0
新增MME地址解析配置，命令如下： 
[ADD MMEHOST]:LOGICNAME="tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org", HOSTNAME="mme50.zte.com.cn", PRIORITY=1, WEIGHT=50, ADDRPOOLID=1
新增地址池配置，命令如下： 
[ADD ADDRPOOL]:IPTYPE="IPV4",IPADDR="192.168.22.22",ADDRPOOLID=1
新增MME地址解析优选子网配置，命令如下： 
[ADD HOSTSUBNETPRI]:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org", SUBNETADDR="192.168.22.0", MASKLEN=24, PRIORITY=1
设置MME地址选择策略配置，命令如下： 
[SET MMESELECTPOLICYCFG]:SERVIPTYPE4DUSTACK="IPv4",AMFSELMMEBYPRIOR="SUPPORT"
修改AMF互操作配置，命令如下： 
[SET 5GINTERWORKCFG]:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="NOSPRT",INTERWORKMODE="WITHN26"
###### 实例2 
场景说明
5G重新接入到4G(重附着)   （有N26接口）用户在5G注册、建立PDN，当用户向4G重选时，UE将用户5G-GUTI映射为4G-GUTI，UE向MME发起Attach Req。 MME将4G GUTI映射为5G GUTI，通过其中的GUAMI信息选择 old AMF，便于向AMF获取用户的移动性和会话上下文。 
5G重选到4G（TAU）        （有N26接口）用户在5G注册、建立PDN，当用户向4G重选时，UE将用户5G-GUTI映射为4G-GUTI，UE向MME发起TAU Req。 MME将4G GUTI映射为5G GUTI，通过其中的GUAMI信息选择 old AMF，便于向AMF获取用户的移动性和会话上下文。 
4G到5G注册更新               （有N26接口）用户在4G注册、建立PDN，当用户向5G重选时，UE将用户4G-GUTI映射为5G-GUTI，向AMF发起Registration Request(Mobility类型)。 AMF将5G-GUTI映射为4G GUTI，通过其中的GUMMEI信息选择 old MME，便于向MME获取用户的移动性和会话上下文。 
5G切换到4G                      （有N26接口）用户在5G注册，并建立若干个PDU，其中包含IMS语音PDU。 移动到4G覆盖下，RAN发起5到4的切换，切换过程中进行数据业务。 在向4G切换时，AMF需要通过切换的目标TAI查询MME的地址，便于向MME发送FowardLocaitonRequest消息。 
4G切换到5G                      （有N26接口）用户在4G注册，并建立若干个PDU，其中包含IMS语音PDU。 移动到5G覆盖下，RAN发起4到5的切换，切换过程中进行数据业务。 在向5G切换时，MME需要通过切换的目标TAI查询AMF的地址，便于向AMF发送FowardLocaitonRequest消息。 
数据规划
配置项|参数|取值
---|---|---
修改AMF GTPC地址配置|AMF GTPC地址|39.16.16.16|39.16.16.16|39.16.16.16
AMF N26 VRF|修改AMF GTPC地址配置|0|0|0
新增MME地址解析配置|FQDN|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org （连接态下5G->4G的切换）或 mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org （空闲态4G->5G重选）|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org （连接态下5G->4G的切换）或 mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org （空闲态4G->5G重选）|tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org （连接态下5G->4G的切换）或 mmec02.mmegi8001.mme.epc.mnc004.mcc460.3gppnetwork.org （空闲态4G->5G重选）
主机名|新增MME地址解析配置|mme50.zte.com.cn|mme50.zte.com.cn|mme50.zte.com.cn
优先级|新增MME地址解析配置|1|1|1
权重|新增MME地址解析配置|50|50|50
地址池ID|新增MME地址解析配置|1|1|1
新增地址池配置|地址类型|IPV4|IPV4|IPV4
IP地址|新增地址池配置|192.168.22.22|192.168.22.22|192.168.22.22
地址池标识|新增地址池配置|1|1|1
设置MME选择策略配置|MME地址解析优先级|HOST_DCACHE_DSERVER|HOST_DCACHE_DSERVER|HOST_DCACHE_DSERVER
优选IP类型|设置MME选择策略配置|IPv4|IPv4|IPv4
支持通过权重和优先级选择切换目标MME|设置MME选择策略配置|支持|支持|支持
修改AMF互操作配置|支持N26互操作|支持N26互操作|支持N26互操作|支持N26互操作
支持无N26互操作|修改AMF互操作配置|不支持无N26互操作|不支持无N26互操作|不支持无N26互操作
互操作模式|修改AMF互操作配置|有N26|有N26|有N26
配置步骤
修改AMF GTPC地址配置，命令如下： 
[SET AMFGTPCADDRCFG]:AMFGTPCADDRESS="39.16.16.16",AMFN26VRF=0
新增地址池配置，命令如下： 
[ADD ADDRPOOL]:IPTYPE="IPV4",IPADDR="192.168.22.22",ADDRPOOLID=1
新增MME地址解析配置，命令如下： 
[ADD MMEHOST]:LOGICNAME="tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org", HOSTNAME="mme50.zte.com.cn", PRIORITY=1, WEIGHT=50, ADDRPOOLID=1
设置MME地址选择策略配置，命令如下： 
[SET MMESELECTPOLICYCFG]:MMEADDRRESOLPRI="HOST_DCACHE_DSERVER",SERVIPTYPE4DUSTACK="IPv4",AMFSELMMEBYPRIOR="SUPPORT"
修改AMF互操作配置，命令如下： 
[SET 5GINTERWORKCFG]:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="NOSPRT",INTERWORKMODE="WITHN26"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|验证网络支持有N26互操作时5G到4G的切换
---|---
测试目的|用户从5G移动到4G覆盖下，RAN发起5G到4G的切换，业务不中断。
预置条件|AMF和MME支持N26接口，UE已经在5G注册并激活了一个PDU会话，UE处于连接态。
测试过程|用户从5G移动到4G覆盖下，RAN发起5G到4G的切换，HO Required中指示信息表明直传隧道可用。切换的过程中，进行数据业务。
通过准则|检查AMF根据Target ID中TAI选择目标MME正确。检查AMF根据HO Required中指示信息表明直传隧道可用，AMF将不向SMF请求创建非直传隧道。检查AMF将用户的移动性上下文及会话上下文等信息传递给MME。检查MME收到源AMF的前转切换请求消息后，向SGW请求创建会话，消息正确，选择的PGW为与切换前相同。检查N7口，SMF+PGW-C为了切换的会话，向PCF进行策略更新，消息正确。SMF+PGW-C将5G PDU连接切换为4G PDN会话，已分配给UE的IP地址保持不变。检查UPF(PSA IP锚点)切换为PGW-U，所有流量路由到该PGW-U；UPF+PGW-U完成数据转发隧道的切换，释放N3/N9隧道资源，分配S5/S8-U or S1-U隧道资源。检查计费报文发送正确。切换过程中，数据通畅。切换完成，检查所有5GC侧SMF、UPF会话及用户面资源被释放。检查切换完成，UE使用映射的GUTI发起TAU流程，流程结束后：AMF中用户上下文被删除，UDM+HSS中只记录了MME的位置信息，AMF位置信息被清除，AMF与gNB间N2用户连接被释放，AMF与PCF间策略会话被删除。
测试结果|–
测试项目|验证网络支持有N26互操作时4G到5G的切换
---|---
测试目的|网络支持有N26互操作，用户从4G移动到5G覆盖下，RAN发起4G到5G的切换，业务不中断。
预置条件|AMF和MME之间存在N26接口，4/5G终端在4G初始注册并激活了一个PDN连接，RAN支持直传隧道。
测试过程|UE从4G移动到5G覆盖下，RAN发起4G到5G的切换，HO Required中指示信息表明直传隧道可用，用户处于连接态，切换的过程中，进行数据业务，切换过程不需要重选UPF。
通过准则|检查MME可以正确识别并处理UE发送的Handover Required消息的Handover Type、Target ID、Source to Target Container等字段。检查AMF根据TAI选择SMF正确。检查HO Required消息中有直传隧道指示可用。MME不创建非直传隧道。检查MME发送Forward Relocation Request消息给AMF，携带IMSI、4G MM上下文、EPS PDN连接、Source To Target Container，各消息字段正确。检查AMF选择PCF正确，向PCF发送的Npcf_AMPolicyControl_Create Request中携带SUPI、RAT Type、PLMN等字段正确。检查AMF根据MME携带过来的PGW FQDN，通过NRF查询PGW FQDN对应SMF+PGW-C的服务化地址正确。检查AMF针对每个PDN连接，发送Nsmf_PDUSession_UpdateSMContext Request给SMF+PGW-C，携带EPS PDN连接、AMF ID以及切换准备指示等字段正确。检查N7口，SMF+PGW-C为了切换的会话，向PCF进行策略更新消息正确。检查SMF+PGW-C向AMF响应UpdateSMContext Response，携带包括PDU Session ID、S_NSSAI、n2SmContainer(PDU Session ID, S-NSSAI, QFI(s), QoS Profile(s), EPS Bearer Setup List）信息正确。检查AMF和目标NR之间的Handover Request/Acknowledge消息中各字段正确。检查SMF+PGW-C将4G PDN连接切换为5G PDU会话，已分配给UE的IP地址保持不变；并向UDM进行会话信息的注册，消息字段正确。检查UPF+PGW-U完成数据转发隧道的切换，PGW-U隧道资源被释放，分配N3/N9隧道资源正确。直传隧道前传报文转发是RAN间直接转。检查成功切换的承载/QOSFlow，触发计费更新，话单正确。切换的过程中，媒体面数据通畅。检查切换后，EPC侧SGW、PGW 会话及用户面资源被释放，无资源挂死。检查切换完成，UE使用映射的GUTI发起注册更新流程结束后，MME中用户上下文被删除，UDM+HSS中只记录了AMF的位置信息，MME位置信息被清除，MME与eNB间S1用户连接被释放，AMF与PCF间建立了策略会话关联。
测试结果|–
测试项目|验证网络支持有N26互操作时4G到5G的注册更新
---|---
测试目的|网络支持有N26互操作，用户从4G移动到5G覆盖下，RAN发起4G到5G的注册更新。
预置条件|AMF和MME之间存在N26接口，4/5G终端在4G初始注册并激活了一个PDN连接。
测试过程|AMF收到注册更新，消息中携带UE Status判断GUTI为映射GUTI，AMF将5G GUTI还原为4G GUTI，构造MME FQDN通过DNS或本地解析查询目标MME地址。AMF向old MME发起上下文请求流程，获取用户移动性管理上下文及会话上下文。如果注册请求消息中携带Additional 5G GUTI，AMF通过服务化接口向对应的old AMF请求获取5G安全上下文。AMF调用SMF服务化接口请求创建会话，在此过程中，MME基于上下文响应消息中的PGW node name向NRF请求获取对应的SMF地址，在后续的承载更新过程中，保证使用4G接入下相同的PGW-C+SMF网元。SMF+PGW-C为了切换的会话，向PCF进行策略更新。SMF+PGW-C将4GPDN连接切换为5G PDU会话，已分配给UE的IP地址保持不变。并向UDM进行会话信息的注册。若5G部署了本地分流，切换过程重选UPF时，可实施本地分流策略。SMF+PGW-C通知不在使用的SGW-U进行资源释放，通知继续使用的UP进行N4会话更新。UPF+PGW-U完成数据转发隧道本端的切换，释放PGW-U隧道资源，分配N3/N9隧道资源。成功切换的承载/QOSFlow，保持计费的连续，若满足计费更新条件，触发计费更新。没有成功切换的承载/QOSFlow，计费结束，关闭话单。UE进入连接态后，数据业务正常。其他处理同正常的注册更新流程，流程结束后，MME中用户上下文被删除，UDM+HSS中只记录了AMF的位置信息，MME位置信息被清除，MME与eNB间S1用户连接被释放，AMF与PCF间建立了策略会话关联。
通过准则|检查AMF正确处理注册更新消息，将5G GUTI还原为4G GUTI，正确查询出目标MME地址。检查AMF和old MME之间的交互消息正确。检查AMF和old AMF之间的交互消息正确。检查AMF和SMF之间的交互消息正确，其中SMF与4G接入下相同的PGW-C+SMF网元。检查N7口SMF+PGW-C为了切换的会话，向PCF进行策略更新的消息正确。检查SMF+PGW-C将4GPDN连接切换为5G PDU会话，已分配给UE的IP地址保持不变。并向UDM进行会话信息的注册。检查PGW-U隧道资源是释放，分配N3/N9隧道资源正确。检查计费报文发送正确。检查UE数据报文通畅。检查MME中用户上下文被删除，UDM+HSS中只记录了AMF的位置信息，MME位置信息被清除，MME与eNB间S1用户连接被释放，AMF与PCF间建立了策略会话关联。
测试结果|–
常见问题处理 :无。 
## ZUF-79-12-002 支持无N26接口互操作 
特性描述 :特性描述 :术语 :术语|含义
---|---
单注册模式|终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一。
双注册模式|终端具有4G和5G能力，可以同时接入4G系统和5G系统。
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
5G重新接入到4G（重附着）（无N26） 
5G重选到4G（TAU）           （无N26） 
4G到5G注册更新                   （无N26） 
###### 5G重新接入到4G（重附着）（无N26） 
AMF和MME间没有部署N26接口，UE之前在5G接入，再重新接入到4G。 
该方式会话重新接入，AMF和MME间无法通过N26接口交换用户标识等信息。 
###### 5G重选到4G（TAU）           （无N26） 
AMF和MME间没有部署N26接口，UE之前在5G接入，移动到4G无线覆盖区域后，UE重选到4G。 
该互操作方式AMF和MME间无法通过N26接口交换移动性管理上下文。 
###### 4G到5G注册更新                   （无N26） 
AMF和MME间没有部署N26接口，UE之前在4G接入，再重新接入到5G。 
该方式会话重新接入，AMF和MME可能都有用户的移动性管理上下文。 
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
UDM+HSS|可同时对用户签约4G和5G、无N26接口，位置更新时，指示UDM+HSS，UDM+HSS可通知UE同时在MME和AMF上注册
协议栈 :4G和5G互操作时，与AMF相关接口涉及： 
与UE间N1接口。 
与gNodeB间N2接口 
与UDM间N8接口。 
与PCF间N15接口 
4G和5G互操作时，与MME相关接口涉及： 
与UE间NAS接口。 
与eNodeB间S1-MME接口 
与HSS间S6a接口。 
本NF/网元实现 :AMF和MME支持有N26接口和无N26接口的4G和5G互操作，支持UE的单注册，也支持UE的双注册。 
业务流程 :基于无N26接口的互操作（EPC流程）
由于需要和5G互操作，4G也有流程被波及而需修改，主要修改内容包括： 
对4G/5G用户，MME需选择和锚定融合的PGW-C+SMF、HSS+UDM等。PGW-C+SMF需选择和锚定融合的PGW-U+UPF、PCRF+PCF等。 
MME需给UE指示是否支持N26。 
4G/5G用户初始附着EPC
普通用户附着，参考23.401 5.3.2 Attach procedure。 
相对于普通附着，4G/5G用户初始附着有如下不同点： 
UE发送Attach Request时：如果为单注册模式UE，UE指示从5GC移动过来，如果UE有native EPS GUTI ，则提供native EPS GUTI ，否则提供IMSI。如果为双注册模式UE，UE指示从5GC移动过来，提供native EPS GUTI。如果UE发送了TAU，且被MME因为不能获取UE标识信息拒绝了，则提供IMSI。如果附着消息中携带了PDN连接，且UE想继续保留该PDN连接的会话连续性，则把Request type 设置为"Handover"，并在PCO中携带PDU Session ID。 
若UE支持5GC NAS并且MME支持无N26互操作，则MME下发Attach Accept消息时，携带“支持无N26互操作”指示。 
基于无N26接口的互操作（5GC流程）
由于需要和4G互操作，5G流程也有被波及而需修改，主要修改内容包括： 
对4G/5G用户，AMF需给UE指示是否支持N26。 
Interworking with N26时，对4G/5G用户，UE在PDU Session建立时， PGW-C+SMF会请求AMF为QoS Flow分配EBI，并把EBI、4G QoS等参数投递给UE和RAN。 
4G/5G用户注册过程
用户注册过程，参考23.502 4.2.2.2 Registration procedures。 
相对于普通注册，4G/5G用户初始注册有如下不同点： 
若UE支持EPC NAS并且AMF支持无N26互操作，则AMF下发Registration Accept消息时，携带“支持无N26互操作”指示。 
5G到4G的重选（无N26，单注册）
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
5G到4G的重新接入（无N26，单注册）
同“基于无N26接口的互操作（EPC流程）”。 
4G到5G的重新接入（无N26，单注册）
同“基于无N26接口的互操作（5GC流程）”。 
5G到4G的重选（无N26，双注册）
双注册模式下无N26接口的互操作和单注册无N26接口互操作类似，主要差异点： 
1、双注册模式下的终端，可以提前在另一个RAT下注册，缩短重选接入时延，在另一个RAT下注册成功后不用立即发起会话创建流程；单注册模式下的终端，在跨RAT移动时才会发起注册流程，并在注册后或注册中（有PDN附着）立即创建目标RAT下的PDN/PDU会话。 
2、双注册模式下，终端分别维护4G移动性管理和5G移动性管理，跨RAT移动不需要进行4/5G GUTI映射接入，直接使用各自Native GUTI接入；单注册模式下终端只维护一套移动性管理状态，跨RAT移动需要进行4/5G GUTI映射。 
4G到5G的重选（无N26，双注册）
双注册模式下无N26接口的互操作和单注册无N26接口互操作类似，主要差异点： 
1、双注册模式下的终端，可以提前在另一个RAT下注册，缩短重选接入时延，在另一个RAT下注册成功后不用立即发起会话创建流程；单注册模式下的终端，在跨RAT移动时才会发起注册流程，并在注册后或注册中（有PDN附着）立即创建目标RAT下的PDN/PDU会话。 
2、双注册模式下，终端分别维护4G移动性管理和5G移动性管理，跨RAT移动不需要进行4/5G GUTI映射接入，直接使用各自Native GUTI接入；单注册模式下终端只维护一套移动性管理状态，跨RAT移动需要进行4/5G GUTI映射。 
5G到4G的重新接入（无N26，双注册）
同“基于无N26接口的互操作（EPC流程）”。 
4G到5G的重新接入（无N26，双注册）
同“基于无N26接口的互操作（5GC流程）”。 
系统影响 :4G与5G互操作，会增加垮RAT的流程，影响系统的话务模型。 
部署了N26接口时，从5G到4G的Handover流程和TAU流程。 

部署了N26接口时，从4G到5G的Handover流程和Registration Update流程。 
没有部署N26接口时，从5G到4G的TAU流程，附着流程，PDN连接建立流程，专有承载建立流程。 
没有部署N26接口时，从4G到5G的Registration流程，PDU Session建立流程，专有QoS flow建立流程。 
为了减少对系统的影响，需尽可能减少垮RAT互操作次数，重叠区要合理规划，避免频繁的跨RAT互操作。 
应用限制 :协议版本：2018年6月份。 
4G MME的GUMMEI和5G AMF的GUAMI规划时尽量不重叠。如果重叠了，一方面RAN选择MME时，真实的GUMMEI和映射的GUMMEI都匹配，导致选择合一的CN节点可能失败，也会导致各个CN节点的负荷可能不均；另一方面，如果MME使用MME-FQDN选择AMF时，会导致可能选择错误的AMF，必须要求MME使用AMF-FQDN选择AMF才可以避免。 
特性交互 :无。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501-f20 System Architecture for the 5G System|全文
3GPP TS 23.502-f20 Procedures for the 5G System|全文
3GPP TS 23.503-f20 Policy and Charging Control Framework for the 5G System|全文
特性能力 :该特性不涉及规格指标。 
  
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布
License要求 :该特性需要开启License，对应的License项目为： 
LICENSE项|归属NF|备注
---|---|---
AMF支持N26互操作|AMF|AMF部署了N26接口，支持4G和5G间有N26接口互操作
AMF支持无N26互操作|AMF|AMF没有部署N26接口，支持4G和5G间无N26接口互操作
MME支持N26互操作|SGSN&MME|MME部署了N26接口，支持4G和5G间有N26接口互操作
MME支持无N26互操作|SGSN&MME|MME没有部署N26接口，支持4G和5G间无N26接口互操作
对其他网元的要求 :要求参与互操作的各网元功能，均依据3GPP协议规定。 
工程规划要求 :规划基于N26接口互操作还是无N26接口互操作。如果基于N26接口互操作，需分别规划AMF和MME的N26接口的GTPC地址和VRF。如果基于N26接口互操作，DNS Server中需增加AMF的解析数据。需要确认解析AMF的方式，如果为根据MME-FQDN解析，则4G GUMMEI和5G GUAMI不能重叠。如果需要RAN选择合一的AMF+MME节点，则4G GUMMEI和5G GUAMI不能重叠。NR需配置4G邻接小区信息等，eNB需配置5G邻接小区信息等。 
O&M相关 :命令 :配置项|命令
---|---
AMF GTPC地址配置|SET AMFGTPCADDRCFG
SHOW AMFGTPCADDRCFG|AMF GTPC地址配置
AMF互操作配置|SET 5GINTERWORKCFG
SHOW 5GINTERWORKCFG|AMF互操作配置
EBI分配基本配置|SET 5GEBIASSIGNPOLICY
SHOW 5GEBIASSIGNPOLICY|EBI分配基本配置
EBI抢占优先级配置|SET 5GDEFAULTEBIASSIGNPRIORITY
SHOW 5GDEFAULTEBIASSIGNPRIORITY|EBI抢占优先级配置
SET 5GEBIPRIOMATCHORDER|EBI抢占优先级配置
SHOW 5GEBIPRIOMATCHORDER|EBI抢占优先级配置
ADD 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
MOD 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
DEL 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
SHOW 5GEBIASSIGNPRIORITY|EBI抢占优先级配置
EPC加密配置|SET EPC NAS ENCRYPT CONFIG
SHOW EPC NAS ENCRYPT CONFIG|EPC加密配置
EPC完保配置|SET EPC NAS INTEGRATE CONFIG
SHOW EPC NAS INTEGRATE CONFIG|EPC完保配置
特性配置 :特性配置 :配置说明 :该配置过程实现支持无N26接口互操作功能。 
配置前提 :已同时部署5GC和EPC系统。 
配置过程 :在EM客户端配置页面的左侧命令树中，展开AMF节点，选择Namf_Communication节点。
执行命令[SET 5GINTERWORKCFG]，配置AMF支持的互操作模式以及AMF当前采用的互操作模式。
执行命令[SET 5GEBIASSIGNPOLICY]，配置AMF的EBI分配策略。
执行命令[ADD 5GEBIASSIGNPRIORITY]，新增基于SNSSAI和ARP的优先级配置。
执行命令[SET 5GEBIPRIOMATCHORDER]，配置EBI优先级匹配顺序。
执行命令[SET 5GDEFAULTEBIASSIGNPRIORITY]，配置EBI分配默认优先级配置。
执行命令[SET EPC NAS ENCRYPT CONFIG]，配置AMF的EPC NAS加密配置。
执行命令[SET EPC NAS INTEGRATE CONFIG]，配置AMF的EPC NAS完保配置。
配置实例 :场景说明 :某局点支持跨系统移动，AMF支持有N26的4G/5G互操作，SMF eMBB切片支持N26方式的4G/5G互操作。 
数据规划 :参数|取值
---|---
AMF支持的互操作模式和当前互操作模式|支持N26互操作|支持（SPRT）
支持无N26互操作|AMF支持的互操作模式和当前互操作模式|支持（SPRT）
互操作模式|AMF支持的互操作模式和当前互操作模式|无N26（WITHOUTN26）
AMF本局的GTPC地址|AMF GTPC地址|6.6.6.6
AMF N26 VRF|AMF本局的GTPC地址|1
EPC NAS加密配置|4G EA0算法开关|支持（EPCEA0SUPPORT）
4G EA0算法优先级|EPC NAS加密配置|1
4G EA1算法开关|EPC NAS加密配置|不支持（EPCEA1NOSUPPORT）
4G EA1算法优先级|EPC NAS加密配置|1
4G EA2算法开关|EPC NAS加密配置|不支持（EPCEA2NOSUPPORT）
4G EA2算法优先级|EPC NAS加密配置|1
4G EA3算法开关|EPC NAS加密配置|不支持（EPCEA3NOSUPPORT）
4G EA3算法优先级|EPC NAS加密配置|1
EPC NAS完保配置|4G IA1算法开关|支持（EPCIA1SUPPORT）
4G IA1算法优先级|EPC NAS完保配置|1
4G IA2算法开关|EPC NAS完保配置|不支持（EPCIA2NOSUPPORT）
4G IA2算法优先级|EPC NAS完保配置|1
4G IA3算法开关|EPC NAS完保配置|不支持（EPCIA3NOSUPPORT）
4G IA3算法优先级|EPC NAS完保配置|1
配置步骤 :步骤|说明|操作
---|---|---
1|配置AMF支持互操作模式和当前互操作模式|SET 5GINTERWORKCFG:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="SPRT",INTERWORKMODE="WITHOUTN26"
2|配置AMF本局的GTPC地址|SET AMFGTPCADDRCFG:AMFGTPCADDRESS="6.6.6.6",AMFN26VRF=1
3|配置EPC NAS加密配置|SET EPC NAS ENCRYPT CONFIG:EPC_EA0="EPCEA0SUPPORT",EPC_EA0ALGPRIORITY=1,EPC_EA1="EPCEA1NOSUPPORT",EPC_EA1ALGPRIORITY=1,EPC_EA2="EPCEA2NOSUPPORT",EPC_EA2ALGPRIORITY=1,EPC_EA3="EPCEA3NOSUPPORT",EPC_EA3ALGPRIORITY=1
4|配置EPC NAS完保配置|SET EPC NAS INTEGRATE CONFIG:EPC_IA1="EPCIA1SUPPORT",EPC_IA1ALGPRIORITY=1,EPC_IA2="EPCIA2NOSUPPORT",EPC_IA2ALGPRIORITY=1,EPC_IA3="EPCIA3NOSUPPORT",EPC_IA3ALGPRIORITY=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|从5GC到EPC的移动性管理
---|---
测试目的|验证终端在空闲态位置更新，所有PDN连接迁移成功。
预置条件|网络中各网元系统及操作维护台运行正常。网络侧不支持N26接口，AMF和MME配置工作在无N26互操作模式。UE已经激活1个PDU会话。UE处于空闲态。。
测试过程|调节无线信号，触发终端在EPC网络发起TAU流程。
通过准则|UE向MME发起TAU Request流程，GUTI映射成功，携带的old Native GUTI由5G-GUTI映射而来。MME发送Identify Request给UE，请求用户IMSI。UE回复Identify Response，携带IMSI。执行鉴权、SMC、ESM Info等过程。MME向SGW发送Create Session Request请求建立承载；SGW和PGW-C/SMF交互后，返回Create Session Response，完成承载建立响应。MME向HSS/UDM发送Update Location请求，HSS/UDM向AMF发送Nudm_UEContextManagement_DeregistrationNotification消息。MME 回复TAU accept给UE， UE发送TAU complete，完成TAU流程。
测试结果|–
测试项目|从EPC到5GC的移动性管理
---|---
测试目的|验证终端在空闲态位置更新，所有PDN连接迁移成功。
预制条件|网络中各网元系统及操作维护台运行正常。UE处于单注册模式下，网络工作在无N26互操作模式，UE已收到IWK without N26指示。AMF和MME均不支持N26接口，SMF+PGW-C融合，UPF+PGW-U融合，PCF+PCRF融合，HSS+UDM融合。UE已经激活1个PDU会话。UE处于空闲态。
测试过程|调节无线信号，触发终端在5GC网络发起registration流程。
通过准则|UE向AMF发起registration流程， registration type 携带为 "Mobility Registration Update，并且将EPC GUTI映射为5G GUTI，映射成功。AMF发送Identify Request给UE，请求用户SUCI。UE回复Identify Response，携带用户SUCI。执行鉴权、SMC、IMEI Check等过程。AMF 下发Registration accept给UE，携带分配的5G-GUTI。UE回复Registration Complete给AMF。UE发起PDU建立流程，type为 “Existing PDU Sesssion”。AMF进行SMF选择时，直接取该PDU会话对应DNN在UDM中登记的PGW-C+SMF ID，根据该ID向NRF查询SMF服务化地址；若该PDU会话未向UDM注册，则SMF+PGW-C发送Nudm_SDM_Registration给UDM，携带PDU会话ID、DNN以及PGW-C+SMF ID。5G中会话建立成功。
测试结果|–
NEW： 
测试项目|5G重新接入到4G（重附着）（无N26）
---|---
测试目的|验证终端从5G 附着到4G。
预置条件|网络中各网元系统及操作维护台运行正常。网络侧不支持N26接口，AMF和MME配置工作在无N26互操作模式。UE已经激活1个PDU会话。UE处于空闲态。
测试过程|终端从5G覆盖移动到4G覆盖，从5G 附着到4G。
通过准则|检查UE发送Attach Request给MME，携带映射的GUTI和UE从5GC移入指示；附着请求中包含PDN连接激活请求，请求类型为“Handover”，并携带包含该PDU会话ID的PCO。检查MMEIdentify Request给UE，请求用户IMSI。检查UE回复Identify Response，携带IMSI。检查MME发送给UE的Create Session Request中，包含Handover指示、PCO、SMF+PGW-C地址等信息。检查SMF+PGW-C根据PCO中的PDU会话ID，定位到对应的PDU会话上下文，终端的IP地址保持不变。检查N7口消息正确。检查此用户的5G资源全部释放，无挂死。用户数据通畅。
测试结果|–
测试项目|5G重选到4G（TAU） （无N26）
---|---
测试目的|验证终端在空闲态位置更新，所有PDN连接迁移成功。
预置条件|网络中各网元系统及操作维护台运行正常。网络侧不支持N26接口，AMF和MME配置工作在无N26互操作模式。UE已经激活1个PDU会话。UE处于空闲态。
测试过程|调节无线信号，触发终端在EPC网络发起TAU流程。
通过准则|检查UE发起TAU Request给目标MME，携带映射的GUTI以及UE从5GC移入指示。检查MME根据TAU Request中UE从5GC移入指示，则判断目标局为AMF。又根据本局不支持N26接口配置，则下发TAU Reject给UE，携带#9网络无法获取UE标识原因值。UE触发初始UE的IMSI附着并激活PDN连接，检查激活PDN连接的请求类型为“initial request”。TAU成功，用户数据报文通畅。检查5G资源全部释放，无挂死。
测试结果|–
测试项目|4G到5G注册更新 （无N26）
---|---
测试目的|验证终端从4G 注册更新到5G。
预置条件|网络中各网元系统及操作维护台运行正常。网络侧不支持N26接口，AMF和MME配置工作在无N26互操作模式。UE已经激活1个PDU会话。UE处于空闲态。
测试过程|调节无线信号，触发终端在5G网络发起注册更新流程。
通过准则|检查UE发起的Registration Request消息字段正确。检查AMF与UE交互获取SUPI，各消息字段正确。检查AMF与UDM之间消息交互正确，符合方案和协议。检查AMF选择SMF正确。检查N4口消息字段正确。检查N7口消息字段正确。切换完成，数据通畅。检查4G资源完全释放。
测试结果|–
常见问题处理 :无。 
# ZUF-79-13 语音业务 
## ZUF-79-13-001 VoNR 
特性描述 :特性描述 :术语 :术语|含义
---|---
VoNR|语音呼叫通过NR接入5GC网络，在5GC网络中进行IMS语音。
描述 :定义 :VoNR是基于5GC网络的语音解决方案，在5GC覆盖区域内提供基于IP的高清晰语音业务。
作为一种IP数据传输技术，全部业务承载于5G网络上，实现数据与语音业务在同一网络下的统一。5G网络提供高速率的数据业务，同时还提供高质量的音视频通话，通过VoNR技术来实现音视频通话。
AMF具有管理VoNR能力、支持被叫域问询、提供独立的语音策略。
背景知识 :移动语音业务是移动运营商的主要收入来源之一，移动通讯技术演进到5G网络后，如何提供用户体验良好的语音业务成为运营商需要迫切解决的问题。 
5G部署主要有两种形态，NSA（5G NR非独立组网）和SA（5G NR独立组网）。 
在NSA模式下采用传统4G网络的VoLTE语音解决方案。 
在SA模式下有新的语音接入解决方案，同时包括VoNR和回落到4G网络后继续语音呼叫接入。4G语音使用VoLTE，终端接入eNodeB，通过EPC网络接入IMS。5G语音使用VoNR，终端接入NG-RAN，通过5GC网络接入IMS。 
5G VoNR语音网络中需要部署IMS，IMS网络与5G网络之间需要互连互通，因为IMS可能不会升级支持N5接口，所以PCF需支持Rx接口；HSS也可能不会升级，UDM需支持Cx和Sh接口。NG-RAN传递UE的NAS信令，支持语音QoS Flow建立。5GC建立用于VoNR的IMS信令、视频和语音承载。
应用场景 :概述 :当5G网络部署为SA模式（5G NR独立组网）时，推荐使用VoNR。 
VoNR用于5G网络覆盖区域下的用户接入IMS域进行语音或视频通话，其中语音业务承载于5GC网络上。AMF在5G语音业务场景中负责如下功能： 
5G网络下的起呼和终呼，AMF负责UE VoNR能力管理。 
4G网络和5G网络互通，用户会在4G和5G网络间来回驻留，网络要支持被叫域确定被叫所在网络，AMF支持T-ADS问询。 
语音业务在呼叫时延、拥塞控制方面相对普通业务有其特殊性，AMF提供独立的语音策略。 
###### VoNR能力管理 
终端要在5GC网络中进行语音业务，需要具有VoNR业务能力，AMF负责UE VoNR能力管理。具有VoNR业务能力的终端，可在网络中IMS注册成功。 
AMF在注册流程中指示UE IMS语音能力，UE会根据该指示决策是否发起IMS业务。AMF决策IMS语音能力的策略包括： 
UE语音能力 
无线语音能力 
运营商策略 
终端S1模式能力 
如果UE语音能力、无线语音能力以及运营商策略不能都不支持IMS over PS，则AMF通知UE不支持IMS over PS。 
如果这三者都支持IMS over PS，且下发IMS over PS时不考虑终端S1模式能力，则AMF通知UE支持IMS over PS。若下发IMS over PS考虑终端S1模式能力，则AMF再根据终端是否支持S1模式决策通知UE是否支持IMS over PS。 
###### T-ADS问询 
被叫域问询。用户注册到IMS网络，被叫用户会在4G网络和5G网络间来回驻留，主叫呼叫5G用户时IMS需要向UDM/HSS发起被叫域问询，UDM/HSS同时向AMF和MME发起被叫域问询，AMF确定当前被叫用户所在域。AMF上报UDM关于支持IMS的同向性指示，UE当前位置是否支持IMS语音、最近接入时间和接入类型。 
###### 独立的语音策略 
语音业务在呼叫时延、拥塞控制方面，相对普通业务有其特殊性，AMF提供独立的语音策略。 
客户收益 :受益方|受益描述
---|---
运营商|提升无线频谱利用率、降低网络成本。
移动用户|提升用户体验，VoNR的接续时延优于VoLTE语音。
实现原理 :系统架构 :VoNR中，5G网络是一个IP-CAN，通过IP实现UE和IMS实体之间的连通的网络实体和接口集合。5GC、RAN都需支持VoNR。网络中需要部署IMS网络，该业务网络与5G网络需互连互通。如[图1]所示。
图1  5G语音业务架构(VoNR)

涉及的NF/网元 :VoNR功能需要UE、NR、AMF、UDM、SMF、PCF、MME、CS网元、IMS网元的共同配合，各网元的主要作用参见下表。 
NF/网元名称|NF/网元作用
---|---
UE|支持NG-RAN/E-UTRAN/GERAN/UTRAN接入。支持将自身的VoNR能力通过NAS信令传递给AMF。
NR|传递UE的NAS信令，支持语音QoS Flow建立。
AMF|VoNR能力管理，在注册流程中指示UE IMS语音能力。支持将IMS语音同向性指示通知HSS。支持寻呼增强。
UDM|向AMF请求用户最新的位置更新信息，将得到的网络信息发送给IMS。向AMF发起被叫域问询。
SMF|SMF建立用于VoNR的IMS信令承载、视频承载和语音承载。
PCF|IMS向PCF发起承载建立请求，PCF向SMF提供授权的QoS策略。IMS视频语音使用audio:QI=1、video:QI=2的承载，SIP/SDP传输IMS信令使用QI=5的承载。
MME|4G用户和5G用户间进行语音通话时，MME网元负责5G用户语音信令和承载的建立和处理。
CS网元|2G/3G用户和5G用户间进行语音通话时，CS网元负责2G/3G用户语音信令和承载的建立和处理。
IMS网元|IMS网络向UDM/HSS获取被叫网络信息，负责将呼叫路由到被叫网络和被叫用户。触发PCF发起专有承载建立。打通主被叫间的语音信令和承载。
协议栈 :本特性涉及到的协议栈如[图2]、[图3]、[图4]所示。
图2  AMF和其他NF的接口协议栈

图3  AMF和UE的接口协议栈

图4  AMF和RAN(gNodeB)的接口协议栈

本NF/网元实现 :AMF管理VoNR能力、支持被叫域问询、提供独立的语音策略。 
业务流程 :VoNR能力管理
用户要进行VoNR语音/视频呼叫时，需要先进行IMS注册。注册流程如[图5]所示。
图5  注册流程

注册流程是用户注册到5GC网络上的流程，作为用户开机后的第一个过程，是后续所有流程的基础。 
在注册过程中，AMF决策UE是否具有IMS
over PS能力，在注册接受消息中指示UE。注册流程完成之后，UE再发起PDU Session建立，网络为其建立IMS DNN默认承载，用于传输IMS信令。后续语音呼叫过程中，网络为其建立IMS
DNN专有承载，用于传输语音和视频。 
在此流程中AMF有如下处理： 
UE在Registration Request消息中携带VoNR关键信元： UE's usage setting。 
UE's usage setting包括以下两种取值： 
Voice centric：表示UE支持IMS语音业务。支持voice centric的终端必须保证语音业务可用。 
Data centric：Data centric的UE即使无法在5GC网络获得语音业务的情况下，仍可以继续驻留在5GC网络中。 
AMF向UDM发起注册，注册消息中携带Homogeneous support for IMS voice over PS Session indication用于指示5GC网络是否支持IMS语音业务。AMF正常处理注册请求，直到完成和PCF的交互。 
后续AMF向NR发送UE Radio Capablity Check Request消息。 
AMF收到NR响应UE Radio Capablity Check Response消息，保存IMS Voice Support Indicator，此字段指示无线对IMS语音连续性的支持能力。 
AMF继续处理注册请求，直到发送注册接受。 
AMF确定5GS network feature support信元，指示UE是否支持IMS voice over PS Session，该信元由UE语音能力、无线语音能力和运营商策略共同决定： 
UE语音能力：是指UE是否支持IMS over PS，AMF根据UE在Registration Request中携带的UE's usage setting。 
无线语音能力：是指无线侧是否支持IMS over PS，AMF基于TA粒度确定无线侧是否支持语音，使用“5G TA Voice Policy Template Cfg”确定。 
终端S1模式能力：是指终端是否支持S1 NAS，若5GMM能力中S1 mode指示位取值为1则表示支持，否则表示不支持。 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS over PS，使用“5G SUPI Voice Policy Cfg”确定。如果UE语音能力、无线语音能力和运营商策略三者有其一不支持IMS over PS，则AMF通知UE不支持IMS over PS。如果UE语音能力、无线语音能力和运营商策略三者都支持IMS over PS，且“参考终端S1能力下发IMS指示”配置项设置为“是”、终端支持S1 NAS，则AMF通知UE支持IMS over PS。如果UE语音能力、无线语音能力和运营商策略三者都支持IMS over PS，且“参考终端S1能力下发IMS指示”配置项设置为“是”、终端不支持S1 NAS，则AMF通知UE不支持IMS over PS。如果UE语音能力、无线语音能力和运营商策略三者都支持IMS over PS，且“参考终端S1能力下发IMS指示”配置项设置为“否”，则无论终端是否支持S1 NAS，则AMF通知UE支持IMS over PS。AMF给UE分配TA List时，根据“5G TA Voice Policy Template Cfg”确定TA List中所有TA的语音能力是否一致，最终给UE分配的TA List中所有TA要么都支持IMS，要么都不支持IMS。 
AMF向UE返回Registration Accept消息，消息中携带5GS network feature support信元，指示是否支持IMS voice over PS Session。 
T-ADS
主被叫5G用户都注册到5GC网络，被叫用户会在4G网络和5G网络间来回驻留。因此主叫呼叫5G用户时，需求决策当前被叫用户所在域： 
如果用户当前在5G网络，5GC网络支持IMS语音，则被叫域选5GC网络，被叫路由到IMS。 
如果用户当前在4G网络，EPC网络支持IMS语音，则被叫域选LTE网络，被叫路由到IMS。 
如果UE在AMF和MME上都是注册状态，当呼叫请求到来时，IMS需要向UDM/HSS发起T-ADS问询，UDM/HSS判断“IMS
Voice over PS Sessions”为“non-homogeneous”或“unknown”时，HSS/HLR同时向AMF和MME发起T-ADS问询，查询UE当前位置是否支持IMS语音、最近接入时间和接入类型，否则直接向IMS返回UE的T-ADS信息。
图6  T-ADS被叫接入域选择流程

流程说明： 
UE发起注册请求。 
AMF正常处理注册请求，直到向UDM注册。 
AMF向UDM发送Nudm_UECM_Registration Request消息，携带AMF支持T-ADS能力标记和T-ADS查询的URI。 
UDM保存UE信息。 
UDM向AMF返回Nudm_UECM_Registration Response消息。 
AMF完成注册流程。 
后续IMS的AS-SCC收到UE的MT Invite消息。 
IMS给UDM/HSS发送UDR消息，查询T-ADS信息。 
HSS给UDM发送UDR消息。 
UDM收到查询T-ADS信息的消息后，判断UE的“IMS Voice over PS Sessions”的值。如果为“non-homogeneous”或“unknown”，则发起向T-ADS的查询，给AMF发送Namf_Location_ProvideLocationInfo
Request消息；如果为“Supported”或“Not Supported”，则直接向IMS返回UE的T-ADS信息。
AMF判断UE为IDLE态，则发起寻呼，正常进行寻呼和业务请求流程。 
UE为连接态，向NR发起位置信息获取，获取用户当前位置信息。AMF获取用户的如下信息： 
UE当前注册区域是否支持IMS 
UE最后一次活动时间 
当前Access Type和RAT type 
AMF给UDM/HSS返回Namf_Location_ProvideLocationInfo Response消息，携带步骤12获得的信息。 
UDM给HSS返回UDA。 
UDM/HSS向IMS返回UE的T-ADS信息。 
T-ADS查询： 
如果UE只在AMF上注册（即单注册），那么UDM/HSS根据AMF上报的T-ADS信息进行如下决策：是否支持T-ADS Data RetrievalIMS语音同向性指示是否向AMF发起T-ADS查询不支持支持/不支持/未知否支持支持否支持不支持否支持未知是 
如果UE在AMF和MME上都是注册状态（即双注册），并且AMF支持T-ADS Data Retrieval，向HSS上报T-ADS信息，那么HSS进行如下决策：MME上报的IMS语音同向性指示AMF上报的IMS语音同向性指示是否向AMF和MME同时发起T-ADS查询不支持不支持否不支持支持是不支持未知是未知支持是无不支持是无无是 
独立的语音策略
语音业务在呼叫时延、拥塞控制方面，相对普通业务有其特殊性，AMF提供独立的语音策略。 
寻呼增强呼叫时延是语音业务关键指标，寻呼时长对语音呼叫时延有直接的影响，因此要尽量提高语音寻呼的一次成功率。针对语音承载提升寻呼优先级可以提高接通率，保障语音体验，为此5G网络通过TA
List寻呼来降低一次寻呼失败率，达到降低寻呼时延的目的。AMF根据用户号段、位置TA、5QI 、DNN以及PPI确定用户寻呼策略，确定寻呼范围、寻呼时长和寻呼优先级。对语音业务：a. 一次寻呼范围：TA Listb. 二次寻呼范围：TA Listc. 寻呼优先级较高。 
拥塞控制AMF根据DNN区分业务优先级，设置语音业务优先级高于普通业务，当系统发生拥塞时，语音业务优先通过。通过业务优先级的拥塞控制，既保障了语音业务通过量，又确保网络的负荷平衡。 
系统影响 :网络中的VoNR用户数以及用户语音业务的话务模型，决定了AMF开启VoNR功能后，AMF实际增加的负荷。 
VoNR对系统资源的占用与VoNR的话务模型强相关： 
一次MO呼叫相当于1次业务请求加2次PDU Session Modify。 
一次MT呼叫相当于2次PDU Session Modify加1次寻呼加1次业务请求。 


应用限制 :



该特性基于3GPP R15 2018年9月份版本实现，与AMF对接的周边网元支持VoNR功能时需要对齐到该协议版本。 




特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2".|4.4.3和5.16.3节: IMS support
3GPP TS 23.502: "Procedures for the 5G System;Stage2".|4.13.6 Support of IMS Voice
3GPP TS 24.501: "Non-Access-Stratum (NAS) protocol for 5G System (5GS);Stage3".|4.3.4 Change or determination of IMS voice availability
特性能力 :名称|指标
---|---
5G SUPI语音策略配置|最多支持配置255个号段。
5G TA语音策略配置|最多支持配置255个语音参数策略模板。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.30|AMF下发IMS voice over PS给UE时，考虑终端S1模式能力。
01|V7.19.10|首次发布。
License要求 :如果要使用VoNR业务，需要申请“AMF支持VoNR功能”的License。 
对其他网元的要求 :eLTE|NR
---|---
-|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
要求参与VoNR的各网元功能，均依据3GPP协议规定，具体功能各网元功能。 
工程规划要求 :部署IMS网络，并与5G网络需互连互通，5GC、RAN都需支持VoNR。 
IMS可能不会升级支持N5接口，因此PCF需支持Rx接口；HSS可能不会升级，因此UDM需支持Cx和Sh接口。 
O&M相关 :命令 :与该特性相关的配置项参见[表1]。
配置项|命令
---|---
修改AMF支持VoNR配置|SET 5GVONRCFG
修改缺省语音参数策略配置|SET 5GDEFAULTSUPIVOICEPOLICY
新增基于SUPI的语音参数策略配置|ADD 5GSUPIVOICEPOLICY
修改缺省语音参数策略配置|SET 5GDEFAULTTAVOICEPOLICY
新增基于TA的语音参数策略模板配置|ADD 5GTAVOICEPOLICYTEMPLATE
新增基于DNN的语音参数策略配置|ADD 5GDNNVOICEPOLICY
设置注册区域分配策略|SET 5GTALISTASSIGNPOLICY
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :AMF支持VoNR功能时，需要进行相应的配置，该配置过程实现： 
5G网络下的起呼和终呼，AMF负责UE VoNR能力管理。 
4G网络和5G网络互通，用户会在4G和5G网络间来回驻留，网络要支持被叫域名确定被叫所在网络，AMF支持T-ADS问询。 
语音业务在呼叫时延、拥塞控制方面，相对普通业务有其特殊性，AMF提供独立的语音策略。 
配置前提 :AMF运行正常。 
AMF网管能正常连接。 
配置过程 :执行[SET 5GVONRCFG]命令配置是否支持IMS VoPS业务，配置是否检查UE无线能力。
执行[SET 5GDEFAULTSUPIVOICEPOLICY]命令配置基于SUPI的缺省语音参数策略配置。
执行[ADD 5GSUPIVOICEPOLICY]命令配置基于SUPI的语音参数策略配置。
执行[SET 5GDEFAULTTAVOICEPOLICY]命令配置基于TA的缺省语音参数策略配置。
执行[SET TACFG]命令配置TA的语音策略模板。
执行[ADD 5GTAVOICEPOLICYTEMPLATE]命令配置基于TA的语音参数策略模板配置。
执行[ADD 5GDNNVOICEPOLICY]命令配置支持语音策略的DNN列表。
执行[SET 5GINTERWORKCFG]命令配置AMF支持N26互操作。
配置实例 :场景说明 :5G网络通过VoNR方式提供语音功能，5G UE注册到5G网络和建立IMS PDU Session后，UE可以通过5G网络注册到IMS。 
5G网络通过VoNR方式提供语音功能，5G UE主叫发起IMS语音呼叫和挂机。 
5G网络通过VoNR方式提供语音功能，5G UE被叫时通过IMS语音被叫和挂机。 
数据规划 :配置项|参数名称|取值
---|---|---
AMF支持VONR配置|IMSVoPs|支持IMS VoPS业务
UE无线能力检查|AMF支持VONR配置|检查UE无线能力
基于SUPI的缺省语音参数策略配置|IMSVoPs|不支持IMS VoPS业务
基于SUPI的语音参数策略配置|SUPI号段|46001123
接入类型|基于SUPI的语音参数策略配置|3GPP
IMSVoPs|基于SUPI的语音参数策略配置|支持IMS VoPS业务
跟踪区配置|跟踪区标识|1
移动国家码|跟踪区配置|460
移动网络码|跟踪区配置|01
跟踪区码|跟踪区配置|0001
跟踪区名称|跟踪区配置|Vonr1
TA语音策略模板ID|跟踪区配置|1
基于TA的缺省语音参数策略配置|IMSVoPs|不支持IMS VoPS业务
EPS FallBack|基于TA的缺省语音参数策略配置|不支持EPS FallBack业务
用户别名|基于TA的缺省语音参数策略配置|vonr1
参考终端S1能力下发IMS指示|基于TA的缺省语音参数策略配置|不支持
基于TA的语音参数策略模板配置|策略模板标识|1(跟踪区配置中的TA语音策略模板)
IMSVoPs|基于TA的语音参数策略模板配置|支持IMS VoPS业务
EPS FallBack|基于TA的语音参数策略模板配置|不支持EPS FallBack业务
用户别名|基于TA的语音参数策略模板配置|vonr-ta
参考终端S1能力下发IMS指示|基于TA的语音参数策略模板配置|不支持
支持语音策略的DNN配置|DNN|zte.com.cn
AMF互操作配置|支持N26互操作|SPRT
注册区域分配策略配置|注册区域分配参考IMS VoPS能力|需要具有相同IMS VoPS能力
配置步骤 :根据规划，进行如下配置。 
配置AMF支持VoNR配置功能，命令如下。 
[SET 5GVONRCFG]:IMSVOPS="SPRT",UERADIOCAPCHECK="YES"
基于SUPI的缺省语音参数策略配置，配置为默认不支持IMS VoPS业务，命令如下。 
[SET 5GDEFAULTSUPIVOICEPOLICY]:IMSVOPS="NOSPRT"
配置基于SUPI的语音参数策略配置，配置用户所在的SUPI号段支持IMS VoPS业务，命令如下。 
[ADD 5GSUPIVOICEPOLICY]:SUPI="46001",ACCESSTYPE="_3GPP",IMSVOPS="SPRT"
修改跟踪区配置，配置用户所在TA的语音策略模板，命令如下。 
[SET TACFG]:TAID=1,MCC="460",MNC="01",TAC="0001",TANAME="Vonr1",TAVOICEPOLICYTEMPID=1
基于TA的缺省语音参数策略配置，配置为默认不支持IMS VoPS业务，命令如下。 
[SET 5GDEFAULTTAVOICEPOLICY]:IMSVOPS="NOSPRT",FALLBACK="NOSPRT",USERALIAS="vonr1",CONSIDERS1CAPFORIMS="NOSPRT"
基于TA的语音参数策略模板配置，配置用户所在的TA支持IMS VoPS业务，命令如下。 
[ADD 5GTAVOICEPOLICYTEMPLATE]:POLICYTEMPID=1,IMSVOPS="SPRT",FALLBACK="NOSPRT",USERALIAS="vonr-ta",CONSIDERS1CAPFORIMS="NOSPRT"
配置支持语音策略的DNN配置，将用户签约的DNN配置到支持语音策略的DNN列表中，命令如下。 
[ADD 5GDNNVOICEPOLICY]:DNN="zte.com.cn"
配置AMF支持N26互操作，命令如下。 
[SET 5GINTERWORKCFG]:SUPINTERWITHN26="SPRT"
设置注册区域分配策略，命令如下： 
[SET 5GTALISTASSIGNPOLICY]:SAMEIMSVOPS="YES"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|具有IMS语音能力的UE注册到5GC
---|---
测试目的|具有IMS语音能力的UE注册到5GC，AMF根据5GC网络能力、UE的语音能力、5G无线覆盖、IMS语音连续性以及本地策略等，确定UE是否支持IMS over PS，并在注册接受消息中指示给UE。
预置条件|UE具备5G能力，支持IMS语音能力AMF支持支持IMS VoPS业务配置用户所在的TA、SUPI号段以及用户签约的DNN支持支持IMS VoPS业务AMF开启UE无线能力检测AMF支持N26模式AMF设置用户注册区域分配策略，确保TA具有相同的IMS能力
测试过程|UE发起注册流程，注册成功。
通过准则|注册过程中AMF向UDM发送Nudm_UECM_Registration Request消息，携带UE的IMS语音同向性指示为支持安全模式完成后，AMF向RAN发起UE RADIO CAPABILITY CHECK消息，RAN返回UE的IMS语音连续性能力为支持AMF在注册接受消息中指示UE支持IMS VoPS业务，TA List中所有TA都支持IMS语音能力
测试结果|–
常见问题处理 :无。 
## ZUF-79-13-002 EPS回落 
特性描述 :特性描述 :术语 :术语|含义
---|---
EPS Fallback|NR与UE配合将UE从5GC接入重定向到EPS接入进行语音呼叫的过程。
描述 :定义 :为支持语音业务，NR可以与UE配合，将UE从5GC接入重定向到EPS接入来进行语音呼叫，该过程称为EPS回落。
AMF网元在回落过程中完成移动性管理出局流程。 
背景知识 :5G SA组网时语音解决方案只有一个：VoNR，即由NR、5GC及IMS配合完成基于NR承载的VoNR语音，具体可参见ZUF-79-13-001 VoNR
。
但NR支持IMS语音承载需要一定的时间周期进行网络专项调优以满足语音QoS要求，在5G建网初期为快速推出5G服务，在NR承载语音不成熟时需要先利用传统4G网络来提供语音服务，此时可以通过EPS Fallback回落技术将5G接入下的用户回落到4G网络，并利用4G网络现有的语音解决方案进行语音呼叫，比如，VoLTE或CSFB等。
回落的前提条件是用户在5G已经提前注册IMS网络，这是因为用户作为被叫时，需要在语音网络中先注册才能被发现，而5G语音只有VoNR，因此用户必须在被叫前提前注册到IMS网络，而用户何时会被叫的时间是不确定的，一般用户会在5G接入时同时注册到IMS网络。 
如[图1]所示，即使采用EPS回落，5G也要部署IMS网络。
图1  EPS Fallback示意图

应用场景 :概述 :语音回落的前提条件是需要先在5G进行IMS注册，UE通过IMS域触发语音呼叫（始呼、终呼），最后在呼叫建立过程中由NG-RAN触发UE回落到4G网络。在此过程中，AMF通知基站UE支持EPS回落，并协助UE完成IMS注册，AMF/MME和UE、4/5G RAN及其他核心网网元协作，通过移动性流程（切换、重选或重接入）完成UE从5G到4G的回落。
基于此，可以把EPS回落分为通知基站UE支持EPS回落、IMS注册、主叫回落及被叫回落四个场景。 
###### 场景1：AMF通知基站UE支持EPS回落 
当AMF判断UE支持EPS回落时，AMF在初始上下文建立请求、切换请求或者路径切换确认消息中，携带EPS回落指示，告知基站UE支持EPS回落，如[图2]所示。
图2  AMF通知NG-RAN UE支持EPS回落

###### 场景2：AMF辅助UE完成IMS注册 
5G网络具备语音能力（支持VoNR或EPS回落）时，AMF在UE注册过程中通过注册接受消息中指示UE支持IMS语音，UE基于该指示注册到IMS网络中。后续该UE可以在IMS网络中进行语音呼叫（主叫或被叫），如[图3]所示。
图3  AMF辅助UE完成IMS注册示意图

###### 场景3：主叫触发EPS回落 
4/5G共覆盖，UE主动发起语音呼叫，IMS触发NG-RAN建立语音专载，NG-RAN不支持语音专载建立，NG-RAN与AMF及MME配合，通过切换、重选或重接入等移动性流程触发UE从5G网络回落到4G网络，通过现有4G网络语音方案完成语音呼叫，如[图4]所示。
图4  主叫触发EPS回落示意图

###### 场景4：被叫触发EPS回落 
4/5G共覆盖，该UE作为被叫时，IMS向该UE接入的NG-RAN发起语音专载建立流程，NG-RAN不支持语音专载建立，NG-RAN与AMF及MME配合，通过切换、重选或重接入等移动性流程触发UE从5G网络回落到4G网络，通过现有4G网络语音方案完成语音呼叫，如[图5]所示。
图5  被叫触发EPS回落示意图

客户收益 :受益方|受益描述
---|---
运营商|节约投资成本，避免5G初期过高的网络建设成本，集中精力发展数据业务。
移动用户|保障5G用户可以使用语音业务。
实现原理 :系统架构 :EPS回落基于语音QoS流建立时触发4/5G互操作流程实现，整个架构要求如下： 
会话、数据转发、签约、策略控制对应4/5G逻辑功能实体需要合一。由于EPS回落过程中，需要保证IMS注册的终端IP地址不变，SMF与PGW-C、UPF与PGW-U需要合一，同时为保证签约及策略控制一致，UDM与HSS、PCF与PCRF需要合一。 
MME与AMF既可以通过有N26接口也可以通过无N26接口实现移动性。EPS回落流程中的移动性，在有N26接口时可以通过切换或重选实现，在无N26接口时可以通过重选实现。 
整体架构如[图6]所示。
图6  系统架构

涉及的NF/网元 :EPS回落涉及网元及功能参见下表。 
NF/网元名称|NF/网元作用
---|---
NG-RAN(NR)|语音QoS Flow建立时：通知核心网因为EPS回落导致语音QoS Flow建立失败。触发UE切换或重选到EPS网络。
E-UTRAN(LTE)|配合NG-RAN触发的UE切换或重选，在EPS网络中实现LTE接入。UE回落后，配合核心网完成LTE接入下的语音专载建立。
AMF|有N26部署时：NG-RAN触发UE跨RAT切换时，与周边网元配合完成5G->4G切换。NG-RAN触发UE跨RAT重选时，与SMF配合完成用户相关上下文到MME的传递。NG-RAN通知核心网的EPS回落导致语音QoS Flow建立失败消息透传给SMF。无N26部署时：NG-RAN通知核心网的EPS回落导致语音QoS Flow建立失败消息透传给SMF。
MME|有N26部署时：配合PGW完成LTE接入下的语音专载建立。NG-RAN触发UE跨RAT切换时，与周边网元配合完成5G->4G切换。NG-RAN触发UE跨RAT重选时，向old AMF获取用户相关上下文，在EPS网络恢复移动性管理及会话管理上下文。无N26部署时：配合PGW完成LTE接入下的语音专载建立。支持无PDN连接附着。支持带切换指示的PDN连接建立。
SMF&PGW-C|有N26部署时：收到NG-RAN的语音QoS Flow建立失败且携带EPS回落指示时，暂停语音流建立，待跨RAT切换成功后在LTE接入下重建语音专载。支持UE跨RAT切换或重选。无N26部署时：收到NG-RAN的语音QoS Flow建立失败且携带EPS回落指示时，暂停语音流建立，待跨RAT切换成功后在LTE接入下重建语音专载。支持带切换指示的PDN连接建立。
UPF&PGW-U|支持RAT改变重建用户面，且UE IP地址保持不变。
PCF&PCR|支持通过N7接口与SMF及PGW-C互通。
UDM&HSS|有N26部署时：支持用户4G&5G统一签约数据。无N26部署时：支持pgwFQDN签约下发给MME。支持用户4G&5G统一签约数据。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈
---|---
N2|用于(R)AN和AMF之间的接口。参见ZUF-79-19-002 N2。
N11|用于AMF和SMF之间的接口。参见ZUF-79-19-004 N11。
N26|用于MME和AMF之间的接口。参见ZUF-79-19-009 N26。
本NF/网元实现 :本特性主要涉及AMF的Communication服务。根据网络部署要求，AMF和MME间可以基于N26或无N26实现EPS回落。AMF网络功能和MME可以合一部署为融合网元，回落时可以缩短时延提高跨RAT切换/重选成功率。 
图7  AMF网元实现

业务流程 :流程协议详细描述可参见3GPP 23.502 4.13.6.1 EPS fallback for IMS voice。 
AMF通知基站UE支持EPS回落
AMF通知基站UE支持EPS回落的流程如[图8]所示。
图8  AMF通知基站UE支持EPS回落流程

流程描述如下： 
当AMF下发N2接口消息Initial Context Setup Request、Handover Request、Path Switch Acknowledge给NG-RAN时，若153号软件参数“AMF支持下发Redirection for Voice EPS Fallback指示”设置为“是”，则携带Redirection for Voice EPS Fallback字段。其中，若4/5G互操作模式为N26模式，或者4/5G互操作模式为无N26模式且UE支持HO attach，则字段取值为possible；若网络配置4/5G互操作模式为无N26模式但UE不支持HO attach，则字段取值为not possible。
有N26时基于切换的EPS回落
有N26时基于切换的EPS回落的流程如[图9]所示。
图9  有N26时基于切换的EPS回落流程

流程描述如下： 
UE从5G接入，触发MO或MT的IMS语音呼叫。 
IMS域AF（P-CSCF）通过Rx接口AAR消息请求PCF+PCRF建立呼叫媒体流信息，PCR+PCRF向IMS发送AAA响应，确认已收到该请求。 
PCF+PCRF收到AF的媒体流建立请求后，转换为PCC规则并触发SM会话策略更新流程，向SMF+PGW-C发送Npcf_SMPolicyControl_UpdateNotify Request消息请求安装语音流规则，SMF+PGW-C向PCF+PCRF发送Npcf_SMPolicyControl_UpdateNotify Response消息，确认已收到该请求。 
SMF发起PDU会话更新流程，向AMF发送Namf_Communication_N1N2Transfer消息，包含N2 SM Container；AMF向SMF+PGW-C发送响应消息，确认已收到该请求。 
AMF与NR交互完成PDU会话资源建立： 
AMF向NR发送PDU Session Resource Setup Request消息，请求建立语音QoS Flow。 
NR基于UE、无线及网络能力，无法提供IMS语音，并可以回落到4G网络，则NR向AMF发送PDU Session Resource Setup Response消息，携带拒绝原因值：IMS voice EPS fallback or RAT fallback triggered。 
AMF将NR返回的N2 SM信息通过调用Nsmf_PDUSession_UpdateSMContext服务化接口通知给SMF+PGW-C，SMF+PGW-C检查拒绝原因为：IMS voice EPS fallback or RAT fallback triggered，则暂停PCF触发的PDU会话修改流程，并启动定时器，等待回落流程完成后重建语音专载。 
NG-RAN根据UE能力发起5G->4G的切换流程。 
切换完成后UE在LTE接入下发起TAU流程。 
移动性流程完成后，PGW-C+SMF重启发起语音专载建立流程。 
语音专载建立成功后，PGW-C+SMF向PCF+PCRF发送Npcf_SMPolicyControl_UpdateNotify Request消息通知语音流规则安装成功，PCF+PCRF向PGW-C+SMF发送Npcf_SMPolicyControl_UpdateNotify Response消息。 
PCF+PCRF向AF发送RAR消息通知媒体流信息建立成功，AF向PCF+PCRF发送RAA响应消息。 
IMS继续完成语音呼叫建立流程。 
有N26时基于重选的EPS回落
有N26时基于重选的EPS回落的流程如[图10]所示。
图10  有N26时基于重选的EPS回落流程

流程描述如下： 
UE从5G接入，触发MO或MT的IMS语音呼叫。 
IMS域AF（P-CSCF）通过Rx接口AAR消息请求PCF+PCRF建立呼叫媒体流信息，PCR+PCRF向IMS发送AAA响应，确认已收到该请求。 
PCF+PCRF收到AF的媒体流建立请求后，转换为PCC规则并触发SM会话策略更新流程，向SMF+PGW-C发送Npcf_SMPolicyControl_UpdateNotify Request消息请求安装语音流规则，SMF+PGW-C向PCF+PCRF发送Npcf_SMPolicyControl_UpdateNotify Response消息，确认已收到该请求。 
SMF发起PDU会话更新流程，向AMF发送Namf_Communication_N1N2Transfer消息，包含N2 SM Container；AMF向SMF+PGW-C发送响应消息，确认已收到该请求。 
AMF与NR交互完成PDU会话资源建立： 
AMF向NR发送PDU Session Resource Setup Request消息，请求建立语音QoS Flow。 
NR基于UE、无线及网络能力，无法提供IMS语音，并可以回落到4G网络，则NR向AMF发送PDU Session Resource Setup Response消息，携带拒绝原因值：IMS voice EPS fallback or RAT fallback triggered。 
AMF将NR返回的N2 SM信息通过调用Nsmf_PDUSession_UpdateSMContext服务化接口通知给SMF+PGW-C，SMF+PGW-C检查拒绝原因为：IMS voice EPS fallback or RAT fallback triggered，则暂停PCF触发的PDU会话修改流程，并启动定时器，等待回落流程完成后重建语音专载。 
NG-RAN根据UE能力发起5G->4G的重选流程，NG-RAN向UE发起AN释放流程，携带重定向指示。 
NG-RAN向AMF发起UE上下文释放流程，请求释放用户N2连接。 
AMF向SMF+PGW-C发送Nsmf_PDUSession_UpdateSMContext消息，请求释放UP连接。 
SMF+PGW-C向UPF+PGW-U发起N4会话修改流程，通知释放UP连接。 
UE发起TAU流程。 
移动性流程完成后，PGW-C+SMF重启发起语音专载建立流程。 
IMS继续完成语音呼叫建立流程。 
无N26时EPS回落
无N26时EPS回落的流程如[图11]所示。
图11  无N26时EPS回落流程

流程描述如下： 
UE从5G接入，触发MO或MT的IMS语音呼叫。 
IMS域AF（P-CSCF）通过Rx接口AAR消息请求PCF+PCRF建立呼叫媒体流信息，PCR+PCRF向IMS发送AAA响应，确认已收到该请求。 
PCF+PCRF收到AF的媒体流建立请求后，转换为PCC规则并触发SM会话策略更新流程，向SMF+PGW-C发送Npcf_SMPolicyControl_UpdateNotify Request消息请求安装语音流规则，SMF+PGW-C向PCF+PCRF发送Npcf_SMPolicyControl_UpdateNotify Response消息，确认已收到该请求。 
SMF+PGW-C发起PDU会话更新流程，向AMF发送Namf_Communication_N1N2Transfer消息，包含N2 SM Container；AMF向SMF+PGW-C发送响应消息，确认已收到该请求。 
AMF与NR交互完成PDU会话资源建立： 
AMF向NR发送PDU Session Resource Setup Request消息，请求建立语音QoS Flow。 
NR基于UE、无线及网络能力，无法提供IMS语音，并可以回落到4G网络，则NR向AMF发送PDU Session Resource Setup Response消息，携带拒绝原因值：IMS voice EPS fallback or RAT fallback triggered。 
AMF将NR返回的N2 SM信息通过调用Nsmf_PDUSession_UpdateSMContext服务化接口通知给SMF+PGW-C，SMF+PGW-C检查拒绝原因为：IMS voice EPS fallback or RAT fallback triggered，则暂停PCF触发的PDU会话修改流程，并启动定时器，等待回落流程完成后重建语音专载。 
NG-RAN根据UE及网络能力（无N26）发起5G->4G的重选流程，NG-RAN向UE发起AN释放流程，携带重定向指示。 
NG-RAN向AMF发起UE上下文释放流程，请求释放用户N2连接。 
AMF向SMF+PGW-C发送Nsmf_PDUSession_UpdateSMContext消息，请求释放UP连接。 
SMF+PGW-C向UPF+PGW-U发起N4会话修改流程，通知释放UP连接。 
UE在5G接入下收到了无N26互操作指示，且UE支持附着时携带切换类型的PDN连接建立请求，则UE发起附着并携带切换类型的PDN连接建立请求流程。 
移动性流程完成后，PGW-C+SMF重启发起语音专载建立流程。 
IMS继续完成语音呼叫建立流程。 
系统影响 :EPS回落影响系统话务模型。 
语音用户忙时增加一次5G到4G切换、5G->4G局间TAU或带切换指示的附着。 
语音用户在AMF注册时同时触发IMS PDU会话建立。 
应用限制 :该特性不涉及应用限制。 
特性交互 :本特性依赖ZUF-79-12-001 支持N26接口互操作
和ZUF-79-12-002 支持无N26接口互操作
以完成UE的EPS回落。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2 "|5.16.3.10 IMS Voice Service via EPS Fallback or RAT fallback in 5GS5.17 Interworking and Migration
3GPP TS 23.502:"Procedures for the 5G System;Stage2"|4.11 System interworking procedures with EPC4.13.6.1 EPS fallback for IMS voice
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.20|支持AMF Redirection for Voice EPS Fallback指示。
01|V7.19.10|首次发布。
License要求 :EPS Fallback是AMF及MME网元为支持IMS语音提供的增强功能，需要进行功能控制，但由于回落过程中原因值仅经AMF透传不解析，AMF及MME无法区分是普通4/5G互操作还是EPS Fallback，因此，本特性无License控制。 
对其他网元的要求 :LTE|NR|MME|SMF&PGW-C|UPF&PGW-U|PCF&PCRF|UDM&HSS
---|---|---|---|---|---|---
√|√|√|√|√|√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :有N26部署时，AMF和MME需要分配GTP-C地址用于互通： 
当AMF和MME分离部署时，需要分配各自的GTP-C地址。 
当AMF和MME合一部署时，AMF和MME可以根据运营商规划使用合一的地址或使用不同的地址。 
O&M相关 :命令 :配置项|命令
---|---
跟踪区配置|SET TACFG
基于TA的缺省语音参数策略配置|SET 5GDEFAULTTAVOICEPOLICY
基于TA的语音参数策略模板配置|ADD 5GTAVOICEPOLICYTEMPLATE
Communication软件参数配置|SET COMMU SOFTWARE PARAMETER
性能统计 :该特性不涉及计数器的变化 
告警和通知 :该特性不涉及告警和通知
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :AMF不支持5G语音，是否支持回落到4G网络进行语音业务，需要进行相应的配置。该配置过程实现： 
如果用户所在TA匹配到语音参数策略，则取该策略里面的“FallBack”值，查看是否支持回落功能。 
如果用户的TA没有匹配到任何语音参数策略，则查询缺省的语音参数策略配置里的“FallBack”值，查看是否支持回落功能。 
AMF通知基站UE支持EPS回落，需要进行相应的配置。该配置过程实现： 

如果Communication软件参数153号软件参数配置为“1”，则AMF通过携带Redirection for Voice EPS Fallback字段通知基站。 
配置前提 :AMF，MME运行正常。 
AMF网管能正常连接。 
配置过程 :执行[SET 5GDEFAULTTAVOICEPOLICY]命令配置基于TA的缺省语音参数策略配置。
执行[SET TACFG]命令配置TA的语音策略模板。
执行[ADD 5GTAVOICEPOLICYTEMPLATE]命令配置基于TA的语音参数策略模板配置。
执行[SET COMMU SOFTWARE PARAMETER]命令，配置Communication软件参数。
配置实例 :场景说明 :5G网络不提供语音功能，注册到5G网络的用户回落到4G后发起VoLTE语音功能。 
5G网络不提供语音功能，注册到5G网络的用户回落到4G后接收VoLTE语音。 
AMF通知基站UE支持EPS回落。 
数据规划 :配置项|参数名称|取值
---|---|---
跟踪区配置|跟踪区标识|1
移动国家码|跟踪区配置|460
移动网络码|跟踪区配置|01
跟踪区码|跟踪区配置|0001
跟踪区名称|跟踪区配置|Vonr1
TA语音策略模板ID|跟踪区配置|1
基于TA的缺省语音参数策略配置|FallBack|支持FallBack业务
基于TA的语音参数策略模板配置|策略模板标识|1(跟踪区配置中的TA语音策略模板)
用户别名|基于TA的语音参数策略模板配置|Vonr
FallBack|基于TA的语音参数策略模板配置|支持FallBack业务
Communication软件参数配置|软参索引|153
当前参数值|Communication软件参数配置|1
配置步骤 :修改跟踪区配置，配置用户所在TA的语音策略模板，命令如下： 
[SET TACFG]:TAID=1,MCC="460",MNC="01",TAC="0001",TANAME="Vonr1",TAVOICEPOLICYTEMPID=1
基于TA的缺省语音参数策略配置，配置为默认不支持IMS VoPS业务，命令如下： 
[SET 5GDEFAULTTAVOICEPOLICY]:IMSVOPS="NOSPRT",FALLBACK="SPRT",USERALIAS="vonr1"
基于TA的语音参数策略模板配置，配置用户所在的TA支持IMS VoPS业务，命令如下： 
[ADD 5GTAVOICEPOLICYTEMPLATE]:POLICYTEMPID=1,IMSVOPS="NOSPRT",FALLBACK="SPRT",USERALIAS="vonr-ta"
设置Communication软件参数配置，命令如下： 
[SET COMMU SOFTWARE PARAMETER]:ID=153,VALUE=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|已接入5G网络并注册到IMS系统的支持4/5G互操作的用户回落到4G进行语音业务
---|---
测试目的|网络部署了N26接口，IMS语音呼叫时，无线支持通过切换方式触发语音呼叫回落到4G后发起VoLTE语音
预置条件|UE具备5G能力，支持IMS语音能力AMF不支持IMS VoPS业务配置用户所在的TA支持“FallBack”AMF支持N26模式
测试过程|UE注册到AMFUE发起语音业务
通过准则|UE回落4G网络UE在4G网络中成功发起语音业务
测试结果|–
测试项目|AMF通知基站UE支持EPS回落
---|---
测试目的|网络部署了N26接口，AMF通知基站UE支持EPS回落
预置条件|UE具备5G能力AMF支持N26模式Communication软件参数配置153号软件参数"AMF支持下发Redirection for Voice EPS Fallback指示"设置为"是"
测试过程|UE初始注册到AMF
通过准则|UE注册过程中在初始上下文建立请求消息中携带EPS回落指示，AMF告知基站UE支持EPS回落。
测试结果|–
常见问题处理 :无。 
## ZUF-79-13-003 紧急业务回落 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :紧急业务回落是指用户在5G网络发起紧急呼叫业务时回落到4G网络进行紧急呼叫的过程。 
AMF包括如下功能： 
AMF在注册过程中，下发网络支持紧急回落的能力和紧急号码列表。 
用户发起紧急呼叫时，AMF将用户回落到4G进行紧急呼叫。 
背景知识 :支持紧急呼叫是移动通讯网络的基本要求，在5G SA网络架构下支持紧急呼叫有以下三种方案，具体参见[表1]。方案1和方案2另有特性专门描述，本特性描述的是方案3。
编号|名称|描述|适用场景
---|---|---|---
方案1|紧急呼叫基于VoNR|紧急呼叫会话在5GC网络中建立，紧急语音呼叫时通过VoNR承载。具体内容参见ZUF-79-13-005 紧急业务。|5G SA网络发展成熟，VoNR部署完善。
方案2|通过EPS Fallback回落|紧急呼叫会话在5GC网络中建立，紧急语音呼叫发起后gNB拒绝并触发EPS Fallback回落到EPC网络后，在4G网络中恢复紧急呼叫会话，紧急语音呼叫通过VoLTE承载。具体内容参见ZUF-79-13-002 EPS回落。|5G网络发展初期VoNR尚未完善，5GS网络未部署紧急回落功能，但现网存在存量4G EPS网络支持紧急呼叫。
方案3|紧急回落|终端发起语音呼叫触发紧急回落流程，终端回落到4G网络后立即建立紧急会话，紧急语音呼叫通过VoLTE承载。|5G网络发展初期VoNR尚未完善，5GS网络已部署紧急回落功能，但现网存在存量4G EPS网络支持紧急呼叫。
三种方案的实现方式如[图1]所示。
图1  5G SA紧急呼叫方案

应用场景 :紧急回落是紧急呼叫的一种解决方案，UE需要明确感知网络对于紧急回落支持的能力，并基于此能力在紧急回落时触发回落到4G网络进行紧急呼叫。 
客户收益 :受益方|受益描述
---|---
运营商|功能完备：5G SA网络可提供紧急业务。节约投资：5G建网初期，节约5G VoNR投入。
移动用户|在5G网络下可享受紧急业务。
实现原理 :系统架构 :AMF通过N1接口消息向UE指示网络的紧急回落能力，UE在发起紧急呼叫时，通过N1接口通知AMF发起紧急回落，AMF通过N2接口触发NG-RAN发起回落流程，AMF和MME配合完成UE回落到EPS网络，最终UE在EPS网络中完成紧急呼叫。 
网络架构如[图2]所示。
图2  紧急回落网络架构

涉及的网元 :NF名称|网元作用
---|---
AMF|AMF通过N1接口消息向UE指示网络的紧急回落能力。UE通过携带紧急回落指示的业务请求时，AMF配合UE完成紧急回落过程。
gNB|UE紧急回落过程中，配合AMF完成紧急回落过程。
协议栈 :接口|描述
---|---
N1|UE与AMF间逻辑接口。具体参见ZUF-79-19-001 N1。
N2|NG-RAN与AMF间逻辑接口。具体参见ZUF-79-19-002 N2。
N26|AMF与MME间逻辑接口。具体参见ZUF-79-19-002 N2。
本网元实现 :通过N1接口消息向UE指示网络的紧急回落能力。 
UE通过携带紧急回落指示的业务请求时，配合UE完成紧急回落过程。 
业务流程 :流程协议详细描述可参见3GPP 23.502 4.13.4 Emergency Services。 
紧急回落能力通知
紧急回落能力通知的流程如[图3]所示。
图3  紧急回落能力通知流程

流程描述如下： 
UE发起注册流程。 
AMF基于功能开关及TA能力配置，判断AMF在当前RAT及TA下支持紧急回落功能，则在Registration Accept消息中通过是否支持紧急回落指示位指示AMF支持紧急回落功能。  
如果AMF配置了紧急号码列表，则在Registration Accept消息中需要包含紧急号码列表。 
如果AMF配置了扩展紧急号码列表，则在Registration Accept消息中需要包含扩展紧急号码列表。 
如果AMF下发了扩展紧急号码列表给UE，则AMF需要等待Registration Complete消息。 
空闲态UE紧急回落
空闲态UE紧急回落的流程如[图4]所示。
图4  空闲态UE紧急回落流程

流程描述如下： 
UE通过NG-RAN接入5G网络。 
UE准备发起紧急呼叫。 
UE检测到网络支持紧急回落，发起携带紧急回落指示的业务请求流程。 
AMF收到带紧急回落指示的业务请求后，立即向NG-RAN发送Initial Context Setup Request并携带紧急回落指示给NG-RAN。 
NG-RAN触发跨RAT切换或重选触发UE回落到4G网络。 
回落成功后，UE在4G接入下发起IMS紧急会话的建立。 
连接态UE紧急回落
连接态UE紧急回落的流程如[图5]所示。
图5  连接态UE紧急回落流程

流程描述如下： 
UE通过NG-RAN接入5G网络。 
UE准备发起紧急呼叫。 
UE检测到网络支持紧急回落，发起携带紧急回落指示的业务请求流程。 
AMF收到带紧急回落指示的业务请求后，立即向NG-RAN发送UE Context Modification Request并携带紧急回落指示给NG-RAN。 
NG-RAN触发跨RAT切换或重选触发UE回落到4G网络。 
回落成功后，UE在4G接入下发起IMS紧急会话的建立。 
系统影响 :紧急回落由紧急呼叫触发，在实际网络运行中性能占比极小，对系统的影响可以忽略不计。 


应用限制 :



本特性不涉及应用限制。 




特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP 23.502(Procedures for the 5G System; Stage 2)|4.13.4 Emergency Services
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNodeB|AMF
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性通过配置开关控制，默认关闭，易于实施，对工程规划无额外要求。 
O&M相关 :命令 :配置项参见下表。 
配置项|命令
---|---
紧急业务回落配置|SET EMERGSRVFALLBACKPLY
SHOW EMERGSRVFALLBACKPLY|紧急业务回落配置
紧急号码列表配置|ADD 5GEMERNUMLIST
SET 5GEMERNUMLIST|紧急号码列表配置
DEL 5GEMERNUMLIST|紧急号码列表配置
SHOW 5GEMERNUMLIST|紧急号码列表配置
扩展紧急号码列表配置|ADD 5GEXTEMERNUMLIST
SET 5GEXTEMERNUMLIST|扩展紧急号码列表配置
DEL 5GEXTEMERNUMLIST|扩展紧急号码列表配置
SHOW 5GEXTEMERNUMLIST|扩展紧急号码列表配置
配置项|命令|新增参数
---|---|---
TA配置|ADD TACFG|支持紧急业务回落
ADD TACFG|TA配置|紧急回落能力
SET TACFG|TA配置|支持紧急业务回落
SET TACFG|TA配置|紧急回落能力
注册区域分配策略|SET 5GTALISTASSIGNPOLICY|注册区域分配参考紧急业务回落能力
性能统计 :性能计数器名称
---
C510040007 紧急回落触发业务请求尝试次数
C510040008 紧急回落触发业务请求成功次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :在AMF不支持5G语音或者不支持5G紧急呼叫的情况下，为了支持回落到4G网络进行紧急业务，需要进行相应的配置。该配置过程实现： 
如果用户接入的TA归属本AMF管理，则采用本TA所配置的紧急业务回落策略； 
如果用户接入的TA不归属本AMF管理，则采用默认紧急业务回落策略。 
配置前提 :AMF，MME运行正常。 
AMF网管能正常连接。 
配置过程 :执行[SET EMERGSRVFALLBACKPLY]命令，进行默认紧急业务回落策略配置；
执行[ADD TACFG]命令，进行TA的紧急业务回落策略配置；
执行[ADD 5GEMERNUMLIST]命令，配置紧急号码列表；
执行[ADD 5GEXTEMERNUMLIST]命令，配置扩展号码列表。
配置实例 :场景说明 :5G网络不支持语音功能，或者不支持紧急呼叫，注册到5G网络的用户需回落到4G后发起紧急呼叫。 
数据规划 :配置项|参数名称|取值
---|---|---
跟踪区配置|跟踪区标识|1
移动国家码|跟踪区配置|460
移动网络码|跟踪区配置|01
跟踪区码|跟踪区配置|0001
跟踪区名称|跟踪区配置|tai0001
支持紧急业务回落|跟踪区配置|是
紧急回落能力|跟踪区配置|仅NR支持
紧急号码列表ID|跟踪区配置|1
扩展紧急号码列表ID|跟踪区配置|0
紧急业务回落配置|支持紧急业务回落|是
紧急回落能力|紧急业务回落配置|仅NR支持
紧急号码列表ID|紧急业务回落配置|1
扩展紧急号码列表ID|紧急业务回落配置|0
紧急号码列表配置|紧急号码列表ID|1(跟踪区配置和紧急业务回落配置中的紧急号码列表ID)
紧急号码|紧急号码列表配置|110
服务类型|紧急号码列表配置|“PC”
配置步骤 :1. 修改跟踪区配置，配置该跟踪区下紧急业务策略以及紧急号码 
[SET TACFG]:TAID=1,TANAME="460",TAVOICEPOLICYTEMPID=01,SPRTEMERGFALLBACK="YES",EMERGFALLBACKCAPA="ONLYNRSPRT",EMERGENCYNUMLISTID=1；
2. 设置默认紧急业务回落配置 
[SET EMERGSRVFALLBACKPLY]:SPRTEMERGFALLBACK="YES",EMERGFALLBACKCAPA="ONLYNRSPRT",EMERGENCYNUMLISTID=1,EXTEMERGNUMLISTID=0
3. 添加紧急号码配置 
[ADD 5GEMERNUMLIST]:LISTID=1,NUMBER="110",TYPE="PC"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|紧急业务回落
---|---
测试目的|UE紧急业务回落是否正常
预置条件|UE、NG-RAN、AMF各网元正常AMF配置支持紧急业务回落AMF配置紧急号码列表
测试过程|UE发起普通注册流程注册成功后，UE发起紧急业务
通过准则|紧急业务回落成功，紧急业务成功
测试结果|–
常见问题处理 :无。 
## ZUF-79-13-004 VoNR保障信令流程 
概述 :VoNR保障信令流程是指在网络侧语音呼叫相关流程和UE或无线侧触发流程冲突时，或IMS PDU Session建立和UE或无线侧触发流程冲突时，AMF保障语音呼叫或IMS PDU Session建立相关流程的成功。 
在语音呼叫或IMS PDU Session建立相关流程和切换、注册更新、业务请求等流程冲突时，AMF可以缓存或通知SMF缓存语音相关消息，从而尽可能地保障语音呼叫或IMS PDU Session建立相关流程顺利完成。 
AMF对语音业务可设置特定的寻呼策略。 
具体可参见3GPP 23502协议 4.9.1 Handover procedures in 3GPP access章节。 
客户收益 :在语音呼叫或IMS PDU Session建立相关流程和UE或无线侧触发的流程冲突时，AMF尽可能保障语音呼叫或IMS PDU Session建立相关流程顺利完成，提升用户体验。 
说明 :当AMF检测到网络发起的VoNR专用QoS流流程与UE或无线网络发起的流程冲突，或IMS PDU Session建立与UE或无线网络发起的流程冲突时，AMF缓存语音呼叫或IMS PDU Session建立流程，等UE或无线网络发起的流程完成后，AMF再重新处理语音呼叫或IMS PDU Session建立流程，或向SMF返回携带具体原因的故障响应。SMF会缓存语音呼叫或IMS PDU Session建立流程，在UE或无线网络发起的流程完成后，SMF继续执行语音呼叫或IMS PDU Session建立流程。 
AMF对语音业务可设置特定的寻呼策略。 
具体信息，参照协议3GPP 23 502 4.9.1.2 基于Xn接口的NG-RAN间切换和4.9.1.3 基于N2接口的NG-RAN间的切换。 
## ZUF-79-13-005 紧急业务 
特性描述 :特性描述 :术语 :术语|含义
---|---
紧急呼叫|紧急呼叫是指用户拨打报警或求救号码。由于这些号码的紧急性，使世界各国都规定紧急号码可以在当时任何可用的网络中使用。
描述 :定义 :紧急业务是电信网络的基本语音业务。网络通过终端信令中携带紧急标识或用户拨打紧急号码两种途径识别并提供紧急业务。 
AMF用于识别紧急业务、下发紧急呼叫号码列表、控制紧急注册和紧急PDU会话的建立。
背景知识 :紧急业务从2G/3G网络语音呼叫发展而来，2G/3G、4G、5G的语音呼叫存在差异，紧急业务语音上也存在差异，差异分析参见[表1]。
比较项|5G网络|4G网络|2G/3G网络
---|---|---|---
紧急业务控制|紧急呼叫业务控制在IMS网络|紧急呼叫业务控制在IMS网络|紧急呼叫控制在MSC
紧急业务承载|紧急呼叫是基于5G承载|紧急呼叫是基于EPS承载|紧急呼叫是基于电路域承载
参与网元|NR\AMF\SMF\PCF\IMS|eNodeB\MME\SGW\PGW\PCRF\IMS|RNC\MSC\MGW
为保障紧急呼叫业务的成功，需要在紧急业务的语音信令发送前建立5G紧急PDU会话，避免紧急呼叫语音信令的丢失和减少时延；同时为保障紧急呼叫语音数据包不丢失且时延小，需要为紧急PDU会话提供紧急QoS。 
紧急PDU只能够用于紧急呼叫业务，不能够被其他业务使用。 
应用场景 :在移动网络中，从合法性角度可将用户分为四类： 
完全合法有效用户 
合法但是位置区无效的用户 
有卡但不合法的用户 
无卡用户 
这四种用户紧急呼叫的支持情况参见[表2]。AMF根据运营商需求确定为哪些用户提供紧急呼叫业务。
用户类型|网络仅支持完全合法用户紧急业务|网络支持完全合法用户和合法但位置无效用户紧急业务|网络支持所有有卡用户紧急业务|网络支持所有用户的紧急业务
---|---|---|---|---
完全合法有效用户|可以进行紧急业务|可以进行紧急业务|可以进行紧急业务|可以进行紧急业务
合法但位置区无效的用户|不可以进行紧急业务|可以进行紧急业务|可以进行紧急业务|可以进行紧急业务
有卡但不合法的用户|不可以进行紧急业务|不可以进行紧急业务|可以进行紧急业务|可以进行紧急业务
无卡用户|不可以进行紧急业务|不可以进行紧急业务|不可以进行紧急业务|可以进行紧急业务
客户收益 :受益方|受益描述
---|---
运营商|5G网络下支持为用户提供紧急呼叫业务，符合国家法律要求。
移动用户|用户享受更稳定和更可靠的网络服务，确保生命财产安全。
实现原理 :系统架构 :本地用户紧急业务呼叫的系统架构如[图1]所示。
图1  非漫游场景的5G系统架构

用户漫游情况下，紧急业务呼叫的系统架构如[图2]所示。
 说明： 
漫游情况下，紧急业务适用于local breakout系统架构，不适用于home
routed系统架构。 
图2  漫游场景的5G系统架构

涉及的网元 :网元名称|网元作用
---|---
UE|识别紧急呼叫，并能触发紧急呼叫。
NR|为紧急呼叫业务提供高优先级高质量承载QoS。
AMF|识别紧急业务、下发紧急呼叫号码列表、控制紧急注册和紧急PDU会话的建立。
SMF|识别紧急承载，保证紧急承载的高优先级。
PCF|识别紧急呼叫业务，并且提供紧急业务的QoS和规则控制。
IMS|识别IMS紧急呼叫业务。进行紧急注册处理。路由紧急呼叫到紧急呼叫中心。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|UE和AMF/SMF之间的接口。参见ZUF-79-19-001 N1。
N2|用于(R)AN和AMF之间的接口。参见ZUF-79-19-002 N2。
N8|用于UDM和AMF之间的接口。参见ZUF-79-19-003 N8。
N26|用于MME和AMF之间的接口。参见ZUF-79-19-009 N26。
本网元实现 :AMF根据UE信令指示识别紧急业务，依据本地运营商配置下发紧急呼叫号码列表，完成紧急注册和建立紧急PDU会话。 
业务流程 :紧急注册流程
完全合法有效用户可以发起普通注册或紧急注册。受限业务状态用户也可以发起紧急注册，但不能携带任意网络切片参数给网络，由配置确定是否允许受限业务状态的UE的紧急登记。注册流程如[图3]所示。
图3  注册流程

注册流程中对紧急业务（紧急注册）涉及的相关处理如下： 
紧急注册时，如果UE没有一个有效的5G-GUTI，注册请求中应携带SUCI；如果UE没有SUPI和有效的5G-GUTI，注册请求消息中应携带PEI；其他情况下，注册请求中携带5G-GUTI，指示最近一次服务的AMF。
UE紧急注册时，有挂起的上行信令，因此在注册请求中携带Follow-on request。 
如果UE携带5G-GUTI标识自己，New AMF不识别，不需要向old AMF获取UE上下文（跳过[图3]中的步骤4和5），New AMF立即向UE请求SUPI。
如果UE携带PEI标识自己，New AMF不需要向UE获取SUPI（跳过[图3]中的步骤6和7）。由AMF本地配置是否允许无用户标识的紧急注册。
UE指示注册类型为紧急注册，如果AMF本地配置支持未授权SUPI的紧急注册，AMF跳过步骤8和9的鉴权或者AMF接受鉴权失败，继续注册流程。 
UE在紧急注册不能鉴权时，PEI非加密传输。如果UE在紧急注册请求中携带了PEI，AMF不需要获取PEI（跳过[图3]中的步骤11）。
如果PEI被阻塞，由AMF本地配置决定紧急注册流程是否继续。 
紧急注册时，如果UE鉴权失败或没有鉴权，AMF不应该到UDM注册。 
紧急注册时，AMF不检查接入限制、区域限制或签约限制；AMF获取任意的UDM注册失败响应，继续注册流程。 
紧急注册时，AMF不执行AM Policy Association的处理（跳过[图3]中的步骤16）。
对紧急注册的UE，当注册类型为Mobility Registration Update，AMF调用SMF的服务化接口Nsmf_PDUSession_UpdateSMContext通知SMF更新AMF信息或释放不一致的PDU会话（执行[图3]中的步骤17）。
AMF发送Registration Accept消息时，判断已打开“是否支持紧急呼叫”开关，消息中携带“IE：5GS network feature support”，结合网络能力确定应急服务支持指示，指示UE可以建立紧急PDU会话获取紧急服务。AMF支持紧急呼叫，则根据用户当前TA查表获得对应的紧急号码列表，携带Emergency
number list，按照协议紧急号码列表编码后长度需小于等于50BYTE，如超过50BYTE，从后往前删除紧急号码，直到满足小于等于50BYTE要求；查表失败则不携带。AMF不支持紧急呼叫，则不携带Emergency
number list字段。
紧急注册时，AMF不执行UE Policy Association Establishment流程（跳过[图3]中的步骤21b）。
紧急注册时，AMF不检查接入限制、区域限制或签约限制。 
非紧急注册流程
非紧急注册即普通注册，AMF判断“是否支持紧急呼叫开关”打开。发送Registration Accept消息时，消息中携带“IE：5GS network feature support”，结合网络能力确定紧急业务支持指示，指示UE可以建立紧急PDU会话获取紧急服务。
AMF支持紧急呼叫，则根据用户当前TA查表获得对应的紧急号码列表，携带“Emergency number list”字段；AMF不支持紧急呼叫，则不携带“Emergency number list”字段。
注册更新流程
注册更新流程中对紧急业务（紧急注册）涉及的相关处理如下： 
紧急注册的UE，之前鉴权失败放行或没有鉴权，后续注册更新不再做鉴权，直接放行。 
注册更新时，AMF对紧急注册或存在的紧急PDU会话，如果AMF判断本地配置开关“受限用户放行紧急呼叫”为打开状态，则跳过移动性限制处理（包括接入限制、区域限制或签约限制），继续后续注册更新流程。
AMF根据用户当前TA查表获得对应的紧急号码列表，在注册更新接受消息中携带“Emergency number list”字段给UE。
业务请求流程
业务请求流程中对紧急业务（紧急注册）涉及的相关处理如下： 
紧急注册的UE，之前鉴权失败放行或没有鉴权，后续业务请求不再做鉴权，直接放行。 
业务请求流程涉及的其他步骤处理同现有系统。业务请求流程说明参见ZUF-79-04-002
业务请求中的“UE触发业务请求流程”。 
紧急去注册流程
UDM触发去注册UDM触发去注册（“Subscription Withdrawn”和“Reregistration
Required”类型），当用户有紧急PDU时，AMF不能去注册UE，只能释放非紧急PDU，保留紧急PDU。UDM触发去注册流程说明参见ZUF-79-03-002 去注册中的“网络侧发起的去注册流程”。 
UE触发去注册UE触发去注册，紧急注册和非紧急注册都不对紧急PDU进行特殊处理，AMF正常去注册UE。UE触发去注册流程说明参见ZUF-79-03-002 去注册中的“UE发起的去注册流程”。 
网管触发去注册网管触发去注册，不对紧急PDU进行特殊处理，AMF正常去注册UE。 
AMF隐式去注册紧急注册的UE，其周期性注册更新定时器到达时，不应触发周期性注册更新流程，而应进入RM-DEREGISTERED状态。对这类UE，AMF启动移动可达定时器，取值和UE的周期性注册更新定时器相近。移动可达定时器到达后，AMF将UE的RM
state设置为RM-DEREGISTERED状态。如果紧急注册的用户，收到周期性注册请求，则注册拒绝（携带隐式分离原因），触发隐式分离。 
紧急PDU会话建立流程
UE发起的PDU会话建立流程如[图4]所示。
图4  UE发起的PDU会话建立流程

PDU会话建立流程中对紧急业务（紧急注册）涉及的相关处理如下： 
UE有紧急业务，触发UE发起的PDU会话建立流程，PDU会话请求携带的请求类型为“Emergency Request”。
如果从EPC网络切换到5G网络的PDU会话，则PDU会话请求携带的请求类型为“Existing Emergency
PDU Session”。
如果请求类型既不是“Emergency Request”，也不是“Existing
Emergency PDU Session”，则AMF拒绝紧急注册UE的PDU会话建立请求。
紧急PDU会话建立时，如果AMF没有UE和请求的PDU session ID对应的PDU会话路由上下文，AMF选择一个SMF（参见ZUF-79-10-001 SMF选择
）。SMF选择成功，AMF在PDU会话路由上下文中存储紧急PDU会话指示。
当请求类型是“Emergency Request”时，AMF判断“支持紧急呼叫”开关已打开，使用本地配置的S-NSSAI和DNN参数值，忽略UE携带的S-NSSAI和DNN参数值，并存储PDU会话的接入类型。
AMF发送Nsmf_PDUSession_CreateSMContext Request给SMF，携带PDU session
ID、本地配置的S-NSSAI和DNN、Request type。 
如果UE在限制业务状态下已注册（紧急注册）且有SUPI但没有被鉴权时，AMF指示SMF
SUPI没有被鉴权。当UE在限制业务状态下已注册（紧急注册）且没有SUPI时，AMF携带PEI给SMF。对无SUPI或SUPI没有被鉴权的情况，SMF识别并决策下一步的处理。
如果PDU会话请求的请求类型是“Emergency Request”，对一个已鉴权的非漫游的UE，SMF本地配置确定向UDM注册（Nudm_UECM_Registration）紧急PDU会话，UDM存储该会话。对一个未鉴权的UE或漫游的UE，SMF不应向UDM注册紧急PDU会话。
如果PDU会话请求的请求类型是“Existing Emergency PDU Session”，SMF通过PDU
Session ID识别已存在的PDU会话，此时SMF不会创建一个新的SM上下文而是更新已存在的SM上下文，并在响应消息中指示AMF
SM上下文已更新。
PDU会话鉴权处理（[图4]中的步骤6）时，如果请求类型指示“Emergency Request”或“Existing Emergency
PDU Session”，那么SMF不应执行二次鉴权/授权。
PCF基于紧急PDN，设置为紧急业务预留的PPD规则的ARP值。
如果已激活MICO模式，请求类型指示“Emergency
Request”，那UE和AMF应本地去活MICO模式。
紧急业务切换流程
源NG-RAN和源AMF对紧急PDU会话的切换决策，不考虑UE相关的限制。“受限用户放行紧急呼叫”开关（参见[SET EMERGSRVPLY]命令）打开，释放非紧急PDU会话，执行紧急PDU会话切换，不携带切换限制列表给无线。
系统影响 :紧急呼叫话务比较低，对系统的影响可忽略。 
应用限制 :该特性不涉及应用限制。 
特性交互 :相关特性|交互关系
---|---
ZUF-79-09-001 支持用户接入网络切片|受限业务状态用户发起紧急注册及后续所有的流程，不使用切片。AMF在紧急注册、紧急注册后的注册更新、紧急PDU会话建立、签约改变等流程中跳过切片的处理。UE普通注册，激活紧急PDU，后续移动更新注册过程，正常协商切片。
ZUF-79-04-003 智能寻呼|在紧急呼叫下行数据/网络侧承载激活或修改触发的寻呼中，需对用户优先寻呼。对紧急业务，可根据APR设置寻呼优先级，对紧急呼叫优先寻呼。
ZUF-79-16-005 LCS|紧急呼叫时根据运营商要求主动触发紧急定位。
ZUF-79-04-005 MICO|紧急业务时MICO失效。UE在紧急注册时在注册接受消息中不能指示MICO preference。当UE已激活MICO模式，在紧急PDU会话建立完成后UE和AMF本地去活MICO模式。直到AMF在注册流程中接受使用MICO模式，UE和AMF才可激活MICO mode。
ZUF-79-17-003 N2接口过载控制|AMF过负荷控制情况下，放行紧急业务。
ZUF-79-17-004 NAS拥塞控制|AMF NAS拥塞控制时，放行紧急业务。
ZUF-79-12 4G5G互操作|支持紧急业务
ZUF-79-03-007 对等PLMN|如果鉴权失败或不鉴权或无卡，则注册接受/注册更新接受不下发EPLMN。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501 System Architecture for the 5G System|5.16.4 Emergency Services
3GPP TS 23.502 Procedures for the 5G System|4.13.4 Emergency Services
3GPP TS 24.501 Non-Access-Stratum (NAS) protocol for 5G System (5GS)|5.3.12 Handling of local emergency numbers5.5.1 Registration procedure5.6.1 Service request procedure8.2.7.19 Emergency number list9.11.3.23  Emergency number list
特性能力 :名称|指标
---|---
紧急呼叫数据|AMF支持为每个PLMN配置一套用于紧急呼叫数据，AMF最大支持17个PLMN。
紧急呼叫号码列表|AMF最大可配置50个紧急号码列表和50个扩展紧急号码列表，每个列表中最大可包含10个号码，不同的TA关联不同的紧急号码列表。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :UE|NR|SMF|PCF|IMS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :为紧急业务分配一个独立DNN，该DNN不被其他业务使用。 
O&M相关 :命令 :新增配置项如下： 
配置项|命令
---|---
设置紧急业务功能开关|SET EMERGSRVPLY
SHOW EMERGSRVPLY|设置紧急业务功能开关
紧急数据配置|ADD EMERGDATA
SET EMERGDATA|紧急数据配置
DEL EMERGDATA|紧急数据配置
SHOW EMERGDATA|紧急数据配置
增加紧急号码|ADD 5GEMERNUMLIST
SET 5GEMERNUMLIST|增加紧急号码
DEL 5GEMERNUMLIST|增加紧急号码
SHOW 5GEMERNUMLIST|增加紧急号码
增加扩展紧急号码|ADD 5GEXTEMERNUMLIST
SET 5GEXTEMERNUMLIST|增加扩展紧急号码
DEL 5GEXTEMERNUMLIST|增加扩展紧急号码
SHOW 5GEXTEMERNUMLIST|增加扩展紧急号码
设置紧急业务回落配置|SET EMERGSRVFALLBACKPLY
SHOW EMERGSRVFALLBACKPLY|设置紧急业务回落配置
设置紧急业务SNSSAI配置|SET EMERGSRVSNSSAI
SHOW EMERGSRVSNSSAI|设置紧急业务SNSSAI配置
设置该TA支持紧急业务能力|ADD TACFG
SET TACFG|设置该TA支持紧急业务能力
DEL TACFG|设置该TA支持紧急业务能力
SHOW TACFG|设置该TA支持紧急业务能力
性能统计 :测量类型|描述
---|---
初始注册流程测量|编号为51143开头的所有计数器
告警和通知 :该特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :当需要支持紧急业务相关的功能时，需要进行如下配置： 
紧急业务策略配置：配置在多种应用场景下支持紧急业务。 
紧急数据配置：新增紧急数据配置相关参数，这些参数影响紧急业务流程的处理。 
紧急号码配置：将配置的紧急号码通过注册接受消息带给终端。 
紧急业务回落配置：配置是否支持对紧急业务的回落处理。 
紧急切片数据配置：紧急业务不再使用用户请求的切片，而是直接使用本地配置的紧急切片，也不再进行切片选择。 
TA配置增加参数：配置对该TA在无线侧对紧急业务的支持。 
接入区域列表分配策略：该配置决定用户接入过程中分配的注册区域。如果要求分配区域都具有相同的业务能力，那么这些区域所对应的TA的紧急业务支持能力必须相同。 
配置前提 :AMF运行正常。 
EM网管能正常连接AMF网元。 
配置过程 :执行[SET EMERGSRVPLY]命令，配置紧急业务策略。策略项包括：
支持紧急业务 
支持无卡用户紧急业务 
紧急注册鉴权 
鉴权失败放行紧急业务 
受限用户放行紧急业务 
上报PEI构造的SUPI 
默认紧急业务能力， 默认值为：NR和E-UTRA均支持。包括如下选项：NR和E-UTRA均不支持仅NR支持仅E-UTRA支持NR和E-UTRA均支持 
执行[ADD EMERGDATA]命令，新增紧急数据配置的相关参数，包括PLMN、DNN、SMF IP地址、FQDN、用户别名。5GC系统使用这个配置识别紧急DNN。
执行ADD 5GEMERNUMLIST
命令，配置紧急号码列表。
执行ADD 5GEXTEMERNUMLIST
命令，配置扩展紧急号码列表。
执行SET EMERGSRVFALLBACKPLY
命令，配置紧急业务回落策略。
执行SET EMERGSRVSNSSAI
命令，配置紧急切片数据。
执行SET TACFG
命令，设置该TA支持的紧急业务能力。
执行[SET 5GTALISTASSIGNPOLICY]命令，配置接入区域列表分配策略。
配置实例 :场景说明 :配置紧急业务的策略以及紧急业务流程相关的数据。 
数据规划 :配置项|参数名称|取值
---|---|---
紧急业务策略配置|支持紧急业务|是：支持|是：支持
支持无卡用户紧急业务|紧急业务策略配置|是：支持|是：支持
紧急注册鉴权|紧急业务策略配置|是|是
鉴权失败放行紧急业务|紧急业务策略配置|是：放行|是：放行
受限用户放行紧急业务|紧急业务策略配置|是：放行|是：放行
上报PEI构造的SUPI|紧急业务策略配置|是：上报|是：上报
默认紧急业务能力|紧急业务策略配置|NR和E-UTRA均支持|NR和E-UTRA均支持
紧急数据配置|移动国家码|460|460
移动网络码|紧急数据配置|11|11
DNN|紧急数据配置|zte.com.cn|zte.com.cn
SMF IP|紧急数据配置|10.10.10.10|10.10.10.10
SMF 端口号|紧急数据配置|5000|5000
URI scheme|紧急数据配置|http|http
API版本|紧急数据配置|v1|v1
SMF FQDN|紧急数据配置|smf.mnc01.mcc460.5g.org|smf.mnc01.mcc460.5g.org
名称|紧急数据配置|emerg1|emerg1
紧急号码列表配置|紧急号码列表ID|1|1
紧急号码|紧急号码列表配置|110|110
服务类型|紧急号码列表配置|报警|报警
扩展紧急号码列表配置|紧急号码列表ID|1|1
紧急号码|扩展紧急号码列表配置|110|110
URN类型|扩展紧急号码列表配置|urn:service:sos.police|urn:service:sos.police
扩展紧急号码使用范围指示|扩展紧急号码列表配置|PLMN所属国家内有效|PLMN所属国家内有效
紧急业务回落配置|支持紧急业务回落|是：支持|是：支持
紧急回落能力|紧急业务回落配置|NR和E-UTRA均支持|NR和E-UTRA均支持
紧急号码列表ID|紧急业务回落配置|1|1
扩展紧急号码列表ID|紧急业务回落配置|1|1
紧急业务SNSSAI配置|紧急业务SST|eMBB|eMBB
紧急业务SD|紧急业务SNSSAI配置|111111|111111
TA配置|紧急业务能力|NR和E-UTRA均支持|NR和E-UTRA均支持
支持紧急业务回落|TA配置|是|是
紧急回落能力|TA配置|NR和E-UTRA均支持|NR和E-UTRA均支持
紧急号码列表|TA配置|1|1
扩展紧急号码列表|TA配置|1|1
注册区域分配策略|注册区域分配参考紧急业务能力|SAMEEMC|SAMEEMC
配置步骤 :序号|步骤|命令示例
---|---|---
1|设置紧急业务功能开关|SET EMERGSRVPLY:SPRTEMERGSRV="YES",SPRTEMERGSRVCARDLESS="YES",AUTHEMERGREGIST="YES",PASSAUTHFAIL="YES",PASSLIMITEDUSER="YES",RPTSUPICONSTUBYPEI="YES",EMERGENCYCAPA="BOTHNREUTRANNOTSPRT"
2|新增紧急数据配置相关参数|ADD EMERGDATA:MCC="460",MNC="11",DNN="zte.com.cn",SMFIP="10.10.10.",SMFPORT=5000,SCHEMA="HTTP",APIVERSION="V1",SMFFQDN="smf.mnc01.mcc460.5g.org",NAME="emerg1"
3|增加紧急号码：110|ADD 5GEMERNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"&"AMB"
4|增加扩展紧急号码：911|ADD 5GEXTEMERNUMLIST:LISTID=1,NUMBER="911",URNTYPE="urn:service:sos.police",EENLV="VALIDINCOUNTRY"
5|设置紧急业务回落配置|SET EMERGSRVFALLBACKPLY:SPRTEMERGFALLBACK="YES",EMERGFALLBACKCAPA="ONLYNRSPRT",EMERGENCYNUMLISTID=1,EXTEMERGNUMLISTID=1
6|设置紧急业务SNSSAI配置|SET EMERGSRVSNSSAI:EMGSST="eMBB",EMGSD="111111"
7|设置该TA支持紧急业务能力|SET TACFG:TAID=,EMERGCAPA="ONLYNRSPRT",SPRTEMERGFALLBACK="YES",EMERGFALLBACKCAPA="ONLYNRSPRT",EMERGENCYNUMLISTID=1,EXTEMERGNUMLISTID=1
8|设置注册区域分配参考紧急业务能力|SET 5GTALISTASSIGNPOLICY:SAMEEMCCAPA="SAMEEMC"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|紧急注册流程成功
---|---
测试目的|验证紧急注册流程能够成功完成
预置条件|5G网络中各NF系统及操作维护台运行正常。已完成紧急业务相关的数据配置。
测试过程|发起类型为紧急的初始注册请求。
通过准则|没有进行获取切片和切片选择。紧急注册流程成功。验证注册接受带的紧急号码列表为配置的号码列表。
测试结果|–
测试项目|紧急业务请求流程成功
---|---
测试目的|验证紧急业务请求流程能够成功完成
预置条件|5G网络中各NF系统及操作维护台运行正常。已完成紧急业务相关的数据配置。
测试过程|发起类型为紧急的业务请求。
通过准则|没有进行获取切片和切片选择。紧急业务请求流程成功。
测试结果|–
测试项目|紧急新建会话流程成功
---|---
测试目的|验证紧急新建会话流程能够成功完成
预置条件|5G网络中各NF系统及操作维护台运行正常。已完成紧急业务相关的数据配置。
测试过程|发起类型为紧急的新建会话请求。
通过准则|没有进行获取切片和切片选择。紧急新建会话流程成功。
测试结果|–
常见问题处理 :无 
## ZUF-79-13-006 T-ADS 
特性描述 :特性描述 :术语 :术语|含义
---|---
VoNR|语音呼叫通过NR接入5GC网络，在5GC网络中进行IMS语音。
描述 :定义 :T-ADS指用户在IMS域注册后，作为被叫方时，IMS需对用户进行域选择的过程。IMS中的SCC AS向UDM发送域选请求，UDM根据用户注册状态和区域同向性信息，确定是否需向AMF或MME发送T-ADS查询请求，查询UE当前位置是否支持IMS语音、最近接入时间和接入类型；AMF或MME收到T-ADS查询消息后，会返回T-ADS查询结果。
AMF支持T-ADS查询，可以返回UE当前位置是否支持IMS语音、最近接入时间和接入类型信息给UDM。 
背景知识 :移动语音业务是移动运营商的主要收入来源之一，移动通讯技术演进到第5代后，如何为用户提供体验良好的语音业务成为运营商需要迫切解决的问题。 
5G部署主要有两种形态，NSA（5G NR非独立组网）和SA（5G NR独立组网）。
在NSA模式下采用传统4G网络的VoLTE语音解决方案。 
在SA模式下有新的语音接入解决方案，包括VoNR和回落到4G网络后继续语音呼叫接入。4G语音使用VoLTE，终端接入eNodeB，通过EPC网络接入IMS。5G语音使用VoNR，终端接入NG-RAN，通过5GC网络接入IMS。 
5G VoNR语音网络中需要部署IMS，IMS网络与5G网络需互连互通，因为IMS可能不会升级支持N5接口，所以PCF需支持Rx接口；HSS也可能不会升级，UDM需支持Cx和Sh接口。
NG-RAN传递UE的NAS信令，支持语音QoS Flow建立。5GC建立用于VoNR的IMS信令、视频和语音承载。
应用场景 :T-ADS应用于已在IMS注册用户的被叫情况。 
用户注册到IMS网络，被叫用户会在4G网络和5G网络间来回驻留，主叫呼叫5G用户时IMS需要向UDM/HSS发起被叫域问询，UDM/HSS同时向AMF和MME发起被叫域问询，AMF确定当前被叫用户所在域。AMF上报UDM关于支持IMS的同向性指示，UE当前位置是否支持IMS语音、最近接入时间和接入类型。 
客户收益 :受益方|受益描述
---|---
运营商|提高了语音呼叫的成功率，减少了语音呼叫的时延，提升了语音业务体验。
移动用户|语音业务成功率提高，时延缩短。
实现原理 :系统架构 :T-ADS是VoNR功能的一个重要组成部分。 
VoNR中，5G网络是一个IP-CAN，通过IP实现UE和IMS实体之间的连通的网络实体和接口集合，如[图1]所示。
图1  5G语音业务架构(VoNR)

涉及的网元 :网元名称|网元作用
---|---
AMF|VoNR能力管理，在注册流程中给指示UEIMS语音能力。支持将IMS语音同向性指示通知HSS。支持T-ADS。
UDM|向AMF请求用户最新的位置更新信息，将得到的网络信息发送给IMS；向AMF发起被叫域问询。
协议栈 :本特性涉及到的协议栈如[图2]所示。
图2  AMF和其他NF的接口协议栈

本网元实现 :AMF收到UDM的T-ADS查询请求消息后，可以给UDM返回UE当前位置是否支持IMS语音、最近接入时间和接入类型。 
业务流程 :主被叫5G用户都注册到5GC网络，被叫用户会在4G网络和5G网络间来回驻留。因此主叫呼叫5G用户时，需求决策当前被叫用户所在域： 
如果用户当前在5G网络，5GC网络支持IMS语音，则被叫域选5GC网络，被叫路由到IMS。 
如果用户当前在4G网络，EPC网络支持IMS语音，则被叫域选LTE网络，被叫路由到IMS。 
如果UE在AMF和MME上都是注册状态，当呼叫请求到来时，IMS需要向UDM/HSS发起T-ADS问询，UDM/HSS判断“IMS Voice over PS Sessions”为“non-homogeneous”或“unknown”时，HSS/HLR同时向AMF和MME发起T-ADS问询，查询UE当前位置是否支持IMS语音、最近接入时间和接入类型，否则直接向IMS返回UE的T-ADS信息。
T-ADS被叫接入域选择的流程如[图3]所示。
图3  T-ADS被叫接入域选择流程

流程说明： 
UE发起注册请求。 
AMF正常处理注册请求，直到向UDM注册。 
AMF向UDM发送Nudm_UECM_Registration Request消息，携带AMF支持T-ADS能力标记和T-ADS查询的URI。 
UDM保存UE信息。 
UDM向AMF返回Nudm_UECM_Registration Response消息。 
AMF完成注册流程。 
后续IMS的AS-SCC收到UE的MT Invite消息。 
IMS给UDM/HSS发送UDR消息，查询T-ADS信息。 
HSS给UDM发送UDR消息。 
UDM收到查询T-ADS信息的消息后，判断UE的“IMS Voice over PS Sessions”的值。如果为“non-homogeneous”或“unknown”，则发起向T-ADS的查询，给AMF发送Namf_Location_ProvideLocationInfo Request消息；如果为“Supported”或“Not Supported”，则直接向IMS返回UE的T-ADS信息。
AMF判断UE为IDLE态，则发起寻呼，正常进行寻呼和业务请求流程。 
UE为连接态，向NR发起位置信息获取，获取用户当前位置信息。AMF获取用户的如下信息： 
UE当前注册区域是否支持IMS 
UE最后一次活动时间 
当前Access Type和RAT type 
AMF给UDM/HSS返回Namf_Location_ProvideLocationInfo Response消息，携带步骤12获得的信息。 
UDM给HSS返回UDA。 
UDM/HSS向IMS返回UE的T-ADS信息。 
T-ADS查询： 
如果UE只在AMF上注册（即单注册），那么UDM/HSS根据AMF上报的T-ADS信息进行如下决策：是否支持T-ADS Data RetrievalIMS语音同向性指示是否向AMF发起T-ADS查询不支持支持/不支持/未知否支持支持否支持不支持否支持未知是 
如果UE在AMF和MME上都是注册状态（即双注册），并且AMF支持T-ADS Data Retrieval，向HSS上报T-ADS信息，那么HSS进行如下决策：MME上报的IMS语音同向性指示AMF上报的IMS语音同向性指示是否向AMF和MME同时发起T-ADS查询不支持不支持否不支持支持是不支持N未知是未知支持是无不支持是无无是 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :需要VoNR功能开启。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2".|4.4.3和5.16.3节: IMS support
3GPP TS 23.502: "Procedures for the 5G System;Stage2".|4.13.6 Support of IMS Voice
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :如果要使用VoNR业务，需要申请“AMF支持VoNR功能”的License。 
对其他网元的要求 :UE|NR|SMF|PCF|UDM
---|---|---|---|---
-|-|-|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
VoNR功能配置|SET 5GVONRCFG
SHOW 5GVONRCFG|VoNR功能配置
缺省语音参数策略配置|SET 5GDEFAULTSUPIVOICEPOLICY
SHOW 5GDEFAULTSUPIVOICEPOLICY|缺省语音参数策略配置
基于SUPI的语音参数策略配置|ADD 5GSUPIVOICEPOLICY
MOD 5GSUPIVOICEPOLICY|基于SUPI的语音参数策略配置
DEL 5GSUPIVOICEPOLICY|基于SUPI的语音参数策略配置
SHOW 5GSUPIVOICEPOLICY|基于SUPI的语音参数策略配置
缺省语音参数策略配置|SET 5GDEFAULTTAVOICEPOLICY
SHOW 5GDEFAULTTAVOICEPOLICY|缺省语音参数策略配置
基于TA的语音参数策略模板配置|ADD 5GTAVOICEPOLICYTEMPLATE
MOD 5GTAVOICEPOLICYTEMPLATE|基于TA的语音参数策略模板配置
DEL 5GTAVOICEPOLICYTEMPLATE|基于TA的语音参数策略模板配置
SHOW 5GTAVOICEPOLICYTEMPLATE|基于TA的语音参数策略模板配置
AMF支持基于DNN语音策略配置|SET 5GDNNVOICESWITCH
SHOW 5GDNNVOICESWITCH|AMF支持基于DNN语音策略配置
支持语音策略的DNN配置|ADD 5GDNNVOICEPOLICY
DEL 5GDNNVOICEPOLICY|支持语音策略的DNN配置
SHOW 5GDNNVOICEPOLICY|支持语音策略的DNN配置
注册区域分配策略|SET 5GTALISTASSIGNPOLICY
SHOW 5GTALISTASSIGNPOLICY|注册区域分配策略
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :AMF先根据AMF是否打开VoNR配置、基于SUPI号段的语音策略、TA语音策略、DNN语音策略以及用户的UE语音能力决策UE是否具有IMSoverPS能力，在注册接受消息中将IMS语音能力带给UE。 
正常的处理注册请求消息流程中，在向UE发送注册接受消息过程中分配TA list时，AMF可以根据TA list分配本地策略，确定TA List中所有TA的语音能力是否一致。 
AMF在注册流程中，根据TA list分配本地策略，携带UE的IMS同向性信息至UDM。 
AMF根据AMF支持VoNR配置，决策是否对用户进行UE无线能力检查。 
配置前提 :系统运行正常，支持VoNR License打开。 
配置过程 :1. 执行[SET 5GVONRCFG]命令，配置AMF是否支持VoNR功能、及其AMF是否支持UE无线能力检查功能。
2. 执行[SET 5GDEFAULTSUPIVOICEPOLICY]命令，配置是否开启缺省SUPI语音参数策略IMS VoPS业务。
3. 执行[ADD 5GSUPIVOICEPOLICY]命令，配置AMF根据终端用户的SUPI号段和无线侧的接入方式，来配置是否支持 IMS over PS。
4. 执行[SET 5GDEFAULTTAVOICEPOLICY]命令，配置或修改是否开启缺省TA语音参数策略IMS VoPS业务和FallBack业务。
5. 执行[ADD 5GTAVOICEPOLICYTEMPLATE]命令，新增TA语音策略模板。
6. 执行[SET 5GDNNVOICESWITCH]命令，配置AMF是否支持根据终端用户接入的DNN，来开启VoNR功能。
7. 执行[ADD 5GDNNVOICEPOLICY]命令，新增支持语音策略的DNN配置。
8. 执行[SET 5GTALISTASSIGNPOLICY]命令，配置注册区域分配策略。
配置实例 :###### 示例1 
场景说明
IMS语音业务能力指示带给UE。 
在注册过程（包括注册更新）中，开启VoNR功能后，AMF会根据UE语音能力、无线覆盖（TA）、漫游协议（IMSI号段），语音DNN策略确定IMS语音能力，在给UE发送注册接受消息时，通过IMSVoPS字段。指示UE是否可以VoNR 
数据规划
配置项|参数名称|取值
---|---|---
AMF支持VoNR配置|IMSVoPs|支持IMS VoPS业务
基于SUPI号段的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
基于TA的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
FallBack|基于TA的缺省语音参数策略配置|不支持Fallback业务
AMF支持基于DNN语音策略配置|支持DNN语音策略开关|支持DNN语音策略
支持语音策略的DNN配置|DNN|ims
配置步骤
步骤|说明|操作
---|---|---
1|开启AMF支持VoNR功能|SET 5GVONRCFG:IMSVOPS="SPRT",UERADIOCAPCHECK="NO"
2|设置基于SUPI号段的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTSUPIVOICEPOLICY:IMSVOPS="SPRT"
3|设置基于TA的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTTAVOICEPOLICY:IMSVOPS="SPRT",FALLBACK="NOSPRT"
4|设置AMF支持基于DNN语音策略为支持DNN语音配置|SET 5GDNNVOICESWITCH:SUPTDNNVOICEPOLICY="SPRT"
5|增加支持语音策略配置的DNN|ADD 5GDNNVOICEPOLICY:DNN="ims"
###### 示例2 
场景说明
TA-List按IMS语音能力策略分配。在正常的处理注册请求消息流程中，AMF在向UE发送注册接受消息过程中分配TA list时，可以根据TA list分配本地策略，确定TA List中所有TA的语音能力是否一致。 
数据规划
配置项|参数名称|取值
---|---|---
AMF支持VoNR配置|IMSVoPs|支持IMS VoPS业务
基于SUPI号段的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
基于TA的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
FallBack|基于TA的缺省语音参数策略配置|不支持Fallback业务
AMF支持基于DNN语音策略配置|支持DNN语音策略开关|支持DNN语音策略
支持语音策略的DNN配置|DNN|ims
注册区域分配策略|注册区域分配参考IMS VoPS能力|需要具有相同的IMS VoPS能力
配置步骤
步骤|说明|操作
---|---|---
1|开启AMF支持VoNR功能|SET 5GVONRCFG:IMSVOPS="SPRT",UERADIOCAPCHECK="NO"
2|设置基于SUPI号段的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTSUPIVOICEPOLICY:IMSVOPS="SPRT"
3|设置基于TA的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTTAVOICEPOLICY:IMSVOPS="SPRT",FALLBACK="NOSPRT"
4|设置AMF支持基于DNN语音策略为支持DNN语音配置|SET 5GDNNVOICESWITCH:SUPTDNNVOICEPOLICY="SPRT"
5|增加支持语音策略配置的DNN|ADD 5GDNNVOICEPOLICY:DNN="ims"
6|设置注册区域分配策略参考IMSVoPS能力为需要具有相同的IMSVoPS|SET 5GTALISTASSIGNPOLICY:SAMEIMSVOPS="YES"
###### 示例3 
场景说明
AMF将IMS语音同向性信息指示给UDM。用户首次注册过程中，AMF需向UDM注册，在注册消息中携带Homogeneous support for IMS voice over PS Session supported indication信息。 
数据规划
配置项|参数名称|取值
---|---|---
AMF支持VoNR配置|IMSVoPs|支持IMS VoPS业务
基于SUPI号段的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
基于TA的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
FallBack|基于TA的缺省语音参数策略配置|支持Fallback业务
AMF支持基于DNN语音策略配置|支持DNN语音策略开关|支持DNN语音策略
支持语音策略的DNN配置|DNN|ims
注册区域分配策略|注册区域分配参考IMS VoPS能力|需要具有相同的IMS VoPS能力
配置步骤
步骤|说明|操作
---|---|---
1|开启AMF支持VoNR功能|SET 5GVONRCFG:IMSVOPS="SPRT",UERADIOCAPCHECK="NO"
2|设置基于SUPI号段的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTSUPIVOICEPOLICY:IMSVOPS="SPRT"
3|设置基于TA的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTTAVOICEPOLICY:IMSVOPS="SPRT",FALLBACK="NOSPRT"
4|设置AMF支持基于DNN语音策略为支持DNN语音配置|SET 5GDNNVOICESWITCH:SUPTDNNVOICEPOLICY="SPRT"
5|增加支持语音策略配置的DNN|ADD 5GDNNVOICEPOLICY:DNN="ims"
6|设置注册区域分配策略参考IMSVoPS能力为需要具有相同的IMSVoPS|SET 5GTALISTASSIGNPOLICY:SAMEIMSVOPS="YES"
###### 示例4 
场景说明
AMF支持UDM的T-ADS查询。UDM判断用户的"IMS Voice over PS Sessions" 为”non-homogeneous”或”unknown"时，向AMF查询UE的T-ADS信息。 
数据规划
配置项|参数名称|取值
---|---|---
AMF支持VoNR配置|IMSVoPs|支持IMS VoPS业务
基于SUPI号段的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
基于TA的缺省语音参数策略配置|IMSVoPs|支持IMS VoPS业务
FallBack|基于TA的缺省语音参数策略配置|不支持Fallback业务
AMF支持基于DNN语音策略配置|支持DNN语音策略开关|支持DNN语音策略
支持语音策略的DNN配置|DNN|ims
注册区域分配策略|注册区域分配参考IMS VoPS能力|不需要具有相同的IMS VoPS能力
配置步骤
步骤|说明|操作
---|---|---
1|开启AMF支持VoNR功能|SET 5GVONRCFG:IMSVOPS="SPRT",UERADIOCAPCHECK="NO"
2|设置基于SUPI号段的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTSUPIVOICEPOLICY:IMSVOPS="SPRT"
3|设置基于TA的缺省语音参数策略配置为支持IMS VoPS业务|SET 5GDEFAULTTAVOICEPOLICY:IMSVOPS="SPRT",FALLBACK="NOSPRT"
4|设置AMF支持基于DNN语音策略为支持DNN语音配置|SET 5GDNNVOICESWITCH:SUPTDNNVOICEPOLICY="SPRT"
5|增加支持语音策略配置的DNN|ADD 5GDNNVOICEPOLICY:DNN="ims"
6|设置注册区域分配策略参考IMSVoPS能力为不需要具有相同的IMSVoPS|SET 5GTALISTASSIGNPOLICY:SAMEIMSVOPS="NO"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|IMS语音业务能力指示带给UE
---|---
测试目的|在注册过程（包括注册更新）中，开启VoNR功能后，AMF会根据UE的语音能力、无线覆盖、漫游协议，语音DNN策略确定IMS语音能力，在给UE发送注册接受消息时指示UE可以使用VoNR。
预置条件|无线支持IMSVoPSAMF支持VoNR License打开，配置支持VoNR功能用户所在号段支持IMSVoPS用户所在TA支持IMSVoPS基于该用户的语音参数策略配置支持IMSVoPS
测试过程|用户发起注册请求
通过准则|注册接受消息中携带5GS network feature support等信息，5GS network feature support 信息中的IMS VoPS字段指示UE支持IMSoverPS
测试结果|–
测试项目|TA-List按IMS语音能力策略分配
---|---
测试目的|在正常的处理注册请求消息流程中，在向UE发送注册接受消息过程中分配TA list时，AMF可以根据TA list分配本地策略，保证TA List中所有TA的语音能力一致。
预置条件|无线支持IMSVoPSAMF支持VoNR License打开，配置支持VoNR功能用户所在号段支持IMSVoPS用户所在TA支持IMSVoPS基于该用户的语音参数策略配置支持IMSVoPS注册区域分配策略中注册区域分配参考IMS VoPS能力设置为需要具有相同的IMSVoPS
测试过程|用户发起注册请求
通过准则|注册接受消息中AMF给UE分配的TA List中所有TA的都支持IMS语音能力
测试结果|–
测试项目|AMF将IMS语音同向性信息指示给UDM
---|---
测试目的|用户注册过程中，发给UDM的注册消息中携带Homogeneous support for IMS voice over PS Session supported indication信息
预置条件|无线支持IMSVoPSAMF支持VoNR License打开，配置支持VoNR功能用户所在号段支持IMSVoPS用户所在TA支持IMSVoPS基于该用户的语音参数策略配置支持IMSVoPS注册区域分配策略中注册区域分配参考IMS VoPS能力设置为需要具有相同的IMSVoPS
测试过程|用户发起注册请求
通过准则|AMF向UDM发送Nudm_UECM_Registration Request消息时携带的Homogeneous support for IMS voice over PS Session supported indication字段为SUPPORT
测试结果|–
测试项目|AMF支持UDM的T-ADS查询
---|---
测试目的|AMF支持UDM查询UE的T-ADS信息
预置条件|无线支持IMSVoPSAMF支持VoNR License打开，配置支持VoNR功能用户所在号段支持IMSVoPS用户所在TA支持IMSVoPS基于该用户的语音参数策略配置支持IMSVoPS注册区域分配策略中注册区域分配参考IMS VoPS能力设置为不需要具有相同的IMSVoPS
测试过程|用户发起注册，AMF向UDM发送Nudm_UECM_Registration Request消息时携带的Homogeneous support for IMS voice over PS Session supported indication字段为UNKNOWN，注册成功后链路释放处于5G-IDLE态。UDM向AMF发起“UeContext”资源查询，请求T-ADS信息
通过准则|AMF发起寻呼，收到业务请求后向UDM回复“UeContext”资源查询响应消息，消息包含用户当前位置是否支持IMSVoPS,与UE最后一次无线电联系的时间戳,当前RAT类型。
测试结果|–
常见问题处理 :无。 
## ZUF-79-13-007 EPS回落保障信令流程 
概述 :EPS回落保障信令流程是指在语音相关流程和UE或无线侧触发的流程冲突时，AMF保障语音相关流程顺利完成的过程。 
在语音相关流程和切换、注册更新、业务请求流程冲突时，AMF可以缓存或通知SMF缓存语音相关消息，待切换、注册更新、业务请求流程完成后，再处理语音相关流程，从而尽可能地保证语音流程顺利完成。 
AMF对语音业务可设置特定的寻呼策略。 
收益 :在语音相关流程和UE或无线侧触发的流程冲突时，AMF尽可能保障语音相关流程顺利完成，提升用户体验。 
描述 :当AMF检测到网络发起的VoNR专用QoS流流程与UE或无线网络发起的流程冲突时，AMF缓存网络发起的VoNR专用QoS流流程，待UE或无线网络发起的流程完成后，AMF再重新处理网络发起的VoNR专用QoS流流程，或向SMF返回携带具体原因的故障响应。SMF则会缓存网络发起的VoNR专用QoS流流程，在UE或无线网络发起的流程完成后，继续处理网络发起的VoNR专用QoS流流程。 
AMF对语音业务可设置特定的寻呼策略。 
具体信息，参照协议3GPP 23502 4.9.1.2 基于Xn接口的NG-RAN间切换和4.9.1.3 基于N2接口的NG-RAN间的切换。 
# 缩略语 
# 缩略语 
5GC :5G Core Network5G核心网
AMF :Access and Mobility Management Function接入和移动管理功能
## ARP 
Allocation and Retention Priority分配保持优先级
## CSFB 
Circuit Switched Fallback电路域回落
DNN :Data Network Name数据网名称
EPC :Evolved Packet Core演进的分组核心网
EPS :Evolved Packet System演进的分组系统
GUTI :Globally Unique Temporary Identity全球唯一临时标识
HSS :Home Subscriber Server归属用户服务器
IMS :IP Multimedia SubsystemIP多媒体子系统
## MICO 
Mobile Initiated Connection Only仅限移动发起连接
MME :Mobility Management Entity移动管理实体
NAS :Network Access Service网络接入服务
## NG-RAN 
Next Generation Radio Access Network下一代无线接入网
## NR 
New Radio新无线
## NSA 
Non-Standalone5G非独立组网
PCF :Policy Control Function策略控制功能
PCRF :Policy and Charging Rules Function策略和计费规则功能
PDU :Packet Data Unit分组数据单元
## PEI 
Permanent Equipment Identifier永久设备标识
## PGW-C 
PDN Gateway Control plane functionPGW控制面网关
## PGW-U 
PDN Gateway User plane functionPGW用户面网关
## PPD 
Parallel Presence Detect并行存在检测
QoS :Quality of Service服务质量
S-NSSAI :Single Network Slice Selection Assistance Information单个网络切片选择辅助信息
## SA 
Standalone5G独立组网
SMF :Session Management Function会话管理功能
## SUCI 
Subscription Concealed Identifier签约的隐藏标识符
SUPI :Subscriber Permanent Identifier用户永久标识
## T-ADS 
Terminating Access Domain Selection终结接入域选择
UDM :Unified Data Management统一数据管理
UPF :User Plane Function用户平面功能
## VoLTE 
Voice over LTELTE语音
VoNR :Voice over New Radio新空口承载语音
eNodeB :Evolved NodeB演进的NodeB
# ZUF-79-14 短消息业务 
## ZUF-79-14-001 SMS over IP 
概述 :AMF判断UE是否具有IMS over PS能力，并在注册接受消息中指示IMS over PS能力给UE。AMF支持SMS over IP，即IMS提供SMS服务，5GC提供IP承载。 
客户收益 :在5GC网络中传送短消息。 
说明 :AMF支持SMS over IP，即IMS提供SMS服务，5GC提供IP承载。用户在IMS注册后，短消息由IP-SM-GW通过IMS投递。 
AMF需要在注册接受消息中指示IMS over PS能力给UE。AMF判断UE是否有IMS over PS能力时，需要考虑以下因素： 
业务PLMN（本地VoNR开关）的VoNR能力 
归属PLMN（IMSI号段）的VoNR能力 
TA 
UE的语音能力 
语音连续性能力 
## ZUF-79-14-002 SMS over NAS 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :SMS over NAS是指短消息通过5G网络的信令面进行传递。
AMF提供短消息业务能力协商，并通过NAS消息透传MO/MT（起呼短消息/终呼短消息）。 
背景知识 :随着物联网在各行各业的蓬勃发展，SMS的应用场景越来越多。例如，大量的水电表监测、水质水位监测系统等，可以采用SMS方式通过短消息中心向其应用服务器上报采集的数据。 
比较项|5G网络|4G网络|2/3G网络
---|---|---|---
短消息方式|IMS短信、SMS over NAS|SGs短信、SGd短信、IMS短信|CS短信/PS短信
适用的业务场景|适用人网和物联网短消息业务|适用人网和物联网短消息业务|适用人网短消息业务
在SMS over NAS短消息业务架构下，AMF通过SMSF与短消息中心交互，建立控制面通道投递上下行短消息数据。AMF支持短消息注册、短消息去注册、短消息起呼和短消息终呼。 
应用场景 :SMS over NAS主要为用户提供空闲态或连接态下的短消息起呼和终呼。短消息起呼和终呼的前提是用户先进行短消息注册到网络。如果用户不想再使用短消息，则发起短消息去注册。 
终端短消息注册/去注册
用户向5G网络注册时同时注册短消息业务，如果用户有短消息权限，则AMF向SMSF激活短消息业务，SMSF向UDM注册短消息业务。用户在后续注册时不再指示短消息支持能力，或AMF发起UE去注册，或UDM通知去注册时，则AMF向SMSF去激活短消息业务，SMSF向UDM去注册短消息业务。 
终端短消息起呼
UE在空闲态或连接态时，要发送短消息。UE通过AMF向SMSF发送起呼短消息内容，由SMSF投递短信给短消息中心。UE空闲态时，需要先触发业务请求连接到网络中。 
终端短消息终呼
UE在空闲态或连接态时，短消息中心要下发短消息给UE，短消息中心通知SMSF，SMSF检查签约，如果允许UE投递短信，则SMSF通过AMF向UE下发短消息内容。UE空闲态时，AMF要先寻呼UE，触发业务请求让UE连接到网络中。 
客户收益 :受益方|受益描述
---|---
运营商|为用户提供多样化的业务特性，提升用户满意度，保障短消息业务需求。
移动用户|享用短消息业务。


实现原理 :



系统架构 :本特性涉及到的网络结构如[图1]和[图2]所示。
图1  非漫游时 SMS over NAS系统架构




图2  漫游时 SMS over NAS系统架构






涉及的网元 :网元名称|网元作用
---|---
UE|UE通过NR接入网络。
NR|支持终端接入。
AMF|支持短消息注册、短消息去注册、短消息起呼和短消息终呼。
UDM|负责短消息签约、SMS信息保存（包括SMSF信息）。
SMSF|负责短消息激活、去激活、短消息上下行投递。


协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N8|ZUF-79-19-003 N8
N20|-


本网元实现 :SMS over NAS短消息业务架构下，AMF通过SMSF与短消息中心交互，建立控制面通道投递上下行短消息数据。AMF支持短消息注册、短消息去注册、短消息起呼和短消息终呼。 


业务流程 :短消息注册
SMS over
NAS短消息业务架构下，短消息注册流程如[图3]所示。
图3  支持SMS over NAS的短消息注册流程




流程说明如下： 


在注册过程中，UE在Registration Request消息中携带"SMS supported"，指示UE是否具有SMS
over NAS的能力，UE是否支持SMS透过NAS传递。


执行注册流程，同现有的系统处理，参见“3GPP 23.502协议中图4.2.2.2.2-1的步骤4~14”。 
AMF通过Nudm_SDM_Get消息向UDM获取SMS签约数据和SMSF数据中的UE上下文。
UDM通过Nudr_DM_Query消息向UDR获取SMS信息。UDM返回Nudm_SDM_Get Response消息。如果存储的SMSF和AMF属于同一PLMN，则携带SMSF信息。
响应消息指示成功且短消息业务允许时，AMF发起Nudm_SDM_Subscribe订阅SMS签约数据修改通知，UDM发送Nudr_DM_Subscribe向UDR发起订阅。 
AMF也可能从old AMF收到的UE上下文信息中包含SMSF信息，old AMF在Namf_Communication_UEContextTransfer
Response消息中传递SMSF信息给new AMF。 
SMSF和其地址的获取方式和优先级为： 

 
AMF从UDM获取SMSF信息。即使已经从old AMF获得过SMSF信息，也以最新从UDM获取到的SMSF信息为准。 

 
AMF从old AMF收到的UE上下文信息中包含SMSF信息。 

 
在上述两种情况下，AMF没有获得SMSF信息，则AMF通过本地配置或NRF选择一个SMSF。 

 


AMF根据UE在Registration Request消息中的"SMS supported"指示和SMS签约数据，检查SMS业务是否允许。

 
如果SMS业务允许，并且UE上下文包含一个服务PLMN可用的SMSF，AMF激活这个SMSF地址并继续完成注册流程。 

 
如果SMS业务允许，但在注册流程中（图3的步骤2）获得的UE上下文中不包含SMSF信息，AMF发现并选择一个服务于UE的SMSF。 

 


继续执行注册流程，同现有的系统处理，参见“3GPP 23.502协议中图4.2.2.2.2-1的步骤15~20”。 


AMF发送Nsmsf_SMService_Activate Request消息给SMSF，会携带AMF address、Access
Type、Trace Requirements、GPSI (if available) and SUPI。如果AMF收到Trace
Requirements的签约信息，则携带Trace Requirements。


SMSF发现一个UDM。 


如果SMSF中保存有UE现有接入类型的UE上下文，则SMSF用新的AMF地址替换旧的AMF地址。否则，SMSF使用现有接入类型向UDM发送Nudm_UECM_Registration消息。 
UDM保存SUPI、SMSF标识、SMSF地址、SMSF数据的UE上下文中的接入类型。UDM通过Nudr_DM_Update消息将SMSF信息存储到UDR，消息中携带SUPI、订阅数据、SMSF数据中的UE上下文。 
SMSF发送Nudm_SDM_Get向UDM获取SMS管理订阅数据，如短信远程服务、短信限制列表。UDM可能通过Nudr_DM_Query（携带SUPI、订阅数据、SMS管理订阅数据）向UDR获取这些信息。 
SMSF收到成功的响应，并发送Nudm_SDM_Subscribe订阅SMS管理订阅数据修改通知。UDM可能发送Nudr_DM_Subscribe向UDR订阅。 
SMSF也创建一个UE上下文存储SMS签约信息和服务于UE的AMF地址。 


SMSF发送Nsmsf_SMService_Activate Response消息给AMF，AMF存储SMSF信息在UE上下文中。 


AMF收到SMSF的成功指示，AMF向UE发送Registration Accept消息，携带"SMS over
NAS allowed"， 指示UE网络允许SMS通过NAS透传。


短消息去注册
在如下情况中，AMF基于本地配置发送Nsmsf_SMService_Deactivate通知SMSF释放短消息UE上下文，给UDM发送Nudm_SDM_Unsubscribe
service去订阅SMS签约数据改变通知。 

 
UE指示AMF自己不再发送和接收SMS over NAS时，UE在后续注册消息中不携带"SMS supported"指示。 

 
AMF发起UE去注册。 

 
AMF收到UDM去注册通知并指示UE初始注册。 

 
取消签约。 

 
UE移动到EPS网络。 

 
SMSF发送Nudm_SDM_Unsubscribe给UDM去订阅SMS管理订阅数据改变通知。UDM发起Nudr_DR_Unsubscribe通知UDR去订阅。 
SMSF发送Nudm_UECM_Deregistration（携带SUPI、NF ID、Access Type）给UDM，UDM删除UE的SMSF地址。UDM通过Nudr_DR_Update（携带SUPI、Subscription Data、SMS Subscription data、SMSF address）更新UDR。SMSF删除用于SMS的UE上下文和AMF地址。
空闲态短消息起呼
空闲态MO SMS over NAS流程如[图4]所示。
图4  空闲态MO SMS over NAS流程




流程说明： 


空闲态下UE执行业务请求流程，UE向AMF发送Service Request消息。 


2a. UE构造SMS消息（CP-DATA/RP-DATA/TPDU/SMS-SUBMIT parts），并封装在Uplink
NAS transport消息中。UE向AMF发送Uplink NAS (SMS body) transport消息。
2b. AMF发送Nsmsf_SMService_UplinkSMS（携带SMS body、SUPI、IMEISV、当前ULI
 ）给SMSF，便于SMSF准确计费。
2c. SMSF发送Namf_Communication_N1N2MessageTransfer响应给AMF。 
2d. AMF给UE返回短消息响应Downlink NAS transport消息。 


SMSF检查SMS管理订阅数据，如果SMS允许投递，执行投递流程（[图4]中的步骤3~5）。


6a. SMSF向AMF发送Namf_Communication_N1N2MessageTransfer（携带Submit
Report）消息。
6b. AMF向UE发送Downlink NAS transport（携带Submit
Report）消息给UE。
 说明： 
如果此Submit Report是最后一条投递给UE的消息，即不再有SMS数据投递给UE，则SMSF在发送的Namf_Communication_N1N2MessageTransfer消息中包含last message indication。如果UE有多条SMS消息发送，则AMF和SMSF继续执行投递流程（[图4]中的步骤2a~6b）。
6c. 当SMS消息发送完毕，UE向AMF返回Uplink NAS
transport（CP-ack）消息。 
6d. AMF返回Nsmsf_SMService_UplinkSMS（CP-ack）消息给SMSF。 


连接态短消息起呼
连接态MO SMS流程除不需要UE触发业务请求流程之外，后续流程同空闲态MO SMS over NAS的流程处理。
空闲态短消息终呼
空闲态MT SMS over NAS流程如[图5]所示。
图5  通过3GPP接入的空闲态MT SMS over NAS流程




流程说明： 


SC发送Message transfer给SMS-GMSC消息，下发短消息。 


SMS-GMSC向UDM发送Send Routing info for SM消息获取SMSF地址。 


SMS-GMSC传递终呼短消息给SMSF。 


4a. SMSF检查SMS管理订阅数据。如果SMS允许投递，SMSF发送Namf_MT_EnableUEReachability Request消息给AMF。 
4b. AMF发现UE处于空闲态，发起寻呼。UE响应寻呼，触发业务请求流程。业务请求流程处理完成，UE进入连接态。 
4c. AMF发送Namf_MT_EnableUEReachability
Response给SMSF。 


5a. SMSF发送Namf_Communication_N1N2MessageTransfer (SMS body)给AMF。 
5b. AMF发送Downlink NAS transport（携带SMS body）消息给UE。 
5c. UE接收MT短消息，向AMF返回Uplink
NAS (CP ack) transport消息。 
5d. AMF发送Nsmsf_SMService_UplinkSMS
(CP ack)给SMSF，便于SMSF准确计费。AMF携带IMEISV和当前ULI。


6a. UE返回Uplink NAS transport (delivery report)给AMF。 
6b.
AMF发送Nsmsf_SMService_UplinkSMS (delivery report)给SMSF。 
6c. SMSF接受UE的投递报告，发送Namf_Communication_N1N2MessageTransfer（CP
ack）给AMF。 
6d. AMF发送Downlink NAS transport (CP ack)给UE。 
 说明： 
如果此SMS CP ack是最后一条投递给UE的消息，即不再有SMS数据投递给UE，则SMSF在发送的Namf_Communication_N1N2MessageTransfer消息中包含last message indication。如果SMSF有多条SMS消息发送，则SMSF和AMF继续执行投递流程（[图5]中的步骤4~6c）。


步骤6c和6d执行的同时, SMSF投递Delivery Report给SC。  


连接态短消息终呼
连接态MT SMS流程除了下面两处不同，其他流程同空闲态MT SMS over NAS的流程处理。

 
AMF不需要执行UE寻呼，可以立即允许SMSF开始投递MT SMS（跳过图5中的步骤4b）。 

 
如果NAS PDU中包含SMS失败（例如UE RRC Inactive、NG-RAN寻呼失败），NG-RAN触发UE上下文释放，并且通知AMF
NAS无法投递。AMF提供无法投递指示给SMSF。 

 




系统影响 :如果SMS MO/MT的话务量较大，则会影响系统的CPU负荷。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501:”System Architecture for the 5G System”|4.4.2 SMS over NAS5.16.2 SMS over NAS
3GPP TS 23.502: "Procedures for the 5G System"|4.13.3 SMS over NAS procedures
3GPP TS 29.503:”Unified Data Management Services”|5.2.2.2.6 SMS Subscription Data Retrieval5.2.2.2.7 SMS Management Subscription Data Retrieval5.2.2.2.12 UE Context In SMSF Data Retrieval6.1.3.9 Resource: SMSSubscriptionData6.1.3.10 Resource: SMSManagementSubscriptionData6.1.6.2.13 Type: SmsSubscriptionData6.1.6.2.14 Type: SmsManagementSubscriptionData
3GPP TS 29.540:”SMS Services”|-
特性能力 :名称|指标
---|---
基于SUPI的SMSF地址解析|支持1024个号段
可获得性 :License要求 :该特性需要受License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License为“AMF支持SMS over NAS功能”。 
对其他网元的要求 :UE|eNodeB|UDM|SMSF
---|---|---|---
√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增和修改的配置项参见下表。 
配置项|命令
---|---
SMS over NAS策略配置|SET SMSPOLICY
SHOW SMSPOLICY|SMS over NAS策略配置
默认SMSF配置|SET DFTSMSF CONFIG
SHOW  DFTSMSF CONFIG|默认SMSF配置
本地解析SMSF配置|ADD SMSFLOCALRESO
DEL SMSFLOCALRESO|本地解析SMSF配置
SHOW SMSFLOCALRESO|本地解析SMSF配置
发现SMSF参数配置|SET NRFDISCSMSFPARACFG
SHOW NRFDISCSMSFPARACFG|发现SMSF参数配置
配置项|命令|新增参数
---|---|---
发现模式配置|SET NFDISCOVERYMODE CONFIG|SMSF发现模式
地址类型选择策略配置|SET NFADDRCHOICEPOLICYCFG|SMSF地址选择策略
等价NF选择策略配置|SET NFSELECTPOLICY|SMSF选择策略
性能统计 :测量类型|描述
---|---
N20接口测量|编号为C51060开头的所有计数器
短消息流程测量|编号为C51006开头的所有计数器
告警和通知 :该特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :当需要AMF支持SMS over NAS功能时，需要进行相应的配置。配置成功后，AMF通过SMSF与短消息中心交互，建立控制面通道投递上下行短消息数据。 
配置前提 :AMF/MME运行正常。 
EM网管能正常连接并登录。 
"AMF支持SMS over NAS功能" License项已打开。 
配置过程 :执行[SET SMSPOLICY]命令，配置AMF支持SMS over NAS功能，以及用户去注册时通知SMSF。
执行[SET NFDISCOVERYMODE CONFIG]命令，配置发现SMSF的方式。
执行[SET NRFDISCSMSFPARACFG]命令，配置NRF发现SMSF时，在发现请求消息中是否携带SUPI。
（可选）执行[SHOW NFDISCOVERYMODE CONFIG]命令，如果发现SMSF的方式为通过本地配置发现，则需要配置默认SMSF地址，或者按号段配置SMSF地址。
通过SET DFTSMSF CONFIG命令，配置默认的SMSF地址。 
通过ADD SMSFLOCALRESO命令，配置基于SUPI号段的SMSF地址。 
5（可选）如果需要支持SMSF容灾，则需要通过[SET SMSFDRCFG]，设置容灾配置项。
配置实例 :场景一 :场景说明
在5G网络中，配置支持SMS over NAS功能。在用户注册过程中激活SMS over NAS和用户去注册过程中去激活SMS over NAS时，设置AMF通过NRF发现SMSF的场景。
数据规划
配置项|参数名称|取值
---|---|---
SMS over NAS策略配置|AMF是否支持SMS over NAS|SUPPORT
当用户去注册时是否通知SMSF|SMS over NAS策略配置|YES
发现模式配置|SMSF发现模式|DiscNfByNrf
发现SMSF参数配置|携带SUPI|NO
配置步骤
步骤|配置说明|命令示例
---|---|---
1|修改SMS over NAS策略配置，支持SMS over NAS。|SET SMSPOLICY:SUPPORTSMSOVERNAS="SUPPORT",NOTIFYSMSFONDEREG="YES"
2|配置发现SMSF的方式。|SET NFDISCOVERYMODE CONFIG:DISCOVERYSMFMODE="DiscNfByNrf"
3|配置发现SMSF时，在发现请求消息中不携带SUPI。|SET NRFDISCSMSFPARACFG:CARRYSUPI="NO"
场景二 :场景说明
在5G网络中，配置支持SMS over NAS功能。在用户注册过程中激活SMS over NAS和用户去注册过程中去激活SMS over NAS时，设置AMF通过本地配置发现SMSF的场景。 
数据规划
配置项|参数名称|取值
---|---|---
SMS over NAS策略配置|AMF是否支持SMS over NAS|SUPPORT
当用户去注册时是否通知SMSF|SMS over NAS策略配置|YES
发现模式配置|SMSF发现模式|DiscNfByNrf
SMSF IP地址信息|地址池标识|1
IP地址|SMSF IP地址信息|196.165.100.8
端口号|SMSF IP地址信息|8080
SMSF profile信息|SMSF Profile标识|1
主机名|SMSF profile信息|zte.com
地址池标识|SMSF profile信息|1
优先级|SMSF profile信息|0
权重|SMSF profile信息|200
URI scheme|SMSF profile信息|HTTP
API版本|SMSF profile信息|V1
SMSF本地解析配置|SUPI号段|46011
SMSF Profile标识|SMSF本地解析配置|1
配置步骤
步骤|配置说明|命令示例
---|---|---
1|修改SMS over NAS策略配置，支持SMS over NAS。|SET SMSPOLICY:SUPPORTSMSOVERNAS="SUPPORT",NOTIFYSMSFONDEREG="YES"
2|配置发现SMSF的方式。|SET NFDISCOVERYMODE CONFIG:DISCOVERYSMFMODE="DiscNfByNrf"
3|配置SMSF的地址池信息。|ADD SMSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="196.165.100.8",PORT=8080
4|配置SMSF profile信息。|ADD SMSFPROFILECFG:SMSFPROFILEID=1,HOST="zte.com",IPADDRESSID=1,PRIORITY=0,WEIGHT=200,SCHEMA="HTTP",APIVERSION="V1"
5|配置SMSF本地解析配置。|ADD SMSFLOCALRESO:SUPISEG="46011",SMSFPROFILEID=1
场景三 :场景说明
本配置适用于UE发起MO SMS场景。
 说明： 
UE接收MT SMS场景无特殊配置，本场景描述的配置也适用于UE接收MT SMS场景。 
数据规划
配置项|参数名称|取值
---|---|---
SMS over NAS策略配置|AMF是否支持SMS over NAS|SUPPORT
当用户去注册时是否通知SMSF|SMS over NAS策略配置|YES
发现模式配置|SMSF发现模式|DiscNfByNrf
发现SMSF参数配置|携带SUPI|NO
SMSF容灾配置|支持SMSF无响应重选（非首次激活）|SPRT
支持MO/MT SMS over NAS流程冲突处理|SMSF容灾配置|SPRT
配置步骤
步骤|配置说明|命令示例
---|---|---
1|修改SMS over NAS策略配置，支持SMS over NAS。|SET SMSPOLICY:SUPPORTSMSOVERNAS="SUPPORT",NOTIFYSMSFONDEREG="YES"
2|配置发现SMSF的方式。|SET NFDISCOVERYMODE CONFIG:DISCOVERYSMFMODE="DiscNfByNrf"
3|配置发现SMSF时，在发现请求消息中不携带SUPI。|SET NRFDISCSMSFPARACFG:CARRYSUPI="NO"
4|配置支持SMSF无响应重选，支持MO/MT SMS over NAS流程冲突。|SET SMSFDRCFG:SUPSMSFNRSPRSEL="SPRT",SUPMOMTSMSCONFLICT="SPRT"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|在AMF通过NRF发现SMSF的场景下短消息收发功能正常
---|---
测试目的|AMF通过NRF发现SMSF，UE能够正常收发短消息。
预置条件|UE-1、UE-2、AMF、NG-RAN、SMSF各网元正常。AMF配置支持SMS over  NAS。AMF配置通过NRF发现SMSF。UE-1和UE-2已经注册成功。
测试过程|UE-1发送短消息给UE-2。
通过准则|UE-2成功收到UE-1发送的短消息。
测试结果|–
测试项目|在AMF通过本地配置发现SMSF的场景下短消息收发功能正常
---|---
测试目的|AMF通过本地配置发现SMSF，UE能够正常收发短消息。
预置条件|UE-1、UE-2、AMF、NG-RAN、SMSF各网元正常。AMF配置支持SMS over NAS。AMF通过本地配置发现SMSF。UE-1和UE-2已经注册成功。
测试过程|UE-1发送短消息给UE-2。
通过准则|UE-2成功收到UE-1发送的短消息。
测试结果|–
测试项目|容灾情况下短消息收发正常
---|---
测试目的|容灾情况下，UE能够正常收发短消息。
预置条件|UE-1、UE-2、AMF、NG-RAN各网元正常。网络中两个SMSF，其中一个故障，一个正常。AMF配置支持SMS over NAS。UE-1和UE-2已经注册成功。
测试过程|UE-1发送短消息给UE-2。
通过准则|UE-2成功收到UE-1发送的短消息。
测试结果|–
常见问题处理 :无 
# 缩略语 
# 缩略语 
## IMEISV 
International Mobile Equipment Identity and Software Version number国际移动设备识别码和软件版本号
## MO 
Mobile Originated移动台发起
NAS :Network Access Service网络接入服务
## NR 
New Radio新无线
NRF :NF Repository Function网络功能仓储
SMS :Short Message Service短消息业务
## SMSF 
Short Message Service Function短消息服务功能
UDM :Unified Data Management统一数据管理
UDR :Unified Data Repository统一数据存储
## ULI 
User Location Information用户位置信息
# ZUF-79-15 网络暴露 
## ZUF-79-15-001 内部事件暴露 
特性描述 :特性描述 :术语 :术语|含义
---|---
内部事件暴露|3GPP内部NFs间互相订阅、上报移动性相关等事件。
描述 :定义 :AMF网元内部事件暴露是指AMF能向3GPP内的其他NF暴露移动性相关的事件。其他NF向AMF订阅移动性相关事件，AMF启动用户状态监测，监测到用户相应的订阅事件，发送相应的移动性事件报告给订阅的NF。 
背景知识 :AMF是一个移动管理网元，它向其他NF提供用户移动状态能力开放信息，目前包括UE位置信息、移动状态和连接状态等。 
应用场景 :3GPP内的其他NF往往有订阅用户移动状态的需求，如根据终端位置进行计费策略制定或者上报上层业务应用，需要订阅其位置信息；对终端下发数据，需要订阅其连接状态等。因此AMF支持如下内部事件暴露： 
位置信息：位置、UE是否在特定感兴趣区域（Presence-In-AOI）的订阅和上报 
移动状态：UE当前的注册状态和接入类型的订阅和上报 
移动连接状态：UE连接状态（IDLE/CONNECTED）和可达状态（reachability state）的订阅和上报 
终端位置事件暴露 
3GPP网络内其他NF存在根据终端位置进行计费等策略的制定或者进行网络业务处理的需求。当其他NF（如SMF）需要获得终端的位置信息时，需要向AMF订阅终端UE的位置和/或UE是否在特定感兴趣区域（Presence-In-AOI）。AMF检测到UE位置改变和/或UE在指定感兴趣区域时，向其他NF发送位置报告。 
终端移动状态事件暴露 
3GPP网络内其他NF需要根据终端的注册状态和接入类型进行下一步的网络业务处理，如切换、语音终呼。当其他NF（如其他局点的AMF、SMF、UDM）需要获得终端的注册状态和接入类型时，需要向AMF订阅终端UE的注册状态和/或接入类型。AMF向其他NF上报UE当前的注册状态和/或接入类型事件报告。 
终端移动连接状态事件暴露 
网络下发下行数据给UE时，终端连接状态未知，可通过SMF先向AMF订阅UE 连接状态（IDLE/CONNECTED）。AMF向SMF上报UE 当前的连接状态（IDLE/CONNECTED），如果UE在IDLE态，SMF继续订阅UE可达状态（reachability state）。当AMF检测到UE可达时，向SMF上报可达事件报告。SMF收到UE可达通知时，触发下行用户面通道建立，保证下行数据成功投递；如果UE不可达，SMF缓存下行数据暂不投递。 
语音终呼时，UDM确定UE是否在5G网络，需要订阅终端移动连接状态。AMF向UDM上报UE 当前的连接状态（IDLE/CONNECTED），或检测到UE可达时，向UDM上报可达事件报告。UDM确定UE在5G网络后，通知IMS在5G网络进行语音终呼。 
客户收益 :受益方|受益描述
---|---
运营商|提高业务成功率。提升用户满意度，保障多样的业务需求。
移动用户|享受优质的网络服务。
实现原理 :系统架构 :其他NF（UDM、SMF、PCF等）通过HTTP RESTful服务化接口向AMF订阅移动性相关事件。 
图1  5G System architecture

涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
UE|UE通过NR接入网络。
NR|支持终端接入。
AMF|AMF向3GPP内的其他NF暴露移动性相关的事件。其他NF向AMF订阅移动性相关事件，AMF启动用户状态监测，监测到用户相应的订阅事件，发送相应的移动性事件报告给订阅的NF。
UDM|UDM向AMF发起订阅，如订阅终端的注册状态、接入类型、连接状态和UE可达等事件。AMF检测到相应的订阅事件，上报UDM。
SMF|SMF向AMF发起订阅，如订阅终端的位置、UE是否在特定感兴趣区域、注册状态、接入类型、连接状态和UE可达等事件。AMF检测到相应的订阅事件，上报SMF。
协议栈 :AMF与其他NF之间的接口协议栈，基于HTTP RESTful服务化接口提供服务。 
图2  接口协议栈

本NF/网元实现 :AMF向3GPP内的其他NF暴露移动性相关的事件。其他NF向AMF订阅移动性相关事件，AMF启动用户状态监测，监测到用户相应的订阅事件，发送相应的移动性事件报告给订阅的NF。支持位置、UE是否在特定感兴趣区域、接入类型、注册类型、连接状态和可达状态等订阅事件的订阅、上报和去订阅。 
业务流程 :AMF处理流程包括： 
公共订阅流程
图3  公共订阅流程

NF Service Consumer向AMF发起订阅，订阅事件包括：位置、UE是否在特定感兴趣区域（Presence-In-AOI）、注册状态、接入类型、连接状态（IDLE/CONNECTED）及可达状态（reachability state）等。 
根据不同处理情况： 
AMF返回成功响应。如果是单次订阅，AMF在响应消息中携带订阅事件报告。 
如果AMF处理失败，则返回4xx/5xx并携带失败原因。 
公共上报流程
图4  公共上报流程

NF Service Consumer向AMF发起订阅，订阅事件包括：位置、UE是否在特定感兴趣区域（Presence-In-AOI）、注册状态、接入类型、连接状态（IDLE/CONNECTED）及可达状态（reachability state）等。 
AMF返回成功响应。如果是单次订阅，AMF在响应消息中携带订阅事件报告。如果AMF处理失败，则返回4xx/5xx并携带失败原因。 
位置订阅/上报
3GPP内的NF向AMF订阅UE最近一次的位置信息和后续的更新位置。如果是单次订阅，AMF上报UE最近一次的位置信息（TAI, Cell-ID for 3GPP access, most recent N3IWF node, UE local IP address）；如果是持续订阅，AMF检测到UE位置改变，就上报UE的最新位置信息，到了要求的截止时间或最大报告数AMF停止订阅检测和上报。 
UE是否在特定感兴趣区域订阅/上报
3GPP内的NF向AMF订阅UE当前是否在特定感兴趣区域。如果是单次订阅，AMF检测UE是否在特定区域时，上报一次报告：UE-ID，Area identifier，Presence Status (IN/OUT/UNKNOWN)。如果是持续订阅，AMF检测到UE进入或离开特定区域时，就上报一次报告：UE-ID，Area identifier，Presence Status (IN/OUT/UNKNOWN)，到了要求的截止时间或最大报告数AMF停止订阅检测和上报。 
接入类型订阅/上报
3GPP内的NF向AMF订阅UE当前的接入类型。如果是单次订阅，AMF上报一次UE当前的接入类型(3GPP, Non-3GPP)和UE ID。如果是持续订阅，AMF检测到UE的接入类型发生改变时，就上报一次报告：UE ID, access-types (3GPP, Non-3GPP)，到了要求的截止时间或最大报告数AMF停止订阅检测和上报。 
注册状态订阅/上报
3GPP内的NF向AMF订阅UE当前的注册状态。如果是单次订阅，AMF上报一次UE当前的注册状态(REGISTERED/DEREGISTERED)和UE ID。如果是持续订阅，AMF检测到UE的注册状态发生改变时，就上报一次报告：UE ID, registration state  (REGISTERED/DEREGISTERED)，到了要求的截止时间或最大报告数AMF停止订阅检测和上报。 
连接状态订阅/上报
3GPP内的NF向AMF订阅UE当前的连接状态。如果是单次订阅，AMF上报一次UE当前的连接状态(IDLE/CONNECTED)和UE ID。如果是持续订阅，AMF检测到UE的连接状态发生改变时，就上报一次报告：UE ID, 连接状态  (IDLE/CONNECTED)，到了要求的截止时间或最大报告数AMF停止订阅检测和上报。 
可达状态订阅/上报
3GPP内的NF向AMF订阅UE当前的可达状态。如果是单次订阅，AMF上报一次UE当前的可达状态(REACHABLE/UNRACHABLE/REGULATORY-ONLY)和UE ID、AMF Id。如果是持续订阅，AMF检测到UE的可达状态发生改变时，就上报一次报告：UE ID, AMF Id，可达状态  (REACHABLE/UNRACHABLE/REGULATORY-ONLY)，到了要求的截止时间或最大报告数AMF停止订阅检测和上报。 
时区订阅/上报
3GPP内的NF向AMF订阅UE的时区（TIMEZONE_REPORT）。如果是单次订阅，AMF上报一次UE当前的时区和UE ID。如果是持续订阅，AMF检测到UE的时区发生改变时，就上报一次时区和UE ID，直到到达截止时间或最大报告次数时，AMF停止订阅检测和上报。 
通信故障订阅/上报
3GPP内的NF向AMF订阅UE的通信故障事件（COMMUNICATION_FAILURE_REPORT）。如果是单次订阅，AMF在识别出通信故障时（如注册失败等），上报一次通信故障事件并携带失败原因值和UE ID。如果是持续订阅，AMF检测到UE的通信故障时，就上报一次，直到到达截止时间或最大报告次数时，AMF停止订阅检测和上报。 
连接丢失订阅/上报
3GPP内的NF向AMF订阅UE的连接丢失事件（LOSS_OF_CONNECTIVITY）。如果是单次订阅，AMF在UE的可达定时器超时或去注册时，上报一次连接丢失事件和UE ID。如果是持续订阅，AMF检测到UE的可达定时器超时或去注册时，就上报一次报告，直到到达截止时间或最大报告次数，AMF停止订阅检测和上报。 
区域内用户数量订阅/上报
3GPP内的NF向AMF订阅区域内用户数量事件（UES_IN_AREA_REPORT）。如果是单次订阅，AMF在统计后上报一次区域内当前用户数量。如果是持续订阅，AMF周期性统计并上报区域内用户数量，直到到达截止时间或最大报告次数，AMF停止订阅和上报。 
DDN失败后可达订阅/上报
3GPP内的NF向AMF订阅UE的DDN失败后可达事件（AVAILABILITY_AFTER_DDN_FAILURE）。如果是单次订阅，AMF在识别出UE在DDN失败后再次可达时，上报一次事件和UE ID。如果是持续订阅，AMF检测到UE在DDN失败后再次可达时，就上报一次事件和UE ID，直到到达截止时间或最大报告次数，AMF停止订阅检测和上报。
去订阅流程
图5  去订阅流程

NF Service Consumer如果要取消一个订阅，应发送DELETE请求，取消一个AMF已存在的订阅事件。 
根据不同处理情况： 
AMF根据subscription ID查找到已订阅的事件，删除该订阅，返回状态码204，指示去订阅成功。 
如果AMF处理失败，则返回4xx/5xx并携带失败原因。 
系统影响 :可能会存在3GPP NF集中向AMF订阅某区域内的多个终端的位置信息，对AMF网元系统性能影响较大。 
为了避免对现网网元的冲击，AMF要启动CPU过负荷控制。 
应用限制 :该特性基本功能基于3GPP R15 2018年12月份版本实现，与AMF对接的周边网元支持内部事件暴露时需要对齐到该协议版本。DDN失败后可达事件，是基于3GPP R16 2020年12月份版本实现。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.502: "Procedures for the 5G System"|4.15.4 Core Network Internal Event Exposure
3GPP TS 29.518: “Access and Mobility Management Services”|5.3 Namf_EventExposure Service6.2 Namf_EventExposure Service API
特性能力 :对于DDN失败后可达事件的订阅，每个用户最多可订阅3个此类型事件。
其他不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.20.40|新增时区/通信故障/连接丢失/区域内用户数量/DDN失败后可达等事件的订阅和上报。
01|V7.19.10|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :UDM|SMF|PCF|
---|---|---|---
√|√|√|
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :5G通用组网和服务化架构，无特殊要求。 
O&M相关 :命令 :配置项|命令
---|---
订阅授权控制策略配置|SHOW SUBSCRIBERAUTHPOLICY
SET SUBSCRIBERAUTHPOLICY|订阅授权控制策略配置
配置项|命令
---|---
基于NF实例号的订阅授权配置|ADD AUTHINFOBASENFINS
SET AUTHINFOBASENFINS|基于NF实例号的订阅授权配置
DEL AUTHINFOBASENFINS|基于NF实例号的订阅授权配置
SHOW AUTHINFOBASENFINS|基于NF实例号的订阅授权配置
配置项|命令
---|---
基于用户号段的订阅授权配置|ADD AUTHINFOBASEUE
DEL AUTHINFOBASEUE|基于用户号段的订阅授权配置
SET AUTHINFOBASEUE|基于用户号段的订阅授权配置
SHOW AUTHINFOBASEUE|基于用户号段的订阅授权配置
配置项|命令
---|---
PRA控制策略配置|SET PRAPOLICY
SHOW PRAPOLICY|PRA控制策略配置
跟踪区模板配置|ADD PRATAPROFILE
DEL PRATAPROFILE|跟踪区模板配置
SHOW PRATAPROFILE|跟踪区模板配置
NG-RAN CGI模板配置|ADD PRANCGIPROFILE
DEL PRANCGIPROFILE|NG-RAN CGI模板配置
SHOW PRANCGIPROFILE|NG-RAN CGI模板配置
gNodeB模板配置|ADD PRAGNBPROFILE
DEL PRAGNBPROFILE|gNodeB模板配置
SHOW PRAGNBPROFILE|gNodeB模板配置
PRA关联配置|ADD PRAASSOC
SET PRAASSOC|PRA关联配置
DEL PRAASSOC|PRA关联配置
SHOW PRAASSOC|PRA关联配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :订阅授权控制策略配置本配置用于设置AMF是否支持对其他前来订阅移动性事件的NF做授权检查，及其授权检查的具体策略。 针对可达性订阅事件，如果UDM等未做授权，AMF可开启授权功能。开启之后，只有在授权范围之内的NF，针对授权的用户才能订阅可达事件。 
基于NF实例号的订阅授权配置本命令用于增加基于NF的订阅授权信息。即当前其他NF向AMF订阅用户的某些移动性事件时，需要基于本配置进行授权检查，检查该NF对于所请求的移动性事件，是否在授权范围内。当需要开启基于NFID的订阅授权功能时，需要添加此配置。 
基于用户号段的订阅授权配置本命令用于增加基于UE标识的订阅授权信息。即其他NF向AMF订阅关于某些特定用户的特定移动性事件，需要经过基于本配置的授权检查。当需要开启基于NFID的订阅授权功能时，需要添加此配置。 
AOI事件类型相关的配置当AMF支持AOI功能时，需要配置AOI相关内容，包括AOI订阅功能等。 
配置前提 :UE、AMF等其他的设备、网元等服务工作正常。 
AMF网管服务器、客户端连接正常；服务器与EE连接正常。 
EE服务已经配置好相关的本地配置。 
EE服务相关的License开关已打开。 
配置过程 :订阅授权控制策略配置 
设置AMF支持对其他NF订阅用户移动性事件的授权功能，其中针对可达性通知事件策略为基于订阅NF标识和号段。 
[SET SUBSCRIBERAUTHPOLICY]:UEREACHABILITYNOTIFY="BASE_NFINS_AND_UEID"
基于NF实例号的订阅授权配置 
新增配置：NF实例标识为"c4b04e7d-44c0-4941-b981-00b7e288c4b4"，不允许订阅用户的可达性通知事件。ADD AUTHINFOBASENFINS:NFINSTANCEID="c4b04e7d-44c0-4941-b981-00b7e288c4b4",UEREACHABILITYNOTIFY="NOTALLOWED" 
删除标识为"c4b04e7d-44c0-4941-b981-00b7e288c4b4"的NF的订阅授权信息。DEL AUTHINFOBASENFINS:NFINSTANCEID="c4b04e7d-44c0-4941-b981-00b7e288c4b4" 
基于用户号段的订阅授权配置 
新增基于号段的订阅授权检查信息，对于"4600100001"号段的用户，其他NF订阅其用户可达事件“UEREACHABILITYNOTIFY”是不允许的。ADD AUTHINFOBASEUE:SUPISEGMENT="4600100001",UEREACHABILITYNOTIFY="NOTALLOWED" 
删除对于"4600100001"号段的授权检查。DEL AUTHINFOBASEUE:SUPISEGMENT="4600100001" 
AOI事件类型的订阅配置 
执行[SET PRAPOLICY]命令，配置支持PRA订阅功能，决定是否基于CPU控制PRA状态报告以及是否在PRA变更时触发Location Reportong Control消息。
执行[ADD PRATAPROFILE]命令，根据数据规划配置核心网预定义的PRA区域所需要的跟踪区模板。
执行[ADD PRANCGIPROFILE]命令，根据数据规划配置核心网预定义的PRA区域所需要的NG-RAN CGI模板。
执行[ADD PRAGNBPROFILE]命令，根据数据规划配置核心网预定义的PRA区域所需要的gNodeB模板。
执行[ADD PRAASSOC]命令，根据数据规划将已配置好的模板关联到核心网预定义的PRA标识上。当基于CPU控制部分PRA状态报告的开关打开时，决定是否将本PRA纳入控制范围。
配置实例 :场景说明 :AMF是否支持对其他前来订阅移动性事件的NF做授权检查，及其授权检查的具体策略。 针对可达性订阅事件，如果UDM等需要授权，AMF可开启授权功能。开启之后，只有在授权范围之内的NF，针对授权的用户才能订阅可达事件。 
基于NF的订阅授权信息。即当前其他NF向AMF订阅用户的某些移动性事件时，需要基于本配置进行授权检查，检查该NF对于所请求的移动性事件，是否在授权范围内。当需要开启基于NFID的订阅授权功能时，需要添加此配置。 
基于UE标识的订阅授权信息。即其他NF向AMF订阅关于某些特定用户的特定移动性事件，需要经过基于本配置的授权检查。当需要开启基于NFID的订阅授权功能时，需要添加此配置。 
某企业为本单位员工提供更高质量的网络，需要根据员工当前的位置信息来判断用户是否在企业网覆盖范围内。同时订阅方与AMF已协商，使用核心网预定义的PRA配置。 
数据规划 :配置|参数|取值
---|---|---
订阅授权控制策略配置|可达事件通知|基于NF实例号控制
基于NF实例号的订阅授权配置|NF实例标识|c4b04e7d-44c0-4941-b981-00b7e288c4b4
UE可达事件通知|基于NF实例号的订阅授权配置|不允许订阅
基于用户号段的订阅授权配置|SUPI号段|4600100001
可达上报|基于用户号段的订阅授权配置|不允许订阅
PRA控制策略配置|是否支持PRA功能|支持PRA功能
禁止部分PRA状态报告CPU门限(%)|PRA控制策略配置|60
禁止全部PRA状态报告CPU门限(%)|PRA控制策略配置|80
跟踪区模板配置|模板标识|1
移动国家码|跟踪区模板配置|460
移动网络码|跟踪区模板配置|11
跟踪区码|跟踪区模板配置|000000
跟踪区码起始|跟踪区模板配置|074FD1
跟踪区码终止|跟踪区模板配置|074FD5
NG-RAN CGI模板配置|模板标识|1
移动国家码|NG-RAN CGI模板配置|460
移动网络码|NG-RAN CGI模板配置|11
Cell标识|NG-RAN CGI模板配置|00012AB01、000000000
Cell标识起始|NG-RAN CGI模板配置|000000000、00012AB03
Cell标识终止|NG-RAN CGI模板配置|000000000、00012AB07
gNodeB模板配置|模板标识|1
移动国家码|gNodeB模板配置|460
移动网络码|gNodeB模板配置|11
gNB比特长度|gNodeB模板配置|28
gNB标识|gNodeB模板配置|211C501、211C503
gNB标识起始|gNodeB模板配置|000000
gNB标识终止|gNodeB模板配置|000000
PRA关联配置|PRA标识|8888888
跟踪区模板标识|PRA关联配置|1
NG-RAN CGI模板标识|PRA关联配置|1
gNodeB模板标识|PRA关联配置|1
是否支持状态报告控制|PRA关联配置|支持状态报告控制
配置步骤 :订阅授权控制策略配置，配置订阅授权控制策略参数，命令如下： 
[SET SUBSCRIBERAUTHPOLICY]:UEREACHABILITYNOTIFY="BASE_NFINS"
基于NF实例号的订阅授权配置，配置基于NF实例号的订阅授权参数，命令如下： 
[ADD AUTHINFOBASENFINS]:NFINSTANCEID="c4b04e7d-44c0-4941-b981-00b7e288c4b4",UEREACHABILITYNOTIFY="NOTALLOWED"
基于用户号段的订阅授权配置，配置基于用户号段的订阅授权配置参数，命令如下： 
[ADD AUTHINFOBASEUE]:SUPISEGMENT="4600100001",UEREACHABILITYNOTIFY="NOTALLOWED"
订阅AOI事件类型相关的配置，命令如下： 
序号|步骤|操作
---|---|---
1|修改PRA控制策略配置信息。为避免过多的PRA订阅对系统造成较大的负荷，规定CPU占用率到达80%时禁止所有PRA的状态报告，CPU占用率达到60%时禁止企业网对应PRA的状态报告。|SET PRAPOLICY:PRASWITCH="SUPPORT",PARTTHRESHOLD=60,ALLTHRESHOLD=80
2|新增跟踪区模板配置。企业网占用5个跟踪区，PLMN为460-11，跟踪区码为074FD1到074FD5。|ADD PRATAPROFILE:PROFILEID=1,MCC="460",MNC="11",TAC="000000",TACST="074FD1",TACEND="074FD5"
3|新增NG-RAN CGI模板配置。企业网占用6个NG-RAN CGI，PLMN为460-11，CELL标识为00012AB01以及00012AB03到00012AB07。|ADD PRANCGIPROFILE:PROFILEID=1,MCC="460",MNC="11",CELL="00012AB01",CELLST="000000000",CELLEND="000000000"ADD PRANCGIPROFILE:PROFILEID=1,MCC="460",MNC="11",CELL="000000000",CELLST="00012AB03",CELLEND="00012AB07"
4|新增gNodeB模板配置。企业网占用2个gNodeB，PLMN为460-11， gNB标识为211C501和211C503，对应比特长度为28位。|ADD PRAGNBPROFILE:PROFILEID=1,MCC="460",MNC="11",BITLEN=28,GNBID="211C501",GNBIDST="000000",GNBIDEND="000000"ADD PRAGNBPROFILE:PROFILEID=1,MCC="460",MNC="11",BITLEN=28,GNBID="211C503",GNBIDST="000000",GNBIDEND="000000"
5|新增PRA关联配置。企业网规划使用8888888的核心网预定义PRA标识。|ADD PRAASSOC:PRAID=8888888,TAPROFILEID=1,NCGIPROFILEID=1,GNBPROFILEID=1,REPORTCTRLSWITCH="SUPPORT"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|基于NF的订阅授权控制
---|---
测试目的|验证基于NF的订阅授权控制功能
预置条件|5G网络内的所有网元运行正常，EM维护正常。用户签约5G业务。打开消息跟踪。订阅授权控制开关打开，配置基于NF的授权，被授权的NF在白名单上
测试过程|用户发起订阅流程。用户注册，用户状态活动，amf发起事件通知过程。
通过准则|订阅授权开关打开能够，订阅事件能够正常的被订阅。信令跟踪能够跟踪的相应的消息，同时流程正常。
测试结果|–
测试项目|基于用户的订阅授权控制
---|---
测试目的|验证基于用户的订阅授权控制功能
预置条件|5G网络内的所有网元运行正常，EM维护正常。用户签约5G业务。打开消息跟踪。订阅授权控制开关打开，同时配置基于用户的授权。用imsi号段匹配用户。
测试过程|用户发起订阅流程。用户注册，用户状态活动，amf发起事件通知过程。
通过准则|订阅授权开关打开能够，订阅事件能够正常的被订阅。信令跟踪能够跟踪的相应的消息，同时流程正常。
测试结果|–
测试项目|AMF能够根据配置的PRA区域判断用户是否在该区域内
---|---
测试目的|验证AMF可以判断用户的PRA状态，并传递给订阅方。
预置条件|5G网络中各NF系统及操作维护台运行正常。用户在UDM中已签约5G业务。在AMF上建立用户信令跟踪。其他NF向AMF订阅PRA功能，本地配置PRA区域。订阅方设置核心网预定义PRA类型。
测试过程|UE在5G网络发起注册流程。
通过准则|UE注册成功。AMF在订阅请求消息中收到PRA ID，在Location Report Control消息中通知RAN，根据订阅方携带的callbackurl，通过Event Notify消息通知订阅方。信令跟踪能够跟踪到相应的消息，同时流程正常。
测试结果|–
常见问题处理 :无。 
## ZUF-79-15-002 NEF事件暴露 
本特性与ZUF-79-15-001 内部事件暴露
特性在功能上一致，属于不同的应用场景，具体内容参见ZUF-79-15-001 内部事件暴露
。
# ZUF-79-16 位置相关业务 
## ZUF-79-16-001 UE位置变化业务 
特性描述 :特性描述 :术语 :术语|含义
---|---
UPF服务区域|UPF服务区域是由一组跟踪区组成，代表了UPF所能提供服务的范围。当UE移出UPF服务区域时，SMF重新选择UPF。
LADN|LADN是指服务于特定区域的本地接入数据网络，可应用于会展、商场、企业等内部数据网络的访问接入。一般每个LADN网络，均存在与之关联的特定DNN，用于激活到该数据网络的PDU会话连接时，选择SMF和UPF。
描述 :定义 :UE位置变化通知是指用户进入或者移出特定区域时，例如UPF服务区域、LADN区域等，系统能够感知用户发生位置变化并执行不同的处理。
背景知识 :无论是从UPF自身能力考虑，还是从运营商规划部署考虑，或是从业务时延考虑，每个UPF的服务区域仅限于某些特定区域。当UE移出UPF的服务区域时，系统需要感知用户这种位置变化，以便重新选择UPF，从而保证业务的连续性。
对于LADN业务，类似UPF仅服务于特定区域，本地数据网络也有覆盖范围，当UE移出覆盖范围时，系统需要感知UE发生位置变化，从而禁止UE数据业务；同时，当UE进入覆盖范围时，系统同样需要感知UE发生位置变化，从而恢复UE数据业务。
对于某些特定用户，通过签约或者配置一些特定区域，以便当UE进入或者移出这些区域时，系统感知UE发生位置变化，从而提供不同的费率或者策略控制。 
引入本特性后，当UE进入或者移出UPF服务区域、LADN区域，以及某些签约或者配置的特定区域时，uMAC能够感知UE发生位置变化，触发相应的处理。 
应用场景 :本特性适用如下应用场景： 
UPF按区域提供数据业务服务。 
服务于特定区域本地数据网络的业务控制。 
客户收益 :受益方|受益描述
---|---
运营商|提供差异化服务：针对某些特定用户签约特定区域，执行不同的费率计费和策略控制。保证用户体验：为用户提供持续的移动性数据业务，避免用户投诉，提高网络服务质量。
终端用户|该特性对于终端用户不可见。

实现原理 :


系统架构 :



本特性涉及的系统架构如[图1]所示。


图1  系统架构






涉及的NF/网元参见下表。 


NF/网元|说明
---|---
NF|UPF|为所服务区域下的UE提供用户面报文的转发和路由，所服务区域覆盖范围的大小取决于网络规划。
NF|SMF|负责向AMF移动事件通知的订阅、更新以及去订阅；当收到AMF订阅通知，指示UE移出Area of Interest时，调用UPF选择功能重新选择UPF。
NF|AMF|处理SMF移动事件通知的订阅、更新以及去订阅；通知(R)AN启动或者取消位置报告；收到(R)AN位置报告时，发送订阅通知给SMF。
网元|(R)AN|当检测到UE移出或者进入Area of Interest时，上报位置报告给AMF，携带UE presence in Areaof Interest。
网元|UE|位置变化时，通知(R)AN或AMF。




业务流程 :UE位置变化通知的流程如[图2]所示。
图2  UE位置变化通知的流程图

流程说明如下： 
PDU会话激活后，SMF发送Namf_EventExposure_Subscribe Request消息给AMF，订阅移动事件通知，消息中携带基于UPF服务区域生成的Area
of Interest。 
AMF创建订阅上下文，并回复Namf_EventExposure_Subscribe Response消息给SMF。 
AMF下发Location Reporting Control消息给(R)AN，携带Area of Interest。 
(R)AN回复Location Report消息给AMF，携带UE Presence in Area of Interest和UE位置信息。 
当(R)AN检测到UE presence in Area of Interest发生变化，则上报Location Report消息给AMF，携带最新的UE
presence in Area of Inerest和UE位置信息。 
AMF发送Namf _EventExposure_Notify消息给SMF，携带(R)AN上报的UE Presence
in Area of Interest和UE位置信息。 
SMF收到AMF订阅通知后，若消息中的UE presence in Area of Interest为OUT，则表示UE已经移出Area
of Interest，则调用UPF选择功能，触发UPF重选。 
重新选择UPF后，SMF发送Namf_EventExposure_Subscribe Request消息给AMF，更新步骤1中订阅的移动事件通知，消息中携带基于新选择的UPF服务区域生成的Area
of Interest。 
AMF更新订阅上下文，并回复Namf_EventExposure_Subscribe Response消息给SMF。 
收到移动事件通知更新消息，或者新的N2连接建立后，AMF下发Location Reporting Control消息给(R)AN，携带Area
of Interest。 
(R)AN回复Location Report消息给AMF。 
PDU会话释放后，SMF发送Namf_EventExposure_Unsubscribe Request消息给AMF，取消步骤1中订阅的移动事件通知。 
AMF删除对应的订阅上下文，并回复发送Namf_EventExposure_Unsubscribe Response消息。 
AMF发送Location Reporting Control消息给(R)AN，通知(R)AN停止位置上报。 


NF实现 :



AMF实现 :####### SMF实现 
在本特性中，AMF承担如下职责： 

 
处理SMF发起的移动事件通知订阅、更新以及去订阅，并发送Location Reporting Control给(R)AN，通知(R)AN启动位置上报，或者取消位置上报。 

 
当与(R)AN建立新的N2连接，如切换或者业务请求流程成功后，下发Location Reporting Control给(R)AN。 

 
收到(R)AN上报的Location Report后，发送订阅通知给SMF。 

 


在本特性中，SMF承担如下职责： 

 
激活PDU会话后，向AMF订阅移动事件通知，携带基于UPF服务区域生成的Area of Interest。 

 
UPF重选后，向AMF更新移动事件通知，携带基于新选择UPF服务区域生成的Area of Interest。 

 
收到AMF订阅通知后，若通知指示UE已经移出Area of Interest，则调用UPF选择功能，重新选择UPF。 

 
释放PDU会话后，通知AMF去订阅移动事件通知。 

 




协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
系统影响 :开启该特性，核心网侧向基站订阅UE小区位置变化信息，变化了则进行上报。该特性会影响核心网性能。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 


遵循标准 :



类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP|3GPP TS 23.502|Procedures for the 5G System
3GPP|3GPP TS 29.500|Technical Realization of Service Based Architecture
3GPP|3GPP TS 29.518|Access and Mobility Management Services
3GPP|3GPP TS 38.413|NGApplication Protocol (NGAP)




特性能力 :本特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNB/ng-eNB
---|---
-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :该特性对于工程规划无特殊要求。 

O&M相关 :


配置命令 :



####### AMF配置命令 
本特性不涉及AMF配置命令的变化 


####### SMF配置命令 
本特性不涉及SMF配置命令的变化 






定时器 :



####### AMF定时器 
本特性不涉及AMF定时器的变化 


####### SMF定时器 
本特性不涉及SMF定时器的变化 




性能统计 :####### AMF性能统计 
序号|性能计数器名称
---|---
1|C510510049 发送LOCATION REPORTING CONTROL次数
2|C510510050 收到LOCATION REPORTING FAILURE INDICATION次数
3|C510510051 收到LOCATION REPORT次数
####### SMF性能统计 
该特性不涉及SMF计数器的变化。 


告警和通知 :



####### AMF告警和通知 
该特性不涉及AMF告警/通知消息的变化。 


####### SMF告警和通知 
该特性不涉及SMF告警/通知消息的变化。 






话单与计费 :



该特性不涉及话单与计费的变化。 




特性配置 :特性配置 :

配置说明 :



该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现UE位置变化通知流程。 






测试用例 :



测试项目|UE位置变更通知
---|---
测试目的|AMF能够向订阅者传送用户的位置信息
预置条件|RAN和AMF都支持UE位置变更通知。AMF和SMF支持事件订阅。UE已成功注册到5GC。
测试过程|UE发起PDU会话创建。UE从当前区域移动到新的区域。
通过准则|会话创建成功后，SMF向AMF发起Namf_EventExposure_Subscribe Request，订阅用户位置变更事件，消息中携带Areaof Interest。AMF回复SMFNamf_EventExposure_Subscribe Response，并且向RAN发送Locationreport Control。RAN检测到UE位置变化，上报Location report携带位置信息和UE Presence in Area ofInterest。AMF发送Namf _EventExposure_Notify消息给SMF，携带RAN上报的UE Presence inArea of Interest和UE位置信息。
测试结果|-




常见问题处理 :无。 
## ZUF-79-16-002 LADN 
特性描述 :特性描述 :术语 :术语|含义
---|---
DNN|DNN是5G系统定义的网络标识，标识了5G核心网所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入等）。
LADN DNN|LADN DNN是一类特殊的DNN，UE通过该DNN指示所需要访问的LADN网络。
LADN服务区域|LADN服务区域是由一组跟踪区组成，代表了LADN网络服务的范围。当UE进入该区域后，才能访问该LADN网络；当UE离开该区域后，禁止UE访问该LADN网络。
LADN信息|LADN信息是由一组LADN服务区域及LADN DNN组成，UE注册过程中由AMF生成并在注册接受消息中携带给UE。
描述 :定义 :LADN是指服务于特定区域的数据网络，可应用于会展、商场、企业等场所的本地数据网络访问。每个LADN网络可关联一个特殊的DNN，用于选择连接LADN网络的网关。 
背景知识 :从覆盖区域上来看，本地数据网络一般仅覆盖特定区域，只有UE处于该特定区域时，才能访问本地数据网络。从服务的可用性来看，UE需要感知可用的本地数据网络信息，以便当UE进入本地数据网络覆盖区域时，触发UE访问本地数据业务。此外，UE访问会展、商场、企业等场所的本地数据网络时，无论是计费策略还是控制策略，与UE访问普通的数据网络存在非常大的区别。 
通过支持LADN，从而使核心网和UE能够支持本地数据网络的上述需求：UE进入本地数据网络覆盖区域后可以访问本地数据网络，并采用特定的计费策略和控制策略，保证本地数据业务正常开展。 
应用场景 :本特性可以应用于以下场景： 
跨区域企业内部网络接入：对于大型企业而言，各个组织职能机构通常分布于不同的区域，企业需要保证员工可以在不同办公区域，随时访问内部数据网络。 
博物馆：用户进入博物馆时，能够访问博物馆内部网站，浏览博物馆相关信息。  
客户收益 :受益方|受益描述
---|---
运营商|提升经营业绩：拓展业务范围，满足市场对于本地数据网络的需求。保证用户体验：能够以较小的代价，如费率、时延等，访问本地数据网络。
移动用户|本特性对于终端用户不可见。
实现原理 :系统架构 :支持LADN的架构如[图1]所示。
图1  图1  支持LADN架构图

涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
AMF|接受SMF移动事件通知的订阅与去订阅，通知(R)AN启动或取消位置报告。在收到(R)AN位置报告后，发送订阅通知给SMF，指示UE当前是否进入或者移出LADN区域。
UDM|UE签约数据管理。
SMF|负责向AMF订阅或去订阅移动事件通知，处理AMF发送的订阅通知。
(R)AN|监控UE当前是否进入或者移出LADN区域，当UE位置状态发生变化时，上报位置报告给AMF。
UE|位置变化时通知(R)AN或AMF。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
本NF/网元实现 :在本特性中，AMF实现如下功能： 
注册流程中，通过Registration Accept消息，下发LADN信息给UE。 
LADN信息变更时，通过配置更新流程，下发变化后的LADN信息给UE。 
接受SMF移动事件通知的订阅、去订阅信息。 
下发Location Reporting Control给(R)AN，通知(R)AN启动或取消位置上报。 
当与(R)AN建立新的N2连接时，如业务请求、切换流程成功后，重新下发Location Reporting Control给(R)AN，启动位置上报。 
收到(R)AN的Location Report后，发送订阅通知给SMF。 
业务流程 :支持LADN业务流程如[图2]所示。
图2  支持LADN业务流程图

UE检测需要发起注册流程，发送Registration Request消息，经过(R)AN给AMF。 
AMF执行注册接受前的鉴权、PEI检查、向UDM请求签约数据等过程。 
AMF根据签约、本地配置，生成LADN信息，并在Registration Accept消息中带给UE。 
当处于LADN服务区域时，UE检测需要新建LADN PDU会话，则发起PDU会话激活流程。AMF向SMF发送Nsmf_PDUSession_CreateSMContext Request，携带参数presenceInLadn指示UE在LADN服务区域。 
LADN PDU会话激活后，SMF发送Namf_EventExposure_Subscribe Request，向AMF订阅移动事件通知，携带LADN DNN。 
AMF创建移动事件通知订阅上下文，并回复Namf_EventExposure_Subscribe Response消息给SMF。 
AMF根据步骤5订阅回复消息中的LADN DNN查询本地配置，生成Area of Interest，并在Location Reporting Control 消息中携带给(R)AN。 
(R)AN回复Location Report消息给MAF，携带UE Presence in Area of Interest和UE位置。 
当(R)AN检测到UE presence in Area of Interest发生变化，则上报Location Report消息给AMF，携带最新的UE presence in Area of Inerest和UE位置信息。 
AMF发送Namf _EventExposure_Notify消息给SMF，携带(R)AN上报的UE Presence in Area of Interest和UE位置信息。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.6.5
3GPP TS 23.502（Procedures for the 5G System）|4.2、4.3、4.9
3GPP TS 24.501（Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3）|5.5.1、5.4.4、6.2.6
3GPP TS 29.502（Session Management Services; Stage 3）|5.2.2
3GPP TS 29.503（Unified Data Management Services; Stage 3）|6.1.6.2.4
3GPP TS 29.518（5G System; Access and Mobility Management Services）|5.3、6.2.6.2.17
3GPP TS 38.413（NG Application Protoco(NGAP)）|8.12
特性能力 :名称|指标
---|---
AMF支持LADN区域配置的最大个数|4096（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布。
License要求 :该特性为ZXUN UMAC的基本特性，无需License支持。 
对其他网元的要求 :UE|NR|UDM|SMF
---|---|---|---
√|√|√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
AMF局域数据网配置|ADD AMFLADN
SET AMFLADN|AMF局域数据网配置
DEL AMFLADN|AMF局域数据网配置
SHOW AMFLADN|AMF局域数据网配置
LADN跟踪区标识列表配置|ADD AMFLADN TAIDLIST
DEL AMFLADN TAIDLIST|LADN跟踪区标识列表配置
SHOW AMFLADN TAIDLIST|LADN跟踪区标识列表配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :        LADN（局域数据网）是由服务PLMN提供的一项功能。LADN服务区域是一组跟踪区， 用户通过PDU会话接入数据网络，仅在特定的LADN服务区中可用。UE在注册（Registration）过程或者UE配置更新过程中，AMF向UE提供LADN信息（即LADN服务区域和LADN DNN）。AMF下发的LADN列表，需要依据UE注册请求消息中携带的LADN指示、AMF本地配置（经由OAM）以及用户的DNN签约信息几方面来确定： 
UE注册请求既没有提供LADN DNN也没有提供请求LADN信息的指示 
则LADN信息的DNN列表，是用户签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
UE注册请求提供了请求LADN信息的指示但未提供LADN DNN 
此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定：如果UE的签约了通配DNN(wildcard *)并且通配DNN为LADN DNN，LADN信息中的DNN列表，是AMF配置的 LADN DNN；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN或者签约了通配DNN但非LADN DNN，LADN信息的LADN DNN列表，是签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
UE注册请求提供了请求LADN信息的指示及LADN DNN 
此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定：如果UE的签约了通配DNN并且通配DNN为LADN DNN，LADN信息中的DNN列表，是ladn Indication 的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN或者签约了通配DNN但非LADN DNN，LADN信息的LADN DNN列表，是ladn Indication指示的、签约DNN中的LADN DNN及AMF配置的LADN DNN三者的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 

用户在注册（Registration）过程中，AMF需要按前述规则确定LADN Information，将最多不超过8个Ladn Information通过注册接受消息中带给UE。另外，当网络侧UE的LADN DNN信息改变时，AMF也可以通过UE配置更新过程(即在configuration update command消息中携带新的LADN Information给UE)更新LADN信息。 
配置前提 :完成AMF基本注册功能的数据配置。 
Namf_Communication服务的 “接入区域配置”已经有合理的注册区域配置及与注册区域对应的TA配置，接入区域列表分配策略也已经设置完成。 
UDM的AMF签约信息中，UE已经签约了一个或多个 DNN（subscribedDnnLIst个数非零)。 
配置过程 :执行[ADD AMFLADN]命令，增加LADN标识及对应的DNN。
执行[ADD AMFLADN TAIDLIST]命令，为步骤1中配置的LADN ID配置关联的TA。
其中，TAID必须引用自接入区域配置→TA配置
(配置前提2)中已经配置完成的TA的TAID。每个LADNID可以关联1-16个TAID，视实际需求而定，即最多需要执行16次增加命令。
配置实例 :场景说明 :增加两个LADN配置，并为配置的LADN ID配置关联的TA。  
AMF增加两个LADN配置,LADN ID分别为1和2，对应的LADN DNN 分别为“zte.com”和“zte.com.cn”； 
LADN ID-1 对应的TA列表为：460-11-100000, 460-02-100002, 460-11-100005, 460-01-100009；LADN ID-2对应的TA列表为：460-11-100000, 460-11-100001, 460-11-100005, 460-02-100007。 
数据规划 :配置项|参数名称|取值
---|---|---
AMF局域数据网配置|LADNID|1|2
LADNDNN|AMF局域数据网配置|zte.com|zte.com.cn
LADN跟踪区标识列表配置|LADNID|1|2
TAID|LADN跟踪区标识列表配置|1000&1002&1005&1009|1000&1001&1005&1007
配置步骤 :步骤|说明|操作
---|---|---
1|增加LADN配置|ADD AMFLADN:LADNID=1,LADNDNN="zte.com"ADD AMFLADN:LADNID=2,LADNDNN="zte.com.cn"
2|配置关联的TA|ADD AMFLADN TAIDLIST:LADNID=1,TAID=1000ADD AMFLADN TAIDLIST:LADNID=1,TAID=1002ADD AMFLADN TAIDLIST:LADNID=1,TAID=1005ADD AMFLADN TAIDLIST:LADNID=1,TAID=1009ADD AMFLADN TAIDLIST:LADNID=2,TAID=1000ADD AMFLADN TAIDLIST:LADNID=2,TAID=1001ADD AMFLADN TAIDLIST:LADNID=2,TAID=1005ADD AMFLADN TAIDLIST:LADNID=2,TAID=1007
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF在注册接受中下发LADN Information
---|---
测试目的|UE注册请求不带Ladn Indication，验证AMF在注册接受下发正确的LADN Information
预置条件|AMF已经有支持UE基本注册流程的配置数据UE在UDM上的AMF签约数据“subscribedDnnList“中，签约了4个Dnn，分别为”*“(通配符)，”zte.com“，”zte.com.cn“，”zzz.com“AMF在OAM上已经完成“配置实例”章节所述的注册区域、TA、注册区域与TAID关联、LADN等相关配置
测试过程|UE发起初始UE注册，初始消息中当前TA为460-11-100000，注册请求不携带LADN Indication
通过准则|注册成功注册接受消息下发的跟踪区列表为：460-11-10000, 460-11-100001, 460-02-100002,460-11-100005；460-02-100007注册接受携带LADN InformationDNN:"zte.com",TaiList: 460-11-10000, 460-02-100002,460-11-100005DNN:"zte.com",TaiList: 460-11-10000, 460-11-100001, 460-11-100005；460-02-100007UE注册请求没有提供请求LADN信息的指示。则LADN信息的DNN列表，是用户签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集。如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。
测试结果|–
测试项目|AMF在注册接受中下发LADN Information
---|---
测试目的|UE 注册请求带Ladn Indication，但Dnn个数为0，验证AMF在注册接受下发正确的LADN Information
预置条件|AMF已经有支持UE基本注册流程的配置数据UE在UDM上的AMF签约数据“subscribedDnnList“中，签约了4个Dnn，分别为”*“(通配符)，”zte.com“，”zte.com.cn“，”zzz.com“AMF在OAM上已经完成“配置实例”章节所述的注册区域、TA、注册区域与TAID关联、LADN等相关配置
测试过程|UE发起初始UE注册，初始消息中当前TA为460-11-100000，注册请求携带LADN Indication，但dnn个数为0；
通过准则|注册成功注册接受消息下发的跟踪区列表为：460-11-10000, 460-11-100001, 460-02-100002,460-11-100005；460-02-100007注册接受携带LADN InformationDNN:"zte.com",TaiList: 460-11-10000, 460-02-100002,460-11-100005DNN:"zte.com",TaiList: 460-11-10000, 460-11-100001, 460-11-100005；460-02-100007UE注册请求提供了请求LADN信息的指示但未提供LADN DNN。此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定。如果UE的签约了通配DNN(wildcard *)，LADN信息中的DNN列表，是AMF配置的 LADN DNN；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN，LADN信息的LADN DNN列表，是签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。
测试结果|–
常见问题处理 :无。 
## ZUF-79-16-003 PRA 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :PRA在PCF上进行区域监视，能感知UE进入或离开指定区域，并通知AMF和无线基站，以便在指定区域进行话务控制和拦截。 
当UE在监控区域活动时，无线向AMF上报事件，AMF向PCF上报事件。 
背景知识 :在5G网络中位置标识一般用作基于位置提供的不同服务与计费策略。 
位置标识来源于无线规划，AMF从无线获得位置标识后可传递给其他网元。PCF基于位置标识提供服务策略，计费中心基于位置标识提供计费策略。 
应用场景 :基于位置标识组网络提供计费和服务，可以分为基于实时位置标识组计费和基于位置标识组提供服务策略两种场景。 
###### 基于实时位置标识组计费：PRA+小区位置上报 
场景特点
系统基于用户进入或离开某位置标识组进行计费，由于涉及用户资费，对用户位置的实时性和精度均要求高，以免发生误判。 
具体的场景比如校园网：校园网由一组位置标识组成，用户进入或离开校园网范围时，采用不同的计费策略。 
解决方案
PCF下发位置标识组到AMF，AMF请求无线判断用户是否离开或进入此区域然后上报用户的位置变化情况，并将结果上报给AMF，AMF传递给PCC计费系统。 
###### 基于位置标识组提供服务策略：PRA 
场景特点
系统基于用户进入或离开某位置标识组进行服务策略。 
具体的场景比如企业网：企业网由一组位置标识组成，用户进入或离开企业网范围时，采用不同的服务策略。 
解决方案
PCF下发位置标识组到AMF，AMF请求无线判断用户是否离开或进入此区域然后上报用户的位置变化情况，并将结果上报给AMF，AMF传递给服务策略系统。 
客户收益 :受益方|受益描述
---|---
运营商|提高策略灵活性：基于用户位置标识为用户提供灵活的服务与计费策略。丰富业务功能： 为用户提供定位能力，便于紧急呼叫时救援，以及方便开展各种与位置相关的增值服务。
移动用户|提高终端用户体验。用户在某些区域可获得更优费率或更好的服务质量，同时可获得终端定位能力，可使用各种与位置相关的增值服务。
实现原理 :系统架构 :PRA功能在现有的网络架构中叠加相应功能，不涉及网络结构的变化。 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
RAN|负责接收AMF的PRA的布控信息。当UE的位置发生变化时，判断其是否发生了PRA区域的变化，对于发生变化的区域需要通知给AMF。
AMF|负责接收SMF等网元的PRA的布控信息。负责把PRA的信息发给给RAN。负责接收RAN的PRA判断结果以及自身根据位置信息来判断PRA的区域变化状态，如果PRA的状态发送变化（IN/OUT/UNKNOWN之间发生变化），则把PRA的新状态信息发给布控的网元。
SMF|负责接收PCF的PRA的布控信息。负责把PRA的布控信息传递给AMF。负责接收AMF的PRA的决策结果并传递给PCF。
协议栈 :PRA功能不涉及新增协议栈。 
本NF/网元实现 :AMF的主要功能包括： 
AMF接收并保存SMF/PCF等网元的PRA布控信息，包括PRA ID和PRA区域信息（如果是UE专属模式）。 

AMF把PRA布控信息发给无线，供无线判断UE进入或者离开区域。 
AMF把无线上报的PRA的结果发送给SMF/PCF等网元。 
业务流程 :PCF通过SMF订阅PRA位置的流程如[图1]所示。
图1  PCF通过SMF订阅PRA位置流程

具体说明如下。 
PCF发消息给SMF订阅PRA业务，消息中包括PRA ID和PRA的区域信息（如果是UE专属的PRA）。 
SMF把PCF的订阅请求，发给AMF。 
 AMF收到SMF的PRA的订阅请求，在用户上线后通过Location Reporting Ctrl消息给gNodeB，包括PRA ID和PRA的区域信息。 
gNodeB判断用户区域满足PRA布控区域要求，上报给AMF UE进入或者离开布控区域。 
AMF把UE进入或者离开区域的结果发给SMF。 
SMF把信息发送给PCF。 
PCF订阅PRA位置的流程如[图2]所示。
图2  PCF订阅PRA位置流程

具体说明如下。 
PCF通过策略响应或者策略通发消息到AMF订阅PRA业务，消息中包括PRA ID和PRA的区域信息（如果是UE专属的PRA）。 
AMF收到PCF的PRA的订阅请求，在用户上线后通过Location Reporting Ctrl消息给gNodeB，包括PRA ID和PRA的区域信息。 
gNodeB判断用户区域满足PRA布控区域要求，上报给AMF UE进入或者离开布控区域。 
AMF把UE进入或者离开区域的结果发给PCF。 
系统影响 :当订阅PRA的用户过多时，该特性对系统的影响包括以下部分： 
AMF和RAN间，AMF和PCF/SMF间的信令增多。 
影响AMF的CPU。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :3GPP TS 23.501: " System Architecture for the 5G System; Stage 2". 
3GPP TS 38.413: "NG-RAN; NG Application Protocol (NGAP)" 
特性能力 :名称|指标
---|---
支持的PRA的布控信息|1024
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7|首次发布。
License要求 :该特性需要开启License，对应的License项目为“AMF支持PRA功能”
对其他网元的要求 :PRA功能涉及到的网元包括SMF、NR和PCF。 
SMF|NR|PCF
---|---|---
√|√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项配置项命令PRA控制策略配置SET PRAPOLICYSHOW PRAPOLICY跟踪区模板配置ADD PRATAPROFILEDEL PRATAPROFILESHOW PRATAPROFILENG-RAN CGI模板配置ADD PRANCGIPROFILEDEL PRANCGIPROFILESHOW PRANCGIPROFILEgNodeB模板配置ADD PRAGNBPROFILEDEL PRAGNBPROFILESHOW PRAGNBPROFILEPRA关联配置ADD PRAASSOCSET PRAASSOCDEL PRAASSOCSHOW PRAASSOC 
软件参数软件参数ID软件参数名称COMMU-140收到PRA订阅后是否立即上报EE-5是否支持立即上报AOI事件 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置过程可以完成PRA订阅和上报功能，达到在PCF上进行区域监视，感知UE进入或离开指定区域来提供不同服务和计费策略的目的。 
要实现PRA订阅和上报功能，需要申请“AMF支持PRA订阅功能”的License，同时需要AMF在“PRA控制策略配置”中配置支持PRA功能。 
配置前提 :AMF环境就绪，与周边NF间链路正常。 
全网已经规划好了核心网预定义的PRA区域。 
EM能正常连接并登录。 
配置过程 :执行[SET PRAPOLICY]命令，设置支持PRA订阅功能，决定是否基于CPU控制PRA状态报告以及是否在PRA变更时触发Location Reportong Control消息。
执行[ADD PRATAPROFILE]命令，根据数据规划配置核心网预定义PRA区域所需要的跟踪区模板。
执行[ADD PRANCGIPROFILE]命令，根据数据规划配置核心网预定义PRA区域所需要的NG-RAN CGI模板。
执行[ADD PRAGNBPROFILE]命令，根据数据规划配置核心网预定义PRA区域所需要的gNodeB模板。
执行[ADD PRAASSOC]命令，根据数据规划将已配置好的模板关联到核心网预定义的PRA标识上，基于CPU控制部分PRA状态报告打开时，决定是否将本PRA纳入控制范围。
执行[SET COMMU SOFTWARE PARAMETER]:ID=140命令，设置AMF收到SMF的PRA订阅后是否需要立即上报。
执行[SET EE SOFTWARE PARAMETER]:ID=5命令，设置AMF收到SMF的PRA订阅后是否需要立即上报。
配置实例 :场景说明 :某企业为本单位员工提供更高质量的网络，需要根据员工当前的位置信息来判断用户是否在企业网覆盖范围内。 
同时PCF与AMF已协商，使用核心网预定义的PRA配置，并且PCF直接向AMF订阅PRA信息。 
数据规划 :参数|示例
---|---
PRA控制策略配置|是否支持PRA功能|SUPPORT
禁止部分PRA状态报告CPU门限(%)|PRA控制策略配置|60
禁止全部PRA状态报告CPU门限(%)|PRA控制策略配置|60
是否支持Location Reporting Control消息|PRA控制策略配置|SUPPORT
跟踪区模板配置|模板标识|1
移动国家码|跟踪区模板配置|460
移动网络码|跟踪区模板配置|11
跟踪区码|跟踪区模板配置|000000（无效值，代表不配置单个跟踪区码）
跟踪区码起始|跟踪区模板配置|074FD1
跟踪区码终止|跟踪区模板配置|074FD5
NG-RAN CGI模板配置|模板标识|1
移动国家码|NG-RAN CGI模板配置|460
移动网络码|NG-RAN CGI模板配置|11
Cell标识|NG-RAN CGI模板配置|00012AB01、000000000（无效值，代表不配置单个Cell标识）
Cell标识起始|NG-RAN CGI模板配置|000000000（无效值，代表不配置Cell标识区段）、00012AB03
Cell标识终止|NG-RAN CGI模板配置|000000000（无效值，代表不配置Cell标识区段）、00012AB07
gNodeB模板配置|模板标识|1
移动国家码|gNodeB模板配置|460
移动网络码|gNodeB模板配置|11
gNB比特长度|gNodeB模板配置|28
gNB标识|gNodeB模板配置|211C501、211C503
gNB标识起始|gNodeB模板配置|000000（无效值，代表不配置gNB标识区段）
gNB标识终止|gNodeB模板配置|000000（无效值，代表不配置gNB标识区段）
PRA关联配置|PRA标识|8888888
跟踪区模板标识|PRA关联配置|1
NG-RAN CGI模板标识|PRA关联配置|1
gNodeB模板标识|PRA关联配置|1
是否支持状态报告控制|PRA关联配置|SUPPORT
设置软件参数|软参索引|140
当前参数值|设置软件参数|1
配置步骤 :序号|步骤|操作
---|---|---
1|修改PRA控制策略配置信息。为避免过多的PRA订阅对系统造成较大的负荷，规定CPU到达80时禁止所有PRA的状态报告，CPU达到60时禁止企业网对应PRA的状态报告。|SET PRAPOLICY:PRASWITCH="SUPPORT",PARTTHRESHOLD=60,ALLTHRESHOLD=80
2|新增跟踪区模板配置。企业网占用5个跟踪区，PLMN为460-11，跟踪区码为074FD1到074FD5。|ADD PRATAPROFILE:PROFILEID=1,MCC="460",MNC="11",TAC="000000",TACST="074FD1",TACEND="074FD5"
3|新增NG-RAN CGI模板配置。企业网占用6个NG-RAN CGI，PLMN为460-11，CELL标识为00012AB01以及00012AB03到00012AB07。|ADD PRANCGIPROFILE:PROFILEID=1,MCC="460",MNC="11",CELL="00012AB01",CELLST="000000000",CELLEND="000000000"ADD PRANCGIPROFILE:PROFILEID=1,MCC="460",MNC="11",CELL="000000000",CELLST="00012AB03",CELLEND="00012AB07"
4|新增gNodeB模板配置。企业网占用2个gNodeB，PLMN为460-11，GNB标识为211C501以及211C503，对应比特长度为28位。|ADD PRAGNBPROFILE:PROFILEID=1,MCC="460",MNC="11",BITLEN=28,GNBID="211C501",GNBIDST="000000",GNBIDEND="000000"ADD PRAGNBPROFILE:PROFILEID=1,MCC="460",MNC="11",BITLEN=28,GNBID="211C503",GNBIDST="000000",GNBIDEND="000000"
5|新增PRA关联配置。企业网规划使用8888888的核心网预定义PRA标识。|ADD PRAASSOC:PRAID=8888888,TAPROFILEID=1,NCGIPROFILEID=1,GNBPROFILEID=1,REPORTCTRLSWITCH="SUPPORT"
6|配置AMF收到PRA订阅后立即上报。|SET COMMU SOFTWARE PARAMETER:ID=140,VALUE=1
场景说明 :某企业为本单位员工提供更高质量的网络，需要根据员工当前的位置信息来判断用户是否在企业网覆盖范围内。 
同时SMF与AMF已协商，使用核心网预定义的PRA配置，并且SMF直接向AMF订阅PRA信息。 
数据规划 :参数|示例
---|---
PRA控制策略配置|是否支持PRA功能|SUPPORT
禁止部分PRA状态报告CPU门限(%)|PRA控制策略配置|60
禁止全部PRA状态报告CPU门限(%)|PRA控制策略配置|60
是否支持Location Reporting Control消息|PRA控制策略配置|SUPPORT
跟踪区模板配置|模板标识|1
移动国家码|跟踪区模板配置|460
移动网络码|跟踪区模板配置|11
跟踪区码|跟踪区模板配置|000000（无效值，代表不配置单个跟踪区码）
跟踪区码起始|跟踪区模板配置|074FD1
跟踪区码终止|跟踪区模板配置|074FD5
NG-RAN CGI模板配置|模板标识|1
移动国家码|NG-RAN CGI模板配置|460
移动网络码|NG-RAN CGI模板配置|11
Cell标识|NG-RAN CGI模板配置|00012AB01、000000000（无效值，代表不配置单个Cell标识）
Cell标识起始|NG-RAN CGI模板配置|000000000（无效值，代表不配置Cell标识区段）、00012AB03
Cell标识终止|NG-RAN CGI模板配置|000000000（无效值，代表不配置Cell标识区段）、00012AB07
gNodeB模板配置|模板标识|1
移动国家码|gNodeB模板配置|460
移动网络码|gNodeB模板配置|11
gNB比特长度|gNodeB模板配置|28
gNB标识|gNodeB模板配置|211C501、211C503
gNB标识起始|gNodeB模板配置|000000（无效值，代表不配置gNB标识区段）
gNB标识终止|gNodeB模板配置|000000（无效值，代表不配置gNB标识区段）
PRA关联配置|PRA标识|8888888
跟踪区模板标识|PRA关联配置|1
NG-RAN CGI模板标识|PRA关联配置|1
gNodeB模板标识|PRA关联配置|1
是否支持状态报告控制|PRA关联配置|SUPPORT
设置软件参数|软参索引|5
当前参数值|设置软件参数|1
配置步骤 :序号|步骤|操作
---|---|---
1|修改PRA控制策略配置信息。为避免过多的PRA订阅对系统造成较大的负荷，规定CPU到达80时禁止所有PRA的状态报告，CPU达到60时禁止企业网对应PRA的状态报告。|SET PRAPOLICY:PRASWITCH="SUPPORT",PARTTHRESHOLD=60,ALLTHRESHOLD=80
2|新增跟踪区模板配置。企业网占用5个跟踪区，PLMN为460-11，跟踪区码为074FD1到074FD5。|ADD PRATAPROFILE:PROFILEID=1,MCC="460",MNC="11",TAC="000000",TACST="074FD1",TACEND="074FD5"
3|新增NG-RAN CGI模板配置。企业网占用6个NG-RAN CGI，PLMN为460-11，CELL标识为00012AB01以及00012AB03到00012AB07。|ADD PRANCGIPROFILE:PROFILEID=1,MCC="460",MNC="11",CELL="00012AB01",CELLST="000000000",CELLEND="000000000"ADD PRANCGIPROFILE:PROFILEID=1,MCC="460",MNC="11",CELL="000000000",CELLST="00012AB03",CELLEND="00012AB07"
4|新增gNodeB模板配置。企业网占用2个gNodeB，PLMN为460-11，GNB标识为211C501以及211C503，对应比特长度为28位。|ADD PRAGNBPROFILE:PROFILEID=1,MCC="460",MNC="11",BITLEN=28,GNBID="211C501",GNBIDST="000000",GNBIDEND="000000"ADD PRAGNBPROFILE:PROFILEID=1,MCC="460",MNC="11",BITLEN=28,GNBID="211C503",GNBIDST="000000",GNBIDEND="000000"
5|新增PRA关联配置。企业网规划使用8888888的核心网预定义PRA标识。|ADD PRAASSOC:PRAID=8888888,TAPROFILEID=1,NCGIPROFILEID=1,GNBPROFILEID=1,REPORTCTRLSWITCH="SUPPORT"
6|配置AMF收到PRA订阅后立即上报。|SET EE SOFTWARE PARAMETER:ID=5,VALUE=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF能够根据配置的PRA区域进行PRA状态上报
---|---
测试目的|验证AMF可以基于用户当前位置，根据配置的核心网预定义PRA信息，判断用户的PRA状态，立即上报给PCF。
预置条件|AMF环境就绪，与周边NF间链路正常。全网已经规划好了核心网预定义的PRA区域。EM网管能正常连接并登录。PCF与AMF已协商，使用核心网预定义的PRA配置，并且PCF直接向AMF订阅PRA信息。“AMF支持PRA订阅功能”（License ID：7216）的License受控项打开。“PRA控制策略配置”中配置支持PRA功能，并且支持Location Reporting Control消息。软件参数配置AMF支持PRA订阅后立即上报。
测试过程|UE在5G网络发起初始注册流程。AMF向PCF发起建立策略关联请求，PCF在策略关联建立响应中携带PRA订阅信息。
通过准则|AMF基于UE当前位置判断用户的PRA状态，并直接通过策略关联更新请求立即上报给PCF。AMF将PRA订阅信息通过Location Reporting control消息通知给RAN侧。
测试结果|–
测试项目|AMF能够根据配置的PRA区域进行PRA状态上报
测试目的|验证AMF可以基于用户当前位置，根据配置的核心网预定义PRA信息，判断用户的PRA状态，立即上报给SMF。
预置条件|AMF环境就绪，与周边NF间链路正常。全网已经规划好了核心网预定义的PRA区域。EM网管能正常连接并登录。SMF与AMF已协商，使用核心网预定义的PRA配置，并且SMF直接向AMF订阅PRA信息。“AMF支持PRA订阅功能”的License受控项打开。“PRA控制策略配置”中配置支持PRA功能，并且支持Location Reporting Control消息。软件参数配置AMF支持PRA订阅后立即上报。
测试过程|UE在5G网络发起初始注册流程。UE在5G网络发起PDU建立流程。SMF向AMF发起订阅请求，请求中携带PRA订阅信息。
通过准则|AMF基于UE当前位置判断用户的PRA状态，并直接订阅响应立即上报给SMF。AMF将PRA订阅信息通过Location Reporting control消息通知给RAN侧。
测试结果|–
常见问题处理 :无。 
## ZUF-79-16-004 TA List变化 
概述 :TA List变化可以监测指定区域中的用户号码。 
客户收益 :在指定区域实施交通管制和用户拦截。 
说明 :TALIST变更用于为其他NF提供位置变更订阅通知。当UE移入/移出此区域时，AMF提供UE位置改变信息。 
对于UE位置变更为或变更为“关注区域”，SMF订阅AMF提供的“UE移动性事件通知”服务，用于报告感兴趣区域中UE的存在。收到AMF的通知后，SMF决定如何处理PDU会话，例如重新分配UPF。 
## ZUF-79-16-005 LCS 
特性描述 :特性描述 :术语 :术语|含义
---|---
LCS|LoCation Services，定位业务
描述 :定义 :LCS是移动通信网络通过无线信号测量来确定终端的地理位置信息及其移动速度的技术。LCS使得网络具备获取用户的地理位置信息的能力。
在5GC中，LCS业务是通过LCS客户端、GMLC、LMF、AMF的配合来实现。
LCS客户端发起定位请求。 
GMLC接收LCS客户端的请求，并向用户注册的AMF发送定位请求。 
AMF接收GMLC的定位请求后，选择LMF并请求LMF执行具体的定位。LMF用于具体收集、计算和决定UE的位置信息。 
定位完成后，定位信息顺序通过LMF、AMF、GMLC返回给LCS客户端。 
背景知识 :LCS定位业务是网络为利于开发基于位置的业务而提供的一组标准化业务能力，也是3GPP协议中规定的标准业务，用于管理用户的定位信息。 
LCS业务可以通过LCS客户端、LCS服务器和终端的交互获得终端在某个时刻的地理位置信息以及信息的精确度等。 
运营商可基于网络的定位能力获取位置信息，并结合位置信息推出各式各样的位置业务应用服务。位置业务应用将极大丰富运营商的业务，增强运营商的业务竞争力。 
应用场景 :紧急呼叫时，AMF主动上报终端的位置信息。 
紧急呼叫时，AMF接收GMLC发起的对终端位置信息查询的消息。 
普通场景（非紧急呼叫）时，AMF接收GMLC发起的对终端位置信息查询的消息。 
位置相关的业务中，UDM向AMF查询终端的当前位置信息。 
客户收益 :受益方|受益描述
---|---
运营商|提供定位业务，同时基于提供的UE位置信息，提供更多的位置类业务应用服务，增强运营商的业务竞争力。
移动用户|享受位置类业务带来的新体验。
实现原理 :系统架构 :LCS由UE、gNodeB（NG-RAN）、AMF、LMF、GMLC、UDM、LCS Client共同完成。LCS非漫游场景的网络架构如[图1]所示。
图1  LCS网络架构-非漫游场景

LCS漫游场景的网络架构如[图2]所示。
图2  LCS网络架构-漫游场景

LCS非漫游场景： UE位于归属网络，定位功能在归属网络内部完成。 
LCS漫游场景： UE位于拜访网络，定位功能由归属网络发起，由拜访网络完成定位并将定位结果返回给归属网络。 
涉及的网元 :NF名称|NF作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF，并传递会话相关消息。
UDM|提供用户及会话相关的签约信息。
GMLC|与LCS客户端及AMF交互，执行LCS客户端的定位请求并向其回送定位结果。
LMF|用于具体收集、计算和决定UE的相关位置信息。
gNodeB（NG-RAN）|UE接入时，提供无线资源及承载。实现AMF选择功能，即根据UE提供的信息选择UE当前服务的AMF。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
NL1/NLs|ZUF-79-19-013 NL1/NLs
NL2/NLg|ZUF-79-19-014 NL2/NLg
Nnrf|ZUF-79-19-010 Nnrf
本网元实现 :AMF在紧急会话建立时，发起NI-LR流程通知GMLC建立紧急会话。AMF在紧急会话释放时，通知GMLC释放紧急会话。 
AMF在MT-LR流程中，接收GMLC的定位请求后，AMF与LMF交互完成定位，最终将定位结果返回给GMLC。 
AMF在LMF和gNodeB、UE之间透传定位信息。 
AMF接收UDM发起的获取位置信息请求后，将UE位置信息返回给UDM。 
业务流程 :AMF支持LCS功能包括： 
支持NI-LR（Network Induced Location Request，网络触发定位请求）流程。 
支持MT-LR（Mobile Terminated Location Request，终端终止定位请求）流程。 
支持UE Assisted and UE Based Positioning（UE辅助及基于UE的定位）流程。 
支持Network Assisted Positioning（网络辅助定位）流程。 
支持Obtaining Non-UE Associated Network Assistance Data（获取非UE网络辅助数据）流程。 
支持Namf_Location_ProvideLocationInfo（UDM发起的获取UE位置信息的服务调用）流程。 
NI-LR流程
NI-LR流程图如[图3]所示。
图3  NI-LR流程

流程说明： 
UE执行紧急注册及紧急呼叫建立流程。 
Namf_Communication服务在紧急会话建立后，若“是否启用定位功能”及“是否启用紧急呼叫主动上报”功能开关均为启用状态，则Namf_Communication服务向Namf_Location服务发送通知紧急呼叫建立（Emergency Session Setup Notify）消息，在消息中携带用户标识SUPI/PEI、用户当前的位置NCGI。
Namf_Location服务接收到通知紧急呼叫建立消息后，生成LcsCorrelationID（即LCS Correlation ID）参数，判断“紧急呼叫是否主动向LMF获取位置”功能开关是否启用。若该开关为启用状态，则选择LMF，并向此LMF发送Nlmf_Location_DetermineLocation Request消息用于获取UE详细位置信息，在消息中携带SUPI/PEI、NCGI、externalClientType=EMERGENCY_SERVICES、LcsCorrelationID及amfId等参数。
LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位，具体参照“UE Assisted and UE Based Positioning流程”、“Network Assisted Positioning流程”、“Obtaining Non-UE Associated Network Assistance Data流程”的相关描述。
定位完成后，LMF向Namf_Location服务发送定位响应消息，携带相关位置参数。 
当Namf_Location服务获得LMF应答或“紧急呼叫是否主动向LMF获取位置”功能开关为关闭状态，Namf_Location服务执行GMLC选择，向选定的GMLC发送Namf_Location_EventNotify Request消息，在消息中携带locationEvent=EMERGENCY_CALL_ORIGINATION、SUPI/PEI、NCGI等参数。
GLMC接收消息后，返回Namf_Location_EventNotify Response消息。 
某一时刻，紧急呼叫释放。 
若“是否启用定位功能”及“是否启用紧急呼叫主动上报”功能开关均为启用状态，则Namf_Communication在紧急PDUSession释放后，向Namf_Location服务发送通知紧急呼叫释放（Emergency Session Release Notify）消息，在消息中携带用户标识SUPI/PEI。
Namf_Location服务接收到通知紧急呼叫释放消息后，根据SUPI/PEI查询用户上下文，获取GMLC信息，向GMLC发送Namf_Location_EventNotify Request消息，在消息中携带locationEvent = EMERGENCY_CALL_RELEASE、SUPI/PEI等参数。
GLMC接收消息后，给AMF返回Namf_Location_EventNotify Response消息。 
MT-LR流程
MT-LR流程图如[图4]所示。
图4  MT-LR流程

流程说明： 
紧急服务中心或公众安全服务中心等的LCS Client需要获取UE当前的位置信息，向GMLC发送定位请求（LCS Request）消息。 
GMLC通过用户标识向其归属UDM发送Nudm_UECM_Get Request消息获取UE信息。 
UDM返回Nudm_UECM_Get Response消息给GMLC，携带UE信息，包括UE当前注册的Serving AMF信息。 
GMLC向Serving AMF的Namf_Location服务发送Namf_Location_ProvidePositioningInfo请求消息，携带SUPI（正常用户）或PEI（无卡用户或非注册紧急用户），以及其他相关参数。
Namf_Location服务接收定位请求后，判断LCS功能开关“是否启用定位功能”是否启用。
若定位功能未启用，则回送失败响应指示403 Forbidden同时携带POSITIONING_DENIED。 
若启用，则继续后续处理。 
Namf_Location服务生成LcsCorrelationID（即LCS Correlation ID）参数，向Namf_Communication服务获取UE当前的NCGI（NR Cell Global Identifier）。 
Namf_Communication服务接收获取请求后： 
若UE处于IDLE态，则寻呼用户，Namf_Communication服务将从业务请求消息中获取的位置信息返回给Namf_Location服务。 
若UE处于CONNECTED态，Namf_Communication服务向RAN发送Location Reporting Control消息，携带direct标记。在获得RAN的响应后，Namf_Communication服务将从响应消息中获取的位置信息返回给Namf_Location服务。此时位置信息为当前NCGI。 
Namf_Location服务向选定的LMF发送Nlmf_Location_DetermineLocation Request消息，确定UE详细位置信息。消息中携带SUPI/PEI、NCGI、correlationID=LcsCorrelationID、amfId=自身NfInstanceId参数，其他参数根据GMLC请求中的参数进行填写（包括externalClientType，supportedGADShapes，locationQoS等）。 
LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程，并完成定位，具体参照“UE Assisted and UE Based Positioning流程”、“Network Assisted Positioning流程”、“Obtaining Non-UE Associated Network Assistance Datad流程”的相关描述。
定位完成后，LMF向Namf_Location服务发送定位响应消息（Nlmf_Location_DetermineLocation Response），携带相关位置参数。 
获得LMF应答后，Namf_Location服务向GMLC发送Namf_Location_ProvidePositioningInfo Response消息，携带的各参数根据LMF返回的参数进行填写。 
GMLC向LCS Client返回定位应答（LCS Response）消息，完成定位处理。 
UE Assisted and UE Based Positioning流程
UE Assisted and UE Based Positioning流程图如[图5]所示。
图5  UE Assisted and UE Based Positioning

流程说明： 
LMF主动向AMF的Namf_Communication服务进行N1N2消息订阅，其中携带参数n2InformationClass=NRPPa、n1MessageClass=LPP、nfId=NfInstanceId of LMF、n2NotifyCallbackUri和n1NotifyCallbackUri。AMF记录订阅信息并分配订阅标识n1n2NotifySubscriptionId，并向LMF回送响应消息。 
LMF向Namf_Communication服务发送Namf_Communication _N1N2MessageTransfer请求，其中lcsCorrelationId=LCS Correlation ID（用于关联定位会话），n1MessageContainer.n1MessageClass=LPP，n1MessageContainer.n1MessageContent=Downlink (DL) Positioning message。 
AMF通过Request-URI中的SUPI或PEI定位到UE上下文，若UE为IDLE状态，则AMF缓存消息，向UE发起paging并处理后续的业务请求。 
AMF根据缓存消息将LMF发送的Downlink (DL) Positioning message（携带在Payload container中）通过DL NAS TRANSPORT消息发送给UE，其中Payload container type=LTE Positioning Protocol (LPP) message container。 
UE根据消息执行测量计算等定位过程。 
定位完成后，若UE已进入IDLE状态，则UE发起业务请求，进入CONNECTED状态。 
UE将Uplink Positioning message（携带在Payload container中）通过UL NAS TRANSPORT消息发送给AMF，其中Payload container type=LTE Positioning Protocol (LPP) message container。 
AMF通过Namf_Communication_N1MessageNotify消息将UE返回内容发送给LMF，其中lcsCorrelationId=LCS Correlation ID、n1MessageContainer.n1MessageClass=LPP、n1MessageContainer.n1MessageContent=Uplink (UL) Positioning message等。 
Network Assisted Positioning流程
Network Assisted Positioning流程图如[图6]所示。
图6  Network Assisted Positioning

流程说明： 
LMF主动向AMF的Namf_Communication服务进行N1N2消息订阅，其中携带n2InformationClass=NRPPa、n1MessageClass=LPP、nfId=NfInstanceId of LMF、n2NotifyCallbackUri和n1NotifyCallbackUri。AMF记录订阅信息并分配订阅标识n1n2NotifySubscriptionId，并向LMF回送响应消息。 
LMF向Namf_Communication服务发送Namf_Communication _N1N2MessageTransfer请求，其中携带lcsCorrelationId=LCS Correlation ID（用于关联UE及定位会话）、n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message。 
Namf_Communication服务通过Request-URI中的SUPI或PEI定位到UE上下文，若UE为IDLE状态，则AMF缓存消息，并向UE发起paging并处理后续的业务请求。 
Namf_Communication服务根据缓存消息，使用DOWNLINK UE ASSOCIATED NRPPA TRANSPORT消息将LMF发送的Network Positioning message（携带在NRPPa-PDU中）发送给gNodeB（NG-RAN）。 
gNodeB（NG-RAN）执行测量定位过程。 
定位完成后，gNodeB（NG-RAN）将Network Positioning message（携带在NRPPa-PDU中）通过UPLINK UE ASSOCIATED NRPPA TRANSPORT消息发送给AMF的Namf_Communication服务。 
Namf_Communication服务使用Namf_Communication_N2InfoNotify消息将gNodeB（NG-RAN）返回内容发送给LMF，其中携带lcsCorrelationId=LCS Correlation ID、n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message、n2NotifySubscriptionId=n1n2NotifySubscriptionId（订阅时分配）。 
Obtaining Non-UE Associated Network Assistance Data流程
Obtaining Non-UE Associated Network Assistance Data流程图如[图7]所示。
图7  Obtaining Non-UE Associated Network Assistance Data

流程说明： 
LMF主动向AMF的Namf_Communication服务进行Non UE的N2消息订阅，其中携带n2InformationClass=NRPPa、nfId=NfInstanceId of LMF、n2NotifyCallbackUri。AMF记录订阅信息并分配订阅标识SubscriptionId，并向LMF回送响应消息。 
LMF向Namf_Communication服务发送Namf_Communication _NonUeN2MessageTransfer请求，其中携带globalRanNodeList（用于标识需要AMF向其发送消息的NG-RAN List）、n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message、n2InfoContainer.nrppaInfo.nfId=NfInstanceId of LMF。 
Namf_Communication服务将LMF发送的Network Positioning message（携带在NRPPa-PDU中）通过DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT消息发送给指定的gNodeB（NG-RAN）。如果存在多个gNodeB（NG-RAN），则分别发送。 
gNodeB（NG-RAN）执行测量定位过程。 
定位完成后，gNodeB（NG-RAN）将Network Positioning message（携带在NRPPa-PDU中）通过UPLINK NON UE ASSOCIATED NRPPA TRANSPORT消息发送给AMF的Namf_Communication服务。 
Namf_Communication服务使用Namf_Communication_NonUeN2InfoNotify消息将gNodeB（NG-RAN）返回的内容发送给LMF，其中携带n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message、n2InfoContainer.nrppaInfo.nfId=NfInstanceId of LMF、n2NotifySubscriptionId=SubscriptionId（订阅时分配的）。 
Namf_Location_ProvideLocationInfo流程
IDLE态处理流程图如[图8]所示。
图8  IDLE态处理

流程说明： 
UDM向AMF的Namf_Location服务发送Namf_Location_ProvideLocationInfo Request消息，URI中携带用户标识SUPI/PEI，消息体携带请求参数，如req5gsLoc，reqCurrentLoc，reqRatType及reqTimeZone参数。 
Namf_Location服务接收Namf_Location_ProvideLocationInfo调用请求后，判断LCS功能开关“是否启用定位功能”是否启用。
若为关闭，则Namf_Location服务回送403 Forbidden响应。 
若为启用，则Namf_Location服务向Namf_Communication服务发送位置获取请求消息，并携带用户标识信息。 
Namf_Communication服务接收请求消息，本流程中此时UE处于IDLE状态，进一步判断reqCurrentLoc参数。 
若reqCurrentLoc为TRUE，则在寻呼UE并获取位置信息后，Namf_Communication服务向Namf_Location服务返回位置获取响应消息，指示currentLoc为TRUE，同时携带User Location Information、RatType、TimeZone等参数。 
若reqCurrentLoc为FALSE或UE寻呼无响应，则取之前保存的UE位置信息作为last known location，Namf_Communication服务向Namf_Location服务返回位置获取响应消息，指示currentLoc为FALSE，同时携带User Location Information、RatType、TimeZone等参数。 
Namf_Communication服务向Namf_Location服务返回位置获取响应消息（Provide Location Response）。 
Namf_Location服务接收到响应消息后，向UDM发送响应（Namf_Location_ProvideLocationInfo Response），并根据UDM的请求通过消息体携带相关信息，如currentLoc、location、ratType、timezone等参数。 
CONNECTED态处理流程图如[图9]所示。
图9  CONNECTED态处理

流程说明： 
UDM向AMF的Namf_Location服务发送Namf_Location_ProvideLocationInfo Request消息，URI中携带用户标识SUPI/PEI，消息体携带请求参数，如req5gsLoc、reqCurrentLoc、reqRatType、reqTimeZone参数。 
Namf_Location服务接收Namf_Location_ProvideLocationInfo调用请求后，判断LCS功能开关“是否启用定位功能”是否启用。
若为关闭，则Namf_Location服务回送403 Forbidden响应。 
若为启用，则Namf_Location服务向Namf_Communication服务发送位置获取请求消息（Provide Location Request），并携带用户标识信息。 
Namf_Communication服务接收Namf_Location服务的请求消息，本流程中此时UE处于CONNECTED状态，进一步判断reqCurrentLoc参数。 
若reqCurrentLoc为TRUE，则Namf_Communication服务向gNodeB（NG-RAN）发送Location Reporting Control消息，并携带direct标记获取UE当前位置信息。Namf_Communication服务返回位置获取响应消息（Provide Location Response），并指示currentLoc为TRUE。 
若reqCurrentLoc为FALSE，则取之前保存的UE位置信息作为last known location。Namf_Communication服务返回位置获取响应消息（Provide Location Response），并指示currentLoc为FALSE。 
gNodeB（NG-RAN）向Namf_Communication服务发送Location Report消息，携带User Location Information。 
Namf_Communication服务向Namf_Location服务返回位置获取响应消息（Provide Location Response），消息中携带currentLoc指示、User Location Information、RatType、TimeZone等参数。 
Namf_Location服务接收响应消息后，向UDM发送响应（Namf_Location_ProvideLocationInfo Response），并根据UDM的请求通过消息体携带相关信息，如currentLoc、location、ratType、timezone等参数。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性的NI-LR（Network Induced Location Request，网络触发定位请求）流程涉及与紧急业务的交互。除此以外，该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.502（Procedures for the 5G System (5GS);Stage 2）|4.13.5 Location Services procedures4.13.5.1 5GC-NI-LR Procedure4.13.5.2 5GC-MT-LR Procedure without UDM Query4.13.5.3 5GC-MT-LR Procedure4.13.5.4 UE Assisted and UE Based Positioning Procedure4.13.5.5 Network Assisted Positioning Procedure4.13.5.6 Obtaining Non-UE Associated Network Assistance Data
3GPP TS 23.273（5G System (5GS) Location Services (LCS);Stage 2）|6.1 5GC-MT-LR Procedure6.10.1 5GC-NI-LR Procedure6.10.2 5GC-MT-LR Procedure without UDM Query6.11 Common Sub-Procedures
3GPP TS 29.518（Access and Mobility Management Services;Stage 3）|5.5 Namf_Location Service6.4 Namf_Location Service API
3GPP TS 29.572（5G System;Location Management Services;Stage 3）|5 Services Offered by the LMF6.1 Nlmf_Location Service API
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.20|首次发布
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为"AMF支持LCS功能"（license ID：7232），此项目显示为“支持”，表示AMF支持LCS功能。
对其他网元的要求 :UE|eNodeB|GMLC|LMF|UDM
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增配置命令参见[表1]。
配置项|命令
---|---
定位开关配置|SET LCSSWITCH
SHOW LCSSWITCH|定位开关配置
GMLC授权配置|SET GMLCAUTHCFG
SHOW GMLCAUTHCFG|GMLC授权配置
LCS功能配置|SET LCSFUNCTION
SHOW LCSFUNCTION|LCS功能配置
发现策略配置|SET LCSDISCOMODE
SHOW LCSDISCOMODE|发现策略配置
LMF节点配置|ADD LMFNODECFG
SET LMFNODECFG|LMF节点配置
DEL LMFNODECFG|LMF节点配置
SHOW LMFNODECFG|LMF节点配置
LMF地址池配置|ADD LMFLOCALADDRPOOL
DEL LMFLOCALADDRPOOL|LMF地址池配置
SHOW LMFLOCALADDRPOOL|LMF地址池配置
LMF地址类型选择策略配置|SET LMFADDRCHOICEPOLICY
SHOW LMFADDRCHOICEPOLICY|LMF地址类型选择策略配置
GMLC地址池配置|ADD GMLCLOCALADDRPOOL
DEL GMLCLOCALADDRPOOL|GMLC地址池配置
SHOW GMLCLOCALADDRPOOL|GMLC地址池配置
GMLC节点配置|ADD GMLCNODECONFIG
SET GMLCNODECONFIG|GMLC节点配置
DEL GMLCNODECONFIG|GMLC节点配置
SHOW GMLCNODECONFIG|GMLC节点配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :如果启用LCS功能，需开启license（uMAC_AMF_7232），并通过[SET LCSSWITCH]命令打开定位功能开关。由于默认的LMF发现模式为本地策略，可通过[ADD LMFNODECFG]、[ADD LMFLOCALADDRPOOL]命令配置目标LMF地址，通过SET LMFADDRCHOICEPOLICY命令修改地址类型（默认IPV4）。
如果启用紧急呼叫，AMF主动上报终端的位置信息功能，需通过[SET LCSSWITCH]命令打开定位功能开关和紧急上报开关。由于默认的GMLC发现模式为本地策略，还需通过[ADD GMLCLOCALADDRPOOL]命令配置目标GMLC地址。
配置前提 :AMF网元运行正常。 
已部署Namf_Location服务。 
已启用License（uMAC_AMF_7232）。 
配置过程 :###### MT-LR流程（有NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET GMLCAUTHCFG]命令，修改GMLC授权状态。
###### MT-LR流程（无NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
（可选）执行[SET LCSDISCOMODE]命令，修改发现模式配置。
执行[ADD LMFNODECFG]命令，新增 LMF节点。
执行[ADD LMFLOCALADDRPOOL]命令，增加LMF地址池配置。
执行[SET LMFADDRCHOICEPOLICY]命令，修改LMF地址选择策略配置。
###### NI-LR流程（有NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
###### NI-LR流程（无NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
执行[ADD GMLCNODECONFIG]命令，新增 GMLC节点。
执行[ADD GMLCLOCALADDRPOOL]命令，增加GMLC地址池配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
（可选）执行[ADD LMFNODECFG]命令，新增 LMF节点。
（可选）执行[ADD LMFLOCALADDRPOOL]命令，增加LMF地址池配置。
（可选）执行[SET LMFADDRCHOICEPOLICY]命令，修改LMF地址选择策略配置。
###### ProvideLocationInfo流程 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
配置实例 :场景说明 :场景一：
紧急呼叫时，AMF主动上报终端的位置信息。 
场景二：
紧急呼叫时，AMF接收GLMC发起的对终端的位置信息查询消息。 
普通场景（非紧急呼叫）时，AMF接收GLMC发起的对终端的位置信息查询消息。 
场景三：
在位置相关的业务中，UDM向AMF查询终端的当前位置信息。 
数据规划 :场景|配置项|参数|取值
---|---|---|---
场景一|LCSSWITCH配置|是否启用定位功能|YES
是否启用紧急呼叫主动上报|场景一|LCSSWITCH配置|YES
发现模式配置|场景一|LMF发现模式|NRF发现
GMLC发现模式|发现模式配置|场景一|NRF发现
LCSFUNCTION配置|场景一|紧急呼叫是否主动向LMF获取位置|NO
是否携带位置qos|LCSFUNCTION配置|场景一|NO
水平精度|LCSFUNCTION配置|场景一|65535
响应时间|LCSFUNCTION配置|场景一|低
是否获取垂直精度|LCSFUNCTION配置|场景一|NO
垂直精度|LCSFUNCTION配置|场景一|65535
定位优先级|LCSFUNCTION配置|场景一|低
是否获取速度|LCSFUNCTION配置|场景一|NO
是否携带GAD参数|LCSFUNCTION配置|场景一|NO
支持的GAD形状|LCSFUNCTION配置|场景一|POINT
场景二|LCSSWITCH配置|是否启用定位功能|YES
是否启用紧急呼叫主动上报|场景二|LCSSWITCH配置|NO
发现模式配置|场景二|LMF发现模式|NRF发现
GMLC发现模式|发现模式配置|场景二|本地配置
场景三|LCSSWITCH配置|是否启用定位功能|YES
是否启用紧急呼叫主动上报|场景三|LCSSWITCH配置|NO
配置步骤 :场景|步骤|说明|操作
---|---|---|---
场景一|1|开启LCS定位开关和紧急呼叫主动上报开关。|SET LCSSWITCH:SWITCHLOCATION="YES",ESSWITCH="YES"
2|场景一|配置GMLC发现模式为NRF发现。|SET LCSDISCOMODE:LMFDISCOVERYMODE="NRF_DISCOVERY",GMLCDISCOVERYMODE="NRF_DISCOVERY"
3|场景一|配置紧急呼叫上报消息参数。|SET LCSFUNCTION:ELMFSWITCH="NO",LQOSSWITCH="NO",HACCURACY=1,RESPONSETIME="LOW_DELAY",VERTREQUESTED="NO",LCSPRIORITY="NORMAL_PRIORITY",VELOCITYREQUESTED="VELOCITY_IS_NOT_REQUESTED",SHAPESWITCH="YES",SUPPORTGADSHAPE="POINT"
场景二|1|开启LCS定位开关。|SET LCSSWITCH:SWITCHLOCATION="YES"
2|场景二|配置LMF发现模式为NRF发现。|SET LCSDISCOMODE:LMFDISCOVERYMODE="NRF_DISCOVERY"
场景三|1|开启LCS定位开关。|SET LCSSWITCH:SWITCHLOCATION="YES"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|普通场景（无NRF发现）时，AMF接收GMLC发起的对终端UE的位置查询（MT-LR）
---|---
测试目的|GMLC根据NEF、AF以及LCS Client等要求发起对UE的定位请求，AMF根据请求向LMF发起确定位置请求，LMF继续对UE进行定位信息获取并给AMF返回响应，最终AMF将位置信息返回给GMLC，供定位发起者进一步使用。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关）已打开。本地配置LMF地址。
测试过程|AMF收到GMLC的Namf_Location_ProvidePositioningInfo请求消息。UE处于CONNECTED态，AMF向RAN发送Location Reporting Control消息携带direct标记，在获得RAN的响应后，从响应消息中获取位置信息。AMF向选定的LMF发送Nlmf_Location_DetermineLocation请求确定UE位置信息。定位完成后，LMF向AMF发送定位响应消息。AMF向保存的GMLC发送Namf_Location_ProvidePositioningInfo响应消息，消息中各参数取值根据LMF返回的数据进行填写。
通过准则|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试结果|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试项目|普通场景时（NRF发现），AMF接收GMLC发起的对终端UE的位置查询（MT-LR）
---|---
测试目的|GMLC根据NEF、AF以及LCS Client等要求发起对UE的定位请求，AMF根据请求向LMF发起确定位置请求，LMF继续对UE进行定位信息获取并给AMF返回响应，最终AMF将位置信息返回给GMLC，供定位发起者进一步使用。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关）已打开。执行SET LCSDISCOMODE命令，修改发现模式配置为NRF发现。
测试过程|AMF收到GMLC的Namf_Location_ProvidePositioningInfo请求消息。UE处于CONNECTED态，AMF向RAN发送Location Reporting Control消息携带direct标记，在获得RAN的响应后，从响应消息中获取位置信息。AMF向NRF返回的LMF发送Nlmf_Location_DetermineLocation请求确定UE位置信息。定位完成后，LMF向AMF发送定位响应消息。AMF向保存的GMLC发送Namf_Location_ProvidePositioningInfo响应消息，消息中各参数取值根据LMF返回的数据进行填写。
通过准则|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试结果|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
常见问题处理 :无 
## ZUF-79-16-006 eLCS 
特性描述 :特性描述 :描述 :定义 :LCS是移动通信网络通过无线信号测量来确定终端的地理位置信息及其移动速度的技术。LCS使得网络具备获取用户的地理位置信息的能力。
eLCS是增强定位业务，参照3GPP Release 16Release 16版本规范实现的LCS功能。 
在5GC中，LCS业务是通过LCS客户端、GMLC、LMF、AMF的配合来实现。
LCS客户端发起定位请求。 
GMLC接收LCS客户端的请求，并向用户注册的AMF发送定位请求。 
AMF接收GMLC的定位请求后，选择LMF并请求LMF执行具体的定位。LMF用于具体收集、计算和决定UE的位置信息。 
定位完成后，定位信息顺序通过LMF、AMF、GMLC返回给LCS客户端。 
背景知识 :LCS定位业务是网络为利于开发基于位置的业务而提供的一组标准化业务能力，也是3GPP协议中规定的标准业务，用于管理用户的定位信息。 
LCS业务可以通过LCS客户端、LCS服务器和终端的交互获得终端在某个时刻的地理位置信息以及信息的精确度等。 
运营商可基于网络的定位能力获取位置信息，并结合位置信息推出各式各样的位置业务应用服务。位置业务应用将极大丰富运营商的业务，增强运营商的业务竞争力。 
应用场景 :紧急呼叫时，AMF主动上报终端的位置信息。 
紧急呼叫时，AMF接收GMLC发起的对终端位置信息查询的消息。 
普通场景（非紧急呼叫）时，AMF接收GMLC发起的对终端位置信息查询的消息。 
位置相关的业务中，UDM向AMF查询终端的当前位置信息。 
终端发起定位，包括终端主动获取位置信息，获取辅助数据，获取位置信息并转发给GMLC三种类型。 
延迟定位（UE可用事件）时，AMF接收GMLC发起的对终端可用后的延迟定位请求消息。 
客户收益 :受益方|受益描述
---|---
运营商|提供定位业务，同时基于提供的UE位置信息，提供更多的位置类业务应用服务，增强运营商的业务竞争力。
移动用户|享受位置类业务带来的新体验。
实现原理 :系统架构 :LCS由UE、gNodeB（NG-RAN）、AMF、LMF、GMLC、UDM、LCS Client共同完成。LCS非漫游场景的网络架构如[图1]所示。
图1  LCS网络架构-非漫游场景

LCS漫游场景的网络架构如[图2]所示。
图2  LCS网络架构-漫游场景

LCS非漫游场景： UE位于归属网络，定位功能在归属网络内部完成。 
LCS漫游场景： UE位于拜访网络，定位功能由归属网络发起，由拜访网络完成定位并将定位结果返回给归属网络。 
涉及的网元 :NF名称|NF作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF，并传递会话相关消息。
UDM|提供用户及会话相关的签约信息。
GMLC|与LCS客户端及AMF交互，执行LCS客户端的定位请求并向其回送定位结果。
LMF|用于具体收集、计算和决定UE的相关位置信息。
gNodeB（NG-RAN）|UE接入时，提供无线资源及承载。实现AMF选择功能，即根据UE提供的信息选择UE当前服务的AMF。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
NL1/NLs|ZUF-79-19-013 NL1/NLs
NL2/NLg|ZUF-79-19-014 NL2/NLg
Nnrf|ZUF-79-19-010 Nnrf
本网元实现 :AMF在紧急会话建立时，发起NI-LR流程通知GMLC建立紧急会话。AMF在紧急会话释放时，通知GMLC释放紧急会话。 
AMF在MT-LR流程中，接收GMLC的定位请求后，AMF与LMF交互完成定位，最终将定位结果返回给GMLC。 
AMF在LMF和gNodeB、UE之间透传定位信息。 
AMF接收UDM发起的获取位置信息请求后，将UE位置信息返回给UDM。 
AMF在MO-LR流程中，接收UE的定位请求后，AMF根据UE请求与LMF交互完成定位或辅助数据的下发，或将位置信息转发给GMLC。 
AMF在MT-LR流程中，接收GMLC的延迟定位请求（UE可用事件类型）并在UE可用后，AMF与LMF交互完成定位，最终将定位结果返回给GMLC。 
业务流程 :AMF支持LCS功能包括： 
支持NI-LR（Network Induced Location Request，网络触发定位请求）流程。 
支持MT-LR（Mobile Terminated Location Request，终端终止定位请求）流程。 
支持UE Assisted and UE Based Positioning（UE辅助及基于UE的定位）流程。 
支持Network Assisted Positioning（网络辅助定位）流程。 
支持Obtaining Non-UE Associated Network Assistance Data（获取非UE网络辅助数据）流程。 
支持Namf_Location_ProvideLocationInfo（UDM发起的获取UE位置信息的服务调用）流程。 
支持MO-LR流程。 
支持Deferred MT-LR（延迟定位）UE可用事件类型（UE Available Location Event）流程。 
NI-LR流程
NI-LR流程图如[图3]所示。
图3  NI-LR流程

流程说明： 
UE执行紧急注册及紧急呼叫建立流程。 
Namf_Communication服务在紧急会话建立后，若“是否启用定位功能”及“是否启用紧急呼叫主动上报”功能开关均为启用状态，则Namf_Communication服务向Namf_Location服务发送通知紧急呼叫建立（Emergency Session Setup Notify）消息，在消息中携带用户标识SUPI/PEI、用户当前的位置NCGI。
Namf_Location服务接收到通知紧急呼叫建立消息后，生成LcsCorrelationID（即LCS Correlation ID）参数，判断“紧急呼叫是否主动向LMF获取位置”功能开关是否启用。若该开关为启用状态，则选择LMF，并向此LMF发送Nlmf_Location_DetermineLocation Request消息用于获取UE详细位置信息，在消息中携带SUPI/PEI、NCGI、externalClientType=EMERGENCY_SERVICES、LcsCorrelationID及amfId等参数。
LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位，具体参照“UE Assisted and UE Based Positioning流程”、“Network Assisted Positioning流程”、“Obtaining Non-UE Associated Network Assistance Data流程”的相关描述。
定位完成后，LMF向Namf_Location服务发送定位响应消息，携带相关位置参数。 
当Namf_Location服务获得LMF应答或“紧急呼叫是否主动向LMF获取位置”功能开关为关闭状态，Namf_Location服务执行GMLC选择，向选定的GMLC发送Namf_Location_EventNotify Request消息，在消息中携带locationEvent=EMERGENCY_CALL_ORIGINATION、SUPI/PEI、NCGI等参数。
GLMC接收消息后，返回Namf_Location_EventNotify Response消息。 
某一时刻，紧急呼叫释放。 
若“是否启用定位功能”及“是否启用紧急呼叫主动上报”功能开关均为启用状态，则Namf_Communication在紧急PDUSession释放后，向Namf_Location服务发送通知紧急呼叫释放（Emergency Session Release Notify）消息，在消息中携带用户标识SUPI/PEI。
Namf_Location服务接收到通知紧急呼叫释放消息后，根据SUPI/PEI查询用户上下文，获取GMLC信息，向GMLC发送Namf_Location_EventNotify Request消息，在消息中携带locationEvent = EMERGENCY_CALL_RELEASE、SUPI/PEI等参数。
GLMC接收消息后，给AMF返回Namf_Location_EventNotify Response消息。 
MT-LR流程
MT-LR流程图如[图4]所示。
图4  MT-LR流程

流程说明： 
紧急服务中心或公众安全服务中心等的LCS Client需要获取UE当前的位置信息，向GMLC发送定位请求（LCS Request）消息。 
GMLC通过用户标识向其归属UDM发送Nudm_UECM_Get Request消息获取UE信息。 
UDM返回Nudm_UECM_Get Response消息给GMLC，携带UE信息，包括UE当前注册的Serving AMF信息。 
GMLC向Serving AMF的Namf_Location服务发送Namf_Location_ProvidePositioningInfo请求消息，携带SUPI（正常用户）或PEI（无卡用户或非注册紧急用户），以及其他相关参数。
Namf_Location服务接收定位请求后，判断LCS功能开关“是否启用定位功能”是否启用。
若定位功能未启用，则回送失败响应指示403 Forbidden同时携带POSITIONING_DENIED。 
若启用，则继续后续处理。 
Namf_Location服务生成LcsCorrelationID（即LCS Correlation ID）参数，向Namf_Communication服务获取UE当前的NCGI（NR Cell Global Identifier）。 
Namf_Communication服务接收获取请求后： 
若UE处于IDLE态，则寻呼用户，Namf_Communication服务将从业务请求消息中获取的位置信息返回给Namf_Location服务。 
若UE处于CONNECTED态，Namf_Communication服务向RAN发送Location Reporting Control消息，携带direct标记。在获得RAN的响应后，Namf_Communication服务将从响应消息中获取的位置信息返回给Namf_Location服务。此时位置信息为当前NCGI。 
Namf_Location服务向选定的LMF发送Nlmf_Location_DetermineLocation Request消息，确定UE详细位置信息。消息中携带SUPI/PEI、NCGI、correlationID=LcsCorrelationID、amfId=自身NfInstanceId参数，其他参数根据GMLC请求中的参数进行填写（包括externalClientType，supportedGADShapes，locationQoS等）。 
LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程，并完成定位，具体参照“UE Assisted and UE Based Positioning流程”、“Network Assisted Positioning流程”、“Obtaining Non-UE Associated Network Assistance Datad流程”的相关描述。
定位完成后，LMF向Namf_Location服务发送定位响应消息（Nlmf_Location_DetermineLocation Response），携带相关位置参数。 
获得LMF应答后，Namf_Location服务向GMLC发送Namf_Location_ProvidePositioningInfo Response消息，携带的各参数根据LMF返回的参数进行填写。 
GMLC向LCS Client返回定位应答（LCS Response）消息，完成定位处理。 
UE Assisted and UE Based Positioning流程
UE Assisted and UE Based Positioning流程图如[图5]所示。
图5  UE Assisted and UE Based Positioning

流程说明： 
LMF主动向AMF的Namf_Communication服务进行N1N2消息订阅，其中携带参数n2InformationClass=NRPPa、n1MessageClass=LPP、nfId=NfInstanceId of LMF、n2NotifyCallbackUri和n1NotifyCallbackUri。AMF记录订阅信息并分配订阅标识n1n2NotifySubscriptionId，并向LMF回送响应消息。 
LMF向Namf_Communication服务发送Namf_Communication _N1N2MessageTransfer请求，其中lcsCorrelationId=LCS Correlation ID（用于关联定位会话），n1MessageContainer.n1MessageClass=LPP，n1MessageContainer.n1MessageContent=Downlink (DL) Positioning message。 
AMF通过Request-URI中的SUPI或PEI定位到UE上下文，若UE为IDLE状态，则AMF缓存消息，向UE发起paging并处理后续的业务请求。 
AMF根据缓存消息将LMF发送的Downlink (DL) Positioning message（携带在Payload container中）通过DL NAS TRANSPORT消息发送给UE，其中Payload container type=LTE Positioning Protocol (LPP) message container。 
UE根据消息执行测量计算等定位过程。 
定位完成后，若UE已进入IDLE状态，则UE发起业务请求，进入CONNECTED状态。 
UE将Uplink Positioning message（携带在Payload container中）通过UL NAS TRANSPORT消息发送给AMF，其中Payload container type=LTE Positioning Protocol (LPP) message container。 
AMF通过Namf_Communication_N1MessageNotify消息将UE返回内容发送给LMF，其中lcsCorrelationId=LCS Correlation ID、n1MessageContainer.n1MessageClass=LPP、n1MessageContainer.n1MessageContent=Uplink (UL) Positioning message等。 
Network Assisted Positioning流程
Network Assisted Positioning流程图如[图6]所示。
图6  Network Assisted Positioning

流程说明： 
LMF主动向AMF的Namf_Communication服务进行N1N2消息订阅，其中携带n2InformationClass=NRPPa、n1MessageClass=LPP、nfId=NfInstanceId of LMF、n2NotifyCallbackUri和n1NotifyCallbackUri。AMF记录订阅信息并分配订阅标识n1n2NotifySubscriptionId，并向LMF回送响应消息。 
LMF向Namf_Communication服务发送Namf_Communication _N1N2MessageTransfer请求，其中携带lcsCorrelationId=LCS Correlation ID（用于关联UE及定位会话）、n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message。 
Namf_Communication服务通过Request-URI中的SUPI或PEI定位到UE上下文，若UE为IDLE状态，则AMF缓存消息，并向UE发起paging并处理后续的业务请求。 
Namf_Communication服务根据缓存消息，使用DOWNLINK UE ASSOCIATED NRPPA TRANSPORT消息将LMF发送的Network Positioning message（携带在NRPPa-PDU中）发送给gNodeB（NG-RAN）。 
gNodeB（NG-RAN）执行测量定位过程。 
定位完成后，gNodeB（NG-RAN）将Network Positioning message（携带在NRPPa-PDU中）通过UPLINK UE ASSOCIATED NRPPA TRANSPORT消息发送给AMF的Namf_Communication服务。 
Namf_Communication服务使用Namf_Communication_N2InfoNotify消息将gNodeB（NG-RAN）返回内容发送给LMF，其中携带lcsCorrelationId=LCS Correlation ID、n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message、n2NotifySubscriptionId=n1n2NotifySubscriptionId（订阅时分配）。 
Obtaining Non-UE Associated Network Assistance Data流程
Obtaining Non-UE Associated Network Assistance Data流程图如[图7]所示。
图7  Obtaining Non-UE Associated Network Assistance Data

流程说明： 
LMF主动向AMF的Namf_Communication服务进行Non UE的N2消息订阅，其中携带n2InformationClass=NRPPa、nfId=NfInstanceId of LMF、n2NotifyCallbackUri。AMF记录订阅信息并分配订阅标识SubscriptionId，并向LMF回送响应消息。 
LMF向Namf_Communication服务发送Namf_Communication _NonUeN2MessageTransfer请求，其中携带globalRanNodeList（用于标识需要AMF向其发送消息的NG-RAN List）、n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message、n2InfoContainer.nrppaInfo.nfId=NfInstanceId of LMF。 
Namf_Communication服务将LMF发送的Network Positioning message（携带在NRPPa-PDU中）通过DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT消息发送给指定的gNodeB（NG-RAN）。如果存在多个gNodeB（NG-RAN），则分别发送。 
gNodeB（NG-RAN）执行测量定位过程。 
定位完成后，gNodeB（NG-RAN）将Network Positioning message（携带在NRPPa-PDU中）通过UPLINK NON UE ASSOCIATED NRPPA TRANSPORT消息发送给AMF的Namf_Communication服务。 
Namf_Communication服务使用Namf_Communication_NonUeN2InfoNotify消息将gNodeB（NG-RAN）返回的内容发送给LMF，其中携带n2InfoContainer.n2InformationClass=NRPPa、n2InfoContainer.nrppaInfo.nrppaPdu=Network Positioning message、n2InfoContainer.nrppaInfo.nfId=NfInstanceId of LMF、n2NotifySubscriptionId=SubscriptionId（订阅时分配的）。 
Namf_Location_ProvideLocationInfo流程
IDLE态处理流程图如[图8]所示。
图8  IDLE态处理

流程说明： 
UDM向AMF的Namf_Location服务发送Namf_Location_ProvideLocationInfo Request消息，URI中携带用户标识SUPI/PEI，消息体携带请求参数，如req5gsLoc，reqCurrentLoc，reqRatType及reqTimeZone参数。 
Namf_Location服务接收Namf_Location_ProvideLocationInfo调用请求后，判断LCS功能开关“是否启用定位功能”是否启用。
若为关闭，则Namf_Location服务回送403 Forbidden响应。 
若为启用，则Namf_Location服务向Namf_Communication服务发送位置获取请求消息，并携带用户标识信息。 
Namf_Communication服务接收请求消息，本流程中此时UE处于IDLE状态，进一步判断reqCurrentLoc参数。 
若reqCurrentLoc为TRUE，则在寻呼UE并获取位置信息后，Namf_Communication服务向Namf_Location服务返回位置获取响应消息，指示currentLoc为TRUE，同时携带User Location Information、RatType、TimeZone等参数。 
若reqCurrentLoc为FALSE或UE寻呼无响应，则取之前保存的UE位置信息作为last known location，Namf_Communication服务向Namf_Location服务返回位置获取响应消息，指示currentLoc为FALSE，同时携带User Location Information、RatType、TimeZone等参数。 
Namf_Communication服务向Namf_Location服务返回位置获取响应消息（Provide Location Response）。 
Namf_Location服务接收到响应消息后，向UDM发送响应（Namf_Location_ProvideLocationInfo Response），并根据UDM的请求通过消息体携带相关信息，如currentLoc、location、ratType、timezone等参数。 
CONNECTED态处理流程图如[图9]所示。
图9  CONNECTED态处理

流程说明： 
UDM向AMF的Namf_Location服务发送Namf_Location_ProvideLocationInfo Request消息，URI中携带用户标识SUPI/PEI，消息体携带请求参数，如req5gsLoc、reqCurrentLoc、reqRatType、reqTimeZone参数。 
Namf_Location服务接收Namf_Location_ProvideLocationInfo调用请求后，判断LCS功能开关“是否启用定位功能”是否启用。
若为关闭，则Namf_Location服务回送403 Forbidden响应。 
若为启用，则Namf_Location服务向Namf_Communication服务发送位置获取请求消息（Provide Location Request），并携带用户标识信息。 
Namf_Communication服务接收Namf_Location服务的请求消息，本流程中此时UE处于CONNECTED状态，进一步判断reqCurrentLoc参数。 
若reqCurrentLoc为TRUE，则Namf_Communication服务向gNodeB（NG-RAN）发送Location Reporting Control消息，并携带direct标记获取UE当前位置信息。Namf_Communication服务返回位置获取响应消息（Provide Location Response），并指示currentLoc为TRUE。 
若reqCurrentLoc为FALSE，则取之前保存的UE位置信息作为last known location。Namf_Communication服务返回位置获取响应消息（Provide Location Response），并指示currentLoc为FALSE。 
gNodeB（NG-RAN）向Namf_Communication服务发送Location Report消息，携带User Location Information。 
Namf_Communication服务向Namf_Location服务返回位置获取响应消息（Provide Location Response），消息中携带currentLoc指示、User Location Information、RatType、TimeZone等参数。 
Namf_Location服务接收响应消息后，向UDM发送响应（Namf_Location_ProvideLocationInfo Response），并根据UDM的请求通过消息体携带相关信息，如currentLoc、location、ratType、timezone等参数。 
MO-LR流程
MO-LR流程如[图10]所示。
图10  MO-LR流程

流程说明： 
UE主动发起MO-LR流程，通过UL NAS TRANSPORT消息携带MO-LR请求给AMF。 
Namf_Communication服务接收消息后，向UDM获取LCS Mobile Originated data签约数据，检查UE签约。 
AMF启动MO-LR的处理，携带参数向Namf_Location服务发送MO-LR请求消息，携带NCGI等相关参数。 
Namf_Location服务接收请求后，创建定位上下文，生成定位关联ID（即LCS Correlation ID）参数，保存MO-LR请求参数。 
Namf_Location服务实例执行LMF发现和选择，并向LMF发送Nlmf_Location_DetermineLocation请求消息，填写SUPI/PEI，NCGI，LcsCorrelationID及amfId参数，携带UeLocationServiceInd（LOCATION_ESTIMATE或LOCATION_ASSISTANCE_DATA）参数。 
LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位，或给UE下发辅助数据。具体参照“UE Assisted and UE Based Positioning处理流程”“Network Assisted Positioning处理流程”“Obtaining Non-UE Associated Network Assistance Data处理流程”相关描述。 
定位完成后，LMF向Namf_Location服务发送定位响应消息。 
可选：Namf_Location服务实例根据MO-LR请求类型，若需要通知GMLC，Namf_Location服务实例执行GMLC选择，向GMLC发送Ngmlc_Location_LocationUpdate消息。 
可选：GLMC接收消息后，返回响应。 
Namf_Location服务给Namf_Communication服务发送MO-LR响应。 
Namf_Communication服务根据响应消息，给UE发送DL NAS TRANSPORT携带响应，完成处理。 
Deferred MT-LR（UE Available Location Event）流程
延迟定位UE可用事件流程如[图11]所示。
图11  Deferred MT-LR（UE Available Location Event）流程

流程说明： 
GMLC向Namf_Location服务发送Namf_Location_ProvidePositioningInfo请求消息，携带SUPI等参数，LdrType指示为UE_AVAILABLE定位事件。 
Namf_Location服务接收定位请求后，向Namf_Communication服务请求UE当前的NCGI，并携带UE可用事件指示。 
Namf_Communication服务接收请求后，判断UE不可用。 
Namf_Communication服务设置UE可用事件标记。 
Namf_Communication服务给Namf_Location服务回送响应消息，指示UE当前不可用。 
某时刻，UE可用。 
Namf_Communication服务向Namf_Location服务发送消息指示UE可用，并携带NCGI等参数。 
Namf_Location服务接收指示消息后，回送响应。 
Namf_Communication服务接收响应消息后，清除UE可用事件标记。 
Namf_Location服务执行LMF发现和选择，并向LMF发送Nlmf_Location_DetermineLocation请求消息，填写SUPI/PEI，NCGI，LcsCorrelationID及amfId等参数。 
LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位。具体参照“UE Assisted and UE Based Positioning处理流程”“Network Assisted Positioning处理流程”“Obtaining Non-UE Associated Network Assistance Data处理流程”相关描述。 
定位完成后，LMF向Namf_Location服务发送定位响应消息。 
Namf_Location服务给GMLC发送Namf_Location_EventNotify消息，填写SUPI/PEI，locationEvent = ACTIVATION_OF_DEFERRED_LOCATION等参数。接收GLMC响应完成处理。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性的NI-LR（Network Induced Location Request，网络触发定位请求）流程涉及与ZUF-79-13-005 紧急业务
的交互。除此以外，该特性不涉及与其他特性的交互。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.502（Procedures for the 5G System (5GS);Stage 2）|4.13.5 Location Services procedures4.13.5.1 5GC-NI-LR Procedure4.13.5.2 5GC-MT-LR Procedure without UDM Query4.13.5.3 5GC-MT-LR Procedure4.13.5.4 UE Assisted and UE Based Positioning Procedure4.13.5.5 Network Assisted Positioning Procedure4.13.5.6 Obtaining Non-UE Associated Network Assistance Data
3GPP TS 23.273（5G System (5GS) Location Services (LCS);Stage 2）|6.1 5GC-MT-LR Procedure6.2 5GC-MO-LR Procedure6.3 Deferred 5GC-MT-LR Procedure for Periodic, Triggered and UE Available Location Events6.10.1 5GC-NI-LR Procedure6.10.2 5GC-MT-LR Procedure without UDM Query6.11 Common Sub-Procedures
3GPP TS 24.080（Mobile radio interface layer 3 Supplementary services specification;Formats and coding）|2 Message functional definitions and contents3 General message format and information elements coding4.2.2.25 lcs-MOLR (MS --> Network)4.4 Data types and identifiers
3GPP TS 24.571（5G System;Control plane Location Services (LCS) procedures;Stage 3）|4.2 LCS Support capabilities5.2.2.1 Mobile Originiated Location Request(MO-LR)
3GPP TS 29.515（5G System; Gateway Mobile Location Services;Stage 3）|5.2.2.3 LocationUpdate6.1 Ngmlc_Location Service API
3GPP TS 29.518（Access and Mobility Management Services;Stage 3）|5.5 Namf_Location Service6.4 Namf_Location Service API
3GPP TS 29.572（5G System;Location Management Services;Stage 3）|5 Services Offered by the LMF6.1 Nlmf_Location Service API
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.22.20|新增支持延迟定位终端可用事件，以及终端发起定位功能。
01|V7.20.20|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为"AMF支持LCS功能"（license ID：7232），此项目显示为“支持”，表示AMF支持LCS功能。
对其他网元的要求 :UE|eNodeB|GMLC|LMF|UDM
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增配置命令参见[表1]。
配置项|命令
---|---
定位开关配置|SET LCSSWITCH
SHOW LCSSWITCH|定位开关配置
GMLC授权配置|SET GMLCAUTHCFG
SHOW GMLCAUTHCFG|GMLC授权配置
LCS功能配置|SET LCSFUNCTION
SHOW LCSFUNCTION|LCS功能配置
发现策略配置|SET LCSDISCOMODE
SHOW LCSDISCOMODE|发现策略配置
LMF节点配置|ADD LMFNODECFG
SET LMFNODECFG|LMF节点配置
DEL LMFNODECFG|LMF节点配置
SHOW LMFNODECFG|LMF节点配置
LMF地址池配置|ADD LMFLOCALADDRPOOL
DEL LMFLOCALADDRPOOL|LMF地址池配置
SHOW LMFLOCALADDRPOOL|LMF地址池配置
LMF地址类型选择策略配置|SET LMFADDRCHOICEPOLICY
SHOW LMFADDRCHOICEPOLICY|LMF地址类型选择策略配置
GMLC地址池配置|ADD GMLCLOCALADDRPOOL
DEL GMLCLOCALADDRPOOL|GMLC地址池配置
SHOW GMLCLOCALADDRPOOL|GMLC地址池配置
GMLC节点配置|ADD GMLCNODECONFIG
SET GMLCNODECONFIG|GMLC节点配置
DEL GMLCNODECONFIG|GMLC节点配置
SHOW GMLCNODECONFIG|GMLC节点配置
发现LMF参数配置|SET LMFDISCOPARA
SHOW LMFDISCOPARA|发现LMF参数配置
发现GMLC参数配置|SET GMLCDISCOPARA
SHOW GMLCDISCOPARA|发现GMLC参数配置
GMLC分析配置|ADD GMLCANALYCFG
SET GMLCANALYCFG|GMLC分析配置
DEL GMLCANALYCFG|GMLC分析配置
SHOW GMLCANALYCFG|GMLC分析配置
LMF控制策略配置|ADD LMFCONTROLPOLICYCFG
SET LMFCONTROLPOLICYCFG|LMF控制策略配置
DEL LMFCONTROLPOLICYCFG|LMF控制策略配置
SHOW LMFCONTROLPOLICYCFG|LMF控制策略配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :如果启用LCS功能，需开启license（uMAC_AMF_7232），并通过SET LCSSWITCH命令打开定位功能开关。由于默认的LMF发现模式为本地策略，可通过ADD LMFNODECFG、ADD LMFLOCALADDRPOOL命令配置目标LMF地址，通过SET LMFADDRCHOICEPOLICY命令修改地址类型（默认IPV4）。 
如果启用紧急呼叫，AMF主动上报终端的位置信息功能，需通过SET LCSSWITCH命令打开定位功能开关和紧急上报开关。由于默认的GMLC发现模式为本地策略，还需通过ADD GMLCNODECONFIG、ADD GMLCLOCALADDRPOOL命令配置目标GMLC地址。 
如果网络侧触发定位请求（MT-LR），请求上报位置信息，需通过SET LCSSWITCH命令打开定位功能开关。由于默认的LMF发现模式为本地策略，还需通过ADD LMFNODECFG、ADD LMFLOCALADDRPOOL命令配置目标LMF地址。 
如果UDM发起获取位置信息请求，AMF在获取位置信息后返回给UDM，需通过SET LCSSWITCH命令打开定位功能开关。 
如果终端发起定位请求（MO-LR），AMF根据UE请求与LMF交互完成定位或辅助数据下发，或将位置信息转发给GMLC，需通过SET LCSSWITCH命令打开定位功能开关和定位协议开关。由于默认的LMF和GMLC发现模式为本地策略，需通过ADD LMFNODECFG、ADD LMFLOCALADDRPOOL命令配置目标LMF地址。若需要转发第三方，则还需通过ADD GMLCNODECONFIG、ADD GMLCLOCALADDRPOOL命令配置目标GMLC地址。 
如果网络侧触发定位请求（MT-LR），请求上报位置信息，并支持延时定位（Deferred MT-LR）UE可用事件类型（UE Available Location Event），则AMF等待UE可用后上报位置信息给GMLC，需通过SET LCSSWITCH命令打开定位功能开关和延迟定位开关。由于默认的LMF和GMLC发现模式为本地策略，需通过ADD LMFNODECFG、ADD LMFLOCALADDRPOOL命令配置目标LMF地址，通过ADD GMLCNODECONFIG、ADD GMLCLOCALADDRPOOL命令配置目标GMLC地址。 
配置前提 :AMF网元运行正常。 
已部署Namf_Location服务。 
已启用License（AMF支持LCS功能）。 
配置过程 :###### MT-LR流程（有NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET GMLCAUTHCFG]命令，修改GMLC授权状态。
（可选）执行[ADD LMFCONTROLPOLICYCFG]命令，新增LMF控制策略配置。
###### MT-LR流程（无NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
（可选）执行[SET LCSDISCOMODE]命令，修改发现模式配置。
执行[ADD LMFNODECFG]命令，新增 LMF节点。
执行[ADD LMFLOCALADDRPOOL]命令，增加LMF地址池配置。
执行[SET LMFADDRCHOICEPOLICY]命令，修改LMF地址选择策略配置。
（可选）执行[ADD LMFCONTROLPOLICYCFG]命令，新增LMF控制策略配置。
###### NI-LR流程（有NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
###### NI-LR流程（无NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
执行[ADD GMLCNODECONFIG]命令，新增 GMLC节点。
执行[ADD GMLCLOCALADDRPOOL]命令，增加GMLC地址池配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
（可选）执行[ADD LMFNODECFG]命令，新增 LMF节点。
（可选）执行[ADD LMFLOCALADDRPOOL]命令，增加LMF地址池配置。
（可选）执行[SET LMFADDRCHOICEPOLICY]命令，修改LMF地址选择策略配置。
###### ProvideLocationInfo流程 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
###### MO-LR流程（有NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET LMFDISCOPARA]命令，修改 发现LMF携带的位置信息参数配置。
（可选）执行[SET GMLCDISCOPARA]命令，修改 发现GMLC携带的位置信息参数配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
（可选）执行[SET AMFCHRFUNC]命令，修改 EMS+日志上报功能 LCS配置。
（可选）执行[ADD GMLCANALYCFG]命令，新增GMLC的分析配置。
（可选）执行[SET OLINPUTN2SRVCFG]命令，修改流程中N2接口入向业务消息最大通过量和权重配置。
（可选）执行[SET LCSSWITCH]命令，修改注册是否携带GMLC信息、 MO-LR是否检查签约或定位服务质量类别配置。
###### MO-LR流程（无NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关配置。
（可选）执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
执行[ADD LMFNODECFG]命令，新增 LMF节点。
执行[ADD LMFLOCALADDRPOOL]命令，增加LMF地址池配置。
执行[ADD GMLCNODECONFIG]命令，新增 GMLC节点。
执行[ADD GMLCLOCALADDRPOOL]命令，增加GMLC地址池配置。
（可选）执行[SET LMFADDRCHOICEPOLICY]命令，修改LMF地址选择策略配置。
（可选）执行[SET AMFCHRFUNC]命令，修改 EMS+日志上报功能 LCS配置。
（可选）执行[ADD GMLCANALYCFG]命令，新增GMLC的分析配置。
（可选）执行[SET OLINPUTN2SRVCFG]命令，修改流程中N2接口入向业务消息最大通过量和权重配置。
（可选）执行[SET LCSSWITCH]命令，修改注册是否携带GMLC信息、 MO-LR是否检查签约或定位服务质量类别配置。
###### Deferred MT-LR（UE Available Location Event）流程（有NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关和延时定位开关配置。
执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET GMLCAUTHCFG]命令，修改GMLC授权状态。
（可选）执行[SET LMFDISCOPARA]命令，修改 发现LMF携带的位置信息参数配置。
（可选）执行[SET GMLCDISCOPARA]命令，修改 发现GMLC携带的位置信息参数配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
（可选）执行[SET AMFCHRFUNC]命令，修改 EMS+日志上报功能 LCS配置。
###### Deferred MT-LR（UE Available Location Event）流程（无NRF） 
执行[SET LCSSWITCH]命令，修改 LCS定位开关和延时定位开关配置。
（可选）执行[SET LCSDISCOMODE]命令，修改发现模式配置。
（可选）执行[SET LCSFUNCTION]命令，修改 LCS定位功能配置。
执行[ADD LMFNODECFG]命令，新增 LMF节点。
执行[ADD LMFLOCALADDRPOOL]命令，增加LMF地址池配置。
执行[ADD GMLCNODECONFIG]命令，新增 GMLC节点。
执行[ADD GMLCLOCALADDRPOOL]命令，增加GMLC地址池配置。
（可选）执行[SET LMFADDRCHOICEPOLICY]命令，修改LMF地址选择策略配置。
（可选）执行[SET AMFCHRFUNC]命令，修改 EMS+日志上报功能 LCS配置。
配置实例 :场景一 :场景说明
紧急呼叫时，AMF主动上报终端的位置信息。 
数据规划
配置项|参数|取值
---|---|---
LCSSWITCH配置|是否启用定位功能|YES
是否启用紧急呼叫主动上报|LCSSWITCH配置|YES
发现模式配置|LMF发现模式|NRF发现
GMLC发现模式|发现模式配置|NRF发现
LCSFUNCTION配置|紧急呼叫是否主动向LMF获取位置|NO
是否携带位置qos|LCSFUNCTION配置|NO
水平精度|LCSFUNCTION配置|65535
响应时间|LCSFUNCTION配置|低
是否获取垂直精度|LCSFUNCTION配置|NO
垂直精度|LCSFUNCTION配置|65535
定位优先级|LCSFUNCTION配置|低
是否获取速度|LCSFUNCTION配置|NO
是否携带GAD参数|LCSFUNCTION配置|NO
支持的GAD形状|LCSFUNCTION配置|POINT
配置步骤
步骤|说明|操作
---|---|---
1|开启LCS定位开关和紧急呼叫主动上报开关。|SET LCSSWITCH:SWITCHLOCATION="YES",ESSWITCH="YES"
2|配置GMLC发现模式为NRF发现。|SET LCSDISCOMODE:LMFDISCOVERYMODE="NRF_DISCOVERY",GMLCDISCOVERYMODE="NRF_DISCOVERY"
3|配置紧急呼叫上报消息参数。|SET LCSFUNCTION:ELMFSWITCH="NO",LQOSSWITCH="NO",HACCURACY=1,RESPONSETIME="LOW_DELAY",VERTREQUESTED="NO",LCSPRIORITY="NORMAL_PRIORITY",VELOCITYREQUESTED="VELOCITY_IS_NOT_REQUESTED",SHAPESWITCH="YES",SUPPORTGADSHAPE="POINT"
场景二 :场景说明
紧急呼叫时，AMF接收GLMC发起的对终端的位置信息查询消息。 
普通场景（非紧急呼叫）时，AMF接收GLMC发起的对终端的位置信息查询消息。 
数据规划
配置项|参数|取值
---|---|---
LCSSWITCH配置|是否启用定位功能|YES
是否启用紧急呼叫主动上报|LCSSWITCH配置|NO
发现模式配置|LMF发现模式|NRF发现
GMLC发现模式|发现模式配置|本地配置
配置步骤
步骤|说明|操作
---|---|---
1|开启LCS定位开关。|SET LCSSWITCH:SWITCHLOCATION="YES"
2|配置LMF发现模式为NRF发现。|SET LCSDISCOMODE:LMFDISCOVERYMODE="NRF_DISCOVERY"
场景三 :场景说明
在位置相关的业务中，UDM向AMF查询终端的当前位置信息。 
数据规划
配置项|参数|取值
---|---|---
LCSSWITCH配置|是否启用定位功能|YES
是否启用紧急呼叫主动上报|LCSSWITCH配置|NO
配置步骤
步骤|说明|操作
---|---|---
1|开启LCS定位开关。|SET LCSSWITCH:SWITCHLOCATION="YES"
###### 场景四 
场景说明
在位置相关的业务中，UE向AMF发起定位会话、请求位置辅助数据或者转发位置信息给LCS客户端或者AF。 
数据规划
配置项|参数|取值
---|---|---
LCSSWITCH配置|是否启用定位功能|YES
是否启用定位协议开关|LCSSWITCH配置|YES
注册是否携带GMLC信息|LCSSWITCH配置|YES
定位请求是否携带UE能力参数|LCSSWITCH配置|YES
发现模式配置|LMF发现模式|NRF发现
GMLC发现模式|发现模式配置|本地配置
配置步骤
步骤|说明|操作
---|---|---
1|开启LCS定位开关、定位协议开关，设置注册携带GMLC信息、定位请求携带UE能力参数。|SET LCSSWITCH:SWITCHLOCATION="YES",FIVEGLCSSWITCH="YES",REGISTGMLC="YES",UELCSCAPABILITY="YES"
2|配置LMF发现模式为NRF发现。|SET LCSDISCOMODE:LMFDISCOVERYMODE="NRF_DISCOVERY"
###### 场景五 
场景说明
在位置相关的业务中，AMF接收GMLC发起的对终端的位置信息的查询消息，AMF支持延时定位请求，当UE当前不可达时，AMF等待UE直到可达后继续后续的定位流程。 
数据规划
配置项|参数|取值
---|---|---
LCSSWITCH配置|是否启用定位功能|YES
是否启用延迟定位开关|LCSSWITCH配置|YES
发现模式配置|LMF发现模式|NRF发现
GMLC发现模式|发现模式配置|本地配置
配置步骤
步骤|说明|操作
---|---|---
1|开启LCS定位开关和延迟定位开关。|SET LCSSWITCH:SWITCHLOCATION="YES",DEFERREDLCS="YES"
2|配置LMF发现模式为NRF发现。|SET LCSDISCOMODE:LMFDISCOVERYMODE="NRF_DISCOVERY"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|紧急呼叫时（无NRF发现），AMF主动上报终端的位置信息（NI-LR）
---|---
测试目的|AMF在紧急会话建立时，发起NI-LR流程通知GMLC建立紧急会话。AMF在紧急会话释放时，通知GMLC释放紧急会话。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关和“是否启用紧急呼叫主动上报”开关）已打开。本地配置LMF地址。本地配置GMLC地址。
测试过程|UE执行紧急注册及紧急呼叫建立流程。Namf_Communication服务向Namf_Location服务发送通知紧急呼叫建立（Emergency Session Setup Notify）消息，在消息中携带用户标识SUPI/PEI、用户当前的位置NCGI。Namf_Location服务接收到Emergency Session Setup Notify消息后，生成LcsCorrelationID（即LCS Correlation ID）参数，选择LMF，并向此LMF发送Nlmf_Location_DetermineLocation Request消息用于获取UE详细位置信息，在消息中携带SUPI/PEI、NCGI、externalClientType=EMERGENCY_SERVICES、LcsCorrelationID及amfId等参数。LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位。定位完成后，LMF向Namf_Location服务发送定位响应消息，携带相关位置参数。Namf_Location服务获得LMF应答后，执行GMLC选择，向选定的GMLC发送Namf_Location_EventNotify Request消息，在消息中携带locationEvent=EMERGENCY_CALL_ORIGINATION、SUPI/PEI、NCGI等参数。GLMC接收消息后，返回Namf_Location_EventNotify Response消息。某一时刻，紧急呼叫释放，Namf_Communication在紧急PDUSession释放后，向Namf_Location服务发送通知紧急呼叫释放（Emergency Session Release Notify）消息，在消息中携带用户标识SUPI/PEI。Namf_Location服务，根据SUPI/PEI查询用户上下文，获取GMLC信息，向GMLC发送Namf_Location_EventNotify Request消息，在消息中携带locationEvent = EMERGENCY_CALL_RELEASE、SUPI/PEI等参数。GLMC接收消息后，给AMF返回Namf_Location_EventNotify Response消息。
通过准则|AMF向GMLC发送Namf_Location_EventNotify Request消息，消息携带内容为LMF返回的定位信息等，并收到Namf_Location_EventNotify Response成功消息。
测试结果|AMF向GMLC发送Namf_Location_EventNotify Request消息，消息携带内容为LMF返回的定位信息等，并收到Namf_Location_EventNotify Response成功消息。
测试项目|普通场景时（NRF发现），AMF接收GMLC发起的对终端UE的位置查询（MT-LR）
---|---
测试目的|GMLC根据NEF、AF以及LCS Client等要求发起对UE的定位请求，AMF根据请求向LMF发起确定位置请求，LMF继续对UE进行定位信息获取并给AMF返回响应，最终AMF将位置信息返回给GMLC，供定位发起者进一步使用。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关）已打开。本地配置LMF地址。
测试过程|AMF收到GMLC的Namf_Location_ProvidePositioningInfo请求消息。UE处于CONNECTED态，AMF向RAN发送Location Reporting Control消息携带direct标记，在获得RAN的响应后，从响应消息中获取位置信息。AMF向选定的LMF发送Nlmf_Location_DetermineLocation请求确定UE位置信息。定位完成后，LMF向AMF发送定位响应消息。AMF向保存的GMLC发送Namf_Location_ProvidePositioningInfo响应消息，消息中各参数取值根据LMF返回的数据进行填写。
通过准则|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试结果|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试项目|普通场景时（NRF发现），AMF接收GMLC发起的对终端UE的位置查询（MT-LR）
---|---
测试目的|GMLC根据NEF、AF以及LCS Client等要求发起对UE的定位请求，AMF根据请求向LMF发起确定位置请求，LMF继续对UE进行定位信息获取并给AMF返回响应，最终AMF将位置信息返回给GMLC，供定位发起者进一步使用。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关）已打开。执行SET LCSDISCOMODE命令，修改发现模式配置为NRF发现。
测试过程|AMF收到GMLC的Namf_Location_ProvidePositioningInfo请求消息。UE处于CONNECTED态，AMF向RAN发送Location Reporting Control消息携带direct标记，在获得RAN的响应后，从响应消息中获取位置信息。AMF向NRF返回的LMF发送Nlmf_Location_DetermineLocation请求确定UE位置信息。定位完成后，LMF向AMF发送定位响应消息。AMF向保存的GMLC发送Namf_Location_ProvidePositioningInfo响应消息，消息中各参数取值根据LMF返回的数据进行填写。
通过准则|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试结果|AMF向GMLC返回成功响应消息，消息携带内容为LMF返回响应的内容。
测试项目|终端发起定位（NRF发现），获取位置信息并转发给GMLC（MO-LR转发第三方）
---|---
测试目的|AMF接收UE的定位请求后，根据UE请求与LMF交互完成定位，并将位置信息转发给GMLC。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关和“是否启用定位协议开关”）已打开。执行SET LCSDISCOMODE命令，修改发现模式配置为NRF发现。
测试过程|UE主动发起MO-LR流程，通过UL NAS TRANSPORT消息携带MO-LR请求给AMF。Namf_Communication服务接收消息后，向UDM获取LCS Mobile Originated data签约数据，检查UE签约。AMF启动MO-LR的处理，携带参数向Namf_Location服务发送MO-LR请求消息，携带NCGI等相关参数。Namf_Location服务接收请求后，创建定位上下文，生成定位关联ID（即LCS Correlation ID）参数，保存MO-LR请求参数。Namf_Location服务实例执行LMF发现和选择，并向LMF发送Nlmf_Location_DetermineLocation请求消息，填写SUPI/PEI，NCGI，LcsCorrelationID及amfId参数，携带UeLocationServiceInd（LOCATION_ESTIMATE或LOCATION_ASSISTANCE_DATA）参数。LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位。定位完成后，LMF向Namf_Location服务发送定位响应消息。Namf_Location服务实例根据MO-LR请求类型，若需要通知GMLC，Namf_Location服务实例执行GMLC选择，向GMLC发送Ngmlc_Location_LocationUpdate消息。GLMC接收消息后，返回响应。Namf_Location服务给Namf_Communication服务发送MO-LR响应。Namf_Communication服务根据响应消息，给UE发送DL NAS TRANSPORT携带响应，完成处理。
通过准则|AMF向GMLC发送Ngmlc_Location_LocationUpdate消息，消息携带内容为LMF返回响应的内容，收到GMLC返回的成功响应，并成功给UE发送DL NAS TRANSPORT消息完成后续处理。
测试结果|AMF向GMLC发送Ngmlc_Location_LocationUpdate消息，消息携带内容为LMF返回响应的内容，收到GMLC返回的成功响应，并成功给UE发送DL NAS TRANSPORT消息完成后续处理。
测试项目|延迟定位（UE可用事件）（NRF发现）时，AMF接收GMLC发起的对终端可用后的延迟定位请求消息（Deferred MT-LR）
---|---
测试目的|AMF在MT-LR流程中，接收GMLC的延迟定位请求（UE可用事件类型）并在UE可用后，AMF与LMF交互完成定位，最终将定位结果返回给GMLC。
预置条件|AMF网元正常。License（“AMF支持LCS功能”）有效。LCS功能开关（“是否启用定位功能”开关和“是否启用延迟定位开关”）已打开。执行SET LCSDISCOMODE命令，修改发现模式配置为NRF发现。
测试过程|GMLC向Namf_Location服务发送Namf_Location_ProvidePositioningInfo请求消息，携带SUPI等参数，LdrType指示为UE_AVAILABLE定位事件。Namf_Location服务接收定位请求后，向Namf_Communication服务请求UE当前的NCGI，并携带UE可用事件指示。Namf_Communication服务接收请求后，判断UE不可用。Namf_Communication服务设置UE可用事件标记。Namf_Communication服务给Namf_Location服务回送响应消息，指示UE当前不可用。某时刻，UE可用。Namf_Communication服务向Namf_Location服务发送消息指示UE可用，并携带NCGI等参数。Namf_Location服务接收指示消息后，回送响应。Namf_Communication服务接收响应消息后，清除UE可用事件标记。Namf_Location服务执行LMF发现和选择，并向LMF发送Nlmf_Location_DetermineLocation请求消息，填写SUPI/PEI，NCGI，LcsCorrelationID及amfId等参数。LMF通过Namf_Communication服务发起向UE或NG-RAN的定位流程并完成定位。定位完成后，LMF向Namf_Location服务发送定位响应消息。Namf_Location服务给GMLC发送Namf_Location_EventNotify消息，填写SUPI/PEI，locationEvent = ACTIVATION_OF_DEFERRED_LOCATION等参数。AMF接收GLMC响应完成处理。
通过准则|AMF向GMLC发送Namf_Location_EventNotify消息，消息携带内容为LMF返回响应的内容，并收到GMLC返回的成功响应。
测试结果|AMF向GMLC发送Namf_Location_EventNotify消息，消息携带内容为LMF返回响应的内容，并收到GMLC返回的成功响应。
常见问题处理 :无 
# 缩略语 
# 缩略语 
AMF :Access and Mobility Management Function接入和移动管理功能
## AN 
Access Network接入网
DNN :Data Network Name数据网名称
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
## LADN 
Local Area Data Network局域数据网
## LCS 
LoCation Services定位业务
## LMF 
Location Management Function定位管理功能
## MO-LR 
Mobile Originating Location Request移动台发起位置请求/移动发起定位请求
NF :Network Function网络功能
PDU :Packet Data Unit分组数据单元
## PEI 
Permanent Equipment Identifier永久设备标识
SMF :Session Management Function会话管理功能
SUPI :Subscriber Permanent Identifier用户永久标识
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
UPF :User Plane Function用户平面功能
# ZUF-79-17 AMF负荷控制、拥塞及过负荷控制 
## ZUF-79-17-001 AMF负载均衡 
特性描述 :特性描述 :术语 :术语|含义
---|---
AMF Region|一个AMF Region由一个或多个AMF Set组成
AMF Set|一个AMF Set由多个为相同区域和网络切片提供服务的AMF组成。AMF Set内的AMF为区域内的UE提供服务，共同分担区域内所有UE的业务处理。UE在AMF Set所服务的区域间移动不需要改变服务AMF
AMF Pointer|用于区分AMF Set内的不同AMF的一个标识
GUAMI|Globally Unique AMF ID的缩写，全局唯一的AMF标识，GUAMI由MCC，MNC，AMF Region ID，AMF Set ID以及AMF Pointer共同标识，即<GUAMI> = <MCC> <MNC> <AMF Region ID> <AMF Set ID> <AMF Pointer>
描述 :定义 :AMF Set是指UE在其间移动而不需要改变服务AMF的区域。一个AMF Set由多个同质的AMF组成，AMF Set内的AMF为区域内的UE提供服务，共同分担区域内所有UE的业务处理。区域内的gNB与AMF Set内的所有AMF均进行互联。
负载均衡是指gNB将UE及其话务根据AMF Set内各AMF的容量权重而负荷分担到各AMF上，以实现话务在AMF之间均衡分布。 
背景知识 :为提高系统可靠性，核心网的业务处理通常需要提供NF冗余机制。 
在4G时代，通过MME POOL实现了MME的负载均衡，负载重平衡以及MME的容灾功能。
对于5G时代的AMF，AMF Set实现的功能与4G基本一致，通过AMF Set实现了AMF的负载均衡，负载重平衡以及AMF的容灾功能。 
应用场景 :AMF Set是5G核心网的重要功能，通常情况下，一个无线连续覆盖的区域，例如多个邻近地区或城市组成的区域，可以组建AMF Set提供网络服务。负载均衡由gNodeB在AMF Set内的各AMF之间执行。 
客户收益 :受益方|受益描述
---|---
运营商|支持负载均衡功能，可以使用户在AMF之间均衡分布，进而有效提高系统运行可靠性，降低系统运行风险。
移动用户|为用户提供更好的网络服务，获得更好的用户满意度。
实现原理 :系统架构 :AMF负载均衡在gNodeB与AMF Set内的各AMF之间执行，网络架构如[图1]所示。
图1  系统架构

涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立用户面会话资源等操作
PCF|为AMF提供接入及移动性管理等用户策略服务
UDSF|为AMF提供非结构化数据的统一数据存储，如保存用户上下文数据
UDM|提供用户及会话相关的签约信息
AUSF|提供用户鉴权服务
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现，NF状态订阅等功能
NSSF|为AMF提供切片选择服务
gNodeB|UE接入时，提供无线资源及承载
协议栈 :接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
本NF/网元实现 :网元|作用
---|---
AMF|向gNodeB下发本AMF的Served GUAMI和权重因子
gNodeB|根据AMF Set内各AMF的权重因子，负荷分担的选择AMF
业务流程 :AMF权重因子下发 
图2  AMF权重因子下发

流程说明： 
AMF收到gNodeB发送的N2 SETUP REQUEST消息。 
AMF根据配置获取Served GUAMI和Relative AMF Capacity参数取值，向gNodeB发送N2
SETUP RESPONSE消息，其中携带Served GUAMI和Relative AMF Capacity参数。gNodeB保存当前AMF的GUAMI和权重因子。 
AMF配置更新
图3  AMF配置更新

流程说明： 
配置中AMF的Relative AMF Capacity发生变更，AMF向全部与本AMF已建立N2连接的gNodeB发送AMF
CONFIGURATION UPDATE消息，其中携带了更新后的Relative AMF Capacity。 
gNodeB更新保存AMF的Relative AMF Capacity，向AMF回AMF CONFIGURATION
UPDATE ACKNOWLEDGE消息进行确认。 
负载均衡
图4  负载均衡

由gNodeB实现AMF Set内各AMF的负载均衡。如gNodeB在UE发起的初始注册流程中，执行AMF选择，根据当前可用的AMF列表以及保存的各AMF的权重因子，将用户的注册请求负荷分担给AMF
Set内的各个AMF。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.19.3 AMF Load Balancing
3GPP TS 38.413（NG Application Protocol）|9.2.6.2 NG SETUP RESPONSE
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布
License要求 :该特性为的基本特性，无需License支持。 
对其他网元的要求 :NR|SMF|PCF|UDM
---|---|---|---
√|-|-|-
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :该特性不涉及。 
特性配置 :该功能属于基本功能，无需特别配置，只要完成初始配置即可。 
## ZUF-79-17-002 AMF负载重平衡 
特性描述 :特性描述 :术语 :术语|含义
---|---
AMF Region|一个AMF Region由一个或多个AMF Set组成。
AMF Set|一个AMF Set由多个为相同区域和网络切片提供服务的AMF组成。AMF Set内的AMF为区域内的UE提供服务，共同分担区域内所有UE的业务处理。UE在AMF Set所服务的区域间移动不需要改变服务AMF。
AMF Pointer|用于区分AMF Set内的不同AMF的一个标识。
GUAMI|Globally Unique AMF ID的缩写，全局唯一的AMF标识，GUAMI由MCC，MNC，AMF Region ID，AMF Set ID以及AMF Pointer共同标识，即<GUAMI> = <MCC> <MNC> <AMF Region ID> <AMF Set ID> <AMF Pointer>。
描述 :定义 :AMF Set是指UE在其间移动而不需要改变服务AMF的区域。一个AMF Set由多个同质的AMF组成，AMF Set内的AMF为区域内的UE提供服务，共同分担区域内所有UE的业务处理。区域内的gNB与AMF Set内的所有AMF均进行互联。 
负载重平衡是指将某个AMF的用户向Set内其他AMF进行迁移的过程，从而减少此AMF上的用户数，以便实现降低此AMF的负载，进而实现AMF Set内各AMF负载的重新平衡。 
ZXUN uMAC-AMF支持两种方式负载重平衡： 
被动负载重平衡该负载重平衡方式下，AMF首先通知RAN侧和NRF，本AMF退出服务。后续用户发起业务时，RAN侧会将该用户引导到Set内其他AMF上。至于用户何时迁移到Set内的其他AMF，依赖于用户何时发起业务。因此，整个负载重平衡的进度完全依赖于用户的业务行为，AMF无法控制整个进程。 
主动负载重平衡该负载重平衡方式下，整个重平衡过程被分为了两个阶段：第一阶段，依赖于用户业务触发用户迁移。第二阶段，AMF主动扫描本局上还存在的用户，并主动触发用户签约。相比较被动负载重平衡，主动负载重平衡由于添加了AMF主动触发用户迁移功能，因此整个重平衡进程进度可以控制，时间可以预期，因此非常适合升级等场景。 
指定AMF卸载通过指定AMF卸载功能，可以将AMF上的某个用户卸载到指定的AMF上。 
ZXUN uMAC-AMF支持通过操作维护人机界面，启动或终止主动负载重平衡，或者查询负载重平衡执行进度。如果期望AMF在负载重平衡流程结束后，仍旧能够分担用户，则必须在负载重平衡启动命令后，至少执行一次负载重平衡停止命令。 
背景知识 :为提高系统可靠性，核心网的业务处理通常需要提供NF冗余机制。在4G时代，通过MME POOL实现了MME的负载均衡，负载重平衡以及MME的容灾功能。对于5G时代的AMF，AMF Set实现的功能与4G基本一致，通过AMF Set实现了AMF的负载均衡，负载重平衡以及AMF的容灾功能。主要区别是： 
5G的AMF与5G-RAN之间支持多SCTP偶联，在某条SCTP偶联故障中断后，AMF与5G-RAN之间的话务可以通过其余正常的SCTP偶联继续处理，从而避免了因SCTP偶联断链而造成的用户释放和业务失败。 
5G的系统架构设计实现了计算与存储分离，对于AMF处理的用户上下文状态数据保存到了UDSF中，在AMF故障后，可以由AMF Set内的其他AMF从UDSF获取用户上下文状态数据并继续处理用户业务，从而获得了较4G时代更好的容灾效果，用户的业务处理在AMF故障后得以继续处理，从而提高了用户感知和用户体验，为运营商能够提供更优质的网络服务提供了系统实现。 
应用场景 :AMF负载重平衡功能，其适用及应用场景包括： 
在日常维护工作中，在某AMF负荷畸高时，提供将该AMF的负荷有效降低方法，从而避免特殊场景或短时话务高峰对AMF的稳定性造成冲击，从而保障网络运行稳定，为用户提供可靠服务。 
在计划性维护之前（如升级，缩扩容等操作），需要将AMF的注册用户及话务迁移到AMF Set内的其他AMF上，再对AMF进行维护操作，从而避免维护工作对网络和用户业务造成不必要的影响，保障网络服务持续提供，提高用户体验。 
升级后测试验证时，将测试用户指定卸载到已执行升级操作的AMF上，以进行业务验证。 
客户收益 :受益方|受益描述
---|---
运营商|通过AMF Set内负载重平衡功能，可以将负荷较高的AMF的负荷降低。也可以在计划性维护前，将AMF平滑的退出服务状态，从而有利于网络服务能力的稳定提供，有利于改善和增强用户体验，提高用户粘性，进而提高运营商运营收入。
移动用户|在对应的应用场景中，可以为用户继续提供服务，有利于为用户提供更好的业务感受。
实现原理 :系统架构 :AMF负载重平衡由AMF Set内的某AMF发起，其中gNodeB，AMF，SMF，PCF，UDM配合完成负载重平衡的过程，其系统架构如[图1]所示。
图1  系统架构

涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等操作
UDM|提供用户及会话相关的签约信息
AUSF|提供用户鉴权服务
PCF|为AMF提供接入及移动性管理等用户策略服务
UDSF|为AMF提供非结构化数据的统一数据存储，如保存用户上下文数据
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现，NF状态订阅等功能
NSSF|为AMF提供切片选择服务
gNodeB|UE接入时，提供无线资源及承载
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N12|ZUF-79-19-005 N12
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15
N18|ZUF-79-19-011 N18
N22|ZUF-79-19-008 N22
本NF/网元实现 :网元|作用
---|---
AMF|被动负载重平衡时，AMF执行如下功能：向gNodeB下发本AMF的Served GUAMI和权重因子Relative AMF Capacity。在负载重平衡过程中，向gNodeB下发AMF STATUS INDICATION消息，指示不可用GUAMI列表；在无UDSF场景中，同时携带backup AMF Name给gNodeB。将用户上下文状态数据保存到UDSF（有UDSF场景）或为其备份的AMF（无UDSF场景）上。无UDSF场景下，备份AMF将其作为备份的GUAMI通过NF注册流程携带给NRF。主动负载重平衡时，AMF执行如下功能：负载重平衡启动时，开关控制是否通知gNodeB，本AMF权重因子为0。重平衡第一阶段，用户活动时，在业务执行完成后，通知UE重新注册。重平衡第二阶段，开始扫描用户并逐一通知UE重新注册。启动重平衡卸载优化，控制第一阶段和第二阶段用户卸载的速率。指定AMF卸载时，AMF执行如下功能：根据卸载指令，首先触发指定用户网络侧去注册并携带重注册指示，后续用户重新初始注册时，通过AMF重选过程将用户转移到指定AMF上。
NRF|在无UDSF场景下，保存备份AMF携带的备份GUAMI信息。在其他NF携带GUAMI执行NF发现流程中，将对应的AMF通过响应消息返回给NF。
SMF|有UDSF场景，在AMF故障后，将故障AMF服务用户的业务报文发送给此AMF Set内的其他AMF，并继续处理业务流程。无UDSF场景，在AMF故障后，通过NRF获取到其备份AMF后，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
PCF|有UDSF场景，在AMF故障后，将故障AMF服务用户的业务报文发送给此AMF Set内的其他AMF，并继续处理业务流程。无UDSF场景，在AMF故障后，通过NRF获取到其备份AMF后，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
UDM|有UDSF场景，在AMF故障后，将故障AMF服务用户的业务报文发送给此AMF Set内的其他AMF，并继续处理业务流程。无UDSF场景，在AMF故障后，通过NRF获取到其备份AMF后，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
gNodeB|实现AMF选择功能，即根据UE提供的信息选择UE当前服务的AMF。在UE没有提供服务AMF信息，或服务AMF不可用时，根据AMF Set内各AMF的权重因子，选择AMF。在服务AMF不可用且存在backup AMF Name时，选择backup AMF。
业务流程 :被动负载重平衡的业务流程
被动负载重平衡的业务流程如[图2]所示。
图2  负载重平衡

流程说明： 
原AMF发起负荷重平衡过程，向gNodeB发送AMF STATUS INDICATION消息，携带Unavailable GUAMI，可选的携带Backup AMF Name（无UDSF场景，携带为其备份的backup AMF）。 
原AMF根据负荷重平衡的类型（话务部分迁移或话务完全迁移），向NRF发送更新（部分迁移方式）或去注册（完全迁移方式）消息。 
NRF接收AMF发送的更新消息或去注册消息，处理并根据AMF状态订阅列表，向订阅了AMF状态的其他NF如SMF发送AMF状态变更通知。 
gNodeB及NF记录此AMF的状态及不可用的GUAMI列表，后续对此GUAMI选择其他AMF继续业务处理流程。 
gNodeB对于后续UE指向原AMF的请求消息，gNodeB将为其选择新AMF进行业务处理。有UDSF场景，gNodeB在AMF Set内根据权重选择一个AMF发送；无UDSF场景，gNodeB根据Backup AMF Name参数为其选择Backup AMF进行发送。 
新AMF接收gNodeB发送的UE消息后，获取用户上下文状态数据（有UDSF场景从UDSF获取，无UDSF场景自身已保存），为此用户继续处理相关业务流程，如与SMF进行流程交互并更新AMF信息。 
新AMF为用户分配新5G-GUTI，并执行AMF UE NGAP ID的更新流程，后续此用户迁移到新AMF，其业务由新AMF进行处理。 
主动负载重平衡的业务流程
主动负载重平衡的业务流程如[图3]所示。
图3  主动负载重平衡业务流程

流程说明： 
AMF1通过EMS发起主动负载重平衡命令，命令中设置是否通知gNodeB更新AMF权重、卸载类型、预处理时长等参数。卸载类型用于指示AMF卸载本AMF上用户的范围，目前支持全量卸载、指定SUPI/GPSI号段卸载、指定用户数卸载、指定保留用户比例卸载四种卸载类型。四种卸载类型下，负载重平衡停止的条件为： 
全量卸载：用户全部卸载完毕，或者AMF1通过操作维护界面主动停止卸载过程。 
指定SUPI/GPSI号段卸载：指定号段下全部用户卸载成功，或者AMF1通过操作维护界面主动停止卸载过程。 
指定用户数卸载：卸载用户数达到指定用户数量，或者AMF1通过操作维护界面主动停止卸载过程。 
指定保留用户比例卸载：负载重平衡命令启动时，AMF1首先根据命令中的指定保留用户比例，计算需要卸载的用户数量。当卸载用户数达到该数量或者AMF1通过操作维护界面主动停止卸载过程时，终止负载重平衡过程。 
若重平衡命令中，指示需要通知gNodeB更新AMF权重，则下发AMF Configuration Update给gNodeB，携带值为0的Relative AMF Capacity。AMF启动预处理定时器，进入负荷重平衡第一次阶段。 
在预处理定时器超时之前，用户主动触发信令业务到原AMF，比如注册、业务请求等（不包括去注册流程）。 
信令业务流程成功之后，下发Configuration update command给UE，携带RED标记，通知UE重新注册。 
UE收到重注册请求消息后，触发移动性注册更新请求且在AS层不携带5G-S-TMSI或GUAMI，注册更新消息通过gNodeB分发给AMF2。 
AMF2通过N14接口从AMF1获取用户上下文，完成注册更新过程，从而达到用户从AMF1迁移到AMF2的效果。 
在预处理定时器超时后，AMF1进入负载重平衡第二阶段，即主动开始扫描本AMF用户数据库。针对扫描到的每个用户，如果用户处于连接态，则触发Configuration update command给UE，携带RED标记，通知UE重新注册；如果是空闲态，则寻呼，寻呼成功后，同样触发Configuration update command给UE，携带RED标记，通知UE重新注册。 
UE收到重注册请求消息后，触发移动性注册更新请求且在AS层不携带5G-S-TMSI或GUAMI，注册更新消息通过gNodeB分发给AMF2。 
AMF2通过N14接口从AMF1获取用户上下文，完成注册更新过程，从而达到用户从AMF1迁移到AMF2的效果。 
重注册流程结束后，如果仍旧期望AMF1分担用户，则必须通过EMS执行负载重平衡停止命令。 
AMF1收到负载重平衡停止命令后，下发AMF Configuration Update给gNodeB，携带Relative AMF Capacity，值为AMF1本地配置。 
负荷重平衡用户卸载过程控制
AMF负荷重平衡用户卸载过程控制的流程如[图4]所示。
图4  负荷重平衡用户卸载过程控制

流程说明： 
需要启动负荷重平衡卸载优化。从OMM发起负荷重平衡过程，AMF启动令牌桶方式控制卸载速率， 以固定速率向令牌桶内投放令牌。 
AMF收到UE的注册、注册更新、业务请求等消息是卸载或者周期性扫描卸载时，触发负荷卸载前，首先获取卸载令牌。 
UE活动卸载和扫描卸载时，在获取到卸载令牌后，AMF对用户进行卸载，流程成功后，触发Configuration update command给UE，携带RED标记，通知UE重新注册。 
如果卸载时，未获取到卸载令牌，则不进行卸载。 
当卸载令牌控制周期结束后，清空剩余令牌，进入下个控制周期。 
指定AMF卸载业务流程
指定AMF卸载业务流程如[图5]所示。
图5  指定AMF卸载

流程说明如下： 
要指定卸载的UE已经注册到Initial AMF。 
操作人员通过EMS，执行指定AMF卸载动态命令，携带要卸载UE的SUPI、目标AMF的GUAMI。 
Initial AMF收到指定卸载指令，判断UE若处于空闲态，则触发寻呼流程。 
Initial AMF触发网络侧分离，并在下发给UE的去注册请求消息中携带重注册指示。 
去注册完成后，UE重新触发初始注册流程，携带5G GUTI，基站将该注册请求转到Initial AMF。 
Initial AMF根据卸载指令中的GUAMI，查找目标AMF，之后触发AMF重定向过程，将UE转移到Target AMF。 
重定向流程成功后，Initial AMF回复卸载响应消息给EMS。 
UE继续在Target AMF上，继续后续的注册流程。 
系统影响 :该特性将指定AMF的用户迁移到AMF Set内的其他AMF，迁移用户的话务将由新AMF进行处理。 
应用限制 :该特性不涉及应用限制。 
特性交互 :本特性不涉及特性交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.19.4 AMF Load Re-Balancing5.21.2 AMF Management
3GPP TS 38.413（3GPP TS 38.413）|8.7.6 AMF Status Indication9.2.6.10 AMF STATUS INDICATION
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.20|新增指定AMF卸载业务功能。
01|V7.18.10|首次发布。
License要求 :对于主动负载重平衡特性，需要申请了License许可后，运营商才能获得该特性的服务。 
主动负载重平衡特性对应的License项目为AMF支持主动重平衡功能和AMF支持无UDSF容灾部分备份功能，此两项目设置为支持，表示可以支持主动负载重平衡功能。
对其他网元的要求 :NR|NRF|SMF|PCF|UDM
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项配置项命令修改负荷重平衡优化配置SET LOADREBALANCOPT查询负荷重平衡优化配置SHOW LOADREBALANCOPT 
软件参数软件参数91 是否支持主动负载重平衡173 指定AMF卸载时等待初始注册定时器时长(秒) 
动态管理动态管理名称命令负载重平衡启动LOAD REBALANC START负载重平衡停止LOAD REBALANC STOP负载重平衡查询LOAD REBALANC QUERY主动重平衡启动ACTIVE REBALANC START主动重平衡停止ACTIVE REBALANC STOP主动重平衡查询ACTIVE REBALANC QUERY用户卸载到指定AMFUNLOADUSERTOSPECIFIEDAMF 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置过程可以完成AMF负荷重平衡优化功能，达到启动AMF主动负载重平衡时，对频繁活动用户卸载过程进行控制的目的。 
要实现对于AMF负载重平衡功能，需要申请以下License许可： 
将AMF支持主动重平衡功能（License ID：7233）的受控项打开，同时需要在软件参数中配置支持主动负载重平衡（软件参数ID：91）。 
将AMF支持无UDSF容灾部分备份功能（License ID：7223）的受控项打开，同时需要AMF配置支持容灾功能，并且容灾策略配置为无UDSF部分备份。 
配置前提 :AMF Pool环境就绪，部署了至少两套AMF并且配置了部分备份关系。 
NRF支持NF注册、订阅以及通知流程。 
AMF以及周边NF已经在NRF上完成注册、订阅操作。 
EM网管能正常连接并登录。 
配置过程 :按照AMF链式备份的配置过程设置AMF的容灾备份关系。 
AMF被动负载重平衡执行LOAD REBALANC START动态命令，设置AMF部分或者全部本局GUAMI不可用，等待不可用GUAMI下的用户主动迁走。 
AMF主动负载重平衡执行SET COMMU SOFTWARE PARAMETER:ID=91,VALUE=1命令，设置支持AMF主动负载重平衡。执行SET LOADREBALANCOPT命令，设置支持AMF负荷重平衡优化以及对负荷卸载过程进行速率控制的优化参数。执行ACTIVE REBALANC START动态命令，设置AMF进入负荷卸载状态，主动触发用户重新在他局注册。 
配置实例 :###### AMF被动负载重平衡 
场景说明
AMF Pool由AMF1和AMF2两个互备局组成，AMF1上注册的用户数远远超出了AMF2上注册的用户数，负荷严重不均。互备局AMF各自本局配置多个GUAMI用以重平衡后均衡负荷。 
数据规划
配置项|参数|取值
---|---|---
负载重平衡启动|是否更新容量权重参数|UPDATE
GUAMI ID列表|负载重平衡启动|1
配置步骤
步骤|说明|操作
---|---|---
1|启动AMF1被动负载重平衡，调整AMF权重为0，指示ID为1的本局GUAMI不可用。|LOAD REBALANC START:WEIGHTSWITCH="UPDATE",GUAMIIDLIST="1"
2|等待AMF1不可用GUAMI下用户迁移到AMF2上，负荷基本均衡后停止AMF1被动负载重平衡，恢复AMF权重以及不可用GUAMI。|LOAD REBALANC STOP
###### AMF主动负载重平衡 
场景说明
AMF Pool由AMF1和AMF2两个主备局组成，主用局AMF1即将执行升级操作，需要将用户全部迁移到备份局AMF2上。 
数据规划
配置项|参数|取值
---|---|---
设置软件参数|软参索引|91
当前参数值|设置软件参数|1
负荷重平衡优化配置|是否支持负荷卸载优化|SUPPORT
负荷卸载控制周期(s)|负荷重平衡优化配置|10
周期令牌投放次数|负荷重平衡优化配置|10
允许卸载突发系数|负荷重平衡优化配置|3
主动重平衡启动|是否更新容量权重参数|UPDATE
卸载类型|主动重平衡启动|RATE
保留用户千分比(‰)|主动重平衡启动|0
卸载步长|主动重平衡启动|50
卸载预处理时间(分钟)|主动重平衡启动|10
主动释放|主动重平衡启动|NOTACTIVERLS
配置步骤
步骤|说明|操作
---|---|---
1|配置AMF支持主动负载重平衡。|SET COMMU SOFTWARE PARAMETER:ID=91,VALUE=1
2|配置执行AMF主动负载重平衡时支持负荷重平衡优化，负荷卸载控制周期为10秒，周期令牌投放次数为10次，允许卸载突发系数为3。|SET LOADREBALANCOPT:UNLOADOPT="SUPPORT",CONTROLPERIOD=10,TOKENDELITIMES=10,BURSTCOEFFICIENT=3
3|启动AMF1主动负载重平衡，调整AMF权重为0，卸载全部用户，卸载步长为每实例1秒卸载50个用户，卸载预处理时间为10分钟，预处理阶段不主动执行AN释放。|ACTIVE REBALANC START:WEIGHTSWITCH="UPDATE",UNLOADTYPE="RATE",RESERVUSERRATE=0,UNLOADSTEP=50,PREPROCTIME=10,ACTIVERELEASE="NOTACTIVERLS"
4|查询AMF主动负载重平衡过程中的详细卸载信息，确认卸载进展。|ACTIVE REBALANC QUERY
5|等待卸载完成后停止主动负载重平衡，恢复AMF权重。|ACTIVE REBALANC STOP
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF被动负载重平衡
---|---
测试目的|验证AMF下注册的用户在其GUAMI被平衡后，后续业务能够迁移到互备局上完成。
预置条件|AMF支持无UDSF容灾部分备份功能License打开。AMF配置支持容灾功能，并且容灾策略配置为无UDSF部分备份。AMF Pool环境就绪，部署了至少两套AMF并且配置了部分备份关系。NRF支持NF注册、订阅以及通知流程。AMF以及周边NF已经在NRF上完成注册、订阅操作。EM网管能正常连接并登录。
测试过程|用户在AMF1的GUAMI1下注册并创建会话，然后释放N2连接。操作AMF1启动被动负载重平衡，指示GUAMI1不可用。SMF通过N1N2 Message Transfer请求消息尝试重新激活会话。
通过准则|SMF通过NRF发现AMF1的互备局AMF2，并将下行消息投递给AMF2。AMF2基于AMF1传递过来的部分备份信息寻呼用户。寻呼上来的用户触发业务请求，AMF2回复业务拒绝并携带隐式分离的拒绝原因值。用户在AMF2上重新注册。
测试结果|–
测试项目|AMF主动负载重平衡
---|---
测试目的|验证AMF下用户能够被主动迁移到备份局重新注册，继续完成业务。
预置条件|AMF支持无UDSF容灾部分备份功能License打开。AMF支持主动重平衡功能License打开。AMF配置支持容灾功能，并且容灾策略配置为无UDSF部分备份。AMF配置软件参数支持主动负载重平衡。AMF Pool环境就绪，部署了至少两套AMF并且配置了部分备份关系。NRF支持NF注册、订阅以及通知流程。AMF以及周边NF已经在NRF上完成注册、订阅操作。EM网管能正常连接并登录。
测试过程|用户在AMF1上注册。操作AMF1启动主动负载重平衡，卸载全量用户。
通过准则|AMF1主动寻呼用户，投递UE配置更新命令携带重注册指示。用户在AMF1的备份局AMF2上重新注册，AMF2负荷不会冲高造成拥塞。AMF1可以在15分钟内卸载完100万用户，30分钟内卸载完500万用户。
测试结果|–
常见问题处理 :无 
## ZUF-79-17-003 N2接口过载控制 
特性描述 :特性描述 :术语 :术语|含义
---|---
过负荷控制|在设备负荷过重时，通过限制接入的业务量，从而降低网元负荷，避免因负荷过高导致设备异常或崩溃。
描述 :定义 :当AMF因对输入的业务处理造成系统发生过载时，需要减少业务输入从而对系统负荷进行有效控制。 
对于N2接口，N2 Overload Control机制可以将AMF的过负荷情况告知给gNodeB，同时指示gNodeB减少某类型业务的输入。 
通过实现AMF的过负荷控制，可以有效的保障网络设备稳定、安全的运行。 
背景知识 :通常情况下，由于用户的异常行为或大量用户集中接入等情况引起的话务高峰容易造成系统设备处理过载，此时若不进行有效控制，则可能发生设备故障宕机的极端情况。因此，为保障系统在这样的情况下仍然能够正常提供网络服务，需要系统设备对用户的业务请求进行一定的话务控制，从而保障系统在正常负荷状态下继续运行，并能够继续提供网络服务。 
应用场景 :AMF在发生系统过负荷（根据过负荷等级判定）的情况下，将启动AMF过负荷控制功能，向gNodeB发送N2 Overload Start消息，对gNodeB输入的话务消息进行一定比例的控制，帮助AMF降低系统处理负荷并恢复正常状态。在系统负荷恢复正常（根据过负荷等级判断确定）后，AMF向gNodeB发送N2 Overload Stop消息，告知gNodeB解除对话务的输入控制，恢复正常处理状态。这一处理过程，实现了AMF的过负荷控制功能。 
客户收益 :受益方|受益描述
---|---
运营商|在系统过载情况下，本特性有助于保持设备的稳定运行，从而提高系统可靠性，降低系统运行风险
移动用户|保护设备避免其彻底故障宕机，从而能够为移动用户继续提供服务
实现原理 :系统架构 :图1  系统架构

AMF过负荷控制功能系统架构及工作原理： 
AMF发生过负荷的情况下，向gNodeB发送N2 OVERLOAD START消息，指示gNodeB减少到此AMF的话务输出。 
AMF将自身的负荷信息通过NF更新消息发送给NRF，NRF更新NF相关数据。 
流程如下： 
对订阅了AMF状态通知的NF如SMF，NRF主动向其发送AMF状态变更通知并携带负荷信息参数； 
同时，在NF发现的响应中，NRF将AMF的负荷信息返回给NF。 
流程如下： 
gNodeB接收N2 OVERLOAD START消息后，根据消息参数指示减少到此AMF的话务输出。 
其他NF如SMF从NRF获取AMF的负荷信息后，在后续的AMF选择流程中使用，如优先选择负荷较低的其他AMF执行业务流程。 
上述流程中步骤1、步骤4a属于N2接口过载控制功能。 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等操作
PCF|为AMF提供接入及移动性管理等用户策略服务
UDM|提供用户及会话相关的签约信息
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现，NF状态订阅及状态变更通知等功能
gNodeB|无线接入网络，在UE接入时提供无线资源及承载
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
本NF/网元实现 :网元|作用
---|---
AMF|在发生过负荷时，向gNodeB发送N2 OVERLOAD START消息。在过负荷解除后，向gNodeB发送N2OVERLOAD STOP消息。
gNodeB|接收AMF发送的N2 OVERLOAD START消息后，对指定业务按比例减少到AMF的输出。在接收AMF发送的N2OVERLOAD STOP消息后，恢复正常处理。
业务流程 :对于N2接口的过载控制功能，是AMF与gNodeB之间实现N2 Overload Start和N2 Overload Stop的流程。AMF的N2接口过载控制功能流程如[图2]所示。
图2  N2接口过负荷控制

过负荷控制执行 - N2 OVERLOAD START流程说明： 
AMF根据资源负荷等级判断，需要执行过负荷控制功能。 
AMF向gNodeB发送N2 OVERLOAD START消息，并携带AMF Overload Response参数，指示控制的话务类型，如拒绝非紧急及非高优先级终端发起的信令连接，只接受紧急业务和终呼信令连接，只接受高优先级业务和终呼信令连接等；携带AMF
Traffic Load Reduction Indication参数，指示需要减少话务的百分比。 
gNodeB接收N2 OVERLOAD START消息后，根据携带参数执行相应控制，减少到此AMF的话务输出。 
过负荷控制解除 - N2 OVERLOAD STOP流程说明： 
AMF根据资源负荷等级判断，需要解除之前已启动的过负荷控制功能。 
AMF向gNodeB发送N2 OVERLOAD STOP消息，指示gNodeB解除过负荷控制。 
gNodeB接收N2 OVERLOAD STOP消息后，解除过负荷控制，正常向此AMF进行话务输出。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.19.5 AMF Control Of Overload
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布
License要求 :如果本特性受license控制，按照下面的示例： 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性对应的License项目为AMF支持N2接口过负荷控制功能，此项目显示为支持，表示可以支持N2接口过载控制功能。
对其他网元的要求 :gNodeB|NRF|SMF|PCF|UDM
---|---|---|---|---
√|-|-|-|-
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
CPU负荷等级配置（过负荷控制基本配置）|SET OLCPULEVELCFG
SHOW OLCPULEVELCFG|CPU负荷等级配置（过负荷控制基本配置）
控制参数配置（过负荷控制基本配置）|SET OVERLOADCFG
SHOW OVERLOADCFG|控制参数配置（过负荷控制基本配置）
保证通过量配置（过负荷配置业务配置）|SET OLGUANUMCFG
SHOW OLGUANUMCFG|保证通过量配置（过负荷配置业务配置）
消息优先级配置（过负荷配置业务配置 - 优先级配置）|SET OLMSGPRIORITYCFG
SHOW OLMSGPRIORITYCFG|消息优先级配置（过负荷配置业务配置 - 优先级配置）
业务优先级配置（过负荷配置业务配置 - 优先级配置）|SET OLSRVPRIORITYCFG
SHOW OLSRVPRIORITYCFG|业务优先级配置（过负荷配置业务配置 - 优先级配置）
N2入向业务量配置（过负荷配置业务配置 - 入向业务量配置）|ADD OLINPUTN2SRVCFG
SET OLINPUTN2SRVCFG|N2入向业务量配置（过负荷配置业务配置 - 入向业务量配置）
DEL OLINPUTN2SRVCFG|N2入向业务量配置（过负荷配置业务配置 - 入向业务量配置）
SHOW OLINPUTN2SRVCFG|N2入向业务量配置（过负荷配置业务配置 - 入向业务量配置）
SBI入向业务量配置（过负荷配置业务配置 - 入向业务量配置）|ADD OLINPUTSBISRVCFG
SET OLINPUTSBISRVCFG|SBI入向业务量配置（过负荷配置业务配置 - 入向业务量配置）
DEL OLINPUTSBISRVCFG|SBI入向业务量配置（过负荷配置业务配置 - 入向业务量配置）
SHOW OLINPUTSBISRVCFG|SBI入向业务量配置（过负荷配置业务配置 - 入向业务量配置）
入向业务总量配置（过负荷配置业务配置 - 入向业务量配置）|SET OLTOTALNUMCFG
SHOW OLTOTALNUMCFG|入向业务总量配置（过负荷配置业务配置 - 入向业务量配置）
N2出向业务量配置（过负荷配置业务配置 - 出向业务量配置）|ADD OLOUTPUTN2SRVCFG
SET OLOUTPUTN2SRVCFG|N2出向业务量配置（过负荷配置业务配置 - 出向业务量配置）
DEL OLOUTPUTN2SRVCFG|N2出向业务量配置（过负荷配置业务配置 - 出向业务量配置）
SHOW OLOUTPUTN2SRVCFG|N2出向业务量配置（过负荷配置业务配置 - 出向业务量配置）
SBI出向业务量配置（过负荷配置业务配置 - 出向业务量配置）|ADD OLOUTPUTSBISRVCFG
SET OLOUTPUTSBISRVCFG|SBI出向业务量配置（过负荷配置业务配置 - 出向业务量配置）
DEL OLOUTPUTSBISRVCFG|SBI出向业务量配置（过负荷配置业务配置 - 出向业务量配置）
SHOW OLOUTPUTSBISRVCFG|SBI出向业务量配置（过负荷配置业务配置 - 出向业务量配置）
拥塞与过负荷控制（N2过负荷控制配置 - N2过负荷基本配置）|SET OLTORANBASICCFG
SHOW OLTORANBASICCFG|拥塞与过负荷控制（N2过负荷控制配置 - N2过负荷基本配置）
拥塞与过负荷控制（N2过负荷控制配置 - N2过负荷参数配置）|SET OLTORANCFG
SHOW OLTORANCFG|拥塞与过负荷控制（N2过负荷控制配置 - N2过负荷参数配置）
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :CPU过负荷控制，无需特殊配置，完成初始配置后即可使用。以下配置内容需要注意： 
入向和出向业务过负荷控制，需要在网管上配置相应控制消息的类型和通过数，可根据实际情况对过负荷控制功能进行修改。 
如果启用OVERLOADSTART/OVERLOADSTOP功能，需打开功能开关SET OLTORANCFG:OLSWITCH="OLSWITCHON"，其余无需特殊配置，完成初始配置后即可使用。 
SBI状态码接收控制，开启429和503状态码接收开关即可，无特殊配置。 
SBI状态码发送控制，需开启429和503状态码发送开关，根据实际情况在网管上配置通用状态码配置或指定状态码配置。 
配置前提 :AMF网元运行正常。 
启用OVERLOADSTART功能时，需要AMF的高CPU运行状态，且打开license（ID为uMAC_AMF_7208）。 
启用OVERLOADSTOP功能时，需要AMF低CPU运行状态，且打开license（ID为uMAC_AMF_7208）。 
启用SBI状态码发送控制功能时，需要AMF网元高CPU运行状态，且打开license（ID为uMAC_AMF_7224）。 
启用SBI状态码接收控制功能时，需要打开license（ID为uMAC_AMF_7224）。 
配置过程 :执行[SET OLCPULEVELCFG]命令，修改CPU负荷等级配置。
执行[SET OVERLOADCFG]命令，修改过负荷控制参数配置。
执行[SET OLGUANUMCFG]命令，修改CPU过负荷业务类型的保证通过量。
执行[SET OLMSGPRIORITYCFG]命令，修改CPU过负荷各消息类型的优先级。
执行[SET OLSRVPRIORITYCFG]命令，修改CPU过负荷各业务类型的优先级。
执行[ADD OLINPUTN2SRVCFG]命令，增加N2入向业务类型的过负荷配置。
执行[ADD OLINPUTSBISRVCFG]命令，增加SBI入向业务类型的过负荷配置。
执行[SET OLTOTALNUMCFG]命令，修改入向业务总量配置。
执行[SET OLTORANBASICCFG]命令，修改overload基本配置参数信息。
执行[SET OLTORANCFG]命令，修改overload控制参数配置信息。
执行[SET GENERALSTATUSCODECFG]命令，修改SBI通用状态码发送控制配置信息。
执行[ADD SPECSTATUSCODECFG]命令，增加SBI指定状态码发送控制配置信息。
配置实例 :###### 示例1 
场景说明
在设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。除了默认开启的CPU拥塞控制来保证系统安全外，还可以单独对某个单项业务控制。CPU拥塞控制参数保持默认即可。 
这里仅就N2入向业务控制配置（初始注册与周期性注册）进行举例说明。出向业务与之入向类似，不做详细介绍。 
数据规划
配置项|参数|取值
---|---|---
修改OVERLOADCFG配置|是否启用CPU过负荷控制|AMFOLSWITCHON
是否启用业务通过量负荷控制|修改OVERLOADCFG配置|SRVSWITCHON
控制周期(100ms)|修改OVERLOADCFG配置|10
评估周期/控制周期|修改OVERLOADCFG配置|5
缓冲百分比(%)|修改OVERLOADCFG配置|5
新增OLINPUTN2SRVCFG配置|业务类型|REGISTRATION
N2口入向业务每秒每实例最大通过量|新增OLINPUTN2SRVCFG配置|1000
过负荷控制业务权重|新增OLINPUTN2SRVCFG配置|1
修改OLTOTALNUMCFG配置|每秒每实例N2口入向控制总量|3000
每秒每实例SBI口入向控制总量|修改OLTOTALNUMCFG配置|3000
配置步骤
步骤|说明|操作
---|---|---
1|开启CPU过负荷控制与业务通过量负荷控制。|SET OVERLOADCFG:OLSWITCH="AMFOLSWITCHON",SRVSWITCH="SRVSWITCHON",OLCTRLCYCLE=10,JUDGERATIO=5,RECOVBUFF=5
2|开启N2入向业务控制（初始注册和周期性注册），每秒最大通过数为1000。|ADD OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION",OLMAXNUM=1000,OLWEIGHT=1
3|修改入向业务总量配置，即所有入向业务类型相加的每秒通过数，如不修改此项配置，则入向总量不控制。|SET OLTOTALNUMCFG:OLINPUTN2TOTALNUM=3000,OLINPUTSBITOTALNUM=3000
###### 示例2 
场景说明
AMF在发生系统过负荷（根据过负荷等级判定）的情况下，将启动AMF过负荷控制功能，向gNodeB发送N2 Overload Start消息，对gNodeB输入的话务消息进行一定比例的控制，帮助AMF降低系统处理负荷并恢复正常状态。在系统负荷恢复正常（根据过负荷等级判断确定）后，AMF向gNodeB发送N2 Overload Stop消息，告知gNodeB解除对话务的输入控制，恢复正常处理状态。 
开始业务话务流程，使AMF整局CPU达到OLTORANCFG配置的N2口发送Overload Start的低/高过载负荷等级，发送OVERLOADSTART。 
降低业务话务流程，使AMF整局CPU降到OLTORANCFG配置的N2口发送Overload Start的低过载负荷等级，发送OVERLOADSTOP。 
数据规划
配置项|参数|取值
---|---|---
修改OLTORANCFG配置|是否开启过载控制|OLSWITCHON
N2口消息中是否携带切片信息|修改OLTORANCFG配置|NSSAISWITCHOFF
N2口发送Overload Start的低过载负荷等级|修改OLTORANCFG配置|SECONDARYLEVEL
轻微过载下Overload Start消息中Overload Action信元设置|修改OLTORANCFG配置|REJECTNONEMCONNECT
轻微过载Traffic Load Reduction Indication信元设置|修改OLTORANCFG配置|10
N2口发送Overload Start的高过载负荷等级|修改OLTORANCFG配置|PRIMARYLEVEL
严重过载下Overload Start消息中Overload Action信元设置|修改OLTORANCFG配置|REJECTNONEMCONNECT
严重过载Traffic Load Reduction Indication信元设置|修改OLTORANCFG配置|20
发送Overload start 的最大gNodeB个数|修改OLTORANCFG配置|64
修改OLCPULEVELCFG配置|一级负荷低门限值(%)|85
二级负荷低门限值(%)|修改OLCPULEVELCFG配置|75
三级负荷低门限值(%)|修改OLCPULEVELCFG配置|65
四级负荷低门限值(%)|修改OLCPULEVELCFG配置|60
配置步骤
步骤|说明|操作
---|---|---
1|开启OVERLOADSTART/OVERLOADSSTOP功能开关。|SET OLTORANCFG:OLSWITCH="OLSWITCHON",NSSAISWITCH="NSSAISWITCHOFF",LOWLEVEL="SECONDARYLEVEL",LOWOLACT="REJECTNONEMCONNECT",LOWOLTLRI=10,HIGHLEVEL="PRIMARYLEVEL",HIGHOLACT="REJECTNONEMCONNECT",HIGHOLTLRI=20,OLGNBNUM=64
2|修改OLCPULEVELCFG配置。|SET OLCPULEVELCFG:OL1THRESHOLD=85,OL2THRESHOLD=75,OL3THRESHOLD=65,OL4THRESHOLD=60
###### 示例3 
场景说明
当AMF接收到对端NF响应消息携带状态码429或503时（对端网元过载），需根据携带的Retry-After参数时长，在该时段内不再向该NF发送消息。 
数据规划
配置项|参数|取值
---|---|---
修改OVERLOADCFG配置|是否启用429和503状态码接收|STATUSRECVSWITCHON|STATUSRECVSWITCHON|STATUSRECVSWITCHON
配置步骤
步骤|说明|操作
---|---|---
1|开启状态码接收控制功能开关。|SET OVERLOADCFG:STATUSRECVSWITCH="STATUSRECVSWITCHON"
###### 示例4 
场景说明
当AMF过载时，配置通用状态码控制配置，发送响应码429或503到对端，并携带Retry-After。 
开始业务话务流程，使AMF整局CPU达到高过载负荷等级，对端SMF发送消息超过配置门限值。此时本控制周期内，如果上一周期发送到本端AMF请求消息最多的10个SMF仍然发送消息到本端AMF上，AMF会返回响应失败，下发响应状态码429或503，并携带Retry-After时长。 
数据规划
配置项|参数|取值
---|---|---
修改OVERLOADCFG配置|是否启用429和503状态码发送|STATUSSENDSWITCHON
修改GENERALSTATUSCODECFG配置|NF类型|SMF
每秒每实例接收消息门限|修改GENERALSTATUSCODECFG配置|1000
比例门限|修改GENERALSTATUSCODECFG配置|50
执行控制的NF个数|修改GENERALSTATUSCODECFG配置|10
仅发送503|修改GENERALSTATUSCODECFG配置|NO
重试时长最小取值（秒）|修改GENERALSTATUSCODECFG配置|10
重试时长最大取值（秒）|修改GENERALSTATUSCODECFG配置|30
修改OLCPULEVELCFG配置|一级负荷低门限值(%)|85
二级负荷低门限值(%)|修改OLCPULEVELCFG配置|75
三级负荷低门限值(%)|修改OLCPULEVELCFG配置|65
四级负荷低门限值(%)|修改OLCPULEVELCFG配置|60
配置步骤
步骤|说明|操作
---|---|---
1|开启状态码发送控制功能开关。|SET OVERLOADCFG:STATUSSENDSWITCH="STATUSSENDSWITCHON"
2|修改SBI通用状态码控制配置。|SET GENERALSTATUSCODECFG:NFTYPE="SMF",MSGTHRESHOLD=1000,JUDGEPERCENT=50,CTRLTOPNUM=10,ONLY503="NO",MINRETRYAFTER=10,MAXRETRYAFTER=30
3|修改OLCPULEVELCFG配置。|SET OLCPULEVELCFG:OL1THRESHOLD=85,OL2THRESHOLD=75,OL3THRESHOLD=65,OL4THRESHOLD=60
###### 示例5 
场景说明
当AMF过载时，配置指定状态码控制配置，发送响应码429或503到对端，并携带Retry-After。 
开始业务话务流程，使AMF整局CPU达到高过载负荷等级，对端SMF发送消息超过配置门限值。此时本控制周期内，如果指定的SMF_01仍然发送消息到本端AMF上，AMF会返回响应失败，下发状态码429或503，并携带Retry-After时长。 
数据规划
配置项|参数|取值
---|---|---
修改OVERLOADCFG配置|是否启用429和503状态码发送|STATUSSENDSWITCHON
增加SPECSTATUSCODECFG配置|NF实例标识|SMF_01
每秒每实例接收消息门限|增加SPECSTATUSCODECFG配置|1000
比例门限|增加SPECSTATUSCODECFG配置|50
重试时长最小取值（秒）|增加SPECSTATUSCODECFG配置|10
重试时长最大取值（秒）|增加SPECSTATUSCODECFG配置|30
修改OLCPULEVELCFG配置|一级负荷低门限值(%)|85
二级负荷低门限值(%)|修改OLCPULEVELCFG配置|75
三级负荷低门限值(%)|修改OLCPULEVELCFG配置|65
四级负荷低门限值(%)|修改OLCPULEVELCFG配置|60
配置步骤
步骤|说明|操作
---|---|---
1|开启状态码发送控制功能开关。|SET OVERLOADCFG:STATUSSENDSWITCH="STATUSSENDSWITCHON"
2|增加SBI指定状态码控制配置。|ADD SPECSTATUSCODECFG:NFID="SMF_01",MSGTHRESHOLD=1000,JUDGEPERCENT=50,MINRETRYAFTER=10,MAXRETRYAFTER=30
3|修改OLCPULEVELCFG配置。|SET OLCPULEVELCFG:OL1THRESHOLD=85,OL2THRESHOLD=75,OL3THRESHOLD=65,OL4THRESHOLD=60
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|CPU过负荷配置（以初始注册与周期性注册业务类型为例）
---|---
测试目的|当多用户注册流程中超过CPU门限值，对该流程进行控制
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|大量UE同时发起注册流程，使CPU负荷增加
通过准则|当CPU使用率超过门限值时，开始CPU过负荷控制，部分注册请求消息被丢弃
测试结果|–
测试项目|N2入向业务过负荷配置（以初始注册与周期性注册业务类型为例）
---|---
测试目的|当多用户注册请求超过配置的入向业务门限值时，对该流程进行控制
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|大量UE同时发起注册流程，达到每秒最大门限值。
通过准则|当每秒钟发起的注册请求数超过配置的门限值时，部分注册请求消息被丢弃。
测试结果|–
测试项目|SBI入向业务过负荷配置（以pdu建立n1n2transfer消息业务类型为例）
---|---
测试目的|pdu建立时n1n2transfer消息的控制
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式UE已注册
测试过程|大量UE同时发起pdu建立流程，达到每秒最大门限值。
通过准则|当每秒钟发起的pdu建立请求数超过配置的门限值时，部分pdu请求消息被丢弃。
测试结果|–
测试项目|N2出向业务过负荷配置（以寻呼消息业务类型为例）
---|---
测试目的|对寻呼消息的控制。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式UE已N2释放
测试过程|一段时间内大量的网络侧触发的寻呼消息，超过配置的门限值。
通过准则|当每秒钟发起的网络侧触发的寻呼请求数超过配置的门限值时，部分寻呼消息被丢弃。
测试结果|–
测试项目|SBI出向业务过负荷配置（以pdu建立create_sm_context消息业务类型为例）
---|---
测试目的|对pdu建立过程中create sm context消息的控制。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式UE已注册
测试过程|大量UE同时发起pdu建立流程，发出的create sm context请求达到每秒最大门限值。
通过准则|当每秒钟发出的create sm context请求数超过配置的门限值时，部分create sm context请求消息被丢弃。
测试结果|–
测试项目|SBI状态码接收控制
---|---
测试目的|当对端网元发送429或503到本端AMF，本端AMF在Retry-After时长内不再发送消息到该网元。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|对端网元发送429或503到本端AMF。
通过准则|后续业务流程，不再选择该过载网元。超过Retry-After时长后，会继续选择该网元。
测试结果|–
测试项目|SBI状态码发送控制
---|---
测试目的|当本端AMF过载时，能下发429或503，并携带Retry-After到对端网元。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|当CPU使用率超过门限值时，对端网元（SMF、PCF）发起大量请求消息到本端AMF，请求消息超过门限时，下发发429或503，并携带Retry-After到对端网元。
通过准则|能选出请求最多的端对网元并下发发429或503，并携带Retry-After时长。
测试结果|–
常见问题处理 :无。 
## ZUF-79-17-004 NAS拥塞控制 
特性描述 :特性描述 :术语 :术语|含义
---|---
拥塞控制|输入信令的增加将导致系统处理负荷持续上升，极端情况下输入信令数量将超出系统实际处理能力，此时需要对输入信令进行拒绝或丢弃控制，从而避免系统负荷持续上升，最终导致系统故障宕机的情况发生。
描述 :定义 :当某类型的业务数量输入过多时，对于UE发起的请求消息，AMF可以通过向UE发送拒绝消息并携带退避时长请求UE在此时间内抑制业务请求的发送，从而有效减少业务输入并实现负荷控制。 
这种对拥塞信令进行的控制即拥塞控制，可以有效保障网络设备稳定、安全的运行。 
背景知识 :通常情况下，由于用户的异常行为或大量用户集中接入等情况引起的话务高峰容易造成系统设备处理过载，此时若不进行有效控制，则可能发生设备故障宕机的极端情况。因此，为保障系统仍然能够正常提供网络服务，需要系统设备对用户的业务请求进行一定的话务控制，从而保障系统在正常负荷状态下继续运行，并能够继续提供网络服务。 
应用场景 :AMF在N1/N2接口发生NAS信令拥塞（根据拥塞控制条件判断确定）后，将对UE发送的请求消息进行一定比例的拒绝处理，同时携带退避定时器用来抑制UE在此时长内发送请求消息，从而实现NAS拥塞控制。 
拥塞控制功能通常应用于以下场景： 
基于NAS MM的拥塞控制 
基于DNN的拥塞控制 
基于S-NSSAI的拥塞控制 
基于S-NSSAI和DNN的拥塞控制 
客户收益 :受益方|受益描述
---|---
运营商|在系统过载情况下，本特性有助于保持设备的稳定运行，从而提高系统可靠性，降低系统运行风险。
移动用户|保护设备避免其彻底故障宕机，从而能够为移动用户继续提供服务。
实现原理 :系统架构 :图1  拥塞控制系统架构及工作原理

拥塞控制系统架构及原理： 
AMF的NAS拥塞控制功能由AMF和UE共同实现并完成 
拥塞控制执行前，UE发出的大量NAS消息在网络中传递及处理，造成AMF发生拥塞 
拥塞控制执行中，AMF对部分UE请求执行拒绝处理，并携带拥塞原因值及退避定时器 
拥塞控制执行后，UE在退避时长内，不再主动发送请求消息。网络中请求消息减少，AMF拥塞得到缓解，并逐步恢复正常 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等操作
gNodeB|无线接入网络，在UE接入时提供无线资源及承载
UE|3GPP终端，支持5G功能
协议栈 :该特性涉及的接口协议栈参见下表： 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
本NF/网元实现 :拥塞控制功能需要UE配合实现，作用参见下表。 
网元|作用
---|---
AMF|在发生NAS信令拥塞（根据拥塞控制条件判断确定）时，按比例拒绝UE请求消息，并携带原因值和Back-off Timer
UE|接收AMF发送的请求拒绝消息（如注册拒绝消息，业务请求拒绝消息）后，在指定的退避时间内不再发送相应的业务请求，在时间超时后，可以重新发起请求
业务流程 :图2  拥塞控制处理流程

流程说明： 
UE发送请求消息经由gNodeB传送到AMF。 
AMF发生NAS信令拥塞（根据拥塞控制条件判断确定）后，则决定拒绝请求消息，并携带拒绝原因值和Back-off Timer（退避定时器）。 
AMF发送请求决绝消息经由gNodeB传送到UE，UE接收消息后，根据原因值识别是网络侧的拥塞控制，则根据Back-off Timer在退避时长内不再主动发送请求消息。 
拥塞控制的停止和解除： 
拥塞控制条件判断不再成立。 
网络侧主动下发NAS信令给UE，此UE相关的拥塞控制解除。 
拥塞控制功能提供以下场景的拥塞控制： 
基于NAS MM的拥塞控制。 
基于DNN的拥塞控制。 
基于S-NSSAI的拥塞控制。 
基于S-NSSAI和DNN的拥塞控制。 
“基于NAS MM的拥塞控制”功能
对于“基于NAS MM的拥塞控制”功能，AMF可以根据以下条件决定是否拒绝业务请求： 
通过“最大会话建立请求速率”是否超过配置阈值进行控制。 
通过“最大接收NAS MM信令速率”是否超过配置阈值进行控制。 
其中，对于用于拥塞控制条件判断的统计项： 
对于“最大会话建立请求速率”，统计UL NAS TRANSPORT（其中Payload container type 为N1 SM information，同时Request type为initial request）消息。 
对于“最大接收NAS MM信令速率”，统计REGISTRATION REQUEST和SERVICE REQUEST消息。 
对于“基于NAS MM的拥塞控制”功能的控制消息： 
REGISTRATION REQUEST 
SERVICE REQUEST 
“基于DNN的拥塞控制”功能
对于“基于DNN的拥塞控制”功能，AMF可以根据以下条件决定是否拒绝业务请求： 
通过此“DNN最大会话建立请求速率”是否超过配置阈值进行控制。 
通过此“DNN最大接收NAS SM信令速率”是否超过配置阈值进行控制。 
其中，对于用于拥塞控制条件判断的统计项： 
对于“DNN最大会话建立请求速率”，统计此DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为initial request）消息。 
对于“DNN最大接收NAS SM信令速率”，统计此DNN相关的UL NAS TRANSPORT（其中Payload container type 为N1 SM information）消息。 
对于“基于DNN的拥塞控制”功能的控制消息： 
此DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为initial request）消息。 
此DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为existing PDU session）消息，此项可选。 
此DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为modification request）消息，此项可选。 
“基于S-NSSAI的拥塞控制”功能
对于“基于S-NSSAI的拥塞控制”功能，AMF可以根据以下条件决定是否拒绝业务请求： 
通过此“S-NSSAI最大会话建立请求速率”是否超过配置阈值进行控制。 
通过此“S-NSSAI最大接收NAS SM信令速率”是否超过配置阈值进行控制。 
其中，对于用于拥塞控制条件判断的统计项： 
对于“S-NSSAI最大会话建立请求速率”，统计此S-NSSAI相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为initial request）消息。 
对于“S-NSSAI最大接收NAS SM信令速率”，统计此S-NSSAI相关的UL NAS TRANSPORT（其中Payload container type 为N1 SM information）消息。 
对于“基于S-NSSAI的拥塞控制”功能的控制消息： 
此S-NSSAI相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为initial request）消息。 
此S-NSSAI相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为existing PDU session）消息，此项可选。 
此S-NSSAI相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为modification request）消息，此项可选。 
“基于S-NSSAI和DNN的拥塞控制”功能
对于“基于S-NSSAI和DNN的拥塞控制”功能，AMF可以根据以下条件决定是否拒绝业务请求： 
通过此“S-NSSAI和DNN的最大会话建立请求速率”是否超过配置阈值进行控制。 
通过此“S-NSSAI和DNN的最大接收NAS SM信令速率”是否超过配置阈值进行控制。 
其中，对于用于拥塞控制条件判断的统计项： 
对于“S-NSSAI和DNN的最大会话建立请求速率”，统计此S-NSSAI和DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为initial request）消息。 
对于“S-NSSAI和DNN的最大接收NAS SM信令速率”，统计此S-NSSAI和DNN相关的UL NAS TRANSPORT（其中Payload container type 为N1 SM information）消息。 
对于“基于S-NSSAI和DNN的拥塞控制”功能的控制消息： 
此S-NSSAI和DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为initial request）消息。 
此S-NSSAI和DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为existing PDU session）消息，此项可选。 
此S-NSSAI和DNN相关的UL NAS TRANSPORT（其中Payload container type为N1 SM information，同时Request type为modification request）消息，此项可选。 
系统影响 :对于UE，拥塞控制执行期间UE会根据退避定时器而延迟发起业务。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.19.7 NAS level congestion control
3GPP TS 24.501（Non-Access-Stratum (NAS) protocol for 5G System）|5.3.9 Handling of NAS level mobility management congestion control5.3.10 Handling of DNN based congestion control5.3.11 Handling of S-NSSAI based congestion control5.4.5 NAS transport procedure(s)5.5 5GMM specific procedures5.6 5GMM connection management procedures6.2 General on elementary 5GSM procedures6.4 UE-requested 5GSM procedures
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。对应的license包括： 
AMF支持基于NAS MM拥塞控制功能 
AMF支持基于DNN拥塞控制功能 
AMF支持基于S-NSSAI拥塞控制功能 
AMF支持基于S-NSSAI和DNN拥塞控制功能 
对其他网元的要求 :gNodeB|UE
---|---
-|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
NAS MM拥塞配置（拥塞控制配置）|SET NASMMCONGESTINCFG
SHOW NASMMCONGESTINCFG|NAS MM拥塞配置（拥塞控制配置）
配置项|命令
---|---
DNN拥塞配置（拥塞控制配置）|ADD DNNCONGESTIONCFG
SET DNNCONGESTIONCFG|DNN拥塞配置（拥塞控制配置）
DEL DNNCONGESTIONCFG|DNN拥塞配置（拥塞控制配置）
SHOW DNNCONGESTIONCFG|DNN拥塞配置（拥塞控制配置）
配置项|命令
---|---
SNSSAI拥塞配置（拥塞控制配置）|ADD SNSSAICONGESTIONCFG
SET SNSSAICONGESTIONCFG|SNSSAI拥塞配置（拥塞控制配置）
DEL SNSSAICONGESTIONCFG|SNSSAI拥塞配置（拥塞控制配置）
SHOW SNSSAICONGESTIONCFG|SNSSAI拥塞配置（拥塞控制配置）
配置项|命令
---|---
SNSSAI DNN拥塞配置（拥塞控制配置）|ADD SNSSAIDNNCONGESTIONCFG
SET SNSSAIDNNCONGESTIONCFG|SNSSAI DNN拥塞配置（拥塞控制配置）
DEL SNSSAIDNNCONGESTIONCFG|SNSSAI DNN拥塞配置（拥塞控制配置）
SHOW SNSSAIDNNCONGESTIONCFG|SNSSAI DNN拥塞配置（拥塞控制配置）
配置项|命令
---|---
控制参数配置（拥塞控制配置  -  OLTORAN配置）|SET OLTORANCFG
SHOW OLTORANCFG|控制参数配置（拥塞控制配置  -  OLTORAN配置）
配置项|命令
---|---
基本参数配置（拥塞控制配置  -  OLTORAN配置）|SET OLTORANBASICCFG
SHOW OLTORANBASICCFG|基本参数配置（拥塞控制配置  -  OLTORAN配置）
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :按接入类型进行拥塞控制功能默认关闭，可根据实际情况决定是否开启该功能。 
NAS MM拥塞控制功能默认关闭，可根据情况决定是否开启该功能，该功能控制的业务类型包括注册请求与业务请求消息。 
SNSSAI DNN拥塞控制功能默认关闭，可根据情况决定是否开启该功能，该功能控制的业务类型包括会话业务类型请求消息。 
SNSSAI拥塞控制功能默认关闭，可根据情况决定是否开启该功能，该功能控制的业务类型包括会话业务类型请求消息。 
DNN拥塞控制功能默认关闭，可根据情况决定是否开启该功能，该功能控制的业务类型包括会话业务类型请求消息。 
 说明： 
当2、3、4同时开启时，判断条件优先级：先判断当前是否满足SNSSAI DNN拥塞配置过负荷条件，不满足再判断是否满足SNSSAI拥塞配置过负荷条件， 最后再判断是否满足DNN拥塞配置过负荷条件。 
配置前提 :5GC(AMF)网元运行正常，无特殊配置前提。 
配置过程 :NAS MM拥塞控制配置 
执行[SET NASMMCONGESTINCFG]命令，修改NAS MM拥塞控制配置。
SNSSAI DNN拥塞控制配置 
执行[ADD SNSSAIDNNCONGESTIONCFG]命令，增加SNSSAI DNN拥塞控制配置。
执行[SET SNSSAIDNNCONGESTIONCFG]命令，修改SNSSAI DNN拥塞控制配置。
执行[DEL SNSSAIDNNCONGESTIONCFG]命令，删除SNSSAI DNN拥塞控制配置。
SNSSAI拥塞控制配置 
执行[ADD SNSSAICONGESTIONCFG]命令，增加SNSSAI拥塞控制配置。
执行[SET SNSSAICONGESTIONCFG]命令，修改SNSSAI拥塞控制配置。
执行[DEL SNSSAICONGESTIONCFG]命令，删除SNSSAI拥塞控制配置。
DNN拥塞控制配置 
执行[ADD DNNCONGESTIONCFG]命令，增加DNN拥塞控制配置。
执行[SET DNNCONGESTIONCFG]命令，修改DNN拥塞控制配置。
执行[DEL DNNCONGESTIONCFG]命令，删除DNN拥塞控制配置。
配置实例 :###### NAS MM拥塞控制配置 
场景说明
按接入类型进行NAS MM拥塞控制。 
数据规划
配置项|参数|取值
---|---|---
修改NASMMCONGESTINCFG配置|CONGESTIONSWITCH|SUPCONGESTIONCTRL
TYPE|修改NASMMCONGESTINCFG配置|MAXRATE
MAXRATE|修改NASMMCONGESTINCFG配置|1000
MINDELAY|修改NASMMCONGESTINCFG配置|600
MAXDELAY|修改NASMMCONGESTINCFG配置|1800
REJECTRATE|修改NASMMCONGESTINCFG配置|100
修改NASMMCONGESTINCFG配置|NASMMCONGESTINCFG|SUPCONGESTIONCTRL
TYPE|修改NASMMCONGESTINCFG配置|MAXNASMM
MAXRATE|修改NASMMCONGESTINCFG配置|1000
MINDELAY|修改NASMMCONGESTINCFG配置|600
MAXDELAY|修改NASMMCONGESTINCFG配置|1800
REJECTRATE|修改NASMMCONGESTINCFG配置|100
配置步骤
步骤|说明|操作
---|---|---
1|SET NASMMCONGESTINCFG:CONGESTIONSWITCH="SUPCONGESTIONCTRL",TYPE="MAXRATE",MAXRATE=1000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100|设置NAS MM拥塞控制配置，拥塞控制类型为最大会话速率，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为600秒到1800秒之间的随机值。
2|SET NASMMCONGESTINCFG:CONGESTIONSWITCH="SUPCONGESTIONCTRL",TYPE="MAXNASMM",MAXRATE=1000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100|设置NAS MM拥塞控制配置，拥塞控制类型为接收NAS MM信令速率，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为600秒到1800秒之间的随机值。
###### SNSSAI DNN拥塞控制配置 
场景说明
按接入类型进行NAS SM（SNSSAI&&DNN）拥塞控制。 
数据规划
配置项|参数|取值
---|---|---
增加SNSSAIDNNCONGESTIONCFG配置|CONGESTIONSWITCH|SUPSNSSAIDNNCONGESTIONCTRL
INITSWITCH|增加SNSSAIDNNCONGESTIONCFG配置|ONLYCTRLINITIALREQ
SNSSAIDNNIDENTITY|增加SNSSAIDNNCONGESTIONCFG配置|1
SST|增加SNSSAIDNNCONGESTIONCFG配置|eMBB
SD|增加SNSSAIDNNCONGESTIONCFG配置|123456
DNN|增加SNSSAIDNNCONGESTIONCFG配置|zte.com.cn
TYPE|增加SNSSAIDNNCONGESTIONCFG配置|MAXRATE
MAXRATE|增加SNSSAIDNNCONGESTIONCFG配置|1000
MINDELAY|增加SNSSAIDNNCONGESTIONCFG配置|600
MAXDELAY|增加SNSSAIDNNCONGESTIONCFG配置|1800
REJECTRATE|增加SNSSAIDNNCONGESTIONCFG配置|100
修改SNSSAIDNNCONGESTIONCFG配置|CONGESTIONSWITCH|SUPSNSSAIDNNCONGESTIONCTRL
INITSWITCH|修改SNSSAIDNNCONGESTIONCFG配置|ONLYCTRLINITIALREQ
SNSSAIDNNIDENTITY|修改SNSSAIDNNCONGESTIONCFG配置|1
SST|修改SNSSAIDNNCONGESTIONCFG配置|eMBB
SD|修改SNSSAIDNNCONGESTIONCFG配置|123456
DNN|修改SNSSAIDNNCONGESTIONCFG配置|zte.com.cn
TYPE|修改SNSSAIDNNCONGESTIONCFG配置|MAXNASm
MAXRATE|修改SNSSAIDNNCONGESTIONCFG配置|1000
MINDELAY|修改SNSSAIDNNCONGESTIONCFG配置|600
MAXDELAY|修改SNSSAIDNNCONGESTIONCFG配置|1800
REJECTRATE|修改SNSSAIDNNCONGESTIONCFG配置|100
删除SNSSAIDNNCONGESTIONCFG配置|SNSSAIDNNIDENTITY|1
配置步骤
步骤|说明|操作
---|---|---
1|ADD SNSSAIDNNCONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAIDNNCONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",SNSSAIDNNIDENTITY="1",SST="eMBB",SD="123456",DNN="zte.com.cn",TYPE="MAXRATE",MAXRATE=1000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100|设置NAS SM （SNSSAI&DNN）拥塞控制配置，拥塞控制类型为建立会话速率，配置拥塞控制的SNSSAI为（sst: eMBB sd: 123456），DNN为zte.com.cn，只控制初始请求消息，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为1800秒到3600秒之间的随机值。
2|SET SNSSAIDNNCONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAIDNNCONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",SNSSAIDNNIDENTITY="1",SST="eMBB",SD="123456",DNN="zte.com.cn",TYPE="MAXNASm",MAXNASSM=1000,MINDELAY=1800,MAXDELAY=3600,REJECTRATE=100|修改NAS SM （SNSSAI&DNN）拥塞控制配置，拥塞控制类型为NAS SM信令速率控制，配置拥塞控制的SNSSAI为（sst: eMBB sd: 123456），DNN为zte.com.cn，只控制初始请求消息，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为1800秒到3600秒之间的随机值。
3|DEL SNSSAIDNNCONGESTIONCFG:SNSSAIDNNIDENTITY="1"|删除NAS SM （SNSSAI&DNN）拥塞控制配置。
###### SNSSAI拥塞控制配置 
场景说明
按接入类型进行NAS SM（SNSSAI）拥塞控制。 
数据规划
配置项|参数|取值
---|---|---
增加SNSSAICONGESTIONCFG配置|CONGESTIONSWITCH|SUPSNSSAICONGESTIONCTRL
INITSWITCH|增加SNSSAICONGESTIONCFG配置|ONLYCTRLINITIALREQ
SNSSAINAME|增加SNSSAICONGESTIONCFG配置|1
SNSSAINAME|增加SNSSAICONGESTIONCFG配置|eMBB
SD|增加SNSSAICONGESTIONCFG配置|123456
TYPE|增加SNSSAICONGESTIONCFG配置|MAXRATE
MAXRATE|增加SNSSAICONGESTIONCFG配置|1000
MINDELAY|增加SNSSAICONGESTIONCFG配置|1800
MAXDELAY|增加SNSSAICONGESTIONCFG配置|3600
REJECTRATE|增加SNSSAICONGESTIONCFG配置|100
修改SNSSAICONGESTIONCFG配置|CONGESTIONSWITCH|SUPSNSSAICONGESTIONCTRL
INITSWITCH|修改SNSSAICONGESTIONCFG配置|ONLYCTRLINITIALREQ
SNSSAINAME|修改SNSSAICONGESTIONCFG配置|1
SNSSAINAME|修改SNSSAICONGESTIONCFG配置|eMBB
SD|修改SNSSAICONGESTIONCFG配置|123456
TYPE|修改SNSSAICONGESTIONCFG配置|MAXNASSM
MAXRATE|修改SNSSAICONGESTIONCFG配置|1000
MINDELAY|修改SNSSAICONGESTIONCFG配置|1800
MAXDELAY|修改SNSSAICONGESTIONCFG配置|3600
REJECTRATE|修改SNSSAICONGESTIONCFG配置|100
删除SNSSAICONGESTIONCFG配置|SNSSAINAME|1
配置步骤
步骤|说明|操作
---|---|---
1|ADD SNSSAICONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAICONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",SNSSAINAME="1",SST="eMBB",SD="123456",TYPE="MAXRATE",MAXRATE=1000,MINDELAY=1800,MAXDELAY=3600,REJECTRATE=100|设置NAS SM （SNSSAI）拥塞控制配置，拥塞控制类型为建立会话速率，配置拥塞控制的SNSSAI为（sst: eMBB sd: 123456），只控制初始请求消息，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为1800秒到3600秒之间的随机值。
2|SET SNSSAICONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAICONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",SNSSAINAME="1",SST="eMBB",SD="123456",TYPE="MAXNASSM",MAXNASSM=1000,MINDELAY=1800,MAXDELAY=3600,REJECTRATE=100|修改NAS SM （SNSSAI）拥塞控制配置，拥塞控制类型为NAS SM信令速率控制，配置拥塞控制的SNSSAI为（sst: eMBB sd: 123456），只控制初始请求消息，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为1800秒到3600秒之间的随机值。
3|DEL SNSSAICONGESTIONCFG:SNSSAINAME="1"|删除NAS SM （SNSSAI）拥塞控制配置。
###### DNN拥塞控制配置 
场景说明
按接入类型进行NAS SM（DNN）拥塞控制。 
数据规划
配置项|参数|取值
---|---|---
增加DNNCONGESTIONCFG配置|CONGESTIONSWITCH|SUPDNNCONGESTIONCTRL
INITSWITCH|增加DNNCONGESTIONCFG配置|ONLYCTRLINITIALREQ
DNN|增加DNNCONGESTIONCFG配置|zte.com.cn
TYPE|增加DNNCONGESTIONCFG配置|MAXRATE
MAXRATE|增加DNNCONGESTIONCFG配置|1000
MINDELAY|增加DNNCONGESTIONCFG配置|1800
MAXDELAY|增加DNNCONGESTIONCFG配置|3600
REJECTRATE|增加DNNCONGESTIONCFG配置|100
修改DNNCONGESTIONCFG配置|CONGESTIONSWITCH|SUPDNNCONGESTIONCTRL
INITSWITCH|修改DNNCONGESTIONCFG配置|ONLYCTRLINITIALREQ
DNN|修改DNNCONGESTIONCFG配置|zte.com.cn
TYPE|修改DNNCONGESTIONCFG配置|MAXNASSM
MAXRATE|修改DNNCONGESTIONCFG配置|1000
MINDELAY|修改DNNCONGESTIONCFG配置|1800
MAXDELAY|修改DNNCONGESTIONCFG配置|3600
REJECTRATE|修改DNNCONGESTIONCFG配置|100
删除DNNCONGESTIONCFG配置|DNN|zte.com.cn
配置步骤
步骤|说明|操作
---|---|---
1|ADD DNNCONGESTIONCFG:CONGESTIONSWITCH="SUPDNNCONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",DNN="zte.com.cn",TYPE="MAXRATE",MAXRATE=1000,MINDELAY=1800,MAXDELAY=3600,REJECTRATE=100|设置NAS SM （DNN）拥塞控制配置，拥塞控制类型为建立会话速率，DNN为zte.com.cn，只控制初始请求消息，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为1800秒到3600秒之间的随机值。
2|SET DNNCONGESTIONCFG:CONGESTIONSWITCH="SUPDNNCONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",DNN="zte.com.cn",TYPE="MAXNASMM",MAXNASSM=1000,MINDELAY=1800,MAXDELAY=3600,REJECTRATE=100|修改NAS SM （DNN）拥塞控制配置，拥塞控制类型为NAS SM信令速率控制，DNN为zte.com.cn，只控制初始请求消息，拥塞控制的域值为承载建立速率1000个每秒，超过此阈值后承载建立拒绝比例为100%，下发的拒绝消息中携带的backoff time时间为1800秒到3600秒之间的随机值。
3|DEL DNNCONGESTIONCFG:DNN="zte.com.cn",|删除NAS SM （DNN）拥塞控制配置。
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|基于接收NAS MM信令速率控制
---|---
测试目的|验证NAS MM信令速率控制功能，在接收NAS MM信令速率高于配置的阈值时，该类请求消息受控。
预置条件|5GC（AMF）网元运行正常。开启NAS MM信令拥塞控制功能。
测试过程|NAS MM拥塞控制策略：设置NAS MM拥塞控制配置，拥塞控制类型为接收NAS MM信令速率，拥塞控制的域值为承载建立速率100个每秒，超过此阈值后承载建立拒绝比例为50%，下发的拒绝消息中携带的backoff time时间为600秒到1800秒之间的随机值。
通过准则|达到拥塞门限时AMF拒绝，拒绝原因值正确，携带的Back-off Timer正确，按比例拒绝。未达到拥塞门限，AMF不会因拥塞拒绝用户业务。按照接收NAS MM信令速率拥塞控制类型进行控制，查看相关性能统计正确。
测试结果|-
常见问题处理 :无。 
## ZUF-79-17-005 AMF服务化接口过载控制 
特性描述 :特性描述 :术语 :术语|含义
---|---
过载控制|在设备负荷过重时，通过限制接入的业务量，从而降低网元负荷，避免因负荷过高导致设备异常或崩溃。通常也称为过负荷控制。
描述 :定义 :当AMF因输入的业务造成系统过载时，需要减少业务输入从而对系统的负荷进行有效控制。对于服务化的SBI接口，AMF支持如下处理机制。
对于SBI接口，AMF在接近过负荷或已经过负荷的情况下，支持向对端CPNF（Control Plane NF，如SMF、PCF）发送429 Too Many Requests和503 Service Unavailable响应码，并通过Retry-After头部携带时长参数，从而在指定时长内抑制对端CPNF发送新请求。同时，AMF支持在接收到对端CPNF发送的携带Retry-After头部的429和503响应码后，在Retry-After头部指示的时长内，抑制发送到此CPNF的新请求。 
同时，AMF可以将动态负荷信息发送给NRF，供其他CP NF在选择AMF时使用。
通过上述处理，可以实现AMF服务化接口的过载控制，有效保障网络设备稳定、安全地运行。 
背景知识 :通常情况下，由于用户的异常行为或大量用户集中接入等情况引起的话务高峰，容易造成系统设备处理过载，此时若不进行有效控制，则可能发生设备故障宕机的极端情况。因此，为保障系统在这样的情况下仍然能够正常提供网络服务，需要系统设备对用户的业务请求进行一定的话务控制，从而保障系统在正常负荷状态下继续运行，并继续提供网络服务。 
应用场景 :对于AMF的服务化接口，AMF支持如下场景处理： 
在AMF接近过负荷或已经过负荷的情况下，对于某些向AMF发送消息较多的NF（如SMF和PCF），AMF支持向其发送429 Too Many Requests和503 Service Unavailable响应码指示其抑制新请求发送。 
CPNF（如UDM，SMF，NRF等NF）在发生过负荷的情况下，会向AMF发送429 Too Many Requests和503 Service Unavailable响应码，指示AMF抑制到此CPNF的新请求发送。 
AMF在负荷较高时，会将动态负荷信息（Load参数）通过NF更新消息发送给NRF。 
在本地发现缓存初始建立时，支持对AUSF、UDM、PCF的发现请求执行并发请求消息数控制。 
客户收益 :受益方|受益描述
---|---
运营商|在系统过载情况下，本特性有助于保持设备的稳定运行，从而提高系统可靠性，降低系统运行风险。
移动用户|保护设备避免其彻底故障宕机，从而能够为移动用户继续提供服务。
实现原理 :系统架构 :图1  系统架构

AMF过载控制功能系统架构及工作原理如下。 
AMF发生过载的情况下，向gNodeB发送OVERLOAD START消息，指示gNodeB减少到此AMF的话务输出。 
AMF将自身的负荷信息通过NF更新消息发送给NRF，NRF更新NF相关数据。 
对订阅了AMF状态通知的NF，如SMF/PCF，NRF主动向其发送AMF状态变更通知并携带负荷信息参数。 
同时，在NF发现的响应中，NRF将AMF的负荷信息返回给NF。 
gNodeB接收OVERLOAD START消息后，根据消息参数指示减少到此AMF的话务输出。 
其他NF如SMF从NRF获取AMF的负荷信息后，在后续的AMF选择流程中使用，优先选择负荷较低的其他AMF执行业务流程。 
除上述步骤2、3、4b外，AMF与CPNF（如SMF，PCF等）之间支持通过发送429 Too Many Requests或503 Service Unavailable响应码以及携带Retry-After头部，指示对端在指定时长内抑制新请求的发送，从而实现响应码发送方的过载控制功能。 
涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等操作
PCF|为AMF提供接入及移动性管理等用户策略服务
UDM|提供用户及会话相关的签约信息
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现，NF状态订阅及状态变更通知等功能
gNodeB|无线接入网络，在UE接入时提供无线资源及承载
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N12|ZUF-79-19-005 N12
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15
N22|ZUF-79-19-008 N22
Nnrf|ZUF-79-19-010 Nnrf
本NF/网元实现 :网元|作用
---|---
AMF|在发生过载时，AMF向NRF发送NF更新消息携带动态负荷信息。在过载解除后，AMF向NRF发送NF更新消息携带新的动态负荷信息。在自身接近过载或发生过载时，AMF向其他CPNF发送429/503响应码。同时，在接收到CPNF（包括UDM，SMF，NRF等NF）的429/503响应码后，能够在指定时间内抑制向对应的CPNF发送新的初始请求消息。在AMF本地发现缓存初始建立时，AMF支持对AUSF、UDM、PCF每种类型分别设置发现请求的并发消息数门限，超过门限的请求将不再向NRF发出请求消息，而是在短暂延时后重复尝试本地缓存，通常再次尝试时本地缓存已建立。AMF的本地缓存机制，既提高了业务流程的处理效率，也减少了到NRF的请求消息数避免NRF过载，同时也减少了网络整体的传输消息数。
NRF|接收CP NF的AMF状态订阅请求，保存订阅数据。接收AMF的NF更新消息，保存NF数据。向订阅了AMF状态的NF主动发送状态变更通知，携带负荷信息。在AMF发现请求的处理流程中，返回AMF负荷信息。
SMF、PCF、UDM|通过AMF状态变更通知消息或AMF发现响应消息获取AMF的负荷信息后，在AMF的选择过程中，减少到AMF的消息发送。在自身发生过载时，向AMF发送429/503响应码；在接收AMF发送的429/503响应码后，能够在指定时间内抑制向AMF发送新的初始请求消息。
业务流程 :AMF服务化接口过载控制功能
AMF服务化接口过载控制功能包括以下功能： 
与NRF实现AMF动态负荷上报功能。 
与CPNF实现SBI接口的429/503过载控制功能。 
在本地发现缓存初始建立时，支持对AUSF、UDM、PCF的发现请求执行并发请求消息数控制。 
AMF探测到UDM/AUSF均过载时，进行业务流控，并携带Back-off Timer指示终端延迟接入。 
与NRF实现AMF动态负荷上报功能
对于与NRF实现AMF动态负荷上报的功能，流程如[图2]所示：
图2  AMF负荷上报

流程说明： 
AMF将自身的负荷信息通过NF更新消息发送给NRF，NRF更新NF相关数据。 
对订阅了AMF状态通知的NF如SMF，NRF主动向其发送AMF状态变更通知并携带负荷信息参数。另外，在NF发现的响应消息中，NRF将AMF的负荷信息返回给NF。 
其他NF如SMF从NRF获取AMF的负荷信息后，在后续的AMF选择流程中使用，减少到AMF的消息发送。 
与CPNF实现SBI接口的429/503过载控制功能
对于SBI接口的429/503过载控制功能，处理原理如下所述。 
AMF发送HTTP响应码429 Too Many Requests/503 Service Unavailable处理机制，如[图3]所示。
图3  AMF发送HTTP响应码429 Too Many Requests/503 Service Unavailable处理机制

AMF统计各CPNF的入向请求消息数，在AMF接近过载时根据统计给CPNF回送429响应码；在AMF过载时根据统计给CPNF回送503响应码。同时通过Retry-After头部携带时长用来在此时间内抑制相应CPNF的新请求发送。 
接收429/503的CPNF在对应时间内将减少到AMF的新请求发送，时间超时后，恢复正常请求发送。 
AMF接收HTTP响应码429 Too Many Requests/503 Service Unavailable处理机制，如[图4]所示。
图4  AMF接收HTTP响应码429 Too Many Requests/503 Service Unavailable处理机制

流程说明： 
AMF接收到个别CPNF（包括NRF）的429/503响应码，其携带Retry-After头部（包含抑制时间）。 
AMF在指定时间内将抑制向此CPNF发送新的初始请求，帮助其恢复正常；在指定时间超时后，再恢复向此CPNF发送新的初始请求。 
AMF接收大量HTTP响应码429 Too Many Requests/503 Service Unavailable处理机制，如[图5]所示。
图5  AMF接收大量HTTP响应码429 Too Many Requests/503 Service Unavailable处理机制

流程说明： 
AMF接收到某类型全部或大多数CPNF的429/503响应码（携带Retry-After头部并包含抑制时间）。 
AMF根据配置启动NAS拥塞控制，携带backoff Timer给部分UE，在整体上减少输入网络的话务量。当此类型CPNF恢复正常后，AMF结束NAS拥塞控制，恢复正常话务处理。 
AMF探测到UDM/AUSF均过载时，进行业务流控，并携带Back-off Timer指示终端延迟接入
AMF探测到UDM/AUSF均过载时，进行业务流控，并携带Back-off Timer指示终端延迟接入，流程如[图6]所示。
图6  AMF探测到UDM/AUSF均过载时，进行业务流控，并携带Back-off Timer指示终端延迟接入

UE发起初始注册和注册更新过程。 
AMF触发AUSF或UDM的服务发现过程，当NRF返回发现结果后，AMF选择合适的AUSF/UDM发起鉴权或者注册更新流程。 
AMF向AUSF/UDM 1发送Nausf_UEAuthentication service/Nudm_UECM_Registration消息。 
AUSF/UDM 1返回HTTP 429/503响应码，携带Retry-After。 
AMF判断对应的AUSF/UDM 1发生拥塞，将对应的AUSF/UDM1添加到故障列表中，并选择其他正常的AUSF/UDM 2发起业务交互。 
AMF向AUSF/UDM 2发送Nausf_UEAuthentication service/Nudm_UECM_Registration消息。 
AUSF/UDM 2返回Nausf_UEAuthentication service ack/Nudm_UECM_Registration ack消息，业务交互成功。 
AMF完成后续的注册更新流程。 
UE再次发起初始注册和注册更新。 
AMF再次触发AUSF或UDM的服务发现过程之后，剔除拥塞的AUSF/UDM，选择状态正常的AUSF/UDM2发起业务流程。 
AMF向AUSF/UDM 2发送Nausf_UEAuthentication service/Nudm_UECM_Registration业务消息。 
AUSF/UDM 2返回HTTP 429/503响应码，携带Retry-After。 
AMF判断AUSF/UDM2故障，更新NF状态，将AUSF/UDM2添加到故障列表，当前用户选择的AUSF/UDM全拥塞，无可用的AUSF/UDM。 
AMF向UE发送注册更新拒绝，UE注册更新失败。 
当AUSF/UDM都发生拥塞后，UE继续发起初始注册/注册更新请求。 
AMF触发AUSF/UDM的服务发现之后，当前用户对应的AUSF/UDM全拥塞，AMF触发业务流控。 
AMF为保护AUSF/UDM，向UE发送注册更新拒绝，根据配置携带拥塞原因值#22，并携带退避定时器Back-off Timer，延迟终端接入网络。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性在如下条件下会启动NAS拥塞控制功能： 
AMF接收到某类型全部或大多数CPNF的429/503响应码（携带Retry-After头部并包含抑制时间）。 
AMF根据配置启动NAS拥塞控制，携带backoff Timer给部分UE，在整体上减少输入网络的话务量。当此类型CPNF恢复正常后，AMF结束NAS拥塞控制，恢复正常话务处理。 
遵循标准 :标准名称|章节
---|---
3GPP TS 29.510（Network Function Repository Services）|5.2.2.3 NFUpdate
3GPP TS 29.500（Technical Realization of Service Based Architecture）|6.4 Overload Control
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.30|新增NRF接口发现请求并发消息数控制、新增AMF支持UDM/AUSF均过载的流控处理。
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。具体license包括： 
AMF支持服务化接口过载控制功能 
对其他网元的要求 :gNodeB|NRF|SMF|PCF|UDM
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
CPU负荷等级配置（过负荷控制基本配置）|SET OLCPULEVELCFG
SHOW OLCPULEVELCFG|CPU负荷等级配置（过负荷控制基本配置）
过负荷控制基本配置|SET OVERLOADCFG
SHOW OVERLOADCFG|过负荷控制基本配置
SBI通用状态码控制（429、503发送）|SET GENERALSTATUSCODECFG
SHOW GENERALSTATUSCODECFG|SBI通用状态码控制（429、503发送）
SBI指定状态码控制（429、503发送）|ADD SPECSTATUSCODECFG
SET SPECSTATUSCODECFG|SBI指定状态码控制（429、503发送）
DEL SPECSTATUSCODECFG|SBI指定状态码控制（429、503发送）
SHOW SPECSTATUSCODECFG|SBI指定状态码控制（429、503发送）
AUSF拥塞控制配置|SET AUSFCONGESTIONCFG
SHOW AUSFCONGESTIONCFG|AUSF拥塞控制配置
UDM拥塞控制配置|SET UDMCONGESTIONCFG
SHOW UDMCONGESTIONCFG|UDM拥塞控制配置
服务发现流控配置|ADD SBISRVDISCOVFLOWCTRL
SET SBISRVDISCOVFLOWCTRL|服务发现流控配置
DEL SBISRVDISCOVFLOWCTRL|服务发现流控配置
SHOW SBISRVDISCOVFLOWCTRL|服务发现流控配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :SBI状态码接收控制，开启429和503状态码接收开关即可，无特殊配置。 
SBI状态码发送控制，需开启429和503状态码发送开关，根据实际情况在网管上配置通用状态码控制配置或指定状态码配置（通用状态码控制配置包括：每秒每实例接收消息门限、比例门限、执行控制的NF个数、仅发送503、重试时长最小取值、重试时长最大取值； 指定状态控制配置包括：NF实例标识、每秒每实例接收消息门限、比例门限、重试时长最小取值、重试时长最大取值）。 
SBI服务发现并发流控功能，需要根据实际情况在网管上配置相应NFType的流控配置，服务发现流控配置包括：目标NF类型、并发的服务发现次数，以及HTTPLB的122号全局参数配置（服务发现流控SUPI/GPSI号段阈值。缓存的号段数小于阈值时，服务发现流控功能生效（默认1000））。 
AMF支持探测到可用的UDM/AUSF均过载时流控处理，需开启AUSF拥塞控制配置、UDM拥塞控制配置，设置AUSF/UDM拥塞时的拥塞控制开关和最小/最大Back-off Timer值。 
配置前提 :5GC(AMF)网元运行正常。 
SBI状态码发送控制：需5GC(AMF)网元高CPU运行状态，且打开license（uMAC_AMF_7224）。 
SBI状态码接收控制：打开license（uMAC_AMF_7224）。 
配置过程 :当AMF接收到对端NF的响应消息携带状态码429或503时（对端网元过载），需根据携带的Retry-After参数时长，在该时段内不再向该NF发送消息。执行SET OVERLOADCFG命令，开启状态码接收控制功能开关。 
当AMF过载时，配置通用状态码控制配置，发送响应码429或503到对端，并携带Retry-After时长。执行SET OVERLOADCFG命令，开启状态码发送控制功能开关。执行SET GENERALSTATUSCODECFG，修改SBI通用状态码控制配置。执行SHOW OLCPULEVELCFG，查询CPU负荷等级配置。 
当AMF过载时，配置指定状态码控制配置，发送响应码429或503到对端，并携带Retry-After时长。执行SET OVERLOADCFG命令，开启状态码发送控制功能开关。执行ADD SPECSTATUSCODECFG，修改SBI指定状态码控制配置。执行SHOW OLCPULEVELCFG，查询CPU负荷等级配置。 
UDM/AUSF均过载时流控处理，配置拥塞控制开关和最小back-off timer，最大back-off timer值。执行SET AUSFCONGESTIONCFG命令，修改AUSF拥塞控制配置。执行SET UDMCONGESTIONCFG命令，修改UDM拥塞控制配置。 
在本地发现缓存初始建立时，配置服务发现并发流控配置，对AUSF、UDM、PCF的发现请求执行并发请求消息数控制。执行ADD SBISRVDISCOVFLOWCTRL命令，配置服务发现并发流控。执行SHOW GLOBAL PARAMETER命令，查询122号软参。执行ADD GLOBALPARAMETER，配置122号软参。 
配置实例 :概述 :在设备升级时，一般都需要整局重启。 
在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。除了默认开启的CPU拥塞控制来保证系统安全外，还可以单独对某个单项业务进行控制。CPU拥塞控制参数保持默认即可。 
这里仅就N2入向业务控制配置（初始注册与周期性注册）进行举例说明，出向业务与之类似，不再赘述。 
场景说明 :当AMF接收到对端NF的响应消息携带状态码429或503时（对端网元过载），需根据携带的Retry-After参数时长，在该时段内不再向该NF发送消息。 
数据规划 :配置项|参数|取值
---|---|---
修改过载控制配置|是否启用429和503状态码接收|STATUSRECVSWITCHON|STATUSRECVSWITCHON|STATUSRECVSWITCHON
配置步骤 :步骤|说明|操作
---|---|---
1|开启状态码接收控制功能开关。|SET OVERLOADCFG:STATUSRECVSWITCH="STATUSRECVSWITCHON"
场景说明 :当AMF过载时，配置通用状态码控制配置，发送响应码429或503到对端，并携带Retry-After时长。 
数据规划 :配置项|参数|取值
---|---|---
修改过载控制配置|是否启用429和503状态码发送|STATUSSENDSWITCHON|STATUSSENDSWITCHON|STATUSSENDSWITCHON
修改SBI通用状态码控制配置|NF类型|SMF|SMF|SMF
每秒每实例接收消息门限|修改SBI通用状态码控制配置|100|100|100
比例门限|修改SBI通用状态码控制配置|50|50|50
执行控制的NF个数|修改SBI通用状态码控制配置|10|10|10
仅发送503|修改SBI通用状态码控制配置|NO|NO|NO
重试时长最小取值（秒）|修改SBI通用状态码控制配置|10|10|10
重试时长最大取值（秒）|修改SBI通用状态码控制配置|30|30|30
配置步骤 :步骤|说明|操作
---|---|---
1|开启状态码发送控制功能开关。|SET OVERLOADCFG:STATUSSENDSWITCH="STATUSSENDSWITCHON"
2|修改SBI通用状态码控制配置。|SET GENERALSTATUSCODECFG:NFTYPE="SMF",MSGTHRESHOLD=100,JUDGEPERCENT=50,CTRLTOPNUM=10,ONLY503="NO",MINRETRYAFTER=10,MAXRETRYAFTER=30
3|查询CPU负荷等级配置。|SHOW OLCPULEVELCFG
场景说明 :当AMF过载时，配置指定状态码控制配置，发送响应码429或503到对端，并携带Retry-After时长。 
数据规划 :配置项|参数|取值
---|---|---
修改过载控制配置|是否启用429和503状态码发送|STATUSSENDSWITCHON|STATUSSENDSWITCHON|STATUSSENDSWITCHON
增加SBI指定状态码控制配置|NF实例标识|SMF_01|SMF_01|SMF_01
每秒每实例接收消息门限|增加SBI指定状态码控制配置|1000|1000|1000
比例门限|增加SBI指定状态码控制配置|50|50|50
重试时长最小取值（秒）|增加SBI指定状态码控制配置|10|10|10
重试时长最大取值（秒）|增加SBI指定状态码控制配置|30|30|30
配置步骤 :步骤|说明|操作
---|---|---
1|开启状态码发送控制功能开关。|SET OVERLOADCFG:STATUSSENDSWITCH="STATUSSENDSWITCHON"
2|修改SBI指定状态码控制配置。|ADD SPECSTATUSCODECFG:NFID="SMF_01",MSGTHRESHOLD=1000,JUDGEPERCENT=50,MINRETRYAFTER=10,MAXRETRYAFTER=30
3|查询CPU负荷等级配置。|SHOW OLCPULEVELCFG
场景说明 :AMF探测到可用的AUSF均过载，对终端接入请求进行流控，并携带back-off timer指示终端延迟接入。 
数据规划 :配置项|参数|取值
---|---|---
修改AUSF拥塞控制配置|支持AUSF全拥塞控制|SPRT|SPRT|SPRT
携带Back-off timer|修改AUSF拥塞控制配置|CARRY|CARRY|CARRY
back-off timer最小值(秒)|修改AUSF拥塞控制配置|10|10|10
back-off timer最大值(秒)|修改AUSF拥塞控制配置|120|120|120
配置步骤 :步骤|说明|操作
---|---|---
1|修改AUSF拥塞控制配置。|SET AUSFCONGESTIONCFG:IFSUPAUSFCONGCTL="SPRT",IFCARRYBACKOFFTIME="CARRY",MINBACKOFFTIME=10,MAXBACKOFFTIME=120
场景说明 :AMF探测到可用的UDM均过载，对终端接入请求进行流控，并携带back-off timer指示终端延迟接入。 
数据规划 :配置项|参数|取值
---|---|---
修改UDM拥塞控制配置|支持UDM全拥塞控制|SPRT|SPRT|SPRT
携带Back-off timer|修改UDM拥塞控制配置|CARRY|CARRY|CARRY
back-off timer最小值(秒)|修改UDM拥塞控制配置|10|10|10
back-off timer最大值(秒)|修改UDM拥塞控制配置|120|120|120
配置步骤 :步骤|说明|操作
---|---|---
1|修改UDM拥塞控制配置。|SET UDMCONGESTIONCFG:IFSUPAUSFCONGCTL="SPRT",IFCARRYBACKOFFTIME="CARRY",MINBACKOFFTIME=10,MAXBACKOFFTIME=120
场景说明 :在HTTPLB弹扩、重启上电等场景，新上电SBI-GW没有本地缓存，大量业务导致单位时间内向NRF发送大量发现请求，对NRF造成冲击。可以配置服务发现并发流控功能，在本地发现缓存初始建立时，对AUSF、UDM、PCF的发现请求消息数进行控制。 
数据规划 :配置项|参数|取值
---|---|---
新增服务发现流控配置|目标NF类型|AUSF或UDM|AUSF或UDM|AUSF或UDM
并发的服务发现次数|新增服务发现流控配置|8|8|8
修改HTTPLB全局参数|编号|122|122|122
参数值|修改HTTPLB全局参数|1000（默认值，根据运营商网络实际号段数修改）|1000（默认值，根据运营商网络实际号段数修改）|1000（默认值，根据运营商网络实际号段数修改）
配置步骤 :步骤|说明|操作
---|---|---
1|新增服务发现流控配置（AUSF）|ADD SBISRVDISCOVFLOWCTRL:TARGETNFTYPE="AUSF_TYPE",THRESHOLD=8
2|新增服务发现流控配置（UDM）|ADD SBISRVDISCOVFLOWCTRL:TARGETNFTYPE="UDM_TYPE",THRESHOLD=8
3|修改HTTPLB 122号全局参数|ADD GLOBALPARAMETER:ID=122,VALUE=1000
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|SBI状态码接收控制
---|---
测试目的|当对端网元发送429或503响应码到本端AMF，本端AMF在Retry-After时长内不再发送消息到该网元。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|对端网元发送429或503响应码到本端AMF。
通过准则|后续业务流程，本端AMF不再选择该过载网元。超过Retry-After时长后，会继续选择该网元。
测试结果|–
测试项目|SBI状态码发送控制
---|---
测试目的|当本端AMF过载时，能下发429或503响应码，并携带Retry-After时长到对端网元。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|当CPU使用率超过门限值时，对端网元（SMF、PCF）发起大量请求消息到本端AMF，请求消息超过门限，本端AMF下发429或503响应码，并携带Retry-After到对端网元。
通过准则|本端AMF能选出请求最多的对端网元并下发429或503响应码，并携带Retry-After时长。
测试结果|–
测试项目|服务发现并发流控
---|---
测试目的|在本地发现缓存初始建立时，对AUSF、UDM的发现请求消息数进行控制。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式已成功对接NRF、AUSF、UDM等周边NF，且AUSF、UDM号段数超过1000
测试过程|大量用户并发注册，触发AMF向NRF并发发现AUSF、UDM。
通过准则|每SC同一时刻向NRF发送的发现消息次数符合服务发现并发流控配置的消息数。
测试结果|–
测试项目|AMF支持探测到可用的UDM/AUSF均过载时处理
---|---
测试目的|AMF支持探测到可用的UDM/AUSF均过载，通过拥塞控制，控制终端的接入速率，降低对AUSF/UDM网元的冲击，保障网络稳定运行。
预置条件|5GC网络功能正常(R)AN已成功对接AMFUE支持5GC模式
测试过程|AMF支持探测到可用的UDM/AUSF均过载。
通过准则|本端AMF能够向UE发送Back-off Time值，控制终端的接入速率。
测试结果|–
常见问题处理 :无。 
## ZUF-79-17-006 终端异常信令管控 
特性描述 :特性描述 :描述 :定义 :终端异常信令管控是指当终端在不停的尝试业务，但是却一直异常时，AMF会采取一定的措施，减少终端触发的信令，避免引起网络拥塞。
AMF对终端异常信令管控包含如下功能： 
注册请求异常信令管控 
业务请求异常信令管控 
PDU会话建立异常信令管控 
背景知识 :信令风暴是指网络侧收到了的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。 
引发信令风暴的原因有很多，主要包括如下原因： 
特殊事件：由于集会、节日、传输中断等导致短时间内大量用户发起业务，带来的信令冲击超过网络的处理能力。 
设备故障：5G核心网的设备故障、重启或用户卸载等场景，触发大量用户同时重新连接网络或者触发用户不停尝试业务流程，从而触发信令风暴。 
终端问题：因出现下述原因，终端业务连续失败后，终端会不断重发信令请求，包括附着请求、业务请求、PDN连接请求会频繁发生。当一定时间内信令请求数很多，即将超过网络信令资源的处理能力时，则会触发信令风暴。终端DNN或其他参数错误终端中毒终端恶意攻击网络传输中断区域限制业务服务器Down其他原因 
不同原因导致的信令风暴，其抑制手段也不同： 
特殊事件：AMF启用过负荷控制，保证发生信令风暴时正常服务。 
设备故障：对于触发大量用户同时重新接入网络场景，AMF启用过负荷控制，保证发生信令风暴时正常服务。对于触发用户不停尝试业务流程，AMF对业务请求、PDU会话建立请求进行信令黑名单控制，避免网络拥塞。 
终端问题：AMF对注册请求、业务请求、PDU会话建立请求进行信令黑名单控制，避免网络拥塞，化解信令风暴。 
应用场景 :由于终端原因导致终端不停尝试注册、业务请求或者PDU会话建立流程，引起信令风暴。
在此场景下，通过网络侧对注册请求、业务请求以及PDU会话建立请求进行异常信令管控，减少终端触发的业务信令，避免网络拥塞，化解信令风暴。 
由于网络原因，导致终端不停尝试业务请求或PDU会话建立流程。
在此场景下，通过网络侧对业务请求进行异常信令管控，使得用户重新注册，将用户从不停业务请求的死循环中解脱出来。通过网络侧对PDU会话请求进行异常信令管控，使得用户尝试接入到4G网络，避免用户因5G网络故障而不停触发PDU会话建立，却始终无法执行正常的移动通信业务。 
客户收益 :受益方|受益描述
---|---
运营商|确保网络设备安全运行，减轻网络信令压力，化解信令风暴，避免网络拥塞。提高用户满意度，保障用户使用数据业务。提升运营商KPI指标，抑制终端频繁发起信令请求导致的业务失败，提升了业务成功率。
移动用户|用户享受更稳定和更可靠的网络服务。
实现原理 :系统架构 :终端异常信令管控网络架构如[图1]所示。
图1  终端异常信令管控网络架构

涉及的网元 :网元名称|网元作用
---|---
AMF|基于UE粒度，检测用户是否存在信令风暴，并执行异常信令管控措施，抑制信令风暴。
SMF|支持Fake DNN的PDU会话建立。
协议栈 :接口|描述|协议栈
---|---|---
N1|UE与AMF间逻辑接口。|参见ZUF-79-19-001 N1
N2|(R)AN与AMF间逻辑接口。|参见ZUF-79-19-002 N2
N11|AMF与SMF间逻辑接口。|参见ZUF-79-19-004 N11
本网元实现 :在一定时间间隔内的对每个用户的信令进行检测，检测是否存在注册请求信令、业务请求信令以及PDU会话建立的信令风暴。 
当检测到出现信令风暴时，将用户置入黑名单，进行信令管控，比如丢弃信令，或者下发拒绝消息。 
动态查询异常管控状态，包括：查询特定用户的管控状态。把特定用户从管控黑名单中删除。查询处于管控黑名单的用户名单。 
业务流程 :注册请求异常信令管控流程如[图2]所示。
图2  注册请求异常信令管控流程图

AMF以UE为颗粒度，记录单位时间T1内产生的Registration Request信令数，当单位时间信令数目没超过阈值N1时，AMF按照正常流程处理用户信令，对单位时间信令数超过阈值N1的UE进行的异常信令进行控制，控制方法如下： 
AMF将该用户加入黑名单，注册拒绝，携带#7（5GS services not allowed）原因值（原因值可配置），并启动黑名单定时器TT1。 
TT1超时前如果继续收到Registration Request，则进入步骤2。 
如果直到TT1超时仍未收到Registration Request，则将用户从黑名单移除，正常处理后续消息。 
网络发起Deregistration（re-registration not required）。 
TT1超时前如果继续收到Registration Request，则进入步骤3。 
如果直到TT1超时仍未收到Registration Request，则将用户从黑名单移除，正常处理后续消息。 
AMF丢弃该用户的信令，对这部分丢弃的信令单独统计。如果黑名单TT1超时时将用户从黑名单移除。 
业务请求异常信令管控流程如[图3]所示。
图3  业务请求异常信令管控流程图

AMF以UE为颗粒度，记录单位时间T2内产生的service request信令数，当单位时间信令数目没超过阈值N2时，AMF按照正常流程处理用户信令，对单位时间信令数超过阈值N2的UE进行的异常信令进行控制。 
控制方法如下： 
根据不同情况，执行不同的控制方法： 
如果...|那么...
---|---
不支持业务请求异常信令管控优化|AMF将该用户加入黑名单，业务请求拒绝，携带#7（5GS services not allowed）原因值（原因值可配置），并启动黑名单定时器TT2。如果TT2超时前继续收到Service Request，则进入步骤2。如果直到TT2超时仍未收到Service Request，则将用户从黑名单移除，正常处理后续消息。
支持业务请求异常信令管控优化|AMF将该用户加入黑名单，业务请求拒绝，携带#10（Implicitly de-registered）原因值（原因值可配置），并启动黑名单定时器TT2。如果TT2超时前继续收到Registration Request，则进入步骤2。如果直到TT2超时仍未收到Service Request，则将用户从黑名单移除，正常处理后续消息。
根据不同情况，执行不同的控制方法： 
如果...|那么...
---|---
不支持业务请求异常信令管控优化|网络发起Deregistration（re-registration not required）。TT2超时前如果收到Registration Request，则进入步骤3。如果直到TT2超时仍未收到Registration Request，则将用户从黑名单移除，正常处理后续消息。
支持业务请求异常信令管控优化|AMF将用户从黑名单中移出，继续执行注册请求。黑名单TT2超时时将用户从黑名单移除。流程结束。
AMF丢弃该用户的信令，对这部分丢弃的信令单独统计。如果黑名单TT2超时时将用户从黑名单移除。 
PDU会话建立异常信令管控流程如[图4]所示。
图4  PDU会话建立异常信令管控流程图

AMF以UE为颗粒度，记录单位时间T3内产生的PDU会话建立信令数，当单位时间信令数目没超过阈值N3时，AMF按照正常流程处理用户信令，对单位时间信令数超过阈值N3的UE进行的异常信令进行控制。 
若“支持PDU会话建立异常信令管控优化”开关关闭，控制方法如下： 
AMF将该用户加入黑名单，并下发DL NAS TRANSPORT，携带#7（5GS services not allowed）原因值（原因值可配置），并启动黑名单定时器TT3。 
TT3超时前如果继续收到PDU会话建立请求，则进入步骤2。 
如果直到TT3超时仍未收到PDU会话建立请求，则将用户从黑名单移除，正常处理后续消息。 
根据不同情况下，执行不同的控制方法： 
如果...|那么...
---|---
不支持业务请求异常信令管控优化|终端继续发起PDU会话建立请求信令时，AMF以本地配置的Fake DNN（能建立但是无法上网）让终端建立成功。如果直到TT3超时仍未收到PDU会话建立请求，则将用户从黑名单移除，终端再发起PDU会话建立请求时使用正常DNN。如果本地未配置Fake DNN或Fake DNN PDU建立失败，则进入步骤3。如果TT3超时前继续收到PDU会话建立请求，则进入步骤3。
支持业务请求异常信令管控优化|网络发起Deregistration（re-registration not required）。如果TT3超时前继续收到Registration Request，黑名单TT3超时时将用户从黑名单移除。如果直到TT3超时仍未收到Registration Request，则将用户从黑名单移除，正常处理后续消息。
据不同情况下，执行不同的控制方法： 
如果...|那么...
---|---
不支持业务请求异常信令管控优化|网络发起Deregistration（re-registration not required）。如果TT3超时前继续收到Registration Request，则进入步骤4。如果直到TT3超时仍未收到Registration Request，则将用户从黑名单移除，正常处理后续消息。
支持业务请求异常信令管控优化|AMF下发注册拒绝，携带#111（Protocol error, unspecified）原因值（原因值可配置）。如果黑名单TT3超时时将用户从黑名单移除。流程结束。
AMF丢弃该用户的信令，对这部分丢弃的信令单独统计。如果黑名单TT3超时时将用户从黑名单移除。 
异常管控状态查询流程如[图5]所示。
图5  异常管控状态查询流程图

当需要获取某特定用户的信令管控状态，操作维护人员可以通过EM查询该用户的信令管控状态，查询请求中包含用户SUPI，返回的响应中指示当前用户信令管控状态。
当需要将用户从异常信令管控黑名单中删除时，操作维护人员可以通过EM，将该用户从异常管控黑名单中删除。 
当需要查询某个SC上异常管控黑名单时，操作维护人员可以通过EM，查询该SC上异常管控黑名单中的用户列表。
系统影响 :在系统出现信令风暴时，开启本功能，可以减少终端的信令业务，从而化解信令风暴。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :该特性不涉及标准协议。 
特性能力 :类型|能力
---|---
黑名单用户容量|黑名单用户容量等同于注册上下文容量的1.2倍。
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.20|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为AMF支持异常信令管控（license ID：7231），此项目显示为支持，表示AMF支持异常信令管控功能。
对其他网元的要求 :UE|NG-RAN|SMF
---|---|---
√|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :Fake DNN需要全网规划。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令AMF异常信令管控策略配置SET ABNORMALSIGMCPOLICYSHOW ABNORMALSIGMCPOLICYAMF异常信令管控配置SET ABNORMALSIGMCCONFIGSHOW ABNORMALSIGMCCONFIGAMF异常信令管控优化配置SET ABNORMALSIGMCOPTSHOW ABNORMALSIGMCOPT 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理命令命令使用说明SHOW USERSIGNALCONTROLSTATE查询用户的异常信令管控状态。DELETE USERSIGNALCONTROLBLACKLIST把用户从异常信令管控黑名单中删除。SHOW SIGNALBLACKUSER查询信令黑名单用户。 
性能统计 :测量类型|描述
---|---
异常信令管控流程测量|编号为51009开头的所有计数器
异常信令管控用户数测量|编号为51082开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :当智能终端网络信令短时频繁成功或终端网络信令连续失败，造成AMF收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，AMF此时需要进行异常信令管控。 
AMF异常信令管控配置成功后，AMF可以根据各配置值，采取一定的措施，减少网络侧要处理的信令，化解信令风暴，避免网络拥塞，确保网络设备安全运行，有力保障不在信令黑名单中的用户使用数据业务和其他业务的成功率。 
配置前提 :AMF运行正常。 
AMF与网管之间连接正常。 
配置过程 :执行[SET ABNORMALSIGMCPOLICY]命令，进行AMF异常信令管控的策略配置。
执行[SET ABNORMALSIGMCCONFIG]命令，进行AMF异常信令管控的参数配置。
（可选）执行[SET ABNORMALSIGMCOPT]命令，进行AMF异常信令管控优化配置。
配置实例 :场景一 :场景说明
由于终端原因导致终端不停尝试注册、业务请求或者PDU会话建立流程，引起信令风暴。 
在此场景下，通过网络侧对注册请求、业务请求以及PDU会话建立请求进行异常信令管控，减少终端触发的业务信令，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
AMF异常信令管控的策略配置|AMF是否支持异常信令管控|YES
AMF异常信令管控的参数配置|注册请求信令统计周期|720秒
注册请求最大信令数|AMF异常信令管控的参数配置|15
注册拒绝原因值|AMF异常信令管控的参数配置|7
注册请求黑名单定时器时长|AMF异常信令管控的参数配置|1200秒
业务请求信令统计周期|AMF异常信令管控的参数配置|720秒
业务请求最大信令数|AMF异常信令管控的参数配置|30
业务请求拒绝原因值|AMF异常信令管控的参数配置|7
业务请求黑名单定时器时长|AMF异常信令管控的参数配置|1200秒
PDU会话建立请求信令统计周期|AMF异常信令管控的参数配置|720秒
PDU会话建立请求最大信令数|AMF异常信令管控的参数配置|16
PDU会话建立请求拒绝原因值|AMF异常信令管控的参数配置|7
PDU会话建立请求黑名单定时器时长|AMF异常信令管控的参数配置|1200秒
FAKE DNN名称|AMF异常信令管控的参数配置|NULL
AMF异常信令管控优化配置|支持业务请求异常信令管控优化|不支持
支持PDU会话建立异常信令管控优化|AMF异常信令管控优化配置|不支持
配置步骤
步骤|说明|命令
---|---|---
1|设置AMF异常信令管控的策略配置。|SET ABNORMALSIGMCPOLICY:SUPPORTSIGCTRL="YES"
2|设置AMF异常信令管控的参数配置。|SET ABNORMALSIGMCCONFIG:REGSTATPERIOD=720,REGMAXSIGNUM=15,REGREJECTCAUSE=7,REGBLACKLISTDURATION=1200,SRSTATPERIOD=720,SRMAXSIGNUM=30,SRREJECTCAUSE=7,SRBLACKLISTDURATION=1200,PDUESTSTATPERIOD=720,PDUESTMAXSIGNUM=16,PDUESTREJECTCAUSE=7,PDUESTBLACKDURATION=1200,FAKEDNN="NULL"
3|设置AMF异常信令管控优化配置。|SET ABNORMALSIGMCOPT:BSUPSRSIGMCOPT="NOTSUPPORT",BSUPPDUESTSIGMCOPT="NOTSUPPORT"
场景二 :场景说明
由于网络原因，导致终端不停尝试业务请求或PDU会话建立流程。 
在此场景下，通过网络侧对业务请求进行异常信令管控，使得用户重新注册，将用户从不停业务请求的死循环中解脱出来。通过网络侧对PDU会话请求进行异常信令管控，使得用户尝试接入到4G，避免用户因5G网络故障而不停触发PDU会话建立，却始终无法执行正常的移动通信业务。 
数据规划
配置项|参数名称|取值
---|---|---
AMF异常信令管控的策略配置|AMF是否支持异常信令管控|YES
AMF异常信令管控优化配置|支持业务请求异常信令管控优化|支持
业务请求拒绝原因值|AMF异常信令管控优化配置|10
支持PDU会话建立异常信令管控优化|AMF异常信令管控优化配置|支持
因PDU会话异常信令管控导致的注册拒绝原因|AMF异常信令管控优化配置|111
配置步骤
步骤|说明|命令
---|---|---
1|设置AMF异常信令管控的策略配置。|SET ABNORMALSIGMCPOLICY:SUPPORTSIGCTRL="YES"
2|设置AMF异常信令管控优化配置（使用默认即可）。|SET ABNORMALSIGMCOPT:BSUPSRSIGMCOPT="SUPPORT",BSRREJCAUSE=10,BSUPPDUESTSIGMCOPT="SUPPORT",BREGREJCAUSE=111
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|统计周期内业务请求信令数大于配置阈值，进入管控黑名单，定时器内UE再次发起多次的业务请求
---|---
测试目的|验证AMF业务请求流程异常信令管控功能的正确性，对终端发起的业务请求信令风暴能够有效地进行管控。
预置条件|AMF上电正常，AMF支持异常信令管控的license开关打开。
测试过程|业务请求信令统计周期600s，最大信令数3条，黑名单定时器300s。用户注册成功，建立PDU会话，进行N2释放，第一次UE触发空闲态信令类型业务请求，AMF正常处理。第二次UE又发起连接态信令业务请求，AMF正常处理。第三次UE发起连接态数据类型业务请求，信令统计周期内达到最大允许业务请求信令数，AMF正常处理。用户发起N2释放，处于空闲态，通过N1N2transfer流程会触发网络侧寻呼，作为响应UE发起MT类型的业务请求，AMF发起业务请求拒绝。黑名单定时器内UE发起紧急业务请求，AMF触发网络侧去注册流程。黑名单定时器内，UE发起初始注册，AMF丢弃该信令。黑名单定时器超时，UE发起初始注册，AMF正常处理。
通过准则|当统计周期内业务请求信令数达到配置阈值3时，AMF发起业务请求拒绝，携带原因值根据配置决定。当300s内继续收到业务请求时，AMF发起Deregistration。当300s内收到初始注册时，AMF丢弃不作处理，观察失败观察。300s后AMF能正常处理初始注册流程。
测试结果|-
测试项目|异常信令管控优化开关打开后，统计周期内业务请求信令数大于配置阈值，进入管控黑名单，定时器内UE再次发起初始注册
---|---
测试目的|验证AMF业务请求流程异常信令管控功能的正确性，对终端发起的业务请求信令风暴能够有效地进行管控。
预置条件|AMF上电正常，AMF支持异常信令管控的license开关打开。
测试过程|业务请求信令统计周期600s，最大信令数3条，黑名单定时器300s。用户注册成功，建立PDU会话，进行N2释放，第一次UE触发空闲态信令类型业务请求，AMF正常处理。第二次UE又发起连接态信令业务请求，AMF正常处理。第三次UE发起连接态数据类型业务请求，信令统计周期内达到最大允许业务请求信令数，AMF正常处理。用户发起N2释放，处于空闲态，通过N1N2transfer流程会触发网络侧寻呼，作为响应UE发起MT类型的业务请求，AMF发起业务请求拒绝。黑名单定时器内，UE发起初始注册，AMF恢复用户白名单，正常处理。
通过准则|当统计周期内业务请求信令数达到配置阈值3时，AMF发起业务请求拒绝，携带原因值根据优化配置决定。300s内AMF仍然能正常处理初始注册流程。
测试结果|-
常见问题处理 :无 
## ZUF-79-17-009 动态流控 
特性描述 :特性描述 :描述 :定义 :动态流控功能是指AMF周边网元（当前只支持AUSF/UDM网元即N8，N12接口）存在过载风险时，AMF根据周边网元返回的响应消息，计算到周边网元的业务成功率，判断周边网元拥塞程度，再通过自动调节N2口接收的初始注册流程、局间的位置改变注册流程，全量容灾场景下的业务请求流程，从而控制向周边网元放通的业务数，最终达到保护周边网元的目的，并保证用户以最大的速率接入网络。 
背景知识 :拥塞和过负荷控制是保障网元运行安全的重要措施。过负荷控制功能指在设备处理的业务量超过了规定值时，需要采取保护措施以限制处理的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。 
核心网在实际运行中，特定区域大批用户涌入引发的注册信令、频繁跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等造成单位时间业务量陡增，一旦出现过负荷，由于网络中不同类型的网元处理能力和资源各不相同，往往会出现由某个网元故障或宕机导致的全网瘫痪。因此为保障网络运行正常，需要从源头上对业务和用户实施控制，来完成整个网络的过负荷控制。随着网络部署越来越集中、网络应用越来越广泛，用户量在不断增加，AMF各周边接口和网元拥塞的可能性也越来越大，经常会出现因为某些特定的原因导致用户短时间内暴发超过正常话务模型的业务，为了保证周边网元的安全，保证用户接通率和接续时长，改善用户体验，引入本特性（即动态流控功能）。 
应用场景 :动态流控功能应用于5GC网络运行中，当AMF周边网元（AUSF/UDM）发生拥塞时，通过自动调节N2口的注册，业务请求等业务速率，减少到周边网元的信令，从而保护周边网元。 
场景一：升级过程中系统重启升级过程中，大量用户重新附着，用户到周边网元的请求同时发起。动态流控可以预防周边网元发生拥塞和瘫痪。 
场景二：系统异常掉电重启系统异常掉电重启，突发大量业务，用户重新注册，导致周边网元请求消息数量也突增，会导致周边网元接口链路拥塞、网元过载，业务成功率明显下降。使用动态流控功能，可动态降低N2口的业务放通率，减小信令拥塞对周边网元的影响。 
场景三：举办大型赛事、节假日、传输网中断等造成大量用户发起业务，对网络造成短暂的冲击此场景下，短时间内会接入超过估算话务模型的业务量，网元自身CPU占用率上升的同时，到周边网元的信令也会增加很多，会导致周边网元拥塞。 
场景四：网络运行中，周边网元能力因扩容增强时，可动态增加放通率，最大速率接入用户，减少用户接续时长此场景下，随着网络运行以及用户容量扩容，网元能力发生变化，动态流控可以动态监测周边网元能力，动态调整到周边网元的放通率，既保护周边网元，同时不影响用户的接入。 
客户收益 :受益方|受益描述
---|---
运营商|通过动态流控，保障UDM/AUSF网元的稳定性。提高UE整网接入成功率，减少周边网元的拥塞或过载瘫痪，提高网络的稳定性，从而提高用户满意度，增加收益。
移动用户|在大量突发业务冲击的场景下，减少因周边网元链路拥塞或过载而导致的用户不能使用业务的问题，动态提高周边网元拥塞时用户的接通率，更大程度的提高用户满意度，享受稳定可靠的网络服务。
实现原理 :系统架构 :系统架构如[图1]所示。
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
AMF|动态监测N8、N12接口的业务成功率和初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求）。在初次接入本局业务量（包括初始注册，GUTI非本局的注册，业务请求）增加，且N8、N12接口成功率降低时，启动动态流控。流控期间，根据周边网元业务成功率，动态调整初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求）的放通率。持续一段时间业务量低于控制门限，解除拥塞控制。
AUSF/UDM|设备发生拥塞时，返回失败的响应或丢弃消息，AMF动态监测业务成功率。
协议栈 :N8/N12属于SBI接口，SBI接口使用HTTP/2协议，统一了信令接口的协议和操作行为，提供了接口功能扩展能力、接口访问性能自适应调整能力，以及接口安全互操作能力。SBI接口协议栈如下图所示。 

本网元实现 :动态流控原理在系统升级重启、重大节日活动、容灾、周边网元故障等情况下，大量用户短时间内接入到AMF，导致AMF各周边接口网元的请求消息快速增加，可能会导致接口拥塞或周边网元设备过载。为了保证周边网元安全以及用户接入成功率和接续时长，通过动态流控功能，自动调节N2接口的初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求）的接入速率，从而避免周边接口拥塞或网元过载。动态流控原理示意图如下图所示。 
动态流控原理说明如下： 
设置周边网元（AUSF/UDM）负荷拥塞控制的启控初始门限和启控最大门限等参数。当AMF接收到UE的初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求）速率超过“起控初始门限（即“初始限制的接入业务最大数量(单SC每秒)”参数）”，动态流控系统监测周边网元的业务成功率，通常情况下，周边网元还未过载。 
当业务消息速率不断增加，超过“起控最大门限（即“允许通过的接入业务最大数量（单SC每秒）”参数）”时， 开始控制N2口业务消息速率，控制发往周边网元的业务请求消息。 
流控周期内，发现周边网元未过载，业务成功率高于设置的门限，动态根据步长增加初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求）放通率。 
后续流控周期内，如果周边网元业务成功率依然高于设置的门限，则继续加大业务放通率，保证用户快速接入网络。 
当系统调整的接入速率超过周边网元的处理能力，检测到流控周期内周边网元业务成功率低于设置的门限，则向下调整业务放通率， 减少向相邻网元的业务量，保护周边网元。 
随着业务量下降，周边网元恢复正常，保持当前业务放通率。 
随着用户持续接入网络，业务速率持续下降，网络恢复正常，再等待保护时长后，解除本次拥塞流控。 
业务流程 :动态流控流程如[图2]所示。
图2  动态流控流程

由于系统升级或异常重启、重大节日等场景，导致大量用户发起到新的AMF重选接入。 
AMF接受大量非本局的业务即初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求）导致业务速率达到动态流控的启控初始门限，AMF开始判断周边网元的处理能力，处理如下： 
周边网元业务成功率低于门限，开始动态流控，限制部分用户接入，防止周边网元拥塞过载。 
周边网元业务成功率高于门限，不限制用户接入，随着业务量上升，超过系统允许的启控最大门限，则开始限制超过门限的用户接入，将业务放通率控制在一定范围之内，防止周边网元拥塞。 
对于被限制接入的初次接入本局业务（包括初始注册，GUTI非本局的注册，业务请求），系统根据配置策略选择丢弃或拒绝。 
允许通过的业务，则被系统正常处理同标准流程处理。 
被允许放通的非本局业务，正常到AUSF/UDM进行注册/信息获取。 
AMF继续监控N8，N12接口的成功率。用于下一周期的判断。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :当通常周边网元设备与一个AMF POOL中的多个AMF相连，保护该周边网元需要所有的AMF开启动态流控功能， 否则达不到保护周边网元的目的。 
当前功能不支持按区分局向来统计成功率。要求各个AUSF、UDM的能力是相近的。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :该特性不涉及标准内容。 
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.22.30|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|gNodeB|AUSF|UDM|SMF
---|---|---|---|---
-|-|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :初始使用时，为了达到最好效果需要根据了解周边网元的能力，并设置最优值。 
再次使用时，可以根据自动学习的参数值进行设置。 
O&M相关 :命令 :命令名称|描述
---|---
AMF自动业务控制策略配置|SET AMF AUTOCTL BASIC PARA
SHOW AMF AUTOCTL BASIC PARA|AMF自动业务控制策略配置
AMF N8N12 自动业务控制策略|SET AMF N8N12 AUTO CNGCTL
SHOW AMF N8N12 AUTO CNGCTL|AMF N8N12 自动业务控制策略
性能统计 :性能计数器
---
C510280057 由于N8N12自动过负荷控制丢弃的初始注册请求个数C510280058 由于N8N12自动过负荷控制拒绝的初始注册请求个数C510280059 由于N8N12自动过负荷控制丢弃的局间位置改变注册请求个数C510280060 由于N8N12自动过负荷控制拒绝的局间位置改变注册请求个数C510280061 由于N8N12自动过负荷控制丢弃的全量容灾导致的他局用户注册请求个数C510280062 由于N8N12自动过负荷控制拒绝的全量容灾导致的他局用户注册请求个数C510280063 由于N8N12自动过负荷控制丢弃的全量容灾导致的他局业务请求个数C510280064 由于N8N12自动过负荷控制拒绝的全量容灾导致的他局业务请求个数
告警和通知 :告警和通知
---
3305504772 业务过负荷告警
业务观察/失败观察 :该特性不涉及业务观察/失败观察。 
话单与计费 :该特性不涉及话单与计费。 
特性配置 :特性配置 :配置说明 :通过设置AMF自动业务控制基本参数与设置AMF N8N12自动业务控制策略的配置，实现N8N12接口自动流控功能。 
配置前提 :5GC(AMF)网元运行正常，了解周边网元能力。 
配置过程 :执行[SET AMF AUTOCTL BASIC PARA]命令，设置AMF自动业务控制基本参数。
执行[SET AMF N8N12 AUTO CNGCTL]命令，设置AMF的N8N12自动业务控制策略。
配置实例 :场景说明 :当注册或业务请求流程较多时，会增加网络中AUSF、UDM网元的负荷。此场景下，当AMF的周边网元（AUSF，UDM等）存在过载风险时，AMF根据周边网元返回的业务成功率的周期变化，判断周边网元的负荷拥塞情况，控制入向业务速率的方式来保护周边网元，通过调节初始注册、Inter-AMF 业务请求、非本局GUTI的注册等业务流程的处理速率，控制向周边网元发往的请求数，从而保护周边网元的目的。 
一般场景下，只需要设置开启自动学习和AMF N8N12 自动业务控制策略是否开启，其他配置使用默认配置即可。 
数据规划 :配置项|参数|取值
---|---|---
AMF自动业务控制基本参数|业务采集周期（秒）|3（默认配置参数，无需设置）
评判周期/业务控制周期|AMF自动业务控制基本参数|3（默认配置参数，无需设置）
评判方式|AMF自动业务控制基本参数|混合周期方式（默认配置参数，无需设置）
拥塞控制时是否上报日志|AMF自动业务控制基本参数|是（默认配置参数，无需设置）
被控制的流程|AMF自动业务控制基本参数|初始注册流程&局间位置改变注册流程&全量容灾导致的他局用户注册流程&全量容灾导致的他局业务请求流程（默认配置参数，无需设置）
是否开启自动学习|AMF自动业务控制基本参数|开启
学习时间|AMF自动业务控制基本参数|六点&七点&八点&九点&十点&十一点&十二点&十三点&十四点&十五点&十六点&十七点&十八点&十九点&二十点&二十一点&二十二点&二十三点（默认配置参数，无需设置）
AMF N8N12 自动业务控制策略|是否开启流控|是
触发拥塞的接入业务通过数量（单SC每秒）|AMF N8N12 自动业务控制策略|120（默认配置参数，无需设置）
初始限制的接入业务最大数量(单SC每秒)|AMF N8N12 自动业务控制策略|300（默认配置参数，无需设置）
允许通过的接入业务最大数量（单SC每秒）|AMF N8N12 自动业务控制策略|1800（默认配置参数，无需设置）
触发拥塞的业务成功率(%)|AMF N8N12 自动业务控制策略|80（默认配置参数，无需设置）
触发提升通过业务数量的业务成功率(%)|AMF N8N12 自动业务控制策略|90（默认配置参数，无需设置）
接入业务控制步长|AMF N8N12 自动业务控制策略|10（默认配置参数，无需设置）
步长使用方法|AMF N8N12 自动业务控制策略|固定步长（默认配置参数，无需设置）
控制持续时间（分钟）|AMF N8N12 自动业务控制策略|5（默认配置参数，无需设置）
用于成功率统计的服务操作|AMF N8N12 自动业务控制策略|Nudm_UECM_Registration Request&Nudm_UECM_Deregistration Request&Nudm_UECM_Update Request&Nudm_SDM_Get_Nssai_Data Request&Nudm_SDM_Get_Am_Data Request&Nudm_SDM_Get_Smf_Select_Data Request&Nudm_SDM_Get_Sms_Data Request&Nudm_SDM_Get_Ue_Ctx_In_Smf_Data Request&Nudm_SDM_Get_Ue_Ctx_In_Smsf_Data Request&Nudm_SDM_Get_Lcs_Mo_Data Request&Nudm_SDM_Get_Multiple_Data Request&Nudm_SDM_Subscribe Request&Nudm_SDM_UnSubscribe Request&Nudm_SDM_Ack_Info Request&Nausf_UEAuthentication_Authenticate Request&Nausf_UEAuthentication_Authenticate Confirm&Nausf_UEAuthentication_EapSessio（默认配置参数，无需设置）
被排除的错误码|AMF N8N12 自动业务控制策略|0（默认配置参数，无需设置）
使用自动门限配置|AMF N8N12 自动业务控制策略|人工（默认配置参数，无需设置）
配置步骤 :步骤|说明|操作
---|---|---
1|设置AMF自动业务控制基本参数|SET AMF AUTOCTL BASIC PARA:AUTOLEARNFG="OPEN"
2|设置AMF N8N12 自动业务控制策略|SET AMF N8N12 AUTO CNGCTL:FLG="YES"
调整特性 :本特性不涉及调整特性。 
测试用例 :本功能不适合现场测试。 
常见问题处理 :无。 
# 缩略语 
# 缩略语 
AMF :Access and Mobility Management Function接入和移动管理功能
AUSF :Authentication Server Function鉴权服务器功能
DNN :Data Network Name数据网名称
EM :Element Management网元管理
## LC 
Load Control负载控制
## LCI 
Load Control Information负荷控制信息
MME :Mobility Management Entity移动管理实体
NF :Network Function网络功能
NRF :NF Repository Function网络功能仓储
NSSF :Network Slice Selection Function网络切片选择功能
## OC 
Overload Control过负荷控制
## OCI 
Overload Control Information过载控制信息
PCF :Policy Control Function策略控制功能
PDU :Packet Data Unit分组数据单元
## SBI 
Service Based Interface基于服务的接口
SC :Service Component服务组件
SMF :Session Management Function会话管理功能
SUPI :Subscriber Permanent Identifier用户永久标识
UDM :Unified Data Management统一数据管理
UDSF :Unstructured Data Storage Function非结构化数据存储功能
UE :User Equipment用户设备
# ZUF-79-18 增强功能 
## ZUF-79-18-001 双连接 
特性描述 :特性描述 :术语 :术语|含义
---|---
EN-DC|EN-DC是指E-UTRA-NR Dual Connectivity，E-UTRAN和NR的双连接。其中eNB为主基站。gNB为辅助基站（EN-DC下的gNB又称En-gNB/en-gNB）。
NGEN-DC|NGEN-DC是指NG-RAN E-UTRA-NR Dual Connectivity，NG-RAN E-UTRA和NR的双连接。其中ng-eNB为主基站，gNB为辅助基站。
NE-DC|NE-DC是指NR-E-UTRA Dual Connectivity，NR和E-UTRA的双连接。其中gNB为主基站，ng-eNB是辅助基站。
MR-DC|MR-DC是指Multi-RAT Dual Connectivity，多RAT双连接。包括EN-DC、NGEN-DC以及NE-DC三种双连接技术。
en-gNB|en-gNB是EN-DC中的辅助基站，向UE提供NR用户面和控制面协议终结，也称为En-gNB。
ng-eNB|ng-eNB是4G无线接入升级后的基站节点，面向UE提供E-UTRA用户面和控制面的节点，通过NG接口连接到5GC。
Master Node|Master Node（简称MN）是指双连接中的主基站。在EN-DC中由eNodeB充当，在NGEN-DC中由ng-eNB充当，在NE-DC中由gNB充当。
Secondary Node|Secondary Node（简称SN）是指双连接中的辅助基站。在EN-DC中由en-gNB充当，在NGEN-DC指gNB，在NE-DC中由ng-eNB充当。
描述 :定义 :双连接是指用户终端可以同时连接主基站和辅助基站，其中只有主基站用于实现控制平面的功能，数据报文可以选择由主基站传输或者辅助基站传输，或者二者同时传输。 
背景知识 :随着智能终端的日益丰富，移动互联网迅猛发展，无线网络的数据流量和信令数量对网络的冲击前所未有，使得“站点”的部署和容量成为无线网络未来发展的关键要素。 
近年来，主基站的密度触碰到无法超越的极限，在很多热点价值区域，经过多年的建设，主基站建设密度已经非常大。但由于城市环境复杂、业务量大的特点，网络仍面临容量压力和深度覆盖盲区。同时受到邻区干扰机制所限，继续提升主基站密度，并不是解决问题的有效办法。 
为了应对未来数据流量陡增、满足容量增长需求，在主基站网络层中，运营商通过布放大量低功率的辅助基站，来满足热点地区对容量的需求。一般来说，主基站覆盖较大区域，解决移动通信连续性的问题，辅助基站设备所覆盖区域，吸收热点地区的数据量。 
基于上述情况，目前3GPP中定义了EN-DC、NGEN-DC以及NE-DC三种双连接技术，可以通过双连接技术解决方案，核心网不需要感知到辅助基站的存在，从而减少网络的部署和维护。 
双连接根据接入的网络不同做如下分类。 
和EPC网络的双连接（MR-DC with the EPC），UE通过eNodeB接入EPC网络，主要指EN-DC双连接，示意图如图1所示。图1  MR-DC with the EPC图中MN指eNodeB，SN指en-gNB。 
和5GC网络的双连接（MR-DC with the 5GC），UE可能通过ng-eNB或者gNB接入5GC网络，主要指NGEN-DC双连接或者NE-DC双连接。示意图如图2所示。图2  MR-DC with the 5GCMR-DC with the 5GC中主基站和辅助基站的关系参见表1。表1  双连接场景MR-DC with the 5GC双连接场景Master Node(MN)Secondary Node(SN)NGEN-DCng-eNBgNBNE-DCgNBng-eNB 
简单说，eNodeB即为纯4G的无线接入节点，gNB为纯5G接入节点，ng-eNB为4G的无线接入升级后的节点，支持N1、N2接口接入5GC网络，en-gNB为5G的无线接入可以和4G的eNB连接支持接入EPC。 
 说明： 
本特性仅涉及MR-DC with the 5GC的双连接，即NGEN-DC和NE-DC。 
应用场景 :双连接主要适用于以下场景： 
热点覆盖在大型场所，包括大规模的剧院、影城、展览馆、体育馆、机场等，其场地开阔、容纳人数众多，当开展活动时，话务模型密度高、话务量大，此时仅依靠覆盖在室外的主基站难以解决无线资源的稀缺。此时通过临时放置辅助基站，通过IP网连接到5GC，
从而扩大热点区域的流量。 
盲点覆盖在主基站无法覆盖的地方，比如写字楼与宾馆酒店，因为写字楼与宾馆酒店一般位于大型、高层建筑内，高层楼宇在底部区域易出现移动信号覆盖弱甚至盲区，此时通过放置微基站来扩大网络的覆盖范围。 
降低成本辅助基站的成本远远低于主基站，使用辅助基站不但提高了网络的吞吐量和覆盖范围，同时也大大节约了建设成本。 
客户收益 :受益方|受益描述
---|---
运营商|增强网络覆盖，降低成本投入。提高热点区域的容量。提高终端的吞吐量。
终端用户|提高用户的网络速度以及覆盖范围，从而提高用户的感受。
实现原理 :系统架构 :MR-DC with 5GC的控制面和用户面与核心网的接口示意图如下图所示。 
图3  MR-DC with 5GC接口示意图

图上的接口说明如下： 
双连接的控制面仅由主基站（MN）与AMF相连接，控制面接口即当前的N2接口。 
双连接的用户面分为主基站（MN）和辅助基站（SN），均为N3标准接口。 
主基站和辅助基站之间通过Xn-C和Xn-U接口交互控制面和用户面的信息。 说明：Xn-C和Xn-U接口为无线接口，不在本特性介绍的范围内。 
用户的会话数据走向说明如下： 
同一个用户的不同会话可以被分担到主基站和辅助基站上。 
同一个会话的不同QoS Flow也可以被分担到主基站和辅助基站上，对于核心网侧看到的就是针对不同QoS Flow存在不同的隧道端点。 
涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|为UE会话创建根据相关信息选择需要接入的SMF，为SMF与UE、(R)AN之间的消息传递提供Transfer服务。
SMF|NF|根据RAN侧的决定对应的分担N3隧道上的QoS Flow。
UPF|NF|在分配给MN和SN的Tunnel上传输QoS Flow。
网元|UE|3GPP终端，支持5G功能。
(R)AN|网元|决定多个QoS Flow如何在MN和SN上分配。
业务流程 :双连接时增加辅助基站的业务流程如[图4]所示。
图4  Secondary Node Addition流程图

流程说明如下。 
主基站（MN）发送SN Addition Request消息请求目标辅助基站（SN）为一个或多个PDU会话/QoS Flow分配无线资源。
SN提供新SCG无线资源配置给MN，发送SN Addition Request Acknowledge消息给MN，其中该消息包含SN RRC configuration消息。
如果是MN终结的承载，可能在第2步之后发生用户面数据传输。 
如果是SN终结的承载，可能在第2步之后发生数据转发和SN Status Transfer。 
MN发送RRC Connection Reconfiguration消息给UE，其中包含没有修改的SN RRC configuration消息。
UE使用新的配置，向MN返回RRC Connection Reconfiguration Complete消息，其中包括需要发给SN的SN RRC configuration complete消息。
MN通过SN Reconfiguration Complete消息通知SN UE成功完成了重配置流程，如果从UE中接收到了SN RRC Configuration complete消息，MN也会在消息中携带给SN。
如果配置承载需要SCG无线资源，UE向SN执行同步。UE发送MN RRC reconfiguration complete消息和对SCG执行Random Access流程的顺序是不确定的。成功完成了RRC Connection Reconfiguration流程不需要对SCG执行Random Access流程。
对于SN使用RLC接入管理终结的承载，MN发送SN Status Transfer消息。
对于SN使用RLC接入管理终结的承载，依赖各自QoS Flow的承载特征，MN由于MR-DC(数据转发)激活了，可能采取措施减少业务中断。
9-12步，对于SN终结的承载，通过PDU Session Path Update流程执行5GC的用户面路径更新。
NF实现 :给SMF提供N1N2MessageTransfer服务操作，透传SMF与RAN间资源建立、修改、删除 请求/响应消息。 
根据MN的指示完成会话修改。 
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
系统影响 :该特性对系统无影响。 
应用限制 :该特性无应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS23.501 System Architecture for the 5G System|5.11 Support for Dual Connectivity, Multi-Connectivity
3GPP|TS37.340 Evolved Universal Terrestrial Radio Access (E-UTRA) and NR；Multi-connectivity|4 Multi-Radio Dual Connectivity
特性能力 :该特性不涉及规格指标。 
版本要求及变更记录 :序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 :License要求 :该特性是基本特性，无需License支持。 
对其他网元的要求 :SMF|UPF
---|---
√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :配置命令 :本特性暂时不涉及配置命令的变化。 
定时器 :本特性暂时不涉及定时器的变化。 
性能统计 :本特性暂时不涉及计数器的变化。 
告警和通知 :本特性暂时不涉及告警和通知的变化。 
话单与计费 :本特性暂时不涉及话单与计费的变化。 
特性配置 :该功能属于基本功能，无需特别配置，只要完成初始配置，即可实现业务请求流程。 
## ZUF-79-18-002 网络共享 
特性描述 :特性描述 :描述 :定义 :网络共享是指不同的运营商进行核心网共享或无线网络共享，主要是多个运营商共同出资建设共享的网络，这是为分担网络建设成本、降低风险而采取的一种建网模式。 
5G MOCN是指无线接入网络（无线接入网络指NG-RAN）共享、核心网不共享的一种网络共享方式，无线接入网络指NG-RAN，即多个运营商共同出资建设共享的无线接入网络，分担网络建设成本，降低网络建设风险，提高建网速度。
背景知识 :网络共享可以帮助运营商消减投资、拓展网络覆盖范围，同时可以帮助新运营商或中小运营商实现虚拟网络运营，从而快速进入电信领域，实现低成本建网和网络运营。 
3GPP协议对网络共享给出了两种网络架构： 
MOCN架构：仅无线接入网络共享，核心网不共享。 
GWCN架构：除了无线接入网络共享，核心网也在运营商间共享。 
目前普遍采用的是MOCN架构。 
5G网络共享，3GPP协议给出的是5G MOCN架构，即多个核心网共享一个无线接入网络，且共享频率资源。5G MOCN组网方式如下图所示。 
图1   5G MOCN网络共享模式

应用场景 :5G MOCN应用场景如下图所示，运营商A和运营商B共享无线接入网络NG-RAN，运营商A拥有自己的核心网A，运营商B拥有自己的核心网B。 
图2  无线接入网络共享

客户收益 :受益方|受益描述
---|---
运营商|通过网络共享功能，运营商可以获得更加灵活的网络建设方式，包括和其他运营商分担网络建设成本，降低网络建设风险，提高建网速度等。
移动用户|此特性对终端用户不可见。
实现原理 :系统架构 :5G MOCN组网架构如[图3]所示，其中AMF A属于运营商A，AMF B属于运营商B，共享无线接入网。
图3  5G MOCN组网架构

涉及的NF/网元 :NF/网元名称|NF/网元作用
---|---
UE|负责携带Selected PLMN ID。
NG-RAN|通过广播系统信息向UE广播某跟踪区中可用的网络信息，根据用户选择的PLMN路由到正确的AMF，根据移动限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。
AMF|负责在注册、业务请求、局内N2切换、局间N2切换以及EPS和5GS互操作业务流程中，传递UE选择的PLMN标志和支持移动限制列表。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
本NF/网元实现 :AMF在注册、业务请求、局内N2切换、局间N2切换以及EPS和5GS互操作业务流程中，传递UE选择的PLMN标志和支持移动限制列表。 
业务流程 :AMF在如下业务流程中传递选择的PLMN标识和支持移动限制列表： 
初始注册 
移动性注册 
业务请求 
局内N2切换 
局间N2切换 
基于N26接口的5GS到EPS切换 
移动限制列表，用于无线接入网络共享的MOCN，但不仅仅用于MOCN功能，非MOCN的普通切换也使用移动限制列表，控制UE后续移动时的漫游限制、区域限制和接入限制。因此，AMF支持移动限制列表，不受License“AMF支持网络共享功能”及系统开关“AMF支持MOCN功能”的控制。移动限制列表，包含如下参数： 
参数|描述
---|---
Serving PLMN|服务PLMN。NG-RAN携带的Selected PLMN ID。
Equivalent PLMNs|对等PLMN。AMF可以为用户配置对等PLMN，也可全局配置对等PLMN，AMF先根据用户的SUPI获取配置的EPLMN，如果没有获得则获取全局配置的默认EPLMN。
RAT Restrictions|RAT限制。AMF基于UDM签约信息，携带Serving PLMN下限制的RAT类型，可以是EUTRAN、NR等类型。
Forbidden Area Information|禁止区域信息。AMF基于UDM签约信息，携带Serving PLMN下禁止的TAC列表。
Service Area Information|服务区域信息。AMF基于UDM签约信息以及PCF策略，携带Serving PLMN下允许的服务区域和不允许的服务区域。
初始注册
初始注册流程如[图4]所示。
图4  初始注册流程

流程说明如下： 
UE获取NG-RAN广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。UE发起初始注册，选择到可以接入的PLMN后，发送Registration Request消息给网络，并将Selected PLMN ID信息携带给NG-RAN。 
NG-RAN根据UE指示的Selected PLMN ID选择AMF，发送Intial UE给选择的AMF，其中封装了Registration Request消息。 
AMF在下发Registration Accept消息之前的处理和普通的注册流程一致。 
AMF发送Downlink NAS Transport消息给NG-RAN，其中封装了Registration Accept消息。如果“AMF支持下发切换限制列表”开关打开，则Downlink NAS Transport消息中携带Mobility Restriction List。Mobility Restriction List中携带Equivalent PLMNs；Selected PLMN ID被包含在Mobility Restriction List中的Serving PLMN中。 
后续处理和普通的注册流程一致。NG-RAN根据移动限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
移动性注册
移动性注册流程如[图5]所示。
图5  移动性注册流程

流程说明如下： 
UE获取NG-RAN广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。UE在空闲态判断需要发起移动性注册流程，比如UE进入新的TA且该TA不在用户当前的TA List中，选择到可以接入的PLMN后，发送Registration Request消息给网络，并将Selected PLMN ID信息携带给NG-RAN。 
NG-RAN根据UE指示的Selected PLMN ID选择AMF，发送Intial UE消息给AMF，其中封装了Registration Request消息。 
AMF在下发Registration Accept消息之前的处理和普通的注册流程一致。 
AMF发送Downlink NAS Transport消息给NG-RAN，其中封装了Registration Accept消息。如果“AMF支持下发切换限制列表”开关打开，则Downlink NAS Transport消息中携带Mobility Restriction List。Mobility Restriction List中携带Equivalent PLMNs；Selected PLMN ID被包含在Mobility Restriction List中的Serving PLMN中。 
后续处理和普通的注册流程一致。NG-RAN根据移动限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
业务请求
业务请求流程如[图6]所示。
图6  业务请求流程

流程说明如下： 
UE获取NG-RAN广播的所有的PLMN ID列表，将这些作为候选列表执行网络选择。UE在空闲态判断需要发起发起业务请求，比如有上行数据需要发送，选择到可以接入的PLMN后，发送Registration Request消息给网络，并将Selected PLMN ID信息携带给NG-RAN。 
NG-RAN根据UE指示的Selected PLMN ID选择AMF，发送Intial UE给选择的AMF，其中封装了Service Request消息。 
AMF在下发Service Accept消息之前的处理和普通的业务流程一致。 
AMF发送Intial Context Setup Request消息给NG-RAN，其中封装了Service Accept消息。如果“AMF支持下发切换限制列表”开关打开，则Intial Context Setup Request消息中携带Mobility Restriction List。Mobility Restriction List中携带Equivalent PLMNs；Selected PLMN ID被包含在Mobility Restriction List中的Serving PLMN中。 
后续处理和普通的业务流程一致。NG-RAN根据移动限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
局内N2切换
局内N2切换流程如[图7]所示。
图7  局内N2切换流程

流程说明如下： 
UE已经注册并且处于连接态。源NG-RAN根据UE的测量报告，判断需要发起切换流程，发送Handover Required消息给AMF，请求消息中的参数Target ID中携带了Selected PLMN ID，同时携带了目标NG-RAN的ID。 
AMF在下发Handover Request消息之前的处理和普通的切换流程一致。 
AMF发送Handover Request消息给目标NG-RAN，如果“AMF支持下发切换限制列表”开关打开，则Handover Request消息中携带Mobility Restriction List。Mobility Restriction List中携带Equivalent PLMNs；Selected PLMN ID被包含在Mobility Restriction List中的Serving PLMN中。 
后续处理和普通的切换流程一致。NG-RAN根据移动限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
局间N2切换
局间N2切换流程如[图8]所示。
图8  局间N2切换流程

流程说明如下： 
UE已经注册并且处于连接态。源NG-RAN根据UE的测量报告，判断需要发起切换流程，发送Handover Required消息给AMF，请求消息中的参数Target ID中携带了Selected PLMN ID，同时携带了目标NG-RAN的ID。 
AMF判断目标NG-RAN不是本局AMF管理的，按照AMF选择功能选择目标AMF，发送Namf_Communication_CreateUEContext Request消息给目标AMF，消息中通过参数targetId携带源NG-RAN带上来的Selected PLMN ID。 
目标AMF按照普通的切换流程进行切换。 
目标AMF发送Handover Request消息给目标NG-RAN。如果“AMF支持下发切换限制列表”开关打开，则Handover Request消息中携带Mobility Restriction List。Mobility Restriction List中携带Equivalent PLMNs；Selected PLMN ID被包含在Mobility Restriction List中的Serving PLMN中。 
后续处理和普通的切换流程一致。目标NG-RAN根据移动限制列表控制UE后续移动时的漫游限制、区域限制和接入限制。 
基于N26接口的5GS到EPS切换
基于N26接口的5GS到EPS切换流程如图所示。 
图9  基于N26接口的5GS到EPS切换

流程说明如下： 

UE已经在5GS网络注册并且处于连接态。NG-RAN根据UE的测量报告，判断需要切换到E-UTRAN，发送Handover Required消息给AMF，请求消息中的参数Target ID中携带了Selected PLMN ID，同时携带了目标E-UTRAN的ID。 

AMF根据消息中的Handover Type以及Target ID中的TAI查询到MME地址，发送Forward Relocation Request消息给MME。若License“AMF支持网络共享功能”为支持，且“MME支持MOCN功能”开关打开，则Forward Relocation Request消息中携带NG-RAN带上来的Selected PLMN ID；开关关闭，则不携带Selected PLMN ID。 
AMF按照系统原有处理进行切换流程。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501|System Architecture for the 5G System
3GPP TS 23.251|Network Sharing; Architecture and functional description
3GPP TS 23.502|Procedures for the 5G System
3GPP TS 24.501|Non-Access-Stratum (NAS) protocol for 5G System (5GS)
3GPP TS 29.518|5G System; Access and Mobility Management Services
3GPP TS 38.413|NG-RAN; NG Application Protocol (NGAP)
特性能力 :名称|指标
---|---
EPLMN模板配置|200（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 :该特性需要开启License，对应的License项目为“AMF支持网络共享功能”，此项目显示为“支持”，表示ZXUN-UMAC支持MOCN功能。
对其他网元的要求 :UE|NR
---|---
√|√
 说明： 
表中“√”表示本特性对网元有要求，“-”表示本特性对网元无要求。 
工程规划要求 :MOCN组网要求支持网络共享的NG-RAN与各AMF互通。 
O&M相关 :命令 :配置项表3  新增配置项配置项命令AMF支持MOCN配置SET AMFSUPPORTMOCNSHOW AMFSUPPORTMOCN 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置支持MOCN功能实现网络共享功能。 
配置前提 :系统正常运行。 
配置过程 :在AMF节点下，执行[SET AMFSUPPORTMOCN]命令，设置支持MOCN。
配置实例 :场景说明 :设置AMF支持MOCN功能。 
配置步骤 :设置AMF支持MOCN功能，命令如下： 
[SET AMFSUPPORTMOCN]:AMFSUPPORTMOCN="AMFSUPTMOCN"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|AMF支持MOCN功能
---|---
测试目的|设置AMF支持MOCN功能。
预置条件|AMF系统正常运行。
测试过程|在AMF节点下，执行SET AMFSUPPORTMOCN:AMFSUPPORTMOCN="AMFSUPTMOCN"命令。
通过准则|通过执行SHOW AMFSUPPORTMOCN命令，显示支持MOCN。
测试结果|–
常见问题处理 :无 
## ZUF-79-18-004 NAS原因值映射 
特性描述 :特性描述 :描述 :定义 :3GPP TS 29.524协议支持SBI接口原因值到NAS原因值映射，便于用户根据实际需要灵活配置SBI接口失败原因值到N1接口NAS失败原因值的映射关系。 
背景知识 :3GPP TS 29.524协议规定的各SBI接口原因值与NAS原因值存在一对多的映射关系，不同用户可能倾向不同的映射关系，需要系统支持用户根据实际需要配置SBI接口失败原因值到NAS失败原因值的映射关系。 
运营商可以根据现网实际情况，灵活调整配置，通过SBI接口原因值到NAS原因值的映射，控制UE进行合理的操作。 
应用场景 :场景一 :AMF在注册和业务请求等过程中，收到AUSF、UDM、NSSF、SMF等服务的失败响应，根据配置进行SBI接口失败原因值（HTTP状态码和应用层错误码）到NAS原因值映射。 
场景二 :AMF进行AUSF、UDM、SMF等服务发现时，如果发现失败，根据配置进行SBI接口失败原因值到NAS原因值映射。 
场景三 :
AMF对AUSF、UDM、NSSF、SMF等SBI接口的具体失败场景，提供默认的NAS原因值映射。 
客户收益 :受益方|受益描述
---|---
运营商|支持SBI接口原因到NAS原因的映射，向UE下发合理的NAS原因。运营商也可以根据现网实际情况，调整配置，以便灵活调整控制UE的行为。
移动用户|在网络失败情况下，移动用户根据映射后的NAS原因进行合理的后续行为，保障终端的接续，提高用户满意度。
实现原理 :系统架构 :系统网络架构如[图1]所示。
图1  5G系统网络架构

###### 涉及的NF 
NF/网元|说明
---|---
AMF|注册流程主处理NF，与UE/RAN/UDM/UDR/PCF/SMF/UPF协作完成注册过程。AMF和各SBI接口服务交互失败，触发SBI接口原因值到NAS原因值的映射。
AUSF|鉴权服务处理NF，注册过程中与UE/AMF/UDM/UDR协作完成用户的鉴权过程。
UDM|用户签约信息处理NF，注册过程中与UDR配合向AUSF/AMF等提供用户签约数据。
EIR|设备标识检查NF，用于检查终端设备标识PEI是否合法。
PCF|用户策略控制NF，注册过程中与UDR配合向AMF提供用户策略控制数据。
SMF|用户会话管理NF，注册更新过程中，如果存在用户会话上下文，可根据UE指示触发用户面隧道建立。
UPF|用户数据转发NF，注册更新过程中，如果存在用户会话上下文，可根据SMF指示建立用户面隧道。
NSSF|网络切片选择NF，注册过程中提供切片选择功能。
UE|支持5G接入的终端，注册等业务流程在网络失败后，根据映射后的NAS原因值进行后续的行为。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N12|ZUF-79-19-005 N12
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15
N22|ZUF-79-19-008 N22
###### 本NF实现 
与AUSF、UDM、NSSF、SMF等NF交互，在与SBI接口交互过程中发生失败，根据运营商配置进行SBI接口失败原因值到NAS原因值的映射。 
与UE交互，在网络失败的情况下向UE下发正确的映射NAS原因值。 
业务流程 :AUSF/UDM/NSSF SBI接口原因值映射NAS原因值
图2  AUSF/UDM/NSSF SBI接口原因值映射NAS原因值

流程说明如下： 
UE向AMF发起注册请求/业务请求消息。 
AMF和其他5GC网元（AUSF/UDM/NSSF）交互时，其他5GC网元超时无响应或者返回失败。 
AMF根据其他5GC网元返回的情况，执行SBI接口原因值到NAS原因值的映射查询过程，获取映射的NAS原因值。 
AMF向UE发送注册拒绝/业务拒绝消息，携带映射的NAS原因值。 
通过NRF发现SBI网元失败映射NAS原因
图3  通过NRF发现SBI网元失败映射NAS原因

流程说明如下： 
UE向AMF发起注册请求/业务请求消息。 
AMF和其他5GC网元（如AUSF/UDM/NSSF等）交互时，AMF向NRF发起查询请求，NRF超时无响应或者返回失败。 
AMF根据NRF返回的情况，执行SBI接口原因值到NAS原因值的映射查询过程，获取映射的NAS原因值。 
AMF向UE发送注册拒绝/业务拒绝消息，携带映射的NAS原因值。 
重激活PDU会话SMF失败，SBI接口原因值映射NAS原因值
图4  重激活PDU会话SMF失败，SBI接口原因值映射NAS原因值

流程说明如下： 
UE向AMF发送注册请求/业务请求消息，携带Uplink Data Status，要求激活用户面。 
AMF触发所有PDU会话向SMF发起恢复用户面过程，SMF超时无响应或者返回失败。 
AMF针对每个PDU会话，根据SBI接口原因值到NAS原因值映射查询，获取映射的NAS原因值，向UE发送注册接受/业务接受消息，携带每个PDU激活失败的NAS原因值。 
重激活PDU会话发现SMF失败，SBI接口原因值映射NAS原因值
图5  重激活PDU会话发现SMF失败，SBI接口原因值映射NAS原因值

流程说明如下： 
UE向AMF发送注册请求/业务请求消息，携带Uplink Data Status，要求激活用户面。 
AMF需要发现SMF时，向NRF发起查询请求，NRF超时无响应或者返回失败。 
AMF针对每个PDU会话，根据SBI接口原因值到NAS原因值映射查询，获取映射的NAS原因值，向UE发送注册接受/业务接受消息，携带每个PDU激活失败的NAS原因值。 
UE激活PDU会话SMF发现失败，SBI接口原因值映射NAS原因值
图6  UE激活PDU会话SMF发现失败，SBI接口原因值映射NAS原因值

流程说明如下： 
UE向AMF发起PDU会话激活流程。 
AMF向NRF发起Nnrf_NFDiscovery操作流程，NRF发现SMF失败。 
AMF拒绝UE的PDU会话激活，根据SBI接口原因值到NAS原因值映射查询，获取映射的NAS原因值。 
AMF向UE发送PDU Session Establishment Response消息，携带映射的NAS原因值。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :AMF支持与AUSF、UDM、NSSF、SMF的SBI接口根据最新版本协议定义的具体失败场景进行NAS原因映射，但是在3GPP TS 29.524协议定义的场景之外，系统无法针对具体场景进行NAS原因映射，因此提供默认的NAS原因映射进行通配。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|System Architecture for the 5G System
TS 23.502|3GPP|Procedures for the 5G System
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
TS 29.501|3GPP|5G System; Principles and Guidelines for Services Definition
TS 29.502|3GPP|Session Management Services; Stage 3
TS 29.503|3GPP|Unified Data Management Services; Stage 3
TS 29.507|3GPP|Access and Mobility Policy Control Service; Stage 3
TS 29.509|3GPP|Authentication Server Services; Stage 3
TS 29.510|3GPP|Network function repository services; Stage 3
TS 29.511|3GPP|Equipment Identity Register Services; Stage 3
TS 29.514|3GPP|Policy Authorization Service; Stage 3
TS 29.524|3GPP|5G System; Cause codes mapping between 5GC interfaces
TS 29.531|3GPP|Network Slice Selection Services; Stage 3
IETF|RFC7231|Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content
特性能力 :名称|指标
---|---
Nausf原因值映射配置最大映射个数|512（个）
Nudm原因值映射配置最大映射个数|512（个）
Nnssf原因值映射配置最大映射个数|512（个）
Nsmf原因值映射配置最大映射个数|512（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.22.20|新增NRF原因值映射配置。
01|V7.20.20|首次发布。
License要求 :该特性为协议基本特性，无需License支持。 
###### 对其他NF的要求 
UE|AUSF|UDM|NSSF|EIR|SMF
---|---|---|---|---|---
-|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令基于SUPI号段的Nausf原因值映射配置ADD AUSFCAUSEMAPPINGCFGBYSUPISET AUSFCAUSEMAPPINGCFGBYSUPIDEL AUSFCAUSEMAPPINGCFGBYSUPISHOW AUSFCAUSEMAPPINGCFGBYSUPINausf原因值映射配置ADD AUSFCAUSEMAPPINGCFGSET AUSFCAUSEMAPPINGCFGDEL AUSFCAUSEMAPPINGCFGSHOW AUSFCAUSEMAPPINGCFGNudm原因值映射配置ADD UDMCAUSEMAPPINGCFGSET UDMCAUSEMAPPINGCFGDEL UDMCAUSEMAPPINGCFGSHOW UDMCAUSEMAPPINGCFG基于SUPI号段的Nudm原因值映射配置ADD UDMCAUSEMAPPINGCFGBYSUPISET UDMCAUSEMAPPINGCFGBYSUPIDEL UDMCAUSEMAPPINGCFGBYSUPISHOW UDMCAUSEMAPPINGCFGBYSUPINnssf原因值映射配置ADD NSSFCAUSEMAPPINGCFGSET NSSFCAUSEMAPPINGCFGDEL NSSFCAUSEMAPPINGCFGSHOW NSSFCAUSEMAPPINGCFGNsmf原因值映射配置ADD SMFCAUSEMAPPINGCFGSET SMFCAUSEMAPPINGCFGDEL SMFCAUSEMAPPINGCFGSHOW SMFCAUSEMAPPINGCFGNnrf原因值映射配置ADD NNRFCAUSEMAPPINGCFGBYSUPISET NNRFCAUSEMAPPINGCFGBYSUPIDEL NNRFCAUSEMAPPINGCFGBYSUPISHOW NNRFCAUSEMAPPINGCFGBYSUPIADD NNRFCAUSEMAPPINGCFGSET NNRFCAUSEMAPPINGCFGDEL NNRFCAUSEMAPPINGCFGSHOW NNRFCAUSEMAPPINGCFG 
安全变量无。 
软件参数无。 
动态管理无。 
性能统计 :性能计数器名称
---
C510010041 初始注册失败次数（111.user-协议失败，未指定_用户原因）
C510010042 初始注册失败次数（62-无可用网络切片）
C510010043 初始注册失败次数（27.user-N1模式不允许_用户原因）
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :       AMF和5GC网元AUSF、UDM、NSSF、SMF交互时，可以根据对端返回的HTTP状态码和应用层错误码，映射为5GMM原因，发送给UE，以便引导UE进行合理的后续行为。 
现网不同局点，也可以根据运营商的需求，调整配置，灵活映射5GMM原因发送给UE，以便灵活调整控制UE的行为。 
具体地，AMF识别AUSF、UDM、NSSF和SMF返回的HTTP状态码（HTTP Status Code）和应用层错误码（Applicaton Error Code），通过网管上对应NF的配置，查找到映射的5GMM原因。在流程结束阶段，如注册拒绝\接受、业务请求拒绝\接受、PDU激活拒绝等NAS消息中，将原因值带给UE。 
5GMM原因映射的通用原则
采用HTTP状态码和应用层错误码为唯一关键字来映射5GMM原因，HTTP状态码和应用层错误码均支持通配的能力，可以采用以下方式进行匹配：
HTTP状态码+通配 
通配+应用层错误码 
通配+通配 
HTTP状态码|应用层错误码|5GMM原因值
---|---|---
XXX code|“Application Error String”|XXX – cause
各个SBI接口原因值映射配置，HTTP状态码和应用层错误码为独立设置，每个NF都有独有的HTTP状态码和应用层错误码组合。 
5GMM原因值为3GPP TS 24.501协议列出的全部取值，AMF支持映射到任意5GMM原因的能力。 
现网可以增加、删除、修改原因映射。 
AMF根据各个SBI接口协议和通用SBI接口协议描述的原因场景，及3GPP TS 29524协议的映射推荐，提供合理的默认映射记录。 
SBI接口原因到5GMM原因的映射查询过程
HTTP超时无响应
HTTP status code+Application Error设置为“65533：等待HTTP响应超时/Wait HTTP Response Timeout”+“65534：无关/Not Applicable”进行查询。 
查询到结果→结束 
未查询到结果→步骤2 
使用“65535：通配/Any HTTP status code”+“65535：通配/Any Application Error”进行查询。 
查询到结果→结束 
未查询到结果→步骤3 
返回通用缺省原因“111 – Protocol error, unspecified”。 
有HTTP响应且有Application Error
使用HTTP status code+Application Error进行查询。 
查询到结果→结束 
未查询到结果→步骤2 
使用“65535：通配/Any HTTP status code”+Application Error进行查询。 
查询到结果→结束 
未查询到结果→步骤3 
使用HTTP status code+“65535：通配/Any Application Error”进行查询。 
查询到结果→结束 
未查询到结果→步骤4 
使用“65535：通配/Any HTTP status code”+“65535：通配/Any Application Error”进行查询。 
查询到结果→结束 
未查询到结果→步骤5 
返回通用缺省原因“111 – Protocol error, unspecified”。 
有HTTP响应且无Application Error
使用HTTP status code+“65533：应用层错误码不存在/Application Error Not Exist”进行查询。 
查询到结果→结束 
未查询到结果→步骤2 
使用HTTP status code+“65535：通配/Any Application Error”进行查询。 
查询到结果→结束 
未查询到结果→步骤3 
使用“65535：通配/Any HTTP status code”+“65535：通配/Any Application Error”进行查询。 
查询到结果→结束 
未查询到结果→步骤4 
返回通用缺省原因“111 – Protocol error, unspecified”。 
NF发现失败

AMF和其他5GC网元（如AUSF/UDM/NSSF等）交互时，AMF向NRF发起查询请求，NRF超时无响应或者返回失败。 

AMF根据NRF返回的情况，执行SBI接口原因值到NAS原因值的映射查询过程，获取映射的NAS原因值，具体分为如下几个场景。 
HTTP超时无响应  
有HTTP响应且有Application Error  
有HTTP响应且无Application Error 
配置前提 :无。 
配置过程 :###### Nausf原因值映射配置 
(可选）执行[ADD AUSFCAUSEMAPPINGCFGBYSUPI]命令，新增基于SUPI号段的Nausf原因值映射配置，以便灵活地针对不同SUPI号段提供差异化的AUSF失败-5GMM原因映射。
执行命令[SHOW AUSFCAUSEMAPPINGCFG]，查询默认Nausf原因值映射配置，即SUPI号段无法匹配时的AUSF失败到5GMM原因映射，AMF根据N12接口协议和通用SBI接口协议描述的原因场景，及3GPP TS 29524协议的映射推荐，提供了一些合理的默认映射记录，可通过此命令查询。如默认记录可以满足差异化要求，则无需额外新增默认Nausf原因值映射配置。
(可选）执行[ADD AUSFCAUSEMAPPINGCFG]命令，新增默认的Nausf原因值映射配置，制定个性化的“HTTP状态码+应用层错误码”到“5GMM原因值+计数归类”的映射配置，其中“计数归类”为初始注册因AUSF失败而拒绝时，期望纠正的5GMM原因值。
###### Nudm原因值映射配置 
(可选）执行[ADD UDMCAUSEMAPPINGCFGBYSUPI]命令，新增基于SUPI号段的Nudmf原因值映射配置，以便灵活地针对不同SUPI号段提供差异化的UDM失败-5GMM原因映射。
执行命令[SHOW UDMCAUSEMAPPINGCFG]，查询默认Nudm原因值映射配置，即SUPI号段无法匹配时的UDM失败-5GMM原因映射，AMF根据N8接口协议和通用SBI接口协议描述的原因场景，及3GPP TS 29524协议的映射推荐，提供了一些合理的默认映射记录，可通过此命令查询。如默认记录可以满足差异化要求，则无需额外新增默认Nudm原因值映射配置。
(可选）执行[ADD UDMCAUSEMAPPINGCFG]命令，新增默认的Nudm原因值映射配置，制定个性化的“HTTP状态码+应用层错误码”到“5GMM原因值+计数归类”的映射配置，其中“计数归类”为初始注册因UDM失败而拒绝时，期望纠正的5GMM原因值。
###### Nnssf原因值映射配置 
执行[SHOW NSSFCAUSEMAPPINGCFG]命令，查询默认Nnssf原因值映射配置。AMF根据N22接口协议和通用SBI接口协议描述的原因场景，及3GPP TS 29524协议的映射推荐，提供了一些合理的默认映射记录，可通过此命令查询。如默认记录可以满足差异化要求，则无需额外新增默认Nnssf原因值映射配置。
(可选）执行[ADD NSSFCAUSEMAPPINGCFG]命令，新增默认的Nnssf原因值映射配置，制定个性化的“HTTP状态码+应用层错误码”到“5GMM原因值+计数归类”的映射配置，其中“计数归类”为初始注册因NSSF失败而拒绝时，期望纠正的5GMM原因值。
###### Nnrf原因值映射配置 
(可选）执行[ADD NNRFCAUSEMAPPINGCFGBYSUPI]命令，新增基于SUPI号段的Nnrf原因值映射配置，以便灵活地针对不同SUPI号段提供差异化的发现失败-5GMM原因映射。
执行[SHOW NNRFCAUSEMAPPINGCFG]命令，查询默认Nnrf原因值映射配置，即SUPI号段无法匹配时的发现失败到5GMM原因映射，AMF根据通用SBI接口协议描述的原因场景，及3GPP TS 29524协议的映射推荐，提供了一些合理的默认映射记录，可通过此命令查询。如默认记录可以满足差异化要求，则无需额外新增默认Nnrf原因值映射配置。
(可选）执行[ADD NNRFCAUSEMAPPINGCFG]命令，新增默认的Nnrf原因值映射配置，制定个性化的“HTTP状态码+应用层错误码”到“5GMM原因值+计数归类”的映射配置，其中“计数归类”为初始注册因发现失败而拒绝时，期望纠正的5GMM原因值。
###### Nsmf原因值映射配置 
执行[SHOW SMFCAUSEMAPPINGCFG]命令，查询默认Nsmf原因值映射配置。AMF根据N11接口协议和通用SBI接口协议描述的原因场景，及3GPP TS 29524协议的映射推荐，提供了一些合理的默认映射记录，可通过此命令查询。如默认记录可以满足差异化要求，则无需额外新增默认Nsmf原因值映射配置。
(可选）执行[ADD SMFCAUSEMAPPINGCFG]命令，新增默认的Nsmf原因值映射配置，制定个性化的“HTTP状态码+应用层错误码”到“5GMM原因值”的映射配置。
配置实例 :场景说明 :场景|场景描述|说明
---|---|---
场景1|AUSF失败导致初始注册拒绝的NAS原因映射|用户初始注册，与AUSF交互失败，用户号段在“基于SUPI号段的Nausf原因值映射配置”中有匹配，存在“HTTP响应码+应用层错误码”为AUSF返回错误响应码+应用层错误码的配置记录，注册拒绝携带NAS原因值为此配置记录对应的“5GMM原因值”。
场景2|UDM失败导致初始注册拒绝的NAS原因映射|用户初始注册，向UDM获取签约数据超时，用户号段在“基于SUPI号段的Nudm原因值映射配置”中无匹配，在“Nudm原因值映射配置”中存在“HTTP响应码+应用层错误码”为“等待HTTT响应超时+无关”的配置记录，注册拒绝携带NAS原因值为此配置记录对应的“5GMM原因值”。
场景3|NSSF失败导致初始注册拒绝的NAS原因映射|用户初始注册，向NSSF选择切片失败，失败响应携带HTTP响应码“404 Not Found”及应用层错误码“USER NOT FOUND”。在“Nnssf原因值映射配置”中存在此HTTP响应码+应用层错误码的配置，注册拒绝，携带NAS原因值为此配置记录对应的“5GMM原因值”。
场景4|SMF发现失败导致注册更新重建用户面失败的NAS原因映射|局内注册更新，某个PDU会话更新时收到SMF的失败响应，携带HTTP响应码“404 Not Found”但无应用层错误码，其余PDU更新成功。“404 Not Found” + “应用层错误码不存在”在“Nsmf原因值映射配置”中不存在记录，退化为“404 Not Found” + “通配”查询，依然不存在，再次退化为“通配” + “通配”，在默认配置记录中存在，且对应“5GMM原因“为“不携带5GMM原因”。注册接受中，更新失败的PDU的PDU session reactivation result error cause，并且不携带此失败原因。
场景5|通过NRF发现SBI网元失败映射NAS原因|用户初始注册，发现AUSF失败，用户号段在“基于SUPI号段的Nnrf原因值映射配置”中无匹配，在“Nnrf原因值映射配置”中存在“HTTP响应码+应用层错误码”为NRF返回错误响应码+应用层错误码的配置记录，注册拒绝携带NAS原因值为此配置记录对应的“5GMM原因值”。
数据规划 :配置名称|参数项|取值
---|---|---
基于SUPI号段的Nausf原因值映射配置|SUPI号段|46001|46001
HTTP状态码|基于SUPI号段的Nausf原因值映射配置|403 Forbidden|403 Forbidden
应用层错误码|基于SUPI号段的Nausf原因值映射配置|DATA_NOT_FOUND|DATA_NOT_FOUND
5GMM 原因值|基于SUPI号段的Nausf原因值映射配置|7 - 5GS services not allowed|7 - 5GS services not allowed
计数归类|基于SUPI号段的Nausf原因值映射配置|111|111
基于SUPI号段的Nudm原因值映射配置|SUPI号段|46012|46012
HTTP状态码|基于SUPI号段的Nudm原因值映射配置|等待HTTP响应超时|等待HTTP响应超时
应用层错误码|基于SUPI号段的Nudm原因值映射配置|无关|无关
5GMM 原因值|基于SUPI号段的Nudm原因值映射配置|3 - Illegal UE|3 - Illegal UE
计数归类|基于SUPI号段的Nudm原因值映射配置|27|27
查询Nudm原因值映射配置|HTTP状态码|等待HTTP响应超时|等待HTTP响应超时
应用层错误码|查询Nudm原因值映射配置|无关|无关
Nnssf原因值映射配置|HTTP状态码|404 Not Found|404 Not Found
应用层错误码|Nnssf原因值映射配置|USER_NOT_FOUND|USER_NOT_FOUND
5GMM 原因值|Nnssf原因值映射配置|27 - N1 mode not allowed|27 - N1 mode not allowed
计数归类|Nnssf原因值映射配置|62|62
Nnrf原因值映射配置|SUPI号段|46012|46012
发现NF场景|Nnrf原因值映射配置|发现SMF（PDU会话建立过程）|发现SMF（PDU会话建立过程）
HTTP状态码|Nnrf原因值映射配置|404 Not Found|404 Not Found
应用层错误码|Nnrf原因值映射配置|USER_NOT_FOUND|USER_NOT_FOUND
5GMM 原因值|Nnrf原因值映射配置|27 - N1 mode not allowed|27 - N1 mode not allowed
计数归类|Nnrf原因值映射配置|27|27
配置步骤 :步骤|说明|操作
---|---|---
1|查询Nausf原因值映射配置的默认记录|SHOW AUSFCAUSEMAPPINGCFG
2|增加基于SUPI号段的Nausf原因值映射配置|ADD AUSFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46001",HTTPSTATUSCODE="403 Forbidden",APPLICATIONERROR="DATA_NOT_FOUND",AUSFMMCAUSE="SERVICENOTALLOWED",COUNTER=111
3|查询Nudm原因值映射配置|SHOW UDMCAUSEMAPPINGCFG:HTTPSTATUSCODE="WAITHTTPTIMEOUT",APPLICATIONERROR="APP_NOT_APPLICABLE"
4|增加基于SUPI号段的Nudm原因值映射配置|ADD UDMCAUSEMAPPINGCFGBYSUPI:SUPISEG="46012",HTTPSTATUSCODE="WAITHTTPTIMEOUT",APPLICATIONERROR="APP_NOT_APPLICABLE",UDMMMCAUSE="ILLEGALUE",COUNTER=27
5|除已有默认记录外，增加Nnssf原因值映射配置|ADD NSSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_404",APPLICATIONERROR="USER_NOT_FOUND",NSSFMMCAUSE="N1MODENOTALLOWED",COUNTER=62
6|查询Nsmf原因值映射配置的默认记录|SHOW SMFCAUSEMAPPINGCFG
7|增加基于SUPI号段的Nnrf原因值映射配置|ADD NNRFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46012",DISNFSITUATION="DISCOVER_SMF_PDU",HTTPSTATUSCODE="HTTP_404",APPLICATIONERROR="USER_NOT_FOUND",NRFMMCAUSE="N1MODENOTALLOWED",COUNTER=27
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|Nausf原因值映射配置匹配
---|---
测试目的|基于SUPI号段的Nausf原因值映射配置可以正确进行AUSF失败时的NAS原因值映射
预置条件|完成NAS原因值映射配置。AMF环境运行正常。
测试过程|用户初始注册。与AUSF交互失败。
通过准则|AMF下发注册拒绝。注册拒绝携带NAS原因值为“7: SERVICENOTALLOWED”。
测试结果|–
测试项目|Nudm原因值映射配置匹配
---|---
测试目的|“基于SUPI号段的Nudm原因值映射配置”无号段匹配时，“Nudm原因值映射配置”可以正确进行UDM失败时的NAS原因值映射
预置条件|完成NAS原因值映射配置。AMF环境运行正常。
测试过程|用户初始注册。注册过程中向UDM获取Multi签约数据超时。
通过准则|AMF下发注册拒绝。注册拒绝携带NAS原因值为“3: ILLEGALUE”。
测试结果|–
测试项目|Nnssf原因值映射配置匹配
---|---
测试目的|Nnssf原因值映射配置可以正确进行NSSF失败时的NAS原因值映射
预置条件|完成NAS原因值映射配置。AMF环境运行正常。
测试过程|用户初始注册。注册过程中向NSSF获取切片失败，失败响应携带HTTP响应码“404 Not Found”及应用层错误码“USER NOT FOUND”。
通过准则|AMF下发注册拒绝。注册拒绝携带NAS原因值为“27: N1MODENOTALLOWED”。计数器C510010043、C511000045统计加1。
测试结果|–
测试项目|Nsmf原因值映射配置匹配
---|---
测试目的|Nsmf原因值映射配置可以正确进行SMF失败时的NAS原因值映射
预置条件|完成NAS原因值映射配置。AMF环境运行正常。
测试过程|用户初始注册，建立多个PDU会话。注册更新，注册请求指示重建会话。某个PDU会话更新时收到SMF的失败响应，携带HTTP响应码“404 Not Found”但无应用层错误码，其余PDU会话更新成功。
通过准则|注册接受。注册接受中，更新失败的PDU对应的PDU session reactivation result error cause，不携带5GMM原因。（因为“404 Not Found” + “应用层错误码不存在”在“Nsmf原因值映射配置”中不存在记录，退化为“404 Not Found” + “通配”查询，依然不存在，再次退化为为“通配” + “通配”，在默认配置记录中存在，且对应“5GMM原因”为“不携带5GMM原因”。）
测试结果|–
测试项目|Nnrf原因值映射配置
---|---
测试目的|Nnrf原因值映射配置可以正确进行NRF发现失败时的NAS原因值映射。
预置条件|完成NAS原因值映射配置。AMF环境运行正常。
测试过程|用户初始注册，NRF发现UDM。NRF发现失败，携带HTTP响应码“404 Not Found”+“USER_NOT_FOUND”。
通过准则|AMF下发注册拒绝。注册拒绝携带NAS原因值为“27: N1MODENOTALLOWED”
测试结果|–
常见问题处理 :无。 
## ZUF-79-18-005 第二RAT用量数据上报 
特性描述 :特性描述 :描述 :定义 :第二RAT用量数据上报指RAN把第二RAT用量数据通过控制面信令上报给AMF，AMF把其透传给I-SMF/V-SMF/A-SMF，I-SMF/V-SMF/A-SMF在CDR中区分不同RAT的用量。
背景知识 :SA组网时，无线可以采用双连接方式，如[图1]所示。Secondary Node可以和Master Node是同一RAT类型的Node，也可以是不同RAT类型的Node。
图1  双连接架构图

应用场景 :第二RAT用量数据上报是SA重要功能，典型场景如下： 
本地用户SMF上报话单中区分第二RAT用量数据。 
漫出用户SMF上报话单中区分第二RAT用量数据。 
漫入用户V-SMF上报话单中区分第二RAT用量数据。 
客户收益 :受益方|受益描述
---|---
运营商|提高收益：收集第二RAT用量，用于计费，便于进行更多的业务创新。
移动用户|此特性对终端用户不可见。
实现原理 :系统架构 :SA组网时，无线可以采用双连接方式，AMF支持第二RAT用量数据上报的系统架构如[图2]所示。Secondary Node可以和Master Node是同一RAT类型的Node，也可以是不同RAT类型的Node。
图2  AMF支持第二RAT用量数据上报的系统架构

涉及的网元 :网元名称|网元作用
---|---
RAN|为UE的5G接入提供无线资源。本特性中，RAN支持上报Secondary RAT usage data。
AMF|AMF透传RAN上报的Secondary RAT usage data信息给SMF。
SMF|SMF把RAN上报的Secondary RAT usage data信息放到话单中。
协议栈 :接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
本网元实现 :AMF透传RAN上报的Secondary RAT usage data信息给SMF。为了透传RAN上报的Secondary RAT usage data信息给SMF，AMF实现以下功能： 
AMF对注销流程的消息处理时序做了调整。 
AMF在Nsmf_PDUSession_CreateSMContext Request、Nsmf_PDUSession_UpdateSMContext Request、Nsmf_PDUSession_ReleaseSMContext Request消息中，把RAN上报的Secondary RAT Usage信息，投递给SMF。 
如果流程需要发送Nsmf_PDUSession_CreateSMContext Request、Nsmf_PDUSession_UpdateSMContext Request、Nsmf_PDUSession_ReleaseSMContext Request消息，则在这些消息中携带Secondary RAT Usage信息。如果流程无这些消息，则通过独立的Nsmf_PDUSession_UpdateSMContext Request消息，把RAN上报的Secondary RAT Usage信息投递给SMF。 
对无线新增的Secondary RAT Data Usage Report，AMF可以缓存或立刻通知SMF。 
业务流程 :UE发起的注销流程
UE发起的注销的正常流程如[图3]所示。
图3  UE发起的注销流程

具体流程说明参见去注册
。
如果AMF支持Secondary RAT用量上报，则需先向通知UE和无线释放资源，再执行通知SMF动作。即先执行第7步到第8步，再执行第2步到第6步。 
网络侧发起的注销流程
网络侧发起的注销的正常流程如[图4]所示。
图4  网络侧发起的注销流程

具体流程说明参见去注册
。
如果AMF支持Secondary RAT用量上报，则应该也需先向通知UE和无线释放资源，再执行通知SMF动作。即给SMF发送消息之前，需要等待UE的去注册接受消息，再通知NR释放N2连接。即先执行第6步到第7步，再执行第4步到第5步。 
AN释放
RAN在N2 UE Context Release Complete消息中携带Secondary RAT用量信息。AN释放UE上下文的流程如[图5]所示。
图5  AN释放流程

具体流程说明参见AN释放UE上下文
。
AMF收到N2 UE Context Release Complete消息，如果消息中携带Secondary RAT用量，则通过Nsmf_PDUSession_UpdateSMContext通知SMF。 
Xn口切换
NR在开始切换执行阶段前，会给AMF上报Secondary RAT Usage Reporting信息，携带Handover指示，AMF缓存Secondary RAT Usage Reporting信息，在后续给SMF的消息中顺带Secondary RAT Usage Reporting信息。 
基于Xn口的切换，无I-UPF变化。基于Xn口的切换，无I-UPF变化的流程如图6所示。图6  基于Xn口的切换，无I-UPF变化的流程图流程说明如下：NR完成切换准备阶段，准备切换执行阶段时，如果有Secondary RAT Usage Reporting信息需要上报，则给AMF发送RAN Usage data report消息，消息中携带Secondary RAT Usage Reporting和handover flag。Target NR发送Path Switch Request消息给AMF，携带Source AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU Session To Be Switched in Downlink List等信息。AMF收到Path Switch Request消息后，针对PDU Session To Be Switched in Downlink List的每一个会话，发送Nsmf_PDUSession_UpdateSMContext Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。如果本地有Secondary RAT Usage Reporting信息，也携带N2 SM Information from source NG-RAN (Secondary RAT usage data)信息给SMF。SMF根据ueLocation判断UPF可以继续服务于UE，发送PFCP Session Modification Request消息给UPF，携带Target NR N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF，携带UPFN3隧道信息。SMF收到UPF响应后，回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF，携带UPFN3隧道信息。AMF收到SMF响应后，回复Path Switch Acknowledge消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU Session To Be Switched in Uplink List等信息。 
基于Xn口的切换，重选I-UPF。基于Xn口的切换，重选I-UPF的流程如图7所示，当切换前PDU会话的用户面路径中无I-UPF，此时Source I-UPF就是UPF（PSA）。图7  基于Xn口的切换，重选I-UPF的流程图流程说明如下：NR完成切换准备阶段，准备切换执行阶段时，如果有Secondary RAT Usage Reporting信息需要上报，则给AMF发送RAN Usage data report消息，消息中携带Secondary RAT Usage Reporting和handover flag。Target NR发送Path Switch Request消息给AMF，携带Source AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU Session To Be Switched in Downlink List等信息。AMF收到Path Switch Request后，针对PDU Session To Be Switched in Downlink List的每一个会话，发送Nsmf_PDUSession_UpdateSMContext Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。如果本地有Secondary RAT Usage Reporting信息，也携带N2 SM Information from source NG-RAN (Secondary RAT usage data)信息给SMF。SMF收到Nsmf_PDUSession_UpdateSMContext Request后，根据ueLocation检测到用户位置发生变化，调用UPF选择功能重新选择I-UPF，最终选择的I-UPF与原有的I-UPF不同。SMF发送PFCP Session Establishment Request消息给新选择的Target I-UPF，携带Target NR N3隧道信息以及UPF（PSA） N9隧道信息。Target I-UPF回复PFCP Session Establishment Response消息给SMF，携带Target I-UPF N3隧道信息以及N9隧道信息。SMF发送PFCP Session Modification Request消息给UPF（PSA），携带Target I-UPF N9隧道信息。UPF（PSA）回复PFCP Session Modification Response消息给SMF，携带UPF（PSA） N9隧道信息。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF，携带Target I-UPF N3隧道信息，并启动资源保护定时器。AMF收到SMF响应后，回复Path Switch Acknowledge消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU Session To Be Switched in Uplink List等信息。如果步骤7中启动的定时器超时后，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source I-UPF释放用户上下文。Source I-UPF释放用户上下文，回复PFCP Session Release Response给SMF。 
基于Xn口的切换，移除I-UPF。基于Xn口的切换，移出I-UPF的流程如图8所示。图8  基于Xn口的切换，移出I-UPFF的流程图流程说明如下：NR完成切换准备阶段，准备切换执行阶段时，如果有Secondary RAT Usage Reporting信息需要上报，则给AMF发送RAN Usage data report消息，消息中携带Secondary RAT Usage Reporting和handover flag。Target NR发送Path Switch Request消息给AMF，携带Source AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU Session To Be Switched in Downlink List等信息。AMF收到Path Switch Request消息后，针对PDU Session To Be Switched in Downlink List每一个会话，发送Nsmf_PDUSession_UpdateSMContext Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。如果本地有Secondary RAT Usage Reporting信息，也携带N2 SM Information from source NG-RAN (Secondary RAT usage data)信息给SMF。SMF收到Nsmf_PDUSession_UpdateSMContext Request消息后，根据ueLocation检测到用户位置发生改变，调用UPF选择功能重新选择I-UPF，最终选择的I-UPF为UPF（PSA）。SMF发送PFCP Session Modification Request消息给UPF（PSA），携带Target NR的N3隧道信息。启动定时器，该定时器超时后通知Source I-UPF释放资源。UPF（PSA）回复PFCP Session Modification Response消息给SMF，携带UPF（PSA） N3隧道信息。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给AMF，携带UPF（PSA） N3隧道信息。AMF收到SMF响应后，回复Path Switch Acknowledge给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU Session To Be Switched in Uplink List等信息。步骤3启动的定时器超时后，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source I-UPF释放用户上下文。Source I-UPF释放用户上下文，回复PFCP Session Release Response给SMF。 
N2口切换
源侧RAN在给UE发送切换命令前，会给AMF上报Secondary RAT Usage Reporting信息，携带Handover指示，AMF缓存Secondary RAT Usage Reporting信息，在后续给SMF的消息中顺带Secondary RAT Usage Reporting信息。 
基于N2接口的切换，无I-UPF变化。基于N2接口的切换，无I-UPF变化的流程如图9所示。图9  基于N2接口的切换，无I-UPF变化 说明：若用户面路径中不存在I-UPF，则UPF指UPF（PSA）。若用户面路径中存在I-UPF，则UPF指I-UPF。若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。流程说明如下：Source NR检测到用户需要切换到Target NR，发送Handover Required消息给Source AMF，携带Handover Type、Target ID、Source To Target Transparent Container等信息。Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target AMF。若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext Request消息给Target AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source To Target Transparent Container等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带用户位置、Target AMF ID、切换准备状态等信息。SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF仍旧为切换前的UPF。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF，携带PDU会话ID、SM N2 Information。Target AMF下发Handover Request消息给Target NR，携带Handover Type、SM N2 Information List、UE AMBR、Security Context、UE Security Capabilities。Target NR回复Handover Request Acknowledge消息给Target AMF，携带PDU Session Admitted List、Target To Source Transparent Container等信息，其中PDU Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、SM N2 Information。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。Target AMF发送Namf_Communication_CreateUEContext Response消息给Source AMF，携带Target To Source Transparent Container。Source AMF发送Handover Command消息给Source NR，携带Target To Source Transparent Container；Source NR收到Handover Command消息后，通过空口通知UE向目标小区切换。UE切换到Target NR后，Target NR发送Handover Notify消息给Target AMF，通知Target AMF用户已经成功切换到目标小区。Target AMF收到Handover Notify消息后，发送Namf_Communication_N2InfoNotify消息给Source AMF，通知Source AMF用户已经切换成功。Source AMF启动定时器，在定时器释放后，通知Source NR释放资源。Source NR回复Namf_Communication_N2InfoNotify Ack消息给Target AMF。如果本地有Secondary RAT Usage Reporting信息，也携带N2 SM Information (Secondary RAT usage data) 信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换完成指示。如果本地有Secondary RAT Usage Reporting信息，也携带缓存的Secondary RAT usage Reporting信息。SMF发送PFCP Session Modification Request消息给UPF，携带Target NR的N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF。SMF回复Nsmf_PDUSession_UpdateSMContext Response给AMF。步骤15启动的定时器超时后，Source AMF发送UE Context Release Command消息给Source NR，通知Source NR释放用户上下文。对于切片不可用对应的PDU Session，Source AMF给SMF发送Nsmf_PDUSession_ReleaseSMContext Request消息，携带 Secondary RAT usage Reporting信息。Source NR释放用户上下文，回复UE Context Release Complete消息给Source AMF。 
基于N2接口的切换，重选I-UPF。基于N2接口的切换，重选I-UPF的流程如图10所示。图10  基于N2接口的切换，重选I-UPF的流程图 说明：若切换前，用户面路径中不存在I-UPF，则Source I-UPF就是UPF（PSA）。若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。流程说明如下：Source NR检测到用户需要切换到Target NR，发送Handover Required消息给Source AMF，携带Handover Type、Target ID、Source To Target Transparent Container等信息。Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target AMF。若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext Request消息给Target AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source To Target Transparent Container等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带用户位置、Target AMF ID、切换准备状态等信息。SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF为Target I-UPF。SMF发送PFCP Session Establishment Request消息给Target I-UPF，通知Target I-UPF创建PDU会话，携带UPF（PSA）的N9隧道信息。Target I-UPF回复PFCP Session Establishment Response消息给SMF，携带Target I-UPF的N3隧道信息。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF，携带PDU会话ID、SM N2 Information。Target AMF下发Handover Request消息给Target NR，携带Handover Type、SM N2 Information List、UE AMBR、Security Context、UE Security Capabilities。Target NR回复Handover Request Acknowledge消息给Target AMF，携带PDU Session Admitted List、Target To Source Transparent Container等信息，其中PDU Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、SM N2 Information。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。Target AMF发送Namf_Communication_CreateUEContext Response消息给Source AMF，携带Target To Source Transparent Container。Source AMF发送Handover Command消息给Source NR，携带Target To Source Transparent Container；Source NR收到Handover Command消息后，通过空口通知UE向目标小区切换。Source NR如果发现有Secondary RAT Usage Reporting信息需要上报，则给AMF发送RAN Usage data report消息，消息中携带Secondary RAT Usage Reporting和handover flag。UE切换到Target NR后，Target NR发送Handover Notify消息，通知Target AMF用户已经成功切换到目标小区。Target AMF收到Handover Notify消息后，发送Namf_Communication_N2InfoNotify消息给Source AMF，通知Source AMF用户已经切换成功。Source AMF启动定时器，在定时器释放后，通知Source NR释放资源，回复Namf_Communication_N2InfoNotify Ack消息给Target AMF。如果本地有Secondary RAT Usage Reporting信息，也携带N2 SM Information (Secondary RAT usage data) 信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换完成指示。如果本地有Secondary RAT Usage Reporting信息，也携带缓存的Secondary RAT usage Reporting信息。SMF发送PFCP Session Modification Request消息给UPF，携带Target NR的N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF。SMF回复Nsmf_PDUSession_UpdateSMContext Response响应消息给Target AMF。若切换前用户面路径中存在I-UPF，则启动定时器。如果步骤17启动的定时器超时后，Source AMF发送UE Context Release Command消息给Source NR，通知Source NR释放用户上下文。对于切片不可用对应的PDU Session，Source AMF给SMF发送Nsmf_PDUSession_ReleaseSMContext Request消息，携带 Secondary RAT usage Reporting信息。Source NR释放用户上下文，回复UE Context Release Complete消息给Source AMF。如果步骤21启动的定时器超时，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source I-UPF释放PDU会话。Source I-UPF回复PFCP Session Release Response消息给SMF。 
基于N2接口的切换，移出I-UPF。基于N2接口的切换，移出I-UPF的流程如图11所示。图11  基于N2接口的切换，移出I-UPF的流程图 说明：若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。流程说明如下：Source NR检测到用户需要切换到Target NR，发送Handover Required消息给Source AMF，携带Handover Type、Target ID、Source To Target Transparent Container等信息。Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target AMF。若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext Request消息给Target AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source To Target Transparent Container等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带用户位置、Target AMF ID、切换准备状态等信息。SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF为UPF（PSA）。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF，携带SM N2 Information。Target AMF下发Handover Request消息给Target NR，携带Handover Type、SM N2 Information List、UE AMBR、Security Context、UE Security Capabilities。Target NR回复Handover Request Acknowledge消息给Target AMF，携带PDU Session Admitted List、Target To Source Transparent Container等信息，其中PDU Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、SM N2 Information。SMF回复Nsmf_PDUSession_UpdateSMContext Response消息给Target AMF。Target AMF发送Namf_Communication_CreateUEContext Response消息给Source AMF，携带Target To Source Transparent Container。Source AMF发送Handover Command消息给Source NR，携带Target To Source Transparent Container。Source NR收到Handover Command消息后，通过空口通知UE向目标小区切换。Source NR如果发现有Secondary RAT Usage Reporting信息需要上报，则给AMF发送RAN Usage data report消息，消息中携带Secondary RAT Usage Reporting和handover flag。UE切换到Target NR后，Target NR发送Handover Notify消息，通知Target AMF用户已经成功切换到目标小区。Target AMF收到Handover Notify消息后，发送Namf_Communication_N2InfoNotify消息给Source AMF，通知Source AMF用户已经切换成功。Source AMF启动定时器，在定时器释放后，通知Source NR释放资源，回复Namf_Communication_N2InfoNotify Ack消息给Target AMF。如果本地有Secondary RAT Usage Reporting信息，也携带N2 SM Information (Secondary RAT usage data) 信息。Target AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给SMF，携带PDU会话ID、切换完成指示。如果本地有Secondary RAT Usage Reporting信息，也携带缓存的Secondary RAT usage Reporting信息。SMF发送PFCP Session Modification Request消息给UPF，携带Target NR的N3隧道信息。UPF回复PFCP Session Modification Response消息给SMF。SMF回复Nsmf_PDUSession_UpdateSMContext Response响应消息给Target AMF。启动定时器，带定时释放后通知I-UPF释放资源。如果步骤15启动的定时器超时，Source AMF发送UE Context Release Command消息给Source NR，通知Source NR释放用户上下文。对于切片不可用对应的PDU Session，Source AMF给SMF发送Nsmf_PDUSession_ReleaseSMContext Request消息，携带 Secondary RAT usage Reporting信息。Source NR释放用户上下文，回复UE Context Release Complete消息给Source AMF。如果步骤19启动的定时器超时，SMF发送PFCP Session Release Request消息给Source I-UPF，通知Source I-UPF释放PDU会话。Source I-UPF回复PFCP Session Release Response消息给SMF。 
RAN触发的Secondary RAT Usage Data Reporting
无线在将要切换或周期性定时上报Secondary RAT Usage Data时，会触发Secondary RAT Usage Data Reporting流程。 
图12  RAN侧触发的Secondary RAT Usage Data Reporting流程

流程说明： 
AMF收到NG-RAN的RAN Usage Data Report消息，消息中携带了Secondary RAT Usage Reporting信息。 
AMF通过Nsmf_PDUSession_UpdateSMContext消息通知V-SMF，携带Secondary RAT Usage Reporting信息。 
V-SMF发送Nsmf_PDUSession_UpdateRequest消息给H-SMF。 
H-SMF发送Nsmf_PDUSession_UpdateSMResponse消息给V-SMF。 
V-SMF返回Nsmf_PDUSession_UpdateSMContextResponse消息给AMF。 
系统影响 :支持Secondary RAT用量数据上报，新增了Secondary RAT Usage上报消息，在现有消息中增加了一些IE的处理，多触发了Nsmf_PDUSession_UpdateSMContext Request/Response消息，会消耗一定的系统资源。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2".|5.12 Charging
3GPP TS 23.502: "Procedures for the 5G System;Stage2".|全文
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.20|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“AMF支持双连接功能”(License ID：7235)，此项目显示为“支持”，表示ZXUN uMAC支持双连接功能。
对其他网元的要求 :UE|RAN|AMF|SMF|UDM
---|---|---|---|---
-|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :新增的配置命令参见下表。 
配置项|命令
---|---
双连接策略配置|SET 5GDUALCONN
SHOW 5GDUALCONN|双连接策略配置
性能统计 :新增的性能计数器参见下表。 
性能计数器名称
---
C510510066 收到 SECONDARY RAT DATA USAGE REPORT 次数
告警和通知 :本特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置该功能，可以实现在SA组网时， AMF把RAN上报上来的第二RAT用量数据透传给I-SMF/V-SMF/A-SMF，以便I-SMF/V-SMF/A-SMF在CDR中区分不同RAT的用量。 
配置前提 :无线RAN采用双连接方式组网。 
AMF支持双连接功能License项已打开。 
配置过程 :执行命令[ SET 5GDUALCONN]:IFAMFDUALCONN="YES",IFSUPUSAGEREPORT="YES"， 设置AMF支持双连接功能， 且支持Secondary RAT Usage Reporting功能。
配置实例 :场景说明 :此功能涉及如下三个场景，这些场景共用相同的配置。 
场景|场景描述|说明
---|---|---
场景1|本地用户SMF上报话单中区分第二RAT用量数据。|通过注册更新、去注册、RAN发送独立SECONDARY RAT DATA USAGE REPORT消息、AN释放、Xn切换、N2切换等流程上报用量信息给SMF。
场景2|漫出用户SMF上报话单中区分第二RAT用量数据。|LBO、HR漫游切出场景，支持上报用量信息给SMF。
场景3|漫入用户V-SMF上报话单中区分第二RAT用量数据。|LBO、HR漫游切入场景，支持上报用量信息给SMF。
数据规划 :配置项|参数|取值
---|---|---
双连接策略配置|AMF支持双连接功能|是
AMF支持用量报告|双连接策略配置|是
配置步骤 :步骤|说明|操作
---|---|---
1|同时打开“AMF支持双连接功能”和“AMF支持用量报告”的开关。|SET 5GDUALCONN:IFAMFDUALCONN="YES",IFSUPUSAGEREPORT="YES"
调整特性 :本特性不涉及调整特性。 


测试用例 :



测试项目|RAN独立消息用量上报
---|---
测试目的|RAN通过发送Secondary RAT Data Usage Report消息将用户的用量报告信息带给AMF，AMF可以将用量上报给SMF。
预置条件|用户注册成功，成功建立PDU。
测试过程|RAN通过发送Secondary RAT Data Usage Report消息将用户的用量报告信息带给AMF。
通过准则|AMF会通过Nsmf_PDUSession_UpdateSMContext消息，将用量报告信息发送给SMF。
测试结果|–


测试项目|Xn切换用量上报
---|---
测试目的|NR在开始切换执行阶段前，会给AMF上报Secondary RAT Usage Reporting信息，携带Handover指示，AMF缓存SecondaryRAT Usage Reporting信息，在切换后续给SMF的消息中顺带Secondary RAT Usage Reporting信息。
预置条件|用户注册成功，成功建立PDU。RAN通过发送Secondary RAT Data Usage Report消息将用户的用量报告信息带给AMF，且携带了Handover指示。
测试过程|RAN发起Xn切换流程。
通过准则|Xn切换过程中，AMF会通过Nsmf_PDUSession_UpdateSMContext消息，将用量报告信息发送给SMF。
测试结果|–


测试项目|N2切换用量上报
---|---
测试目的|NR在开始切换执行阶段前，会给AMF上报Secondary RAT Usage Reporting信息，携带Handover指示，AMF缓存SecondaryRAT Usage Reporting信息，在切换后续给SMF的消息中顺带Secondary RAT Usage Reporting信息。
预置条件|用户注册成功，成功建立PDU。RAN通过发送Secondary RAT Data Usage Report消息将用户的用量报告信息带给AMF，且携带了Handover指示。
测试过程|RAN发起N2切换流程。
通过准则|N2切换过程中，AMF会通过Nsmf_PDUSession_UpdateSMContext消息，将用量报告信息发送给SMF。
测试结果|–


测试项目|去注册时AMF上报第二用量信息给SMF
---|---
测试目的|去注册时AMF上报第二用量信息给SMF。
预置条件|用户注册成功，成功建立PDU。
测试过程|用户发起去注册流程。RAN通过UE Context Release Complete消息携带用量信息。
通过准则|去注册过程中，AMF会通过Nsmf_PDUSession_ReleaseSMContext Request消息，将用量报告信息发送给SMF。
测试结果|–


测试项目|N2释放流程中AMF上报第二用量信息给SMF
---|---
测试目的|N2释放流程中AMF上报第二用量信息给SMF。
预置条件|用户注册成功，成功建立PDU。
测试过|一段时间后UE进入空闲态，以InitUE发起移动性注册流程，触发老连接N2释放流程，RAN在UE ContextRelease Complete中携带用量信息。
通过准则|移动性注册流程中，AMF会通过Nsmf_PDUSession_UpdateSMContext消息，将用量报告信息发送给SMF。
测试结果|–




常见问题处理 :无 
## ZUF-79-18-006 N2接口惯性运行 
特性描述 :特性描述 :描述 :定义 :N2接口惯性运行特性是指当AMF与NR之间的N2链路出现全故障时，处于连接状态的UE用户面不释放，仍旧保持连接态，从而保证正在进行的业务不受影响。
背景知识 :如[图1]所示，园区基站同时连接大网和园区应急网络，其中园区应急AMF下发给基站的权重为0。
图1  园区基站同时连接大网和园区应急网络

正常场景下，园区基站将用户路由到大网网络。当大网N2接口故障时，园区基站会在用户下一次信令业务时，将用户信令业务路由到应急网络。但在用户触发信令业务之前，为了减少N2故障对于用户业务的影响，对于已经激活用户面的PDU会话，在N2故障或者恢复后，仍旧能够保持网络在线，即维持用户处于连接态。 
应用场景 :N2接口惯性运行特性适用的场景为：工业园区，园区内部署应急网络，且该紧急网络仅在园区基站到运营商网络故障时接管业务。 
客户收益 :受益方|受益描述
---|---
运营商|提高系统异常兼容能力，提升网络服务质量。
终端用户|该特性对终端用户不可见。
实现原理 :系统架构 :N2接口惯性运行的系统架构如[图2]所示。
图2  N2接口惯性运行系统架构

涉及的网元 :网元名称|网元作用
---|---
大网AMF|与园区基站之间链路正常时，负责园区用户接入管理。与园区基站之间链路异常时，保持已经接入用户业务惯性运行。
大网SMF|当园区基站与大网AMF之间链路正常时，负责园区用户会话管理。
应急AMF|当园区基站与大网AMF之间N2链路异常时，临时负责用户接入管理，保证在此期间用户业务正常。
应急SMF|当园区基站与大网AMF之间链路异常时，负责园区用户会话管理。
UPF|负责园区用户用户面管理。
NR|当与大网AMF之间链路正常时，将用户信令业务分发到大网AMF。当与大网AMF之间链路异常时，将用户信令业务分发到应急AMF。
协议栈 :该特性涉及的接口协议栈参见[表1]。
接口|协议栈信息参考
---|---
N2|ZUF-79-19-002 N2
N11|ZUF-79-19-004 N11
本网元实现 :对于N2接口惯性运行，本网元支持如下功能： 
本网元支持按DNN和TAI参数来配置用户是否惯性用户。 
当本网元检测到NR链路异常时，对于惯性用户，保持用户连接态，不通知SMF释放用户面，NR与UPF之间的N3隧道仍旧保持；对于非惯性用户，则通知SMF释放用户面，即释放N3隧道。 
当本网元收到NR注册请求消息NG Setup Request时，若请求消息中携带UE Retention指示，则在NG Setup Response响应中，携带UE Retention指示。 
业务流程 :N2链路异常，用户惯性运行
N2链路异常，用户惯性运行的流程如[图3]所示。
图3  N2链路异常，用户惯性运行

流程说明： 
UE已经注册并激活PDU会话，且处于连接态。 
大网AMF检测到NR的链路异常。 
大网AMF根据已激活PDU会话的DNN以及用户当前TA，判断用户是否为惯性用户。若用户为惯性用户，则保持用户处于连接态，即不释放用户面；否则，通知SMF释放用户面，用户进入空闲态。 
NR触发注册流程
NR触发注册流程如[图4]所示。
图4  NR触发注册流程

流程说明： 
UE已经注册并激活PDU会话，且处于连接态。 
NR在故障恢复后，触发NG Setup Request消息，携带UE Retention指示，指示大网AMF保留用户N2链接。 
大网AMF根据本地策略，判断支持UE Retention，则回复NG Setup Response时，携带UE Retention指示。 
用户保持链接状态，惯性运行。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准类别|标准名称
---|---
TS 23.501|System Architecture for the 5G System
TS 23.502|Procedures for the 5G System
TS 38.413|NG Application Protocol (NGAP)
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.22.20|首次发布。
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 :UE|NR|SMF|UPF
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :命令名称|描述
---|---
SET INERTIAOPPLYCFG|修改惯性运行策略配置的参数。
SHOW INERTIAOPPLYCFG|查询惯性运行策略配置。
ADD DNNTAI NON INERTIA USER|新增指定DNN和TAI的非惯性用户配置，根据DNN和TAI来配置用户是否为非惯性用户。
DEL DNNTAI NON INERTIA USER|删除指定DNN和TAI的非惯性用户配置。
SHOW DNNTAI NON INERTIA USER|查询指定DNN和TAI的非惯性用户配置。
ADD DNNTAI INERTIA USER|新增指定DNN和TAI的惯性用户配置，根据DNN和TAI来配置用户是否为惯性用户。
DEL DNNTAI INERTIA USER|删除指定DNN和TAI的惯性用户配置。
SHOW DNNTAI INERTIA USER|查询指定DNN和TAI的惯性用户配置。
命令名称|相关参数
---|---
SET INERTIAOPPLYCFG|涉及惯性运行策略、gNB局向信息同步时长(分钟)参数。
SHOW INERTIAOPPLYCFG|涉及惯性运行策略、gNB局向信息同步时长(分钟)参数。
ADD DNNTAI NON INERTIA USER|涉及DNN、移动国家码、移动网络码、跟踪区码参数。
DEL DNNTAI NON INERTIA USER|涉及DNN、移动国家码、移动网络码、跟踪区码参数。
SHOW DNNTAI NON INERTIA USER|涉及DNN、移动国家码、移动网络码、跟踪区码参数。
ADD DNNTAI INERTIA USER|涉及DNN、移动国家码、移动网络码、跟踪区码参数。
DEL DNNTAI INERTIA USER|涉及DNN、移动国家码、移动网络码、跟踪区码参数。
SHOW DNNTAI INERTIA USER|涉及DNN、移动国家码、移动网络码、跟踪区码参数。
性能统计 :该特性不涉及计数器。 
告警和通知 :该特性不涉及告警/通知消息。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过修改惯性运行策略配置，新增指定DNN和TAI的非惯性用户配置和新增指定DNN和TAI的惯性用户配置，实现AMF支持N2接口惯性运行功能。 
当园区基站和运营商虚拟云上的AMF之间的N2接口链路故障，或者下沉到园区的UPF和运营商虚拟云上的SMF之间的N4接口链路发生故障时，才需要选择用户惯性运行策略，使用本配置。惯性运行策略默认为全为惯性用户，即发生N2链路故障时，处于连接态的用户数据业务不受影响。
配置前提 :已完成了初始配置。 
配置过程 :执行[SET INERTIAOPPLYCFG]命令，修改惯性运行策略配置。
其中惯性运行策略参数：
该参数设置为ALL_INERTIA，表示全部用户都支持惯性运行。该参数默认值为ALL_INERTIA。 
该参数设置为NONE_INERTIA，表示全部用户都不支持惯性运行。 
该参数设置为SPECIFIED_INERTIA，表示只有属于基于DNN和TAI惯性用户配置的用户（通过ADD DNNTAI INERTIA USER命令配置），才支持惯性运行，其他用户不支持惯性运行。 
该参数设置为SPECIFIED_NONE_INERTIA，表示只有属于基于DNN和TAI非惯性用户配置的用户（通过ADD DNNTAI NON INERTIA USER命令配置），不支持惯性运行，其他用户支持惯性运行。 
该参数默认值为ALL_INERTIA。 
2. （可选）执行[ADD DNNTAI NON INERTIA USER]命令，新增指定DNN和TAI的非惯性用户配置。
3. （可选）执行[ADD DNNTAI INERTIA USER]命令，新增指定DNN和TAI的惯性用户配置。
配置实例 :场景说明 :当园区基站和运营商虚拟云上的AMF之间的N2接口链路故障，或者下沉到园区的UPF和运营商虚拟云上的SMF之间的N4接口链路发生故障时，需要选择用户惯性运行策略，决策处于连接态的用户是否保持惯性运行。以惯性运行策略配置中惯性运行策略参数选择SPECIFIED_INERTIA为例：
满足指定惯性用户配置的用户，将保持惯性运行。 
不满足指定惯性用户配置的用户，将不能保持惯性运行。 
数据规划 :命令|参数名称|取值|数据来源|说明
---|---|---|---|---
SET INERTIAOPPLYCFG|惯性运行策略（inertiaopply）|SPECIFIED_INERTIA|本端规划|配置惯性运行的用户范围，默认全部用户都支持惯性运行。
gNB局向信息同步时长(分钟)（gnbinfodur）|SET INERTIAOPPLYCFG|8|本端规划|控制服务上电后，在配置的时间长度内，不会由于NR局向信息不存在而判定AMF到该NR之间发生断链。
ADD DNNTAI INERTIA USER|DNN（dnn）|zte.com.cn|本端规划|配置惯性用户的DNN。
移动国家码（mcc）|ADD DNNTAI INERTIA USER|460|全网规划|配置惯性用户TAI中的MCC，由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。
移动网络码（mnc）|ADD DNNTAI INERTIA USER|11|全网规划|配置惯性用户TAI中的MNC，由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。
跟踪区码（tac）|ADD DNNTAI INERTIA USER|123456|全网规划|配置惯性用户TAI中的TAC，由运营商在PLMN内统一规划，以16进制数字编码。
配置步骤 :步骤|说明|操作
---|---|---
1|配置惯性运行策略为SPECIFIED_INERTIA。|SET INERTIAOPPLYCFG:INERTIAOPPLY="SPECIFIED_INERTIA",GNBINFODUR=8
2|新增基于DNN和TAI惯性用户配置。|ADD DNNTAI INERTIA USER:DNN="zte.com.cn",MCC="460",MNC="11",TAC="123456"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|N2接口故障时连接态用户惯性运行情况
---|---
测试目的|验证N2接口故障时，惯性运行策略配置为指定惯性用户的连接态用户能否保持惯性运行。
预置条件|初始配置已经完成。
测试过程|惯性运行策略配置为SPECIFIED_INERTIA基于DNN和TAI惯性用户配置中正确配置DNN、MCC、MNC、TAC，这些需要和测试目标用户PUD会话中的DNN与用户的current TAI相匹配，即将该测试用户配置为指定的惯性用户。用户发起附着。用户进行业务，在一段时间后，N2口发生故障。
通过准则|该目标测试用户保持惯性运行，保持连接态。若存在其他用户，则不匹配“基于DNN和TAI惯性用户配置”的用户，不能保持惯性运行，不能使用数据业务。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## A-SMF 
Anchor-SMF锚点SMF
AMF :Access and Mobility Management Function接入和移动管理功能
AUSF :Authentication Server Function鉴权服务器功能
## CDR 
Call Detail Record呼叫详细记录，即话单
DNN :Data Network Name数据网名称
EIR :Equipment Identity Register设备标识寄存器
## EN-DC 
E-UTRA-NR Dual ConnectivityE-UTRA和NR的双连接
## GWCN 
Gateway Core Network网关核心网
## I-SMF 
Intermediate-SMF中间SMF
## MCC 
Mobile Country Code移动国家码
## MNC 
Mobile Network Code移动网络号
## MOCN 
Multi-Operator Core Network多运营商核心网
## MR-DC 
Multi-RAT Dual Connectivity多RAT双连接
## NE-DC 
NR-E-UTRA Dual ConnectivityNR和E-UTRA的双连接
## NGEN-DC 
NG-RAN E-UTRA-NR Dual ConnectivityNG-RAN E-UTRA和NR的双连接
## NR 
New Radio新无线
NSSF :Network Slice Selection Function网络切片选择功能
PCF :Policy Control Function策略控制功能
## PEI 
Permanent Equipment Identifier永久设备标识
RAN :Radio Access Network无线接入网
RAT :Radio Access Technology无线接入技术
## RLC 
Radio Link Control无线链路控制
## SA 
Standalone5G独立组网
## SCG 
Secondary Cell Group辅助小区组
SMF :Session Management Function会话管理功能
## TAC 
Tracking Area Code跟踪区域码
## TAI 
Tracking Area Identity跟踪区标识
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
UPF :User Plane Function用户平面功能
# ZUF-79-19 接口 
## ZUF-79-19-001 N1 
描述 :N1接口是UE和AMF/SMF之间的接口，用于UE和AMF/SMF之间的消息交互。作为N1接口的终结点，AMF除了处理发往自身的移动管理类消息，还透明传递UE和SMF之间的会话管理类消息。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|作为核心网侧N1接口终结点，处理N1接口移动性管理类消息、N1层安全。
SMF|NF|处理N1接口会话管理类消息。
网元|(R)AN|透明传递N1接口消息。
UE|网元|处理N1接口消息，包括移动性管理类和会话管理类消息。
协议栈 :UE与AMF间的接口协议栈如下图所示，图中的(R)AN Protocol
Layer为UE与(R)AN之间空口协议栈。 
UE与SMF间的接口协议栈如下图所示，图中的(R)AN
Protocol Layer为UE与(R)AN之间空口协议栈，NAS-SM为N1接口负责会话管理的消息，UE和SMF之间的消息是由AMF进行透明传递的。 

消息描述 :N1接口所支持的消息参见下表。 
分类|消息名称|方向|说明
---|---|---|---
移动性管理消息|Authentication request|AMF->UE|AMF向UE发送的鉴权请求
Authentication response|移动性管理消息|UE->AMF|UE回复的鉴权响应
Authentication result|移动性管理消息|UE->AMF|EAP-AKA'鉴权过程中，UE回复给核心网的鉴权结果
Authentication failure|移动性管理消息|UE->AMF|EPS-AKA'鉴权过程中，UE通知AMF鉴权失败
Authentication reject|移动性管理消息|UE->AMF|EPS-AKA'鉴权过程中，UE通知AMF鉴权拒绝
Registration request|移动性管理消息|UE->AMF|用于UE首次注册，或者位置变化时，发送注册请求给AMF
Registration Accept|移动性管理消息|AMF->UE|用于AMF接受UE注册请求时，下发注册接受消息给UE
Registration complete|移动性管理消息|UE->AMF|当AMF请求消息中包含5G-GUTI时，UE向AMF确认注册接受消息
Registration reject|移动性管理消息|AMF->UE|用于AMF通知UE拒绝注册
UL NAS transport|移动性管理消息|UE->AMF|UE向AMF发送上行NAS传输消息，用于传送短消息、LPP消息等
DL NAS transport|移动性管理消息|AMF->UE|AMF向UE发送下行NAS传输消息，用于传送短消息、LPP消息等
De-registration request(UE originating de-registration)|移动性管理消息|UE->AMF|用于UE通知AMF，UE去注册
De-registration accept(UE originating de-registration)|移动性管理消息|AMF->UE|用于AMF通知UE，去注册请求已接受
De-registration request(UE terminated de-registration)|移动性管理消息|AMF->UE|用于AMF通知UE，终止去注册
De-registration accept(UE terminated de-registration)|移动性管理消息|UE->AMF|用于UE回复AMF，注册已终止
Service request|移动性管理消息|UE->AMF|UE向AMF发送业务请求
Service accept|移动性管理消息|AMF->UE|AMF向UE回复接受业务请求
Service reject|移动性管理消息|AMF->UE|用于AMF通知UE拒绝业务请求
Configuration update command|移动性管理消息|AMF->UE|AMF向UE发送配置更新请求
Configuration update complete|移动性管理消息|UE->AMF|UE向AMF确认配置更新请求
Identity request|移动性管理消息|AMF->UE|AMF向UE发送标识请求
Identity response|移动性管理消息|UE->AMF|UE向AMF回复标识响应
Notification request|移动性管理消息|AMF->UE|AMF向UE发送通知请求
Notification response|移动性管理消息|UE->AMF|UE回复通知响应
Security mode command|移动性管理消息|AMF->UE|AMF向UE发送安全模式请求
Security mode complete|移动性管理消息|UE->AMF|UE向AMF回复安全模式请求
Security mode reject|移动性管理消息|UE->AMF|AMF通知UE拒绝安全模式请求
5GMM status|移动性管理消息|AMF<-->UE|任何时刻，当UE或者AMF处理收到的5G移动性管理协议栈数据失败时，UE或者AMF可以发送该消息给对端，指示错误发生
会话管理消息|PDU session establishment request|UE->SMF|UE向SMF发送PDU会话建立请求
PDU session establishment accept|会话管理消息|SMF->UE|SMF回复UE接受PDU会话建立请求
PDU session establishment reject|会话管理消息|SMF->UE|SMF回复UE拒绝PDU会话建立
PDU session authentication command|会话管理消息|SMF->UE|SMF向UE发送PDU会话鉴权请求
PDU session authentication complete|会话管理消息|UE->SMF|UE向SMF确认PDU会话鉴权请求
PDU session modification request|会话管理消息|UE->SMF|UE向SMF发送PDU会话修改请求
PDU session modification reject|会话管理消息|SMF->UE|SMF回复UE拒绝PDU会话修改
PDU session modification command|会话管理消息|SMF->UE|SMF向UE发送PDU会话修改命令
PDU session modification complete|会话管理消息|UE->SMF|UE向SMF确认PDU会话修改命令
PDU session modification command reject|会话管理消息|UE->SMF|UE回复SMF拒绝PDU会话修改
PDU session release request|会话管理消息|UE->SMF|UE向SMF发送PDU会话释放请求
PDU session release reject|会话管理消息|SMF->UE|SMF回复UE拒绝PDU会话释放
PDU session release command|会话管理消息|SMF->UE|SMF向UE发送PDU会话释放命令
PDU session release complete|会话管理消息|UE->SMF|UE向SMF确认PDU会话释放
5GSM status|会话管理消息|SMF<-->UE|任何时刻，当UE或者SMF处理收到的5G会话管理协议栈数据失败时，UE或者SMF可以发送该消息给对端，指示错误发生
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 24.501|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
3GPP|3GPP TS 33.501|Security Architecture and Procedures for 5G System
## ZUF-79-19-002 N2 
描述 :N2接口是(R)AN和AMF之间的接口，用于(R)AN和AMF间的上下文管理、会话管理等消息的交互。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|作为核心网侧N2接口终结点，处理网元级、用户级N2接口消息，比如进行NR注册、配置更新、UE上下文管理等N2接口消息处理。另外，AMF还透传(R)AN侧发送的PDU会话级N2接口消息给SMF，或者透传SMF发送的PDU会话级消息给(R)AN。
SMF|NF|处理N2接口PDU会话级的消息。
网元|(R)AN|处理N2接口消息，以及TNL连接管理。
协议栈 :(R)AN与AMF间的接口协议栈如下图所示： 
(R)AN与SMF间的接口协议栈如下图所示： 

消息描述 :N2接口所支持的消息参见下表。 
分类|消息名|方向|说明
---|---|---|---
PDU会话管理消息|PDU SESSION RESOURCE SETUP REQUEST|AMF->(R)AN|AMF通知(R)AN给一个或者多个PDU会话分配资源
PDU SESSION RESOURCE SETUP RESPONSE|PDU会话管理消息|(R)AN->AMF|(R)AN回复PDU会话分配资源的响应给AMF
PDU SESSION RESOURCE RELEASE COMMAND|PDU会话管理消息|AMF->(R)AN|AMF通知(R)AN释放已经建立的PDU会话资源
PDU SESSION RESOURCE RELEASE RESPONSE|PDU会话管理消息|(R)AN->AMF|(R)AN回复释放PDU会话资源响应给AMF
PDU SESSION RESOURCE MODIFY REQUEST|PDU会话管理消息|AMF->(R)AN|AMF通知(R)AN修改已有PDU会话
PDU SESSION RESOURCE MODIFY RESPONSE|PDU会话管理消息|(R)AN->AMF|(R)AN回复PDU会话修改响应给AMF
PDU SESSION RESOURCE NOTIFY|PDU会话管理消息|(R)AN->AMF|当已建立的PDU会话资源或者QoS Flow被释放等场景发生时，(R)AN通知AMF
PDU SESSION RESOURCE MODIFY INDICATION|PDU会话管理消息|(R)AN->AMF|(R)AN向AMF发送PDU会话修改指示
PDU SESSION RESOURCE MODIFY CONFIRM|PDU会话管理消息|AMF->(R)AN|AMF向(R)AN确认PDU会话修改
UE上下文管理消息|INITIAL CONTEXT SETUP REQUEST|AMF->(R)AN|AMF向(R)AN发送初始上下文建立请求
INITIAL CONTEXT SETUP RESPONSE|UE上下文管理消息|(R)AN->AMF|(R)AN向AMF回复初始上下文建立响应
INITIAL CONTEXT SETUP FAILURE|UE上下文管理消息|(R)AN->AMF|(R)AN回复AMF初始上下文建立失败
UE CONTEXT RELEASE REQUEST|UE上下文管理消息|(R)AN->AMF|(R)AN向AMF发送UE上下文释放请求
UE CONTEXT RELEASE COMMAND|UE上下文管理消息|AMF->(R)AN|AMF向(R)AN发送UE上下文释放命令
UE CONTEXT RELEASE COMPLETE|UE上下文管理消息|(R)AN->AMF|(R)AN向AMF确认UE上下文释放
UE CONTEXT MODIFICATION REQUEST|UE上下文管理消息|AMF->(R)AN|AMF向(R)AN发送UE上下文修改请求
UE CONTEXT MODIFICATION RESPONSE|UE上下文管理消息|(R)AN->AMF|(R)AN向AMF返回UE上下文修改响应
UE CONTEXT MODIFICATION FAILURE|UE上下文管理消息|(R)AN->AMF|(R)AN回复AMF，UE上下文修改失败
UE移动性管理消息|HANDOVER REQUIRED|(R)AN->AMF|(R)AN向AMF发送切换需求
HANDOVER COMMAND|UE移动性管理消息|AMF->(R)AN|AMF向(R)AN发送切换命令
HANDOVER PREPARATION FAILURE|UE移动性管理消息|AMF->(R)AN|AMF向(R)AN发送切换准备失败消息
HANDOVER REQUEST|UE移动性管理消息|AMF->(R)AN|AMF向(R)AN发送切换请求
HANDOVER REQUEST ACKNOWLEDGE|UE移动性管理消息|(R)AN->AMF|(R)AN向AMF返回切换请求响应
HANDOVER FAILURE|UE移动性管理消息|(R)AN->AMF|(R)AN向AMF发送切换失败消息
HANDOVER NOTIFY|UE移动性管理消息|(R)AN->AMF|(R)AN向AMF发送切换通知
PATH SWITCH REQUEST|UE移动性管理消息|(R)AN->AMF|(R)AN向AMF发送路径转换请求
PATH SWITCH REQUEST ACKNOWLEDGE|UE移动性管理消息|AMF->(R)AN|AMF向(R)AN返回路径转换响应
PATH SWITCH REQUEST FAILURE|UE移动性管理消息|AMF->(R)AN|AMF向(R)AN发送路径转换失败消息
HANDOVER CANCEL|UE移动性管理消息|(R)AN->AMF|(R)AN向AMF发送切换取消消息
HANDOVER CANCEL ACKNOWLEDGE|UE移动性管理消息|AMF->(R)AN|AMF向(R)AN返回切换取消响应
寻呼消息|PAGING|AMF->(R)AN|AMF向(R)AN发送寻呼请求消息
NAS传递消息|INITIAL UE MESSAGE|(R)AN->AMF|(R)AN向AMF发送初始UE消息
DOWNLINK NAS TRANSPORT|NAS传递消息|AMF->(R)AN|AMF向(R)AN发送下行NAS传输消息
UPLINK NAS TRANSPORT|NAS传递消息|(R)AN->AMF|(R)AN向AMF发送上行NAS传输消息
NAS NON DELIVERY INDICATION|NAS传递消息|(R)AN->AMF|(R)AN向AMF发送NAS未投递指示
REROUTE NAS REQUEST|NAS传递消息|AMF->(R)AN|AMF向(R)AN发送重路由NAS请求
接口管理消息|NG SETUP REQUEST|(R)AN->AMF|(R)AN向AMF发送建立NG请求
NG SETUP RESPONSE|接口管理消息|AMF->(R)AN|AMF向(R)AN返回建立NG响应
NG SETUP FAILURE|接口管理消息|AMF->(R)AN|AMF向(R)AN发送建立NG失败消息
RAN CONFIGURATION UPDATE|接口管理消息|(R)AN->AMF|(R)AN向AMF发送RAN配置更新请求
RAN CONFIGURATION UPDATE ACKNOWLEDGE|接口管理消息|AMF->(R)AN|AMF向(R)AN返回RAN配置更新响应
RAN CONFIGURATION UPDATE FAILURE|接口管理消息|AMF->(R)AN|AMF向(R)AN发送RAN配置更新失败消息
AMF CONFIGURATION UPDATE|接口管理消息|AMF->(R)AN|AMF向(R)AN发送AMF配置更新请求
AMF CONFIGURATION UPDATE ACKNOWLEDGE|接口管理消息|(R)AN->AMF|(R)AN向AMF返回AMF配置更新响应
AMF CONFIGURATION UPDATE FAILURE|接口管理消息|(R)AN->AMF|(R)AN向AMF发送AMF配置更新失败消息
NG RESET|接口管理消息|(R)AN->AMF|(R)AN向AMF发送NG RESET消息
NG RESET ACKNOWLEDGE|接口管理消息|AMF->(R)AN|AMF向(R)AN返回NG RESET响应
ERROR INDICATION|接口管理消息|AMF->(R)AN或(R)AN->AMF|错误指示，AMF和(R)AN之间可以相互发送
配置传输消息|UPLINK RAN CONFIGURATION TRANSFER|AMF->(R)AN|AMF向(R)AN发送上行RAN配置传输消息
DOWNLINK RAN CONFIGURATION TRANSFER|配置传输消息|(R)AN->AMF|(R)AN向AMF发送下行RAN配置传输消息
位置报告消息|LOCATION REPORTING CONTROL|AMF->(R)AN|AMF向(R)AN发送位置报告控制消息
LOCATION REPORTING FAILURE INDICATION|位置报告消息|(R)AN>AMF|(R)AN向AMF发送位置报告失败指示
LOCATION REPORT|位置报告消息|(R)AN->AMF|(R)AN向AMF发送位置报告消息
UE TNLA绑定消息|UE TNLA BINDING RELEASE REQUEST|AMF->(R)AN|AMF向(R)AN发送UE TNLA绑定释放请求
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 38.413|NG-RAN; NG Application Protocol (NGAP)
## ZUF-79-19-003 N8 
描述 :N8接口是UDM和AMF之间的接口。通过N8接口，UDM完成对AMF的注册管理服务和签约数据管理服务。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|AMF通过N8接口完成向UDM注册的服务，包括：注册、去注册、更新等服务。AMF通过N8接口完成用户签约数据管理服务，包括：获取签约数据、订阅签约数据、去订阅签约数据等。
UDM|NF|UDM通过N8接口完成对AMF的注册管理服务，包括：注册、去注册、更新、去注册通知等服务。UDM通过N8接口完成AMF相关的用户签约数据管理服务，包括：UDM向AMF下发签约数据、UDM在AMF订阅的签约数据发生改变时通知AMF等。
协议栈 :UDM与AMF间的N8接口协议栈如下图所示： 

消息描述 :N8接口所支持的服务参见下表。 
服务|服务操作|操作语义|说明
---|---|---|---
Subscriber Data Management (SDM)|Get|Request/Response|AMF从UDM中获取签约信息，比如用户签约的网络切片选择信息，接入和移动性签约信息等。
Subscribe|Subscriber Data Management (SDM)|Subscribe/Notify|AMF从UDM订阅用户签约信息变化通知。
Unsubscribe|Subscriber Data Management (SDM)|Subscribe/Notify|AMF从UDM取消订阅用户签约信息变化通知。
Notification|Subscriber Data Management (SDM)|Subscribe/Notify|UDM通知AMF用户的签约数据发生变化。
UE Context Management (UECM)|Registration|Request/Response|在UDM中注册AMF，存贮UE上下文中和该AMF相关的信息。
DeregistrationNotification|UE Context Management (UECM)|Subscribe/Notify|UDM通知AMF，UDM中去注册相关信息。
Deregistration|UE Context Management (UECM)|Request/Response|AMF请求UDM删除UE上下文中和该AMF相关的信息，UDM中此AMF相关的订阅也被删除。
Update|UE Context Management (UECM)|Request/Response|AMF更新UDM中UE相关信息，比如更新PEI。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP|3GPP TS 23.502|Procedures for the 5G System
3GPP|3GPP TS 29.500|5G System; Technical Realization of Service Based Architecture; Stage 3
3GPP|3GPP TS 29.501|5G System;Principle and Guidelines for Service Definition
3GPP|3GPP TS 29.503|5G System; Unified Data Management Services
## ZUF-79-19-004 N11 
描述 :N11接口是AMF和SMF之间的接口，用于AMF和SMF之间会话管理、事件订阅等消息的交互。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|为SMF提供如下服务： N1/N2消息传输：将会话管理的N1/N2消息透传给SMF。EBI管理：分配、释放EBI。事件订阅：为SMF提供订阅服务，确保事件发生时SMF能够得到通知，比如UE移出感兴趣区域。
SMF|NF|负责PDU会话管理，为AMF提供PDU会话管理服务，包括PDU会话建立、修改、释放以及PDU会话上下文收集。
协议栈 :N11接口协议栈如下图所示： 

消息描述 :AMF和SMF通过调用服务，实现消息交互。N11接口中，涉及AMF和SMF的服务操作参见下表。 
NF|服务|操作|操作语义|说明
---|---|---|---|---
AMF|Namf_Communication|N1N2MessageTransfer|Request/Response|用于SMF向(R)AN或UE发送N1或N2消息
EBIAssignment|AMF|Namf_Communication|Request/Response|用于PDU会话激活流程中，SMF向AMF请求分配EBI
Namf_EventExposure|AMF|Subscribe|Subscribe/Notify|用于其他NF，比如SMF向AMF进行事件订阅
UnSubscribe|Namf_EventExposure|AMF|Subscribe/Notify|用于其他NF，比如SMF向AMF取消之前订阅的事件
Notify|Namf_EventExposure|AMF|Subscribe/Notify|用于SMF订阅的事件发生时，AMF通知SMF
SMF|Nsmf_PDUSession|Create SM context|Request/Response|用于AMF通知SMF创建PDU会话
Update SM Context|SMF|Nsmf_PDUSession|Request/Response|用于AMF通知SMF更新PDU会话
Release SM Context|SMF|Nsmf_PDUSession|Request/Response|用于AMF通知SMF释放PDU会话
Context|SMF|Nsmf_PDUSession|Request/Response|用于AMF间注册更新或者切换流程中，源AMF向SMF获取PDU会话上下文
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 29.502|5G System; Session Management Services; Stage 3
3GPP|3GPP TS 29.518|5G System; Access and Mobility Management Services; Stage 3
## ZUF-79-19-005 N12 
概述 :AMF为AMF和AUSF之间的连接提供了N12协议接口。 
客户收益 :AMF通过N12协议接口与AUSF对接。 
说明 :AMF和AUSF之间的接口协议基于HTTP RESTful业务接口提供服务。协议栈如下： 
图1  协议栈

## ZUF-79-19-006 N14 
描述 :N14接口用于AMF间用户上下文消息的交互。 
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|在AMF发生变化的移动性业务过程中，源AMF和目标AMF间传递用户上下文。
协议栈 :AMF间的接口协议栈如下图所示： 

消息描述 :N14接口涉及的AMF服务化操作参见下表。 
NF|服务|操作|操作语义|说明
---|---|---|---|---
AMF|Namf_Communication|UEContextTransfer|Request/Response|用于目标AMF向源AMF请求用户上下文。
RegistrationCompleteNotify|AMF|Namf_Communication|Subscribe / Notify|用于目标AMF通知源AMF，用户已经在目标AMF注册成功。
CreateUEContext|AMF|Namf_Communication|Request/Response|用于AMF变化的切换流程中，源AMF将用户上下文传递给目标AMF。
ReleaseUEContext|AMF|Namf_Communication|Request/Response|用于切换取消流程中，源AMF通知目标AMF取消切换。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 29.518|5G System; Access and Mobility Management Services; Stage 3
## ZUF-79-19-007 N15 
描述 :N15接口是AMF和PCF之间的接口，用于AMF和PCF之间的消息交互。AMF可以通过N15接口向PCF请求AM（Access&Mobility）策略控制，或上报AM策略控制相关事件。PCF可以通过N15接口向AMF推送最新的AM策略，并订阅AM策略控制相关事件。 
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF|说明
---|---
NF|PCF|向AMF提供AM（Access&Mobility）策略，并订阅相关事件。
AMF|NF|执行PCF提供的AM策略，并向PCF上报相关事件。
协议栈 :AMF与PCF间的接口协议栈如下图所示： 

消息描述 :AMF和PCF通过服务操作的调用，实现消息交互。AMF和PCF在N15接口提供的服务操作如下： 
NF|服务|操作|操作语义|说明
---|---|---|---|---
PCF|Npcf_AMPolicyControl|Create|Request/Response|AMF向PCF请求建立AM策略关联，PCF在响应中下发AM策略，并订阅AM策略控制相关事件。
Update|PCF|Npcf_AMPolicyControl|Request/Response|AMF向PCF上报AM策略控制相关事件，PCF在响应中可能更新AM策略和事件订阅。
Delete|PCF|Npcf_AMPolicyControl|Request/Response|AMF请求PCF删除AM策略关联。
UpdateNotify|PCF|Npcf_AMPolicyControl|Subscribe/Notify|PCF因为内部或外部事件触发，主动向AMF更新AM策略和事件订阅。AM策略更新通知操作不需要显式的订阅操作，在AMF调用Create操作请求PCF建立AM策略关联时，PCF就认为AMF订阅了AM策略更新通知。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System (R15)
3GPP|3GPP TS 23.502|Procedures for the 5G System (R15)
3GPP|3GPP TS 23.503|Policy and Charging Control Framework for the 5G System (R15)
3GPP|3GPP TS 29.507|Access and Mobility Policy Control Service（R15）
## ZUF-79-19-008 N22 
描述 :N22接口是AMF和NSSF之间的接口，用于AMF和NSSF之间的消息交互。AMF通过N22接口调用NSSF提供的服务，可以在UE注册时重选AMF，在PDU会话激活时选择SMF，或者更新切片配置信息。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|AMF调用NSSF提供的服务，可以在UE注册时重选AMF，在PDU会话激活时选择SMF，或者更新切片配置信息。
NSSF|NF|存储全网切片信息，并对外提供查询服务。
协议栈 :N22接口协议栈如下图所示： 

消息描述 :N22接口中，涉及AMF和NSSF的服务操作参见下表。 
NF|服务|操作|操作语义|说明
---|---|---|---|---
NSSF|Nnssf_NSSelection|Get|Request/Response|应用于注册过程中重选AMF，或PDU会话激活过程中选择SMF。
Nnssf_NSSAIAvailability|NSSF|Update|Request/Response|用于AMF向NSSF更新TA所支持的S-NSSAIs信息，并从NSSF获取TA下受限的S-NSSAIs信息。
Notify|Nnssf_NSSAIAvailability|NSSF|Subscribe/Notify|用于当NSSF上TA与S-NSSAI关系发生变化时，比如某S-NSSAI在TA下由不受限变成受限时，NSSF向AMF通知这些变化信息。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 29.510|5G System; Network function repository services; Stage 3
## ZUF-79-19-009 N26 
描述 :N26接口是MME和AMF之间的接口，用于4/5G跨系统切换时，AMF和MME之间进行信息传递。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|负责MME节点选择，收发N26接口消息，完成5G MM上下文和4G MM上下文相互转化。
MME|NF|负责AMF节点选择，收发N26接口消息。
协议栈 :N26接口协议栈如下图所示。 

消息描述 :N26接口中，涉及AMF和MME的消息参见下表。 
消息名称|方向|说明
---|---|---
Forward Relocation Request|AMF<->MME|用于4/5G跨系统切换时，用户需要切换，并在该消息中携带用户MM上下文以及PDN连接上下文。
Forward Relocation Response|AMF<->MME|用于4/5G跨系统切换时，目标侧MME向源侧AMF回复切换响应或者目标侧AMF向源侧MME回复切换响应。
Forward Relocation Complete Notification|AMF<->MME|用于4/5G跨系统切换时，用户已经切换到目标侧。
Forward Relocation Complete Acknowledge|AMF<->MME|用于4/5G跨系统切换时，源侧AMF回复切换成功通知确认消息给目标侧MME或者源侧MME回复切换成功通知确认消息给目标侧AMF。
Relocation Cancel Request|AMF<->MME|用于4/5G跨系统切换时，源侧AMF通知目标侧MME切换取消或者源侧MME通知目标侧AMF切换取消。
Relocation Cancel Response|AMF<->MME|用于4/5G跨系统切换时，目标侧MME取消切换后，回复响应给源侧AMF或者目标侧AMF取消切换后，回复响应给源侧MME。
Context Request|AMF<->MME|用于4/5G跨系统切换时，目标侧MME向源侧AMF请求用户上下文或者目标侧AMF向源侧MME请求用户上下文。
Context Response|AMF<->MME|用于4/5G跨系统切换时，源侧AMF回复上下文请求响应给目标侧MME或者源侧MME回复上下文请求响应给目标侧AMF。
Context Acknowledge|AMF<->MME|用于4/5G跨系统切换时，目标侧MME回复上下文请求响应确认消息给源侧AMF或者目标侧AMF回复上下文请求响应确认消息给源侧MME。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 29.274|Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C)
## ZUF-79-19-010 Nnrf 
概述 :AMF为AMF和NRF之间的连接提供了Nnrf协议接口。 
客户收益 :AMF通过Nnrf协议接口与NRF对接。 
说明 :AMF和NRF之间的接口协议基于HTTP RESTful业务接口提供服务。协议栈如下： 
图1  协议栈

## ZUF-79-19-011 N18 
概述 :AMF为AMF和UDSF之间的连接提供了NUDSF协议接口。 
客户收益 :AMF通过Nudsf协议接口与UDSF对接。 
说明 :AMF与UDSF之间的接口协议是通过私有接口实现的。 
图1  N18接口

## ZUF-79-19-012 N20 
概述 :AMF为AMF和SMSF之间的连接提供了N20协议接口。
客户收益 :AMF通过N20协议接口与SMSF对接。 
说明 :AMF与SMSF之间的接口协议是通过基于HTTP RESTful的服务接口实现的。 
图1  N20协议栈

## ZUF-79-19-013 NL1/NLs 
描述 :NL1接口是AMF和LMF之间的接口，用于AMF和LMF之间定位流程的处理。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|AMF通过NL1接口向LMF发起用户定位请求。
LMF|NF|LMF通过NL1接口向AMF返回用户定位响应。
协议栈 :NL1接口协议栈如下图所示： 

消息描述 :NL1接口所支持的消息参见下表。 
服务|服务操作|操作语义|说明
---|---|---|---
Nlmf_Location|DetermineLocation|Request/Response|AMF向LMF发起用户定位请求并获得定位结果响应。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.273|5G System (5GS) Location Services (LCS); Stage 2
3GPP|3GPP TS 29.518|5G System; Access and Mobility Management Services; Stage 3
3GPP|3GPP TS 29.572|5G System; Location Management Services; Stage 3
## ZUF-79-19-014 NL2/NLg 
描述 :NL2接口是AMF和GMLC之间的接口，用于AMF和GMLC之间定位流程的处理。
实现原理 :涉及的网元 :涉及的NF/网元参见下表。 
NF/网元|说明
---|---
NF|AMF|AMF通过NL2接口向GMLC发送事件通知消息。AMF通过NL2接口向GMLC返回定位信息响应。
GMLC|NF|GMLC通过NL2接口向AMF发起定位信息请求。
协议栈 :NL2接口协议栈如下图所示： 

消息描述 :NL2接口所支持的消息参见下表。 
服务|服务操作|操作语义|说明
---|---|---|---
Namf_Location|ProvidePositioningInfo|Request/Response|GMLC向AMF发起定位信息请求或获得定位信息响应。
EventNotify|Namf_Location|Subscribe/Notify|AMF向GMLC发送定位相关的事件通知消息。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.273|5G System (5GS) Location Services (LCS); Stage 2
3GPP|3GPP TS 29.515|5G System; Gateway Mobile Location Services; Stage 3
3GPP|3GPP TS 29.518|5G System; Access and Mobility Management Services; Stage 3
## ZUF-79-19-015 N17 
描述 :N17接口是AMF和5G-EIR之间的接口。通过N17接口，5G-EIR为AMF提供终端设备状态合法性检查服务。
实现原理 :涉及的网元 :涉及的NF参见[表1]。
NF|说明
---|---
AMF|AMF通过N17口向5G-EIR请求终端设备状态。
5G-EIR|5G-EIR通过N17口向AMF提供终端设备状态。
协议栈 :AMF与5G-EIR间的接口协议栈如[图1]所示。
图1  AMF与5G-EIR间的接口协议栈

消息描述 :AMF和5G-EIR通过服务操作的调用，实现消息交互。AMF和5G-EIR在N17接口提供的服务参见[表2]。
NF|服务|操作|操作语义|说明
---|---|---|---|---
5G-EIR|N5g-eir_EquipmentIdentityCheck|Get|Request/Response|AMF向5G-EIR发送终端设备状态请求，5G-EIR向AMF返回终端设备状态响应。
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP|3GPP TS 23.502|Procedures for the 5G System
3GPP|3GPP TS 29.511|Equipment Identity Register Services
# 缩略语 
# 缩略语 
AMF :Access and Mobility Management Function接入和移动管理功能
## EBI 
EPS Bearer IDEPS承载标识
EIR :Equipment Identity Register设备标识寄存器
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
## LMF 
Location Management Function定位管理功能
## LPP 
LTE Positioning ProtocolLTE定位协议
MME :Mobility Management Entity移动管理实体
NSSF :Network Slice Selection Function网络切片选择功能
PCF :Policy Control Function策略控制功能
SMF :Service Management Function业务管理功能
## SMSF 
Short Message Service Function短消息服务功能
TA :Tracking Area跟踪区域
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
# ZUF-79-20 漫游 
## ZUF-79-20-001 支持Home-Routed和Local-Breakout 
特性描述 :特性描述 :术语 :术语|含义
---|---
LBO|Local Break Out，一种漫游用户接入业务的方式：PDU Session的锚点SMF在VPLMN中。
HR|Home Routed，一种漫游用户接入业务的方式：PDU Session的锚点SMF在HPLMN中。
描述 :定义 :漫游，指移动终端用户移动到归属运营商网络以外的国家或地区仍能继续使用移动终端业务。漫游只能在网络制式兼容，且已经签署双边漫游协议的国家或地区的运营商网络之间进行。 
根据移动终端的漫游业务接入策略，可以分为两种漫游方式：Home routed、Local breakout。 
Home routed，指漫游用户通过归属网络的锚点SMF接入获取归属网络提供的业务。 
Local breakout，指漫游用户通过拜访网络的锚点SMF接入获取相应的业务。业务的提供者可以是归属网络，也可以是拜访网络。 
漫游方式选择，指AMF根据用户签约数据和双边漫游协议确定用户漫游方式。 
背景知识 :为实现用户在全球范围内不间断的互联互通，无缝为用户提供话音，数据及多媒体等在内的多种业务，漫游依然是5G网络部署和发展需要重点解决的问题。 
运营商通过提供漫游服务，能够为用户提供更大地理范围上的服务，增加自身网络的竞争力，提高用户对网络的满意程度，从而吸引更多的新用户，防止已有用户的流失。 
同时，可以通过为漫游伙伴的用户提供服务，来增加网络的收入。因此漫游服务具有很高的实用价值。 
应用场景 :从漫游方式看，场景包括如下几种： 
场景一： 漫游用户通过LBO方式访问业务 
场景二： 漫游用户通过HR方式访问归属地业务 
###### 场景一： 漫游用户通过LBO方式访问业务 
跨国运营或跨地区运营的运营商，用户从其一个运营地区移动到另一个运营地区；或同一地区，不同运营商合并后，用户从一个运营商运营的地区移动到另一个运营商运营的地区；或两个不同运营商具有很紧密的信任关系，签署的漫游协议允许用户使用LBO方式。 
###### 场景二： 漫游用户通过HR方式访问归属地业务 
用户从归属运营商运营的地区移动到其他地区的其他运营商时，签署的漫游协议允许用户使用HR方式。 
客户收益 :受益方|受益描述
---|---
运营商|提高运营成本效益：可以通过为漫游伙伴的用户提供服务，来增加网络的收入。提高用户满意度：能够为用户提供更大地理范围上的服务，增加自身网络的竞争力，提高用户对网络的满意程度，从而吸引更多的新用户，防止已有用户的流失。
移动用户|用户可以在更大地理范围上的使用服务，包括话音，数据及多媒体等在内的多种业务。
实现原理 :系统架构 :本特性涉及的系统架构包括LBO和HR对应的系统架构。 
LBO对应的系统架构如下图所示。 
图1  Local Breakout系统架构图

HR对应的系统架构如下图所示。 
图2  Home Routed系统架构图

涉及的网元 :NF名称|网元作用
---|---
UE|可以接入漫游网络
AMF|可以为漫入用户提供接入和移动性管理可以为漫入用户的PDU Session确定漫游接入方式
SMF|可以为漫入用户提供会话和业务接入可以为漫出用户提供会话和业务接入
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N11|ZUF-79-19-004 N11
本网元实现 :AMF支持两种漫游方式： 
Home-Routed 
Local-Breakout 
AMF可全局或基于SUPI号段设置LBO策略，LBO策略可以基于签约或基于本地策略限制使用LBO。 
业务流程 :对漫游用户的PDU Session，AMF按如下方式确定漫游方式。 
AMF根据S-NSSAI+APN，确定签约是否允许使用LBO，如果不允许，则直接确定使用HR。如果签约允许使用LBO，则根据本地策略进一步确认。 
AMF先基于SUPI号段，确定是否有匹配的记录。 
如果有匹配的记录，则判断配置的记录中是否允许使用LBO，如果不允许，则直接确定使用HR。如果配置的记录允许使用LBO，则返回允许使用LBO。 
如果根据SUPI没有匹配到记录，则使用全局配置判断是否允许使用LBO，如果不允许，则直接确定使用HR。如果全局配置中允许使用LBO，则返回允许使用LBO。 
如果按LBO方式确定PDU Session的漫游方式后，vSMF返回不支持LBO，则AMF再根据本地策略确定是转HR还是直接拒绝。 
系统影响 :若用户使用HR方式漫游时，对于AMF会需要选择vSMF和hSMF，比非漫游用户消耗的资源略多（预估单用户不超过5%）。 
考虑到漫游用户占比应该不大，因此对系统影响有限。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501-f50 System Architecture for the 5G System|全文
3GPP TS 23.502-f50 Procedures for the 5G System|全文
3GPP TS 23.503-f50 Policy and Charging Control Framework for the 5G System|全文
特性能力 :名称|指标|说明
---|---|---
支持的SUPI号段数|1024|最多可配置1024个SUPI号段
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.11|首次发布
License要求 :该特性为ZXUN uMAC的基本特性，无需License支持。 
对其他网元的要求 :UE|gNodeB|AMF|UDM|SMF
---|---|---|---|---
-|-|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
漫游策略配置|SET ROAMINGPOLICY
SHOW ROAMINGPOLICY|漫游策略配置
基于SUPI号段漫游策略配置|ADD SUPIROAMINGPOLICY
MOD SUPIROAMINGPOLICY|基于SUPI号段漫游策略配置
DEL SUPIROAMINGPOLICY|基于SUPI号段漫游策略配置
SHOW SUPIROAMINGPOLICY|基于SUPI号段漫游策略配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :为支持漫游相关的业务，需要进行漫游方式选择的配置。 
漫游策略配置：配置各种漫游参数，用于全局性的漫游方式选择和漫游流程处理。 
基于SUPI号段漫游策略配置：配置基于SUPI号段的漫游参数，这些参数影响某一SUPI号段用户的漫游方式选择和漫游流程处理。 
配置前提 :AMF/MME运行正常。 
EM网管能正常连接并登录。 
配置过程 :执行[SET ROAMINGPOLICY]命令，配置全局的漫游策略参数。
执行[ADD SUPIROAMINGPOLICY]命令，配置基于SUPI的漫游策略参数。
配置实例 :场景说明 :场景|场景描述|细节
---|---|---
场景1|Local breakout漫游接入|漫游用户通过拜访网络的锚点SMF接入获取相应的业务，签署的漫游协议允许用户使用LBO方式。
场景2|Home routed漫游接入|漫游用户通过归属网络的锚点SMF接入获取归属网络提供的业务，签署的漫游协议允许用户使用HR方式。
数据规划 :配置名称|参数项|取值
---|---|---
漫游策略配置|SUPI号段漫游策略|支持|不支持
额外的hSMF数量|漫游策略配置|【0,10】|【0,10】
默认LBO策略|漫游策略配置|限制|签约
默认hSMF查询方式|漫游策略配置|需要hNSSF返回NRF信息|不需hNSSF返回NRF信息
基于SUPI号段漫游策略配置|SUPI|长度为【1,16】的SUPI号段|长度为【1,16】的SUPI号段
LBO|基于SUPI号段漫游策略配置|限制|签约
hSMF查询方式|基于SUPI号段漫游策略配置|需要hNSSF返回NRF信息|不需hNSSF返回NRF信息
配置步骤 :序号|步骤|命令实例
---|---|---
1|LBO漫游接入|SET ROAMINGPOLICY:SUPIROAMINGPOLICY="SUPPORT"ADD SUPIROAMINGPOLICY:SUPI="46002",LBO="SUBSCRIBE",HSMFQUERYMODE="NOHNSSFRETURNNRF"
2|HR漫游接入|SET ROAMINGPOLICY:SUPIROAMINGPOLICY="SUPPORT"ADD SUPIROAMINGPOLICY:SUPI="46002",LBO="RESTRICT",HSMFQUERYMODE="NOHNSSFRETURNNRF"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|用户漫游注册
---|---
测试目的|漫游用户注册是否成功
预置条件|UE、NG-RAN、AMF各网元正常运营商间已经签约漫游协议，使用LBO方式当前DNN，S-NSSAI对应的签约支持LBOAMF本局配置的MCC为460，MNC为11
测试过程|PLMN为46002的用户发起普通注册流程
通过准则|用户注册成功
测试结果|–
测试项目|漫游用户以LBO方式建立PDU会话
---|---
测试目的|漫游用户以LBO方式建立PDU会话是否成功
预置条件|UE、NG-RAN、AMF各网元正常运营商间已经签约漫游协议，使用LBO方式当前DNN，S-NSSAI对应的签约支持LBOAMF本局配置的MCC为460，MNC为11“漫游策略配置”中”SUPI号段漫游策略“设置为”支持“”基于SUPI号段漫游策略配置“中配置的”supi“为46002，”LBO“为”签约“PLMN为46002的用户注册成功
测试过程|用户发起PDU会话建立
通过准则|用户在PDU建立过程中只选择V-SMF用户PDU会话建立成功
测试结果|–
测试项目|漫游用户以HR方式建立PDU会话
---|---
测试目的|漫游用户以HR方式建立PDU会话是否成功
预置条件|UE、NG-RAN、AMF各网元正常运营商间已经签约漫游协议，使用HR方式当前DNN，S-NSSAI对应的签约不支持LBO“漫游策略配置”中”SUPI号段漫游策略“设置为”支持“”基于SUPI号段漫游策略配置“中配置的”SUPI号段“为46002，”LBO“为”限制“PLMN为46002的用户注册成功
测试过程|用户发起PDU会话建立
通过准则|用户在PDU建立过程中先查询V-SMF，再查询H-SMF用户PDU会话建立成功
测试结果|–
常见问题处理 :无。 
## ZUF-79-20-002 I-SMF选择 
特性描述 :特性描述 :术语 :术语|含义
---|---
A-SMF|即Anchor SMF，锚定SMF。当单个SMF用于3GPP Rel-15中的非漫游和LBO场景时，Anchor SMF是服务PDU会话的SMF。因此，A-SMF用于控制锚定PDU会话的UPF，这个UPF在I-SMF插入前已分配。Anchor SMF连接PCC和UDM，执行UE IP地址分配等任务。
I-SMF|即Intermediate SMF。I-SMF用于控制具有N3接口且不被A-SMF控制的UPF。该UPF是一个在RAN和锚定PDU会话的UPF之间的intermediate UPF。I-SMF根据需要被插入、重定位或移除。
描述 :定义 :I-SMF选择是指UE在运营商网络下的大区间进行漫游时，在归属地大区和非归属地大区之间来回移动，5G网络执行I-SMF的插入、改变和删除。
当UE从归属地大区移出时，AMF选择并插入I-SMF；当UE从非归属地大区移动到其他非归属地大区时，AMF选择new I-SMF，I-SMF改变；当UE从非归属地大区移动回归属地大区时，AMF删除I-SMF。
背景知识 :国内运营商网络下，大区间漫游的需求是使用Local Break Out（拜访地直接接入）方式，产生的费用统一结算。用户在大区间漫游的过程中，需要保证业务连续性。 
EPC架构中，建立会话时必须既有PGW又有SGW（PGW/SGW可合一），其中：PGW是锚点，SGW随着UE位置的移动而变换，符合移动通信需求。
5GC架构中，PGW/SGW/MME的会话管理功能整合到了SMF中。如果UPF与基站之间全互联，则可以通过I-UPF的变换解决接入问题。但如果A-SMF管理的UPF无法与基站建立连接，则无法保证SSC mode1，即无法保证会话建立时作为PDU会话锚点的UPF在整个会话过程中保持不变。如[图1]所示：
UE从大区1移动到大区2，如果大区1中A-SMF管理的UPF无法与UE所在的基站建立连接，则A-SMF既无法选择，也无法连接能连接大区2的I-UPF。 
图1  大区间移动场景图

5GC架构中，用户在大区间漫游过程中，保证业务连续性时存在以下问题： 
由于每个A-SMF管理的UPF数量有限，UPF无法与全国基站都建立连接。 
使用ssc mode2/3时，网络侧通知UE重新建立会话，会导致会话不连续。 
目前AMF选择SMF的主要因素包括：S-NSSAI、DNN和PLMN，不考虑UE当前位置。 
因此，5GC架构中引入I-SMF，用于管理具有N3接口，且不被A-SMF控制的UE当前位置所在的UPF。这样可以使用户在跨大区移动时仍能保证ssc mode1业务连续性。该特性用于VONR等对连续性要求比较高的业务。 
应用场景 :该特性使用场景包括： 
非漫游场景下，用户非移动时I-SMF插入。 
非漫游场景下，用户移动时I-SMF插入、改变和删除。 
跨PLMN漫游Local Breakout场景下，用户非移动时I-SMF插入。 
跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除。 
###### 场景一：非漫游场景下，用户非移动时I-SMF插入 
非跨PLMN漫游场景下，UE没有移动，发起PDU会话建立请求，网络中A-SMF管理的UPF无法与UE所在的基站建立连接。运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service area，决策并执行I-SMF插入。
###### 场景二：非漫游场景下，用户移动时I-SMF插入、改变和删除 
非跨PLMN漫游场景下，UE已建立PDU会话，为了保证会话不中断，执行移动注册更新/业务请求/跨NG-RAN N2口切换/Xn切换等业务时，如果UE从A-SMF service area移动到new I-SMF service area，则AMF选择并插入I-SMF；如果UE从old I-SMF service area移动到new I-SMF service area，则I-SMF改变，AMF选择new I-SMF；如果UE从I-SMF service area移动回到A-SMF service area，则AMF删除I-SMF。 
###### 场景三：跨PLMN漫游Local Breakout场景下，用户非移动时I-SMF插入 
跨PLMN漫游Local Breakout场景下，UE没有移动，在VPLMN下发起PDU会话建立请求，网络中A-SMF管理的UPF无法与UE所在的基站建立连接。运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service area，决策并执行I-SMF插入。
###### 场景四：跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除 
跨PLMN漫游Local Breakout场景下，UE在VPLMN下已建立PDU会话，为了保证会话不中断，执行移动注册更新/业务请求/跨NG-RAN N2口切换/Xn切换等业务时，如果UE从A-SMF service area移动到new I-SMF service area，则AMF选择并插入I-SMF；如果UE从old I-SMF service area移动到new I-SMF service area，则I-SMF改变，AMF选择new I-SMF；如果UE从I-SMF service area移动回到A-SMF service area，则AMF删除I-SMF。 
客户收益 :受益方|受益描述
---|---
运营商|提高用户满意度：用户在大区间移动时，保证业务连续性，增加自身网络的竞争力，提高用户对网络的满意程度，从而吸引更多的新用户，防止已有用户的流失。
移动用户|用户在大区间无间断地使用数据、语音及多媒体等在内的多种业务，享受优质的网络服务。
实现原理 :系统架构 :本特性涉及的系统架构包括插入I-SMF的非漫游无数据分流、插入I-SMF的非漫游有数据分流、插入I-SMF的漫游LBO和漫游HR对应的系统架构。 
插入I-SMF的非漫游无数据分流对应的系统架构如[图2]所示。
图2  插入I-SMF的非漫游无数据分流对应的系统架构

N16a 是SMF与 I-SMF之间的接口。 
N38 是I-SMF之间的接口。 
此架构下，无数据分流。AMF根据当前位置选择I-SMF，和I-SMF交互完成业务流程。 
插入I-SMF的非漫游有数据分流对应的系统架构如[图3]所示。
图3  插入I-SMF的非漫游有数据分流对应的系统架构

此架构下，有数据分流。AMF根据当前位置选择I-SMF，和I-SMF交互完成业务流程。 
插入I-SMF的漫游LBO对应的系统架构如[图4]所示。
图4  插入I-SMF的漫游LBO对应的系统架构

Local Breakout漫游场景下，VPLMN下AMF根据当前位置选择I-SMF，和I-SMF交互完成业务流程。 
漫游HR对应的系统架构如[图5]所示。
图5  漫游HR对应的系统架构

漫游Home routed场景下，AMF使用V-SMF，需要输出计费接口。I-SMF无计费接口，UPF上报的计费信息需要透传给A-SMF统一计费。 
该场景下AMF选择V-SMF时，应以TA为主要考虑因素。 
该场景下叠加大区漫游时，I-SMF与V-SMF合一，无需单独的I-SMF。 
涉及的网元 :NF名称|NF作用
---|---
UE|可以通过NR接入网络。
AMF|可以决策I-SMF插入、改变和删除。可以选择I-SMF。可以与I-SMF交互，完成会话管理。
I-SMF|可以为大区漫入用户提供会话和业务接入。可以与A-SMF交互，完成会话和业务接入。
I-UPF|在RAN和锚定PDU会话的UPF之间的intermediate UPF，可以根据I-SMF指示建立用户面隧道。
NRF|负责I-SMF的地址解析。
协议栈 :接口|协议栈信息参考
---|---
N11|ZUF-79-19-004 N11
N14|ZUF-79-19-006 N14
Nnrf|ZUF-79-19-010 Nnrf
本网元实现 :UE在运营商网络下的大区间漫游，当UE从归属地大区移出时，AMF选择I-SMF，插入I-SMF；从非归属地大区移动到其他非归属地大区时，AMF选择new
I-SMF，I-SMF改变；从非归属地大区移动回归属地大区时，AMF删除I-SMF。涉及PDU会话创建、注册更新、业务请求、N2切换和Xn切换等业务流程。 
业务流程 :I-SMF选择，AMF涉及的业务流程如[表1]所示。
场景|业务流程
---|---
非漫游场景下，用户非移动时I-SMF插入|PDU会话创建时I-SMF插入
非漫游场景下，用户移动时I-SMF插入、改变和删除|注册更新时I-SMF插入、改变和删除
UE触发业务请求时I-SMF插入、改变和删除|非漫游场景下，用户移动时I-SMF插入、改变和删除
网络侧触发业务请求时I-SMF插入、改变和删除|非漫游场景下，用户移动时I-SMF插入、改变和删除
UE发生跨NG-RAN N2口切换时I-SMF插入、改变和删除|非漫游场景下，用户移动时I-SMF插入、改变和删除
UE发生Xn切换时I-SMF插入、改变和删除。|非漫游场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE空闲态从5G移动到4G时，I-SMF删除|非漫游场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE空闲态从4G移动到5G时，I-SMF插入|非漫游场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE从5G切换到4G时，I-SMF删除|非漫游场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE从4G移动到5G时，I-SMF插入|非漫游场景下，用户移动时I-SMF插入、改变和删除
无N26接口UE从4G移动到5G时，I-SMF插入|非漫游场景下，用户移动时I-SMF插入、改变和删除
跨PLMN漫游Local Breakout场景下，用户非移动时I-SMF插入|PDU会话创建时I-SMF插入
跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除|注册更新时I-SMF插入、改变和删除
UE触发业务请求时I-SMF插入、改变和删除|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
网络侧触发业务请求时I-SMF插入、改变和删除|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
UE发生跨NG-RAN N2口切换时I-SMF插入、改变和删除|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
UE发生Xn切换时I-SMF插入、改变和删除|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE空闲态从5G移动到4G时，I-SMF删除|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE空闲态从4G移动到5G时，I-SMF插入|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE从5G切换到4G时，I-SMF删除|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
有N26接口UE从4G移动到5G时，I-SMF插入|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
无N26接口UE从4G移动到5G时，I-SMF插入|跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
一、非漫游场景下，用户非移动时I-SMF插入
PDU会话创建时I-SMF插入图6  PDU会话创建时I-SMF插入

非漫游场景下，UE没有移动，发起PDU会话建立请求。 
网络中A-SMF管理的UPF无法与UE所在的基站建立连接，运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service
area，决策并执行I-SMF插入。AMF判断如果A-SMF的service area包括UE当前的TA，则同现有系统处理PDU Session
establishment流程；如果A-SMF的service area不包括UE当前的TA，则AMF根据如下参数选择一个I-SMF： 
S-NSSAI    
UE location (i.e. TA)，现阶段仅支持根据UE TA 
AMF发送Nsmf_PDUSession_CreateSMContext Request消息给I-SMF，携带A-SMF的smfUri（AMF构造的URI）、additionalSmfUri。 
I-SMF发送Nsmf_PDUSession_CreateSMContext Response消息给AMF。AMF收到响应消息后，在UE相应的会话上下文中保存I-SMF信息。 
I-SMF向A-SMF创建会话，如果smfUri指示的A-SMF没有响应，则I-SMF根据additionalSmfUri重选A-SMF。 
后续处理同现有系统处理。 
二、非漫游场景下，用户移动时I-SMF插入、改变和删除
注册更新时I-SMF插入、改变和删除非漫游场景下，UE已建立PDU会话，因移动注册更新时，AMF基于UE当前位置和SMF的service
area，决策并执行I-SMF插入、改变和删除。如[图7]所示。
图7  注册更新I-SMF插入、改变和删除

UE向(R)AN发起注册更新请求。 
RAN进行AMF选择。 
RAN给new AMF发送注册更新请求。 
new AMF向old AMF发送Namf_Communication_UEContextTransfer Request消息，请求UE上下文。 
old AMF向new AMF发送Namf_Communication_UEContextTransfer Response消息，如果有在I-SMF创建的PDU会话，则携带I-SMF的PduSessionContext，上下文中包含I-SMF
information（ismfId）和SMF information（hsmfId）。 
步骤6-9，同现有注册更新流程处理。 
步骤10，AMF决策是否需要执行I-SMF插入、改变和删除。AMF先检查从旧局获得的I-SMF/SMF，在本地是否存储有其service area。如果AMF没有I-SMF/SMF的service area，则需要用hsmfId/ismfId逐一查询NRF，分别获得I-SMF和SMF的service area信息；如果本地存储有I-SMF/SMF的service area，则直接进行决策。决策过程如下： 
如果Old AMF仅包含SMF信息，没有I-SMF信息，New AMF判断A-SMF的service area包括UE当前的TA，则不需要插入I-SMF。 
如果Old AMF包含了I-SMF信息和SMF信息，New AMF判断I-SMF的service area包括UE当前的TA，则继续使用该I-SMF。 
如果Old AMF包含了I-SMF信息和SMF信息，New AMF判断A-SMF的service area包括UE当前的TA，即UE移动到了A-SMF的service area，则触发I-SMF删除。 
如果Old AMF仅包含SMF信息，没有I-SMF信息，New AMF判断A-SMF的service area不包括UE当前的TA，则需要插入I-SMF。AMF先根据如下参数选择一个I-SMF：S-NSSAIUE location (i.e. TA，现阶段仅支持根据UE TA选择) 
如果Old AMF包含了I-SMF信息和SMF信息，New AMF判断A-SMF和I-SMF的service area都不包括UE当前的TA，同上选择一个新的I-SMF，触发I-SMF改变。 
New AMF向Old AMF发送Namf_Communication_RegistrationStatusUpdate消息，I-SMF改变或删除时携带smfChangeInfoList指示列表，Old AMF收到后记录I-SMF改变或删除指示。 
步骤11-16，同现有注册更新流程。 
步骤17，New AMF基于步骤10的I-SMF决策结果，执行I-SMF不变、插入、改变和删除处理。 
如果I-SMF不变，同现有系统处理注册更新，与SMF交互替换为与I-SMF交互。 
如果I-SMF插入，New AMF发送Nsmf_PDUSession_CreateSMContext给I-SMF，携带A-SMF的smContextRef，同业务请求流程中I-SMF插入处理。 
如果I-SMF改变，New AMF发送Nsmf_PDUSession_CreateSMContext给New I-SMF，携带Old I-SMF的smContextRef，同业务请求流程中I-SMF改变处理。 
如果I-SMF删除，New AMF发送Nsmf_PDUSession_CreateSMContext(smContextRef)给A-SMF，同业务请求流程中I-SMF删除处理。 
步骤17a-17b，Old AMF针对每个有I-SMF改变或删除的PDU会话，向Old I-SMF发送Nsmf_PDUSession_ReleaseSMContext Request消息，携带ismfReleaseOnly指示。Old I-SMF返回Nsmf_PDUSession_ReleaseSMContext Response消息。 
后续步骤同现有注册更新流程。 
UE触发业务请求时I-SMF插入、改变和删除图8  UE触发业务请求时I-SMF插入、改变和删除

UE发起业务请求，RAN向AMF发送业务请求。 
AMF决策I-SMF插入、改变和删除： 
无I-SMF，A-SMF的service area包括UE当前的TA，同现有系统处理业务请求。 
无I-SMF，A-SMF的service area不包括UE当前的TA，UE从A-SMF的service area移动到new
I-SMF的service area，AMF选择I-SMF，执行如下I-SMF插入处理。 
有I-SMF，I-SMF的service area包括UE当前的TA，I-SMF无改变，AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
Request，同现有系统处理业务请求，与SMF交互替换为与I-SMF交互。 
有I-SMF，I-SMF和A-SMF的service area不包括UE当前的TA，UE从old I-SMF的service
area移动到new I-SMF的service area，I-SMF改变，AMF选择new I-SMF，执行如下I-SMF改变处理。 
有I-SMF，A-SMF的service area包括UE当前的TA，UE从I-SMF的service area移动到A-SMF的service
area，AMF执行如下I-SMF删除处理。 
如果...|那么...
---|---
I-SMF插入处理|参见步骤3-步骤6，步骤8-步骤9，步骤17，步骤18-步骤21
I-SMF改变处理|参见步骤3-步骤9，步骤17，步骤17（I-SMF改变处理），步骤18-步骤21
I-SMF删除处理|参见步骤10-步骤16，步骤17（I-SMF删除处理），步骤22-步骤26
AMF选择一个new I-SMF，发送Nsmf_PDUSession_CreateSMContext
Request给new I-SMF，消息中携带A-SMF的smContextRef（携带之前A-SMF在创建会话响应中头部带回的smContextRef，包含IP地址），根据UE指示携带upCnxState（设置为“UP
activate”指示建立N3隧道用户面资源），其他字段同现有系统携带。 
new I-SMF向old-SMF获取SM Context；old-SMF响应，对于下行数据触发的业务请求，old SMF携带forwarding
indication指示需要一个前传隧道发送缓存的下行数据包。 
new I-SMF选择 I-UPF，建立N4 Session。 
建立N4 Session后，如果有
forwarding indication，new I-SMF为来自old I-UPF缓存的下行数据传输分配tunnel endpoints，或请求new
I-UPF分配这个tunnel endpoints。 
new I-SMF发送Nsmf_PDUSession_UpdateSMContext Request消息到old I-SMF，携带tunnel
endpoints for buffered DL data，建立前传隧道。old I-SMF发送N4 session modification消息到old
I-UPF，携带tunnel endpoints for buffered DL data。之后，old I-UPF开始发送缓存的下行数据给new
I-UPF。 
I-SMF插入时，I-SMF发送Nsmf_PDUSession_Create
Request消息到A-SMF，携带new I-UPF tunnel endpoint for buffered DL data，用于建立前传隧道。A-SMF发送N4
Session Modification到PSA UPF。I-SMF插入时，携带new I-UPF tunnel endpoint
for buffered DL data。之后，PSA UPF开始发送缓存的下行数据给new I-UPF。 
new I-SMF返回Nsmf_PDUSession_CreateSMContext
Response消息给AMF，携带N2 SM information (PDU Session ID, QFI(s), QoS profile(s),
CN N3 Tunnel Info, S-NSSAI, User Plane Security Enforcement, UE Integrity
Protection Maximum Data Rate), N1 SM Container, Cause)，其中CN N3 Tunnel
Info是new I-UPF的UL Tunnel信息，其他字段同现有系统携带。AMF收到后，在UE相应的会话上下文中保存N2 SM
information。 
如果UE从old I-SMF service
area移动到A-SMF service area，AMF发送Nsmf_PDUSession_CreateSMContext Request到A-SMF，消息中携带source
I-SMF的smContextRef（携带之前source I-SMF在创建会话响应中头部带回的smContextRef，包含IP地址），根据UE指示携带upCnxState（设置为“UP
activate”指示建立N3隧道用户面资源），其他字段同现有系统携带。 
A-SMF向old I-SMF获取SM Context，old I-SMF响应。对于下行数据触发的业务请求，old SMF携带
forwarding indication指示需要一个前传隧道发送缓存的下行数据包。 
如果A-SMF选择了一个new I-UPF，A-SMF发送N4 Session Establishment到这个new
I-UPF。 
如果有forwarding indication，A-SMF为来自old I-UPF缓存的下行数据传输分配tunnel
endpoints，或请求new I-UPF分配这个tunnel endpoints。 
如果PSA UPF可以服务UE当前的TA，A-SMF发送N4 Session Modification到PSA UPF。如果有forwarding
indication，A-SMF为来自old I-UPF缓存的下行数据传输分配tunnel endpoints或请求 PSA UPF分配这个tunnel
endpoints。A-SMF发送Nsmf_PDUSession_UpdateSMContext Request到old I-SMF，携带tunnel
endpoints for buffered DL data，建立前传隧道。old I-SMF发送N4 session modification到old
I-UPF，携带tunnel endpoints for buffered DL data to the old I-UPF。 
old I-UPF开始发送缓存的下行数据给new I-UPF或PSA UPF。 
A-SMF发送Nsmf_PDUSession_CreateSMContext
Response到AMF，携带N2 SM information，其中CN N3 Tunnel Info是new I-UPF的UL
Tunnel信息，其他字段同现有系统携带。 
AMF与RAN交互处理。 
I-SMF改变处理：步骤9成功响应，AMF发送Nsmf_PDUSession_ReleaseSMContext Request到old
I-SMF，携带ismfReleaseOnly，指示old I-SMF释放自身资源，不能触发A-SMF资源释放。old I-SMF返回Nsmf_PDUSession_ReleaseSMContext
response消息。 
I-SMF删除处理：步骤16成功响应，AMF发送Nsmf_PDUSession_ReleaseSMContext Request到old
I-SMF，携带I-SMF only indication，指示old I-SMF释放自身资源，不能触发SMF资源释放。old I-SMF返回Nsmf_PDUSession_ReleaseSMContext
response消息。 
AMF发送Nsmf_PDUSession_UpdateSMContext
Request消息到new I-SMF，如果AMF在[步骤17]收到一个或多个N2 SM information，则AMF前传N2 SM information到每PDU会话对应的new
I-SMF，其他字段同现有系统携带。
new I-SMF更新AN Tunnel Info和List of accepted QFI(s)到new I-UPF，下行数据从new
I-UPF传送到UE。 
new I-SMF更新SMF，A-SMF和PCF交互完成。 
new I-SMF发送Nsmf_PDUSession_UpdateSMContext
Response消息给AMF。 
AMF发送Nsmf_PDUSession_UpdateSMContext
Request消息到A-SMF，如果AMF在[步骤17]收到一个或多个N2 SM information，则AMF前传N2 SM information到每PDU会话对应的new
I-SMF，其他字段同现有系统携带。
A-SMF与PCF交互更新业务策略。 
如果A-SMF选择了一个new I-UPF，A-SMF更新AN Tunnel Info和List of accepted
QFI(s)到这个new I-UPF，否则更新到PSA UPF。 
A-SMF返回Nsmf_PDUSession_UpdateSMContext Response消息给AMF。 
new I-SMF/A-SMF根据定时器释放非直传数据前传隧道。old
I-SMF/A-SMF释放old I-UPF上的PDU会话。 
网络侧触发业务请求时I-SMF插入、改变和删除
网络侧触发业务请求I-SMF插入、改变和删除的处理同[图8]。
UE发生跨NG-RAN N2口切换时I-SMF插入、改变和删除
图9  Inter NG-RAN node N2 based handover, preparation phase, with
I-SMF insertion/change/removal

UE发生跨NG-RAN N2口切换，S-RAN向S-AMF发送Handover Required消息。S-AMF执行T-AMF选择后，向T-AMF发送Namf_Communication_CreateUEContext
Request消息，通过消息中的ueContext.sessionContextList.PduSessionContext携带hsmfId和ismfId。 
T-AMF决策Target I-SMF插入、改变和删除。T-AMF先检查从老局获得的I-SMF/SMF，在本地是否存储有其service
area。如果AMF没有I-SMF/SMF的service area，则需要逐一查询NRF（用hsmfId/ismfId查询NRF），分别获得I-SMF和SMF的service
area信息；如果本地存储有I-SMF/SMF的service area，则直接进行决策。决策过程如下： 
无I-SMF，A-SMF的service area包括UE当前的TA，同现有系统处理N2切换。 
无I-SMF，A-SMF的service area不包括UE当前的TA，UE从A-SMF的service area移动到new
I-SMF的service area，AMF选择Target I-SMF，执行如下I-SMF插入处理。 
有I-SMF，I-SMF的service area包括UE当前的TA，I-SMF无改变，同现有系统处理N2切换，与SMF交互替换为与I-SMF交互。 
有I-SMF，I-SMF和SMF的service area不包括UE当前的TA，UE从old I-SMF的service
area移动到new I-SMF的service area，I-SMF改变，AMF选择Target I-SMF，执行如下I-SMF改变处理。 
有I-SMF，A-SMF的service area包括UE当前的TA，UE从I-SMF的service area移动到A-SMF的service
area，AMF执行如下I-SMF删除处理。 
如果...|那么...
---|---
I-SMF插入处理|参见步骤3，步骤5-步骤8，步骤14-步骤19，步骤23，步骤31
I-SMF改变处理|参见步骤3-步骤4，步骤6-步骤8，步骤14-步骤16，步骤20-步骤22，步骤31
I-SMF删除处理|参见步骤9-步骤13，步骤24-步骤31
T-AMF对要切换的PDU会话，选择一个Target
I-SMF，发送Nsmf_PDUSession_CreateSMContext消息给Target I-SMF，I-SMF插入时携带A-SMF的smContextRef（携带之前A-SMF在创建会话响应中头部带回的smContextRef，并增加IP地址构造完整的URI），n2SmInfo，targetId，hostate为"PREPARING"，其他字段同现有系统处理。 
Target I-SMF发送Nsmf_PDUSession_Context
Request，向Source I-SMF获取上下文信息。 
Target I-SMF发送Nsmf_PDUSession_Context
Request，向A-SMF获取上下文信息。UPF分配CN Tunnel Info。 
Target I-SMF选择一个Target
I-UPF。 
Target I-SMF/Target I-UPF分配CN Tunnel Info。 
Target I-SMF发送Nsmf_PDUSession_CreateSMContext
Response给T-AMF，携带PDU Session ID, N2 SM Information, Reason for non-acceptance，其他字段同现有系统处理。Target
I-SMF接受PDU会话的N2切换，N2 SM Information包含N3 UP地址和UPF的UL CN Tunnel ID 和QoS参数。 
T-AMF发送Nsmf_PDUSession_CreateSMContext给A-SMF，携带source
I-SMF的smContextRef（携带之前source I-SMF在创建会话响应中头部带回的smContextRef，并增加IP地址构造完整的URI），targetId，hostate为"PREPARING"，其他字段同现有系统处理。 
A-SMF选择一个Target I-UPF。 
A-SMF/PSA UPF分配ULCN Tunnel Info (i.e. N3 tunnel info)。 
如果A-SMF选择了一个Target I-UPF，Target I-UPF分配CN Tunnel Info。 
A-SMF发送Nsmf_PDUSession_CreateSMContext
Response给T-AMF，携带PDU Session ID, N2 SM Information, Reason for non-acceptance，其他字段同现有系统处理。Target
I-SMF接受PDU会话的N2切换，N2 SM Information包含N3 UP地址和UPF的UL CN Tunnel ID 和QoS参数。 
T-AMF和RAN交互（Handover
Request/ACK）。 
T-AMF发送Nsmf_PDUSession_UpdateSMContext Request给Target I-SMF，携带PDU
Session ID, N2 SM response received from T-RAN（N3 tunnel info of T-RAN）。 
Target I-SMF指示Target
I-UPF分配DL forwarding tunnel(s) for indirect forwarding，也可以选择另外一个UPF做indirect
forwarding。Target I-UPF分配N9 Tunnel identifiers for forwarding data。 
Target I-SMF发送Nsmf_PDUSession_UpdateSMContext Request给Source
I-SMF，建立indirect forwarding tunnel。 
source I-SMF指示source I-UPF分配DL forwarding tunnel。 
Source I-SMF响应Target
I-SMF。 
Target I-SMF发送Nsmf_PDU
Session_UpdateSMContext给A-SMF，建立indirect forwarding tunnel。 
A-SMF指示PSA UPF分配DL forwarding tunnel。 
A-SMF响应Target I-SMF。 
Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
Response给T-AMF，携带N2 SM Information，此信息中包含了通过Target AMF->Source AMF发送给S-RAN的DL
forwarding Tunnel Info，其他字段同现有系统处理。 
T-AMF发送Nsmf_PDUSession_UpdateSMContext
Request给A-SMF，携带PDU Session ID, N2 SM response received from T-RAN。 
Target I-UPF没有被选择，A-SMF通知UPF分配DL forwarding tunnel。 
Target I-UPF被选择，A-SMF通知I-UPF分配DL forwarding tunnel。 
A-SMF发送Nsmf_PDUSession_UpdateSMContext，通知 Source I-SMF建立indirect
forwarding tunnel。 
Source I-SMF通知Source I-UPF建立indirect forwarding tunnel。 
source I-SMF响应A-SMF。 
A-SMF返回Nsmf_PDUSession_UpdateSMContext Response给T-AMF，携带N2
SM Information，此信息中包含了通过Target AMF->Source AMF发送给S-RAN的DL forwarding
Tunnel Info。 
T-AMF向S-AMF返回Namf_Communication_CreateUEContext
Response消息，同现有系统处理。 
图10  Inter NG-RAN node N2 based handover, execution phase, with
I-SMF insertion/change/removal

原N2切换流程步骤1-6中，步骤6a T-AMF发送Namf_Communication_N2InfoNotify给S-AMF，I-SMF改变或删除时携带smfChangeInd指示。 
如果...|那么...
---|---
I-SMF插入处理|参见步骤2，步骤5-步骤9，步骤15-步骤16，步骤18
I-SMF改变处理|参见步骤2-步骤9，步骤15-步骤17
I-SMF删除处理|参见步骤10-步骤15，步骤19-步骤20
T-AMF发送Nsmf_PDUSession_UpdateSMContext
Request消息给Target I-SMF，N2切换成功时，每PDU会话携带HoState，其他字段同现有系统处理。 
S-AMF发送Nsmf_PDUSession_ReleaseSMContext Request消息给source I-SMF。携带ismfReleaseOnly指示（设置为1），用于source
I-SMF不释放SMF的资源。携带hoCompleteIndication指示，其他字段同现有系统处理。source I-SMF启动定时器释放相应PDU会话的SM
Context。 
source I-SMF发送Nsmf_PDUSession_ReleaseSMContext Response消息给S-AMF。 
Target I-SMF向Target
I-UPF指示T-RAN的DL AN Tunnel Info。 
Target I-SMF更新A-SMF。 
A-SMF向PSA UPF提供Target I-UPF的DL CN Tunnel Info。 
A-SMF响应Target I-SMF。 
Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
Response消息给T-AMF，同现有系统处理。 
T-AMF发送 Nsmf_PDUSession_UpdateSMContext
Request消息给SMF，N2切换成功时，每PDU会话携带HoState，其他字段同现有系统处理。 
S-AMF发送Nsmf_PDUSession_ReleaseSMContext Request消息给source I-SMF，携带ismfReleaseOnly指示（设置为1），用于source
I-SMF不释放SMF的资源；携带hoCompleteIndication指示。source I-SMF启动定时器释放相应PDU会话的SM
Context。source I-SMF发送Nsmf_PDUSession_ReleaseSMContext Response消息给S-AMF。 
A-SMF向Target I-UPF指示T-RAN的DL AN Tunnel Info。 
A-SMF向PSA UPF指示T-RAN的DL AN Tunnel Info和Target I-UPF的DL CN Tunnel
Info。 
A-SMF发送Nsmf_PDUSession_UpdateSMContext Response消息给T-AMF。 
T-AMF同现有系统处理注册更新。S-AMF同现有系统释放S-RAN的UE
Context。 
Target I-SMF向Target
I-UPF释放Target I-UPF上的非直传数据转发资源。 
Source I-SMF通知Source
I-UPF释放Source I-UPF上的非直传数据转发资源。 
SMF通知PSA UPF释放:UPF（PSA）上的非直传数据转发资源，释放N3
Tunnel。 
Source I-SMF通知Source
I-UPF释放PDU会话，释放Source I-UPF上的非直传数据转发资源。 
A-SMF通知PSA UPF释放UPF（PSA）上的非直传数据转发资源，释放N3
Tunnel。 
UE发生Xn切换时I-SMF插入、改变和删除
I-SMF插入
图11  Xn based inter NG-RAN handover with insertion of intermediate
SMF

目标RAN向AMF发起N2 Path Switch Request请求。 
对要切换的每个PDU会话，AMF判断当前无I-SMF，A-SMF的service area不包括UE当前的TA，UE从A-SMF的service
area移动到new I-SMF的service area，则AMF决策插入I-SMF，对每个N2 Path Switch Request拒绝的PDU会话，AMF发送Nsmf_PDUSession_UpdateSMContext
Request消息给A-SMF。 
AMF选择I-SMF，执行I-SMF插入处理。AMF发送Nsmf_PDUSession_CreateSMContext
Request消息给I-SMF，携带A-SMF的smContextRef（携带之前A-SMF在创建会话响应中头部带回的smContextRef，包含IP地址），n2SmInfo，其他字段同现有系统处理。 
new I-SMF向A-SMF获取SM context。 
I-SMF通知I-UPF UL CN
Tunnel Info of PSA UPF，I-SMF/PSA UPF分配UL and DL CN Tunnel Info，建立会话。 
I-SMF请求A-SMF创建会话。 
A-SMF向PSA UPF发送 DL
CN Tunnel Info of the I-UPF通知。 
UPF（PDU Session Anchor）向源RAN发送一个或多个“N3
End Marker”数据包，源NG-RAN转发 “N3 End Marker数据包到目标RAN。 
A-SMF返回创建会话响应给I-SMF。 
I-SMF发送Nsmf_PDUSession_CreateSMContext Response消息给AMF，携带 I-UPF的UL
CN Tunnel Info，其他字段同现有系统处理。 
后续流程同原有系统。 
I-SMF改变
图12  Xn based inter NG-RAN handover with intermediate I-SMF re-allocation

目标RAN向AMF发起N2 Path Switch Request请求。 
对要切换的每个PDU会话，AMF判断source I-SMF的service area不包括UE当前的TA，UE从source
I-SMF的service area移动到new I-SMF的service area，则AMF决策I-SMF改变，对每个N2 Path
Switch Request拒绝的PDU会话，AMF发送Nsmf_PDUSession_UpdateSMContext Request给source
I-SMF，source I-SMF发送Nsmf_PDUSession_Update Request给A-SMF。 
有如下两种情况。 
AMF发送Nsmf_PDUSession_CreateSMContext Request消息给target I-SMF，携带source
I-SMF的smContextRef（携带之前source I-SMF在创建会话响应中头部带回的smContextRef，包含IP地址），n2SmInfo，其他字段同现有系统处理。 
AMF选择I-SMF，执行I-SMF改变处理。 
Target I-SMF发送Nsmf_PDUSession_Context Request消息给Source I-SMF，获取SM
Context。 
同[步骤5]。
Target I-SMF更新A-SMF。 
同[步骤7]。
同[步骤8]。
A-SMF向Target I-SMF返回更新响应。 
I-SMF发送Nsmf_PDUSession_CreateSMContext Response消息给AMF，携带UL
CN Tunnel Info of the I-UPF，其他字段同现有系统处理。 
AMF给RAN返回切换响应。 
AMF发送Nsmf_PDUSession_ReleaseSMContextRequest消息给source I-SMF，携带I-smfReleaseOnly指示（设置为1），用于source
I-SMF仅释放自身资源，不释放A-SMF的资源。source I-SMF通知source I-UPF释放，其他字段同现有系统处理。 
后续流程同原有系统处理。 
I-SMF删除
图13  Xn based inter NG-RAN handover with removal of intermediate
SMF

目标RAN向AMF发起N2 Path Switch Request请求。 
对要切换的每个PDU会话，AMF判断source I-SMF的service area不包括UE当前的TA，UE从source
I-SMF的service area移动到A-SMF的service area，AMF决策I-SMF删除，对每个N2 Path Switch
Request拒绝的PDU会话，AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给source
I-SMF。 
AMF执行I-SMF删除处理。AMF发送Nsmf_PDUSession_CreateSMContext Request消息给A-SMF，携带source
I-SMF的smContextRef（携带之前source I-SMF在创建会话响应中头部带回的smContextRef，包含IP地址），n2SmInfo，其他字段同现有系统处理。 
A-SMF选择一个I-UPF创建会话，携带target NG-RAN Tunnel Info，A-SMF/I-UPF分配CN
Tunnel Info。 
A-SMF通知PSA UPF修改会话，携带I-UPF的DL CN Tunnel Info。 
A-SMF通知I-UPF修改会话，携带UPF(PSA)的UL CN Tunnel Info。 
UPF（PDU Session Anchor）向源RAN发送一个或多个“N3 End Marker”数据包，源NG-RAN转发
“N3 End Marker数据包到目标RAN。 
A-SMF发送Nsmf_PDUSession_CreateSMContext Response给AMF，携带I-UPF的UL
CN Tunnel Info，其他字段同现有系统处理。 
AMF给RAN返回切换响应。 
AMF发送Nsmf_PDUSession_ReleaseSMContext request消息给source I-SMF，携带ismfReleaseOnly指示（设置为1），用于source
I-SMF仅释放自身资源，不释放A-SMF的资源。source I-SMF通知source I-UPF释放。Source I-SMF发送Nsmf_PDUSession_ReleaseSMContext
Response响应给AMF。 
后续流程同原有系统处理。 
有N26接口UE空闲态从5G移动到4G时，I-SMF删除
图14  5GS to EPS Idle mode mobility using N26 interface

UE在空闲态从5G移动到4G，发起TAU请求。 
eNodeB将TAU请求转发给RAN。 
RAN将TAU请求转发给MME。 
MME向AMF发送Context Request消息。 
AMF发送Nsmf_PDUSession_ContextRequest消息给I-SMF，获取UE EPS PDN Connection。I-SMF返回响应。 
步骤6-15，同现有系统处理。 
步骤15b-15c，AMF设置的资源保护定时器超时，发送Nsmf_PDUSession_ReleaseSMContext
Request消息给I-SMF，携带ismfReleaseOnly，指示old I-SMF释放自身资源，不能触发A-SMF资源释放。I-SMF触发I-UPF释放PDU会话。I-SMF返回Nsmf_PDUSession_ReleaseSMContext
response消息给AMF。 
步骤16-19，同现有系统处理。 
有N26接口UE空闲态从4G移动到5G时，I-SMF插入
有N26接口UE空闲态从4G移动到5G时，I-SMF插入如[图15]所示。
图15  
EPS to 5GS mobility for single-registration mode with N26
interface

步骤1-14，UE在空闲态从4G移动到5G，发起注册请求。同现有系统处理。 
步骤14a，AMF根据PGW-C+SMF FQDN到NRF发现获得Service Area，判断UE当前所在的TA是否在PGW-C+SMF的Service Area。 
如果当前TA在PGW-C+SMF的Service Area，则不需要插入I-SMF，同现有系统处理。 
如果当前TA不在PGW-C+SMF的Service Area，则需要插入I-SMF，AMF选择到I-SMF，发送Nsmf_PDUSession_CreateSMContext
Request给I-SMF，消息中携带PGW-C+SMF的smfUri（AMF构造的URI）（smContextRef不携带，获取不到），pduSessionId，ueEpsPdnConnection，epsInterworkingInd，配置的interworking
snssai，其他字段同现有系统携带。 
步骤14b-14c，I-SMF执行与PGW-C+SMF、UPF的交互，为PDU会话建立CN隧道。 
步骤14f，I-SMF向AMF返回Nsmf_PDUSession_CreateSMContext Response消息，携带PDU
Session ID, S-NSSAI, N2 SM information。 
步骤15-16，HSS+UDM向MME发送Cancel Location，MME回复Cancel Location Ack，向SGW发送Delete
Session Request消息通知SGW释放。 
步骤17，AMF向UE发送Registration Accept消息，如果New AMF为UE分配了新的5G-GUTI，则需要在本消息中携带。 
步骤18，如果AMF为UE分配了新的5G-GUTI，则UE向New AMF发送Registration Complete消息。 
有N26接口UE从5G移动到4G时，I-SMF删除
有N26接口UE从5G切换到4G时，I-SMF删除的流程如[图16]所示。
图16  5GS to EPS handover for single-registration mode with N26 interface

UE在连接态从5G切换到4G，NG-RAN向AMF发送Handover Required消息。 
步骤2，AMF向I-SMF发送Nsmf_PDUSession_ContextRequest消息，获取UE EPS PDN Connection。I-SMF向PGW-C获取PDU会话信息，返回给AMF。 
步骤3-10，同ZUF-79-12-001 支持N26接口互操作
“5G到4G的切换（N26）”流程中的步骤3-9。
步骤11，AMF发送Handover Command消息给Source NR。Source NR发送Handover Command消息给UE，通知UE切换到目标接入网络。UE删除没有分配EBI的PDU Session和QoS flow。 
步骤12，UE切换到目标小区，给eNodeB发送Handover Complete消息。eNodeB给MME发送Handover Notify消息。 MME通知AMF切换完成。 AMF设置定时器用于监测NG-RAN和PGW-C+SMF的资源释放，给MME返回切换完成确认消息。 
步骤13-17，MME给SGW发送Modify Bearer Request消息，通知eNodeB用户面隧道等信息。SGW给PGW-C+SMF发送Modify Bearer Request消息，PGW-C+SMF删除没有缺省QoS flow和没有EBI的PDU Session。PGW-C+SMF向UPF+PGW-U触发N4 Session Modification过程，更新用户面路径。PGW-C+SMF向SGW返回Modify Bearer Response消息。SGW向MME返回Modify Bearer Response消息。 
步骤18，UE发起TAU流程。在该流程中，AMF可以通知UDM去订阅，释放AMF和NR的相关资源。 
如果AMF在步骤18触发的TAU流程中收到UDM的去注册通知消息，或者在步骤12中设置的资源保护定时器超时，则发送Nsmf_PDUSession_ReleaseSMContext Request消息给I-SMF，携带ismfReleaseOnly，指示Old I-SMF释放自身资源，不能触发A-SMF资源释放。I-SMF触发I-UPF释放PDU会话。I-SMF返回Nsmf_PDUSession_ReleaseSMContext response消息给AMF。 
步骤19，对于non-GBR的QoS Flow，PGW-C+SMF可以发起专有承载建立流程。 
步骤20，如果MME设置的资源保护监测定时器超时，且建立了非直接数据前转隧道，则MME通知SGW释放非直接数据前转隧道资源。 
步骤21，如果资源保护监测定时器超时，且建立了非直接数据前转隧道，则释放非直接数据前转隧道资源 
21a，如果I-SMF在步骤12e设置的资源保护定时器超时，I-SMF释放非直接数据前转隧道资源。 
21b，如果PGW-C+SMF在步骤16设置的资源保护定时器超时，则向PGW-U+UPF发送N4会话修改请求，释放非直接数据前转隧道资源。 
21c，AMF在步骤12d设置的资源保护定时器超时，向NG-RAN发送UE Context Release Command消息释放资源。 
有N26接口UE从4G切换到5G时，I-SMF插入
有N26接口UE从4G切换到5G时，I-SMF插入的流程如[图17]所示。
图17  EPS to 5GS handover using N26 interface, preparation phase

步骤1-3，UE在连接态从4G切换到5G，eNB向MME发送Handover Required消息，MME根据Target ID确定是到NR的切换，选择一个AMF，向AMF发送Forward Relocation Request消息。 
步骤4，AMF根据PGW-C+SMF FQDN到NRF发现获得Service Area，判断UE当前所在的TA是否在PGW-C+SMF的service area。 
如果当前TA在PGW-C+SMF的service area，则不需要插入I-SMF，发送Nsmf_PDUSession_CreateSMContext Request给PGW-C+SMF。 
如果当前TA不在PGW-C+SMF的service area，则需要插入I-SMF，AMF选择到I-SMF，发送Nsmf_PDUSession_CreateSMContext Request给I-SMF，消息中携带PGW-C+SMF的smfUri（AMF构造的URI）、ueEpsPdnConnection、配置的interworking S-NSSAI、hoState为"PREPARING"、targetId，其他字段同现有4G切换到5G流程。 
步骤5-6，I-SMF通知PGW-C+SMF，如果动态PCC被部署，则PGW-C+SMF可以向PCF+PCRF触发SMF发起的SM策略修改。PGW-C+SMF可以向PGW-U+UPF发送N4会话修改。 
步骤7，PGW-C+SMF通过I-SMF向AMF返回Nsmf_PDUSession_CreateSMContext Response消息，携带PDU Session ID, S-NSSAI, N2 SM information。 
步骤8，I-SMF向I-UPF发起N4 Session Establishment流程，I-UPF返回响应。 
步骤9-10，AMF发送Handover Request消息给NR。NR返回Handover Request Acknowledge消息给AMF。 
步骤11，AMF发送Nsmf_PDUSession_UpdateSMContext Request消息给I-SMF，携带PDU Session ID, N2 SM information，hoState为"PREPARED" 等信息。 
步骤12，I-SMF通知PGW-C+SMF，PGW-C+SMF向PGW-U+UPF指示NR的N3 UP address和Tunnel ID等信息。 
步骤13，PGW-C+SMF通过I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext Response消息，携带PDU Session ID, EPS Bearer Setup List, CN tunnel information for data forwarding等信息。 
步骤14， AMF给MME返回Forward Relocation Response消息。 
步骤15，如果非直接数据前转隧道被使用，则MME向SGW创建非直接数据前转隧道。 
图18  EPS to 5GS handover using N26 interface, execution phase

步骤1-6，同“ZUF-79-12-001 支持N26接口互操作
“4G到5G的切换（N26）”执行阶段流程中的步骤1-6。
步骤7，AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext Request 消息，携带Handover Complete indication for PDU Session ID等信息。 
步骤8-9，I-SMF通知PGW-C+SMF，PGW-C+SMF向PGW-U+UPF发起N4会话修改，指示用户面路径已切换到NR。如果PCC被部署，则PGW-C+SMF通知PCF+PCRF信息改变，如RAT Type和UE Location等信息。 
步骤10，PGW-C+SMF通过I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext Response消息，携带PDU Session ID等信息。 
步骤11，I-SMF向I-UPF提供N3下行AN隧道信息。 
步骤12，UE完成切换后注册过程。 
步骤13，MME释放源侧资源。 
无N26接口UE从4G移动到5G时，I-SMF插入
无N26接口UE从4G移动到5G时，I-SMF插入的流程如[图19]所示。
图19  无N26接口UE从4G移动到5G时，I-SMF插入的流程

流程说明如下： 
0. UE在EPC附着。 
1. UE检测到需从4G移动到5G，发起注册流程，发送Registration Request消息，携带Registration type( set to "mobility registration update")、5G-GUTI(mapped from the 4G-GUTI)、native 5G-GUTI (if available) as an Additional GUTI等信息。UE指示从EPC移动到5GC。 
2. NR选择一个合适的AMF。 
3. NR发送Registration Request消息给AMF。如果Registration type为"mobility registration update"，UE指示从EPC移动到5GC，AMF支持5GS-EPS interworking procedure without N26 interface，则AMF把看看做 "initial Registration"，不做PDU Session状态同步。 
4. AMF根据5G-GUTI 查找不到UE的MM上下文等信息，发起向UE获取SUCI过程。 
5. AMF完成对UE的安全过程。 
6. AMF完成对UE的Equipment ID检查过程。 
7. AMF完成向UDM+HSS的注册过程。若UE从EPC移入且AMF支持无N26互操作，则携带UE已注册MME指示；若HSS+UDM支持同时在AMF和MME注册，则不会发送注销通知给MME，且在注册响应中携带支持UE在AMF和MME同时注册指示。HSS+UDM如果保存了PGW-C+SMF FQDN，则会返回给AMF。 
8. 如果需向PCF建立AM Policy Association，则AMF向PCF发起AM Policy Association建立过程。 
9. AMF通知SMF更新信息。 
10. AMF向UE发送Registration Accept消息，携带5G-GUTI、TA List等信息。如果HSS+UDM指示支持UE在AMF和MME同时注册，则AMF在Registration Accept消息中携带interworking without N26指示给UE。 
11. UE向AMF返回Registration Complete消息。 
12. UE移动到5G后，如果UE想把4G中的PDN连接切换到5GS中，则发起UE requested PDU Session Establishment 流程。执行I-SMF插入过程，如[图20]所示。
13. PGW-C+SMF完成EPC中PDN连接资源的释放。 
I-SMF插入过程如[图20]所示。
图20  I-SMF插入过程

流程说明： 
AMF基于UE当前位置和PGW-C+SMF的service area，决策并执行I-SMF插入。 
AMF发送Nsmf_PDUSession_CreateSMContext Request消息给I-SMF，携带PGW-C+SMF的smfUri（AMF构造的URI）。 
I-SMF发送Nsmf_PDUSession_CreateSMContext Response消息给AMF。AMF收到响应消息后，在UE相应的会话上下文中保存I-SMF信息。 
I-SMF向PGW-C+SMF创建会话，如果smfUri指示的PGW-C+SMF没有响应，则I-SMF根据additionalSmfUri重选PGW-C+SMF。 
后续处理同现有系统处理。 
跨PLMN漫游Local Breakout场景下，用户非移动时I-SMF插入
PDU会话创建时I-SMF插入，同[图6]。
跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除
漫游LBO场景下，UE选择VPLMN的SMF作为A-SMF，DNN
OI设置为VPLMN进行A-SMF选择。I-SMF的选择和处理，同[非漫游场景下，用户移动时I-SMF插入、改变和删除]。
系统影响 :移动性流程业务请求、切换和注册更新，省间/跨大区增加了I-SMF到NRF发现的流程。这几个流程中业务请求话务模型最高，对系统性能有一定影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :相关特性|交互关系
---|---
ZUF-79-13-005 紧急业务|紧急PDU会话遵从本特性I-SMF的处理原则。
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501 System Architecture for the 5G System|5.34.3 I-SMF selection
3GPP TS 23.502 Procedures for the 5G System|4.23 Support of deployments topologies with specific SMF Service Areas4.26.5.2 I-SMF Context Transfer procedure
3GPP TS 29.502 Session Management Services|5.2.2 Service Operations6.1 Nsmf_PDUSession Service API
3GPP TS 29.510 Network Function Repository Services|6.2.3.2.3 Resource Standard Methods6.2.6 Data Model6.2.9 Features supported by the NFDiscovery service
3GPP TS 29.518 Access and Mobility Management Services|6.1.6.2 Structured data types
特性能力 :名称|指标
---|---
基于TA的SMF本地地址解析|AMF最大支持4096个TA配置
SMF管理区域配置|AMF最大支持1024个SMF实例
跟踪区组配置|AMF最大支持65535个跟踪区组
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.21|首次发布。
License要求 :该特性需要申请License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为AMF支持I-SMF，此项目显示为“支持”，表示uMAC AMF支持I-SMF功能。
对其他网元的要求 :UE|I-SMF/SMF|I-UPF/UPF|NRF|
---|---|---|---|---
-|√|√|√|
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :如果现网NRF不可用或没有部署，则需要启动本地I-SMF地址解析，现网SMF的服务区域在AMF进行本地配置。 
O&M相关 :命令 :配置项表2  新增配置项配置项命令I-SMF策略配置SET AMFSUPPORTISMFSHOW AMFSUPPORTISMFA-SMF选择策略配置SET ASMFSELPOLICYSHOW ASMFSELPOLICY解析SMF策略配置SET RESOLVESMFPOLICYSHOW RESOLVESMFPOLICYSMF地址池配置ADD SMFIPPOOLCFGDEL SMFIPPOOLCFGSHOW SMFIPPOOLCFGSMF服务区域配置ADD SMFSERVAREACFGSET SMFSERVAREACFGDEL SMFSERVAREACFGSHOW SMFSERVAREACFG表3  修改配置项配置项命令新增参数跟踪区组配置ADD TAGROUPCFG"跟踪区组类型" 取值范围：通用类型、SMF服务区、业务区域限制、IP位置关联、切片可用性"跟踪区别名"发现SMF参数配置SET NRFDISCSMFPARACFG"携带Preferred-TAI" 0：不携带 1：携带 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软件参数的变化。 
动态管理动态管理命令查询用户信息SHOW USER INFORMATION 
性能统计 :编号|性能计数器名称
---|---
1|C510020046 AMF内移动性注册I-SMF插入请求次数
2|C510020047 AMF内移动性注册I-SMF插入成功次数
3|C510020048 AMF内移动性注册I-SMF不变请求次数
4|C510020049 AMF内移动性注册I-SMF不变成功次数
5|C510020050 AMF内移动性注册I-SMF改变请求次数
6|C510020051 AMF内移动性注册I-SMF改变成功次数
7|C510020052 AMF内移动性注册I-SMF删除请求次数
8|C510020053 AMF内移动性注册I-SMF删除成功次数
9|C510020054 AMF间移动性注册I-SMF插入请求次数
10|C510020055 AMF间移动性注册I-SMF插入成功次数
11|C510020056 AMF间移动性注册I-SMF不变请求次数
12|C510020057 AMF间移动性注册I-SMF不变成功次数
13|C510020058 AMF间移动性注册I-SMF改变请求次数
14|C510020059 AMF间移动性注册I-SMF改变成功次数
15|C510020060 AMF间移动性注册I-SMF删除请求次数
16|C510020061 AMF间移动性注册I-SMF删除成功次数
17|C510020062 N26口的互操作流程注册I-SMF插入请求次数
18|C510020063 N26口的互操作流程注册I-SMF插入成功次数
19|C510040055 数据触发业务请求I-SMF插入尝试次数
20|C510040056 数据触发业务请求I-SMF插入成功次数
21|C510040057 数据触发业务请求I-SMF不变尝试次数
22|C510040058 数据触发业务请求I-SMF不变成功次数
23|C510040059 数据触发业务请求I-SMF改变尝试次数
24|C510040060 数据触发业务请求I-SMF改变成功次数
25|C510040061 数据触发业务请求I-SMF删除尝试次数
26|C510040062 数据触发业务请求I-SMF删除成功次数
27|C510040063 寻呼触发业务请求I-SMF插入尝试次数
28|C510040064 寻呼触发业务请求I-SMF插入成功次数
29|C510040065 寻呼触发业务请求I-SMF不变尝试次数
30|C510040066 寻呼触发业务请求I-SMF不变成功次数
31|C510040067 寻呼触发业务请求I-SMF改变尝试次数
32|C510040068 寻呼触发业务请求I-SMF改变成功次数
33|C510040069 寻呼触发业务请求I-SMF删除尝试次数
34|C510040070 寻呼触发业务请求I-SMF删除成功次数
35|C510050013 基于Xn接口Path Switch(I-SMF插入)请求次数
36|C510050014 基于Xn接口Path Switch(I-SMF插入)成功次数
37|C510050015 基于Xn接口Path Switch(I-SMF不变)请求次数
38|C510050016 基于Xn接口Path Switch(I-SMF不变)成功次数
39|C510050017 基于Xn接口Path Switch(I-SMF改变)请求次数
40|C510050018 基于Xn接口Path Switch(I-SMF改变)成功次数
41|C510050019 基于Xn接口Path Switch(I-SMF删除)请求次数
42|C510050020 基于Xn接口Path Switch(I-SMF删除)成功次数
43|C510050021 5G内基于N2接口AMF不变的切换(I-SMF插入)请求次数
44|C510050022 5G内基于N2接口AMF不变的切换(I-SMF插入)成功次数
45|C510050023 5G内基于N2接口AMF不变的切换(I-SMF不变)请求次数
46|C510050024 5G内基于N2接口AMF不变的切换(I-SMF不变)成功次数
47|C510050025 5G内基于N2接口AMF不变的切换(I-SMF改变)请求次数
48|C510050026 5G内基于N2接口AMF不变的切换(I-SMF改变)成功次数
49|C510050027 5G内基于N2接口AMF不变的切换(I-SMF删除)请求次数
50|C510050028 5G内基于N2接口AMF不变的切换(I-SMF删除)成功次数
51|C510050029 5G内基于N2接口切入(I-SMF插入)请求次数
52|C510050030 5G内基于N2接口切入(I-SMF插入)成功次数
53|C510050031 5G内基于N2接口切入(I-SMF不变)请求次数
54|C510050032 5G内基于N2接口切入(I-SMF不变)成功次数
55|C510050033 5G内基于N2接口切入(I-SMF改变)请求次数
56|C510050034 5G内基于N2接口切入(I-SMF改变)成功次数
57|C510050035 5G内基于N2接口切入(I-SMF删除)请求次数
58|C510050036 5G内基于N2接口切入(I-SMF删除)成功次数
59|C510070010 PDU Session建立I-SMF插入请求次数
60|C510070011 PDU Session建立I-SMF插入成功次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :I-SMF有以下两种不同的发现方式，可以通过[SET NFDISCOVERYMODE CONFIG]命令来配置NF发现模式，从而配置I-SMF发现方式。
NRF发现I-SMF。 
本地配置发现I-SMF。 
根据I-SMF发现方式的不同，I-SMF配置的使用也分为两种不同的方式。 
配置前提 :打开“AMF支持I-SMF功能”的License。 
配置过程 :通过NRF发现I-SMF和通过本地配置发现I-SMF，两种配置方式分别对应不同的配置过程。 
通过NRF发现I-SMF模式下的配置过程：执行命令SET NFDISCOVERYMODE CONFIG，配置SMF发现模式为NRF发现SMF。执行命令SET AMFSUPPORTISMF， 打开I-SMF开关。执行命令SET NRFDISCSMFPARACFG，配置发现SMF时携带参数preferredTa。【可选】NRF不支持优选TA特性时，可执行命令SET ASMFSELPOLICY，配置A-SMF选择支持优选TA。 
通过本地配置发现I-SMF模式下的配置过程：执行命令SET NFDISCOVERYMODE CONFIG，配置SMF发现模式为本地发现SMF。执行命令SET AMFSUPPORTISMF，打开I-SMF开关。执行命令ADD SMFIPPOOLCFG，配置A-SMF IP地址池。执行命令ADD SMFIPPOOLCFG，配置I-SMF IP地址池。执行命令ADD TAGROUPCFG，配置跟踪区组配置。执行命令ADD SMFSERVAREACFG，配置A-SMF服务区配置。 
配置实例 :场景说明 :在NRF发现SMF模式下，各场景下的配置相同。 
数据规划 :配置项|参数|取值
---|---|---
I-SMF策略配置|AMF支持I-SMF|是
A-SMF选择策略配置|A-SMF选择支持优选TA|是
发现SMF参数配置|是否携带preferredTa|是
配置步骤 :步骤|说明|操作
---|---|---
1|设置I-SMF策略配置，打开I-SMF开关。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|设置A-SMF选择策略配置，支持A-SMF选择优选TA功能。|SET ASMFSELPOLICY:AMFSELASMFBYTA="SUPPORT"
3|设置发现SMF参数配置，携带preferredTa。|SET NRFDISCSMFPARACFG:CARRYPREFERREDTAI="SupPreferredTai"
场景说明 :本地发现SMF模式下的四个不同场景。 
场景一：
非漫游场景下，用户非移动时I-SMF插入。非跨PLMN漫游场景下，UE没有移动，发起PDU会话建立请求，网络中A-SMF管理的UPF无法与UE所在的基站建立连接。运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service area，决策并执行I-SMF插入。
场景二：
非漫游场景下，用户移动时I-SMF插入、改变和删除。非跨PLMN漫游场景下，UE已建立PDU会话，为了保证会话不中断，执行移动注册更新/业务请求/跨NG-RAN N2口切换/Xn切换等业务时，如果UE从A-SMF service area移动到new I-SMF service area，则AMF选择并插入I-SMF；如果UE从old I-SMF service area移动到new I-SMF service area，则I-SMF改变，AMF选择new I-SMF；如果UE从I-SMF service area移动回到A-SMF service area，则AMF删除I-SMF。 
场景三：
跨PLMN漫游Local Breakout场景下，用户非移动时I-SMF插入。跨PLMN漫游Local Breakout场景下，UE没有移动，在VPLMN下发起PDU会话建立请求，网络中A-SMF管理的UPF无法与UE所在的基站建立连接。运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service area，决策并执行I-SMF插入。
场景四：
跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除。跨PLMN漫游Local Breakout场景下，UE在VPLMN下已建立PDU会话，为了保证会话不中断，执行移动注册更新/业务请求/跨NG-RAN N2口切换/Xn切换等业务时，如果UE从A-SMF service area移动到new I-SMF service area，则AMF选择并插入I-SMF；如果UE从old I-SMF service area移动到new I-SMF service area，则I-SMF改变，AMF选择new I-SMF；如果UE从I-SMF service area移动回到A-SMF service area，则AMF删除I-SMF。 
数据规划 :场景|配置项|配置说明|参数取值
---|---|---|---
场景一|业务发生时所在TA|TA1|TA1:100001
A-SMF服务TA|场景一|TA2|TA2:100000
I-SMF策略配置|场景一|是否支持I-SMF功能|是
A-SMF的地址信息|场景一|A-SMF IP地址|ip:192.168.100.80  port:8080  id:1
I-SMF的地址信息|场景一|I-SMF IP地址|ip:192.168.100.81  port:8080  id:2
A-SMF NF profile级信息|场景一|A-SMF NF profile|SMFPROFILEID:1,HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1",PDUSESSSERPROFILEID:1
A-SMF NF service级信息|场景一|A-SMF NF service profile|SMFSERPROFILEID:1,SMFSERTYPE:"PDU_SESSION_SERVICE",HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:16,SCHEME:"HTTP",APIVERSION:"V1"
I-SMF profile NF级信息|场景一|I-SMF NF profile|SMFPROFILEID:2,HOST:"zte.com.cn2",IPPOOLID:2,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1",PDUSESSSERPROFILEID:2
A-SMF地址解析配置|场景一|本地发现A-SMF配置|ID:1,DNN:"zte.com",SNSSAISST:"eMBB",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:1
I-SMF地址解析配置|场景一|本地发现I-SMF配置，支持TA1|ID:1,MCC:"460",MNC:"011",TAC:"100001",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:2
跟踪区组配置|场景一|配置A-SMF的跟踪区组，不支持TA1|TAGROUPID:1,MCC:"460",MNC:"011",TAC:"100000",TACST:"000000",TACEND:"000000",TAGRPTYPE:"COMMTYPE"
A-SMF服务区配置|场景一|配置A-SMF的fqdn和A-SMF跟踪区的对应关系|FQDN:"zte.com.cn",TAGRPID:1
场景二|UE开始所在TA1，插入I-SMF|TA1|TA1:100001
UE移动到TA2,I-SMF改变|场景二|TA2|TA2:100002
UE移动到TA3,A-SMF能服务的TA, I-SMF删除|场景二|TA3|TA3:100000
是否支持I-SMF功能|场景二|I-SMF策略配置|是
A-SMF的地址信息|场景二|A-SMF IP地址|ip:192.168.100.80  port:8080  id:1
I-SMF1的地址信息|场景二|I-SMF1 IP地址|ip:192.168.100.81  port:8080  id:2
I-SMF2的地址信息|场景二|I-SMF2 IP地址|ip:192.168.100.82  port:8080  id:3
A-SMF NF级信息|场景二|A-SMF NF profile|SMFPROFILEID:1,HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1",PDUSESSSERPROFILEID:1
A-SMF NF service级信息|场景二|A-SMF NF service profile|SMFSERPROFILEID:1,SMFSERTYPE:"PDU_SESSION_SERVICE",HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:16,SCHEME:"HTTP",APIVERSION:"V1"
I-SMF NF级信息|场景二|I-SMF1 NF profile|SMFPROFILEID:2,HOST:"zte.com.cn2",IPPOOLID:2,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1"
I-SMF NF级信息|场景二|I-SMF2 NF profile|SMFPROFILEID:3,HOST:"zte.com.cn3",IPPOOLID:3,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1"
本地发现A-SMF配置|场景二|A-SMF地址解析配置|ID:1,DNN:"zte.com",SNSSAISST:"eMBB",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:1
本地发现I-SMF配置|场景二|I-SMF1地址解析配置|ID:1,MCC:"460",MNC:"011",TAC:"100001",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:2
本地发现I-SMF配置|场景二|I-SMF2地址解析配置|ID:2,MCC:"460",MNC:"011",TAC:"100002",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:3
配置A-SMF的跟踪区组|场景二|跟踪区组配置|TAGROUPID:1,MCC:"460",MNC:"011",TAC:"100000",TACST:"000000",TACEND:"000000",TAGRPTYPE:"COMMTYPE"
配置A-SMF的fqdn和A-SMF跟踪区的对应关系|场景二|A-SMF服务区配置|FQDN:"zte.com.cn",TAGRPID:1
场景三|业务发生时所在ta|TA1|TA1:100001
A-SMF服务ta|场景三|TA2|TA2:100000
是否支持I-SMF功能|场景三|I-SMF策略配置|是
A-SMF的地址信息|场景三|A-SMF IP地址|ip:192.168.100.80 port:8080 id:1
I-SMF的地址信息|场景三|I-SMF IP地址|ip:192.168.100.81 port:8080 id:2
A-SMF NF级信息|场景三|A-SMF NF profile|SMFPROFILEID:1,HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1",PDUSESSSERPROFILEID:1
A-SMF NF service级信息|场景三|A-SMF NF service profile|SMFSERPROFILEID:1,SMFSERTYPE:"PDU_SESSION_SERVICE",HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:16,SCHEME:"HTTP",APIVERSION:"V1"
I-SMF NF级信息|场景三|I-SMF NF profile|SMFPROFILEID:2,HOST:"zte.com.cn2",IPPOOLID:2,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1",PDUSESSSERPROFILEID:2
本地发现A-SMF配置|场景三|A-SMF地址解析配置|ID:1,DNN:"zte.com",SNSSAISST:"eMBB",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:1
本地发现I-SMF配置,支持TA1|场景三|I-SMF地址解析配置|ID:1,MCC:"460",MNC:"011",TAC:"100001",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:2
配置A-SMF的跟踪区组，不支持TA1|场景三|跟踪区组配置|TAGROUPID:1,MCC:"460",MNC:"011",TAC:"100000",TACST:"000000",TACEND:"000000",TAGRPTYPE:"COMMTYPE"
配置A-SMF的fqdn和A-SMF跟踪区的对应关系|场景三|A-SMF服务区配置|FQDN:"zte.com.cn",TAGRPID:1
场景四|UE开始所在TA1，插入I-SMF|TA1|TA1:100001
UE移动到TA2,I-SMF改变|场景四|TA2|TA2:100002
UE移动到TA3,A-SMF能服务的TA, I-SMF删除|场景四|TA3|TA3:100000
是否支持I-SMF功能|场景四|I-SMF策略配置|是
A-SMF的地址信息|场景四|A-SMF IP地址|ip:192.168.100.80 port:8080 id:1
I-SMF1的地址信息|场景四|I-SMF1 IP地址|ip:192.168.100.81 port:8080 id:2
I-SMF2的地址信息|场景四|I-SMF2 IP地址|ip:192.168.100.82 port:8080 id:3
A-SMF NF级信息|场景四|A-SMF NF profile|SMFPROFILEID:1,HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1",PDUSESSSERPROFILEID:1
A-SMF NF service级信息|场景四|A-SMF NF service profile|SMFSERPROFILEID:1,SMFSERTYPE:"PDU_SESSION_SERVICE",HOST:"zte.com.cn",IPPOOLID:1,PRIORITY:5,WEIGHT:16,SCHEME:"HTTP",APIVERSION:"V1"
I-SMF NF级信息|场景四|I-SMF1 NF profile|SMFPROFILEID:2,HOST:"zte.com.cn2",IPPOOLID:2,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1"
I-SMF NF级信息|场景四|I-SMF2 NF profile|SMFPROFILEID:3,HOST:"zte.com.cn3",IPPOOLID:3,PRIORITY:5,WEIGHT:100,SCHEMEAPIVERSION:"HTTP",APIVERSION:"V1"
本地发现A-SMF配置|场景四|A-SMF地址解析配置|ID:1,DNN:"zte.com",SNSSAISST:"eMBB",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:1
本地发现I-SMF配置|场景四|I-SMF1地址解析配置|ID:1,MCC:"460",MNC:"011",TAC:"100001",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:2
本地发现I-SMF配置|场景四|I-SMF2地址解析配置|ID:2,MCC:"460",MNC:"011",TAC:"100002",SNSSAISD:"12",NSIID:"jiangsu.nanjing",SMFPROFILEID:3
配置A-SMF的跟踪区组|场景四|跟踪区组配置|TAGROUPID:1,MCC:"460",MNC:"011",TAC:"100000",TACST:"000000",TACEND:"000000",TAGRPTYPE:"COMMTYPE"
配置A-SMF的fqdn和A-SMF跟踪区的对应关系|场景四|A-SMF服务区配置|FQDN:"zte.com.cn",TAGRPID:1
配置步骤 :场景|步骤|说明|操作
---|---|---|---
场景一|1|设置I-SMF策略配置，打开I-SMF开关|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|场景一|配置A-SMF的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|场景一|配置I-SMF的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|场景一|配置A-SMF跟踪区 不支持TA1，支持TA2|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
5|场景一|配置A-SMF服务区，即A-SMF的fqdn和跟踪区的对应关系|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
场景二|1|设置I-SMF策略配置，打开I-SMF开关|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|场景二|配置A-SMF的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|场景二|配置I-SMF1的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|场景二|配置I-SMF2的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=3,IPADDRESS=192.168.100.82,PORT=8080
5|场景二|配置A-SMF跟踪区 不支持当前ta|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
6|场景二|配置A-SMF服务区，即A-SMF的fqdn和跟踪区的对应关系|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
场景三|1|设置I-SMF策略配置，打开I-SMF开关|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|场景三|配置A-SMF的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|场景三|配置I-SMF的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|场景三|配置A-SMF跟踪区 不支持TA1|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
5|场景三|配置A-SMF服务区，即A-SMF的fqdn和跟踪区的对应关系|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
场景四|1|设置I-SMF策略配置，打开I-SMF开关|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|场景四|配置A-SMF的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|场景四|配置I-SMF1的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|场景四|配置I-SMF2的地址池信息|ADD SMFIPPOOLCFG:ADDRPOOLID=3,IPADDRESS=192.168.100.82,PORT=8080
5|场景四|配置A-SMF跟踪区 不支持当前ta|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
6|场景四|配置A-SMF服务区，即A-SMF的fqdn和跟踪区的对应关系|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
场景一 :场景说明 :非漫游场景下，用户非移动时I-SMF插入。非跨PLMN漫游场景下，UE没有移动，发起PDU会话建立请求，网络中A-SMF管理的UPF无法与UE所在的基站建立连接。运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service area，决策并执行I-SMF插入。
数据规划 :参数|取值
---|---
I-SMF策略配置|AMF是否支持I-SMF|支持
SMF地址池配置|地址池标识|1
IP地址|SMF地址池配置|192.168.100.80
端口号|SMF地址池配置|8080
解析SMF策略配置|支持基于号段选择A-SMF|支持
支持基于号段选择I-SMF和V-SMF|解析SMF策略配置|支持
支持基于号段本地解析A-SMF地址|解析SMF策略配置|支持
支持基于号段本地解析I-SMF和V-SMF地址|解析SMF策略配置|支持
跟踪区组配置|跟踪区组标识|1
移动国家码|跟踪区组配置|460
移动网络码|跟踪区组配置|011
跟踪区码（HEX）|跟踪区组配置|100000
跟踪区码起始（HEX）|跟踪区组配置|000000
跟踪区码终止（HEX）|跟踪区组配置|000000
跟踪区组类型|跟踪区组配置|COMMTYPE
SMF服务区域配置|跟踪区组号|1
编号|SMF服务区域配置|1
SMF FQDN|SMF服务区域配置|zte.com.cn
配置步骤 :步骤|说明|操作
---|---|---
1|设置I-SMF策略配置，打开I-SMF开关。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|配置A-SMF的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|配置I-SMF的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT"
5|配置A-SMF跟踪区不支持TA1，支持TA2。|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
6|配置A-SMF服务区，即A-SMF的FQDN和跟踪区的对应关系。|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
场景二 :场景说明 :非漫游场景下，用户移动时I-SMF插入、改变和删除。非跨PLMN漫游场景下，UE已建立PDU会话，为了保证会话不中断，执行移动注册更新/业务请求/跨NG-RAN N2口切换/Xn切换等业务时，如果UE从A-SMF service area移动到new I-SMF service area，则AMF选择并插入I-SMF；如果UE从old I-SMF service area移动到new I-SMF service area，则I-SMF改变，AMF选择new I-SMF；如果UE从I-SMF service area移动回到A-SMF service area，则AMF删除I-SMF。 
数据规划 :参数|取值
---|---
I-SMF策略配置|AMF是否支持I-SMF|支持
SMF地址池配置|地址池标识|1
IP地址|SMF地址池配置|192.168.100.80
端口号|SMF地址池配置|8080
解析SMF策略配置|支持基于号段选择A-SMF|支持
支持基于号段选择I-SMF和V-SMF|解析SMF策略配置|支持
支持基于号段本地解析A-SMF地址|解析SMF策略配置|支持
支持基于号段本地解析I-SMF和V-SMF地址|解析SMF策略配置|支持
跟踪区组配置|跟踪区组标识|1
移动国家码|跟踪区组配置|460
移动网络码|跟踪区组配置|011
跟踪区码（HEX）|跟踪区组配置|100000
跟踪区码起始（HEX）|跟踪区组配置|000000
跟踪区码终止（HEX）|跟踪区组配置|000000
跟踪区组类型|跟踪区组配置|COMMTYPE
SMF服务区域配置|跟踪区组号|1
编号|SMF服务区域配置|1
SMF FQDN|SMF服务区域配置|zte.com.cn
配置步骤 :步骤|说明|操作
---|---|---
1|设置I-SMF策略配置，打开I-SMF开关。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|配置A-SMF的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|配置I-SMF1的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|配置I-SMF2的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=3,IPADDRESS=192.168.100.82,PORT=8080
5|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT"
6|配置A-SMF跟踪区不支持当前TA。|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
7|配置A-SMF服务区，即A-SMF的FQDN和跟踪区的对应关系。|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
场景三 :场景说明 :跨PLMN漫游Local Breakout场景下，用户非移动时I-SMF插入。跨PLMN漫游Local Breakout场景下，UE没有移动，在VPLMN下发起PDU会话建立请求，网络中A-SMF管理的UPF无法与UE所在的基站建立连接。运营商部署了I-UPF，AMF基于UE当前位置和A-SMF的service area，决策并执行I-SMF插入。
数据规划 :参数|取值
---|---
I-SMF策略配置|AMF是否支持I-SMF|支持
SMF地址池配置|地址池标识|1
IP地址|SMF地址池配置|192.168.100.80
端口号|SMF地址池配置|8080
解析SMF策略配置|支持基于号段选择A-SMF|支持
支持基于号段选择I-SMF和V-SMF|解析SMF策略配置|支持
支持基于号段本地解析A-SMF地址|解析SMF策略配置|支持
支持基于号段本地解析I-SMF和V-SMF地址|解析SMF策略配置|支持
跟踪区组配置|跟踪区组标识|1
移动国家码|跟踪区组配置|460
移动网络码|跟踪区组配置|011
跟踪区码（HEX）|跟踪区组配置|100000
跟踪区码起始（HEX）|跟踪区组配置|000000
跟踪区码终止（HEX）|跟踪区组配置|000000
跟踪区组类型|跟踪区组配置|COMMTYPE
SMF服务区域配置|跟踪区组号|1
编号|SMF服务区域配置|1
SMF FQDN|SMF服务区域配置|zte.com.cn
配置步骤 :步骤|说明|操作
---|---|---
1|设置I-SMF策略配置，打开I-SMF开关。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|配置A-SMF的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|配置I-SMF的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT"
5|配置A-SMF跟踪区不支持TA1。|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
6|配置A-SMF服务区，即A-SMF的FQDN和跟踪区的对应关系。|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
##### 场景四 
场景说明 :跨PLMN漫游Local Breakout场景下，用户移动时I-SMF插入、改变和删除。跨PLMN漫游Local Breakout场景下，UE在VPLMN下已建立PDU会话，为了保证会话不中断，执行移动注册更新/业务请求/跨NG-RAN N2口切换/Xn切换等业务时，如果UE从A-SMF service area移动到new I-SMF service area，则AMF选择并插入I-SMF；如果UE从old I-SMF service area移动到new I-SMF service area，则I-SMF改变，AMF选择new I-SMF；如果UE从I-SMF service area移动回到A-SMF service area，则AMF删除I-SMF。 
数据规划 :参数|取值
---|---
I-SMF策略配置|AMF是否支持I-SMF|支持
SMF地址池配置|地址池标识|1
IP地址|SMF地址池配置|192.168.100.80
端口号|SMF地址池配置|8080
解析SMF策略配置|支持基于号段选择A-SMF|支持
支持基于号段选择I-SMF和V-SMF|解析SMF策略配置|支持
支持基于号段本地解析A-SMF地址|解析SMF策略配置|支持
支持基于号段本地解析I-SMF和V-SMF地址|解析SMF策略配置|支持
跟踪区组配置|跟踪区组标识|1
移动国家码|跟踪区组配置|460
移动网络码|跟踪区组配置|011
跟踪区码（HEX）|跟踪区组配置|100000
跟踪区码起始（HEX）|跟踪区组配置|000000
跟踪区码终止（HEX）|跟踪区组配置|000000
跟踪区组类型|跟踪区组配置|COMMTYPE
SMF服务区域配置|跟踪区组号|1
编号|SMF服务区域配置|1
SMF FQDN|SMF服务区域配置|zte.com.cn
配置步骤 :步骤|说明|操作
---|---|---
1|设置I-SMF策略配置，打开I-SMF开关。|SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
2|配置A-SMF的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=192.168.100.80,PORT=8080
3|配置I-SMF1的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=2,IPADDRESS=192.168.100.81,PORT=8080
4|配置I-SMF2的地址池信息。|ADD SMFIPPOOLCFG:ADDRPOOLID=3,IPADDRESS=192.168.100.82,PORT=8080
5|设置解析SMF策略配置。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT"
6|配置A-SMF跟踪区不支持当前TA|ADD TAGROUPCFG:TAGROUPID=1,MCC="460",MNC="011",TAC="100000",TACST="000000",TACEND="000000",TAGRPTYPE="COMMTYPE"
7|配置A-SMF服务区，即A-SMF的FQDN和跟踪区的对应关系。|ADD SMFSERVAREACFG:ID=1,FQDN="zte.com.cn",TAGRPID=1
调整特性 :本特性不涉及调整特性。 
测试用例 :测试用例1
测试项目|I-SMF插入
---|---
测试目的|测试UE从A-SMF service area移动到new I-SMF service area，AMF选择并插入I-SMF。
预置条件|I-SMF开关打开，I-SMF license打开。用户已成功注册到5GC。
测试过程|UE已建立PDU会话，发生Xn切换，TA区域已发生变更，已不在A-SMF的服务区。
通过准则|AMF通过查询NRF，获得I-SMF的信息。AMF向I-SMF发起Nsmf_PDUSession_CreateSMContext Request。I-SMF响应成功。Xn切换成功。
测试结果|–
测试用例2
测试项目|I-SMF改变
---|---
测试目的|测试UE从I-SMF service area移动到此I-SMF不能服务的area，AMF选择并使用新的I-SMF。
预置条件|I-SMF开关打开，I-SMF license打开。用户已成功注册到5GC。
测试过程|UE已建立PDU会话，且PDU会话使用了I-SMF。发生Xn切换，TA区域已发生变更，已不在I-SMF的服务区。
通过准则|AMF通过查询NRF，获得I-SMF的信息。AMF向I-SMF发起Nsmf_PDUSession_CreateSMContext Request。I-SMF响应成功。Xn切换成功。AMF向老的I-SMF发起删除流程。
测试结果|–
测试用例3
测试项目|I-SMF删除
---|---
测试目的|测试UE从I-SMF service area移动到此A-SMF的area，AMF选择并使用A-SMF。
预置条件|I-SMF开关打开，I-SMF license打开。用户已成功注册到5GC。
测试过程|UE已建立PDU会话，且PDU会话使用了I-SMF。发生Xn切换，TA区域已发生变更，不在I-SMF的服务区，回到了A-SMF的服务区。AMF不需要发起NRF查询。AMF向A-SMF发起Nsmf_PDUSession_CreateSMContext Request，消息中携带source I-SMF的smContextRef（携带之前source I-SMF在创建会话响应中头部带回的smContextRef，包含IP地址），携带n2sminfo。AMF收到成功的响应后，给基站发送path swith ACK，携带成功的PDU列表。AMF收到成功响应后，向source I-SMF发起Nsmf_PDUSession_ReleaseSMContext Request，携带I-SMF only indication，指示old I-SMF释放自身资源。AMF向A-SMF发起修改流程。
通过准则|AMF不需要发起NRF查询。AMF向A-SMF发起Nsmf_PDUSession_CreateSMContext Request。A-SMF响应成功。Xn切换成功。AMF向I-SMF发起删除流程。
测试结果|–
常见问题处理 :无。 
## ZUF-79-20-003 I-SMF场景下的PDU会话重建 
特性描述 :特性描述 :描述 :定义 :I-SMF场景下的PDU会话重建是指对于本网用户，当AMF发现由于用户移动需要插入/改变I-SMF时，在用户进入空闲态后通知UE重新建立PDU会话。 
背景知识 :一些运营商网络下，大区间/省间漫游采用Local BreakOut（拜访地直接接入）方式。 
用户在大区间/省间漫游的过程中，需要保证业务连续性。当用户跨大区/省移动后，原来的A-SMF无法服务于当前区域，AMF会在PDU会话中插入/改变I-SMF。I-SMF与A-SMF不在同一区域（例如：不同省份），导致I-SMF和A-SMF管理下UPF之间的迂回流量增加，浪费承载资源，增加业务时延。
为了节省承载资源，降低业务时延，对于本网用户，当AMF发现需要插入/改变I-SMF时，会通知UE重新建立PDU会话。 
应用场景 :用户跨大区/省移动后，原来的A-SMF无法服务于当前区域，AMF在PDU会话中插入I-SMF，I-SMF和A-SMF在不同区域。如[图1]所示。
图1  用户跨大区/省移动后插入I-SMF

客户收益 :受益方|受益描述
---|---
运营商|节省承载资源。
移动用户|降低业务时延，提升业务体验。
实现原理 :系统架构 :本特性涉及的PDU会话插入I-SMF的网络架构如下图所示。 
图2  PDU会话插入I-SMF的非漫游网络架构

涉及的网元 :网元名称|网元作用
---|---
UE|接受网络侧的消息指示，重建PDU会话。
AMF|识别出需要重建的PDU会话，在用户进入空闲态后，通知UE重建PDU会话。收到UE的PDU会话建立请求后，重新选择SMF，建立PDU会话。
SMF|基于AMF的指示，通知UE重建PDU会话。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N11|ZUF-79-19-004 N11
本网元实现 :本网用户移动后，对于需要插入/改变I-SMF且对应DNN配置为需要重建的PDU会话，AMF判定该PDU会话需要重建。 
AMF识别出需要重建的PDU会话后，控制PDU会话重建的时机： 
在特定的时间段，发起PDU会话重建。 
在用户进入空闲态后立即发起PDU会话重建，或者进入空闲态的时长达到一定阈值时发起PDU会话重建。 
PDU会话重建
PDU会话重建示意图如[图3]所示。
图3  PDU会话重建示意图

UE在区域1建立PDU会话，AMF1选择本区域内的SMF1。 
UE移动到区域2，SMF1无法服务当前区域，AMF2插入SMF2作为I-SMF。 
UE进入空闲态后，AMF2通知UE重建PDU会话，AMF2选择本区域内的SMF2。 
业务流程 :PDU会话重建涉及的流程如下： 
业务请求流程 
移动注册更新流程 
基于N2接口的切换流程 
基于Xn接口的切换流程 
空闲态下基于N26接口，4G跨系统移动到5G流程 
基于N26接口，4G跨系统移动到5G进行切换流程 
PDU会话重建流程
PDU会话重建流程如下图。 
流程说明如下： 
AMF识别需要重建的PDU会话，通过(R)AN向对应的UE发送Paging消息。 
UE发起业务请求流程，同系统现有处理。 
业务请求流程结束后，针对需要重建的PDU会话，AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext Request消息，携带release为true，原因值为“REL_DUE_TO_REACTIVATION”。 
SMF返回Nsmf_PDUSession_UpdateSMContext Response消息，携带n1SmMsg为PDU session release command。 
AMF透传PDU session release command消息给UE。 
后续流程同AMF触发的PDU会话释放流程。 
UE向AMF发送PDU Session Establishment Request消息，重建PDU会话。 
AMF选择本区域内的A-SMF，向A-SMF发送Nsmf_PDUSession_CreateSMContext Request消息。 
后续流程同现有PDU会话建立流程。 
系统影响 :AMF需要向用户发起寻呼，并通知用户重建PDU会话。因此，网络中的寻呼次数、业务请求次数、PDU会话释放和建立次数会增加，对系统性能有一定影响。具体影响取决于用户跨大区/省移动时，I-SMF插入/改变的话务模型。 
应用限制 :该特性不涉及应用限制。 
特性交互 :业务|交互
---|---
ZUF-79-20-002 I-SMF选择|I-SMF特性开启后，用户跨大区/省移动过程中AMF才会插入/改变I-SMF，发起PDU会话重建。
遵循标准 :无。 
特性能力 :名称|指标
---|---
支持PDU会话重建的最大DNN个数|128（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.21.10|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。
对其他网元的要求 :UE|gNodeB|SMF
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
PDU会话重建策略配置|SET PDUREBUILD POLICY
SHOW PDUREBUILD POLICY|PDU会话重建策略配置
基于DNN的PDU会话重建配置|ADD PDUREBUILDDNNCFG
SET PDUREBUILDDNNCFG|基于DNN的PDU会话重建配置
DEL PDUREBUILDDNNCFG|基于DNN的PDU会话重建配置
SHOW PDUREBUILDDNNCFG|基于DNN的PDU会话重建配置
性能统计 :性能计数器名称
---
C510070012 PDU会话重建引起的PDU Session释放次数
告警和通知 :该特性不涉及告警和通知的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置可以完成当用户发生I-SMF插入/改变的注册更新、切换、业务请求流程后，AMF为这类用户进行重建PDU会话的功能，从而在用户接入的I-SMF与A-SMF不在同一区域时，减少I-SMF和A-SMF管理下UPF之间的迂回流量，避免承载资源浪费，降低业务时延。 
配置前提 :AMF以及周边网元运行正常。 
AMF支持I-SMF功能。 
配置过程 :执行[SET PDUREBUILD POLICY]命令，设置PDU会话重建策略为支持。
执行[ADD PDUREBUILDDNNCFG]命令，设置需要重建的DNN，配置重建PDU会话的时间范围，以及空闲态的时长。
配置实例 :###### 场景一：数据DNN 
场景说明
对于数据DNN，在固定时间内，用户已进入空闲态一段时间后，进行PDU会话重建。 
数据规划
配置项|参数|取值
---|---|---
PDU会话重建策略配置|支持PDU会话重建|SPRT
基于DNN的PDU会话重建配置|DNN|cmnet
起始时间|基于DNN的PDU会话重建配置|1_TIME
结束时间|基于DNN的PDU会话重建配置|2_TIME
空闲态时长|基于DNN的PDU会话重建配置|5
配置步骤
步骤|说明|操作
---|---|---
1|开启PDU会话重建功能|SET PDUREBUILD POLICY:SUPPDUREBUILD="SPRT"
2|配置cmnet DNN，在固定时间（01:00-02:00）且用户已经进入空闲态一段时间（5 S）后，进行PDU会话重建|ADD PDUREBUILDDNNCFG:DNN="cmnet",STARTTIME="1_TIME",ENDTIME="2_TIME",IDLEDURATION=5
###### 场景二：语音DNN 
场景说明
对于语音DNN，用户一旦进入空闲态，立即进行PDU会话重建。 
数据规划
配置项|参数|取值
---|---|---
PDU会话重建策略配置|支持PDU会话重建|SPRT
基于DNN的PDU会话重建配置|DNN|ims
起始时间|基于DNN的PDU会话重建配置|0_TIME
结束时间|基于DNN的PDU会话重建配置|0_TIME
空闲态时长|基于DNN的PDU会话重建配置|0
配置步骤
步骤|说明|操作
---|---|---
1|开启PDU会话重建功能|SET PDUREBUILD POLICY:SUPPDUREBUILD="SPRT"
3|配置ims DNN，用户一旦进入空闲态立即进行PDU会话重建|ADD PDUREBUILDDNNCFG:DNN="ims",STARTTIME="0_TIME",ENDTIME="0_TIME",IDLEDURATION=0
调整特性 :本特性不涉及调整特性 
测试用例 :测试项目|对于IMS的语音DNN，用户一旦进入空闲态立即进行PDU会话重建
---|---
测试目的|验证对于语音DNN，在用户进入空闲态后可以立即进行PDU会话重建。
预置条件|AMF支持PDU会话重建功能。配置IMS DNN，设置用户一旦进入空闲态立即进行重建。
测试过程|用户发起PDU激活，DNN为IMS。用户发生移动性业务请求流程，该PDU发生I-SMF插入行为。用户进入空闲态。
通过准则|UE向AMF发起请求，重建PDU会话。AMF选择本区域内的A-SMF，向A-SMF发送Nsmf_PDUSession_CreateSMContext Request消息。
测试结果|–
测试项目|对于cmnet的数据DNN，在固定时间且用户已经进入空闲态一段时间后，进行重建
---|---
测试目的|验证对于数据DNN，在用户进入空闲态后，可以按照配置时间进行PDU会话重建。
预置条件|AMF支持PDU会话重建功能。配置cmnet DNN，设置在固定时间（01:00-02:00）内，且用户已经进入空闲态一段时间（5 S）后，进行PDU会话重建。
测试过程|用户发起PDU激活，DNN为cmnet。用户发生移动注册更新流程，该PDU发生I-SMF插入行为。用户进入空闲态超过5秒。
通过准则|时间到01:00-02:00时，UE向AMF发起请求，重建PDU会话。AMF选择本区域内的A-SMF，向A-SMF发送Nsmf_PDUSession_CreateSMContext Request消息。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
5GC :5G Core Network5G核心网
## A-SMF 
Anchor-SMF锚点SMF
AMF :Access and Mobility Management Function接入和移动管理功能
EPC :Evolved Packet Core演进的分组核心网
## I-SMF 
Intermediate-SMF中间SMF
## LBO 
Local Breakout本地路由疏导
NRF :NF Repository Function网络功能仓储
PCC :Policy and Charging Control计费和策略控制
PDU :Packet Data Unit分组数据单元
PLMN :Public Land Mobile Network公共陆地移动网
RAN :Radio Access Network无线接入网
SMF :Session Management Function会话管理功能
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
UPF :User Plane Function用户平面功能
## VPLMN 
Visited Public Land Mobile Network拜访公众陆地移动网
# ZUF-79-21 容灾 
## ZUF-79-21-001 AMF支持SMF容灾 
特性描述 :特性描述 :描述 :定义 :AMF支持SMF容灾功能指的是在SMF故障后，其原承担的会话不再有效，AMF感知SMF故障后，更新NF故障列表，扫描所有用户，释放与故障SMF相关的会话资源，通知UE进行会话重建。同时，新的PDU会话建立发现选择SMF时，剔除故障SMF，选择状态正常的SMF。
背景知识 :相比传统移动通讯的核心网，5G核心网存在大容量、高度集中等特点，对可靠性要求很高。外在因素（台风、地震、塌方等）和内在因素（设备老化、元件损坏、系统升级、掉电等）都会导致通讯设备业务中断，用户无法继续业务甚至无法接入，导致用户数据丢失、自动操作系统异常等严重后果。因此，需要一个完善强大的容灾系统来保障整个5G系统的稳定运行。 
5G核心网容灾采用跨DC的异地容灾或地理容灾的方式，当其中一个DC发生故障无法提供服务时，另外一个DC可以接管5G核心网业务。这样可以增强网络的处理能力和快速恢复能力，从而将损失降到最低。
应用场景 :###### 场景一：AMF识别SMF故障 
AMF通过NRF状态通知或者链路检测识别SMF发生故障后，在收到UE业务时自动识别出故障SMF，选择其他正常SMF进行业务流程，保证UE的接入。 
###### 场景二：无I-SMF场景下，SMF发生故障时，AMF释放与故障SMF相关的会话 
AMF通过NRF状态通知或者链路检测识别SMF发生故障后，通过定时器延时释放故障SMF的会话。延时定时器到期后后，AMF扫描与故障SMF相关的PDU会话，释放相关会话并通知UE重建会话。 
###### 场景三：I-SMF发生故障时，AMF重选I-SMF继续会话 
AMF通过NRF状态通知或者链路检测识别I-SMF发生故障后，设置定时器延时处理I-SMF会话。延时定时器到期后，AMF扫描与故障I-SMF相关的PDU会话，重选I-SMF继续会话。 
###### 场景四：AMF支持SMF恢复处理 
AMF通过NRF状态通知或者链路检测识别出故障SMF已经恢复之后，在收到UE业务时自动选择已经恢复的SMF进行业务流程。 
客户收益 :受益方|受益描述
---|---
运营商|满足运营商业务功能的需求，在SMF发生故障后继续为用户提供业务服务，保障整个网络正常运行，提高5G网络的可靠性。
移动用户|在SMF故障容灾场景下， 保障UE的接入，快速恢复用户业务，提高用户满意度。
实现原理 :系统架构 :AMF支持SMF故障网络及架构图如[图1]所示。
图1  SMF容灾架构示意图

###### 涉及的NF 
网元名称|网元作用
---|---
AMF|SMF发生故障或恢复后， AMF通过NRF状态通知或链路检测识别SMF故障或恢复。AMF扫描与故障SMF（无I-SMF场景下）相关的PDU会话，释放PDU会话并通知UE重建会话。AMF扫描与故障I-SMF相关的PDU会话，重选I-SMF继续会话。用户接入后，AMF识别故障SMF，选择正常的SMF执行业务流程。
NRF|AMF订阅NRF的状态通知，NRF检测到SMF故障或恢复，向AMF发送SMF故障通知或故障恢复消息。
SMF|SMF向NRF注册。
(R)AN|无线接入网络，在注册过程中根据UE请求的NSSAI或5G-GUTI选择Initial AMF。
UE|支持5G接入的终端，在注册请求消息中根据NSSAI inclusion mode，提供请求的NSSAI，并完成Allowed NSSAI和Rejected NSSAI的更新。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
NRF|ZUF-79-19-010 Nnrf
###### 本NF实现 
SMF发生故障或恢复时， AMF通过NRF状态通知或链路检测识别SMF故障或恢复。AMF可以通过NRF状态通知被动识别SMF故障或恢复AMF可以通过链路检测主动识别SMF故障或恢复 
SMF故障时，AMF选择其他正常SMF执行业务流程。 
AMF扫描与故障SMF（无I-SMF场景下）相关的PDU会话，释放PDU会话并通知UE重建会话。 
AMF扫描与故障I-SMF相关的PDU会话，重选I-SMF继续会话。 
业务流程 :SMF发生故障或恢复， AMF通过NRF状态通知或链路检测识别SMF故障或恢复
图2  SMF发生故障或恢复， AMF通过NRF状态通知或链路检测识别SMF故障或恢复

SMF_1接通电源后向NRF发送Nnrf_NFManagement_NFRegister消息进行网元注册。 
SMF_2接通电源后向NRF发送Nnrf_NFManagement_NFRegister消息进行网元注册。 
UE注册更新完毕后，发起PDU会话建立，AMF向NRF请求发现SMF后，向NRF发送Nnrf_NFManagement_NFStatusSubscribe消息，与NRF交互订阅SMF的状态。 
当SMF_1发生故障，NRF通过链路检测发现SMF_1故障。 
NRF根据状态订阅列表，向AMF发送Nnrf_NFManagement_NFStatusNotify通知SMF_1发生故障，AMF将SMF_1放入NF故障列表。 
当SMF_1故障恢复，NRF通过链路检测发现SMF_1故障已经恢复。 
NRF根据状态订阅列表，向AMF发送Nnrf_NFManagement_NFStatusNotify通知SMF_1故障已经恢复，AMF将SMF_1从NF故障列表移除。 
SMF故障时，AMF选择其他正常SMF执行业务流程
图3  AMF选择正常SMF执行业务流程

UE通过在N1 SM容器内发送包含PDU会话建立请求的NAS消息触发PDU会话建立过程，PDU会话建立请求携带PDU session ID, PDU Session Type, SSC mode, 5GSM Capability等信息。 
AMF通过NRF发现或本地策略选择SMF，排除故障的SMF_1，选择没有故障的SMF_2发起PDU会话建立流程。 
AMF向选择后的SMF_2发起Nsmf_PDUSession_CreateSMContext Request消息。 
SMF_2和PCF、UDM完成订阅检索、订阅更新、计费、QoS和规则创建等操作。 
SMF_2在会话承载创建完成后，向AMF发送Nsmf_PDUSession_CreateSMContext Response消息。 
SMF_2执行辅助身份验证和授权。 
SMF_2完成SM Policy关联创建和UPF会话创建。 
SMF_2会话和承载资源创建完成后，向AMF发送Namf_Communication_N1N2MessageTransfer消息，创建N1和N2接口会话，携带QoS信息。AMF返回响应。 
AMF收到消息，向gNodeB发送N2 PDU Session Establishment消息建立无线会话资源，同时向UE透传PDU Session Establishment Accept消息。 
后续流程正常完成，完成整个PDU会话创建过程。 
AMF扫描与故障SMF（无I-SMF）相关的PDU会话，释放PDU会话并通知UE重建会话
图4  AMF扫描与故障SMF（无I-SMF）相关的PDU会话，释放PDU会话并通知UE重建会话

SMF_1接通电源后向NRF发送Nnrf_NFManagement_NFRegister消息进行网元注册。 
SMF_2接通电源后向NRF发送Nnrf_NFManagement_NFRegister消息进行网元注册。 
UE注册更新完毕后，发起PDU会话建立。AMF向NRF请求发现SMF后，按照优先级和权重选择SMF_1，向SMF_1发起PDU会话建立过程。 
AMF向NRF发送Nnrf_NFManagement_NFStatusSubscribe消息订阅SMF的状态，并同时检测与SMF_1之间的链路状态。 
当SMF_1发生故障，AMF通过链路检测发现SMF_1故障 ，或者NRF发现SMF_1故障后，向AMF发送Nnrf_NFManagement_NFStatusNotify通知SMF_1发生故障。 
AMF启动定时扫描， 扫描所有与故障SMF相关的PDU会话，进行PDU会话释放流程。 
AMF根据用户状态进行释放： 
如果用户处于空闲态，首先寻呼用户，业务接入成功后，AMF发起PDU会话释放，触发UE进行PDU会话重建。 
如果用户处于连接态，AMF直接发起PDU会话释放，触发UE进行PDU会话重建。 

UE收到PDU会话释放消息后，触发PDU会话重建，AMF向状态正常的SMF_2发起PDU会话建立过程。 
AMF扫描与故障I-SMF相关的PDU会话，重选I-SMF继续会话
图5  AMF扫描与故障I-SMF相关的PDU会话，重选I-SMF继续会话

I-SMF_1接通电源后向NRF发送Nnrf_NFManagement_NFRegister消息进行网元注册。 
I-SMF_2接通电源后向NRF发送Nnrf_NFManagement_NFRegister消息进行网元注册。 
UE在核心网中注册完成后，发起PDU会话建立流程。AMF决策需要插入I-SMF，向NRF请求发现I-SMF后，按照优先级和权重选择I-SMF_1，向I-SMF_1/A-SMF发起PDU会话建立过程。 
AMF进行状态订阅和链路检测。 
4a. AMF向NRF发送Nnrf_NFManagement_NFStatusSubscribe消息订阅I-SMF_1的状态。 
4b. AMF检测其与I-SMF_1之间的链路状态。 
AMF通过以下方式获知I-SMF_1发生故障： 
NRF发现I-SMF_1故障后，向AMF发送Nnrf_NFManagement_NFStatusNotify消息通知I-SMF_1发生故障。 
AMF通过链路检测发现I-SMF_1故障。 
AMF启动定时扫描， 扫描所有与故障I-SMF相关的PDU会话。 
AMF根据用户状态进行I-SMF重选流程： 
7a. 如果用户处于连接态，则发起AN释放。 
7b. 如果用户处于空闲态，则寻呼用户。 
UE发起业务请求流程。 
AMF执行I-SMF重选流程，基于TA/S-NSSAI，通过NRF发现重新选择到I-SMF_2。 
AMF向重选的I-SMF_2发送Nsmf_PDUSession_CreateSMContext Request消息，携带A-SMF信息。 
I-SMF_2向A-SMF获取到PDU会话信息。 
AMF收到I-SMF_2返回的Nsmf_PDUSession_CAreateSMContext Response消息，保存I-SMF_2的URI，N2 SM information等信息。
AMF向RAN发送N2 Request消息，包含N2 SM信息（用于RAN侧更新N3隧道信息）。 
业务请求流程继续。 
系统影响 :系统增加了SMF故障后的会话扫描释放，会消耗少量性能，此操作是容灾后的故障恢复，对系统整体性能影响有限。 
应用限制 :该特性的链路检测功能（即检测AMF与SMF之间的链路是否正常），只适用于AMF与对端SMF直连的场景。如果AMF与SMF之间是非直连，如间接通信，则不适用该特性。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2
TS 23.502|3GPP|3GPP TS 23.502 Technical Specification Group Services and System Aspects; Procedures for the 5G System; Stage 2
TS 24007|3GPP|Mobile radio interface signalling layer 3
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 :名称|指标
---|---
AMF支持同时进行链路检测的最大NF个数|4000
AMF支持同时进行链路检测的最大IP个数|6000
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.20|新增以下功能：无I-SMF场景下，若SMF异常，AMF释放故障SMF相关会话有I-SMF场景下，若I-SMF异常，AMF对故障I-SMF相关会话处理
01|V7.20.20|首次发布
License要求 :该特性为AMF容灾的基本特性，无需License支持。 
###### 对其他NF的要求 
UE|gNodeB|SMF|NRF|UDM
---|---|---|---|---
√|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :工程规划上，需要AMF以及SMF进行容灾备份，如POOL容灾备份。 
O&M相关 :命令 :配置项|命令
---|---
NF故障检测及处理配置|SET NFDETECPROCCFG
SHOW NFDETECPROCCFG|NF故障检测及处理配置
SMF容灾策略公共配置|SET SMFDRPOLICYCFG
SHOW SMFDRPOLICYCFG|SMF容灾策略公共配置
A-SMF容灾策略配置|SET ASMFDRPOLICYCFG
SHOW ASMFDRPOLICYCFG|A-SMF容灾策略配置
I/V-SMF容灾策略配置|SET IVSMFDRPOLICYCFG
SHOW IVSMFDRPOLICYCFG|I/V-SMF容灾策略配置
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :告警和通知
---
3305242916 SMF不可达
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :为支持SMF容灾功能，需要配置当AMF感知到SMF故障时的处理策略。 
NF故障检测及处理配置：配置是否启用通过NRF状态通知检测NF故障及恢复的功能，以及设置周期性向NRF查询NF故障列表中故障网元节点的间隔时长和每个查询周期查询故障NF的个数。支持配置SMF本地链路检测，SMF本地检测记录是在AMF通过NRF选择某个SMF后插入的。从插入本地检测记录开始，到达设置的老化时间，检测记录会被自动删除，待下次发现NF后再次插入。 
SMF容灾策略公共配置：用于控制SMF会话释放延时时间、会话释放频率、单次查询用户个数、本地释放后原因值。 
A-SMF容灾策略配置：用来控制A-SMF容灾策略配置，包括：IMS会话释放开关、数据会话释放开关、IMS会话释放通知开关和数据会话释放通知开关。 
I/V-SMF容灾策略配置：用来控制I/V-SMF容灾策略配置，包括： I-SMF IMS会话释放开关、 I-SMF 数据会话释放开关、V-SMF IMS会话释放开关、V-SMF 数据会话释放开关、IMS会话释放通知开关和数据会话释放通知开关。 
配置前提 :AMF向NRF订阅SMF的状态并检测和SMF之间的链路运行。 
配置过程 :根据SMF状态检测方式，分别配置通过NRF状态通知检测和本地检测。 
配置通过NRF状态通知检测执行SET NFDETECPROCCFG命令，配置是否启用通过NRF状态通知检测NF故障及恢复的功能。配置周期性向NRF查询NF故障列表中故障网元节点的间隔时长和每个查询周期查询故障NF的个数。 
配置本地检测执行SET NFDETECPROCCFG命令，配置是否启用SMF本地检测功能，配置NRF发现检测老化时间和本地发现检测老化时间。 
执行[SET SMFDRPOLICYCFG]命令，配置SMF故障后会话延时释放时间、会话释放频率、单次查询用户个数、本地释放后原因值会话释放通知开关。
（可选）执行[SET ASMFDRPOLICYCFG]命令，配置A-SMF容灾策略配置参数，包括：A-SMF IMS会话释放开关、数据会话释放开关、IMS会话释放通知开关和数据会话释放开关。
（可选）执行[SET IVSMFDRPOLICYCFG]命令，配置I/V-SMF容灾策略配置参数，包括：I-SMF IMS会话释放开关、I-SMF 数据会话释放开关、V-SMF IMS会话释放开关、V-SMF 数据会话释放开关、IMS会话释放通知开关和数据会话释放通知开关。
配置实例 :###### 场景1：通过NRF状态订阅识别出SMF发生故障和恢复 
场景说明
NRF检测开关打开，SMF发生故障，AMF通过NRF状态订阅识别出SMF发生故障。 
SMF发生故障后恢复，AMF通过NRF状态通知或者链路检测识别出故障SMF已经恢复。 
数据规划
配置项|参数|取值
---|---|---
NF故障检测及处理配置|NRF检测开关|功能打开
查询周期(秒)|NF故障检测及处理配置|60
查询个数|NF故障检测及处理配置|1
配置步骤
步骤|说明|操作
---|---|---
1|配置启用通过NRF状态通知检测NF故障和恢复的功能。配置向NRF周期性查询NF故障列表中故障网元节点的时间间隔和每个查询周期查询故障NF的个数。|SET NFDETECPROCCFG:NRFSWITCH="OFF",QUERYPERIOD=60,QUERYNUMBER=1
###### 场景2：通过本地检测识别出SMF发生故障和恢复 
场景说明
SMF本地检测开关打开，AMF与SMF间链路故障，AMF通过本地检测识别出SMF发生故障。 
SMF发生故障后恢复，AMF通过本地检测识别出故障SMF已经恢复。 
数据规划
配置项|参数|取值
---|---|---
NF故障检测及处理配置|SMF本地检测开关|功能打开
查询周期(秒)|NF故障检测及处理配置|60
查询个数|NF故障检测及处理配置|1
配置步骤
步骤|说明|操作
---|---|---
1|配置启用SMF本地检测功能。配置向NRF周期性查询NF故障列表中故障网元节点的时间间隔和每个查询周期查询故障NF的个数。|SET NFDETECPROCCFG:QUERYPERIOD=60,QUERYNUMBER=1,LOCALCFGSWITCH="ON"
###### 场景3：无I-SMF时，SMF发生故障时，AMF释放与故障SMF相关的会话 
场景说明
NRF检测开关打开，SMF发生故障，AMF通过NRF状态通知识别出SMF发生故障。 
AMF识别A-SMF发生故障后，设置会话延时释放的相关参数，释放与故障A-SMF相关的IMS会话和数据会话。 
数据规划
配置项|参数|取值
---|---|---
NF故障检测及处理配置|NRF检测开关|功能打开
查询周期(秒)|NF故障检测及处理配置|60
查询个数|NF故障检测及处理配置|1
SMF容灾策略公共配置|会话释放延时时间(second)|10
会话释放频率(millisecond)|SMF容灾策略公共配置|500
单次查询用户个数|SMF容灾策略公共配置|60
本地释放后原因值|SMF容灾策略公共配置|5GSM Cause: Invalid PDU session identity
A-SMF容灾策略配置|IMS会话释放开关|会话释放
数据会话释放开关|A-SMF容灾策略配置|会话释放
IMS会话释放通知开关|A-SMF容灾策略配置|释放后通知
数据会话释放通知开关|A-SMF容灾策略配置|释放后不通知
配置步骤
步骤|说明|操作
---|---|---
1|配置启用通过NRF状态通知检测NF故障和恢复的功能。配置向NRF周期性查询NF故障列表中故障网元节点的时间间隔和每个查询周期查询故障NF的个数。|SET NFDETECPROCCFG:NRFSWITCH="ON",QUERYPERIOD=60,QUERYNUMBER=1
2|配置SMF故障后，会话延时释放时间、会话释放频率、单次查询用户个数、本地释放后原因值。|SET SMFDRPOLICYCFG:DELAYTIME=10,RELEASERATE=500,QUERYNUMBER=60,PROCESSAFTERREL="CARRYGSMCAUSE"
3|配置A-SMF容灾策略，配置IMS会话释放开关、数据会话释放开关、IMS会话释放通知开关和数据会话释放通知开关。|SET ASMFDRPOLICYCFG:IMSPDURELSWITCH="RELEASE",DATAPDURELSWITCH="RELEASE",IMSRELNOTIFYSWITCH="RELEASENOTIFY",DATARELNOTIFYSWITCH="RELEASENOTNOTIFY"
###### 场景4：I-SMF发生故障时，AMF重选I-SMF继续会话 
场景说明
NRF检测开关打开，SMF发生故障，AMF通过NRF状态订阅识别出SMF发生故障。 
AMF识别I-SMF发生故障后，设置会话延时释放的相关参数，释放数据会话，不释放IMS会话，且触发UE重选I-SMF继续会话。 
数据规划
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|NRF检测开关|功能打开
查询周期(秒)|修改NF故障检测及处理配置|60
查询个数|修改NF故障检测及处理配置|1
修改SMF容灾策略公共配置|故障延时判断时间(second)|10
会话释放频率(millisecond)|修改SMF容灾策略公共配置|500
单次查询用户个数|修改SMF容灾策略公共配置|60
本地释放后原因值|修改SMF容灾策略公共配置|5GSM Cause: Invalid PDU session identity
I/V-SMF容灾策略配置|I-SMF IMS会话释放开关|会话不释放，重选I-SMF
I-SMF 数据会话释放开关|I/V-SMF容灾策略配置|会话释放
V-SMF IMS会话释放开关|I/V-SMF容灾策略配置|会话释放
V-SMF 数据会话释放开关|I/V-SMF容灾策略配置|会话释放
IMS会话释放通知开关|I/V-SMF容灾策略配置|释放后通知
数据会话释放通知开关|I/V-SMF容灾策略配置|释放后不通知
配置步骤
步骤|说明|操作
---|---|---
1|配置启用通过NRF状态通知检测NF故障和恢复的功能。配置向NRF周期性查询NF故障列表中故障网元节点的时间间隔和每个查询周期查询故障NF的个数。|SET NFDETECPROCCFG:NRFSWITCH="ON",QUERYPERIOD=60,QUERYNUMBER=1
2|配置SMF故障后会话延时释放时间、会话释放频率、单次查询用户个数、本地释放后原因值。|SET SMFDRPOLICYCFG:DELAYTIME=10,RELEASERATE=500,QUERYNUMBER=60,PROCESSAFTERREL="CARRYGSMCAUSE"
3|配置A-SMF容灾策略，配置IMS会话释放开关、数据会话释放开关、IMS会话释放通知开关和数据会话释放通知开关|SET ASMFDRPOLICYCFG:IMSPDURELSWITCH="RELEASE",DATAPDURELSWITCH="RELEASE",IMSRELNOTIFYSWITCH="RELEASENOTIFY",DATARELNOTIFYSWITCH="RELEASENOTNOTIFY"
4|配置I/V-SMF容灾策略配置，配置I-SMF IMS会话释放开关、I-SMF 数据会话释放开关、V-SMF IMS会话释放开关、V-SMF 数据会话释放开关、IMS会话释放通知开关和数据会话释放通知开关|SET IVSMFDRPOLICYCFG:ISMFIMSPDURELSWITCH="NOTRELEASEBUTRESELECT",ISMFDATAPDURELSWITCH="RELEASE",VSMFIMSPDURELSWITCH="RELEASE",VSMFDATAPDURELSWITCH="RELEASE",IMSRELNOTIFYSWITCH="RELEASENOTIFY",DATARELNOTIFYSWITCH="RELEASENOTNOTIFY"
调整特性 :本特性不涉及调整特性。 


测试用例 :



测试项目|SMF故障后的PDU会话建立
---|---
测试目的|SMF故障后的PDU会话建立选择其他SMF
预置条件|AMF通过向NRF订阅SMF的状态以及检测和SMF之间的链路运行。启用通过NRF状态通知检测NF故障及恢复的功能。
测试过程|SMF通知AMF其处于故障状态。用户注册成功，创建PDU会话，向SMF发起会话创建超时。
通过准则|AMF会选择其他SMF，发起会话创建过程。
测试结果|-


测试项目|SMF故障后的PDU会话修改
---|---
测试目的|SMF故障后的PDU会话修改拒绝
预置条件|AMF通过向NRF订阅SMF的状态以及检测和SMF之间的链路运行。启用通过NRF状态通知检测NF故障及恢复的功能。配置SMF容灾策略，包括会话释放延时时间、会话释放频率、单次查询用户个数、本地释放后原因值。
测试过程|用户PDU会话建立成功。对应的SMF通知AMF其处于故障状态。用户发起PDU会话修改过程。
通过准则|AMF向UE回复拒绝，原因值和配置的本地释放后原因值一致。
测试结果|-


测试项目|无I-SMF时，SMF故障后主动释放PDU会话
---|---
测试目的|SMF故障后主动释放PDU会话
预置条件|AMF通过向NRF订阅SMF的状态以及检测和SMF之间的链路运行。配置SMF容灾策略，包括会话释放延时时间、会话释放频率、单次查询用户个数、本地释放后原因值。配置A-SMF容灾策略，包括IMS会话释放开关、数据会话释放开关、IMS会话释放通知开关、数据会话释放通知开关。
测试过程|批量用户PDU会话建立成功。故障SMF通知AMF其处于故障状态。
通过准则|按“会话释放频率”和“单次查询用户个数”周期性进行扫描，故障SMF对应的所有PDU会话都完成本地释放，并对于IMS语音会话，通知UE重建会话。
测试结果|-


测试项目|SMF故障恢复
---|---
测试目的|SMF故障恢复后PDU会话创建可以选择已恢复的SMF
预置条件|AMF通过向NRF订阅SMF的状态以及检测和SMF之间的链路运行。配置AMF向NRF查询NF故障列表的周期和每个查询周期查询故障NF的个数。
测试过程|SMF通知AMF其处于故障后，AMF检测到SMF故障恢复。 用户注册成功，创建PDU会话。
通过准则|AMF会选择恢复的SMF，发起PDU会话创建过程。
测试结果|-


测试项目|SMF本地检测故障
---|---
测试目的|SMF本地检测故障后PDU会话创建可以选择其它的SMF
预置条件|AMF开启SMF本地检测。SMF跟AMF间链路故障，本地检测状态为不可用。
测试过程|AMF创建PDU会话，通过NRF发现多个SMF，其中部分SMF的本地检测状态为故障。用户注册成功，向本地检测状态为正常的SMF成功创建PDU会话。
通过准则|AMF会选择本地检测正常的SMF，发起PDU会话创建过程。
测试结果|-


测试项目|SMF本地检测故障恢复
---|---
测试目的|SMF故障恢复后PDU会话创建可以选择已恢复的SMF
预置条件|AMF开启SMF本地检测。SMF跟AMF间链路故障，本地检测状态为不可用。
测试过程|恢复故障的SMF链路，本地检测该SMF状态正常。用户注册成功，向本地检测状态正常的SMF成功创建PDU会话。
通过准则|AMF会选择本地检测状态恢复的SMF，发起PDU会话创建过程。
测试结果|-


测试项目|I-SMF故障后AMF触发I-SMF重选
---|---
测试目的|I-SMF故障后，AMF重选I-SMF继续会话
预置条件|AMF向NRF订阅SMF的状态以及检测和SMF之间的链路运行。配置SMF容灾策略，包括会话释放延时时间、会话释放频率、单次查询用户个数、本地释放后原因值。配置I/V-SMF容灾策略，故障I-SMF涉及的IMS语音会话释放开关配置为“”会话不释放，重选I-SMF”。
测试过程|批量用户建立包含I-SMF的PDU会话成功。故障I-SMF通知AMF其处于故障状态。
通过准则|按“会话释放频率”和“单次查询用户个数”周期性进行扫描，故障SMF对应的IMS语音会话，不释放当前会话，且触发UE重选I-SMF重建会话。对于连接态用户I-SMF故障后，对于连接态用户，AMF执行N2释放，等待用户主动发起业务请求后，AMF执行I-SMF重选，选择其他可用I-SMF重建会话。对于空闲态用户I-SMF故障后，对于空闲态用户，AMF寻呼用户，触发用户发起业务请求后，AMF执行I-SMF重选，选择其他可用I-SMF重建会话。
测试结果|-




常见问题处理 :无。 
## ZUF-79-21-002 AMF支持UDM容灾 
特性描述 :特性描述 :描述 :定义 :AMF支持UDM容灾是指在主用AUSF/UDM故障后，AMF通过NRF获取AUSF/UDM的故障状态，或者通过链路检测来确定AUSF/UDM故障，AMF在AUSF/UDM发生故障或者向AUSF/UDM请求无响应后，选择其他同组的AUSF/UDM继续处理用户流程，为用户提供不间断服务。
背景知识 :相比传统移动通讯的核心网，5G核心网存在大容量、高度集中等特点，对可靠性要求很高。外在因素（台风、地震、塌方等）和内在因素（设备老化、元件损坏、系统升级、掉电等）都会导致通讯设备业务中断，用户无法继续业务甚至无法接入，导致用户数据丢失、自动操作系统异常等严重后果。因此，需要一个完善强大的容灾系统来保障整个5G系统的稳定运行。 
5G核心网容灾采用跨DC的异地容灾或地理容灾的方式，当其中一个DC发生故障无法提供服务时，另外一个DC可以接管5G核心网业务。这样可以增强网络的处理能力和快速恢复能力，从而将损失降到最低。
应用场景 :###### 场景1：AMF支持在AUSF/UDM无响应时执行重选（非初次选择，为后续流程） 
AMF收到UE的注册更新消息，向AUSF/UDM发起鉴权和注册流程，若AMF向AUSF/UDM发起业务交互时AUSF/UDM无响应，则AMF等待超时后，执行AUSF/UDM重选，选择其他正常的AUSF/UDM进行注册更新等业务流程。 
###### 场景2：AMF支持识别AUSF/UDM的故障及恢复 
AMF通过向NRF订阅AUSF/UDM的状态或者周期检测与AUSF/UDM的链路状态来识别AUSF/UDM的故障与恢复。 
###### 场景3：AMF支持在选择AUSF/UDM时剔除故障态AUSF/UDM 
当AMF检测到AUSF/UDM故障后，UE发起业务流程时，AMF不再选择故障AUSF/UDM，选择同组其他运行正常的AUSF/UDM执行业务流程交互。 
###### 场景4：AMF支持在故障AUSF/UDM恢复后能够继续使用其执行业务 
当AMF检测到AUSF/UDM故障，AMF不再选择故障AUSF/UDM，当AUSF/UDM故障恢复后，AMF通过NRF状态通知或链路检测，确定AUSF/UDM故障恢复，在后续业务流程中继续选择已经恢复的AUSF/UDM。 
客户收益 :受益方|受益描述
---|---
运营商|满足运营商业务功能的需求，在AUSF/UDM发生故障及容灾场景下继续为用户提供业务服务，保障整个网络正常运行，提高5G网络的可靠性。
移动用户|在AUSF/UDM故障容灾场景下， 保障UE的接入，快速恢复用户的业务，保证用户的利益，提高用户满意度。
实现原理 :系统架构 :AMF支持UDM容灾网络架构图如[图1]所示。
图1  UDM容灾框架示意图

###### 涉及的NF 
网元名称|网元作用
---|---
AMF|AUSF/UDM发生故障时， AMF通过NRF订阅通知或自动检测识别AUSF/UDM故障。业务流程中，AMF识别故障的AUSF/UDM，选择同组运行正常的AUSF/UDM执行业务流程。AUSF/UDM故障恢复后，AMF通过NRF订阅通知或自动检测识别AUSF/UDM已经恢复。AMF识别已经恢复的AUSF/UDM，在业务过程中重新选择故障已经恢复的AUSF/UDM执行业务流程。
NRF|AMF向NRF订阅AUSF/UDM的状态，当NRF检测到AUSF/UDM发生故障，向AMF发送AUSF/UDM故障通知。当NRF检测到AUSF/UDM恢复，向AMF发送AUSF/UDM故障恢复通知。
AUSF/UDM|主备AUSF/UDM向NRF注册NF。
(R)AN|无线接入网络，在注册过程中根据UE请求的NSSAI或5G-GUTI选择Initial AMF。
UE|支持5G接入的终端，在注册请求消息中根据NSSAI inclusion mode，提供请求的NSSAI，并完成Allowed NSSAI和Rejected NSSAI的更新。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N12|ZUF-79-19-005 N12
NRF|ZUF-79-19-010 Nnrf
本网元实现 :AMF通过NRF订阅识别AUSF/UDM的故障及恢复。 
AMF通过链路检测支持识别AUSF/UDM的故障及恢复 。 
AMF支持在选择AUSF/UDM时剔除故障态AUSF/UDM。 
AMF支持在故障AUSF/UDM恢复后能够使用其执行业务。 
AMF支持后续流程时，在AUSF/UDM无响应时执行重选。 
业务流程 :AMF通过NRF订阅识别AUSF/UDM的故障及恢复
图2  AMF通过NRF订阅识别AUSFUDM的故障及恢复

AUSF/UDM_1上电后向NRF发起Nnrf_NFManagement_NFRegister消息进行网元注册。 
AUSF/UDM_2上电后向NRF发起Nnrf_NFManagement_NFRegister消息进行网元注册。 
UE发起注册更新，AMF向NRF请求发现AUSF/UDM后，向NRF发送Nnrf_NFManagement_NFStatusSubscribe消息订阅AUSF/UDM的状态。 
当AUSF/UDM_1发生故障，NRF通过链路检测发现故障。 
NRF根据状态订阅列表，向AMF发送Nnrf_NFManagement_NFStatusNotify通知AUSF/UDM_1发生故障，AMF将AUSF/UDM_1放入NF故障列表。 
当AUSF/UDM_1故障恢复，NRF通过链路检测发现故障已经恢复。 
NRF根据状态订阅列表，向AMF发送Nnrf_NFManagement_NFStatusNotify通知AUSF/UDM_1故障已经恢复，AMF将AUSF/UDM_1从NF故障列表移除。 
AMF通过链路检测支持识别AUSF/UDM的故障及恢复
图3  AMF通过链路检测支持识别AUSFUDM的故障及恢复

AMF向NRF请求或本地发现AUSF/UDM_1后，本地状态检测开关打开情况下，AMF实时监测AUSF/UDM_1链路状态；当AUSF/UDM_1链路故障时，AMF自动识别，并将AUSF/UDM_1添加到NF故障列表。 
AUSF/UDM_1链路故障期间，AMF收到UE注册更新，AMF选择状态正常的AUSF/UDM_2进行业务流程交互。 
当AUSF/UDM_1链路恢复正常，AMF自动识别AUSF/UDM_1故障恢复，并将AUSF/UDM_1从NF故障列表移除。 
AMF支持在选择AUSF/UDM时剔除故障态AUSF/UDM
图4  AMF支持在选择AUSF/UDM时剔除故障态AUSF/UDM

AMF收到UE的初始注册或注册更新Registration Request消息。判断需要向AUSF/UDM发起鉴权请求和注册更新。 
AMF执行AUSF发现选择过程，选择AUSF/UDM_1。 
AMF向AUSF/UDM_1获取了鉴权信息后，进行Authentication/Security过程，完成鉴权加密。 
AMF向UDM发起注册更新前，进行UDM选择，AMF根据SUPI、NfGroupId等信息查询UDM网元信息，并根据优先级权重选择了AUSF/UDM_1。 
AMF向选择的AUSF/UDM_1发送注册请求消息，注册更新成功。 
AMF收到注册成功响应后，向AUSF/UDM_1发起Nudm_SDM_Get获取签约信息成功。 
AMF同时向AUSF/UDM_1发起Nudm_SDM_Subscribe消息订阅成功。 
AMF后续收到UE的Registration Request注册更新请求，判断需要发起鉴权过程。 
AMF执行AUSF发现选择过程，根据SUPI、NfGroupId等信息查询AUSF网元信息，剔除故障AUSF/UDM_1，选择AUSF/UDM_2。 
AMF向AUSF/UDM_2获取了鉴权信息后，进行Authentication/Security过程，完成鉴权加密。 
AMF向UDM发起注册更新前，进行UDM选择，AMF根据SUPI、NfGroupId等信息查询UDM网元信息，剔除故障AUSF/UDM_1，选择AUSF/UDM_2。 
AMF向选择的AUSF/UDM_2发送注册请求消息，注册更新成功。 
AMF收到注册成功响应后，向AUSF/UDM_2发起Nudm_SDM_Get获取签约信息成功。 
AMF同时向AUSF/UDM_2发起Nudm_SDM_Subscribe消息订阅成功。 
AMF支持故障台AUSF/UDM恢复后使用其继续执行业务
图5  AMF支持故障台AUSF/UDM恢复后使用其继续执行业务

AMF收到UE的初始注册或注册更新Registration Request消息。判断需要向AUSF/UDM发起鉴权请求和注册更新。 
AMF执行AUSF发现选择过程，根据SUPI、NfGroupId等信息查询AUSF网元信息，剔除故障AUSF/UDM_1，选择AUSF/UDM_2。 
AMF向AUSF/UDM_2获取了鉴权信息后，进行Authentication/Security过程，完成鉴权加密。 
AMF向UDM发起注册更新前，进行UDM选择，AMF根据SUPI、NfGroupId等信息查询UDM网元信息，剔除故障AUSF/UDM_1，选择AUSF/UDM_2。 
AMF向选择的AUSF/UDM_2发送注册请求消息，注册更新成功。 
AMF收到注册成功响应后，向AUSF/UDM_2发起Nudm_SDM_Get获取签约信息成功。 
AMF同时向AUSF/UDM_2发起Nudm_SDM_Subscribe消息订阅成功。 
AMF通过NRF或链路检测发现AUSF/UDM_1已经恢复，将AUSF/UDM_1从NF故障列表移除，后续收到UE的Registration Request注册更新请求。 
AMF执行AUSF发现选择过程，根据SUPI、NfGroupId等信息查询AUSF网元信息，根据优先级权重选择故障恢复的AUSF/UDM_1。 
AMF向AUSF/UDM_1获取了鉴权信息后，进行Authentication/Security过程，完成鉴权加密。 
AMF向UDM发起注册更新前，进行UDM选择，AMF根据SUPI、NfGroupId等信息查询UDM网元信息，根据优先级权重选择故障恢复的AUSF/UDM_1。 
AMF向选择的AUSF/UDM_1发送注册请求消息，注册更新成功。 
AMF收到注册成功响应后，向AUSF/UDM_1发起Nudm_SDM_Get获取签约信息成功。 
AMF同时向AUSF/UDM_1发起Nudm_SDM_Subscribe消息订阅成功。 
AMF支持后续流程中UDM无响应时执行重选
图6  AMF支持后续流程中UDM无响应时执行重选

AMF收到UE的初始注册或注册更新Registration Request消息。判断需要向AUSF/UDM发起鉴权请求和注册更新。 
AMF进行UDM服务发现选择。 
AMF向选择的AUSF/UDM_1发送注册请求消息，注册更新成功。 
AMF收到注册成功响应后，向AUSF/UDM_1发起Nudm_SDM_Get获取签约信息，AUSF/UDM_1无响应。 
AMF向AUSF/UDM_1发送Nudm_SDM_Subscribe消息进行订阅，AUSF/UDM_1无响应。 
AMF没有收到AUSF/UDM_1响应消息，根据运营商开关控制执行UDM重选。 
AMF重新选择AUSF/UDM_2，向AUSF/UDM_2发起Nudm_SDM_Get获取签约信息，获取签约信息成功。 
AMF同时向AUSF/UDM_2发送Nudm_SDM_Subscribe订阅请求成功。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性的链路检测（也称本地检测）功能只适用于与对端NF直连的场景，非直连（例如间接通信）的场景不适用。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2
TS 23.502|3GPP|3GPP TS 23.502 Technical Specification Group Services and System Aspects; Procedures for the 5G System; Stage 2
TS 24007|3GPP|Mobile radio interface signalling layer 3
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS);
TS 38.413|3GPP|NG Application Protocol (NGAP)
TS 29.518|3GPP|5G System; Access and Mobility Management Services
TS 29.510|3GPP|5G System: Network function repository services
TS 29.509|3GPP|5G System; Authentication Server Services
RFC|RFC7231|Hypertext Transfer Protocol
特性能力 :该特性涉及的链路检测（也称本地检测，即HTTP PING检测）功能，AMF整机支持最多同时检测4000个NF服务，最多同时检测6000个IP地址。 
名称|指标
---|---
AMF链路检测支持的最大同时检测NF服务个数|4000
AMF链路检测支持的最大同时检测IP个数|6000
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.20|新增功能：通过HTTP PING方式的本地检测功能。
01|V7.20.20|首次发布。
License要求 :该特性为AUSF/UDM容灾的基本特性，无需License支持。 
###### 对其他NF的要求 
UE|gNodeB|NRF|AUSF/UDM
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :工程规划上，需要AUSF/UDM进行容灾备份，如主备容灾备份，AMF配置AUSF/UDM故障重选策略。 
O&M相关 :命令 :配置项参见下表。 
配置项|命令
---|---
NF故障检测及处理配置|SET NFDETECPROCCFG
SHOW NFDETECPROCCFG|NF故障检测及处理配置
UDM容灾重选配置|SET UDMDRCFG
SHOW UDMDRCFG|UDM容灾重选配置
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :为支持AUSF/UDM容灾功能，需要配置NF故障检测，根据需要开启故障检测开关，并配置UDM故障后的容灾配置。 
AUSF容灾功能仅包括NF故障检测部分，即只支持NRF故障检测、本地检测AUSF是否故障，并在发现选择AUSF局向时，剔除故障局向，与正常局向进行交互。 
NF故障检测配置： 
开启AUSF/UDM本地检测开关，配置AUSF/UDM本地检测范围及老化时长。 
UDM容灾配置（专指UDM容灾配置，不涉及AUSF）： 
UDM无响应重选开关：用于设置当跟UDM交互失败时，是否执行重选UDM功能。 
UDM重用开关：用于设置决定每次操作成功后，AMF是否保存UDM信息用于下次交互。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
如果需要开启本地检测，需要AMF与AUSF、UDM保持直连。 
配置过程 :根据AUSF状态检测方式，分别配置通过NRF状态通知检测和本地检测。 
配置通过NRF状态通知检测执行SET NFDETECPROCCFG命令，开启通过NRF状态通知检测NF故障及恢复的功能。 
配置本地检测执行SET NFDETECPROCCFG命令，开启UDM本地检测功能。 
根据UDM状态检测方式，分别配置通过NRF状态通知检测和本地检测。 
配置通过NRF状态通知检测执行SET NFDETECPROCCFG命令，开启通过NRF状态通知检测NF故障及恢复的功能。执行SET UDMDRCFG命令，修改UDM容灾重选配置。 
配置本地检测执行SET NFDETECPROCCFG命令，开启UDM本地检测功能。执行SET UDMDRCFG命令，修改UDM容灾重选配置。 
配置实例 :###### NRF状态通知或者链路检测识别出AUSF发生故障和恢复 
场景说明
NRF检测开关打开，AUSF发生故障，AMF通过NRF状态通知或者链路检测识别出AUSF发生故障。 
AMF通过NRF状态通知或者链路检测识别AUSF发生故障后，上报告警。 
AUSF发生故障后恢复，恢复告警。 
数据规划
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|NRF检测开关|功能打开
查询周期(秒)|修改NF故障检测及处理配置|60
查询个数|修改NF故障检测及处理配置|1
配置步骤
步骤|说明|操作
---|---|---
1|开启通过NRF状态通知检测NF故障和恢复的功能。|SET NFDETECPROCCFG:NRFSWITCH="ON",QUERYPERIOD=60,QUERYNUMBER=1
###### 本地检测识别出AUSF发生故障和恢复 
场景说明
本地检测开关打开，AUSF发生故障，AMF通过本地检测识别出AUSF发生故障。 
AMF通过本地检测识别AUSF发生故障后，再次跟AUSF交互时会发现并选择其它AUSF。 
AUSF发生故障后恢复，AMF通过本地局向状态检测通知识别出故障AUSF已经恢复。 
数据规划
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|AUSF本地检测开关|功能打开
AUSF/UDM本地检测范围|修改NF故障检测及处理配置|选择后检测
NRF发现检测老化时间|修改NF故障检测及处理配置|10080
本地发现检测老化时间|修改NF故障检测及处理配置|2160
配置步骤
步骤|说明|操作
---|---|---
1|开启通过本地检测NF故障和恢复的功能。|SET NFDETECPROCCFG:AUSFLOCALSWITCH="ON",AUSFUDMDETECSCOPE="AFTERSELECT",NRFDISCAGINGTIME=10080,LOCALDISCAGINGTIME=2160
###### NRF状态通知或者链路检测识别出UDM发生故障和恢复 
场景说明
NRF检测开关打开，UDM发生故障，AMF通过NRF状态通知或者链路检测识别出UDM发生故障。 
AMF通过NRF状态通知或者链路检测识别UDM发生故障后，设置定时器，延时确认UDM故障。确认UDM故障后，再次跟UDM交互时会发现并选择其它UDM。 
UDM发生故障后恢复，AMF通过NRF状态通知或者链路检测识别出故障UDM已经恢复。 
数据规划
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|NRF检测开关|功能打开
查询周期(秒)|修改NF故障检测及处理配置|60
查询个数|修改NF故障检测及处理配置|1
修改容灾重选配置|UDM无响应重选开关|无响应重选
UDM重用开关|修改容灾重选配置|重用
配置步骤
步骤|说明|操作
---|---|---
1|开启通过NRF状态通知检测NF故障和恢复的功能。|SET NFDETECPROCCFG:NRFSWITCH="ON",QUERYPERIOD=60,QUERYNUMBER=1
2|配置容灾重选参数。|SET UDMDRCFG:UDMRESELECTSWITCH="SUPTUDMRESELECT",UDMREUSESWITCH="SUPTUDMREUSE"
###### 本地检测识别出UDM发生故障和恢复 
场景说明
本地检测开关打开，UDM发生故障，AMF通过本地检测识别出UDM发生故障。 
AMF通过本地检测识别UDM发生故障后，再次跟UDM交互时会发现并选择其它UDM。 
UDM发生故障后恢复，AMF通过本地局向状态检测通知识别出故障UDM已经恢复。 
数据规划
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|UDM本地检测开关|功能打开
AUSF/UDM本地检测范围|修改NF故障检测及处理配置|选择后检测
NRF发现检测老化时间|修改NF故障检测及处理配置|10080
本地发现检测老化时间|修改NF故障检测及处理配置|2160
修改UDM容灾重选配置|UDM无响应重选开关|无响应重选
UDM重用开关|修改UDM容灾重选配置|重用
配置步骤
步骤|说明|操作
---|---|---
1|开启通过本地检测NF故障和恢复的功能。|SET NFDETECPROCCFG:UDMLOCALSWITCH="ON",AUSFUDMDETECSCOPE="AFTERSELECT",NRFDISCAGINGTIME=10080,LOCALDISCAGINGTIME=2160
2|配置容灾重选参数。|SET UDMDRCFG:UDMRESELECTSWITCH="SUPTUDMRESELECT",UDMREUSESWITCH="SUPTUDMREUSE"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|UDM容灾时重新发现
---|---
测试目的|测试UDM容灾时重新发现其它UDM。
预置条件|UE向主用UDM注册成功。主用UDM发生故障。
测试过程|UE发起移动注册。
通过准则|AMF发起NRF查询UDM。AMF向备用UDM发起交互。
测试结果|–
测试项目|UDM重用
---|---
测试目的|测试UDM重用。
预置条件|UE向主用UDM注册成功。
测试过程|UE发起移动注册。
通过准则|AMF直接与主用UDM交互。
测试结果|–
测试项目|UDM重用，故障后重选
---|---
测试目的|测试UDM重用，并在主用UDM故障后重选其它UDM。
预置条件|UE向主用UDM注册成功。主用UDM发生故障。
测试过程|UE发起移动注册。
通过准则|AMF向主用UDM发起交互。AMF与主用UDM交互失败。AMF发起NRF查询UDM。AMF向备用UDM发起交互。
测试结果|–
测试项目|UDM重用，故障后不重选
---|---
测试目的|测试UDM重用，并在主用UDM故障后交互失败。
预置条件|UE向主用UDM注册成功。主用UDM发生故障。
测试过程|UE发起移动注册。
通过准则|AMF向主用UDM发起交互。AMF与主用UDM交互失败，不再尝试其它UDM。
测试结果|–
测试项目|NRF状态通知检测UDM故障，上报告警
---|---
测试目的|测试UDM通过NRF状态通知检测为故障，并上报告警。
预置条件|AMF与UDM交互，可以与UDM服务中的UECM、SDM两种中的任一种服务交互或同时交互。AMF向NRF发现多个UDM，其中部分UDM通过NRF状态检测为不可用。
测试过程|AMF收到NRF的UDM状态通知，UDM状态为故障。
通过准则|UDM状态为故障，上报UDM不可达告警。
测试结果|–
测试项目|NRF状态通知检测NF故障，与AUSF交互选择状态正常AUSF
---|---
测试目的|测试AUSF通过NRF状态通知检测为故障，上报告警。
预置条件|AMF在注册流程中对UE进行鉴权，与AUSF交互。AMF向NRF发现多个AUSF，其中部分AUSF通过NRF状态通知检测为不可用。
测试过程|AMF收到NRF的AUSF状态通知，AUSF状态为故障。
通过准则|AUSF状态为故障，上报AUSF不可达告警。
测试结果|–
测试项目|本地检测NF故障，与UDM交互选择状态正常UDM
---|---
测试目的|测试UDM通过本地检测为故障，AMF在与UDM交互时，选择状态正常的UDM。
预置条件|AMF与UDM交互，可以与UDM服务中的UECM、SDM两种中的任一种服务交互或同时交互。AMF向NRF发现多个UDM，其中部分UDM通过本地检测为不可用。
测试过程|UE发起移动注册，与UDM发生交互。
通过准则|AMF向本地检测状态正常的UDM发起交互。
测试结果|–
测试项目|本地检测NF故障，与AUSF交互选择状态正常的AUSF
---|---
测试目的|测试AUSF通过本地检测为故障，AMF在与AUSF交互时，选择状态正常的AUSF。
预置条件|AMF在注册流程中对UE进行鉴权，与AUSF交互。AMF向NRF发现多个AUSF，其中部分AUSF通过本地检测为不可用。
测试过程|UE发起移动注册。
通过准则|AMF向本地检测状态正常的AUSF发起交互。
测试结果|–
常见问题处理 :无。 
## ZUF-79-21-003 AMF支持PCF容灾 
特性描述 :特性描述 :描述 :定义 :AMF支持PCF容灾功能是指在PCF发生故障后，AMF根据PCF注册到NRF的网元优先级和容量负荷选择备用的PCF，并与新选择的PCF进行业务交互，满足运营商业务功能的需求，在PCF发生故障及容灾场景下继续为用户提供不间断的业务服务。
背景知识 :相比传统移动通讯的核心网，5G核心网存在大容量、高度集中等特点，对可靠性要求很高。外在因素（台风、地震、塌方等）和内在因素（设备老化、元件损坏、系统升级、掉电等）都会导致通讯设备业务中断，用户无法继续业务甚至无法接入，导致用户数据丢失、自动操作系统异常等严重后果。因此，需要一个完善强大的容灾系统来保障整个5G系统的稳定运行。 
5G核心网容灾采用跨DC的异地容灾或地理容灾的方式，当其中一个DC发生故障无法提供服务时，另外一个DC可以接管5G核心网业务。这样可以增强网络的处理能力和快速恢复能力，从而将损失降到最低。
PCF容灾支持以下几种方式，当一个PCF故障后，另一个PCF或POOL下其他PCF节点可以接管业务，支持所有业务流程的处理。 
1+1互备容灾方式。 
1+1主备容灾方式。 
POOL容灾方式。 
应用场景 :###### 场景1：AMF支持识别PCF的故障及恢复 
AMF上电成功，向NRF订阅PCF的状态或周期检测与PCF间的链路状态，当PCF发生故障或故障恢复时，AMF可以通过NRF状态通知或链路检测确定。 
###### 场景2：AMF支持在PCF故障后，后续业务流程重选PCF（非初次选择，为后续流程） 
AMF接收到UE注册更新请求等业务消息，需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并进行业务交互。当PCF发生故障，后续收到UE的业务流程，AMF进行PCF重选，选择正常的PCF进行业务交互。 
###### 场景3：AMF支持在故障PCF恢复后业务倒回 
AMF接收到UE注册更新请求等业务消息，需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并进行业务交互。当PCF发生故障，后续与故障的PCF交互失败后，AMF进行PCF重选，选择正常的PCF进行业务交互。当故障的 PCF恢复后，AMF根据运营商策略，将与用户交互的PCF切换回原来PCF。 
###### 场景4：AMF支持PCF倒换后备份PCF主动下发消息处理 
AMF接收到UE注册更新请求等业务消息，需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并进行业务交互。当PCF发生故障，备份PCF向AMF下发策略更新等业务流程时，AMF无论是否获知PCF发生故障，都能接收备份PCF初始下发的消息，正常处理业务流程。 
###### 场景5：AMF正常运行，PCF故障，AMF重选PCF时接收到307/308响应处理 
AMF接收到UE注册更新请求等业务消息，需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并进行业务交互。当PCF发生故障，后续AMF与PCF进行业务交互时，AMF重选PCF，并与此PCF进行业务交互，当收到PCF的307/308响应时，解析响应消息中携带的new PCF信息，并向此new PCF重新发送请求消息，后续与此new PCF交互。 
###### 场景6：PCF故障，AMF重选PCF后，新PCF再次发生故障 
AMF接收到UE注册更新请求等业务消息，需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并进行业务交互。当PCF发生故障，后续AMF与PCF进行业务交互时，AMF重选PCF，并与选择后的PCF进行业务交互，后续重选的PCF再次发生故障， 在POOL组网下，AMF后续业务再次发生PCF重选，保证业务连续性。 
客户收益 :受益方|受益描述
---|---
运营商|满足运营商业务功能的需求，在PCF发生故障及容灾场景下继续为用户提供业务服务，保障整个网络正常运行，提高5G网络的可靠性。
移动用户|在PCF故障容灾场景下， 保障UE的接入和业务策略，为用户提供不间断业务服务，提高用户满意度。
实现原理 :系统架构 :AMF支持PCF容灾网络架构图如[图1]所示。
图1  PCF容灾框架示意图

AMF支持PCF容灾示意图如[图2]所示。
图2  PCF故障及容灾示意图

###### 涉及的NF 
网元名称|网元作用
---|---
AMF|PCF发生故障时， AMF通过NRF订阅通知或链路检测识别PCF故障。业务流程中，AMF识别故障的PCF，选择同组运行正常的PCF执行业务流程。PCF故障恢复后，AMF通过NRF和链路检测识别PCF已经恢复。AMF识别PCF故障恢复，并支持在故障PCF恢复后将业务倒回。
NRF|AMF向NRF订阅PCF的状态，NRF检测到PCF故障，向AMF发送PCF故障通知。当NRF检测到PCF故障恢复，向AMF发送PCF故障恢复通知。
PCF|PCF向NRF注册NF。NRF监测与PCF的网络运行。由NRF通知AMF订阅的PCF的状态，AMF进行PCF重选。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N15|ZUF-79-19-007 N15
NRF|ZUF-79-19-010 Nnrf
本网元实现 :PCF发生故障，AMF后续业务进行PCF重选。 
PCF发生故障，AMF后续收到重选后的PCF携带307/308响应消息处理。 
PCF故障恢复，AMF支持将与PCF业务交互倒回原来PCF。 
业务流程 :PCF发生故障，AMF后续业务进行PCF重选
图3  PCF发生故障，AMF后续业务进行PCF重选

AMF接收到UE的N1 Message（注册更新请求等业务消息），需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并与选择的PCF_1进行业务交互。 
AMF向PCF_1发送Npcf_AMPolicyControl_Create消息。 
AMF收到PCF_1的Npcf_AMPolicyControl_Create Rsp消息，存储策略信息。 
后续AMF进行正常的注册更新流程。 
UE后续向AMF发送N1 Message（注册更新请求等业务消息），AMF判断需要向PCF发起策略更新。 
AMF检查PCF_1是否存在故障，若故障，则执行[7b]，若正常，则执行[7a]。
AMF根据PCF_1状态进行业务处理： 
PCF_1正常，直接发送Npcf_AMPolicyControl_Update消息给PCF_1，进行策略更新流程。 
PCF_1发生故障，根据运营商策略进行PCF重选。开关打开，进行PCF重选，重选PCF后执行[8b]；开关关闭，当前业务流程失败。
AMF进行业务处理： 
AMF向PCF_1发送Npcf_AMPolicyControl_Update消息后，若PCF无响应，则PCF流程流程失败，对于涉及操作策略的流程，继续使用现有策略数据进行处理。 
AMF重选PCF后，向新的PCF_x发送Npcf_AMPolicyControl_Update消息进行策略更新。 
新的PCF_x向AMF返回Npcf_AMPolicyControl_Update RSP消息，AMF使用新的策略进行业务处理。后续其他流程正常处理。 
PCF发生故障，AMF后续收到重选后的PCF携带307/308响应消息
AMF接收到UE的N1 Message（注册更新请求等业务消息），需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF，并与选择的PCF_1进行业务交互。 
AMF向PCF_1发送Npcf_AMPolicyControl_Create消息。 
AMF收到PCF_1的Npcf_AMPolicyControl_Create Rsp消息，存储策略信息。 
后续AMF进行正常的注册更新流程。 
UE后续向AMF发送N1 Message（注册更新请求等业务消息），AMF判断需要向PCF发起策略更新。 
AMF检查PCF_1故障，根据运营商策略进行PCF重选，选择新的PCF_x进行业务流程交互。 
AMF向PCF_x发送Npcf_AMPolicyControl_Update消息. 
PCF_x返回POST Response消息，响应码为307/308 redirect。 
AMF根据HTTP消息中携带的Location信息，获得重定向的PCR_2。 
AMF向PCF_2发送Npcf_AMPolicyControl_Create消息。 
AMF收到PCF_2的Npcf_AMPolicyControl_Create Rsp消息，存储策略信息。后续AMF策略处理流程，AMF与新的PCF_2进行正常交互。 
PCF故障恢复后，AMF恢复选择故障恢复的PCF执行业务流程
图4  PCF故障恢复后，AMF恢复选择故障恢复的PCF执行业务流程

AMF接收到UE的N1 Message（注册更新请求等业务消息），需要执行AMF策略关联建立或修改时，首先通过NRF或本地策略发现选择PCF。 
AMF选择PCF_1，完成AMF Association Establishment/Modification过程。  
UE后续向AMF发送N1 Message（注册更新请求等业务消息），AMF判断需要向PCF发起策略更新。 
AMF检查PCF_1故障，根据运营商策略进行PCF重选，选择新的PCF_2进行业务流程交互。 
AMF向PCF_2发送Npcf_AMPolicyControl_Update消息。 
PCF_2返回Npcf_AMPolicyControl_Update Response响应消息，PCF策略更新流程成功。 
后续UE向AMF发送N1 Message（注册更新请求等业务消息），AMF判断需要向PCF发起策略更新。 
AMF检查PCF_1故障已经恢复，根据运营商策略进行判断： 
倒回方式  --  AMF更新用户业务交互的PCF_2局向为原PCF_1。 
故障恢复不倒回 -- AMF与PCF处理业务流程时，继续向PCF_2局向发起策略更新流程。 
AMF后续向恢复的PCF_1发送Npcf_AMPolicyControl_Update消息，处理策略更新流程。 
故障恢复的PCF_1返回Npcf_AMPolicyControl_Update Response响应消息，PCF策略更新流程成功。后续其他流程正常处理。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性的链路检测（也称本地检测）功能只适用于与对端NF直连的场景，非直连（例如间接通信）的场景不适用。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 29.500|5G System;Technical Realization of Service Based Architecture
TS 29.501|3GPP|5G System;Principles and Guidelines for Services Definition
TS 29.507|3GPP|Access and Mobility Policy Control Service
TS 29.525|3GPP|5G System; UE Policy Control Service
TS 29.518|3GPP|5G System; Access and Mobility Management Services
TS 29.510|3GPP|5G System: Network function repository services
TS 29.509|3GPP|5G System; Authentication Server Services
RFC|RFC7231|Hypertext Transfer Protocol
RFC3986|RFC|Uniform Resource Identifier (URI)
特性能力 :该特性涉及的链路检测（也称本地检测，即HTTP PING检测）功能，AMF整机支持最多同时检测4000个NF服务，最多同时检测6000个IP地址。 
名称|指标
---|---
AMF链路检测支持的最大同时检测NF服务个数|4000
AMF链路检测支持的最大同时检测IP个数|6000
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.30|新增通过HTTP PING方式的本地检测功能。
01|V7.20.20|首次发布。
License要求 :该特性为PCF容灾的基本特性，无需License支持。 
###### 对其他NF的要求 
UE|gNodeB|PCF|NRF
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :工程规划上，需要PCF进行容灾备份，如主备、POOL等备份方式，AMF配置PCF故障重选策略。 
O&M相关 :命令 :配置项参见下表。 
配置项|命令
---|---
PCF容灾策略配置|SET PCFDRPOLICYCFG
SHOW PCFDRPOLICYCFG|PCF容灾策略配置
NF故障检测及处理配置|SET NFDETECPROCCFG
SHOW NFDETECPROCCFG|NF故障检测及处理配置
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :为支持PCF容灾功能，需要配置NF故障检测功能，根据需要开启故障检测开关，并配置PCF故障后的容灾配置。 
PCF容灾功能包括NF故障检测部分，即支持NRF故障检测、本地检测PCF是否故障，并在发现选择PCF局向时，剔除故障局向，与正常局向进行交互。 
通过相关配置，实现在以下场景中能够继续执行业务流程的功能。 
当AMF和PCF业务交互异常，如PCF发生故障，或是链路故障导致暂时通讯失败时，AMF重选PCF，从而保证业务能够继续执行。 
当PCF连续发生故障时，AMF也可以决策是否可以连续重选PCF。当故障PCF恢复时，AMF亦可决策是否需要将PCF业务倒回至原来的PCF。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
开启本地检测需要AMF与PCF保持直连。 
配置过程 :###### PCF故障时，AMF是否执行重选PCF功能 
执行命令 [SET PCFDRPOLICYCFG]，设置PCF故障重选开关，当该开关打开时，主用PCF故障时，AMF尝试跟其它PCF交互。
设置 PCF恢复后启用方式参数。当主用PCF已经恢复后，UE倒回到主用PCF进行交互。 
设置支持连续故障参数。当主用PCF故障，选择备用PCF，备用PCF又故障了，再次选择其它PCF 。 
###### 根据PCF状态检测方式，分别配置通过NRF状态通知检测和本地检测 
配置通过NRF状态通知检测：执行[SET NFDETECPROCCFG]命令，开启通过NRF状态通知检测NF故障及恢复的功能。
配置本地检测：执行[SET NFDETECPROCCFG]命令，开启PCF本地检测功能。
配置实例 :场景说明 :场景一：处理PCF容灾，可以根据本功能的开关处理不同PCF容灾场景。 
场景二：NRF状态通知或者链路检测识别出PCF发生故障和恢复。NRF检测开关打开，PCF发生故障，AMF通过NRF状态通知或者链路检测识别出PCF发生故障。AMF通过NRF状态通知或者链路检测识别PCF发生故障后，上报告警。PCF发生故障后恢复，恢复告警。 
场景三：本地检测识别出PCF发生故障和恢复本地检测开关打开，PCF发生故障，AMF通过本地检测识别出PCF发生故障。AMF通过本地检测识别PCF发生故障后，再次跟PCF交互时会发现并选择其它PCF。PCF发生故障后恢复，AMF通过本地局向状态检测通知识别出故障PCF已经恢复。 
数据规划 :配置名称|参数项|取值
---|---|---
PCF容灾策略配置|PCF故障重选开关|PCF故障重选|PCF故障不重选
PCF恢复后启用方式|PCF容灾策略配置|PCF恢复后启用方式为话务倒回|PCF恢复后启用方式为新选择使用
支持连续故障|PCF容灾策略配置|支持连续故障|不支持连续故障
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|NRF检测开关|ON
查询周期(秒)|修改NF故障检测及处理配置|60
查询个数|修改NF故障检测及处理配置|1
NRF发现检测老化时间(分)|修改NF故障检测及处理配置|10080
配置项|参数|取值
---|---|---
修改NF故障检测及处理配置|PCF本地检测开关|ON
PCF本地检测范围|修改NF故障检测及处理配置|选择后检测
NRF发现检测老化时间(分)|修改NF故障检测及处理配置|10080
本地发现检测老化时间(分)|修改NF故障检测及处理配置|2160
配置步骤 :步骤|配置说明|命令示例
---|---|---
1|设置PCF故障重选开关为：PCF故障重选|SET PCFDRPOLICYCFG:PCFRESELESWITCH="SWITCH_ON"
2|设置PCF恢复后启用方式为：PCF恢复后启用方式为话务倒回|SET PCFDRPOLICYCFG:PCFENABLEMODE="REVERSE"
3|设置支持连续故障为：支持连续故障|SET PCFDRPOLICYCFG:SUPPORTCONFAULT="SUPPORTCONFAULT"
步骤|说明|操作
---|---|---
1|开启通过NRF状态通知检测NF故障和恢复的功能。|SET NFDETECPROCCFG:NRFSWITCH="ON",QUERYPERIOD=60,QUERYNUMBER=1,NRFDISCAGINGTIME=10080
步骤|说明|操作
---|---|---
1|开启通过本地检测NF故障和恢复的功能。|SET NFDETECPROCCFG:PCFLOCALSWITCH="ON",PCFDETECSCOPE="AFTERSELECT",NRFDISCAGINGTIME=10080,LOCALDISCAGINGTIME=2160
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|PCF容灾时重新发现
---|---
测试目的|测试PCF容灾时重新发现其它PCF。
预置条件|UE向主用PCF建立成功。主用PCF发生故障。配置 PCF故障重选开关为AMF重选新的PCF
测试过程|UE发生移动注册。
通过准则|AMF发起NRF查询PCF。AMF向备用PCF发起交互。
测试结果|–
测试项目|PCF恢复后启用容灾倒回
---|---
测试目的|测试主用PCF恢复后能自动倒回到主用PCF。
预置条件|主用PCF发生故障，并且AMF已重选到备用PCF后，主用PCF又恢复。配置PCF恢复后启用方式为启用容灾倒回。
测试过程|UE发生移动注册。
通过准则|AMF直接跟主用PCF交互，完成主用PCF的恢复倒回。
测试结果|–
测试项目|PCF恢复后不支持启用容灾倒回
---|---
测试目的|测试主用PCF恢复后，不支持容灾倒回，保持继续使用备用PCF，不倒回主用PCF。
预置条件|主用PCF发生故障，并且AMF已重选到备用PCF后，主用PCF又恢复。配置PCF恢复后启用方式为不支持启用容灾倒回。
测试过程|UE发生移动注册。
通过准则|AMF继续使用备用PCF，不倒回主用PCF。
测试结果|–
测试项目|主用PCF故障，选择备用后，备用PCF又故障，再次发现其它PCF
---|---
测试目的|测试备用PCF故障后，还能继续发现其它PCF。
预置条件|UE向主用PCF建立成功。主用PCF发生故障，选择备用PCF。备用PCF又发生故障。配置支持连续故障为支持。
测试过程|UE发生移动注册。
通过准则|AMF再次发现PCF。AMF向其它备用PCF发起交互。
测试结果|–
测试项目|NRF状态通知检测NF故障，与PCF交互选择状态正常PCF
---|---
测试目的|测试PCF通过NRF状态通知检测为故障，上报告警。
预置条件|AMF在注册流程中PCF建立，与PCF交互。AMF向NRF发现多个PCF，其中部分PCF通过NRF状态通知检测为不可用。
测试过程|AMF收到NRF的PCF状态通知，PCF状态为故障。注册流程中选择状态正常的PCF。
通过准则|PCF状态为故障，上报PCF不可达告警。注册流程中PCF建立成功。
测试结果|–
测试项目|本地检测NF故障，与PCF交互选择状态正常PCF
---|---
测试目的|测试PCF通过本地检测为故障，上报告警。
预置条件|AMF在注册流程中PCF建立，与PCF交互。AMF本地发现多个PCF，其中部分PCF通过本地检测为不可用。
测试过程|通过本地检测为不可用。注册流程中选择状态正常的PCF。
通过准则|PCF状态为故障，上报PCF不可达告警。注册流程中PCF建立成功。
测试结果|–
常见问题处理 :无。 
## ZUF-79-21-004 AMF支持NRF容灾 
特性描述 :特性描述 :描述 :定义 :AMF支持NRF容灾功能是指AMF能够在一台NRF故障后，继续使用另一台NRF执行业务流程，保障网络服务的可用性。 NRF支持主备或互备容灾方式。 
背景知识 :相比传统移动通讯的核心网，5G核心网存在大容量、高度集中等特点，对可靠性要求很高。外在因素（台风、地震、塌方等）和内在因素（设备老化、元件损坏、系统升级、掉电等）都会导致通讯设备业务中断，用户无法继续业务甚至无法接入，导致用户数据丢失、自动操作系统异常等严重后果。因此，需要一个完善强大的容灾系统来保障整个5G系统的稳定运行。 
5G核心网容灾采用跨DC的异地容灾或地理容灾的方式，当其中一个DC发生故障无法提供服务时，另外一个DC可以接管5G核心网业务。这样可以增强网络的处理能力和快速恢复能力，从而将损失降到最低。
为提高系统可靠性，核心网的业务处理通常需要提供NF冗余机制。作为5G网络的核心NF，NRF同样需要具备冗余备份机制，其他NF如AMF，SMF等需要支持NRF的容灾功能。 
应用场景 :###### 场景1：AMF支持NRF互备容灾 
此场景下，主用NRF和备用NRF同时处理业务。 
###### 场景2：AMF支持NRF主备容灾 
此场景下，正常情况只有主用NRF处理业务，备用NRF不处理业务。主用故障后，备用NRF转为主用NRF并开始处理业务。 
###### 场景3：AMF支持NRF均故障的处理 
此场景下，主用NRF和备用NRF均已故障。 
客户收益 :受益方|受益描述
---|---
运营商|提高系统运行可靠性，降低系统运行风险。为用户提供更好的网络服务，获得更高的用户满意度。
移动用户|在网络中NRF发生故障的情况下，用户业务能够得到快速恢复。
实现原理 :系统架构 :AMF支持NRF容灾功能网络架构如[图1]、[图2]、[图3]所示。
根据NRF容灾方式的不同（互备或主备）分别描述如下。 
图1  NRF互备工作方式

NRF互备，是指两台NRF同时处理业务。此时，AMF配置同DC的NRF为主用NRF，异DC的NRF为备用NRF。
正常情况下，AMF和同DC的NRF通信。两台NRF之间进行数据同步。 
当主用NRF故障时，AMF通过检测消息判断主用NRF故障，则与备用NRF通信。 
当主用NRF恢复正常后，AMF可以自动或手动倒回到主用NRF。 
图2  NRF主备工作方式

NRF主备，是指只有主用NRF处理业务，备用NRF不处理业务。主用NRF故障后，备用NRF转为主用，并处理业务。此时，AMF配置主用NRF和备用NRF信息。 
正常情况下，AMF和主用NRF通信。主用NRF将数据同步到备用NRF。 
当主用NRF故障时，AMF通过检测消息判断主用NRF故障，则与备用NRF通信。 
当主用NRF恢复正常后，AMF可以自动或手动倒回到主用NRF。 
图3  主用NRF故障

NRF1为主用NRF，NRF2为备用NRF。当主用NRF故障后，所有AMF均与备用NRF通信。 
###### 涉及的NF 
NF|作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息。
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现，NF状态订阅等功能。
协议栈 :接口|协议栈信息参考
---|---
Nnrf|ZUF-79-19-010 Nnrf
###### 本NF实现 
AMF支持配置主用和备用NRF，如IP地址信息。 
AMF支持通过保活检测识别NRF的故障。 
AMF在主用NRF故障后，支持选择备用NRF继续处理业务。 
AMF在主用NRF恢复后，支持自动或手动的恢复选择主用NRF执行业务。 
业务流程 :主用NRF故障流程
图4  主用NRF故障流程

AMF投入服务后，向主用NRF注册。 
AMF通过保活机制与主用NRF执行通信检测，如心跳检测机制。 
AMF通过主用NRF执行NF服务发现等业务流程。 
某时刻，主用NRF发生故障宕机。AMF保活机制的请求消息无法再接收到主用NRF的响应消息。 
AMF判定主用NRF故障。 
（可选）在主用NRF故障后，AMF根据配置向备用NRF进行注册。 
在主用NRF故障后，AMF通过备用NRF执行NF服务发现等业务流程。 
主用NRF恢复流程
图5  主用NRF恢复流程

在主用NRF故障后，AMF通过备用NRF执行NF服务发现等业务流程。 
某时刻，主用NRF恢复。AMF通过两种方式可以获知主用NRF恢复： 
主用NRF故障后，AMF继续向其发送保活检测消息，通过保活机制获知。 
向备用NRF发送NF服务发现时，备用NRF返回HTTP 308 Permanent Redirect（AMF可以根据NRF进行配置）响应，指示主用NRF已恢复。 
AMF识别主用NRF恢复。 
（可选）在主用NRF恢复后，AMF根据配置向主用NRF进行注册。 
在主用NRF恢复后，AMF恢复使用主用NRF执行NF服务发现等业务流程。 
NRF均故障流程
在主用及备用NRF均故障的情况下，为了继续提供服务，AMF支持如下处理功能： 
NRF均故障时，本地缓存停止老化，继续使用缓存选择NF/NFS。 
NRF均故障时，本地缓存发现失败的情况下，根据配置可以使用本地配置发现和选择NF/NFS。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :当NRF均故障时，AMF使用本地缓存继续处理业务。由于该时刻本地缓存中可能只是部分NF信息，存在发现NF失败的可能。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 29.510（Network Function Repository Services;Stage 3）|5.2 Nnrf_NFManagement Service5.2.2.3.2 NF Heart-Beat5.3 Nnrf_NFDiscovery Service
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.20|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|NRF|SMF|UDM
---|---|---|---|---
-|-|√|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项|命令
---|---
NRF地址配置|ADD NRFNODECFG
SET NRFNODECFG|NRF地址配置
DEL NRFNODECFG|NRF地址配置
SHOW NRFNODECFG|NRF地址配置
NRF FQDN配置|ADD NRFFQDNNODECFG
SET NRFFQDNNODECFG|NRF FQDN配置
DEL NRFFQDNNODECFG|NRF FQDN配置
SHOW NRFFQDNNODECFG|NRF FQDN配置
NRF策略配置|SET NRFPOLICYCFG
SHOW NRFPOLICYCFG|NRF策略配置
查询结果缓存配置|SET NFDISCOVERYRESULTCACHED
SHOW NFDISCOVERYRESULTCACHED|查询结果缓存配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :告警和通知
---
3305242626 NRF节点不可达告警
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过相关配置，实现AMF支持NRF容灾功能，使AMF能够在一台NRF故障后，继续使用另一台NRF执行业务流程，从而保障网络服务的可用性。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
配置过程 :执行[ADD NRFNODECFG]命令，配置主用/备用NRF的IP地址参数。
执行[ADD NRFFQDNNODECFG]命令，配置主用/备用NRF的FQDN参数。AMF通过FQDN向DNS服务器查询，获取NRF的IP地址。
执行[SET NRFPOLICYCFG]命令，配置NRF策略参数，如NRF模式、主用恢复后启用方式、主备间永久重定向响应码等。
 说明： 
NRF地址配置和NRF FQDN配置选择其一配置即可，通常只需配置NRF地址，如果两者都配置，优先根据NRF的FQDN来查询NRF的IP地址。 
配置实例 :场景说明 :场景一
NRF互备容灾。 
场景二
NRF主备容灾。 
场景三
主用/备用NRF均故障，开启了缓存。 
场景四
主用/备用NRF均故障，未开启缓存，发现模式为优先NRF发现。 
数据规划 :配置名称|参数项|取值
---|---|---
NRF地址配置|NRF地址列表ID|[1,20]|[1,20]|[1,20]
主备类型选择|NRF地址配置|主用|备用|备用
NRF IP地址类型|NRF地址配置|IPV4|IPV6|IPV6
NRF IPV4地址|NRF地址配置|字符串|字符串|字符串
NRF IPV6地址|NRF地址配置|字符串|字符串|字符串
NRF IP地址优先级|NRF地址配置|[0,65535]|[0,65535]|[0,65535]
NRF端口号|NRF地址配置|[1,65535]|[1,65535]|[1,65535]
API版本|NRF地址配置|v1|v2|v2
NRF FQDN配置|主备类型选择|主用|备用|备用
FQDN|NRF FQDN配置|字符串|字符串|字符串
NRF端口号|NRF FQDN配置|【1,65535】|【1,65535】|【1,65535】
URI scheme|NRF FQDN配置|http|https|https
API版本|NRF FQDN配置|v1|v2|v2
NRF策略配置|NRF模式|主备模式|互备双活模式|互备双活模式
主用恢复后启用方式|NRF策略配置|自动启用|手动启用|手动启用
主备间永久重定向响应码|NRF策略配置|[0,4294967295]|[0,4294967295]|[0,4294967295]
查询结果缓存配置|发现结果是否缓存|不缓存|缓存|缓存
发现模式配置|AUSF发现模式|通过NRF发现NF|通过本地配置发现NF|优先使用NRF发现NF
配置步骤 :场景|步骤|配置说明|命令示例
---|---|---|---
场景一|1|配置同DC的NRF为主用NRF，异DC的NRF为备用NRF。|NRF地址配置：ADD NRFNODECFG:NRFNODELISTID=1,TYPECHOICE="ACTIVE",IPTYPE="IPV4",IPV4ADDR="192.168.10.10",PRIORITY=0,PORT=8080,APIVERSION="V1"ADD NRFNODECFG:NRFNODELISTID=2,TYPECHOICE="BACKUP",IPTYPE="IPV4",IPV4ADDR="192.168.20.20",PRIORITY=0,PORT=8080,APIVERSION="V1"或NRF FQDN配置：ADD NRFFQDNNODECFG:TYPECHOICE="ACTIVE",FQDN="zte1.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"ADD NRFFQDNNODECFG:TYPECHOICE="BACKUP",FQDN="zte2.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
2|场景一|配置NRF模式为互备双活模式。|SET NRFPOLICYCFG:NRFPATTERN="DUAL_ACTIVE",NRFENABLEMODE="AUTO",SPARENRFOFFRSPCODE=308
场景二|1|配置主用NRF为主用，备用NRF为备用。|NRF地址配置：ADD NRFNODECFGNRFNODELISTID=1,TYPECHOICE="ACTIVE",IPTYPE="IPV4",IPV4ADDR="192.168.10.10",PRIORITY=0,PORT=8080,APIVERSION="V1"ADD NRFNODECFGNRFNODELISTID=2,TYPECHOICE="BACKUP",IPTYPE="IPV4",IPV4ADDR="192.168.20.20",PRIORITY=0,PORT=8080,APIVERSION="V1"或NRF FQDN配置：ADD NRFFQDNNODECFG:TYPECHOICE="ACTIVE",FQDN="zte1.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"ADD NRFFQDNNODECFG:TYPECHOICE="BACKUP",FQDN="zte2.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
2|场景二|配置NRF模式为主备模式。|SET NRFPOLICYCFG:NRFPATTERN="MAIN_STANDBY",NRFENABLEMODE="AUTO",SPARENRFOFFRSPCODE="308"
场景三|1|配置主用NRF为主用，备用NRF为备用。|NRF地址配置：ADD NRFNODECFGNRFNODELISTID=1,TYPECHOICE="ACTIVE",IPTYPE="IPV4",IPV4ADDR="192.168.10.10",PRIORITY=0,PORT=8080,APIVERSION="V1"ADD NRFNODECFG:NRFNODELISTID=2,TYPECHOICE="BACKUP",IPTYPE="IPV4",IPV4ADDR="192.168.20.20",PRIORITY=0,PORT=8080,APIVERSION="V1"或NRF FQDN配置：ADD NRFFQDNNODECFG:TYPECHOICE="ACTIVE",FQDN="zte1.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"ADD NRFFQDNNODECFG:TYPECHOICE="BACKUP",FQDN="zte2.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
2|场景三|配置NRF模式为主备模式。|SET NRFPOLICYCFG:NRFPATTERN="MAIN_STANDBY",NRFENABLEMODE="AUTO",SPARENRFOFFRSPCODE="308"
3|场景三|配置查询结果缓存配置为缓存。|SET NFDISCOVERYRESULTCACHED:NFDISCRESULTCACHED="DISCOVERYRESULTCACHED"
场景四|1|配置主用NRF为主用，备用NRF为备用。|NRF地址配置：ADD NRFNODECFG:NRFNODELISTID=1,TYPECHOICE="ACTIVE",IPTYPE="IPV4",IPV4ADDR="192.168.10.10",PRIORITY=0,PORT=8080,APIVERSION="V1"ADD NRFNODECFG:NRFNODELISTID=2,TYPECHOICE="BACKUP",IPTYPE="IPV4",IPV4ADDR="192.168.20.20",PRIORITY=0,PORT=8080,APIVERSION="V1"或NRF FQDN配置：ADD NRFFQDNNODECFG:TYPECHOICE="ACTIVE",FQDN="zte1.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"ADD NRFFQDNNODECFG:TYPECHOICE="BACKUP",FQDN="zte2.com.cn",PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
2|场景四|配置NRF模式为主备模式。|SET NRFPOLICYCFG:NRFPATTERN="MAIN_STANDBY",NRFENABLEMODE="AUTO",SPARENRFOFFRSPCODE="308"
3|场景四|配置查询结果缓存配置为不缓存。|SET NFDISCOVERYRESULTCACHED:NFDISCRESULTCACHED="DISCOVERYRESULTNOTCACHED"
4|场景四|配置各NF发现模式。以AUSF为例，其他NF类似。|SET NFDISCOVERYMODE CONFIGDISCOVERYAUSFMODE="DiscNfPriorityNrf"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|NRF主备容灾，主用NRF故障
---|---
测试目的|测试主用NRF故障后，AMF能与备用NRF继续通信。
预置条件|AMF已在主用NRF注册成功。配置了主用NRF和备用NRF的地址。配置了NRF模式为主备模式。
测试过程|主用NRF故障宕机。AMF发起NF服务发现等业务流程。
通过准则|AMF能与备用NRF正常进行NF服务发现等业务流程。
测试结果|–
测试项目|NRF互备容灾，主用NRF故障
---|---
测试目的|测试主用NRF故障后，AMF是否能与备NRF继续通信。
预置条件|AMF已在主用NRF注册成功。配置了主用NRF和备用NRF的地址。配置了NRF模式为互备模式。
测试过程|主用NRF故障宕机。AMF发起NF服务发现等业务流程。
通过准则|AMF能与备用NRF正常进行NF服务发现等业务流程。
测试结果|–
测试项目|NRF主备容灾，主用NRF故障后恢复
---|---
测试目的|测试主用NRF故障恢复后，AMF能倒回主用NRF，继续与主用NRF通信。
预置条件|配置了主用NRF和备用NRF的地址。配置了NRF模式为主备模式，主用恢复后启用方式为自动启用，主备间永久重定向响应码为308。主用NRF故障。
测试过程|主用NRF从故障中恢复。AMF发起NF服务发现等业务流程。
通过准则|AMF重新与主用NRF正常进行NF服务发现等业务流程。
测试结果|–
测试项目|NRF互备容灾，主用NRF故障后恢复
---|---
测试目的|测试主用NRF故障恢复后，AMF能倒回主用NRF，继续与主用NRF通信。
预置条件|配置了主用NRF和备用NRF的地址。配置了NRF模式为主备模式，配置主用恢复后启用方式为自动启用。主用NRF故障。
测试过程|主用NRF从故障中恢复。发起NF服务发现等业务流程。
通过准则|AMF重新与主用NRF正常进行NF服务发现等业务流程。
测试结果|–
测试项目|主用和备用NRF均故障
---|---
测试目的|测试开启了发现结果缓存后，主用和备用NRF均故障时，AMF可以成功发起NF服务发现流程。
预置条件|配置了主用NRF和备用NRF的地址。配置了缓存发现结果，缓存了完整的发现结果。主用和备用NRF均故障。
测试过程|AMF发起NF服务发现流程。
通过准则|流程成功。
测试结果|–
测试项目|主用和备用NRF均故障
---|---
测试目的|测试开启了发现结果缓存后，主用和备用NRF均故障时，若发现模式为NRF发现，AMF发起NF服务发现流程失败。
预置条件|配置了主用NRF和备用NRF的地址。配置了发现模式为NRF发现。配置了缓存发现结果，缓存的发现结果不全。主用和备用NRF均故障。
测试过程|AMF发起NF服务发现流程。
通过准则|从缓存中发现失败。
测试结果|–
测试项目|主用和备用NRF均故障
---|---
测试目的|测试主用和备用NRF均故障时，设置发现结果不缓存，发现模式为NRF发现，AMF发起NF服务发现等流程失败。
预置条件|配置了主用NRF和备用NRF的地址。配置了发现结果不缓存，发现模式为NRF发现。主用和备用NRF均故障。
测试过程|AMF发起NF服务发现流程。
通过准则|流程失败。
测试结果|–
测试项目|主用和备用NRF均故障
---|---
测试目的|测试主用和备用NRF均故障时，设置发现结果不缓存，发现模式为优先NRF发现，通过本地发现NF成功。
预置条件|配置了主用NRF和备用NRF的地址。配置了发现结果不缓存，发现模式为优先NRF发现。本地配置了各NF的地址信息。主用和备用NRF均故障。
测试过程|AMF发起NF服务发现流程。NRF发现失败，使用本地配置继续发现选择各NF。
通过准则|本地发现各NF成功，流程成功。
测试结果|–
常见问题处理 :无。 
## ZUF-79-21-005 AMF支持NSSF容灾 
特性描述 :特性描述 :描述 :定义 :AMF支持NSSF容灾功能是指AMF能够在一台NSSF故障后，继续使用另一台NSSF执行业务流程，保障网络服务的可用性。NSSF支持主备容灾方式。 
背景知识 :相比传统移动通讯的核心网，5G核心网存在大容量、高度集中等特点，对可靠性要求很高。外在因素（台风、地震、塌方等）和内在因素（设备老化、元件损坏、系统升级、掉电等）都会导致通讯设备业务中断，用户无法继续业务甚至无法接入，导致用户数据丢失、自动操作系统异常等严重后果。因此，需要一个完善强大的容灾系统来保障整个5G系统的稳定运行。 
5G核心网容灾采用跨DC的异地容灾或地理容灾的方式，当其中一个DC发生故障无法提供服务时，另外一个DC可以接管5G核心网业务。这样可以增强网络的处理能力和快速恢复能力，从而将损失降到最低。
为提高系统可靠性，核心网的业务处理通常需要提供NF冗余机制。作为5G网络的核心NF，NSSF同样需要具备冗余备份机制，AMF需要支持NSSF的容灾功能。 
应用场景 :###### 场景1：AMF支持NSSF主备容灾 
此场景下，两台NSSF分别作为主用NSSF和备用NSSF。 
###### 场景2：AMF支持NSSF均故障的处理 
此场景下，两台NSSF均发生故障，AMF需要具备继续提供服务的能力。 
客户收益 :受益方|受益描述
---|---
运营商|提高系统运行可靠性，降低系统运行风险。为用户提供更好的网络服务，获得更好的用户满意度。
移动用户|在网络中NSSF发生故障的情况下，用户的业务仍然能够得到处理。
实现原理 :系统架构 :AMF支持NSSF容灾功能网络架构如[图1]、[图2]所示。
图1  NSSF主备工作方式

NSSF主备，是指只有主用NSSF处理业务，备用NSSF不处理业务。主用故NSSF障后，备用NSSF转为主用处理业务。此时，AMF配置主用NSSF为高优先级，备用NSSF为低优先级。 
正常情况下，AMF和主用NSSF通信。 
当主用NSSF故障时，AMF通过业务消息或链路状态判断主用NSSF故障，则与备用NSSF通信。 
当主用NSSF恢复正常后，AMF可以倒回到主用NSSF。 
图2  主用NSSF故障

NSSF1为主用NSSF，NSSF2为备用NSSF。当主用NSSF故障后，所有AMF均与备用NSSF通信。 
###### 涉及的NF 
NF|作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息。
AUSF|提供用户鉴权服务。
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现，NF状态订阅等功能。
NSSF|为AMF提供切片选择服务。
PCF|为AMF提供接入及移动性管理等用户策略服务。
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等操作。
UDM|提供用户及会话相关的签约信息。
gNodeB|UE接入时，提供无线资源及承载。
协议栈 :该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N22|ZUF-79-19-008 N22
###### 本NF实现 
AMF支持配置主用和备用NSSF，如IP地址信息。 
AMF在主用NSSF故障后，支持选择备用NSSF继续处理业务。 
AMF在主用NSSF恢复后，支持恢复选择主用NSSF执行业务。 
业务流程 :NSSF主用故障处理流程
图3  NSSF故障处理

正常情况下，AMF发送请求消息给主用NSSF，主用NSSF回复响应后，完成流程处理。 
某时刻，主用NSSF故障，AMF发往主用NSSF的请求无响应。 
AMF在主用故障情况下，重选备用NSSF。 
AMF发送请求消息给备用NSSF，备用NSSF回复响应后，完成流程处理。 
NSSF均故障流程
在主用及备用NSSF均故障的情况下，为了继续提供服务，AMF支持如下处理功能： 
NSSF均故障时，当AMF无法支持所有“请求切片和签约切片的交集”时，AMF支持向NRF发出发现请求，发现满足切片交集的AMF，根据NRF返回结果择优选择AMF，并视需要选择执行AMF re-allocation流程。 
NSSF均故障时，当AMF可以部分支持“请求切片和签约切片的交集”时，根据配置，AMF可以选择执行上述NRF发现流程或直接采用自身为用户提供服务。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性的链路检测（也称本地检测）功能只适用于与对端NF直连的场景，非直连（例如间接通信）的场景不适用。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 29.531（Network Slice Selection Services; Stage 3）|5.2 Nnssf_NSSelection Service
特性能力 :该特性涉及的链路检测（也称本地检测，即HTTP PING检测）功能，AMF整机支持最多同时检测4000个NF服务，最多同时检测6000个IP地址。 
名称|指标
---|---
AMF链路检测支持的最大同时检测NF服务个数|4000
AMF链路检测支持的最大同时检测IP个数|6000
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.30|新增通过HTTP PING方式的本地检测功能。
01|V7.20.20|首次发布。
License要求 :该特性为AMF的基本特性，无需License支持。 
对其他网元的要求 :UE|eNodeB|NSSF|SMF|UDM
---|---|---|---|---
-|-|√|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :本特性不涉及工程规划要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令重选状态配置ADD RESELECTIONSTATUSDEL RESELECTIONSTATUSSET RESELECTIONSTATUSSHOW RESELECTIONSTATUS重新选择配置ADD RESELECTIONDEL RESELECTIONSET RESELECTIONSHOW RESELECTIONNSSF地址池配置ADD NSSFLOCALADDRPOOLDEL NSSFLOCALADDRPOOLSHOW NSSFLOCALADDRPOOLNSSF地址解析配置ADD NSSFPROFILECFGDEL NSSFPROFILECFGSET NSSFPROFILECFGSHOW NSSFPROFILECFGNSSF容灾配置SET NSSFDRCFGSHOW NSSFDRCFGNF故障检测及处理配置SET NFDETECPROCCFGSHOW NFDETECPROCCFG 
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过相关配置，实现以下功能： 
AMF和NSSF交互过程中，若NSSF发生故障，或是链路故障导致暂时通讯失败，AMF重选NSSF，并使用新选择的NSSF完成切片选择过程，从而保证业务的连续性。 
当主备NSSF都没有响应时，可以用NRF代替NSSF，通过NRF选择出合适的AMF来进行相关服务。 
AMF支持识别NSSF的故障及恢复。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
配置过程 :###### 当主用NSSF故障时，AMF执行重选NSSF功能 
执行命令[ADD NSSFLOCALADDRPOOL]，[ADD NSSFPROFILECFG]，配置主备NSSF的地址。
执行命令[ADD RESELECTIONSTATUS]，设置触发重选的HTTP状态码。
执行命令[ADD RESELECTION]，设置NSSF网元的不同IP重选次数。
 说明： 
命令[ADD RESELECTION]中NSSF网元的不同IP重选次数的最大值由用户进行设置，建议设置为1。如果重选次数未达到最大值，并且前一次NSSF响应超时，则继续进行重选。如果NSSF回复了失败响应，则要看该响应是否是命令[ADD RESELECTIONSTATUS]里的 HTTP状态码。
###### 当主备NSSF均故障时，AMF通过NRF代替NSSF 
执行命令[SET NSSFDRCFG]，用NRF代替NSSF，通过NRF选择出合适的AMF来进行相关服务。
###### AMF通过本地检测或NRF通知的方式识别NSSF的故障与恢复 
执行命令[SET NFDETECPROCCFG]，设置支持通过NRF和本地检测NSSF故障与恢复。
配置实例 :###### 实例1：AMF支持NSSF主备容灾 
场景说明一
AMF支持NSSF主备容灾。 
数据规划一
配置项|参数|取值
---|---|---
NSSF地址池配置|地址池标识|[1,65535]
IP地址|NSSF地址池配置|主用NSSF：193.15.2.6备用NSSF：193.15.2.7
端口号|NSSF地址池配置|8080
NSSF地址解析配置|NSSF Profile标识|主用NSSF：1备用NSSF：2
域名|NSSF地址解析配置|主用NSSF：nssf.5gc.mnc001.mcc460.3gppnetwork.org备用NSSF：nssfbak.5gc.mnc001.mcc460.3gppnetwork.org
地址池标识|NSSF地址解析配置|主用NSSF：1备用NSSF：2
优先级|NSSF地址解析配置|主用NSSF：0备用NSSF：10
权重|NSSF地址解析配置|200
URI scheme|NSSF地址解析配置|HTTP
重选状态配置|列表ID|[1,255]
NF类型|重选状态配置|NSSF
NF重选状态码|重选状态配置|404
重新选择配置|NF类型|NSSF
链路重选次数|重新选择配置|[0,10]
IP重选次数|重新选择配置|[0,10]
配置步骤
步骤|说明|操作
---|---|---
1|配置主备NSSF信息|配置主用NSSF：ADD NSSFLOCALADDRPOOL:L:ADDRPOOLID=1,IPADDRESS="193.15.2.6",PORT=8080ADD NSSFPROFILECFG::NSSFPROFILEID=1,HOST=nssf.5gc.mnc001.mcc460.3gppnetwork.org,IPADDRESSID=1,PRIORITY=0,WEIGHT=200,SCHEMA=HTTP配置备用NSSF：ADD NSSFLOCALADDRPOOL:ADDRPOOLID=2,IPADDRESS="193.15.2.7",PORT=8080ADD NSSFPROFILECFG::NSSFPROFILEID=2,HOST=nssfbak.5gc.mnc001.mcc460.3gppnetwork.org,IPADDRESSID=2,PRIORITY=10,WEIGHT=200,SCHEMA=HTTP
2|设置触发NSSF重选的HTTP状态码为404|ADD RESELECTIONSTATUS:LISTID=1,NFTYPE="NSSF",STATUSCODE="Not_Found"
3|设置NSSF的不同IP重选次数|ADD RESELECTION:NFTYPE="NSSF",LINKRESELTIME=1,IPRESELTIME=1
###### 实例2：AMF支持NSSF均故障的处理 
场景说明二
AMF支持NSSF均故障的处理。 
数据规划二
配置项|参数|取值
---|---|---
NSSF容灾配置|NRF发现开关|NSSF故障不启用NRF|NSSF故障启用NRF
部分支持开关|NSSF容灾配置|部分切片支持不启用NRF|部分切片支持启用NRF
携带Region开关|NSSF容灾配置|不携带|携带
配置步骤二
步骤|说明|操作
---|---|---
1|设置当主备NSSF故障时，AMF通过NRF代替NSSF|SET NSSFDRCFG:NRFDISCOVERYSWITCH="SUPPORT"
###### 实例3：NSSF故障与恢复 
场景说明三
设置AMF支持识别NSSF的故障及恢复：AMF能够通过接收NRF的通知，或通过本地检测的方式识别NSSF的故障与恢复。 
数据规划三
配置项|参数|取值
---|---|---
NSSF故障检测配置|NRF检测开关|打开|关闭
NSSF本地检测开关|NSSF故障检测配置|打开|关闭
配置步骤三
步骤|说明|操作
---|---|---
1|设置NSSF故障检测配置。|SET NFDETECPROCCFG:NRFSWITCH="ON",NSSFLOCALSWITCH="ON"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|主用NSSF故障，选择备用NSSF
---|---
测试目的|AMF本地协商发现，AMF支持的切片不能全部满足用户的实际需要，执行本地解析或NRF发现选择NSSF，主用NSSF故障，选择新NSSF成功后，与NSSF交互成功。
预置条件|请求和签约的切片交集，AMF支持的切片不能全部满足用户需要的切片集。   主用NSSF发生故障。配置支持NSSF无响应重选。
测试过程|AMF与备用NSSF交互，获取可以重定向的AMF。
通过准则|AMF与备用NSSF交互成功，获取可以重定向的AMF，成功重定向。
测试结果|–
测试项目|主备用NSSF故障，通过NRF选择合适AMF
---|---
测试目的|AMF本地协商发现，AMF支持的切片不能全部满足用户的实际需要，执行本地解析或NRF发现选择NSSF，主备用NSSF故障，与NRF交互成功。
预置条件|请求和签约的切片交集，AMF支持的切片不能全部满足用户需要的切片集。主备用NSSF均发生故障。配置支持NSSF容灾功能。
测试过程|用NRF代替NSSF，AMF 通过NRF获取可以重定向的AMF。
通过准则|AMF与NRF交互成功，获取可以重定向的AMF，成功重定向。
测试结果|–
测试项目|AMF通过本地检测识别NSSF故障与恢复
---|---
测试目的|测试AMF可以通过本地检测识别NSSF的故障与恢复。
预置条件|请求和签约的切片交集，AMF支持的切片不能全部满足用户需要的切片集。已打开AMF支持本地检测NSSF故障开关。
测试过程|构造环境使NSSF1故障。UE注册过程中需用通过NSSF发现更合适的AMF，通过本地检测发现NSSF1 AMF识别到NSSF1故障，选择NSSF2进行切片协商。构造环境使NSSF1故障恢复。UE注册过程中需用通过NSSF发现更合适的AMF, AMF识别到NSSF1恢复，选择NSSF1进行切片协商。
通过准则|AMF与NRF交互成功，获取可以重定向的AMF，成功重定向。
测试结果|–
常见问题处理 :无。 
## ZUF-79-21-006 AMF支持SMSF容灾 
特性描述 :特性描述 :描述 :定义 :AMF支持SMSF容灾功能是指AMF在SMSF故障情况下，继续使用另一个SMSF服务网元执行业务流程，保障用户SMS业务服务的连续性。
背景知识 :相比传统移动通讯的核心网，5G核心网存在大容量、高度集中等特点，对可靠性要求很高。外在因素（台风、地震、塌方等）和内在因素（设备老化、元件损坏、系统升级、掉电等）都会导致通讯设备业务中断，用户无法继续业务甚至无法接入，导致用户数据丢失、自动操作系统异常等严重后果。因此，需要一个完善强大的容灾系统来保障整个5G系统的稳定运行。 
5G核心网容灾采用跨DC的异地容灾或地理容灾的方式，当其中一个DC发生故障无法提供服务时，另外一个DC可以接管5G核心网业务。这样可以增强网络的处理能力和快速恢复能力，从而将损失降到最低。
SMSF支持跨DC SMSF 1+1互备容灾方式。SMSF通过STP连接到SMSC/IP-SM-GW，也可以采用SMSC/IP-SM-GW与SMSF直连的组网，当AMF检测到SMSF故障时，继续使用另一个SMSF服务网元执行业务流程，保障用户SMS业务服务的连续性。 
应用场景 :###### 场景1：AMF支持识别SMSF的故障及恢复 
AMF上电成功，向NRF订阅SMSF的状态或者周期检测与SMSF的链路状态，当SMF服务网元发生故障或故障恢复时，AMF可以通过NRF状态通知或链路检测确定。 
###### 场景2：SMSF故障，AMF在执行后续短信业务时重选SMSF 
AMF通过NRF状态通知或链路检测识别SMSF故障，后续收到UE的短信业务时，重新选择SMSF，AMF向新SMSF发送短信业务请求，完成短信投递。 
###### 场景3：SMSF故障，AMF在SMSF无响应时重选SMSF 
AMF未检测到SMSF故障前，收到UE的短信业务，AMF向SMSF发送短信业务请求后，SMSF无响应，超时后，AMF重新选择SMSF，AMF向新SMSF发送短信业务请求，完成短信投递。 
###### 场景4：AMF支持选择故障已恢复的SMSF进行业务交互 
SMSF故障恢复后，AMF通过NRF状态通知或链路检测感知SMSF恢复，对尚未迁移到其他SMSF的业务仍使用恢复后的SMSF。 
###### 场景5：SMSF故障，AMF收到备用SMSF的MT短信业务处理 
SMSF故障后，AMF收到备用SMSF的MT短信业务时，正常向UE投递短信业务。后续当收到UE短信业务消息时，会触发SMSF的重选和更新。
客户收益 :受益方|受益描述
---|---
运营商|满足运营商业务功能的需求，在SMSF发生故障及容灾场景下继续为用户提供业务服务，保障整个网络正常运行，提高5G网络的可靠性。
移动用户|在SMSF故障容灾场景下， AMF选择备用SMSF处理用户的短信业务，快速恢复用户的业务，保证用户的利益，提高用户满意度。
实现原理 :系统架构 :AMF支持SMSF容灾网络架构图如[图1]所示。
图1  SMF容灾架构示意图

SMSF容灾短信业务路径组网，如[图2]所示。
图2  短信业务路径示意图

###### 涉及的NF 
网元名称|网元作用
---|---
AMF|SMSF发生故障， AMF通过NRF订阅通知或链路检测识别SMSF故障。业务流程中，AMF识别故障的SMSF，选择同组运行正常的SMSF执行业务流程。SMSF故障恢复，AMF通过NRF或自动检测识别SMSF已经恢复。AMF识别已经恢复的SMSF，业务过程中，恢复选择故障已经恢复的SMSF执行业务流程。
NRF|AMF向NRF订阅SMSF的状态，NRF检测到SMSF故障已经恢复，向AMF发送SMSF故障通知。当NRF检测到SMSF恢复，向AMF发送AUSF/UDM故障恢复通知。
SMSF|SMSF向NRF注册NF。NRF监测与SMSF的网络运行。由NRF通知AMF订阅的SMSF的状态，AMF进行SMSF重选。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N20|ZUF-79-19-012 N20
NRF|ZUF-79-19-010 Nnrf
###### 本NF实现 
AMF支持通过SMSF状态订阅和本地检测识别SMSF的故障及恢复。 
AMF支持SMS over NAS短消息激活过程中，排除故障SMSF和重选。 
SMSF故障，MO SMS over NAS短消息激活支持SMSF网元级容灾，AMF在SMSF无响应时执行重选。 
SMSF故障，MT SMS over NAS短消息激活支持SMSF网元级容灾，AMF在SMSF无响应时执行重选。 
业务流程 :AMF支持SMS over NAS短消息激活过程中，排除故障SMSF和重选
图3  AMF支持SMS over NAS短消息激活过程中，排除故障SMSF和重选

UE发起注册更新，向AMF发送Registration Request消息，携带“SMS supported”指示，指示UE的SMS over NAS传输能力。 
AMF向UDM注册成功后，AMF向UDM发送Nudm_SDM_Get消息获取用户签约信息，获取到SMS Subscription数据。 
Registration Request中包含“SMS supported”指示，并且SMS Subscription数据中允许SMS业务，AMF通过NRF或本地策略发现和选择SMSF为UE服务，向NRF订阅SMSF_1的状态通知。 
AMF继续处理注册业务流程。 
注册业务流程完成后，AMF向SMSF_1服务发送Nsmsf_SMService_Activate Request消息前进行SMSF_1状态检查： 
如果SMSF_1正常，AMF向SMSF_1服务发送Nsmsf_SMService_Activate Request进行短信激活过程。 
如果SMSF_1故障或者AMF向SMSF_1发送短信激活请求后，对端SMSF超时无响应，AMF重新根据权重优先级重新选择一个SMSF_2为UE服务，AMF向SMSF_2服务发送Nsmsf_SMService_Activate Request进行短信激活过程。 
SMSF 执行UDM发现并选择UDM服务网元。 
SMSF进行检查，如果没有UE上下文，则使用Nudm_UECM_Registration with Access Type向UDM发起注册流程。 
SMSF通过Nudm_SDM_Get检索并获取到SMS管理订阅数据（例如SMS远程服务、SMS限制列表）。 
SMSF向AMF返回Nsmsf_SMService_Activate Response消息，短信注册激活成功。 
AMF向UE发送Registration Accept消息，注册更新流程完成。 
SMSF故障，MO SMS over NAS短消息激活支持SMSF网元级容灾，AMF在SMSF无响应时执行重选
图4  SMSF故障，MO SMS over NAS短消息激活支持SMSF网元级容灾，AMF在SMSF无响应时执行重选

UE发起短消息业务，触发Service Request流程，建立到AMF的NAS信令连接。 
UE构建要发送的SMS消息（SMS消息由CP-DATA/RP-DATA/TPDU/SMS-SUBMIT部分组成）。SMS消息封装在NAS消息中，UE向AMF发送NAS消息。 
AMF调用Nsmsf_SMService_UplinkSMS进行服务操作，将SMS消息和SUPI转发给SMSF_2。 
AMF等待SMSF_2响应超时，AMF重新根据优先级权重重新选择一个SMSF_1为UE服务。 
AMF向SMSF_1发起Nsmsf_SMService_UplinkSMS服务操作。 
SMSF_1检查SMS签约数据，如果允许短信投递，则向SMS/IWMSC发送Forward NO成功，SMS/IWMSC返回Submit Report。 
SMSF_1同时调用Namf_Communication_N1N2MessageTransfer服务操作，向AMF转发SMS ack消息。 
AMF通过Downlink NAS transport消息将SMSF_1返回的SMS ack消息转发给UE，通知UE短信submit已经接收处理。 
SMS/IWMSC完成短信submit成功，SMS/IWMSC向SMSF_1返回Submit Report。 
SMSF_1通过调用Namf_Communication_N1N2MessageTransfer服务操作将短信提交的报告转发给AMF。 
AMF将收到的消息通过Downlink NAS transport转发给UE。 
当不再发送SMS时，UE向SMSF返回CP ack。 
AMF调用Nsmsf_SMService_UplinkSMS服务操作，向SMSF转发SMS ack消息。 
SMSF故障，MT SMS over NAS短消息激活支持SMSF网元级容灾，AMF在SMSF无响应时执行重选
图5  SMSF故障，MT SMS over NAS短消息激活支持SMSF网元级容灾，AMF在SMSF无响应时执行重选

短消息中心SC向SMS/IWMSC发送Message Transfer消息。 
SMS/IWMSC向UDM发送Send Routing Info For SM， SC/SMS-GMSC/UDM完成短信MT投递路由，获取到SMSF_2网元信息。 
SMSF_2收到SC的Foward MT SM消息。 
SMSF_2检查SMS签约数据。如果允许SMS投递，SMSF_2向AMF调用Namf_MT_EnableUEReachability Request服务操作消息。AMF触发寻呼和业务请求流程。 
AMF发起寻呼/业务请求流程。 
寻呼和业务请求成功，AMF向SMSF_2返回Namf_MT_EnableUEReachability Response消息。 
SMSF_2通过调用Namf_Communication_N1N2MessageTransfer服务操作，将SMS消息（SMS消息由CPDATA/RPDATA/TPDU/SMS DELIVER部分组成）转发到AMF。 
AMF将SMS消息传递给UE。 
UE向SMSF确认接收SMS消息。 
AMF收到UE上行消息时，SMSF_2发生故障，AMF根据运营商策略以及优先级权重选择SMSF_1，AMF调用Nsmsf_SMService_UplinkSMS服务操作，将消息转发给SMSF_1。 
UE向AMF返回短信投递报告。 
投递报告封装在NAS消息中，发送给AMF，AMF通过调用Nsmsf_SMService_UplinkSMS服务操作将投递报告转发给重新选择后的SMSF_1。 
SMSF_1将Dilivery Rpt信息发送给SMS/IWMSC，SMS/IWMSC发送给SC，SC确认短信投递成功。 
SMSF_1使用Namf_Communication_N1N2MessageTransfer服务操作向AMF发送SMS CP ack消息。 
AMF将SMS消息通过NAS消息封装给UE。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性的链路检测（也称本地检测）功能只适用于与对端NF直连的场景，非直连（例如间接通信）的场景不适用。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :类别|标准编号|标准名称
---|---|---
3GPP|TS 23.501|Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2
TS 23.502|3GPP|3GPP TS 23.502 Technical Specification Group Services and System Aspects; Procedures for the 5G System; Stage 2
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS)
TS 29.518|3GPP|5G System; Access and Mobility Management Services
TS 29.510|3GPP|5G System: Network function repository services
RFC|RFC7231|Hypertext Transfer Protocol
RFC3986|RFC|Uniform Resource Identifier (URI)
特性能力 :该特性涉及的链路检测（也称本地检测，即HTTP PING检测）功能，AMF整机支持最多同时检测4000个NF服务，最多同时检测6000个IP地址。 
名称|指标
---|---
AMF链路检测支持的最大同时检测NF服务个数|4000
AMF链路检测支持的最大同时检测IP个数|6000
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.30|新增通过HTTP PING方式的本地检测功能。
01|V7.20.20|首次发布。
License要求 :该特性需要开启License，对应的License项目为“AMF支持SMS over NAS功能”，此项目显示为“打开”。
###### 对其他NF的要求 
UE|gNodeB|NRF|SMSF|UDM
---|---|---|---|---
-|-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :工程规划上，需要SMSF进行容灾备份，如主备、POOL等备份方式，AMF配置SMSF故障重选策略。 
O&M相关 :命令 :配置项 
配置项|命令
---|---
重选状态码配置|ADD SBIRESELECTSTATUSCODE
DEL SBIRESELECTSTATUSCODE|重选状态码配置
SET SBIRESELECTSTATUSCODE|重选状态码配置
SHOW SBIRESELECTSTATUSCODE|重选状态码配置
重选配置|ADD SBIRESELECT
DEL SBIRESELECT|重选配置
SET SBIRESELECT|重选配置
SHOW SBIRESELECT|重选配置
SMSF容灾配置|SET SMSFDRCFG
SHOW SMSFDRCFG|SMSF容灾配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过相关配置，实现以下功能： 
AMF和SMSF交互过程中，若SMSF发生故障，或链路故障导致暂时通讯失败，AMF重选SMSF，并使用新选择的SMSF完成短消息业务，从而保证业务的连续性。 
当发生故障的SMSF恢复时，AMF对尚未迁移到其他SMSF的业务仍使用恢复后的SMSF， 对后来的短消息业务使用负荷分担的方式。 
AMF支持识别SMSF的故障及恢复。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
AMF支持SMS over NAS功能License项已打开。 
配置过程 :本功能用于设置当SMSF故障时，AMF是否执行重选SMSF功能。 
执行命令 [ADD SBIRESELECTSTATUSCODE]， 设置触发重选的HTTP状态码。
执行命令[ADD SBIRESELECT]，设置SMSF网元的不同IP重选次数。
执行命令[SET SMSFDRCFG]， 打开支持SMSF无响应重选（非首次激活）开关和支持MO/MT SMS over NAS流程冲突处理开关。
（可选）如果需要AMF支持通过本地检测或NRF通知的方式识别SMSF的故障与恢复，执行命令[SET NFDETECPROCCFG]，设置支持通过NRF和本地检测SMSF故障与恢复。
 说明： 
支持SMSF无响应重选（非首次激活）开关说明：AMF在向SMSF前传短消息时，如果SMSF无响应， 若此开关打开，AMF会根据发现SMSF的方式再次选择SMSF进行前传短消息。 
支持MO/MT SMS over NAS流程冲突处理开关说明：MT SMS over NAS流程中，由于消息中无SMSF信息，无法更新UE上下文中的SMSF信息，只能在后续MO流程再更新。如果网络中部署了多个SMSF（大于2），MO/MT流程可能存在冲突，即上行和下行容灾的SMSF可能不同。若此开关打开，AMF重选SMSF前，会先从UDM获取一次目前注册的SMSFID，使用此SMSFID重选SMSF。 
配置实例 :场景说明 :处理SMSF容灾，可以根据本功能的开关处理不同SMSF容灾场景。以下是SMSF容灾重选下的四个不同场景。 
场景一：
打开支持SMSF无响应重选（非首次激活）开关：AMF接收UE的短信业务，发现SMSF故障，执行本地解析或NRF发现重新选择SMSF，选择新SMSF成功后，与SMSF交互成功。 
场景二：
打开支持SMSF无响应重选（非首次激活）：用户选择的SMSF故障后，AMF未检测到SMSF故障前接收UE的短信业务，AMF向SMSF发送前传请求，SMSF无响应，AMF执行本地解析或NRF发现重新选择SMSF成功后， 与SMSF交互成功。 
场景三：
打开支持MO/MT SMS over NAS流程冲突处理开关：SMSF发生故障，AMF收到备用SMSF的MT短信消息，正常向UE投递短信业务。后续当UE发起MO流程时，会触发SMSF的重选和更新。 
场景四：
设置触发SMSF重选的HTTP状态码为504，且设置SMSF的不同IP重选次数：注册激活SMSF时，如果当前选择的SMSF无响应，AMF会使用本地解析或NRF发现的SMSF列表中的其他SMSF IP进行激活SMSF。 
场景五：
设置AMF支持识别SMSF的故障及恢复：AMF能够通过接收NRF的通知，或通过本地检测的方式识别SMSF的故障与恢复。 
数据规划 :配置项|参数|取值
---|---|---
SMSF容灾配置|支持SMSF无响应重选（非首次激活）开关|支持|不支持
支持MO/MT SMS over NAS流程冲突处理开关|SMSF容灾配置|支持|不支持
重选状态码配置|标识|1|1
目的NF类型|重选状态码配置|SMSF|SMSF
状态码|重选状态码配置|504|504
SMSF重选配置|目的NF类型|SMSF|SMSF
链路重选次数|SMSF重选配置|0|0
IP重选次数|SMSF重选配置|3|3
NF重选次数|SMSF重选配置|1|1
重选等待时长(秒)|SMSF重选配置|2|2
SMSF故障检测配置|NRF检测开关|打开|关闭
SMSF本地检测开关|SMSF故障检测配置|打开|关闭
配置步骤 :场景|步骤|说明|操作
---|---|---|---
场景一|1|AMF收到短消息时，已识别到SMSF故障，打开支持SMSF无响应重选（非首次激活）开关。|SET SMSFDRCFG:SUPSMSFNRSPRSEL="SPRT",SUPMOMTSMSCONFLICT="SPRT"
场景二|1|AMF收到短消息时，未识别到SMSF故障，SMSF无响应重选。打开支持SMSF无响应重选（非首次激活）开关。|SET SMSFDRCFG:SUPSMSFNRSPRSEL="SPRT",SUPMOMTSMSCONFLICT="SPRT"
场景三|1|支持MO/MT流程冲突处理开关，MT流程交互正常。|SET SMSFDRCFG:SUPSMSFNRSPRSEL="SPRT",SUPMOMTSMSCONFLICT="SPRT"
场景四|1|注册激活SMSF时无响应重选，触发激活SMSF时无响应重选状态码。|ADD SBIRESELECTSTATUSCODE:ID=1,TARGETNFTYPE="SMSF_TYPE",STATUSCODE=504
2|场景四|设置SMSF的不同IP重选次数。|ADD SBIRESELECT:TARGETNFTYPE="SMSF_TYPE",LINKRESELTIMES=0,IPRESELECTIMES=3,NFRESELECTIMES=1,RESELECTTIME=2
场景五|1|设置SMSF故障检测配置。|SET NFDETECPROCCFG:NRFSWITCH="ON",SMSFLOCALSWITCH="ON"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|主用SMSF故障，选择备用SMSF
---|---
测试目的|测试AMF发现SMSF故障后，执行本地解析或NRF发现重新选择SMSF，并能与SMSF交互。
预置条件|UE注册过程已向主用SMSF激活短消息。主用SMSF发生故障。AMF收到UE的MO短消息。配置 支持SMSF无响应重选。
测试过程|UE发送短消息。
通过准则|AMF选择新的SMSF网元，并交互成功。
测试结果|–
测试项目|主用SMSF发生故障，AMF前传MO短消息超时无响应，选择备用SMSF
---|---
测试目的|测试AMF向SMSF发送前传请求，SMSF超时无响应，AMF可以选择新SMSF并成功交互。
预置条件|UE注册过程已向主用SMSF激活短消息。AMF收到UE的MO短消息时主用SMSF发生故障， AMF未检测到SMSF故障。配置 支持SMSF无响应重选。
测试过程|UE发送短消息。
通过准则|AMF选择新的SMSF网元，并交互成功。
测试结果|–
测试项目|主用SMSF发生故障，备用SMSF给AMF发送MT短消息
---|---
测试目的|测试AMF前传MT短消息给UE并收到UE的MO响应后， 检测到主用SMSF故障，可以从UDM获取SMSFID并重新发现SMSF。
预置条件|UE注册过程已向主用SMSF激活短消息。主用SMSF发生故障。给UE发送短消息，AMF收到备用SMSF的MT消息。配置 支持MO/MT SMS over NAS流程冲突处理。
测试过程|AMF给UE发送短消息。
通过准则|AMF与备用SMSF网元完成MT流程。
测试结果|–
测试项目|注册激活短消息重选SMSF
---|---
测试目的|测试用户在注册过程中激活SMSF， SMSF超时无响应时， AMF可以通过选择发现的其他SMSF IP来激活SMSF。
预置条件|UE和AMF都只支持短消息。AMF上短消息License已开。AMF本地发现或通过NRF发现结果。配置支持SMSF无响应重选。
测试过程|UE注册。
通过准则|AMF使用新的SMSF IP激活成功。
测试结果|–
测试项目|AMF通过NRF通知识别SMSF故障与恢复
---|---
测试目的|测试AMF可以通过接收NRF的故障通知与恢复通知识别SMSF的故障与恢复。
预置条件|UE和AMF都支持短消息。AMF上短消息License已开。AMF本地发现或通过NRF发现结果。配置支持SMSF无响应重选。已打开AMF支持NRF检测SMSF故障开关。
测试过程|NRF向AMF发送通知，告知SMSF1发生故障。UE注册过程中通过NRF发现SMSF1, AMF识别到SMSF1故障，激活失败。NRF向AMF发送通知，告知SMSF1故障恢复。UE注册过程中通过NRF发现SMSF1, AMF识别到SMSF1故障恢复，激活成功。
通过准则|AMF使用新的SMSF IP激活成功。
测试结果|–
测试项目|AMF通过本地检测识别SMSF故障与恢复
---|---
测试目的|测试AMF可以通过本地检测识别SMSF的故障与恢复。
预置条件|UE和AMF都支持短消息。AMF上短消息License已开。AMF本地发现或通过NRF发现结果。配置支持SMSF无响应重选。已打开AMF支持本地检测SMSF故障开关。
测试过程|构造环境使SMSF1故障。UE注册过程中通过本地检测发现SMSF1, AMF识别到SMSF1故障，激活失败。构造环境使SMSF1故障恢复。UE注册过程过通过本地检测发现SMSF1, AMF识别到SMSF1恢复，激活成功。
通过准则|AMF使用新的SMSF IP激活成功。
测试结果|–
常见问题处理 :无。 
## ZUF-79-21-007 AMF支持P-CSCF容灾 
特性描述 :特性描述 :描述 :定义 :UE发起IMS PDN连接，连接建立后，S-CSCF检测到Mw接口故障、P-CSCF故障（重启、拥塞）时，AMF和UDM共同实现VoNR语音被叫业务快速恢复，减少用户被叫时出现的语音业务中断时长，提升用户体验。
背景知识 :Vo5G(Voice over 5G)是5G语音解决方案的总称，包括以下4种方案： 
VoNR（Vonr over NR） 
EPSFB（EPS Fallback） 
VoeLTE（Voice over eLTE） 
RAT FB（RAT Fallback） 
数据业务驱动了5G的演进，但语音业务依然是运营商的重要业务，5G沿用4G的语音架构，基于IMS用户提供语音业务，是加速5G发展的一个重要技术。相比于4G语音，5G语音主要有如下优势： 
使用成本：5G上行带宽和小区容量较4G有10到20倍的提升，单比特（bit）带宽成本降低。 
普及性：视频通话普及、运营商网间共享部署，支持手机、eMTC设备（TV、摄像头、车载）等互联互通。 
高体验：支持多方视频通信，语音抗干扰能力强，增强覆盖，带来有效的覆盖增益。 
GSM/UMTS网络，语音基于CS，核心侧由MSC完成语音业务控制和接续。4G时期，引入IMS，使承载、控制和业务三者完全分离，用户从EPC接入到IMS核心侧，由VoLTE提供语音业务，5G时期，有如下4种Vo5G方案： 
VoNR（Voice over NR）：基于NR的语音方案称，是Vo5G的目标语音方案。 
EPS FB（EPS Fallback）：5G建网初期，NR覆盖不全且eNodeB未升级，为保证语音连续性，采用EPS Fallback回落到LTE网络由VoLTE提供语音，它是VoLTE向VoNR演进的过渡语音方案。 
VoeLTE（Voice over eLTE）：NR覆盖范围受限，增强LTE网络使其可接入5GC，该语音方案称为VoeLTE。 
RAT FB（RAT Fallback）：NR不支持语音，语音需回落到eLTE网络处理，该语音方案为RAT FB。 
VoNR基础语音业务场景下，P-CSCF是用户接入IMS网络的统一入口点，主要负责信令和消息的代理。主叫和被叫的IMS会话消息都会通过P-CSCF。当P-CSCF故障时，用户主叫可能会失败，终端用户重新接入后，可实现业务恢复。对于用户被叫，在用户不进行主叫且IMS注册定时器超时前，用户的被叫是一直失败的，用户体验较差。 
为提升用户体验，AMF、SMF、UDM、S-CSCF协同实现P-CSCF故障场景下的VoNR语音快速恢复。 
应用场景 :###### 场景1：AMF和SMF正常，基于UDM的P-CSCF故障恢复 
在VoNR被叫场景下，S-CSCF收到INVITE消息时，如果检测到被叫用户所注册的P-CSCF故障，则通知UDM。 
UDM向该用户注册的AMF发送P-CSCF Restoration通知，触发AMF对该用户进行IMS PDU会话重建或用户重新注册到5G网络。如果AMF检测到SMF状态正常，AMF向SMF发送IMS PDU会话重建通知，通知SMF触发IMS PDU会话重建流程。 
###### 场景2：AMF正常，SMF故障，基于UDM的P-CSCF故障恢复 
在VoNR被叫场景下，S-CSCF收到INVITE消息时，如果检测到被叫用户所注册的P-CSCF故障，则通知UDM。 
UDM向该用户注册的AMF发送P-CSCF Restoration通知，触发AMF对该用户进行IMS PDU会话重建或用户重新注册到5G网络。如果AMF检测到SMF也发生故障，则AMF立即向终端触发IMS PDU会话重建流程。 
###### 场景3：AMF无IMS PDU会话，收到UDM的P-CSCF恢复通知 
在VoNR被叫场景下，S-CSCF收到INVITE消息时，如果检测到被叫用户所注册的P-CSCF故障，则通知UDM。 
UDM向该用户注册的AMF发送P-CSCF Restoration通知，触发AMF对该用户进行IMS PDU会话重建或用户重新注册到5G网络。如果AMF检测当前无IMS PDU会话上下文，则AMF触发终端重新注册到网络。 
客户收益 :受益方|受益描述
---|---
运营商|提高故障场景下的VoNR语音恢复速度，减少用户被叫时出现的语音业务中断时长。
移动用户|通话体验更加流畅。
实现原理 :系统架构 :AMF处理基于UDM的P-CSCF Restoration通知业务流程架构如[图1]所示。
图1  AMF基于UDM的P-CSCF故障恢复业务架构

###### 涉及的NF 
网元名称|网元作用
---|---
UE|支持NG-RAN/E-UTRAN/GERAN/UTRAN接入；支持将自身的VoNR能力通过NAS信令传递给AMF，支持VONR语音PDU重建。
NR|传递UE的NAS信令，支持语音QoS Flow建立与释放。
AMF|VoNR能力管理，在注册流程中指示pcscfRestorationCallbackUri；支持处理UDM的P-CSCF Restoration通知，触发IMS PDU重建。
UDM|支持IMS网络的HSSP-CSCF Restoration指示，支持向AMF发送P-CSCF Restoration通知。
SMF|SMF建立用于VoNR的IMS信令承载、视频承载和语音承载，支持AMF的Nsmf_PDUSession_UpdateSMContext消息，处理AMF的IMS PDU重建指示。
PCF|IMS向PCF发起承载建立请求，PCF向SMF提供授权的QoS策略；IMS视频语音使用audio:QI=1、video:QI=2的承载，SIP/SDP传输IMS信令使用QI=5的承载。
CS网元|2G/3G用户和5G用户间进行语音通话时，CS网元负责2G/3G用户语音信令和承载的建立和处理。
IMS网元|IMS网络P-CSCF故障时，支持向UDM/HSS发送P-CSCF Restoration指示。
协议栈 :本特性涉及到的协议栈如下。 
图2  AMF和其他NF的协议栈

图3  AMF和UE的接口协议栈

图4  AMF和RAN（gNodeB）的接口协议栈

###### 本NF实现 
P-CSCF发生容灾时，VONR或者VOLTE语音会产生中断，AMF感知不到CSCF发生故障， 如果SMF没有感知CSCF发生故障，触发IMS会话重建， 那么语音将会中断，只能等UE重新发起业务流程重新建立PDU会话；用户体验比较不好。 
在VoNR被叫场景下，S-CSCF收到INVITE消息时，检测到被叫用户注册的P-CSCF故障，向UDM发送P-CSCF Restoration指示。UDM收到指示后，向用户注册的AMF发送P-CSCF Restoration流程，AMF触发该用户的IMS PDU会话重建或重新注册。 
AMF检测到SMF正常，则AMF通知SMF触发UE的IMS PDU会话重建。 
AMF检测到SMF也发生故障，则AMF通知UE进行IMS PDU会话重建。 
AMF检测无IMS PDU会话，AMF根据运营商策略是否触发UE重新注册。 
业务流程 :SMF正常，AMF通知SMF触发UE的IMS PDU会话重建。
流程如[图5]所示：
图5  SMF正常，AMF处理P-CSCF故障业务流程

业务流程： 
UE在Registration Request消息中携带VoNR关键信元： UE's usage setting。支持Voice centric。 
AMF向UDM发起注册，注册消息中携带pcscfRestorationCallbackUri、amfServiceNamePcscfRest属性用于指示AMF是否支持P-CSCF故障恢复。AMF正常处理注册请求，直到完成和PCF的交互。 
AMF根据UE语音能力、无线语音能力和运营商策略共同决定UE支持IMS voice over PS Session。 
AMF向UE返回Registration Accept消息，消息中携带5GS network feature support信元，指示是否支持IMS voice over PS Session。 
UE触发IMS PDU会话建立， 后续在此PDU上进行VONR语音业务。 
P-CSCF发生故障，S-CSCF发送P-CSCF Restoration指示给UDM。 
UDM根据AMF的注册URL，向AMF发送P-CSCF Restoration通知消息（如果SMF向UDM注册，UDM会向SMF发送P-CSCF Rstoration通知）。 
AMF收到消息后，存在IMS PDU会话，检测到SMF正常，AMF向SMF发送Nsmf_PDUSession_UpdateSMContext消息，原因值：REL_DUE_TO_REACTIVATION。 
SMF收到消息后，向UE发送PDU会话释放，触发IMS PDU会话重建。 
UE收到PDU会话释放消息后，触发IMS PDU会话重建。 
后续在此PDU上进行VONR语音业务。 
SMF故障，AMF触发UE的IMS PDU会话重建。
流程如[图6]所示：
图6  SMF故障，AMF处理P-CSCF故障业务流程

业务流程： 
UE在Registration Request消息中携带VoNR关键信元： UE's usage setting。支持Voice centric。 
AMF向UDM发起注册，注册消息中携带pcscfRestorationCallbackUri、amfServiceNamePcscfRest属性用于指示AMF是否支持P-CSCF故障恢复。AMF正常处理注册请求，直到完成和PCF的交互。 
AMF根据UE语音能力、无线语音能力和运营商策略共同决定UE支持IMS voice over PS Session。 
AMF向UE返回Registration Accept消息，消息中携带5GS network feature support信元，指示是否支持IMS voice over PS Session。 
UE触发IMS PDU会话建立， 后续在此PDU上进行VONR语音业务。 
P-CSCF发生故障，S-CSCF发送P-CSCF Restoration指示给UDM。 
UDM根据AMF的注册URL，向AMF发送P-CSCF Restoration通知消息（如果SMF向UDM注册，UDM会向SMF发送P-CSCF Rstoration通知）。 
AMF收到消息后，存在IMS PDU会话，检测到SMF故障，AMF向UE发送PDU会话释放。失败原因：Reactivation requested，触发IMS PDU会话重建。 
UE收到PDU会话释放消息后，触发IMS PDU会话重建。 
后续在此PDU上进行VONR语音业务。 
无IMS PDU会话，AMF根据运营商策略是否触发UE重新注册。
流程如[图7]所示：
图7  无IMS PDU会话，AMF触发UE重新注册

业务流程： 
UE在Registration Request消息中携带VoNR关键信元： UE's usage setting。支持Voice centric。 
AMF向UDM发起注册，注册消息中携带pcscfRestorationCallbackUri、amfServiceNamePcscfRest属性用于指示AMF是否支持P-CSCF故障恢复。AMF正常处理注册请求，直到完成和PCF的交互。 
AMF根据UE语音能力、无线语音能力和运营商策略共同决定UE支持IMS voice over PS Session。 
AMF向UE返回Registration Accept消息，消息中携带5GS network feature support信元，指示是否支持IMS voice over PS Session。 
UE触发IMS PDU会话建立， 后续在此PDU上进行VONR语音业务。 
P-CSCF发生故障，S-CSCF发送P-CSCF Restoration指示给UDM。 
UDM根据AMF的注册URL，向AMF发送P-CSCF Restoration通知消息（如果SMF向UDM注册，UDM会向SMF发送P-CSCF Rstoration通知）。 
AMF收到消息后，不存在IMS PDU会话，AMF根据运营商策略和用户状态分别触发UE重新注册： 
用户处于Connected态，AMF触发UE网络去注册， 原因是“re-registration required”。 
用户处于Idle态，AMF寻呼用户，收到service req后，向UE发送service reject，隐式去注册。 
UE收到去注册消息或者Service Reject消息，触发重新注册流程。 
注册完成，UE重新发起IMS PDU会话建立，会话建立成功后，后续在此PDU上进行VoNR语音业务。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP 23.380|"IMS Restoration Procedures"
3GPP 23.501|System architecture for the 5G System
3GPP 23.502|Procedures for the 5G System; Stage 2
3GPP 29.503|5G System; Unified Data Management Services; Stage 3
3GPP 29.510|5G System: Network function repository services; Stage 3
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.20.40|首次发布。
License要求 :该特性需要申请License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“AMF支持基于UDM的P-CSCF 故障恢复功能”，此项目显示为支持，表示AMF支持基于UDM的P-CSCF故障恢复功能。
###### 对其他NF的要求 
UE|gNodeB|UDM|SMF|P-CSCF
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :部署IMS网络，并与5G网络需互连互通，5GC、RAN都需支持VoNR。 
需要AMF/UDM支持P-CSCF故障恢复通知。 
开通基于UDM的P-CSCF故障恢复功能，需要申请License。 
O&M相关 :命令 :配置项|命令
---|---
P-CSCF故障恢复配置|SET UDMPCSCFRESTORCFG
SHOW UDMPCSCFRESTORCFG|P-CSCF故障恢复配置
性能统计 :性能计数器名称
---
C510520103 接收Nudm_UECM_PcscfRestorationNotification请求次数
C510520104 发送Nudm_UECM_PcscfRestorationNotification成功响应次数
C510520105 发送Nudm_UECM_PcscfRestorationNotification失败响应次数
C511400105 接收Nudm_UECM_PcscfRestorationNotification请求次数
C511400106 发送Nudm_UECM_PcscfRestorationNotification成功响应次数
C511400107 发送Nudm_UECM_PcscfRestorationNotification失败响应次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :P-CSCF故障恢复配置用于，在S-CSCF、PCSCF等故障情况下，UDM通知AMF P-CSCF故障恢复时，AMF处理VoNR被叫恢复的行为。 
通过P-CSCF故障恢复配置，AMF可以进行以下类别的P-CSCF故障恢复配置。 
AMF支持基于UDM的P-CSCF故障恢复功能。 
AMF支持无IMS会话的P-CSCF故障恢复功能。 
配置前提 :AMF以及周边网元运行正常。 
AMF网管能正常连接。 
配置过程 :配置功能开关和默认策略。执行[SET UDMPCSCFRESTORCFG]命令，设置AMF是否支持”基于UDM的P-CSCF故障恢复功能”、AMF是否支持”无IMS会话的P-CSCF故障恢复功能”。
配置实例 :场景说明 :AMF根据license和配置开关控制"AMF基于UDM支持P-CSCF故障恢复"功能。 
AMF在向UDM发起注册时携带pcscfRestorationCallbackUri和amfServiceNamePcscfRest参数，表示支持PCSCF故障恢复 
数据规划 :配置项|参数名称|取值
---|---|---
P-CSCF故障恢复配置|AMF支持基于UDM的P-CSCF故障恢复功能|是
配置步骤 :步骤|说明|操作
---|---|---
1|修改P-CSCF故障恢复配置|SET UDMPCSCFRESTORCFG:SUPPCSCFRESTORE="SUPTPCSCFRESTORE"
场景说明 :UE注册完成后创建默认数据PDU会话，创建IMS PDU会话。 
P-CSCF网元故障或者其他网元发生故障，UDM触发故障恢复。 
AMF和SMF正常，AMF收到UDM的P-CSCF故障恢复。 
AMF给UDM回成功响应。 
AMF释放向SMF发送IMS PDU会话连接释放，发送Nsmf_PDUSession_UpdateSMContext通知SMF释放IMS 会话PDU连接，通知SMF发起IMS PDU会话释放重建。 
数据规划 :配置项|参数名称|取值
---|---|---
P-CSCF故障恢复配置|AMF支持基于UDM的P-CSCF故障恢复功能|是
配置步骤 :步骤|说明|操作
---|---|---
1|修改P-CSCF故障恢复配置|SET UDMPCSCFRESTORCFG:SUPPCSCFRESTORE="SUPTPCSCFRESTORE"
场景说明 :UE注册完成后创建默认数据PDU会话，未创建IMS PDU会话。 
P-CSCF网元故障或者其他网元发生故障，UDM触发故障恢复。 
AMF和SMF正常，AMF收到UDM的P-CSCF故障恢复。 
AMF给UDM回成功响应。 
AMF根据开关“支持无IMS会话的P-CSCF恢复功能”控制是否去注册用户（原因是再注册）。 
UE后续重新发起注册。 
数据规划 :配置项|参数名称|取值
P-CSCF故障恢复配置|AMF支持基于UDM的P-CSCF故障恢复功能|是
支持无IMS会话的P-CSCF故障恢复功能|P-CSCF故障恢复配置|是
配置步骤 :步骤|说明|操作
---|---|---
1|修改P-CSCF故障恢复配置|SET UDMPCSCFRESTORCFG:SUPPCSCFRESTORE="SUPTPCSCFRESTORE",SUPPCSCFNOIMSPDU="SUPTPCSCFNOIMSPDU"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|支持P-CSCF恢复，初始SUCI注册
---|---
测试目的|支持P-CSCF恢复，初始SUCI注册，向UDM注册时携带pcscfRestorationCallbackUri和amfServiceNamePcscfRest
预置条件|“AMF基于UDM支持P-CSCF故障恢复功能”license打开，支持P-CSCF恢复功能
测试过程|UE发起初始SUCI注册
通过准则|AMF向UDM注册消息中携带pcscfRestorationCallbackUri和amfServiceNamePcscfRest
测试结果|–
测试项目|收到UDM的P-CSCF恢复通知，有IMS会话，IMS会话关联的SMF正常，用户连接态
---|---
测试目的|收到UDM的P-CSCF恢复通知，有IMS会话，IMS会话关联的SMF正常，用户连接态
预置条件|1.“AMF基于UDM支持P-CSCF故障恢复功能”license打开，支持P-CSCF恢复功能2.用户有IMS会话
测试过程|1.UDM给AMF发送P-CSCF恢复通知2.AMF检测到IMS对应的SMF正常3.用户处于连接态
通过准则|1.响应UDM成功2.AMF向SMF发送IMS会话释放请求，携带原因值REL_DUE_TO_REACTIVATION3.SMF响应消息中未携带N1N2Transfer，SMF触发N1N2Transfer释放IMS会话，AMF透传给RAN和UE
测试结果|–
测试项目|收到UDM的P-CSCF恢复通知，无IMS会话，支持无IMS会话的P-CSCF恢复，用户连接态
---|---
测试目的|收到UDM的P-CSCF恢复通知，无IMS会话，支持无IMS会话的P-CSCF恢复，用户连接态
预置条件|1.“AMF基于UDM支持P-CSCF故障恢复功能”license打开，支持P-CSCF恢复功能，支持无IMS会话的P-CSCF恢复2.用户无IMS会话
测试过程|1.UDM给AMF发送P-CSCF恢复通知2.用户处于连接态
通过准则|1.响应UDM成功2.AMF去注册用户，携带re-register
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## 5G-GUTI 
5G Globally Unique Temporary Identity5G全球唯一临时标识
AMF :Access and Mobility Management Function接入和移动管理功能
AUSF :Authentication Server Function鉴权服务器功能
## CSCF 
Call Session Control Function呼叫对话控制功能
## DC 
Data Center数据中心
IMS :IP Multimedia SubsystemIP多媒体子系统
## MT 
Mobile Terminal移动终端
NRF :NF Repository Function网络功能仓储
## NSSAI 
Network Slice Selection Assistance Information网络切片选择辅助信息
NSSF :Network Slice Selection Function网络切片选择功能
PCF :Policy Control Function策略控制功能
PDN :Packet Data Network分组数据网
SMF :Session Management Function会话管理功能
## SMSF 
Short Message Service Function短消息服务功能
UDM :Unified Data Management统一数据管理
UE :User Equipment用户设备
URI :Uniform Resource Identifier统一资源标识符
VoNR :Voice over New Radio新空口承载语音
# ZUF-79-22 专网 
## ZUF-79-22-001 AMF支持PNI-NPN(CAG) 
特性描述 :特性描述 :描述 :定义 :PNI-NPN：非独立专网，指在PLMN上提供NPN。对于PNI-NPN，可以通过专用DNN或者切片来标识。由于网络切片不能制止UE自动接入非PNI-NPN允许接入的区域，因此需要通过CAG，制止UE接入非PNI-NPN允许的小区。
背景知识 :企业和行业构建无线专网，可以降低成本，提高效率，改进质量，增加收益。 
早在2G时代，企业和行业就存在大量的专网需求并部署了大量的通信私网，其中包括行业应用和通信终端，涉及性能提升、开通、灵活定制、SLA、安全内网、智能操控、自服务和服务集成等众多内在要求。 
在5G时代构建无线专网，按照5G专网和运营商公共网络的关系，可以考虑以下几种方案。 
独立非公共网络（SNPN） 
无线网络和核心网以独立网络实现专网功能，定义SNPN ID，提供接入控制、网络和小区选择等功能，但是需要SNPN商用终端。 
集成在公共网络的非公共网络（PNI-NPN） 
无线网络和核心网需要升级支持CAG功能，并且需要支持CAG功能的商用终端。
集成在公共网络的非公共网络（切片） 
专网用户使用特殊的S-NSSAI，通过切片可用性功能，定义S-NSSAI的有效范围。但是网络切片不提供接入控制功能，对网络侧性能会有影响。
网络共享（MOCN）
共享无线网络，专网仅需建立自己的核心网。 
目前，没有一种方案完美满足各种需求，需要企业或行业用户根据自身需求和能力，综合考虑预算、建网经验和运维团队等因素，选择合适的方案。5G专网的方案对比参见[表1]。
对比项|独立非公共网络（SNPN）|集成在公共网络的非公共网络（PNI-NPN）|集成在公共网络的非公共网络（切片）|网络共享（MOCN）
---|---|---|---|---
协议支撑|R16协议|R16协议|R15协议|R15协议
特点|完全独立的网络|使用PLMNPLMN需支持CAG|使用PLMNPLMN需支持网络切片|使用PLMN的RAN，但需要新建核心网RAN需支持MOCN
优势|不依赖公网可以根据专网特点新建移动网络，更好的满足专网的特殊需求维护方便|不需新建移动网络，仅需对PLMN升级改造支持CAG，成本（CAPEX、OPEX、TCO）低快速交付|不需新建移动网络，仅需为专网规划一个独立的网络切片，成本（CAPEX、OPEX、TCO）低快速交付维护方便|仅需新建核心网，成本（CAPEX、OPEX、TCO）适中交付速度适中维护方便可以根据专网特点新建核心网，更好的满足专网的特殊需求
劣势|新建移动网络，成本（CAPEX、OPEX、TCO）高交付时间长需要终端支持SNPN|依赖公网维护复杂需要终端支持CAG|依赖公网网络切片不提供网络接入控制功能，对网络侧性能有影响|依赖公网的RANMOCN有数量限制，数量过多则会影响RAN性能
应用场景 :根据用户是否可以接入PLMN小区，可分为如下两个场景。 
场景一： 专网用户仅能接入CAG小区用户仅能在被授权的CAG小区接入，进入非授权的CAG小区或PLMN小区，接入就会失败。 
场景二： 专网用户可接入CAG小区和PLMN小区用户可以在被授权的CAG小区和PLMN小区接入，进入非授权的CAG小区，接入才会失败。 
当签约CAG信息改变，导致用户在当前小区下不能继续接入时，AMF可以让用户下线后重新接入。 
客户收益 :受益方|受益描述
---|---
运营商|通过为企业或行业用户提供专网服务，提高运营收益，提升用户满意度。
移动用户|作为专网用户，享受定制化的业务。
实现原理 :系统架构 :AMF支持PNI-NPN功能，PNI-NPN通过专用的切片或DNN标识，通过CAG功能控制UE的接入区域。
AMF支持CAG功能，需要通过UDM获取签约数据，再结合UE能力和本地策略，确定UE的Allowed CAG List，并提供给UE和NR，同时AMF根据UE的Allowed CAG List信息，在UE接入AMF时，判断UE是否允许接入。 
PNI-NPN的系统架构如[图1]所示。
图1  PNI-NPN系统架构

涉及的网元 :网元名称|网元作用
---|---
UE|支持CAG功能，支持PNI-NPN对应的DNN或切片激活PDU会话。
NR|支持CAG功能，支持PNI-NPN对应的切片激活的PDU会话。
AMF|支持CAG功能，支持PNI-NPN对应的DNN或切片激活PDU会话。
SMF|支持PNI-NPN对应的DNN或切片激活PDU会话。
UPF|支持PNI-NPN对应的DNN或切片激活的PDU会话。
NSSF|支持PNI-NPN对应的切片。
UDM|支持签约CAG功能，支持签约PNI-NPN对应的DNN或切片。
NRF|支持根据PNI-NPN对应的DNN或切片选择SMF。
PCF|支持根据PNI-NPN对应的DNN或切片下发策略给SMF，支持根据PNI-NPN对应的DNN或切片下发URSP规则给UE。
协议栈 :接口|协议栈信息参考
---|---
N1|ZUF-79-19-001 N1
N2|ZUF-79-19-002 N2
N8|ZUF-79-19-003 N8
N11|ZUF-79-19-004 N11
N14|ZUF-79-19-006 N14
N15|ZUF-79-19-007 N15
N22|ZUF-79-19-008 N22
Nnrf|ZUF-79-19-010 Nnrf
本网元实现 :AMF支持PNI-NPN，一方面是支持根据特定DNN或特定切片选择SMF，另一方面是支持CAG功能。目前，AMF已支持根据特定DNN或特定切片选择SMF。 
AMF支持CAG功能，包括以下内容。 
AMF支持根据UE的签约CAG、UE的CAG能力和本地策略，确定UE的Allowed CAG List信息，将信息下发给UE，并通过移动限制列表指示给RAN。 
AMF支持在UE使用Initial UE Message消息发起初始注册/注册更新/业务请求流程时，根据UE当前接入小区支持的CAG信息，判断UE是否可以接入。 
当签约的CAG信息变更时，UDM通知AMF新的签约CAG信息。AMF收到UE新的签约CAG信息后，通知UE新的CAG列表，重新配置UE的Allowed CAG列表和/或CAG-only indication信息。AMF收到UE的确认消息后，通知UDM更新签约的CAG信息成功。AMF也通过更新移动限制列表，把新的CAG列表信息指示给RAN。如果新的签约CAG信息导致用户不能在当前小区下接入，AMF可以基于本地策略，让用户下线再重新上线。 
支持CAG的UE，可以支持紧急呼叫。仅支持接入CAG小区的UE，在普通PLMN下的小区或在不允许的CAG列表中的小区发起紧急业务，AMF需把非紧急呼叫的PDU会话释放掉，对于紧急呼叫的PDU会话，AMF基于本地策略确定是否允许接入。 
AMF确定UE Allowed CAG List的方法如下。 
获取用户的SUPI。使用SUPI匹配“基于SUPI号段CAG策略配置”，如果匹配到CAG策略，则执行步骤1a~1d；如果匹配不到，则执行步骤2。 
如果CAG策略为“签约”，则把签约的CAG List和CAG only作为UE的Allowed CAG List和Used CAG only。 
如果CAG策略为“本地”，则把本地配置的CAG List和CAG only作为UE的Allowed CAG List和Used CAG only。 
如果CAG策略为“签约与本地交集”，则把本地配置的CAG List和签约的CAG List的交集作为UE的Allowed CAG List，本地配置的CAG only和签约的CAG only都为“是”时，Used CAG only为“是”。 
如果CAG策略为“签约与本地并集”，则把本地配置的CAG List和签约的CAG List的并集作为UE的Allowed CAG List，本地配置的CAG only或签约的CAG only为“是”时，Used CAG only为“是”。 
使用“缺省CAG策略配置”。 
如果CAG策略为“签约”，则把签约的CAG List和CAG only作为UE的Allowed CAG List和Used CAG only。 
如果CAG策略为“本地”，则把本地配置的CAG List和CAG only作为UE的Allowed CAG List和Used CAG only。 
如果CAG策略为“签约与本地交集”，则把本地配置的CAG List和签约的CAG List的交集作为UE的Allowed CAG List，本地配置的CAG only和签约的CAG only都为“是”时，Used CAG only为“是”。 
如果CAG策略为“签约与本地并集”，则把本地配置的CAG List和签约的CAG List的并集作为UE的Allowed CAG List，本地配置的CAG only或签约的CAG only为“是”时，Used CAG only为“是”。AMF支持PNI-NPN，需要AMF支持CAG功能。CAG功能主要涉及注册、业务请求、寻呼、基于N2口的切换等。 
业务流程 :AMF支持PNI-NPN，需要AMF支持CAG功能。CAG功能主要涉及注册、业务请求、寻呼、基于N2口的切换等。 
初始注册/注册更新
在初始注册和注册更新流程中，AMF对CAG接入的处理是相同的，本节以初始注册过程为例，描述注册过程中对CAG的处理。 
图2  初始注册

流程说明： 
UE发起注册流程，发送初始注册请求消息，消息中携带5GMM Capability信息，5GMM Capability信息中的CAG标识置位为1。 
NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG列表。 
（可选）AMF执行对UE的鉴权过程。 
（可选）如果AMF本地没有用户签约数据，则AMF向UDM获取用户签约的切片数据。 
（可选）如果AMF需要向NSSF获取用户允许的切片，则AMF完成向NSSF获取用户允许的切片过程。 
AMF确定不需重定向。 
（可选）如果AMF之前没有向UDM注册，则AMF向UDM注册、获取用户签约数据、订阅签约数据变更通知。 
如果AMF向UDM获取用户签约数据，则AMF向UDM发送Nudm_SDM_Get Request消息，携带Feature Negotiation信息，Feature Negotiation信息中的CAGFeature置位为1；UDM向AMF返回Nudm_SDM_Get Response消息，消息中携带Access and Mobility Subscription Data等信息，Access and Mobility Subscription Data信息中包含签约的CAG信息。 
AMF根据UE的CAG能力信息、签约CAG信息、本地策略，确定UE的Allowed CAG List信息。 
AMF根据NR携带的当前接入小区的CAG列表和UE的Allowed CAG List，判定至少有一个相同的CAG，则用户可以正常接入该CAG小区。 
（可选）如果需要建立AM策略关联，则AMF向PCF发起建立AM策略关联过程。 
（可选）AMF向UE发送注册接受消息，消息中携带CAG Information List信息，包含UE的Allowed CAG List。 
如果注册接受消息在Initial Context Setup Request消息中投递给UE，则Initial Context Setup Request消息需要携带Mobility Restriction List信息，Mobility Restriction List信息中包含NPN Mobility Information信息，NPN Mobility Information信息中包含UE的Allowed CAG List信息。 
如果注册接受消息在Downlink Direct Transfer消息中投递给UE，则Downlink Direct Transfer消息需要携带Mobility Restriction List信息，Mobility Restriction List信息中包含NPN Mobility Information信息，NPN Mobility Information信息中包含UE的Allowed CAG List信息。 
NR给UE转发注册接受消息。 
（可选）如果NR收到了AMF的Initial Context Setup Request消息，则NR向AMF返回Initial Context Setup Response消息。 
（可选）UE向AMF返回注册完成消息。 
（可选）如果需要建立UE策略关联，则AMF向PCF发起建立UE策略关联过程。 
（可选）AMF判断在初始注册过程中是否向UDM获取了Access and Mobility Subscription Data等签约信息，如果没有，则不需通知UDM；如果有，则AMF向UDM发送Nudm_SDM_Info Request消息，通知UDM已经把最新的签约CAG信息发送给UE了，UDM向AMF返回Nudm_SDM_Info Response消息。 
业务请求
业务请求过程对CAG的处理如[图3]所示。
图3  业务请求

流程说明： 
UE处于空闲态，有上行信令或数据报文需要发送，或收到寻呼消息，则UE发起业务请求消息。 
NR收到UE的业务请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG列表。 
（可选）AMF执行对UE的鉴权过程。 
AMF取用注册过程中为UE确定的Allowed CAG List信息。 
AMF根据NR携带的当前接入小区的CAG列表和UE的Allowed CAG List，判定至少有一个相同的CAG，则用户可以正常接入该CAG小区。 
AMF通知SMF更新PDU会话。 
（可选）如果PDU会话需要建立UP Connectivity，则AMF向NR发送Initial Context Setup Request消息，消息中携带业务接受消息和Mobility Restriction List信息，Mobility Restriction List信息中包含NPN Mobility Information信息，NPN Mobility Information信息中包含UE的Allowed CAG List信息。 
NR转发业务接受消息给UE。 
（可选）如果NR收到了AMF的Initial Context Setup Request消息，则NR给AMF返回Initial Context Setup Response消息。 
AMF通知SMF更新PDU会话。 
寻呼过程
UE处于空闲态，AMF寻呼用户时，需在寻呼消息中把为UE确定的Allowed CAG List信息也携带给NR，使NR选择合适的CAG小区寻呼用户。 
切换过程
基于Xn口的切换，NR间直接交互，如果目标小区不允许UE接入，目标NR直接发送拒绝消息给源NR，AMF无感知。 
基于N2口的切换，如果目标小区不允许UE接入，则目标NR返回拒绝消息给AMF，AMF转发给源NR，处理过程如[图4]所示。
图4  N2口切换

流程说明： 
Source NR发起N2口切换流程，发送Handover Required消息给Source AMF。 
（可选）Source AMF判断是否为跨AMF的切换。如果是，则选择Target AMF。 
Source AMF向Target AMF发送Namf_Communication_CreateUEContext Request消息，携带SupportedFeatures信息，SupportedFeatures信息中的NPN标识置位为1。 
Target AMF通知SMF更新PDU会话。 
Target AMF向Target NR发送Handover Request消息，携带Mobility Restriction List信息（包含UE的Allowed CAG List信息）。 
Target NR发现目标小区不允许UE接入。 
Target NR返回Handover Preparation Failure消息给Target AMF，携带Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container信息。 
Target AMF向Source AMF返回Namf_Communication_CreateUEContext Response消息，携带#403 Forbidden，消息中携带缓存的Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container信息。 
Source AMF向Source NR发送Handover Failure消息，携带Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container信息。 
签约信息变更
当签约的CAG信息变更时，处理过程如[图5]所示。
图5  CAG信息变更

流程说明： 
UDM检测到签约的CAG信息改变，且目前注册的AMF支持CAG，则发起签约数据变更流程，向AMF发送Nudm_SDM_Notification消息，消息中携带新的签约CAG信息。AMF向UDM返回确认消息。 
AMF根据UE的CAG能力信息、新的签约CAG信息、本地策略，确定新的UE Allowed CAG List信息。 
AMF比较新的Allowed CAG List和老的Allowed CAG List信息后，发现发生了改变。 
（可选）如果UE处于空闲态，则AMF寻呼用户并处理用户的业务请求。 
AMF发送Downlink Direct Transfer消息给NR。 
AMF发送Downlink Direct Transfer消息给NR，携带Configuration Update Command消息，消息中携带Configuration Update Indication和新的Allowed CAG List信息。Configuration Update Indication指示UE需要返回确认消息但不需要重新注册。如果新的Allowed CAG List信息还没有通过Mobility Restriction List带给NR，则在携带Configuration Update Command的Downlink Direct Transfer消息中，携带Mobility Restriction List信息，Mobility Restriction List信息中包含新的UE Allowed CAG List信息。 
如果根据新的Allowed CAG List，发现用户当前所在小区不允许用户接入，且根据本地策略，判断需要下线用户，则AMF发送Downlink Direct Transfer消息给NR，携带De-registration Request消息和新的Allowed CAG List信息。 
NR转发Configuration Update Command消息给UE。如果下线用户，则NR转发De-registration Request消息给UE。 
UE返回Configuration Update Complete消息给AMF。如果下线用户，则UE返回De-registration Accept消息给AMF。 
AMF向UDM发送Nudm_SDM_Info Request消息，通知UDM已经把最新的签约CAG信息发送给UE。UDM返回Nudm_SDM_Info Response消息。 
系统影响 :PNI-NPN功能在实际网络运行中性能占比较小，对系统的影响较小。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.501: "System Architecture for the 5G System;Stage 2".|5.30.3 Public Network Integrated NPN
3GPP TS 23.502: "Procedures for the 5G System;Stage2".|全部
特性能力 :名称|指标
---|---
单个小区下每个PLMN支持的CAG个数|12（个）
单个用户每个PLMN下Allowed CAG个数|12（个）
单个用户每个PLMN下签约的CAG个数|12（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
02|V7.21.40|增加签约CAG信息改变的策略。
01|V7.20.40|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特定的服务。 
该特性需要开启License，对应的License项目为“AMF支持PNI-NPN功能”（License ID：7236），此项目显示为“支持”，表示AMF支持PNI-NPN功能。 
对其他网元的要求 :UE|gNodeB|UDM|PCF|SMF|UPF|NSSF|NRF
---|---|---|---|---|---|---|---
√|√|√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :需要根据规划，设置本局决策UE的Allowed CAG List的策略。 
O&M相关 :命令 :配置项|命令
---|---
缺省CAG策略配置|SET DEFAULT CAG POLICY
SHOW DEFAULT CAG POLICY|缺省CAG策略配置
基于SUPI号段CAG策略配置|ADD SUPI CAG POLICY
SET SUPI CAG POLICY|基于SUPI号段CAG策略配置
DEL SUPI CAG POLICY|基于SUPI号段CAG策略配置
SHOW SUPI CAG POLICY|基于SUPI号段CAG策略配置
CAG Profile配置|ADD CAG PROFILE
SET CAG PROFILE|CAG Profile配置
DEL CAG PROFILE|CAG Profile配置
SHOW CAG PROFILE|CAG Profile配置
CAG Profile组配置|ADD CAG GROUP
SET CAG GROUP|CAG Profile组配置
DEL CAG GROUP|CAG Profile组配置
SHOW CAG GROUP|CAG Profile组配置
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过CAG相关配置，可以实现PNI-NPN功能。让企业和行业用户在公网的基础上，使用较低的成本构建无线专网，提高效率，改进质量，增加收益。 
配置前提 :AMF运行正常。 
EM网管能正常连接并登录。 
支持 "AMF支持PNI-NPN功能" License。 
打开PNI-NPN开关。 
配置过程 :###### 场景一：专网用户仅能接入CAG小区 
执行[SET DEFAULT CAG POLICY]命令，修改缺省CAG策略配置。
###### 场景二：专网用户可接入CAG小区和PLMN小区 
执行[ADD CAG PROFILE]命令，新增CAG Profile配置。
执行[ADD CAG GROUP]命令，新增CAG Profile组配置。
执行[ADD SUPI CAG POLICY]命令，新增基于SUPI号段CAG策略配置。
执行[SET DEFAULT CAG POLICY]命令，修改缺省CAG策略配置。
###### 场景三：UDM签约变更后去注册用户 
执行[SET DEFAULT CAG POLICY]命令，修改缺省CAG策略配置。
配置实例 :场景一 :场景说明
专网用户仅能接入CAG小区。 
数据规划
配置项|参数|取值
---|---|---
缺省CAG策略配置|是否支持PNI-NPN|是|是
是否支持基于SUPI号段的CAG策略|缺省CAG策略配置|否|否
CAG策略|缺省CAG策略配置|签约|签约
UE不支持CAG并且被CAG限制接入时的拒绝原因值|缺省CAG策略配置|15 - No suitable cells in tracking area|15 - No suitable cells in tracking area
配置步骤
步骤|说明|操作
---|---|---
1|配置缺省CAG策略|SET DEFAULT CAG POLICY:IFSPRTPNINPN="SPRTPNINPN",IFSPRTSUPICAG="NOTSPRTSUPICAG",CAGPOLICY="SUB",NOSPRTCAGREJCAUSE="NOSUITABLECELLSINTA"
场景二 :场景说明
专网用户可接入CAG小区和PLMN小区。 
数据规划
配置项|参数|取值
---|---|---
CAG Profile配置|CAG Profile标识|1|1
移动国家码|CAG Profile配置|460|460
移动网络码|CAG Profile配置|11|11
CAG标识|CAG Profile配置|12345678|12345678
CAG ONLY指示|CAG Profile配置|NOT CAG ONLY|NOT CAG ONLY
CAG Profile组配置|CAG Profile组标识|1|1
CAG Profile标识|CAG Profile组配置|1|1
基于SUPI号段CAG策略配置|SUPI号段|46011|46011
CAG策略|基于SUPI号段CAG策略配置|本地|本地
CAG Profile组标识|基于SUPI号段CAG策略配置|1|1
缺省CAG策略配置|是否支持PNI-NPN|是|是
是否支持基于SUPI号段的CAG策略|缺省CAG策略配置|是|是
CAG策略|缺省CAG策略配置|签约|签约
UE不支持CAG并且被CAG限制接入时的拒绝原因值|缺省CAG策略配置|15 - No suitable cells in tracking area|15 - No suitable cells in tracking area
配置步骤
步骤|说明|操作
---|---|---
1|配置CAG Profile|ADD CAG PROFILE:CAGPROFILEID=1,MCC="460",MNC="11",CAGID="12345678",CAGONLY="NO"
2|配置CAG Profile组|ADD CAG GROUP:CAGGROUPID=1,CAGPROFILEID=1
3|配置基于SUPI号段CAG策略|ADD SUPI CAG POLICY:SUPISEGMENT="46011",CAGPOLICY="LOCAL",CAGGROUPID=1
4|配置缺省CAG策略|SET DEFAULT CAG POLICY:IFSPRTPNINPN="SPRTPNINPN",IFSPRTSUPICAG="SPRTSUPICAG",CAGPOLICY="SUB",NOSPRTCAGREJCAUSE="NOSUITABLECELLSINTA"
场景三 :场景说明
UDM签约变更后，若新的签约CAG信息和小区下CAG信息无交集，去注册用户。 
数据规划
配置项|参数|取值
---|---|---
缺省CAG策略配置|是否支持PNI-NPN|是|是
是否支持基于SUPI号段的CAG策略|缺省CAG策略配置|是|是
CAG策略|缺省CAG策略配置|签约|签约
UE不支持CAG并且被CAG限制接入时的拒绝原因值|缺省CAG策略配置|15 - No suitable cells in tracking area|15 - No suitable cells in tracking area
新的签约CAG信息和小区下CAG信息无交集时是否去注册用户|缺省CAG策略配置|是|是
配置步骤
步骤|说明|操作
---|---|---
1|配置缺省CAG策略|SET DEFAULT CAG POLICY:IFSPRTPNINPN="SPRTPNINPN",IFSPRTSUPICAG="SPRTSUPICAG",CAGPOLICY="SUB",NOSPRTCAGREJCAUSE="NOSUITABLECELLSINTA",IFDETACHUESUBCHANGE="YES"
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|注册流程，终端支持CAG，用户仅能接入CAG小区，最终协商的CAG List与UE当前接入小区支持的CAG List无交集，注册拒绝
---|---
测试目的|注册流程，终端支持CAG，用户仅能接入CAG小区，最终协商的CAG List与UE当前接入小区支持的CAG List无交集，注册拒绝，AMF下发原因值：76（原因值固定）。
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|UE发起注册流程，发送初始注册请求消息，消息中携带5GMM Capability信息（CAG标识置位为1）。NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG List。UDM向AMF返回Nudm_SDM_Get Response消息，消息中携带Access and Mobility Subscription Data等信息，Access and Mobility Subscription Data信息中包含签约的CAG信息。AMF向UDM获取用户的签约信息，得到的CAG List与当前小区支持的CAG List没有交集，注册拒绝。
通过准则|AMF拒绝用户接入，下发NAS原因值：76。
测试结果|–
测试项目|注册流程，终端不支持CAG，用户仅能接入CAG小区，最终协商的CAG List与UE当前接入小区支持的CAG List无交集，注册拒绝
---|---
测试目的|注册流程，终端不支持CAG，用户仅能接入CAG小区，最终协商的CAG List与UE当前接入小区支持的CAG List无交集，注册拒绝，AMF下发原因值：15（原因值从缺省CAG策略配置获取）。
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|UE发起注册流程，发送初始注册请求消息，消息中携带5GMM Capability信息（CAG标识置位为0）。NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG List。UDM向AMF返回Nudm_SDM_Get Response消息，消息中携带Access and Mobility Subscription Data等信息，Access and Mobility Subscription Data信息中包含签约的CAG信息。AMF向UDM获取用户的签约信息，得到的CAG List与当前小区支持的CAG List没有交集，注册拒绝。
通过准则|AMF拒绝用户接入，下发NAS原因值：15 。
测试结果|–
测试项目|业务请求流程因CAG限制提前结束
---|---
测试目的|业务请求流程，终端支持CAG，用户仅能接入CAG小区，最终协商的CAG List与UE当前接入小区支持的CAG List无交集，AMF拒绝UE的业务请求，下发原因值：76（原因值固定）。
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|UE发起业务请求流程，消息中携带5GMM Capability信息（CAG标识置位为0）。NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG List。注册上下文中保存的协商CAG List与当前小区支持的CAG List无交集。
通过准则|AMF拒绝用户接入，下发NAS原因值：76。
测试结果|–
测试项目|寻呼消息携带CAG List信息
---|---
测试目的|UE处于空闲态，AMF寻呼用户时，需在寻呼消息中把Allowed CAG List信息也携带给NR，使NR选择合适的CAG小区寻呼用户。
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|UE发起注册流程，发送初始注册请求消息，消息中携带5GMM Capability信息（CAG标识置位为1）。NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG列表。UDM向AMF返回Nudm_SDM_Get Response消息，消息中携带Access and Mobility Subscription Data等信息，Access and Mobility Subscription Data信息中包含签约的CAG信息。AMF向UDM获取用户的签约信息，得到的CAG List与当前小区支持的CAG List有交集，UE在AMF上注册成功。N2接口释放，UE进入空闲态。AMF向NR侧发送寻呼消息，寻呼消息携带CAG List信息。
通过准则|寻呼消息携带CAG List信息。
测试结果|–
测试项目|切换流程处理CAG信息
---|---
测试目的|基于N2口的切换，如果目标小区不允许UE接入，则目标NR返回拒绝消息给AMF，AMF转发给源侧RAN。
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|源AMF局切目标AMF局时，源AMF局携带用户签约的CAG List信息。目标AMF局将协商好的CAG信息通过Handover Request消息带给目标NR。目标NR发现自身的Cell CAG List和AMF发送过来的CAG List没有交集，向目标AMF回复失败，并携带Container。Container被源AMF透传给源侧NR。
通过准则|基于N2口的切换，如果目标小区不允许UE接入，则返回拒绝消息给AMF，AMF转发给源侧NR。
测试结果|–
测试项目|连接态签约变更流程
---|---
测试目的|用户的签约的CAG信息变更，AMF能通知NR侧用户最新的Allowed CAG List。
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|UE发起注册流程，发送初始注册请求消息，消息中携带5GMM Capability信息（CAG标识置位为1）。NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG List。UDM向AMF返回Nudm_SDM_Get Response消息，消息中携带Access and Mobility Subscription Data等信息，Access and Mobility Subscription Data信息中包含签约的CAG信息。AMF向UDM获取用户的签约信息，得到的CAG List与当前小区支持的CAG List有交集，UE在AMF上注册成功。UDM发起签约变更，携带新的CAG信息。AMF给NR下发Configuration Update Command，携带最新的Allowed CAG List。
通过准则|AMF向NR发送Downlink NAS Transport，向UE发送Configuration update command，通知它们最新的Allowed CAG List。
测试结果|–
测试项目|用户关机，AMF正常处理用户的去注册消息
---|---
测试目的|用户关机，AMF正常处理用户的去注册消息
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为15-TA内没有合适的小区。
测试过程|UE发起注册流程，发送初始注册请求消息，消息中携带5GMM Capability信息（CAG标识置位为1）。NR收到UE的初始注册请求消息后，通过Initial UE Message消息转发给AMF，同时携带NPN Access Information信息，NPN Access Information信息中包含了UE当前接入小区支持的CAG List。UDM向AMF返回Nudm_SDM_Get Response消息，消息中携带Access and Mobility Subscription Data等信息，Access and Mobility Subscription Data信息中包含签约的CAG信息。AMF向UDM获取用户的签约信息，得到的CAG List与当前小区支持的CAG List有交集，UE在AMF上注册成功。AMF收到UE的关机去注册消息， 正常处理用户的去注册消息。
通过准则|AMF正确处理UE的关机去注册请求，完成去注册。
测试结果|–
测试项目|UDM中签约数据改变后，签约的CAG List与当前小区支持的CAG List无交集，通知UE去注册
---|---
测试目的|验证UDM中签约数据改变后，签约的CAG List与当前小区支持的CAG List无交集，通知UE去注册
预置条件|已配置AMF支持PNI-NPN功能，CAG策略为签约，UE不支持CAG并且被CAG限制接入时的拒绝原因值为“15-TA内没有合适的小区”。
测试过程|场景一：UE在专网注册成功。AMF向UDM注册，获取签约信息，订阅成功。修改用户的CAG签约数据，将CAG从CAG List中清除，发送Notify通知AMF。AMF收到UDM的签约信息修改后，发现CAG List为空，则发起去注册流程通知UE下线。场景二：UE在公网注册成功。AMF向UDM注册，获取签约信息，订阅成功。修改用户的CAG签约数据，将CAG从CAG List中清除，发送Notify通知AMF。AMF收到UDM的签约信息修改后，发现CAG List为空，通过Configuration Update Command消息通知UE。
通过准则|针对用户当前的驻留网络分为两种场景进行测试。终端在专网注册时，AMF收到UDM的签约修改消息后，判断CAG List不包含基站携带的CAG ID，则发起去注册流程，通知UE下线。终端在公网注册时，AMF收到UDM的签约修改消息后，判断CAG List不包含基站携带的CAG ID，下发Configuration Update Command给UE，携带空的CAG Information List。
测试结果|–
常见问题处理 :无。 
# 缩略语 
# 缩略语 
## CAG 
Closed Access Group闭合接入组
## CAPEX 
Capital Expenditure资本性支出
DNN :Data Network Name数据网名称
## MOCN 
Multi-Operator Core Network多运营商核心网
## OPEX 
Operating Expenditure运营性支出
## PNI-NPN 
Public Network Integrated NPN公共网络集成的NPN网络，即非独立专网
S-NSSAI :Single Network Slice Selection Assistance Information单个网络切片选择辅助信息
## TCO 
Total Cost of Ownership总体拥有成本
