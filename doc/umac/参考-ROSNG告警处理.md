# 告警条目说明 
概述 :文档从多个方面对告警条目进行了描述，下面分别介绍每个告警条目的含义。 
## 告警码 
告警码就是系统对告警条目的统一编号，是个十进制的正整数，全局唯一，方便用户检索。 
本文将告警码作为小节标题，方便检索。 
## 告警ID 
也称为告警流水号，有告警产生或者通知上报都会递增，对于告警恢复不会递增，告警恢复的流水号是对应的告警产生的流水号。 
流水号从1开始，范围是：1 ~ 232-1，到达最大值时会翻转为1。
## 告警原型 
告警原型给出了此告警的模板。告警原型包括了Comment和DisplayResult两部分： 
Comment： 该告警的标题，是告警的概貌。 
DisplayResult：该告警细化的原型描述。其中变化的内容，通过告警参数体现。每个告警根据其特性，告警参数的个数：0~N。 
告警样例 :告警样例部分给出此告警的实例，就是设备上告警发生时的显示信息，以命令[show logging alarm]查看到的样式为准。
对于可恢复的告警：告警样例分为“告警产生”和“告警恢复”两小部分。 
告警描述 :告警描述是对设备告警语言的通俗解释，告诉读者告警原型中的信息具体表达了什么含义。 
## 告警级别 
默认级别指明了本条告警的默认告警级别是多少。 
对于ZXR10设备来说，告警级别分为八个级别，其中第一级告警最严重，第八级告警最轻微，参见[表1]。
告警级别|重要程度|说明
---|---|---
1|EMERGENCIES（严重告警）|可能会导致系统与业务崩溃的告警，需要立即采取相应措施
2|ALERTS（重大告警）|系统出现重大故障，可能影响业务正常运行，需要立即采取相应措施
3|CRITICAL（紧急告警）|出现紧急情况，需要尽快处理
4|ERRORS（错误告警）|出现错误，在适当的时间进行处理
5|WARNINGS（警告告警）|系统提示一些需要警告的情况，以引起用户注意，需要进一步观察
6|NOTIFICATIONS（通告信息）|系统认为应该通告到各部分并记录的普通但很重要的事件信息
7|INFORMATIONAL（报告信息）|一般性通知信息
8|DEBUGGING（调试信息）|对管理员为调试系统或网络而输入命令的响应信息类别
一般而言，1-5级属于告警，6-8级归为通知。 
告警级别分为默认告警级别和实际告警级别： 
默认告警级别：每条告警的原始分配的级别，是固定不变的，用户不能更改。 
实际告警级别：设备运行过程中被实际使用的告警级别。用户可以通过命令alarm level-change <alarm-code><level>来具体修改一条告警的实际告警级别，所有默认级别的告警都可以修改。 
告警类别 :目前的告警类别分为两类，参见下表。 
告警类别|说明
---|---
普通告警|告警级别1~5，大部分都有告警恢复
通知|告警级别6~8，没有告警恢复
告警恢复 :告警恢复就是由故障状态恢复到正常状态时，上报的一条带有“Clear”状态的告警消息。与告警恢复对应，告警产生是在正常状态下，发生故障时上报的告警消息。告警恢复必然与某个告警产生对应。 
本文中用“是”或“否”来表明本条告警是否可恢复： 
是：告警可恢复 
否：告警不可恢复 
不是所有的告警都有告警恢复： 
大部分“普通告警”都有告警恢复 
“性能告警”一般都有告警恢复 
“通知”一般没有告警恢复 
对于不可恢复的告警，可以通过命令[alarm-confirm ]<flow-id>手动恢复告警，其中参数<flow-id>表示告警流水号，可以通过TRAP、[show logging alarm]打印到终端的告警信息中查到。
告警类型 :按照告警的性质进行划分，告警信息分为以下五种： 
通信告警（CommunicationAlarm）：此类告警与从某一点向另一点运送信息所需要的规程和(或)进程相关。 
处理错误告警（ProcessingErrorAlarm）：此类告警与软件或处理故障相关，包括内存溢出、版本不匹配、程序异常中止等产生的告警。 
质量服务告警（QoSAlarm）：此类告警与服务质量相关，包括网络拥塞、系统资源占用率高、带宽抖动或变小等产生的告警。 
设备告警（EquipmentAlarm）：此类告警与设备故障相关，包括各个设备部件、接口等产生的告警。 
环境告警（EnvironmentalAlarm）：此类告警与设备所处的环境条件相关，包括所处环境的温度、湿度、通风情况有异常时产生的告警。 
引起原因 :引起原因是指可能产生告警的各种原因。给出告警原因的目的是希望通过了解告警的触发条件、触发频率等信息，从而及时获得排除故障的解决方法和预防措施。 
产生的影响 :系统影响告诉读者本告警可能对系统或运行的业务所造成的影响和后果。 
处理建议 :处理建议有针对性地给出读者能够排除该告警的建议和操作。 
# 告警信息格式说明 
ZXR10系统中告警信息的一般格式如下： 
<type><code> ID <flow-id> level <level>{occurred | cleared} at <time> sent by <position> %<module>% <description>
[表1]中对告警信息中的各个域进行了说明。
参数|描述
---|---
<type>|消息类型“An alarm”表示是告警；“A notification”表示是通知
<code>|告警码
<flow-id>|告警流水号
<level>|告警级别
occurred | cleared|告警状态：occurred表示告警发生；cleared表示告警恢复
<time>|告警发生的时间
<position>|告警发生的单板位置
<module>|告警所属的模块名称
<description>|告警信息描述，包括告警名称（comment）和告警原型描述（ DisplayResult）
 说明： 
告警状态为“cleared”表明：告警恢复，不需采取任何操作。 
# ACL 
## 150202 
告警描述 :ACL聚合号池资源耗尽。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment: ACL polymerized number is invalid  
DisplayResult: The ACL polymerized number for ('$1', '$2') is invalid` 
参数说明 :$1：业务类型（"NETFLOW","IPFLOW","PORT-ACL","HQOS"等） 
$2：业务的详细情况 
告警样例 :`A notification 150202 ID 26 level 6 occurred at 00:00:00 01-01-2000 sent by 
ZXR10 PFU-0/20/0 %ACL%ACL polymerized number for is invalid.  The ACL polymerized 
number for ('IPFLOW', 'ifname=gei-0/1/0/3, ACLName=test') is invalid` 
引起原因 :在接口绑定ACL，为该ACL分配聚合号的聚合号池已耗尽。 
在接口对某类报文（ipv4/ipv6，input/output）应用ACL，对符合ACL规则的报文进行采样。如果配置的采样接口过多，导致ACL分配聚合号的聚合号池耗尽。 
产生的影响 :最近一次在接口上绑定ACL的配置没有正常启用；同时，如果再对该接口绑定新的ACL，新的ACL也不能生效。 
处理建议 :使用命令[show ipv4-access-lists config]（[show ipv6-access-lists config]或[show link-access-lists
config]或[show ipv4-mixed-access-lists config]或[show ipv6-mixed-access-lists config]）或[show ip flow interface ]<name>查看当前版本的ACL个数的性能参数值，确认已绑定的不同ACL个数是否超过性能参数值。
Y→步骤2 
N→步骤3 
使用命令[show ipv4-access-group]（[show
ipv6-access-group]或[show link-access-group]或[show ipv4-mixed-access-group]或[show ipv6-mixed-access-group]）查看接口绑定配置，根据配置信息及操作过程确定超出性能参数值时的配置条目，进行删除。使用上述命令查看是否正常删除。
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 150204 
告警描述 :ACL配置过多未生效。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:ACL does not take effect.
DisplayResult:ACL for ('$1','$2') has too many rules configured.` 
参数说明 :$1：ACL业务类型 
$2：ACL类型 
告警样例 :`A notification 150204 ID 24 level 6 occurred at 23:49:35 01-24-2019 sent by 
ZXR10 PFU-0/1/0 %ACL% ACL does not take effect.  ACL for ('HQOS','ALL_ACL,
class-map:cmap1') has too many rules configured.` 
引起原因 :ACL配置了太多规则，导致ACL业务没有生效，触发此告警。 
产生的影响 :当前配置的ACL没有生效。 
处理建议 :删除ACL中过多配置的规则，使数目和系统容量指标相匹配，查看告警是否恢复。 
Y→结束 
N→步骤2 
请联系中兴通讯技术支持工程师。 
# ARP 
## 50401 
告警描述 :某个动态ARP条目的MAC地址被改变。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:The MAC of the dynamic ARP item changed.
DisplayResult:(Old MAC = $1, new MAC = $2, IP = $3, interface = $4).` 
参数说明 :$1：旧的MAC地址 
$2：新的MAC地址 
$3：IP of this ARP item 
$4：接口名称 
告警样例 :`A notification 50401 ID 1 level 6 occurred at 11:06:27 02-27-2010 sent by PFU-0/1/0
%ARP% The MAC of the dynamic arp item changed.  (old MAC = 00D0.DF22.0206, new 
MAC = 00D0.DF22.0205, IP = 2.3.4.6, interface = gei_0/1/0/1)` 
引起原因 :正在使用的动态ARP条目的MAC地址被ARP报文更新。 
IP地址配置冲突。 
产生的影响 :可能由于ARP攻击而更改正常ARP条目的MAC，导致数据报文被错误地发送到攻击者指定的MAC对应的主机。 
处理建议 :使用[show arp]<ip-address>命令查看更新后的ARP条目，检查新的MAC地址是否正确。
Y→步骤5 
N→步骤2 
进入ARP配置模式，在同一个接口上配置具有相同IP和正确MAC的静态ARP条目，根据[show arp]<ip-address>命令或命令提示检查是否配置成功。
Y→步骤5 
N→步骤3 
检查是否是IP地址配置错误或IP地址配置冲突。 
Y→步骤4 
N→步骤5 
配置正确的IP地址，检查告警是否恢复。 
Y→结束 
N→步骤5 
排除ARP攻击源，检查告警是否恢复。 
Y→结束 
N→步骤6 
请联系中兴通讯技术支持工程师。 
## 50402 
告警描述 :动态ARP条目的学习过程受到ARP的接口保护功能限制。
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:ARP entries on the interface reached threshold. 
DisplayResult:$5 the num(num=$1) of interface(index=$2, name=$3) 
protect$4, current_num=$7.` 
参数说明 :$1：接口ARP保护阈值 
$2：接口索引 
$3：接口名 
$4：(1、discard IP(IP=丢弃报文的源IP地址) ；2、警恢复时，参数为空) 
$5：(1、Overflow ；2、Recover) 
$7：接口ARP保护当前值 
告警样例 :告警产生： 
`An alarm 50402 ID 1 level 4 occurred at 10:57:05 02-27-2010 sent by MPU-0/26/0
%ARP% ARP entries on the interface reached threshold.  Overflow the num(num=2) 
of interface(index=6, name=supervlan5) protect, discard IP(IP=2.3.4.6), current_num=2.` 
告警恢复： 
`An alarm 50402 ID 1 level 4 cleared at 10:57:52 02-27-2010 sent by MPU-0/26/0
%ARP% ARP entries on the interface reached threshold.  Recover the num(num=2) 
of interface(index=6, name=supervlan5) protect, discard IP(IP=2.3.4.6), current_num=1.` 
引起原因 :某个接口上ARP条目数目达到设定的ARP保护阈值。 
产生的影响 :该接口上无法再学习更多动态ARP条目。 
处理建议 :使用[show running-config arp]命令，查看接口上是否配置了[protect]命令。
Y→步骤2 
N→步骤3 
根据实际情况，删除[protect]命令，或者进入ARP配置模式，通过[protect interface]命令，按提示将接口保护阈值配置成较大值，使用[show running-config
arp]命令查看配置是否生效。
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 50403 
告警描述 :动态ARP条目的学习过程受到ARP的MAC保护功能限制。
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:ARP entries on the MAC reached threshold.
DisplayResult:$3 the num(num=$4) of MAC(MAC=$1) protect$2, current_num=$6.` 
参数说明 :$1：MAC地址 
$2：(1、discard IP(IP=丢弃报文的源IP地址) ；2、警恢复时，参数为空) 
$3：(1、Overflow ;2、Recover) 
$4：MAC保护阈值 
$6：MAC保护当前值 
告警样例 :告警产生： 
`An alarm 50403 ID 1 level 4 occurred at 10:56:19 02-27-2010 sent by PFU-0/1/0
%ARP% ARP entries on the MAC reached threshold. Overflow the num(num=2) of 
MAC(MAC=00D0.DF22.2783) protect, discard IP(IP=192.168.88.88), current_num=2.` 
告警恢复： 
`An alarm 50403 ID 1 level 4 cleared at 10:55:52 02-27-2010 sent by PFU-0/1/0
%ARP% ARP entries on the MAC reached threshold. Recover the num(num=1) of 
MAC(MAC=00D0.DF22.2783) protect, discard IP(IP=192.168.88.88), current_num=1.` 
引起原因 :具有某个MAC地址的ARP条目数目达到设定的ARP保护阈值。 
产生的影响 :无法再学习更多具有该MAC地址的动态ARP条目。 
处理建议 :使用[show running-config arp]命令，查看是否配置了MAC保护命令。
Y→步骤2 
N→步骤6 
检查告警信息指定的保护阈值是否与配置的特定MAC保护阈值相同。 
Y→步骤3 
N→步骤4 
进入ARP配置模式，使用[protect special-mac]命令，按提示将该MAC地址的MAC保护阈值增大，检查告警是否恢复。
Y→结束 
N→步骤4 
检查告警信息指定的保护阈值，是否大于等于用户配置的普通MAC保护阈值。 
Y→步骤5 
N→步骤6 
进入ARP配置模式，使用[protect common-mac]命令，按提示将普通MAC保护阈值增大，检查告警是否恢复。
Y→结束 
N→步骤6 
请联系中兴通讯技术支持工程师。 
## 50404 
告警描述 :动态ARP条目的学习过程受到ARP的全局保护功能限制。
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:ARP entries reached threshold.
DisplayResult:$3 the num(num_g=$1) of whole protect$2, current_num=$5.` 
参数说明 :$1：全局保护阈值 
$2：(1、discard IP(IP=丢弃报文的源IP地址)； 2、警恢复时，参数为空) 
$3：(1、Overflow; 2、Recover) 
$5：全局保护当前值 
告警样例 :告警产生： 
`An alarm 50404 ID 1 level 4 occurred at 11:16:12 02-27-2010 sent by MPU-0/26/0
%ARP% ARP entries reached threshold. Overflow the num(num_g=12) of whole protect, 
discard IP(IP=2.3.4.6)` 
告警恢复： 
`An alarm 50404 ID 1 level 4 cleared at 11:16:28 02-27-2010 sent by MPU-0/26/0
%ARP% ARP entries reached threshold.  Recover the num(num_g=12) of whole protect` 
引起原因 :全局ARP条目总数达到设定的ARP保护阈值。 
产生的影响 :无法再学习更多的动态ARP条目。 
处理建议 :使用[show running-config arp]命令，查看是否配置了[protect whole]命令：
Y→步骤2 
N→步骤3 
根据实际情况，删除[protect whole]命令，或者进入ARP配置模式，使用[protect whole]命令，按提示将全局保护阈值增大，再使用[show running-config
arp]命令查看配置是否生效：
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 50405 
告警描述 :接收的ARP报文源MAC地址与本地接口的MAC地址冲突。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:MAC of received packet conflict with local's.
DisplayResult:MAC(MAC=$1, intf_index=$2, intf_name=$3, vlan=$4) of 
received packet conflict with local's.` 
参数说明 :$1：ARP报文的源MAC 
$2：接口索引 
$3：接口名 
$4：VLAN ID 
告警样例 :`A notification 50405 level 6 occurred at 17:39:34 10-28-2009 sent by MPU-0-20-3
%ARP% MAC of received packet conflict with local's.  MAC(MAC=00d0.d001.0203, 
intf_index=2, intf_name=gei-0/1/0/1, vlan=1) of received packet conflict with local's` 
引起原因 :接收的ARP报文源MAC地址与本地接口的MAC地址相同。 
产生的影响 :该ARP报文被丢弃，无法学习ARP条目。 
处理建议 :使用[show interface]命令查看本地接口的MAC地址是否与接收到的ARP报文源MAC一致。
Y→步骤2 
N→步骤3 
进入接口配置模式，在本地接口上配置MAC地址偏移，使用[show running-config-interface]命令查看配置是否生效。
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 50406 
告警描述 :接收的ARP报文源IP地址与本接口的IP地址冲突。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment: IP of received packet conflict with local's! 
DisplayResult: IP(IP=$1, intf_index=$2, intf_name=$3) of received packet conflict with 
local's` 
参数说明 :$1：ARP报文的源IP 
$2：接口索引 
$3：接口名 
告警样例 :`A notification 50406 ID 1 level 6 occurred at 11:03:19 02-27-2010 sent by PFU-0/1/0
%ARP% IP of received packet conflict with local's!  IP(IP=192.168.88.200, intf_index=2, 
intf_name=gei-0/1/0/1) of received packet conflict with local's` 
引起原因 :接收的ARP源IP地址与本接口的IP地址相同。 
产生的影响 :该ARP报文被丢弃，无法学习ARP条目。 
处理建议 :使用[show interface]命令查看本地接口的某个IP地址，是否与接收到的ARP报文源IP一致。
Y→步骤2 
N→步骤3 
进入接口配置模式，重新配置一个无冲突的IP地址，使用[show running-config-interface]命令查看配置是否生效。
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 50408 
告警描述 :接收的ARP报文源IP地址不在SuperVLAN的IP POOL范围内。 
默认级别 :7 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment: IP of received packet is not in IP POOL 
DisplayResult: IP(IP=$1) of received packet is not in IP POOL(supervlanIntf=$2, 
subvlan={ $3 , $4 , $5 }, subifindex=$6)` 
参数说明 :$1：ARP报文的源IP 
$2：SuperVLAN接口名 
$3：SubVLAN封装的外层VLAN ID 
$4：SubVLAN封装的内层VLAN ID 
$5：SubVLAN封装的第三层VLAN
ID（目前支持两层VLAN ID，该字段保留） 
$6：SubVLAN的索引 
告警样例 :`A notification 50408 ID 1 level 7 occurred at 12:00:42 02-27-2010 sent by PFU-0/1/0
%ARP% IP of received packet is not in IP POOL!  IP(IP=2.3.4.6) of received packet is 
not in IP POOL(supervlanIntf=supervlan5, subvlan={ 3 , 0 , 0 }, subifindex=7)` 
引起原因 :SuperVLAN接口启用了IP POOL过滤功能，如果收到的ARP报文源地址不在相应的IP POOL段，会丢弃该报文。 
SuperVLAN中的终端配置错误IP地址。 
产生的影响 :该ARP报文被丢弃，无法学习ARP条目。 
处理建议 :使用[show running-config supervlan]命令查看SuperVLAN是否配置了IP
POOL过滤开关。
Y→步骤2 
N→步骤3 
进入SuperVLAN配置模式，将产生告警的报文源IP地址加入到对应SubVLAN的IP POOL中，检查告警是否恢复。 
Y→结束 
N→步骤3 
检查在SubVLAN中的终端是否配置了错误的IP地址。 
Y→步骤4 
N→步骤5 
确保终端配置的IP地址和掩码正确，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 50411 
告警描述 :本地网关接口配置的IP地址与网络某设备冲突。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment: Gateway ip invalid! 
DisplayResult: IP(IP=$1) of the gateway(intf_index=$2, intf_name=$3) detected confict 
in the network` 
参数说明 :$1：网关IP地址 
$2：接口索引 
$3：接口名 
告警样例 :`A notification 50411 ID 1 level 6 occurred at 17:24:40 05-10-2010 sent by ZXR10 MPU-0/26/0
%ARP% Gateway ip invalid!  IP(IP=192.168.88.200) of the gateway(intf_index=2, 
intf_name=gei-0/1/0/1) detected confict in the network` 
引起原因 :ARP模块发送免费ARP报文，探测到网关接口配置的IP地址与网络某设备相同。 
端口下存在环路。 
产生的影响 :该网关IP地址设置无效。 
处理建议 :检查网络环境，查看网络内是否存在配置相同IP地址的主机。 
Y→步骤2 
N→步骤3 
修改网关接口或对方主机的IP地址，避免网络中出现IP地址冲突，检查告警是否恢复。 
Y→结束 
N→步骤3 
查看端口下是否存在环路。 
Y→步骤4 
N→步骤5 
排除环路，检查故障是否清除。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 50412 
告警描述 :源地址过滤丢弃ARP报文。
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface source filter protect.
DisplayResult:The source filter alarm threshold($3 packet(s) per 10 seconds) of 
interface (intf_index=$1, intf_name=$2), current_value=$4.` 
参数说明 :$1：接口索引值 
$2：接口名字 
$3：ARP源地址过滤的告警阈值 
$4：ARP源地址过滤的当前值 
告警样例 :告警产生： 
`An alarm 50412 ID 1 level 4 occurred at 11:16:12 02-27-2010 sent by PFU-0/1/0
%ARP% Interface source filter protect.  overflow the source filter alarm threshold
(100 packets per 10 second) of interface (intf_index=2, intf_name=gei-0/1/0/1), current_value=110` 
告警恢复： 
`An alarm 50412 ID 1 level 4 occurred at 11:16:28 02-27-2010 sent by PFU-0/1/0
%ARP% Interface source filter protect.  recover the source filter alarm threshold
(100 packets per 10 second) of interface (intf_index=2, intf_name=fei-0/1/0/1), current_value=90` 
引起原因 :源地址过滤丢弃ARP报文。 
产生的影响 :ARP报文丢弃。 
学习不到ARP条目。 
处理建议 :执行命令[show ip forwording route ]<IP>查看丢弃的ARP报文的源IP的路由，是否有路由。
Y→步骤2 
N→步骤3 
路由中对应的接口是否是ARP报文的收包接口。 
Y→步骤5 
N→步骤3 
默认不进行ARP学习，是否仍想学习到这个IP对应的ARP。 
Y→步骤4 
N→步骤5 
为该接口添加一段包括源IP地址在内的路由，检查告警是否清除。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 50413 
告警描述 :学习限制丢弃ARP应答报文。
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface learn limit protect.
DisplayResult:The learn limit alarm threshold($3 packet(s) per 10 seconds) of 
interface (intf_index=$1, intf_name=$2), current_value=$4.` 
参数说明 :$1：接口索引值 
$2：接口名字 
$3：ARP学习限制过滤的告警阈值 
$4：ARP学习限制过滤的当前值 
告警样例 :告警产生： 
`An alarm 50413 ID 1 level 4 occurred at 11:16:12 02-27-2010 sent by PFU-0/1/0
%ARP% Interface learn limit protect. overflow the learn limit alarm threshold
(100 packets per 10 second) of interface (intf_index=2, intf_name=gei-0/1/0/1), 
current_value=110` 
告警恢复： 
`An alarm 50413 ID 1 level 4 occurred at 11:16:28 02-27-2010 sent by PFU-0/1/0
%ARP% Interface learn limit protect.  recover the learn limit alarm threshold
(100 packets per 10 second) of interface (intf_index=2, intf_name=gei-0/1/0/1), 
current_value=95` 
引起原因 :学习限制丢弃ARP应答报文。 
产生的影响 :ARP报文丢弃。 
学习不到ARP条目。 
处理建议 :执行命令[show running-config arp]查看ARP学习限制功能是否开启。
Y→步骤2 
N→步骤4 
确认是否需要开启ARP学习限制功能。 
Y→结束 
N→步骤3 
关闭ARP学习限制功能。完成后，检查告警是否清除。 
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 50414 
告警描述 :限速丢弃ARP报文。
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface speed limit protect.
DisplayResult:The speed limit($3 packet(s) per second) of interface
(intf_ip=$4, intf_index=$1, intf_name=$2), current_value=$5.` 
参数说明 :$1：接口索引值 
$2：接口名字 
$3：ARP限速过滤的阈值 
$4：接口IP地址 
$5：ARP限速过滤的当前值 
告警样例 :告警产生： 
`An alarm 50414 ID 1 level 4 occurred at 11:16:12 02-27-2010 sent by PFU-0/1/0
%ARP% Interface speed limit protect.  overflow the speed limit(100 packets per second) 
of interface (intf_index=2, intf_name=gei-0/1/0/1), current_value=110` 
告警恢复： 
`An alarm 50414 ID 1 level 4 occurred at 11:16:28 02-27-2010 sent by PFU-0/1/0
%ARP% Interface speed limit protect.  recover the speed limit(100 packets per second) 
of interface (intf_index=2, intf_name=gei-0/1/0/1), current_value=95` 
引起原因 :限速丢弃ARP报文。 
产生的影响 :ARP报文丢弃。 
学习不到ARP条目。 
处理建议 :执行命令[show running-config arp]查看ARP速率限制功能是否开启。
Y→步骤2 
N→步骤3 
执行命令[debug arp packet interface ]<收包接口>查看收到的ARP报文的速率是否达到设置的限速阈值。
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 50416 
告警描述 :ARP热备配置校验结果。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:ARP hotback config.
DisplayResult:$1. (ICBG = $2, peer interface = $3, local interface = $4).` 
参数说明 :$1：配置状态 （success 或 fail） 
$2：备份组名 
$3：对端接口名 
$4：本端接口名 
告警样例 :`A notification 50416 ID 1 level 6 occurred at 17:24:40 03-10-2013 sent by MPU-0/26/0 
%ARP%ARP hotback config. Success.
(ICBG = bvi23, peer interface = gei-0/1/0/2, local interface = gei-0/1/0/2)` 
引起原因 :在同一个备份组的ARP热备接口中，影响热备ARP条目有效性的两种关键属性存在不一致：IPv4子网不一致、VLAN配置不一致。 
产生的影响 :备设备上通过热备得到的ARP条目不可用，业务可能断流。 
处理建议 :在主备设备上都执行[show icbg bvi23]命令，确认两个接口是否绑定在该备份组上。
Y→步骤3 
N→步骤2 
执行[icbg]命令重新正确设置备份组所应绑定的接口。完成后，检查告警是否清除。
Y→结束 
N→步骤3 
在主备设备上都执行[show ip interface]命令，查看两个接口的IPv4主地址是否在同一个子网上。
Y→步骤5 
N→步骤4 
在主备设备的接口上执行[ip address]命令，将两个接口的IPv4主地址修改到同一个子网上。完成后，检查告警是否清除。
Y→结束 
N→步骤5 
在主备设备上执行[show running-confing vlan]命令，确认两个接口的VLAN配置是否一致。
Y→步骤7 
N→步骤6 
将两个接口的VLAN配置修改为一致，检查告警是否清除。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 50417 
告警描述 :ARP条目的出接口发生变化。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:ARP out interface update.
DisplayResult:(Interface name:$4,IP:$3,old out interface name:$1,new out interface name:$2).` 
参数说明 :$1：旧的出接口名 
$2：新的出接口名 
$3：ARP条目的下一条IP 
$4：三层接口名 
告警样例 :`A notification 50417 ID 3 level 6 occurred at 18:13:13 04-06-2016 sent by ZXR10 MPU-0/26/0
%ARP% ARP out interface update. interface name:supervlan1,IP:1.1.1.1,old out 
interface name:gei-0/1/0/1,new out interface name:gei-0/1/0/2.` 
引起原因 :ARP条目出接口发生变化。 
产生的影响 :无影响。 
处理建议 :提示用户，无需处理。 
# BFD 
## 300501 
告警描述 :BFD会话Down。
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment: SessionInfo ：
DisplayResult: $1` 
参数说明 :$1：BFD会话相关信息，主要包括会话的概要信息、会话是创建还是Down或Up 
告警样例 :告警产生： 
创建的会话没有Up：An alarm 300501 ID 36 level 5 occurred at 12:01:25 05-27-2013 sent by ZXR10 MPU-0/26/0
%BFD% SessionInfo :  [Session Create But Not Up]Ld:2061/Rd:0,Protocol:INSTANCE ,
multiHop,VpnId:0,Local/Peer:192.0.1.1/192.0.1.2 
会话Down：An alarm 300501 ID 39 level 5 occurred at 12:09:51 05-27-2013 sent by ZXR10 MPU-0/26/0
%BFD% SessionInfo :  [Session Down For FTM_UP_DOWN]Ld:2061/Rd:3002,Protocol:INSTANCE ,
multiHop,VpnId:0,Local/Peer:192.0.1.1/192.0.1.2 
告警恢复： 
`An alarm 300501 ID 36 level 5 cleared at 12:08:10 05-27-2013 sent by ZXR10 MPU-0/26/0
%BFD% SessionInfo :  [Session Up]Ld:2061/Rd:3002,Protocol:INSTANCE ,multiHop,VpnId:0,
Local/Peer:192.0.1.1/192.0.1.2` 
引起原因 :报文连续转发失败的数量超过用户配置的阈值。 
产生的影响 :导致本会话所检测的链路上发送报文失败。 
处理建议 :查看告警会话类型是否是IP类型。 
Y→步骤2 
N→步骤3 
Ping BFD会话的远端地址是否可以ping通。 
Y→步骤4 
N→步骤6 
执行命令[lsp ping bfd fec/tunnel ID]，查看会话的fec/tunnel
ID是否可以ping通。
Y→步骤4 
N→步骤7 
查看对端是否有相对应的配置。 
Y→步骤10 
N→步骤5 
对端配置相对应的会话，检查告警是否恢复。 
Y→结束 
N→步骤10 
检查端口连线是否正确。 
Y→步骤10 
N→步骤9 
查看LDP邻居，TE隧道，PW邻居是否正确配置。 
Y→步骤10 
N→步骤8 
配置对应的LDP邻居，TE隧道，PW邻居，检查告警是否恢复。 
Y→结束 
N→步骤10 
重新连接好线缆，检查告警是否恢复。 
Y→结束 
N→步骤10 
请联系中兴通讯技术支持工程师。 
## 300505 
告警描述 :BFD会话第一次状态切为UP。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment: BFD session status changed.
DisplayResult: $1` 
参数说明 :$1：BFD会话相关信息，在代码中组织，主要包括会话的概要信息 
告警样例 :`A notification 300505 ID 9 level 6 occurred at 12:38:42 05-09-2014 
sent by ZXR10 MPU-0/26/0
%BFD% BFD session status changed. 
[Session Up]Ld:2049/Rd:2049,Protocol:INSTANCE ,
multiHop,VpnId:0,Local/Peer:10.1.1.1/10.1.1.2` 
引起原因 :BFD会话创建UP后的通知告警。 
产生的影响 :会话正常创建时产生的通知告警，无影响。 
处理建议 :正常运行信息，无需处理。 
# BGP 
## 200215 
告警描述 :从邻居收到的前缀数目超出配置的最大前缀数目。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Error update prefix over:
DisplayResult:No. of prefix received from $1($2) reaches $3, exceed limit $4` 
参数说明 :$1：IP地址 
$2：地址簇描述 
$3：接收的最大数目 
$4：配制可以接收的最大数目 
告警样例 :`A notification 200215 ID 231 level 6 occurred at 01:49:15.901 01-13-2012 sent by 
M6000-N6 MPU-0/21/0%BGP% Error update prefix over: No. of prefix received from 
10.7.7.7(IPv4 Unicast) reaches 7, exceed limit 6` 
引起原因 :从特定邻居收到的前缀数目超出配置接收的最大路由数目。 
产生的影响 :可以只告警而不中断邻居间的连接，并继续接收该邻居发过来的路由前缀。 
告警和中断邻居之间的连接，并在配置的一个时间之后自动建立邻居间的连接。 
告警并维持邻居之间的连接，但是不再接收该邻居发过来的路由。 
处理建议 :执行命令[show running-config bgp]查看是否配置了[maximum-prefix]命令。
Y→步骤2 
N→步骤4 
检查收到的路由数目是否超过了配置的最大前缀数目或者告警门限。 
Y→步骤3 
N→步骤4 
根据实际情况，执行命令[neighbor ]<peergroup-name> maximum-prefix <number>修改配置的最大路由条目数或减少收到的路由数，并reset邻居，检查告警是否恢复。
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 200233 
告警描述 :从邻居收到的前缀数目达到配置的告警门限。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Update prefix threshold MAXPFX:
DisplayResult:No. of prefix received from $1   $2 $3  $4 , max  $5` 
参数说明 :$1：IP地址 
$2：地址簇描述 
$3：接收的最大数目 
$4：配制可以接收的最大数目 
$5：最大数目 
告警样例 :告警产生： 
`An alarm 200233 ID 1 level 5 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/26/0
%BGP% No. of prefix received from 1.1.1.1 reaches 10, max 10` 
告警恢复： 
`An alarm 200233 ID 1 level 5 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/26/0
%BGP% No. of prefix received from 1.1.1.1 recede 10, max 10` 
引起原因 :从邻居收到的前缀数目超出了配置接收的路由告警门限值。 
产生的影响 :无，仅给出告警信息。 
处理建议 :执行命令[show running-config bgp]查看是否配置了[maximum-prefix restart ][drop-routes | warning-only]命令。
Y→步骤2 
N→步骤4 
检查收到的路由数目，是否超过了配置的最大前缀数目或告警门限。 
Y→步骤3 
N→步骤4 
根据实际情况，执行命令[neighbor ]<peergroup-name> maximum-prefix <number>修改配置的最大路由条目数或减少收到的路由数，并reset邻居，检查告警是否恢复。
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 200235 
告警描述 :BGP邻居地址和本地接口地址冲突。
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface collided:
DisplayResult:Neighbor address $1  $2 $3` 
参数说明 :$1:ip地址 
$2:地址簇描述 
$3: 原因描述串 
告警样例 :告警产生： 
`An alarm 200235 ID 464 level 5 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/26/0
%BGP% Neighbor address 1.1.1.1 common can be found in local system & nieghbor is disabled` 
告警恢复： 
`An alarm 200235 ID 464 level 5 occurred at 01：14：45 01-01-2010 sent by ZXR10 MPU-0/26/0
%BGP% Neighbor address 1.1.1.1 common and interface address are  not collide` 
引起原因 :BGP邻居和本地接口配置了相同的IP地址。 
产生的影响 :邻居被禁用。 
处理建议 :查看BGP邻居地址是否和本地接口地址相同。 
Y→步骤2 
N→步骤3 
根据地址规划，修改IP地址，避免IP地址冲突，完成后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200238 
告警描述 :BGP邻居Down。
默认级别 :4 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Neighbor state changed.
DisplayResult: IP= $1 $2 state is $3` 
参数说明 :$1：IP地址 
$2：VRF名称 
$3：状态Down或者Up 
告警样例 :告警产生： 
`An alarm 200238 ID 5 level 4 occurred at 01:23:52 11-17-2013 sent by ZXR10 MPU-0/26/0
%BGP% Neighbor state changed.  IP=20.1.1.2 zte state is DOWN` 
告警恢复： 
`An alarm 200238 ID 5 level 4 cleared at 01:24:11 11-17-2013 sent by ZXR10 MPU-0/26/0
%BGP% Neighbor state changed.  IP=20.1.1.2 zte state is UP` 
引起原因 :BGP的邻居状态发生Down。 
产生的影响 :从该邻居学习的路由被删除，出现流量丢失。 
处理建议 :执行命令[show ip interface brief]查看接口地址，ping邻居地址看是否能ping通。
Y→步骤3 
N→步骤2 
查看是否地址配置有问题，修改接口地址看是否能ping通。 
Y→步骤3 
N→步骤5 
执行命令[show running-config bgp]查看BGP配置是否有问题。
Y→步骤4 
N→步骤5 
修改BGP配置，查看告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
# BOARD 
## 350302 
告警描述 :公用普通密码key不在位。 
默认级别 :3 
告警恢复 :是 
告警类型 :设备告警 
告警类别 :普通告警 
告警描述原型 :`Comment:General public key module offline.
DisplayResult:$1.` 
参数说明 :$1:公用普通密码上报的告警原因 
告警样例 :告警产生： 
`An alarm 350302 ID 17 level 3 occurred at 09:41:56 09-18-2016 sent by ZXR10 MPU-0/3/0
%BOARD% General public key module offline. General public key is offline.` 
告警恢复： 
`An alarm 350302 ID 17 level 3 cleared at 09:42:13 09-18-2016 sent by ZXR10 MPU-0/3/0
%BOARD% General public key module offline. General public key is online.` 
引起原因 :公用普通密码key不在位。 
产生的影响 :密码管理功能不可用。 
处理建议 :检查公用普通密码key是否在板卡上连接正常。 
Y→步骤3 
N→步骤2 
重新连接普通密码key，检查告警是否消失。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 350303 
告警描述 :公用普通密码key状态异常。 
默认级别 :5 
告警恢复 :否 
告警类型 :设备告警 
告警类别 :通知 
告警描述原型 :`Comment:General public key module state error.
DisplayResult:$1.` 
参数说明 :$1：公用普通密码上报的告警原因 
告警样例 :`An notification 350303 ID 17 level 5 occurred at 09:41:56 09-18-2016 sent by ZXR10 MPU-0/3/0
%BOARD% General public key module state error. General public key is error.` 
引起原因 :公用普通密码key状态异常。 
产生的影响 :密码管理功能不可用。 
处理建议 :请联系中兴通讯技术支持工程师。 
# CPS 
## 100401 
告警描述 :物理接口上单位时间内某类报文接收数量超过阈值。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:The upsend packet flow of control plane reached quota limit.
DisplayResult:(Interface = $1, flowtype = $2, current value = $3, quota value = $4).` 
参数说明 :$1：接口名 
$2：flowtype名称 
$3：当前流量统计值 
$4：阈值 
告警样例 :告警产生： 
`An alarm 100401 ID 1 level 5 occurred at 22:09:37 10-23-2010 sent by M6000 PFU-0/0/0
%CPS% The upsend packet flow of control plane reached quota limit. Interface = xgei-0/0/1/1, 
flowtype = igmp-default, current value = 450, quota value = 400` 
告警恢复： 
`An alarm 100401 ID 1 level 5 cleared at 22:09:42 10-23-2010 sent by M6000 PFU-0/0/0
%CPS% The upsend packet flow of control plane reached quota limit. Interface = xgei-0/0/1/1, 
flowtype = igmp-default, current value = 300, quota value = 400` 
引起原因 :可能是受到攻击导致流量异常，也可能是限速阈值配置得太小。 
产生的影响 :接口接收时强制丢弃超过阈值的这种类型的报文。 
处理建议 :检查该类型报文的告警流量是否正常。 
Y→步骤2 
N→步骤3 
限速值和告警阈值太小，可以在安全配置（CPS）模式下，通过接口的限速命令扩大该类型报文的限速值和告警阈值。 
扩大限速值的命令为：flow rate-limit <speed-value> flowtype <flowtype-name> interface <interface-name> 
扩大告警阈值的命令为：flow quota-limit <quota-value> flowtype <flowtype-name> interface <interface-name> 
检查网络，查看是否存在攻击报文。 
Y→步骤4 
N→步骤5 
排除攻击源，检查告警是否清除。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 150501 
告警描述 :设备受到SMURF攻击。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Smurf attack.
DisplayResult:$1.` 
参数说明 :$1:LPP实例单位时间内收到SMURF攻击报文数量 
告警样例 :告警产生： 
`An alarm 150501 ID 36 level 5 occurred at 17:54:35 07-17-2017 sent by rp1 PFU-0/1/0
%CPS% Smurf attack.  Local packet process instance 1 is attacked for received 15 
smurf packets in one second.` 
告警恢复： 
`An alarm 150501 ID 36 level 5 cleared at 17:55:35 07-17-2017 sent by rp1 PFU-0/1/0 
%CPS% Smurf attack.   The rate of the smurf attack is lower than the threshold.` 
引起原因 :设备收到SMURF攻击报文。 
产生的影响 :设备被攻击。 
处理建议 :使用show logging service typeid ip命令，查看告警时间段附近记录的攻击报文信息。 
Y→步骤3 
N→步骤2 
查看记录的业务日志文件（PC版本在/datadisk0/LOG/SERVICE目录中），找到告警时间段附近的攻击报文信息。 
Y→步骤3 
N→步骤4 
则根据记录报文的源地址、源MAC信息确定攻击源，查看告警是否清除。 
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 150502 
告警描述 :设备受到TTL1攻击。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:TTL1 attack.
DisplayResult:$1.` 
参数说明 :$1：LPP实例单位时间内收到TTL1攻击报文数量 
告警样例 :告警产生： 
`An alarm 150502 ID 36 level 5 occurred at 17:54:35 07-17-2017 sent by rp1 PFU-0/1/0 
%CPS% TTL1 attack. Local packet process instance 1 is attacked for received 15 TTL1 
packets in one second.` 
告警恢复： 
`An alarm 150502 ID 36 level 5 cleared at 17:55:35 07-17-2017 sent by rp1 PFU-0/1/0 
%CPS% TTL1 attack. The rate of the TTL1 attack is lower than the threshold.` 
引起原因 :设备收到TTL1攻击报文。 
产生的影响 :设备被攻击。 
处理建议 :使用[show logging service typeid ip]命令，查看告警时间段附近记录的攻击报文信息。
Y→步骤3 
N→步骤2 
查看记录的业务日志文件（PC版本在/datadisk0/LOG/SERVICE目录中），找到告警时间段附近的攻击报文信息。 
Y→步骤3 
N→步骤4 
则根据记录报文的源地址、源MAC信息确定攻击源，查看告警是否清除。 
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
# FRR 
## 200805 
告警描述 :FRR切换。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:FRR switch.
DisplayResult:$1` 
参数说明 :$1：切换信息 
告警样例 :FRR切换： 
`A notification 200805 ID 155 level 6 occurred at 01:41:03 04-10-2013 sent by ZXR10 MPU-0/20/0 
%L3VPN% FRR switch.  Global master nexthop:30.1.1.0 slave nexthop:40.1.1.2 
slave label:16387 status: switch` 
FRR回切： 
`A notification 200805 ID 155 level 6 occurred at 01:41:03 04-10-2013 sent by ZXR10 MPU-0/20/0 
%L3VPN% FRR switch.  Global master nexthop:30.1.1.2 slave nexthop:40.1.1.2 
slave label:16387 status: cutback` 
引起原因 :FRR切换或回切。 
产生的影响 :提示FRR切换回切信息。 
处理建议 :提示用户FRR切换信息，回切信息。 
# IF-PERF 
## 150401 
告警描述 :入向字节带宽利用率超阈值。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Receiving bytes in packets performance.
DisplayResult:The interface("$1") $2 is $3%
(threshold range from $4% to $5% per $7 seconds).` 
参数说明 :$1：接口名 
$2：告警描述,表示端口入向带宽利用率（ingress bindwidth usage） 
$3：带宽占用百分比 
$4：门限类型,共两类：低（low），高（high) 
$5：相应门限类型对应的门限值 
$7：周期 
告警样例 :告警产生： 
`An alarm 150401 ID 373 level 5 occurred at 15:27:20 05-16-2011 sent by U35 MPU-0/26/0
%IF-PERF% Receiving bytes in packets performance  The interface("gei-0/2/0/4") ingress 
bindwidth usage is 7%(threshhold high[6%] per 120 seconds)` 
告警恢复： 
`An alarm 150401 ID 373 level 5 cleared at 15:27:30 05-16-2011 sent by U35 MPU-0/26/0
%IF-PERF% Receiving bytes in packets performance  The interface("gei-0/2/0/4") ingress 
bindwidth usage is 6%(threshhold high[6%] per 120 seconds)` 
引起原因 :接口状态未UP或者已配置shutdown。 
该接口入向流量过大或者过小。 
接口入向带宽利用率设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :执行命令[show intf-statistics threshold ]<interface-name> input-utilization查看接口输入报文的流量门限阈值。执行命令[show
interface ]<interface-name>查看接口当前的输入的带宽利用率是否超过流量门限阈值。
Y→步骤2 
N→步骤3 
调整接口入向带宽流量门限阈值。 
`ZXR10(config)intf-statistics
ZXR10(config-intf-statistics)interface interface_name
ZXR10(config-intf-statistics-if)intf-statistics threshold input-utilization high ** low **` 
调整后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 150402 
告警描述 :出向字节带宽利用率超阈值。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Sending bytes in packets performance.
DisplayResult:The interface("$1") $2 is $3%
(threshold range from $4% to $5% per $7 seconds).` 
参数说明 :$1：接口名 
$2：告警描述，表示端口出向带宽利用率（engress bindwidth usage） 
$3：带宽占用百分比 
$4：门限类型,共两类：低（low），高（high) 
$5：相应门限类型对应的门限值 
$7：周期 
告警样例 :告警产生： 
`An alarm 150402 ID 389 level 5 occurred at 15:41:30 05-16-2011 sent by U35 MPU-0/26/0
%IF-PERF% Sending bytes in packets performance  The interface("gei-0/2/0/9") egress 
bindwidth usage is 38%(threshold high[37%] per 120 seconds)` 
告警恢复： 
`An alarm 150402 ID 389 level 5 cleared at 15:42:10 05-16-2011 sent by U35 MPU-0/26/0
%IF-PERF% Sending bytes in packets performance  The interface("gei-0/2/0/9") egress 
bindwidth usage is 35%(threshold high[37%] per 120 seconds)` 
引起原因 :该接口出向流量过大或者过小。 
接口状态未UP或者已配置shutdown。 
接口出向带宽利用率设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :执行命令[show intf-statistics threshold ]<interface-name> output-utilization查看接口输出报文的流量门限阈值。执行命令[show
interface ]<interface-name>查看接口当前输出的带宽利用率是否超过阈值。
Y→步骤2 
N→步骤3 
调整接口出向带宽流量门限阈值。 
`ZXR10(config)intf-statistics
ZXR10(config-intf-statistics)interface interface_name
ZXR10(config-intf-statistics-if)intf-statistics threshold output-utilization high ** low **` 
调整后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 150403 
告警描述 :收到CRC错误报文超阈值。
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Receiving CRC packets performance.
DisplayResult:The interface("$1") $2 is $3
(threshold range from $4 to $5 per 10 seconds).` 
参数说明 :$1：接口名 
$2：告警描述，表示端口收到的CRC错误报文总数（ingress
FCSError total packet） 
$3：当前计数值 
$4：门限类型（low，high） 
$5：相应门限类型对应的门限值 
告警样例 :告警产生： 
`An alarm 150403 ID 406 level 5 occurred at 15:52:30 05-16-2011 sent by U35 MPU-0/4/0
%IF-PERF% Receiving CRC packets performance  The interface("gei-0/2/0/9") ingress 
FCSError total packet is 15066(threshold high[10000] per  10 seconds)` 
告警恢复： 
`An alarm 150403 ID 406 level 5 cleared at 15:53:15 05-16-2011 sent by U35 MPU-0/4/0
%IF-PERF% Receiving CRC packets performance  The interface("gei-0/2/0/9") ingress 
FCSError total packet is 9864(threshold high[10000] per  10 seconds)` 
引起原因 :链路上CRC错误报文过多。 
接口状态未UP。 
接口CRC错误报文阈值设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :执行命令[show intf-statistics threshold ]<interface-name> input-utilization，查看接口输入CRC错误报文的流量门限阈值。执行命令[show interface ]<interface-name>，查看接口当前CRC错误流量/报文流量是否超过阈值。
Y→步骤2 
N→步骤3 
调整接口入向CRC错误报文流量门限阈值。 
`ZXR10(config)intf-statistics
ZXR10(config-intf-statistics)interface interface_name
ZXR10(config-intf-statistics-if)intf-statistics threshold input-fcserrors high ** low **` 
调整后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 150404 
告警描述 :收到CRC错误报文率超阈值。
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Receiving CRC packets performance.
DisplayResult:The interface("$1") $2 is $3%(threshold range from $4% to $5% per $7 seconds).` 
参数说明 :$1:接口名 
$2:告警描述，表示端口收到的CRC错误报文率(ingress FCSError ratio) 
$3:当前计数值 
$4:门限类型,共两类：低（low），高（high) 
$5:相应门限类型对应的门限值 
$7:周期 
告警样例 :告警产生： 
`An alarm 150404 ID 16 level 5 occurred at 16:00:11 03-14-2011 sent by ZXR10 MPU-0/21/0                                              
%IF-PERF% Receiving CRC packets performance  The interface("gei-0/4/0/2") ingress 
FCSError ratio is 0%(threshold low[20%] per 120 seconds)` 
告警恢复： 
`An alarm 150404 ID 16 level 5 cleared at 16:00:11 03-14-2011 sent by ZXR10 MPU-0/21/0      
%IF-PERF% Receiving CRC packets performance  The interface("gei-0/4/0/2") ingress 
FCSError ratio is 21%(threshold low[20%] per 120 seconds)` 
引起原因 :链路上CRC错误报文过多。 
接口状态未UP。 
接口CRC错误报文率阈值设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :执行命令[show intf-statistics threshold ]<interface-name> input-fcsratio，查看接口CRC错误报文率的流量门限阈值。执行命令[show
interface ]<interface-name>，查看接口当前CRC错误流量/报文流量是否超过阈值。
Y→步骤2 
N→步骤3 
调整接口入向CRC错误报文率门限阈值。 
`ZXR10(config)intf-statistics
ZXR10(config-intf-statistics)interface interface_name
ZXR10(config-intf-statistics-if)intf-statistics threshold input-fcsratio high ** low **` 
调整后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 150405 
告警描述 :入向字节带宽利用率超阈值（在指定的时间段范围内）。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Receiving bytes in packets performance.
DisplayResult:The interface("$1") $2 is $3%(low threshold is $4% per $7 seconds).` 
参数说明 :$1：接口名 
$2：告警描述,表示端口入向带宽利用率（ingress bindwidth usage） 
$3：带宽占用百分比 
$4：门限类型：低（low） 
$7：周期 
告警样例 :告警产生： 
`An alarm 150405 ID 30 level 5 occurred at 01:07:21 03-04-2016 sent by ZXR10 MPU-0/26/0
%IF-PERF% Receiving bytes in packets performance. The interface("gei-0/1/0/1") ingress 
bindwidth usage is 0%(low threshold is 2% per 120 seconds)` 
告警恢复： 
`An alarm 150405 ID 30 level 5 cleared at 03:06:01 03-04-2016 sent by ZXR10 MPU-0/26/0
%IF-PERF% Receiving bytes in packets performance. The interface("gei-0/1/0/1") ingress 
bindwidth usage is 3%(low threshold is 2% per 120 seconds)` 
引起原因 :该接口入向流量过大或者过小 （在指定的时间段范围）。 
接口状态未UP或者已配置shutdown。 
接口入向带宽利用率设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :用[show interface ]<interface_name>检查接口状态是否正常。
Y→步骤2 
N→步骤5 
用[show running-config interface-performance]查看接口下配置的流量门限值。
查看接口当前的输入的带宽利用率是否超过阈值。 
Y→步骤4 
N→步骤5 
调整接口生效时间范围内的入向带宽流量门限阈值，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 150406 
告警描述 :出向字节带宽利用率超阈值（在指定的时间段范围内）。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Sending bytes in packets performance.
DisplayResult:The interface("$1") $2 is $3%(low threshold is $4% per $7 seconds).` 
参数说明 :$1：接口名 
$2：告警描述,表示端口出向带宽利用率（engress bindwidth usage） 
$3：带宽占用百分比 
$4：门限类型：低（low） 
$7：周期 
告警样例 :告警产生： 
`An alarm 150406 ID 30 level 5 occurred at 01:07:21 03-04-2016 sent by ZXR10 MPU-0/26/0
%IF-PERF% Sending bytes in packets performance. The interface("gei-0/1/0/1") engress 
bindwidth usage is 0%(low threshold is 2% per 120 seconds)` 
告警恢复： 
`An alarm 150406 ID 30 level 5 cleared at 03:06:01 03-04-2016 sent by ZXR10 MPU-0/26/0
%IF-PERF% Sending bytes in packets performance. The interface("gei-0/1/0/1") ingress 
bindwidth usage is 3%(low threshold is 2% per 120 seconds)` 
引起原因 :该接口出向流量过大或者过小（在指定的时间段范围）。 
接口状态未UP或者已配置shutdown。 
接口出向带宽利用率设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :用[show interface ]<interface_name>检查接口状态是否正常。
Y→步骤2 
N→步骤5 
用[show running-config interface-performance]查看接口下配置的流量门限值。
查看接口当前的输入的带宽利用率是否超过阈值。 
Y→步骤4 
N→步骤5 
调整接口生效时间范围内的入向带宽流量门限阈值，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 150407 
告警描述 :收到CRC错误报文超阈值(在指定的时间段范围内)。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Receiving CRC packets performance.
DisplayResult:The interface("$1") $2 is $3(low threshold is $4 per $7 seconds).` 
参数说明 :$1:接口名 
$2:告警描述，表示端口收到的CRC错误报文总数(ingress FCSError total packet) 
$3:当前计数值 
$4:门限类型：低(low) 
$7:周期 
告警样例 :告警产生： 
`An alarm 150407 ID 30 level 5 occurred at 01:07:21 03-04-2016 sent by ZXR10 MPU-0/26/0
%IF-PERF% Receiving CRC packets performance. The interface("gei-0/1/0/1") engress 
bindwidth usage is 0%(low threshold is 2% per 120 seconds)` 
告警恢复： 
`An alarm 150407 ID 30 level 5 cleared at 03:06:01 03-04-2016 sent by ZXR10 MPU-0/26/0
%IF-PERF% Receiving CRC packets performance. The interface("gei-0/1/0/1") ingress 
bindwidth usage is 3%(low threshold is 2% per 120 seconds)` 
引起原因 :链路上CRC错误报文过多（在指定的时间段范围）。  
接口状态未UP或者已配置shutdown或接口删除。  
接口CRC错误报文率阈值设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :用[show interface ]<interface_name>检查接口状态是否正常。
Y→步骤2 
N→步骤5 
用[show running-config interface-performance]查看接口下配置的流量门限值。
查看接口当前的输入的带宽利用率是否超过阈值。 
Y→步骤4 
N→步骤5 
调整接口生效时间范围内的入向带宽流量门限阈值，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 150408 
告警描述 :收到CRC错误报文率超阈值(在指定的时间段范围内)。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Receiving CRC packets performance.
DisplayResult:The interface("$1") $2 is $3%(low threshold is $4% per $7 seconds).` 
参数说明 :$1：接口名 
$2：告警描述，表示端口收到的CRC错误报文率(ingress
FCSError ratio) 
$3：当前计数值 
$4：门限类型：低(low) 
$7：周期 
告警样例 :告警产生： 
`An alarm 150408 ID 30 level 5 occurred at 01:07:21 03-04-2016 sent by ZXR10 MPU-0/20/0
%IF-PERF% Receiving CRC packets performance. The interface("fei-0/1/0/1") ingress 
FCSError ratio is 0%(low threshold is 2% per 120 seconds)` 
告警恢复： 
`An alarm 150408 ID 30 level 5 cleared at 03:06:01 03-04-2016 sent by ZXR10 MPU-0/20/0
%IF-PERF% Receiving CRC packets performance. The interface("fei-0/1/0/1") ingress 
FCSError ratio is 3%(low threshold is 2% per 120 seconds)` 
引起原因 :链路上CRC错误报文过多（在指定的时间段范围）。  
接口状态未UP或者已配置shutdown或接口删除。 
接口CRC错误报文率阈值设置与实际情况不符。 
产生的影响 :影响报文收发及报文处理。 
处理建议 :用[show interface ]<interface_name>检查接口状态是否正常。
Y→步骤2 
N→步骤5 
用[show running-config interface-performance]查看接口下配置的流量门限值。
查看接口当前的输入的带宽利用率是否超过阈值。 
Y→步骤4 
N→步骤5 
调整接口生效时间范围内的入向带宽流量门限阈值，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
IP :## 150101 
告警描述 :接口IPv4协议状态Down。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface status.
DisplayResult:The interface(index=$2,name='$1') turned into $3.` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口协议状态 
告警样例 :告警产生： 
`An alarm 150101 ID 16 level 5 occurred at 12:16:24 02-27-2010 sent by ZXR10 MPU-0/26/0
%IP% Interface status  The interface(index=8,name='loopback1') turned into protocol DOWN` 
告警恢复： 
`An alarm 150101 ID 16 level 5 cleared at 12:16:27 02-27-2010 sent by ZXR10 MPU-0/26/0
%IP% Interface status  The interface(index=8,name='loopback1') turned into protocol UP` 
删除接口导致的告警恢复： 
`An alarm 150101 ID 16 level 5 cleared at 12:16:27 02-27-2010 sent by ZXR10 MPU-0/26/0
%IP% Interface status  The interface(index=8,name='loopback1') turned into DELETED` 
引起原因 :对端口进行了shutdown操作。 
端口连线出现异常等，引起端口Down。 
接口被删除。 
产生的影响 :路由等业务无法正常启动和运行。 
处理建议 :执行命令[show running-config-interface]，查看接口上是否配置了[shutdown]命令。
Y→步骤7 
N→步骤2 
执行命令[show interface]，查看接口的物理状态是否up。
Y→步骤4 
N→步骤3 
检查接口模块、物理线路，排除故障后，检查告警是否恢复。 
Y→结束 
N→步骤4 
执行命令[show interface]，查看接口的链路状态是否up。
Y→步骤7 
N→步骤5 
执行命令[show running-config-interface]，查看两端设备的接口的配置是否相匹配。
Y→步骤7 
N→步骤6 
根据实际情况进行配置。完成后，检查告警是否恢复。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 150102 
告警描述 :接口IPv6协议状态Down。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface v6 status.
DisplayResult:The interface(index=$2,name='$1') v6 status turned into $3.` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口v6协议状态 
告警样例 :告警产生： 
`An alarm 150102 ID 17 level 5 occurred at 11:00:05 03-10-2010 sent by ZXR10 MPU-0/26/0
%IP% Interface v6 status  The interface(index=7,name='loopback1') v6 status turned into
 protocol DOWN` 
告警恢复： 
`An alarm 150102 ID 17 level 5 cleared at 10:59:49 03-10-2010 sent by ZXR10 MPU-0/26/0
%IP% Interface v6 status  The interface(index=7,name='loopback1') v6 status turned into 
protocol UP` 
删除接口导致的告警恢复： 
`An alarm 150102 ID 17 level 5 cleared at 10:59:49 03-10-2010 sent by ZXR10 MPU-0/26/0
%IP% Interface v6 status  The interface(index=7,name='loopback1') v6 status turned into 
DELETED` 
引起原因 :对端口进行shutdown操作。 
端口连线出现异常等，引起端口Down。 
接口IPv6协议态Down，接口没有ipv6 enable。 
产生的影响 :IPv6路由等业务无法启动或运行。 
处理建议 :执行命令[show interface]，查看接口是否开启了IPv6功能。
Y→步骤3 
N→步骤2 
开启IPv6功能，完成后，检查告警是否恢复。 
Y→结束 
N→步骤3 
执行命令[show ipv6 interface]，查看接口的物理状态是否up。
Y→步骤5 
N→步骤4 
检查接口模块、物理线路，排除硬件故障后，检查告警是否恢复。 
Y→结束 
N→步骤5 
执行命令[show ipv6 interface]，查看接口的IPv6链路状态是否up。
Y→步骤8 
N→步骤6 
执行命令[show running-config-interface]，查看两端设备的接口配置是否相匹配。
Y→步骤8 
N→步骤7 
根据实际情况进行配置，完成后，检查告警是否恢复。 
Y→结束 
N→步骤8 
请联系中兴通讯技术支持工程师。 
## 150104 
告警描述 :接口删除通知。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface delete.
DisplayResult:The interface(index=$2,name='$1') was $3.` 
参数说明 :$1：接口名字； 
$2：接口索引值； 
$3：接口操作 
告警样例 :`A notification 150104 ID 26 level 6 occurred at 00:00:00 01-01-2000 sent by 
ZXR10 MPU-0/20/0 %IP% Interface delete  The interface(index=12,name='loopback11') 
was deleted` 
引起原因 :用户使用no interface命令对接口进行删除操作。 
用户对线卡或者接口卡进行拔板操作。 
用户对父接口进行删除操作时，会触发子接口的删除操作。 
产生的影响 :设备侧基于此接口的路由，转发等功能无法实现。 
处理建议 :确认接口是否需要删除。 
Y→结束 
N→步骤2 
恢复接口，完成后，检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 150106 
告警描述 :接口二层检测状态Down。 
默认级别 :3 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Interface layer2 detect status
DisplayResult: The interface(index=$2,name='$1') layer2 detect status turned into $3` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口二层检测状态Up或者Down 
告警样例 :告警产生： 
`An alarm 150106 ID 4 level 3 occurred at 07:19:56 10-25-2011 sent by ZXR10 MPU-0/20/0
%IP% Interface layer2 detect status  The interface(index=5,name='fei-0/1/0/1') layer2 
detect status turned into protocol DOWN` 
告警恢复： 
`An alarm 150106 ID 4 level 3 cleared at 07:20:31 10-25-2011 sent by ZXR10 MPU-0/20/0
%IP% Interface layer2 detect status  The interface(index=5,name='fei-0/1/0/1') layer2 
detect status turned into  protocol UP` 
删除接口导致的告警恢复： 
`An alarm 150106 ID 4 level 3 cleared at 07:20:31 10-25-2011 sent by ZXR10 MPU-0/20/0
%IP% Interface layer2 detect status  The interface(index=5,name='fei-0/1/0/1') 
layer2 detect status turned into DELETED` 
引起原因 :对端端口Down。 
链路中断。 
产生的影响 :被检测的二层链路Down。 
处理建议 :执行命令[show samgr track]检查track对象是否存在。
Y→步骤2 
N→步骤4 
执行命令[show running-config]，检查端口是否配置了track实例。
Y→步骤3 
N→步骤5 
检查端口连线是否正确。 
Y→步骤7 
N→步骤6 
配置track对象，检查告警是否恢复。 
`ZXR10(config)samgr
  ZXR10(config-samgr)track track_name /*根据不同检测类型配置不同类型对象*/
  ZXR10(config)interface interace_name
  ZXR10(config-if)track track_name` 
Y→结束 
N→步骤7 
配置接口track实例，检查告警是否恢复。 
`ZXR10(config)interface interace_name
  ZXR10(config-if)track track_name` 
Y→结束 
N→步骤7 
重新插好线缆，检查告警是否恢复。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 150107 
告警描述 :接口三层IPv4检测状态Down。 
默认级别 :3 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Interface ipv4 detect status
DisplayResult: The interface(index=$2,name='$1') ipv4 detect status turned into $3` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口三层IPv4检测状态Up或者Down 
告警样例 :告警产生： 
`An alarm 150107 ID 5 level 3 occurred at 07:21:00 10-25-2011 sent by ZXR10 MPU-0/26/0
%IP% Interface ipv4 detect status  The interface(index=5,name='smartgroup2') ipv4 
detect status turned into protocol DOWN` 
告警恢复： 
`An alarm 150107 ID 5 level 3 cleared at 07:21:22 10-25-2011 sent by ZXR10 MPU-0/26/0
%IP% Interface ipv4 detect status  The interface(index=5,name='smartgroup2') ipv4 
detect status turned into protocol UP` 
删除接口导致的告警恢复： 
`An alarm 150107 ID 5 level 3 cleared at 07:21:22 10-25-2011 sent by ZXR10 MPU-0/26/0
%IP% Interface ipv4 detect status  The interface(index=5,name='smartgroup2') ipv4 
detect status turned into DELETED` 
引起原因 :对端端口Down。 
链路中断。 
产生的影响 :被检测的三层IPv4链路Down。 
处理建议 :执行命令[show samgr track]检查track对象是否存在。
Y→步骤2 
N→步骤4 
执行命令[show running-config]，检查端口是否配置了track实例。
Y→步骤3 
N→步骤5 
检查端口连线是否连好。 
Y→步骤7 
N→步骤6 
配置track对象，检查告警是否恢复。 
`ZXR10(config)samgr
  ZXR10(config-samgr)track track_name /*根据不同检测类型配置不同类型对象*/
  ZXR10(config)interface interace_name
  ZXR10(config-if)track track_name` 
Y→结束 
N→步骤7 
配置接口track实例，检查告警是否恢复。 
`ZXR10(config)interface interace_name
  ZXR10(config-if)track track_name` 
Y→结束 
N→步骤7 
重新插好线缆，检查告警是否恢复。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 150108 
告警描述 :接口三层IPv6检测状态Down。 
默认级别 :3 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Interface ipv6 detect status
DisplayResult: The interface(index=$2,name='$1') ipv6 detect status turned into $3` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口三层IPv6检测状态Up或者Down 
告警样例 :告警产生： 
`An alarm 150108 ID 6 level 3 occurred at 07:21:51 10-25-2011 sent by ZXR10 MPU-0/26/0
%IP% Interface ipv6 detect status  The interface(index=5,name='smartgroup2') ipv6 
detect status turned into protocol DOWN` 
告警恢复： 
`An alarm 150108 ID 6 level 3 cleared at 07:22:09 10-25-2011 sent by ZXR10 MPU-0/26/0
%IP% Interface ipv6 detect status  The interface(index=5,name='smartgroup2') ipv6 
detect status turned into protocol UP` 
删除接口导致的告警恢复： 
`An alarm 150108 ID 6 level 3 cleared at 07:22:09 10-25-2011 sent by ZXR10 MPU-0/26/0
%IP% Interface ipv6 detect status  The interface(index=5,name='smartgroup2') ipv6 
detect status turned into DELETED` 
引起原因 :对端端口Down。 
链路中断。 
产生的影响 :被检测的三层IPv6链路Down。 
处理建议 :执行命令[show samgr track]检查track对象是否存在。
Y→步骤2 
N→步骤4 
执行命令[show running-config]，检查端口是否配置了track实例。
Y→步骤3 
N→步骤5 
检查端口连线是否连好。 
Y→步骤7 
N→步骤6 
配置track对象，检查告警是否恢复。 
`ZXR10(config)samgr
  ZXR10(config-samgr)track track_name /*根据不同检测类型配置不同类型对象*/
  ZXR10(config)interface interace_name
  ZXR10(config-if)track track_name` 
Y→结束 
N→步骤7 
配置接口track实例，检查告警是否恢复。 
`ZXR10(config)interface interace_name
  ZXR10(config-if)track track_name` 
Y→结束 
N→步骤7 
重新插好线缆，检查告警是否恢复。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 150111 
告警描述 :接口二层协议状态Down。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Interface layer2 status. 
DisplayResult:The interface(index=$2,name='$1') layer2 status turned into $3.` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口二层协议状态 
告警样例 :告警产生： 
`An alarm 150111 ID 8 level 5 occurred at 13:55:18 03-28-2013 sent by ZXR10 MPU-0/26/0
%IP% Interface layer2 status.  The interface(index=11,name='gei-0/1/0/5.1') layer2 
status turned into protocol DOWN` 
告警恢复： 
`An alarm 150111 ID 8 level 5 cleared at 13:55:39 03-28-2013 sent by ZXR10 MPU-0/26/0
%IP% Interface layer2 status. The interface(index=11,name='gei-0/1/0/5.1') layer2 
status turned into protocol UP` 
删除接口导致的告警恢复： 
`An alarm 150111 ID 8 level 5 cleared at 13:55:39 03-28-2013 sent by ZXR10 MPU-0/26/0
%IP% Interface layer2 status. The interface(index=11,name='gei-0/1/0/5.1') layer2 
status turned into DELETED` 
引起原因 :对端口进行shutdown操作。 
端口连线出现异常或者二层检测链路不同等，引起端口Down。 
接口被删除。 
产生的影响 :接口链路中断，该接口无法进行正常转发。 
基于二层的IP层和IPv6层的相关业务，如路由等无法正常下发。 
处理建议 :执行命令[show running-config-interface]，查看接口上是否配置了[shutdown]命令。
Y→步骤7 
N→步骤2 
执行命令[show interface]，查看接口的物理状态是否是up。
Y→步骤4 
N→步骤3 
检查接口模块、物理线路，排除硬件故障后，检查告警是否恢复。 
Y→结束 
N→步骤4 
执行命令[show interface]，查看接口的链路状态是否是up。
Y→步骤7 
N→步骤5 
执行命令[show running-config-interface]，查看两端设备的接口的配置是否相匹配。
Y→步骤7 
N→步骤6 
根据实际情况进行配置，检查告警是否恢复。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 150114 
告警描述 :接口IPv4协议首次UP。 
默认级别 :5 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface status.
DisplayResult:The interface(index=$2,name='$1') turned into $3.` 
参数说明 :$1：接口名字 
$2：接口索引值 
$3：接口状态UP或者DOWN 
告警样例 :`A notification 150114 ID 27 level 5 occurred at 01:34:08 04-25-2020 sent by ZXR10 MPU-0/26/0
%IP% Interface status.  The interface(index=3,name='gei-0/1/0/1') turned into protocol UP.` 
引起原因 :接口第一次IPv4协议UP。 
产生的影响 :无 
处理建议 :无需处理。 
# IPSec 
## 302001 
告警描述 :IKE协商失败。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment: IKE negotiation failed 
DisplayResult: (Interface $1,peer $2,mode $3,phase $4,message $5,$6)` 
参数说明 :$1：告警信息对应的接口名 
$2：告警信息对应的对端地址 
$3：协商模式 
$4：第几阶段 
$5：第几条消息 
$6：简单描述的失败原因 
告警样例 :`A notification 302001 ID 1 level 6 occurred at 08:00:45 03-02-2011 sent by ZXR10 GSU-0/4/0
%IPsec% IKE negotiation failed.  (Interface gei-0/1/0/1,peer 100.0.0.35,mode quick,phase 
2,message 2,parse negotiation message error)` 
引起原因 :IKE报文发送失败。 
IKE报文解析错误。 
IKE协商处理失败。 
产生的影响 :无法生成IPSec SA，对应IPSec隧道无法进行IPSec处理，使用该IPSec隧道进行IPSec保护的业务将断流。 
处理建议 :检查端口和链路工作是否正常。 
Y→步骤3 
N→步骤2 
排除端口和链路物理故障，检查告警是否消失。 
Y→结束 
N→步骤3 
执行ping命令确定对端设备是否在线（检查是否能ping通对端设备）。
Y→步骤5 
N→步骤4 
连接线路有问题，检查、恢复链路（确保ping通对端设备），检查告警是否清除。 
Y→结束 
N→步骤5 
执行IPSec的[show running-config]命令查看配置是否匹配。
Y→步骤7 
N→步骤6 
修改配置，配置匹配后，检查告警是否清除。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 302002 
告警描述 :IPSec DPD检测失败。
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:IPsec DPD failed.
DisplayResult:(local $1,peer $2,vrf $3).` 
参数说明 :$1：告警信息对应的接口名 
$2：告警信息对应的对端地址 
告警样例 :告警产生： 
`An alarm 302002 ID 1 level 5 occurred at 07:59:40 03-02-2011 sent by ZXR10 GSU-0/4/0
%IPsec% IPsec DPD failed.  (Interface ipsec_tunnel1,peer 100.0.0.35)` 
告警恢复： 
`An alarm 302002 ID 1 level 5 cleared at 08:00:06 03-02-2011 sent by ZXR10 GSU-0/4/0
%IPsec% IPsec DPD failed.  (Interface ipsec_tunnel1,peer 100.0.0.35)` 
引起原因 :对端死亡，无法连通对端，包括网络阻塞，对端SA失效等引起的连通检测失败。 
产生的影响 :删除已经生成的IPSec SA，会尝试建立一条新的IPSec隧道。对应的IPSec隧道无法进行IPSec保护，使用该隧道的业务将断流。 
处理建议 :检查端口和链路工作是否正常。 
Y→步骤3 
N→步骤2 
排除端口和链路物理故障，检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 302003 
告警描述 :IPSec出接口的MTU值小于IPSec包的封装长度。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:The interface MTU is error.
DisplayResult:` 
参数说明 :无 
告警样例 :`A notification 302003 ID 1 level 6 occurred at 08:00:45 03-02-2011 sent 
by ZXR10 GSU-0/4/0 %IPSEC% The interface MTU is error.` 
引起原因 :当IPSec出接口的MTU值小于IPSec封装长度时，发起告警。 
产生的影响 :提示用户修改出接口MTU。 
处理建议 :执行命令[show ip forwarding route]查看IPSec出接口信息。
执行命令[ip mtu]修改出接口的MTU值，确保IPSec出接口的MTU值大于IPSec包的封装长度，检查告警是否清除。
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 302004 
告警描述 :IPSec配置重复。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment: The tunnel or transport configuration is same.
DisplayResult: ($1 ,$2)` 
参数说明 :$1：隧道名称 
$2：重复隧道信息 
告警样例 :`A notification 302004 ID 1 level 6 occurred at 08:00:45 03-02-2011 sent by ZXR10 GSU-0/4/0 
%IPSEC% The tunnel or transport configuration is the same.  (ipsec_transport4 ,local 
peer vrf is the same with ipsec_transport3)` 
引起原因 :隧道、transport下配置相同的local（interface）IP、peer
IP和peer VRF。 
产生的影响 :IPSec隧道、transport接口协商异常。 
处理建议 :执行命令[show running ipsec]查看IPSec配置信息，是否有ipsec_tunnel
或者ipsec_transport下配置相同的local IP、peer IP和peer VRF。
Y→步骤2 
N→步骤3 
修改ipsec_tunnel或者ipsec_transport下的local IP、peer IP和peer VRF配置，完成后，检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
# L3VPN 
## 200310 
告警描述 :进入VRF的IPv4路由超过配置的路由最大上限。 
默认级别 :3 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Routes limit is reached.
DisplayResult:Error data:$1` 
参数说明 :$1：vpn实例名字 
告警样例 :告警产生： 
`An alarm 200310 ID 1 level 3 occurred at 01:56:12 02-27-2010 sent by MPU-0/20/0
%COURIER% Routes limit is reached. Error data:The routes limit of yy is reached` 
告警消除： 
`An alarm 200310 ID 1 level 3 cleared at 03:44:58 02-27-2010 sent by MPU-0/20/0
%COURIER% Routes limit is reached. Error data:The routes limit of yy is reached` 
引起原因 :配置了 VPN Route Limit功能，非warning-only（例如：vrf配置模式下，配置maximum
routes 4 75），当vrf中新路由加入，现有路由数（不包括新路由）达到配置的最大路由上限（第一个参数 ，如4），告警发生。 
产生的影响 :新路由不能加入。 
处理建议 :show ip vrf detail vrf实例名：检查此vrf
实例是否配置了最大路由条数限制。 
Y→步骤2 
N→步骤3 
去除最大路由条数的限制或将最大限制改大，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200311 
告警描述 :进入VRF的IPv4路由超过配置的告警门限。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Routes warning limit is reached.
DisplayResult:Warning data:$1` 
参数说明 :$1：vpn实例名字 
告警样例 :告警产生：  
`An alarm 200311 ID 1 level 5 occurred at 08:28:30 07-22-2011 sent by ZXR10 MPU-0/20/0
%COURIER% Routes warning limit is reached. Warning data:The routes limit of zte is reached` 
告警消除：  
`An alarm 200311 ID 1 level 5 cleared at 08:28:54 07-22-2011 sent by ZXR10 MPU-0/20/0
%COURIER% Routes warning limit is reached. Warning data:The routes limit of zte is reached` 
引起原因 :配置了 VPN Route Limit功能（例如：VRF配置模式下，配置maximum
routes 4 75或者maximum routes 4 warning-only），当VRF新路由加入后，路由现有总数（包括新路由）达到告警上限（配置maximum
routes 4 75时，告警上限为4 * 75% =3,配置maximum routes 4 warning-only时，告警上限为4
*100% =4），告警发生。 
产生的影响 :无 
处理建议 :show ip vrf detail vrf实例名：检查此vrf 实例是否配置了最大路由条数限制。 
Y→步骤2 
N→步骤3 
去除最大路由条数的限制或将最大限制改大，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200312 
告警描述 :进入VRF的IPv6路由超过配置的路由最大上限。
默认级别 :3 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment: IPv6 routes limit is reached.
DisplayResult: Error data:$1` 
参数说明 :$1：VPN的实例名字 
告警样例 :告警产生： 
`An alarm 200312 ID 6 level 3 occurred at 09:29:12 06-04-2013 sent by ZXR10 MPU-0/20/0
%L3VPN% IPv6 routes limit is reached.  Error data:The IPv6 routes limit of zte is reached` 
告警消除： 
`An alarm 200312 ID 6 level 3 cleared at 09:29:32 06-04-2013 sent by ZXR10 MPU-0/20/0
%L3VPN% IPv6 routes limit is reached.  Error data:The IPv6 routes limit of zte is reached` 
引起原因 :VRF配置了 VPN Route Limit功能，在VRF的v6地址族下非warning-only（例如：VRF
v6地址族配置模式下，配置maximum routes 4 75），当VRF中新路由加入，现有路由数（不包括新路由）达到配置的最大路由上限（第一个参数
，如4），告警发生。
产生的影响 :新路由不能加入。 
处理建议 :执行命令[show ip vrf detail ]<vrf-name>，检查此VRF实例是否配置了最大路由条数限制。
Y→步骤2 
N→步骤3 
去除最大路由条数的限制或将最大限制改大，检查告警是否清除。 
`ZXR10(config)ip vrf vrf-name
ZXR10(config-vrf)address-family ipv6
ZXR10(config-vrf-af)no maximum routes  /*删除限制*/
ZXR10(config-vrf-af)maximum routes <更大值> <更大值>  /*或将限制值改大*/` 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200313 
告警描述 :进入VRF的IPv6路由超过配置的告警门限。
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment: IPv6 routes warning limit is reached.
DisplayResult: Warning data:$1
` 
参数说明 :$1：VPN的实例名字 
告警样例 :告警产生： 
`An alarm 200313 ID 7 level 5 occurred at 09:29:12 06-04-2013 sent by ZXR10 MPU-0/20/0
%L3VPN% IPv6 routes warning limit is reached.  Warning data:The IPv6 routes warning 
limit of zte is reached` 
告警消除： 
`An alarm 200313 ID 7 level 5 cleared at 09:29:32 06-04-2013 sent by ZXR10 MPU-0/20/0
%L3VPN% IPv6 routes warning limit is reached.  Warning data:The IPv6 routes warning 
limit of zte is reached
` 
引起原因 :配置了VPN IPv6 Route Limit功能（例如：VRF v6地址族配置模式下，配置maximum routes 4 75或maximum routes 4 warning-only），当VRF新v6路由加入后，IPv6路由现有总数（包括新路由）达到告警上限（配置maximum routes 4 75时，告警上限为4ⅹ75%=3，配置maximum routes 4 warning-only时，告警上限为4ⅹ100%=4），产生告警。
产生的影响 :无。 
处理建议 :执行命令[show ip vrf detail ]<vrf-name>，检查此VRF实例是否配置了最大路由条数告警命令。
Y→步骤2 
N→步骤3 
去除最大路由条数告警的限制或将最大告警限制改大。 
`ZXR10(config)ip vrf vrf-name
ZXR10(config-vrf)address-family ipv6
ZXR10(config-vrf-af)no maximum routes  /*去除最大路由条数告警的限制*/
ZXR10(config-vrf-af)maximum routes <更大值> warning-only
/*或将最大告警限制改大*/` 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200806 
告警描述 :ECMP成员有效性发生变化。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment: ECMP change
DisplayResult: $1` 
参数说明 :$1：ECMP 成员down的信息 
告警样例 :UNI侧场景成员有效变无效： 
`A notification 200806 ID 155 level 6 occurred at 01:41:03 06-25-2014 sent by ZXR10 MPU-0/20/0 
%L3VPN% ECMP change.  Vaild number:2 Nexthop:30.1.1.0 Port:fei-0/1/0/1 status: Invaild ` 
NNI侧场景成员有效变无效： 
`A notification 200806 ID 155 level 6 occurred at 01:41:03 06-25-2014 sent by ZXR10 MPU-0/20/0 
%L3VPN% ECMP change.  Vaild number:2 Tunnel:tunnel1 status: Invaild` 
引起原因 :pernament ECMP成员无效。 
产生的影响 :提示ECMP成员无效信息。 
处理建议 :提示用户ECMP成员无效信息，无需处理。 
## 200807 
告警描述 :L3VPN peer不可达。 
默认级别 :6 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:L3VPN PEER change. 
DisplayResult:Tunnel $1 vrf $2 is $3` 
参数说明 :$1：TUNNEL远端地址 
$2：VPN名称 
$3: 状态信息 
告警样例 :告警产生： 
`An alarm 200807 ID 256 level 6 occurred at 01:48:40 04-10-2013 sent by ZXR10 MPU-0/20/0 
%L3VPN% L3VPN PEER change. Tunnel 131.0.77.8 vrf cqz1 is unreachable` 
告警恢复： 
`An alarm 200807 ID 300 level 6 cleared at 01:30:40 01-01-2000 sent by ZXR10 MPU-0/20/0 
%L3VPN% L3VPN PEER change. Tunnel 131.0.77.8 vrf cqz1 is reachable` 
引起原因 :在vrf配置peer tunnel-policy，也就是vrf绑定隧道策略的情况下，隧道策略检测到的隧道up或down。 
产生的影响 :用户可以直接感知隧道的状态，对业务无影响。 
处理建议 :检查对端L3VPN配置。 
## 200808 
告警描述 :L3VPN接收帧数越限。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Receive frames threshold crossed. 
DisplayResult:VRF $8.` 
参数说明 :$8:VRF名字 
告警样例 :告警产生： 
`An alarm 200808 1 ID 164 level 5 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%L3VPN% Receive frames threshold crossed. VRF zte <118-description> 
15min high alarm occur. High thres is: 200, current value is: 100000` 
告警恢复： 
`An alarm 200808 1 ID 164 level 5 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%L3VPN% Receive frames threshold crossed. VRF zte <118-description> 
15min high alarm occur. High thres is: 200, current value is: 100000` 
引起原因 :L3VPN业务量过大。 
产生的影响 :L3VPN收包占用带宽过大。 
处理建议 :检查业务量增大是否为故障引起。 
Y→步骤2  
N→步骤3 
排除业务量增大是故障引起，检查告警是否消失。 
Y→结束  
N→步骤3 
联系中兴通讯技术支持人员。  
## 200809 
告警描述 :L3VPN发送帧数越限。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Send frames threshold crossed. 
DisplayResult:VRF $8.` 
参数说明 :$8：VRF名字 
告警样例 :告警产生： 
`An alarm 200809 1 ID 164 level 5 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%L3VPN% Send frames threshold crossed.(name = zte).<118-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. ` 
告警恢复： 
`An alarm 200809 1 ID 164 level 5 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%L3VPN% Send frames threshold crossed.(name = zte).<118-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000. ` 
引起原因 :L3VPN业务量过大。 
产生的影响 :L3VPN发包占用带宽过大。 
处理建议 :检查业务量增大是否为故障引起。 
Y→步骤2  
N→步骤3 
排除业务量增大是故障引起，检查告警是否消失。 
Y→结束  
N→步骤3 
联系中兴通讯技术支持人员。  
# LDP 
## 250106 
告警描述 :LDP会话Down。
默认级别 :4 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Session to neighbor changed.
DisplayResult:Neighbor($1:$2--$4:$3) is $6, status code: $5, $7.` 
参数说明 :$1：对端的LDP LSR ID标识符   
$2：对端LDP标签空间标识符  
$3：本端LDP标签空间标识符   
$4：本端LDP LSR ID标识符  
$5：会话状态改变的原因码   
$6：当前状态   
$7：$5参数中对应的具体原因 
告警样例 :告警产生： 
`An alarm 250106 ID 1 level 4 occurred at 02:28:33 03-01-2010 sent by MPU-0/26/0
%LDP% Session to neighbor changed. Neighbor(13.13.13.13:0--23.1.1.2:0) is down, 
pre-state: OPERATIONAL, state: NONEXISTENT, status code: 9, 
Transport address changed.` 
告警恢复： 
`An alarm 250106 ID 1 level 4 cleared at 02:28:50 03-01-2010 sent by MPU-0/26/0
%LDP% Session to neighbor changed.  Neighbor(2.9.9.9:0--1.9.9.9:0) is up, 
pre-state: OPENREC, state: OPERATIONAL, status code: 2147483393, 
Receive keepalive.` 
引起原因 :LDP邻居Down。 
产生的影响 :对应LSP标签变为Untag，标签流不通。 
处理建议 :执行命令[show mpls ldp neighbor]检查会话状态是否为Oper。
Y→结束 
N→步骤2 
检查引起LDP会话状态变迁的事件码，查阅告警手册事件码说明是否与用户实际操作一致。 
Y→结束 
N→步骤3 
执行命令[show running-config ldp]检查配置是否正确。
Y→步骤4 
N→步骤6 
执行命令[show ip forward route]检查会话邻居建链使用的传输地址路由是否存在。
Y→步骤5 
N→步骤6 
检查会话邻居建链使用的传输地址是否能被Ping通。 
Y→结束 
N→步骤6 
请联系中兴通讯技术支持工程师。 
## 250107 
告警描述 :清除LDP会话。 
默认级别 :7 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Clear neighbor.
DisplayResult:Clear neighbor($1:$2--$4:$3) by console.` 
参数说明 :$1：对端LDP LSR ID标识符 
$2：对端LDP标签空间标识符 
告警样例 :`A notification 250107 ID 1 level 7 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%LDP% Clear neighbor.  Clear neighbor($1:$2) by console.` 
引起原因 :清除（clear）了LDP邻居。 
产生的影响 :无 
处理建议 :这是提示性信息，不需要用户处理。 
## 250109 
告警描述 :LDP会话GR过程描述。
默认级别 :7 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment： LDP GR processing.
DisplayResult： $1` 
参数说明 :$1：细节描述。 
告警样例 :`A notification 250109 ID 1 level 7 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%LDP% LDP GR processing. GR timer stopped, delete all sessions stale labels.` 
引起原因 :LDP协议GR过程开启。 
产生的影响 :无。 
处理建议 :这是提示性信息，不需要用户处理。 
## 250110 
告警描述 :LDP不同会话发现相同的邻居地址。
默认级别 :7 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Get the same address from different session.
DisplayResult:Neighbor($1:$2--$4:$3) send the address message 
including conflicting address($5).` 
参数说明 :$1：对端LDP LSR ID标识符 
$2：对端LDP标签空间标识符 
$5：相同的邻居地址 
告警样例 :`A notification 250110 ID 1 level 7 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%LDP% Get the same address from different session. Neighbor(2.2.2.2:0) send the same 
PEERADDR(2.2.2.1).` 
引起原因 :用户组网错误，导致LDP不同会话发现相同的邻居地址。 
产生的影响 :可能无法形成正确的LSP。
处理建议 :查看告警信息中引起地址冲突的对端设备LSR ID是否存在。 
Y→步骤2 
N→步骤3 
根据LSR ID找到相应设备，检查是否能删除该设备上引起冲突的接口地址。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 250111 
告警描述 :TCP建立失败。
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:TCP connect failed.
DisplayResult:Session neighbor($1:$2--$4:$3),transport address:src/dst($5/$6).` 
参数说明 :$1：对端LDP LSR ID标识符 
$2：对端LDP标签空间标识符 
$5：本端LDP传输层地址 
$6：对端LDP传输层地址 
告警样例 :告警产生： 
`An alarm 250111 ID 1 level 5 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%LDP% TCP connect failed.Session neighbor(9.6.3.1:0),
transport address:src/dst(9.6.3.2/9.6.3.1).` 
告警恢复： 
`An alarm 250111 ID 1 level 5 cleared at 02:28:50 03-01-2010 sent by MPU-0/20/0
%LDP% TCP connect failed.Session neighbor(9.6.3.1:0),
transport address:src/dst(9.6.3.2/9.6.3.1).` 
引起原因 :LDP主动端发起TCP建联请求后，可能会因为两端配置的MD5不同、路由不可达等原因未建立成功。 
产生的影响 :LDP会话建立失败，等待重新发起建联请求。 
处理建议 :执行命令[show mpls ldp neighbor]检查会话状态是否为Oper。
Y→结束 
N→步骤2 
执行命令[show running-config ldp]检查配置是否正确。
Y→步骤3 
N→步骤5 
执行命令[show ip forward route]检查会话邻居建链使用的传输地址路由是否存在。
Y→步骤4 
N→步骤5 
检查会话邻居建链使用的传输地址是否能被Ping通。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 250112 
告警描述 :会话个数达到所允许的LDP会话最大个数的80%。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:LDP session reached the percentage of global alarm threshold.
DisplayResult:(Alarm threshold = $1 percent,current session count:$2).` 
参数说明 :$1：门限值 
告警样例 :告警产生： 
`An alarm 250112 ID 1 level 5 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%LDP% LDP session reached the percentage of global alarm threshold.
( Alarm threshold = 80 percent)` 
告警恢复： 
`An alarm 250112 ID 1 level 5 cleared at 02:28:50 03-01-2010 sent by MPU-0/20/0
%LDP% LDP session reached the percentage of global alarm threshold.
( Alarm threshold = 80 percent)` 
引起原因 :会话个数达到所允许的LDP会话最大个数的80%,用于提醒用户即将性能满。 
产生的影响 :提醒用户，当前LDP会话的总数已经达到最大会话数的百分比，不需要用户处理。使用户能够更好的规划LDP会话的相关配置。 
处理建议 :提示用户，不需要用户处理。 
## 250113 
告警描述 :LDP会话数目达到允许上限。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:LDP session reached the global threshold.
DisplayResult:(current session count:$1).` 
参数说明 :$1：门限值 
告警样例 :告警产生： 
`An alarm 250113 ID 1 level 5 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%LDP% LDP session reached the global threshold..` 
告警恢复： 
`An alarm 250113 ID 1 level 5 cleared at 02:28:50 03-01-2010 sent by MPU-0/20/0
%LDP% LDP session reached the global threshold..` 
引起原因 :会话个数达到所允许的LDP会话最大个数的100%,用于提醒用户已经达到性能满。 
产生的影响 :提醒用户，当前LDP会话的总数已经达到最大会话数，不需要用户处理。 
处理建议 :提示用户，不需要用户处理。 
## 250114 
告警描述 :hello传输层地址与会话不一致。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:LDP hello transport addr is inconsistent with session.  
DisplayResult:$1,local_trans/peer_trans: $2/$3$4` 
参数说明 :$1：直连hello显示收到hello的接口名如“fei-0/1/0/1”；目标hello显示“target” 
$2：本端的对应接口或目标会话的传输层地址 
$3：hello的传输层地址 
$4：如果是hello删除导致的clear，显示“,deleted.”；其他情况下（如因为hello加入进了会话）只显示句号“.” 
告警样例 :告警产生： 
`An alarm 250114 ID 34 level 5 occurred at 07:10:17 05-03-2017 sent by ZXR10 MPU-0/20/0
%LDP% LDP hello transport addr is inconsistent with session.  
fei-0/1/0/4,local_trans/peer_trans: 123.123.123.123/40.40.40.2.
An alarm 250114 ID 30 level 5 occurred at 07:01:40 05-03-2017 sent by ZXR10 MPU-0/20/0
%LDP% LDP hello transport addr is inconsistent with session.  
fei-0/1/0/5,local_trans/peer_trans: 123.123.123.123/50.50.50.2
An alarm 250114 ID 31 level 5 occurred at 07:03:13 05-03-2017 sent by ZXR10 MPU-0/20/0
%LDP% LDP hello transport addr is inconsistent with session.  
target,local_trans/peer_trans: 123.123.123.123/122.122.122.122.` 
告警恢复： 
`An alarm 250114 ID 34 level 5 cleared at 07:10:40 05-03-2017 sent by ZXR10 MPU-0/20/0
%LDP% LDP hello transport addr is inconsistent with session.  fei-0/1/0/4,
local_trans/peer_trans: 123.123.123.123/40.40.40.2,deleted.
An alarm 250114 ID 30 level 5 cleared at 07:08:01 05-03-2017 sent by ZXR10 MPU-0/20/0
%LDP% LDP hello transport addr is inconsistent with session.  fei-0/1/0/5,
local_trans/peer_trans: 123.123.123.123/50.50.50.2.
An alarm 250114 ID 31 level 5 cleared at 07:08:14 05-03-2017 sent by ZXR10 MPU-0/20/0
%LDP% LDP hello transport addr is inconsistent with session.  target,
local_trans/peer_trans: 123.123.123.123/122.122.122.122,deleted.` 
引起原因 :由于与会话的传输层地址不一致导致hello未加入当前会话，用于提示用户可能由于配置原因导致hello加入不进当前会话。 
产生的影响 :提醒用户，当前收到的hello由于传输层地址与会话不一致不能绑定到当前会话，使用户能够检查当前配置，更好的规划LDP会话的相关配置。 
处理建议 :[show mpls ldp neighbor]命令查看会话的传输层地址。
[show mpls ldp discovery]命令查看hello的传输层地址是否与1中会话的对端传输层地址相同。
Y→步骤3  
N→步骤4  
[show running-config ldp]查看本端的传输层地址配置是否与1中会话的本端传输层地址相同。
Y→结束 
N→步骤4  
按照场景，是否有必要到对端或者在本端修改传输层地址配置。 
Y→步骤5  
N→步骤6 
修改配置，[show mpls ldp neighbor]命令查看hello是否加入会话，告警是否消失。
Y→结束 
N→步骤6  
请联系中兴通讯技术支持工程师。 
# MPLSOAM 
## 250403 
告警描述 :TE静态隧道Down。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Tunnel state changed!
   DisplayResult: Tunnel is $1 ( Tunnel = $2  ingressId = $3 )` 
参数说明 :$1：隧道状态，告警产生为：local down或remote down；告警消除为：local
up或remote up 
$2：隧道ID 
$3：ingress ID 
告警样例 :告警产生： 
`An alarm 250403 ID 484 level 5 occurred at 09:33:30 01-30-2012 sent by ZXR10 PFU-0/1/0
 %MPLSOAM% Tunnel state changed.  Tunnel is remote down (Tunnel = 3 ingressId = 5.6.7.8)` 
告警恢复： 
`An alarm 250403 ID 89 level 5 cleared at 09:07:28 01-30-2012 sent by ZXR10 PFU-0/1/0
 %MPLSOAM% Tunnel state changed.  Tunnel is remote up (Tunnel = 3 ingressId = 5.6.7.8)` 
引起原因 :MPLSOAM检测到TE静态隧道Down，可能原因有： 
TE隧道链路断开或者损坏。 
TE隧道的节点的接口关闭或者损坏。 
产生的影响 :流量中断或者切换到备份隧道继续工作。 
处理建议 :执行命令[show mpls traffic-eng static]查看TE隧道状态是否up。
Y→步骤4 
N→步骤2 
执行命令[show running-config mplsoam]检查MPLS-OAM配置是否正确（头、尾节点的检测报文类型，检测频率等）。
Y→步骤4 
N→步骤3 
调整MPLS-OAM配置，检查告警是否清除。 
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
# MRT 
## 200901 
告警描述 :组播快速重路由倒换事件。 
默认级别 :5 
告警恢复 :是 
告警类型 :设备告警 
告警类别 :返回式事件 
告警描述原型 :`Comment:MRT FRR switch event.
DisplayResult:FRR index $1, master iif $2, slave iif $3, switch to $4, reason: $5.` 
参数说明 :$1：FRR索引 
$2：主备状态描述：slave 或 master 
告警样例 :倒换事件产生： 
`A MRT FRR switch event 200901 ID 427 level 5 occurred at 12:49:32 10-23-2012 sent by ZXR10 MPU-0/20/0
MRT FRR switch event. FRR index 111,switch to state:slave` 
倒换事件消失： 
`A MRT FRR switch event 200901 ID 453 level 5 cleared at 12:51:36 10-23-2012 sent by ZXR10 MPU-0/20/0
MRT FRR switch event.  FRR index 111,switch to state:master` 
引起原因 :端口状态down。 
检测的track状态down。 
产生的影响 :可能组播流量中断。 
处理建议 :使用show ip mroute命令查看入接口，show interface查看入接口的协议状态是否down。 
Y→步骤2 
N→步骤3 
根据实际情况配置为up，检查告警是否清除。 
Y→结束 
N→步骤3 
使用show samgr track命令，查看入接口的track状态是否down 
Y→步骤4 
N→步骤5 
根据实际情况配置为up，检查告警是否清除。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
# MSDP 
## 200701 
告警描述 :MSDP邻居Down。
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:MSDP peer state changed.
DisplayResult:MSDP $1: The reason of MSDP peer $2 $3 was $4.` 
参数说明 :$1:VRF实例名称，公网为空 
$2:邻居地址 
$3:邻居状态 
$4:邻居状态变化原因 
告警样例 :告警产生： 
`An alarm 200701 ID 1 level 5 occurred at 09:05:10 10-27-2009 sent by ZXR10 PFU-0/20/0 
%MSDP% MSDP peer state changed.MSDP vrf(zte): The reason of MSDP peer 100.10.10.20 
down was tcp close.` 
告警恢复： 
`An alarm 200701 ID 1 level 5 cleared at 09:05:15 10-27-2009 sent by ZXR10 PFU-0/20/0
%MSDP% MSDP peer state changed.MSDP vrf(zte): The reason of MSDP peer 100.10.10.20 
down was tcp close.` 
引起原因 :执行no peer命令删除邻居。 
执行shut down命令关闭邻居。 
执行clear ip msdp peer命令重置TCP连接。 
收到错误协议报文。 
保活周期（75秒）内未收到保活报文导致邻居超时。 
TCP建链接口Down或地址变化 
TCP Socket支撑模块出错。 
产生的影响 :TCP连接断开，邻居状态为Down。 
处理建议 :检查网络链路是否有故障。 
Y→步骤2 
N→步骤3 
排除链路故障，检查告警是否清除。 
Y→结束 
N→步骤3 
执行命令[show ip interface brief]查看接口状态是否是Down。
Y→步骤4 
N→步骤5 
排除接口故障，检查告警是否清除。 
Y→结束 
N→5 
执行命令[show ip msdp peer]查看是否删除了该邻居。
Y→步骤6 
N→步骤7 
增加该邻居，检查告警是否清除。 
Y→结束 
N→步骤7 
执行命令[show ip msdp peer]查看邻居是否shutdown。
Y→步骤8 
N→步骤9 
执行命令[no shutdown]开启邻居，检查告警是否清除。
Y→结束 
N→步骤9 
执行命令[show ip msdp peer]查看两端password是否一致。
Y→步骤11 
N→步骤10 
配置两端password一致，检查告警是否清除。 
Y→结束 
N→步骤11 
请联系中兴通讯技术支持工程师。 
# MTUNNEL-GROUP 
## 240402 
告警描述 :P2MP隧道倒换事件。 
默认级别 :3 
告警恢复 :根据翻转模式确定是否有告警消失。 
告警类型 :设备告警 
告警类别 :倒换事件 
告警描述原型 :`Comment:P2MP tunnel group switch event.
DisplayResult:P2MP tunnel group $1 switching to state: $2, reason: $3.` 
参数说明 :$1：发生倒换的P2MP隧道保护组id; 
$2：倒换的状态; 
$3：当前倒换状态产生原因 
告警样例 :倒换事件产生： 
`A protected event 240402 ID 427 level 3 occurred at 12:49:32 10-23-2012 sent by ZXR10 MPU-0/20/0
%MTUNNEL-GROUP% P2MP tunnel group switch event. P2MP tunnel group 1 switching to state: switched, 
reason: SF on working.` 
倒换事件消失： 
`A protected event 240402 ID 453 level 3 cleared at 12:51:36 10-23-2012 sent by ZXR10 MPU-0/20/0
%MTUNNEL-GROUP% P2MP tunnel group switch event. P2MP tunnel group 1 switching to state: no switch, 
reason: no request.` 
引起原因 :P2MP隧道保护组工作P2MP隧道或者保护P2MP隧道,检测出链路信号中断或者信号衰减,导致的切换或回切。 
产生的影响 :无影响，提示倒换发生。 
处理建议 :用户无需处理。 
# OSPF 
## 200401 
告警描述 :端口状态迁移。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface state changed.
DisplayResult:Interface $4 changed from $5 to $6 
(ProcessId:$1;AreaId:$2;IfName:$3;Reason:$7)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：OSPF接口IP地址 
$5：改变前的接口状态 
$6：改变后的接口状态 
$7：错误原因 
告警样例 :`A notification 200401 level 6 occurred at 14:05:39 03-01-2010 sent by MPU-0/26/0
%OSPFv2% Interface state changed. Intf 1.2.3.4 Waiting->DOWN 
(ProcessId:100;AreaId:0.0.0.1;IfName:gei-0/1/0/1;Reason:Physical down)` 
引起原因 :接口up、接口down、选举BDR、选举DR等。
产生的影响 :接口状态发生改变，如：Waiting->BackupDR。 
处理建议 :检查接口状态改变是否合理、是否出现异常，查看报文收发情况。 
## 200402 
告警描述 :虚链端口状态迁移。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual interface state changed.
DisplayResult:Interface $3 changed from $5 to $6 
(ProcessId:$1;TransitAreaId:$2;VirtIfNbrId:$4)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：OSPF接口IP地址 
$4：对端邻居ID 
$5：改变前的接口状态 
$6：改变后的接口状态 
告警样例 :`A notification 200402 level 6 occurred at 13:58:07 03-01-2010 sent by MPU-0/26/0
%OSPFv2% Virtual interface state changed. Vintf 2.2.3.5 P To P->Down
（ProcessId:100;TransitAreaId:0.0.0.1;VirtIfNbrId:1.0.0.2）` 
引起原因 :接口up、接口down。 
产生的影响 :虚链接口状态改变，如：DR->Down。 
处理建议 :检查虚接口状态改变是否合理、是否出现异常，查看报文收发情况。 
## 200403 
告警描述 :邻居状态迁移。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Neighbor state changed.
DisplayResult:Local ($3,IP $4) neighbor (Router ID $5,IP $6) 
changed from $7 to $8 (ProcessId:$1;AreaId:$2;Reason:$9)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$5：邻居路由器ID 
$6：OSPF接口IP地址 
$7：改变前的邻居状态 
$8：改变后的邻居状态 
$9：错误原因 
告警样例 :`A notification 200403 level 6 occurred at 14:36:45 03-01-2010 sent by MPU-0/26/0
%OSPFv2% Neighbor state changed. Nbr 2.2.3.5 intf 2.2.3.4 Full->Init(ProcessId:100;
AreaId:0.0.0.1;IfName:gei-0/1/0/1;NbrId:1.0.0.2;NbrIpAddr:10.0.0.2；Reason:bfdSessionStateChange)` 
引起原因 :收发报文导致里邻居状态改变，比如，hello报文收发成功导致邻居状态变化：Init->2
Way。 
产生的影响 :邻居状态发生改变，如：Init->2 Way。 
处理建议 :检查邻居状态改变是否合理、是否出现异常，查看报文收发情况。 
## 200404 
告警描述 :虚邻居状态迁移。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual neighbor state changed.
DisplayResult:Local $3 neighbor $4 changed from $5 to $6 
(ProcessId:$1;TransitAreaId:$2;VirtIfNbrId:$4;Reason:$7)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$4：OSPF虚邻居的IP地址 
$5：改变前的邻居状态 
$6：改变后的邻居状态 
$7：错误原因 
告警样例 :`A notification 200404 level 6 occurred at 14:22:21 08-26-2009 sent by MPU-0/26/0
%OSPFv2% Virtual neighbor state changed. Vnbr 4.3.3.3 Exch->Down
（ProcessId:100;TransitAreaId:0.0.0.1;VirtIfNbrId:1.0.0.2; Reason:DeadTimerExpire）` 
引起原因 :收发报文导致里虚链邻居状态改变，比如，hello报文收发成功导致邻居状态变化：Init->2
Way。 
产生的影响 :虚链邻居状态改变，如：Init->2 Way。 
处理建议 :检查虚链邻居状态改变是否合理、是否出现异常，查看报文收发情况。 
## 200405 
告警描述 :端口认证失败。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface auth failure.
DisplayResult:Intf $4 bad auth: $5 
(ProcessId:$1;AreaId:$2;IfName:$3;PacketSrc:$6;PacketType:$7)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：OSPF接口IP地址 
$5：邻居认证失败的提示信息 
$6：数据包源地址 
$7：数据包类型 
告警样例 :`A notification 200405 ID 1 level 6 occurred at 10:01:23 09-21-2009 sent by MPU-0/26/0
%OSPFv2% IfAuthFailure  intf 2.2.2.89 bad auth: bad md5 auth key
（ProcessId:100;AreaId:0.0.0.1;IfName:gei-0/1/0/1）` 
引起原因 :邻居建立的过程中，链路两端的接口认证配置不一致。 
产生的影响 :接口认证失败，邻居关系不能建立。 
处理建议 :执行命令[show running-config ospf]检查路由器对应接口上的邻接路由器设置的认证密码，是否与本路由器上的对应设置一致。
Y→步骤3 
N→步骤2 
将两端的认证密码修改一致。 
如果采用MD5认证，则修改的示例如下：ZXR10(config-ospfv2)#interface gei-0/1/0/1
ZXR10(config-ospfv2-if)#message-digest-key 1 md5 zte 
如果采用简单密码认证，则修改的示例如下：ZXR10(config-ospfv2)#interface gei-0/1/0/1
ZXR10(config-ospfv2-if)#authentication-key zte 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200406 
告警描述 :虚端口认证失败。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual interface auth failure.
DisplayResult:Vintf $4 bad auth: $7 
(ProcessId:$1;TransitAreaId:$2;VirtIfNbrId:$3)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：对端邻居ID 
$4：OSPF虚接口的IP地址 
$7：虚邻居认证失败的提示信息 
告警样例 :`A notification 200406 ID 1 level 6 occurred at 13:57:57 09-26-2009 sent by MPU-0/26/0
%OSPFv2% Virtual interface auth failure. Vintf 2.2.2.89 bad auth: Auth type mismatch
（ProcessId:100;TransitAreaId:0.0.0.1;VirtIfNbrId:1.0.0.2）` 
引起原因 :虚链邻居建立的过程中，虚链路两端的接口认证配置不一致。 
产生的影响 :虚接口认证失败，邻居关系建立不成功。 
处理建议 :执行命令[show running-config ospf]检查路由器对应虚接口上的邻接路由器设置的认证密码，是否与本路由器上的对应设置一致。
Y→步骤3 
N→步骤2 
将两端的认证密码修改一致。 
如果采用MD5认证，则修改的示例如下：ZXR10(config-ospfv2)#area 1 virtual-link 1.1.1.1 message-digest-key 1 md5 zte 
如果采用简单密码认证，则修改的示例如下：ZXR10(config-ospfv2)#area 1 virtual-link 1.1.1.1 authentication-key zte 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200407 
告警描述 :端口接收错误包。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface rx bad packet.
DisplayResult:On interface $4 Packet type $6 $7 
(ProcessId:$1;AreaId:$2;IfName:$3;PacketSrc:$5)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：OSPF接收错误报文的接口IP地址 
$5：数据包源地址 
$6$7：收到错误报文的提示信息 
告警样例 :`A notification 200407 level 6 occurred at 13:57:57 09-26-2009 sent by MPU-0/26/0
%OSPFv2% Interface rx bad packet. Bad pkt on intf 1.1.1.1: bad lstype in req pkt
（ProcessId:100;AreaId:0.0.0.1;IfName:gei-0/1/0/1;packetsrc;10.0.0.2;packetType:4）` 
引起原因 :一方邻居已经断掉，而另一方认为邻居仍然存在。 
产生的影响 :两端的接口配置不匹配，邻居建立不成功。 
处理建议 :检查接口物理连接是否可靠。 
## 200408 
告警描述 :虚端口接收错误包。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual interface rx bad packet.
DisplayResult:On interface $3 Packet type $6 $7 
(ProcessId:$1;TransitAreaId:$2;VirtIfNbrId:$4;PacketSrc:$5)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：OSPF接收错误报文的虚接口IP地址 
$4：对端邻居ID 
$5：数据包源地址 
$6$7：收到错误报文的提示信息 
告警样例 :`A notification 200408 level 6 occurred at 15:21:01 09-30-2009 sent by MPU-0/26/0
%OSPFv2% Virtual interface rx bad packet. Bad pkt on vintf 1.1.1.1: bad lstype in ack pkt
（ProcessId:100;TransitAreaId:0.0.0.1;VirtIfNbrId:1.0.0.2;PacketSrc:10.0.0.2;packetType:4）` 
引起原因 :一方虚邻居已经断掉，而另一方认为虚邻居仍然存在。 
产生的影响 :两端的接口配置不匹配，邻居建立不成功。 
处理建议 :检查组成虚接口的各个接口的物理连接是否可靠。 
## 200409 
告警描述 :接口配置错误。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface config error.
DisplayResult:On intf $4 : $7
(ProcessId:$1;AreaId:$2;IfName:$3;PacketSrc:$5;PacketType:$6)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：OSPF接收报文的接口IP地址 
$5：数据包源地址 
$6：数据包类型 
$7：收到接口配置不匹配报文的提示信息 
告警样例 :`A notification 200409 ID 1 level 6 ID 1 occurred at 14:02:22 03-01-2010 sent by MPU-0/26/0
%OSPFv2% Interface config error. On intf 1.2.3.4 : area mismatch
（ProcessId:100;AreaId:0.0.0.1;IfName:gei-0/1/0/1;packetSrc:10.0.0.2;PacketType:1）` 
引起原因 :两端的认证类型不一致。 
HELLO TIMER大小不一致。 
DEAD TIMER大小不一致。 
广播网络中，两端的网络掩码不匹配。 
两端的区域号不一致。 
产生的影响 :两端的接口配置不匹配，邻居建立不成功。 
处理建议 :执行命令[show running-config ospf]检查路由器对应接口上的邻接路由器的配置，是否与本路由器上的一致。
Y→步骤3 
N→步骤2 
修改接口上与对端接口不一致的配置。 
修改hello-interval，示例如下：ZXR10(config-ospfv2)#interface gei-0/1/0/1
ZXR10(config-ospfv2-if)#hello-interval 10 
修改dead-interval，示例如下：ZXR10(config-ospfv2)#interface gei-0/1/0/1
ZXR10(config-ospfv2-if)#dead-interval 40 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200410 
告警描述 :虚接口配置错误。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual interface config error.
DisplayResult:On vintf $4 : $7
(ProcessId:$1;TransitAreaId:$2;VirtIfNbrId:$3;PacketSrc:$5;PacketType:$6)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：对端邻居ID 
$4：OSPF接收报文的虚接口IP地址 
$5：数据包源地址 
$6：数据包类型 
$7：收到虚接口配置不匹配报文的提示信息 
告警样例 :`A notification 200410 ID 1 level 6 occurred at 08:25:11 10-21-2009 sent by MPU-0/26/0
%OSPFv2% Virtual interface config error. On vintf 2.2.2.1 : area mismatch
（ProcessId:100;TransitAreaId:0.0.0.1;VirtIfNbrId:1.0.0.2;PacketSrc:10.0.0.2;PacketType:1）` 
引起原因 :邻居建链的时候： 
两端的认证类型不一致 
HELLO TIMER大小不一致 
DEAD TIMER大小不一致 
产生的影响 :两端的虚接口配置不匹配，邻居建立不成功。 
处理建议 :执行命令[show running-config ospf]检查路由器对应虚接口上的邻接路由器的配置，是否与本路由器上的一致。
Y→步骤3 
N→步骤2 
修改虚接口上与对端接口不一致的配置。 
修改hello-interval，示例如下： 
`ZXR10(config-ospfv2)interface gei-0/1/0/1
ZXR10(config-ospfv2-if)area 1 virtual-link 1.1.1.1 hello-interval 10` 
修改dead-interval，示例如下： 
`ZXR10(config-ospfv2)interface gei-0/1/0/1
ZXR10(config-ospfv2-if)area 1 virtual-link 1.1.1.1 dead-interval 40` 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200420 
告警描述 :OSPF邻居Down。
默认级别 :4 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Neighbor state changed.
DisplayResult:Nbr(Router ID $4,IP $5), Local($3,IP $6), Full->Down.
(ProcessId:$1;AreaId:$2;Reason:$7)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：本地接口名称 
$4：邻居路由器ID 
$5：邻居接口IP地址 
$6：本地接口IP地址 
$7：错误原因 
告警样例 :告警产生： 
`An alarm 200420 ID 7 level 4 occurred at 01:03:52 05-27-2015 sent by ZXR10 MPU-0/26/0 
%OSPF% Neighbor state changed.  Nbr(id 10.0.0.2,ip 10.0.0.2), 
Local(gei-0/1/0/1,ip 10.0.0.1), Full->Down
(ProcessId:100;AreaId:0.0.0.1;Reason:SliceDown)` 
告警恢复： 
`An alarm 200420 ID 7 level 4 cleared at 01:03:52 05-27-2015 sent by ZXR10 MPU-0/26/0 
%OSPF% Neighbor state changed.  Nbr(id 10.0.0.2,ip 10.0.0.2), 
Local(gei-0/1/0/1,ip 10.0.0.1), Loading->Full
(ProcessId:100;AreaId:0.0.0.1;Reason:SliceDown)
` 
引起原因 :OSPF接口Down或者邻居关系超时。 
产生的影响 :OSPF的邻居会断开。 
处理建议 :检查邻居状态改变是否DOWN、是否出现异常，查看报文收发情况。 
Y→步骤2 
N→步骤3 
分析以上事件的原因是否因人为操作引起。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200421 
告警描述 :OSPF虚链邻居Down。
默认级别 :4 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Virtual neighbor state changed.
DisplayResult:Vnbr(Router ID $3), Local($5), Full->Down.
(ProcessId:$1;TransitAreaId:$2;Reason:$4)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：虚链邻居的路由器ID 
$4：错误原因 
$5：虚链的本地接口标识 
告警样例 :告警产生： 
`An alarm 200421 ID 12 level 4 occurred at 03:32:54 05-27-2015 sent by ZXR10 MPU-0/26/0 
%OSPF% Virtual neighbor state changed.  Vnbr(id 10.0.0.2), Local(vl(0.0.0.1 To 10.0.0.2)), 
Full->Down (ProcessId:100;TransitAreaId:0.0.0.1;Reason:networkTypeChange)` 
告警恢复： 
`An alarm 200421 ID 12 level 4 cleared at 03:32:54 05-27-2015 sent by ZXR10 MPU-0/26/0 
%OSPF% Virtual neighbor state changed.  Vnbr(id 10.0.0.2), Local(vl(0.0.0.1 To 10.0.0.2)), 
Loading->Full (ProcessId:100;TransitAreaId:0.0.0.1;Reason:networkTypeChange)` 
引起原因 :OSPF接口UP或邻居关系从FULL回退到2WAY状态。 
产生的影响 :OSPF的邻居会断开。 
处理建议 :检查虚链邻居状态改变是否DOWN、是否出现异常，查看报文收发情况。 
Y→步骤2 
N→步骤3 
分析以上事件的原因是否因人为操作引起。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200424 
告警描述 :OSPF链路状态数据库中非自己生成的LSA数目达到阈值。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Non self LSAs arrive at threshold.
DisplayResult:The threshold for maximum number: $2, current number: $3 (ProcessId:$1)` 
参数说明 :$1：OSPF进程号 
$2：配置的LSA阈值数 
$3：当前非自己生成的LSA数目 
告警样例 :`A notification 200424 ID 152 level 6 occurred at 16:02:55 11-24-2011 sent by ZXR10 PFU-0/20/0 
%OSPF% Non self LSAs arrive at threshold. 
Non self-originated LSAs has arrived at threshold of maximum number:750（ProcessId:1）` 
引起原因 :OSPF的非自己生成的LSA数目达到阈值。 
产生的影响 :无。 
处理建议 :检查本端和远端的配置是否错误，如lsa-limit和重分发配置。
Y→步骤2 
N→步骤3 
修改错误配置。 
查看lsa-limit配置是否存在问题、是否合理：ZXR10(config)#show ip ospf 1
OSPF 1 Router ID 2.2.2.2 enable
Domain ID type 0x5,value 0.0.0.1
Enabled for 16:16:12,Debug on
Number of areas 0, Normal 0, Stub 0, NSSA 0
Number of interfaces 0
Number of neighbors 0
Number of adjacent neighbors 0
Number of virtual links 0
Total number of entries in LSDB 0
Number of ASEs in LSDB 0, Checksum Sum 0x00000000
Number of grace LSAs 0
Number of new LSAs received 0
Number of self-originated LSAs 0
Maximum number of non self-originated LSAs allowed 10000, current number 0
Threshold for sending warning 75%
limit-time 5 minutes, fresh-time 10 minutes
limit-count allowed 5, current limit-count 0可以使用以下命令修改配置：ZXR10(config-ospfv2)#lsa-limit ?
<1-4294967294>  Max number of non self-generated LSAs can receive 
在远端设备上执行命令show running-config ospf查看是否存在错误的重分配配置：如错误地配置了重分配BGP：ZXR10(config)#show running-config ospf
! <OSPF>
router ospf 1
redistribute bgp-int
!
! </OSPF>删除重分配BGP配置：ZXR10(config-ospfv2)#no redistribute bgp-int 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200425 
告警描述 :OSPF链路状态数据库中非自己生成的LSA数目超出最大值。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Non self LSAs exceed maximum number.
DisplayResult:The maximum number: $2, current number: $3 (ProcessId:$1)` 
参数说明 :$1：OSPF进程号 
$2：LSA最大值 
$3：当前非自己生成的LSA数目 
告警样例 :`A notification 200425 ID 152 level 6 occurred at 16:02:55 11-24-2011 sent by ZXR10 PFU-0/20/0 
%OSPF% Non self LSAs exceed maximum number.
Non self-originated LSAs has exceeded maximum number:1001(ProcessId:1)` 
引起原因 :OSPF的非自己生成LSA数目超出最大值。 
产生的影响 :不再接收新的LSA，如果在1分钟后非自己生成LSA仍然超出最大值，将切断邻居链接，并清空链路状态数据库。 
处理建议 :检查本端和远端的配置是否错误，如lsa-limit和重分发配置。
Y→步骤2 
N→步骤3 
修改错误配置。 
查看lsa-limit配置是否存在问题：ZXR10(config-ospfv2)#show ip ospf 1
OSPF 1 Router ID 2.2.2.2 enable
Domain ID type 0x5,value 0.0.0.1
Enabled for 16:16:12,Debug on
Number of areas 0, Normal 0, Stub 0, NSSA 0
Number of interfaces 0
Number of neighbors 0
Number of adjacent neighbors 0
Number of virtual links 0
Total number of entries in LSDB 0
Number of ASEs in LSDB 0, Checksum Sum 0x00000000
Number of grace LSAs 0
Number of new LSAs received 0
Number of self-originated LSAs 0
Maximum number of non self-originated LSAs allowed 10000, current number 0
Threshold for sending warning 75%
limit-time 5 minutes, fresh-time 10 minutes
limit-count allowed 5, current limit-count 0
可以使用以下命令修改配置：ZXR10(config-ospfv2)#lsa-limit ?
<1-4294967294>  Max number of non self-generated LSAs can receive 
在远端设备上执行命令show running-config ospf查看是否存在错误的重分配配置：如错误地配置了重分配BGP：ZXR10(config-ospfv2)#show running-config ospf
! <OSPF>
router ospf 1
redistribute bgp-int
!
! </OSPF>
删除重分配BGP配置：ZXR10(config-ospfv2)#no redistribute bgp-int 
检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200426 
告警描述 :OSPF接口状态改变。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Interface state changed.
DisplayResult:Intf $3 in OSPFv3 process $1, $4->$5. (Process:$1;AreaId:$2;IfName:$3)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：改变前的接口状态 
$5：改变后的接口状态 
告警样例 :`A notification 200426 ID 1 level 6 occurred at 10:01:23 09-21-2009 sent by MPU-0/26/0
%OSPF% Interface state changed.
Intf gei-0/1/0/1 in OSPFv3 process 1, DR->DOWN.(AreaId:0.0.0.1)` 
引起原因 :接口Up、接口Down、选举BDR、选举DR等。
产生的影响 :接口状态发生改变。 
处理建议 :检查接口状态改变是否正常。 
Y→结束 
N→步骤2 
请联系中兴通讯技术支持工程师。 
## 200427 
告警描述 :OSPF虚接口状态改变。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual interface state changed.
DisplayResult:Area $1 nbr $2 in $3 process $4, $5->$6.` 
参数说明 :$1：OSPF区域号 
$2：邻居的路由器ID 
$3：协议类型（OSPFv2或OSPFv3） 
$4：OSPF进程号 
$5：改变前的虚接口状态 
$6：改变后的虚接口状态 
告警样例 :`A notification 200427 ID 1 level 6 occurred at 10:01:23 09-21-2009 sent by MPU-0/20/0
%OSPF% Virtual interface state changed.Area 0.0.0.1 nbr 1.1.1.3 in OSPFv3 process 1, 
POINT_TO_POINT->DOWN.` 
引起原因 :接口Up、接口Down。 
产生的影响 :虚链接口状态发生改变。 
处理建议 :检查虚接口状态改变是否正常。 
Y→结束 
N→步骤2 
检查到虚链对端的OSPF路由是否存在。 
Y→步骤3 
N→步骤4 
检查虚链对端在传输区域是否有接口配置了IPv6地址。 
Y→步骤5 
N→步骤4 
排除故障。查看故障是否消除。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 200428 
告警描述 :OSPF邻居状态改变。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Neighbor state changed.
DisplayResult:Nbr $4 on intf $3 in OSPFv3 process $1, $5->$6. (AreaId:$2;Reason:$9)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：邻居的路由器ID 
$5：改变前的邻居状态 
$6：改变后的邻居状态 
$9：错误原因 
告警样例 :`A notification 200428 ID 1 level 6 occurred at 10:01:23 09-21-2009 sent by MPU-0/26/0
%OSPF% Neighbor state changed.Nbr 1.1.1.2 on intf gei-0/1/0/1 in OSPFv3 process 1, 
FULL->DOWN.(AreaId:0.0.0.1;Reason:BfdSessionDown)` 
引起原因 :建立邻居或者删除邻居、BFD断链、收不到邻居的Hello报文或者收到异常报文等。 
产生的影响 :邻居状态发生改变。 
处理建议 :检查邻居状态改变是否正常。 
Y→结束 
N→步骤2 
检查接口收发包是否正常。 
Y→步骤4 
N→步骤3 
排除故障。查看故障是否消除。 
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 200429 
告警描述 :OSPF虚邻居状态改变。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment: Virtual neighbor state changed.
DisplayResult: Area $1 nbr $2 in $3 process $4, $5->$6.` 
参数说明 :$1：OSPF区域号 
$2：邻居的路由器ID 
$3：协议类型（OSPFv2或OSPFv3） 
$4：OSPF进程号 
$5：改变前的虚邻居状态 
$6：改变后的虚邻居状态 
告警样例 :`A notification 200429 ID 1 level 6 occurred at 10:01:23 09-21-2009 sent by MPU-0/20/0
%OSPF% Virtual neighbor state changed.Area 0.0.0.1 nbr 1.1.1.2 in OSPFv3 process 1, FULL->DOWN.` 
引起原因 :建立虚邻居或者删除虚邻居、收不到邻居的Hello报文或者收到异常报文等。 
产生的影响 :虚邻居状态发生改变。 
处理建议 :检查虚邻居状态改变是否正常。 
Y→结束 
N→步骤2 
检查虚链的出接口收发包是否正常。 
Y→步骤5 
N→步骤3 
检查到虚链对端的OSPF路由是否存在。 
Y→步骤5 
N→步骤4 
排除故障。检查故障是否消除。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 200432 
告警描述 :物理接口被删除导致OSPF接口被删除。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment: Delete OSPF interface.
DisplayResult: Intf $1 in $2 process $3.` 
参数说明 :$1：接口名 
$2：协议类型（OSPFv2或OSPFv3） 
$3：OSPF进程号 
告警样例 :`A notification 200432 ID 1 level 6 occurred at 10:01:23 09-21-2009 sent by MPU-0/20/0
%OSPF% Delete OSPF interface.Intf gei-0/1/0/1 in OSPFv3 process 1.` 
引起原因 :退出线卡、删除接口。 
产生的影响 :OSPF接口被删除，邻居断链。 
处理建议 :检查物理接口是否被删除。 
Y→步骤3 
N→步骤2 
检查线卡是否正常。 
Y→步骤4 
N→步骤3 
排除故障。检查故障是否消除。 
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 200434 
告警描述 :OSPFv2邻居数目达到允许上限。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:OSPFv2 adjacency number reached the global threshold.
DisplayResult:(OSPFv2 adjacency number = $1).` 
参数说明 :$1：整机允许的OSPFv2最大邻居数 
告警样例 :告警产生： 
`An alarm 200434 ID 1 level 5 occurred at 01:30:35 01-01-2000 sent by ZXR10 MPU-0/26/0
%OSPF% OSPFv2 adjacency number reached the global threshold. 
(OSPFv2 adjacency number = 2000)` 
告警恢复： 
`An alarm 200434 ID 1 level 5 cleared at 01:30:40 01-01-2000 sent by ZXR10 MPU-0/26/0
%OSPF% OSPFv2 adjacency number reached the global threshold. 
(OSPFv2 adjacency number = 2000)` 
引起原因 :邻居个数达到所允许的OSPFv2邻居最大个数的100%，用于提醒用户性能已满。 
产生的影响 :提醒用户，当前OSPFv2邻居的总数已经达到最大邻居数的百分比，不需要用户处理。使用户能够更好的规划OSPFv2邻居相关配置。 
处理建议 :提示用户，用户无需处理。 
## 200435 
告警描述 :OSPFv2邻居数目达到允许数目的80%。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:OSPFv2 adjacency number reached the percentage of global alarm threshold.
DisplayResult:(Alarm threshold = $1 percent).` 
参数说明 :$1:达到OSPFv2邻居最大个数的比例。 
告警样例 :告警产生： 
`An alarm 200435 ID 1 level 5 occurred at 02:28:33 03-01-2010 sent by MPU-0/20/0
%OSPF% OSPFv2 adjacency number reached the percentage of global alarm threshold.
(Alarm threshold = 80 percent)` 
告警消除： 
`An alarm 200435 ID 1 level 5 cleared at 02:28:33 03-01-2010 sent by MPU-0/20/0
%OSPF% OSPFv2 adjacency number reached the percentage of global alarm threshold.
(Alarm threshold = 80 percent)` 
引起原因 :邻居个数达到所允许的OSPFv2邻居最大个数的80%,用于提醒用户即将性能满。 
产生的影响 :提醒用户，当前OSPFv2邻居的总数已经达到最大邻居数的80%，不需要用户处理。使用户能够更好的规划OSPFv2邻居相关配置。 
处理建议 :提示用户，用户无需处理。 
## 200436 
告警描述 :OSPFv3邻居数目达到允许上限。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:OSPFv3 adjacency number reached the global threshold.
DisplayResult:(OSPFv3 adjacency number = $1).` 
参数说明 :$1：整机允许的OSPFv3最大邻居数 
告警样例 :告警产生： 
`An alarm 200436 ID 1 level 5 occurred at 01:30:35 01-01-2000 sent by ZXR10 MPU-0/26/0
%OSPF% OSPFv3 adjacency number reached the global threshold.
(OSPFv3 adjacency number = 2000)` 
告警恢复： 
`An alarm 200436 ID 1 level 5 cleared at 01:30:40 01-01-2000 sent by ZXR10 MPU-0/26/0
%OSPF% OSPFv3 adjacency number reached the global threshold.
(OSPFv3 adjacency number = 2000)` 
引起原因 :邻居个数达到所允许的OSPFv3邻居最大个数的100%，用于提醒用户性能已满。 
产生的影响 :提醒用户，当前OSPFv3邻居的总数已经达到最大邻居数的百分比，不需要用户处理。使用户能够更好的规划OSPFv3邻居相关配置。 
处理建议 :提示用户，用户无需处理。 
## 200437 
告警描述 :OSPFv3邻居数目达到允许数目的80%。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:OSPFv3 adjacency number reached the percentage of global alarm threshold.
DisplayResult:(Alarm threshold = 80 percent)` 
参数说明 :无 
告警样例 :告警产生： 
`An alarm 200437 ID 1 level 5 occurred at 02:28:33 03-01-2010 sent by MPU-0/26/0
%OSPF%OSPFv3 adjacency number reached the percentage of global alarm threshold.
(Alarm threshold = 80 percent)（NbrCntLimit:2000）` 
告警消除： 
`An alarm 200437 ID 1 level 5 cleared at 02:28:33 03-01-2010 sent by MPU-0/26/0
%OSPF%OSPFv3 adjacency number reached the percentage of global alarm threshold.
(Alarm threshold = 80 percent)（NbrCntLimit:2000）` 
引起原因 :邻居个数达到所允许的OSPFv3邻居最大个数的80%，用于提醒用户即将性能满。 
产生的影响 :提醒用户，当前OSPFv3邻居的总数已经达到最大邻居数的80%，不需要用户处理。使用户能够更好的规划OSPFv3邻居相关配置。 
处理建议 :提示用户，无需用户处理。 
## 200438 
告警描述 :OSPFv2接口对应的某个邻居上有重传报文。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Neighbor retransmit packet.
DisplayResult:Interface $8 on neighbor $4 LS type: 
$5 Advertising Router: $6 Link State ID: $7 (ProcessId:$1;AreaId:$2;IfName:$3)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：接口名 
$4：邻居路由器ID 
告警样例 :`A notification 200438 ID 45 level 6 occurred at 15:26:38 05-03-2017 sent by ZXR10 MPU-0/26/0
%OSPF%Neighbor retransmit packet. On nbr 10.0.0.2 local interface 10.0.0.1
（ProcessId:100;AreaId:0.0.0.1;IfName:gei-0/1/0/1）` 
引起原因 :接口的邻居上报文有重传时通知提醒用户。 
产生的影响 :提醒用户，当OSPFv2邻居上有重传时提醒用户，不需要用户处理。 
处理建议 :提示用户，无需用户处理。 
## 200439 
告警描述 :OSPFv2虚链接口的邻居上有重传报文。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Virtual neighbor retransmit packet.
DisplayResult:Interface $7 on neighbor $3 LS type: $4 Advertising Router: $5 Link State ID: $6 
(ProcessId:$1;TransitAreaId:$2;VirtIfNbrId:$3)` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：邻居路由器ID 
告警样例 :`A notification 200439 ID 45 level 6 occurred at 15:26:38 05-03-2017 sent by ZXR10 MPU-0/26/0
%OSPF%Virtual neighbor retransmit packet. 
On nbr 2.2.2.2 local virtual interface vl(0.0.0.1 To 2.2.2.2)(ProcessId:100）` 
引起原因 :虚链接口的邻居上报文有重传时通知提醒用户。 
产生的影响 :提醒用户，当OSPFv2的虚链邻居上有重传时提醒用户，不需要用户处理。 
处理建议 :提示用户，用户无需处理。 
## 200440 
告警描述 :OSPFv2有LSA新生成。
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Originate LSA.
DisplayResult:Proc Id $1 area $2 LS type: $3 Advertising Router: $4 Link State ID: $5` 
参数说明 :$1：描述新生成LSA三要素的字符串 
告警样例 :`A notification 200440 ID 45 level 6 occurred at 15:26:38 05-03-2017 sent by ZXR10 MPU-0/26/0 
%OSPF% Originate LSA. lsId 10.0.0.1 lsType 2 advRtr 1.1.1.1（ProcessId:100;AreaId:0.0.0.1）` 
引起原因 :OSPFv2有LSA新产生，用于提醒用户。 
产生的影响 :提醒用户，OSPFv2有LSA新产生，不需要用户处理 
处理建议 :提示用户，无需用户处理。 
## 200441 
告警描述 :OSPFv2有LSA flush。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:MaxAge LSA.
DisplayResult:Proc Id $1 area $2 LS type: $3 Advertising Router: $4 Link State ID: $5` 
参数说明 :$1：描述要flush掉的LSA的三要素的字符串 
告警样例 :`A notification 200441 ID 45 level 6 occurred at 15:26:38 05-03-2017 sent by ZXR10 MPU-0/26/0 
%OSPF% MaxAge LSA. Maxage lsa lsId 10.0.0.1 lsType 2 advRtr 1.1.1.1（ProcessId:100;AreaId:0.0.0.1）` 
引起原因 :OSPFv2有LSA要flush，用于提醒用户。 
产生的影响 :提醒用户，OSPFv2有LSA要flush，不需要用户处理。 
处理建议 :提示用户，无需用户处理。 
## 200442 
告警描述 :OSPF邻居down。 
默认级别 :4 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Neighbor state changed.
DisplayResult:(NeighborID:$4;Interface:$3;State:$5->$6;ProcessId:$1;AreaId:$2;Reason:$7).` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：本地接口名称 
$4：邻居路由器ID 
$5：改变前的邻居状态 
$6：改变后的邻居状态 
$7：错误原因 
告警样例 :告警产生： 
`An alarm 200442 ID 528 level 4 occurred at 17:40:54 11-29-2019 sent by ZXR10 MPU-0/26/0
%OSPF%Neighbor state changed.  
(NeighborID:0.0.0.2;Interface:gei-0/1/0/4;State:Full->Down;Reason:BfdSessionDown).` 
告警恢复： 
`An alarm 200442 ID 528 level 4 cleared at 17:40:55 11-29-2019 sent by ZXR10 MPU-0/26/0
%OSPF%Neighbor state changed.  
(NeighborID:0.0.0.2;Interface:gei-0/1/0/4;State:Full->Down;Reason:BfdSessionDown).` 
引起原因 :OSPF接口down或者邻居关系超时。 
产生的影响 :OSPF邻居down。 
处理建议 :请检查报文收发情况、邻居状态改变是否down、是否出现异常。 
Y→步骤2 
N→步骤3 
分析以上事件的原因是否因人为操作引起。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200443 
告警描述 :OSPF虚链邻居down。 
默认级别 :4 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Virtual neighbor state changed.
DisplayResult:(NeighborID:$3;Interface:$4;State:$5->$6;ProcessId:$1;TransitAreaId:$2;Reason:$7).` 
参数说明 :$1：OSPF进程号 
$2：OSPF区域号 
$3：邻居路由器ID 
$4：本地接口名称 
$5：改变前的邻居状态 
$6：改变后的邻居状态 
$7：错误原因 
告警样例 :告警产生： 
`An alarm 200443 ID 529 level 4 occurred at 17:40:54 11-29-2019 sent by ZXR10 MPU-0/26/0
%OSPF%Virtual neighbor state changed.(NeighborID:0.0.0.2;Interface:OSPF_VL0;
State:Full->Down;ProcessId:10;TransitAreaId:0.0.0.1;Reason:DeadTimerExpire).` 
告警恢复： 
`An alarm 200443 ID 529 level 4 cleared at 17:40:55 11-29-2019 sent by ZXR10 MPU-0/26/0
%OSPF% Virtual neighbor state changed.(NeighborID:0.0.0.2;Interface:OSPF_VL0;
State:Full->Down;ProcessId:10;TransitAreaId:0.0.0.1;Reason:DeadTimerExpire).` 
引起原因 :OSPF接口down或者邻居从FULL回退到two way。 
产生的影响 :OSPF虚链邻居down。 
处理建议 :请检查报文收发情况、虚链邻居状态改变是否down、是否出现异常。 
Y→步骤2 
N→步骤3 
分析以上事件的原因是否因人为操作引起。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
# PBR 
## 150203 
告警描述 :Route-map发生改变。 
默认级别 :7 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:Route-map changed.
DisplayResult:The valid set of route-map $1 seq $2 changed,old valid set is $3,new valid set is $4.
` 
参数说明 :$1： route-map名称 
$2：seq编号 
$3：原来集合名称 
$4：新集合名称 
告警样例 :`A notification 150203 ID 26 level 7 occurred at 00:00:00 01-01-2000 sent by ZXR10 PFU-0/20/0
%ACL% Route-map changed.  The valid set of route-map 1 seq 2 changed,old valid set is 3,new valid set is 4.` 
引起原因 :Route-map配置发生变化。 
产生的影响 :无。 
处理建议 :无。 
# PIM 
## 200101 
告警描述 :PIM邻居Down。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:PIM neighbor changed.
DisplayResult:PIM$1 neighbor $2 $4 on interface $3. Reason: $5.` 
参数说明 :$1：PIM VRF名称 
$2：邻居地址 
$3：接口名 
$4：邻居状态 
$5：邻居变化原因 
告警样例 :告警产生： 
`An alarm 200101 ID 1 level 5 occurred at 09:05:15 10-27-2009 sent by MPU-0-26-0
%PIM% PIM neighbor changed.  PIM neighbor 4.4.4.4 down on interface gei_0/1/0/1.` 
告警恢复： 
`An alarm 200101 ID 2 level 5 cleared at 09:05:15 10-27-2009 sent by MPU-0-26-0
%PIM% PIM neighbor changed.  PIM neighbor 4.4.4.4 up on interface gei_0/1/0/1.` 
引起原因 :可能是对端接口no pimsm或no pimdm。 
有可能是对端接口地址改变。 
有可能是配置了neighbor filter（邻居过滤）。 
接口的管理状态或物理状态为Down。 
产生的影响 :相应邻居消失。 
处理建议 :执行命令[show running-config multicast]检查接口是否配置了[no pimsm]或[no pimdm]：
Y→步骤2 
N→步骤3 
在接口上配置pimsm或pimdm，完成后，检查告警是否恢复。
Y→结束 
N→步骤3 
执行命令[show ip interface brief]检查接口的物理状态是否是down。
Y→步骤4 
N→步骤5 
检查线路和接口，排除接口和链路物理故障，完成后，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 200102 
告警描述 :接口Down。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:PIM interface changed. 
DisplayResult:PIM$1 interface $2 changed state to $3. Reason: $4.` 
参数说明 :$1:PIM vrf名称 
$2:接口名 
$3:接口状态 
$4:接口变化原因 
告警样例 :告警产生： 
`An alarm 200102 ID 2 level 5 occurred at 08:09:52 02-26-2010 sent by MPU-0/20/0
%PIM% PIM interface changed!  PIM interface loopback1 changed state to down!` 
告警恢复： 
`An alarm 200102 ID 2 level 5 cleared at 08:10:53 02-26-2010 sent by MPU-0/20/0
%PIM% PIM interface changed!  PIM interface loopback1 changed state to up!` 
引起原因 :可能是接口的管理状态或物理状态为Down。 
产生的影响 :相应组播接口消失。 
处理建议 :执行命令[show running-config multicast]检查接口是否配置了[no pimsm]或[no pimdm]：
Y→步骤2 
N→步骤3 
在接口上配置pimsm或pimdm，完成后，检查告警是否恢复。
Y→结束 
N→步骤3 
执行命令[show ip interface brief]检查接口的物理状态是否是down。
Y→步骤4 
N→步骤5 
检查线路和接口，排除接口和链路物理故障，完成后，检查告警是否恢复。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 200103 
告警描述 :某接口地址改变。 
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment: PIM address change!
DisplayResult: PIM$1 address change from $2 to $3 on interface $4!` 
参数说明 :$1：PIM VRF名称 
$2：接口原来地址 
$3：接口现在地址 
$4：接口名 
告警样例 :`A notification 200103 ID 1 level 6 occurred at 02:20:35 02-27-2010 sent by MPU-0/20/0
%PIM% PIM address change!  PIM address change from 5.5.5.5 to 0.0.0.0 on interface loopback1!` 
引起原因 :接口地址被更改。 
产生的影响 :接口上配置的相关功能出现变化。 
处理建议 :检查是否配置了[ip address]。
Y→步骤3 
N→步骤2 
检查是否配置了[no ip addresss]。
Y→步骤3 
N→步骤4 
执行命令[show ip pim interface]查看接口地址变化是否改变了DR的优先级；执行命令[show ip pim rp mapping]查看RP是否变化。
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 200104 
告警描述 :某接口上DR改变。
默认级别 :6 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :通知 
告警描述原型 :`Comment:PIM DR changed. 
DisplayResult:PIM$1 DR changed from $2 to $3 on interface $4. Reason: $5.` 
参数说明 :$1:PIM vrf名称 
$2:接口原来DR地址 
$3:接口现在DR地址 
$4:接口名 
$5:DR变化原因 
告警样例 :`A notification 200104 ID 1 level 6 occurred at 02:20:35 02-27-2010 sent by MPU-0/20/0
%PIM% PIM DR changed!  PIM DR change from 0.0.0.0 to 5.5.5.6 on interface loopback1!` 
引起原因 :修改了PIM-SM配置。 
修改了接口的IP地址。 
修改了DR的优先级。 
产生的影响 :可能引起DR变化。 
处理建议 :检查是否刚配置了[pimsm]或[pimdm]，或者[no pimsm]或[no pimdm]。
Y→结束 
N→步骤2 
检查是否刚修改接口的地址，配置[ip address]或[no ip
address]。
Y→结束 
N→步骤3 
检查是否刚改变了DR的优先级，配置了[dr-priority]。
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 200105 
告警描述 :静态RP删除。
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:PIM Static RP changed.
DisplayResult:PIM$1 static-RP $2 has been $3.` 
参数说明 :$1:PIM vrf名称 
$2:静态RP地址 
$3:静态RP状态 
告警样例 :告警产生： 
`An alarm 200105 ID 1 level 5 occurred at 02:25:56 02-27-2010 sent by MPU-0/20/0
%PIM% PIM Static RP changed!  PIM static-RP 1.1.1.1 has been removed!` 
告警恢复： 
`An alarm 200105 ID 2 level 5 cleared at 02:26:09 02-27-2010 sent by MPU-0/20/0
%PIM% PIM Static RP changed!  PIM static-RP 1.1.1.1 has been added!` 
引起原因 :静态RP被删除。 
配置了rp-smart命令 
静态RP的下一跳发生变化。 
产生的影响 :可能引起RP改变。 
处理建议 :执行命令[show running-config multicast]检查是否删除了静态RP。
Y→步骤2 
N→步骤3 
配置静态RP，完成后，检查告警是否恢复。 
Y→结束 
N→步骤3 
执行命令[show running-config multicast]检查是否配置了[rp-smart]。
Y→步骤4 
N→步骤5 
配置no rp-smart，完成后，检查告警是否恢复。
Y→结束 
N→步骤5 
执行命令[show ip pim nexthop]检查到静态RP的下一跳是否改变。
Y→步骤6 
N→步骤7 
恢复原先的下一跳，完成后，检查告警是否恢复。 
Y→结束 
N→步骤7 
请联系中兴通讯技术支持工程师。 
## 200106 
告警描述 :接口上候选RP被删除。 
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:PIM Candidate RP changed.
DisplayResult:PIM$1 candidate-RP $2 has been $3.` 
参数说明 :$1:PIM vrf名称 
$2:IPv4是CRP接口名，IPv6是CRP地址 
$3:CRP状态 
告警样例 :告警产生： 
`An alarm 200106 ID 1 level 5 occurred at 02:27:28 02-27-2010 sent by MPU-0/20/0
%PIM% PIM Candidate RP changed!  PIM candidate-RP on interface loopback1 has been removed!` 
告警恢复： 
`An alarm 200106 ID 2 level 5 cleared at 02:27:31 02-27-2010 sent by MPU-0/20/0
%PIM% PIM Candidate RP changed!  PIM candidate-RP on interface loopback1 has been added!` 
引起原因 :接口上候选RP被删除。 
产生的影响 :可能引起RP改变。 
处理建议 :执行命令[show running-config multicast]检查是否删除了这个动态RP。
Y→步骤2 
N→步骤3 
配置这个动态RP，完成后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200107 
告警描述 :接口上候选BSR被删除。
默认级别 :5 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:PIM Candidate BSR changed.
DisplayResult:PIM$1 candidate-BSR $2 has been $3.` 
参数说明 :$1:PIM vrf名称 
$2:IPv4是CBSR接口名，IPv6是CBSR地址 
$3:CBSR状态 
告警样例 :告警产生： 
`An alarm 200107 ID 1 level 5 occurred at 02:29:04 02-27-2010 sent by MPU-0/20/0
%PIM% PIM Candidate BSR changed!  PIM candidate-BSR on interface loopback1 has been removed!` 
告警恢复： 
`An alarm 200107 ID 2 level 5 cleared at 02:29:10 02-27-2010 sent by MPU-0/20/0
%PIM% PIM Candidate BSR changed!  PIM candidate-BSR on interface loopback1 has been added!` 
引起原因 :接口上候选BSR被删除。 
产生的影响 :可能引起BSR改变。 
处理建议 :执行命令[show running-config multicast]检查是否删除了这个候选BSR：
Y→步骤2 
N→步骤3 
配置这个候选BSR，完成后，检查告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
# PORT_GROUP 
## 240501 
告警描述 :复用段保护倒换。 
默认级别 :3 
告警恢复 :是 
告警类型 :设备告警 
告警类别 :倒换事件 
告警描述原型 :`Comment: Port group switch event
DisplayResult: Port group $1 switching to state: $2, reason: $3
` 
参数说明 :$1：发生倒换的端口保护组号 
$2：倒换的状态 
$3：当前倒换状态产生原因 
告警样例 :倒换事件产生： 
`A protected event 240501 ID 29 level 3 occurred at 06:25:57 12-27-2012 sent by ZXR10 MPU-0/20/0
%PORT-GROUP% Port group switch event. Port group 1 switching to state: switched, 
reason: SF on working
` 
倒换事件更新（更新有多种，只列举一例）： 
`A protected event 240501 ID 32 level 3 changed at 06:26:38 12-27-2012 sent by ZXR10 MPU-0/20/0
%PORT-GROUP% Port group switch event. Port group 1 switching to state: switched, 
reason: manual switch
` 
倒换事件消失： 
`A protected event 240501 ID 32 level 3 cleared at 06:26:38 12-27-2012 sent by ZXR10 MPU-0/20/0
%PORT-GROUP% Port group switch event  Port group 1 switching to state: no switch, 
reason: no request` 
引起原因 :主端口出现故障或者APS模式下进行了手动切换。 
产生的影响 :流量由主端口切换到备端口上。 
处理建议 :执行命令[show port-group all]，查看主端口的协议状态是否Down或检测状态是否是SF。
Y→步骤4 
N→步骤2 
执行命令[show aps]检查switch cmd是否是null。
Y→步骤3 
N→步骤4 
在APS命令模式下执行命令[aps switch clear]清除，检查告警是否清除。
Y→结束 
N→步骤4 
请联系中兴通讯技术支持工程师。 
## 240502 
告警描述 :MCAPS保护组的主备设备配置不同。 
默认级别 :5 
告警恢复 :否 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:MC-APS configuration.
DisplayResult:The master and slave configuration of MC-APS group $1 is different.` 
参数说明 :$1：端口保护组号 
告警样例 :告警产生： 
`An alarm 240502 ID 1 level 5 occurred at 15:47:39 04-28-2013 sent by ZXR10 MPU-0/20/0
%PORT-GROUP% MC-APS configuration.The master and slave configuration of MC-APS 
group 100 is different` 
告警恢复： 
`An alarm 240502 ID 1 level 5 cleared at 15:47:39 04-28-2013 sent by ZXR10 MPU-0/20/0
%PORT-GROUP% MC-APS configuration.The master and slave configuration of MC-APS 
group 100 is different` 
引起原因 :MCAPS保护组的主备设备配置不同。 
产生的影响 :可能导致用户配置的主备保护无法实现。 
处理建议 :重新配置，使MCAPS保护组的主备设备配置相同，检查告警是否清除。 
Y→结束 
N→步骤2 
请联系中兴通讯技术支持工程师。 
# RIB 
## 200320 
告警描述 :路由数超过阈值。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Count of IPv4 RIB reached the warning threshold.
DisplayResult:(Current count=$1; Threshold=$2%)` 
参数说明 :$1：当前整机路由数目 
$2: 设定的告警阈值（百分比） 
告警样例 :IPv4 路由总数达到80%告警： 
`An alarm 200320 ID 10 level 5 occurred at 12:38:57 02-28-2019 sent by ZXR10 MPU-0/20/0
%RIB% Count of IPv4 RIB reached the warning threshold.  (Current=16; Threshold=80%)` 
IPv4 路由总数达到80%告警消除： 
`An alarm 200320 ID 10 level 5 cleared at 12:39:16 02-28-2019 sent by ZXR10 MPU-0/20/0
%RIB% Count of IPv4 RIB reached the warning threshold.  (Current=15; Threshold=80%)` 
引起原因 :整机路由总数高于门限。 
产生的影响 :提示用户路有数已达上限，可能影响服务质量。 
处理建议 :使用show running-config route-protocol-mgr命令，查看是否配置了RIB告警门限。 
Y→步骤2 
N→步骤3 
根据实际情况修改扩大告警门限值或删除部分路由（修改门限的命令为ipv4-rib usage-rate threshold
<percent-value>），检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 200321 
告警描述 :路由数超过阈值。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Count of IPv6 RIB reached the warning threshold.
DisplayResult:(Current count=$1; Threshold=$2%)` 
参数说明 :$1：当前整机路由数目 
$2: 设定的告警阈值（百分比） 
告警样例 :IPv6 路由总数达到80%告警： 
`An alarm 200321 ID 10 level 5 occurred at 12:38:57 02-28-2019 sent by ZXR10 MPU-0/20/0
%RIB% Count of IPv6 RIB reached the warning threshold.  (Current=16; Threshold=80%)` 
IPv6 路由总数达到80%告警消除： 
`An alarm 200321 ID 10 level 5 cleared at 12:39:16 02-28-2019 sent by ZXR10 MPU-0/20/0
%RIB% Count of IPv6 RIB reached the warning threshold.  (Current=15; Threshold=80%)` 
引起原因 :整机路由总数高于门限。 
产生的影响 :提示用户路有数已达上限，可能影响服务质量。 
处理建议 :使用show running-config route-protocol-mgr命令，查看是否配置了RIB告警门限。 
Y→步骤2 
N→步骤3 
根据实际情况修改扩大告警门限值或删除部分路由（修改门限的命令为ipv6-rib usage-rate threshold
<percent-value>），检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
# SECTION_GROUP 
## 240405 
告警描述 :section保护组失效。 
默认级别 :3 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Section group invalid.
DisplayResult:Section group $1 invalid.` 
参数说明 :$1：段保护组ID 
告警样例 :告警产生： 
`An alarm 240405 ID 339 level 3 occurred at 10:02:30 04-10-2017 sent by ZXR10 MPU-0/20/0
%SECTION-GROUP% Section group invalid. Section group 1 invalid.` 
告警恢复： 
`An alarm 240405 ID 256 level 3 cleared at 10:02:34 04-10-2017 sent by ZXR10 MPU-0/20/0
%SECTION-GROUP% Section group invalid. Section group 1 invalid.` 
引起原因 : 东/西向section均SF。 

东/西向section配置不完整。 
产生的影响 :section保护组失效可能会引起环网保护失效。 
处理建议 :提示用户，检查当前段实体是否正常或者配置是否完整。 
# SYSTEM 
## 350301 
告警描述 :设备上当前告警数量超过阈值。 
默认级别 :3 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment: Number of current alarms in the equipment reaches the threshold.
DispalyResult: $1% of the capacity of current alarm database is occupied, the records 
in current alarm database is $2, and the capacity is $3.` 
参数说明 :$1：当前告警占用告警的百分比 
$2：当前告警的数量 
$3：当前告警库的容量 
告警样例 :告警产生： 
`An alarm 350301 ID 1 level 3 occurred at 15:47:39 04-28-2013 sent by ZXR10 MPU-0/20/0
%SYSTEM% Number of current alarms in the equipment reaches the threshold.90% of the 
capacity of current alarm database is occupied, the records in current alarm database 
is 4506, and the capacity is 5000.` 
告警恢复： 
`An alarm 350301 ID 1 level 3 cleared at 15:47:39 04-28-2013 sent by ZXR10 MPU-0/20/0
%SYSTEM% Number of current alarms in the equipment reaches the threshold.84% of the 
capacity of current alarm database is occupied, the records in current alarm database 
is 4249, and the capacity is 5000.` 
引起原因 :设备上当前告警数量超过阈值。 
产生的影响 :在没有告警恢复的情况下，继续有告警上报有可能会被丢弃。同时，告警指示灯可能会发生故障。 
处理建议 :执行命令[show alarm current]，查看是否存在当前告警，并且数量超过本告警的恢复阀值。
Y→步骤2 
N→步骤3 
处理当前告警池中的告警，使之恢复。当前告警池告警数量低于本告警的恢复阀值之后，查看本告警是否恢复。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 350304 
告警描述 :发送告警心跳。 
默认级别 :6 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:Send heartbeat.
DisplayResult:Send heartbeat msg to $1.` 
参数说明 :$1：告警心跳消息发送的终端类型 
告警样例 :`A notification 350304 ID 9 level 6 occurred at 17:02:52 05-16-2017 sent by ZXR10 MPU-0/20/0
%SYSTEM% Send heartbeat. Send heartbeat msg to CONSOLE.` 
引起原因 :发送告警心跳消息到指定终端。 
产生的影响 :已发送过告警心跳消息。 
处理建议 :用户无需处理。 
## 350305 
告警描述 :告警日志缓冲区使用超过阈值。 
默认级别 :4 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Buffer occupied reaches the threshold.
DisplayResult:(Percentage:$1;Occupancy:$2 bytes)` 
参数说明 :$1：当前已使用的日志缓冲百分比 
$2：当前已使用的日志缓冲字节 
告警样例 :告警产生： 
`An alarm 350305 ID 16 level 4 occurred at 09:33:56 04-30-2020 sent by ZXR10 MPU-0/20/0
%SYSTEM% Buffer occupied reaches the threshold.  (Percentage:87;Occupancy:89668 bytes)
` 
告警消失： 
`An alarm 350305 ID 16 level 4 cleared at 09:35:56 04-30-2020 sent by ZXR10 MPU-0/20/0 
%SYSTEM% Buffer occupied reaches the threshold. (Percentage:85;Occupancy:79668 bytes)` 
引起原因 :告警日志缓冲区使用超过使用阈值。 
产生的影响 :提示用户告警日志缓冲区设置的阈值，可能导致告警日志记录频率提高。 
处理建议 :执行[show running-config alarm all]命令查看当前的告警日志缓冲是否偏小。
Y→步骤2 
N→步骤3 
在告警日志策略下使用[buffer]命令，调整告警日志buffer到合适值，查看告警是否消失。
Y→结束 
N→步骤3 
使用[show running-config alarm all]命令，查看当前的告警日志缓冲区阈值是否偏小。
Y→步骤4 
N→步骤5 
在告警日志策略下使用[alarm-threshold]命令，调整告警日志缓冲区阈值到合适值，查看告警是否消失。
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 360105 
告警描述 :加载配置失败。 
默认级别 :4 
告警恢复 :是 
告警类型 :处理错误告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Loading configuration failed.
DisplayResult:(CfgType:$1;Result:$2;ErrorIn:$3)` 
参数说明 :$1：配置类型 
$2：结果 
$3：错误信息 
告警样例 :`An alarm 360105 ID 4 level 4 occurred at 01:38:08 01-16-2020 sent by ZXR10 MPU-0/20/0
%SYSTEM% Loading configuration failed.  (CfgType:text;Result:fail;ErrorIn:startrun.dat)` 
或 
`An alarm 360105 ID 4 level 4 occurred at 01:38:08 01-16-2020 sent by ZXR10 MPU-0/20/0
%SYSTEM% Loading configuration failed.  (CfgType:binary;Result:fail;ErrorIn:.zdb)` 
引起原因 :startrun.dat或.zdb配置文件遭到破坏。 
startrun.dat或.zdb配置文件没有读取成功。 
设备上电失败导致读取文件失败。 
产生的影响 :该告警会导致当前系统没有恢复上次设备上ZDB文件中保存的配置数据，导致数据恢复失败。 
处理建议 :是否允许删除原来的配置文件，空配置重新启动设备： 
Y→步骤2 
N→步骤3 
使用删除命令删除ZDB配置文件。 
采用以下两种方法之一恢复数据： 

将配置相同的设备上的ZDB文件替换到故障设备上的ZDB文件。把主控板上面的/sysdisk0/config/DATA0和DATA1中的_MIM_RDB_.ZDB替换新的ZDB文件，设备断电，重新启动。 
网管下载数据到设备上，重新生成ZDB文件，恢复数据。 
用户终端下发配置命令，检查告警是否清除： 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
TCP :## 100121 
告警描述 :TCP链接收到大量攻击报文。 
默认级别 :5 
告警恢复 :否 
告警类型 :通信告警 
告警类别 :通知 
告警描述原型 :`Comment:TCP connection being attacked.
DisplayResult:$1.` 
参数说明 :$1：攻击原因 
告警样例 :`A notification 100121 level 5 occurred at 07:56:24 05-11-2010 sent by MPU-0/20/0
%TCP% TCP connection being attacked.  ( addresss = TCB[local 10.40.156.163:2000,
remote 10.40.50.131:2107]Connection is attacked for receiving lots of white 
list packets )` 
引起原因 :TCP持续收到大量白名单攻击报文。 
产生的影响 :大量TCP白名单攻击报文上送控制面，可能导致主控CPU冲高，进一步影响TCP正常报文收发和其他协议报文的正常收发，继而影响TCP连接及其他协议的稳定性。 
处理建议 :提示用户收到大量攻击报文，供用户参考。 
## 100122 
告警描述 :当前CPU的TCP代理连接个数即将达到上限。 
默认级别 :5 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:TCP proxy connections will overflow.
DisplayResult:$1.` 
参数说明 :$1:TCP代理连接个数是否达到阈值 
告警样例 :告警产生： 
`An alarm 100122 ID 32 level 2 occurred at 07:47:05 04-08-2013 sent by ZXR10 MPU-0/20/0 
%TCP%The percent of current TCP connections has reached the threshold(80%)` 
告警恢复： 
`An alarm 100122 ID 32 level 2 cleared at 07:47:05 04-08-2013 sent by ZXR10 MPU-0/20/0 
%TCP%The percent of current TCP connections is lower than the threshold(80%)` 
引起原因 :流量过载导致TCP代理连接个数即将达到上限。 
产生的影响 :不能建立新的TCP连接。 
处理建议 :提示用户。 
# TUNNEL_GROUP 
## 240401 
告警描述 :隧道倒换事件。 
默认级别 :3 
告警恢复 :根据翻转模式确定是否有告警消失。 
告警类型 :设备告警 
告警类别 :倒换事件 
告警描述原型 :`Comment:Tunnel group switch event.
DisplayResult:Tunnel group $1 switching to state: $2, reason: $3$4.` 
参数说明 :$1：发生倒换的隧道保护组ID 
$2：倒换的状态 
$3：当前倒换状态产生原因 
$4：翻转模式，分为翻转和非翻转 
告警样例 :倒换事件产生： 
`A protected event 240401 ID 427 level 3 occurred at 12:49:32 10-23-2012 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP% Tunnel group switch event. Tunnel group 1026 switching to state: switched, 
reason: SF on working, revert mode: revertive.` 
倒换事件消失： 
`A protected event 240401 ID 453 level 3 cleared at 12:51:36 10-23-2012 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP% Tunnel group switch event. Tunnel group 1024 switching to state: no switch, 
reason: no request.` 
非倒换事件产生： 
`A protected event 240401 ID 340 level 3 occurred at 07:33:58 10-24-2012 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP% Tunnel group switch event. Tunnel group 1026 switching to state: no switch, 
reason: lockout of protecton.` 
引起原因 :隧道保护组工作隧道或者保护隧道，检测出链路信号中断或者信号衰减，导致的切换或回切。 
配置手工切换命令导致的切换回切。 
产生的影响 :导致业务转发路径发生切换。 
处理建议 :检查是否是人为配置手工切换导致的告警。 
Y→结束 
N→步骤2 
排除链路中存在的故障，检查告警是否清除。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 240403 
告警描述 :设备TUNNEL-GROUP数量超出告警阈值。 
默认级别 :5 
告警恢复 :是 
告警类型 :质量服务告警 
告警类别 :普通告警 
告警描述原型 :`Comment:The number of tunnel group reached the percentage of global alarm threshold.
DisplayResult:(Alarm threshold = $1 percent).` 
参数说明 :$1：告警阈值 
告警样例 :告警产生： 
`An alarm 240403 ID 357 level 5 occurred at 10:32:30 04-10-2017 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP%The number of tunnel group reached the percentage of global alarm threshold.
(Alarm threshold = 80 percent).` 
告警恢复： 
`An alarm 240403 ID 357 level 5 cleared at 10:32:30 04-10-2017 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP%The number of tunnel group reached the percentage of global alarm threshold.
(Alarm threshold = 75 percent).` 
引起原因 :设备上存在的隧道保护组已经超出容量告警阈值。 
产生的影响 :设备上隧道保护组数量过多，可能会降低性能。 
处理建议 :提示用户，不需要用户处理。 
## 240404 
告警描述 :隧道保护组失效。 
默认级别 :3 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :普通告警 
告警描述原型 :`Comment:Tunnel group invalid.
DisplayResult:Tunnel group $1 invalid.` 
参数说明 :$1：隧道保护组ID 
告警样例 :告警产生： 
`An alarm 240404 ID 357 level 3 occurred at 10:32:30 04-10-2017 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP% Tunnel group invalid. Tunnel group 1 invalid.` 
告警恢复： 
`An alarm 240404 ID 357 level 3 cleared at 10:32:46 04-10-2017 sent by ZXR10 MPU-0/20/0
%TUNNEL-GROUP% Tunnel group invalid. Tunnel group 1 invalid.` 
引起原因 : 切换后，备隧道SF。 

回切后，主隧道SF。 

主备隧道均SF。 

保护组主、备隧道配置不完整。 
产生的影响 :隧道保护组失效可能会引起经过隧道的业务断流。 
处理建议 :提示用户，检查当前隧道实体是否正常或者配置是否完整。 
# TWAMP 
## 300912 
告警描述 :丢包率越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Frame loss ratio threshold crossed of TWAMP.
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300912 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Frame loss ratio threshold crossed of TWAMP.(ConnectionId=1,SessionId=2,SourceIP 
=1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<586-desricp> 15m low alarm occur. 
Low thres is 0.1. Current value is: 0.2. ` 
告警恢复： 
`An alarm 300912 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Frame loss ratio threshold crossed of TWAMP.(ConnectionId=1,SessionId=2,SourceIP 
=1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<586-desricp> 15m low alarm occur. 
Low thres is 0.1. Current value is: 0. ` 
引起原因 :链路阻塞。 
端口出现光衰。 
产生的影响 :链路出现丢包情况。 
处理建议 :检查该链路是否出现阻塞。 
Y→步骤3 
N→步骤2 
检查端口是否出现光衰。 
Y→步骤4 
N→步骤5 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤2 
排除端口光衰，检查告警是否消失。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 300913 
告警描述 :双向时延越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Bidirectional delay threshold crossed of TWAMP (unit:ns).
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300913 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Bidirectional delay threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<662-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. ` 
告警恢复： 
`An alarm 300913 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Bidirectional delay threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<662-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000. ` 
引起原因 :链路阻塞。 
产生的影响 :链路双向时延过大。 
处理建议 :检查该链路是否出现阻塞。 
Y→步骤2 
N→步骤3 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 300914 
告警描述 :双向时延变化越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Bidirectional delay variation threshold crossed of TWAMP (unit:ns).
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300914 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP%Bidirectional delay variation threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<662-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. ` 
告警恢复： 
`An alarm 300914 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Bidirectional delay variation threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<662-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000. ` 
引起原因 :链路阻塞。 
产生的影响 :链路双向时延变化过大。 
处理建议 :检查该链路是否出现阻塞。 
Y→步骤2 
N→步骤3 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤3 
请联系中兴通讯技术支持工程师。 
## 300915 
告警描述 :前向时延越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Forward delay threshold crossed of TWAMP (unit:ns).
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300915 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Forward delay threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. ` 
告警恢复： 
`An alarm 300915 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Forward delay threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000. ` 
引起原因 :时钟不同步 
链路阻塞。 
产生的影响 :链路前向时延过大。 
处理建议 :检查时钟是否同步。 
Y→步骤2 
N→步骤3 
检查该链路是否出现阻塞。 
Y→步骤4 
N→步骤5 
排除时钟同步，检查告警是否消失。 
Y→结束 
N→步骤2 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 300916 
告警描述 :前向时延变化越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Forward delay variation threshold crossed of TWAMP (unit:ns).
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300916 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Forward delay threshold variation  crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. ` 
告警恢复： 
`An alarm 300916 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Forward delay variation  threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000. ` 
引起原因 :时钟不同步 
链路阻塞。 
产生的影响 :链路前向时延变化过大。 
处理建议 :检查时钟是否同步。 
Y→步骤2 
N→步骤3 
检查该链路是否出现阻塞。 
Y→步骤4 
N→步骤5 
排除时钟同步，检查告警是否消失。 
Y→结束 
N→步骤2 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 300917 
告警描述 :反向时延越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Reverse delay threshold crossed of TWAMP (unit:ns).
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300917 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Reverse delay threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. 
` 
告警恢复： 
`An alarm 300917 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Reverse delay threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000.  ` 
引起原因 :时钟不同步 
链路阻塞。 
产生的影响 :链路反向时延过大。 
处理建议 :检查时钟是否同步。 
Y→步骤2 
N→步骤3 
检查该链路是否出现阻塞。 
Y→步骤4 
N→步骤5 
排除时钟同步，检查告警是否消失。 
Y→结束 
N→步骤2 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
## 300918 
告警描述 :反向时延变化越限。 
默认级别 :2 
告警恢复 :是 
告警类型 :通信告警 
告警类别 :性能告警 
告警描述原型 :`Comment:Reverse delay variation threshold crossed of TWAMP (unit:ns).
DisplayResult:(ConnectionId=$8,SessionId=$9,SourceIP =$10,DestinationIP=$11,
VrfName=$13,Dscp=$12).` 
参数说明 :$8：TWAMP控制链接ID 
$9：控制连接上测试会话ID 
$10：源IP地址 
$11：目的IP地址 
$13：VRF名称 
$12：DSCP优先级 
告警样例 :告警产生： 
`An alarm 300918 1 ID 164 level 2 occurred at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Reverse delay threshold variation  crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm occur. High thres is 10000000. Current value is: 20000000. ` 
告警恢复： 
`An alarm 300918 1 ID 164 level 2 cleared at 01:14:45 01-01-2010 sent by ZXR10 MPU-0/20/0
%TWAMP% Reverse delay variation  threshold crossed of TWAMP (unit:ns).(ConnectionId=1,
SessionId=2,SourceIP =1.1.1.1,DestinationIP=1.1.1.2,VrfName=abc,Dscp=0).<587-desricp> 
15m high alarm disappear. High thres is 10000000. Current value is: 100000. ` 
引起原因 :时钟不同步 
链路阻塞。 
产生的影响 :链路反向时延变化过大。 
处理建议 :检查时钟是否同步。 
Y→步骤2 
N→步骤3 
检查该链路是否出现阻塞。 
Y→步骤4 
N→步骤5 
排除时钟同步，检查告警是否消失。 
Y→结束 
N→步骤2 
排除出链路阻塞，检查告警是否消失。 
Y→结束 
N→步骤5 
请联系中兴通讯技术支持工程师。 
 缩略语 
 缩略语 
# ARP 
Address Resolution Protocol地址解析协议
# BDR 
Backup Designate Router备用指定路由器
# BFD 
Bidirectional Forwarding Detection双向转发检测
# BGP 
Border Gateway Protocol边界网关协议
# BSR 
Bootstrap Router自举路由器
# CRC 
Cyclic Redundancy Check循环冗余校验
# DPD 
Dead Peer Detect对等体死亡检测
# DR 
Designated Router指定路由器
# ECMP 
Equal-Cost Multi-Path routing等价多路由
# FRR 
Fast Reroute快速重路由
# GR 
Graceful Restart优雅重启
IP :Internet Protocol因特网协议
# LDP 
Label Distribution Protocol标记分发协议
# LSA 
Link State Advertisement链路状态广播
# LSP 
Label Switched Path标签交换路径
# MAC 
Media Access Control媒介接入控制
# MSDP 
Multicast Source Discovery Protocol组播源发现协议
# MTU 
Maximum Transfer Unit最大传输单元
# OSPF 
Open Shortest Path First开放最短路径优先
# RP 
Rendezvous Point汇聚点
TCP :Transmission Control Protocol传输控制协议
# VRF 
Virtual Route Forwarding虚拟路由转发
