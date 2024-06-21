 MME对等PLMN配置 
背景知识 
EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 
配置EPLMN后，移动用户可以在运营商为他提供的不同PLMN之间驻留，允许移动用户选择其他通信网络的服务。 
移动用户可以有多个对等PLMN，但只有一个归属PLMN（HPLMN），移动用户通过IMSI号码提取归属PLMN。 
在多个网络同时为一个移动用户服务时，网络侧通过对等PLMN列表告诉eNodeB和UE：当前网络与归属PLMN 是等同的。业务流程如下： 
 
用户每次附着或跟踪区更新时，当MME完成附着（Attach）或跟踪区更新（TAU）流程时，就通过附着接受（Attach Accept）或跟踪区更新接受（TAU Accept）消息把EPLMN列表信息下发给移动用户。
 
 
移动用户将网络侧下发的EPLMN列表加上当前网络的网络号保存在SIM卡中，下次附着或跟踪区更新接受后刷新EPLMN列表。通过这个过程，移动用户实现通过查询保存着的EPLMN列表来选择连接的网络资源。
 
 
功能描述 
如果不同运营商的网络资源之间或者同一运营商定义的不同PLMN之间需要实现通信网络资源共享。比如共有A、B两个PLMN网络。在B网络信号好的时候，原先登记在A网络的用户的手机可以根据保存在SIM卡上的EPLMN的信息自动重选B网络。此时，需要配置MME对等PLMN。 
注意事项： 
当MME需要为用户提供EPLMN列表时，应该根据软件参数“支持EPLMN组数” （ID：262197）以及“MME对等PLMN配置”，决定是否向用户提供EPLMN列表，以及提供EPLMN的组数。（说明：软件参数取值为0，则不向用户提供EPLMN列表；取值为1，则最多向用户提供5组EPLMN列表；取值为2，则最多向用户提供15组EPLMN列表。） 
MME支持对整个网元配置默认的对等PLMN，也支持根据IMSI号段/跟踪区配置对等PLMN。配置项说明如下： 
 
根据IMSI号段/跟踪区配置对等PLMN
                                配置对等PLMN Profile（
                                ADD MME PLMN PROFILE
                                ），该配置项把EPLMN列表组和PLMN Profile标识关联，方便被多种跟踪区和号码段的组合所引用。
                            
                                配置IMSI号段对等PLMN（
                                ADD MME IMSI TAI PLMN
                                ），该配置项对IMSI号段/跟踪区组合配置PLMN Profile标识。配置后，属于IMSI号段对等PLMN配置内的用户使用对等PLMN功能时，MME从此配置中获取EPLMN列表。
                            
 
 
配置默认对等PLMN
                        默认对等PLMN配置（
                        SET MME PLMN DEFAULT
                        ）用于当不属于IMSI号段对等PLMN配置内的用户使用对等PLMN功能时，MME从此配置中获取EPLMN列表。
                    
 
 
相关主题 
 
默认对等PLMN配置
 
 
对等PLMN Profile配置
 
 
IMSI号段对等PLMN配置
 
 
父主题： [系统配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 默认对等PLMN配置 
# 默认对等PLMN配置 
背景知识 
EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 
移动用户可以在运营商为他提供的不同EPLMN之间驻留，可以自己选择其他通信网络资源来提供服务。 
移动用户每次附着或路由更新时，SGSN通过附着接受或路由更新接受消息把EPLMN列表信息下发给移动用户。 
功能描述 
                当SGSN为移动用户提供EPLMN列表时，如果移动用户对应的IMSI号段已经在“IMSI号段对等PLMN配置（
                [ADD SGSN IMSI RAI PLMN]
                ）”中配置，则SGSN网元根据配置的列表下发EPLMN信息；如果移动用户IMSI号段不在已经配置的列表中，则SGSN根据“默认对等PLMN配置”获取EPLMN列表，下发给RNC和UE。
            
注意事项： 
SGSN根据软件参数“SGSN支持EPLMN组数”，决定向用户提供EPLMN的组数。 
相关主题 
 
设置默认对等PLMN(SET MME PLMN DEFAULT)
 
 
删除默认对等PLMN(DEL MME PLMN DEFAULT)
 
 
查询默认对等PLMN(SHOW MME PLMN DEFAULT)
 
 
父主题： [MME对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置默认对等PLMN(SET MME PLMN DEFAULT) 
## 设置默认对等PLMN(SET MME PLMN DEFAULT) 
命令功能 
该命令用于配置MME支持的默认对等PLMN网络，对等PLMN是指为与终端当前所选择的PLMN处于同等地位、优先级相同的PLMN网络。 
当MME支持对等PLMN，但是基于IMSI号段和跟踪区的对等PLMN没有配置时需要从该配置中获取对等PLMN列表。 
该命令配置成功后，用户每次附着或路由更新时，MME基于此策略给用户分配对等PLMN，并通过附着接受或路由更新接受消息把对等的PLMN信息下发给终端 。 
注意事项 
 
增加该配置前，需要先设置MME携带给终端的对等PLMN的最大组数，命令为： SET MOBILE MANAGEMENT;
 
 
MME携带给终端的对等PLMN组数可设置为0组、5组、15组，0组表示MME不支持对等PLMN。
 
 
配置默认对等PLMN时最多可以配置15组。
 
 
该命令为全局默认配置，如果用户配置了基于IMSI和跟踪区的对等PLMN网络，则优先选择与IMSI号段相同的PLMN网络。
 
 
基于IMSI的对等PLMN配置命令为： ADD MME IMSI TAI PLMN;
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|运营商|参数可选性:必选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code），MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code），移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
命令举例 
设置默认对等PLMN，设置移动国家码为460，移动网号为001。
SET MME PLMN DEFAULT:PLMN="460"-"001"; 
父主题： [默认对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除默认对等PLMN(DEL MME PLMN DEFAULT) 
## 删除默认对等PLMN(DEL MME PLMN DEFAULT) 
命令功能 
该命令用于删除默认对等的PLMN网络。 
执行命令时，不需要输入任何参数，而且执行该命令时，不需要任何其它限制。 
注意事项 
该命令将一次性删除[SET MME PLMN DEFAULT]命令中配置的全部PLMN。
命令举例 
删除所有的默认对等PLMN。
DEL MME PLMN DEFAULT; 
父主题： [默认对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询默认对等PLMN(SHOW MME PLMN DEFAULT) 
## 查询默认对等PLMN(SHOW MME PLMN DEFAULT) 
命令功能 
该命令用于查询MME网元的默认对等PLMN。 
执行该命令时，不需要输入任何参数，执行成功后，显示配置的默认对等PLMN。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|运营商|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
命令举例 
查询所有的默认对等PLMN。
SHOW MME PLMN DEFAULT; 
`
命令 (No.1): SHOW MME PLMN DEFAULT;
操作维护  运营商
----------------
删除      460-001
----------------
记录数 1
命令执行成功（耗时 0.083 秒）。
` 
父主题： [默认对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 对等PLMN Profile配置 
# 对等PLMN Profile配置 
背景知识 
EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 
ZXUN uMAC-SGSN产品支持配置全局默认的对等PLMN，也支持区分用户号段配置对等PLMN。 
功能描述 
区分用户号段/路由区/位置区配置对等PLMN时，由于用户号段＋路由区＋位置区的组合很多，为了提高配置效率，SGSN根据“对等PLMN Profile配置”把EPLMN列表组和PLMN Profile标识关联，用户号段＋路由区＋位置区的组合只需要引用相应的PLMN Profile标识。 
区分用户号码段对等PLMN功能的流程如下： 
                        配置对等PLMN Profile。配置命令为：
                        [ADD SGSN PLMN PROFILE]
                        。
                    
                        如果需要在PLMN Profile中增加运营商，使用命令：
                        [ADD SGSN PLMN]
                        。
                    
                        配置SGSN IMSI号段对等PLMN。参见
                        [ADD SGSN IMSI RAI PLMN]
                        。
                    
注意事项： 
SGSN根据软件参数“SGSN支持EPLMN组数”，决定向用户提供EPLMN的组数。 
相关主题 
 
增加PLMN(ADD MME PLMN)
 
 
删除PLMN(DEL MME PLMN)
 
 
新增对等PLMN Profile配置(ADD MME PLMN PROFILE)
 
 
修改对等PLMN Profile配置(SET MME PLMN PROFILE)
 
 
删除对等PLMN Profile配置(DEL MME PLMN PROFILE)
 
 
查询对等PLMN Profile配置(SHOW MME PLMN PROFILE)
 
 
父主题： [MME对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加PLMN(ADD MME PLMN) 
## 增加PLMN(ADD MME PLMN) 
命令功能 
该命令用于修改已经配置好的某个对等PLMN Profile。如果该PLMN Profile包含的PLMN太少了，则可以使用该命令，在现有的基础上添加一个或者多个PLMN。 
注意事项 
该命令可以新增PROFILE标识和PLMN，但不包括用户别名，如果想增加别名，可以使用修改EPLMN分组配置添加，配置命令为： [SET MME PLMN PROFILE];
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
PLMN|运营商|参数可选性:必选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
命令举例 
增加PLMN，设置PLMN Profile标识为2，移动国家码为460，移动网号为002。
ADD MME PLMN:PROFILEID=2,PLMN="460"-"002"; 
父主题： [对等PLMN Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除PLMN(DEL MME PLMN) 
## 删除PLMN(DEL MME PLMN) 
命令功能 
该命令用于删除已经配置好的某个对等PLMN Profile。如果该PLMN Profile包含的PLMN太多了，则可以使用该命令，在现有的基础上删除一个或者多个PLMN。 
注意事项 
该命令可以根据PLMN Profile标识和PLMN号码单条记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
PLMN|运营商|参数可选性:必选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
命令举例 
删除PLMN Profile标识为2，移动国家码为460，移动网号为002的PLMN。
DEL MME PLMN:PROFILEID=2,PLMN="460"-"002"; 
父主题： [对等PLMN Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增对等PLMN Profile配置(ADD MME PLMN PROFILE) 
## 新增对等PLMN Profile配置(ADD MME PLMN PROFILE) 
命令功能 
该命令用于MME网元新增的对等PLMN分组配置。 
该命令主要用于配置各种组合的PLMN列表，每个列表有一个唯一的PLMN Profile标识。 
该命令配置成功后，对运营商(PLMN)进行了分组，提供给新增配置IMSI号对等PLMN使用。 
注意事项 
 
该命令关联“基于IMSI号段的对等PLMN配置”，配置命令为： ADD MME IMSI TAI PLMN;
 
 
该命令执行后，只需要同步变化表即可生效。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
PLMN|运营商|参数可选性:任选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
新增对等PLMN Profile配置，设置PLMN Profile标识为1，移动国家码为460，移动网号为003。 
ADD MME PLMN PROFILE:PROFILEID=1,PLMN="460"-"003"; 
父主题： [对等PLMN Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改对等PLMN Profile配置(SET MME PLMN PROFILE) 
## 修改对等PLMN Profile配置(SET MME PLMN PROFILE) 
命令功能 
该命令用于修改MME网元的对等PLMN 组配置。 
执行该命令时，需要输入“PLMN Profile标识”，用于确定修改哪个PLMN Profile的配置。 
注意事项 
该命令可以修改已配置成功的PROFILE标识中的PLMN和用户别名。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
PLMN|运营商|参数可选性:任选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
修改PLMN Profile标识为1的对等PLMN Profile配置，移动国家码修改为460，移动网号修改为001。
SET MME PLMN PROFILE:PROFILEID=1,PLMN="460"-"001"; 
父主题： [对等PLMN Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除对等PLMN Profile配置(DEL MME PLMN PROFILE) 
## 删除对等PLMN Profile配置(DEL MME PLMN PROFILE) 
命令功能 
该命令用于删除MME网元的对等PLMN Profile配置。
注意事项 
根据PROFILE标识删除记录，执行该命令之前，需要确认PLMN Profile标识是否在“IMSI号段对等PLMN配置”（查看命令为：[SHOW MME IMSI TAI PLMN]）中被引用。
 
如果没有被IMSI号段对等PLMN配置使用，则可直接执行该命令。
 
 
如果指定的PLMN Profile标识已被IMSI号段对等PLMN配置使用，则不能删除，需要先删除引用该PLMN Profile的配置（删除命令为：DEL MME IMSI TAI PLMN），然后再执行该命令。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
命令举例 
删除PLMN Profile标识为1的PLMN。
DEL MME PLMN PROFILE:PROFILEID=1; 
父主题： [对等PLMN Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询对等PLMN Profile配置(SHOW MME PLMN PROFILE) 
## 查询对等PLMN Profile配置(SHOW MME PLMN PROFILE) 
命令功能 
命令用于查询MME网元的对等PLMN Profile配置。 
该命令按以下方式输入参数，显示对应的信息。 
 
如果不输入任何参数，则显示所有的对等PLMN Profile配置信息。
 
 
如果输入“对等PLMN Profile标识”或“用户别名”，则显示该标识或用户别名对应的对等PLMN Profile配置信息。
 
 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW MME IMSI TAI PLMN。
PLMN|运营商|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
查询所有的对等PLMN Profile配置。
SHOW MME PLMN PROFILE; 
`
命令 (No.1): SHOW MME PLMN PROFILE;
操作维护         PLMN Profile标识   运营商    用户别名
------------------------------------------------------
复制 修改 删除   1                  460-001   
------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [对等PLMN Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# IMSI号段对等PLMN配置 
# IMSI号段对等PLMN配置 
背景知识 
EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 
ZXUN uMAC-SGSN产品支持配置全局默认的对等PLMN，也支持区分用户号段配置对等PLMN。 
功能描述 
当SGSN需要为用户提供EPLMN列表时，属于IMSI号段对等PLMN配置内的用户使用对等PLMN功能时，SGSN根据“IMSI号段对等PLMN配置”获取EPLMN列表。 
区分用户号码段对等PLMN功能的流程如下： 
                        配置对等PLMN Profile。参见
                        [ADD SGSN PLMN PROFILE]
                        。
                    
                        如果需要在PLMN Profile中增加运营商，使用命令：
                        [ADD SGSN PLMN]
                        。
                    
                        配置SGSN IMSI号段对等PLMN。配置命令为：
                        [ADD SGSN IMSI RAI PLMN]
                        。
                    
注意事项： 
SGSN根据软件参数“SGSN支持EPLMN组数”，决定向用户提供EPLMN的组数。 
相关主题 
 
新增MME IMSI对等PLMN配置(ADD MME IMSI TAI PLMN)
 
 
修改MME IMSI对等PLMN配置(SET MME IMSI TAI PLMN)
 
 
删除MME IMSI对等PLMN配置(DEL MME IMSI TAI PLMN)
 
 
查询MME IMSI对等PLMN配置(SHOW MME IMSI TAI PLMN)
 
 
父主题： [MME对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增MME IMSI对等PLMN配置(ADD MME IMSI TAI PLMN) 
## 新增MME IMSI对等PLMN配置(ADD MME IMSI TAI PLMN) 
命令功能 
该命令用于MME新增基于IMSI号段和跟踪区的对等PLMN配置。 
该命令配置成功后，用户每次附着或路由更新时，MME基于此策略给用户分配对等PLMN，并通过附着接受或路由更新接受消息把对等的PLMN信息下发给终端，UE将网络侧下发的对等PLMN列表和当前网络的网络号保存在SIM卡中，直到下次附着或路由更新接受后被刷新。 
注意事项 
 
增加该配置前，需要先设置MME携带给终端的对等PLMN的最大组数，命令为： SET MOBILE MANAGEMENT:MMEEPLMNLISTNUM="5 EPLMNs";
 
 
MME携带给终端的对等PLMN组数可设置为0组、5组、15组， 0组表示MME不支持对等PLMN。
 
 
增加该配置前需要关联对等PLMN Profile配置中“PLMN Profile标识”，命令为： ADD MME PLMN PROFILE;还需要关联跟踪区配置中的“跟踪区标识”，配置命令为： ADD TA;
 
 
当没有配置基于IMSI号段的对等PLMN，但MME支持EPLMN功能时，则系统会取默认对等PLMN配置列表，配置命令为： SET MME PLMN DEFAULT;
 
 
一个IMSI号段最多对应15个PLMN。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行限制的作用，而不需要将每个用户的完整号码都配置上。
ISALLTA|是否适用于所有跟踪区|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对于已选择的IMSI号段，是否是针对所有跟踪区来新增或修改或删除对等PLMN配置。否（NO）：不适用于所有跟踪区，表示只针对某个或部分跟踪区，此时需要输入跟踪区标识。是（YES）：适用于所有跟踪区，此时不需要输入跟踪区标识。
TAID|跟踪区标识|参数可选性:任意单选参数；参数类型:整数；参数范围为:1~65535。|某个IMSI号段可以根据某个跟踪区来进行添加或修改或删除PLMN配置。在MME中一个TAID对应一个跟踪区。当“是否适用于所有跟踪区参数”设置为“否”时，需要输入该参数。在配置该参数前需要先查询跟踪区配置中的“跟踪区标识”，根据已配置成功的跟踪区来设置该参数，查询命令为SHOW TA。最多可以配置16个跟踪区标识。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
PLMN|PLMN|参数可选性:任意单选参数；参数类型:复合参数|PLMN识别号，由MCC和MNC组成，代表一个PLMN范围。
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。此参数关联对等PLMN Profile配置中的“PLMN Profile标识”，需要根据已配置成功的ProfileID来设置该参数，查询命令为SHOW MME PLMN PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。
命令举例 
新增MME IMSI对等PLMN配置，设置IMSI号段为46001，适用于所有路由区，PLMN Profile标识为1。 
ADD MME IMSI TAI PLMN:IMSI="46001",ISALLTA="YES",PROFILEID=1; 
父主题： [IMSI号段对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改MME IMSI对等PLMN配置(SET MME IMSI TAI PLMN) 
## 修改MME IMSI对等PLMN配置(SET MME IMSI TAI PLMN) 
命令功能 
该命令用于根据IMSI号段和跟踪区来修改的对等PLMN配置。
注意事项 
 
该命令必须根据“IMSI号段”和“是否适用于所有跟踪区”两个参数来修改与之匹配的记录。
 
 
“是否适用于所有跟踪区”参数包括YES和NO：选择YES指选择所有跟踪区；选择NO需要添加指定跟踪区标识，“跟踪区标识“，配置命令为： ADD TA。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行限制的作用，而不需要将每个用户的完整号码都配置上。
ISALLTA|是否适用于所有跟踪区|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对于已选择的IMSI号段，是否是针对所有跟踪区来新增或修改或删除对等PLMN配置。否（NO）：不适用于所有跟踪区，表示只针对某个或部分跟踪区，此时需要输入跟踪区标识。是（YES）：适用于所有跟踪区，此时不需要输入跟踪区标识。
TAID|跟踪区标识|参数可选性:任意单选参数；参数类型:整数；参数范围为:1~65535。|某个IMSI号段可以根据某个跟踪区来进行添加或修改或删除PLMN配置。在MME中一个TAID对应一个跟踪区。当“是否适用于所有跟踪区参数”设置为“否”时，需要输入该参数。在配置该参数前需要先查询跟踪区配置中的“跟踪区标识”，根据已配置成功的跟踪区来设置该参数，查询命令为SHOW TA。最多可以配置16个跟踪区标识。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
PLMN|PLMN|参数可选性:任意单选参数；参数类型:复合参数|PLMN识别号，由MCC和MNC组成，代表一个PLMN范围。
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。此参数关联对等PLMN Profile配置中的“PLMN Profile标识”，需要根据已配置成功的ProfileID来设置该参数，查询命令为SHOW MME PLMN PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。
命令举例 
修改IMSI号段为46001，适用于所有路由区的MME IMSI对等PLMN配置，将PLMN Profile标识修改为2。 
SET MME IMSI TAI PLMN:IMSI="46001",ISALLTA="YES",PROFILEID=2; 
父主题： [IMSI号段对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除MME IMSI对等PLMN配置(DEL MME IMSI TAI PLMN) 
## 删除MME IMSI对等PLMN配置(DEL MME IMSI TAI PLMN) 
命令功能 
该命令用于根据IMSI号段和跟踪区删除的对等PLMN配置。
注意事项 
 
该命令必须根据“IMSI号段”和“是否适用于所有跟踪区”两个参数来删除与之匹配的记录。
 
 
“是否适用于所有跟踪区”参数包括YES和NO：选择YES指选择所有跟踪区；选择NO指不适用于所有跟踪区时，需要输入跟踪区标识。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行限制的作用，而不需要将每个用户的完整号码都配置上。
ISALLTA|是否适用于所有跟踪区|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对于已选择的IMSI号段，是否是针对所有跟踪区来新增或修改或删除对等PLMN配置。否（NO）：不适用于所有跟踪区，表示只针对某个或部分跟踪区，此时需要输入跟踪区标识。是（YES）：适用于所有跟踪区，此时不需要输入跟踪区标识。
TAID|跟踪区标识|参数可选性:任意单选参数；参数类型:整数；参数范围为:1~65535。|某个IMSI号段可以根据某个跟踪区来进行添加或修改或删除PLMN配置。在MME中一个TAID对应一个跟踪区。当“是否适用于所有跟踪区参数”设置为“否”时，需要输入该参数。在配置该参数前需要先查询跟踪区配置中的“跟踪区标识”，根据已配置成功的跟踪区来设置该参数，查询命令为SHOW TA。最多可以配置16个跟踪区标识。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
PLMN|PLMN|参数可选性:任意单选参数；参数类型:复合参数|PLMN识别号，由MCC和MNC组成，代表一个PLMN范围。
命令举例 
IMSI号段为46001，适用于所有路由区的MME IMSI对等PLMN配置。 
DEL MME IMSI TAI PLMN:IMSI="46001",ISALLTA="YES"; 
父主题： [IMSI号段对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME IMSI对等PLMN配置(SHOW MME IMSI TAI PLMN) 
## 查询MME IMSI对等PLMN配置(SHOW MME IMSI TAI PLMN) 
命令功能 
该命令用于MME查询IMSI号段对等PLMN配置关系。 
 
该命令不带参数，可一次性查询出所有的配置记录。
 
 
该命令也可根据IMSI号段查询与之匹配的记录。
 
 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行限制的作用，而不需要将每个用户的完整号码都配置上。
TAID|跟踪区标识|参数可选性:任意单选参数；参数类型:整数；参数范围为:1~65535。|某个IMSI号段可以根据某个跟踪区来进行添加或修改或删除PLMN配置。在MME中一个TAID对应一个跟踪区。当“是否适用于所有跟踪区参数”设置为“否”时，需要输入该参数。在配置该参数前需要先查询跟踪区配置中的“跟踪区标识”，根据已配置成功的跟踪区来设置该参数，查询命令为SHOW TA。最多可以配置16个跟踪区标识。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
PLMN|PLMN|参数可选性:任意单选参数；参数类型:复合参数|PLMN识别号，由MCC和MNC组成，代表一个PLMN范围。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行限制的作用，而不需要将每个用户的完整号码都配置上。
ISALLTA|是否适用于所有跟踪区|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|对于已选择的IMSI号段，是否是针对所有跟踪区来新增或修改或删除对等PLMN配置。否（NO）：不适用于所有跟踪区，表示只针对某个或部分跟踪区，此时需要输入跟踪区标识。是（YES）：适用于所有跟踪区，此时不需要输入跟踪区标识。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数。|某个IMSI号段可以根据某个跟踪区来进行添加或修改或删除PLMN配置。在MME中一个TAID对应一个跟踪区。当“是否适用于所有跟踪区参数”设置为“否”时，需要输入该参数。在配置该参数前需要先查询跟踪区配置中的“跟踪区标识”，根据已配置成功的跟踪区来设置该参数，查询命令为SHOW TA。最多可以配置16个跟踪区标识。
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|PLMN识别号，由MCC和MNC组成，代表一个PLMN范围。
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数。|对等PLMN Profile的编号。此参数关联对等PLMN Profile配置中的“PLMN Profile标识”，需要根据已配置成功的ProfileID来设置该参数，查询命令为SHOW MME PLMN PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。
命令举例 
查询IMSI号段为46002的对等PLMN配置。 
SHOW MME IMSI TAI PLMN:IMSI="46002"; 
`
命令 (No.1): SHOW MME IMSI TAI PLMN:IMSI="46002";
操作维护         IMSI号段   是否适用于所有跟踪区   跟踪区标识   PLMN    PLMN Profile标识   用户别名
-------------------------------------------------------------------------------------------------------
复制 修改 删除   46002      是                                          1                  
-------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [IMSI号段对等PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
