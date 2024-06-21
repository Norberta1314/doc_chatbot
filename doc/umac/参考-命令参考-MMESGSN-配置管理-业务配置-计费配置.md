 计费配置 
背景知识 
SGSN输出的计费话单包括移动性管理话单M-CDR、会话管理话单S-CDR、短消息始呼SMS-MO-CDR和终呼话单SMS-MT-CDR等。 
SGSN的话单输出到计费网关CG，CG可以是多个。 
计费特性就是计费方法标识，运营商可以对不同用户或不同APN采用不同计费方法，比如普通计费、预付费、平率计费和热计费等。 
用户可以签约计费特性，若用户没有签约计费特性，则使用缺省计费特性，也就是指在SGSN配置的计费特性。 
计费模式分类： 
 
用户归属本SGSN，则为归属。
 
 
用户不归属本SGSN，PDP使用的是本SGSN所在运营商的GGSN，对此PDP而言则为拜访。
 
 
用户不归属本SGSN，PDP使用的是用户归属运营商的GGSN，对此PDP而言则为漫游。
 
 
不同计费模式的缺省计费特性可以不同。 
不同网号的缺省计费特性可以不同。 
只有S-CDR的计费模式才存在漫游和拜访。 
M-CDR和SMS-CDR则只能判断是否归属，当不是归属时，可以指定计费模式为拜访还是漫游。 
对于非归属本SGSN用户，当用户签约计费特性时，也可以根据配置确定是优先用签约的计费特性还是SGSN配置的缺省计费特性，以便于对非归属用户的计费方法控制。 
功能描述 
计费配置是SGSN的一项基本配置，SGSN根据本配置进行计费话单的输出及话单中计费特性参数控制。 
本配置包括APN计费模板配置、指定出话单时间配置、DNS解析类APN配置、多网号用户计费特性配置、缺省计费特性配置、Ga接口配置和基于IMSI号段过滤CDR配置。 
在配置指定话单时间配置和DNS解析类APN配置前，需要先配置基于APN计费模板配置。 
相关主题 
 
APN计费模板配置
 
 
指定出话单时间配置
 
 
DNS解析类APN配置
 
 
缺省计费特性配置
 
 
多网号用户计费特性配置
 
 
Ga接口配置
 
 
IMSI号段过滤CDR配置
 
 
本地话单策略配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# APN计费模板配置 
# APN计费模板配置 
背景知识 
计费策略包括计费方式（按流量还是按时长）、最大时长限制、最大流量限制、部分话单最大碎片数、无线资源占用时长、PDP非激活时长和费率时段等。 
SGSN根据计费策略来产生会话管理话单S-CDR。 
当不同的APN需要不同的计费策略时，需要基于APN来设置计费策略。 
并不是每个APN都采用不同的计费策略，而计费策略的信息又比较多，所以引入计费模板的概念，即一个计费策略作为一个计费模板（就是为该计费策略指定一个编号，称为计费模板号），具有相同计费策略的APN配置同一个计费模板号，当APN比较多时，可以简化配置。 
功能描述 
当不同的APN具有不同的计费策略时，需要基于APN来设置计费策略，配置流程如下所示。 
                        配置计费策略模板（计费策略+模板号），该配置命令为：
                        [ADD APNCTPL]
                        。
                    
                        在APN配置中配置APN计费策略对应的计费模板号，参见
                        [ADD GPRS APN]
                        。
                    
系统提供一个缺省计费策略，其计费模板号为0；缺省计费策略是：按流量计费、计费流量门限是4096000000、碎片话单最大个数为5、无线资源占用时长为60分钟、PDP非激活时长为1440分钟，费率时段为0点到24点。 
缺省计费策略不可修改和删除。 
如果APN并没有特殊的计费策略需求，则不需要配置该APN和计费模板的关系，采用缺省计费策略。 
相关主题 
 
新增APN计费模板配置(ADD APNCTPL)
 
 
修改APN计费模板配置(SET APNCTPL)
 
 
删除APN计费模板配置(DEL APNCTPL)
 
 
查询APN计费模板配置(SHOW APNCTPL)
 
 
修改APN计费模板费率时段(SET APNCTPL RATE)
 
 
查询APN计费模板费率时段(SHOW APNCTPL RATE)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增APN计费模板配置(ADD APNCTPL) 
## 新增APN计费模板配置(ADD APNCTPL) 
命令功能 
该命令用于新增APN计费模板配置。当新增一种计费策略时，使用该命令。成功后，不同的APN可以使用不同时长或者流量的计费策略。 
一个APN计费模板就是一种计费策略，被[ADD GPRS APN]关联。
注意事项 
 
建议设置计费方式为TIMEFLOW，以保证话单安全。
 
 
建议计费时间门限设置为1小时的整倍数，以提高系统扫描的效率。
 
 
设置部分话单最大碎片数为一个合理值，可以减少部分话单数。
 
 
无线承载释放时长和无活动PDP存在时长为计费时间门限的整倍数，这两个参数不要太大，建议为计费时间门限的两倍，以减少系统资源的使用。 
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~31。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
TYPE|计费方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:TIMEFLOW。|该参数表示计费方式，取值含义如下：TIME：定时长计费方式FLOW：定流量计费方式TIMEFLOW：定时长+流量计费方式
TIMELMT|计费时间门限(分钟)|参数可选性:必选参数；参数类型:整数；参数范围为:5~4320。默认值:60。|该参数表示定时长计费时间门限，只有在计费方式为定时长或定时长+流量计费时才有意义，建议配置为1小时的整倍数。
FLOWLMT|计费流量门限(字节)|参数可选性:必选参数；参数类型:整数；参数范围为:102400~4096000000。默认值:10485760。|该参数表示定流量计费的流量门限，只有在计费方式为定流量或定时长+流量计费时才有意义，用户使用流量（上行+下行）超过这个值，产生一张流量门限话单。
MAXFRAG|部分话单最大碎片数|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。默认值:5。|该参数表示部分话单携带的最大碎片数，推荐值为5。一个PDP的碎片话单累计达到这个值后将产生一个部分话单，将这些碎片话单一起发送给计费中心。
RABTIMELMT|无线承载释放时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:30~4320。默认值:60。|该参数表示当无线承载无流量的时间超过这个值后，系统将这个承载释放，节约系统无线资源。
PDPTIMELMT|无活动PDP存在时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:360~4294967295。默认值:1440。|该参数表示当PDP无活动时间超过这个值后，系统将这个PDP释放，及时释放系统PDP资源，因为这个PDP可能已经被其他网元释放了。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示计费模板的名称。
命令举例 
新增APN计费模板，计费模板标识为0，计费方式是流量和时间，计费时间门限为120分钟，计费流量门限为4096000000字节，部分话单最大碎片数为6，无线承载释放时间为360分钟，无活动PDP存在时长为360分钟。
ADD APNCTPL:TPLID=1,TYPE="TIMEFLOW",TIMELMT=120,FLOWLMT=4096000000,MAXFRAG=6,RABTIMELMT=360,PDPTIMELMT=360; 
父主题： [APN计费模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改APN计费模板配置(SET APNCTPL) 
## 修改APN计费模板配置(SET APNCTPL) 
命令功能 
该命令用于修改APN计费模板配置。 
该命令可以同时或者分别修改APN计费模板配置的计费方式、计费时间门限，计费流量门限、部分话单最大碎片数、无线承载释放时间以及无活动PDP存在时长等属性。 
注意事项 
 
建议设置计费方式为TIMEFLOW，以保证话单安全；
 
 
建议计费时间门限设置为1小时的整倍数，以提高系统扫描的效率;
 
 
设置部分话单最大碎片数为一个合理值，可以减少部分话单数； 
 
 
无线承载释放时长和无活动PDP存在时长为计费时间门限的整倍数，这两个参数不要太大，建议为计费时间门限的两倍，以减少系统资源的使用。 
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~31。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
TYPE|计费方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示计费方式，取值含义如下：TIME：定时长计费方式FLOW：定流量计费方式TIMEFLOW：定时长+流量计费方式
TIMELMT|计费时间门限(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:5~4320。|该参数表示定时长计费时间门限，只有在计费方式为定时长或定时长+流量计费时才有意义，建议配置为1小时的整倍数。
FLOWLMT|计费流量门限(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:102400~4096000000。|该参数表示定流量计费的流量门限，只有在计费方式为定流量或定时长+流量计费时才有意义，用户使用流量（上行+下行）超过这个值，产生一张流量门限话单。
MAXFRAG|部分话单最大碎片数|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|该参数表示部分话单携带的最大碎片数，推荐值为5。一个PDP的碎片话单累计达到这个值后将产生一个部分话单，将这些碎片话单一起发送给计费中心。
RABTIMELMT|无线承载释放时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:30~4320。|该参数表示当无线承载无流量的时间超过这个值后，系统将这个承载释放，节约系统无线资源。
PDPTIMELMT|无活动PDP存在时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:360~4294967295。|该参数表示当PDP无活动时间超过这个值后，系统将这个PDP释放，及时释放系统PDP资源，因为这个PDP可能已经被其他网元释放了。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示计费模板的名称。
命令举例 
修改标识为1的APN计费模板，将计费方式修改是流量和时间，计费时间门限修改为240分钟，计费流量门限修改为104857600字节，部分话单最大碎片数修改为为9，无线承载释放时间修改为480分钟，无活动PDP存在时长改为960分钟。
SET APNCTPL:TPLID=1,TYPE="TIMEFLOW",TIMELMT=240,FLOWLMT=104857600,MAXFRAG=9,RABTIMELMT=480,PDPTIMELMT=960; 
父主题： [APN计费模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除APN计费模板配置(DEL APNCTPL) 
## 删除APN计费模板配置(DEL APNCTPL) 
命令功能 
该命令用于删除APN计费模板配置。
注意事项 
 
删除前要保证该计费模板没有被GPRS APN 关联，请参考命令SHOW GPRS APN。
 
 
计费模板标识为0的记录不能删除。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~31。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
命令举例 
删除标识为2的APN计费模板。
DEL APNCTPL:TPLID=2; 
父主题： [APN计费模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询APN计费模板配置(SHOW APNCTPL) 
## 查询APN计费模板配置(SHOW APNCTPL) 
命令功能 
该命令用于查询APN计费模板配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
TYPE|计费方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示计费方式，取值含义如下：TIME：定时长计费方式FLOW：定流量计费方式TIMEFLOW：定时长+流量计费方式
TIMELMT|计费时间门限(分钟)|参数可选性:任选参数；参数类型:整数。|该参数表示定时长计费时间门限，只有在计费方式为定时长或定时长+流量计费时才有意义，建议配置为1小时的整倍数。
FLOWLMT|计费流量门限(字节)|参数可选性:任选参数；参数类型:整数。|该参数表示定流量计费的流量门限，只有在计费方式为定流量或定时长+流量计费时才有意义，用户使用流量（上行+下行）超过这个值，产生一张流量门限话单。
MAXFRAG|部分话单最大碎片数|参数可选性:任选参数；参数类型:整数。|该参数表示部分话单携带的最大碎片数，推荐值为5。一个PDP的碎片话单累计达到这个值后将产生一个部分话单，将这些碎片话单一起发送给计费中心。
RABTIMELMT|无线承载释放时间(分钟)|参数可选性:任选参数；参数类型:整数。|该参数表示当无线承载无流量的时间超过这个值后，系统将这个承载释放，节约系统无线资源。
PDPTIMELMT|无活动PDP存在时长(分钟)|参数可选性:任选参数；参数类型:整数。|该参数表示当PDP无活动时间超过这个值后，系统将这个PDP释放，及时释放系统PDP资源，因为这个PDP可能已经被其他网元释放了。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示计费模板的名称。
命令举例 
查询已配置的APN计费模板信息。
SHOW APNCTPL; 
`
命令 (No.1): SHOW APNCTPL;
操作维护         计费模板标识   计费方式     计费时间门限(分钟)   计费流量门限(字节)   部分话单最大碎片数   无线承载释放时间(分钟)   无活动PDP存在时长(分钟)   用户别名
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   0              流量和时间   60                   10485760             5                    60                       1440                      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [APN计费模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改APN计费模板费率时段(SET APNCTPL RATE) 
## 修改APN计费模板费率时段(SET APNCTPL RATE) 
命令功能 
该命令用于修改计费模板费率时段。当计费模板需要在不同时间按不同标准收费时，使用该命令。设置成功后，每到该命令设置的一个时刻，系统将产生一张费率切换的碎片话单。
注意事项 
 
对于每个计费模板，每天最多可以设置10个不同的费率时段。
 
 
设置不同的费率时段越多，导致系统出的碎片话单越多，将影响系统负荷。
 
 
只能在整点和半点设置。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~31。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
TIME|费率时段|参数可选性:必选参数；参数类型:复合参数|该参数表示计费时段，每个时段可以有不同的费率折扣。
TIME_F|起始时间(HH:MM)|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示一个费率时段的起始时间。
TIME_T|结束时间(HH:MM)|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示一个费率时段的结束时间。
RATE|费率折扣|参数可选性:必选参数；参数类型:整数；参数范围为:0~100。|该参数表示一个费率时段的费率折扣。
命令举例 
修改标识为1的计费模板费率时段：在00:00-02:00之间的费率折扣为20%、在02:00-04:00之间的费率折扣为30%、在04:00-06:30之间的费率折扣为60%、在06:30-09:00之间的费率折扣为50%、在09:00-11:30之间的费率折扣为40%、在11:30-14:00之间的费率折扣为20%、在14:00-17:00之间的费率折扣为30%、在17:00-20:00之间的费率折扣为20%、在20:00-22:30之间的费率折扣为10%、在22:30-00:00之间的费率折扣为20%。
SET APNCTPL RATE:TPLID=1,TIME="00:00"-"02:00"-"20"&"02:00"-"04:00"-"30"&"04:00"-"06:30"-"60"&"06:30"-"09:00"-"50"&"09:00"-"11:30"-"40"&"11:30"-"14:00"-"20"&"14:00"-"17:00"-"30"&"17:00"-"20:00"-"20"&"20:00"-"22:30"-"10"&"22:30"-"24:00"-"20"; 
父主题： [APN计费模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询APN计费模板费率时段(SHOW APNCTPL RATE) 
## 查询APN计费模板费率时段(SHOW APNCTPL RATE) 
命令功能 
该命令用于查询APN计费模板费率时段。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数。|该参数为计费模板标识，不同的模板可以实现不同的计费策略。
TIME_F|起始时间(HH:MM)|参数可选性:任选参数；参数类型:字符型。|该参数表示一个费率时段的起始时间。
TIME_T|结束时间(HH:MM)|参数可选性:任选参数；参数类型:字符型。|该参数表示一个费率时段的结束时间。
RATE|费率折扣|参数可选性:任选参数；参数类型:整数。|该参数表示一个费率时段的费率折扣。
命令举例 
查询已配置的APN计费模板费率时段。
SHOW APNCTPL RATE; 
`
命令 (No.1): SHOW APNCTPL RATE
操作维护  计费模板标识   起始时间(HH:MM)   结束时间(HH:MM)   费率折扣
---------------------------------------------------------------------
修改      0              00:30             02:00             80
修改      1              00:00             24:00             100
修改      3              00:00             24:00             100
修改      6              00:00             24:00             100
修改      10             00:00             24:00             100
---------------------------------------------------------------------
记录数 5
命令执行成功（耗时 0.15 秒）。
` 
父主题： [APN计费模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 指定出话单时间配置 
# 指定出话单时间配置 
背景知识 
            
            定点产生话单，即指定一天中的某一个或多个半点或整点时间点产生S-CDR话单。
        
功能描述 
话单时间超长会导致计费中心处理出问题时，根据计费中心能够容忍的话单时长和CG负荷综合考虑，配置指定一天中任何一个或多个半点或整点产生话单，指定的时间点越多，产生的话单就越多，CG的负荷会越大，所以需要综合考虑来指定出话单的时间。 
不同的计费模板可以配置不同定点产生话单。系统也可以配置一个统一的定点话单时间并指定为缺省，计费模板没有配置特定的定点话单产生时间时，采用缺省定点话单时间来产生定点话单。 
相关主题 
 
设置出话单时间(SET CDR TIME)
 
 
增加时间(ADD TIME)
 
 
删除时间(DEL TIME)
 
 
清空出话单时间(CLEAR CDR TIME)
 
 
查询出话单时间(SHOW CDR TIME)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置出话单时间(SET CDR TIME) 
## 设置出话单时间(SET CDR TIME) 
命令功能 
该命令用于对某个或所有计费模板设置产生管理话单的时间点，当需要指定一天中的某些整点或者半点出话单时，使用本命令。本命令执行成功后，关联本计费模板的所有APN的PDP在设置的时刻产生管理话单。 
由于一个计费模板可以被多个APN关联，因此，关联这个计费模板的所有APN的PDP都会在这些整点或者半点产生话单。 
管理话单就是某些APN在某些特定的时刻生成的部分话单。本命令产生的话单的原因可以使用CAUSE来区分，如果选择Tariff Time Change，将只会出部分话单的一个碎片；否则直接产生部分话单， CauseForRecClosing为managementIntervention(20)。 
注意事项 
 
一天最多可配置10个产生管理话单时刻。
 
 
配置过多的管理话单时间，将导致过多的话单产生，影响系统性能。 
 
 
该命令指定出话单的时间是计费模板的属性之一，配置命令参见ADD APNCTPL。 
 
 
计费模板配置需要被APN配置管理，配置命令参见ADD GPRS APN。 
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ISDEFAULT|是否缺省配置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定是否缺省配置。如果是缺省配置，对于没有使用命令SET CDR TIME配置的计费模板，都使用这个缺省配置。其取值含义如下所示。NO： 非缺省YES：缺省
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数用于设置产生管理话单时间的计费模板，如果ISDEFAULT指示是缺省配置，则不能指定本参数。
CDRTIME|出话单时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置产生管理话单的时间，最多可以配置10个，而且不能重合，且只能配置在整点或者半点。
CAUSE|出话单原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置产生管理话单的原因，取值如下所示。Tariff Time Change：产生碎片话单tariffTime(1)Management Intervention：产生部分话单managementIntervention(20)
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数对产生管理话单的记录指定名称。
命令举例 
设置产生管理话单时间，非缺省配置，计费模板标识为1，出管理话单时间为02:00以及02:30，出话单原因为费率改变，用户别名为zte。
SET CDR TIME:TPLID=1,CDRTIME="02:00"&"02:30",CAUSE="Tariff Time Change",NAME="zte"; 
父主题： [指定出话单时间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加时间(ADD TIME) 
## 增加时间(ADD TIME) 
命令功能 
该命令用于对某个计费模板增加产生管理话单的时间点。当需要指定一天中的某些整点或者半点产生话单时，使用本命令。
注意事项 
 
一天最多可配置10个产生管理话单时刻。
 
 
配置过多的管理话单时间，将导致过多的话单产生，影响系统性能。 
 
 
该命令增加的指定出话单的时间是计费模板的属性之一，配置命令参见ADD APNCTPL。
 
 
计费模板配置需要被APN配置管理，配置命令参见ADD GPRS APN。 
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ISDEFAULT|是否缺省配置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定是否缺省配置。如果是缺省配置，对于没有使用命令SET CDR TIME配置的计费模板，都使用这个缺省配置。其取值含义如下所示。NO： 非缺省YES：缺省
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数用于设置产生管理话单时间的计费模板，如果ISDEFAULT指示是缺省配置，则不能指定本参数。
CDRTIME|出话单时间|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置产生管理话单的时间，最多可以配置10个，而且不能重合，且只能配置在整点或者半点。
命令举例 
为非缺省配置、标识为1的计费模板增加产生管理话单时间，增加在01:00出话单。
ADD TIME:TPLID=1,CDRTIME="01:00"; 
父主题： [指定出话单时间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除时间(DEL TIME) 
## 删除时间(DEL TIME) 
命令功能 
该命令用于删除某个计费模板部分管理话单产生的时间点。当需要删除指定一天中某些管理话单产生时间点时，使用本命令。
注意事项 
如果全部删除管理话单产生时间，配置命令参见：[CLEAR CDR TIME]。
参数说明 
标识|名称|类型|说明
---|---|---|---
ISDEFAULT|是否缺省配置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定是否缺省配置。如果是缺省配置，对于没有使用命令SET CDR TIME配置的计费模板，都使用这个缺省配置。其取值含义如下所示。NO： 非缺省YES：缺省
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数用于设置产生管理话单时间的计费模板，如果ISDEFAULT指示是缺省配置，则不能指定本参数。
CDRTIME|出话单时间|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置产生管理话单的时间，最多可以配置10个，而且不能重合，且只能配置在整点或者半点。
命令举例 
删除产生管理话单时间，非缺省配置，计费模板标识为1，删除在01:00出话单。
DEL TIME:ISDEFAULT="NO",TPLID=1,CDRTIME="01:00"; 
父主题： [指定出话单时间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 清空出话单时间(CLEAR CDR TIME) 
## 清空出话单时间(CLEAR CDR TIME) 
命令功能 
该命令用于删除某个计费模板所有产生管理话单的时间点。当需要删除指定一天中所有产生管理话单的时间点时，使用本命令。
注意事项 
如果只删除部分管理话单产生时间，配置命令参见：[DEL TIME]。
参数说明 
标识|名称|类型|说明
---|---|---|---
ISDEFAULT|是否缺省配置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定是否缺省配置。如果是缺省配置，对于没有使用命令SET CDR TIME配置的计费模板，都使用这个缺省配置。其取值含义如下所示。NO： 非缺省YES：缺省
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数用于设置产生管理话单时间的计费模板，如果ISDEFAULT指示是缺省配置，则不能指定本参数。
命令举例 
清空标识为1的计费模块的产生管理话单时间。
CLEAR CDR TIME:ISDEFAULT="NO",TPLID=1; 
父主题： [指定出话单时间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询出话单时间(SHOW CDR TIME) 
## 查询出话单时间(SHOW CDR TIME) 
命令功能 
该命令用于查询产生管理话单时间。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ISDEFAULT|是否缺省配置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定是否缺省配置。如果是缺省配置，对于没有使用命令SET CDR TIME配置的计费模板，都使用这个缺省配置。其取值含义如下所示。NO： 非缺省YES：缺省
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数用于设置产生管理话单时间的计费模板，如果ISDEFAULT指示是缺省配置，则不能指定本参数。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ISDEFAULT|是否缺省配置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定是否缺省配置。如果是缺省配置，对于没有使用命令SET CDR TIME配置的计费模板，都使用这个缺省配置。其取值含义如下所示。NO： 非缺省YES：缺省
TPLID|计费模板标识|参数可选性:任选参数；参数类型:整数。|该参数用于设置产生管理话单时间的计费模板，如果ISDEFAULT指示是缺省配置，则不能指定本参数。
CDRTIME|出话单时间|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|该参数用于设置产生管理话单的时间，最多可以配置10个，而且不能重合，且只能配置在整点或者半点。
CAUSE|出话单原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置产生管理话单的原因，取值如下所示。Tariff Time Change：产生碎片话单tariffTime(1)Management Intervention：产生部分话单managementIntervention(20)
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数对产生管理话单的记录指定名称。
命令举例 
查询已配置的产生管理话单时间。
SHOW CDR TIME; 
`
命令 (No.1): SHOW CDR TIME;
操作维护 是否缺省配置 计费模板标识 出话单时间 出话单原因 用户别名 
---------------------------------------------------------------------------
修改  否 1 02:00&02:30 费率改变 zte 
修改  是   无  
---------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.063 秒）。
` 
父主题： [指定出话单时间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# DNS解析类APN配置 
# DNS解析类APN配置 
背景知识 
            
            如果为APN服务的GGSN是SGSN通过对APN FQDN进行DNS查询得到的，则该APN称为DNS解析类APN。
        
功能描述 
当DNS解析类APN需要特殊计费策略，设置双栈支持、DT属性、过滤S-CDR时，需要进行本配置，配置原则如下： 
 
DNS解析类APN不使用缺省计费策略时，则在本配置中配置计费模板号。用户进行该APN的业务时，SGSN根据计费模板号对应的计费策略来产生会话管理话单S-CDR。
 
 
DNS解析类APN对应的GGSN都支持双栈，则在本配置中配置APN为支持双栈。SGSN给GGSN发消息创建PDP上下文请求时，根据本配置确定终端用户地址中地址类型参数填写，终端请求双栈而GGSN也支持双栈时，则终端用户地址中地址类型为双栈。
 
 
DNS解析类APN对应的GGSN都支持DT时，则在本配置中配置该APN为支持DT，SGSN决策会话是否能够DT时则判断为GGSN支持DT。
 
 
DNS解析类APN不需要输出会话管理类话单S-CDR时，则在配置中配置APPN为不输出话单，SGSN对该APN的所有会话都不产生S-CDR。
 
 
相关主题 
 
新增DNS解析类APN配置(ADD DNSAPNCHG)
 
 
修改DNS解析类APN配置(SET DNSAPNCHG)
 
 
删除DNS解析类APN配置(DEL DNSAPNCHG)
 
 
查询DNS解析类APN配置(SHOW DNSAPNCHG)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增DNS解析类APN配置(ADD DNSAPNCHG) 
## 新增DNS解析类APN配置(ADD DNSAPNCHG) 
命令功能 
APN在GGSN中用于标识一个指定的外部PDN，SGSN可根据用户在PDP上下文中携带的APN，通过DNS解析结果或本地配置信息得到与此APN对应的GGSN地址。 
如果为接入某个APN的用户服务的GGSN是SGSN通过对APN的FQDN（Fully Qualified Domain Name，全称域名）进行DNS解析得到的，则该APN称为DNS解析类APN。 
该命令用于设置DNS解析类APN的相关属性，包括如下内容： 
1、对接入此类APN的用户，SGSN是否使用指定的计费策略对用户计费。 
2、对接入此类APN的用户，GGSN是否支持启用RNC与GGSN之间的DT（Direct Tunnel，直连隧道）功能。 
3、对接入此类APN的用户，SGSN是否通过IPv4/IPv6/IPv4v6地址为MS提供业务，使MS可以用IPv4/IPv6/IPv4v6地址进行数据传输。 
4、对接入此类APN的用户，SGSN是否产生S-CDR话单。 
注意事项 
此功能适用于SGSN网元。 
如果对接入此类APN的用户，SGSN使用指定的计费策略对用户计费，则先需要通过[ADD APNCTPL]命令配置计费模板。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|表示DNS解析类APN的名称。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnAPN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置DNS解析类APN的名称为“zte.com.cn.mnc011.mcc460.gprs”
CHGTPL|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。默认值:0。|表示DNS解析类APN关联的计费模板标识，表示对接入此APN的用户，SGSN使用指定计费模板的计费策略对用户计费。该参数的取值是通过ADD APNCTPL命令配置的参数“TPLID”。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|配置SGSN对此类APN解析获取的GGSN是否支持DT功能。配置为“不支持”：表示GGSN不支持DT功能。配置为“支持”：表示GGSN支持DT功能。配置为“根据签约APN信息决策是否支持DT”：表示根据MS在HLR的的签约信息确定GGSN是否支持DT功能。在UMTS网络中，分别在RNC与SGSN、SGSN与GGSN之间建立GTP-U通道的（Indirect Tunnel）来处理用户面数据。如果启用了DT（Direct Tunnel，直连隧道）功能，则将RNC与SGSN、SGSN与GGSN之间用户面的两段隧道（Indirect Tunnel）优化为一段隧道，优化后用户面转发不经过SGSN，而直接在RNC和GGSN之间建立GTP-U隧道，通过节省用户面资源降低了保证运营商的资金投入和运营成本，同时也优化了UMTS网络用户面的性能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|配置SGSN对此类APN解析获取的GGSN是否支持双栈功能（MS是否可以用IPv4/IPv6/IPv4v6地址进行数据传输）。配置为“不支持”时，GGSN不支持双栈功能。配置为“支持”时，GGSN支持双栈功能。“默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK 在SGSN使用DNS对APN进行解析获取GGSN IP地址情况下，GGSN是否支持双栈功能，除了受ADD DNSAPNCHG命令的控制，还受到ADD DUAL STACK IP命令配置结果的控制。SGSN将解析出的GGSN IP地址与ADD DUAL STACK IP命令配置的GGSN IP地址列表进行比较，如果解析出的GGSN IP地址在ADD DUAL STACK IP命令配置的GGSN IP地址列表中，则表示此GGSN支持双栈功能。
SCDRFLT|过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|配置对接入此类APN的MS，SGSN是否生成S-CDR话单。配置为“是”时，SGSN不生成S-CDR话单。配置为“否”时，SGSN生成S-CDR话单。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
新增DNS解析类APN，APN名称为zte.com.cn.mnc460.mcc001.gprs，计费模板标识为1，不支持DT功能，不支持终端双栈功能。
ADD DNSAPNCHG:APN="zte.com.cn.mnc460.mcc001.gprs",CHGTPL=1; 
父主题： [DNS解析类APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改DNS解析类APN配置(SET DNSAPNCHG) 
## 修改DNS解析类APN配置(SET DNSAPNCHG) 
命令功能 
该命令用于修改DNS解析类APN的配置数据，包括如下内容： 
1、对接入此类APN的用户，SGSN是否使用指定的计费策略对用户计费。 
2、对接入此类APN的用户，GGSN是否支持启用RNC与GGSN之间的DT（Direct Tunnel，直连隧道）功能。 
3、对接入此类APN的用户，SGSN是否通过IPv4/IPv6/IPv4v6地址为MS提供业务，使MS可以用IPv4/IPv6/IPv4v6地址进行数据传输。 
4、对接入此类APN的用户，SGSN是否产生S-CDR话单。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|表示DNS解析类APN的名称。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnAPN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置DNS解析类APN的名称为“zte.com.cn.mnc011.mcc460.gprs”
CHGTPL|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|表示DNS解析类APN关联的计费模板标识，表示对接入此APN的用户，SGSN使用指定计费模板的计费策略对用户计费。该参数的取值是通过ADD APNCTPL命令配置的参数“TPLID”。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置SGSN对此类APN解析获取的GGSN是否支持DT功能。配置为“不支持”：表示GGSN不支持DT功能。配置为“支持”：表示GGSN支持DT功能。配置为“根据签约APN信息决策是否支持DT”：表示根据MS在HLR的的签约信息确定GGSN是否支持DT功能。在UMTS网络中，分别在RNC与SGSN、SGSN与GGSN之间建立GTP-U通道的（Indirect Tunnel）来处理用户面数据。如果启用了DT（Direct Tunnel，直连隧道）功能，则将RNC与SGSN、SGSN与GGSN之间用户面的两段隧道（Indirect Tunnel）优化为一段隧道，优化后用户面转发不经过SGSN，而直接在RNC和GGSN之间建立GTP-U隧道，通过节省用户面资源降低了保证运营商的资金投入和运营成本，同时也优化了UMTS网络用户面的性能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置SGSN对此类APN解析获取的GGSN是否支持双栈功能（MS是否可以用IPv4/IPv6/IPv4v6地址进行数据传输）。配置为“不支持”时，GGSN不支持双栈功能。配置为“支持”时，GGSN支持双栈功能。“默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK 在SGSN使用DNS对APN进行解析获取GGSN IP地址情况下，GGSN是否支持双栈功能，除了受ADD DNSAPNCHG命令的控制，还受到ADD DUAL STACK IP命令配置结果的控制。SGSN将解析出的GGSN IP地址与ADD DUAL STACK IP命令配置的GGSN IP地址列表进行比较，如果解析出的GGSN IP地址在ADD DUAL STACK IP命令配置的GGSN IP地址列表中，则表示此GGSN支持双栈功能。
SCDRFLT|过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置对接入此类APN的MS，SGSN是否生成S-CDR话单。配置为“是”时，SGSN不生成S-CDR话单。配置为“否”时，SGSN生成S-CDR话单。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
修改名称为zte.com.cn.mnc460.mcc001.gprs的DNS解析类APN，将计费模板标识修改为0，支持DT功能，支持终端双栈功能。
SET DNSAPNCHG:APN="zte.com.cn.mnc460.mcc001.gprs",CHGTPL=0,DTSPRT="YES",DUALSTACKFLAG="YES"; 
父主题： [DNS解析类APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除DNS解析类APN配置(DEL DNSAPNCHG) 
## 删除DNS解析类APN配置(DEL DNSAPNCHG) 
命令功能 
该命令用于删除DNS解析类APN的属性配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|表示DNS解析类APN的名称。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnAPN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置DNS解析类APN的名称为“zte.com.cn.mnc011.mcc460.gprs”
命令举例 
删除名称为zte.com.cn.mnc460.mcc001.gprs的DNS解析类APN配置信息。
DEL DNSAPNCHG:APN="zte.com.cn.mnc460.mcc001.gprs"; 
父主题： [DNS解析类APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询DNS解析类APN配置(SHOW DNSAPNCHG) 
## 查询DNS解析类APN配置(SHOW DNSAPNCHG) 
命令功能 
该命令用于查询DNS解析类APN的相关属性。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|表示DNS解析类APN的名称。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnAPN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置DNS解析类APN的名称为“zte.com.cn.mnc011.mcc460.gprs”
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|表示DNS解析类APN的名称。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnAPN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置DNS解析类APN的名称为“zte.com.cn.mnc011.mcc460.gprs”
CTPLID|计费模板标识|参数可选性:任选参数；参数类型:整数。|表示DNS解析类APN关联的计费模板标识，表示对接入此APN的用户，SGSN使用指定计费模板的计费策略对用户计费。该参数的取值是通过ADD APNCTPL命令配置的参数“TPLID”。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置SGSN对此类APN解析获取的GGSN是否支持DT功能。配置为“不支持”：表示GGSN不支持DT功能。配置为“支持”：表示GGSN支持DT功能。配置为“根据签约APN信息决策是否支持DT”：表示根据MS在HLR的的签约信息确定GGSN是否支持DT功能。在UMTS网络中，分别在RNC与SGSN、SGSN与GGSN之间建立GTP-U通道的（Indirect Tunnel）来处理用户面数据。如果启用了DT（Direct Tunnel，直连隧道）功能，则将RNC与SGSN、SGSN与GGSN之间用户面的两段隧道（Indirect Tunnel）优化为一段隧道，优化后用户面转发不经过SGSN，而直接在RNC和GGSN之间建立GTP-U隧道，通过节省用户面资源降低了保证运营商的资金投入和运营成本，同时也优化了UMTS网络用户面的性能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置SGSN对此类APN解析获取的GGSN是否支持双栈功能（MS是否可以用IPv4/IPv6/IPv4v6地址进行数据传输）。配置为“不支持”时，GGSN不支持双栈功能。配置为“支持”时，GGSN支持双栈功能。“默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK 在SGSN使用DNS对APN进行解析获取GGSN IP地址情况下，GGSN是否支持双栈功能，除了受ADD DNSAPNCHG命令的控制，还受到ADD DUAL STACK IP命令配置结果的控制。SGSN将解析出的GGSN IP地址与ADD DUAL STACK IP命令配置的GGSN IP地址列表进行比较，如果解析出的GGSN IP地址在ADD DUAL STACK IP命令配置的GGSN IP地址列表中，则表示此GGSN支持双栈功能。
SCDRFLT|过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置对接入此类APN的MS，SGSN是否生成S-CDR话单。配置为“是”时，SGSN不生成S-CDR话单。配置为“否”时，SGSN生成S-CDR话单。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
查询已配置的DNS解析类APN信息。
SHOW DNSAPNCHG; 
`
命令 (No.1): SHOW DNSAPNCHG;
操作维护         APN名称                         计费模板标识   支持DT功能                      支持终端双栈功能   过滤S-CDR
----------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   zte.com.cn.mnc460.mcc001.gprs   0              支持                            支持               否
----------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [DNS解析类APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 缺省计费特性配置 
# 缺省计费特性配置 
背景知识 
计费特性就是计费方法标识，运营商可以对不同用户或不同APN采用不同计费方法，比如普通计费、预付费、平率计费和热计费等。 
用户可以签约计费特性，若用户没有签约计费特性，则使用缺省计费特性，也就是指在SGSN配置的计费特性。 
计费模式分类： 
 
用户归属本SGSN，则为归属。
 
 
用户不归属本SGSN，PDP使用的是本SGSN所在运营商的GGSN，对此PDP而言则为拜访。
 
 
用户不归属本SGSN，PDP使用的是用户归属运营商的GGSN，对此PDP而言则为漫游。
 
 
不同计费模式的缺省计费特性可以不同。 
不同网号的缺省计费特性可以不同。 
只有S-CDR的计费模式才存在漫游和拜访。 
M-CDR和SMS-CDR则只能判断是否归属，当不是归属时，可以指定计费模式为拜访还是漫游。 
对于非归属本SGSN用户，当用户签约计费特性时，也可以根据配置确定是优先用签约的计费特性，还是SGSN配置的缺省计费特性，以便于对非归属用户的计费方法控制。 
功能描述 
存在不签约计费特性的用户或者需要控制非归属用户的计费特性时，进行本配置。 
SGSN产生话单时，SGSN先确定用户类型，根据用户类型获取配置的计费特性信息，以确定输出话单中的计费特性。 
相关主题 
 
设置缺省计费特性配置(SET CHGCHAR DEFAULT)
 
 
查询缺省计费特性配置(SHOW CHGCHAR DEFAULT)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置缺省计费特性配置(SET CHGCHAR DEFAULT) 
## 设置缺省计费特性配置(SET CHGCHAR DEFAULT) 
命令功能 
本命令用于根据用户类型来配置不同用户的缺省计费特性，用户分为三种类型： 
归属用户：用户归属本SGSN所属PLMN。 
拜访用户：用户不归属本SGSN所属PLMN，但使用本SGSN所在PLMN的GGSN激活PDP。 
漫游用户：用户不归属本SGSN所属PLMN，使用归属PLMN的GGSN激活PDP。 
对于以上三种用户，可以通过本命令，根据“计费特性“、”计费特性优先“和”非PDP优先“三个限制条件设置对应的计费特性。 
其中，对于归属用户，只受到“计费特性“的限制，不受”计费特性优先“和”非PDP优先“两个条件的限制，这两个计费条件仅对非归属用户（包括漫游用户和拜访用户）进行限制。 
对于非归属用户，SGSN首先根据用户的IMSI号码获取MCC和MNC，然后根据获取的MCC和MNC与通过[ADD CHGCHAR PLMN]命令配置的MCC和MNC进行比较：
如果匹配成功，则使用通过[SET CHGCHAR PLMN]命令配置的计费特性。
如果匹配失败，则使用本命令的”计费特性优先“和”非PDP优先“两个条件决定的计费特性。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MODE|计费选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|计费选择模式根据用户进行分类，包括以下三种：归属用户：用户归属本地PLMN。拜访用户：用户不归属本地PLMN，但使用本SGSN所在PLMN的GGSN激活PDP。漫游用户：用户不归属本地PLMN，使用用户归属PLMN的GGSN激活PDP。此参数设置为“归属缺省计费选择模式”：表示对归属用户配置计费特性。此参数设置为“拜访计费选择模式”：表示对拜访用户配置计费特性。此参数设置为“漫游计费选择模式”：表示对漫游用户配置计费特性。
CHAR|计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示用户的计费类型，仅当“计费选择模式”设置为“归属缺省计费选择模式”时有效，即该参数仅对归属用户进行限制，包括以下选项：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。SGSN根据自身的配置或HLR中签约的计费属性确定MS是否采用热计费，若采用热计费，在CDR中打上热计费标志，传给CG。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。
PRIO|计费特性优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数仅对非归属用户有限制。SGSN优先使用本地的计费特性还是优先使用HLR签约的计费特性对用户计费。配置为“本地计费特性优先（Default）“：表示SGSN采用本命令配置的计费特性对用户进行计费。配置为“签约计费特性优先（Subscription）“：表示SGSN根据用户的HLR签约信息进行处理，如果签约信息中包括计费特性，则使用签约的计费特性对用户进行计费，如果签约信息中没有计费特性，则使用本命令配置的计费特性对用户进行计费。
MPRIO|非PDP优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数仅对非归属用户（包括漫游用户和拜访用户）进行限制。此参数用于在M-CDR和SMS-CDR话单中标识非归属用户的计费类型是“漫游计费”还是“拜访计费”。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
设置缺省计费特性，计费选择模式为归属缺省计费选择模式，计费特性为热计费，计费特性优选缺省计费特性，移动性管理话单和短消息话单时优先为拜访计费。
SET CHGCHAR DEFAULT:MODE="Roaming",CHAR="Hot Billing",PRIO="Default",MPRIO="Visiting"; 
父主题： [缺省计费特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询缺省计费特性配置(SHOW CHGCHAR DEFAULT) 
## 查询缺省计费特性配置(SHOW CHGCHAR DEFAULT) 
命令功能 
该命令用于查询缺省计费特性配置。显示SGSN当前缺省计费特性配置 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MODE|计费选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|计费选择模式根据用户进行分类，包括以下三种：归属用户：用户归属本地PLMN。拜访用户：用户不归属本地PLMN，但使用本SGSN所在PLMN的GGSN激活PDP。漫游用户：用户不归属本地PLMN，使用用户归属PLMN的GGSN激活PDP。此参数设置为“归属缺省计费选择模式”：表示对归属用户配置计费特性。此参数设置为“拜访计费选择模式”：表示对拜访用户配置计费特性。此参数设置为“漫游计费选择模式”：表示对漫游用户配置计费特性。
CHAR|计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示用户的计费类型，仅当“计费选择模式”设置为“归属缺省计费选择模式”时有效，即该参数仅对归属用户进行限制，包括以下选项：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。SGSN根据自身的配置或HLR中签约的计费属性确定MS是否采用热计费，若采用热计费，在CDR中打上热计费标志，传给CG。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。
PRIO|计费特性优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数仅对非归属用户有限制。SGSN优先使用本地的计费特性还是优先使用HLR签约的计费特性对用户计费。配置为“本地计费特性优先（Default）“：表示SGSN采用本命令配置的计费特性对用户进行计费。配置为“签约计费特性优先（Subscription）“：表示SGSN根据用户的HLR签约信息进行处理，如果签约信息中包括计费特性，则使用签约的计费特性对用户进行计费，如果签约信息中没有计费特性，则使用本命令配置的计费特性对用户进行计费。
MPRIO|非PDP优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数仅对非归属用户（包括漫游用户和拜访用户）进行限制。此参数用于在M-CDR和SMS-CDR话单中标识非归属用户的计费类型是“漫游计费”还是“拜访计费”。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
查询缺省计费特性的配置信息。
SHOW CHGCHAR DEFAULT; 
`
命令 (No.1): SHOW CHGCHAR DEFAULT
操作维护  计费选择模式           计费特性   计费特性优先       非PDP优先
------------------------------------------------------------------------
修改      归属缺省计费选择模式   普通计费   签约计费特性优先   拜访计费
修改      漫游计费选择模式       热计费     本地计费特性优先   拜访计费
修改      拜访计费选择模式       普通计费   签约计费特性优先   拜访计费
------------------------------------------------------------------------
记录数 3
命令执行成功（耗时 0.022 秒）。
` 
父主题： [缺省计费特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 多网号用户计费特性配置 
# 多网号用户计费特性配置 
背景知识 
对漫游用户可以忽略用户签约的计费特性，而使用在SGSN中根据归属网号配置的计费特性；当漫游用户没有签约计费特性时，使用归属网号配置的计费特性，此时该计费特性又称为该网号的缺省计费特性。 
不同网号的计费特性可以不同，需要根据网号配置计费特性。 
功能描述 
当网络中存在多网号，且不同网号有不同的计费特性要求时，则需要为网号配置计费特性，配置信息包括网号、计费模式、计费特性和是否忽略HLR中签约计费特性。SGSN产生话单时，先确定用户类型，对非归属用户，根据计费模式和网号查询本配置的计费特性信息，以确定输出话单中的计费特性。 
                在本配置中没有配置的网号，则取“缺省计费特性配置”中配置的计费特性，参见
                [SET CHGCHAR DEFAULT]
                。
            
相关主题 
 
新增多网号用户计费特性配置(ADD CHGCHAR PLMN)
 
 
修改多网号用户计费特性配置(SET CHGCHAR PLMN)
 
 
删除多网号用户计费特性配置(DEL CHGCHAR PLMN)
 
 
查询多网号用户计费特性配置(SHOW CHGCHAR PLMN)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增多网号用户计费特性配置(ADD CHGCHAR PLMN) 
## 新增多网号用户计费特性配置(ADD CHGCHAR PLMN) 
命令功能 
本命令用于设置非归属用户（包括漫游用户和拜访用户）的计费特性。 
 
拜访用户：用户不归属本地PLMN，但使用本SGSN所在PLMN的GGSN激活PDP。
 
 
漫游用户：用户不归属本地PLMN，使用用户归属PLMN的GGSN激活PDP。
 
 
通过本命令，可以根据用户的IMSI号段对不同的用户类型配置不同的计费特性，方便运营商区分计费。 
注意事项 
SGSN首先根据非归属用户的IMSI号码匹配PLMN查询通过本命令配置的计费特性，如果获取不到匹配的记录，会根据[SET CHGCHAR DEFAULT]命令设置的缺省计费特性对非归属用户计费。
可通过“计费特性”、“计费特性优先”和“非PDP优先”三个限制条件设置对应的计费特性。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网）由MCC和MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。（参考协议3GPP PS 24.003）
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。参考协议3GPP 24.003）
命令举例 
新增多网号用户计费特性，其中国家移动码为460，移动网号是01。 
ADD CHGCHAR PLMN:PLMN="460"-"01"; 
父主题： [多网号用户计费特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改多网号用户计费特性配置(SET CHGCHAR PLMN) 
## 修改多网号用户计费特性配置(SET CHGCHAR PLMN) 
命令功能 
该命令用于修改多网号用户计费特性配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网）由MCC和MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。（参考协议3GPP PS 24.003）
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。参考协议3GPP 24.003）
MODE|计费选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN对非归属用户在生成S-CDR话单时，SGSN根据计费选择模式选择相应的计费特性，计费选择模式根据用户进行分类，包括以下两种类型：拜访用户：用户不归属本SGSN所属PLMN，但使用本SGSN所在PLMN的GGSN激活PDP。漫游用户：用户不归属本SGSN所属PLMN，使用用户归属PLMN的GGSN激活PDP。此参数设置为“拜访计费选择模式”：表示对拜访用户配置计费特性。此参数设置为“漫游计费选择模式”：表示对漫游用户配置计费特性。
CHAR|计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示用户的计费类型，仅对非归属用户进行限制，包括以下选项：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。SGSN根据自身的配置或HLR中签约的计费属性确定MS是否采用热计费，若采用热计费，在CDR中打上热计费标志，传给CG。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。
PRIO|计费特性优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数仅对非归属用户（包括漫游用户和拜访用户）进行限制。对非归属用户（包括漫游用户和拜访用户），SGSN优先使用本地的计费特性还是优先使用HLR签约的计费特性对用户计费。配置为“本地计费特性优先（Default）“：表示SGSN采用本命令配置的计费特性对用户进行计费。配置为“签约计费特性优先（Subscription）“：表示SGSN根据用户的HLR签约信息进行处理，如果签约信息中包括计费特性，则使用签约的计费特性对用户进行计费，如果签约信息中没有计费特性，则使用本命令配置的计费特性对用户进行计费。
MPRIO|非PDP优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数用于在M-CDR和SMS-CDR话单中进一步标识非归属用户使用“漫游计费”还是“拜访计费”。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
修改国家移动码为460、移动网号为01的多网号用户计费特性，计费选择模式修改为拜访计费选择模式，计费特性修改为热计费。 
SET CHGCHAR PLMN:PLMN="460"-"01",MODE="Visiting",CHAR="Hot Billing"; 
父主题： [多网号用户计费特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除多网号用户计费特性配置(DEL CHGCHAR PLMN) 
## 删除多网号用户计费特性配置(DEL CHGCHAR PLMN) 
命令功能 
该命令用于删除多网号用户计费特性配置。使用本命令删除网号标识。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网）由MCC和MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。（参考协议3GPP PS 24.003）
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。参考协议3GPP 24.003）
命令举例 
删除国家移动码为460、移动网号为01的多网号用户计费特性。 
DEL CHGCHAR PLMN:PLMN="460"-"01"; 
父主题： [多网号用户计费特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询多网号用户计费特性配置(SHOW CHGCHAR PLMN) 
## 查询多网号用户计费特性配置(SHOW CHGCHAR PLMN) 
命令功能 
该命令用于查询多网号用户计费特性配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:任选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网）由MCC和MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。（参考协议3GPP PS 24.003）
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。参考协议3GPP 24.003）
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:任选参数；参数类型:字符型。|PLMN（Public Land Mobile Network，公共陆地移动网）由MCC和MNC组成。
MODE|计费选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN对非归属用户在生成S-CDR话单时，SGSN根据计费选择模式选择相应的计费特性，计费选择模式根据用户进行分类，包括以下两种类型：拜访用户：用户不归属本SGSN所属PLMN，但使用本SGSN所在PLMN的GGSN激活PDP。漫游用户：用户不归属本SGSN所属PLMN，使用用户归属PLMN的GGSN激活PDP。此参数设置为“拜访计费选择模式”：表示对拜访用户配置计费特性。此参数设置为“漫游计费选择模式”：表示对漫游用户配置计费特性。
CHAR|计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示用户的计费类型，仅对非归属用户进行限制，包括以下选项：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。SGSN根据自身的配置或HLR中签约的计费属性确定MS是否采用热计费，若采用热计费，在CDR中打上热计费标志，传给CG。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。
PRIO|计费特性优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数仅对非归属用户（包括漫游用户和拜访用户）进行限制。对非归属用户（包括漫游用户和拜访用户），SGSN优先使用本地的计费特性还是优先使用HLR签约的计费特性对用户计费。配置为“本地计费特性优先（Default）“：表示SGSN采用本命令配置的计费特性对用户进行计费。配置为“签约计费特性优先（Subscription）“：表示SGSN根据用户的HLR签约信息进行处理，如果签约信息中包括计费特性，则使用签约的计费特性对用户进行计费，如果签约信息中没有计费特性，则使用本命令配置的计费特性对用户进行计费。
MPRIO|非PDP优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数用于在M-CDR和SMS-CDR话单中进一步标识非归属用户使用“漫游计费”还是“拜访计费”。3GPP协议规范详细定义了话单格式，SGSN支持以下CDR的生成：S-CDR（SGSN PDP context generated-CDR）：记录SGSN中用户使用的PDP上下文的信息和移动性管理相关的信息。M-CDR（Mobility Management generated-CDR）：用于记录移动台的移动性管理的信息。SMS-CDR（SGSN delivered short message mobile originated-CDR）：记录移动台短消息的信息。
命令举例 
查询已配置的多网号用户计费特性。 
SHOW CHGCHAR PLMN; 
`
命令 (No.1): SHOW CHGCHAR PLMN
操作维护  网号标识   计费选择模式       计费特性   计费特性优先       非PDP优先
-------------------------------------------------------------------------------
修改      460-01     漫游计费选择模式   热计费     本地计费特性优先   拜访计费
修改      460-01     拜访计费选择模式   热计费     签约计费特性优先   拜访计费
-------------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.032 秒）。
` 
父主题： [多网号用户计费特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# Ga接口配置 
# Ga接口配置 
背景知识 
Ga接口为SGSN/GGSN与计费网关CG之间的接口，用于传送CDR计费话单，采用GTP'协议，承载在UDP/IP协议上。SGSN可以为用户产生SMS-CDR（短信话单）、S-CDR（流量话单），生成话单后发送给CG网关，CG对话单进行合并整理后上报给计费中心。 
功能描述 
如SGSN支持Ga接口，需对本模块配置，配置步骤如下： 
 
设置Ga接口SGSN侧地址模式，可选择单地址或多地址模式，同时配置Ga接口SGSN侧的IP地址。单地址时，配置一个IP地址，各个处理单元采用相同IP地址。多地址时，为每个处理单元配置一个地址，各个处理单元采用不同IP地址。
 
 
设置Ga接口参数，如发送Echo Request的时间间隔、发送NodeAlive Request时间间隔、等待话单请求响应时长，话单请求消息重发次数等。
 
 
在CG服务器配置中，设置CG服务器的IP地址和端口号，设置此CG服务的IMSI范围，当CG Profile选择为负荷分担模式时使用此IMSI范围来选择CG。
 
 
配置CG Profile，以CG Profile ID作为标识，其中最大可包含两个CG服务器，两者关系可选择为主备或负荷分担。
 
 
为PLMN配置一个CG Profile ID，发送话单时SGSN基于用户所在的PLMN得到CG Profile ID。
 
 
相关主题 
 
本地Ga接口其他配置
 
 
CG服务器配置
 
 
CG Profile配置
 
 
CG PLMN配置
 
 
本端单地址配置
 
 
话单Node ID配置
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 本地Ga接口其他配置 
## 本地Ga接口其他配置 
背景知识 
在3GPP 32.295协议中定义了SGSN或CG使用NodeAlive Request/Respond来完成Ga接口的建立，SGSN和CG均可发起Ga接口建立。Ga接口建立后SGSN和CG使用Echo Request/Respond来监测Ga连接是否正常。 
SGSN需要发送话单时，向CG发送Data Record Transfer Request消息携带话单信息，CG以Data Record Transfer Respond消息响应指示SGSN话单发送成功或失败。 
功能描述 
本模块对Ga接口上各种管理参数进行配置，包括： 
 
发送NODEALIVE REQ时间间隔，如Ga接口建立失败，SGSN按照此时间间隔定时尝试建立Ga接口，直达Ga接口建立成功。
 
 
发送ECHO REQ时间间隔，Ga接口建立成功后，SGSN按照此时间间隔定时向CG发送Echo Request，等待CG返回的Echo Respond响应消息。如果连续多次等待Echo Respond响应超时，则认为Ga连接故障。
 
 
等待CG应答时间，此参数为SGSN向CG发送消息等待响应的时长，超过此时长则认为消息发送失败进行重发。
 
 
发送次数，此参数为SGSN向CG发送Data Record Transfer Request消息的最大重发次数，当SGSN发送Data Record Transfer Request消息等待响应超时后则进行重发，超过此最大发送次数SGSN认为Ga接口故障，不再发送。
 
 
定时保存话单时间间隔，SGSN按照此时间间隔，定时将缓存的话单文件保存到磁盘中。
 
 
发送CG话单时间间隔，SGSN收到Data Record Tranfer Respond消息携带CG Full原因，指示CG服务器处理过载时，停止向此CG发送话单，等待此配置时间间隔后，再尝试向此CG发送话单。
 
 
CG链路恢复前ECHO消息测试次数，SGSN判断Ga连接故障后，定时发送Data Record Transfer Request消息进行尝试，如收到成功响应后并不立刻判断为Ga连接恢复，而是发送多次Echo Request，如都能得到成功响应才认为Ga连接恢复，而发送Echo Request的次数即是由此参数配置。
 
 
相关主题 
 
设置本地Ga接口其他配置(SET LOCAL GAINFO)
 
 
查询本地Ga接口其他配置(SHOW LOCAL GAINFO)
 
 
父主题： [Ga接口配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置本地Ga接口其他配置(SET LOCAL GAINFO) 
### 设置本地Ga接口其他配置(SET LOCAL GAINFO) 
命令功能 
该命令用于设置本地Ga接口其他相关配置，包括：发送ECHO REQ时间间隔、发送NODEALIVE REQ时间间隔、等待CG应答时间、CG无应答消息发送次数、MP话单保存缓冲区的话单自动保存到硬盘文件的时间、检测到CG硬盘无空间后，SGSN尝试向该CG发送话单时间以及SGSN跟CG链路有断到通前ECHO消息测试次数。
注意事项 
如果SGSN跟CG之间的链路不稳定，比如网络延时等，"等待CG应答时间(秒)"和"CG无应答消息发送次数"可以相对设置大一些以减少消息重发。建议配置"等待CG应答时间(秒)"为6秒，"CG无应答消息发送次数"为6。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ECHOSNDTIME|发送ECHO REQ时间间隔(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:60~300。|该参数指定SGSN在与CG链路正常的情况下发送ECHO REQ时间间隔。一般使用默认值60秒，无需修改。
NODEALIVESNDTIME|发送NODEALIVE REQ时间间隔(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:30~300。|该参数指定SGSN发送NODEALIVE REQ时间间隔。一般使用默认值30秒，无需修改。
CGTIMEOUT|等待CG应答时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:3~10。|该参数指定SGSN发送请求消息后，等待等待CG应答的时间间隔，超过这个时间SGSN可能重发这个请求消息。如果CG的负荷过重，或者SGSN和CG链路不稳定，建议将该参数设置为6秒。
MSGRESNFCNT|发送次数|参数可选性:任选参数；参数类型:整数；参数范围为:3~10。|该参数指定SGSN发送请求消息后，如果没有收到CG的应答，重发该请求消息，当发送这个消息超过这个次数后，SGSN认为到CG的通讯链路中断。如果CG的负荷过重，或者SGSN和CG链路不稳定，建议将该参数设置为6次。
SAVECDRTIME|定时保存话单时间间隔(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~30。|该参数指定MP话单保存内存缓冲区的话单到硬盘中的自动保存时间，一般情况，这个缓冲区的话单超过30KB就会保存到文件，因此这个时间不必太小。一般使用默认值30分钟，无需修改。
CGFULLTIME|发送CG话单时间间隔(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~30。|该参数指定检测到CG硬盘无空间后，SGSN尝试向该CG发送话单时间。一般使用默认值10分钟，无需修改。
LINKRESTESTTIME|CG链路恢复前ECHO消息测试次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数指定SGSN跟CG链路由断到通前ECHO消息测试次数;一次ECHO消息可能不足以证明链路已经恢复，因此需要多测试几次。一般使用默认值3次，无需修改。
命令举例 
设置CG应答超时时长是8秒。 
SET LOCAL GAINFO:CGTIMEOUT=8; 
父主题： [本地Ga接口其他配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询本地Ga接口其他配置(SHOW LOCAL GAINFO) 
### 查询本地Ga接口其他配置(SHOW LOCAL GAINFO) 
命令功能 
该命令用于查询本地Ga接口其他相关配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ECHOSNDTIME|发送ECHO REQ时间间隔(秒)|参数可选性:任选参数；参数类型:整数。|该参数指定SGSN在与CG链路正常的情况下发送ECHO REQ时间间隔。一般使用默认值60秒，无需修改。
NODEALIVESNDTIME|发送NODEALIVE REQ时间间隔(秒)|参数可选性:任选参数；参数类型:整数。|该参数指定SGSN发送NODEALIVE REQ时间间隔。一般使用默认值30秒，无需修改。
CGTIMEOUT|等待CG应答时间(秒)|参数可选性:任选参数；参数类型:整数。|该参数指定SGSN发送请求消息后，等待等待CG应答的时间间隔，超过这个时间SGSN可能重发这个请求消息。如果CG的负荷过重，或者SGSN和CG链路不稳定，建议将该参数设置为6秒。
MSGRESNFCNT|发送次数|参数可选性:任选参数；参数类型:整数。|该参数指定SGSN发送请求消息后，如果没有收到CG的应答，重发该请求消息，当发送这个消息超过这个次数后，SGSN认为到CG的通讯链路中断。如果CG的负荷过重，或者SGSN和CG链路不稳定，建议将该参数设置为6次。
SAVECDRTIME|定时保存话单时间间隔(分钟)|参数可选性:任选参数；参数类型:整数。|该参数指定MP话单保存内存缓冲区的话单到硬盘中的自动保存时间，一般情况，这个缓冲区的话单超过30KB就会保存到文件，因此这个时间不必太小。一般使用默认值30分钟，无需修改。
CGFULLTIME|发送CG话单时间间隔(分钟)|参数可选性:任选参数；参数类型:整数。|该参数指定检测到CG硬盘无空间后，SGSN尝试向该CG发送话单时间。一般使用默认值10分钟，无需修改。
LINKRESTESTTIME|CG链路恢复前ECHO消息测试次数|参数可选性:任选参数；参数类型:整数。|该参数指定SGSN跟CG链路由断到通前ECHO消息测试次数;一次ECHO消息可能不足以证明链路已经恢复，因此需要多测试几次。一般使用默认值3次，无需修改。
命令举例 
查询本地Ga接口其他相关配置。 
SHOW LOCAL GAINFO; 
`
命令 (No.1): SHOW LOCAL GAINFO;
操作维护 发送ECHO REQ时间间隔(秒) 发送NODEALIVE REQ时间间隔(秒) 等待CG应答时间(秒) 发送次数 定时保存话单时间间隔(分钟) 发送CG话单时间间隔(分钟) CG链路恢复前ECHO消息测试次数 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改  60 30 3 3 30 30 3 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [本地Ga接口其他配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CG服务器配置 
## CG服务器配置 
背景知识 
CG服务器作为计费网关，使用Ga接口与SGSN网元连接，接收SGSN发送的用户话单信息，进行缓存、合并、整理后上报给计费中心。 
功能描述 
本模块配置CG服务器的IP地址和UDP端口号，SGSN建向此IP地址和UDP端口号发送NodeAlive Request消息，请求Ga接口建立。 
相关主题 
 
新增CG服务器配置(ADD CGCFG)
 
 
修改CG服务器配置(SET CGCFG)
 
 
删除CG服务器配置(DEL CGCFG)
 
 
查询CG服务器配置(SHOW CGCFG)
 
 
父主题： [Ga接口配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增CG服务器配置(ADD CGCFG) 
### 新增CG服务器配置(ADD CGCFG) 
命令功能 
该命令用于新增一个CG服务器。当系统需要新增一个计费服务器来接收话单时，使用本命令。
注意事项 
 
新增的CG必须被CG Profile关联才可以使用，配置命令参见ADD CGPROFILE或者SET CGPROFILE。
 
 
新增CG服务器的个数不能大于License中最大CG容量取值，最大CG容量默认取值为2。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CG服务器的标识，每个CG服务器都有一个唯一的编号。
CGADDR|CG侧地址|参数可选性:必选参数；参数类型:地址|CG服务器地址，可以配置为IPV4的地址也可以配置IPV6的地址。CG侧和本端使用相同的IP地址类型，查询命令参见SHOW SINGLE ADDR或者SHOW MULTI ADDR。
CGPORT|CG起始端口号|参数可选性:必选参数；参数类型:整数；参数范围为:0~65534。|CG服务器端口号，和CG侧地址一起跟SGSN进行通讯，通常可以使用知名端口号3386，详细描述参见3GPP TS 32295中的Port usage章节。
PORTNUM|端口数量|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。默认值:1。|该参数用于设置CG端口的数量。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|CG服务器的名称。
命令举例 
新增了一个CG服务器。CG服务器标识为2。CG的地址为20.10.1.200，CG侧端口为3000，CG的名称为CG2。 
ADD CGCFG:ID=2,CGADDR="20.10.1.200",CGPORT=3000,PORTNUM=1,NAME="CG2"; 
父主题： [CG服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改CG服务器配置(SET CGCFG) 
### 修改CG服务器配置(SET CGCFG) 
命令功能 
该命令用于修改CG服务器属性，包括对CG侧地址和端口号、用户别名的修改。
注意事项 
新增的CG必须被CGPROFILE关联才可以使用，配置命令参见[ADD CGPROFILE]或者[SET CGPROFILE]。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CG服务器的标识，每个CG服务器都有一个唯一的编号。
CGADDR|CG侧地址|参数可选性:任选参数；参数类型:地址|CG服务器地址，可以配置为IPV4的地址也可以配置IPV6的地址。CG侧和本端使用相同的IP地址类型，查询命令参见SHOW SINGLE ADDR或者SHOW MULTI ADDR。
CGPORT|CG起始端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65534。|CG服务器端口号，和CG侧地址一起跟SGSN进行通讯，通常可以使用知名端口号3386，详细描述参见3GPP TS 32295中的Port usage章节。
PORTNUM|端口数量|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|该参数用于设置CG端口的数量。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|CG服务器的名称。
命令举例 
将CG服务器ID为2的CG服务器对应的地址修改为20.10.1.190，端口改为5000，用户别名改为CG2。 
SET CGCFG:ID=2,CGADDR="20.10.1.190",CGPORT=5000,PORTNUM=1,NAME="CG2"; 
父主题： [CG服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除CG服务器配置(DEL CGCFG) 
### 删除CG服务器配置(DEL CGCFG) 
命令功能 
该命令用于删除一个CG服务器。
注意事项 
被删除CG服务器不能被任何CG Profile关联。 
首先查询CG服务器是否被CG Prolfile关联，命令参见[SHOW CGPROFILE]。
若该CG服务器与CG Prolfile关联，应先删除相应的关联，命令参见[SET CGPROFILE]，再删除该CG服务器。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CG服务器的标识，每个CG服务器都有一个唯一的编号。
命令举例 
删除CG服务器ID为2的CG服务器配置。 
DEL CGCFG:ID=2; 
父主题： [CG服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CG服务器配置(SHOW CGCFG) 
### 查询CG服务器配置(SHOW CGCFG) 
命令功能 
该命令用于查询CG服务器配置。
注意事项 
如果不指定任何ID，将显示本局配置的所有CG服务器。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|CG服务器ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|CG服务器的标识，每个CG服务器都有一个唯一的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|CG服务器ID|参数可选性:任选参数；参数类型:整数。|CG服务器的标识，每个CG服务器都有一个唯一的编号。
CGADDR|CG侧地址|参数可选性:任选参数；参数类型:地址|CG服务器地址，可以配置为IPV4的地址也可以配置IPV6的地址。CG侧和本端使用相同的IP地址类型，查询命令参见SHOW SINGLE ADDR或者SHOW MULTI ADDR。
CGPORT|CG起始端口号|参数可选性:任选参数；参数类型:整数。|CG服务器端口号，和CG侧地址一起跟SGSN进行通讯，通常可以使用知名端口号3386，详细描述参见3GPP TS 32295中的Port usage章节。
PORTNUM|端口数量|参数可选性:任选参数；参数类型:整数。|该参数用于设置CG端口的数量。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|CG服务器的名称。
命令举例 
查询CG服务器的配置。 
SHOW CGCFG; 
`
命令 (No.1): SHOW CGCFG
操作维护         CG服务器ID   CG侧地址      CG起始端口号   端口数量     用户别名
----------------------------------------------------------------------------
复制 修改 删除   1                          0           1 
复制 修改 删除   2            20.10.1.190   5000        1            CG2
----------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.022 秒）。
` 
父主题： [CG服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CG Profile配置 
## CG Profile配置 
背景知识 
为了提高Ga接口的容灾能力，3GPP 32.295协议中定义Ga接口支持主备CG。主用CG故障时，备用CG代替原主用CG，接收SGSN发送的话单，整理合并后上报给计费中心。 
ZXUN uMAC SGSN Ga接口最大支持连接32个具有不同优先级或者权重的CG服务器。SGSN发送话单时，优先选择级别高的CG，如果SGSN配置了多个同一优先级的CG，则基于CG的权重进行负荷分担。 
功能描述 
CG Profile是一组CG服务器的集合，以CG Profile ID为标识，一个CG Profile中最少包括一个，最多包括32个CG服务器，这32个CG服务器具有不同的优先级或者权重。 
                SGSN上可以配置多个CG Profile ID。SGSN发送话单时，首先根据用户PLMN在“CG PLMN配置”(参见命令
                [ADD CGPLMN]
                )中得到CG Profile ID，使用此ID在“CG Profile 配置”中查找CG服务器，优先选择级别高的CG服务器，在同一优先级时基于CG的权重选择CG服务器。如用户PLMN未配置对应一个CG Profile，SGSN选择默认属性的CG Profile。在“CG Profile配置”中，ID为0的CG Profile是默认属性，此记录自动生成，不可删除。
            
相关主题 
 
新增CG Profile配置(ADD CGPROFILE)
 
 
修改CG Profile配置(SET CGPROFILE)
 
 
增加CG Profile中的服务器(ADD CGSERVER)
 
 
修改CG Profile中的服务器(SET CGSERVER)
 
 
删除CG Profile配置(DEL CGPROFILE)
 
 
查询CG Profile配置(SHOW CGPROFILE)
 
 
父主题： [Ga接口配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增CG Profile配置(ADD CGPROFILE) 
### 新增CG Profile配置(ADD CGPROFILE) 
命令功能 
该命令用于新增一个CG Profile，一次可以将多个CG服务器关联到一个CG Profile中。使用该命令新增CG Profile成功后，SGSN才可以和该CG进行通信。 
CG Profile就是计费网关（CG服务器）的工作组。 
新增CG Profile前，需要先创建CG服务器。 
注意事项 
 
系统中有且只能配置一条通用类型的CG Profile，供没有配置CG PLMN的PLMN使用，命令参见ADD CGPLMN。
 
 
每个CG Profile必须至少配置一个CG服务器。CG服务器的配置命令参见ADD CGCFG。
 
 
一个CG只能被一个CG Profile关联。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|CG Profile ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~7。|该参数是CG Profile的标示号，取值需全局唯一。
CGSERVER|CG服务器|参数可选性:必选参数；参数类型:复合参数|该参数是以下三个参数的组合：CG服务器ID、优先级、权重。用于指定CG Profle中一个CG服务器的标识、优先级和权重。至少配置一个CG服务器，最多32个，每个CG服务器必须配置对应的优先级和权重。
CGINDEX|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
PRIORITY|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~5。|该参数用于指定CG服务器的优先级。优先级取值范围为1-5，数值越低级别越高。
WEIGHT|权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指定CG服务器的权重，取值范围1-1000。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|CG PROFILE 的名称。
命令举例 
新增CG Profile，标识为1，CG服务器ID为2，CG服务器的优先级为3，CG服务器的权重为50，名称为Profile1。 
ADD CGPROFILE:PROFILEID=1,CGSERVER=2-3-50,NAME="Profile1"; 
父主题： [CG Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改CG Profile配置(SET CGPROFILE) 
### 修改CG Profile配置(SET CGPROFILE) 
命令功能 
该命令用于建立CG Profile和CG服务器的关联，设置CG服务器的优先级和权重。
注意事项 
 
每个CG Profile必须至少配置一个CG服务器。CG服务器的配置命令参见ADD CGCFG;
 
 
一个CG只能被一个CG Profile关联。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|CG Profile ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~7。|该参数是CG Profile的标示号，取值需全局唯一。
CGSERVER|CG服务器|参数可选性:任选参数；参数类型:复合参数|该参数是以下三个参数的组合：CG服务器ID、优先级、权重。用于指定CG Profle中一个CG服务器的标识、优先级和权重。至少配置一个CG服务器，最多32个，每个CG服务器必须配置对应的优先级和权重。
CGINDEX|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
PRIORITY|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~5。|该参数用于指定CG服务器的优先级。优先级取值范围为1-5，数值越低级别越高。
WEIGHT|权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指定CG服务器的权重，取值范围1-1000。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|CG PROFILE 的名称。
命令举例 
修改标识为1的CG Profile中的CG服务器2，优先级改为5，权重改为100。 
SET CGPROFILE:PROFILEID=1,CGSERVER=2-5-100,NAME="Profile1"; 
父主题： [CG Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 增加CG Profile中的服务器(ADD CGSERVER) 
### 增加CG Profile中的服务器(ADD CGSERVER) 
命令功能 
该命令用于设置CG服务器归属到CG Profile中，以及设置CG服务器在CG Profile中的优先级和权重。
注意事项 
一个CG服务器只能归属到一个CG Profile，一个CG Profile可以包含多个CG服务器。增加CG服务器的命令，参见[ADD CGCFG]。
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|CG Profile ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~7。|该参数是CG Profile的标识号，取值需全局唯一。
CGINDEX|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
PRIORITY|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~5。|该参数用于指定CG服务器的优先级。优先级取值范围为1-5，数值越低级别越高。
WEIGHT|权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指定CG服务器的权重，取值范围1-1000。
命令举例 
增加CG Profile中的CG Server配置，Profile标识为0，CG服务器标识为2，CG服务器优先级为5，CG服务器权重为100。 
ADD CGSERVER:PROFILEID=0,CGINDEX=2,PRIORITY=5,WEIGHT=100; 
父主题： [CG Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改CG Profile中的服务器(SET CGSERVER) 
### 修改CG Profile中的服务器(SET CGSERVER) 
命令功能 
该命令用于修改CG Profile中CG服务器的优先级和权重。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CGINDEX|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
PRIORITY|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数用于指定CG服务器的优先级。优先级取值范围为1-5，数值越低级别越高。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指定CG服务器的权重，取值范围1-1000。
命令举例 
修改标识为2的CG服务器配置，优先级改为4，权重改为90。 
SET CGSERVER:CGINDEX=2,PRIORITY=4,WEIGHT=90; 
父主题： [CG Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除CG Profile配置(DEL CGPROFILE) 
### 删除CG Profile配置(DEL CGPROFILE) 
命令功能 
该命令用于删除一个CG Profile或者删除CG 服务器与它所在CG Profile的关联。
注意事项 
 
删除CG Profile前，确保该CG Profile不被CGPLMN关联，查询命令参见SHOW CGPLMN。
 
 
删除CG Profile时，CG Profile标识符参数和CG服务器标识符参数是互斥的，只能填写一个。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|CG Profile ID|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~7。|该参数是CG Profile的标示号，取值需全局唯一。
CGINDEX|CG服务器ID|参数可选性:必须单选参数；参数类型:整数；参数范围为:1~32。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
命令举例 
删除标识为1的CG Profile。 
DEL CGPROFILE:PROFILEID=1; 
父主题： [CG Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CG Profile配置(SHOW CGPROFILE) 
### 查询CG Profile配置(SHOW CGPROFILE) 
命令功能 
该命令用于查询CG Profile配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|CG Profile ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~7。|该参数是CG Profile的标示号，取值需全局唯一。
CGINDEX|CG服务器ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PROFILEID|CG Profile ID|参数可选性:任选参数；参数类型:整数。|该参数是CG Profile的标示号，取值需全局唯一。
PROPERTY|属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否为通用的CG Profile。该参数不需要指定，系统默认ID为零的CG Profile 就是通用的CG Profile。通用的CG Profile 只能有一个。当没有给PLMN话单指定CG Profile时，使用通用的CG Profile。查询命令参见SHOW CGPLMN。
CGINDEX|CG服务器ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定CG Profile关联的CG服务器的标识。CG服务器ID查询命令参见 SHOW CGCFG。
PRIORITY|优先级|参数可选性:任选参数；参数类型:整数。|该参数用于指定CG服务器的优先级。优先级取值范围为1-5，数值越低级别越高。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数。|该参数用于指定CG服务器的权重，取值范围1-1000。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|CG PROFILE 的名称。
命令举例 
查询已配置的CG Profile。 
SHOW CGPROFILE; 
`
命令 (No.1): SHOW CGPROFILE
操作维护         CG Profile ID   属性     CG服务器ID   优先级   权重    用户别名
--------------------------------------------------------------------------------
复制 修改 删除   0               通用     1            1        1000    
复制 修改 删除   1               不通用   2            4        100     Profile2
--------------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.022 秒）。
` 
父主题： [CG Profile配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CG PLMN配置 
## CG PLMN配置 
背景知识 
在现网中，存在多个运营商可以共用同一SGSN网元，但CG网关却各自独立的组网模式。此时SGSN在发送话单时，需基于用户的PLMN，将其话单发送到归属的CG网关。 
功能描述 
本模块为PLMN指定一个CG Profile ID，SGSN为发送话单时，使用用户的PLMN查找本模块配置数据得到CG Profile ID，通过CG Profile ID在“CG Profile配置”中可查找到一个CG服务器，向其发送话单请求消息。 
相关主题 
 
新增CG PLMN配置(ADD CGPLMN)
 
 
修改CG PLMN配置(SET CGPLMN)
 
 
删除CG PLMN配置(DEL CGPLMN)
 
 
查询CG PLMN配置(SHOW CGPLMN)
 
 
父主题： [Ga接口配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增CG PLMN配置(ADD CGPLMN) 
### 新增CG PLMN配置(ADD CGPLMN) 
命令功能 
该命令用于新增一个CG PLMN配置。当需要为PLMN配置CG Profile ID来选择CG服务器时，使用该命令。成功后，对应PLMN产生的话单将发送到CG Profile ID对应的计费服务器上。 
PLMN网元标识由MCC+MNC共同确定。 
注意事项 
 
CG PLMN配置是为PLMN指定使用一个CG Profile，其优先级高于通用CG Profile。
 
 
当未执行ADD CGPLMN命令为PLMN指定CG Profile ID时，使用通用CG Profile，通用CG Profile的配置命令参见ADD CGPROFILE，将其中的CG Profile ID值设置为"0"即可。
 
 
如果CG PLMN与通用CG Profile都没有配置，则无法找到话单发送的CG。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:必选参数；参数类型:复合参数|公共陆地移动网络PLMN由MCC+MNC共同确定。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MCC，该参数用于设定PLMN中移动国家码。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MNC，该参数用于设定PLMN中移动网络号。
PROFILEID|CG Profile ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~7。|该参数用于获取CG Profile的标识号，其查询命令参见SHOW CGPROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|CG PLMN的名称。
命令举例 
新增CG PLMN配置，移动国家码为460，移动网号是01，对应的CG Profile标识为0，用户别名是plmn_1。 
ADD CGPLMN:PLMN="460"-"01",PROFILEID=0,NAME="plmn_1"; 
父主题： [CG PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改CG PLMN配置(SET CGPLMN) 
### 修改CG PLMN配置(SET CGPLMN) 
命令功能 
该命令用于修改CG PLMN配置。可修改指定PLMN的CG Profile ID。修改后，该PLMN产生的话单将发送到新配置的CG Profile ID对应的计费服务器上。
注意事项 
 
CG PLMN配置是为PLMN指定使用一个CG Profile，其优先级高于通用CG Profile。
 
 
当未执行ADD CGPLMN命令为PLMN指定CG Profile ID时，使用通用CG Profile，通用CG Profile的配置命令参见ADD CGPROFILE，将其中的CG Profile ID值设置为"0"即可。
 
 
如果CG PLMN与通用CG Profile都没有配置，则无法找到话单发送的CG。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:必选参数；参数类型:复合参数|公共陆地移动网络PLMN由MCC+MNC共同确定。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MCC，该参数用于设定PLMN中移动国家码。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MNC，该参数用于设定PLMN中移动网络号。
PROFILEID|CG Profile ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~7。|该参数用于获取CG Profile的标识号，其查询命令参见SHOW CGPROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|CG PLMN的名称。
命令举例 
修改移动国家码为460，移动网号是01对应的CG PLMN，将CG Profile标识修改为1。 
SET CGPLMN:PLMN="460"-"01",PROFILEID=1; 
父主题： [CG PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除CG PLMN配置(DEL CGPLMN) 
### 删除CG PLMN配置(DEL CGPLMN) 
命令功能 
该命令用于删除一个CG PLMN配置。删除后，解除PLMN与CG Profile的关联关系，该PLMN采用通用CG Profile进行计费业务处理 。
注意事项 
直接删除由MCC+MNC共同确定的PLMN标识，就解除了PLMN与CG Profile ID的关联关系。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:必选参数；参数类型:复合参数|公共陆地移动网络PLMN由MCC+MNC共同确定。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MCC，该参数用于设定PLMN中移动国家码。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MNC，该参数用于设定PLMN中移动网络号。
命令举例 
删除移动国家码为460，移动网号是01对应的CG PLMN配置。 
DEL CGPLMN:PLMN="460"-"01"; 
父主题： [CG PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CG PLMN配置(SHOW CGPLMN) 
### 查询CG PLMN配置(SHOW CGPLMN) 
命令功能 
该命令用于查询一个CG PLMN配置。
注意事项 
无.
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:任选参数；参数类型:复合参数|公共陆地移动网络PLMN由MCC+MNC共同确定。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MCC，该参数用于设定PLMN中移动国家码。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|PLMN由MCC+MNC共同确定，移动终端IMSI号码中包含MNC，该参数用于设定PLMN中移动网络号。
PROFILEID|CG Profile ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~7。|该参数用于获取CG Profile的标识号，其查询命令参见SHOW CGPROFILE。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|网号标识|参数可选性:任选参数；参数类型:字符型。|公共陆地移动网络PLMN由MCC+MNC共同确定。
PROFILEID|CG Profile ID|参数可选性:任选参数；参数类型:整数。|该参数用于获取CG Profile的标识号，其查询命令参见SHOW CGPROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|CG PLMN的名称。
命令举例 
查询已配置的CG PLMN信息。 
SHOW CGPLMN; 
`
命令 (No.1): SHOW CGPLMN
操作维护    网号标识   CG Profile ID   用户别名
----------------------------------------------
复制 修改   460-01     0               plmn_1
----------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [CG PLMN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 本端单地址配置 
## 本端单地址配置 
背景知识 
SGSN网元与CG之间使用Ga接口连接，采用UDP协议，协议为Ga接口定义的UDP端口号为3868。 
为提高处理能力，SGSN中每个处理单元与CG之间建立一个Ga连接。当从CG接收到消息，为确定其属于哪个处理单元，使用SGSN的IP地址+UDP端口来区分。当按照协议规定只能使用UDP端口3868，则只能为每个处理单元配置一个IP地址，整个SGSN需要配置多个IP地址，中兴SGSN提供了另外一种方式，则是SGSN采用一个地址，但UDP端口不再固定为3868，而是每个处理单元不同UDP端口。 
功能描述 
当SGSN在“Ga接口基本配置”选择为单地址模式，需对本模块配置。 
在本模块中可为SGSN配置一个IPv4或IPv6地址，各个处理单元均使用此地址，用于和CG网元建立Ga连接。在网络IP地址资源有限的情况下，可选择单地址模式减少IP地址的占用。 
相关主题 
 
设置本端单地址配置(SET SINGLE ADDR)
 
 
查询本端单地址配置(SHOW SINGLE ADDR)
 
 
父主题： [Ga接口配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置本端单地址配置(SET SINGLE ADDR) 
### 设置本端单地址配置(SET SINGLE ADDR) 
命令功能 
该命令用于设置本端单地址配置。当选择通信地址模式为单地址时，使用该命令配置Ga接口IP地址、VRF ID参数。 
每个话单转发模块使用一个独立的Ga接口，区分不同Ga接口的标识为：IP地址+端口号。单地址即为用同一个地址对应多个端口来区分各个模块。
 
本端的端口号为(35000+模块号)，其中35000为协议定义的固定值，端口号在网元实现内部动态获取与指定，无需在OMM中配置。 
注意事项 
 
缺省地址模式设置为0，即为单地址模式，其配置命令参见SET GACFG。
 
 
单地址模式对应的本端地址可以和其它用户本端IP地址冲突，不同于多地址模式。
 
 
单地址模式对应的本端地址不能设置为空，但VRF可以设置为空，VRF的配置命令参见。
 
 
本端地址对应的远端服务器地址为计费服务器CG侧地址与服务端口，CG服务器配置命令参见ADD CGCFG。
 
 
使用单地址模式，可以同时设置一个IPv4地址与一个IPv6地址。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
LOCALADDR|本端IPv4地址|参数可选性:任选参数；参数类型:地址|本端对应的IPv4格式的地址，其查询命令参见SHOW IPSTACK ALL。
LOCALV6ADDR|本端IPv6地址|参数可选性:任选参数；参数类型:地址|本端对应的IPv6格式的地址，其查询命令参见SHOW IPSTACK ALL。
VRF|VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|当需要让某接口的信令/数据在不同的虚拟路由域内传输时设置VRF标识，其查询命令参见SHOW VRFCFG。
命令举例 
设置本端IPv4地址为192.168.0.1，VRF标识为0。 
SET SINGLE ADDR:LOCALADDR="192.168.0.1",VRF=0; 
父主题： [本端单地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询本端单地址配置(SHOW SINGLE ADDR) 
### 查询本端单地址配置(SHOW SINGLE ADDR) 
命令功能 
该命令用于查询本端单地址配置。 
注意事项 
无.
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LOCALADDR|本端IPv4地址|参数可选性:任选参数；参数类型:地址|本端对应的IPv4格式的地址，其查询命令参见SHOW IPSTACK ALL。
LOCALV6ADDR|本端IPv6地址|参数可选性:任选参数；参数类型:地址|本端对应的IPv6格式的地址，其查询命令参见SHOW IPSTACK ALL。
VRF|VRF标识|参数可选性:任选参数；参数类型:整数。|当需要让某接口的信令/数据在不同的虚拟路由域内传输时设置VRF标识，其查询命令参见SHOW VRFCFG。
命令举例 
查询本端单地址配置。 
SHOW SINGLE ADDR; 
`
命令 (No.1): SHOW SINGLE ADDR
操作维护  本端IPv4地址   本端IPv6地址   VRF标识
-----------------------------------------------
修改      192.168.0.1                   0
-----------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [本端单地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 话单Node ID配置 
## 话单Node ID配置 
背景知识 
在3GPP 32.215协议中定义了CDR格式，其中CDR话单中包含格式为字符型的Node ID字段，CG网元使用此字段来识别当前话单由哪个网元上报。 
功能描述 
本模块配置本SGSN的Node ID，SGSN发出的话单CDR中包含此Node ID。组网时，需为网络中SGSN和MSC/VLR网元规划好Node ID，以便CG或计费中心通过此Node ID即可知道当前话单由哪个网元上报。 
相关主题 
 
设置话单的Node ID(SET CDR NODEID)
 
 
重置话单的Node ID为空(RESET CDR NODEID)
 
 
查询话单的Node ID(SHOW CDR NODEID)
 
 
父主题： [Ga接口配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置话单的Node ID(SET CDR NODEID) 
### 设置话单的Node ID(SET CDR NODEID) 
命令功能 
该命令用于设置话单的Node ID。当现网CDR格式需支持Node ID字段时，使用该命令进行配置。Node ID主要用于标识一个DNS主机名。 
在CDR话单编码时根据配置的Node ID进行话单的ASN.1编码，如果没有使用该命令配置Node ID，则在SGSN网元内部进行编解码的时候不处理该Node ID字段。 
注意事项 
Node ID的有效长度为20个字节，超过20个字节的Node ID 字符串，系统将做截断处理为最大20个字节。
参数说明 
标识|名称|类型|说明
---|---|---|---
NODEID|话单Node ID|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|SGSN对携带Node ID字段的话单进行编解码处理。Node ID的有效长度为20个字节，以“\0”字符结尾。超过20个字节的Node ID 字符串，系统将做截断处理为最大20个字节。该参数默认值为空，其查询命令参见SHOW CDR NODEID。
命令举例 
设置话单的Node ID为1111。 
SET CDR NODEID:NODEID="1111"; 
父主题： [话单Node ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 重置话单的Node ID为空(RESET CDR NODEID) 
### 重置话单的Node ID为空(RESET CDR NODEID) 
命令功能 
该命令用于重置话单的Node ID为空。当运营商不需要SGSN网元对话单中的Node ID参数进行判断与处理时，使用该命令清除话单的Node ID参数。
注意事项 
该命令执行后Node ID将被设置为空，执行前请确认后再执行。
命令举例 
重置话单的Node ID为空。 
RESET CDR NODEID; 
父主题： [话单Node ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询话单的Node ID(SHOW CDR NODEID) 
### 查询话单的Node ID(SHOW CDR NODEID) 
命令功能 
该命令用于查询话单的Node ID。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NODEID|话单Node ID|参数可选性:任选参数；参数类型:字符型。|SGSN对携带Node ID字段的话单进行编解码处理。Node ID的有效长度为20个字节，以“\0”字符结尾。超过20个字节的Node ID 字符串，系统将做截断处理为最大20个字节。该参数默认值为空，其查询命令参见SHOW CDR NODEID。
命令举例 
查询话单的Node ID。 
SHOW CDR NODEID;  
`
命令 (No.1): SHOW CDR NODEID
操作维护  话单Node ID
---------------------
修改      1111
---------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [话单Node ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# IMSI号段过滤CDR配置 
# IMSI号段过滤CDR配置 
背景知识 
SGSN话单分为会话管理话单S-CDR、移动性管理话单M-CDR、短消息MO话单SMS-SMO-CDR和短消息MT话单SMS-SMT-CDR。默认SGSN输出上述所有话单，但通常运营商只需要上述话单中的一部分用于计费，对于不用于计费的话单则要求能通过配置进行屏蔽。 
话单屏蔽都是根据运营商和地域进行的，通常IMSI分配就是根据地域和运营商进行的，从而根据IMSI就能够判断出用户所在运营商和地域，所以根据IMSI号段就可以实现根据运营商和地域进行话单过滤。 
如运营商计费策略是本地用户从GGSN上获取话单，漫游用户从SGSN获取话单，则要求本地用户在SGSN不输出话单，漫游用户在SGSN输出话单，则通过在SGSN上配置屏蔽本地用户话单，不屏蔽漫游用户话单就可以实现上述需求。 
功能描述 
当运营商不需要SGSN出某种话单时，则配置过滤对应的IMSI号段对应的话单。 
注意事项：本配置中IMSI号段务必配置准确，如果IMSI号段配置错误，则要求出话单的号段不会有对应话单，可能造成该号段无法计费，影响非常大，请慎重配置。 
相关主题 
 
新增IMSI号段过滤CDR配置(ADD IMSI CDR FILTER)
 
 
修改IMSI号段过滤CDR配置(SET IMSI CDR FILTER)
 
 
删除IMSI号段过滤CDR配置(DEL IMSI CDR FILTER)
 
 
查询IMSI号段过滤CDR配置(SHOW IMSI CDR FILTER)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增IMSI号段过滤CDR配置(ADD IMSI CDR FILTER) 
## 新增IMSI号段过滤CDR配置(ADD IMSI CDR FILTER) 
命令功能 
该命令用于增加IMSI号段过滤对应CDR配置。当用户的计费信息可以从本网的GGSN获取，而SGSN仅需要输出会话管理话单S-CDR，或SGSN对部分用户不需要输出会话管理话单S-CDR时（如本地用户），使用该命令。该命令可以控制此IMSI号码各类型话单部分或全部过滤，如只过滤S-CDR或过滤S-CDR和M-CDR或过滤全部。增加IMSI号段过滤CDR配置成功后，SGSN按照配置过滤对应类型话单，不再输出该IMSI号段用户对应话单。 
注意事项 
一旦配置为不输出对应话单，则会对此IMSI号段的计费造成影响，请慎重配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|表示对该IMSI号段用户的话单，按照配置过滤规则进行过滤。
FILTER|是否过滤话单|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数为需要过滤的SGSN用户话单类型。取值含义如下：“MCDRFLT”：过滤M-CDR话单。“SMOCDRFLT”：过滤SMS-SMO-CDR话单。“SMTCDRFLT”：过滤SMS-SMT-CDR话单。“SCDRFLT”：过滤S-CDR话单。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数对话单过滤规则记录指定名称。
命令举例 
增加IMIS号段过滤CDR配置。增加的IMSI号段为445555，对应的过滤话单类型为MCDR和SMOCDR和SMTCDR类型。 
ADD IMSI CDR FILTER:IMSI="445555",FILTER="MCDRFLT"&"SMOCDRFLT"&"SMTCDRFLT"; 
父主题： [IMSI号段过滤CDR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改IMSI号段过滤CDR配置(SET IMSI CDR FILTER) 
## 修改IMSI号段过滤CDR配置(SET IMSI CDR FILTER) 
命令功能 
该命令用于修改IMSI号段过滤CDR配置。当增加的IMSI号段过滤CDR配置不满足运营商要求时使用此命令，如多过滤该IMSI号段应该输出的话单，或少过滤该IMSI段不应该输出的话单，则通过此命令添加或减少该IMS号段对应的话单，以达到用户需求。 
注意事项 
一旦配置为不输出对应话单，则会对此IMSI号段的计费造成影响，需要慎重配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|表示对该IMSI号段用户的话单，按照配置过滤规则进行过滤。
FILTER|是否过滤话单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为需要过滤的SGSN用户话单类型。取值含义如下：“MCDRFLT”：过滤M-CDR话单。“SMOCDRFLT”：过滤SMS-SMO-CDR话单。“SMTCDRFLT”：过滤SMS-SMT-CDR话单。“SCDRFLT”：过滤S-CDR话单。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数对话单过滤规则记录指定名称。
命令举例 
修改IMIS号段过滤CDR配置。修改的IMSI号段为445555，修改后的过滤话单类型为MCDR和SMOCDR类型。 
SET IMSI CDR FILTER:IMSI="445555",FILTER="MCDRFLT"&"SMOCDRFLT"; 
父主题： [IMSI号段过滤CDR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除IMSI号段过滤CDR配置(DEL IMSI CDR FILTER) 
## 删除IMSI号段过滤CDR配置(DEL IMSI CDR FILTER) 
命令功能 
该命令用于删除IMSI号段过滤CDR配置。删除后，不对该IMSI号段话单进行过滤，该IMSI号段所有话单SGSN正常输出。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|表示对该IMSI号段用户的话单，按照配置过滤规则进行过滤。
命令举例 
删除IMIS号段为445555的过滤话单配置。 
DEL IMSI CDR FILTER:IMSI="445555"; 
父主题： [IMSI号段过滤CDR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询IMSI号段过滤CDR配置(SHOW IMSI CDR FILTER) 
## 查询IMSI号段过滤CDR配置(SHOW IMSI CDR FILTER) 
命令功能 
该命令用于查询IMSI号段过滤CDR配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|表示对该IMSI号段用户的话单，按照配置过滤规则进行过滤。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|表示对该IMSI号段用户的话单，按照配置过滤规则进行过滤。
FILTER|是否过滤话单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为需要过滤的SGSN用户话单类型。取值含义如下：“MCDRFLT”：过滤M-CDR话单。“SMOCDRFLT”：过滤SMS-SMO-CDR话单。“SMTCDRFLT”：过滤SMS-SMT-CDR话单。“SCDRFLT”：过滤S-CDR话单。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数对话单过滤规则记录指定名称。
命令举例 
查询IMIS过滤话单配置。 
SHOW IMSI CDR FILTER;  
`
命令 (No.1): SHOW IMSI CDR FILTER
操作维护         IMSI号段   是否过滤话单                                    用户别名
------------------------------------------------------------------------------------
复制 修改 删除   44555      过滤M-CDR & 过滤SMS-SMO-CDR & 过滤SMS-SMT-CDR   test
------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
 ` 
父主题： [IMSI号段过滤CDR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 本地话单策略配置 
# 本地话单策略配置 
相关主题 
 
设置本地话单策略配置(SET LOCAL CDR POLICY)
 
 
查询本地话单策略配置(SHOW LOCAL CDR POLICY)
 
 
父主题： [计费配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置本地话单策略配置(SET LOCAL CDR POLICY) 
## 设置本地话单策略配置(SET LOCAL CDR POLICY) 
命令功能 
该命令用于配置当SGSN与CG服务器之间的链路异常时，SGSN将产生的话单信息写入到本地话单文件的策略，比如本地话单是否加密、以及加密所使用的秘钥。 
注意事项 
话单加密开关由关闭到打开时，必须同步设置加密秘钥。若系统中存在加密的本地话单，则不能修改加密秘钥。 
参数说明 
标识|名称|类型|说明
---|---|---|---
CDRENCRYPTION|本地话单是否加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|
CDRENCPWDKEY|本地话单加密秘钥|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:8~32个字符。|
CDRENCPWDKEYCON|确认本地话单加密秘钥|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:8~32个字符。|
命令举例 
设置本地话单策略配置。本地话单是否加密为否。 
SET LOCAL CDR POLICY:CDRENCRYPTION="NO" 
父主题： [本地话单策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询本地话单策略配置(SHOW LOCAL CDR POLICY) 
## 查询本地话单策略配置(SHOW LOCAL CDR POLICY) 
命令功能 
该命令用于查询当SGSN与CG服务器之间的链路异常时，SGSN将产生的话单信息写入到本地话单文件的策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CDRENCRYPTION|本地话单是否加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|
命令举例 
查询本地话单策略配置。 
SHOW LOCAL CDR POLICY 
`
命令 (No.1): SHOW LOCAL CDR POLICY
操作维护                本地话单是否加密
------------------------------------------------------
修改                    是                        
------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [本地话单策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
