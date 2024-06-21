 NF发现和选择配置 


背景知识 


AMF执行业务流程时要和周边NF进行交互，交互前要发现和选择对应的NF，这些NF包括：AUSF、UDM、PCF、SMF、SMSF和AMF。 


 
AUSF发现和选择：
UE注册时，AMF发现和选择合适的AUSF进行鉴权。 

 
UDM发现和选择：
UE在注册时，完成到UDM的登记，AMF发现和选择合适的UDM。 

 
PCF发现和选择：
UE在注册时，AMF为UE进行策略关联的建立，发现和选择合适的PCF。 

 
SMF发现和选择：
UE发起PDU会话建立，AMF发现和选择合适的SMF建立PDU会话。 

 
SMSF发现和选择：
UE通过NAS消息投递短消息时，AMF发现和选择合适的SMSF进行短消息投递。 

 
AMF发现和选择：
UE在5G网络内移动，目标区域不是当前UE所在AMF的服务区时，根据目标区域发现和选择新AMF为UE提供服务。 

 




功能说明 


NF发现和选择配置提供：NF发现强制策略、发现模式、查询结果缓存、通过NRF发现AUSF、PCF、SMF、UDM、AMF和SMSF时的参数、本地解析、地址类型选择策略和等价NF选择策略。 




子主题： 






# NF发现策略配置 
# NF发现策略配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置各NF解析数据，发现和选择NF。因此AMF需要提供NF发现模式选择。 

AMF和远端的NRF进行消息交互，发现和选择各NF时，消息量大，AMF需要将NRF查询结果缓存到本地，以有效的减少网络中的信令量。 




功能说明 


NF发现策略配置提供强制发现策略、发现模式和开启NRF查询结果缓存。 




子主题： 






## 发现模式配置 
## 发现模式配置 


背景知识 


在5GC网络中，AMF与其它NF进行业务交互时，需要获取对应NF的信息以保证两者之间能成功通信，AMF获取NF的方式有两种，通过NRF发现和通过本地配置发现。 




功能说明 


本功能用于配置AMF发现NF的方式，包括通过NRF发现和通过本地配置发现。 




子主题： 






### 修改NF发现模式配置(SET NFDISCOVERYMODE CONFIG) 
### 修改NF发现模式配置(SET NFDISCOVERYMODE CONFIG) 


功能说明 

该命令用于设置或修改AMF发现NF的模式。 


注意事项 


 
本命令执行后，配置立即生效。 

 
当参数“发现模式”配置为“通过NRF发现”或“优先使用NRF”时，需要确保被发现的NF已经在NRF中注册。 

 
当参数“发现模式”配置为“通过本地配置发现NF”时，需要确保已增加了被发现的NF的本地解析配置，比如当NSSF的“发现模式”配置为“通过本地配置发现NF”，需要确保已使用ADD NSSFPROFILECFG命令配置NSSF的本地解析数据。 

 
该命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
discoverySmsfMode|SMSF发现模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: DiscNfByNrf|参数作用：该参数用于设置AMF发现SMSF的模式，取值及含义如下：通过NRF发现：当配置为NRF发现时，AMF通过NRF发现SMSF。通过本地配置发现：当配置为本地配置发现时，AMF通过本地配置发现SMSF。优先使用NRF发现：当配置为优先使用NRF发现时，AMF先通过NRF发现SMSF，如果失败后，会使用本地配置的数据发现SMSF。修改影响：无。数据来源：本端规划。默认值：通过NRF发现。配置原则：当SMSF的“发现模式”配置为“通过本地配置发现NF”，需要确保已使用ADD SMSFPROFILECFG命令配置SMSF的本地解析数据。
discoveryNssfMode|NSSF发现模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: DiscNfByLocal|参数作用：该参数用于设置AMF发现NSSF的模式，取值及含义如下：通过NRF发现：当配置为NRF发现时，AMF通过NRF发现NSSF。通过本地配置发现：当配置为本地配置发现时，AMF通过本地配置发现NSSF。优先使用NRF发现：当配置为优先使用NRF发现时，AMF先通过NRF发现NSSF，如果失败后，会使用本地配置的数据发现NSSF。修改影响：无。数据来源：本端规划。默认值：通过本地配置发现。配置原则：当NSSF的“发现模式”配置为“通过本地配置发现NF”，需要确保已使用ADD NSSFPROFILECFG命令配置NSSF的本地解析数据。
discoveryeirmode|5G-EIR发现模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: DiscNfByNrf|参数作用：该参数用于设置AMF发现5G-EIR的模式，取值及含义如下：通过NRF发现：当配置为NRF发现时，AMF通过NRF发现5G-EIR。通过本地配置发现：当配置为本地配置发现时，AMF通过本地配置发现5G-EIR。优先使用NRF发现：当配置为优先使用NRF发现时，AMF先通过NRF发现5G-EIR，如果失败后，会使用本地配置的数据发现5G-EIR。修改影响：无。数据来源：本端规划。默认值：通过NRF发现。配置原则：无。




命令举例 


`
设置NF发现模式，SMSF发现模式为NRF发现，NSSF发现模式为NRF发现，EIR发现模式为NRF发现,。
SET NFDISCOVERYMODE CONFIG:DISCOVERYSMSFMODE="DiscNfByNrf",DISCOVERYNSSFMODE="DiscNfByNrf",DISCOVERYEIRMODE="DiscNfByNrf"
` 


### 查询NF发现模式配置(SHOW NFDISCOVERYMODE CONFIG) 
### 查询NF发现模式配置(SHOW NFDISCOVERYMODE CONFIG) 


功能说明 

该命令用于查询AMF发现NF的模式。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
discoverySmsfMode|SMSF发现模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: DiscNfByNrf|参数作用：该参数用于设置AMF发现SMSF的模式。通过NRF发现通过本地配置发现优先使用NRF发现
discoveryNssfMode|NSSF发现模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: DiscNfByLocal|参数作用：该参数用于设置AMF发现NSSF的模式。通过NRF发现通过本地配置发现优先使用NRF发现
discoveryeirmode|5G-EIR发现模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: DiscNfByNrf|参数作用：该参数用于设置AMF发现5G-EIR的模式。 通过NRF发现通过本地配置发现优先使用NRF发现




命令举例 


`
查询NF发现模式。
SHOW NFDISCOVERYMODE CONFIG:

(No.11) : SHOW NFDISCOVERYMODE CONFIG:
-----------------Namf_Communication_0----------------
操作维护       SMSF发现模式   NSSF发现模式  5G-EIR发现模式 
------------------------------------------------------------------------
修改          通过NRF发现NF  通过NRF发现NF 通过NRF发现NF  
------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-28 15:44:53 耗时: 0.136 秒

` 


## 发现处理策略配置 
## 发现处理策略配置 


背景知识 


当NF discovery返回的Profile中未携带capacity参数时，需要配置capacity的缺省值以保证合理选择一个NF。 




功能说明 


本功能用于配置发现处理策略，目前只支持capacity的缺省值配置。 




子主题： 






### 修改发现处理策略配置(SET DISCPROCPOLICYCFG) 
### 修改发现处理策略配置(SET DISCPROCPOLICYCFG) 


功能说明 

该命令用于设置发现处理策略，目前只支持capacity的缺省值的设置。 

当NF discovery返回的Profile中未携带capacity参数时，需要配置capacity的缺省值以保证合理选择一个NF。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
DEFCAPACITY|缺省权重|参数可选性: 必选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置发现处理策略配置中capacity的缺省值。Capacity又被称为静态权重，是同一类型的NF实例的相对权重值。




命令举例 


`
设置发现处理策略配置中capacity的缺省值为10。 
SET DISCPROCPOLICYCFG:DEFCAPACITY=10
` 


### 查询发现处理策略配置(SHOW DISCPROCPOLICYCFG) 
### 查询发现处理策略配置(SHOW DISCPROCPOLICYCFG) 


功能说明 

该命令用于查询发现处理策略配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
DEFCAPACITY|缺省权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于设置发现处理策略配置中capacity的缺省值。Capacity又被称为静态权重，是同一类型的NF实例的相对权重值




命令举例 


`
查询发现处理策略配置。 
SHOW DISCPROCPOLICYCFG:

(No.5) : SHOW DISCPROCPOLICYCFG:
-----------------Namf_Communication_0----------------
Default Capacity
10
记录数：1
执行成功耗时: 0.549 秒

` 


## 查询结果缓存配置 
## 查询结果缓存配置 


背景知识 


在5G网络中，所有的NF都需要将自身的信息注册到NRF中，当5G网络中的NF在需要发现其他NF时，可以到NRF进行获取，根据NF注册的信息，发现这些满足条件的NF并执行对应的业务流程。 




功能说明 


本功能用于控制本AMF通过NRF发现并获取其他的NF信息后，是否将些NF的信息缓存在本地，在后续流程中，避免每次均到NRF去发现其他NF，从而节省网络带宽及加快NRF的处理进度。 




子主题： 






### 修改发现结果是否缓存配置(SET NFDISCOVERYRESULTCACHED) 
### 修改发现结果是否缓存配置(SET NFDISCOVERYRESULTCACHED) 


功能说明 

该命令用于开启或关闭NRF发现结果缓存功能。 

开启此功能可有效的减少AMF和NRF之间的信令交互数量，降低网络信令负荷。 


注意事项 

AMF开启NRF发现结果缓存功能之后，并非每次都实时向NRF查询，因此如果NRF侧信息有变化，需要主动向AMF更新缓存，避免AMF使用旧的缓存。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
nfDiscResultCached|发现结果是否缓存|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DISCOVERYRESULTCACHED|该参数用于配置AMF是否缓存NRF发现的结果。




命令举例 


`
设置AMF支持缓存NRF发现结果。
SET NFDISCOVERYRESULTCACHED:NFDISCRESULTCACHED="DISCOVERYRESULTCACHED"
` 


### 查询发现结果是否缓存配置(SHOW NFDISCOVERYRESULTCACHED) 
### 查询发现结果是否缓存配置(SHOW NFDISCOVERYRESULTCACHED) 


功能说明 

该命令用于查询AMF是否开启了NRF发现结果缓存功能。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
nfDiscResultCached|发现结果是否缓存|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DISCOVERYRESULTCACHED|该参数用于配置AMF是否缓存NRF发现的结果。




命令举例 


`
查询AMF是否支持缓存NRF发现结果。
SHOW NFDISCOVERYRESULTCACHED

(No.1) : SHOW NFDISCOVERYRESULTCACHED:
-----------------Namf_Communication_0----------------
发现结果是否缓存
不缓存
记录数：1
执行成功耗时: 0.932 秒

` 


# NF发现参数配置 
# NF发现参数配置 


背景知识 


AMF通过NRF发现其他NF时，需要考虑的因素不同，包括用户号码、切片、路由信息、DNN、位置信息和PLMN等。因运营商的部署环境不同，考虑的因素也有差异。 




功能说明 


本功能用于配置AMF发现AUSF、PCF、SMF、UDM、AMF和SMSF的参数。 




子主题： 






## 发现AUSF参数配置 
## 发现AUSF参数配置 


背景知识 


AMF需要通过NRF来发现AUSF（Authentication Server Function，鉴权服务器功能），并选择一个合适的AUSF来获取鉴权向量。 

AMF发现和选择AUSF时，可参考以下因素，包括：SUPI、Routing Indicator、preferred-locality。 具体参见3GPP TS 23501协议“6.3.4 AUSF discovery and selection”章节。 




功能说明 


本功能用于控制AMF通过NRF发现AUSF时，发送给NRF的发现消息中所携带的参数。 




子主题： 






### 修改NRF发现AUSF参数配置(SET NRFDISCAUSFPARACFG) 
### 修改NRF发现AUSF参数配置(SET NRFDISCAUSFPARACFG) 


功能说明 

该命令用于修改NRF发现AUSF参数配置。当AMF需要发现AUSF时，使用该命令配置AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数，NRF可根据这些参数作为参考因素来选择合适的AUSF。 

包括是否携带如下参数：SUPI、Routing Indicator、preferred-locality、carryhnwpubkeyid。比如是否包含SUPI，即在AMF发送给NRF的Nnrf_NF Discovery请求消息中，所携带的查询条件是否携带SUPI。 


注意事项 


 
该命令执行后，配置立即生效。 

 
具体参数的选择，要根据网络中AUSF的实际能力来设置，确保AUSF向NRF注册时，AUSF向NRF上报的NF Profile中携带了这些信息。其中，SUPI、Routing Indicator二者必须携带其中一个。比如，通过此命令设置为AMF发现AUSF时，AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数需要携带SUPI，则要确保AUSF向NRF注册时，已经携带了SUPI信息，否则会导致AMF发现AUSF失败，影响鉴权。 

 

如果通过此命令设置为AMF发现AUSF时，AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数需要携带preferred-locality，但preferred-locality字段是否有效取决于获取到的AUSF位置信息是否有效。 

AUSF位置信息来源如下： 


 
通过ADD PREFER LOCALITY命令配置的AUSF位置，即AMF配置的NF优选位置。 

 
如果通过ADD PREFER LOCALITY命令无法获取到AUSF位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carryParaMode|携带参数方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupiPrior|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在查询条件中携带的参数，取值及含义如下：Routing Indicator优先。SUPI优先：则AMF发出的Nnrf_NFDiscovery请求中携带SUPI字段，根据SUPI匹配到多个可用的AUSF修改影响：有Routing Indicator优先和SUPI优先两种选项，修改该参数，可以修改AMF发送给NRF的请求消息中携带的参数。数据来源：本端规划。默认值：否。配置原则：无。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupLocality）配置原则：preferred-locality字段是否有效取决于获取到的AUSF位置信息是否有效。AUSF位置信息来源如下：通过ADD PREFER LOCALITY命令配置的AUSF位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到AUSF位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现AUSF时，是否支持在NRF的发现结果中，基于Locality来优选目标AUSF（即AMF根据本地配置的AUSF位置来选择AUSF），取值及含义如下：不支持：AMF不支持根据本地配置的AUSF位置来选择AUSF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标AUSF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取AUSF的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据AUSF的位置选择AUSF的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取AUSF的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取AUSF的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。数据来源：本端规划。默认值：不携带。配置原则：当"携带参数方式（carryParaMode）"配置为"Routing Indicator优先"时，本参数才会生效。




命令举例 


`
设置通过NRF发现AUSF的时候，优先携带Routing Indicator，不携带preferred-locality，不支持基于Locality优选。
SET NRFDISCAUSFPARACFG:CARRYPARAMODE="RoutingPrior",CARRYPRELOCALITY="NOTCARRYPRELOCALITY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYHNWPUBKEYID="NOTCARRY"
` 


### 查询NRF发现AUSF参数配置(SHOW NRFDISCAUSFPARACFG) 
### 查询NRF发现AUSF参数配置(SHOW NRFDISCAUSFPARACFG) 


功能说明 

该命令用于查询AMF通过NRF发现AUSF时，AMF发送给NRF的请求消息中的参数配置。 


注意事项 

无


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carryParaMode|携带参数方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupiPrior|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在查询条件中携带的参数，取值及含义如下：Routing Indicator优先。SUPI优先：则AMF发出的Nnrf_NFDiscovery请求中携带SUPI字段，根据SUPI匹配到多个可用的AUSF
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现AUSF时，是否支持在NRF的发现结果中，基于Locality来优选目标AUSF（即AMF根据本地配置的AUSF位置来选择AUSF），取值及含义如下：不支持：AMF不支持根据本地配置的AUSF位置来选择AUSF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标AUSF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取AUSF的位置。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。




命令举例 


`
查看通过NRF发现AUSF的时候，优先携带发现参数SUPI，不携带preferred-locality，不支持基于Locality优选。 
SHOW NRFDISCAUSFPARACFG:

(No.2) : SHOW NRFDISCAUSFPARACFG:
-----------------Namf_Communication_0----------------------------------------------------------------
操作维护       携带参数方式 携带preferred-locality      支持基于Locality优选     携带home-pub-key-id策略
-----------------------------------------------------------------------------------------------------
修改           SUPI优先     不携带preferred-locality     不支持                      不携带
-----------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-08 19:30:41 耗时: 0.159 秒

` 


### 新增基于PLMN的NRF发现AUSF参数配置(ADD NRFDISCAUSFPLMNPARACFG) 
### 新增基于PLMN的NRF发现AUSF参数配置(ADD NRFDISCAUSFPLMNPARACFG) 


功能说明 

该命令用于新增一组AMF基于PLMN通过NRF发现AUSF的参数配置。当AMF需要发现AUSF以获取鉴权向量时，使用该命令，基于PLMN配置AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数。 


注意事项 


 
该命令执行后，配置立即生效。 

 
具体参数的选择，根据网络中AUSF的实际能力来设置，确保AUSF向NRF注册NF Profile时携带了这些信息。比如，通过此命令设置发现时携带preferred-locality，则要确保AUSF向NRF注册时已经携带了preferred-locality，否则会导致AMF发现AUSF失败。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带preferred-locality字段。数据来源：本端规划。默认值：NOTCARRYPRELOCALITY。配置原则：preferred-locality字段是否有效取决于获取到的UDM位置信息是否有效。UDM位置信息来源如下：通过ADD PREFER LOCALITY命令配置的UDM位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到UDM位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据UDM的位置选择UDM的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取UDM的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。数据来源：本端规划。默认值：不携带。配置原则：当SET NRFDISCAUSFPARACFG命令中的参数“携带参数方式（CARRYPARAMODE）”配置为“Routing Indicator优先”时，本参数才会生效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。




命令举例 


`
该命令用于新增一组AMF通过基于PLMN的NRF发现AUSF的参数配置。移动国家码为460，移动网络码为11，不携带preferred-locality，不支持基于Locality优选，不携带home-pub-key-id。
ADD NRFDISCAUSFPLMNPARACFG:MCC="460",MNC="11",CARRYPRELOCALITY="NOTCARRYPRELOCALITY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYHNWPUBKEYID="NOTCARRY"
` 


### 修改基于PLMN的NRF发现AUSF参数配置(SET NRFDISCAUSFPLMNPARACFG) 
### 修改基于PLMN的NRF发现AUSF参数配置(SET NRFDISCAUSFPLMNPARACFG) 


功能说明 

该命令用于修改AMF基于PLMN通过NRF发现AUSF的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带preferred-locality字段。数据来源：本端规划。默认值：NOTCARRYPRELOCALITY。配置原则：preferred-locality字段是否有效取决于获取到的UDM位置信息是否有效。UDM位置信息来源如下：通过ADD PREFER LOCALITY命令配置的UDM位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到UDM位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据UDM的位置选择UDM的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取UDM的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。数据来源：本端规划。默认值：不携带。配置原则：当SET NRFDISCAUSFPARACFG命令中的参数“携带参数方式（CARRYPARAMODE）”配置为“Routing Indicator优先”时，本参数才会生效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。




命令举例 


`
该命令用于修改基于PLMN的NRF发现AUSF参数配置。修改移动国家码460移动网络码11，不携带preferred-locality，不支持基于Locality优选，不携带home-pub-key-id。
SET NRFDISCAUSFPLMNPARACFG:MCC="460",MNC="11",CARRYPRELOCALITY="NOTCARRYPRELOCALITY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYHNWPUBKEYID="NOTCARRY"
` 


### 删除基于PLMN的NRF发现AUSF参数配置(DEL NRFDISCAUSFPLMNPARACFG) 
### 删除基于PLMN的NRF发现AUSF参数配置(DEL NRFDISCAUSFPLMNPARACFG) 


功能说明 

该命令用于删除一组AMF基于PLMN通过NRF发现AUSF的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。




命令举例 


`
该命令用于删除基于PLMN的NRF发现AUSF参数配置。删除移动国家码460，移动网络码11。
DEL NRFDISCAUSFPLMNPARACFG:MCC="460",MNC="11"
` 


### 查询基于PLMN的NRF发现AUSF参数配置(SHOW NRFDISCAUSFPLMNPARACFG) 
### 查询基于PLMN的NRF发现AUSF参数配置(SHOW NRFDISCAUSFPLMNPARACFG) 


功能说明 

该命令用于查询AMF基于PLMN通过NRF发现AUSF时，AMF发送给NRF的请求消息中的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现AUSF是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现AUSF是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现AUSF时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。




命令举例 


`
该命令用于查询基于PLMN的NRF发现AUSF参数配置。
SHOW NRFDISCAUSFPLMNPARACFG:

(No.4) : SHOW NRFDISCAUSFPLMNPARACFG:
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 携带preferred-locality      支持基于Locality优选   携带home-pub-key-id策略
-------------------------------------------------------------------------------------------------------------
复制 修改 删除 460        11         不携带preferred-locality    Not Support            不携带
-------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-08 19:46:11 耗时: 0.148 秒

` 


## 发现PCF参数配置 
## 发现PCF参数配置 


背景知识 


AMF需要通过NRF来发现PCF，并选择一个合适的PCF来获取策略信息。 

AMF发现和选择PCF时，可参考以下因素，包括：SUPI，sNSSAI，GPSI。 具体参见3GPP TS 23501协议“6.3.7 PCF discovery and selection”章节。 




功能说明 


本功能用于控制AMF通过NRF发现PCF时，发送给NRF的发现消息中所携带的参数。 

具体参数的选择，要根据网络中PCF的实际能力来设置，确保PCF向NRF注册NF Profile时，携带了这些信息。比如，通过此命令设置发现时携带SUPI，则要确保PCF向NRF注册时已经携带了SUPI信息，否则会导致AMF发现PCF失败。 




子主题： 






### 修改NRF发现PCF参数配置(SET NRFDISCPCFPARACFG) 
### 修改NRF发现PCF参数配置(SET NRFDISCPCFPARACFG) 


功能说明 

该命令用于设置当AMF发现PCF时，发送给NRF的消息中需要携带的参考因素，即在AMF发送给NRF的Nnrf_NFDiscovery请求消息中，所携带的查询条件。  

包括是否携带如下参数： 


 
SUPI（Subscriber Permanent Identifier，用户永久标识） 

 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息） 

 
GPSI（Generic Public Subscription Identifier，一般公共用户标识） 

 

当网络中的PCF支持向NRF注册号段范围，希望根据终端用户的号段选择PCF时，需要配置此功能。 


注意事项 


 
该命令执行后，配置立即生效。 

 
此配置需要根据网络中PCF的实际能力来设置，确保PCF向NRF注册NF Profile时携带了特定的参数。比如进行如下配置：当AMF发现PCF时，带给NRF的消息中需要携带SUPI，则要确保PCF向NRF注册时，已经携带了SUPI信息，否则会导致AMF发现PCF失败。 

 
该命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carrySupi|携带SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSupi|参数作用：该参数用于设置AMF通过NRF发现PCF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带SUPI，取值及含义如下：不支持SUPI支持SUPI：AMF发出的Nnrf_NFDiscovery请求中携带SUPI字段为当前用户的SUPI。修改影响：如果设置为支持，则AMF发出的Nnrf_NFDiscovery请求中携带SUPI字段，根据SUPI匹配到多个可用的UDM。数据来源：本端规划。默认值：支持SUPI配置原则：无。
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupSnssai|参数作用：该参数用于设置AMF通过NRF发现PCF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带S-NSSAI（为当前用户的Allowed Nssai），取值及含义如下：不支持SNSSAI：不携带“SNSSAI”字段。支持SNSSAI：携带“SNSSAI”字段，AMF发出的Nnrf_NFDiscovery请求中携带S-NSSAI字段。为当前要建立的PDU所对应的S-NSSAI。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带SNSSAI字段。数据来源：本端规划。默认值：不支持SNSSAI配置原则：无。
carryGpsi|携带GPSI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupGpsi|参数作用：该参数用于设置AMF通过NRF发现PCF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带携带GPSI，取值及含义如下：不支持GPSI支持GPSI：如果设置为支持，则AMF发出的Nnrf_NFDiscovery请求中携带GPSI字段。 为当前用户的GPSI修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带GPSI字段。数据来源：本端规划。默认值：不支持GPSI配置原则：无。




命令举例 


`
设置通过NRF发现PCF的时候，携带用户SUPI、SNSSAI、GPSI。
SET NRFDISCPCFPARACFG:CARRYSUPI="SupSupi",CARRYSNSSAI="SupSnssai",CARRYGPSI="SupGpsi"
` 


### 查询NRF发现PCF参数配置(SHOW NRFDISCPCFPARACFG) 
### 查询NRF发现PCF参数配置(SHOW NRFDISCPCFPARACFG) 


功能说明 

该命令用于查询NRF发现PCF参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carrySupi|携带SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSupi|参数作用：该参数用于设置AMF通过NRF发现PCF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带SUPI，取值及含义如下：不支持SUPI支持SUPI：AMF发出的Nnrf_NFDiscovery请求中携带SUPI字段为当前用户的SUPI。
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupSnssai|参数作用：该参数用于设置AMF通过NRF发现PCF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带S-NSSAI（为当前用户的Allowed Nssai），取值及含义如下：不支持SNSSAI：不携带“SNSSAI”字段。支持SNSSAI：携带“SNSSAI”字段，AMF发出的Nnrf_NFDiscovery请求中携带S-NSSAI字段。为当前要建立的PDU所对应的S-NSSAI。
carryGpsi|携带GPSI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupGpsi|参数作用：该参数用于设置AMF通过NRF发现PCF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带携带GPSI，取值及含义如下：不支持GPSI支持GPSI：如果设置为支持，则AMF发出的Nnrf_NFDiscovery请求中携带GPSI字段。 为当前用户的GPSI




命令举例 


`
查看通过NRF发现PCF的时候，是否支持携带SUPI。 
SHOW NRFDISCPCFPARACFG:

(No.4) : SHOW NRFDISCPCFPARACFG:
-----------------Namf_Communication_0----------------
携带SUPI 携带SNSSAI 携带GPSI
支持SUPI 支持SNSSAI 支持GPSI
记录数：1
执行成功耗时: 0.06 秒

` 


## 发现SMF参数配置 
## 发现SMF参数配置 


背景知识 


UE发起PDU会话建立流程，AMF需要选择合适的SMF建立PDU会话。 

在非漫游或者漫游LBO场景下，当UE发起PDU会话建立流程或移动性相关的业务流程时，如果A-SMF管理的UPF无法与UE所在的eNodeB建立连接，那么AMF此时需要根据UE当前所在的位置，选择合适的I-SMF，为UE建立PDU会话。 

在漫游HR场景下，当UE发起PDU会话建立流程或移动性相关的业务流程时，AMF需要根据UE当前的位置，选择合适的V-SMF， 为UE建立PDU会话。 

AMF通过NRF发现的方式，来选择A/H-SMF，可携带如下参数： 


 
DNN（Data Network Name，数据网络名称） 

 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息） 

 
NSI-ID（Network Slice Instance，网络切片实例） 

 
Tai 

 
PLMN 

 
PGW-ind 

 
preferred-locality 

 
preferred-Tai 

 
servingScope 

 

具体描述，参见3GPP TS 23501协议“6.3.2 SMF discovery and selection”。 




功能说明 


本功能用于控制AMF通过NRF发现SMF时，发送给NRF的发现消息中所携带的参数。 如果AMF支持网络切片选择功能，需要通过此命令设置AMF发现SMF时所参考的因素。 

具体参数的选择，要根据网络中SMF的实际能力来设置，确保SMF向NRF注册NF Profile时携带了这些信息。比如，通过此命令设置发现时携带DNN，则要确保切片中的SMF向NRF注册时已经携带了DNN信息，否则会导致AMF发现SMF失败，影响用户PDU建立。 




子主题： 






### 发现A-SMF参数配置 
### 发现A-SMF参数配置 


背景知识 


AMF需要通过NRF来发现A-SMF，并选择一个合适的A-SMF来为UE建立PDU会话。 




功能说明 


本功能用于控制AMF通过NRF发现A-SMF时，发送给NRF的发现消息中所携带的参数。  




子主题： 






#### 修改NRF发现A-SMF参数配置(SET NRFDISCSMFPARACFG) 
#### 修改NRF发现A-SMF参数配置(SET NRFDISCSMFPARACFG) 


功能说明 

该命令用于修改AMF通过NRF发现A-SMF（Anchor-SMF，锚点SMF）的参数配置。 

当AMF需要发现A-SMF时，使用该命令配置AMF发送给NRF的发现请求消息中所携带的参数，NRF可根据这些参数作为参考因素来选择合适的A-SMF。包括如下参数：S-NSSAI、PLMN、NS-ID（Network Slice Instance，网络切片实例）、preferred-locality、servingScope等。  

通过此命令可以配置AMF基于Locality优选SMF的策略（即AMF根据SMF的位置来优先选择目标SMF）。AMF执行Locality优选时，只能使用NRF优选和本地优选中的一种；在同时配置的情况下，以本地优选的优先级为高。 


 
NRF优选：对应本命令的参数“携带preferred-locality（CARRYLOCALITY）”，AMF通过NRF发现SMF时，需要携带preferred-locality参数。 

 
本地优选：对应本命令的参数“支持基于Locality优选（SUPPLOCALITYSEL）”，AMF通过NRF发现SMF时，不携带preferred-locality参数，AMF基于Locality（即本地配置的的数据）选择目标SMF。 

 

通过此命令可以配置AMF基于TAI选择SMF的策略： 


 
基于TAI选择A-SMF：本命令的参数”携带Preferred跟踪区标识（CARRYPREFERREDTAI）“用于控制AMF是否基于TAI通过NRF发现A-SMF。在该参数配置为“不携带（NotSupPreferredTai）”或者NRF不支持preferred-tai时，还可以通过SET ASMFSELPOLICY命令中的配置参数”A-SMF选择支持优选TA（AMFSELASMFBYTA）“，控制AMF是否基于TAI来优选A-SMF。 

 
基于TAI选择H-SMF：本命令的参数”携带跟踪区标识（CARRYTA）“用于控制AMF是否基于TAI通过NRF发现H-SMF。 

 

通过此命令可以配置AMF基于servingScope选择SMF的策略（servingScope也是一种根据SMF的位置来优先选择目标SMF的策略）： 


 
本命令的参数”携带servingScope（CARRYSERVINGSCOPE）“用于控制AMF是否基于servingScope通过NRF发现A-SMF。 

 
通过配置参数”服务范围扩展策略（SERVSCOPEEXTPLY）“控制SMF选择使用的servingScope。当该参数配置为”不支持扩展（NotSupServScopeExtPly）“时，则优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）“；当该参数配置为”支持扩展（SupServScopeExtPly）“时，则使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。 

 


注意事项 


 
该命令执行后，配置立即生效。 

 
SMF发现参数的配置，要根据5GC网络中SMF的实际能力来设置，确保SMF向NRF注册NF Profile时携带了这些信息。比如，通过此命令配置参数”携带SNSSAI（CARRYSNSSAI）”为“支持SNSSAI（SupSnssai）”，则要确保目标切片网络中的SMF向NRF注册时已经携带了S-NSSAI信息，否则会导致AMF发现SMF失败，影响用户PDU会话的建立。 

 
通过此命令配置参数“携带preferred-locality（CARRYLOCALITY）”为“携带（SupLocality）”或者参数“支持基于Locality优选（SUPPLOCALITYSEL）”为“支持（SUPPORT）”时，可以使用ADD PREFER LOCALITY命令中配置的参数“优选位置（PRELOCALITY）”（即，指定Locality），也可以使用SET AMFLOCALOFFICECFG命令中配置的参数“位置信息（LOCALITY）”（即，AMF的Locality）。 

 
该命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carryOIinDNN|DNN携带OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotCarryOI|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中携带DNN时是否需要包含OI（Operator Identifier，运营商标识），取值及含义如下：不支持OI：不携带“OI”字段。支持OI：携带“OI”字段，AMF发出的Nnrf_NFDiscovery请求中携带的DNN字段包含OI。修改影响：无。数据来源：本端规划。默认值：不支持OI（NotCarryOI）配置原则：无。
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSnssai|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带S-NSSAI（为当前用户的Allowed Nssai），取值及含义如下：不支持SNSSAI：不携带“SNSSAI”字段。支持SNSSAI：携带“SNSSAI”字段，AMF发出的Nnrf_NFDiscovery请求中携带S-NSSAI字段。为当前要建立的PDU所对应的S-NSSAI。修改影响：无。数据来源：本端规划。默认值：支持SNSSAI（SupSnssai）配置原则：无。
carryPlmn|携带目标PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupPlmn|参数作用：该参数用于配置在非漫游场景下，AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带目标PLMN，取值及含义如下：不支持PLMN：不携带“PLMN”字段。支持PLMN：携带“PLMN”字段，AMF发出的Nnrf_NFDiscovery请求中携带目标PLMN字段。修改影响：无。数据来源：本端规划。默认值：不支持（PLMNNotSupPlmn）配置原则：无。
carryNsiId|携带切片实例号|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupNsiId|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带NSI（Network Slice Instance，网络切片实例） ID，取值及含义如下：不支持切片实例号：不携带“切片实例号”字段。支持切片实例号：携带“切片实例号”字段，则AMF发出的Nnrf_NFDiscovery请求中携带NSI ID字段。修改影响：无。数据来源：本端规划。默认值：不支持切片实例号（NotSupNsiId）配置原则：无。
carryLocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupLocality|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupLocality）配置原则：preferred-locality字段是否有效取决于AMF获取到的SMF位置信息是否有效。SMF位置信息来源如下：通过ADD PREFER LOCALITY命令配置的SMF位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到SMF位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
carryPgwInd|携带pgw-ind标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupCarryPgwInd|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带pgw-ind，取值及含义如下：不支持携带pgw-ind标识：不携带“pgw-ind”字段。支持携带pgw-ind标识：携带“pgw-ind”字段，AMF发出的Nnrf_NFDiscovery请求中携带pgw-ind。修改影响：无。数据来源：本端规划。默认值：支持携带pgw-ind标识（SupCarryPgwInd）配置原则：无。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据SMF的位置选择SMF的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取SMF的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。修改影响：无。数据来源：本端规划。默认值：携带（SupPreferredTai）配置原则：无。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupTai）配置原则：无。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupCarryServingScope）。配置原则：配置本参数之前，需要确认License项： "AMF支持基于servingScope选择SMF"已激活，否则本参数无法生效。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。修改影响：无。数据来源：本端规划。默认值：0配置原则：如果此配置设置为非0值时，本参数的取值来源于ADD SMF SERVSCOPE GRP命令中的参数"服务范围组标识（SERVSCOPEGRPID）"，必须通过ADD SMF SERVSCOPE GRP命令预先配置，否则本参数无法生效。如果本命令的参数“服务范围扩展策略（SERVSCOPEEXTPLY）”配置为“不扩展（NotSupServScopeExtPl）”，在用户没有配置本参数的情况下，则默认使用SET AMFLOCALOFFICECFG命令中的默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。NRF对于“服务范围”按照“包含”逻辑进行处理，即SMF能为发现请求中携带的所有服务范围提供服务，NRF才会认为其满足条件；所以如果参数“服务范围扩展策略（SERVSCOPEEXTPLY）”配置为“不扩展（NotSupServScopeExtPl）”，本参数在输入时，应避免输入无效的服务范围组标识。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。修改影响：无。数据来源：本端规划。默认值：不扩展（NotSupServScopeExtPly）配置原则：无。




命令举例 


`
AMF向NRF发现A-SMF时，支持DNN携带OI，携带S-NSSAI、跟踪区标识、目标PLMN、NSIID、preferred-locality、PreferredTai、pgw-ind标识参数，支持基于Locality优选，支持携带服务范围，设置服务区范围组标识为1，设置服务范围扩展策略为基于TA信息映射。
SET NRFDISCSMFPARACFG:CARRYOIINDNN="CarryOI",CARRYSNSSAI="SupSnssai",CARRYPLMN="SupPlmn",CARRYNSIID="SupNsiId",CARRYLOCALITY="SupLocality",CARRYPGWIND="SupCarryPgwInd",SUPPLOCALITYSEL="SUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="SupTai",CARRYSERVINGSCOPE="SupCarryServingScope",SERVSCOPEGRPID=1,SERVSCOPEEXTPLY="SupServScopeExtPly"
` 


#### 查询NRF发现A-SMF参数配置(SHOW NRFDISCSMFPARACFG) 
#### 查询NRF发现A-SMF参数配置(SHOW NRFDISCSMFPARACFG) 


功能说明 

该命令用于查询AMF通过NRF发现A-SMF时，AMF发送给NRF的请求消息中所携带的参数，NRF可根据这些参数作为参考因数来选择合适的SMF。   


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carryOIinDNN|DNN携带OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotCarryOI|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中携带DNN时是否需要包含OI（Operator Identifier，运营商标识），取值及含义如下：不支持OI：不携带“OI”字段。支持OI：携带“OI”字段，AMF发出的Nnrf_NFDiscovery请求中携带的DNN字段包含OI。
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSnssai|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带S-NSSAI，取值及含义如下：不支持SNSSAI：不携带“SNSSAI”字段。支持SNSSAI：携带“SNSSAI”字段，AMF发出的Nnrf_NFDiscovery请求中携带S-NSSAI字段。为当前要建立的PDU所对应的S-NSSAI。
carryPlmn|携带目标PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupPlmn|参数作用：该参数用于配置在非漫游场景下，AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带目标PLMN，取值及含义如下：不支持PLMN：不携带“PLMN”字段。支持PLMN：携带“PLMN”字段，AMF发出的Nnrf_NFDiscovery请求中携带目标PLMN字段。
carryNsiId|携带切片实例号|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupNsiId|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带NSI（Network Slice Instance，网络切片实例） ID，取值及含义如下：不支持切片实例号：不携带“切片实例号”字段。支持切片实例号：携带“切片实例号”字段，则AMF发出的Nnrf_NFDiscovery请求中携带NSI ID字段。
carryLocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupLocality|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
carryPgwInd|携带pgw-ind标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupCarryPgwInd|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带pgw-ind，取值及含义如下：不支持携带pgw-ind标识：不携带“pgw-ind”字段。支持携带pgw-ind标识：携带“pgw-ind”字段，AMF发出的Nnrf_NFDiscovery请求中携带pgw-ind。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。




命令举例 


`
查询当前AMF发现A-SMF时所携带参数的配置。
SHOW NRFDISCSMFPARACFG

(No.1) : SHOW NRFDISCSMFPARACFG:
-----------------Namf_Communication_0----------------
操作维护       DNN携带OI 携带SNSSAI 携带目标PLMN 携带切片实例号 携带preferred-locality  携带pgw-ind标识     支持基于Locality优选 携带Preferred跟踪区标识 携带跟踪区标识 携带servingScope 服务范围组标识 服务范围扩展策略 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           支持OI    支持SNSSAI 支持PLMN     支持切片实例号 携带                    支持携带pgw-ind标识 支持                 携带                    携带           携带             1              基于TA信息映射   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-04-22 10:20:22 耗时: 0.13 秒

` 


#### 新增基于PLMN的NRF发现A-SMF参数配置(ADD PLMN NRFDISCSMFPARA) 
#### 新增基于PLMN的NRF发现A-SMF参数配置(ADD PLMN NRFDISCSMFPARA) 


功能说明 

该命令用于新增一组AMF基于PLMN和DNN两个维度来通过NRF发现A-SMF的参数配置。当AMF需要发现SMF以创建和管理PDU会话时，使用该命令，配置AMF发送给NRF的请求消息中所携带的参数。 


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令基于PLMN和DNN两个维度来通过NRF发现A-SMF（Anchor-SMF，锚点SMF），优先级从高到低顺序为：PLMN+DNN、PLMN、DNN。AMF先使用PLMN+DNN进行匹配，如果不能获取对应的记录，就使用PLMN进行匹配，如果仍然不能匹配相应的记录，则使用DNN进行匹配。 

 
该命令最多只能配置4096条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于用户的DNN来通过NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：无。数据来源：本端规划。默认值：不携带。配置原则：无。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据SMF的位置选择SMF的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取SMF的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。修改影响：无。数据来源：本端规划。默认值：携带（SupPreferredTai）配置原则：无。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupTai）配置原则：无。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupCarryServingScope）。配置原则：配置本参数之前，需要确认License项： "AMF支持基于servingScope选择SMF"已激活，否则本参数无法生效。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。修改影响：无。数据来源：本端规划。默认值：0配置原则：如果此配置设置为非0值时，本参数的取值来源于ADD SMF SERVSCOPE GRP命令中的参数"服务范围组标识（SERVSCOPEGRPID）"，必须通过ADD SMF SERVSCOPE GRP命令预先配置，否则本参数无法生效。如果本命令的参数“服务范围扩展策略（SERVSCOPEEXTPLY）”配置为“不扩展（NotSupServScopeExtPl）”，在用户没有配置本参数的情况下，则默认使用SET AMFLOCALOFFICECFG命令中的默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。NRF对于“服务范围”按照“包含”逻辑进行处理，即SMF能为发现请求中携带的所有服务范围提供服务，NRF才会认为其满足条件；所以如果参数“服务范围扩展策略（SERVSCOPEEXTPLY）”配置为“不扩展（NotSupServScopeExtPl）”，本参数在输入时，应避免输入无效的服务范围组标识。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。修改影响：无。数据来源：本端规划。默认值：不扩展（NotSupServScopeExtPly）配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。




命令举例 


`
新增MCC是460，MNC是11，DNN是"zte.com.cn"的NRF发现A-SMF参数配置，不携带跟踪区标识，不携带preferred-locality，支持携带prefer-Tai，不支持基于Locality优选，不支持携带servingScope，设置服务区范围组标识为0，设置服务范围扩展策略为不扩展。
ADD PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn",CARRYPRELOCALITY="NOTCARRY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="NotSupTai",CARRYSERVINGSCOPE="NotSupCarryServingScope",SERVSCOPEGRPID=0,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
` 


#### 修改基于PLMN的NRF发现A-SMF参数配置(SET PLMN NRFDISCSMFPARA) 
#### 修改基于PLMN的NRF发现A-SMF参数配置(SET PLMN NRFDISCSMFPARA) 


功能说明 

该命令用于修改一组AMF基于PLMN和DNN两个维度通过NRF发现A-SMF的参数配置。 


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于用户的DNN来通过NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：无。数据来源：本端规划。默认值：不携带。配置原则：无。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据SMF的位置选择SMF的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取SMF的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。修改影响：无。数据来源：本端规划。默认值：携带（SupPreferredTai）配置原则：无。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupTai）配置原则：无。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。修改影响：无。数据来源：本端规划。默认值：不携带（NotSupCarryServingScope）。配置原则：配置本参数之前，需要确认License项： "AMF支持基于servingScope选择SMF"已激活，否则本参数无法生效。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。修改影响：无。数据来源：本端规划。默认值：0配置原则：如果此配置设置为非0值时，本参数的取值来源于ADD SMF SERVSCOPE GRP命令中的参数"服务范围组标识（SERVSCOPEGRPID）"，必须通过ADD SMF SERVSCOPE GRP命令预先配置，否则本参数无法生效。如果本命令的参数“服务范围扩展策略（SERVSCOPEEXTPLY）”配置为“不扩展（NotSupServScopeExtPl）”，在用户没有配置本参数的情况下，则默认使用SET AMFLOCALOFFICECFG命令中的默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。NRF对于“服务范围”按照“包含”逻辑进行处理，即SMF能为发现请求中携带的所有服务范围提供服务，NRF才会认为其满足条件；所以如果参数“服务范围扩展策略（SERVSCOPEEXTPLY）”配置为“不扩展（NotSupServScopeExtPl）”，本参数在输入时，应避免输入无效的服务范围组标识。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。修改影响：无。数据来源：本端规划。默认值：不扩展（NotSupServScopeExtPly）配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。




命令举例 


`
MCC是460，MNC是11，DNN是"zte.com.cn"的NRF发现A-SMF参数配置，不携带跟踪区标识，不携带preferred-locality，支持携带prefer-Tai，不支持基于Locality优选，不支持携带servingScope，设置服务区范围组标识为0，设置服务范围扩展策略为不扩展。
SET PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn",CARRYPRELOCALITY="NOTCARRY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYPREFERREDTAI="SupPreferredTai",CARRYTA="NotSupTai",CARRYSERVINGSCOPE="NotSupCarryServingScope",SERVSCOPEGRPID=0,SERVSCOPEEXTPLY="NotSupServScopeExtPly"
` 


#### 删除基于PLMN的NRF发现A-SMF参数配置(DEL PLMN NRFDISCSMFPARA) 
#### 删除基于PLMN的NRF发现A-SMF参数配置(DEL PLMN NRFDISCSMFPARA) 


功能说明 

该命令用于删除一组AMF基于PLMN和DNN两个维度通过NRF发现A-SMF的参数配置。 


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于用户的DNN来通过NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。




命令举例 


`
删除MCC是460，MNC是11，DNN是"zte.com.cn"的NRF发现A-SMF参数配置
DEL PLMN NRFDISCSMFPARA:MCC="460",MNC="11",DNN="zte.com.cn"
` 


#### 查询基于PLMN的NRF发现A-SMF参数配置(SHOW PLMN NRFDISCSMFPARA) 
#### 查询基于PLMN的NRF发现A-SMF参数配置(SHOW PLMN NRFDISCSMFPARA) 


功能说明 

该命令用于查询AMF基于PLMN和DNN两个维度通过NRF发现A-SMF的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于用户的DNN来通过NRF发现SMF是否携带preferred-locality时，该参数必须填写。要求PLMN（MCC+MNC）和DNN至少有一个输入有效取值。当MCC+MNC配置为"FFF"+"FF"时，表示PLMN无效，当DNN配置为“NULL”时，表示DNN无效。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FF|参数作用：该参数用于配置AMF基于用户目前所在的PLMN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63默认值: NULL|参数作用：该参数用于配置AMF基于用户的DNN来通过NRF发现A-SMF时，AMF是否携带preferred-locality和servingScope的DNN，使用的DNN（Data Network Name，数据网名称） 为NI名称。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，是否支持在NRF的发现结果中，基于Locality来优选目标A-SMF（即AMF根据本地配置的A-SMF位置来选择A-SMF），取值及含义如下：不支持：AMF不支持根据本地配置的A-SMF位置来选择A-SMF。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标A-SMF，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取A-SMF的位置。
carrypreferredtai|携带Preferred跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupPreferredTai|参数作用：该参数用于设置AMF通过NRF发现A-SM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带Preferred-Tai，取值及含义如下：不携带：不携带“Preferred跟踪区标识”字段。携带：携带“Preferred跟踪区标识”字段，AMF发出的Nnrf_NFDiscovery请求中携带Preferred-Tai。
carryta|携带跟踪区标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupTai|参数作用：该参数用于设置AMF通过NRF发现H-SMF（home SMF）时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带TAI，取值及含义如下：不携带：不携带“跟踪区标识”字段。携带：携带“跟踪区标识”字段，AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带TAI字段。
carryservingscope|携带servingScope|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupCarryServingScope|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带servingScope，取值及含义如下：不携带：不携带“servingScope”字段。携带：携带“servingScope”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带servingScope字段。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 0-4096默认值: 0|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中所携带的servingScope group ID（服务范围组标识）。
servscopeextply|服务范围扩展策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupServScopeExtPly|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息是否支持servingScope Extension Policy（服务范围扩展策略）取值及含义如下：不扩展（NotSupServScopeExtPly）：优先使用本命令中配置的参数”服务范围组标识（SERVSCOPEGRPID）“对应的服务范围，如果参数”服务范围组标识（SERVSCOPEGRPID）未配置，则默认使用ADD SERVICEAREACODE命令中配置的参数”区域编码（AREACODE）作为SMF选择的“服务范围”。基于TA信息映射（SupServScopeExtPly）：使用ADD SMF SERVSCOPE TA GRP命令中基于TA映射的服务范围。




命令举例 


`
查询基于PLMN的NRF发现A-SMF参数配置。
SHOW PLMN NRFDISCSMFPARA

(No.3) : SHOW PLMN NRFDISCSMFPARA:
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 DNN         携带preferred-locality  支持基于Locality优选 携带跟踪区标识 携带Preferred跟踪区标识 携带servingScope 服务范围组标识 服务范围扩展策略 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 460        11         zte.com.cn  不携带                  不支持               不携带         携带                    不携带           0              不扩展           
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-04-22 11:35:20 耗时: 0.151 秒

` 


### 发现I/V-SMF参数配置 
### 发现I/V-SMF参数配置 


背景知识 


AMF需要通过NRF来发现I/V-SMF，并选择一个合适的I/V-SMF来为UE建立PDU会话。 




功能说明 


本功能用于控制AMF通过NRF发现I/V-SMF时，发送给NRF的发现消息中所携带的参数。  




子主题： 






#### 修改NRF发现I/V-SMF参数配置(SET NRFDISCIVSMFPARACFG) 
#### 修改NRF发现I/V-SMF参数配置(SET NRFDISCIVSMFPARACFG) 


功能说明 

该命令用于修改AMF通过NRF发现I/V-SMF的参数配置。 

当AMF需要发现I/V-SMF时，使用该命令配置AMF发送给NRF的发现请求消息中所携带的参数，NRF可根据这些参数作为参考因素来选择合适的I/V-SMF。包括如下参数：S-NSSAI、PLMN、NS-ID（Network Slice Instance，网络切片实例）、preferred-locality。  


注意事项 

本命令执行后，结果立即生效。 

具体参数的选择，要根据5GC网络中I/V-SMF的实际能力来设置，确保I/V-SMF向NRF注册NF Profile时，携带了这些信息。比如，通过此命令设置为携带S-NSSAI，则要确保目标切片网络中的I/V-SMF向NRF注册时已经携带了S-NSSAI信息，否则会导致AMF发现I/V-SMF失败，影响用户PDU会话的建立。 

如果已经通过[SET AMFSUPPOTSLICESELECT]命令设置了AMF支持网络切片选择功能，可以通过本命令配置AMF发现I/V-SMF是否携带切片实例号。

通过此命令配置AMF发现I/V-SMF携带preferred-locality参数，preferred-locality字段是否有效取决于AMF获取到的I/V-SMF位置信息是否有效，I/V-SMF位置信息来源如下： 


 
通过ADD PREFER LOCALITY命令配置的I/V-SMF位置。 

 
如果通过ADD PREFER LOCALITY命令无法获取到I/V-SMF位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”，则使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）”。 

 
通过此命令可以配置Locality优选策略： 

 

NRF优选：对应配置参数“携带preferred-locality”，NRF发现携带preferred-locality参数。
本地优选：对应配置参数“支持基于Locality优选”，NRF发现不携带preferred-locality参数， AMF基于Locality选择目标NF。
AMF执行Locality优选时，只能使用NRF优选和本地优选中的一种；在同时配置的情况下，以本地优选的优先级为高。
 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSnssai|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带S-NSSAI。修改影响：如果设置为支持，则AMF发出的Nnrf_NFDiscovery请求中携带S-NSSAI字段。为当前要建立的PDU所对应的S-NSSAI。数据来源：本端规划。默认值：SupSnssai配置原则：无。
carryPlmn|携带目标PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupPlmn|参数作用：该参数用于AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带目标PLMN。修改影响：如果设置为支持，则AMF发出的Nnrf_NFDiscovery请求中携带目标PLMN字段。数据来源：本端规划。默认值：NotSupPlmn配置原则：无。
carryNsiId|携带切片实例号|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupNsiId|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带NSI（Network Slice Instance，网络切片实例） ID。修改影响：如果设置为支持，则AMF发出的Nnrf_NFDiscovery请求中携带NSI ID字段。数据来源：本端规划。默认值：NotSupNsiId配置原则：无。
carryLocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupLocality|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。数据来源：本端规划。默认值：NotSupLocality配置原则：无。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF是否支持在NRF发现结果中基于Locality优选目标I/V-SMF。修改影响：如果设置为支持，则AMF支持基于本地配置的Locality优选目标SMF。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：同时配置支持supplocalitysel和carryprelocality字段时，以AMF执行Locality本地优选的优先级为高，SMF位置信息来源如下：通过使用SET AMFLOCALOFFICECFG命令参数“位置信息（locality）”配置SMF位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。




命令举例 


`
AMF向NRF发现I/V-SMF时，携带S-NSSAI、NSIID、PLMN,不支持携带preferred-locality参数，不支持基于Locality优选。
SET NRFDISCIVSMFPARACFG:CARRYSNSSAI="SupSnssai",CARRYPLMN="SupPlmn",CARRYNSIID="SupNsiId",CARRYLOCALITY="NotSupLocality",SUPPLOCALITYSEL="NOTSUPPORT""
` 


#### 查询NRF发现I/V-SMF参数配置(SHOW NRFDISCIVSMFPARACFG) 
#### 查询NRF发现I/V-SMF参数配置(SHOW NRFDISCIVSMFPARACFG) 


功能说明 

该命令用于查询AMF通过NRF发现I/V-SMF时，AMF发送给NRF的请求消息中所携带的参数，NRF可根据这些参数作为参考因数来选择合适的SMF。   


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSnssai|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带S-NSSAI。
carryPlmn|携带目标PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupPlmn|参数作用：该参数用于AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带目标PLMN。
carryNsiId|携带切片实例号|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupNsiId|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带NSI（Network Slice Instance，网络切片实例） ID。
carryLocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupLocality|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，是否支持基于Locality来优选目标I/V-SMF（即AMF优先选择特定位置的I/V-SMF进行业务交互）。




命令举例 


`
查询当前AMF发现I/V-SMF时所携带参数的配置。
SHOW NRFDISCIVSMFPARACFG

(No.1) : SHOW NRFDISCIVSMFPARACFG:
-----------------Namf_Communication_0----------------
操作维护       携带SNSSAI       携带目标PLMN    携带切片实例号       携带LOCALITY      支持基于Locality优选  
-----------------------------------------------------------------------------------------------------------------
修改              支持SNSSAI      支持PLMN            支持切片实例号       不携带                   不支持     
-----------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-03-15 17:53:57 耗时: 0.235 秒

` 


#### 新增基于PLMN的NRF发现I/V-SMF参数配置(ADD PLMN NRFDISCIVSMFPARA) 
#### 新增基于PLMN的NRF发现I/V-SMF参数配置(ADD PLMN NRFDISCIVSMFPARA) 


功能说明 

该命令用于新增一组AMF基于PLMN通过NRF发现I/V-SMF的参数配置。当AMF需要发现SMF以创建和管理PDU会话时，使用该命令，基于PLMN配置AMF发送给NRF的请求消息中所携带的参数。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF是否支持在NRF发现结果中基于Locality优选目标I/V-SMF。修改影响：如果设置为支持，则AMF支持基于本地配置的Locality优选目标SMF。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：同时配置支持supplocalitysel和carryprelocality字段时，以AMF执行Locality本地优选的优先级为高，SMF位置信息来源如下：通过使用SET AMFLOCALOFFICECFG命令参数“位置信息（locality）”配置SMF位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，是否支持基于Locality来优选目标I/V-SMF（即AMF优先选择特定位置的SMF进行业务交互）。




命令举例 


`
新增MCC是460，MNC是11的NRF发现I/V-SMF参数配置，支持携带preferred-locality，不支持基于Locality优选。
ADD PLMN NRFDISCIVSMFPARA:MCC="460",MNC="11",CARRYPRELOCALITY="CARRY",SUPPLOCALITYSEL="NOTSUPPORT"
` 


#### 修改基于PLMN的NRF发现I/V-SMF参数配置(SET PLMN NRFDISCIVSMFPARA) 
#### 修改基于PLMN的NRF发现I/V-SMF参数配置(SET PLMN NRFDISCIVSMFPARA) 


功能说明 

该命令用于修改一组AMF基于PLMN通过NRF发现I/V-SMF的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF是否支持在NRF发现结果中基于Locality优选目标I/V-SMF。修改影响：如果设置为支持，则AMF支持基于本地配置的Locality优选目标SMF。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：同时配置支持supplocalitysel和carryprelocality字段时，以AMF执行Locality本地优选的优先级为高，SMF位置信息来源如下：通过使用SET AMFLOCALOFFICECFG命令参数“位置信息（locality）”配置SMF位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，是否支持基于Locality来优选目标I/V-SMF（即AMF优先选择特定位置的SMF进行业务交互）。




命令举例 


`
修改MCC是460，MNC是11的NRF发现I/V-SMF参数配置，支持携带preferred-locality，不支持基于Locality优选。
SET PLMN NRFDISCIVSMFPARA:MCC="460",MNC="11",CARRYPRELOCALITY="CARRY",SUPPLOCALITYSEL="NOTSUPPORT"
` 


#### 删除基于PLMN的NRF发现I/V-SMF参数配置(DEL PLMN NRFDISCIVSMFPARA) 
#### 删除基于PLMN的NRF发现I/V-SMF参数配置(DEL PLMN NRFDISCIVSMFPARA) 


功能说明 

该命令用于删除一组AMF基于PLMN通过NRF发现I/V-SMF的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，是否支持基于Locality来优选目标I/V-SMF（即AMF优先选择特定位置的SMF进行业务交互）。




命令举例 


`
删除MCC是460，MNC是11的NRF发现I/V-SMF参数配置
DEL PLMN NRFDISCIVSMFPARA:MCC="460",MNC="11"
` 


#### 查询基于PLMN的NRF发现I/V-SMF参数配置(SHOW PLMN NRFDISCIVSMFPARA) 
#### 查询基于PLMN的NRF发现I/V-SMF参数配置(SHOW PLMN NRFDISCIVSMFPARA) 


功能说明 

该命令用于查询AMF基于PLMN通过NRF发现I/V-SMF的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现I/V-SMF是否携带preferred-locality和servingScope的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现I/V-SMF时，是否支持基于Locality来优选目标I/V-SMF（即AMF优先选择特定位置的SMF进行业务交互）。




命令举例 


`
查询基于PLMN的NRF发现I/V-SMF参数配置。
SHOW PLMN NRFDISCIVSMFPARA

(No.2) : SHOW PLMN NRFDISCIVSMFPARA:
-----------------Namf_Communication_0----------------
操作维护             移动国家码    移动网络码    携带preferred-locality      支持基于Locality优选 
---------------------------------------------------------------------------------------------------------
复制 修改 删除     460             11                 携带                              不支持               
---------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-02-18 16:56:57 耗时: 0.146 秒

` 


## 发现UDM参数配置 
## 发现UDM参数配置 


背景知识 


AMF需要通过NRF发现UDM实例信息，并选择一个合适的UDM来获取签约数据。 

AMF发现和选择UDM时，可参考以下因素，包括：SUPI、preferred-locality。 具体参见3GPP TS 23501协议“6.3.9 UDM discovery and selection”章节。 




功能说明 


本功能用于控制AMF通过NRF发现UDM时，发送给NRF的发现消息中所携带的参数。 

具体参数的选择，要根据网络中UDM的实际能力来设置，确保UDM向NRF注册NF Profile时携带了这些信息。比如，通过此命令设置发现时携带SUPI，则要确保UDM向NRF注册时已经携带了SUPI号段信息，否则会导致AMF发现UDM失败。 参考TS29510 第"6.1.6.2.7 Type: UdmInfo”章节中supiRanges字段。 




子主题： 






### 修改NRF发现UDM参数配置(SET NRFDISCUDMPARACFG) 
### 修改NRF发现UDM参数配置(SET NRFDISCUDMPARACFG) 


功能说明 

该命令用于修改AMF通过NRF发现UDM的参数配置。当AMF需要发现UDM以获取签约数据时，使用该命令。配置AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数，NRF根据这些参数来选择合适的UDM。包括是否携带如下参数：SUPI、preferred-locality、carryrt、carryhnwpubkeyid。 


注意事项 


 
该命令执行后，配置立即生效。 

 
具体参数的选择，根据网络中UDM的实际能力来设置，确保UDM向NRF注册NF Profile时携带了这些信息。比如，通过此命令设置发现时携带SUPI，则要确保UDM向NRF注册时已经携带了SUPI号段信息，否则会导致AMF发现UDM失败。 

 
通过此命令配置参数“携带preferred-locality（CARRYLOCALITY）”为“携带（SupLocality）”或者参数“支持基于Locality优选（SUPPLOCALITYSEL）”为“支持（SUPPORT）”时，可以使用ADD PREFER LOCALITY命令中配置的参数“优选位置（PRELOCALITY）”（即，指定Locality），也可以使用SET AMFLOCALOFFICECFG命令中配置的参数“位置信息（LOCALITY）”（即，AMF的Locality）。 

 
该命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carrySupi|携带SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSupi|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带SUPI，取值及含义如下：不支持SUPI：如果设置为不支持SUPI，则AMF发送给NRF的Nnrf_NFDiscovery请求消息中不会携带SUPI字段。支持SUPI：如果设置为支持，则AMF发送给NRF的Nnrf_NFDiscovery请求消息中会携带SUPI字段，NRF根据SUPI，会匹配到多个可用的UDM。修改影响：如果设置为不支持SUPI，同时也没有配置AMF发送给NRF的Nnrf_NFDiscovery请求消息中携带其他的发现参数，则可能导致NRF发现UDM失败。数据来源：本端规划。默认值：support SUPI。配置原则：无。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带preferred-locality字段。数据来源：本端规划。默认值：NOTCARRYPRELOCALITY。配置原则：preferred-locality字段是否有效取决于获取到的UDM位置信息是否有效。UDM位置信息来源如下：通过ADD PREFER LOCALITY命令配置的UDM位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到UDM位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据UDM的位置选择UDM的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取UDM的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。数据来源：本端规划。默认值：不携带。配置原则：无。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。数据来源：本端规划。默认值：不携带。配置原则：当"携带routing-indicator（carryRT）"配置为"携带"时，本参数才生效。




命令举例 


`
设置通过NRF发现UDM的时候，携带用户SUPI，不携带preferred-locality，不支持基于Locality优选。
SET NRFDISCUDMPARACFG:CARRYSUPI="SupSupi",CARRYPRELOCALITY="NOTCARRYPRELOCALITY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYRT="NOTCARRY",CARRYHNWPUBKEYID="NOTCARRY"
` 


### 查询NRF发现UDM参数配置(SHOW NRFDISCUDMPARACFG) 
### 查询NRF发现UDM参数配置(SHOW NRFDISCUDMPARACFG) 


功能说明 

该命令用于查询AMF通过NRF发现UDM时，AMF发送给NRF的请求消息中的参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carrySupi|携带SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSupi|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带SUPI，取值及含义如下：不支持SUPI支持SUPI：AMF发出的Nnrf_NFDiscovery请求中携带SUPI字段为当前用户的SUPI。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。




命令举例 


`
查看通过NRF发现UDM的时候，是否支持携带SUPI，是否携带preferred-locality。 
SHOW NRFDISCUDMPARACFG:

(No.6) : SHOW NRFDISCUDMPARACFG:
-----------------Namf_Communication_0---------------------------------------------------------------------------------------
操作维护       携带SUPI 携带preferred-locality       支持基于Locality优选    携带routing-indicator    携带home-pub-key-id策略
----------------------------------------------------------------------------------------------------------------------------
修改           支持SUPI 不携带preferred-locality       不支持                    不携带                 不携带
----------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-08 19:54:16 耗时: 0.13 秒

` 


### 新增基于PLMN的NRF发现UDM参数配置(ADD NRFDISCUDMPLMNPARACFG) 
### 新增基于PLMN的NRF发现UDM参数配置(ADD NRFDISCUDMPLMNPARACFG) 


功能说明 

该命令用于新增一组AMF基于PLMN通过NRF发现UDM的参数配置。当AMF需要发现UDM以获取签约数据时，使用该命令，基于PLMN配置AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数。 


注意事项 


 
该命令执行后，配置立即生效。 

 
具体参数的选择，根据网络中UDM的实际能力来设置，确保UDM向NRF注册NF Profile时携带了这些信息。比如，通过此命令设置发现时携带preferred-locality，则要确保UDM向NRF注册时已经携带了preferred-locality，否则会导致AMF发现UDM失败。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带preferred-locality字段。数据来源：本端规划。默认值：NOTCARRYPRELOCALITY。配置原则：preferred-locality字段是否有效取决于获取到的UDM位置信息是否有效。UDM位置信息来源如下：通过ADD PREFER LOCALITY命令配置的UDM位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到UDM位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据UDM的位置选择UDM的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取UDM的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator，取值及含义如下：不携带：不携带“routing-indicator”字段。携带：携带“routing-indicator”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。修改影响：无。数据来源：本端规划。默认值：不携带。配置原则：无。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。不携带：不携带home-pub-key-id策略。携带：携带home-pub-key-id策略，如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。修改影响：无数据来源：本端规划。默认值：不携带。配置原则：当SET NRFDISCAUSFPARACFG命令中的参数“携带参数方式（CARRYPARAMODE）”配置为“Routing Indicator优先”时，本参数才会生效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator，取值及含义如下：不携带：不携带“routing-indicator”字段。携带：携带“routing-indicator”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。不携带：不携带home-pub-key-id策略。携带：携带home-pub-key-id策略，如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。




命令举例 


`
该命令用于新增PLMN的NRF发现UDM参数配置。当AMF需要发现UDM时，可以基于PLMN配置AMF发送给NRF的Nnrf_NF Discovery请求消息中所携带的参数，不支持基于Locality优选，不携带routing-indicator，不携带home-pub-key-id。
ADD NRFDISCUDMPLMNPARACFG:MCC="460",MNC="11",CARRYPRELOCALITY="NOTCARRYPRELOCALITY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYRT="NOTCARRY",CARRYHNWPUBKEYID="NOTCARRY"
` 


### 修改基于PLMN的NRF发现UDM参数配置(SET NRFDISCUDMPLMNPARACFG) 
### 修改基于PLMN的NRF发现UDM参数配置(SET NRFDISCUDMPLMNPARACFG) 


功能说明 

该命令用于修改AMF基于PLMN通过NRF发现UDM的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。修改影响：如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求中会携带preferred-locality字段。数据来源：本端规划。默认值：NOTCARRYPRELOCALITY。配置原则：preferred-locality字段是否有效取决于获取到的UDM位置信息是否有效。UDM位置信息来源如下：通过ADD PREFER LOCALITY命令配置的UDM位置，即AMF配置的NF优选位置。如果通过ADD PREFER LOCALITY命令无法获取到UDM位置，且ADD PREFER LOCALITY命令中的参数“uselocloaclity”配置为“YES”，则使用与AMF相同的本地位置信息，即使用SET AMFLOCALOFFICECFG命令配置的参数“locality”。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。修改影响：无。数据来源：本端规划。默认值：NOTSUPPORT。配置原则：当本参数”支持基于Locality优选“和参数”携带servingScope“都同时配置为支持时（servingScope也是一种根据UDM的位置选择UDM的方式），此种情况下，AMF以Locality本地优选的优先级为高，此时AMF获取UDM的位置信息来源如下：通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置，且ADD PREFER LOCALITY命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator，取值及含义如下：不携带：不携带“routing-indicator”字段。携带：携带“routing-indicator”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。修改影响：无。数据来源：本端规划。默认值：不携带。配置原则：无。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。不携带：不携带home-pub-key-id策略。携带：携带home-pub-key-id策略，如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。修改影响：无数据来源：本端规划。默认值：不携带。配置原则：当SET NRFDISCAUSFPARACFG命令中的参数“携带参数方式（CARRYPARAMODE）”配置为“Routing Indicator优先”时，本参数才会生效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator，取值及含义如下：不携带：不携带“routing-indicator”字段。携带：携带“routing-indicator”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。不携带：不携带home-pub-key-id策略。携带：携带home-pub-key-id策略，如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。




命令举例 


`
该命令用于修改基于PLMN的NRF发现UDM参数配置。
SET NRFDISCUDMPLMNPARACFG:MCC="460",MNC="11",CARRYPRELOCALITY="NOTCARRYPRELOCALITY",SUPPLOCALITYSEL="NOTSUPPORT",CARRYRT="NOTCARRY",CARRYHNWPUBKEYID="NOTCARRY"
` 


### 删除基于PLMN的NRF发现UDM参数配置(DEL NRFDISCUDMPLMNPARACFG) 
### 删除基于PLMN的NRF发现UDM参数配置(DEL NRFDISCUDMPLMNPARACFG) 


功能说明 

该命令用于删除AMF基于PLMN通过NRF发现UDM的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator，取值及含义如下：不携带：不携带“routing-indicator”字段。携带：携带“routing-indicator”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。不携带：不携带home-pub-key-id策略。携带：携带home-pub-key-id策略，如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。




命令举例 


`
该命令用于删除基于PLMN的NRF发现UDM参数配置。
DEL NRFDISCUDMPLMNPARACFG:MCC="460",MNC="11"
` 


### 查询基于PLMN的NRF发现UDM参数配置(SHOW NRFDISCUDMPLMNPARACFG) 
### 查询基于PLMN的NRF发现UDM参数配置(SHOW NRFDISCUDMPLMNPARACFG) 


功能说明 

该命令用于查询AMF基于PLMN通过NRF发现UDM时，AMF发送给NRF的请求消息中的参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置基于PLMN的NRF发现UDM是否携带preferred-locality的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：当配置基于PLMN的NRF发现UDM是否携带preferred-locality时，该参数必须填写有效。
carryprelocality|携带preferred-locality|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYPRELOCALITY|参数作用：该参数用于设置AMF通过NRF发现UDM时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中是否携带preferred-locality，取值及含义如下：不携带：不携带“preferred-locality”字段。携带：携带“preferred-locality”字段，AMF发出的Nnrf_NFDiscovery请求中携带preferred-locality字段。
supplocalitysel|支持基于Locality优选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置AMF通过NRF发现UDM时，是否支持在NRF的发现结果中，基于Locality来优选目标UDM（即AMF根据本地配置的UDM位置来选择UDM），取值及含义如下：不支持：AMF不支持根据本地配置的UDM位置来选择UDM。支持：AMF支持基于本地配置的“位置信息（locality）”来优选目标UDM，即通过SET AMFLOCALOFFICECFG命令的参数“位置信息（locality）”获取UDM的位置。
carryrt|携带routing-indicator|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带routing-indicator，取值及含义如下：不携带：不携带“routing-indicator”字段。携带：携带“routing-indicator”字段，AMF发出的Nnrf_NFDiscovery请求消息中会携带routing-indicator字段。
carryhnwpubkeyid|携带home-pub-key-id策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTCARRY|参数作用：该参数用于设置AMF通过NRF发现UDM时，在AMF向NRF发送的Nnrf_NFDiscovery请求消息中，是否携带home-pub-key-id。不携带：不携带home-pub-key-id策略。携带：携带home-pub-key-id策略，如果设置为携带，则AMF发出的Nnrf_NFDiscovery请求消息中会携带home-pub-key-id字段。




命令举例 


`
该命令用于查询基于PLMN的NRF发现UDM参数配置。
SHOW NRFDISCUDMPLMNPARACFG:

(No.8) : SHOW NRFDISCUDMPLMNPARACFG:
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 携带preferred-locality       支持基于Locality优选      携带routing-indicator    携带home-pub-key-id策略
------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 460        11         不携带preferred-locality        不支持                   不携带                 不携带
------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-08 19:58:36 耗时: 0.202 秒

` 


## 发现AMF参数配置 
## 发现AMF参数配置 


背景知识 


AMF通过NRF发现其它AMF时，需要结合实际的业务场景来设置具体的发现请求参数，在N2接口的局间切换过程中，本功能用于源AMF通过NRF发现目标AMF的基本参数配置。 

N2接口是NR和AMF之间的接口，用于NR和AMF间的上下文管理、会话管理等消息的交互。 




功能说明 


本功能用于配置在N2接口的局间切换流程中，源AMF通过NRF发现目标AMF时，是否携带源AMF Region，源AMF Set及允许的SNSSAI。 




子主题： 






### 修改NRF发现AMF参数配置(SET NRFDISCAMFPARACFG) 
### 修改NRF发现AMF参数配置(SET NRFDISCAMFPARACFG) 


功能说明 

本功能用于配置在N2接口的局间切换流程中，原AMF通过NRF发现目标AMF时，是否携带原AMF Region，原AMF Set及允许的SNSSAI。 


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令需要根据网络中AMF的实际能力来设置，确保AMF向NRF注册NF Profile时，携带了特定的参数。比如：当AMF发现目标AMF时，带给NRF的消息中需要携带Region，则要确保目标AMF向NRF注册时，已经携带了Region信息，否则会导致AMF发现目标AMF失败。 

 
该命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carryRegion|携带Region|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupRegion|参数作用：该参数用于设置在局间切出流程中，AMF通过NRF发现目标AMF时，AMF是否携带源AMF Region。该参数仅适用于局间切出流程，取值及含义如下：不支持Region：不携带“Region”支持Region：携带“Region”修改影响：无。数据来源：本端规划。默认值：不支持Region。配置原则：如果配置为携带，需要以十六进制格式携带。
carrySet|携带Set|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupSet|参数作用：该参数仅用于设置在局间切出流程中，AMF通过NRF发现目标AMF时，AMF是否携带源AMF Set，取值及含义如下：不支持Set：不携带“Set”支持Set：携带“Set”修改影响：无。数据来源：本端规划。默认值：不支持Set。配置原则：如果配置为携带，需要以十六进制格式携带。
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSnssai|参数作用：该参数仅用于设置在局间切出流程中，AMF通过NRF发现目标AMF时，AMF是否携带源AMF允许的SNSSAI，取值及含义如下：不支持SNSSAI：不携带“SNSSAI”支持SNSSAI：携带“SNSSAI”修改影响：无。数据来源：本端规划。默认值：不支持SNSSAI。配置原则：无。




命令举例 


`
设置NRF发现AMF参数，携带原AMF Region，携带原AMF Set，携带允许的SNSSAI。
SET NRFDISCAMFPARACFG:CARRYREGION="SupRegion",CARRYSET="SupSet",CARRYSNSSAI="SupSnssai"
` 


### 查询NRF发现AMF参数配置(SHOW NRFDISCAMFPARACFG) 
### 查询NRF发现AMF参数配置(SHOW NRFDISCAMFPARACFG) 


功能说明 

本命令用于查询NRF发现AMF参数的策略配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carryRegion|携带Region|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupRegion|参数作用：该参数用于设置AMF是否携带源AMF Region。该参数仅用于局间切出流程，发现目标AMF时根据该参数配置决定是否携带源AMF Region,如果携带，以十六进制格式携带。
carrySet|携带Set|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupSet|参数作用：该参数用于设置AMF是否携带源AMF Set。该参数仅用于局间切出流程，发现目标AMF时根据该参数配置决定是否携带源AMF Set,如果携带，以十六进制格式携带。
carrySnssai|携带SNSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SupSnssai|参数作用：该参数用于设置AMF是否携带源AMF允许的SNSSAI。




命令举例 


`
查询NRF发现AMF参数的策略配置。
SHOW NRFDISCAMFPARACFG:

(No.1) : SHOW NRFDISCAMFPARACFG:
-----------------Namf_Communication_0----------------
携带Region   携带Set   携带SNSSAI
不支持Region 不支持Set 不支持SNSSAI
记录数：1
执行成功耗时: 0.155 秒

` 


## 发现SMSF参数配置 
## 发现SMSF参数配置 


背景知识 


AMF需要通过NRF来发现SMSF，并选择一个合适的SMSF来获取策略信息。 

AMF通过NRF发现和选择SMSF时，可参考以下因素，包括：SUPI、GPSI。 具体参见3GPP TS 23501协议“6.3.10 SMSF discovery and selection”章节。 




功能说明 


本功能用于控制AMF通过NRF发现SMSF时，发送给NRF的发现消息中所携带的参数。 

具体参数的选择，要根据SMSF的实际能力来设置，确保SMSF向NRF注册NF Profile时，携带了这些信息。比如，通过本功能设置发现时携带SUPI、GPSI，则要确保SMSF向NRF注册时已经携带了SUPI、GPSI信息，否则会导致AMF发现SMSF失败。 




子主题： 






### 修改NRF发现SMSF参数配置(SET NRFDISCSMSFPARACFG) 
### 修改NRF发现SMSF参数配置(SET NRFDISCSMSFPARACFG) 


功能说明 

该命令用于设置/修改AMF发现SMSF时，携带给NRF的参考因素，即AMF向NRF发送的Nnrf_NF Discovery请求消息中，所携带的查询条件。 包括是否携带如下参数：SUPI、GPSI。 

当SMSF支持向NRF注册号段范围，AMF需要实现根据终端号段选择SMSF时，需要配置此命令。 


注意事项 

具体参数的选择，要根据SMSF的实际能力来设置，确保SMSF向NRF注册NF Profile时，携带了这些信息。比如，通过本功能设置发现时携带SUPI、GPSI，则要确保SMSF向NRF注册时已经携带了SUPI、GPSI信息，否则会导致AMF发现SMSF失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
carrySupi|携带SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于设置AMF通过NRF发现SMSF时，AMF向NRF发送的Nnrf_NF Discovery请求消息，所携带的查询条件中，是否携带SUPI。如果设置为携带，则AMF发送给NRF的Nnrf_NF Discovery请求消息中会携带SUPI字段，为当前用户的SUPI。修改影响：本参数设置为开启之后，当AMF发现SMSF时，如果有有效的SMSFID且151号软参设置为开启，则在查询条件中携带SUPI，如果没有有效的SMSFID，则不判断软参直接携带SUPI。151号软参，是用于控制是否可以同时携带SMSFID和SUPI。151软参为开启状态 ，表示可以同时携带SMSFID和SUPI；151软参为关闭状态，表示只能携带SMSFID，不能携带SUPI。数据来源：本端规划默认值：0配置原则：无
carryGpsi|携带GPSI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于设置AMF发现SMSF时，AMF向NRF发送的Nnrf_NF Discovery请求消息，所携带的查询条件中，是否携带GPSI。如果设置为携带，则AMF发送给NRF的Nnrf_NF Discovery请求消息中会携带GPSI字段，为当前用户的GPSI。修改影响：本参数设置为开启之后，当AMF发现SMSF时，如果没有有效的SMSFID，则在查询条件中携带GPSI，如果有有效的SMSFID，则不携带GPSI。数据来源：本端规划默认值：0配置原则：无




命令举例 


`
设置通过NRF发现SMSF的时候，携带用户SUPI、GPSI。
SET NRFDISCSMSFPARACFG:CARRYSUPI="YES",CARRYGPSI="YES"
` 


### 查询NRF发现SMSF参数配置(SHOW NRFDISCSMSFPARACFG) 
### 查询NRF发现SMSF参数配置(SHOW NRFDISCSMSFPARACFG) 


功能说明 

该命令用于查询NRF发现SMSF参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
carrySupi|携带SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于设置AMF通过NRF发现SMSF时，AMF向NRF发送的Nnrf_NF Discovery请求消息，所携带的查询条件中，是否携带SUPI。如果设置为携带，则AMF发送给NRF的Nnrf_NF Discovery请求消息中会携带SUPI字段，为当前用户的SUPI。修改影响：本参数设置为开启之后，当AMF发现SMSF时，如果有有效的SMSFID且151号软参设置为开启，则在查询条件中携带SUPI，如果没有有效的SMSFID，则不判断软参直接携带SUPI。151号软参，是用于控制是否可以同时携带SMSFID和SUPI。151软参为开启状态 ，表示可以同时携带SMSFID和SUPI；151软参为关闭状态，表示只能携带SMSFID，不能携带SUPI。数据来源：本端规划默认值：0配置原则：无
carryGpsi|携带GPSI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于设置AMF发现SMSF时，AMF向NRF发送的Nnrf_NF Discovery请求消息，所携带的查询条件中，是否携带GPSI。如果设置为携带，则AMF发送给NRF的Nnrf_NF Discovery请求消息中会携带GPSI字段，为当前用户的GPSI。修改影响：本参数设置为开启之后，当AMF发现SMSF时，如果没有有效的SMSFID，则在查询条件中携带GPSI，如果有有效的SMSFID，则不携带GPSI。数据来源：本端规划默认值：0配置原则：无




命令举例 


`
查看通过NRF发现SMSF的时候，是否支持携带SUPI、GPSI。 
SHOW NRFDISCSMSFPARACFG:

(No.4) : SHOW NRFDISCSMSFPARACFG:
-----------------Namf_Communication_0----------------
携带SUPI 携带GPSI
携带        携带
记录数：1
执行成功耗时: 5.005 秒

` 


# NF本地解析配置 
# NF本地解析配置 


背景知识 


当5GC网络中没有部署NRF或者NRF不可用（升级或故障）以及进行拨测时，运营商希望通过AMF本地配置数据，来获取到各个NF的IP地址，后续用于发现和选择各个NF。因此AMF需要提供NF本地的IP地址解析配置数据。 




功能说明 


NF本地解析配置提供AUSF、UDM、PCF、SMF、SMSF和AMF的本地解析配置。 




子主题： 






## AUSF本地解析配置 
## AUSF本地解析配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取AUSF的解析数据，后续用于本地发现和选择AUSF。 




功能说明 


UE注册时，AMF发现和选择合适的AUSF进行鉴权。本地解析配置提供通过Routing码解析对应的AUSF。 




子主题： 






### 号段选择AUSF配置 
### 号段选择AUSF配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的AUSF进行功能测试，在AUSF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该AUSF进行功能测试。 

 
当网络中的某个AUSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该AUSF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发鉴权流程，AMF根据用户的GPSI/SUPI号码选择接入的AUSF。 

本配置提供基于号段选择AUSF的策略配置，包括：功能开关、有效时长以及基于号段选择AUSF的配置。 

基于号段选择AUSF功能通常应用于拨测场景，AMF在选择AUSF时，首先根据用户的GPSI/SUPI号段选择AUSF，在选择失败的情况下，后续再重新通过到NRF或本地服务发现AUSF。 




子主题： 






#### 基于号段选择AUSF策略 
#### 基于号段选择AUSF策略 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的AUSF进行功能测试，在AUSF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该AUSF进行功能测试。 

 
当网络中的某个AUSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该AUSF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发鉴权流程，AMF根据用户GPSI/SUPI号码选择接入的AUSF。 

本功能用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权。 




子主题： 






##### 修改基于号段选择AUSF策略(SET RESOLAUSFSEGPOLICY) 
##### 修改基于号段选择AUSF策略(SET RESOLAUSFSEGPOLICY) 


功能说明 

该命令用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supausfnumsel|支持基于号段选择AUSF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权。修改影响：修改参数为支持时，影响如下:AMF在选择AUSF时，首先根据用户的GPSI/SUPI号段选择AUSF，在选择失败的情况下，后续再重新通过到NRF或本地配置数据发现AUSF。数据来源：本端配置。配置原则：本参数需要根据运营商拨测场景进行配置。运维人员需要对新接入网络的AUSF进行功能测试，在AUSF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该AUSF进行功能测试。当网络中的某个AUSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该AUSF，进行测试。




命令举例 


`
设置支持基于号段选择AUSF的功能。
SET RESOLAUSFSEGPOLICY:SUPAUSFNUMSEL="SPRT"
` 


##### 查询基于号段选择AUSF策略(SHOW RESOLAUSFSEGPOLICY) 
##### 查询基于号段选择AUSF策略(SHOW RESOLAUSFSEGPOLICY) 


功能说明 

该命令用于查询AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
supausfnumsel|支持基于号段选择AUSF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权。




命令举例 


`
查询基于号段选择AUSF的策略。
SHOW RESOLAUSFSEGPOLICY

(No.1) : SHOW RESOLAUSFSEGPOLICY:
-----------------Namf_Communication_0----------------
操作维护       info   
----------------------
修改           不支持 
----------------------
记录数：1
执行成功开始时间:2021-07-09 12:13:14 耗时: 0.192 秒

` 


#### 基于号段选择AUSF配置 
#### 基于号段选择AUSF配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的AUSF进行功能测试，在AUSF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该AUSF进行功能测试。 

 
当网络中的某个AUSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该AUSF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发鉴权流程，AMF根据用户GPSI/SUPI号码选择拨测的AUSF网元。 

本配置提供基于GPSI/SUPI号段解析AUSF的配置数据以及其有效时长。 




子主题： 






##### 新增基于号段选择AUSF配置(ADD RESOLAUSFSEGCFG) 
##### 新增基于号段选择AUSF配置(ADD RESOLAUSFSEGCFG) 


功能说明 

该命令用于新增AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权的相关配置数据，使得拨测场景配置号段下的测试用户能够选择到指定的AUSF。 


注意事项 

如需要在基于号段选择AUSF配置中配置地址池标识，必须先通过[ADD AUSFLOCALADDRPOOL]命令配置AUSF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置AUSF Profile网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置AUSF Profile对应的域名，即AUSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置AUSF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD AUSFLOCALADDRPOOL命令配置AUSF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置AUSF Profile对应的优先级。修改影响：当根据号段匹配到多个AUSF Profile时，根据优先级高低选择其中的一个AUSF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置AUSF Profile对应的权重。修改影响：当根据号段匹配到多个AUSF Profile并且各个AUSF Profile的优先级相同时，根据权重选择其中的一个AUSF Profile。优先选择权重最大的AUSF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置AUSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置AUSF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配AUSF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析没有有效截止日期。




命令举例 


`
新增SUPI号码类型、用户号码为460111234567890的拨测用户的AUSF配置数据：FQDN为zte.com，配置地址池标识为1，优先级为0，权重为200，URI scheme为HTTP，API版本为V1，不指定有效时间。
ADD RESOLAUSFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",FQDN="zte.com",IPPOOLID=1,PRIORITY=0,WEIGHT=200,SCHEME="HTTP",APIVERSION="V1"
` 


##### 修改基于号段选择AUSF配置(SET RESOLAUSFSEGCFG) 
##### 修改基于号段选择AUSF配置(SET RESOLAUSFSEGCFG) 


功能说明 

该命令用于修改AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权的相关配置数据，使得拨测场景配置号段下的测试用户能够选择到指定的AUSF。 


注意事项 

如需要修改基于号段选择AUSF配置中的地址池标识，必须先通过[ADD AUSFLOCALADDRPOOL]命令配置AUSF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置AUSF Profile网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置AUSF Profile对应的域名，即AUSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置AUSF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD AUSFLOCALADDRPOOL命令配置AUSF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置AUSF Profile对应的优先级。修改影响：当根据号段匹配到多个AUSF Profile时，根据优先级高低选择其中的一个AUSF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置AUSF Profile对应的权重。修改影响：当根据号段匹配到多个AUSF Profile并且各个AUSF Profile的优先级相同时，根据权重选择其中的一个AUSF Profile。优先选择权重最大的AUSF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置AUSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置AUSF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配AUSF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析没有有效截止日期。




命令举例 


`
修改SUPI号码类型、用户号码为460111234567890的拨测用户的AUSF配置数据：FQDN为zte.com，地址池标识修改为1。
SET RESOLAUSFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",FQDN="zte.com",IPPOOLID=1
` 


##### 删除基于号段选择AUSF配置(DEL RESOLAUSFSEGCFG) 
##### 删除基于号段选择AUSF配置(DEL RESOLAUSFSEGCFG) 


功能说明 

该命令用于删除AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权的相关配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置AUSF Profile对应的域名，即AUSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。




命令举例 


`
删除SUPI号码类型、用户号码为460111234567890的拨测用户的所有AUSF配置数据。
DEL RESOLAUSFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"
` 


##### 查询基于号段选择AUSF配置(SHOW RESOLAUSFSEGCFG) 
##### 查询基于号段选择AUSF配置(SHOW RESOLAUSFSEGCFG) 


功能说明 

该命令用于查询AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个AUSF进行鉴权的相关配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLAUSFSEGPOLICY命令开启AMF支持基于号段选择AUSF后，AMF在选择AUSF时，会先根据配置的号段选择AUSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置AUSF Profile网元的标识符，依据网络规划配置。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置AUSF Profile对应的域名，即AUSF的域名。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置AUSF Profile对应的地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置AUSF Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置AUSF Profile对应的权重。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置AUSF Profile对应的URI scheme。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置AUSF Profile对应的API版本。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。




命令举例 


`
查询SUPI号码类型、用户号码为460111234567890的拨测用户的所有AUSF配置数据。
SHOW RESOLAUSFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"

(No.1) : SHOW RESOLAUSFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"
-----------------Namf_Communication_0----------------
操作维护            用户号码        号码类型   NF实例标识                                FQDN       地址池标识   优先级    权重   URI scheme    API版本   有效时间 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除    460111234567890   SUPI      2b3d8182-365c-44ff-a051-ef56f89732d5      zte.com    1            0        200    HTTP          V1版本           
---------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-22 14:03:31 耗时: 0.151 秒

` 


### AUSF地址池配置 
### AUSF地址池配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取AUSF的IP地址，后续用于本地发现和选择AUSF。 




功能说明 


一个AUSF会关联多个IP地址，为了提高配置效率，AMF根据“AUSF地址池配置”把地址列表和地址池标识关联，“基于号段选择AUSF配置”中只需要引用相应的地址池标识。 




子主题： 






#### 增加AUSF地址池配置(ADD AUSFLOCALADDRPOOL) 
#### 增加AUSF地址池配置(ADD AUSFLOCALADDRPOOL) 


功能说明 

该命令用于增加一条AUSF地址池配置。一个地址池ID可以对应多个地址。 


注意事项 


 
一个IP地址只能归属一个地址池标识。 

 
一个地址池内最多配置16个IP地址。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AUSF地址池配置的地址池标识。当地址池标识被基于号段选择AUSF配置引用时引用时，不能被删除。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于地址池标识对应的AUSF网元或AUSF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AUSF网元或AUSF服务通信IP地址对应的端口号。




命令举例 


`
增加地址池标识符为1，AUSF的IP地址为“12.12.12.12”，端口号为8080的AUSF地址池配置。
ADD AUSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",PORT=8080
` 


#### 删除AUSF地址池配置(DEL AUSFLOCALADDRPOOL) 
#### 删除AUSF地址池配置(DEL AUSFLOCALADDRPOOL) 


功能说明 

该命令用于删除一条AUSF地址池配置。 


注意事项 

当地址池标识被基于号段选择AUSF配置引用时，不能被删除。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AUSF地址池配置的地址池标识。当地址池标识被基于号段选择AUSF配置引用时引用时，不能被删除。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于地址池标识对应的AUSF网元或AUSF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AUSF网元或AUSF服务通信IP地址对应的端口号。




命令举例 


`
删除地址池标识符为1，AUSF的IP地址为“12.12.12.12”，端口号为8080的AUSF地址池配置。
DEL AUSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",PORT=8080
` 


#### 查询AUSF地址池配置(SHOW AUSFLOCALADDRPOOL) 
#### 查询AUSF地址池配置(SHOW AUSFLOCALADDRPOOL) 


功能说明 

该命令用于查询AUSF地址池配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AUSF地址池配置的地址池标识。当地址池标识被基于号段选择AUSF配置引用时引用时，不能被删除。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于地址池标识对应的AUSF网元或AUSF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AUSF网元或AUSF服务通信IP地址对应的端口号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AUSF地址池配置的地址池标识。当地址池标识被基于号段选择AUSF配置引用时引用时，不能被删除。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于地址池标识对应的AUSF网元或AUSF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AUSF网元或AUSF服务通信IP地址对应的端口号。




命令举例 


`
删除地址池标识符为1的AUSF地址池配置。
SHOW AUSFLOCALADDRPOOL:ADDRPOOLID=1

(No.1) : SHOW AUSFLOCALADDRPOOL:ADDRPOOLID=1
-----------------Namf_Communication_0----------------
地址池标识   IP地址         端口号
1           12.12.12.12    8080        

` 


## UDM本地解析配置 
## UDM本地解析配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取UDM的解析数据，后续用于本地发现和选择UDM。 




功能说明 


UE在注册时，完成到UDM的登记，AMF发现和选择合适的UDM。UDM本地解析配置提供通过SUPI号段解析对应的UDM。 




子主题： 






### 号段选择UDM配置 
### 号段选择UDM配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM进行处理，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的UDM进行功能测试，在UDM还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该UDM进行功能测试。 

 
当网络中的某个UDM可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该UDM，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发选择UDM流程，AMF根据用户的GPSI/SUPI号码选择接入的UDM。 

本配置提供基于号段选择UDM的策略配置，包括：功能开关、有效时长以及基于号段选择UDM的配置。 

基于号段选择UDM功能通常应用于拨测场景，AMF在选择UDM时，首先根据用户的GPSI/SUPI号段选择UDM，在选择失败的情况下，后续再重新通过到NRF或本地服务发现UDM。 




子主题： 






#### 基于号段选择UDM策略 
#### 基于号段选择UDM策略 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM进行处理，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的UDM进行功能测试，在UDM还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该UDM进行功能测试。 

 
当网络中的某个UDM可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该UDM，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发UDM选择流程，AMF根据用户GPSI/SUPI号码选择接入的UDM。 

本功能用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM进行处理。 




子主题： 






##### 修改基于号段选择UDM策略(SET RESOLUDMSEGPOLICY) 
##### 修改基于号段选择UDM策略(SET RESOLUDMSEGPOLICY) 


功能说明 

该命令用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supudmnumsel|支持基于号段选择UDM|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM。修改影响：修改参数为支持时，影响如下:AMF在选择UDM时，首先根据用户的GPSI/SUPI号段选择UDM，在选择失败的情况下，后续再重新通过到NRF或本地配置数据发现UDM。数据来源：本端配置。配置原则：本参数需要根据运营商拨测场景进行配置。运维人员需要对新接入网络的UDM进行功能测试，在UDM还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该UDM进行功能测试。当网络中的某个UDM可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该UDM，进行测试。




命令举例 


`
设置支持基于号段选择UDM的功能。
SET RESOLUDMSEGPOLICY:SUPUDMNUMSEL="SPRT"
` 


##### 查询基于号段选择UDM策略(SHOW RESOLUDMSEGPOLICY) 
##### 查询基于号段选择UDM策略(SHOW RESOLUDMSEGPOLICY) 


功能说明 

该命令用于查询AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
supudmnumsel|支持基于号段选择UDM|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM。




命令举例 


`
查询基于号段选择UDM的策略。
SHOW RESOLUDMSEGPOLICY

(No.1) : SHOW RESOLUDMSEGPOLICY
-----------------Namf_Communication_0----------------
操作维护  支持基于号段选择UDM
-------------------------------
修改      支持
-------------------------------
记录数：1
执行成功开始时间:2021-06-15 17:37:14 耗时: 0.137 秒

` 


#### 基于号段选择UDM配置 
#### 基于号段选择UDM配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM进行处理，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的UDM进行功能测试，在UDM还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该UDM进行功能测试。 

 
当网络中的某个UDM可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该UDM，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发UDM流程，AMF根据用户GPSI/SUPI号码选择拨测的UDM网元。 

本配置提供基于GPSI/SUPI号段解析UDM的配置数据以及其有效时长。 




子主题： 






##### 新增基于号段选择UDM配置(ADD RESOLUDMSEGCFG) 
##### 新增基于号段选择UDM配置(ADD RESOLUDMSEGCFG) 


功能说明 

该命令用于新增AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM，使得拨测场景配置号段下的测试用户能够选择到指定的UDM。 


注意事项 

如需要在基于号段选择UDM配置中配置地址池标识，必须先通过[ADD UDMLOCALADDRPOOL]命令配置UDM地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置UDM Profile网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置UDM Profile对应的域名，即UDM的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置UDM Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD UDMLOCALADDRPOOL命令配置UDM的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置UDM Profile对应的优先级。修改影响：当根据号段匹配到多个UDM Profile时，根据优先级高低选择其中的一个UDM，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置UDM Profile对应的权重。修改影响：当根据号段匹配到多个UDM Profile并且各个UDM Profile的优先级相同时，根据权重选择其中的一个UDM Profile。优先选择权重最大的UDM Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置UDM Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置UDM Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配UDM Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析没有有效截止日期。




命令举例 


`
新增SUPI号码类型、用户号码为460111234567890的拨测用户的UDM配置数据：FQDN为zte.com，配置地址池标识为1，优先级为0，权重为200，URI scheme为HTTP，API版本为V1，不指定有效时间。
ADD RESOLUDMSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",FQDN="zte.com",IPPOOLID=1,PRIORITY=0,WEIGHT=200,SCHEME="HTTP",APIVERSION="V1"
` 


##### 修改基于号段选择UDM配置(SET RESOLUDMSEGCFG) 
##### 修改基于号段选择UDM配置(SET RESOLUDMSEGCFG) 


功能说明 

该命令用于修改AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM，使得拨测场景配置号段下的测试用户能够选择到指定的UDM。 


注意事项 

如需要修改基于号段选择UDM配置中的地址池标识，必须先通过[ADD UDMLOCALADDRPOOL]命令配置UDM地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置UDM Profile网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置UDM Profile对应的域名，即UDM的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置UDM Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD UDMLOCALADDRPOOL命令配置UDM的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置UDM Profile对应的优先级。修改影响：当根据号段匹配到多个UDM Profile时，根据优先级高低选择其中的一个UDM，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置UDM Profile对应的权重。修改影响：当根据号段匹配到多个UDM Profile并且各个UDM Profile的优先级相同时，根据权重选择其中的一个UDM Profile。优先选择权重最大的UDM Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置UDM Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置UDM Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配UDM Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析没有有效截止日期。




命令举例 


`
修改SUPI号码类型、用户号码为460111234567890的拨测用户的UDM配置数据：FQDN为zte.com，地址池标识修改为1。
SET RESOLUDMSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",FQDN="zte.com",IPPOOLID=1
` 


##### 删除基于号段选择UDM配置(DEL RESOLUDMSEGCFG) 
##### 删除基于号段选择UDM配置(DEL RESOLUDMSEGCFG) 


功能说明 

该命令用于删除AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置UDM Profile对应的域名，即UDM的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。




命令举例 


`
删除SUPI号码类型、用户号码为460111234567890的拨测用户的所有UDM配置数据。
DEL RESOLUDMSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"
` 


##### 查询基于号段选择UDM配置(SHOW RESOLUDMSEGCFG) 
##### 查询基于号段选择UDM配置(SHOW RESOLUDMSEGCFG) 


功能说明 

该命令用于查询AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个UDM。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）； 初始注册流程时还未获取到GPSI，初始注册流程拨测应配置为SUPI类型。修改影响：通过SET RESOLUDMSEGPOLICY命令开启AMF支持基于号段选择UDM后，AMF在选择UDM时，会先先根据配置的号段选择UDM，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置UDM Profile网元的标识符，依据网络规划配置。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置UDM Profile对应的域名，即UDM的域名。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置UDM Profile对应的地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置UDM Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置UDM Profile对应的权重。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置UDM Profile对应的URI scheme。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置UDM Profile对应的API版本。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。




命令举例 


`
查询SUPI号码类型、用户号码为460111234567890的拨测用户的所有UDM配置数据。
SHOW RESOLUDMSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"

(No.1) : SHOW RESOLUDMSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"
-----------------Namf_Communication_0----------------
操作维护            用户号码          号码类型   NF实例标识                              FQDN       地址池标识   优先级    权重   URI scheme    API版本   有效时间 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除    460111234567890     SUPI      2b3d8182-365c-44ff-a051-ef56f89732d5    zte.com    1            0        200    HTTP          V1版本           
---------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-22 14:03:31 耗时: 0.151 秒

` 


### UDM地址池配置 
### UDM地址池配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取UDM的IP地址，后续用于本地发现和选择UDM。 




功能说明 


一个UDM会关联多个IP地址，为了提高配置效率，AMF根据“UDM地址池配置”把地址列表和地址池标识关联，“基于号段选择UDM配置”中只需要引用相应的地址池标识。 




子主题： 






#### 增加UDM地址池配置(ADD UDMLOCALADDRPOOL) 
#### 增加UDM地址池配置(ADD UDMLOCALADDRPOOL) 


功能说明 

该命令用于增加一条UDM地址池配置。在现网需要基于终端用户的GPSI/SUPI号段来选择接入的UDM(拨测)的场景下，通过本命令设置UDM的IP地址及端口号。 


注意事项 

1、一个IP地址只能归属一个地址池标识
2、一个地址池内最多配置16个IP地址


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置UDM地址池的标识。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于配置地址池标识对应的UDM IP地址。IP地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的UDM的端口号。




命令举例 


`
增加地址池标识符为1，UDM的IP地址为“12.12.12.12”，端口号为8080的UDM地址池配置。
ADD UDMLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",Port=8080
` 


#### 删除UDM地址池配置(DEL UDMLOCALADDRPOOL) 
#### 删除UDM地址池配置(DEL UDMLOCALADDRPOOL) 


功能说明 

该命令用于删除一条UDM地址池配置。 


注意事项 

当地址池标识被基于号段选择UDM配置引用时，不能被删除。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置UDM地址池的标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置地址池标识对应的UDM IP地址。IP地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的UDM的端口号。




命令举例 


`
删除地址池标识符为1，UDM的IP地址为“12.12.12.12”，端口号为8080的UDM地址池配置。
DEL UDMLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",Port=8080
` 


#### 查询UDM地址池配置(SHOW UDMLOCALADDRPOOL) 
#### 查询UDM地址池配置(SHOW UDMLOCALADDRPOOL) 


功能说明 

该命令用于查询UDM地址池配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置UDM地址池的标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置地址池标识对应的UDM IP地址。IP地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的UDM的端口号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置UDM地址池的标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置地址池标识对应的UDM IP地址。IP地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的UDM的端口号。




命令举例 


`
查询地址池标识符为1的UDM地址池配置。
SHOW UDMLOCALADDRPOOL:ADDRPOOLID=1

(No.1) : SHOW UDMLOCALADDRPOOL:
-----------------Namf_Communication_0----------------
地址池标识   IP地址         端口号
1         12.12.12.12      8080        
记录数：1
执行成功耗时: 0.12 秒

` 


## PCF本地解析配置 
## PCF本地解析配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取PCF的解析数据，后续用于本地发现和选择PCF。 




功能说明 


UE在注册时，AMF为UE进行策略关联的建立，发现和选择合适的PCF。PCF本地解析配置提供通过SUPI号段配置解析对应的PCF。 




子主题： 






### 号段选择PCF配置 
### 号段选择PCF配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的PCF进行功能测试，在PCF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该PCF进行功能测试。 

 
当网络中的某个PCF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该PCF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发PCF流程，AMF根据用户的GPSI/SUPI号码选择接入的PCF。 

本配置提供基于号段选择PCF的策略配置，包括：功能开关、有效时长以及基于号段选择PCF的配置。 

基于号段选择PCF功能通常应用于拨测场景，AMF在选择PCF时，首先根据用户的GPSI/SUPI号段选择PCF，在选择失败的情况下，后续再重新通过到NRF或本地服务发现PCF。 




子主题： 






#### 基于号段选择PCF策略 
#### 基于号段选择PCF策略 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的PCF进行功能测试，在PCF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该PCF进行功能测试。 

 
当网络中的某个PCF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该PCF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发PCF流程，AMF根据用户GPSI/SUPI号码选择接入的PCF。 

本功能用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理。 




子主题： 






##### 修改基于号段选择PCF策略(SET RESOLPCFSEGPOLICY) 
##### 修改基于号段选择PCF策略(SET RESOLPCFSEGPOLICY) 


功能说明 

该命令用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
suppcfnumsel|支持基于号段选择PCF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理。修改影响：修改参数为支持时，影响如下:AMF在选择PCF时，首先根据用户的GPSI/SUPI号段选择PCF，在选择失败的情况下，后续再重新通过到NRF或本地配置数据发现PCF。数据来源：本端配置。配置原则：本参数需要根据运营商拨测场景进行配置。运维人员需要对新接入网络的PCF进行功能测试，在PCF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该PCF进行功能测试。当网络中的某个PCF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该PCF，进行测试。




命令举例 


`
设置支持基于号段选择PCF的功能。
SET RESOLPCFSEGPOLICY:SUPPCFNUMSEL="SPRT"
` 


##### 查询基于号段选择PCF策略(SHOW RESOLPCFSEGPOLICY) 
##### 查询基于号段选择PCF策略(SHOW RESOLPCFSEGPOLICY) 


功能说明 

该命令用于查询AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
suppcfnumsel|支持基于号段选择PCF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理。




命令举例 


`
查询基于号段选择PCF的策略。
SHOW RESOLPCFSEGPOLICY

(No.1) : SHOW RESOLPCFSEGPOLICY
-----------------Namf_Communication_0----------------
操作维护  支持基于号段选择PCF
-------------------------------
修改      支持
-------------------------------
记录数：1
执行成功开始时间:2021-06-15 17:37:14 耗时: 0.137 秒

` 


#### 基于号段选择PCF配置 
#### 基于号段选择PCF配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理，主要用于运营商拨测场景。 


 
运维人员需要对新接入网络的PCF进行功能测试，在PCF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该PCF进行功能测试。 

 
当网络中的某个PCF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该PCF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，触发PCF流程，AMF根据用户GPSI/SUPI号码选择拨测的PCF网元。 

本配置提供基于GPSI/SUPI号段解析PCF的配置数据以及其有效时长。 




子主题： 






##### 新增基于号段选择PCF配置(ADD RESOLPCFSEGCFG) 
##### 新增基于号段选择PCF配置(ADD RESOLPCFSEGCFG) 


功能说明 

该命令用于新增AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理的相关配置数据，使得拨测场景配置号段下的测试用户能够选择到指定的PCF。 


注意事项 

如需要在基于号段选择PCF配置中配置地址池标识，必须先通过[ADD PCFLOCALADDRPOOL]命令配置PCF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置PCF Profile网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PCF Profile对应的域名，即PCF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置PCF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD PCFLOCALADDRPOOL命令配置PCF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置PCF Profile对应的优先级。修改影响：当根据号段匹配到多个PCF Profile时，根据优先级高低选择其中的一个PCF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置PCF Profile对应的权重。修改影响：当根据号段匹配到多个PCF Profile并且各个PCF Profile的优先级相同时，根据权重选择其中的一个PCF Profile。优先选择权重最大的PCF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置PCF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置PCF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配PCF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析没有有效截止日期。




命令举例 


`
新增SUPI号码类型、用户号码为460111234567890的拨测用户的PCF配置数据：FQDN为zte.com，地址池标识为1，优先级为0，权重为200，URI scheme为HTTP，API版本为V1，不指定有效时间。
ADD RESOLPCFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",FQDN="zte.com",IPPOOLID=1,PRIORITY=0,WEIGHT=200,SCHEME="HTTP",APIVERSION="V1"
` 


##### 修改基于号段选择PCF配置(SET RESOLPCFSEGCFG) 
##### 修改基于号段选择PCF配置(SET RESOLPCFSEGCFG) 


功能说明 

该命令用于修改AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理的相关配置数据，使得拨测场景配置号段下的测试用户能够选择到指定的PCF。 


注意事项 

如需要修改基于号段选择PCF配置中的地址池标识，必须先通过[ADD PCFLOCALADDRPOOL]命令配置PCF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置PCF Profile网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PCF Profile对应的域名，即PCF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置PCF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD PCFLOCALADDRPOOL命令配置PCF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置PCF Profile对应的优先级。修改影响：当根据号段匹配到多个PCF Profile时，根据优先级高低选择其中的一个PCF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置PCF Profile对应的权重。修改影响：当根据号段匹配到多个PCF Profile并且各个PCF Profile的优先级相同时，根据权重选择其中的一个PCF Profile。优先选择权重最大的PCF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置PCF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置PCF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配PCF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析没有有效截止日期。




命令举例 


`
修改SUPI号码类型、用户号码为460111234567890的拨测用户的PCF配置数据：FQDN为zte.com，地址池标识修改为1。
SET RESOLPCFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI",FQDN="zte.com",IPPOOLID=1
` 


##### 删除基于号段选择PCF配置(DEL RESOLPCFSEGCFG) 
##### 删除基于号段选择PCF配置(DEL RESOLPCFSEGCFG) 


功能说明 

该命令用于删除AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理的相关配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PCF Profile对应的域名，即PCF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。




命令举例 


`
删除SUPI号码类型、用户号码为460111234567890的拨测用户的所有PCF配置数据。
DEL RESOLPCFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"
` 


##### 查询基于号段选择PCF配置(SHOW RESOLPCFSEGCFG) 
##### 查询基于号段选择PCF配置(SHOW RESOLPCFSEGCFG) 


功能说明 

该命令用于查询AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个PCF进行处理的相关配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET RESOLPCFSEGPOLICY命令开启AMF支持基于号段选择PCF后，AMF在选择PCF时，会先先根据配置的号段选择PCF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则SUPI号段的优先级高于GPSI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该命令用于设置GPSI/SUPI号码或号段。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2|参数作用：该命令用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置PCF Profile网元的标识符，依据网络规划配置。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PCF Profile对应的域名，即PCF的域名。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置PCF Profile对应的地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置PCF Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置PCF Profile对应的权重。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置PCF Profile对应的URI scheme。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置PCF Profile对应的API版本。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。




命令举例 


`
查询SUPI号码类型、用户号码为460111234567890的拨测用户的所有PCF配置数据。
SHOW RESOLPCFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"

(No.1) : SHOW RESOLPCFSEGCFG:NUMBER="460111234567890",NUMTYPE="SUPI"
-----------------Namf_Communication_0----------------
操作维护            用户号码          号码类型   NF实例标识                             FQDN       地址池标识   优先级    权重   URI scheme    API版本   有效时间 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除    460111234567890     SUPI      2b3d8182-365c-44ff-a051-ef56f89732d5   zte.com    1            0        200    HTTP          V1版本           
--------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-22 14:03:31 耗时: 0.151 秒

` 


### PCF地址池配置 
### PCF地址池配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取PCF的IP地址，后续用于本地发现和选择PCF。 




功能说明 


本配置用于设置"基于号段选择PCF配置"中引用的PCF地址池标识。 

一个PCF会关联多个IP地址及端口号，为了提高配置效率，AMF在“PCF地址池配置”中将IP地址及端口号与地址池标识进行关联，在“基于号段选择PCF配置”中只需要引用相应的地址池标识即可关联多个IP地址。 




子主题： 






#### 增加PCF地址池配置(ADD PCFLOCALADDRPOOL) 
#### 增加PCF地址池配置(ADD PCFLOCALADDRPOOL) 


功能说明 

该命令用于增加PCF地址池配置，该命令设置的地址池可以被"基于号段选择AUSF配置"[ADD RESOLPCFSEGCFG]引用。

该命令的配置结果可以通过[SHOW PCFLOCALADDRPOOL]命令进行查询。

一个用户号段会关联多个IP地址及端口号，为了提高配置效率，AMF在“PCF地址池配置”中将IP地址及端口号与地址池标识进行关联，在“基于号段选择AUSF配置”中只需要引用相应的地址池标识即可关联多个IP地址。 


注意事项 

一个IP地址只能归属一个地址池标识。 

一个地址池内最多配置16个IP地址。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置PCF地址池标识。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于配置与PCF地址池标识关联的PCF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置与PCF地址池标识关联的PCF的端口号。




命令举例 


`
增加PCF地址池配置，其中地址池标识为1，PCF的IP地址为“12.12.12.12”，端口号为8080。
ADD PCFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",Port=8080
` 


#### 删除PCF地址池配置(DEL PCFLOCALADDRPOOL) 
#### 删除PCF地址池配置(DEL PCFLOCALADDRPOOL) 


功能说明 

该命令用于删除一条PCF地址池配置。 

可以选择删除某个地址池中的特定地址，也可以选择删除整个地址池。 

该命令的配置结果可以通过[SHOW PCFLOCALADDRPOOL]命令进行查询。


注意事项 

当地址池标识被"基于号段选择AUSF配置"([ADD RESOLPCFSEGCFG])引用时，不能被删除。必须解除绑定关系后进行删除操作。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置PCF地址池标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置与PCF地址池标识关联的PCF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置与PCF地址池标识关联的PCF的端口号。




命令举例 


`
删除地址池标识为1，PCF的IP地址为“12.12.12.12”，端口号为8080的PCF地址池配置。
DEL PCFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",Port=8080
` 


#### 查询PCF地址池配置(SHOW PCFLOCALADDRPOOL) 
#### 查询PCF地址池配置(SHOW PCFLOCALADDRPOOL) 


功能说明 

该命令用于查询PCF地址池配置。可以查询特定配置，也可以查询所有配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置PCF地址池标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置与PCF地址池标识关联的PCF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置与PCF地址池标识关联的PCF的端口号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置PCF地址池标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置与PCF地址池标识关联的PCF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置与PCF地址池标识关联的PCF的端口号。




命令举例 


`
查询地址池标识为1的PCF地址池配置。
SHOW PCFLOCALADDRPOOL:ADDRPOOLID=1

(No.1) : SHOW PCFLOCALADDRPOOL:ADDRPOOLID=1
-----------------Namf_Communication_0----------------
地址池标识   IP地址     端口号
1         12.12.12.12      8080        
记录数：1

执行成功开始时间:2020-05-21 16:21:21 耗时: 0.241 秒

` 


## SMF本地解析配置 
## SMF本地解析配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取SMF的解析数据，后续用于本地发现和选择SMF。 




功能说明 


在5GC网络中，UE发起PDU会话建立，AMF发现和选择合适的SMF建立PDU会话。本功能用于配置AMF通过对号段进行解析，获取对应的SMF。 




子主题： 






### SMF 地址池配置 
### SMF 地址池配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置SMF解析数据，发现和选择SMF。 




功能说明 


一个SMF会关联多个IP地址，为了提高配置效率，AMF根据 "SMF地址池配置"把地址列表和地址池标识关联， 其它配置中只需要引用相应的地址池标识。 




子主题： 






#### 新增SMF IP POOL配置(ADD SMFIPPOOLCFG) 
#### 新增SMF IP POOL配置(ADD SMFIPPOOLCFG) 


功能说明 

当现网没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置SMF解析数据，发现和选择SMF。 

该命令用于新增SMF地址池配置。 


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令最多只能配置32768条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置IP地址池标识，一个标识最多对应16个地址。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：该参数配置后，会被ADD RESOLASMFCFG命令和ADD RESOLIVSMFCFG命令使用。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|参数作用：该参数用于设置IP地址池内的IP地址。一个地址池包括IP地址和端口号。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 0-65535默认值: 8080|参数作用：该参数用于设置IP地址池端口号。一个地址池包括IP地址和端口号。修改影响：无。数据来源：本端规划 。默认值：8080。配置原则：无。




命令举例 


`
新增一条SMF Profile配置。
ADD SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS="1.1.1.1",PORT=8080
` 


#### 删除SMF  IP POOL配置(DEL SMFIPPOOLCFG) 
#### 删除SMF  IP POOL配置(DEL SMFIPPOOLCFG) 


功能说明 

该命令用于删除SMF地址池配置。 


注意事项 

该命令执行后，配置立即生效。 

本命令执行之前，需要确认被删除的地址池标识（IPPOOLID），不在[SHOW RESOLASMFCFG]命令或[SHOW RESOLIVSMFCFG]的查询结果中，否则不能删除成功。

可以通过以下两种方式解决后，再执行本命令。 


 
通过SET RESOLASMFCFG命令或者SET RESOLIVSMFCFG命令修改地址池标识（IPPOOLID）。 

 
通过DEL RESOLASMFCFG命令或者DEL RESOLIVSMFCFG命令删除地址池标识（IPPOOLID）。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置IP地址池标识，一个标识最多对应16个地址。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：该参数配置后，会被ADD RESOLASMFCFG命令和ADD RESOLIVSMFCFG命令使用。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置IP地址池内的IP地址。一个地址池包括IP地址和端口号。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 8080|参数作用：该参数用于设置IP地址池端口号。一个地址池包括IP地址和端口号。修改影响：无。数据来源：本端规划 。默认值：8080。配置原则：无。




命令举例 


`
删除一个IP pool内所有记录
DEL SMFIPPOOLCFG:ADDRPOOLID=1
删除一个IP pool内一条记录
DEL SMFIPPOOLCFG:ADDRPOOLID=1,IPADDRESS=1.1.1.1,PORT=8080
` 


#### 查询SMF  IP POOL配置(SHOW SMFIPPOOLCFG) 
#### 查询SMF  IP POOL配置(SHOW SMFIPPOOLCFG) 


功能说明 

该命令用于查询SMF地址池配置。 

可以查询所有配置，也可以按ipaddr查询特定配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置IP地址池标识，一个标识最多对应16个地址。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：该参数配置后，会被ADD RESOLASMFCFG命令和ADD RESOLIVSMFCFG命令使用。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置IP地址池内的IP地址。一个地址池包括IP地址和端口号。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 8080|参数作用：该参数用于设置IP地址池端口号。一个地址池包括IP地址和端口号。修改影响：无。数据来源：本端规划 。默认值：8080。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置IP地址池标识，一个标识最多对应16个地址。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置IP地址池内的IP地址。一个地址池包括IP地址和端口号。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 8080|参数作用：该参数用于设置IP地址池端口号。一个地址池包括IP地址和端口号。




命令举例 


`
查询查询一个IP pool内所有记录。
SHOW SMFIPPOOLCFG:ADDRPOOLID=1

-----------------Namf_Communication_0----------------
ADDRPOOLID   IPADDRESS   PORT
1            1.1.1.1      8080  
记录数：1

执行成功耗时: 0.22 秒

` 


### 基于号段解析SMF配置 
### 基于号段解析SMF配置 


背景知识 


基于号段选择SMF，主要用于运营商拨测和割接等场景。 


 
拨测使用场景：1）运维人员需要测试新入网的SMF，SMF没有和NRF建立连接或还没有向NRF注册，现网不方便在DNS上加入这个测试数据的场景，AMF能够将测试卡号码指向该SMF进行拨测。2）运维人员怀疑某个SMF可能有问题或者故障，AMF能够将测试卡号码指向该SMF进行拨测。 

 
割接使用场景：运营商割接SMF时，将用户分块进行割接（如：先割接30万用户），割接时AMF使用号段+DNN或号段+TA等参数指定到割接的SMF。 

 

该功能的应用场景如下： 


 
终端发起PDU会话建立请求，AMF根据用户GPSI/SUPI号码选择拨测的A-SMF。 

 
终端发起PDU会话建立、局内或局间注册更新、业务请求、N2/Xn口切换以及4G到5G的互操作请求，AMF根据用户GPSI/SUPI号码选择拨测的I-SMF或V-SMF（漫游Home Routed方式的V-SMF）。 

 
终端发起PDU会话建立请求，AMF根据用户GPSI/SUPI号码+DNN等参数选择割接的A-SMF。 

 
终端发起PDU会话建立、局内或局间注册更新、业务请求、N2/Xn口切换以及4G到5G的互操作请求，AMF根据用户GPSI/SUPI号码+TA等参数选择割接的I-SMF或V-SMF。 

 




功能说明 


本配置提供基于号段解析SMF的全局策略和用户级策略配置，提供基于号段解析A-SMF、I-SMF和V-SMF的配置。 




子主题： 






#### 解析SMF策略配置 
#### 解析SMF策略配置 


背景知识 


基于号段选择SMF，主要用于运营商拨测和割接等场景。 


 
拨测使用场景：1）运维人员需要测试新入网的SMF，SMF没有和NRF建立连接或还没有向NRF注册，现网不方便在DNS上加入这个测试数据的场景，AMF能够将测试卡号码指向该SMF进行拨测。2）运维人员怀疑某个SMF可能有问题或者故障，AMF能够将测试卡号码指向该SMF进行拨测。 

 
割接使用场景：运营商割接SMF时，将用户分块进行割接（如：先割接30万用户），割接时AMF使用号段+DNN或号段+TA等参数指定到割接的SMF。 

 

该本配置提供基于号段解析SMF的全局策略。 




功能说明 


该命令用于设置支持基于号段选择A-SMF、I-SMF和V-SMF的功能开关，以及支持基于号段本地解析A-SMF、I-SMF和V-SMF地址、号段选择失败后是否重选A-SMF、I-SMF和V-SMF的默认配置。 




子主题： 






##### 修改解析SMF策略配置(SET RESOLVESMFPOLICY) 
##### 修改解析SMF策略配置(SET RESOLVESMFPOLICY) 


功能说明 

该命令用于设置解析SMF策略配置的默认配置。 

该命令的配置结果优先级低于[ADD RESOSMFPLYBASEDUSER]命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了“用户级解析SMF策略”。只要其中一个号码能够匹配成功，则使用“用户级解析SMF策略”。若均没有匹配成功，则使用“解析SMF策略”。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SUPASMFNUMSEL|支持基于号段选择A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段选择A-SMF，选项如下。支持：该开关开启，用户才能进入割接环境或拨测环境选择A-SMF。不支持：该开关关闭，用户不能进入割接环境或拨测环境。
SUPIVSMFNUMSEL|支持基于号段选择I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段选择I-SMF和V-SMF，选项如下。支持：该开关开启，用户才能进入割接环境或拨测环境选择I-SMF和V-SMF。不支持：该开关关闭，用户不能进入割接环境或拨测环境。
LOCALRESOLVEASMF|支持基于号段本地解析A-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段本地解析A-SMF地址，选项如下。不支持：用户进入割接环境。通过ADD RESOLASMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择A-SMF。若交集为空，则判断“号段选择失败后是否重选A-SMF”参数取值，若为支持，则会按照正常逻辑重选A-SMF，若为不支持，则不再进行A-SMF选择。支持：用户进入拨测环境。通过ADD RESOLASMFCFG命令的配置策略，获取A-SMF FQDN。
LOCALRESOLVEIVSMF|支持基于号段本地解析I-SMF和V-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段本地解析I-SMF和V-SMF地址，选项如下。不支持：用户进入割接环境。通过SHOW RESOLIVSMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择I-SMF和V-SMF。若交集为空，则判断“号段选择失败后是否重选I-SMF和V-SMF”参数取值，若为支持，则会按照正常逻辑重选I-SMF和V-SMF，若为不支持，则不再进行I-SMF和V-SMF选择。支持：用户进入拨测环境。通过SHOW RESOLIVSMFCFG命令的配置策略，获取I-SMF/V-SMF FQDN。
RSASMFANUMFAIL|号段选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|号段选择失败指的是“基于号段解析A-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。该参数用于设置号段选择失败后是否重选A-SMF。重选：按照正常流程选择A-SMF。不重选：不再进行A-SMF选择。
RSIVSMFANUMFAIL|号段选择失败后是否重选I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|号段选择失败指的是“基于号段解析I-SMF和V-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。该参数用于设置号段选择失败后是否重选I-SMF和V-SMF。重选：按照正常流程选择I-SMF和V-SMF。不重选：不再进行I-SMF和V-SMF选择。
forcenrfdisc|割接模式时是否强制向NRF发现SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|该参数用于设置割接模式时是否强制向NRF发现SMF，默认为否。否：先从SBIGW缓存中获取SMF，若缓存里没有，再向NRF发现。是：不从SBIGW缓存中获取SMF，直接向NRF发现。该参数适用于割接时未能及时从SBIGW缓存中获取到指定SMF的场景，开启该参数后，从NRF获取到指定SMF后应及时关闭，防止一直向NRF发现影响性能。




命令举例 


`
设置支持基于号段选择A-SMF，支持基于号段选择I-SMF和V-SMF，支持基于号段本地解析A-SMF地址，支持基于号段本地解析I-SMF和V-SMF地址，号段选择失败后是否重选A-SMF为“重选”，号段选择失败后是否重选I-SMF和V-SMF为“重选”，割接模式时是否强制向NRF发现SMF为“否”。 
SET RESOLVESMFPOLICY:SUPASMFNUMSEL="SPRT",SUPIVSMFNUMSEL="SPRT",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT",RSASMFANUMFAIL="RESELECT",RSIVSMFANUMFAIL="RESELECT",FORCENRFDISC="INVALID"
` 


##### 查询解析SMF策略配置(SHOW RESOLVESMFPOLICY) 
##### 查询解析SMF策略配置(SHOW RESOLVESMFPOLICY) 


功能说明 

该命令用于查询解析SMF策略配置的默认配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
SUPASMFNUMSEL|支持基于号段选择A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段选择A-SMF，选项如下。支持：该开关开启，用户才能进入割接环境或拨测环境选择A-SMF。不支持：该开关关闭，用户不能进入割接环境或拨测环境。
SUPIVSMFNUMSEL|支持基于号段选择I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段选择I-SMF和V-SMF，选项如下。支持：该开关开启，用户才能进入割接环境或拨测环境选择I-SMF和V-SMF。不支持：该开关关闭，用户不能进入割接环境或拨测环境。
LOCALRESOLVEASMF|支持基于号段本地解析A-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段本地解析A-SMF地址，选项如下。不支持：用户进入割接环境。通过ADD RESOLASMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择A-SMF。若交集为空，则判断“号段选择失败后是否重选A-SMF”参数取值，若为支持，则会按照正常逻辑重选A-SMF，若为不支持，则不再进行A-SMF选择。支持：用户进入拨测环境。通过ADD RESOLASMFCFG命令的配置策略，获取A-SMF FQDN。
LOCALRESOLVEIVSMF|支持基于号段本地解析I-SMF和V-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置是否支持基于号段本地解析I-SMF和V-SMF地址，选项如下。不支持：用户进入割接环境。通过SHOW RESOLIVSMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择I-SMF和V-SMF。若交集为空，则判断“号段选择失败后是否重选I-SMF和V-SMF”参数取值，若为支持，则会按照正常逻辑重选I-SMF和V-SMF，若为不支持，则不再进行I-SMF和V-SMF选择。支持：用户进入拨测环境。通过SHOW RESOLIVSMFCFG命令的配置策略，获取I-SMF/V-SMF FQDN。
RSASMFANUMFAIL|号段选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|号段选择失败指的是“基于号段解析A-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。该参数用于设置号段选择失败后是否重选A-SMF。重选：按照正常流程选择A-SMF。不重选：不再进行A-SMF选择。
RSIVSMFANUMFAIL|号段选择失败后是否重选I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|号段选择失败指的是“基于号段解析I-SMF和V-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。该参数用于设置号段选择失败后是否重选I-SMF和V-SMF。重选：按照正常流程选择I-SMF和V-SMF。不重选：不再进行I-SMF和V-SMF选择。
forcenrfdisc|割接模式时是否强制向NRF发现SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|该参数用于设置割接模式时是否强制向NRF发现SMF，默认为否。否：先从SBIGW缓存中获取SMF，若缓存里没有，再向NRF发现。是：不从SBIGW缓存中获取SMF，直接向NRF发现。该参数适用于割接时未能及时从SBIGW缓存中获取到指定SMF的场景，开启该参数后，从NRF获取到指定SMF后应及时关闭，防止一直向NRF发现影响性能。




命令举例 


`
查询解析SMF策略配置的默认配置。 
SHOW RESOLVESMFPOLICY

(No.1) : SHOW RESOLVESMFPOLICY:
-----------------Namf_Communication_0----------------
支持基于号段选择A-SMF 支持基于号段选择I-SMF和V-SMF 支持基于号段本地解析A-SMF地址 支持基于号段本地解析I-SMF和V-SMF地址 号段选择失败后是否重选A-SMF 号段选择失败后是否重选I-SMF和V-SMF 割接模式时是否强制向NRF发现SMF
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
不支持                不支持                       不支持                        不支持                               不重选                      不重选                             否
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-08-17 14:08:21 耗时: 0.138 秒

` 


#### 用户级解析SMF策略配置 
#### 用户级解析SMF策略配置 


背景知识 


基于号段选择SMF，主要用于运营商拨测和割接等场景。 


 
拨测使用场景：1）运维人员需要测试新入网的SMF，SMF没有和NRF建立连接或还没有向NRF注册，现网不方便在DNS上加入这个测试数据的场景，AMF能够将测试卡号码指向该SMF进行拨测。2）运维人员怀疑某个SMF可能有问题或者故障，AMF能够将测试卡号码指向该SMF进行拨测。 

 
割接使用场景：运营商割接SMF时，将用户分块进行割接（如：先割接30万用户），割接时AMF使用号段+DNN或号段+TA等参数指定到割接的SMF。 

 

该本配置提供基于号段解析SMF的用户级策略。 




功能说明 


该命令用于设置是否支持基于GPSI/SUPI号段本地解析A-SMF、I-SMF和V-SMF地址、号段选择失败后是否重选A-SMF、I-SMF和V-SMF。 




子主题： 






##### 增加用户级解析SMF策略配置(ADD RESOSMFPLYBASEDUSER) 
##### 增加用户级解析SMF策略配置(ADD RESOSMFPLYBASEDUSER) 


功能说明 

该命令增加用户级解析SMF策略配置，用于配置某一GPSI/SUPI号段是否支持基于GPSI/SUPI号段本地解析A-SMF、I-SMF和V-SMF地址、号段选择失败后是否重选A-SMF、I-SMF和V-SMF、割接模式时是否强制向NRF发现SMF。 

该命令的配置结果优先级高于[SET RESOLVESMFPOLICY]命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了"用户级解析SMF策略”。只要其中一个号码能够匹配成功，则使用"用户级解析SMF策略”。若均没有匹配成功，则使用"解析SMF策略”。

该命令配置完成后，可以通过[SHOW RESOSMFPLYBASEDUSER]命令查询配置结果。


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令最多只能配置4096条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。
LOCALRESOLVEASMF|支持基于号段本地解析A-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于号段，通过本地配置的数据解析获A-SMF地址，取值及含义如下：不支持：在割接场景下。通过ADD RESOLASMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择，从交集中选择A-SMF。若交集为空，则判断本命令的参数"号段选择失败后是否重选A-SMF”参数取值，若为支持，则会按照正常逻辑重选A-SMF，若为不支持，则不再进行A-SMF选择。支持：在拨测场景下。通过ADD RESOLASMFCFG命令的配置策略，获取A-SMF配置。修改影响：无。数据来源：本端规划。默认值：不支持，用户进入割接场景。配置原则：无。
LOCALRESOLVEIVSMF|支持基于号段本地解析I-SMF和V-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于号段本地解析I-SMF和V-SMF地址，取值及含义如下：不支持：用户进入割接场景。通过SHOW RESOLIVSMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则AMF按照优先级和权重选择I-SMF和V-SMF。若交集为空，则根据本命令的参数"号段选择失败后是否重选I-SMF和V-SMF（RSIVSMFANUMFAIL）”的值进行判断，若配置值为支持，则后续AMF会按照正常逻辑重选I-SMF和V-SMF，若配置值为不支持，则AMF不再进行I-SMF和V-SMF选择。支持：用户进入拨测场景。通过SHOW RESOLIVSMFCFG命令的配置策略，获取I-SMF/V-SMF 配置。修改影响：无。数据来源：本端规划。默认值：不支持：用户进入割接场景。配置原则：无。
RSASMFANUMFAIL|号段选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|参数作用：该参数用于设置根据号段选择A-SMF失败后，AMF是否重选A-SMF。号段选择失败指的是"基于号段解析A-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空，取值及含义如下：重选：AMF按照正常流程选择A-SMF。不重选：AMF不再进行A-SMF选择。修改影响：无。数据来源：本端规划。默认值：不重选。配置原则：无。
RSIVSMFANUMFAIL|号段选择失败后是否重选I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|参数作用：该参数用于设置号段选择失败后是否重选I-SMF和V-SMF。号段选择失败指的是"基于号段解析I-SMF和V-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。重选：按照正常流程选择I-SMF和V-SMF。不重选：不再进行I-SMF和V-SMF选择。修改影响：无。数据来源：本端规划。默认值：不重选：不再进行I-SMF和V-SMF选择。配置原则：无。
forcenrfdisc|割接模式时是否强制向NRF发现SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：该参数用于设置割接模式时是否强制向NRF发现SMF，默认为否。否：先从SBIGW缓存中获取SMF，缓存里没有，再向NRF发现。是：不从SBIGW缓存中获取SMF，直接向NRF发现。修改影响：开启该参数后，由于每次都强制向NRF发现，可能会导致性能变差。数据来源：本端规划。默认值：否，即不强制向NRF发现SMF。配置原则：该参数适用于割接时未能及时从SBIGW缓存中获取到指定SMF的场景，开启该参数后，从NRF获取到指定SMF后应及时关闭，防止一直向NRF发现影响性能。




命令举例 


`
增加号码类型为GPSI，号码为"13895122456”的用户群支持基于号段本地解析A-SMF地址，支持基于号段本地解析I-SMF和V-SMF地址，号段选择失败后是否重选A-SMF为"重选”，号段选择失败后是否重选I-SMF和V-SMF为"重选”，割接模式时是否强制向NRF发现SMF为“否”。 
ADD RESOSMFPLYBASEDUSER:NUMBER="13895122456",NUMTYPE="GPSI",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT",RSASMFANUMFAIL="RESELECT",RSIVSMFANUMFAIL="RESELECT",FORCENRFDISC="INVALID"
` 


##### 修改用户级解析SMF策略配置(SET RESOSMFPLYBASEDUSER) 
##### 修改用户级解析SMF策略配置(SET RESOSMFPLYBASEDUSER) 


功能说明 

该命令用于修改某一GPSI/SUPI号段是否支持本地解析A-SMF、I-SMF和V-SMF地址、号段选择失败后是否重选A-SMF、I-SMF和V-SMF、割接模式时是否强制向NRF发现SMF。 

该命令的配置结果优先级高于[SET RESOLVESMFPOLICY]命令的配置结果。判断逻辑如下：判断该用户的GPSI和SUPI号码是否配置了"用户级解析SMF策略”。只要其中一个号码能够匹配成功，则使用"用户级解析SMF策略”。若均没有匹配成功，则使用"解析SMF策略”。

该命令配置完成后，可以通过[SHOW RESOSMFPLYBASEDUSER]命令查询配置结果。


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。
LOCALRESOLVEASMF|支持基于号段本地解析A-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于号段，通过本地配置的数据解析获A-SMF地址，取值及含义如下：不支持：在割接场景下。通过ADD RESOLASMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择，从交集中选择A-SMF。若交集为空，则判断本命令的参数"号段选择失败后是否重选A-SMF”参数取值，若为支持，则会按照正常逻辑重选A-SMF，若为不支持，则不再进行A-SMF选择。支持：在拨测场景下。通过ADD RESOLASMFCFG命令的配置策略，获取A-SMF配置。修改影响：无。数据来源：本端规划。默认值：不支持，用户进入割接场景。配置原则：无。
LOCALRESOLVEIVSMF|支持基于号段本地解析I-SMF和V-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于号段本地解析I-SMF和V-SMF地址，取值及含义如下：不支持：用户进入割接场景。通过SHOW RESOLIVSMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则AMF按照优先级和权重选择I-SMF和V-SMF。若交集为空，则根据本命令的参数"号段选择失败后是否重选I-SMF和V-SMF（RSIVSMFANUMFAIL）”的值进行判断，若配置值为支持，则后续AMF会按照正常逻辑重选I-SMF和V-SMF，若配置值为不支持，则AMF不再进行I-SMF和V-SMF选择。支持：用户进入拨测场景。通过SHOW RESOLIVSMFCFG命令的配置策略，获取I-SMF/V-SMF 配置。修改影响：无。数据来源：本端规划。默认值：不支持：用户进入割接场景。配置原则：无。
RSASMFANUMFAIL|号段选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|参数作用：该参数用于设置根据号段选择A-SMF失败后，AMF是否重选A-SMF。号段选择失败指的是"基于号段解析A-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空，取值及含义如下：重选：AMF按照正常流程选择A-SMF。不重选：AMF不再进行A-SMF选择。修改影响：无。数据来源：本端规划。默认值：不重选。配置原则：无。
RSIVSMFANUMFAIL|号段选择失败后是否重选I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|参数作用：该参数用于设置号段选择失败后是否重选I-SMF和V-SMF。号段选择失败指的是"基于号段解析I-SMF和V-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。重选：按照正常流程选择I-SMF和V-SMF。不重选：不再进行I-SMF和V-SMF选择。修改影响：无。数据来源：本端规划。默认值：不重选：不再进行I-SMF和V-SMF选择。配置原则：无。
forcenrfdisc|割接模式时是否强制向NRF发现SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：该参数用于设置割接模式时是否强制向NRF发现SMF，默认为否。否：先从SBIGW缓存中获取SMF，缓存里没有，再向NRF发现。是：不从SBIGW缓存中获取SMF，直接向NRF发现。修改影响：开启该参数后，由于每次都强制向NRF发现，可能会导致性能变差。数据来源：本端规划。默认值：否，即不强制向NRF发现SMF。配置原则：该参数适用于割接时未能及时从SBIGW缓存中获取到指定SMF的场景，开启该参数后，从NRF获取到指定SMF后应及时关闭，防止一直向NRF发现影响性能。




命令举例 


`
修改号码类型为GPSI，号码为"13895122456”的用户群支持基于号段本地解析A-SMF地址，支持基于号段本地解析I-SMF和V-SMF地址，号段选择失败后是否重选A-SMF为"重选”，号段选择失败后是否重选I-SMF和V-SMF为"重选”，割接模式时是否强制向NRF发现SMF为“否”。 
SET RESOSMFPLYBASEDUSER:NUMBER="13895122456",NUMTYPE="GPSI",LOCALRESOLVEASMF="SPRT",LOCALRESOLVEIVSMF="SPRT",RSASMFANUMFAIL="RESELECT",RSIVSMFANUMFAIL="RESELECT",FORCENRFDISC="INVALID"
` 


##### 删除用户级解析SMF策略配置(DEL RESOSMFPLYBASEDUSER) 
##### 删除用户级解析SMF策略配置(DEL RESOSMFPLYBASEDUSER) 


功能说明 

该命令用于删除某一号段用户的解析SMF策略配置。 

该命令配置完成后，可以通过[SHOW RESOSMFPLYBASEDUSER]命令查询配置结果。


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。




命令举例 


`
删除号码类型为GPSI，号码为"13895122456”的用户级解析SMF策略配置。 
DEL RESOSMFPLYBASEDUSER:NUMBER="13895122456",NUMTYPE="GPSI"
` 


##### 查询用户级解析SMF策略配置(SHOW RESOSMFPLYBASEDUSER) 
##### 查询用户级解析SMF策略配置(SHOW RESOSMFPLYBASEDUSER) 


功能说明 

该命令用于查询用户级解析SMF策略配置，可以使某一号段，也可以全部配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划 。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）
LOCALRESOLVEASMF|支持基于号段本地解析A-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于号段，通过本地配置的数据解析获A-SMF地址，取值及含义如下：不支持：在割接场景下。通过ADD RESOLASMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则按照优先级和权重选择，从交集中选择A-SMF。若交集为空，则判断本命令的参数"号段选择失败后是否重选A-SMF”参数取值，若为支持，则会按照正常逻辑重选A-SMF，若为不支持，则不再进行A-SMF选择。支持：在拨测场景下。通过ADD RESOLASMFCFG命令的配置策略，获取A-SMF配置。
LOCALRESOLVEIVSMF|支持基于号段本地解析I-SMF和V-SMF地址|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于号段本地解析I-SMF和V-SMF地址，取值及含义如下：不支持：用户进入割接场景。通过SHOW RESOLIVSMFCFG命令的配置策略，将获取的SMF FQDN与正常发现的SMF FQDN取交集，若交集不为空，则AMF按照优先级和权重选择I-SMF和V-SMF。若交集为空，则根据本命令的参数"号段选择失败后是否重选I-SMF和V-SMF（RSIVSMFANUMFAIL）”的值进行判断，若配置值为支持，则后续AMF会按照正常逻辑重选I-SMF和V-SMF，若配置值为不支持，则AMF不再进行I-SMF和V-SMF选择。支持：用户进入拨测场景。通过SHOW RESOLIVSMFCFG命令的配置策略，获取I-SMF/V-SMF 配置。
RSASMFANUMFAIL|号段选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|参数作用：该参数用于设置根据号段选择A-SMF失败后，AMF是否重选A-SMF。号段选择失败指的是”基于号段解析A-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空，取值及含义如下：重选：AMF按照正常流程选择A-SMF。不重选：AMF不再进行A-SMF选择。
RSIVSMFANUMFAIL|号段选择失败后是否重选I-SMF和V-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORESELECT|参数作用：该参数用于设置号段选择失败后是否重选I-SMF和V-SMF。号段选择失败指的是"基于号段解析I-SMF和V-SMF配置”选择的SMF结果和正常选择的SMF结果中的FQDN取交集，结果为空。重选：按照正常流程选择I-SMF和V-SMF。不重选：不再进行I-SMF和V-SMF选择。
forcenrfdisc|割接模式时是否强制向NRF发现SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：该参数用于设置割接模式时是否强制向NRF发现SMF，默认为否。否：先从SBIGW缓存中获取SMF，缓存里没有，再向NRF发现。是：不从SBIGW缓存中获取SMF，直接向NRF发现。




命令举例 


`
查询全部用户级解析SMF策略配置。 
SHOW RESOSMFPLYBASEDUSER:

(No.1) : SHOW RESOSMFPLYBASEDUSER:
-----------------Namf_Communication_0_A----------------
用户号码     号码类型 支持基于号段本地解析A-SMF地址 支持基于号段本地解析I-SMF和V-SMF地址 号段选择失败后是否重选A-SMF 号段选择失败后是否重选I-SMF和V-SMF 割接模式时是否强制向NRF发现SMF
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
13895122456  GPSI     支持                          支持                                 重选                        重选                               是
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

执行成功开始时间:2020-05-25 15:02:51 耗时: 0.395 秒

` 


#### 基于号段解析A-SMF配置 
#### 基于号段解析A-SMF配置 


背景知识 


基于号段选择A-SMF，主要用于运营商拨测和割接场景。 


 
拨测使用场景：1）运维人员需要测试新入网的SMF，SMF没有和NRF建立连接或还没有向NRF注册，现网不方便在DNS上加入这个测试数据的场景，AMF能够将测试卡号码指向该SMF进行拨测。2）运维人员怀疑某个SMF可能有问题或者故障，AMF能够将测试卡号码指向该SMF进行拨测。 

 
割接使用场景：运营商割接SMF时，将用户分块进行割接（如：先割接30万用户），割接时AMF使用号段+DNN或号段+TA等参数指定到割接的SMF。 

 

该功能的应用场景如下： 


 
终端发起PDU会话建立请求，AMF根据用户GPSI/SUPI号码选择拨测的A-SMF。 

 
终端发起PDU会话建立请求，AMF根据用户GPSI/SUPI号码+DNN等参数选择割接的A-SMF。 

 




功能说明 


该命令用于设置基于GPSI/SUPI号段解析A-SMF的数据，包括SMF主机名、地址池标识、优先级、权重、URI scheme、API版本、PGW FQDN、有效期。 




子主题： 






##### 新增基于号段解析A-SMF配置(ADD RESOLASMFCFG) 
##### 新增基于号段解析A-SMF配置(ADD RESOLASMFCFG) 


功能说明 

该命令新增基于号段解析A-SMF配置，用于在割接或拨测场景，让某一部分测试用户选择到指定的A-SMF。该命令配置的数据包括GPSI/SUPI号段、NF实例标识、A-SMF主机名、地址池标识、优先级、权重、URI scheme、API版本、PGW FQDN、有效时间。 

该命令的配置结果可以通过[SHOW RESOLASMFCFG]命令进行查询。


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令最多只能配置4096条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
NUMBER|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|参数作用：该参数用于设置NF实例标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
host|A-SMF FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置A-SMF的FQDN。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
ipPoolId|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置A-SMF地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于ADD SMFIPPOOLCFG命令中的参数"地址池标识（ADDRPOOLID）"，必须通过ADD SMFIPPOOLCFG命令预先配置。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置A-SMF优先级，当AMF查询到多个SMF时，根据SMF的优先级选择其中的一个SMF，优先级数字越小，表示SMF的优先级越高。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置A-SMF的静态权重，当AMF查询到多个A-SMF，并且各个A-SMF的优先级相同时，AMF会根据权重值选择其中的一个A-SMF，AMF优先选择权重值大的A-SMF。修改影响：无。数据来源：本端规划。默认值：200。配置原则：无。
schemeapiVersion|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于配置A-SMF支持的URI scheme，取值及含义如下：http：支持HTTP协议https：支持HTTPS协议修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于配置A-SMF的API版本，取值及含义如下：V1版本V2版本修改影响：无。数据来源：本端规划。默认值：V1版本。配置原则：无。
pgwFqdn|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PGW FQDN，用于在4G和5G网络互操作时，AMF通过本地解析配置数据获取A-SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：只支持输入小写字母。
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组号段地址解析数据。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。本参数设置为空，表示号段解析无有效截止日期。




命令举例 


`
新增一条基于GPSI/SUPI号段解析A-SMF配置，其中，编号为1，用户号码为13895122456，号码类型为GPSI，NF实例标识为"f81d4fae-7dec-1111-a765-00a0c91e6789"，A-SMF FQDN为zte.com.cn，优先级为1，权重为10，URI scheme为HTTP，API版本为V1，PGW FQDN为zte123.com.cn，有效时间为2020-01-20 11:16:38。
ADD RESOLASMFCFG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",HOST="zte.com.cn",PRIORITY=1,WEIGHT=10,SCHEMEAPIVERSION="HTTP",APIVERSION="V1",PGWFQDN="zte123.com.cn",VALIDITYTIME="2020-01-20 11:16:38"
` 


##### 修改基于号段解析A-SMF配置(SET RESOLASMFCFG) 
##### 修改基于号段解析A-SMF配置(SET RESOLASMFCFG) 


功能说明 

该命令修改基于号段解析A-SMF配置，用于在割接场景，让某一部分测试用户选择到指定的A-SMF。 

该命令的配置结果可以通过[SHOW RESOLASMFCFG]命令进行查询。


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|参数作用：该参数用于设置NF实例标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
host|A-SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置A-SMF的FQDN。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
ipPoolId|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置A-SMF地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于ADD SMFIPPOOLCFG命令中的参数"地址池标识（ADDRPOOLID）"，必须通过ADD SMFIPPOOLCFG命令预先配置。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置A-SMF优先级，当AMF查询到多个SMF时，根据SMF的优先级选择其中的一个SMF，优先级数字越小，表示SMF的优先级越高。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置A-SMF的静态权重，当AMF查询到多个A-SMF，并且各个A-SMF的优先级相同时，AMF会根据权重值选择其中的一个A-SMF，AMF优先选择权重值大的A-SMF。修改影响：无。数据来源：本端规划。默认值：200。配置原则：无。
schemeapiVersion|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于配置A-SMF支持的URI scheme，取值及含义如下：http：支持HTTP协议https：支持HTTPS协议修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于配置A-SMF的API版本，取值及含义如下：V1版本V2版本修改影响：无。数据来源：本端规划。默认值：V1版本。配置原则：无。
pgwFqdn|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PGW FQDN，用于在4G和5G网络互操作时，AMF通过本地解析配置数据获取A-SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：只支持输入小写字母。
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组号段地址解析数据。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。本参数设置为空，表示号段解析无有效截止日期。




命令举例 


`
修改一条基于GPSI/SUPI号段解析A-SMF配置，其中，编号为1，修改用户号码为13895122456，号码类型为GPSI，NF实例标识为"f81d4fae-7dec-1111-a765-00a0c91e6789"，A-SMF FQDN为zte.com.cn，优先级为1，权重为10，URI scheme为HTTP，API版本为V1，PGW FQDN为zte123.com.cn，有效时间为2020-01-20 11:16:38。
SET RESOLASMFCFG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",HOST="zte.com.cn",PRIORITY=1,WEIGHT=10,SCHEMEAPIVERSION="HTTP",APIVERSION="V1",PGWFQDN="zte123.com.cn",VALIDITYTIME="2020-01-20 11:16:38"
` 


##### 删除基于号段解析A-SMF配置(DEL RESOLASMFCFG) 
##### 删除基于号段解析A-SMF配置(DEL RESOLASMFCFG) 


功能说明 

该命令删除基于GPSI/SUPI号段解析A-SMF的配置数据。 

该命令的配置结果可以通过[SHOW RESOLASMFCFG]命令进行查询。


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。




命令举例 


`
删除一条基于GPSI/SUPI号段解析A-SMF配置，其中编号为1。
DEL RESOLASMFCFG:ID=1
` 


##### 查询基于号段解析A-SMF配置(SHOW RESOLASMFCFG) 
##### 查询基于号段解析A-SMF配置(SHOW RESOLASMFCFG) 


功能说明 

该命令用于查询基于GPSI/SUPI号段解析A-SMF的配置数据。 

可以查询所有配置，也可以按号码段查询特定配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：无。数据来源：本端规划。默认值：GPSI（Generic Public Subscription Identifier，一般公共用户标识）配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置GPSI/SUPI号码或号段。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，取值及含义如下：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|参数作用：该参数用于设置NF实例标识。
host|A-SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置A-SMF的FQDN。
ipPoolId|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置A-SMF地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置A-SMF优先级，当AMF查询到多个SMF时，根据SMF的优先级选择其中的一个SMF，优先级数字越小，表示SMF的优先级越高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置A-SMF的静态权重，当AMF查询到多个A-SMF，并且各个A-SMF的优先级相同时，AMF会根据权重值选择其中的一个A-SMF，AMF优先选择权重值大的A-SMF。
schemeapiVersion|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于配置A-SMF支持的URI scheme，取值及含义如下：http：支持HTTP协议https：支持HTTPS协议
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于配置A-SMF的API版本，取值及含义如下：V1版本V2版本
pgwFqdn|PGW FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于配置PGW FQDN，用于在4G和5G网络互操作时，AMF通过本地解析配置数据获取A-SMF。
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期。




命令举例 


`
查询所有基于GPSI/SUPI号段解析A-SMF配置。
SHOW RESOLASMFCFG

(No.1) : SHOW RESOLASMFCFG:
-----------------Namf_Communication_0----------------
操作维护       编号 用户号码 号码类型 NF实例标识                           A-SMF FQDN 地址池标识 优先级 权重 URI scheme API版本 PGW FQDN      有效时间            
------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1    138523   GPSI     f81d4fae-7dec-1111-a765-00a0c91e6789 zte.com    1          1      200  HTTP       V1版本  zte123.com.cn 2021-08-26 00:00:00 
------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-12 12:23:38 耗时: 0.149 秒

` 


#### 基于号段解析I-SMF和V-SMF配置 
#### 基于号段解析I-SMF和V-SMF配置 


背景知识 


基于号段选择I-SMF和V-SMF，主要用于运营商拨测和割接场景。 


 
拨测使用场景：1）运维人员需要测试新入网的SMF，SMF没有和NRF建立连接或还没有向NRF注册，现网不方便在DNS上加入这个测试数据的场景，AMF能够将测试卡号码指向该SMF进行拨测。2）运维人员怀疑某个SMF可能有问题或者故障，AMF能够将测试卡号码指向该SMF进行拨测。 

 
割接使用场景：运营商割接SMF时，将用户分块进行割接（如：先割接30万用户），割接时AMF使用号段+DNN或号段+TA等参数指定到割接的SMF。 

 

该功能的应用场景如下： 


 
终端发起PDU会话建立、局内或局间注册更新、业务请求、N2/Xn口切换以及4G到5G的互操作请求，AMF根据用户GPSI/SUPI号码选择拨测的I-SMF或V-SMF（漫游Home Routed方式的V-SMF）。 

 
终端发起PDU会话建立、局内或局间注册更新、业务请求、N2/Xn口切换以及4G到5G的互操作请求，AMF根据用户GPSI/SUPI号码+TA等参数选择割接的I-SMF或V-SMF。 

 




功能说明 


该命令用于设置基于GPSI/SUPI号段解析I-SMF和V-SMF的数据，包括SMF主机名、地址池标识、优先级、权重、URI scheme、API版本、有效时间。 




子主题： 






##### 新增基于号段解析I-SMF和V-SMF配置(ADD RESOLIVSMFCFG) 
##### 新增基于号段解析I-SMF和V-SMF配置(ADD RESOLIVSMFCFG) 


功能说明 


该命令的配置结果可以通过[SHOW RESOLIVSMFCFG]命令进行查询。


注意事项 

如需要在基于GPSI/SUPI号段解析I-SMF和V-SMF配置中配置地址池，必须先配置SMF地址池。可以通过[SHOW SMFIPPOOLCFG]命令查询已配置的SMF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|该参数为每个配置赋予不同的编号，用于区分不同配置。
NUMBER|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 1-16|该参数用于设置GPSI/SUPI号码或号段。
NUMTYPE|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
host|SMF FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|该参数用于设置SMF的FQDN。
ipPoolId|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|SMF地址池标识，该参数必须已经存在，可以通过SHOW SMFIPPOOLCFG命令查询已配置的SMF地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|SMF优先级，用于当查询到多个SMF时，根据优先级高低选择其中的一个SMF，优先级数字越小，优先级越高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|静态权重，用于查询到多个SMF并且各个SMF实例的优先级相同时，根据权重选择其中的一个SMF。
schemeapiVersion|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置A-SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置A-SMF的API版本，比如v1或v2。
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长为空表示号段解析无有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组MME 号段地址解析。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：无。




命令举例 


`
新增基于号段解析I-SMF和V-SMF配置，其中号码类型为GPSI，号段为13895122456，NF实例标识为f81d4fae-7dec-1111-a765-00a0c91e6789，FQDN为zte.com.cn，优先级为1，权重为10，scheme为HTTP，API版本为v1，有效时间为2020-01-20 11:16:38。
ADD RESOLIVSMFCFG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",HOST="zte.com.cn",PRIORITY=1,WEIGHT=10,SCHEMEAPIVERSION="HTTP",APIVERSION="V1",VALIDITYTIME="2020-01-20 11:16:38"
` 


##### 修改基于号段解析I-SMF和V-SMF配置(SET RESOLIVSMFCFG) 
##### 修改基于号段解析I-SMF和V-SMF配置(SET RESOLIVSMFCFG) 


功能说明 

该命令修改基于GPSI/SUPI号段解析I-SMF和V-SMF配置，用于在者割接场景，让某一部分测试用户选择到指定的I-SMF或者V-SMF。 

该命令的配置结果可以通过[SHOW RESOLIVSMFCFG]命令进行查询。


注意事项 

如需要在基于GPSI/SUPI号段解析I-SMF和V-SMF配置中配置地址池，必须先配置SMF地址池。可以通过[SHOW SMFIPPOOLCFG]命令查询已配置的SMF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|该参数为每个配置赋予不同的编号，用于区分不同配置。
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|该参数用于设置GPSI/SUPI号码或号段。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
host|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于设置SMF的FQDN。
ipPoolId|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|SMF地址池标识，该参数必须已经存在，可以通过SHOW SMFIPPOOLCFG命令查询已配置的SMF地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|SMF优先级，用于当查询到多个SMF时，根据优先级高低选择其中的一个SMF，优先级数字越小，优先级越高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|静态权重，用于查询到多个SMF并且各个SMF实例的优先级相同时，根据权重选择其中的一个SMF。
schemeapiVersion|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置A-SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置A-SMF的API版本，比如v1或v2。
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长为空表示号段解析无有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组MME 号段地址解析。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：无。




命令举例 


`
修改基于号段解析I-SMF和V-SMF配置，其中号码类型为GPSI，号段为13895122456，FQDN为zte.com.cn，优先级为1，权重为10，scheme为HTTP，API版本为v1，有效时间为2020-01-20 11:16:38。
SET RESOLIVSMFCFG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",HOST="zte.com.cn",PRIORITY=1,WEIGHT=10,SCHEMEAPIVERSION="HTTP",APIVERSION="V1",VALIDITYTIME="2020-01-20 11:16:38" 
` 


##### 删除基于号段解析I-SMF和V-SMF配置(DEL RESOLIVSMFCFG) 
##### 删除基于号段解析I-SMF和V-SMF配置(DEL RESOLIVSMFCFG) 


功能说明 

该命令用于删除基于GPSI/SUPI号段解析I-SMF和V-SMF的配置数据。 

该命令的配置结果可以通过[SHOW RESOLIVSMFCFG]命令进行查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|该参数为每个配置赋予不同的编号，用于区分不同配置。




命令举例 


`
删除一条基于GPSI/SUPI号段解析I-SMF和V-SMF配置，ID为1。
DEL RESOLIVSMFCFG:ID=1
` 


##### 查询基于号段解析I-SMF和V-SMF配置(SHOW RESOLIVSMFCFG) 
##### 查询基于号段解析I-SMF和V-SMF配置(SHOW RESOLIVSMFCFG) 


功能说明 

该命令用于查询基于GPSI/SUPI号段解析I-SMF和V-SMF的配置数据。 

可以查询所有配置，也可以按号码段查询特定配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-4096|该参数为每个配置赋予不同的编号，用于区分不同配置。
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|该参数用于设置GPSI/SUPI号码或号段。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）




输出参数说明 


标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-4096|该参数为每个配置赋予不同的编号，用于区分不同配置。
NUMBER|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 1-16|该参数用于设置GPSI/SUPI号码或号段。
NUMTYPE|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
host|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于设置SMF的FQDN。
ipPoolId|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|SMF地址池标识，该参数必须已经存在，可以通过SHOW SMFIPPOOLCFG命令查询已配置的SMF地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|SMF优先级，用于当查询到多个SMF时，根据优先级高低选择其中的一个SMF，优先级数字越小，优先级越高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|静态权重，用于查询到多个SMF并且各个SMF实例的优先级相同时，根据权重选择其中的一个SMF。
schemeapiVersion|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置A-SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置A-SMF的API版本，比如v1或v2。
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长为空表示号段解析无有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组MME 号段地址解析。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：无。




命令举例 


`
查询所有基于GPSI/SUPI号段解析I-SMF和V-SMF配置。

(No.1) : SHOW RESOLIVSMFCFG:
-----------------Namf_Communication_0----------------
操作维护       编号 用户号码 号码类型 NF实例标识                           SMF FQDN 地址池标识 优先级 权重 URI scheme API版本 有效时间            
--------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1    13853    GPSI   f81d4fae-7dec-1111-a765-00a0c91e6789 zte.com  1          2      200  HTTP       V1版本  2021-08-25 00:00:00 
--------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-12 14:49:47 耗时: 0.156 秒

` 


## SMSF本地解析配置 
## SMSF本地解析配置 


背景知识 


当5GC网络中没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置的数据，来获取SMSF的IP地址，后续用于发现和选择SMSF。 




功能说明 


UE通过NAS消息投递短消息时，AMF发现和选择合适的SMSF进行短消息投递。 

本功能用于配置AMF通过对SUPI号段进行解析，获取对应的SMSF。 




子主题： 






### 默认SMSF配置 
### 默认SMSF配置 


背景知识 


5GC网络中的AMF与SMSF进行交互时，需要获取SMSF的IP地址以进行通信。 

AMF获取SMSF的IP地址的方式有以下两种。 


 
通过NRF发现SMSF的IP地址 

 
通过AMF本地配置的数据，解析获取SMSF的IP地址
此种方式是指，AMF可以配置一个和AMF通信的默认的SMSF，还可以通过对SUPI进行解析，来获取对应的SMSF的IP地址。
通常情况下，如果是测试场景，建议使用默认SMSF的IP地址。如果是商用局场景，建议使用通过对进行SUPI解析，获取的SMSF IP地址。 

 




功能说明 


本功能用于配置本AMF对应的默认SMSF。 

当本AMF通过对SUPI的解析，没有获取到SMSF时，会使用本功能配置的默认SMSF。 




子主题： 






#### 修改默认SMSF配置(SET DFTSMSF CONFIG) 
#### 修改默认SMSF配置(SET DFTSMSF CONFIG) 


功能说明 

本功能用于配置本AMF对应的默认SMSF的IP地址信息。 


注意事项 


 
本命令执行后，配置立即生效。 

 
系统的业务数据完成后，本命令已经存在初始配置值，如果运营商没有特殊需求，无需修改，按初始配置值生效。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
enable|是否启用|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ENABLE|参数作用：此参数用于控制SMSF是否可以启用默认SMSF配置，取值及含义如下：不启用启用修改影响：修改此参数，影响AMF是否可以使用默认SMSF的配置信息。 数据来源：本端规划。 默认值：不启用。配置原则：无。
smsfIpAddress|SMSF IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置默认SMSF的IP地址，地址格式可以为IPv4或IPv6。修改影响：修改此参数，影响默认SMSF的IP地址信息。 数据来源：本端规划。 默认值：无。配置原则：该参数应设置为正确的IPv4或IPv6地址格式 。
smsfPort|SMSF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|参数作用：该参数用于设置默认SMSF的端口号。修改影响：修改此参数，影响默认SMSF的端口号信息。 数据来源：本端规划。 默认值：8080。配置原则：无。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置默认SMSF的URI scheme，取值及含义如下：httphttps修改影响：修改此参数，影响默认SMSF的URI scheme信息。 数据来源：本端规划。 默认值：http配置原则：无。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置默认SMSF的API版本，取值及含义如下：v1v2修改影响：修改此参数，影响默认SMSF的API版本信息。 数据来源：本端规划。 默认值：v1配置原则：无。




命令举例 


`
设置默认SMSF的IP地址为“10.10.10.10”，端口号为8080。

(No.32) : SET DFTSMSF CONFIG:SMSFIPADDRESS="10.10.10.10",smsfPort=8080
-----------------Namf_Communication_0----------------
执行成功耗时: 1.214 秒

` 


#### 查询默认SMSF配置(SHOW DFTSMSF CONFIG) 
#### 查询默认SMSF配置(SHOW DFTSMSF CONFIG) 


功能说明 

该命令用于查询本AMF对应的默认SMSF的IP地址信息。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
enable|是否启用|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ENABLE|参数作用：此参数用于控制SMSF是否可以启用默认SMSF配置，取值及含义如下：不启用启用
smsfIpAddress|SMSF IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置默认SMSF的IP地址，地址格式可以为IPv4或IPv6。
smsfPort|SMSF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|参数作用：该参数用于设置默认SMSF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置默认SMSF的URI scheme，取值及含义如下：httphttps
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置默认SMSF的API版本，取值及含义如下：v1v2




命令举例 


`
查询默认SMSF配置。
SHOW DFTSMSF CONFIG

(No.1) : SHOW DFTSMSF CONFIG:
-----------------Namf_Communication_0----------------
是否启用    SMSF IP地址    SMSF端口号    URI scheme   API版本
不启用      8.8.8.8        8080          http         v1
记录数：1

执行成功耗时: 0.171 秒

` 


### 本地解析SMSF配置 
### 本地解析SMSF配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置SMSF解析数据，发现和选择SMSF。 

AMF本地配置SMSF解析数据，需要通过本地解析SMSF配置、SMSF Profile配置、SMSF地址池配置三者配合，选择出最优的SMSF用于短消息流程交互。 




功能说明 


本配置用于增加SUPI号段和SMSF模板的关联关系，AMF使用本地解析方式选择SMSF时，可以按照用户SUPI号段匹配到最优的SMSF进行短消息流程的交互。 




子主题： 






#### 增加本地解析SMSF配置(ADD SMSFLOCALRESO) 
#### 增加本地解析SMSF配置(ADD SMSFLOCALRESO) 


功能说明 

该命令用于增加一条本地解析SMSF配置。即配置用户SUPI号段与SMSF模板(SMSF Profile配置)的关联关系。当AMF选择SMSF的方式为”本地解析“时，会根据用户SUPI号码，按照号段最长匹配原则，从这些关联关系配置中，选择匹配的SMSF进行短消息流程交互。 


注意事项 

必须是SMSF Profile配置中已存在的Profile ID。 

一个SUPI段最多允许配置32个Profile。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 0-16|该参数用于配置SUPI号段，可选填。
smsfProfileID|SMSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置supiSeg对应的SMSF Profile标识。必须是SMSF Profile配置中已存在的Profile ID。一个SUPI段最多允许配置32个Profile。




命令举例 


`
增加SUPI号段为“46011”的SMSF本地解析, SMSF Profile标识为1。
ADD SMSFLOCALRESO:SUPISEG="46011",SMSFPROFILEID=1
` 


#### 删除本地解析SMSF配置(DEL SMSFLOCALRESO) 
#### 删除本地解析SMSF配置(DEL SMSFLOCALRESO) 


功能说明 

该命令用于删除一条本地解析SMSF配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 0-16|该参数用于配置SUPI号段，可选填。




命令举例 


`
删除SUPI号段为“46011”的SMSF本地解析配置。
DEL SMSFLOCALRESO:SUPISEG="46011"
` 


#### 查询本地解析SMSF配置(SHOW SMSFLOCALRESO) 
#### 查询本地解析SMSF配置(SHOW SMSFLOCALRESO) 


功能说明 

该命令用于查询本地解析SMSF配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于配置SUPI号段，可选填。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 0-16|该参数用于配置SUPI号段，可选填。
smsfProfileID|SMSF Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置supiSeg对应的SMSF Profile标识。必须是SMSF Profile配置中已存在的Profile ID。一个SUPI段最多允许配置32个Profile。




命令举例 


`
查询SUPI号段为“46011”的SMSF本地解析配置。
SHOW SMSFLOCALRESO:SUPISEG="46011"

(No.1) :SHOW SMSFLOCALRESO:SUPISEG="46011"
-----------------Namf_Communication_0----------------
SUPI号段      SMSF Profile标识
46011         1

` 


### SMSF Profile配置 
### SMSF Profile配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置SMSF解析数据，发现和选择SMSF。 

AMF本地配置SMSF解析数据，需要通过本地解析SMSF配置、SMSF Profile配置、SMSF地址池配置三者配合，选择出最优的SMSF用于短消息流程交互。 




功能说明 


本配置用于增加用于本地解析的SMSF模板，包括：SMSF的主机名、优先级、权重、IP地址、URI scheme和API版本等信息。 




子主题： 






#### 增加SMSF Profile配置(ADD SMSFPROFILECFG) 
#### 增加SMSF Profile配置(ADD SMSFPROFILECFG) 


功能说明 

该命令用于增加一条SMSF Profile配置。即配置一个包含NF实例标识、主机名、IP地址、端口号、权重、优先级、API版本及URI scheme等NF信息的模板，并用SMSF Profile标识(SMSF模板标识)来标识这一模板。当AMF选择SMSF的方式为”本地“时，会根据权重、优先级等参考条件，从配置中选择合适的SMSF进行短消息流程交互。 


注意事项 


 
主机名为必填，地址池标识为选填。 

 
一个Profile下最多输入一个地址池标识。 

 
一个Profile下只能输入一个host。 

 
ipAddressID 是引用SMSF地址池配置里的ipAddressID。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SMSFProfileId|SMSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识。当SMSF Profile标识被本地解析SMSF配置引用时，不能被删除。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置SMSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
host|主机名|参数可选性: 必选参数类型: 字符串参数范围: 0-100|该参数用于配置SMSF Profile标识对应SMSF的主机名，根据现网规划配置。主机名必须填写。一个Profile下只能输入一个主机名。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识对应的地址池标识。地址池标识为选填，不填表示无效。一个SMSF Profile下最多配置1个地址池标识。ipAddressID是引用SMSF地址池配置(SHOW SMSFLOCALADDRPOOL)里的ipAddressID。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于配置SMSF Profile标识的SMSF的优先级。AMF本地解析SMSF时，会优先选择优先级高的SMSF。优先级数值越小，表示优先级别越高。默认值为0，即默认优先级为最高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|该参数用于配置SMSF Profile标识对应的权重。AMF本地解析SMSF时，如果存在多个同等优先级的SMSF，会再根据权重进行筛选，选择权重较大的SMSF进行短消息流程的交互。权重值越大，权重优先级越高。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置SMSF Profile标识对应的URI模式。URI模式分为两类：http协议：是超文本传输协议，信息是明文传输。如果攻击者截取了Web浏览器和网站服务器之间的传输报文，就可以直接读懂其中的信息。https协议：是具有安全性的ssl加密传输协议，为浏览器和服务器之间的通信加密，确保数据传输的安全。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置API版本。用于标识服务化接口的应用版本号。目前支持V1和V2版本。




命令举例 


`
增加SMSF Profile标识为1，主机名为SMSFNJ的配置。
ADD SMSFPROFILECFG:SMSFPROFILEID=1,HOST="SMSFNJ"
` 


#### 修改SMSF Profile配置(SET SMSFPROFILECFG) 
#### 修改SMSF Profile配置(SET SMSFPROFILECFG) 


功能说明 

该命令用于修改一条SMSF Profile配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SMSFProfileId|SMSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识。当SMSF Profile标识被本地解析SMSF配置引用时，不能被删除。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置SMSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，操作员不能随意配置，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。nfInstanceId不允许从有效修改为无效。同类型NF本地解析配置中，nfInstanceId不允许重复。
host|主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于配置SMSF Profile标识对应SMSF的主机名，根据现网规划配置。主机名必须填写。一个Profile下只能输入一个主机名。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识对应的地址池标识。地址池标识为选填，不填表示无效。一个SMSF Profile下最多配置1个地址池标识。ipAddressID是引用SMSF地址池配置(SHOW SMSFLOCALADDRPOOL)里的ipAddressID。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于配置SMSF Profile标识的SMSF的优先级。AMF本地解析SMSF时，会优先选择优先级高的SMSF。优先级数值越小，表示优先级别越高。默认值为0，即默认优先级为最高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|该参数用于配置SMSF Profile标识对应的权重。AMF本地解析SMSF时，如果存在多个同等优先级的SMSF，会再根据权重进行筛选，选择权重较大的SMSF进行短消息流程的交互。权重值越大，权重优先级越高。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置SMSF Profile标识对应的URI模式。URI模式分为两类：http协议：是超文本传输协议，信息是明文传输。如果攻击者截取了Web浏览器和网站服务器之间的传输报文，就可以直接读懂其中的信息。https协议：是具有安全性的ssl加密传输协议，为浏览器和服务器之间的通信加密，确保数据传输的安全。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置API版本。用于标识服务化接口的应用版本号。目前支持V1和V2版本。




命令举例 


`
修改SMSF Profile标识为1，主机名为SMSFNJ的配置。
SET SMSFPROFILECFG:SMSFPROFILEID=1,HOST="SMSFNJ"
` 


#### 删除SMSF Profile配置(DEL SMSFPROFILECFG) 
#### 删除SMSF Profile配置(DEL SMSFPROFILECFG) 


功能说明 

该命令用于删除一条SMSF Profile配置。 


注意事项 

当SMSF Profile标识被本地解析SMSF配置配置引用时，不能被删除。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SMSFProfileId|SMSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识。当SMSF Profile标识被本地解析SMSF配置引用时，不能被删除。




命令举例 


`
删除SMSF Profile标识为1的配置。
DEL SMSFPROFILECFG:SMSFPROFILEID=1
` 


#### 查询SMSF Profile配置(SHOW SMSFPROFILECFG) 
#### 查询SMSF Profile配置(SHOW SMSFPROFILECFG) 


功能说明 

该命令用于查询SMSF Profile配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SMSFProfileId|SMSF Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识。当SMSF Profile标识被本地解析SMSF配置引用时，不能被删除。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SMSFProfileId|SMSF Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识。当SMSF Profile标识被本地解析SMSF配置引用时，不能被删除。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置SMSF网元的标识符，依据网络规划配置。
host|主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于配置SMSF Profile标识对应SMSF的主机名，根据现网规划配置。主机名必须填写。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF Profile标识对应的地址池标识。地址池标识为选填，不填表示无效。一个SMSF Profile下最多配置1个地址池标识。ipAddressID是引用SMSF地址池配置(SHOW SMSFLOCALADDRPOOL)里的ipAddressID。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于配置SMSF Profile标识的SMSF的优先级。AMF本地解析SMSF时，会优先选择优先级高的SMSF。优先级数值越小，表示优先级别越高。默认值为0，即默认优先级为最高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|该参数用于配置SMSF Profile标识对应的权重。AMF本地解析SMSF时，如果存在多个同等优先级的SMSF，会再根据权重进行筛选，选择权重较大的SMSF进行短消息流程的交互。权重值越大，权重优先级越高。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置SMSF Profile标识对应的URI模式。URI模式分为两类：http协议：是超文本传输协议，信息是明文传输。如果攻击者截取了Web浏览器和网站服务器之间的传输报文，就可以直接读懂其中的信息。https协议：是具有安全性的ssl加密传输协议，为浏览器和服务器之间的通信加密，确保数据传输的安全。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置API版本。用于标识服务化接口的应用版本号。目前支持V1和V2版本。




命令举例 


`
查询SMSF Profile标识为1的配置。
SHOW SMSFPROFILECFG:SMSFPROFILEID=1

(No.1) : SHOW SMSFPROFILECFG:SMSFPROFILEID=1
-----------------Namf_Communication_0----------------
SMSF Profile标识     NF实例标识                              主机名      地址池标识     优先级    权重    URI scheme    API版本   
1                    2b3d8182-365c-44ff-a051-ef56f89732d5   SMSFNJ      1             0        200     HTTP          v1             

` 


### SMSF地址池配置 
### SMSF地址池配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置SMSF解析数据，发现和选择SMSF。 

AMF本地配置SMSF解析数据，需要通过本地解析SMSF配置、SMSF Profile配置、SMSF地址池配置三者配合，选择出最优的SMSF用于短消息流程交互。 




功能说明 


一个SMSF Profile可以关联多个IP地址，为了提高配置效率，AMF通过“SMSF地址池配置”把地址列表和地址池标识关联，“SMSF Profile配置”只需要引用相应的地址池标识。 




子主题： 






#### 增加SMSF地址池配置(ADD SMSFLOCALADDRPOOL) 
#### 增加SMSF地址池配置(ADD SMSFLOCALADDRPOOL) 


功能说明 

一个SMSF Profile可以关联多个IP地址，为了提高配置效率，AMF通过“SMSF地址池配置”把SMSF的一个或多个地址与地址池标识关联，“SMSF Profile配置”只需要引用相应的地址池标识。 

该命令用于增加一条SMSF地址池配置，以供“SMSF Profile配置” 引用。 


注意事项 

一个IP地址只能归属一个地址池标识。 

一个地址池内最多配置16个IP地址。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF地址池标识，一个地址池标识可以关联多个“IP地址与端口号的组合”，但需要保证这些组合中不存在重复的IP地址，即一个地址池标识下，即使端口号不同，也不允许配置相同的IP地址。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于配置归属该SMSF地址池的SMSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置归属该SMSF地址池的SMSF的端口号。




命令举例 


`
增加SMSF地址池配置，地址池标识符为1，SMSF的IP地址为“12.12.12.12”，端口号为8080。
ADD SMSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",PORT=8080
` 


#### 删除SMSF地址池配置(DEL SMSFLOCALADDRPOOL) 
#### 删除SMSF地址池配置(DEL SMSFLOCALADDRPOOL) 


功能说明 

该命令用于删除一条SMSF地址池配置。 


注意事项 

当地址池标识被SMSF Profile配置引用时，不能被删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF地址池标识，一个地址池标识可以关联多个“IP地址与端口号的组合”，但需要保证这些组合中不存在重复的IP地址，即一个地址池标识下，即使端口号不同，也不允许配置相同的IP地址。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置归属该SMSF地址池的SMSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置归属该SMSF地址池的SMSF的端口号。




命令举例 


`
删除SMSF地址池配置，地址池标识符为1，SMSF的IP地址为“12.12.12.12”，端口号为8080。
DEL SMSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",PORT=8080
` 


#### 查询SMSF地址池配置(SHOW SMSFLOCALADDRPOOL) 
#### 查询SMSF地址池配置(SHOW SMSFLOCALADDRPOOL) 


功能说明 

该命令用于查询SMSF地址池配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF地址池标识，一个地址池标识可以关联多个“IP地址与端口号的组合”，但需要保证这些组合中不存在重复的IP地址，即一个地址池标识下，即使端口号不同，也不允许配置相同的IP地址。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置归属该SMSF地址池的SMSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置归属该SMSF地址池的SMSF的端口号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置SMSF地址池标识，一个地址池标识可以关联多个“IP地址与端口号的组合"，但需要保证这些组合中不存在重复的IP地址，即一个地址池标识下，即使端口号不同，也不允许配置相同的IP地址。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置配置SMSF地址池配置的地址池标识对应的SMSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置配置SMSF地址池配置的地址池标识对应的SMSF的端口号。




命令举例 


`
查询地址池标识符为1的SMSF地址池配置。
SHOW SMSFLOCALADDRPOOL:ADDRPOOLID=1

(No.1) : SHOW SMSFLOCALADDRPOOL:ADDRPOOLID=1
-----------------Namf_Communication_0----------------
地址池标识   IP地址         端口号
1          12.12.12.12      8080        

` 


## AMF本地解析配置 
## AMF本地解析配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取其他AMF的解析数据，后续用于本地发现和选择其他的AMF。 




功能说明 


UE在5G网络内移动，目标区域不是当前UE所在AMF的服务区时，根据目标区域发现和选择新AMF为UE提供服务。AMF本地解析配置提供本地配置解析对应的目标AMF。 




子主题： 






### 号段选择AMF配置 
### 号段选择AMF配置 


背景知识 


基于号段选择AMF是指用户位置发生移动，触发N2切换请求流程，将业务切到其他AMF上时，AMF根据用户GPSI/SUPI号码选择拨测的目标AMF。可用于运营商拨测场景。拨测使用场景如下： 


 
运维人员需要测试新入网的AMF，AMF没有和NRF建立连接或还没有向NRF注册，原AMF能够将测试用户指向该AMF进行拨测。 

 
运维人员怀疑原AMF可能有问题或者故障，原AMF能够将测试用户指向该AMF进行切换拨测。 

 




功能说明 


本配置提供基于号段解析AMF的全局策略，以及用户级基于号段解析AMF的配置。 




子主题： 






#### 基于号段选择AMF策略 
#### 基于号段选择AMF策略 


背景知识 


基于号段选择AMF是指用户位置发生移动，触发N2切换请求流程，将业务切到其他AMF上时，AMF根据用户GPSI/SUPI号码选择拨测的目标AMF。可用于运营商拨测场景。拨测使用场景如下： 


 
运维人员需要测试新入网的AMF，AMF没有和NRF建立连接或还没有向NRF注册，原AMF能够将测试用户指向该AMF进行拨测。 

 
运维人员怀疑原AMF可能有问题或者故障，原AMF能够将测试用户指向该AMF进行切换拨测。 

 




功能说明 


该配置用于设置支持基于号段选择AMF的功能开关。 




子主题： 






##### 修改基于号段选择AMF策略配置(SET RESOLAMFPOLICY) 
##### 修改基于号段选择AMF策略配置(SET RESOLAMFPOLICY) 


功能说明 

该命令用于设置支持基于号段选择AMF策略配置。用于在AMF拨测场景中，让某一部分测试用户在切换流程中将业务切换到其他AMF时，AMF根据用户GPSI/SUPI号码选择拨测所指定的AMF网元。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supamfnumsel|支持基于号段选择AMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置是否支持基于号段选择AMF。修改影响：开启之后，用户可通过号段选择AMF配置选择目标AMF。数据来源：本端规划 默认值：不支持 配置原则：无




命令举例 


`
设置支持基于号段选择AMF的功能。
SET RESOLAMFPOLICY:SUPAMFNUMSEL="SPRT"
` 


##### 查询基于号段选择AMF策略配置(SHOW RESOLAMFPOLICY) 
##### 查询基于号段选择AMF策略配置(SHOW RESOLAMFPOLICY) 


功能说明 

该命令用于查询支持基于号段选择AMF这个功能开关的状态。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
supamfnumsel|支持基于号段选择AMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置是否支持基于号段选择AMF。修改影响：开启之后，用户可通过号段选择AMF配置选择目标AMF。数据来源：本端规划 默认值：不支持 配置原则：无




命令举例 


`
查询基于号段选择AMF策略配置。
SHOW RESOLAMFPOLICY

(No.1) : SHOW RESOLAMFPOLICY:
-----------------Namf_Communication_0----------------
操作维护     支持基于号段选择AMF
----------------------
修改            支持 
----------------------
记录数：1

执行成功开始时间:2020-05-29 16:32:49 耗时: 0.436 秒

` 


#### 基于号段选择AMF配置 
#### 基于号段选择AMF配置 


背景知识 


基于号段选择AMF是指用户位置发生移动，触发N2切换请求流程，将业务切到其他AMF上时，AMF根据用户GPSI/SUPI号码选择拨测的目标AMF。可用于运营商拨测场景。拨测使用场景如下： 


 
运维人员需要测试新入网的AMF，AMF没有和NRF建立连接或还没有向NRF注册，原AMF能够将测试用户指向该AMF进行拨测。 

 
运维人员怀疑原AMF可能有问题或者故障，原AMF能够将测试用户指向该AMF进行切换拨测。 

 




功能说明 


该配置用于设置基于GPSI/SUPI号段解析AMF的数据，包括AMF FQDN、地址池标识、优先级、权重、URI scheme和API版本。 




子主题： 






##### 新增基于号段选择AMF配置(ADD RESOLAMFNUMCFG) 
##### 新增基于号段选择AMF配置(ADD RESOLAMFNUMCFG) 


功能说明 

该命令用于新增基于号段解析AMF配置，用于在AMF拨测场景中，让某一部分测试用户在切换流程中将业务切换到其他AMF时，AMF根据用户GPSI/SUPI号码选择拨测所指定的AMF网元。 

该命令的配置结果可以通过[SHOW RESOLAMFNUMCFG]命令进行查询。

执行此命令前，需先执行[SET RESOLAMFPOLICY]命令，配置支持基于号段选择AMF。


注意事项 

如需要在基于号段解析AMF配置中配置地址池，必须先配置AMF地址池。可以通过[SHOW AMFLOCALADDRPOOL]命令查询已配置的AMF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。设置号码长度大于等于10且小于等于15。修改影响：基于号段选择AMF开启后，AMF对配置号段对应的用户进行AMF拨测。数据来源：本端规划默认值：无  配置原则：无
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：基于号段选择AMF开启后，AMF对符合号码类型的用户进行AMF拨测。数据来源：本端规划默认值：无配置原则：无
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置目标AMF的FQDN。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的FQDN。数据来源：本端规划默认值：无配置原则：无
ippoolid|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置AMF地址池标识，该参数必须已经存在，可以通过SHOW AMFLOCALADDRPOOL命令查询已配置的AMF地址池。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的地址池标识。数据来源：本端规划默认值：无配置原则：无
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置AMF优先级，用于当查询到多个AMF时，根据优先级高低选择其中的一个AMF，优先级数字越小，优先级越高。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的优先级。数据来源：本端规划默认值：0配置原则：无
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置AMF静态权重，用于查询到多个AMF并且各个AMF实例的优先级相同时，根据权重选择其中的一个AMF。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的权重。数据来源：本端规划默认值：200配置原则：无
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置AMF的URI scheme。比如 "http"、"https"。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的URI scheme。数据来源：本端规划默认值：http配置原则：无
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置AMF的API版本，比如v1或v2。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的API版本。数据来源：本端规划默认值：v1配置原则：无
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于配置表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长配置为空表示该号段配置永久有效。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF，对应的配置条目中增加或修改时间参数，限制该配置的有效使用日期。数据来源：本端规划默认值：无配置原则：无




命令举例 


`
新增一条基于GPSI/SUPI号段解析AMF配置，其中，用户号码为13895122456，号码类型为GPSI，NF实例标识为f81d4fae-7dec-1111-a765-00a0c91e6789，AMF的FQDN为amf1，地址池标识为1，优先级为1，权重为10，URI scheme为HTTP，API版本为V1，配置有效时间为2022-01-20 11:16:38。
ADD RESOLAMFNUMCFG:NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",FQDN="amf1",IPPOOLID=1,PRIORITY=1,WEIGHT=10,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2022-01-20 11:16:38"
` 


##### 修改基于号段选择AMF配置(SET RESOLAMFNUMCFG) 
##### 修改基于号段选择AMF配置(SET RESOLAMFNUMCFG) 


功能说明 

该命令用于修改基于号段解析AMF配置，用于拨测场景中，让某一部分测试用户在切换流程中切出到其他局时，AMF根据用户GPSI/SUPI号码选择拨测所指定的AMF网元。 

该命令的配置结果可以通过[SHOW RESOLAMFNUMCFG]命令进行查询。


注意事项 

如需要修改基于号段解析AMF配置中的地址池，该地址池必须存在。可以通过[SHOW AMFLOCALADDRPOOL]命令查询已配置的AMF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。设置号码长度大于等于10且小于等于15。修改影响：基于号段选择AMF开启后，AMF对配置号段对应的用户进行AMF拨测。数据来源：本端规划默认值：无  配置原则：无
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：基于号段选择AMF开启后，AMF对符合号码类型的用户进行AMF拨测。数据来源：本端规划默认值：无配置原则：无
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
fqdn|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置目标AMF的FQDN。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的FQDN。数据来源：本端规划默认值：无配置原则：无
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置AMF地址池标识，该参数必须已经存在，可以通过SHOW AMFLOCALADDRPOOL命令查询已配置的AMF地址池。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的地址池标识。数据来源：本端规划默认值：无配置原则：无
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置AMF优先级，用于当查询到多个AMF时，根据优先级高低选择其中的一个AMF，优先级数字越小，优先级越高。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的优先级。数据来源：本端规划默认值：0配置原则：无
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置AMF静态权重，用于查询到多个AMF并且各个AMF实例的优先级相同时，根据权重选择其中的一个AMF。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的权重。数据来源：本端规划默认值：200配置原则：无
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置AMF的URI scheme。比如 "http"、"https"。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的URI scheme。数据来源：本端规划默认值：http配置原则：无
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置AMF的API版本，比如v1或v2。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的API版本。数据来源：本端规划默认值：v1配置原则：无
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于配置表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长配置为空表示该号段配置永久有效。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF，对应的配置条目中增加或修改时间参数，限制该配置的有效使用日期。数据来源：本端规划默认值：无配置原则：无




命令举例 


`
修改一条基于GPSI/SUPI号段解析AMF配置，其中，修改用户号码为13895122456，号码类型为GPSI，NF实例标识为f81d4fae-7dec-1111-a765-00a0c91e6789，AMF的FQDN为amf1，优先级为2，权重为10，URI scheme为HTTP，API版本为V1，配置有效时间为2021-12-20 11:11:11。
SET RESOLAMFNUMCFG:NUMBER="13895122456",NUMTYPE="GPSI",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",FQDN="amf1",IPPOOLID=1,PRIORITY=2,WEIGHT=10,SCHEME="HTTP",APIVERSION="V1",VALIDITYTIME="2021-12-20 11:11:11"
` 


##### 删除基于号段选择AMF配置(DEL RESOLAMFNUMCFG) 
##### 删除基于号段选择AMF配置(DEL RESOLAMFNUMCFG) 


功能说明 

该命令用于删除基于号段解析AMF的配置数据。 

该命令的配置结果可以通过[SHOW RESOLAMFNUMCFG]命令进行查询。


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。设置号码长度大于等于10且小于等于15。修改影响：基于号段选择AMF开启后，AMF对配置号段对应的用户进行AMF拨测。数据来源：本端规划默认值：无  配置原则：无
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：基于号段选择AMF开启后，AMF对符合号码类型的用户进行AMF拨测。数据来源：本端规划默认值：无配置原则：无
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置目标AMF的FQDN。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的FQDN。数据来源：本端规划默认值：无配置原则：无




命令举例 


`
删除一条基于GPSI/SUPI号段解析AMF配置。
DEL RESOLAMFNUMCFG:NUMBER="13895122456",NUMTYPE="GPSI",FQDN="amf1"
` 


##### 查询基于号段选择AMF配置(SHOW RESOLAMFNUMCFG) 
##### 查询基于号段选择AMF配置(SHOW RESOLAMFNUMCFG) 


功能说明 

该命令用于查询基于号段解析AMF的配置数据。可以查询所有配置，也可以按号码段查询特定配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。设置号码长度大于等于10且小于等于15。修改影响：基于号段选择AMF开启后，AMF对配置号段对应的用户进行AMF拨测。数据来源：本端规划默认值：无  配置原则：无
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：基于号段选择AMF开启后，AMF对符合号码类型的用户进行AMF拨测。数据来源：本端规划默认值：无配置原则：无
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置目标AMF的FQDN。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的FQDN。数据来源：本端规划默认值：无配置原则：无




输出参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。设置号码长度大于等于10且小于等于15。修改影响：基于号段选择AMF开启后，AMF对配置号段对应的用户进行AMF拨测。数据来源：本端规划默认值：无  配置原则：无
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置号码类型，选项如下。GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）修改影响：基于号段选择AMF开启后，AMF对符合号码类型的用户进行AMF拨测。数据来源：本端规划默认值：无配置原则：无
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
fqdn|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置目标AMF的FQDN。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的FQDN。数据来源：本端规划默认值：无配置原则：无
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置AMF地址池标识，该参数必须已经存在，可以通过SHOW AMFLOCALADDRPOOL命令查询已配置的AMF地址池。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的地址池标识。数据来源：本端规划默认值：无配置原则：无
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置AMF优先级，用于当查询到多个AMF时，根据优先级高低选择其中的一个AMF，优先级数字越小，优先级越高。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的优先级。数据来源：本端规划默认值：0配置原则：无
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置AMF静态权重，用于查询到多个AMF并且各个AMF实例的优先级相同时，根据权重选择其中的一个AMF。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的权重。数据来源：本端规划默认值：200配置原则：无
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置AMF的URI scheme。比如 "http"、"https"。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的URI scheme。数据来源：本端规划默认值：http配置原则：无
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置AMF的API版本，比如v1或v2。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF的API版本。数据来源：本端规划默认值：v1配置原则：无
validityTime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于配置表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长配置为空表示该号段配置永久有效。修改影响：基于号段选择AMF开启后，AMF对需要拨测的用户配置目标AMF，对应的配置条目中增加或修改时间参数，限制该配置的有效使用日期。数据来源：本端规划默认值：无配置原则：无




命令举例 


`
查询所有基于GPSI/SUPI号段解析AMF配置。
SHOW RESOLAMFNUMCFG

(No.1) : SHOW RESOLAMFNUMCFG:
-----------------Namf_Communication_0----------------
操作维护       用户号码 号码类型 NF实例标识                           FQDN    地址池标识 优先级 权重 URI scheme API版本 有效时间            
--------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 13856000001    GPSI     f81d4fae-7dec-1111-a765-00a0c91e6789 zte.com 1          1      200  HTTP       V1版本  2021-08-27 00:00:00 
--------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-12 15:08:45 耗时: 0.156 秒

` 


### AMF地址池配置 
### AMF地址池配置 


背景知识 


在运营商拨测等场景下，需要通过AMF本地配置获取AMF的IP地址，后续用于本地发现和选择AMF。 




功能说明 


一个AMF会关联多个IP地址，为了提高配置效率，AMF根据“AMF地址池配置”把地址列表和地址池标识关联，“基于号段选择AMF配置”中只需要引用相应的地址池标识。 




子主题： 






#### 增加AMF地址池配置(ADD AMFLOCALADDRPOOL) 
#### 增加AMF地址池配置(ADD AMFLOCALADDRPOOL) 


功能说明 

该命令用于增加一条AMF地址池配置。一个地址池ID可以对应多个地址。 


注意事项 

一个IP地址只能归属一个地址池标识。 

 
 一个地址池内最多配置16个IP地址。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF地址池配置的地址池标识。当地址池标识被基于号段选择AMF配置配置引用时，不能被删除。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于地址池标识对应的AMF网元或AMF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AMF网元或AMF服务通信IP地址对应的端口号。




命令举例 


`
增加地址池标识符为1，IP地址为“12.12.12.12”，端口号为8080的AMF地址池配置。
ADD AMFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",PORT=8080
` 


#### 删除AMF地址池配置(DEL AMFLOCALADDRPOOL) 
#### 删除AMF地址池配置(DEL AMFLOCALADDRPOOL) 


功能说明 

该命令用于删除一条AMF地址池配置。 


注意事项 

当地址池标识被基于号段选择AMF配置引用时，不能被删除。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF地址池配置的地址池标识。当地址池标识被基于号段选择AMF配置配置引用时，不能被删除。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于地址池标识对应的AMF网元或AMF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AMF网元或AMF服务通信IP地址对应的端口号。




命令举例 


`
删除地址池标识符为1，IP地址为“12.12.12.12”，端口号为8080的AMF地址池配置。
DEL AMFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",PORT=8080
` 


#### 查询AMF地址池配置(SHOW AMFLOCALADDRPOOL) 
#### 查询AMF地址池配置(SHOW AMFLOCALADDRPOOL) 


功能说明 

该命令用于查询AMF地址池配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF地址池配置的地址池标识。当地址池标识被基于号段选择AMF配置配置引用时，不能被删除。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于地址池标识对应的AMF网元或AMF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AMF网元或AMF服务通信IP地址对应的端口号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF地址池配置的地址池标识。当地址池标识被基于号段选择AMF配置配置引用时，不能被删除。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于地址池标识对应的AMF网元或AMF服务的IP地址，地址格式可以为IPv4或IPv6。 一个IP地址只能归属一个地址池标识。一个地址池内最多配置16个IP地址。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置地址池标识对应的AMF网元或AMF服务通信IP地址对应的端口号。




命令举例 


`
删除地址池标识符为1的AMF地址池配置。
SHOW AMFLOCALADDRPOOL:ADDRPOOLID=1

(No.1) : SHOW AMFLOCALADDRPOOL:ADDRPOOLID=1
-----------------Namf_Communication_0----------------
地址池标识   IP地址          端口号
1           12.12.12.12      8080        

` 


## NSSF本地解析配置 
## NSSF本地解析配置 


背景知识 


当5GC网络中没有部署NRF或者NRF不可用（升级或故障）时，运营商希望通过AMF本地配置的数据，来获取NSSF的IP地址，后续用于发现和选择NSSF。 




功能说明 


UE进行各业务流程，AMF和NSSF协商切片或向NSSF获取切片信息时，NSSF本地解析配置提供NF级和服务级的地址解析数据配置。 




子主题： 






### NSSF地址解析配置 
### NSSF地址解析配置 


背景知识 


5GC网络中的AMF与NSSF进行交互时，需要获取NSSF的IP地址以进行通信。 

AMF获取NSSF的IP地址的方式有以下两种。 


 
通过NRF发现NSSF的IP地址。 

 
通过AMF本地配置的数据，解析获取NSSF的IP地址。
通常情况下，建议使用通过AMF本地配置的数据解析获取NSSF IP地址。 

 




功能说明 


本功能用于本AMF，通过对NSSF地址解析配置进行解析，获取对应的NSSF。 




子主题： 






#### 增加NSSF Profile配置(ADD NSSFPROFILECFG) 
#### 增加NSSF Profile配置(ADD NSSFPROFILECFG) 


功能说明 

该命令用于增加一条NSSF Profile配置。 


注意事项 

1.本命令执行后，配置立即生效。 

2.最多只能配置1024条记录。 

3.同一个"NSSF服务Profile标识"下，仅能配置一个地址池标识。 

4.同一个"NSSF服务Profile标识"下，仅能配置一个域名。
5.执行本命令之前，确保"地址池标识"已经通过ADD NSSFLOCALADDRPOOL命令配置。 

NSSelSerProfileld和NSSAIAVAISerProld没有配置有效值，则表示该NSSF支持所有服务，服务的选择因子就是该NF Profile下面的配置。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFProfileId|NSSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：NSSFProfileld对于所有的记录都是唯一的。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置NSSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，不能单独修改，必须全网统一规划，确保没有重复。数据来源：全网规划。默认值：无。配置原则：1. 采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node"。只能为a-f、0-9的字符。2. nfInstanceId不允许从有效设为无效。3. 同类型NF本地解析配置中，nfInstanceId不允许重复。
host|域名|参数可选性: 必选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名。域名只支持小写输入。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的地址池标识。修改影响：无。数据来源：地址池标识是引用NSSF地址池配置里的地址池标识（通过ADD NSSFLOCALADDRPOOL命令配置）。默认值：无。配置原则：一个Profile下最多输入1个地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于配置NSSF Profile对应的优先级。修改影响：无。数据来源：本端规划默认值：0。配置原则：数值越小优先级越高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于配置NSSF Profile对应的权重。修改影响：无。数据来源：本端规划默认值：200。配置原则：无。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于配置NSSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划默认值：http。配置原则：无。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于配置API版本。修改影响：无。数据来源：本端规划默认值：v1。配置原则：无。
NSSelSerProfileId|NS Selection服务Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的NS Selection服务Profile标识。修改影响：无。数据来源：引用的是NSSF服务Profile配置里的NSSF服务Profile标识（通过ADD NSSFSERPROFILECFG命令配置）。默认值：无。配置原则：无。
NSSAIAVAISerProId|NSSAI Availability服务标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的NSSAI Availability服务Profile标识。修改影响：无。数据来源：引用的是NSSF服务Profile配置里的NSSF服务Profile标识（通过ADD NSSFSERPROFILECFG命令配置）。默认值：无。配置原则：无。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置NSSF网元的实例名称，依据网络规划配置。修改影响：nfInstanceName是一个网元的唯一实例名称，操作员不能随意修改，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：同类型NF本地解析配置中，nfInstanceName不允许重复。




命令举例 


`
增加NSSF Profile配置，NSSF Profile标识为1，域名为nssf，其余参数采用默认值。
ADD NSSFPROFILECFG:NSSFPROFILEID=1,HOST="nssf",PRIORITY=0,WEIGHT=200,SCHEMA="HTTP",APIVERSION="V1"
` 


#### 修改NSSF Profile配置(SET NSSFPROFILECFG) 
#### 修改NSSF Profile配置(SET NSSFPROFILECFG) 


功能说明 

该命令用于修改一条NSSF Profile配置。 


注意事项 

1.本命令执行后，配置立即生效。 

2.不支持修改"NSSF服务类型"，若需要修改已有配置记录的"NSSF服务类型"，则应先删除对应的配置记录，然后通过ADD NSSFPROFILECFG命令新增对应的配置记录。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFProfileId|NSSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：NSSFProfileld对于所有的记录都是唯一的。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置NSSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，不能单独修改，必须全网统一规划，确保没有重复。数据来源：全网规划。默认值：无。配置原则：1. 采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node"。只能为a-f、0-9的字符。2. nfInstanceId不允许从有效设为无效。3. 同类型NF本地解析配置中，nfInstanceId不允许重复。
host|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名。域名只支持小写输入。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的地址池标识。修改影响：无。数据来源：地址池标识是引用NSSF地址池配置里的地址池标识（通过ADD NSSFLOCALADDRPOOL命令配置）。默认值：无。配置原则：一个Profile下最多输入1个地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于配置NSSF Profile对应的优先级。修改影响：无。数据来源：本端规划默认值：0。配置原则：数值越小优先级越高。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于配置NSSF Profile对应的权重。修改影响：无。数据来源：本端规划默认值：200。配置原则：无。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于配置NSSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划默认值：http。配置原则：无。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于配置API版本。修改影响：无。数据来源：本端规划默认值：v1。配置原则：无。
NSSelSerProfileId|NS Selection服务Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的NS Selection服务Profile标识。修改影响：无。数据来源：引用的是NSSF服务Profile配置里的NSSF服务Profile标识（通过ADD NSSFSERPROFILECFG命令配置）。默认值：无。配置原则：无。
NSSAIAVAISerProId|NSSAI Availability服务标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的NSSAI Availability服务Profile标识。修改影响：无。数据来源：引用的是NSSF服务Profile配置里的NSSF服务Profile标识（通过ADD NSSFSERPROFILECFG命令配置）。默认值：无。配置原则：无。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置NSSF网元的实例名称，依据网络规划配置。修改影响：nfInstanceName是一个网元的唯一实例名称，操作员不能随意修改，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：同类型NF本地解析配置中，nfInstanceName不允许重复。




命令举例 


`
修改NSSF Profile配置，NSSF Profile标识为1，修改其对应的地址池标识为1。
SET NSSFPROFILECFG:NSSFPROFILEID=1,IPADDRESSID=1
` 


#### 删除NSSF Profile配置(DEL NSSFPROFILECFG) 
#### 删除NSSF Profile配置(DEL NSSFPROFILECFG) 


功能说明 

该命令用于删除一条NSSF Profile配置。 


注意事项 

1.本命令执行后，配置立即生效。 

2.本命令仅支持一次删除一条配置记录，即删除指定"NSSF服务Profile标识"对应的配置记录。 

3.执行本命令之前，确保待删除配置记录的"NSSF服务Profile标识"，不在SHOW NSSFPROFILECFG命令查询结果中。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFProfileId|NSSF Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：NSSFProfileld对于所有的记录都是唯一的。




命令举例 


`
删除NSSF Profile标识为1的配置。
DEL NSSFPROFILECFG:NSSFPROFILEID=1
` 


#### 查询NSSF Profile配置(SHOW NSSFPROFILECFG) 
#### 查询NSSF Profile配置(SHOW NSSFPROFILECFG) 


功能说明 

该命令用于查询NSSF Profile配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFProfileId|NSSF Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：NSSFProfileld对于所有的记录都是唯一的。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFProfileId|NSSF Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile标识。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置NSSF网元的标识符，依据网络规划配置。
host|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置NSSF Profile对应的地址池标识。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于配置NSSF Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于配置NSSF Profile对应的权重。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于配置NSSF Profile对应的URI scheme。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于配置API版本。
NSSelSerProfileId|NS Selection服务Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF Profile对应的NS Selection服务Profile标识，引用的是NSSF服务Profile配置里的NSSF服务Profile标识（通过ADD NSSFSERPROFILECFG命令配置）。
NSSAIAVAISerProId|NSSAI Availability服务标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF Profile对应的NSSAI Availability服务Profile标识，引用的是NSSF服务Profile配置里的NSSF服务Profile标识（通过ADD NSSFSERPROFILECFG命令配置）。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置NSSF网元的实例名称，依据网络规划配置。




命令举例 


`
查询NSSF Profile标识为1的配置。
SHOW NSSFPROFILECFG:NSSFPROFILEID=1

(No.1) : SHOW NSSFPROFILECFG:NSSFPROFILEID=1
-----------------Namf_Communication_0----------------
NSSF Profile标识    NF实例标识                              域名      地址池标识     优先级   权重    URI scheme    API版本   NS Selection服务Profile标识  NSSAI Availability服务标识  NF实例名
1                  11111111-7dec-11d0-a765-111111111110   nssf           1         0       200       HTTP          v1             1   

` 


### NSSF Profile服务配置 
### NSSF Profile服务配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障），或者不支持NRF发现NSSF时，运营商希望通过AMF本地配置NSSF解析数据，发现和选择NSSF。 

AMF本地配置NSSF解析数据，需要通过NSSF地址解析配置、NSSF服务Profile配置、NSSF地址池配置三个配合。 




功能说明 


NSSF本地解析配置按照NRF响应的分层结构（网元级和服务级），分为了“NSSF服务Profile配置”和“ NSSF地址解析配置”，“ NSSF地址解析配置”对应NF Profile，而“NSSF服务Profile配置”对应NF Service。“NSSF 服务Profile配置”的配置项包括主机名，IP地址池标识，权重，优先级，URI scheme，API Version。 




子主题： 






#### 增加NSSF服务Profile配置(ADD NSSFSERPROFILECFG) 
#### 增加NSSF服务Profile配置(ADD NSSFSERPROFILECFG) 


功能说明 

该命令用于增加一条NSSF服务Profile配置。 


注意事项 


 
一个Profile下最多配置1个地址池标识。 

 
一个Profile下只能配置一个域名。 

 
地址池标识是引用NSSF地址池配置里的地址池标识（通过ADD NSSFLOCALADDRPOOL命令配置）。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFSerProfileId|NSSF服务Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile标识。当NSSF服务Profile标识被NSSF Profile配置引用时，不能被删除。
NSSFSerType|NSSF服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: NSSF_NSSELECTION|该参数用于配置NSSF服务类型，取值如下：SELECTION 服务，对应的协议原文解释为：This service enables Network Slice selection in both the Serving PLMN and the HPLMN。NSSAI AVAILABILITY 服务，对应的协议原文解释为：This service enables to update the S-NSSAI(s) the NF service consumer (e.g AMF) supports on a per TA basis on the NSSF and to subscribe and notify any change in status, on a per TA basis, of the SNSSAIs available per TA (unrestricted) and the restricted S-NSSAI(s) per PLMN in that TA in the serving PLMN of the UE.
host|域名|参数可选性: 必选参数类型: 字符串参数范围: 0-100|该参数用于配置NSSF服务Profile对应的域名，即NSSF服务的域名。一个Profile下只能输入一个域名。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile对应的地址池标识。一个Profile下最多输入1个地址池标识。地址池标识是引用NSSF地址池配置里的地址池标识（通过ADD NSSFLOCALADDRPOOL命令配置）。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于配置NSSF服务Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|该参数用于配置NSSF服务Profile对应的权重。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置NSSF服务Profile对应的URI scheme。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置API版本。




命令举例 


`
增加NSSF服务Profile配置，NSSF服务Profile标识为1，NSSF服务类型为SELECTION服务，域名为nssf_ser。其余参数使用默认值。
ADD NSSFSERPROFILECFG:NSSFSERPROFILEID=1,NSSFSERTYPE="NSSF_NSSELECTION",HOST="nssf_ser",PRIORITY=0,WEIGHT=200,SCHEMA="HTTP",APIVERSION="V1"
` 


#### 修改NSSF服务Profile配置(SET NSSFSERPROFILECFG) 
#### 修改NSSF服务Profile配置(SET NSSFSERPROFILECFG) 


功能说明 

该命令用于修改一条NSSF服务Profile配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFSerProfileId|NSSF服务Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile标识。当NSSF服务Profile标识被NSSF Profile配置引用时，不能被删除。
host|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于配置NSSF服务Profile对应的域名，即NSSF服务的域名。一个Profile下只能输入一个域名。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile对应的地址池标识。一个Profile下最多输入1个地址池标识。地址池标识是引用NSSF地址池配置里的地址池标识（通过ADD NSSFLOCALADDRPOOL命令配置）。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于配置NSSF服务Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|该参数用于配置NSSF服务Profile对应的权重。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置NSSF服务Profile对应的URI scheme。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置API版本。




命令举例 


`
修改NSSF服务Profile配置，NSSF服务Profile标识为1，对应的域名为nssf_ser1。
SET NSSFSERPROFILECFG:NSSFSERPROFILEID=1,HOST="nssf_ser1"
` 


#### 删除NSSF服务Profile配置(DEL NSSFSERPROFILECFG) 
#### 删除NSSF服务Profile配置(DEL NSSFSERPROFILECFG) 


功能说明 

该命令用于删除一条NSSF服务Profile配置。 


注意事项 

1、如果NSSF Profile下未关联任何NSSF服务，本命令执行后，不会影响业务。2、如果NSSF Profile下关联了该NSSF服务Profile标识，则本配置无法删除。（不属于高危命令） 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFSerProfileId|NSSF服务Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile标识。当NSSF服务Profile标识被NSSF Profile配置引用时，不能被删除。




命令举例 


`
删除NSSF服务Profile标识为1的配置。
DEL NSSFSERPROFILECFG:NSSFSERPROFILEID=1
` 


#### 查询NSSF服务Profile配置(SHOW NSSFSERPROFILECFG) 
#### 查询NSSF服务Profile配置(SHOW NSSFSERPROFILECFG) 


功能说明 

该命令用于查询NSSF服务Profile配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFSerProfileId|NSSF服务Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile标识。当NSSF服务Profile标识被NSSF Profile配置引用时，不能被删除。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
NSSFSerProfileId|NSSF服务Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile标识。当NSSF服务Profile标识被NSSF Profile配置引用时，不能被删除。
NSSFSerType|NSSF服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: NSSF_NSSELECTION|该参数用于配置NSSF服务类型，取值如下：SELECTION 服务，对应的协议原文解释为：This service enables Network Slice selection in both the Serving PLMN and the HPLMN。NSSAI AVAILABILITY 服务，对应的协议原文解释为：This service enables to update the S-NSSAI(s) the NF service consumer (e.g AMF) supports on a per TA basis on the NSSF and to subscribe and notify any change in status, on a per TA basis, of the SNSSAIs available per TA (unrestricted) and the restricted S-NSSAI(s) per PLMN in that TA in the serving PLMN of the UE.
host|域名|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于配置NSSF服务Profile对应的域名，即NSSF服务的域名。一个Profile下只能输入一个域名。
ipAddressID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF服务Profile对应的地址池标识。一个Profile下最多输入1个地址池标识。地址池标识是引用NSSF地址池配置里的地址池标识（通过ADD NSSFLOCALADDRPOOL命令配置）。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|该参数用于配置NSSF服务Profile对应的优先级。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|该参数用于配置NSSF服务Profile对应的权重。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置NSSF服务Profile对应的URI scheme。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置API版本。




命令举例 


`
查询NSSF服务Profile配置。
SHOW NSSFSERPROFILECFG

(No.1) : SHOW NSSFSERPROFILECFG:
-----------------Namf_Communication_0----------------
NSSF服务Profile标识    NSSF服务类型       域名      地址池标识  优先级    权重    URI scheme    API版本 
1                      NSSF_NSSELECTION  nssf_ser     1         0       200       HTTP          v1           
记录数：1
执行成功耗时: 0.12 秒

` 


### NSSF地址池配置 
### NSSF地址池配置 


背景知识 


当现网没有部署NRF或者NRF不可用（升级或故障），或者不支持NRF发现NSSF时，运营商希望通过AMF本地配置NSSF解析数据，发现和选择NSSF。 

AMF本地配置NSSF解析数据，需要通过NSSF地址解析配置、NSSF服务Profile配置、NSSF地址池配置三个配合。 




功能说明 


一个NSSF服务Profile会关联多个IP地址，为了提高配置效率，AMF通过“NSSF地址池配置”把地址列表和地址池标识关联，“NSSF服务Profile配置”中只需要引用相应的地址池标识。 




子主题： 






#### 增加NSSF地址池配置(ADD NSSFLOCALADDRPOOL) 
#### 增加NSSF地址池配置(ADD NSSFLOCALADDRPOOL) 


功能说明 

该命令用于增加一条NSSF地址池配置，配置NSSF的地址。 


注意事项 

一个IP地址只能归属一个地址池标识。 

一个地址池内最多配置16个IP地址。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF地址池标识。
ipAddress|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于配置归属该NSSF地址池的NSSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 必选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置归属该NSSF地址池的NSSF的端口号。




命令举例 


`
增加NSSF地址池配置，地址池标识符为1，NSSF的IP地址为“12.12.12.12”，端口号为8080。
ADD NSSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",Port=8080
` 


#### 删除NSSF地址池配置(DEL NSSFLOCALADDRPOOL) 
#### 删除NSSF地址池配置(DEL NSSFLOCALADDRPOOL) 


功能说明 

该命令用于删除一条NSSF地址池配置。 


注意事项 

本命令执行后，可能导致AMF与NSSF断链，AMF会启用NSSF容灾后选择NRF发现AMF，可能会影响到5G间AMF重定向流程的成功率。 

如果因为规划改变或其他原因，需要删除错误或多余的配置，请先确保：1、通过ADD NSSFLOCALADDRPOOL命令添加正确的地址池；2、通过ADD NSSFPROFILECFG命令或ADD NSSFSERPROFILECFG命令，关联到该地址池标识。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF地址池标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置归属该NSSF地址池的NSSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置归属该NSSF地址池的NSSF的端口号。




命令举例 


`
删除NSSF地址池配置，地址池标识符为1，NSSF的IP地址为“12.12.12.12”，端口号为8080。
DEL NSSFLOCALADDRPOOL:ADDRPOOLID=1,IPADDRESS="12.12.12.12",Port=8080
` 


#### 查询NSSF地址池配置(SHOW NSSFLOCALADDRPOOL) 
#### 查询NSSF地址池配置(SHOW NSSFLOCALADDRPOOL) 


功能说明 

该命令用于查询NSSF地址池配置。可单条查询和全部查询。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF地址池标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置归属该NSSF地址池的NSSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置归属该NSSF地址池的NSSF的端口号。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置NSSF地址池标识。
ipAddress|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于配置归属该NSSF地址池的NSSF的IP地址，地址格式可以为IPv4或IPv6。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置归属该NSSF地址池的NSSF的端口号。




命令举例 


`
查询地址池标识符为1的NSSF地址池配置。
SHOW NSSFLOCALADDRPOOL:ADDRPOOLID=1

(No.1) : SHOW NSSFLOCALADDRPOOL:ADDRPOOLID=1
-----------------Namf_Communication_0----------------
地址池标识   IP地址        端口号
1         12.12.12.12      8080        
记录数：1
执行成功耗时: 0.12 秒

` 


### 号段选择NSSF配置 
### 号段选择NSSF配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个NSSF，主要用于运营商拨测场景。 


 
对于一个新接入网络的NSSF，在此NSSF还没有和NRF建立连接或还没有向NRF注册之前，运维人员需要对此NSSF进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF进行功能测试。 

 
当网络中的某个NSSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF，进行测试。 

 




功能说明 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入的NSSF，主要用于运营商拨测场景。 

终端发起初始注册请求等业务流程，AMF选择目标NSSF时，首先根据终端用户的GPSI/SUPI号码号段选择目标NSSF，在选择失败的情况下，后续再重新通过到NRF获取或根据本地的配置数据这两种方式发现目标NSSF。 




子主题： 






#### 基于号段选择NSSF策略 
#### 基于号段选择NSSF策略 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个NSSF，主要用于运营商拨测场景。 


 
对于一个新接入网络的NSSF，在此NSSF还没有和NRF建立连接或还没有向NRF注册之前，运维人员需要对此NSSF进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF进行功能测试。 

 
当网络中的某个NSSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，AMF根据用户GPSI/SUPI号码选择接入的NSSF。 

本功能用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个NSSF。 




子主题： 






##### 设置基于号段选择NSSF策略(SET SELECTNSSFPOLICY) 
##### 设置基于号段选择NSSF策略(SET SELECTNSSFPOLICY) 


功能说明 

该命令用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入指定的NSSF。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supnssfnumsel|支持基于号段选择NSSF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个NSSF。修改影响：修改参数为支持时，影响如下。AMF在选择NSSF时，首先根据用户的GPSI/SUPI号段选择NSSF，如果根据用户的GPSI/SUPI号段，不能匹配到对应的NSSF，后续再重新通过到NRF获取或本地配置数据发现NSSF。数据来源：本端配置。配置原则：本参数需要根据运营商拨测场景进行配置。运维人员需要对新接入网络的NSSF进行功能测试，在NSSF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF进行功能测试。当网络中的某个NSSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF，进行测试。




命令举例 


`
设置支持基于号段选择NSSF。
SET SELECTNSSFPOLICY:supnssfnumsel="SPRT"
` 


##### 查询基于号段选择NSSF策略(SHOW SELECTNSSFPOLICY) 
##### 查询基于号段选择NSSF策略(SHOW SELECTNSSFPOLICY) 


功能说明 

该命令用于查询AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入指定的NSSF。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
supnssfnumsel|支持基于号段选择NSSF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个NSSF。修改影响：修改参数为支持时，影响如下。AMF在选择NSSF时，首先根据用户的GPSI/SUPI号段选择NSSF，如果根据用户的GPSI/SUPI号段，不能匹配到对应的NSSF，后续再重新通过到NRF获取或本地配置数据发现NSSF。数据来源：本端配置。配置原则：本参数需要根据运营商拨测场景进行配置。运维人员需要对新接入网络的NSSF进行功能测试，在NSSF还没有和NRF建立连接或还没有向NRF注册之前，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF进行功能测试。当网络中的某个NSSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF，进行测试。




命令举例 


`
查询基于号段选择NSSF策略配置。
SHOW SELECTNSSFPOLICY

(No.1) : SHOW SELECTNSSFPOLICY:
-----------------Namf_Communication_0_A----------------
支持基于号段选择NSSF
不支持
记录数：1

执行成功开始时间:2020-05-29 16:32:49 耗时: 0.436 秒

` 


#### 基于号段选择NSSF配置 
#### 基于号段选择NSSF配置 


背景知识 


AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到哪个NSSF，主要用于运营商拨测场景。 


 
对于一个新接入网络的NSSF，在此NSSF还没有和NRF建立连接或还没有向NRF注册之前，运维人员需要对此NSSF进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF进行功能测试。 

 
当网络中的某个NSSF可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户接入到该NSSF，进行测试。 

 




功能说明 


终端发起初始注册请求等业务流程，AMF根据用户GPSI/SUPI号码选择拨测的NSSF网元。 

本配置提供基于GPSI/SUPI号段解析NSSF的配置数据以及其有效时长。 




子主题： 






##### 新增基于号段选择NSSF配置(ADD SELECTNSSFCFG) 
##### 新增基于号段选择NSSF配置(ADD SELECTNSSFCFG) 


功能说明 

该命令用于新增AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到指定NSSF的相关配置数据，使得拨测场景配置号段下的测试用户能够选择到指定的NSSF。 


注意事项 

如果需要在基于GPSI/SUPI号段选择NSSF的配置数据中配置地址池，必须确保已经通过[ADD NSSFLOCALADDRPOOL]命令配置NSSF地址池。可以通过[SHOW NSSFLOCALADDRPOOL]命令查询已配置的NSSF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置NSSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，不能单独修改，必须全网统一规划，确保没有重复。数据来源：全网规划。默认值：无。配置原则：1. 采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node"。只能为a-f、0-9的字符。2. nfInstanceId不允许从有效设为无效。3. 同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|NSSF FQDN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置NSSF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD NSSFLOCALADDRPOOL命令配置NSSF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置NSSF Profile对应的优先级。修改影响：当根据号段匹配到多个NSSF Profile时，根据优先级高低选择其中的一个NSSF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置NSSF Profile对应的权重。修改影响：当根据号段匹配到多个NSSF Profile并且各个NSSF Profile的优先级相同时，根据权重选择其中的一个NSSF Profile。优先选择权重最大的NSSF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置NSSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置NSSF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 0-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配NSSF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析一直有效。




命令举例 


`
新增一条基于GPSI/SUPI号段解析NSSF配置，其中，用户号码为13895122456，号码类型为GPSI，NSSF FQDN为zte.com.cn，优先级为1，权重为10，URI scheme为HTTP，API版本为V1，有效时间到2021年6月2日11点20分30秒。
ADD SELECTNSSFCFG:number="138951222456",numtype="GPSI",fqdn="zte.com.cn",ippoolid=1,priority=1,weight=10,scheme="HTTP",apiversion="V1",validitytime="2021-6-2 11:20:30"
` 


##### 修改基于号段选择NSSF配置(SET SELECTNSSFCFG) 
##### 修改基于号段选择NSSF配置(SET SELECTNSSFCFG) 


功能说明 

该命令用于修改AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到指定NSSF的相关配置数据，使得拨测场景配置号段下的测试用户能够选择到指定的NSSF。 


注意事项 

如果需要在基于GPSI/SUPI号段选择NSSF的配置数据中配置地址池，必须确保已经通过[ADD NSSFLOCALADDRPOOL]命令配置NSSF地址池。可以通过[SHOW NSSFLOCALADDRPOOL]命令查询已配置的NSSF地址池。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置NSSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，不能单独修改，必须全网统一规划，确保没有重复。数据来源：全网规划。默认值：无。配置原则：1. 采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node"。只能为a-f、0-9的字符。2. nfInstanceId不允许从有效设为无效。3. 同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|NSSF FQDN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置NSSF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD NSSFLOCALADDRPOOL命令配置NSSF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置NSSF Profile对应的优先级。修改影响：当根据号段匹配到多个NSSF Profile时，根据优先级高低选择其中的一个NSSF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置NSSF Profile对应的权重。修改影响：当根据号段匹配到多个NSSF Profile并且各个NSSF Profile的优先级相同时，根据权重选择其中的一个NSSF Profile。优先选择权重最大的NSSF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置NSSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置NSSF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 0-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配NSSF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析一直有效。




命令举例 


`
修改一条基于GPSI/SUPI号段解析NSSF配置，其中，用户号码为13895122456，号码类型为GPSI，NSSF FQDN为zte.com.cn，优先级为1，权重为10，URI scheme为HTTP，API版本为V1，有效时间到2021年6月2日11点20分30秒。
SET SELECTNSSFCFG:number="138951222456",numtype="GPSI",fqdn="zte.com.cn",ippoolid=1,priority=1,weight=10,scheme="HTTP",apiversion="V1",validitytime="2021-6-2 11:20:30"
` 


##### 删除基于号段选择NSSF配置(DEL SELECTNSSFCFG) 
##### 删除基于号段选择NSSF配置(DEL SELECTNSSFCFG) 


功能说明 

该命令用于删除AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到指定NSSF的相关配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
fqdn|NSSF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。




命令举例 


`
删除一条基于GPSI/SUPI号段解析NSSF配置，其中，用户号码为13895122456，号码类型为GPSI，NSSF FQDN为zte.com.cn。
DELETE SELECTNSSFCFG:number="138951222456",numtype="GPSI",fqdn="zte.com.cn"
` 


##### 查询基于号段选择NSSF配置(SHOW SELECTNSSFCFG) 
##### 查询基于号段选择NSSF配置(SHOW SELECTNSSFCFG) 


功能说明 

该命令用于查询AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择接入到指定NSSF的相关配置数据。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
fqdn|NSSF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型，可以配置为GPSI（Generic Public Subscription Identifier，一般公共用户标识）或者SUPI（Subscriber Permanent Identifier，用户永久标识）。修改影响：通过SET SELECTNSSFPOLICY命令开启AMF支持基于号段选择NSSF后，AMF在选择NSSF时，会先根据配置的号段选择NSSF，该字段和号码类型作为非唯一索引，可以确定一组或多组号段地址解析，如果即配置了SUPI号段，也配置了GPSI号段，则GPSI号段的优先级高于SUPI号段的优先级，如果配置的号码类型相同，则相同的号码类型中，号段越长的优先级越高。数据来源：本端规划。默认值：无。配置原则：无。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-36|参数作用：该参数用于设置NSSF网元的标识符，依据网络规划配置。修改影响：nfInstanceId是一个网元的唯一标识符，不能单独修改，必须全网统一规划，确保没有重复。数据来源：全网规划。默认值：无。配置原则：1. 采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。2. nfInstanceId不允许从有效设为无效。3. 同类型NF本地解析配置中，nfInstanceId不允许重复。
fqdn|NSSF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置NSSF Profile对应的域名，即NSSF的域名。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个Profile下只能输入一个域名，域名只支持小写输入。
ippoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置NSSF Profile对应的地址池标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：设置本参数前，必须先通过ADD NSSFLOCALADDRPOOL命令配置NSSF的地址池。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置NSSF Profile对应的优先级。修改影响：当根据号段匹配到多个NSSF Profile时，根据优先级高低选择其中的一个NSSF，优先级数字越小，优先级越高。数据来源：本端规划。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置NSSF Profile对应的权重。修改影响：当根据号段匹配到多个NSSF Profile并且各个NSSF Profile的优先级相同时，根据权重选择其中的一个NSSF Profile。优先选择权重最大的NSSF Profile。数据来源：本端规划。默认值：200。配置原则：无。
scheme|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：该参数用于设置NSSF Profile对应的URI scheme。修改影响：无。数据来源：本端规划。默认值：HTTP。配置原则：无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：该参数用于设置NSSF Profile对应的API版本。修改影响：无。数据来源：本端规划。默认值：V1。配置原则：无。
validitytime|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 0-30|参数作用：该参数用于设置本号段解析配置的有效截止日期。修改影响：当有效截止日期到期后，AMF不再依据此号段解析配置匹配NSSF Profile。数据来源：本端规划。默认值：无。配置原则：输入标准的年月日时分秒格式的时间，比如2020-01-20 11:16:38。有效时间为空，表示号段解析一直有效。




命令举例 


`
查询所有基于GPSI/SUPI号段解析NSSF配置。
SHOW SELECTNSSFCFG

(No.9) : SHOW SELECTNSSFCFG:
-----------------Namf_Communication_0_A----------------
用户号码   号码类型    NF实例标识                               NSSF FQDN   地址池标识 优先级 权重  URI scheme API版本  有效时间
86138138  GPSI      11111111-7dec-11d0-a765-111111111110    zte.com.cn  1         1    100   HTTP       V1版本   2021-6-2 11:20:30
记录数：1

执行成功开始时间:2021-06-01 10:18:22 耗时: 0.353 秒

` 


## 5G-EIR本地解析配置 
## 5G-EIR本地解析配置 


背景知识 


UE在注册时，AMF可以向5G-EIR发起对用户终端的合法性检查。AMF通过本地解析，发现和选择5G-EIR进行通讯。 




功能说明 


5G-EIR本地解析配置用于配置5G-EIR的IP地址、端口号等，便于AMF和其对接。 




子主题： 






### 默认5G-EIR配置 
### 默认5G-EIR配置 


背景知识 


AMF开启PEI检查功能后，需要和5G-EIR网元对接，AMF需要发现5G-EIR网元。AMF支持通过本地配置发现5G-EIR网元，当前只支持本地配置发现一个5G-EIR网元。 




功能说明 


本节点用于配置本地发现5G-EIR网元，即本地配置5G-EIR网元的IP地址、端口号等，以便AMF采用HTTP协议和5G-EIR进行交互。 

AMF本地配置发现5G-EIR，当前只支持配置一个5G-EIR，系统默认存在一条5G-EIR网元数据，该数据仅仅只是示例，不能直接和5G-EIR对接。现网需要获取到5G-EIR的真实数据(IP地址、端口号等)，使用本节点修改配置为该真实数据，且将"是否启用"设置为"启用"，才可以和5G-EIR对接。 




子主题： 






#### 修改默认5G-EIR配置(SET DFT 5G EIR CONFIG) 
#### 修改默认5G-EIR配置(SET DFT 5G EIR CONFIG) 


功能说明 

该命令用于修改默认5G-EIR配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
enable|是否启用|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DISABLE|参数作用：此参数用于控制AMF是否可以启用默认5G-EIR配置。 0：不启用1：启用修改影响：修改此参数，影响AMF是否可以使用默认5G-EIR的配置信息。 数据来源：本端规划。 默认值：0-不启用。配置原则： 无。
ipaddress|IP地址|参数可选性: 任选参数类型: 字符串|参数作用：此参数用于设置AMF对应的默认5G-EIR的IP地址，地址格式可以为IPv4或IPv6。修改影响：修改此参数，影响AMF使用的默认5G-EIR的IP地址信息。 数据来源：本端规划。 默认值：无。配置原则： 无。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|参数作用：此参数用于设置AMF对应的默认5G-EIR的端口号。修改影响：修改此参数，影响AMF使用的默认5G-EIR的端口号取值。 数据来源：本端规划。 默认值：8080。配置原则： 无。
urischema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：此参数用于设置AMF对应的默认5G-EIR的URI scheme。比如 "http"、"https"。修改影响：修改此参数，影响AMF使用的默认5G-EIR的URI scheme取值。 数据来源：本端规划。 默认值：0-HTTP。配置原则： 无。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：此参数用于设置默认5G-EIR的API版本，比如v1或v2。修改影响：修改此参数，影响AMF使用的默认5G-EIR的API版本e取值。 数据来源：本端规划。 默认值：0-V1。配置原则： 无。




命令举例 


`
设置默认5G-EIR的IP地址为“10.10.10.10”，端口号为8088。
SET DFT 5G EIR CONFIG:IPADDRESS="10.10.10.10",port=8088
` 


#### 查询默认5G-EIR配置(SHOW DFT 5G EIR CONFIG) 
#### 查询默认5G-EIR配置(SHOW DFT 5G EIR CONFIG) 


功能说明 

该命令用于查询默认5G-EIR配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
enable|是否启用|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DISABLE|参数作用：此参数用于控制AMF是否可以启用默认5G-EIR配置。 0：不启用1：启用
ipaddress|IP地址|参数可选性: 任选参数类型: 字符串|参数作用：此参数用于设置AMF对应的默认5G-EIR的IP地址，地址格式可以为IPv4或IPv6。修改影响：修改此参数，影响AMF使用的默认5G-EIR的IP地址信息。 数据来源：本端规划。 默认值：无。配置原则： 无。
port|端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|参数作用：此参数用于设置AMF对应的默认5G-EIR端口号。
urischema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|参数作用：此参数用于设置AMF对应的默认5G-EIR的URI scheme。比如 "http"、"https"。
apiversion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|参数作用：此参数用于设置默认5G-EIR的API版本，比如v1或v2。




命令举例 


`
查询默认5G-EIR配置。
SHOW DFT 5G EIR CONFIG

(No.13) : SHOW DFT 5G EIR CONFIG:
-----------------Namf_Communication_0----------------
操作维护       是否启用 IP地址      端口号 URI scheme API版本 
--------------------------------------------------------------
修改           不启用   10.10.10.10 8088   http       v1      
--------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-28 15:51:02 耗时: 0.183 秒

` 


# NF发现默认HTTP端口号配置 
# NF发现默认HTTP端口号配置 


背景知识 


AMF通过NRF发现或本地解析发现NF时，有些场景下无法获取端口号。 


 
NRF返回IP地址时未返回端口号； 

 
NRF或者本地解析返回FQDN而非IP地址，AMF使用FQDN查询DNS，DNS查询无法获取端口号。 

 




功能说明 


NF发现默认HTTP端口号配置。 




子主题： 






## 修改NF发现默认HTTP端口号配置(SET NFDISDEFHTTPPORT CONFIG) 
## 修改NF发现默认HTTP端口号配置(SET NFDISDEFHTTPPORT CONFIG) 


功能说明 

该命令用于修改NF发现默认HTTP端口号配置。 

5G内NF发现通过NRF进行，如果NRF返回的NF信息响应中不包含IP地址和端口属性，应使用FQDN属性值进行DNS查询。如果在DNS查询期间未收到端口号，则应使用默认HTTP端口号。 

目前仅DNS查询不返回端口号时使用。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
defaultHttpPort|默认http端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 80|该参数用于设置NF发现的默认http端口号。
defaultHttpsPort|默认https端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 443|该参数用于设置NF发现的默认https端口号。




命令举例 


`
设置NF发现默认http端口号为80，默认https端口号为443。
SET NFDISDEFHTTPPORT CONFIG:DEFAULTHTTPPORT=80,DEFAULTHTTPSPORT=443
` 


## 查询NF发现默认HTTP端口号配置(SHOW NFDISDEFHTTPPORT CONFIG) 
## 查询NF发现默认HTTP端口号配置(SHOW NFDISDEFHTTPPORT CONFIG) 


功能说明 

该命令用于查询NF发现默认HTTP端口号配置。 


注意事项 

无。 


输出参数说明 


标识|名称|类型|说明
---|---|---|---
defaultHttpPort|默认http端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 80|该参数用于显示NF发现的默认http端口号。
defaultHttpsPort|默认https端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 443|该参数用于设置NF发现的默认https端口号。




命令举例 


`
查询NF发现默认HTTP端口号。
SHOW NFDISDEFHTTPPORT CONFIG

(No.2) : SHOW NFDISDEFHTTPPORT CONFIG:
-----------------Namf_Communication_0----------------
操作维护       默认http端口号 默认https端口号 
----------------------------------------------
修改           80             443             
----------------------------------------------

` 


# NF选择策略配置 
# NF选择策略配置 


背景知识 


通常，与AMF交互的各类NF，会提供两种类型的IP地址，IPv4和IPv6，AMF需要选择一种类型的IP地址进行NF间的通信。 

AMF选择根据静态权重，选择NF的算法有两种：随机选择算法和轮循选择算法。 




功能说明 


NF选择策略配置提供地址类型选择策略和等价NF选择策略的配置。 




子主题： 






## 地址类型选择策略配置 
## 地址类型选择策略配置 


背景知识 


5GC网络中的各个NF提供了两种类型的IP地址，IPv4和IPv6，需要选择一种类型的IP地址进行NF间的通信 。 




功能说明 


本功能用于配置各NF通信的IP地址类型，可以选择IPv4或IPv6，默认是IPv4。 




子主题： 






### 修改NF地址选择策略配置(SET NFADDRCHOICEPOLICYCFG) 
### 修改NF地址选择策略配置(SET NFADDRCHOICEPOLICYCFG) 


功能说明 

该命令用于配置或修改每个NF的IP地址选择策略。当NF部署成功时，需要此命令设置各个NF的IP地址选择策略，可以选择IPv4和IPv6。当NF的选择策略发生变化，也可以使用此命令进行修改。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
smfAddrChoicePolicy|SMF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置SMF的IP地址选择策略。
pcfAddrChoicePolicy|PCF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置PCF的IP地址选择策略。
udmAddrChoicePolicy|UDM地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置UDM的IP地址选择策略。
ausfAddrChoicePolicy|AUSF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置AUSF的IP地址选择策略。
amfAddrChoicePolicy|AMF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置AMF的IP地址选择策略。
smsfAddrChoicePolicy|SMSF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置SMSF的IP地址选择策略。
nssfAddrChoicePolicy|NSSF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置NSSF的IP地址选择策略。




命令举例 


`
设置各NF的IP地址选择策略。
SET NFADDRCHOICEPOLICYCFG:SMFADDRCHOICEPOLICY="IPV4",PCFADDRCHOICEPOLICY="IPV4",UDMADDRCHOICEPOLICY="IPV4",AUSFADDRCHOICEPOLICY="IPV4",AMFADDRCHOICEPOLICY="IPV4",SMSFADDRCHOICEPOLICY="IPV4",NSSFADDRCHOICEPOLICY="IPV4"
` 


### 查询NF地址选择策略配置(SHOW NFADDRCHOICEPOLICYCFG) 
### 查询NF地址选择策略配置(SHOW NFADDRCHOICEPOLICYCFG) 


功能说明 

该命令用于查询所有NF的IP地址选择策略。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
smfAddrChoicePolicy|SMF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置SMF的IP地址选择策略。
pcfAddrChoicePolicy|PCF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置PCF的IP地址选择策略。
udmAddrChoicePolicy|UDM地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置UDM的IP地址选择策略。
ausfAddrChoicePolicy|AUSF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置AUSF的IP地址选择策略。
amfAddrChoicePolicy|AMF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置AMF的IP地址选择策略。
smsfAddrChoicePolicy|SMSF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置SMSF的IP地址选择策略。
nssfAddrChoicePolicy|NSSF地址选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|该参数用于设置NSSF的IP地址选择策略。




命令举例 


`
查询各NF的IP地址选择策略。
SHOW NFADDRCHOICEPOLICYCFG:

(No.1) : SHOW NFADDRCHOICEPOLICYCFG:
-----------------Namf_Communication_0----------------
SMF地址选择策略  PCF地址选择策略 UDM地址选择策略 AUSF地址选择策略 AMF地址选择策略 SMSF地址选择策略  NSSF地址选择策略
IPV4                    IPV4          IPV4            IPV4           IPV4         IPV4             IPV4
记录数：1

执行成功耗时: 1.298 秒

` 


## 等价NF选择策略配置 
## 等价NF选择策略配置 


背景知识 


在5G某些业务流程中，AMF和NF之间存在消息交互，AMF通过NRF发现可用的NF，NRF会根据AMF提供的发现参数，向AMF返回所有满足条件的NF，此时，AMF需要根据一定的选择策略，选择其中一个NF进行业务交互。 




功能说明 


本功能用于设置等价NF选择策略，当AMF向NRF发现多个NF后，AMF可以依据权重负荷值进行算法选择，从中选出一个可用的NF。 




子主题： 






### 修改NF选择策略配置(SET NFSELECTPOLICY) 
### 修改NF选择策略配置(SET NFSELECTPOLICY) 


功能说明 

本命令用于设置或修改AMF选择NF的策略，包括随机选择和轮询选择两种算法。 


注意事项 

建议设置为随机选择算法。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
smfSelectPolicy|SMF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个SMF后的选择策略。
pcfSelectPolicy|PCF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个PCF后的选择策略。
udmSelectPolicy|UDM选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个UDM后的选择策略。
ausfSelectPolicy|AUSF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个AUSF后的选择策略。
amfSelectPolicy|AMF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个AMF后的选择策略。
smsfSelectPolicy|SMSF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个SMSF后的选择策略。
nssfSelectPolicy|NSSF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个NSSF后的选择策略。




命令举例 


`
设置SMF选择策略为轮询，PCF选择策略为随机。
SET NFSELECTPOLICY:SMFSELECTPOLICY="NFPOLLINGSELECT",PCFSELECTPOLICY="NFRANDSELECT"
` 


### 查询NF选择策略配置(SHOW NFSELECTPOLICY) 
### 查询NF选择策略配置(SHOW NFSELECTPOLICY) 


功能说明 

本命令用于查询AMF选择NF的策略。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
smfSelectPolicy|SMF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个SMF后的选择策略。
pcfSelectPolicy|PCF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个PCF后的选择策略。
udmSelectPolicy|UDM选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个UDM后的选择策略。
ausfSelectPolicy|AUSF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个AUSF后的选择策略。
amfSelectPolicy|AMF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个AMF后的选择策略。
smsfSelectPolicy|SMSF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个SMSF后的选择策略。
nssfSelectPolicy|NSSF选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NFRANDSELECT|该参数用于设置AMF发现多个NSSF后的选择策略。




命令举例 


`
查询NF选择策略。
SHOW NFSELECTPOLICY:

(No.1) : SHOW NFSELECTPOLICY:
-----------------Namf_Communication_0----------------
SMF选择策略 PCF选择策略 UDM选择策略 AUSF选择策略 AMF选择策略 SMSF选择策略   NSSF选择策略
轮询选择    随机选择    随机选择    随机选择     随机选择    随机选择       随机选择
记录数：1
执行成功耗时: 0.078 秒

` 


# SMF选择配置 
# SMF选择配置 


背景知识 


当终端接入到5G网络，在PDU会话建立流程中，AMF需要通过DNN来选择合适的SMF，涉及到的流程如下。 


 
如果终端的请求消息中没有携带的DNN，且在终端的签约信息中，该终端的S-NSSAI下也不存在default DNN，可以使用本AMF配置的缺省DNN。 

 
如果终端的请求消息中携带的DNN不合法，AMF可以通过本AMF的配置数据，按运营商策略更正为其他DNN，后续终端会使用更正后的DNN，来选择SMF，建立PDU会话。 

 




功能说明 


SMF选择配置提供DNN更正配置，更正方式包括：指定DNN和签约的默认DNN。 




子主题： 






## A-SMF选择配置 
## A-SMF选择配置 


背景知识 


 当终端接入到5G网络，在PDU会话建立流程中，AMF需要通过DNN来选择合适的A-SMF。为此，AMF先选择切片，然后基于选择的切片选择DNN。涉及到的流程如下： 

如果终端的请求消息中携带切片，切片若不在允许访问切片范围内，AMF拒绝PDU会话建立；切片若在允许访问切片范围内时： 


 
如果终端的请求消息中没有携带的DNN，且在终端的签约信息中，该终端的S-NSSAI下也不存在default DNN，可以使用本AMF配置的缺省DNN。 

 
如果终端的请求消息中携带的DNN不合法，AMF可以通过本AMF的配置数据，按运营商策略更正为其他DNN，后续终端会使用更正后的DNN，来选择A-SMF，建立PDU会话。 

 

如果终端的请求消息中没有携带切片和DNN，AMF可以通过本AMF的配置数据，按运营商策略选择一个切片。如果选择的切片下不存在default DNN，可以使用本AMF配置的DNN。 

如果终端的请求消息中携带DNN没有携带切片，AMF可以通过本AMF的配置数据，按运营商策略选择一个切片。如果携带的DNN不合法，AMF可以通过本AMF的配置数据，按运营商策略更正为其他DNN，后续终端会使用更正后的DNN，来选择A-SMF，建立PDU会话。 




功能说明 


A-SMF选择配置包括： 


 
A-SMF选择策略配置 

 
切片选择策略配置 

 
DNN更正配置 

 
缺省DNN配置 

 




子主题： 






### A-SMF选择策略配置 
### A-SMF选择策略配置 


背景知识 


AMF在进行会话建立时，需要和SMF交互，运营商一般会根据地理位置、SMF服务能力部署不同的SMF来提供服务，AMF在会话建立时需要选择合适的SMF。 

 进行SMF选择时，AMF可以提供一些选择策略。 

目前选择策略有A-SMF选择是否支持优选TA，和是否支持同DNN的多PDU选择同一个SMF两种策略。 




功能说明 


SMF策略配置提供A-SMF选择支持优选TA策略和同DNN的多PUD选择同一个SMF两种策略。 

A-SMF选择支持优选TA策略: 


 
当支持A-SMF选择支持优选TA策略时，在NRF不支持优先TA特性情况下，AMF在NRF返回的SMF列表中优先匹配UE TA的SMF列表，再根据权重优先级选择。 

 
当不支持A-SMF选择支持优选TA策略时，AMF对NRF返回的SMF列表根据权重优先级选择。 

 

同DNN的多PUD选择同一个SMF： 


 
当支持同DNN的多PDU选择同一个SMF时，DNN相同的不同PDU建立过程会选择相同的SMF。 

 
当不支持同DNN的多PDU选择同一个SMF时，DNN相同的不同PDU建立过程各自选择SMF。 

 




子主题： 






#### 修改 A-SMF选择策略配置(SET ASMFSELPOLICY) 
#### 修改 A-SMF选择策略配置(SET ASMFSELPOLICY) 


功能说明 

该命令用于设置A-SMF选择策略配置。 


注意事项 

该命令执行后立即生效。 

无感分流专用SMF失败重选开关关闭时，无感分流用户只能选择专用SMF进行会话的建立。如果候选的SMF中没有专用的SMF，则会PDU建立失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
amfSelASmfByTa|A-SMF选择支持优选TA|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置A-SMF选择是否支持优选TA当支持时，在NRF不支持优先TA特性情况下，AMF在NRF返回的SMF列表中优先匹配UE TA的SMF列表，再根据权重优先级选择当不支持时，AMF对NRF返回的SMF列表根据权重优先级选择。
amfSelSameASmfByDnn|支持相同DNN的多PDU会话选择同一个A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于显示是否支持同DNN的多PDU选择同一个SMF当支持时，DNN相同的不同PDU建立过程会选择相同的SMF当不支持时，DNN相同的不同PDU建立过程各自选择SMF。
supSameSmfDiffDnn|支持不同DNN的多PDU会话选择同一个A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置是否支持不同DNN的多PDU选择同一个SMF当支持时，不同DNN的不同PDU建立过程会选择相同的SMF当不支持时，不同DNN的不同PDU建立过程各自选择SMF。
supSelSmfBySubSmfId|支持基于签约SMF ID选择A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置是否支持基于签约SMF ID选择SMF当支持时，会基于UDM签约的SMF ID通过NRF发现获取到A-SMF列表当不支持时，不会基于UDM签约的SMF ID来选择SMF
reSelSmfBySubSmfid|基于签约SMF ID选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置基于签约SMF ID选择失败后是否重选A-SMF当支持时，基于签约SMF ID选择失败后会基于DNN重选SMF当不支持时，基于签约SMF ID选择失败后不会重选SMF。
supseldedsmf|支持选择无感分流专用SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置是否支持选择无感分流专用SMF。修改影响：设置为支持，则AMF在NRF返回的SMF列表中，为签约了专用DNN且有无感分流需求的用户优先选择无感分流专用SMF。数据来源：本端规划。默认值：不支持。配置原则：“支持选择无感分流专用SMF”仅在License项“AMF支持网络侧多DNN会话功能”打开时才生效。
reselifdedsmffail|选择无感分流专用SMF失败是否重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于设置是否支持在选择无感分流专用SMF失败时进行重选。修改影响：如果无感分流专用SMF均不可用，设置为否，则SMF选择失败；设置为是，则在过滤后的普通SMF列表中执行SMF选择，选择到普通SMF。数据来源：本端规划。默认值：是。配置原则：“支持选择无感分流专用SMF”仅在License项“AMF支持网络侧多DNN会话功能”打开时才生效。




命令举例 


`
设置或修改A-SMF选择策略。
SET ASMFSELPOLICY:AMFSELASMFBYTA="NOTSUPPORT",AMFSELSAMEASMFBYDNN="NOTSUPPORT",SUPSAMESMFDIFFDNN="NOTSUPPORT",SUPSELSMFBYSUBSMFID="NOTSUPPORT",RESELSMFBYSUBSMFID="YES",SUPSELDEDSMF="NOTSUPPORT",RESELIFDEDSMFFAIL="YES"
` 


#### 查询 A-SMF选择策略配置(SHOW ASMFSELPOLICY) 
#### 查询 A-SMF选择策略配置(SHOW ASMFSELPOLICY) 


功能说明 

该命令用于查询A-SMF选择策略配置。 


注意事项 

无


输出参数说明 


标识|名称|类型|说明
---|---|---|---
amfSelASmfByTa|A-SMF选择支持优选TA|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于显示A-SMF选择是否支持优选TA当支持时，在NRF不支持优先TA特性情况下，AMF在NRF返回的SMF列表中优先匹配UE TA的SMF列表，再根据权重优先级选择当不支持时，AMF对NRF返回的SMF列表根据权重优先级选择。
amfSelSameASmfByDnn|支持相同DNN的多PDU会话选择同一个A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于显示是否支持同DNN的多PDU选择同一个SMF当支持时，DNN相同的不同PDU建立过程会选择相同的SMF当不支持时，DNN相同的不同PDU建立过程各自选择SMF。
supSameSmfDiffDnn|支持不同DNN的多PDU会话选择同一个A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置是否支持不同DNN的多PDU选择同一个SMF当支持时，不同DNN的不同PDU建立过程会选择相同的SMF当不支持时，不同DNN的不同PDU建立过程各自选择SMF。
supSelSmfBySubSmfId|支持基于签约SMF ID选择A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置是否支持基于签约SMF ID选择SMF当支持时，会基于UDM签约的SMF ID通过NRF发现获取到A-SMF列表当不支持时，不会基于UDM签约的SMF ID来选择SMF
reSelSmfBySubSmfid|基于签约SMF ID选择失败后是否重选A-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置基于签约SMF ID选择失败后是否重选A-SMF当支持时，基于签约SMF ID选择失败后会基于DNN重选SMF当不支持时，基于签约SMF ID选择失败后不会重选SMF。
supseldedsmf|支持选择无感分流专用SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置是否支持选择无感分流专用SMF。
reselifdedsmffail|选择无感分流专用SMF失败是否重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置是否支持在选择无感分流专用SMF失败时进行重选。




命令举例 


`
查询A-SMF选择策略。 
SHOW ASMFSELPOLICY:

(No.1) : SHOW ASMFSELPOLICY:
-----------------Namf_Communication_0----------------
操作维护       A-SMF选择支持优选TA 支持相同DNN的多PDU会话选择同一个A-SMF 支持不同DNN的多PDU会话选择同一个A-SMF 支持基于签约SMF ID选择A-SMF 基于签约SMF ID选择失败后是否重选A-SMF 支持选择无感分流专用SMF 选择无感分流专用SMF失败是否重选
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           不支持              不支持                                不支持                                不支持                      是                                    不支持                  是
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-02-03 15:27:22 耗时: 0.128 秒

` 


#### 新增基于SUPI的A-SMF选择策略配置(ADD SUPI ASMFSELPOLICY) 
#### 新增基于SUPI的A-SMF选择策略配置(ADD SUPI ASMFSELPOLICY) 


功能说明 

该命令用于新增基于SUPI的A-SMF选择策略配置。当AMF需要区分不同的SUPI号段和DNN使用不同的A-SMF选择策略时，使用该命令进行配置。 


注意事项 

该命令执行后立即生效。 

AMF可以基于SUPI和/或DNN配置SMF选择策略，优先级顺序从高到低为：SUPI+DNN、SUPI。 

最多配置4096条记录。 

无感分流专用SMF失败重选开关关闭时，无感分流用户只能选择专用SMF进行会话的建立。如果候选的SMF中没有专用的SMF，则会PDU建立失败。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100默认值: NULL|参数作用：此参数用于设置需要被匹配的用户DNN，AMF支持根据用户的DNN来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN只支持输入小写。
supseldedsmf|支持选择无感分流专用SMF|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置是否支持选择无感分流专用SMF。修改影响：设置为支持，则AMF在NRF返回的SMF列表中，为签约了专用DNN且有无感分流需求的用户优先选择无感分流专用SMF。数据来源：本端规划。默认值：不支持。配置原则：“支持选择无感分流专用SMF”仅在License项“AMF支持网络侧多DNN会话功能”打开时才生效。
reselifdedsmffail|选择无感分流专用SMF失败是否重选|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于设置是否支持在选择无感分流专用SMF失败时进行重选。修改影响：如果无感分流专用SMF均不可用，设置为否，则SMF选择失败；设置为是，则在过滤后的普通SMF列表中执行SMF选择，选择到普通SMF。数据来源：本端规划。默认值：是。配置原则：“支持选择无感分流专用SMF”仅在License项“AMF支持网络侧多DNN会话功能”打开时才生效。




命令举例 


`
增加一条基于SUPI号段"46011"和DNN为"zte.com"的A-SMF选择策略配置，不支持选择无感分流专用SMF功能，支持选择无感分流专用SMF失败后重选。
ADD SUPI ASMFSELPOLICY:SUPI="460111",DNN="zte.com",SUPSELDEDSMF="NOTSUPPORT",RESELIFDEDSMFFAIL="YES"
` 


#### 修改基于SUPI的A-SMF选择策略配置(SET SUPI ASMFSELPOLICY) 
#### 修改基于SUPI的A-SMF选择策略配置(SET SUPI ASMFSELPOLICY) 


功能说明 

该命令用于修改基于SUPI的A-SMF选择策略配置。 


注意事项 

该命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100默认值: NULL|参数作用：此参数用于设置需要被匹配的用户DNN，AMF支持根据用户的DNN来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN只支持输入小写。
supseldedsmf|支持选择无感分流专用SMF|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于设置是否支持选择无感分流专用SMF。修改影响：设置为支持，则AMF在NRF返回的SMF列表中，为签约了专用DNN且有无感分流需求的用户优先选择无感分流专用SMF。数据来源：本端规划。默认值：不支持。配置原则：“支持选择无感分流专用SMF”仅在License项“AMF支持网络侧多DNN会话功能”打开时才生效。
reselifdedsmffail|选择无感分流专用SMF失败是否重选|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于设置是否支持在选择无感分流专用SMF失败时进行重选。修改影响：如果无感分流专用SMF均不可用，设置为否，则SMF选择失败；设置为是，则在过滤后的普通SMF列表中执行SMF选择，选择到普通SMF。数据来源：本端规划。默认值：是。配置原则：“支持选择无感分流专用SMF”仅在License项“AMF支持网络侧多DNN会话功能”打开时才生效。




命令举例 


`
修改一条基于SUPI号段"46011"和DNN为"zte.com"的A-SMF选择策略配置，支持选择无感分流专用SMF功能，支持选择无感分流专用SMF失败后重选。
SET SUPI ASMFSELPOLICY:SUPI="460111",DNN="zte.com",SUPSELDEDSMF="SUPPORT",RESELIFDEDSMFFAIL="YES"
` 


#### 删除基于SUPI的A-SMF选择策略配置(DEL SUPI ASMFSELPOLICY) 
#### 删除基于SUPI的A-SMF选择策略配置(DEL SUPI ASMFSELPOLICY) 


功能说明 

该命令用于删除基于SUPI的A-SMF选择策略配置。 


注意事项 

该命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100默认值: NULL|参数作用：此参数用于设置需要被匹配的用户DNN，AMF支持根据用户的DNN来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN只支持输入小写。




命令举例 


`
删除一条基于SUPI号段"46011"和DNN为"zte.com"的A-SMF选择策略配置。
DEL SUPI ASMFSELPOLICY:SUPI="460111",DNN="zte.com"
` 


#### 查询基于SUPI的A-SMF选择策略配置(SHOW SUPI ASMFSELPOLICY) 
#### 查询基于SUPI的A-SMF选择策略配置(SHOW SUPI ASMFSELPOLICY) 


功能说明 

该命令用于查询基于SUPI的A-SMF选择策略配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100默认值: NULL|参数作用：此参数用于设置需要被匹配的用户DNN，AMF支持根据用户的DNN来设置不同的A-SMF选择策略配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN只支持输入小写。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|该参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来设置不同的A-SMF选择策略配置。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100默认值: NULL|该参数用于设置需要被匹配的用户DNN，AMF支持根据用户的DNN来设置不同的A-SMF选择策略配置。DNN只支持输入小写。
supseldedsmf|支持选择无感分流专用SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置是否支持选择无感分流专用SMF。
reselifdedsmffail|选择无感分流专用SMF失败是否重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置是否支持在选择无感分流专用SMF失败时进行重选。




命令举例 


`
查询基于SUPI的A-SMF选择策略配置。
SHOW SUPI ASMFSELPOLICY

(No.4) : SHOW SUPI ASMFSELPOLICY:
-----------------Namf_Communication_0_A----------------
SUPI号段       DNN          支持选择无感分流专用SMF   选择无感分流专用SMF失败是否重选
46011         zte.com       支持                      是
记录数：1

执行成功开始时间:2022-04-28 10:10:44 耗时: 0.277 秒

` 


### 切片选择策略配置 
### 切片选择策略配置 


背景知识 


当终端接入到5G网络，在PDU会话建立流程中，AMF先选择切片，然后基于选择的切片选择DNN。涉及到的流程如下： 


 
如果终端的请求消息中携带切片，切片若不在允许访问切片范围内，AMF拒绝PDU会话建立；切片若在允许访问切片范围内时，AMF使用终端携带的切片。 

 
如果终端的请求消息中没有携带切片和DNN，AMF可以通过本AMF的配置数据，在允许访问切片范围内，按运营商策略选择一个切片。 

 
如果终端的请求消息中携带DNN没有携带切片，AMF可以通过本AMF的配置数据，按运营商策略选择一个切片。当终端未携带请求DNN或者请求DNN没有签约在切片下时，在允许访问切片范围内选择一个切片；当终端携带的请求DNN签约在切片下时，在包含请求DNN的允许访问切片范围内选择一个切片。 

 




功能说明 


切片选择策略配置包括： 


 
缺省切片选择策略配置 

 
切片选择策略配置 

 

切片选择策略，包括如下几种： 


 
指定切片优先：若指定切片在签约信息中（当用户未携带请求DNN或者请求DNN没有签约在切片下时，基于允许访问切片；当用户携带的请求DNN签约在切片下时，基于包含请求DNN的允许访问切片），则使用指定切片；否则继续使用“签约切片”策略。 

 
签约切片：基于签约切片信息（当用户未携带请求DNN或者请求DNN没有签约在切片下时，基于允许访问切片；当户携带的请求DNN签约在切片下时，基于包含请求DNN的允许访问切片），选择合适的切片。如果签约了默认切片，则使用签约的默认切片；如果未签约默认切片，则使用签约的非默认切片。 

 




子主题： 






#### 修改缺省切片选择策略配置(SET DEFAULT SLICE SELECTION POLICY) 
#### 修改缺省切片选择策略配置(SET DEFAULT SLICE SELECTION POLICY) 


功能说明 

该命令用于修改缺省切片选择策略配置。PDU会话建立流程，当用户没有携带切片时，需在AMF中配置切片选择策略。  


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
sliceselpolicy|缺省切片选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ONLYSUBSCRIBEDSNSSAI|目前有2种策略。仅签约切片和指定切片。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
ignorewildcard|忽略通配DNN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTIGNORE|设置是否忽略签约通配DNN。
basednncorrect|支持基于DNN更正策略选择切片|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|设置是否支持基于DNN更正策略选择切片。请求DNN未签约在切片下，且用户未签约通配DNN时，如果该配置设置为支持，则根据DNN更正配置选择合适的切片；如果该配置为不支持，则从用户的Allowed NSSAI列表中选择合适的切片




命令举例 


`
修改缺省切片选择策略为“仅签约切片”，SST为“1-eMBB”，SD为“NULL”，忽略通配DNN, 支持基于DNN更正策略选择切片
SET DEFAULT SLICE SELECTION POLICY:SLICESELPOLICY="ONLYSUBSCRIBEDSNSSAI",SST="eMBB",SD="NULL",IGNOREWILDCARD="IGNORE",BASEDNNCORRECT="YES"
` 


#### 查询缺省切片选择策略配置(SHOW DEFAULT SLICE SELECTION POLICY) 
#### 查询缺省切片选择策略配置(SHOW DEFAULT SLICE SELECTION POLICY) 


功能说明 

该命令用于查询缺省切片选择策略配置。  


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
sliceselpolicy|缺省切片选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ONLYSUBSCRIBEDSNSSAI|目前有2种策略。仅签约切片和指定切片。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
ignorewildcard|忽略通配DNN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTIGNORE|设置是否忽略签约通配DNN。
basednncorrect|支持基于DNN更正策略选择切片|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|设置是否支持基于DNN更正策略选择切片。请求DNN未签约在切片下，且用户未签约通配DNN时，如果该配置设置为支持，则根据DNN更正配置选择合适的切片；如果该配置为不支持，则从用户的Allowed NSSAI列表中选择合适的切片




命令举例 


`
查询缺省切片选择策略配置
SHOW DEFAULT SLICE SELECTION POLICY:

(No.16) :  SHOW DEFAULT SLICE SELECTION POLICY:
-----------------Namf_Communication_0----------------
操作维护       缺省切片选择策略 SST    SD   忽略通配DNN 支持基于DNN更正策略选择切片 
------------------------------------------------------------------------------------
修改           仅签约切片       1-eMBB NULL 忽略        支持                        
------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-12-14 21:31:29 耗时: 0.17 秒

` 


#### 新增切片选择策略配置(ADD SLICE SELECTION POLICY) 
#### 新增切片选择策略配置(ADD SLICE SELECTION POLICY) 


功能说明 

该命令用于增加一个SUPI号段对应的切片选择策略。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置一个特定SUPI号段。
sliceselpolicy|切片选择策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ONLYSUBSCRIBEDSNSSAI|目前有2种策略。仅签约切片和指定切片。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
ignorewildcard|忽略通配DNN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTIGNORE|设置是否忽略签约通配DNN。




命令举例 


`
新增一条切片选择策略。SUPI号段为46011，切片选择策略为仅签约切片，SST为1-eMBB，SD为NULL，不忽略通配DNN。
ADD SLICE SELECTION POLICY:SUPI="46011",SLICESELPOLICY="ONLYSUBSCRIBEDSNSSAI",SST="eMBB",SD="NULL",IGNOREWILDCARD="NOTIGNORE"
` 


#### 修改切片选择策略配置(SET SLICE SELECTION POLICY) 
#### 修改切片选择策略配置(SET SLICE SELECTION POLICY) 


功能说明 

该命令用于修改一个SUPI号段对应的切片选择策略。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置一个特定SUPI号段。
sliceselpolicy|切片选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ONLYSUBSCRIBEDSNSSAI|目前有2种策略。仅签约切片和指定切片。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
ignorewildcard|忽略通配DNN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTIGNORE|设置是否忽略签约通配DNN。




命令举例 


`
修改SUPI号段为46011的切片选择策略。将其策略改为指定切片优先，忽略通配DNN。
SET SLICE SELECTION POLICY:SUPI="46011",SLICESELPOLICY="SPECIFICSNSSAIPRIOR",SD="NULL",IGNOREWILDCARD="IGNORE"
` 


#### 删除切片选择策略配置(DEL SLICE SELECTION POLICY) 
#### 删除切片选择策略配置(DEL SLICE SELECTION POLICY) 


功能说明 

该命令用于删除一个SUPI号段对应的切片选择策略。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置一个特定SUPI号段。




命令举例 


`
删除SUPI号段为123的切片选择策略
DEL SLICE SELECTION POLICY:SUPI=123
` 


#### 查询切片选择策略配置(SHOW SLICE SELECTION POLICY) 
#### 查询切片选择策略配置(SHOW SLICE SELECTION POLICY) 


功能说明 

该命令用于查询一个SUPI号段对应的切片选择策略。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置一个特定SUPI号段。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置一个特定SUPI号段。
sliceselpolicy|切片选择策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ONLYSUBSCRIBEDSNSSAI|目前有2种策略。仅签约切片和指定切片。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
ignorewildcard|忽略通配DNN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTIGNORE|设置是否忽略签约通配DNN。




命令举例 


`
查询当前所有的切片选择策略
SHOW SLICE SELECTION POLICY

(No.5) : SHOW SLICE SELECTION POLICY:
-----------------Namf_Communication_0----------------
操作维护       SUPI号段 切片选择策略 SST    SD   忽略通配DNN 
-------------------------------------------------------------
复制 修改 删除 46011    指定切片优先 1-eMBB NULL 忽略        
-------------------------------------------------------------
记录数：1
执行成功开始时间:2020-12-14 21:36:55 耗时: 0.137 秒

` 


### DNN更正配置 
### DNN更正配置 


背景知识 


5G网络中定义的DNN(Data Network Name，数据网络名称)就是4G网络中定义的APN，这两个标识符具有相同的含义并携带相同的信息（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。 

DNN或APN的组成有两部分： 


 
网络ID，这部分表示一个外部网络，这部分是必选的。 

 
运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。 

 

网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。 

运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。 

当终端接入到5G网络，在PDU会话建立流程中，AMF需要通过DNN来选择合适的SMF，如果终端的请求消息中携带的DNN不合法，AMF可以通过本地的配置数据，按运营商策略更正为其他DNN，后续终端会使用更正后的DNN，来选择SMF，建立PDU会话。 




功能说明 


在PDU会话建立流程中，如果终端在请求消息中，没有携带DNN或者携带的DNN不合法，会导致会话建立流程失败。 

本功能用于设置在会话流程建立过程中，AMF是否支持DNN更正功能，开启该功能后，如果出现上述异常情况，可修改终端的DNN，保证会话流程的正常进行。 




子主题： 






#### 修改DNN更正策略(SET DNNCORRECT POLICY) 
#### 修改DNN更正策略(SET DNNCORRECT POLICY) 


功能说明 

该命令用于设置或修改AMF的DNN更正策略，包括是否支持DNN更正功能、A-SMF发现失败后是否支持DNN更正。  


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
dnnCorrectPolicy|支持DNN更正功能|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPDNNCORRECT|参数作用：该参数用于设置AMF是否支持DNN更正功能，取值及含义如下：支持DNN更正：AMF支持DNN更正功能，即如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。不支持DNN更正：AMF不支持DNN更正功能修改影响：无。数据来源：本端规划。默认值：支持DNN更正。配置原则：无。
supdnncorriffail|A-SMF发现失败后支持DNN更正|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：UE在发起请求建立PDU会话流程中，携带了DNN（此DNN称为请求DNN），同时UE又签约了通配DNN，但是携带的请求DNN未签约，该参数用于设置，当AMF使用UE携带的请求DNN，通过NRF来发现A-SMF失败后，是否会把请求DNN更正为其他签约的DNN，取值及含义如下：支持：当AMF使用UE携带的请求DNN，通过NRF来发现A-SMF失败后，会把请求DNN更正为其他签约的DNN。不支持：当AMF使用UE携带的请求DNN，通过NRF来发现A-SMF失败后，不会把请求DNN更正为其他签约的DNN。修改影响：无。数据来源：本端规划。默认值：支持。配置原则：无。




命令举例 


`
设置AMF的DNN更正策略
SET DNNCORRECT POLICY:DNNCORRECTPOLICY="SUPDNNCORRECT",SUPDNNCORRIFFAIL="SUPPORT"
` 


#### 查询DNN更正策略(SHOW DNNCORRECT POLICY) 
#### 查询DNN更正策略(SHOW DNNCORRECT POLICY) 


功能说明 

该命令用于查询AMF的DNN更正策略。  


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
dnnCorrectPolicy|支持DNN更正功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPDNNCORRECT|参数作用：该参数用于设置AMF是否支持DNN更正功能，取值及含义如下：支持DNN更正：AMF支持DNN更正功能，即如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。不支持DNN更正：AMF不支持DNN更正功能
supdnncorriffail|A-SMF发现失败后支持DNN更正|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：UE在发起请求建立PDU会话流程中，携带了DNN（此DNN称为请求DNN），同时UE又签约了通配DNN，但是携带的请求DNN未签约，该参数用于设置，当AMF使用UE携带的请求DNN，通过NRF来发现A-SMF失败后，是否会把请求DNN更正为其他签约的DNN，取值及含义如下：支持：当AMF使用UE携带的请求DNN，通过NRF来发现A-SMF失败后，会把请求DNN更正为其他签约的DNN。不支持：当AMF使用UE携带的请求DNN，通过NRF来发现A-SMF失败后，不会把请求DNN更正为其他签约的DNN。




命令举例 


`
查询AMF的DNN更正策略
SHOW DNNCORRECT POLICY:

(No.19) : SHOW DNNCORRECT POLICY:
-----------------Namf_Communication_0----------------
操作维护       DNN更正策略 A-SMF发现失败后支持DNN更正 
------------------------------------------------------
修改           支持DNN更正 支持                       
------------------------------------------------------
记录数：1
执行成功开始时间:2020-11-23 09:44:14 耗时: 0.576 秒

` 


#### 新增DNN更正配置(ADD DNNCORRECT CONFIG) 
#### 新增DNN更正配置(ADD DNNCORRECT CONFIG) 


功能说明 

该命令用于增加一个SUPI号段对应的DNN更正配置。 


注意事项 


 
该命令执行后，配置立即生效。 

 
该命令最多只能配置4096条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置一个特定的SUPI号段，对于此号段的终端，如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|参数作用：该参数用于设置特定的SUPI号段对应的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有四种。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。1-eMBB：提供高带宽、大数据量的服务。2-uRLLC：提供超高可靠低时延服务。3-mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。4-V2X：即Vehicle To Everything，车对外界的信息交换，是未来智能交通运输系统的关键技术。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置特定的SUPI号段对应的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：无。数据来源：本端规划。默认值：NULL。配置原则：无。
dnnCorrectPolicy|DNN更正方式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIBEDNN|参数作用：该参数用于特定的SUPI号段的终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，对应的DNN更正方式，取值及含义如下：签约DNN：设置为该选项，表示如果用户存在签约的默认DNN，AMF可将终端的DNN更正为签约的默认DNN；如果用户没有签约的默认DNN，则使用签约的非默认DNN。指定DNN：设置为该选项，表示AMF先判断指定DNN（即参数”DNN“）的配置值，是否在用户的签约DNN范围中，如果在用户的签约DNN范围中，则使用参数”DNN“的配置值来进行更正，如果不在用户的签约DNN范围中，则AMF使用”签约DNN“的配置策略。修改影响：无。数据来源：本端规划。默认值：签约DNN。配置原则： 签约DNN：对于漫游用户，在非跨国或跨网场景下，如果请求消息中携带的DNN不合法，则AMF对此类漫游号段用户使用的DNN更正方式为“签约DNN”；对于本地用户，如果请求消息中携带的DNN不合法，则AMF对本地号段用户的DNN使用更正方式为“签约DNN”。指定DNN：对于漫游用户，如果用户漫游到隶属于运营商的另一个网络时，如果请求消息中携带的DNN不合法，则AMF对此类漫游号段用户的DNN使用更正方式为“指定DNN”；对于本地用户，如果运营商决策UDM签约的默认DNN变更或不适用于更正的DNN，则当请求消息中携带的DNN不合法时，AMF对本地号段用户使用的DNN更正方式为"指定DNN"。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置一个特定SUPI选择指定DNN更正方式，对应的具体DNN。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN只支持输入小写字母，当参数”DNN更正方式（dnnCorrectPolicy）“配置为”指定DNN（CONFIGDNN）“时，如果属于特定的SUPI号段的终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可将终端的DNN修改为本参数配置的DDN，以保证会话流程的正常进行。




命令举例 


`
设置SUPI值为"46011222222"的用户的DNN更正配置为"签约DNN"
ADD DNNCORRECT CONFIG:SUPI="46011222222",DNNCORRECTPOLICY="SUBSCRIBEDNN"
` 


#### 修改DNN更正配置(MOD DNNCORRECT CONFIG) 
#### 修改DNN更正配置(MOD DNNCORRECT CONFIG) 


功能说明 

该命令用于修改一个SUPI号段对应的DNN更正配置。 


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置一个特定的SUPI号段，对于此号段的终端，如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|参数作用：该参数用于设置特定的SUPI号段对应的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有四种。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。1-eMBB：提供高带宽、大数据量的服务。2-uRLLC：提供超高可靠低时延服务。3-mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。4-V2X：即Vehicle To Everything，车对外界的信息交换，是未来智能交通运输系统的关键技术。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置特定的SUPI号段对应的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：无。数据来源：本端规划。默认值：NULL。配置原则：无。
dnnCorrectPolicy|DNN更正方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIBEDNN|参数作用：该参数用于特定的SUPI号段的终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，对应的DNN更正方式，取值及含义如下：签约DNN：设置为该选项，表示如果用户存在签约的默认DNN，AMF可将终端的DNN更正为签约的默认DNN；如果用户没有签约的默认DNN，则使用签约的非默认DNN。指定DNN：设置为该选项，表示AMF先判断指定DNN（即参数”DNN“）的配置值，是否在用户的签约DNN范围中，如果在用户的签约DNN范围中，则使用参数”DNN“的配置值来进行更正，如果不在用户的签约DNN范围中，则AMF使用”签约DNN“的配置策略。修改影响：无。数据来源：本端规划。默认值：签约DNN。配置原则： 签约DNN：对于漫游用户，在非跨国或跨网场景下，如果请求消息中携带的DNN不合法，则AMF对此类漫游号段用户使用的DNN更正方式为“签约DNN”；对于本地用户，如果请求消息中携带的DNN不合法，则AMF对本地号段用户的DNN使用更正方式为“签约DNN”。指定DNN：对于漫游用户，如果用户漫游到隶属于运营商的另一个网络时，如果请求消息中携带的DNN不合法，则AMF对此类漫游号段用户的DNN使用更正方式为“指定DNN”；对于本地用户，如果运营商决策UDM签约的默认DNN变更或不适用于更正的DNN，则当请求消息中携带的DNN不合法时，AMF对本地号段用户使用的DNN更正方式为"指定DNN"。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置一个特定SUPI选择指定DNN更正方式，对应的具体DNN。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN只支持输入小写字母，当参数”DNN更正方式（dnnCorrectPolicy）“配置为”指定DNN（CONFIGDNN）“时，如果属于特定的SUPI号段的终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可将终端的DNN修改为本参数配置的DDN，以保证会话流程的正常进行。




命令举例 


`
修改SUPI值为"46011222222"的用户的DNN更正配置为"指定DNN"，并设置该指定DNN为"zte.com.cn"
MOD DNNCORRECT CONFIG:SUPI="46011222222",DNNCORRECTPOLICY="CONFIGDNN",DNN="zte.com.cn"
` 


#### 删除DNN更正配置(DEL DNNCORRECT CONFIG) 
#### 删除DNN更正配置(DEL DNNCORRECT CONFIG) 


功能说明 

该命令用于删除一个SUPI号段对应的DNN更正配置。 


注意事项 

该命令执行后，配置立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置一个特定的SUPI号段，对于此号段的终端，如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|参数作用：该参数用于设置特定的SUPI号段对应的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有四种。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。1-eMBB：提供高带宽、大数据量的服务。2-uRLLC：提供超高可靠低时延服务。3-mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。4-V2X：即Vehicle To Everything，车对外界的信息交换，是未来智能交通运输系统的关键技术。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置特定的SUPI号段对应的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：无。数据来源：本端规划。默认值：NULL。配置原则：无。




命令举例 


`
删除SUPI值为"46011222222"的用户的DNN更正配置
DEL DNNCORRECT CONFIG:SUPI="46011222222"
` 


#### 查询DNN更正配置(SHOW DNNCORRECT CONFIG) 
#### 查询DNN更正配置(SHOW DNNCORRECT CONFIG) 


功能说明 

该命令用于查询一个SUPI号段对应的DNN更正配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置一个特定的SUPI号段，对于此号段的终端，如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supi|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于设置一个特定的SUPI号段，对于此号段的终端，如果终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，AMF可修改终端的DNN，以保证会话流程的正常进行。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: 0|参数作用：该参数用于设置特定的SUPI号段对应的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有四种。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。1-eMBB：提供高带宽、大数据量的服务。2-uRLLC：提供超高可靠低时延服务。3-mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。4-V2X：即Vehicle To Everything，车对外界的信息交换，是未来智能交通运输系统的关键技术。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置特定的SUPI号段对应的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
dnnCorrectPolicy|DNN更正方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIBEDNN|参数作用：该参数用于特定的SUPI号段的终端在请求建议PDU会话流程中，没有携带DNN或者携带的DNN不合法，对应的DNN更正方式，取值及含义如下：签约DNN：设置为该选项，表示如果用户存在签约的默认DNN，AMF可将终端的DNN更正为签约的默认DNN；如果用户没有签约的默认DNN，则使用签约的非默认DNN。指定DNN：设置为该选项，表示AMF先判断指定DNN（即参数”DNN“）的配置值，是否在用户的签约DNN范围中，如果在用户的签约DNN范围中，则使用参数”DNN“的配置值来进行更正，如果不在用户的签约DNN范围中，则AMF使用”签约DNN“的配置策略。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：该参数用于设置一个特定SUPI选择指定DNN更正方式，对应的具体DNN。




命令举例 


`
查询所有SUPI的DNN更正配置
SHOW DNNCORRECT CONFIG

(No.17) : SHOW DNNCORRECT CONFIG:
-----------------Namf_Communication_0----------------
操作维护       SUPI号段 SST SD   DNN更正方式 DNN 
-------------------------------------------------
复制  删除      111      0   NULL 签约DNN         
-------------------------------------------------
记录数：1
执行成功开始时间:2021-01-12 10:49:59 耗时: 0.129 秒

` 


### 缺省DNN配置 
### 缺省DNN配置 


背景知识 


5G网络中定义的DNN(Data Network Name，数据网络名称)就是4G网络中定义的APN，这两个标识符具有相同的含义并携带相同的信息（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。 

DNN或APN的组成有两部分： 


 
网络ID，这部分表示一个外部网络，这部分是必选的。 

 
运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。 

 

网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。 

运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。 

在PDU会话建立流程中，AMF需要通过DNN来选择合适的SMF，如果终端的请求消息中没有携带的DNN，且在终端的签约信息中，该终端的S-NSSAI下也不存在default DNN，可以使用本功能配置的缺省DNN。 




功能说明 


该功能用于配置终端的缺省DNN。 

在PDU会话建立流程中，AMF需要通过DNN来选择合适的SMF，如果终端的请求消息中没有携带的DNN，且在终端的签约信息中，该终端的S-NSSAI下也不存在default DNN，可以使用本功能配置的缺省DNN。 

如果AMF根据终端的S-NSSAI获取缺省DNN失败，则DNN选择失败。 




子主题： 






#### 新增缺省DNN配置(ADD DEFAULTDNNCONFIG) 
#### 新增缺省DNN配置(ADD DEFAULTDNNCONFIG) 


功能说明 

该命令用于在本AMF上配置终端的缺省DNN。 


注意事项 

一个AMF最多只能配置255个缺省DNN记录。DNN只支持输入小写。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|该参数用于设置S-NSSAI对应的缺省的DNN。DNN只支持输入小写。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置S-NSSAI对应的缺省的DNN。DNN只支持输入小写。




命令举例 


`
增加缺省DNN配置：SST为eMBB，SD为303001，DNN为zte.com.cn”。
ADD DEFAULTDNNCONFIG:SST="eMBB",SD="303001",DNN="zte.com.cn"
` 


#### 修改缺省DNN配置(SET DEFAULTDNNCONFIG) 
#### 修改缺省DNN配置(SET DEFAULTDNNCONFIG) 


功能说明 

该命令用于修改本AMF上配置的终端的缺省DNN。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|该参数用于设置S-NSSAI对应的缺省的DNN。DNN只支持输入小写。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置S-NSSAI对应的缺省的DNN。DNN只支持输入小写。




命令举例 


`
修改缺省DNN配置：SST为eMBB，SD为303001，DNN为zte.com.cn1。
SET DEFAULTDNNCONFIG:SST="eMBB",SD="303001",DNN="zte.com.cn1"
` 


#### 删除缺省DNN配置(DEL DEFAULTDNNCONFIG) 
#### 删除缺省DNN配置(DEL DEFAULTDNNCONFIG) 


功能说明 

该命令用于删除本AMF上配置终端的缺省DNN。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置S-NSSAI对应的缺省的DNN。DNN只支持输入小写。




命令举例 


`
删除SST为eMBB，SD为303001的缺省DNN配置。
DEL DEFAULTDNNCONFIG: :SST="eMBB",SD="303001"
` 


#### 查询缺省DNN配置(SHOW DEFAULTDNNCONFIG) 
#### 查询缺省DNN配置(SHOW DEFAULTDNNCONFIG) 


功能说明 

该命令用于查询本AMF上配置的所有缺省DNN，或查询某个指定缺省DNN信息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置S-NSSAI对应的缺省的DNN。DNN只支持输入小写。




命令举例 


`
查询所有缺省DNN配置。
SHOW DEFAULTDNNCONFIG

(No.1) : SHOW DEFAULTDNNCONFIG
-----------------Namf_Communication_0----------------
 SST        SD            DNN  
 eMBB    303001      zte.com.cn  
记录数：1
执行成功耗时: 0.093 秒

` 


### 专用DNN配置 
### 专用DNN配置 


背景知识 


随着5G专网业务的不断拓展，越来越多场景提出双域专网需求，用户希望利用5G与已有的WiFi网络协同（或替代已有WiFi），解决公网专网协同访问问题，涉及校园、医院、政务、文旅等多个行业。 

为提升双域专网漫游场景下的业务体验，满足客户无感知访问公网及专网的业务需求，可采用网络侧多DNN会话（又名无感分流）方案，即： 


 
当终端接入到5G网络后，终端只建立通用DNN的PDU会话，AMF基于本地配置的专用DNN列表识别出有无感分流需求的用户，并为该类用户选择无感分流专用SMF。 

 
专网业务到达，在无感分流专用SMF和负责企业专网DNN业务的SMF之间建立专用DNN的PDU会话；无感分流专用SMF负责专用DNN会话和通用DNN会话之间的业务映射，屏蔽终端侧感知。 

 




功能说明 


该功能用于AMF本地配置专用DNN列表以及无感分流关键字。 




子主题： 






#### 新增专用DNN配置(ADD DEDICATEDDNNCFG) 
#### 新增专用DNN配置(ADD DEDICATEDDNNCFG) 


功能说明 

该命令用于新增专用DNN配置。当AMF需要识别有无感分流需求的用户并为该类用户选择无感分流专用SMF时，使用该命令配置专用DNN列表。 


注意事项 

该命令执行后立即生效。 

应至少配置一个DNN作为无感分流关键字，即：将该DNN对应的配置参数“是否无感分流关键字”设为是。 

最多配置4096条记录。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：此参数用于设置专用DNN列表，用于识别出有无感分流需求的用户，并为该类用户选择无感分流专用SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN NI，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
istransplitkey|是否无感分流关键字|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：此参数用于设置对应的专用DNN是否为无感分流关键字。修改影响：无。数据来源：本端规划。默认值：否。配置原则：应至少配置一个DNN作为无感分流关键字。




命令举例 


`
新增专用DNN配置，DNN为zte.com.cn，是无感分流关键字。
ADD DEDICATEDDNNCFG:DNN="zte.com",ISTRANSPLITKEY="YES"
` 


#### 修改专用DNN配置(SET DEDICATEDDNNCFG) 
#### 修改专用DNN配置(SET DEDICATEDDNNCFG) 


功能说明 

该命令用于修改专用DNN配置。 


注意事项 

该命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：此参数用于设置专用DNN列表，用于识别出有无感分流需求的用户，并为该类用户选择无感分流专用SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN NI，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
istransplitkey|是否无感分流关键字|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：此参数用于设置对应的专用DNN是否为无感分流关键字。修改影响：无。数据来源：本端规划。默认值：否。配置原则：应至少配置一个DNN作为无感分流关键字。




命令举例 


`
修改专用DNN配置，DNN为zte.com.cn，设置为非无感分流关键字。
SET DEDICATEDDNNCFG:DNN="zte.com",ISTRANSPLITKEY="NO"
` 


#### 删除专用DNN配置(DEL DEDICATEDDNNCFG) 
#### 删除专用DNN配置(DEL DEDICATEDDNNCFG) 


功能说明 

该命令用于删除专用DNN配置。 


注意事项 

该命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：此参数用于设置专用DNN列表，用于识别出有无感分流需求的用户，并为该类用户选择无感分流专用SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN NI，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。




命令举例 


`
删除专用DNN配置，DNN为zte.com.cn。
DEL DEDICATEDDNNCFG:DNN="zte.com"
` 


#### 查询专用DNN配置(SHOW DEDICATEDDNNCFG) 
#### 查询专用DNN配置(SHOW DEDICATEDDNNCFG) 


功能说明 

该命令用于查询专用DNN配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：此参数用于设置专用DNN列表，用于识别出有无感分流需求的用户，并为该类用户选择无感分流专用SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：DNN NI，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于设置专用DNN列表，用于识别出有无感分流需求的用户，并为该类用户选择无感分流专用SMF。DNN只支持输入小写。
istransplitkey|是否无感分流关键字|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置对应的专用DNN是否为无感分流关键字。




命令举例 


`
查询专用DNN配置。
SHOW DEDICATEDDNNCFG

(No.3) : SHOW DEDICATEDDNNCFG:
-----------------Namf_Communication_0----------------
DNN            是否无感分流关键字
zte.com        是
记录数：1

执行成功耗时: 0.26 秒

` 


## I/V-SMF选择配置 
## I/V-SMF选择配置 


背景知识 


5G网络中，如果A-SMF管理的UPF无法与NR建立连接，则无法保证SSC mode1。当用户建立PDU会话或携带PDU会话移动时，如果A-SMF管理的UPF无法与UE所在的基站建立连接，则需要通过UE的当前位置信息来选择并插入合适的I-SMF。 

漫游HR场景下，当用户建立PDU会话或携带PDU会话移动时，A-SMF在用户归属地，AMF需要通过UE的当前位置信息来选择并插入合适的V-SMF。 




功能说明 


I/V-SMF选择配置包括：I-SMF策略配置 




子主题： 






### I-SMF策略配置 
### I-SMF策略配置 


背景知识 


在5G网络中，如果A-SMF管理的UPF无法与NR建立连接，则无法保证SSC mode1。 

4G网络支持为终端用户提供IP地址的连续性，在5G网络中，业务场景更加多样，为了满足不同业务对连续性的不同要求，5G系统支持不同的SSC Mode（Session and Service Continuity，会话和业务的连续性），一个PDU会话的SSC Mode在该会话的生命周期里保持不变。当已有PDU会话的SSC Mode不满足应用要求时，UE会为应用建立新的PDU会话。 

SSC Mode包括以下类型。 


 
SSC Mode1：提供IP连续性
对于SSC Mode1的PDU会话，网络提供给UE的IP地址与为UE选择的UPF保持不变
适用于IMS语音等对业务连续性有高要求的应用。 

 
SSC Mode2：不提供IP连续性
当SMF确定提供服务的UPF需要改变时，如当前用户面路径不是最优路径时，SMF会请求UE释放原PDU会话，重新建立一个新的到相同DN的PDU会话，SMF为重新建立的PDU会话选择新的UPF。（先断后连）
适用于缓存类的视频业务等对于业务连续性要求不高，允许业务出现短暂中断的应用。 

 
SSC Mode3：提供短期IP连续性
当SMF决定需要切换会话路径时，如UE移动导致原会话的用户面路径不是最优路径时，SMF会请求UE重新建立一个新的到相同DN的PDU会话，SMF为重新建立的PDU会话选择新的UPF，并在定时器到时或与该DN相关的业务流已转移到新会话上后，请求UE释放原PDU会话。（先连后断）
适用于MPTCP等支持多径传输的应用。 

 




功能说明 


本功能用于配置AMF是否支持I-SMF功能。 

当UE从大区1移动到大区2，如果大区1的A-SMF管理的UPF无法与UE所在的基站建立连接，则A-SMF无法选择能连接大区2下RAN的I-UPF。此种情况下就需要插入一个I-SMF。 




子主题： 






#### 修改AMF是否支持I-SMF配置(SET AMFSUPPORTISMF) 
#### 修改AMF是否支持I-SMF配置(SET AMFSUPPORTISMF) 


功能说明 

该命令用于设置AMF是否支持I-SMF功能。当运营商网络部署的A-SMF管理UPF的数量有限，A-SMF管理的UPF无法与UE所在的基站建立连接，并且网络中部署了I-UPF时，需要使用此命令打开I-SMF功能以管理I-UPF。该命令支持UE支持跨大区移动。 

当需要开启或关闭I-SMF功能时，可使用此命令。  


注意事项 

无


输入参数说明 


标识|名称|类型|说明
---|---|---|---
amfSupportIsmf|AMF是否支持I-SMF|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置AMF是否支持I-SMF功能。如果本参数设置为“支持”，则需要通过SET NRFDISCSMFPARACFG命令将CARRYPREFERREDTAI参数设置为SupPreferredTai，即“支持Preferred-TAI”。




命令举例 


`
设置或修改是否支持I-SMF功能。
SET AMFSUPPORTISMF:AMFSUPPORTISMF="SUPPORT"
` 


#### 查询AMF是否支持I-SMF配置(SHOW AMFSUPPORTISMF) 
#### 查询AMF是否支持I-SMF配置(SHOW AMFSUPPORTISMF) 


功能说明 

该命令用于查询AMF是否支持I-SMF功能。  


注意事项 

无


输出参数说明 


标识|名称|类型|说明
---|---|---|---
amfSupportIsmf|AMF是否支持I-SMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于显示AMF是否支持I-SMF功能。




命令举例 


`
查询AMF是否支持I-SMF。
SHOW AMFSUPPORTISMF:

(No.1) : SHOW AMFSUPPORTISMF:
-----------------Namf_Communication_0----------------
AMF是否支持I-SMF
支持
记录数：1

执行成功耗时： 0.381 秒

` 


## SMF选择服务范围配置 
## SMF选择服务范围配置 


背景知识 


在PDU会话建立流程中，涉及AMF选择SMF的过程，在SMF的选择过程中，AMF支持选择特定区域，即服务范围（servingScope）的SMF。 

服务范围（servingScope）表示NF实例可以服务的区域。当SMF只为某些区域服务时，SMF在向NRF注册时，需要携带支持的服务范围（servingScope）。 

当终端接入到5G网络，在PDU会话建立流程中，AMF可以基于服务范围（servingScope）选择服务于特定区域的SMF。 




功能说明 


本功能配置与跟踪区组标识匹配的servingScope group ID（服务范围组标识），使得AMF可以基于跟踪区映射出服务范围（servingScope），从而通过NRF选择服务特定区域的SMF。  




子主题： 






### SMF服务范围组配置 
### SMF服务范围组配置 


背景知识 


当终端接入到5G网络，在PDU会话建立流程中，AMF可以基于服务范围（servingScope）选择服务于特定区域的SMF。 

服务范围（servingScope）表示NF实例可以服务的区域。当SMF只为某些区域服务时，SMF在向NRF注册时携带支持的服务范围。 




功能说明 


本功能用于配置SMF服务范围组。 

当AMF需要基于服务范围（servingScope）选择服务于特定区域的SMF时，就需要配置SMF服务范围组。 




子主题： 






#### 新增SMF服务范围组配置(ADD SMF SERVSCOPE GRP) 
#### 新增SMF服务范围组配置(ADD SMF SERVSCOPE GRP) 


功能说明 

该命令用于新增SMF服务范围组配置。当AMF需要基于服务范围（servingScope）选择服务于特定区域的SMF时，使用该命令配置 SMF服务范围组。 


注意事项 

该命令执行后立即生效。 

一条配置命令，只能配置一个“服务范围组标识”与一个“服务范围”的关联关系；当需要将多个“服务范围”关联到同一个“服务范围组标识”时，需要执行多条配置命令。 

一个“服务范围组标识”最多关联128个“服务范围”，同一个“服务范围”可以归属不同的“服务范围组标识”。 

当需要修改“服务范围组标识”与“服务范围”的关联关系时，应先执行删除命令，再执行新增命令。 

最多可输入4096条记录。

输入参数说明 


标识|名称|类型|说明
---|---|---|---
servscopegrpid|服务范围组标识|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围组标识。修改影响：AMF发送给NRF的Nnrf_NFDiscovery请求中携带的服务范围组标识根据本参数的配置值获取。数据来源：本端规划。默认值：无。配置原则：一个服务范围组标识最多关联128个服务范围。
servingscope|服务范围|参数可选性: 必选参数类型: 字符串参数范围: 1-64|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围（servingScope）。修改影响：AMF发送给NRF的Nnrf_NFDiscovery请求中携带服务范围（servingScope）根据本参数的配置值获取。数据来源：本端规划。默认值：无。配置原则：无。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置SMF服务范围组的描述。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围组标识。
servingscope|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 1-64|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围（servingScope）。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置SMF服务范围组的描述。




命令举例 


`
新增服务范围组标识是1，服务范围是"nanjing"，别名是"NJ"的SMF服务范围组。
ADD SMF SERVSCOPE GRP:SERVSCOPEGRPID="1",SERVINGSCOPE="nanjing",ALIAS="NJ"
` 


#### 删除SMF服务范围组配置(DEL SMF SERVSCOPE GRP) 
#### 删除SMF服务范围组配置(DEL SMF SERVSCOPE GRP) 


功能说明 

该命令用于删除SMF服务范围组配置。 


注意事项 

该命令执行后立即生效。 

删除某个“服务范围组标识”下全部记录之前，需要先删除或修改“SMF服务范围跟踪区组配置”和“发现A-SMF参数配置”中关联该“服务范围组标识”的配置记录。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
servscopegrpid|服务范围组标识|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围组标识。修改影响：AMF发送给NRF的Nnrf_NFDiscovery请求中携带的服务范围组标识根据本参数的配置值获取。数据来源：本端规划。默认值：无。配置原则：一个服务范围组标识最多关联128个服务范围。
servingscope|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 1-64|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围（servingScope）。修改影响：AMF发送给NRF的Nnrf_NFDiscovery请求中携带服务范围（servingScope）根据本参数的配置值获取。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围组标识。
servingscope|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 1-64|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围（servingScope）。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置SMF服务范围组的描述。




命令举例 


`
删除服务范围组标识是1，服务范围是"nanjing"的SMF服务范围组。
DEL SMF SERVSCOPE GRP:SERVSCOPEGRPID="1",SERVINGSCOPE="nanjing"
` 


#### 查询SMF服务范围组配置(SHOW SMF SERVSCOPE GRP) 
#### 查询SMF服务范围组配置(SHOW SMF SERVSCOPE GRP) 


功能说明 

该命令用于查询SMF服务范围组配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围组标识。修改影响：AMF发送给NRF的Nnrf_NFDiscovery请求中携带的服务范围组标识根据本参数的配置值获取。数据来源：本端规划。默认值：无。配置原则：一个服务范围组标识最多关联128个服务范围。
servingscope|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 1-64|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围（servingScope）。修改影响：AMF发送给NRF的Nnrf_NFDiscovery请求中携带服务范围（servingScope）根据本参数的配置值获取。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围组标识。
servingscope|服务范围|参数可选性: 任选参数类型: 字符串参数范围: 1-64|参数作用：该参数用于设置AMF通过NRF发现A-SMF时，AMF发送给NRF的Nnrf_NFDiscovery请求消息中所携带的服务范围（servingScope）。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置SMF服务范围组的描述。




命令举例 


`
查询SMF服务范围组配置。
SHOW SMF SERVSCOPE GRP

(No.3) : SHOW SMF SERVSCOPE GRP:
-----------------Namf_Communication_0----------------
操作维护       服务范围组标识 服务范围 别名 
--------------------------------------------
复制  删除      1              nanjing  NJ   
--------------------------------------------
记录数：1
执行成功开始时间:2022-04-12 14:52:11 耗时: 0.141 秒

` 


### SMF服务范围跟踪区组配置 
### SMF服务范围跟踪区组配置 


背景知识 


当终端接入到5G网络，在PDU会话建立流程中，AMF可以基于服务范围（servingScope）选择服务于特定区域的SMF。 

服务范围（servingScope）表示NF实例可以服务的区域。当SMF只为某些区域服务时，SMF在向NRF注册时携带支持的服务范围。 




功能说明 


本功能用于配置SMF服务范围跟踪区组。 

当AMF需要基于跟踪区映射出服务范围（servingScope）选择服务于特定区域的SMF时，使用本功能配置跟踪区和服务范围的映射关系。 




子主题： 






#### 新增SMF服务范围跟踪区组配置(ADD SMF SERVSCOPE TA GRP) 
#### 新增SMF服务范围跟踪区组配置(ADD SMF SERVSCOPE TA GRP) 


功能说明 

该命令用于新增SMF服务范围跟踪区组配置。当AMF需要基于跟踪区映射出服务范围（servingScope）选择服务于特定区域的SMF时，使用该命令配置跟踪区和服务范围的映射关系。 


注意事项 

该命令执行后立即生效。 

配置本命令前，需要先执行“SMF服务范围组配置”，然后在本命令中通过配置参数“服务范围组ID”将“跟踪区组标识”与“服务范围组ID”关联起来。同一个“跟踪区组标识”只能关联同一个“服务范围组ID”；不同的“跟踪区组标识”可以关联同一个“服务范围组ID”。 

一条配置命令，只能配置一个“跟踪区组标识”与一个“跟踪区码”和/或一个跟踪区码范围（“跟踪区码起始”和“跟踪区码终止”用于标识一个跟踪区码范围）的关联关系；当需要将多个“跟踪区码”和/或跟踪区范围关联到同一个跟踪区组标识时，需要执行多条配置命令。 

“跟踪区码”和跟踪区码范围至少有一个配置有效取值。“跟踪区码”无效取值为“000000”；“跟踪区码起始”或“跟踪区码终止”有一个取值为“000000”，则跟踪区码范围无效。 

本配置下不应存在跟踪区重叠，即：相同或者不同跟踪区组配置中，不应存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围也不应重叠。操作人员应在配置之前做好数据规划。
当需要修改配置参数时，应先执行删除命令，再执行新增命令。
最多可输入65535条记录。

输入参数说明 


标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置和服务范围（servingScope）关联的跟踪区组标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：取值范围为1-65535，每个跟踪区组标识下面可以包括若干条具体的跟踪区范围。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区模板的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区组单条记录的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的单个跟踪区码，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：“跟踪区码”和跟踪区码范围（跟踪区码起始+跟踪区码终止）至少有一个配置有效取值。“跟踪区码”配置为“000000“表示无效取值，“跟踪区码起始”或“跟踪区码终止”，两个参数中有一个取值为“000000”，则此跟踪区码范围无效。不允许存在跟踪区互相重叠的配置数据，即：相同或者不同跟踪区组配置中，不允许存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围（跟踪区码起始+跟踪区码终止）也不允许重叠。操作人员应在配置之前做好数据规划。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的起始，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：如下：“跟踪区码”和跟踪区码范围（跟踪区码起始+跟踪区码终止）至少有一个配置有效取值。“跟踪区码”配置为“000000“表示无效取值，“跟踪区码起始”或“跟踪区码终止”，两个参数中有一个取值为“000000”，则此跟踪区码范围无效。不允许存在跟踪区互相重叠的配置数据，即：相同或者不同跟踪区组配置中，不允许存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围（跟踪区码起始+跟踪区码终止）也不允许重叠。操作人员应在配置之前做好数据规划。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的终止，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：如下：“跟踪区码”和跟踪区码范围（跟踪区码起始+跟踪区码终止）至少有一个配置有效取值。“跟踪区码”配置为“000000“表示无效取值，“跟踪区码起始”或“跟踪区码终止”，两个参数中有一个取值为“000000”，则此跟踪区码范围无效。不允许存在跟踪区互相重叠的配置数据，即：相同或者不同跟踪区组配置中，不允许存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围（跟踪区码起始+跟踪区码终止）也不允许重叠。操作人员应在配置之前做好数据规划。
servscopegrpid|服务范围组标识|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于配置与跟踪区组标识匹配的servingScope group ID（服务范围组标识），使得AMF可以基于跟踪区映射出服务范围（servingScope），从而通过NRF选择服务特定区域的SMF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于ADD SMF SERVSCOPE GRP命令配置的参数“服务范围组标识（servscopegrpid）”
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置本条记录的描述。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置和服务范围（servingScope）关联的跟踪区组标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区组单条记录的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区组单条记录的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的单个跟踪区码，由运营商在PLMN内统一规划，以16进制数字编码。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的起始，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的终止，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于配置与跟踪区组标识匹配的servingScope group ID（服务范围组标识），使得AMF可以基于跟踪区映射出服务范围（servingScope），从而通过NRF选择服务特定区域的SMF。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置本条记录的描述。




命令举例 


`
新增跟踪区组标识是"1"，mcc是"460"，mnc是"11"，tac是"000001"，tac范围从"000010"到"000020"，服务范围组标识是"1"的服务范围跟踪区组。
ADD SMF SERVSCOPE TA GRP:TAGROUPID="1",MCC="460",MNC="11",TAC="000001",TACST="000010",TACEND="000020",SERVSCOPEGRPID="1",ALIAS="NJ"
` 


#### 删除SMF服务范围跟踪区组配置(DEL SMF SERVSCOPE TA GRP) 
#### 删除SMF服务范围跟踪区组配置(DEL SMF SERVSCOPE TA GRP) 


功能说明 

该命令用于删除SMF服务范围跟踪区组配置。 


注意事项 

该命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置和服务范围（servingScope）关联的跟踪区组标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：取值范围为1-65535，每个跟踪区组标识下面可以包括若干条具体的跟踪区范围。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区模板的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区组单条记录的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的单个跟踪区码，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：“跟踪区码”和跟踪区码范围（跟踪区码起始+跟踪区码终止）至少有一个配置有效取值。“跟踪区码”配置为“000000“表示无效取值，“跟踪区码起始”或“跟踪区码终止”，两个参数中有一个取值为“000000”，则此跟踪区码范围无效。不允许存在跟踪区互相重叠的配置数据，即：相同或者不同跟踪区组配置中，不允许存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围（跟踪区码起始+跟踪区码终止）也不允许重叠。操作人员应在配置之前做好数据规划。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的起始，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：如下：“跟踪区码”和跟踪区码范围（跟踪区码起始+跟踪区码终止）至少有一个配置有效取值。“跟踪区码”配置为“000000“表示无效取值，“跟踪区码起始”或“跟踪区码终止”，两个参数中有一个取值为“000000”，则此跟踪区码范围无效。不允许存在跟踪区互相重叠的配置数据，即：相同或者不同跟踪区组配置中，不允许存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围（跟踪区码起始+跟踪区码终止）也不允许重叠。操作人员应在配置之前做好数据规划。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的终止，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：如下：“跟踪区码”和跟踪区码范围（跟踪区码起始+跟踪区码终止）至少有一个配置有效取值。“跟踪区码”配置为“000000“表示无效取值，“跟踪区码起始”或“跟踪区码终止”，两个参数中有一个取值为“000000”，则此跟踪区码范围无效。不允许存在跟踪区互相重叠的配置数据，即：相同或者不同跟踪区组配置中，不允许存在重复的跟踪区和跟踪区范围，跟踪区与跟踪区范围（跟踪区码起始+跟踪区码终止）也不允许重叠。操作人员应在配置之前做好数据规划。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置和服务范围（servingScope）关联的跟踪区组标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区组单条记录的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区组单条记录的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的单个跟踪区码，由运营商在PLMN内统一规划，以16进制数字编码。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的起始，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的终止，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于配置与跟踪区组标识匹配的servingScope group ID（服务范围组标识），使得AMF可以基于跟踪区映射出服务范围（servingScope），从而通过NRF选择服务特定区域的SMF。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置本条记录的描述。




命令举例 


`
删除跟踪区组标识是"1"，mcc是"460"，mnc是"11"，tac是"000001"，tac范围从"000010"到"000020"，服务范围组标识是"1"的服务范围跟踪区组。
DEL SMF SERVSCOPE TA GRP:TAGROUPID="1",MCC="460",MNC="11",TAC="000001",TACST="000010",TACEND="000020",SERVSCOPEGRPID="1"
` 


#### 查询SMF服务范围跟踪区组配置(SHOW SMF SERVSCOPE TA GRP) 
#### 查询SMF服务范围跟踪区组配置(SHOW SMF SERVSCOPE TA GRP) 


功能说明 

该命令用于查询SMF服务范围跟踪区组配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置和服务范围（servingScope）关联的跟踪区组标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：取值范围为1-65535，每个跟踪区组标识下面可以包括若干条具体的跟踪区范围。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置和服务范围（servingScope）关联的跟踪区组标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区组单条记录的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区组单条记录的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的单个跟踪区码，由运营商在PLMN内统一规划，以16进制数字编码。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的起始，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区组单条记录的跟踪区码范围的终止，由运营商在PLMN内统一规划，以16进制数字编码。当存在PLMN相同且连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须依次增加。
servscopegrpid|服务范围组标识|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数用于配置与跟踪区组标识匹配的servingScope group ID（服务范围组标识），使得AMF可以基于跟踪区映射出服务范围（servingScope），从而通过NRF选择服务特定区域的SMF。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-15|参数作用：该参数用于配置本条记录的描述。




命令举例 


`
查询SMF服务范围组配置。
SHOW SMF SERVSCOPE TA GRP

(No.3) : SHOW SMF SERVSCOPE TA GRP:
-----------------Namf_Communication_0----------------
操作维护       跟踪区组标识 移动国家码 移动网络码 跟踪区码 跟踪区码起始 跟踪区码终止 服务范围组标识 别名 
---------------------------------------------------------------------------------------------------------
复制  删除      1            460        11         000001   000010       000020       1                   NJ
---------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-04-12 15:01:53 耗时: 0.148 秒

` 


# NF优选位置配置 
# NF优选位置配置 


背景知识 


 AMF通过NRF发现和选择目标NF时，优先选择特定位置的NF进行业务交互，可以满足运营商在不同场景下的需求： 


 
优选与AMF相同位置的目标NF：为了避免跨DC的路由迂回，需要优选与AMF相同位置（例如：同数据中心、资源池）的NF。 

 
优选指定位置的目标NF：由于网络调整或本地NF升级等原因，需要选择其他指定位置内的NF。 

 




功能说明 


优选位置配置可以为所有NF类型设置同一个优选位置，也可以为不同的NF设置不同的优选位置。包括如下配置： 


 
优选位置：当AMF需要基于位置信息优选目标NF，并且期望选择的目标NF与AMF的位置不同时，可以设置指定的位置信息。 

 
指定位置无效是否使用本地位置：当指定位置无效时，AMF可以决策是否使用全局配置中与AMF相同的本地位置。 

 




子主题： 






## 新增优选位置配置(ADD PREFER LOCALITY) 
## 新增优选位置配置(ADD PREFER LOCALITY) 


功能说明 

AMF通过NRF发现和选择目标NF时，需要基于位置信息优先选择特定位置的目标NF进行业务交互，并且期望选择的目标NF与AMF的位置不同时，使用该命令配置指定的位置信息。 

当AMF需要通过NRF发现和选择目标NF时，AMF会在发送给NRF的Nnrf_NF Discovery请求消息中所携带相关的的参数，NRF可根据这些参数作为参考因素来选择合适的NF。包括如下参数：S-NSSAI、PLMN、NSI（Network Slice Instance，网络切片实例）、preferred-locality等。  

AMF通过NRF发现和选择目标NF时，如果需要基于位置信息优先选择特定位置的目标NF进行业务交互，AMF会在发送给NRF的Nnrf_NF Discovery请求消息中所携带preferred-locality参数，preferred-locality参数是否有效取决于AMF获取到的NF位置信息是否有效，NF位置信息来源如下： 


 
通过本命令配置的NF位置。 

 
如果通过本命令无法获取到NF位置，且本命令中的参数“指定位置无效是否使用本地位置（uselocloaclity）”配置为“YES”，则使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）”。 

 


注意事项 

本命令执行后，结果立即生效。 

配置本命令前，需要先配置如下命令。 


 
通过SET NRFDISCAUSFPARACFG命令配置基于Locality选择AUSF的策略，将参数“携带preferred-locality（carryprelocality）”设置为“携带”。 

 
通过SET NRFDISCUDMPARACFG命令配置基于Locality选择UDM的策略，将参数“携带preferred-locality（carryprelocality）”设置为“携带”。 

 
通过SET NRFDISCSMFPARACFG命令配置基于Locality选择SMF的策略，将参数“携带preferred-locality（carryprelocality）”设置为“携带”。 

 

本命令支持两种选择策略： 


 
NRF优选：如果上述命令中，配置为“携带preferred-locality”，表示AMF通过NRF发现和选择目标NF时，优使用preferred-locality参数。 

 
本地优选：如果上述命令中，配置为“支持基于Locality优选”，表示AMF通过NRF发现和选择目标NF时，不携带preferred-locality参数， AMF基于Locality选择目标NF。 

 

AMF执行Locality优选时，只能使用NRF优选和本地优选中的一种；如果两者同时配置的情况下，以本地优选的优先级为高。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。修改影响：修改该参数，可以改变指定配置的NF类型。数据来源：本端规划。默认值：ALL NF配置原则：无。
prelocality|优选位置|参数可选性: 任选参数类型: 字符串参数范围: 0-99默认值: NULL|参数作用：该参数用于AMF需要基于位置信息优选目标NF时设置指定NF的Preferred locality。修改影响：修改该参数，可以改变被发现目标NF的位置信息配置。其中，默认值NULL为无效位置信息，AMF不携带。数据来源：本端规划。默认值：NULL 配置原则：无。
uselocloaclity|指定位置无效是否使用本地位置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于当指定NF类型或所有NF类型中未配置有效的Preferred locality时，是否需要获取全局配置中与AMF相同的本地位置，即使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）。修改影响：修改该参数，可以改变指定位置无效时，AMF是否使用全局配置中与AMF相同的本地位置。数据来源：本端规划。默认值：NO 配置原则：无。
localityselpri|位置选择优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RELYONLOCALITY|参数作用：该参数用于配置AMF基于位置选择NF的优先级，即配置AMF是否以发送给NRF的Nnrf_NFDiscovery请求消息中携带preferred-locality参数作为选择NF的优选条件。修改影响：修改该参数，可以改变位置优选顺序。数据来源：本端规划。默认值：RELYONLOCALITY 配置原则：无。
localitymatchply|位置匹配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLMATCH|参数作用：该参数用于选择位置匹配策略，包含全匹配和按Lable最长匹配两种方法。修改影响：修改该参数，可以改变位置匹配方法。数据来源：本端规划。默认值：FULLMATCH 配置原则：无。
locselsuprecovery|位置优选是否支持容灾|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于选择位置优选是否支持容灾。修改影响：修改该参数，用于更改位置优选支持容灾功能。数据来源：本端规划。默认值：NO 配置原则：无。
locmatchdiff|位置匹配与不匹配NF个数差值|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 1|参数作用：该参数用于显示位置匹配与不匹配NF个数相差数值，取值范围在0-255。修改影响：修改该参数，当差值超过配置的个数，则AMF不执行Locality优选。数据来源：本端规划。默认值：1 配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。
prelocality|优选位置|参数可选性: 任选参数类型: 字符串参数范围: 0-99默认值: NULL|参数作用：该参数用于AMF需要基于位置信息优选目标NF时设置指定NF的Preferred locality。
uselocloaclity|指定位置无效是否使用本地位置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于当指定NF类型或所有NF类型中未配置有效的Preferred locality时，是否需要获取全局配置中与AMF相同的本地位置，即使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）。
localityselpri|位置选择优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RELYONLOCALITY|参数作用：该参数用于配置AMF基于位置选择NF的优先级，即配置AMF是否以发送给NRF的Nnrf_NFDiscovery请求消息中携带preferred-locality参数作为选择NF的优选条件。
localitymatchply|位置匹配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLMATCH|参数作用：该参数用于选择位置匹配策略，包含全匹配和按Lable最长匹配两种方法。
locselsuprecovery|位置优选是否支持容灾|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于选择位置优选是否支持容灾。
locmatchdiff|位置匹配与不匹配NF个数差值|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 1|参数作用：该参数用于显示位置匹配与不匹配NF个数相差数值，取值范围在0-255。




命令举例 


`
新增一组优选位置配置，其中NF类型是SMF，优选位置为"nanjing.dc,"，指定位置无效不使用本地位置，位置选择优先级以优先级优先，位置匹配策略采用全匹配，位置优选不支持容灾，位置匹配与不匹配NF个数差值为1。
ADD PREFER LOCALITY:NFTYPE="SMF",PRELOCALITY="nanjing.dc",USELOCLOACLITY="NO",LOCALITYSELPRI="RELYONLOCALITY",LOCALMATCHPLY="FULLMATCH",LOCSELSUPRECOVERY="NO",LOCMATCHDIFF="1"
` 


## 修改优选位置配置(SET PREFER LOCALITY) 
## 修改优选位置配置(SET PREFER LOCALITY) 


功能说明 

该命令用于修改优选位置配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。修改影响：修改该参数，可以改变指定配置的NF类型。数据来源：本端规划。默认值：ALL NF配置原则：无。
prelocality|优选位置|参数可选性: 任选参数类型: 字符串参数范围: 0-99默认值: NULL|参数作用：该参数用于AMF需要基于位置信息优选目标NF时设置指定NF的Preferred locality。修改影响：修改该参数，可以改变被发现目标NF的位置信息配置。其中，默认值NULL为无效位置信息，AMF不携带。数据来源：本端规划。默认值：NULL 配置原则：无。
uselocloaclity|指定位置无效是否使用本地位置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于当指定NF类型或所有NF类型中未配置有效的Preferred locality时，是否需要获取全局配置中与AMF相同的本地位置，即使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）。修改影响：修改该参数，可以改变指定位置无效时，AMF是否使用全局配置中与AMF相同的本地位置。数据来源：本端规划。默认值：NO 配置原则：无。
localityselpri|位置选择优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RELYONLOCALITY|参数作用：该参数用于配置AMF基于位置选择NF的优先级，即配置AMF是否以发送给NRF的Nnrf_NFDiscovery请求消息中携带preferred-locality参数作为选择NF的优选条件。修改影响：修改该参数，可以改变位置优选顺序。数据来源：本端规划。默认值：RELYONLOCALITY 配置原则：无。
localitymatchply|位置匹配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLMATCH|参数作用：该参数用于选择位置匹配策略，包含全匹配和按Lable最长匹配两种方法。修改影响：修改该参数，可以改变位置匹配方法。数据来源：本端规划。默认值：FULLMATCH 配置原则：无。
locselsuprecovery|位置优选是否支持容灾|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于选择位置优选是否支持容灾。修改影响：修改该参数，用于更改位置优选支持容灾功能。数据来源：本端规划。默认值：NO 配置原则：无。
locmatchdiff|位置匹配与不匹配NF个数差值|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 1|参数作用：该参数用于显示位置匹配与不匹配NF个数相差数值，取值范围在0-255。修改影响：修改该参数，当差值超过配置的个数，则AMF不执行Locality优选。数据来源：本端规划。默认值：1 配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。
prelocality|优选位置|参数可选性: 任选参数类型: 字符串参数范围: 0-99默认值: NULL|参数作用：该参数用于AMF需要基于位置信息优选目标NF时设置指定NF的Preferred locality。
uselocloaclity|指定位置无效是否使用本地位置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于当指定NF类型或所有NF类型中未配置有效的Preferred locality时，是否需要获取全局配置中与AMF相同的本地位置，即使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）。
localityselpri|位置选择优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RELYONLOCALITY|参数作用：该参数用于配置AMF基于位置选择NF的优先级，即配置AMF是否以发送给NRF的Nnrf_NFDiscovery请求消息中携带preferred-locality参数作为选择NF的优选条件。
localitymatchply|位置匹配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLMATCH|参数作用：该参数用于选择位置匹配策略，包含全匹配和按Lable最长匹配两种方法。
locselsuprecovery|位置优选是否支持容灾|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于选择位置优选是否支持容灾。
locmatchdiff|位置匹配与不匹配NF个数差值|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 1|参数作用：该参数用于显示位置匹配与不匹配NF个数相差数值，取值范围在0-255。




命令举例 


`
修改NF类型是SMF的优选位置配置，优选位置为"zhenjiang.dc"，指定位置无效不使用本地位置，位置选择优先级以优先级优先，位置匹配策略采用全匹配，位置优选不支持容灾，位置匹配与不匹配NF个数差值为1。
SET PREFER LOCALITY:NFTYPE="SMF",PRELOCALITY="zhenjiang.dc",USELOCLOACLITY="NO",LOCALITYSELPRI="RELYONLOCALITY",LOCALMATCHPLY="FULLMATCH",LOCSELSUPRECOVERY="NO",LOCMATCHDIFF="1"
` 


## 删除优选位置配置(DEL PREFER LOCALITY) 
## 删除优选位置配置(DEL PREFER LOCALITY) 


功能说明 

该命令用于删除优选位置配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。修改影响：修改该参数，可以改变指定配置的NF类型。数据来源：本端规划。默认值：ALL NF配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。
prelocality|优选位置|参数可选性: 任选参数类型: 字符串参数范围: 0-99默认值: NULL|参数作用：该参数用于AMF需要基于位置信息优选目标NF时设置指定NF的Preferred locality。
uselocloaclity|指定位置无效是否使用本地位置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于当指定NF类型或所有NF类型中未配置有效的Preferred locality时，是否需要获取全局配置中与AMF相同的本地位置，即使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）。
localityselpri|位置选择优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RELYONLOCALITY|参数作用：该参数用于配置AMF基于位置选择NF的优先级，即配置AMF是否以发送给NRF的Nnrf_NFDiscovery请求消息中携带preferred-locality参数作为选择NF的优选条件。
localitymatchply|位置匹配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLMATCH|参数作用：该参数用于选择位置匹配策略，包含全匹配和按Lable最长匹配两种方法。
locselsuprecovery|位置优选是否支持容灾|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于选择位置优选是否支持容灾。
locmatchdiff|位置匹配与不匹配NF个数差值|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 1|参数作用：该参数用于显示位置匹配与不匹配NF个数相差数值，取值范围在0-255。




命令举例 


`
删除NF类型是SMF的优选位置配置
DEL PREFER LOCALITY:NFTYPE="SMF"
` 


## 查询优选位置配置(SHOW PREFER LOCALITY) 
## 查询优选位置配置(SHOW PREFER LOCALITY) 


功能说明 

该命令用于查询优选位置配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。修改影响：修改该参数，可以改变指定配置的NF类型。数据来源：本端规划。默认值：ALL NF配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: ALL|参数作用：该参数用于设置指定NF的优选类型。当前支持的NF类型为：AUSF、UDM、SMF、ALL NF。
prelocality|优选位置|参数可选性: 任选参数类型: 字符串参数范围: 0-99默认值: NULL|参数作用：该参数用于AMF需要基于位置信息优选目标NF时设置指定NF的Preferred locality。
uselocloaclity|指定位置无效是否使用本地位置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于当指定NF类型或所有NF类型中未配置有效的Preferred locality时，是否需要获取全局配置中与AMF相同的本地位置，即使用SET AMFLOCALOFFICECFG命令配置的参数“位置信息（locality）。
localityselpri|位置选择优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RELYONLOCALITY|参数作用：该参数用于配置AMF基于位置选择NF的优先级，即配置AMF是否以发送给NRF的Nnrf_NFDiscovery请求消息中携带preferred-locality参数作为选择NF的优选条件。
localitymatchply|位置匹配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLMATCH|参数作用：该参数用于选择位置匹配策略，包含全匹配和按Lable最长匹配两种方法。
locselsuprecovery|位置优选是否支持容灾|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于选择位置优选是否支持容灾。
locmatchdiff|位置匹配与不匹配NF个数差值|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 1|参数作用：该参数用于显示位置匹配与不匹配NF个数相差数值，取值范围在0-255。




命令举例 


`
查询优选位置配置。
SHOW PREFER LOCALITY

(No.2) : SHOW PREFER LOCALITY:
-----------------Namf_Communication_0----------------
操作维护       NF类型 优选位置 指定位置无效是否使用本地位置 位置选择优先级           位置匹配策略  位置优选是否支持容灾  位置匹配与不匹配NF个数差值
------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   SMF   NULL     是                        Locality->优先级->权重   全匹配        否                    1
------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-14 10:18:49 耗时: 1.763秒

` 


