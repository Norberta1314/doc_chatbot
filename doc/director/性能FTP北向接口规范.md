# 性能FTP北向接口规范 
## 范围 
TECS_Director_Performance_FTP_Northbound_Interface_Specifications 
本规范定义了一个标准的FTP性能北向接口，TECS Director向更高级别的上级网管系统提供该接口。
本规范适用于TECS Director—上级网管系统之间的交互设计。
## FTP性能北向接口规范 
### 文件访问方式 
TECS Director支持如下访问方式：
在TECS Director部署FTP服务，存储数据文件，上级网管系统作为FTP客户端通过GET操作到TECS Director取文件。 
在上级网管系统部署FTP服务，TECS Director作为FTP客户端向服务端上传数据文件，最多支持向4个FTP服务端上传数据文件。 
### 文件存储路径 
当服务器位置选择本地时，文件存储路径为： 
非PVC部署：/paasdata/op-comsrv/data/FTPv3/ftp-director/data/ztepm/PM
PVC部署：/glusterdata/volumedata/service/opcs/<卷集ID>/data/ztepm/PM
其中卷集ID为ftp-director实例PVC卷集ID。 
### 登录名和密码 
上级网管系统到TECS Director取文件时，FTP用户名为pm，初始密码为Perf#out1!。可在系统管理→配置中心→内控管理
页面上修改pm用户的密码。
### 文件传输协议 
支持使用FTP和SFTP协议传输文件。 
当对网络安全性要求更高时，建议使用SFTP。
### 性能文件命名规则 
命名格式为：  
<Data Type>[-<NE Type>-<NE Mark>]-<Query Scope>-<Object Type>-<Measurement Period>-<Starting Time>-<Ending Time>.csv
参数具体说明参见[表1](a6c8315c235140e4bb4679f9ceca387a.html#topicid9044541__08863728-3961-4948-a955-c6802aed0285)。
参数|含义|备注
---|---|---
Data Type|数据类型|这里为性能管理"PM"
NE Type|网元类型|可在性能北向FTP服务器设置页面文件命名格式中选择是否包含这两项
NE Mark|网元标识|可在性能北向FTP服务器设置页面文件命名格式中选择是否包含这两项
Query Scope|领域|支持：TECS：虚拟资源PIM：硬件资源CEPH：分布式存储OPENPALLETE：容器资源OPERATE：运营资源
Object Type|计数器类型|取值为：DCHOSTHOSTNETWORKVMVMNETWORKCLOUDENVIRONMENTDISKSWITCHROUTERSTORAGE
Measurement Period|数据粒度|支持：5分钟15分钟
Starting Time|性能数据的开始时间|格式为：YYYYMMDDhhmmss“DD”：天“MM”：月“YYYY”：年“hh”：小时（24制）“mm” ：分钟"ss"：秒
Ending Time|性能数据的结束时间|格式为：YYYYMMDDhhmmss“DD”：天“MM”：月“YYYY”：年“hh”：小时（24制）“mm” ：分钟"ss"：秒
举例： 
文件命名格式中不包含NE Type和NE Mark：PM-TECS-VM-5-20200508101000-20200508101500.csv。文件名中各项所代表的参数参见表2。表2  文件名各项代表参数文件名项代表参数PMData TypeTECSQuery ScopeVMObject Type5Measurement Period20200508101000Starting Time20200508101500Ending Time 
文件命名格式中包含NE Type和NE Mark：PM-DIRECTOR-10.47.181.84-TECS-VM-5-20200508102500-20200508103000.csv。表3  文件名各项代表参数文件名项代表参数PMData TypeDIRECTORNE Type10.47.181.84NE MarkTECSQuery ScopeVMObject Type5Measurement Period20200508101000Starting Time20200508101500Ending Time 
### 文件格式 
CSV文件格式要求： 
文件第一行为字段名，每个字段以英文逗号“,”分隔。支持中文和英文，指标格式支持“指标名称和ID”、“指标ID”和“指标名称”，语言和指标格式可以在性能北向FTP服务器设置中文件列名格式进行配置。 
从第二行开始是性能数据，每条记录占用一行，记录中的每个数据之间使用英文逗号“,”分隔。 
性能数据的字段有Start Time，End Time，Object Name，Object Id，Env Id和计数器（一般有多个计数器） 
Start Time和End Time格式为：YYYY/MM/DD hh:mm:ss，“DD”， “MM”， “YYYY”， “hh”， “mm” ，"ss" 分别表示天，月，年，小时（24小时制），分钟和秒。 
Object Name是对象名称，下级节点名称在前，上级节点名称在后，通过符号”|”分隔，各计数器类型的对象名称格式参见文件中Object Name拼接规则。 
Object Id是对象标识。 
Env Id是资源池标识，没有资源池属性的对象该列为空，例如VDC。 
如果记录中的某字段值为空，不填写该值，直接输入下一个字段。指标值为空，填写“--”。 
一个例子： 
Start Time|End Time|Object Name|Object Id|Env Id|C100020001(vcpu)|C100020002(vcpu)
---|---|---|---|---|---|---
2021/1/12 9:50|2021/1/12 9:55|host-192-168-170-71|27|DC|host-192-168-170-71_host-192-168-170-71|d3187e28-08fe-41e1-8bff-e024c9d13067|20|20
2021/1/12 9:50|2021/1/12 9:55|host-192-168-170-72|27|DC|host-192-168-170-72_host-192-168-170-72|d3187e28-08fe-41e1-8bff-e024c9d13067|0|0
CSV文件特殊数据说明： 
“N/A”表示不支持。 
“--”表示没有采集到数据，原因可能有：资源池不支持该指标指标计算过程中出现问题生成文件过程中出现问题 
“NaN”表示无穷大。 
“0”表示性能数据为0。 
如果北向对接需要的数据中有除0之外的其他三种，请联系运维管理员。 
### 数据粒度和文件生成周期 
文件的性能数据粒度支持5分钟和15分钟粒度的，文件生成周期可在性能北向FTP服务器设置页面根据需要设置。
性能数据粒度为5分钟时，文件生成周期有以下选择。5分钟15分钟30分钟60分钟 
性能数据粒度为15分钟时，文件生成周期有以下选择。15分钟30分钟60分钟 
### 时区 
时区支持本地时区和格林威治时区，默认是本地时区，可以根据需要在性能北向FTP服务器设置页面设置。
### 上报空间汇总结果 
性能数据默认包括空间汇总结果，可以根据需要在性能北向FTP服务器设置页面设置。
### 上报指标 
包含基础指标和关键指标，可以根据需要在性能北向FTP服务器设置页面选择。
### 文件压缩 
文件压缩格式为“zip”，zip文件命名规则为<Data Type>[-<NE Type>-<NE Mark>]-<Measurement Period>-<Starting Time>-<Ending Time>.zip，字段含义同[性能文件命名规则](a6c8315c235140e4bb4679f9ceca387a.html)。
FTP服务器上的是zip文件，使用前需要解压。
### 配置页面 
## 参考 
### 文件示例 
[PM-TECS-HOST-5-20210202095000-2.xls](files/PM-TECS-HOST-5-20210202095000-2.xls)
[PM-PIM-FIREWALL-5-2021020209500.xls](files/PM-PIM-FIREWALL-5-2021020209500.xls)
### 文件中Object Name拼接规则 

### 文件中Object Name拼接规则 


 

#### 虚拟资源 
数据中心dc：对象本身名称 
云环境vim：云环境名称|数据中心名称 
可用域az：对象本身名称|云环境名称|数据中心名称 
主机集群hostaggregate：对象本身名称|云环境名称|数据中心名称 
主机host（包含控制节点和计算节点）：对象本身名称|云环境名称|数据中心名称 
裸金属bm：对象本身名称|云环境名称|数据中心名称 
主机网络hostnetwork：对象本身名称|主机名称|云环境名称|数据中心名称 
主机链路hostnetworklink：对象本身名称|主机名称|云环境名称|数据中心名称 
主机磁盘分区hostdiskpartition：对象本身名称|主机名称|云环境名称|数据中心名称 
虚机vm：虚机名称|主机名称|云环境名称|数据中心名称 
虚机网络vmnetwork：对象本身名称虚机名称|主机名称|云环境名称|数据中心名称 
磁盘disk：对象本身名称虚机名称|主机名称|云环境名称|数据中心名称 
#### 硬件资源 
子级对象名称在前，父级对象名称在后，“|”分隔，层层拼接。 
#### 分布式存储 
分布式存储集群cephcluster集群名称|分布式存储系统名称|云环境名称|数据中心名称 
分布式存储池cephpool存储池名称|集群名称|分布式存储系统名称|云环境名称|数据中心名称 
分布式存储卷cephvolume卷名称|存储池名称|集群名称|分布式存储系统名称|云环境名称|数据中心名称 
分布式存储节点cephnode节点名称|集群名称|分布式存储系统名称|云环境名称|数据中心名称 
分布式存储端口cephport端口名称|节点名称|集群名称|分布式存储系统名称|云环境名称|数据中心名称 
分布式存储节点文件系统cephfilesystem文件系统挂载点|节点名称|集群名称|分布式存储系统名称|云环境名称|数据中心名称 
#### 容器资源 
子级对象名称在前，父级对象名称在后，“|”分隔，层层拼接。 
