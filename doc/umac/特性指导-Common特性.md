# ZUF-76-01 系统架构 
## ZUF-76-01-001 支持与UDSF/CDB合一部署 
特性描述 : 
特性描述 : 
术语 : 
术语|含义
---|---
非结构化数据|是指存储在UDSF中的，不采用Schema/数据字典定义的数据。一般是与特定NF相关，由NF自身来解析的透明数据，如与特定NF相关的会话数据、状态数据、链路数据等。
结构化数据|是指存储在UDR中的通过Schema/数据字典定义的数据，主要指用户业务签约数据、策略数据、能力开放数据等。
计算与存储分离|是指网络中将计算密集型NF（如AMF、SMF等）与存储密集型NF（如UDSF）分离，计算密集型NF侧重于应用业务逻辑的处理，存储密集型NF侧重于数据的存储与访问。计算密集型NF可以将状态数据存放在存储密集型NF中，实现业务组件无状态以及组件间负荷分担特性。
无状态|是指业务组件中不再保存持久化状态，用户可以通过任一业务组件来进行业务处理，从而实现业务组件间负荷分担。
K/V数据读写接口|是指从采用“键”/“值”存储的数据库中，通过如下接口来访问其中的数据：Get（key）：通过“键”标识查询以前存储的相关数据。Set（key, value )：在“键”标识下存储这个“值”，若该“键”标识下已有“值”，则替换该“值”。Delete（key)：删除以该“键”标识下的数据。
数据老化|是指数据库中当前时间已晚于数据记录中的“过期时间（Expired Time）”，这部分数据记录属于老化数据，会自动删除。
数据分布|是指数据在各个CDN节点上分布情况。一个租户的数据是按照HASH算法，根据主键标识，均匀分布在各个CDN节点上。
多主复制|是指在地理容灾的情况下，每个站点都可同时进行读写操作。当需要将写的内容同步到另一个站点时，两站点之间可以双向进行数据复制。
描述 : 
定义 : 
统一数据层是指将5GC中相关控制类NF的非结构化数据放到CUDR（UDSF）中。
基于统一数据层，5GC实现了计算与存储分离。计算与存储分离是把计算密集型的业务NF和存储密集型的NF（UDSF）分离，业务网元专注于无状态的业务逻辑处理，不存储和维护数据；数据类的网元（UDSF）统一存储和管理业务网元所需数据。 
CUDR（UDSF）可存储业务NF的数据。业务NF通过统一或通用的数据访问接口，实时从CUDR（UDSF）读写数据，实现业务和数据解耦和隔离。 
CUDR（UDSF）支持严格的个人数据保护措施。通过严格的操作权限控制操作员的访问，基于操作界面匿名化、在线数据导出匿名化、离线数据匿名化、数据传输过程加密保护等措施尽力避免个人用户数据泄露。 
背景知识 : 
面对万物互联5G时代多样化、极致通讯的需求，运营商需要构建更敏捷、更灵活的网络。NFV/SDN等虚拟化技术已经广泛应用到云化核心网中，实现了软硬件分离以及网络控制和转发的分离，降低TCO，但还存在如下挑战：
网络弹性不足：核心网各NF各自维护会话上下文数据，网元弹性、缩扩容需消耗较长时间进行迁移和恢复数据，难以实现快速的业务弹性、无损用户体验和加速新业务发布。 
数据孤岛：核心网各NF各自存储数据形成数据孤岛，难以分析和挖掘数据的价值。数据分散维护和管理，增加运维复杂度。 
通过统一数据层，5GC实现了计算与存储的分离，解决了网络弹性不足及数据孤岛问题，具有如下优势： 
快速、业务无损的网络弹性：控制类NF组件间无需迁移状态数据，实现秒级弹性。弹性过程中，状态数据不丢失，保证了业务的连续性。 
统一数据管理，简化运维，资源共享，降低OPEX和CAPEX：通过共享CUDR（UDSF），减少网络中数据库的数量和种类，降低了OPEX和CAPEX。业务逻辑无状态，业务处理组件从1+1主备演进为N+K负荷分担，减少了资源冗余。 
提高系统稳定性：业务逻辑无状态，业务组件支持N+K负荷分担，一个组件故障，其他组件可实时接管。基于分布式存储的会话上下文的数据库，支持本地容灾和地理容灾，提高了可靠性。 
有利于数据分析和业务创新：数据集中存储，简化数据的采集难度，有利于数据分析。支持多个应用间共享数据，方便业务创新。 
应用场景 : 
统一数据层主要适用于业务NF专有CUDR（UDSF）场景。
CUDR（UDSF）仅为该NF服务，不能被多个业务NF共享。CUDR（UDSF）一般每份数据有两个副本，并自动在副本间同步和恢复数据。专有CUDR（UDSF）组网如[图1]所示。
图1  专有CUDR
逻辑上，CUDR（UDSF）数据按照一致性HASH算法被切分为上千个数据分片，每个数据分片分别在左右域各一份。 
部署上，CUDR（UDSF）数据分片副本按照尽量均匀和反亲和的原则分布在不同CUDR（UDSF）节点上，不同CUDR（UDSF）节点分别在左域和右域。 
客户收益 : 
受益方|受益描述
---|---
运营商|实现快速、业务无损的网络弹性。统一数据管理，简化运维，资源共享，降低OPEX和CAPEX。提高系统稳定性。有利于数据分析和业务创新。
终端用户|此特性对终端用户不可见。
实现原理 : 
系统架构 : 
本特性涉及的系统架构如下图所示。 
图2  统一数据层示意图
在5GC网络中，业务NF专注于无状态的业务逻辑处理，将数据统一存储在CUDR（UDSF）上，由CUDR（UDSF）进行统一管理。
涉及的NF参见下表。 
NF|说明
---|---
业务NF|包括AMF、SMF、PCF等5GC业务NF，实现无状态业务逻辑处理以及快速网络弹性。
CUDR（UDSF）|统一存储和管理业务网元所需数据，实现业务与数据解耦。
CUDR（UDSF）的软件架构如下图所示。 
图3  CUDR（UDSF）软件架构
CUDR（UDSF）由上下文数据存储节点（CDN）、控制中心（CC）和客户端（CCA/CACHE）组成，对网元提供K/V数据读写接口。
[图3]中颜色相同的数据切片为同一数据切片的两个副本，副本之间互相进行数据同步以保证数据的高可靠性。
CC监控所有CDN和CCA/CACHE的状态，进行相关FCAPS操作维护和生命周期管理。
CUDR（UDSF）各组件及功能参见下表。 
组件|说明
---|---
CDN|数据读写访问数据复制/恢复/合并数据迁移
CC|系统管理：CDN节点和CCA/Cache状态维护、操作维护FCAPS和生命周期管理（LCM）控制入口
CCA|提供数据访问接口API数据分布路由管理：从CUDR（UDSF）中获取并缓存数据分布、CDN节点状态、选择数据访问路由信息
CACHE|管理和维护关系型内存库缓存客户端数据老化客户端数据从CDN加载数据向CDN同步数据
 说明： 
CUDR（UDSF）客户端可通过CACHE访问CDN，也可直接通过CCA访问CDN。 
协议栈 : 
N18/Nudsf是5GC NF和CUDR（UDSF）之间的接口。NF通过N18/Nudsf接口实现NF自身非结构化数据的存储与检索。该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N18/Nudsf|ZUF-79-19-011 N18
NF实现 : 
CUDR（UDSF）支持多租户机制，按照应用NF类型创建租户，避免不同NF数据间的相互影响，如图4所示。租户间隔离数据存储、数据访问、操作维护和生命周期管理，租户间无资源竞争。图4  CUDR（UDSF）支持多租户示意图 
CUDR（UDSF）客户端支持CACHE机制。CACHE为业务NF提供关系型数据存储和访问模型，数据以关系表的方式存储在本地内存数据库中。业务NF本地缓存临时热点数据，提升NF读写数据性能。CACHE向NF屏蔽CUDR数据节点，简化NF数据访问流程。 
CUDR（UDSF）采用分布式存储和计算架构。CUDR（UDSF）所有数据节点均可读可写，通过扩展数据节点，数据访问性能线性扩展。存储容量线性扩展，可提供100亿记录级别的海量数据存储。分布式存储逻辑上，CUDR（UDSF）数据按照一致性HASH算法被切分为上千个数据分片，每个数据分片有多个数据副本组成。部署上，CUDR（UDSF）数据分片副本按照尽量均匀和反亲和的原则分布在多个CUDR（UDSF）节点上，如图5所示。图5  CUDR（UDSF）分布式存储示意图图5中，1、2、3......表示数据分片副本1的编号，1'、2'、3'......表示数据分片副本2的编号，相同的数据存储在相同编号的两个副本上，副本之间互相同步保证数据的一致性。分布式计算CUDR（UDSF）每个数据节点都可处理数据读写操作，数据节点全负荷分担，无主备之分。 
CUDR（UDSF）支持数据复制。CUDR（UDSF）的数据复制是以数据分片为单位，优先级高的副本向其他优先级低的副本进行数据复制。对删除操作，采用操作码同步的方式向其他副本同步（即向其他副本同步Delete操作）。对非删除操作，基于日志方式向其他副本复制数据，将变更的数据及时同步到其他副本（即按照Set操作的日志，将所有日志同步到其他副本上）。支持基于日志和时间戳多主复制。数据复制有冲突时，采用时间和自定义规则方式自动合并和矫正冲突数据。某个节点故障而导致数据丢失时，通过在线恢复自动恢复数据。 
CUDR（UDSF）支持弹性伸缩和数据自迁移。CUDR（UDSF）支持根据各节点的CPU占用以及存储空间占用自动进行弹性伸缩。弹性伸缩过程中，数据根据新的规则重新分布，整个过程业务不中断。 
业务流程 : 
更新CUDR（UDSF）中用户数据
更新CUDR（UDSF）中用户数据的操作适用于如下场景： 
增加单条用户数据或多条用户数据。 
修改单条用户数据或多条用户数据。 
删除单条用户数据或多条用户数据。 
增加、删除、修改组合操作单条或多条用户数据。 
图6  更新CUDR（UDSF）中用户数据流程
流程说明如下： 
当业务NF需要更新用户数据时，向CCA/CACHE发起更新数据请求。 
CCA/CACHE向用户所在的CDN节点发起更新数据请求。 
CDN节点更新NF用户数据版本。 
CDN节点更新NF用户数据。 
CDN节点向CCA/CACHE返回更新数据响应。 
CCA/CACHE向业务NF返回更新数据响应。 
读取CUDR（UDSF）中用户数据
读取CUDR（UDSF）中用户数据的操作适合于查询单条用户数据或多条用户数据。NF用户数据以TLV（Type-Length-Value）编码格式存储到CUDR（UDSF）中，由NF根据版本自行编译。老版本对于新版本数据中无法识别的属性，按照忽略的原则处理。
图7  读取CUDR中用户数据流程
流程说明如下： 
业务NF在需要读取用户数据时，向CCA/CACHE发起读数据请求。 
CCA/CACHE向用户所在的CDN节点发起读数据请求。 
CDN节点查询出NF用户数据及版本。 
CDN节点向CCA/CACHE返回读数据响应。 
CCA/CACHE向NF返回读数据响应。 
NF检查返回响应的NF用户数据版本。 
（可选）若返回的NF用户数据的版本与NF的数据版本不同，NF根据版本不一致处理原则转换数据。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
CUDR（UDSF）只能和ZTE 5GC各业务NF配套使用，不支持其他厂家的NF。 
特性交互 : 
相关特性|交互关系
---|---
ZUF-76-01-002 软件无状态架构|本特性是软件无状态架构的前提，5GC只有采用了统一数据层，相关业务NF软件才能采用无状态架构。
遵循标准 : 
类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|Technical Specification Group Services and System Aspects;System Architecture for the 5G System;Stage 2.
3GPP|3GPP TS 23.502|Technical Specification Group Services and System Aspects; Procedures for the 5G System;Stage 2.
特性能力 : 
名称|指标|说明
---|---|---
CUDR （UDSF）数据节点总数|1000|一套CUDR中能够部署的最大CDN数量
记录总数|100亿|一套CUDR中能够容纳的最大“键”/“值”记录总数
支持的最大租户数|255|一套CUDR中能够支持的最大租户数，每个租户都有独立的CDN
每租户数据分片数|1024|每个租户按照“主键”HASH算法将用户数据分布到1024个数据分片中
每数据分片支持的副本数|1~4|每个数据分片支持1-4个副本，每个副本中的用户数据都相同
版本要求及变更记录 : 
序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 : 
License要求 : 
该特性为基本特性，无需License支持。 
O&M相关 : 
配置命令 : 
配置项|命令
---|---
租户配置|ADD CDBTENANT
DEL CDBTENANT|租户配置
SET CDBTENANT|租户配置
SHOW CDBTENANT|租户配置
参数配置|ADD CDBPARAM
SET CDBPARAM|参数配置
SHOW CDBPARAM|参数配置
DEL CDBPARAM|参数配置
定时器 : 
本特性暂时不涉及定时器的变化。 
性能统计 : 
该特性不涉及性能统计计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
话单与计费 : 
本特性暂时不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
在实例化的过程中，会自动增加租户配置和租户参数配置，并且会根据这些配置部署UDSF。实例化中存在两种业务场景：
场景一：业务NF专有场景此场景下只需要配置一个租户相关信息。先规划好租户的ID、名称，以及对应CDN节点的内存库大小等，再进行配置。 
场景二：多业务NF共享场景此场景下需要配置多个租户相关信息。先规划好多租户的ID、名称，以及每个租户下对应的CDN节点的内存库大小等，再进行配置。 
配置前提 : 
系统运行正常。 
配置过程 : 
在AMF节点下，执行[ADD CDBTENANT]命令，配置租户参数。
在AMF节点下，执行[ADD CDBPARAM]命令，配置租户的CDN节点。
#### 配置实例1 
配置场景 : 
业务NF专有CUDR场景，此种场景下只需要配置一个租户的相关参数，在实例化的时候会自动配置一个租户信息。
数据规划 : 
参数|取值
---|---
租户ID（TENANTID）|1
租户名称（TENANTNAME）|tenant_1
每个域的默认激活节点数（ACTIVENODES）|3
主用NF(局)标识（NFID1）|1
备用NF(局)标识（NFID2）|0
左域SC TYPE（LEFTSCTYPE）|1
右域SC TYPE（RIGHTSCTYPE）|2
单个CDN节点的内存库大小(M)（MDBSIZE）|7680
单个CDN节点使用的日志缓冲区大小(M)（LOGBUFF）|1024
单个CDN节点预删除数据的存储空间(M)（PREDELSIZE）|200
单个CDN节点消息缓冲区大小(M)（MQBUFSIZE）|20
配置步骤 : 
步骤|说明|操作
---|---|---
1|增加租户的配置。|ADD CDBTENANT:TENANTID=1,TENANTNAME="tenant_1",ACTIVENODES=3,NFID1=1,NFID2=0,LEFTSCTYPE=1,RIGHTSCTYPE=2
2|增加CDN节点参数配置。|ADD CDBPARAM:TENANTID=1,MDBSIZE=7680,LOGBUFSIZE=1024,PREDELSIZE=200,MQBUFSIZE=20
#### 配置实例2 
配置场景 : 
多业务NF共享CUDR场景，此场景下需要配置多个租户的相关参数，在实例化的时候会自动配置多个租户信息。
数据规划 : 
多业务NF共享CUDR场景数据规划 
参数|取值
---|---
第一个租户的租户ID（TENANTID）|1
第一个租户的租户名称（TENANTNAME）|tenant_1
第一个租户的每个域的默认激活节点数（ACTIVENODES）|3
第一个租户的主用NF(局)标识（NFID1）|1
第一个租户的备用NF(局)标识（NFID2）|0
第一个租户的左域SC TYPE（LEFTSCTYPE）|1
第一个租户的右域SC TYPE（RIGHTSCTYPE）|2
第一个租户的单个CDN节点的内存库大小(M)（MDBSIZE）|7680
第一个租户的单个CDN节点使用的日志缓冲区大小(M)（LOGBUFF）|1024
第一个租户的单个CDN节点预删除数据的存储空间(M)（PREDELSIZE）|200
第一个租户的单个CDN节点消息缓冲区大小(M)（MQBUFSIZE）|20
第二个租户的租户ID（TENANTID）|2
第二个租户的租户名称（TENANTNAME）|tenant_2
第二个租户的每个域的默认激活节点数（ACTIVENODES）|3
第二个租户的主用NF(局)标识（NFID1）|2
第二个租户的备用NF(局)标识（NFID2）|0
第二个租户的左域SC TYPE（LEFTSCTYPE）|3
第二个租户的右域SC TYPE（RIGHTSCTYPE）|4
第二个租户的单个CDN节点的内存库大小(M)（MDBSIZE）|7680
第二个租户的单个CDN节点使用的日志缓冲区大小(M)（LOGBUFF）|1024
第二个租户的单个CDN节点预删除数据的存储空间(M)（PREDELSIZE）|200
第二个租户的单个CDN节点消息缓冲区大小(M)（MQBUFSIZE）|20
配置步骤 : 
多业务NF共享CUDR场景配置步骤 
步骤|说明|操作
---|---|---
1|增加第一个租户的配置。|ADD CDBTENANT:TENANTID=1,TENANTNAME="tenant_1",ACTIVENODES=3,NFID1=1,NFID2=0,LEFTSCTYPE=1,RIGHTSCTYPE=2
2|增加第一个租户的CDN节点参数配置。|ADD CDBPARAM:TENANTID=1,MDBSIZE=7680,LOGBUFSIZE=1024,PREDELSIZE=200,MQBUFSIZE=20
3|增加第二个租户的配置。|ADD CDBTENANT:TENANTID=2,TENANTNAME="tenant_2",ACTIVENODES=3,NFID1=2,NFID2=0,LEFTSCTYPE=3,RIGHTSCTYPE=4
4|增加第二个租户的CDN节点参数配置。|ADD CDBPARAM:TENANTID=2, MDBSIZE=7680, LOGBUFSIZE=1024, PREDELSIZE=200, MQBUFSIZE=20
调整特性 : 
本特性不需要调整。 
测试用例 : 
测试项目|业务NF专有UDSF场景测试
---|---
测试目的|测试业务NF在专有UDSF场景下业务运行正常
预置条件|按照业务NF专有UDSF场景进行部署UDSF和业务NF系统运行正常
测试过程|业务NF发起业务观察业务运行情况
通过准则|业务NF正常发起业务观察业务运行正常
测试结果|-
测试项目|业务NF共享UDSF场景测试
---|---
测试目的|测试业务NF在共享UDSF场景下业务运行正常
预置条件|按照业务NF共享UDSF场景进行部署UDSF和各业务NF系统运行正常
测试过程|各个业务NF发起业务观察所有业务NF的业务运行情况
通过准则|各个业务NF正常发起业务观察所有业务NF的业务运行正常
测试结果|-
常见问题处理 : 
无。 
## ZUF-76-01-002 软件无状态架构 
特性描述 : 
特性描述 : 
术语 : 
术语|含义
---|---
无状态|是指业务组件中不再保存持久化状态，用户可以通过任一业务组件来进行业务处理，从而实现业务组件间负荷分担。
描述 : 
定义 : 
3GPP TS 23.501标准规范中，提出了计算和存储分离的概念，对NF的状态数据进行统一存储，实现业务逻辑与状态数据分离，如[图1]所示，将状态数据存储在UDSF中。
图1  业务逻辑与状态数据
支持无状态架构的NF需要满足如下特性： 
计算与存储分离。 
同类型的VNFC以集群的工作方式负荷分担，系统的容量可随VNFC实例数增加而线性增长。 
缩扩容（Scale）和容灾恢复（Resilience）等导致VNFC实例变化后，秒级达到负荷均衡。 
背景知识 : 
面对万物互联5G时代多样化、极致通讯的需求，运营商需要构建更敏捷、更灵活的网络。NFV/SDN等虚拟化技术已经广泛应用到云化核心网中，实现了软硬件分离以及网络控制和转发的分离，降低TCO，但还存在如下挑战：
网络弹性不足：核心网各NF各自维护会话上下文数据，网元弹性、缩扩容需消耗较长时间进行迁移和恢复数据，难以实现快速的业务弹性、无损用户体验和加速新业务发布。 
容灾复杂：NF故障后，需要进行数据迁移。 
通过NF支持无状态架构，5GC实现了计算与存储的分离，解决了网络弹性不足问题及简化了容灾恢复，具有如下优势： 
快速、业务无损的网络弹性：控制类NF组件间无需迁移状态数据，实现秒级弹性。弹性过程中，状态数据不丢失，保证了业务的连续性。 
简洁的容灾恢复：通过共享UDSF，一个NF故障后，另一个NF可以从UDSF恢复用户数据。 
提高系统稳定性：业务逻辑无状态，业务组件支持N+M负荷分担，一个组件故障，其他组件可实时接管。基于分布式存储会话上下文数据库，支持本地容灾和地理容灾，提高了可靠性。 
应用场景 : 
NF无状态架构应用于NFV环境下的VNF。在NFV环境下，部署无状态架构的NF，可以方便地实现快速、业务无损的网络弹性，以及简洁的容灾恢复。
客户收益 : 
受益方|受益描述
---|---
运营商|业务创新：数据与存储分离，数据统一存储，利于数据分析和业务创新。节省投资：统一数据管理，简化运维，资源共享，降低OPEX和CAPEX。提高用户业务体验：实现快速、业务无损的网络弹性，提高系统稳定性。
终端用户|此特性对终端用户不可见。
实现原理 : 
系统架构 : 
本特性涉及的计算与存储架构图如[图2]所示。
图2  计算与存储分离架构图
在5GC网络中，业务NF专注于无状态的业务逻辑处理，将数据统一存储在UDSF上，由UDSF进行统一管理。
涉及的NF参见[表1]。
NF|说明
---|---
业务NF|包括AMF、SMF、PCF等5G业务NF，实现无状态业务逻辑处理以及快速网络弹性。
UDSF|统一存储和管理业务网元所需数据，实现计算与存储分离，业务和数据解耦。
AMF采用无状态的设计思路实现，软件架构如[图3]所示。业务处理逻辑实现了计算与存储分离，每个Stateless
NFC为了实现高效的业务逻辑处理，会在Local Cache中缓存部分用户数据。系统的LoadBalancer负载均衡器按无状态的方式进行话务均衡分发，保障业务逻辑在执行弹性伸缩、
自愈及重生时，系统负荷分布可以敏捷均衡。
图3  软件架构图
Stateless NF各组件及功能参见[表2]。
组件|说明
---|---
业务逻辑|业务流程处理组件。
Local Cache|本地数据库，用于缓存部分用户数据，减少和UDSF交互次数，提高系统性能。
Stateless Load Balancer|无状态负荷均衡组件，用于把收到的信令报文分发到Stateless NFC分发。
协议栈 : 
N18/Nudsf是业务NF和UDSF之间的接口。NF通过N18/Nudsf接口实现NF自身非结构化数据的存储与检索。该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
N18/Nudsf|ZUF-79-19-011 N18
NF实现 : 
AMF采用流程级NF无状态架构，实现无状态业务逻辑处理以及快速网络弹性。 
业务流程 : 
事务无状态处理流程
事务（Transaction）无状态：计算类NF，整个业务流程仅收到一次请求消息。NF收到请求消息后，回响应或向其他NF发送请求和接收响应后，业务流程就会结束，不包含再次接收请求消息。实现事务级无状态的NF，在一次事务中，会向UDSF读取和写入用户数据。不同事务，可以在不同的Stateless
NFC实例上处理。
事务无状态处理的业务流程图如[图4]所示。
图4  事务无状态处理
流程说明如下： 
Other NF给Stateless NF发送Transaction Request消息。 
Stateless NF的Stateless LB选择一个Stateless NFC实例，向其转发Transaction
Request消息。 
Stateless NFC的Service Logic组件向Local Cache获取用户数据。Stateless NFC的Local
Cache如果发现本地有用户数据，直接向Service Logic返回用户数据。Local Cache如果发现本地没有用户数据，则向UDSF获取用户数据后向Service
Logic返回用户数据。 
Stateless NFC的Service Logic组件继续业务处理，可以向其他NF发请求，可以访问Local Cache中数据，直到业务处理结束。 
Stateless NFC的Service Logic发送Transaction Response消息给Stateless
LB。 
Stateless LB发送Transaction Response消息给Other NF。 
Stateless NFC的Service Logic通过Cache把用户数据写入UDSF。 
Stateless NFC可以删除Local Cache中的用户数据，也可以保留Local Cache中的用户数据。 
流程无状态处理流程
流程（Procedure）无状态：计算类NF，业务流程比较复杂，整个业务流程有多个Transaction组成，收到多次请求消息，业务流程才结束。实现流程级无状态的NF，同一业务流程中的多个Transaction，是在同一个Stateless
NFC中处理的，且在业务流程中，仅会在业务流程的第一个Transaction中，向UDSF读取用户数据，在业务流程的最后一个Transaction中，向UDSF写入用户数据，业务流程的中间事务，不需向UDSF交互。 
流程无状态处理的业务流程图如[图5]所示。
图5  流程无状态处理
流程说明如下： 
Other NF给Stateless NF发送Transaction Request(1)消息。 
Stateless NF的Stateless LB选择一个Stateless NFC实例，向其转发Transaction
Request(1)消息。 
Stateless NFC的Service Logic组件向Local Cache获取用户数据。Stateless NFC的Local
Cache如果发现本地有用户数据，直接向Service Logic返回用户数据。Local Cache如果发现本地没有用户数据，则向UDSF获取用户数据后向Service
Logic返回用户数据。 
Stateless NFC的Service Logic组件继续业务处理，可以给其他NF发请求，可以访问Local Cache中数据，直到业务处理结束。 
Stateless NFC的Service Logic发送Transaction Response(1)消息给Stateless
LB。 
Stateless LB发送Transaction Response(1)消息给Other NF。 
Other NF给Stateless NF发送Transaction Request(N)消息。 
Stateless NF的Stateless LB选择处理Transaction Request(1)的Stateless
NFC实例，向其转发Transaction Request(N)消息。 
Stateless NFC的Service Logic组件继续业务处理，可以向其他NF发请求，可以访问Local Cache中数据，直到业务处理结束。 
Stateless NFC的Service Logic发送Transaction Response(N)消息给Stateless
LB。 
Stateless LB发送Transaction Response(N)消息给Other NF。 
Other NF给Stateless NF发送Transaction Request(Last)消息。 
Stateless NF的Stateless LB选择处理Transaction Request(1)的Stateless
NFC实例，向其转发Transaction Request(Last)消息。 
Stateless NFC的Service Logic组件继续业务处理，可以向其他NF发请求，可以访问Local Cache中数据，直到业务处理结束。 
Stateless NFC的Service Logic发送Transaction Response(Last)消息给Stateless
LB。 
Stateless LB发送Transaction Response(Last)消息给Other NF。 
Stateless NFC的Service Logic通过Cache把用户数据写入UDSF。 
Stateless NFC可以删除Local Cache中的用户数据，也可以保留Local Cache中的用户数据。 
会话无状态处理流程
会话（Session）无状态：计算类NF，业务流程比较复杂，短时间需使用大量用户数据。业务流程起始于UE会话建立，结束于UE会话释放。在会话存续期间，可能会有多个业务流程。实现会话无状态的NF，同一会话的多个业务流程，是在同一个Stateless
NFC种处理的，且在会话存续期间，仅会在会话的第一个流程的第一个Transaction中，向UDSF读取用户数据，在会话结束的最后一个Transaction中，向UDSF写入用户数据，会话存续期间的中间业务流程，在业务流程结束才需向UDSF写入用户数据。
会话无状态处理的业务流程图如[图6]所示。
图6  会话无状态处理
流程说明如下： 
Other NF发起业务流程，建立会话，具体处理参见[流程无状态处理流程]，但Stateless NF中的Stateless NFC会把会话数据保存在Local
Cache中，不删除。
该会话的其他业务流程中的Transaction Request，Stateless LB会把其转发给Local Cache中有会话数据的Stateless
NFC实例处理。 
Other NF发起业务流程，结束会话，Stateless NF中的Stateless NFC删除Local Cache中的会话数据。 
内部事件触发
内部事件触发的业务流程图如[图7]所示。
图7  内部事件触发
流程说明如下： 
Stateful NFC触发了内部事件，如隐式注销用户事件、产生定时话单事件。 
Stateful NFC向Stateless NFC发送Transaction Request消息。 
Stateless NFC的Service Logic向Stateful NFC返回Transaction Response消息。 
Stateless NFC的Service Logic的处理，与收到Other NF的Transaction Request处理一致，参见[事务无状态处理流程]。
系统影响 : 
AMF无状态设计架构，基于流程级无状态实现，无额外系统资源消耗。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
类别|标准编号|标准名称
---|---|---
3GPP|3GPP TS 23.501|System Architecture for the 5G System
3GPP|3GPP TS 23.502|Procedures for the 5G System
特性能力 : 
该特性不涉及规格指标。 
版本要求及变更记录 : 
序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 : 
License要求 : 
该特性为5G产品的基本特性，无需license支持。 
对其他网元的要求 : 
UE|gNB/ng-eNB
---|---
-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及。 
O&M相关 : 
配置命令 : 
本特性暂时不涉及配置命令的变化。 
定时器 : 
本特性暂时不涉及定时器的变化。 
性能统计 : 
本特性暂时不涉及计数器的变化。 
告警和通知 : 
本特性暂时不涉及告警和通知的变化。 
话单与计费 : 
本特性暂时不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
本特性无需特殊配置，完成初始配置后即可使用。 
测试用例 : 
测试项目|AMF支持无状态架构
---|---
测试目的|验证AMF支持无状态架构
预置条件|RAN、各NF运行正常。AMF有多个业务处理单元。
测试过程|用户发起注册流程，接入到AMF业务处理单元1。AMF业务处理单元1异常重启。用户发起业务请求流程。
通过准则|用户发起注册流程成功，AMF向UDSF写入用户数据。用户所在的AMF业务处理单元1重启后，用户发起业务请求，AMF向UDSF获取用户数据，由AMF其他正常业务处理单元处理业务请求，业务请求流程成功。
测试结果|-
# 缩略语 
# 缩略语 
5GC : 
5G Core Network5G核心网
AMF : 
Access and Mobility Management Function接入和移动管理功能
## API 
Application Program Interface应用程序接口
## CAPEX 
Capital Expenditure资本性支出
## CC 
Control Center控制中心
## CDN 
Context Data Node上下文数据节点
## CUDR 
Cloud Unified Data Repository云化统一数据仓库
## FCAPS 
Fault Configuration Accounting Performance and Security错误、配置、计帐、性能和安全（指网络管理的要素）
NF : 
Network Function网络功能
NFV : 
Network Functions Virtualization网络功能虚拟化
NFVO : 
Network Functions Virtualization Orchestrator网络功能虚拟化编排器
## OPEX 
Operating Expenditure运营性支出
PCF : 
Policy Control Function策略控制功能
## SDN 
Software Defined Network软件定义网络
SMF : 
Session Management Function会话管理功能
## TCO 
Total Cost of Ownership总体拥有成本
## TLV 
Tag, Length, Value标记、长度、取值
UDSF : 
Unstructured Data Storage Function非结构化数据存储功能
UE : 
User Equipment用户设备
VNF : 
Virtualized Network Function虚拟化网络功能
## VNFC 
Virtualized Network Function Component虚拟网络功能组件
VNFM : 
Virtualized Network Function Manager虚拟化网络功能管理器
# ZUF-76-02 NFV 
## ZUF-76-02-001 VNF自动部署 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
自动部署功能是指运维人员通过NFVO为VNF实例分配所需的NFVI资源的过程。
自动部署是ZXUN uMAC实现所有功能的基础。
背景知识 : 
虚拟化又称为云化，云是网络的一种比喻说法，是对电信网、互联网和底层基础设施的抽象描述。 
 说明： 
底层基础设施指的是主机、内存、CPU、接口、网络等硬件设施或网络资源。
云化就是指通过虚拟化技术NFV，将核心网网元的基础架构从专用硬件向通用硬件进行演进，从而实现软硬件的解耦。
对核心网进行云化后，其硬件设备和网元不再是一一对应的关系，由于底层的硬件设施和上层应用是解耦的，底层的硬件资源通过NFV可以被上层的多种应用共享。
NFV是云化核心网的关键技术。通过基于行业标准的x86服务器、存储和交换设备及虚拟化技术，使网络设备功能不再依赖于专用硬件，从而降低网络昂贵的设备成本，资源可以充分灵活共享，帮助运营商获得更多、更灵活的网络能力，实现新业务的快速开发和部署。
ETSI制定的NFV架构由NFVI、VNF以及MANO三个部分组成。
NFVI：基础硬件设施NFVI包括通用的硬件设施及其虚拟化。 
MANO：云管理及调度平台在NFV架构中，MANO负责对整个NFVI资源的管理和编排，负责业务网络和NFVI资源的映射和关联。MANO包括VIM、VNFM和NFVO三个部分，分别完成对NFVI、VNF和NS三个层次的管理。 
VNF：上层业务应用VNF使用软件实现虚拟化网络功能。 
应用场景 : 
主要应用于运营商已部署好的云管理系统的通用服务器设备上，进行ZXUN uMAC虚拟化交换局开局。
客户收益 : 
收益者|收益描述
---|---
运营商|可以根据运营商局点用户容量和流量进行定制开局，节省硬件资源。可以提供自动化的软件安装和功能加载，快速完成ZXUN uMAC部署。可以提供针对不同虚拟化云平台完成ZXUN uMAC自动部署。
移动终端用户|对终端用户不可见。
实现原理 : 
系统架构 : 
根据核心网云化的三层结构，NFV架构中各个节点的关系如[图1]所示。
图1  NFV三层架构
涉及的网元 : 
各节点的功能说明参见[表1]。
架构|节点|描述|对应的产品
---|---|---|---
NFVI（基础硬件设施）|服务器|NFVI是网络功能虚拟化基础设施，通常指的是物理资源，包括主机、内存、CPU、接口等硬件设施。|云平台的硬件通常采用高性能的服务器，如HP C7000，DELL R730等。中兴通讯自研的云平台服务器为ZXCLOUDE9000企业级刀片服务器。
磁阵|NFVI（基础硬件设施）|用于数据存储的设备，运营商可以根据实际运营状况决定是否需要配置磁阵，在交接局业务量较小的情况下，无需配置。|根据运营商的实际环境配置，对磁阵的型号没有限制，如Fujitsu DX100 S3、中兴R5300。
外部交接机|NFVI（基础硬件设施）|外部交换机指的是在实际组网环境中，用于将NFVI和磁阵接入运营商维护网络的交换机。|根据运营商的实际环境配置，对交换机的型号没有限制。
MANO（云管理及调度平台）|VIM|VIM是虚拟化基础设施管理系统，是NFVI的管理者。VIM主要负责基础设施层硬件资源、虚拟化资源的管理、监控和故障上报，面向上层业务应用提供虚拟化资源池。VIM为NFVO和VNFM提供VNF相关虚拟资源的操作接口。|VIM称为云平台管理软件，常见的VIM包括VmWare、OpenStack等。中兴通讯基于OpenStack开源标准接口研发的云平台管理软件的产品名称为TECS OpenStack。
VNFM和NFVO|MANO（云管理及调度平台）|NFVO负责全网的网络服务、虚拟资源以及物理资源的编排和管理功能。VNFM对核心网所有网元提供生命周期管理以及弹性伸缩相关的虚拟机操作管理功能。|由中兴通讯自研的用于实现VNFM和NFVO功能的产品名称为ZXUN Vmanager。
VNF（上层业务应用）|VNF|一个VNF对应于在传统非虚拟化网络中的一个物理网络功能，即对应核心网的各种网元，如：AMF、MME、PGW、SGW等。|中兴通讯用于实现PGW和SGW网元功能的产品名称为ZXUN xGW，用于实现AMF、MME和Gn/Gp SGSN网元功能的产品名称为ZXUNuMAC。
本网元实现 : 
VIM启动ZXUN uMAC的虚机，ZXUN uMAC从VNFM下载产品包，ZXUN uMAC开始安装自身软件，并配置相关的数据，最后向VNFM返回VNF实例化完成。
业务流程 : 
ZXUN uMAC自动部署依赖MANO完成，NFVO根据ZXUN uMAC提供的信息（包括：整局用户容量、流量、网络信息等），与VNFM交互协同，完成ZXUN uMAC自动部署。
流程图如[图2]所示。
图2  业务流程
用户发起实例化请求到NFVO，其中携带实例化需要的VNF信息。 
NFVO校验请求的合法性。 
NFVO向VNFM发起VNF实例化，携带VNFD信息、实例化信息、软件版本信息。 
VNFM收到VNF实例化请求，校验请求的合法性，计算ZXUN uMAC需要的虚机资源。
VNFM向NFVO申请创建和分配虚机资源。 
NFVO处理相关的资源分配工作。 
NFVO向VIM申请创建资源。 
VIM创建虚机，将虚机绑定到网络和存储。 
VIM返回NFVO创建结果。 
NFVO返回VNFM申请到的创建资源结果。 
VNFM启动创建的资源。 
VIM启动虚机。 
ZXUN uMAC从VNFM下载ZXUN uMAC产品包。
ZXUN uMAC虚机开始安装自身软件，并配置相关的数据。
ZXUN uMAC向VNFM返回VNF实例化完成。
VNFM向NFVO返回VNF实例化完成。 
NFVO向用户反馈ZXUN uMAC实例化完成。
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
自动部署特性必须运行在支持ETSI NFV规范的虚拟化软硬件平台上。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称
---
ETSI GS NFV 001 V1.1.1(2013-10)
ETSI GS NFV 002 V1.1.1(2013-10)
ETSI GS NFV 003 V1.1.1(2013-10)
ETSI GS NFV 004 V1.1.1(2013-10)
ETSI GS NFV-PER 001 V1.1.1(2014-06)
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
NFVO|VNFM|VIM
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 : 
命令 : 
配置项该特性不涉及配置项的变化。 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警和通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
自动部署VNF是通过CloudStudio进行操作的。 
自动部署VNF也称为VNF的实例化过程，在实例化过程中，系统完成VNF所需虚拟资源的创建和业务程序的自动部署。
在实例化的过程中，通过以下过程实现各VM之间的通信。 
为每个VM分配虚拟网口，并对虚拟网口进行标识。 
通过VLAN技术建立虚拟网桥。 
建立虚拟网口与虚拟网桥的通信连接。 
部署网络，使VM所处的逻辑层与物理层互通。 
配置前提 : 
已获取VNF自定义文件。
配置过程 : 
自动部署过程参见VNF的部署
。
## ZUF-76-02-002 VNF弹性伸缩 
特性描述 : 
特性描述 : 
术语 : 
术语|含义
---|---
Scale in|Scale in，弹性缩容。让部分虚机退出服务，退出对硬件资源的占用。即在单个虚机资源固定的情况下，通过减少虚机数来实现负载的均衡。
Scale out|Scale out，弹性扩容。为部分虚机申请硬件资源，让该虚机进入服务。即在单个虚机资源固定的情况下，通过增加虚机数来实现负载的均衡。
描述 : 
定义 : 
手工弹性是指人工从VNFM触发SC（服务组件，Service Component）占用的虚拟资源弹出或者缩减流程。 
自动弹性是指根据SC（服务组件，Service Component）的资源利用情况自动弹出或者缩减资源。NF实时监控服务组件的资源利用情况，当服务组件的资源利用率达到设置的弹出门限时，增加新的资源并迁移业务到新服务组件；当服务组件的资源利用率达到设置的缩进门限时，先将待释放的服务组件的业务迁移到其他服务组件，再释放服务组件。 
背景知识 : 
虚机弹扩（scale out），即申请服务组件所占用的资源，包括vCPU、内存、磁盘和网口。 
虚机弹缩（scale in），即释放服务组件所占用的资源，包括vCPU、内存、磁盘和网口。 
scale out：NF支持scale out功能，以实现负载均衡和提升处理能力。即在合同容量范围内，NF支持不影响业务连续性的自动或者手工扩容虚拟机，即根据弹性伸缩策略（包括CPU负荷、数据区占用和时间周期等），自动或者手工启动新的虚拟机。scale
out如图1所示。图1  scale out在scale out之前，系统只有3#虚拟机在工作，且CPU负荷占用达到90%。在scale out后，系统有3#和4#虚拟机在工作，且4#虚拟机分担系统的一半的负荷。 
scale inNF支持scale in功能，以实现节能降耗的要求。即在合同容量范围内，NF支持不影响业务连续性的自动或者手工缩容虚拟机，即根据弹性伸缩策略，自动或者手工关闭正在运行的虚拟机。scale
in如图2所示。图2  scale in在scale in之前，系统有3#和4#虚拟机在工作，且两个虚机的CPU负荷占用都为20%。在scale in后，系统只有3#虚拟机在工作，且3#虚拟机的负荷变为40%。 说明：所有资源均是折算为百分比，弹缩算法和CPU一致。如上下文，不是根据用户数量，而按容量比例来进行弹缩。实际使用时，需要查询具体的容量值。 
应用场景 : 
运营商希望系统运行时，能智能分配资源。在保证用户体验的情况下，通过手工弹性在遇到节假日或者大型活动时，预先手工扩大资源以应对突发的业务量。在话务低潮时，手工缩减资源。通过自动弹性，在话务高峰期时自动增加资源，在话务低潮期自动收回多余资源。 
客户收益 : 
受益方|受益描述
---|---
运营商|系统运行时，在保证用户体验的情况下，提高系统资源利用率。话务高峰前手工触发增加资源，话务低潮后手工触发回收资源。系统运行时，智能调配资源。在保证用户体验的情况下，话务高峰期，资源不足时自动增加资源；话务低潮时回收多余的资源。达到充分利用系统资源，降低运维成本的目的。
终端用户|此特性对终端用户不可见。
实现原理 : 
系统架构 : 
本特性涉及的系统架构如[图3]所示。
图3  系统架构图
上图描述了系统虚拟化组成部分，弹缩由这些组件一起实现。 
涉及的NF/网元参见下表。 
网元名称|说明
---|---
NFVO|提供网元自动部署界面，负责VNF资源编排。NFVO根据人工制作的VNF描述文件（后续简称为info文件），为VNF实例分配需要的基础设施资源，并监控虚拟机启动过程。
VNFM|负责计算VNF需要的虚机资源提供给NFVO编排，提供VNF版本包下载服务给VNF。由中兴通讯自研的用于实现VNFM和NFVO功能的产品名称为CloudStudio。
VIM|负责基础设施层虚拟资源管理，VIM为NFVO和VNFM提供VNF相关虚拟资源的操作接口。中兴通讯基于OpenStack开源标准接口研发的云平台管理软件的产品名称为ZTETECS OpenStack。
NFV|从VNFM下载自身的软件版本，并完成自身的安装和配置。
业务流程 : 
####### 手工弹扩流程 
手工弹扩业务流程如[图4]所示。
图4  手工弹扩业务流程
流程说明如下： 
用户在VNFM选择需要弹出的SC（服务组件，Service Component），触发SC弹出。
VNFM向VNF发送SC副本数量增加变化请求。
VNF找到SC归属的VM，判断VM可以弹出。
VNF向VNFM发送VM创建请求。 
VNFM向VIM发送VM创建请求。 
VM创建成功后，VIM向VNFM发送成功建立消息。
VNFM向VNF回VM创建响应消息。 
VNF收到VM上电成功消息，进行SC负荷重平衡操作，新弹出的SC投入服务。 
####### 手工弹缩流程 
手工弹缩业务流程如[图5]所示。
图5  手工弹缩业务流程
流程说明如下。 
用户在VNFM选择需要缩减的SC，触发SC缩容。 
VNFM向VNF发送SC副本数量减少变化请求。 
VNF找到SC归属的VM，选择可以删掉的VM。 
VNF把待删除的VM上的业务迁移到其他VM。 
VNFM向VNF查询SC复本数量变化，更新SC复本数量。 
VNF向VNFM发送VM删除请求。 
VNFM向VIM发送VM删除请求。 
VM删除后VIM向VNFM发送删除成功。 
VNFM向VNF发送删除成功。 
####### 自动弹扩流程 
自动弹扩业务流程如[图6]所示。
图6  自动弹扩业务流程
流程说明如下。 
在VNFM配置SC（服务组件，Service Component）自动弹缩门限。
VNF配置使能SC自动弹缩。
VNF监控SC的KPI指标，如果SC的KPI指标超过门限，SC所在的VM可以弹出。
VNF向VNFM发送VM创建请求。 
VNFM向VIM发送VM创建请求。 
VIM虚机创建完成后，向VNFM发送虚机创建响应消息。 
VNFM向VNF发送虚机创建响应消息。 
VNF收到VM上电成功消息。 
VNF执行SC负荷重平衡。 
VNF通知VNFM SC复本数量增加，VNFM更新SC复本。 
####### 自动弹缩流程 
自动弹缩业务流程如[图7]所示。
图7  自动弹缩业务流程
在VNFM配置SC自动弹缩门限。 
VNF配置使能SC自动弹缩。 
VNF监控SC的KPI指标，如果SC的KPI指标低于门限，SC所在的VM可以缩减。 
VNF选择待删除的VM。 
VNF把待删除的VM的业务迁移到其他VM。 
VNF通知VNFM SC复本数量减少。 
VNF向VNFM发送VM删除请求。 
VNFM向VIM发送VM删除请求。 
VM删除后，VIM向VNFM发送VM删除响应消息。 
VNFM向VNF发送VM删除响应消息。 
NF实现 : 
手工弹缩是在VNFM上对相应的VM进行手工操作弹性，VNFM下发相应的消息给NF，NF经过内部处理给VNFM返回允许或者拒绝操作。 
自动弹缩是SC自动弹缩激活后，如果NF检测某个虚机的CPU或者RAM达到设定的阈值，则发起自动弹性流程，上报VNFM，再由VNFM与云平台交互删除或者创建相应的VM。 
协议栈 : 
该特性不涉及具体业务接口和协议栈。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
弹出需要提前预留硬件资源，并且服务组件没有超过系统设定的容量上限。 
特性交互 : 
自动弹缩与手工弹缩互斥。 
遵循标准 : 
类别|标准编号|标准名称
---|---|---
ETSI|ETSI GS NFV 001 V1.1.1(2013-10)|Network Functions Virtualization (NFV); Use Cases V1.1.1
ETSI|ETSI GS NFV 002 V1.1.1(2013-10)|Network Functions Virtualization (NFV); Architectural FrameworkV1.1.1
ETSI|ETSI GS NFV 003 V1.1.1(2013-10)|Network Functions Virtualization (NFV); Terminology for MainConcepts in NFV V1.1.1
ETSI|ETSI GS NFV 004 V1.1.1(2013-10)|Network Functions Virtualization (NFV); Virtualization RequirementsV1.1.1
ETSI|ETSI GS NFV-PER 001 V1.1.1(2014-06)|Network Functions Virtualization (NFV); Performance & PortabilityBest Practises V1.1.1
特性能力 : 
该特性不涉及规格指标。 
版本要求及变更记录 : 
序号|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
可获得性 : 
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
NFVO|NFVM|VIM
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
扩容过程中会创建新的虚机，需要占用额外的云平台资源，特别是如果某种类型的虚机开通了互斥功能的情况下，会占用更多的云平台资源，必须保证云平台的物理硬件资源足够，否则会导致扩容失败。 
O&M相关 : 
配置命令 : 
配置项|命令
---|---
弹性全局配置|SET SCALEGLBBASECFG
SHOW SCALEGLBBASECFG|弹性全局配置
弹性全局策略配置|SET SCALEPOLICYGLB
SHOW SCALEPOLICYGLB|弹性全局策略配置
定时器 : 
本特性不涉及定时器的变化。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
手动缩扩容和自动缩扩容功能需要在创建NF蓝图时设置VM的初始值和最大值，最大值即是扩容的最大限额。 
配置前提 : 
NF已经通过CloudStudio操作实例化成功。 
NF已经接入EM。 
配置过程 : 
 说明： 
各NF的配置操作基本相同，下文以AMF的操作为例。 
手动弹性操作： 
执行[SET SCALEGLBBASECFG]命令，配置此NF支持弹性，并且弹性模式是手动。
自动弹性操作： 
执行[SET SCALEGLBBASECFG]命令，配置此NF支持弹性，并且弹性模式是自动。
执行[SET SCALEPOLICYGLB]命令，配置NF自动弹性的触发参数。
配置实例 : 
###### 手工扩容 
配置场景
用户对AMF的GSU发起手工扩容。 
数据规划
根据假设的场景，AMF数据规划参见。 
参数|取值
---|---
AMF GSU虚拟机初始个数|3
AMF GSU虚拟机最大个数|8
AMF的弹性模式|手动manual
配置步骤
步骤|说明|操作
---|---|---
１|配置支持手动弹性。|SET SCALEGLBBASECFG:SCALESWITCH=ENABLE,MODE=MANUAL
###### 自动弹缩 
配置场景
配置AMF支持GSU自动扩容，并在CPU占用率达到门限时，自动进行VM弹缩。 
数据规划
根据假设的场景，AMF数据规划参见。 
参数|取值
---|---
AMF GSU虚拟机初始个数|3
AMF GSU虚拟机最大个数|8
AMF 的弹性模式|自动automatic
自动弹性类型|CPU占用率
扩容门限（%）|10
缩容门限（%）|5
步骤
步骤|说明|操作
---|---|---
1|配置支持自动弹性。|SET SCALEGLBBASECFG:SCALESWITCH=ENABLE,MODE=AUTOMATIC
2|配置自动弹性的策略。|SET SCALEPOLICYGLB:POLICYTYPE=CPU_RATIO,SCALEOUTTHD=10,SCALEINTHD=5
测试用例 : 
测试项目|AMF手动弹性
---|---
测试目的|验证AMF的GSU虚拟机的手动弹性功能。|验证AMF的GSU虚拟机的手动弹性功能。|验证AMF的GSU虚拟机的手动弹性功能。
预置条件|创建AMF蓝图时，设置GSU的初始值是3，最大值是8。部署AMF成功。已使用SET SCALEGLBBASECFG命令配置AMF支持手动弹性。|创建AMF蓝图时，设置GSU的初始值是3，最大值是8。部署AMF成功。已使用SET SCALEGLBBASECFG命令配置AMF支持手动弹性。|创建AMF蓝图时，设置GSU的初始值是3，最大值是8。部署AMF成功。已使用SET SCALEGLBBASECFG命令配置AMF支持手动弹性。
测试步骤|在CloudStudio上选择应用→VNF，在打开的页面中单击要操作的AMF右侧的弹性按钮，选择弹性伸展并且在VM的表格内填写要操作的VM个数，单击提交按钮执行操作。扩容完成后，单击要操作的AMF右侧的弹性按钮，选择弹性收缩并且在VM的表格内填写要操作的VM个数，单击提交按钮执行操作。|在CloudStudio上选择应用→VNF，在打开的页面中单击要操作的AMF右侧的弹性按钮，选择弹性伸展并且在VM的表格内填写要操作的VM个数，单击提交按钮执行操作。扩容完成后，单击要操作的AMF右侧的弹性按钮，选择弹性收缩并且在VM的表格内填写要操作的VM个数，单击提交按钮执行操作。|在CloudStudio上选择应用→VNF，在打开的页面中单击要操作的AMF右侧的弹性按钮，选择弹性伸展并且在VM的表格内填写要操作的VM个数，单击提交按钮执行操作。扩容完成后，单击要操作的AMF右侧的弹性按钮，选择弹性收缩并且在VM的表格内填写要操作的VM个数，单击提交按钮执行操作。
预期结果|手动扩容成功，GSU VM被成功扩出，在CloudStudio上能看到任务执行成功。手动缩容成功，GSU VM被成功缩回，在CloudStudio上能看到任务执行成功。|手动扩容成功，GSU VM被成功扩出，在CloudStudio上能看到任务执行成功。手动缩容成功，GSU VM被成功缩回，在CloudStudio上能看到任务执行成功。|手动扩容成功，GSU VM被成功扩出，在CloudStudio上能看到任务执行成功。手动缩容成功，GSU VM被成功缩回，在CloudStudio上能看到任务执行成功。
消息流程|无|无|无
测试结果|□ 通过       □ 不通过|□ 通过       □ 不通过|□ 通过       □ 不通过
备注|||
签字||测试日期|
测试项目|AMF的自动弹性
---|---
测试目的|验证AMF的自动弹性功能。|验证AMF的自动弹性功能。|验证AMF的自动弹性功能。
预置条件|AMF已经实例化完成，设置GSU初始值3，最大值8。AMF已经接入EM。UE registration流程已经正常。已使用SET SCALEGLBBASECFG命令配置AMF支持自动弹性。|AMF已经实例化完成，设置GSU初始值3，最大值8。AMF已经接入EM。UE registration流程已经正常。已使用SET SCALEGLBBASECFG命令配置AMF支持自动弹性。|AMF已经实例化完成，设置GSU初始值3，最大值8。AMF已经接入EM。UE registration流程已经正常。已使用SET SCALEGLBBASECFG命令配置AMF支持自动弹性。
测试步骤|通过模拟工具让批量用户发起注册流程，提高并发量。30分钟后，停止模拟工具批量用户的注册流程。|通过模拟工具让批量用户发起注册流程，提高并发量。30分钟后，停止模拟工具批量用户的注册流程。|通过模拟工具让批量用户发起注册流程，提高并发量。30分钟后，停止模拟工具批量用户的注册流程。
预期结果|通过提高并发量，使GSU的CPU占用率达到10%后，AMF的GSU VM扩容，从云平台上可以看到增加GSU VM。停止模拟工具的注册流程后，GSU的CPU占用率降低到5%后，一个GSU VM被缩容，在云平台上可以看到GSU VM减少。|通过提高并发量，使GSU的CPU占用率达到10%后，AMF的GSU VM扩容，从云平台上可以看到增加GSU VM。停止模拟工具的注册流程后，GSU的CPU占用率降低到5%后，一个GSU VM被缩容，在云平台上可以看到GSU VM减少。|通过提高并发量，使GSU的CPU占用率达到10%后，AMF的GSU VM扩容，从云平台上可以看到增加GSU VM。停止模拟工具的注册流程后，GSU的CPU占用率降低到5%后，一个GSU VM被缩容，在云平台上可以看到GSU VM减少。
消息流程|无|无|无
测试结果|□ 通过       □ 不通过|□ 通过       □ 不通过|□ 通过       □ 不通过
备注|||
签字||测试日期|
## ZUF-76-02-003 虚机自愈 
特性描述 : 
特性描述 : 
术语 : 
本特性不涉及相关术语。 
描述 : 
定义 : 
uMAC运行过程中，由于硬件、云平台、人为等原因，导致部分虚机有可能处于异常状态(包括被挂起、休眠、错误）。针对这种状态异常的虚机，uMAC提供了及时恢复吊死虚机的能力，称为虚机自愈。 
背景知识 : 
虚机自愈是uMAC本身的一种异常保护机制，当检测到云平台上虚机的状态和本地的状态不一致时，会先触发虚机状态不一致告警，之后触发虚机自愈的过程。 
虚机自愈的过程中会产生告警通知，虚机自愈起来后，告警通知会随之恢复。 
uMAC的虚机自愈功能开关默认是关闭的，管理人员可以自行开启。 
应用场景 : 
uMAC运行过程中，出现部分虚机状态异常。运营商希望系统自动恢复异常的虚机，满足高可靠性要求。 
客户收益 : 
受益方|受益描述
---|---
运营商|及时检测状态异常的虚机资源，并自动将其恢复，由此维护系统的高可用性和健壮性。
终端用户|此特性对终端用户不可见。
实现原理 : 
系统架构 : 
ZXUN uMAC虚机自愈特性是基于ETSI
NFV架构，如[图1]所示。
图1  ETSI NFV架构图
涉及的网元 : 
网元名称|网元作用
---|---
VNFM|提供接口给ZXUN uMAC虚机状态查询，以及完成后续的虚机自愈操作。
VIM|负责基础设施层虚拟资源管理，提供创建、删除、状态查询等虚机及相关资源的接口。
ZXUN uMAC|对应图中的VNF，负责定时发消息给VNFM查询云平台上的虚机状态，并结合本地状态来决定是否触发告警和虚机自愈。
本网元实现 : 
ZXUN uMAC运行过程中，OMU虚机会定时检测备用OMU和GSU、CDU、IPU各虚机状态，一旦认为被检测的虚机状态不正确，则会触发虚机自愈。在自愈过程中，故障虚机会下电后重启，恢复到正常工作状态。
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
本特性必须运行在支持ETSI NFV规范的虚拟化软硬件平台上。 
特性交互 : 
本特性必须在自动部署完成后进行。 
遵循标准 : 
标准名称|章节
---|---
ETSI GS NFV|ETSI GS NFV 001 V1.1.1(2013-10)
ETSI GS NFV 002 V1.1.1(2013-10)|ETSI GS NFV
ETSI GS NFV 003 V1.1.1(2013-10)|ETSI GS NFV
ETSI GS NFV 004 V1.1.1(2013-10)|ETSI GS NFV
ETSI GS NFV-PER 001 V1.1.1(2014-06)|ETSI GS NFV
特性能力 : 
恢复状态异常的虚机，以维护系统正常运行。 
状态检测在ZXUN uMAC的主控虚机（OMU）上进行，其他任何类型的虚机（包括备用OMU）都可以被检测并执行自愈。
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
NFVO|VNFM|VIM
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
无 
O&M相关 : 
命令 : 
配置项表1  新增配置项配置项命令修改自愈全局配置SET AUTOHEALINGGLB查询自愈全局配置SHOW AUTOHEALINGGLB修改自愈级别配置SET AUTOHEALINGLV查询自愈级别配置SHOW AUTOHEALINGLV新增指定VM类型的自愈配置ADD VMAUTOHEALING修改指定VM类型的自愈配置SET VMAUTOHEALING删除指定VM类型的自愈配置DEL VMAUTOHEALING查询指定VM类型的自愈配置SHOW VMAUTOHEALING新增指定VM类型的自愈级别配置ADD VMAUTOHEALINGLV修改指定VM类型的自愈级别配置SET VMAUTOHEALINGLV删除指定VM类型的自愈级别配置DEL VMAUTOHEALINGLV查询指定VM类型的自愈级别配置SHOW VMAUTOHEALINGLV 
软件参数该特性不涉及软件参数的变化。 
告警和通知 : 
告警和通知
---
3490709513 虚机状态不一致
3490709514 模块状态不一致
3490709515 模块自愈
3490709534 虚机迁移
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
自愈功能可通过EM系统配置不同的自愈策略，例如可以分别配置容器重建、虚机重启、虚机重建策略来达到容器的自愈，还可以按照不同的虚机类型来配置对应的自愈策略。 
配置前提 : 
实例化已经完成，系统已经接入EM系统。 
配置过程 : 
使用[SET AUTOHEALINGGLB]命令，修改自愈全局配置。
使用[SET AUTOHEALINGLV]命令，修改自愈级别配置。
（可选）使用[ADD VMAUTOHEALING]命令，指定VM类型的自愈配置。
（可选）使用[ADD VMAUTOHEALINGLV]命令，指定VM类型的自愈级别配置。
配置实例 : 
场景说明 : 
启用自愈全局配置，并设置自愈相关信息。 
数据规划 : 
参数|示例
---|---
自愈功能总开关|启用
自愈级别|虚机重组
自愈超时|600 s
重试次数|2
虚机类型|IPU
指定VM类型的自愈功能开关|开启
自愈等待时间|30 s
自愈失败策略|无操作
自愈级别|虚机重组
自愈超时|600 s
重试次数|2
配置步骤 : 
步骤|说明|命令
---|---|---
1|设置启用自愈。|SET AUTOHEALINGGLB:HEALINGSWITCH="ENABLE"
2|将VMREBUILD级别的重试次数修改为2。|SET AUTOHEALINGLV:LEVEL="VMREBUILD",HEALINGSWITCH="ENABLE",TIMEOUT=600,RETRYCOUNT=2
3|启用IPU的自愈，自愈等待时间为30 s、自愈失败策略为无操作。|ADD VMAUTOHEALING:VMTYPE="IPU",HEALINGSWITCH="ENABLE",WAITTIME=30,FAILPOLICY="NOACTION"
4|启用IPU虚机重组级别的自愈，自愈超时时长为600 s、重试次数为2。|ADD VMAUTOHEALINGLV:VMTYPE="IPU",LEVEL="VMREBUILD",HEALINGSWITCH="ENABLE",TIMEOUT=600,RETRYCOUNT=2
调整特性 : 
本特性暂不涉及调整参数。 
测试用例 : 
###### 容器自愈 
测试项目|容器自愈
---|---
测试目的|验证容器自愈功能。
预置条件|实例化完成。容器重建开关打开。
测试过程|将虚机上一个容器删除。
通过准则|容器重建成功
测试结果|–
###### 虚机自愈 
测试项目|虚机自愈
---|---
测试目的|验证虚机自愈功能。
预置条件|实例化完成。虚机重建开关打开。
测试过程|在NFVO的虚机管理界面上删除一个虚机。
通过准则|虚机重建成功，虚机上容器运行正常。
测试结果|–
常见问题处理 : 
无 
## ZUF-76-02-004 支持多个IaaS云平台 
概述 : 
ZTE AMF/MME/SGSN支持适应多个IaaS云平台，如ZTE TECS、VMWare以及基于OpenStack的第三方IaaS云平台。 
客户收益 : 
操作员层面： 
有助于网络操作员在多个IaaS云平台中部署VNF。 
说明 : 
ZTE AMF/MME/SGSN支持适应以下多个IaaS云平台： 
ZTE TECS 
VMWare 
基于OpenStack（如RedHat OpenStack）的第三方IaaS云平台 
## ZUF-76-02-005 虚机的反亲和部署 
概述 : 
虚机的反亲和部署功能提供反亲和机制，允许将虚机部署在不同的物理资源中。 
客户收益 : 
操作员层面： 
有助于网络操作员提高虚机的可靠性，安全服务可用性和连续性。 
说明 : 
相同应用类型（例如OMU和IPU）的虚机可由VIM部署在不同的物理资源中。 
# 缩略语 
# 缩略语 
## CPU 
Central Processing Unit中央处理器
ETSI : 
European Telecommunications Standards Institute欧洲电信标准化协会
## KPI 
Key Performance Indicator关键性能指标
MANO : 
Management and Orchestration管理和编排
MME : 
Mobility Management Entity移动管理实体
NF : 
Network Function网络功能
NFV : 
Network Functions Virtualization网络功能虚拟化
## NFVI 
Network Functions Virtualization Infrastructure网络功能虚拟化基础设施
NFVO : 
Network Functions Virtualization Orchestrator网络功能虚拟化编排器
## NS 
Network Service网络服务
OMU : 
Operation & Management Unit操作管理单元
PGW : 
PDN Gateway分组数据网网关
SGW : 
Serving Gateway服务网关
## TECS 
Tulip Elastic Cloud System郁金香弹性云系统
VIM : 
Virtualized Infrastructure Manager虚拟化基础设施管理系统
## VLAN 
Virtual Local Area Network虚拟局域网
VM : 
Virtual Machine虚拟机
VNF : 
Virtualized Network Function虚拟化网络功能
VNFM : 
Virtualized Network Function Manager虚拟化网络功能管理器
# ZUF-76-03 版本升级 
## ZUF-76-03-001 升级 
特性描述 : 
特性描述 : 
术语 : 
本特性不涉及相关术语。 
描述 : 
定义 : 
软件升级是指软件从低版本到高版本的更新，用于解决bug或者满足用户新需求。 
ZTE EMS支持对VNF版本的集中管理，通过自动化的一键升级和一键回退，操作人员可以方便对VNF的软件版本进行集中升级管理。 
背景知识 : 
ZTE EMS支持VNF软件管理功能，提供VNF版本一键升级、版本回退及查看升级报告功能。 
升级包：网元软件升级的目标版本包。可以同时供多网元使用，也可以多次使用。 
升级任务：所有操作都通过任务来管理。创建任务时分别设置各个升级步骤的执行策略（手动、定时），对每个VNF设置不同的升级包、升级参数等。升级过程中（或升级完成后）通过界面查看升级信息。 
手工回退：正常升级结束后，若用户想退回升级前的版本，可以便捷的回退版本。过程与升级类似。不同地方在于，回退只能手动执行。回退完成后也会生成报告，在报告管理中方便的查看报告。 
升级报告：升级完毕后，系统会自动生成报告供用户查看。 
普通升级：一次性更新所有组件的版本，重启后自动加载新版本，进行中的业务将会中断。 
ISSU升级（不中断升级）：对VNF全部实例进行版本更新，升级过程中不中断业务。 
本特性特指普通升级。 
应用场景 : 
解决故障，或合入用户新需求。 
客户收益 : 
受益方|受益描述
---|---
运营商|有助于统一维护软件版本的集中升级管理，使操作快捷、方便、简易。
移动用户|不涉及终端用户收益。
实现原理 : 
系统架构 : 
维护人员通过升级管理对网元版本进行升级，系统架构如[图1]所示。
从EMS上发起VNF软件升级，通过与VNF交互，完成VNF软件版本的升级。 
图1  系统架构
###### 涉及的网元/NF 
网元名称|网元作用
---|---
EMS|主要提供获取升级VNF对象等功能。
Catalog|软件仓库，负责对VNF软件升级包进行存储，对其状态进行更新和维护。
VNF|升级操作的实施对象，通过与EMS交互，完成升级操作。
协议栈 : 
本特性不涉及协议栈。 
本网元实现 : 
创建升级任务 
任何VNF软件版本升级，必须创建一个升级任务，通过任务形式完成VNF的软件版本升级，概述如下： 
定义版本升级任务名称。 
选择版本升级VNF和对应的升级软件包。 
校验版本升级VNF和升级软件包，如果匹配则创建成功。 
指定任务类型（自动执行还是手工执行）。 
升级VNF版本 
根据VNF版本升级配置的升级步骤，软件管理执行升级步骤，直至执行完所有升级步骤，完成VNF的版本软件升级。 
升级过程中一旦出现任何异常导致无法升级，和用户交互或者系统自动判断，根据最终的判断结果，给出各种操作选项，如继续升级，停止升级，还是回退。 
回退VNF版本 
升级管理根据VNF版本升级配置的回退步骤，依次执行直至回退完毕。 
查看升级报告 
升级完毕后（不论是正常还是异常完毕），系统自动产生升级报告，给出升级过程中所有相关升级信息。 
对于升级失败的场景下，通过升级报告可以快速定位失败原因。 
业务流程 : 
创建升级任务
图2  创建升级任务流程
“创建任务”时，软件管理向EMS查询升级对象。 
EMS获取所有升级对象。 
EMS向软件管理返回并显示升级对象。 
软件管理向EMS查询升级包。 
EMS查询所有升级包。 
EMS向软件管理返回并显示升级包。 
软件管理上选择升级包。 
软件管理向EMS获取升级类型请求。 
EMS向VNF获取升级类型请求 
VNF向EMS返回升级类型。 
EMS向软件管理返回并显示升级类型。 
软件管理上选择升级类型。 
软件管理向EMS发送初始化升级对象请求。 
EMS向VNF发送初始化升级对象请求。 
VNF向EMS返回应答。 
EMS向软件管理返回应答。 
软件管理向EMS发送加载升级包请求。 
EMS向VNF发送加载升级包请求。 
VNF通过SFTP/FTP加载升级包。 
VNF向EMS返回版本加载进度。 
EMS向软件管理返回版本加载进度直到完成。 
软件管理向EMS发送获取步骤文件请求。 
EMS向VNF发送获取步骤文件请求。 
VNF向EMS返回步骤文件。 
EMS向软件管理返回步骤文件。 
软件管理上设置升级步骤。 
软件管理上设置升级参数。 
升级任务创建完毕，用例结束。 
执行升级任务
图3  执行升级任务流程
用户进入升级管理，单击“执行任务”。 
软件管理向EMS发送执行升级步骤请求。 
EMS向VNF发送执行升级步骤请求。 
VNF向EMS返回升级步骤。 
EMS向软件管理返回升级步骤。 
软件管理向EMS发送执行升级子步骤请求。 
EMS向VNF发送执行升级子步骤请求。 
VNF向EMS返回升级子步骤。 
EMS向软件管理返回升级子步骤。 
VNF向EMS上报原因和处理建议。 
EMS向软件管理上报原因和处理建议。 
VNF向EMS上报异常处理操作，显示对应的界面按钮（重试、忽略、停止升级、回退、继续、重启等）。 
EMS向软件管理上报异常处理操作，显示对应的界面按钮（重试、忽略、停止升级、回退、继续、重启等）。 
软件管理显示原因和处理操作，并选择合适的处理操作。 
软件管理向EMS发送执行下一个升级子步骤请求。 
EMS向VNF发送执行下一个升级子步骤请求。 
VNF向EMS返回完成当前的升级步骤。 
EMS向软件管理返回完成当前的升级步骤。 
软件管理直到完成所有的升级步骤。 
软件管理产生升级报告。 
软件管理完成升级任务，用例结束。 
执行回退
图4  执行回退流程
VNF在执行升级子步骤时，某个升级子步骤出现异常导致无法继续升级时，VNF上报回退操作给向EMS上报回退操作。 
EMS向软件管理上报回退操作。 
软件管理执行回退操作。 
软件管理判断失败步骤是否配置了子步骤回退，如果没有则执行整版本回退。 
软件管理向EMS发送执行子步骤回退。 
EMS向VNF发送执行子步骤回退。 
VNF向向EMS上报原因和处理建议。 
EMS向软件管理上报原因和处理建议。 
软件管理执行下一个子步骤回退。 
软件管理完成所有子步骤回退。 
软件管理产生版本回退报告。 
软件管理完成版本回退，用例结束。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性需要网元版本配合支持，适用虚拟化管理的VNF。 
要求VNF状态正常。且在升级过程中，不能进行其它VNF操作，如缩扩容、虚机操作。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
本特性采用中兴通讯内部的接口和协议，不涉及标准协议。 
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
EMS|-
---|---
√|
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
该特性不涉及命令。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
该功能属于基本功能，无需特别配置，只要完成初始配置即可。 
# ZUF-76-04 可靠性 
## ZUF-76-04-001 MME/SGSN POOL 
概述 : 
ZTE MME/SGSN支持POOL组网。POOL中的每个网络节点都承载一部分用户。 
客户收益 : 
操作员层面： 
POOL中的每个MME/SGSN都承载一部分用户。当一个MME/SGSN不起作用时，RAN将用户接入到POOL中的其他MME/SGSN，以确保网络可靠性。 
说明 : 
ZTE MME/SGSN支持POOL组网。 
多个SGSN、MMECN节点同时服务一组RAN覆盖的无线网络区域。在这些区域中，所有UE拥有同等机会访问每个SGSN/MME。当一个区域发生灾害，导致该区域SGSN/MME故障时，RAN将UE路由到其他区域SGSN/MME。 
## ZUF-76-04-002 MME链式容灾备份 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
语音容灾，是指在IMS/EPC/CS网络中，网元设备出现故障后，能够保证语音业务及时接管和恢复的功能。 
对于VoLTE业务，EPC网络作为VoLTE业务的承载提供者，需要在网元设备出现故障后，能够及时进行EPS承载的重建，以保证VoLTE业务及时恢复。  
对于CSFB业务，MME需要能够在MME故障或MSC故障后，能够及时恢复和MSC的SGs连接，以保证CSFB业务及时恢复。 
背景知识 : 
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
应用场景 : 
###### MME故障后的业务恢复 
MME发生故障或重启，该MME上的UE有下行的数据报文（例如：VoLTE业务终呼信令），SGW能够立即为UE重新选择可用的MME，通过新MME触发UE重新附着，完成EPS承载重建。 
MME发生故障或重启，该MME上的UE有CSFB的终呼业务，MSC/VLR能够立即选择其他可用MME下发寻呼，通过新MME触发UE重新联合附着，完成MSC注册和SGs连接恢复。 
###### SGW故障后的业务恢复 
SGW发生故障或重启，UE的下行业务触发PGW通过可用的SGW通知MME触发UE恢复。同时MME感知SGW故障后扫描故障SGW中的UE，依次触发UE恢复。恢复时，MME可选择触发UE重新附着或者触发UE重新选择SGW，完成EPS承载重建。 
###### PGW故障后的业务恢复 
PGW发生故障或重启，MME针对该PGW上的用户，主动触发UE重新附着或重建IMS
PDN连接，完成EPS承载重建。 
###### P-CSCF故障后的业务恢复 
P-CSCF发生故障或重启，P-CSCF采用基于HSS的方式恢复。MME根据HSS的指示，重建UE的IMS
PDN连接。UE从PGW获取新的P-CSCF地址后，进行IMS注册，完成IMS业务恢复。 
###### MSC故障后的CSFB业务恢复 
MSC发生故障或重启，UE的CS语音被叫业务由备份MSC/VLR向MME下发无LAI寻呼，触发UE的IMSI重新附着。同时MME发现MSC发生故障或重启后，扫描故障MSC中的UE，依次触发UE发起IMSI附着，注册到正常的MSC上，完成CSFB业务恢复。 
###### MSC/VLR手动卸载 
当发现某个MSC故障或者需要升级维护时，需要对该MSC上注册的UE进行迁移。MME提供网管动态管理命令，触发注册在该MSC的UE重新发起IMSI附着。 
客户收益 : 
受益方|受益描述
---|---
运营商|提高系统的可靠性和安全性。在部署了VoLTE的网络中，提高VoLTE业务的可靠性，大幅减少因网络故障对VoLTE业务的影响。
移动用户|网络故障后，VoLTE业务不受影响。
实现原理 : 
涉及的网元 : 
语音容灾功能需要UE、MME、SGW、PGW、HSS、MSC/VLR的共同配合，各网元的主要作用参见下表。 
网元|作用
---|---
UE|接受MME的指示，重新附着、重选SGW或重建IMS PDN连接。
MME|SGW/PGW故障或重启后，MME能够主动触发UE重新附着、重选SGW或重建IMS PDN连接。其他MME故障或重启后，作为新选择的MME能够接受SGW的指示触发UE重新附着；能备份特定MME的UE动态位置信息，以便在寻呼用户时有效控制寻呼范围，
SGW|MME故障或重启后，能够保持PDN连接和承载上下文。在收到下行的数据报文时，可以立即选择一个可用的MME，发送PGWDownlink Triggering Notification消息给MME触发UE恢复。
PGW|SGW故障或重启后，能够保持PDN连接和承载上下文。在收到下行的数据报文时，可以通过其他可用的SGW，发送DownlinkData Notification消息给MME触发UE恢复。
HSS|P-CSCF故障后，能够接收S-CSCF的指示，通知MME触发UE恢复。
MSC/VLR|MME故障或重启后，能够在MME POOL中选择一个MME进行被叫业务。MSC/VLR故障或重启后，作为备用MSC/VLR能够下发无LAI寻呼。
业务流程 : 
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
系统影响 : 
###### 容灾恢复中 
一旦有一个网元发生故障或重启，该网元上的所有用户都有待恢复。这些用户的恢复过程，对POOL内的其他网元，带来了额外的业务负荷，所以POOL内的网元都需要有适当的冗余（一般情况下冗余1/N，N为POOL内节点数目），来保证容灾的业务接管。 
为了防止短时间内大量用户恢复造成的业务激增，需要MME在扫描恢复时，合理地控制单位时间内恢复的用户数目，既要避免对同时处理的正常业务造成过大的影响，也要避免恢复时间过长。 
按每秒每模块最快恢复40个用户、每模块5万用户需要恢复来计算，全部恢复需要约21分钟，触发恢复的业务负担增加不超过3%。 
###### 容灾准备中 
为了满足MME故障恢复时寻呼负荷的控制，POOL内的MME间需要实时的进行用户动态位置信息的备份，这将会增加一定的MME局间信令和业务负荷，但不超过1%。 
###### MME在无用户注册信息时的寻呼 
MME POOL组网中，如果用户所在的MME宕机，则MSC/VLR在MME
POOL中重选可用的MME下发寻呼。MME收到寻呼消息后，尽管当前没有UE的上下文信息，但是判断寻呼消息中携带有CS业务恢复指示，则采用IMSI寻呼的方式。IMSI寻呼时，MME可以利用寻呼消息中的LAC信息，或者是从故障MME的备份节点获取用户的位置信息来控制寻呼范围，而避免全网寻呼。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
业务|交互
---|---
本地资源回收|采用容灾业务恢复后，无需再使用本地资源回收。本地资源回收，是指SGW/PGW故障后，MME将相关的会话上下文资源予以回收，而不通知UE恢复业务。
遵循标准 : 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access". 
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3". 
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)". 
3GPP TS 29.274: "General Packet Radio Service (GPRS); Evolved GPRS Tunnelling Protocol (eGTP) for EPS". 
3GPP TS 29.272: " Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol". 
3GPP TS 23.007: "Restoration procedures". 
特性能力 : 
MME主动触发的UE恢复流程，最大支持每秒每模块100个用户。 
MME间的备份关系可支持链式备份和集中备份。 
可获得性 : 
License要求 : 
该特性需要申请了下表中的License许可后，运营商才能获得该特性的服务。 
License ID|License控制值|License描述
---|---|---
7049|支持|MME支持MME容灾故障恢复功能
7058|支持|MME支持SGW容灾故障恢复功能
7059|支持|MME支持PGW容灾故障恢复功能
7052|支持|MME支持P-CSCF恢复功能
7056|支持|MME支持SGs口主动恢复
对其他网元的要求 : 
需要SGW支持容灾故障恢复的相关功能，支持3GPP TS 23.007中描述的“网络侧触发的业务恢复”功能。 
需要PGW支持容灾故障恢复的相关功能，支持3GPP TS 23.007中描述的“网络侧触发的业务恢复”功能。 
需要MSC/VLR支持容灾故障恢复的相关功能，支持3GPP
TS 23.007中描述的“网络侧触发的业务恢复”功能。 
需要HSS支持3GPP TS 23.380中描述的“P-CSCF恢复”功能。 
由于POOL内MME间传递UE动态位置信息备份的接口是私有接口，所以要求POOL内的MME由同一厂家提供。 
工程规划要求 : 
语音容灾对组网无特殊要求。 
MME间采用S10接口的GTP-C地址进行通信以实现UE的动态位置信息备份。 
O&M相关 : 
命令 : 
配置项表1  新增配置项配置项命令容灾恢复配置SET SERVRSTOCFGSHOW SERVRSTOCFGADD POOLBAKMMECFGSET POOLBAKMMECFGDEL POOLBAKMMECFGSHOW POOLBAKMMECFG表2  修改配置项配置项命令修改的参数Support Feature管理ADD SUPFEATURESupport Feature 2SET SUPFEATURESupport Feature 2SHOW GLOBAL SUPFEATURESupport Feature 2SGs口VLR局向配置ADD VLROFFICE局向属性SET VLROFFICE局向属性SHOW VLROFFICE局向属性 
软件参数表3  新增软件参数软件参数ID软件参数名称786732支持MME容灾的未知备份节点的备份数据查询786733查询他局备份数据等待时间262446支持SMS Only用户的SGs口主动恢复 
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
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
通过配置实现语音容灾功能。 
配置前提 : 
MME基础配置已经完成，即用户可以在MME附着并且该用户的语音承载已建立。 
容灾相关License功能项已经设置为支持，包括：MME支持MME容灾故障恢复功能、MME支持SGW容灾故障恢复功能、MME支持PGW容灾故障恢复功能、MME支持P-CSCF恢复功能、MME支持SGs口主动恢复。 
需要规划POOL内MME间的动态位置信息备份关系。比如POOL内有四个MME：MME1、MME2、MME3、MME4，链式备份的备份关系为MME1的备份为MME2、MME2的备份为MME3、MME3的备份为MME4、MME4的备份为MME1。 
需要配置与MME对接的VLR POOL以及POOL内各个VLR的权重和优先级，以便MME进行VLR选择。 
配置过程 : 
执行命令[SET SERVRSTOCFG]，分别开启支持SGW容灾恢复、支持PGW容灾恢复、支持MME容灾恢复、支持P-CSCF容灾恢复、支持PGW触发的SGW恢复的开关。
对应的参数为：支持SGW容灾恢复、支持PGW容灾恢复、支持MME容灾恢复、支持P-CSCF容灾恢复、支持PGW触发的SGW恢复。
对于已经配置Feature ID的HSS局向，执行命令[SET SUPFEATURE]，配置支持P-CSCF Restoration能力。
对应的参数为：Support Feature
2。
执行命令[SET VLROFFICE]，配置VLR局向支持故障后的主动恢复的开关。
对应的参数为：局向属性。
执行命令[SET SERVRSTOCFG]，配置合理的容灾恢复速率和GW容灾寻呼范围。
对应的参数为：容灾恢复扫描速率(用户数/百毫秒/模块)、容灾业务恢复速率(Subscriber/100
ms/Module)、GW容灾恢复时IMSI寻呼范围。
执行命令[SET SERVRSTOCFG]，配置合理的采用SGW重选方式的故障恢复时长。
对应的参数为：采用SGW重选方式的故障恢复时长(分钟)。
执行命令[SET SERVRSTOCFG]，配置本MME的备份节点IP。
对应的参数为：备份MME的MME IP地址。
执行命令[ADD POOLBAKMMECFG]，配置POOL内其它MME的IP及其备份节点IP。
对应的参数为：MME的GTPC地址、备份MME的GTPC地址。
执行命令[SET SERVRSTOCFG]，配置合理的动态位置信息备份速率。
对应的参数为：数据备份消息发送频率(毫秒)、数据备份消息包大小(KB)。
执行命令[SET SOFTWARE PARAMETER]，根据需要开启“支持MME容灾的未知备份节点的备份数据查询”功能，并设置合理的“查询他局备份数据等待时间”。
“支持MME容灾的未知备份节点的备份数据查询”对应的软件参数ID为786732
；“查询他局备份数据等待时间”对应的软件参数ID为786733
。
执行命令[SET SERVRSTOCFG]，配置合理的备份数据老化时长。
对应的参数为：备份数据老化时长(小时)。
执行命令[SET SERVRSTOCFG]，配置合理的VLR局向故障恢复检测时长。
对应的参数为：VLR局向故障恢复检测时长(分钟)。
执行命令[SET SOFTWARE PARAMETER]，开启“支持SMS Only用户的SGs口主动恢复”功能。
“支持SMS Only用户的SGs口主动恢复”对应的软件参数ID为262446
。
配置实例 : 
###### MME容灾配置 
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
[SET SERVRSTOCFG]:MMERSTOFLAG="YES",BAKMMEIP="10.10.10.10",BAKRATE=1000,BAKSIZE=4;
配置POOL内MME间备份关系，命令如下： 
[ADD POOLBAKMMECFG]:MMEIP="10.10.10.10",BAKMMEIP="10.10.10.11",NAME="MME1";
[ADD POOLBAKMMECFG]:MMEIP="10.10.10.11",BAKMMEIP="10.10.10.12",NAME="MME2";
[ADD POOLBAKMMECFG]:MMEIP="10.10.10.12",BAKMMEIP="10.10.10.13",NAME="MME3";
配置未知备份节点的相关软件参数，命令如下： 
[SET SOFTWARE PARAMETER]:PARAID=786732,PARAVALUE=1; 
[SET SOFTWARE PARAMETER]:PARAID=786733,PARAVALUE=3;
###### SGW容灾配置 
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
[SET SERVRSTOCFG]:SGWRSTOFLAG="YES",PGWTRIGSGWRSTO="YES",RSTOSCANRATE=40,RSTORATE=5,GWRSTOPGAREA="TALIST",SGWRELOCTIME=10;
###### PGW容灾配置 
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
[SET SERVRSTOCFG]:PGWRSTOFLAG="YES",RSTOSCANRATE=40,RSTORATE=5,GWRSTOPGAREA="TAList";
配置IMS APN NI，命令如下： 
[ADD IMS APN]:APNNAME="IMS";
###### P-CSCF容灾配置 
在P-CSCF容灾配置之前，应当完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
支持P-CSCF容灾恢复|支持
HSS局向支持P-CSCF Restoration能力|支持
根据规划，分两种情况进行如下配置。 
已配置Feature ID（值为1）的HSS开启P-CSCF Restoration的场景打开支持P-CSCF容灾恢复功能开关，命令如下：SET SERVRSTOCFG: PCSCFRSTOFLAG="YES";打开HSS局向支持P-CSCF Restoration能力开关，命令如下：SET SUPFEATURE:FEATUREID=1,SUPFEATURE2="PCSCF"; 
未配置Feature ID的HSS开启P-CSCF Restoration的场景打开支持P-CSCF容灾恢复功能开关，命令如下：SET SERVRSTOCFG: PCSCFRSTOFLAG="YES";新增Support Feature配置，支持P-CSCF Restoration，命令如下：ADD SUPFEATURE:FEATUREID=1,SUPFEATURE="TRACE"&"TADS"&"STALOC",SUPFEATURE2="PCSCF"; 说明：注意要把全局支持的Support Feature配置进去，可以使用SHOW GLOBAL SUPFEATURE命令查询全局支持的Support Feature。HSS的Diameter邻接局向（ID为1）配置引用Support Feature配置中的Feature ID参数，命令如下：SET DIAMADJ:ADJID=1,SUPFEATUREID=1; 
###### SGs口快速恢复配置 
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
[SET VLROFFICE]:VLROFFICEID=1,ATTR="ASSRES";
[SET VLROFFICE]:VLROFFICEID=2,ATTR="ASSRES";
[SET VLROFFICE]:VLROFFICEID=3,ATTR="ASSRES";
配置SGs口快速恢复参数，命令如下： 
[SET SERVRSTOCFG]:RSTOSCANRATE=40,RSTORATE=5,VLRDETCTIME=2;
配置支持SMS Only用户SGs口主动恢复，命令如下： 
[SET SOFTWARE PARAMETER]:PARAID=262446,PARAVALUE=1;
调整特性 : 
POOL内MME间备份关系调整：当因为POOL内增加或减少MME节点等原因，导致需要调整POOL内MME间备份关系，可参考配置过程中的步骤6和步骤7予以调整。 
备份速率调整：一般无需特别调整备份速率，如需调整可参考配置过程中的步骤8。 
恢复速率调整：一般无需特别调整恢复速率，特殊情况下，可根据系统的负荷情况加快或减慢恢复速率，调整方法可参考配置过程中的步骤4。 
采用SGW重选方式的故障恢复时长调整：需要根据PGW发现SGW故障后，保留PDN连接的时间来调整，保证采用SGW重选方式的故障恢复时，PGW仍保留有原PDN连接。 
测试用例 : 
###### MME容灾恢复 
测试项目|MME容灾恢复
---|---
测试目的|测试MME收到SGW发送的DDN消息后，能够触发用户重新附着。
预置条件|EPC网络中各网元运行正常。POOL内有三个MME网元。
测试过程|用户附着后，处于IDLE态。用户附着的MME故障。网络侧有下行数据报文。
通过准则|用户附着成功，能够在备份的MME上查询到该用户的备份数据。新的MME收到SGW发送的DDN消息后，获取用户的位置信息，寻呼用户。用户重新附着成功。
测试结果|
###### SGW容灾恢复-MME发起的重新附着 
测试项目|SGW容灾恢复-MME发起的重新附着
---|---
测试目的|测试SGW故障后MME能够主动触发用户重新附着。
预置条件|EPC网络中各网元运行正常。采用SGW重选方式的故障恢复时长设置为0分钟。
测试过程|用户附着后，处于IDLE态。用户所在的SGW故障。
通过准则|用户附着成功。一段时间后，MME寻呼用户。用户重新附着成功。
测试结果|
###### SGW容灾恢复-MME发起的重选SGW 
测试项目|SGW容灾恢复-MME发起的重选SGW
---|---
测试目的|测试SGW故障后MME能够主动触发用户重选SGW。
预置条件|EPC网络中各网元运行正常。采用SGW重选方式的故障恢复时长设置为2分钟。
测试过程|用户附着后，处于IDLE态。用户所在的SGW故障。
通过准则|用户附着成功。SGW故障，2分钟内用户都会重选SGW 。
测试结果|
###### SGW容灾恢复- PGW触发的恢复 
测试项目|SGW容灾恢复- PGW触发的恢复
---|---
测试目的|测试SGW故障后PGW主动触发恢复。
预置条件|EPC网络中各网元运行正常。支持PGW触发的SGW恢复的开关。
测试过程|用户附着后，处于IDLE态。PGW重选一个正常的SGW，MME收到SGW发送的PGW Downlink Triggering Notification消息，消息中携带此用户的IMSI。
通过准则|MME返回成功的PGW Downlink Triggering Answer消息，不携带MMEID。用户处于IDLE态，MME寻呼UE。MME收到UE的业务请求后，重选SGW。
测试结果|
###### PGW容灾恢复 
测试项目|PGW容灾恢复
---|---
测试目的|测试用户仅IMS PDN连接对应的PGW故障后，MME能够触发用户重建IMS PDN连接。
预置条件|EPC网络中各网元运行正常。
测试过程|用户附着时创建数据PDN连接，再创建IMS PDN连接。用户IMS PDN连接对应的PGW故障。
通过准则|用户附着成功，建立两个PDN连接。一段时间后，MME指示UE重建IMS PDN连接。用户重建IMS PDN连接成功。
测试结果|
###### P-CSCF容灾恢复 
测试项目|P-CSCF容灾恢复
---|---
测试目的|测试MME根据HSS的IDR指示，重建IMS PDN，进行P-CSCF恢复。
预置条件|EPC网络中各网元运行正常。MME的License中支持P-CSCF容灾恢复。支持P-CSCF容灾恢复的开关打开。HSS局向关联的Feature ID配置支持P-CSCF Restoration能力。MME支持Feature协商。
测试过程|用户附着时，HSS返回的ULA消息指示支持P-CSCF恢复。用户建立普通PDN，再建立一个IMS PDN，并建立专有承载。用户处于连接态，收到HSS发送的IDR消息中携带P-CSCF恢复flag。
通过准则|MME收到IDR后，返回成功的IDA，发起IMS PDN去连接，携带NAS原因值为“reactivation requested”，同时通知SGW删除会话。
测试结果|
###### SGs口主动恢复 
测试项目|SGs口主动恢复
---|---
测试目的|测试VLR故障时，能触发SGs口的主动恢复。
预置条件|MME的License中支持SGs口主动恢复。SGs口的VLR局向支持故障后的主动恢复。VLR局向都可达。VLR局向故障恢复检测时长为2分钟。容灾业务扫描速率为40/100ms。容灾业务恢复速率为5/100ms。
测试过程|用户在VLR上联合附着，处于连接态。VLR不可达时间达到阈值2分钟。MME发送IMSI Detach消息后，收到UE发出的Detach Accept消息和联合TAU消息。
通过准则|VLR不可达两分钟后直接进行IMSI Detach，并清除SGs状态。MME收到Detach Accept后，不主动释放S1连接，收到联合TAU后，重选VLR发起位置更新。
测试结果|
常见问题处理 : 
无。 
## ZUF-76-04-005 VNFC支持1+1主备冗余 
特性描述 : 
特性描述 : 
术语 : 
本特性不涉及相关术语。 
描述 : 
定义 : 
实例主备特性是指运行实例采用主用和备用的工作方式，即一个主用，一个备用。正常工作状态时，主用实例提供服务，备用实例对主用实例的数据进行备份。当主用异常宕机或执行主备倒换命令时，备用转换为主用提供服务，从而保证业务正常运行。 
背景知识 : 
为提高系统可靠性，业务处理实例需要提供冗余机制，在实例发生故障的情况下，由其他运行实例继续处理话务，从而保障系统不间断提供服务。引入该特性的目的在于提高运行实例的可靠性，从而进一步提高NF的可靠性。 
应用场景 : 
本特性作为系统的基本特性，在商用系统运行时，均需要提供。 
客户收益 : 
受益方|受益描述
---|---
运营商|运营商可以通过实例主备特性提高系统运行可靠性，降低系统运行风险
终端用户|此特性对终端用户不可见
实现原理 : 
系统架构 : 
实例主备的系统架构如[图1]所示。
图1  实例主备
采用实例主备工作方式时，主用（Active）运行实例和备用（Standby）运行实例分别运行在不同的资源之上，如：不同的虚机或容器、不同的硬件服务器，以及不同的资源分区（ZONE）。主用运行实例处于工作状态（Active），当主用运行实例故障宕机或执行倒换时，备用运行实例成为主用（Active），保证服务不间断。 
uMAC网元采用实例主备工作方式的VNFC为OMU。 
业务流程 : 
本特性不涉及业务流程。 
NF实现 : 
uMAC网元中，采用实例主备工作方式的VNFC为OMU。 
协议栈 : 
该特性不涉及。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
该特性不涉及。 
特性能力 : 
该特性不涉及规格指标。 
版本要求及变更记录 : 
序号|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布。
可获得性 : 
License要求 : 
该特性为基本特性，无需license支持。 
对其他网元的要求 : 
该特性不涉及对其他网元的要求。 
工程规划要求 : 
该特性不涉及工程规划要求。 
特性配置 : 
该功能属于基本功能，无需特别配置，只要完成初始配置即可。 
## ZUF-76-04-006 VNFC支持N+M负荷分担冗余 
特性描述 : 
特性描述 : 
术语 : 
本特性不涉及相关术语。 
描述 : 
定义 : 
实例负荷分担特性是指运行实例采用负荷分担的工作方式，即所有运行实例共同分担处理业务。当部分运行实例异常宕机时，由其余运行正常的实例共同分担处理业务，从而保证业务正常运行。在此工作方式下，采用N+M冗余方式，即当N个实例可以满足系统容量的业务处理时，再提供M个实例用于冗余，且N+M个实例共同分担处理业务，此时系统能够承受最多M个实例的异常宕机而不影响系统处理能力。 
背景知识 : 
为提高系统可靠性，业务处理实例需要提供冗余机制，在个别实例发生故障的情况下，其他正常运行的实例仍然可以继续处理话务，从而保障系统不间断提供服务。引入该特性的目的在于提高运行实例的可靠性，从而进一步提高NF的可靠性。 
应用场景 : 
本特性作为系统的基本特性，在商用系统运行时，均需要提供。 
客户收益 : 
受益方|受益描述
---|---
运营商|运营商可以通过实例负荷分担特性提高系统运行可靠性，降低系统运行风险
终端用户|此特性对终端用户不可见
实现原理 : 
系统架构 : 
采用N+M冗余方式的实例负荷分担的系统架构如[图1]所示。
图1  实例负荷分担
采用实例负荷分担工作方式的服务运行实例，全部为主用（Active）工作状态。运行实例分别运行在不同的资源之上，如不同的虚机或容器、不同的硬件服务器，以及不同的资源分区（ZONE）。当部分（小于等于M）运行实例故障宕机时，其业务由其他正常运行的实例继续处理，从而可以不间断提供服务。 
uMAC网元中采用实例负荷分担工作方式的VNFC为 GSU/CDU/IPU。 
业务流程 : 
本特性不涉及业务流程。 
NF实现 : 
uMAC网元中采用实例负荷分担工作方式的VNFC为 GSU/CDU/IPU。 
协议栈 : 
该特性不涉及。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
该特性不涉及。 
特性能力 : 
该特性不涉及规格指标。 
版本要求及变更记录 : 
序号|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布。
可获得性 : 
License要求 : 
该特性为基本特性，无需license支持。 
对其他网元的要求 : 
该特性不涉及对其他网元的要求。 
特性配置 : 
该功能属于基本功能，无需特别配置，只要完成初始配置即可。 
## ZUF-76-04-007 AMF/MME/SGSN过负荷控制 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响遵循标准特性能力可获得性O&M相关 
术语 : 
术语|含义
---|---
过负荷控制|限制接入的业务量，来降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。
描述 : 
定义
过负荷控制功能指在设备处理的业务量超过了处理能力时，需要采取的保护措施，以限制处理的业务量，来降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。 
背景知识
为了防止以下情况而引起突发业务冲击对整个系统的影响，各个设备上必须使用过负荷控制。 
在各个网元中，经常会出现因为某些原因（例如网元重启后、对方网元不可达，用户大量移动）导致用户短时间内暴发超过正常话务模型的业务请求次数。此时，各设备的处理器CPU资源、数据区资源、甚至接口或内部交换带宽都可能达到极限能力，从而导致系统崩溃，例如CPU占用率长时间100%会导致自愈系统认为故障而复位。 
某些网元处理能力很强，突然涌现的业务，对自身影响不大，但周边网元由于比较老旧，无法处理突发业务，也没有过负荷保护，从而系统崩溃，而周边网元的宕机导致了自身网元的业务也无法进行。 
uMAC网元（包括AMF/MME/SGSN）提供控制手段参见[表1]。
功能名称|功能概述
---|---
入向业务总量控制|控制单位时间内允许通过的业务总量，业务总量的计算为各个单项业务的加权叠加。
入向单项业务控制|控制单位时间内通过的各个单项业务量。
CPU拥塞控制|在服务组件上根据CPU拥塞情况对各类业务限制一定的通过率，保护CPU不会冲高MP 。
出向业务控制|对于本MME、SGSN发起的到其他网元（比如HSS、EIR）的业务，或者AMF发往RAN、SBI接口限制一定的业务量，保护对方网元不会被冲击。
信令拥塞控制|按照信令链路拥塞情况，限制信令接口的业务通过量，保护信令链路。
按网元拥塞控制|对于AMF/MME/SGSN，协议支持N2、S1、Iu口overload消息，可以告知对方网元本局拥塞情况，接收overload消息的网元就会控制本方发送的信令。对于Iu口，SGSN和RNC可以互相通知；对于S1口/N2口，只有AMF/MME通知gNodeB/eNodeB。
自动负荷控制（Auto Load Control）|如果HLR\HSS处理能力较弱，根据Gr\S6a口消息成功率，会自动调整接入业务（比如附着、局间TAU/RAU、跨RAT TAU/RAU）的速率。
在遭遇业务量突发增加时，uMAC网元为了保障自身工作正常，可通过以下方式控制本网元处理的业务量。 
使用入向业务控制功能（包括总量和单项业务量）和CPU拥塞控制功能。 
通知RNC/eNodeB/gNodeB网元，本网元的业务已经过负荷，需要RNC/eNodeB/gNodeB网元控制接入到本网元的业务数量。 
如果uMAC网元的周边网元如HLR/HSS/UDM等网元处理能力较弱，uMAC网元为了保障周边网元安全，可通过以下方式控制出局到该网元的业务数量。
使用出向业务控制功能和信令拥塞控制功能。 
使用自动负荷控制功能，根据Gr/S6a口消息成功率来控制接入业务的速率。 
接收RNC的过负荷通知，减少该RNC的业务。 
应用场景 : 
遭遇突发业务场景
uMAC网元忽然接入超过估算话务模型的业务量，CPU占用陡升。例如，举办大型赛事，大量外地用户涌入。uMAC网元可采用以下过负荷控制功能来保证自身安全： 
入向业务总量控制 
入向业务单项控制 
CPU拥塞控制功能 
按网元拥塞控制 
建议开启CPU拥塞控制功能，该功能默认开启，CPU的过载门限为75%，高过载门限为85%。在过载拥塞时只对低优先级业务（默认为Attach、Service
Request、注册-初次注册、事件暴露订阅等）进行控制，只要在CPU高过载时对所有业务进行控制，包括高优先级业务（默认为TAU/RAU、HO、注册-位置更新）。在默认情况下已经可以保证对uMAC网元的保护，但如果持续出现过负荷告警，建议通过扩容来降低uMAC设备的负荷。 
uMAC设备升级场景
在设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。 
uMAC网元可采用以下过负荷控制功能来保证自身安全： 
入向业务总量控制 
入向业务单项控制 
CPU拥塞控制功能 
按网元拥塞控制 
建议除了使用默认开启的CPU拥塞控制功能外，开启入向业务控制功能对Attach业务进行限制，限制的数值为1小时内所有用户接入的速率，即全部接入的用户数/业务服务组件实例数/3600。例如：本局有100万用户，16个实例，则需要限制Attach接入业务数为1000000/16/3600=17次。 
邻接的HLR/HSS/UDM等网元处理能力弱场景
由于HLR/HSS/UDM是老的网元或未完成扩容，整体处理能力弱。在SGSN/MME/AMF业务繁忙时，无法处理位置更新业务，甚至出现了宕机重启的情况。 
uMAC网元提供了如下功能来保护邻接网元： 
出向业务控制功能 
信令拥塞控制功能 
自动负荷控制功能 
为了保护HLR/HSS/UDM等网元，除了默认开启的信令拥塞功能外，还建议开启出向业务控制功能，对SGSN/MME/AMF发出的业务进行控制。例如本场景中评估HLR/HSS/UDM最多处理1000条/秒位置更新业务，则可以在出向业务控制功能中配置本局到该HLR/HSS局向，或者SBI接口，最多发送1000条/秒位置更新业务。 
SGSN/MME还支持自动负荷制功能，根据Gr\S6a口消息成功率，自动调整接入业务（比如附着、局间TAU/RAU、跨RAT TAU/RAU）的速率。 
客户收益 : 
受益方|受益描述
---|---
运营商|防止设备被突发大量业务冲击，在突发大话务情况下，不会异常或者崩溃，提高网络的稳定性。
实现原理 : 
涉及的网元
网元|作用
---|---
RNC|RNC发生拥塞通知SGSN。接收SGSN的过负荷通知消息，并进行拥塞控制。
uMAC设备（SGSN）|接收RNC的过负荷通知消息，并进行拥塞控制。通知RNC，SGSN设备发生拥塞。
uMAC设备（MME）|通知eNB，MME设备发生拥塞。
uMAC设备（AMF）|通知gNB，AMF设备发生拥塞。
eNodeB|接收MME的过负荷通知消息，并进行拥塞控制。
gNodeB|接收AMF的过负荷通知消息，并进行拥塞控制。
本网元实现
uMAC过负荷控制功能控制的是用户业务流程的首个消息，对后续消息放行。在系统负荷允许的范围内通过尽量多的业务。用户业务被拒绝后，通过重新尝试，可以逐渐平滑的接入进来。 
uMAC过负荷控制功能说明如[图1]所示。
图1  过负荷控制功能
默认情况下，uMAC系统已经开启了CPU负荷控制、自动负荷控制和信令拥塞控制，没有开启业务流量控制（包括出向和入向）和网元拥塞控制。在这种默认配置下已经能很好的保护自身网元，同时对邻接网元也开启了基本保护。 
业务流程
N2口拥塞通知
AMF在过负荷情况时，发送overload start消息通知gNodeB，在退出过负荷时，发送overload stop消息给gNodeB。如[图2]所示
图2  N2口拥塞通知
S1口拥塞通知
MME在过负荷情况时，发送overload
start消息通知eNodeB，在退出过负荷时，发送overload stop消息给eNodeB。如[图3]所示。
图3  S1口拥塞通知
RNC拥塞通知SGSN
RNC在过负荷情况下，向SGSN发送Overload消息，SGSN会根据RNC的拥塞情况对Iu口下行触发的业务首个消息进行控制。如[图4]所示。
图4  RNC拥塞通知SGSN
SGSN拥塞通知RNC
SGSN在过负荷情况下，向RNC发送Overload消息，通知RNC本方拥塞。如[图5]所示。
图5  SGSN拥塞通知RNC
系统影响 : 
过负荷控制功能在系统过负荷情况下，会拒绝进行部分业务处理。对放行的业务没有影响。 
遵循标准 : 
3GPP TS 25.413: "UTRAN Iu interface Radio Access Network Application
Part (RANAP) signaling” 
3GPP TS 36.413: " S1 Application Protocol (S1AP)” 
3GPP TS 38.413：“NG Application Protocol (NGAP)” 
特性能力 : 
CPU过负荷功能分为2级过负荷（高过载和低过载），在高过载时才控制优先业务。 
默认控制周期为1秒，检测计算周期为5秒。 
可获得性 : 
对其他网元的要求
本功能基本上由uMAC网元的内部实现；仅在进行网元间的拥塞控制时，需要RNC、eNB共同配合。 
工程规划要求
无特殊要求。 
O&M相关 : 
命令
新增配置项参见[表2]和[表3]。
配置项（SGSN/MME）|命令
---|---
过负荷基本参数配置|SET OVERLOAD BASIC PARA
SHOW OVERLOAD BASIC PARA|过负荷基本参数配置
SGSN通用过负荷参数配置|SET OVERLOAD PARA
SHOW OVERLOAD PARA|SGSN通用过负荷参数配置
SGSN通用业务控制配置|SET SERVICE CONTROL
SHOW SERVICE CONTROL|SGSN通用业务控制配置
SGSN特定局向业务控制配置|ADD SGSN OFFICE SERVICE MAXIMUM
SET SGSN OFFICE SERVICE MAXIMUM|SGSN特定局向业务控制配置
DEL SGSN OFFICE SERVICE MAXIMUM|SGSN特定局向业务控制配置
SHOW SGSN OFFICE SERVICE MAXIMUM|SGSN特定局向业务控制配置
MME过负荷参数配置|SET MME OVERLOAD PARA
SHOW MME OVERLOAD PARA|MME过负荷参数配置
MME通用业务控制配置|SET MME SERVICE CONTROL
SHOW MME SERVICE CONTROL|MME通用业务控制配置
配置项（AMF）|命令
---|---
CPU负荷等级配置|SET OLCPULEVELCFG
SHOW OLCPULEVELCFG|CPU负荷等级配置
控制参数配置|SET OVERLOADCFG
SHOW OVERLOADCFG|控制参数配置
保证通过量配置|SET OLGUANUMCFG
SHOW OLGUANUMCFG|保证通过量配置
消息优先级配置|SET OLMSGPRIORITYCFG
SHOW OLMSGPRIORITYCFG|消息优先级配置
业务优先级配置|SET OLSRVPRIORITYCFG
SHOW OLSRVPRIORITYCFG|业务优先级配置
N2入向业务量配置|ADD OLINPUTN2SRVCFG
SET OLINPUTN2SRVCFG|N2入向业务量配置
DEL OLINPUTN2SRVCFG|N2入向业务量配置
SHOW OLINPUTN2SRVCFG|N2入向业务量配置
SBI入向业务量配置|ADD OLINPUTSBISRVCFG
SET OLINPUTSBISRVCFG|SBI入向业务量配置
DEL OLINPUTSBISRVCFG|SBI入向业务量配置
SHOW OLINPUTSBISRVCFG|SBI入向业务量配置
入向业务总量配置|SET OLTOTALNUMCFG
SHOW OLTOTALNUMCFG|入向业务总量配置
N2出向业务量配置|ADD OLOUTPUTN2SRVCFG
SET OLOUTPUTN2SRVCFG|N2出向业务量配置
DEL OLOUTPUTN2SRVCFG|N2出向业务量配置
SHOW OLOUTPUTN2SRVCFG|N2出向业务量配置
SBI出向业务量配置|ADD OLOUTPUTSBISRVCFG
SET OLOUTPUTSBISRVCFG|SBI出向业务量配置
DEL OLOUTPUTSBISRVCFG|SBI出向业务量配置
SHOW OLOUTPUTSBISRVCFG|SBI出向业务量配置
拥塞与过负荷控制|SET OLTORANBASICCFG
SHOW OLTORANBASICCFG|拥塞与过负荷控制
拥塞与过负荷控制|SET OLTORANCFG
SHOW OLTORANCFG|拥塞与过负荷控制
性能统计
测量类型名称|性能计数器名称
---|---
S1口负荷控制测量|编号为C43300开头的所有计数器
S11/S3/S10/Gn口负荷控制测量|编号为C43301开头的所有计数器
Diameter接口负荷控制测量|编号为C43302开头的所有计数器
SGSN Iu/Gb口过负荷性能统计|编号为C40527开头的所有计数器
SGSN GnGp口过负荷性能统计|编号为C40582开头的所有计数器
SGSN Gr/Gf口过负荷性能统计|编号为C40583开头的所有计数器
SGSN Gd/Gs/Ge口过负荷性能统计|编号为C40584开头的所有计数器
Communication服务负荷控制测量|编号为C51028开头的所有计数器
告警和通知
告警和通知
---
2115633223 MP上报CPU过负荷一级告警
2116681799 MP上报CPU过负荷二级告警
2117730375 MP上报CPU过负荷三级告警
2114584630 业务过负荷告警
3305504772 业务过负荷告警
3306291478 CPU一级过负荷告警
3307340054 CPU二级过负荷告警
3308388630 CPU三级过负荷告警
3309437206 CPU四级过负荷通知
特性配置 : 
摘要配置特性调整特性测试用例常见问题处理 
配置特性 : 
配置说明
过负荷控制功能默认开启，默认参数一般无需改动。可根据实际情况对过负荷控制功能进行修改。 
配置前提
uMAC（AMF/MME/SGSN）网元运行正常。
SGSN/MME配置过程
执行[SET OVERLOAD BASIC PARA]命令，修改过负荷基本配置信息。
[SET OVERLOAD PARA]命令，修改SGSN通用过负荷配置信息。
[SET SERVICE CONTROL]命令，修改SGSN通用业务控制配置信息。
[SET SGSN OFFICE SERVICE MAXIMUM]命令，修改SGSN特定局向业务控制配置信息。
[SET MME OVERLOAD PARA]命令，修改MME过负荷参数配置信息。
[SET MME SERVICE CONTROL]命令，修改MME通用业务控制配置。
AMF配置过程
执行[SET OLCPULEVELCFG]命令，修改CPU负荷等级配置。
执行[SET OVERLOADCFG]命令，修改过负荷控制参数配置。
执行[SET OLGUANUMCFG]命令，修改CPU过负荷业务类型的保证通过量。
执行[SET OLMSGPRIORITYCFG]命令，修改CPU过负荷各消息类型的优先级。
执行[SET OLSRVPRIORITYCFG]命令，修改CPU过负荷各业务类型的优先级。
执行[ADD OLINPUTN2SRVCFG]命令，增加N2入向业务类型的过负荷配置。
执行[SET OLINPUTN2SRVCFG]命令，修改N2入向业务类型的过负荷配置。
执行[DEL OLINPUTN2SRVCFG]命令，删除N2入向业务类型的过负荷配置。
执行[ADD OLINPUTSBISRVCFG]命令，增加SBI入向业务类型的过负荷配置。
执行[SET OLINPUTSBISRVCFG]命令，修改SBI入向业务类型的过负荷配置。
执行[DEL OLINPUTSBISRVCFG]命令，删除SBI入向业务类型的过负荷配置。
执行[SET OLTOTALNUMCFG]命令，修改入向业务总量配置。
执行[ADD OLOUTPUTN2SRVCFG]命令，增加N2出向业务类型的过负荷配置。
执行[SET OLOUTPUTN2SRVCFG]命令，修改N2出向业务类型的过负荷配置。
执行[DEL OLOUTPUTN2SRVCFG]命令，删除N2出向业务类型的过负荷配置。
执行[ADD OLOUTPUTSBISRVCFG]命令，增加SBI出向业务类型的过负荷配置。
执行[SET OLOUTPUTSBISRVCFG]命令，修改SBI出向业务类型的过负荷配置。
执行[DEL OLOUTPUTSBISRVCFG]命令，删除SBI出向业务类型的过负荷配置。
执行[SET OLTORANBASICCFG]命令，修改overload基本配置参数信息。
执行[SET OLTORANCFG]命令，修改overload控制参数配置信息。
配置实例-uMAC设备升级
实例场景
在设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。除了默认开启的CPU拥塞控制来保证系统安全外，还可以单独对某个单项业务控制。CPU拥塞控制参数保持默认即可。这里仅就入向的单项业务控制配置进行举例说明。 
配置脚本
步骤|命令|说明
---|---|---
1|SET OVERLOAD BASIC PARA:CPUENABLE="YES",THRESHOLD=75,HTHRESHOLD=85;|开启CPU拥塞控制，CPU拥塞门限值为75，CPU高拥塞门限值为85。
2|SET OVERLOAD PARA:RNCADJCTRL="YES",OTHERADJCTRL="YES";|开启RNC信令局向拥塞控制，开启其他信令局向拥塞控制。
3|SET SERVICE CONTROL:ATTNUM=17;|配置SGSN每模块每秒最多通过的ATTACH数目为17个。
4|SET SGSN OFFICE SERVICE MAXIMUMADJID=1,HLRAUTHNUM=200,HLRLUNUM=65535;|配置局向号为1的邻接局的业务控制，MP模块每秒到HLR鉴权最大数目改为200，MP模块每秒到HLR位置更新最大数目改为65535
5|SET MME OVERLOAD PARA:S1CTRL="YES",DIAMCTRL="NO",SGSCTRL="YES",LOWLEVEL="NoSending";|配置MME过负荷参数，S1口开启信令拥塞控制，Diameter口关闭拥塞控制，SGs口开启拥塞控制，设置S1口不主动发送overloadstart消息。
6|SET MME SERVICE CONTROL:ATTNUM=17;|配置MME每模块每秒最多通过的ATTACH数目为17个。
配置实例-邻接的HLR/HSS网元处理能力弱
实例场景
由于HLR/HSS是老的网元或未完成扩容，整体处理能力弱。在SGSN/MME业务繁忙时，无法处理位置更新业务，甚至出现了宕机重启的情况。 
配置脚本
命令|说明
---|---
SET SGSN OFFICE SERVICE MAXIMUM:ADJID=1,HLRLUNUM=1000;|配置SGSN到某1号HLR局向，最多每秒1000个位置更新请求。其他配置项按默认配置即可。
AMF配置实例1
场景说明
在设备升级时，一般都需要整局重启。 
在重启后，本局的所有用户都会很快重新附着，导致单位时间内的用户附着数很高。除了默认开启的CPU拥塞控制来保证系统安全外，还可以单独对某个单项业务控制。CPU拥塞控制参数保持默认即可。 
这里仅就N2入向业务控制配置（初始注册与周期性注册）进行举例说明。 
数据规划
配置项|参数|取值
---|---|---
修改OVERLOADCFG配置|是否启用CPU过负荷控制|AMFOLSWITCHON|AMFOLSWITCHON|AMFOLSWITCHON
是否启用业务通过量负荷控制|修改OVERLOADCFG配置|SRVSWITCHON|SRVSWITCHON|SRVSWITCHON
控制周期(100ms)|修改OVERLOADCFG配置|10|10|10
评估周期/控制周期|修改OVERLOADCFG配置|5|5|5
缓冲百分比(%)|修改OVERLOADCFG配置|5|5|5
新增OLINPUTN2SRVCFG配置|业务类型|REGISTRATION|REGISTRATION|REGISTRATION
N2口入向业务每秒每实例最大通过量|新增OLINPUTN2SRVCFG配置|1000|1000|1000
过负荷控制业务权重|新增OLINPUTN2SRVCFG配置|1|1|1
修改OLTOTALNUMCFG配置|每秒每实例N2口入向控制总量|3000|3000|3000
每秒每实例N2口入向控制总量|修改OLTOTALNUMCFG配置|3000|3000|3000
配置步骤
步骤|说明|操作
---|---|---
1|开启CPU过负荷控制与业务通过量负荷控制。|SET OVERLOADCFG:OLSWITCH="AMFOLSWITCHON",SRVSWITCH="SRVSWITCHON",OLCTRLCYCLE=10,JUDGERATIO=5,RECOVBUFF=5
2|开启N2入向业务控制（初始注册和周期性注册），每秒最大通过数为1000。|ADD OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION",OLMAXNUM=1000,OLWEIGHT=1
3|修改入向业务总量配置，即所有入向业务类型相加的每秒通过数，如不修改此项配置，则入向总量不控制。|SET OLTOTALNUMCFG:OLINPUTN2TOTALNUM=3000,OLINPUTSBITOTALNUM=3000
AMF配置实例2
场景说明
AMF在发生系统过负荷（根据过负荷等级判定）的情况下，将启动AMF过负荷控制功能，向gNodeB发送N2 Overload Start消息，对gNodeB输入的话务消息进行一定比例的控制，帮助AMF降低系统处理负荷并恢复正常状态。在系统负荷恢复正常（根据过负荷等级判断确定）后，AMF向gNodeB发送N2 Overload Stop消息，告知gNodeB解除对话务的输入控制，恢复正常处理状态。 
数据规划
配置项|参数|取值
---|---|---
修改N2口基本参数配置|发送overload到RAN侧的周期(100ms)|20
每周期使用的CPU采样量|修改N2口基本参数配置|5
CPU采样周期(s)|修改N2口基本参数配置|1
VRU数据采集周期/CPU采样周期|修改N2口基本参数配置|90
修改RAN侧过载控制配置|是否开启过载控制|OLSWITCHON
N2口消息中是否携带切片信息|修改RAN侧过载控制配置|NSSAISWITCHOFF
N2口发送Overload Start的低过载负荷等级|修改RAN侧过载控制配置|SECONDARYLEVEL
轻微过载下Overload Start消息中Overload Action信元设置|修改RAN侧过载控制配置|REJECTNONEMCONNECT
轻微过载Traffic Load Reduction Indication信元设置|修改RAN侧过载控制配置|10
N2口发送Overload Start的高过载负荷等级|修改RAN侧过载控制配置|PRIMARYLEVEL
严重过载下Overload Start消息中Overload Action信元设置|修改RAN侧过载控制配置|REJECTNONEMCONNECT
严重过载Traffic Load Reduction Indication信元设置|修改RAN侧过载控制配置|20
发送Overload start 的最大gNodeB个数|修改RAN侧过载控制配置|64
配置步骤
步骤|说明|操作
---|---|---
1|修改N2口基本参数配置。|SET OLTORANBASICCFG:OLTORANCYCLE=20,SAMPLENUM=5,SAMPLECYCLE=1,LTMMULTIPLE=90
2|修改RAN侧过载控制配置。|SET OLTORANCFG:OLSWITCH="OLSWITCHON",NSSAISWITCH="NSSAISWITCHON",LOWLEVEL="SECONDARYLEVEL",LOWOLACT="REJECTUPNASCONNECT",LOWOLTLRI=10,HIGHLEVEL="PRIMARYLEVEL",HIGHOLACT="REJECTNONEMCONNECT",HIGHOLTLRI=20,OLGNBNUM=64
调整特性 : 
无 
测试用例 : 
系统异常情况下的功能，非特殊需要，不建议现场进行测试。 
常见问题处理 : 
无 
## ZUF-76-04-008 VNFC支持1+1互备冗余 
概述 : 
VNFC支持1+1互备冗余，是指运行实例采用互备的工作方式。正常情况下，两个实例都工作，均处理业务。当一个运行实例故障，则由另一个运行实例接管业务，从而保证业务正常运行。
uMAC网元采用实例1+1互备工作方式的VNFC为CDU。 
UDSF或CDB运行在CDU上，是基于内存数据库的分布式存储系统，主要存储用户的稳态上下文数据。当处理服务的某个虚机出现异常并被其他虚机接管时，CDB可以恢复用户数据防止会话丢弃。
 说明： 
当vAMF/vMME/vSGSN启用ZUF-76-01-001 支持与UDSF/CDB合一部署
特性时，vAMF/vMME/vSGSN才能支持CDU（UDSF/CDB） 1+1互备。
客户收益 : 
该特性可提升设备可靠性，便于设备监控和升级。 
引入CDU（UDSF/CDB）有以下收益： 
业务流程和用户数据存储分离 
提升系统可靠性 
跨数据中心的数据部署 
实现ISSU 
降低成本 
说明 : 
实例采用1+1互备工作方式时，实例分别运行在不同的资源之上，如：不同的虚机或容器、不同的硬件服务器、以及不同的资源分区（ZONE）。当一个运行实例故障宕机或执行倒换时，另一个运行实例接管业务，保证服务不间断。 
## ZUF-76-04-009 AMF Set-部分备份 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
AMF Set是指UE在其间移动而不需要改变服务AMF的区域。一个AMF Set由多个同质的AMF组成，AMF Set内的AMF为区域内的UE提供服务，共同分担区域内所有UE的业务处理。区域内的gNB与AMF Set内的所有AMF均进行互联。 
同质的AMF，是指这些AMF具有同等能力，比如处理同样的切片、接入同类型的用户等。 
AMF部分容灾备份功能（也称无UDSF部分备份功能）是指：正常工作状态，AMF将用户关键信息同时保存到其备份AMF中。当AMF故障后，用户发起的业务由AMF Set内的其他AMF触发用户重新注册；网络侧NF发起的业务发送给备份AMF后，由备份AMF查询用户关键信息后寻呼用户，并在用户发起业务请求后触发用户重新注册。在用户重新注册后，用户业务恢复正常。 
背景知识 : 
为提高系统可靠性，核心网的业务处理通常需要提供NF冗余机制。在4G时代，通过MME POOL实现了MME的负荷分担以及MME的容灾功能。对于5G时代的AMF，AMF Set实现的功能与4G基本一致，通过AMF Set实现了AMF的负荷分担以及AMF的容灾功能。主要区别如下： 
5G网络中，AMF与5G-RAN之间支持多SCTP偶联，在某条SCTP偶联故障中断后，AMF与5G-RAN之间的话务可以通过其余正常的SCTP偶联继续处理，从而避免了因SCTP偶联断链而造成的用户释放和业务失败。 
5G网络中，AMF将处理的用户上下文状态数据保存到了其备份AMF中。在AMF故障后，可以由备份AMF使用备份的用户上下文状态数据继续处理用户业务，从而获得了比4G网络更好的容灾效果。用户的业务在AMF故障后得以继续处理，从而提高了用户感知和用户体验，为运营商能够提供更优质的网络服务提供了系统实现。但上述方式需要备份整个用户上下文数据，备份量大，对承载网的带宽提出了较高要求。在某些运营商承载网络改造困难较大或其不要求实现业务连续性的情况下，可采用AMF部分备份功能。 
应用场景 : 
在同时满足如下场景时，可以部署AMF部分备份功能。 
网络未部署UDSF。 
网络需要部署AMF容灾功能。 
网络带宽受限，同时无业务连续性要求。 
客户收益 : 
受益方|受益描述
---|---
运营商|提高系统运行可靠性，降低系统运行风险。为用户提供更好的网络服务，获得更高的用户满意度。
移动用户|在网络中AMF发生故障的情况下，用户的业务能够得到快速恢复。
实现原理 : 
系统架构 : 
AMF部分备份功能的网络架构如[图1]所示。该功能由AMF Set内的各AMF，以及gNodeB、NRF、SMF、PCF等共同实现。
图1  网络架构图
涉及的网元 : 
NF名称|NF作用
---|---
AMF|为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息。
AUSF|提供用户鉴权服务。
UDM|提供用户及会话相关的签约信息。在AMF故障后，通过NRF获取到其备份AMF后，将故障AMF服务用户的信令报文发送给其备份AMF，以便触发用户业务恢复流程。
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现、NF状态订阅等功能。在无UDSF场景下，保存备份AMF携带的备份GUAMI信息。在其他NF携带GUAMI执行NF发现流程中，将对应的AMF通过响应消息返回给NF。
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等。在AMF故障后，通过NRF获取到其备份AMF后，将故障AMF服务用户的信令报文发送给其备份AMF，以便触发用户业务恢复流程。对于上述已触发过AMF而未收到AMF更新消息的会话，需要处理会话的超时释放。
PCF|为AMF提供接入及移动性管理等用户策略服务。在AMF故障后，通过NRF获取到其备份AMF后，将故障AMF服务用户的业务报文发送给其备份AMF，以便触发用户业务恢复流程。对于上述已触发过AMF而未收到AMF更新消息的会话，需要处理会话的超时释放。
NSSF|为AMF提供切片选择服务。
gNodeB|UE接入时，提供无线资源及承载。实现AMF选择功能，即根据UE提供的信息选择UE当前服务的AMF。在UE没有提供服务AMF信息，或服务AMF不可用时，根据AMF Set内各AMF的权重因子，选择AMF。
协议栈 : 
该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
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
Nnrf|ZUF-79-19-010 Nnrf
本网元实现 : 
AMF向gNodeB下发本AMF的Served GUAMI和权重因子。 
根据维护需要，AMF发起负荷重平衡过程。 
AMF将用户关键信息同步到为其备份的AMF。 
备份AMF需要保存用户关键信息，用于故障后被叫业务恢复流程。 
备份AMF将其作为备份的GUAMI通过NF注册流程携带给NRF。 
业务流程 : 
AMF部分备份（也称无UDSF部分备份）
AMF部分备份（也称无UDSF部分备份）原理如[图2]所示。AMF Set内的AMF相互指定备份关系，用于用户关键信息（如SUPI/TAList/5G-GUTI）的备份。
如下图所示，AMF1备份到AMF2，AMF2备份到AMF3，AMF3备份到AMF1。 
图2  AMF部分备份原理图
当某个AMF故障时，如AMF1故障，此时用户发起的业务由gNodeB选择AMF Set内的其他AMF进行处理，选择的AMF接收用户业务消息后，查询用户上下文数据失败，则触发用户重注册。 
此时SMF或PCF发起的业务由SMF或PCF选择备份AMF进行处理，备份AMF接收业务消息后，查询用户上下文数据失败，再次查询用户备份数据并触发寻呼用户，用户接收寻呼消息后发起业务请求的流程同上述用户发起的业务。 
用户重新进行注册后，业务恢复正常。 
AMF状态订阅及故障检测
图3  状态订阅及故障检测
流程说明： 
原AMF（为与备份AMF区分，称为原AMF）投入服务后，向NRF发起NF注册，携带GUAMI List。 
备份AMF（即步骤1中原AMF的备份AMF）启动后，向NRF发起NF注册，携带GUAMI List，同时携带backupInfoAmfFailure及backupInfoAmfRemoval参数，此参数具体取值为原AMF的GUAMI，用于指示备份AMF将作为原AMF的备份。 
备份AMF向NRF发起AMF状态订阅，对原AMF的状态变更进行订阅，以便在原AMF维护或故障后获得通知。 
原AMF在发送给gNodeB的NG SETUP RESPONSE消息中携带GUAMI List，此处不再携带Backup AMF Name，上行流程可以任选Set内AMF执行业务恢复。 
原AMF相邻的其他NF如SMF、PCF等向NRF发起AMF状态订阅，其他NF对有业务交互的AMF的状态变更进行订阅，以便在AMF维护或故障后获得通知。 
原AMF在正常工作状态，需要周期性向NRF发送更新消息，实现NF与NRF之间的Heartbeat保活机制，以便NRF识别AMF故障。 
某时刻原AMF故障，无法响应gNodeB发送的请求消息。 
某时刻原AMF故障，无法正常向NRF发送Heartbeat保活机制的更新消息。 
gNodeB和NRF判定原AMF故障。 
NRF向订阅了原AMF状态的其他AMF如备份AMF发送状态变更通知消息，其他AMF如备份AMF获知原AMF故障。 
NRF向订阅了原AMF状态的其他NF发送状态变更通知消息，其他NF获知原AMF故障。 
RAN主动发起的业务流程
图4  RAN主动发起的业务流程
流程说明： 
为AMF1（原AMF）配置备份的AMF2（备份AMF）。原AMF1将Served GUAMI下发给gNodeB。 
备份AMF2通过NF注册流程将其备份的GUAMI保存到NRF中，供其他NF获取。 
用户接入网络并进行业务流程处理。 
AMF1在业务处理流程中，将用户关键信息同步到为其备份的AMF2中（AMF1和AMF2中均配置独占的UDSF服务）。备份AMF2保存同步数据。 
某时刻，AMF1发生故障。UE发起业务，gNodeB发送消息无响应，gNodeB识别AMF1故障。 
gNodeB识别AMF1故障后，将用户的请求消息发送给此AMF Set内的其他AMF，如AMF2。 
AMF2接收用户请求后，无法正常获取用户上下文数据，按3GPP规范要求触发用户重注册。 
后续此UE执行注册流程，AMF正常处理，业务恢复。 
CPNF主动发起的业务流程
图5  CPNF主动发起的业务流程
流程说明： 
各AMF在正常业务处理流程中，其中UE1用户的业务由AMF1处理。 
业务流程处理完毕，AMF1将用户关键信息同步到为其备份AMF2中（AMF1和AMF2中均配置独占的UDSF服务，UDSF服务提供上下文数据存储的功能）。备份AMF2保存同步数据。 
某时刻，AMF1发生故障，无法正常向NRF发送Heartbeat保活机制的更新消息，NRF识别并判定AMF1故障。NRF向订阅了原AMF状态的备份AMF即AMF2以及其他NF如SMF、PCF等发送状态变更通知消息，备份AMF即AMF2以及SMF等获知原AMF故障。 
（可选）在其他NF如SMF、PCF等本地没有备份AMF信息的情况下，向NRF执行AMF发现流程，用于获取原AMF的备份AMF信息。 
其他NF如SMF、PCF等在需要主动发起业务流程的情况下，选择故障AMF1（即原AMF）的备份AMF即AMF2。 
其他NF如SMF将业务消息发送给备份AMF即AMF2。 
备份AMF即AMF2查询用户上下文失败，查询用户备份数据。 
备份AMF即AMF2使用用户备份数据寻呼用户。 
UE接收寻呼后，发起业务请求。 
AMF2接收用户请求后，无法正常获取用户上下文数据，按3GPP规范要求触发用户重注册。 
后续此UE执行注册流程，AMF正常处理，业务恢复。 
AMF计划性移除/维护处理流程
图6  AMF计划性移除/维护处理流程
流程说明： 
某时刻，需要执行退服维护，如AMF升级、改造等场景。 
根据不同的退服方式，选择执行如下操作。 
如果采用逐步退服的方式，即逐步将指定GUAMI的用户及业务迁移到备份AMF，则向NRF发送NF更新消息，将即将不可用的GUAMI从profile中移除。 
如果采用一次性退服的方式，即将全部GUAMI的用户及业务一次性全部迁移到备份AMF，则向NRF发送去注册消息。 
退服的AMF向gNodeB发送AMF STATUS INDICATION消息，携带不可用的GUAMI List，用于指示不可用GUAMI的业务需要gNodeB选择备份AMF继续处理。 
NRF接收退服AMF的更新或去注册消息后，根据具体的消息类型，向订阅了此AMF状态的备份AMF发送状态变更通知。 
NRF接收退服AMF的更新或去注册消息后，根据具体的消息类型，向订阅了此AMF状态的其他NF如SMF、PCF、UDM等发送状态变更通知。 
后续gNodeB及其他NF如SMF、PCF等将选择备份AMF发送消息，根据不同场景分为三个处理流程，最终完成用户在新AMF接入。 
对于用户发起的注册消息，AMF2获取5G-GUTI后按局间流程从原AMF（即AMF1）获取上下文并继续处理完成注册。 
除注册外的其他用户消息如业务请求，AMF2接收后无法获取上下文，触发用户重注册，用户注册后迁移到其他AMF。 
对于SMF、PCF发起的下行流程，AMF2接收后，根据备份数据寻呼用户，后续流程与b流程处理一致。 
AMF恢复流程
图7  AMF故障后恢复流程
流程说明： 
AMF故障后恢复或维护完成，投入服务。 
AMF向NRF发起NF注册，携带GUAMI List。 
NRF识别AMF恢复可用，NRF向订阅了此AMF状态的备份AMF发送状态变更通知消息，备份AMF获知原AMF恢复为可用。 
NRF向订阅了此AMF状态的其他NF如SMF、PCF等发送状态变更通知消息，其他NF如SMF等获知原AMF恢复为可用。 
AMF向gNodeB发送NG SETUP RESPONSE或AMF CONFIGURATION UPDATE消息，携带GUAMI List及权重因子参数，通知gNodeB其投入服务。 
gNodeB，备份AMF，以及恢复AMF相邻的其他NF均识别AMF恢复为可用，后续与此AMF相关的业务（未发生迁移的用户及会话）恢复与此AMF交互。 
gNodeB接收到原AMF承担用户的业务消息，将其正常发送给恢复的AMF；其他NF需要处理原AMF承担用户的业务消息，将其发送给恢复的AMF。AMF尝试向其备份AMF获取用户关键信息后寻呼用户。 
恢复的AMF由于无用户上下文数据，按异常流程触发用户重新注册，恢复业务处理。 
系统影响 : 
AMF Set容灾功能在开通时，需要配置冗余容量用于AMF故障后的话务接管处理。冗余度参照运行商具体要求和配置指导要求执行。 
对于本功能，AMF需要向备份AMF同步用户关键信息用于故障后的业务恢复，在话务模型与处理能力估算时需要考虑这部分消耗。  
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.21.2 AMF Management5.21.2.1 AMF Addition/Update5.21.2.2 AMF planned removal procedure5.21.2.3 Procedure for AMF Auto-recovery
3GPP TS 38.413（NG Application Protocol ）|8.7.1 NG Setup8.7.6 AMF Status Indication9.2.6.2 NG SETUP RESPONSE9.2.6.10 AMF STATUS INDICATION
特性能力 : 
名称|指标
---|---
AMF Set中最大支持AMF个数|64个（按规范规定，Set内AMF的唯一标识AMF Pointer为6 bits）。
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布
License要求 : 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“AMF支持无UDSF容灾部分备份功能”。
对其他网元的要求 : 
UE|gNodeB|NRF|SMF|PCF|UDM
---|---|---|---|---|---
-|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
启用本特性前，需要根据运营商冗余容量的具体要求，配置冗余容量。 
O&M相关 : 
命令 : 
配置项配置项命令容灾策略配置SET DISASTERRECOVERYPOLICYSHOW DISASTERRECOVERYPOLICY容灾开关SET DISASTERSWITCHPARASHOW DISASTERSWITCHPARAAMF资源标识SET AMFNRISHOW AMFNRINotify IP配置ADD NOTIFYIPSET NOTIFYIPDEL NOTIFYIPSHOW NOTIFYIPSet内其他AMF配置ADD OTHERAMFCFGSET OTHERAMFCFGDEL OTHERAMFCFGSHOW OTHERAMFCFG备份AMF配置ADD BACKUPAMFSET BACKUPAMFDEL BACKUPAMFSHOW BACKUPAMF接管AMF配置ADD TAKEOVERAMFSET TAKEOVERAMFDEL TAKEOVERAMFSHOW TAKEOVERAMF控制策略配置SET CONTROLPOLICYSHOW CONTROLPOLICY控制参数配置SET CONTROLPARASHOW CONTROLPARA 
动态管理配置项命令备份数据清除CLEAR BACKUPDATA备份数据查询SHOW BACKUPDATA 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
通过配置以下内容来实现本特性功能。 
AMF容灾配置，包括：容灾策略配置容灾开关配置AMF资源标识配置Notify IP配置Set内其他AMF配置 
Set内其他AMF配置，包括：备份AMF配置接管AMF配置 
部分备份配置，包括：控制策略配置控制参数配置 
配置前提 : 
AMF Pool环境就绪，环境中部署了至少两套AMF（AMF1和AMF2），一套NRF。 
NRF支持NF注册、订阅以及通知流程。 
AMF、SMF等已经在NRF上完成注册、订阅操作。 
EM网管能正常连接并登录。 
配置过程 : 
执行[ADD GUAMICFG]命令，设置可接管局AMF的GUAMI信息。
执行[SET DISASTERRECOVERYPOLICY]命令，设置容灾策略为无UDSF部分备份。
执行[SET DISASTERSWITCHPARA]命令，设置支持容灾功能。
执行[ADD AMFNRI]命令，设置可接管局AMF的资源标识。
执行[ADD OTHERAMFCFG]命令，设置本局可接管GUAMI对应的AMF的地址信息。
执行[ADD BACKUPAMF]命令，设置本局GUAMI对应的备份AMF。
执行[ADD TAKEOVERAMF]命令，设置本局AMF可接管的GUAMI。
执行[SET CONTROLPOLICY]命令，设置部分备份的控制策略。
执行[SET CONTROLPARA]命令，设置部分备份传递备份信息的控制参数。
配置实例 : 
场景说明 : 
无UDSF的部分数据备份。网络需要部署AMF容灾功能，但是无UDSF部署，且带宽受限，同时无业务连续性要求。 
数据规划 : 
主用局
配置名称|参数项|取值
---|---|---
AMF本局配置|AMF名称|amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
GUAMI池配置|GUAMI标识|本局：1他局：2
Point标识|GUAMI池配置|本局：11他局：22
本局GUAMI配置|GUAMI标识|1
容灾策略|容灾策略配置|无UDSF部分备份
容灾开关|是否支持容灾功能|是
AMF资源标识|AMF名称|本局：amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org他局：amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
AMF资源标识|AMF资源标识|本局：1他局：2
Set内其他AMF配置|Pointer标识|22
IP地址|Set内其他AMF配置|192.168.1.2
端口号|Set内其他AMF配置|8080
URI Schema|Set内其他AMF配置|HTTP
API版本|Set内其他AMF配置|V1
备份AMF配置|GUAMI标识|1
AMF名称|备份AMF配置|amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
接管AMF配置|Backup GUAMI标识|2
主用AMF名称|接管AMF配置|amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
控制参数配置|备份AMF的GTPC地址|192.168.1.2
备份数据消息发送频率（毫秒）|控制参数配置|1000
备份数据消息打包大小（KB）|控制参数配置|4
老化时长（分钟）|控制参数配置|120
备份局
配置名称|参数项|取值
---|---|---
AMF本局配置|AMF名称|amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
GUAMI池配置|GUAMI标识|本局：2他局：1
Point标识|GUAMI池配置|本局：22他局：11
本局GUAMI配置|GUAMI标识|2
容灾策略|容灾策略配置|无UDSF部分备份
容灾开关|是否支持容灾功能|是
AMF资源标识|AMF名称|本局：amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org他局：amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
AMF资源标识|AMF资源标识|本局：2他局：1
Set内其他AMF配置|Pointer标识|11
IP地址|Set内其他AMF配置|192.168.1.1
端口号|Set内其他AMF配置|8080
URI Schema|Set内其他AMF配置|HTTP
API版本|Set内其他AMF配置|V1
备份AMF配置|GUAMI标识|2
AMF名称|备份AMF配置|amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
接管AMF配置|Backup GUAMI标识|1
主用AMF名称|接管AMF配置|amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org
控制参数配置|备份AMF的GTPC地址|192.168.1.1
备份数据消息发送频率（毫秒）|控制参数配置|1000
备份数据消息打包大小（KB）|控制参数配置|4
老化时长（分钟）|控制参数配置|120
配置步骤 : 
主用局
序号|步骤|命令实例
---|---|---
1|配置他局GUAMI。|ADD GUAMICFG:ADD GUAMICFG:GUAMIID=2,MCC="460",MNC="22",REGIONID=22,SETID=22,POINTID=22需要确保本局GUAMI配置正确：GUAMIID=1,MCC="460",MNC="11",REGIONID=11,SETID=11,POINTID=11
2|配置容灾策略。|SET DISASTERRECOVERYPOLICY:DISASTERPOLICY="WITHOUT_UDSF_PARTIAL"
3|配置容灾开关。|SET DISASTERSWITCHPARA:SUPPORTDISASTER="YES"
4|配置他局AMF资源标识。|ADD AMFNRI:AMFNAME="amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org",AMFNRI=2需要确保本局AMF资源标识配置正确：AMFNAME="amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org",AMFNRI=1
5|配置Set内其他AMF。|ADD OTHERAMFCFG:POINTERID=22,IPADDRESS=192.168.1.2,PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
6|配置备份AMF。|ADD BACKUPAMF:GUAMIID=1,AMFNAME="amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org"
7|配置接管AMF。|ADD TAKEOVERAMF:BACKUPGUAMI=2,MASTERAMFNAME="amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org"
8|配置控制参数。|SET CONTROLPARA:BACKAMFIP="192.168.1.2",BACKRATE=1000,BACKSIZE=4,AGINGTIME=120
备份局
序号|步骤|命令实例
---|---|---
1|配置他局GUAMI。|ADD GUAMICFG:ADD GUAMICFG:GUAMIID=1,MCC="460",MNC="11",REGIONID=11,SETID=11,POINTID=11需要确保本局GUAMI配置正确：GUAMIID=2,MCC="460",MNC="22",REGIONID=22,SETID=22,POINTID=22
2|配置容灾策略。|SET DISASTERRECOVERYPOLICY:DISASTERPOLICY="WITHOUT_UDSF_PARTIAL"
3|配置容灾开关。|SET DISASTERSWITCHPARA:SUPPORTDISASTER="YES"
4|配置他局AMF资源标识。|ADD AMFNRI:AMFNAME="amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org",AMFNRI=1需要确保本局AMF资源标识配置正确：AMFNAME="amf2.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org",AMFNRI=2
5|配置Set内其他AMF。|ADD OTHERAMFCFG:POINTERID=11,IPADDRESS=192.168.1.1,PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
6|配置备份AMF。|ADD BACKUPAMF:GUAMIID=2,AMFNAME="amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org"
7|配置接管AMF。|ADD TAKEOVERAMF:BACKUPGUAMI=1,MASTERAMFNAME="amf1.cluster1.net1.amf.5gc.mnc012.mcc345.3gppnetwork.org"
8|配置控制参数。|SET CONTROLPARA:BACKAMFIP="192.168.1.1",BACKRATE=1000,BACKSIZE=4,AGINGTIME=120
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|Pool内AMF之间能够备份在线用户信息
---|---
测试目的|验证Pool内AMF之间能够备份在线用户信息
预置条件|AMF Pool环境就绪，环境中部署了至少两套AMF（AMF1和AMF2），一套NRF。NRF支持NF注册、订阅以及通知流程。AMF、SMF等已经在NRF上完成注册、订阅操作。在各个逻辑网元上建立接口信令跟踪和用户信令跟踪。
测试过程|UE在AMF1上注册成功。在AMF2查询用户的备份信息。
通过准则|通过动态命令SHOW BACKUPDATA，可以查询到用户的GUTI、TA list信息。
测试结果|–
常见问题处理 : 
无。 
## ZUF-76-04-010 AMF Set-语音用户数据备份 
概述 : 
AMF Set下的多个AMF实例并行服务于一组RAN所覆盖的无线区域。区域内的用户可以访问AMF Set下的任意AMF实例。 
客户收益 : 
每个AMF承载一些用户。当一个AMF发生故障时，用户可以访问AMF Set内的其他AMF，以保证网络的可靠性。 
说明 : 
AMF Set下多个AMF Instance并行地共同服务于一组RAN所覆盖的无线区域，该区域内用户可以接入AMF Set下的任一AMF instance。如果某个地域发生灾难，其 他AMF不能正常工作了，RAN会把用户路由到其他区域的AMF。 
AMF Set中UDSF采用非共享模式部署时，为每个AMF部署独占的UDSF。AMF间通过自定义接口实现跨网元数据备份，AMF故障后由备份AMF接管业务。
AMF间备份用户的上下文信息，AMF可同时支持语音容灾和数据容灾。 
## ZUF-76-04-011 AMF Set-全量备份 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
AMF全量容灾备份，是指AMF Set组网方式下，主用AMF将用户全量数据备份存储到备用AMF。当主用AMF发生故障时，备用AMF可以使用全量备份的用户上下文信息继续处理用户业务，用户无需重新注册即可恢复业务，保障了用户数据业务和语音业务的连续性，同时减轻了对网络的信令冲击。
背景知识 : 
为提高系统可靠性，核心网的业务处理通常需要提供NF冗余机制。
对于4G时代的MME，通过MME POOL实现了MME的负荷分担以及MME的容灾功能。 
对于5G时代的AMF，通过AMF Set机制实现了AMF的负荷分担以及AMF的容灾功能，与4G的MME POOL功能基本一致。AMF Set下多个AMF并行地共同服务于一组RAN所覆盖的无线区域，该区域内用户可以接入AMF Set下的任一AMF。如果某个AMF发生故障，UE选择Set内其他AMF重新注册接入后，即可重新使用业务。 
在AMF Set组网下，AMF还可以进一步支持用户数据全量备份，将用户上下文信息完整传输保存到其备份AMF中。 
术语 : 
术语|含义
---|---
AMF Set|一个AMF Set由多个为相同区域和网络切片提供服务的AMF组成。AMF Set内的AMF为区域内的UE提供服务，共同分担区域内所有UE的业务处理。UE在AMF Set所服务的区域间移动不需要改变服务AMF。
AMF Region|一个AMF Region由一个或多个AMF Set组成。
AMF Pointer|用于区分AMF Set内的不同AMF的标识。按协议规定，AMF Set内的唯一标识AMF Pointer为6 bits。
GUAMI|Globally Unique AMF ID的缩写，全局唯一的AMF标识，GUAMI由MCC、MNC、AMF Region ID、AMF Set ID以及AMF Pointer共同标识，即<GUAMI> = <MCC> <MNC> <AMF Region ID> <AMF Set ID> <AMF Pointer>。
应用场景 : 
当网络未部署外置共享UDSF网元，而网络又需要支持AMF容灾功能，并提供业务连续性需求时，需要开启AMF全量容灾备份功能。 
客户收益 : 
受益方|受益描述
---|---
运营商|提高系统运行可靠性，降低系统运行风险。为用户提供更好的网络服务。
移动用户|提高了用户体验。
实现原理 : 
系统架构 : 
AMF全量容灾备份功能网络架构如[图1]所示，功能由AMF Set内的各AMF、以及gNodeB、NRF、SMF、PCF等共同实现。
图1  AMF全量容灾备份功能网络架构
###### 涉及的NF 
NF名称|NF作用
---|---
AUSF|提供用户鉴权服务。
UDM|提供用户及会话相关的签约信息。AMF故障后，通过本地保存信息或NRF获取到其备份AMF，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
NRF|网络功能数据仓储功能，为AMF提供注册功能，并实现NF发现、NF状态订阅及通知等功能。接收NF注册和状态订阅请求并处理，在AMF状态变更情况下，向订阅者发送AMF状态变更通知。保存备份AMF携带的备份GUAMI信息。在其他NF携带GUAMI执行NF发现流程中，将对应的AMF或备份AMF通过响应消息返回给NF。
SMF|提供用户会话相关服务，如分配UE IP地址，指示UPF建立会话用户面资源等操作。AMF故障后，通过本地保存信息或NRF获取到其备份AMF，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
PCF|为AMF提供接入及移动性管理等用户策略服务。AMF故障后，通过本地保存信息或NRF获取到其备份AMF，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
NSSF|为AMF提供切片选择服务。
SMSF|提供短消息服务。AMF故障后，通过本地保存信息或NRF获取到其备份AMF，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
GMLC|提供定位服务。AMF故障后，通过本地保存信息或NRF获取到其备份AMF，将故障AMF服务用户的业务报文发送给其备份AMF，并继续处理业务流程。
gNodeB|UE接入时，提供无线资源及承载。实现AMF选择功能，即根据UE提供的信息选择UE当前服务的AMF。在UE没有提供服务AMF信息，或服务AMF不可用时，根据AMF Set内各AMF的权重因子，选择AMF。在服务AMF不可用且存在备份AMF信息时，选择备份AMF发送消息。
协议栈 : 
该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
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
N20|ZUF-79-19-012 N20
NL2|ZUF-79-19-014 NL2/NLg
Nnrf|ZUF-79-19-010 Nnrf
NF实现 : 
AMF主要实现以下功能： 
为UE接入提供移动性管理功能，为UE的会话流程选择SMF并传递会话相关消息。 
向gNodeB下发本AMF的Served GUAMI、备份AMF信息、以及权重因子。 
将用户上下文状态数据转发备份到为其备份的AMF上。 
备份AMF将其作为备份的GUAMI通过NF注册流程携带给NRF。 
AMF全量容灾备份原理如[图2]所示。AMF Set内的AMF相互指定上下文备份关系：AMF1备份到AMF2、AMF2备份到AMF1、AMF3备份到AMF4、AMF4备份到AMF3。当某个AMF故障时，如AMF1故障，则其承担用户的业务将由gNodeB发送给其备份的AMF（即AMF2）继续处理，下行消息由SMF/UDM等网元送到备份的AMF（即AMF2）处理。
图2  AMF全量容灾备份原理
业务流程 : 
AMF状态订阅及故障检测
AMF状态订阅及故障检测的流程如[图3]所示。
图3  AMF状态订阅及故障检测流程
流程说明： 
主AMF（即AMF1）启动后，向NRF发起NF注册，携带GUAMI List。 
备份AMF（即AMF2）启动后，向NRF发起NF注册，携带GUAMI List，同时携带BackupInfoAMFFailure及BackupInfoAMFRemoval参数，此参数具体取值为主AMF的GUAMI，用于指示备份AMF将作为主AMF的备份。 
备份AMF向NRF发起AMF状态订阅，对主AMF的状态变更进行订阅，以便在主AMF维护或故障后获得通知。 
主AMF在发送给gNodeB的NG Setup Response消息中携带GUAMI List及GUAMI对应的Backup AMF Name，用于指示gNodeB其GUAMI对应的备份AMF信息。 
主AMF相邻的其他NF，如SMF、PCF等向NRF发起AMF状态订阅，对与自身有业务交互的AMF进行状态变更订阅，以便在AMF维护或故障后获得通知。 
主AMF在正常工作状态，需要周期性向NRF发送更新消息，实现AMF与NRF之间的Heartbeat保活机制，以便NRF识别AMF故障。 
某时刻主AMF故障，无法响应gNodeB发送的请求消息。 
某时刻主AMF故障，无法正常向NRF发送Heartbeat保活机制的更新消息。 
gNodeB和NRF判定主AMF故障。 
NRF向订阅了主AMF状态的其他AMF（如备份AMF）发送状态变更通知消息，其他AMF（如备份AMF）获知主AMF故障。 
NRF向订阅了主AMF状态的其他NF发送状态变更通知消息，其他NF获知主AMF故障。 
RAN主动发起的业务流程
RAN主动发起的业务流程如[图4]所示。
图4  RAN主动发起的业务流程
流程说明： 
为主AMF（即AMF1）配置备份AMF（即AMF2）。主AMF将Served GUAMI以及Backup AMF Name信息下发给gNodeB。 
备份AMF通过NF注册流程将其备份的GUAMI保存到NRF中，供其他NF获取。 
用户接入网络并进行业务流程处理。 
主AMF在业务处理流程中，将用户上下文状态数据同步到为其备份AMF中。主AMF和备份AMF中均配置独占的UDSF服务，UDSF服务提供上下文数据存储的功能。备份AMF保存同步数据。
某时刻，主AMF发生故障。UE发起业务gNodeB发送消息无响应。 
gNodeB识别并判定主AMF故障。 
gNodeB判定主AMF故障后，将用户的请求消息发送给主AMF的备份AMF，即AMF2。 
备份AMF接收用户请求后，判断用户为主AMF所处理，备份AMF从保存数据中获取用户上下文状态数据，并继续处理此用户的相关业务流程。备份AMF为用户重新分配5G-GUTI，向gNodeB发送更新5G-GUTI及 AMF UE NGAP ID的消息，后续此用户在备份AMF进行处理。 
备份AMF与其他NF交互，继续处理此用户业务流程，其他NF接收消息后，识别主AMF故障，后续与备份AMF交互处理此用户相关业务流程。 
后续此UE的业务将在备份AMF正常处理。 
NF主动发起的业务流程
NF主动发起的业务流程如[图5]所示。
图5  NF主动发起的业务流程
流程说明： 
各AMF在正常业务处理流程中，其中UE1用户的业务由主AMF（即AMF1）处理。 
业务流程处理完毕，主AMF将用户上下文状态数据同步到为其备份AMF中。主AMF和备份AMF中均配置独占的UDSF服务，UDSF服务提供上下文数据存储的功能。备份AMF保存同步数据。 
某时刻，主AMF发生故障，无法正常向NRF发送Heartbeat保活机制的更新消息，NRF识别并判定主AMF故障。NRF向订阅了主AMF状态的备份AMF（即AMF2）以及其他NF（如SMF、PCF等）发送状态变更通知消息，备份AMF以及SMF等获知主AMF故障。 
（可选）在其他NF如SMF，PCF等本地没有备份AMF信息的情况下，向NRF执行AMF发现流程，用于获取主AMF的备份AMF信息。 
其他NF（如SMF、PCF等）在需要主动发起业务流程的情况下，选择故障AMF（即主AMF）的备份AMF。 
其他NF将业务消息发送给备份AMF。 
备份AMF接收业务消息后，判断用户（例如UE1）原为AMF所处理。备份AMF从保存的数据中获取UE1的用户上下文状态数据，并继续处理此用户的相关业务流程。备份AMF为用户重新分配5G-GUTI，向gNodeB发送消息更新5G-GUTI及AMF UE NGAP ID的消息，后续此用户在备份AMF进行处理。 
备份AMF与其他NF（如PCF）交互，继续处理此用户业务流程。其他NF接收消息后，识别为主AMF故障，后续与备份AMF交互处理此用户相关业务流程。 
备份AMF与其他NF（如UDM）交互，通知备份AMF成为此用户的服务AMF，UDM保存相关信息，后续与备份AMF交互处理此用户相关业务流程。 
后续UE1的业务在备份AMF进行处理。 
AMF计划性移除或维护处理流程
AMF计划性移除或维护处理的流程如[图6]所示。
图6  AMF计划性移除或AMF计划性移除或维护处理流程
流程说明： 
主AMF（即AMF1）启动后，在发送给gNodeB的NG Setup Response消息中携带GUAMI List及GUAMI对应的Backup AMF Name，把备份AMF（即AMF2）信息传递给gNodeB。 
某时刻，需要对主AMF进行维护（计划性移除或负荷重平衡），如主AMF升级、改造，或负荷重平衡等场景。 
根据具体的维护目的执行如下流程。 
对于负荷重平衡操作，主AMF向NRF发送NF更新消息，将即将不可用的GUAMI从profile中移除。 
对于计划性移除操作，主AMF向NRF发送去注册消息。 
备份AMF向gNodeB发送AMF Status Indication消息，携带不可用的GUAMI List，用于指示不可用GUAMI的业务需要gNodeB选择备份AMF继续处理。 
NRF接收维护AMF的更新或去注册消息后，根据具体的消息类型，向订阅了此AMF状态的备份AMF发送状态变更通知。 
NRF接收维护AMF的更新或去注册消息后，根据具体的消息类型，向订阅了此AMF状态的其他NF（如SMF、PCF、UDM等）发送状态变更通知。 
后续gNodeB及其他NF将选择备份AMF继续执行相关用户的业务流程。 
系统影响 : 
AMF全量容灾备份功能在开通时，需要配置备份AMF的冗余容量，用于AMF故障后的话务接管处理。在话务模型估算时需要考虑这部分消耗。 
对于用户上下文数据的备份，AMF需要与备份AMF进行交互并备份用户上下文状态数据。在处理能力估算时需要考虑这部分消耗。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称|章节
---|---
3GPP TS 23.501（System Architecture for the 5G System）|5.21.2 AMF Management5.21.2.1 AMF Addition/Update5.21.2.2 AMF planned removal procedure5.21.2.3 Procedure for AMF Auto-recovery
3GPP TS 38.413（NG Application Protocol ）|8.7.1 NG Setup8.7.6 AMF Status Indication9.2.6.2 NG SETUP RESPONSE9.2.6.10 AMF STATUS INDICATION
特性能力 : 
名称|指标
---|---
AMF Set中支持最大AMF个数|64（个）
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.22.20|首次发布
License要求 : 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
对应的License项目为： 
“AMF支持无UDSF全量容灾”（license ID：uMAC_AMF_7255），此项目显示为“打开”，表示AMF支持无UDSF全量容灾备份。 
“AMF支持无UDSF容灾部分备份功能”（license ID：uMAC_AMF_7223），此项目显示为“打开”，表示AMF支持无UDSF部分容灾备份。 
对其他网元的要求 : 
UE|eNodeB|NRF|SMF|PCF|UDM|SMSF|GMLC
---|---|---|---|---|---|---|---
-|√|√|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
启用本特性前，需要根据运营商冗余容量的具体要求，配置冗余容量。 
O&M相关 : 
命令 : 
配置项|命令
---|---
GUAMI池配置|ADD GUAMICFG
SET GUAMICFG|GUAMI池配置
DEL GUAMICFG|GUAMI池配置
SHOW GUAMICFG|GUAMI池配置
容灾策略配置|SET DISASTERRECOVERYPOLICY
SHOW DISASTERRECOVERYPOLICY|容灾策略配置
容灾开关配置|SET DISASTERSWITCHPARA
SHOW DISASTERSWITCHPARA|容灾开关配置
AMF资源标识|ADD AMFNRI
SET AMFNRI|AMF资源标识
DEL AMFNRI|AMF资源标识
SHOW AMFNRI|AMF资源标识
Notify IP配置|ADD NOTIFYIP
SET NOTIFYIP|Notify IP配置
DEL NOTIFYIP|Notify IP配置
SHOW NOTIFYIP|Notify IP配置
Set内其他AMF配置|ADD OTHERAMFCFG
SET OTHERAMFCFG|Set内其他AMF配置
DEL OTHERAMFCFG|Set内其他AMF配置
SHOW OTHERAMFCFG|Set内其他AMF配置
备份AMF配置|ADD BACKUPAMF
SET BACKUPAMF|备份AMF配置
DEL BACKUPAMF|备份AMF配置
SHOW BACKUPAMF|备份AMF配置
接管AMF配置|ADD TAKEOVERAMF
SET TAKEOVERAMF|接管AMF配置
DEL TAKEOVERAMF|接管AMF配置
SHOW TAKEOVERAMF|接管AMF配置
控制策略配置|SET CONTROLPOLICY
SHOW CONTROLPOLICY|控制策略配置
控制参数配置|SET CONTROLPARA
SHOW CONTROLPARA|控制参数配置
NF标识配置|ADD NFCFG
SET NFCFG|NF标识配置
DEL NFCFG|NF标识配置
SHOW NFCFG|NF标识配置
CGW互联配置|ADD CGWNODE
SET CGWNODE|CGW互联配置
DEL CGWNODE|CGW互联配置
SHOW CGWNODE|CGW互联配置
租户配置|ADD CDBTENANT
SET CDBTENANT|租户配置
DEL CDBTENANT|租户配置
SHOW CDBTENANT|租户配置
参数配置|ADD CDBPARAM
SET CDBPARAM|参数配置
DEL CDBPARAM|参数配置
SHOW CDBPARAM|参数配置
过负荷配置|ADD CDBLOADLV
SET CDBLOADLV|过负荷配置
DEL CDBLOADLV|过负荷配置
SHOW CDBLOADLV|过负荷配置
内存库告警阈值配置|ADD CDBMEMALARMLV
SET CDBMEMALARMLV|内存库告警阈值配置
DEL CDBMEMALARMLV|内存库告警阈值配置
SHOW CDBMEMALARMLV|内存库告警阈值配置
数据区告警阈值配置|ADD CDBBUFFLV
SET CDBBUFFLV|数据区告警阈值配置
DEL CDBBUFFLV|数据区告警阈值配置
SHOW CDBBUFFLV|数据区告警阈值配置
CDU数据一致性功能配置|SET CDUDATACHECK
SHOW CDUDATACHECK|CDU数据一致性功能配置
性能统计 : 
性能计数器名称
---
C510230001	上行容灾消息请求次数
C510230002 下行容灾消息请求次数
C510230003 接管成功次数
C510230004 部分备份触发寻呼请求次数
C510230005 部分备份触发寻呼成功次数
C510230006 部分备份触发寻呼失败次数
C510230007 上行全量容灾消息请求次数
C510230008 下行全量容灾消息请求次数
C510230009 平滑通知周边网元消息发送次数
C510230010 平滑通知周边网元消息丢弃次数
告警和通知 : 
该特性不涉及告警/通知消息。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
通过该配置过程可以完成AMF全量备份功能，达到主用局AMF和备份局AMF上的用户相互业务接管无损的目的。 
配置前提 : 
AMF Pool环境就绪，环境中部署了至少主备两套AMF（AMF1和AMF2）并内置UDSF，以及一套NRF。 
AMF以及其周边NF已经在NRF上完成注册、订阅操作。 
“AMF支持无UDSF全量容灾”和“AMF支持无UDSF容灾部分备份功能”的License项已打开。 
配置过程 : 
###### 全新配置全量备份 
执行[ADD GUAMICFG]命令，设置容灾AMF的GUAMI信息。
执行[SET DISASTERRECOVERYPOLICY]命令，设置容灾策略为无UDSF全量备份。
执行[SET DISASTERSWITCHPARA]命令，设置支持容灾功能。
执行[ADD AMFNRI]命令，设置主用AMF和容灾AMF的资源标识。
执行[ADD NOTIFYIP]命令，设置向PCF携带的容灾AMF的可替换地址信息。
执行[ADD OTHERAMFCFG]命令，设置本局可接管GUAMI对应的容灾AMF的地址信息。
执行[ADD BACKUPAMF]命令，设置本局GUAMI对应的容灾AMF。
执行[ADD TAKEOVERAMF]命令，设置本AMF可接管的容灾AMF的GUAMI。
（可选）执行[SET CONTROLPOLICY]命令，设置部分备份的控制策略。
 说明： 
通常情况下，按默认值配置即可，可以不需要执行该步骤。默认值为：拒绝原因值为Implicitly de-registered、携带备份AMF开关为携带。
如果需要配置的参数值与默认值不一致，则需要执行此步骤。 
执行[SET CONTROLPARA]命令，设置部分备份传递备份信息的控制参数。
执行[ADD NFCFG]命令，设置主用AMF和容灾AMF的NF标识。
执行[ADD CGWNODE]命令，设置主备UDSF之间的CGW互联配置。
执行[ADD CDBTENANT]命令，设置UDSF的主用租户和容灾租户。
执行[ADD CDBPARAM]命令，设置UDSF主用租户和容灾租户的参数。
执行[ADD CDBLOADLV]命令，设置UDSF主用租户和容灾租户的过负荷配置。
执行[ADD CDBMEMALARMLV]命令，设置UDSF主用租户和容灾租户的内存库告警阈值配置。
执行[ADD CDBBUFFLV]命令，设置UDSF主用租户和容灾租户的数据区告警阈值配置。
（可选）执行[SET CDUDATACHECK]命令，设置CDU上保存的数据和GSU上保存的数据的一性致功能。
 说明： 
通常情况下，按默认值配置即可，可以不需要执行该步骤。默认值为：公共数据扫描速率（条/秒）为1、数据老化时长（小时）为24、用户数据扫描速率（条/秒）为10、无线局向相关数据扫描速率（条/秒）为10、最小扫描间隔（分钟）为120。
如果需要配置的参数值与默认值不一致，则需要执行此步骤。 
执行[SYNA]:STYPE="ALL",INCREF="NO"命令，执行传送全表数据操作。
全表数据传送成功后，执行[RESET SYSTEM]命令，重启全局。
###### 部分备份修改为全量备份 
执行[SET DISASTERRECOVERYPOLICY]命令，设置容灾策略为无UDSF全量备份。
执行[ADD NFCFG]命令，设置主用AMF和容灾AMF的NF标识。
执行[ADD CGWNODE]命令，设置主备UDSF之间的CGW互联配置。
执行[ADD CDBTENANT]命令，设置UDSF的主用租户和容灾租户。
执行[SYNA]:STYPE="ALL",INCREF="NO"命令，执行传送全表数据操作。
全表数据传送成功后，执行[RESET SYSTEM]命令，重启全局。
#### 配置实例（全新配置全量备份） 
场景说明 : 
现场有主用局AMF1和容灾局AMF2，其中主用局AMF1使用GUAMI标识为1、AMF资源标识为1；容灾局AMF2使用GUAMI标识为2、AMF资源标识为2，实现AMF全量容灾备份功能。 
数据规划 : 
配置项|参数|AMF1取值|AMF2取值|数据来源|说明
---|---|---|---|---|---
GUAMI配置|GUAMI标识|1|2|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的GUAMI配置数据在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW GUAMICFG命令查看本局的GUAMI配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
移动国家码|GUAMI配置|460|460|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的GUAMI配置数据在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW GUAMICFG命令查看本局的GUAMI配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
移动网络码|GUAMI配置|00|00|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的GUAMI配置数据在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW GUAMICFG命令查看本局的GUAMI配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
Region标识|GUAMI配置|1|1|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的GUAMI配置数据在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW GUAMICFG命令查看本局的GUAMI配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
Set标识|GUAMI配置|2|2|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的GUAMI配置数据在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW GUAMICFG命令查看本局的GUAMI配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
Point标识|GUAMI配置|3|4|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的GUAMI配置数据在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW GUAMICFG命令查看本局的GUAMI配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
容灾策略配置|容灾策略配置|WITHOUT_UDSF_FULL|WITHOUT_UDSF_FULL|本端规划|-
容灾开关配置|是否支持容灾功能|YES|YES|本端规划|-
AMF资源标识配置|AMF名称|amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的资源标识在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW AMFNRI命令查看本局的资源标识配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
AMF资源标识|AMF资源标识配置|1|2|全网规划|在AMF1和AMF2上都需要配置这2个局的数据。通常本局上的资源标识在初始配置时已添加，此处只要添加对端局上数据即可。通过SHOW AMFNRI命令查看本局的资源标识配置情况：如果本局数据已配置，则只需配置备用局数据。如果本局数据未配置，则需主备局的数据都需要配置。
Notify IP配置|通知IP名称|amf2|amf1|本端规划|配置对端局的Notify IP，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。通知IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
通知IP地址类型|Notify IP配置|IPV4|IPV4|全网规划|配置对端局的Notify IP，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。通知IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
通知IP地址|Notify IP配置|192.168.1.2|192.168.1.1|全网规划|配置对端局的Notify IP，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。通知IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
Set内其他AMF配置|Pointer标识|4|3|已配置数据中获取|配置Set内其他AMF参数，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
IP地址|Set内其他AMF配置|192.168.1.2|192.168.1.1|全网规划|配置Set内其他AMF参数，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
端口号|Set内其他AMF配置|8080|8080|全网规划|配置Set内其他AMF参数，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
URI Schema|Set内其他AMF配置|HTTP|HTTP|全网规划|配置Set内其他AMF参数，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
API版本|Set内其他AMF配置|V1|V1|全网规划|配置Set内其他AMF参数，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。IP地址来自于对端局上的服务端模板配置中的IP地址。查询服务端模板配置命令为SHOW SERVERPROFILE。
备份AMF配置|本局GUAMI标识|1|2|已配置数据中获取|对应“GUAMI配置”中本端的GUAMI标识。
容灾局AMF名称|备份AMF配置|amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|已配置数据中获取|对应“AMF资源标识配置”中对端局的AMF名称，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。
接管AMF配置|Backup GUAMI标识|2|1|已配置数据中获取|对应“GUAMI配置”中对端局的GUAMI标识，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。
主用AMF名称|接管AMF配置|amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|已配置数据中获取|对应“AMF资源标识配置”中对端局的AMF名称，即AMF1上填写AMF2的数据，AMF2上填写AMF1上的数据。
控制参数配置|备份AMF的GTPC地址|192.168.2.2|192.168.2.1|全网规划|需要填写对端局的GTPC地址，即AMF1上填写AMF2的GTPC地址，AMF2上填写AMF1上的GTPC地址。GTPC地址的获取命令为SHOW AMFGTPCADDRCFG。
备份数据消息发送频率（毫秒）|控制参数配置|800|800|本端规划|保持默认即可。
备份数据消息打包大小（KB）|控制参数配置|4|4|本端规划|保持默认即可。
老化时间（分钟）|控制参数配置|2160|2160|本端规划|保持默认即可。
NF标识配置|NF标识|1|2|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。NF标识为实例化时本局的局号。
NF名称|NF标识配置|amf1|amf2|本端规划|不需要和AMF名称保持一致。
NF类型|NF标识配置|在AMF1上配置时选择：本地NF在AMF2上配置时选择：和本地NF部署在不同TMSP的其他NF|在AMF2上配置时选择：本地NF在AMF1上配置时选择：和本地NF部署在不同TMSP的其他NF|本端规划|本局设置为本地NF，对端局设置为和本地NF部署在不同TMSP的其他NF。
CGW互联配置|NF ID|1|2|已配置数据中获取|在AMF1和AMF2上都需要配置这2个局的数据。NF ID对应“NF标识配置”中的NF标识。
网络用途|CGW互联配置|数据同步网络1|数据同步网络1|本端规划|-
IP地址类型|CGW互联配置|IPV4|IPV4|本端规划|-
IP地址|CGW互联配置|192.168.3.1|192.168.3.2|本端规划|-
侦听端口最小值|CGW互联配置|30000|30000|本端规划|CGW作为服务端的侦听端口范围，与AMF部署的CGW虚机个数要相同。例如：AMF有3个CGW虚机，则AMF的侦听端口最小值配置为30000，AMF的侦听端口最大值配置为30002。
侦听端口最大值|CGW互联配置|30002|30002|本端规划|CGW作为服务端的侦听端口范围，与AMF部署的CGW虚机个数要相同。例如：AMF有3个CGW虚机，则AMF的侦听端口最小值配置为30000，AMF的侦听端口最大值配置为30002。
连接端口最小值|CGW互联配置|50000|50000|本端规划|CGW作为客户端的端口范围，配置范围为50000~（49999+16*CGW虚机数量）。例如：AMF有3个CGW虚机，则端口范围为50000~50047。
连接端口最大值|CGW互联配置|50047|50047|本端规划|CGW作为客户端的端口范围，配置范围为50000~（49999+16*CGW虚机数量）。例如：AMF有3个CGW虚机，则端口范围为50000~50047。
NF列表|CGW互联配置|1|2|本端规划|实例化时本局AMF的局号。
VPNID|CGW互联配置|0|0|已配置数据中获取|在本局AMF的CommonS_TMSP服务下的Rosng配置中，使用show ip vrf detail命令，获取VRF的VPNID。如果没有配置，则VPNID为0。
DSCP标签|CGW互联配置|0|0|已配置数据中获取|在本局AMF中使用SHOW QOSMAPIPV4或SHOW QOSMAPIPV6命令获取可用的DSCP。
租户配置|租户ID|1|2|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。
租户名称|租户配置|amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|已配置数据中获取|对应“AMF资源标识配置”中的AMF名称。
每个域的默认激活节点数|租户配置|3|3|本端规划|-
主用NF(局)标识|租户配置|1|2|本端规划|实例化时主用局的局号。
备用NF(局)标识|租户配置|2|1|本端规划|实例化时容灾局的局号。
左域SC TYPE|租户配置|9|0|本端规划|需要和服务注册信息获取的与租户相关SC类型对应的SC类型ID保持一致。SC类型ID的查询命令为：SHOW SERVICEINFO:SERVICETYPENAME="Nudsf_UnstructuredDataManagement"
右域SC TYPE|租户配置|10|12|本端规划|需要和服务注册信息获取的与租户相关SC类型对应的SC类型ID保持一致。SC类型ID的查询命令为：SHOW SERVICEINFO:SERVICETYPENAME="Nudsf_UnstructuredDataManagement"
访问策略|租户配置|仅本地访问|仅本地访问|本端规划|-
单向复制开关|租户配置|开启|开启|本端规划|-
CDB参数配置|租户ID|1|2|已配置数据中获取|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
内存库大小(MB)|CDB参数配置|6656|6656|本端规划|中规格虚机（C4M32）配置值6656。小规格虚机（C2M8）配置值4096。
日志库大小(MB)|CDB参数配置|1024|1024|本端规划|使用默认值1024。
数据区个数|CDB参数配置|15000|15000|本端规划|使用默认值15000。
过负荷配置|租户ID|1|2|已配置数据中获取|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
过负荷等级|过负荷配置|0/1/2/3/4|0/1/2/3/4|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
CPU负荷阈值|过负荷配置|75/80/85/90/95|75/80/85/90/95|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
内存库告警阈值配置|租户ID|1|2|已配置数据中获取|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
内存库一级告警阈值(%)|内存库告警阈值配置|90|90|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
内存库二级告警阈值(%)|内存库告警阈值配置|80|80|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
内存库三级告警阈值(%)|内存库告警阈值配置|70|70|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
数据区告警阈值配置|租户ID|1|2|已配置数据中获取|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
数据区1级告警阈值(%)|数据区告警阈值配置|90|90|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
数据区2级告警阈值(%)|数据区告警阈值配置|80|80|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
数据区3级告警阈值(%)|数据区告警阈值配置|70|70|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
数据区4级告警阈值(%)|数据区告警阈值配置|60|60|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。租户ID对应“租户配置”中的租户ID。
配置步骤 : 
步骤|说明|操作
---|---|---
1|在AMF1上查询是否新增了AMF1的GUAMI。如果未有AMF1的GUAMI数据，则需要新增AMF1的GUAMI。如果有AMF1的GUAMI数据，则只需新增AMF2的GUAMI。|查询命令：SHOW GUAMICFG，查询结果中，如果有AMF1的GUAMI数据，则说明已经添加过了AMF的GUAMI，此处不需要执行添加操作，否则需要新增AMF1的GUAMI。新增AMF1的GUAMI的命令：ADD GUAMICFG:GUAMIID=1,MCC="460",MNC="00",REGIONID=1,SETID=2,POINTID=3
在AMF1上新增AMF2的GUAMI。|1|ADD GUAMICFG:GUAMIID=2,MCC="460",MNC="00",REGIONID=1,SETID=2,POINTID=4
2|在AMF1上设置容灾策略。|SET DISASTERRECOVERYPOLICY:DISASTERPOLICY="WITHOUT_UDSF_FULL"
3|在AMF1上设置容灾开关。|SET DISASTERSWITCHPARA:SUPPORTDISASTER="YES"
4|在AMF1上查询是否新增了AMF1的资源标识。如果未有AMF1的资源标识数据，则需要新增AMF1的资源标识。如果有AMF1的资源标识数据，则只需新增AMF2的资源标识。|查询命令：SHOW AMFNRI，查询结果中，如果有AMF1的资源标识数据，则说明已经添加过了AMF的资源标识，此处不需要执行添加操作，否则需要新增AMF1的资源标识。新增AMF1的资源标识的命令：ADD AMFNRI:AMFNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",AMFNRI=1
在AMF1上新增AMF2资源标识。|4|ADD AMFNRI:AMFNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",AMFNRI=2
5|在AMF1上新增AMF2的Notify IP。|ADD NOTIFYIP:IPADDRNAME="amf2",IPADDRTYPE="IPV4",IPADDRESS=192.168.1.2
6|在AMF1上新增Set内其他AMF配置。|ADD OTHERAMFCFG:POINTERID=4,IPADDRESS=192.168.1.2,PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
7|在AMF1上新增备份AMF配置。|ADD BACKUPAMF:GUAMIID=1,AMFNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org"
8|在AMF1上新增接管AMF配置。|ADD TAKEOVERAMF:BACKUPGUAMI=2,MASTERAMFNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org"
9|在AMF1上修改控制参数配置。|SET CONTROLPARA:BACKAMFIP="192.168.2.2",BACKRATE=800,BACKSIZE=4,AGINGTIME=2160
10|在AMF1上新增AMF1和AMF2的NF标识。|ADD NFCFG:NFID=1,NFNAME="amf1",NFTYPE="self_nf"ADD NFCFG:NFID=2,NFNAME="amf2",NFTYPE="diff_tmsp_nf"
00|在AMF1上新增AMF1和AMF2的CGW互联配置。|ADD CGWNODE:NFID=1,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.1",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="1",VPNID=0,DSCP=0ADD CGWNODE:NFID=2,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.2",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="2",VPNID=0,DSCP=0
12|在AMF1上新增AMF1和AMF2的租户配置。|ADD CDBTENANT:TENANTID=1,TENANTNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=1,NFID2=2,LEFTSCTYPE=9,RIGHTSCTYPE=10,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"ADD CDBTENANT:TENANTID=2,TENANTNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=2,NFID2=1,LEFTSCTYPE=0,RIGHTSCTYPE=12,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"
13|在AMF1上新增AMF1和AMF2的CDB参数配置。|ADD CDBPARAM:TENANTID=1,MDBSIZE=6656,LOGBUFSIZE=1024,BUFFNUM=15000ADD CDBPARAM:TENANTID=2,MDBSIZE=6656,LOGBUFSIZE=1024,BUFFNUM=15000
14|在AMF1上新增AMF1和AMF2的过负荷配置。|ADD CDBLOADLV:TENANTID=1,LEVEL=0,CPU=75ADD CDBLOADLV:TENANTID=1,LEVEL=1,CPU=80ADD CDBLOADLV:TENANTID=1,LEVEL=2,CPU=85ADD CDBLOADLV:TENANTID=1,LEVEL=3,CPU=90ADD CDBLOADLV:TENANTID=1,LEVEL=4,CPU=95ADD CDBLOADLV:TENANTID=2,LEVEL=0,CPU=75ADD CDBLOADLV:TENANTID=2,LEVEL=1,CPU=80ADD CDBLOADLV:TENANTID=2,LEVEL=2,CPU=85ADD CDBLOADLV:TENANTID=2,LEVEL=3,CPU=90ADD CDBLOADLV:TENANTID=2,LEVEL=4,CPU=95
15|在AMF1上新增AMF1和AMF2的内存库告警阈值配置。|ADD CDBMEMALARMLV:TENANTID=1,DB_RATIO_LV1=90,DB_RATIO_LV2=80,DB_RATIO_LV3=70ADD CDBMEMALARMLV:TENANTID=2,DB_RATIO_LV1=90,DB_RATIO_LV2=80,DB_RATIO_LV3=70
16|在AMF1上新增AMF1和AMF2的数据区告警阈值配置。|ADD CDBBUFFLV:TENANTID=1,BUFF_LV1=90,BUFF_LV2=80,BUFF_LV3=70,BUFF_LV4=60ADD CDBBUFFLV:TENANTID=2,BUFF_LV1=90,BUFF_LV2=80,BUFF_LV3=70,BUFF_LV4=60
17|在AMF1上传送全表数据。|SYNA:STYPE="ALL",INCREF="NO"
18|在AMF1上全表数据传送成功后，重启全局。|RESET SYSTEM
步骤|说明|操作
---|---|---
1|在AMF2上查询是否新增了AMF2的GUAMI。如果未有AMF2的GUAMI数据，则需要新增AMF2的GUAMI。如果有AMF2的GUAMI数据，则只需新增AMF1的GUAMI。|查询命令：SHOW GUAMICFG新增AMF2的GUAMI的命令：ADD GUAMICFG:GUAMIID=2,MCC="460",MNC="00",REGIONID=1,SETID=2,POINTID=4
在AMF2上新增AMF1的GUAMI。|1|ADD GUAMICFG:GUAMIID=1,MCC="460",MNC="00",REGIONID=1,SETID=2,POINTID=3
2|在AMF2上设置容灾策略。|SET DISASTERRECOVERYPOLICY:DISASTERPOLICY="WITHOUT_UDSF_FULL"
3|在AMF2上设置容灾开关。|SET DISASTERSWITCHPARA:SUPPORTDISASTER="YES"
4|在AMF2上查询是否新增了AMF2的资源标识。如果未有AMF2的资源标识数据，则需要新增AMF2的资源标识。如果有AMF2的资源标识数据，则只需新增AMF1的资源标识。|查询命令：SHOW AMFNRI新增AMF2的资源标识的命令：ADD AMFNRI:AMFNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",AMFNRI=2
在AMF2上新增AMF1资源标识。|4|ADD AMFNRI:AMFNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",AMFNRI=1
5|在AMF2上新增AMF1的Notify IP。|ADD NOTIFYIP:IPADDRNAME="amf1",IPADDRTYPE="IPV4",IPADDRESS=192.168.1.1
6|在AMF2上新增Set内其他AMF配置。|ADD OTHERAMFCFG:POINTERID=3,IPADDRESS=192.168.1.1,PORT=8080,SCHEMA="HTTP",APIVERSION="V1"
7|在AMF2上新增备份AMF配置。|ADD BACKUPAMF:GUAMIID=2,AMFNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org"
8|在AMF2上新增接管AMF配置。|ADD TAKEOVERAMF:BACKUPGUAMI=1,MASTERAMFNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org"
9|在AMF2上修改控制参数配置。|SET CONTROLPARA:BACKAMFIP="192.168.2.1",BACKRATE=800,BACKSIZE=4,AGINGTIME=2160
10|在AMF2上新增AMF2和AMF1的NF标识。|ADD NFCFG:NFID=2,NFNAME="amf2",NFTYPE="self_nf"ADD NFCFG:NFID=1,NFNAME="amf1",NFTYPE="diff_tmsp_nf"
00|在AMF2上新增AMF2和AMF1的CGW互联配置。|ADD CGWNODE:NFID=2,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.2",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="2",VPNID=0,DSCP=0ADD CGWNODE:NFID=1,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.1",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="1",VPNID=0,DSCP=0
12|在AMF2上新增AMF2和AMF1的租户配置。|ADD CDBTENANT:TENANTID=2,TENANTNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=2,NFID2=1,LEFTSCTYPE=0,RIGHTSCTYPE=12,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"ADD CDBTENANT:TENANTID=1,TENANTNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=1,NFID2=2,LEFTSCTYPE=9,RIGHTSCTYPE=10,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"
13|在AMF2上新增AMF2和AMF1的CDB参数配置。|ADD CDBPARAM:TENANTID=2,MDBSIZE=6656,LOGBUFSIZE=1024,BUFFNUM=15000ADD CDBPARAM:TENANTID=1,MDBSIZE=6656,LOGBUFSIZE=1024,BUFFNUM=15000
14|在AMF2上新增AMF2和AMF1的过负荷配置。|ADD CDBLOADLV:TENANTID=2,LEVEL=0,CPU=75ADD CDBLOADLV:TENANTID=2,LEVEL=1,CPU=80ADD CDBLOADLV:TENANTID=2,LEVEL=2,CPU=85ADD CDBLOADLV:TENANTID=2,LEVEL=3,CPU=90ADD CDBLOADLV:TENANTID=2,LEVEL=4,CPU=95ADD CDBLOADLV:TENANTID=1,LEVEL=0,CPU=75ADD CDBLOADLV:TENANTID=1,LEVEL=1,CPU=80ADD CDBLOADLV:TENANTID=1,LEVEL=2,CPU=85ADD CDBLOADLV:TENANTID=1,LEVEL=3,CPU=90ADD CDBLOADLV:TENANTID=1,LEVEL=4,CPU=95
15|在AMF2上新增AMF2和AMF1的内存库告警阈值配置。|ADD CDBMEMALARMLV:TENANTID=2,DB_RATIO_LV1=90,DB_RATIO_LV2=80,DB_RATIO_LV3=70ADD CDBMEMALARMLV:TENANTID=1,DB_RATIO_LV1=90,DB_RATIO_LV2=80,DB_RATIO_LV3=70
16|在AMF2上新增AMF2和AMF1的数据区告警阈值配置。|ADD CDBBUFFLV:TENANTID=2,BUFF_LV1=90,BUFF_LV2=80,BUFF_LV3=70,BUFF_LV4=60ADD CDBBUFFLV:TENANTID=1,BUFF_LV1=90,BUFF_LV2=80,BUFF_LV3=70,BUFF_LV4=60
17|在AMF2上传送全表数据。|SYNA:STYPE="ALL",INCREF="NO"
18|在AMF2上全表数据传送成功后，重启全局。|RESET SYSTEM
#### 配置实例（部分备份修改为全量备份） 
场景说明 : 
现场有主用局AMF1和容灾局AMF2已经配置为部分备份，对主用局AMF1和容灾局AMF2改造成全量备份功能。 
数据规划 : 
配置项|参数|AMF1取值|AMF2取值|数据来源|说明
---|---|---|---|---|---
容灾策略配置|容灾策略配置|WITHOUT_UDSF_FULL|WITHOUT_UDSF_FULL|本端规划|-
NF标识配置|NF标识|1|2|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。NF标识为实例化时本局的局号。
NF名称|NF标识配置|amf1|amf2|本端规划|不需要和AMF名称保持一致。
NF类型|NF标识配置|在AMF1上配置时选择：本地NF在AMF2上配置时选择：和本地NF部署在不同TMSP的其他NF|在AMF2上配置时选择：本地NF在AMF1上配置时选择：和本地NF部署在不同TMSP的其他NF|本端规划|本局设置为本地NF，对端局设置为和本地NF部署在不同TMSP的其他NF。
CGW互联配置|NF ID|1|2|已配置数据中获取|在AMF1和AMF2上都需要配置这2个局的数据。NF ID对应“NF标识配置”中的NF标识
网络用途|CGW互联配置|数据同步网络1|数据同步网络1|本端规划|-
IP地址类型|CGW互联配置|IPV4|IPV4|本端规划|-
IP地址|CGW互联配置|192.168.3.1|192.168.3.2|本端规划|-
侦听端口最小值|CGW互联配置|30000|30000|本端规划|CGW作为服务端的侦听端口范围，与AMF部署的CGW虚机个数要相同。例如：AMF有3个CGW虚机，则AMF的侦听端口最小值配置为30000，AMF的侦听端口最大值配置为30002。
侦听端口最大值|CGW互联配置|30002|30002|本端规划|CGW作为服务端的侦听端口范围，与AMF部署的CGW虚机个数要相同。例如：AMF有3个CGW虚机，则AMF的侦听端口最小值配置为30000，AMF的侦听端口最大值配置为30002。
连接端口最小值|CGW互联配置|50000|50000|本端规划|CGW作为客户端的端口范围，配置范围为50000~（49999+16*CGW虚机数量）。例如：AMF有3个CGW虚机，则端口范围为50000~50047。
连接端口最大值|CGW互联配置|50047|50047|本端规划|CGW作为客户端的端口范围，配置范围为50000~（49999+16*CGW虚机数量）。例如：AMF有3个CGW虚机，则端口范围为50000~50047。
NF列表|CGW互联配置|1|2|本端规划|实例化时本局AMF的局号。
VPNID|CGW互联配置|0|0|已配置数据中获取|在本局AMF的CommonS_TMSP服务下的Rosng配置中，使用show ip vrf detail命令，获取VRF的VPNID。如果没有配置，则VPNID为0。
DSCP标签|CGW互联配置|0|0|已配置数据中获取|在本局AMF中使用SHOW QOSMAPIPV4或SHOW QOSMAPIPV6命令获取可用的DSCP。
租户配置|租户ID|1|2|本端规划|在AMF1和AMF2上都需要配置这2个局的数据。
租户名称|租户配置|amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org|已配置数据中获取|对应“AMF资源标识配置”中的AMF名称。
每个域的默认激活节点数|租户配置|3|3|本端规划|-
主用NF(局)标识|租户配置|1|2|本端规划|实例化时主用局的局号。
备用NF(局)标识|租户配置|2|1|本端规划|实例化时容灾局的局号。
左域SC TYPE|租户配置|9|0|本端规划|需要和服务注册信息获取的与租户相关SC类型对应的SC类型ID保持一致。SC类型ID的查询命令为：SHOW SERVICEINFO:SERVICETYPENAME="Nudsf_UnstructuredDataManagement"
右域SC TYPE|租户配置|10|12|本端规划|需要和服务注册信息获取的与租户相关SC类型对应的SC类型ID保持一致。SC类型ID的查询命令为：SHOW SERVICEINFO:SERVICETYPENAME="Nudsf_UnstructuredDataManagement"
访问策略|租户配置|仅本地访问|仅本地访问|本端规划|-
配置步骤 : 
步骤|说明|操作
---|---|---
1|在AMF1上设置容灾策略。|SET DISASTERRECOVERYPOLICY:DISASTERPOLICY="WITHOUT_UDSF_FULL"
2|在AMF1上新增主用局AMF1和容灾局AMF2的NF标识。|ADD NFCFG:NFID=1,NFNAME="amf1",NFTYPE="self_nf"ADD NFCFG:NFID=2,NFNAME="amf2",NFTYPE="diff_tmsp_nf"
3|在AMF1上新增主用局AMF1和容灾局AMF2的CGW互联配置。|ADD CGWNODE:NFID=1,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.1",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="1",VPNID=0,DSCP=0ADD CGWNODE:NFID=2,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.2",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="2",VPNID=0,DSCP=0
4|在AMF1上修改主用局AMF1和容灾局AMF2的租户配置。|SET CDBTENANT:TENANTID=1,TENANTNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=1,NFID2=2,LEFTSCTYPE=9,RIGHTSCTYPE=10,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"SET CDBTENANT:TENANTID=2,TENANTNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=2,NFID2=1,LEFTSCTYPE=0,RIGHTSCTYPE=12,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"
5|在AMF1上传送全表数据。|SYNA:STYPE="ALL",INCREF="NO"
6|在AMF1上全表数据传送成功后，重启全局。|RESET SYSTEM
步骤|说明|操作
---|---|---
1|在AMF2上设置容灾策略。|SET DISASTERRECOVERYPOLICY:DISASTERPOLICY="WITHOUT_UDSF_FULL"
2|在AMF2上新增容灾局AMF2和主用局AMF1的NF标识。|ADD NFCFG:NFID=2,NFNAME="amf2",NFTYPE="self_nf"ADD NFCFG:NFID=1,NFNAME="amf1",NFTYPE="diff_tmsp_nf"
3|在AMF2上新增容灾局AMF2和主用局AMF1的CGW互联配置。|ADD CGWNODE:NFID=2,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.2",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="2",VPNID=0,DSCP=0ADD CGWNODE:NFID=1,NETTYPE="data_access_1",IPTYPE="IPV4",IP="192.168.3.1",SERVERPORTSTART=30000,SERVERPORTEND=30002,CONNECTPORTSTART=50000,CONNECTPORTEND=50047,NFLIST="1",VPNID=0,DSCP=0
4|在AMF2上修改容灾局AMF2和主用局AMF1的租户配置。|SET CDBTENANT:TENANTID=2,TENANTNAME="amf2.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=2,NFID2=1,LEFTSCTYPE=9,RIGHTSCTYPE=12,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"SET CDBTENANT:TENANTID=1,TENANTNAME="amf1.cluster1.net1.amf.5gc.mnc000.mcc460.3gppnetwork.org",ACTIVENODES=3,NFID1=1,NFID2=2,LEFTSCTYPE=0,RIGHTSCTYPE=10,ACCESSPOLICY="local_access_only",ONEWAYREPLICATION="ONE_WAY_REPLICATION_ON"
5|在AMF2上传送全表数据。|SYNA:STYPE="ALL",INCREF="NO"
6|在AMF2上全表数据传送成功后，重启全局。|RESET SYSTEM
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|主备AMF之间能够备份全量用户信息
---|---
测试目的|验证主备AMF之间能够备份全量用户信息。
预置条件|AMF Pool环境就绪，环境中部署了至少主备两套AMF（AMF1和AMF2），以及一套NRF。NRF支持NF注册、订阅以及通知流程。AMF以及其周边NF已经在NRF上完成注册、订阅操作。在各个逻辑网元上建立接口信令跟踪和用户信令跟踪。“AMF支持无UDSF全量容灾”和“AMF支持无UDSF容灾部分备份功能”的License项已打开。
测试过程|UE在AMF1上注册成功。在AMF2上查询用户信息。
通过准则|通过动态命令SHOW USER INFORMATION，可以在AMF2上查询到AMF1用户的全部上下文信息。
测试结果|–
测试项目|备份AMF能够在主用AMF状态异常时通过上行流程正常接管用户
---|---
测试目的|验证主用AMF状态异常时，备份AMF能够通过上行流程正常接管用户并且业务无损。
预置条件|AMF Pool环境就绪，环境中部署了至少主备两套AMF（AMF1和AMF2），以及一套NRF。NRF支持NF注册、订阅以及通知流程。AMF以及其周边NF已经在NRF上完成注册、订阅操作。在各个逻辑网元上建立接口信令跟踪和用户信令跟踪。“AMF支持无UDSF全量容灾”和“AMF支持无UDSF容灾部分备份功能”的License项已打开。
测试过程|UE在AMF1上注册成功，创建会话后进入空闲态。AMF1计划性维护或者故障。UE发起业务请求尝试激活会话。
通过准则|基站将UE的业务请求投递到AMF2，AMF2能够正常处理UE的业务请求并激活会话，业务请求流程结束后AMF2通知周边NF用户已被接管并重新分配GUTI。
测试结果|–
测试项目|备份AMF能够在主用AMF状态异常时通过下行流程正常接管用户
---|---
测试目的|验证主用AMF状态异常时，备份AMF能够通过下行流程正常接管用户并且业务无损。
预置条件|AMF Pool环境就绪，环境中部署了至少主备两套AMF（AMF1和AMF2），以及一套NRF。NRF支持NF注册、订阅以及通知流程。AMF以及其周边NF已经在NRF上完成注册、订阅操作。在各个逻辑网元上建立接口信令跟踪和用户信令跟踪。“AMF支持无UDSF全量容灾”和“AMF支持无UDSF容灾部分备份功能”的License项已打开。
测试过程|UE在AMF1上注册成功，创建会话后进入空闲态。AMF1计划性维护或者故障。SMF触发N1N2 Message Transfer请求尝试恢复用户面。
通过准则|SMF识别AMF1不可达，重新通过NRF发现AMF2并将N1N2 Message Transfer请求投递到AMF2，AMF2能够正常寻呼UE，流程结束后AMF2通知周边NF用户已被接管并重新分配GUTI。
测试结果|–
常见问题处理 : 
无。 
# 缩略语 
# 缩略语 
AMF : 
Authentication Management Field鉴权管理域
Access and Mobility Management Function接入和移动管理功能
AUSF : 
Authentication Server Function鉴权服务器功能
## CDB 
Cloud Database云数据库
## CDU 
Cloud Database Unit云数据库单元
## DDN 
Downlink Data Notification下行数据通知
EIR : 
Equipment Identity Register设备标识寄存器
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
## GUAMI 
Globally Unique AMF ID全球唯一AMF标识
HLR : 
Home Location Register归属位置寄存器
HSS : 
Home Subscriber Server归属用户服务器
MME : 
Mobility Management Entity移动管理实体
NF : 
Network Function网络功能
NRF : 
NF Repository Function网络功能仓储
NSSF : 
Network Slice Selection Function网络切片选择功能
PCF : 
Policy Control Function策略控制功能
RNC : 
Radio Network Controller无线网络控制器
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SMF : 
Session Management Function会话管理功能
## SMSF 
Short Message Service Function短消息服务功能
UDM : 
Unified Data Management统一数据管理
UDSF : 
Unstructured Data Storage Function非结构化数据存储功能
## VNFC 
Virtualized Network Function Component虚拟网络功能组件
eNodeB : 
Evolved NodeB演进的NodeB
## uMAC 
unified Mobile Access Controller统一的移动性接入控制器
# ZUF-76-05 IP协议栈 
## ZUF-76-05-001 JumboFrame 
概述 : 
巨帧是一种厂商标准的超长帧格式，专门为千兆以太网设计的。随着巨帧的应用，最大帧长度可以增加到2020字节。 
客户收益 : 
简化SGSN和GGSN之间用户面报文的重分片过程，提高处理效率。 
说明 : 
巨帧是一种厂商标准的超长帧格式，专门为千兆以太网设计的。 
通过这种技术，SGSN支持将IP报文从1500字节扩展到2020字节，防止Gn报文分片。 
## ZUF-76-05-002 VLAN 
特性描述 : 
特性描述 : 
适用网元 : 
AMF、MME、SGSN 
描述 : 
定义 : 
VLAN是对物理网络的逻辑划分，用于将一个物理网络划分为多个逻辑上的虚拟网络，从而限制广播报文的范围。处于同一VLAN内的设备能直接二层互通，而处于不同VLAN内的设备二层是相互隔离的，需经过三层路由转发。
ZXUN uMAC支持通过在子接口上配置VLAN ID的方式实现VLAN功能。
背景知识 : 
引入VLAN的意义
引入VLAN之前，存在以下问题：
 
可靠性差网络中所有的设备都属于同一个广播域，容易导致广播风暴，影响网络的正常使用。 
 
安全性差网络中的所有设备二层均可以相互直接访问。 
 
资源浪费如果想构建安全的网络，不同的企业需要搭建自己的网络。 
 
因此，802.1Q引入了VLAN技术，将一个物理的LAN划分为逻辑上的多个广播域。不同VLAN的设备不能直接二层互通，从而广播报文被限制在同一个VLAN内，提高网络的可靠性和安全性。
VLAN报文封装
802.1Q标准定义了一种新的帧格式，在标准的以太网帧的源地址后面加入了4个字节的802.1Q的报文头（VLAN Tag）。Tag头定义了以太网帧所属的VLAN，通过Tag头来区分Tag帧属于哪个VLAN，如[图1]所示。
图1  带VLAN的报文结构图
TPID（Tag Protocol Identifier
标签协议标识符）表示报文是否带有VLAN Tag，长度为16比特。缺省情况下，TPID取值为0x8100，表示数据帧中包括VLAN Tag。
Priority
用来表示报文的802.1p优先级，长度为3比特，其值由QoS等流控信息决定。
CFI用来表示MAC地址在不同的传输介质中是否以标准格式进行封装，长度为1比特。取值为0表示MAC地址以标准格式进行封装，为1表示以非标准格式封装，缺省取值为0。
VLAN ID用来表示该报文所属VLAN的编号，长度为12比特，取值范围为0～4095。由于0 和4095为协议保留取值，所以VLAN ID的取值范围为1～4094。
应用场景 : 
本特性无应用场景限制，适用于所有的移动网络。 
客户收益 : 
受益方|受益描述
---|---
运营商|VLAN内部的广播和单播流量不会被转发到其他VLAN中，从而有助于控制网络流量，提高网络安全性和可靠性。增加新的VLAN用户，运营商无需升级硬件设备增加端口，只需要在设备上新增一个对应的VLAN子接口即可，由此实现减少设备投资、简化网络管理。
终端用户|该特性对终端用户不可见。
实现原理 : 
系统架构 : 
[图2]是一个VLAN应用，3台交换机在不同的区域，分别连接3台办公机，这3台办公机分别属于不同的VLAN，比如不同的终端用户，同一个虚线框表示同一个VLAN。
图2  VLAN应用示意图
涉及的网元 : 
网元名称|网元作用
---|---
AMF、SMF、UPF、PCF等5GC NF|对子接口接收的报文解VLAN封装，对子接口发送的报文加VLAN封装。
对端网元设备|对端网元设备与ZXUN uMAC上同一VLAN下的子接口能互通。
本网元实现 : 
运营商在部署分组交换网时，可以在ZXUN uMAC上配置VLAN，用于实现以下功能：
 
流量隔离ZXUN uMAC可以将不同的子接口划分到不同的VLAN。不同VLAN之间的报文二层不能互通，从而实现流量隔离。 
 
增加接口数量ZXUN uMAC支持在一个物理接口下创建多个子接口，并将多个子接口划分到不同的VLAN，可以在不增加物理链路的情况下，增加接口数量。 
 
适配对端如果与ZXUN uMAC对接的网元设备划分了VLAN，ZXUN uMAC需要将子接口也划分到相应的VLAN中。 
 
运营商对ZXUN uMAC配置子接口和VLAN ID，其中VLAN ID与对方设备配置的VLAN
ID相同。
ZXUN uMAC对子接口接收的报文解VLAN封装，对子接口发送的报文加VLAN封装。
业务流程 : 
不涉及。 
系统影响 : 
VLAN子接口对报文的收发决定于系统的转发性能，该特性本身不会影响系统性能。如果配置了大量的VLAN子接口会增加系统配置恢复的时长。 
应用限制 : 
与ZXUN uMAC对接的网元设备需要支持VLAN特性，VLAN特性才能正常使用。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准类别|标准名称
---|---
IEEE|802.1Q,Virtual Bridged Local Area Networks
特性能力 : 
名称|指标
---|---
整局支持VLAN数目|4094
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
配置项目|命令
---|---
配置子接口|interface
配置子接口|ip address
配置子接口|ip vrf forwarding
配置VLAN|vlan-configuration
配置VLAN|interface
配置VLAN|encapsulation-dot1q
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
运营商在部署分组交换网时，ZXUN uMAC支持在一个物理接口下创建多个子接口，并将多个子接口划分到不同的VLAN中，可以在不增加物理链路的情况下，增加接口数量。
配置前提 : 
 
网络平面使用SR-IOV网卡或DVS网卡，这两种网卡类型支持VLAN子接口。 
 
网络平面需要配置成vlan-transparent透传模式。 
 
配置过程 : 
进入ROSNG配置模式 
在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置
，进入ROSNG配置模式。
（可选）创建VRF。 
 说明： 
是否创建VRF，是在部署分组交换网时，由运营商规划决定。 
创建子接口。 
[interface]
配置子接口的IP地址。 
[ip address]
（可选）子接口绑定VRF。 
[ip vrf forwarding]
进入VLAN配置模式。 
[vlan-configuration]
进入VLAN子接口业务配置模式，interface name为之前创建的子接口名称。 
[interface]
配置子接口的VLAN封装类型及VLAN ID。 
[encapsulation-dot1q]
 说明： 
VLAN ID值由运营商在部署网络时规划决定。 
如果子接口绑定了VLAN ID，则与其对接的设备也需绑定相同的VLAN ID，以保证正常通讯。 
配置实例 : 
场景说明 : 
利用VLAN子接口技术，实现同一物理以太网接口上不同VLAN用户的接入和路由，如[图1]所示。
图1  VLAN接口配置实例拓扑图
数据规划 : 
子接口名称|VLAN-ID|子接口IP地址|子网掩码
---|---|---|---
xgei-1/0/1/1.10|100|192.2.1.1|255.255.255.0
配置步骤 : 
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|创建子接口|ZXROSNG#config terminalZXROSNG(config)#interface xgei-1/0/1/1.10ZXROSNG(config-if-xgei-1/0/1/1.10)#exit
3|进入子接口VLAN配置模式|ZXROSNG(config)#vlan-configurationZXROSNG(config-vlan)#interface xgei-1/0/1/1.10
4|配置VLAN ID|ZXROSNG(config-vlan-if-xgei-1/0/1/1.10)#encapsulation-dot1q100ZXROSNG(config-vlan-if-xgei-1/0/1/1.10)#exitZXROSNG(config-vlan)#exit
5|为子接口配置IP地址|ZXROSNG(config)#interface xgei-1/0/1/1.10ZXROSNG(config-if-xgei-1/0/1/1.10)#no shutdownZXROSNG(config-if-xgei-1/0/1/1.10)#ip address 192.2.1.1 255.255.255.0ZXROSNG(config-if-xgei-1/0/1/1.10)#exit
调整特性 : 
不涉及。 
测试用例 : 
测试项目|VLAN子接口
---|---
测试目的|验证VLAN子接口功能，能正常进行报文的转发和处理。
预置条件|基础配置完成。配置VLAN子接口。对端网元设备支持VLAN特性，且配置相同的VLAN-ID。
测试过程|从本端子接口向对端接口ping包。
通过准则|ping包正常，两个网元之间可以互通。
测试结果|–
常见问题处理 : 
不涉及。 
## ZUF-76-05-003 IPv6 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响特性交互遵循标准特性能力可获得性O&M相关 
描述 : 
定义
IPv6是Internet Protocol Version
6的缩写，是IETF设计的用于替代现行版本IP协议（IPv4）的下一代IP协议。
背景知识
目前全球因特网所采用的协议族是TCP/IP协议族。IP是TCP/IP协议族中网络层的协议，是TCP/IP协议族的核心协议。
IPv6相比IPv4，具有以下特点： 
IPv6地址长度为128位，相比IPv4的32位地址长度，地址空间增大了2的96次方倍，可以能够解决IPv4地址个数不足的问题。 
灵活的IP报文头部格式。使用一系列固定格式的扩展头部取代了IPv4中可变长度的选项字段。IPv6中选项部分的出现方式也有所变化，使路由器可以简单路过选项而不做任何处理，加快了报文处理速度。 
简化的IP报文头部格式。IPv6简化了报文头部格式，字段只有8个，加快报文转发，提高了吞吐量。 
提高安全性。身份认证和隐私权是IPv6的关键特性。 
支持更多的服务类型。 
允许协议继续演变，增加新的功能，使之适应未来技术的发展。 
本功能指SGSN、MME、AMF承载层面（接口和路由）支持IPv6及IPv4IPv6双栈。 
应用场景 : 
以MME为例，MME在3GPP网络中的位置如[图1]所示。
图1  MME在3GPP的标准架构中的位置
本功能应用于MME与其他周围网元、路由器设备通过IPv6，及IPv4IPv6双栈进行互联互通。 
客户收益 : 
收益者|收益描述
---|---
运营商|支持承载网络从IPv4平滑演进IPv6网络，保护了运营商的现有IPv4网络投资，又支持接入新建的IPv6网络。
实现原理 : 
涉及的网元
本功能属于底层承载相关功能： 
需要与SGSN、MME、AMF对接的对方设备也要支持IPv6能力。 
需要DNS服务器地址解析时，返回IPv6类型的地址。 
本网元实现
业务接口支持IPv6比如，对于MME标准协议接口，支持IPv6地址。 
License控制本功能受IPv6 License功能开关控制，只有开关开启时，配置的IPv6地址才有效。接口板也才支持IPv6业务报文的接收和转发。License功能开关变更，比如开启到关闭，或者关闭到开启，需要重启整局。 
GTP节点管理支持双栈MME、SGSN支持双栈IPv6功能，对GTP节点管理功能有波及，不影响其他接口的节点管理，比如偶联接口以局向为单位进行管理，而不是IP。 
业务流程
本功能涉及底层承载功能，无业务流程。 
系统影响 : 
不开启IPv6功能，对系统没有影响。开启IPv6能力后，业务性能相比IPv4有所下降。 
特性交互 : 
本功能波及GTP节点管理、GW选择功能，对于GTP节点管理，涉及主用、备用地址切换。对于GW选择功能，需要考虑双方的IP类型支持能力。 
遵循标准 : 
RFC2460,2463,2960,3596,5881 
3GPP TS 23.401: "GPRS enhancements for E-UTRAN access ". 
3GPP TS 24.301:"Non-Access-Stratum (NAS) protocol for Evolved
Packet System (EPS) ". 
3GPPTS36.413: "Evolved Universal Terrestrial Access Network
(E-UTRAN); S1 Application Protocol (S1AP)" 
3GPP TS 29.274: “Evolved General Packet Radio Service (GPRS)
Tunnelling Protocol for Control plane (GTPv2-C)” 
3GPP TS 29.272: " Mobility Management Entity (MME) and Serving
GPRS Support Node (SGSN) related interfaces based on Diameter protocol". 
3GPP TS 29.118: “Mobility Management Entity (MME) –Visitor
Location Register (VLR) SGs interface specification” 
3GPP TS 29.280: “3GPP Sv interface (MME to MSC, and SGSN to
MSC) for SRVCC” 
特性能力 : 
本功能支持IPv6报文收发、分片和重组，支持最大32KB控制面IPv6包。IPv6接口支持BFD、端口聚合（LACP）、VRF。支持IPv6静态路由转发，最大支持10万个路由条目，每个路由支持最多8个下一跳。
AMF、MME、SGSN支持IPv6 ICMP、TCP、UDP、SCTP、DNS应用，支持IPv6及IPv4IPv6双栈的业务接口包括：SBI、N1N2、S1-mme、
S6a/S13、 S11/S10、SGs,、Svr、Gn、Gb、Iu、Gr、Gs、Ga、DNS等接口。
可获得性 : 
版本要求及变更记录
ZXUN-uMAC V7.19.10版本及后续版本。 
License要求
本网元受IPv6 License功能开关控制，只有开关开启，才能支持本功能。 
O&M相关 : 
命令
配置项新增配置项参见表1。表1  新增配置项配置项命令MME GTPC信令地址配置SET MME GTPCSHOW MME GTPC 
安全变量无新增安全变量 
定时器无新增定时器 
软件参数无新增软件参数 
性能统计
无新增计数器 
告警和通知
无新增告警和通知 
业务观察/失败观察
无新增业务观察/失败观察 
话单与计费
本功能与话单和计费无关 
特性配置 : 
配置特性 : 
配置前提
MME本局开启支持IPv6的license。 
MME前后台正常，与邻接网元正常通信。 
MME本局同时配置IPv4和IPv6的GTPC地址。 
AMF本局已配置IPv6的接口地址。 
MME配置过程
使用[SHOW LICENSE]命令，确定本局已支持IPv6的license。
 说明： 
如license不支持IPv6，联系中兴通讯技术支持
升级license。
使用[ADD SCTPIDCFG]命令，配置偶联索引。
使用[SET MME GTPC]，配置MME IPv6 GTPC地址。
AMF 配置过程
N2口支持IPv6
在CommonS_SIG下，使用[ADD SCTP]命令，配置本端IPv6动态偶联地址。
在Namf_MP下，使用[ADD N2SCTPIDCFG]命令，配置AMF使用的动态IPv6偶联标识。
SBI口支持IPv6
在CommonS_HTTP_LB下，使用[ADD CLIENTPROFILE]命令，配置IPv6类型的客户端模板。
在CommonS_HTTP_LB下，使用[ADD SERVERPROFILE]命令，配置IPv6类型的服务端模板。
在Namf_Communication下，使用[ADD SERVICECFG]命令，配置AMF作为服务端IP地址类型为IPv6。
在Namf_Communication下，使用[ADD ASSOCIATED HTTPSERVERPROFILEID]命令，配置AMF相应服务关联IPv6的HTTP服务端模板。
在Namf_MP下，使用[SET DEFAULTHTTPCLIENTID]命令，配置缺省关联的IPv6类型的HTTP客户端模板。
GTPC地址支持IPv6
在Namf_MP下面，使用[SET AMFGTPCADDRCFG]命令，配置AMF IPv6的GTPC地址。
配置实例
数据规划
本例对MME网元IPv6地址规划参见[表1]。
接口类型|IPv6地址
---|---
GTPC地址|2FFF:20:100:0:0:0:0:16
本例对AMF网元IPv6地址规划参见[表2]。
接口类型|IPv6地址
---|---
N2口偶联IP|2FFF:0:100::16/128
AMF GTPC IP|2FFF:20:100::16/128
SBI接口 IP|2FFF:20:200::16/128
MME配置脚本
步骤|命令|说明
---|---|---
1|ADD SCTPIDCFG:SCTPID=1,TYPE=S1APADD SCTPIDCFG:SCTPID=2,TYPE=DIM|配置S1AP和Diameter的偶联索引。
2|SET MME GTPC:IPV6ADDR="2FFF:20:100:0:0:0:0:16"|配置IPv6 GTPC地址。
AMF配置脚本
步骤|命令|说明
---|---|---
1|ADD SCTP:ID=10,LOCPORT=5000,REMPORT=0,VPNID1=0,LOCADDR1=2FFF:0:100::16,VPNID2=0,VPNID3=0,VPNID4=0,ROLE="SVR",INSTRM=16,OUTSTRM=16,MAXRTRY=5,MAXRTO=500,MINRTO=50,INITRTO=100,QOSTYPE="NULL",QOSVALUE=0,HB=500,MAXBURST=0,FIXNH="CLOSE",SCTPMAXRTRYNUM=10,DELAYACK=20,PMTU=0,PRIMARYPATH="REMIP1",BREAKTIME=0,CB=50,MINCWND=0,PLTIMER=10,MPPLTHRD=100,DPLEN="MTU",CHECKSUM="ADAPTIVE",CROSSLINK="CLOSE",SCTPALARM="CONFORM",DROPPKTSTREAM=0,DROPPKTSWITCH="ON",SNDBUFLEN=0,RCVBUFLEN=0,OFCID=0,PROTOCALTYPE=,MPDTHRD=0|配置本端IPv6动态偶联地址。
2|ADD N2SCTPIDCFG:SCTPID=10|配置AMF使用的动态IPv6偶联标识10。
3|ADD CLIENTPROFILE:ID=1,IPADDR=2FFF:20:200::16,STARTPORT=20000,ENDPORT=30000,VPNID=0,CONNNUM=2,CONNELASTIC="SWITCH_ON",RESPBODYMAXLENGTH=204800,RESPTIMER=30,MAXCONCURRENTSTREAMS=1000,KEEPALIVETIMER=30,KEEPALIVESWITCH="SWITCH_ON",HTTPVERSION="HTTP_2"|配置IPv6类型的客户端模板。
4|ADD SERVERPROFILE:ID=1,IPADDR=2FFF:20:200::16,PORT=8080,VPNID=0,REQBODYMAXLENGTH=204800,RESPTIMER=30,MAXCONCURRENTSTREAMS=1000,HTTPVERSION="HTTP_2"|配置IPv6类型的服务端模板。
5|ADD SERVICECFG:SERVICETYPE="COMMUNICATION",VERSION=1,APIVERSION="F40",IPADDRTYPE="IPV6",PRIORITYFLG="INVALID",CAPACITYFLG="INVALID"|配置Communication服务作为服务端IP地址类型为IPv6。
6|ADD ASSOCIATED HTTPSERVERPROFILEID:SERVICETYPE="COMMUNICATION",HTTPSERVERPROFILEID=1|配置Communication服务关联ID为1的IPv6的HTTP服务端模板。
7|SET DEFAULTHTTPCLIENTID:DEFAULTHTTPIPV6ID=1|配置缺省关联ID为1的IPv6类型的HTTP客户端模板。
8|SET AMFGTPCADDRCFG:AMFGTPCIPV6ADDRESS="2FFF:20:100::16"|配置AMF IPv6的GTPC地址。
调整特性 : 
无 
测试用例 : 
无 
常见问题处理 : 
对于SGSN和MME合一局时，SGSN和MME的GTPC地址必须同时配置或不配置IPv6地址，否则传表会失败。
## ZUF-76-05-004 IPv4IPv6双栈 
特性描述 : 
特性描述 : 
术语 : 
本特性不涉及相关术语。 
描述 : 
定义 : 
双栈是指在一台设备上同时启用IPv4协议栈和IPv6协议栈。 
ZXUN uMAC同时支持IPv4和IPv6两种协议栈，从而可以用IPv4或IPv6地址进行数据传输。 
ZXUN uMAC支持UE地址的IPv6和IPv4IPv6双栈功能。 
背景知识 : 
IPv4地址IPv4通常用点分十进制记法书写，例如192.168.0.1，其中的数字都是十进制的数字，中间用实心圆点分隔。一个IPv4地址可以分为网络地址和主机地址两部分，其中网络地址可以使用如下形式描述：192.168.0.0/16，其中斜线后的数字表示网络地址部分的长度是16位，这对应2个字节，即网络地址部分是192.168.0.0。IPv4地址有以下特殊规定：0.0.0.0在没有IP地址的主机启动时使用；255.255.255.255作为通用的广播目的地址；127.X.X.X称为环回地址；仅主机位都为“0”的地址表示该网络本身，主机位都为“1”的地址用作该网络的广播地址；合法的主机IP地址其网络地址和主机地址都不能全“0”或全“1”。 
IPv6地址IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数，共计128位。标准的IPv6地址表达方式，地址中的每个整数都必须表示出来，但起始的0可以不必表示。当出现地址中可能包含一长串的0的情况时，允许用“空隙”来表示这一长串的0。例如，地址2000:0:0:0:0:0:0:1可以被表示为2000::1。在这种方法中，只有当16位组全部为0时才会被两个冒号取代，且两个冒号在地址中只能出现一次。 
应用场景 : 
当网络中IPv4地址资源不足时，可以使用IPv6地址并部署IPv4和IPv6双栈接口实现数据传输。 
客户收益 : 
受益方|受益描述
---|---
运营商|以IPv4和IPv6双栈接口为基础进行网络部署，运营商可以同时获得IPv4地址和IPv6地址，避免进行IPv4地址和IPv6地址之间的NAT转换，同时使得网络中具备更多的IP地址资源，从而解决网络中IP地址资源不足的问题。
移动用户|此特性对终端用户不可见。
实现原理 : 
系统架构 : 
本特性不涉及系统架构。 
协议栈 : 
协议栈如[图1]所示。
图1  IP协议栈
本网元实现 : 
业务接口支持IPv4IPv6双栈AMF、MME、SGSN对于标准协议接口，支持IPv4IPv6双栈地址以AMF为例，AMF各个业务接口的IP地址配置和地址选择策略参加下表。表1  AMF各个业务接口的IP地址配置和地址选择策略业务接口和IP地址配置地址选择策略SBI接口 服务地址每个服务支持配置IPv4和IPv6 类型的IP地址。AMF选择NRF地址时，根据配置的NRF IPv4地址和IPv6地址的优先级顺序来选择IP地址类型。AMF选择其他网元时，针对对方网元类型（比如SMF、PCF、UDM、AUSF等）分配配置地址优先选择策略（IPv4 或者 IPv6），根据优先地址类型过滤NRF解析的IP列表，排除无效地址后，再根据拓扑、权重优先级顺序选择。N2口偶联IP偶联本端地址支持IPv6和IPv4。对方选择IPv6或者IPv4端点创建动态偶联。N26口GTPC IPAMF支持2个GTPC IP配置，分别为IPv4、IPv6 类型。对DNS解析的IP列表排除无效地址后，结合本方配置的GTPC IP类型，根据拓扑、权重优先级顺序选择相同类型的对方IP。如果双方都支持双栈，根据“业务IP双栈时采用的IP类型”开关来进行选择。DNS接口IPDNS客户端地址支持IPv6和IPv4DNS服务器IP和客户端IP成对配置，地址类型相同。 
License控制本功能受IPv6 License功能开关控制，只有开关开启时，配置的IPv6地址才有效。接口板也才支持IPv6业务报文的接收和转发。License功能开关变更，比如开启到关闭，或者关闭到开启，需要重启整局。 
GTP节点管理支持IPv4IPv6双栈AMF、MME、SGSN支持双栈IPv6、IPv4双栈功能，对GTP节点管理功能有波及，不影响其他接口的节点管理，比如偶联接口以局向为单位进行管理，而不是IP。GSN节点之间通过echo消息来进行检活，在双方GTP节点可能支持IPv4 or/and IPv6的情况下，节点管理需要进行扩展。在EPC网络中，MME、SGSN可以携带双栈的控制面地址给GW，GW返回双栈地址给MME。本端在节点管理时，把对方IPv4、IPv6地址作为两个独立的节点进行管理，并且选择一个地址作为主地址，另一个地址作为候选地址。如果主地址链路异常，则判断该承载是否有候选地址，如果没有，则直接回收该承载。如果还有候选地址，则采用后续地址转为主用地址进行通信。如果候选地址的链路也异常了，则MME、SGSN把和该节点相关的承载资源回收。 
UE地址的IPv6和IPv4IPv6双栈功能SGSN/MME支持UE地址的IPv6和IPv4IPv6双栈功能。以MME为例，在PDN session建立过程中，MME根据UE请求和迁移信息，来决定PDN type（IPv4、IPv6或IPv4IPv6双栈），PGW根据PDN type分配对应的UE地址。 
业务流程 : 
本功能涉及底层承载功能，无业务流程。 
系统影响 : 
不开启IPv6功能，对系统没有影响。 
开启IPv6能力后，业务性能相比不开启有所下降。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称|章节
---|---
IETF|RFC791 Internet ProtocolRFC2373 IP Version 6 Addressing Architecture
3GPP|3GPP TS 23.401: "GPRS enhancements for E-UTRAN access ".3GPP TS 24.301:"Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS) ".3GPPTS36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)"3GPP TS 29.274: “Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C)”3GPP TS 29.272: " Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol".3GPP TS 29.118: “Mobility Management Entity (MME) –Visitor Location Register (VLR) SGs interface specification”3GPP TS 29.280: “3GPP Sv interface (MME to MSC, and SGSN to MSC) for SRVCC”
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.10|首次发布。
License要求 : 
本网元受IPv6 License功能开关控制，只有开关开启，才能支持本功能。 
对其他网元的要求 : 
UE|BSS/RAN|SGSN|PGW|HSS
---|---|---|---|---
-|√|√|√|√
UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
UE|NR|AMF|SMF|UPF
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
配置项表5  AMF GTPC地址配置配置项命令AMF GTPC地址配置SET AMFGTPCADDRCFGSHOW AMFGTPCADDRCFG表6  默认HTTP客户端模板标识配置配置项命令默认HTTP客户端模板标识配置SET DEFAULTHTTPCLIENTIDSHOW DEFAULTHTTPCLIENTID表7  客户端模板配置配置项命令客户端模板配置ADD CLIENTPROFILESET CLIENTPROFILEDELETE CLIENTPROFILESHOW CLIENTPROFILE 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
当网络中IPv4地址资源不足时，可以使用IPv6地址并部署IPv4和IPv6双栈接口实现数据传输。 
配置前提 : 
AMF支持同时配置IPv4和IPv6的GTPC地址 
AMF与邻接NF正常通信 
配置过程 : 
执行[SET AMFGTPCADDRCFG]命令，配置AMF GTPC地址。
执行[SET DEFAULTHTTPCLIENTID]命令，配置默认HTTP客户端模板标识。
配置实例 : 
数据规划 : 
接口类型|IPV6地址
---|---
GTPC|2FFF:20:100::16/128
HTTP|2FFF:0:100::16/128
配置步骤 : 
步骤|命令|说明
---|---|---
1|SET DEFAULTHTTPCLIENTID:DEFAULTHTTPIPV4ID=1,DEFAULTHTTPSIPV4ID=1,DEFAULTHTTPIPV6ID=1,DEFAULTHTTPSIPV6ID=1|配置默认HTTP客户端模板标识
2|ADD CLIENTPROFILE:ID=2,IPV4ADDR="2FFF:0:100::16",STARTPORT=20000,ENDPORT=30000,VPNID=0,CONNNUM=2,CONNELASTIC="SWITCH_ON",RESPBODYMAXLENGTH=10240,RESPTIMER=30,MAXCONCURRENTSTREAMS=1000,KEEPALIVETIMER=30,KEEPALIVESWITCH="SWITCH_ON",HTTPVERSION="HTTP_2",TLSCERTID=0|客户端模板配置
3|SET AMFGTPCADDRCFG:AMFGTPCADDRESS="2FFF:20:100::16",AMFN26VRF=1|AMF GTPC地址配置
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
无。 
常见问题处理 : 
无。 
## ZUF-76-05-005 ACL 
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
ZXUN uMAC支持ACL（Access Control List，访问控制列表）来实现包过滤功能。
ACL是一种IP包过滤技术，通过对IP报文的源地址、报文目的地址、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有意义）等信息对照ACL规则数据库进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，动作包括：允许（Permit）、拒绝（Deny）等。 
背景知识
信息点间通信和内外网络的通信都是企业网络中必不可少的业务需求，但是为了保证内网的安全性，需要通过安全策略来保障非授权用户只能访问特定的网络资源，从而达到对访问进行控制的目的。简而言之，ACL可以过滤网络中的流量，是控制访问的一种网络技术手段。 
访问控制列表（ACL）是一系列有顺序的规则组的集合，每个规则组中可以定义多个规则，这些规则根据数据包的源地址、目的地址、端口号等来描述。 
这些规则是由一系列有顺序的“permit | deny”语句组成，是一个匹配选项的集合，由用户根据不同业务进行选择配置。ACL通过这些规则对数据包进行分类，ZXUN uMAC根据这些规则判断哪些数据包可以接收，哪些数据包需要拒绝，从而达到访问控制的目的。
ACL的匹配顺序一个访问控制列表可以由多条规则组成，ZXUN uMAC采用按照用户配置ACL的规则的先后进行匹配。 
ACL的主要功能ACL的主要功能就是一方面保护资源节点，阻止非法用户对资源节点的访问，另一方面限制特定的用户节点所能具备的访问权限。 
应用场景 : 
ZXUN uMAC通过ACL过滤来限制用户面报文和控制面信令，来增加组网的安全性。
客户收益 : 
收益者|收益描述
---|---
运营商|可以限制网络流量，从而提高网络性能，实现网络隔离和抗攻击安全功能，增加网络访问的安全性。
移动终端用户|对终端用户不可见。
实现原理 : 
系统架构
无。 
涉及的网元
不涉及其他网元。 
协议栈
无。 
本网元实现
ZXUN uMAC支持将IPv4 ACL应用在接口上，通过对IPv4报文的源目的IP、源目的端口号、IP协议类型等属性进行解析，对匹配到ACL规则的IPv4报文采取相应的动作（允许通过或丢弃）。
接口ACL匹配过程ACL的匹配结果包括允许（permit）和拒绝（deny）两种，ZXUN uMAC对报文解析出源IP地址、目的IP地址、源端口号、目的端口号、IP协议类型等属性，并去匹配已经配置的ACL，如果能获取到匹配结果，则按照此条规则对报文进行过滤，决定对其进行转发还是将其丢弃。如果没有获取到匹配结果，则不过滤此报文。如果匹配结果是允许（permit），则转发报文。如果匹配结果是拒绝（deny），则丢弃报文。 
接口ACL过滤功能的报文方向接口ACL过滤功能支持对接口报文的入向和出向这两个方向分别进行过滤。入向过滤：在接口接收到报文之后，对报文进行深入处理之前，根据ACL的匹配结果决定是转发此报文还是丢弃此报文。出向过滤：在接口报文发送之前，对报文进行以太网头封装后，根据ACL的匹配结果决定是转发此报文还是丢弃此报文。 
业务流程
无。 
系统影响 : 
接口使用ACL规则过滤会导致接口转发报文的效率降低。 
应用限制 : 
ZXUN uMAC支持的ACL过滤功能仅对三层的IP报文进行限制，对于二层报文不限制。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
本特性遵循的标准为： 
RFC 4314 draft-ietf-imapext-2086upd 
特性能力 : 
全局最多支持配置4K个IPv4 ACL group和32K个IPv4 ACL规则，每个IPv4 ACL group最多能配置32K个IPv4 ACL规则。 
全局最多支持配置1K个IPv6 ACL group和32K个IPv6 ACL规则，每个IPv6 ACL group最多能配置32K个IPv6 ACL规则。 
可获得性 : 
版本要求及变更记录
ZXUN-uMAC V7.19.10版本及后续版本。 
License要求
本特性无License控制。 
对其他网元的要求
无。 
工程规划要求
无。 
O&M相关 : 
配置项该特性不涉及命令配置的变化。 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计
新增的性能计数器参见下表。 
测量类型名称|性能计数器名称
---|---
PORT ACL性能测量|C558560003 接收字节数(字节)
C558560004 接收帧数(包)|PORT ACL性能测量
C558560005 接收字节速率(比特/秒)|PORT ACL性能测量
C558560006 发送字节数(字节)|PORT ACL性能测量
C558560007 发送帧数(包)|PORT ACL性能测量
C558560008 发送字节速率(比特/秒)|PORT ACL性能测量
告警和通知
该特性不涉及告警和通知消息的变化。 
业务观察/失败观察
该特性不涉及业务观察/失败观察的变化。 
话单与计费
该特性不涉及话单与计费的变化。 
特性配置 : 
该功能属于基本功能，无需特别配置，只要完成初始配置即可。 
## ZUF-76-05-006 BFD 
特性描述 : 
特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
BFD是一种双向转发检测机制，可以提供毫秒级的检测，可以实现链路的快速检测。BFD通过与上层路由协议联动，实现路由的快速收敛，保证业务的连续性。
背景知识 : 
网络设备一个越来越重要的特征是，要求对相邻系统之间通信故障进行快速检测，这样在出现故障时可以更快的建立起替代通道或倒换到其他链路。 
BFD协议的出现，为上述问题提出了一种解决方案。BFD能够在系统之间的任何类型通道上进行故障检测，这些通道包括直接的物理链路，虚电路，隧道，MPLS，LSP，多跳路由通道，以及非直接的通道。
同时正是由于BFD实现故障检测的简单、单一性，致使BFD能够专注于转发故障的快速检测，帮助网络以良好QoS实现语音、视频及其他点播业务的传输，从而帮助服务提供商基于IP网的实现，为客户提供所需的高可靠性、高适用性VoIP及其他实时业务。
应用场景 : 
当ZXUN uMAC与外部路由或者交换设备连接，对于丢包和延迟比较敏感时，需要配置BFD。一般会与静态路由，OSPF，BGP等路由协议配合开启BFD。
客户收益 : 
受益方|受益描述
---|---
运营商|可实现毫秒级的路由切换，提供网络的稳定性，可靠性。加快路由的快速收敛，减少核心网络的流量振荡。
终端用户|该特性对终端用户不可见。
实现原理 : 
系统架构 : 
不涉及。 
涉及的网元 : 
该特性由ZXUN uMAC自身完成，不需要与其他网元交互。
本网元实现 : 
BFD是一个简单的Hello协议，与路由协议的Hello机制类似，只不过更简洁更通用。
建立BFD会话的两个系统之间周期性的互发报文，如果在一个商定的时间段内没有收到对端报文，就认为和对端的通信通道出现故障，BFD会话Down，并通知上层协议重新选路。 
为了减少设备负荷，BFD还设计了一些特殊的应用方式，在这些方式下，可以减少BFD报文发送，或者不必周期性的发送BFD报文，只在需要的时候才发送。 
BFD的主要目标为： 
 
提供一种低负载的，快速检测出在两个相邻的转发引擎间的故障，包括接口，数据链路，更进一步是转发引擎本身的失效。 
 
提供一种单一的检测机制，应用于各种媒介上，任意的协议层。BFD是在与下一跳的转发引擎通信中来检测失效，倾向于在一个系统转发引擎的一些部分中工作，转发引擎和控制引擎是分离的。 
 
这不但将协议绑定于转发平面，而且将协议从路由协议引擎（控制层面）中分离（使之在无中断转发中起作用），还能在控制引擎中运行。 
BFD提供两个各种系统之间的失效检测，包括直联物理链路，虚电路，隧道，MPLS LSP,多跳路由路径。 
BFD有两种操作模式，异步模式和查询模式。只支持BFD异步模式，不支持查询模式，不支持回声检测（echo） 
报文格式如[图1]所示。
图1  BFD报文格式
 
Vers：协议的版本号，协议版本为1。 
 
Diag：本地协议最后一次从up状态转换到其他状态的原因。 
 
State（Sta）：BFD 会话当前状态，取值为：0 代表AdminDown，1 代表Down， 2 代表Init，3
代表Up。 
 
Demand（D）：设置为1，表示发送协议希望操作在查询模式；设置为0，表示发送协议不区分操作在查询模式，或者表示发送协议不能操作在查询模式。 
 
Poll（P）：设置为1，表示发送协议请求进行连接确认，或者发送请求参数改变的确认；设置为0，表示发送协议不请求确认。 
 
Final（F）：设置为1，表示发送协议响应一个接收到P 比特为1 的BFD 控制报文；设置为0，表示发送协议不响应一个P
比特为1 的BFD 控制报文。 
 
BFD实现如[图2]所示。
图2  BFD原理示意图
检测链路出现故障,BFD检测到链路故障，拆除BFD邻居会话； 
BFD通知本地路由协议（比如OSPF进程)BFD邻居不可达； 
本地路由进程（比如OSPF）中断邻居关系或者删除对应的路由表项目； 
数据立即切换到另一个路由器。 
业务流程 : 
不涉及。 
系统影响 : 
该特性不涉及系统影响。 
应用限制 : 
与ZXUN uMAC连接的设备需要支持BFD功能，ZXUN uMAC不能单独开启BFD功能。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准类别|标准名称
---|---
IETF|RFC 5880 Bidirectional Forwarding Detection (BFD)
特性能力 : 
名称|指标
---|---
整局支持配置BFD最大个数|1000
BFD会话支持的检测时长|10–990ms
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
bfd|进入BFD会话配置模式。
session|为BFD配置会话信息。
命令名称|修改说明
---|---
ip route|IPv4静态路由配置关联BFD。
ipv6 route|IPv6静态路由配置关联BFD。
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
编号|告警和通知
---|---
1|300501
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
运营商在部署分组交换网，需要快速检测链路状态，则建议打开BFD检测。有助于路由的快速收敛，防止核心网络的流量震荡。 
配置前提 : 
各个端口正常。 
配置过程 : 
步骤|配置说明|配置步骤
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置实例化BFD|进入BFD配置模式。bfd配置BFD会话。sessionbfd配置模式下，进入接口模式。interface配置bfd会话参数。time-negotiation
3|配置静态路由BFD|配置静态路由，开启bfd。ip route
4|配置OSPF路由触发BFD|配置ospf，开启bfd。router ospf配置ospf，开启bfd。bfd
5|配置BGP路由触发BFD|配置BGP路由，开启bfd。router bgp <as number>BGP模式下开启bfd。neighbor fall-overbfd
配置实例 : 
场景说明 : 
静态路由中关联BFD检测，用于快速检测链路状态。 
OSPF中关联BFD检测，用于快速检测链路状态。 
BGP中关联BFD检测，用于快速检测链路状态。 
数据规划 : 
静态路由目的地址|下一跳地址|BGP邻居地址|OSPF域area|OSPF协议进程号
---|---|---|---|---
172.20.108.1|172.20.130.214|1.1.1.213|0|1
配置步骤 : 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置静态路由并开启BFD，对端也做同样的配置|ZXROSNG(config)#ip route 172.20.108.1 255.255.255.255 172.20.130.214bfd enable
步骤|说明|操作
---|---|---
1|启动或者进入已经有的OSPF进程|ZXROSNG(config)#router ospf 1
2|关联BFD|ZXROSNG(config-ospf-1)#bfd area 0
步骤|说明|操作
---|---|---
1|启动或者进入已经有的BFD进程|ZXROSNG(config)#router bgp 100
2|如果是多跳，需要配置multihop开关(可选)|ZXROSNG(config-bgp-100)#neighbor 1.1.1.213 ebgp-multihop
3|关联开启BFD|ZXROSNG(config-bgp-100)#neighbor 1.1.1.213 fall-over bfd
调整特性 : 
不涉及。 
测试用例 : 
测试项目|BFD功能
---|---
测试目的|验证BFD功能，能正常进行BFD检测。
预置条件|基础配置完成。配置BFD功能。
测试过程|修改BFD的检测时间，查看BFD状态。
通过准则|检测时间正确，BFD状态为up。
测试结果|–
常见问题处理 : 
不涉及。 
## ZUF-76-05-007 DSCP映射 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
DSCP映射，指根据QoS在报文IP头标记特定的DSCP值，用于网络QoS处理。
ZXUN uMAC支持用户面报文和控制面信令进行DSCP映射，承载网和接收设备可能会根据不同的优先级处理标记的IP报文，从而实现QoS功能。 
背景知识 : 
IETF于1998年12月发布了Diff-Serv（Differentiated Service）的QoS分类标准。Diff-Serv体系规定，每一个传输报文在网络中区分为不同的类别，分类信息包含在IP报文头中，Diff-Serv体系使用了数据包IP头部的TOS标识字节中的高6位bit，通过编码值来区分优先级，即DSCP。DSCP有6个bit，取值范围为0~63，可以定义为64个等级（优先级）。IPv4报文头中的DSCP如[图1]所示，IPv6报文头中的DSCP如[图2]所示。
图1  IPv4报文头中的DSCP
图2  IPv6报文头中的DSCP
在遵循Diff-Serv体系的网络中，各交换机和路由器对包含同样分类信息的报文采取同样的传输服务策略，对包含不同分类信息的报文采取不同的传输服务策略。 
网络上的主机、交换机、路由器或者其它网络设备可以基于不同的应用策略或者基于不同的报文内容为报文赋予类别信息。 
交换机或路由器根据报文所携带的类别信息，可以为各种业务流提供不同的传输优先级，为某种业务流预留带宽，适当的丢弃一些重要性较低的报文，或者采取其他一些操作。这种行为在Diff-Serv体系中被称作PHB。
Diff-Serv定义了DSCP与PHB的映射关系，参见[表1]。
DSCP|PHB|说明
---|---|---
101110|EF|加速转发，绝对QoS，提供低丢包率、低延时和确保带宽的服务。
001xxx|AF1|保证转发，介于EF和BE之间，允许在整体流量不超过预定速率前提下以更高的可能性转发报文。AF划分4个等级，分别为AF1、AF2、AF3、AF4。每一个级别又可以细划分为三种优先级：xxx=010，低级xxx=100，中级xxx=110，高级,
010xxx|AF2|保证转发，介于EF和BE之间，允许在整体流量不超过预定速率前提下以更高的可能性转发报文。AF划分4个等级，分别为AF1、AF2、AF3、AF4。每一个级别又可以细划分为三种优先级：xxx=010，低级xxx=100，中级xxx=110，高级,
011xxx|AF3|保证转发，介于EF和BE之间，允许在整体流量不超过预定速率前提下以更高的可能性转发报文。AF划分4个等级，分别为AF1、AF2、AF3、AF4。每一个级别又可以细划分为三种优先级：xxx=010，低级xxx=100，中级xxx=110，高级,
100xxx|AF4|保证转发，介于EF和BE之间，允许在整体流量不超过预定速率前提下以更高的可能性转发报文。AF划分4个等级，分别为AF1、AF2、AF3、AF4。每一个级别又可以细划分为三种优先级：xxx=010，低级xxx=100，中级xxx=110，高级,
000000|BE|尽力而为，比如浏览网页的业务。
应用场景 : 
承载网和接收设备可能会根据不同的优先级处理标记DSCP的IP报文，从而实现QoS功能。 
客户收益 : 
受益方|受益描述
---|---
运营商|有助于运营商针对不同的用户和业务提供不同优先级的QoS转发策略和控制，在网络拥塞时，高优先级的用户或高优先级的业务可以及时的处理，保证收益最大化。
移动用户|在网络拥塞情况下，依然可以保证VoLTE等高优先级业务的体验不受影响。
实现原理 : 
系统架构 : 
本特性涉及的系统架构如[图3]所示。
图3  DSCP映射系统架构
涉及的网元 : 
网元名称|网元作用
---|---
AMF/MME/SGSN|用户面报文和控制面信令发送前，在IP报文头标记特定的DSCP值。
其他网元、承载网络的路由交换设备|根据报文IP头中的DSCP值，映射成优先级，进行QoS处理。
协议栈 : 
本特性涉及的IP协议栈如[图4]所示。
图4  协议栈
本网元实现 : 
AMF/MME/SGSN的DSCP映射的功能说明参见[表2]
DSCP映射功能|说明
---|---
Gn、Iu、Gb接口用户面报文DSCP映射|通过Gn、Iu和Gb接口发送用户面报文时，SGSN在上行/下行流中将该PDP的QoS参数映射为DSCP，并在Iu、Gn接口GTP报文IP头部，或者Gb接口IPNS报文的IP头部中标记DSCP。
SCTP信令的DSCP映射|AMF/MME/SGSN支持配置各个SCTP链路的DSCP（对于S1、N2口动态偶联，则支持按服务器端点配置DSCP），并在发出的SCTP信令的IP报头中标记DSCP。
GTP信令的DSCP映射|AMF/MME/SGSN支持配置GTP信令的DSCP，并在发出的GTP信令的IP报文头部标记DSCP。
Gb信令的DSCP映射|SGSN支持配置Gb下行层3信令（即于Gb接口投递的GMM、SM、SMS的NAS信令报文）的DSCP、Gb下行承载信令（LLC、BSSGP、IPNS层的信令报文）的DSCP，并在发出的Gb信令的IPNS报头中标记DSCP。
Ga信令的DSCP映射|SGSN支持配置Ga口信令DSCP，并在发出的Ga口信令的IP报头中标记DSCP。
ETSI LI的DSCP映射|AMF/MME/SGSN支持配置ETSI LI1/ETSI LI2口的DSCP，SGSN支持配置ETSI LI3口的DSCP，并在发出的ETSI LI1/ETSI LI2/ETSI LI3口报文的IP报头中标记DSCP。
DNS接口的DSCP映射|AMF/MME/SGSN支持配置DNS信令的DSCP，并在发出的DNS信令的IP报头中标记DSCP。
SBI HTTP信令的DSCP映射|AMF支持配置HTTP客户端模版的DSCP、HTTP服务器端模版的DSCP，并在发出的HTTP信令的IP报头中标记DSCP。
EMS+信令的DSCP映射|AMF/MME/SGSN支持配置EMS+信令的DSCP，并在发出的EMS+信令的IP报头中标记DSCP。
业务流程 : 
本特性为通用IP包转发，无特定的业务流程。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
类别|标准编号|标准名称
---|---|---
IETF RFC|2474|Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
02|V7.21.40|新增基于接口类型设置DSCP标签功能。
01|V7.19.10|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
UE|RNC/BSC|GGSN|HLR|MSC
---|---|---|---|---
-|√|√|√|√
UE|eNodeB|SGW|HSS|CG
---|---|---|---|---
-|√|√|√|√
UE|NR|SMF|UDM|PCF|NRF
---|---|---|---|---|---
-|√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
配置项|命令
---|---
AMF DSCP映射配置|SET MP SIG DSCP
SHOW MP SIG DSCP|AMF DSCP映射配置
MME/SGSN DSCP映射配置|SET SIG DSCP
SHOW SIG DSCP|MME/SGSN DSCP映射配置
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
通过该配置过程，可以完成对接口信令报文或用户数据报文的DSCP配置，后续各个对应接口的信令报文或用户数据报文IP承载层的DSCP值就为本配置的DSCP值，实现信令报文和用户数据报文的优先级配置。 
配置前提 : 
AMF、MME、SGSN存在相应的接口，且对端网元支持DSCP映射功能。 
配置过程 : 
###### AMF配置过程 
执行 [SET MP SIG DSCP] 命令， 配置DNS接口信令、EMS+信令、ETSI LI1/ETSI LI2口信令和GTP信令的DSCP。
执行 [SET CLIENTPROFILE] 命令，配置SBI HTTP信令的DSCP。
执行 [SET SCTP] 命令，配置SCTP链路的DSCP。
###### MME/SGSN配置过程 
执行 [SET SIG DSCP] 命令， 配置以下接口的DSCP值：GB下行层三信令DSCP，GB下行承载信令DSCP，GTP信令DSCP，Ga口信令DSCP，ETSI LI1/ETSI LI2口信令DSCP，ETSI LI3口信令DSCP，IWS S102口信令DSCP，S102口信令DSCP，DNS信令DSCP，EMS+信令DSCP。
配置实例 : 
场景说明 : 
全网规划接口信令报文和用户数据报文的DSCP数值，如下： 
AMF
支持DNS信令DSCP配置，并在发出的DNS信令的IP报头中标记DSCP。 
支持配置EMS+信令的DSCP，并在发出的EMS+信令的IP报头中标记DSCP。 
支持配置ETSI LI1/ETSI LI2口的DSCP，并在发出的ETSI LI1/ETSI LI2口报文的IP报头中标记DSCP。 
支持配置GTP信令的DSCP，并在发出的GTP信令的IP报文头部标记DSCP。 
支持配置HTTP客户端模版的DSCP、HTTP服务器端模版的DSCP，并在发出的HTTP信令的IP报头中标记DSCP，或校验收到的消息中的DSCP值。 
支持配置各个SCTP链路的DSCP（对于N2口动态偶联，则支持按服务器端点配置DSCP），并在发出的SCTP信令的IP报头中标记DSCP。 
MME/SGSN
支持配置GB下行层三信令DSCP，应用于Gb接口投递的GMM、SM、SMS的NAS信令报文。 
支持配置GB下行承载信令DSCP，应用于Gb接口投递的LLC、BSSGP、IPNS的信令报文。 
支持配置Gn接口的信令报文的DSCP值。 
支持配置Ga接口、ETSI LI1/ETSI LI2接口、ETSI LI3接口的DSCP值。 
支持配置IWS S102口信令DSCP、S102口信令DSCP、DNS信令DSCP、EMS+信令DSCP。 
数据规划 : 
配置项|参数名称|取值
---|---|---
AMF DSCP映射配置|DNS信令DSCP|10
EMS+信令DSCP|AMF DSCP映射配置|11
ETSI LI1/ETSI LI2口信令DSCP|AMF DSCP映射配置|12
GTP信令DSCP|AMF DSCP映射配置|13
AMF HTTP模板配置|编号|1
DSCP标签值|AMF HTTP模板配置|46
SCTP偶联配置|SCTP标识|1
QoS优先级方式|SCTP偶联配置|DSCP
QoS优先级值|SCTP偶联配置|32
MMESGSN DSCP映射配置|GB下行层三信令DSCP|1
GB下行承载信令DSCP|MMESGSN DSCP映射配置|2
GTP信令DSCP|MMESGSN DSCP映射配置|3
Ga口信令DSCP|MMESGSN DSCP映射配置|4
ETSI LI1/ETSI LI2口信令DSCP|MMESGSN DSCP映射配置|5
ETSI LI3口信令DSCP|MMESGSN DSCP映射配置|6
IWS S102口信令DSCP|MMESGSN DSCP映射配置|7
S102口信令DSCP|MMESGSN DSCP映射配置|8
DNS信令DSCP|MMESGSN DSCP映射配置|9
EMS+信令DSCP|MMESGSN DSCP映射配置|10
配置步骤 : 
步骤|说明|操作
---|---|---
1|配置AMF DNS接口信令、EMS+信令、ETSI LI1/ETSI LI2口信令和GTP信令的DSCP。|SET MP SIG DSCP:DNSDSCP=10,EMSDSCP=11,X1X2DSCP=12,GTPDSCP=13
2|配置AMF SBI HTTP信令的DSCP。|ADD CLIENTPROFILE:ID=1,IPADDR="2.2.2.2",STARTPORT=10000,ENDPORT=60000,HTTP2_DSCP=46ADD SERVERPROFILE:ID=1,IPADDR="1.1.1.1",PORT=8080,HTTP2_DSCP=46
3|配置AMF SCTP链路的DSCP。|SET SCTP:ID=1,QOSTYPE="DSCP",QOSVALUE=32
4|配置MME/SGSN接口信令的DSCP。|SET SIG DSCP:GBNASSIGDSCP=1,GBASSIGDSCP=2,GNGTPSIGDSCP=3,GADSCP=4,X1X2DSCP=5,X3DSCP=6,IWSS102DSCP=7,S102DSCP=8,DNSDSCP=9,EMSDSCP=10
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|AMF支持GTP信令的DSCP
---|---
测试目的|验证AMF的GTP信令中携带正确的DSCP值
预置条件|AMF支持N26接口功能。DSCP映射配置中，GTP信令DSCP设置为48。
测试过程|UE接入5G网络。UE移动到4G网络覆盖范围，发起5G到4G切换流程。
通过准则|Forward Relocation Request和Forward Relocation Complete Ack携带有效DSCP值（48）。
测试结果|-
测试项目|AMF支持EMS+信令的DSCP
---|---
测试目的|验证AMF的EMS+信令中携带正确的DSCP值
预置条件|开启EMS+功能。配置EMS+ DSCP值为12。
测试过程|UE接入5G网络。UE发起业务流程。
通过准则|AMF上报的EMS+消息中，携带DSCP值为12。
测试结果|-
测试项目|MME支持GTP信令的DSCP
---|---
测试目的|验证MME的GTP信令中携带正确的DSCP值
预置条件|MME支持N26接口功能。DSCP映射配置中，GTP信令DSCP设置为48。
测试过程|UE接入4G网络。UE移动到5G网络覆盖范围，发起4G到5G切换流程。
通过准则|Forward Relocation Request和Forward Relocation Complete Ack携带有效DSCP值（48）。
测试结果|-
测试项目|MME支持EMS+信令的DSCP
---|---
测试目的|验证MME的EMS+信令中携带正确的DSCP值
预置条件|开启EMS+功能。配置EMS+ DSCP值为12。
测试过程|UE接入4G网络。UE发起业务流程。
通过准则|MME向EMS+上报的信令中，携带DSCP值为12。
测试结果|-
常见问题处理 : 
无。 
## ZUF-76-05-008 UDP/TCP 
概述 : 
UDP/TCP是互联网协议的核心组成部分。 
UDP提供基于数据报（消息）方法的不可靠服务。 
TCP提供可靠有序的基于字节流的数据传输。 
业务端口包括源端口和目的端口，用于在UDP和TCP的应用层业务之间划分数据报。 
客户收益 : 
UDP适合于时间敏感的应用，因为丢弃报文的优先级高于等待延迟的报文。UDP的无状态特性有助于服务器迅速响应来自大量客户端的查询。 
TCP适合在网络中发送大量数据。应用程序不需要将数据分割成IP大小的碎片。TCP处理IP详细信息。TCP优化是为了准确传递而不是及时传递。 
说明 : 
UDP采用简单的传输模型，没有隐式握手对话，以提供可靠性、排序或数据完整性。UDP允许ZXUN
uMAC发送消息（如GTP），不要求先前的通信建立特殊的传输通道或数据路径。 
ZXUN
uMAC使用UDP承载信令消息（如GTP），并在控制面和媒体面提供高效转发。 
TCP提供可靠的流传输服务，保证数据流从一个主机传输到另一个主机，不会出现数据重复或丢失。 
ZXUN uMAC可以使用TCP作为合法拦截数据和AMF HTTP数据的传输协议。 
基于UDP协议的接口如下：Gb、Gn、S10、S11、Sv等。 
基于TCP协议的接口如下： 
ETSI LI1/ETSI LI2/ETSI LI3控制面信令 
AMF HTTP/2 
## ZUF-76-05-009 SCTP 

概述 : 
SCTP（流控制传输协议）是一种传输层协议，其作用与TCP（传输控制协议）和UDP（用户数据报协议）这些主流协议类似。该协议提供了一些相同的业务特性：像UDP一样以消息为导向，像TCP一样通过拥塞控制确保对消息进行可靠、有序的传输。 
客户收益 : 
SCTP提供可靠的数据传输，且不受TCP的限制。 
ZXUN
uMAC支持SCTP为ZXUN uMAC与其他节点之间的关键信号消息提供可靠和安全的传输机制。 
说明 : 
基于消息的多流：SCTP应用向SCTP传输层提交将以消息（字节组）形式传输的数据。多流是指SCTP能够同时传输多个独立的数据块流。 
SCTP协议的特点如下： 
多归属是指连接的一个或两个端点可以由一个以上的IP地址组成的功能，用于实现冗余网络路径之间的透明倒换。 
相对于TCP字节流的数据传输，在独立码流内传输块可以消除不必要的头端阻塞。 
路径选择和监控选择一个主数据传输路径，并测试传输路径的连通性。 
验证和确认机制防止泛洪攻击，并提供关于数据块重复或缺失的通知。 
SCTP设计的特点是为了提高安全性，如4路握手（相对于TCP3路握手），防止SYN泛洪攻击，以及利用大量cookie进行关联验证和真实性验证。 
基于SCTP协议的接口如下：Iu、Gr、Gs、S1、S6a、SGs、N1、N2等。 
## ZUF-76-05-010 GRE 

概述 : 
GRE（通用路由封装）采用Tunnel（隧道）技术将专用的IP报文封装在含有GRE报头的公共IP报文中。GRE功能支持在ZXUN
uMAC和外部主机或路由器（如S11或Gn接口）之间使用隧道。这种隧道传输技术在不同的内部网络之间实现了流量隔离。 
如RFC1701、RFC1702、RFC2784、RFC2890所述，ZXUN
uMAC支持GRE功能。 
客户收益 : 
GRE隧道可实现网络流量隔离。 
GRE隧道功能为操作员节省了IP地址空间。同时，GRE隧道功能可将大量的不同专用IP地址报文封装在单个公共IP隧道中，因此含有这些专用IP地址的报文和消息可以通过公共GRE隧道和Internet访问远程专用网络。 
这些隧道技术独立于用于帧传输的任何底层数据链路协议。因此，在虚拟路由转发的基础上，ZXUN uMAC很容易通过通用骨干连接到业务提供商的远程节点或网络。 
说明 : 
ZXUN uMAC支持GRE隧道，而且可以在ZXUN uMAC和专用网络网关之间创建GRE隧道。 
GRE是一种协议，用于将任意网络层协议封装在另一个任意网络层协议之上。GRE被记录在RFC 1701和RFC 1702中，并在RFC
2784和RFC 2890上重新定义。但是，封装风格保持不变。RFC 1701和RFC 2784描述了如何将任意报文封装在GRE报头中，以及如何将生成的GRE报文封装在任意协议中并转发。RFC
1702描述了如何将IP报文封装在GRE报头中，以及如何将GRE报文封装在IP报文中并转发。其结果是一个IP隧道。 
GRE是一种简单而通用的隧道技术。不仅专用的IP报文可以封装在含有GRE报头的公共IP报文中，二层报文以及IP组播也可以封装在隧道中。但是，GRE不支持任何常见的隧道安全技术，比如鉴权、授权和加密。 
## ZUF-76-05-011 HTTP/SBI 
特性描述 : 
特性描述 : 
术语 : 
术语|含义
---|---
HTTP|超文本传输协议
HTTP/2|HTTP协议2.0版本
HTTP/1.1|HTTP协议1.1版本
HTTPLB|HTTP负载均衡组件
SBI|服务化接口
URI|统一资源标识符
描述 : 
定义 : 
超文本传输协议（HTTP，HyperText Transfer Protocol）是互联网上应用最为广泛的一种网络协议。所有的万维网上传输的文件都必须遵守这个标准。设计HTTP最初的目的是为了提供一种发布和接收HTML页面的方法。 
HTTP/2 （原名HTTP/2.0）即超文本传输协议 2.0，是下一代HTTP协议，基于RFC 7540 。主要增强了如下功能： 多路复用请求； 对请求划分优先级； 压缩HTTP头； 服务器推送流（即Server Push技术）。 
背景知识 : 
5GC中所有NF都统一使用HTTP/2作为SBI（服务化接口）的标准协议，各NF内有多种不同类型的NFS需要处理HTTP协议报文。 
本特性就是把HTTP协议报文处理独立出来，以便使各业务NFS做到不需要关心HTTP协议的处理细节。 
当收到外部NF的HTTP协议请求报文时，HTTPLB模块通过调用各业务NFS的分发库，把HTTP协议报文发给需要处理的业务NFS。 
应用场景 : 
在5G核心网内部，作为AMF和其它各NF的SBI接口的HTTP/2协议报文标准处理组件。 
客户收益 : 
受益方|受益描述
---|---
运营商|本特性是5GC网元必备的基础特性
移动用户|本特性是5GC网元必备的基础特性
实现原理 : 
系统架构 : 
5GC核心网组网图如[图1]所示。
各NF之间以“N+小写的NF名称”命名的接口都是SBI接口，都统一使用HTTP/2作为SBI（服务化接口）的标准协议。例如Namf，Nnssf等。 
图1  5G核心网系统架构
涉及的网元 : 
基本协议不涉及具体网元的功能。 
协议栈 : 
协议栈如[图2]所示。
图2  SBI协议栈
本网元实现 : 
基本协议不涉及具体网元的功能。 
业务流程 : 
HTTP正向代理
HTTP正向代理，作用是收到同一个NF内的其他业务NFS发来的业务请求时，把该请求编码成HTTP请求发送给对端NF。 
业务流程如下。 
HTTPLB组件收到同一个NF内其他业务NFS发来的业务请求。 
HTTPLB组件根据业务请求中携带的协议版本号，把业务请求编码成HTTP/2或HTTP/1.1请求。 
HTTPLB根据业务请求的对端IP地址和端口，查询是否已经存在可用的TCP或TLS连接，如果存在，则通过已有的连接把HTTP请求发送给对端NF。 
HTTP反向代理
HTTP反向代理，作用是收到对端NF发来的HTTP请求时， 首先把请求解码成内部消息，然后根据HTTP请求携带的服务名，把内部消息发送给同一个NF内的被请求的业务NFS。 
业务流程如下。 
HTTPLB组件收到对端NF发来的HTTP请求。 
HTTPLB组件根据HTTP请求的协议版本号，把该HTTP/2或HTTP/1.1请求解码成内部消息。 
HTTPLB根据HTTP请求携带的服务名，把内部消息发送给同一个NF内的被请求的业务NFS。 
TCP连接管理
TCP连接管理是指创建和维护两个NF之间的TCP连接，以及发送HTTP请求时的连接选择。 
业务流程如下。 
作为正向代理时的业务流程： 
当收到同一个NF内业务NFS发来的内部请求并编码成HTTP请求后，根据远端IP地址和端口，选择一条可用的TCP连接发送出去。 
如果没有可用的TCP连接，则发送TCP SYNC消息向对端NF建立TCP连接，并完成三次握手。 
如果收到对端拆链的TCP消息(FIN或RST)，或者由于连接保活超期等原因时，拆除TCP连接。 
作为反向代理时的业务流程： 
当收到对端NF发送的TCP SYNC消息时，回复SYNC ACK消息并完成三次握手。 
从一条TCP连接上收到的HTTP请求，发送其响应时必须选择同一条连接。 
如果收到对端拆链的TCP消息(FIN或RST)，或者由于连接保活超期等原因时，拆除TCP连接。 
TLS连接管理
TLS连接管理是在TCP连接管理的基础上，增加TLS加密通道的协商，并且使用TLS加解密处理HTTP消息。 
业务流程如下。 
作为正向代理时的业务流程： 
当收到同一个NF内业务NFS发来的内部请求并编码成HTTP请求后，如果请求URI携带了https，则在TCP连接建立成功后，继续TLS加密通道的协商 
加密通道协商完成后，发送加密后的HTTP请求 
收到对端加密的HTTP响应，解密之后再进行后续处理。 
作为反向代理时的业务流程： 
当收到对端NF发送的TCP SYNC消息并完成三次握手后，配合对端继续进行TLS协商。 
协商完成后，收到对端加密的HTTP请求，解密之后再进行后续处理。 
发送对应的HTTP响应之前，先进行加密操作。 
HTTP信令跟踪
HTTP信令跟踪用于接收或发送HTTP消息时，在EMS界面对HTTP消息进行跟踪。 
不涉及业务流程。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
本特性遵循IETF和3GPP标准组织的协议规范，主要包括RFC7540、RFC7541、3GPP TS29.500等。 
特性能力 : 
名称|指标
---|---
转发消息速率TPS(Transaction Per Second)|70000注：在VM规格为8HT 24G内存情况下指标（硬件CPU E5-2670 V3 @ 2.30GHz）。该随硬件变化性能有所不同。
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7|基本特性
License要求 : 
该特性为uMAC的基本特性，无需License支持。 
对其他网元的要求 : 
本特性不涉及对其他网元的要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
配置项|命令
---|---
默认HTTP客户端模板标识配置|SHOW DEFAULTHTTPCLIENTID
SET DEFAULTHTTPCLIENTID|默认HTTP客户端模板标识配置
HTTP客户端模板配置|ADD CLIENTPROFILE
SET CLIENTPROFILE|HTTP客户端模板配置
DELETE CLIENTPROFILE|HTTP客户端模板配置
SHOW CLIENTPROFILE|HTTP客户端模板配置
HTTP服务端模板配置|ADD SERVERPROFILE
SET SERVERPROFILE|HTTP服务端模板配置
DELETE SERVERPROFILE|HTTP服务端模板配置
SHOW SERVERPROFILE|HTTP服务端模板配置
客户端TCP静态链路配置|ADD CLIENTTCPLINK
SET CLIENTTCPLINK|客户端TCP静态链路配置
DELETE CLIENTTCPLINK|客户端TCP静态链路配置
SHOW CLIENTTCPLINK|客户端TCP静态链路配置
服务端TCP静态链路配置|ADD SERVERTCPLINK
SET SERVERTCPLINK|服务端TCP静态链路配置
DELETE SERVERTCPLINK|服务端TCP静态链路配置
SHOW SERVERTCPLINK|服务端TCP静态链路配置
全局参数配置|ADD GLOBALPARAMETER
SET GLOBALPARAMETER|全局参数配置
DELETE GLOBALPARAMETER|全局参数配置
SHOW GLOBALPARAMETER|全局参数配置
显示HTTP链路信息|SHOW LINK INFO
显示HTTP链路详细信息|SHOW LINK DETAIL INFO
删除动态连接|DELETE DYNAMIC CONNECTION
删除所有服务端连接|DELETE SERVER CONNECTION
设置链路状态|SET LINK OPERATION
设置链路优先级值|SET LINK PRIORITY
设置链路权重值|SET LINK WEIGHT
性能统计 : 
编号|性能计数器
---|---
1|C556010001 发送的HTTP请求数
2|C556010002 发送成功的HTTP请求数
3|C556010003 发送失败的HTTP请求数
4|C556010004 接收的HTTP响应数
5|C556010005 接收的HTTP 1XX响应数
6|C556010006 接收的HTTP 2XX响应数
7|C556010007 接收的HTTP 3XX响应数
8|C556010008 接收的HTTP 4XX响应数
9|C556010009 接收的HTTP 5XX响应数
10|C556010010 接收HTTP响应超时数
11|C556020001 接收的HTTP请求数
12|C556020002 发送的HTTP响应数
13|C556020003 发送的HTTP 1XX响应数
14|C556020004 发送的HTTP 2XX响应数
15|C556020005 发送的HTTP 3XX响应数
16|C556020006 发送的HTTP 4XX响应数
17|C556020007 发送的HTTP 5XX响应数
18|C556030001 发送的动态建链请求数
19|C556030002 发送动态建链请求后建链成功数
20|C556030003 发送动态建链请求后建链失败数
21|C556040001 接收动态建链请求后建链成功数
告警和通知 : 
编号|告警名称|描述
---|---|---
1|3506438145 HTTP静态链路断链|配置的HTTP客户端或服务端静态TCP链路发生了断链
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
HTTP属于基本协议栈，AMF只需要配置HTTP正向代理和HTTP反向代理。 
配置前提 : 
5G系统网络功能正常 
TCP连接正常 
TLS连接正常 
配置过程 : 
执行[ADD CLIENTPROFILE]命令，新增HTTP客户端模板配置。
执行[ADD SERVERPROFILE]命令，新增HTTP服务端模板配置。
配置实例 : 
场景说明 : 
无。 
数据规划 : 
配置项|参数名称|取值
---|---|---
模板IP|HTTP客户端模板IP|192.168.16.200
HTTP服务端模板IP|模板IP|192.168.16.200
配置步骤 : 
步骤|命令|说明
---|---|---
1|ADD CLIENTPROFILE:ID=1,IPV4ADDR="192.168.16.200",STARTPORT=20000,ENDPORT=30000,VPNID=0,CONNNUM=2,CONNELASTIC=1,RESPBODYMAXLENGTH=10240,RESPTIMER=30,MAXCONCURRENTSTREAMS=100,KEEPALIVETIMER=30,KEEPALIVESWITCH=1|配置HTTP客户端模板IP
2|ADD SERVERPROFILE:ID=1,IPV4ADDR="192.168.16.200",PORT=8080,VPNID=0,REQBODYMAXLENGTH=10240,RESPTIMER=30,MAXCONCURRENTSTREAMS=100|配置HTTP服务端模板IP
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
无。 
常见问题处理 : 
无。 
## ZUF-76-05-012 IP链路检测 
概述 : 
在商用网络中，eNB和核心网网元在CN通过一系列的传输网络和承载网络传递信息。在eNB侧，无线设备发起链路检测请求，根据核心网网元的响应，统计eNB和核心网网元间的信息传输的丢包，延迟和抖动情况。运营商利用该功能跟踪eNB和核心网网元间的传输降质情况，判断是否由于传输或者是eNB和核心网网元本身导致了链路故障（UE的SCTP链路)。eNB和核心网之间的链路检测也包含MME和SGW之间的链路。 
收益 : 
通过IPPD链路检测统计和告警功能及时发现eNB和MME之间的链路故障，判断是否由于传输或网元本身导致了这些故障。 
描述 : 
在eNB侧，eNB发起ICMP (UDP)请求报文到其他网元，统计对端网元响应的延迟情况，并据此分析IP传输通道的丢包，延迟和抖动的统计数据，并生成相关统计报告。 
图1  MME支持eNB侧的IP链路检测功能
在eNB侧，eNB发起ICMP (UDP)请求报文到其他网元，统计对端网元响应的延迟情况，并据此分析IP传输通道的丢包，延迟，和抖动的统计数据，并生成相关统计报告。 
## ZUF-76-05-013 BGP 
概述 : 
该功能支持BGP协议。
收益 : 
支持BGP动态协议，避免手动配置静态路由。 
描述 : 
边界网关协议（BGP）是运行于 TCP 上的一种自治系统的路由协议。 BGP 是唯一一个用来处理像因特网大小的网络的协议，也是唯一能够妥善处理好不相关路由域间的多路连接的协议。BGP 构建在 EGP 的经验之上。 BGP 系统的主要功能是和其他的 BGP 系统交换网络可达信息。网络可达信息包括列出的自治系统（AS）的信息。这些信息有效地构造了 AS 互联的拓朴图并由此清除了路由环路，同时在 AS 级别上可实施策略决策。 
在使用中，uMAC中配置的静态路由需要通过BGP发布。由此实现业务地址的对外发布. 
## ZUF-76-05-014 VLAN Trunk 
概述 : 
虚拟化SGSN/MME/AMF支持VLAN trunk，实现了虚拟机内外部网络的转换功能，使得虚拟机可以通过一个vNic访问到多个网络。 
收益 : 
虚拟机支持的vNIC数量有限。通过VLAN Trunk功能，可以为vNIC配置子接口，以支持更多的网络，并通过网络隔离业务逻辑接口，提高安全性。 
描述 : 
VLAN Trunk功能主要实现虚拟机内外网之间的转换，开启VLAN Trunk功能，使得虚拟机可以通过一个vNIC访问多个网络。 
启用VLAN Trunk功能后，虚拟机中的网络接口将配置为VLAN接口模式，并通过vNIC连接到计算节点上的parent_port。parent_port将向不同的VLAN子端口发送不同的标记数据包，并连接到虚拟网络。Parent_port可用于发送和接收无标记VLAN数据包，而子端口（child_port）可用于接收和发送VLAN标记数据包。 
# 缩略语 
# 缩略语 
3GPP : 
3rd Generation Partnership Project第三代合作伙伴计划
5GC : 
5G Core Network5G核心网
## ACL 
Access Control List访问控制列表
AF : 
Assured Forwarding确保转发
AMF : 
Access and Mobility Management Function接入和移动管理功能
## BE 
Best Effort尽力而为
## BFD 
Bidirectional Forwarding Detection双向转发检测
## BGP 
Border Gateway Protocol边界网关协议
## BSSGP 
Base
Station Subsystem GPRS Protocol基站子系统GPRS协议
DNS : 
Domain Name System域名系统
## DSCP 
Differentiated Services Code Point差分服务编码点
## DVS 
Distributed Virtual Switch分布式虚拟交换机
## EF 
Expedited Forwarding 快速转发
## GMM 
GPRS Mobile ManagementGPRS 移动性管理
## ICMP 
Internet Control Message ProtocolInternet控制报文协议
## IETF 
Internet Engineering Task Force因特网工程任务组
Internet Engineering Task ForceInternet工程任务组
IP : 
Internet Protocol因特网协议
IPv4 : 
Internet Protocol version 4第四版互联网协议
IPv6 : 
Internet Protocol Version 6IP协议的版本6
## LACP 
Link Aggregation Control Protocol链路聚合控制协议
## LAN 
Local Area Network局域网
## LLC 
Logical Link Control逻辑链路控制
## LSP 
Link State Protocol Data Unit链路状态协议数据单元
## MAC 
Media Access Control媒介接入控制
MME : 
Mobility Management Entity移动管理实体
## MPLS 
Multiprotocol Label Switching多协议标记交换
## NAT 
Network Address Translation网络地址转换
NF : 
Network Function网络功能
## OSPF 
Open Shortest Path First开放最短路径优先
PCF : 
Policy Control Function策略控制功能
## PHB 
Per Hop Behavior逐跳行为
QoS : 
Quality of Service服务质量
SCTP : 
Stream Control Transmission Protocol流控制传输协议
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SM : 
Session Management会话管理
SMF : 
Session Management Function会话管理功能
SMS : 
Short Message Service短消息业务
## SR-IOV 
Single-Root I/O Virtualization单根I/O虚拟化
TCP : 
Transmission Control Protocol传输控制协议
## TOS 
Type of Service服务类型
## UDP 
User Datagram Protocol用户数据报协议
UPF : 
User Plane Function用户平面功能
## VLAN 
Virtual Local Area Network虚拟局域网
## VRF 
Virtual Route Forwarding虚拟路由转发
## VoIP 
Voice over Internet Protocol在IP协议上传送语音
# ZUF-76-06 IP路由 
## ZUF-76-06-001 静态路由 
特性描述 : 

特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
静态路由是网络管理员通过手工方式配置到路由表中的路由信息，适用于规模比较小的网络，如网络结构比较简单、具有固定网络拓扑的静态网络。 
ZXUN uMAC支持使用IPv4/IPv6静态路由来转发报文。
背景知识 : 
路由指分组从源到目的地时，决定端到端路径的网络范围的进程。路由工作在网络层的数据包转发设备。 
动态路由是指网元设备能够自动建立自己的路由表，并且能够根据网络拓扑的不断变化进行适时调整。 
静态路由相比动态路由的优势： 
网络安全保密性高，动态路由需要网络设备之间频繁地交换各自的路由表，而对路由表的分析可以揭示网络的拓扑结构和网络地址等信息。 
不占用网络带宽，因为静态路由不会产生更新流量。 
应用场景 : 
IPv4/IPv6静态路由适用于规模较小的网络，如网络结构比较简单、具有固定网络拓扑的静态网络。只有网络管理员可以修改静态路由表。 
当设备不能使用动态路由协议或者不能建立到达目的网络的路由时，也可以使用静态路由。 
客户收益 : 
受益方|受益描述
---|---
运营商|静态路由无需进行路由交换，可节省网络的带宽、CPU利用率和路由器内存。静态路由是手工配置，可对网络中的路由行为精确控制，从而提高网络的安全性。
终端用户|该特性对终端用户不可见。
实现原理 : 
系统架构 : 
如[图1]示，可以在DeviceA上配置一条目的地址为10.42.16.1，出接口为interface1的静态路由。
图1  静态路由架构图
涉及的网元 : 
网元名称|网元作用
---|---
SGW-C、PGW-C、SMF、UPF、SGW-U、PGW-U|路由表中添加配置的静态路由，并根据报文的目的地址查找路由表，进行转发。
对端网元设备|支持静态路由，接收并转发报文。
本网元实现 : 
概述
ZXUN uMAC支持IPv4静态路由，可根据自身的需求来进行配置，达到精确控制网络路由的目的。
静态路由表的生成完全是在网络管理员对全网拓扑的熟悉的情况下，根据自己的路由需求来进行配置的，因此可以达到对网络中路由行为的精确控制。在网络拓扑发生变化时，需要及时对静态路由表进行重新配置。 
静态路由不同于其它动态路由协议，由于不需要在接口上设置相关的协议数据，只需要对用户配置的静态路由的参数，如目的地址，掩码，下一跳，出接口等做合法性校验即可。 
BFD
静态路由自身没有检测机制，当网络发生故障的时候，需要网络管理员介入重新配置静态路由。BFD是一种通用的快速故障检测机制，利用BFD可以检测静态路由所在链路的状态。
BFD可为每条静态路由绑定一个BFD会话。
当某条静态路由上的BFD会话检测到故障（由Up转为Down），BFD会将故障通知路由管理模块，路由管理模块将这条路由设置为“非激活”状态（此条路由不可用，从IP路由表中删除）。 
当某条静态路由上的BFD会话协商成功（由Down转为Up），BFD会通知路由管理模块，路由管理模块将这条路由设置为“激活”状态（此路由可用，加入IP路由表）。 
默认路由
默认路由又称为缺省路由，是一种特殊的静态路由，目的地址与掩码配置为全零
（0.0.0.0 0.0.0.0）。当路由表中的所有路由都选择失败的时候，将使用默认路由来转发报文。 
默认路由可以是管理员设定的静态路由，也可能是由动态路由协议自动产生的结果，如OSPF、IS-IS。
使用默认路由可以极大的减少路由表条目，从而大大减轻路由器的处理负担，但是如果不正确配置，可能导致路由自环或非最佳路由。 
IPv6静态路由和IPv4静态路由的区别
IPv6静态路由和IPv4静态路由的区别在于目的地址和下一跳地址类型不同。IPv6静态路由是使用IPv6地址为下一跳地址和目的地址，而IPv4静态路由则使用IPv4地址为下一跳地址和目的地址。
业务流程 : 
不涉及。 
系统影响 : 
当网络拓扑发生变化或出现网络问题，静态路由不能自适应变化的网络拓扑结构，可能会导致路由不可达，通信中断。 
应用限制 : 
在静态路由组网下，必须由网络管理员修改路由配置，当网络结构不稳定时不建议配置静态路由。 
特性交互 : 
相关特性|交互关系
---|---
ZUF-76-05-006 BFD|静态路由可以绑定BFD会话，利用BFD会话来检测静态路由所在链路的状态。当某条静态路由上的BFD会话检测到链路故障，BFD会将故障上报系统，系统将这条路由从IP路由表中删除。当某条静态路由上的BFD会话检测到故障的链路重新建立成功，BFD会上报系统，系统将这条路由加入IP路由表。
遵循标准 : 
本特性采用中兴通讯内部的接口和协议，不涉及标准协议。 
特性能力 : 
名称|指标
---|---
整局支持路由最大条目|100000
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
ip route|该命令用于配置IPv4静态路由。
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
运营商在部署分组交换网时，若新建规模较小且网络拓扑结构较简单的网络时，可采用IPv4静态路由实现ZXUN uMAC与对端网元设备之间的通信。
配置前提 : 
启用静态路由的接口地址已配置。 
配置过程 : 
进入ROSNG配置模式。 
在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置
，进入ROSNG配置模式。
（可选）创建VRF。 
在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置
，进入ROSNG配置模式。
创建指定VPN ID的VRF实例。
[ip vrf]
为VRF配置RD。
[rd]
激活VRF的IPv4地址族能力。
[address-family ipv4]
激活VRF的IPv6地址族能力。
[address-family ipv6]
配置IPv4静态路由。 
[ip route]
配置实例 : 
场景说明 : 
如[图1]所示，ZXUN uMAC对接Router 1的接口配置IP地址为10.6.1.1，Router 1对接ZXUN uMAC的接口配置IP地址为10.6.1.2，同属于10.6.1.X网段；Router 1对接Router
2的接口配置IP地址10.7.1.1，Router 2对接Router 1的接口配置IP地址10.7.1.2，同属于10.7.1.X网段；则ZXUN uMAC到Router 2的静态路由下一跳配置为10.6.1.2，同时可以配置一条下一跳为10.6.1.2的缺省路由：
配置一条目的地址为10.7.1.1，下一跳为10.6.1.2的静态路由。 
配置一条目的地址为0.0.0.0，下一跳为10.6.1.2的缺省路由。 
图1  静态路由配置实例图
数据规划 : 
类型|下一跳IP地址|目的网段IP|子网掩码|绑定VRF
---|---|---|---|---
非缺省路由|10.6.1.2|10.7.1.1|255.255.255.0|Gn
缺省路由|10.6.1.2|0.0.0.0|0.0.0.0|Gn
配置步骤 : 
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置IPv4静态路由|配置无VRF的IPv4静态路由ZXROSNG#config terminalZXROSNG(config)#iproute 10.7.1.1 255.255.255.0 10.6.1.2配置带VRF的IPv4静态路由ZXROSNG#config terminalZXROSNG(config)#iproute vrf Gn 10.7.1.1 255.255.255.0 10.6.1.2
3|配置缺省路由|ZXROSNG#config terminalZXROSNG(config)#ip route vrfGn 0.0.0.0 0.0.0.0 10.6.1.2
调整特性 : 
不涉及。 
测试用例 : 
测试项目|IPv4静态路由
---|---
测试目的|验证IPv4静态路由，能正常进行报文的转发和处理。
预置条件|基础配置完成。配置IPv4静态路由实例。
测试过程|从本端子接口向对端接口ping包。
通过准则|ping包正常，两端可以互通。
测试结果|—
常见问题处理 : 
不涉及。 
## ZUF-76-06-002 路由等价多路径 
特性描述 : 

特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
等价路由功能（也称为路由负荷分担功能或者下一跳路由功能），在转发报文的过程中，在没有更高优先级的路由的情况下，目的地相同、掩码相同、优先级相同但是下一跳不同的多条路由会同时被采纳，并依次通过各条路由发送报文，从而实现网络的负荷分担。 
ZXUN uMAC支持对IPv4/IPv6协议类型的网络进行等价路由。
背景知识 : 
ZXUN uMAC支持对IPv4和IPv6这两种协议类型的网络进行路由负荷分担。
IPv4路由负荷分担针对承载在IPv4协议上的网络进行路由负荷分担。 
IPv6路由负荷分担针对承载在IPv6协议上的网络进行路由负荷分担。 
等价路由的优势： 
转发的报文在多条路由中传输，对报文进行了负荷分担，有利于优化网络流量。 
如果一条路由出现故障，报文还能继续在其他的路由上进行转发，提高了网络的可靠性。 
应用场景 : 
本特性无应用场景限制，适用于所有的5GC移动网络。 
客户收益 : 
受益方|受益描述
---|---
运营商|分配流量到多条路由上，从而充分利用网络的带宽资源，防止网络出现拥塞。减小某条路由发生故障对网络的影响，从而提高网络的可靠性。
终端用户|此特性对终端用户不可见。
实现原理 : 
涉及的网元 : 
该特性由ZXUN uMAC实现，无需其他网元的配合。
本网元实现 : 
路由负荷分担包括两种方式，per-packet（包模式）和per-destination（流模式），两种方式的优缺点参见[表2]。
类别|描述|优点|缺点
---|---|---|---
per-packet|包模式以报文为单位，根据负荷分担权重轮转选择链路，链路上的权重值越大，则该链路上通过的报文就越多。|路径利用率高，因为包模式使用轮转法来确定数据包走的路径，使得转发流量均匀得分布在各条路径上。|对于到给定目的地流量可能会选择不同的路径，导致数据包乱序，接收端收到乱序包后要重新排序，从而影响性能。
per-destination|流模式以流为单位，通过Hash算法使流量均衡分担到每一条链路上。|到给定目的的包可以保证走同一条路径。|当流量中只有少量的目的地址时，可能会引起流量集中在少数路径上，分担不均衡；当流量中目的地址增加时，负荷分担会更有效。
ZXUN uMAC只支持流模式的路由负荷分担，以流为单位，通过Hash算法使流量均衡分担到每一条链路上。
业务流程 : 
不涉及。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
ZXUN uMAC只支持流模式的路由负荷分担，以流为单位，通过Hash算法使流量均衡分担到每一条链路上。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
本特性采用中兴通讯内部的接口和协议，不涉及标准协议。 
特性能力 : 
名称|指标
---|---
整局可配置同一目的地等价路由最大条数|16
整局可配置等价路由最大条数|8192
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
ip load-sharing|配置接口路由负荷分担模式
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
IPv4等价路由可使超出单个接口带宽的流量均分到多条链路上，实现流量在各条链路上的负荷分担。以OSPF路由为例，介绍IPv4等价路由配置。
配置前提 : 
 
可以正常接入用户。 
 
（可选）VRF已配置（适用于需要配置带VRF的OSPF路由协议）。 
 
配置过程 : 
步骤|配置说明|配置步骤
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置接口地址|配置开启路由负荷分担功能的接口，并且进入接口配置模式。interface启用接口no shutdown配置接口地址ip address退出接口配置exit
3|配置静态路由负荷分担功能|配置静态路由。ip route配置接口路由负荷分担模式，ZXUN uMAC只支持流模式负荷分担，因此该命令的参数必须为per-destination，包模式负荷分担的参数per-packet不生效。ip load-sharing
4|配置BGP路由负荷分担功能。|启用BGP协议模块，并且进入BGP配置模式router bgp配置一个BGP邻居及其自治系统号。neighbor remote-as配置BGP负荷分担时支持的最大路由数目。maximum-paths配置接口路由负荷分担模式，ZXUN uMAC只支持流模式负荷分担，因此该命令的参数必须为per-destination，包模式负荷分担的参数per-packet不生效。ip load-sharing
5|配置OSPFv2路由负荷分担功能。|配置一个OSPFv2实例，并且进入IPv4-OSPF模式。router ospf创建OSPFv2区域。area配置OSPFv2区域内的网络地址。network配置OSPFv2协议负荷分担时支持的最大路由数目。maximum-paths配置接口路由负荷分担模式，ZXUN uMAC只支持流模式负荷分担，因此该命令的参数必须为per-destination，包模式负荷分担的参数per-packet不生效。ip load-sharing退出接口配置exit
配置实例 : 
场景说明 : 
以OSPF协议为例，在同一个邻居节点在同一区域有多条链路可达，且其链路代价相同，启用IPv4等价路由，则可实现OSPF的IPv4等价路由，如[图1]所示。
图1  IPv4等价路由示意图
数据规划 : 
接口名称|接口IP地址
---|---
xgei-1/0/1/1|101.2.1.100
xgei-1/0/1/2|102.2.1.100
OSPF实例号|OSPF区域ID号|OSPF协议运行的接口IP|反掩码
---|---|---|---
1|0|101.2.1.0|0.0.0.255
102.2.1.0|1|0|0.0.0.255
配置步骤 : 
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置接口IP地址|配置接口xgei-1/0/1/1的IP地址。ZXROSNG#configure terminalZXROSNG(config)#interface xgei-1/0/1/1ZXROSNG(config-if-xgei-1/0/1/1)#no shutdownZXROSNG(config-if-xgei-1/0/1/1)#ip address 101.2.1.100 255.255.255.0ZXROSNG(config-if-xgei-1/0/1/1)#exit配置接口xgei-1/0/1/2的IP地址。ZXROSNG#configure terminalZXROSNG(config)#interface xgei-1/0/1/2ZXROSNG(config-if-xgei-1/0/1/2)#no shutdownZXROSNG(config-if-xgei-1/0/1/2)#ip address 102.2.1.100 255.255.255.0ZXROSNG(config-if-xgei-1/0/1/2)#exit
3|启用并配置OSPF协议|ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#network 101.2.1.0 0.0.0.255ZXROSNG(config-ospf-1-area-0)#network 102.2.1.0 0.0.0.255ZXROSNG(config-ospf-1-area-0)#exitZXROSNG(config-ospf-1)#maximum-paths 2ZXROSNG(config-ospf-1)#exit
4|配置IPv4等价路由，默认为逐流方式。|配置接口xgei-1/0/1/1逐流方式。ZXROSNG(config)#interface xgei-1/0/1/1ZXROSNG(config-if-xgei-1/0/1/1)#ip load-sharing per-destinationZXROSNG(config-if-xgei-1/0/1/1)#exit配置接口xgei-1/0/1/2逐流方式。ZXROSNG(config)#interface xgei-1/0/1/2ZXROSNG(config-if-xgei-1/0/1/2)#ip load-sharing per-destinationZXROSNG(config-if-xgei-1/0/1/2)#exit
调整特性 : 
不涉及。 
测试用例 : 
测试项目|IPv4等价路由
---|---
测试目的|验证IPv4等价路由，能正常进行报文的负荷分担。
预置条件|基础配置完成。配置接口的OSPF IPv4等价路由。
测试过程|对本端进行流量灌包。
通过准则|报文在配置IPv4等价路由的接口上能负荷分担。
测试结果|–
常见问题处理 : 
不涉及。 
## ZUF-76-06-003 策略路由 
特性描述 : 

特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
策略路由，是一种根据用户预定的策略来进行选择的路由机制。与传统的，只根据目的地址查找路由表进行转发的路由机制相比，策略路由还可以根据其他方式，比如根据源地址、源端口号以及目的端口号来选择路由。 
ZXUN uMAC支持策略路由功能，可以实现根据预定策略来选择路由的功能。
 说明： 
目前ZXUN uMAC只支持IPv4协议类型的策略路由，不支持IPv6协议类型的策略路由。
背景知识 : 
相比根据IP报文的目的地址查找路由表进行转发，策略路由可以根据报文的五元组信息灵活选择路由进行转发，ZXUN uMAC中策略路由的优先级要高于普通路由。
应用场景 : 
两台终端设备访问服务器时，ZXUN uMAC对不同的终端地址采用策略路由，转发给不同的路由器。
ZXUN uMAC对用户报文外发提供策略路由功能，策略路由规则支持下列功能：
支持匹配IPv4或IPv6的ACL规则，可根据IP源、目的地址，协议号，源、目的端口号来决定报文的转发下一跳。 
IPv4、IPv6都支持VRF内的策略路由。 
IPv4、IPv6都支持等价多下一跳，最多支持8个等价下一跳地址；根据配置顺序和路由可达状态在多个下一跳间负荷分担。 
IPv4支持指定GRE隧道为策略路由下一跳出口，IPv6暂不支持指定GRE、6to4、6in4等隧道为为策略路由下一跳出口。 
可支持根据策略路由匹配规则，设定报文的IPv4 ToS/DSCP码或IPv6的Traffic Class字段值。 
策略路由规则指定的下一跳地址，在普通路由检测到该下一跳地址失效时，策略路由中的下一跳地址也同步失效。 
客户收益 : 
受益方|受益描述
---|---
运营商|报文可以根据运营商制定的策略进行路由转发，从而提高网络的灵活性。
终端用户|该特性对终端用户不可见。
实现原理 : 
系统架构 : 
不涉及。 
本网元实现 : 
相对于传统路由协议，基于策略路由原理的路由使网络管理者对报文转发和存储具有更强的控制能力，使用更灵活。例如：如果在目的地址相同的情况下，需要根据源地址来选取两条等价路径中的这一条或者另一条，策略路由可以很方便地解决问题。 
在ZXUN uMAC中，使用route-map来对应策略，操作员可以配置多个不同的route-map，ZXUN uMAC将route-map应用在报文对外发送的逻辑接口上，可以根据策略来实现报文外发时路由的选择。
每个route-map由一系列sequence组成，每个sequence中含有多个match和set语句。 
match和set语句的作用如下： 
match语句中定义了多种条件，用于和报文进行匹配。 
set中语句规定了当条件匹配成功时，系统将要进行的动作。 
当一个sequence的match语句中定义的条件未匹配时，系统继续尝试匹配下一个sequence中的match语句。 
对于ZXUN uMAC发送的报文，判断是否存在策略路由，如果没有，则按照普通路由进行转发；如果存在策略路由，则按照route-map的sequence依次进行处理。ZXUN uMAC中，通过Virtual-Template虚接口作为策略路由和用户业务的关联点，关联到Virtual-Template接口上的策略路由规则，可以被用户业务感知并使用。逻辑网元可以通过绑定Virtual-Template接口，明确本网元在路由系统中的使用的策略关联点，具体过程如下。
用报文去匹配第一个sequence中配置的ACL。
若匹配失败，则继续匹配下一个sequence中配置的ACL。 
若匹配成功，执行下一步操作。 
判断所属sequence的属性。 
若sequence的属性为deny，则按照普通路由进行转发处理。 
若sequence的属性为permit，则根据该sequence中的set项规定的动作进行转发。 
判断是否存在有效的set ip next-hop项，即是否存在有效的下一跳。 
当存在有效的set ip next-hop项时，则将报文送往设定的下一跳。当存在多个有效的set ip
next-hop项时，按照逐流方法选择有效的下一跳。 
若未设置set ip next-hop或不存在有效的set ip next-hop项时，则按照普通路由进行转发处理。 
业务流程 : 
不涉及。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
本特性采用中兴通讯内部的接口和协议，不涉及标准协议。 
特性能力 : 
名称|指标
---|---
整局可配置route-map最大数|200
整局可配置route-map sequence最大条数|200
整局可配置match/set项最大条数|2000
每条route-map子规则下可配置相同类型的match/set项最大条数|10
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
ipv4-access-list|配置IPv4类型的访问控制列表ACL（Access Control List）。
route-map|创建（删除）或进入route-map配置模式。
ip policyinterface|用于接口的IPv4策略路由配置，也就是对指定的虚机实接口或虚接口绑定route-map，根据路由策略为报文分配转发路径。
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
在ZXUN uMAC中启用IP策略路由功能。
配置前提 : 
 
ZXUN uMAC路由配置正确，可以到达策略路由指定的下一跳。 
 
ZXUN uMAC业务配置正确，可以正常接入用户。 
 
配置过程 : 
步骤|配置说明|配置步骤
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置ACL|创建IPv4类型的访问控制列表，并且进入IPv4-ACL模式。ipv4-access-list配置ACL规则。该命令可手动配置规则的序号，若此项参数值使用缺省值，则表示根据ACL步长来自动配置规则的序号。rule
3|配置route-map|创建route-map。route-map配置match项，对与访问表匹配的包进行策略路由。match ip address配置指定下一跳地址。set ip next-hop
4|配置虚接口及虚接口的子接口|创建virtual_template接口。interface配置virtual_template虚拟模板的工作模式。mode创建virtual_template接口的子接口。interface（可选）配置virtual_template接口的子接口绑定到私网路由。ip vrfforwarding
5|配置策略路由规则应用|配置将route-map绑定到指定的virtual_template接口的子接口。ip policy interface
配置实例 : 
场景说明 : 
用户接入ZXUN uMAC，用户分配到的IPv4地址处于名为SGi的VRF下。通过普通路由，该用户访问PDN采用2.2.2.2为下一跳，启用策略路由后，希望该用户走1.1.1.1访问PDN。
数据规划 : 
VRF名称|ACL规则名称|MS的地址池|反掩码|下一跳IP地址|虚接口及其子接口名称
---|---|---|---|---|---
SGi|james|172.0.0.0|0.0.0.255|1.1.1.1|virtual_template1
virtual_template1.1|SGi|james|172.0.0.0|0.0.0.255|1.1.1.1
配置步骤 : 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置ACL|配置名为james的ACLZXROSNG#config terminalZXROSNG(config)#ipv4-access-listjamesZXROSNG(config-ipv4-acl)#rule permit 172.0.0.0 0.0.0.255ZXROSNG(config-ipv4-acl)#exit
3|配置route-map|ZXROSNG(config)#route-map jamesZXROSNG(config-route-map)#matchip address jamesZXROSNG(config-route-map)#set ip next-hop 1.1.1.1ZXROSNG(config-route-map)#exit
4|配置虚接口及虚接口的子接口|ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#modeps-coreZXROSNG(config-if-virtual_template1)#exitZXROSNG(config)#interfacevirtual_template1.1ZXROSNG(config-if-virtual_template1.1)#ipvrf forwarding SGiZXROSNG(config-if-virtual_template1.1)#exit
5|配置策略路由规则应用|ZXROSNG(config)#ip policy interface virtual_template1.1route-map james
调整特性 : 
不涉及。 
测试用例 : 
测试项目|策略路由功能
---|---
测试目的|用户面报文可进行策略路由转发。
预置条件|基础配置完成。网元运行正常，用户可接入APN，分配IPv4地址进行数据业务。网元到PDN侧的IPv4地址A有两条或以上的等价路由，对应不同的下一跳出接口。配置ipv4-acl、route-map，route-map中指定下一跳为上述路由出接口中的一个，配置Virtual-Template接口及子接口，子接口关联APN对应的VRF，使用ippolicy配置策略路由规则应用。网元或出接口连接的交换机设备上可以进行镜像抓包。
测试过程|在网元下，配置将virtual-Template接口与网元绑定。多个用户接入，上行到IP地址A的报文匹配策略路由规则，镜像抓包检查到IP地址A的各个路由出接口的报文转发结果。在网元下，将virtual-Template接口与网元的绑定删除。
通过准则|将策略与网元绑定成功。匹配策略路由规则的所有用户上行报文，只在route-map指定的路由下一跳出接口转发，其他出接口不转发。策略与网元绑定可正常删除。策略路由不再生效，不同用户的上行报文可以在多个等价的路由下一跳出接口转发。
测试结果|–
常见问题处理 : 
不涉及。 
## ZUF-76-06-004 VRF 
特性描述 : 

特性描述 : 
适用网元 : 
AMF、MME、SGSN 
描述 : 
定义 : 
VRF即虚拟路由转发功能，是对物理设备的逻辑划分。每个VRF对应一个VPN，有自己独立的路由表、转发表和相应的接口，不受其他VPN路由表的影响，从而实现业务流量的隔离。
ZXUN uMAC支持VRF功能，用于将一台路由设备在逻辑上划分为多台虚拟路由设备，也就是多个VPN路由转发实例。
背景知识 : 
虚拟路由转发表VRF（Virtual Routing and Forwarding）应用于三层VPN（Virtual
Private Network）。每一个VRF可以看作一台虚拟的路由器，好像是一台专用的PE设备。该虚拟路由器包括如下元素：
 
每个VRF对应一个VPN，有自己独立的路由表、转发表，不受其他VPN路由表影响。 
 
每个VRF有自己独立的地址空间，同一台路由设备上的不同VPN间不会产生地址冲突。 
 
应用场景 : 
本特性应用于运营商需要实现网络隔离的场景。 
 
按物理接口/逻辑接口、隧道、路由配置VRF，可实现接口彼此隔离，提高安全性，避免恶意访问。 
 
不同的VRF下可以配置相同的地址，实现地址资源的重复使用。 
 
客户收益 : 
受益方|受益描述
---|---
运营商|可以为不同的VPN配置缺省路由，达到简化路由配置的目的。可实现路由和流量的隔离，不同VPN间的业务数据被隔离，提高网络的安全性。可实现IP地址的重复使用，在不同VPN实例下的接口使用相同的IP地址，节省运营商的地址资源。
终端用户|该功能对终端用户不可见。
实现原理 : 
系统架构 : 
不涉及。 
涉及的网元 : 
该特性由ZXUN uMAC实现，无需其他网元的配合。
本网元实现 : 
ZXUN uMAC支持VRF功能，通过将接口、路由协议、APN、地址池等绑定不同的VRF，实现不同的组网。
ZXUN uMAC支持的VRF功能如下：
 
ZXUN uMAC支持VRF的IPv4类型，IPv6类型，或者IPv4+IPv6混合类型。实现IPv4和IPv6承载网之间的流量隔离，提高网络的安全性。 
 
ZXUN uMAC支持物理接口/逻辑接口配置VRF，均能够部署到不同的VRF中，可实现接口彼此隔离，提高安全性，避免恶意访问。 
 
ZXUN uMAC支持不同的VRF间IP地址重叠。每个VRF有自己独立的地址空间，即不同的VRF下可以配置相同的地址，实现地址资源的重复使用。 
 
ZXUN uMAC支持APN配置VRF，可将用户请求的不同业务接入不同的网络，实现不同APN流量逻辑上的隔离。 
 
ZXUN uMAC支持VRF功能，通过将接口、路由协议、APN、地址池等绑定不同的VRF，实现不同的组网。
VRF绑定关系|绑定说明
---|---
组网应用|接口绑定VRF|ZXUN uMAC支持物理接口/逻辑接口绑定到某个特定的VRF中，实现接口的隔离，组建独立的网络。
组网应用|隧道绑定VRF|与接口绑定VRF类似，ZXUN uMAC创建隧道后，把隧道绑定到相应的VRF中，实际上就是把隧道接口绑定到某个VRF。绑定后，该隧道就只属于该VRF，与其他的隧道和接口隔离开来。
组网应用|静态路由绑定VRF|ZXUN uMAC支持IPv4/IPv6静态路由绑定VRF。静态路由工作在同一个VRF域内，可根据配置的下一跳地址在路由表中查找出接口。
组网应用|动态路由绑定VRF|ZXUN uMAC支持OSPFv2、OSPFV3、BGP4、BGP-4+路由协议绑定VRF。以OSPFv2为例，ZXUN uMAC支持VRF多实例部署，通过OSPFv2路由协议将指定VRF内的路由信息同步给对端路由设备，并接收该VRF的路由信息，完成指定VRF内的路由条目交互。
业务应用|APN绑定VRF|APN是ZXUN uMAC对用户进行划分的一个单位，通过APN绑定VRF，ZXUN uMAC可将用户请求的不同业务接入不同的网络，实现不同APN流量逻辑上的隔离。APN绑定的VRF需要和其关联的地址池绑定的VRF一致。
资源应用|地址池绑定VRF|ZXUN uMAC为用户分配IP地址时，需要先创建地址池，并为其分配对应的地址段。如若绑定VRF，则不同的VRF下可以配置相同的IP地址，从而实现地址资源的重复使用。
资源应用|对接网元绑定VRF|ZXUN uMAC支持对接NF绑定VRF功能。以AMF为例，如果AMF绑定VRF，表明需要在ZXUN uMAC和该AMF之间建立VPN，并根据配置的VRF的路由信息转发计费报文。
未使用VRF功能时，路由信息均是公共的，不同业务类型的IP报文从同一张路由表中获取路由信息。 
使用VRF功能后，设备中的路由信息需要与VRF建立绑定关系，使每个VRF都拥有独立的路由表，不与VRF绑定的路由形成一个独立的公网路由表。每个VRF都通过唯一的VRF名称标识，路由信息与VRF绑定即建立路由信息与VRF名称的对应关系。 
业务流程 : 
不涉及。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
组网规划必须保证通过该IP地址发送和接收报文的接口在同一个VRF中，否则会导致业务报文丢弃。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准类别|标准名称
---|---
IETF|RFC 2764 A Framework for IP Based Virtual Private Networks
特性能力 : 
名称|指标
---|---
整局支持配置VRF数目|4096
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
类别|命令
---|---
创建VRF|ip vrf
创建VRF|rd
创建VRF|address-family ipv4
创建VRF|address-family ipv6
绑定VRF|ip vrf forwarding
绑定VRF|tunnel vrf
绑定VRF|ip route
绑定VRF|router ospf
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
运营商在部署分组交换网时，ZXUN uMAC支持VRF功能，通过将物理接口/逻辑接口、隧道、APN、地址池等绑定VRF，可为该VRF内用户提供在逻辑上隔离的虚拟专用网络。
配置前提 : 
操作员已登录EM客户端。 
配置过程 : 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|创建VRF|创建指定VPN ID的VRF实例。ip vrf为VRF配置RD。rd激活VRF的IPv4地址族能力。address-family ipv4激活VRF的IPv6地址族能力。address-family ipv6
3|绑定VRF|接口绑定VRF。ip vrf forwarding隧道绑定VRF。tunnel vrf静态路由绑定VRF。ip route动态路由协议OSPFv2绑定VRF。routerospfAPN绑定VRF。vrf地址池绑定VRF。ip vrf forwarding
配置实例 : 
场景说明 : 
进行VRF配置。 
数据规划 : 
VRF名称|VPN ID|RD
---|---|---
Gn|504|504:504
接口名称|接口地址|子网掩码|对端目的地址|子网掩码
---|---|---|---|---
xgei-1/0/1/1|200.190.1.1|255.255.255.0|200.190.2.0|255.255.255.0
配置步骤 : 
根据规划，进行如下配置： 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|创建VRF|创建名称为Gn的VRF实例，指定VPN ID为504ZXROSNG#config terminalZXROSNG(config)#ip vrf Gn vpnid 504为实例配置RDZXROSNG(config-vrf-Gn)#rd 504:504激活VRF的IPv4地址族能力ZXROSNG(config-vrf-Gn)#address-familyipv4ZXROSNG(config-vrf-Gn-af-ipv4)#exit激活VRF的IPv6地址族能力ZXROSNG(config-vrf-Gn)#address-familyipv6ZXROSNG(config-vrf-Gn-af-ipv6)#exitZXROSNG(config-vrf-Gn)#exit
3|将指定的接口资源划入VRF中|ZXROSNG(config)#interface xgei-1/0/1/1ZXROSNG(config-if-xgei-1/0/1/1)#ip vrf forwarding GnZZXROSNG(config-if-xgei-1/0/1/1)#ip address 200.190.1.1 255.255.255.0ZXROSNG(config-if-xgei-1/0/1/1)#exit
4|配置VRF路由|ZXROSNG(config)#ip route vrf Gn 200.190.2.0 255.255.255.0200.190.1.1
调整特性 : 
不涉及。 
测试用例 : 
测试项目|VRF功能
---|---
测试目的|验证VRF功能，能正常进行报文的转发和处理。
预置条件|基础配置完成。配置一个VPN实例。将指定的接口资源划入VPN实例中。
测试过程|从本端子接口向对端接口，执行ping操作。
通过准则|ping包正常，两个网元之间互通。
测试结果|–
常见问题处理 : 
不涉及。 
## ZUF-76-06-005 OSPFv2 
特性描述 : 
特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
ZXUN uMAC支持OSPFv2路由协议与对端网元设备互通，通过交互OSPF协议报文来传递路由信息，实现网络拓扑共享的目的。
背景知识 : 
OSPF是IETF组织开发的一个基于链路状态的自治系统内部路由协议。适用于规模较大，组网环境比较复杂的网络。
OSPF包括OSPFv2（OSPF Version 2）和OSPFv3（OSPF Version 3）两个相互独立的协议版本。OSPFv2应用于IPv4网络，是基于子网运行的路由协议。OSPFv3主要应用于IPv6网络，是基于链路运行的路由协议。 
在IP网络上，OSPF通过收集和传递自治系统的链路状态来动态地发现并传播路由，目前IPv4协议使用的是OSPF版本2，统称OSPFv2。
应用场景 : 
运营商在部署规划分组交换网时，如果网络拓扑结构复杂，或者三层网络设备数量较多，ZXUN uMAC可以使用OSPFv2动态路由和对端网元互通，自动适应网络拓扑的变化。
客户收益 : 
受益方|受益描述
---|---
运营商|能够自动适应网络拓扑的变化，减少运营商的网络开销，降低成本。能确保路由计算的安全性，提高网络安全。
终端用户|该特性对终端用户不可见。
实现原理 : 
系统架构 : 
不涉及 
本网元实现 : 
通过开启OSPFv2进程，与对端网元设备相互传递路由信息。 
OSPFv2是基于链路状态的路由协议，用于在同一自治系统内交互路由信息。ZXUN uMAC支持OSPFv2实现以下功能。
区域划分OSPFv2区域将网络分为若干个较小部分，以减少每个路由器存储和维护的信息量，屏蔽网络拓扑变化波及的范围。区域是从逻辑上将路由器划分到不同的组，每个组用区域号（Area ID）来标识。常用的区域种类有骨干区域、虚连接、末节区域和非完全末节区域。 
路由聚合路由聚合可节约骨干区域的资源，通过将一组网络地址聚合为一个聚合地址来实现。OSPFv2支持区域边界路由聚合和路由重分布时的路由聚合两种方式。路由聚合方式说明区域边界路由聚合当区域边界路由向别的区域发送路由信息时，如果该区域存在一些连续的网段，可以通过命令将这些连续的网段聚合成一个网段。这样可以只发送一条LSA。路由重分布时的路由聚合当其他路由协议的路由重分布到OSPFv2中之后，每条单独的路由作为一个外部的LSA被通告。可以通过聚合将这些外部路由作为一条单独的路由进行通告，这将大大减小OSPFv2的链路状态数据库的大小。 
多OSPFv2进程OSPFv2支持多进程，ZXUN uMAC上可以运行多个不同的OSPFv2进程，彼此之间独立互不影响。 说明：ZXUN uMAC的一个接口只能属于一个OSPFv2进程。 
认证功能为了增强网络上路由进程的安全性，可以在路由器上配置OSPFv2认证。OSPFv2的邻居必须在该网络上使用相同的认证。ZXUN uMAC支持简单口令认证和采用报文摘要口令（MD5）认证。 
BFD for OSPFv2BFD（Bidirectional Forwarding Detection，双向转发检测）是一种通用的快速故障检测机制。当OSPFv2邻居之间的链路出现故障时，利用BFD可以快速检测路由所在链路的状态。 
OSPFv2路由负载均衡当OSPFv2路由表中同时出现了多条优先级相同的路径，就可以对流量进行负载均衡。 
业务流程 : 
不涉及。 
系统影响 : 
运行OSPF会占用一定的系统资源，比如OSPF计算会消耗一定的CPU资源，OSPF存储路由会消耗一定的内存资源。 
应用限制 : 
OSPFv2是IGP，仅适用于同一个自治系统内，不同自治系统的网元设备相互通信需要使用EGP。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准类别|标准名称
---|---
IETF|RFC 1765 OSPF Database OverflowRFC 2328 OSPF Version 2RFC 3101 OSPF Not-So-Stubby Area (NSSA) Option 1-9RFC 3137 OSPF Stub Router AdvertisementRFC 3630 Traffic Engineering Extensions to OSPF Version 2RFC 4811 OSPF Out-of-Band LSDB ResynchronizationRFC 4812 OSPF Restart SignalingRFC 4813 OSPF Link-Local Signaling
特性能力 : 
名称|指标
---|---
整局支持最大路由数目|100000
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
interface|进入OSPFv2接口配置模式
router ospf|创建OSPFv2进程
area|创建OSPFv2的区域
network|运行OSPFv2协议接口的网络类型
maximum-paths|配置OSPFv2协议负载均衡时支持的最大路由数目
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
ZXUN uMAC上开启OSPFv2进程，使ZXUN uMAC与对端网元设备之间通过OSPFv2协议学习路由。
配置前提 : 
 
ZXUN uMAC业务配置正确，可以正常接入用户。 
 
VRF已配置（适用于需要配置带VRF的OSPF路由协议）。 
 
配置过程 : 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置OSPFv2基本功能|在路由器上启动OSPFv2进程，使得路由器之间能通过OSPFv2协议学习到路由。创建OSPFv2进程router ospf创建OSPFv2的区域area配置路由器的router-idrouter-id 进入OSPFv2接口配置模式interface运行OSPFv2协议接口的网络类型network
3|配置OSPFv2接口属性|进入OSPFv2接口配置模式interface接口发送HELLO报文的时间间隔hello-interval接口上邻居的死亡时间dead-interval接口重传LSA的时间间隔retransmit-interval接口传输一个链路状态更新数据包的延迟transmit-delay接口的费用值cost接口优先级priority
4|配置OSPFv2区域|创建OSPFv2的区域area配置区域内的汇总地址范围range定义一个区域为stub（末梢）区域stub配置本设备在stub区域内通告的主机路由stub-host定义一个区域为NSSA区域nssa配置OSPFv2区域之间的网络路由过滤信息filter-list该命令在IPv4–OSPF区域模式下运行，用于在两PE路由器之间，建立sham-link链路sham-link如果指定区域存在，使指定区域有效enablearea如果指定区域存在，使指定的区域无效disablearea
5|配置OSPFv2认证|配置OSPFv2某个区域的认证authentication进入OSPFv2接口配置模式interface配置某接口的认证方式authentication使用简单口令认证类型的接口设置口令authentication-keyMD5报文摘要认证message-digest-key
6|配置OSPFv2路由聚合|配置路由重分布时的路由聚合summary-address进入IPv4–OSPF区域模式area配置区域间路由聚合range
7|（可选）配置OSPFv2路由其他选项|配置OSPFv2实例的缺省路由notifydefault route修改该OSPFv2实例的参考带宽auto-cost配置所有接口的BFD属性bfd配置OSPFv2路由管辖距离distanceospf开启OSPFv2实例的快速重计算路由（fast-reroute）功能fast-reroute配置非广播网络上的邻居路由器neighbor配置OSPFv2协议负载均衡时支持的最大路由数目maximum-paths配置路由器的域IDdomain-id配置实例的域tagdomain-tag配置本OSPFv2实例支持无中断转发能力nsf配置NSF运行所需的最长时间grace-period将一个接口配置为被动接口passive-interface配置distribute-list过滤路由distribute-list配置本设备引入其他协议学习到的路由信息redistribute配置metric的最大值max-metric配置track联动功能trackOSPFv2实例下接口的邻居TTL跳数ttl-security
配置实例 : 
场景说明 : 
ZXUN uMAC与Router通过两条链路建链，通告各自的一个回环地址路由。
数据规划 : 
接口名称|接口IP地址|子网掩码
---|---|---
xgei-0/2/0/3|11.22.1.1|255.255.255.0
xgei-0/2/0/4|11.22.10.1|255.255.255.0
loopback1|1.1.1.11|255.255.255.0
OSPF实例号|OSPF区域ID号|OSPF协议运行的接口IP|反掩码
---|---|---|---
1|0|11.22.1.0|0.0.0.255
11.22.10.0|1|0|0.0.0.255
1.1.1.11|1|0|0.0.0.0
配置步骤 : 
根据规划，进行如下配置。 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置接口地址和回环接口地址|配置接口xgei-0/2/0/3的IP地址。ZXROSNG#config terminalZXROSNG(config)#interface xgei-0/2/0/3ZXROSNG(config-if-xgei-0/2/0/3)#no shutdownZXROSNG(config-if-xgei-0/2/0/3)#ip address 11.22.1.1 255.255.255.0ZXROSNG(config-if-xgei-0/2/0/3)#exit配置接口xgei-0/2/0/4的IP地址。ZXROSNG(config)#interface xgei-0/2/0/4ZXROSNG(config-if-xgei-0/2/0/4)#no shutdownZXROSNG(config-if-xgei-0/2/0/4)#ip address 11.22.10.1 255.255.255.0ZXROSNG(config-if-xgei-0/2/0/4)#exit配置接口loopback1的IP地址。ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#no shutdownZXROSNG(config-if-loopback1)#ip address 1.1.1.11 255.255.255.0ZXROSNG(config-if-loopback1)#exit
3|配置OSPF|ZXROSNG#config terminalZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#network 11.22.1.0 0.0.0.255ZXROSNG(config-ospf-1-area-0)#network 11.22.10.0 0.0.0.255ZXROSNG(config-ospf-1-area-0)#network 1.1.1.11 0.0.0.0ZXROSNG(config-ospf-1)#maximum-paths 2ZXROSNG(config-ospf-1)#exit
调整特性 : 
不涉及。 
测试用例 : 
测试项目|OSPF建链功能
---|---
测试目的|验证OSPF路由正确发布。
预置条件|基础配置完成。ZXUN uMAC业务配置正确，可以正常接入用户。
测试过程|开启OSPF进程，并将接口加入OSPF域内。
通过准则|OSPF路由能生效，邻居建链成功，能正确生成路由。
测试结果|–
常见问题处理 : 
不涉及。 
## ZUF-76-06-006 OSPFv3 
特性描述 : 

特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
ZXUN uMAC支持通过OSPFv3路由协议与对端网元设备互通，通过交互OSPF协议报文来传递路由信息，实现网络拓扑共享的目的。
背景知识 : 
OSPF是IETF组织开发的一个基于链路状态的自治系统内部路由协议。适用于规模较大，组网环境比较复杂的网络。
OSPF包括OSPFv2（OSPF Version 2）和OSPFv3（OSPF Version 3）两个相互独立的协议版本。OSPFv2应用于IPv4网络，是基于子网运行的路由协议。OSPFv3主要应用于IPv6网络，是基于链路运行的路由协议。 
OSPFv3是OSPF版本3的简称。随着IPv6网络的建设，同样需要动态路由协议为IPv6报文的转发提供准确有效的路由信息。基于此，IETF在保留了OSPFv2优点的基础上针对IPv6网络修改形成了OSPFv3。
OSPFv3主要用于在IPv6网络中提供路由功能，是IPv6网络中路由技术的主流协议。
应用场景 : 
运营商在部署规划分组交换网时，如果网络拓扑结构复杂，或者三层网络设备数量较多，ZXUN uMAC可以使用OSPFv3动态路由和对端网元互通，自动适应网络拓扑的变化。
客户收益 : 
受益方|受益描述
---|---
运营商|能够自动适应网络拓扑的变化，减少运营商的网络开销，降低成本。能确保路由计算的安全性，提高网络安全。
终端用户|该特性对终端用户不可见。
实现原理 : 
系统架构 : 
不涉及。 
本网元实现 : 
与OSPFv2相比，OSPFv3在工作机制上与OSPFv2基本相同，但为了支持IPv6地址格式，OSPFv3对OSPFv2做了一些改动。下面详细介绍OSPFv3与OSPFv2的异同点。
OSPFv3与OSPFv2的相同点
OSPFv3在协议设计思路和工作机制与OSPFv2基本一致。
报文类型相同，包含Hello、DD、LSR、LSU、LSAck五种类型的报文。 
区域划分相同。 
LSA泛洪和同步机制相同，为了保证LSDB内容的正确性，需要保证LSA的可靠泛洪和同步。 
路由计算方法相同，采用最短路径优先算法计算路由。 
网络类型相同，支持广播、NBMA、P2MP和P2P四种网络类型。 
邻居发现和邻接关系形成机制相同，OSPF路由器启动后，便会通过OSPF接口向外发送Hello报文，收到Hello报文的OSPF路由器会检查报文中所定义的参数，如果双方一致就会形成邻居关系。形成邻居关系的双方不一定都能形成邻接关系，这要根据网络类型而定，只有当双方成功交换DD报文，交换LSA并达到LSDB的同步之后，才形成真正意义上的邻接关系。 
DR选举机制相同，在NBMA和广播网络中需要选举DR和BDR。 
OSPFv3与OSPFv2的不同点
由于OSPFv3是基于IPv6的，OSPFv3与OSPFv2存在一些不同。
OSPFv3拓扑是基于链路（link）的，OSPFv2拓扑是基于子网（subnet）的。IPv6使用“链路”作为结点在链路层进行通信的设施或介质。“结点”和链路相连，多个IP子网可以分配为一个链路，不在同一个IP子网上的两个结点可以在单个链路上直接通信。 
删去地址语义除了在链路状态更新报文中的LSA净荷外，OSPFv3报文中不出现IPv6地址。路由器LSA和网络LSA不再包含地址信息，只简单表示拓扑信息。OSPF路由器ID和LSA ID保留为32位IPv4地址，不为其分配IPv6地址。 
增加了泛洪范围LSA的泛洪范围体现在LSA的LS类型字段，分为链路本地范围、区域范围和自治域范围三类。OSPFv3支持在单条链路上运行多个OSPF协议实例的功能。 
链路本地地址的使用IPv6链路本地地址用于单个链路上的邻居发现和自动配置等，IPv6路由器不转发源地址为链路本地地址的IPv6数据报文。分配给链路本地单播地址的IPv6地址范围为FE80/10。除了虚链路之外，OSPFv3与接口相关的链路本地地址可以作为源地址来发送OSPF报文。对于虚链路，必须使用全球范围或者本地站点的IPv6地址作为源地址。链路本地地址出现在OSPFv3的链路LSA中，但不允许出现在其它LSA中。 
认证方式的变化在OSPFv3报文首部中删除了认证类型和认证字段，所有和认证相关的字段在OSPFv3的区域数据结构和接口数据结构中不再出现。OSPFv3使用IPv6自身提供的认证机制来实现报文交换的完整性和机密性。 
协议报文格式的变化OSPFv3直接运行在IPv6之上。OSPF报文首部不包含地址语义。地址信息包含在不同类型的LSA中，因此OSPFv3实现了与网络协议的分离。OSPFv3的报文格式变化如下。版本号从2变为3。Hello报文和数据库描述报文的选项字段扩展到24位。报文首部删除了认证和认证类型字段。Hello报文不包含地址语义，而是包含该路由器用于标识链路的接口ID。如果路由器成为链路上的DR，接口ID就是网络LSA的链路状态ID。为了在SPF计算时处理路由器LSA，在选项字段中增加了R和V6两个标志位。OSPF报文首部包含一个“实例ID”，允许在一个单独的链路上运行多个OSPF协议实例。 
OSPFv3报文格式
OSPFv3和OSPFv2一样，具有相同类型的五种报文。但是，其报文头长度只有16字节，且没有认证字段。增加了一个Instance
ID用来表示可在同一条链路上运行多个实例。OSPFv3的报文如[图1]所示。图1  OSPFv3报文格式
Version：OSPF的版本号。对于OSPFv3来说，其值为3。
Type：OSPF报文的类型。数值从1到5，分别对应Hello报文、DD报文、LSR报文、LSU报文和LSAck报文。
Packet
Length：OSPF报文的总长度，包括报文头在内，单位为字节。
Instance ID：同一条链路上的实例标识。 
0：保留位，值为0。 
OSPFv3的LSA类型
LSA是构成OSPFv3链路状态数据库的基本单元，路由器使用LSA构造一个完整的网络拓扑，并由此产生路由表。RFC2740中定义了七类LSA。
路由器LSALSA类型为0x2001，由每个路由器生成，描述本路由器的链路状态和开销，只在路由器所处区域内传播。 
网络LSALSA类型为0x2002，对于含有多个路由器的广播和NBMA链路，该链路的DR生成网络LSA。 
域间前缀LSALSA类型0x2003，等价于OSPFv2中的3型LSA，域间前缀路由器LSA由区域边界路由器产生，用于描述其他区域的IPv6地址前缀。对stub区域，域间前缀LSA也可用于描述默认路由。 
域间路由器LSALSA类型0x2004，等价于IPv4的4型LSA，由ABR产生，用于描述到其他区域的ASBR。 
AS外部LSALSA类型0x4005，由ASBR产生，用于描述AS外部的目的地。 
链路LSALSA类型0x0008，路由器对于每个与其相连的链路通告单独的链路LSA，这些LSA有本地链路的泛洪范围，不泛洪到与其相关的链路之外。 
域内前缀LSALSA类型0x2009，路由器用域内前缀LSA来通告一个或者多个IPv6地址前缀，这些IPv6前缀与路由器本身、相连的stub网段或相连的transit网段相关。 
其中Link LSA和Intra Area Prefix LSA两种LSA是OSPFv3新增的。
业务流程 : 
不涉及。 
系统影响 : 
OSPFv3路由协议是ZXUN uMAC的标准组网协议，对网络内其他业务无影响，但报文发送时需查找的路由数量越多，消耗的性能越高。
应用限制 : 
OSPFv3是IGP，仅适用于同一个自治系统内，不同自治系统的网元设备相互通信需要使用EGP。
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准类别|标准名称
---|---
IETF|RFC 2740 OSPF for IPv6RFC 2328 OSPF Version 2RFC 3101 The OSPF Not-So-Stubby Area (NSSA) Option 1-9RFC 3137 OSPF Stub Router AdvertisementRFC 3630 Traffic Engineering Extensions to OSPF Version 2RFC 4811 OSPF Out-of-Band LSDB ResynchronizationRFC 4812 OSPF Restart SignalingRFC 4813 OSPF Link-Local SignalingRFC 5187 OSPFv3 Graceful Restart
特性能力 : 
名称|指标
---|---
整局支持最大路由数目|100000
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
ipv6 router ospf|创建OSPFv3进程
area|创建OSPFv3的区域
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
ZXUN uMAC上开启OSPFv3进程，使ZXUN uMAC与对端网元设备之间通过OSPFv3协议学习路由。
配置前提 : 
 
ZXUN uMAC业务配置正确，可以正常接入用户。 
 
当需要配置带VRF的OSPF路由协议时，需要保证管理的VRF信息已配置。 
 
配置过程 : 
步骤|配置说明|配置步骤
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置OSPFv3基本功能|创建OSPFv3进程ipv6 router ospf创建OSPFv3的区域area配置路由器的router-idrouter-id
3|配置OSPFv3接口属性|除了interface命令，其余命令都可以采用默认值。进入IPv6-OSPF接口模式。interface配置OSPFv3特定接口的认证密钥。authentication配置OSPFv3特定接口的密钥encryption配置特定接口的双向转发检测属性。bfd配置特定接口的cost值。cost指定接口发送Hello报文的时间间隔。hello-interval配置该接口接收Hello报文的最大时间间隔。dead-interval指定接口重传LSA的时间间隔。retransmit-interval指定接口传输一个链路状态更新数据包的延迟。transmit-delay抑制接口产生8型link LSA。linklsa-suppress配置接口类型为non-broadcast或point-to-multipoint的网络中的相邻路由器。neighbor配置接口优先级。priority
4|（可选）配置OSPFv3区域|可以采用默认值，如果有特殊需求可以自行修改。进入IPv6–OSPF区域模式。area配置OSPFv3的区域为stub区域。stub配置stub区域的默认路由的度量值。default-cost配置OSPFv3的区域下所有接口认证。authentication配置区域下所有接口的双向转发检测属性。bfd配置OSPFv3区域下所有接口的密钥。encryption配置区域内的汇总地址范围。range定义OSPFv3虚拟链路。virtual-link
5|（可选）配置OSPFv3认证|可以采用默认值，如果有特殊需求可以自行修改。配置OSPFv3某个区域的认证authentication进入OSPFv3接口配置模式interface使用简单口令认证类型的接口设置口令authentication-key
6|（可选）配置OSPFv3路由其他选项|配置OSPFv3实例的缺省路由notifydefault route配置所有接口的BFD属性bfd配置OSPFv3路由管辖距离distanceospf配置OSPFv3协议负载均衡时支持的最大路由数目maximum-paths配置本OSPFv3实例支持无中断转发能力nsf配置NSF运行所需的最长时间grace-period配置distribute-list过滤路由distribute-list配置本设备引入其他协议学习到的路由信息redistribute
配置实例 : 
场景说明 : 
ZXUN uMAC与R1通过两条链路建链，通告各自的一个回环地址路由。
数据规划 : 
接口名称|接口IP地址/掩码位数
---|---
gei-0/3/0/6|3611::11/64
loopback5|3555::52/64
OSPF实例号|OSPF区域ID号|本端route-id
---|---|---
1|0（或者0.0.0.0）|0.0.0.1
配置步骤 : 
步骤|说明|操作
---|---|---
1|进入ROSNG配置模式|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点，在下方区域框中选择Rosng配置管理→router配置，进入ROSNG配置模式。
2|配置接口启用IPv6协议|配置接口IPv6的基本信息。ZXROSNG(config)#interface gei-0/3/0/6ZXROSNG(config-if-gei-0/3/0/6)#ipv6 enableZXROSNG(config-if-gei-0/3/0/6)#ipv6address 3611::11/64ZXROSNG(config-if-gei-0/3/0/6)#exit配置环回接口IPv6的基本信息。ZXROSNG(config)#interface loopback5ZXROSNG(config-if-loopback5)#ipv6 enableZXROSNG(config-if-loopback5)#ipv6address 3555::52/64ZXROSNG(config-if-loopback5)#exit
3|配置OSPFv3基本功能|创建OSPFv3进程，OSPF实例号为1：ZXROSNG(config)#ipv6 routerospf 1配置路由器的router-id：ZXROSNG(config-ospfv3-1)#router-id0.0.0.1
4|配置OSPFv3接口属性|ZXROSNG(config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#interfacegei-0/3/0/6ZXROSNG(config-ospfv3-1-area-0-if-gei-0/3/0/6)#exitZXROSNG(config-ospfv3-1-area-0)#interface loopback5
5|保存数据|ZXROSNG(config-ospfv3-1-area-0-if-loopback5)#endZXROSNG#write
调整特性 : 
不涉及。 
测试用例 : 
测试项目|OSPFv3建链功能
---|---
测试目的|验证OSPF路由正确发布
预置条件|基础配置完成。ZXUN uMAC业务配置正确，可以正常接入用户。
测试过程|开启OSPF进程，并将接口加入OSPF域内。
通过准则|OSPF路由能生效，邻居建链成功，能正确生成路由。
测试结果|–
常见问题处理 : 
不涉及。 
# ZUF-76-07 信令 
## ZUF-76-07-001 M3UA 
概述 : 
ZXUN uMAC提供IP协议的信令传输。 
客户收益 : 
SIGTRAN协议栈支持通过IP网络传输SCN信令协议。该协议栈支持SCN信令协议分层模型定义中的层间标准原语接口，保证现有SCN信令应用在不进行任何更新的情况下同时使用，并将标准IP传输协议作为传输低层，通过增加自身的功能来满足SCN信令的独特传输需求。 
说明 : 
SIGTRAN包含两层：传输层和UA层。传输层协议通过SCTP（流控制传输协议）在IP网络上提供可靠的报文传输。UA层在SCN信令协议分层模型中对每种协议进行适配，分别负责SCN和IP协议之间的层间原语传输。典型的SIGTRAN协议栈如下图所示。 
图1  典型的SIGTRAN协议栈
SCTP是IP网络的信令承载，实现基于IP的公共分组交换网络的交流、端到端执行流量控制和差错控制。 
SCTP包含以下功能： 
连接状态和数据收发的管理分为连接建立和拆除、数据收发处理和连接管控。 
建立和拆除连接包括处理连接状态变化和处理异常。 
数据收发信处理的传输部分完成用户应用数据的接收和分片，缓冲数据分配，根据当前网络拥塞状态和对端接收缓冲状态发送数据，将数据挂在等待确认队列中，设置等待超时定时时间，并做好RTT（往返时延）测量准备。接收部分负责分片数据和无序数据的缓冲、恢复、确认和再生。值得注意的是，一个连续的数据收发处理受连接状态和存储在连接控制块中的其他控制信息的控制，并随着其他功能模块的运行而变化。 
连接管控部分中的拥塞控制和窗口管理对滑动窗口进行管理。加速、减速、慢启动和拥塞的整个控制机制是由对端选择确认中携带的信息和超时消息的传输触发的，在此过程中，这些消息和信息的输出影响了连接控制块中拥塞窗口、接收窗口、慢启动阈值和往返超时时间的控制信息。 
路径管理对连接的多个路径实施可访问性检测（心跳），并将相应信息上报到用户应用协议。 
M3UA表示MTP第三层的用户适配层协议，支持： 
SS7 MTP3用户部分承载在IP之上的信息传输（SCCP等）。 
基于IP的分布式信令节点；CTP传输连接管理。 
MTP3用户协议对端层的无缝运行；MTP3
网管功能；以及协议层关键数据实时观测功能。 
## ZUF-76-07-002 SCCP 

概述 : 
SCCP：信令连接控制协议，SS7的一部分。支持SCCP负荷分担和SCCP屏蔽。 
客户收益 : 
提供SCCP通信。 
说明 : 
SCCP是ITU建立的SS7（7号信令系统）中的一个协议。SCCP提供MTP的补充功能，在交换机、交换机和专用中心之间传输电路相关和无关的信令信息，并建立无连接和面向连接的网络服务。 
ZXUN uMAC支持SCCP的负荷分担。GT（全局名）被转换成DPC（目的地信令点编码）。基于DPC，共16个局向可以进行负荷分担。 
ZXUN uMAC支持SCCP屏蔽。屏蔽条件根据来源地址和目标地址的组合进行设置。符合屏蔽条件的消息会被舍弃。SCCP根据屏蔽条件判断接收到的消息，并将其中符合条件的消息舍去。 
## ZUF-76-07-003 MAP 
概述 : 
SGSN使用MAP协议作为部分接口的标准协议。 
客户收益 : 
该特性支持基于MAP协议的标准定义接口。 
说明 : 
MAP是一个应用层协议，广泛用于SGSN的七号信令接口。Gr、Gd以及Gf协议接口使用MAP信令。 
## ZUF-76-07-004 TCAP 

概述 : 
TC（事物处理能力）协议是一种统一的电路无关消息传输协议。协议执行过程与消息结构和特定的应用程序无关。TC包括TCAP（事物处理能力应用部分）和ISP（中间业务部分）。TCAP提供OSI参考模型中第七层的功能，ISP提供第四到第六层的功能。根据不同要求，TC可以分为面向连接的TC和连接无关的TC。 
客户收益 : 
该特性提供标准接口。 
说明 : 
为了统一支持应用服务，TCAP将不同节点之间的消息交互抽象为一个“操作”过程。也就是说，开始节点触发一个操作后，目标节点执行该操作并向开始节点返回执行结果。为了完成某个业务过程，两个节点的多个对等实体之间可能会触发大量操作，执行这些组合在一起的相关操作形成一次“对话”，即一次事物处理。这种操作模型类似和计算机进行一次人机对话。就像对话语句由一些简单的单词组成一样，TCAP消息由一些基本的块/元素组成。一个元素对应一个操作请求或响应，而一条消息（对话）可能包含多个元素。因此，一定量的元素可以组成大量消息。TCAP可应用于以下业务：移动通信业务、涉及专用服务节点的补充业务的注册、激活和触发、电路无关信息的传输以及网络运维。 
## ZUF-76-07-005 RANAP 

概述 : 
ZXUN uMAC提供RAN的RANAP功能，包括向UTRAN发送CN（核心网）信令，在CN和UTRAN之间交换信息，以及在UTRAN中实施UE-CN（接入层除外）的透明传输控制信令。 
客户收益 : 
该特性提供了WCDMA中RNC与接入网之间的必要协议。 
说明 : 
RANAP协议功能如下所列： 
 
迁移服务RNC。该功能支持将服务RNC功能以及相关Iu资源（RAB和信令连接），从一个RNC切换到另一个RNC。 
 
整体RAB管理。该功能负责RAB的建立、修改和释放。 
 
RAB列队。该功能的目的是允许将一些请求的RAB放入队列，并指示对端实体关于该队列。 
 
请求RAB释放。当CN具备整体RAB管理功能时，RAC可请求释放RAB。 
 
释放全部IU连接资源。该功能用于明确释放与一个Iu连接有关的全部资源。 
 
请求释放所有Iu连接资源。当Iu释放由CN管理时，RNC可以请求释放相应Iu连接中的全部Iu连接资源。 
 
转发SRNS上下文。该功能负责在报文转发时将SRNS上下文从RNC转发到CN进行系统间变更。 
 
控制Iu接口的过载。该功能允许调整Iu接口的负载。 
 
重置Iu接口。该功能用户重置Iu接口。 
 
向RNC发送UE公共ID（永久NAS UE身份）。该功能可让RNC识别UE公共ID。 
 
寻呼用户。该功能为CN提供寻呼UE的能力。 
 
控制UE活动跟踪。该功能允许为指定的UE设置一个跟踪模式。同时，支持去活之前建立的跟踪。 
 
在UE和CN之间传输NAS信息。该功能含有两个子类：
将初始NAS信令消息从UE传输到CN。该功能透明地传输NAS消息，从而建立Iu信令连接。
在UE和CN之间传输NAS信令消息。该功能在现有的Iu信号连接上透明地传输NAS信令消息。此外，该功能还包含一个特定的服务，以不同方式处理信令消息。
 
 
控制UTRAN中的安全模式。该功能用于发送安全密钥（加密和完整性保护）给UTRAN并设置运行模式以实现安全功能。 
 
控制位置上报。该功能允许CN操作UTRAN上报UE位置的模式。 
 
上报位置。该功能用于将实际的位置信息从RNC传输到CN。 
 
上报数据量：该功能负责上报特定RAB在UTRAN上未成功传输的DL数据量。 
 
上报整体错误情况。该功能允许上报一般错误情况，对于这些情况，没有定义具体功能的错误消息。 
 
位置相关数据。该功能允许CN从RNC解密密钥（需转发给UE）中提取广播辅助数据，或者请求RNC向UE下发专用辅助数据。 
 
## ZUF-76-07-006 BSSGP 

概述 : 
SGSN使用BSSGP协议作为Gb接口的标准协议。 
客户收益 : 
该特性提供标准接口。 
说明 : 
BSSGP就是BSS GPRS Protocol BSS-GPRS协议。BSSGP主要功能是提供无线数据、QoS和选路信息，以满足在BSS和SGSN之间传输用户数据时的需要。在BSS中，BSSGP用作LLC帧和RLC/MAC块之间的接口；在SGSN中，BSSGP形成一个RLC/MAC和LLC帧之间的接口。SGSN和BSS之间的BSSGP协议具有一一对应关系，如果一个SGSN处理多个BSS，这个SGSN对于每一个BSS都必须有一个BSSGP协议机制。 
## ZUF-76-07-007 BSSAP PLUS 

概述 : 
SGSN使用BSSAP PLUS协议作为Gs接口的标准协议。 
客户收益 : 
该特性提供标准接口。 
说明 : 
BSSAP PLUS用于支持Gs接口上VLR（拜访位置寄存器）和SGSN（服务GPRS支持节点）之间的信令。 
图1  BSSAP PLUS
## ZUF-76-07-008 GTP 
概述 : 
SGSN/MME使用GTP协议作为Gn/Gp/S11/S10接口的标准协议。 
客户收益 : 
SGSN/MME使用GTP协议作为Gn/Gp/S11/S10接口的标准协议。 
说明 : 
ZXUN uMAC支持标准的GTP协议。 
支持GTP协议版本返回，使用低版本的GTP协议，不支持高版本。 
支持GSN节点的有效性以及通过Recover（恢复）值重启节点。 
支持将无效节点加入GTP节点黑名单，以过滤后续节点；支持配置GTP节点白名单，以避免误将不支持回声检测的节点加入到黑名单。 
支持错误Indicate（指示）消息和GTPU。 
## ZUF-76-07-009 S1AP 

概述 : 
MME使用S1AP协议作为S1接口的标准协议。 
客户收益 : 
实现MME和eNodeB之间的信令交换。 
说明 : 
S1是EPC和E-UTRAN之间的接口，EPC侧的接入点是控制面MME或用户面SGW。eNodeB与MME之间的连接是S1控制面接口，称为S1-MME接口。和SGW之间的连接是S1用户面接口，称为S1-U接口。S1-MME接口实现了基于SCTP的S1AP和NSA协议，其协议栈如下图所示。 
图1  协议栈
## ZUF-76-07-010 SGsAP 

概述 : 
SGs是MME和VLR NE之间的接口。 
MME使用SGsAP协议作为SGs接口的标准协议。 
客户收益 : 
MME通过SGs完成与VLR NE的网络互连。 
说明 : 
SGs在SCTP连接上，其协议栈如下图所示。 
图1  协议栈
## ZUF-76-07-011 Diameter 
概述 : 
MME使用Diameter作为S6a口和计费接口的标准协议，MME作为Diameter客户端位于执行访问控制的网络的边缘。Diameter客户端生成Diameter消息，请求用户的鉴权、授权以及计费业务。 
客户收益 : 
Diameter客户端的基础功能就是在协议的基础上支持Diameter。 
说明 : 
Diameter客户端位于执行访问控制的网络的边缘。Diameter客户端生成Diameter消息，请求用户的鉴权、授权以及计费业务。 
ZXUN uMAC支持Diameter客户端功能。在Diameter链路未建立时，ZXUN uMAC执行链路建立并处理相关消息。当Diameter链路建立失败时，根据配置的时间间隔，MME可以连续尝试建立链路。Diameter链路创建后，ZXUN
uMAC处理响应消息。 
## ZUF-76-07-012 GTP' 

概述 : 
SGSN使用GTP'协议作为Ga接口的标准协议。 
客户收益 : 
实现SGSN和CG之间的交互。 
说明 : 
ZXUN uMAC支持标准的GTP'协议（增强型GTP），以保证CDR传输的可靠性。 
## ZUF-76-07-013 NGAP 
概述 : 
AMF使用NGAP协议作为N2接口的标准协议。 
客户收益 : 
实现AMF和gNodeB之间的信令交换。 
说明 : 
NGAP提供NG-RAN节点和AMF之间的信令服务，满足TS 38.410[3]中描述的NGAP功能。NGAP业务分为以下两类： 
非UE相关业务：这些业务与NG-RAN节点和使用非UE相关信令连接AME之间的整个NG接口实例有关。 
UE相关业务：这些业务与UE相关。提供这些服务的NGAP功能与为相关UE维护的UE相关信令连接相关。 
NGAP协议栈如下： 
图1  NGAP协议栈
NG-AP（NG应用协议）：5G-AN节点与AMF之间的应用层协议。TS 38.413 [34]中对NG-AP进行了定义。 
SCTP（流控制传输协议）：该协议保证AMF与5G-AN节点（N2）之间的信令消息传输。RFC 4960 [44]中对SCTP进行了定义。 
# ZUF-76-08 DNS客户端 
## ZUF-76-08-001 DNS客户端 

概述 : 
ZXUN uMAC支持DNS客户端与DNS服务器交互，从DNS服务器获取有用信息。 
客户收益 : 
配置DNS客户端向DNS服务器发送名称解析查询，用于管理业务屏蔽链路、服务器选择等。DNS查询用于NF寻址和NF选择等过程。 
说明 : 
ZXUN uMAC支持DNS客户端的以下基本功能： 
 
支持A类和AAAA类查询 
 
支持针对服务器的S-NAPTR查询 
 
支持缓存功能 
 
支持DNS递归查询 
 
DNS服务器查询支持备份和负荷分担 
 
支持DNS服务器链路检测 
 
支持DNS缓存刷新 
 
DNS响应消息中支持多个IP地址 
 
支持DNS解析的S-NAPTR 
 
支持CNAME记录 
 
支持选择不同的DNS服务器进行GPRS、LTE查询 
 
SGSN/MME/AMF支持基于UDP和TCP的DNS客户端。UDP模式只能处理不超过512字节的查询结果，TCP模式支持超过512字节的查询结果。SGSN/MME/AMF支持UDP和TCP模式的选择和切换，当UDP响应报文超长截断时，SGSN/MME/AMF采用TCP模式进行查询。 
# ZUF-76-09 时钟和NTP 
## ZUF-76-09-001 时钟和定时器管理 
特性描述 : 

特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
为了保证ZXUN uMAC与其他网元协调工作，需要准确设置ZXUN uMAC时间信息，包括配置时间和时区。
ZXUN uMAC通过此功能给运营商能提供时钟和时区维护命令。
 说明： 
在中国采用首都北京所在地东八区的时间为全国统一使用时间。 
背景知识 : 
时区（Time Zone)是地球上的区域使用同一个时间定义。整个地球按照经度被划分为24个时区，绕地球一周的经度共360度，所以每个时区的范围是15度。每两个邻区间的本地时间间隔1小时，东部区域时间比西边区域时间早1小时。 
以0度经线（本初子午线，经过英国伦敦东南Greenwich）为基准，向东向西各延伸7.5度，这一部分地区（东经7.5度至西经7.5度之间）就称作0时区。在中国采用首都北京所在地东八区的时间为全国统一使用时间。 
应用场景 : 
本特性无应用场景限制，适用于所有的5GC移动网络。 
客户收益 : 
受益方|受益描述
---|---
运营商|依靠正确的时间，才能处理各种业务，包括计费等。
终端用户|系统稳定运行，给用户提供更好业务体验。
实现原理 : 
系统架构 : 
不涉及。 
涉及的网元 : 
网元名称|网元作用
---|---
ZXUN uMAC|使系统时区和时间与ZXUN uMAC所在地区的时区和时间保持一致。
本网元实现 : 
系统正常工作必须要配置系统时钟，系统时钟包括时区配置和时间配置。 
业务流程 : 
不涉及。 
系统影响 : 
该特性会影响系统时间。在性能统计、告警和日志中记录的时间的准确性会因此受到影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
该特性不涉及遵循标准。 
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
SET TIMEZONE|此命令用于时区配置。
SET TIME|此命令用于设置ZXUN uMAC时间。
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
为了保证ZXUN uMAC与其他网元协调工作，需要准确设置ZXUN uMAC的系统时间信息。
配置前提 : 
操作人员已经登录EM系统。 
配置过程 : 
在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点。
使用命令[SET TIMEZONE]，配置系统的时区。
使用命令[SET TIME]，配置系统的时间。
配置实例 : 
场景说明 : 
ZXUN uMAC处于中国地区。
数据规划 : 
对应的时区为东八区，比UTC时间晚8个小时，修改系统时间为2019年6月12日14点52分01秒100毫秒。 
配置步骤 : 
步骤|说明|操作
---|---|---
1|进入配置页面|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点。
2|设置时区为东八区。|在时区配置里执行如下命令：SET TIMEZONE:TIMEZONE="GMTE0800"
3|修改系统时间为2019年6月12日14点52分01秒100毫秒。|在时间管理里执行如下命令：SET TIME:TIME=2019-06-1214:52:01,MSEC=100
调整特性 : 
不涉及。 
测试用例 : 
测试项目|时钟与时间管理
---|---
测试目的|测试时区配置和修改时间的准确性。
预置条件|基本配置完成。
测试过程|修改系统时区为东八区。修改当前时间为2019年6月12日14点52分01秒100毫秒。
通过准则|时区和时间正常，与修改值一致。
测试结果|-
常见问题处理 : 
不涉及。 
## ZUF-76-09-002 NTP 
特性描述 : 

特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
NTP网络时间协议定义了时间服务器和其他设备之间进行时间同步的策略和算法，用于保持全网时间的同步。
NTP的作用是对网络内所有具有时钟的设备进行时间同步，使网络内所有设备的时钟时间基本保持一致，使设备能够提供基于统一时间的多种应用。实际应用中，NTP能够提供1ms～50ms时间精确度。 
ZXUN uMAC采用了NTP的客户端/服务器模式进行时间同步。ZXUN uMAC作为时间客户端向局域网中的时间服务器来请求标准时间，以确保ZXUN uMAC的本地时间与时间服务器的时间保持同步。通常使用EM服务器作为NTP时间服务器。
背景知识 : 
在实际使用中，为了满足不同情况下的网络时钟同步需求，根据网络部署情况选择适当的工作模式，NTP有以下四种工作模式。
 
客户端/服务器模式客户端定期向服务器发送NTP报文同步时钟。 
 
对等体模式主动对等体和被动对等体可以互相同步，等级低（层数大）的对等体向等级高（层数小）的对等体同步。 
 
广播模式服务器周期性的向广播地址发送时钟同步报文，客户端根据收到的广播消息同步本地时钟。 
 
组播模式服务器周期性的向组播地址发送时钟同步报文，客户端根据收到的组播消息同步本地时钟。 
 
应用场景 : 
本特性应用于需要网络中所有设备的时钟保持一致的场景，包括但不局限于以下场景。 
 
网络管理系统：对从不同设备收集来的日志信息、调试信息进行分析时，需要以时间作为参照依据。 
 
计费系统：要求所有设备的时钟保持一致。 
 
客户收益 : 
受益方|受益描述
---|---
运营商|NTP功能可以使各设备保持时间同步，便于准确进行设备维护和故障处理，包括不限于话单，日志等。对于网络中的众多设备，如果依靠管理员手工输入命令来修改系统时钟，不仅工作量巨大，也不能保证时钟的精确性。通过配置NTP，可以很快将网络中设备的时钟同步，同时保证很高的精度。
终端用户|系统稳定运行，给用户提供更好业务体验，包括不限于话费更准确。
实现原理 : 
系统架构 : 
NTP的系统架构如[图1]所示。
图1  NTP系统架构原理
涉及的网元 : 
网元名称|网元作用
---|---
NTP服务器|通常使用EM服务器作为NTP时间服务器。作为ZXUN uMAC进行时钟同步的时钟源。
ZXUN uMAC|作为NTP客户端，连接NTP服务器，以NTP服务器作为时钟源，获取标准时间，并据此调整自身时间与标准时间同步。
本网元实现 : 
NTP的基本工作原理如[图2]所示。
图2  NTP系统架构原理
Device A和Device B通过网络相连，Device A和Device B都有自己独立的系统时钟，需要通过NTP实现各自系统时钟的自动同步。为便于理解，作如下假设，
 
在Device A和Device B的系统时钟同步之前，Device A的时钟设定为10:00:00am，Device
B的时钟设定为11:00:00am。 
 
Device B作为NTP时间服务器，即Device A将使自己的时钟与Device B的时钟同步。 
 
业务流程 : 
如[图2]所示，业务流程如下：
NTP报文在Device A和Device B之间单向传输所需要的时间为1秒。Device A发送一个NTP报文给Device B，该报文带有此报文离开Device
A时的时间戳，该时间戳为10:00:00am（T1）。
当此NTP报文到达Device B时，Device B加上自己的时间戳，该时间戳为11:00:01am（T2）。
当此NTP报文离开Device B时，Device B再加上自己的时间戳，该时间戳为11:00:02am（T3）。
当Device A接收到该响应报文时，Device A的本地时间为10:00:03am（T4）。
至此，Device A已经拥有足够的信息来计算两个重要的参数， 
NTP报文的往返时延Delay=（T4-T1）-（T3-T2）=2秒。
Device A相对Device
B的时间差offset=（（T2-T1）+（T3-T4））/2=1小时。
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
只有网络中部署了NTP服务器，本特性才能正常使用。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准类别|标准名称
---|---
RFC 1059|Network Time Protocol (Version 1)
RFC 1119|Network Time Protocol (Version 2)
RFC 1305|Network Time Protocol (Version 3)
RFC 5905|Network Time Protocol (Version 4)
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
SET NTP|启动NTP功能，并设置NTP相关参数，如NTP服务器地址等。
ADD NTPKEY|配置NTP密钥。
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 

特性配置 : 
配置说明 : 
本操作指导介绍在运行网络中配置NTP的操作过程。 
配置前提 : 
 
操作人员已经登录EM系统。 
 
NTP服务器已正常工作，ZXUN uMAC只支持配置为客户端。 
 
配置过程 : 
在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点。
使用[SET NTP]命令，启动NTP功能且配置相关参数。
配置实例 : 
场景说明 : 
操作员通过开启NTP功能，完成NTP客户端地址，服务器地址等相关配置后，可以正常使用NTP功能。 
数据规划 : 
规划NTP主用服务器IP地址为10.43.1.1，NTP备用服务器地址为2001::1。 
配置步骤 : 
步骤|说明|操作
---|---|---
1|进入配置页面|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点。
2|启用NTP服务，配置主服务器IP地址为"10.43.1.1"，次服务器地址为"2001::1"|在NTP配置里执行如下命令：SET NTP:ENABLE="YES",PRIMARYADD=10.43.1.1,SECADD=2001::1
调整特性 : 
不涉及。 
测试用例 : 
测试项目|NTP功能
---|---
测试目的|验证NTP功能，能正常进行时钟同步。
预置条件|基础配置完成。上级NTP服务器正常。
测试过程|启用NTP并配置参数。修改NTP服务器时钟，NTP客户端能够同步。
通过准则|NTP时钟同步正常，本地时间跟NTP服务器时间一致。
测试结果|-
常见问题处理 : 
不涉及。 
## ZUF-76-09-003 夏令时功能 
特性描述 : 
特性描述 : 
适用网元 : 
可能的适用网元：AMF、MME、SGSN 
描述 : 
定义 : 
夏时制，夏时令（DST），又称“日光节约时制”和“夏令时间”，是一种为节约能源而人为规定地方时间的制度，在这一制度实行期间所采用的统一时间称为“夏令时间”。一般在天亮早的夏季人为将时间提前一小时，可以使人早起早睡，减少照明量，以充分利用光照资源，从而节约照明用电。
ZXUN uMAC支持夏令时配置。
背景知识 : 
夏令时也叫夏时制，是某些国家和地区实行的时间调整制度。 
高纬度地区由于夏季太阳升起时间明显比冬季早，人为将时间提前一小时，减少照明量，以充分利用光照资源，从而实现节约能源。目前全世界有近110个国家每年要实行夏令时。 
每个国家的夏时制实施方式有所不同，比如美国的实施方法为：在每年3月份的第二个礼拜日凌晨2点将时间向前偏移1个小时，在每年11月份的第一个礼拜日凌晨2点将时间向后偏移一小时。简单讲，就是在春天将时间提前一小时，在秋天将时间推迟一小时。 
应用场景 : 
本特性适用于可以根据本国或本地区的规定，自由地定制实行夏令时的地区。 
客户收益 : 
受益方|受益描述
---|---
运营商|满足用户需求，提供夏令时服务，减少能源消耗。
终端用户|实现夏令时，用户感受到夏令时时段，需要早起一个小时。
实现原理 : 
系统架构 : 
不涉及。 
涉及的网元 : 
网元名称|网元作用
---|---
ZXUN uMAC|夏令时功能启用之后，当进入夏令时实施区间的一刻，系统时间会根据用户的设定进行夏令时时间的调整。当到达夏令时实施区间的结束时刻，系统时间会自动向前调整与设置偏移等同的时间长度，恢复正常的时间设置。
本网元实现 : 
鉴于地球在围绕太阳旋转时，地轴稍有偏斜，从而导致地球上除了赤道附近以外的地区，冬季日照较短，夏季日照较长。 
以北京为例，冬至是一年之中日照最短的一天，日出时间为7时33分（天亮时间为7时6分），日落时间为16时53分（天黑时间为17时20分），日照时间9小时20分。夏至是一年中日照最长的一天，日出时间为4时46分（天亮时间为4时19分），日落时间为19时47分（天黑时间为20时14分），日照时间15小时1分。 
实施夏令时，就是在日照较长的月份，将自然时间向前拨一个小时。从而使人们早晨可以提前一个小时起床，晚上入寝休息也提前一个小时。由此来节约夜间的照明能源。 
实施夏令时，也就是将自然时间向前拨一个小时，未设置前为8时，设置后，这个时间点为9时，所以需要提前一个小时起床。 
进入夏令时时段后，系统时间比当地所在时区快了1小时，退出夏令时时段后，系统时间又恢复到正常，如[图1]所示。
图1  系统原理
业务流程 : 
不涉及。 
系统影响 : 
使用夏令时后，系统的时间采用经过夏令时调整过的本地时间。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
该特性不涉及遵循标准。 
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
O&M相关 : 
命令 : 
命令名称|描述
---|---
SET DAYLIGHTSAVE|该命令用于ZXUN uMAC设置夏令时。
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
本节介绍当ZXUN uMAC所在地需要启用夏令时功能时，如何对夏令时功能进行设置。
配置前提 : 
操作人员已经登录EM系统。 
配置过程 : 
在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点。
使用命令[SET DAYLIGHTSAVE]，配置夏令时。
配置实例 : 
场景说明 : 
ZXUN uMAC支持配置两种格式的夏令时：
基于绝对日期格式的夏令时只需要设置一次，以后每年都根据固定的进入和退出夏令时的月、时、日、分循环执行。 
基于相对日期格式的夏令时只需要设置一次，以后每年都根据相对的进入和退出夏令时的月、星期、时、分循环执行。 
###### 规划数据 
配置绝对格式的夏令时，起始时间为5月1日12点，终止时间为9月1日0点。 
配置相对格式的夏令时，起始时间为3月第一个星期日0点，终止时间为9月最后一个周六的12点。 
配置步骤 : 
步骤|说明|操作
---|---|---
1|进入配置页面|在EM客户端，切换到配置页面，在配置页面的左侧命令树中，展开需要配置的某个NF节点，选择CommonS_TMSP_0节点。
2|配置夏令时|配置绝对格式的夏令时起始时间为5月1日12点，终止时间为9月1日0点：SETDAYLIGHTSAVE:ENABLE="Absolute",ABSSTARTTIME="05-01 12:00",ABSENDTIME="9-100:00"配置相对格式的夏令时起始时间为3月第一个星期日0点，终止时间为9月最后一个周六的12点：SET DAYLIGHTSAVE:ENABLE="Relative",STARTMONTH="Mar",STARTWEEKNO="First",STARTWEEKDAY="Mon",STARTTIME="00:00",ENDMONTH="Sep",ENDWEEKNO="Last",ENDWEEKDAY="Sat",ENDTIME="12:00"
调整特性 : 
不涉及。 
测试用例 : 
测试项目|夏令时功能
---|---
测试目的|测试夏令时配置数据是否生效。
预置条件|基本配置完成。
测试过程|配置夏令时起始时间、终止时间，调整方式为向后偏移1小时。
通过准则|当前时间进入到夏令时起始时间后，当前系统时间增加1小时。当前时间离开夏令时终止时间后，当前系统时间减少1小时，恢复夏令时起始前的时间。
测试结果|-
常见问题处理 : 
不涉及。 
# ZUF-76-10 操作维护 
## ZUF-76-10-001 故障管理 

概述 : 
故障管理功能支持告警和通知，并向运营商提供故障详情。该功能会随时通知用户当前系统状态，并及时发现故障。 
客户收益 : 
为操作员提供便捷的系统管理工具。 
说明 : 
根据严重程度，告警分为四级：一级代表最高级别，四级代表最低级别。 
告警分为五类，包括通信告警、处理错误告警、QoS告警、设备告警和环境告警。如果发生故障，将产生告警。当故障修复或消失后，恢复相应的告警。 
通知是指操作员必须知道的某些事件时需要上报的消息，但并不表示有故障发生。通知不需要恢复。 
故障管理主要由当前告警、通知、历史告警和告警设置四个功能部分组成。 
实时显示当前告警/通知：当前告警列表将现有未恢复的告警显示给用户。告警信息包括告警源、级别、产生时间、内容、原因、类型和附加信息。实时通知列表显示接收到的通知。通知信息包括通知生成时间、源、内容和附加信息。 
查询历史告警/通知：操作员查询历史告警和通知，而且可以设置查询条件。 
告警设置：包括环境参数设置、告警过滤规则设置和告警抑制设置。 
## ZUF-76-10-002 性能统计 
概述 : 
性能管理提供系统性能参数和流量的测量功能。 
客户收益 : 
性能管理通过测量性能参数和业务数据来检验移动系统的性能，为网络规划和故障处理提供数据支持。 
说明 : 
性能管理包括以下功能： 
测量任务管理 
性能阈值监控 
性能查询 
性能数据导出和备份 
系统的运行主要分为三个部分： 
性能查询：查询和分析性能测量任务的数据。 
性能监控：对性能阈值任务数据进行实时监控和历史监控。 
性能定制：执行测量任务/阈值任务定义、性能数据导出和备份、性能测量对象管理等操作。 
## ZUF-76-10-003 配置管理 
概述 : 
配置管理是对NF的资源进行配置和管理。该功能执行NF配置修改和扩容，并为实现这些要求提供灵活的支持。 
客户收益 : 
支持灵活配置和修改NF的特性，使设备能够根据实际需求处理各种网络应用。 
说明 : 
配置管理包括本地配置、接入区域配置、NF选择配置、安全配置等。 
## ZUF-76-10-004 安全管理 
概述 : 
安全管理包括创建、删除和修改用户，以及修改和设置用户权限。 
客户收益 : 
安全管控操作维护操作员的权限。不同用户具有不同的操作权限，以保证维护的安全性。 
说明 : 
安全管理包括用户管理和角色管理。 
根据权限级别从高到低，预定义的角色类型有四种：系统管理员、系统维护员、系统操作员和系统监控员。在用户管理中，操作员设置用户角色，赋予用户相应角色的权限。 
用户管理包括以下特性： 
创建用户 
删除用户 
修改用户信息 
角色管理涉及以下特性： 
创建角色 
删除角色 
修改角色信息 
## ZUF-76-10-005 日志管理 
概述 : 
日志管理支持查询操作日志、安全日志和系统日志。 
客户收益 : 
操作日志记录了客户端发起并由服务器处理的所有操作。对于异常操作引起的故障，需要对异常操作前的操作进行分析，以定位和解决故障。 
安全日志记录了操作员登录/注销等安全操作，满足安全审计的要求。 
系统日志记录了系统执行的重要操作，用于分析系统的运行状态。 
说明 : 
日志管理包括日志查询、日志统计、日志输出和NF日志查询。 
日志查询包括以下功能： 
操作日志：提供操作日志查询功能，可查询操作员、级别、操作时间和操作内容。 
安全日志：提供安全日志查询功能，可查询用户名、操作时间、日志名称、主机地址和访问方式。 
系统日志：提供系统日志查询功能，可查询日志名称、级别、来源和操作时间。 
日志统计包括以下特性： 
操作日志：提供按级别、操作接口、Top5操作、Top5地址和Top5用户的操作日志统计。 
安全日志：提供按Top5日志名称、Top5地址和Top5用户的安全日志统计。 
系统日志：提供按级别、Top5来源和Top5日志名称的系统日志统计。 
日志输出包括以下特性： 
文件输出：将日志文件输出到指定的FTP服务器中。 
Syslog输出：将Syslog输出到指定的Syslog服务器中。 
NF日志查询包括以下功能： 
操作日志：提供NF操作日志查询功能，可查询操作员、级别、操作时间和操作内容。 
安全日志：提供NF安全日志查询功能，可查询用户名、操作时间、日志名称、主机地址和访问方式。 
系统日志：提供NF系统日志查询功能，可查询日志名称、级别、来源和操作时间。 
## ZUF-76-10-006 MML终端 

概述 : 
MML终端是一个人机交互工具，可显示配置管理、性能管理、故障管理和人机命令响应的收发信息，是用户维护系统的辅助工具。 
客户收益 : 
MML终端提供人机交互的快捷方式、友好的接口和多样化的人机命令。此外，还为系统运维提供强大的支持和辅助。 
方便快捷：通过下发人机命令，可以直接便捷地获取指定系统的运行状态信息，方便用户分析当前系统的运行状态，帮助定位系统的异常运行状态。 
友好便捷的接口：提供友好方便的接口，支持命令处理、结果显示、命令提示、帮助和辅助设置。 
丰富的人机命令：提供配置管理、性能管理、故障管理等人机命令，支持增加、删除、查询、修改系统运行状态和状态参数。此外，还能有效地支持系统运维。 
说明 : 
NF命令行接口采用主流的人机交互模式。命令语言结构简单、易学、易用，还提供在线帮助和错误提示。 
此外，命令行支持批量输入脚本并立即执行，灵活且易于使用，减少了维护工作量。 
## ZUF-76-10-007 系统数据备份与恢复 
概述 : 
系统数据备份与恢复实现数据备份与恢复的功能。 
客户收益 : 
该功能为操作员管理系统数据备份和恢复提供了一个方便的工具。 
说明 : 
系统数据备份与恢复包括： 
备份配置数据 
恢复配置数据 
## ZUF-76-10-008 Telnet功能 
概述 : 
OAM支持Telnet功能。用户可以通过Telnet客户端访问OAM服务器。 
客户收益 : 
Telnet客户端使管理NF更加方便。 
说明 : 
OAM服务器采用Telnet方式。操作员可以通过Telnet客户端访问OAM服务器。 
# ZUF-76-11 业务跟踪 
## ZUF-76-11-001 信令跟踪 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
信令跟踪功能（即3GPP协议中的Trace功能）可以有效应用于工程系统维护、故障定位、设备信令流程查询等多种场景，是一种应用广泛的系统维护和排障手段。 
本功能提供针对中兴通讯核心网设备的各类信令跟踪流程，包括跟踪指定的接口、跟踪指定的用户、跟踪指定的NF、跟踪随机用户等。通过对跟踪到的各类信令的解码及展示功能，操作维护人员可以直观地分析和判断相关信令的正确性，有助于协助排查相关问题。跟踪码流及其解码结果，可以导出为数据文件，供事后分析。
EM信令跟踪支持核心网2G、3G、4G和5G各类NF。
背景知识 : 
跟踪类型各个NF支持的不同跟踪功能，例如用户跟踪、接口跟踪、链路跟踪。 
跟踪任务跟踪任务是对跟踪类型的一次执行过程，从创建任务，开始跟踪，到停止跟踪，跟踪任务的状态参见表1。表1  跟踪任务状态状态状态名说明scheduled已计划定时任务，但任务开始时间还未到。active激活中执行激活命令后，或任务时间已开始。activated已激活NF反馈成功。对于含有多个NF的任务，只要有NF反馈成功即已激活。stopped已停止用户停止任务，或者任务的执行时间结束。 
监控实时查看NF上报的信令数据，并进行分析。 
历史数据信令保存的历史数据文件，可回溯分析。 
应用场景 : 
类型|场景
---|---
单NF用户跟踪|定位故障或验证新业务，分析本NF特定用户相关的接口、链路业务信令。
接口/链路/协议跟踪|定位故障或验证新业务，分析指定接口、链路业务信令。
端到端用户跟踪|用户投诉处理或NF间业务信令分析，跟踪特定用户端到端的核心网侧全流程信令。
客户收益 : 
受益方|受益描述
---|---
运营商|当业务出现故障或异常时，通过定制特定的信令跟踪任务采集相关数据进行分析，快速定位并排除故障。
终端用户|当用户业务出现故障投诉，操作维护人员通过用户跟踪采集相关数据分析，快速定位并排除故障。
实现原理 : 
系统架构 : 
图1  系统架构
操作维护人员通过Web界面创建信令跟踪任务。 
EM将已创建的跟踪任务按照约定的命令下发到NF。任务下发成功后，NF上将创建对应的跟踪任务。
如果一个跟踪任务中包含多个被跟踪的NF，EM将对任务中包含的所有NF下发命令。 
NF根据EM指定的跟踪参数跟踪目标（如：接口、用户、链路）。 
NF上报采集跟踪数据到EM。 
EM处理解析或保存跟踪数据，操作维护人员通过Web客户端监控实时查看信令或者查看历史信令数据。 
涉及的网元 : 
系统名称|说明
---|---
NF|各个NF，例如AMF、SMF、UPF。
EM|管理系统，提供信令跟踪功能。
Web|浏览器，提供跟踪下发操作界面和信令呈现。
本网元实现 : 
EM跟踪功能由跟踪界面、任务管理、数据采集、数据监控与处理、解码组成，与数据库和文件系统交互，如[图2]所示。
EM下发跟踪任务到NF，NF上报信令数据到EM。
图2  系统组成
业务流程 : 
创建定时任务
图3  创建定时任务流程
[创建任务]
流程说明： 
用户通过菜单导航选择NF类型进入跟踪任务管理界面，创建跟踪任务。
界面获取跟踪设置参数。 
返回跟踪设置参数并界面呈现。 
用户设置跟踪条件：跟踪类型、跟踪的NF以及对应的NFS实例，定时任务时间设置，根据需要设置跟踪业务条件。
用户提交跟踪条件。 
界面发起跟踪任务创建。 
跟踪任务管理保存任务。 
返回任务列表。 
界面展现任务列表。 
创建即时和持续任务
任务创建后自动启动，包括即时和持续任务。 
图4  创建即时和持续任务流程
[创建激活任务]
流程说明： 
用户通过菜单导航选择NF类型进入跟踪任务管理界面，创建跟踪任务。
界面获取跟踪设置参数。 
返回跟踪设置参数并界面呈现。 
用户设置跟踪条件：跟踪类型、跟踪的NF以及对应的NFS实例，即时/持续任务设置，根据需要设置跟踪业务条件。
用户提交跟踪条件。 
界面发起跟踪任务创建。 
跟踪任务管理保存任务。 
下发激活任务到NF。 
NF返回激活任务结果。 
更新任务状态。 
返回任务列表。 
界面展现任务列表。 
启动任务
对于已计划的任务，当到达任务的开始时间时，自动启动任务。 
图5  启动任务流程
[启动任务]
流程说明： 
用户选择停止状态或者已计划状态的跟踪任务，单击启动任务按钮。 
界面发起跟踪任务启动。 
下发激活任务到NF。
NF返回激活任务结果。 
更新任务状态。 
返回任务启动结果。 
界面更新任务状态。 
停止任务
对于定时任务或者即时任务，当到达任务的结束时间时，系统自动停止任务。 
图6  停止任务流程
[停止任务]
流程说明： 
用户选择激活中或已激活状态的跟踪任务，单击停止任务按钮。 
界面发起跟踪任务停止。 
下发去激活任务到NF。
NF返回去激活任务结果。 
更新任务状态。 
返回停止结果。 
界面更新任务状态。 
同步任务
图7  同步任务流程
[同步任务]
流程说明： 
EM定时进行任务同步。
获取NF的任务列表。
NF返回任务列表。 
检查比较任务。 
EM和NF任务列表比较，EM任务存在，对应NF任务缺失，执行5~6操作： 
EM激活信令跟踪任务。 
NF返回执行结果。 
EM和NF任务列表比较，NF任务存在，对应EM任务缺失，执行7~8操作： 
EM去激活信令跟踪任务。 
NF返回执行结果。 
更新任务状态。 
返回任务执行结果。 
界面更新任务状态。 
查看任务
图8  查看任务流程
[查看任务]
流程说明： 
用户单击任务名称查看任务。 
获取任务条件参数。 
返回任务信息界面。 
界面呈现跟踪条件。 
修改任务
图9  修改任务流程
[修改任务]
流程说明： 
用户选择停止或已计划状态的跟踪任务，单击修改任务按钮。 
获取任务条件参数。 
返回任务信息界面。 
界面呈现跟踪条件。 
用户修改跟踪条件提交。 
界面发起跟踪任务修改。 
修改任务并保存。 
返回任务执行结果。 
界面更新任务列表。 
删除任务
图10  删除任务流程
[删除任务]
流程说明： 
用户选择停止或已计划状态的跟踪任务，单击删除任务。 
界面发起删除跟踪任务。 
删除保存的任务。 
返回任务结果。 
界面更新任务列表。 
查看NF任务状态
图11  查看NF任务状态流程
[查看网元任务状态]
流程说明： 
用户选择跟踪任务，单击查看NF任务状态。
界面发起获取NF任务状态。 
返回任务执行结果。 
界面展现NF任务状态。 
实时信令数据监控
用户选择跟踪任务，单击监控按钮。系统展现监控视图并实时更新信令数据结果。 
当不再需要监控时，用户关闭监控界面，系统停止展示信令数据结果。 
图12  实时信令数据监控流程
[监控任务]
流程说明： 
NF上报数据到EM数据采集。
EM数据采集保存数据到文件。 
用户选择跟踪任务，单击监控。 
界面发起跟踪任务监控。 
监控获取跟踪任务信息。 
跟踪任务管理返回结果。 
根据任务信息获取界面并返回。 
展现监控信令表格列头。 
数据采集获取监控任务信息。 
数据采集对监控的任务上报的数据解析入库。 
界面获取信令数据。 
监控从数据库获取信令数据。 
返回查询数据结果。 
处理数据满足展现要求。 
返回数据结果。 
界面展现信令数据。 
查看历史数据
用户选择跟踪任务，单击查看历史数据，进入查看界面，选择开始结束时间，系统展示跟踪数据。 
如果指定时间段内没有信令数据，界面提示无数据。 
图13  查看历史数据流程
[查看历史数据]
流程说明： 
用户选择跟踪任务，单击查看历史数据。 
用户选择开始结束时间。 
界面发起查看历史数据。 
获取跟踪任务信息。 
跟踪任务管理返回结果。 
根据任务信息获取界面并返回。 
展现信令表格列头。 
界面获取信令数据。 
从文件读取信令数据。 
数据解析入库。 
从数据库获取信令数据。 
返回查询数据。 
处理数据满足展现要求。 
返回数据。 
界面展现信令数据。 
详细解码
图14  详细解码流程
[详细解码]
流程说明： 
用户在监控或查看历史数据界面选择一条信令单击查看详细解码。 
界面发起查看详细解码信息。 
根据信令进行解码处理。 
返回处理结果。 
界面显示详细解码信息。 
保存数据
图15  保存数据流程
[保存数据]
流程说明： 
用户在监控或查看历史数据界面选择信令，选择按照pcap或txt保存。
界面发起保存信令数据。 
根据信令进行解码处理。 
返回处理结果。 
保存信令数据到文件。 
返回文件。 
导出数据
图16  导出数据流程
[导出数据]
流程说明： 
用户选择跟踪任务导出。 
界面展现导出设置。 
用户设置导出时间段。 
界面发起导出数据。 
保存信令数据到文件。 
获取跟踪任务信息。 
返回结果。 
返回打包sta格式文件。
离线数据查看
离线数据查看界面，用户选择一个信令sta文件导入，系统展现文件中的信令数据。
对于非法文件，系统检测提示文件格式不正确。 
图17  离线数据查看流程
[离线数据查看]
流程说明： 
用户选择离线数据查看。 
界面展现导入设置。 
用户选择sta文件导入。
界面发起导入数据。 
从文件读取信令数据。 
数据解析入库。 
从数据库获取信令数据。 
返回查询数据。 
处理数据满足展现要求。 
返回数据结果。 
界面展现信令数据。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
相关特性|交互关系
---|---
ZUF-76-10-005 日志管理|相关操作需要记录操作日志。
ZUF-76-10-004 安全管理|相关操作需要进行权限控制、鉴权。
ZUF-76-10-007 系统数据备份与恢复|信令跟踪任务数据库表备份恢复。
遵循标准 : 
标准类别|标准名称
---|---
3GPP|3GPP TS 32.421: "Telecommunication management; Subscriber andequipment trace: Trace concepts and requirements".3GPP TS 32.422: "Telecommunication management; Subscriber andequipment trace: Trace control and configuration management".3GPP TS 32.423: "Telecommunication management; Subscriber andequipment trace: Trace data definition and management".
特性能力 : 
名称|指标
---|---
NF信令跟踪任务数|100
端到端跟踪任务数|500
实时信令数据监控数|20
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.12|首次发布。
License要求 : 
端到端跟踪特性需要申请License许可后，运营商才能获得该特性的服务。 
该特性对应License文件中的项目编号为“cn.e2eTraceTaskNum”，此编号配置为“1-500”，表示申请的EM支持的端到端跟踪任务数。
对其他网元的要求 : 
UE|BSS/RAN|SGSN|PGW|HSS
---|---|---|---|---
-|√|√|√|√
UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
UE|NR|AMF|SMF|UPF
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 : 
命令 : 
本特性不涉及命令的变化。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
该特性的相关操作参见“信令跟踪
”
。
# 缩略语 
# 缩略语 
3GPP : 
3rd Generation Partnership Project第三代合作伙伴计划
AMF : 
Access and Mobility Management Function接入和移动管理功能
EM : 
Element Management网元管理
NF : 
Network Function网络功能
NFS : 
Network Function Service网络功能服务
PLMN : 
Public Land Mobile Network公共陆地移动网
SMF : 
Session Management Function会话管理功能
## TCE 
Trace Collection Entity跟踪采集实体
UPF : 
User Plane Function用户平面功能
# ZUF-76-12 业务维护增强功能 
## ZUF-76-12-001 DUMP 

概述 : 
DUMP用于从ZXUN uMAC导出用户信息。 
SGSN的用户信息包括IMSI、MSISDN、IMEI、RAI、CELLID、PTMSI、接入类型等。 
MME的用户信息包括IMSI、MSISDN、IMEI、TAI、CELLID、GUTI等。 
客户收益 : 
方便操作员从ZXUN uMAC获取用户信息。 
说明 : 
导出的用户信息以普通文件格式TXT和CSV保存。由于用户数过多，执行该程序需要一段时间。指定的模块用于导出用户信息。为了避免对其他操作的影响，可以暂停和恢复导出程序。导出的用户信息按2G/3G/4G用户状态分别统计。 
## ZUF-76-12-003 CHR 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
ZXUN EMSPlus是面向用户的数据业务运营分析产品，立足于从用户的角度感知和分析网络信息和业务信息，通过对海量数据灵活地挖掘和分析，实现对业务流量、用户流量、日志查询、终端应用和用户回溯等全方位的可视化管理，构建可视、可管、可控的业务管道，为移动数据业务精细化运营提供了全面支撑。
 
ZXUN uMAC作为整个数据业务运营分析系统的一个组成部分，负责上报CHR记录给ZXUN EMSPlus。ZXUN uMAC提供的CHR数据主要分为三类：
成功日志：业务流程成功时上报该日志，包括移动性管理事件日志、会话管理事件日志、切换事件日志等。 
失败日志：业务流程失败时上报该日志，包括移动性管理事件日志、会话管理事件日志、切换事件日志等。 
特殊日志：包括DNN更正、鉴权成功、鉴权失败、EBI分配等事件日志。 
背景知识 : 
在传统的网管系统中，监视网络运行状况主要是依靠告警监控和性能报表分析，但这两个功能都是从网元设备的角度反映网络运行状况，而无法反映每一个呼叫的具体细节，即无法反映用户粒度的网络质量情况。此外现有的性能统计是基于一定采集周期来分析的，也不能做到对网络质量的实时监控。 
随着移动网络业务和技术的复杂性不断增加，以及市场竞争的加剧，要求网络维护工作从原来面向网络设备向面向业务、注重客户感知的方向转变。为了更好地满足故障处理、客户投诉处理和网络性能实时分析等网络管理需求，需要实时采集CHR信令消息，实现CHR分析功能。 
随着网络带宽的提升，4G技术早已普及，5G技术稳步推进，移动互联网正逐渐渗透到人们生活、工作的各个领域，短信、铃图下载、移动音乐、手机游戏、视频应用、手机支付、位置服务等丰富多彩的移动互联网应用得到迅猛发展，同时运营商对移动业务的经营分析、用户互联网行为分析需求越来越迫切，为了实现这些需求，需要基于用户呼叫历史记录，实现数据采集分析功能。 
应用场景 : 
ZXUN uMAC上报的CHR记录，可以用于用户投诉处理、故障定位、网络质量优化、用户行为分析和业务发展分析。
用户投诉处理：呼叫记录分析系统上报的业务报告中包含了详细的信息，是用户投诉处理、呼叫跟踪和例行呼叫测试中不可缺少的信息。 
故障定位：呼叫记录分析系统上报的业务报告中包含了详细的背景参数（比如：设备供应商的内部字段），在分析设备质量问题和故障定位方面更加有效。 
网络质量优化：详细可定制的网络分析功能和运营分析报表多维度地展现网络运行质量，为运维决策提供有力支撑。 
用户行为分析：通过对用户呼叫记录数据的分析过滤，可以实现对用户行为和终端使用情况的细致分析，向市场服务部门提供用户信息列表，实现用户的差异化服务，有针对性地发展用户，引导用户正确使用业务。 
业务发展分析：分析各类业务的开展状况、运行质量，辅助业务扩展和市场决策。 
客户收益 : 
受益方|受益描述
---|---
运营商|对网络进行监控，运营商可以根据监控数据进行网络优化，缩短用户投诉的处理时间，提高用户满意度，提高网络运维的效率。
移动用户|享受运营商挖掘的新业务，提升网络服务体验。
#### 实现原理 
系统架构 : 
图1  系统架构图
涉及的网元 : 
网元名称|网元作用
---|---
ZXUN uMAC|上报业务流程的CHR记录给ZXUN EMSPlus服务器。
ZXUN EMSPlus|负责存储CHR记录，支持基于CHR的用户行为分析、故障分析等功能。
协议栈 : 
ZXUN uMAC与ZXUN EMSPlus之间为非标准接口，采用UDP协议。 
本网元实现 : 
ZXUN uMAC支持在业务流程成功或者失败时，上报该业务流程的CHR记录给EMSPlus服务器。通过本地配置，ZXUN uMAC实现如下CHR上报控制： 
控制是否上报成功日志、失败日志或者特殊日志，特殊日志包括鉴权成功日志、鉴权失败日志等。 
控制是否上报移动性日志、会话日志、寻呼日志、切换日志等。 
控制日志上报速率。 
业务流程 : 
ZXUN uMAC支持在业务流程成功或者失败时，上报该业务流程的CHR记录给ZXUN EMSPlus服务器，供ZXUN EMSPlus服务器进行用户故障分析、行为分析等。 
ZXUN uMAC执行用户业务流程。 
用户业务流程结束后，ZXUN uMAC根据如下逻辑，上报CHR日志给ZXUN EMSPlus服务器： 
若本次上报为成功日志，且"支持全量日志上报" License项打开，本地配置支持对应类型的日志上报，则上报日志。 
若本次上报为失败日志，且本地支持对应类型的日志上报，则上报日志。 
若本次上报为特殊日志，且"支持全量日志上报" License项打开，本地配置支持对应的特殊日志上报，则上报日志。 
系统影响 : 
开启本特性后，对于系统的CPU性能以及带宽会有影响，影响程度取决于系统话务模型、系统接入的用户数量。工程实施时，若开启本特性，则需要考虑适当增加资源，以抵销本特性对于性能的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
ZXUN uMAC在业务流程结束后，上报CHR记录给ZXUN EMSPlus服务器。 
遵循标准 : 
类别|标准编号|标准名称
---|---|---
3GPP|TS 23.003|Numbering, addressing and identification
TS 23.501|3GPP|Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2
TS 23.502|3GPP|3GPP TS 23.502 Technical Specification Group Services and System Aspects; Procedures for the 5G System; Stage 2
TS 24.501|3GPP|Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3
TS 29.503|3GPP|Unified Data Management Services; Stage 3
TS 29.531|3GPP|Network Slice Selection Services; Stage 3
TS 38.413|3GPP|NG Application Protocol (NGAP)
特性能力 : 
ZXUN uMAC AMF网元支持本地配置CHR上报速率限制，MME/SGSN网元支持本地配置CHR上报速率限制。实际商用配置要依据实际话务模型和其他特定需求，协商确定，特性能力参见下表。 
名称|指标
---|---
AMF网元单SC最大支持每秒上报的CHR个数|65535（默认值2000）
MME网元单SC最大支持每秒上报的CHR个数|1000（默认值2000，老版本升级上来默认值是1000）
SGSN网元单SC最大支持每秒上报的CHR个数|1000（默认值2000，老版本升级上来默认值是1000）
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
02|V7.21.20|新增支持上报全量EMSPlus日志功能，包括成功日志、特殊日志以及失败日志。
01|V7.20.20|首次发布。
License要求 : 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“支持全量日志上报”（license ID：7014），此项目显示为“支持”，表示ZXUN uMAC支持全量日志上报。若激活该License，则AMF/MME/SGSN支持上报全量EMSPlus日志，包括成功日志、特殊日志以及失败日志；否则，仅支持上报失败日志。
对其他网元的要求 : 
UE|gNB|AMF|MME|SGSN|EMS+
---|---|---|---|---|---
-|-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 : 
命令 : 
配置项表1  新增AMF配置项AMF网元配置项命令EMS+配置SET EMSPLUSCFGSHOW EMSPLUSCFGEMS+功能开关配置SET AMFCHRFUNCSHOW AMFCHRFUNCEMS+限速配置SET AMFCHRLIMTCFGSHOW AMFCHRLIMTCFG表2  新增MME/SGSN配置项MME/SGSN网元配置项命令EMS+配置SET EMSPLUSSHOW EMSPLUSEMS+功能开关配置SET EMSPLUSLOGSHOW EMSPLUSLOGEMS+限速配置SET EMSPLUS RATELIMITSHOW EMSPLUS RATELIMIT 
安全变量无。 
软件参数无。 
动态管理无。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
该配置过程实现ZXUN uMAC支持在业务流程成功或者失败时，上报该业务流程的CHR记录给EMSPlus服务器。 
对接EMSPlus时： 
V7.21.20之前版本，MME/SGSN本端端口范围为15000-15999。 
V7.21.20以及之后版本，MME/SGSN本端端口范围为16000-16999。 
配置前提 : 
如果需要上报成功日志或特殊日志，则需要激活license“支持全量日志上报”。 
如果只需上报失败日志，则无需激活license“支持全量日志上报”。 
配置过程 : 
###### AMF网元的配置 
AMF网元的配置步骤如下： 
执行[SET EMSPLUSCFG]命令，配置本端AMF和对端EMSPlus的地址、端口等信息。
执行[SET AMFCHRFUNC]命令，配置EMSPlus功能开关，决定AMF需要上报哪些事件给EMSPlus。
（可选）执行[SET AMFCHRLIMTCFG]命令，当上报事件数量过多而导致EMSPlus或AMF的性能无法支持时，配置上报限速。
###### MME/SGSN网元的配置 
MME/SGSN网元的配置步骤如下： 
执行[SET EMSPLUS]命令，配置本端MME/SGSN和对端EMSPlus的地址、端口等信息。
执行[SET EMSPLUSLOG]命令，配置EMSPlus功能开关，决定MME/SGSN需要上报哪些事件给EMSPlus。
（可选）执行[SET EMSPLUS RATELIMIT]命令，当上报事件数量过多而导致EMSPlus或MME/SGSN的性能无法支持时，配置上报限速。
配置实例 : 
###### 场景一：应用于用户投诉、故障定位 
场景说明
AMF/MME/SGSN需要上报事件日志给EMSPlus，主要上报流程失败的相关事件。通过分析上报的日志内容，帮助进行故障定位、快速处理用户投诉。 
数据规划
AMF数据规划参见下表。 
AMF配置项|参数名称|取值
---|---|---
修改EMS+配置|开启EMS+日志上报功能|开启
链路IP地址类型|修改EMS+配置|IPV4
主用远端服务器IPv4地址|修改EMS+配置|172.151.1.26
主用远端服务器UDP端口号|修改EMS+配置|15000
本端IPv4地址|修改EMS+配置|172.151.1.17
本端UDP起始端口号|修改EMS+配置|15000
VRF标识|修改EMS+配置|2
修改EMS+上报功能配置|功能开关|失败日志、特殊日志
上报日志功能开关|修改EMS+上报功能配置|上报MM日志、上报SM日志、上报寻呼日志、上报切换日志、上报释放日志、上报短消息日志
上报特殊日志功能开关|修改EMS+上报功能配置|上报鉴权失败日志、上报解码失败日志、上报EBI分配失败日志、上报PDU会话获取失败日志、上报PDU会话切换失败日志
修改EMS+限速配置|总上报速率|2000
失败CHR上报速率|修改EMS+限速配置|200
特殊CHR上报速率|修改EMS+限速配置|200
MME/SGSN数据规划参见下表。 
MME/SGSN配置项|参数名称|取值
---|---|---
设置EMS PLUS配置|是否开启EMS PLUS功能|开启
EMS PLUS服务端IP|设置EMS PLUS配置|172.151.1.26
EMS PLUS服务端端口号|设置EMS PLUS配置|15000
MME/SGSN本端IP|设置EMS PLUS配置|172.151.1.18
VRF ID|设置EMS PLUS配置|2
链路检测时间间隔(秒)|设置EMS PLUS配置|5
链路检测次数|设置EMS PLUS配置|5
设置EMS PLUS日志配置|功能开关|失败日志、特殊日志
网元类型开关|设置EMS PLUS日志配置|SGSN、MME
日志开关|设置EMS PLUS日志配置|上报MM日志、上报SM日志、上报寻呼日志、上报切换日志、上报短信日志、上报释放日志、上报漫游用户日志
特殊日志开关|设置EMS PLUS日志配置|上报APN更正日志、上报IMEI灰名单日志、上报IMEI Unknown名单日志、上报RIM成功日志、上报RIM失败日志、上报DNS查询成功日志、上报DNS查询失败日志、上报鉴权成功日志、上报鉴权失败日志
修改EMS+限速配置|总上报速率|2000
失败CHR上报速率|修改EMS+限速配置|200
特殊CHR上报速率|修改EMS+限速配置|200
配置步骤
AMF的配置步骤参见下表。 
AMF步骤|说明|操作
---|---|---
1|配置本端AMF和对端EMSPlus的地址、端口等信息。|SET EMSPLUSCFG:ENABLE="ON",IPADDRESSTYPE="IPV4",REMOTEIPV4="172.151.1.26",REMOTEUDPPORT=15000,LOCALIPV4="172.151.1.17",LOCALUDPPORT=15000,VRFID=2
2|配置EMSPlus功能开关。|SET AMFCHRFUNC:FLG="FAILURE"&"SPECIAL",LOGFUNCFLG="MM"&"SM"&"PAGING"&"HANDOVER"&"RELEASE"&"SMS",SPECIALFUNCFLG="AUTHENTICATION_FAIL"&"DECODING_FAILURE"&"EPS_BEARERID_ALLOCATION_FAIL"&"PDU_SESSION_RETRIVE_FAIL"&"PDU_SESSION_HANDOVER_FAIL"
3|配置上报限速。|SET AMFCHRLIMTCFG:TOTALRATE=2000,FAILRATE=200,SPECRATE=200
MME/SGSN的配置步骤参见下表。 
MME/SGSN步骤|说明|操作
---|---|---
1|配置本端MME/SGSN和对端EMSPlus的地址、端口等信息。|SET EMSPLUS:SWITCH="ON",SVRIP="172.151.1.26",SVRPORT=15000,LOCALIP="172.151.1.17",VRFID=2,CHECKINTERVAL=5,CHECKNUM=5
2|配置EMSPlus功能开关。|SET EMSPLUSLOG:FUNCFLG="FAILURE"&"SPECIAL",NETYPEFLG="SGSN"&"MME",LOGFUNCFLG="REPMMLOG"&"REPSMLOG"&"REPHOLOG"&"REPPAGINGLOG"&"REPSMSLOG"&"REPRELESELOG"&"REPROAMUSERLOG",SPECFAILLOGFLG="REPAPNMODLOG"&"REPIMEIGRAYLISTLOG"&"REPIMEIUKLISTLOG"&"REPRIMSUCCLOG"&"REPRIMFAILLOG"&"REPDNSQRYSUCCLOG"&"REPDNSQRYFAILLOG"&"REPAUTHSUCCLOG"&"REPAUTHFAILLOG"
3|配置上报速率。|SET EMSPLUS RATELIMIT:TOTALRATE=2000,FAILRATE=200,SPECRATE=200
###### 场景二：应用于网络质量优化，用户行为分析，业务发展分析 
场景说明
AMF/MME/SGSN需要上报事件日志给EMSPlus，上报流程主事件，通过全量的日志分析，多维度地展现网络运行质量、有针对性地发展用户、辅助业务扩展和市场决策。 
数据规划
AMF数据规划参见下表。 
AMF配置项|参数名称|取值
---|---|---
修改EMS+配置|开启EMS+日志上报功能|开启
链路IP地址类型|修改EMS+配置|IPV4
主用远端服务器IPv4地址|修改EMS+配置|172.151.1.26
主用远端服务器UDP端口号|修改EMS+配置|15000
本端IPv4地址|修改EMS+配置|172.151.1.17
本端UDP起始端口号|修改EMS+配置|15000
VRF标识|修改EMS+配置|2
修改EMS+上报功能配置|功能开关|成功日志、失败日志、特殊日志
上报日志功能开关|修改EMS+上报功能配置|上报MM日志、上报SM日志、上报寻呼日志、上报切换日志、上报释放日志、上报短消息日志
上报特殊日志功能开关|修改EMS+上报功能配置|NULL
修改EMS+限速配置|总上报速率|2000
失败CHR上报速率|修改EMS+限速配置|200
特殊CHR上报速率|修改EMS+限速配置|200
MME/SGSN数据规划参见下表。 
MME/SGSN配置项|参数名称|取值
---|---|---
设置EMS PLUS配置|是否开启EMS PLUS功能|开启
EMS PLUS服务端IP|设置EMS PLUS配置|172.151.1.26
EMS PLUS服务端端口号|设置EMS PLUS配置|15000
MME/SGSN本端IP|设置EMS PLUS配置|172.151.1.17
VRF ID|设置EMS PLUS配置|2
链路检测时间间隔(秒)|设置EMS PLUS配置|5
链路检测次数|设置EMS PLUS配置|5
设置EMS PLUS日志配置|功能开关|成功日志、失败日志、特殊日志
网元类型开关|设置EMS PLUS日志配置|SGSN、MME
日志开关|设置EMS PLUS日志配置|上报MM日志、上报SM日志、上报寻呼日志、上报切换日志、上报短信日志、上报释放日志、上报漫游用户日志
特殊日志开关|设置EMS PLUS日志配置|上报APN更正日志、上报IMEI灰名单日志、上报IMEI Unknown名单日志、上报RIM成功日志、上报RIM失败日志、上报DNS查询成功日志、上报DNS查询失败日志、上报鉴权成功日志、上报鉴权失败日志
修改EMS+限速配置|总上报速率|2000
失败CHR上报速率|修改EMS+限速配置|200
特殊CHR上报速率|修改EMS+限速配置|200
配置步骤
AMF的配置步骤参见下表。 
AMF步骤|说明|操作
---|---|---
1|配置本端AMF和对端EMSPlus的地址、端口等信息。|SET EMSPLUSCFG:ENABLE="ON",IPADDRESSTYPE="IPV4",REMOTEIPV4="172.151.1.26",REMOTEUDPPORT=15000,LOCALIPV4="172.151.1.17",LOCALUDPPORT=15000,VRFID=2
2|配置EMSPlus功能开关。|SET AMFCHRFUNC:FLG="SUCCESS"&"FAILURE"&"SPECIAL",LOGFUNCFLG="MM"&"SM"&"PAGING"&"HANDOVER"&"RELEASE"&"SMS",SPECIALFUNCFLG="NULL"
3|配置上报限速。|SET AMFCHRLIMTCFG:TOTALRATE=2000,FAILRATE=200,SPECRATE=200
MME/SGSN的配置步骤参见下表。 
MME/SGSN步骤|说明|操作
---|---|---
1|配置本端MME/SGSN和对端EMSPlus的地址、端口等信息。|SET EMSPLUS:SWITCH="ON",SVRIP="172.151.1.26",SVRPORT=15000,LOCALIP="172.151.1.17",VRFID=2,CHECKINTERVAL=5,CHECKNUM=5
2|配置EMSPlus功能开关。|SET EMSPLUSLOG:FUNCFLG="SUCCESS"&"FAILURE"&"SPECIAL",NETYPEFLG="SGSN"&"MME",LOGFUNCFLG="REPMMLOG"&"REPSMLOG"&"REPHOLOG"&"REPPAGINGLOG"&"REPSMSLOG"&"REPRELESELOG"&"REPROAMUSERLOG",SPECFAILLOGFLG="REPAPNMODLOG"&"REPIMEIGRAYLISTLOG"&"REPIMEIUKLISTLOG"&"REPRIMSUCCLOG"&"REPRIMFAILLOG"&"REPDNSQRYSUCCLOG"&"REPDNSQRYFAILLOG"&"REPAUTHSUCCLOG"&"REPAUTHFAILLOG"
3|配置上报速率。|SET EMSPLUS RATELIMIT:TOTALRATE=2000,FAILRATE=200,SPECRATE=200
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|ZXUN uMAC上报失败日志
---|---
测试目的|ZXUN uMAC上报失败日志。
预置条件|系统运行正常。网元与EMSPlus系统连接正常。开启EMSPlus功能。
测试过程|开启上报失败日志功能开关。开启上报SM日志功能开关。PDU会话建立流程中选择本地SMF失败。
通过准则|ZXUN uMAC上报失败日志，检查上报事件正确，携带正确的公共字段、扩展字段、失败原因及失败内部原因。
测试结果|–
测试项目|ZXUN uMAC上报成功日志
---|---
测试目的|ZXUN uMAC上报成功日志。
预置条件|系统运行正常。网元与EMSPlus系统连接正常。开启EMSPlus功能。
测试过程|开启上报全量（成功+失败+特殊）日志功能开关。开启上报MM日志功能开关。用户紧急注册到ZXUN uMAC成功。
通过准则|ZXUN uMAC上报成功日志，检查上报事件正确，携带正确的公共字段和、扩展字段和新增字段。
测试结果|–
测试项目|ZXUN uMAC上报特殊日志
---|---
测试目的|ZXUN uMAC上报特殊日志。
预置条件|系统运行正常。网元与EMSPlus系统连接正常。开启EMSPlus功能。
测试过程|开启上报特殊日志开关功能开关。开启上报鉴权成功日志功能开关。用户注册或者去注册流程中有鉴权流程，且鉴权成功。
通过准则|ZXUN uMAC上报鉴权成功事件，检查上报事件正确，携带正确的公共字段和扩展字段。
测试结果|–
测试项目|ZXUN uMAC进行日志过滤
---|---
测试目的|ZXUN uMAC进行日志过滤。
预置条件|系统运行正常。网元与EMSPlus系统连接正常。开启EMSPlus功能。
测试过程|关闭上报失败日志功能开关。用户初始注册到ZXUN uMAC失败。
通过准则|检查ZXUN uMAC不上报初始注册事件。
测试结果|–
常见问题处理 : 
无。 
## ZUF-76-12-004 AMF周边网元拨测 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
AMF周边网元拨测功能是指维护人员使用测试号码到特定的周边网元(AUSF、SMF、PCF、UDM、NSSF、AMF、MME)，对周边网元进行指定业务的测试，来检查周边网元链路以及业务是否正常。
背景知识 : 
在系统实际运行过程中，运维人员需要测试新入网的周边网元的网络状况和数据配置的正确性，使用测试卡到指定的周边网元进行拨测。在业务测试正常情况后，进行入网割接，保障新入网网元投入运行后业务运行正常。同时运维人员怀疑某个网元可能有问题或者故障，通过将测试卡指向该网元进行拨测，进行问题和故障排查。 
应用场景 : 
在5G网络下，运维人员可以通过拨测模式和商用割接模式对周边网元进行拨测。 
拨测模式使用场景：运维人员需要测试新入网的SMF\PCF\UDM\MME\AMF\NSSF\AUSF网元，根据测试用户的GPSI和SUPI号码的配置，将对应的用户指定到对应的网元上，对特定网元进行业务测试，检查网元是否满足要求。运维人员怀疑某个SMF\PCF\UDM\MME\AMF\NSSF\AUSF网元可能有问题或者故障，根据测试用户的GPSI和SUPI号码的配置，将对应的用户指定到对应的网元上，对特定网元进行业务测试，排查指定的网元的问题和故障。 
商用割接模式使用场景：在割接SMF时，需要对用户按批次进行割接，使用户注册或激活到指定的网元上。AMF发现SMF网元时，通过指定的网元号段的配置，来满足割接模式的要求。在系统运行中，根据SMF网元维护的需要，AMF向NRF发现SMF网元后，运维人员根据测试用户的GPSI和SUPI号码的配置，通过与本地配置的号段进行匹配的方式，将对应的用户指定到对应SMF上，进行业务测试，排查指定SMF的问题和故障。 
 说明： 
拨测发生在运营商机房或者路测。 
客户收益 : 
受益方|受益描述
---|---
运营商|可以方便运营商在网元投入使用前，通过拨测方式进行业务拨测，保障网元投入运营后运行正常。当指定网元出现故障和问题时，通过拨测方式可以将用户指定到对应网元， 进行业务拨测，排查网元的故障和问题。
移动用户|指定网元拨测可以保障周边网元运行正常，从而减少网络问题造成终端业务受影响，提高移动用户的体验。
实现原理 : 
系统架构 : 
该特性涉及到的网络结构如[图1]所示。
图1  系统架构
涉及的网元 : 
网元名称|网元作用
---|---
SMF|AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的SMF上，对特定SMF网元进行业务测试。支持拨测和割接两种场景。拨测SMF分为A-SMF、I-SMF、V-SMF，通过区分SMF的角色进行指定SMF的拨测。
AUSF|AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的AUSF上，对特定网元进行业务测试，检查网元是否满足要求。
UDM|AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的UDM上，对特定网元进行业务测试，检查网元是否满足要求。
AMF|切换场景下，源AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的目标AMF上，对特定AMF网元进行切换业务测试，检查网元是否满足要求。
MME|4/5G互操作时，AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的MME上，对特定MME网元进行4/5G互操作测试，检查网元是否满足要求。
NSSF|AMF与NSSF交互获取切片管理策略以控制用户接入合适的网络切片。AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的NSSF上，对特定NSSF网元进行业务测试，检查网元是否满足要求。
PCF|AMF根据测试用户的GPSI和SUPI号码配置，将对应的用户指定到对应的PCF上，对特定PCF网元进行AM和UE策略控制相关的业务测试，检查网元是否满足要求。
###### 本NF实现 
AMF根据GPSI/SUPI号码或号段选择拨测网元，实现的功能如下： 
AMF根据GPSI/SUPI号码或号段选择拨测的AUSF。 
AMF根据GPSI/SUPI号码或号段选择拨测的UDM。 
AMF根据GPSI/SUPI号码或号段选择拨测的PCF。 
AMF根据GPSI/SUPI号码或号段选择拨测的NSSF。 
原AMF根据GPSI/SUPI号码或号段选择拨测的目标AMF。 
AMF根据GPSI/SUPI号码或号段选择拨测的MME。 
AMF根据GPSI/SUPI号码或号段选择拨测的SMF。 
业务流程 : 
拨测AUSF流程
注册更新流程时，选择拨测AUSF网元进行鉴权过程，如[图2]所示。
图2  拨测AUSF流程图
流程说明： 
在新AUSF上线前或者维护人员定位故障时，维护人员配置测试号码指定到AUSF-2，对指定的AUSF-2进行拨测。 
终端发起初始注册更新，AMF判断需要进行鉴权过程。 
AMF在发现AUSF服务之前，根据用户SUPI或者GPSI读取配置获取拨测AUSF网元。当前用户是拨测用户，AMF根据配置获取拨测AUSF-2网元信息，向AUSF-2发起鉴权过程。 
AMF指定拨测AUSF_2时，AMF发起和AUSF_2的鉴权向量获取、鉴权确认流程交互。 
AMF继续完成注册更新流程。 
拨测UDM流程
注册更新流程时，选择拨测UDM网元进行注册更新过程，如[图3]所示。
图3  拨测UDM流程图
流程说明： 
在新的UDM上线前或者维护人员定位故障时，维护人员配置测试号码指定到UDM-2，对指定的UDM-2进行拨测。 
终端发起初始注册更新，AMF判断需要向UDM发起注册更新过程。 
AMF在发现UDM服务之前，根据用户SUPI或者GPSI读取配置获取拨测UDM网元信息。当前用户是拨测用户，AMF根据配置获取拨测UDM-2网元信息，向UDM-2发起注册更新过程。 
AMF指定拨测UDM-2时，AMF和UDM-2进行注册更新、签约信息获取、订阅、切片获取流程交互。 
AMF继续完成注册更新流程。 
拨测PCF流程
注册更新或切换流程时，选择拨测PCF网元进行策略控制，如[图4]所示。
图4  拨测PCF流程图
流程说明： 
在新的PCF上线前或者维护人员定位故障时，维护人员配置测试号码指定到拨测网元PCF-2，对指定的PCF-2进行拨测。 
终端发起初始注册更新，AMF判断需要发起策略关联建立和PCF发起事件订阅。 
AMF在发现PCF服务之前，根据用户SUPI或者GPSI读取配置获取拨测PCF网元信息。当前用户是拨测用户，AMF根据配置获取拨测PCF-2网元信息，向PCF-2发起策略关联建立过程。 
AMF指定拨测PCF-2时，AMF和PCF-2进行策略关联建立和PCF发起事件订阅流程交互。 
AMF继续完成注册更新流程。 
拨测NSSF流程
注册更新、PDU建立时，选择拨测NSSF网元进行切片选择，如[图5]所示。
图5  拨测NSSF流程图
流程说明： 
在新的NSSF上线前或者维护人员定位故障时，维护人员配置测试号码指定到拨测网元NSSF-2，对指定的NSSF-2进行拨测。 
终端发起初始注册更新，AMF判断需要向NSSF发起切片选择过程。 
AMF在发现NSSF服务之前，根据用户SUPI或者GPSI读取配置获取拨测NSSF网元信息。当前用户是拨测用户，AMF根据配置获取拨测NSSF-2网元信息，向NSSF-2发起切片选择过程。 
AMF指定拨测NSSF-2时，AMF和NSSF-2进行策略关联建立和NSSF发起切片选择过程。 
AMF继续完成注册更新流程。 
拨测AMF流程
切换流程时，选择拨测AMF网元进行切换过程，如[图6]所示。
图6  拨测AMF流程图
流程说明： 
在新的AMF上线前或者维护人员定位故障时，维护人员配置测试号码指定到拨测网元AMF-2，对指定的AMF-2进行拨测。 
终端移动触发跨AMF切换，AMF判断需要向target AMF发起切换。 
AMF在发现targetAMF服务之前，根据用户SUPI或者GPSI读取配置获取拨测AMF网元信息。当前用户是拨测用户，AMF根据配置获取拨测AMF-2网元信息，向AMF-2发起切换过程。 
AMF指定拨测AMF-2时，AMF向AMF-2发起切换流程。 
AMF继续完成后续的切换流程。 
拨测MME流程
4G、5G切换流程时，选择拨测MME网元进行4G、5G互操作，如[图7]所示。
图7  拨测MME流程图
流程说明： 
在4/5G网络切换场景下，新MME使用前或者维护人员定位故障时，维护人员配置测试号码指定到拨测网元MME-2，对指定的MME-2进行拨测。 
终端移动，发生5G到4G网络的切换，AMF判断需要向target MME发起切换。 
AMF根据Target eNB ID合适的target MME之前，根据用户SUPI或者GPSI读取配置获取拨测MME网元信息。当前用户是拨测用户，AMF根据配置获取拨测MME-2的网元信息，向MME-2发起切换过程。 
AMF指定拨测MME-2时，AMF向MME-2发起5G到4G的切换流程。 
AMF继续完成后续的切换流程。 
拨测SMF流程
注册更新//PDU会话建立/切换/业务请求时，选择拨测SMF网元进行业务过程，如[图8]所示。
图8  拨测SMF流程图
流程说明： 
新SMF使用前或者维护人员定位故障时，维护人员配置测试号码指定到拨测网元I-SMF-2或A-SMF-2，对指定的I-SMF-2或A-SMF-2进行拨测。 
当终端发起注册、PDU会话建立、切换、业务请求时，触发PDU会话建立或更新。 
AMF在ISMF或ASMF的选择时，根据用户SUPI或者GPSI读取配置获取拨测SMF的选择策略。 
当前用户是拨测用户，AMF根据配置获取拨测I-SMF-2或A-SMF-2的地址等信息，向I-SMF-2或A-SMF-2发起PDU会话操作过程。 
当前用户是割接模式拨测用户，AMF首先向NRF发起SMF的服务发现，然后从发现结果中获取配置的SMF作为拨测网元。 
AMF指定拨测I-SMF-2或A-SMF-2时，AMF向I-SMF-2或A-SMF-2发起PDU会话建立或修改流程。 
AMF继续完成后续对应的注册/PDU建立/切换/业务请求等业务流程。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
该特性不涉及标准协议。 
特性能力 : 
名称|指标
---|---
基于号段选择AUSF配置|500（个）
基于号段选择UDM配置|500（个）
基于号段选择SMF配置|500（个）
基于号段选择PCF配置|500（个）
基于号段选择AMF配置|500（个）
基于号段选择MME配置|500（个）
基于号段选择NSSF配置|500（个）
基于号段选择AUSF策略|1（个）
基于号段选择UDM策略|1（个）
基于号段选择SMF策略|1（个）
基于号段选择PCF策略|1（个）
基于号段选择AMF策略|1（个）
基于号段选择MME策略|1（个）
基于号段选择NSSF策略|1（个）
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.21.30|首次发布。
License要求 : 
该特性为基本特性，无需License支持。 
###### 对其他NF的要求 
AMF|SMF|PCF|UDM|AUSF
---|---|---|---|---
-|-|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
本特性新增配置项参见[表1]。
配置项|命令
---|---
修改基于号段选择PCF策略|SET RESOLPCFSEGPOLICY
查询基于号段选择PCF策略|SHOW RESOLPCFSEGPOLICY
新增基于号段选择PCF配置|ADD RESOLPCFSEGCFG
修改基于号段选择PCF配置|SET RESOLPCFSEGCFG
删除基于号段选择PCF配置|DEL RESOLPCFSEGCFG
查询基于号段选择PCF配置|SHOW RESOLPCFSEGCFG
修改基于号段选择UDM策略|SET RESOLUDMSEGPOLICY
查询基于号段选择UDM策略|SHOW RESOLUDMSEGPOLICY
新增基于号段选择UDM配置|ADD RESOLUDMSEGCFG
修改基于号段选择UDM配置|SET RESOLUDMSEGCFG
删除基于号段选择UDM配置|DEL RESOLUDMSEGCFG
查询基于号段选择UDM配置|SHOW RESOLUDMSEGCFG
修改基于号段选择AUSF策略|SET RESOLAUSFSEGPOLICY
查询基于号段选择AUSF策略|SHOW RESOLAUSFSEGPOLICY
新增基于号段选择AUSF配置|ADD RESOLAUSFSEGCFG
修改基于号段选择AUSF配置|SET RESOLAUSFSEGCFG
删除基于号段选择AUSF配置|DEL RESOLAUSFSEGCFG
查询基于号段选择AUSF配置|SHOW RESOLAUSFSEGCFG
修改基于号段选择AMF策略配置|SET RESOLAMFPOLICY
查询基于号段选择AMF策略配置|SHOW RESOLAMFPOLICY
新增基于号段选择AMF配置|ADD RESOLAMFNUMCFG
修改基于号段选择AMF配置|SET RESOLAMFNUMCFG
删除基于号段选择AMF配置|DEL RESOLAMFNUMCFG
查询基于号段选择AMF配置|SHOW RESOLAMFNUMCFG
设置基于号段选择MME策略|SET SELECTMMEPLYBASENUMSEG
查询基于号段选择MME策略|SHOW SELECTMMEPLYBASENUMSEG
新增基于号段选择MME配置|ADD SELECTMMECFGBYNUMSEG
修改基于号段选择MME配置|SET SELECTMMECFGBYNUMSEG
删除基于号段选择MME配置|DEL SELECTMMECFGBYNUMSEG
查询基于号段选择MME配置|SHOW SELECTMMECFGBYNUMSEG
设置基于号段选择NSSF策略|SET SELECTNSSFPOLICY
查询基于号段选择NSSF策略|SHOW SELECTNSSFPOLICY
新增基于号段选择NSSF配置|ADD SELECTNSSFCFG
修改基于号段选择NSSF配置|SET SELECTNSSFCFG
删除基于号段选择NSSF配置|DEL SELECTNSSFCFG
查询基于号段选择NSSF配置|SHOW SELECTNSSFCFG
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
各个拨测网元的拨测配置，基本一致。 
通过增加SMF\PCF\UDM\MME\AMF\NSSF\AUSF地址池配置，可以增加指定拨测SMF\PCF\UDM\MME\AMF\NSSF\AUSF的地址池。 
通过该配置基于号段选择SMF\PCF\UDM\MME\AMF\NSSF\AUSF策略，可以开启或关闭指定拨测SMF\PCF\UDM\MME\AMF\NSSF\AUSF网元。 
通过该配置基于号段选择SMF\PCF\UDM\MME\AMF\NSSF\AUSF配置，可以根据号段来指定拨测某个SMF\PCF\UDM\MME\AMF\NSSF\AUSF网元。 
配置前提 : 
网元正常运行。 
配置过程 : 
###### 拨测PCF配置过程 
拨测某PCF，需要配置该PCF相应的地址池。如果指定拨测的PCF有多个，则以各自的优先级、权重来决定优先级顺序。 
配置过程如下： 
执行[ADD PCFLOCALADDRPOOL]命令，增加指定拨测PCF的地址池。
执行[SET RESOLPCFSEGPOLICY]命令，设置基于号段选择PCF策略，开启支持基于号段选择PCF。
执行[ADD RESOLPCFSEGCFG]命令，设置基于号段选择PCF配置，配置某SUPI号段或GPSI号段，到指定拨测的PCF。
###### 拨测AUSF配置过程 
拨测某AUSF，需要配置该AUSF相应的地址池。如果指定拨测的AUSF有多个，则以各自的优先级、权重来决定优先级顺序。 
配置过程如下： 
执行[ADD AUSFLOCALADDRPOOL]命令，增加指定拨测AUSF的地址池。
执行[SET RESOLAUSFSEGPOLICY]命令，设置基于号段选择AUSF策略，开启支持基于号段选择AUSF。
执行[ADD RESOLAUSFSEGCFG]命令，设置基于号段选择AUSF配置，配置某SUPI号段或GPSI号段，到指定拨测的AUSF。
###### 拨测UDM配置过程 
拨测某UDM，需要配置该UDM相应的地址池。如果指定拨测的UDM有多个，则以各自的优先级、权重来决定优先级顺序。 
执行[ADD UDMLOCALADDRPOOL]命令，增加指定拨测UDM的地址池。
执行[SET RESOLUDMSEGPOLICY]命令，设置基于号段选择UDM策略，开启支持基于号段选择UDM。
执行[ADD RESOLUDMSEGCFG]命令，设置基于号段选择UDM配置，配置某SUPI号段或GPSI号段，到指定拨测的UDM。
###### 拨测AMF配置过程 
拨测某AMF，需要配置该AMF相应的地址池。如果指定拨测的AMF有多个，则以各自的优先级、权重来决定优先级顺序。 
执行[ADD AMFLOCALADDRPOOL]命令，增加指定拨测AMF的地址池。
执行[SET RESOLAMFPOLICY]命令，设置基于号段选择AMF策略，开启支持基于号段选择AMF。
执行[ADD RESOLAMFNUMCFG]命令，设置基于号段选择AMF配置，配置某SUPI号段或GPSI号段，到指定拨测的AMF。
###### 拨测MME配置过程 
拨测某MME，需要配置该MME相应的地址池。如果指定拨测的MME有多个，则以各自的优先级、权重来决定优先级顺序。 
执行[ADD ADDRPOOL]命令，增加指定拨测MME的地址池。
执行[ADD MMEHOST]命令，增加MME地址解析配置。
执行[SET SELECTMMEPLYBASENUMSEG]命令，设置基于号段选择MME策略，开启支持基于号段选择MME。
执行[ADD SELECTMMECFGBYNUMSEG]命令，设置基于号段选择MME配置，配置某SUPI号段或GPSI号段，到指定拨测的MME。
###### 拨测SMF配置过程 
拨测某SMF，需要配置该SMF相应的地址池。如果指定拨测的SMF有多个，则以各自的优先级、权重来决定优先级顺序。 
拨测A-SMF： 
执行[ADD SMFIPPOOLCFG]命令，增加指定拨测A-SMF的地址池。
执行[SET RESOLVESMFPOLICY]命令，设置基于号段选择A-SMF策略，开启支持基于号段选择A-SMF。
执行[ADD RESOLASMFCFG]命令，设置基于号段选择A-SMF配置，配置某SUPI号段或GPSI号段，到指定拨测的A-SMF。
拨测I-SMF和V-SMF： 
执行[ADD SMFIPPOOLCFG]命令，增加指定拨测I-SMF和V-SMF的地址池。
执行[SET RESOLVESMFPOLICY]命令，设置基于号段选择I-SMF和V-SMF策略，开启支持基于号段选择I-SMF和V-SMF。
执行[ADD RESOLIVSMFCFG]命令，设置基于号段选择I-SMF和V-SMF配置，配置某SUPI号段或GPSI号段，到指定拨测的I-SMF和V-SMF。
###### 拨测NSSF配置过程 
拨测某NSSF，需要配置该NSSF相应的地址池。如果指定拨测的NSSF有多个，则以各自的优先级、权重来决定优先级顺序。 
配置过程如下： 
执行[ADD NSSFLOCALADDRPOOL]命令，增加指定拨测NSSF的地址池。
执行[SET SELECTNSSFPOLICY]命令，设置基于号段选择NSSF策略，开启支持基于号段选择NSSF。
执行[ADD RESOLAUSFSEGCFG]命令，设置基于号段选择NSSF配置，配置某SUPI号段或GPSI号段，到指定拨测的NSSF。
配置实例 : 
###### 拨测PCF 
场景说明
通过配置SUPI号段来指定拨测到某个PCF。 
数据规划
配置项|参数|取值
---|---|---
配置PCF地址池|地址池标识|1
IP地址|配置PCF地址池|192.168.1.1
端口号|配置PCF地址池|8000
配置支持基于号段选择PCF|支持基于号段选择PCF|支持
配置SUPI号段指定拨测到某个PCF|用户号码|460111234567890
号码类型|配置SUPI号段指定拨测到某个PCF|SUPI
NF实例标识|配置SUPI号段指定拨测到某个PCF|2b3d8182-365c-44ff-a051-ef56f89732d5
FQDN|配置SUPI号段指定拨测到某个PCF|zte.com
地址池标识|配置SUPI号段指定拨测到某个PCF|1
优先级|配置SUPI号段指定拨测到某个PCF|0
权重|配置SUPI号段指定拨测到某个PCF|200
URI scheme|配置SUPI号段指定拨测到某个PCF|HTTP
API版本|配置SUPI号段指定拨测到某个PCF|V1
有效时间|配置SUPI号段指定拨测到某个PCF|2021-09-23 00:00:00
配置步骤
步骤|说明|操作
---|---|---
1|增加PCF地址池。|ADD PCFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="192.168.1.1",PORT=8000
2|将“支持基于号段选择PCF”的开关打开。|SET RESOLPCFSEGPOLICY:SUPPCFNUMSEL="SPRT"
3|配置SUPI号段指定拨测到某个PCF。|ADD RESOLPCFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",NFINSTANCEID="2b3d8182-365c-44ff-a051-ef56f89732d5",FQDN="zte.com",IPPOOLID=1,PRIORITY=0,WEIGHT=200,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2021-09-23 00:00:00"
###### 拨测AUSF 
场景说明
通过配置SUPI号段指来定拨测到某个AUSF。 
数据规划
配置项|参数|取值
---|---|---
配置AUSF地址池|地址池标识|1
IP地址|配置AUSF地址池|192.168.1.1
端口号|配置AUSF地址池|8000
配置支持基于号段选择AUSF|支持基于号段选择AUSF|支持
配置SUPI号段指定拨测到AUSF|用户号码|460111234567890
号码类型|配置SUPI号段指定拨测到AUSF|SUPI
NF实例标识|配置SUPI号段指定拨测到AUSF|2b3d8182-365c-44ff-a051-ef56f89732d5
FQDN|配置SUPI号段指定拨测到AUSF|zte.com
地址池标识|配置SUPI号段指定拨测到AUSF|1
优先级|配置SUPI号段指定拨测到AUSF|0
权重|配置SUPI号段指定拨测到AUSF|200
URI scheme|配置SUPI号段指定拨测到AUSF|HTTP
API版本|配置SUPI号段指定拨测到AUSF|V1
有效时间|配置SUPI号段指定拨测到AUSF|2021-09-23 00:00:00
配置步骤
步骤|说明|操作
---|---|---
1|增加AUSF地址池。|ADD AUSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="192.168.1.1",PORT=8000
3|将“支持基于号段选择AUSF”的开关打开。|SET RESOLAUSFSEGPOLICY:SUPAUSFNUMSEL="SPRT"
4|配置SUPI号段指定拨测到AUSF，关联地址池1，优先级为0。|ADD RESOLAUSFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",NFINSTANCEID="2b3d8182-365c-44ff-a051-ef56f89732d5",FQDN="zte.com",IPPOOLID=1,PRIORITY=0,WEIGHT=200,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2021-09-23 00:00:00"
###### 拨测UDM 
场景说明
通过配置GPSI号段来指定拨测到某个UDM。 
数据规划
配置项|参数|取值
---|---|---
配置UDM地址池|地址池标识|1
IP地址|配置UDM地址池|192.168.1.1
端口号|配置UDM地址池|8000
配置支持基于号段选择UDM|支持基于号段选择UDM|支持
配置GPSI号段指定拨测到某个UDM|用户号码|8613812345678
号码类型|配置GPSI号段指定拨测到某个UDM|GPSI
NF实例标识|配置GPSI号段指定拨测到某个UDM|2b3d8182-365c-44ff-a051-ef56f89732d5
FQDN|配置GPSI号段指定拨测到某个UDM|zte.com
地址池标识|配置GPSI号段指定拨测到某个UDM|1
优先级|配置GPSI号段指定拨测到某个UDM|0
权重|配置GPSI号段指定拨测到某个UDM|200
URI scheme|配置GPSI号段指定拨测到某个UDM|HTTP
API版本|配置GPSI号段指定拨测到某个UDM|V1
有效时间|配置GPSI号段指定拨测到某个UDM|2021-09-23 00:00:00
配置步骤
步骤|说明|操作
---|---|---
1|增加UDM地址池。|ADD UDMLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="192.168.1.1",PORT=8000。
2|将“支持基于号段选择UDM”的开关打开。|SET RESOLPCFSEGPOLICY:SUPUDMNUMSEL="SPRT"。
3|配置GPSI号段指定拨测到某个UDM。|ADD RESOLUDMSEGCFG:NUMBER="8613812345678",NUMTYPE="GPSI",NFINSTANCEID="2b3d8182-365c-44ff-a051-ef56f89732d5",FQDN="zte.com",IPPOOLID=1,PRIORITY=0,WEIGHT=200,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2021-09-23 00:00:00"。
###### 拨测AMF 
场景说明
通过配置GPSI号段来指定拨测到某个AMF。 
数据规划
配置项|参数|取值
---|---|---
配置AMF地址池|地址池标识|1
IP地址|配置AMF地址池|192.168.1.1
端口号|配置AMF地址池|8080
配置支持基于号段选择AMF|支持基于号段选择AMF|支持
配置GPSI号段指定拨测到某个AMF|用户号码|13812345678
号码类型|配置GPSI号段指定拨测到某个AMF|GPSI
NF实例标识|配置GPSI号段指定拨测到某个AMF|f81d4fae-7dec-1111-a765-00a0c91e6789
FQDN|配置GPSI号段指定拨测到某个AMF|amf1
地址池标识|配置GPSI号段指定拨测到某个AMF|1
优先级|配置GPSI号段指定拨测到某个AMF|1
权重|配置GPSI号段指定拨测到某个AMF|10
URI scheme|配置GPSI号段指定拨测到某个AMF|HTTP
API版本|配置GPSI号段指定拨测到某个AMF|V1
有效时间|配置GPSI号段指定拨测到某个AMF|2022-01-20 11:16:38
配置步骤
步骤|说明|操作
---|---|---
1|增加AMF地址池。|ADD AMFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="192.168.1.1",PORT=8080
2|将“支持基于号段选择AMF”的开关打开。|SET RESOLAMFPOLICY:SUPAMFNUMSEL="SPRT"
3|配置GPSI号段指定拨测到某个AMF。|ADD RESOLAMFNUMCFG:NUMBER="13812345678",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",FQDN="amf1",IPPOOLID=1,PRIORITY=1,WEIGHT=10,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2022-01-20 11:16:38"
###### 拨测MME 
场景说明
通过配置GPSI号段来指定拨测到某个MME。 
数据规划
配置项|参数|取值
---|---|---
配置MME地址池|IP类型|IPV4
IP地址|配置MME地址池|192.168.22.22
地址池标识|配置MME地址池|1
MME地址解析配置|FQDN|tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org
主机名|MME地址解析配置|mme22
优先级|MME地址解析配置|1
权重|MME地址解析配置|100
地址池标识|MME地址解析配置|1
配置支持基于号段选择MME|支持基于号段选择MME|支持
配置GPSI号段指定拨测到某个MME|编号|1
用户号码|配置GPSI号段指定拨测到某个MME|13895122456
号码类型|配置GPSI号段指定拨测到某个MME|GPSI
地址池标识|配置GPSI号段指定拨测到某个MME|1
优先级|配置GPSI号段指定拨测到某个MME|1
权重|配置GPSI号段指定拨测到某个MME|10
有效时间|配置GPSI号段指定拨测到某个MME|2021-09-23 00:00:00
配置步骤
步骤|说明|操作
---|---|---
1|增加MME地址池。|ADD ADDRPOOL:IPTYPE="IPV4",IPADDR="192.168.22.22",ADDRPOOLID=1
2|增加MME地址解析配置。|ADD MMEHOST:LOGICNAME="mmec86.mmegi0140.mme.epc.mnc002.mcc460.3gppnetwork.org",HOSTNAME="mme22",PRIORITY=1,WEIGHT=100,ADDRPOOLID=1
3|将“支持基于号段选择MME”的开关打开。|SET SELECTMMEPLYBASENUMSEG:SUPMMENUMSEL="SPRT"
4|配置GPSI号段指定拨测到某个MME。|ADD SELECTMMECFGBYNUMSEG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",IPADDRESSPOOLID=1,PRIORITY=1,WEIGHT=10,VALIDITYPERIOD="2020-01-20 11:16:38"
###### 拨测SMF 
场景说明
通过配置GPSI号段来指定拨测到某个SMF。 
数据规划
配置项|参数|取值
---|---|---
配置SMF地址池|地址池标识|1
IP地址|配置SMF地址池|192.168.1.1
端口号|配置SMF地址池|8080
配置支持基于号段选择A-SMF|支持基于号段选择A-SMF|支持
配置支持基于号段选择I-SMF和V-SMF|支持基于号段选择I-SMF和V-SMF|支持
配置GPSI号段指定拨测到A-SMF|编号|1
用户号码|配置GPSI号段指定拨测到A-SMF|13895122456
号码类型|配置GPSI号段指定拨测到A-SMF|GPSI
NF实例标识|配置GPSI号段指定拨测到A-SMF|f81d4fae-7dec-1111-a765-00a0c91e6789
A-SMF FQDN|配置GPSI号段指定拨测到A-SMF|zte.com.cn
地址池标识|配置GPSI号段指定拨测到A-SMF|1
优先级|配置GPSI号段指定拨测到A-SMF|1
权重|配置GPSI号段指定拨测到A-SMF|10
URI scheme|配置GPSI号段指定拨测到A-SMF|HTTP
API版本|配置GPSI号段指定拨测到A-SMF|V1
PGW FQDN|配置GPSI号段指定拨测到A-SMF|zte123.com.cn
有效时间|配置GPSI号段指定拨测到A-SMF|2020-01-20 11:16:38
配置GPSI号段指定拨测到I-SMF和V-SMF|编号|1
用户号码|配置GPSI号段指定拨测到I-SMF和V-SMF|13895122456
号码类型|配置GPSI号段指定拨测到I-SMF和V-SMF|GPSI
NF实例标识|配置GPSI号段指定拨测到I-SMF和V-SMF|f81d4fae-7dec-1111-a765-00a0c91e6789
SMF FQDN|配置GPSI号段指定拨测到I-SMF和V-SMF|zte.com.cn
地址池标识|配置GPSI号段指定拨测到I-SMF和V-SMF|1
优先级|配置GPSI号段指定拨测到I-SMF和V-SMF|1
权重|配置GPSI号段指定拨测到I-SMF和V-SMF|10
URI scheme|配置GPSI号段指定拨测到I-SMF和V-SMF|HTTP
API版本|配置GPSI号段指定拨测到I-SMF和V-SMF|V1
有效时间|配置GPSI号段指定拨测到I-SMF和V-SMF|2020-01-20 11:16:38
配置步骤
步骤|说明|操作
---|---|---
1|增加SMF地址池。|ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS="192.168.1.1",PORT=8080
2|配置支持基于号段选择A-SMF。|SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT"
3|配置支持基于号段选择I-SMF和V-SMF。|SET RESOLVESMFPOLICY:SUPIVSMFNUMSEL="SPRT"
4|配置GPSI号段指定拨测到A-SMF。|ADD RESOLASMFCFG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",HOST="zte.com.cn",IPPOOLID=1,PRIORITY=1,WEIGHT=10,SCHEMEAPIVERSION="HTTP",APIVERSION="V1",PGWFQDN="zte123.com.cn",VALIDITYTIME="2020-01-20 11:16:38"
5|配置GPSI号段指定拨测到I-SMF和V-SMF。|ADD RESOLIVSMFCFG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",HOST="zte.com.cn",IPPOOLID=1,PRIORITY=1,WEIGHT=10,SCHEMEAPIVERSION="HTTP",APIVERSION="V1",VALIDITYTIME="2020-01-20 11:16:38"
###### 拨测NSSF 
场景说明
通过配置GPSI号段来指定拨测到某个NSSF。 
数据规划
配置项|参数|取值
---|---|---
增加NSSF 地址池配置|地址池标识|1
IP地址|增加NSSF 地址池配置|192.168.22.22
端口号|增加NSSF 地址池配置|8080
设置基于号段选择NSSF策略|支持基于号段选择NSSF|支持
新增基于号段选择NSSF配置|用户号码|13895122456
号码类型|新增基于号段选择NSSF配置|GPSI
NSSF FQDN|新增基于号段选择NSSF配置|2b3d8182-365c-44ff-a051-ef56f89732d5
地址池标识|新增基于号段选择NSSF配置|1
URI scheme|新增基于号段选择NSSF配置|HTTP
API版本|新增基于号段选择NSSF配置|V1
优先级|新增基于号段选择NSSF配置|1
权重|新增基于号段选择NSSF配置|10
有效时间|新增基于号段选择NSSF配置|2021-12-31 00:00:00
配置步骤
步骤|说明|操作
---|---|---
1|增加NSSF地址池配置。|ADD NSSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="192.168.22.22",PORT=8080
2|将“支持基于号段选择NSSF”的开关打开。|SET SELECTNSSFPOLICY:SUPNSSFNUMSEL="SPRT"
3|配置GPSI号段指定拨测到某个NSSF。|ADD SELECTNSSFCFG:NUMBER="13895122456",NUMTYPE="GPSI",FQDN="2b3d8182-365c-44ff-a051-ef56f89732d5",IPPOOLID=1,PRIORITY=1,WEIGHT=10,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2021-12-31 00:00:00"
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|测试根据SUPI号段能够指定拨测到某个指定PCF
---|---
测试目的|测试根据SUPI号段能够指定拨测到某个指定PCF。
预置条件|无
测试过程|增加PCF地址池配置，增加指定拨测PCF的地址池。修改基于号段选择PCF策略，打开支持基于号段选择PCF开关。配置测试SUPI号段拨测该PCF，地址池配置为该PCF的地址池。用该号段的用户发起初始注册，并发起PCF建立流程。
通过准则|使用拨测的PCF交互成功。
测试结果|–
测试项目|测试根据SUPI号段能够指定拨测到某个指定AUSF
---|---
测试目的|测试根据SUPI号段能够指定拨测到某个指定AUSF。
预置条件|无
测试过程|增加AUSF地址池配置，增加指定拨测AUSF的地址池。修改基于号段选择AUSF策略，打开支持基于号段选择AUSF开关。配置测试SUPI号段拨测该AUSF，地址池配置为该AUSF的地址池。用该号段的用户发起初始注册，与AUSF交互。
通过准则|使用拨测的AUSF交互成功。
测试结果|–
测试项目|测试根据GPSI号段能够指定拨测到某个指定UDM
---|---
测试目的|测试根据GPSI号段能够指定拨测到某个指定UDM。
预置条件|无
测试过程|增加UDM地址池配置，增加指定拨测UDM的地址池。修改基于号段选择UDM策略，打开支持基于号段选择UDM开关。配置测试GPSI号段拨测该UDM，地址池配置为该UDM的地址池。用该号段的用户发起初始注册，与UDM交互。
通过准则|使用拨测UDM交互成功。
测试结果|–
测试项目|测试根据SUPI号段能够指定拨测到某个指定AMF
---|---
测试目的|测试根据SUPI号段能够指定拨测到某个指定AMF。
预置条件|无
测试过程|增加AMF地址池配置，增加指定拨测AMF的地址池。修改基于号段选择AMF策略，打开支持基于号段选择AMF开关。配置测试SUPI号段拨测该AMF，地址池配置为该AMF的地址池。用该号段的用户发起N2切换流程。
通过准则|发起N2切换的目标局为配置的指定拨测AMF。
测试结果|–
测试项目|测试根据SUPI号段能够指定拨测到某个指定MME
---|---
测试目的|测试根据SUPI号段能够指定拨测到某个指定MME。
预置条件|无
测试过程|增加MME地址池配置，增加指定拨测MME的地址池。增加MME地址解析配置。修改基于号段选择MME策略，打开支持基于号段选择MME开关。配置测试SUPI号段拨测该MME，地址池配置为该MME的地址池。用该号段的用户发起5到4切换流程，与MME交互。
通过准则|5到4切换流程与拨测的MME交互成功。
测试结果|–
测试项目|测试根据GPSI号段能够指定拨测到某个指定SMF
---|---
测试目的|测试根据GPSI号段能够指定拨测到某个指定SMF。
预置条件|无
测试过程|增加SMF地址池配置，增加指定拨测SMF的地址池。修改基于号段选择SMF策略，打开支持基于号段选择A-SMF或者支持基于号段选择I-SMF和V-SMF策略开关。配置测试GPSI号段拨测A-SMF或者I-SMF和V-SMF，地址池配置为该SMF的地址池。用该号段的用户发起PDU建立流程，与SMF交互。
通过准则|与拨测的SMF交互成功。
测试结果|–
测试项目|测试根据GPSI号段能够指定拨测到某个指定NSSF
---|---
测试目的|测试根据GPSI号段能够指定拨测到某个指定NSSF。
预置条件|无
测试过程|增加NSSF地址池配置，增加指定拨测NSSF的地址池。修改基于号段选择NSSF策略，打开支持基于号段选择NSSF开关。配置测试GPSI号段拨测该NSSF，地址池配置为该NSSF的地址池。用该GPSI号段的用户发起初始注册，并发起切片选择。
通过准则|进行切片选择的NSSF为配置的指定拨测NSSF。
测试结果|–
常见问题处理 : 
无 
# 缩略语 
# 缩略语 
AMF : 
Access and Mobility Management Function接入和移动管理功能
AUSF : 
Authentication Server Function鉴权服务器功能
CHR : 
Call History Record呼叫历史记录
DNN : 
Data Network Name数据网名称
GPSI : 
Generic Public Subscription Identifier一般公共用户标识
MME : 
Mobility Management Entity移动管理实体
NSSF : 
Network Slice Selection Function网络切片选择功能
PCF : 
Policy Control Function策略控制功能
SMF : 
Session Management Function会话管理功能
SUPI : 
Subscriber Permanent Identifier用户永久标识
UDM : 
Unified Data Management统一数据管理
# ZUF-76-13 网元安全管理 
## ZUF-76-13-001 服务化接口安全 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
SBI接口安全是指为了应对SBI接口的网络安全风险，降低网络受攻击的风险，所采取的安全措施。
ZTE AMF在SBI接口安全方面提供了如下措施：
基于OAuth2的动态授权。 
基于本地配置的静态授权。 
背景知识 : 
随着计算机技术和通信技术的不断发展，人们除了享受技术发展所得来的便利性的同时，也时刻面临着各种各样的安全风险。为了解决安全风险，信息服务提供商，包括设备制造商、运营商，衍生出了各种各样的安全措施，其中授权是一项非常重要且广泛使用的安全措施。5G作为新一代网络通信技术，相比以前的通信技术，更加开放，因而其所面临的安全风险也更加突出。 
应用场景 : 
SBI接口安全应用以下场景中： 
在5GC网络未启用NRF动态授权（OAuth2）方式时，可采用AMF本地静态授权的方式，对NF的服务调用进行授权控制。在启用OAuth2方式时，一般不需要叠加启用AMF本地静态授权功能。 
在5GC网络启用NRF静态授权（NF/NFSProfile）的方式时，可同时采用AMF本地静态授权的方式，对NF的服务调用进行授权控制。 
在5GC网络未启用NRF动态授权（OAuth2）方式，也未启用NRF静态授权（NF/NFSProfile）的方式时，可采用AMF本地静态授权的方式，对NF的服务调用进行授权控制。 
客户收益 : 
受益方|受益描述
---|---
运营商|降低网络安全风险，提高网络服务质量。
移动用户|对用户不可见。
实现原理 : 
系统架构 : 
本特性涉及到的网络结构如[图1]所示。
图1  服务化接口安全的组网图
###### 涉及的NF 
NF名称|NF作用
---|---
NRF|基于OAuth2授权时，提供各NF的访问令牌。基于静态授权时，在服务发现过程中，执行服务提供方注册时的静态授权策略，比如允许的PLMN检查。
Other NFs|包括SMF、AUSF、UDM等。基于OAuth2授权时，校验AMF携带过来的访问令牌，校验通过才允许AMF的调用请求。基于静态授权时，向NRF注册时携带本地配置的静态策略，比如允许的PLMN、S-NSSAI等。
协议栈 : 
各接口均为SBI接口，对应的协议栈如[图2]所示。
图2  SBI接口协议
###### 本NF实现 
ZTE AMF支持基于OAuth2的动态授权和基于本地配置的静态授权，并支持通过本地配置选择SBI接口安全模式。 
基于OAuth2的动态授权第一次调用其他NF服务时，向NRF获取该NF服务的访问令牌并缓存。调用其他NF的服务时，请求消息中携带访问令牌，用于其他NF认证本AMF是否有权限调用该服务。访问令牌失效时，重新向NRF获取。 
基于本地配置的静态授权提供黑/白名单两种授权模式，禁止或者允许访问本AMF的PLMN、S-NSSAI、URI、NF类型、NF域。当采用黑名单配置时，只要处于黑名单范围，则禁止其他NF的服务调用请求。当采用白名单配置时，只要处于白名单范围，则允许其他NF的服务调用。向NRF注册时，携带本地配置时允许访问本AMF的PLMN、S-NSSAI、NF类型、NF域。 
###### 基于OAuth2的动态授权业务流程 
基于OAuth2的动态授权业务流程如[图3]所示。
图3  基于OAuth2的动态授权业务流程
流程说明： 
在第一次调用Other NFs服务时，或者缓存的访问令牌失效，则发送Nnrf_AccessToken_Get Request给NRF，获取Other NFs的访问令牌。 
NRF生成访问令牌，并在Nnrf_AccessToken_Get Response中带给AMF，AMF缓存该访问令牌。 
AMF调用Other NFs服务，携带NRF返回的访问令牌，用于Other NFs针对本AMF进行认证授权。 
###### 基于本地配置的静态授权业务流程 
AMF发起NRF注册流程，携带本地配置的静态授权信息流程如[图4]所示。
图4  AMF发起NRF注册流程，携带本地配置的静态授权信息流程
流程说明： 
AMF向NRF发起注册。 
如果本地静态授权配置了PLMN白名单，则注册请求消息中携带Allowed PLMN。 
如果本地静态授权配置中配置了NF Domain白名单，则注册请求消息中携带Allowed NF Domains。 
如果本地静态授权配置中配置了NF类型白名单，则注册请求消息中携带Allowed NF Types。 
如果本地静态授权配置中配置了S-NSSAI白名单，则注册请求消息中携带Allowed NSSAIs。 
NRF保存AMF的注册信息，包括携带过来的静态授权信息，并返回注册响应给AMF。 
AMF发起NRF更新流程，携带最新本地配置的静态授权信息流程如[图5]所示。
图5  AMF发起NRF更新流程，携带最新本地配置的静态授权信息
流程说明： 
如果本地静态授权配置中，PLMN白名单、NF Domain白名单、S-NSSAI白名单、NF类型白名单，其中之一配置发生变化，则AMF向NRF发起更新流程。 
NRF保存AMF的最新信息并返回更新响应给AMF。 
AMF执行本地授权检查流程如[图6]所示。
图6  AMF执行本地授权检查
流程说明： 
AMF收到其他NF调用本AMF的服务调用请求，执行本地配置的静态授权检查。 
AMF返回服务调用响应给调用者NF。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称|章节
---|---
3GPP TS 29.510 Network Function Repository Services;Stage 3|Nnrf_AccessToken ServiceNnrf_AccessToken Service API
3GPP TS 33.501 Security architecture and procedures for 5G system|Service Based Interfaces (SBI)
RFC 6749|IETF RFC 6749: "OAuth2.0 Authorization Framework"
RFC 7519|IETF RFC 7519: "JSON Web Token (JWT)"
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 : 
该特性为ZXUN-uMAC的基本特性，无需License支持。 
对其他网元的要求 : 
UE|NRF|Other NFs
---|---|---
-|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
配置项表1  新增配置项配置项命令Oauth2配置SET NFOAUTHPOLICYSHOW NFOAUTHPOLICY静态授权策略SET STATICAUTHPOLICYSHOW STATICAUTHPOLICYPLMN白名单配置ADD ALLOWEDPLMNSSET ALLOWEDPLMNSDEL ALLOWEDPLMNSSHOW ALLOWEDPLMNSNF类型白名单配置ADD ALLOWEDNFTYPESSET ALLOWEDNFTYPESDEL ALLOWEDNFTYPESSHOW ALLOWEDNFTYPESNF域白名单配置ADD ALLOWEDNFDOMAINSSET ALLOWEDNFDOMAINSDEL ALLOWEDNFDOMAINSSHOW ALLOWEDNFDOMAINSSnssai白名单配置ADD ALLOWEDSNSSAISET ALLOWEDSNSSAIDEL ALLOWEDSNSSAISHOW ALLOWEDSNSSAIURI白名单配置ADD URIWHITECFGDEL URIWHITECFGSHOW URIWHITECFGURI黑名单配置ADD URIBLACKCFGDEL URIBLACKCFGSHOW URIBLACKCFG 
安全变量该特性不涉及安全变量的改变。 
软件参数该特性不涉及软件参数的改变。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
在AMF上设置服务化接口安全功能的相关配置。 
配置前提 : 
AMF系统正常运行。 
配置过程 : 
执行[SET STATICAUTHPOLICY]命令，设置静态授权策略。
执行[ADD ALLOWEDSNSSAI]命令，添加Snssai白名单配置。
执行[ADD ALLOWEDPLMNS]命令，添加PLMN白名单配置。
执行[ADD ALLOWEDNFTYPES]命令，添加NF类型白名单配置。
执行[ADD ALLOWEDNFDOMAINS]命令，添加NF域白名单配置。
执行[ADD URIWHITECFG]命令，添加URI白名单配置。
执行[ADD URIBLACKCFG]命令，添加URI黑名单配置。
配置实例 : 
###### 示例1 
场景说明
NRF静态授权开启，向NRF注册消息中会携带AllowXXX参数，如allowedPlmns、allowedNfTypes等。
数据规划
参数|示例
---|---
配置静态授权策略信息|NRF静态授权开关|On
本地静态授权开关|配置静态授权策略信息|Off
名单判断开关|配置静态授权策略信息|WhiteList
授权失败处理|配置静态授权策略信息|Drop
NF类型授权处理开关|配置静态授权策略信息|Off
配置AllowedSnssai信息|编号|1
服务类型|配置AllowedSnssai信息|COMMUNICATION
SST|配置AllowedSnssai信息|eMBB
SD|配置AllowedSnssai信息|123456
配置AllowedPlmns信息|编号|1
服务类型|配置AllowedPlmns信息|COMMUNICATION
移动国家码|配置AllowedPlmns信息|460
移动网络码|配置AllowedPlmns信息|11
配置AllowedNFTypes信息|编号|1
服务类型|配置AllowedNFTypes信息|COMMUNICATION
NF类型|配置AllowedNFTypes信息|AMF
配置AllowedNFDomains信息|编号|1
服务类型|配置AllowedNFDomains信息|COMMUNICATION
NF域|配置AllowedNFDomains信息|zte.com.cn
配置步骤
步骤|说明|命令
---|---|---
1|配置静态授权策略信息。|SET STATICAUTHPOLICY:NRFAUTHSWITCH="On",LOCALAUTHSWITCH="Off",WHITEORBLACK="WhiteList",AUTHFAILUREHANDING="Drop",USERAGENTSWITCH="Off"
2|配置AllowedSnssai信息。|ADD ALLOWEDSNSSAI:ID=1,SERVICETYPE="COMMUNICATION",SST="eMBB",SD="123456"
3|配置AllowedPlmns信息。|ADD ALLOWEDPLMNS:ID=1,SERVICETYPE="COMMUNICATION",MCC="460",MNC="11"
4|配置AllowedNFTypes信息。|ADD ALLOWEDNFTYPES:ID=1,SERVICETYPE="COMMUNICATION",NFTYPE="AMF"
5|配置AllowedNFDomains信息。|ADD ALLOWEDNFDOMAINS:ID=1,SERVICETYPE="COMMUNICATION",NFDOMAIN="zte.com.cn"
###### 示例2 
场景说明
URI不在白名单里，NonUeN2InfoSubscribeReq消息中的N2NotifyCallbackUri不在白名单中，回复NonUeN2InfoSubscribeReq消息时AMF返回失败响应。
数据规划
参数|示例
---|---
配置静态授权策略信息|NRF静态授权开关|Off
本地静态授权开关|配置静态授权策略信息|On
名单判断开关|配置静态授权策略信息|WhiteList
授权失败处理|配置静态授权策略信息|ReplyFailedRes
NF类型授权处理开关|配置静态授权策略信息|Off
配置URI白名单信息|IP类型|IPV4
IP开始地址|配置URI白名单信息|0.0.0.0
IP结束地址|配置URI白名单信息|0.0.0.0
配置步骤
步骤|说明|命令
---|---|---
1|配置静态授权策略信息。|SET STATICAUTHPOLICY:NRFAUTHSWITCH="Off",LOCALAUTHSWITCH="On",WHITEORBLACK="WhiteList",AUTHFAILUREHANDING="ReplyFailedRes",USERAGENTSWITCH="Off"
2|配置URI白名单信息。|ADD URIWHITECFG:IPTYPE="IPV4",IPADDRSTART=0.0.0.0,IPADDREND=0.0.0.0
###### 示例3 
场景说明
LMF发起NonUeN2InfoSubscribe消息，由于URI在黑名单里，回复NonUeN2InfoSubscribeReq消息时AMF返回失败响应。
数据规划
参数|示例
---|---
配置静态授权策略信息|NRF静态授权开关|Off
本地静态授权开关|配置静态授权策略信息|On
名单判断开关|配置静态授权策略信息|WhiteList
授权失败处理|配置静态授权策略信息|ReplyFailedRes
NF类型授权处理开关|配置静态授权策略信息|Off
配置URI黑名单信息|IP类型|IPV4
IP开始地址|配置URI黑名单信息|192.32.1.5
IP结束地址|配置URI黑名单信息|192.32.1.16
配置步骤
步骤|说明|命令
---|---|---
1|配置静态授权策略信息。|SET STATICAUTHPOLICY:NRFAUTHSWITCH="Off",LOCALAUTHSWITCH="On",WHITEORBLACK="BlackList",AUTHFAILUREHANDING="ReplyFailedRes",USERAGENTSWITCH="Off"
2|配置URI黑名单信息，设置NonUeN2InfoSubscribeReq消息中的N2NotifyCallbackUri在黑名单中。|ADD URIBLACKCFG:IPTYPE="IPV4",IPADDRSTART=192.32.1.5,IPADDREND=192.32.1.16
###### 示例4 
场景说明
PCF发送的N1N2MessageTransfer消息，由于URI在黑名单里，回复N1N2MessageTransfer消息时AMF返回失败响应。
数据规划
参数|示例
---|---
配置静态授权策略信息|NRF静态授权开关|Off
本地静态授权开关|配置静态授权策略信息|On
名单判断开关|配置静态授权策略信息|WhiteList
授权失败处理|配置静态授权策略信息|ReplyFailedRes
NF类型授权处理开关|配置静态授权策略信息|Off
配置URI黑名单信息|IP类型|IPV4
IP开始地址|配置URI黑名单信息|192.32.1.25
IP结束地址|配置URI黑名单信息|192.32.1.36
配置步骤
步骤|说明|命令
---|---|---
1|配置静态授权策略信息。|SET STATICAUTHPOLICY:NRFAUTHSWITCH="Off",LOCALAUTHSWITCH="On",WHITEORBLACK="BlackList",AUTHFAILUREHANDING="ReplyFailedRes",USERAGENTSWITCH="Off"
2|配置URI黑名单信息，设置N1N2MessageTransfer消息中的n1n2FailureTxfNotifURI里的IP在黑名单中。|ADD URIBLACKCFG:IPTYPE="IPV4",IPADDRSTART=192.32.1.25,IPADDREND=192.32.1.36
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|NRF静态授权功能正常
---|---
测试目的|NRF静态授权是否生效。
预置条件|NRF静态授权开关开启。
测试过程|AMF自动向NRF发起注册。
通过准则|向NRF注册消息携带AllowXXX参数，如allowedPlmns、allowedNfTypes等。
测试结果|–
测试项目|URI不在白名单里，返回失败消息
---|---
测试目的|URI不在白名单里，回复NonUeN2InfoSubscribeReq消息时返回失败响应。
预置条件|静态授权开关打开。
测试过程|LMF发送NonUeN2InfoSubscribeReq，携带的N2NotifyCallbackUri不在白名单中。
通过准则|AMF回复了失败响应。
测试结果|–
测试项目|URI在黑名单里，返回失败消息
---|---
测试目的|URI在黑名单里，回复NonUeN2InfoSubscribeReq消息时返回失败响应。
预置条件|静态授权开关打开。
测试过程|LMF发起NonUeN2InfoSubscribe，携带的N2NotifyCallbackUri在黑名单中。
通过准则|AMF回复了失败响应。
测试结果|–
常见问题处理 : 
无。 
## ZUF-76-13-002 GTP接口安全 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
AMF网元可以检查消息发送方是否被授权发送GTP-C协议的每条消息。通过“消息类型+IP地址”的组合以及黑白名单的设置，实现AMF对指定GTP-C消息的过滤功能。 
背景知识 : 
无 
应用场景 : 
当AMF收到N26接口上符合协议的GTP消息，如果需要针对GTP的消息类型和发送方IP进行过滤时，可使用该功能。 
客户收益 : 
受益方|受益描述
---|---
运营商|通过实现GTP-C过滤名单来应对GTP边界的安全，可防止非法消息冲击服务，并达到防欺诈、防攻击的作用。
移动用户|用户可享受更稳定和更可靠的网络服务。
实现原理 : 
系统架构 : 
GTP消息检查功能的系统架构如[图1]所示。
图1  系统架构-GTP消息检查
涉及的网元 : 
网元名称|网元作用
---|---
AMF|在业务端，结合GTP消息类型和发送方IP地址，决策是否需要进行GTP-C的消息过滤。
协议栈 : 
接口|描述|协议栈
---|---|---
N26|AMF与MME之间逻辑接口|ZUF-79-19-009 N26
本网元实现 : 
AMF会根据当前设置的黑白名单类型，按照“消息类型+IP类型”对GTP-C消息进行过滤，确认该消息是否可被AMF处理或转发。 
针对不符合安全检查要求被丢弃的GTP消息，可通过动态命令分别查找当前黑、白名单中的过滤消息统计的数量；支持对GTP的过滤统计进行清空操作。 
正常情况下，AMF需要处理的GTP消息类型（仅N26接口）参见[表1]。除此之外，其他消息类型均为非法，会在IPS处丢弃，业务并不会处理。
Message ID|NAME
---|---
1|Echo Request
2|Echo Response
3|Version Not Supported Indication
128|Identification Request
129|Identification Response
130|Context Request
131|Context Response
132|Context Acknowledge
133|Forward Relocation Request
134|Forward Relocation Response
135|Forward Relocation Complete Notification
136|Forward Relocation Complete Acknowledge
139|Relocation Cancel Request
140|Relocation Cancel Response
141|Configuration Transfer Tunnel
业务流程 : 
GTP-C消息过滤流程如[图2]所示。
图2  GTP-C消息过滤流程图
业务处理逻辑
AMF运行正常，收到来自N26口的GTP消息。 
开启“GTP安全检查开关”→转2 
未开启“GTP安全检查开关”→转入8 
查询GTP黑名单开关类型。 
黑名单→转3 
白名单→转6 
检查对端地址是否在黑名单网段。 
是→转4 
否→转8 
检查消息类型是否在黑名单网段配置。 
是→转5 
否→转8 
该GTP消息类型与源地址IP均在黑名单配置中。应直接丢弃该消息，并上报相应告警及计数器，流程结束。 
检查对端地址是否在白名单网段。 
是→转7 
否→转9 
检查消息类型是否在白名单网段配置。 
是→转8 
否→转9 
当前策略配置下，该消息符合AMF的安全检查规则或未开启策略，可正常处理业务流程，流程结束。 
该GTP消息类型或源地址IP有一种或均不满足白名单配置。应直接丢弃该消息，并上报相应告警及计数器，流程结束。 
动态命令
GTP统计查询 ：设置黑、白名单类型后，可查询当前被AMF过滤的GTP消息的数量。 
GTP统计清除： 删除当前AMF的GTP过滤统计信息。 
系统影响 : 
为提高IP地址查询的处理能力，本特性采用Trie表的方式实现，但需要额外消耗内存。例如，目前白名单为1024个，黑名单为256个，估计占用内存2~3 M。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称|章节
---|---
3GPP TS 33.117 Catalogue of general security assurance requirements|-
3GPP TS 33.512 Access and Mobility management Function (AMF)|-
特性能力 : 
名称|指标
---|---
黑白名单采用Trie表的方式|黑名单256个，白名单1024个，预计占用内存2-3 M。
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.20.20|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
UE|AMF
---|---
-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
配置项表2  新增配置项配置项命令GTP安全检查开关配置SET GTPSECCHKSWITCHSHOW GTPSECCHKSWITCHGTP黑白名单开关配置SET GTPBLKWHTSWITCHSHOW GTPBLKWHTSWITCHGTP白名单配置ADD GTPWHITELISTDEL GTPWHITELISTSHOW GTPWHITELISTGTP黑名单配置ADD GTPBLACKLISTDEL GTPBLACKLISTSHOW GTPBLACKLISTGTP消息类型配置ADD GTPMSGTYPELISTDEL GTPMSGTYPELISTSET GTPMSGTYPELISTSHOW GTPMSGTYPELIST 
动态管理命令使用说明SHOW GTPSECCHECKSTATAMF支持对GTP消息的安全检查，对不符合安全检查的消息进行丢弃。该命令用于查询GTP消息过滤统计。DEL GTPSECCHECKSTATAMF支持对GTP消息的安全检查，对不符合安全检查的消息进行丢弃。该命令用于清空GTP消息过滤统计。 
性能统计 : 
该特性不涉及计数器的变化。
告警和通知 : 
告警和通知
---
3305242928 消息安全检查未通过
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
在网元间相互访问时，通常需要对接收消息执行安全检查。AMF需要针对GTP接口的安全威胁，进行必要的安全防范，从而提升整个网元的安全性。本配置涉及N26口GTP消息的黑白名单过滤功能。 
配置前提 : 
AMF运行正常。 
EM（AMF网元）环境能正常连接。 
配置过程 : 
执行[SET GTPSECCHKSWITCH] 命令，设置GTP安全检查开关 ，选择是否要进行GTP安全检查。
执行[SET GTPBLKWHTSWITCH]命令，设置当前安全检查消息的过滤类型，选择按照黑名单或白名单进行GTP消息过滤。
执行[ADD GTPWHITELIST]  / [ADD GTPBLACKLIST] 命令，添加需要过滤的GTP消息类型和地址段。
执行[ADD GTPMSGTYPELIST]命令按照“消息标识号”设置不同区段的消息类型，用于与IP地址段（步骤3）相互关联。
配置实例 : 
场景说明 : 
场景一：AMF采用黑名单方式的安全检查策略。 
场景二：AMF采用白名单方式的安全检查策略。 
数据规划 : 
类别|配置项|参数名称|取值
---|---|---|---
场景一|GTP安全检查开关配置|安全检查开关|开（默认为关闭，使用时需手动开启）
GTP黑白名单开关配置|场景一|名单检查开关|黑名单
GTP黑名单配置|场景一|规则索引、IP地址类型、起始IP地址、结束IP地址、消息标识号1、消息标识号2、消息标识号3、消息标识号4|未配置，需根据需要进行添加
GTP消息类型配置|场景一|消息标识号、起始消息类型、结束消息类型|未配置，需根据需要进行添加（默认全0，表示无效值）
场景二|GTP安全检查开关配置|安全检查开关|开（默认为关闭，使用时需手动开启）
GTP黑白名单开关配置|场景二|名单检查开关|白名单
GTP白名单配置|场景二|规则索引、IP地址类型、起始IP地址、结束IP地址、消息标识号1、消息标识号2、消息标识号3、消息标识号4|未配置，需根据需要进行添加
GTP消息类型配置|场景二|消息标识号、起始消息类型、结束消息类型|未配置，需根据需要进行添加（默认全0，无效值）
配置步骤 : 
场景一的配置步骤如下： 
步骤|说明|命令
---|---|---
1|开启GTP安全检查开关。|SET GTPSECCHKSWITCH:CHECKSWITCH="ON"
2|设置当前GTP黑白名单开关为黑名单。|SET GTPBLKWHTSWITCH:WHITEORBLACK="BLACK"
3|设置“消息标识号1”的起始与结束消息类型为 1~132。设置“消息标识号2”的起始与结束消息类型为 133~140。|ADD GTPMSGTYPELIST:INDEXID=1,MSGTYPESTART=1,MSGTYPEEND=132ADD GTPMSGTYPELIST:INDEXID=2,MSGTYPESTART=133,MSGTYPEEND=140
4|设置黑名单IP地址段（192.168.1.1~192.168.255.1），并与消息标识号（步骤3中配置）相关联。|ADD GTPBLACKLIST:RULEINDEX=1,IPTYPE="IPV4",IPADDRSTART="192.168.1.1",IPADDREND="192.168.255.1",MSGINDEXID1=1,MSGINDEXID2=2,MSGINDEXID3=0,MSGINDEXID4=0
场景二的配置步骤如下： 
步骤|说明|命令
---|---|---
1|开启GTP安全检查开关。|SET GTPSECCHKSWITCH:CHECKSWITCH="ON"
2|设置当前GTP黑白名单开关为白名单。|SET GTPBLKWHTSWITCH:WHITEORBLACK="WHITE"
3|设置“消息标识号1”的起始与结束消息类型为 1~132。设置“消息标识号2”的起始与结束消息类型为 133~140。|ADD GTPMSGTYPELIST:INDEXID=1,MSGTYPESTART=1,MSGTYPEEND=132ADD GTPMSGTYPELIST:INDEXID=2,MSGTYPESTART=133,MSGTYPEEND=140
4|设置黑名单IP地址段（192.168.1.1~192.168.255.1），并与消息标识号（步骤3中配置）相关联。|ADD GTPWHITELIST:RULEINDEX=1,IPTYPE="IPV4",IPADDRSTART="192.168.1.1",IPADDREND="192.168.255.1",MSGINDEXID1=1,MSGINDEXID2=2,MSGINDEXID3=0,MSGINDEXID4=0
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|GTP黑名单消息过滤
---|---
测试目的|AMF收到的GTP消息在黑名单配置中，查看该消息是否被丢弃。
预置条件|开启GTP安全检查开关。设置当前GTP黑白名单开关为黑名单。配置当前GTP过滤黑名单的消息类型以及源地址（地址类型IPv4 ，IP地址段为192.168.1.1~192.168.10.1，消息类型范围为133~140）。AMF收到GTP消息（例如，在4G切换5G的流程中，AMF收到来自MME的Forward Relocation Request消息）。
测试过程|AMF收到来自MME的Forward Relocation Request 消息，检测到发送该消息的地址为192.168.1.2 ，消息类型Forward Relocation Request（133），处于黑名单内。
通过准则|AMF直接丢弃该消息，并在相关告警和性能统计中记录本次过滤结果。
测试结果|-
测试项目|GTP白名单消息过滤
---|---
测试目的|AMF收到的GTP消息在白名单配置中，查看该消息是否被正常处理。
预置条件|开启GTP安全检查开关。设置当前GTP黑白名单开关为白名单。配置当前GTP过滤白名单的消息类型以及源地址（地址类型IPv4，IP地址段为192.168.1.1~192.168.10.1 ，消息类型范围为133~140）AMF收到GTP消息（例如，在4G切换5G的流程中，AMF收到来自MME的Forward Relocation Request消息）。
测试过程|AMF收到来自MME的Forward Relocation Request 消息，检测到发送该消息的地址为192.168.1.2 ，消息类型Forward Relocation Request（133），处于白名单内。
通过准则|该消息处于白名单内，AMF正常处理消息，触发4G到5G的切换流程，无相关告警和性能统计。
测试结果|-
常见问题处理 : 
无 
# 缩略语 
# 缩略语 
5GC : 
5G Core Network5G核心网
AMF : 
Access and Mobility Management Function接入和移动管理功能
AUSF : 
Authentication Server Function鉴权服务器功能
## LMF 
Location Management Function定位管理功能
NF : 
Network Function网络功能
NRF : 
NF Repository Function网络功能仓储
PCF : 
Policy Control Function策略控制功能
## SBI 
Service Based Interface基于服务的接口
SMF : 
Session Management Function会话管理功能
UDM : 
Unified Data Management统一数据管理
URI : 
Uniform Resource Identifier统一资源标识符
ZTE : 
Zhongxing Telecommunications Equipment中兴通讯
