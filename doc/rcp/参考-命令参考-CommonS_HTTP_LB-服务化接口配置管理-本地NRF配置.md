 本地NRF配置 


背景知识 


在5G核心网系统中，服务使用者向NRF发现服务提供者，NRF在发现响应中携带满足条件的服务提供者的NFProfile。但某些场景下，运营商没有部署NRF或者NRF无法提供某些NF的发现结果，此时需要在服务使用者（本端）上把服务提供者（对端）的NFProfile配置出来。当服务使用者需要发现一个服务提供者时，就按照类似NRF的功能逻辑，在本地用服务发现请求里面的参数跟NFProfile里面的参数逐一匹配，如果全部匹配成功，则使用NFProfile里面的信息作为服务提供者的信息，上述功能称为本地NRF功能。 




功能说明 


本地NRF配置目录包含了本地NRF功能所需要的所有配置，包括公共配置、对端NF配置、对端NF服务实例配置、NF扩展信息配置。当运营商没有部署NRF，或者部署了NRF但NRF无法提供某些NF的发现结果时，需要配置该组命令。如果不配置本地NRF配置目录下的命令，则本地NRF功能无法生效。 




子主题： 






# 公共配置 
# 公共配置 


背景知识 


本地NRF配置中，有部分参数在对端NF配置、对端NF服务实例配置、NF扩展信息配置中都会出现，例如IP地址配置、PLMN ID配置等等，为了避免重复配置，将这些配置都放到公共配置命令树目录下，对端NF配置或NF实例配置等只需要引用这些公共配置的编号即可。 




功能说明 


公共配置命令树目录包含了本地NRF功能所需要的所有公共配置。当启用本地NRF功能时，需要配置该组命令。如果不配置公共配置，则上述NF配置或NF服务实例配置也无法配置成功，本地NRF功能无法生效。 




子主题： 






## PLMN ID配置 
## PLMN ID配置 


背景知识 


PLMN ID(Public Land Mobile Network Identification，公共陆地移动网标识) 包含公共陆地移动网的移动国家码和移动网号。 

服务使用者（本端）会携带用户当前所在网络的PLMN ID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN ID与NFProfile的PLMN ID列表进行比较，找到匹配的PLMN ID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN ID，这是一组PLMN ID信息。在本地NRF功能开启时，PLMN ID配置会呈现在对端NFProfile的plmnList数组中。 




功能说明 


PLMN ID配置用于配置服务提供者的公共陆地移动网的移动国家码和移动网号，当启用本地NRF功能时，需要配置该组命令。 

该配置被“PLMN ID组参数配置”引用，最终呈现在本地NRF配置的对端NFProfile的plmnList数组中。由于该引用关系是强制的，如果不配置PLMN ID，则PLMN ID组参数也无法配置成功。 




子主题： 






### 新增PLMN ID配置(ADD SBIPLMNID) 
### 新增PLMN ID配置(ADD SBIPLMNID) 


功能说明 

该命令用于新增PLMN ID配置。当本地NRF配置中所配置的对端NFProfile需要携带使用移动国家码和移动网号所组成的公共陆地移动网信息时，使用该命令。 

命令执行成功后，PLMN ID编号可以被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。 


 
“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。 

 
“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。 

 
“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 必选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




命令举例 


`
新增PLMN ID配置：PLMN ID编号为1，移动国家码为"123"，移动网号为"456"。
ADD SBIPLMNID:INDEX=1,MCC="123",MNC="456";
` 


### 修改PLMN ID配置(SET SBIPLMNID) 
### 修改PLMN ID配置(SET SBIPLMNID) 


功能说明 

该命令用于修改PLMN ID配置。当本地NRF配置中所配置的对端NFProfile携带的公共陆地移动网信息需要变更时，使用该命令。命令执行成功后，修改后的公共陆地移动网信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




命令举例 


`
修改PLMN ID配置：PLMN ID编号为1，移动国家码为"123"，移动网号为"456"。
SET SBIPLMNID:INDEX=1,MCC="123",MNC="456";
` 


### 删除PLMN ID配置(DEL SBIPLMNID) 
### 删除PLMN ID配置(DEL SBIPLMNID) 


功能说明 

该命令用于删除PLMN ID配置。当本地NRF配置中所配置的对端NFProfile不需要携带该公共陆地移动网时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该公共陆地移动网。 


注意事项 

如果要删除该PLMN ID配置，需要先删除引用该配置的“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”。 


 
“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询，通过DEL SBIPLMNIDARRPARAM命令进行删除。 

 
“PLMN NID配置”通过SHOW SBIPLMNNID命令查询，通过DEL SBIPLMNNID命令进行删除。 

 
“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询，通过DEL SBIGUAMIARRPARAM命令进行删除。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




命令举例 


`
删除PLMN ID配置：PLMN ID编号为1。
DEL SBIPLMNID:INDEX=1;
` 


### 查询PLMN ID配置(SHOW SBIPLMNID) 
### 查询PLMN ID配置(SHOW SBIPLMNID) 


功能说明 

该命令用于查询PLMN ID配置。当需要查询对端NFProfile携带的公共陆地移动网信息时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号，该编号是PLMN ID配置的唯一标识。该参数被“PLMN ID组参数配置”、“PLMN NID配置”及“GUAMI组参数配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“PLMN NID配置”通过SHOW SBIPLMNNID命令查询。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
MCC|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家/地区代码，包含3个数字。该参数由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动网络代码，包含2或3位数字。该参数由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。




命令举例 


`
查询PLMN ID配置：PLMN ID编号为1。
SHOW SBIPLMNID:INDEX=1

(No.1) : SHOW SBIPLMNID:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN ID编号 移动国家码 移动网号 
-----------------------------------------------
复制 修改 删除 1           123        456      
-----------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:21:25 耗时: 0.618 秒

` 


## PLMN ID组配置 
## PLMN ID组配置 


背景知识 


PLMN ID(Public Land Mobile Network Identification，公共陆地移动网标识) 包含公共陆地移动网的移动国家码和移动网号。 

服务使用者（本端）会携带用户当前所在网络的PLMN ID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN ID与NFProfile的PLMN ID列表进行比较，找到匹配的PLMN ID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN ID，这是一组PLMN ID信息。在本地NRF功能开启时，PLMN ID配置会呈现在对端NFProfile的plmnList数组中。 




功能说明 


PLMN ID组配置包括“PLMN ID组编号配置”和“PLMN ID组参数配置”，一个PLMN ID组下面可以包含若干个PLMN ID组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置对应本地NRF配置的对端NFProfile的plmnList数组，如果不配置，对端NFProfile缺少plmnList数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。 




子主题： 






### PLMN ID组编号配置 
### PLMN ID组编号配置 


背景知识 


PLMN ID(Public Land Mobile Network Identification，公共陆地移动网标识) 包含公共陆地移动网的移动国家码和移动网号。 

服务使用者（本端）会携带用户当前所在网络的PLMN ID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN ID与NFProfile的PLMN ID列表进行比较，找到匹配的PLMN ID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN ID，这是一组PLMN ID信息。在本地NRF功能开启时，PLMN ID配置会呈现在对端NFProfile的plmnList数组中。 




功能说明 


PLMN ID组编号配置用于配置一个PLMN ID组，一个PLMN ID组包含了若干个PLMN ID组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被“对端NF服务实例配置”引用，最终呈现在本地NRF配置的对端NFProfile的PLMN数组中。如果不配置，则对端NFProfile缺少plmnList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增PLMN ID组编号配置(ADD SBIPLMNIDARRID) 
#### 新增PLMN ID组编号配置(ADD SBIPLMNIDARRID) 


功能说明 

该命令用于新增PLMN ID组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组PLMN ID时，使用该命令。 

命令执行成功后，PLMN ID组编号可以被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。 


 
“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN ID组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号，该编号是PLMN ID组编号配置的唯一标识。该参数被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号，该编号是PLMN ID组编号配置的唯一标识。该参数被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




命令举例 


`
新增PLMN ID组编号配置：PLMN ID组编号为1。
ADD SBIPLMNIDARRID:ARRAYID=1;
` 


#### 删除PLMN ID组编号配置(DEL SBIPLMNIDARRID) 
#### 删除PLMN ID组编号配置(DEL SBIPLMNIDARRID) 


功能说明 

该命令用于删除PLMN ID组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组PLMN ID时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组PLMN ID。 


注意事项 

如果要删除该PLMN ID配置，需要先删除引用该配置的“PLMN ID组参数配置”，并在“对端NF基本信息配置”及“对端NF服务实例配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询，通过DEL SBIPLMNIDARRPARAM命令进行删除。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询，通过SET SBIPEERNFBASEINFO命令进行设置。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询，通过SET SBIPEERNFSERVICEINSTANCE命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN ID组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号，该编号是PLMN ID组编号配置的唯一标识。该参数被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号，该编号是PLMN ID组编号配置的唯一标识。该参数被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




命令举例 


`
删除PLMN ID组编号配置：PLMN ID组编号为1。
DEL SBIPLMNIDARRID:ARRAYID=1;
` 


#### 查询PLMN ID组编号配置(SHOW SBIPLMNIDARRID) 
#### 查询PLMN ID组编号配置(SHOW SBIPLMNIDARRID) 


功能说明 

该命令用于查询PLMN ID组编号配置。当需要查询PLMN ID组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号，该编号是PLMN ID组编号配置的唯一标识。该参数被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号，该编号是PLMN ID组编号配置的唯一标识。该参数被“PLMN ID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“PLMN ID组参数配置”通过SHOW SBIPLMNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




命令举例 


`
查询PLMN ID组编号配置：PLMN ID组编号为1。
SHOW SBIPLMNIDARRID:ARRAYID=1

(No.1) : SHOW SBIPLMNIDARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN ID组编号 
----------------------------
复制 删除      1            
----------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:23:15 耗时: 0.609 秒

` 


### PLMN ID组参数配置 
### PLMN ID组参数配置 


背景知识 


PLMN ID(Public Land Mobile Network Identification，公共陆地移动网标识) 包含公共陆地移动网的移动国家码和移动网号。 

服务使用者（本端）会携带用户当前所在网络的PLMN ID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN ID与NFProfile的PLMN ID列表进行比较，找到匹配的PLMN ID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN ID，这是一组PLMN ID信息。在本地NRF功能开启时，PLMN ID配置会呈现在对端NFProfile的plmnList数组中。 




功能说明 


PLMN ID组参数配置用于配置一个PLMN ID归属于哪个PLMN ID组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置PLMN ID组参数，则一个PLMN ID不能归属于一个具体的PLMN ID组，导致对端NFProfile将缺少plmnList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增PLMN ID组参数配置(ADD SBIPLMNIDARRPARAM) 
#### 新增PLMN ID组参数配置(ADD SBIPLMNIDARRPARAM) 


功能说明 

该命令用于新增PLMN ID组参数配置。当PLMN ID配置需要归属于一个PLMN ID组时，使用该命令。命令执行成功后，PLMN ID组就可以包含PLMN ID配置。 


注意事项 

如果要新增该PLMN ID组参数配置，需要先新增“PLMN ID配置”和“PLMN ID组编号配置”。 


 
“PLMN ID配置”通过SHOW SBIPLMNID命令查询，通过ADD SBIPLMNID命令进行新增。 

 
“PLMN ID组编号配置”通过SHOW SBIPLMNIDARRID命令查询，通过ADD SBIPLMNIDARRID命令进行新增。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




命令举例 


`
新增PLMN ID组参数配置：配置索引为1，PLMN ID组编号为1，PLMN ID编号为1。
ADD SBIPLMNIDARRPARAM:INDEX=1,ARRAYID=1,PLMNID=1;
` 


#### 修改PLMN ID组参数配置(SET SBIPLMNIDARRPARAM) 
#### 修改PLMN ID组参数配置(SET SBIPLMNIDARRPARAM) 


功能说明 

该命令用于修改PLMN ID组参数配置。当PLMN ID配置需要变更归属的PLMN ID组时，使用该命令。命令执行成功后，PLMN ID配置归属到变更后的PLMN ID组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




命令举例 


`
修改PLMN ID组参数配置：配置索引为1，PLMN ID组编号为1，PLMN ID编号为1。
SET SBIPLMNIDARRPARAM:INDEX=1,ARRAYID=1,PLMNID=1;
` 


#### 删除PLMN ID组参数配置(DEL SBIPLMNIDARRPARAM) 
#### 删除PLMN ID组参数配置(DEL SBIPLMNIDARRPARAM) 


功能说明 

该命令用于删除PLMN ID组参数配置。当PLMN ID配置不需要归属于PLMN ID组时，使用该命令。命令执行成功后，原先的PLMN ID组不再携带该PLMN ID配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




命令举例 


`
删除PLMN ID组参数配置：配置索引为1。
DEL SBIPLMNIDARRPARAM:INDEX=1;
` 


#### 查询PLMN ID组参数配置(SHOW SBIPLMNIDARRPARAM) 
#### 查询PLMN ID组参数配置(SHOW SBIPLMNIDARRPARAM) 


功能说明 

该命令用于查询PLMN ID组参数配置。当需要查询PLMN ID组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN ID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID组编号。PLMN ID组编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNIDARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID配置”中的配置，通过SHOW SBIPLMNID命令查询。




命令举例 


`
查询PLMN ID组参数配置：配置索引为1。
SHOW SBIPLMNIDARRPARAM:INDEX=1

(No.1) : SHOW SBIPLMNIDARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 PLMN ID组编号 PLMN ID编号 
------------------------------------------------
复制 修改 删除 1        1            1          
------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:24:51 耗时: 0.629 秒

` 


## PLMN NID配置 
## PLMN NID配置 


背景知识 


PLMN NID（Public Land Mobile Network Network Identifier，公共陆地移动网网络标识）表示使用公共陆地移动网和网络标识共同标识的SNPN（Standalone Non-Public Network，独立专网）。 

服务使用者（本端）会携带用户当前所在网络的PLMN NID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN NID与NFProfile的PLMN NID列表进行比较，找到匹配的PLMN NID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN NID，这是一组PLMN NID信息。在本地NRF功能开启时，PLMN NID配置会呈现在对端NFProfile的snpnList数组中。 




功能说明 


该组命令用于配置服务提供者的公共陆地移动网和网络标识共同标识的独立专网，当启用本地NRF功能时，需要配置该组命令。 

该配置被“PLMN NID组参数配置”引用，最终呈现在本地NRF配置的对端NFProfile的snpnList数组中。由于该引用关系是强制的，如果不配置PLMN NID，则PLMN NID组参数也无法配置成功。 




子主题： 






### 新增PLMN NID配置(ADD SBIPLMNNID) 
### 新增PLMN NID配置(ADD SBIPLMNNID) 


功能说明 

该命令用于新增PLMN NID配置。当本地NRF配置中所配置的对端NFProfile需要携带使用公共陆地移动网和网络标识共同标识的独立专网信息时，使用该命令。 

命令执行成功后，PLMN NID编号可以被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。 


 
“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。 

 
“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。 

 
“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。 

 
“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。 

 


注意事项 

如果要新增该PLMN NID配置，需要先新增PLMN ID配置。 

“PLMN ID配置”通过[SHOW SBIPLMNID]命令查询，通过[ADD SBIPLMNID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




命令举例 


`
新增PLMN NID配置：PLMN NID编号为1，PLMN ID编号为1，网络标识为"net123"。
ADD SBIPLMNNID:INDEX=1,PLMNID=1,NID="net123";
` 


### 修改PLMN NID配置(SET SBIPLMNNID) 
### 修改PLMN NID配置(SET SBIPLMNNID) 


功能说明 

该命令用于修改PLMN NID配置。当本地NRF配置中所配置的对端NFProfile携带的独立专网信息需要变更时，使用该命令。命令执行成功后，修改后的独立专网信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




命令举例 


`
修改PLMN NID配置：PLMN NID编号为1，PLMN ID编号为1，网络标识为"net123"。
SET SBIPLMNNID:INDEX=1,PLMNID=1,NID="net123";
` 


### 删除PLMN NID配置(DEL SBIPLMNNID) 
### 删除PLMN NID配置(DEL SBIPLMNNID) 


功能说明 

该命令用于删除PLMN NID配置。当本地NRF配置中所配置的对端NFProfile不需要携带该独立专网信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该独立专网。 


注意事项 

如果要删除该PLMN NID配置，需要先删除引用该配置的“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”。 


 
“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询，通过DEL SBIPLMNNIDARRPARAM命令进行删除。 

 
“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询，过DEL SBIPLMNSNSSAI命令进行删除。 

 
“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询，通过DEL SBITAIARRPARAM命令进行删除。 

 
“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询，通过DEL SBITAIRANGEARRPARAM命令进行删除。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




命令举例 


`
删除PLMN NID配置：PLMN NID编号为1。
DEL SBIPLMNNID:INDEX=1;
` 


### 查询PLMN NID配置(SHOW SBIPLMNNID) 
### 查询PLMN NID配置(SHOW SBIPLMNNID) 


功能说明 

该命令用于查询PLMN NID配置。当需要查询对端NFProfile携带的独立专网信息时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。该编号是PLMN NID配置的唯一标识。该参数被“PLMN NID组参数配置”、“PLMN S-NSSAI配置”、“TAI组参数配置”及“TAI范围组参数配置”引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“TAI组参数配置”通过SHOW SBITAIARRPARAM命令查询。“TAI范围组参数配置”通过SHOW SBITAIRANGEARRPARAM命令查询。该参数用数字表示 ，无特殊配置原则。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）的移动国家码和移动网号。PLMN ID编号引用“PLMN ID配置”中的配置，该编号是”PLMN ID配置“的唯一标识，通过SHOW SBIPLMNID命令查询。
NID|网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于设置网络标识，与PLMN ID一起用于标识SNPN（Standalone Non-Public Network，独立专网）。该参数根据协议设置。




命令举例 


`
查询PLMN NID配置：PLMN NID编号为1。
SHOW SBIPLMNNID:INDEX=1

(No.1) : SHOW SBIPLMNNID:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN NID编号 PLMN ID编号 网络标识 
-------------------------------------------------
复制 修改 删除 1            1           net123   
-------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:25:57 耗时: 0.607 秒

` 


## PLMN NID组配置 
## PLMN NID组配置 


背景知识 


PLMN NID（Public Land Mobile Network Network Identifier，公共陆地移动网网络标识）表示使用公共陆地移动网和网络标识共同标识的SNPN（Standalone Non-Public Network，独立专网）。 

服务使用者（本端）会携带用户当前所在网络的PLMN NID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN NID与NFProfile的PLMN NID列表进行比较，找到匹配的PLMN NID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN NID，这是一组PLMN NID信息。在本地NRF功能开启时，PLMN NID配置会呈现在对端NFProfile的snpnList数组中。 




功能说明 


PLMN NID组配置对应“本地NRF配置”的对端NFProfile的snpnList数组，如果不配置，则对端NFProfile缺少snpnList数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。当启用本地NRF功能时，需要配置该组命令。 

PLMN NID组配置包括“PLMN NID组编号配置”和“PLMN NID组参数配置”，一个PLMN NID组下面可以包含若干个PLMN NID组参数。 




子主题： 






### PLMN NID组编号配置 
### PLMN NID组编号配置 


背景知识 


PLMN NID（Public Land Mobile Network Network Identifier，公共陆地移动网网络标识）表示使用公共陆地移动网和网络标识共同标识的SNPN（Standalone Non-Public Network，独立专网）。 

服务使用者（本端）会携带用户当前所在网络的PLMN NID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN NID与NFProfile的PLMN NID列表进行比较，找到匹配的PLMN NID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN NID，这是一组PLMN NID信息。在本地NRF功能开启时，PLMN NID配置会呈现在对端NFProfile的snpnList数组中。 




功能说明 


PLMN NID组编号配置用于配置一个PLMN NID组，一个PLMN NID组包含了若干个PLMN NID组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被“对端NF基本信息”和“对端NF服务实例配置”引用，最终呈现在本地NRF配置的对端NFProfile的snpnList数组中。如果不配置，则对端NFProfile缺少snpnList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增PLMN NID组编号配置(ADD SBIPLMNNIDARRID) 
#### 新增PLMN NID组编号配置(ADD SBIPLMNNIDARRID) 


功能说明 

该命令用于新增PLMN NID组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组PLMN NID时，使用该命令。 

命令执行成功后，PLMN NID组编号可以被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。 


 
“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN NID组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号，该编号是PLMN NID组编号配置的唯一标识。被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号，该编号是PLMN NID组编号配置的唯一标识。被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




命令举例 


`
新增PLMN NID组编号配置：PLMN NID组编号为1。
ADD SBIPLMNNIDARRID:ARRAYID=1;
` 


#### 删除PLMN NID组编号配置(DEL SBIPLMNNIDARRID) 
#### 删除PLMN NID组编号配置(DEL SBIPLMNNIDARRID) 


功能说明 

该命令用于删除PLMN NID组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组PLMN NID时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组PLMN NID。 


注意事项 

如果要删除该PLMN NID组编号配置，需要先删除引用该配置的“PLMN NID组参数配置”，并在“对端NF基本信息配置”及“对端NF服务实例配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
”PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询，通过DEL SBIPLMNNIDARRPARAM命令进行删除。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询，通过SET SBIPEERNFBASEINFO命令进行设置。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询，通过SET SBIPEERNFSERVICEINSTANCE命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN NID组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号，该编号是PLMN NID组编号配置的唯一标识。被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号，该编号是PLMN NID组编号配置的唯一标识。被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




命令举例 


`
删除PLMN NID组编号配置：PLMN NID组编号为1。
DEL SBIPLMNNIDARRID:ARRAYID=1;
` 


#### 查询PLMN NID组编号配置(SHOW SBIPLMNNIDARRID) 
#### 查询PLMN NID组编号配置(SHOW SBIPLMNNIDARRID) 


功能说明 

该命令用于查询PLMN NID组编号配置。当需要查询PLMN NID组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号，该编号是PLMN NID组编号配置的唯一标识。被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号，该编号是PLMN NID组编号配置的唯一标识。被“PLMN NID组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN NID组参数配置”通过SHOW SBIPLMNNIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




命令举例 


`
查询PLMN NID组编号配置：PLMN NID组编号为1。
SHOW SBIPLMNNIDARRID:ARRAYID=1

(No.1) : SHOW SBIPLMNNIDARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN NID组编号 
-----------------------------
复制 删除      1             
-----------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:28:13 耗时: 0.61 秒

` 


### PLMN NID组参数配置 
### PLMN NID组参数配置 


背景知识 


PLMN NID（Public Land Mobile Network Network Identifier，公共陆地移动网网络标识）表示使用公共陆地移动网和网络标识共同标识的SNPN（Standalone Non-Public Network，独立专网）。 

服务使用者（本端）会携带用户当前所在网络的PLMN NID，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN NID与NFProfile的PLMN NID列表进行比较，找到匹配的PLMN NID时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN NID，这是一组PLMN NID信息。在本地NRF功能开启时，PLMN NID配置会呈现在对端NFProfile的snpnList数组中。 




功能说明 


PLMN NID组参数配置用于配置一个PLMN NID归属于哪个PLMN NID组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置PLMN NID组参数，则一个PLMN NID不能归属于一个具体的PLMN NID组，导致对端NFProfile将缺少snpnList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增PLMN NID组参数配置(ADD SBIPLMNNIDARRPARAM) 
#### 新增PLMN NID组参数配置(ADD SBIPLMNNIDARRPARAM) 


功能说明 

该命令用于新增PLMN NID组参数配置。当一个PLMN NID配置需要归属于一个PLMN NID组时，使用该命令。命令执行成功后，PLMN NID组就可以包含PLMN NID配置。 


注意事项 

如果要新增该PLMN NID组参数配置，需要先新增“PLMN ID配置”和“PLMN NID组编号配置”。 


 
“PLMN ID配置”通过SHOW SBIPLMNID命令查询，通过ADD SBIPLMNID命令进行新增。 

 
“PLMN NID组编号配置”通过SHOW SBIPLMNNIDARRID命令查询，通过ADD SBIPLMNNIDARRID命令进行新增。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




命令举例 


`
新增PLMN NID组参数配置：配置索引为1，PLMN NID组编号为1，PLMN NID编号为1。
ADD SBIPLMNNIDARRPARAM:INDEX=1,ARRAYID=1,PLMNNID=1;
` 


#### 修改PLMN NID组参数配置(SET SBIPLMNNIDARRPARAM) 
#### 修改PLMN NID组参数配置(SET SBIPLMNNIDARRPARAM) 


功能说明 

该命令用于修改PLMN NID组参数配置。当一个PLMN NID配置需要变更归属的PLMN NID组时，使用该命令。命令执行成功后，PLMN NID配置归属到变更后的PLMN NID组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




命令举例 


`
修改PLMN NID组参数配置：配置索引为1，PLMN NID组编号为1，PLMN NID编号为1。
SET SBIPLMNNIDARRPARAM:INDEX=1,ARRAYID=1,PLMNNID=1;
` 


#### 删除PLMN NID组参数配置(DEL SBIPLMNNIDARRPARAM) 
#### 删除PLMN NID组参数配置(DEL SBIPLMNNIDARRPARAM) 


功能说明 

该命令用于删除PLMN NID组参数配置。当一个PLMN NID配置不需要归属于PLMN NID组时，使用该命令。命令执行成功后，原先的PLMN NID组不再携带该PLMN NID配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




命令举例 


`
删除PLMN NID组参数配置：配置索引为1。
DEL SBIPLMNNIDARRPARAM:INDEX=1;
` 


#### 查询PLMN NID组参数配置(SHOW SBIPLMNNIDARRPARAM) 
#### 查询PLMN NID组参数配置(SHOW SBIPLMNNIDARRPARAM) 


功能说明 

该命令用于查询PLMN NID组参数配置。当需要查询PLMN NID组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN NID组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID组编号。PLMN NID组编号引用“PLMN NID组编号配置”中的配置，通过SHOW SBIPLMNNIDARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号。PLMN NID编号引用“PLMN NID配置”中的配置，通过SHOW SBIPLMNNID命令查询。




命令举例 


`
查询PLMN NID组参数配置：配置索引为1。
SHOW SBIPLMNNIDARRPARAM:INDEX=1

(No.1) : SHOW SBIPLMNNIDARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 PLMN NID组编号 PLMN NID编号 
----------------------------------------------------
复制 修改 删除 1        1              1            
----------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:29:36 耗时: 0.617 秒

` 


## S-NSSAI配置 
## S-NSSAI配置 


背景知识 


S-NSSAI(Single Network Slice Selection Assistance Information，单个网络切片选择协助信息) 包含单个网络切片的切片区分符和切片/服务类型。 

网络切片标识是网络切片技术中最重要的参数。S-NSSAI唯一标识一个网络切片,S-NSSAI的集合称为NSSAI，其标识一组网络切片，在切片选择过程中起重要作用。 

服务使用者（本端）会携带用户当前所在网络的S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带S-NSSAI，这是一组S-NSSAI信息。在本地NRF功能开启时，S-NSSAI配置会呈现在对端NFProfile的SnssaiList数组中。 




功能说明 


S-NSSAI配置用于配置服务提供者的单个网络切片选择协助信息的切片区分符和切片/服务类型，当启用本地NRF功能时，需要配置该组命令。 

该配置被“S-NSSAI组参数配置”“S-NSSAI SMF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用，并最终呈现在本地NRF配置的对端NFProfile的SnssaiList数组中。由于该引用关系是强制的，如果不配置S-NSSAI，则S-NSSAI组参数，S-NSSAI UPF信息组参数和S-NSSAI SMF信息组参数也无法配置成功。 




子主题： 






### 新增S-NSSAI配置(ADD SBISNSSAI) 
### 新增S-NSSAI配置(ADD SBISNSSAI) 


功能说明 

该命令用于新增S-NSSAI编号配置。当本地NRF配置中所配置的对端NFProfile需要添加携带切片/服务类型和切片区分符的单个网络切片选择协助信息时，使用该命令。 

命令执行成功后，S-NSSAI编号可以被“S-NSSAI组参数配置”、“S-NSSAI SMF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。 


 
“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。 

 
“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。 

 
“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 必选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




命令举例 


`
新增S-NSSAI配置：S-NSSAI编号为1，切片区分符为"ABCdef"，切片/服务 类型为"255"。
ADD SBISNSSAI:INDEX=1,SD="ABCdef",SST=255;
` 


### 修改S-NSSAI配置(SET SBISNSSAI) 
### 修改S-NSSAI配置(SET SBISNSSAI) 


功能说明 

该命令用于修改S-NSSAI配置。当本地NRF配置中所配置的对端NFProfile携带的单个网络切片选择协助信息需要变更时，使用该命令。命令执行成功后，修改后的单个网络切片选择协助信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




命令举例 


`
修改S-NSSAI配置：S-NSSAI编号为1，切片区分符为"abcDEF"，切片/服务 类型为"255"。
SET SBISNSSAI:INDEX=1,SD="abcDEF",SST=255;
` 


### 删除S-NSSAI配置(DEL SBISNSSAI) 
### 删除S-NSSAI配置(DEL SBISNSSAI) 


功能说明 

该命令用于删除S-NSSAI配置。当本地NRF配置中所配置的对端NFProfile不需要携带该单个网络切片选择协助信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该单个网络切片选择协助信息。 


注意事项 

如果要删除该S-NSSAI配置，需要先删除引用该配置的“S-NSSAI组参数配置”、“S-NSSAI SMF信息组参数配置”及“S-NSSAI UPF信息组参数配置”。 


 
“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询，通过DEL SBISNSSAIARRPARAM命令进行删除。 

 
“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询，通过DEL SBISNSSAISMFINFOARRPARAM命令进行删除。 

 
“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询，通过DEL SBISNSSAIUPFINFOARRPARAM命令进行删除。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




命令举例 


`
删除S-NSSAI配置：S-NSSAI编号为1。
 DEL SBISNSSAI:INDEX=1;
` 


### 查询S-NSSAI配置(SHOW SBISNSSAI) 
### 查询S-NSSAI配置(SHOW SBISNSSAI) 


功能说明 

该命令用于查询S-NSSAI配置。当需要查询对端NFProfile携带的单个网络切片选择协助信息时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号是S-NSSAI配置的唯一标识。该参数被“S-NSSAI组参数配置及“S-NSSAI UPF信息组参数配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“S-NSSAI SMF信息组参数配置”通过SHOW SBISNSSAISMFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
SST|切片/服务 类型|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片/服务类型，该参数是在0到255之间的无符号整数，表示切片/服务类型。该参数用于了解期望的网络切片在功能和服务方面的行为。 值0到127对应于标准SST范围。值128到255对应运营商的特定范围。
SD|切片区分符|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择协助信息）的切片区分符，其是一个3字节的字符串，以十六进制形式来表示切片区分符。组成该参数的每个字符应取值“ 0”至“ 9”或“ A”至“ F”并代表4bits。代表切片区分符的4个最高有效位的有效字符应首先出现在字符串中，代表切片区分符的4个最低有效位的字符应最后出现在字符串中。切片区分符是一个可选参数，是对切片/服务（Slice / Service）类型的补充，以允许在相同切片/服务类型的情况下对多个网络切片进行区分。




命令举例 


`
查询S-NSSAI配置。
SHOW SBISNSSAI

(No.3) : SHOW SBISNSSAI:
-----------------CommonS_HTTP_LB_0----------------
操作维护       S-NSSAI编号 切片区分符 切片/服务 类型 
--------------------------------------------------
复制 修改 删除 1           aaaaa1     1                         
复制 修改 删除 22          ABCdef     22             
复制 修改 删除 569         ABCDEF     100                        
复制 修改 删除 65535       ffffff     255            
--------------------------------------------------
记录数：6
执行成功   耗时: 0.543 秒

` 


## S-NSSAI组配置 
## S-NSSAI组配置 


背景知识 


S-NSSAI(Single Network Slice Selection Assistance Information，单个网络切片选择协助信息) 包含单个网络切片的切片区分符和切片/服务类型。 

网络切片标识是网络切片技术中最重要的参数。S-NSSAI唯一标识一个网络切片,S-NSSAI的集合称为NSSAI，其标识一组网络切片，在切片选择过程中起重要作用。 

服务使用者（本端）会携带用户当前所在网络的S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带S-NSSAI，这是一组S-NSSAI信息。在本地NRF功能开启时，S-NSSAI配置会呈现在对端NFProfile的SnssaiList数组中。 




功能说明 


S-NSSAI组配置包括“S-NSSAI组编号配置”和“S-NSSAI组参数配置”，一个S-NSSAI组可以包含若干个S-NSSAI组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置对应本地NRF配置的对端NFProfile的SnssaiList数组，如果不配置，对端NFProfile缺少SnssaiList数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。 




子主题： 






### S-NSSAI组编号配置 
### S-NSSAI组编号配置 


背景知识 


S-NSSAI(Single Network Slice Selection Assistance Information，单个网络切片选择协助信息) 包含单个网络切片的切片区分符和切片/服务类型。 

网络切片标识是网络切片技术中最重要的参数。S-NSSAI唯一标识一个网络切片,S-NSSAI的集合称为NSSAI，其标识一组网络切片，在切片选择过程中起重要作用。 

服务使用者（本端）会携带用户当前所在网络的S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带S-NSSAI，这是一组S-NSSAI信息。在本地NRF功能开启时，S-NSSAI配置会呈现在对端NFProfile的SnssaiList数组中。 




功能说明 


S-NSSAI组编号配置用于配置一个S-NSSAI组，一个S-NSSAI组包含了若干个S-NSSAI组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被“S-NSSAI组参数配置”，“PLMN S-NSSAI配置”，“对端NF基本信息配置”和“对端NF服务实例配置”引用，最终呈现在本地NRF配置的对端NFProfile的SnssaiList数组中。如果不配置，则对端NFProfile缺少SnssaiList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增S-NSSAI组编号配置(ADD SBISNSSAIARRID) 
#### 新增S-NSSAI组编号配置(ADD SBISNSSAIARRID) 


功能说明 

该命令用于新增S-NSSAI组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组S-NSSAI时，使用该命令。 

命令执行成功后，S-NSSAI组编号可以被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。 


 
“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。 

 
“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该编号是S-NSSAI组编号配置的唯一标识。该参数被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该编号是S-NSSAI组编号配置的唯一标识。该参数被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




命令举例 


`
新增S-NSSAI组编号配置：S-NSSAI组标识为1。
ADD SBISNSSAIARRID:ARRAYID=1;
` 


#### 删除S-NSSAI组编号配置(DEL SBISNSSAIARRID) 
#### 删除S-NSSAI组编号配置(DEL SBISNSSAIARRID) 


功能说明 

该命令用于删除S-NSSAI组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组S-NSSAI时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组S-NSSAI。 


注意事项 

如果要删除该S-NSSAI组编号配置，需要先删除引用该配置的“S-NSSAI组参数配置”和“PLMN S-NSSAI配置”，并在“对端NF基本信息配置”及“对端NF服务实例配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询，通过DEL SBISNSSAIARRPARAM命令进行删除。 

 
“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询，通过DEL SBIPLMNSNSSAI命令进行删除。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询，通过SET SBIPEERNFBASEINFO命令进行设置。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询，通过SET SBIPEERNFSERVICEINSTANCE命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该编号是S-NSSAI组编号配置的唯一标识。该参数被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该编号是S-NSSAI组编号配置的唯一标识。该参数被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




命令举例 


`
删除S-NSSAI组编号配置：S-NSSAI组标识为1。
DEL SBISNSSAIARRID:ARRAYID=1;
` 


#### 查询S-NSSAI组编号配置(SHOW SBISNSSAIARRID) 
#### 查询S-NSSAI组编号配置(SHOW SBISNSSAIARRID) 


功能说明 

该命令用于查询S-NSSAI组编号配置。当需要查询S-NSSAI组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该编号是S-NSSAI组编号配置的唯一标识。该参数被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该编号是S-NSSAI组编号配置的唯一标识。该参数被“S-NSSAI组参数配置”、“PLMN S-NSSAI配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“S-NSSAI组参数配置”通过SHOW SBISNSSAIARRPARAM命令查询。“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数无特殊配置原则。




命令举例 


`
查询S-NSSAI组编号配置。
SHOW SBISNSSAIARRID

(No.52) : SHOW SBISNSSAIARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
S-NSSAI组标识
1
记录数：1

执行成功耗时: 0.133 秒

` 


### S-NSSAI组参数配置 
### S-NSSAI组参数配置 


背景知识 


S-NSSAI(Single Network Slice Selection Assistance Information，单个网络切片选择协助信息) 包含单个网络切片的切片区分符和切片/服务类型。 

网络切片标识是网络切片技术中最重要的参数。S-NSSAI唯一标识一个网络切片,S-NSSAI的集合称为NSSAI，其标识一组网络切片，在切片选择过程中起重要作用。 

服务使用者（本端）会携带用户当前所在网络的S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带S-NSSAI，这是一组S-NSSAI信息。在本地NRF功能开启时，S-NSSAI配置会呈现在对端NFProfile的SnssaiList数组中。 




功能说明 


S-NSSAI组参数配置用于配置一个S-NSSAI归属于哪个S-NSSAI组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置S-NSSAI组参数，则一个S-NSSAI不能归属于一个具体的S-NSSAI组，导致对端NFProfile缺少SnssaiList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增S-NSSAI组参数配置(ADD SBISNSSAIARRPARAM) 
#### 新增S-NSSAI组参数配置(ADD SBISNSSAIARRPARAM) 


功能说明 

该命令用于新增S-NSSAI组参数配置。当S-NSSAI配置需要归属于一个S-NSSAI组时，使用该命令。命令执行成功后，S-NSSAI组就可以包含S-NSSAI配置。 


注意事项 

如果要新增该S-NSSAI组参数配置，需要先新增“S-NSSAI配置”和“S-NSSAI组编号配置”。 


 
“S-NSSAI配置”通过SHOW SBISNSSAI命令查询，通过ADD SBISNSSAI命令进行新增。 

 
“S-NSSAI组编号配置”通过SHOW SBISNSSAIARRID命令查询，通过ADD SBISNSSAIARRID命令进行新增。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




命令举例 


`
新增S-NSSAI组参数配置：配置索引为1，S-NSSAI组编号为1，S-NSSAI编号为1。
ADD SBISNSSAIARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=1;
` 


#### 修改S-NSSAI组参数配置(SET SBISNSSAIARRPARAM) 
#### 修改S-NSSAI组参数配置(SET SBISNSSAIARRPARAM) 


功能说明 

该命令用于修改S-NSSAI组参数配置。当S-NSSAI配置需要变更归属的S-NSSAI组时，使用该命令。命令执行成功后，S-NSSAI配置归属到变更后的S-NSSAI组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




命令举例 


`
修改S-NSSAI组参数配置：配置索引为1，S-NSSAI组编号为1，S-NSSAI编号为2。
SET SBISNSSAIARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=2;
` 


#### 删除S-NSSAI组参数配置(DEL SBISNSSAIARRPARAM) 
#### 删除S-NSSAI组参数配置(DEL SBISNSSAIARRPARAM) 


功能说明 

该命令用于删除S-NSSAI组参数配置。当S-NSSAI配置不需要归属于S-NSSAI组时，使用该命令。命令执行成功后，原先的S-NSSAI组不再携带该S-NSSAI配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




命令举例 


`
删除S-NSSAI组参数配置：配置索引为1。
DEL SBISNSSAIARRPARAM:INDEX=1;
` 


#### 查询S-NSSAI组参数配置(SHOW SBISNSSAIARRPARAM) 
#### 查询S-NSSAI组参数配置(SHOW SBISNSSAIARRPARAM) 


功能说明 

该命令用于查询S-NSSAI组参数配置。当需要查询S-NSSAI组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“SNSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，S-NSSAI组编号引用“S-NSSAI组编号配置”中的配置，S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，S-NSSAI编号引用“S-NSSAI配置”中的配置，S-NSSAI编号通过SHOW SBISNSSAI命令查询。




命令举例 


`
查询S-NSSAI组参数配置。
SHOW SBISNSSAIARRPARAM:INDEX=1

(No.4) : SHOW SBISNSSAIARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 S-NSSAI组编号 S-NSSAI编号
----------------------------------------------------------------
复制 修改 删除 1        1            1              
----------------------------------------------------------------
记录数：1
耗时: 0.596 秒

` 


## PLMN S-NSSAI配置 
## PLMN S-NSSAI配置 


背景知识 


PLMN S-NSSAI（Public Land Mobile Network Network Single Network Slice Selection Assistance Information，公共陆地移动网单一网络切片选择协助信息）表示使用独立专网和单一网络切片选择协助信息组编号共同标识的配置信息。 

服务使用者（本端）会携带用户当前所在网络的PLMN S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN S-NSSAI与NFProfile的PLMN S-NSSAI列表进行比较，找到匹配的PLMN S-NSSAI时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN S-NSSAI，这是一组PLMN S-NSSAI信息。在本地NRF功能开启时，PLMN S-NSSAI配置会呈现在对端NFProfile的plmnSnssnaiList数组中。 




功能说明 


该组命令用于配置服务提供者的独立专网和单一网络切片选择协助信息组编号共同标识的公共陆地移动网单一网络切片选择协助信息，当启用本地NRF功能时，需要配置该组命令。 

该配置被“PLMN S-NSSAI组参数配置”引用，最终呈现在本地NRF配置的对端NFProfile的plmnSnssnaiList数组中。由于该引用关系是强制的，如果不配置PLMN S-NSSAI，则PLMN S-NSSAI组参数也无法配置成功。 




子主题： 






### 新增PLMN S-NSSAI配置(ADD SBIPLMNSNSSAI) 
### 新增PLMN S-NSSAI配置(ADD SBIPLMNSNSSAI) 


功能说明 

该命令用于新增PLMN S-NSSAI配置。当本地NRF配置中所配置的对端NFProfile需要携带使用SNPN（Standalone Non-Public Network，独立专网）和S-NSSAI组编号共同标识的PLMN S-NSSAI时，使用该命令。 

命令执行成功后，PLMN S-NSSAI编号可以被“PLMN S-NSSAI组参数配置”引用。“PLMN S-NSSAI组参数配置”通过[SHOW SBIPIMNSNSSAIARRPARAM]命令查询。


注意事项 

如果要新增该PLMN S-NSSAI配置，需要先新增PLMN NID编号和S-NSSAI组编号。 

“PLMN NID编号”通过[SHOW SBIPLMNNID]命令查询，通过[ADD SBIPLMNNID]命令进行新增。

“S-NSSAI组编号”通过[SHOW SBISNSSAIARRID]命令查询，通过[ADD SBISNSSAIARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




命令举例 


`
新增PLMN  S-NSSAI配置：PLMN  S-NSSAI编号为1，PLMN NID编号为1，S-NSSAI组标识为123。
ADD SBIPLMNSNSSAI:INDEX=1,PLMINNID=1,SNSSAIARRAY=123;
` 


### 修改PLMN S-NSSAI配置(SET SBIPLMNSNSSAI) 
### 修改PLMN S-NSSAI配置(SET SBIPLMNSNSSAI) 


功能说明 

该命令用于修改PLMN S-NSSAI配置。当本地NRF配置中所配置的对端NFProfile携带的PLMN S-NSSAI需要变更时，使用该命令。命令执行成功后，修改后的独立专网信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




命令举例 


`
修改PLMN  S-NSSAI配置：PLMN  S-NSSAI编号为1，PLMN NID编号为1，S-NSSAI组标识为123。
SET SBIPLMNSNSSAI:INDEX=1,PLMINNID=1,SNSSAIARRAY=123;
` 


### 删除PLMN S-NSSAI配置(DEL SBIPLMNSNSSAI) 
### 删除PLMN S-NSSAI配置(DEL SBIPLMNSNSSAI) 


功能说明 

该命令用于删除PLMN S-NSSAI配置。当本地NRF配置中所配置的对端NFProfile不需要携带该PLMN S-NSSAI时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该独立专网。 


注意事项 

如果要删除该PLMN S-NSSAI配置，需要先删除引用该配置的“PLMN S-NSSAI组参数配置”。 

“PLMN S-NSSAI组参数配置”通过[SHOW SBIPIMNSNSSAIARRPARAM]命令查询，通过[DEL SBIPIMNSNSSAIARRPARAM]命令进行删除。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




命令举例 


`
删除PLMN  S-NSSAI配置：PLMN  S-NSSAI编号为1。
DEL SBIPLMNSNSSAI:INDEX=1;
` 


### 查询PLMN S-NSSAI配置(SHOW SBIPLMNSNSSAI) 
### 查询PLMN S-NSSAI配置(SHOW SBIPLMNSNSSAI) 


功能说明 

该命令用于查询PLMN S-NSSAI配置。当需要查询对端NFProfile携带的PLMN S-NSSAI时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|PLMN  S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号。该编号是PLMN S-NSSAI配置的唯一标识，被“PLMN SNSSAI组参数配置”引用。“PLMN SNSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。该参数用数字表示，无特殊配置原则。
PLMINNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，PLMN NID编号是由NID（网络标识）与PLMN ID一起标识的SNPN（Standalone Non-Public Network，独立专网）的唯一标识。PLMN NID编号通过SHOW SBIPLMNNID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI组编号，该参数用于与SNPN（Standalone Non-Public Network，独立专网）共同标识PLMN S-NSSAI。S-NSSAI组编号通过SHOW SBISNSSAIARRID命令查询。




命令举例 


`
查询PLMN  S-NSSAI配置。
SHOW SBIPLMNSNSSAI

(No.3) : SHOW SBIPLMNSNSSAI:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN  S-NSSAI编号 PLMN NID编号 S-NSSAI组编号 
-------------------------------------------------
复制 修改 删除 1                 1            1            
-------------------------------------------------
记录数：1
耗时: 0.595 秒

` 


## PLMN S-NSSAI组配置 
## PLMN S-NSSAI组配置 


背景知识 


PLMN S-NSSAI（Public Land Mobile Network Network Single Network Slice Selection Assistance Information，公共陆地移动网单一网络切片选择协助信息）表示使用独立专网和单一网络切片选择协助信息组编号共同标识的配置信息。 

服务使用者（本端）会携带用户当前所在网络的PLMN S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN S-NSSAI与NFProfile的PLMN S-NSSAI列表进行比较，找到匹配的PLMN S-NSSAI时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN S-NSSAI，这是一组PLMN S-NSSAI信息。在本地NRF功能开启时，PLMN S-NSSAI配置会呈现在对端NFProfile的plmnSnssnaiList数组中。 




功能说明 


PLMN S-NSSAI组配置对应“本地NRF配置”的对端NFProfile的plmnSnssnaiList数组，如果不配置，则对端NFProfile缺少plmnSnssnaiList数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。当启用本地NRF功能时，需要配置该组命令。 

PLMN S-NSSAI组配置包括“PLMN S-NSSAI组编号配置”和“PLMN S-NSSAI组参数配置”，一个PLMN S-NSSAI组下面可以包含若干个PLMN S-NSSAI组参数。 




子主题： 






### PLMN S-NSSAI组编号配置 
### PLMN S-NSSAI组编号配置 


背景知识 


PLMN S-NSSAI（Public Land Mobile Network Network Single Network Slice Selection Assistance Information，公共陆地移动网单一网络切片选择协助信息）表示使用独立专网和单一网络切片选择协助信息组编号共同标识的配置信息。 

服务使用者（本端）会携带用户当前所在网络的PLMN S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN S-NSSAI与NFProfile的PLMN S-NSSAI列表进行比较，找到匹配的PLMN S-NSSAI时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN S-NSSAI，这是一组PLMN S-NSSAI信息。在本地NRF功能开启时，PLMN S-NSSAI配置会呈现在对端NFProfile的plmnSnssnaiList数组中。 




功能说明 


PLMN S-NSSAI组编号配置用于配置一个PLMN S-NSSAI组，一个PLMN S-NSSAI组包含了若干个PLMN S-NSSAI组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被“对端NF基本信息”和“对端NF服务实例配置”引用，最终呈现在本地NRF配置的对端NFProfile的plmnSnssnaiList数组中。如果不配置，则对端NFProfile缺少plmnSnssnaiList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增PLMN S-NSSAI组编号配置(ADD SBIPIMNSNSSAIARRID) 
#### 新增PLMN S-NSSAI组编号配置(ADD SBIPIMNSNSSAIARRID) 


功能说明 

该命令用于新增PLMN S-NSSAI组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组PLMN S-NSSAI时，使用该命令。 

命令执行成功后，PLMN S-NSSAI组编号可以被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。 


 
“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN  S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，该编号是PLMN S-NSSAI组编号配置的唯一标识。被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN  S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，该编号是PLMN S-NSSAI组编号配置的唯一标识。被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




命令举例 


`
新增PLMN  S-NSSAI组编号配置：PLMN  S-NSSAI组编号为1。
ADD SBIPIMNSNSSAIARRID:ARRAYID=1;
` 


#### 删除PLMN S-NSSAI组编号配置(DEL SBIPIMNSNSSAIARRID) 
#### 删除PLMN S-NSSAI组编号配置(DEL SBIPIMNSNSSAIARRID) 


功能说明 

该命令用于删除PLMN S-NSSAI组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组PLMN S-NSSAI时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组PLMN S-NSSAI。 


注意事项 

如果要删除该PLMN S-NSSAI组编号配置，需要先删除引用该配置的“PLMN S-NSSAI组参数配置”，并在“对端NF基本信息配置”及“对端NF服务实例配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询，通过DEL SBIPIMNSNSSAIARRPARAM命令进行删除。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询，通过SET SBIPEERNFBASEINFO命令进行设置。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询，通过SET SBIPEERNFSERVICEINSTANCE命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN  S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，该编号是PLMN S-NSSAI组编号配置的唯一标识。被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN  S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，该编号是PLMN S-NSSAI组编号配置的唯一标识。被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




命令举例 


`
删除PLMN  S-NSSAI组编号配置：PLMN  S-NSSAI组编号为1。
DEL SBIPIMNSNSSAIARRID:ARRAYID=1;
` 


#### 查询PLMN S-NSSAI组编号配置(SHOW SBIPIMNSNSSAIARRID) 
#### 查询PLMN S-NSSAI组编号配置(SHOW SBIPIMNSNSSAIARRID) 


功能说明 

该命令用于查询PLMN S-NSSAI组编号配置。当需要查询PLMN S-NSSAI组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN  S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，该编号是PLMN S-NSSAI组编号配置的唯一标识。被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN  S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，该编号是PLMN S-NSSAI组编号配置的唯一标识。被“PLMN S-NSSAI组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”等引用。“PLMN S-NSSAI组参数配置”通过SHOW SBIPIMNSNSSAIARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。该参数用数字表示，无特殊配置原则。




命令举例 


`
查询PLMN  S-NSSAI组编号配置。
SHOW SBIPIMNSNSSAIARRID

(No.6) : SHOW SBIPIMNSNSSAIARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN  S-NSSAI组编号 
--------------------------------
复制 删除      1                
--------------------------------
记录数：1
耗时: 0.599 秒

` 


### PLMN S-NSSAI组参数配置 
### PLMN S-NSSAI组参数配置 


背景知识 


PLMN S-NSSAI（Public Land Mobile Network Network Single Network Slice Selection Assistance Information，公共陆地移动网单一网络切片选择协助信息）表示使用独立专网和单一网络切片选择协助信息组编号共同标识的配置信息。 

服务使用者（本端）会携带用户当前所在网络的PLMN S-NSSAI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的PLMN S-NSSAI与NFProfile的PLMN S-NSSAI列表进行比较，找到匹配的PLMN S-NSSAI时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带PLMN S-NSSAI，这是一组PLMN S-NSSAI信息。在本地NRF功能开启时，PLMN S-NSSAI配置会呈现在对端NFProfile的plmnSnssnaiList数组中。 




功能说明 


PLMN S-NSSAI组参数配置用于配置一个PLMN S-NSSAI归属于哪个PLMN S-NSSAI组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置PLMN S-NSSAI组参数，则一个PLMN S-NSSAI不能归属于一个具体的PLMN S-NSSAI组，导致对端NFProfile将缺少plmnSnssnaiList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增PLMN S-NSSAI组参数配置(ADD SBIPIMNSNSSAIARRPARAM) 
#### 新增PLMN S-NSSAI组参数配置(ADD SBIPIMNSNSSAIARRPARAM) 


功能说明 

该命令用于新增PLMN S-NSSAI组参数配置。当一个PLMN S-NSSAI配置需要归属于一个PLMN S-NSSAI组时，使用该命令。命令执行成功后，PLMN S-NSSAI组就可以包含PLMN S-NSSAI配置。 


注意事项 

如果要新增该PLMN S-NSSAI组参数配置，需要先新增“PLMN S-NSSAI配置”和“PLMN S-NSSAI组编号配置”。 


 
“PLMN S-NSSAI配置”通过SHOW SBIPLMNSNSSAI命令查询，通过ADD SBIPLMNSNSSAI命令进行新增。 

 
“PLMN S-NSSAI组编号配置”通过SHOW SBIPIMNSNSSAIARRID命令查询，通过ADD SBIPIMNSNSSAIARRID命令进行新增。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




命令举例 


`
新增PLMN S-NSSAI组参数配置：配置索引为1，PLMN S-NSSAI组编号为1，PLMN S-NSSAI编号为1。
ADD SBIPIMNSNSSAIARRPARAM:INDEX=1,ARRAYID=1,PLMNSNSSAI=1;
` 


#### 修改PLMN S-NSSAI组参数配置(SET SBIPIMNSNSSAIARRPARAM) 
#### 修改PLMN S-NSSAI组参数配置(SET SBIPIMNSNSSAIARRPARAM) 


功能说明 

该命令用于修改PLMN S-NSSAI组参数配置。当一个PLMN S-NSSAI配置需要变更归属的PLMN S-NSSAI组时，使用该命令。命令执行成功后，PLMN S-NSSAI配置归属到变更后的PLMN S-NSSAI组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




命令举例 


`
修改PLMN S-NSSAI组参数配置：配置索引为1，PLMN S-NSSAI组编号为1，PLMN S-NSSAI编号为1。
SET SBIPIMNSNSSAIARRPARAM:INDEX=1,ARRAYID=1,PLMNSNSSAI=1;
` 


#### 删除PLMN S-NSSAI组参数配置(DEL SBIPIMNSNSSAIARRPARAM) 
#### 删除PLMN S-NSSAI组参数配置(DEL SBIPIMNSNSSAIARRPARAM) 


功能说明 

该命令用于删除PLMN S-NSSAI组参数配置。当一个PLMN S-NSSAI配置不需要归属于PLMN S-NSSAI组时，使用该命令。命令执行成功后，原先的PLMN S-NSSAI组不再携带该PLMN NID配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




命令举例 


`
删除PLMN S-NSSAI组参数配置：配置索引为1。
DEL SBIPIMNSNSSAIARRPARAM:INDEX=1;
` 


#### 查询PLMN S-NSSAI组参数配置(SHOW SBIPIMNSNSSAIARRPARAM) 
#### 查询PLMN S-NSSAI组参数配置(SHOW SBIPIMNSNSSAIARRPARAM) 


功能说明 

该命令用于查询PLMN S-NSSAI组参数配置。当需要查询PLMN S-NSSAI组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是“PLMN S-NSSAI组参数配置”的唯一标识。该参数用数字表示，无特殊配置原则。
ARRAYID|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI组编号，PLMN S-NSSAI组编号引用“PLMN S-NSSAI组编号配置”中的配置，PLMN S-NSSAI组编号通过SHOW SBIPIMNSNSSAIARRID命令查询。
PLMNSNSSAI|PLMN S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN S-NSSAI编号，PLMN S-NSSAI编号引用“PLMN S-NSSAI配置”中的配置，PLMN S-NSSAI配置索引通过SHOW SBIPLMNSNSSAI命令查询。




命令举例 


`
查询PLMN S-NSSAI组参数配置。
SHOW SBIPIMNSNSSAIARRPARAM

(No.7) : SHOW SBIPIMNSNSSAIARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引                 PLMN S-NSSAI组编号 PLMN S-NSSAI编号 
----------------------------------------------------------------------------
复制 修改 删除 1                        1                1                  
----------------------------------------------------------------------------
记录数：1
耗时: 0.613 秒

` 


## NSI组配置 
## NSI组配置 


背景知识 


NSI（Network Slice Instance，网络切片实例）表示一组网络功能实例和所需资源（例如计算，存储和网络资源），它们构成了已部署的网络切片。 

服务使用者（本端）会携带用户当前所在网络的NSI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的NSI（即用户当前所在网络的NSI）与对端NFProfile的NSI列表进行比较，找到匹配的NSI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带NSI，这是一组NSI信息。在本地NRF功能开启时，NSI配置会呈现在对端NFProfile的nsiList数组中。 




功能说明 


NSI组配置即对应本地NRF配置的对端NFProfile的nsiList数组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置，则对端NFProfile缺少nsiList数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。 

NSI组配置包括NSI组编号配置和NSI组参数配置，一个NSI组下面可以包含若干个NSI组参数。 




子主题： 






### NSI组编号配置 
### NSI组编号配置 


背景知识 


NSI（Network Slice Instance，网络切片实例）表示一组网络功能实例和所需资源（例如计算，存储和网络资源），它们构成了已部署的网络切片。 

服务使用者（本端）会携带用户当前所在网络的NSI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的NSI（即用户当前所在网络的NSI）与对端NFProfile的NSI列表进行比较，找到匹配的NSI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带NSI，这是一组NSI信息。在本地NRF功能开启时，NSI配置会呈现在对端NFProfile的nsiList数组中。 




功能说明 


NSI组编号配置用于配置一个NSI组，一个NSI组包含了若干个NSI组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被对端NF基本信息引用，最终呈现在本地NRF配置的对端NFProfile的nsiList数组中。如果不配置，则对端NFProfile缺少nsiList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增NSI组编号配置(ADD SBINSIARRID) 
#### 新增NSI组编号配置(ADD SBINSIARRID) 


功能说明 

该命令用于新增NSI组编号配置。当本地NRF配置的对端NFProfile需要携带一组NSI时，使用该命令。命令执行成功后，NSI组编号可以被NSI组参数配置及对端NF基本信息配置引用。 

NSI组参数配置通过[SHOW SBINSIARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NSI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号，该编号是NSI组编号配置的唯一标识，被NSI组参数配置及对端NF基本信息配置引用。NSI组参数配置通过SHOW SBINSIARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号，该编号是NSI组编号配置的唯一标识，被NSI组参数配置及对端NF基本信息配置引用。NSI组参数配置通过SHOW SBINSIARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




命令举例 


`
新增NSI组编号配置：NSI组编号为1。
ADD SBINSIARRID:ARRAYID=1;
` 


#### 删除NSI组编号配置(DEL SBINSIARRID) 
#### 删除NSI组编号配置(DEL SBINSIARRID) 


功能说明 

该命令用于删除NSI组编号配置。当本地NRF配置的对端NFProfile不需要携带该组NSI时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组NSI。 


注意事项 

如果要删除该NSI组编号配置，需要先删除引用该配置的NSI组参数配置和对端NF基本信息配置。 

NSI组参数配置通过[SHOW SBIPLMNIDARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NSI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号，该编号是NSI组编号配置的唯一标识，被NSI组参数配置及对端NF基本信息配置引用。NSI组参数配置通过SHOW SBINSIARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号，该编号是NSI组编号配置的唯一标识，被NSI组参数配置及对端NF基本信息配置引用。NSI组参数配置通过SHOW SBINSIARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




命令举例 


`
删除NSI组编号配置：NSI组编号为1。
DEL SBINSIARRID:ARRAYID=1;
` 


#### 查询NSI组编号配置(SHOW SBINSIARRID) 
#### 查询NSI组编号配置(SHOW SBINSIARRID) 


功能说明 

该命令用于查询NSI组编号配置。当需要查询NSI组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号，该编号是NSI组编号配置的唯一标识，被NSI组参数配置及对端NF基本信息配置引用。NSI组参数配置通过SHOW SBINSIARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号，该编号是NSI组编号配置的唯一标识，被NSI组参数配置及对端NF基本信息配置引用。NSI组参数配置通过SHOW SBINSIARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




命令举例 


`
查询NSI组编号配置：NSI组编号为1。
SHOW SBINSIARRID:ARRAYID=1

(No.1) : SHOW SBINSIARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       NSI组编号 
-------------------------
复制 删除      1         
-------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:32:08 耗时: 0.615 秒

` 


### NSI组参数配置 
### NSI组参数配置 


背景知识 


NSI（Network Slice Instance，网络切片实例）表示一组网络功能实例和所需资源（例如计算，存储和网络资源），它们构成了已部署的网络切片。 

服务使用者（本端）会携带用户当前所在网络的NSI，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的NSI（即用户当前所在网络的NSI）与对端NFProfile的NSI列表进行比较，找到匹配的NSI时，就认为发现成功。NRF返回的对端NFProfile包含的服务中会携带NSI，这是一组NSI信息。在本地NRF功能开启时，NSI配置会呈现在对端NFProfile的nsiList数组中。 




功能说明 


NSI组参数配置用于配置一个NSI归属于哪个NSI组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在NF中引用该NSI组参数归属的NSI组编号。如果不配置NSI组参数，则一个NSI不能归属于一个具体的NSI组，导致对端NFProfile将缺少nsiList数组，本端如果需要向NRF发现可用的对端，则发现失败。 

如果要新增NSI组参数配置，需要先使用命令 [ADD SBINSIARRID]新增NSI组编号配置。




子主题： 






#### 新增NSI组参数配置(ADD SBINSIARRPARAM) 
#### 新增NSI组参数配置(ADD SBINSIARRPARAM) 


功能说明 

该命令用于新增NSI组参数配置。当一个NSI配置需要归属于一个NSI组时，使用该命令。命令执行成功后，NSI组就可以包含NSI配置。 


注意事项 

如果要新增该NSI组参数配置，需要先新增NSI组编号配置。 

NSI组编号配置通过[SHOW SBINSIARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 必选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




命令举例 


`
新增NSI组参数配置：配置索引为1，NSI组编号为1，NSI为"abc"。
ADD SBINSIARRPARAM:INDEX=1,ARRAYID=1,NSI="abc";
` 


#### 修改NSI组参数配置(SET SBINSIARRPARAM) 
#### 修改NSI组参数配置(SET SBINSIARRPARAM) 


功能说明 

该命令用于修改NSI组参数配置。当一个NSI配置需要变更归属的NSI组时，使用该命令。命令执行成功后，NSI配置归属到变更后的NSI组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




命令举例 


`
修改NSI组参数配置：配置索引为1，NSI组编号为1，NSI为"abc"。
SET SBINSIARRPARAM:INDEX=1,ARRAYID=1,NSI="abc";
` 


#### 删除NSI组参数配置(DEL SBINSIARRPARAM) 
#### 删除NSI组参数配置(DEL SBINSIARRPARAM) 


功能说明 

该命令用于删除NSI组参数配置。当一个NSI配置不需要归属于NSI组时，使用该命令。命令执行成功后，原先的NSI组不再携带该NSI配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




命令举例 


`
删除NSI组参数配置：配置索引为1。
DEL SBINSIARRPARAM:INDEX=1;
` 


#### 查询NSI组参数配置(SHOW SBINSIARRPARAM) 
#### 查询NSI组参数配置(SHOW SBINSIARRPARAM) 


功能说明 

该命令用于查询NSI组参数配置。当需要查询NSI组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NSI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NSI组编号。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。该参数无特殊配置原则。
NSI|NSI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的NSI（Network Slice Instance，网络切片实例）标识，用于在部署同一网络切片的多个网络切片实例时，标识网络切片实例的核心网络部分。该参数无特殊配置原则。




命令举例 


`
查询NSI组参数配置：配置索引为1。
SHOW SBINSIARRPARAM:INDEX=1

(No.1) : SHOW SBINSIARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 NSI组编号 NSI 
--------------------------------------
复制 修改 删除 1        1         abc   
--------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:32:47 耗时: 0.604 秒

` 


## 域组配置 
## 域组配置 


背景知识 


域是NF的FQDN（Fully Qualified Domain Name，全称域名），表示允许访问NF实例的NF域名。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的NF域列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置域，则允许任何NF域可以访问该NF实例。在本地NRF功能开启时，域配置会呈现在对端NFProfile的allowedNfDomains数组中




功能说明 


域组配置即对应本地NRF配置的对端NFProfile的allowedNfDomains数组。如果不配置，则对端NFProfile缺少allowedNfDomains数组，表示所有NF域的服务使用者都可以访问对端NF实例。当启用本地NRF功能时，需要配置该组命令。 

域组配置包括域组编号配置和域组参数配置，一个域组下面可以包含若干个域组参数。 




子主题： 






### 域组编号配置 
### 域组编号配置 


背景知识 


域是NF的FQDN（Fully Qualified Domain Name，全称域名），表示允许访问NF实例的NF域名。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的NF域列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置域，则允许任何NF域可以访问该NF实例。在本地NRF功能开启时，域配置会呈现在对端NFProfile的allowedNfDomains数组中




功能说明 


域组编号配置用于配置一个域组，一个域组包含了若干个域组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被对端NF基本信息引用，最终呈现在本地NRF配置的对端NFProfile的allowedNfDomains数组中。如果不配置，则对端NFProfile缺少allowedNfDomains数组，表示所有NF域的服务使用者都可以访问对端NF实例。 




子主题： 






#### 新增域组编号配置(ADD SBIDOMAINARRID) 
#### 新增域组编号配置(ADD SBIDOMAINARRID) 


功能说明 

该命令用于新增域组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组域时，使用该命令。命令执行成功后，域组编号可以被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。 

域组参数配置通过[SHOW SBIDOMAINARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。对端NF服务实例配置通过[SHOW SBIPEERNFSERVICEINSTANCE]命令查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|域组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号，该编号是域组编号配置的唯一标识。被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。域组参数配置通过SHOW SBIDOMAINARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号，该编号是域组编号配置的唯一标识。被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。域组参数配置通过SHOW SBIDOMAINARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




命令举例 


`
新增域组编号配置：域组编号为1。
ADD SBIDOMAINARRID:ARRAYID=1;
` 


#### 删除域组编号配置(DEL SBIDOMAINARRID) 
#### 删除域组编号配置(DEL SBIDOMAINARRID) 


功能说明 

该命令用于删除域组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组域时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组域。 


注意事项 

如果要删除该域组编号配置，需要先删除引用该配置的域组参数配置、对端NF基本信息配置及对端NF服务实例配置。 

域组参数配置通过[SHOW SBIDOMAINARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。对端NF服务实例配置通过[SHOW SBIPEERNFSERVICEINSTANCE]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|域组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号，该编号是域组编号配置的唯一标识。被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。域组参数配置通过SHOW SBIDOMAINARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号，该编号是域组编号配置的唯一标识。被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。域组参数配置通过SHOW SBIDOMAINARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




命令举例 


`
删除域组编号配置：域组编号为1。
DEL SBIDOMAINARRID:ARRAYID=1;
` 


#### 查询域组编号配置(SHOW SBIDOMAINARRID) 
#### 查询域组编号配置(SHOW SBIDOMAINARRID) 


功能说明 

该命令用于查询域组编号配置。当需要查询域组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号，该编号是域组编号配置的唯一标识。被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。域组参数配置通过SHOW SBIDOMAINARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号，该编号是域组编号配置的唯一标识。被域组参数配置、对端NF基本信息配置及对端NF服务实例配置引用。域组参数配置通过SHOW SBIDOMAINARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




命令举例 


`
查询域组编号配置：域组编号为1。
SHOW SBIDOMAINARRID:ARRAYID=1

(No.1) : SHOW SBIDOMAINARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       域组编号 
------------------------
复制 删除      1        
------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:35:04 耗时: 0.612 秒

` 


### 域组参数配置 
### 域组参数配置 


背景知识 


域是NF的FQDN（Fully Qualified Domain Name，全称域名），表示允许访问NF实例的NF域名。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的NF域列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置域，则允许任何NF域可以访问该NF实例。在本地NRF功能开启时，域配置会呈现在对端NFProfile的allowedNfDomains数组中




功能说明 


域组参数配置用于配置一个域归属于哪个域组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在NF中引用该域组参数归属的域组编号。如果不配置域组参数，则一个域不能归属于一个具体的域组，导致对端NFProfile将缺少allowedNfDomains数组，表示所有NF域的服务使用者都可以访问对端NF实例。 




子主题： 






#### 新增域组参数配置(ADD SBIDOMAINARRPARAM) 
#### 新增域组参数配置(ADD SBIDOMAINARRPARAM) 


功能说明 

该命令用于新增域组参数配置。当一个域配置需要归属于一个域组时，使用该命令。命令执行成功后，域组就可以包含域配置。 


注意事项 

如果要新增该域组参数配置，需要先新增域组编号配置。 

域组编号配置通过[SHOW SBIDOMAINARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 必选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




命令举例 


`
新增域组参数配置：配置索引为1，域组编号为1，域为"zte.com.cn"。
ADD SBIDOMAINARRPARAM:INDEX=1,ARRAYID=1,DOMAIN="zte.com.cn";
` 


#### 修改域组参数配置(SET SBIDOMAINARRPARAM) 
#### 修改域组参数配置(SET SBIDOMAINARRPARAM) 


功能说明 

该命令用于修改域组参数配置。当一个域配置需要变更归属的域组时，使用该命令。命令执行成功后，域配置归属到变更后的域组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




命令举例 


`
修改域组参数配置：配置索引为1，域组编号为1，域为"zte.com.cn"。
SET SBIDOMAINARRPARAM:INDEX=1,ARRAYID=1,DOMAIN="zte.com.cn";
` 


#### 删除域组参数配置(DEL SBIDOMAINARRPARAM) 
#### 删除域组参数配置(DEL SBIDOMAINARRPARAM) 


功能说明 

该命令用于删除域组参数配置。当一个域配置不需要归属于域组时，使用该命令。命令执行成功后，原先的域组不再携带该域配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




命令举例 


`
删除域组参数配置：配置索引为1。
DEL SBIDOMAINARRPARAM:INDEX=1;
` 


#### 查询域组参数配置(SHOW SBIDOMAINARRPARAM) 
#### 查询域组参数配置(SHOW SBIDOMAINARRPARAM) 


功能说明 

该命令用于查询域组参数配置。当需要查询域组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是域组参数配置的唯一标识。
ARRAYID|域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置域组编号。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
DOMAIN|域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF的FQDN（Fully Qualified Domain Name，全称域名）。




命令举例 


`
查询域组参数配置：配置索引为1。
SHOW SBIDOMAINARRPARAM:INDEX=1

(No.1) : SHOW SBIDOMAINARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 域组编号 域         
--------------------------------------------
复制 修改 删除 1        1        zte.com.cn 
--------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:37:05 耗时: 0.63 秒

` 


## NF类型组配置 
## NF类型组配置 


背景知识 


NF类型是协议规定的5GC（5G Core Network）中NF的类型。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的NF类型列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置NF类型，则允许任何NF类型可以访问该NF实例。在本地NRF功能开启时，NF类型配置会呈现在对端NFProfile的allowedNfTypes数组中。




功能说明 


NF类型组配置即对应本地NRF配置的对端NFProfile的allowedNfTypes数组。如果不配置，则对端NFProfile缺少allowedNfTypes数组，表示所有NF类型的服务使用者都可以访问对端NF实例。当启用本地NRF功能时，需要配置该组命令。 

NF类型组配置包括NF类型组编号配置和NF类型组参数配置，一个NF类型组下面可以包含若干个NF类型组参数。 




子主题： 






### NF类型组编号配置 
### NF类型组编号配置 


背景知识 


NF类型是协议规定的5GC（5G Core Network）中NF的类型。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的NF类型列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置NF类型，则允许任何NF类型可以访问该NF实例。在本地NRF功能开启时，NF类型配置会呈现在对端NFProfile的allowedNfTypes数组中。




功能说明 


NF类型组编号配置用于配置一个NF类型组，一个NF类型组包含了若干个NF类型组参数。当启用本地NRF功能时，需要配置该组命令。 

当启用本地NRF功能时，如果需要限定可以访问NF实例的NF类型列表，则需要配置NF类型组编号。配置后，最终呈现在本地NRF配置的对端NFProfile的allowedNfTypes数组中。如果不配置，则对端NFProfile缺少allowedNfTypes数组，表示所有NF类型的服务使用者都可以访问对端NF实例。 




子主题： 






#### 新增NF类型组编号配置(ADD SBINFTYPEARRID) 
#### 新增NF类型组编号配置(ADD SBINFTYPEARRID) 


功能说明 

该命令用于新增NF类型组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组NF类型时，使用该命令。命令执行成功后，NF类型组编号可以被NF类型组参数配置和对端NF基本信息配置引用。 

NF类型组参数配置通过[SHOW SBINFTYPEARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF类型组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号，该编号是NF类型组编号配置的唯一标识。被NF类型组参数配置及对端NF基本信息配置引用。NF类型组参数配置通过SHOW SBINFTYPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号，该编号是NF类型组编号配置的唯一标识。被NF类型组参数配置及对端NF基本信息配置引用。NF类型组参数配置通过SHOW SBINFTYPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




命令举例 


`
新增NF类型组编号配置：NF类型组编号为1。
ADD SBINFTYPEARRID:ARRAYID=1;
` 


#### 删除NF类型组编号配置(DEL SBINFTYPEARRID) 
#### 删除NF类型组编号配置(DEL SBINFTYPEARRID) 


功能说明 

该命令用于删除NF类型组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组NF类型时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组NF类型。 


注意事项 

如果要删除该NF类型组编号配置，需要先删除引用该配置的NF类型组参数配置和对端NF基本信息配置。 

NF类型组参数配置通过[SHOW SBINFTYPEARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF类型组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号，该编号是NF类型组编号配置的唯一标识。被NF类型组参数配置及对端NF基本信息配置引用。NF类型组参数配置通过SHOW SBINFTYPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号，该编号是NF类型组编号配置的唯一标识。被NF类型组参数配置及对端NF基本信息配置引用。NF类型组参数配置通过SHOW SBINFTYPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




命令举例 


`
删除NF类型组编号配置：NF类型组编号为1。
DEL SBINFTYPEARRID:ARRAYID=1;
` 


#### 查询NF类型组编号配置(SHOW SBINFTYPEARRID) 
#### 查询NF类型组编号配置(SHOW SBINFTYPEARRID) 


功能说明 

该命令用于查询NF类型组编号配置。当需要查询NF类型组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号，该编号是NF类型组编号配置的唯一标识。被NF类型组参数配置及对端NF基本信息配置引用。NF类型组参数配置通过SHOW SBINFTYPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号，该编号是NF类型组编号配置的唯一标识。被NF类型组参数配置及对端NF基本信息配置引用。NF类型组参数配置通过SHOW SBINFTYPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




命令举例 


`
查询NF类型组编号配置：NF类型组编号为1。
SHOW SBINFTYPEARRID:ARRAYID=1

(No.1) : SHOW SBINFTYPEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       NF类型组编号 
----------------------------
复制 删除      1            
----------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:19:02 耗时: 0.616 秒

` 


### NF类型组参数配置 
### NF类型组参数配置 


背景知识 


NF类型是协议规定的5GC（5G Core Network）中NF的类型。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的NF类型列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置NF类型，则允许任何NF类型可以访问该NF实例。在本地NRF功能开启时，NF类型配置会呈现在对端NFProfile的allowedNfTypes数组中。




功能说明 


NF类型组参数配置用于配置一个NF类型归属于哪个NF类型组。当启用本地NRF功能时，需要配置该组命令。 

当限定可以访问NF实例的NF类型列表时，则需要配置NF类型组参数。配置完成后，在NF中引用该NF类型组参数归属的NF类型组编号。如果不配置NF类型组参数，则一个NF类型不能归属于一个具体的NF类型组，已经配置的NF类型组编号只能是一个孤立配置，导致组装NFProfile时会失败。 




子主题： 






#### 新增NF类型组参数配置(ADD SBINFTYPEARRPARAM) 
#### 新增NF类型组参数配置(ADD SBINFTYPEARRPARAM) 


功能说明 

该命令用于新增NF类型组参数配置。当一个NF类型配置需要归属于一个NF类型组时，使用该命令。命令执行成功后，NF类型组就可以包含NF类型配置。 


注意事项 

如果要新增该NF类型组参数配置，需要先新增NF类型组编号配置。 

NF类型组编号配置通过[SHOW SBINFTYPEARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




命令举例 


`
新增NF类型组参数配置：配置索引为1，NF类型组编号为1，NF类型为"NRF"。
ADD SBINFTYPEARRPARAM:INDEX=1,ARRAYID=1,NFTYPE="NRF_TYPE";
` 


#### 修改NF类型组参数配置(SET SBINFTYPEARRPARAM) 
#### 修改NF类型组参数配置(SET SBINFTYPEARRPARAM) 


功能说明 

该命令用于修改NF类型组参数配置。当一个NF类型配置需要变更归属的NF类型组时，使用该命令。命令执行成功后，NF类型配置归属到变更后的NF类型组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




命令举例 


`
修改NF类型组参数配置：配置索引为1，NF类型组编号为1，NF类型为"NRF"。
SET SBINFTYPEARRPARAM:INDEX=1,ARRAYID=1,NFTYPE="NRF_TYPE";
` 


#### 删除NF类型组参数配置(DEL SBINFTYPEARRPARAM) 
#### 删除NF类型组参数配置(DEL SBINFTYPEARRPARAM) 


功能说明 

该命令用于删除NF类型组参数配置。当一个NF类型配置不需要归属于NF类型组时，使用该命令。命令执行成功后，原先的NF类型组不再携带该NF类型配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




命令举例 


`
删除NF类型组参数配置：配置索引为1。
DEL SBINFTYPEARRPARAM:INDEX=1;
` 


#### 查询NF类型组参数配置(SHOW SBINFTYPEARRPARAM) 
#### 查询NF类型组参数配置(SHOW SBINFTYPEARRPARAM) 


功能说明 

该命令用于查询NF类型组参数配置。当需要查询NF类型组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF类型组参数配置的唯一标识。
ARRAYID|NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF类型组编号。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置协议规定的5GC（5G Core Network）中NF的类型。




命令举例 


`
查询NF类型组参数配置：配置索引为1。
SHOW SBINFTYPEARRPARAM:INDEX=1

(No.1) : SHOW SBINFTYPEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 NF类型组编号 NF类型 
--------------------------------------------
复制 修改 删除 1        1            NRF    
--------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:14:33 耗时: 0.628 秒

` 


## 服务范围组配置 
## 服务范围组配置 


背景知识 


服务范围表示在PLMN中NF实例可以服务的区域，可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的服务范围列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置服务范围，则不为NF实例提供特定的服务区域，但不意味着NF实例可以服务PLMN中的每个区域。在本地NRF功能开启时，服务范围配置会呈现在对端NFProfile的servingScope数组中。




功能说明 


服务范围组配置即对应本地NRF配置的对端NFProfile的servingScope数组。如果不配置，则对端NFProfile缺少servingScope数组，表示不为NF实例提供特定的服务区域。当启用本地NRF功能时，需要配置该组命令。 

服务范围组配置包括服务范围组编号配置和服务范围组参数配置，一个服务范围组下面可以包含若干个服务范围组参数。 




子主题： 






### 服务范围组编号配置 
### 服务范围组编号配置 


背景知识 


服务范围表示在PLMN中NF实例可以服务的区域，可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的服务范围列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置服务范围，则不为NF实例提供特定的服务区域，但不意味着NF实例可以服务PLMN中的每个区域。在本地NRF功能开启时，服务范围配置会呈现在对端NFProfile的servingScope数组中。




功能说明 


服务范围组编号配置用于配置一个服务范围组，一个服务范围组包含了若干个服务范围组参数。当启用本地NRF功能时，需要配置该组命令。 

当启用本地NRF功能时，如果需要提供NF实例在PLMN中可以服务的特定服务范围列表，则需要配置服务范围组编号。配置后，最终呈现在本地NRF配置的对端NFProfile的servingScope数组中。如果不配置，则对端NFProfile缺少servingScope数组，但不意味着NF实例可以服务PLMN中的每个区域。 




子主题： 






#### 新增服务范围组编号配置(ADD SBISERVSCOPEARRID) 
#### 新增服务范围组编号配置(ADD SBISERVSCOPEARRID) 


功能说明 

该命令用于新增服务范围组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组服务范围时，使用该命令。命令执行成功后，服务范围组编号可以被服务范围组参数配置和对端NF基本信息配置引用。 

服务范围组参数配置通过[SHOW SBISERVSCOPEARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|服务范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号，该编号是服务范围组编号配置的唯一标识。被服务范围组参数配置及对端NF基本信息配置引用。服务范围组参数配置通过SHOW SBISERVSCOPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号，该编号是服务范围组编号配置的唯一标识。被服务范围组参数配置及对端NF基本信息配置引用。服务范围组参数配置通过SHOW SBISERVSCOPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




命令举例 


`
新增服务范围组编号配置：服务范围组编号为1。
ADD SBISERVSCOPEARRID:ARRAYID=1;
` 


#### 删除服务范围组编号配置(DEL SBISERVSCOPEARRID) 
#### 删除服务范围组编号配置(DEL SBISERVSCOPEARRID) 


功能说明 

该命令用于删除服务范围组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组服务范围时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组服务范围。 


注意事项 

如果要删除该服务范围组编号配置，需要先删除引用该配置的服务范围组参数配置和对端NF基本信息配置。 

服务范围组参数配置通过[SHOW SBISERVSCOPEARRPARAM]命令查询。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|服务范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号，该编号是服务范围组编号配置的唯一标识。被服务范围组参数配置及对端NF基本信息配置引用。服务范围组参数配置通过SHOW SBISERVSCOPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号，该编号是服务范围组编号配置的唯一标识。被服务范围组参数配置及对端NF基本信息配置引用。服务范围组参数配置通过SHOW SBISERVSCOPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




命令举例 


`
删除服务范围组编号配置：服务范围组编号为1。
DEL SBISERVSCOPEARRID:ARRAYID=1;
` 


#### 查询服务范围组编号配置(SHOW SBISERVSCOPEARRID) 
#### 查询服务范围组编号配置(SHOW SBISERVSCOPEARRID) 


功能说明 

该命令用于查询服务范围组编号配置。当需要查询服务范围组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号，该编号是服务范围组编号配置的唯一标识。被服务范围组参数配置及对端NF基本信息配置引用。服务范围组参数配置通过SHOW SBISERVSCOPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号，该编号是服务范围组编号配置的唯一标识。被服务范围组参数配置及对端NF基本信息配置引用。服务范围组参数配置通过SHOW SBISERVSCOPEARRPARAM命令查询。对端NF基本信息配置通过SHOW SBIPEERNFBASEINFO命令查询。




命令举例 


`
查询服务范围组编号配置：服务范围组编号为1。
SHOW SBISERVSCOPEARRID:ARRAYID=1

(No.1) : SHOW SBISERVSCOPEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       服务范围组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:38:53 耗时: 0.598 秒

` 


### 服务范围组参数配置 
### 服务范围组参数配置 


背景知识 


服务范围表示在PLMN中NF实例可以服务的区域，可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。 

本地NRF功能中，该配置主要用于对端NF基本信息配置中。用于限定可以访问NF实例的服务范围列表，其中，对端NF基本信息配置可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置服务范围，则不为NF实例提供特定的服务区域，但不意味着NF实例可以服务PLMN中的每个区域。在本地NRF功能开启时，服务范围配置会呈现在对端NFProfile的servingScope数组中。




功能说明 


服务范围组参数配置用于配置一个服务范围归属于哪个服务范围组。当启用本地NRF功能时，需要配置该组命令。 

当需要提供NF实例在PLMN中可以服务的特定服务范围列表，则需要配置服务范围组参数。配置完成后，在NF中引用该服务范围组参数归属的服务范围组编号。如果不配置服务范围组参数，则一个服务范围不能归属于一个具体的服务范围组，已经配置的服务范围组编号只能是一个孤立配置，导致组装NFProfile时会失败。 




子主题： 






#### 新增服务范围组参数配置(ADD SBISERVSCOPEARRPARAM) 
#### 新增服务范围组参数配置(ADD SBISERVSCOPEARRPARAM) 


功能说明 

该命令用于新增服务范围组参数配置。当一个服务范围配置需要归属于一个服务范围组时，使用该命令。命令执行成功后，服务范围组就可以包含服务范围配置。 


注意事项 

如果要新增该服务范围组参数配置，需要先新增服务范围组编号配置。 

服务范围组编号配置通过[SHOW SBISERVSCOPEARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 必选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




命令举例 


`
新增服务范围组参数配置：配置索引为1，服务范围组编号为1，服务范围为"123000"。
ADD SBISERVSCOPEARRPARAM:INDEX=1,ARRAYID=1,SERVSCOPE="123000";
` 


#### 修改服务范围组参数配置(SET SBISERVSCOPEARRPARAM) 
#### 修改服务范围组参数配置(SET SBISERVSCOPEARRPARAM) 


功能说明 

该命令用于修改服务范围组参数配置。当一个服务范围配置需要变更归属的服务范围组时，使用该命令。命令执行成功后，服务范围配置归属到变更后的服务范围组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




命令举例 


`
修改服务范围组参数配置：配置索引为1，服务范围组编号为1，服务范围为"123000"。
SET SBISERVSCOPEARRPARAM:INDEX=1,ARRAYID=1,SERVSCOPE="123000";
` 


#### 删除服务范围组参数配置(DEL SBISERVSCOPEARRPARAM) 
#### 删除服务范围组参数配置(DEL SBISERVSCOPEARRPARAM) 


功能说明 

该命令用于删除服务范围组参数配置。当一个服务范围配置不需要归属于服务范围组时，使用该命令。命令执行成功后，原先的服务范围组不再携带该服务范围配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




命令举例 


`
删除服务范围组参数配置：配置索引为1。
DEL SBISERVSCOPEARRPARAM:INDEX=1;
` 


#### 查询服务范围组参数配置(SHOW SBISERVSCOPEARRPARAM) 
#### 查询服务范围组参数配置(SHOW SBISERVSCOPEARRPARAM) 


功能说明 

该命令用于查询服务范围组参数配置。当需要查询服务范围组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是服务范围组参数配置的唯一标识。
ARRAYID|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务范围组编号。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SERVSCOPE|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。




命令举例 


`
查询服务范围组参数配置：配置索引为1。
SHOW SBISERVSCOPEARRPARAM:INDEX=1

(No.1) : SHOW SBISERVSCOPEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 服务范围组编号 服务范围 
------------------------------------------------
复制 修改 删除 1        1              123000   
------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:40:24 耗时: 0.643 秒

` 


## NF集标识组配置 
## NF集标识组配置 


背景知识 


NF集由相同用户或业务区/服务区提供服务的多个NF组成。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。NF集标识即表示为一组可用来提供分发、冗余和可伸缩性的既有网络中相等且可互换的NF集合的全局唯一标识。 

服务使用者（本端）会携带用户当前所在网络的NF集标识，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的NF集标识与NFProfile的NF集标识列表进行比较，找到匹配的NF集标识时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带NF集标识，这是一组NF集标识信息。在本地NRF功能开启时，NF集标识配置会呈现在对端NFProfile的nfSetIdList数组中。 




功能说明 


NF集标识组配置对应“本地NRF配置”的对端NFProfile的nfSetIdList数组，如果不配置，则对端NFProfile缺少nfSetIdList数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。当启用本地NRF功能时，需要配置该组命令。 

NF集标识组配置包括“NF集标识组编号配置”和“NF集标识组参数配置”，一个NF集标识组下面可以包含若干个NF集标识组参数。 




子主题： 






### NF集标识组编号配置 
### NF集标识组编号配置 


背景知识 


NF集由相同用户或业务区/服务区提供服务的多个NF组成。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。NF集标识即表示为一组可用来提供分发、冗余和可伸缩性的既有网络中相等且可互换的NF集合的全局唯一标识。 

服务使用者（本端）会携带用户当前所在网络的NF集标识，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的NF集标识与NFProfile的NF集标识列表进行比较，找到匹配的NF集标识时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带NF集标识，这是一组NF集标识信息。在本地NRF功能开启时，NF集标识配置会呈现在对端NFProfile的nfSetIdList数组中。 




功能说明 


NF集标识组编号配置用于配置一个NF集标识组，一个NF集标识组包含了若干个NF集标识组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被“对端NF基本信息”引用，最终呈现在本地NRF配置的对端NFProfile的nfSetIdList数组中。如果不配置，则对端NFProfile缺少nfSetIdList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增NF集标识组编号配置(ADD SBINFSETIDARRID) 
#### 新增NF集标识组编号配置(ADD SBINFSETIDARRID) 


功能说明 

该命令用于新增NF集标识组编号配置。当本地NRF配置中所配置的对端NFProfile需要携带一组NF集标识时，使用该命令。 

命令执行成功后，NF集标识组编号可以被“NF集标识组参数配置”及“对端NF基本信息配置”引用。 


 
“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。 

 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF集标识组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号，该编号是NF集标识组编号配置的唯一标识。被“NF集标识组参数配置”及“对端NF基本信息配置”引用。“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号，该编号是NF集标识组编号配置的唯一标识。被“NF集标识组参数配置”及“对端NF基本信息配置”引用。“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




命令举例 


`
新增NF集标识组编号配置：NF集标识组编号为1。
ADD SBINFSETIDARRID:ARRAYID=1;
` 


#### 删除NF集标识组编号配置(DEL SBINFSETIDARRID) 
#### 删除NF集标识组编号配置(DEL SBINFSETIDARRID) 


功能说明 

该命令用于删除NF集标识组编号配置。当本地NRF配置中所配置的对端NFProfile不需要携带该组NF集标识时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该组NF集标识。 


注意事项 

如果要删除该NF集标识组编号配置，需要先删除引用该配置的“NF集标识组参数配置”，并在“对端NF基本信息配置”中将引用该配置的参数值设置为0来删除引用关系。 

<
 
“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询，通过DEL SBINFSETIDARRPARAM命令进行删除。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询，通过SET SBIPEERNFBASEINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF集标识组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号，该编号是NF集标识组编号配置的唯一标识。被“NF集标识组参数配置”及“对端NF基本信息配置”引用。“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号，该编号是NF集标识组编号配置的唯一标识。被“NF集标识组参数配置”及“对端NF基本信息配置”引用。“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




命令举例 


`
删除NF集标识组编号配置：NF集标识组编号为1。
DEL SBINFSETIDARRID:ARRAYID=1;
` 


#### 查询NF集标识组编号配置(SHOW SBINFSETIDARRID) 
#### 查询NF集标识组编号配置(SHOW SBINFSETIDARRID) 


功能说明 

该命令用于查询NF集标识组编号配置。当需要查询NF集标识组编号配置时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号，该编号是NF集标识组编号配置的唯一标识。被“NF集标识组参数配置”及“对端NF基本信息配置”引用。“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号，该编号是NF集标识组编号配置的唯一标识。被“NF集标识组参数配置”及“对端NF基本信息配置”引用。“NF集标识组参数配置”通过SHOW SBINFSETIDARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。该参数无特殊配置原则。




命令举例 


`
查询NF集标识组编号配置：NF集标识组编号为1。
SHOW SBINFSETIDARRID:ARRAYID=1

(No.1) : SHOW SBINFSETIDARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       NF集标识组编号 
--------------------------
复制 删除      1          
--------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:42:10 耗时: 0.607 秒

` 


### NF集标识组参数配置 
### NF集标识组参数配置 


背景知识 


NF集由相同用户或业务区/服务区提供服务的多个NF组成。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。NF集标识即表示为一组可用来提供分发、冗余和可伸缩性的既有网络中相等且可互换的NF集合的全局唯一标识。 

服务使用者（本端）会携带用户当前所在网络的NF集标识，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的NF集标识与NFProfile的NF集标识列表进行比较，找到匹配的NF集标识时，就认为发现成功。NRF返回的对端的NFProfile包含的服务中会携带NF集标识，这是一组NF集标识信息。在本地NRF功能开启时，NF集标识配置会呈现在对端NFProfile的nfSetIdList数组中。 




功能说明 


NF集标识组参数配置用于配置一个NF集标识归属于哪个NF集标识组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置NF集标识组参数，则一个NF集标识不能归属于一个具体的NF集标识组，导致对端NFProfile将缺少nfSetIdList数组，本端如果需要向NRF发现可用的对端，则发现失败。 




子主题： 






#### 新增NF集标识组参数配置(ADD SBINFSETIDARRPARAM) 
#### 新增NF集标识组参数配置(ADD SBINFSETIDARRPARAM) 


功能说明 

该命令用于新增NF集标识组参数配置。当一个NF集标识配置需要归属于一个NF集标识组时，使用该命令。命令执行成功后，NF集标识组就可以包含NF集标识配置。 


注意事项 

如果要新增该NF集标识组参数配置，需要先新增“NF集标识组编号配置”。 


 
“NF集标识组编号配置”通过ADD SBINFSETIDARRID命令进行新增。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 必选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




命令举例 


`
新增NF集标识组参数配置：配置索引为1，NF集标识组编号为1，NF集标识为"setxyz.smfset.5gc.mnc012.mcc345"。
ADD SBINFSETIDARRPARAM:INDEX=1,ARRAYID=1,NFSETID="setxyz.smfset.5gc.mnc012.mcc345";
` 


#### 修改NF集标识组参数配置(SET SBINFSETIDARRPARAM) 
#### 修改NF集标识组参数配置(SET SBINFSETIDARRPARAM) 


功能说明 

该命令用于修改NF集标识组参数配置。当一个NF集标识配置需要变更归属的NF集标识组时，使用该命令。命令执行成功后，NF集标识配置归属到变更后的NF集标识组。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




命令举例 


`
修改NF集标识组参数配置：配置索引为1，NF集标识组编号为1，NF集标识为"setxyz.smfset.5gc.mnc012.mcc345"。
SET SBINFSETIDARRPARAM:INDEX=1,ARRAYID=1,NFSETID="setxyz.smfset.5gc.mnc012.mcc345";
` 


#### 删除NF集标识组参数配置(DEL SBINFSETIDARRPARAM) 
#### 删除NF集标识组参数配置(DEL SBINFSETIDARRPARAM) 


功能说明 

该命令用于删除NF集标识组参数配置。当一个NF集标识配置不需要归属于NF集标识组时，使用该命令。命令执行成功后，原先的NF集标识组不再携带该NF集标识配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




命令举例 


`
删除NF集标识组参数配置：配置索引为1。
DEL SBINFSETIDARRPARAM:INDEX=1;
` 


#### 查询NF集标识组参数配置(SHOW SBINFSETIDARRPARAM) 
#### 查询NF集标识组参数配置(SHOW SBINFSETIDARRPARAM) 


功能说明 

该命令用于查询NF集标识组参数配置。当需要查询NF集标识组参数时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是NF集标识组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF集标识组编号。NF集标识组编号引用了“NF集标识组编号配置”中的配置，通过SHOW SBINFSETIDARRID命令查询。
NFSETID|NF集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置要求监视其状态的NF实例的NF集标识。格式为以下字符串："set&ltSet ID&gt.&ltNFType&gtset.5gc.mnc&ltMNC&gt.mcc&ltMCC>"其中，&ltMNC>表示PLMN的移动网络代码，包含2或3位数字，模式：'^ [0-9] {2,3} $'。&ltMCC>表示PLMN的移动国家/地区代码，包含3个数字，模式：'^ [0-9] {3} $'。&ltNFType>表示在5GC中可以找到的不同类型的网络功能或网络实体，需使用小写字符，如'amf'、'smf'等。&ltSet ID>编码由字母字符（A-Z和a-z），数字（0-9）和/或连字符（-）组成的字符串，并且应以字母字符或数字结尾。 模式：'^([A-Za-z0-9\-]*[A-Za-z0-9])$'。例子：    "setxyz.smfset.5gc.mnc012.mcc345"、    "set12.pcfset.5gc.mnc012.mcc345"




命令举例 


`
查询NF集标识组参数配置：配置索引为1。
SHOW SBINFSETIDARRPARAM:INDEX=1

(No.1) : SHOW SBINFSETIDARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 NF集标识组编号 NF集标识                        
-----------------------------------------------------------------------
复制 修改 删除 1        1              setxyz.smfset.5gc.mnc012.mcc345 
-----------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 11:44:36 耗时: 0.638 秒

` 


## IPv4地址配置 
## IPv4地址配置 


背景知识 


IPv4（Internet Protocol version 4，网际协议版本4）通常被写作点分十进制的形式，即四个字节被分开用十进制写出，中间用点分隔，比如：192.168.1.1。 

IPv4地址组是一个或多个IPv4地址的集合。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的服务提供者的NF Profile携带ipv4Addresses参数（包含一个或多个IPv4地址的IPv4地址组）。 

IP端点是网络功能服务侦听入向侧服务请求的IP地址和端口信息。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的服务提供者的NF Profile中会携带ipEndPoints参数（包含一个或多个IP端点信息的IP端点信息组）。 




功能说明 


本配置用于配置服务提供者的IPv4地址，当启用本地NRF功能时，需要使用该组命令。IPv4地址配置被IPv4地址组参数配置、IP端点配置引用。 




子主题： 






### 新增IPv4地址配置(ADD SBIIPV4ADDR) 
### 新增IPv4地址配置(ADD SBIIPV4ADDR) 


功能说明 

本命令用于新增IPv4地址配置，即给IPv4地址增加编号。 

当启用本地NRF功能时，需要执行此命令增加服务提供者（对端）网络功能（NF）的IPv4地址。命令执行成功后，新增的IPv4地址编号可以被IPv4地址组参数配置、IP端点配置引用。 

IPv4地址组是一个或多个IPv4地址的集合。一个网络功能可能拥有多个IPv4地址。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回对端的NF Profile携带的ipv4Addresses参数（包含一个或多个IPv4地址的IPv4地址组）。 

IP端点是网络功能服务侦听入向侧服务请求的IP地址和端口信息。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回对端的NF Profile包含的服务中会携带IP End Points参数（包含一个或多个IP端点信息的IP端点信息组）。 


注意事项 

系统支持的该配置项的最大记录数为8192。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




命令举例 


`
增加IPv4地址配置：编号为1，IP地址为“192.168.20.100”。 
ADD SBIIPV4ADDR:ID=1,IP="192.168.20.100"
` 


### 修改IPv4地址配置(SET SBIIPV4ADDR) 
### 修改IPv4地址配置(SET SBIIPV4ADDR) 


功能说明 

本命令用于修改IPv4地址配置，即变更IPv4地址编号所标识的IPv4地址。当服务提供者（对端）网络功能（NF）的IPv4地址发生变更时，执行该命令。 


注意事项 

IPv4地址编号无法修改，只允许修改IPv4地址。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




命令举例 


`
修改IPv4地址配置：编号为1，IP地址为“192.168.20.100”。 
SET SBIIPV4ADDR:ID=1,IP="192.168.20.100"
` 


### 删除IPv4地址配置(DEL SBIIPV4ADDR) 
### 删除IPv4地址配置(DEL SBIIPV4ADDR) 


功能说明 

本命令用于删除IPv4地址配置。当服务提供者（对端）网络功能（NF）的IPv4地址不再使用时，执行该命令。 


注意事项 

IPv4地址配置编号被IPv4地址组参数配置、IP端点配置引用，必须先去除IPv4地址组参数、IP端点配置配置中的引用，才能删除IPv4地址配置编号。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




命令举例 


`
删除IPv4地址配置：编号为1。
DEL SBIIPV4ADDR:ID=1
` 


### 查询IPv4地址配置(SHOW SBIIPV4ADDR) 
### 查询IPv4地址配置(SHOW SBIIPV4ADDR) 


功能说明 

本命令用于查询IPv4地址配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址的编号，用于标识一个IPv4地址。IPv4地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4地址编号对应的IPv4地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv4地址。




命令举例 


`
查询IPv4地址配置：编号为1。
SHOW SBIIPV4ADDR:ID=1

(No.3) : SHOW SBIIPV4ADDR:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IPv4地址编号 IP地址         
-------------------------------------------
复制 修改 删除 1            192.168.20.100 
-------------------------------------------
记录数：1
执行成功 开始时间:2020-11-11 15:00:23 耗时: 0.536 秒

` 


## IPv4地址组配置 
## IPv4地址组配置 


背景知识 


IPv4（Internet Protocol version 4，网际协议版本4），它通常被写作点分十进制的形式，即四个字节被分开用十进制写出，中间用点分隔，比如：192.168.1.1。 

IPv4地址组是一个或者多个IPv4地址的集合。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile会携带ipv4Addresses参数（包含一个或多个IPv4地址的IPv4地址组）。本端从中选择一个IPv4地址使用，并照顾到负载均衡。 




功能说明 


IPv4地址组配置是给IPv4地址组指定一个编号，便于在其它配置（例如，对端NF基本信息配置）中引用IPv4地址组。 

启用本地NRF功能时，需要在本地配置服务提供者的IPv4地址组。 

新增IPv4地址组后，必须通过IPv4地址组参数配置在组内添加一个或多个IPv4地址。组内无IPv4地址的地址组在被对端NF基本信息配置引用后，会导致对端NF的NFProfile的组装失败，本地NRF发现失败。 




子主题： 






### IPv4地址组编号配置 
### IPv4地址组编号配置 


背景知识 


IPv4（Internet Protocol version 4，网际协议版本4）通常被写作点分十进制的形式，即四个字节被分开用十进制写出，中间用点分隔，比如：192.168.1.1。 

IPv4地址组是一个或多个IPv4地址的集合。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NF Profile会携带ipv4Addresses参数（包含一个或多个IPv4地址的IPv4地址组）。本端从中选择一个IPv4地址使用，并保持负载均衡。 




功能说明 


本配置用于配置IPv4地址组编号。IPv4地址组是一个或多个IPv4地址的集合。为便于在其它配置命令中引用IPv4地址组，需要给IPv4地址组指定一个编号。 

当启用本地NRF功能时，需要配置该组命令。该配置被对端NF基本信息配置引用。如果不配置，则在对端NF基本信息配置中无法配置IPv4地址组参数，本地NRF返回的服务提供者的NF Profile中不携带ipv4Addresses参数。 




子主题： 






#### 新增IPv4地址组编号配置(ADD SBIIPV4ADDRARRID) 
#### 新增IPv4地址组编号配置(ADD SBIIPV4ADDRARRID) 


功能说明 

本命令用于新增IPv4地址组编号。IPv4地址组是一个或多个IPv4地址的集合。为了便于在其它配置命令中引用IPv4地址组，需要给IPv4地址组指定一个编号。 

当启用本地NRF功能，且需要添加一个新的IPv4地址组编号时，使用该命令。命令执行成功，再将对端网络功能（NF）的IPv4地址加入新增的IPv4地址组后，IPv4地址组编号可以被对端NF基本信息配置引用。 


注意事项 

通过IPv4地址组参数配置（[ADD SBIIPV4ADDRARRPARAM]命令）在IPv4地址组内添加对端NF一个或多个IPv4地址后，IPv4地址组才能正常使用。

如果IPv4地址组内无对端NF的IPv4地址，当对端NF基本信息配置引用了该IPv4地址组后，会导致该NF的NF Profile组装失败，本地NRF发现失败。 

系统支持的该配置项的最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号。




命令举例 


`
新增IPv4地址组编号配置：IPv4地址组编号为1。 
ADD SBIIPV4ADDRARRID:ARRAYID=1
` 


#### 删除IPv4地址组编号配置(DEL SBIIPV4ADDRARRID) 
#### 删除IPv4地址组编号配置(DEL SBIIPV4ADDRARRID) 


功能说明 

本命令用于删除IPv4地址组编号。当IPv4地址组编号不再使用时，使用该命令删除。 


注意事项 

IPv4地址编号被对端NF基本信息配置引用，必须先去除对端NF基本信息配置中的引用，才能删除IPv4地址编号。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号。




命令举例 


`
删除IPv4地址组编号配置：IPv4地址组编号为1。
DEL SBIIPV4ADDRARRID:ARRAYID=1
` 


#### 查询IPv4地址组编号配置(SHOW SBIIPV4ADDRARRID) 
#### 查询IPv4地址组编号配置(SHOW SBIIPV4ADDRARRID) 


功能说明 

本命令用于查询IPv4地址组编号。当需要查询IPv4地址组编号的配置情况时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号。




命令举例 


`
查询IPv4地址组编号配置：IPv4地址组编号为1。
SHOW SBIIPV4ADDRARRID:ARRAYID=1

(No.5) : SHOW SBIIPV4ADDRARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IPv4地址组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-11-11 15:02:04 耗时: 0.519 秒

` 


### IPv4地址组参数配置 
### IPv4地址组参数配置 


背景知识 


IPv4（Internet Protocol version 4，网际协议版本4）通常被写作点分十进制的形式，即四个字节被分开用十进制写出，中间用点分隔，比如：192.168.1.1。 

IPv4地址组是一个或多个IPv4地址的集合。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NF Profile会携带ipv4Addresses参数（包含一个或多个IPv4地址的IPv4地址组）。本端从中选择一个IPv4地址使用，并保持负载均衡。 




功能说明 


本配置用于对IPv4地址组内的IPv4地址进行管理。当启用本地NRF功能时，需要配置该组命令。 

在IPv4地址组内必须添加一个或多个IPv4地址。如果IPv4地址组内无IPv4地址，在被对端NF基本信息配置引用后，会导致对端NF的NF Profile组装失败，本地NRF发现失败。 




子主题： 






#### 新增IPv4地址组参数配置(ADD SBIIPV4ADDRARRPARAM) 
#### 新增IPv4地址组参数配置(ADD SBIIPV4ADDRARRPARAM) 


功能说明 

本命令用于新增IPv4地址组参数配置。 

当开启本地NRF功能，且需要在Pv4地址组中增加对端NF的IPv4地址时使用该命令。 

新增的IPv4地址组，需要使用本命令在组内添加一个或者多个IPv4地址才可以被对端NF基本信息配置引用。 


注意事项 

组内无IPv4地址的地址组被对端NF基本信息配置引用后，会导致对端NF的NF Profile组装失败，影响本地NRF发现。 

执行一次命令只能将一条IPv4地址加入地址组，一个地址组内的最大地址数受配置项容量的限制，系统支持的该配置项最大记录数为8192。 

配置索引只用来标识该配置记录，不会被其他配置引用。配置索引不可以重复。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




命令举例 


`
新增IPv4地址组参数配置：配置索引为1，IPv4地址组编号为1，IPv4地址编号为1。 
ADD SBIIPV4ADDRARRPARAM:INDEX=1,ARRAYID=1,IPV4=1
` 


#### 修改IPv4地址组参数配置(SET SBIIPV4ADDRARRPARAM) 
#### 修改IPv4地址组参数配置(SET SBIIPV4ADDRARRPARAM) 


功能说明 

本命令用于修改IPv4地址组参数配置，当需要修改IPv4地址组内的IPv4地址时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




命令举例 


`
修改IPv4地址组参数配置：配置索引为1，IPv4地址组编号为1，IPv4地址编号为1。 
SET SBIIPV4ADDRARRPARAM:INDEX=1,ARRAYID=1,IPV4=1
` 


#### 删除IPv4地址组参数配置(DEL SBIIPV4ADDRARRPARAM) 
#### 删除IPv4地址组参数配置(DEL SBIIPV4ADDRARRPARAM) 


功能说明 

本命令用于删除IPv4地址组参数配置，当需要删除IPv4地址组内的IPv4地址时，使用该命令。 


注意事项 

删除IPv4地址组内的最后一个IPv4地址时，需要先去除对端NF基本信息配置中对地址组编号的引用，再删除该IPv4地址。 

不含IPv4地址的地址组在被对端NF基本信息配置所引用后，会导致对端NF的NF Profile组装失败，本地NRF发现失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




命令举例 


`
删除IPv4地址组参数配置：配置索引为1。
DEL SBIIPV4ADDRARRPARAM:INDEX=1
` 


#### 查询IPv4地址组参数配置(SHOW SBIIPV4ADDRARRPARAM) 
#### 查询IPv4地址组参数配置(SHOW SBIIPV4ADDRARRPARAM) 


功能说明 

本命令用于查询IPv4地址组参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv4地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址组编号，该编号通过SHOW SBIIPV4ADDRARRID命令查询。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，该编号通过SHOW SBIIPV4ADDR命令查询。




命令举例 


`
查询IPv4地址组参数配置：配置索引为1。
SHOW SBIIPV4ADDRARRPARAM:INDEX=1

(No.7) : SHOW SBIIPV4ADDRARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 IPv4地址组编号 IPv4地址编号 
----------------------------------------------------
复制 修改 删除 1        1              1            
----------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-11 15:03:42 耗时: 0.513 秒

` 


## IPv6地址配置 
## IPv6地址配置 


背景知识 


IPv6（Internet Protocol version 6，网际协议版本6），是用于替代IPv4（Internet Protocol version 4，网际协议版本4）的新一代IP协议。IPv6的地址长度为128位，典型的IPv6地址表示方法：A345:1026:B3F5:0000:DCAA:1122:3344:5678。  

IPv6地址组是一个或多个IPv6地址的集合。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的服务提供者的NF Profile携带ipv6Addresses参数（包含一个或多个IPv6地址的IPv6地址组）。 

IP端点是网络功能服务侦听入向侧服务请求的IP地址和端口信息。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的服务提供者的NF Profile中会携带ipEndPoints参数（包含一个或多个IP端点信息的IP端点信息组）。 




功能说明 


本配置用于配置服务提供者的IPv6地址，当启用本地NRF功能时，需要使用该组命令。IPv6地址配置被IPv6地址组参数配置、IP端点配置引用。 




子主题： 






### 新增IPv6地址配置(ADD SBIIPV6ADDR) 
### 新增IPv6地址配置(ADD SBIIPV6ADDR) 


功能说明 

本命令用于新增IPv6地址配置，即给IPv6地址增加编号。 

当启用本地NRF功能时，需要执行此命令增加服务提供者（对端）网络功能（NF）的IPv6地址。命令执行成功后，新增的IPv6地址编号可以被IPv6地址组参数配置、IP端点配置引用。 

IPv6地址组是一个或多个IPv6地址的集合。一个网络功能可能拥有多个IPv6地址。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回对端的NF Profile携带的ipv6Addresses参数（包含一个或多个IPv6地址的IPv6地址组）。 

IP端点是网络功能服务侦听入向侧服务请求的IP地址和端口信息。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回对端的NF Profile包含的服务中会携带IP End Points参数（包含一个或多个IP端点信息的IP端点信息组）。 


注意事项 

系统支持的该配置项的最大记录数为8192。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




命令举例 


`
增加IPv6地址配置：编号为1，IP地址为“3480:e024::1”。 
ADD SBIIPV6ADDR:ID=1,IP="3480:e024::1"
` 


### 修改IPv6地址配置(SET SBIIPV6ADDR) 
### 修改IPv6地址配置(SET SBIIPV6ADDR) 


功能说明 

本命令用于修改IPv6地址配置，即变更IPv6地址编号所标识的IPv6地址。当服务提供者（对端）网络功能（NF）的IPv6地址发生变更时，执行该命令。 


注意事项 

IPv6地址编号无法修改，只允许修改IPv6地址。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




命令举例 


`
修改IPv6地址配置：编号为1，IP地址为“3480:e024::1”。 
SET SBIIPV6ADDR:ID=1,IP="3480:e024::1"
` 


### 删除IPv6地址配置(DEL SBIIPV6ADDR) 
### 删除IPv6地址配置(DEL SBIIPV6ADDR) 


功能说明 

本命令用于删除IPv6地址配置。当服务提供者（对端）网络功能（NF）的IPv6地址不再使用时，执行该命令。 


注意事项 

IPv6地址配置编号被IPv6地址组参数配置、IP端点配置引用，必须先去除IPv6地址组参数、IP端点配置配置中的引用，才能删除IPv6地址配置编号。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




命令举例 


`
删除IPv6地址配置：编号为1。
DEL SBIIPV6ADDR:ID=1
` 


### 查询IPv6地址配置(SHOW SBIIPV6ADDR) 
### 查询IPv6地址配置(SHOW SBIIPV6ADDR) 


功能说明 

本命令用于查询IPv6地址配置。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址的编号，用于标识一个IPv6地址。IPv6地址编号不可重复。
IP|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv6地址编号对应的IPv6地址，该地址通常是服务提供者（对端）网络功能（NF）的IPv6地址。




命令举例 


`
查询IPv6地址配置：编号为1。
SHOW SBIIPV6ADDR:ID=1

(No.9) : SHOW SBIIPV6ADDR:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IPv6地址编号 IP地址       
-----------------------------------------
复制 修改 删除 1            3480:e024::1 
-----------------------------------------
记录数：1
执行成功 开始时间:2020-11-11 15:10:32 耗时: 0.592 秒

` 


## IPv6地址组配置 
## IPv6地址组配置 


背景知识 


IPv6（Internet Protocol version 6，网际协议版本6），是用于替代IPv4（Internet Protocol version 4，网际协议版本4）的新一代IP协议。IPv6的地址长度为128位，典型的IPv6地址表示方法：A345:1026:B3F5:0000:DCAA:1122:3344:5678。  

IPv6地址组是一个或多个IPv6地址的集合。当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的服务提供者的NF Profile携带ipv6Addresses参数（包含一个或多个IPv6地址的IPv6地址组）。本端从中选择一个IPv6地址使用，并照顾到负载均衡。 




功能说明 


IPv6地址组配置是给IPv6地址组指定一个编号，便于在其它配置（例如，对端NF基本信息配置）中引用IPv6地址组。 

启用本地NRF功能时，需要在本地配置服务提供者的IPv6地址组。 

新增IPv6地址组后，必须通过IPv6地址组参数配置在组内添加一个或多个IPv6地址。组内无IPv6地址的地址组在被对端NF基本信息配置引用后，会导致对端NF的NFProfile的组装失败，本地NRF发现失败。 




子主题： 






### IPv6地址组编号配置 
### IPv6地址组编号配置 


背景知识 


IPv6（Internet Protocol version 6，网际协议版本6），是用于替代IPv4（Internet Protocol version 4，网际协议版本4）的新一代IP协议。IPv6的地址长度为128位，典型的IPv6地址表示方法：A345:1026:B3F5:0000:DCAA:1122:3344:5678。  

IPv6地址组是一个或者多个IPv6地址的集合。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile会携带ipv6Addresses参数，这是一个IPv6地址组，包含一个或者多个IPv6地址，本端从中选择一个IPv6地址使用，并保持负载均衡。 




功能说明 


本配置用于配置IPv6地址组编号。IPv6地址组是一个或多个IPv6地址的集合。为便于在其它配置命令中引用IPv6地址组，需要给IPv6地址组指定一个编号。 

当启用本地NRF功能时，需要配置该组命令。该配置被对端NF基本信息配置引用。如果不配置，则在对端NF基本信息配置中无法配置IPv6地址组参数，本地NRF返回的服务提供者的NF Profile中不携带ipv6Addresses参数。 




子主题： 






#### 新增IPv6地址组编号配置(ADD SBIIPV6ADDRARRID) 
#### 新增IPv6地址组编号配置(ADD SBIIPV6ADDRARRID) 


功能说明 

本命令用于新增IPv6地址组编号。IPv6地址组是一个或多个IPv6地址的集合。为了便于在其它配置命令中引用IPv6地址组，需要给IPv6地址组指定一个编号。 

当启用本地NRF功能，且需要添加一个新的IPv6地址组编号时，使用该命令。命令执行成功，再将对端网络功能（NF）的IPv6地址加入新增的IPv6地址组后，IPv6地址组编号可以被对端NF基本信息配置引用。 


注意事项 

通过IPv6地址组参数配置（[ADD SBIIPV6ADDRARRPARAM]命令）在IPv6地址组内添加对端NF一个或多个IPv6地址后，IPv6地址组才能正常使用。

如果IPv6地址组内无对端NF的IPv6地址，当对端NF基本信息配置引用了该IPv6地址组后，会导致该NF的NF Profile组装失败，本地NRF发现失败。 

系统支持的该配置项的最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6地址组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号。




命令举例 


`
新增IPv6地址组编号配置：IPv6地址组编号为1。 
ADD SBIIPV6ADDRARRID:ARRAYID=1
` 


#### 删除IPv6地址组编号配置(DEL SBIIPV6ADDRARRID) 
#### 删除IPv6地址组编号配置(DEL SBIIPV6ADDRARRID) 


功能说明 

本命令用于删除IPv6地址组编号。当IPv6地址组编号不再使用时，使用该命令删除。 


注意事项 

IPv6地址编号被对端NF基本信息配置引用，必须先去除对端NF基本信息配置中的引用，才能删除IPv6地址编号。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6地址组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号。




命令举例 


`
删除IPv6地址组编号配置：IPv6地址组编号为1。
DEL SBIIPV6ADDRARRID:ARRAYID=1
` 


#### 查询IPv6地址组编号配置(SHOW SBIIPV6ADDRARRID) 
#### 查询IPv6地址组编号配置(SHOW SBIIPV6ADDRARRID) 


功能说明 

本命令用于查询IPv6地址组编号。当需要查询IPv6地址组编号的配置情况时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号。




命令举例 


`
查询IPv6地址组编号配置：IPv6地址组编号为1。
SHOW SBIIPV6ADDRARRID:ARRAYID=1

(No.12) : SHOW SBIIPV6ADDRARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IPv6地址组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-11-11 15:41:55 耗时: 0.527 秒

` 


### IPv6地址组参数配置 
### IPv6地址组参数配置 


背景知识 


IPv6（Internet Protocol version 6，网际协议版本6），是用于替代IPv4（Internet Protocol version 4，网际协议版本4）的新一代IP协议。IPv6的地址长度为128位，典型的IPv6地址表示方法：A345:1026:B3F5:0000:DCAA:1122:3344:5678。  

IPv6地址组是一个或者多个IPv6地址的集合。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile会携带ipv6Addresses参数，这是一个IPv6地址组，包含一个或者多个IPv6地址，本端从中选择一个IPv6地址使用，并保持负载均衡。 




功能说明 


本配置用于对IPv6地址组内的IPv6地址进行管理。当启用本地NRF功能时，需要配置该组命令。 

在IPv6地址组内必须添加一个或多个IPv6地址。如果IPv6地址组内无IPv6地址，在被对端NF基本信息配置引用后，会导致对端NF的NF Profile组装失败，本地NRF发现失败。 




子主题： 






#### 新增IPv6地址组参数配置(ADD SBIIPV6ADDRARRPARAM) 
#### 新增IPv6地址组参数配置(ADD SBIIPV6ADDRARRPARAM) 


功能说明 

本命令用于新增IPv6地址组参数配置。 

当开启本地NRF功能，且需要在IPv6地址组中增加对端NF的IPv6地址时使用该命令。 

新增的IPv6地址组，需要使用本命令在组内添加一个或者多个IPv6地址才可以被对端NF基本信息配置引用。 


注意事项 

组内无IPv6地址的地址组被对端NF基本信息配置引用后，会导致对端NF的NF Profile组装失败，影响本地NRF发现。 

执行一次命令只能将一条IPv6地址加入地址组，一个地址组内的最大地址数受配置项容量的限制，系统支持的该配置项最大记录数为8192。 

配置索引只用来标识该配置记录，不会被其他配置引用。配置索引不可以重复。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




命令举例 


`
新增IPv6地址组参数配置：配置索引为1，IPv6地址组编号为1，IPv6地址编号为1。 
ADD SBIIPV6ADDRARRPARAM:INDEX=1,ARRAYID=1,IPV6=1
` 


#### 修改IPv6地址组参数配置(SET SBIIPV6ADDRARRPARAM) 
#### 修改IPv6地址组参数配置(SET SBIIPV6ADDRARRPARAM) 


功能说明 

本命令用于修改IPv6地址组参数配置，当需要修改IPv6地址组内的IPv6地址时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




命令举例 


`
修改IPv6地址组参数配置：配置索引为1，IPv6地址组编号为1，IPv6地址编号为1。 
SET SBIIPV6ADDRARRPARAM:INDEX=1,ARRAYID=1,IPV6=1
` 


#### 删除IPv6地址组参数配置(DEL SBIIPV6ADDRARRPARAM) 
#### 删除IPv6地址组参数配置(DEL SBIIPV6ADDRARRPARAM) 


功能说明 

本命令用于删除IPv6地址组参数配置，当需要删除IPv6地址组内的IPv6地址时，使用该命令。 


注意事项 

删除IPv6地址组内的最后一个IPv6地址时，需要先去除对端NF基本信息配置中对地址组编号的引用，再删除该IPv6地址。 

不含IPv6地址的地址组在被对端NF基本信息配置所引用后，会导致对端NF的NF Profile组装失败，本地NRF发现失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




命令举例 


`
删除IPv6地址组参数配置：配置索引为1。
DEL SBIIPV6ADDRARRPARAM:INDEX=1
` 


#### 查询IPv6地址组参数配置(SHOW SBIIPV6ADDRARRPARAM) 
#### 查询IPv6地址组参数配置(SHOW SBIIPV6ADDRARRPARAM) 


功能说明 

本命令用于查询IPv6地址组参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是IPv6地址组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址组编号，该编号通过SHOW SBIIPV6ADDRARRID命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，该编号通过SHOW SBIIPV6ADDR命令查询。




命令举例 


`
查询IPv6地址组参数配置：配置索引为1。
SHOW SBIIPV6ADDRARRPARAM:INDEX=1

(No.14) : SHOW SBIIPV6ADDRARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 IPv6地址组编号 IPv6地址编号 
----------------------------------------------------
复制 修改 删除 1        1              1            
----------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-11 15:44:10 耗时: 0.543 秒

` 


## IP端点配置 
## IP端点配置 


背景知识 


IP端点是网络功能(NF)的服务用于侦听入向侧服务请求的IP地址和端口信息（包括IPv4和/或IPv6地址）。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带ipEndPoints，这是一组IP端点信息，本端从中选择一个作为本次服务请求的对端IP地址和端口信息。在本地NRF功能开启时，IP端点配置会呈现在对端NFProfile的ipEndPoints数组中。 




功能说明 


该组命令用于配置服务提供者用于侦听入向侧服务请求的IP地址和端口信息（包括IPv4或IPv6地址），当启用本地NRF功能时，需要配置该组命令。 

该配置被IP端点组参数配置引用，最终呈现在本地NRF配置的对端NFProfile的ipEndPoints数组中。由于该引用关系是强制的，如果不配置IP端点，则IP端点组参数也无法配置成功。 




子主题： 






### 新增IP端点配置(ADD SBIIPENDPOINT) 
### 新增IP端点配置(ADD SBIIPENDPOINT) 


功能说明 

该命令用于新增IP端点配置。当启用本地NRF功能时，执行该命令。命令执行成功后，本配置可以被IP端点组参数配置引用。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号。
IPV4|IPv4地址编号|参数可选性: 必须单选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 必须单选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。
PORT|端口|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置端口号，范围1-65535。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点配置编号。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。
PORT|端口|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置端口号，范围1-65535。




命令举例 


`
新增IP端点配置：IP端点编号为1，IPv4地址编号为1，端口为8080。 
ADD SBIIPENDPOINT:INDEX=1,IPV4=1,PORT=8080
` 


### 修改IP端点配置(SET SBIIPENDPOINT) 
### 修改IP端点配置(SET SBIIPENDPOINT) 


功能说明 

该命令用于修改IP端点配置。当IP端点编号关联的IPv4地址编号、IPv6地址编号、端口发生变更时，执行该命令。 


注意事项 

IP端点配置编号被IP端点组参数配置引用后，修改IP端点配置对IP端点组参数配置无影响。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号。
IPV4|IPv4地址编号|参数可选性: 必须单选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 必须单选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。
PORT|端口|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置端口号，范围1-65535。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点配置编号。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。
PORT|端口|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置端口号，范围1-65535。




命令举例 


`
修改IP端点编号为1的IP端点配置，将IPv4地址编号修改为2。 
SET SBIIPENDPOINT:INDEX=1,IPV4=2
` 


### 删除IP端点配置(DEL SBIIPENDPOINT) 
### 删除IP端点配置(DEL SBIIPENDPOINT) 


功能说明 

本命令用于删除IP端点配置。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点配置编号。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。
PORT|端口|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置端口号，范围1-65535。




命令举例 


`
删除IP端点编号为1的IP端点配置。
DEL SBIIPENDPOINT:INDEX=1
` 


### 查询IP端点配置(SHOW SBIIPENDPOINT) 
### 查询IP端点配置(SHOW SBIIPENDPOINT) 


功能说明 

该命令用于查询IP端点配置，包括IP端点编号，及其关联的IPv4地址编号、IPv6地址编号、端口。 


注意事项 

IP端点配置编号被IP端点组参数配置引用后，必须先删除IP端点组参数配置，才能删除被引用的IP端点配置。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点配置编号。
IPV4|IPv4地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址编号，IPv4地址编号通过SHOW SBIIPV4ADDR命令查询。
IPV6|IPv6地址编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6地址编号，IPv6地址编号通过SHOW SBIIPV6ADDR命令查询。
PORT|端口|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置端口号，范围1-65535。




命令举例 


`
查询IP端点编号为1的IP端点配置。
SHOW SBIIPENDPOINT:INDEX=1

(No.2) : SHOW SBIIPENDPOINT:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IP端点编号 IPv4地址编号 IPv6地址编号 端口 
-------------------------------------------------------------
复制 修改 删除 1          1                         8080 
-------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:06:51 耗时: 0.566 秒

` 


## IP端点组配置 
## IP端点组配置 


背景知识 


IP端点是网络功能(NF)的服务用于侦听入向侧服务请求的IP地址和端口信息（包括IPv4和/或IPv6地址）。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带ipEndPoints，这是一组IP端点信息，本端从中选择一个作为本次服务请求的对端IP地址和端口信息。在本地NRF功能开启时，IP端点配置会呈现在对端NFProfile的ipEndPoints数组中。 




功能说明 


IP端点组配置即对应本地NRF配置的对端NFProfile的ipEndPoints数组，如果不配置，则对端NFProfile缺少ipEndPoints数组，本端如果需要请求对端提供的服务，则服务请求无法发送成功。当启用本地NRF功能时，需要配置该组命令。 

IP端点组配置包括IP端点组编号配置和IP端点组参数配置，一个IP端点组下面可以包含若干个IP端点组参数。 




子主题： 






### IP端点组编号配置 
### IP端点组编号配置 


背景知识 


IP端点是网络功能(NF)的服务用于侦听入向侧服务请求的IP地址和端口信息（包括IPv4和/或IPv6地址）。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带ipEndPoints，这是一组IP端点信息，本端从中选择一个作为本次服务请求的对端IP地址和端口信息。在本地NRF功能开启时，IP端点配置会呈现在对端NFProfile的ipEndPoints数组中。 




功能说明 


IP端点组编号配置用于配置一个IP端点组，一个IP端点组包含了若干个IP端点组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被对端NF服务实例配置引用，最终呈现在本地NRF配置的对端NFProfile的ipEndPoints数组中。如果不配置，则对端NFProfile缺少ipEndPoints数组，本端如果需要请求对端提供的服务，服务请求无法发送成功。 




子主题： 






#### 新增IP端点组编号配置(ADD SBIIPENDPOINTARRID) 
#### 新增IP端点组编号配置(ADD SBIIPENDPOINTARRID) 


功能说明 

该命令用于新增IP端点组编号。当启用本地NRF功能时，执行该命令。命令执行成功后，本配置被IP端点组参数配置引用。命令执行成功后，服务使用者如果需要使用服务提供者提供的服务，则根据配置的组信息向服务提供者发送服务请求。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IP端点组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号。




命令举例 


`
新增IP端点组编号配置：IP端点组编号为1。 
ADD SBIIPENDPOINTARRID:ARRAYID=1
` 


#### 删除IP端点组编号配置(DEL SBIIPENDPOINTARRID) 
#### 删除IP端点组编号配置(DEL SBIIPENDPOINTARRID) 


功能说明 

本命令用于删除IP端点组编号。 


注意事项 

IP端点组编号被IP端点组参数配置引用后，必须先删除IP端点组参数配置，才能删除被引用的IP端点组配置。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IP端点组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号。




命令举例 


`
删除IP端点组编号为1的IP端点组编号配置。
DEL SBIIPENDPOINTARRID:ARRAYID=1
` 


#### 查询IP端点组编号配置(SHOW SBIIPENDPOINTARRID) 
#### 查询IP端点组编号配置(SHOW SBIIPENDPOINTARRID) 


功能说明 

本命令用于查询IP端点组编号。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号。




命令举例 


`
查询IP端点组编号为1的IP端点组编号配置。
SHOW SBIIPENDPOINTARRID:ARRAYID=1

(No.10) : SHOW SBIIPENDPOINTARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IP端点组编号 
--------------------------------
复制 删除      1                
--------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:16:47 耗时: 0.523 秒

` 


### IP端点组参数配置 
### IP端点组参数配置 


背景知识 


IP端点是网络功能(NF)的服务用于侦听入向侧服务请求的IP地址和端口信息（包括IPv4和/或IPv6地址）。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带ipEndPoints，这是一组IP端点信息，本端从中选择一个作为本次服务请求的对端IP地址和端口信息。在本地NRF功能开启时，IP端点配置会呈现在对端NFProfile的ipEndPoints数组中。 




功能说明 

IP端点组参数配置用于配置一个IP端点归属于哪个IP端点组。当启用本地NRF功能时，需要配置该组命令。
如果不配置IP端点组参数，则一个IP端点不能归属于一个具体的IP端点组，本端无法获取对端的IP端点信息，本端如果需要请求对端提供的服务，服务请求无法发送成功。 




子主题： 






#### 新增IP端点组参数配置(ADD SBIIPENDPOINTARRPARAM) 
#### 新增IP端点组参数配置(ADD SBIIPENDPOINTARRPARAM) 


功能说明 

该命令用于新增IP端点组参数配置。当启用本地NRF功能时，执行该命令。命令执行成功后，服务使用者如果需要使用服务提供者提供的服务，则根据配置的组信息向服务提供者发送服务请求。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




命令举例 


`
新增IP端点组参数配置，其中配置索引为1，IP端点组编号为1，IP端点编号为1。 
ADD SBIIPENDPOINTARRPARAM:INDEX=1,ARRAYID=1,IPENDPOINT=1
` 


#### 修改IP端点组参数配置(SET SBIIPENDPOINTARRPARAM) 
#### 修改IP端点组参数配置(SET SBIIPENDPOINTARRPARAM) 


功能说明 

该命令用于修改IP端点组参数配置。当配置索引关联的IP端点组编号、IP端点编号发生变更时，执行该命令。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




命令举例 


`
修改IP端点组参数配置，其中配置索引为1，IP端点组编号为1，将IP端点编号修改为2。 
SET SBIIPENDPOINTARRPARAM:INDEX=1,ARRAYID=1,IPENDPOINT=2
` 


#### 删除IP端点组参数配置(DEL SBIIPENDPOINTARRPARAM) 
#### 删除IP端点组参数配置(DEL SBIIPENDPOINTARRPARAM) 


功能说明 

本命令用于删除IP端点组参数配置。 


注意事项 

如果删除IP端点组参数配置，则在服务使用者请求服务时，无法通过ipEndPoints获取到服务提供者的IpEndPoint，也就无法向该IpEndPoint的服务提供者发送服务请求。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




命令举例 


`
删除配置索引为1的IP端点组参数配置。
DEL SBIIPENDPOINTARRPARAM:INDEX=1
` 


#### 查询IP端点组参数配置(SHOW SBIIPENDPOINTARRPARAM) 
#### 查询IP端点组参数配置(SHOW SBIIPENDPOINTARRPARAM) 


功能说明 

该命令用于查询IP端点组参数配置，即查询配置索引关联的IP端点组编号、IP端点编号。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点组编号，IP端点组编号通过SHOW SBIIPENDPOINTARRID命令查询。
IPENDPOINT|IP端点编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP端点编号，IP端点编号通过SHOW SBIIPENDPOINT命令查询。




命令举例 


`
查询配置索引为1的IP端点组参数配置。
SHOW SBIIPENDPOINTARRPARAM:INDEX=1

(No.11) : SHOW SBIIPENDPOINTARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 IP端点组编号 IP端点编号 
--------------------------------------------------------
复制 修改 删除 1        1            1              
--------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:17:26 耗时: 0.512 秒

` 


## NF服务版本组配置 
## NF服务版本组配置 


背景知识 


NF（网络功能，Network Function）服务版本是NF服务支持的API版本号，包含了URI中用于访问API的服务实例的版本号和API完整版本号。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带versions，这是一组NF服务版本信息，服务使用者从中选择一个，把其中的API URI版本号作为本次服务请求的URI中使用的版本号。在本地NRF功能开启时，NF服务版本组配置会呈现在对端NFProfile的versions数组中。 




功能说明 


NF服务版本组配置对应本地NRF配置出来的对端NFProfile的versions数组。如果不配置，则对端NFProfile缺少versions数组，本端如果需要请求对端提供的服务，服务请求的URI不能携带正确的版本号，可能导致服务请求发送失败以及业务流程失败。当启用本地NRF功能时，需要配置该组命令。 

NF服务版本组配置包括NF服务版本组编号配置和NF服务版本组参数配置，一个NF服务版本组下面可以包含若干个NF服务版本组参数。 




子主题： 






### NF服务版本组编号配置 
### NF服务版本组编号配置 


背景知识 


NF（网络功能，Network Function）服务版本是NF服务支持的API版本号，包含了URI中用于访问API的服务实例的版本号和API完整版本号。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带versions，这是一组NF服务版本信息，服务使用者从中选择一个，把其中的API URI版本号作为本次服务请求的URI中使用的版本号。在本地NRF功能开启时，NF服务版本组配置会呈现在对端NFProfile的versions数组中。 




功能说明 


NF服务版本组编号配置用于配置一个NF服务版本组的编号，一个NF服务版本组包含了若干个NF服务版本组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被对端NF服务实例配置引用，最终呈现在本地NRF配置出来的对端NFProfile的versions数组中。如果不配置，则对端NFProfile缺少versions数组，本端如果需要请求对端提供的服务，服务请求的URI不能携带正确的版本号，可能导致服务请求发送失败以及业务流程失败。 




子主题： 






#### 新增NF服务版本组编号配置(ADD SBINFSVERSIONARRID) 
#### 新增NF服务版本组编号配置(ADD SBINFSVERSIONARRID) 


功能说明 

该命令用于新增NF服务版本组编号。当启用本地NRF功能时，执行该命令。命令执行成功后，当服务使用者从NRF获取到服务提供者的服务版本组时，把其中一个的API URI版本号作为本次服务请求的URI中使用的版本号。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号。




命令举例 


`
新增NF服务版本组编号配置，其中NF服务版本组编号为1。 
ADD SBINFSVERSIONARRID:ARRAYID=1
` 


#### 删除NF服务版本组编号配置(DEL SBINFSVERSIONARRID) 
#### 删除NF服务版本组编号配置(DEL SBINFSVERSIONARRID) 


功能说明 

本命令用于删除NF服务版本组编号。 


注意事项 

删除后，服务使用者（本端）无法获取服务提供者（对端）的API URI版本号，本端如果需要请求对端提供的服务，服务请求的URI不能携带正确的版本号，可能导致服务请求发送失败以及业务流程失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号。




命令举例 


`
删除NF服务版本组编号为1的NF服务版本组编号配置。
DEL SBINFSVERSIONARRID:ARRAYID=1
` 


#### 查询NF服务版本组编号配置(SHOW SBINFSVERSIONARRID) 
#### 查询NF服务版本组编号配置(SHOW SBINFSVERSIONARRID) 


功能说明 

本命令用于查询NF服务版本组编号。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号。




命令举例 


`
查询所有的NF服务版本组编号配置。
SHOW SBINFSVERSIONARRID;

(No.14) : SHOW SBINFSVERSIONARRID;
-----------------CommonS_HTTP_LB_0----------------
操作维护       NF服务版本组编号 
--------------------------------
复制 删除      1                
--------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:19:56 耗时: 0.509 秒

` 


### NF服务版本组参数配置 
### NF服务版本组参数配置 


背景知识 


NF（网络功能，Network Function）服务版本是NF服务支持的API版本号，包含了URI中用于访问API的服务实例的版本号和API完整版本号。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带versions，这是一组NF服务版本信息，服务使用者从中选择一个，把其中的API URI版本号作为本次服务请求的URI中使用的版本号。在本地NRF功能开启时，NF服务版本组配置会呈现在对端NFProfile的versions数组中。 




功能说明 


NF服务版本组参数配置包含一个API URI版本号和一个API完整版本号，以及该组参数归属于哪个NF服务版本组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置NF服务版本组参数，则NF服务版本组没有具体内容，本端无法获取对端的API URI版本号，本端如果需要请求对端提供的服务，服务请求的URI不能携带正确的版本号，可能导致服务请求发送失败以及业务流程失败。 




子主题： 






#### 新增NF服务版本组参数配置(ADD SBINFSVERSIONARRPARAM) 
#### 新增NF服务版本组参数配置(ADD SBINFSVERSIONARRPARAM) 


功能说明 

该命令用于新增NF服务版本组参数配置。当启用本地NRF功能时，执行该命令。命令执行成功后，当服务使用者从NRF获取到服务提供者的服务版本组时，把其中一个的API URI版本号作为本次服务请求的URI中使用的版本号。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 必选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 必选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




命令举例 


`
新增NF服务版本组参数配置，其中配置索引为1，NF服务版本组编号为1，API URI版本号为"v1.0"，API完整版号本为"1.0.0.alpha-1"。 
ADD SBINFSVERSIONARRPARAM:INDEX=1,ARRAYID=1,APIVERSIONINURI="v1.0",APIFULLVERSION="1.0.0.alpha-1"
` 


#### 修改NF服务版本组参数配置(SET SBINFSVERSIONARRPARAM) 
#### 修改NF服务版本组参数配置(SET SBINFSVERSIONARRPARAM) 


功能说明 

该命令用于修改NF服务版本组参数配置。当配置索引关联的NF服务版本组编号、API URI版本号、API完整版本号发生变更时，执行该命令。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




命令举例 


`
修改NF服务版本组参数配置，其中配置索引为1，NF服务版本组编号为1，将API URI版本号改为"v1.1"。
SET SBINFSVERSIONARRPARAM:INDEX=1,ARRAYID=1,APIVERSIONINURI="v1.1"
` 


#### 删除NF服务版本组参数配置(DEL SBINFSVERSIONARRPARAM) 
#### 删除NF服务版本组参数配置(DEL SBINFSVERSIONARRPARAM) 


功能说明 

该命令用于删除NF服务版本组参数配置。 


注意事项 

如果删除NF服务版本组编号，则在服务使用者请求服务时，无法通过NF服务版本组编号获取到服务提供者的API版本号。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




命令举例 


`
删除配置索引为1的NF服务版本组参数配置。
DEL SBINFSVERSIONARRPARAM:INDEX=1
` 


#### 查询NF服务版本组参数配置(SHOW SBINFSVERSIONARRPARAM) 
#### 查询NF服务版本组参数配置(SHOW SBINFSVERSIONARRPARAM) 


功能说明 

该命令用于查询NF服务版本组参数配置，即查询配置索引关联的NF服务版本组编号、API URI版本号、API完整版本号。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。
ARRAYID|NF服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务版本组编号，NF服务版本组编号通过SHOW SBINFSVERSIONARRID命令查询。
APIVERSIONINURI|API URI版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API URI版本号，即访问API的URI中使用的服务实例的版本号。
APIFULLVERSION|API完整版本号|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API的完整版本号，建议格式为以'.'分隔、至少分为3段的字符串。




命令举例 


`
查询所有的NF服务版本组参数配置。
SHOW SBINFSVERSIONARRPARAM;

(No.15) : SHOW SBINFSVERSIONARRPARAM;
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 NF服务版本组编号 API URI版本号 API完整版本号 
---------------------------------------------------------------------
复制 修改 删除 1        1                v1.0          1.0.0.alpha-1 
---------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:20:45 耗时: 0.508 秒

` 


## NF服务集标识组配置 
## NF服务集标识组配置 


背景知识 


多个同类型NF（网络功能，Network Function）内为相同用户或业务区/服务区提供服务的一组同类型NF服务称为NF服务集，NF服务集标识是这个集合的全局唯一标识符。NF服务集内的服务共享上下文，当某个服务故障后，其所承担业务可以由服务集内的其他负荷分担的服务接管。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带nfServiceSetIdList，这是一组NF服务集标识。当本端选择的对端NF服务出现故障时，可以选择同一个NF服务集内的其他负荷分担的服务继续使用。 




功能说明 


NF服务集标识组配置对应本地NRF配置出来的对端NFProfile的nfServiceSetIdList数组。如果不配置，则对端NFProfile缺少nfServiceSetIdList数组，本端选择的对端NF服务出现故障时，只能尝试切换到其他的非共享上下文的NF服务，不能在同一个NF服务集中选择负荷分担的服务继续使用，可能造成业务中断。 

NF服务集标识组配置包括NF服务集标识组编号配置和NF服务集标识组参数配置，一个NF服务集标识组下面可以包含若干个NF服务集标识组参数。 




子主题： 






### NF服务集标识组编号配置 
### NF服务集标识组编号配置 


背景知识 


多个同类型NF（网络功能，Network Function）内为相同用户或业务区/服务区提供服务的一组同类型NF服务称为NF服务集，NF服务集标识是这个集合的全局唯一标识符。NF服务集内的服务共享上下文，当某个服务故障后，其所承担业务可以由服务集内的其他负荷分担的服务接管。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带nfServiceSetIdList，这是一组NF服务集标识。当本端选择的对端NF服务出现故障时，可以选择同一个NF服务集内的其他负荷分担的服务继续使用。 




功能说明 


NF服务集标识组编号配置用于配置一个NF服务集标识组的编号。一个NF服务集标识组包含了若干个NF服务集标识组参数。当启用本地NRF功能时，需要配置该组命令。 

本配置被对端NF服务实例配置引用，最终呈现在本地NRF配置出来的对端NFProfile的nfServiceSetIdList数组中。如果不配置，则对端NFProfile缺少nfServiceSetIdList数组，本端选择的对端NF服务出现故障时，只能尝试切换到其他的非共享上下文的NF服务，不能在同一个NF服务集中选择负荷分担的服务继续使用，可能造成业务中断。 




子主题： 






#### 新增NF服务集标识组编号配置(ADD SBINFSSETIDARRID) 
#### 新增NF服务集标识组编号配置(ADD SBINFSSETIDARRID) 


功能说明 

该命令用于新增NF服务集标识组编号配置。当启用本地NRF功能时，执行该命令。命令执行成功后，当服务使用者选择了其中一个NF服务集标识表示的NF服务集后，如果NF服务出现故障时，可以选择同一服务集内的其他服务继续使用。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务集标识组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号。




命令举例 


`
新增NF服务集标识组编号配置，其中NF服务集标识组编号为1。
ADD SBINFSSETIDARRID:ARRAYID=1;
` 


#### 删除NF服务集标识组编号配置(DEL SBINFSSETIDARRID) 
#### 删除NF服务集标识组编号配置(DEL SBINFSSETIDARRID) 


功能说明 

该命令用于删除NF服务集标识组编号配置。 


注意事项 

删除后，服务使用者（本端）无法获取服务提供者（对端）的NF服务集标识，本端选择的对端NF服务出现故障时，只能尝试切换到其他的非共享上下文的NF服务，不能在同一个NF服务集中选择负荷分担的服务继续使用，可能造成业务中断。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务集标识组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号。




命令举例 


`
删除NF服务集标识组编号为1的NF服务集标识组编号配置。
DEL SBINFSSETIDARRID:ARRAYID=1;
` 


#### 查询NF服务集标识组编号配置(SHOW SBINFSSETIDARRID) 
#### 查询NF服务集标识组编号配置(SHOW SBINFSSETIDARRID) 


功能说明 

该命令用于查询NF服务集标识组编号配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号。




命令举例 


`
查询所有NF服务集标识组编号配置。
SHOW SBINFSSETIDARRID

(No.12) : SHOW SBINFSSETIDARRID:
-----------------CommonS_HTTP_LB_0----------------
操作维护       NF服务集标识组编号 
------------------------------
复制 删除      1                      
------------------------------
记录数：1
执行成功开始时间:2020-12-09 11:18:08 耗时: 0.512 秒

` 


### NF服务集标识组参数配置 
### NF服务集标识组参数配置 


背景知识 


多个同类型NF（网络功能，Network Function）内为相同用户或业务区/服务区提供服务的一组同类型NF服务称为NF服务集，NF服务集标识是这个集合的全局唯一标识符。NF服务集内的服务共享上下文，当某个服务故障后，其所承担业务可以由服务集内的其他负荷分担的服务接管。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端）时，NRF返回的对端的NFProfile包含的服务中会携带nfServiceSetIdList，这是一组NF服务集标识。当本端选择的对端NF服务出现故障时，可以选择同一个NF服务集内的其他负荷分担的服务继续使用。 




功能说明 


NF服务集标识组参数配置包含一个NF服务集标识，以及该参数归属于哪个NF服务集标识组。当启用本地NRF功能时，需要配置该组命令。 

如果不配置NF服务集标识组参数，则NF服务集标识组没有具体内容，本端无法获取对端的NF服务集标识，本端选择的对端NF服务出现故障时，只能尝试切换到其他的非共享上下文的NF服务，不能在同一个NF服务集中选择负荷分担的服务继续使用，可能造成业务中断。 




子主题： 






#### 新增NF服务集标识组参数配置(ADD SBINFSSETIDARRPARAM) 
#### 新增NF服务集标识组参数配置(ADD SBINFSSETIDARRPARAM) 


功能说明 

该命令用于新增NF服务集标识组参数配置。当启用本地NRF功能时，执行该命令。命令执行成功后，当服务使用者选择了其中一个NF服务集标识表示的NF服务集后，如果NF服务出现故障时，可以选择同一服务集内的其他服务继续使用。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 必选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




命令举例 


`
新增NF服务集标识组参数配置，其中配置索引为1，NF服务集标识组编号为1，NF服务集标识为"setxyz.snnsmf-pdusession.nfi54804518-4191-46b3-955c-ac631f953ed8.5gc.mnc012.mcc345"。
ADD SBINFSSETIDARRPARAM:INDEX=1,ARRAYID=1,NFSERVSETID="setxyz.snnsmf-pdusession.nfi54804518-4191-46b3-955c-ac631f953ed8.5gc.mnc012.mcc345";
` 


#### 修改NF服务集标识组参数配置(SET SBINFSSETIDARRPARAM) 
#### 修改NF服务集标识组参数配置(SET SBINFSSETIDARRPARAM) 


功能说明 

该命令用于修改NF服务集标识组参数配置。当配置索引关联的NF服务集标识组编号、NF服务集标识发生变更时，执行该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




命令举例 


`
修改NF服务集标识组参数配置，其中配置索引为1，NF服务集标识组编号为1，将NF服务集标识改为"setabc.snnsmf-pdusession.nfi54804518-4191-46b3-955c-ac631f953ed8.5gc.mnc012.mcc345"。
SET SBINFSSETIDARRPARAM:INDEX=1,ARRAYID=1,NFSERVSETID="setabc.snnsmf-pdusession.nfi54804518-4191-46b3-955c-ac631f953ed8.5gc.mnc012.mcc345";
` 


#### 删除NF服务集标识组参数配置(DEL SBINFSSETIDARRPARAM) 
#### 删除NF服务集标识组参数配置(DEL SBINFSSETIDARRPARAM) 


功能说明 

该命令用于删除NF服务集标识组参数配置。 


注意事项 

如果删除NF服务集标识组参数配置，则在服务使用者请求服务时，无法通过NF服务集标识组编号获取到服务提供者的NF服务集标识，也就无法获取提供服务的NF服务集。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




命令举例 


`
删除配置索引为1的NF服务集标识组参数配置。
DEL SBINFSSETIDARRPARAM:INDEX=1;
` 


#### 查询NF服务集标识组参数配置(SHOW SBINFSSETIDARRPARAM) 
#### 查询NF服务集标识组参数配置(SHOW SBINFSSETIDARRPARAM) 


功能说明 

该命令用于查询NF服务集标识组参数配置，即查询配置索引关联的NF服务集标识组编号、NF服务集标识。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引
ARRAYID|NF服务集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NF服务集标识组编号，NF服务集标识组编号通过SHOW SBINFSSETIDARRID命令查询。
NFSERVSETID|NF服务集标识|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置NF服务集标识，应该按照“set.sn.nfi.5gc.mnc.mcc”的格式配置。




命令举例 


`
查询所有的NF服务集标识组参数配置。
SHOW SBINFSSETIDARRPARAM

(No.13) : SHOW SBINFSSETIDARRPARAM:
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 NF服务集标识组编号 NF服务集标识                                                                       
--------------------------------------------------------------------------------------------------------------------------                                                                        
复制 修改 删除 1        1                  setxyz.snnsmf-pdusession.nfi54804518-4191-46b3-955c-ac631f953ed8.5gc.mnc012.mcc345                                                                      
--------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:18:50 耗时: 0.518 秒

` 


## SUPI范围组配置 
## SUPI范围组配置 


背景知识 


SUPI（Subscription Permanent Identifier， 用户永久标识符）必须包含IMSI（International Mobile Subscriber Identity，国际移动用户标识）、NSI（network specific identifier，网络特定标识符）、GCI（Global Cable Identifier，全局电缆标识符）或GLI（Global Line Identifier，全局线路标识符）之一，目前系统支持的是IMSI。 

服务发现响应消息中的SUPI范围组（SupiRanges）是数组格式，每个元素（SUPI范围）用一个start和一个end表示，表明该NF为这些范围内的SUPI提供服务。即NF可以为SUPI范围组（SupiRanges）内的SUPI提供服务。 

SupiRanges在AUSF、CHF、PCF、UDM、UDR、OCS这6个NF特有信息中携带。如果以上6个NF的发现响应不带NF特有信息，或者特有信息中不携带supiRanges，表示该NF可以为所有SUPI服务。 




功能说明 


SUPI范围组数据配置包括SUPI范围组编号配置和SUPI范围组参数配置，一个SUPI范围组编号可以被若干个SUPI范围组参数引用。 

当启用本地NRF功能时，SUPI范围组配置应用于AUSF、CHF、PCF、UDM、UDR、OCS这6个NF信息配置中，用于限定这6个NF可以服务的SUPI范围。如果上述NF中SUPI范围组没有配置，则该NF可以为服务网络中的所有SUPI服务。 




子主题： 






### SUPI范围组编号配置 
### SUPI范围组编号配置 


背景知识 


SUPI（Subscription Permanent Identifier， 用户永久标识符）必须包含IMSI（International Mobile Subscriber Identity，国际移动用户标识）、NSI（network specific identifier，网络特定标识符）、GCI（Global Cable Identifier，全局电缆标识符）或GLI（Global Line Identifier，全局线路标识符）之一，目前系统支持的是IMSI。 

服务发现响应消息中的SUPI范围组（SupiRanges）是数组格式，每个元素（SUPI范围）用一个start和一个end表示，表明该NF为这些范围内的SUPI提供服务。即NF可以为SUPI范围组（SupiRanges）内的SUPI提供服务。 

SupiRanges在AUSF、CHF、PCF、UDM、UDR、OCS这6个NF特有信息中携带。如果以上6个NF的发现响应不带NF特有信息，或者特有信息中不携带supiRanges，表示该NF可以为所有SUPI服务。 




功能说明 


SUPI范围组编号配置用于配置一个SUPI范围组，一个SUPI范围组包含了若干个SUPI范围参数。 

当启用本地NRF功能时，如果NF（AUSF、CHF、PCF、UDM、UDR、OCS）需要限定可以服务的SUPI，则需要配置SUPI范围组编号。配置后，在本地NRF配置的NF扩展信息中关联该SUPI范围组编号。如果本地NRF配置的NF扩展信息中没有关联SUPI范围组配置，则该NF可以为服务网络中的所有SUPI服务。 




子主题： 






#### 新增SUPI范围组编号配置(ADD SBISUPIRANGEARRID) 
#### 新增SUPI范围组编号配置(ADD SBISUPIRANGEARRID) 


功能说明 

该命令用于新增SUPI范围组编号。当启用本地NRF功能，且需要限定AUSF、CHF、PCF、UDM、UDR、OCS这6个NF可以服务的SUPI范围时，使用该命令。命令执行成功后，可以在上述NF配置信息中关联该组编号，从而达到限制SUPI服务范围的目的。 


注意事项 

仅当启用本地NRF功能，且需要限定AUSF、CHF、PCF、UDM、UDR、OCS这6个NF可以服务的SUPI范围时，才需配置；否则不配置。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SUPI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组的编号，该编号全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组的编号，该编号全局唯一。该参数无特殊配置原则。




命令举例 


`
新增SUPI范围组编号配置：SUPI范围组编号为1。 
ADD SBISUPIRANGEARRID:ARRAYID=1
` 


#### 删除SUPI范围组编号配置(DEL SBISUPIRANGEARRID) 
#### 删除SUPI范围组编号配置(DEL SBISUPIRANGEARRID) 


功能说明 

该命令用于删除SUPI范围组编号。当该SUPI组编号不再被任何NF关联时，执行该命令。 


注意事项 

删除前需要把归属于该SUPI组编号的所有SUPI组参数配置删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SUPI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组的编号，该编号全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组的编号，该编号全局唯一。该参数无特殊配置原则。




命令举例 


`
删除SUPI范围组编号配置：SUPI范围组编号为1。
DEL SBISUPIRANGEARRID:ARRAYID=1
` 


#### 查询SUPI范围组编号配置(SHOW SBISUPIRANGEARRID) 
#### 查询SUPI范围组编号配置(SHOW SBISUPIRANGEARRID) 


功能说明 

该命令用于查询SUPI范围组的编号。查询时，可以指定SUPI组编号查询对应的SUPI组编号信息；如果不指定SUPI组编号，则查询所有已配置的SUPI组编号信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组的编号，该编号全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组的编号，该编号全局唯一。该参数无特殊配置原则。




命令举例 


`
查询SUPI范围组编号配置：SUPI范围组编号为1。
SHOW SBISUPIRANGEARRID:ARRAYID=1

(No.2) : SHOW SBISUPIRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       SUPI范围组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-11-16 16:57:40 耗时: 1.559 秒

` 


### SUPI范围组参数配置 
### SUPI范围组参数配置 


背景知识 


SUPI（Subscription Permanent Identifier， 用户永久标识符）必须包含IMSI（International Mobile Subscriber Identity，国际移动用户标识）、NSI（network specific identifier，网络特定标识符）、GCI（Global Cable Identifier，全局电缆标识符）或GLI（Global Line Identifier，全局线路标识符）之一，目前系统支持的是IMSI。 

服务发现响应消息中的SUPI范围组（SupiRanges）是数组格式，每个元素（SUPI范围）用一个start和一个end表示，表明该NF为这些范围内的SUPI提供服务。即NF可以为SUPI范围组（SupiRanges）内的SUPI提供服务。 

SupiRanges在AUSF、CHF、PCF、UDM、UDR、OCS这6个NF特有信息中携带。如果以上6个NF的发现响应不带NF特有信息，或者特有信息中不携带supiRanges，表示该NF可以为所有SUPI服务。 




功能说明 


SUPI范围组参数配置用于配置SUPI范围组的具体信息，包括SUPI范围的开始和结束，并通过SUPI范围组编号标识该SUPI范围参数归属于哪个SUPI范围组。 

当NF（AUSF、CHF、PCF、UDM、UDR、OCS）需要限定服务的具体SUPI时，需要配置SUPI范围组参数。配置完成后，在NF配置中引用该SUPI范围组参数归属的SUPI范围组编号。 

没有配置SUPI范围组参数的SUPI范围组编号将不能被NF配置引用。如果NF（AUSF、CHF、PCF、UDM、UDR、OCS）引用了该SUPI范围组编号，在组装NFProfile时会失败。 




子主题： 






#### 新增SUPI范围组参数配置(ADD SBISUPIRANGEARRPARAM) 
#### 新增SUPI范围组参数配置(ADD SBISUPIRANGEARRPARAM) 


功能说明 

该命令用于新增SUPI范围组参数配置。当某个SUPI范围组需要增加NF（AUSF、CHF、PCF、UDM、UDR、OCS）可以服务的SUPI范围时，执行该命令。命令执行成功后，关联该SUPI范围组的NF（AUSF、CHF、PCF、UDM、UDR、OCS）仅能为组范围内的SUPI提供服务。 


注意事项 

新增归属的SUPI范围组编号参数，需要保证该组参数归属的SUPI范围组编号已经存在，该组编号通过[SHOW SBISUPIRANGEARRID]命令查询。

SUPI范围组参数配置中的START、END从高位开始，不足32位时，START在低位补0，END在低位补9，补齐后再比较START是否小于END。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 必选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 必选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
新增SUPI范围组参数配置：配置索引为1，SUPI范围组编号为1，SUPI范围开始为460012340000，结束为460012345000。 
ADD SBISUPIRANGEARRPARAM:INDEX=1,ARRAYID=1,START="460012340000",END="460012345000"
` 


#### 修改SUPI范围组参数配置(SET SBISUPIRANGEARRPARAM) 
#### 修改SUPI范围组参数配置(SET SBISUPIRANGEARRPARAM) 


功能说明 

该命令用于修改SUPI范围组参数配置。当NF（AUSF、CHF、PCF、UDM、UDR、OCS）服务的SUPI范围信息发生变更时，执行该命令修改NF关联的SUPI范围组内的SUPI范围。命令执行成功后，关联该SUPI范围组的NF（AUSF、CHF、PCF、UDM、UDR、OCS）为修改后的组范围内的SUPI提供服务。 


注意事项 

修改SUPI范围组参数配置会导致NF（AUSF、CHF、PCF、UDM、UDR、OCS）服务的SUPI范围发生变化，需慎重。 

SUPI范围组参数配置中的START、END从高位开始，不足32位时，START在低位补0，END在低位补9，补齐后再比较START是否小于END。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
修改SUPI范围组参数配置：配置索引为1，SUPI范围组编号为1，SUPI范围开始为460012340000，结束为460012346000。 
SET SBISUPIRANGEARRPARAM:INDEX=1,ARRAYID=1,START="460012340000",END="460012346000"
` 


#### 删除SUPI范围组参数配置(DEL SBISUPIRANGEARRPARAM) 
#### 删除SUPI范围组参数配置(DEL SBISUPIRANGEARRPARAM) 


功能说明 

该命令用于删除SUPI范围组参数配置。当NF（AUSF、CHF、PCF、UDM、UDR、OCS）不再对某个SUPI范围提供服务时，使用该命令删除NF所关联的SUPI范围组中该SUPI范围信息。命令执行成功后，NF不再对该SUPI范围提供服务。 


注意事项 

删除SUPI范围组参数配置，需要先查询对应的配置索引，再使用配置索引进行删除。配置索引通过[SHOW SBISUPIRANGEARRPARAM]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
删除SUPI范围组参数配置：配置索引为1。
DEL SBISUPIRANGEARRPARAM:INDEX=1
` 


#### 查询SUPI范围组参数配置(SHOW SBISUPIRANGEARRPARAM) 
#### 查询SUPI范围组参数配置(SHOW SBISUPIRANGEARRPARAM) 


功能说明 

该命令用于查询SUPI范围组参数配置，包括范围组编号、及开始结束范围。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如IMSI范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
查询SUPI范围组参数配置：配置索引为1。
SHOW SBISUPIRANGEARRPARAM:INDEX=1

(No.5) : SHOW SBISUPIRANGEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 SUPI范围组编号 开始         结束          
----------------------------------------------------------------------
复制 修改 删除 1        1              460012340000 460012346000      
----------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-16 17:19:25 耗时: 1.507 秒


` 


## GPSI范围组配置 
## GPSI范围组配置 


背景知识 


GPSI（Generic Public Subscription Identifier，一般公共用户标识）应该包含一个MSISDN或者扩展标识符，简单地说就是手机号。 

服务发现响应消息中的GPSI范围组（GpsiRanges）是数组格式，每个元素（GPSI范围）用一个start和一个end表示，表明该NF为这些范围内的GPSI提供服务。即NF可以为GUPI范围组（GpsiRanges）内的GUPI提供服务。 

GpsiRanges在CHF、PCF、UDM、UDR、OCS这5个NF特有信息中携带。如果以上5个NF的发现响应不带NF特有信息，或者特有信息中不携带gpsiRanges，表示该NF可以为所有GPSI服务。 




功能说明 


GPSI范围组数据配置包括GPSI范围组编号配置和GPSI范围组参数配置，一个GPSI范围组编号可以被若干个GPSI范围组参数引用。 

当启用本地NRF功能时，GPSI范围组配置应用于CHF、PCF、 UDM 、UDR、OCS这5个NF信息配置中，用于限定这5个NF可以服务的GPSI范围。如果上述NF中GPSI范围组没有配置，则该NF可以为服务网络中的所有GPSI服务。 




子主题： 






### GPSI范围组编号配置 
### GPSI范围组编号配置 


背景知识 


GPSI（Generic Public Subscription Identifier，一般公共用户标识）应该包含一个MSISDN或者扩展标识符，简单地说就是手机号。 

服务发现响应消息中的GPSI范围组（GpsiRanges）是数组格式，每个元素（GPSI范围）用一个start和一个end表示，表明该NF为这些范围内的GPSI提供服务。即NF可以为GUPI范围组（GpsiRanges）内的GUPI提供服务。 

GpsiRanges在CHF、PCF、UDM、UDR、OCS这5个NF特有信息中携带。如果以上5个NF的发现响应不带NF特有信息，或者特有信息中不携带gpsiRanges，表示该NF可以为所有GPSI服务。 




功能说明 


GPSI范围组编号配置用于配置一个GPSI范围组，一个GPSI范围组包含了若干个GPSI范围参数。 

当启用本地NRF功能时，如果NF（CHF、PCF、UDM、UDR、OCS）需要限定可以服务的GPSI，则需要配置GPSI范围组编号。配置后，在本地NRF配置的NF扩展信息中关联该GPSI范围组编号。如果本地NRF配置的NF扩展信息中没有关联GPSI范围组配置，则该NF可以为服务网络中的所有GPSI服务。 




子主题： 






#### 新增GPSI范围组编号配置(ADD SBIGPSIRANGEARRID) 
#### 新增GPSI范围组编号配置(ADD SBIGPSIRANGEARRID) 


功能说明 

该命令用于新增GPSI范围组编号。当启用本地NRF功能，且需要限定CHF、PCF、UDM、UDR、OCS这5个NF可以服务的GPSI范围时，使用该命令。执行成功后，可以在上述NF配置信息中关联该组编号，从而达到限制GSPI服务范围的目的。 


注意事项 

仅当启用本地NRF功能，且需要限定CHF、PCF、UDM、UDR、OCS这5个NF可以服务的GSPI范围时，才需配置；否则不配置。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GPSI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，该编号全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，该编号全局唯一。该参数无特殊配置原则。




命令举例 


`
新增GPSI范围组编号配置：GPSI范围组编号为1。 
ADD SBIGPSIRANGEARRID:ARRAYID=1
` 


#### 删除GPSI范围组编号配置(DEL SBIGPSIRANGEARRID) 
#### 删除GPSI范围组编号配置(DEL SBIGPSIRANGEARRID) 


功能说明 

该命令用于删除GPSI范围组编号。当该GPSI组编号不再被任何NF关联时，执行该命令。 


注意事项 

删除前需要把归属于该GPSI组编号的所有GPSI组参数配置删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GPSI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，该编号全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，该编号全局唯一。该参数无特殊配置原则。




命令举例 


`
删除GPSI范围组编号配置：GPSI范围组编号为1。
DEL SBIGPSIRANGEARRID:ARRAYID=1
` 


#### 查询GPSI范围组编号配置(SHOW SBIGPSIRANGEARRID) 
#### 查询GPSI范围组编号配置(SHOW SBIGPSIRANGEARRID) 


功能说明 

该命令用于查询GPSI范围组的编号。查询时，可以指定GPSI组编号查询对应的GPSI组编号信息；如果不指定GPSI组编号，则查询所有已配置的GPSI组编号信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，该编号全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，该编号全局唯一。该参数无特殊配置原则。




命令举例 


`
查询GPSI范围组编号配置：GPSI范围组编号为1。
SHOW SBIGPSIRANGEARRID:ARRAYID=1

(No.3) : SHOW SBIGPSIRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       GPSI范围组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-11-17 15:59:46 耗时: 0.529 秒

` 


### GPSI范围组参数配置 
### GPSI范围组参数配置 


背景知识 


GPSI（Generic Public Subscription Identifier，一般公共用户标识）应该包含一个MSISDN或者扩展标识符，简单地说就是手机号。 

服务发现响应消息中的GPSI范围组（GpsiRanges）是数组格式，每个元素（GPSI范围）用一个start和一个end表示，表明该NF为这些范围内的GPSI提供服务。即NF可以为GUPI范围组（GpsiRanges）内的GUPI提供服务。 

GpsiRanges在CHF、PCF、UDM、UDR、OCS这5个NF特有信息中携带。如果以上5个NF的发现响应不带NF特有信息，或者特有信息中不携带gpsiRanges，表示该NF可以为所有GPSI服务。 




功能说明 


GPSI范围组参数配置用于配置GPSI范围组的具体信息，包括GPSI范围的开始和结束，并通过GPSI范围组编号标识该GPSI范围参数归属于哪个GPSI范围组。 

当NF（CHF、PCF、UDM、UDR、OCS）需要限定服务的具体GPSI时，需要配置GPSI范围组参数。配置完成后，在NF配置中引用该GPSI范围组参数归属的GPSI范围组编号。 

没有配置GPSI范围组参数的GPSI范围组编号将不能被NF配置引用。如果NF（CHF、PCF、UDM、UDR、OCS）引用了该GPSI范围组编号，在组装NFProfile时会失败。 




子主题： 






#### 新增GPSI范围组参数配置(ADD SBIGPSIRANGEARRPARAM) 
#### 新增GPSI范围组参数配置(ADD SBIGPSIRANGEARRPARAM) 


功能说明 

该命令用于新增GPSI范围组参数配置。当某个GPSI范围组需要增加NF（CHF、PCF、UDM、UDR、OCS）可以服务的GPSI范围时，执行该命令。命令执行成功后，关联该GPSI范围组的NF（CHF、PCF、UDM、UDR、OCS）仅能为组范围内的GPSI提供服务。 


注意事项 

新增归属的GPSI范围组编号参数，需要保证该组参数归属的GPSI范围组编号已经存在，该组编号通过[SHOW SBIGPSIRANGEARRID]命令查询。

GPSI范围组参数配置中的START、END从高位开始，不足32位时，START在低位补0，END在低位补9，补齐后再比较START是否小于END。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 必选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 必选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
新增GPSI范围组参数配置：配置索引为1，GPSI范围组编号为1，GPSI开始为8613900000000，结束为8613910000000。 
ADD SBIGPSIRANGEARRPARAM:INDEX=1,ARRAYID=1,START="8613900000000",END="8613910000000"
` 


#### 修改GPSI范围组参数配置(SET SBIGPSIRANGEARRPARAM) 
#### 修改GPSI范围组参数配置(SET SBIGPSIRANGEARRPARAM) 


功能说明 

该命令用于修改GPSI范围组参数配置。当NF（CHF、PCF、UDM、UDR、OCS）服务的GPSI范围信息发生变更时，执行该命令修改NF关联的GPSI范围组内的GPSI范围。命令执行成功后，关联该GPSI范围组的NF（CHF、PCF、UDM、UDR、OCS）为修改后的组范围内的GPSI提供服务。 


注意事项 

修改SUPI范围组参数配置会导致NF（CHF、PCF、UDM、UDR、OCS）服务的GPSI范围发生变化，需慎重。 

GPSI范围组参数配置中的START、END从高位开始，不足32位时，START在低位补0，END在低位补9，补齐后再比较START是否小于END。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
修改GPSI范围组参数配置：配置索引为1，GPSI开始为8613900000000，结束为8613920000000。 
SET SBIGPSIRANGEARRPARAM:INDEX=1,START="8613900000000",END="8613920000000"
` 


#### 删除GPSI范围组参数配置(DEL SBIGPSIRANGEARRPARAM) 
#### 删除GPSI范围组参数配置(DEL SBIGPSIRANGEARRPARAM) 


功能说明 

本命令用于删除GPSI范围组参数配置。当NF（CHF、PCF、UDM、UDR、OCS）不再对某个GPSI范围提供服务时，使用该命令删除NF所关联的GPSI范围组中该GPSI范围信息。命令执行成功后，NF不再对该GPSI范围提供服务。 


注意事项 

删除GPSI范围组参数配置，需要先查询对应的配置索引，再使用配置索引进行删除。配置索引通过[SHOW SBIGPSIRANGEARRPARAM]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
删除GPSI范围组参数配置：配置索引为1。
DEL SBIGPSIRANGEARRPARAM:INDEX=1
` 


#### 查询GPSI范围组参数配置(SHOW SBIGPSIRANGEARRPARAM) 
#### 查询GPSI范围组参数配置(SHOW SBIGPSIRANGEARRPARAM) 


功能说明 

该命令用于查询GPSI范围组参数配置，包括范围组编号、及开始结束范围。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-4294967295|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GPSI范围组编号，表示该GPSI范围组参数配置归属于哪个GPSI范围组。该编号通过SHOW SBIGPSIRANGEARRID命令查询。该参数无特殊配置原则。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围开始的第一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-31|该参数用于设置GPSI范围结束的最后一个值，当GPSI的范围可以表示为数字范围（例如MSISDN范围）时使用。该字符串应仅由数字组成。该参数无特殊配置原则。




命令举例 


`
查询GPSI范围组参数配置：GPSI范围组编号为1。
SHOW SBIGPSIRANGEARRPARAM:ARRAYID=1

(No.8) : SHOW SBIGPSIRANGEARRPARAM:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 GPSI范围组编号 开始          结束           
------------------------------------------------------------------------
复制 修改 删除 1        1              8613900000000 8613920000000      
------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-17 16:43:51 耗时: 0.623 秒

` 


## 数据集组配置 
## 数据集组配置 


背景知识 


数据集是一种类型的数据集合，数据集的类型有订阅数据、策略数据、结构化开放数据以及应用程序数据。 

数据集组是一个或者多个数据集的集合。在服务发现响应中，数据集组是数组格式，每个元素表示一种数据集类型。 

服务发现响应通过UDR特有信息中携带supportedDataSets。如果服务发现响应不带UDR特有信息，或者特有信息中不携带supportedDataSets，表示该UDR支持所有类型的数据集。 




功能说明 


数据集范围组数据配置包括数据集组编号配置和数据集组参数配置，一个数据集组编号可以被若干个数据集组参数引用。 

当启用本地NRF功能时，数据集组配置应用于UDR信息配置中，用于限定UDR可以支持的数据集。如果UDR数据集组没有配置，则该UDR可以支持所有的数据集。 




子主题： 






### 数据集组编号配置 
### 数据集组编号配置 


背景知识 


数据集是一种类型的数据集合，数据集的类型有订阅数据、策略数据、结构化开放数据以及应用程序数据。 

数据集组是一个或者多个数据集的集合。在服务发现响应中，数据集组是数组格式，每个元素表示一种数据集类型。 

服务发现响应通过UDR特有信息中携带supportedDataSets。如果服务发现响应不带UDR特有信息，或者特有信息中不携带supportedDataSets，表示该UDR支持所有类型的数据集。 




功能说明 


数据集组编号配置用于配置一个数据集组，一个数据集组包含了若干个数据集参数。 

当启用本地NRF功能时，如果UDR需要限定支持的数据集类型，则需要配置数据集组编号。配置后，在本地NRF配置的NF扩展信息中关联该数据集组编号。 

如果本地NRF配置的NF扩展信息中没有关联数据集组配置，则该NF可以支持所有数据集。 




子主题： 






#### 新增数据集组编号配置(ADD SBIDATASETARRID) 
#### 新增数据集组编号配置(ADD SBIDATASETARRID) 


功能说明 

本命令用于新增数据集组编号。当UDR需要新增限定可以服务的数据集组时，使用该命令。执行成功后，可以在上述UDR信息配置中关联该组编号。 


注意事项 

系统支持的该配置项最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|数据集组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号。该编号全局唯一。




命令举例 


`
新增数据集组编号配置：数据集组编号为1。 
ADD SBIDATASETARRID:ARRAYID=1
` 


#### 删除数据集组编号配置(DEL SBIDATASETARRID) 
#### 删除数据集组编号配置(DEL SBIDATASETARRID) 


功能说明 

本命令用于删除数据集组编号。当该数据集组编号不再被任何UDR关联时，可以使用该命令删除数据集组编号配置。 


注意事项 

删除前需要把归属于该数据集组编号的所有数据集组参数配置删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|数据集组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号。该编号全局唯一。




命令举例 


`
删除数据集组编号配置：数据集组编号为1。
DEL SBIDATASETARRID:ARRAYID=1
` 


#### 查询数据集组编号配置(SHOW SBIDATASETARRID) 
#### 查询数据集组编号配置(SHOW SBIDATASETARRID) 


功能说明 

本命令用于查询数据集组编号。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号。该编号全局唯一。




命令举例 


`
查询数据集组编号配置：数据集组编号为1。
SHOW SBIDATASETARRID:ARRAYID=1

(No.11) : SHOW SBIDATASETARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       数据集组编号 
----------------------------
复制 删除      1            
----------------------------
记录数：1
执行成功 开始时间:2020-11-17 16:47:00 耗时: 0.631 秒

` 


### 数据集组参数配置 
### 数据集组参数配置 


背景知识 


数据集是一种类型的数据集合，数据集的类型有订阅数据、策略数据、结构化开放数据以及应用程序数据。 

数据集组是一个或者多个数据集的集合。在服务发现响应中，数据集组是数组格式，每个元素表示一种数据集类型。 

服务发现响应通过UDR特有信息中携带supportedDataSets。如果服务发现响应不带UDR特有信息，或者特有信息中不携带supportedDataSets，表示该UDR支持所有类型的数据集。 




功能说明 


数据集组参数配置用于配置数据集组的具体信息，包括数据集类型，并通过数据集组编号标识该数据集参数归属于哪个数据集组。 

当UDR需要限定支持的数据集时，需要配置数据集组参数。配置完成后，在NF配置中引用该数据集组参数归属的数据集组编号。 

没有配置数据集组参数的数据集组编号将不能被NF配置引用。如果NF引用了该数据集组编号，在组装NFProfile时会失败。 




子主题： 






#### 新增数据集组参数配置(ADD SBIDATASETARRPARAM) 
#### 新增数据集组参数配置(ADD SBIDATASETARRPARAM) 


功能说明 

本命令用于新增数据集组参数配置。当某个数据集组中需要增加UDR可以支持的数据集时，使用该命令在数据集组内增加数据集。命令执行成功后，关联该数据集组的UDR将支持新增的数据集。 


注意事项 

新增归属的数据集组编号参数，需要保证该组参数归属的数据集组编号已经存在，该组编号通过[SHOW SBIDATASETARRID]命令查询。

系统支持的该配置项最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




命令举例 


`
新增数据集组参数配置：配置索引为1，数据集组编号为1，数据集标识为POLICY。 
ADD SBIDATASETARRPARAM:INDEX=1,ARRAYID=1,DATASETID=POLICY
` 


#### 修改数据集组参数配置(SET SBIDATASETARRPARAM) 
#### 修改数据集组参数配置(SET SBIDATASETARRPARAM) 


功能说明 

本命令用于修改数据集组参数配置。当UDR支持的数据集发生变更时，使用该命令修改UDR关联的数据集组内的数据集。命令执行成功后，关联该数据集组的UDR支持的数据集也会发生变化。 


注意事项 

修改归属的数据集组编号参数，需要保证该组参数归属的数据集组编号已经存在，该组编号通过[SHOW SBIDATASETARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




命令举例 


`
修改数据集组参数配置：配置索引为1，数据集组编号为1，数据集标识为POLICY。 
SET SBIDATASETARRPARAM:INDEX=1,ARRAYID=1,DATASETID=POLICY
` 


#### 删除数据集组参数配置(DEL SBIDATASETARRPARAM) 
#### 删除数据集组参数配置(DEL SBIDATASETARRPARAM) 


功能说明 

本命令用于删除数据集组参数配置。当UDR不再对某个数据集提供服务时，使用该命令删除UDR所关联的数据集组中该数据集信息。命令执行成功后，UDR不再对该数据集提供服务。 


注意事项 

删除数据集组参数配置，需要先查询对应的配置索引，再使用配置索引进行删除。配置索引通过[SHOW SBIDATASETARRPARAM]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




命令举例 


`
删除数据集组参数配置：配置索引为1。
DEL SBIDATASETARRPARAM:INDEX=1
` 


#### 查询数据集组参数配置(SHOW SBIDATASETARRPARAM) 
#### 查询数据集组参数配置(SHOW SBIDATASETARRPARAM) 


功能说明 

本命令用于查询数据集组参数配置，包括：数据集组编号和数据集标识。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。
DATASETID|数据集标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置数据集标识，表示UDR实例支持数据集类型。各参数选项的含义是：SUBSCRIPTION：订阅数据。POLICY：策略数据。EXPOSURE：对外开放的结构化数据。APPLICATION：应用数据。




命令举例 


`
查询数据集组参数配置：配置索引为1。
SHOW SBIDATASETARRPARAM:INDEX=1

(No.13) : SHOW SBIDATASETARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 数据集组编号 数据集标识 
------------------------------------------------
复制 修改 删除 1        1            POLICY     
------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-17 16:53:04 耗时: 0.644 秒

` 


## 路由指示组配置 
## 路由指示组配置 


背景知识 


路由指示组表示一组路由指示器，路由指示器允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。 

本地NRF功能中，该配置主要用于”AUSF信息配置“和”UDM信息配置“中。用于限定AUSF或UDM可以服务的路由指示器列表。如果AUSF或UDM中没有配置路由指示组，则说明其可以服务于任何路由指示器。在本地NRF功能开启时，路由指示配置会呈现在AUSF和UDM配置的routingIndicators数组中。 




功能说明 


路由指示组配置对应AUSF和UDM配置的routingIndicators数组。如果不配置，则相关NF配置缺少routingIndicators数组，表示该NF可以服务于任何路由指示器。当启用本地NRF功能时，需要配置该组命令。 

路由指示组配置包括路由指示组编号配置和路由指示组参数配置，一个路由指示组下面可以包含若干个路由指示组参数。 




子主题： 






### 路由指示组编号配置 
### 路由指示组编号配置 


背景知识 


路由指示组表示一组路由指示器，路由指示器允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。 

本地NRF功能中，该配置主要用于”AUSF信息配置“和”UDM信息配置“中。用于限定AUSF或UDM可以服务的路由指示器列表。如果AUSF或UDM中没有配置路由指示组，则说明其可以服务于任何路由指示器。在本地NRF功能开启时，路由指示配置会呈现在AUSF和UDM配置的routingIndicators数组中。 




功能说明 


路由指示组编号配置用于配置一个路由指示组，一个路由指示组包含了若干个路由指示组参数。当启用本地NRF功能时，需要配置该组命令。 

当启用本地NRF功能时，如果需要提供AUSF或UDM实例可以服务的特定路由指示器列表，则需要配置路由指示组编号。配置后，最终呈现在AUSF或UDM配置的routingIndicators数组中。如果不配置，则相关NF配置中缺少routingIndicators数组，表示该NF可以服务于任何路由指示器。 




子主题： 






#### 新增路由指示组编号配置(ADD SBIROUTINDARRID) 
#### 新增路由指示组编号配置(ADD SBIROUTINDARRID) 


功能说明 

该命令用于新增路由指示组编号配置。当NF（AUSF、UDM）需要新增限定可以服务的路由指示器列表时，使用该命令。 

命令执行成功后，路由指示组编号可以被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。 


注意事项 

必须先配置该路由指示组编号，才能在“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”中引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|路由指示组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号，该编号是路由指示组编号配置的唯一标识。被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询。“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询。“UDM信息配置”通过SHOW SBIUDMINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号，该编号是路由指示组编号配置的唯一标识。被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询。“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询。“UDM信息配置”通过SHOW SBIUDMINFO命令查询。该参数无特殊配置原则。




命令举例 


`
新增路由指示组编号配置：路由指示组编号为1。
ADD SBIROUTINDARRID:ARRAYID=1;
` 


#### 删除路由指示组编号配置(DEL SBIROUTINDARRID) 
#### 删除路由指示组编号配置(DEL SBIROUTINDARRID) 


功能说明 

该命令用于删除路由指示组编号配置。当该路由指示组编号不再被任何NF引用时，使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该路由指示配置，需要先删除引用该配置的“路由指示组参数配置”，并在“AUSF信息配置”及“UDM信息配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询，通过DEL SBIROUTINDARRPARAM命令进行删除。 

 
“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询，通过SET SBIAUSFINFO命令进行设置。 

 
“UDM信息配置”通过SHOW SBIUDMINFO命令查询，通过SET SBIUDMINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|路由指示组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号，该编号是路由指示组编号配置的唯一标识。被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询。“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询。“UDM信息配置”通过SHOW SBIUDMINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号，该编号是路由指示组编号配置的唯一标识。被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询。“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询。“UDM信息配置”通过SHOW SBIUDMINFO命令查询。该参数无特殊配置原则。




命令举例 


`
删除路由指示组编号配置：路由指示组编号为1。
DEL SBIROUTINDARRID:ARRAYID=1;
` 


#### 查询路由指示组编号配置(SHOW SBIROUTINDARRID) 
#### 查询路由指示组编号配置(SHOW SBIROUTINDARRID) 


功能说明 

该命令用于查询路由指示组编号配置。当需要查询路由指示组编号配置时，使用该命令。 

指定路由指示组编号，可以查询指定的路由指示组信息；不指定路由指示组编号，可以查询已经配置的所有路由指示组信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号，该编号是路由指示组编号配置的唯一标识。被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询。“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询。“UDM信息配置”通过SHOW SBIUDMINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号，该编号是路由指示组编号配置的唯一标识。被“路由指示组参数配置”、“AUSF信息配置”及“UDM信息配置”引用。“路由指示组参数配置”通过SHOW SBIROUTINDARRPARAM命令查询。“AUSF信息配置”通过SHOW SBIAUSFINFO命令查询。“UDM信息配置”通过SHOW SBIUDMINFO命令查询。该参数无特殊配置原则。




命令举例 


`
查询路由指示组编号配置：路由指示组编号为1。
SHOW SBIROUTINDARRID:ARRAYID=1

(No.1) : SHOW SBIROUTINDARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       路由指示组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:26:49 耗时: 0.652 秒

` 


### 路由指示组参数配置 
### 路由指示组参数配置 


背景知识 


路由指示组表示一组路由指示器，路由指示器允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。 

本地NRF功能中，该配置主要用于”AUSF信息配置“和”UDM信息配置“中。用于限定AUSF或UDM可以服务的路由指示器列表。如果AUSF或UDM中没有配置路由指示组，则说明其可以服务于任何路由指示器。在本地NRF功能开启时，路由指示配置会呈现在AUSF和UDM配置的routingIndicators数组中。 




功能说明 


路由指示组参数配置用于配置一个路由指示归属于哪个路由指示组。当启用本地NRF功能时，需要配置该组命令。 

当需要提供NF实例可以服务的特定路由指示器列表，则需要配置路由指示组参数。配置完成后，在NF中引用该路由指示组参数归属的路由指示组编号。如果没有配置路由指示组参数的路由指示组，被“AUSF信息配置”或“UDM信息配置”引用后，会导致组装NFProfile失败。 




子主题： 






#### 新增路由指示组参数配置(ADD SBIROUTINDARRPARAM) 
#### 新增路由指示组参数配置(ADD SBIROUTINDARRPARAM) 


功能说明 

该命令用于新增路由指示组参数配置。当NF（AUSF、UDM）已配置可以服务的路由指示组编号，需要新增归属于该路由指示组编号的参数时，使用该命令。命令执行成功后，NF（AUSF、UDM）新增了可以服务的该组路由指示信息。 


注意事项 

如果要新增该路由指示组参数配置，需要先新增“路由指示组编号配置”。如果没有配置路由指示组参数的路由指示组，被“AUSF信息配置”或“UDM信息配置”引用后，会导致组装NFProfile失败。 

“路由指示组编号配置”通过[ADD SBIROUTINDARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 必选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 任选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




命令举例 


`
新增路由指示组参数配置：配置索引为1，路由指示组编号为1，路由指示器为"1234"。
ADD SBIROUTINDARRPARAM:INDEX=1,ARRAYID=1,ROUTINGINDICATOR="1234";
` 


#### 修改路由指示组参数配置(SET SBIROUTINDARRPARAM) 
#### 修改路由指示组参数配置(SET SBIROUTINDARRPARAM) 


功能说明 

该命令用于修改路由指示组参数配置。当NF（AUSF、UDM）已配置可以服务的路由指示组编号，需要修改归属于该路由指示组编号的参数时，使用该命令。命令执行成功后，NF（AUSF、UDM）修改了可以服务的该组路由指示信息。 


注意事项 

如果要修改如下配置项，则需要保证如下配置都已经存在： 

“路由指示组编号配置”通过[SHOW SBIROUTINDARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 任选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 任选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




命令举例 


`
修改路由指示组参数配置：配置索引为1，路由指示组编号为1，路由指示器为"1234"。
SET SBIROUTINDARRPARAM:INDEX=1,ARRAYID=1,ROUTINGINDICATOR="1234";
` 


#### 删除路由指示组参数配置(DEL SBIROUTINDARRPARAM) 
#### 删除路由指示组参数配置(DEL SBIROUTINDARRPARAM) 


功能说明 

该命令用于删除路由指示组参数配置。当NF（AUSF、UDM）已配置可以服务的路由指示组编号，需要删除归属于该路由指示组编号的参数时，使用该命令。命令执行成功后，NF（AUSF、UDM）删除了可以服务的该组路由指示信息。 


注意事项 

如果归属于某个路由指示组编号的所有路由指示组参数配置都已经删除，建议删除该路由指示组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 任选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




命令举例 


`
删除路由指示组参数配置：配置索引为1。
DEL SBIROUTINDARRPARAM:INDEX=1;
` 


#### 查询路由指示组参数配置(SHOW SBIROUTINDARRPARAM) 
#### 查询路由指示组参数配置(SHOW SBIROUTINDARRPARAM) 


功能说明 

该命令用于查询路由指示组参数配置。当需要查询路由指示组参数时，使用该命令。 

指定路由指示组编号，可以查询指定的路由指示组的参数信息；不指定路由指示组编号，可以查询所有已经配置的路由指示组的参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 任选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是路由指示组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置路由指示组编号。路由指示组编号通过SHOW SBIROUTINDARRID命令查询。
ROUTINGINDICATOR|路由指示器|参数可选性: 任选参数类型: 字符串参数范围: 1-4|该参数用于设置路由指示器，表示允许使用SUCI（Subscription Concealed Identifier，用户匿名标识）将网络信令路由到能够为用户服务的AUSF和UDM实例。如果目标NF类型是“ AUSF”或“ UDM”，则可以包括在内。该参数无特殊配置原则。




命令举例 


`
查询路由指示组参数配置：配置索引为1。
SHOW SBIROUTINDARRPARAM:INDEX=1

(No.1) : SHOW SBIROUTINDARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 路由指示组编号 路由指示器 
--------------------------------------------------
复制 修改 删除 1        1              1234       
--------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:29:07 耗时: 0.616 秒

` 


## GUAMI组配置 
## GUAMI组配置 


背景知识 


GUAMI（Globally Unique AMF Identifier，全球唯一AMF标识）用于标识AMF，由MCC、MNC及AMF ID组成。 

格式为：&ltGUAMI> = &ltMCC>&ltMNC>&ltAMFID>。 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
AMFID由6个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的“PLMN ID编号”中配置，该编号可以通过[SHOW SBIPLMNID]命令查询。

本地NRF功能中，该配置主要用于”AMF信息配置“中。服务使用者（本端）会携带用户当前的GUAMI。 
当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的GUAMI与NFProfile的GUAMI列表进行比较，找到匹配的GUAMI时，就认为发现AMF成功。 
当作为服务的AMF失败或计划迁移时，同样与NFProfile的用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表进行比较，找到匹配的GUAMI时，则认为发现AMF成功。 
如果没有配置GUAMI组，则AMF无法设置相应的GUAMI列表、失败备用GUAMI列表和迁移备用GUAMI列表，既不能为服务使用者提供符合条件的AMF，且当作为服务的AMF失败或计划迁移时，将没有可以匹配GUAMI的AMF可用。 
在本地NRF功能开启时，GUAMI配置会呈现在AMF配置的guamiList、backupInfoAmfFailure和backupInfoAmfRemoval数组中。 




功能说明 


GUAMI组配置应用于“AMF信息配置”中。如果不配置，则AMF配置将缺少guamiList、backupInfoAmfFailure和backupInfoAmfRemoval数组，表示无法为服务使用者提供可发现AMF的GUAMI列表、用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表。当启用本地NRF功能时，需要配置该组命令。 

GUAMI组配置包括GUAMI组编号配置和GUAMI组参数配置，一个GUAMI组下面可以包含若干个GUAMI组参数。 




子主题： 






### GUAMI组编号配置 
### GUAMI组编号配置 


背景知识 


GUAMI（Globally Unique AMF Identifier，全球唯一AMF标识）用于标识AMF，由MCC、MNC及AMF ID组成。 

格式为：&ltGUAMI> = &ltMCC>&ltMNC>&ltAMFID>。 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
AMFID由6个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的“PLMN ID编号”中配置，该编号可以通过[SHOW SBIPLMNID]命令查询。

本地NRF功能中，该配置主要用于”AMF信息配置“中。服务使用者（本端）会携带用户当前的GUAMI。 
当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的GUAMI与NFProfile的GUAMI列表进行比较。找到匹配的GUAMI时，就认为发现AMF成功。 
当作为服务的AMF失败或计划迁移时，同样与NFProfile的用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表进行比较。找到匹配的GUAMI时，则认为发现AMF成功。 
如果没有配置GUAMI组，则AMF无法设置相应的GUAMI列表、失败备用GUAMI列表和迁移备用GUAMI列表，既不能为服务使用者提供符合条件的AMF，且当作为服务的AMF失败或计划迁移时，将没有可以匹配GUAMI的AMF可用。 
在本地NRF功能开启时，GUAMI配置会呈现在AMF配置的guamiList、backupInfoAmfFailure和backupInfoAmfRemoval数组中。 




功能说明 


GUAMI组编号配置用于配置一个GUAMI组，一个GUAMI组包含了若干个GUAMI组参数。当启用本地NRF功能时，需要配置该组命令。 

当启用本地NRF功能时，如果需要提供可发现AMF的GUAMI列表、用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表，则需要配置GUAMI组编号。如果不配置，则AMF配置中缺少guamiList、backupInfoAmfFailure和backupInfoAmfRemoval数组，当需要为服务使用者提供AMF实例时，将无法发现成功；当作为服务的AMF失败或计划迁移时，将没有可以匹配GUAMI的AMF可用。 




子主题： 






#### 新增GUAMI组编号配置(ADD SBIGUAMIARRID) 
#### 新增GUAMI组编号配置(ADD SBIGUAMIARRID) 


功能说明 

该命令用于新增GUAMI组编号配置。当AMF需要新增限定可以支持的GUAMI列表、用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表时，使用该命令。 

命令执行成功后，GUAMI组编号可以被“GUAMI组参数配置”及“AMF信息配置”引用。 


注意事项 

必须先配置该GUAMI组编号，才能在“GUAMI组参数配置”及“AMF信息配置”中引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GUAMI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，该编号是GUAMI组编号配置的唯一标识。被“GUAMI组参数配置”及“AMF信息配置”引用。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。“AMF信息配置”通过SHOW SBIAMFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，该编号是GUAMI组编号配置的唯一标识。被“GUAMI组参数配置”及“AMF信息配置”引用。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。“AMF信息配置”通过SHOW SBIAMFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
新增GUAMI组编号配置：GUAMI组编号为1。
ADD SBIGUAMIARRID:ARRAYID=1;
` 


#### 删除GUAMI组编号配置(DEL SBIGUAMIARRID) 
#### 删除GUAMI组编号配置(DEL SBIGUAMIARRID) 


功能说明 

该命令用于删除GUAMI组编号配置。当该GUAMI组编号不再被任何NF引用时，使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该GUAMI组编号配置，需要先删除引用该配置的“GUAMI组参数配置”，并在“AMF信息配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询，通过DEL SBIGUAMIARRPARAM命令进行删除。 

 
“AMF信息配置”通过SHOW SBIAMFINFO命令查询，通过SET SBIAMFINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GUAMI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，该编号是GUAMI组编号配置的唯一标识。被“GUAMI组参数配置”及“AMF信息配置”引用。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。“AMF信息配置”通过SHOW SBIAMFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，该编号是GUAMI组编号配置的唯一标识。被“GUAMI组参数配置”及“AMF信息配置”引用。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。“AMF信息配置”通过SHOW SBIAMFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
删除GUAMI组编号配置：GUAMI组编号为1。
DEL SBIGUAMIARRID:ARRAYID=1;
` 


#### 查询GUAMI组编号配置(SHOW SBIGUAMIARRID) 
#### 查询GUAMI组编号配置(SHOW SBIGUAMIARRID) 


功能说明 

该命令用于查询GUAMI组编号配置。当需要查询GUAMI组编号配置时，使用该命令。 

指定GUAMI组编号，可以查询指定的GUAMI组信息；不指定GUAMI组编号，可以查询已经配置的所有GUAMI组信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，该编号是GUAMI组编号配置的唯一标识。被“GUAMI组参数配置”及“AMF信息配置”引用。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。“AMF信息配置”通过SHOW SBIAMFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，该编号是GUAMI组编号配置的唯一标识。被“GUAMI组参数配置”及“AMF信息配置”引用。“GUAMI组参数配置”通过SHOW SBIGUAMIARRPARAM命令查询。“AMF信息配置”通过SHOW SBIAMFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
查询GUAMI组编号配置：GUAMI组编号为1。
SHOW SBIGUAMIARRID:ARRAYID=1

(No.1) : SHOW SBIGUAMIARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       GUAMI组编号 
---------------------------
复制 删除      1           
---------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:45:25 耗时: 0.612 秒

` 


### GUAMI组参数配置 
### GUAMI组参数配置 


背景知识 


GUAMI（Globally Unique AMF Identifier，全球唯一AMF标识）用于标识AMF，由MCC、MNC及AMF ID组成。 

格式为：&ltGUAMI> = &ltMCC>&ltMNC>&ltAMFID>。 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
AMFID由6个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的“PLMN ID编号”中配置，该编号可以通过[SHOW SBIPLMNID]命令查询。

本地NRF功能中，该配置主要用于”AMF信息配置“中。服务使用者（本端）会携带用户当前的GUAMI。 
当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的GUAMI与NFProfile的GUAMI列表进行比较。找到匹配的GUAMI时，就认为发现AMF成功。 
当作为服务的AMF失败或计划迁移时，同样与NFProfile的用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表进行比较。找到匹配的GUAMI时，则认为发现AMF成功。 
如果没有配置GUAMI组，则AMF无法设置相应的GUAMI列表、失败备用GUAMI列表和迁移备用GUAMI列表，既不能为服务使用者提供符合条件的AMF，且当作为服务的AMF失败或计划迁移时，将没有可以匹配GUAMI的AMF可用。 
在本地NRF功能开启时，GUAMI配置会呈现在AMF配置的guamiList、backupInfoAmfFailure和backupInfoAmfRemoval数组中。 




功能说明 


GUAMI组参数配置用于配置一个GUAMI归属于哪个GUAMI组。当启用本地NRF功能时，需要配置该组命令。 

当需要提供可发现AMF的GUAMI列表、用作AMF失败备用GUAMI列表和AMF迁移备用GUAMI列表时，则需要配置GUAMI组参数。配置完成后，在NF中引用该GUAMI组参数归属的GUAMI组编号。如果没有配置GUAMI组参数的GUAMI组，被“AMF信息配置”引用后，会导致组装NFProfile失败。 




子主题： 






#### 新增GUAMI组参数配置(ADD SBIGUAMIARRPARAM) 
#### 新增GUAMI组参数配置(ADD SBIGUAMIARRPARAM) 


功能说明 

该命令用于新增GUAMI组参数配置。当AMF已配置可以服务的GUAMI组编号，需要新增归属于该GUAMI组编号的参数时，使用该命令。命令执行成功后，AMF新增了可以服务的该组GUAMI信息。 


注意事项 

如果要新增该GUAMI组参数配置，需要先新增“GUAMI组编号配置”。如果没有配置GUAMI组参数的GUAMI组，被“AMF信息配置”引用后，会导致组装NFProfile失败。 

“GUAMI组编号配置”通过[ADD SBIGUAMIARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 必选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




命令举例 


`
新增GUAMI组参数配置：配置索引为1，GUAMI组编号为1，PLMN ID编号为1，AMF标识为"000001"。
ADD SBIGUAMIARRPARAM:INDEX=1,ARRAYID=1,PLMNID=1,AMFID="000001";
` 


#### 修改GUAMI组参数配置(SET SBIGUAMIARRPARAM) 
#### 修改GUAMI组参数配置(SET SBIGUAMIARRPARAM) 


功能说明 

该命令用于修改GUAMI组参数配置。当AMF已配置可以服务的GUAMI组编号，需要修改归属于该GUAMI组编号的参数时，使用该命令。命令执行成功后，AMF修改了可以服务的该组GUAMI信息。 


注意事项 

如果要修改如下配置项，则需要保证如下配置都已经存在： 


 
“GUAMI组编号配置”通过SHOW SBIGUAMIARRID命令查询。 

 
“PLMN ID组编号配置”通过SHOW SBIPLMNID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




命令举例 


`
修改GUAMI组参数配置：配置索引为1，GUAMI组编号为1，PLMN ID编号为1，AMF标识为"000001"。
SET SBIGUAMIARRPARAM:INDEX=1,ARRAYID=1,PLMNID=1,AMFID="000001";
` 


#### 删除GUAMI组参数配置(DEL SBIGUAMIARRPARAM) 
#### 删除GUAMI组参数配置(DEL SBIGUAMIARRPARAM) 


功能说明 

该命令用于删除GUAMI组参数配置。当AMF已配置可以服务的GUAMI组编号，需要删除归属于该GUAMI组编号的参数时，使用该命令。命令执行成功后，AMF删除了可以服务的该组GUAMI信息。 


注意事项 

如果归属于某个GUAMI组编号的所有GUAMI组参数配置都已经删除，建议删除该GUAMI组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




命令举例 


`
删除GUAMI组参数配置：配置索引为1。
DEL SBIGUAMIARRPARAM:INDEX=1;
` 


#### 查询GUAMI组参数配置(SHOW SBIGUAMIARRPARAM) 
#### 查询GUAMI组参数配置(SHOW SBIGUAMIARRPARAM) 


功能说明 

该命令用于查询GUAMI组参数配置。当需要查询GUAMI组参数时，使用该命令。 

指定GUAMI组编号，可以查询指定的GUAMI组的参数信息；不指定GUAMI组编号，可以查询所有已经配置GUAMI组的参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是GUAMI组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号。GUAMI组编号引用“GUAMI组编号配置”中的配置，通过SHOW SBIGUAMIARRID命令查询。
PLMNID|PLMN ID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN ID编号。PLMN ID编号引用“PLMN ID组编号配置”中的配置，通过SHOW SBIPLMNID命令查询。
AMFID|AMF标识|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于设置AMF标识，由AMF区域标识（8位），AMF集标识（10位）和AMF指针（6位）组成。 它被编码为6个十六进制字符（即24位）的字符串。




命令举例 


`
查询GUAMI组参数配置：配置索引为1。
SHOW SBIGUAMIARRPARAM:INDEX=1

(No.1) : SHOW SBIGUAMIARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 GUAMI组编号 PLMN ID编号 AMF标识 
--------------------------------------------------------
复制 修改 删除 1        1           1           000001  
--------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:48:45 耗时: 0.623 秒

` 


## TAC范围组配置 
## TAC范围组配置 


背景知识 


TAC是跟踪区代码（Tracking Area Code，TAC），由运营商管理分配，定义某一运营商唯一的跟踪区代码。 

TAC由2或3个字节的字符串组成，以十六进制表示。在实际配置中，字符串长度为4或者6。 

本地NRF功能中，该配置主要用于限定TAC的范围，应用于TAI范围组配置中，用于表示TAC的范围。 




功能说明 


TAC范围组配置包括TAC范围组编号配置和TAC范围组参数配置，一个TAC范围组编号可以被若干个TAC范围组参数引用。 

TAC范围组配置主要用于在TAI范围组配置中限定TAC的范围，为TAI范围组配置中的必选参数。 




子主题： 






### TAC范围组编号配置 
### TAC范围组编号配置 


背景知识 


TAC是跟踪区代码（Tracking Area Code，TAC），由运营商管理分配，定义某一运营商唯一的跟踪区代码。 

TAC由2或3个字节的字符串组成，以十六进制表示。在实际配置中，字符串长度为4或者6。 

本地NRF功能中，该配置主要用于限定TAC的范围，应用于TAI范围组配置中，用于表示TAC的范围。 




功能说明 


TAC范围组编号配置用于配置一个TAC范围组，一个TAC范围组编号可以被若干个TAC范围组参数引用。 

当启用本地NRF功能时，如果需要配置TAI范围组，首先需要配置TAC范围组编号。 




子主题： 






#### 新增TAC范围组编号配置(ADD SBITACRANGEARRID) 
#### 新增TAC范围组编号配置(ADD SBITACRANGEARRID) 


功能说明 

该命令用于新增TAC范围组编号配置。当需要新增TAI范围组用于限定NF（SMF、AMF、NWDAF）可以服务的TAI范围时，使用该命令。执行成功后，可以在TAI范围组参数配置中关联该TAC范围组编号。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAC范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号。该编号全局唯一。




命令举例 


`
新增TAC范围组编号配置：TAC范围组编号为1。
ADD SBITACRANGEARRID:ARRAYID=1;
` 


#### 删除TAC范围组编号配置(DEL SBITACRANGEARRID) 
#### 删除TAC范围组编号配置(DEL SBITACRANGEARRID) 


功能说明 

该命令用于删除TAC范围组编号配置。当不再需要该TAC范围组时，例如引用该TAC范围组编号的TAI范围组参数已经删除，则使用该命令。 


注意事项 

删除TAC范围组编号前，需要把引用该TAC范围组编号的所有TAI范围组参数配置全部删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAC范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号。该编号全局唯一。




命令举例 


`
删除TAC范围组编号配置：TAC范围组编号为1。
DEL SBITACRANGEARRID:ARRAYID=1;
` 


#### 查询TAC范围组编号配置(SHOW SBITACRANGEARRID) 
#### 查询TAC范围组编号配置(SHOW SBITACRANGEARRID) 


功能说明 

该命令用于查询TAC范围组编号配置。当需要查询已经配置的TAC范围组编号信息时，使用该命令。查询时，可以指定TAC范围组编号，查询成功后，会回显对应的TAC范围组编号信息；如果不指定TAC范围组编号，则回显已经配置的所有TAC范围组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号。该编号全局唯一。




命令举例 


`
查询TAC范围组编号配置：TAC范围组编号为1。
SHOW SBITACRANGEARRID:ARRAYID=1

(No.6) : SHOW SBITACRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       TAC范围组编号 
-----------------------------
复制 删除      1             
-----------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:03:30 耗时: 0.621 秒

` 


### TAC范围组参数配置 
### TAC范围组参数配置 


背景知识 


TAC是跟踪区代码（Tracking Area Code，TAC），由运营商管理分配，定义某一运营商唯一的跟踪区代码。 

TAC由2或3个字节的字符串组成，以十六进制表示。在实际配置中，字符串长度为4或者6。 

本地NRF功能中，该配置主要用于限定TAC的范围，应用于TAI范围组配置中，用于表示TAC的范围。 




功能说明 


TAC范围组参数配置用于配置TAC范围的开始和结束，并通过TAC范围组编号标识该TAC范围组参数归属于哪个TAC范围组。 

当需要限定NF（SMF、AMF、NWDAF）可以服务的TAI范围时，需要配置TAC范围组参数。配置完成后，在TAI范围组参数配置中可以引用该TAC范围组归属的TAC范围组编号。 

没有配置TAC范围组参数的TAC范围组编号将不能被TAI范围组参数配置引用。如果该TAC范围组编号被TAI范围组引用，在组装NFProfile时会失败。 




子主题： 






#### 新增TAC范围组参数配置(ADD SBITACRANGEARRPARAM) 
#### 新增TAC范围组参数配置(ADD SBITACRANGEARRPARAM) 


功能说明 

该命令用于新增TAC范围组参数配置。用于表示一个具体的TAC范围，被TAI范围组参数配置引用。当需要新增TAI范围组参数配置且需要引用的TAC范围不存在时，执行该命令。 


注意事项 

目前不支持检查参数START和END的大小关系。如果配置错误，则会导致在本地NRF匹配时失败，达不到预期的匹配效果。 

 
需要保证该组参数归属的组编号已经存在，可以通过SHOW SBITACRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。该索引全局唯一。
ARRAYID|TAC范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 必选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 必选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




命令举例 


`
新增TAC范围组参数配置：TAC范围组参数配置索引为1，TAC范围组编号为1，开始为“1234”，结束为“4567”。
ADD SBITACRANGEARRPARAM:INDEX=1,ARRAYID=1,START="1234",END="4567";
` 


#### 修改TAC范围组参数配置(SET SBITACRANGEARRPARAM) 
#### 修改TAC范围组参数配置(SET SBITACRANGEARRPARAM) 


功能说明 

该命令用于修改TAC范围组参数配置。用于修改已经存在的TAC范围，或者修改归属的TAC范围组编号。当需要修改上述两项内容时，执行该命令。 


注意事项 

目前不支持检查参数START和END的大小关系。如果配置错误，则会导致在本地NRF匹配时失败，达不到预期的匹配效果。 

 
如果修改归属的组编号配置，需要保证该组编号已经存在，可以通过SHOW SBITACRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。该索引全局唯一。
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




命令举例 


`
修改TAC范围组参数配置：TAC范围组参数配置索引为1，TAC范围组编号为1，开始为“5678”，结束为“6789”。
SET SBITACRANGEARRPARAM:INDEX=1,ARRAYID=1,START="5678",END="6789";
` 


#### 删除TAC范围组参数配置(DEL SBITACRANGEARRPARAM) 
#### 删除TAC范围组参数配置(DEL SBITACRANGEARRPARAM) 


功能说明 

该命令用于删除TAC范围组参数配置。因为TAC范围组参数配置是为TAI范围组参数配置服务的，其所归属的TAC范围组编号被TAI范围组参数配置所引用。所以当其归属的TAC范围组编号不再被任何TAI范围组参数配置引用时，可以执行该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。该索引全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




命令举例 


`
删除TAC范围组参数配置：TAC范围组参数配置索引为1。
DEL SBITACRANGEARRPARAM:INDEX=1;
` 


#### 查询TAC范围组参数配置(SHOW SBITACRANGEARRPARAM) 
#### 查询TAC范围组参数配置(SHOW SBITACRANGEARRPARAM) 


功能说明 

该命令用于查询TAC范围组参数配置。当需要查询已经配置的TAC范围组参数信息时，执行该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有TAC范围组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。该索引全局唯一。
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组参数配置索引。
ARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，该编号通过SHOW SBITACRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组开始位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围开始的第一个值。目前支持的长度是4或者6。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC范围组结束位置，当将TAC的范围表示为十六进制范围（例如TAC范围）时，将使用标识TAC范围结尾的最后一个值。目前支持的长度是4或者6。




命令举例 


`
查询TAC范围组参数配置：TAC范围组参数配置索引为1。
SHOW SBITACRANGEARRPARAM:INDEX=1

(No.8) : SHOW SBITACRANGEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 TAC范围组编号 开始 结束   
--------------------------------------------------
复制 修改 删除 1        65535         abcd cdefa1 
--------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:03:53 耗时: 0.608 秒

` 


## TAI组配置 
## TAI组配置 


背景知识 


TAI（Tracking Area Identity，跟踪区识别码）用于标识跟踪区域，由MCC、MNC及TAC（Tracking Area Code，跟踪区代码）组成。 

格式为：<TAI> = <MCC><MNC><TAC> 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
TAC由2或3个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的PLMN NID编号中配置，该编号可以通过[SHOW SBIPLMNNID]命令查询。

本地NRF功能中，通过TAI组配置，可以限定SMF、AMF、UPF、NWDAF四个NF可以服务的TAI列表。通过TAI范围组该配置可以限定SMF、AMF、NWDAF三个NF可以服务的TAI范围列表。TAI组配置和TAI范围组配置一般配合使用,用于限定NF可以服务的TAI信息。 

如果是一组具体的TAI，则使用TAI组配置。 

 
如果限定的TAI信息是一组范围，则使用TAI范围组配置。 




功能说明 


TAI组数据配置包括TAI组编号配置和TAI组参数配置，一个TAI组编号可以被若干个TAI组参数引用。 

TAI组配置应用于SMF、AMF、UPF、NWDAF四个NF信息配置中，用于限定这四个NF可以服务的TAI列表。该配置一般和TAI范围组配合使用，如果上述NF中TAI组配置和TAI范围组配置都没有配置，则该NF可以为服务网络中的所有TAI服务。 




子主题： 






### TAI组编号配置 
### TAI组编号配置 


背景知识 


TAI（Tracking Area Identity，跟踪区识别码）用于标识跟踪区域，由MCC、MNC及TAC（Tracking Area Code，跟踪区代码）组成。 

格式为：<TAI> = <MCC><MNC><TAC> 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
TAC由2或3个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的PLMN NID编号中配置，该编号可以通过[SHOW SBIPLMNNID]命令查询。

本地NRF功能中，通过TAI组配置，可以限定SMF、AMF、UPF、NWDAF四个NF可以服务的TAI列表。通过TAI范围组该配置可以限定SMF、AMF、NWDAF三个NF可以服务的TAI范围列表。TAI组配置和TAI范围组配置一般配合使用,用于限定NF可以服务的TAI信息。 

如果是一组具体的TAI，则使用TAI组配置。 

 
如果限定的TAI信息是一组范围，则使用TAI范围组配置。 




功能说明 


TAI组编号配置用于配置一个TAI组，一个TAI组包含了若干个TAI组参数。 

当启用本地NRF功能时，如果NF（SMF、AMF、UPF、NWDAF）需要限定可以服务的TAI列表，则需要配置TAI组编号。配置后，在本地NRF配置的NF扩展信息中关联该TAI组编号。 

如果本地NRF配置中没有关联TAI组配置，也没有TAI范围组配置，则该NF可以为服务网络中的所有TAI服务。 




子主题： 






#### 新增TAI组编号配置(ADD SBITAIARRID) 
#### 新增TAI组编号配置(ADD SBITAIARRID) 


功能说明 

该命令用于新增TAI组编号配置。当SMF、AMF、UPF、NWDAF四个NF需要新增限定可以服务的TAI列表时，使用该命令。执行成功后，可以在上述四个NF配置信息中关联该组编号。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号。该编号全局唯一。




命令举例 


`
新增TAI组编号配置：TAI组编号为9。
ADD SBITAIARRID:ARRAYID=9;
` 


#### 删除TAI组编号配置(DEL SBITAIARRID) 
#### 删除TAI组编号配置(DEL SBITAIARRID) 


功能说明 

该命令用于删除TAI组编号配置。当该TAI组编号不再被任何NF关联时，可以使用该命令删除TAI组编号配置。 


注意事项 

删除前需要把归属于该TAI组编号的所有TAI组参数配置删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号。该编号全局唯一。




命令举例 


`
删除TAI组编号配置：TAI组编号为9。
DEL SBITAIARRID:ARRAYID=9;
` 


#### 查询TAI组编号配置(SHOW SBITAIARRID) 
#### 查询TAI组编号配置(SHOW SBITAIARRID) 


功能说明 

该命令用于查询TAI组编号配置。当需要查询已经配置的TAI组编号信息时，使用该命令。查询时，可以指定TAI组编号，查询成功后，会回显对应的TAI组编号信息；如果不指定TAI组编号，则回显已经配置的所有TAI组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号。该编号全局唯一。




命令举例 


`
查询TAI组编号配置：TAI组编号为9。
SHOW SBITAIARRID:ARRAYID=9

(No.3) : SHOW SBITAIARRID:ARRAYID=9
-----------------CommonS_HTTP_LB_0----------------
操作维护       TAI组编号  
--------------------
复制  删除      9    
--------------------
记录数：1
执行成功 开始时间:2020-10-29 15:36:01 耗时: 0.133 秒

` 


### TAI组参数配置 
### TAI组参数配置 


背景知识 


TAI（Tracking Area Identity，跟踪区识别码）用于标识跟踪区域，由MCC、MNC及TAC（Tracking Area Code，跟踪区代码）组成。 

格式为：<TAI> = <MCC><MNC><TAC> 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
TAC由2或3个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的PLMN NID编号中配置，该编号可以通过[SHOW SBIPLMNNID]命令查询。

本地NRF功能中，通过TAI组配置，可以限定SMF、AMF、UPF、NWDAF四个NF可以服务的TAI列表。通过TAI范围组该配置可以限定SMF、AMF、NWDAF三个NF可以服务的TAI范围列表。TAI组配置和TAI范围组配置一般配合使用,用于限定NF可以服务的TAI信息。 

如果是一组具体的TAI，则使用TAI组配置。 

 
如果限定的TAI信息是一组范围，则使用TAI范围组配置。 




功能说明 


TAI组参数配置用于配置TAI组的具体信息，包括：MCC、MNC和TAC，并通过TAI组编号标识该TAI组参数归属于哪个TAI组。 

当NF（SMF、AMF、UPF、NWDAF）需要限定服务的具体TAI时，需要配置TAI组参数。配置完成后，在NF配置中引用该TAI组参数归属的TAI组编号。 

没有配置TAI组参数的TAI组编号将不能被NF配置引用。如果NF（SMF、AMF、UPF、NWDAF）引用了该TAI组编号，在组装NFProfile时会失败。 




子主题： 






#### 新增TAI组参数配置(ADD SBITAIARRPARAM) 
#### 新增TAI组参数配置(ADD SBITAIARRPARAM) 


功能说明 

该命令用于新增TAI组参数配置。当某个TAI组中需要增加NF（SMF、AMF、UPF、NWDAF）可以服务的TAI时，使用该命令在TAI组内增加TAI组参数。命令执行成功后，关联该TAI组的NF（SMF、AMF、UPF、NWDAF）对新增的TAI提供服务。 


注意事项 

需要保证该组参数归属的TAI组编号已经存在，该组编号通过SHOW SBITAIARRID命令查询。 

 
需要保证关联的PLMN NID编号已经存在，该编号可以通过SHOW SBIPLMNNID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 必选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




命令举例 


`
新增TAI组参数配置：TAI组参数配置索引为1，TAI组编号为9， PLMN NID编号为1，TAC为“1234”。
ADD SBITAIARRPARAM:INDEX=1,ARRAYID=9,PLMNNID=1,TAC="1234";
` 


#### 修改TAI组参数配置(SET SBITAIARRPARAM) 
#### 修改TAI组参数配置(SET SBITAIARRPARAM) 


功能说明 

该命令用于修改TAI组参数配置。当NF（SMF、AMF、UPF、NWDAF）服务的TAI信息发生变更时，使用该命令修改NF关联的TAI组内的TAI组参数信息。命令执行成功后，关联该TAI组的NF（SMF、AMF、UPF、NWDAF）对TAI组内的TAI提供服务。 


注意事项 

如果修改归属的TAI组编号，需要保证该组编号已经存在，可以通过SHOW SBITAIARRID命令查询。 

 
如果修改关联的PLMN NID编号，需要保证该编号已经存在，可以通过SHOW SBIPLMNNID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




命令举例 


`
修改TAI组参数配置：TAI组参数配置索引为1，TAI组编号为9，PLMN NID编号为1，TAC为“5678”。
SET SBITAIARRPARAM:INDEX=1,ARRAYID=9,PLMNNID=1,TAC="5678";
` 


#### 删除TAI组参数配置(DEL SBITAIARRPARAM) 
#### 删除TAI组参数配置(DEL SBITAIARRPARAM) 


功能说明 

该命令用于删除TAI组参数配置。当NF（SMF、AMF、UPF、NWDAF）不再对某个TAI提供服务时，使用该命令删除NF所关联的TAI组中该TAI的参数组信息。命令执行成功后，NF不再对该TAI提供服务。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




命令举例 


`
删除TAI组参数配置：TAI组参数配置索引为1。
DEL SBITAIARRPARAM:INDEX=1;
` 


#### 查询TAI组参数配置(SHOW SBITAIARRPARAM) 
#### 查询TAI组参数配置(SHOW SBITAIARRPARAM) 


功能说明 

该命令用于查询TAI组参数配置。当需要查询已经配置的TAI组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有TAI组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组参数配置索引。该索引全局唯一。
ARRAYID|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。表示该TAI组参数配置归属于哪个TAI组。
TAC|TAC|参数可选性: 任选参数类型: 字符串参数范围: 4-6|该参数用于设置TAC，2或3个字节的字符串，以十六进制表示，标识指定的跟踪区号。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，该编号可以通过SHOW SBIPLMNNID命令查询。可以通过该编号获取到TAI的MCC和MNC信息。




命令举例 


`
查询TAI组参数配置:TAI组参数配置索引为1。
SHOW SBITAIARRPARAM:INDEX=1

(No.4) : SHOW SBITAIARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 TAI组编号 TAC    PLMN NID编号 
-----------------------------------------------------
复制 修改 删除 1        1         63F84B 1           
-----------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:03:01 耗时: 0.583 秒

` 


## TAI范围组配置 
## TAI范围组配置 


背景知识 


TAI（Tracking Area Identity，跟踪区识别码）用于标识跟踪区域，由MCC、MNC及TAC（Tracking Area Code，跟踪区代码）组成。 

格式为：<TAI> = <MCC><MNC><TAC> 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
TAC由2或3个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的PLMN NID编号中配置，该编号可以通过[SHOW SBIPLMNNID]命令查询。TAC在TAC范围组编号中配置，该编号可以通过[SHOW SBITACRANGEARRID]命令查询。

本地NRF功能中，该配置以组编号的方式对外呈现，在NF（SMF、AMF、NWDAF）扩展信息配置中引用该组编号，用于表示该NF可以服务的TAI范围列表。 

TAI范围组配置与TAI组配置配合使用，表示对应NF可以服务的TAI信息。其中，TAI组配置表示NF（SMF、AMF、UPF、NWDAF）可以服务的TAI列表。如果TAI信息是一组范围，则使用TAI范围组配置；如果TAI信息是一组具体的TAI，则使用TAI组配置。 




功能说明 


本地NRF功能打开时，TAI范围组是以一组数据配置呈现的，该组数据配置包括TAI范围组编号配置和TAI范围组参数配置，一个TAI范围组编号可以被若干个TAI范围组参数引用。 

TAI范围组配置应用于NF（SMF、AMF、NWDAF）扩展信息配置中，用于表示该NF可以服务的TAI范围列表。该配置一般和TAI组配合使用，如果上述NF中TAI组配置和TAI范围组配置都没有配置，则说明该NF可以为服务网络中的所有TAI服务。 




子主题： 






### TAI范围组编号配置 
### TAI范围组编号配置 


背景知识 


TAI（Tracking Area Identity，跟踪区识别码）用于标识跟踪区域，由MCC、MNC及TAC（Tracking Area Code，跟踪区代码）组成。 

格式为：<TAI> = <MCC><MNC><TAC> 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
TAC由2或3个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的PLMN NID编号中配置，该编号可以通过[SHOW SBIPLMNNID]命令查询。TAC在TAC范围组编号中配置，该编号可以通过[SHOW SBITACRANGEARRID]命令查询。

本地NRF功能中，该配置以组编号的方式对外呈现，在NF（SMF、AMF、NWDAF）扩展信息配置中引用该组编号，用于表示该NF可以服务的TAI范围列表。 

TAI范围组配置与TAI组配置配合使用，表示对应NF可以服务的TAI信息。其中，TAI组配置表示NF（SMF、AMF、UPF、NWDAF）可以服务的TAI列表。如果TAI信息是一组范围，则使用TAI范围组配置；如果TAI信息是一组具体的TAI，则使用TAI组配置。 




功能说明 


TAI范围组编号配置用于配置一个TAI范围组，一个TAI范围组包含了若干个TAI范围组参数。 

当启用本地NRF功能时，如果NF（SMF、AMF、NWDAF）需要增加可以服务的TAI范围列表时，则需要配置TAI范围组编号。配置后，最终呈现在本地NRF配置的NF扩展信息的TAI范围数组中。如果不配置，并且也没有TAI组配置，则说明该NF可以为服务网络中的所有TAI服务。 




子主题： 






#### 新增TAI范围组编号配置(ADD SBITAIRANGEARRID) 
#### 新增TAI范围组编号配置(ADD SBITAIRANGEARRID) 


功能说明 

该命令用于新增TAI范围组编号配置。当NF（SMF、AMF、NWDAF）需要新增可以服务的TAI范围组时，使用该命令。执行成功后，可以在NF扩展信息配置中关联该TAI范围组编号。 

其中，SMF信息配置使用[ADD SBISMFINFO]命令，AMF信息配置使用[ADD SBIAMFINFO]命令，NWDAF信息配置使用[ADD SBINWDAFINFO]命令。


注意事项 

必须先配置该TAI范围组编号，才能在NF（SMF、AMF、NWDAF）扩展信息配置中引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，该编号全局唯一。TAI范围组编号被以下配置引用：NF扩展信息配置：用于新增NF（SMF、AMF、NWDAF）可以服务的TAI范围列表。SMF信息配置可以使用SHOW SBISMFINFO命令查询，AMF信息配置可以使用SHOW SBIAMFINFO命令查询，NWDAF信息配置可以使用SHOW SBINWDAFINFO命令查询。TAI范围组参数配置：一个TAI范围组编号可以被若干个TAI范围组参数引用。TAI范围组参数配置可以使用SHOW SBITAIRANGEARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，该编号全局唯一。TAI范围组编号被以下配置引用：NF扩展信息配置：用于新增NF（SMF、AMF、NWDAF）可以服务的TAI范围列表。SMF信息配置可以使用SHOW SBISMFINFO命令查询，AMF信息配置可以使用SHOW SBIAMFINFO命令查询，NWDAF信息配置可以使用SHOW SBINWDAFINFO命令查询。TAI范围组参数配置：一个TAI范围组编号可以被若干个TAI范围组参数引用。TAI范围组参数配置可以使用SHOW SBITAIRANGEARRPARAM命令查询。




命令举例 


`
新增TAI范围组编号配置：TAI范围组编号为1。
ADD SBITAIRANGEARRID:ARRAYID=1;
` 


#### 删除TAI范围组编号配置(DEL SBITAIRANGEARRID) 
#### 删除TAI范围组编号配置(DEL SBITAIRANGEARRID) 


功能说明 

该命令用于删除TAI范围组编号配置。当SMF、AMF、NWDAF三个NF不再关联该TAI范围组编号时，可以使用该命令删除TAI范围组编号配置。 


注意事项 

删除前需要把归属于该TAI范围组编号的所有TAI范围组参数配置删除。可以使用命令[SHOW SBITAIRANGEARRPARAM]:ARRAYID=TAI范围组编号查询归属于该TAI范围组编号的所有TAI范围组参数配置。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，该编号全局唯一。TAI范围组编号被以下配置引用：NF扩展信息配置：用于新增NF（SMF、AMF、NWDAF）可以服务的TAI范围列表。SMF信息配置可以使用SHOW SBISMFINFO命令查询，AMF信息配置可以使用SHOW SBIAMFINFO命令查询，NWDAF信息配置可以使用SHOW SBINWDAFINFO命令查询。TAI范围组参数配置：一个TAI范围组编号可以被若干个TAI范围组参数引用。TAI范围组参数配置可以使用SHOW SBITAIRANGEARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，该编号全局唯一。TAI范围组编号被以下配置引用：NF扩展信息配置：用于新增NF（SMF、AMF、NWDAF）可以服务的TAI范围列表。SMF信息配置可以使用SHOW SBISMFINFO命令查询，AMF信息配置可以使用SHOW SBIAMFINFO命令查询，NWDAF信息配置可以使用SHOW SBINWDAFINFO命令查询。TAI范围组参数配置：一个TAI范围组编号可以被若干个TAI范围组参数引用。TAI范围组参数配置可以使用SHOW SBITAIRANGEARRPARAM命令查询。




命令举例 


`
删除TAI范围组编号配置：TAI范围组编号为1。
DEL SBITAIRANGEARRID:ARRAYID=1;
` 


#### 查询TAI范围组编号配置(SHOW SBITAIRANGEARRID) 
#### 查询TAI范围组编号配置(SHOW SBITAIRANGEARRID) 


功能说明 

该命令用于查询TAI范围组编号配置。查询时，可以指定TAI范围组编号，查询成功后，会回显对应的TAI范围组编号信息；如果不指定TAI范围组编号，则回显已经配置的所有TAI范围组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，该编号全局唯一。TAI范围组编号被以下配置引用：NF扩展信息配置：用于新增NF（SMF、AMF、NWDAF）可以服务的TAI范围列表。SMF信息配置可以使用SHOW SBISMFINFO命令查询，AMF信息配置可以使用SHOW SBIAMFINFO命令查询，NWDAF信息配置可以使用SHOW SBINWDAFINFO命令查询。TAI范围组参数配置：一个TAI范围组编号可以被若干个TAI范围组参数引用。TAI范围组参数配置可以使用SHOW SBITAIRANGEARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，该编号全局唯一。TAI范围组编号被以下配置引用：NF扩展信息配置：用于新增NF（SMF、AMF、NWDAF）可以服务的TAI范围列表。SMF信息配置可以使用SHOW SBISMFINFO命令查询，AMF信息配置可以使用SHOW SBIAMFINFO命令查询，NWDAF信息配置可以使用SHOW SBINWDAFINFO命令查询。TAI范围组参数配置：一个TAI范围组编号可以被若干个TAI范围组参数引用。TAI范围组参数配置可以使用SHOW SBITAIRANGEARRPARAM命令查询。




命令举例 


`
查询TAI范围组编号配置：TAI范围组编号为1。
SHOW SBITAIRANGEARRID:ARRAYID=1

(No.9) : SHOW SBITAIRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       TAI范围组编号 
-----------------------------
复制 删除      1             
-----------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:04:36 耗时: 0.609 秒

` 


### TAI范围组参数配置 
### TAI范围组参数配置 


背景知识 


TAI（Tracking Area Identity，跟踪区识别码）用于标识跟踪区域，由MCC、MNC及TAC（Tracking Area Code，跟踪区代码）组成。 

格式为：<TAI> = <MCC><MNC><TAC> 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 
TAC由2或3个字节的字符串组成，以十六进制表示。 

 

其中，MCC和MNC在关联的PLMN NID编号中配置，该编号可以通过[SHOW SBIPLMNNID]命令查询。TAC在TAC范围组编号中配置，该编号可以通过[SHOW SBITACRANGEARRID]命令查询。

本地NRF功能中，该配置以组编号的方式对外呈现，在NF（SMF、AMF、NWDAF）扩展信息配置中引用该组编号，用于表示该NF可以服务的TAI范围列表。 

TAI范围组配置与TAI组配置配合使用，表示对应NF可以服务的TAI信息。其中，TAI组配置表示NF（SMF、AMF、UPF、NWDAF）可以服务的TAI列表。如果TAI信息是一组范围，则使用TAI范围组配置；如果TAI信息是一组具体的TAI，则使用TAI组配置。 




功能说明 


TAI范围组参数配置用于配置TAI范围组的三个组成部分的具体信息：MCC、MNC和TAC范围。同时，会在“TAI范围组编号”中配置该TAI范围组参数归属于哪个TAI范围组。 

当NF（SMF、AMF、NWDAF）需要新增可以提供服务的TAI范围时，需要配置归属于该TAI范围组的参数。配置完成后，在NF中引用该TAI范围组参数归属的TAI范围组编号。如果不配置TAI范围组参数，则无法配置具体的TAI范围信息，已经配置的TAI范围组编号只能是一个孤立配置。如果NF（SMF、AMF、NWDAF）引用了该TAI范围组编号，那么在组装NFProfile时会失败。 




子主题： 






#### 新增TAI范围组参数配置(ADD SBITAIRANGEARRPARAM) 
#### 新增TAI范围组参数配置(ADD SBITAIRANGEARRPARAM) 


功能说明 

该命令用于新增TAI范围组参数配置。当NF（SMF、AMF、NWDAF）已配置可以服务的TAI范围组编号，需要新增归属于该TAI范围组编号的参数时，使用该命令。执行成功后，NF（SMF、AMF、NWDAF）新增了可以服务的该范围组参数的TAI信息。 


注意事项 

需要保证该范围组参数归属的TAI范围组编号已经存在，该编号通过SHOW SBITAIRANGEARRID命令查询。 

 
需要保证关联的PLMN NID编号已经存在，该编号通过SHOW SBIPLMNNID命令查询。 

 
需要保证关联的TAC范围组编号已经存在，该编号通过SHOW SBITACRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




命令举例 


`
新增TAI范围组参数配置：TAI范围组参数配置索引为1，TAI范围组标识为1，PLMN NID编号为1，TAC范围组编号为1。
ADD SBITAIRANGEARRPARAM:INDEX=1,ARRAYID=1,PLMNNID=1,TACRANGEARRAYID=1;
` 


#### 修改TAI范围组参数配置(SET SBITAIRANGEARRPARAM) 
#### 修改TAI范围组参数配置(SET SBITAIRANGEARRPARAM) 


功能说明 

该命令用于修改TAI范围组参数配置。当NF（SMF、AMF、NWDAF）已配置可以服务的TAI范围组编号，需要修改归属于该TAI范围组编号的参数时，使用该命令。执行成功后，NF（SMF、AMF、NWDAF）修改了可以服务的该范围组参数的TAI信息。 


注意事项 

如果修改该范围组参数归属的TAI范围组编号，则需要保证该范围组编号已经存在，该编号通过SHOW SBITAIRANGEARRID命令查询。 

 
如果修改关联的PLMN NID编号，则需要保证该编号已经存在，该编号通过SHOW SBIPLMNNID命令查询。 

 
如果修改关联的TAC范围组编号，则需要保证该编号已经存在，该编号通过SHOW SBITACRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




命令举例 


`
修改TAI范围组参数配置：TAI范围组参数配置索引为1，TAI范围组标识为1，PLMN NID编号为1，TAC范围组编号为7。
SET SBITAIRANGEARRPARAM:INDEX=1,ARRAYID=1,PLMNNID=1,TACRANGEARRAYID=7;
` 


#### 删除TAI范围组参数配置(DEL SBITAIRANGEARRPARAM) 
#### 删除TAI范围组参数配置(DEL SBITAIRANGEARRPARAM) 


功能说明 

该命令用于新增TAI范围组参数配置。当NF（SMF、AMF、NWDAF）已配置可以服务的TAI范围组编号，需要删除归属于该TAI范围组编号的参数时，使用该命令。执行成功后，NF（SMF、AMF、NWDAF）删除了可以服务的该范围组参数的TAI信息。 


注意事项 

如果归属于某个TAI范围组编号的所有TAI范围组参数配置都已经删除，建议删除该TAI范围组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




命令举例 


`
删除TAI范围组参数配置：TAI范围组参数配置索引为1。
DEL SBITAIRANGEARRPARAM:INDEX=1;
` 


#### 查询TAI范围组参数配置(SHOW SBITAIRANGEARRPARAM) 
#### 查询TAI范围组参数配置(SHOW SBITAIRANGEARRPARAM) 


功能说明 

该命令用于查询TAI范围组参数配置。当需要查询已经配置的TAI范围组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有TAI范围组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组参数配置索引，该索引全局唯一。
ARRAYID|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAI范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBITAIRANGEARRID命令查询。
PLMNNID|PLMN NID编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN NID编号，可以通过该编号获取到TAI的MCC和MNC信息。该编号通过SHOW SBIPLMNNID命令查询。
TACRANGEARRAYID|TAC范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置TAC范围组编号，可以通过该编号获取到TAC的范围信息。该编号通过SHOW SBITACRANGEARRID命令查询。




命令举例 


`
查询TAI范围组参数配置：TAI范围组参数配置索引为1。
SHOW SBITAIRANGEARRPARAM:INDEX=1

(No.10) : SHOW SBITAIRANGEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 TAI范围组编号 PLMN NID编号 TAC范围组编号 
----------------------------------------------------------------
复制 修改 删除 1        65535         65535       741           
----------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:04:55 耗时: 0.621 秒

` 


## DNN组配置 
## DNN组配置 


背景知识 


DNN（Data Network Name，数据网络名称）用于标识5G网络名称，由网络标识符和运营商标识符两部分组成。DNN被编码为字符串格式，且由点进行分割（例如 Label1.Label2.Label3）。 


 
网络标识符：外部网络的标识符号，必选参数。 

 
运营商标识符：归属运营商的表示符号，可选参数。 

 

本地NRF功能中，该配置以组编号的方式对外呈现，在NF（例如：PCF、BSF）扩展信息配置中引用该组编号，用于表示该NF可以服务的DNN列表。 

如果DNN不包括运营商标识符，则NF配置的PLMN组中的所有PLMN都支持DNN。其中，NF配置的PLMN组可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置DNN，则说明其可以服务于任何DNN。




功能说明 


本地NRF功能打开时，DNN组是以一组数据配置呈现的，该组数据配置包括DNN组编号配置和DNN组参数配置，一个DNN组编号可以被若干个DNN组参数引用。 

当NF（例如：PCF、BSF）需要新增该NF可以服务的DNN列表时，使用该配置。 




子主题： 






### DNN组编号配置 
### DNN组编号配置 


背景知识 


DNN（Data Network Name，数据网络名称）用于标识5G网络名称，由网络标识符和运营商标识符两部分组成。DNN被编码为字符串格式，且由点进行分割（例如 Label1.Label2.Label3）。 


 
网络标识符：外部网络的标识符号，必选参数。 

 
运营商标识符：归属运营商的表示符号，可选参数。 

 

本地NRF功能中，该配置以组编号的方式对外呈现，在NF（例如：PCF、BSF）扩展信息配置中引用该组编号，用于表示该NF可以服务的DNN列表。 

如果DNN不包括运营商标识符，则NF配置的PLMN组中的所有PLMN都支持DNN。其中，NF配置的PLMN组可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置DNN，则说明其可以服务于任何DNN。




功能说明 


DNN组编号配置用于配置一个DNN组，一个DNN组包含了若干个DNN组参数。 

当启用本地NRF功能时，如果NF（例如：PCF、BSF）需要增加可以服务的DNN列表，则需要配置DNN范围组编号。配置后，最终呈现在本地NRF配置的NF扩展信息的DNN数组中。如果不配置，则说明该NF可以为服务网络中的所有DNN服务。 




子主题： 






#### 新增DNN组编号配置(ADD SBIDNNARRID) 
#### 新增DNN组编号配置(ADD SBIDNNARRID) 


功能说明 

该命令用于新增DNN组编号配置。当NF（例如：PCF、BSF）需要新增可以服务的DNN组时，使用该命令。执行成功后，可以在NF扩展信息配置中关联该DNN组编号。 

其中，PCF扩展信息配置使用[ADD SBIPCFINFO]命令，BSF扩展信息配置使用[ADD SBIBSFINFO]命令。


注意事项 

必须先配置该DNN组编号，才能在NF（例如：PCF、BSF）扩展信息配置中引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号全局唯一。DNN组编号被以下配置引用：NF扩展信息配置：用于新增NF（PCF、BSF等）可以服务的DNN列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询，PCF扩展信息配置可以使用SHOW SBIPCFINFO命令查询。DNN组参数配置：一个DNN组编号可以被若干个DNN组参数引用。DNN组参数配置可以使用SHOW SBIDNNARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号全局唯一。DNN组编号被以下配置引用：NF扩展信息配置：用于新增NF（PCF、BSF等）可以服务的DNN列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询，PCF扩展信息配置可以使用SHOW SBIPCFINFO命令查询。DNN组参数配置：一个DNN组编号可以被若干个DNN组参数引用。DNN组参数配置可以使用SHOW SBIDNNARRPARAM命令查询。




命令举例 


`
新增DNN组编号配置：DNN组编号为1。 
ADD SBIDNNARRID:ARRAYID=1
` 


#### 删除DNN组编号配置(DEL SBIDNNARRID) 
#### 删除DNN组编号配置(DEL SBIDNNARRID) 


功能说明 

该命令用于删除DNN组编号配置。当NF（例如：PCF、BSF）不再关联该DNN组编号时，可以使用该命令删除DNN组编号配置。 


注意事项 

删除前需要把归属于该DNN组编号的所有DNN组参数配置删除。可以使用命令[SHOW SBIDNNARRPARAM]指定DNN组编号的方式，查询归属于该DNN组编号的所有DNN组参数配置。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号全局唯一。DNN组编号被以下配置引用：NF扩展信息配置：用于新增NF（PCF、BSF等）可以服务的DNN列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询，PCF扩展信息配置可以使用SHOW SBIPCFINFO命令查询。DNN组参数配置：一个DNN组编号可以被若干个DNN组参数引用。DNN组参数配置可以使用SHOW SBIDNNARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号全局唯一。DNN组编号被以下配置引用：NF扩展信息配置：用于新增NF（PCF、BSF等）可以服务的DNN列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询，PCF扩展信息配置可以使用SHOW SBIPCFINFO命令查询。DNN组参数配置：一个DNN组编号可以被若干个DNN组参数引用。DNN组参数配置可以使用SHOW SBIDNNARRPARAM命令查询。




命令举例 


`
删除DNN组编号配置：DNN组编号为1。
DEL SBIDNNARRID:ARRAYID=1
` 


#### 查询DNN组编号配置(SHOW SBIDNNARRID) 
#### 查询DNN组编号配置(SHOW SBIDNNARRID) 


功能说明 

该命令用于查询DNN组编号配置。查询时，可以指定DNN组编号，查询成功后，会回显对应的DNN组编号信息；如果不指定DNN组编号，则回显已经配置的所有DNN组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号全局唯一。DNN组编号被以下配置引用：NF扩展信息配置：用于新增NF（PCF、BSF等）可以服务的DNN列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询，PCF扩展信息配置可以使用SHOW SBIPCFINFO命令查询。DNN组参数配置：一个DNN组编号可以被若干个DNN组参数引用。DNN组参数配置可以使用SHOW SBIDNNARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号全局唯一。DNN组编号被以下配置引用：NF扩展信息配置：用于新增NF（PCF、BSF等）可以服务的DNN列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询，PCF扩展信息配置可以使用SHOW SBIPCFINFO命令查询。DNN组参数配置：一个DNN组编号可以被若干个DNN组参数引用。DNN组参数配置可以使用SHOW SBIDNNARRPARAM命令查询。




命令举例 


`
查询DNN组编号配置：DNN组编号为1。
SHOW SBIDNNARRID:ARRAYID=1

(No.11) : SHOW SBIDNNARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       DNN组编号 
-------------------------
复制 删除      1         
-------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:05:13 耗时: 0.597 秒

` 


### DNN组参数配置 
### DNN组参数配置 


背景知识 


DNN（Data Network Name，数据网络名称）用于标识5G网络名称，由网络标识符和运营商标识符两部分组成。DNN被编码为字符串格式，且由点进行分割（例如 Label1.Label2.Label3）。 


 
网络标识符：外部网络的标识符号，必选参数。 

 
运营商标识符：归属运营商的表示符号，可选参数。 

 

本地NRF功能中，该配置以组编号的方式对外呈现，在NF（例如：PCF、BSF）扩展信息配置中引用该组编号，用于表示该NF可以服务的DNN列表。 

如果DNN不包括运营商标识符，则NF配置的PLMN组中的所有PLMN都支持DNN。其中，NF配置的PLMN组可以通过[SHOW SBIPEERNFBASEINFO]命令查询。如果该NF中没有配置DNN，则说明其可以服务于任何DNN。




功能说明 


DNN组参数配置用于配置DNN的具体信息。同时，会在“DNN组编号”中配置该DNN组参数归属于哪个DNN组。 

当NF（例如：PCF、BSF）需要新增可以提供服务的DNN列表时，需要配置归属于该DNN组的参数。配置完成后，在NF中引用该DNN组参数归属的DNN组编号。如果不配置DNN组参数，则无法配置具体的DNN信息，已经配置的DNN组编号只能是一个孤立配置。如果NF（例如：PCF、BSF）引用了该DNN组编号，那么在组装NFProfile时会失败。 




子主题： 






#### 新增DNN组参数配置(ADD SBIDNNARRPARAM) 
#### 新增DNN组参数配置(ADD SBIDNNARRPARAM) 


功能说明 

该命令用于新增DNN组参数配置。当NF（PCF、BSF等）已配置可以服务的DNN组编号，需要新增归属于该DNN组编号的参数时，使用该命令。执行成功后，NF（PCF、BSF等）新增了可以服务的该范围组参数的DNN信息。 


注意事项 

需要保证该范围组参数归属的DNN组编号已经存在，该编号通过[SHOW SBIDNNARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 必选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




命令举例 


`
新增DNN组参数配置：配置索引为1，DNN组编号为2，数据网络标识为“1”。 
ADD SBIDNNARRPARAM:INDEX=1,ARRAYID=2,DNN="1"
` 


#### 修改DNN组参数配置(SET SBIDNNARRPARAM) 
#### 修改DNN组参数配置(SET SBIDNNARRPARAM) 


功能说明 

该命令用于修改DNN组参数配置。当NF（PCF、BSF等）已配置可以服务的DNN组编号，需要修改归属于该DNN组编号的参数时，使用该命令。执行成功后，NF（PCF、BSF等）修改了可以服务的该范围组参数的DNN信息。 


注意事项 

如果修改该范围组参数归属的DNN组编号，则需要保证该范围组编号已经存在，该编号通过[SHOW SBIDNNARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




命令举例 


`
修改DNN组参数配置：配置索引为1，DNN组编号为2，数据网络标识为“123”。 
SET SBIDNNARRPARAM:INDEX=1,ARRAYID=2,DNN="123"
` 


#### 删除DNN组参数配置(DEL SBIDNNARRPARAM) 
#### 删除DNN组参数配置(DEL SBIDNNARRPARAM) 


功能说明 

该命令用于新增DNN组参数配置。当NF（PCF、BSF等）已配置可以服务的DNN组编号，需要删除归属于该DNN组编号的参数时，使用该命令。执行成功后，NF（PCF、BSF等）删除了可以服务的该范围组参数的DNN信息。 


注意事项 

如果归属于某个DNN组编号的所有DNN组参数配置都已经删除，建议删除该DNN组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




命令举例 


`
删除DNN组参数配置：配置索引为1。
DEL SBIDNNARRPARAM:INDEX=1
` 


#### 查询DNN组参数配置(SHOW SBIDNNARRPARAM) 
#### 查询DNN组参数配置(SHOW SBIDNNARRPARAM) 


功能说明 

该命令用于查询DNN组参数配置。当需要查询已经配置的DNN组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有DNN组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组参数配置索引，该索引为DNN组参数配置的全局唯一索引。
ARRAYID|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIDNNARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置数据网络名称，由两部分组成：网络标识符：外部网络的标识符号，必选参数。运营商标识符：归属运营商的表示符号，可选参数。




命令举例 


`
查询DNN组参数配置：DNN组参数配置索引为1。
SHOW SBIDNNARRPARAM:INDEX=1

(No.12) : SHOW SBIDNNARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 DNN组编号 数据网络标识   
-------------------------------------------------
复制 修改 删除 1        65535     zhongguoyidong 
-------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:05:34 耗时: 0.651 秒

` 


## IPv4地址范围组配置 
## IPv4地址范围组配置 


背景知识 


本地NRF功能中，IPv4地址范围组配置用于配置一组IPv4地址范围，这一组地址范围以组编号的方式对外呈现。当BSF需要新增可以服务的IPv4地址范围时，使用该配置，并在BSF扩展信息配置中引用该组编号。BSF扩展信息配置可以通过[ADD SBIBSFINFO]命令完成。




功能说明 


本地NRF功能打开时，IPv4地址范围组是以一组数据配置呈现的，该组数据配置包括IPv4地址范围组编号配置和IPv4地址范围组参数配置，一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数配置引用。 

IPv4地址范围组配置应用于BSF扩展信息配置中，用于标识该BSF可以提供服务的IPv4地址范围。BSF扩展信息可以通过[SHOW SBIBSFINFO]命令查询。




子主题： 






### IPv4地址范围组编号配置 
### IPv4地址范围组编号配置 


背景知识 


本地NRF功能中，IPv4地址范围组配置用于配置一组IPv4地址范围，这一组地址范围以组编号的方式对外呈现。当BSF需要新增可以服务的IPv4地址范围时，使用该配置，并在BSF扩展信息配置中引用该组编号。BSF扩展信息配置可以通过[ADD SBIBSFINFO]命令完成。




功能说明 


IPv4地址范围组编号配置用于配置一个IPv4地址范围组，一个IPv4地址范围组包含了若干个IPv4地址范围组参数。 

当启用本地NRF功能时，如果BSF需要新增可以服务的IPv4地址范围列表，则需要配置IPv4地址范围组编号。配置后，最终呈现在本地NRF配置的BSF扩展信息的IPv4地址范围数组中。如果不配置，则说明该BSF可以为服务网络中的所有IPv4地址服务。BSF扩展信息可以通过[SHOW SBIBSFINFO]命令查询。




子主题： 






#### 新增IPv4地址范围组编号配置(ADD SBIIPV4ADDRRANGEARRID) 
#### 新增IPv4地址范围组编号配置(ADD SBIIPV4ADDRRANGEARRID) 


功能说明 

该命令用于新增IPv4地址范围组编号配置。当BSF需要新增可以服务的IPv4地址范围组时，使用该命令。执行成功后，可以在BSF扩展信息配置中关联该IPv4地址范围组编号。 

BSF扩展信息配置使用[ADD SBIBSFINFO]命令。


注意事项 

必须先配置该IPv4地址范围组编号，才能在BSF扩展信息配置中引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，该编号全局唯一。IPv4地址范围组编号被以下配置引用：BSF扩展信息配置：用于新增BSF可以服务的IPv4地址范围列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询。IPv4地址范围组参数配置：一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数引用。IPv4地址范围组参数配置可以使用SHOW SBIIPV4ADDRRANGEARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，该编号全局唯一。IPv4地址范围组编号被以下配置引用：BSF扩展信息配置：用于新增BSF可以服务的IPv4地址范围列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询。IPv4地址范围组参数配置：一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数引用。IPv4地址范围组参数配置可以使用SHOW SBIIPV4ADDRRANGEARRPARAM命令查询。




命令举例 


`
新增IPv4地址范围组编号配置：IPv4地址范围组编号为1。 
ADD SBIIPV4ADDRRANGEARRID:ARRAYID=1
` 


#### 删除IPv4地址范围组编号配置(DEL SBIIPV4ADDRRANGEARRID) 
#### 删除IPv4地址范围组编号配置(DEL SBIIPV4ADDRRANGEARRID) 


功能说明 

该命令用于删除IPv4地址范围组编号配置。当BSF不再关联该IPv4地址范围组编号时，可以使用该命令删除IPv4地址范围组编号配置。 


注意事项 

删除前需要把归属于该IPv4地址范围组编号的所有IPv4地址范围组参数配置删除。可以使用命令[SHOW SBIIPV4ADDRRANGEARRPARAM]指定IPv4地址范围组编号，查询归属于该IPv4地址范围组编号的所有IPv4地址范围组参数配置。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，该编号全局唯一。IPv4地址范围组编号被以下配置引用：BSF扩展信息配置：用于新增BSF可以服务的IPv4地址范围列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询。IPv4地址范围组参数配置：一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数引用。IPv4地址范围组参数配置可以使用SHOW SBIIPV4ADDRRANGEARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，该编号全局唯一。IPv4地址范围组编号被以下配置引用：BSF扩展信息配置：用于新增BSF可以服务的IPv4地址范围列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询。IPv4地址范围组参数配置：一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数引用。IPv4地址范围组参数配置可以使用SHOW SBIIPV4ADDRRANGEARRPARAM命令查询。




命令举例 


`
删除IPv4地址范围组编号配置：IPv4地址范围组编号为1。
DEL SBIIPV4ADDRRANGEARRID:ARRAYID=1
` 


#### 查询IPv4地址范围组编号配置(SHOW SBIIPV4ADDRRANGEARRID) 
#### 查询IPv4地址范围组编号配置(SHOW SBIIPV4ADDRRANGEARRID) 


功能说明 

该命令用于查询IPv4地址范围组编号配置。查询时，可以指定IPv4地址范围组编号，查询成功后，会回显对应的IPv4地址范围组编号信息；如果不指定IPv4地址范围组编号，则回显已经配置的所有IPv4地址范围组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，该编号全局唯一。IPv4地址范围组编号被以下配置引用：BSF扩展信息配置：用于新增BSF可以服务的IPv4地址范围列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询。IPv4地址范围组参数配置：一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数引用。IPv4地址范围组参数配置可以使用SHOW SBIIPV4ADDRRANGEARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，该编号全局唯一。IPv4地址范围组编号被以下配置引用：BSF扩展信息配置：用于新增BSF可以服务的IPv4地址范围列表。BSF扩展信息配置可以使用SHOW SBIBSFINFO命令查询。IPv4地址范围组参数配置：一个IPv4地址范围组编号可以被若干个IPv4地址范围组参数引用。IPv4地址范围组参数配置可以使用SHOW SBIIPV4ADDRRANGEARRPARAM命令查询。




命令举例 


`
查询IPv4地址范围组编号配置：IPv4地址范围组编号为1。
SHOW SBIIPV4ADDRRANGEARRID:ARRAYID=1

(No.13) : SHOW SBIIPV4ADDRRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IPv4地址范围组编号 
----------------------------------
复制 删除      1                  
----------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:06:00 耗时: 0.639 秒

` 


### IPv4地址范围组参数配置 
### IPv4地址范围组参数配置 


背景知识 


本地NRF功能中，IPv4地址范围组配置用于配置一组IPv4地址范围，这一组地址范围以组编号的方式对外呈现。当BSF需要新增可以服务的IPv4地址范围时，使用该配置，并在BSF扩展信息配置中引用该组编号。BSF扩展信息配置可以通过[ADD SBIBSFINFO]命令完成。




功能说明 


IPv4地址范围组参数配置用于配置IPv4地址范围组的具体信息，包括：IPv4的起始地址和结束地址。同时，会在“IPv4地址范围组编号”中配置该IPv4地址范围组参数归属于哪个IPv4地址范围组。 

当BSF需要新增可以提供服务的IPv4地址范围时，需要配置归属于该IPv4地址范围组的参数。配置完成后，在BSF中引用该IPv4地址范围组参数归属的IPv4地址范围组编号。如果不配置IPv4地址范围组参数，则无法配置具体的IPv4地址范围信息，已经配置的IPv4地址范围组编号只能是一个孤立配置。如果BSF引用了该IPv4地址范围组编号，那么在组装NFProfile时会失败。 




子主题： 






#### 新增IPv4地址范围组参数配置(ADD SBIIPV4ADDRRANGEARRPARAM) 
#### 新增IPv4地址范围组参数配置(ADD SBIIPV4ADDRRANGEARRPARAM) 


功能说明 

该命令用于新增IPv4地址范围组参数配置。当BSF已配置可以服务的IPv4地址范围组编号，需要新增归属于该IPv4地址范围组编号的参数时，使用该命令。执行成功后，BSF新增了可以服务的该范围组参数的IPv4地址信息。 


注意事项 

目前不支持检查参数START和END的大小关系。如果配置错误，则会导致在本地NRF匹配时失败，达不到预期的匹配效果。 

 
需要保证该组参数归属的IPv4地址范围组编号已经存在，该组编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 必选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 必选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




命令举例 


`
新增IPv4地址范围组参数配置：配置索引为1，IPv4地址范围组编号为1，起始IPv4地址为"1.2.3.4"，结束IPv4地址为"3.4.5.6"。 
ADD SBIIPV4ADDRRANGEARRPARAM:INDEX=1,ARRAYID=1,START="1.2.3.4",END="3.4.5.6"
` 


#### 修改IPv4地址范围组参数配置(SET SBIIPV4ADDRRANGEARRPARAM) 
#### 修改IPv4地址范围组参数配置(SET SBIIPV4ADDRRANGEARRPARAM) 


功能说明 

该命令用于修改IPv4地址范围组参数配置。当BSF已配置可以服务的IPv4地址范围组编号，需要修改归属于该IPv4地址范围组编号的参数时，使用该命令。执行成功后，BSF修改了可以服务的该范围组参数的IPv4地址信息。 


注意事项 

目前不支持检查参数START和END的大小关系。如果配置错误，则会导致在本地NRF匹配时失败，达不到预期的匹配效果。 

 
如果修改归属的组编号配置，需要保证该组编号已经存在，可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




命令举例 


`
修改IPv4地址范围组参数配置：配置索引为1，IPv4地址范围组编号为1，起始IPv4地址为"5.6.7.8"，结束IPv4地址为"9.1.2.3"。 
SET SBIIPV4ADDRRANGEARRPARAM:INDEX=1,ARRAYID=1,START="5.6.7.8",END="9.1.2.3"
` 


#### 删除IPv4地址范围组参数配置(DEL SBIIPV4ADDRRANGEARRPARAM) 
#### 删除IPv4地址范围组参数配置(DEL SBIIPV4ADDRRANGEARRPARAM) 


功能说明 

该命令用于新增IPv4地址范围组参数配置。当BSF已配置可以服务的IPv4地址范围组编号，需要删除归属于该IPv4地址范围组编号的参数时，使用该命令。执行成功后，BSF删除了可以服务的该范围组参数的IPv4地址信息。 


注意事项 

如果归属于某个IPv4地址范围组编号的所有IPv4地址范围组参数配置都已经删除，建议删除该IPv4地址范围组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




命令举例 


`
删除IPv4地址范围组参数配置：配置索引为1。
DEL SBIIPV4ADDRRANGEARRPARAM:INDEX=1
` 


#### 查询IPv4地址范围组参数配置(SHOW SBIIPV4ADDRRANGEARRPARAM) 
#### 查询IPv4地址范围组参数配置(SHOW SBIIPV4ADDRRANGEARRPARAM) 


功能说明 

该命令用于查询IPv4地址范围组参数配置。当需要查询已经配置的IPv4地址范围组参数信息时，使用该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv4地址范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4起始地址。为IPv4参数格式。
END|结束|参数可选性: 任选参数类型: 字符串|该参数用于设置IPv4结束地址。为IPv4参数格式。




命令举例 


`
查询IPv4地址范围组参数配置：配置索引为1。
SHOW SBIIPV4ADDRRANGEARRPARAM:INDEX=1

(No.14) : SHOW SBIIPV4ADDRRANGEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 IPv4地址范围组编号 起始    结束    
-----------------------------------------------------------
复制 修改 删除 1        768                1.2.3.4 2.3.4.5 
-----------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:06:15 耗时: 0.639 秒

` 


## IPv6前缀范围组配置 
## IPv6前缀范围组配置 


背景知识 


本地NRF功能中，该配置用于配置一组IPv6前缀范围，这一组IPv6前缀范围以组编号的方式对外呈现。当BSF需要新增可以服务的IPv6范围时，使用该配置，并在BSF扩展信息配置中引用该组编号。BSF扩展信息配置可以通过[ADD SBIBSFINFO]命令完成。




功能说明 


本地NRF功能打开时，IPv6前缀范围组是以一组数据配置呈现的，该组数据配置包括IPv6前缀范围组编号配置和IPv6前缀范围组参数配置，一个IPv6前缀范围组编号可以被若干个IPv6前缀范围组参数配置引用。 

IPv6前缀范围组配置应用于BSF扩展信息配置中，用于标识该BSF可以提供服务的IPv6地址范围。BSF扩展信息可以通过[SHOW SBIBSFINFO]命令查询。




子主题： 






### IPv6前缀范围组编号配置 
### IPv6前缀范围组编号配置 


背景知识 


本地NRF功能中，该配置用于配置一组IPv6前缀范围，这一组IPv6前缀范围以组编号的方式对外呈现。当BSF需要新增可以服务的IPv6范围时，使用该配置，并在BSF扩展信息配置中引用该组编号。BSF扩展信息配置可以通过[ADD SBIBSFINFO]命令完成。




功能说明 


IPv6前缀范围组编号配置用于配置一个IPv6前缀范围组，一个IPv6前缀范围组包含了若干个IPv6前缀范围组参数。 

当启用本地NRF功能时，如果BSF需要新增可以服务的IPv6地址范围列表，则需要配置IPv6前缀范围组编号。配置后，最终呈现在本地NRF配置的BSF扩展信息的IPv6前缀范围数组中。如果不配置，则说明该BSF可以为服务网络中的所有IPv6地址服务。BSF扩展信息可以通过[SHOW SBIBSFINFO]命令查询。




子主题： 






#### 新增IPv6前缀范围组编号配置(ADD SBIIPV6PREFIXRANGEARRID) 
#### 新增IPv6前缀范围组编号配置(ADD SBIIPV6PREFIXRANGEARRID) 


功能说明 

该命令用于新增IPv6前缀范围组编号配置。当BSF需要新增可以服务的IPv6前缀范围组时，使用该命令。执行成功后，可以在BSF扩展信息配置中关联该IPv6前缀范围组编号。 

BSF扩展信息配置使用[ADD SBIBSFINFO]命令。


注意事项 

必须先配置该IPv6前缀范围组编号，才能在IPv6前缀范围组参数配置和BSF扩展信息配置中引用。 


 
使用命令SHOW SBIIPV6PREFIXRANGEARRPARAM查询IPv6前缀范围组参数配置。 

 
使用命令SHOW SBIBSFINFO查询BSF扩展信息配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6前缀范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识配置的IPv6前缀范围信息归属于哪个IPv6前缀范围组。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识配置的IPv6前缀范围信息归属于哪个IPv6前缀范围组。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
新增IPv6前缀范围组编号配置：IPv6前缀范围组编号为1。 
ADD SBIIPV6PREFIXRANGEARRID:ARRAYID=1
` 


#### 删除IPv6前缀范围组编号配置(DEL SBIIPV6PREFIXRANGEARRID) 
#### 删除IPv6前缀范围组编号配置(DEL SBIIPV6PREFIXRANGEARRID) 


功能说明 

该命令用于删除IPv6前缀范围组编号配置。当BSF不再关联该IPv6前缀范围组编号时，可以使用该命令删除IPv6前缀范围组编号配置。 


注意事项 


 
删除前需要把归属于该IPv6前缀范围组编号的所有IPv6前缀范围组参数配置删除。可以使用命令SHOW SBIIPV6PREFIXRANGEARRPARAM指定IPv6前缀范围组编号，查询归属于该IPv6前缀范围组编号的所有IPv6前缀范围组参数配置。 

 
BSF扩展信息中引用该IPv6前缀范围组编号的配置设置为0。使用命令SHOW SBIBSFINFO查询BSF扩展信息配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6前缀范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识配置的IPv6前缀范围信息归属于哪个IPv6前缀范围组。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识配置的IPv6前缀范围信息归属于哪个IPv6前缀范围组。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
删除IPv6前缀范围组编号配置：IPv6前缀范围组编号为1。
DEL SBIIPV6PREFIXRANGEARRID:ARRAYID=1
` 


#### 查询IPv6前缀范围组编号配置(SHOW SBIIPV6PREFIXRANGEARRID) 
#### 查询IPv6前缀范围组编号配置(SHOW SBIIPV6PREFIXRANGEARRID) 


功能说明 

该命令用于查询IPv6前缀范围组编号配置。查询时，可以指定IPv6前缀范围组编号，查询成功后，会回显对应的IPv6前缀范围组编号信息；如果不指定IPv6前缀范围组编号，则回显已经配置的所有IPv6前缀范围组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识配置的IPv6前缀范围信息归属于哪个IPv6前缀范围组。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识配置的IPv6前缀范围信息归属于哪个IPv6前缀范围组。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
查询IPv6前缀范围组编号配置：IPv6前缀范围组编号为1。
SHOW SBIIPV6PREFIXRANGEARRID:ARRAYID=1

(No.15) : SHOW SBIIPV6PREFIXRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       IPv6前缀范围组编号 
----------------------------------
复制 删除      1                  
----------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:06:39 耗时: 0.63 秒

` 


### IPv6前缀范围组参数配置 
### IPv6前缀范围组参数配置 


背景知识 


本地NRF功能中，该配置用于配置一组IPv6前缀范围，这一组IPv6前缀范围以组编号的方式对外呈现。当BSF需要新增可以服务的IPv6范围时，使用该配置，并在BSF扩展信息配置中引用该组编号。BSF扩展信息配置可以通过[ADD SBIBSFINFO]命令完成。




功能说明 


IPv6前缀范围组参数配置用于配置IPv6前缀范围组的具体信息，包括：IPv6的起始前缀和结束前缀。同时，会在“IPv6前缀范围组编号”中配置该IPv6前缀范围组参数归属于哪个IPv6前缀范围组。 

当BSF需要新增可以提供服务的IPv6地址范围时，需要配置IPv6前缀范围组参数，该参数配置IPv6前缀范围信息以及归属的IPv6前缀范围组。配置完成后，在BSF中引用该IPv6前缀范围组参数归属的IPv6前缀范围组编号。如果不配置IPv6前缀范围组参数，则无法配置具体的IPv6前缀范围信息，已经配置的IPv6前缀范围组编号只能是一个孤立配置。如果BSF引用了该IPv6前缀范围组编号，那么在组装NFProfile时会失败。 




子主题： 






#### 新增IPv6前缀范围组参数配置(ADD SBIIPV6PREFIXRANGEARRPARAM) 
#### 新增IPv6前缀范围组参数配置(ADD SBIIPV6PREFIXRANGEARRPARAM) 


功能说明 

该命令用于新增IPv6前缀范围组参数配置。当BSF需要新增可以服务的IPv6前缀范围时，使用该命令配置IPv6前缀范围组参数，该参数配置IPv6前缀范围信息以及归属的IPv6前缀范围组。执行成功后，BSF新增了一个可以服务的IPv6地址范围信息。 


注意事项 

目前不支持检查参数START和END的大小关系。如果配置错误，则会导致在本地NRF匹配时失败，达不到预期的匹配效果。 

 
需要保证该组参数归属的IPv6前缀范围组编号已经存在，该组编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 必选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 必选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




命令举例 


`
新增IPv6前缀范围组参数配置：配置索引为666，IPv6前缀范围组编号为1，IPv6起始前缀为“1:2::/96”，IPv6结束前缀为“a::b/96”。 
ADD SBIIPV6PREFIXRANGEARRPARAM:INDEX=666,ARRAYID=1,START="1:2::/96",END="a::b/96"
` 


#### 修改IPv6前缀范围组参数配置(SET SBIIPV6PREFIXRANGEARRPARAM) 
#### 修改IPv6前缀范围组参数配置(SET SBIIPV6PREFIXRANGEARRPARAM) 


功能说明 

该命令用于修改IPv6前缀范围组参数配置。当BSF已配置可以服务的IPv6前缀范围组编号，需要修改归属于该IPv6前缀范围组编号的IPv6前缀范围信息时，使用该命令。执行成功后，BSF修改了一个可以服务的IPv6地址范围信息。 


注意事项 

目前不支持检查参数START和END的大小关系。如果配置错误，则会导致在本地NRF匹配时失败，达不到预期的匹配效果。 

 
如果修改归属的组编号配置，需要保证该组编号已经存在，可以通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




命令举例 


`
修改IPv6前缀范围组参数配置：配置索引为666，IPv6前缀范围组编号为1，IPv6起始前缀为“1:2::/96”，IPv6结束前缀为“a::c/96”。 
SET SBIIPV6PREFIXRANGEARRPARAM:INDEX=666,ARRAYID=1,START="1:2::/96",END="a::c/96"
` 


#### 删除IPv6前缀范围组参数配置(DEL SBIIPV6PREFIXRANGEARRPARAM) 
#### 删除IPv6前缀范围组参数配置(DEL SBIIPV6PREFIXRANGEARRPARAM) 


功能说明 

该命令用于删除IPv6前缀范围组参数配置。当BSF已配置可以服务的IPv6前缀范围组编号，需要删除归属于该IPv6前缀范围组编号的IPv6前缀范围信息时，使用该命令。执行成功后，BSF删除了一个可以服务的IPv6地址范围信息。 


注意事项 

如果归属于某个IPv6前缀范围组编号的所有IPv6前缀范围组参数配置都已经删除，建议删除该IPv6前缀范围组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




命令举例 


`
删除IPv6前缀范围组参数配置：配置索引为666。
DEL SBIIPV6PREFIXRANGEARRPARAM:INDEX=666
` 


#### 查询IPv6前缀范围组参数配置(SHOW SBIIPV6PREFIXRANGEARRPARAM) 
#### 查询IPv6前缀范围组参数配置(SHOW SBIIPV6PREFIXRANGEARRPARAM) 


功能说明 

该命令用于查询IPv6前缀范围组参数配置。当需要查询已经配置的IPv6前缀范围组参数信息时，使用该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。该参数无特殊配置原则。
ARRAYID|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IPv6前缀范围组编号，标识该范围组参数归属于哪个范围组编号。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
START|起始|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6起始前缀。为IPv6前缀格式。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 0-71|该参数用于设置IPv6结束前缀。为IPv6前缀格式。




命令举例 


`
查询IPv6前缀范围组参数配置：配置索引为666。
SHOW SBIIPV6PREFIXRANGEARRPARAM:INDEX=666

(No.4) : SHOW SBIIPV6PREFIXRANGEARRPARAM:INDEX=666
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 IPv6前缀范围组编号 起始     结束    
------------------------------------------------------------
复制 修改 删除 666      1                  1:2::/96 a::c/96 
------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-22 15:49:02 耗时: 0.627 秒

` 


## PLMN范围组配置 
## PLMN范围组配置 


背景知识 


PLMN（Public Land Mobile Network，公共陆地移动网) 范围用于标识一段公共陆地移动网区域，由移动国家码和移动网号组成。 

格式为：<MCC><MNC>。 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 

本地NRF功能中，该配置主要用于限定PLMN的范围，应用于PLMN范围组配置中，用于表示PLMN的范围。该配置以组编号的方式对外呈现，在CHF信息配置中引用该组编号，用于表示该NF可以服务的PLMN范围列表。 

其中，CHF信息配置通过[SHOW SBICHFINFO]命令查询。




功能说明 


本地NRF功能打开时，PLMN范围组是以一组数据配置呈现的，该组数据配置包括PLMN范围组编号配置和PLMN范围组参数配置，一个PLMN范围组编号可以被若干个PLMN范围组参数引用。 

当CHF需要新增该NF可以服务的PLMN范围列表时，使用该配置。 

CHF信息配置通过[SHOW SBICHFINFO]命令查询。




子主题： 






### PLMN范围组编号配置 
### PLMN范围组编号配置 


背景知识 


PLMN（Public Land Mobile Network，公共陆地移动网) 范围用于标识一段公共陆地移动网区域，由移动国家码和移动网号组成。 

格式为：<MCC><MNC>。 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 

本地NRF功能中，该配置主要用于限定PLMN的范围，应用于PLMN范围组配置中，用于表示PLMN的范围。该配置以组编号的方式对外呈现，在CHF信息配置中引用该组编号，用于表示该NF可以服务的PLMN范围列表。 

其中，CHF信息配置通过[SHOW SBICHFINFO]命令查询。




功能说明 


PLMN范围组编号配置用于配置一个PLMN范围组，一个PLMN范围组包含了若干个PLMN范围组参数。 

当启用本地NRF功能时，如果CHF需要新增该NF可以服务的PLMN范围列表，则需要配置PLMN范围范围组编号。配置后，最终呈现在本地NRF配置的CHF的PLMN范围数组中。如果没有配置，则说明该CHF可以服务于所有PLMN。 

CHF信息配置通过[SHOW SBICHFINFO]命令查询。




子主题： 






#### 新增PLMN范围组编号配置(ADD SBIPLMNRANGEARRID) 
#### 新增PLMN范围组编号配置(ADD SBIPLMNRANGEARRID) 


功能说明 

该命令用于新增PLMN范围组编号配置。当CHF需要新增限定可以服务的PLMN范围组时，使用该命令。执行成功后，可以在CHF信息配置中关联该PLMN范围组编号。 


注意事项 

必须先配置该PLMN范围组编号，才能在“PLMN范围组参数配置”及“CHF信息配置”中引用。 


 
使用命令SHOW SBIPLMNRANGEARRPARAM查询“PLMN范围组参数配置”。 

 
使用命令SHOW SBICHFINFO查询“CHF信息配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号，该编号是PLMN范围组编号配置的唯一标识。被“PLMN范围组参数配置”及“CHF信息配置”引用。“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询。“CHF信息配置”通过SHOW SBICHFINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号，该编号是PLMN范围组编号配置的唯一标识。被“PLMN范围组参数配置”及“CHF信息配置”引用。“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询。“CHF信息配置”通过SHOW SBICHFINFO命令查询。




命令举例 


`
新增PLMN范围组编号配置：PLMN范围组编号为1。
ADD SBIPLMNRANGEARRID:ARRAYID=1;
` 


#### 删除PLMN范围组编号配置(DEL SBIPLMNRANGEARRID) 
#### 删除PLMN范围组编号配置(DEL SBIPLMNRANGEARRID) 


功能说明 

该命令用于删除PLMN范围组编号配置。当CHF不再关联该PLMN范围组编号时，可以使用该命令删除PLMN范围组编号配置。 


注意事项 

如果要删除该PLMN范围组编号配置，需要先删除引用该配置的“PLMN范围组参数配置”，并在“CHF信息配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询，通过DEL SBIPLMNRANGEARRPARAM命令进行删除。 

 
“CHF信息配置”通过SHOW SBICHFINFO命令查询，通过SET SBICHFINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号，该编号是PLMN范围组编号配置的唯一标识。被“PLMN范围组参数配置”及“CHF信息配置”引用。“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询。“CHF信息配置”通过SHOW SBICHFINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号，该编号是PLMN范围组编号配置的唯一标识。被“PLMN范围组参数配置”及“CHF信息配置”引用。“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询。“CHF信息配置”通过SHOW SBICHFINFO命令查询。




命令举例 


`
删除PLMN范围组编号配置：PLMN范围组编号为1。
DEL SBIPLMNRANGEARRID:ARRAYID=1;
` 


#### 查询PLMN范围组编号配置(SHOW SBIPLMNRANGEARRID) 
#### 查询PLMN范围组编号配置(SHOW SBIPLMNRANGEARRID) 


功能说明 

该命令用于查询PLMN范围组编号配置。查询时，可以指定PLMN范围组编号，查询成功后，会回显对应的PLMN范围组编号信息；如果不指定PLMN范围组编号，则回显已经配置的所有PLMN范围组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号，该编号是PLMN范围组编号配置的唯一标识。被“PLMN范围组参数配置”及“CHF信息配置”引用。“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询。“CHF信息配置”通过SHOW SBICHFINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号，该编号是PLMN范围组编号配置的唯一标识。被“PLMN范围组参数配置”及“CHF信息配置”引用。“PLMN范围组参数配置”通过SHOW SBIPLMNRANGEARRPARAM命令查询。“CHF信息配置”通过SHOW SBICHFINFO命令查询。




命令举例 


`
查询PLMN范围组编号配置：PLMN范围组编号为1。
SHOW SBIPLMNRANGEARRID:ARRAYID=1

(No.1) : SHOW SBIPLMNRANGEARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PLMN范围组编号 
------------------------------
复制 删除      1              
------------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:50:40 耗时: 0.616 秒

` 


### PLMN范围组参数配置 
### PLMN范围组参数配置 


背景知识 


PLMN（Public Land Mobile Network，公共陆地移动网) 范围用于标识一段公共陆地移动网区域，由移动国家码和移动网号组成。 

格式为：<MCC><MNC>。 


 
MCC由3个十进制数组成，编码范围为十进制的000～999。 

 
MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。 

 

本地NRF功能中，该配置主要用于限定PLMN的范围，应用于PLMN范围组配置中，用于表示PLMN的范围。该配置以组编号的方式对外呈现，在CHF信息配置中引用该组编号，用于表示该NF可以服务的PLMN范围列表。 

其中，CHF信息配置通过[SHOW SBICHFINFO]命令查询。




功能说明 


PLMN范围组参数配置用于配置PLMN范围的具体信息。同时，会在“PLMN范围组编号”中配置该PLMN范围组参数归属于哪个PLMN范围组。 

当CHF需要新增该NF可以服务的PLMN范围列表时，需要配置PLMN范围组参数，该参数配置PLMN范围信息以及归属的PLMN范围组。配置完成后，在CHF中引用该PLMN范围组参数归属的PLMN范围组编号。如果不配置PLMN范围组参数，则无法配置具体的PLMN范围信息，已经配置的PLMN范围组编号只能是一个孤立配置。如果CHF引用了该PLMN范围组编号，那么在组装NFProfile时会失败。 

CHF信息配置通过[SHOW SBICHFINFO]命令查询。




子主题： 






#### 新增PLMN范围组参数配置(ADD SBIPLMNRANGEARRPARAM) 
#### 新增PLMN范围组参数配置(ADD SBIPLMNRANGEARRPARAM) 


功能说明 

该命令用于新增PLMN范围组参数配置。当CHF需要新增可以提供服务的PLMN范围时，使用该命令配置PLMN范围组参数，该参数配置PLMN范围信息以及归属的PLMN范围组。执行成功后，CHF新增了一个可以服务的PLMN范围信息。 


注意事项 

需要保证该范围组参数归属的PLMN范围组编号已经存在，该编号通过[SHOW SBIPLMNRANGEARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 必选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 必选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




命令举例 


`
新增PLMN范围组参数配置：配置索引为1，PLMN范围组编号为1，开始为"12300"，结束为"123999"。
ADD SBIPLMNRANGEARRPARAM:INDEX=1,ARRAYID=1,START="12300",END="123999";
` 


#### 修改PLMN范围组参数配置(SET SBIPLMNRANGEARRPARAM) 
#### 修改PLMN范围组参数配置(SET SBIPLMNRANGEARRPARAM) 


功能说明 

该命令用于修改PLMN范围组参数配置。当CHF已配置可以服务的PLMN范围组编号，需要修改归属于该PLMN范围组编号的PLMN范围信息时，使用该命令。执行成功后，CHF修改了一个可以服务的PLMN范围信息。 


注意事项 

如果修改该范围组参数归属的PLMN范围组编号，则需要保证该范围组编号已经存在，该编号通过[SHOW SBIPLMNRANGEARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




命令举例 


`
修改PLMN范围组参数配置：配置索引为1，PLMN范围组编号为1，开始为"12300"，结束为"123999"。
SET SBIPLMNRANGEARRPARAM:INDEX=1,ARRAYID=1,START="12300",END="123999";
` 


#### 删除PLMN范围组参数配置(DEL SBIPLMNRANGEARRPARAM) 
#### 删除PLMN范围组参数配置(DEL SBIPLMNRANGEARRPARAM) 


功能说明 

该命令用于删除PLMN范围组参数配置。当CHF已配置可以服务的PLMN范围组编号，需要删除归属于该PLMN范围组编号的PLMN范围信息时，使用该命令。执行成功后，CHF删除了一个可以服务的PLMN范围信息。 


注意事项 

如果归属于某个PLMN范围组编号的所有PLMN范围组参数配置都已经删除，建议删除该PLMN范围组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




命令举例 


`
删除PLMN范围组参数配置：配置索引为1。
DEL SBIPLMNRANGEARRPARAM:INDEX=1;
` 


#### 查询PLMN范围组参数配置(SHOW SBIPLMNRANGEARRPARAM) 
#### 查询PLMN范围组参数配置(SHOW SBIPLMNRANGEARRPARAM) 


功能说明 

该命令用于查询PLMN范围组参数配置。当需要查询已经配置的PLMN范围组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有PLMN范围组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是PLMN范围组参数配置的唯一标识。
ARRAYID|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PLMN范围组编号。标识配置的PLMN范围信息归属于哪个PLMN范围组。该编号通过SHOW SBIPLMNRANGEARRID命令查询。
START|开始|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围开始的第一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。
END|结束|参数可选性: 任选参数类型: 字符串参数范围: 5-6|该参数用于设置标识PLMN范围结束的最后一个值。 该字符串的编码格式：<MCC><MNC>。MCC由3个十进制数组成，编码范围为十进制的000～999。MNC由2个或3个十进制数组成，编码范围为十进制的00～99或000～999，目前，在我国取2个十进制组成。




命令举例 


`
查询PLMN范围组参数配置：配置索引为1。
SHOW SBIPLMNRANGEARRPARAM:INDEX=1

(No.1) : SHOW SBIPLMNRANGEARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 PLMN范围组编号 开始  结束   
----------------------------------------------------
复制 修改 删除 1        1              12300 123999 
----------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:53:16 耗时: 0.613 秒

` 


## API版本组配置 
## API版本组配置 


背景知识 


API版本表示应用程序接口对应的版本。 

本地NRF功能中，API版本组配置用于配置一组API版本，这一组版本以组编号的方式对外呈现。当缺省通知端点组配置需要新增缺省通知类型可以支持的API版本时，使用该配置。如果缺省通知端点组配置中没有配置API版本组，则不为缺省通知类型提供特定的API版本，缺省通知类型可以支持任何API版本。缺省通知端点组参数配置可以通过[ADD SBIDLFTNOTEENDPOINTARRPARAM]命令完成




功能说明 


本地NRF功能打开时，API版本组是以一组数据配置呈现的，该组数据配置包括API版本组编号配置和API版本组参数配置，一个API版本组编号可以被若干个API版本组参数引用。 

当缺省通知端点组配置需要新增缺省通知类型可以支持的API版本列表时，使用该配置。 




子主题： 






### API版本组编号配置 
### API版本组编号配置 


背景知识 


API版本表示应用程序接口对应的版本。 

本地NRF功能中，API版本组配置用于配置一组API版本，这一组版本以组编号的方式对外呈现。当缺省通知端点组配置需要新增缺省通知类型可以支持的API版本时，使用该配置。如果缺省通知端点组配置中没有配置API版本组，则不为缺省通知类型提供特定的API版本，缺省通知类型可以支持任何API版本。缺省通知端点组参数配置可以通过[ADD SBIDLFTNOTEENDPOINTARRPARAM]命令完成




功能说明 


API版本组编号配置用于配置一个API版本组，一个API版本组包含了若干个API版本组参数。 

当启用本地NRF功能时，如果缺省通知端点组配置需要新增缺省通知类型可以支持的API版本列表，则需要配置API版本范围组编号。配置后，最终呈现在本地NRF配置的缺省通知端点组配置的API版本数组中。如果不配置，则说明该缺省通知类型可以支持所有API版本。 




子主题： 






#### 新增API版本组编号配置(ADD SBIAPIVERSIONARRID) 
#### 新增API版本组编号配置(ADD SBIAPIVERSIONARRID) 


功能说明 

该命令用于新增API版本组编号配置。当缺省通知端点组配置需要新增限定默认通知类型所支持的API版本组时，使用该命令。执行成功后，可以在缺省通知端点组配置中关联该API版本组编号。 


注意事项 

必须先配置该API版本组编号，才能在“API版本组参数配置”及“缺省通知端点组参数配置”中引用。 


 
使用命令SHOW SBIAPIVERSIONARRPARAM查询“API版本组参数配置”。 

 
使用命令SHOW SBIDLFTNOTEENDPOINTARRPARAM查询“缺省通知端点组参数配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|API版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，该编号是API版本组编号配置的唯一标识。被“API版本组参数配置”及“缺省通知端点组参数配置”引用。“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，该编号是API版本组编号配置的唯一标识。被“API版本组参数配置”及“缺省通知端点组参数配置”引用。“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。




命令举例 


`
新增API版本组编号配置：API版本组编号为1。
ADD SBIAPIVERSIONARRID:ARRAYID=1;
` 


#### 删除API版本组编号配置(DEL SBIAPIVERSIONARRID) 
#### 删除API版本组编号配置(DEL SBIAPIVERSIONARRID) 


功能说明 

该命令用于删除API版本组编号配置。当缺省通知端点组配置不再关联该API版本组编号时，可以使用该命令删除API版本组编号配置。 


注意事项 

如果要删除该API版本组编号配置，需要先删除引用该配置的“API版本组参数配置”，并在“缺省通知端点组参数配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询，通过DEL SBIAPIVERSIONARRPARAM命令进行删除。 

 
“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询，通过SET SBIDLFTNOTEENDPOINTARRPARAM命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|API版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，该编号是API版本组编号配置的唯一标识。被“API版本组参数配置”及“缺省通知端点组参数配置”引用。“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，该编号是API版本组编号配置的唯一标识。被“API版本组参数配置”及“缺省通知端点组参数配置”引用。“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。




命令举例 


`
删除API版本组编号配置：API版本组编号为1。
DEL SBIAPIVERSIONARRID:ARRAYID=1;
` 


#### 查询API版本组编号配置(SHOW SBIAPIVERSIONARRID) 
#### 查询API版本组编号配置(SHOW SBIAPIVERSIONARRID) 


功能说明 

该命令用于查询API版本组编号配置。查询时，可以指定API版本组编号，查询成功后，会回显对应的API版本组编号信息；如果不指定API版本组编号，则回显已经配置的所有API版本组编号信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，该编号是API版本组编号配置的唯一标识。被“API版本组参数配置”及“缺省通知端点组参数配置”引用。“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，该编号是API版本组编号配置的唯一标识。被“API版本组参数配置”及“缺省通知端点组参数配置”引用。“API版本组参数配置”通过SHOW SBIAPIVERSIONARRPARAM命令查询。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。




命令举例 


`
查询API版本组编号配置：API版本组编号为1。
SHOW SBIAPIVERSIONARRID:ARRAYID=1

(No.1) : SHOW SBIAPIVERSIONARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       API版本组编号 
-----------------------------
复制 删除      1             
-----------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:55:41 耗时: 0.626 秒

` 


### API版本组参数配置 
### API版本组参数配置 


背景知识 


API版本表示应用程序接口对应的版本。 

本地NRF功能中，API版本组配置用于配置一组API版本，这一组版本以组编号的方式对外呈现。当缺省通知端点组配置需要新增缺省通知类型可以支持的API版本时，使用该配置。如果缺省通知端点组配置中没有配置API版本组，则不为缺省通知类型提供特定的API版本，缺省通知类型可以支持任何API版本。缺省通知端点组参数配置可以通过[ADD SBIDLFTNOTEENDPOINTARRPARAM]命令完成




功能说明 


API版本组参数配置用于配置API版本的具体信息。同时，会在“API版本组编号”中配置该API版本组参数归属于哪个API版本组。 

当缺省通知端点组配置需要新增缺省通知类型可以支持的API版本列表时，需要配置API版本组参数，该参数配置API版本信息以及归属的API版本组。配置完成后，在缺省通知端点组配置中引用该API版本组参数归属的API版本组编号。如果不配置API版本组参数，则无法配置具体的API版本信息，已经配置的API版本组编号只能是一个孤立配置。如果缺省通知端点组配置引用了该API版本组编号，那么在组装NFProfile时会失败。 




子主题： 






#### 新增API版本组参数配置(ADD SBIAPIVERSIONARRPARAM) 
#### 新增API版本组参数配置(ADD SBIAPIVERSIONARRPARAM) 


功能说明 

该命令用于新增API版本组参数配置。当缺省通知端点组参数配置需要新增可以提供服务的API版本时，使用该命令配置API版本组参数，该参数配置API版本信息以及归属的API版本组。执行成功后，缺省通知端点组参数配置新增了一个可以服务的API版本信息。 


注意事项 

需要保证该范围组参数归属的API版本组编号已经存在，该编号通过[SHOW SBIAPIVERSIONARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 必选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 任选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




命令举例 


`
新增API版本组参数配置：配置索引为1，API版本组编号为1，版本为"v1"。
ADD SBIAPIVERSIONARRPARAM:INDEX=1,ARRAYID=1,VERSION="v1";
` 


#### 修改API版本组参数配置(SET SBIAPIVERSIONARRPARAM) 
#### 修改API版本组参数配置(SET SBIAPIVERSIONARRPARAM) 


功能说明 

该命令用于修改API版本组参数配置。当缺省通知端点组参数配置已配置可以服务的API版本组编号，需要修改归属于该API版本组编号的API版本信息时，使用该命令。执行成功后，缺省通知端点组参数配置修改了一个可以服务的API版本信息。 


注意事项 

如果修改该组参数归属的API版本组编号，则需要保证该API版本组编号已经存在，该编号通过[SHOW SBIAPIVERSIONARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 任选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 任选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




命令举例 


`
修改API版本组参数配置：配置索引为1，API版本组编号为1，版本为"v1"。
SET SBIAPIVERSIONARRPARAM:INDEX=1,ARRAYID=1,VERSION="v1";
` 


#### 删除API版本组参数配置(DEL SBIAPIVERSIONARRPARAM) 
#### 删除API版本组参数配置(DEL SBIAPIVERSIONARRPARAM) 


功能说明 

该命令用于删除API版本组参数配置。当缺省通知端点组参数配置已配置可以服务的API版本组编号，需要删除归属于该API版本组编号的API版本信息时，使用该命令。执行成功后，缺省通知端点组参数配置删除了一个可以服务的API版本信息。 


注意事项 

如果归属于某个API版本组编号的所有API版本组参数配置都已经删除，建议删除该API版本组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 任选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




命令举例 


`
删除API版本组参数配置：配置索引为1。
DEL SBIAPIVERSIONARRPARAM:INDEX=1;
` 


#### 查询API版本组参数配置(SHOW SBIAPIVERSIONARRPARAM) 
#### 查询API版本组参数配置(SHOW SBIAPIVERSIONARRPARAM) 


功能说明 

该命令用于查询API版本组参数配置。当需要查询已经配置的API版本组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有API版本组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 任选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是API版本组参数配置的唯一标识。
ARRAYID|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置API版本组编号，标识该API版本组参数归属于哪个API版本组编号。该编号通过SHOW SBIAPIVERSIONARRID命令查询。
VERSION|版本|参数可选性: 任选参数类型: 字符串参数范围: 1-7|该参数用于设置默认通知类型支持的API版本。




命令举例 


`
查询API版本组参数配置：配置索引为1。
SHOW SBIAPIVERSIONARRPARAM:INDEX=1

(No.1) : SHOW SBIAPIVERSIONARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 API版本组编号 版本 
-------------------------------------------
复制 修改 删除 1        1             v1   
-------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 13:58:54 耗时: 0.608 秒

` 


## 缺省通知端点组配置 
## 缺省通知端点组配置 


背景知识 


本地NRF功能中，缺省通知端点组配置用于配置一组可回调URI的通知类型的通知端点。通常服务使用者（本端）向服务提供者（对端）订阅时，会显式地在请求中携带回调URI，对端在需要发送通知时，通过该回调URI将通知消息发往本端。当本端在订阅时，未在请求中显式地携带回调URI，那么对端在需要发送通知时，可以使用本配置的缺省回调URI将通知消息发往本端。此时如果对端NF中没有配置缺省通知端点组，则可能导致对应业务流程失败。 




功能说明 


本地NRF功能打开时，缺省通知端点组是以一组数据配置呈现的，该组数据配置包括缺省通知端点组编号配置和缺省通知端点组参数配置，一个缺省通知端点组编号可以被若干个缺省通知端点组参数引用。 

当服务使用者（本端）在订阅时，未在请求中显式地携带回调URI，那么服务提供者（对端）在需要发送通知时，可以使用缺省回调URI将通知消息发往本端，因此需要使用该配置增加对端NF支持的缺省通知端点组。 




子主题： 






### 缺省通知端点组编号配置 
### 缺省通知端点组编号配置 


背景知识 


本地NRF功能中，缺省通知端点组配置用于配置一组可回调URI的通知类型的通知端点。通常服务使用者（本端）向服务提供者（对端）订阅时，会显式地在请求中携带回调URI，对端在需要发送通知时，通过该回调URI将通知消息发往本端。当本端在订阅时，未在请求中显式地携带回调URI，那么对端在需要发送通知时，可以使用本配置的缺省回调URI将通知消息发往本端。此时如果对端NF中没有配置缺省通知端点组，则可能导致对应业务流程失败。 




功能说明 


缺省通知端点组编号配置用于配置一个缺省通知端点组，一个缺省通知端点组包含了若干个缺省通知端点组参数。 

当启用本地NRF功能时，如果当本端在订阅时，未在请求中显式地携带回调URI，那么对端在需要发送通知时，若要使用本配置的缺省回调URI将通知消息发往本端，则需要
新增可以支持的缺省通知端点组，并且需要配置缺省通知端点范围组编号。配置后，最终呈现在本地NRF配置的对端NF的缺省通知端点数组中。 




子主题： 






#### 新增缺省通知端点组编号配置(ADD SBIDLFTNOTEENDPOINTARRID) 
#### 新增缺省通知端点组编号配置(ADD SBIDLFTNOTEENDPOINTARRID) 


功能说明 

该命令用于新增缺省通知端点组编号配置。当需要新增对端NF支持的缺省通知端点组时，使用该命令。执行成功后，可以在缺省通知端点组参数配置、对端NF基本信息配置和对端NF服务实例配置中关联该缺省通知端点组编号。 


注意事项 

必须先配置该缺省通知端点组编号，才能在“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”中引用。 


 
使用命令SHOW SBIDLFTNOTEENDPOINTARRPARAM查询“缺省通知端点组参数配置”。 

 
使用命令SHOW SBIPEERNFBASEINFO查询“对端NF基本信息配置”。 

 
使用命令SHOW SBIPEERNFSERVICEINSTANCE查询“对端N服务实例配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|缺省通知端点组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，该编号是缺省通知端点组编号配置的唯一标识。被“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，该编号是缺省通知端点组编号配置的唯一标识。被“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




命令举例 


`
新增缺省通知端点组编号配置：缺省通知端点组编号为1。
ADD SBIDLFTNOTEENDPOINTARRID:ARRAYID=1;
` 


#### 删除缺省通知端点组编号配置(DEL SBIDLFTNOTEENDPOINTARRID) 
#### 删除缺省通知端点组编号配置(DEL SBIDLFTNOTEENDPOINTARRID) 


功能说明 

该命令用于删除缺省通知端点组编号配置。当缺省通知端点组配置不再关联该缺省通知端点组编号时，可以使用该命令删除缺省通知端点组编号配置。 


注意事项 

如果要删除该缺省通知端点组配置，需要先删除引用该配置的“缺省通知端点组参数配置”，并在“对端NF基本信息配置”及“对端NF服务实例配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询，通过DEL SBIPLMNIDARRPARAM命令进行删除。 

 
“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询，通过SET SBIPEERNFBASEINFO命令进行设置。 

 
“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询，通过SET SBIPEERNFSERVICEINSTANCE命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|缺省通知端点组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，该编号是缺省通知端点组编号配置的唯一标识。被“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，该编号是缺省通知端点组编号配置的唯一标识。被“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




命令举例 


`
删除缺省通知端点组编号配置：缺省通知端点组编号为1。
DEL SBIDLFTNOTEENDPOINTARRID:ARRAYID=1;
` 


#### 查询缺省通知端点组编号配置(SHOW SBIDLFTNOTEENDPOINTARRID) 
#### 查询缺省通知端点组编号配置(SHOW SBIDLFTNOTEENDPOINTARRID) 


功能说明 

该命令用于查询缺省通知端点组编号配置。查询时，可以指定缺省通知端点组编号，查询成功后，会回显对应的缺省通知端点组编号信息；如果不指定缺省通知端点组编号，则回显已经配置的所有缺省通知端点组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，该编号是缺省通知端点组编号配置的唯一标识。被“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，该编号是缺省通知端点组编号配置的唯一标识。被“缺省通知端点组参数配置”、“对端NF基本信息配置”及“对端NF服务实例配置”引用。“缺省通知端点组参数配置”通过SHOW SBIDLFTNOTEENDPOINTARRPARAM命令查询。“对端NF基本信息配置”通过SHOW SBIPEERNFBASEINFO命令查询。“对端NF服务实例配置”通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




命令举例 


`
查询缺省通知端点组编号配置：缺省通知端点组编号为1。
SHOW SBIDLFTNOTEENDPOINTARRID:ARRAYID=1

(No.1) : SHOW SBIDLFTNOTEENDPOINTARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       缺省通知端点组编号 
----------------------------------
复制 删除      1                  
----------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:01:37 耗时: 0.658 秒

` 


### 缺省通知端点组参数配置 
### 缺省通知端点组参数配置 


背景知识 


本地NRF功能中，缺省通知端点组配置用于配置一组可回调URI的通知类型的通知端点。通常服务使用者（本端）向服务提供者（对端）订阅时，会显式地在请求中携带回调URI，对端在需要发送通知时，通过该回调URI将通知消息发往本端。当本端在订阅时，未在请求中显式地携带回调URI，那么对端在需要发送通知时，可以使用本配置的缺省回调URI将通知消息发往本端。此时如果对端NF中没有配置缺省通知端点组，则可能导致对应业务流程失败。 




功能说明 


缺省通知端点组参数配置用于配置缺省通知端点的具体信息。同时，会在“缺省通知端点组编号”中配置该缺省通知端点组参数归属于哪个缺省通知端点组。 

当对端NF需要新增可以支持的缺省通知端点组时，需要配置缺省通知端点组参数，该参数配置缺省通知端点信息以及归属的缺省通知端点组。配置完成后，在对端NF中引用该缺省通知端点组参数归属的缺省通知端点组编号。如果不配置缺省通知端点组参数，则无法配置具体的缺省通知端点信息，已经配置的缺省通知端点组编号只能是一个孤立配置。如果对端NF引用了该缺省通知端点组编号，那么在组装NFProfile时会失败。 




子主题： 






#### 新增缺省通知端点组参数配置(ADD SBIDLFTNOTEENDPOINTARRPARAM) 
#### 新增缺省通知端点组参数配置(ADD SBIDLFTNOTEENDPOINTARRPARAM) 


功能说明 

该命令用于新增缺省通知端点组参数配置。当服务使用者（本端）在订阅时，未在请求中显式地携带回调URI，那么服务提供者（对端）在需要发送通知时，需要使用缺省回调URI将通知消息发往本端，可以使用该命令新增缺省通知端点组参数，该参数配置缺省通知端点信息以及归属的缺省通知端点组。执行成功后，对端NF新增了一个可以支持的缺省通知端点信息。 


注意事项 


 
需要保证该组参数归属的缺省通知端点组编号已经存在，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。 

 
需要保证关联的API版本组编号已经存在，该编号通过SHOW SBIAPIVERSIONARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 必选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




命令举例 


`
新增缺省通知端点组参数配置：配置索引为1，缺省通知端点组编号为1，通知类型为"N1_MESSAGES"，URI为"zte.com.cn"，N1消息类型为"5GMM"，N2信息类型为"SM"，API版本组编号为1。
ADD SBIDLFTNOTEENDPOINTARRPARAM:INDEX=1,ARRAYID=1,NOTIFICATIONTYPE="N1_MESSAGES",CALLBACKURI="zte.com.cn",N1MSGETYPE="5GMM",N2INFOTYPE="SM",VERSIONARRAY=1;
` 


#### 修改缺省通知端点组参数配置(SET SBIDLFTNOTEENDPOINTARRPARAM) 
#### 修改缺省通知端点组参数配置(SET SBIDLFTNOTEENDPOINTARRPARAM) 


功能说明 

该命令用于修改缺省通知端点组参数配置。当对端NF已配置可以支持的缺省通知端点组编号，需要修改归属于该缺省通知端点组编号的缺省通知端点信息时，使用该命令。执行成功后，对端NF修改了一个可以支持的缺省通知端点信息。 


注意事项 


 
如果修改该组参数归属的缺省通知端点组编号，则需要保证该组编号已经存在，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。 

 
如果修改关联的API版本组编号，则需要保证该编号已经存在，该编号通过SHOW SBIAPIVERSIONARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




命令举例 


`
修改缺省通知端点组参数配置：配置索引为1，缺省通知端点组编号为1，通知类型为"N1_MESSAGES"，URI为"zte.com.cn"，N1消息类型为"5GMM"，N2信息类型为"SM"，API版本组编号为1。
SET  SBIDLFTNOTEENDPOINTARRPARAM:INDEX=1,ARRAYID=1,NOTIFICATIONTYPE="N1_MESSAGES",CALLBACKURI="zte.com.cn",N1MSGETYPE="5GMM",N2INFOTYPE="SM",VERSIONARRAY=1;
` 


#### 删除缺省通知端点组参数配置(DEL SBIDLFTNOTEENDPOINTARRPARAM) 
#### 删除缺省通知端点组参数配置(DEL SBIDLFTNOTEENDPOINTARRPARAM) 


功能说明 

该命令用于删除缺省通知端点组参数配置。当对端NF已配置可以支持的缺省通知端点组编号，需要删除归属于该缺省通知端点组编号的缺省通知端点信息时，使用该命令。执行成功后，对端NF删除了一个可以支持的缺省通知端点信息。 


注意事项 

如果归属于某个缺省通知端点组编号的所有缺省通知端点组参数配置都已经删除，建议删除该缺省通知端点组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




命令举例 


`
删除缺省通知端点组参数配置：配置索引为1。
DEL SBIDLFTNOTEENDPOINTARRPARAM:INDEX=1;
` 


#### 查询缺省通知端点组参数配置(SHOW SBIDLFTNOTEENDPOINTARRPARAM) 
#### 查询缺省通知端点组参数配置(SHOW SBIDLFTNOTEENDPOINTARRPARAM) 


功能说明 

该命令用于查询缺省通知端点组参数配置。当需要查询已经配置的缺省通知端点组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有缺省通知端点组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是缺省通知端点组参数配置的唯一标识。
ARRAYID|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置缺省通知端点组编号，标识该缺省通知端点组参数归属于哪个缺省通知端点组编号。该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
NOTIFICATIONTYPE|通知类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置提供相应的回调URI的通知类型。各参数选项的含义是：N1_MESSAGES（N1消息）：通知类型为N1消息。选择该场景下，与UE之间交互的为N1消息，即通知消息中包含的为UE的消息。N2_INFORMATION（N2信息）：通知类型为N2信息。选择该场景下，与RAN之间交互的为N2信息，即通知信息中包含的为RAN的信息。LOCATION_NOTIFICATION（位置信息通知）：通知类型为位置信息。选择该场景下，AMF向NF服务使用者（例如GMLC）通知位置信息。DATA_REMOVAL_NOTIFICATION（数据删除通知）：通知类型为通过UDR通知数据删除。选择该场景下，可以在撤消订阅后删除UE注册数据。DATA_CHANGE_NOTIFICATION（数据更改通知）：通知类型为通过UDR通知数据更改。选择该场景下，可以在用户签约数据变更时触发此通知。LOCATION_UPDATE_NOTIFICATION（位置更新通知）：通知类型为位置信息更新。选择该场景下，在MO_LR程序期间，GMLC向NF服务使用者（例如NEF）通知UE位置信息更新。
CALLBACKURI|URI|参数可选性: 任选参数类型: 字符串参数范围: 0-255|该参数用于设置回调URI，该参数包含默认通知端点，服务提供者将使用该默认通知端点，来向尚未在服务提供者中显式注册回调URI的服务使用者发送通知（例如，作为隐式订阅的结果）。
N1MSGETYPE|N1消息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N1消息类型，如果通知类型为N1_MESSAGES，则该参数将存在并标识要通知的N1消息的类别。各参数选项的含义是：INVALID（无效的）：支持N1消息类型为无效的。5GMM（5GS Mobility Management，移动性管理消息）：支持N1消息类型为5GMM。SM（Session Management，会话管理）：支持N1消息类型为SM。LPP（LTE Positioning Protocol，LTE定位协议）：支持N1消息类型为LPP。SMS（Short Message Service，短消息业务）：支持N1消息类型为SMS。UPDP（UE Policy Delivery，UE策略投递）：支持N1消息类型为UPDP。LCS（Location Services，定位业务）：支持N1消息类型为LCS。
N2INFOTYPE|N2信息类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置N2信息类型，如果通知类型为N2_INFORMATION，则该参数将存在并标识要通知的N2信息的类别。各参数选项的含义是：INVALID（无效的）：支持N2信息类型为无效的。SM（Session Management,会话管理）：支持N2信息类型为SM。NRPPa（NR Positioning Protocol Annex，NR定位协议A）：支持N2信息类型为NRPPa。PWS（Public Warning System，公共预警系统）：支持N2信息类型为PWS。PWS-BCAL（Broadcast Completed Area List or the Broadcast Cancelled Area List，广播完成区域列表和广播取消区域列表）：支持N2信息类型为PWS-BCAL。PWS-RF（Restart Indication or Failure Indication，重启或故障指示）：支持N2信息类型为PWS-RF。RAN（Radio Access Network，无线接入网）：支持N2信息类型为RAN。
VERSIONARRAY|API版本组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置API版本组编号，可以通过该编号获取到API版本信息。该编号通过SHOW SBIAPIVERSIONARRID命令查询。




命令举例 


`
查询缺省通知端点组参数配置：配置索引为1。
SHOW SBIDLFTNOTEENDPOINTARRPARAM:INDEX=1

(No.1) : SHOW SBIDLFTNOTEENDPOINTARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 缺省通知端点组编号 通知类型    URI        N1消息类型 N2信息类型 API版本组编号 
------------------------------------------------------------------------------------------------------
复制 修改 删除 1        1                  N1_MESSAGES zte.com.cn 5GMM       SM         1             
------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:03:07 耗时: 0.602 秒

` 


# 对端NF配置 
# 对端NF配置 


背景知识 


本地NRF功能需要配置出服务提供者（对端）的完整NFProfile，NFProfile中包含了基本信息参数、与特定NF类型有关的NF扩展信息参数以及服务实例参数。对端NF配置包含了与上述所有参数对应的一系列配置。 




功能说明 


该组命令用于配置对端NFProfile包含的NF基本信息、NF扩展信息和NF服务实例。当启用本地NRF功能时，需要配置该组命令。如果不配置该组命令，则无法生成对端NFProfile，导致服务使用者从本地NRF配置信息中发现服务提供者失败，从而导致发现流程失败。 




子主题： 






## 对端NF基本信息配置 
## 对端NF基本信息配置 


背景知识 


在5GC的实际使用中，存在服务使用者（本端）无法通过NRF发现服务提供者（对端）的场景，此时服务使用者通过本地NRF配置可以发现服务提供者。 

当服务提供者（对端）将其NF信息向NRF注册时，注册请求中携带对端NFProfile参数，该参数包含通用基本信息、扩展信息和服务实例的参数。 

当服务使用者（本端）通过本地NRF配置发现可用的服务提供者（对端），NRF可以用服务发现请求中的发现参数与对端NFProfile包含的基本信息进行匹配，并将匹配结果以服务发现结构的形式返回给服务者使用者。如果能匹配成功，则认为发现服务提供者成功，并且在发现响应中携带该NFProfile。服务使用者根据服务发现结果选择服务提供者或访问服务。 

当本端启用本地NRF功能时，基本信息配置会呈现在对端NFProfile的基本信息参数中。 




功能说明 


对端NF基本信息配置即对应本地NRF配置的对端NFProfile的基本信息参数。当启用本地NRF功能时，需要配置该组命令。如果不配置该组命令，则NFProfile不能携带NF基本信息，当服务使用者从本地NRF配置信息中发现服务提供者时，无法根据NF基本信息中的参数进行匹配，可能导致发现失败。 




子主题： 






### 新增对端NF基本信息配置(ADD SBIPEERNFBASEINFO) 
### 新增对端NF基本信息配置(ADD SBIPEERNFBASEINFO) 


功能说明 

该命令用于新增对端NF基本信息配置。当本地NRF配置中所配置的对端NFProfile需要携带基本信息字段时，使用该命令。命令执行成功后，本地NRF配置中会新增一个对端NFProfile及其基本信息字段。该配置中的“对端NF基本信息编号”可以被对端NF扩展信息配置及对端NF服务实例配置引用。 

对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。对端NF服务实例配置通过[SHOW SBIPEERNFSERVICEINSTANCE]命令查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFINSTANCEID|NF实例标识|参数可选性: 必选参数类型: 字符串参数范围: 0-63|该参数用于设置NF实例的唯一标识。必须全局范围内唯一。
NFTYPE|NF类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-127|该参数用于设置NF类型。
NFSTATUS|NF状态|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFINSTANCEID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置NF实例的唯一标识。必须全局范围内唯一。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-127|该参数用于设置NF类型。
NFSTATUS|NF状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




命令举例 


`
新增对端NF基本信息配置：对端NF信息编号为1，NF实例标识为"aaa00a00-0a00-000a-a0a0-00aa00a00aa0"， NF类型为"NRF_TYPE"，NF状态为"REGISTERED"，NF实例名称为"abc"，PLMN ID组编号为1，PLMN NID组编号为1，S-NSSAI组编号为1，PLMN S-NSSAI组编号为1，NSI组编号为1，域名为"zte.com.cn"，PLMN间域名为"plmn.com.cn"，IPv4地址组编号为1，IPv6地址组编号为1，允许的PLMN ID组编号为2，允许的PLMN NID组编号为2，允许的NF类型组编号为2，允许的域组编号为2，允许的S-NSSAI组编号为2，容量为10，优先级为1，地区为"NJ"，NF集标识编号为1，资源在NF服务实例间共享为"是"，是否支持基于LCI头域的负载控制为"是"，是否支持基于OCI头域的过载控制为"是"，缺省通知端点组编号为1，服务范围组编号为1。
ADD SBIPEERNFBASEINFO:ID=1,NFINSTANCEID="aaa00a00-0a00-000a-a0a0-00aa00a00aa0",NFTYPE="NRF_TYPE",NFSTATUS="REGISTERED",NFINSTANCENAME="abc",PLMNLARRAY=1,PLMNNIDARRAY=1,SNSSAIARRAY=1,PLMNSNSSAIARRAY=1,NSIARRAY=1,FQDN="zte.com.cn",INTERPLMNFQDN="plmn.com.cn",IPV4ARRAY=1,IPV6ARRAY=1,ALLOWPLMN=2,ALLOWPLMNNID=2,ALLOWNFTYPE=2,ALLOWNDOMAIN=2,ALLOWSNSSAI=2,CAPACITY=10,PRIORITY=1,LOCALITY="NJ",NFSETIDARRAY=1,NFSERVPERSISTENCE="YES",LCHSUPPORTIND="YES",OLCHSUPPORTIND="YES",DLFTNOTIFICATIONARR=1,SERVSCOPEARRAY=1;
` 


### 修改对端NF基本信息配置(SET SBIPEERNFBASEINFO) 
### 修改对端NF基本信息配置(SET SBIPEERNFBASEINFO) 


功能说明 

该命令用于修改对端NF基本信息配置。当本地NRF配置中所配置的对端NFProfile中的基本信息字段需要修改时，使用该命令。命令执行成功后，修改后的基本信息字段会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFSTATUS|NF状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFINSTANCEID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置NF实例的唯一标识。必须全局范围内唯一。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-127|该参数用于设置NF类型。
NFSTATUS|NF状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




命令举例 


`
修改对端NF基本信息配置：对端NF信息编号为1，NF状态为"REGISTERED"，NF实例名称为"abc"，PLMN ID组编号为1，PLMN NID组编号为1，S-NSSAI组编号为1，PLMN S-NSSAI组编号为1，NSI组编号为1，域名为"zte.com.cn"，PLMN间域名为"plmn.com.cn"，IPv4地址组编号为1，IPv6地址组编号为1，允许的PLMN ID组编号为2，允许的PLMN NID组编号为2，允许的NF类型组编号为2，允许的域组编号为2，允许的S-NSSAI组编号为2，容量为10，优先级为1，地区为"NJ"，NF集标识编号为1，资源在NF服务实例间共享为"是"，是否支持基于LCI头域的负载控制为"是"，是否支持基于OCI头域的过载控制为"是"，缺省通知端点组编号为1，服务范围组编号为1。
SET SBIPEERNFBASEINFO:ID=1,NFSTATUS="REGISTERED",NFINSTANCENAME="abc",PLMNLARRAY=1,PLMNNIDARRAY=1,SNSSAIARRAY=1,PLMNSNSSAIARRAY=1,NSIARRAY=1,FQDN="zte.com.cn",INTERPLMNFQDN="plmn.com.cn",IPV4ARRAY=1,IPV6ARRAY=1,ALLOWPLMN=2,ALLOWPLMNNID=2,ALLOWNFTYPE=2,ALLOWNDOMAIN=2,ALLOWSNSSAI=2,CAPACITY=10,PRIORITY=1,LOCALITY="NJ",NFSETIDARRAY=1,NFSERVPERSISTENCE="YES",LCHSUPPORTIND="YES",OLCHSUPPORTIND="YES",DLFTNOTIFICATIONARR=1,SERVSCOPEARRAY=1;
` 


### 删除对端NF基本信息配置(DEL SBIPEERNFBASEINFO) 
### 删除对端NF基本信息配置(DEL SBIPEERNFBASEINFO) 


功能说明 

该命令用于删除对端NF基本信息配置。当本地NRF配置不再需要配置该对端NFProfile时，使用该命令。命令执行成功后，本地NRF配置中将不包含该对端NFProfile。 


注意事项 

如果要删除对端NF基本信息配置，需要先删除引用该配置的对端NF扩展信息配置和对端NF服务实例配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询，对端NF服务实例配置通过[SHOW SBIPEERNFSERVICEINSTANCE]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFINSTANCEID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置NF实例的唯一标识。必须全局范围内唯一。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-127|该参数用于设置NF类型。
NFSTATUS|NF状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




命令举例 


`
删除对端NF基本信息配置：对端NF基本信息配置索引为1。
DEL SBIPEERNFBASEINFO:ID=1;
` 


### 查询对端NF基本信息配置(SHOW SBIPEERNFBASEINFO) 
### 查询对端NF基本信息配置(SHOW SBIPEERNFBASEINFO) 


功能说明 

该命令用于查询对端NF基本信息配置。当需要查询本地NRF配置中所配置的对端NFProfile中的基本信息字段时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFINSTANCEID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置NF实例的唯一标识。必须全局范围内唯一。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-127|该参数用于设置NF类型。
NFSTATUS|NF状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF基本信息编号，该编号是对端NF基本信息的唯一标识，被对端NF扩展信息配置及对端NF服务实例配置引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。对端NF服务实例配置通过SHOW SBIPEERNFSERVICEINSTANCE命令查询。
NFINSTANCEID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置NF实例的唯一标识。必须全局范围内唯一。
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-127|该参数用于设置NF类型。
NFSTATUS|NF状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置NF实例的状态。INVALID：NF实例的状态为无效的。REGISTERED：NF实例的状态为已注册的。表示NF实例已在NRF中注册，并且可以被其他NF发现SUSPENDED：NF实例的状态为已中止的。表示NF实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：NF实例的状态为无法被发现的。表示NF实例已在NRF中注册，可以运行，但是无法被其他NF发现。
NFINSTANCENAME|NF实例名称|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF实例的名称，方便操作人员识别。
PLMNLARRAY|PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN ID组编号，表示可用于该NF的一组PLMN（Public Land Mobile Network，公共陆地移动网）。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
PLMNNIDARRAY|PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN NID组编号，表示可用于该NF的一组SNPN（Standalone Non-Public Network，独立专网）。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，表示可用于该NF的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则NF可以服务于任何S-NSSAI。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，表示一组NF所支持的每个PLMN（Public Land Mobile Network，公共陆地移动网）支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果设置了该参数，则将取代“S-NSSAI组编号”，该参数适用于NF（例如AMF）支持多个PLMN并且每个PLMN中支持的切片不同的场景。该参数引用了PLMN S-NSSAI组编号配置，可以通过SHOW SBIPIMNSNSSAIARRID命令查询。
NSIARRAY|NSI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NSI组编号，表示NF可以服务的一组网络切片实例（NSI）。如果未设置，则NF可以服务任何NSI。该参数引用了NSI组编号配置，可以通过SHOW SBINSIARRID命令查询。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置FQDN（Fully Qualified Domain Name，全称域名）。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可用于PLMN（Public Land Mobile Network，公共陆地移动网）间路由的域名，如果NF需要由不同PLMN中的其他NF发现，则必须将用于PLMN间路由的FQDN（Fully Qualified Domain Name，全称域名）注册到NRF。
IPV4ARRAY|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示该NF包含的一组IPv4地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6ARRAY|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示该NF包含的一组IPv6地址。NFProfile中应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
ALLOWPLMN|允许的PLMN ID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN ID组编号，表示允许访问NF实例的一组PLMN（Public Land Mobile Network，公共陆地移动网）。如果未设置，则允许任何PLMN访问NF。该参数引用了PLMN ID组编号配置，可以通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的PLMN NID组编号，表示允许访问NF实例的一组SNPN（Standalone Non-Public Network，独立专网）。如果NFService和NFProfile中存在此参数，则以NFService中的参数为准。NFService和NFProfile中均缺少此参数，表示除NFProfile的SNPN列表中已注册的SNPN之外，不允许任何SNPN访问服务实例。该参数引用了PLMN NID组编号配置，可以通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的NF类型组编号，表示允许访问NF实例的一组NF类型。如果未设置，则允许任何NF类型访问NF。该参数引用了NF类型组编号配置，可以通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的域组编号，表示允许访问NF实例的一组NF域名。如果未设置，则允许任何NF域访问NF。该参数引用了域组编号配置，可以通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许的S-NSSAI组编号，表示允许访问NF实例的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。如果未设置，则允许任何切片访问NF。该参数引用了S-NSSAI组编号配置，可以通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，表示为相对于其他相同类型NF实例的权重。如果有多个不同的NFProfile都携带了该参数，则服务使用者应该按照该参数设置的容量权重，以负荷分担的方式访问NF服务提供者。如果NF服务列表（NFServiceList）参数中也存在容量参数，则NF服务的容量将优先于该值。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级，如果同一个服务发现响应消息中携带了多个不同的服务提供者的NFProfile，则服务使用者始终根据该参数选择优先级最高（即值最小）的NFProfile。默认为0。
LOCALITY|地区|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置运营商定义的NF实例位置相关的信息（例如地理位置、数据中心）。
NFSETIDARRAY|NF集标识组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF集标识组编号，表示为相同用户或业务区/服务区提供服务的一组NF组成的NF集。当某个NF故障后，其所承担话务可以由集内的其他NF接管，继续提供服务。该参数引用了NF集标识组编号配置，可以通过SHOW SBINFSETIDARRID命令查询。
NFSERVPERSISTENCE|是否支持资源在NF服务实例间共享|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持资源在NF服务实例间共享。NF实例中支持相同API版本和相同NF服务名的不同服务实例，可以选择支持将其资源状态保存在共享存储中。因此，当NF服务使用者选择了相同API版本的新NF服务实例后，可以使用这些共享存储中的资源。
LCHSUPPORTIND|是否支持基于LCI头域的负载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于LCI（Load Control Information，负载控制信息）头域的负载控制。支持LC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含负载信息的LCI头域，服务使用者能够根据LCI负载分担来选择服务提供者，从而实现负载均衡。
OLCHSUPPORTIND|是否支持基于OCI头域的过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持基于OCI（Overload Control Information，过载控制信息）头域的过载控制。支持OLC-H功能的NF服务提供者，向NF服务使用者发送的消息中可以携带包含过载信息的OCI头域，服务使用者能够根据OCI来控制发送到服务提供者的请求消息数量，从而实现过载保护。
DLFTNOTIFICATIONARR|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，表示一组通知类型不同的通知端点。该参数引用了缺省通知端点组编号配置，可以通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
SERVSCOPEARRAY|服务范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置服务范围组编号，表示在PLMN（Public Land Mobile Network，公共陆地移动网）中NF实例可以服务的一组区域。该属性可以指示地理区域，例如可以在集中式数据中心中用来发现和选择NF，这些NF可为位于特定地区或省份的用户提供服务。该参数引用了服务范围组编号配置，可以通过SHOW SBISERVSCOPEARRID命令查询。
SCPDOMAIN|NF归属的SCP域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|SCP域由一个或多个SCP和零个或多个NF（非SCP）组成。SCP域中的SCP可以直接与该域中的任何NF（非SCP）或者SCP通信。NF包括SCP和NF（非SCP）两种类型。该参数用于设置NF归属的SCP域，表示SCP（Service Communication Proxy，服务通讯代理）所属的SCP域列表，或NF（非SCP）所属的SCP域。其中，NF（非SCP）只能属于一个SCP域。若NF（非SCP）设置了归属的SCP域，则该NF优先通过属于相同的SCP域的SCP网元接入服务。




命令举例 


`
查询对端NF基本信息配置：对端NF基本信息配置索引为1。
SHOW SBIPEERNFBASEINFO:ID=1

(No.1) : SHOW SBIPEERNFBASEINFO:ID=1
-----------------http_st_ci_1/CommonS_HTTP_LB_0----------------
操作维护       对端NF信息编号 NF实例标识                           NF类型 NF状态     NF实例名称 PLMN ID组编号 PLMN NID组编号 S-NSSAI组编号 PLMN S-NSSAI组编号 NSI组编号 域名       PLMN间域名  IPv4地址组编号 IPv6地址组编号 允许的PLMN ID组编号 允许的PLMN NID组编号 允许的NF类型组编号 允许的域组编号 允许的S-NSSAI组编号 容量 优先级 地区 NF集标识组编号 是否支持资源在NF服务实例间共享 是否支持基于LCI头域的负载控制 是否支持基于OCI头域的过载控制 缺省通知端点组编号 服务范围组编号 NF归属的SCP域 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1              aaa00a00-0a00-000a-a0a0-00aa00a00aa0 NRF    REGISTERED abc        1             1              1             1                  1         zte.com.cn plmn.com.cn 1              1              2                   2                    2                  2              2                   10   1      NJ   1              是                             是                            是                            1                  1                            
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 19:06:56 耗时: 0.636 秒

` 


## 对端NF扩展信息配置 
## 对端NF扩展信息配置 


背景知识 


对端NF扩展信息配置即对应所有与特定NF类型有关的NF扩展信息，例如AMF信息、SMF信息等等。 




功能说明 


该配置通过引用“NF扩展信息配置”中单个NF信息配置编号的方式，来组织成NFProfile中的NF扩展信息，注意必须引用与NFProfile中NF类型参数一致的NF信息配置编号。当启用本地NRF功能时，需要配置该组命令。如果不配置该组命令，则NFProfile不能携带NF扩展信息，当服务使用者从本地NRF配置信息中发现服务提供者时，无法根据NF扩展信息中的参数进行匹配，可能导致发现失败。 




子主题： 






### 新增对端NF扩展信息配置(ADD SBIPEERNFEXTINFO) 
### 新增对端NF扩展信息配置(ADD SBIPEERNFEXTINFO) 


功能说明 

本命令用于新增对端NF扩展信息。当本地NRF配置中所配置的对端NFProfile需要携带扩展信息字段时，使用该命令。命令执行成功后，在本地NRF发现的对端NFProfile中将包含NF扩展信息字段。 


注意事项 

在配置NF扩展信息之前需要先配置对端NF基本信息，二者通过对端NF信息编号做关联。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。

系统支持的该配置项最大记录数为1024。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




命令举例 


`
增加对端NF扩展信息配置：对端NF信息编号为1，UDR信息编号为1。 
ADD SBIPEERNFEXTINFO:ID=1,UDRINFO=1
` 


### 修改对端NF扩展信息配置(SET SBIPEERNFEXTINFO) 
### 修改对端NF扩展信息配置(SET SBIPEERNFEXTINFO) 


功能说明 

本命令用于修改对端NF扩展信息。当本地NRF配置中所配置的对端NFProfile携带的扩展信息字段需要修改时，使用该命令。命令执行成功后，修改后的基本信息字段会呈现在本地NRF配置中所配置的对端NFProfile的扩展信息字段中。 


注意事项 

修改对端NF扩展信息，需要保证对端NF扩展信息已经存在，该信息通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




命令举例 


`
修改对端NF扩展信息配置：对端NF信息编号为1，UDR信息编号为1。 
SET SBIPEERNFEXTINFO:ID=1,UDRINFO=1
` 


### 删除对端NF扩展信息配置(DEL SBIPEERNFEXTINFO) 
### 删除对端NF扩展信息配置(DEL SBIPEERNFEXTINFO) 


功能说明 

本命令用于删除对端NF扩展信息。当本地NRF配置中所配置的对端NFProfile不需要携带扩展信息字段时，使用该命令。命令执行成功后，在本地NRF发现的对端NFProfile将不再包含NF扩展信息字段。 


注意事项 

删除对端NF扩展信息配置，需要先查询对应的对端NF信息编号，再使用对端NF信息编号进行删除。对端NF信息编号通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




命令举例 


`
删除对端NF扩展信息配置：对端NF信息编号为1。
DEL SBIPEERNFEXTINFO:ID=1
` 


### 查询对端NF扩展信息配置(SHOW SBIPEERNFEXTINFO) 
### 查询对端NF扩展信息配置(SHOW SBIPEERNFEXTINFO) 


功能说明 

本命令用于查询对端NF扩展信息。通常使用对端NF信息编号查询对应的NF扩展信息编号，即网元特有的信息编号，比如AMF信息编号、SMF信息编号等。对端NF基本信息配置通过[SHOW SBIPEERNFBASEINFO]命令查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|对端NF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置对端NF扩展信息关联的对端NF信息编号，该编号通过SHOW SBIPEERNFBASEINFO命令查询。
AMFINFO|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AMF信息编号，AMF信息编号通过SHOW SBIAMFINFO命令查询。当对端NF类型是AMF时，配置此参数。如果不配置，则对端NFProfile不包含AMF信息。
AUSFINFO|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置AUSF信息编号，AUSF信息编号通过SHOW SBIAUSFINFO命令查询。当对端NF类型是AUSF时，配置此参数。如果不配置，则对端NFProfile不包含AUSF信息。
BSFINFO|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置BSF信息编号，BSF信息编号通过SHOW SBIBSFINFO命令查询。当对端NF类型是BSF时，配置此参数。如果不配置，则对端NFProfile不包含BSF信息。
CHFINFO|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置CHF信息编号，CHF信息编号通过SHOW SBICHFINFO命令查询。当对端NF类型是CHF时，配置此参数。如果不配置，则对端NFProfile不包含CHF信息。
GMLCINFO|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GMLC信息编号，GMLC信息编号通过SHOW SBIGMLCINFO命令查询。当对端NF类型是GMLC时，配置此参数。如果不配置，则对端NFProfile不包含GMLC信息。
LMFINFO|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置LMF信息编号，LMF信息编号通过SHOW SBILMFINFO命令查询。当对端NF类型是LMF时，配置此参数。如果不配置，则对端NFProfile不包含LMF信息。
NWDAFINFO|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NWDAF信息编号，NWDAF信息编号通过SHOW SBINWDAFINFO命令查询。当对端NF类型是NWDAF时，配置此参数。如果不配置，则对端NFProfile不包含NWDAF信息。
PCFINFO|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PCF信息编号，PCF信息编号通过SHOW SBIPCFINFO命令查询。当对端NF类型是PCF时，配置此参数。如果不配置，则对端NFProfile不包含PCF信息。
SMFINFO|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF信息编号，SMF信息编号通过SHOW SBISMFINFO命令查询。当对端NF类型是SMF时，配置此参数。如果不配置，则对端NFProfile不包含SMF信息。
UDMINFO|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDM信息编号，UDM信息编号通过SHOW SBIUDMINFO命令查询。当对端NF类型是UDM时，配置此参数。如果不配置，则对端NFProfile不包含UDM信息。
UDRINFO|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UDR信息编号，UDR信息编号通过SHOW SBIUDRINFO命令查询。当对端NF类型是UDR时，配置此参数。如果不配置，则对端NFProfile不包含UDR信息。
UPFINFO|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF信息编号，UPF信息编号通过SHOW SBIUPFINFO命令查询。当对端NF类型是UPF时，配置此参数。如果不配置，则对端NFProfile不包含UPF信息。
OCSINFO|OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置OCS信息编号，OCS信息编号通过SHOW SBIOCSINFO命令查询。当对端NF类型是CUSTOM_OCS时，配置此参数。如果不配置，则对端NFProfile不包含OCS信息。




命令举例 


`
查询对端NF扩展信息配置：对端NF信息编号为1。
SHOW SBIPEERNFEXTINFO:ID=1

(No.12) : SHOW SBIPEERNFEXTINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       对端NF信息编号 AMF信息编号 AUSF信息编号 BSF信息编号 CHF信息编号 GMLC信息编号 LMF信息编号 NWDAF信息编号 PCF信息编号 SMF信息编号 UDM信息编号 UDR信息编号 UPF信息编号 OCS信息编号
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1              5                                                                                                                                                                                                                                                                                  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-25 16:45:05 耗时: 0.571 秒

` 


# 对端NF服务实例配置 
# 对端NF服务实例配置 


背景知识 


5GC采用了SBA（Service Based Architecture，基于服务的架构）架构，基于服务的设计理念，每个NF以服务的方式进行呈现，该服务为NF可以提供的一组服务。 

在本地NRF中，该命令用于配置一个具体的服务，包括：服务名称、服务实例标识以及服务实例的状态等。 




功能说明 


本地NRF功能中，需要配置对端NF可以提供的服务信息时，需要使用该命令。 

该配置依赖于对端NF配置，归属NF编号标识了该服务的归属关系。该编号通过[SHOW SBIPEERNFBASEINFO]命令查询。

如果对端NF配置没有关联任何一个对端NF服务实例配置，则在服务发现时，不会匹配到该NF。 




子主题： 






## 新增对端NF服务实例配置(ADD SBIPEERNFSERVICEINSTANCE) 
## 新增对端NF服务实例配置(ADD SBIPEERNFSERVICEINSTANCE) 


功能说明 

该命令用于新增对端NF服务实例配置。当本地NRF配置的NF实例需要增加可以为5GC网络中其他NF提供的服务时，使用该命令。执行成功后，该NF实例新增了一个可以提供的服务，该服务在被其他NF服务发现时进行匹配和使用。 


注意事项 


 
需要保证配置的“归属NF编号”已经存在，该编号通过SHOW SBIPEERNFBASEINFO命令查询。 

 
如果需要配置“次选CHF服务实例”，则需要保证“首选CHF服务实例”已经配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 必选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




命令举例 


`
新增对端NF服务实例配置：配置索引为1，归属NF编号为1，服务实例标识为1，服务名称为："nnrf_disc"，服务版本组编号为1，协议模式为：HTTPS，服务实例状态为REGISTERED，域名为："zte.com"，PLMN间域名为："5gc.com"，IP端点组编号为1，API路径前缀为："uri"，缺省通知端点组编号为1，允许的PLMN组编号为1，允许的PLMN NID组编号为1，允许的NF类型组编号为1，允许的域组编号为1，允许的S-NSSAI组编号为1，容量为12，优先级为1，支持的特性为："2"，首选CHF服务实例为："12"，次选CHF服务实例为："11"， NF服务集组标识为1，S-NSSAI组编号为1，PLMN S-NSSAI组编号为1。 
ADD SBIPEERNFSERVICEINSTANCE:INDEX=1,NFINDEX=1,SRVINSTANCEID="1",SERVICENAME="NNRF_DISC",SERVICEVERSIONARRAY=1,SCHEME="HTTPS",NFSERVICESTATUS="REGISTERED",FQDN="zte.com",INTERPLMNFQDN="5gc.com",IPENDPOINTARRAY=1,APIPREFIX="uri",DLFTNOTIFICATEARRAY=1,ALLOWPLMN=1,ALLOWPLMNNID=1,ALLOWNFTYPE=1,ALLOWNDOMAIN=1,ALLOWSNSSAI=1,CAPACITY=12,PRIORITY=1,SUPPORTEDFEATURES="2",PRIMARYCHFSRVINST="12",SECONDCHFSRVINST="11",NFSERVICESETARRAY=1,SNSSAIARRAY=1,PLMNSNSSAIARRAY=1
` 


## 修改对端NF服务实例配置(SET SBIPEERNFSERVICEINSTANCE) 
## 修改对端NF服务实例配置(SET SBIPEERNFSERVICEINSTANCE) 


功能说明 

该命令用于修改对端NF服务实例配置。当本地NRF配置的NF实例需要修改可以为5GC网络中其他NF提供的服务时，例如：服务实例状态、协议模式等，使用该命令。执行成功，该NF实例修改了一个可以提供的服务，该服务在被其他NF服务发现时进行匹配和使用。 


注意事项 


 
需要保证配置的“归属NF编号”已经存在，该编号通过SHOW SBIPEERNFBASEINFO命令查询。 

 
如果需要配置“次选CHF服务实例”，则需要保证“首选CHF服务实例”已经配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




命令举例 


`
修改对端NF服务实例配置：配置索引为1，归属NF编号为1，服务实例标识为1，服务名称为："nnrf_disc"，服务版本组编号为1，协议模式为：HTTPS，服务实例状态为SUSPENDED，域名为："zte.com"，PLMN间域名为："5gc.com"，IP端点组编号为1，API路径前缀为："uri"，缺省通知端点组编号为1，允许的PLMN组编号为1，允许的PLMN NID组编号为1，允许的NF类型组编号为1，允许的域组编号为1，允许的S-NSSAI组编号为1，容量为12，优先级为1，支持的特性为："2"，首选CHF服务实例为："12"，次选CHF服务实例为："11"， NF服务集组标识为1，S-NSSAI组编号为1，PLMN S-NSSAI组编号为1。 
SET SBIPEERNFSERVICEINSTANCE:INDEX=1,NFINDEX=1,SRVINSTANCEID="1",SERVICENAME="NNRF_DISC",SERVICEVERSIONARRAY=1,SCHEME="HTTPS",NFSERVICESTATUS="SUSPENDED",FQDN="zte.com",INTERPLMNFQDN="5gc.com",IPENDPOINTARRAY=1,APIPREFIX="uri",DLFTNOTIFICATEARRAY=1,ALLOWPLMN=1,ALLOWPLMNNID=1,ALLOWNFTYPE=1,ALLOWNDOMAIN=1,ALLOWSNSSAI=1,CAPACITY=12,PRIORITY=1,SUPPORTEDFEATURES="2",PRIMARYCHFSRVINST="12",SECONDCHFSRVINST="11",NFSERVICESETARRAY=1,SNSSAIARRAY=1,PLMNSNSSAIARRAY=1
` 


## 删除对端NF服务实例配置(DEL SBIPEERNFSERVICEINSTANCE) 
## 删除对端NF服务实例配置(DEL SBIPEERNFSERVICEINSTANCE) 


功能说明 

该命令用于删除对端NF服务实例配置。当本地NRF配置的NF实例不再为5GC网络中其他NF提供某个服务时，使用该命令。执行成功后，该NF删除了一个可以提供的服务，在被其他NF服务发现时也不会再匹配和使用该服务。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




命令举例 


`
删除对端NF服务实例配置：配置索引为1。
DEL SBIPEERNFSERVICEINSTANCE:INDEX=1
` 


## 查询对端NF服务实例配置(SHOW SBIPEERNFSERVICEINSTANCE) 
## 查询对端NF服务实例配置(SHOW SBIPEERNFSERVICEINSTANCE) 


功能说明 

该命令用于查询对端NF服务实例配置。当需要查询某个服务的具体信息时，使用该命令。执行成功后，会返回该服务实例的具体配置信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该配置索引全局唯一。用于唯一标识一个服务实例。
NFINDEX|归属NF编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置本次配置的服务实例归属的NF，用NF编号进行标识，该NF编号通过SHOW SBIPEERNFBASEINFO命令查询。
SRVINSTANCEID|服务实例标识|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于设置服务实例标识，是给定NF实例中服务实例的唯一ID。禁止填写"N/A"。
SERVICENAME|服务名称|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于设置服务实例的名称。服务名称枚举选项和取值含义参见3GPP TS 29.510 6.1.6.3.11章节。
SERVICEVERSIONARRAY|服务版本组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置服务版本组编号，表示服务支持的API版本，以及可用的服务的相应退出日期。该编号通过SHOW SBINFSVERSIONARRID命令查询。
SCHEME|协议模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置访问该服务的协议模式。HTTP：协议模式类型为HTTP。HTTP是一个基于请求与响应，无状态的，应用层的协议，常基于TCP/IP协议传输数据，互联网上应用最为广泛的一种网络协议,所有的WWW文件都必须遵守这个标准。HTTPS：协议模式类型为HTTPS。HTTPS是一种通过计算机网络进行安全通信的传输协议，经由HTTP进行通信，利用SSL/TLS建立全信道，加密数据包。
NFSERVICESTATUS|服务实例状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置服务实例的状态。INVALID：服务实例的状态为INVALID。无效状态，NF服务实例尚未在NRF中注册，不能被其他NF发现。REGISTERED：服务实例的状态为REGISTERED。NF服务实例已在NRF中注册，并且可以被其他NF发现。SUSPENDED：服务实例的状态为SUSPENDED。NF服务实例已在NRF中注册，但无法运行，无法被其他NF发现。UNDISCOVERABLE：服务实例的状态为UNDISCOVERABLE。NF服务实例已在NRF中注册，可以运行，但无法被其他NF发现。
FQDN|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置完全合格的域名（FQDN），表示该PLMN的FQDN。服务使用者构造服务的API URI使用。
INTERPLMNFQDN|PLMN间域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PLMN间的FQDN，如果NF服务需要由不同PLMN中的其他NF发现，则可以将用于PLMN间路由的FQDN注册到NRF。
IPENDPOINTARRAY|IP端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IP端点组编号，用于表示该服务正在侦听传入服务请求的网络功能的IP地址和端口信息。该编号通过SHOW SBIIPENDPOINTARRID命令查询。
APIPREFIX|API路径前缀|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置API路径前缀，为可选路径段，用于构建不同API URI的{apiRoot}变量的可选路径段。
DLFTNOTIFICATEARRAY|缺省通知端点组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置缺省通知端点组编号，该编号通过SHOW SBIDLFTNOTEENDPOINTARRID命令查询。
ALLOWPLMN|允许的PLMN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN组编号，该编号通过SHOW SBIPLMNIDARRID命令查询。
ALLOWPLMNNID|允许的PLMN NID组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的PLMN NID组编号，该编号通过SHOW SBIPLMNNIDARRID命令查询。
ALLOWNFTYPE|允许的NF类型组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的NF类型组编号，该编号通过SHOW SBINFTYPEARRID命令查询。
ALLOWNDOMAIN|允许的域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的域组编号，该编号通过SHOW SBIDOMAINARRID命令查询。
ALLOWSNSSAI|允许的S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置允许访问该服务的S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
CAPACITY|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置静态容量信息，范围为0-65535，表示为相对于相同类型其他服务的权重。取值越大，则权重越高。用于NF服务选择和负载均衡。默认为65535。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置优先级（相对于其他相同类型的服务），范围为0-65535，用于NF服务选择；较低的值表示较高的优先级。用于NF服务选择和负载均衡。默认为0。
SUPPORTEDFEATURES|支持的特性|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置服务实例支持的特性。
PRIMARYCHFSRVINST|首选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置首选CHF服务实例。
SECONDCHFSRVINST|次选CHF服务实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置次选CHF服务实例。只有配置了“首选CHF服务实例”，才能进行该参数配置。
NFSERVICESETARRAY|NF服务集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置NF服务集组编号，该编号通过SHOW SBINFSSETIDARRID命令查询。
SNSSAIARRAY|S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置S-NSSAI组编号，该编号通过SHOW SBISNSSAIARRID命令查询。
PLMNSNSSAIARRAY|PLMN S-NSSAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN S-NSSAI组编号，该编号通过SHOW SBIPIMNSNSSAIARRID命令查询。




命令举例 


`
查询对端NF服务实例配置：配置索引为1。
SHOW SBIPEERNFSERVICEINSTANCE:INDEX=1

(No.10) : SHOW SBIPEERNFSERVICEINSTANCE:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 归属NF编号 服务实例标识 服务名称  服务版本组编号 协议模式 服务实例状态 域名    PLMN间域名 IP端点组编号 API路径前缀 缺省通知端点组编号 允许的PLMN组编号 允许的PLMN NID组编号 允许的NF类型组编号 允许的域组编号 允许的S-NSSAI组编号 容量 优先级 支持的特性 首选CHF服务实例 次选CHF服务实例 NF服务集组编号 S-NSSAI组编号 PLMN S-NSSAI组编号 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1        1          1             nnrf_disc 1               HTTPS     REGISTERED   zte.com 5gc.com    1            uri          1                   1                1                     1                   1              1                    12   1      2           12              11              1               1             1                
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 15:24:42 耗时: 0.67 秒

` 


# NF扩展信息配置 
# NF扩展信息配置 


背景知识 


NF扩展信息配置包含了所有单个NF扩展信息配置，例如AMF信息、SMF信息等等。单个NF扩展信息配置编号被“对端NF扩展信息配置”引用，表现为NFProfile中的单个NF扩展信息参数。 




功能说明 


该组命令用于配置所有的单个NF扩展信息。当启用本地NRF功能时，需要配置该组命令。如果不配置该组命令，则NFProfile不能携带NF扩展信息，当服务使用者从本地NRF配置信息中发现服务提供者时，无法根据NF扩展信息中的参数进行匹配，可能导致发现失败。 




子主题： 






## AMF配置 
## AMF配置 


背景知识 


当服务提供者（对端）向NRF注册时，如果对端的NF(网络功能，Network Function)类型为AMF，注册请求中携带的对端NFProfile参数可以包含AMF信息(AmfInfo)参数，该参数又包含了一些通用或AMF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为AMF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的AMF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，AMF信息配置会呈现在对端NFProfile的AMF信息参数中。 




功能说明 


AMF配置为命令树目录，下面包含了AMF信息配置。AMF信息配置即对应本地NRF配置的对端NFProfile的AMF信息参数，如果不配置，则对端NFProfile缺少AMF信息参数，本端如果需要发现可用的对端AMF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### AMF信息配置 
### AMF信息配置 


背景知识 


当服务提供者（对端）向NRF注册时，如果对端的NF(网络功能，Network Function)类型为AMF，注册请求中携带的对端NFProfile参数可以包含AMF信息(AmfInfo)参数，该参数又包含了一些通用或AMF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为AMF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的AMF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，AMF信息配置会呈现在对端NFProfile的AMF信息参数中。 




功能说明 


AMF信息配置即对应本地NRF配置的对端NFProfile的AMF信息参数，如果不配置，则对端NFProfile缺少AMF信息参数，本端如果需要发现可用的对端AMF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增AMF信息配置(ADD SBIAMFINFO) 
#### 新增AMF信息配置(ADD SBIAMFINFO) 


功能说明 

本命令用于新增AMF信息配置。当启用本地NRF功能时，执行该命令。命令执行成功后，本配置可以被对端NF扩展信息配置引用。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 必选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 任选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




命令举例 


`
增加AMF信息配置，AMF信息编号为1，AMF区域标识为“12"，AMF集标识为"3a1",GUAMI组编号为1，TAI组编号为1，TAI范围组编号为1，失败备用GUAMI组编号为2，迁移备用GUAMI组编号为3。
ADD SBIAMFINFO:ID=1,AMFREGIONID="12",AMFSETIDENT="3a1",GUAMIARRAY=1,TAIARRAY=1,TAIRNGARRAY=1,FAILBAKGUAMIARRAY=2,RMVBAKGUAMIARRAY=3
` 


#### 修改AMF信息配置(SET SBIAMFINFO) 
#### 修改AMF信息配置(SET SBIAMFINFO) 


功能说明 

本命令用于修改AMF信息配置。当AMF信息编号关联的AMF区域标识等参数发生变更时，执行该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 任选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 任选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




命令举例 


`
修改AMF信息编号为1的AMF信息配置，将AMF区域标识改为“34"，AMF集标识改为"3bc"。 
SET  SBIAMFINFO:ID=1,AMFREGIONID="34",AMFSETIDENT="3bc"
` 


#### 删除AMF信息配置(DEL SBIAMFINFO) 
#### 删除AMF信息配置(DEL SBIAMFINFO) 


功能说明 

本命令用于删除AMF信息配置。 


注意事项 

删除后，服务使用者如果需要发现可用的AMF时，就无法进行有效的发现参数匹配，可能导致业务失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 任选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




命令举例 


`
删除AMF信息编号为1的AMF信息配置。
DEL SBIAMFINFO:ID=1
` 


#### 查询AMF信息配置(SHOW SBIAMFINFO) 
#### 查询AMF信息配置(SHOW SBIAMFINFO) 


功能说明 

本命令用于查询AMF信息配置，包括AMF信息编号，及其关联的AMF区域标识等参数。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 任选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AMF信息编号。
AMFREGIONID|AMF区域标识|参数可选性: 任选参数类型: 字符串参数范围: 2-2|该参数用于设置AMF区域标识，格式为2个十六进制字符，范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF区域标识与配置的AMF区域标识是否一致，如果一致则认为匹配成功。
AMFSETIDENT|AMF集标识|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于设置AMF集标识，格式为3个十六进制字符，第1个字符范围是0-3，后面2个字符范围是A-F或a-f或0-9。当本地NRF功能处理服务发现请求时，会比较发现请求中的AMF集标识与配置的AM集标识是否一致，如果一致则认为匹配成功。
GUAMIARRAY|GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的GUAMI与配置的GUAMI组信息是否一致，如果一致则认为匹配成功。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，TAI组编号通过SHOW SBITAIARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的TAI与配置的TAI组信息是否一致，如果一致则认为匹配成功。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，TAI范围组编号通过SHOW SBITAIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会判断发现请求中的TAI是否落在配置的TAI范围组的范围内，如果是则认为匹配成功。
FAILBAKGUAMIARRAY|失败备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置失败备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在故障场景下，本AMF可以接管哪些GUAMI。
RMVBAKGUAMIARRAY|迁移备用GUAMI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置迁移备用GUAMI组编号，GUAMI组编号通过SHOW SBIGUAMIARRID命令查询。该参数用于AMF容灾，表示在维护场景下，本AMF可以接管哪些GUAMI。




命令举例 


`
查询AMF信息编号为1的AMF信息配置。
SHOW SBIAMFINFO:ID=1

(No.3) : SHOW SBIAMFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       AMF信息编号 AMF区域标识 AMF集标识 GUAMI组编号 TAI组编号 TAI范围组编号 失败备用GUAMI组编号 迁移备用GUAMI组编号 
-----------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1           12          3a1       1           1         1             2                   3                           
-----------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:08:22 耗时: 0.517 秒

` 


## AUSF配置 
## AUSF配置 


背景知识 


当服务提供者（对端）向NRF注册时，如果对端的NF(网络功能，Network Function)类型为AUSF，注册请求中携带的对端NFProfile参数可以包含AUSF信息(AusfInfo)参数，该参数又包含了一些通用或AUSF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为AUSF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的AUSF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，AUSF信息配置会呈现在对端NFProfile的ASUF信息参数中。 




功能说明 


AUSF配置为命令树目录，下面包含了AUSF信息配置。AUSF信息配置即对应本地NRF配置的对端NFProfile的AUSF信息参数，如果不配置，则对端NFProfile缺少AUSF信息参数，本端如果需要发现可用的对端AUSF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### AUSF信息配置 
### AUSF信息配置 


背景知识 


当服务提供者（对端）向NRF注册时，如果对端的NF(网络功能，Network Function)类型为AUSF，注册请求中携带的对端NFProfile参数可以包含AUSF信息(AusfInfo)参数，该参数又包含了一些通用或AUSF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为AUSF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的AUSF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，AUSF信息配置会呈现在对端NFProfile的ASUF信息参数中。 




功能说明 


AUSF信息配置即对应本地NRF配置的对端NFProfile的AUSF信息参数，如果不配置，则对端NFProfile缺少AUSF信息参数，本端如果需要发现可用的对端AUSF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增AUSF信息配置(ADD SBIAUSFINFO) 
#### 新增AUSF信息配置(ADD SBIAUSFINFO) 


功能说明 

本命令用于新增AUSF信息配置。当启用本地NRF功能时，执行该命令。命令执行成功后，本配置可以被对端NF扩展信息配置引用。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
增加AUSF信息配置，AUSF信息编号为1，NF组标识为“nfGroup1"，SUPI范围组编号为1，路由指示组编号为1。 
ADD SBIAUSFINFO:ID=1,GROUPID="nfGroup1",SUPIRANGEARRAY=1,ROUTINDARRAY=1
` 


#### 修改AUSF信息配置(SET SBIAUSFINFO) 
#### 修改AUSF信息配置(SET SBIAUSFINFO) 


功能说明 

本命令用于修改AUSF信息配置。当AUSF信息编号关联的NF组标识、SUPI范围组编号、路由指示组编号发生变更时，执行该命令 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
修改AUSF信息编号为1的AUSF信息配置，将NF组标识改为“nfGroup2"。 
SET SBIAUSFINFO:ID=1,GROUPID="nfGroup2"
` 


#### 删除AUSF信息配置(DEL SBIAUSFINFO) 
#### 删除AUSF信息配置(DEL SBIAUSFINFO) 


功能说明 

本命令用于删除AUSF信息配置。 


注意事项 

删除后，服务使用者如果需要发现可用的AUSF时，就无法进行有效的发现参数匹配，可能导致业务失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
删除AUSF信息编号为1的AUSF信息配置。
DEL SBIAUSFINFO:ID=1
` 


#### 查询AUSF信息配置(SHOW SBIAUSFINFO) 
#### 查询AUSF信息配置(SHOW SBIAUSFINFO) 


功能说明 

本命令用于查询AUSF信息配置，包括AUSF信息编号，及其关联的NF组标识、SUPI范围组编号、路由指示组编号参数。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|AUSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置AUSF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置NF组标识，NF组标识是一组AUSF的标识符。如果不配置，则该AUSF不属于任何AUSF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，SUPI范围组编号通过SHOW SBISUPIRANGEARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的SUPI是否落在配置的SUPI范围组的范围内，如果是则认为匹配成功。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，路由指示组编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
查询AUSF信息编号为1的AUSF信息配置。
SHOW SBIAUSFINFO:ID=1

(No.7) : SHOW SBIAUSFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       AUSF信息编号 NF组标识 SUPI范围组编号 路由指示组编号 
-------------------------------------------------------------------
复制 修改 删除 1            nfGroup1 1              1              
-------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-09 11:14:33 耗时: 0.518 秒

` 


## BSF配置 
## BSF配置 


背景知识 


当服务提供者（对端）向NRF注册时，如果对端的NF（网络功能，Network Function）类型为BSF，注册请求中携带的对端NFProfile参数可以包含BSF信息（BsfInfo）参数，该参数又包含了一些通用或BSF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为BSF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的BSF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，BSF信息配置会呈现在对端NFProfile的BSF信息参数中。 




功能说明 


本地NRF功能中，BSF配置包括： 


 
BSF信息配置：用于配置具体的BSF信息，如：IPv4 域名组标识、DNN组标识、IPv4 地址范围组标识、IPv6 前缀范围组标识等。 

 




子主题： 






### BSF信息配置 
### BSF信息配置 


背景知识 


当服务提供者（对端）向NRF注册时，如果对端的NF（网络功能，Network Function）类型为BSF，注册请求中携带的对端NFProfile参数可以包含BSF信息（BsfInfo）参数，该参数又包含了一些通用或BSF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为BSF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的BSF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，BSF信息配置会呈现在对端NFProfile的BSF信息参数中。 




功能说明 


BSF信息配置即对应本地NRF配置的对端NFProfile的BSF信息参数。当启用本地NRF功能时，需要配置该组命令。如果不配置，则对端NFProfile缺少BSF信息参数，本端如果需要发现可用的对端BSF时，就无法进行有效的发现参数匹配，可能导致业务失败。 




子主题： 






#### 新增BSF信息配置(ADD SBIBSFINFO) 
#### 新增BSF信息配置(ADD SBIBSFINFO) 


功能说明 

该命令用于新增BSF信息配置。当本地NRF配置中所配置的对端NFProfile需要携带BSF信息时，使用该命令。命令执行成功后，BSF信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


注意事项 

如果要新增该BSF信息配置，需要先新增域组编号、DNN组编号、IPv4地址范围组编号和IPv6前缀范围组编号。 

域组编号通过[SHOW SBIDOMAINARRID]命令查询。

DNN组编号通过[SHOW SBIDNNARRID]命令查询。

IPv4地址范围组编号通过[SHOW SBIIPV4ADDRRANGEARRID]命令查询。

IPv6前缀范围组编号通过[SHOW SBIIPV6PREFIXRANGEARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
增加BSF信息配置：编号为1，IPv4 地址范围组编号为1，IPv4 域名组编号为1，IPv6 前缀范围组编号为1，SMF DNN组编号为1。 
ADD SBIBSFINFO:ID=3,IPV4RNGARRAY=1,IPDOMAINARRAY=1,IPV6PREFIXRNGARRAY=1,DNNARRAY=1
` 


#### 修改BSF信息配置(SET SBIBSFINFO) 
#### 修改BSF信息配置(SET SBIBSFINFO) 


功能说明 

该命令用于修改BSF信息配置。当本地NRF配置中所配置的对端NFProfile携带的BSF信息需要变更时，使用该命令。命令执行成功后，修改后的BSF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
修改BSF信息配置：编号为1，IPv4 地址范围组编号为65535。 
SET SBIBSFINFO:ID=1,IPV4RNGARRAY=65535
` 


#### 删除BSF信息配置(DEL SBIBSFINFO) 
#### 删除BSF信息配置(DEL SBIBSFINFO) 


功能说明 

该命令用于删除BSF信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该BSF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该BSF信息。 


注意事项 

如果要删除该BSF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
删除BSF信息配置：编号为1。
DEL SBIBSFINFO:ID=1
` 


#### 查询BSF信息配置(SHOW SBIBSFINFO) 
#### 查询BSF信息配置(SHOW SBIBSFINFO) 


功能说明 

该命令用于查询BSF信息配置。当需要查询对端NFProfile携带的BSF信息时，使用该命令。 


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|BSF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置BSF信息编号。
IPV4RNGARRAY|IPv4 地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，指BSF处理的IPv4地址范围的列表。该编号可以通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPDOMAINARRAY|IPv4 域名组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4域名组编号，指由BSF处理的3GPP 29.513 [28]条款6.2中所述的IPv4地址域列表。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何IP域。该编号可以通过SHOW SBIDOMAINARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6 前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，指BSF可以处理的IPv6前缀范围的列表。该编号通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，指BSF处理的DNN列表。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NF配置文件的plmnList中的所有PLMN都支持DNN。 如果没有配置此处的IPv4 域名组编号时，则BSF可以服务于任何DNN。该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
查询BSF信息配置：编号为1。
SHOW SBIBSFINFO:ID=1

SHOW SBIBSFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       BSF信息编号 IPv4 地址范围组编号 IPv4 域名组编号 IPv6 前缀范围组编号 SMF DNN组编号 
-------------------------------------------------------------------------------------------------
复制 修改 删除 1           1                   1               1                   1             
-------------------------------------------------------------------------------------------------
记录数：1
耗时: 0.619 秒

` 


## CHF配置 
## CHF配置 


背景知识 


当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF(网络功能，Network Function)类型为CHF（计费功能，Charging Function），注册请求中携带的对端NFProfile参数可以包含CHF信息（ChfInfo）参数，该参数又包含了一些通用或CHF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为CHF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的CHF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，CHF信息配置会呈现在对端NFProfile的CHF信息参数中。 




功能说明 


CHF配置为命令树目录，下面包含了CHF信息配置。CHF信息配置即对应本地NRF配置的对端NFProfile的CHF信息参数，如果不配置，则对端NFProfile缺少CHF信息参数，本端如果需要发现可用的对端CHF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### CHF信息配置 
### CHF信息配置 


背景知识 


当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF(网络功能，Network Function)类型为CHF（计费功能，Charging Function），注册请求中携带的对端NFProfile参数可以包含CHF信息（ChfInfo）参数，该参数又包含了一些通用或CHF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为CHF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的CHF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，CHF信息配置会呈现在对端NFProfile的CHF信息参数中。 




功能说明 


CHF信息配置即对应本地NRF配置的对端NFProfile的CHF信息参数，如果不配置，则对端NFProfile缺少CHF信息参数，本端如果需要发现可用的对端CHF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增CHF信息配置(ADD SBICHFINFO) 
#### 新增CHF信息配置(ADD SBICHFINFO) 


功能说明 

本命令用于新增CHF信息。当本地NRF配置中所配置的对端NFProfile需要携带CHF信息时，使用该命令。命令执行成功后，CHF信息编号可以被对端NF扩展信息配置引用。 


注意事项 

系统支持的该配置项最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。测试使用
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
增加CHF信息配置：CHF信息编号为1，GPSI范围组编号为1。 
ADD SBICHFINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 修改CHF信息配置(SET SBICHFINFO) 
#### 修改CHF信息配置(SET SBICHFINFO) 


功能说明 

本命令用于修改CHF信息。当本地NRF配置中所配置的对端NFProfile携带的CHF信息需要变更时，使用该命令。命令执行成功后，修改后的CHF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

修改CHF信息，需要保证CHF信息编号已经存在，该编号通过[SHOW SBICHFINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。测试使用
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
修改CHF信息配置：CHF信息编号为1，GPSI范围组编号为1。 
SET  SBICHFINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 删除CHF信息配置(DEL SBICHFINFO) 
#### 删除CHF信息配置(DEL SBICHFINFO) 


功能说明 

本命令用于删除CHF信息。当本地NRF配置中所配置的对端NFProfile不需要携带该CHF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该CHF信息。 


注意事项 

如果要删除该CHF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
删除CHF信息配置：CHF信息编号为1。
DEL SBICHFINFO:ID=1
` 


#### 查询CHF信息配置(SHOW SBICHFINFO) 
#### 查询CHF信息配置(SHOW SBICHFINFO) 


功能说明 

本命令用于查询CHF信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。测试使用
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CHF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置CHF信息编号。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组CHF的标识符。如果不配置，则该CHF不属于任何CHF组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何SUPI。该编号通过SHOW SBISUPIRANGEARRID命令查询。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，用于指定CHF实例可以服务的GPSI范围列表。如果未提供，则CHF可以服务于任何GPSI。该编号通过SHOW SBIGPSIRANGEARRID命令查询。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN范围组编号，用于指定CHF实例可以服务的PLMN范围列表（包括CHF实例的PLMN ID）。如果未提供，则CHF可以为任何PLMN服务。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
查询CHF信息配置：CHF信息编号为1。
SHOW SBICHFINFO:ID=1

(No.12) : SHOW SBICHFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       CHF信息编号 NF组标识 SUPI范围组编号 GPSI范围组编号 PLMN范围组编号 
---------------------------------------------------------------------------------
复制 修改 删除 1                                   1                             
---------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-19 16:54:33 耗时: 0.635 秒

` 


## GMLC配置 
## GMLC配置 


背景知识 


GMLC（Gateway for Mobile Location Center，移动定位中心网关）设备用于与定位客户端交互，执行定位客户端的定位请求并向其回送定位结果。 

当服务提供者（对端）向NRF注册时，如果对端的NF（网络功能，Network Function）类型为GMLC，注册请求中携带的对端NFProfile参数可以包含GMLC信息(GMLCInfo)参数，该参数又包含了一些通用或GMLC特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为GMLC时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的GMLC信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，GMLC信息配置会呈现在对端NFProfile的GMLC信息参数中。 




功能说明 


GMLC配置为命令树目录，下面包含了GMLC信息配置。 

GMLC信息配置用于配置具体的GMLC信息。GMLC信息配置包含两个部分：GMLC信息编号和客户端类型。 




子主题： 






### GMLC信息配置 
### GMLC信息配置 


背景知识 


GMLC（Gateway for Mobile Location Center，移动定位中心网关）设备用于与定位客户端交互，执行定位客户端的定位请求并向其回送定位结果。 

当服务提供者（对端）向NRF注册时，如果对端的NF（网络功能，Network Function）类型为GMLC，注册请求中携带的对端NFProfile参数可以包含GMLC信息(GMLCInfo)参数，该参数又包含了一些通用或GMLC特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为GMLC时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的GMLC信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，GMLC信息配置会呈现在对端NFProfile的GMLC信息参数中。 




功能说明 


GMLC信息配置即对应本地NRF配置的对端NFProfile的GMLC信息参数。本地NRF功能中，当NF需要和GMLC进行交互时，需要使用该配置。配置完成后，NF可以通过服务发现，发现GMLC并进行交互。如果不配置，则对端NFProfile缺少GMLC信息参数，本端如果需要发现可用的对端GMLC时，就无法进行有效的发现参数匹配，可能导致业务失败。 




子主题： 






#### 新增GMLC信息配置(ADD SBIGMLCINFO) 
#### 新增GMLC信息配置(ADD SBIGMLCINFO) 


功能说明 

该命令用于新增GMLC信息配置。当本地NRF配置中所配置的对端NFProfile需要携带GMLC信息时，使用该命令。命令执行成功后，GMLC信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。

对端NF扩展信息配置中引用GMLC信息编号后，则该对端NF具备了GMLC能力。本端可以通过服务发现，发现GMLC并进行交互。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 必选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




命令举例 


`
增加GMLC信息配置：编号为1，客户端类型为"EMERGENCY_SERVICES"&"VALUE_ADDED_SERVICES"&"PLMN_OPERATOR_SERVICES"&"LAWFUL_INTERCEPT_SERVICES"&"PLMN_OPERATOR_BROADCAST_SERVICES"&"PLMN_OPERATOR_OM"&"PLMN_OPERATOR_ANONYMOUS_STATISTICS"&"PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT"。 
ADD SBIGMLCINFO:ID=1,CLIENTTYPE="EMERGENCY_SERVICES"&"VALUE_ADDED_SERVICES"&"PLMN_OPERATOR_SERVICES"&"LAWFUL_INTERCEPT_SERVICES"&"PLMN_OPERATOR_BROADCAST_SERVICES"&"PLMN_OPERATOR_OM"&"PLMN_OPERATOR_ANONYMOUS_STATISTICS"&"PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT"
` 


#### 修改GMLC信息配置(SET SBIGMLCINFO) 
#### 修改GMLC信息配置(SET SBIGMLCINFO) 


功能说明 

该命令用于修改GMLC信息配置。当本地NRF配置中所配置的对端NFProfile携带的GMLC信息需要变更时，使用该命令。命令执行成功后，修改后的GMLC信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 必选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




命令举例 


`
修改GMLC信息配置：编号为1，客户端类型为"EMERGENCY_SERVICES"。 
SET SBIGMLCINFO:ID=1,CLIENTTYPE="EMERGENCY_SERVICES"
` 


#### 删除GMLC信息配置(DEL SBIGMLCINFO) 
#### 删除GMLC信息配置(DEL SBIGMLCINFO) 


功能说明 

该命令用于删除GMLC信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该GMLC信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该GMLC信息。 


注意事项 

如果要删除该GMLC信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




命令举例 


`
删除GMLC信息配置：编号为1。
DEL SBIGMLCINFO:ID=1
` 


#### 查询GMLC信息配置(SHOW SBIGMLCINFO) 
#### 查询GMLC信息配置(SHOW SBIGMLCINFO) 


功能说明 

该命令用于查询GMLC信息配置。当需要查询对端NFProfile携带的GMLC信息时，使用该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|GMLC信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置GMLC信息编号。该编号全局唯一。提供给对端NF扩展信息配置使用。对端NF扩展信息配置可以使用SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置GMLC服务的特定的定位客户端类型，如果不配置，则GMLC实例不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。




命令举例 


`
查询GMLC信息配置：GMLC信息编号为1。
SHOW SBIGMLCINFO:ID=1

(No.2) : SHOW SBIGMLCINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       GMLC信息编号 客户端类型                                                                                                                                                                                                            
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1            EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-14 09:40:25 耗时: 0.153 秒

` 


## LMF配置 
## LMF配置 


背景知识 


LMF（Location Management Function，定位管理功能）是5G核心网中的网络实体，用于具体收集、计算和决定UE的相关位置信息，如：小区信息、接入基站等。 

当服务提供者（对端）向NRF注册时，如果对端的NF（网络功能，Network Function）类型为LMF，注册请求中携带的对端NFProfile参数可以包含LMF信息（LmfInfo）参数，该参数又包含了一些通用或LMF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为LMF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的LMF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，LMF信息配置会呈现在对端NFProfile的LMF信息参数中。 




功能说明 


LMF配置为命令树目录，下面包含了LMF信息配置。LMF信息配置即对应本地NRF配置的对端NFProfile的LMF信息参数，如果不配置，则对端NFProfile缺少LMF信息参数，本端如果需要发现可用的对端LMF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该命令。 




子主题： 






### LMF信息配置 
### LMF信息配置 


背景知识 


LMF（Location Management Function，定位管理功能）是5G核心网中的网络实体，用于具体收集、计算和决定UE的相关位置信息，如：小区信息、接入基站等。 

当服务提供者（对端）向NRF注册时，如果对端的NF（网络功能，Network Function）类型为LMF，注册请求中携带的对端NFProfile参数可以包含LMF信息（LmfInfo）参数，该参数又包含了一些通用或LMF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为LMF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的LMF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，LMF信息配置会呈现在对端NFProfile的LMF信息参数中。 




功能说明 


LMF信息配置即对应本地NRF配置的对端NFProfile的LMF信息参数，如果不配置，则对端NFProfile缺少LMF信息参数，本端如果需要发现可用的对端LMF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该命令。 




子主题： 






#### 新增LMF信息配置(ADD SBILMFINFO) 
#### 新增LMF信息配置(ADD SBILMFINFO) 


功能说明 

该命令用于新增LMF信息配置。当本地NRF配置中所配置的对端NFProfile需要携带LMF信息（例如：服务的客户端类型、支持的接入类型等）时，使用该命令。命令执行成功后，LMF信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


注意事项 

LMF信息配置表最大容量为1024。新增LMF信息时注意不要超过最大容量。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




命令举例 


`
增加LMF信息配置：编号为655，客户端类型"EMERGENCY_SERVICES"，LMF标识为“lmf_5gc”，接入类型为“3GPP接入类型”，支持AN节点类型为“所有AN节点类型”，支持RAT类型为“NR”。 
ADD SBILMFINFO:ID=655,CLIENTTYPE="EMERGENCY_SERVICES",LMFID="lmf_5gc",ACCESSTYPE="3GPP_ACCESS",ANNODETYPE="ALL_NB",RATTYPE="NR"
` 


#### 修改LMF信息配置(SET SBILMFINFO) 
#### 修改LMF信息配置(SET SBILMFINFO) 


功能说明 

该命令用于修改LMF信息配置。当本地NRF配置中所配置的对端NFProfile携带的LMF信息（例如：服务的客户端类型、支持的接入类型等）需要变更时，使用该命令。命令执行成功后，修改后的LMF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

LMF信息配置一般与对端NF扩展信息配置配合使用。可以使用命令[SHOW SBIPEERNFEXTINFO]查询对端NF扩展信息配置。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




命令举例 


`
修改LMF信息配置：编号为655，客户端类型"EMERGENCY_SERVICES"，LMF标识为“lmf_5gc”，接入类型为“3GPP接入类型”，支持AN节点类型为“所有AN节点类型”，支持RAT类型为“NULL”。  
SET SBILMFINFO:ID=655,CLIENTTYPE="EMERGENCY_SERVICES",LMFID="lmf_5gc",ACCESSTYPE="3GPP_ACCESS",ANNODETYPE="ALL_NB",RATTYPE="NULL"
` 


#### 删除LMF信息配置(DEL SBILMFINFO) 
#### 删除LMF信息配置(DEL SBILMFINFO) 


功能说明 

该命令用于删除LMF信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该LMF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该LMF信息。 


注意事项 

如果要删除该LMF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




命令举例 


`
删除LMF信息配置：编号为655。
DEL SBILMFINFO:ID=655
` 


#### 查询LMF信息配置(SHOW SBILMFINFO) 
#### 查询LMF信息配置(SHOW SBILMFINFO) 


功能说明 

该命令用于查询LMF信息配置。当需要查询对端NFProfile携带的LMF信息（例如：服务的客户端类型、支持的接入类型等）时，使用该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|LMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置LMF信息编号，该编号是LMF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
CLIENTTYPE|客户端类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: EMERGENCY_SERVICES&VALUE_ADDED_SERVICES&PLMN_OPERATOR_SERVICES&LAWFUL_INTERCEPT_SERVICES&PLMN_OPERATOR_BROADCAST_SERVICES&PLMN_OPERATOR_OM&PLMN_OPERATOR_ANONYMOUS_STATISTICS&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT|该参数用于设置LMF服务的特定的客户端类型。参数类型为位枚举，默认全选，支持位枚举中所有的客户端类型。如果该参数设置为NULL，则不专用于服务特定的客户端类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。EMERGENCY_SERVICES：紧急服务。VALUE_ADDED_SERVICES：增值服务。PLMN_OPERATOR_SERVICES：运营商自有服务。LAWFUL_INTERCEPT_SERVICES：合法拦截服务。PLMN_OPERATOR_BROADCAST_SERVICES：运营商广播服务。PLMN_OPERATOR_OM：运营商运维。PLMN_OPERATOR_ANONYMOUS_STATISTICS：运营商匿名统计。PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT：运营商终端服务支持。
LMFID|LMF标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置LMF实例标识。可以唯一标识该LMF。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的接入类型，如果不配置，则支持所有接入类型。ALL_ACCESS：表示该LMF支持所有接入类型。包括：3GPP和非3GPP。3GPP_ACCESS：表示该LMF仅支持3GPP接入类型。NON_3GPP_ACCESS：表示该LMF仅支持非3GPP接入类型。
ANNODETYPE|支持AN节点类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置LMF支持的AN节点类型（例如：gNB或NG-eNB），如果未配置，则支持所有AN节点类型 。ALL_NB：表示该LMF支持所有AN节点类型。包括：gNB和NG-eNB。GNB：表示该LMF仅支持gNB节点类型。NG_ENB：表示该LMF仅支持NG-eNB节点类型。
RATTYPE|支持RAT类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NR&EUTRA&WLAN&VIRTUAL&NBIOT&WIRELINE&WIRELINE_CABLE&WIRELINE_DSL&WIRELINE_PON&LTE_M&NR_U&EUTRA_U&TRUSTED_N3GA&TRUSTED_WLAN&UTRA&GERA|该参数用于设置LMF支持的RAT节点类型。参数类型为位枚举，默认全选，支持位枚举中的所有RAT节点类型。如果该参数设置为NULL，则表示不专用于指定的RAT节点类型。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示支持位枚举中的所有RAT节点类型。NR：New Radio，新空口。EUTRA：（WB）演进的通用地面无线电接入。WLAN：不受信任的无线局域网（IEEE 802.11）访问。VIRTUAL：虚拟，一般用于非3GPP接入的场景。NBIOT：NB IoT，窄带物联网。WIRELINE：Wireline access，有线接入。WIRELINE_CABLE：有线电缆接入。WIRELINE_DSL：Wireline DSL access。WIRELINE_PON：Wireline PON access。LTE_M：LTE-M，此RAT类型值仅在核心网络中使用；当使用E-UTRA的M类UE向NG-RAN提供了M类指示时，应使用它。NR_U：New Radio in unlicensed bands。EUTRA_U：（WB）在无执照频段内演进的通用地面无线电接入。TRUSTED_N3GA：可信的非3GPP接入。TRUSTED_WLAN：受信任的无线局域网（IEEE 802.11）访问。UTRA：UMTS地面无线电接入。GERA：GSM EDGE无线电访问网络。




命令举例 


`
查询LMF信息配置：LMF信息编号为655。
SHOW SBILMFINFO:ID=655

(No.5) : SHOW SBILMFINFO:ID=655
-----------------CommonS_HTTP_LB_0----------------
操作维护       LMF信息编号 客户端类型         LMF标识 接入类型     支持AN节点类型 支持RAT类型 
----------------------------------------------------------------------------------------------
复制 修改 删除 655         EMERGENCY_SERVICES lmf_5gc 3GPP接入类型 所有AN节点类型 New Radio   
----------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2021-01-29 14:56:15 耗时: 0.636 秒

` 


## NWDAF配置 
## NWDAF配置 


背景知识 


NWDAF（网络数据分析功能，Network Data Analytics Function）是3GPP在Rel 15的5G标准中引入的网络功能，主要用于网络相关数据的分析。 

当服务提供者（对端）向NRF注册时，如果对端的NF(网络功能，Network Function)类型为NWDAF，注册请求中携带的对端NFProfile参数可以包含NWDAF信息(NWDAFInfo)参数，该参数又包含了一些通用或NWDAF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为NWDAF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的NWDAF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，NWDAF信息配置会呈现在对端NFProfile的NWDAF信息参数中。 




功能说明 


NWDAF配置为命令树目录，下面包含了NWDAF信息配置。 

NWDAF信息配置用于配置具体的NWDAF信息。NWDAF信息配置包含五个部分： 


 
NWDAF信息编号 

 
TAI组编号。 

 
TAI范围组编号。 

 
分析服务支持的事件ID 

 
订阅支持的事件 

 




子主题： 






### NWDAF信息配置 
### NWDAF信息配置 


背景知识 


NWDAF（网络数据分析功能，Network Data Analytics Function）是3GPP在Rel 15的5G标准中引入的网络功能，主要用于网络相关数据的分析。 

当服务提供者（对端）向NRF注册时，如果对端的NF(网络功能，Network Function)类型为NWDAF，注册请求中携带的对端NFProfile参数可以包含NWDAF信息(NWDAFInfo)参数，该参数又包含了一些通用或NWDAF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为NWDAF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的NWDAF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，NWDAF信息配置会呈现在对端NFProfile的NWDAF信息参数中。 




功能说明 


NWDAF信息配置即对应本地NRF配置的对端NFProfile的NWDAF信息参数。本地NRF功能中，当NF需要和NWDAF进行交互时，需要使用该配置。配置完成后，NF可以通过服务发现，发现NWDAF并进行交互。如果不配置，则对端NFProfile缺少NWDAF信息参数，本端如果需要发现可用的对端NWDAF时，就无法进行有效的发现参数匹配，可能导致业务失败。 




子主题： 






#### 新增NWDAF信息配置(ADD SBINWDAFINFO) 
#### 新增NWDAF信息配置(ADD SBINWDAFINFO) 


功能说明 

该命令用于新增NWDAF信息配置。当本地NRF配置中所配置的对端NFProfile需要携带NWDAF信息时，使用该命令。命令执行成功后，NWDAF信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。

对端NF扩展信息配置中引用NWDAF信息编号后，则该对端NF具备了NWDAF能力。本端可以通过服务发现，发现NWDAF并进行交互。 


注意事项 

需要保证引用的如下配置已经存在： 


 
TAI组编号：通过命令SHOW SBITAIARRID查询。 

 
TAI范围组编号：通过命令SHOW SBITAIRANGEARRID查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




命令举例 


`
增加NWDAF信息配置：编号为655，TAI组编号为1，TAI范围组编号为65535，分析服务支持的事件ID为："LOAD_LEVEL_INFORMATION"，订阅支持的事件为："NF_LOAD"。 
ADD SBINWDAFINFO:ID=655,TAIARRAY=1,TAIRNGARRAY=65535,EVENTIDS="LOAD_LEVEL_INFORMATION",NWDAFEVENTS="NF_LOAD"
` 


#### 修改NWDAF信息配置(SET SBINWDAFINFO) 
#### 修改NWDAF信息配置(SET SBINWDAFINFO) 


功能说明 

该命令用于修改NWDAF信息配置。当本地NRF配置中所配置的对端NFProfile携带的NWDAF信息需要变更时，使用该命令。命令执行成功后，修改后的NWDAF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

如果修改TAI信息，需要保证引用的如下配置已经存在： 


 
TAI组编号：通过命令SHOW SBITAIARRID查询。 

 
TAI范围组编号：通过命令SHOW SBITAIRANGEARRID查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




命令举例 


`
修改NWDAF信息配置：编号为655，TAI组编号为1，TAI范围组编号为1，分析服务支持的事件ID为："LOAD_LEVEL_INFORMATION"，订阅支持的事件为："NF_LOAD"。 
SET SBINWDAFINFO:ID=655,TAIARRAY=1,TAIRNGARRAY=1,EVENTIDS="LOAD_LEVEL_INFORMATION",NWDAFEVENTS="NF_LOAD"
` 


#### 删除NWDAF信息配置(DEL SBINWDAFINFO) 
#### 删除NWDAF信息配置(DEL SBINWDAFINFO) 


功能说明 

该命令用于删除NWDAF信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该NWDAF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该NWDAF信息。 


注意事项 

如果要删除该NWDAF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




命令举例 


`
删除NWDAF信息配置：编号为655。
DEL SBINWDAFINFO:ID=655
` 


#### 查询NWDAF信息配置(SHOW SBINWDAFINFO) 
#### 查询NWDAF信息配置(SHOW SBINWDAFINFO) 


功能说明 

该命令用于查询NWDAF信息配置。当需要查询对端NFProfile携带的NWDAF信息时，使用该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|NWDAF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置NWDAF信息编号，该编号是NWDAF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
EVENTIDS|分析服务支持的事件ID|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: LOAD_LEVEL_INFORMATION&NETWORK_PERFORMANCE&NF_LOAD&QOS_SUSTAINABILITY&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&USER_DATA_CONGESTION&ABNORMAL_BEHAVIOUR|该参数用于设置服务支持的事件ID，如果不配置，则NWDAF可以服务任何事件ID。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。分析服务支持的事件如下：LOAD_LEVEL_INFORMATION：网络切片实例的负载级别事件。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。
NWDAFEVENTS|订阅支持的事件|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NF_LOAD&QOS_SUSTAINABILITY&SLICE_LOAD_LEVEL&SERVICE_EXPERIENCE&UE_MOBILITY&UE_COMM&ABNORMAL_BEHAVIOUR&USER_DATA_CONGESTION&NETWORK_PERFORMANCE|该参数用于设置服务支持的事件，如果不配置，则NWDAF可以服务任何nwdafEvent。注意，如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选。支持的订阅事件如下：NF_LOAD：NF负载信息事件，针对特定NF或NF列表以及特定UE的NF负载分析信息。QOS_SUSTAINABILITY：QoS可持续性事件，对于任何UE，在特定区域和时间段内，报告QoS变化统计信息或预测QoS变化的可能性。SLICE_LOAD_LEVEL：网络切片实例的负载级别事件。SERVICE_EXPERIENCE：服务体验事件，针对特定UE或一组UE或任何UE的应用程序或具有给定应用程序或一组应用程序或任何应用程序的网络切片的服务体验。UE_MOBILITY：UE移动性事件，用于特定UE或一组UE的UE移动性信息。UE_COMM：UE通讯事件，用于特定UE或一组UE的UE通信信息。ABNORMAL_BEHAVIOUR：异常行为事件，针对特定UE或一组UE或任何UE的异常行为信息。USER_DATA_CONGESTION：用户数据拥塞事件，感兴趣区域中任何UE或特定UE的用户数据拥塞。NETWORK_PERFORMANCE：网络性能事件，感兴趣区域中的任何UE或特定UE或一组UE的网络性能。




命令举例 


`
查询NWDAF信息配置：NWDAF信息编号为655。
SHOW SBINWDAFINFO:ID=655

(No.5) : SHOW SBINWDAFINFO:ID=655
-----------------CommonS_HTTP_LB_0----------------
操作维护       NWDAF信息编号 TAI组编号 TAI范围组编号 分析服务支持的事件ID   订阅支持的事件 
-------------------------------------------------------------------------------------------
复制 修改 删除 655           1         1             LOAD_LEVEL_INFORMATION NF_LOAD        
-------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2021-01-29 15:05:03 耗时: 0.638 秒

` 


## PCF配置 
## PCF配置 


背景知识 


PCF（Policy Control Function，策略控制功能）是5G核心网中的网络实体，提供统一的策略框架和控制平面功能的策略规则。 

当服务提供者（对端）向NRF注册时，如果对端的NF（Network Function，网络功能）类型为PCF，注册请求中携带的对端NFProfile参数可以包含PCF信息（PcfInfo）参数，该参数又包含了一些通用或PCF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为PCF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的PCF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，PCF信息配置会呈现在对端NFProfile的PCF信息参数中。 




功能说明 


PCF配置为命令树目录，下面包含了PCF信息配置。PCF信息配置即对应本地NRF配置的对端NFProfile的PCF信息参数，如果不配置，则对端NFProfile缺少PCF信息参数，本端如果需要发现可用的对端PCF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该命令。 




子主题： 






### PCF信息配置 
### PCF信息配置 


背景知识 


PCF（Policy Control Function，策略控制功能）是5G核心网中的网络实体，提供统一的策略框架和控制平面功能的策略规则。 

当服务提供者（对端）向NRF注册时，如果对端的NF（Network Function，网络功能）类型为PCF，注册请求中携带的对端NFProfile参数可以包含PCF信息（PcfInfo）参数，该参数又包含了一些通用或PCF特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为PCF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的PCF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，PCF信息配置会呈现在对端NFProfile的PCF信息参数中。 




功能说明 


PCF信息配置即对应本地NRF配置的对端NFProfile的PCF信息参数，如果不配置，则对端NFProfile缺少PCF信息参数，本端如果需要发现可用的对端PCF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该命令。 




子主题： 






#### 新增PCF信息配置(ADD SBIPCFINFO) 
#### 新增PCF信息配置(ADD SBIPCFINFO) 


功能说明 

该命令用于新增PCF信息配置。当本地NRF配置中所配置的对端NFProfile需要携带PCF信息（例如：可以提供服务的DNN信息、GPSI范围信息以及SUPI范围信息等）时，使用该命令。命令执行成功后，PCF信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


注意事项 

如果要新增该PCF信息配置，需要保证引用的如下组编号已经存在： 


 
DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。 

 
GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。 

 
SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




命令举例 


`
增加PCF信息配置：编号为1，NF组编号为 1，DNN组编号为1，GPSI范围组编号为65535，SUPI范围组编号为65535，Rx口Diameter主机名为“nanjing.rx”，Rx口Diameter域名为“domain.nanjing”,是否支持V2X策略/参数为“是”。 
ADD SBIPCFINFO:ID=1,NFGROUPID=1,DNNARRAY=1,GPSIRANGEARRAY=65535,SUPIRANGEARRAY=65535,RXDIAMHOST=nanjing.rx,RXDIAMREALM=domain.nanjing,V2XSUPPORTED=YES
` 


#### 修改PCF信息配置(SET SBIPCFINFO) 
#### 修改PCF信息配置(SET SBIPCFINFO) 


功能说明 

该命令用于修改PCF信息配置。当本地NRF配置中所配置的对端NFProfile携带的PCF信息（例如：可以提供服务的DNN信息、GPSI范围信息以及SUPI范围信息等）需要变更时，使用该命令。命令执行成功后，修改后的PCF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

如果要修改PCF信息配置，需要保证引用的组编号已经存在： 


 
DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。 

 
GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。 

 
SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




命令举例 


`
修改PCF信息配置：编号为1，NF组编号为 1，DNN组编号为1，GPSI范围组编号为65535，SUPI范围组编号为65535，Rx口Diameter主机名为“nanjing.rx”，Rx口Diameter域名为“domain.nanjing”,是否支持V2X策略/参数为“否”。 
SET SBIPCFINFO:ID=1,NFGROUPID="1",DNNARRAY=1,GPSIRANGEARRAY=65535,SUPIRANGEARRAY=65535,RXDIAMHOST="nanjing.rx",RXDIAMREALM="domain.nanjing",V2XSUPPORTED="NO"
` 


#### 删除PCF信息配置(DEL SBIPCFINFO) 
#### 删除PCF信息配置(DEL SBIPCFINFO) 


功能说明 

该命令用于删除PCF信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该PCF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该PCF信息。 


注意事项 

如果要删除该PCF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




命令举例 


`
删除PCF信息配置：编号为1。
DEL SBIPCFINFO:ID=1
` 


#### 查询PCF信息配置(SHOW SBIPCFINFO) 
#### 查询PCF信息配置(SHOW SBIPCFINFO) 


功能说明 

该命令用于查询PCF信息配置。当需要查询对端NFProfile携带的PCF信息（例如：可以提供服务的DNN信息、GPSI范围信息以及SUPI范围信息等）时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|PCF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置PCF信息编号，该编号是PCF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
NFGROUPID|NF组编号|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置该PCF实例归属的PCF组标识。PCF组标识表示一组PCF实例。如果未配置，则该PCF实例不属于任何PCF组。该参数无特殊配置原则。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。该编号对应DNN信息，表示PCF实例可以为携带了这些DNN信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配DNN。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。该编号对应GPSI范围信息，表示PCF实例可以为携带了这些GPSI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配GPSI信息。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。该编号对应SUPI范围信息，表示PCF实例可以为携带了这些SUPI范围信息的服务消费者提供服务。如果未配置，则该PCF实例在提供服务时不匹配SUPI信息。
RXDIAMHOST|Rx口Diameter主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter主机名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter主机名。
RXDIAMREALM|Rx口Diameter域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置Rx口Diameter域名。如果该PCF实例支持Rx口，则该参数应当指示与PCF对接的Rx接口的Diameter域。
V2XSUPPORTED|是否支持V2X策略/参数|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持V2X（Vehicle To Everything，车对外界的信息交换）策略/参数。PCF使用AMF提供的服务，为UE和NG-RAN提供V2X服务相关参数，并使AMF能够创建或更新V2X服务相关的UE上下文。




命令举例 


`
查询PCF信息配置：PCF信息编号为1。
SHOW SBIPCFINFO:ID=1

(No.6) : SHOW SBIPCFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       PCF信息编号 NF组编号 DNN组编号 GPSI范围组编号 SUPI范围组编号 Rx口Diameter主机名 Rx口Diameter域名 是否支持V2X策略/参数 
-------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1           1        1         65535          65535          nanjing.rx         domain.nanjing   是                   
-------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 15:35:12 耗时: 0.673 秒

` 


## SMF配置 
## SMF配置 


背景知识 


SMF（Session Management Function，会话管理功能）是5G核心网中的网络实体，负责处理用户的业务，可以看成是MME承载管理部分以及SGW和PGW的控制面功能的组合。 

5G核心网中，SMF通过基于Nsmf服务的接口向AMF、其他SMF（V-SMF、H-SMF或I-SMF）、PCF和NEF提供以下服务： 


 
Nsmf_PDUSession：服务操作PDU会话，允许其他网元来建立，修改，释放PDU会话。 

 
Nsmf_EventExposure：其他NF订阅的事件通知服务。 

 
Nsmf_NIDD：传送非IP数据的服务。 

 




功能说明 


本地NRF功能中，SMF配置包括： 


 
SMF信息配置：配置具体的SMF信息，如：TAI信息、接入类型、优先级等。 

 
S-NSSAI SMF信息组配置：用于配置DNN组和S-NSSAI信息，对外提供SMF信息组编号，供SMF信息配置引用。 

 




子主题： 






### SMF信息配置 
### SMF信息配置 


背景知识 


SMF（Session Management Function，会话管理功能）是5G核心网中的网络实体，负责处理用户的业务，可以看成是MME承载管理部分以及SGW和PGW的控制面功能的组合。 

5G核心网中，SMF通过基于Nsmf服务的接口向AMF、其他SMF（V-SMF、H-SMF或I-SMF）、PCF和NEF提供以下服务： 


 
Nsmf_PDUSession：服务操作PDU会话，允许其他网元来建立，修改，释放PDU会话。 

 
Nsmf_EventExposure：其他NF订阅的事件通知服务。 

 
Nsmf_NIDD：传送非IP数据的服务。 

 




功能说明 


本地NRF功能中，当PCF、AMF等NF需要通过SBI-GW向SMF发送请求消息时，需要使用该配置。 

配置步骤如下： 



配置对端NF基本信息。 


根据SMF需要提供服务对象的DNN和S-NSSAI信息配置S-NSSAI SMF信息组。 


根据SMF需要提供的服务对象的TAI信息等配置SMF信息，并引用S-NSSAI SMF信息组编号。 


在对端NF扩展信息中关联该SMF。 






子主题： 






#### 新增SMF信息配置(ADD SBISMFINFO) 
#### 新增SMF信息配置(ADD SBISMFINFO) 


功能说明 

该命令用于新增SMF信息配置。当本地NRF配置中所配置的对端NFProfile需要携带SMF信息时，使用该命令。命令执行成功后，SMF信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


注意事项 

需要保证如下配置都已经存在： 


 
S-NSSAI SMF信息组编号配置：可以通过SHOW SBISNSSAISMFINFOARRID命令查询。 

 
TAI组编号配置：可以通过SHOW SBITAIARRID命令查询。 

 
TAI范围组编号配置：可以通过SHOW SBITAIRANGEARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（例如：3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




命令举例 


`
增加SMF信息配置：编号为1，S-NSSAI SMF信息组编号为1，TAI组编号为65535，TAI范围组编号为65535，接入类型为“所有接入类型”，PGW FQDN为"nanjing.snf"，优先级为1。 
ADD SBISMFINFO:ID=1,SNSSAISMFINFOARRAY=1,TAIARRAY=65535,TAIRNGARRAY=65535,ACCESSTYPE=ALL_ACCESS,PGWFQDN=nanjing.snf,PRIORITY=1
` 


#### 修改SMF信息配置(SET SBISMFINFO) 
#### 修改SMF信息配置(SET SBISMFINFO) 


功能说明 

该命令用于修改SMF信息配置。当本地NRF配置中所配置的对端NFProfile携带的SMF信息需要变更时，使用该命令。命令执行成功后，修改后的SMF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

如果要修改如下配置，则需要需要保证该配置都已经存在： 


 
S-NSSAI SMF信息组编号配置：可以通过SHOW SBISNSSAISMFINFOARRID命令查询。 

 
TAI组编号配置：可以通过SHOW SBITAIARRID命令查询。 

 
TAI范围组编号配置：可以通过SHOW SBITAIRANGEARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（例如：3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




命令举例 


`
修改SMF信息配置：编号为1，S-NSSAI SMF信息组编号为1，TAI组编号为65535，TAI范围组编号为65535，接入类型为“所有接入类型”，PGW FQDN为"nanjing.snf"，优先级为2。 
SET SBISMFINFO:ID=1,SNSSAISMFINFOARRAY=1,TAIARRAY=65535,TAIRNGARRAY=65535,ACCESSTYPE="ALL_ACCESS",PGWFQDN="nanjing.snf",PRIORITY=2
` 


#### 删除SMF信息配置(DEL SBISMFINFO) 
#### 删除SMF信息配置(DEL SBISMFINFO) 


功能说明 

该命令用于删除SMF信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该SMF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该SMF信息。 


注意事项 

如果要删除该SMF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（例如：3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




命令举例 


`
删除SMF信息配置：编号为1。
DEL SBISMFINFO:ID=1
` 


#### 查询SMF信息配置(SHOW SBISMFINFO) 
#### 查询SMF信息配置(SHOW SBISMFINFO) 


功能说明 

该命令用于查询SMF信息配置。当需要查询对端NFProfile携带的SMF信息时，使用该命令。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SMF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF信息编号。
SNSSAISMFINFOARRAY|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，该编号通过SHOW SBITAIARRID命令查询。
TAIRNGARRAY|TAI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI范围组编号，该编号通过SHOW SBITAIRANGEARRID命令查询。
ACCESSTYPE|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置SMF支持的接入类型（例如：3GPP_ACCESS和/或NON_3GPP_ACCESS），如果不配置，则两种访问类型都支持。
PGWFQDN|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置PGW FQDN，如果SMF是组合的SMF/PGW-C，则表示PGW的FQDN。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置优先级（相对于相同类型的其他NF），在0-65535的范围内，用于与SMF Info属性匹配的服务请求的NF选择；较低的值表示较高的优先级。




命令举例 


`
查询SMF信息配置：SMF信息编号为1。
SHOW SBISMFINFO:ID=1

(No.1) : SHOW SBISMFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       SMF信息编号 S-NSSAI SMF信息组编号 TAI组编号 TAI范围组编号 接入类型     PGW FQDN    优先级 
--------------------------------------------------------------------------------------------------------
复制 修改 删除 1           1                   65535     65535         所有接入类型 nanjing.snf 1      
--------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 15:33:30 耗时: 0.651 秒

` 


### S-NSSAI SMF信息组配置 
### S-NSSAI SMF信息组配置 


背景知识 


S-NSSAI SMF信息组为SMF信息配置的必选部分，包括： 


 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）：可以参见配置SHOW SBISNSSAI 

 
DNN（Data Network Name，数据网络名称）：可以参见配置SHOW SBIDNNARRID。 

 

本地NRF功能中，该配置以组编号的方式对外呈现，在SMF扩展信息配置中引用该组编号，用于表示该NF可以服务的DNN列表和S-NSSAI信息。SMF扩展信息配置可以通过配置[SHOW SBISMFINFO]命令查看。




功能说明 


本地NRF功能打开时，S-NSSAI SMF信息组是以一组数据配置呈现的，该组数据配置包括S-NSSAI SMF信息组编号配置和S-NSSAI SMF信息组参数配置，一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。 

S-NSSAI SMF信息组配置应用于SMF扩展信息配置中，用于表示该SMF可以服务的DNN列表和S-NSSAI信息。 




子主题： 






#### S-NSSAI SMF信息组编号配置 
#### S-NSSAI SMF信息组编号配置 


背景知识 


S-NSSAI SMF信息组为SMF信息配置的必选部分，包括： 


 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）：可以参见配置SHOW SBISNSSAI 

 
DNN（Data Network Name，数据网络名称）：可以参见配置SHOW SBIDNNARRID。 

 

本地NRF功能中，该配置以组编号的方式对外呈现，在SMF扩展信息配置中引用该组编号，用于表示该NF可以服务的DNN列表和S-NSSAI信息。SMF扩展信息配置可以通过配置[SHOW SBISMFINFO]命令查看。




功能说明 


S-NSSAI SMF信息组编号配置用于配置一个S-NSSAI SMF信息组，一个S-NSSAI SMF信息组包含了若干个S-NSSAI SMF信息组参数。 

当启用本地NRF功能时，如果要配置SMF扩展信息，则需要首先配置S-NSSAI SMF信息组编号。配置后，最终呈现在本地NRF配置的SMF扩展信息的S-NSSAI SMF信息组编号中。 




子主题： 






##### 新增S-NSSAI SMF信息组编号配置(ADD SBISNSSAISMFINFOARRID) 
##### 新增S-NSSAI SMF信息组编号配置(ADD SBISNSSAISMFINFOARRID) 


功能说明 

该命令用于新增S-NSSAI SMF信息组编号。当新增SMF扩展信息时，使用该命令。执行成功后，可以在SMF扩展信息配置中关联该S-NSSAI SMF信息组编号。SMF信息配置使用[ADD SBISMFINFO]命令。


注意事项 

必须先配置该S-NSSAI SMF信息组编号，才能在SMF扩展信息配置中引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI SMF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号。该编号全局唯一。S-NSSAI SMF信息组编号被以下配置引用：SMF扩展信息配置：用于表示该SMF可以服务的DNN列表和S-NSSAI信息。该配置可以使用SHOW SBISMFINFO命令查询。S-NSSAI SMF信息组参数配置：一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。S-NSSAI SMF信息组参数配置可以使用SHOW SBISNSSAISMFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号。该编号全局唯一。S-NSSAI SMF信息组编号被以下配置引用：SMF扩展信息配置：用于表示该SMF可以服务的DNN列表和S-NSSAI信息。该配置可以使用SHOW SBISMFINFO命令查询。S-NSSAI SMF信息组参数配置：一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。S-NSSAI SMF信息组参数配置可以使用SHOW SBISNSSAISMFINFOARRPARAM命令查询。




命令举例 


`
新增S-NSSAI SMF信息组编号配置：S-NSSAI SMF信息组编号为1。 
ADD SBISNSSAISMFINFOARRID:ARRAYID=1
` 


##### 删除S-NSSAI SMF信息组编号配置(DEL SBISNSSAISMFINFOARRID) 
##### 删除S-NSSAI SMF信息组编号配置(DEL SBISNSSAISMFINFOARRID) 


功能说明 

该命令用于删除S-NSSAI SMF信息组编号。当没有SMF扩展信息关联S-NSSAI SMF信息组编号时，可以执行该命令删除S-NSSAI SMF信息组编号。 


注意事项 

删除前需要把归属于该S-NSSAI SMF信息组编号的所有S-NSSAI SMF信息组参数配置删除。可以使用命令[SHOW SBISNSSAISMFINFOARRPARAM]指定S-NSSAI SMF信息组编号，查询归属于该S-NSSAI SMF信息组编号的所有S-NSSAI SMF信息组参数配置。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI SMF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号。该编号全局唯一。S-NSSAI SMF信息组编号被以下配置引用：SMF扩展信息配置：用于表示该SMF可以服务的DNN列表和S-NSSAI信息。该配置可以使用SHOW SBISMFINFO命令查询。S-NSSAI SMF信息组参数配置：一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。S-NSSAI SMF信息组参数配置可以使用SHOW SBISNSSAISMFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号。该编号全局唯一。S-NSSAI SMF信息组编号被以下配置引用：SMF扩展信息配置：用于表示该SMF可以服务的DNN列表和S-NSSAI信息。该配置可以使用SHOW SBISMFINFO命令查询。S-NSSAI SMF信息组参数配置：一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。S-NSSAI SMF信息组参数配置可以使用SHOW SBISNSSAISMFINFOARRPARAM命令查询。




命令举例 


`
删除S-NSSAI SMF信息组编号配置：S-NSSAI SMF信息组编号为1。
DEL SBISNSSAISMFINFOARRID:ARRAYID=1
` 


##### 查询S-NSSAI SMF信息组编号配置(SHOW SBISNSSAISMFINFOARRID) 
##### 查询S-NSSAI SMF信息组编号配置(SHOW SBISNSSAISMFINFOARRID) 


功能说明 

该命令用于查询S-NSSAI SMF信息组编号。查询时，可以指定S-NSSAI SMF信息组编号，查询成功后，会回显对应的S-NSSAI SMF信息组编号信息；如果不指定S-NSSAI SMF信息组编号，则回显已经配置的所有S-NSSAI SMF信息组编号信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号。该编号全局唯一。S-NSSAI SMF信息组编号被以下配置引用：SMF扩展信息配置：用于表示该SMF可以服务的DNN列表和S-NSSAI信息。该配置可以使用SHOW SBISMFINFO命令查询。S-NSSAI SMF信息组参数配置：一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。S-NSSAI SMF信息组参数配置可以使用SHOW SBISNSSAISMFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI SMF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号。该编号全局唯一。S-NSSAI SMF信息组编号被以下配置引用：SMF扩展信息配置：用于表示该SMF可以服务的DNN列表和S-NSSAI信息。该配置可以使用SHOW SBISMFINFO命令查询。S-NSSAI SMF信息组参数配置：一个S-NSSAI SMF信息组编号可以被若干个S-NSSAI SMF信息组参数引用。S-NSSAI SMF信息组参数配置可以使用SHOW SBISNSSAISMFINFOARRPARAM命令查询。




命令举例 


`
查询S-NSSAI SMF信息组编号配置：S-NSSAI SMF信息组编号为1。
SHOW SBISNSSAISMFINFOARRID:ARRAYID=1

(No.4) : SHOW SBISNSSAISMFINFOARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       S-NSSAI SMF信息组编号 
-----------------------------------
复制 删除      1                   
-----------------------------------
记录数：1
执行成功 开始时间:2020-12-15 15:34:18 耗时: 0.625 秒

` 


#### S-NSSAI SMF信息组参数配置 
#### S-NSSAI SMF信息组参数配置 


背景知识 


S-NSSAI SMF信息组为SMF信息配置的必选部分，包括： 


 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）：可以参见配置SHOW SBISNSSAI 

 
DNN（Data Network Name，数据网络名称）：可以参见配置SHOW SBIDNNARRID。 

 

本地NRF功能中，该配置以组编号的方式对外呈现，在SMF扩展信息配置中引用该组编号，用于表示该NF可以服务的DNN列表和S-NSSAI信息。SMF扩展信息配置可以通过配置[SHOW SBISMFINFO]命令查看。




功能说明 


S-NSSAI SMF信息组参数配置用于配置DNN组和S-NSSAI的具体信息以及该S-NSSAI SMF信息组参数归属于哪个S-NSSAI SMF信息组编号。其中： 


 
DNN组编号可以通过SHOW SBIDNNARRID命令查询。 

 
S-NSSAI编号可以通过SHOW SBISNSSAI命令查询。 

 
S-NSSAI SMF信息组可以通过SHOW SBISNSSAISMFINFOARRID命令查询。 

 

配置完成后，在SMF扩展信息中引用该S-NSSAI SMF信息组参数归属的S-NSSAI SMF信息组编号。如果不配置S-NSSAI SMF信息组参数，则无法配置具体的S-NSSAI SMF信息，已经配置的S-NSSAI SMF信息组编号只能是一个孤立配置。如果SMF扩展信息配置中引用了该S-NSSAI SMF信息组编号，那么在组装NFProfile时会失败。 




子主题： 






##### 新增S-NSSAI SMF信息组参数配置(ADD SBISNSSAISMFINFOARRPARAM) 
##### 新增S-NSSAI SMF信息组参数配置(ADD SBISNSSAISMFINFOARRPARAM) 


功能说明 

该命令用于新增S-NSSAI SMF信息组参数配置。当SMF已配置可以服务的S-NSSAI SMF信息组编号，需要新增归属于该S-NSSAI SMF信息组编号的参数时，使用该命令。执行成功后，SMF新增了可以服务的该S-NSSAI SMF信息组参数的DNN和S-NSSAI信息。 


注意事项 

需要保证如下配置都已经存在： 


 
S-NSSAI SMF信息组编号配置：可以通过SHOW SBISNSSAISMFINFOARRID命令查询。 

 
S-NSSAI编号配置：可以通过SHOW SBISNSSAI命令查询。 

 
DNN组编号配置：可以通过SHOW SBIDNNARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
新增S-NSSAI SMF信息组参数配置：配置索引为1，S-NSSAI SMF信息组编号为1，S-NSSAI编号为1，DNN组编号1。 
ADD SBISNSSAISMFINFOARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=1,DNNARRAY=1
` 


##### 修改S-NSSAI SMF信息组参数配置(SET SBISNSSAISMFINFOARRPARAM) 
##### 修改S-NSSAI SMF信息组参数配置(SET SBISNSSAISMFINFOARRPARAM) 


功能说明 

该命令用于修改S-NSSAI SMF信息组参数配置。当SMF已配置可以服务的S-NSSAI SMF信息组编号，需要修改归属于该S-NSSAI SMF信息组编号的参数时，使用该命令。执行成功后，SMF新修改了可以服务的该S-NSSAI SMF信息组参数的DNN和S-NSSAI信息。 


注意事项 

如果是修改如下配置项，则需要保证如下配置都已经存在： 


 
S-NSSAI SMF信息组编号配置：可以通过SHOW SBISNSSAISMFINFOARRID命令查询。 

 
S-NSSAI编号配置：可以通过SHOW SBISNSSAI命令查询。 

 
DNN组编号配置：可以通过SHOW SBIDNNARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
修改S-NSSAI SMF信息组参数配置：配置索引为1，S-NSSAI SMF信息组编号为1，S-NSSAI编号为65535，DNN组编号65535。  
SET SBISNSSAISMFINFOARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=65535,DNNARRAY=65535
` 


##### 删除S-NSSAI SMF信息组参数配置(DEL SBISNSSAISMFINFOARRPARAM) 
##### 删除S-NSSAI SMF信息组参数配置(DEL SBISNSSAISMFINFOARRPARAM) 


功能说明 

该命令用于删除S-NSSAI SMF信息组参数配置。当SMF已配置可以服务的S-NSSAI SMF信息组编号，需要删除归属于该S-NSSAI SMF信息组编号的参数时，使用该命令。执行成功后，SMF删除了可以服务的该范围组参数的DNN和S-NSSAI信息。 


注意事项 

如果归属于某个S-NSSAI SMF信息组编号的所有S-NSSAI SMF信息组参数配置都已经删除，建议删除该S-NSSAI SMF信息组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
删除S-NSSAI SMF信息组参数配置：配置索引为1。
DEL SBISNSSAISMFINFOARRPARAM:INDEX=1
` 


##### 查询S-NSSAI SMF信息组参数配置(SHOW SBISNSSAISMFINFOARRPARAM) 
##### 查询S-NSSAI SMF信息组参数配置(SHOW SBISNSSAISMFINFOARRPARAM) 


功能说明 

该命令用于查询S-NSSAI SMF信息组参数配置。当需要查询已经配置的S-NSSAI SMF信息组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会回显对应的配置信息；如果不指定配置索引，则回显已经配置的所有S-NSSAI SMF信息组参数信息。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引。该索引全局唯一。
ARRAYID|S-NSSAI SMF 信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI SMF信息组编号，该编号通过SHOW SBISNSSAISMFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号，该编号通过SHOW SBISNSSAI命令查询。
DNNARRAY|DNN组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN组编号，该编号通过SHOW SBIDNNARRID命令查询。




命令举例 


`
查询S-NSSAI SMF信息组参数配置：配置索引为1。
SHOW SBISNSSAISMFINFOARRPARAM:INDEX=1

(No.5) : SHOW SBISNSSAISMFINFOARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 S-NSSAI SMF信息组编号 S-NSSAI编号 DNN组编号 
---------------------------------------------------------------------
复制 修改 删除 1        1                   65535        65535     
---------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 15:34:35 耗时: 0.61 秒

` 


## UDM配置 
## UDM配置 


背景知识 


当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF（网络功能，Network Function）类型为UDM（统一数据管理，Unified Data Management ），注册请求中携带的对端NFProfile参数可以包含UDM信息（UdmInfo）参数，该参数又包含了一些通用或UDM特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为UDM时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的UDM信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，UDM信息配置会呈现在对端NFProfile的UDM信息参数中。 




功能说明 


UDM配置为命令树目录，下面包含了UDM信息配置。UDM信息配置即对应本地NRF配置的对端NFProfile的UDM信息参数，如果不配置，则对端NFProfile缺少UDM信息参数，本端如果需要发现可用的对端UDM时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### UDM信息配置 
### UDM信息配置 


背景知识 


当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF（网络功能，Network Function）类型为UDM（统一数据管理，Unified Data Management ），注册请求中携带的对端NFProfile参数可以包含UDM信息（UdmInfo）参数，该参数又包含了一些通用或UDM特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为UDM时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的UDM信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，UDM信息配置会呈现在对端NFProfile的UDM信息参数中。 




功能说明 


UDM信息配置即对应本地NRF配置的对端NFProfile的UDM信息参数，如果不配置，则对端NFProfile缺少UDM信息参数，本端如果需要发现可用的对端UDM时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增UDM信息配置(ADD SBIUDMINFO) 
#### 新增UDM信息配置(ADD SBIUDMINFO) 


功能说明 

本命令用于新增UDM信息。当本地NRF配置中所配置的对端NFProfile需要携带UDM信息时，使用该命令。命令执行成功后，UDM信息编号可以被对端NF扩展信息配置引用。 


注意事项 

系统支持的该配置项最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
增加UDM信息配置：编号为1，GPSI范围组编号为1。 
ADD SBIUDMINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 修改UDM信息配置(SET SBIUDMINFO) 
#### 修改UDM信息配置(SET SBIUDMINFO) 


功能说明 

本命令用于修改UDM信息。当本地NRF配置中所配置的对端NFProfile携带的UDM信息需要变更时，使用该命令。命令执行成功后，修改后的UDM信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

修改UDM信息，需要保证UDM信息编号已经存在，该编号通过[SHOW SBIUDMINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
修改UDM信息配置：编号为1，GPSI范围组编号为1。 
SET SBIUDMINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 删除UDM信息配置(DEL SBIUDMINFO) 
#### 删除UDM信息配置(DEL SBIUDMINFO) 


功能说明 

本命令用于删除UDM信息。当本地NRF配置中所配置的对端NFProfile不需要携带该UDM信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该UDM信息。 


注意事项 

如果要删除该UDM信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
删除UDM信息配置：编号为1。
DEL SBIUDMINFO:ID=1
` 


#### 查询UDM信息配置(SHOW SBIUDMINFO) 
#### 查询UDM信息配置(SHOW SBIUDMINFO) 


功能说明 

本命令用于查询UDM信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDM信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDM信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDM的标识符。如果不配置，则该UDM不属于任何UDM组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDM可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDM可以为任何GPSI服务。
ROUTINDARRAY|路由指示组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置路由指示组编号，该编号通过SHOW SBIROUTINDARRID命令查询。当本地NRF功能处理服务发现请求时，会比较发现请求中的路由指示器是否与配置的路由指示组一致，如果一致则认为匹配成功。




命令举例 


`
查询UDM信息配置：编号为1。
SHOW SBIUDMINFO:ID=1

(No.11) : SHOW SBIUDMINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       UDM信息编号 NF组标识 SUPI范围组编号 GPSI范围组编号 路由指示组编号
--------------------------------------------------------------------------------
复制 修改 删除 1                                   5                            
--------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-17 20:22:57 耗时: 0.611 秒

` 


## UDR配置 
## UDR配置 


背景知识 


当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF(网络功能，Network Function)类型为UDR（统一数据仓库，Unified Data Repository），注册请求中携带的对端NFProfile参数可以包含UDR信息（UdrInfo）参数，该参数又包含了一些通用或UDR特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为UDR时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的UDR信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，UDR信息配置会呈现在对端NFProfile的UDR信息参数中。 




功能说明 


UDR配置为命令树目录，下面包含了UDR信息配置。UDR信息配置即对应本地NRF配置的对端NFProfile的UDR信息参数，如果不配置，则对端NFProfile缺少UDR信息参数，本端如果需要发现可用的对端UDR时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### UDR信息配置 
### UDR信息配置 


背景知识 


当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF(网络功能，Network Function)类型为UDR（统一数据仓库，Unified Data Repository），注册请求中携带的对端NFProfile参数可以包含UDR信息（UdrInfo）参数，该参数又包含了一些通用或UDR特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为UDR时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的UDR信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，UDR信息配置会呈现在对端NFProfile的UDR信息参数中。 




功能说明 


UDR信息配置即对应本地NRF配置的对端NFProfile的UDR信息参数，如果不配置，则对端NFProfile缺少UDR信息参数，本端如果需要发现可用的对端UDR时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增UDR信息配置(ADD SBIUDRINFO) 
#### 新增UDR信息配置(ADD SBIUDRINFO) 


功能说明 

本命令用于新增UDR信息。当本地NRF配置中所配置的对端NFProfile需要携带UDR信息时，使用该命令。命令执行成功后，UDR信息编号可以被对端NF扩展信息配置引用。 


注意事项 

系统支持的该配置项最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




命令举例 


`
增加UDR信息配置：编号为1，GPSI范围组编号为1。 
ADD SBIUDRINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 修改UDR信息配置(SET SBIUDRINFO) 
#### 修改UDR信息配置(SET SBIUDRINFO) 


功能说明 

本命令用于修改UDR信息。当本地NRF配置中所配置的对端NFProfile携带的UDR信息需要变更时，使用该命令。命令执行成功后，修改后的UDR信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

修改UDR信息，需要保证UDR信息编号已经存在，该编号通过[SHOW SBIUDRINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




命令举例 


`
修改UDR信息配置：编号为1，GPSI范围组编号为1。 
SET SBIUDRINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 删除UDR信息配置(DEL SBIUDRINFO) 
#### 删除UDR信息配置(DEL SBIUDRINFO) 


功能说明 

本命令用于删除UDR信息。当本地NRF配置中所配置的对端NFProfile不需要携带该UDR信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该UDR信息。 


注意事项 

如果要删除该UDR信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




命令举例 


`
删除UDR信息配置：编号为1。
DEL SBIUDRINFO:ID=1
` 


#### 查询UDR信息配置(SHOW SBIUDRINFO) 
#### 查询UDR信息配置(SHOW SBIUDRINFO) 


功能说明 

本命令用于查询UDR信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UDR信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UDR信息编号。该编号全局唯一。
GROUPID|NF组标识|参数可选性: 任选参数类型: 字符串参数范围: 1-127|该参数用于设置NF组标识，NF组标识是一组UDR的标识符。如果不配置，则该UDR不属于任何UDR组。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该UDR可以为任何SUPI服务。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该UDR可以为任何GPSI服务。
SUPPDATASETARRAY|支持的数据集组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置支持的数据集组编号，该编号通过SHOW SBIDATASETARRID命令查询。如果不配置，则该UDR可以支持所有数据集。




命令举例 


`
查询UDR信息配置：编号为1。
SHOW SBIUDRINFO:ID=1

(No.2) : SHOW SBIUDRINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       UDR信息编号 NF组标识 SUPI范围组编号 GPSI范围组编号 支持的数据集组编号 
------------------------------------------------------------------------------------
复制 修改 删除 1           1        1                                                                   
------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-11-19 15:37:06 耗时: 0.607 秒

` 


## UPF配置 
## UPF配置 


背景知识 


UPF（User Plane Function，用户平面功能）是5G核心网中的网络实体，相当于SGW和PGW的用户面功能的集合，可提供数据分流及流量统计、IP报文的分片与重组、用户数据跟踪等功能。 

当服务提供者（对端）向NRF注册时，如果对端的NF（Network Function，网络功能）类型为UPF，那么注册请求中携带的对端NFProfile参数可以包含UPF信息（UPFInfo）参数，该参数又包含了一些通用或UPF特有的参数。 

当服务使用者（本端）向NRF请求发现可用的服务提供者（对端），并且对端的NF类型为UPF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的UPF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，UPF信息配置会呈现在对端NFProfile的UPF信息参数中。 




功能说明 


UPF配置为命令树目录，下面包含了UPF信息配置和UPF相关的S-NSSAI UPF信息组配置、SMF服务区域组配置、UPF接口信息组配置、DNAI组配置和DNN UPF信息组配置。UPF信息配置即对应本地NRF配置的对端NFProfile的UPF信息参数，如果不配置，则对端NFProfile缺少UPF信息参数，本端如果需要发现可用的对端UPF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### UPF信息配置 
### UPF信息配置 


背景知识 


UPF（User Plane Function，用户平面功能）是5G核心网中的网络实体，相当于SGW和PGW的用户面功能的集合，可提供数据分流及流量统计、IP报文的分片与重组、用户数据跟踪等功能。 

当服务提供者（对端）向NRF注册时，如果对端的NF（Network Function，网络功能）类型为UPF，那么注册请求中携带的对端NFProfile参数可以包含UPF信息（UPFInfo）参数，该参数又包含了一些通用或UPF特有的参数。 

当服务使用者（本端）向NRF请求发现可用的服务提供者（对端），并且对端的NF类型为UPF时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的UPF信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，UPF信息配置会呈现在对端NFProfile的UPF信息参数中。 




功能说明 


UPF信息配置即对应本地NRF配置的对端NFProfile的UPF信息参数，如果不配置，则对端NFProfile缺少UPF信息参数，本端如果需要发现可用的对端UPF时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增UPF信息配置(ADD SBIUPFINFO) 
#### 新增UPF信息配置(ADD SBIUPFINFO) 


功能说明 

该命令用于新增UPF信息配置。当本地NRF配置中所配置的对端NFProfile需要携带UPF信息时，使用该命令。命令执行成功后，UPF信息编号可以被对端NF扩展信息配置引用。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


注意事项 

如果要新增该UPF信息配置，需要先新增S-NSSAI UPF信息组编号配置。S-NSSAI UPF信息组编号通过[SHOW SBISNSSAIUPFINFOARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




命令举例 


`
新增UPF信息配置：UPF信息编号为1，S-NSSAI UPF信息组编号为1，SMF服务区域组编号为1，UPF接口信息组编号为1，是否支持与EPS协作为"是"，PDU会话类型为"IPV4"，是否支持ATSSS-LL为"是"，是否支持MPTCP为"是"，是否支持UE IP地址/前缀分配为"是"，TAI组编号为1，W-AGF IPv4地址组编号为1，W-AGF IPv6地址组编号为1，W-AGF FQDN为"wagf1.com"，TNGF IPv4地址组编号为1，TNGF IPv6地址组编号为1，TNGF FQDN为"tngf1.com"，TWIF IPv4地址组编号为1，TWIF IPv6地址组编号为1，TWIF FQDN为"twif1.com"，优先级为1，是否支持GTP-U冗余路径为"是"。
ADD SBIUPFINFO:ID=1,SNSSAIUPFARRAY=1,SMFSRVAREAARRAY=1,UPFITFARRAY=1,IWKEPSIND="YES",PDUSESSTYPE="IPV4",ATSSSLL="YES",MPTCP="YES",UEIPADDRIND="YES",TAIARRAY=1,WAGFIPV4ARRAY=1,WAGFIPV6ARRAY=1,WAGFFQDN="wagf1.com",TNGFIPV4ARRAY=1,TNGFIPV6ARRAY=1,TNGFFQDN="tngf1.com",TWIFIPV4ARRAY=1,TWIFIPV6ARRAY=1,TWIFFQDN="twif1.com",PRIORITY=1,SUPREDUNDANTGTPU="YES";
` 


#### 修改UPF信息配置(SET SBIUPFINFO) 
#### 修改UPF信息配置(SET SBIUPFINFO) 


功能说明 

该命令用于修改UPF信息配置。当本地NRF配置中所配置的对端NFProfile携带的UPF信息需要变更时，使用该命令。命令执行成功后，修改后的UPF信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




命令举例 


`
修改UPF信息配置：UPF信息编号为1，S-NSSAI UPF信息组编号为1，SMF服务区域组编号为1，UPF接口信息组编号为1，是否支持与EPS协作为"是"，PDU会话类型为"IPV4"，是否支持ATSSS-LL为"是"，是否支持MPTCP为"是"，是否支持UE IP地址/前缀分配为"是"，TAI组编号为1，W-AGF IPv4地址组编号为1，W-AGF IPv6地址组编号为1，W-AGF FQDN为"wagf1.com"，TNGF IPv4地址组编号为1，TNGF IPv6地址组编号为1，TNGF FQDN为"tngf1.com"，TWIF IPv4地址组编号为1，TWIF IPv6地址组编号为1，TWIF FQDN为"twif1.com"，优先级为1，是否支持GTP-U冗余路径为"是"。
SET SBIUPFINFO:ID=1,SNSSAIUPFARRAY=1,SMFSRVAREAARRAY=1,UPFITFARRAY=1,IWKEPSIND="YES",PDUSESSTYPE="IPV4",ATSSSLL="YES",MPTCP="YES",UEIPADDRIND="YES",TAIARRAY=1,WAGFIPV4ARRAY=1,WAGFIPV6ARRAY=1,WAGFFQDN="wagf1.com",TNGFIPV4ARRAY=1,TNGFIPV6ARRAY=1,TNGFFQDN="tngf1.com",TWIFIPV4ARRAY=1,TWIFIPV6ARRAY=1,TWIFFQDN="twif1.com",PRIORITY=1,SUPREDUNDANTGTPU="YES";
` 


#### 删除UPF信息配置(DEL SBIUPFINFO) 
#### 删除UPF信息配置(DEL SBIUPFINFO) 


功能说明 

该命令用于删除UPF信息配置。当本地NRF配置中所配置的对端NFProfile不需要携带该UPF信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该UPF信息。 


注意事项 

如果要删除该UPF信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




命令举例 


`
删除UPF信息配置：UPF信息编号为1。
DEL SBIUPFINFO:ID=1;
` 


#### 查询UPF信息配置(SHOW SBIUPFINFO) 
#### 查询UPF信息配置(SHOW SBIUPFINFO) 


功能说明 

该命令用于查询UPF信息配置。当需要查询对端NFProfile携带的UPF信息时，使用该命令。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|UPF信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF信息编号，该编号是UPF信息配置的唯一标识，被对端NF扩展信息配置所引用。对端NF扩展信息配置通过SHOW SBIPEERNFEXTINFO命令查询。
SNSSAIUPFARRAY|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，表示UPF所支持的每个S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的参数列表。如果UPF信息配置和NFProfile中都存在此S-NSSAI时，则以UPF信息配置中的S-NSSAI为准。该参数引用了S-NSSAI UPF信息组编号配置，可以通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SMFSRVAREAARRAY|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SMF服务区域组编号，表示UPF可以为之提供服务的一组SMF服务区域。如果未设置，UPF可以为任何SMF服务区域提供服务。该参数引用了SMF服务区域组编号配置，可以通过SHOW SBISMFSRVAREAARRID命令查询。
UPFITFARRAY|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置UPF接口信息组编号，表示在UPF上配置的用户平面接口列表。当NRF返回的服务发现响应消息中携带了一组UPF接口信息时，NF服务使用者（例如，SMF）可以将该UPF接口信息用于UPF选择。该参数引用了UPF接口信息组编号配置，可以通过SHOW SBIUPFITFINFOARRID命令查询。
IWKEPSIND|是否支持与EPS协作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持与EPS（Evolved Packet System，演进的分组系统）互通。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示UPF可以选择任何PDU会话类型。IPV4：支持PDU会话的类型为IPv4。IPV6：支持PDU会话的类型为IPv6。IPV4V6：支持PDU会话的类型为IPv4和IPv6。UNSTRUCTURED：支持PDU会话的类型为非结构化。ETHERNET：支持PDU会话的类型为以太网。
ATSSSLL|是否支持ATSSS-LL|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持ATSSS-LL（ATSSS Low-Layer，ATSSS低层）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
MPTCP|是否支持MPTCP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持MPTCP（Multi-Path TCP Protocol，支持多路径TCP协议）功能，该功能与接入流量导向、交换、拆分（ATSSS）的过程有关。
UEIPADDRIND|是否支持UE IP地址/前缀分配|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持分配UE（User Equipment，用户设备）的IP地址/前缀。
TAIARRAY|TAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TAI组编号，表示UPF可以服务的TAI（Tracking Area Identity，跟踪区标识）列表。如果未设置，UPF可以为整个SMF服务区域服务，该SMF服务区域由SMF服务区域组定义。该参数引用了TAI组编号配置，可以通过SHOW SBITAIARRID命令查询。
WAGFIPV4ARRAY|W-AGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv4地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
WAGFIPV6ARRAY|W-AGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置W-AGF IPv6地址组编号，表示W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
WAGFFQDN|W-AGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置W-AGF（Wireline Access Gateway Function，有线接入网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TNGFIPV4ARRAY|TNGF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv4地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TNGFIPV6ARRAY|TNGF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TNGF IPv6地址组编号，表示TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TNGFFQDN|TNGF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TNGF（Trusted Non-3GPP Gateway Function，可信非3GPP网关功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
TWIFIPV4ARRAY|TWIF IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv4地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv4地址。该参数引用了IPv4地址组编号配置，可以通过SHOW SBIIPV4ADDRARRID命令查询。
TWIFIPV6ARRAY|TWIF IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置TWIF IPv6地址组编号，表示TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的一组N3终端的可用端点IPv6地址。该参数引用了IPv6地址组编号配置，可以通过SHOW SBIIPV6ADDRARRID命令查询。
TWIFFQDN|TWIF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置TWIF（Trusted WLAN Interworking Function，可信WLAN互通功能）数据中的N3终端的可用端点的FQDN（Fully Qualified Domain Name，全称域名）。
PRIORITY|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|该参数用于设置UPF的优先级（相对于同类型的其他NF），如果有多个不同的NFProfile，其中UPF信息的优先级不同，则服务使用者根据该参数选择优先级最高的UPF信息。
SUPREDUNDANTGTPU|是否支持GTP-U冗余路径|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否支持GTP-U（GPRS Tunneling Protocol User Plane，GPRS隧道协议用户面）冗余路径。




命令举例 


`
查询UPF信息配置：UPF信息编号为1。
SHOW SBIUPFINFO:ID=1

(No.1) : SHOW SBIUPFINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       UPF信息编号 S-NSSAI UPF信息组编号 SMF服务区域组编号 UPF接口信息组编号 是否支持与EPS协作 PDU会话类型                   是否支持ATSSS-LL 是否支持MPTCP 是否支持UE IP地址/前缀分配 TAI组编号 W-AGF IPv4地址组编号 W-AGF IPv6地址组编号 W-AGF FQDN TNGF IPv4地址组编号 TNGF IPv6地址组编号 TNGF FQDN TWIF IPv4地址组编号 TWIF IPv6地址组编号 TWIF FQDN 优先级 是否支持GTP-U冗余路径 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1           1                     1                 1                 是                IPV4&IPV6&IPV4V6&UNSTRUCTURED 是               是            是                         1         1                   1                   wagf1.com 1                   1                   tngf1.com 1                   1                   twif1.com 1      是                    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:08:38 耗时: 0.583 秒

` 


### SMF服务区域组配置 
### SMF服务区域组配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，SMF与发现的UPF进行通信。SMF服务区域表示UPF可以服务的SMF服务区域。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。该配置用于限定UPF可以服务的SMF服务区域列表。服务使用者（本端）会携带用户当前的SMF服务区域信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的SMF服务区域与对端NFProfile所配置的SMF服务区域列表进行比较，找到匹配的SMF服务区域时，就认为发现UPF成功。如果没有配置SMF服务区域组，则UPF无法设置相应的SMF服务区域列表，从而表示UPF可以服务于任何SMF服务区域，会为服务使用者提供所有的UPF。在本地NRF功能开启时，SMF服务区域配置会呈现在UPF信息配置的smfServingArea数组中。 




功能说明 


本地NRF功能打开时，SMF服务区域组是以一组数据配置呈现的，该组数据配置包括SMF服务区域组编号配置和SMF服务区域组参数配置，一个SMF服务区域组编号可以被若干个SMF服务区域组参数引用。 

SMF服务区域组配置应用于UPF扩展信息配置中，用于表示该UPF可以服务的SMF服务区域。 




子主题： 






#### SMF服务区域组编号配置 
#### SMF服务区域组编号配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，SMF与发现的UPF进行通信。SMF服务区域表示UPF可以服务的SMF服务区域。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。该配置用于限定UPF可以服务的SMF服务区域本列表。服务使用者（本端）会携带用户当前的SMF服务区域信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的SMF服务区域与对端NFProfile所配置的SMF服务区域列表进行比较，找到匹配的SMF服务区域时，就认为发现UPF成功。如果没有配置SMF服务区域组，则UPF无法设置相应的SMF服务区域列表，从而表示UPF可以服务于任何SMF服务区域，会为服务使用者提供所有的UPF。在本地NRF功能开启时，SMF服务区域配置会呈现在UPF信息配置的smfServingArea数组中。 
SMF服务区域组数据配置包括SMF服务区域组编号配置和SMF服务区域组参数配置。 




功能说明 


SMF服务区域组编号配置用于配置一个SMF服务区域组，一个SMF服务区域组包含了若干个SMF服务区域组参数。 

当启用本地NRF功能时，如果UPF扩展信息需要增加可以服务的SMF服务区域列表，则需要新增该组编号配置。SMF服务区域组编号配置后，可以被多个SMF服务区域组参数引用，从而组成一组SMF服务区域信息。最终SMF服务区域组编号可以被UPF信息配置所引用。 




子主题： 






##### 新增SMF服务区域组编号配置(ADD SBISMFSRVAREAARRID) 
##### 新增SMF服务区域组编号配置(ADD SBISMFSRVAREAARRID) 


功能说明 

该命令用于新增SMF服务区域组编号配置。当UPF信息配置需要携带一组SMF服务区域列表时，使用该命令。 

命令执行成功后，SMF服务区域组编号可以被“SMF服务区域组参数配置”及“UPF信息配置”引用。 


注意事项 

必须先配置该SMF服务区域组编号，才能在“SMF服务区域组参数配置”及“UPF信息配置”中引用。 


 
使用命令SHOW SBISMFSRVAREAARRPARAM查询“SMF服务区域组参数配置”。 

 
使用命令SHOW SBIUPFINFO查询“UPF信息配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SMF服务区域组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号，该编号是SMF服务区域组编号配置的唯一标识，被“SMF服务区域组参数配置”及“UPF信息配置”引用。“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号，该编号是SMF服务区域组编号配置的唯一标识，被“SMF服务区域组参数配置”及“UPF信息配置”引用。“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
新增SMF服务区域组编号配置：SMF服务区域组编号为1。 
ADD SBISMFSRVAREAARRID:ARRAYID=1
` 


##### 删除SMF服务区域组编号配置(DEL SBISMFSRVAREAARRID) 
##### 删除SMF服务区域组编号配置(DEL SBISMFSRVAREAARRID) 


功能说明 

该命令用于删除SMF服务区域组编号配置。当该组SMF服务区域列表不被任何UPF信息配置所引用时，建议使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该SMF服务区域组编号配置，需要先删除引用该配置的“SMF服务区域组参数配置”，并在“UPF信息配置”中将引用该配置的参数值设置为0来删除引用关系。 

<
 
“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询，通过DEL SBISMFSRVAREAARRPARAM命令进行删除。 

 
“UPF信息配置”通过SHOW SBIUPFINFO命令查询，通过SET SBIUPFINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SMF服务区域组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号，该编号是SMF服务区域组编号配置的唯一标识，被“SMF服务区域组参数配置”及“UPF信息配置”引用。“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号，该编号是SMF服务区域组编号配置的唯一标识，被“SMF服务区域组参数配置”及“UPF信息配置”引用。“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
删除SMF服务区域组编号配置：SMF服务区域组编号为1。
DEL SBISMFSRVAREAARRID:ARRAYID=1
` 


##### 查询SMF服务区域组编号配置(SHOW SBISMFSRVAREAARRID) 
##### 查询SMF服务区域组编号配置(SHOW SBISMFSRVAREAARRID) 


功能说明 

该命令用于查询SMF服务区域组编号配置。当配置SMF服务区域组参数及UPF信息时，需要获取已配置的SMF服务区域组编号，此时可执行该命令查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号，该编号是SMF服务区域组编号配置的唯一标识，被“SMF服务区域组参数配置”及“UPF信息配置”引用。“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号，该编号是SMF服务区域组编号配置的唯一标识，被“SMF服务区域组参数配置”及“UPF信息配置”引用。“SMF服务区域组参数配置”通过SHOW SBISMFSRVAREAARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
查询SMF服务区域组编号配置：SMF服务区域组编号为1。
SHOW SBISMFSRVAREAARRID:ARRAYID=1

(No.1) : SHOW SBISMFSRVAREAARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       SMF服务区域组编号 
---------------------------------
复制 删除      1                 
---------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:31:42 耗时: 0.627 秒

` 


#### SMF服务区域组参数配置 
#### SMF服务区域组参数配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，SMF与发现的UPF进行通信。SMF服务区域表示UPF可以服务的SMF服务区域。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。该配置用于限定UPF可以服务的SMF服务区域本列表。服务使用者（本端）会携带用户当前的SMF服务区域信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的SMF服务区域与对端NFProfile所配置的SMF服务区域列表进行比较，找到匹配的SMF服务区域时，就认为发现UPF成功。如果没有配置SMF服务区域组，则UPF无法设置相应的SMF服务区域列表，从而表示UPF可以服务于任何SMF服务区域，会为服务使用者提供所有的UPF。在本地NRF功能开启时，SMF服务区域配置会呈现在UPF信息配置的smfServingArea数组中。 
SMF服务区域组数据配置包括SMF服务区域组编号配置和SMF服务区域组参数配置。 




功能说明 


SMF服务区域组参数配置用于配置一个SMF服务区域归属于哪个SMF服务区域组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在UPF扩展信息配置中引用该SMF服务区域组参数归属的SMF服务区域组编号。如果不配置SMF服务区域组参数，则无法配置具体的SMF服务区域，已经配置的SMF服务区域组编号只能是一个孤立配置。如果没有配置SMF服务区域组参数的SMF服务区域组被“UPF信息配置”引用后，会导致组装NFProfile失败。 




子主题： 






##### 新增SMF服务区域组参数配置(ADD SBISMFSRVAREAARRPARAM) 
##### 新增SMF服务区域组参数配置(ADD SBISMFSRVAREAARRPARAM) 


功能说明 

该命令用于新增SMF服务区域组参数配置。当需要新增UPF可支持的SMF服务区域列表时，使用该命令配置SMF服务区域组参数，该参数配置SMF服务区域信息及其归属的SMF服务区域组。 


注意事项 

如果要新增该SMF服务区域组参数配置，需要先新增“SMF服务区域组编号配置”。 

“SMF服务区域组编号配置”通过[ADD SBISMFSRVAREAARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 必选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




命令举例 


`
新增SMF服务区域组参数配置：配置索引为1，SMF服务区域组编号为1，服务区域为"01"。 
ADD SBISMFSRVAREAARRPARAM:INDEX=1,ARRAYID=1,AREA="01"
` 


##### 修改SMF服务区域组参数配置(SET SBISMFSRVAREAARRPARAM) 
##### 修改SMF服务区域组参数配置(SET SBISMFSRVAREAARRPARAM) 


功能说明 

该命令用于修改SMF服务区域组参数配置。当UPF已配置可以支持的SMF服务区域组编号，需要修改归属于该SMF服务区域组编号的SMF服务区域信息时，使用该命令。 


注意事项 

如果修改该组参数归属的SMF服务区域组编号，则需要保证该SMF服务区域组编号已经存在，该编号通过[SHOW SBISMFSRVAREAARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




命令举例 


`
修改SMF服务区域组参数配置：配置索引为1，SMF服务区域组编号为1，服务区域为"01"。 
SET SBISMFSRVAREAARRPARAM:INDEX=1,ARRAYID=1,AREA="01"
` 


##### 删除SMF服务区域组参数配置(DEL SBISMFSRVAREAARRPARAM) 
##### 删除SMF服务区域组参数配置(DEL SBISMFSRVAREAARRPARAM) 


功能说明 

该命令用于删除SMF服务区域组参数配置。当UPF已配置可以支持的SMF服务区域组编号，需要删除归属于该SMF服务区域组编号的SMF服务区域信息时，使用该命令。 


注意事项 

如果归属于某个SMF服务区域组编号的所有SMF服务区域组参数配置都已经删除，建议删除该SMF服务区域组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




命令举例 


`
删除SMF服务区域组参数配置：配置索引为1。
DEL SBISMFSRVAREAARRPARAM:INDEX=1
` 


##### 查询SMF服务区域组参数配置(SHOW SBISMFSRVAREAARRPARAM) 
##### 查询SMF服务区域组参数配置(SHOW SBISMFSRVAREAARRPARAM) 


功能说明 

该命令用于查询SMF服务区域组参数配置。当需要查询已经配置的SMF服务区域组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会显示对应的配置信息；如果不指定配置索引，则显示已经配置的所有SMF服务区域组参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是SMF服务区域组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|SMF服务区域组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置SMF服务区域组编号。SMF服务区域组编号引用了“SMF服务区域组编号配置”中的配置，通过SHOW SBISMFSRVAREAARRID命令查询。
AREA|服务区域|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置UPF可以服务的SMF服务区域。




命令举例 


`
查询SMF服务区域组参数配置：配置索引为1。
SHOW SBISMFSRVAREAARRPARAM:INDEX=1

(No.1) : SHOW SBISMFSRVAREAARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 SMF服务区域组编号 服务区域 
---------------------------------------------------
复制 修改 删除 1        1                 01       
---------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:33:43 耗时: 0.603 秒

` 


### DNAI组配置 
### DNAI组配置 


背景知识 


DNAI（Data Network Access Identifier，数据网络接入标识符）表示可以接入一个数据网络的用户平面的标识。 

本地NRF功能中，该配置主要用于“DNN UPF信息组参数配置”中。该配置用于限定服务于某个DNN（Data Network Name，数据网名称）中的UPF所支持的数据网络接入标识符列表。服务使用者（本端）会携带用户当前的DNAI信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的DNAI与对端NFProfile的DNAI列表进行比较，找到匹配的DNAI时，就认为发现UPF成功。如果没有配置DNAI组，则UPF无法设置相应的DNAI列表，从而表示UPF可以支持任何DNAI，会为服务使用者提供所有的UPF。在本地NRF功能开启时，DNAI配置会呈现在DNN UPF信息组配置的dnaiList数组中。 




功能说明 


本地NRF功能打开时，DNAI组是以一组数据配置呈现的，该组数据配置包括DNAI组编号配置和DNAI组参数配置，一个DNAI组编号可以被若干个DNAI组参数引用。 

DNAI组配置被“DNN UPF信息组参数配置”引用，最终应用于UPF扩展信息中，用于表示服务于某个DNN中的UPF所支持的数据网络接入标识符列表。 




子主题： 






#### DNAI组编号配置 
#### DNAI组编号配置 


背景知识 


DNAI（Data Network Access Identifier，数据网络接入标识符）表示可以接入一个数据网络的用户平面的标识。 

本地NRF功能中，该配置主要用于“DNN UPF信息组参数配置”中。该配置用于限定服务于某个DNN（Data Network Name，数据网名称）中的UPF所支持的数据网络接入标识符列表。服务使用者（本端）会携带用户当前的DNAI信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的DNAI与对端NFProfile的DNAI列表进行比较，找到匹配的DNAI时，就认为发现UPF成功。如果没有配置DNAI组，则UPF无法设置相应的DNAI列表，从而表示UPF可以支持任何DNAI，会为服务使用者提供所有的UPF。在本地NRF功能开启时，DNAI配置会呈现在DNN UPF信息组配置的dnaiList数组中。 
DNAI组数据配置包括DNAI组编号配置和DNAI组参数配置。 




功能说明 


DNAI组编号配置用于配置一个DNAI组，一个DNAI组包含了若干个DNAI组参数。 

当启用本地NRF功能时，如果UPF扩展信息需要增加某个DNN（Data Network Name，数据网名称）中的UPF所支持的DNAI列表，则需要新增该组编号配置。DNAI组编号配置后，可以被多个DNAI组参数引用，从而组成一组DNAI信息。最终DNAI组编号可以被DNN UPF信息组参数配置所引用。 




子主题： 






##### 新增DNAI组编号配置(ADD SBIDNAIARRID) 
##### 新增DNAI组编号配置(ADD SBIDNAIARRID) 


功能说明 

该命令用于新增DNAI组编号配置。当UPF信息中的DNN UPF信息组配置需要携带一组DNAI列表时，使用该命令。 

命令执行成功后，DNAI组编号可以被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。 


注意事项 

必须先配置该DNAI组编号，才能在“DNAI组参数配置”及“DNN UPF信息组参数配置”中引用。 


 
使用命令SHOW SBIDNAIARRPARAM查询“DNAI组参数配置”。 

 
使用命令SHOW SBIDNNUPFINFOARRPARAM查询“DNN UPF信息组参数配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号，该编号是DNAI组编号配置的唯一标识，表示一组接入数据网络的用户平面的标识。该参数被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号，该编号是DNAI组编号配置的唯一标识，表示一组接入数据网络的用户平面的标识。该参数被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。




命令举例 


`
新增DNAI组编号配置：DNAI组编号为1。 
ADD SBIDNAIARRID:ARRAYID=1
` 


##### 删除DNAI组编号配置(DEL SBIDNAIARRID) 
##### 删除DNAI组编号配置(DEL SBIDNAIARRID) 


功能说明 

该命令用于删除DNAI组编号配置。当该组DNAI列表不被任何DNN UPF信息组参数配置所引用时，建议使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该DNAI组编号配置，需要先删除引用该配置的“DNAI组参数配置”，并在“DNN UPF信息组参数配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询，通过DEL SBIDNAIARRPARAM命令进行删除。 

 
“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询，通过SET SBIDNNUPFINFOARRPARAM命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号，该编号是DNAI组编号配置的唯一标识，表示一组接入数据网络的用户平面的标识。该参数被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号，该编号是DNAI组编号配置的唯一标识，表示一组接入数据网络的用户平面的标识。该参数被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。




命令举例 


`
删除DNAI组编号配置：DNAI组编号为1。
DEL SBIDNAIARRID:ARRAYID=1
` 


##### 查询DNAI组编号配置(SHOW SBIDNAIARRID) 
##### 查询DNAI组编号配置(SHOW SBIDNAIARRID) 


功能说明 

该命令用于查询DNAI组编号配置。当配置DNAI组参数及DNN UPF信息组参数时，需要获取已配置的DNAI组编号，此时可执行该命令查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号，该编号是DNAI组编号配置的唯一标识，表示一组接入数据网络的用户平面的标识。该参数被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号，该编号是DNAI组编号配置的唯一标识，表示一组接入数据网络的用户平面的标识。该参数被“DNAI组参数配置”及“DNN UPF信息组参数配置”引用。“DNAI组参数配置”通过SHOW SBIDNAIARRPARAM命令查询。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。




命令举例 


`
查询DNAI组编号配置：DNAI组编号为1。
SHOW SBIDNAIARRID:ARRAYID=1

(No.1) : SHOW SBIDNAIARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       DNAI组编号 
--------------------------
复制 删除      1          
--------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:42:48 耗时: 0.596 秒

` 


#### DNAI组参数配置 
#### DNAI组参数配置 


背景知识 


DNAI（Data Network Access Identifier，数据网络接入标识符）表示可以接入一个数据网络的用户平面的标识。 

本地NRF功能中，该配置主要用于“DNN UPF信息组参数配置”中。该配置用于限定服务于某个DNN（Data Network Name，数据网名称）中的UPF所支持的数据网络接入标识符列表。服务使用者（本端）会携带用户当前的DNAI信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的DNAI与对端NFProfile的DNAI列表进行比较，找到匹配的DNAI时，就认为发现UPF成功。如果没有配置DNAI组，则UPF无法设置相应的DNAI列表，从而表示UPF可以支持任何DNAI，会为服务使用者提供所有的UPF。在本地NRF功能开启时，DNAI配置会呈现在DNN UPF信息组配置的dnaiList数组中。 

DNAI组数据配置包括DNAI组编号配置和DNAI组参数配置。 




功能说明 


DNAI组参数配置用于配置一个DNAI归属于哪个DNAI组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在DNN UPF信息组配置中引用该DNAI组参数归属的DNAI组编号。如果不配置DNAI组参数，则无法配置具体的DNAI，已经配置的DNAI组编号只能是一个孤立配置。如果没有配置DNAI组参数的DNAI组被“DNN UPF信息组参数配置”引用后，会导致组装NFProfile失败。 




子主题： 






##### 新增DNAI组参数配置(ADD SBIDNAIARRPARAM) 
##### 新增DNAI组参数配置(ADD SBIDNAIARRPARAM) 


功能说明 

该命令用于新增DNAI组参数配置。当需要新增某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI列表时，使用该命令配置DNAI组参数，该参数配置DNAI信息及其归属的DNAI组。 


注意事项 

如果要新增该DNAI组参数配置，需要先新增“DNAI组编号配置”。 

“DNAI组编号配置”通过[ADD SBIDNAIARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 必选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




命令举例 


`
新增DNAI组参数配置：配置索引为1，DNAI组编号为1，DNAI为"abc"。 
ADD SBIDNAIARRPARAM:INDEX=1,ARRAYID=1,DATANAI="abc"
` 


##### 修改DNAI组参数配置(SET SBIDNAIARRPARAM) 
##### 修改DNAI组参数配置(SET SBIDNAIARRPARAM) 


功能说明 

该命令用于修改DNAI组参数配置。当UPF已配置可以支持的DNAI组编号，需要修改归属于该DNAI组编号的DNAI信息时，使用该命令。 


注意事项 

如果修改该组参数归属的DNAI组编号，则需要保证该DNAI组编号已经存在，该编号通过[SHOW SBIDNAIARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




命令举例 


`
修改DNAI组参数配置：配置索引为1，DNAI组编号为1，DNAI为"abc"。 
SET SBIDNAIARRPARAM:INDEX=1,ARRAYID=1,DATANAI="abc"
` 


##### 删除DNAI组参数配置(DEL SBIDNAIARRPARAM) 
##### 删除DNAI组参数配置(DEL SBIDNAIARRPARAM) 


功能说明 

该命令用于删除DNAI组参数配置。当UPF已配置可以支持的DNAI组编号，需要删除归属于该DNAI组编号的DNAI信息时，使用该命令。 


注意事项 

如果归属于某个DNAI组编号的所有DNAI组参数配置都已经删除，建议删除该DNAI组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




命令举例 


`
删除DNAI组参数配置：配置索引为1。
DEL SBIDNAIARRPARAM:INDEX=1
` 


##### 查询DNAI组参数配置(SHOW SBIDNAIARRPARAM) 
##### 查询DNAI组参数配置(SHOW SBIDNAIARRPARAM) 


功能说明 

该命令用于查询DNAI组参数配置。当需要查询已经配置的DNAI组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会显示对应的配置信息；如果不指定配置索引，则显示已经配置的所有DNAI组参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNAI组参数配置的唯一标识。
ARRAYID|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
DATANAI|DNAI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置可以接入数据网络的用户平面标识符，表示某个DNN（Data Network Name，数据网名称）中的UPF可支持的DNAI。




命令举例 


`
查询DNAI组参数配置：配置索引为1。
SHOW SBIDNAIARRPARAM:INDEX=1

(No.1) : SHOW SBIDNAIARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 DNAI组编号 DNAI 
----------------------------------------
复制 修改 删除 1        1          abc  
----------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:47:56 耗时: 0.607 秒

` 


### DNN UPF信息组配置 
### DNN UPF信息组配置 


背景知识 


DNN UPF信息组为S-NSSAI UPF信息组配置的必选部分，表示UPF所支持给定DNN的参数集，参数包括： 


 
DNN（Data Network Name，数据网络名称）：用于标识5G网络名称，由网络标识符和运营商标识符两部分组成。 

 
DNAI（Data Network Access Identifier，数据网络接入标识符）：可以参见配置SHOW SBIDNAIARRID。 

 
PduSessionType：UPF支持的PDU会话类型的列表。 

 
IPv4AddressRange：UPF可处理的IPv4地址范围列表。 

 
IPv6PrefixRange：UPF可处理的IPv6前缀范围列表。 

 

本地NRF功能中，该配置主要用于“S-NSSAI UPF信息组参数配置”中。该配置用于限定UPF所支持给定DNN的参数集。服务使用者（本端）会携带用户当前的DNN参数集，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的DNN参数集与对端NFProfile的DNN参数集进行比较，找到匹配的DNN参数集时，就认为发现UPF成功。如果没有配置DNN UPF信息组，则UPF无法设置相应的DNN参数集列表，从而表示UPF可以支持任何DNN参数集，会为服务使用者提供所有的UPF。在本地NRF功能开启时，DNN UPF信息组配置会呈现在S-NSSAI UPF信息组配置的dnnUpfInfoList数组中。 




功能说明 


本地NRF功能打开时，DNN UPF信息组是以一组数据配置呈现的，该组数据配置包括DNN UPF信息组编号配置和DNN UPF信息组参数配置，一个DNN UPF信息组编号可以被若干个DNN UPF信息组参数引用。 

DNN UPF信息组配置被“S-NSSAI UPF信息组参数配置”引用，最终应用于UPF扩展信息中，用于表示UPF所支持每个DNN的参数列表。 




子主题： 






#### DNN UPF信息组编号配置 
#### DNN UPF信息组编号配置 


背景知识 


DNN UPF信息组为S-NSSAI UPF信息组配置的必选部分，表示UPF所支持给定DNN的参数集，参数包括： 


 
DNN（Data Network Name，数据网络名称）：用于标识5G网络名称，由网络标识符和运营商标识符两部分组成。 

 
DNAI（Data Network Access Identifier，数据网络接入标识符）：可以参见配置SHOW SBIDNAIARRID。 

 
PduSessionType：UPF支持的PDU会话类型的列表。 

 
IPv4AddressRange：UPF可处理的IPv4地址范围列表。 

 
IPv6PrefixRange：UPF可处理的IPv6前缀范围列表。 

 

本地NRF功能中，该配置主要用于“S-NSSAI UPF信息组参数配置”中。该配置用于限定UPF所支持给定DNN的参数集。服务使用者（本端）会携带用户当前的DNN参数集，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的DNN参数集与对端NFProfile的DNN参数集进行比较，找到匹配的DNN参数集时，就认为发现UPF成功。如果没有配置DNN UPF信息组，则UPF无法设置相应的DNN参数集列表，从而表示UPF可以支持任何DNN参数集，会为服务使用者提供所有的UPF。在本地NRF功能开启时，DNN UPF信息组配置会呈现在S-NSSAI UPF信息组配置的dnnUpfInfoList数组中。 

DNN UPF信息组数据配置包括DNN UPF信息组编号配置和DNN UPF信息组参数配置。 




功能说明 


DNN UPF信息组编号配置用于配置一个DNN UPF信息组，一个DNN UPF信息组包含了若干个DNN UPF信息组参数。 

当启用本地NRF功能时，如果UPF扩展信息需要增加UPF所支持的DNN UPF信息列表，则需要新增该组编号配置。DNN UPF信息组编号配置后，可以被多个DNN UPF信息组参数引用，从而组成一组DNN UPF信息信息。最终DNN UPF信息组编号可以被S-NSSAI UPF信息组参数配置所引用。 




子主题： 






##### 新增DNN UPF信息组编号配置(ADD SBIDNNUPFINFOARRID) 
##### 新增DNN UPF信息组编号配置(ADD SBIDNNUPFINFOARRID) 


功能说明 

该命令用于新增DNN UPF信息组编号配置。当UPF信息中的S-NSSAI UPF信息组配置需要携带一组DNN UPF信息列表时，使用该命令。 

命令执行成功后，DNN UPF信息组编号可以被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。 


注意事项 

必须先配置该DNN UPF信息组编号，才能在“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”中引用。 


 
使用命令SHOW SBIDNNUPFINFOARRPARAM查询“DNN UPF信息组参数配置”。 

 
使用命令SHOW SBISNSSAIUPFINFOARRPARAM查询“S-NSSAI UPF信息组参数配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号，该编号是DNN UPF信息组编号配置的唯一标识，表示UPF所支持的一组DNN参数集。该参数被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号，该编号是DNN UPF信息组编号配置的唯一标识，表示UPF所支持的一组DNN参数集。该参数被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。




命令举例 


`
新增DNN UPF信息组编号配置：DNN UPF信息组编号为1。 
ADD SBIDNNUPFINFOARRID:ARRAYID=1
` 


##### 删除DNN UPF信息组编号配置(DEL SBIDNNUPFINFOARRID) 
##### 删除DNN UPF信息组编号配置(DEL SBIDNNUPFINFOARRID) 


功能说明 

该命令用于删除DNN UPF信息组编号配置。当该组DNN UPF信息列表不被任何S-NSSIA UPF信息组参数配置所引用时，建议使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该DNN UPF信息组编号配置，需要先删除引用该配置的“DNN UPF信息组参数配置”，并在“S-NSSAI UPF信息组参数配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询，通过DEL SBIDNNUPFINFOARRPARAM命令进行删除。 

 
“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询，通过SET SBISNSSAIUPFINFOARRPARAM命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号，该编号是DNN UPF信息组编号配置的唯一标识，表示UPF所支持的一组DNN参数集。该参数被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号，该编号是DNN UPF信息组编号配置的唯一标识，表示UPF所支持的一组DNN参数集。该参数被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。




命令举例 


`
删除DNN UPF信息组编号配置：DNN UPF信息组编号为1。
DEL SBIDNNUPFINFOARRID:ARRAYID=1
` 


##### 查询DNN UPF信息组编号配置(SHOW SBIDNNUPFINFOARRID) 
##### 查询DNN UPF信息组编号配置(SHOW SBIDNNUPFINFOARRID) 


功能说明 

该命令用于查询DNN UPF信息组编号配置。当配置DNN UPF信息组参数及S-NSSAI UPF信息组参数时，需要获取已配置的DNN UPF信息组编号，此时可执行该命令查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号，该编号是DNN UPF信息组编号配置的唯一标识，表示UPF所支持的一组DNN参数集。该参数被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号，该编号是DNN UPF信息组编号配置的唯一标识，表示UPF所支持的一组DNN参数集。该参数被“DNN UPF信息组参数配置”及“S-NSSAI UPF信息组参数配置”引用。“DNN UPF信息组参数配置”通过SHOW SBIDNNUPFINFOARRPARAM命令查询。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。




命令举例 


`
查询DNN UPF信息组编号配置：DNN UPF信息组编号为1。
SHOW SBIDNNUPFINFOARRID:ARRAYID=1

(No.1) : SHOW SBIDNNUPFINFOARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       DNN UPF信息组编号 
---------------------------------
复制 删除      1                 
---------------------------------
记录数：1
执行成功 开始时间:2020-12-15 17:03:28 耗时: 0.622 秒

` 


#### DNN UPF信息组参数配置 
#### DNN UPF信息组参数配置 


背景知识 


DNN UPF信息组为S-NSSAI UPF信息组配置的必选部分，表示UPF所支持给定DNN的参数集，参数包括： 


 
DNN（Data Network Name，数据网络名称）：用于标识5G网络名称，由网络标识符和运营商标识符两部分组成。 

 
DNAI（Data Network Access Identifier，数据网络接入标识符）：可以参见配置SHOW SBIDNAIARRID。 

 
PduSessionType：UPF支持的PDU会话类型的列表。 

 
IPv4AddressRange：UPF可处理的IPv4地址范围列表。 

 
IPv6PrefixRange：UPF可处理的IPv6前缀范围列表。 

 

本地NRF功能中，该配置主要用于“S-NSSAI UPF信息组参数配置”中。该配置用于限定UPF所支持给定DNN的参数集。服务使用者（本端）会携带用户当前的DNN参数集，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的DNN参数集与对端NFProfile的DNN参数集进行比较，找到匹配的DNN参数集时，就认为发现UPF成功。如果没有配置DNN UPF信息组，则UPF无法设置相应的DNN参数集列表，从而表示UPF可以支持任何DNN参数集，会为服务使用者提供所有的UPF。在本地NRF功能开启时，DNN UPF信息组配置会呈现在S-NSSAI UPF信息组配置的dnnUpfInfoList数组中。 

DNN UPF信息组数据配置包括DNN UPF信息组编号配置和DNN UPF信息组参数配置。 




功能说明 


DNN UPF信息组参数配置用于配置一个DNN UPF信息归属于哪个DNN UPF信息组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在S-NSSAI UPF信息组配置中引用该DNN UPF信息组参数归属的DNN UPF信息组编号。如果不配置DNN UPF信息组参数，则无法配置具体的DNN UPF信息，已经配置的DNN UPF信息组编号只能是一个孤立配置。如果没有配置DNN UPF信息组参数的DNN UPF信息组，被“S-NSSAI UPF信息组参数配置”引用后，会导致组装NFProfile失败。 




子主题： 






##### 新增DNN UPF信息组参数配置(ADD SBIDNNUPFINFOARRPARAM) 
##### 新增DNN UPF信息组参数配置(ADD SBIDNNUPFINFOARRPARAM) 


功能说明 

该命令用于新增DNN UPF信息组参数配置。当需要新增UPF可支持的DNN UPF信息列表时，使用该命令配置DNN UPF信息组参数，该参数配置DNN UPF信息及其归属的DNN UPF信息组。 


注意事项 

如果要新增该DNN UPF信息组参数配置，需要先新增“DNN UPF信息组编号配置”。 

“DNN UPF信息组编号配置”通过[ADD SBIDNNUPFINFOARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 必选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
新增DNN UPF信息组参数配置：配置索引为1，DNN UPF信息组编号为1，数据网络标识为"Label1.Label2.Label3"，DNAI组编号为1，PDU会话类型为"IPV4"&"IPV6"，IPv4地址范围组编号为1，IPv6前缀范围组编号为1。 
ADD SBIDNNUPFINFOARRPARAM:INDEX=1,ARRAYID=1,DNN="Label1.Label2.Label3",DNAIARRAY=1,PDUSESSTYPE="IPV4"&"IPV6",IPV4RNGARRAY=1,IPV6PREFIXRNGARRAY=1
` 


##### 修改DNN UPF信息组参数配置(SET SBIDNNUPFINFOARRPARAM) 
##### 修改DNN UPF信息组参数配置(SET SBIDNNUPFINFOARRPARAM) 


功能说明 

该命令用于修改DNN UPF信息组参数配置。当UPF已配置可以支持的DNN UPF信息组编号，需要修改归属于该DNN UPF信息组编号的DNN UPF信息时，使用该命令。 


注意事项 

如果修改该组参数归属的DNN UPF信息组编号，则需要保证该DNN UPF信息组编号已经存在，该编号通过[SHOW SBIDNNUPFINFOARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
修改DNN UPF信息组参数配置：配置索引为1，DNN UPF信息组编号为1，数据网络标识为"Label1.Label2.Label3"，DNAI组编号为1，PDU会话类型为"IPV4"&"IPV6"，IPv4地址范围组编号为1，IPv6前缀范围组编号为1。 
SET SBIDNNUPFINFOARRPARAM:INDEX=1,ARRAYID=1,DNN="Label1.Label2.Label3",DNAIARRAY=1,PDUSESSTYPE="IPV4"&"IPV6",IPV4RNGARRAY=1,IPV6PREFIXRNGARRAY=1
` 


##### 删除DNN UPF信息组参数配置(DEL SBIDNNUPFINFOARRPARAM) 
##### 删除DNN UPF信息组参数配置(DEL SBIDNNUPFINFOARRPARAM) 


功能说明 

该命令用于删除DNN UPF信息组参数配置。当UPF已配置可以支持的DNN UPF信息组编号，需要删除归属于该DNN UPF信息组编号的DNN UPF信息时，使用该命令。 


注意事项 

如果归属于某个DNN UPF信息组编号的所有DNN UPF信息组参数配置都已经删除，建议删除该DNN UPF信息组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
删除DNN UPF信息组参数配置：配置索引为1。
DEL SBIDNNUPFINFOARRPARAM:INDEX=1
` 


##### 查询DNN UPF信息组参数配置(SHOW SBIDNNUPFINFOARRPARAM) 
##### 查询DNN UPF信息组参数配置(SHOW SBIDNNUPFINFOARRPARAM) 


功能说明 

该命令用于查询DNN UPF信息组参数配置。当需要查询已经配置的DNN UPF信息组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会显示对应的配置信息；如果不指定配置索引，则显示已经配置的所有DNN UPF信息组参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是DNN UPF信息组参数配置的唯一标识。该参数无特殊配置原则。
ARRAYID|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
DNN|数据网络标识|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置UPF支持的DNN（Data Network Name，数据网络标识）。 DNN必须包含网络标识符，并且可以另外包含一个运营商标识符。如果不包括运营商标识符，则NFProfile中所有PLMN（Public Land Mobile Network，公共陆地移动网）都支持DNN。该参数应被编码为字符串，其中标签由点分隔（例如“ Label1.Label2.Label3”）。
DNAIARRAY|DNAI组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置DNAI组编号。DNAI组编号引用了“DNAI组编号配置”中的配置，通过SHOW SBIDNAIARRID命令查询。
PDUSESSTYPE|PDU会话类型|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET|该参数用于设置UPF为特定DNN所支持的PDU会话类型的列表。类型为位枚举，默认全选。如果该参数设置为NULL，则表示UPF不选择支持的PDU会话类型。注意：如果该参数的值全部都不勾选（包括NULL），即该值缺省，依然默认全选，表示可以为该特定DNN选择UPF支持的任何PDU会话类型。IPV4（IPv4类型）：表示当用户接入时，CPF（Control Plane Function，控制面功能）会根据该配置中的IPv4地址类型选择相匹配的用户面。IPV6（IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv6地址类型选择相匹配的用户面。IPV4V6（IPv4&IPv6类型）：表示当用户接入时，CPF会根据该配置中的IPv4和IPv6地址类型选择相匹配的用户面。UNSTRUCTURED（非结构化类型）：表示当用户接入时，CPF会根据该配置中的非结构化地址类型选择相匹配的用户面。ETHERNET（以太网类型）：表示当用户接入时，CPF会根据该配置中的以太网地址类型选择相匹配的用户面。
IPV4RNGARRAY|IPv4地址范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址范围组编号，表示UPF可处理的IPv4地址范围列表。SMF可以使用该IPv4地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv4地址范围组编号引用了“IPv4地址范围组编号配置”中的配置，通过SHOW SBIIPV4ADDRRANGEARRID命令查询。
IPV6PREFIXRNGARRAY|IPv6前缀范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6前缀范围组编号，表示UPF可处理的IPv6前缀范围的列表。SMF可以使用该IPv6地址范围列表，来选择支持在用户订阅中可接收到UE静态IP地址的UPF。IPv6前缀范围组编号引用了“IPv6前缀范围组编号配置”中的配置，通过SHOW SBIIPV6PREFIXRANGEARRID命令查询。




命令举例 


`
查询DNN UPF信息组参数配置：配置索引为1。
SHOW SBIDNNUPFINFOARRPARAM:INDEX=1

(No.1) : SHOW SBIDNNUPFINFOARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 DNN UPF信息组编号 数据网络标识           DNAI组编号 PDU会话类型  IPv4地址范围组编号 IPv6前缀范围组编号 
----------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1        1                 Label1.Label2.Label3 1          IPV4&IPV6   1                  1                  
----------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 17:09:10 耗时: 0.614 秒

` 


### S-NSSAI UPF信息组配置 
### S-NSSAI UPF信息组配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，之后SMF与发现的UPF进行通信。S-NSSAI UPF信息表示UPF可以支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）信息。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。S-NSSAI UPF信息组为UPF信息配置的必选部分，该配置用于限定UPF可以服务的S-NSSAI列表。服务使用者（本端）会携带用户当前的S-NSSAI信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与对端NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现UPF成功。在本地NRF功能开启时，S-NSSAI配置会呈现在UPF信息配置的sNssaiUpfInfoList数组中。 




功能说明 


本地NRF功能打开时，S-NSSAI UPF信息组是以一组数据配置呈现的，该组数据配置包括S-NSSAI UPF信息组编号配置和S-NSSAI UPF信息组参数配置，一个S-NSSAI UPF信息组编号可以被若干个S-NSSAI UPF信息组参数引用。 

S-NSSAI UPF信息组配置应用于UPF扩展信息配置中，用于表示该UPF可以服务的S-NSSAI信息。 




子主题： 






#### S-NSSAI UPF信息组编号配置 
#### S-NSSAI UPF信息组编号配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，之后SMF与发现的UPF进行通信。S-NSSAI UPF信息表示UPF可以支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）信息。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。S-NSSAI UPF信息组为UPF信息配置的必选部分，该配置用于限定UPF可以服务的S-NSSAI列表。服务使用者（本端）会携带用户当前的S-NSSAI信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与对端NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现UPF成功。在本地NRF功能开启时，S-NSSAI配置会呈现在UPF信息配置的sNssaiUpfInfoList数组中。 

S-NSSAI UPF信息组数据配置包括S-NSSAI UPF信息组编号配置和S-NSSAI UPF信息组参数配置。 




功能说明 


S-NSSAI UPF信息组编号配置用于配置一个S-NSSAI UPF信息组，一个S-NSSAI UPF信息组包含了若干个S-NSSAI UPF信息组参数。 

当启用本地NRF功能时，如果UPF扩展信息需要增加可以服务的S-NSSAI列表，则需要新增该组编号配置。S-NSSAI UPF信息组编号配置后，可以被多个S-NSSAI UPF信息组参数引用，从而组成一组S-NSSAI UPF信息信息。最终S-NSSAI UPF信息组编号可以被UPF信息配置所引用。 




子主题： 






##### 新增S-NSSAI UPF信息组编号配置(ADD SBISNSSAIUPFINFOARRID) 
##### 新增S-NSSAI UPF信息组编号配置(ADD SBISNSSAIUPFINFOARRID) 


功能说明 

该命令用于新增S-NSSAI UPF信息组编号配置。当UPF信息需要携带一组S-NSSAI UPF信息列表时，使用该命令。 

命令执行成功后，S-NSSAI UPF信息组编号可以被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。 


注意事项 

必须先配置该S-NSSAI UPF信息组编号，才能在“S-NSSAI UPF信息组参数配置”及“UPF信息配置”中引用。 


 
使用命令SHOW SBISNSSAIUPFINFOARRPARAM查询“S-NSSAI UPF信息组参数配置”。 

 
使用命令SHOW SBIUPFINFO查询“UPF信息配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，该编号是S-NSSAI UPF信息组编号配置的唯一标识，表示UPF可以服务的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。该参数被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，该编号是S-NSSAI UPF信息组编号配置的唯一标识，表示UPF可以服务的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。该参数被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。




命令举例 


`
新增S-NSSAI UPF信息组编号配置：S-NSSAI UPF信息组编号为1。 
ADD SBISNSSAIUPFINFOARRID:ARRAYID=1
` 


##### 删除S-NSSAI UPF信息组编号配置(DEL SBISNSSAIUPFINFOARRID) 
##### 删除S-NSSAI UPF信息组编号配置(DEL SBISNSSAIUPFINFOARRID) 


功能说明 

该命令用于删除S-NSSAI UPF信息组编号配置。当该组S-NSSAI UPF信息列表不被任何UPF所引用时，建议使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该S-NSSAI UPF信息组编号配置，需要先删除引用该配置的“S-NSSAI UPF信息组参数配置”，并在“UPF信息配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询，通过DEL SBISNSSAIUPFINFOARRPARAM命令进行删除。 

 
“UPF信息配置”通过SHOW SBIUPFINFO命令查询，通过SET SBIUPFINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，该编号是S-NSSAI UPF信息组编号配置的唯一标识，表示UPF可以服务的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。该参数被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，该编号是S-NSSAI UPF信息组编号配置的唯一标识，表示UPF可以服务的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。该参数被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。




命令举例 


`
删除S-NSSAI UPF信息组编号配置：S-NSSAI UPF信息组编号为1。
DEL SBISNSSAIUPFINFOARRID:ARRAYID=1
` 


##### 查询S-NSSAI UPF信息组编号配置(SHOW SBISNSSAIUPFINFOARRID) 
##### 查询S-NSSAI UPF信息组编号配置(SHOW SBISNSSAIUPFINFOARRID) 


功能说明 

该命令用于查询S-NSSAI UPF信息组编号配置。当配置S-NSSAI UPF信息组参数及UPF信息时，需要获取已配置的S-NSSAI UPF信息组编号，此时可执行该命令查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，该编号是S-NSSAI UPF信息组编号配置的唯一标识，表示UPF可以服务的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。该参数被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号，该编号是S-NSSAI UPF信息组编号配置的唯一标识，表示UPF可以服务的一组S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）。该参数被“S-NSSAI UPF信息组参数配置”及“UPF信息配置”引用。“S-NSSAI UPF信息组参数配置”通过SHOW SBISNSSAIUPFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。




命令举例 


`
查询S-NSSAI UPF信息组编号配置：S-NSSAI UPF信息组编号为1。
SHOW SBISNSSAIUPFINFOARRID:ARRAYID=1

(No.1) : SHOW SBISNSSAIUPFINFOARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       S-NSSAI UPF信息组编号 
------------------------------------
复制 删除      1                    
------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:34:56 耗时: 0.621 秒

` 


#### S-NSSAI UPF信息组参数配置 
#### S-NSSAI UPF信息组参数配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，之后SMF与发现的UPF进行通信。S-NSSAI UPF信息表示UPF可以支持的S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）信息。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。S-NSSAI UPF信息组为UPF信息配置的必选部分，该配置用于限定UPF可以服务的S-NSSAI列表。服务使用者（本端）会携带用户当前的S-NSSAI信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的S-NSSAI与对端NFProfile的S-NSSAI列表进行比较，找到匹配的S-NSSAI时，就认为发现UPF成功。在本地NRF功能开启时，S-NSSAI配置会呈现在UPF信息配置的sNssaiUpfInfoList数组中。 

S-NSSAI UPF信息组数据配置包括S-NSSAI UPF信息组编号配置和S-NSSAI UPF信息组参数配置。 




功能说明 


S-NSSAI UPF信息组参数配置用于配置一个S-NSSAI UPF信息归属于哪个S-NSSAI UPF信息组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在UPF扩展信息中引用该S-NSSAI UPF信息组参数归属的S-NSSAI UPF信息组编号。如果不配置S-NSSAI UPF信息组参数，则无法配置具体的S-NSSAI UPF信息，已经配置的S-NSSAI UPF信息组编号只能是一个孤立配置。如果没有配置S-NSSAI UPF信息组参数的S-NSSAI UPF信息组，被“UPF信息配置”引用后，会导致组装NFProfile失败。 




子主题： 






##### 新增S-NSSAI UPF信息组参数配置(ADD SBISNSSAIUPFINFOARRPARAM) 
##### 新增S-NSSAI UPF信息组参数配置(ADD SBISNSSAIUPFINFOARRPARAM) 


功能说明 

该命令用于新增S-NSSAI UPF信息组参数配置。当UPF需要新增可服务的S-NSSAI信息列表时，使用该命令配置S-NSSAI UPF信息组参数，该参数配置S-NSSAI UPF信息及其归属的S-NSSAI UPF信息组。 


注意事项 


 
需要保证该组参数归属的S-NSSAI UPF信息组编号已经存在，该编号通过SHOW SBISNSSAIUPFINFOARRID命令查询。 

 
需要保证关联的S-NSSAI编号已经存在，该编号通过SHOW SBISNSSAI命令查询。 

 
需要保证关联的DNN UPF信息组编号已经存在，该编号通过SHOW SBIDNNUPFINFOARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




命令举例 


`
新增S-NSSAI UPF信息组参数配置：配置索引为1，S-NSSAI UPF信息组编号为1，S-NSSAI编号为1，DNN UPF信息组编号为1，是否支持冗余传输为"是"。 
ADD SBISNSSAIUPFINFOARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=1,DNNUPFARRAY=1,REDUNDANTTRANS="YES"
` 


##### 修改S-NSSAI UPF信息组参数配置(SET SBISNSSAIUPFINFOARRPARAM) 
##### 修改S-NSSAI UPF信息组参数配置(SET SBISNSSAIUPFINFOARRPARAM) 


功能说明 

该命令用于修改S-NSSAI UPF信息组参数配置。当UPF已配置可以支持的S-NSSAI UPF信息组编号，需要修改归属于该S-NSSAI UPF信息组编号的S-NSSAI UPF信息时，使用该命令。 


注意事项 


 
如果修改该范围组参数归属的S-NSSAI UPF信息组编号，则需要保证该S-NSSAI UPF信息组编号已经存在，该编号通过SHOW SBISNSSAIUPFINFOARRID命令查询。 

 
如果修改关联的S-NSSAI编号，则需要保证该编号已经存在，该编号通过SHOW SBISNSSAI命令查询。 

 
如果修改关联的DNN UPF信息组编号，则需要保证该编号已经存在，该编号通过SHOW SBIDNNUPFINFOARRID命令查询。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




命令举例 


`
修改S-NSSAI UPF信息组参数配置：配置索引为1，S-NSSAI UPF信息组编号为1，S-NSSAI编号为1，DNN UPF信息组编号为1，是否支持冗余传输为"是"。 
SET SBISNSSAIUPFINFOARRPARAM:INDEX=1,ARRAYID=1,SNSSAI=1,DNNUPFARRAY=1,REDUNDANTTRANS="YES"
` 


##### 删除S-NSSAI UPF信息组参数配置(DEL SBISNSSAIUPFINFOARRPARAM) 
##### 删除S-NSSAI UPF信息组参数配置(DEL SBISNSSAIUPFINFOARRPARAM) 


功能说明 

该命令用于删除S-NSSAI UPF信息组参数配置。当UPF已配置可以支持的S-NSSAI UPF信息组编号，需要删除归属于该S-NSSAI UPF信息组编号的S-NSSAI UPF信息时，使用该命令。 


注意事项 

如果归属于某个S-NSSAI UPF信息组编号的所有S-NSSAI UPF信息组参数配置都已经删除，建议删除该S-NSSAI UPF信息组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




命令举例 


`
删除S-NSSAI UPF信息组参数配置：配置索引为1。
DEL SBISNSSAIUPFINFOARRPARAM:INDEX=1
` 


##### 查询S-NSSAI UPF信息组参数配置(SHOW SBISNSSAIUPFINFOARRPARAM) 
##### 查询S-NSSAI UPF信息组参数配置(SHOW SBISNSSAIUPFINFOARRPARAM) 


功能说明 

该命令用于查询S-NSSAI UPF信息组参数配置。当需要查询已经配置的S-NSSAI UPF信息组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会显示对应的配置信息；如果不指定配置索引，则显示已经配置的所有S-NSSAI UPF信息组参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是S-NSSAI UPF信息组参数配置的唯一标识。
ARRAYID|S-NSSAI UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI UPF信息组编号。S-NSSAI UPF信息组编号引用了“S-NSSAI UPF信息组编号配置”中的配置，通过SHOW SBISNSSAIUPFINFOARRID命令查询。
SNSSAI|S-NSSAI编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置S-NSSAI编号。S-NSSAI编号引用了“S-NSSAI配置”中的配置，通过SHOW SBISNSSAI命令查询。
DNNUPFARRAY|DNN UPF信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置DNN UPF信息组编号。DNN UPF信息组编号引用了“DNN UPF信息组编号配置”中的配置，通过SHOW SBIDNNUPFINFOARRID命令查询。
REDUNDANTTRANS|是否支持冗余传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置UPF是否在相应网络切片的传输层上支持冗余传输路径。为了支持高可靠的URLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信）服务，可使用冗余传输，即UE可以在5G网络上建立两个冗余PDU会话，使得5GS将两个冗余PDU会话的用户平面路径设置为不相交。




命令举例 


`
查询S-NSSAI UPF信息组参数配置：配置索引为1。
SHOW SBISNSSAIUPFINFOARRPARAM:INDEX=1

(No.1) : SHOW SBISNSSAIUPFINFOARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 S-NSSAI UPF信息组编号 S-NSSAI编号 DNN UPF信息组编号 是否支持冗余传输 
---------------------------------------------------------------------------------------------
复制 修改 删除 1        1                     1           1                 是               
---------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:40:46 耗时: 0.606 秒

` 


### UPF接口信息组配置 
### UPF接口信息组配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，之后SMF与发现的UPF进行通信。UPF接口信息表示UPF可以支持的用户平面接口列表。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。该配置用于限定UPF可以支持的用户平面接口列表。服务使用者（本端）会携带用户当前的用户平面接口信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的用户平面接口与对端NFProfile的用户平面接口列表进行比较，找到匹配的用户平面接口时，就认为发现UPF成功。在本地NRF功能开启时，S-NSSAI配置会呈现在UPF信息配置的interfaceUpfInfoList数组中。 




功能说明 


本地NRF功能打开时，UPF接口信息组是以一组数据配置呈现的，该组数据配置包括UPF接口信息组编号配置和UPF接口信息组参数配置，一个UPF接口信息组编号可以被若干个UPF接口信息组参数引用。 

UPF接口信息组配置应用于UPF扩展信息配置中，用于表示该UPF可以支持的用户平面接口列表。 




子主题： 






#### UPF接口信息组编号配置 
#### UPF接口信息组编号配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，之后SMF与发现的UPF进行通信。UPF接口信息表示UPF可以支持的用户平面接口列表。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。该配置用于限定UPF可以支持的用户平面接口列表。服务使用者（本端）会携带用户当前的用户平面接口信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的用户平面接口与对端NFProfile的用户平面接口列表进行比较，找到匹配的用户平面接口时，就认为发现UPF成功。在本地NRF功能开启时，S-NSSAI配置会呈现在UPF信息配置的interfaceUpfInfoList数组中。 

UPF接口信息组数据配置包括UPF接口信息组编号配置和UPF接口信息组参数配置。 




功能说明 


UPF接口信息组编号配置用于配置一个UPF接口信息组，一个UPF接口信息组包含了若干个UPF接口信息组参数。 

当启用本地NRF功能时，如果UPF扩展信息需要增加可以支持的用户平面接口列表，则需要新增该组编号配置。UPF接口信息组编号配置后，可以被多个UPF接口信息组参数引用，从而组成一组UPF接口信息。最终UPF接口信息组编号可以被UPF信息配置所引用。 




子主题： 






##### 新增UPF接口信息组编号配置(ADD SBIUPFITFINFOARRID) 
##### 新增UPF接口信息组编号配置(ADD SBIUPFITFINFOARRID) 


功能说明 

该命令用于新增UPF接口信息组编号配置。当UPF信息配置需要携带一组UPF接口信息列表时，使用该命令。 

命令执行成功后，UPF接口信息组编号可以被“UPF接口信息组参数配置”及“UPF信息配置”引用。 


注意事项 

必须先配置该UPF接口信息组编号，才能在“UPF接口信息组参数配置”及“UPF信息配置”中引用。 


 
使用命令SHOW SBIUPFITFINFOARRPARAM查询“UPF接口信息组参数配置”。 

 
使用命令SHOW SBIUPFINFO查询“UPF信息配置”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|UPF接口信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号，该编号是UPF接口信息组编号配置的唯一标识，表示UPF可以支持的一组用户平面接口列表。该参数被“UPF接口信息组参数配置”及“UPF信息配置”引用。“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号，该编号是UPF接口信息组编号配置的唯一标识，表示UPF可以支持的一组用户平面接口列表。该参数被“UPF接口信息组参数配置”及“UPF信息配置”引用。“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
新增UPF接口信息组编号配置：UPF接口信息组编号为1。 
ADD SBIUPFITFINFOARRID:ARRAYID=1
` 


##### 删除UPF接口信息组编号配置(DEL SBIUPFITFINFOARRID) 
##### 删除UPF接口信息组编号配置(DEL SBIUPFITFINFOARRID) 


功能说明 

该命令用于删除UPF接口信息组编号配置。当该组UPF接口信息列表不被任何UPF所引用时，建议使用该命令。命令执行成功后，该组配置无法被查询，也无法再被引用。 


注意事项 

如果要删除该UPF接口信息组编号配置，需要先删除引用该配置的“UPF接口信息组参数配置”，并在“UPF信息配置”中将引用该配置的参数值设置为0来删除引用关系。 


 
“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询，通过DEL SBIUPFITFINFOARRPARAM命令进行删除。 

 
“UPF信息配置”通过SHOW SBIUPFINFO命令查询，通过SET SBIUPFINFO命令进行设置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|UPF接口信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号，该编号是UPF接口信息组编号配置的唯一标识，表示UPF可以支持的一组用户平面接口列表。该参数被“UPF接口信息组参数配置”及“UPF信息配置”引用。“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号，该编号是UPF接口信息组编号配置的唯一标识，表示UPF可以支持的一组用户平面接口列表。该参数被“UPF接口信息组参数配置”及“UPF信息配置”引用。“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
删除UPF接口信息组编号配置：UPF接口信息组编号为1。
DEL SBIUPFITFINFOARRID:ARRAYID=1
` 


##### 查询UPF接口信息组编号配置(SHOW SBIUPFITFINFOARRID) 
##### 查询UPF接口信息组编号配置(SHOW SBIUPFITFINFOARRID) 


功能说明 

该命令用于查询UPF接口信息组编号配置。当配置UPF接口信息组参数及UPF信息时，需要获取已配置的UPF接口信息组编号，此时可执行该命令查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号，该编号是UPF接口信息组编号配置的唯一标识，表示UPF可以支持的一组用户平面接口列表。该参数被“UPF接口信息组参数配置”及“UPF信息配置”引用。“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号，该编号是UPF接口信息组编号配置的唯一标识，表示UPF可以支持的一组用户平面接口列表。该参数被“UPF接口信息组参数配置”及“UPF信息配置”引用。“UPF接口信息组参数配置”通过SHOW SBIUPFITFINFOARRPARAM命令查询。“UPF信息配置”通过SHOW SBIUPFINFO命令查询。该参数无特殊配置原则。




命令举例 


`
查询UPF接口信息组编号配置：UPF接口信息组编号为1。
SHOW SBIUPFITFINFOARRID:ARRAYID=1

(No.1) : SHOW SBIUPFITFINFOARRID:ARRAYID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       UPF接口信息组编号 
---------------------------------
复制 删除      1                 
---------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:26:51 耗时: 0.637 秒

` 


#### UPF接口信息组参数配置 
#### UPF接口信息组参数配置 


背景知识 


当UPF向NRF注册了自己的相关配置信息，SMF可以通过向NRF订阅发现UPF，之后SMF与发现的UPF进行通信。UPF接口信息表示UPF可以支持的用户平面接口列表。 

本地NRF功能中，该配置主要用于“UPF信息配置”中。该配置用于限定UPF可以支持的用户平面接口列表。服务使用者（本端）会携带用户当前的用户平面接口信息，当服务使用者向NRF发现可用的服务提供者（对端）时，NRF根据发现请求的用户平面接口与对端NFProfile的用户平面接口列表进行比较，找到匹配的用户平面接口时，就认为发现UPF成功。在本地NRF功能开启时，S-NSSAI配置会呈现在UPF信息配置的interfaceUpfInfoList数组中。 

UPF接口信息组数据配置包括UPF接口信息组编号配置和UPF接口信息组参数配置。 




功能说明 


UPF接口信息组参数配置用于配置一个UPF接口信息归属于哪个UPF接口信息组。当启用本地NRF功能时，需要配置该组命令。 

配置完成后，在UPF扩展信息中引用该UPF接口信息组参数归属的UPF接口信息组编号。如果不配置UPF接口信息组参数，则无法配置具体的UPF接口信息，已经配置的UPF接口信息组编号只能是一个孤立配置。如果没有配置UPF接口信息组参数的UPF接口信息组，被“UPF信息配置”引用后，会导致组装NFProfile失败。 




子主题： 






##### 新增UPF接口信息组参数配置(ADD SBIUPFITFINFOARRPARAM) 
##### 新增UPF接口信息组参数配置(ADD SBIUPFITFINFOARRPARAM) 


功能说明 

该命令用于新增UPF接口信息组参数配置。当需要新增UPF可支持的UPF接口信息列表时，使用该命令配置UPF接口信息组参数，该参数配置UPF接口信息及其归属的UPF接口信息组。 


注意事项 

如果要新增该UPF接口信息组参数配置，需要先新增“UPF接口信息组编号配置”。 

“UPF接口信息组编号配置”通过[ADD SBIUPFITFINFOARRID]命令进行新增。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




命令举例 


`
新增UPF接口信息组参数配置：配置索引为1，UPF接口信息组编号为1，接口类型为N3，IPv4地址组编号为1，IPv6地址组编号引为1，FQDN为"upfitf1.com"，网络实例为"001"。 
ADD SBIUPFITFINFOARRPARAM:INDEX=1,ARRAYID=1,ITFTYPE="N3",IPV4=1,IPV6=1,FQDN="upfitf1.com",NETWORKINST="001"
` 


##### 修改UPF接口信息组参数配置(SET SBIUPFITFINFOARRPARAM) 
##### 修改UPF接口信息组参数配置(SET SBIUPFITFINFOARRPARAM) 


功能说明 

该命令用于修改UPF接口信息组参数配置。当UPF已配置可以支持的UPF接口信息组编号，需要修改归属于该UPF接口信息组编号的UPF接口信息时，使用该命令。 


注意事项 

如果修改该组参数归属的UPF接口信息组编号，则需要保证该UPF接口信息组编号已经存在，该编号通过[SHOW SBIUPFITFINFOARRID]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




命令举例 


`
修改UPF接口信息组参数配置：配置索引为1，UPF接口信息组编号为1，接口类型为N3，IPv4地址组编号为1，IPv6地址组编号引为1，FQDN为"upfitf1.com"，网络实例为"001"。 
SET SBIUPFITFINFOARRPARAM:INDEX=1,ARRAYID=1,ITFTYPE="N3",IPV4=1,IPV6=1,FQDN="upfitf1.com",NETWORKINST="001"
` 


##### 删除UPF接口信息组参数配置(DEL SBIUPFITFINFOARRPARAM) 
##### 删除UPF接口信息组参数配置(DEL SBIUPFITFINFOARRPARAM) 


功能说明 

该命令用于删除UPF接口信息组参数配置。当UPF已配置可以支持的UPF接口信息组编号，需要删除归属于该UPF接口信息组编号的UPF接口信息时，使用该命令。 


注意事项 

如果归属于某个UPF接口信息组编号的所有UPF接口信息组参数配置都已经删除，建议删除该UPF接口信息组编号配置，防止被误引用。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




命令举例 


`
删除UPF接口信息组参数配置：配置索引为1。
DEL SBIUPFITFINFOARRPARAM:INDEX=1
` 


##### 查询UPF接口信息组参数配置(SHOW SBIUPFITFINFOARRPARAM) 
##### 查询UPF接口信息组参数配置(SHOW SBIUPFITFINFOARRPARAM) 


功能说明 

该命令用于查询UPF接口信息组参数配置。当需要查询已经配置的UPF接口信息组参数信息时，使用该命令。查询时，可以指定配置索引，查询成功后，会显示对应的配置信息；如果不指定配置索引，则显示已经配置的所有UPF接口信息组参数信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
INDEX|配置索引|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置配置索引，该索引是UPF接口信息组参数配置的唯一标识。
ARRAYID|UPF接口信息组编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置UPF接口信息组编号。UPF接口信息组编号引用了“UPF接口信息组编号配置”中的配置，通过SHOW SBIUPFITFINFOARRID命令查询。
ITFTYPE|接口类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置用户平面接口类型。N3（N3接口）：N3接口是5G (R)AN（Radio Access Network，无线接入网 ）与UPF间的接口。选择该场景下，用于传递5G (R)AN与UPF间的上下行用户数据流。N6（N6接口）：N6接口是 UPF与DN（Data Network）的接口。选择该场景下，用于传递UPF与DN之间的上下行用户数据流，基于IP和路由协议与DN网络通信。N9（N9接口）：N9接口是UPF和UPF之间的用户面接口。选择该场景下，用于传递UPF间的上下行用户数据流。
IPV4|IPv4地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv4地址组编号，表示用户平面接口的可用端点IPv4地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv4地址组编号引用了“IPv4地址组编号配置”中的配置，通过SHOW SBIIPV4ADDRARRID命令查询。
IPV6|IPv6地址组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置IPv6地址组编号，表示用户平面接口的可用端点IPv6地址。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。IPv6地址组编号“IPv6地址组编号配置”中的配置，通过SHOW SBIIPV6ADDRARRID命令查询。
FQDN|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-127|该参数用于设置用户平面接口的FQDN（Fully Qualified Domain Name，全称域名）。UPF接口信息组配置中根据组网需求，应至少包含一个寻址参数（FQDN、IPv4地址或IPv6地址）。
NETWORKINST|网络实例|参数可选性: 任选参数类型: 字符串参数范围: 0-63|该参数用于设置与用户平面接口关联的网络实例，网络实例字段应编码为OctetString，并在UPF中应包含能够唯一标识特定网络实例（如PDN实例）的标识符。该参数可以被编码为域名或接入点名称（APN）。在该参数被编码为APN情况下，PDN实例字段可以仅包含APN网络标识符或包含APN网络标识符和APN运营商标识符的完整APN。




命令举例 


`
查询UPF接口信息组参数配置：配置索引为1。
SHOW SBIUPFITFINFOARRPARAM:INDEX=1

(No.15) : SHOW SBIUPFITFINFOARRPARAM:INDEX=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       配置索引 UPF接口信息组编号 接口类型 IPv4地址组编号 IPv6地址组编号 FQDN        网络实例 
------------------------------------------------------------------------------------------------------
复制 修改 删除 1        1                 N3       1              1              upfitf1.com 001      
------------------------------------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-12-15 14:27:55 耗时: 0.6 秒

` 


## OCS配置 
## OCS配置 


背景知识 


OCS（在线计费系统，Online Charging System），是指参与通信过程控制的计费系统，是在线计费系统的融合，能够解决用户实时信用控制、预付费使用数据业务和增值业务实时计费等问题。 

当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF（网络功能，Network Function）类型为OCS，那么注册请求中携带的对端NFProfile参数可以包含OCS信息（OCSInfo）参数，该参数又包含了一些通用或OCS特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为OCS时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的OCS信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，OCS信息配置会呈现在对端NFProfile的OCS信息参数中。 




功能说明 


OCS配置为命令树目录，下面包含了OCS信息配置。OCS信息配置即对应本地NRF配置的对端NFProfile的OCS信息参数，如果不配置，则对端NFProfile缺少OCS信息参数，本端如果需要发现可用的对端OCS时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






### OCS信息配置 
### OCS信息配置 


背景知识 


OCS（在线计费系统，Online Charging System），是指参与通信过程控制的计费系统，是在线计费系统的融合，能够解决用户实时信用控制、预付费使用数据业务和增值业务实时计费等问题。 

当服务提供者（对端）向NRF（网络存储功能，Network Repository Function）注册时，如果对端的NF（网络功能，Network Function）类型为OCS，那么注册请求中携带的对端NFProfile参数可以包含OCS信息（OCSInfo）参数，该参数又包含了一些通用或OCS特有的参数。 

当服务使用者（本端）向NRF发现可用的服务提供者（对端），并且对端的NF类型为OCS时，NRF可以用服务发现请求中的发现参数与对端NFProfile包含的OCS信息进行比较，如果能匹配成功，则认为发现成功，并且在发现响应中携带该NFProfile。当本端启用本地NRF功能时，OCS信息配置会呈现在对端NFProfile的OCS信息参数中。 




功能说明 


OCS信息配置即对应本地NRF配置的对端NFProfile的OCS信息参数，如果不配置，则对端NFProfile缺少OCS信息参数，本端如果需要发现可用的对端OCS时，就无法进行有效的发现参数匹配，可能导致业务失败。当启用本地NRF功能时，需要配置该组命令。 




子主题： 






#### 新增OCS信息配置(ADD SBIOCSINFO) 
#### 新增OCS信息配置(ADD SBIOCSINFO) 


功能说明 

本命令用于新增OCS信息。当本地NRF配置中所配置的对端NFProfile需要携带OCS信息时，使用该命令。命令执行成功后，OCS信息编号可以被对端NF扩展信息配置引用。 


注意事项 

系统支持的该配置项最大记录数为2048。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
增加OCS信息配置：编号为1，GPSI范围组编号为1。 
ADD SBIOCSINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 修改OCS信息配置(SET SBIOCSINFO) 
#### 修改OCS信息配置(SET SBIOCSINFO) 


功能说明 

本命令用于修改OCS信息。当本地NRF配置中所配置的对端NFProfile携带的OCS信息需要变更时，使用该命令。命令执行成功后，修改后的OCS信息会呈现在本地NRF配置中所配置的对端NFProfile中。 


注意事项 

修改OCS信息，需要保证OCS信息编号已经存在，该编号通过[SHOW SBIOCSINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
修改OCS信息配置：编号为1，GPSI范围组编号为1。 
SET SBIOCSINFO:ID=1,GPSIRANGEARRAY=1
` 


#### 删除OCS信息配置(DEL SBIOCSINFO) 
#### 删除OCS信息配置(DEL SBIOCSINFO) 


功能说明 

本命令用于删除OCS信息。当本地NRF配置中所配置的对端NFProfile不需要携带该OCS信息时，使用该命令。命令执行成功后，本地NRF配置中所配置的对端NFProfile将不携带该OCS信息。 


注意事项 

如果要删除该OCS信息配置，需要先删除引用该配置的对端NF扩展信息配置。对端NF扩展信息配置通过[SHOW SBIPEERNFEXTINFO]命令查询。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
删除OCS信息配置：编号为1。
DEL SBIOCSINFO:ID=1
` 


#### 查询OCS信息配置(SHOW SBIOCSINFO) 
#### 查询OCS信息配置(SHOW SBIOCSINFO) 


功能说明 

本命令用于查询OCS信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|CUSTOM_OCS信息编号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置OCS信息编号。该编号全局唯一。
SUPIRANGEARRAY|SUPI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置SUPI（Subscriber Permanent Identifier，用户永久标识）范围组编号，该编号通过SHOW SBISUPIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何SUPI对应的用户提供计费。
GPSIRANGEARRAY|GPSI范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置GPSI（Generic Public Subscription Identifier，一般公共用户标识）范围组编号，该编号通过SHOW SBIGPSIRANGEARRID命令查询。如果不配置，则该OCS实例可以对任何GPSI对应的用户提供计费。
PLMNRNGARRAY|PLMN范围组编号|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置PLMN（Public Land Mobile Network，公共陆地移动网）范围组编号，用于指定OCS实例可以服务的PLMN范围列表。如果不配置，则该OCS实例可以对任何PLMN对应的用户提供计费。该编号通过SHOW SBIPLMNRANGEARRID命令查询。




命令举例 


`
查询OCS信息配置：编号为1。
SHOW SBIOCSINFO:ID=1

(No.6) : SHOW SBIOCSINFO:ID=1
-----------------CommonS_HTTP_LB_0----------------
操作维护       CUSTOM_OCS信息编号  SUPI范围组编号 GPSI范围组编号 PLMN范围组编号 
--------------------------------------------------------------------------------
复制 修改 删除 1                   1              1              1              
--------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-07-26 11:09:50 耗时: 0.959秒

` 


