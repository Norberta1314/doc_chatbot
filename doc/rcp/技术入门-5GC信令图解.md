# 5GC信令流程 
信令流程 :### 注册及移动性管理 
UE要使用网络服务，首先需要向网络进行注册。注册流程分为如下几种场景： 
初次注册到5G网络。 
当UE移动出了原来注册的区域时，进行移动性注册更新。 
周期性注册更新。 
当UE处在去注册状态下，要接入网络接受服务的时候，UE会发起初始注册流程。 
当UE移动到注册区之外的新的跟踪区 (TA，Tracking Area)时，或者UE需要更新注册过程中协商的能力或协议参数时，或者当UE想要获取LADN信息时，UE会发起移动注册更新流程。 
当UE在之前注册流程中协商的周期性注册更新定时器超时的时候，发起周期性注册更新流程。 
#### 注册 
本节包括以下流程： 
普通注册流程 
AMF重分配流程 
##### 注册流程业务场景 
UE要使用网络服务，首先需要向网络进行注册。注册流程分为如下几种场景： 

初次注册到5G网络。 
当UE移动出了原来注册的区域时，进行移动性注册更新。 
周期性注册更新。 
初始注册流程发生的场景如下： 
UE进行5GS业务初始注册时。 
UE进行紧急业务初始注册时。 
UE进行SMS over NAS初始注册时。 
当UE从GERAN移动到NG-RAN覆盖区或UE从UTRAN移动到NG-RAN覆盖区，且：UE在A/Gb模式或Iu模式下发起GPRS附着或路由区更新流程。UE在S1模式下没有成功执行EPS附着或跟踪区更新流程，在N1模式下也没有成功执行注册流程。 
移动注册流程发生的场景如下： 
当UE移出了原来注册的区域时，进行移动性注册更新。 
当UE移动到注册区之外的新的TA时，或者UE需要更新注册过程中协商的能力或协议参数时，或者当UE想要获取LADN信息时，UE会发起移动注册更新流程。 
周期注册流程发生的场景如下： 
当UE在之前注册流程中协商的周期性注册更新定时器超时时，发起周期性注册更新流程。 
##### 普通注册流程 
普通注册流程如[图1](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__875aa8a9-14ae-4b84-b2aa-36e5224450b2)所示。
图1  普通注册
[]images/%E6%B5%81%E7%A8%8B%E5%9B%BE(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE发送Registration Request
到(R)AN，消息中包含注册类型、用户标识（SUCI或5G-GUTI或PEI）、UE的5GC能力及可选的Requested NSSAI等参数。Registration Request消息中的关键信元参见[表1](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__50633fa9-87a0-40fe-bf50-a398693e1782)。
关键信元|信元解释|示例
---|---|---
Registration Type|指示UE请求的注册类型，Bits 1/2/3组合取值代表注册类型，注册类型取值如下：1（0x01），初始注册。2（0x02），移动注册更新。3（0x03），周期注册更新。4（0x04），紧急注册。5（0x05），其他取值。|
5GS mobile identity|用于提供SUCI、5G-GUTI、IMEI、IMEISV。|
(R)AN接收到消息，根据RAT或Requested NSSAI选择合适的AMF，如果(R)AN无法选择到合适的AMF，则将Registration Request
发送给缺省AMF，由缺省AMF进行AMF选择过程。
(R)AN将Registration Request
消息放在N2 Message (Initial UE Message)消息中转发给AMF。N2 Message (Initial UE Message)消息中的关键信元参见[表2](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__9e592f88-9273-4b74-83a2-969956a98ada)。
关键信元|信元解释|示例
---|---|---
PLMN Identity|PLMN标识，PLMN用于区分一个国家或地区不同的移动通信运营商。PLMN包含MCC和MNC，即PLMN=MCC + MNC。MCC和MNC说明如下：MCC由国际电信联盟（ITU）统一分配和管理，用于唯一识别移动用户所属的国家，一个国家可以被分配多个MCC。MCC由三位数字组成，中国的MCC为460，美国的MCC为310、311和316。MNC用于识别移动用户所属的移动网络，和MCC一起可以唯一识别所属运营商，MNC由2位或3位数字组成。|
TAC|用于唯一标识一个跟踪区域码。由运营商自行分配，用于网络侧跟踪UE的位置信息。|
（可选）如果Registration Request
中携带的是5G-GUTI，并且AMF检测到5G-GUTI不是本局分配的，AMF会调用Old AMF的服务化接口Namf_Communication_UEContextTransfer
请求用户的SUPI和MM Context，请求消息中包含完整的注册请求NAS消息，Old AMF对请求消息中携带的NAS消息进行完整性检查。
（可选）Old AMF响应New AMF调用的服务化接口Namf_Communication_UEContextTransfer
，参数包括SUPI、UE上下文等信息。
（可选）如果UE没有提供SUPI，也没有从Old AMF处获取到SUPI，AMF向UE发送Identity Request
消息请求获取SUCI。
（可选）UE向AMF返回Identity Response
消息，消息中包含SUCI。
如果AMF没有用户上下文，或者Registration
Request
消息没有被完整性保护，或者完整性检查失败，AMF会调用AUSF服务发起UE鉴权过程。这时AMF会根据Routing Ind选择一个AUSF。
（可选）AUSF执行对UE的鉴权过程。
（可选）如果AMF改变，New AMF调用Old AMF的服务化接口Namf_Communication_RegistrationCompleteNotify，通知Old
AMF收到MM Context。 
（可选）AMF向UE发送Identity Request
消息，请求获取PEI。UE向AMF返回Identity Response
消息包含PEI。
（可选）AMF通过服务化接口消息N5g-eir_EquipmentIdentityCheck_Get向EIR发起PEI检查过程，EIR向AMF返回检查结果响应。
（可选）如果第14步需要执行，则New AMF根据SUPI选择一个UDM实例。
New AMF及Old AMF分别执行如下操作： 
如果AMF改变，或者如果AMF没有用户的有效的上下文，AMF需要向UDM注册并获取签约数据。AMF调用UDM的服务化接口Nudm_UEContextManagement_Registration
向UDM注册，以及订阅当UDM注销该AMF时，发送的用户通知。Nudm_UEContextManagement_Registration请求消息中的关键信元参见[表3](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__d8f362c1-152c-4988-89ad-71f389e3147d)。
关键信元|信元解释|示例
---|---|---
deregCallbackUri|AMF提供的URI，用于接收去注册通知。|
guami|全球唯一AMF标识。|
ratType|表示UE当前的RAT类型，包括3GPP接入技术和非3GPP接入技术。|
imsVoPs|指示AMF是否支持IMS语音能力。|
AMF调用UDM的服务化接口Nudm_SubscriberDataManagement_Get
获取签约数据。Nudm_SubscriberDataManagement_Get响应消息中的关键信元参见[表4](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__0d6edcb6-084c-46b7-b35c-0b6aa8868734)。
关键信元|信元解释|示例
---|---|---
Data|请求的数据集，比如AM（接入和移动签约数据），SMF_SEL（SMF选择的签约数据）。|
AMF获取签约数据成功后，通过Nudm_SubscriberDataManagement_Subscribe
向UDM订阅签约数据变更通知。Nudm_SubscriberDataManagement_Subscribe请求消息中的关键信元参见[表5](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__b142cc7e-01ef-49c7-b51a-a017b9fc327f)。
关键信元|信元解释|示例
---|---|---
nfInstanceId|唯一标识NF实例的字符串。 NF实例ID的格式应为通用唯一标识符，此处为AMF的实例标识。|
callbackReference|NF服务消费者（此处为AMF）提供的URI，用于接收通知。|
monitoredResourceUris|一组URI，用于标识触发了变更通知的资源，如标识amData变更后通知AMF。|
New AMF向UDM注册成功后，UDM向Old AMF发送Nudm_UEContextManagement_DeregistrationNotification
通知，携带通知原因值。Nudm_UEContextManagement_DeregistrationNotification请求消息中的关键信元参见[表6](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__6524dcb7-03c2-412d-85b2-04dadab272c0)。
关键信元|信元解释|示例
---|---|---
accessType|表示用户注册的接入类型，包括：1（0x01），3GPP_Access。2（0x02），Non-3GPP_Access。3（0x03），3GPP_Access and non-3GPP_access。|
deregReason|表示Deregistration Notification原因，包括：UE_INITIAL_REGISTRATION。UE_REGISTRATION_AREA_CHANGE。SUBSCRIPTION_WITHDRAWN。5GS_TO_EPS_MOBILITY。5GS_TO_EPS_MOBILITY_UE_INITIAL_REGISTRATION。REREGISTRATION_REQUIRED。此处UDM发起去注册的原因是UE_INITIAL_REGISTRATION。|
Old AMF调用UDM的服务化接口Nudm_SubscriberDataManagement_Unsubscribe
取消签约数据订阅。
（可选）如果AMF决定与PCF通信，则AMF选择一个PCF实例。
（可选）New AMF向PCF发起一个策略关联建立过程，参见接入和移动性策略控制
。
（可选）PCF调用AMF的服务化接口Namf_EventExposure_Subscribe
向AMF请求订阅该UE移动性管理相关的事件变化通知。
（可选）如果AMF改变或UE的PDU Session Status与AMF保存的不一致，AMF调用SMF的服务化接口Nsmf_PDUSession_UpdateSMContext
通知SMF更新AMF信息或释放不一致的PDU会话。
（可选）如果Old AMF已与PCF建立关联且没有将PCF ID传递给New AMF，AMF发起策略关联终止过程，参见接入和移动性策略控制
。
New AMF向UE发送Registration Accept
消息，接受UE发起的注册请求。如果New AMF为UE分配了新的5G-GUTI，则需要在本消息中携带。Registration Accept消息中的关键信元参见[表7](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__6b8e10ee-e9dc-4351-8117-43e820c1b8d9)。
关键信元|信元解释|示例
---|---|---
5GS registration result|用于指示注册结果。Bits 1/2/3代表注册接入类型，包括：1（0x01），3GPP access。2（0x02），Non-3GPP access。3（0x03），3GPP access and non-3GPP access。|
5G-GUTI|5G UE临时标识，包含MCC、MNC、AMF Region ID、AMF Set ID、AMF Pointer、5G-TMSI信息，用于全球唯一临时标识一个UE。当AMF为UE新分配5G UE临时标识时，通过本信元携带给UE。|
TAI list|用于将AMF为UE分配的跟踪区列表传递给UE，UE在该跟踪区列表内移动时，不会向AMF发起移动注册更新。该信元编码允许对不同类型列表进行组合。当不同的TAIs共享PLMN标识时，允许对“00”和“01”类型的列表进行进一步编码。|
Allowed NSSAI|允许NSSAI，表示UE请求的NSSAI中，哪些S-NSSAI被网络允许了。网络根据UE请求的NSSAI、UE签约的NSSAI、网络支持的NSSAI进行协商，得到UE允许的NSSAI，下发给UE。|
configured NSSAI|配置NSSAI，表示网络配置给UE使用的NSSAI。UE收到这个配置参数时，可以知道网络下可用的S-NSSAI。|
T3512 value|周期性注册定时器T3512。当T3512超时时，根据UE是否注册紧急业务，发起不同流程：如果UE未注册紧急业务，则发起周期性注册流程。如果UE已注册紧急业务，则发起本地去注册流程。|
（可选）如果AMF为UE分配了新的5G-GUTI，则UE向New AMF发送Registration Complete
消息。
##### AMF重分配流程业务场景 
在注册流程中，(R)AN侧优先根据5G GUAMI查找目标AMF，其次根据Requested NSSAI查找目标AMF，如果(R)AN无法根据UE在AN消息中携带的5G GUAMI或Requested NSSAI查找到目标AMF，会选择一个缺省的AMF（也称为初始AMF）进行注册流程。因此当初始AMF接收到注册请求时，初始AMF可能需要将注册请求重路由到另一个AMF（因为初始AMF不是为UE服务的合适的AMF），因此要执行AMF重分配流程的注册流程，将UE的NAS消息重路由到目标AMF，由目标AMF继续为UE提供注册服务。 
##### AMF重分配流程 
AMF重分配流程如[图2](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__221d12fd-1334-411e-940f-0dab9e3fd8d8)所示。
图2  AMF重分配
[]images/c48f3277d0024b23bb6565804f9b7d52(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
对应[普通注册流程](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__5e19aad1-bd5e-40a7-be9c-2468065dd73d)的步骤1~3，Initial AMF已经收到Registration Request
消息。Registration Request消息中的关键信元参见[表8](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__478a118c-94b7-49ea-b735-3c078398fe2c)。
关键信元|信元解释|示例
---|---|---
registration type|指示请求的注册类型，Bits 3 2 1组合取值代表注册类型，注册类型取值如下：Bits 3 2 10 0 1，初始注册。0 1 0，移动注册更新。0 1 1，周期注册更新。1 0 0，紧急注册。|
Mobile identity|5GS mobile identity信元用于提供SUCI、5G-GUTI、IMEI、IMEISV或5G-S-TMSI。|
Requested NSSAI|用于标识一个S-NSSAI集合。|
（可选）如果需要执行安全流程，则对应[普通注册流程](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__5e19aad1-bd5e-40a7-be9c-2468065dd73d)的步骤4~9。
（可选）如果Initial AMF需要根据UE签约数据判断是否需要重分配AMF，且Initial AMF没有从Old
AMF获取到切片签约信息，但需要基于切片签约信息进行AMF切片选择，则： 
Initial AMF选择一个合适的UDM。 
Initial AMF调用UDM的服务化接口Nudm_SubscriberDataManagement_Get
向UDM请求获取签约切片选择信息。
UDM向AMF返回签约切片选择信息，包含签约的一组S-NSSAI。
（可选）如果Initial AMF已获取到签约的切片信息，则： 
Initial AMF调用NSSF的服务化接口Nnssf_NSSelection_Get
进行切片选择。Nnssf_NSSelection_Get请求消息中的关键信元参见[表9](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__7c858130-a099-4fd0-a6b1-98d3481dee4e)。
关键信元|信元解释|示例
---|---|---
NF type|NF服务消费者的NF类型，比如AMF。|
NF ID|NF服务消费者的NF ID。|
slice-info-request-for-registration|表示在注册过程中向NSSF请求网络切片信息。|
subscribedNssai|包含签约的S-NSSAI列表和每个S-NSSAI的指示。|
NSSF向Intial AMF返回Allowed NSSAI及支持这些NSSAI的对应的AMF Set或AMF地址列表。Nnssf_NSSelection_Get响应消息中的关键信元参见[表10](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__81407b9d-26ef-4cf7-b593-ccf9e38d1ce1)。
关键信元|信元解释|示例
---|---|---
allowedNssaiList|如果NSSF收到请求的NSSAI和签约的S-NSSAI，或者对应请求中的“requestmapping”标志为“true”，则该IE应包含NSSF在服务PLMN中授权的允许的S-NSSAI。|
configuredNssai|如果NSSF没有收到请求的NSSAI，或者请求的NSSAI中包含的S-NSSAI在服务PLMN中无效，则该IE将包含NSSF在服务PLMN中授权的配置的S-NSSAI。|
targetAmfSet|NSSF根据配置以及NSSF是否接收到请求的NSSAI和签约的S-NSSAI决定是否包含此IE。当该IE出现时，该IE应包含目标AMF集合。如果请求消息中包含“请求映射”IE，并且设置为“true”，则不包含此IE。|
candidateAmfList|NSSF根据配置以及NSSF是否接收到请求的NSSAI和签约的S-NSSAI决定是否包含此IE。当该IE出现时，该IE应包含候选AMF(s)的列表。如果请求消息中包含“请求映射”IE，并且设置为“true”，则不包含此IE。|
（可选）Initial AMF向Old AMF发送Namf_Communication_RegistrationCompleteNotify消息并携带失败指标。 
Initial AMF根据NSSF返回的AMF Set或AMF地址列表判断需要将NAS消息（Registration Request
）重路由给其他AMF处理。
Initial AMF向Old AMF发送拒绝指示，通知UE在Initial AMF处的注册流程还未完全结束。Old AMF保持没有收到Namf_Communication_UEContextTransfer
消息之前的状态不变。
（可选）如果NSSF没有返回AMF地址列表，且Initial AMF准备将NAS消息直接路由给Target AMF，则： 
Initial AMF调用NRF的服务化接口Nnrf_NFDiscovery
（包含AMF Set信息）请求获取Target
AMF地址列表。
NRF返回对应的Target AMF列表及对应的地址。 
AMF基于本地策略，分别执行如下操作： 
(7A)： 如果AMF基于本地策略决定将NAS消息直接路由给Target AMF，Initial AMF调用Target
AMF的服务化接口Namf_Communication_N1MessageNotify将NAS消息传递给Target AMF，通过步骤8在Target
AMF发送给(R)AN的第一条消息中更新N2端点信息。 
(7B)：如果AMF基于本地策略决定将NAS消息通过(R)AN路由给Target AMF，则：Initial AMF向(R)AN发送Reroute NAS Request消息并包含NAS消息。(R)AN通过Initial UE Message将NAS消息传递给Target AMF。 
如果Target AMF已经从Initial AMF获取到UE上下文，则继续执行[普通注册流程](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__5e19aad1-bd5e-40a7-be9c-2468065dd73d)的步骤9，11~21；如果Target AMF没有从Initial AMF获取到UE上下文，则继续执行[普通注册流程](1%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__5e19aad1-bd5e-40a7-be9c-2468065dd73d)的步骤4~21。
#### 去注册 
本节包括以下流程： 
UE发起的去注册流程 
网络侧发起的去注册流程 
业务场景 :UE发起的去注册流程和网络侧发起的去注册流程一般应用于以下场景： 
当UE不需要继续访问网络接受服务、或者UE无权限继续访问网络时，会发生去注册流程。如果是UE主动退出网络，UE会主动发起去注册流程通知网络，不再接入5GS。网络通知UE，它不再具有5GS的访问权限。 
当UE无权限继续访问网络时，或者因为操作维护原因网络侧需要UE去注册、或者去注册定时器超时，会发生网络侧发起的去注册流程。 
##### UE发起的去注册流程 
UE发起的去注册流程如[图1](2%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__44850683-22ac-4090-89ec-9732a46919b5)所示。
图1  UE发起的去注册
[]images/UE%E5%8F%91%E8%B5%B7%E7%9A%84%E5%8E%BB%E6%B3%A8%E5%86%8C(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE发送Deregistration Request (UE Originating Deregistration)
消息给AMF，消息中携带5G-GUTI、Deregistration type、Access Type等信息。Deregistration
type指示是否关机。Access Type指示是3GPP接入下去注册、非3GPP接入下去注册，或者两种接入方式下都去注册。Deregistration Request (UE Originating Deregistration)消息中的关键信元参见[表1](2%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__009a5122-7eff-49e7-92c8-3f3c69a729d9)。
关键信元|信元解释|示例
---|---|---
De-registration type|表示去注册类型。对于UE侧触发的去注册，该信元中的Switch off字段指示本次去注册流程是否由关机触发：Switch off（0x00），Normal de-registration，表示正常去注册。Switch off（0x01），Switch off，表示关机。对于网络侧触发的去注册，该信元中的Re-registration required指示终端是否在去注册后发起注册流程：Re-registration required（0x00）：Re-registration required，去注册后无需发起注册流程。Re-registration required（0x01）：Re-registration not required，去注册后需发起初始注册流程。|
Access type|表示待发送给UE的下行信令或用户数据的接入类型，包括：0x01，3GPP access。0x02，Non-3GPP access。0x03，3GPP access and non-3GPP access。|
5GS mobile identity|用于提供SUCI、5G-GUTI、IMEI、IMEISV。|
如果UE在需要去注册的Access Type下没有已建立的PDU会话，则跳过第2步至第5步。 
如果UE在需要去注册的Access
Type下有已建立的PDU会话，则AMF给SMF发送Nsmf_PDUSession_ReleaseSMContext
 Request消息，消息中携带SUPI、PDU
Session ID等信息。
SMF释放PDU会话资源（如IP address / Prefix(es)和会话上下文），并通知UPF释放用户面资源。 
SMF给UPF发送N4会话释放请求消息，消息中携带N4 Session ID等信息。UPF将丢弃所有该PDU会话的缓存报文，释放PDU会话相关的所有资源。 
UPF给SMF返回N4会话释放响应消息。 
SMF给AMF返回Nsmf_PDUSession_ReleaseSMContext
 Response消息。
SMF释放与PCF间会话资源，退订UDM会话管理签约数据改变通知事件。 
如果动态PCC被应用，SMF完成会话管理策略终止过程。 
SMF通过Nudm_SubscriberDataManagement_Unsubscribe
服务，通知UDM退订会话管理签约数据改变通知事件。
SMF通过Nudm_UEContextManagement_Deregistration
服务，通知UDM删除SMF标识、SMF地址、DNN、PDU
Session ID等信息。
AMF发起策略关联终止过程，PCF到UDR/SPR退订该用户的策略签约变更通知。 
如果存在该UE与PCF的会话，且UE在任何接入下已不再注册到网络，则AMF完成AM策略关联终止过程，删除该UE与PCF的会话。
如果存在该UE与PCF的会话，且UE在任何接入下已不再注册到网络，则AMF完成UE策略关联终止过程，删除该UE与PCF的会话。
如果Deregistration type指示不是关机，则AMF给UE发送Deregistration Accept(UE Originating Deregistration)
消息。
如果Deregistration
type指示为关机，则AMF不会向UE发送Deregistration Accept(UE Originating Deregistration)
消息。
AMF通知(R)AN释放N2 UE上下文。 
##### 网络侧发起的去注册流程 
网络侧发起的去注册流程如[图2](2%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__e6160b87-728e-40df-bf98-ef991f757fdd)所示。
图2  网络侧发起的去注册
[]images/%E7%BD%91%E7%BB%9C%E4%BE%A7%E5%8F%91%E8%B5%B7%E7%9A%84%E5%8E%BB%E6%B3%A8%E5%86%8C(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UDM请求删除用户注册管理上下文和PDU会话，则UDM将发送Nudm_UEContextManagement_DeregistrationNotification
消息给AMF，消息中携带SUPI，Access Type，Removal Reason等信息。
Access Type指示是3GPP接入下去注册、非3GPP接入下去注册，或者两种接入方式下都去注册。Removal Reason指示销户。 
如果是UDM触发的去注册，AMF执行去注册流程。AMF发起的去注册过程可以是显式去注册或隐式去注册。Deregistration Request(UE Terminated Deregistration)
消息中携带的关键信元参见[表2](2%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__e26f8581-55a0-44de-b599-85221be140fa)。
对于隐式去注册，AMF不给UE发送Deregistration Request(UE Terminated Deregistration)消息。 
如果UE处于连接态，AMF使用显式去注册方式，给UE发送Deregistration Request(UE Terminated Deregistration)消息，消息中携带Deregistration type，Access
Type等信息。Deregistration type指示UE在去注册后是否需要重注册。 
如果UE处于空闲态，AMF使用显式去注册方式，则AMF寻呼UE。 
关键信元|信元解释|示例
---|---|---
De-registration type|表示去注册类型。对于UE侧触发的去注册，该信元中的Switch off字段指示本次去注册流程是否由关机触发：Switch off（0x00），Normal de-registration，表示正常去注册。Switch off（0x01），Switch off，表示关机。对于网络侧触发的去注册，该信元中的Re-registration required指示终端是否在去注册后发起注册流程：Re-registration required（0x00）：Re-registration required，去注册后无需发起注册流程。Re-registration required（0x01）：Re-registration not required，去注册后需发起初始注册流程。|
5GMM cause|表示网络侧主动发起去注册请求的原因。|
如果去注册流程由UDM触发，那么AMF向UDM返回Nudm_UEContextManagement_DeregistrationNotification
确认消息。
3a. AMF通过Nudm_SubscriberDataManagement_Unsubscribe
服务，通知UDM退订接入和移动签约数据改变通知事件、SMF选择签约数据改变通知事件。
如果UE在需去注册的Access Type下已建立PDU会话，则执行UE发起的去注册流程的第2步到第5步。 
AMF发起策略关联终止过程，PCF到UDR/SPR退订该用户的策略签约变更通知。 
AMF完成AMF发起的AM策略关联终止过程，删除该UE与PCF的会话。 
AMF完成AMF发起的UE策略关联终止过程，删除该UE与PCF的会话。 
如果UE收到了去注册请求消息，则UE给AMF返回Deregistration Accept (UE Terminated Deregistration)
消息。
AMF通知(R)AN释放N2 UE上下文。 
#### 移动性限制 
本节包括以下流程： 
注册拒绝流程 
注册流程 
配置更新流程 
业务请求流程 
基于N2的局内切换流程 
基于N2的局间或跨RAT切换流程 
业务场景 :网络的移动性管理既要保证UE可达和数据传输连续，又要防止UE接入某些受限区域或者请求不该使用的服务。移动性限制就是指UE的接入访问受限、移动受限等，只有3GPP接入才有移动性移动性限制。 
4G中移动性限制通过一些可选特性实现，5G协议中则明确定义了移动性限制有RAT Restriction、Forbidden Area、Service Area Restriction、核心网类型限制四种： 
RAT Restriction：定义UE不能接入的RAT类型。 
Forbidden Area：在该区域禁止UE的接入，UE不能发任何消息给网络。 
Service Area Restriction：分为Allowed Area和Non Allowed Area。UE在Allowed Area可正常接入网络，在Non Allowed Area可以发起周期性更新、注册请求，但不能发起SR和任何会话相关信令。 
核心网类型限制：定义了UE是否可以在一个网络下接入5GC。 
##### 注册拒绝流程 
注册拒绝流程如[图1](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__f260b3dd-3414-4fbb-929b-bf5484f0f53d)所示。
图1  注册拒绝
[]images/%E7%A7%BB%E5%8A%A8%E6%80%A7%E9%99%90%E5%88%B6%E6%B3%A8%E5%86%8C%E6%8B%92%E7%BB%9D(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE判断需要发起注册流程时，发送Registration Request
消息。
NG-RAN收到注册请求消息后，如果消息中有5G-GUTI，则根据5G-GUTI选择AMF，如果消息中没有5G-GUTI，则根据消息中Requested
NSSAI信息，选择一个合适的AMF。 
NG-RAN向AMF发送Registration Request
消息。
AMF处理注册请求消息，包括获取用户信息，安全过程等。 
AMF为了向UDM获取用户签约数据，向UDM发送Nudm_SubscriberDataManagement_Get
消息。
UDM向AMF返回Nudm_SubscriberDataManagement_Get
响应消息，消息中携带ratRestrictions、serviceAreaRestriction等用户签约信息。Nudm_SubscriberDataManagement_Get响应消息中的关键信元参见[表1](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__fa8cfd36-7c2b-4b56-98c3-f69aa393ec8f)。
关键信元|信元解释|示例
---|---|---
ratRestrictions|被限制的RAT类型列表。|
forbiddenAreas|禁止区域列表。|
serviceAreaRestriction|签约业务区限制。|
AMF根据用户签约数据及本地策略，确定UE的移动性限制策略，决定拒绝用户接入。 
AMF向UE发送Registration Reject
消息，消息中携带5GMM Cause等信息。如果Core Network type为不允许接入5GC，则5GMM
Cause值设置为“N1 mode not allowed”。
##### 注册流程 
注册流程如[图2](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__8907661d-5c55-4015-a65e-f1cbee15c2f8)所示。
图2  注册
[]images/3b0cb4dd567d42b1a9f717a02352d17f(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE判断需要发起注册流程时，发送Registration Request
消息给NG-RAN。
NG-RAN收到注册请求消息，如果消息中携带5G-GUTI，则根据5G-GUTI选择AMF，如果消息中没有5G-GUTI，则根据消息中Requested
NSSAI信息，选择一个合适的AMF。 
NG-RAN向AMF发送Registration Request
消息。
AMF处理注册请求消息，包括向Old AMF获取用户信息，向UE获取用户信息，安全过程等。 
AMF向UDM发送Nudm_SubscriberDataManagement_Get
消息，向UDM获取用户签约数据。
UDM向AMF返回Nudm_SubscriberDataManagement_Get
响应消息，消息中携带用户签约信息。Nudm_SubscriberDataManagement_Get响应消息中的关键信元参见[表2](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__e37278be-649d-41fc-93ea-861596d55b4a)。
关键信元|信元解释|示例
---|---|---
ratRestrictions|被限制的RAT类型列表。|
forbiddenAreas|禁止区域列表。|
serviceAreaRestriction|签约业务区限制。|
coreNetworkTypeRestrictions|受限核心网类型列表。|
继续处理注册过程，如确定UE是否需重定向等。 
AMF向PCF发送Npcf_AMPolicyControl_Create
消息，获取用户接入和移动性策略。
PCF向AMF返回Npcf_AMPolicyControl_Create
响应消息。Npcf_AMPolicyControl_Create响应消息中的关键信元参见[表3](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__3ec6815a-d498-4d46-9bcf-99d4b2eb57a0)。
关键信元|信元解释|示例
---|---|---
serviceAreaRestriction|签约业务区限制。|
AMF根据用户签约数据、PCF提供的Service Area Restrictions数据以及本地策略，确定UE的移动性限制策略。 
AMF继续处理注册流程，包括更新PDU会话等，直到AMF向UE发送注册接受消息。 
AMF向UE发送Registration Accept
消息，消息中携带Service Area List等信息。如果需要向(R)AN发送初始上下文建立请求消息，则在请求消息中携带Mobility
Restriction List等信息。Registration Accept消息中的关键信元参见[表4](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__745d7f1f-0216-4661-9ff3-2baeb6cf40e8)。Initial Context Setup Request消息中的关键信元参见[表5](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__2727d230-9066-45c3-922f-1401523ae9cf)。
关键信元|信元解释|示例
---|---|---
Service area list|表示将允许区域的允许跟踪区域列表或不允许区域的禁止跟踪区域列表从网络传输给UE。|
关键信元|信元解释|示例
---|---|---
Mobility Restriction List|定义了后续移动动作的接入限制。其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。|
继续处理注册流程，直到注册流程结束。 
##### 配置更新流程 
配置更新流程如[图3](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__a4998b02-621d-4c33-bb56-e10a8905be85)所示。
图3  配置更新
[]images/%E7%A7%BB%E5%8A%A8%E6%80%A7%E9%99%90%E5%88%B6%E9%85%8D%E7%BD%AE%E6%9B%B4%E6%96%B0(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
由于用户签约数据改变、PCF提供的UE业务接入限制数据改变、本地策略改变，导致用户移动性限制策略改变，需要把新的用户移动性限制策略通知UE。 
AMF向UE发送Configuration Update Command
消息，消息中携带新的Service Area List等信息。Configuration Update Command消息中的关键信元参见[表6](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__0a4d23dc-7001-45bc-bf0b-dad8e38dc4db)。
关键信元|信元解释|示例
---|---|---
Service area list|将允许区域的允许跟踪区域列表或不允许区域的禁止跟踪区域列表从网络传输给UE。|
UE更新Service Area List信息后，向AMF返回Configuration Update Complete
消息。
##### 业务请求流程 
业务请求流程如[图4](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__20a96db7-dfb5-42ef-a03c-084251ea4983)所示。
图4  业务请求
[]images/%E7%A7%BB%E5%8A%A8%E6%80%A7%E9%99%90%E5%88%B6%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE判断需要发起业务请求流程，向NG-RAN发送Service Request
消息。
NG-RAN收到注册请求消息后，向AMF发送Service Request
消息。
AMF处理业务请求消息，包括安全过程、更新PDU会话等。 
AMF向NG-RAN发送Initial Context Setup Request
消息，在请求消息中携带Mobility Restriction List等信息。Initial Context Setup Request消息中的关键信元参见[表7](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__3514b8b0-6a07-4c48-bd4b-c27a5a2eb38b)。
关键信元|信元解释|示例
---|---|---
Mobility Restriction List|定义了后续移动动作的接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。该数据结构中Mobility Restriction List只包含如下信息：RAT Restrictions：RAT限制相关信息。RAT Restrictions包含两部分，PLMN Identity和RAT Restriction Information。Forbidden Area Information：Forbidden Area相关信息。Forbidden Area Information包含两部分，PLMN Identity和Forbidden TACs。|
AMF继续处理业务请求，直到流程结束。 
##### 基于N2的局内切换流程 
基于N2的局内切换流程如[图5](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__e0c28f90-18ca-4278-9a80-753119ec0509)所示。
图5  基于N2的局内切换
[]images/%E7%A7%BB%E5%8A%A8%E6%80%A7%E9%99%90%E5%88%B6N2%E5%B1%80%E5%86%85%E5%88%87%E6%8D%A2(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
Source NG-RAN判断需要发起基于N2的切换时，发送Handover Required
消息。
AMF处理切换需求消息，确定AMF不需改变。 
AMF向NG-RAN发送Handover Request
消息，在请求消息中携带Mobility Restriction List等信息。Handover Request消息中的关键信元参见[表8](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__d05f29c8-58ae-4454-934a-518d34c8c246)。
关键信元|信元解释|示例
---|---|---
Mobility Restriction List|定义了后续移动动作的接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。该数据结构中Mobility Restriction List只包含如下信息：RAT Restrictions：RAT限制相关信息。RAT Restrictions包含两部分，PLMN Identity和RAT Restriction Information。Forbidden Area Information：Forbidden Area相关信息。Forbidden Area Information包含两部分，PLMN Identity和Forbidden TACs。|
AMF继续处理切换，直到流程结束。 
##### 基于N2的局间或跨RAT切换流程 
基于N2的局间或跨RAT切换流程如[图6](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__145a73b6-0849-4124-8542-64bb7176de40)所示。
图6  基于N2的局间或跨RAT切换
[]images/%E7%A7%BB%E5%8A%A8%E6%80%A7%E9%99%90%E5%88%B6%E5%9F%BA%E4%BA%8EN2%E7%9A%84%E5%B1%80%E9%97%B4%E6%88%96%E8%B7%A8RAT%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
基于N2的跨AMF的切换处理完成或垮RAT切换处理完成，且切换过程中Target AMF在Handover Request消息中不携带Mobility
Restriction List信息。 
UE发起切换后的注册流程，向NG-RAN发送Registration Request
消息。
NG-RAN向AMF发送Registration Request
消息。
AMF处理注册请求消息，包括安全过程、获取签约数据、更新PCF等。 
AMF根据用户签约数据、PCF提供的Service Area Restrictions数据以及本地策略，确定UE的移动性限制策略。 
AMF返回Registration Accept
消息，消息中携带Service Area List等信息。AMF向NG-RAN发送DNT消息，消息中携带Mobility
Restriction List和注册接受等信息。DNT消息中的关键信元参见[表9](3%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__245ac083-b93e-459f-81d5-b2fe4793b543)。
关键信元|信元解释|示例
---|---|---
Mobility Restriction List|定义了后续移动动作的接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。该数据结构中Mobility Restriction List包含如下信息：RAT Restrictions：RAT限制相关信息。RAT Restrictions包含两部分，PLMN Identity和RAT Restriction Information。Forbidden Area Information：Forbidden Area相关信息。Forbidden Area Information包含两部分，PLMN Identity和Forbidden TACs。|
NG-RAN向UE发送Registration Accept
消息，UE更新Service Area List等信息。
继续处理注册流程，直到注册流程结束。 
#### UE配置更新 
本节包括以下流程： 
AMF触发的UE配置更新业务流程 
PCF触发的UE配置更新业务流程 
业务场景 :UE的配置可以由网络侧随时发起UE配置更新流程而进行更新。UE配置包括： 
AMF决定和提供的接入和移动性管理相关参数，包括配置的NSSAI及其与签约S-NSSAI的映射，允许的NSSAI及其与签约S-NSSAI的映射。 
当AMF想改变UE的接入和移动性管理相关参数配置时，AMF会发起UE配置更新流程。 
如果UE配置更新流程要求UE发起注册流程，AMF会显式地向UE做指示。 
##### AMF触发的UE配置更新业务流程 
AMF触发的UE配置更新业务流程如[图1](4%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__228076c9-966b-4a9c-8ec7-2adf2f0cb35e)所示。
图1  AMF触发的UE配置更新
[]images/UE%E9%85%8D%E7%BD%AE%E6%9B%B4%E6%96%B0-AMF%E8%A7%A6%E5%8F%91%E7%9A%84UE%E9%85%8D%E7%BD%AE%E6%9B%B4%E6%96%B0(%E9%87%8D%E7%94%A81).png)
由于各种原因（例如：UE移动性改变，来自UDM的用户数据更新通知的接收，网络切片配置的改变）或UE需要执行注册过程，AMF确定UE配置更新的必要性。如果UE处于CM-IDLE，则AMF将触发网络触发的业务请求。 
AMF发送Configuration Update Command
消息给UE。消息中携带相应的参数，主要包括：5G-GUTI
, TAI List, Allowed NSSAI
,
Mapping Of Allowed NSSAI, Configured NSSAI for the Serving PLMN, Mapping
Of Configured NSSAI, rejected S-NSSAIs, NITZ, Mobility Restrictions,
LADN Information, MICO,Configuration update indication
等。其中Configuration update indication
的作用是指示UE是否需要回复ACK或者重新注册。Configuration Update Command消息中的关键信元参见[表1](4%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__0239b7a7-2846-46fe-9a10-e73bdd73828c)。
关键信元|信元解释|示例
---|---|---
Configuration update indication|表示与通用UE配置更新流程相关的附加信息，主要包括UE是否需要发起注册请求和是否需要确认命令消息。是否需要发起注册请求取值及含义如下：registration not requested (0x00)：UE不需要发起注册请求流程。registration requested (0x01)：UE需要发起注册请求流程。是否需要确认命令消息取值及含义如下：acknowledgement not requested (0x00)：UE不确认命令消息。acknowledgement requested (0x01)：UE应确认命令消息。|
（可选）如果UE配置更新指示需要确认UE配置更新命令，则UE将向AMF发送Configuration Update Complete
消息。除NITZ外，AMF应请求对所有UE配置更新的确认消息。如果不需要注册过程，跳过步骤3a，3b，3c，3d和步骤4的过程。
（可选）如果配置更新指示需要注册过程，则根据UE配置更新命令中包含的参数执行以下步骤。 
如果在UE配置更新命令消息中包括了MICO，则UE应在确认之后立即发起注册过程，与网络重新协商MICO模式。后续跳过步骤3b，3c，3d和步骤4。
如果由AMF向UE提供的新的Allowed NSSAI或新的Mapping Of Allowed NSSAI或新的Configured
NSSAI不影响到切片的现有连接，则AMF在步骤2中接收到确认消息后不需要为UE释放NAS信令连接，也不需要立即注册。UE可以立即使用新的Allowed
NSSAI或新的Mapping Of Allowed NSSAI映射。跳过步骤3c和3d。 
如果AMF向UE提供的新的Allowed NSSAI或新的Mapping Of Allowed NSSAI映射或新的Configured
NSSAI影响到网络片的现有连接，则AMF会在UE配置更新命令消息中包括新的Allowed NSSAI以及相关的Mapping Of
Allowed NSSAI（如果可用），以及UE在执行注册过程时不应在接入层信令中提供5G-GUTI的指示。在步骤2中接收到确认之后，AMF将释放UE的NAS信令连接，除非存在与紧急服务相关联的已建立的PDU会话。跳过步骤3d。 
如果在订阅的S-NSSAI更新之后AMF不能确定新的Allowed NSSAI，则AMF不在UE配置更新命令消息中包括任何Allowed
NSSAI，而是指示UE在执行注册过程时不提供Access Stratum信令中的5G-GUTI。 在步骤2中接收到确认消息之后，AMF将释放UE的NAS信令连接，除非存在与紧急服务相关联的已建立的PDU会话。 
（可选）在UE进入CM-IDLE状态之后发起注册过程，并且根据从AMF接收的指示在接入层信令中包含5G-GUTI。 如果存在与紧急服务相关联的已建立的PDU会话并且UE已经接收到执行注册过程的指示，则UE将仅在与紧急服务相关联的PDU会话被释放之后才发起注册过程。 
在UE成功完成所需的注册过程之前，AMF应拒绝来自UE的任何NAS消息（携带用于非紧急PDU会话的PDU会话建立请求）。 
##### PCF触发的UE配置更新业务流程 
PCF触发的UE配置更新业务流程如[图2](4%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__7e2c424a-9af8-4b30-a635-3f0ab817328d)所示。
图2  PCF触发的UE配置更新
[]images/UE%E9%85%8D%E7%BD%AE%E6%9B%B4%E6%96%B0-PCF%E8%A7%A6%E5%8F%91%E7%9A%84UE%E9%85%8D%E7%BD%AE%E6%9B%B4%E6%96%B0(%E9%87%8D%E7%94%A81).png)
PCF触发UE配置更新： 
AMF从PCF接收到Npcf_AMPolicyControl_Create
响应消息（接入和移动性相关信息或UE策略容器（UE接入和PDU会话选择相关信息）或两者皆有）。
AMF从PCF接收到Npcf_AMPolicyControl_Update
响应消息（接入和移动性相关信息或UE策略容器（UE接入和PDU会话选择相关信息）或两者皆有）。
如果UE处于CM-IDLE态，则AMF触发网络触发的服务请求，如果UE不可达，AMF向PCF报告UE策略容器不能被提供给UE。如果UE处于CM-CONNECTED，则AMF透明地将从PCF接收的UE策略容器（UE接入和PDU会话选择相关信息）传送到UE。UE策略容器包括PSI列表，用于通知UE添加、移除或修改一个或多个PSI。
UE执行PSI操作并将结果发送到AMF。AMF将结果透明地传输给PCF。如果一个或多个PSI操作失败，则UE包括UE策略容器（存储的PSI列表）。 
（可选）如果AMF接收到UE策略容器并且PCF订阅了UE策略容器的接收通知，则AMF通过Npcf_AMPolicyControl_Update
请求将UE的响应转发到PCF，该Npcf_AMPolicyControl_Update
请求包括关于策略控制请求触发条件的信息。
（可选）PCF确认AMF接收到Npcf_AMPolicyControl_Update
响应。
### 连接管理 
#### 业务请求 
本节包括以下流程： 
UE触发业务请求流程 
网络触发业务请求流程 
业务场景 :服务请求流程用于空闲状态UE与AMF之间建立信令连接，也可以用于空闲态或连接态UE激活已建立的PDU会话的用户面连接。 
UE发起服务请求的主要目的有： 
将空闲态UE转换成连接态，以发送上行数据/信令。 
作为对Paging消息的响应。 
激活一个PDU会话的用户面连接。 
当UE处于CM-IDLE态，网络侧有数据或信令需要向UE发送时，触发该流程。当UE处于CM-CONNECT态时，也可通过该流程，激活指定的某些PDU会话，建立用户面连接，进行数据传输。 
##### UE触发业务请求流程 
UE触发业务请求流程如[图1](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__b2cbd2fb-0e17-496c-acbd-7ed91691fc77)所示。
图1  UE触发业务请求
[]images/UE%E8%A7%A6%E5%8F%91%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE发送Service Request
消息给RAN。如果仅用于建立信令连接，则不携带"Uplink data status"字段。如果用于数据连接恢复，则通过"Uplink
data status"字段指示期望恢复的PDU Session。"PDU Session Status"指示UE侧可用的PDU Session。Service Request消息中的关键信元参见[表1](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__d0bf380d-9f7b-4f5f-bd32-6e3b3a89224b)。
关键信元|信元解释|示例
---|---|---
Service type|Service type信元用于明确业务请求流程的目的。0x00：信令触发的业务请求。0x01：上行数据触发的业务请求，消息中携带Uplink data status信元。0x02：寻呼触发的业务请求。|
5GS mobile identity|5GS移动身份信元，用于提供5G-S-TMSI。|
RAN侧基于RRC流程中的5G-S-TMSI选择正确的AMF，将Service Request
消息发送给AMF。
AMF对业务请求消息进行合法性校验，如果该消息没有完整性保护或消息完整性保护校验失败，则AMF需要发起安全流程。如果业务请求流程仅用于信令连接建立，则后续步骤4~11及步骤15~22跳过。 
如果Service Request包含"Uplink data status"，AMF调用SMF的服务化接口Nsmf_PDUSession_UpdateSMContext
请求SMF为对应的PDU会话建立用户面连接。Nsmf_PDUSession_UpdateSMContext消息中的关键信元参见[表2](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__34489ece-bc23-4483-aa68-1f9d36ef17c5)。
关键信元|信元解释|示例
---|---|---
UpCnxState|请求激活或去激活PDU会话的用户面连接。SM上下文的UpCnxState属性表示PDU会话的用户面连接状态，取值如下：ACTIVATED：5G-和UPF之间建立N3隧道（上下行分配F-TEID）。DEACTIVATED：5G-和UPF之间没有建立N3隧道。ACTIVATING：正在建立N3隧道（5G-的下行Flow的F-TEID尚未分配）。|
SMF基于用户位置信息进行UPF选择，决策继续使用当前UPF或重选/新建/删除I-UPF。 
如果CN隧道由UPF分配，且CN隧道信息发生改变，SMF向PSA（Anchor UPF）发送PFCP Session Modification Request
消息，请求更新N3及N9及前转隧道信息。如果CN隧道由SMF分配则在步骤7中处理。如果SMF重选或新插入I-UPF，SMF向new
I-UPF发送PFCP Session Modification Request
消息，请求建立N3/N9及前传隧道端点信息。new I-UPF申请用户面隧道资源成功后向SMF发送PFCP Session Modification Response
消息。
如果SMF重选或新插入I-UPF，SMF向PSA（Anchor UPF）发送PFCP Session Modification Request
消息，请求更新N9及前传隧道信息，如果之前A-UPF有下行缓存数据则发送给new I-UPF。如果SMF删除I-UPF，则PSA需要开始缓存N6口下行数据数据报文，并建立前传隧道，为接收从Old I-UPF转发的数据报文做准备。PSA向SMF发送PFCP Session Modification Response
消息。
如果SMF重选或删除I-UPF，SMF向Old I-UPF发送PFCP Session Modification Request
消息，携带新的前传隧道端点信息用于Old I-UPF前传数据，同时通知Old I-UPF删除N3隧道信息。I-UPF向SMF发送PFCP Session Modification Response
消息。
如果I-UPF改变，且Old I-UPF有缓存数据，则Old I-UPF向new I-UPF前传数据。 
如果I-UPF删除，且Old I-UPF有缓存数据，Old I-UPF向UPF(PSA)前传数据。 
SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response响应消息，包含N2 SM信息用于通知RAN更新N3隧道信息。Nsmf_PDUSession_UpdateSMContext消息中的关键信元参见[表3](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__ab473afc-2cf2-4ad9-acac-98cd4b28ffca)。
关键信元|信元解释|示例
---|---|---
n2SmInfo|N2 SM信息，用于通知RAN更新N3隧道信息。|
AMF向RAN发送N2 Request消息包含N2 SM信息用于RAN侧更新N3隧道信息。N2 Request消息中的关键信元参见[表4](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__4869605d-ec34-474f-b036-574afc6051e4)。
关键信元|信元解释|示例
---|---|---
PDUSessionResourceSetupListSUReq|PDU会话资源建立列表。|
S-NSSAI|单网络切片标识。|
pDUSessionAggregate MaximumBitrate|PDU会话聚合最大比特率。|
RAN与UE交互重建用户面承载，在此过程中，AMF向UE发送的Service Accept消息中的关键信元参见[表5](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__42f83ce7-a56a-4fea-8593-a597fac7bdb5)。
关键信元|信元解释|示例
---|---|---
PDU session reactivation result|PDU会话用户面资源建立的结果。|
RAN向AMF发送N2 Request Ack消息包含N2 SM信息用于UPF更新N3隧道RAN侧端点信息，N2 Request Ack消息中的关键信元参见[表6](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__95438e15-eaa1-4406-95cb-8fb70ae894ef)。
关键信元|信元解释|示例
---|---|---
RAN UE NGAP ID|唯一标识NG-RAN节点内NG接口的UE关联。|
PDU Session ID|用于标识一个UE的PDU会话。|
AMF调用SMF的服务化接口Nsmf_PDUSession_UpdateSMContext
 Request透传N2
SM信息。Nsmf_PDUSession_UpdateSMContext消息中的关键信元参见[表7](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__13fca491-9b83-42f9-9c2d-be4d22ddc0d2)。
关键信元|信元解释|示例
---|---|---
n2SmInfo|N2 SM信息，用于恢复用户面相关的N2会话信息。|
如果PCF已订阅SMF位置变化信息且UE的位置改变，SMF触发SM策略修改流程。 
如果SMF重选或新插入I-UPF，SMF向new I-UPF发送PFCP Session Modification Request
消息更新N3隧道RAN侧端点信息，此时I-UPF可以向RAN发送下行数据。new
I-UPF向SMF发送PFCP Session Modification Request
消息。
如果SMF删除I-UPF，SMF向PSA发送PFCP Session Modification Request
消息更新N3隧道RAN侧端点信息，此时PSA可以向RAN发送下行数据。PSA向SMF发送PFCP Session Modification Request
消息。
SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response响应消息。
如果new I-UPF已建立前传隧道，且前传隧道定时器超时，SMF向new I-UPF发送PFCP Session Modification Request
消息释放前传隧道信息，new I-UPF向SMF发送PFCP Session Modification Response
消息。
如果PSA已建立前传隧道，且前传隧道定时器超时，SMF向PSA发送PFCP Session Modification Request
消息释放前传隧道信息，PSA向SMF发送PFCP Session Modification Response
消息。
如果SMF继续使用Old I-UPF，SMF向Old I-UPF发送PFCP Session Modification Request
消息更新N3隧道RAN侧端点信息。如果SMF更新或删除I-UPF，SMF在资源保持定时器超时后向Old I-UPF发送PFCP Session Release Request消息请求释放用户面资源。Old I-UPF向SMF发送PFCP Session Modification Response
/PFCP Session Release Response消息。
##### 网络触发业务请求流程 
网络触发业务请求流程如[图2](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__6eede584-dd1a-493d-b133-15971f681c9e)所示。
图2  网络触发业务请求
[]images/%E7%BD%91%E7%BB%9C%E5%8F%91%E8%B5%B7%E7%9A%84%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UPF收到下行数据报文但没有建立N3隧道，UPF本地缓存下行数据报文。 
UPF向SMF发送N4 Data Notification消息，携带下行数据报文对应的QoS Flow信息。SMF向UPF发送N4
Data Notification Ack消息。 
SMF调用AMF的服务化接口Namf_Communication_N1N2MessageTransfer
携带对应的PDU
Session ID及N2 SM信息。AMF响应SMF的服务化接口调用请求。Namf_Communication_N1N2MessageTransfer消息中的关键信元参见[表8](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__8a95a25f-cca3-4a7e-85b5-9e866db864ba)。
关键信元|信元解释|示例
---|---|---
AreaofVality|表示提供的N2信息有效的TA列表。|
根据UE状态不同，AMF进行不同的处理： 
如果UE处于连接状态，AMF不需要发起寻呼流程，后续流程同[UE触发业务请求流程](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__690ac4d9-2d2c-4e9d-92f4-360da7c3c561)步骤3及步骤12~22。
如果UE处于空闲态，AMF向UE所在注册区域内的所有gNB发送Paging消息。Paging消息中的关键信元参见[表9](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__8320d7c1-1529-4e17-a4cc-55ca541aec09)。
关键信元|信元解释|示例
---|---|---
UE Paging Identity|唯一标识正在发送的消息，所有消息都必须携带该IE。|
TAI List for Paging|寻呼的TAI列表。|
AMF启动寻呼流程定时器，如果超时未收到UE响应，AMF向SMF发送Namf_EventExposure_Notify
消息通知寻呼失败，SMF通知UPF。
UE收到寻呼请求后，发起业务请求流程，同[UE触发业务请求流程](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__690ac4d9-2d2c-4e9d-92f4-360da7c3c561)。Service Request消息中的关键信元参见[表10](9%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__c183063c-4ceb-428a-b6e4-9777ab9edd84)。
关键信元|信元解释|示例
---|---|---
Service type|Service type信元用于明确业务请求流程的目的。0x00：信令，如果是信令原因触发的业务请求，消息中携带PDU session status信元。0x01：数据，如果是上传数据触发的业务请求，UE有待发送的上行用户数据，消息中携带Uplink data status信元。0x02：移动终呼业务，如果是寻呼请求触发的业务请求，消息中携带mobile terminated services信元。|
5GS mobile identity|5GS移动身份信元，用于提供5G-S-TMSI。|
UPF向RAN侧传送下行报文。 
#### AN释放UE上下文 
业务场景 :当UE长时间不活动时，(R)AN上UE不活动定时器超时后，(R)AN会发起AN Rlease流程节省网络资源，AN Rlease流程可以释放UE逻辑上的NG-AP（NG Application Protocol）信令连接和关联的N3用户面连接，以及(R) AN的RRC信令和资源。但是当NG-AP信令连接因(R)AN或AMF故障而断开时，则AN Release由AMF或(R)AN在本地进行，不使用(R)AN和AMF之间的任何信令。AN Release会导致UE的所有UP连接都被去激活。 
##### AN释放UE上下文 
AN释放UE上下文流程如[图1](10%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__aecd87c2-5ebc-4098-9e69-a711c3865b8a)所示。
图1  AN释放UE上下文
[]images/1558059946454(%E9%87%8D%E7%94%A81).png)
流程说明如下。 
（可选）(R)AN检测到需要释放UE上下文，则发送UE Context Release Request
消息给AMF，携带释放原因值。UE Context Release Request消息中关键信元参见[表1](10%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__aa56a3bc-794c-49a5-a90a-66ca4dfa0c87)。
关键信元|信元解释|示例
---|---|---
AMF UE NGAP ID|在AMF内唯一标识UE在NG接口上的关联。|
RAN UE NGAP ID|唯一标识(R)AN节点内NG接口的UE关联。|
Cause|指示NGAP协议特定事件的原因。|
AMF收到(R)AN的UE Context Release Request
消息，或者AMF主动释放N2信令连接，则发送UE Context Release Command
消息给(R)AN。UE Context Release Command消息中关键信元参见[表2](10%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__6f4c711a-3c31-4c39-8ec2-55d32284ca1d)。
关键信元|信元解释|示例
---|---|---
AMF UE NGAP ID|在AMF内唯一标识UE在NG接口上的关联。|
RAN UE NGAP ID|唯一标识(R)AN节点内NG接口的UE关联。|
Cause|指示NGAP协议特定事件的原因。|
（可选）若UE和(R)AN间存在RRC连接，则(R)AN通知UE释放RRC连接。 
(R)AN回复UE Context Release Complete
给AMF进行响应。UE Context Release Complete消息中关键信元参见[表3](10%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__fead8506-4ba6-4e85-b94b-01dd1be64a6e)。
关键信元|信元解释|示例
---|---|---
AMF UE NGAP ID|在AMF内唯一标识UE在NG接口上的关联。|
RAN UE NGAP ID|唯一标识(R)AN节点内NG接口的UE关联。|
（可选）若用户已激活了PDU会话上下文，则AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、导致AN释放UE上下文的原因。Nsmf_PDUSession_UpdateSMContext Request消息中的关键信元参见[表4](10%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__a25b0c23-f48b-40c5-a7fe-d0f1f5ae569e)。
关键信元|信元解释|示例
---|---|---
upCnxState|请求激活或去激活PDU会话的用户面连接。SM上下文的upcnxstate属性表示PDU会话的用户面连接状态，取值如下：ACTIVATED：5G-和UPF之间建立N3隧道（上下行分配F-TEID）。DEACTIVATED：5G-和UPF之间没有建立N3隧道。ACTIVATING：正在建立N3隧道（5G-的下行Flow的F-TEID尚未分配）。|
（可选）SMF发送PFCP Session Modification Request
消息给UPF，通知UPF释放N3用户面隧道。
（可选）UPF回复PFCP Session Modification Response
消息给SMF。
（可选）SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给AMF进行响应。Nsmf_PDUSession_UpdateSMContext Response消息中的关键信元为upCnxState，参见[表4](10%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__a25b0c23-f48b-40c5-a7fe-d0f1f5ae569e)。
#### 连接态下的UE可达性 
本节包括以下流程： 
RRC Inactive Assistance Information的下发 
UE可达性通知请求 
UE活动通知 
RRC连接恢复 
概述 :连接态下的UE可达性，涉及核心网的流程包括RRC Inactive Assistance
Information消息的下发、UE可达性通知请求、UE活动通知、RRC连接恢复。 
##### RRC Inactive Assistance Information的下发 
RRC
Inactive Assistance Information由AMF下发给(R)AN，涉及流程如下： 
业务请求 
基于Xn接口的切换 
基于N2接口的切换 
RRC Inactive Assistance Information下发给(R)AN的流程如[图1](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__2fb3fd97-89d7-4ae8-879b-cc0feadafd01)所示。
图1  RRC Inactive Assistance Information下发给(R)AN
[]images/1557400130560(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
业务请求流程中，AMF通过Initial Context Setup Request
，将RRC Inactive Assistance
Information带给(R)AN。Initial Context Setup Request消息中的关键信元参见[表1](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__adbc532a-acd9-4434-94fb-c623e707a7a5)。
关键信元|信元解释|示例
---|---|---
Core Network Assistance Information for Inactive|提供RRC_INACTIVE配置等辅助信息。|
基于Xn接口的切换流程中，AMF通过Path Switch Request Acknowledge
，将RRC Inactive Assistance
Information带给(R)AN。Path Switch Request Acknowledge消息中的关键信元为Core Network Assistance Information for Inactive，参见[表1](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__adbc532a-acd9-4434-94fb-c623e707a7a5)。
基于N2接口的切换流程中，AMF通过Handover Request
，将RRC Inactive Assistance
Information带给(R)AN。Handover Request消息中的关键信元为Core Network Assistance Information for Inactive，参见[表1](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__adbc532a-acd9-4434-94fb-c623e707a7a5)。
##### UE可达性通知请求 
UE可达性通知请求流程如[图2](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__33f47adf-61ca-4531-8765-5b6d6bdcb8e3)所示。
图2  UE可达性通知请求
[]images/1557400225143(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
在注册或者签约更新流程中，通过Nudm_UEContextManagement_Registration
或者Nudm_UEContextManagement_Update
两个服务操作，UDM将授权进行UE可达性请求的网络功能实体ID，通知给AMF。
若一个业务相关的实体需要请求UE可达性，则发送请求消息给UDM。 
UDM设置URRP_AMF标记，并下发Namf_EventExposure_Subscribe
请求给AMF。Namf_EventExposure_Subscribe消息中的关键信元参见[表2](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__89c02276-21e6-4da2-b61a-810a0a06b7fa)。
关键信元|信元解释|示例
---|---|---
Type|表示需要上报的AMF事件类型。|
网络功能实体也可以直接向AMF请求UE可达性，通过下发Namf_EventExposure_Subscribe
请求给AMF，关键信元参见步骤3。
AMF收到UE可达性请求后，先校验请求UE可达性的网络功能实体是否被授权，再设置URRP_AMF标记。 
若UE处于连接态，则AMF发起N2 Notification过程，向(R)AN查询UE可达性状态。 
##### UE活动通知 
UE活动通知流程如[图3](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__d312114b-9739-4db2-908d-74f43490dd12)所示。
图3  UE活动通知
[]images/1557392477358(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
若AMF发起N2 Notification流程，则(R)AN回复UE Notification。或者UE移动到其他(R)AN，触发其他(R)AN发送Path
Switch Request
给AMF。AMF收到UE Notification或者Path Switch Request
后，表示UE处于活动状态。
根据不同情况，执行以下流程： 
AMF判断URRP_AMF标记有效，且UDM发起了UE可达性请求，则发送Namf_EventExposure_Notify
给UDM，通知UDM
UE可达，UDM将该通知转发给真正请求UE可达性状态的NF。
若UE可达性请求为其他NF发起，则AMF直接发送Namf_EventExposure_Notify
给NF，通知NF UE可达。Namf_EventExposure_Notify消息中的关键信元参见[表3](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__f44b8d0f-13d4-4015-a575-ea7bd60d7dd4)。
关键信元|信元解释|示例
---|---|---
Reachability|UE可达性标识。REACHABLE：表示UE可达。UNREACHABLE：表示UE不可达。REGULATORY_ONLY：表示UE位于不允许区域，仅监管优先业务可访问UE。|
##### RRC连接恢复 
RRC连接恢复流程如[图4](11%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__5e5021ae-aa7e-496b-9e2f-08ca66154547)所示。
图4  RRC连接恢复
[]images/1557400171869(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
处于RRC Inactive状态的UE，检测到存在上行数据或者信令需要发送，则发送RRC连接建立请求给(R)AN。 
若当前接入的(R)AN与源(R)AN之间存在Xn接口，则当前接入的(R)AN通过Xn接口，向源(R)AN请求UE上下文。 
当前接入的(R)AN获取UE上下文成功后，发起Path Switch流程。 
当前接入的(R)AN下发RRC建立成功响应给UE，此时UE进入RRC连接状态。 
### 会话管理 
#### PDU会话建立 
业务场景 :以移动终端上网为例，最终到达Internet来访问相关的网页、视频，畅游互联网世界，这个过程中就必须建立移动终端与Internet之间相应的数据通道，传递数据包，保证业务端到端的传输质量。这些都需要通过会话管理流程实现。 
PDU会话建立业务场景主要包括： 
UE需要与外部网络进行业务交互。 
UE在3GPP与非3GPP接入方式中切换。 
UE从4G PDN连接切换到5G PDU会话。 
##### PDU会话建立 
非漫游PDU会话建立流程如[图1](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__6841e9db-b8fa-4857-8129-d00c6f6b0489)所示。
图1  非漫游PDU会话建立
[]images/4c0dd2687c7547bca8a1f36262871a91(%E9%87%8D%E7%94%A81).png)
UE向AMF发送NAS消息，该消息中包括：S-NSSAI、DNN、PDU Session ID、Request type、N1 SMF container（PDU Session Establishment Request
）等信息。
关键信元|信元解释|示例
---|---|---
PDU session ID|PDU session ID信元用于在5GSM消息中标识一个PDU会话。|
Message type|该信元为Message type类型，在本消息中取值是PDU session establishment request，指示消息类型是：PDU会话建立请求消息。|
Integrity protection maximum data rate|Integrity protection maximum data rate信元用于UE向网络指示UE支持的上下行用户面完整性保护的最大速率。|
PDU Session type|PDU session type信元用于指示PDU会话类型，如：IPv4、IPv6、IPv4v6双栈等等。|
SSC mode|SSC mode信元用于指示SSC模式。业务连续性模式有三种流程。SSC Mode1提供IP连续性，对于SSC Mode1的PDU会话，网络提供给UE的IP地址与为UE选择的UPF保持不变。SSC Mode2不提供IP连续性，当SMF确定提供服务的UPF需要改变时，如当前用户面路径不是最优路径时，SMF会请求UE释放原PDU会话，重新建立一个新的到相同DN的PDU会话，SMF为重新建立的PDU会话选择新的UPF。SSC Mode3提供短暂IP连续性，当SMF决定需要切换会话路径时，如UE移动导致原会话的用户面路径不是最优路径时，SMF会请求UE重新建立一个新的到相同DN的PDU会话，SMF为重新建立的PDU会话选择新的UPF，并在定时器到时或与该DN相关的业务流已转移到新会话上后，请求UE释放原PDU会话。|
AMF执行切片选择过程选择合适的SMF。 
AMF接收到UE的PDU Session Establishment Request
消息，发现是创建新PDU会话时，会执行SMF选择流程为该PDU会话选择SMF。在AMF执行SMF选择过程中，AMF会与NSSF交互获取网络切片信息，再通过NRF发现SMF。
AMF向SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息请求建立PDU会话。
消息中包括：SUPI、DNN、S-NSSAI、PDU Session ID、AMF ID、Request Type、N1 SM container（PDU Session Establishment Request
）、User location information、Access Type、PEI，GPSI、Subscription For PDU Session Status Notification等信息。
关键信元|信元解释|示例
---|---|---
supi|supi信元用于指示用户的SUPI信息，如："imsi-46011xxxxxxxxxx"。|
gpsi|gpsi信元用于指示用户的GPSI号码，如："msisdn-86145 xxxx xxxx"。|
pduSessionId|pduSessionId信元用于指示PDU会话标识，如："5"。|
dnn|dnn信元用于指示数据网络名称，如："3gnet"。|
sNssai|sNssai信元用于指示网络切片标识，包括SST和SD。协议规定编号0-127为标准SST，编号128-255为运营商自定义的SST（具体解释参见协议3GPP TS 23501的"5.15.2.2 Standardised SST values"），目前协议明确编号的标准SST有四种，示例如下：1：表示eMBB，适用于处理5G增强型移动宽带。2：表示uRLLC，适用于处理超可靠的低延迟通信。3：表示mIoT，适用于处理大规模物联网。4：V2X，适用于处理V2X服务。SD用于区分同一种SST之内不同的S-NSSAI。|
servingNfId|servingNfId信元用于指示服务AMF的标识符NFID。|
requestType|requestType信元用于指示PDU会话请求类型。指示是新的PDU会话还是紧急PDU会话，或者是已有的PDU会话或紧急PDU会话，如："requestType":"INITIAL_REQUEST"。|
smContextStatusUri|smContextStatusUri信元用于指示接收短消息SM上下文状态通知消息的回调URI。|
epsInterworkingInd|epsInterworkingInd信元指示PDU会话是否可能移动到EPS，以及EPS互操作过程中是否使用N26接口。|
SMF向UDM发起会话注册和获取签约信息。 
签约信息包括：SSC mode、Session AMBR等，UDM返回：Nudm_SDM_Get UE Session Management Subscription Data Response给SMF。 
Nudm_SDM_Get UE Session Management Subscription Data Response消息中的关键信元参见[表3](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__19411ce3-76ca-4e2c-a912-30481134344e)。
关键信元|信元解释|示例
---|---|---
singleNssai|singleNssai信元用于指示单个网络切片选择辅助信息。|
dnnConfigurations|dnnConfigurations信元用于指示网络切片的附加DNN配置信息。|
sscModes|sscModes用于指示默认/允许的SSC模式。|
iwkEpsInd|iwkEpsInd信元用于指示是否支持EPS互操作。|
5gQosProfile|5gQosProfile信元用于指示数据网络会话关联的5G QoS参数。|
5qi|5qi信元标识一个标准的5G QoS特征组合，5QI值和对应的这组QoS特征一一映射。针对每个会话UDM会签约缺省的5qi。|
arp|arp信元用于控制QoS Flow的创建或修改的优先级。针对每个会话UDM会签约缺省的ARP。|
sessionAmbr|sessionAmbr信元限制了UE每个PDU会话的所有Non-GBR QoS Flow提供的聚合速率最大值。针对每个会话UDM会签约缺省的sessionAmbr。|
staticIpAddress|staticIpAddress信元用于指示签约的UE的静态IP地址。|
SMF向AMF返回Nsmf_PDUSession_CreateSMContext
 Response消息。
根据会话是否成功建立，消息中携带不同的参数。 
若会话建立流程执行成功并创建了SM上下文，则在Nsmf_PDUSession_CreateSMContext Response消息中将SM上下文的ID带给AMF。 
若会话建立流程执行失败，则通过消息中的Cause通知AMF流程失败，AMF释放该会话相关资源，并将N1 SM container（PDU Session Reject）发送给UE。 
SMF执行PCF选择功能选择一个合适的PCF。 
SMF发现是创建新PDU会话时，通过NRF来发现选择一个合适的PCF。 
SMF向PCF发送建立PDU-CAN会话流程。PCF发送Npcf_SMPolicyControl_Create Response给SMF，携带QoS控制策略、计费控制策略、UPF选择策略等信息。 
Npcf_SMPolicyControl_Create Response消息中的关键信元参见[表4](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__059b86cd-1e8e-4eb4-b0bb-829812c341da)。
关键信元|信元解释|示例
---|---|---
sessRules|sessRules信元用于指示一组会话规则，是会话级QoS规则，用于进行PDU会话粒度的策略控制。|
authSessAmbr|authSessAmbr信元用于指示授权的会话AMBR。|
authDefQos|authDefQos信元用于指示授权的默认QoS信息，包括5qi、arp等。|
pccRules|pccRules信元用于指示一组PCC规则，是业务级QoS规则，用于进行QoS Flow粒度的策略控制。会话可以对应多个pccRule和多个qosflow。|
flowInfos|flowInfos信元用于指示一组IP数据流的过滤信息。|
policyCtrlReqTriggers|policyCtrlReqTriggers信元用于指示触发策略更新的事件。|
qosDesc|qosDesc信元用于指示业务级QoS的详细内容，包括5qi、arp等。|
chargingInfo|chargingInfo信元用于指示计费信息，包含PDU会话的CHF地址。|
SMF执行UPF选择功能选择一个合适的UPF。 
SMF根据DNN、DNAI、用户的位置信息等进行UPF选择。 
SMF向PCF发起Session Management Policy Modification（Npcf_SMPolicyControl_Update
）消息。
携带选择的UPF信息，给UE分配的IP地址，获取UPF所需要的控制计费策略。 
Npcf_SMPolicyControl_Update消息中的关键信元参见[表5](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__e650bd99-3608-4603-ae83-558e05fdd9ab)。
关键信元|信元解释|示例
---|---|---
repPolicyCtrlReqTriggers|repPolicyCtrlReqTriggers信元表示策略控制触发需要满足的触发器，比如UE_IP_CH表示使用IP地址变更触发的更新。|
ipv4Address|ipv4Address信元表示用户终端的IPv4地址。|
SMF向第8步选择的UPF发起PFCP会话建立过程。携带给UPF的各种规则，包括PDR、URR、QER、BAR、FAR。
SMF向UPF发送PFCP Session Establishment Request
消息，携带的关键信元参见[表6](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__9c6b9d37-45aa-4ffe-ad26-2d2605444e7b)。
关键信元|信元解释|示例
---|---|---
T_FSEID|包含标识会话的控制面网元分配的唯一标识符。指示SMF控制面SEID，提供用户后续信令交互。|T_FSEID|
Create PDR|表示Packet Detection Rule ，用于详细指示UPF针对每一条QoS Flow的流处理策略。PDR由流规则与流动作组成，PDR区分上下行。N3接口的PDR，称之为上行PDR。N6接口的PDR，称之为下行PDR。|表示Packet Detection Rule ，用于详细指示UPF针对每一条QoS Flow的流处理策略。PDR由流规则与流动作组成，PDR区分上下行。N3接口的PDR，称之为上行PDR。N6接口的PDR，称之为下行PDR。|表示Packet Detection Rule ，用于详细指示UPF针对每一条QoS Flow的流处理策略。PDR由流规则与流动作组成，PDR区分上下行。N3接口的PDR，称之为上行PDR。N6接口的PDR，称之为下行PDR。
PDR ID|Create PDR|指示PFCP会话配置的PDR标识。|
PDI|Create PDR|PDI信元用于表示流规则，包含报文方向（source interface） 和filter（SDF Filter/Application ID）。当入口数据流量的对应字段与PDI中的所有匹配条件都匹配成功表示适合。|
Source interface|Create PDR|Source interface信元用于指示报文方向，PDR区分上下行。比如取值为0表示上行PDR，即收到上行侧的报文进行匹配。也即从N3接口收到的报文进行处理。比如取值为1表示下行PDR，即收到下行侧的报文进行匹配。|
T_FTEID|Create PDR|指示由SMF或UPF分配用户面的隧道端点标识，以及SMF分配的隧道端点标识。此隧道用于N3接口与RAN进行数据传输。|
UE IP Address|Create PDR|指示SMF分配的UE IP地址。|
UE IP Address Pool Identity|Create PDR|指示UPF分配IP地址的地址池名称。|
Create FAR|表示Forwarding Action Rule，用于定义流转发类动作，包括流量转发、丢弃、缓存等。FAR同PDR一样区分上下行。|表示Forwarding Action Rule，用于定义流转发类动作，包括流量转发、丢弃、缓存等。FAR同PDR一样区分上下行。|表示Forwarding Action Rule，用于定义流转发类动作，包括流量转发、丢弃、缓存等。FAR同PDR一样区分上下行。
FAR ID|Create FAR|指示PFCP会话配置的FAR标识。|
Apply Action|Create FAR|指示对数据包适用的动作。|
Forwarding Parameters|Create FAR|指示Apply Action为请求转发数据包，包含用户面功能需要应用的转发指令。|
Destination interface|Create FAR|取值为0表示上行FAR。取值为1表示下行FAR。|
Destination interface type|Create FAR|取值为n6，表示为N6接口。取值为n3 3gpp access，表示为n3接口。|
Create URR|表示Usage Reporting Rule ，用于定义统计类上报动作，如流量耗尽后上报、离线计费上报等。|表示Usage Reporting Rule ，用于定义统计类上报动作，如流量耗尽后上报、离线计费上报等。|表示Usage Reporting Rule ，用于定义统计类上报动作，如流量耗尽后上报、离线计费上报等。
URR ID|Create URR|指示PFCP会话配置的URR标识。|
Create QER|如果对匹配该PFCP会话的一个或多个PDR的报文应用QoS执行或QoS标记动作，则该信元应出现。可能存在多个相同类型的IE来表示多个QER。|如果对匹配该PFCP会话的一个或多个PDR的报文应用QoS执行或QoS标记动作，则该信元应出现。可能存在多个相同类型的IE来表示多个QER。|如果对匹配该PFCP会话的一个或多个PDR的报文应用QoS执行或QoS标记动作，则该信元应出现。可能存在多个相同类型的IE来表示多个QER。
QER ID|Create QER|指示PFCP会话配置的QER标识。|
Gate Status|Create QER|指示数据包是否允许在上行和/或下行方向被允许转发或丢弃。|
QoS Flow Identifier|Create QER|指示QoS Flow标识。|
UPF向SMF发送PFCP Session Establishment Response
响应，携带的关键信元参见[表7](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__ba599ce2-196f-450f-aa82-93fab802f49d)。
关键信元|信元解释|示例
---|---|---
Cause|Cause信元指示接受或拒绝相应的请求消息。|
T_FSEID|T_FSEID用于指示由用户面网元分配的唯一标识符，用于标识会话，由UPF分配。如果原因设置为请求接受（成功），则该信元应出现。|
SMF向AMF发送Namf_Communication_N1N2MessageTransfer
 Request消息请求传递N2资源的请求。
携带N1 Container和N2 Container，其中N1 Container为SMF回复给UE的PDU会话建立响应，N2 Container为SMF向RAN发起的资源建立请求。 
Namf_Communication_N1N2MessageTransfer
Request消息中的关键信元参见[表8](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__8567cf69-ee44-4527-919f-102865517aaa)。
关键信元|信元解释|示例
---|---|---
n1MessageContainer|n1MessageContainer信元用于传递N1 message。|
n2InfoContainer|n2InfoContainer信元用于传递N2 information。|
完成后AMF向SMF发送Namf_Communication_N1N2MessageTransfer
  Response消息，消息中的关键信元参见[表9](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__f2bb4a08-e2a8-4fd3-8ab6-8d03f57c0804)。
关键信元|信元解释|示例
---|---|---
Cause|用于提供AMF上N1/N2消息传输处理的结果。|
AMF向(R)AN发送N2 PDU Session Request（PDU Session Resource Setup Request
）消息请求创建N2 PDU会话，向RAN透传PDU Session Establishment Accept
消息以及SMF发起的AN-specific resource setup消息。
PDU Session Establishment Accept中，携带QoS Rule规则。 
AN-specific resource setup中，携带QoS Profile、UPF的媒体面隧道端点信息。 
PDU Session Resource Setup Request
消息中的关键信元参见[表10](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__f0feec0a-6d39-4d22-bb66-75fe1430fbc5)。
关键信元|信元解释|示例
---|---|---
PDU Session Aggregate Maximum Bit Rate|用于指示会话的AMBR。|
UL NG-U UP TNL Information|用于指示UPF的隧道信息。|
PDU Session Type|用于指示PDU会话类型。|
QoS Flow Identifier|用于指示Qos Flow标识。|
QoS Flow Setup Request List|用于指示业务质量的索引，5QI对应4G的QCI。|
PDU Session Establishment Accept
消息中的关键信元参见[表11](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__5fc9b0ce-fa24-4546-af26-04ef22339186)。
关键信元|信元解释|示例
---|---|---
Selected PDU session type|Selected PDU session type信元用于指示PDU会话类型。|
Authorized QoS rules|Authorized QoS rules信元用于指示UE使用的一组QoS规则。|
PDU address|PDU address信元用于分配给UE以下信息：与PDU会话关联的IPv4地址与所述PDU会话关联的IPv6本地链路地址接口标识与所述PDU会话关联的本地IPv6链路地址接口标识和IPv4地址|
Authorized QoS flow descriptions|QoS flow descriptions信元用于表示UE使用的QoS流描述的集合，每个QoS流描述包含一组参数集合。|
5QI|标识一个标准的5G QoS特征组合，5QI值和对应的这组QoS特征一一映射。|
Session AMBR|Session-AMBR信元用于表示UE建立PDU会话时指示初始签约的PDU会话聚合最大比特速率，或者在网络改变PDU会话聚合最大比特速率时指示新签约的PDU会话聚合最大比特速率。|
(R)AN和UE之间根据AN-specific resource setup消息建立资源连接。 
(R)AN向AMF回复N2 PDU Session Request Ack（PDU Session Resource Setup Response
）消息，携带(R)AN侧下行媒体面隧道端点信息。
PDU Session Resource Setup Response消息中的关键信元参见[表12](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__058c0750-94ca-40a8-9d1d-5bb8e039f159)。
关键信元|信元解释|示例
---|---|---
DL QoS Flow per TNL Information|指示GTP Tunnel信息，包含AN侧的隧道信息，即(R)AN侧IP地址和TEID。|
AMF向SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息。携带N2 Container，Container为(R)AN回复给SMF的资源建立响应，其中有(R)AN侧的媒体面隧道端点信息。
SMF向UPF发起PFCP Session Modification Request
消息，进行PFCP会话修改流程，协商(R)AN侧下行媒体面隧道信息。
PFCP Session Modification Request
消息中的关键信元参见[表13](13%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__4e30bb3c-0202-4b28-8d15-40a34d374ec7)。
关键信元|信元解释|示例
---|---|---
Update FAR|如果需要修改先前为PFCP会话创建的FAR，则该信元应该出现。|如果需要修改先前为PFCP会话创建的FAR，则该信元应该出现。|如果需要修改先前为PFCP会话创建的FAR，则该信元应该出现。
FAR ID|Update FAR|用于标识要更新的FAR。|
Apply Action|Update FAR|用于指示对数据包适用的动作。|
Update Forwarding parameters|Update FAR|用于指示Apply Action为请求转发更新数据包，包含更新的用户面功能需要应用的信息，如gNodeB侧的N3接口地址 。|
SMF向AMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息。
SMF会话建立完成，向AMF发起Nsmf_PDUSession_SMContextStatusNotify（Nsmf_PDUSession_NotifySMContextStatus
消息。
如果UE申请的是IPv6类型的PDU会话，SMF还需要通过UPF向UE发布IPv6路由公告。 
如果会话建立在第4步之后失败了，SMF需要向UDM发起去注册和去订阅的流程。 
#### PDU会话修改 
业务场景 :在UE能力变更、QoS参数有修改等场景下，UE和网络侧都可以发起PDU会话修改流程。 
##### PDU会话修改 
非漫游PDU会话修改流程如[图1](14%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__97711438-9590-40d4-bbd0-b2c99fb71895)所示。
图1  非漫游PDU会话修改
[]images/1aef79587e7e4c098e1542c8d58d38ff(%E9%87%8D%E7%94%A81).png)
PDU会话修改流程可能有多种方式触发，包括以下几种。 
UE发送NAS message消息发起PDU Session Modification Request
，用以对UE使用的QoS策略请求更新。
PDU Session Modification Request
消息中的关键信元参见[表1](14%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__836c7661-e129-49f4-8686-406fb996e214)。
关键信元|信元解释|示例
---|---|---
Requested QoS rules|Requested QoS rules信元用于指示UE需要修改的QoS规则：Create new QoS rule：增加QoS规则。Delete existing QoS rule：减少QoS规则。Modify existing QoS rule and add packet filters：增加packet filter。Modify existing QoS rule and delete packet filters：删除packet filter。|
Requested QoS flow descriptions|Requested QoS flow descriptions信元用于指示需要修改的QoS flow，比如：Create new QoS flow description表示增加QoS flow。|
PDU session ID|PDU session ID信元用于在5GSM消息中标识一个PDU会话。|
PCF向SMF发送消息，通知SMF发起PCF initiated SM Policy Association Modification（Npcf_SMPolicyControl_Update
）流程，用以修改策略。
当UDM的签约数据发生改变时，UDM会通知SMF发起Nudm_SubscriberDataManagement_Notification
流程。
当SMF收到(R)AN发起的策略修改或本地配置的策略发生变化时，SMF可以决定是否发起会话修改流程。 
当(R)AN的资源发生变化时，(R)AN可以通过发送N2 Message消息触发一个会话修改流程。 
SMF可能会发起SMF initiated SM Policy Association Modification（Npcf_SMPolicyControl_Update
）流程，通知订阅事件发生改变。但是如果会话修改流程是由1b或者1d触发，这步会被省略。
Npcf_SMPolicyControl_Update消息中的关键信元参见[表2](14%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__e51e2141-0e59-4869-b6f8-49cfb3d008af)。
关键信元|信元解释|示例
---|---|---
repPolicyCtrlReqTriggers|repPolicyCtrlReqTriggers信元用于指示SMF向PCF上报发生的事件。比如：RES_MO_RE表示SMF接收到UE发送的资源修改请求。|
ueInitResReq|ueInitResReq信元用于指示UE请求特定的QoS处理。|
第三步可能包括下面两种情况。 
如果是UE或(R)AN触发的会话修改流程，则SMF会向AMF发送Response of Nsmf_PDUSession_UpdateSMContext消息。 
如果是SMF/PCF/UDM触发的会话修改流程，则SMF/PCF/UDM会调用AMF的Transfer服务向UE和(R)AN发送Namf_Communication_N1N2MessageTransfer通知。 
AMF可能会向(R)AN发送N2 Session Request（PDU Session Resource Modify Request
）消息。
PDU Session Resource Modify Request
消息中的关键信元参见[表3](14%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__870ac93a-7847-46b2-8c29-0d3c593c3e1b)。
关键信元|信元解释|示例
---|---|---
qosFlowAddOrModifyRequestList|增加、删除、修改QoS flow场景携带该信元。||增加、删除、修改QoS flow场景携带该信元。
QoS Flow Identifier|qosFlowAddOrModifyRequestList|增加的QoS flow对应的QFI。|
QOS flow to release list|qosFlowAddOrModifyRequestList|删除QoS flow携带该信元。|
QoS Flow Level QoS Parameters|qosFlowAddOrModifyRequestList|增加或修改QoS参数时携带该信元，具体包括5QI、ARP等。|
(R)AN可能会与UE发生AN-specific resource momdification消息，将SMF发送过来的信息通知UE。 
(R)AN可能会向AMF发送N2 Session Response（PDU Session Resource Modify Response
）消息，通知QFI的安装情况。
AMF负责将(R)AN发送的消息通过Nsmf_PDUSession_UpdateSMContext
 Request传递给SMF，SMF处理完成后返回Nsmf_PDUSession_UpdateSMContext
 Response。
关键信元|信元解释|示例
---|---|---
n1SmMsg|指示发送给UE的N1 SM Container。|
n2SmInfo|指示发送给(R)AN的N2 SM Information。|
n2SmInfoType|指示N2 SM Information的类型，比如：PDU_RES_MOD_RSP表示为PDU会话修改响应。|
UE发送PDU Session Modification Command
 Ack，通知网络侧UE对会话修改命令的决策结果。
PDU Session Modification Command
消息中的关键信元参见[表5](14%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__d302c3aa-bd59-4267-a607-0d195d6bace7)。
关键信元|信元解释|示例
---|---|---
Authorized QoS rules|QoS规则信元用于指示UE使用的一组QoS规则。|
Mapped EPS bearer contexts|Mapped EPS bearer contexts信元用于指示一个PDU会话对应的EPS上下文集合。|
Authorized QoS flow descriptions|QoS flow descriptions信元用于表示UE使用的QoS流描述集合，每个QoS流描述包含一组参数的集合。|
(R)AN将接收的NAS消息转发至AMF。 
AMF将Nsmf_PDUSession_UpdateSMContext
 Request消息发送给SMF请求更新，SMF处理完成后返回Nsmf_PDUSession_UpdateSMContext
 Response。
SMF根据UE对于会话修改的决策信息通过N4 Session Modification Request（PFCP Session Modification Request
）消息通知UPF更新隧道信息，UPF完成后返回N4 Session Modification Response（PFCP Session Modification Response
）消息。
PFCP Session Modification Request
消息中的关键信元参见[表6](14%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__d5304a15-b132-483e-903a-8618b53536cd)。
关键信元|信元解释|示例
---|---|---
Update FAR|如果需要修改先前为PFCP会话创建的FAR，则该信元应该出现。FAR ID：标识要更新的FAR。Apply Action：指示对数据包适用的动作。Update Forwarding parameters：指示Apply Action为请求转发更新数据包，包含更新的用户面功能需要应用的信息，如gNodeB侧的N3接口地址 。|
SMF将会话更新的结果通知PCF，执行Session Management Policy Modification（Npcf_SMPolicyControl_Update
）流程更新PCF的相关策略信息。
#### PDU会话释放 
摘要 :本节包括以下流程： 
UE发起的释放流程 
AMF发起的会话释放流程 
网络侧发起的会话释放流程 
业务场景 :PDU会话释放的业务场景主要包括： 
当UE不再需要相关业务时。 
PCF、SMF本地配置释放策略。 
UDM订阅数据发生变化。 
DN需要取消UE的接入权限。 
UE不在LADN服务区。 
所有PDU会话的QoS Flow已经释放。 
当UE与AMF的会话状态不匹配，或者UE的网络切片不可用时。 
##### UE发起的释放流程 
UE发起的释放流程示意图如[图1](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__%E9%9D%9E%E6%BC%AB%E6%B8%B8UE%E5%8F%91%E8%B5%B7%E7%9A%84PDU%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B%E5%9B%BE-ADD08BB7)所示。
图1  非漫游UE发起的PDU会话释放流程图
[]images/%E9%9D%9E%E6%BC%AB%E6%B8%B8UE%E5%8F%91%E8%B5%B7%E7%9A%84PDU%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B%E5%9B%BE(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
当UE不再需要相关业务时，UE发送PDU Session Release Request
消息请求释放PDU会话。AMF调用SMF的Nsmf_PDUSession_UpdateSMContext
 Request服务透传UE发起的会话释放申请。
Nsmf_PDUSession_UpdateSMContext消息的关键信元参见[表1](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__a22f2fce-e4a8-43e7-b265-31f7ccaeb7f9)。
关键信元|信元解释|示例
---|---|---
servingNetwork|servingNetwork信元中包括服务核心网运营商PLMN ID。|
n1SmMsg|n1SmMsg信元用于透传N1 SM消息。即透传PDU Session Release Request消息。|
anType|anType信元用于指示PDU会话要关联的接入网类型。比如3GPP_ACCESS表示3GPP接入。|
ueLocation|ueLocation信元用于指示UE的位置信息。|
SMF释放在会话创建时给UE分配的IP地址，并向UPF发送N4 Session Release Request（PFCP Session Deletion Request
）消息，通知用户面释放会话用户面相关的资源。
UPF处理完成后返回N4 Session Release Response（PFCP Session Deletion Response
）消息。
SMF向AMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息。
携带N1 Container和N2 Container，其中N1 Container携带的是需要发送给UE的释放请求，N2
Container里携带的是需要发送给(R)AN的资源释放请求。 
关键信元|信元解释|示例
---|---|---
n1SmMsg|n1SmMsg信元用于指示发送给UE的N1 SM Container。传递的消息是PDU Session Release Command。|
n2SmInfo|n2SmInfo信元用于指示发送给(R)AN的N2 SM Information。传递的消息是PDU Session Resource Release Command。|
AMF通过N2 Resource Release Request消息透传SMF发起的释放RAN侧N2资源的请求及释放UE会话的请求。 
(R)AN释放与UE之间的资源连接，并透传释放UE会话的请求。 
(R)AN向AMF回复N2 Resource Release Ack。 
AMF和SMF之间处理更新会话流程。 
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request，携带N2 Container向SMF传递(R)AN回复的N2 Resource Release Ack消息。
SMF发送Nsmf_PDUSession_UpdateSMContext
 Response，向AMF指示收到了AMF的更新会话服务操作。
UE向(R)AN回复PDU Session Release Ack（PDU Session Release Complete
）。
(R)AN向AMF发送N2 Uplink NAS Transport
消息透传UE的PDU Session Release Ack（PDU Session Release Complete
）。
AMF和SMF之间处理更新会话流程。 
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request，携带N1 Container，内容为UE回复的PDU Session Release Ack（PDU Session Release Complete
）消息。
SMF发送Nsmf_PDUSession_UpdateSMContext
 Response，向AMF指示收到了AMF的更新会话服务操作。
SMF向AMF发送Nsmf_PDUSession_SMContextStatusNotify（Nsmf_PDUSession_NotifySMContextStatus
消息，发起会话释放状态通知。
SMF发起Session Management Policy Termination（Npcf_SMPolicyControl_Delete
）流程，通知PCF释放与UE会话相关的所有资源。
SMF向UDM发起Deregistration/Unsubscription流程，通知UDM释放与UE会话相关的所有资源。 
##### AMF发起的会话释放流程 
AMF发起的会话释放流程示意图如[图2](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__%E9%9D%9E%E6%BC%AB%E6%B8%B8AMF%E5%8F%91%E8%B5%B7%E7%9A%84PDU%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B%E5%9B%BE-ADD0A8A8)所示。
图2  非漫游AMF发起的PDU会话释放流程图
[]images/%E9%9D%9E%E6%BC%AB%E6%B8%B8AMF%E5%8F%91%E8%B5%B7%E7%9A%84PDU%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B%E5%9B%BE(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
AMF调用SMF的Nsmf_PDUSession_ReleaseSMContext
 Request服务发起会话释放请求。

Nsmf_PDUSession_ReleaseSMContext Request关键信元参见[表3](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__383df6c4-d5f8-47c3-a878-a1197baba0aa)。
关键信元|信元解释|示例
---|---|---
Cause|Cause信元用于指示SM上下文释放的原因。|
ueLocation|ueLocation信元用于指示UE的位置信息。|
SMF释放在会话创建时给UE分配的IP地址，并向UPF发送N4 Session Release Request（PFCP Session Deletion Request
）消息，通知用户面释放会话用户面相关的资源。
UPF处理完成后返回N4 Session Release Response（PFCP Session Deletion Response
）消息。
SMF向AMF回复Nsmf_PDUSession_ReleaseSMContext
 Response消息。
SMF发起Session Management Policy Termination（Npcf_SMPolicyControl_Delete
）流程，通知PCF释放与UE会话相关的所有资源。
SMF向UDM发起Deregistration/Unsubscription流程，通知UDM释放与UE会话相关的所有资源。 
##### 网络侧发起的会话释放流程 
网络侧发起的会话释放流程示意图如[图3](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__%E9%9D%9E%E6%BC%AB%E6%B8%B8%E7%BD%91%E7%BB%9C%E4%BE%A7%E5%8F%91%E8%B5%B7%E7%9A%84PDU%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B%E5%9B%BE-ADD39DDD)所示。
图3  非漫游网络侧发起的PDU会话释放流程图
[]images/%E9%9D%9E%E6%BC%AB%E6%B8%B8%E7%BD%91%E7%BB%9C%E4%BE%A7%E5%8F%91%E8%B5%B7%E7%9A%84PDU%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B%E5%9B%BE(%E9%87%8D%E7%94%A81).png)
由PCF、UDM或SMF本地策略触发SMF决策发起会话释放流程。 
SMF释放在会话创建时给UE分配的IP地址，并向UPF发送N4 Session Release Request（PFCP Session Deletion Request
）消息，通知用户面释放会话用户面相关的资源。
UPF处理完成后返回N4 Session Release Response（PFCP Session Deletion Response
）消息。
SMF调用AMF的N1N2传输服务操作通知(R)AN和UE释放资源。 
SMF向AMF发送Namf_Communication_N1N2MessageTransfer
 Request消息，携带N1 Container和N2
Container，其中N1 Container携带的是需要发送给UE的释放请求，N2 Container携带的是需要发送给(R)AN的资源释放请求。
Namf_Communication_N1N2MessageTransfer
 Request消息中的关键信元参见[表4](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__7d546ab4-0866-46a9-aa88-99d997075a01)。
关键信元|信元解释|示例
---|---|---
authority|authority信元用于指示AMF的主机名。|
user-agent|user-agent信元指示消息由SMF发送。|
n1MessageContainer|n1MessageContainer信元用于指示发送给UE的N1 SM Container。|
n2SmInfo|n2SmInfo信元用于指示发送给(R)AN的N2 SM Information。传递的消息是PDU SESSION RESOURCE RELEASE COMMAND。|
AMF回复Namf_Communication_N1N2MessageTransfer
 Response消息。
AMF通过N2 Resource Release Request消息透传SMF发起的释放(R)AN侧N2资源的请求及释放UE会话的请求。N2 Resource Release Request消息中的关键信元参见[表5](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__c3307619-228d-489c-a207-e1742ffd0f23)。
关键信元|信元解释|示例
---|---|---
Cause|Cause信元用于指示会话释放原因。|
(R)AN释放与UE之间的资源连接，并透传释放UE会话的请求。 
(R)AN向AMF回复N2 Resource Release Ack。 
AMF和SMF之间处理更新会话流程。 
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带N2 Container向SMF传递(R)AN回复的N2 Resource Release Ack消息。Nsmf_PDUSession_UpdateSMContext Request（PDU SESSION RESOURCE RELEASE RESPONSE）消息中的关键信元参见[表6](15%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199539__4ffcdc27-a935-44f2-98cd-0998e8e959b1)。
关键信元|信元解释|示例
---|---|---
UE location|UE location信元用于指示UE的位置信息。|
SMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息，向AMF指示收到了AMF的更新会话服务操作。
UE向(R)AN回复PDU Session Release Ack（PDU Session Release Complete
）消息。
(R)AN向AMF发送N2 Uplink NAS Transport
消息透传UE的PDU Session Release Ack（PDU Session Release Complete
）。
AMF和SMF之间处理更新会话流程。 
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带N1 Container，内容为UE回复的PDU Session Release Ack（PDU Session Release Complete
）消息。
SMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息，向AMF指示收到了AMF的更新会话服务操作。
SMF向AMF发送Nsmf_PDUSession_SMContextStatusNotify（Nsmf_PDUSession_NotifySMContextStatus
）消息，发起会话释放状态通知。
SMF发起Session Management Policy Termination（Npcf_SMPolicyControl_Delete
）流程，通知PCF释放与UE会话相关的所有资源。
SMF向UDM发起Deregistration/Unsubscription流程，通知UDM释放与UE会话相关的所有资源。 
#### QoS Flow操作 
摘要 :QoS Flow操作包括对QoS Flow的建立、修改、删除操作，对QoS Flow的三种操作是在PDU Session建立与修改流程中实现。 
对于QoS Flow操作的业务流程描述借用PDU Session操作流程来描述。 
QoS Flow建立 
QoS Flow修改 
QoS Flow释放 
##### QoS Flow建立 
QoS Flow建立包括UE发起的QoS Flow建立与PCF发起的QoS Flow建立，详细描述如下。 
UE发起的QoS Flow建立UE发起的QoS Flow建立流程是通过UE发起的PDU Session修改流程实现，其流程图参见PDU会话建立的业务流程。UE在PDU Session修改消息中携带需要新建的QoS Flow的信息，SMF与PCF协商决策需要新建的QoS Flow，通知UE、(R)AN、UPF建立相关QoS信息。 
PCF发起的QoS Flow建立PCF发起的QoS Flow建立流程是通过PDU Session建立或修改流程实现的，其流程图参见PDU会话建立的业务流程与PDU会话修改的业务流程。PDU Session建立或修改流程中，PCF与SMF交互，将需要新建的QoS Flow相关策略发送给SMF，从而触发QoS Flow建立流程。流程中SMF通知UE、(R)AN、UPF建立相关QoS信息。 
##### QoS Flow修改 
QoS Flow修改包括UE发起的QoS Flow修改与PCF发起的QoS Flow修改，详细描述如下。 
UE发起的QoS Flow修改UE发起的QoS Flow修改流程是通过UE发起的PDU Session修改流程实现，其流程图可参见PDU会话修改的业务流程。UE在PDU Session修改消息中携带需要修改的QoS Flow的信息，SMF与PCF协商决策需要修改的QoS Flow，通知UE、(R)AN、UPF修改相关QoS信息。 
PCF发起的QoS Flow修改PCF发起的QoS Flow修改流程是通过PDU Session修改流程实现的，其流程图参见PDU会话修改的业务流程。PDU Session修改流程中，PCF与SMF交互，将需要修改的QoS Flow相关策略发送给SMF，从而触发QoS Flow修改流程。流程中SMF通知UE、(R)AN、UPF修改相关QoS信息。 
##### QoS Flow释放 
QoS Flow释放包括UE发起的QoS Flow释放、(R)AN发起的QoS Flow释放与PCF发起的QoS Flow释放，详细描述如下。 
UE发起的QoS Flow释放UE发起的QoS Flow释放流程是通过UE发起的PDU Session修改流程实现，其流程图可参见PDU会话修改的业务流程。UE在PDU Session修改消息中携带需要释放的QoS Flow的信息，SMF与PCF协商决策需要释放的QoS Flow，通知UE、(R)AN、UPF删除相关QoS信息。 
(R)AN发起的QoS Flow释放(R)AN发起的QoS Flow释放流程是通过(R)AN发起的PDU Session修改流程实现，其流程图可参见PDU会话修改的业务流程。(R)AN在PDU Session修改消息中携带需要释放的QoS Flow的信息，SMF与PCF协商决策是否需要释放QoS Flow，若需要释放则通知UE、(R)AN、UPF删除相关QoS信息。 
PCF发起的QoS Flow释放PCF发起的QoS Flow释放流程是通过PDU Session修改流程实现的，其流程图参见PDU会话修改的业务流程。PDU Session修改流程中，PCF与SMF交互，将需要释放的QoS Flow相关策略发送给SMF，从而触发QoS Flow释放流程。流程中SMF通知UE、(R)AN、UPF删除相关QoS信息。 
#### 业务连续性模式 
##### 会话和业务的连续性模式类别 
5G系统支持会话和业务的连续性SSC。
4G网络提供[SSC Mode1](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__7313310f-26a6-48fa-bcec-c0c3bf362a58)（IP连续性）。在5G网络中，业务场景更加多样，为了满足不同业务对连续性的不同要求，5G网络支持不同类型的SSC
Mode，在4G网络提供的[SSC Mode1](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__7313310f-26a6-48fa-bcec-c0c3bf362a58)基础上增加了[SSC Mode2](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__6aef3fb6-f41d-4f11-ae9f-283747745ca4)和[SSC Mode3](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__995d0671-a90f-4cd7-85bf-142f32f6ff75)，一个PDU会话的SSC Mode在该会话的生命周期里保持不变。当已有PDU会话的SSC
Mode不满足应用要求时，UE会为应用建立新的PDU会话。
业务连续性模式有三种流程。 
SSC Mode1提供IP连续性，对于SSC Mode1的PDU会话，网络提供给UE的IP地址与为UE选择的UPF保持不变。 
SSC Mode2不提供IP连续性，当SMF确定提供服务的UPF需要改变时，如当前用户面路径不是最优路径时，SMF会请求UE释放原PDU会话，重新建立一个新的到相同DN的PDU会话，SMF为重新建立的PDU会话选择新的UPF。因此SSC Mode2是一种先断后连的方式。 
SSC Mode3提供短暂IP连续性，当SMF决定需要切换会话路径时，如UE移动导致原会话的用户面路径不是最优路径时，SMF会请求UE重新建立一个新的到相同DN的PDU会话，SMF为重新建立的PDU会话选择新的UPF，并在定时器到时或与该DN相关的业务流已转移到新会话上后，请求UE释放原PDU会话。因此SSC Mode3是一种先连后断的方式。 
##### SSC Mode1 
当UE位置变化/AF/PCF触发锚点变化时，SMF会决策服务的UPF是否发生变化。 
如果可以应用UL分类器或者Multi-homing，则SMF不会删除源锚点（UPF）。 
如果不可以应用UL分类器或者Multi-homing，SMF回复PCF失败，可能由PCF发起主动释放会话流程。流程参见PDU会话释放中的网络侧发起的会话释放流程。 
在初始会话建立流程中，AMF给SMF发送的Nsmf_PDUSession_CreateSMContext Request消息的n1SmMsg信元中，UE会携带SSC
mode=1，SMF向UDM获取签约信息。 
UDM在Nudm_SDM_Get Response消息中，会返回allowed sscmode=1。 
SMF通过Namf_Communication_N1N2MessageTransfer Request消息发送给AMF，其中PDU
session establishment accept消息中的Selected SSC mode =1，把选择的sscmode携带给UE。 
##### SSC Mode2 
SSC Mode2情况下，锚点变化流程示意图如[图1](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__fe0ca9b6-2f5c-4459-9e88-6c94d8b48c7c)所示。
图1  SSC Mode2会话的锚点变化
[]images/SSC%20Mode2%E4%BC%9A%E8%AF%9D%E7%9A%84%E9%94%9A%E7%82%B9%E5%8F%98%E5%8C%96(%E9%87%8D%E7%94%A81).png)
当UE位置变化/AF/PCF触发锚点变化时，SMF决策服务的UPF是否发生变化。 
如果可以应用UL分类器或者Multi-homing，则使用相应的特性功能执行。 
如果不可以应用UL分类器或者Multi-homing，则执行后续流程。 
执行PDU会话释放流程，流程参见PDU会话释放
中“业务流程”中的网络侧发起的会话释放流程。
SMF发送Namf_Communication_N1N2MessageTransfer
消息，通过AMF将N1
Container信息发给UE，包含PDU Session ID及指示需要PDU会话重建到相同的DN。其中包括PDU Session
Release Command消息。PDU Session Release Command
消息中的关键信元参见[表1](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__31482005-8693-43d4-bd08-12b19a268be5)。
关键信元|信元解释|示例
---|---|---
5GSM cause|5GSM cause信元用于指示5GSM请求被拒绝的原因。5GSM cause固定值为#Reactivationrequested(0027)。|
UE从第2步接收到指示需要重建PDU会话到相同DN，UE发起新的PDU会话建立流程，SMF为SSC Mode2重建PDU会话选择新的UPF（如[图1](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__fe0ca9b6-2f5c-4459-9e88-6c94d8b48c7c)所示的UPF2）。
##### SSC Mode3 
SSC Mode3情况下，锚点变化流程示意图如[图2](17%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__3593ce44-5270-446a-8f5b-7bd397c3e1b1)所示。
图2  SSC Mode3会话的锚点变化
[]images/SSC%20Mode3%E4%BC%9A%E8%AF%9D%E7%9A%84%E9%94%9A%E7%82%B9%E5%8F%98%E5%8C%96(%E9%87%8D%E7%94%A81).png)
当UE位置变化/AF/PCF触发锚点变化时，SMF决策服务的UPF是否发生变化。 
如果可以应用UL分类器或者Multi-homing，则使用相应的特性功能执行。 
如果不可以应用UL分类器或者Multi-homing，则执行后续流程。 
SMF发送Namf_Communication_N1N2MessageTransfer
消息，携带PDU Session ID、SMF Reallocation requested indication, N1 SM
container (PDU Session Modification Command
(Cause, ePCO (PDU Session Address Lifetime value)))，其中：
PDU Session ID指示已分配的PDU会话。 
SMF Reallocation requested indication表示是否请求SMF重选。 
PDU Session Modification Command中的Cause指示需要重建PDU会话到相同DN。ePCO中的PDU Session Address Lifetime value发给UE，指示网络希望保留PDU会话的时长。PDU Session Modification Command消息中的关键信元参见表2。表2  PDU Session Modification Command消息中的关键信元关键信元信元解释示例5GSM cause5GSM cause信元用于指示5GSM请求被拒绝的原因。5GSM cause固定值为Reactivation requested(0x27)。 
消息发送后，SMF启动该PDU Session Address Lifetime value的PDU会话释放定时器。 
AMF转发NAS消息给UE。UE会接收到PDU Session Modification Command
消息中的PDU Session Address Lifetime value，并启动定时器。
UE接收到PDU Session Modification Command
消息，会触发PDU会话建立流程，申请建立到相同DN的数据通道，本流程中的处理与PDU会话建立
中的流程差异如下：
在非漫游PDU会话建立流程中的第1步，UE根据SSC Mode生成新的PDU Session ID，并向AMF发送PDU Session Establishment Request消息，消息中包含新的PDU
Session ID，以及需要释放的原PDU Session ID。NAS请求消息中的PDU会话ID包含新的PDU Session
ID 
在非漫游PDU会话建立流程中的第2步，如果本流程请求SMF重选，则AMF选择不同的SMF，否则AMF发送Nsmf_PDUSession_CreateSMContext Request消息给原SMF。 
在非漫游PDU会话建立流程中的第3步，AMF在Nsmf_PDUSession_CreateSMContext Request消息中同时携带新的PDU Session ID和原PDU Session ID。SMF检测到PDU会话建立请求触发是基于携带的原PDU
Session ID。SMF保存新的PDU Session ID，为新的PDU会话选择新的会话锚点（如图2中的UPF2）。 
新的PDU会话建立后，UE将所有新业务关联到新PDU会话的IP地址，也可能提前将现存的业务流从原PDU会话移到新的PDU会话。 
第3步提供的定时器超时之前（一旦UE统一所有业务使用新的PDU会话或不再需要会话），UE发起原PDU会话释放流程，或定时器超时，SMF发起原PDU会话释放流程。 
#### PDU会话支持Uplink Classifier 
PDU会话支持Uplink Classifier的建立流程如[图1](18%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__389824f2-496a-4652-911a-ea99232fed12)所示。
图1  PDU会话支持Uplink Classifier的建立
[]images/PDU%E4%BC%9A%E8%AF%9D%E6%94%AF%E6%8C%81Uplink%20Classifier%E7%9A%84%E5%BB%BA%E7%AB%8B(%E9%87%8D%E7%94%A81).png)
UE注册到网络中，建立PDU会话，会话锚点是UPF1。 
AF向PCF请求影响业务路由。
PCF向SMF发送Npcf_SMPolicyControl_UpdateNotify
消息，消息中包括DNAI。
SMF根据业务路由信息进行UPF重选，选择的结果为：UPF3为Uplink
Classifier，UPF2为业务App2数据的锚点，UPF1为业务App1数据的锚点。
SMF向UPF2发送N4 Session Establish Request（PFCP Session Establishment Request
）消息，消息中携带PDR、URR、FAR、QER，通知其建立N4会话。
PFCP Session Establishment
Request消息中的关键信元参见[表1](18%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__304d9373-c3c9-45a8-9a61-31836f0928a7)。
关键信元|信元解释|示例
---|---|---
T_FSEID|指示SMF控制面SEID，提供用户后续信令交互。|
Create PDR|用于指示上行报文，包括：PDR ID：指示PFCP会话配置的PDR标识。Precedence：指示PDR在PFCP会话的所有PDRs中应用的优先级。PDI：指示匹配的报文。Source Interface：上下行两个Create PDR。T_FTEID：上行为N9隧道。|
Create FAR|FAR ID：指示PFCP会话配置的FAR标识。Apply Action：指示对数据包适用的动作。Forwarding Parameters：指示Apply Action为请求转发数据包，包含用户面功能需要应用的转发指令。Destination Interface ：下行指向ULCL UPF的N9隧道。T_FTEID：下行指向N9隧道。|
UPF2完成会话建立，向SMF发送N4 Session Establish Response（PFCP Session Establishment Response
）消息，包括N9
TunnelInfo等。
SMF向UPF3（ULCL UPF）发送N4 Session Establish Request（PFCP Session Establishment Request
）消息，消息中携带PDR、URR、FAR、QER，通知其建立N4会话。
PFCP Session Establishment Request消息中的关键信元参见[表2](18%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__b2b250dd-b3bb-4dce-aab3-886738010777)。
关键信元|信元解释|示例
---|---|---
CP F-SEID|指示SMF控制面SEID，提供用户后续信令交互。|
Create PDR|上行报文PDR ID：指示PFCP会话配置的PDR标识。Precedence：指示PDR在PFCP会话的所有PDRs中应用的优先级。PDI：指示匹配的报文。Source Interface：有4个CreatePDR。T_FTEID：上行N3隧道，下行N9隧道。|
Create FAR|FAR ID：指示PFCP会话配置的FAR标识。Apply Action：指示对数据包适用的动作。Forwarding Parameters：指示Apply Action为请求转发数据包，包含用户面功能需要应用的转发指令。Destination Interface ：下行指向。T_FTEID：上行N3隧道，下行N9隧道。|
UPF3完成会话建立，向SMF发送N4 Session Establish Response（PFCP Session Establishment Response
）消息，包括N3&N9
TunnelInfo等。
SMF向UPF1发送N4 Session Update Request消息，消息中携带PDR、URR、FAR、QER，通知其更新N4会话。UPF1完成会话更新，向SMF发送N4
Session Update Response消息。 
（可选）SMF向UPF2发送N4 Session Update Request消息，通知其更新N4会话。UPF2完成会话更新，向SMF发送N4
Session Update Response消息。 
SMF构造Namf_Communication_N1N2MessageTransfer
消息，携带N2 SM Container信元，更新N3 TEID等。
AMF根据N2 SM Container携带的信息，构造PDU Session Resource
Modify Request
，通知RAN更新remote N3 TEID等。
AMF构造Namf_Communication_N1N2MessageTransfer
 ACK消息，通知SMF已经将N2信息发送给RAN。
RAN成功更新remote N3 info等参数后，构造PDU Session
Resource Modify Response
。
AMF构造Nsmf_PDUSession_UpdateSMContext
 Request消息，将RAN的响应结果通知到SMF。
SMF处理RAN的响应信息，构造Nsmf_PDUSession_UpdateSMContext
 Response消息，响应AMF。
建立完成后的数据转发路径如下： 
Uplink data（App1）：UE->RAN->UPF3（Uplink Classifier）->UPF1（PSA1）->DN 
Downlink data（App1）：DN->UPF1（PSA1）->UPF3（Uplink Classifier）->RAN->UE 
Uplink data（App2）：UE->RAN->UPF3（Uplink Classifier）->UPF2（PSA2）->DN 
Downlink data（App2）：DN->UPF2（PSA2）->UPF3（Uplink Classifier）->RAN->UE 
#### PDU会话支持Multi-homing 
PDU会话支持Multi-homing的建立流程如[图1](19%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__c0bcfaa5-c5da-4116-9f26-b3107f5dac07)所示。
图1  PDU会话支持Multi-homing的建立
[]images/PDU%E4%BC%9A%E8%AF%9D%E6%94%AF%E6%8C%81Multi-homing%E7%9A%84%E5%BB%BA%E7%AB%8B(%E9%87%8D%E7%94%A81).png)
UE注册到网络中，建立PDU会话，会话锚点是UPF1。 
AF向PCF请求影响业务路由。
PCF向SMF发送Npcf_SMPolicyControl_UpdateNotify
消息，消息中包括DNAI。
SMF根据业务路由信息进行UPF重选，选择的结果为：UPF3为Branching Point，UPF2为业务App2数据的锚点，UPF1为业务App1数据的锚点。
SMF向UPF2发送N4 Session Establish Request（PFCP Session Establishment Request
）消息，消息中携带PDR、URR、FAR、QER，通知其建立N4会话。
UPF2完成会话建立，向SMF发送N4 Session Establish Response（PFCP Session Establishment Response
）消息，包括N9 TunnelInfo等。
SMF向UPF3发送N4 Session Establish Request（PFCP Session Establishment Request
）消息，消息中携带PDR、URR、FAR、QER，通知其建立N4会话。
UPF3完成会话建立，向SMF发送N4 Session Establish Response（PFCP Session Establishment Response
）消息，包括N3&N9 TunnelInfo等。
SMF向UPF1发送N4 Session Update Request消息，消息中携带PDR、URR、FAR、QER，通知其更新N4会话。UPF1完成会话更新，向SMF发送N4 Session Update Response消息。 
（可选）SMF向UPF2发送N4 Session Update Request消息，通知其更新N4会话。UPF2完成会话更新，向SMF发送N4 Session Update Response消息。 
SMF构造Namf_Communication_N1N2MessageTransfer
消息，携带N2 SM Container信元，更新N3 TEID等。
AMF根据N2 SM Container携带的信息，构造PDU Session Resource Modify Request
，通知RAN更新remote N3 TEID等。
AMF构造Namf_Communication_N1N2MessageTransfer
 ACK消息，通知SMF已经将N2信息发送给RAN。
RAN成功更新remote N3 info等参数后，构造PDU Session Resource Modify Response
。
AMF构造Nsmf_PDUSession_UpdateSMContext
 Request消息，将RAN的响应结果通知到SMF。
SMF处理RAN的响应信息，构造Nsmf_PDUSession_UpdateSMContext
 Response消息，响应AMF。
建立完成后的数据转发路径如下： 
Uplink data（App1）：UE->RAN->UPF3（Branching Point）->UPF1（PSA1）->DN 
Downlink data（App1）：DN->UPF1（PSA1）->UPF3（Branching Point）->RAN->UE 
Uplink data（App2）：UE->RAN->UPF3（Branching Point）->UPF2（PSA2）->DN 
Downlink data（App2）：DN->UPF2（PSA2）->UPF3（Branching Point）->RAN->UE 
其中Data（App1）代表经过IP锚点UPF1（PSA1）接入DN的数据；Data（App2）代表经过分支锚点UPF2（PSA2）接入DN的数据，典型的是Local DN的数据。 
#### 支持Local Area Data Network 
支持LADN业务流程如[图1](20%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__b9254c65-f014-453f-a5e3-e2fc70b1e27e)所示。
图1  支持LADN业务
[]images/%E6%94%AF%E6%8C%81LAND%E4%B8%9A%E5%8A%A1(%E9%87%8D%E7%94%A81).png)
UE检测需要发起注册流程，发送Registration Request
消息，经过(R)AN给AMF。
执行注册接受前的鉴权、PEI检查、向UDM请求签约数据等过程。 
AMF根据签约、本地配置，生成LADN信息，并在Registration Accept
消息中带给UE。
当处于LADN服务区域时，UE检测需要新建LADN PDU会话，则发起PDU会话激活流程。LADN PDU会话激活后，SMF发送Namf_EventExposure_Subscribe
 Request，向AMF订阅移动事件通知，携带LADN DNN。
AMF创建移动事件通知订阅上下文，并回复Namf_EventExposure_Subscribe
 Response消息给SMF。
AMF根据步骤5订阅回复消息中的LADN DNN查询本地配置，生成Area of Interest，并在Location Reporting Control
消息中携带给(R)AN。
(R)AN回复Location Report
消息给AMF，携带UE Presence in Area of Interest和UE位置。
当(R)AN检测到UE presence in Area of Interest发生变化，则上报Location Report
消息给AMF，携带最新的UE presence in Area of Inerest和UE位置信息。
AMF发送Namf_EventExposure_Notify
消息给SMF，携带(R)AN上报的UE Presence in Area of Interest和UE位置信息。
Namf_EventExposure_Notify消息中的关键信元参见[表1](20%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#T_1554257199554__04fa83ee-0dfb-454e-882b-78767c126dc5)。
关键信元|信元解释|示例
---|---|---
areaList|areaList信元用于指示地区信息。|
location|location信元用于指示UE位置信息。|
根据UE Presence in Area of Interest的值，执行对应的流程。 
若UE Presence in Area of Interest为OUT，即UE已经移出LADN服务区域，则执行以下流程。SMF根据本地配置，触发PDU会话释放，或者去活PDU会话用户面。触发PDU会话释放则执行以下步骤。若本地配置释放PDU会话，则SMF发送Namf_EventExposure_Unsubscribe Request消息给AMF，通知AMF去订阅步骤4中订阅的移动事件通知。AMF删除对应的移动事件通知订阅上下文，回复Namf_EventExposure_Unsubscribe Response消息给SMF。AMF下发Location Reporting Control给(R)AN，通知(R)AN停止位置报告。 
若UE Presence in Area of Interest为IN，即UE已经移入LADN服务区域，则执行以下流程。SMF确保下行数据通知正常启用。当收到下行数据时，SMF触发网络侧业务请求流程。 
若UE Presence in Area of Interest为UNKNOWN，即无法确定UE是否处于或者移出LADN服务区域，则执行以下流程。SMF确保下行数据通知正常启用。当收到下行数据时，SMF触发网络侧业务请求流程。 
### 切换 
#### 基于Xn接口的切换 
根据切换过程中，是否存在I-UPF改变，基于Xn接口的切换划分如下三种场景： 
基于Xn口的切换，无UPF变化 
基于Xn口的切换，重选I-UPF 
基于Xn口的切换，移除I-UPF 
业务场景 :切换流程用于将UE从一个源NG-RAN节点切换到一个目标NG-RAN节点，切换过程中使用Xn接口。新的无线条件、负载均衡或特定的服务都可能触发切换流程。 
##### 基于Xn口的切换，无UPF变化 
基于Xn口的切换，无I-UPF变化的流程如[图1](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__c2927583-4d71-4db1-984a-1cda3bd4ee61)所示。
图1  基于Xn口的切换，无I-UPF变化
[]images/%E5%88%87%E6%8D%A2-%E5%9F%BA%E4%BA%8EXn%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%EF%BC%8C%E6%97%A0I-UPF%E5%8F%98%E5%8C%96(%E9%87%8D%E7%94%A81).png)
Target NR发送Path Switch Request
消息给AMF，携带Source AMF UE NGAP ID、UE Location
Information、UE Security Capabilities、PDU Session To Be Switched in
Downlink List等信息。Path Switch Request消息中的关键信元参见[表1](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__4e5bfa93-ff3e-45c1-936c-e0cb3e706f49)。
关键信元|信元解释|示例
---|---|---
User Location Information|用于提供UE的位置信息。|
PDU Session Resource to be Switched in Downlink List|用于携带需要切换的PDU会话列表，每个PDU会话包含PDUSessionID和pathSwitchRequestTransfer。pathSwitchRequestTransfer中包括目标gNB分配的N3接口下行数据的TunnelID信息。|
AMF收到Path Switch Request
消息后，针对PDU
Session To Be Switched in Downlink List的每一个会话，发送Nsmf_PDUSession_UpdateSMContext
 Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。
SMF根据ueLocation判断UPF可以继续服务于UE，发送PFCP Session
Modification Request
消息给UPF，携带Target NR N3隧道信息。PFCP Session Modification
Request消息中的关键信元参见[表2](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__7e79ec04-aae8-49de-950d-d22a90db9eff)。
关键信元|信元解释|示例
---|---|---
Update FAR|用于更新下行PDR关联的FAR。|
UPF回复PFCP Session Modification Response
消息给SMF，携带UPF N3隧道信息。
SMF收到UPF响应后，回复Nsmf_PDUSession_UpdateSMContext
Response消息给AMF，携带UPF N3隧道信息。
AMF收到SMF响应后，回复Path Switch Request Acknowledge
消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU
Session To Be Switched in Uplink List等信息。
##### 基于Xn口的切换，重选I-UPF 
基于Xn口的切换，重选I-UPF的流程如[图2](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__edf2ed0f-bdbf-48c8-956d-9bb62d8dc37c)所示。当切换前PDU会话的用户面路径中有I-UPF，此I-UPF就是Source I-UPF。
图2  基于Xn口的切换，重选I-UPF
[]images/%E5%9F%BA%E4%BA%8EXn%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%EF%BC%8C%E9%87%8D%E9%80%89I-UPF(%E9%87%8D%E7%94%A81).png)
Target NR发送Path Switch Request
消息给AMF，携带Source
AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU
Session To Be Switched in Downlink List等信息。Path Switch Request消息中的关键信元参见[表3](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__89e01821-7324-41cb-b9a4-2c19dd07b15e)。
关键信元|信元解释|示例
---|---|---
user Location Information|提供UE的位置信息。|
PDU Session To Be Switched in Downlink List|用于携带需要切换的PDU会话列表，每个PDU会话包含PDUSessionID和pathSwitchRequestTransfer。pathSwitchRequestTransfer中包括目标gNB分配的N3接口下行数据的Tunnel ID信息。|
AMF收到Path Switch Request
后，针对PDU
Session To Be Switched in Downlink List的每一个会话，发送Nsmf_PDUSession_UpdateSMContext
 Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。
SMF收到Nsmf_PDUSession_UpdateSMContext
 Request后，根据ueLocation检测到用户位置发生变化，调用UPF选择功能重新选择I-UPF，最终选择的I-UPF与原有的I-UPF不同。SMF发送PFCP Session Establishment Request
消息给新选择的Target
I-UPF，携带Target NR N3隧道信息以及UPF（PSA）N9隧道信息。PFCP Session Establishment
Request消息中的关键信元参见[表4](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__caa7b1ff-905b-48b8-8b18-d7888ff7a8d8)。
关键信元|信元解释|示例
---|---|---
Create FAR|用于建立下行PDR关联的FAR。|
Target I-UPF回复PFCP Session Establishment
Response
消息给SMF，携带Target I-UPF N3隧道信息以及N9隧道信息。
SMF发送PFCP Session Modification Request
消息给UPF（PSA），携带Target I-UPF N9隧道信息。PFCP Session Modification Request消息中的关键信元参见[表5](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__fe99ca61-6a44-413a-a75c-49c37e49105b)。
关键信元|信元解释|示例
---|---|---
Update FAR|用于更新下行PDR关联的FAR。|
UPF（PSA）回复PFCP Session Modification
Response
消息给SMF，携带UPF（PSA） N9隧道信息。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给AMF，携带Target I-UPF N3隧道信息，并启动资源保护定时器。Nsmf_PDUSession_UpdateSMContext
Response消息中的关键信元参见[表6](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__995741a9-c581-4d29-bd7c-1d7f75105485)。 
关键信元|信元解释|示例
---|---|---
UL NG-U UP TNL Information|用于通知基站Target I-UPF N3隧道信息。|
AMF收到SMF响应后，回复Path Switch Request Acknowledge
消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU
Session To Be Switched in Uplink List等信息。
（可选）如果步骤7中启动的定时器超时后，SMF发送PFCP Session Release Request消息给Source
I-UPF，通知Source I-UPF释放用户上下文。Source I-UPF释放用户上下文，回复PFCP Session Release
Response给SMF。 
（可选）Source I-UPF释放用户上下文，回复PFCP Session Release Response给SMF。 
##### 基于Xn口的切换，移除I-UPF 
基于Xn口的切换，移除I-UPF的流程如[图3](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__0b2b601f-0260-4af7-9b7c-c78bccfb836e)所示。
图3  基于Xn口的切换，移除I-UPF
[]images/%E5%9F%BA%E4%BA%8EXn%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%EF%BC%8C%E7%A7%BB%E5%87%BAI-UPF(%E9%87%8D%E7%94%A81).png)
Target NR发送Path Switch Request
消息给AMF，携带Source
AMF UE NGAP ID、UE Location Information、UE Security Capabilities、PDU
Session To Be Switched in Downlink List等信息。Path Switch Request消息中的关键信元参见[表7](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__6dec9076-83be-4e2b-ac49-f05554e5434b)。
关键信元|信元解释|示例
---|---|---
UE Location Information|提供UE的位置信息。|
PDU Session To Be Switched in Downlink List|用于携带需要切换的PDU会话列表，每个PDU会话包含PDUSessionID和pathSwitchRequestTransfer。pathSwitchRequestTransfer中包括目标gNB分配的N3接口下行数据的Tunnel ID信息。|
AMF收到Path Switch Request
消息后，针对PDU
Session To Be Switched in Downlink List每一个会话，发送Nsmf_PDUSession_UpdateSMContext
 Request消息给会话归属的SMF，携带ueLocation、n2SmInfo等信息。
SMF收到Nsmf_PDUSession_UpdateSMContext
 Request消息后，根据ueLocation检测到用户位置发生改变，调用UPF选择功能重新选择I-UPF，最终选择的I-UPF为UPF（PSA）。SMF发送PFCP Session Modification Request
消息给UPF（PSA），携带Target
NR的N3隧道信息。启动定时器，该定时器超时后通知Source I-UPF释放资源。PFCP Session Modification
Request消息中的关键信元参见[表8](1601430396095%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#z783df6c13b1341b38f6e1f182eb4eb29__2212fdf8-c757-4fca-81ae-4b740cee3ab9)。
关键信元|信元解释|示例
---|---|---
Update FAR|用于建立下行PDR关联的FAR。|
UPF（PSA）回复PFCP Session Modification
Response
消息给SMF，携带UPF（PSA） N3隧道信息。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给AMF，携带UPF（PSA） N3隧道信息。
AMF收到SMF响应后，回复Path Switch Request Acknowledge
消息给Target NR，携带AMF UE NGAP ID、RAN UE NGAP ID、Security Context、PDU
Session To Be Switched in Uplink List等信息。
SMF发送[PFCP Session Modification](None)消息给UPF（PSA），通知UPF（PSA）释放N9隧道信息。
（可选）步骤3启动的定时器超时后，SMF发送PFCP Session Release Request消息给Source
I-UPF，通知Source I-UPF释放用户上下文。 
（可选）Source I-UPF释放用户上下文，回复PFCP Session Release Response给SMF。 
#### 基于N2接口的切换 
根据切换过程中是否存在I-UPF的变化，基于N2接口的切换可以划分为如下场景： 
基于N2接口的切换，无I-UPF变化 
基于N2接口的切换，重选I-UPF 
基于N2接口的切换，移除I-UPF 
业务场景 :切换流程用于将UE从一个源NG-RAN节点切换到一个目标NG-RAN节点，切换过程中使用N2接口。新携带SM N2 Information的无线条件、负载均衡或特定的服务都可能触发切换流程。 
当NG-RAN之间不存在Xn接口时或者基于Xn接口的切换流程失败（比如，目标NG-RAN与源UPF之间无IP连接）时，需要通过N2接口进行切换，基于N2接口的切换流程分为准备阶段和执行阶段。 
准备阶段：源NG-RAN节点发起切换流程后，准备阶段主要完成的工作是目标侧核心网和无线网的资源分配，包括SMF选择新的目标UPF作为中间UPF、目标UPF和UPF（PSA）之间建立N9接口隧道、目标NG-RAN分配无线资源、目标NG-RAN和目标UPF之间建立N3接口隧道、目标AMF上建立UE上下文。 
执行阶段：源NG-RAN节点通知UE切换，UE切换后，目标NG-RAN通知目标AMF， 目标AMF通知源AMF，源AMF释放被拒绝切换的会话。目标SMF将目标UPF的信息通知UPF（PSA
），完成下行数据通道的切换。切换完成后，一般后续还有跟随有注册流程，释放源UPF和源NG-RAN上面的资源，并释放间接数据转发隧道的资源。 
##### 基于N2接口的切换，无I-UPF变化 
基于N2接口的切换，无I-UPF变化的流程如[图1](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__e3058f9a-ac17-482b-bea7-e066c2a39640)所示。
图1  基于N2接口的切换，无I-UPF变化
[]images/%E5%9F%BA%E4%BA%8EN2%E6%8E%A5%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%EF%BC%8C%E6%97%A0I-UPF%E5%8F%98%E5%8C%96(%E9%87%8D%E7%94%A81).png)
 说明： 
若用户面路径中不存在I-UPF，则UPF指UPF（PSA）。 
若用户面路径中存在I-UPF，则UPF指I-UPF。 
若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。 
流程说明如下： 
Source NR检测到用户需要切换到Target NR，发送Handover
Required
消息给Source AMF，携带Handover
Type、Target ID、Source To Target Transparent Container等信息。
Handover Required消息中的关键信元参见[表1](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__0c188efa-d630-451f-bb29-0e9489d0ecc7)。
关键信元|信元解释|示例
---|---|---
Handover Type|表示源侧触发了哪种切换，切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
Cause|指示NGAP协议特定事件的原因。|
Target ID|标识切换的目标，Target ID可以是NG-RAN，也可以是E-UTRAN。|
PDU Session Resource List|PDU会话资源列表。|
PDU Session ID|用于标识UE的一个PDU会话。|
Handover Required Transfer|NG-RAN通过AMF透传给SMF的Handover Required Transfer IE。|
Source to Target Transparent Container|用于通过核心网将无线相关信息从切换源侧透传给切换目标侧。由源侧RAN节点产生，并发送到目标侧RAN节点。|
（可选）Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target
AMF。 
（可选）若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext
 Request消息给Target
AMF，携带SUPI、Handover Type、Target ID以及PDU会话列表、Source To Target Transparent
Container等信息。
Namf_Communication_CreateUEContext消息中的关键信元参见[表2](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__6e70d119-e3eb-4f8e-9db9-f323d56aca79)。
关键信元|信元解释|示例
---|---|---
UeContext|表示要创建的单个UeContext资源，包括SUPI、PEI、groupList等。|
targetId|目标RAN的标识。|
sourceToTargetData|包含Source to Target Transparent Container。Source to Target TransparentContainer用于通过核心网将无线相关信息从切换源侧透传给切换目标侧。由源侧RAN节点产生，并发送到目标侧RAN节点。|
pduSessionList|包含N2SmInformation的列表，其中每个N2SmInformation包含每个PDU会话ID从源RAN接收的HandoverRequired Transfer。|
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带用户位置、Target AMF ID、切换准备状态等信息。
Nsmf_PDUSession_UpdateSMContext消息中的关键信元参见[表3](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__d5f0368a-6191-4105-a3f0-816a72a69d21)。
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
n2SmInfo|如果收到AN发送的N2 SM信息，则该信元应该存在。当出现时，该信元将引用N2 SM信息二进制数据。|
targetId|目标RAN的标识。|
（可选）SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF仍旧为切换前的UPF。 
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target AMF，携带PDU会话ID、SM N2 Information。
Nsmf_PDUSession_UpdateSMContext Response消息中的关键信元参见[表4](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__72a6192c-dd53-4fdb-9a90-abd36ed2067f)。
关键信元|信元解释|示例
---|---|---
n2SmInfo|如果需要向AN发送的N2 SM信息，则该信元必须存在。当出现时，该信元将引用N2 SM信息二进制数据。|
Target AMF下发Handover Request
消息给Target NR，携带Handover
Type、SM N2 Information List、UE AMBR、Security Context、UE Security Capabilities。
Handover Request消息中的关键信元参见[表5](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__ef2e3013-0a26-4fc4-acff-bba9490e4cba)。
关键信元|信元解释|示例
---|---|---
Handover Type|表示源侧触发了哪种切换。切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
Cause|指示NGAP协议特定事件的原因。|
PDU Session Resource Setup List|PDU会话资源建立列表。|
PDU Session ID|用于标识UE的一个PDU会话。|
Handover Request Transfer|SMF通过AMF透传给NG-RAN的Handover Request Transfer IE。|
Target NR回复Handover Request Acknowledge
消息给Target AMF，携带PDU Session Admitted List、Target
To Source Transparent Container等信息，其中PDU Session Admmitted List包含了PDU会话ID、SM
N2 Information等信息。
Handover Request Acknowledge消息中的关键信元参见[表6](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__a482b2ca-9080-4b3e-8e0a-a957e083970b)。
关键信元|信元解释|示例
---|---|---
PDU Session Resource Admitted List|PDU会话资源准入列表。|
PDU Session ID|用于标识UE的一个PDU会话。|
Handover Request Acknowledge Transfer|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge Transfer IE。|
Target to Source Transparent Container|用于通过核心网将无线相关信息从切换目标侧透传给切换源侧。由目标侧RAN节点产生，并发送到源侧RAN节点。|
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、SM N2 Information。
Nsmf_PDUSession_UpdateSMContext Request消息中的关键信元参见[表7](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__4f373255-6b1c-4556-a708-f9b34df6cacf)。
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
n2SmInfo|如果收到AN发送的N2 SM信息，则该信元应该存在。当出现时，该IE将引用N2 SM信息二进制数据。|
Handover Request Acknowledge Transfer|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge Transfer IE。|
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target AMF。
Nsmf_PDUSession_UpdateSMContext Response消息中的关键信元参见[表8](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__c8644e32-527c-431c-b7cd-43f6d59d8b68)。
关键信元|信元解释|示例
---|---|---
n2SmInfo|如果需要向AN发送N2 SM信息，则该信元必须存在。当出现时，该IE将引用N2 SM信息二进制数据。|
Handover Command Transfer|SMF通过AMF透传给NG-RAN的Handover Command Transfer IE。|
（可选）Target AMF发送Namf_Communication_CreateUEContext
 Response消息给Source
AMF，携带Target To Source Transparent Container。
Namf_Communication_CreateUEContext Response消息中的关键信元参见[表9](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__46334dc2-ef56-4711-bd53-8967c23b2c24)。
关键信元|信元解释|示例
---|---|---
UeContex|表示要创建的单个UeContext资源。|
targetToSourceData|包含“Target To Source Transparent Container”。|
pduSessionList|包含N2SmInformation的列表，其中每个N2SmInformation包含每个PDU会话ID从源RAN接收的HandoverRequired Transfer。|
Source AMF发送Handover Command
消息给Source NR，携带Target To Source Transparent Container。Source NR收到Handover Command
消息后，通过空口通知UE向目标小区切换。
Handover Command消息中的关键信元参见[表10](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__b47873b3-0466-47d6-bc56-bdf3cb53a878)。
关键信元|信元解释|示例
---|---|---
Handover Type|表示源侧触发了哪种切换。切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
PDU Session Resource Handover List|PDU会话资源切换列表。|
PDU Session ID|用于标识一个UE的PDU会话。|
Handover Command Transfer|SMF通过AMF透传给NG-RAN的Handover Command Transfer IE。|
Target to Source Transparent Container|用于通过核心网将无线相关信息从切换目标侧透传给切换源侧；由目标侧RAN节点产生，并发送到源侧RAN节点。|
UE切换到Target NR后，Target NR发送Handover
Notify
消息给Target AMF，通知Target AMF用户已经成功切换到目标小区。
（可选）Target AMF收到Handover Notify
消息后，发送Namf_Communication_N2InfoNotify
消息给Source AMF，通知Source
AMF用户已经切换成功。
Handover Notify消息中的关键信元参见[表11](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__29295fec-59cd-409d-8e3a-2a61a49db0f7)。
关键信元|信元解释|示例
---|---|---
User Location Information|用于提供UE的位置信息。|
（可选）Source AMF启动定时器，在定时器释放后，通知Source NR释放资源。Source NR回复Namf_Communication_N2InfoNotify
 Ack消息给Target
AMF。
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、切换完成指示。
Nsmf_PDUSession_UpdateSMContext Request消息中的关键信元参见[表12](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__e6eb5d8e-1d40-4e47-9dd5-5f3b2cc0e292)。
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
SMF发送PFCP Session Modification Request
消息给UPF，携带Target NR的N3隧道信息。
UPF回复PFCP Session Modification Response
消息给SMF。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response给AMF。
步骤15启动的定时器超时后，Source AMF发送UE Context
Release Command
消息给Source NR，通知Source NR释放用户上下文。
Source NR释放用户上下文，回复UE Context Release
Complete
消息给Source AMF。
##### 基于N2接口的切换，重选I-UPF 
基于N2接口的切换，重选I-UPF的流程如[图2](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__bf8fd866-855c-4d83-9cbe-82281d8e6aab)所示。
图2  基于N2接口的切换，重选I-UPF
[]images/%E5%9F%BA%E4%BA%8EN2%E6%8E%A5%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%EF%BC%8C%E9%87%8D%E9%80%89I-UPF(%E9%87%8D%E7%94%A81).png)
 说明： 
若切换前，用户面路径中不存在I-UPF，则Source I-UPF就是UPF（PSA）。 
若Source NR与Target NR归属同一个AMF管理，则Target AMF和Source AMF指同一个AMF。 
流程说明如下： 
Source NR检测到用户需要切换到Target NR，发送Handover
Required
消息给Source AMF，携带Handover Type、Target ID、Source To Target
Transparent Container等信息。Handover Required消息中的关键信元参见[表13](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__c480ad13-e0ce-4854-a816-4eb0a965f6bc)。
关键信元|信元解释|示例
---|---|---
Handover Type|该IE表示源侧触发的是哪种切换。切换类型有如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
Cause|该IE的目的是为了指示NGAP协议特定事件的原因。|
Target ID|该IE标识切换的目标，Target ID可以是NG-RAN，也可以是E-UTRAN。|
PDU Session Resource List|PDU会话资源列表。|
Source to Target Transparent Container|该IE用于通过核心网将无线相关信息从切换源侧透传给切换目标侧。由源侧RAN节点产生，并发送到目标侧RAN节点。|
（可选）Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target
AMF。 
（可选）若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext
 Request消息给Target AMF，携带SUPI、Handover
Type、Target ID以及PDU会话列表、Source To Target Transparent Container等信息。
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带用户位置、Target AMF ID、切换准备状态等信息。
（可选）SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF为Target I-UPF。 
SMF发送PFCP Session Establishment Request
消息给Target I-UPF，通知Target I-UPF创建PDU会话，携带UPF（PSA）的N9隧道信息。
Target I-UPF回复PFCP Session Establishment
Response
消息给SMF，携带Target I-UPF的N3隧道信息。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target AMF，携带PDU会话ID、SM N2 Information。
Target AMF下发Handover Request
消息给Target
NR，携带Handover Type、SM N2 Information List、UE AMBR、Security Context、UE
Security Capabilities。Handover Request消息中的关键信元参见[表14](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__6fd5dc3f-4bb5-4ad6-8f16-d2b581515fa5)。
关键信元|信元解释|示例
---|---|---
Handover Type|该IE表示源侧触发的是哪种切换。切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
Cause|该IE的目的是为了指示NGAP协议特定事件的原因。|
Target NR回复Handover Request Acknowledge
消息给Target AMF，携带PDU Session Admitted List、Target To Source Transparent
Container等信息，其中PDU Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。
Handover Request Acknowledge消息中的关键信元参见[表15](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__a5d7b859-206e-4fc0-a155-9f02fddb31fd)。
关键信元|信元解释|示例
---|---|---
Handover Request Acknowledge Transfer|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge Transfer IE。|
Target to Source Transparent Container|该IE用于通过核心网将无线相关信息从切换目标侧透传给切换源侧。由目标侧RAN节点产生，并发送到源侧RAN节点。|
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、SM N2 Information。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target AMF。
（可选）Target AMF发送Namf_Communication_CreateUEContext
 Response消息给Source AMF，携带Target To Source Transparent Container。
Source AMF发送Handover Command
消息给Source
NR，携带Target To Source Transparent Container；Source NR收到Handover Command
消息后，通过空口通知UE向目标小区切换。
UE切换到Target NR后，Target NR发送Handover
Notify
消息，通知Target AMF用户已经成功切换到目标小区。
（可选）Target AMF收到Handover Notify
消息后，发送Namf_Communication_N2InfoNotify
消息给Source AMF，通知Source AMF用户已经切换成功。
（可选）Source AMF启动定时器，在定时器释放后，通知Source NR释放资源，回复Namf_Communication_N2InfoNotify
 Ack消息给Target
AMF。
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、切换完成指示。
SMF发送PFCP Session Modification Request
消息给UPF，携带Target NR的N3隧道信息。
UPF回复PFCP Session Modification Response
消息给SMF。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response响应消息给Target AMF。若切换前用户面路径中存在I-UPF，则启动定时器。
如果步骤17启动的定时器超时后，Source AMF发送UE Context
Release Command
消息给Source NR，通知Source NR释放用户上下文。
Source NR释放用户上下文，回复UE Context Release
Complete
消息给Source AMF。
（可选）如果步骤21启动的定时器超时，SMF发送PFCP Session Release Request消息给Source
I-UPF，通知Source I-UPF释放PDU会话。 
（可选）Source I-UPF回复PFCP Session Release Response消息给SMF。 
##### 基于N2接口的切换，移除I-UPF 
基于N2接口的切换，移除I-UPF的流程如[图3](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__3a8f34c5-18fd-4242-96a8-9a764246ecfb)所示。
图3  基于N2接口的切换，移除I-UPF
[]images/%E5%9F%BA%E4%BA%8EN2%E6%8E%A5%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%EF%BC%8C%E7%A7%BB%E5%87%BAI-UPF(%E9%87%8D%E7%94%A81).png)
 说明： 
若Source NR与Target NR归属同一个AMF管理，则Target
AMF和Source AMF指同一个AMF。 
流程说明如下： 
Source NR检测到用户需要切换到Target NR，发送Handover
Required
消息给Source AMF，携带Handover Type、Target ID、Source To Target
Transparent Container等信息。
Handover Required
消息中的关键信元参见[表16](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__92cb9bf4-f814-46a7-8ed0-1e15c50aff58)。
关键信元|信元解释|示例
---|---|---
Handover Type|表示源侧触发了哪种切换，切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
Cause|指示NGAP协议特定事件的原因。|
Target ID|标识切换的目标，Target ID可以是NG-RAN，也可以是E-UTRAN。|
PDU Session Resource List|PDU会话资源列表。|
PDU Session ID|用于标识UE的一个PDU会话。|
Handover Required Transfer|NG-RAN通过AMF透传给SMF的Handover Required Transfer IE。|
Source to Target Transparent Container|用于通过核心网将无线相关信息从切换源侧透传给切换目标侧。由源侧RAN节点产生，并发送到目标侧RAN节点。|
（可选）Source AMF检测到Target NR不归属自身管理，则调用AMF选择功能，选择管理Target NR的Target
AMF。 
（可选）若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_CreateUEContext
 Request消息给Target AMF，携带SUPI、Handover
Type、Target ID以及PDU会话列表、Source To Target Transparent Container等信息。
Namf_Communication_CreateUEContext
 Request消息中的关键信元参见[表17](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__ea867272-d49f-4c7f-87c9-cb2354db0cc1)。
关键信元|信元解释|示例
---|---|---
UeContext|表示要创建的单个UeContext资源，包括SUPI、PEI、groupList等。|
targetId|目标RAN的标识。|
sourceToTargetData|包含Source to Target Transparent Container。Source to Target TransparentContainer用于通过核心网将无线相关信息从切换源侧透传给切换目标侧。由源侧RAN节点产生，并发送到目标侧RAN节点。|
pduSessionList|包含N2SmInformation的列表，其中每个N2SmInformation包含每个PDU会话ID从源RAN接收的HandoverRequired Transfer。|
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带用户位置、Target AMF ID、切换准备状态等信息。
Nsmf_PDUSession_UpdateSMContext消息中的关键信元参见[表18](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__9780a524-37bf-4561-87de-a89a4f35c30b)。
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
n2SmInfo|如果收到AN发送的N2 SM信息，则该信元应该存在。当出现时，该信元将引用N2 SM信息二进制数据。|
targetId|目标RAN的标识。|
（可选）SMF若检测到用户位置发生变化，则调用UPF选择功能重新选择UPF，本场景中选择的UPF为UPF（PSA）。 
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target AMF，携带SM N2 Information。
Nsmf_PDUSession_UpdateSMContext Response消息中的关键信元参见[表19](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__887e13e6-58ba-4627-a837-699c18860cc7)。
关键信元|信元解释|示例
---|---|---
n2SmInfo|如果需要向AN发送的N2 SM信息，则该信元必须存在。当出现时，该信元将引用N2 SM信息二进制数据。|
Target AMF下发Handover Request
消息给Target
NR，携带Handover Type、SM N2 Information List、UE AMBR、Security Context、UE
Security Capabilities。
Handover Request消息中的关键信元参见[表20](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__48330ff0-f575-4b0f-8cf3-bb2d75ac2d16)。
关键信元|信元解释|示例
---|---|---
Handover Type|表示源侧触发了哪种切换。切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
Cause|指示NGAP协议特定事件的原因。|
PDU Session Resource Setup List|PDU会话资源建立列表。|
PDU Session ID|用于标识UE的一个PDU会话。|
Handover Request Transfer|SMF通过AMF透传给NG-RAN的Handover Request Transfer IE。|
Target NR回复Handover Request Acknowledge
消息给Target AMF，携带PDU Session Admitted List、Target To Source Transparent
Container等信息，其中PDU Session Admmitted List包含了PDU会话ID、SM N2 Information等信息。
Handover Request Acknowledge消息中的关键信元参见[表21](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__701a1f7e-1974-4dff-a15a-8dacbf887047)。
关键信元|信元解释|示例
---|---|---
PDU Session Resource Admitted List|PDU会话资源准入列表。|
PDU Session ID|用于标识UE的一个PDU会话。|
Handover Request Acknowledge Transfer|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge Transfer IE。|
Target to Source Transparent Container|用于通过核心网将无线相关信息从切换目标侧透传给切换源侧。由目标侧RAN节点产生，并发送到源侧RAN节点。|
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、SM N2 Information。
Nsmf_PDUSession_UpdateSMContext Request消息中的关键信元参见[表22](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__c0ef16f1-581a-4a5f-9c45-474ea6e87d9d)。
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
n2SmInfo|如果收到AN发送的N2 SM信息，则该信元应该存在。当出现时，该IE将引用N2 SM信息二进制数据。|
Handover Request Acknowledge Transfer|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge Transfer IE。|
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target AMF。
Nsmf_PDUSession_UpdateSMContext Response消息中的关键信元参见[表23](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__1c8514cc-7d67-4331-90f9-a620e0beaee6)。
关键信元|信元解释|示例
---|---|---
n2SmInfo|如果需要向AN发送N2 SM信息，则该信元必须存在。当出现时，该IE将引用N2 SM信息二进制数据。|
Handover Command Transfer|SMF通过AMF透传给NG-RAN的Handover Command Transfer IE。|
（可选）Target AMF发送Namf_Communication_CreateUEContext
 Response消息给Source AMF，携带Target To Source Transparent Container。
Namf_Communication_CreateUEContext Response消息中的关键信元参见[表24](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__692db443-d584-4d20-a1c0-b42fa2e405d3)。
关键信元|信元解释|示例
---|---|---
UeContex|表示要创建的单个UeContext资源。|
targetToSourceData|包含“Target To Source Transparent Container”。|
pduSessionList|包含N2SmInformation的列表，其中每个N2SmInformation包含每个PDU会话ID从源RAN接收的HandoverRequired Transfer。|
Source AMF发送Handover Command
消息给Source
NR，携带Target To Source Transparent Container。Source NR收到Handover Command
消息后，通过空口通知UE向目标小区切换。
Handover Command消息中的关键信元参见[表25](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__7902922e-9129-4ada-b766-f7b7c3f5f569)。
关键信元|信元解释|示例
---|---|---
Handover Type|表示源侧触发了哪种切换。切换类型包括如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node|
PDU Session Resource Handover List|PDU会话资源切换列表。|
PDU Session ID|用于标识一个UE的PDU会话。|
Handover Command Transfer|SMF通过AMF透传给NG-RAN的Handover Command Transfer IE。|
Target to Source Transparent Container|用于通过核心网将无线相关信息从切换目标侧透传给切换源侧。由目标侧RAN节点产生，并发送到源侧RAN节点。|
UE切换到Target NR后，Target NR发送Handover
Notify
消息，通知Target AMF用户已经成功切换到目标小区。
（可选）Target AMF收到Handover Notify
消息后，发送Namf_Communication_N2InfoNotify
消息给Source AMF，通知Source AMF用户已经切换成功。
Handover Notify消息中的关键信元参见[表26](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__08753752-5a70-4531-9f52-dc38737bb4ba)。
关键信元|信元解释|示例
---|---|---
User Location Information|用于提供UE的位置信息。|
（可选）Source AMF启动定时器，在定时器释放后，通知Source NR释放资源，回复Namf_Communication_N2InfoNotify
 Ack消息给Target
AMF。
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、切换完成指示。
Nsmf_PDUSession_UpdateSMContext Request消息中的关键信元参见[表27](1601430399446%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#zfc4911990b6b489e9db27da8e64f29b5__efb8e7f7-9bcd-4410-9db3-30511a94996d)。
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
SMF发送PFCP Session Modification Request
消息给UPF，携带Target NR的N3隧道信息。
UPF回复PFCP Session Modification Response
消息给SMF。
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response响应消息给Target AMF。启动定时器，带定时释放后通知I-UPF释放资源。
如果步骤15启动的定时器超时，Source AMF发送UE Context
Release Command
消息给Source NR，通知Source NR释放用户上下文。
Source NR释放用户上下文，回复UE Context Release
Complete
消息给Source AMF。
（可选）如果步骤19启动的定时器超时，SMF发送PFCP Session Release Request消息给Source
I-UPF，通知Source I-UPF释放PDU会话。 
（可选）Source I-UPF回复PFCP Session Release Response消息给SMF。 
#### 基于N2接口的切换取消 
基于N2接口的切换取消流程如[图1](1601430090231%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#ze48cfd8f3dd4434fa7d1d9dc602ee12e__6c4253e0-1aa8-4aba-84f3-58d23f67dc55)所示。
图1  基于N2接口的切换取消
[]images/%E5%9F%BA%E4%BA%8EN2%E6%8E%A5%E5%8F%A3%E7%9A%84%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88(%E9%87%8D%E7%94%A81).png)
 说明： 
若Source NR与Target NR归属同一个AMF管理，则Target
AMF和Source AMF指同一个AMF。 
流程说明如下： 
在N2切换过程中，Source NR检测到需要取消切换，发送Handover Cancel
消息给Source
AMF，携带切换取消原因。Handover Cancel消息中的关键信元参见[表1](1601430090231%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#ze48cfd8f3dd4434fa7d1d9dc602ee12e__e9d288cf-7a82-4852-8f34-a8645f248233)。
关键信元|信元解释|示例
---|---|---
Cause|指示NGAP协议特定事件的原因。|
（可选）若Target NR归属Target AMF管理，则Source AMF发送Namf_Communication_ReleaseUEContext
 Request消息给Target AMF，通知Target AMF终止切换。Namf_Communication_ReleaseUEContext消息中的关键信元参见[表2](1601430090231%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#ze48cfd8f3dd4434fa7d1d9dc602ee12e__490a073c-8c2e-411f-9f88-f28d38de14a1)。
关键信元|信元解释|示例
---|---|---
ngapCause|表示从RAN接收的NGAP原因。|
（可选）若Target AMF已经下发Handover Request
消息给Target NR，则发送UE Context Release Command
消息给Target NR，通知Target NR释放用户上下文。
（可选）Target NR回复UE Context Release Complete
消息给Target
AMF。
Target AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给SMF，携带PDU会话ID、切换取消指示。Nsmf_PDUSession_UpdateSMContext Request消息中的关键信元参见[表3](1601430090231%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#ze48cfd8f3dd4434fa7d1d9dc602ee12e__3552d3d0-c0ef-4536-bd68-06cc737ba27c)，
关键信元|信元解释|示例
---|---|---
hoState|用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换。PREPARING：正在为PDU会话做切换准备。SMF正在准备目标5G和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID。PREPARED：PDU会话切换已经准备完成。目标5G和UPF之间的N3隧道更新SMF，目标5G为切换执行时下行流量分配的F-TEID。COMPLETED：切换完成（成功）。CANCELLED：表示切换取消。|
（可选）若已经重选了新的I-UPF，则发送PFCP Session Release Request消息给新选择的Target
I-UPF。 
（可选）Target I-UPF回复PFCP Session Release Response消息给SMF。 
SMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息给Target
AMF。
（可选）Target AMF回复Namf_Communication_ReleaseUEContext
 Response消息给Source AMF。
Source AMF回复Handover Cancel Acknowledge
消息给Source NR。
### 4/5G互操作 
#### 背景 
从协议的演进历史以及实际应用来看，5G网络的覆盖将会是一个由点到面的过程。在5G网络全面覆盖之前，4G网络都是5G网络的良好补充，5G与4G并存将是一个长期的过程。    
在5G网络建设初期，网络覆盖不全面，当用户移动到没有5G网络的地方，就需要切换到4G网络来实现业务需求，因此网络侧和终端侧都必须支持用户在4/5G网络之间切换的业务连续性。在现阶段，用户的语音业务仍需要4G网络来提供服务，确保通话的稳定性与可靠性；数据业务已经可以使用5G网络来提供服务，提高系统容量和传输速率。 
5G用户将会在4/5G网络中移动和切换，移动过程中的业务连续性将直接影响用户的体验，尤其是语音类业务。4/5G互操作就是为了保证业务连续性，优化用户体验。因此，4/5G互操作是运营商必须具备的能力。 
考虑到5G网络的建网周期、成本等原因，有两种组网方式供运营商灵活选择。有些运营商选择初期采用NSA（非独立组网）方式，后期逐渐向SA（独立组网）方式演进，有些则直接建设SA网络。
NSA组网：利用4G现网，成本低、周期短，但是4/5G互操作主要发生在4/5G基站之间，操作复杂。 
SA组网：需要新建5G核心网，成本高、周期长，但是支持eMBB（增强型移动宽带）、uRLLC（超可靠低时延通信）和mMTC（大规模机器通信）等网络切片以及MEC（移动边缘计算），这是5G网络的核心价值。在该组网架构下，4/5G互操作主要发生在4/5G核心网之间。 
用户在5G SA和4G EPS系统之间移动，相关的流程统称为4/5G互操作。包括4/5G用户接入EPC、4/5G用户接入5GC、基于N26接口的跨系统移动和无N26接口的跨系统移动。其中基于N26接口的跨系统移动包括了空闲态和连接态下，4/5G跨系统的注册更新、切换、TAU、切换取消等流程。 
系统架构 :3GPP定义的4/5G互操作的系统架构如[图1](7.html#T_1554257199539__ba784754-237e-4108-b270-daa1efca9b92)所示。
图1  4/5G互操作系统架构
[]images/1604478095511.png)
4/5G互操作涉及4G和5G网络中的多个网元或NF。为了支持4/5G互操作，保证用户的业务连续性，3GPP定义了4个融合网元，包括：HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U，网元功能参见[表1](7.html#T_1554257199539__b4220265-b351-4254-86c5-6fe618b92f40)。
网元/NF名称|功能
---|---
AMF|EBI管理，包括分配、回收等。支持DNS NAPTR查询 。支持节点选择，包括MME选择、SMF+PGW-C选择。支持N26接口。支持将5G MM上下文转化为4G MM上下文。支持无N26接口下，从4G移动到5G时，通知UDM+HSS用户已经在MME注册。SMC（Security Mode Control，安全模式控制）过程中选择EPS NAS算法。支持N11接口已有信令适配4/5G互操作的改造。
MME|支持节点选择，包括AMF选择、SMF+PGW-C选择。支持N26接口。支持无N26接口下，从5G移动到4G时，携带单注册指示给HSS+UDM。支持无PDN连接的附着。
SMF+PGW-C|支持PDU会话或者QoS Flow释放时，通知AMF回收EBI。支持切换过程中将数据前转所使用的EPS承载映射为QoS Flow。支持PGW-U+UPF合一节点选择，支持PCF+PCRF合一节点选择，支持将PGW FQDN注册到UDM。支持PDU会话激活时，向AMF请求分配EBI，并通知NR和UE。支持PDU会话激活时，分配映射的QoS，并通知UE。支持在承载激活时，把5G QoS、S-NSSAI携带给UE。维护5G会话标识（PDU会话ID）与PDN连接的关联关系，4G承载标识与QoS Flow的关联关系。
HSS+UDM|管理用户4G和5G签约数据。支持用户同时在MME和AMF注册。支持存储PGW FQDN，并随着签约数据一起下发给AMF和MME。
UPF+PGW-U|维护QFI与EPC数据前转通道的关联关系。支持从QoS Flow到EPC承载的转换。
PCF+PCRF|通过N7接口为4/5G用户下发4G和5G控制策略。
#### 4/5G用户接入EPC 
4/5G用户接入EPC的流程如[图1](1601433782320.html#z5fbcebb0933c4747a57966ad052bcb1c__f72be21d-e840-4f1b-8b5d-bd06bbe95e8b)所示。
图1  4/5G用户接入EPC
[]images/%E7%94%A8%E6%88%B7%E6%8E%A5%E5%85%A5EPC.png)
 说明： 
此处仅描述4/5G互操作引入的变化部分，对于EPC通用业务交互，不再赘述。 
流程说明如下： 
UE发起会话建立请求，在PCO中携带PDU Session ID。 
MME判断出是4/5G用户，则选择合一部署的SMF+PGW-C。 
SMF+PGW-C接收到Create Session Request消息，保留PDU Session ID，判断出是4/5G用户。 
SMF+PGW-C选择PCF，向其发送Npcf_SMPolicyControl_Create
 Request请求会话策略。
PCF通过Npcf_SMPolicyControl_Create
 Response消息向SMF+PGW-C下发会话策略信息。
SMF+PGW-C收到会话策略后，进行承载绑定，并选择合一部署的UPF+PGW-U。若支持with N26互操作，则生成5G QoS Rules。 
SMF+PGW-C通知UPF+PGW-U建立N4会话，仅仅下发EPC的数据处理策略及隧道资源，使用信令为PFCP Session Establishment Request
和PFCP Session Establishment Response
。
SMF+PGW-C向MME响应Create Session Response消息，其中，PCO中携带S_NSSAI；若支持with N26互操作，PCO还需携带5G QoS Rules。 
MME接收到Create Session Response消息，构造NAS信令响应UE的会话建立请求，并将来自SMF+PGW-C的PCO透传给UE。 
#### 4/5G用户接入5GC 
4/5G用户接入5GC的流程如[图1](1601433828549.html#zb1ee5d9cb92f4b54a0cf3dbf304c67f6__dc584bee-0b3a-4e09-b90f-372e2ef3f377)所示。
图1  4/5G用户接入5GC
[]images/%E7%94%A8%E6%88%B7%E6%8E%A5%E5%85%A55GC.png)
 说明： 
此处仅描述4/5G互操作引入的变化部分，对于5GC通用业务交互，不再赘述。 
流程说明如下： 
UE发起PDU Session建立请求。 
AMF判断出是4/5G用户，则选择合一部署的SMF+PGW-C。 
SMF+PGW-C接收到Nsmf_PDUSession_CreateSMContext
 Request消息，判断是4/5G用户。
SMF+PGW-C选择PCF，并且请求会话策略，使用信令为Npcf_SMPolicyControl_Create
 Request。
SMF+PGW-C向AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应消息。
PCF向SMF+PGW-C下发会话策略信息，使用信令为Npcf_SMPolicyControl_Create
 Respongse。
SMF+PGW-C收到会话策略后，进行QoSFlow绑定，并选择合一部署的UPF+PGW-U。若支持N26互操作，生成Mapped 4G QoS及TFT。 
SMF+PGW-C通知UPF+PGW-U建立N4会话，下发5G的数据处理策略及隧道资源，使用信令为PFCP Session Establishment Request
和PFCP Session Establishment Response
。
SMF+PGW-C支持N26互操作，则向AMF发送Namf_Communication_EBIAssignment
请求消息请求分配EBI，携带PDU Session ID、 ARPList等信息，其中ARPList是已经绑定成功QoSFlow所使用的ARPs。
（可选）当EBI不足时，AMF根据S_NSSAI和ARP的优先级进行抢占，若抢占成功，AMF通过Nsmf_PDUSession_UpdateSMContext
消息通知正在占用的SMF+PGW-C进行EBI释放。
AMF向SMF+PGW-C发送Namf_Communication_EBIAssignment
响应消息，携带分配的EBIs。
SMF+PGW-C发送Namf_Communication_N1N2MessageTransfer
消息，通知AMF进行N1N2接口信息的转发。其中，N1 Contaniner 5G QoS Rules中携带mapped 4G QoS、TFT、EBI，N2 Contaniner QoS Profile中携带EBI。
AMF收到Namf_Communication_N1N2MessageTransfer
消息后，构造N2 Session Request消息，携带N2 info（QoS Profile.EBI）及NAS信令PDU SESSION ESTABLISH ACCEPT（QoS Rules&mapped 4G QoS、TFT 、EBI）。
RAN保存QoS Profile中的EBI信息，以便UE向4G切换时使用；同时，构造AN消息，向UE转发NAS信令。UE接收并保存4G相关参数，以便向4G切换时使用。 
RAN向AMF返回N2 Session Response响应消息。 
#### 基于N26接口的跨系统移动 
本节包括以下流程： 
空闲态下基于N26接口，4G跨系统移动到5G进行注册更新 
连接态下基于N26接口，4G跨系统移动到5G进行切换 
连接态下基于N26接口，4G跨系统移动到5G，切换取消 
空闲态下基于N26接口，5G跨系统移动到4G进行TAU切换 
连接态下基于N26接口，5G跨系统移动到4G进行切换 
连接态下基于N26接口，5G跨系统移动到4G，切换取消 
##### 空闲态下基于N26接口，4G跨系统移动到5G进行注册更新 
空闲态下基于N26接口4G到5G注册更新流程如[图1](1601433938753.html#z8af3de5b3bc24b5790dcdd9a148f66d4__db5028b5-1314-4e67-a7c5-ec604a23659e)所示。
图1  空闲态下基于N26接口4G到5G注册更新
[]images/%E7%A9%BA%E9%97%B2%E6%80%814G%E5%88%B05G%E6%B3%A8%E5%86%8C%E6%9B%B4%E6%96%B0.png)
流程说明如下： 
UE检测需要发起注册流程（比如从4G覆盖区域进入5G覆盖区域），则发起Registration Request
给AMF，携带由4G的GUTI映射为5G的GUTI、UE从EPC移入指示（UE Status）、请求的NSSAI（包含全部PDN连接的S-NSSAI）、PDU会话ID列表（包含全部PDN连接的PDU会话ID）、TAU请求（经过4G安全上下文校验处理）、注册类型（Mobility Registration
Updating）。
AMF根据注册类型为“Mobility Registration Updating”以及EPC移入指示（UE Status），判断源局为MME，则将映射的5G-GUTI还原为4G
Native GUTI，并根据其中的GUMMEI信息构造MME FQDN，通过本地EPC地址解析或者DNS查询得到MME地址。
AMF发送Context Request
给源MME，携带4G-GUTI、TAU请求。
MME对TAU Request进行完整性校验，校验通过后回复Context Response
，携带Cause、IMSI、4G
MM上下文以及EPS PDN连接信息，不携带未使用的EPS鉴权向量。MME判断PDN连接对应的网关为SMF+PGW-C时，则判定该PDN连接需要切换到5GS，Context Response需要包含该PDN连接，否则如果网关为standalone
PGW-C（即仅支持4G），则无需迁移该PDN连接到5GC，Context Response中不应该包含该PDN连接。
（可选）AMF存储MME携带过来的信息，将4G安全上下文转化为5G安全上下文。根据本地策略或者Context Response中的Cause值，若决策需要触发认证过程，则发起认证和SMC过程，其中包括向AUSF请求鉴权向量。AMF将4G安全上下文中的加密和完保算法保存到映射的5G安全上下文中。
AMF回复Context Acknowledge
给MME，携带SGW改变指示。
（可选）若需要进行IMEI Check，则发起IMEI检测过程，包括向UE请求IMEI以及向5G-EIR进行IMEI Check的过程。
AMF调用UDM选择过程，选择UDM。然后向HSS+UDM注册、订阅并请求用户签约数据，注册消息中携带drFlag标记，value为false。 
AMF调用PCF选择功能，选择PCF。 
AMF发送Npcf_AMPolicyControl_Create
 Request给新选择的PCF，携带SUPI、RAT Type、PLMN、用户位置等信息。
PCF返回Npcf_AMPolicyControl_Create
 Response给AMF。
AMF根据MME携带过来的PGW FQDN，通过NRF查询PGW FQDN对应SMF+PGW-C的服务化地址。 
AMF针对每个PDN连接，发送Nsmf_PDUSession_CreateSMContext
 Request给SMF+PGW-C，携带EPS
PDN连接信息、AMF ID、pduSessionsActivateList等信息。
（可选）SMF+PGW-C解码处理Nsmf_PDUSession_CreateSMContext
 Request，保存接入信息。若PCF订阅的信息发生变化，则向PCF发送Npcf_SMPolicyControl_Update
Request消息。
（可选）PCF根据当前的用户接入参数，授权策略控制参数，向SMF+PGW-C响应Npcf_SMPolicyControl_Update

Response消息。SMF+PGW-C更新会话/QoS Flow控制参数。
SMF+PGW-C向AMF响应Nsmf_PDUSession_CreateSMContext
 Response消息。
HSS+UDM下发Cancel Location Request给MME，通知MME注销用户。在本步骤启动资源保护定时器。 
AMF下发Registration Accept
，携带服务区域、Allowed NSSAI、分配的5G-GUTI等信息。
UE回复Registration Complete
，注册完成。
（可选）当资源保护定时器超时后，MME对于步骤4未迁移到5GC的PDN连接，发送Delete Session Request给SGW，携带OI（Operation
Indication）标记，通知SGW释放用户信息，本地删除承载信息。 
##### 连接态下基于N26接口，4G跨系统移动到5G进行切换 
连接态下基于N26接口4G跨系统移动到5G流程如[图2](1601433938753.html#z8af3de5b3bc24b5790dcdd9a148f66d4__abf5f3e4-5bc8-49b5-b687-8c9fc685555c)所示。
图2  连接态下基于N26接口4G跨系统移动到5G
[]images/%E8%BF%9E%E6%8E%A5%E6%80%814G%E5%88%B05G%E5%88%87%E6%8D%A2.png)
流程说明如下： 
Source eNodeB检测到UE需要切换到目标NR，则发送Handover Required给Source MME，携带Handover
Type、Target ID、Source to Target Container。 
Source MME收到Handover Required消息后，根据消息中的Handover Type以及Target
ID中的TAI，构造5GS TAI FQDN，用于查询目标AMF地址。若UE为专网用户，则根据TAI和签约的UE
Usage Type查询AMF地址。
MME发送Forward Relocation Request
消息给该AMF，携带S1AP Cause、IMSI、4G MM上下文、EPS PDN连接、UE Usage Type、Source To
Target Container。MME侧未使用的EPS鉴权向量，禁止传递给AMF。MME判断PDN连接对应的网关为SMF+PGW-C时，则判定该PDN连接需要切换到5GS，Forward Relocation Request需要包含该PDN连接，否则如果网关为standalone
PGW-C，则无需迁移该PDN连接到5GC，Forward Relocation
Request中不应该包含该PDN连接。
AMF存储MME携带过来信息，将4G安全上下文转化为5G安全上下文，并将4G安全上下文的加密和完保算法，保存到映射的5G安全上下文中。如果MME没有携带UE
5G安全能力，则默认UE支持完整性保护算法（1\2）和加密算法（0\1\2）。AMF根据MME携带过来的PGW FQDN，通过NRF查询PGW
FQDN对应SMF+PGW-C的服务化地址。 
AMF针对每个PDN连接，发送Nsmf_PDUSession_CreateSMContext
 Request给SMF+PGW-C，携带EPS
PDN连接、AMF ID以及切换准备指示。
（可选）SMF+PGW-C解码处理Nsmf_PDUSession_CreateSMContext
 Request消息，根据切换指示判断用户当前正处于切换准备阶段，保存用户接入信息。若部署了PCC，且PCF订阅的接入信息发生了变化，SMF+PGW-C向PCF发起策略更新请求，请求消息为Npcf_SMPolicyControl_Update
 Request。
（可选）PCF返回策略更新响应Npcf_SMPolicyControl_Update
Response。
SMF+PGW-C向AMF响应Nsmf_PDUSession_CreateSMContext
 Response，携带包括PDU Session ID、S_NSSAI、n2SmContainer(PDU
Session ID, S-NSSAI, QFI(s), QoS Profile(s),
EPS Bearer Setup List）信息。
AMF下发Handover Request
给目标NR，携带Cause、UE安全能力、NCC（Next Hop Chaining
Counter）和NH（Next-Hop）、N2 SM信息、Source to Target Container以及4G to 5G
NAS Container。其中，4G to 5G NAS Container包含AMF选择的5G NAS安全算法、Replayed
UE安全能力等信息。
目标NR回复Handover Request Acknowledge
，携带Target to Source Container、N2
SM信息，其中包括每个PDU会话分配的TEID地址，以及已接受的转发的QoS流列表。
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request给SMF+PGW-C，携带N2
SM信息。
SMF+PGW-C存储新的N3隧道信息，向AMF响应应答消息。 
AMF回复Forward Relocation Response
给MME，携带Cause、EPS Bearer Setup
List、Target to Source Container、SGW改变指示以及AMF控制面隧道信息。
MME下发Handover Command给Source eNodeB，携带Target to Source Container，UE开始切换到目标NR。 
UE切换到目标NR小区后，目标NR发送Handover Notify
给AMF。
AMF发送Forward Relocation Complete Notification
给Source MME，通知后者UE已经切换到目标AMF。
Source MME启动资源保护定时器，并回复Forward Relocation Complete Acknowledge
给AMF。
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request给SMF+PGW-C，携带切换完成指示。
（可选）SMF+PGW-C解码Nsmf_PDUSession_UpdateSMContext Request消息，若PCF订阅的接入参数发生了变化，则向PCF请求策略更新，请求消息为Npcf_SMPolicyControl_Update
 Request。
（可选）PCF将策略发送给SMF+PGW-C。 
SMF+PGW-C判断切换已经完成，则向UPF发送N4 Session Modification Request，携带N3隧道地址和TEID。UPF切换数据前，向源NR发送Endmarker。
UPF响应SMF+PGW-CNpcf_SMPolicyControl_Update
Response。
SMF+PGW-C构造Nsmf_PDUSession_UpdateSMContext
 Response消息响应AMF。
（可选）资源保护定时器超时后，MME对于步骤3未迁移到5GC的PDN连接，发送Delete Session Request给SGW，携带OI标记，然后通知Source
eNodeB以及SGW，删除用户信息，本地删除承载信息。 
##### 连接态下基于N26接口，4G跨系统移动到5G，切换取消 
连接态下基于N26接口4G到5G切换取消流程如[图3](1601433938753.html#z8af3de5b3bc24b5790dcdd9a148f66d4__effa8d39-922b-4bc8-ba9c-bd3e0bc1cb3a)所示。
图3  连接态下基于N26接口4G到5G切换取消
[]images/%E8%BF%9E%E6%8E%A5%E6%80%814G%E5%88%B05G%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88.png)
流程说明如下： 
切换准备阶段，源eNodeB由于某些原因，比如UE重新选择源eNodeB下的小区，发送Handover Cancel给MME，取消切换。 
MME发送Relocation Cancel Request
给AMF。
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request给SMF+PGW-C，携带切换取消指示。
（可选）SMF+PGW-C删除已经保存的目标RAN的N3隧道信息。若已经建立了非直传隧道，则SMF构造PFCP Session
Modification Request
消息，通知UPF释放非直传相关资源。
（可选）UPF构造PFCP Session Modification Response
消息响应SMF+PGW-C。
SMF+PGW-C构造Nsmf_PDUSession_UpdateSMContext
 Response消息响应AMF。
（可选）若AMF已通知目标NR创建PDU会话，则下发UE Context Release Command
，通知目标RAN释放无线侧UE上下文，不等待响应。
AMF回复Relocation Cancel Response
。
（可选）若创建了非直传隧道，则MME发送Delete Indirect Data Forwarding Tunnel
Request给SGW。 
（可选）SGW回复Delete Indirect Data Forwarding Tunnel Response。 
MME回复Handover Cancel Acknowledge。 
##### 空闲态下基于N26接口，5G跨系统移动到4G进行TAU切换 
空闲态下基于N26接口5G跨系统移动到4G进行TAU切换的流程如[图4](1601433938753.html#z8af3de5b3bc24b5790dcdd9a148f66d4__d532e0a5-7771-44b5-af6b-bb6f2c302e16)所示。
图4  空闲态下基于N26接口5G跨系统移动到4G进行TAU切换
[]images/1601434302889.png)
流程说明如下： 
UE检测到需要切换到4G，比如进入4G网络覆盖的小区，则Source eNodeB发送TAU Request消息给Target
MME，携带5G-GUTI映射的GUTI以及UE从5GC移入指示。 
Target MME根据映射GUTI查询源AMF地址。 
Target MME发送Context Request
给Source AMF，携带映射的GUTI、Complete TAU
Request。
Source AMF使用当前5G安全上下文校验TAU Request，校验成功后，针对每个已经分配了EBI的PDU会话，发送Nsmf_PDUSession_RetrieveSMContext

Request（携带PDU会话ID、MME Capacity）给SMF+PGW-C，获取PDU会话上下文映射的EPS承载上下文。
（可选）如果UPF+PGW-U分配了CN隧道信息，则SMF+PGW-C向UPF+PGW-U发送PFCP Session
Modification Request
请求消息，请求建立每个EPS承载的隧道。
（可选）UPF+PGW-U为SMF+PGW-C提供每个EPS承载的PGW-U隧道信息。 
SMF+PGW-C向AMF响应 Nsmf_PDUSession_RetrieveSMContext
 Response消息，携带映射的EPS承载上下文（包括与PDU会话对应的PDN连接的PGW-C控制平面隧道信息，每个EPS承载的EBI，每个EPS承载的PGW-U隧道信息以及每个EPS承载的EPS
QoS参数）。
AMF返回Context Response
，携带映射的5G安全上下文、UE安全能力、DRX、EPS PDN连接、UE
Usage Type等信息，不携带SGW Name以及SGW控制面F-TEID。
（可选）MME根据本地策略（比如本地配置强制鉴权），或者Context Response的原因值（用户完整性认证失败），决策是否发起鉴权流程，包括向HSS请求鉴权向量。 
MME回复Context Acknowledge
给Source AMF，携带SGW改变指示。
MME根据TAI以及UE Usage Type（若UE为4G专网用户）选择SGW。 
针对每一个Source AMF发送过来的EPS PDN连接，MME发送Create Session Request给SGW。 
SGW分配U面的S1-U和S5/S8-U隧道资源，并向SMF+PGW-C发送Modify Bearer Request消息。 
（可选）若SGW采用CUPS架构，则Create Session Request消息由SGW-C处理，SGW-C向SGW-U发送Sxa会话建立消息，进行UP资源分配。
（可选）SMF+PGW-C保存接入信息。若PCF订阅的信息发生变化，则向PCF发送Npcf_SMPolicyControl_Update

Request消息。
（可选）PCF根据当前的用户接入参数，授权策略控制参数，向SMF+PGW-C响应Npcf_SMPolicyControl_Update

Response消息。
SMF+PGW-C更新会话/承载参数，通知UPF+PGW-U更新PFCP会话，消息PFCP Session Modification Request
中包括被更新的策略控制参数及S5/S8-U隧道信息。
UPF+PGW-U回复SMF+PGW-C会话修改响应PFCP Session Modification Response
。
SMF+PGW-C向SGW响应Modify Bearer Response消息。 
SGW回复Create Session Response给MME。 
MME发送Location Update Request给HSS+UDM，请求用户签约数据。位置更新请求消息中，Dual-Registration-5G-Indicator标识为0。 
HSS+UDM发送Nudm_UEContextManagement_DeregistrationNotification
给AMF，注销原因为“5G到4G的移动性”。AMF收到注销通知后，向HSS+UDM取消订阅。对于步骤4存在异常情况，有未迁移的PDU会话，AMF通知SMF释放该PDU会话，携带原因为“REL_DUE_TO_HO”，SMF无需通知UE和RAN释放资源。
HSS+UDM下发Location Update Acknowledge给MME，携带用户签约数据。 
MME下发TAU Accept，通过Downlink NAS Transport或者Initial Context Setup
Request经eNodeB发送给UE。 
UE回复TAU Complete。 
核心网可以发起专有承载建立过程，若部署了PCC，则由PCF+PCRF触发。 
##### 连接态下基于N26接口，5G跨系统移动到4G进行切换 
连接态下基于N26接口5G跨系统移动到4G进行切换的流程如[图5](1601433938753.html#z8af3de5b3bc24b5790dcdd9a148f66d4__2e2f5603-0fc6-49ad-952a-44e9c2cf9bfc)所示。
图5  连接态下基于N26接口5G跨系统移动到4G进行切换
[]images/%E8%BF%9E%E6%8E%A5%E6%80%815G%E5%88%B04G%E5%88%87%E6%8D%A2.png)
流程说明如下： 
Source NR检测到需要切换UE到目标小区，则发送Handover Required
给Source AMF，携带Handover
Type、Target ID、Source To Target Container。
AMF根据Handover Type判断目标RAN为E-UTRAN，则根据目标4G TAI通过DNS或者本地配置，查询MME地址。若用户为4G专网用户，则根据目标4G
TAI以及签约的UE Usage Type，查询MME地址。 
针对每个已分配EBI的PDU会话，AMF发送Nsmf_PDUSession_RetrieveSMContext
 Request，携带PDU会话ID以及MME能力，其中MME能力通过AMF本地配置获取，用以指示目标MME是否支持non-IP
PDN连接。
（可选）如果PGW-U UPF分配了CN隧道信息，则SMF+PGW-C向UPF+PGW-U发送PFCF会话修改请求PFCP Session Modification Request
，为每个EPS承载建立隧道。
（可选）UPF+PGW-U为SMF+PGW-C提供每个EPS承载的PGW-U隧道信息。 
SMF+PGW-C向AMF响应Nsmf_PDUSession_RetrieveSMContext
 Response消息，携带映射的EPS承载上下文（包括与PDU会话对应的PDN连接的PGW-C控制平面隧道信息，每个EPS承载的EBI，每个EPS承载的PGW-U隧道信息以及每个EPS承载的EPS
QoS参数）。
AMF发送Forward Relocation Request
给目标MME，携带映射的5G安全上下文、UE安全能力、DRX、EPS
PDN连接、UE Usage Type、Target ID、S1AP Cause等信息，不携带SGW Name以及SGW控制面F-TEID。
目标MME根据目标TAI以及UE Usage Type（若用户为4G专网用户）构造FQDN，选择新的SGW地址。 
针对每一个PDN连接，目标MME发送Create Session Request，携带SMF+PGW-C地址和TEID、该PDN连接下的EPS
Bearer列表、APN、PAA等，不携带EPS Interworking Indication。 
SGW回复Create Session Response。 
目标MME下发Handover Request给目标eNodeB，携带Source To Target Container、Handover
Type（LTEtoNR）。 
目标eNodeB回复Handover Request Acknowledge，携带Target To Source Container。 
目标MME回复Forward Relocation Response
给AMF，携带Target To Source Container以及切换成功的EPS
Bearer列表。
AMF下发Handover Command
给Source NR，携带Target To Source Container，Source
NR通知UE可以开始切换到目标小区。
UE切换目标小区后，目标eNodeB发送Handover Notify给MME，通知MME UE已经成功切换到目标小区。 
MME发送Forward Relocation Complete Notification
给AMF，通知AMF UE已经切换成功。
AMF回复Forward Relocation Complete Acknowledge
，并启动资源保护定时器。
MME发送Modify Bearer Request给SGW，携带目标eNodeB的用户面地址和用户面TEID。 
SGW发送Modify Bearer Request给SMF+PGW-C，携带SGW控制面地址和TEIDC，以及用户面地址和TEIDU。 
（可选）若SGW是CUPS的，则Modify Bearer Request消息由SGW-C处理，SGW-C向SGW-U发送Sxa会话修改消息。 
（可选）SMF+PGW-C保存接入信息。若PCF订阅的信息发生变化，则SMF+PGW-C向PCF发送Npcf_SMPolicyControl_Update

Request消息。
（可选）PCF根据当前的用户接入参数，授权策略控制参数，向SMF+PGW-C响应Npcf_SMPolicyControl_Update

Response消息。
SMF+PGW-C更新会话/承载参数，通过PFCP Session Modification Request
通知UPF+PGW-U更新PFCF会话，携带被更新的策略控制参数及S5/S8-U隧道信息。
UPF+PGW-U向SMF+PGW-C返回响应消息PFCP Session Modification Response
。
SMF+PGW-C向SGW响应Modify Bearer Response消息。 
SGW回复Modify Bearer Response给MME。 
UE检测到需要接入方式发生变化，则发起TAU流程，EPC核心网（MME+SGW+PGW）按照切换后TAU流程进行。 
（可选）核心网可以发起专有承载建立。若部署了PCC，则由PCF+PCRF触发专有承载建立。 
资源保护定时器超时，AMF通过UE Context Release Command
通知Source NR释放用户上下文。
资源保护定时器超时，AMF通过Npcf_AMPolicyControl_Delete
 Request通知PCF+PCRF删除策略会话。若在资源保护定时器未超时前，收到HSS+UDM去注册通知，或者资源保护定时器超时，AMF存在未迁移的PDU会话，则通知SMF释放这些PDU会话，携带原因为“REL_DUE_TO_HO”，SMF无需通知UE和RAN释放资源。
##### 连接态下基于N26接口，5G跨系统移动到4G，切换取消 
连接态下基于N26接口5G到4G切换取消流程如[图6](1601433938753.html#z8af3de5b3bc24b5790dcdd9a148f66d4__1b17b497-2033-4e0f-a2e7-c4d372476317)所示。
图6  连接态下基于N26接口5G到4G切换取消
[]images/%E8%BF%9E%E6%8E%A5%E6%80%815G%E5%88%B04G%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88.png)
流程说明如下： 
由于某些原因，比如UE重新选择到源NR的小区，源NR发送Handover Cancel
给AMF，通知AMF取消切换。
AMF发送Relocation Cancel Request
给MME，通知MME取消切换。
若已经通知SGW创建会话，则发送Delete Session Request给SGW，携带SI（Scope Indication）标记，表示SGW将释放UE的所有承载资源。 
SGW回复Delete Session Response给MME。 
（可选）若已经通知SGW创建了非直传隧道，则发送Delete Indirect Data Forwarding Tunnel
Request给SGW。 
（可选）SGW删除非直传隧道，并回复Delete Indirect Data Forwarding Tunnel Response。 
（可选）若已经通知目标eNodeB创建承载，则发送UE Context Release Command给目标eNodeB，不等待响应。 
MME回复Relocation Cancel Response
给AMF。
（可选）若已通知SMF+PGW-C创建非直传隧道，则AMF发送Nsmf_PDUSession_UpdateSMContext

Request，携带切换取消指示。
（可选）SMF+PGW-C通过N4接口消息通知UPF+PGW-U释放非直传数据。 
（可选）UPF+PGW-U释放资源后，响应SMF+PGW-C。 
（可选）SMF+PGW-C向AMF响应Nsmf_PDUSession_UpdateSMContext
 Response消息。
AMF回复Handover Cancel Acknowledge
给Source NR。
#### 无N26接口的跨系统移动 
本节包括以下流程： 
无N26接口的4G跨系统移动到5G 
无N26接口的5G跨系统移动到4G 
##### 无N26接口的4G跨系统移动到5G 
无N26接口的4G跨系统移动到5G流程如[图1](1601434801194.html#zd6a93300b9d042df965de62c556cd9b6__349bef53-224c-4f3c-9e13-0252bbdfcaa1)所示。
图1  无N26接口的4G跨系统移动到5G
[]images/4G%E5%88%B05G%E7%A7%BB%E5%8A%A8%E6%80%A7.png)
流程说明如下： 
UE已经注册到EPS系统，并激活了PDN连接。 
UE检测到需要切换到5G网络，比如进入5G覆盖区域，则发起Registration Request
，携带映射的5G-GUTI、UE从EPC移入指示、包含全部PDN连接关联的PDU会话ID的列表、注册类型为初始注册（如果为注册更新，则AMF将其看成是初始注册，并跳过PDU会话状态同步）。
AMF根据附着请求中的UE ID无法获取用户IMSI，且AMF配置工作在无N26互操作模式，发送Identify Request给UE，请求用户SUCI。
UE回复Identify Response，携带用户SUCI。 
执行鉴权、SMC、IMEI Check等过程。 
AMF发送Nudm_UEContextManagement_Registration
进行注册。
若UE从EPC移入、AMF配置工作在无N26互操作模式并且注册类型为初始注册，则AMF携带drFlag标记并设置值为true，指示UDM+HSS不需要下发注销通知给MME。 
若HSS+UDM支持UE同时在AMF和MME注册，则不会发送注销通知给AMF，且在注册响应中携带支持UE在AMF和MME同时注册指示。 
AMF发送Nudm_SubscriberDataManagement_Get
 Request给HSS+UDM，获取UE Context In SMF Data，其中包含4G激活PDN连接关联的DNN和SMF地址。
AMF选择PCF并向PCF注册。 
AMF下发Registration Accept
，携带分配的5G-GUTI。若HSS+UDM指示支持同时在AMF和MME注册，则携带支持无N26互操作指示。
UE回复Registration Complete
给AMF。
针对需要切换的PDU会话，UE触发已存在的PDU会话的激活流程，将4G PDN连接切换为5G PDU会话。AMF进行SMF选择，向SMF转发会话建立请求，携带"Existing PDU Session”指示。 
针对已切换为PDU会话的PDN连接，SMF+PGW-C向MME触发承载去活过程，但不通知UE。 
##### 无N26接口的5G跨系统移动到4G 
无N26接口的5G跨系统移动到4G流程如[图2](1601434801194.html#zd6a93300b9d042df965de62c556cd9b6__9c4756c9-94c7-4fea-9c2e-4b99e52a2a65)所示。
图2  无N26接口的5G跨系统移动到4G
[]images/1600398491059.png)
流程说明如下： 
UE注册到5GC并激活了PDU会话。 
UE检测到需要切换到4GS，比如进入4G网络覆盖区域，则根据网络指示“支持无N26互操作”，UE发送Attach Request给MME，携带4G GUTI（native GUTI或者mapped GUTI）和UE从5GC移入指示。若存在5G激活的PDU会话，则附着请求中包含PDN连接激活请求，请求类型为“Handover”，并携带包含该PDU会话ID的PCO。
MME根据附着请求中的UE ID无法获取用户IMSI，且MME配置工作在无N26互操作模式，则发送Identify Request给UE，请求用户IMSI。 
UE回复Identify Response，携带IMSI。 
执行鉴权、SMC、ESM Info等过程。 
MME发送Update Location Request，并且判断本局支持无N26互操作，UE Status指示用户已经在5G注册，则消息中携带Dual-Registration-5G-Indicator指示给HSS+UDM，HSS+UDM将不会下发去注册通知给AMF。 
HSS+UDM返回Update Location Acknowledge给MME，携带SMF+PGW-C地址、APN等信息。 
继续附着流程。 
若还存在未切换的PDU会话，则UE继续发起Handover类型的PDN连接建立流程，将5G PDU会话转化为4G PDN连接。 
针对已经切换完成的PDU会话，SMF+PGW-C触发5GC侧PDU会话释放，不通知UE。 
### VoNR/EPS Fallback 
VoNR :##### VoNR注册 
VoNR注册可分为以下3个流程，3个流程必须按顺序进行。 
[5G注册及数据DNN的PDU会话建立流程](1607333999903.html#zad8ecd73111d4b4c8f9848c165a171a7__ca889102-bd54-42c9-ac30-f6d0231a637b)
[IMS DNN的PDU会话建立与P-CSCF发现流程](1607333999903.html#zad8ecd73111d4b4c8f9848c165a171a7__c58dfdd6-44ae-436e-926f-5da547eba0c1)
[IMS注册流程](1607333999903.html#zad8ecd73111d4b4c8f9848c165a171a7__ac425815-7f66-4829-a104-81baa8ff33b9)
###### 5G注册及数据DNN的PDU会话建立流程 
5G注册及数据DNN的PDU会话建立流程如[图1](1607333999903.html#zad8ecd73111d4b4c8f9848c165a171a7__a95902fb-ffab-470a-bbdc-0ae9e16d1cf5)所示。
图1  5G注册及数据DNN的PDU会话建立流程
[]images/1607333999626.png)
流程说明： 
UE发送Registration Request
到(R)AN，消息中包含注册类型、用户标识、UE的5GC能力及可选的Requested NSSAI等参数。另外还包括VoNR关键信元： UE's usage setting。UE's usage setting包括以下两种取值：
Voice centric：表示UE支持IMS语音业务。支持voice centric的终端必须保证语音业务可用。 
Data centric：Data centric的UE即使无法在5GC网络获得语音业务，仍可以继续驻留在5GC网络中。 
(R)AN接收到消息，根据用户临时标识或Requested NSSAI选择合适的AMF，如果(R)AN无法选择到合适的AMF，则将Registration Request
发送给缺省AMF，由缺省AMF进行AMF选择。
(R)AN将Registration Request
消息转发给AMF。
（可选）如果Registration Request
中携带的是5G-GUTI，并且AMF检测到5G-GUTI不是本局分配的，AMF向Old AMF发送Namf_Communication_UEContextTransfer
 Request请求用户的SUPI和MM Context，请求消息中包含完整的注册请求NAS消息，Old AMF对请求消息中携带的NAS消息进行完整性检查。
（可选）Old AMF返回Namf_Communication_UEContextTransfer
 Response，参数包括SUPI、UE上下文等信息。
（可选）如果UE没有提供SUCI，也没有从Old AMF处获取到SUCI，AMF向UE发送Identity Request
消息请求获取SUCI。
（可选）UE向AMF返回Identity Response
消息，消息中包含SUCI。
（可选）如果AMF没有用户上下文，或者Registration Request
消息没有被完整性保护，或者完整性检查失败，AMF会调用AUSF发起UE鉴权过程，此时AMF会根据SUPI选择一个AUSF。
（可选）AUSF执行对UE的鉴权过程。 
（可选）如果AMF改变，New AMF向Old AMF发送Namf_Communication_RegistrationStatusUpdate
，通知Old AMF收到MM Context。
（可选）AMF向UE发送Identity Request
消息，请求获取PEI。UE向AMF返回Identity Response
消息包含SUPI。
（可选）AMF通过服务化接口消息N5g-eir_EquipmentIdentityCheck_Get向EIR发起IMEI检查过程，EIR向AMF返回检查结果响应。
（可选）如果第14步需要执行，则New AMF根据SUPI选择一个UDM实例。
（可选）New AMF及Old AMF分别执行如下操作： 
如果AMF改变，或者如果AMF没有用户的有效的上下文，AMF需要向UDM注册并获取签约数据。AMF调用UDM的服务化接口Nudm_UECM_Registration向UDM注册，以及订阅当UDM去注册这个AMF时UDM向AMF发送的变更通知。其中注册消息中携带Homogeneous support for IMS voice over PS Session indication用于指示5GC网络是否支持IMS语音业务。 
AMF调用UDM的服务化接口Nudm_SDM_Get获取签约数据。 
AMF获取签约数据成功后，通过Nudm_SDM_Subscribe向UDM订阅签约数据变更通知。 
New AMF向UDM注册成功后，UDM向Old AMF发送Nudm_UECM_DeregistrationNotify通知，携带通知原因值。 
Old AMF调用UDM的服务化接口Nudm_SDM_Unsubscribe取消签约数据订阅。 
（可选）如果AMF决定与PCF通信，则AMF选择一个PCF实例。
（可选）New AMF向PCF发起策略关联建立过程。 
AMF向NR发送UE RADIO CAPABILITY CHECK REQUEST消息。 
AMF收到NR响应UE RADIO CAPABILITY CHECK RESPONSE消息，保存IMS Voice Support Indicator，此字段指示无线对IMS语音连续性的支持能力。 
New AMF向UE发送Registration Accept
消息，接受UE发起的注册请求。如果New AMF为UE分配了新的5G-GUTI，则需要在本消息中携带。AMF确定5GS Network Feature Support信元，指示UE是否支持IMS voice over PS Session，该信元由UE语音能力、无线语音能力和运营商策略共同决定。
（可选）New AMF和PCF交互，完成UE策略关联建立。 
（可选）如果AMF为UE分配了新的5G-GUTI，则UE向New AMF发送Registration Complete
消息。
（可选）Vo5G用户先进行数据DNN会话建立过程，其中5QI取8或9，表示数据DNN缺省承载。 
###### IMS DNN的PDU会话建立与P-CSCF发现流程 
IMS DNN的PDU会话建立与P-CSCF发现流程如[图2](1607333999903.html#zad8ecd73111d4b4c8f9848c165a171a7__6f1d33de-7b01-481a-ba8c-f6fb8cfd5942)所示。
图2  IMS DNN的PDU会话建立与P-CSCF发现流程
[]images/1607333999736.png)
流程说明： 
UE向AMF发送PDU Session Establishment Request
消息。消息中包括：S-NSSAI(s)、DNN、PDU Session ID、Request type、N1 SMF container（PDU Session Establishment Request
，其中携带ePCO请求P-CSCF地址）等信息。
AMF执行SMF选择流程，根据切片信息选择合适的SMF。AMF接收到UE的PDU Session Establishment Request
消息，发现是创建新PDU会话时，会执行SMF选择流程为该PDU会话选择SMF。在AMF执行SMF选择过程中，AMF会与NSSF交互，获取网络切片信息，通过NRF选择一个合适的SMF。
AMF向SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息请求建立PDU会话。消息中包括：SUPI、DNN、S-NSSAI、PDU Session ID、AMF ID、Request Type、N1 SM container （PDU Session Establishment Request
）、User location information、Access Type、PEI，GPSI、Subscription For PDU Session Status Notification等信息。
（可选）SMF向UDM发起会话注册并获取签约信息，签约信息包括：SSC mode、Session AMBR等。 
SMF向AMF回复Nsmf_PDUSession_CreateSMContext
 Response。根据会话是否成功建立，消息中携带不同的参数。
若会话建立流程执行成功并创建了SM上下文，则在Nsmf_PDUSession_CreateSMContext Response消息中将SM上下文的ID带给AMF。 
若会话建立流程执行失败，则通过消息中的Cause通知AMF会话流程失败，AMF释放该会话相关资源，并将N1 SM container（PDU Session Reject）发送给UE。 
SMF执行PCF选择功能选择一个合适的PCF。SMF发现是创建新PDU会话时，通过NRF来选择一个合适的PCF。 
SMF向PCF发送建立PDU-CAN会话流程。PCF下发给SMF的相关QoS控制策略、计费控制策略、UPF选择策略等信息。 
SMF根据DNN、DNAI、用户的位置信息等进行UPF选择。 
SMF向PCF发起Session Management Policy Modification消息，消息携带选择的UPF信息和给UE分配的IP地址，获取UPF所需要的计费控制策略。 
（可选）SMF向选择的UPF发起N4会话建立过程，携带给UPF的各种规则，包括PDR、URR、QER、BAR、FAR，UPF返回响应消息。
SMF向AMF发送Namf_Communication_N1N2MessageTransfer
消息，请求传递N2资源，携带N1 Container和N2 Container，其中N1 Container为SMF回复给UE的PDU会话建立响应（携带P-CSCF地址），N2 Container为SMF向RAN发起的资源建立请求。完成后AMF向SMF发送Namf_Communication_N1N2MessageTransfer
_Ack消息。
AMF向(R)AN发送N2 PDU Session Request消息请求N2 PDU会话创建，向(R)AN透传PDU Session Establishment Accept
消息以及SMF发起的AN-specific resource setup消息。
PDU Session Establishment Accept中，携带QoS Rule规则。 
AN-specific resource setup中，携带QoS Profile、UPF的媒体面隧道端点信息。 
(R)AN和UE之间根据AN-specific resource setup消息建立资源连接。 
(R)AN向AMF回复N2 PDU Session Response消息，携带(R)AN侧下行媒体面隧道端点信息。 
AMF向SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带N2 Container，Container为(R)AN回复给SMF的资源建立响应，其中有(R)AN侧的媒体面隧道端点信息。
SMF向UPF发起N4 Session Modification procedure流程，协商(R)AN侧下行媒体面隧道信息，并联合UDM完成注册。 
SMF向AMF回复Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）SMF会话建立完成，向AMF发起Nsmf_PDUSession_SMContextNotify消息。 
（可选）如果UE申请的是IPv6类型的PDU会话，SMF还需要通过UPF向UE发布IPv6路由公告。 
（可选）如果会话建立在第4步之后失败了，SMF需要向UDM发起去注册和去订阅的流程，UDM返回响应消息。 
###### IMS注册流程 
IMS注册流程如[图3](1607333999903.html#zad8ecd73111d4b4c8f9848c165a171a7__06150180-ce93-4691-8628-a2d906768d8b)所示。
图3  IMS注册流程
[]images/1607333999846.png)
流程说明： 
UE向IMS拜访网络入口P-CSCF发送REGISTER消息请求注册。 
P-CSCF收到REGISTER消息后，解析出用户的PANI（P-Access-Network-Info），识别出5G信息，确认VoNR用户的PANI头域增加了NR相关接入信息如“3GPP-NR”、“3GPP-NR-FDD”或“3GPP-NR-TDD”， 即可使用VoLTE的所有功能。 
当P-CSCF向PCF订阅了“IP接入网络类型变化事件”和“接入网信息上报事件"时，则会触发P-CSCF到PCF的媒体承载订阅流程，PCF接着会通知5GC进行IP接入网类型和位置信息上报，即进行第2~6步。否则，直接进行第7步。 
（可选）P-CSCF向PCF发送AAR消息，请求获取UE的接入网类型。
（可选）PCF向P-CSCF返回AAA消息，其中IP-CAN-Type和RAT-Type AVP携带了UE的接入网类型。
PCF通知5GC去进行位置上报，5GC对PCF进行位置上报后，UE的位置信息通过RAR消息上报给P-CSCF。
（可选）PCF向P-CSCF发送RAR消息。 
（可选）P-CSCF向PCF返回RAA响应。
如果P-CSCF成功获取到UE位置信息，则会从ULI中提取MCC和MNC信息，保存到本地用户数据中并生成PVNI（P-Visited-Network-ID）头域添加到REGISTER消息中。同时，P-CSCF也会根据ULI刷新PANI头域。 
如果P-CSCF未获取到UE位置信息，则无需生成PVNI头域。 
P-CSCF向I-CSCF转发REGISTER注册消息。 
I-CSCF向UDM发送UAR消息，请求获取提供服务的S-CSCF地址信息。
UDM向I-CSCF返回UAA响应消息， I-CSCF向指定的S-CSCF转发REGISTER消息，S-CSCF收到注册消息后，解析出PANI，识别出5G信息，向UDM获取鉴权数据。
S-CSCF向UDM发送MAR消息获取用户鉴权向量并告知该S-CSCF为用户提供服务。
UDM向S-CSCF返回MAA消息，消息中携带用户鉴权向量信息。
S-CSCF经I-CSCF向P-CSCF返回401 Unauthorized响应。 
P-CSCF继续向UE转发401，UE收到401响应后，进行认证处理。 
UE对网络侧鉴权成功后，会基于鉴权数据，重新构造REGISTER消息，按照初始REGISTER消息的路径发给P-CSCF。 
P-CSCF向I-CSCF转发REGISTER消息。 
I-CSCF向UDM获取之前为用户提供服务的S-CSCF的地址，并向S-CSCF转发REGISTER消息。 
S-CSCF收到鉴权响应后，将期望收到的鉴权响应XRES和实际收到的鉴权响应RES进行比较。
如果两者匹配，则IMS网络对UE鉴权通过，S-CSCF向UDM下载用户签约数据并返回200响应。 
如果两者不匹配，IMS网络对UE鉴权失败。 
S-CSCF根据用户签约信息中的iFC数据中的AS地址，向AS发送第三方注册请求。 
AS收到REGISTER注册请求后，发现用户是第一次注册，则解析出PANI，识别5G信息，向UDM发送UDR消息获取用户数据。
UDM向AS返回UDA响应。
AS向UDM发送SNR消息，请求订阅用户数据。
AS收到UDM返回的SNA响应。
AS根据收到的用户数据对用户进行鉴权。鉴权通过后，向S-CSCF返回第三方注册的200成功响应。至此，用户的注册流程完成。 
##### VoNR语音呼叫流程 
本节包括以下流程： 
VoNR语音呼叫主叫流程 
VoNR语音呼叫被叫流程 
###### VoNR语音呼叫主叫流程 
VoNR语音呼叫主叫流程如[图1](1600310204625.html#T_1554257199539__b2cbd2fb-0e17-496c-acbd-7ed91691fc77)所示。
图1  VoNR语音呼叫主叫流程
[]images/1600310204455.png)
流程说明如下： 
5G和IMS注册过程。 
5G注册过程。 
IMS DNN的PDU会话建立过程(5QI=5)与P-CSCF发现。
IMS注册过程。 
（可选）如果UE处于CM-IDLE态，UE通过发起Service Request
，建立NR与UPF的用户面连接。
UE_A发起初始INVITE请求，消息中通过PANI头域携带用户接入信息。P-CSCF收到INVITE消息后，解析出主叫用户的PANI，识别出5G信息，确认VoNR用户的PANI头域增加了NR相关接入信息，如“3GPP-NR”、“3GPP-NR-FDD”或“3GPP-NR-TDD”。
如果P-CSCF向PCF订阅了“IP接入网络类型变化事件”和“接入网信息上报事件”，则会触发P-CSCF到PCF的媒体承载订阅流程，即进行第3~7步。 
如果P-CSCF没有向PCF订阅“IP接入网络类型变化事件”和“接入网信息上报事件”，则P-CSCF会直接转发INVITE消息，无需等待RAR消息，也不更改PANI头域，即无Network-Provided参数，则直接进行第8步。如果P-CSCF未在呼叫时订阅“IP接入网络类型变化事件”，则使用注册时记录的接入网类型。 
P-CSCF向PCF发送AAR消息，请求获取UE的接入网类型。
PCF向P-CSCF返回AAA消息，其中IP-CAN-Type和RAT-Type AVP携带了UE的接入网类型。
PCF发起建立专用QoS Flow的流程。 
PCF将位置信息通过RAR消息发送给P-CSCF，此时的位置信息为5G信息，其中IP-CAN-Type、RAT-Type和3GPP-User-Location-Info AVP都携带5G信元。 
P-CSCF收到RAR消息后，向PCF返回RAA响应，并根据RAR消息中的位置信息刷新SIP消息中的PANI头域，增加Network-Provided参数，随着INVITE消息转发给S-CSCF。 
P-CSCF将INVITE消息发送给S-CSCF。S-CSCF收到INVITE消息后，会做如下处理： 
解析出主叫用户的PANI，识别出5G信息，确认用户的PANI头域增加了NR相关接入信息，即可使用VoNR的所有功能。 
从P-Asserted-Identity头域判断主叫号码已注册，则根据主叫用户签约的iFC模板数据，去AS触发主叫业务。
S-CSCF向AS转发INVITE消息。 
如果Rx策略未订阅“IP接入网络类型变化事件”和“接入网信息上报事件”，AS收到INVITE消息后，如果业务需要位置信息但发现PANI头域无Network-Provided参数，则会触发到UDM的取位置信息过程，即进行10~12步。 
如果Rx策略订阅了“IP接入网络类型变化事件”和“接入网信息上报事件”，AS收到INVITE消息后，解析出PANI，识别出5G信息，确保用户的PANI头域携带了Network-Provided参数且增加了NR相关接入信息，即可使用VoNR的所有功能，向主叫UE_A提供语音业务，进行第13步。 
（可选）AS向UDM发送UDR消息，请求获取用户的位置信息。
（可选）UDM经AMF向NR获取用户的位置信息。 
（可选）UDM向AS返回UDA消息，消息中通过User-Data携带AS请求的用户数据。用户从5G接入时，直接用5G位置信息替换PANI头域中的位置信息，同时增加Network-Provided参数。
AS向S-CSCF返回INVITE消息。 
I-CSCF将呼叫路由到被叫侧，继续完成后续的呼叫流程。 
被叫侧返回183响应，表示呼叫请求正在处理，消息中携带被叫的媒体信息。 
主叫UE_A向被叫侧发送的PRACK请求，表示主叫侧成功接收183响应，并且进行资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫侧返回180响应，表示被叫振铃。 
主叫UE_A向被叫侧发送PRACK请求，表示主叫侧成功接收180响应，并且已完成资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫摘机，向主叫侧返回200 OK响应。 
主叫UE_A返回INVITE消息的ACK响应消息，主被叫进入通话。 
主叫挂机，主叫终端向P-CSCF发送BYE消息，消息中携带PANI头域。 
P-CSCF收到BYE消息后，根据配置触发STR请求终止会话，并获取用户位置信息。
PCF向P-CSCF返回STA消息，消息中IP-CAN-Type和RAT-Type AVP携带UE的接入网类型信息。
P-CSCF从RAR消息中提取UE位置信息更新到PANI头域中，增加Network-Provided参数，释放5QI=1的媒体资源，将BYE消息经S-CSCF路由到AS。 
AS收到BYE消息后，根据消息中的PANI头域将用户位置信息填写到Finish/Last PANI中，再将BYE消息路由到被叫侧。 
拆线成功后，被叫侧返回200 OK响应消息，表示主被叫之间的呼叫链路已拆除。 
###### VoNR语音呼叫被叫流程 
VoNR语音呼叫被叫流程如[图2](1600310204625.html#T_1554257199539__6eede584-dd1a-493d-b133-15971f681c9e)所示。
图2  VoNR语音呼叫被叫流程
[]images/1600310204575.png)
流程说明如下： 
5G注册和IMS注册过程。 
5G注册过程。 
IMS DNN的PDU会话建立过程(5QI=5)与P-CSCF发现。 
IMS注册过程。 
UE_A呼叫UE_B，为用户提供IMS业务的I/S-CSCF收到主叫侧发送的INVITE消息。 
S-CSCF将INVITE消息路由到AS，触发被叫业务和被叫网络域选。 
AS收到INVITE消息后，判断用户在IMS网络已注册，则启动T-ADS域选流程。其中UDM收到查询T-ADS信息的消息后，判断UE的“IMS Voice over PS Sessions”的值：
如果值为“non-homogeneous”或“unknown”，则发起向T-ADS的查询，向AMF发送Namf_MT_ProvideDomainSelectionInfo Request消息。AMF向UDM返回Namf_MT_ProvideDomainSelectionInfo Response消息，UDM向AS返回UE的T-ADS信息。AMF获取用户的如下信息：UE当前注册区域是否支持IMUE最后一次活动时间当前Access Type和RAT type 
如果值为“Supported”或“Not Supported”，则直接向IMS返回UE的T-ADS信息。 
如果AS签约了被叫位置相关业务，则会启动到UDM获取位置信息的过程，UDM发起终端的位置上报流程。AS收到UDM返回的UDA，取出位置信息，发现增加了5G位置信息5GSLocationInformation和用户状态的结构5GSUserState，该位置信息不会去替换INVITE消息PANI头域中的位置信息。
AS根据域选结果将INVITE消息返回给I/S-CSCF。 
I/S-CSCF经P-CSCF将INVITE消息路由给UPF。如果UE_B在空闲态，则5GC启动Paging流程，对被叫UE_B进行寻呼。 
UPF对UE_B进行寻呼。 
寻呼成功后，UE_B通过业务请求过程恢复UE_B和UPF之间的用户面连接，与主叫流程的业务请求过程相同。 
UPF将INVITE消息路由给被叫UE_B。 
UE_B返回183响应，表示呼叫请求正在处理，消息中携带被叫的PANI和媒体信息。P-CSCF收到183消息后，解析出主叫用户的PANI，识别出5G信息，确保VoNR用户的PANI头域增加了NR相关接入信息如“3GPP-NR”、“3GPP-NR-FDD”或“3GPP-NR-TDD”， 即可使用VoLTE的所有功能。 
如果P-CSCF向PCF订阅了“IP接入网络类型变化事件”和“接入网信息上报事件”，则会触发P-CSCF到PCF的媒体承载订阅流程，即进行第12~16步。在AAA消息中，PCF会通过IP-CAN-Type和RAT-Type AVP携带UE的接入网类型的信息。PCF接着会通知5GC去进行媒体专用QoS Flow的建立及用户位置上报。由于NR不支持语音，故在专有QoS Flow的建立过程中，触发EPS Fallback流程。 
如果Rx策略未订阅“IP接入网络类型变化事件”和“接入网信息上报事件”，则PCF通知5GC进行专用QoS Flow的建立过程中触发EPS Fallback流程，即进行第14步。回落后，P-CSCF会直接转发183消息，无需等待RAR消息，也不会更改PANI头域，即无Network-Provided参数，直接进行第17步。 
如果P-CSCF未在呼叫时订阅“IP接入网络类型变化事件”，则使用注册时记录的接入网类型。 
P-CSCF向PCF发送AAR消息，请求获取UE的接入网类型。 
PCF向P-CSCF返回AAA消息，其中IP-CAN-Type和RAT-Type AVP携带了UE的接入网类型。 
PCF发起专用QoS Flow建立流程。 
PCF将位置信息通过RAR消息发送给P-CSCF，此时的位置信息为5G信息，其中IP-CAN-Type、RAT-Type和3GPP-User-Location-Info AVP都携带5G信元。 
P-CSCF收到RAR消息后，向PCF返回RAA响应。 
P-CSCF根据RAR消息中的位置信息刷新SIP消息中的PANI头域，增加Network-Provided参数，随着183消息转发给S-CSCF。 
S-CSCF向AS转发183消息。AS收到183消息后，解析出用户的PANI，识别出4G信息，确认用户的PANI头域增加了NR相关的接入信息， 即可使用VoNR的所有功能，则向被叫UE_B提供语音业务并将被叫UE_B的PANI写入CDR。
AS经I/S-CSCF向主叫侧返回183消息。 
主叫侧向被叫侧发送的PRACK请求，表示主叫侧成功接收183响应，并且进行资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫侧返回180响应，表示被叫振铃。 
主叫UE_A向被叫侧发送PRACK请求，表示主叫侧成功接收180响应，并且已完成资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫摘机，向主叫侧返回200 OK响应。 
主叫侧返回INVITE消息的ACK响应消息，主被叫进入通话。 
挂机释放流程。 
#### EPS Fallback 
##### EPS Fallback注册 
EPS Fallback注册流程同[VoNR注册](1607333999903.html)。
##### EPS Fallback语音呼叫 
本节包括以下流程： 
EPS Fallback语音呼叫主叫流程 
EPS Fallback语音呼叫被叫流程 
###### EPS Fallback语音呼叫主叫流程 
EPS Fallback语音呼叫主叫流程如[图1](1600310161033.html#T_1554257199539__6afdc832-f91f-4192-b4a5-decc631909f7)所示。
图1  EPS Fallback语音呼叫主叫流程
[]images/1657675641745.png)流程说明如下：5G注册及IMS注册过程。 
5G注册过程。 
IMS DNN的PDU会话建立过程(5QI=5)与P-CSCF发现。
IMS注册过程。 
（可选）如果UE处于CM-IDLE态，UE通过发起Service Request，建立NR与UPF的用户面连接。
UE_A发起初始INVITE请求，消息中通过PANI头域携带用户接入信息。P-CSCF收到INVITE消息后，解析出主叫用户的PANI，识别出5G信息，确认VoNR用户的PANI头域增加了NR相关接入信息如“3GPP-NR”、“3GPP-NR-FDD”或“3GPP-NR-TDD”。
如果P-CSCF向PCF订阅了“IP接入网络类型变化事件”和“接入网信息上报事件”，则会触发P-CSCF到PCF的媒体承载订阅流程，即进行第3~7步。由于NR不支持语音，故在专有QoS Flow建立中，会触发EPS Fallback的流程，进行第5步。 
如果P-CSCF没有向PCF订阅“IP接入网络类型变化事件”和“接入网信息上报事件”，则PCF通知5GC进行专用QoS Flow的建立过程中触发EPS Fallback流程，即进行第5步。回落后，会直接转发INVITE消息，无需等待RAR消息，也不更改PANI头域，即无Network-Provided参数，则直接进行第8步。如果P-CSCF未在呼叫时订阅“IP接入网络类型变化事件”，则使用注册时记录的接入网类型。 
P-CSCF向PCF发送AAR消息，请求获取UE的接入网类型。
PCF向P-CSCF返回AAA消息，其中IP-CAN-Type和RAT-Type AVP携带了UE的接入网类型。
PCF发起建立专用QoS Flow的流程，当流程到(R)AN后，(R)AN判断发起EPS Fallback的流程。 
EPS Fallback之前，(R)AN会通知UE_A测量LTE的信号，再通过切换或者重定向的方式向E-UTRAN的回落。整个回落过程，没有信令通知IMS，故IMS不感知EPS Fallback流程的触发。 
EPS Fallback之后，回落到LTE网络，由VoLTE提供服务。 
PCF将回落后的位置信息通过RAR消息发送给P-CSCF，此时的位置信息为回落后4G的信息，其中IP-CAN-Type、RAT-Type和3GPP-User-Location-Info AVP都携带4G的信元。
P-CSCF收到RAR消息后，向PCF返回RAA响应，并根据RAR消息中的位置信息刷新SIP消息中的PANI头域，增加Network-Provided参数，随着INVITE消息转发给S-CSCF。
P-CSCF将INVITE消息路由给S-CSCF。S-CSCF收到INVITE消息后，会做如下处理： 
解析出主叫用户的PANI，识别出4G信息，确认用户的PANI头域增加了E-UTRAN相关接入信息， 即可使用VoLTE的所有功能。 
从P-Asserted-Identity头域判断主叫号码已注册，则根据主叫用户签约的iFC模板数据，去AS触发主叫业务。
S-CSCF向AS转发INVITE消息。 
如果Rx策略未订阅“IP接入网络类型变化事件”和“接入网信息上报事件”，AS收到INVITE消息后，如果业务需要位置信息但发现PANI头域无Network-Provided参数，则会触发到UDM获取位置信息的过程。此时UDM记录的是MME的地址，则触发4G的取位置信息过程，即进行10~12步。 
如果Rx策略订阅了“IP接入网络类型变化事件”和“接入网信息上报事件”，AS收到INVITE消息后，解析出PANI，识别出4G信息，确保用户的PANI头域携带了Network-Provided参数且增加了E-UTRAN相关接入信息， 即可使用VoLTE的所有功能，向主叫UE_A提供语音业务，接着进行第13步。 
（可选）AS向UDM发送UDR消息，请求获取用户的位置信息。
（可选）UDM经MME向E-UTRAN获取用户的位置信息。 
（可选）UDM向AS返回UDA消息，消息中通过User-Data携带AS请求的用户数据。用户从4G接入时，直接用4G位置信息替换PANI头域中的位置信息，同时增加Network-Provided参数。
AS向S-CSCF返回INVITE消息。 
I-CSCF将呼叫路由到被叫侧，继续完成后续呼叫流程。 
被叫侧返回183响应，表示呼叫请求正在处理，消息中携带被叫的媒体信息。 
主叫UE_A向被叫侧发送的PRACK请求，表示主叫侧成功接收183响应，并且进行资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫侧返回180响应，表示被叫振铃。 
主叫UE_A向被叫侧发送PRACK请求，表示主叫侧成功接收180响应，并且已完成资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫摘机，向主叫侧返回200 OK响应。 
主叫UE_A返回INVITE消息的ACK响应消息，主被叫进入通话。 
主叫挂机，主叫终端向P-CSCF发送BYE消息，消息中携带PANI头域。 
P-CSCF收到BYE消息后，根据配置触发STR请求终止会话，并获取用户位置信息。
PCF向P-CSCF返回STA消息，消息中IP-CAN-Type和RAT-Type AVP携带UE的接入网类型信息。
P-CSCF从RAR消息中提取UE位置信息更新到PANI头域中，增加Network-Provided参数，释放QCI=1的媒体资源，将BYE消息经S-CSCF路由到AS。 
AS收到BYE消息后，根据消息中的PANI头域将用户位置信息填写到Finish/Last PANI中，再将BYE消息路由到被叫侧。 
拆线成功后，被叫侧返回200 OK响应消息，表示主被叫之间的呼叫链路已拆除。 
###### EPS Fallback语音呼叫被叫流程 
EPS Fallback语音呼叫被叫流程如[图2](1600310161033.html#T_1554257199539__59b80d93-d456-4652-923b-43b9f26dfe1e)所示。
图2  EPS Fallback语音呼叫被叫流程
[]images/1657676959608.png)流程说明如下： 
5G注册和IMS注册过程。 
5G注册过程。 
IMS DNN的PDU会话建立过程(5QI=5)与P-CSCF发现。 
IMS注册过程。 
UE_A呼叫UE_B，为用户提供IMS业务的I/S-CSCF收到主叫侧发送的INVITE消息。 
S-CSCF将INVITE消息路由到AS，触发被叫业务和被叫网络域选。 
AS收到INVITE消息后，判断用户在IMS网络已注册，则启动T-ADS域选流程。其中UDM收到查询T-ADS信息的消息后，判断UE的“IMS Voice over PS Sessions”的值：
如果值为“non-homogeneous”或“unknown”，则发起向T-ADS的查询，给AMF发送Namf_MT_ProvideDomainSelectionInfo Request消息。AMF向UDM返回Namf_MT_ProvideDomainSelectionInfo Response消息，UDM向AS返回UE的T-ADS信息。AMF获取用户的如下信息：UE当前注册区域是否支持IMSUE最后一次活动时间当前Access Type和RAT type 
如果值为“Supported”或“Not Supported”，则直接向IMS返回UE的T-ADS信息。 
如果AS签约了被叫位置相关业务，则会启动到UDM获取位置信息的过程，UDM发起终端的位置上报流程。AS收到UDM返回的UDA，取出位置信息，发现增加了5G位置信息5GSLocationInformation和用户状态的结构5GSUserState，该位置信息不会去替换INVITE消息PANI头域中的位置信息。
AS根据域选结果将INVITE消息返回给I/S-CSCF。 
I/S-CSCF经P-CSCF将INVITE消息路由给UPF。如果UE_B在空闲态，则5GC启动Paging流程，对被叫UE_B进行寻呼。 
AMF对UE_B进行寻呼。 
寻呼成功后，UE_B通过Service Request
过程恢复UE_B和UPF之间的用户面连接，与主叫流程的Service Request
过程相同。
UPF将INVITE消息路由给被叫UE_B。 
UE_B返回183响应，表示呼叫请求正在处理，消息中携带被叫的PANI和媒体信息。P-CSCF收到183消息后，解析出主叫用户的PANI，识别出5G信息，确保VoNR用户的PANI头域增加了NR相关接入信息如“3GPP-NR”、“3GPP-NR-FDD”或“3GPP-NR-TDD”， 即可使用VoLTE的所有功能。
如果P-CSCF向PCF订阅了“IP接入网络类型变化事件”和“接入网信息上报事件”，则会触发P-CSCF到PCF的媒体承载订阅流程，即进行第12~16步。在AAA消息中，PCF会通过IP-CAN-Type和RAT-Type AVP携带UE的接入网类型的信息。PCF接着会通知5GC进行媒体专用QoS Flow的建立及用户位置上报。由于NR不支持语音，故在专有QoS Flow建立中，会触发EPS Fallback的流程。 
如果Rx策略未订阅“IP接入网络类型变化事件”和“接入网信息上报事件”，则PCF通知5GC进行专用QoS Flow的建立过程中触发EPS Fallback流程，即进行第14步。回落后，P-CSCF会直接转发183消息，无需等待RAR消息，也不会更改PANI头域，即无Network-Provided参数，直接进行第17步。 
如果P-CSCF未在呼叫时订阅“IP接入网络类型变化事件”，则使用注册时记录的接入网类型。 
P-CSCF向PCF发送AAR消息，请求获取UE的接入网类型。
PCF向P-CSCF返回AAA消息，其中IP-CAN-Type和RAT-Type AVP携带了UE的接入网类型。
PCF发起专用QoS Flow建立流程，当流程到(R)AN后，(R)AN根据配置判断是否发起EPS Fallback的流程。 
EPS Fallback之前，(R)AN会通知UE_B测量LTE的信号，再通过切换或者重定向的方式向E-UTRAN回落。整个回落过程，没有信令通知IMS，故IMS不感知EPS Fallback流程的触发。 
EPS Fallback之后，回落到LTE网络，由VoLTE提供服务。 
PCF将回落后的位置信息通过RAR消息发送给P-CSCF，此时的位置信息为回落后4G的信息，其中IP-CAN-Type、RAT-Type和3GPP-User-Location-Info AVP都携带4G的信元。
P-CSCF收到RAR消息后，向PCF返回RAA响应。
P-CSCF根据RAR消息中的位置信息刷新SIP消息中的PANI头域，增加Network-Provided参数，随着183消息转发给S-CSCF。 
S-CSCF向AS转发183消息。AS收到183消息后，解析出用户的PANI，识别出4G信息，确认用户的PANI头域增加E-UTRAN相关接入信息如“3GPP-E-UTRAN-FDD”或“3GPP-E-UTRAN-TDD”， 即可使用VoLTE的所有功能，则向被叫UE_B提供语音业务并将被叫UE_B的PANI写入CDR。
AS经I/S-CSCF向主叫侧返回183消息。 
主叫侧向被叫侧发送的PRACK请求，表示主叫侧成功接收183响应，并且进行资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫侧返回180响应，表示被叫振铃。 
主叫UE_A向被叫侧发送PRACK请求，表示主叫侧成功接收180响应，并且已完成资源预留。 
被叫侧返回针对PRACK请求的200 OK响应，表示成功接收PRACK请求。 
被叫摘机，向主叫侧返回200 OK响应。 
主叫侧返回INVITE消息的ACK响应消息，主被叫进入通话。 
挂机释放流程。 
### 跨SMF服务区互联 
UE进行跨区域移动时，当UE所在的新区域超出了原来SMF的服务范围时，需要在接入的AMF和原SMF之间插入能够为当前服务区域提供服务的I-SMF（Intermediate SMF），以保证用户会话业务的连续性。 
I-SMF，即中间SMF，是UE移动到原SMF无法控制的区域时插入的SMF，用以支持用户在当前服务区域的业务。I-SMF是一个相对的概念，是具有I-SMF功能的SMF。一个SMF在不同场景中，可以以不同的形态开展业务，即以SMF或I-SMF的形态开展业务。 
假设某设备的NF类型为SMF，该设备的服务区域为A区域： 
当该设备为本区域用户提供服务时，该SMF作为SMF在流程中发挥作用。 
当一个用户由其他区域移动至本区域时，服务于该用户的原SMF无法在该区域提供服务，此时，该区域的AMF会选择本区域的SMF作为I-SMF为用户提供服务，以保证用户业务的连续性。 
#### 注册管理 
##### 注册更新 
根据注册更新过程中，是否存在I-SMF改变，划分如下四种场景： 
I-SMF更换的注册更新 
I-SMF插入的注册更新 
I-SMF删除的注册更新 
I-SMF不变的注册更新 
###### I-SMF更换的注册更新 
I-SMF更换的注册更新流程如[图1](1600152917702.html#z23668bc9cfea437ab888a2a2145fe920__92b9d1bf-6574-45c9-aed5-0a0e8128628b)所示。
图1  I-SMF更换的注册更新
[]images/1603099251443.png)
流程说明： 
UE发起移动性注册更新流程，向(R)AN发送AN消息，包括AN parameters和Registration Request
消息。(R)AN将Registration Request
消息经N2接口转发给AMF。
AMF根据UE的位置判断其移出I-SMF的服务区域，需要更换I-SMF，则发起I-SMF重选过程，并向Target I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息。
Target I-SMF向Source I-SMF发送Nsmf_PDUSession_Context Request消息，Source I-SMF返回Nsmf_PDUSession_Context Response消息。 
Target I-SMF选择Target I-UPF。 
Target I-SMF向Target I-UPF发起N4会话建立流程。 
（可选）建立转发隧道。 
假如有下行数据被缓存，则Target I-SMF向Source I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，要求建立转发隧道。
Source I-SMF向Source I-UPF发起N4 Session Modification流程。 
Source I-SMF向Target I-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response消息。
Target I-SMF与A-SMF、A-UPF交互。 
Target I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request消息。
A-SMF向A-UPF发起N4会话更新流程。 
A-SMF向Target I-SMF返回Nsmf_PDUSession_Update
 Response消息。

Target I-SMF向AMF发送Nsmf_PDUSession_CreateSMContext
 Response消息，同时Target I-SMF启动一个定时器用于释放转发隧道。
AMF向UE发送Registration Accept
消息。
（可选）如果分配了5G-5GTI，UE向New AMF返回Registration Complete
消息。
AMF向Source I-SMF发送Nsmf_PDUSession_ReleaseSMContext
 Request消息，Source I-SMF返回Nsmf_PDUSession_ReleaseSMContext
 Response消息。
AMF向Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息。
（可选）Target I-SMF向Target I-UPF发起N4 Session Modification流程。 
（可选）Target I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request消息。
（可选）A-SMF向PCF发起SM策略更新请求，上报位置及接入类型变化信息。 
（可选）A-SMF向Target I-SMF返回Nsmf_PDUSession_Update
 Response消息。
（可选） Target I-SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）Target I-SMF向Target I-UPF发起转发隧道删除流程。 
（可选）Source I-SMF向Source I-UPF发起会话释放流程，释放PDU会话相关资源。 
###### I-SMF插入的注册更新 
I-SMF插入的注册更新流程如[图2](1600152917702.html#z23668bc9cfea437ab888a2a2145fe920__914a56a9-1d30-40f0-a50c-431ea7908a58)所示。
图2  I-SMF插入的注册更新
[]images/%E4%B8%8B%E8%BD%BD.png)
流程说明： 
UE发起移动性注册更新流程，向(R)AN发送AN消息包括AN parameters和Registration Request
消息。(R)AN将Registration Request
消息经N2接口转发给AMF。
AMF根据UE的位置判断其移出SMF的服务区域，需要插入I-SMF，则发起I-SMF选择过程，并向Target I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息。
Target I-SMF向A-SMF发送Nsmf_PDUSession_Context Request消息，A-SMF返回Nsmf_PDUSession_Context Response消息。 
Target I-SMF选择Target I-UPF。 
Target I-SMF向Target I-UPF发起N4会话建立流程。 
（可选）建立转发隧道。 
假如有下行数据被缓存，则Target I-SMF向A-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，要求建立转发隧道。
A-SMF向Source I-UPF发起N4会话更新流程。 
A-SMF向Target I-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response消息。
Target I-SMF与A-SMF、A-UPF交互。 
Target I-SMF向A-SMF发送Nsmf_PDUSession_Create
 Request消息。
A-SMF向A-UPF发起N4会话更新流程。 
A-SMF向Target I-SMF返回Nsmf_PDUSession_Create
 Response消息。
Target I-SMF向AMF发送Nsmf_PDUSession_CreateSMContext
 Response消息，同时Target I-SMF启动一个定时器用于释放转发隧道。
AMF向UE发送Registration Accept
消息。
（可选）如果分配了5G-5GTI，UE向New AMF返回Registration Complete
消息。
AMF向Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息。
（可选）Target I-SMF向Target I-UPF发起N4会话更新流程。 
（可选）Target I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request 消息。
（可选）A-SMF向PCF发起SM策略更新请求，上报位置及接入类型变化信息。 
（可选）A-SMF向Target I-SMF返回Nsmf_PDUSession_Update
 Response消息。
（可选） Target I-SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）Target I-SMF向Target I-UPF发起转发隧道删除流程。 
（可选）A-SMF向Source I-UPF发起会话释放流程，释放PDU会话相关资源。 
###### I-SMF删除的注册更新 
I-SMF删除的注册更新如[图3](1600152917702.html#z23668bc9cfea437ab888a2a2145fe920__d2f4531e-4b74-49eb-be34-0b5a6a59e03b)所示。
图3  I-SMF删除的注册更新
[]images/1603332688643.png)
流程说明： 
UE发起移动性注册更新流程，向(R)AN发送AN消息包括AN parameters和Registration Request
消息。(R)AN将Registration Request
消息经N2接口转发给AMF。
AMF根据UE的位置判断其移入A-SMF的服务区域，AMF向A-SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息。
A-SMF向Source I-SMF发送Nsmf_PDUSession_Context Request消息，Source I-SMF返回Nsmf_PDUSession_Context Response消息。 
A-SMF选择Target I-UPF。 
A-SMF向Target I-UPF发起N4会话建立流程。 
A-SMF向A-UPF发起N4会话更新流程。 
（可选）建立转发隧道。 
A-SMF向Source I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息。
Source I-SMF向Source I-UPF发起N4 Session Modification流程。 
Source I-SMF向A-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response消息。
A-SMF向A-UPF发起N4会话更新流程。 
A-SMF向AMF发送Nsmf_PDUSession_CreateSMContext
 Response消息，同时A-SMF启动一个定时器用于释放转发隧道。
AMF向UE发送Registration Accept
消息。
（可选）如果分配了5G-5GTI，UE向New AMF返回Registration Complete
消息。
AMF向Source I-SMF发送Nsmf_PDUSession_ReleaseSMContext
 Request消息，Source I-SMF返回Nsmf_PDUSession_ReleaseSMContext
 Response消息。
AMF向A-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息。
（可选）A-SMF向PCF发起SM策略更新请求，上报位置及接入类型变化信息。 
（可选）A-SMF向Target I-UPF发起N4会话更新流程。 
（可选）A-SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）A-SMF向Target I-UPF发起转发隧道删除流程。 
（可选）Source I-SMF向Source I-UPF发起N4会话释放流程，释放PDU会话相关资源。 
###### I-SMF不变的注册更新 
I-SMF不变的注册更新流程同普通注册流程。流程说明参见[普通注册流程](1.html#T_1554257199539__5e19aad1-bd5e-40a7-be9c-2468065dd73d)，其中SMF替换成I-SMF。
##### UE发起的去注册 
I-SMF侧由UE发起的去注册流程同通用的由UE发起的去注册流程。流程说明参见[UE发起的去注册流程](2.html#T_1554257199539__7b01f714-56cb-4aaf-b051-0b05a498d6ae)。其中SMF替换成I-SMF，UPF替换成I-UPF。
##### 网络侧发起的去注册 
I-SMF侧由网络侧发起的去注册流程同通用的由网络侧发起的去注册流程。流程说明参见[网络侧发起的去注册流程](2.html#T_1554257199539__e908b5af-25a6-4cdf-9949-0354a5126255)。其中SMF替换成I-SMF，UPF替换成I-UPF。
#### 连接管理 
##### AN释放 
I-SMF侧的AN释放流程同通用的AN释放流程。流程说明参见AN释放UE上下文
。其中SMF替换成I-SMF，UPF替换成I-UPF。
##### UE触发业务请求 
根据UE触发业务请求过程中，是否存在I-SMF改变，划分如下四种场景： 
终端发起的业务请求触发I-SMF更新 
终端发起的业务请求触发I-SMF插入 
终端发起的业务请求触发I-SMF删除 
终端发起的业务请求触发I-SMF不变（I-UPF变化） 
###### 终端发起的业务请求触发I-SMF更新 
终端发起的业务请求触发I-SMF更新的业务流程如[图1](1600153330289.html#z402bc721892442e28f0dc830d729f77b__b53c9e74-b250-40ef-a23e-9859985f40e0)所示。
图1  终端发起的业务请求触发I-SMF更新
[]images/1603250569169.png)
流程说明如下： 
UE发起业务请求。 

UE向RAN发送Service Request
请求（ 包含Uplink data status、PDU Session status），触发业务请求。

RAN向AMF转发UE的Service Request
请求。
AMF根据UE的位置判断其移出old I-SMF的服务区域，AMF选择new I-SMF。 
AMF向new I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request 请求(包含PDU Session ID, SM Context ID, UE location info, Access Type, RAT Type, Operation Type)。

new I-SMF和old I-SMF交互。 
new I-SMF向old I-SMF发送Nsmf_PDUSession_Context Request请求（包含SM context type）。 
old I-SMF向new I-SMF返回Nsmf_PDUSession_Context Response响应（包含SM context）。 
new I-SMF选择new I-UPF。 

new I-UPF 向new I-UPF发起N4 Session Establishment流程。 
new I-UPF 向new I-UPF发送N4 Session Establishment Request
请求。
new I-UPF 向new I-UPF返回N4 Session Establishment Response
响应。
（可选）假如有下行数据被缓存，则转发隧道。 
new I-SMF向old I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求 (包含tunnel endpoints for buffered DL data)，要求建立转发隧道。
old I-SMF向old I-UPF发起N4 Session Modification Request
请求。
old I-SMF向old I-UPF返回N4 Session Modification Response
响应。
old I-SMF向new I-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
SMF与UPF交互。 
new I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求 (包含new I-UPF DL tunnel information, SM Context ID at I-SMF, Access Type, RAT Type)。
A-SMF向UPF(PSA)发送N4 Session Modification Request
请求（包含the new I-UPF DL tunnel information）。
A-SMF向UPF(PSA)返回N4 Session Modification Response
响应（包含the new I-UPF DL tunnel information）。
A-SMF向new I-SMF返回Nsmf_PDUSession_Update
 Response响应。
new I-SMF向AMF发送Nsmf_PDUSession_CreateSMContext
 Response响应 (包含N2 SM information (PDU Session ID, QFI(s), QoS profile(s), CN N3 Tunnel Info, S-NSSAI, User Plane Security Enforcement, UE Integrity Protection Maximum Data Rate), N1 SM Container, Cause))，同时new I-SMF启用一个定时器用于释放转发隧道。
AMF向RAN发送PDU Session Resource Setup Request
消息。
RAN跟UE交互，进行RRC Connection reconfiguration。 
RAN给AMF返回PDU Session Resource Setup Response
消息。
AMF与old I-SMF交互。 
AMF向old I-SMF发送Nsmf_PDUSession_ReleaseSMContext
 Reques请求，同时old I-SMF启用一个定时器，用于延时释放。
old I-SMF向AMF返回Nsmf_PDUSession_ReleaseSMContext
 Response响应。

AMF 向new I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求 (包含N2 SM information, RAT type, Access type) 。
new I-SMF向new I-UPF发起N4 Session Modification流程。 
new I-SMF向new I-UPF发起N4 Session Modification Request
请求。
new I-UPF向new I-SMF返回N4 Session Modification Response
响应。
new I-SMF与A-SMF交互。 
new I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request 请求（包含RAT type, Access type）。
A-SMF向PCF发起SMF initiated SM Policy Modification。 
A-SMF返回Nsmf_PDUSession_Update
 Response响应。

new I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
（可选）[步骤9](1600153330289.html#z402bc721892442e28f0dc830d729f77b__210a1872-c1da-4907-8f6d-7af1df728bea)定时器超时后，new I-SMF与I-UPF交互。
new I-SMF向I-UPF发送N4 Session Modification Request
，要求删除转发隧道。
new I-UPF向I-SMF返回N4 Session Modification Response
，转发隧道删除响应。
（可选）[步骤13](1600153330289.html#z402bc721892442e28f0dc830d729f77b__2674e679-31e6-41fb-bdb6-a4c0b2868836)中定时器超时后，old I-SMF和old I-UPF交互。
old I-SMF向old I-UPF发送N4 Session Release Request（即 PFCP Session Deletion Request
）消息，old I-SMF和old I-UPF释放PDU会话相关资源。
 说明： 
协议23.502中的N4 Session Release Request/Response消息，对应协议29.244中的PFCP Session Deletion Request/Response消息。 
old I-UPF向old I-SMF返回N4 Session Release Response（即PFCP Session Deletion Response
）消息。
###### 终端发起的业务请求触发I-SMF插入 
终端发起的业务请求触发I-SMF插入流程如[图2](1600153330289.html#z402bc721892442e28f0dc830d729f77b__82f04598-1900-4ff9-a859-da08e6a37e2c)所示。
图2  终端发起的业务请求触发I-SMF插入
[]images/2.1%20%20%E7%BB%88%E7%AB%AF%E5%8F%91%E8%B5%B7%E7%9A%84%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E8%A7%A6%E5%8F%91I-SMF%E6%8F%92%E5%85%A5.png)
流程说明如下： 
UE发起业务请求。 
UE向RAN发送Service Request
请求（包含Uplink data status、PDU Session status），触发业务请求。
RAN向AMF转发UE的Service Request
请求。
AMF根据UE的位置判断其移出SMF的服务区域，AMF选择I-SMF。 
AMF向new I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request 请求(包含PDU Session ID, SM Context ID, UE location info, Access Type, RAT Type, Operation Type)。
new I-SMF和old A-I-SMF交互。 
I-SMF向A-SMF发送Nsmf_PDUSession_Context Request请求 (包含SM context type)。 
A-SMF向I-SMF返回Nsmf_PDUSession_Context Response 响应(包含SM context)。 
I-SMF选择I-UPF。 
I-SMF向I-UPF发起N4 Session Establishment流程。 
I-SMF向I-UPF发送N4 Session Establishment  Request
请求。
I-UPF向I-SMF返回N4 Session Establishment Response
响应。
（可选）假如有下行数据被缓存，则转发隧道。 
new I-SMF向old I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求 (包含tunnel endpoints for buffered DL data)，要求建立转发隧道。
old I-SMF向old I-UPF发起N4 Session Modification Request
请求。
old I-SMF向old I-UPF返回N4 Session Modification Response
响应。
old I-SMF向new I-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
SMF与UPF交互。 
new I-SMF向UPF(PSA)发送Nsmf_PDUSession_Update
 Request 请求(包含new I-UPF DL tunnel information, SM Context ID at I-SMF, Access Type, RAT Type)。
UPF(PSA)向PCF发送N4 Session Modification Request
请求。
PCF向UPF(PSA)返回N4 Session Modification Response
响应。
A-SMF向new I-SMF返回Nsmf_PDUSession_Update
 Response响应。

I-SMF向AMF发送Nsmf_PDUSession_CreateSMContext
 Response 响应(包含N2 SM information (PDU Session ID, QFI(s), QoS profile(s), CN N3 Tunnel Info, S-NSSAI, User Plane Security Enforcement, UE Integrity Protection Maximum Data Rate), N1 SM Container, Cause))，同时new I-SMF启用一个定时器用于释放转发隧道。
AMF向RAN发送PDU Session Resource Setup Request
消息。
RAN跟UE交互，进行RRC Connection reconfiguration。 
RAN给AMF返回PDU Session Resource Setup Response
消息。
AMF 向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求 (包含N2 SM information, RAT type, Access type) 。
I-SMF向I-UPF发起N4 Session Modification流程。 
I-SMF向I-UPF发送N4 Session Modification Request
请求。
I-UPF向I-SMF返回N4 Session Modification Response
响应。
I-SMF向I-UPF发起N4 Session Modification流程。 
I-SMF向I-UPF发送N4 Session Modification Request
请求。
I-UPF向I-SMF返回N4 Session Modification Response
响应。
I-SMF与A-SMF交互。 
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求 (包含RAT type, Access type)。
A-SMF向PCF发送SMF initiated SM Policy Modification。 
A-SMF返回Nsmf_PDUSession_Update
 Respons响应。

I-SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response响应。
（可选）[步骤9](1600153330289.html#z402bc721892442e28f0dc830d729f77b__11348994-1007-4fb4-ba83-3e0953ddbb32)中定时器超时后，old I-SMF和old I-UPF交互。
old I-SMF向old I-UPF发送N4 Session Release Request（即PFCP Session Deletion Request
）消息，old I-SMF和old I-UPF释放PDU会话相关资源。
old I-UPF向old I-SMF返回N4 Session Release Response（即PFCP Session Deletion Response
）消息。
###### 终端发起的业务请求触发I-SMF删除 
终端发起的业务请求触发I-SMF删除流程如[图3](1600153330289.html#z402bc721892442e28f0dc830d729f77b__ad5924cd-442b-4a9f-815a-a549258f50c5)所示。
图3  终端发起的业务请求触发I-SMF删除
[]images/3%E7%BB%88%E7%AB%AF%E5%8F%91%E8%B5%B7%E7%9A%84%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E8%A7%A6%E5%8F%91I-SMF%E5%88%A0%E9%99%A4.png)
流程说明如下： 
UE发起业务请求。 
UE向RAN发送Service Request
请求（包含Uplink data status、PDU Session status），触发业务请求。
RAN向AMF转发UE的Service Request
请求。
AMF根据UE的位置判断其移出SMF的服务区域，AMF选择I-SMF。 
AMF向SMF发送Nsmf_PDUSession_CreateSMContext
 Request 请求(包含PDU Session ID, SM Context ID, UE location info, Access Type, RAT Type, Operation Type)。
SMF和I-SMF交互。 
SMF向I-SMF发送Nsmf_PDUSession_Context Request请求 (包含SM context type)。 
I-SMF向SMF返回Nsmf_PDUSession_Context Response 响应(包含SM context)。 
SMF选择new I-UPF。 
（可选）SMF向new I-UPF发起N4 Session Establishment流程。 
（可选）假如有下行数据被缓存，则转发隧道。 
SMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request 请求。
I-SMF向old I-UPF发送N4 Session Modification Request
请求。
old I-UPF向I-SMF返回N4 Session Modification Response
响应。
I-SMF向SMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
SMF向UPF(PSA)发起N4 Session Modification流程。 
SMF向UPF发送N4 Session Modification Request
请求。
UPF向SMF返回N4 Session Modification Response
响应。
SMF向AMF发送Nsmf_PDUSession_CreateSMContext
 Response响应 (包含N2 SM information (PDU Session ID, QFI(s), QoS profile(s), CN N3 Tunnel Info, S-NSSAI), N1 SM Container, Cause))。同时I-SMF启用一个定时器。
AMF向RAN发送PDU Session Resource Setup Request
消息。
RAN跟UE交互，进行RRC Connection reconfiguration。 
RAN给AMF返回PDU Session Resource Setup Response
消息。
AMF与I-SMF交互。 

AMF向I-SMF发送Nsmf_PDUSession_ReleaseSMContext
 Request 请求，同时I-SMF启用一个定时器。
I-SMF向AMF返回Nsmf_PDUSession_ReleaseSMContext
 Response响应。
AMF 向SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求(包含N2 SM information, RAT type, Access type) 。
SMF向PCF发起SM策略更新请求。 
SMF向I-UPF发起N4 Session Modification流程。 
SMF向I-UPF发送N4 Session Modification Request
请求。
I-UPF向SMF返回N4 Session Modification Response
响应。
SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
（可选）定时器超时。 
[步骤9](1600153330289.html#z402bc721892442e28f0dc830d729f77b__3ee8d172-07b6-43cb-a70f-43249193c72e)定时器超时后，SMF向new I-UPF发送N4 Session Modification Request
，请求删除转发隧道。
old I-UPF向SMF返回N4 Session Modification Response
。
[步骤10](1600153330289.html#z402bc721892442e28f0dc830d729f77b__839ca32e-764d-4d6c-8209-adb5644f4a2d)中定时器超时后，I-SMF向old I-UPF发送N4 Session Release Request（即PFCP Session Deletion Request
）消息，I-SMF和I-UPF释放PDU会话相关资源。
old I-UPF向I-SMF返回N4 Session Release Response（即PFCP Session Deletion Response
）消息。
###### 终端发起的业务请求触发I-SMF不变（I-UPF变化） 
终端发起的业务请求触发I-SMF不变（I-UPF变化）的流程如[图4](1600153330289.html#z402bc721892442e28f0dc830d729f77b__1b0f836f-2953-40db-b06c-17afd1498949)所示。
图4  终端发起的业务请求触发I-SMF不变（I-UPF变化）
[]images/4%E7%BB%88%E7%AB%AF%E5%8F%91%E8%B5%B7%E7%9A%84%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E8%A7%A6%E5%8F%91I-SMF%E4%B8%8D%E5%8F%98%EF%BC%88I-UPF%E5%8F%98%E5%8C%96%EF%BC%89.png)
流程说明如下： 
UE向RAN发送Service Request
请求，其中携带要激活的PDU会话列表、允许的PDU会话列表、PDU会话状态等信息。
RAN将Service Request
消息经N2接口转发给AMF。
（可选）AMF选择I-SMF。当AMF决策I-SMF不变时，无I-SMF选择过程。 
（可选）如果UE在Service Request
消息中指示了要激活的PDU会话列表， 则AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
请求消息，其中包含PDU会话ID、操作类型，UE位置信息、RAT等信息，其中操作类型（Operation Type）设置为“UP activate”，以指示PDU会话的用户面建立。
根据从AMF收到的位置信息，SMF确定继续使用当前的UPF还是选择新的I-UPF。 
I-SMF向new I-UPF发起N4 Session Establishment流程。 
I-SMF向new I-UPF发送N4 Session Establishment Request
请求。
new I-UPF向I-SMF返回N4 Session Establishment Response
响应。
A-SMF将从I-SMF接收到的新的I-UPF的DL隧道信息提供给UPF。 
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求。
A-SMF向A-UPF发起N4 Session Modification Request
请求。
A-UPF向A-SMF返回N4 Session Modification Response
响应。
A-SMF向I-SMF返回Nsmf_PDUSession_Update
 Response响应。
（可选）如果SMF移除old I-UPF，则转发隧道。 
SMF向old I-UPF发送N4 Session Modification Request
消息，为缓冲的DL数据提供DL隧道信息。
old I-UPF返回N4 Session Modification Response
消息。
（可选）如果I-UPF被改变，old I-UPF向new I-UPF进行缓冲下行数据转发。 
（可选）SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
响应消息，其中包含N2 SM信息，PDU会话ID，QFI，QoS配置，CN N3隧道信息，S-NSSAI，MBR等信息。
AMF向RAN转发从SMF接收的PDU Session Resource Setup Request
信息，其中包含切换限制列表，签约UE-AMBR，MM NAS服务接受、UE radio capability等信息。
RAN根据被激活PDU会话的QoS流的QoS信息和DRB，与UE执行RRC连接重配置。 
RAN向AMF返回PDU Session Resource Setup Response
消息，其中包含N2 SM信息及AN隧道信息等内容。
接收到N2 SM信息后，AMF向I-SMF发出Nsmf_PDUSession_UpdateSMContext
请求消息，其中携带N2 SM信息。
（可选）A-SMF从I-SMF获取UE位置信息。如果部署了动态PCC，则SMF可以将UE位置信息通知给PCF，并获取更新后的策略。 
（可选）如果[步骤5](1600153330289.html#z402bc721892442e28f0dc830d729f77b__f03b89f4-b871-4afa-95c5-b2b0bd8925bd)中选择了新的I-UPF，则执行以下流程。
SMF向new I-UPF发送N4 Session Modification Request
消息，以更新AN隧道信息和接受的QFI列表。
UPF返回N4 Session Modification Response
消息。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
响应消息。
（可选）如果已经为新的I-UPF建立了转发隧道，且I-SMF在步骤8a中用于转发隧道的定时器已到期，则执行以下流程。 
I-SMF向new I-UPF发送N4 Session Modification Request
消息以释放转发隧道。
new I-UPF返回N4 Session Modification Response
消息。
（可选）如果[步骤5](1600153330289.html#z402bc721892442e28f0dc830d729f77b__f03b89f4-b871-4afa-95c5-b2b0bd8925bd)中选择了继续使用旧的I-UPF，则执行以下流程。
I-SMF向old I-UPF发送N4 Session Release Request（即PFCP Session Deletion Request
）消息。
old I-UPF返回N4 Session Release Response（即PFCP Session Deletion Response
）消息。
##### 网络侧触发业务请求 
网络发起的业务请求流程如[图1](1600153370282.html#z42da4bb63d4a4dec8193a30e774755c1__c4691b7f-a364-4f20-b07e-bf1342906b3d)所示。
图1  网络发起的业务请求（带I-SMF）
[]images/1603960642581.png)
流程说明如下： 
UE向I-UPF发送PDU会话的下行数据。 
I-UPF与I-SMF交互。 
I-UPF向I-SMF发出PFCP Session Report Request
（Data Notification）消息，其中携带N4会话ID、用于标识DL数据包的QoS流的信息，DSCP等内容。
I-SMF返回PFCP Session Report Response
（Data Notification Ack）消息。
当UPF接收PDU会话的下行数据并且UPF中没有存储该PDU会话的AN隧道信息时，UPF可以基于SMF指令决定缓冲下行数据，或者将下行数据转发到SMF。 
（可选）I-SMF与AMF交互。 
接收到数据通知消息后，SMF确定是否需联系AMF，如果是，则SMF向AMF调用Namf_Communication_N1N2MessageTransfer
消息，其中携带SUPI、PDU会话ID、N2 SM信息（可选，包括QFI，QoS profile，CN N3隧道信息，S-NSSAI等）等内容。
AMF向I-SMF返回响应。 
如果UE在AMF处于CM-IDLE状态，并且AMF能够寻呼UE，则AMF立即向SMF发送Namf_Communication_N1N2MessageTransfer响应消息，其原因是“Attempting to reach UE”，其指示AMF可以忽略SMF发来的N2 SM信息，一旦UE可达，可以要求SMF再次提供N2 SM信息。 
如果UE在AMF处于CM-CONNECTED状态，则AMF立即向SMF发送Namf_Communication_N1N2MessageTransfer响应消息，其原因是N1/N2 transfer success。 
SMF通知UPF用户面恢复失败。如果SMF从AMF接收到UE不可及或仅可用于监管优先服务的指示，则SMF可以基于本地策略进行下列操作。如果SMF从AMF接收到从SMF请求的Namf_Communication_N1N2MessageTransfer
消息包含临时拒绝的指示，则SMF可以基于本地策略向UPF指示临时缓冲数据。
指示UPF停止发送Data Notification。 
指示UPF停止缓冲下行数据并丢弃缓冲数据。 
以上两种指示组合。 
当UE不可及时，不再向AMF发送进一步Namf_Communication_N1N2MessageTransfer消息。 
（可选）根据UE的不同状态，分别执行不同的操作。 
如果UE处于CM-CONNECTED状态，则执行UE发起的业务区请求流程中的步骤10至19（参见“UE触发业务请求
”流程），以激活该PDU会话的用户面连接（即建立无线资源和N3隧道），而不向RAN节点和UE发送寻呼消息。
如果UE处于CM-IDLE状态且PDU会话与3GPP接入关联，则AMF向RAN节点发送寻呼消息。 
如果UE在同一PLMN中通过3GPP和非3GPP接入同时注册，并且UE在一侧接入中处于CM-CONNECTED状态并且步骤3a中的PDU会话与另一侧接入相关联，则AMF基于本地策略可通过连接态的接入向UE发送包含另一侧接入类型的NAS通知消息。跳过步骤5。 
（可选）如果AMF没有从收到UE返回的寻呼响应消息，则AMF可以基于寻呼策略来发起进一步寻呼。如果UE不响应寻呼，则AMF通过在步骤3a中向SMF提供的通知目标地址发送Namf_Communication_N1N2TransferFailureNotification
来通知SMF。
（可选）如果处于CM-IDLE状态的UE接收到针对PDU会话的寻呼请求时，UE将触发业务请求流程以建立对应PDU会话的用户面连接。具体流程可参见“UE触发业务请求
”流程。
UPF通过在业务请求流程中建立的N3隧道向UE发送缓冲的下行数据。 
#### 会话管理 
##### PDU会话建立 
UE发起的带I-SMF的会话建立流程如[图1](1600153608623.html#z3dfba7a1890a4d22a005747935fb3732__fcc5bcaf-7732-4ddf-ae37-9506a6548c45)所示。
图1  UE发起的带I-SMF的会话建立流程
[]images/1603962019252.png)
流程说明如下： 
UE向AMF发送PDU Session Establishment Request
（NAS）消息，消息中包含：S-NSSAI(s)、DNN、PDU Session ID、Request type、Old PDU Session ID、SM container等信息。
AMF接收到UE的会话建立消息，发现是创建新PDU会话时，执行SMF选择流程为该PDU会话选择SMF。在AMF选择SMF的过程中，AMF会与NSSF交互获取网络切片信息，再通过NRF发现SMF。AMF发现需要插入I-SMF，通过NRF再次查询I-SMF信息。 
AMF向I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息，消息中包括：SUPI、DNN、S-NSSAI、PDU Session ID、AMF ID、Request Type、hplmnSnssai、SmfUri、additionalsmfUri、N1 SM container、User location information、Access Type、PEI、GPS、Subscription For PDU Session Status Notification等信息。
I-SMF收到AMF的会话创建请求消息后，判断是新建PDU会话，并且本地可以执行，则向AMF返回Nsmf_PDUSession_CreateSMContext
 Response消息，消息中包含：Cause，SM Context ID or N1 SM container等信息。Nsmf_PDUSession_CreateSMContext Response消息中携带supportedFeatures指示支持DTSSA（I-SMF）功能。此时尚未与A-SMF交互，无QoS Flow信息，响应消息中不携带N1N2参数。
I-SMF根据UE位置和S-NSSAI等信息选择I-UPF。 
I-SMF向I-UPF发起N4会话建立流程，向I-UPF发送N4 Session Establishment Request
消息，请求分配I-UPF左侧N3端点和右侧N9端点。此时建立N4会话，可以避免PDU会话建立过程中I-UPF收到上下行数据时返回错误提示。如果会话建立失败，则直接执行[第21步](1600153608623.html#z3dfba7a1890a4d22a005747935fb3732__ba350d9c-4378-46c1-b353-fe0c384dbcbb)。
I-SMF向A-SMF发送Nsmf_PDUSession_Create
 Request消息，消息中携带SUPI、DNN、S-NSSAI、PDU Session ID、Request Type、pgwS8cFteid、ismfId、ismfPduSessionUri、cnTunnelInfo、n1SmInfoFromUe、unknownN1SmInfo、iSmfServiceInstanceId、roamingChargingProfilechargingIdUser location information、Access Type、PEI、GPSI、Subscription For PDU Session Status Notification等信息。
（可选）如果A-SMF没有获取过签约信息，A-SMF与UDM交互，在UDM上完成会话注册并获取会话签约数据。 
（可选）如果A-SMF需要在DN-AAA服务器建立PDU会话期间执行二次身份验证/授权，则会触发PDU会话建立身份验证/授权。 
（可选）如果A-SMF配置了PCF，则A-SMF需要与PCF交互获取控制策略。 
A-SMF执行PCF的选择过程，通过NRF获取A-PCF。 
A-SMF与A-PCF交互获取默认PCC控制策略，包括AMBR、5QI、ARP等信息。 
A-SMF的会话创建流程执行以下操作：选择UPF，为UE分配IPv4地址，获取本地计费、控制策略。 
A-SMF与A-PCF再次交互，通知A-PCF已分配的用户地址，A-PCF将更新的PCC控制策略信息通知SMF。 
A-SMF与A-UPF、UDM交互。 
A-SMF向A-UPF发送N4 Session Establishment Request
消息，将计费策略、控制策略带给A-UPF。A-UPF建立隧道信息，并通过N4 Session Establishment Response
消息将隧道信息带给A-SMF。
（可选）A-SMF向UDM注册。 
A-SMF向I-SMF发送Nsmf_PDUSession_Create
 Response消息，该消息将A-SMF获得的用户地址、隧道信息、控制策略等信息通过I-SMF带给UE与(R)AN。消息中主要包括：PDU Session ID、Access Type、N2 SM information、N1 SM container等信息。
I-SMF向AMF发送Namf_Communication_N1N2MessageTransfer
消息，该消息将I-SMF获得的用户地址、隧道信息、控制策略等信息通过AMF带给UE与(R)AN。消息中主要包括：PDU Session ID、Access Type、N2 SM information、N1 SM container等信息。AMF收到消息后返回确认消息。
AMF向(R)AN发送N2 PDU Session Request消息，将I-SMF获得的用户地址、隧道信息、控制策略等信息转发给(R)AN，同时在(R)AN上建立N3隧道。 
(R)AN与UE交互，返回PDU会话建立接受消息，携带QoS Rule(s)、selected SSC mode、S-NSSAI、allocated IPv4 address、interface identifier、Session-AMBR、selected PDU Session Type等信息。 
(R)AN向AMF返回N2 PDU Session Request Ack消息，将N3隧道信息发给AMF。 
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，将(R)AN建立的N3隧道信息带给I-SMF。消息中主要包括：N2 SM information (PDU Session ID, AN Tunnel Info, List of accepted/rejected QFI(s))，Request Type等信息。
I-SMF与I-UPF交互，将AMF携带的(R)AN上建立的N3隧道信息以及N9接口A-UPF的隧道等信息带给I-UPF。 
I-SMF向AMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）I-SMF向AMF发送Nsmf_PDUSession_NotifySMContextStatus
消息，通知AMF会话建立失败，释放相关资源。
（可选）对于IPv6类型的会话，A-SMF指示A-UPF向UE发送IPv6 Router Advertisement报文。 
（可选）如果I-SMF在步骤18中接收的消息表明(R)AN已拒绝一些QFI，则I-SMF通过Nsmf_PDUSession_Update
请求通知A-SMF，A-SMF负责相应地更新UE相关的QoS规则和QoS Flow级别QoS参数，该流程同(R)AN发起的更新。
（可选）A-SMF与UDM交互，发送Nudm_UEContextManagement_Deregistration
消息（携带SUPI，DNN，PDU会话ID）注销指定的PDU会话。
##### PDU会话修改 
###### UE发起的PDU会话修改 
UE发起的带I-SMF的会话修改流程如[图1](1600153625204.html#z6e820de48d294e3d82d247106043fa2e__fc0feb09-a818-4040-a01f-6c50c7d3cf54)所示。
图1  UE发起的带I-SMF的会话修改
[]images/1603964291522.png)
流程说明如下： 
UE发起会话修改。 
UE向AMF发送PDU会话修改请求PDU Session Modification Request
。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带smfUri信元，I-SMF根据该信元判断自身角色为I-SMF。
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request消息，其中包含SM Context ID、UE请求PDU会话修改或来自VPLMN的QoS修改请求等信息，通知A-SMF修改PDU会话，A-SMF收到消息后返回响应。
A-SMF发起SM策略关联更新流程Npcf_SMPolicyControl_Update
，向PCF报告某些已订阅事件，如：用户位置变化。
A-SMF向I-SMF发送Nsmf_PDUSession_Update
 Request消息，包含SM上下文ID、QoS文件等。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
响应，携带N2 SM信息。
（可选）AMF将N2 SM信息通过PDU Session Resource Modify Request
消息发送给(R)AN，将NAS消息通过(R)AN带给UE，(R)AN与UE交互并向AMF返回响应PDU Session Resource Modify Response
。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，将N2 SM信息和用户位置信息转发给I-SMF，I-SMF向AMF返回响应。
（可选）UE返回会话修改完成消息PDU Session Modification Complete
。
（可选）(R)AN将Uplink NAS Transport
消息转发到AMF。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带UE接受PDU会话变更的响应，I-SMF向AMF返回响应。
I-SMF向I-UPF发起N4会话修改流程（Session Modification Request
/Session Modification Response
），更新PDU会话修改所涉及的I-UPF N4会话，修改QoS相关参数。
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Response消息，该响应消息中携带UE向I-SMF发送的PDU会话修改命令Ack消息。
（可选）A-SMF通知A-UPF修改N4会话流程（Session Modification Request
/Session Modification Response
）。
（可选）A-SMF通知PCF PCC策略执行结果（Npcf_SMPolicyControl_Update
）。
###### 网络侧发起的PDU会话修改 
根据发起PDU会话修改的NF不同，划分如下三种场景： 
PCF发起的带I-SMF的会话修改 
UDM发起的带I-SMF的会话修改 
NR发起的带I-SMF的会话修改 
####### PCF发起的带I-SMF的会话修改 
图1  PCF发起的带I-SMF的会话修改
[]images/2.%20PCF%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E6%9B%B4%E6%96%B0.png)
流程说明如下： 
A-SMF收到PCF的Npcf_SMPolicyControl_UpdateNotify
消息，需要新建或更新QoS Flow。
（可选）如果A-SMF判断需要发起EBI分配流程，则执行EBI分配流程。 

A-SMF向I-SMF发送Nsmf_PDUSession_Update
 Request消息。
I-SMF向AMF发送Namf_Communication_N1N2MessageTransfer
 Request消息，携带N1和N2消息，AMF返回响应。
（可选）AMF将N2 SM消息（PDU Session Resource Modify Request
）发送给(R)AN，将NAS消息通过(R)AN带给UE，(R)AN与UE交互并向AMF返回响应（PDU Session Resource Modify Response
）。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带N2 SM信息和用户位置信息，I-SMF返回响应。

（可选）UE返回会话修改完成响应。 
（可选）(R)AN将Uplink NAS Transport
消息转发到AMF。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带UE接受PDU会话变更的响应，I-SMF返回响应。
I-SMF向I-UPF发送N4会话修改请求（Session Modification Request
/Session Modification Response
），通知I-UPF更新New QoS Flow的上行PDR和下行PDR。

I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Response消息，该响应消息中携带UE向I-SMF发送的PDU会话修改命令Ack消息。
（可选） A-SMF通知A-UPF修改N4会话流程（Session Modification Request
/Session Modification Response
）。
（可选）A-SMF向PCF发送Session Management Policy Modification消息（即Npcf_SMPolicyControl_Update
 ），通知会话修改结果。
####### UDM发起的带I-SMF的会话修改 
图2  UDM发起的带I-SMF的会话修改
[]images/3.%20UDM%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E6%9B%B4%E6%96%B0.png)
流程说明如下： 
UDM向A-SMF发Nudm_SubscriberDataManagement_Notification
消息，携带SUPI和会话管理订阅数据。A-SMF更新会话管理订阅数据后向UDM返回Nudm_SubscriberDataManagement_Notification
 Ack消息，携带SUPI。
A-SMF向PCF上报PCF订阅的事件（Npcf_SMPolicyControl_Update
 ），A-SMF可以根据本地策略决定是否修改QoS Profile。
A-SMF向I-SMF发送Nsmf_PDUSession_Update
 Request消息，携带SM Context ID，QoS Profile，Session-AMBR，QoS规则和QoS Flow级别QoS参数。
（可选）如果有新的QosFlow需要创建，A-SMF给向A-UPF发起N4会话修改请求（Session Modification Request
/Session Modification Response
），提供上行PDR。
I-SMF向AMF发送Namf_Communication_N1N2MessageTransfer
消息，携带N2消息或同时携带N1、N2消息。
N2消息PDU Session Resource Modify Request Transfer携带参数：PDU Session ID, QFI(s), QoS Profile(s), Alternative QoS Profile(s), Session-AMBR等。  
N1消息PDU Session Modification Command携带参数：PDU Session ID，Qos Flow level Qos parameters，Session-AMBR等。 
（可选）AMF将N2 SM消息（PDU Session Resource Modify Request
）发送给(R)AN，将NAS消息通过(R)AN带给UE，(R)AN与UE交互并向AMF返回响应（PDU Session Resource Modify Response
）。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，将N2 SM信息和用户位置信息转发给I-SMF，I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）UE返回会话修改完成消息PDU Session Modification Command
 Ack。
（可选）(R)AN将Uplink NAS Transport
消息转发到AMF。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带UE接受PDU会话变更的响应，I-SMF向AMF返回响应。
I-SMF通过向I-UPF发送N4会话修改请求消息（Session Modification Request
/Session Modification Response
），通知I-UPF更新New QoS Flow的上行PDR和下行PDR。
I-SMF向A-SMF返回[Nsmf_PDUSession_Update](../../Nsmf\topics\9.html) Response消息，该响应消息中携带UE向I-SMF发送的PDU会话修改命令Ack消息。
（可选）如果(R)AN带了新的参数，A-SMF通知A-UPF修改N4会话流程（Session Modification Request
/Session Modification Response
）。
（可选）A-SMF向PCF发送SMF initiated SM Policy Association Modification消息（即Npcf_SMPolicyControl_Update
 ），通知会话修改结果。
####### NR发起的带I-SMF的会话修改 
图3  NR发起的带I-SMF的会话修改
[]images/4.%20NR%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E6%9B%B4%E6%96%B0.png)
步骤说明如下： 
(R)AN发起会话修改流程。 
(R)AN向AMF发送会话修改请求（PDU Session Resource Modify Indication
）。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带smfUri信元，I-SMF根据该信元判断自身角色为I-SMF。
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request消息，携带UE请求PDU会话修改或来自VPLMN的QoS修改请求等信息，A-SMF收到消息后返回响应。
A-SMF向PCF上报PCF订阅的事件Npcf_SMPolicyControl_Update
，A-SMF可以根据本地策略决定是否改变QoS Profile。
A-SMF向I-SMF发送Nsmf_PDUSession_Update
 Request消息，携带SM Context ID，QoS Profile，Session-AMBR，QoS规则和QoS Flow级别QoS参数。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
（可选）AMF将N2 SM消息（PDU Session Resource Modify Request
）发送给(R)AN，将NAS消息通过(R)AN带给UE，(R)AN与UE交互并向AMF返回响应（PDU Session Resource Modify Response
）。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，将N2 SM信息和用户位置信息转发给I-SMF。
I-SMF向I-UPF发送N4会话修改请求消息（Session Modification Request
/Session Modification Response
），通知I-UPF更新New QoS Flow的上行PDR和下行PDR。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response消息。
（可选）UE返回会话修改完成消息。 
（可选）(R)AN将Uplink NAS Transport
消息转发到AMF。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息，携带UE接受PDU会话变更的响应，I-SMF向AMF返回响应。
I-SMF向A-SMF返回Nsmf_PDUSession_Update
 Response消息，该响应消息中携带UE向I-SMF发送的PDU会话修改命令Ack消息。
（可选）A-SMF通知A-UPF修改N4会话流程（Session Modification Request
/Session Modification Response
）。
（可选）A-SMF向PCF发送Npcf_SMPolicyControl_Update
 Request消息，通知会话修改结果。
##### PDU会话释放 
###### UE发起的PDU会话释放 
UE发起的PDU会话释放流程如[图1](1600153671745.html#z56567e633a234f528c4d7aafbd2c4eea__9b39dfc2-fbfd-4ca2-8519-e2f71e41c5f3)所示。
图1  AMF通过UpdateSMContext通知释放
[]images/1603960971086.png)
流程说明如下： 
I-SMF发起请求。 
I-SMF收到AMF发起Nsmf_PDUSession_UpdateSMContext
服务操作，其中携带的release IE为true，并携带cause IE。
（可选）I-SMF向A-MF发起Nsmf_PDUSession_Update
 Request请求，其中判断如果AMF携带的Release IE为true，则RequestIndication设置为"NW_REQ_PDU_SES_REL"，透传AMF携带的cause IE。
（可选）A-SMF向I-SMF返回Nsmf_PDUSession_Update
 Response响应。
N4会话释放。 
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF向I-SMF发起Nsmf_PDUSession_Update
 Request请求，其中requestIndication设置为NW_REQ_PDU_SES_REL，如果I-SMF收到的cause为REL_DUE_TO_REACTIVATION，则n1smCause指示重复激活（Reactivation requested）。
N4会话释放。 
I-SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应，其中携带N1 SM container (PDU Session Release Command
)通知UE释放会话，如果该会话的UP连接存在，则携带N2 PDU Session Resource Release Command
 (PDU Session ID) 通知(R)AN释放会话。如果AMF携带的cause IE是REL_DUE_TO_DUPLICATE_SESSION_ID，则不需携带N1 SM container。
AMF向RAN发起会话释放请求PDU Session Resource Release Command
。
RAN与UE交互，发送AN-Specific Resource Modification。 
RAN向AMF返回会话释放响应PDU Session Resource Release Response
。
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request(包含N2 SM Resource Release Ack , User Location Information)。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
UE释放会话流程。 
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request(包含N1 SM container (PDU Session Release Ack, User Location Information)。
I-SMF向AMF返回[Nsmf_PDUSession_UpdateSMContext](../../Nsmf\topics\4.html) Response响应。
I-SMF向A-SMF返回Nsmf_PDUSession_Update
 Response响应，携带释放结果。
A-SMF启动SM策略关联终止过程来释放与PCF的SM策略控制关联。 
A-SMF向PCF发送SM策略关联终止请求Npcf_SMPolicyControl_Delete
 Request。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起去订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF释放会话相关资源，并向I-SMF发送Nsmf_PDUSession_NotifyStatus
 (Release) 。
I-SMF释放会话相关资源，向AMF发起Nsmf_PDUSession_NotifySMContextStatus
 (Release)。
###### 网络侧发起的PDU会话释放 
根据发起PDU会话释放的NF不同，划分如下六种场景： 
AMF通过ReleaseSMContext 通知释放 
SMF发起的带I-SMF的会话释放 
I-SMF主动发起的会话释放 
PCF发起的带I-SMF的会话释放 
UDM发起的带I-SMF的会话释放 
RAN发起的带I-SMF的会话释放 
####### AMF通过ReleaseSMContext 通知释放 
图1  AMF通过ReleaseSMContext 通知释放
[]images/1.2%20AMF%E9%80%9A%E8%BF%87ReleaseSMContext%20%E9%80%9A%E7%9F%A5%E9%87%8A%E6%94%BE.png)
流程说明如下： 
（可选）AMF在UE或网络发起的去注册过程中发起PDU会话释放。在这种情况下，UE和I-SMF之间没有NAS消息，I-SMF收到AMF发起的Nsmf_PDUSession_ReleaseSMContext
服务操作。
I-SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
I-SMF向A-SMF发送Nsmf_PDUSession_Release
 Request请求，请求A-SMF释放PDU会话。
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF启动SM策略关联终止过程Npcf_SMPolicyControl_Delete
来释放与PCF的SM策略控制关联。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF向I-SMF返回Nsmf_PDUSession_Release
 Response响应。
（可选）I-SMF向AMF返回Nsmf_PDUSession_ReleaseSMContext
 Response响应，并清除本地资源。
####### SMF发起的带I-SMF的会话释放 
图2  SMF发起的带I-SMF的会话释放
[]images/2.%20SMF%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE.png)
流程说明如下： 
由于动态命令或本地策略，A-SMF决定需要释放会话。 
N4会话释放。 
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF向I-SMF发起Nsmf_PDUSession_Update
 Request请求，其中requestIndication设置为NW_REQ_PDU_SES_REL。
N4会话释放。 
I-SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
（可选）AMF与I-SMF交互。 
I-SMF调用AMF的Namf_Communication_N1N2MessageTransfer
服务，其中携带N1 SM container (PDU Session Release Command
)通知UE释放会话，如果该会话的UP连接存在，则携带N2 PDU Session Resource Release Command
 (PDU Session ID) 通知(R)AN释放会话。
AMF向I-SMF返回响应。 
AMF向RAN发起会话释放请求（即PDU Session Resource Release Command
）。
RAN与UE交互，发送AN-Specific Resource Modification消息。 
RAN向AMF返回会话释放响应（即PDU Session Resource Release Response
）。
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
UE返回会话释放确认给RAN，RAN携带给AMF。 
AMF向I-SMF发起[Nsmf_PDUSession_UpdateSMContext](../../Nsmf\topics\4.html) Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Response消息，携带释放结果。
A-SMF启动SM策略关联终止过程Npcf_SMPolicyControl_Delete
来释放与PCF的SM策略控制关联。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF向I-SMF返回Nsmf_PDUSession_NotifyStatus
 (Release)。
I-SMF释放会话相关资源，向AMF发起Nsmf_PDUSession_NotifySMContextStatus
 (Release)。
####### I-SMF主动发起的会话释放 
图3  I-SMF主动发起的会话释放
[]images/3%E3%80%81%20I-SMF%E4%B8%BB%E5%8A%A8%E5%8F%91%E8%B5%B7%E7%9A%84%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE.png)
流程说明如下： 
I-UPF检测idle态的会话有效性到期或收到A-UPF的error ind指示，上报给I-SMF。 
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求。
A-SMF向I-SMF返回Nsmf_PDUSession_Update
 Response响应。
N4会话释放。 
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF向I-SMF发起Nsmf_PDUSession_Update
 Request请求，其中requestIndication设置为NW_REQ_PDU_SES_REL。
N4会话释放。 
I-SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
（可选）AMF与I-SMF交互。 
I-SMF调用AMF的Namf_Communication_N1N2MessageTransfer
服务，其中携带N1 SM container (PDU Session Release Command
)通知UE释放会话，如果该会话的UP连接存在，则携带N2 PDU Session Resource Release Command
 (PDU Session ID) 通知(R)AN释放会话。
AMF向I-SMF返回响应。 
AMF向RAN发起会话释放请求（即PDU Session Resource Release Command
）。
RAN与UE交互，发送AN-Specific Resource Modification。 
RAN向AMF返回会话释放响应（即PDU Session Resource Release Response
）。
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回[Nsmf_PDUSession_UpdateSMContext](../../Nsmf\topics\4.html) Response响应。
UE返回会话释放确认给RAN，RAN携带给AMF。 
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
I-SMF向A-SMF发起Nsmf_PDUSession_Update
 Response，携带释放结果。
A-SMF启动SM策略关联终止过程Npcf_SMPolicyControl_Delete
来释放与PCF的SM策略控制关联。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF向I-SMF返回Nsmf_PDUSession_NotifyStatus
 (Release)。
I-SMF释放会话相关资源，向AMF发起Nsmf_PDUSession_NotifySMContextStatus
 (Release)。
####### PCF发起的带I-SMF的会话释放 
图4  PCF发起的带I-SMF的会话释放
[]images/4%E3%80%81PCF%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE.png)
流程说明如下： 
PCF向A-SMF下发会话释放指示。 
PCF向A-SMF发送Npcf_SMPolicyControl_UpdateNotify
 Request请求。
A-SMF向I-SMF返回Nsmf_PDUSession_Update
 Response响应。
N4会话释放。 
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF向I-SMF发起Nsmf_PDUSession_Update
 Request请求，其中requestIndication设置为NW_REQ_PDU_SES_REL。
N4会话释放。 
I-SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
（可选）AMF与I-SMF交互。 
I-SMF调用AMF的Namf_Communication_N1N2MessageTransfer
服务，其中携带N1 SM container (PDU Session Release Command
)通知UE释放会话，如果该会话的UP连接存在，则携带N2 PDU Session Resource Release Command
 (PDU Session ID) 通知(R)AN释放会话。
AMF向I-SMF返回响应。 
AMF向RAN发起会话释放请求（即PDU Session Resource Release Command
）。
RAN与UE交互，发送AN-Specific Resource Modification。 
RAN向AMF返回会话释放响应（即PDU Session Resource Release Response
）。
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
UE返回会话释放确认给RAN，RAN携带给AMF。 
AMF向I-SMF发起[Nsmf_PDUSession_UpdateSMContext](../../Nsmf\topics\4.html) Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
I-SMF向A-SMF发起Nsmf_PDUSession_Update
 Response，携带释放结果。
A-SMF启动SM策略关联终止过程Npcf_SMPolicyControl_Delete
来释放与PCF的SM策略控制关联。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF向I-SMF返回Nsmf_PDUSession_NotifyStatus
 (Release)。
I-SMF释放会话相关资源，向AMF发起Nsmf_PDUSession_NotifySMContextStatus
 (Release)。
####### UDM发起的带I-SMF的会话释放 
图5  UDM发起的带I-SMF的会话释放
[]images/5%E3%80%81UDM%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE.png)
流程说明如下： 
A-SMF收到UDM的签约数据变化通知Nudm_SubscriberDataManagement_Notification
。
N4会话释放。 
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF向I-SMF发起Nsmf_PDUSession_Update
 Request请求，其中requestIndication设置为NW_REQ_PDU_SES_REL。
N4会话释放。 
I--SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
（可选）AMF与I-SMF交互。 
I-SMF调用AMF的Namf_Communication_N1N2MessageTransfer
服务，其中携带N1 SM container (PDU Session Release Command
)通知UE释放会话，如果该会话的UP连接存在，则携带N2 PDU Session Resource Release Command
 (PDU Session ID) 通知(R)AN释放会话。
AMF向I-SMF返回响应。 
AMF向RAN发起会话释放请求（即PDU Session Resource Release Command
）。
RAN与UE交互，发送AN-Specific Resource Modification。 
RAN向AMF返回会话释放响应（即PDU Session Resource Release Response
）。
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
UE返回会话释放确认给RAN，RAN携带给AMF。 
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
I-SMF向A-SMF发起Nsmf_PDUSession_Update
 Response，携带释放结果。
A-SMF启动SM策略关联终止过程Npcf_SMPolicyControl_Delete
来释放与PCF的SM策略控制关联。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF向I-SMF返回Nsmf_PDUSession_NotifyStatus
 (Release)。
I-SMF释放会话相关资源，向AMF发起Nsmf_PDUSession_NotifySMContextStatus
 (Release)。
####### RAN发起的带I-SMF的会话释放 
图6  RAN发起的带I-SMF的会话释放
[]images/6%E3%80%81%20RAN%E5%8F%91%E8%B5%B7%E7%9A%84%E5%B8%A6I-SMF%E7%9A%84%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE.png)
流程说明如下： 
发起请求。 
RAN向I-SMF发送N2 Message。 
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Info。
I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求，requestIndication设置为NW_REQ_PDU_SES_REL。
A-SMF向I-SMF返回响应。 
N4会话释放。 
A-SMF向A-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
A-UPF向A-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
A-SMF向I-SMF发起Nsmf_PDUSession_Update
 Request请求，其中requestIndication设置为NW_REQ_PDU_SES_REL。
N4会话释放。 
I--SMF向I-UPF发送N4会话释放请求消息（即PFCP Session Deletion Request
）。
I-UPF向I-SMF返回N4会话释放响应消息（即PFCP Session Deletion Response
）。
（可选）AMF与I-SMF交互。 
I-SMF在Update响应里携带N1 SM container (PDU Session Release Command
)通知UE释放会话，如果该会话的UP连接存在，则携带N2 PDU Session Resource Release Command
 (PDU Session ID) 通知(R)AN释放会话。
AMF向I-SMF返回响应。 
AMF向RAN发起会话释放请求（即PDU Session Resource Release Command
）。
RAN与UE交互，发送AN-Specific Resource Modification。 
RAN向AMF返回会话释放响应（即PDU Session Resource Release Response
）。
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
UE返回会话释放确认给RAN，RAN携带给AMF。 
AMF向I-SMF发起Nsmf_PDUSession_UpdateSMContext
 Request请求，携带N2 SM Resource Release Ack , User Location Information。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
I-SMF向A-SMF发起Nsmf_PDUSession_Update
 Response，携带释放结果。
A-SMF启动SM策略关联终止过程Npcf_SMPolicyControl_Delete
来释放与PCF的SM策略控制关联。
PCF向A-SMF返回SM策略关联终止响应Npcf_SMPolicyControl_Delete
 Response。
（可选）如果是最后一个会话，则A-SMF通过Nudm_SubscriberDataManagement_Unsubscribe
向UDM发起订阅。
A-SMF向UDM发起会话去注册过程Nudm_UEContextManagement_Deregistration
。
A-SMF向CHF上报话单。 
A-SMF向I-SMF返回Nsmf_PDUSession_NotifyStatus
 (Release)。
I-SMF释放会话相关资源，向AMF发起Nsmf_PDUSession_NotifySMContextStatus
 (Release)。
#### 5GS系统内3GPP接入下的切换 
##### 基于Xn口的切换 
根据切换过程中，是否存在I-SMF改变，基于Xn接口的切换划分如下四种场景： 
插入I-SMF的Xn切换 
更换I-SMF的Xn切换 
删除I-SMF的Xn切换 
I-SMF不变的Xn切换 
###### 插入I-SMF的Xn切换 
图1  插入I-SMF的Xn切换
[]images/1.%E6%8F%92%E5%85%A5I-SMF%E7%9A%84Xn%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
源基站与目的基站进行切换准备以及执行过程，Target NG-RAN向AMF发起N2 Path Switch Request
请求。
（可选）在N2路径切换请求中接收到的PDU会话列表，对于其中每个被拒绝的PDU会话，AMF都需要发起释放操作，携带以下参数：failedToBeSwitched、Path Switch Request Setup Failed Transfer ，同[RAN发起的带I-SMF的会话释放](1600153682248.html#z15e0fa4b895845bca5cf01ee10dff1fc__ae41ac37-3d98-4cf0-8395-7d6af5d5b62d)。
AMF选择I-SMF。 
如果根据SMF的服务区信息，发现新的位置无法服务，则AMF选择I-SMF插入会话。 
如果选择了新的I-SMF，则AMF发送Nsmf_PDUSession_CreateSMContext
请求（包含SUPI，AMF ID，SMF ID，SM上下文ID，N2 SM信息（辅助RAT使用数据），UE位置信息，UE存在于LADN服务区域中）到新选择的I-SMF。
新的I-SMF和A-SMF交互。 
新的I-SMF向A-SMF发送Nsmf_PDUSession_Context请求（包含SM context，SMContextRef）以获取SM上下文。 
A-SMF向I-SMF返回上下文响应，包含I-UPF上行用到的N9地址psaTunnelInfo，epsPdnCnxInfo，epsBearerInfo。 
I-SMF执行UPF选择过程。 
I-SMF向I-UPF发送N4会话建立请求PFCP Session Establishment Request
。
I-UPF向I-SMF返回N4会话建立响应PFCP Session Establishment Response
。
I-SMF根据AMF携带的smContextRef以及A-SMF返回的smfUri里的IP地址相同，判断是插入流程，向A-SMF发起Nsmf_PDUSession_Create
 Request请求，包含SUPI, PDU Session ID，(Secondary RAT usage data，Handover Flag)，UE Location Information，UE presence in LADN service area，DL CN Tunnel Info of the I-UPF，DNAI list supported by the I-SMF，End Marker Indication。
A-SMF与Psa UPF交互。假如old I-UPF不存在或N3与N9隧道不能复用，则A-SMF新建N9隧道。为了支持后续可能的4/5G互操作，A-SMF还需要申请Pgw S5uFteid。 
A-SMF向Psa UPF发起N4会话修改请求PFCP Session Modification Request
，包含I-UPF的DL CN隧道信息。
Psa UPF向A-SMF返回N4会话修改响应PFCP Session Modification Response
。
（可选）如果存在old I-UPF，需要设置定时器延时删除I-UPF以及N3隧道资源。为了辅助Target NG-RAN中的重新排序功能，Psa UPF在切换路径时，为旧路径上的每个N3 / N9隧道发送一个或多个“结束标记”数据包，并将“结束标记”分组转发到Target NG-RAN。 
A-SMF向I-SMF返回Nsmf_PDUSession_Create
 Response响应。如果A-SMF携带了新的N9隧道，则执行9a，I-SMF向I-UPF发起N4会话修改。
I-SMF向 AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应 (包含 I-UPF分配的N3 Tli信息UL CN Tunnel Info )。
AMF给基站发送N2 Path Switch Request Acknowledge
。
Target NG- RAN 向Source NG-RAN发起资源释放请求。 
后续流程同现有处理。 
###### 更换I-SMF的Xn切换 
图2  更换I-SMF的Xn切换
[]images/2.%20%E6%9B%B4%E6%8D%A2I-SMF%E7%9A%84Xn%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE通过Source NG-RAN与Target NG-RAN间的Xn接口切换到Target NG-RAN下，TargetNG-RAN发送N2 Path Switch Request
消息给AMF，携带需要切换的PDU会话列表、用户位置信息。
（可选）在N2路径切换请求中接收到的PDU会话列表，对于其中每个被拒绝的PDU会话，AMF都需要发起释放操作，携带以下参数：failedToBeSwitched、Path Switch Request Setup Failed Transfer ，同[RAN发起的带I-SMF的会话释放](1600153682248.html#z15e0fa4b895845bca5cf01ee10dff1fc__ae41ac37-3d98-4cf0-8395-7d6af5d5b62d)。
AMF选择I-SMF。 
如果根据用户TA服务区信息，发现老的I-SMF无法继续服务，则选择新的I-SMF。 
如果选择了新的I-SMF，则AMF发送Nsmf_PDUSession_CreateSMContext
请求（包括PDU Session ID, 旧的I-SMF的SM Context ID, UE location info, Access Type, RAT Type, Operation Type）到新选择的I-SMF。
New I-SMF与Old I-SMF交互。 
New I-SMF通过调用Nsmf_PDUSession_Context Request请求（包含SM context type, SM Context ID）从Old I-SMF中检索SM上下文。SM上下文类型指示所请求的信息是所有SM上下文，即PDN 连接上下文和5G SM上下文。 
Old I-SMF 向New I-SMF返回响应，指示的PDU会话的SM上下文。 
New I-SMF基于所接收的SM上下文选择 New I-UPF。 
New I-SMF向New I-UPF发送N4会话建立请求PFCP Session Establishment Request
。
New I-UPF向New I-SMF返回N4会话建立响应PFCP Session Establishment Response
。
New I-SMF调用Nsmf_PDUSession_Update
请求（包含Secondary RAT usage data, UE Location Information, UE presence in LADN service area, DL CN Tunnel Info of the I-UPF, DNAI list supported by target I-SMF, End Marker Indication）。 SMF将替换I-SMF的SM上下文ID，以便后续会话进行进一步操作。
A-SMF与Psa UPF交互。假如old I-UPF不存在，并且N3与N9隧道不能复用，则A-SMF新建N9隧道。 
A-SMF向Psa UPF发起N4会话修改请求PFCP Session Modification Request
，包含I-UPF的DL CN隧道信息。
Psa UPF向A-SMF返回N4会话修改响应PFCP Session Modification Response
。
（可选）如果存在old I-UPF，需要设置定时器延时删除I-UPF，以及N3隧道资源。为了辅助Target NG-RAN中的重新排序功能，Psa UPF在切换路径时，为旧路径上的每个N3 / N9隧道发送一个或多个“结束标记”数据包，并将“结束标记”分组转发到Target NG-RAN。 
A-SMF向I-SMF返回Nsmf_PDUSession_Create
 Response响应，携带：Tunnel Info at UPF(PSA) for UL data。
New I-SMF向 AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应 (包含N2 SM information (CN N3 Tunnel Info,Security Indication) )。
AMF给基站发送 N2 Path Switch Request Acknowledge
。
资源与会话释放。 
AMF将Nsmf_PDUSession_ReleaseSMContext
 Request请求（包含I-SMF only indication）发送到旧I-SMF以释放旧I-SMF中的资源。I-SMF only indication指示旧I-SMF不去释放A-SMF的资源。
N4会话释放。 
Old I-SMF向AMF返回[Nsmf_PDUSession_ReleaseSMContext](../../Nsmf\topics\5.html) Response响应。
TARGET RAN 向Source RAN发起资源释放请求。 
后续流程同现有处理。 
###### 删除I-SMF的Xn切换 
图3  删除I-SMF的Xn切换
[]images/3.%20%E5%88%A0%E9%99%A4I-SMF%E7%9A%84Xn%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B(%E9%87%8D%E7%94%A81).png)
流程说明如下： 
UE通过Source NG-RAN与Target NG-RAN间的Xn接口切换到Target NG-RAN下，Target NG-RAN发送N2 Path Switch Request
消息给AMF，携带需要切换的PDU会话列表、用户位置信息。
（可选）在N2路径切换请求中接收到的PDU会话列表，对于其中每个被拒绝的PDU会话，AMF都需要发起释放操作，携带以下参数：failedToBeSwitched、Path Switch Request Setup Failed Transfer ，同[RAN发起的带I-SMF的会话释放](1600153682248.html#z15e0fa4b895845bca5cf01ee10dff1fc__ae41ac37-3d98-4cf0-8395-7d6af5d5b62d)。
AMF选择I-SMF。 
如果根据用户TA服务区信息，发现老的I-SMF无法继续服务，则选择新的I-SMF。 
根据无smContextRef，判断是I-SMF删除的Xn切换流程。如果选择了新的I-SMF，则AMF发送Nsmf_PDUSession_CreateSMContext
 Request（包括SUPI, PDU Session ID, AMF ID, PDU Session To Be Switched with N2 SM Information (Secondary RAT usage data), UE Location Information, UE presence in LADN service area, Target NG-RAN Tunnel Info）到SMF。
SMF基于所接收的SM上下文选择 I-UPF。 
A-SMF向 I-UPF发起N4会话建立请求PFCP Session Establishment Request
，New I-UPF提供隧道端点。
NEW I-UPF向A-SMF返回N4 PFCP Session Establishment Response
响应。
N4会话修改请求。 
SMF向Psa UPF发起N4会话修改请求PFCP Session Modification Request
（包含I-UPF的DL CN隧道信息）。
Psa UPF向SMF返回N4 PFCP Session Modification Response
响应。
N4会话更新请求。 
SMF向New I-UPF发起N4会话更新请求PFCP Session Modification Request
。
New I-UPF UPF向SMF返回N4 PFCP Session Modification Response
响应。
（可选）如果存在old I-UPF，需要设置定时器延时删除I-UPF，以及N3隧道资源，为了辅助目标NG-RAN中的重新排序功能，psa UPF在切换路径时，为旧路径上的每个N3 / N9隧道发送一个或多个“结束标记”数据包，应当将“结束标记”分组转发到目标NG-RAN。 
A-SMF向 AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应 (包含N2 SM information (CN N3 Tunnel Info,Security Indication) )。
AMF给基站发送 N2 Path Switch Request Acknowledge
。
资源与会话释放。 
AMF将Nsmf_PDUSession_ReleaseSMContext
 Request请求（包含I-SMF only indication）发送到旧I-SMF以释放旧I-SMF中的资源。I-SMF only indication指示旧I-SMF不去释放A-SMF的资源。
N4会话释放。 
Old I-SMF向AMF返回Nsmf_PDUSession_ReleaseSMContext
 Response响应。
TARGET RAN 向Source RAN发起资源释放请求。 
后续流程同现有处理。 
###### I-SMF不变的Xn切换 
图4  I-SMF不变的Xn切换
[]images/4.%20I-SMF%E4%B8%8D%E5%8F%98%E7%9A%84Xn%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B(%E9%87%8D%E7%94%A81).png)
该流程场景不做描述，相较于无I-SMF的基于Xn接口NG-RAN间的Handover流程，主要存在如下差异点： 
步骤1中，AMF收到Path Switch Request
后，根据N2消息中携带的信元，分别识别需要激活和去激活的PDU。
针对需要激活的PDU，如果当前I-SMF不变，AMF会给I-SMF发送Nsmf_PDUSession_UpdateSMContext Request消息，携带SUPI、AMF ID、SM Context ID In I-SMF、PDU Session To Be Switched with N2 SM Information、UE Location Information等信元。 
针对要去激活的PDU，AMF直接给I-SMF发送Nsmf_PDUSession_UpdateSMContext Request消息。 
##### 基于N2接口的切换 
根据切换过程中，是否存在I-SMF改变，基于N2接口的切换划分如下四种场景： 
I-SMF更新的N2切换 
I-SMF插入的N2切换 
I-SMF删除的N2切换 
I-SMF不变的N2切换 
###### I-SMF更新的N2切换 
图1  I-SMF更新的N2切换
[]images/1.1%20%20I-SMF%E6%9B%B4%E6%96%B0%E7%9A%84N2%E5%88%87%E6%8D%A2%E6%89%A7%E8%A1%8C.png)
流程说明如下： 
准备T测业务资源

Source-RAN检测到UE需要切换到目标小区，发送Handover Required
消息给Source AMF。
Source AMF选择Target AMF。 
Source AMF向Target AMF发送Namf_Communication_CreateUEContext
 Request请求。
Target AMF根据UE的位置判断其移出SMF的服务区域，Target AMF根据新的位置选择判断更新I-SMF。 
Target AMF向Target I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request请求（包含PDU Session ID，Target ID，T-AMF ID，SM Context ID）。
Target I-SMF向Source I-SMF发送Nsmf_PDUSession_Context Request请求（包含SM context type，SM Context ID）。 
Source I-SMF向Target I-SMF返回Nsmf_PDUSession_Context Response响应，包含PSA
N9隧道信息。 
Target I-SMF选择Target I-UPF。 
Target I-SMF向Target I-UPF发送N4 PFCP Session Establishment Request
请求。
Target I-UPF向Target I-SMF返回N4 PFCP Session Establishment Response
响应。

I-SMF向Target AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应（包含PDU Session ID, N2 SM Information） 。
准备非直传隧道
Target AMF检测切换响应。 
Target AMF下发Handover Request
给Target NG-RAN，携带PDU会话列表，列表每项包含UPF
N3隧道信息以及QoS信息。
Target NG-RAN发送Handover Request Acknowledge
给Target AMF，携带Target
to Source transparent container、建立成功的PDU会话列表，列表中每项包含目标NR N3隧道信息。
Target AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request 消息（包含PDU Session ID, N2 SM Response received from T-RAN）。
（可选）如果有间接转发隧道，Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
（包含T-RAN SM N3 forwarding Information list, indication to allocate DL forwarding tunnel（s） for indirect forwarding） ，分配间接转发隧道信息。
（可选）Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应（包含Target I-UPF N9 forwarding Information list）。
（可选）Target I-SMF向Source I-SMF发送Nsmf_PDUSession_UpdateSMContext

Request请求（包含Target I-UPF SM N9 forwarding Information list, Operation
type）。
（可选）Source I-SMF向Source I-UPF发送N4 PFCP Session Modification Request
请求（包含UPF SM N9 forwarding Information list, indication to allocate
DL forwarding tunnel（s） for indirect forwarding），建立间接转发隧道。
（可选） Source I-UPF向Source I-SMF返回N4 PFCP Session Modification Response
响应
（包含UPF SM N3 forwarding Information list）。
（可选）Source I-SMF向 Target I-SMF返回Nsmf_PDUSession_UpdateSMContext

Response响应 （包含UPF SM N3 forwarding Information list）。
Target I-SMF向Target AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应（包含N2 SM Information）。
Target AMF向Source AMF返回Namf_Communication_CreateUEContext
 Response响应。
切换执行阶段1：切下行
Source AMF下发Handover Command
给Source NG-RAN，携带Target to Source
transparent container。
Source NG-RAN将Handover Command
发送给UE。
UE切换到Target NG-RAN后，发送Handover Confirm。 
Target NG-RAN发送Handover Notify
给Target AMF。Target AMF向Source
AMF发送Namf_Communication_N2InfoNotify
消息，I-SMF改变或删除时携带smfChangeInfoList指示列表。

Target AMF向Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求。

Source AMF与Source
I-SMF交互。 
Source AMF向Source I-SMF发送Nsmf_PDUSession_ReleaseSMContext

Request请求（包含I-SMF only indication），Source I-SMF收到消息后启动定时器。
Source I-SMF向Source AMF返回Nsmf_PDUSession_ReleaseSMContext

Response响应。
Target I-SMF与Target I-UPF交互。 
Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，携带DL
AN Tunnel Info of T-RAN。
Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应。
SMF与UPF交互。 
Target I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求（包含PDU
Session ID、  DL CN Tunnel Info of Target I-UPF for N9、DNAI(s) supported
by the I-SMF）。

A-SMF向A-UPF发送N4 PFCP Session Modification Request
请求，携带DL CN Tunnel
Info of Target I-UPF。
A-UPF向A-SMF返回N4 PFCP Session Modification Response
响应。
A-SMF向Target I-SMF返回Nsmf_PDUSession_Update
 Response响应。
Target I-SMF向Target AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
切换执行阶段2：删除老资源
UE发起移动性注册更新过程。 
上下文释放。 
Source AMF下发UE Context Release Command
给Source NG-RAN。
Source NG-RAN返回UE Context Release Complete
给Source AMF。
（可选）如果有间接转发隧道，进行N4会话修改。 
Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，删除间接转发隧道信息。
Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应。
（可选）[步骤29](1600153452074.html#z101bf2fd180a402db9ccffe221fc28f5__48c72a6f-1f32-47f0-b9be-6d8f7f3d86f8)中的定时器超时，进行N4会话释放。
Source I-SMF向Source I-UPF发送N4 PFCP Session Deletion Request
，删除间接转发隧道信息及释放PDU资源。
Source I-UPF向Source I-SMF返回N4 PFCP Session Deletion Response
响应。
###### I-SMF插入的N2切换 
图2  I-SMF插入的N2切换
[]images/2.1%20%20I-SMF%E6%8F%92%E5%85%A5%E7%9A%84N2%E5%88%87%E6%8D%A2%E6%89%A7%E8%A1%8C.png)
流程说明如下： 
准备T测业务资源
Source NG-RAN检测到UE需要切换到目标小区，发送Handover Required
消息给Source AMF。
Source AMF选择Target AMF。 
Source AMF向Target AMF发送Namf_Communication_CreateUEContext
 Request请求。
Target AMF根据UE的位置判断其移出SMF的服务区域，Target AMF根据新的位置选择判断插入I-SMF。 
Target AMF向Target I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request请求（包含PDU Session ID, Target ID, T-AMF ID SM Context ID）。
Target I-SMF向A-SMF发送Nsmf_PDUSession_Context Request请求（SM context
type, SM Context ID）。 
A-SMF向Target I-SMF返回Nsmf_PDUSession_Context Response响应。 
I-SMF选择Target I-UPF。 
Target I-SMF向Target I-UPF发送N4 PFCP Session Establishment Request
请求。
Target I-UPF向Target I-SMF返回N4 PFCP Session Establishment Response
响应。

Target I-SMF向A-SMF发送Nsmf_PDUSession_Create
 Request请求。
（可选）如果插入前SMF只连接PSA UPF，未曾分配过N9核心网隧道信息， A-SMF向PSA UPF发送N4 PFCP Session
Modification Request
请求。
（可选）PSA UPF向A-SMF返回N4 PFCP Session Modification  Response
响应，其中包含PSA
UPF分配的N9核心网隧道信息。
A-SMF向Target I-SMF返回Nsmf_PDUSession_Create
 Response响应，包含PSA
UPF的N9核心网隧道信息。
Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，携带PSA
UPF的N9核心网隧道信息。
Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应。
Target I-SMF向Target AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应（PDU
Session ID, N2 SM Information）。
准备非直传隧道
Target AMF检测切换响应。 
Target AMF下发Handover Request
给Target NG-RAN，携带PDU会话列表，列表每项包含UPF
N3隧道信息以及QoS信息。
Target NG-RAN发送Handover Request Acknowledge
给Target AMF，携带Target
to Source transparent container、建立成功的PDU会话列表，列表中每项包含目标NR N3隧道信息。
Target AMF向Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求（包含PDU
Session ID, N2 SM Response received from T-RAN）。
（可选）如果有间接转发隧道，Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
（T-RAN SM N3 forwarding Information list，indication to allocate
DL forwarding tunnel(s) for indirect forwarding），分配间接转发隧道信息。
（可选）Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应（Target
I-UPF N9 forwarding Information list）。
（可选）Target I-SMF向A-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求（包含Target I-UPF SM N9 forwarding Information list, Operation type）。
（可选） A-SMF向PSA UPF发送N4 PFCP Session Modification Request
请求（包含UPF
SM N9 forwarding Information list, indication to allocate DL forwarding
tunnel(s) for indirect forwarding），建立间接转发隧道。
（可选）PSA UPF向A-SMF返回N4 PFCP Session Modification Response
响应（包含UPF
SM N3 forwarding Information list）。
（可选）A-SMF向Target I-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应（包含UPF
SM N3 forwarding Information list）。
Target I-SMF向Target AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应（包含N2
SM Information）。
Target AMF向Source AMF返回Namf_Communication_CreateUEContext
 Response响应。
切换执行阶段1：切下行
Source AMF下发Handover Command
给Source NG-RAN，携带Target to Source
transparent container。
Source NG-RAN将[Handover Command](../../N2接口\topics\21.html)发送给UE。
UE切换到Target NG-RAN后，发送Handover Confirm。 
Target NG-RAN发送Handover Notify
给Target AMF。
Target AMF向Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求（包含Handover
Complete Indication）。
Target I-SMF与Target I-UPF交互。 
Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，携带DL
AN Tunnel Info of T-RAN。
Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应。
SMF与UPF交互。 
Target I-SMF向A-SMF发送Nsmf_PDUSession_Update
 Request请求（包含PDU
Session ID、 DL CN Tunnel Info of Target I-UPF for N9、DNAI(s) supported
by the I-SMF）。
A-SMF向A-UPF发送N4 PFCP Session Modification Request
请求，携带DL CN Tunnel
Info of Target I-UPF。
A-UPF向A-SMF返回N4 PFCP Session Modification Response
响应。
A-SMF向Target I-SMF返回Nsmf_PDUSession_Update
 Response响应。
Target I-SMF向Target AMF返回[Nsmf_PDUSession_UpdateSMContext](../../Nsmf\topics\4.html) Response响应。
切换执行阶段2：删除老资源
UE发起移动性注册更新过程。 
上下文释放。 
Source AMF下发UE Context Release Command
给Source NG-RAN。
Source NG-RAN返回UE Context Release Complete
给Source AMF。
（可选）如果有间接转发隧道，N4会话修改。 
Target I-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，删除间接转发隧道信息。
Target I-UPF向Target I-SMF返回N4 PFCP Session Modification Response
响应。
（可选）如果定时器超时，进行N4会话释放。 
ASMF向PSA-UPF发送N4 PFCP Session Modification Request
，删除间接转发隧道信息及释放PDU资源。
PSA UPF向A-SMF返回N4 PFCP Session Modification Response
响应。
###### I-SMF删除的N2切换 
图3  I-SMF删除的N2切换
[]images/3.1%20%20I-SMF%E5%88%A0%E9%99%A4%E7%9A%84N2%E5%88%87%E6%8D%A2%E6%89%A7%E8%A1%8C.png)
流程说明如下： 
准备T侧业务资源
Source NG-RAN检测到UE需要切换到目标小区，发送Handover Required
消息给Source AMF。
Source AMF选择Target AMF。 
Source AMF向Target AMF发送Namf_Communication_CreateUEContext
 Request请求。
Target AMF根据UE的位置判断其移出SMF的服务区域，Target AMF根据新的位置选择判断删除I-SMF。 
Target AMF向 SMF发送Nsmf_PDUSession_CreateSMContext
 Request请求（包含PDU
Session ID、Target ID、T-AMF ID、SM Context ID）。
A-SMF选择Target I-UPF。 
如果...|那么...
---|---
步骤6不需要插入I-UPF|执行步骤7-步骤8
步骤6需要插入新的I-UPF|执行步骤9-步骤10
（可选）当无需插入I-UPF时，A-SMF向PSA
UPF发送N4 PFCP Session Modification Request
请求。
（可选）PSA UPF向A-SMF返回N4
PFCP Session Modification Response
响应。
（可选）当需要插入新的I-UPF时，SMF向I-UPF发送N4
PFCP Session Establishment Request
请求。
（可选）Target I-UPF向I-SMF返回N4
PFCP Session Establishment Response
响应。
A-SMF向Target AMF返回Nsmf_PDUSession_CreateSMContext
 Response响应（PDU
Session ID, N2 SM Information）。
准备非直传隧道
Target AMF检测切换响应。 
Target AMF下发Handover Request
给Target NG-RAN，携带PDU会话列表，列表每项包含UPF（PSA）
N3隧道信息以及QoS信息。
Target NG-RAN发送Handover Request Acknowledge
给Target AMF，携带Target
to Source transparent container、建立成功的PDU会话列表，列表中每项包含目标NR N3隧道信息。
Target AMF向SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求（包含PDU
Session ID，N2 SM Response received from T-RAN）。
如果...|那么...
---|---
需要间接转发隧道|执行步骤16-步骤23
步骤6不需要插入I-UPF|执行步骤16-步骤17
步骤6需要插入新的I-UPF|执行步骤18-步骤19
（可选）A-SMF向PSA UPF发送N4
PFCP Session Modification Request
请求（包含T-RAN SM N3 forwarding Information
list、indication to allocate DL forwarding tunnel(s) for indirect
forwarding），分配间接转发隧道信息。
（可选）PSA UPF向A-SMF返回N4
PFCP Session Modification Response
响应（包含UPF N9 forwarding Information list）。
（可选）A-SMF向Target
I-UPF发送N4 PFCP Session Modification Request
消息 （包含T-RAN SM N3 forwarding Information
list、indication to allocate DL forwarding tunnel(s)  for indirect
forwarding），分配间接转发隧道信息。
（可选）Target I-UPF向A-SMF返回N4
PFCP Session Modification Response
响应（包含Target I-UPF N9 forwarding Information
list）。
（可选）A-SMF向Source I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求（包含UPF
SM N9 forwarding Information list, Operation type）。
（可选）Source I-SMF向Source I-UPF发送N4 PFCP Session Modification Request
请求
（包含UPF SM N9 forwarding Information list，indication to allocate DL
forwarding tunnel(s) for indirect forwarding），建立间接转发隧道。
（可选）Source I-UPF向Source I-SMF返回N4 PFCP Session Modification Response
响应（包含UPF
SM N3 forwarding Information list）。
（可选）Source I-SMF向A-SMF返回Nsmf_PDUSession_UpdateSMContext

Response响应（包含UPF SM N3 forwarding Information list）。
A-SMF向Target AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应（包含N2
SM Information）。
Target AMF向Source AMF返回Namf_Communication_CreateUEContext
 Response响应。
切换执行阶段1：切下行
Source AMF下发Handover Command
给Source NG-RAN，携带Target to Source
transparent container。
Source NG-RAN将Handover Command
发送给UE。
UE切换到Target NG-RAN后，发送Handover Confirm。 
Target NG-RAN发送Handover Notify
给Target AMF。
Target AMF向Target I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求（包含Handover
Complete indication）。
Source I-SMF与Source
AMF交互。 

Source AMF向Souce I-SMF发送Nsmf_PDUSession_ReleaseSMContext

Request请求（包含I-SMF only indication），I-SMF收到消息后启动定时器。
Source I-SMF向Source AMF返回Nsmf_PDUSession_ReleaseSMContext
 Response响应。
SMF与UPF交互。 
A-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，携带DL
AN Tunnel Info of T-RAN。
Target I-UPF向A-SMF返回N4 PFCP Session Modification Response
响应。
A-SMF向PSA UPF发送N4 PFCP Session Modification Request
请求，携带DL CN Tunnel
Info of Target I-UPF。
PSA UPF向SMF返回N4 PFCP Session Modification Response
响应。
SMF向Target AMF返回Nsmf_PDUSession_UpdateSMContext
 Response。
切换执行阶段2：删除老资源
UE发起移动性注册更新过程。 
上下文释放。 
Source AMF下发UE Context Release Command
给Source-RAN。
Source-RAN返回UE Context Release Complete
给Source AMF。
（可选）如果[步骤31](1600153452074.html#z101bf2fd180a402db9ccffe221fc28f5__a745eae6-74a4-4412-a349-45e510026b04)中的定时器超时，N4会话释放。
Source I-SMF向Source I-UPF发送N4 PFCP Session Deletion Request
请求，删除间接转发隧道信息及释放PDU资源。
Source I-UPF向Source I-SMF返回N4 PFCP Session Deletion Response
响应。
（可选）如果有间接转发隧道，进行N4会话修改。 
A-SMF向Target I-UPF发送N4 PFCP Session Modification Request
请求，删除间接转发隧道信息。如果没有Target
I-UPF，则发给A-UPF。
Target I-UPF向A-SMF返回N4 PFCP Session Modification Response
响应。
###### I-SMF不变的N2切换 
图4  I-SMF不变的N2切换
[]images/4.1%20I-SMF%E4%B8%8D%E5%8F%98%E7%9A%84N2%E5%88%87%E6%8D%A2%E6%89%A7%E8%A1%8C.png)
流程说明如下： 
在切换准备阶段，相较于无I-SMF的基于N2接口NG-RAN间的Handover流程，主要存在如下差异： 
目标AMF收到源侧AMF的Namf_Communication_CreateUEContext Request消息后，目标AMF会直接向I-SMF发送Nsmf_PDUSession_UpdateSMContext
Request消息（包含PDU Session ID、Target ID、T-AMF ID、N2 SM Information）更新上下文。 
在收到目标RAN侧的N2消息后，AMF将N2信息发送给I-SMF。 
在切换执行阶段，相较于无I-SMF的基于N2接口NG-RAN间的Handover流程，主要存在如下差异： 
AMF侧对于部分未切换成功的PDU，源AMF发送Release消息给I-SMF，由I-SMF通知PDU释放。 
目标AMF给目标I-SMF发送Nsmf_PDUSession_UpdateSMContext Request消息，携带Handover
Complete indication。 
##### 基于N2接口的切换取消 
根据切换取消过程中，是否存在I-SMF改变，基于N2接口的切换取消划分如下四种场景： 
I-SMF变化的N2切换取消 
I-SMF插入的N2切换取消 
I-SMF删除的N2切换取消 
I-SMF不变的N2切换取消 
###### I-SMF变化的N2切换取消 
图1  I-SMF变化的N2切换取消
[]images/1.2%20%20I-SMF%E5%8F%98%E5%8C%96%E7%9A%84N2%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88.png)
流程说明如下： 
Source RAN检测到需要取消切换，发送Handover Cancel
给Source AMF，携带切换取消原因值。
（可选）Source AMF若已经通知Target AMF切换，则调用Target AMF的Namf_Communication_ReleaseUEContext
 Request服务，通知Target AMF取消切换。
（可选）Target AMF收到Namf_Communication_ReleaseUEContext
 Request消息后，若已经建立Target AMF与Target NR间的N2连接，则发送UE Context Release Command
给Target RAN，通知Target NR释放N2连接。

针对每一个PDU会话，Target AMF调用对应new I-SMF的Nsmf_PDUSession_UpdateSMContext
服务，携带PDU会话ID、切换取消指示。
N4会话释放。 
Target I-SMF发送N4 PFCP Session Deletion Request
到Target I-UPF，以释放为N4会话分配的所有资源。
Target I-UPF向Target I-SMF返回N4会话释放响应PFCP Session Deletion Response
。
（可选）如果在准备阶段设置了间接转发隧道，则Target I-SMF向Source I-SMF发起Nsmf_PDUSession_UpdateSMContext
请求，指示Source I-SMF删除临时分配给间接转发隧道的资源。
（可选）N4会话修改。 
Source I-SMF调用N4会话修改请求PFCP Session Modification Request
到Source I-UPF，以删除分配给间接转发隧道的所有资源。
Source I-UPF向Source I-SMF返回N4会话修改响应PFCP Session Modification Response
。
（可选）Source I-SMF向Target I-SMF返回Nsmf_PDUSession_UpdateSMContext
响应。
Target I-SMF向Target AMF返回：Nsmf_PDUSession_UpdateSMContext
 Response，指示切换取消完成。
（可选）Target AMF返回[Namf_Communication_ReleaseUEContext](../../Namf\topics\6.html) Response给Source AMF。
Source AMF向Source RAN返回Handover Cancel Acknowledge
。
###### I-SMF插入的N2切换取消 
图2  
I-SMF插入的N2切换取消
[]images/2.2%20%20I-SMF%E6%8F%92%E5%85%A5%E7%9A%84N2%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88.png)
流程说明如下： 
Source RAN检测到需要取消切换，发送Handover Cancel
给AMF，携带切换取消原因值。
（可选）Source AMF若已经通知Target AMF切换，则调用Target AMF的Namf_Communication_ReleaseUEContext
服务，通知Target AMF取消切换，携带UE Context ID, Relocation Cancel Indication。
（可选）Target AMF收到Namf_Communication_ReleaseUEContext
 Request消息后，若已经建立Target AMF与Target RAN间的N2连接，则发送[UE Context Release Command](../../N2接口\topics\14.html)给Target RAN，通知Target RAN释放为切换分配的AN资源。
针对每一个PDU会话，Target AMF调用对应new I-SMF的Nsmf_PDUSession_UpdateSMContext
服务，携带PDU会话ID、切换取消指示，以释放SM上下文和在Target I-SMF上分配的所有资源。
N4会话释放。 
Target I-SMF发送N4 PFCP Session Deletion Request
到Target I-UPF，以释放为N4会话分配的所有资源。
Target I-UPF向Target I-SMF返回N4会话释放响应PFCP Session Deletion Response
。
Target I-SMF向A-SMF调用Nsmf_PDUSession_Update
请求（包含PDU会话ID，Relocation Cancel Indication重定位取消指示），以释放在准备阶段分配的PDU会话资源。
（可选）如果在准备阶段分配了N9的CN隧道，即N3和N9的CN隧道不同，则进行N4会话修改。 
A-SMF向PSA UPF发送N4会话修改请求PFCP Session Modification Request
，要求PSA UPF释放N9的CN隧道。
PSA UPF向A-SMF返回N4会话修改响应PFCP Session Modification Response
。
A-SMF向Target I-SMF返回Nsmf_PDUSession_Update
响应。
（可选）如果在准备阶段设置了间接转发隧道，则Target I-SMF向A-SMF发起Nsmf_PDUSession_UpdateSMContext
请求。
（可选）如果在准备阶段分配了N9的CN隧道，即N3和N9的CN隧道不同，则进行N4会话修改。 
A-SMF调用N4对PSA UPF的会话修改请求PFCP Session Modification Request
，以删除分配给间接转发隧道的所有资源。
PSA UPF向A-SMF返回N4会话修改响应PFCP Session Modification Response
。
（可选） A-SMF向Target I-SMF返回Nsmf_PDUSession_UpdateSMContext
响应。
I-SMF给Target AMF返回Nsmf_PDUSession_UpdateSMContext
响应，指示切换取消完成。
（可选）Target AMF返回Namf_Communication_ReleaseUEContext
 Response给Source AMF。
Source AMF给Source RAN返回Handover Cancel Acknowledge
。
###### I-SMF删除的N2切换取消 
图3  I-SMF删除的N2切换取消
[]images/3.2%20I-SMF%E5%88%A0%E9%99%A4%E7%9A%84N2%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88.png)
流程说明如下： 
Source RAN检测到需要取消切换，发送Handover Cancel
给AMF，携带切换取消原因值。
（可选）Source AMF若已经通知Target AMF切换，则调用Target AMF的Namf_Communication_ReleaseUEContext
服务，通知Target AMF取消切换。
（可选）Target AMF收到Namf_Communication_ReleaseUEContext
 Request消息后，若已经建立Target AMF与Target NR间的N2连接，则发送UE Context Release Command
给Target RAN，通知Target RAN释放N2连接。
针对每一个PDU会话，Target AMF调用对应new I-SMF的Nsmf_PDUSession_UpdateSMContext
服务，携带PDU会话ID、切换取消指示，以释放SM上下文以及在准备阶段在SMF上分配的所有资源。
（可选）如果在准备阶段分配了N3的CN隧道，即N3和N9的CN隧道不同，则进行N4会话修改。 
Target A-SMF向Target A-UPF发送N4会话修改请求PFCP Session Modification Request
，要求UPF释放N3的CN隧道。
Target A-UPF向Target A-SMF返回N4会话修改响应PFCP Session Modification Response
。
（可选）如果在准备阶段设置了间接转发隧道，则SMF向Source I-SMF发起Nsmf_PDUSession_UpdateSMContext
请求，指示源I-SMF删除临时分配给间接转发隧道的资源。
（可选）N4会话修改。 
Source I-SMF调用N4会话修改请求PFCP Session Modification Request
到Source I-UPF，以删除分配给间接转发隧道的所有资源。
Source I-UPF向Source I-SMF返回N4会话修改响应PFCP Session Modification Response
。
（可选）Source I-SMF向Target A-SMF返回Nsmf_PDUSession_UpdateSMContext
响应。
Target A-SMF向Target AMF返回Nsmf_PDUSession_UpdateSMContext
响应。
（可选）Target AMF向Source AMF返回Namf_Communication_ReleaseUEContext
 Response响应。
Source AMF给Source RAN返回Handover Cancel Acknowledge
。
###### I-SMF不变的N2切换取消 
图4  I-SMF不变的N2切换取消
[]images/4.2%20%20I-SMF%E4%B8%8D%E5%8F%98%E7%9A%84N2%E5%88%87%E6%8D%A2%E5%8F%96%E6%B6%88.png)
流程说明如下： 
Source RAN检测到需要取消切换，发送Handover Cancel
给AMF，携带切换取消原因值。
（可选）Source AMF若已经通知Target AMF切换，则调用Target AMF的Namf_Communication_ReleaseUEContext
服务，通知Target AMF取消切换。
（可选）Target AMF收到Namf_Communication_ReleaseUEContext
 Request消息后，若已经建立Target AMF与Target RAN间的N2连接，则发送UE Context Release Command
给Target RAN，通知Target RAN释放N2连接。
针对每一个PDU会话，Target AMF调用对应I-SMF的Nsmf_PDUSession_UpdateSMContext
服务，携带PDU会话ID、切换取消指示。
N4会话修改。 
I-SMF调用N4 PFCP Session Modification Request
到I-UPF，以删除分配给间接转发隧道的所有资源以及new N3隧道。
I-UPF向I-SMF返回N4会话修改响应PFCP Session Modification Response
。
I-SMF给Target AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应，指示切换取消完成。
（可选）T-AMF返回Namf_Communication_ReleaseUEContext
 Response给Source AMF。
Source AMF给Source RAN返回Handover Cancel Acknowledge
。
#### 4G 5G互操作 
##### 连接态下基于N26接口，5G跨系统移动到4G进行切换 
连接态下基于N26接口，5G跨系统移动到4G进行切换的流程如[图1](1600153524434.html#z7724352136ab4770bc9b3d7ca17e2dda__69010d0e-0070-4d04-8c71-fc98e9f49466)所示。
图1  连接态5G到4G的切换
[]images/1603963993759.png)
流程说明如下： 
NG-RAN决定将UE切换到E-UTRAN，例如IMS语音回落EPS网络场景。NG-RAN发送Handover Required
消息到AMF，通知有用户要进行切换。
（可选）如果AMF确定可以传输一个或多个EBI，则AMF向I-SMF发送Nsmf_PDUSession_Context消息，携带notToTransferEbiList。I-SMF之前已经缓存过EBI以及映射的QoS参数，直接返回给AMF。如果会话不支持4/5G互操作，则I-SMF返回响应拒绝， 设置原因值NO_EPS_5GS_CONTINUITY。 
AMF给目标MME发送Forward Relocation Request
，AMF将PDN连接上下文、安全上下文、MM上下文通过N26发送给目标MME。
MME选择SGW并向SGW发送Create Session Request消息，通知SGW建立承载。 
SGW分配本地资源，并向MME返回Create Session Response消息。 
MME发送Handover Request
消息给E-UTRAN，请求建立无线网络资源，包含承载信息，安全上下文。
E-UTRAN向MME发送Handover Request Acknowledge
消息。此时E-UTRAN做好在已经建立的E-RAB上接收GTP分组数据单元的准备。
（可选）如果使用Indirect Forwarding数据转发的方式，则MME向SGW请求建立间接转发隧道。 
MME向SGW发送Create Indirect Data Forwarding Tunnel Request消息，包含目标E-UTRAN的转发通道的地址和TEID。 
SGW-C向SGW-U发起N4会话更新流程，要求建立非直传隧道。 
SGW向MME发送Create Indirect Data Forwarding Tunnel Response响应消息。 
MME向AMF发送Forward Relocation Response
消息。对于间接转发方式，消息中还包含SGW的间接转发通道的地址和TEID。
（可选）如果使用Indirect Forwarding数据转发的方式，则AMF向I-SMF发送SGW间接转发通道的地址和TEID，用于建立间接转发隧道，I-SMF可能选择一个I-UPF进行数据转发。 
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息给I-SMF。
基于EPS bearer ID与QoS Flow ID之间的映射关系，I-SMF将数据转发的承载映射到5G QoS Flow。I-SMF将QFI、SGW地址和TEID发送给I-UPF。如果有间接转发的话，I-UPF还会分配数据转发的CN隧道信息。 
I-SMF返回Nsmf_PDUSession_UpdateSMContext
 Response消息，携带数据转发的CN隧道信息、QoS flow。
AMF发送Handover Command
给NG-RAN，通知切换准备完成。NG-RAN把消息转发到UE，通知UE切换到目的接入网络。此时下行数据可以通过UPF+PGW-U和SGW，从NG-RAN发送到目的E-UTRAN。
UE成功切换到目标小区后，上下行数据通过E-UTRAN进行发送。 
UE成功同步到目标小区后，发送Handover Complete消息给E-UTRAN，此时E-UTRAN将缓存的下行数据下发到UE，上行数据则经由UE→E-UTRAN→SGW→UPF+PGW-U。 
E-UTRAN发送Handover Notify
消息到MME，通知目标MME UE已经位于目标小区。
MME发送Forward Relocation Complete Notification
消息到AMF。
AMF发送Forward Relocation Complete Acknowledge
消息响应MME。
AMF向I-SMF发起PDU会话释放流程，请求删除I-SMF，并携带仅删除I-SMF指示。 
MME发送Modify Bearer Request消息到SGW，告知E-UTRAN的用户面地址和TEID。 
SGW发送Modify Bearer Request到A-SMF+PGW-C，携带SGW分配的SGW与PGW之间下行数据传输隧道的地址和TEID。 
A-SMF+PGW-C向UPF+PGW-U发起N4会话更新流程，更新用户面路径。 
A-SMF+PGW-C向SGW返回Modify Bearer Response消息。此时下行数据包就可以通过新建立的下行数据通道通过SGW转发给目标E-UTRAN。UE和UPF+PGW-U之间端到端的缺省承载和专有承载的用户面数据传输通道都建立完成。 
SGW发送Modify Bearer Response消息响应MME。 
UE发起TAU流程。 
在切换完成后，A-SMF+PGW-C可决定将映射到缺省承载中的部分数据流映射为专有承载，A-SMF+PGW-C可发起专有承载建立。 
（可选）如果使用了间接转发，AMF和MME分别发起间接转发隧道删除流程。 
##### 连接态下基于N26接口，4G跨系统移动到5G进行切换 
连接态下基于N26接口，4G跨系统移动到5G进行切换的流程图如[图1](1600153539138.html#zdff47f287c2245558b3b1374c37fcef5__30bbc191-839d-4738-823f-ed42a2c9505e)所示。
图1  4G到5G的切换
[]images/1603961746775.png)
流程说明如下： 
E-UTRAN决定将UE切换到NG-RAN。 
获取EPS上下文（准备阶段）
E-UTRAN发送Handover Required
消息到MME，通知有用户要进行切换。消息中包含的Indirect
Forwarding Flag信元，指示数据是否能从E-UTRAN直接传输到NG-RAN。
创建SM上下文
MME给目标AMF发送Forward Relocation Request
请求，消息中包含Indirect Forwarding
Flag，通知目标AMF数据是否可以直接传输。AMF将收到的EPS MM上下文转化为5G MM上下文。
AMF判断UE当前所在TA不在PGW-C+SMF的服务区域，决策插入I-SMF。AMF向I-SMF发送Nsmf_PDUSession_CreateSMContext

Request消息，创建SM上下文。消息中携带UE EPS PDN连接信息、AMF ID、和Indirect Forwarding
Flag。
I-SMF向A-SMF发起Nsmf_PDUSession_Create
 Request请求。
（可选）如果应用了动态PCC策略，则PGW-C+A-SMF向H-PCF+H-PCRF发起SM Policy Modification更新策略。其中，用户位置是在切换完成后才上报的。 
A-SMF+PGW-C向UPF+PGW-U交互。 
A-SMF+PGW-C向UPF+PGW-U发送PFCP Session Modification Request
，建立CN隧道。SMF返回PDUSessionCreatedData给I-SMF。
UPF+PGW-U向A-SMF+PGW-C返回PFCP Session Modification Response
响应。
SMF返回Nsmf_PDUSession_Create
 Response给I-SMF。
I-SMF选择I-UPF，并启动N4会话建立过程。 
I-SMF发送Nsmf_PDUSession_CreateSMContext
 Response给AMF，携带PDU会话ID、QFI、QoS
profile、CN隧道信息等。
AMF发送Handover Request
消息给NG-RAN，请求建立无线网络资源。
NG-RAN向AMF发送Handover Request Acknowledge
消息，携带NG-RAN的AN隧道信息以及N3隧道信息。此时NG-RAN已经做好传输分组数据单元的准备。
数据转发隧道
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request给I-SMF消息，更新N3的隧道信息。
I-SMF向I-UPF发起N4会话修改，将NG-RAN的N3用户面地址和TEID发送给I-UPF，并且将SGW的TEID和UPF的QFI和N3隧道信息做映射。 
I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Response消息响应AMF，消息中携带PDU会话ID、EPS承载建立列表和CN隧道。
AMF发送Forward Relocation Response
给MME，将CN隧道信息转发给MME。
（可选）如果数据转发采用Indirect Forwarding的方式，则SGW-C与MME交互。 
MME发送Create Indirect Data Forwarding Tunnel Request消息给SGW-C，更新源侧SGW-C与Indirect
Forwarding方式有关的地址信息等。 
SGW-C向SGW-U发起PFCP Session Modification Request
请求。
SGW-U向SGW-C返回PFCP Session Modification Response
响应。
SGW-C向MME返回Create Indirect Data Forwarding Tunnel Response响应消息。 
先切上行（执行阶段）
MME发送Handover Command
消息给E-UTRAN，通知切换准备完成。
E-UTRAN把Handover Command
消息发送到UE。收到这条消息后，UE将释放被目标小区所拒绝的EPS承载以及相应的EPS无线侧承载。
UE切换到NG-RAN后，发送Handover Confirm给NG-RAN，确认切换到NG-RAN。此时下行数据经由E-UTRAN→S-GW→UPF+PGW-U→NG-RAN→UE。 
NG-RAN发送Handover Notify
消息到AMF，通知目标AMF用户已经位于目标小区，消息中携带N3下行AN隧道信息。
AMF通过发送Forward Relocation Complete Notification
消息通知MME，UE已经到达目标区域。
MME发送Forward Relocation Complete Acknowledge
消息响应AMF。此时MME会启动一个定时器，用以监管E-UTRAN与S-GW的资源释放情况。
再切下行
AMF发送Nsmf_PDUSession_UpdateSMContext
 Request消息到I-SMF。
I-SMF向I-UPF发起N4会话更新，更新本地N3用户面。 
I-SMF向I-UPF发送PFCP Session Modification Request
请求。
I-UPF向I-SMF返回PFCP Session Modification Response
响应。
I-SMF发送Nsmf_PDUSession Modification Request请求通知A-SMF切换完成，消息中携带Handover
Complete indication（hoPreparationIndication：False），标志N26切换成功。 
A-SMF+PGW-C更新UPF+PGW-U的CN隧道信息，指示下行数据面已经切换到NG-RAN，并且EPS承载的CN隧道信息可以被释放。 
（可选）如果应用了PCC，则A-SMF+PGW-C向PCF+PCRF更新信息，例如用户的位置和接入类型的变更（接入类型在准备阶段上报）。 
A-SMF返回Nsmf_PDUSession Modification Response响应给I-SMF。 
I-SMF回复Nsmf_PDUSession_UpdateSMContext
 Response给AMF，确认收到了Handover
Complete。
收尾阶段
UE执行EPS到5GS的移动性注册流程。 
删除建立的转发通道和资源。流程结束。 
##### 空闲态下基于N26接口，5G跨系统移动到4G进行TAU 
空闲态下基于N26接口，5G跨系统移动到4G进行TAU的流程如[图1](1600153575794.html#zd2652df5029f4accaf0deeab04032552__48bce7eb-7084-4ab3-90d7-8fbf8cec6444)所示。
图1  5G到4G的TAU
[]images/1603962118648.png)
流程说明如下： 
UE从5GS覆盖区移动到EPS覆盖区，触发TAU流程。 
UE发送向E-UTRAN发送TAU Request消息，消息中EPS mobile identity IE携带5G-GUTI映射出的4G-GUTI，接入层信令中包含由5G-GUTI映射出GUMMEI。TAU Request消息使用5G的安全上下文进行完整性保护。消息中携带UE status信元，向网络提供与EPS交互的当前UE注册状态的相关信息，取值为UE is in 5GMM-REGISTERED state。 
E-UTRAN将TAU Request消息转发给MME。MME根据TAU Request消息中的EPS mobile identity IE信息，判断GUTI不是MME分配的，再根据MME FQDN通过DNS进行对端AMF查询。 
获取SM上下文
MME向对端AMF发送Context Request
消息，获取用户上下文。
AMF向SMF+PGW-C发送Nsmf_PDUSession_RetrieveSMContext
 Request请求SM上下文。SMF+PGW-C发送PFCP Session Modification Request
给UPF+PGW-U，为每个EPS承载建立CN隧道，并且提供EPS承载上下文给AMF。
AMF对TAU请求消息进行完整性校验，并通过Nsmf_PDUSession_Context Request携带映射后的EPS Bearer context请求PGW提供SM上下文，AMF向SMF提供目标MME能力。本步骤是与3GPP接入的并分配了EBI的UE的所有PDU会话对应的SMF+PGW-C都进行的。在本步骤中，如果AMF正确验证了UE，则AMF启动定时器。 
I-SMF返回映射后的EPS承载上下文，包括PDU会话对应的PDN连接的PGW-C控制面隧道信息、每个EPS承载的EBI、每个EPS承载的PGW-U隧道信息、每个EPS承载的EPS QoS参数。 
AMF向MME返回Context Response
消息，携带映射的MM上下文（包含映射的安全上下文），SM EPS UE上下文（包含缺省承载和专有GBR承载）。
MME根据本地策略等决策是否进行鉴权过程，与4G中TAU鉴权过程一致。 
创建EPS上下文
MME向AMF发送Context Acknowledge
消息，消息中包含Cause和SGW Change Indication。
MME根据Context Response
消息中各PDN Connection的PGW-C Node Name信息，优选与其中某一个PGW-C合建的SGW-C，向选中的SGW-C发送Create Session Request消息。SGW-C根据TAI、DNN等因素为每个PDN Connection选择作为SGW-U的UPF，并向该UPF发送PFCP Session Establishment Request消息。该消息中，为PDN Connection中的每个EPS Bearer建立Uplink和Downlink方向的PDR，并分配不同的SGW-U S1-U接口的F-TEID用于上行数据转发，SGW-U S5/S8-U接口的F-TEID用于下行数据转发。
SGW-C向PGW-C发送Modify Bearer Request消息，通知SGW-C的S5/S8-C接口的F-TEID，以及SGW-U S5/S8-U接口的F-TEID。SMF+PGW-C根据PCF+PCRF之前下发的Policy Control Request Trigger，向PCF+PCRF上报RAT变化、UE位置变化等事件。PCF+PCRF下发更新后的策略。更新后的策略如果需要触发EPS Bearer操作，如承载激活、修改、删除等，在[步骤19](1600153575794.html#zd2652df5029f4accaf0deeab04032552__59866237-2e01-417e-a0e8-4e0cb74d2d1b)中执行。
PGW-C通知UPF+PGW-U将Downlink数据隧道切换到SGW-U。 
PGW-C向SGW-C返回Modify Bearer Response消息，该消息中主要包含各EPS Bearer的Charging ID信息。 
（可选）PGW-C+A-SMF向PCF+PCRF获取策略信息。 
SGW-C向MME返回Create Session Reponse消息，其中包含了每个EPS Bearer的SGW-U S1-U接口F-TEID信息。 
MME向UDM+HSS发送Update Location Reqeust消息，该消息中双注册标识被置0或不携带。 
收尾阶段
UDM+HSS调用Nudm_UEContextManagement_DeregistrationNotification
 service operation，其中的DeregistrationData的DeregistrationReason为“5GS_TO_EPS_MOBILITY”。AMF在删除UE上下文时，调用Nudm_SubscriberDataManagement_Unsubscribe
服务操作，取消对UE签约数据的变更订阅。AMF资源保护定时器超时通知I-SMF释放。
UDM+HSS向MME返回Update Location Ack消息。 
MME向UE发送TAU Accept消息，如果TAU Request消息中的Active Flag置位，则TAU Accept消息被携带在S1AP-MME接口的Initial Context Setup Request消息中发送给eNodeB。Initial Context Setup Request消息中包含了待建立的E-RAB信息。 
（可选）如果新分配了4G-GUTI，UE向MME返回TAU Complete消息。 
（可选）PCF+PCRF可能因为RAT变化发起专有承载建立/修改/删除流程，通过发起这些流程将相关修改同步给UE。 
##### 空闲态下基于N26接口，4G跨系统移动到5G进行注册更新 
空闲态下基于N26接口，4G跨系统移动到5G进行注册更新的流程如[图1](1600153589845.html#z3f8b33d06aef4c6b8c309338554edeff__4ec46fac-8f72-4780-bbf1-b49440c85bca)所示。
图1  4G到5G的注册更新
[]images/1603962216759.png)
流程说明如下： 
UE触发注册流程。 
获取EPS上下文
UE向NR发起注册请求Registration Request
。
（可选）如果在AN消息中未携带5G-S-TMSI or GUAMI，或者携带的5G-S-TMSI or GUAMI不能指示一个合法的AMF时，NG-RAN根据RAT和请求的网络切片标识（NSSAI）选择AMF。如果NG-RAN不能选择合适的AMF，则将注册请求转发给NG-RAN中已配置的AMF进行AMF选择。 
NG-RAN将Registration Request
消息转发给AMF。消息中包括N2参数、注册消息、UE的接入选择和PDU会话选择信息以及UE上下文请求。
AMF与MME交互。 
AMF发送Context Request
给源MME，携带4G-GUTI、TAU请求。
MME对TAU Request进行完整性校验，校验通过后回复Context Response
。
（可选）如果UE在注册请求消息中携带了5G-GUTI(5G-GUTI as Additional GUTI)，则Target AMF发送消息给Old AMF。Old AMF对注册请求消息进行完整性保护检查，如果通过，则给Target AMF返回UE的SUPI、MM Context等信息。 
AMF完成对UE的安全过程。 
AMF向MME返回Context Acknowledge
消息，携带Serving GW change indication等信息。
AMF重建会话
（可选）如果AMF接受为UE服务，则AMF向MME发送上下文确认。 
（可选）如果需对UE进行设备检查，则AMF完成对UE的Equipmet ID检查过程。 
AMF选择合适的UDM，向其发起注册过程。 
AMF向UDM注册时，通过不携带双注册标识或携带的双注册标识为0，告知UDM保留AMF或者MME的单注册。 
AMF执行PCF选择过程，并向PCF获取移动性策略。 
AMF判断UE当前所在TA不在PGW-C+SMF的服务区域，决策插入I-SMF，调用Nsmf_PDUSession_CreateSMContext
请求，消息关键字段：interworking S-NSSAI、pduSessionsActivateList（指示在注册请求消息中接收到的所有需要重新激活的PDU会话表）、ueEpsPdnConnection、hoState（PREPARING）、smfUri、epsBearerCtxStatus，UpCnxState（不带DNN、pduSessionID、requestType、hostate、N1SmMsg）。
I-SMF判断不带requestType、HoState、N2消息，UeEpsPdnConnection则认为是4G到5G IDLE态移动性流程，根据smfUri判断是I-SMF角色，创建本地N3、N9隧道信息。 
I-SMF发送Nsmf_PDUSession_CreateSMContext
 Request消息给A-SMF+PGW-C，携带CN隧道信息以及epsBearerIds、pgwS8cFteid、epsBearerCtxStatus（不带requestType、sNssai）。
SMF+PGW-C首先根据PdnConnectionConnection找到关联的会话，检查epsBearerCtxStatus，发现如果有承载已被UE删除未通知网络侧，则本地释放这些EPS承载以及相应的5G QoS，随后发起N4会话更新，准备N9隧道信息， 
A-SMF返回Nsmf_PDUSession_CreateSMContext
 Response给I-SMF，携带 pduSessionID，the allocated EBI(s) information, S-NSAI, UE EPS PDN connection(s), 以及PDU Session Type, Session AMBR等会话参数。
I-SMF把pdusessionid更新到上下文索引里面，返回Nsmf_PDUSession_CreateSMContext
响应给AMF，携带本地N3隧道，以及从aSMF接收到的pduSessionID、snssai等信息。如果pdusessionid在pduSessionsActivateList里，还需要携带N2消息。
I-SMF通过PFCP Session Modification Request
/PFCP Session Modification Response
下发N4 Modification过程，把aSMF的N9隧道携带给I-UPF。
SMF发起向PCFSM策略关联修改过程。 
（可选）如果AMF下发upCnxState指示，需要激活用户面，则执行此步骤。 
NG-RAN向AMF发起N2 Setup Request请求。 
AMF向I-SMF发送Nsmf_PDUSession_UpdateSMContext
 Request请求。
I-SMF向I-UPF发起PFCP Session Establishment Request
请求。
I-UPF向I-SMF返回PFCP Session Establishment Response
响应。
I-SMF向AMF返回Nsmf_PDUSession_UpdateSMContext
 Response响应。
AMF向NG-RAN返回N2 Setup Response响应。 
删除4G侧资源
UDM+HSS向MME发送类型为“MME_UPDATE_PROCEDURE”的Cancel Location消息，MME收到该消息后释放UE Context和SGW-C上的EPS Bearer资源。 
MME发送给SGW-C的Delete Session Request消息中OI标识为0，SGW-C释放SGW-U上的EPS Bearer资源。 
注册成功，AMF给UE发送注册成功消息。 
UE向Old AMF发送注册完成消息。 
### 安全管理 
#### 鉴权 
本节包括如下流程： 
5G AKA鉴权 
EAP-AKA'鉴权 
同4G鉴权一样，5G鉴权支持UE和网络侧的双向认证。同时，5G统一了3GPP和非3GPP的鉴权方式，支持5G AKA和EAP-AKA‘两种鉴权方式。 
当UE触发注册、业务请求等流程时，若AMF安全校验失败或者AMF配置强制鉴权，则触发鉴权流程。采用的鉴权方式由AUSF根据用户签约或配置确定。 
##### 5G AKA鉴权 
5G AKA为4G鉴权EPS AKA的演进，增加了归属网络对于服务网络的认证。完整的5G AKA鉴权流程如[图1](1598961474723.html#z18282a75705b4bdf9deb950a676cc681__eab6f501-ec7b-40ac-97c7-7c7c14d0176f)所示。
图1  5G AKA鉴权
[]images/5GAKA%E9%89%B4%E6%9D%83.png)
流程说明如下： 
UE触发注册、业务请求，或者去注册请求等NAS请求消息给AMF，携带5G GUTI或者SUCI。 
（可选）若NAS请求消息中携带5G GUTI，但AMF根据5G GUTI查找用户上下文失败，则向UE发送Identity
Request
，请求用户标识。
（可选）UE回复Identity Response
，携带SUCI。
AMF校验NAS请求消息失败，或者AMF开启强制鉴权，则启动鉴权流程，发送Nausf_UEAuthentication_Authenticate
Request给AUSF，携带SUCI或者SUPI，以及服务网络名称。 
AUSF发送Nudm_UEAuthentication_Get
 Request给UDM，携带SUCI或者SUPI，以及服务网络名称。

若请求消息携带SUCI，UDM解密SUCI得到SUPI。 
UDM根据用户签约或者本地配置，确定鉴权方式为5G AKA。 

UDM生成5G HE AV，其中包含RAND、AUTN、XRES*以及Kausf，回复Nudm_UEAuthentication_Get
 Response给AUSF，携带生成的5G HE AV，并在响应中指示选择的鉴权方式为5G AKA。同时若AUSF在步骤4中携带了SUCI，则响应消息中还携带SUPI给AUSF。
AUSF保存XRES*，并根据XRES*计算HXRES*，根据Kausf计算并保存Kseaf。 

AUSF回复Nausf_UEAuthentication_Authenticate Response给AMF，携带5G
SE AV，其中包括RAND、AUTN以及HXRES*。 
AMF发送Authentication Request
给UE，携带RAND、AUTN、ABBA、ngKSI等参数。
UE校验AUTN，包括AUTN中的MAC、序列号等，完成对网络侧的校验后，计算RES*。 
UE回复Authentication Response
，携带RES*。
AMF根据RES*计算HRES*，并和从AUSF获取的HXRES*进行比较，一致则认为UE合法，完成对于网络侧对终端的校验。 
AMF校验UE合法后，发送Nausf_UEAuthentication_Authenticate Request给AUSF，携带UE返回的RES*。 
AUSF执行RES*的校验，比如比较RES*与本地保存的XRES*是否一致。 

AUSF回复Nausf_UEAuthentication_Authenticate Response给AMF，携带最终的鉴权结果。若鉴权结果为成功，响应消息中携带Kseaf。若步骤4中携带SUCI，则响应消息中携带SUPI。 
##### EAP-AKA'鉴权 
EAP-AKA'鉴权方式中，网络侧鉴权功能由AUSF负责，AMF只参与AUSF和UE之间鉴权信息的传递，以及最终KAMF密钥的推演。完整的EAP-AKA‘认证流程如[图2](1598961474723.html#z18282a75705b4bdf9deb950a676cc681__db6810ae-06c8-490f-96a2-10be343a49e4)所示。
图2  EAP-AKA'鉴权
[]images/5GAKA%E2%80%98%E9%89%B4%E6%9D%83.png)
流程说明如下： 
UE触发注册、业务请求，或者去注册请求等NAS请求消息给AMF，携带5G GUTI或者SUCI。 
若NAS请求消息中携带5G GUTI，但AMF根据5G GUTI查找用户上下文失败，则向UE发送Identity Request
，请求用户标识。
UE回复Identity Response
，携带SUCI。
AMF校验NAS请求消息失败，或者AMF开启强制鉴权，则启动鉴权流程，发送Nausf_UEAuthentication_Authenticate
Request给AUSF，携带SUCI或者SUPI，以及服务网络名称。 
AUSF发送Nudm_UEAuthentication_Get
 Request给UDM，携带SUCI或者SUPI，以及服务网络名称。
若请求消息携带SUCI，UDM解密SUCI得到SUPI。 
UDM根据用户签约或者本地配置，确定鉴权方式为EAP-AKA’。 
UDM生成EAP-AKA'  AV，包含RAND、AUTN、XRES、CK'以及IK'，并在Nudm_UEAuthentication_Get

Response中携带给AUSF，同时响应中指示选择的鉴权方式为EAP-AKA'。另外，若AUSF在步骤4中携带了SUCI，则响应消息中还携带SUPI给AUSF。
AUSF回复Nausf_UEAuthentication_Authenticate Response，携带EAP Request/AKA'-Challenge。 
AMF通过Authentication Request
，将EAP Request/AKA'-Challenge透传给UE，同时请求消息携带ABBA、ngKSI等参数。
UE校验EAP Request/AKA'-Challenge的AUTN，包括MAC、序列号等信息，完成对网络侧的鉴权，校验通过后，计算鉴权响应RES*。 
UE回复Authentication Response
，携带EAP Response/AKA'-Challenge。
AMF通过Nausf_UEAuthentication_Authenticate Request，透传UE侧的EAP
Response/AKA'-Challenge给AUSF。 
AUSF校验鉴权响应，完成网络侧对于UE的鉴权。校验通过后，AUSF根据CK’和IK‘推演EMSK，并将EMSK的高256比特位作为Kausf，继续推演得到Kseaf。 
AUSF回复Nausf_UEAuthentication_Authenticate Response，携带EAP Success，Kseaf。若步骤4中携带SUCI，则响应消息中携带SUPI。 
AMF通过N1消息将EAP Success透传给UE，EAP-AKA'鉴权完成。 
#### NAS安全算法协商 
概述 :NAS安全算法协商，在UE和AMF之间协商用于NAS消息加密的算法，以及用于NAS消息完整性保护的算法，适用如下场景： 
用户生成新的安全密钥，比如执行了鉴权过程，导致原有协商的安全算法已不支持。 
用户支持的安全算法发生变化，导致原有协商的安全算法已不支持。 
AMF支持的安全算法发生变化，导致原有协商的安全算法已不支持。 
##### 流程描述 
当原有协商的安全算法已不适用，则触发算法协商流程。算法协商流程如[图1](1598961480754.html#zfa2b542a3d6d4458a7876c63109c2bde__7d0879ce-96ad-4bf2-b308-c060acb171ed)所示。
图1  NAS安全算法协商流程
[]images/1599115805881.png)
流程说明如下： 
AMF根据UE安全能力中指示UE所支持的安全算法，AMF本地配置所支持的安全算法，以及本地配置的各个安全算法的优先级，分别为加密和完整性保护，协商一个安全算法，并发送Security Mode Command
消息到UE，消息中携带协商的安全算法，UE安全能力等，用于UE与本地的UE安全能力进行校验，防止被降维攻击。AMF在发送消息之前，采用新协商的完整性保护算法，对该NAS消息进行完整性保护。
UE执行Security Mode Command
消息的完整性校验，以及UE安全能力校验，校验通过后回复Security Mode Complete
消息，该消息使用新协商的算法进行加密和完整性保护。
 说明： 
安全算法协商完成后 ，后续无论上行NAS消息，还是下行NAS消息，都可以启用加密和完整性保护。 
#### 5G用户临时标识分配 
概述 :同4G一样，5G也支持为用户分配临时标识5G GUTI，用于后续终端与核心网交互时标识用户。5G
GUTI包含GUAMI和5G-TMSI两部分，GUAMI用于标识5G GUTI归属哪个AMF，5G-TMSI用于AMF标识用户。为了支持用户在4G/5G之间移动，4G
GUTI与5G GUTI之间需要相互转化，转化规则如[图1](1598961484484.html#zc7dabdd5a1a642eb94758f68c154df60__%E8%BD%AC%E5%8C%96%E8%A7%84%E5%88%99-48C1B235)所示。
图1  转化规则
[]images/1599125911113.png)
##### 流程描述 
当用户注册时，AMF根据本地策略，为用户分配5G GUTI，Registration
Accept
消息携带5G GUTI并通知到UE。具体流程如[图2](1598961484484.html#zc7dabdd5a1a642eb94758f68c154df60__aa946224-82d5-476c-9a98-32eae54553c5)所示。
图2  5G用户临时标识分配流程
[]images/1599115773669.png)
流程说明如下： 
UE发送Registration Request
消息触发注册请求，携带注册类型、SUCI或5G GUTI。
AMF根据本地策略决策是否分配新的5G GUTI，比如SUCI注册或者注册类型为初始注册时必须分配5G GUTI、周期性注册根据本地配置决策是否分配新的5G
GUTI。 
AMF下发Registration Accept
消息时，携带新分配的5G GUTI。
UE收到携带5G GUTI的Registration Accept
消息，必须回复Registration Complete
消息给AMF，通知AMF确认UE已经收到新分配的5G
GUTI。
### 控制面和用户面协作 
#### 节点管理 
本节包括以下流程： 
节点关联建立 
节点关联更新 
节点关联关系删除 
节点检测 
UPF选择 
##### 节点关联建立 
UPF发起的节点关联建立流程如[图1](22.html#T_1554257199554__UPF%E5%8F%91%E8%B5%B7%E8%8A%82%E7%82%B9%E5%85%B3%E8%81%94%E5%BB%BA%E7%AB%8B%E6%B5%81%E7%A8%8B%E7%A4%BA%E6%84%8F%E5%9B%BE-47D9CBF4)所示。
图1  UPF发起节点关联建立流程示意图
[]images/UPF%E5%8F%91%E8%B5%B7%E8%8A%82%E7%82%B9%E5%85%B3%E8%81%94%E5%BB%BA%E7%AB%8B.png)
流程说明如下： 
UPF向SMF发送PFCP Association Setup Request
消息请求关联建立，消息中携带UPF的Node ID、UPF能力、UPF N3/N9口的GTPU地址与UPF可支持的TEID范围。
SMF向UPF发送PFCP Association Setup Response
响应消息，消息中携带SMF的能力。
##### 节点关联更新 
UPF发起的节点关联更新流程如[图2](22.html#T_1554257199554__UPF%E5%8F%91%E8%B5%B7%E8%8A%82%E7%82%B9%E5%85%B3%E8%81%94%E6%9B%B4%E6%96%B0%E6%B5%81%E7%A8%8B%E7%A4%BA%E6%84%8F%E5%9B%BE-47D9CE3E)所示。
图2  UPF发起节点关联更新流程示意图
[]images/UPF%E5%8F%91%E8%B5%B7%E8%8A%82%E7%82%B9%E5%85%B3%E8%81%94%E6%9B%B4%E6%96%B0.png)
流程说明如下： 
UPF向SMF发送PFCP Association Update Request
消息请求关联更新，消息中携带UPF的Node ID、UPF能力，可能携带UPF N3/N9口的GTPU地址与UPF可支持的TEID范围。
SMF向UPF发送PFCP Association Update Response
响应消息。
##### 节点关联关系删除 
节点关联关系删除流程如[图3](22.html#T_1554257199554__%E8%8A%82%E7%82%B9%E5%85%B3%E8%81%94%E5%85%B3%E7%B3%BB%E5%88%A0%E9%99%A4%E6%B5%81%E7%A8%8B%E7%A4%BA%E6%84%8F%E5%9B%BE-47D9D066)所示。
图3  节点关联关系删除流程示意图
[]images/%E8%8A%82%E7%82%B9%E5%85%B3%E8%81%94%E5%88%A0%E9%99%A4.png)
流程说明如下： 
UPF收到OAM发来的释放消息，给SMF发送PFCP Association Update Request
消息，通知SMF需要进行关联关系的删除操作，同时携带优雅退出时长T。
SMF回复PFCP Association Update Response
消息，同时开启定时器，设置超时时间为T。
定时器到期后，SMF向UPF发送PFCP Association Release Request
消息请求删除节点关联关系。
UPF收到请求消息后，释放相关会话、删除该SMF的关联关系，并且向SMF发送PFCP Association Release Response
响应消息。
SMF收到响应消息后，会释放相关会话、删除关联关系。 
##### 节点检测 
UPF发起的节点检测流程如[图4](22.html#T_1554257199554__%E8%8A%82%E7%82%B9%E6%A3%80%E6%B5%8B-AF91832C)所示。
图4  节点检测
[]images/%E8%8A%82%E7%82%B9%E6%A3%80%E6%B5%8B.png)
流程说明如下： 
UPF向SMF发送PFCP Heartbeat Request
心跳检测消息。
SMF向UPF返回PFCP Heartbeat Response
消息。
如果UPF在配置的重发次数范围内未收到PFCP Heartbeat Response
心跳响应，UPF会删除与该SMF的节点关联，并释放相关会话。
##### UPF选择 
UPF选择的业务流程如[图5](22.html#T_1554257199554__%E6%A0%B9%E6%8D%AEDNN%E9%80%89%E6%8B%A9UPF-B117B48E)所示。
图5  根据DNN或负荷选择UPF
[]images/%E6%A0%B9%E6%8D%AEDNN%E9%80%89%E6%8B%A9UPF.png)
流程说明如下： 
UPF上电成功后向SMF发起PFCP Association Setup Request
消息请求关联注册，在请求消息中携带支持的DNN。
UE发起PDU会话建立流程。 
SMF根据UPF所支持的DNN，选择UPF。若有多个UPF符合，则SMF根据UPF的负荷情况进行选择。 
SMF完成PDU会话建立的后续流程。 
根据TAC以及其它参数的选择流程是一样的，只是UM的决策顺序及权重有差异。 
#### 用户交互 
##### PFCP连接处理 
本节包括以下流程： 
SMF发起N4连接建立流程 
UPF发起N4连接建立流程 
SMF发起N4连接更新流程 
UPF发起N4连接更新流程 
SMF发起的N4连接释放流程 
UPF发起的N4连接释放流程 
###### SMF发起N4连接建立流程 
SMF发起N4连接建立流程如[图1](25.html#T_1554257199554__09e75a63-41bc-4de5-99e5-18ab08c7be12)所示。
图1  SMF发起N4连接建立流程
[]images/SMF%E5%8F%91%E8%B5%B7%E5%81%B6%E8%81%94%E5%BB%BA%E7%AB%8B.png)
流程说明如下： 
SMF向UPF发起N4连接建立请求消息（N4 Association Setup Request
），携带自己支持的特性和可用资源。
UPF向SMF回复N4连接建立应答消息（N4 Association Setup Response
），携带自己支持的特性和可用资源。
###### UPF发起N4连接建立流程 
UPF发起N4连接建立流程如[图2](25.html#T_1554257199554__dc83d045-43b0-4dba-a47b-30e5c04195c2)所示。
图2  UPF发起N4连接建立流程
[]images/UPF%E5%8F%91%E8%B5%B7%E5%81%B6%E8%81%94%E5%BB%BA%E7%AB%8B.png)
流程说明如下： 
UPF向SMF发起N4连接建立请求消息（N4 Association Setup Request
），携带自己支持的特性和可用资源。
SMF向UPF回复N4连接建立应答消息（N4 Association Setup Response
），携带自己支持的特性和可用资源。
###### SMF发起N4连接更新流程 
SMF发起N4连接更新流程如[图3](25.html#T_1554257199554__2836c833-3f56-4b00-98d9-0a15eb41680b)所示。
图3  SMF发起N4连接更新流程
[]images/SMF%E5%8F%91%E8%B5%B7%E5%81%B6%E8%81%94%E6%9B%B4%E6%96%B0.png)
流程说明如下： 
当SMF需要更新自己支持的特性时，SMF向UPF发起N4连接更新请求消息（N4 Association Update Request
），携带自己支持的特性和可用资源。
UPF向SMF回复N4连接更新应答消息（N4 Association Update Response
），确认更新是否成功。
###### UPF发起N4连接更新流程 
UPF发起N4连接更新流程如[图4](25.html#T_1554257199554__bdfd16b2-968a-440d-b82d-34753f3e6551)所示。
图4  UPF发起的连接更新流程
[]images/UPF%E5%8F%91%E8%B5%B7%E5%81%B6%E8%81%94%E6%9B%B4%E6%96%B0.png)
流程说明如下： 
当UPF需要更新自己支持的特性或用户面IP资源时，UPF向SMF发起N4连接更新请求消息（N4 Association Update Request
），携带自己支持的特性和可用资源。
SMF向UPF回复N4连接更新应答消息（N4 Association Update Response
），确认更新是否成功。
###### SMF发起的N4连接释放流程 
SMF发起的N4连接释放流程如[图5](25.html#T_1554257199554__1e051bf6-63ea-4efc-9c51-a4e8cbf4de9b)所示。
图5  SMF发起的N4连接释放流程
[]images/SMF%E5%8F%91%E8%B5%B7%E5%81%B6%E8%81%94%E9%87%8A%E6%94%BE.png)
流程说明如下： 
当SMF需要终结N4连接时（比如OAM，异常等），SMF向UPF发起N4连接释放请求消息（N4 Association Release Request
）。
UPF释放相关资源，并向SMF回复N4连接释放应答消息（N4 Association Release Response
）。
###### UPF发起的N4连接释放流程 
UPF发起的N4连接释放流程如[图6](25.html#T_1554257199554__28ae7975-9680-42c6-8cc4-e484cac3a52b)所示。
图6  UPF发起的N4连接释放流程
[]images/UPF%E5%8F%91%E8%B5%B7%E5%81%B6%E8%81%94%E9%87%8A%E6%94%BE.png)
流程说明如下： 
当需要终结N4连接时（比如OAM，异常等），UPF发起释放流程，UPF发起N4连接更新请求消息（N4 Association Update Request
），携带优雅退出时长。
SMF回复N4连接更新应答消息（N4 Association Update Response
），并开始释放资源。
SMF向UPF发起N4连接释放消息（N4 Association Release Request
）。
UPF释放相关资源，并向SMF回复N4连接释放应答消息（N4 Association Release Response
）。
##### PFCP会话处理 
本节包括以下流程： 
N4会话建立流程 
N4会话修改流程 
N4会话删除流程 
###### N4会话建立流程 
N4会话建立流程如[图1](26.html#T_1554257199554__a0088d7f-e64b-4411-965b-1dc8f15477c6)所示。
图1  N4会话建立流程
[]images/%E4%BC%9A%E8%AF%9D%E5%BB%BA%E7%AB%8B%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
触发请求方（比如AMF或PCF）触发SMF建立一个新的PDU会话或对后续的PDU会话重分配PDU会话。
SMF向UPF下发N4会话建立请求消息（N4 Session Establishment Request
），携带结构化的控制信息。
UPF创建N4会话上下文，并回复应答消息（N4 Session Establishment Response
），在应答消息中携带需要回复给SMF的控制信息。
SMF与触发请求方交互（比如AMF或PCF）。
###### N4会话修改流程 
N4会话修改流程如[图2](26.html#T_1554257199554__e53bf2b4-052a-40c3-ab14-c8e3ed4de0f9)所示。
图2  N4会话修改流程
[]images/%E4%BC%9A%E8%AF%9D%E6%9B%B4%E6%96%B0%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
触发请求方（比如AMF或PCF）触发SMF修改一个PDU会话。 
SMF向UPF下发N4会话修改请求消息（N4 Session Modification Request
），携带结构化的控制信息。
UPF验证会话ID，更新N4会话上下文的参数，并回复应答消息（N4 Session Modification Response
），在应答消息中携带需要回复给SMF的控制信息。
SMF与触发请求方交互（比如AMF或PCF）。
###### N4会话删除流程 
N4会话删除流程如[图3](26.html#T_1554257199554__de338d69-7d88-45d0-8ddb-93cc883692f7)所示。
图3  N4会话删除流程
[]images/%E4%BC%9A%E8%AF%9D%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
触发请求方（比如AMF或PCF）触发SMF释放一个PDU会话。
SMF向UPF下发N4会话释放请求消息（N4 Session Release Request）。 
UPF验证会话ID，删除N4会话上下文，并回复应答消息（N4 Session Release Response），在应答消息中携带用量信息给SMF。 
SMF与触发请求方交互（比如AMF或PCF）。
##### 报文转发 
报文转发的业务流程图如[图1](27.html#T_1554257199554__fb6b6c9f-5f28-4336-8e60-cd872d354ab9)所示。
图1  报文转发
[]images/%E6%8A%A5%E6%96%87%E8%BD%AC%E5%8F%91.png)
流程说明如下： 
UPF收到报文后，根据隧道信息或UE IP查找PFCP会话上下文。
UPF找到上下文后，根据L3/4或L7信息，按优先级依次匹配PDR。
UPF匹配到优先级最高的PDR后，依次执行其所关联的QER(s)、URR(s)和FAR。
UPF根据FAR规则，指定流量转向、隧道封装等操作。 
UPF根据QER规则，执行QoS策略、门控等操作。 
UPF根据URR规则，执行用量统计操作，并按门限定时定量上报用量统计。 
UPF发送报文。 
##### 用量上报 
用量上报流程图如[图1](28.html#T_1554257199554__7c34440f-a7db-4764-b056-87950a400473)所示。
图1  用量上报流程图
[]images/%E7%94%A8%E9%87%8F%E4%B8%8A%E6%8A%A5%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
UPF探测到事件门限、用量门限或某个事件，触发用量上报。 
UPF向SMF发送N4会话用量上报消息，携带触发条件和具体的用量。 
SMF验证会话ID，找到对应的N4会话上下文，汇聚用量，实现计费、用量监控等功能。 
##### 缓存 
本节包括以下流程： 
SMF缓存流程 
UPF缓存流程 
GW-C缓存流程 
GW-U缓存流程 
###### SMF缓存流程 
配置下行报文缓存在SMF时，流程如[图1](29.html#T_1554257199554__6c06ac48-42cd-41d9-b71a-0b609c0a78ce)所示。
图1  SMF缓存流程
[]images/SMF%E7%BC%93%E5%AD%98%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
UE进入IDLE态，去活PDU会话。 
SMF发送N4会话修改请求（N4 Session Modification Request
）消息给UPF，修改FAR，建立CP-UP通道。
UPF回复N4会话修改应答（N4 Session Modification Response
）消息。
UPF收到下行报文。 
UPF将报文通过CP-UP通道转发给SMF。 
SMF缓存报文。 
用户重新附着，SMF激活PDU会话。 
SMF开始发送还在缓存周期内的报文，缓存周期可在本地配置或由PCF下发。 
SMF将报文通过CP-UP通道转发给UPF。 
UPF将下行报文发送给UE。 
报文发送结束后，SMF发送N4会话修改请求（N4 Session Modification Request
）消息给UPF，修改FAR，删除CP-UP通道。
UPF回复N4会话修改应答（N4 Session Modification Response
）消息。
###### UPF缓存流程 
配置下行报文缓存在UPF时，流程如[图2](29.html#T_1554257199554__d1e60066-6291-493b-b3f1-102cd7a3431e)所示。
图2  UPF缓存流程
[]images/UPF%E7%BC%93%E5%AD%98%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
UE进入IDLE态，去活PDU会话。 
SMF发送N4会话修改请求（N4 Session Modification Request
）消息给UPF，修改FAR，通知UPF缓存报文以及相应的缓存周期。
UPF回复N4会话修改应答（N4 Session Modification Response
）消息。
UPF收到下行报文。 
UPF缓存报文。 
用户重新附着，SMF激活PDU会话。 
SMF发送N4会话修改请求（N4 Session Modification Request
）消息给UPF，修改FAR，通知UPF发送缓存的报文。
UPF回复N4会话修改应答（N4 Session Modification Response
）消息。
UPF开始发送还在缓存周期内的报文。 
UPF将下行报文发送给UE。 
###### GW-C缓存流程 
配置下行报文缓存在GW-C时，流程如[图3](29.html#T_1554257199554__9647cd95-2d9f-4726-999b-39cff7cf4979)所示。
图3  GW-C缓存流程
[]images/GW-C%E7%BC%93%E5%AD%98%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
UE进入IDLE态，去活PDN连接。 
GW-C发送Sx会话修改请求（Sx Session Modification Request）消息给GW-U，修改FAR，建立CP-UP通道。
GW-U回复Sx会话修改应答（Sx Session Modification Response）消息。 
GW-U收到下行报文。 
GW-U将报文通过CP-UP通道转发给GW-C。 
GW-C缓存报文。 
用户重新附着，GW-C激活PDN连接。 
GW-C开始发送还在缓存周期内的报文，缓存周期可在本地配置或由PCRF下发。 
GW-C将报文通过CP-UP通道转发给GW-U。 
GW-U将下行报文发送给UE。 
报文发送结束后，GW-C发送Sx会话修改请求（Sx Session Modification Request）消息给GW-U，修改FAR，删除CP-UP通道。
GW-U回复Sx会话修改应答（Sx Session Modification Response）消息。 
###### GW-U缓存流程 
配置下行报文缓存在GW-U时，流程如[图4](29.html#T_1554257199554__b615b453-340f-4759-81e6-9ec59c375f98)所示。
图4  GW-U缓存流程
[]images/GW-U%E7%BC%93%E5%AD%98%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
UE进入IDLE态，去活PDN连接。 
GW-C发送Sx会话修改请求（Sx Session Modification Request）消息给GW-U，修改FAR，通知GW-U缓存报文以及相应的缓存周期。
GW-U回复Sx会话修改应答（Sx Session Modification Response）消息。 
GW-U收到下行报文。 
GW-U缓存报文。 
用户重新附着，GW-C激活PDN连接。 
GW-C发送Sx会话修改请求（Sx Session Modification Request）消息给GW-U，修改FAR，通知GW-U发送缓存的报文。
GW-U回复Sx会话修改应答（Sx Session Modification Response）消息。 
GW-U开始发送还在缓存周期内的报文。 
GW-U将下行报文发送给UE。 
##### QoS执行 
本节包括以下流程： 
QoS执行 
门控 
###### QoS执行 
QoS流程包括以下业务流程： 
SMF和UPF之间的QoS执行流程 
GW-C和GW-U之间的QoS执行流程 
SMF和UPF之间的QoS执行流程
SMF和UPF之间的QoS执行流程如[图1](30.html#T_1554257199554__1430c81f-1b03-4b42-9048-1d5a68ec858e)所示。
图1  QoS执行流程
[]images/QoS%E6%89%A7%E8%A1%8C%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
AMF或PCF触发SMF发起PDU会话建立/修改流程。
SMF向UPF发送N4会话建立/修改请求（N4 Session Establishment Request
/Session Modification Request
）消息，下发QoS策略，通过PDR区分策略是会话级、承载级、QoS Flow级还是业务/应用级QoS。
UPF向SMF回复N4会话建立/修改应答（N4 Session Establishment Response
/Session Modification Response
）消息。
UPF收到报文，匹配PDR，选择相应级别的QoS策略，执行QoS策略。 
GW-C和GW-U之间的QoS执行流程
GW-C和GW-U之间的QoS执行流程如[图2](30.html#T_1554257199554__e099d089-7063-42c9-ad49-9d4c429b9db5)所示。
图2  QoS执行流程
[]images/QoS%E6%89%A7%E8%A1%8C%E6%B5%81%E7%A8%8B2.png)
流程说明如下： 
MME或PCRF触发GW-C发起PDN连接建立/修改流程。 
GW-C向GW-U发送Sx会话建立/修改请求（Sx Session Establishment/Modification Request）消息，下发QoS策略，通过PDR区分策略是会话级、承载级还是业务/应用级QoS。
GW-U向GW-C回复Sx会话建立/修改应答（Sx Session Establishment/Modification Response）消息。 
GW-U收到报文，匹配PDR，选择相应级别的QoS策略，执行QoS策略。 
###### 门控 
门控流程包括以下业务流程： 
SMF和UPF之间的门控流程 
GW-C和GW-U之间的门控流程 
SMF和UPF之间的门控流程
SMF和UPF之间的门控流程如[图3](30.html#T_1554257199554__b4c32540-d966-4e27-9bbb-f5696d7b10ee)所示。
图3  门控流程
[]images/%E9%97%A8%E6%8E%A7%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
AMF或PCF触发SMF发起PDU会话建立/修改流程。 
SMF向UPF发送N4会话建立/修改请求（N4 Session Establishment Request
/Session Modification Request
）消息，下发门控策略，通过PDR区分策略是会话级、承载级、QoS Flow级还是业务/应用级门控。
UPF向SMF回复N4会话建立/修改应答（N4 Session Establishment Response
/Session Modification Response
）消息。
UPF收到报文，匹配PDR，执行相应级别的门控策略。
GW-C和GW-U之间的门控流程
GW-C和GW-U之间的门控流程如[图4](30.html#T_1554257199554__bb309753-6d0b-4725-bf59-4281f3ed35fb)所示。
图4  门控流程
[]images/%E9%97%A8%E6%8E%A7%E6%B5%81%E7%A8%8B2.png)
流程说明如下： 
MME或PCRF触发GW-C发起PDN连接建立/修改流程。 
GW-C向GW-U发送Sx会话建立/修改请求（Sx Session Establishment/Modification Request）消息，下发门控策略，通过PDR区分策略是会话级、承载级还是业务/应用级门控。 
GW-U向GW-C回复Sx会话建立/修改应答（Sx Session Establishment/Modification Response）消息。 
GW-U收到报文，匹配PDR，执行相应级别的门控策略。
##### 策略与计费控制执行 
本节包括以下流程： 
策略下发流程 
策略更新流程 
###### 策略下发流程 
策略下发包括如下业务流程： 
SMF和UPF之间的策略下发 
GW-C和GW-U之间的策略下发 
SMF和UPF之间的策略下发
SMF和UPF之间的策略下发流程如[图1](31.html#T_1554257199554__87f56200-da2b-4ef4-b917-fb05aa8765bd)所示。
图1  SMF和UPF之间的策略下发流程
[]images/%E7%AD%96%E7%95%A5%E4%B8%8B%E5%8F%91%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
会话建立时，触发请求方（比如AMF或PCF）触发SMF建立或重定位一个PDU会话，消息中携带业务策略信息，包括业务匹配规则和策略执行规则。
SMF向UPF下发N4会话建立请求（N4 Session Establishment Request
）消息，携带业务策略信息。
UPF创建N4会话上下文，并回复N4会话建立应答（N4 Session Establishment Response
）消息。
SMF与触发请求方交互（比如AMF或PCF），触发下一步流程。
GW-C和GW-U之间的策略下发
GW-C和GW-U之间的策略下发流程如[图2](31.html#T_1554257199554__a55f79ed-ff7a-476b-a55d-7bf64a71022a)所示。
图2  GW-C和GW-U之间的策略下发流程
[]images/%E7%AD%96%E7%95%A5%E4%B8%8B%E5%8F%91%E6%B5%81%E7%A8%8B2.png)
流程说明如下： 
会话建立时，触发请求方（比如MME或PCRF）触发GW-C建立或重定位一个PDN连接，消息中携带业务策略信息，包括业务匹配规则和策略执行规则。 
GW-C向GW-U下发Sx会话建立请求（Sx Session Establishment Request）消息，携带业务策略信息。 
GW-U创建Sx会话上下文，并回复Sx会话建立应答（Sx Session Establishment Response）消息。 
GW-C与触发请求方交互（比如MME或PCRF），触发下一步流程。 
###### 策略更新流程 
策略更新包括如下业务流程： 
SMF和UPF之间的策略更新 
GW-C和GW-U之间的策略更新 
SMF和UPF之间的策略更新
SMF和UPF之间的策略更新流程如[图3](31.html#T_1554257199554__88def839-31aa-4c85-b2d9-57bcd5c97018)所示。
图3  SMF和UPF之间的策略更新流程
[]images/%E7%AD%96%E7%95%A5%E6%9B%B4%E6%96%B0%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
业务策略有变更，或有新的业务策略需要下发时，触发请求方（比如AMF或PCF）触发SMF下发PDU会话修改消息。
SMF向UPF下发N4会话修改请求（N4 Session Modification Request
）消息，携带业务策略信息。
UPF验证会话ID，更新N4会话上下文中的业务策略参数，并回复N4会话修改应答（N4 Session Modification Response
）消息。
SMF与触发请求方交互（比如AMF或PCF），触发下一步流程。
GW-C和GW-U之间的策略更新
GW-C和GW-U之间的策略更新流程如[图4](31.html#T_1554257199554__bc8ba6b6-16af-41bb-9a34-a8702e774208)所示。
图4  GW-C和GW-U之间的策略更新流程
[]images/%E7%AD%96%E7%95%A5%E6%9B%B4%E6%96%B0%E6%B5%81%E7%A8%8B2.png)
流程说明如下： 
业务策略有变更，或有新的业务策略需要下发时，触发请求方（比如MME或PCRF）触发GW-C下发PDN连接修改消息。 
GW-C向GW-U下发Sx会话修改请求（Sx Session Modification Request）消息，携带业务策略信息。 
GW-U验证会话ID，更新Sx会话上下文中的业务策略参数，并回复Sx会话修改应答（Sx Session Modification Response）消息。 
GW-C与触发请求方交互（比如MME或PCRF），触发下一步流程。 
### 策略控制 
#### PDU会话策略控制 
本节包括以下流程： 
SM策略关联建立流程 
SMF发起的SM策略关联修改流程 
PCF发起的SM策略关联修改流程 
SMF发起的SM策略关联终止流程 
PCF发起的SM策略关联终止流程 
##### SM策略关联建立流程 
SM策略关联建立流程如[图1](36.html#T_1554257199570__08b633d4-f7eb-403d-a1a4-40917a0c0b81)所示。
图1  SM策略关联建立流程
[]images/SM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E5%BB%BA%E7%AB%8B%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
在PDU会话建立流程中，如果SMF确定需要向PCF请求PDU会话策略控制，SMF需要先为该PDU会话向PCF请求建立SM策略关联。为此SMF向PCF发送Npcf_SMPolicyControl_Create
 Request请求，请求中包含SUPI、PDU会话标识、DNN、S-NSSAI、订阅通知指示（即SMF后续接收PCF为该SM策略关联下发的策略更新通知的URI地址），可选包含UE的IPv4地址和（或）IPv6地址前缀、GPSI、PEI、签约的会话聚合带宽（Subscribed Session AMBR）和签约的缺省QoS（Subscribed Default QoS）等信息。
如果PCF确定对该PDU会话策略控制需要用到该用户的策略签约信息，并且PCF本地没有该用户的策略签约信息，则PCF向UDR获取该用户的策略签约信息，并向UDR订阅该用户的策略签约信息变更通知。
如果PCF确定对该PDU会话策略控制需要用到该用户的消费门限信息，并且PCF本地没有该用户的消费门限信息，则PCF向CHF获取该用户的消费门限信息，并向CHF订阅该用户的消费门限信息变更通知。
PCF基于运营商配置的策略规则和各NF的输入信息进行策略决策，生成SM策略，并确定需要为此SM策略关联向SMF订阅的事件。
PCF向SMF发送Npcf_SMPolicyControl_Create
 Response消息，其中包含PCF生成的SM策略关联ID、SM策略、订阅的事件列表。
##### SMF发起的SM策略关联修改流程 
SMF发起的SM策略关联修改流程如[图2](36.html#T_1554257199570__f967fea6-4b93-4301-b071-40cba4bd381d)所示。
图2  SM策略关联修改流程(SMF发起)
[]images/SM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E4%BF%AE%E6%94%B9%E6%B5%81%E7%A8%8B(SMF%E5%8F%91%E8%B5%B7).png)
流程说明如下： 
当PCF订阅的事件发生时（例如PCF向SMF订阅了PLMN change事件后，UE移动导致用户接入的PLMN发生了变化），SMF向PCF发送Npcf_SMPolicyControl_Update
 Request消息，携带SM策略关联ID、事件号及事件相关信息。
PCF重新进行策略决策，可能更新SM策略。 
如果此次流程中SMF上报了PDU会话的用量，则PCF累计出最新的用量（例如当月用户总流量），将其作为PCF动态生成且需持久保存的策略数据，更新到UDR，以便下次PDU会话建立时PCF能够从UDR取回再用于策略决策。 
PCF向SMF发送Npcf_SMPolicyControl_Update
 Response消息，如果PCF更新了SM策略，则将最新的SM策略包含在响应消息中。
##### PCF发起的SM策略关联修改流程 
PCF发起的SM策略关联修改流程如[图3](36.html#T_1554257199570__aaf344bc-2f9a-43cb-af62-0346612f330f)所示。
图3  SM策略关联修改流程(PCF发起)
[]images/SM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E4%BF%AE%E6%94%B9%E6%B5%81%E7%A8%8B(PCF%E5%8F%91%E8%B5%B7).png)
流程说明如下： 
PCF收到内部事件触发（如时段切换）或外部事件触发（如UDR通知PCF某用户的策略签约信息发生了变更）。 
PCF重新进行策略决策。 
如果PCF确定需要更新SM策略，则PCF向SMF发送Npcf_SMPolicyControl_UpdateNotify
消息，其中包含最新的SM策略。
SMF执行最新的SM策略，向PCF发送Npcf_SMPolicyControl_UpdateNotify
 Ack消息。
##### SMF发起的SM策略关联终止流程 
SMF发起的SM策略关联终止流程如[图4](36.html#T_1554257199570__75aee14b-afbf-4dc9-9f2b-d657d6c7df37)所示。
图4  SM策略关联终止流程(SMF发起)
[]images/SM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E7%BB%88%E6%AD%A2%E6%B5%81%E7%A8%8B(SMF%E5%8F%91%E8%B5%B7).png)
流程说明如下： 
在UE或SMF发起的PDU会话释放流程中，SMF查找到某PDU会话有相关的SM策略关联，向PCF发送Npcf_SMPolicyControl_Delete
 Request消息，请求PCF删除SM策略关联。请求中携带SM策略关联ID，可能还包含最后用量上报（即SM策略关联删除前SMF统计到用户已使用但SMF但还未上报的用量）。
PCF收到Npcf_SMPolicyControl_Delete
 Request消息后，如果发现其中有最后用量上报，需要更新到UDR。如果PCF确定此PDU会话结束后，PCF已不需要为该用户接收UDR策略签约变更通知，则PCF向UDR退订该用户的策略签约信息变更通知。
如果PCF确定此PDU会话结束后，PCF已不需要为该用户接收CHF消费门限信息变更通知，则PCF向CHF退订该用户的消费门限信息变更通知。
PCF向SMF发送Npcf_SMPolicyControl_Delete
 Response消息。
##### PCF发起的SM策略关联终止流程 
PCF发起的SM策略关联终止流程如[图5](36.html#T_1554257199570__2aa52711-64d8-4429-bdcd-80ca6344fb06)所示。
图5  SM策略关联终止流程(PCF发起)
[]images/SM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E7%BB%88%E6%AD%A2%E6%B5%81%E7%A8%8B(PCF%E5%8F%91%E8%B5%B7).png)
流程说明如下： 
PCF收到内部事件（如套餐过期）或外部事件（如UDR注销用户通知）。 
PCF进行策略决策，确定需要删除某个PDU会话的SM策略。 
PCF向SMF发送Npcf_SMPolicyControl_UpdateNotify
消息，其中包含SM策略关联删除指示。
SMF向PCF回复Npcf_SMPolicyControl_UpdateNotify
 Ack消息。
后续流程同[SMF发起的SM策略关联终止流程](36.html#T_1554257199570__e2bf2894-f83d-437a-bc2f-2a050dfc8194)。
#### 接入和移动性策略控制 
本节包含以下流程： 
AM策略关联建立流程 
AMF发起的AM策略关联修改流程 
PCF发起的AM策略关联修改流程 
AMF发起的AM策略关联终止流程 
PCF发起的AM策略关联终止流程 
##### AM策略关联建立流程 
AM策略关联建立流程如[图1](37.html#T_1554257199570__AM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E5%BB%BA%E7%AB%8B%E6%B5%81%E7%A8%8B-BF506F23)所示。
图1  AM策略关联建立流程
[]images/AM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E5%BB%BA%E7%AB%8B%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
在UE注册或切换到某个AMF的过程中，如果该AMF确定需要为该UE向PCF请求接入和移动性策略控制，该AMF需要向PCF请求建立AM策略关联。为此该AMF向PCF发送Npcf_AMPolicyControl_Create
 Request消息，请求中包含用户永久标识（SUPI）、订阅通知指示（NotificationURI，即AMF后续接收PCF为该AM策略关联下发的策略更新通知的URI地址）。
如果AMF从UDM获取了业务区域限制（Service
Area Restrictions）、无线/频率选择优先级索引（RFSP Index）、一般公共用户标识（GPSI）、允许的切片选择信息（the Allowed NSSAI），AMF也将这些信息包含在Npcf_AMPolicyControl_Create
 Request消息中。
AMF还可以在Npcf_AMPolicyControl_Create
 Request消息中包含接入方式（Access Type）、无线接入技术（RAT）、永久设备标识（PEI）、用户位置信息（ULI）、UE时区（UE Time Zone）等信息。
如果PCF确定对该UE的接入和移动性策略控制需要用到该用户的策略签约信息，并且PCF本地没有该用户的策略签约信息，则PCF向UDR获取该用户的策略签约信息，并向UDR订阅该用户的策略签约信息变更通知。
如果PCF确定对该UE的接入和移动性策略控制需要用到该用户的消费门限信息，并且PCF本地没有该用户的消费门限信息，则PCF向CHF获取该用户的消费门限信息，并向CHF订阅该用户的消费门限信息变更通知。
PCF基于运营商配置的策略规则及各NF提供的信息进行策略决策，生成AM策略，其中包含PCF授权的业务区域限制（Service
Area Restrictions）和RFSP Index；PCF同时还确定需要为此AM策略关联向AMF订阅的事件列表。
PCF向AMF发送Npcf_AMPolicyControl_Create
 Response消息，其中包含PCF生成的AM策略关联ID、AM策略、订阅的事件列表。
##### AMF发起的AM策略关联修改流程 
AMF发起的AM策略关联修改流程如[图2](37.html#T_1554257199570__4b280cd8-89c4-4217-8f1e-be9416baa37f)所示。
图2  AM策略关联修改流程（AMF发起）
[]images/1526880452149.png)
流程说明如下： 
当PCF订阅的事件发生时（如UDM通知AMF某用户签约的业务区域限制或RFSP
Index发生了改变），AMF向PCF发送Npcf_AMPolicyControl_Update
 Request消息，携带AM策略关联ID、事件号及事件相关信息。
PCF重新进行策略决策，可能更新AM策略。 
PCF向AMF发送Npcf_AMPolicyControl_Update
 Response消息，如果PCF更新了AM策略，则此响应消息中包含最新的AM策略。
##### PCF发起的AM策略关联修改流程 
PCF发起的AM策略关联修改流程如[图3](37.html#T_1554257199570__e1ba1692-cc5a-4026-a686-7fa2e2faec6f)所示。
图3  AM策略关联修改流程（PCF发起）
[]images/1526880537149.png)
流程说明如下： 
PCF收到内外部事件触发（内部事件例如时段变更通知，外部事件例如UDR策略签约信息变更通知）。 
PCF重新进行策略决策，确定需要调整某UE的AM策略。 
PCF向AMF发送Npcf_AMPolicyControl_UpdateNotify
消息，携带更新的AM策略。
AMF回复Npcf_AMPolicyControl_UpdateNotify
 Ack消息。
##### AMF发起的AM策略关联终止流程 
AMF发起的AM策略关联终止流程如[图4](37.html#T_1554257199570__AM%E7%AD%96%E7%95%A5%E5%85%B3%E8%81%94%E7%BB%88%E6%AD%A2%E6%B5%81%E7%A8%8BAMF%E5%8F%91%E8%B5%B7-BF507DBF)所示。
图4  AM策略关联终止流程(AMF发起)
[]images/1535335644136.png)
流程说明如下： 
在UE去注册流程中，或AMF重选伴随PCF重选流程中，源AMF需要向PCF终止AM策略关联。AMF向PCF发送Npcf_AMPolicyControl_Delete
 Request消息，携带AM策略关联ID。
如果PCF确定此AM策略关联结束后，PCF已不需要为该用户接收UDR策略签约变更通知，则PCF向UDR去订阅该用户的策略签约变更通知。 
如果PCF确定此AM策略关联结束后，PCF已不需要为该用户接收CHF消费门限信息变更通知，则PCF向CHF去订阅该用户的消费门限信息变更通知。
PCF删除本地保存的该AM策略关联的相关信息，向AMF发送Npcf_AMPolicyControl_Delete
 Response消息。
##### PCF发起的AM策略关联终止流程 
PCF发起的AM策略关联终止流程如[图5](37.html#T_1554257199570__08164619-600f-4305-b809-cb0b2c2e6136)所示。
图5  AM策略关联终止流程（PCF发起）
[]images/1526880664149.png)
流程说明如下： 
PCF收到内外部事件触发（内部事件例如时段变更通知，外部事件例如UDR通知PCF已删除了某用户的策略签约）。 
PCF重新进行策略决策，确定需要删除相关的AM策略关联。 
PCF向AMF发送Npcf_AMPolicyControl_UpdateNotify
消息，携带AM策略关联ID及删除AM策略关联指示。
AMF回复Npcf_AMPolicyControl_UpdateNotify
 Ack消息。
后续流程同[AMF发起的AM策略关联终止流程](37.html#T_1554257199570__e3ec87a9-be10-4c65-a6e7-658d5578f2ee)。
### NG-RAN位置上报 
概述 :位置上报流程是指其它NF（例如：SMF、PCF等）向AMF订阅位置上报服务时，AMF向NG-RAN发送位置上报请求，要求NG-RAN上报CM-CONNECTED状态UE的当前位置，或者UE处于AOI（Area Of Interest，兴趣区域）的IN/OUT/UNKNOW等状态。
当UE迁移到CM-IDLE状态或者AMF发送取消指示时NG-RAN停止上报。当UE发生基于Xn的切换时，NG-RAN节点的位置上报相关信息会传递给目的NG-RAN节点。 
#### NG-RAN位置上报流程 
NG-RAN位置上报流程如[图1](1600073971102.html#zb33604f12d0849539fd356908e237837__8aa89e25-3a46-4a81-aa51-98b44a7afc95)所示。
图1  NG-RAN位置上报流程
[]images/1600074695554.png)
流程说明如下： 
AMF发送Location Reporting Control
消息给NG-RAN。Location Reporting Control
消息包含需要标识上报位置的用户、位置上报类型、位置上报级别、AOI（兴趣区域）和请求参考ID。其中，位置上报级别可以是“TAI+小区标识”。位置上报类型为以下某一种：
一次性上报UE当前小区的位置上报 
连续上报小区发生变化的位置上报 
连续上报兴趣区域的位置上报 
NG-RAN发送Location Report
消息给AMF，消息中包括UE的位置、UE是否在AOI中、请求参考ID和时间戳。
当UE处于RRC去活的CM-CONNECTED状态时，如果AMF请求位置上报类型是“一次性上报UE当前小区的位置上报”时，则NR-RAN会寻呼用户。寻呼成功后，把UE当前的位置信息上报给AMF。 
当UE处于RRC去活的CM-CONNECTED状态时，如果AMF请求位置上报类型是“连续上报小区发生变化的位置上报”时，则NR-RAN立即把UE最后的位置信息上报给AMF。后续NG-RAN会持续检测UE位置，当发现UE所处小区发生变化后，则继续上报给AMF。 
当UE处于CM-CONNECTED状态时，如果AMF请求位置上报类型是“连续上报兴趣区域的位置上报”，则NR-RAN启动跟踪并立即把UE当前是否在兴趣区域等信息上报给AMF。后续NG-RAN检测到UE进入或者离开兴趣区域时，NR-RAN把UE的位置信息上报给AMF。 
如果AMF需要终止正在进行中的请求上报类型为“连续上报小区发生变化的位置上报”或“连续上报兴趣区域的位置上报”时，AMF发送Cancel Location Reporting消息通知NG-RAN停止相应的位置信息上报。其中，Cancel Location Reporting消息中的位置上报类型为以下某一种：
取消连续上报。 
取消兴趣区域。此类型下，AMF可以包括请求参考ID，便于NG-RAN停止对应的兴趣区域的位置上报。 
取消用户当前所有的位置上报。 
### 计费 
SMF与CHF之间基于SBI协议创建计费会话，融合计费涉及的业务流程包括CHF服务发现、计费会话创建、计费会话更新和计费会话终止流程。 
本节包含如下流程： 
CHF服务发现流程 
SBI计费会话创建流程 
SBI计费会话更新流程 
SBI计费会话终止流程 
#### CHF服务发现流程 
SMF支持通过NRF查询CHF的服务，获取CHF的计费服务IP地址和端口。如[图1](42.html#T_1554257199570__a71b61bb-fe13-49b8-87bc-6d636b81ebc2)所示。
图1  CHF服务的NRF发现流程
[]images/1599034171429.png)
流程说明如下： 
SMF作为服务消费者，发起NF Discovery Request（Nnrf_NFDiscovery
 Request）到NRF，请求CHF融合计费功能服务。NRF决定是否允许SMF发现所请求的服务，并授权服务发现请求，根据请求中的信息发现对应的融合计费功能实例。
NRF返回NF Discovery Response（Nnrf_NFDiscovery
 Response）消息，包含对应CHF的服务描述。
#### SBI计费会话创建流程 
用户激活或者首业务报文到达时会触发SMF创建SBI计费会话。 
用户激活时，创建SBI计费会话，预申请配额，可以避免用户访问业务时才申请配额导致用户访问业务有延迟，提升用户体验。 
业务触发时，创建SBI计费会话，不申请配额，而是在用户使用业务时申请配额，可避免用户长期占用配额不使用的情况。 
用户激活时创建SBI计费会话流程如[图2](42.html#T_1554257199570__eedca363-caff-4724-a879-4eb2be64d9b5)所示。
图2  PDU会话触发计费开始流程
[]images/1599034539793.png)
流程说明如下： 
UE发起PDU Session Establishment Request
，SMF收到PDU Session Establishment Request
消息。
SMF根据配置的计费方式选择是否进行在线计费，根据CHF选择方式选中相应的CHF，准备创建在线计费SBI计费会话。 
SMF发送ChargingDataRequest
（initial）消息给CHF，请求创建SBI计费会话，ChargingDataRequest
（initial）消息中携带需要预申请配额的业务RG。
CHF授权通过，回复ChargingDataResponse
（initial）消息给SMF，接受SBI计费会话建立，ChargingDataResponse
（initial）消息中会携带CHF分给用户的信用配额。
SMF发送N4 Session Establish Request（PFCP Session Establishment Request
）消息给UPF，创建用户面隧道。
UPF创建用户面隧道成功，发送N4 Session Establish Response（PFCP Session Establishment Response
）消息给SMF。
SMF响应PDU Session Establishment Accept
消息。
用户正常使用业务。 
业务触发创建SBI计费会话流程如[图3](42.html#T_1554257199570__1edbdb1f-bf12-4342-a990-d956f6bc677f)所示。
图3  业务触发SBI计费开始流程
[]images/1599037158784.png)
流程说明如下： 
UE发起PDU Session Establishment Request
，SMF收到PDU Session Establishment Request
消息。
SMF发送N4 Session Establish Request（PFCP Session Establishment Request
）消息给UPF，创建用户面隧道。
UPF创建用户面隧道成功，发送N4 Session Establish Response（PFCP Session Establishment Response
）消息给SMF。
SMF响应PDU Session Establishment Accept
消息。
用户开始使用业务，UPF触发N4 Session Report Request（PFCP Session Report Request
）消息给SMF，携带业务的start指示。
SMF发送N4 Session Report Response（PFCP Session Report Response
）消息给UPF。
SMF根据CHF选择方式选中相应的CHF，发送ChargingDataRequest
（initial）消息给CHF，请求创建SBI计费会话，ChargingDataRequest
（initial）消息中携带需要预申请配额的业务RG。
CHF授权通过，回复ChargingDataResponse
（initial）响应消息给SMF，接受SBI计费会话建立，ChargingDataResponse
（initial）消息中会携带CHF分给用户的信用配额。
SMF把CHF下发业务的配额等计费信息，发送N4 Session Modification Request（PFCP Session Modification Request
）消息给UPF。
UPF给对应的业务安装配额，对用户的业务使用情况进行监控，UPF发送N4 Session Modification Response（PFCP Session Modification Response
）消息给SMF。
用户正常使用业务。 
#### SBI计费会话更新流程 
SBI计费会话更新流程可以由SMF、UPF、CHF发起。 
SMF发起的SBI计费会话更新流程SMF通过发送ChargingDataRequest（update）消息，发起SBI计费会话更新流程。SMF支持在计费触发条件改变时发送ChargingDataRequest（update）。触发条件由CHF下发。计费触发条件包括ULI、UCI、RAT、服务节点、QoS信息等发生改变。以ULI更新为例，SBI计费会话更新流程如图4所示。图4  ULI改变触发的SBI计费会话更新流程流程说明如下：UE的位置移动，SMF收到PDU会话更新，原因为ULI改变，SMF决定通知CHF。SMF通过N4 Session Modification Request（PFCP Session Modification Request）消息通知UPF，查询该用户的流量等计费信息。UPF查询到计费信息后，通过N4 Session Modification Response（PFCP Session Modification Response）消息通知SMF，携带流量等计费信息。SMF通过发送ChargingDataRequest（update）消息，携带Request Unit和Rating
Group等参数，发起SBI计费会话更新。CHF分配配额，返回ChargingDataResponse（update）消息，携带更新的配额信息。SMF通过N4 Session Modification Request（PFCP Session Modification Request）消息通知UPF，更新该用户的流量配额等计费信息。用户正常使用业务。 
UPF发起的SBI计费会话更新流程UPF通过如下事件触发SMF发起SBI计费会话更新流程。新业务触发的初始配额申请：发生在各RG的首个报文到达UPF的时刻。会话离线门限到达：CHF下发的会话的时间或流量门限到达，触发ChargingDataRequest（update）。RG离线门限到达：CHF下发的RG的时间或流量门限到达，触发ChargingDataRequest（update）。配额耗尽：CHF下发的时间或流量配额耗尽，触发ChargingDataRequest（update）。剩余配额量达到门限值：当用户未消耗的配额小于等于配额门限值（VQT/TQT）后，会触发用户重新申请配额。配额有效期到期：VT（Validity Time）用于指示CHF所分配配额的有效时长。时长超期后，会触发用户重新申请配额。配额保持定时器超期：用户长时间没有业务访问，报文停止转发时长超过QHT（Quota-Holding-Time）时会触发用户重新申请配额。以流量门限到达为例说明，SBI计费会话更新流程如图5所示。图5  流量门限到达触发的SBI计费会话更新流程流程说明如下：流量门限到达，UPF通过N4 Session Report Request（PFCP Session Report Request）消息通知SMF，携带流量等计费信息。SMF给UPF回复N4 Session Report Response（PFCP Session Report Response）消息F。SMF通过发送ChargingDataRequest（update）消息，发起SBI计费会话更新。CHF分配配额，返回ChargingDataResponse（update）消息，携带更新的配额信息。SMF通过N4 Session Modification Request（PFCP Session Modification Request）消息通知UPF，更新该用户的流量配额等计费信息。用户正常使用业务。 
CHF发起的会话通知流程如果CHF主动向SMF发送ChargingNotifyRequest（重授权）消息，则会触发SMF发起SBI计费会话更新流程，重授权目标可以是整个SBI计费会话，或者某几个业务。SMF收到请求后先响应请求，随后发出ChargingDataRequest（update）消息，根据重授权目标携带部分或全部业务。CHF发起的会话更新流程如图6所示。图6  CHF发起的重鉴权流程流程说明如下：SMF收到CHF的ChargingNotifyRequest（重授权）消息，其中的请求类型为重鉴权请求。SMF发送成功的HTTP响应消息。SMF通过N4 Session Modification Request（PFCP Session Modification Request）消息通知UPF，查询该用户的流量等计费信息。UPF查询到计费信息后，通过N4 Session Modification Response（PFCP Session Modification Response）消息通知SMF，携带流量等计费信息。SMF通过发送ChargingDataRequest（update）消息，发起SBI计费会话更新。CHF分配配额，返回ChargingDataResponse（update）消息，携带更新的配额信息。SMF通过N4 Session Modification Request（PFCP Session Modification Request）消息通知UPF，更新该用户的流量配额等计费信息。用户正常使用业务。 
#### SBI计费会话终止流程 
SBI计费会话的终止可以由SMF发起，或者由CHF发起。 
SMF发起的SBI计费会话终止流程PDU会话去激活时，SMF会发起PDU会话对应的SBI计费会话终止请求。CHF回复ChargingDataResponse（terminate）消息，终结SBI计费会话。如图7所示。图7  SMF发起的SBI计费会话终止流程流程说明如下：SMF收到PDU会话删除请求，SMF需要释放SBI计费会话。SMF通过N4 Session Deletion Request（PFCP Session Deletion Request）消息通知UPF，查询该用户的流量等计费信息。UPF查询到计费信息后，通过N4 Session Deletion Response（PFCP Session Deletion Response）消息通知SMF，携带流量等计费信息。SMF通过发送ChargingDataRequest（terminate）消息，发起SBI计费会话释放请求。CHF返回ChargingDataResponse（terminate）消息。SMF回复PDU Session Release Command消息。 
CHF发起的SBI计费会话终止流程CHF发起的SBI计费会话终止，分为异步和同步两种方式。异步终止：CHF主动向SMF发起ChargingDataRequest（terminate）消息，请求终止SBI计费会话。SMF先回复响应消息，同时去激活SBI计费会话对应的PDU会话，向CHF发送ChargingDataRequest（terminate）消息终止SBI计费会话。同步终止：CHF收到SMF发来的ChargingDataRequest（terminate）消息后，在ChargingDataResponse（terminate）消息中携带异常结果码，通知SMF会话出现异常，需要终止。SMF根据本地配置的异常结果码处理动作，终止SBI计费会话，并去活对应的PDU会话。异步终止的流程如图8所示。图8  CHF发起的SBI计费会话终止流程流程说明如下：SMF收到CHF的ChargingNotifyRequest消息，其中携带的通知类型为释放会话请求。SMF发送成功的HTTP响应消息。SMF通过N4 Session Deletion Request（PFCP Session Deletion Request）消息通知UPF，查询该用户的流量等计费信息。UPF查询到计费信息后，通过N4 Session Deletion Response（PFCP Session Deletion Response）消息通知SMF，携带流量等计费信息。SMF通过发送ChargingDataRequest（terminate）请求消息，发起SBI计费会话终止请求。CHF返回ChargingDataResponse（terminate）消息。SMF释放会话。 
NRF :本节包含如下流程： 
NF服务注册流程 
NF服务更新流程 
NF服务去注册流程 
NF或NF服务的发现流程 
NF或NF服务的状态订阅通知流程 
#### NF服务注册流程 
NF服务注册流程如[图1](44.html#T_1554257199570__4c2cdefc-5353-4e92-a995-a5e1029ee68a)所示。
图1  NF服务注册流程
[]images/ZUF-90-11-001-NF%E6%9C%8D%E5%8A%A1%E6%B3%A8%E5%86%8C%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
NF向NRF发送Nnrf_NFManagement_NFRegister
 Request消息，请求注册本NF实例信息及支持的NF服务实例。
NRF保存NF实例信息及支持的NF服务实例信息，并标识该NF可用。
NRF向NF发送Nnrf_NFManagement_NFRegister
 Response消息。
#### NF服务更新流程 
NF服务更新流程如[图2](44.html#T_1554257199570__f27f9046-e3e1-4a06-a32e-97f5f931fd8d)所示。
图2  NF服务更新流程
[]images/ZUF-90-11-001-NF%E6%9C%8D%E5%8A%A1%E6%9B%B4%E6%96%B0%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
NF向NRF发送Nnrf_NFManagement_NFUpdate
 Request消息，请求服务信息更新。
NRF更新保存的NF实例信息。
NRF向NF发送Nnrf_NFManagement_NFUpdate
 Response消息，接受本次更新。
#### NF服务去注册流程 
NF服务去注册流程如[图3](44.html#T_1554257199570__d8fb79cb-8c59-4502-9cb9-8e9a81e34a2d)所示。
图3  NF服务去注册流程
[]images/ZUF-90-11-001-NF%E6%9C%8D%E5%8A%A1%E5%8E%BB%E6%B3%A8%E5%86%8C%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
NF实例准备退出服务，向NRF发送Nnrf_NFManagement_NFDeregister
 Request消息，请求去注册。
NRF接受NF退出服务的请求，标记该NF不可用。
NRF向NF发送Nnrf_NFManagement_NFDeregister
 Response消息，NF退出服务。
#### NF或NF服务的发现流程 
NF或NF服务的发现流程如[图4](44.html#T_1554257199570__435ac19a-df92-456c-977e-34c4c077591b)所示。
图4  NF或NF服务发现流程
[]images/ZUF-90-11-001-NF%E6%9C%8D%E5%8A%A1%E5%8F%91%E7%8E%B0%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
NF服务消费者需要发现目标NF服务，向NRF发送Nnrf_NFDiscovery
 Request消息，请求发现目标NF服务。
如果NRF的服务PLMN与归属PLMN不一致，服务PLMN中的NRF根据请求消息中携带的PLMN来获取归属PLMN的NRF地址，将该发现请求转发给归属PLMN的NRF，归属PLMN中的NRF基于请求的服务参数查询到匹配的NF服务实例，向请求NRF发送Nnrf_NFDiscovery
 Response消息。
服务PLMN中的NRF向请求NF发送Nnrf_NFDiscovery
 Response消息。
#### NF或NF服务的状态订阅通知流程 
NF或NF服务的状态订阅通知流程包括如下业务流程： 
当NRF的服务PLMN即为归属PLMN时的NF或NF服务状态订阅通知流程 
当NRF的服务PLMN与归属PLMN不一致时的NF或NF服务状态订阅通知流程 
当NRF的服务PLMN即为归属PLMN时
当NRF的服务PLMN即为归属PLMN时的状态订阅通知流程如[图5](44.html#T_1554257199570__16452fd3-f175-4a91-adde-703503117ca8)所示。
图5  服务PLMN即为归属PLMN时的状态订阅通知流程
[]images/NF%E6%88%96NF%E6%9C%8D%E5%8A%A1%E7%8A%B6%E6%80%81%E8%AE%A2%E9%98%85%E9%80%9A%E7%9F%A5%E6%B5%81%E7%A8%8BPLMN%E4%B8%80%E8%87%B4.png)
流程说明如下： 
NF服务消费者向NRF发送Nnrf_NFManagement_NFStatusSubscribe
 Request消息，请求订阅NF实例及包含服务的注册/更新/去注册。
NRF授权NF服务状态订阅需求。 
NRF向NF服务消费者发送Nnrf_NFManagement_NFStatusSubscribe
 Response消息。
被订阅的NF实例及包含服务信息发生变更，NRF向NF服务消费者发送Nnrf_NFManagement_NFStatusNotify
 Request消息。
当NRF的服务PLMN与归属PLMN不一致时
当NRF的服务PLMN与归属PLMN不一致时的状态订阅通知流程如[图6](44.html#T_1554257199570__fe68e134-cc9d-4155-8694-f8d84262aed4)所示。
图6  服务PLMN与归属PLMN不一致时的状态订阅通知流程
[]images/ZUF-90-11-001-NF%E6%88%96NF%E6%9C%8D%E5%8A%A1%E7%9A%84%E7%8A%B6%E6%80%81%E8%AE%A2%E9%98%85%E9%80%9A%E7%9F%A5%E6%B5%81%E7%A8%8B.png)
流程说明如下： 
服务PLMN中的NF服务消费者向NRF发送Nnrf_NFManagement_NFStatusSubscribe
 Reques消息，请求订阅NF实例及包含服务的注册/更新/去注册。
服务PLMN中的NRF根据请求消息中携带的PLMN来获取归属PLMN的NRF地址，将该请求转发给归属PLMN的NRF，归属PLMN中的NRF保存订阅信息，向请求NRF发送Nnrf_NFManagement_NFStatusSubscribe
 Response消息。
服务PLMN中的NRF向NF服务消费者发送Nnrf_NFManagement_NFStatusSubscribe
 Response消息。
被订阅的NF实例及包含服务信息发生变更，归属PLMN中的NRF向NF服务消费者发送Nnrf_NFManagement_NFStatusNotify
 Request消息。
### 网络切片 
#### 支持用户接入网络切片 
注册流程中切片信息处理如[图1](39.html#T_1554257199570__d7702d38-6a47-4cae-ac2d-af72f9b8a631)所示。
图1  注册过程中切片信息处理
[]images/%E6%94%AF%E6%8C%81%E7%94%A8%E6%88%B7%E6%8E%A5%E5%85%A5%E7%BD%91%E7%BB%9C%E5%88%87%E7%89%87.png)
流程说明如下： 
UE判断需要发起注册流程时，发送注册请求消息（Registration Request
），消息中携带Requested NSSAI。
NG-RAN收到注册请求消息后，如果消息中有5G-GUTI，则根据5G-GUTI选择AMF；如果消息中没有5G-GUTI，则根据消息中Requested NSSAI信息，选择一个合适的AMF（Initial AMF）。 
NG-RAN向Initial AMF发送注册请求消息（Registration Request
）。
Initial AMF处理注册请求消息，包括获取用户信息，安全过程等。 
Initial AMF向UDM发送Nudm_SDM_Get
消息，向UDM获取用户签约数据。
UDM向Initial AMF返回Nudm_SDM_Get
响应消息，消息中携带Subscribed NSSAI等用户签约信息。
Initial AMF向NSSF发送Nnssf_NSSelection_Get
消息，消息中携带Requested NSSAI、Subscribed NSSAI、用户接入的TA、SUPI等信息。
NSSF根据Requested NSSAI、Subscribed NSSAI等信息，以及本地策略，确定Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate。NSSF给Intial AMF返回Nnssf_NSSelection_Get
响应消息，消息中携带Allowed NSSAI、Rejected NSSAI、AMF Set或AMF Candidate等信息。
如果NSSF返回了AMF Set，则Initial AMF向NRF发送Nnrf_NFDiscovery
_Request消息，消息中携带AMF Set等信息。
NRF向Initial AMF返回Nnrf_NFDiscovery
_Request响应消息，消息中携带AMF Candidate等信息。
Initial AMF根据AMF Candidate等信息，确定AMF是否需要重定向。 
如果AMF需要重定向，则Intial AMF从AMF Candidate中选择一个AMF作为Target AMF。Intial AMF和Target AMF间完成AMF重定向过程。 
继续处理注册过程。 
Intial AMF（AMF没有进行重定向）或Target AMF（AMF进行了重定向）向PCF发送Npcf_AMPolicyControl_Create
消息。
PCF向AMF返回Npcf_AMPolicyControl_Create
响应消息，消息中携带URSP等信息，URSP信息中包含NSSP信息。
AMF继续处理注册流程，包括更新PDU会话等，直到AMF向UE发送注册接受消息。 
AMF向UE发送注册接受消息Registration Accept
，消息中携带Allowed NSSAI、Rejected NSSAI、URSP等信息。
继续处理注册流程，直到注册流程结束。 
#### 网络切片的PDU连接创建 
PDU会话建立过程中的切片信息处理流程如[图1](40.html#T_1554257199570__02c528dd-125c-4925-8cd2-ab2e455c3266)所示。
图1  PDU会话建立过程中的切片信息处理
[]images/%E7%BD%91%E7%BB%9C%E5%88%87%E7%89%87%E5%9C%B0PDU%E8%BF%9E%E6%8E%A5%E5%88%9B%E7%AB%8B.png)
UE判断需要发起PDU会话建立流程时，发送PDU Session Establishment Request
消息，消息中携带请求的S-NSSAI、DNN、PDU会话ID等信息。
AMF向NSSF发送Nnssf_NSSelection_Get
_Request消息，携带S-NSSAI、DNN等信息。
NSSF返回Nnssf_NSSelection_Get
_Response消息，在消息中携带NSI等信息。
AMF向NRF发送Nnrf_NFDiscovery
_Request消息，携带NSI、S-NSSAI、DNN等信息。
NRF返回Nnrf_NFDiscovery
_Response消息，在消息中携带SMF
Candidate列表等信息。
AMF根据SMF Candidate列表等信息，选择一个SMF。 
继续处理PDU会话建立流程，如通知SMF创建会话上下文，创建用户面上下文等，直到PDU会话建立流程结束。 
缩略语 :缩略语 :### 5G-GUTI 
5G Globally Unique Temporary Identity5G全球唯一临时标识
5GC :5G Core Network5G核心网
### 5GS 
5G System5G系统
AAA :Answer-Auth-Answer应答鉴权响应
### AAR 
Answer-Auth-Request应答鉴权请求
AF :Application Function应用功能
AMF :Access and Mobility Management Function接入和移动管理功能
AUSF :Authentication Server Function鉴权服务器功能
### BAR 
Buffer Action Rule报文缓存规则
### CDR 
Charging Data Record计费数据记录
CHF :Charging Function计费功能
### CSCF 
Call Session Control Function呼叫对话控制功能
### CUPS 
Control and User Plane Separation控制面与用户面分离
### DNAI 
DN Access Identifier数据网络接入标识符
DNN :Data Network Name数据网名称
EIR :Equipment Identity Register设备标识寄存器
### FAR 
Forwarding Action Rule报文转发规则
### FDD 
Frequency Division Duplex频分双工
FQDN :Fully Qualified Domain Name完全限定域名
GPSI :Generic Public Subscription Identifier一般公共用户标识
### GUMMEI 
Globally Unique MME Identifier全球唯一移动性管理实体标识
GUTI :Globally Unique Temporary Identity全球唯一临时标识
### iFC 
initial Filter Criteria初始过滤规则
IMEI :International Mobile Equipment Identity国际移动设备标识
IMS :IP Multimedia SubsystemIP多媒体子系统
IMSI :International Mobile Subscriber Identity国际移动用户标识
IPv4 :Internet Protocol Version 4互联网通信协议第四版
IPv6 :Internet Protocol Version 6互联网通信协议第六版
### LADN 
Local Area Data Network局域数据网
LTE :Long Term Evolution长期演进
### MAA 
Multimedia-Authorization-Answer多媒体鉴权响应
### MAR 
Multimedia-Authorization-Request多媒体鉴权请求
### MCC 
Mobile Country Code移动国家码
### MICO 
Mobile Initiated Connection Only仅限移动发起连接
### MM 
Mobility Management移动性管理
MME :Mobility Management Entity移动管理实体
### MNC 
Mobile Network Code移动网络号
NAS :Non-Access Stratum非接入层
NF :Network Function网络功能
### NG-RAN 
Next Generation Radio Access Network下一代无线接入网
### NITZ 
Network Identity and Time Zone网络标志和时区
### NR 
New Radio新无线
NRF :NF Repository Function网络仓储功能
### NSSAI 
Network Slice Selection Assistance Information网络切片选择辅助信息
NSSF :Network Slice Selection Function网络切片选择功能
P-CSCF :Proxy-Call Session Control Function代理呼叫会话控制功能
### PANI 
P-Access-Network-Info接入网信息（SIP私有扩展之一）
PCC :Policy and Charging Control计费和策略控制
PCF :Policy Control Function策略控制功能
### PCO 
Protocol Configuration Option协议配置选项
### PDR 
Packet Detection Rule报文检测规则
PDU :Packet Data Unit分组数据单元
### PEI 
Permanent Equipment Identifier永久设备标识
### PFCP 
Packet Forwarding Control Protocol报文转发控制协议
PLMN :Public Land Mobile Network公共陆地移动网
### PSI 
PCF Session IdentityPCF会话标识
### QCI 
QoS Class IdentifierQoS类别标识
### QER 
QoS Enforcement RuleQoS执行规则
### QFI 
QoS Flow IdentityQoS流标识
### RAA 
Re-Auth-Answer重新鉴权响应
### RAR 
Re-Auth-Request重新鉴权请求
RAT :Radio Access Technology无线接入技术
### RFSP 
RAT/Frequency Selection Priority无线/频率选择优先级
### RRC 
Radio Resource Control无线资源控制
S-NSSAI :Single Network Slice Selection Assistance Information单个网络切片选择辅助信息
SM :Session Management会话管理
SMF :Session Management Function会话管理功能
### SNA 
Subscription-Notification-Answer订阅通知响应
### SNR 
Subscription-Notification-Request订阅通知请求
### SSC 
Session and Service Continuity会话与业务连续性
### STA 
Session-Termination-Answer会话终止响应
### STR 
Session-Termination-Request会话终止请求
### SUCI 
Subscription Concealed Identifier签约的隐藏标识符
SUPI :Subscriber Permanent Identifier用户永久标识
### T-ADS 
Terminating Access Domain Selection终结接入域选择
### TAI 
Tracking Area Identity跟踪区标识
TAU :Tracking Area Update跟踪区域更新
### TDD 
Time Division Duplex时分双工
### TEID 
Tunnel Endpoint Identifier隧道端点标识
### UAA 
User-Authorization- Answer用户授权响应
### UAR 
User-Authorization-Request用户授权请求
### UDA 
User-Data-Answer用户数据响应
UDM :Unified Data Management统一数据管理
UDR :User Data Request用户数据（读取）请求
UE :User Equipment用户设备
### ULI 
User Location Information用户位置信息
UPF :User Plane Function用户平面功能
URI :Uniform Resource Identifier统一资源标识符
### URR 
Usage Reporting Rule用量上报规则
### URSP 
UE Route Selection PolicyUE路由选择策略
### XRES 
Expected User Response预期的用户响应
## 接口协议 
### Namf 
#### Namf接口协议简介 
场景描述 :Namf是AMF为其他NF提供服务的接口。 
图1  Namf接口示意图
[]images/1.PNG)
 说明： 
目前，AMF还不支持向LMF、GMLC、CBCF、PWS、NEF提供服务。 
协议栈 :图2  服务化接口协议栈
[]images/3.PNG)
Namf和其他所有服务化接口一样，都采用如上图所示的协议栈，应用层统一采用HTTP/2协议，携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
##### 网络功能服务列表 
AMF通过Namf接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括下表所定义的各种： 
NF|NFS|NFS的解释
---|---|---
AMF|Namf_Communication|NF通过AMF的此服务与UE/(R)AN通信。该服务的关键功能有：提供向UE传送N1消息的服务操作。提供向AN发起N2消息的服务操作。允许NF订阅和取消订阅来自UE的特定N1消息的通知。允许NF订阅和取消订阅来自AN的特定信息的通知。UE信息管理和传递（包括其安全上下文）。
Namf_EventExposure|AMF|AMF提供此服务，以使NF能够为自己/其他NF订阅事件通知，并获得有关事件的通知。已知的服务消费者是NEF、SMF、UDM。Namf _ EventExposure Service提供以下事件：位置报告事件，NF订阅此事件可以获取一个UE或一组UE最新的位置信息。AOI内状态报告事件，NF订阅此事件以接收特定AOI（Area of Interest，感兴趣区域）中UE当前的状态，以及UE进入或离开指定区域时的通知。时区报告事件，NF订阅此事件以接收UE或一组UE的当前时区。接入类型报告事件，NF订阅此事件以接收UE或一组UE当前的接入类型。注册状态报告事件，NF订阅此事件以接收UE或一组UE当前的注册状态。连接状态报告事件，NF订阅此事件以接收UE或一组UE的当前连接状态。可达性报告事件，NF订阅此事件以接收UE或一组UE当前的可达性。通信失败报告事件，NF订阅此事件以接收UE或一组UE或任何UE的通信失败报告。区域内用户数报告事件，NF订阅该事件，用于接收特定区域内的用户数，或者根据当前位置请求AMF主动寻找该区域内的UE。失去连接报告事件，NF订阅该事件，用于接收AMF检测到UE或一组UE信令或者数据通信不可达。
Namf_MT|AMF|该服务允许NF请求与向目标UE发送MT信令或数据能力相关的信息。以下是该NF业务的关键功能UE处于IDLE状态时寻呼UE，然后当UE进入CM-CONNECTED状态后向其他NF发送响应。如果UE处于CONNECTED状态，向请求方NF发响应。向消费者NF提供IMS语音的终接域选择信息。
Namf_Location|AMF|该服务用于NF服务消费者请求AMF发起定位请求，并提供位置信息。它还用于随后将位置变化事件通知给NF服务消费者。该NF业务的关键功能如下：允许NF请求目标UE的当前大地测量和可选的公民位置。允许将紧急会话相关的事件信息通知给NF。允许NF请求与目标UE的位置对应的NPLI（Network Provided Location Information ，网络侧提供位置信息）和/或本地时区。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Namf接口上提供的各服务以及各服务支持的服务操作见下表： 
服务名称|服务操作|服务操作的解释
---|---|---
Namf_Communication|UEContextTransfer|用于注册流程中。如：当target AMF收到注册请求消息，消息中UE的5G-GUTI包括源AMF信息，则target AMF调用源AMF的Namf_Communication_UEContextTransfer以获取UE上下文（如UE的SUPI和MM上下文）。
RegistrationStatusUpdate|Namf_Communication|用于注册流程中。如：target AMF调用源AMF的Namf_Communication_RegistrationStatusUpdate用来向源AMF更新目标AMF上的UE注册状态，从而指示针对指定UE的先前的UEContextTransfer的结果。
CreateUEContext|Namf_Communication|用于基于N2的Inter NG-RAN切换流程中。如：当源AMF不能继续服务UE并在切换过程中选择目标AMF后，源AMF调用目标AMF的Namf_Communication_CreateUEContext用于在目标AMF中创建UE上下文。
ReleaseUEContext|Namf_Communication|用于基于N2的Inter NG-RAN切换取消流程中。如：当源AMF在切换过程中接收到来自(R)AN的切换取消时，源AMF调用目标AMF的Namf_Communication_ReleaseUEContext用于释放目标AMF中的UE Context。
N1N2MessageSubscribe|Namf_Communication|用于UE配置更新等流程中。NF服务消费者（例如LMF或PCF）通过调用AMF的Namf_Communication_N1N2MessageSubscribe可以订阅特定N1消息类型（例如LPP或UPDP）或N2信息类型（例如，NRPPa）的通知。
N1N2MessageUnSubscribe|Namf_Communication|NF服务消费者（例如LMF或PCF）调用AMF的Namf_Communication_N1N2MessageUnsubscribe用来通知AMF停止通知特定类型（例如LPP或UPDP）的N1消息或N2信息。
N1MessageNotify|Namf_Communication|用于AMF重分配的注册、UE配置更新等流程。如：在AMF重分配的注册流程中，初始AMF通过NRF获取目标AMF的URI信息，然后初始AMF调用自己的Namf_Communication_N1MessageNotify向目标AMF提供RAN NGAP ID、初始AMF名称、RAN ID、N1消息、UE SUPI和MM上下文、允许NSSAI等信息。如：在UE配置更新流程中，因为之前PCF向AMF订阅了N1消息，当AMF收到UE发送的UPDP消息后，调用自己的Namf_Communication_N1MessageNotify将UPDP消息通知给PCF。
N2InfoNotify|Namf_Communication|用于基于N2的Inter NG-RAN切换流程和网络辅助定位流程。如：在基于N2的Inter NG-RAN切换流程中，目标AMF调用Namf_Communication_N2InfoNotify通知源AMF用户已经成功切换到目标侧。如：在网络辅助定位流程中，当AMF收到5G-AN发送的NRPP消息时，调用Namf_Communication_N2InfoNotify向LMF通知收到的位置信息。
N1N2MessageTransfer|Namf_Communication|用于PDU会话建立/修改/释放、网络侧发起的服务请求、Inter NG-RAN node N2 based handover、UE配置更新等流程中。如：在PDU会话建立过程中，SMF调用AMF的Namf_Communication_N1N2MessageTransfer从而通过AMF向UE和(R)AN发送N1会话管理信息（UE IP地址、QoS Rule等）和N2会话管理信息（CN Tunnel Info、QoS Profile等）。
N1N2TransferFailureNotification|Namf_Communication|用于PDU会话建立/修改/释放、网络侧发起的服务请求、Inter NG-RAN node N2 based handover、UE配置更新等流程中。如：AMF通过此通知NF服务消费者（如SMF）在其之前发起的Namf _ Communication _ N1N2MessageTransfer流程中，因为UE响应寻呼失败，因此AMF向UE下发N1消息失败。
AMFStatusChangeSubscribe|Namf_Communication|用于AMF规划的删除流程中。用于NF服务消费者订阅AMF的状态变化。
AMFStatusChangeUnSubscribe|Namf_Communication|用于AMF规划的删除流程中。用于NF服务消费者取消订阅AMF的状态变化。
AMFStatusChangeNotify|Namf_Communication|用于AMF规划的删除流程中。该服务操作通知每一个以前订阅了AMF的状态变化通知的NF服务消费者AMF的状态发生了变化，例如AMF不可用了。
EBIAssignment|Namf_Communication|用于UE请求PDU会话建立、UE或网络请求PDU会话修改流程中。由NF服务消费者（例如，SMF）向NF服务制造者（即AMF）调用，以请求AMF为给定UE的现有PDU会话的QoS Flow映射的EPS承载分配EPS承载ID。
Namf_EventExposure|Subscribe|该服务操作被NF服务消费者（例如NEF）向AMF调用，为一个UE、一组UE或任何一个UE订阅事件。
Unsubscribe|Namf_EventExposure|该服务操作由NF服务消费者（例如NEF）向AMF调用，以删除先前在AMF上创建的现有订阅。
Notify|Namf_EventExposure|当订阅中包含的某些事件发生时，AMF调用通知服务操作，向NF服务消费者发送通知。
Namf_Location|ProvideLocationInfo|该服务操作允许NF服务消费者（例如UDM）请求目标UE的NPLI（Network Provided Location Information ，网络侧提供位置信息）。
Namf_MT|EnableUEReachability|当SMSF需要下发MT SMS时，调用AMF的Namf_MT_EnableUEReachability API，通知AMF使能用户可达。
ProvideDomainSelectionInfo|Namf_MT|当NF服务消费者，比如UDM，需要获取用于IMS语音落地域选择的用户信息时，调用Namf_MT_ProvideDomainSelectionInfo API。
##### Namf_Communication_UEContextTransfer 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_UEContextTransfer|Request/Response|当目标AMF收到注册请求消息，消息中UE的5G-GUTI包括源AMF信息，则目标AMF调用源AMF的Namf_Communication_UEContextTransfer以获取UE上下文（如UE的SUPI和MM上下文）。NF服务消费者发送POST请求消息中包含UeContextTransferReqData数据类型的对象。如果成功，目标AMF应响应状态码“201 Created”，并且PUT响应的消息体应包含UeRegStatusUpdateRspData数据类型的对象。如果失败或重定向时，目标AMF应返回403/404的HTTP状态码，并且消息体应包含一个ProblemDetails结构。
##### Namf_Communication_RegistrationStatusUpdate 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_RegistrationStatusUpdate|Request/Response|用于通用注册流程和AMF重分配流程注册流程中，目标AMF调用源AMF的Namf_Communication_RegistrationStatusUpdate用来向源AMF更新目标AMF上的UE注册状态，从而指示针对指定UE的先前的UEContextTransfer的结果。NF服务消费者发送POST请求消息中包含UeRegStatusUpdateReqData数据类型的对象。如果成功，目标AMF应响应状态码“201 Created”，并且PUT响应的消息体应包含N1N2MessageTransferRspData数据类型的对象。如果失败或重定向时，目标AMF应返回403/404的HTTP状态码，并且消息体应包含一个ProblemDetails结构。
##### Namf_Communication_CreateUEContext 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_CreateUEContext|Request/Response|NF服务消费者（例如，源AMF）使用带有“Individual UeContext”资源的URI的HTTP PUT方法创建UE上下文，其中ueContextId唯一标识一个UeContext资源，由UE的SUPI或PEI组成。NF服务消费者发送PUT请求消息中包含UeContextCreateData结构，包括N2信息通知回调URI。如果成功，目标AMF应响应状态码“201 Created”，并且PUT响应的消息体应包含UeContextCreatedData结构。如果失败或重定向时，目标AMF应返回403的HTTP状态码，并且消息体应包含一个UeContextCreateError结构。
##### Namf_Communication_ReleaseUEContext 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_ReleaseUEContext|Request/Response|用于基于N2的Inter NG-RAN切换取消流程中。NF服务消费者发送POST请求消息中包含需要传递到目标AMF的任何数据。如果成功，目标AMF将在后续响应中返回“204 No Content”，其中包含一个空净荷体。如果失败或重定向时，目标AMF应返回403/404的HTTP状态码，并且消息体应包含一个ProblemDetails结构。
##### Namf_Communication_N1N2MessageSubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_N1N2MessageSubscribe|Subscribe/Notify|用于UE配置更新等流程中。NF服务消费者（例如LMF或PCF）通过调用AMF的Namf_Communication_N1N2MessageSubscribe可以订阅特定N1消息类型（例如LPP或UPDP）或N2信息类型（例如，NRPPa）的通知。NF服务消费者应发送POST请求，在AMF中创建订阅资源，用于UE特定的N1/N2消息通知，该POST请求的净荷体包括UeN1N2InfoSubscriptionCreateData数据结构。如果请求被接受，AMF应包含一个HTTP位置头，以提供新创建的资源（订阅）的位置，以及指示请求的资源在响应消息中创建的状态码201。该响应消息的净荷体包括UeN1N2InfoSubscriptionCreatedData数据结构。
##### Namf_Communication_N1N2MessageUnSubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_N1N2MessageUnSubscribe|Subscribe/Notify|用于AMF重分配的注册、UE配置更新等流程。NF服务消费者（例如LMF或PCF）调用AMF的该服务操作用来通知AMF停止通知特定类型（例如LPP或UPDP）的N1消息或N2信息。NF服务使用者应发送删除请求以删除AMF中已有的订阅资源。如果请求被接受，AMF应在响应消息中回复204指示删除订阅ID成功。
##### Namf_Communication_N1MessageNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_N1MessageNotify|Subscribe/Notify|用于AMF重分配的注册、UE配置更新等流程。该服务操作用于AMF将从UE接收到的N1消息通知到目的NF。AMF应向N1通知URI发送HTTP POST请求，POST请求的净荷体应包含带有订阅N1消息的N1MessageNotification数据结构。成功时，应返回204No Content。失败时， 返回403响应，响应消息体中应包含一个ProblemDetails对象。
##### Namf_Communication_N2InfoNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_N2InfoNotify|Subscribe/Notify|用于NGRAN节点N2切换流程和网络辅助定位流程。该服务操作被AMF调用，通知NF服务消费者从接入网接收到订阅的N2信息。AMF应向n2InfoNotifyUrl发送HTTP POST请求，POST请求的净荷体应包含N2InformationNotification数据结构，包含NF服务消费者订阅的N2信息。成功时，应返回204No Content，响应的净荷体为空。失败时， 消息体中应包含一个ProblemDetails对象。
##### Namf_Communication_N1N2MessageTransfer 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_N1N2MessageTransfer|Request/Response|用于PDU会话建立/修改/释放、网络侧发起的服务请求、Inter NG-RAN node N2 based handover、UE配置更新等流程中。NF服务消费者应发送POST请求，传递N1和N2信息，NF服务消费者可以在请求消息的AMF中包含N1N2MessageTransfer通知URI。POST请求消息体中包括N1N2MessageTransferReqData数据结构。在成功的情况下，即如果请求被接受，并且AMF能够将N1/N2消息传递给UE和/或者，则AMF应响应一个200 OK的状态码，AMF将N1N2MessageTransferRspData中的原因IE设置为“N1_N2_TRANSFER_INITIATED”。在失败或重定向时，返回3XX/4xx/5xx响应，消息体应包含N1N2MessageTransferErrorr结构。
##### Namf_Communication_N1N2TransferFailureNotification 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_N1N2TransferFailureNotification|Subscribe/Notify|用于PDU会话建立/修改/释放、网络侧发起的服务请求、Inter NG-RAN node N2 based handover、UE配置更新等流程中。当AMF确定寻呼或NAS通知失败时，如果NF服务消费者提供了通知URI，AMF应在通知URI上向NF服务消费者发送一个POST请求。在POST请求体中，包含N1/N2消息传递原因信息。NF服务消费者应发送“204 No Content”状态码的响应。
##### Namf_Communication_AMFStatusChangeSubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_AMFStatusChangeSubscribe|Subscribe/Notify|用于AMF规划的删除流程中。用于NF服务消费者订阅AMF的状态变化。NF服务使用者应发送POST请求，请求消息体中包括SubscriptionData数据结构。成功时，AMF应包含一个HTTP位置头，以提供新创建的资源（订阅）的位置，以及状态码201。失败或重定向时，返回4xx/5xx响应，消息体包含一个ProblemDetails结构。
该服务操作通过向AMF提供更新的签约数据，更新AMF中以前签约的NF业务消费者的签约数据，对整个签约数据（通过新的签约数据完全替换现有的签约数据）进行更新操作。NF服务使用者应向代表个人订阅的资源URI发送PUT请求，请求体应包含订阅数据的表示，以替换AMF中先前的订阅数据。PUT请求的净荷体应包含SubscriptionData数据结构。在成功的情况下，应返回“200 OK”，PUT响应的净荷体应包含被替换资源的表示，SubscriptionData的数据结构。失败或重定向时，返回403响应，消息体包含一个ProblemDetails数据结构。|Namf_Communication_AMFStatusChangeSubscribe|Subscribe/Notify
##### Namf_Communication_AMFStatusChangeUnSubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_AMFStatusChangeUnSubscribe|Subscribe/Notify|用于AMF规划的删除流程中。此服务操作将删除已有的订阅通知。NF服务使用者应向代表个人订阅的资源URI发送删除请求，请求体应为空。成功时，返回204 No Content，响应正文为空。失败或重定向时，返回404响应，消息体包含一个ProblemDetails结构。
##### Namf_Communication_AMFStatusChangeNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_AMFStatusChangeNotify|Subscribe/Notify|用于AMF规划的删除流程中。该服务操作通知每一个以前订阅了AMF的状态变化通知的NF服务消费者AMF的状态发生了变化，例如AMF不可用了。AMF向回调URI发送POST请求，请求体中包含GUAMI和相关状态变化，GUAMI由NF服务消费者在订阅操作时指示。成功时，由NF服务消费者返回“204 No content”。失败或重定向时，返回404响应，消息体包含一个ProblemDetails结构。
##### Namf_Communication_EBIAssignment 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Communication_EBIAssignment|Request/Response|用于UE请求PDU会话建立、UE或网络请求PDU会话修改流程中。NF服务消费者（例如，SMF）应调用个人ue context资源上的“assign-ebi”自定义方法，NF服务消费者应提供PDU会话标识、ARP列表和S-NSSAI作为服务操作的输入。NF服务消费者发送的POST请求的净荷主体包括一个AssignEbiData数据结构。在成功的情况下，则AMF应响应一个200 OK的状态码。响应消息的净荷主体包括一个AssignedEbiData数据结构。失败或重定向时，返回403响应，消息体应包含AssignEbiError结构。
##### Namf_EventExposure_Subscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_EventExposure_Subscribe|Subscribe/Notify|该服务操作用于NF业务消费者（如，NEF）为UE订阅事件。NF服务消费者应发送POST请求在AMF中创建订阅资源，POST请求的净荷主体应包含要创建的个人订阅资源的表示。请求中可以包含失效时间，由NF服务消费者建议为提示。表示需要保持订阅的时间，以及订阅事件应停止生成报告的时间。POST请求的净荷主体包括一个AmfCreateEventSubscription数据结构。成功时，AMF响应消息中包含一个HTTP位置头，以提供新创建的资源（订阅）的位置，以及状态码201。响应消息的净荷主体包括一个AmfCreatedEventSubscription数据结构。失败或重定向时，返回403响应，消息体包含一个ProblemDetails数据结构。
NF服务消费者应发送PATCH请求修改AMF中的订阅资源，修改可能是订阅的事件或更新事件选项。PATCH请求净荷主体包括一个AmfUpdateEventSubscriptionItem数据结构。成功时，AMF应该将修改后的订阅资源或其子资源的表示形式连同状态码200 OK一起返回。响应消息的净荷主体包括一个AmfUpdatedEventSubscription数据结构。失败或重定向时，返回403/404响应，消息体包含一个ProblemDetails数据结构。|Namf_EventExposure_Subscribe|Subscribe/Notify
##### Namf_EventExposure_Unsubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_EventExposure_Unsubscribe|Subscribe/Notify|取消订阅服务操作由NF服务使用者（例如NEF）向AMF调用，以删除先前在AMF上创建的现有订阅。NF服务消费者应发送删除请求以删除AMF中已有的订阅资源。成功后，AMF应回复204状态码，指示在响应消息中删除订阅ID标识的资源成功。失败或重定向时，返回404响应，消息体包含一个ProblemDetails数据结构。
##### Namf_EventExposure_Notify 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_EventExposure_Notify|Subscribe/Notify|通知服务操作由AMF调用，用于当订阅中包含的某些事件发生时，向通知URI发送通知。AMF发送POST请求，发送通知。POST请求的净荷主体包括一个AmfEventNotification数据结构。如果接收到通知，NF服务消费者应在响应消息中回复指示收到通知的状态码204。
##### Namf_Location_ProvideLocationInfo 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_Location_ProvideLocationInfo|Request/Response|该服务操作允许NF服务消费者（如，UDM）请求目标UE的网络提供的位置信息 。NF服务消费者应向AMF发送一个POST请求，POST请求的净荷主体应包含指示所需位置信息类型的“RequestLocInfo”数据结构。成功时，AMF返回200 OK响应，响应的净荷体包含一个包含网络提供目标UE位置信息的“ProvideLocInfo”数据结构。失败或重定向时，返回403/404响应，消息体包含一个ProblemDetails数据结构。
##### Namf_MT_EnableUEReachability 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_MT_EnableUEReachability|Request/Response|当SMSF需要下发MT SMS时，调用AMF的Namf_MT_EnableUEReachability API，通知AMF使能用户可达。NF服务消费者发送PUT请求消息中包含EnableUEReachabilityReqData数据类型的对象。如果成功，AMF应响应状态码为"200 OK"，并且PUT响应的消息体中包含EnableUEReachabilityRspData数据类型的对象。如果失败或者重定向，AMF返回403/503/504等HTTP状态码，并且消息中应包含ProblemDetails或ProblemDetailsEnableUeReachability数据类型的对象。
##### Namf_MT_ProvideDomainSelectionInfo 
服务操作|操作语义|服务操作的解释
---|---|---
Namf_MT_ProvideDomainSelectionInfo|Request/Response|当NF服务消费者，比如UDM，需要获取用于IMS语音落地域选择的用户信息时，调用Namf_MT_ProvideDomainSelectionInfo API。NF服务消费者发送GET请求消息，URI中包含info-class=TADS的请求参数。如果成功，则AMF应相应状态码为"200 OK"，并且GET响应的消息体中包含UeContextInfo数据类型的对象。如果失败或者重定向，AMF返回403/404HTTP状态码，并且消息中应包含ProblemDetails数据类型的对象。
#### 数据类型解释 
##### UeContextCreateData 
UeContextCreateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
UeContext|Mandatory|表示要创建的单个ueContext资源。
targetId|Mandatory|表示目标RAN的标识。
sourceToTargetData|Mandatory|该IE包含“Source to Target Transparent Container”。
pduSessionList|Mandatory|该IE包含N2SmInformation的列表，其中每个N2SmInformation包含每个PDU会话ID从源RAN接收的“切换要求传输”。
n2NotifyUri|Mandatory|该IE应包含一个回调URI，用于接收N2信息通知。
ueRadioCapability|Conditional|如果有“UE Radio Capability Information”，则该IE包含“UE Radio Capability Information”。
ngapCause|Conditional|如果有，该IE将会出现。当出现时，它将代表从RAN接收的NGAP原因。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应出现。
##### UeContextTransferReqData 
UeContextTransferReqData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
reason|Mandatory|表示业务请求的原因。
accessType|Mandatory|该IE应包含UE的接入类型。
plmnId|Optional|如果存在，该IE应包含NF服务消费者的PLMN ID。
regRequest|Optional|如果存在，则该IE应参考触发UE上下文转移的注册请求消息，消息类应为5GMM，消息内容应参考N1消息内容二进制数据。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### UeContextCreatedData 
UeContextCreatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
UeContext|Mandatory|表示新创建的个人上下文资源。
targetToSourceData|Mandatory|该IE应包含“Target to Source Transparent Container”。
pduSessionList|Mandatory|该IE包含N2SmInformation的列表，其中每个N2SmInformation包含从SMF接收的“切换命令传输”，每个PDU会话ID。
pcfReselectedInd|Conditional|如果目标AMF已经决定为AM策略选择一个新的PCF，而不是旧AMF包含在UeContext中的一个，则该IE应该显示并设置为true。
ngapCause|Conditional|如果有，该IE将会出现。当出现时，它将代表从RAN接收到的NGAP原因。
failedSessionList|Conditional|该IE包含N2SmInformation的列表，每个N2SmInformation包含从SMF接收到的PDU会话切换失败的“Handover Preparation Unsuccessful Transfer”N2短消息内容。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### UeContextTransferRspData 
UeContextTransferRspData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
UeContext|Mandatory|表示应用修改后的一个单独的ueContext资源。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
ueRadioCapability|Conditional|如果在上下文转移过程中可用，则包含“UE无线能力信息”。
##### UeContextCreateError 
UeContextCreateError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|表示详细的应用错误信息。应用级别错误原因应编码在“原因”属性中。
ngapCause|Conditional|如果可用，应提供此IE。它表示从RAN收到的NGAP Cause。
targetToSourceFailureData|Conditional|如果收到来自目标NG-RAN的“目标到源失败透明容器”，则应显示此IE。当此IE存在时，应包含此容器。
##### SubscriptionData 
SubscriptionData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
amfStatusUri|Mandatory|该IE应包含接收AMF状态变化通知的回调URI。
guamiList|Conditional|如果订阅AMF支持的任何GUAMI的状态变化，则该IE将不存在，它将用于订阅AMF支持的特定GUAMI。
##### UeRegStatusUpdateReqData 
UeRegStatusUpdateReqData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
transferStatus|Mandatory|该IE应指示先前UE上下文转移是否完成。
toReleaseSessionList|Conditional|如果在UE上下文转移过程中存在与网络切片(s)关联的PDU会话(s)，则该IE将出现在UE上下文转移过程中。当出现时，该IE应包含与不再可用的S-NSSAI(s)相关联的所有PDU会话(s)。
pcfReselectedInd|Conditional|如果目标AMF决定为AM策略选择一个新的PCF，而不是旧AMF包含在UeContext中的一个新PCF，则该IE应该显示并设置为true。
##### UeRegStatusUpdateRspData 
UeRegStatusUpdateReqData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
regStatusTransferComplete|Mandatory|该IE应指示在源AMF上是否成功完成UE上下文转移的状态更新。如果上下文传输完成成功，则该值为true；如果上下文传输未完成成功，则该值为false；缺省值为true。
##### UeN1N2InfoSubscriptionCreateData 
UeRegStatusUpdateRspData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
n2InformationClass|Conditional|如果NF服务消费者订阅了N2信息通知，则该IE应出现。该IE表示NF服务消费者需要通知的N2信息的类别。
n2NotifyCallbackUri|Conditional|如果NF服务消费者订阅了N2信息通知，该IE将显示。该IE表示需要通知N2信息的回调URI。
n1MessageClass|Conditional|如果NF服务消费者订阅了N1消息通知，该IE将会出现。该IE表示NF服务消费者需要通知的N1消息类。
n1NotifyCallbackUri|Conditional|如果NF服务消费者订阅了N1消息通知，则该IE应出现。该IE表示需要通知N1消息的回调URI。
nfId|Conditional|如果订阅的是“NRPPa”N2信息类和/或“eMLPP”N1信息类，则该IE应存在。当出现时，该IE应携带用于NGAP“路由标识”IE的值，用于标识网络功能（如，LMF）。处理NRPPa和/或eMLPP数据的实例。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### UeN1N2InfoSubscriptionCreatedData 
UeN1N2InfoSubscriptionCreateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
n1n2NotifySubscriptionId|Mandatory|表示AMF为订阅通知UE相关的N1/N2信息所创建的Id。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### N1MessageNotification 
N1MessageNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
n1NotifySubscriptionId|Conditional|表示产生通知的订阅ID。NF服务使用者使用此方法将通知与相应的订阅关联。如果通知是通过NRF隐式订阅的，那么该值应该设置为“隐式”。如果通知是基于N1MessgeNotification订阅的，则该IE应该出现。AMF重分配流程中，初始AMF向目标AMF转发NAS消息时的异常。
n1MessageContainer|Mandatory|包含N1消息类和N1消息内容。
lcsCorrelationId|Optional|如果通知的N1消息为LCS流程，NF业务生产者（如，AMF）可以包括LCS关联标识。
registrationCtxtContainer|Conditional|如果通知的N1消息类型为5GMM（如，在AMF重分配流程注册时），NF业务生产者（如，AMF）如果有可用的信元，则应包含该信元。
##### N2InformationNotification 
N2InformationNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
n2NotifySubscriptionId|Mandatory|表示产生通知的订阅ID。NF服务使用者使用此将通知与对应的订阅相关联。
n2InfoContainer|Conditional|除NG-RAN节点N2切换流程外，该IE应存在。当出现该IE时，该IE应包含与对应的N2信息类相关的N2信息。
toReleaseSessionList|Conditional|在N2切换过程中，如果有与网络切片(s)关联的PDU会话(s)不再可用，则该IE将出现。当出现时，该IE应包含与不再可用的S-NSSAI(s)相关联的所有PDU会话(s)。
lcsCorrelationId|Conditional|如果在相应的N1/N2消息传输服务操作中接收到LCS相关标识，则该IE应出现。当该信元存在时，该信元应携带LCS相关标识。
notifyReason|Conditional|如果不存在“n2InfoContainer”属性，则该IE应存在；该IE可能会出现在其他地方。该IE表示N2信息通知的原因。
##### N1N2MessageTransferReqData 
N1N2MessageTransferReqData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
n1MessageContainer|Conditional|如果需要传递N1消息，则必须包含该IE。
n2InfoContainer|Conditional|如果需要传递N2信息，则必须包含该IE。
skipInd|Conditional|如果服务使用者（如，SMF）要求在UE处于CM-CONNECTED状态时才向UE发送N1消息，例如在SMF发起的PDU会话释放过程时，该IE应显示为“true”。当出现此IE时，该IE应设置为：-true：当UE处于CM-IDLE状态时，AMF不会向UE发送N1消息。-false （默认）：AMF向UE发送N1消息。
lastMsgIndication|Optional|当出现此标志时，表示传递的消息是最后一条消息
pduSessionId|Optional|如果N1 / N2消息类型为SM，则发送N1 / N2消息的PDU会话ID。
lcsCorrelationId|Optional|如果N1消息类型为eMLPP，则发送N1消息的LCS关联标识。
ppi|Optional|当该IE出现时，该IE指示要应用的寻呼策略。寻呼策略在AMF上配置。
arp|Optional|此信元当出现时，表示发起N1/N2消息传输的PDU会话的分配保持优先级，当N1/N2消息类不是SM时，该IE不会出现。
5qi|Optional|当该IE出现时，该IE表示该PDU会话所关联的5QI，当N1/N2消息类型不是SM时，该IE不会出现。
n1n2FailureTxfNotifURI|Optional|如果包含，则此IE表示AMF应通知N1/N2消息传递失败的回调URI。
smfReallocationInd|Optional|该IE应指示SMF被请求重新分配。当出现此IE时，该IE设置如下：-true：请求重新分配SMF。-false （默认）：不请求SMF重分配。
areaOfValidity|Optional|该IE表示提供的N2信息有效的TA列表。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### N1N2MessageTransferRspData 
N1N2MessageTransferRspData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
cause|Mandatory|该IE应提供AMF中N1/N2消息传递处理的结果。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现
##### N1N2MessageTransferError 
N1N2MessageTransferError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|该IE应提供AMF中N1/N2消息传递处理的结果。
errInfo|Conditional|该IE可包含用于提供与错误相关的附加信息。
##### AssignEbiData 
AssignEbiData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pduSessionId|Mandatory|表示请求分配EBI(s)的PDU会话的标识符。
arpList|Conditional|如果NF服务消费者 (如， SMF) 请求AMF为PDU会话分配EBI(s)，则该IE应出现，当出现此IE时，该IE应包含请求EBI(s)的QoS流(s)映射的ARP列表。
releasedEbiList|Conditional|如果NF服务消费者（如，SMF）需要从QoS流中释放分配的EBI(s)（如，当QoS流被释放时），该IE应该出现。
##### AssignedEbiData 
AssignedEbiData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pduSessionId|Mandatory|表示请求分配EBI(s)的PDU会话的标识符。
assignedEbiList|Mandatory|如果AMF分配了请求的EBI(s)，则该IE应该出现。该IE应包含已成功分配的EBI。
failedArpList|Conditional|如果AMF为一组ARP的(s)分配EBIs失败，则该IE应该出现。
releasedEbiList|Conditional|如果NF服务使用者请求释放EBI(s)或AMF撤销已分配给同一个PDU会话的EBI，该IE应包含在AMF上释放的EBI(s)列表。
##### AssignEbiFailed 
AssignEbiFailed的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pduSessionId|Mandatory|表示请求分配EBI(s)的PDU会话的标识符。
failedArpList|Conditional|如果AMF为一组ARP分配EBIs失败，则该IE应该出现。
##### AssignEbiError 
AssignEbiError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|表示应用错误信息。应用级别错误原因应当在“原因”属性中进行编码。
failureDetails|Mandatory|描述失败的详细信息，包括EBI分配失败的ARPs列表。
##### RequestLocInfo 
RequestLocInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
req5gsLoc|Conditional|如果在NPLI中请求5GS位置信息，则该IE应该显示并且设置为“true”。当出现时，IE应设置为：-true：请求UE位置-false （默认）：表示不请求UE的位置信息。
reqCurrentLoc|Conditional|如果在NPLI中请求5GS位置信息，则可能存在此IE。当出现时，IE应设置为：-true：请求UE当前位置-false （默认）：不请求UE当前位置。
reqRatType|Conditional|如果在NPLI中请求UE的类型，则该IE应该显示并且设置为“true”。当出现时，IE应设置为：-TRUE：请求UE的类型。-false （默认）：表示不请求UE的类型。
reqTimeZone|Conditional|如果在NPLI中请求UE的本地时区，则该IE应该显示并且设置为“true”。当出现时，IE应设置为：-true：请求UE本地时区-false （默认）：不请求UE的本地时区。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### ProvideLocInfo 
ProvideLocInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
currentLoc|Conditional|如果5GS位置信息是由NF服务消费者请求的，则该IE应该存在。当出现此IE时，该IE应设置为：-true：返回UE当前位置-false：返回UE最后一个已知位置。
location|Optional|如果存在，则该IE包含UE的位置信息。
geoInfo|Optional|如果存在，该IE应包含UE的地理信息。
locationAge|Optional|如果存在，该IE应包含位置信息的年龄。
ratType|Optional|如果存在，该IE将包含UE当前的RAT类型。
timezone|Optional|如果存在，该IE应包含UE的本地时区。
supportedFeatures|Optional|如果支持至少一个可选特性，则该IE应该出现。
##### AmfCreateEventSubscription 
AmfCreateEventSubscription的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscription|Mandatory|表示要创建的AMF事件订阅资源。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### AmfCreatedEventSubscription 
AmfCreatedEventSubscription的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscription|Mandatory|表示新创建的AMF事件订阅资源。
subscriptionId|Mandatory|表示新创建的AMF事件订阅资源的URI。
reportList|Optional|表示立即事件报告（如，订阅的事件的当前值/状态）。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### AmfUpdateEventSubscriptionItem 
AmfUpdateEventSubscriptionItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
op|Mandatory|该IE表示在I对资源进行的PATCH操作。该IE应支持以下取值：- "添加"- "替换"- "移除"
path|Mandatory|该IE包含一个JSON指针值，它引用了要执行PATCH操作的资源的位置。该IE将包含JSON指针，指向AMF事件订阅中的“/eventList”数组的有效索引，格式为：' /eventList\/[0-]$|\/eventList\/[1-9][0-9]*$ '
value|Conditional|该IE表示需要增加的AMF事件，或更新已存在的AMF事件的值。如果PATCH操作为“add”或“replace”，则必须存在。
##### AmfUpdatedEventSubscription 
AmfUpdatedEventSubscription的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscription|Mandatory|表示更新的AMF事件订阅资源。
##### AmfEventSubscription 
AmfEventSubscription的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
eventList|Mandatory|事件列表，描述此订阅要订阅的事件。
notifyUri|Mandatory|标识此订阅由AMF发送的通知的接收方。
notifyCorrelationId|Mandatory|标识通知关联ID。AMF应在通知中包含此ID。对于指定的NF服务消费者，该IE的值在每次订阅中必须是唯一的。
nfId|Mandatory|创建该订阅的NF的标识。
subsChangeNotifyUri|Conditional|如果订阅是由NF服务消费者代表另一个NF创建的，则应出现此IE。（e.g UDM在AMF创建事件订阅，用于向NEF发送事件通知。）当出现时，该IE应标识AMF发送的通知的接收方，以创建新的订阅ID。该ID被NF服务消费者视为与单个UE相关的事件订阅的订阅ID的更改，或视为与UE群组相关的事件订阅相关的新订阅ID的创建（例如，在涉及AMF变更的移动性流程中）。
subsChangeNotifyCorelationId|Conditional|当NF服务消费者(例如，UDM)正在代表另一个NF服务消费者（例如：NEF）订阅事件，则出现该IE应包含通知关联ID。AMF应在创建新订阅ID的通知中包含该订阅ID，NF服务消费者将其视为与单个UE相关的事件订阅的订阅ID的更改，或将其视为与UE组相关的事件订阅的新订阅ID的创建。 对于发送该IE的给定NF服务消费者，该IE的值在每次订阅中必须是唯一的。
supi|Conditional|订阅永久标识。
groupId|Conditional|标识一组UE。
gpsi|Conditional|通用公共订阅标识符。
pei|Conditional|永久设备标识符。
anyUE|Conditional|如果事件订阅适用于任何UE，则该IE应出现。 如果不存在，则使用默认值“FALSE”。
options|Optional|如果NF服务消费者希望描述如何生成事件报告，可以包含该IE。
##### AmfEventNotification 
AmfEventNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
notifyCorrelationId|Conditional|如果通知不是通知创建新的订阅ID，则必须包含此IE。如果通知用于通知创建新的订阅Id，并且对应的事件订阅没有包含子变更enotifycorrelationid属性。当出现此IE时，该IE应指示NF服务消费者在事件订阅时提供的通知关联标识。如果NF服务使用者使用一个通用的回调URI来进行多个订阅，该参数可以使用。
subsChangeNotifyCorrelationId|Conditional|如果通知是在AMF中通知创建新的订阅Id，并且对应的事件订阅包含了子变更enotifycorrelationid属性，则应该包含该IE。当出现时，该IE设置为订阅时提供的subsChangeNotifyCorrelationId的值。
reportList|Conditional|如果有事件上报，则该IE会出现，该IE表示要下发的事件报告。
##### AmfEvent 
AmfEvent maxReports的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
type|Mandatory|用于描述需要上报的AMF事件类型。
immediateFlag|Optional|指示是否请求订阅响应中的立即事件报告。报告包含订阅时在AMF中存储的事件的当前值/状态。如果flag不出现，则不应立即报告。
areaList|Optional|AmfEventArea的列表，标识PRESENT_IN_AOI_REPORT和UES_IN_AREA_REPORT事件类型应用的区域。仅当在订阅Presence Reporting Area的事件订阅中提供AmfEventArea时，才会使用多于一个AmfEventArea IE实例。
locationFilterList|Optional|描述要应用于LOCATION_REPORT事件类型的过滤器。
refId|Optional|事件关联的Reference Id。
##### AmfEventArea 
AmfEventArea的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
presenceInfo|Conditional|如果订阅的兴趣区域不是LADN服务区域，则应出现此IE。
ladnInfo|Conditional|如果订阅的兴趣区域是LADN服务区，则应包含此IE。
##### UeContext 
UeContext的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
supi|Conditional|该IE应包含UE的SUPI。
supiUnauthInd|Conditional|如果SUPI存在，则此IE应存在。当出现时，应指出SUPI是否未经认证。
gpsiList|Conditional|该IE应包含UE的GPSI。
pei|Conditional|该IE应包含UE的移动设备标识。
udmGroupId|Optional|它指示为UE服务的UDM组的标识。
ausfGroupId|Optional|它应指示为UE服务的AUSF组的标识。
routingIndicator|Optional|它将指示UE的路由指示。
groupList|Conditional|该IE列出UE所属的签约内部组。
drxParameter|Conditional|该IE应包含UE的DRX参数。
subRfsp|Conditional|它指示UE的签约RFSP索引。
usedRfsp|Conditional|它指示UE使用的RFSP索引。
subUeAmbr|Conditional|该IE指示UE的签约UE AMBR值。
smsSupport|Conditional|指示UE是否支持通过3GPP接入或通过非3GPP接入或通过3GPP和非3GPP接入时，在NAS上传送SMS。
smsfId|Conditional|它表示为UE服务的SMSF网络功能实例的标识。NF服务消费者（例如，target AMF）可以使用该信息标识SMSF NF服务配置文件（NF服务消费者会从NRF接收多个SMSF NF服务配置文件）。
seafData|Conditional|该IE包含从UE的AUSF接收的数据中派生的安全数据。
5gMmCapability|Conditional|该IE包含UE的5G MM（Mobility Management）能力。
pcfId|Conditional|该IE指示下发AM策略和/或UE策略的PCF标识。
pcfSetId|Conditional|该IE包含下发AM策略和/或UE策略的PCF的NF Set ID。
pcfAmpServiceSetId|Conditional|该IE包含PCF的AM策略服务的NF服务集ID。
pcfUepServiceSetId|Conditional|该IE包含PCF的UE策略服务的NF服务集ID。
pcfBindingLevel|Conditional|该IE应包含PCF的AM策略和UE策略关联资源的服务化接口绑定级别。
pcfAmPolicyUri|Conditional|该IE应包含AMF使用的单个AM策略资源的URI。
amPolicyReqTriggerList|Conditional|当出现此IE时，该IE应指示AM策略请求触发条件。每当满足这些触发条件时，NF服务消费者（例如：目标AMF）将向PCF请求AM策略。
pcfUePolicyUri|Conditional|该IE应包含AMF使用的单个UE策略资源的URI。
uePolicyReqTriggerList|Conditional|当出现此IE时，该IE应指示UE策略请求触发条件。每当满足这些触发条件时，NF服务消费者（例如：目标AMF）将向PCF请求UE策略。
hpcfId|Optional|该IE指示PCF在归属PLMN中用于UE策略的标识。
restrictedRatList|Optional|该IE应指示UE受限的RAT类型列表。
forbiddenAreaList|Optional|该IE应指示UE的禁止区域列表。
serviceAreaRestriction|Optional|该IE应指示UE的服务区域限制。
restrictedCnList|Optional|该IE应指示UE受限的核心网类型列表。
eventSubscriptionList|Conditional|它指示针对UE或UE所属的组的事件订阅。
mmContextList|Conditional|该IE应包含UE的MM上下文。
sessionContextList|Conditional|该IE包含UE的PDU Session上下文。
traceData|Conditional|如果激活了基于信令的跟踪，则该IE会出现。
serviceGapExpiryTime|Conditional|该IE的值应指示UE的活动服务间隔计时器的过期时间。如果启用了业务间隔控制，并且AMF启动了业务间隔定时器且尚未超时，则该IE应该出现。
stnSr|Optional|该IE应包含UE的STN-SR。
cMsisdn|Optional|该IE应包含UE的C-MSISDN。
msClassmark2|Optional|该IE应包含UE的Mobile Station Classmark 2。
supportedCodecList|Optional|该IE应指示UE支持的语音编解码列表。
smallDataRateStatusInfos|Optional|该IE应指示PDU会话释放时的小数据速率控制状态列表
restrictedPrimaryRatList|Optional|该IE应指示被限制作为UE主要RAT使用的RAT类型列表。
restrictedSecondaryRatList|Optional|该IE应指示被限制作为UE的次RAT使用的RAT类型列表。
##### PduSessionContext 
PduSessionContext的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pduSessionId|Mandatory|PDU会话标识。
smContextRef|Mandatory|表示SM上下文的URI， 当出现时，它应携带以下SM上下文的URI：- I-SMF，用于与I-SMF之间的PDU会话；或者- V-SMF，用于HR PDU会话；或者- SMF，用于没有I-SMF的非漫游PDU会话或LBO漫游PDU会话；
sNssai|Mandatory|PDU Session关联的S-NSSAI信息。
dnn|Mandatory|数据网络名称。
accessType|Mandatory|PDU会话的接入类型。
allocatedEbiList|Conditional|当PDU会话分配至少一个EBI时，该IE应出现。当出现时，该IE应包含当前分配给PDU会话的EBI。
hsmfId|Conditional|该IE指示PDU会话的关联归属SMF。
hsmfSetId|Conditional|该IE应包含归属SMF的NF Set ID。
hsmfServiceSetId|Conditional|该IE应包含归属SMF的PDUSession服务实例的NF Service Set ID。
smfBinding|Conditional|该IE应包含归属SMF的SM上下文资源的SBI绑定级别。
vsmfId|Conditional|该IE应出现在漫游PDU会话中。当出现时，它应指示用于home-routed PDU会话的关联v-SMF，或者指示用于local-breakout PDU会话的关联v-SMF。
vsmfSetId|Conditional|该IE应包含V-SMF的NF Set ID。
vsmfServiceSetId|Conditional|该IE应包含归属v-SMF的PDUSession服务实例的NF Service Set ID。
vsmfBinding|Conditional|该IE应包含v-SMF的SM上下文资源的SBI绑定级别。
ismfId|Conditional|如果I-SMF参与PDU会话，则该IE应出现。当出现时，它将指示PDU会话的关联I-SMF。
ismfSetId|Conditional|该IE应包含I-SMF的NF Set ID。
ismfServiceSetId|Conditional|该IE应包含归属I-SMF的PDUSession服务实例的NF Service Set ID。
ismfBinding|Conditional|该IE应包含I-SMF的SM上下文资源的SBI绑定级别。
nsInstance|Conditional|该IE应指示PDU会话的网络切片实例。
smfServiceInstanceId|Optional|当出现时，该IE包含服务于PDU会话上下文的SMF服务实例的服务实例Id。 AMF可以使用该IE来标识受SMF服务实例失败或重启影响的PDU会话上下文
maPduSession|Conditional|该IE应指示它是否是MA PDU会话。true：表示PDU会话为MA PDU会话；false（缺省值）：该PDU会话不是MA PDU会话。
##### SmfChangeIndication 
SmfChangeIndication取值如表所示： 
枚举值|描述
---|---
CHANGED|I-SMF或V-SMF改变。
REMOVED|I-SMF被删除
##### EnableUEReachabilityReqData 
EnableUEReachabilityReqData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
reachability|Mandatory|指示服务消费者期望的用户可达性状态。
##### EnableUEReachabilityRspData 
EnableUEReachabilityRspData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
reachability|Mandatory|指示用户当前的可达性状态。
### Nsmf 
#### Nsmf接口协议简介 
场景描述 :Nsmf是SMF为其他NF提供服务的接口。 
图1  Nsmf接口示意图
[]images/1.PNG)
N16a是SMF与I-SMF之间的参考点，N38是I-SMF与I-SMF之间的参考点。 
 说明： 
目前，SMF还不支持向NEF提供服务。 
协议栈 :图2  服务化接口协议栈
[]images/3.PNG)
Nsmf和其他所有服务化接口一样，都采用如上图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
##### 网络功能服务列表 
SMF通过Nsmf接口向其他NF提供多种服务（NFS，Network Function Service），具体服务参见下表。 
NF|NFS|NFS的解释
---|---|---
SMF|Nsmf_PDUSession|管理PDU会话，使用从PCF接收的策略和计费规则。Nsmf_PDUSession服务运行在PDU会话上，该服务提供的服务操作允许消费者NF建立、修改和释放PDU会话，其关键功能如下。当接收到来自AMF的N1消息通知时，创建、修改和删除PDU会话的SM上下文；SM上下文表示针对一个PDU会话，NF服务消费者（例如：AMF）与SMF之间的关联。获取PDU会话的SM上下文，例如通过N26接口将PDU会话移动到EPC。HR漫游场景下，V-SMF与H-SMF之间PDU会话的创建、修改和删除。将策略和计费规则与PDU会话关联，并将策略和计费规则绑定到QoS Flow中。通过N4与UPF交互，完成用户面会话的创建、修改和释放。处理从UPF来的用户面事件，并应用相应的策略和计费规则。
Nsmf_EventExposure|SMF|此服务将PDU会话上发生的事件公开给消费者NF。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Nsmf接口上提供的各服务以及各服务支持的服务操作见下表： 
服务名称|服务操作|服务操作的解释
---|---|---
Nsmf_PDUSession|Create SM Context|创建SM上下文服务操作用于对于给定的PDU会话创建一个单独的SM上下文。使用场景有：UE发起的PDU会话建立EPS到5GS空闲模式移动性或基于N26接口的切换PDU会话在3GPP接入和非3GPP接入之间的切换
Update SM Context|Nsmf_PDUSession|更新SM上下文服务操作用于更新个人SM上下文和/或提供从UE或从无线接收到的N1或N2 SM信息到SMF。使用场景有：PDU会话修改UE请求的PDU会话释放激活或去激活已有PDU会话的用户面Xn和N2切换流程由于AMF规划维护或AMF失败的AMF间改变RAN发起的QoS Flow移动所有需要提供N1或N2 SM信息给SMF的流程ESP到5GS的空闲态移动或基于N26接口的切换5GS到EPS的基于N26接口的切换由于网络切片实例不再可用导致的网络切片集合改变，而AMF请求的PDU会话释放AMF收到一个“初始请求”，PDU会话标识在UE的PDU会话上下文中已经存在
Release SM Context|Nsmf_PDUSession|释放SM上下文服务操作用于释放指定PDU会话的SM上下文。使用场景有：UE发起的去注册网络侧发起的去注册，如AMF发起的去注册网络侧请求的PDU会话释放，如当UE和AMF上PDU会话状态不一致时，AMF发起的释放5GS到EPS空闲态移动，将那些移到EPC网络的PDU会话的SMF上下文释放基于N26接口的5GS到EPS切换或空闲态移动，将那些没有移到EPC网络的PDU会话的SMF上下文释放
Notify SM Context Status|Nsmf_PDUSession|通知SM上下文状态服务操作用于SMF通知NF服务消费者SMF中与PDU会话相关的SM上下文状态（如，当SM上下文释放时）。主要用于如下两个流程：UE请求的PDU会话建立过程，创建SM上下文响应后PDU会话建立失败。UE或网络请求的PDU会话释放，例如SMF发起的释放。
Retrieve SM Context|Nsmf_PDUSession|检索SM上下文服务操作应用于从SMF或检索针对给定PDU会话检索单个SM上下文。主要用于基于N26接口的5GS到EPS的切换流程和基于N26接口的5GS到EPS空闲模式的移动性注册流程。
Nsmf_PDUSession|Create|在涉及I-SMF的场景中创建一个单独的PDU会话。使用场景有：伴随I-SMF插入的UE发起的PDU会话建立伴随I-SMF插入的注册、服务请求、切换流程
Nsmf_PDUSession|Update|更新I-SMF中的单个PDU会话和/或提供所述I-SMF向所述UE发送N1 SM信令所需的信息。使用场景有：UE或者I-SMF发去的PDU会话修改UE或者I-SMF请求的PDU会话释放增加/删除/修改由I-SMF控制的PDU会话的锚点和分流节点I-SMF发送的N4流量使用报告相关通知
Nsmf_PDUSession|Release|在PDU会话释放流程下，I-SMF释放SM上下文服务操作用于释放指定PDU会话的SM上下文。
Nsmf_PDUSession|Notify Status|通知SM上下文状态服务操作用于I-SMF通知NF服务消费者SMF中与PDU会话相关的SM上下文状态（如，当SM上下文释放时）。用于带有I-SMF的PDU会话流程。
[Nsmf_PDUSession_CreateSMContext](3.html)
[Nsmf_PDUSession_UpdateSMContext](4.html)
[Nsmf_PDUSession_ReleaseSMContext](5.html)
[Nsmf_PDUSession_NotifySMContextStatus](6.html)
[Nsmf_PDUSession_RetrieveSMContext](7.html)
[Nsmf_PDUSession_Create](8.html)
[Nsmf_PDUSession_Update](9.html)
[Nsmf_PDUSession_Release](10.html)
[Nsmf_PDUSession_NotifyStatus](11.html)
##### Nsmf_PDUSession_CreateSMContext 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_CreateSMContext|Request/Response|每个PDU会话只能有一个单独的SM上下文。NF服务消费者（如，AMF）使用HTTP POST方法创建SM上下文，该POST请求的净荷主体应包括：SmContextCreateData结构，包括N2信息通知回调URI。如果成功，SMF应响应状态码“201 Created”，并且PUT响应的消息体应包含SMContextCreatedData结构。如果失败或重定向时，目标SMF应返回3XX/4xx/5xx的HTTP状态码，并且消息体应包含一个SmContextCreateError结构。
##### Nsmf_PDUSession_UpdateSMContext 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_UpdateSMContext|Request/Response|该服务操作用于更新单个SM上下文或提供从UE/RAN接收到的指定PDU会话的N1或N2 SM信息到SMF。NF服务消费者应向SMF中发送POST请求，POST请求的净荷包含SMContextUpdateData。成功时，返回204 No Content或200 OK，在后一种情况下，响应的净荷体应包含SMContextUpdatedData。如果失败或重定向时，目标SMF应返回3XX/4xx/5xx的HTTP状态码，对于4xx/5xx的HTTP状态码场景，消息体应包含一个SMContextUpdateError结构。
##### Nsmf_PDUSession_ReleaseSMContext 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_ReleaseSMContext|Request/Response|该服务操作用于释放指定PDU会话的SM上下文。NF服务消费者应向SMF发送一个POST请求，POST请求的净荷体包含SMContextReleaseData。在成功的情况下，SMF将返回一个204 No Content响应或者200 OK，在后一种情况下，PUT响应的消息体应包含SMContextReleasedData结构。在失败或重定向中，SMF返回失败的HTTP状态代码，对于4xx/5xx响应，消息体应包含一个ProblemDetails结构。
##### Nsmf_PDUSession_NotifySMContextStatus 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_NotifySMContextStatus|Subscribe/Notify|该服务操作用于SMF通知NF服务消费者在SMF中与PDU会话相关的SM上下文状态（如，当SM上下文释放时）。主要用于如下两个流程：UE请求的PDU会话建立过程，创建SM上下文响应后PDU会话建立失败。UE或网络请求的PDU会话释放，例如SMF发起的释放。SMF应向NF服务消费者发送POST请求，请求的净荷体应包含SMContextStatusNotification。成功时，应返回204 No Content，响应的净荷体为空。如果请求中SMF指示释放了消息上下文资源，则NF服务消费者应释放与SMF的关联，释放PDU会话，并释放分配给PDU会话的EBI。在失败或重定向中，NF服务消费者（如：AMF）应返回失败的HTTP状态代码，对于4xx/5xx响应，消息体应包含一个ProblemDetails结构。
##### Nsmf_PDUSession_RetrieveSMContext 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_RetrieveSMContext|Request/Response|该服务操作应用于从SMF获取给定PDU会话的单个SM上下文。主要用于基于N26接口的5GS到EPS的切换流程和基于N26接口的5GS到EPS空闲模式的移动性注册流程。NF服务消费者向SMF发送一个POST请求，该POST请求包含SMContextRetrieveData。成功时，SMF应返回200 OK，响应的净荷体应包含SmContextRetrievedData。失败时，返回403响应，消息体应包含一个ProblemDetails结构。
##### Nsmf_PDUSession_Create 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_Create|Request/Response|在涉及I-SMF的场景或跨PLMN漫游场景中创建一个单独的PDU会话。NF服务消费者（I-SMF）使用HTTP POST方法创建SM上下文，该POST请求的净荷主体应包括：PduSessionCreateData结构，包括代表PDU会话的回调URI，供SMF可能用于随后修改或释放PDU会话。如果成功，SMF应响应状态码“201 Created”，并且PUT响应的消息体应包含PduSessionCreatedData结构。如果失败或重定向时，目标AMF应返回4xx/5xx的HTTP状态码，并且消息体应包含一个PduSessionCreateError结构。
##### Nsmf_PDUSession_Update 
服务操作|操作语义|业务操作的解释
---|---|---
Nsmf_PDUSession_Update|Request/Response|更新I-SMF中的单个PDU会话和/或提供所述I-SMF向所述UE发送N1 SM信令所需的信息。用于HR（home-routed roaming）会话场景，包括I-SMF/V-SMF向A-SMF/H-SMF发起的正向更新以及A-SMF/H-SMF向I-SMF/V-SMF发起的反向更新操作。NF服务消费者（I-SMF）使用HTTP POST方法更新SMF中的PDU会话，或者为SMF提供从UE接收的N1SM信令消息，该POST请求的净荷主体应包括：HsmfUpdateData结构，包括PDU会话请求类型、从UE获取的N1信令消息。如果成功，SMF应响应状态码204 No Content或者200 OK，在后一种情况下，PUT响应的消息体应包含HsmfUpdatedData结构。如果失败，目标AMF应返回4xx/5xx的HTTP状态码，并且消息体应包含一个HsmfUpdateError结构。NF服务消费者（SMF）使用HTTP POST方法I-SMF中的更新PDU会话，或者为I-SMF提供从UE接收的N1SM信令消息，该POST请求的净荷主体应包括：VsmfUpdateData结构，包括PDU会话请求类型、从UE获取的N1信令消息。如果成功，SMF应响应状态码204 No Content或者200 OK，在后一种情况下，PUT响应的消息体应包含VsmfUpdatedData结构。如果失败，目标AMF应返回4xx/5xx的HTTP状态码，并且消息体应包含一个VsmfUpdateError结构。
##### Nsmf_PDUSession_Release 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_Release|Request/Response|该服务操作用于释放指定PDU会话的SM上下文。NF服务消费者应向SMF发送一个POST请求，POST请求的净荷体包含ReleaseData。在成功的情况下，SMF应响应状态码200 OK，PUT响应的消息体应包含ReleasedData结构；或者204 No Content，响应的净荷体为空。在失败的情况下，SMF返回失败的HTTP状态代码，对于4xx/5xx响应，消息体应包含一个ProblemDetails结构。
##### Nsmf_PDUSession_NotifyStatus 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmf_PDUSession_NotifyStatus|Request/Response|通知SM上下文状态服务操作用于I-SMF通知NF服务消费者SMF中与PDU会话相关的SM上下文状态（如，当SM上下文释放时）。SMF应向NF服务消费者发送一个POST请求，POST请求的净荷体包含StatusNotification。在成功的情况下，NF服务消费者应响应状态码204 No Content，响应的净荷体为空。在失败的情况下，NF服务消费者（如：I-SMF）返回失败的HTTP状态代码，对于4xx/5xx响应，消息体应包含一个ProblemDetails结构。
#### 数据类型解释 
##### SmContextCreateData 
SmContextCreateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
supi|Conditional|除非UE是紧急注册和无ICCI，否则该IE应该存在。当出现时，它应包含用户永久标识。
unauthenticatedSupi|Conditional|如果消息中存在SUPI，但未经过身份验证，且为紧急注册UE，则该IE应出现。在目前的情况下，应设置为：true：未认证SUPI。false （默认）：认证成功的SUPI。
pei|Conditional|如果UE处于紧急注册状态，且UE处于紧急状态或SUPI未认证，则该IE应出现。对于所有其他情况，如果有，该IE将会出现。当出现时，它应包含永久设备标识。
gpsi|Conditional|如果该IE可用，则该IE应出现。当出现时，该IE应包含用户的GPSI。
pduSessionId|Conditional|除EPS到5GS空闲模式移动性或N26接口切换外，该IE应存在。当出现时，它应该包含PDU会话标识。
dnn|Conditional|除EPS到5GS空闲模式移动性或N26接口切换外，该IE应存在。当出现时，它应包含所要求的DNN。
sNssai|Conditional|该IE在PDU会话建立过程中存在，此时应包含所请求的S-NSSAI，对应服务PLMN的S-NSSAI，从允许的NSSAI中获得S-NSSAI。在EPS到5GS空闲模式的移动性或N26接口切换时，该IE也应该存在，此时应包含AMF中配置的EPS互通的S-NSSAI。
hplmnSnssai|Conditional|对于HR PDU会话，除EPS到5GS空闲模式移动性或N26接口切换外，还应有此IE。当存在时，它将包含请求的S-NSSAI for HPLMN，这与sNssai信元中包含的SNSSAI值对应的S-NSSAI对应的S-NSSAI。
servingNfId|Mandatory|该IE应包含服务NF的标识符（如，服务AMF）。
guami|Conditional|该IE应包含服务AMF的GUAMI。如果NF服务使用者是AMF ，则应包括它。
serviceName|Optional|当出现此IE时，该IE应包含要发送SM上下文状态通知的AMF服务的名称。如果NF服务使用者是AMF，则可以包含此IE。
servingNetwork|Mandatory|该IE包含服务核心网运营商PLMN ID。
requestType|Conditional|如果请求与现有的PDU会话或现有的紧急PDU会话有关，除了EPS到5GS空闲模式的移动性或切换使用N26接口之外，该IE应该出现。当出现时，它应指示该请求是指新的PDU会话还是紧急PDU会话，或者是已有的PDU会话或紧急PDU会话。
n1SmMsg|Conditional|该IE应存在并引用N1 SM消息二进制数据，除EPS到5GS空闲模式移动性或切换使用N26之外。
anType|Mandatory|该IE应指示PDU会话要关联的接入网类型。
ratType|Conditional|该IE应该存在，并且指示UE使用的RAT类型。
presenceInLadn|Conditional|如果DNN对应的是LADN，则该IE应该出现，应该设置为in或out，以指示UE在LADN服务区内或不在服务区。
ueLocation|Conditional|如果有UE的位置信息，该IE应包含UE的位置信息。
ueTimeZone|Conditional|如果有UE时区，该IE将包含UE时区。
addUeLocation|Optional|UE的附加位置。如果anType指示非3GPP接入且有有效的3GPP接入用户位置信息，则该IE可能存在。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置。表示获取位置信息时的UTC时间。
smContextStatusUri|Mandatory|该IE应包含接收短消息上下文状态通知的回调URI。
hSmfUri|Conditional|该IE在HR漫游场景下存在，当出现时，应包含所选择的H-SMF的Nsmf_PDUSession业务的URI。
oldPduSessionId|Conditional|如果从UE接收到该信息，该IE将会出现。当出现时，它将包含从UE接收到的旧PDU会话ID
pduSessionsActivateList|Conditional|在使用N26接口的EPS到5GS空闲模式移动性时，如果UE指示在注册请求中激活了PDU会话，则该IE应该存在。当出现时，它应指示UE请求重新激活的所有PDU会话。
ueEpsPdnConnection|Conditional|在EPS到5GS空闲模式移动性或N26接口切换时，该IE应存在。当存在时，它将包含一个包含EPS承载上下文的MME UE EPS PDN连接。
hoState|Conditional|在使用N26接口的EPS到5GS切换过程中，该IE应该存在，请求准备PDU会话的切换。
additionalSmfUri|Optional|该IE可能存在于带有I-SMF的PDU会话场景。当出现时，它应该包含AMF根据给定的DNN、hplmnsnssoft和该PDU会话所发现的附加SMF的Nsmf_PDUSession服务的URI数组。提供该信元时，当I-SMF无法接收SmfUri识别的SMF的任何响应时，I-SMF应使用这些额外的SMF。
pcfId|Optional|当出现时，该IE应包含AMF为UE选择的PCF的标识（用于接入和移动性策略控制）。
nrfUri|Optional|该IE可能用于指示在同一个网络切片实例中用于PCF选择的NRF。当出现时，SMF应使用NRF URI来选择PCF。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
selMode|Conditional|如果该IE可用，则该IE应显示。当出现时，它应指示所请求的DNN是否对应显式订阅的DNN或通配符订阅的使用。
backupAmfInfo|Conditional|如果NF服务消费者为AMF，且AMF支持AMF管理，且AMF不支持UDSF，则该IE应包含以下情况：与SMF的第一次交互。修改BackupAmfInfo。
traceData|Conditional|如果需要激活跟踪，则必须包含该IE。
udmGroupId|Optional|当出现时，它应指示为UE服务的UDM组的标识。
routingIndicator|Optional|当出现时，它应指示UE的路由指示。
epsInterworkingInd|Optional|当选择PGW的-C+SMF服务于PDU Session时，AMF可以提供指示。当出现时，该IE应指示PDU会话是否可能移动到EPS，以及EPS互操作过程中是否使用N26接口。AMF可以从不同的来源获取指示的值，如UE无线能力（如，支持S1模式）、UE签约数据 、核心网类型限制 (DNN) 和“与EPS指示的互操作” (DNN) 和配置。
indirectForwardingFlag|Conditional|AMF应在基于N26的EPS到5GS的Handover流程中包含这一指示，通知SMF间接数据转发的适用性或不适用性。在目前的情况下，应设置为：True：间接数据转发。False：不进行间接数据转发。
n2SmInfo|Conditional|如果需要将N2 SM信息发送至I-SMF，则该IE应存在。
n2SmInfoType|Conditional|如果存在n2SmInfo属性，则该IE应存在。当出现此IE时，该IE将指示n2SmInfo属性中携带的NG AP的SMF相关IE容器的NG AP IE类型。
smContextRef|Conditional|当I-SMF插入/变更/删除时，该IE应存在。当出现时，它应该包含SMF或者源I-SMF中的SM上下文资源的URI。
##### SMContextCreatedData 
SMContextCreatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
smfUri|Conditional|当请求中包含了additionalSmfUri IE并且I-SMF向SMF创建的PDU会话，此SMF在additionalSmfUri列表中，该IE应存在。当出现时，它应包含建立PDU会话的SMF的URI。
pduSessionId|Conditional|在EPS到5GS空闲模式移动性或N26接口切换时，该IE应存在。当出现时，应设置为PDU会话ID。
sNssai|Conditional|在EPS到5GS空闲模式移动性或N26接口切换时，该IE应存在。当出现时，它将包含分配给PDU会话的S-NSSAI。
upCnxState|Conditional|如果请求SMF激活相应请求中PDU会话的用户面连接，则该IE应出现。
n2SmInfo|Conditional|如果需要向AN发送N2短消息信息，则该信元必须存在。
n2SmInfoType|Conditional|如果存在n2SmInfo属性，则该IE应出现。在n2SmInfo属性中携带的NG AP的SMF相关IE容器的NG AP IE类型。
allocatedEbiList|Conditional|如果消费者NF是AMF和系统间移动性，则应该出现这个IE，当现在，它应该包含一个EBI到当前分配给PDU会话的ARP映射的数组。
hoState|Conditional|如果请求SMF为PDU会话在相应的请求中准备EPS到5GS切换，则该IE应该出现。
gpsi|Conditional|如果请求中没有提供GPSI IE，例如对于移动到另一种接入方式的PDU会话，并且SMF知道GPSI已经与PDU会话关联，则该IE应存在。当出现时，它应包含与PDU会话相关联的用户GPSI。
smfServiceInstanceId|Optional|当出现时，该IE应包含服务于PDU会话上下文的SMF服务实例的service instance。该IE可用于AMF识别SMF服务实例的失败或重启影响的PDU会话上下文。
recoveryTime|Optional|服务PDU会话的SMF服务实例启动/重启的时间戳。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### SmContextCreateError 
SmContextCreateError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|提供关于错误的信息。
n1SmMsg|Conditional|如果请求中接收到N1 SM信息，且SMF能够向UE返回N1 SM信息，则该IE应出现。当出现时，应引用N1 SM消息二进制数据。
recoveryTime|Optional|SMF服务实例启动/重启时的时间戳。
##### SMContextUpdateData 
SMContextUpdateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pei|Conditional|如果它是可用的，并且还没有提供给SMF，那么这个IE将会出现。当出现时，该IE应包含永久设备标识符。
servingNfId|Conditional|有AMF间变化或移动时，或者发生AMF变化的N2切换时，出现此IE。当出现时，它应包含服务NF的标识符（如，AMF）。
smContextStatusUri|Conditional|当出现此IE时，该IE应包含接收短消息上下文状态通知的回调URI。
guami|Conditional|当AMF的servingNfId出现时，该IE将会出现。出现时，它将包含服务AMF的GUAMI。
servingNetwork|Conditional|如果存在serviceid信元，则该信元必须存在。当存在时，它将包含服务核心网运营商PLMN ID。
backupAmfInfo|Conditional|修改backupAmfInfo时，如果NF服务消费者为AMF，且AMF支持无DSF的AMF管理，则需要包含此IE。删除backupamfinfo时，此IE应该包含空值。
anType|Conditional|该IE应在PDU会话接入网类型变化时出现，例如在3GPP接入和非可信非3GPP接入之间的PDU会话切换期间。当出现此IE时，该IE应指示PDU会话要关联的接入网类型。
ratType|Conditional|修改RAT类型时，该IE应出现，并指示UE使用的RAT类型。
presenceInLadn|Conditional|如果PDU会话的DNN与LADN相对应，则在服务请求过程、Xn切换、N2切换流程中出现此IE。设置为in或out表示UE处于或离开LADN服务区。
ueLocation|Conditional|如果该IE可用，并且需要上报给SMF（如，用户位置发生改变或者PDU会话的用户面被去激活），则该IE应该出现。当该IE出现时，该IE应包含：UE位置信息；获取UeLocation信息的UTC时间。
ueTimeZone|Conditional|如果该IE可用，则UE的时区已经改变，需要上报给SMF。当出现该IE时，该IE应包含UE的时区。
addUeLocation|Optional|UE的附加位置。如果an Type指示非3GPP接入，且有有效的3GPP接入用户位置信息，则该IE可能存在。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置；获取位置信息时的UTC时间。
upCnxState|Conditional|该IE应用于请求激活或去激活PDU会话的用户面连接。SM上下文的upcnxstate属性表示PDU会话的用户面连接状态，取值如下：ACTIVATED：5G-和UPF之间建立N3隧道（上下行分配F-TEID）；DEACTIVATED：5G-和UPF之间没有建立N3隧道；ACTIVATING：正在建立N3隧道（5G-的下行Flow的F-TEID尚未分配）。
hoState|Conditional|该IE应用于请求PDU会话的切换的准备、执行或取消。SM上下文的hoState属性表示PDU会话的切换状态，hoState属性可以取值如下：NONE：PDU会话没有发生切换；PREPARING：移交正在准备PDU会议；SMF正在准备目标5G-和UPF之间的N3隧道，即为上行流量分配UPF的F-TEID；PREPARED：为PDU会话准备切换；目标5G-和UPF之间的N3隧道更新SMF，目标5G-为切换执行时下行流量分配的F-TEID；COMPLETED：切换完成（成功）；CANCELLED：表示取消切换。
toBeSwitched|Conditional|该IE应该在Xn切换中出现，请求将PDU会话切换到新的下行N3隧道端点。在目前的情况下，应设置为：true：请求切换到PDU会话。false （默认）：表示不请求切换PDU会话。
failedToBeSwitched|Conditional|如果在目标RAN中建立PDU会话失败，则在Xn切换中出现该IE。当出现时，表明在目标RAN中建立PDU会话失败的。
n1SmMsg|Conditional|如果接收到UE发送的N1条短消息，则该IE应出现。当出现时，该IE应引用N1 SM消息二进制数据。
n2SmInfo|Conditional|如果收到AN发送的N2短消息信息，则该信元应该存在。当出现时，该IE将引用N2 SM信息二进制数据。
n2SmInfoType|Conditional|如果存在n2SmInfo属性，则该IE应出现。当出现此IE时，该IE将指示n2SmInfo属性中携带的NG AP的SMF相关IE容器的NG AP IE类型。
targetServingNfId|Conditional|当hoState信元值为PREPARING时，在带AMF变化的N2切换准备中，该信元必须存在。当出现时，它应包含目标服务NF的标识。
dataForwarding|Conditional|该IE应在5GS到EPS切换时出现。在目前的情况下，应设置为：true：建立间接数据转发隧道；false （默认）：间接数据转发隧道不需要建立或需要释放。
n9ForwardingTunnel|Conditional|如果UE触发带有I-SMF更改/删除的服务请求流程中，需要在I-UPF缓存下行链路数据包，则该IE应出现。当出现时，该IE应携带I-UPF的N9转发通道信息。
n9DlForwardingTnlList|Conditional|如果带有I-SMF更改/删除的基于N2接口的切换流程中，要求在目标I-UPF和源I-UPF/UPF之间建立下行链路间接数据转发通道，则该IE应出现。当出现时，该IE应携带I-UPF的N9下行链路间接数据转发通道信息列表。
n9UlForwardingTnlLis|Conditional|如果带有I-SMF更改/删除的基于N2接口的切换流程中，要求在目标I-UPF和源I-UPF/UPF之间建立上行链路间接数据转发通道，则该IE应出现。当出现时，该IE应携带I-UPF的N9上行链路间接数据转发通道信息列表。
epsBearerSetup|Conditional|在使用N26接口进行5GS到EPS切换时，该IE应该存在。当出现时，它将包含EPS承载上下文(s)在EPS中成功建立，如果在EPS中没有成功地为任何PDU会话分配资源，数组应该为空。
revokeEbiList|Conditional|该IE应用于请求SMF撤销部分EBI。当出现时，它应包含撤销的EBI。
release|Conditional|该IE用于指示网络发起的PDU会话释放请求。在P-CSCF恢复过程中、AMF由于PDU会话ID重复而请求PDU会话释放时、AMF由于网络切片不可用请求PDU会话释放时，该IE出现。在目前的情况下，应设置为：true：需要释放PDU会话；false （默认）：不需要释放PDU会话。
cause|Optional|当出现时，该IE应指示请求修改的原因，例如请求去激活PDU会话的用户面连接的NF服务消费者原因。
ngApCause|Conditional|如果有信息，该IE应该存在。当出现时，该IE应指示请求修改的原因，例如请求去激活PDU会话的用户面连接的NGAP原因。
5gMmCauseValue|Conditional|在任何网络发起的PDU会话修改或释放过程中，如果AMF收到UE发送的5GMM原因码，则必须包含该IE。
sNssai|Conditional|在EPS到5GS空闲模式移动或N26接口切换时，如果归属PLMN的S-NSSAI派生的服务PLMN的S-NSSAI与创建SM上下文请求中提供的S-NSSAI不同，则该信元必须存在。在当前的情况下，它应该包含服务PLMN的S-NSSAI。
traceData|Conditional|如果需要激活、修改或去激活跟踪，则必须包含该IE。对于跟踪修改，它应该包含完整的跟踪数据替换。对于跟踪去激活，它应该包含空值。
epsInterworkingInd|Optional|如果在创建PDU会话时已经提供了指示，并且在创建会话或上次更新之后，它的值发生了变化，那么该IE可能会出现。当出现时，该IE应指示PDU会话是否可能移动到EPS，以及EPS互操作过程中是否使用N26接口。
anTypeCanBeChanged|Conditional|在服务请求过程中，该IE应呈现并设置为true，表示与PDU会话关联的接入网类型可以改变。在目前的情况下，应设置为：true：允许修改PDU会话的接入类型。false：不允许修改PDU会话的接入类型（默认）。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### SMContextUpdatedData 
SMContextUpdatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
upCnxState|Conditional|如果请求中要求SMF激活或去激活PDU会话的用户面连接，则该IE应出现。
hoState|Conditional|如果请求SMF准备、执行或取消对相应请求中的PDU会话的切换，该IE应出现。
releaseEbiList|Conditional|如果SMF确定部分EBI不需要，则该IE应该出现，当出现时，它应该包含要释放的EBIs。
allocatedEbiList|Conditional|如果消费者NF是AMF且发生系统间移动，则应该出现这个IE，当现在，它应该包含一组分配给PDU会话的EBI到ARP映射。
modifiedEbiList|Conditional|如果PDU会话修改过程导致已分配EBI的QoS流的ARP改变，则该IE应出现。
n1SmMsg|Conditional|如果需要向UE发送N1条短消息信息，则该IE应出现。当出现时，该IE应引用N1 SM消息二进制数据。
n2SmInfo|Conditional|如果需要向AN发送N2短消息信息，则该信元必须存在。当出现时，该IE将引用N2 SM信息二进制数据。
n2SmInfoType|Conditional|如果存在n2SmInfo属性，则该IE应出现。在n2SmInfo属性中携带的NG AP的SMF相关信元容器的NG AP信元类型。
epsBearerSetup|Conditional|使用N26接口进行EPS到5GS切换时，该IE必须存在。当存在时，它将包含成功切换到5GS的EPS承载上下文。
dataForwarding|Conditional|如果该IE在相应的请求中存在，则该IE应出现。
n3DlForwardingTnlList|Conditional|如果请求间接数据转发，且相应请求中包含N9下行链路间接数据转发隧道信息，则该IE应出现。当存在时，它应携带源I-UPF或源UPF的N3下行链路间接数据转发隧道信息列表。
n3UlForwardingTnlList|Conditional|如果请求间接数据转发，且相应请求中包含N9上行链路间接数据转发隧道信息，则该IE应出现。当存在时，它应携带源I-UPF或源UPF的N3上行链路间接数据转发隧道信息列表。
cause|Conditional|如果由于资源不足而导致用户面连接激活失败，则该IE应出现。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应出现。
##### SMContextUpdateError 
SMContextUpdateError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|提供关于错误的信息。
n1SmMsg|Conditional|如果需要向UE返回N1的SM信息，则该IE应出现。当出现时，它应引用N1个SM消息二进制数据。
n2SmInfo|Conditional|如果需要向NGRAN返回N2的SM信息，则该IE必须存在。当出现时，它应引用N2 SM消息二进制数据。
n2SmInfoType|Conditional|如果存在n2SmInfo属性，则该IE应出现。在n2SmInfo属性中携带的NG AP的SMF相关IE容器的NG AP IE类型。
upCnxState|Conditional|如果请求SMF激活或去激活相应请求中PDU会话的用户面连接，则该IE应出现。SM上下文的upcnxstate属性表示PDU会话的用户面连接状态，取值如下：ACTIVATED：5G-和UPF之间建立N3隧道（上下行分配F-TEID）；DEACTIVATED：5G-和UPF之间没有建立N3隧道；ACTIVATING：正在建立N3隧道（5G-的下行Flow的F-TEID尚未分配）。
recoveryTime|Optional|SMF服务实例启动/重启时的时间戳。
##### SMContextReleaseData 
SMContextReleaseData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
cause|Conditional|该IE应指示NF服务消费者请求SM上下文释放的原因。
ngApCause|Conditional|该IE应指示请求的短消息上下文释放的NGAP原因。
5gMmCauseValue|Conditional|如果AMF因5GMM失败而释放PDU会话，则该IE应包含在该IE中，此时该IE应包含从UE接收到的5GMM原因码值。
ueLocation|Conditional|当出现时，它应该包含UE的位置信息。
ueTimeZone|Conditional|当出现时，它应该包含UE的时区信息。
addUeLocation|Optional|UE的附加位置。如果之前上报的无线类型是非3GPP接入且有有效的3GPP接入用户位置信息，则可能存在该IE。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置时间戳，UE的附加位置获取的时间
n2SmInfo|Conditional|如果收到AN发送的N2短消息信息，则该信元应该存在。当出现时，该IE将引用N2 SM信息二进制数据。
n2SmInfoType|Conditional|如果存在n2SmInfo属性，则该IE应出现。在n2SmInfo属性中携带的NG AP的SMF相关IE容器的NG AP IE类型。
ismfReleaseOnly|Conditional|在伴随有I-SMF的改变或移除的5GS切换到EPS空闲模式流程，伴随有I-SMF的改变或移除的基于Xn/N2接口的切换流程中，该IE应存在并取值设置为“true”，表示仅在I-SMF中释放PDU会话的SM上下文。
##### SMContextRetrieveData 
SMContextRetrieveData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
targetMmeCap|Conditional|如果该IE可用，则该IE应存在。当存在时，该IE应包含目标MME能力。
smContextType|Conditional|如果请求为检索完整SM上下文，则在使用I-SMF插入/更改/删除的场景中，应存在该IE。
servingNetwork|Conditional|当存在时，它将包含服务核心网运营商PLMN ID。
##### SmContextRetrievedData 
SmContextRetrievedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
ueEpsPdnConnection|Mandatory|This IE shall contain an MME/SGSN UE EPS PDN Connection including the mapped EPS bearer context(s), if the SM context type was not present in the request or if it was present and indicated a request to retrieve the UE EPS PDN Connection.This IE shall be set to an empty string if the SM context type was present in the request and indicated a request to retrieve the complete SM context.
smContext|Conditional|This IE shall be present if the SM context type was present in the request and indicated a request to retrieve the complete SM context.
smallDataRateStatus|Conditional|This IE shall be present during N26 based Interworking Procedures, if in the request the smContextType is set to "EPS_PDN_CONNECTION" and if the status is available (see clauses 4.11.1.1 and 4.11.1.3.2 in 3GPP TS 23.502 [3]).When present, it shall indicate the small data rate control status for the PDU session.
apnRateStatus|Conditional|This IE shall be present during N26 based Interworking Procedures, if in the request the smContextType is set to "EPS_PDN_CONNECTION" and if the status is available (see clauses 4.11.1.1 and 4.11.1.3.2 in 3GPP TS 23.502 [3]).When present, it shall indicate the APN rate control status for the PDN connection (APN rates are shared by all PDN connections of the UE to this APN).
dlDataWaitingInd|Conditional|This IE shall be present, if the SM context type was not present in the request or if it was present and indicated a request to retrieve the UE EPS PDN Connection, and if downlink data buffered in the SMF/UPF needs to be forwarded to EPS (see clause 4.11.1.3.2A of 3GPP TS 23.502 [3]).When present, it shall be set as follows:true: DL data needs to be sent to the UE;false (default): no DL data needs to be sent to the UE.
##### SMContextStatusNotification 
SMContextStatusNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
statusInfo|Mandatory|该IE应包含SM上下文的状态信息。
smallDataRateStatus|Conditional|This IE shall be present, if the NF Service Consumer has indicated support of CIoT and if the status is available.When present, it shall indicate the current small data rate control status for the PDU session.
apnRateStatus|Conditional|This IE shall be present, if the NF Service Consumer has indicated support of CIoT and if the status is available.When present, it shall indicate the current APN rate control status for the PDN connection (APN rates are shared by all PDN connections of the UE to this APN).
ddnFailureStatus|Conditional|This IE shall be present if the DDN Failure shall be reported (see clause 5.2.8.2.8 of 3GPP TS 23.502 [3]).When present, it shall be set as follows:true: DDN failure detectedfalse (default): DDN failure is not detected
newSmfId|Conditional|This IE may be present if resourceStatus in statusInfo is:TRANSFERREDWhen present, it shall include:the new I-SMF instance identifier ifthe cause in statusInfo is "ISMF_CONTEXT_TRANSFER";the new SMF instance identifier if the cause in statusInfo is "SMF_CONTEXT_TRANSFER".
newSmfSetId|Conditional|This IE may be present if resourceStatus in statusInfo is:TRANSFERREDWhen present, it shall include:The new I-SMF set identifier if cause in statusInfo is "ISMF_SERVICE_CONTEXT_TRANSFER";The new SMF set identifier if cause in statusInfo is "SMF_SERVICE_CONTEXT_TRANSFER",
oldSmfId|Conditional|This IE shall be present if resourceStatus in statusInfo is:TRANSFERREDWhen present, it shall include:The old I-SMF instance identifier if cause in statusInfo is "ISMF_CONTEXT_TRANSFER";The old SMF instance identifier if cause in statusInfo is "SMF_CONTEXT_TRANSFER".
oldSmContextRef|Conditional|This IE may be present if resourceStatus in statusInfo is:TRANSFERREDWhen present, this IE shall include the identifier of the SM Context resource in the old I-SMF or SMF.
##### PduSessionCreateData 
PduSessionCreateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
supi|Conditional|除非UE是紧急注册和无ICCI，否则该IE应该存在。当出现时，它应包含用户永久标识。
unauthenticatedSupi|Conditional|如果消息中存在SUPI，但未经过身份验证，且为紧急注册UE，则该IE应出现。在目前的情况下，应设置为：true：未认证SUPI；false （默认）：认证成功的SUPI。
pei|Conditional|如果UE处于紧急注册状态，且UE处于紧急状态或SUPI未认证，则该IE应出现。对于所有其他情况，如果有，该IE将会出现。当出现时，它应包含永久设备标识。
pduSessionId|Conditional|除EPS到5GS空闲模式移动性或N26接口切换外，该IE应存在。当出现时，它应该包含PDU会话标识。
dnn|Mandatory|除EPS到5GS空闲模式移动性或N26接口切换外，该IE应存在。当出现时，它应包含所要求的DNN。
sNssai|Conditional|该IE在PDU会话建立过程中存在，此时应包含所请求的S-NSSAI，对应服务PLMN的S-NSSAI，从允许的NSSAI中获得S-NSSAI。在EPS到5GS空闲模式的移动性或N26接口切换时，该IE也应该存在，此时应包含AMF中配置的EPS互通的S-NSSAI。
ismfId|Conditional|在有I-SMF的PDU会话场景下，该IE应存在。当出现时，它应该包含I-SMF标识。
requestType|Conditional|如果请求与现有的PDU会话或现有的紧急PDU会话有关，除了使用N26接口的EPS到5GS空闲模式的移动性或切换流程外，该IE应该出现。当出现时，它应指示该请求是指新的PDU会话还是紧急PDU会话，或者是已有的PDU会话或紧急PDU会话。
epsBearerId|Conditional|在EPS到5GS空闲模式移动性或N26接口切换流程中，该IE应该出现。当出现时，它应指包含从MME收到的EPS承载标识。
pgwS8cFteid|Conditional|在EPS到5GS空闲模式移动性或N26接口切换流程中，该IE应该出现。当出现时，它应该包含Base64编码字节，对从MME收到的控制平面的PGW S8 F-TEID进行编码。
ismfPduSessionUri|Conditional|在有I-SMF的PDU会话场景下，该IE应存在。当出现时，它应该在I-SMF中包含代表PDU会话的URI。
icnTunnelInfo|Conditional|在有I-SMF的PDU会话场景下，该IE应存在，除非控制平面CIoT 5GS优化被启用，并且该PDU会话选择通过NEF进行数据传送。当出现时，它应该包含I-SMF控制的I-UPF的N9隧道信息。
n9ForwardingTunnelInfo|Conditional|如果由SMF控制的I-UPF上有可用的缓冲数据，则在有I-SMF的服务请求流程中，该IE应存在。当出现时，它应该包含I-SMF控制的I-UPF的N9隧道信息。
anType|Mandatory|该IE应在PDU会话接入网类型变化时出现。
ratType|Conditional|修改RAT类型时，该IE应出现，并指示UE使用的RAT类型。
ueLocation|Conditional|当出现时，它应该包含UE的位置信息。
ueTimeZone|Conditional|如果有UE时区，该IE将包含UE时区。
addUeLocation|Optional|UE的附加位置。如果an Type指示非3GPP接入，且有有效的3GPP接入用户位置信息，则该IE可能存在。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置获取位置信息时的UTC时间。
gpsi|Conditional|如果该IE可用，则该IE应出现。当出现时，该IE应包含用户的GPSI。
n1SmInfoFromUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
pcfId|Optional|当出现时，该IE应包含AMF为UE选择的PCF的标识（用于接入和移动性策略控制）。
hoPreparationIndication|Conditional|在有N26接口的4G切换到5G切换准备流程或者有I-SMF插入的N2切换准备流程中，该IE应该存在，且取值应该设置为true。
selMode|Conditional|如果该IE可用，则该IE应显示。当出现时，它应指示所请求的DNN是否对应显式订阅的DNN或通配符订阅的使用。
alwaysOnRequested|Conditional|如果UE请求建立一个永久在线的PDU会话，并且I-SMF的本地策略允许，该IE应存在，且取值应该设置为true。
udmGroupId|Optional|当出现时，它应指示为UE服务的UDM组的标识。
routingIndicator|Optional|当出现时，它应指示UE的路由指示。
epsInterworkingInd|Optional|当选择PGW的-C+SMF服务于PDU Session时，AMF可以提供指示。当出现时，该IE应指示PDU会话是否可能移动到EPS，以及EPS互操作过程中是否使用N26接口。AMF可以从不同的来源获取指示的值，如UE无线能力（如，支持S1模式）、UE签约数据、核心网类型限制（DNN）和“与EPS指示的互操作”（DNN）和配置。
iSmfServiceInstanceId|Optional|当该UE出现时，它包含服务于PDU会话的I-SMF服务实例的serviceInstanceId。SMF可以使用此IE来识别受I-SMF服务故障或重启影响的PDU会话。
recoveryTime|Optional|服务PDU会话的I-SMF服务实例启动/重启的时间戳。
oldPduSessionId|Conditional|如果从UE接收到该信息，该IE将会出现。当出现时，它将包含从UE接收到的旧PDU会话ID。
epsBearerCtxStatus|Conditional|在EPS到5GS空闲模式移动性或N26接口切换流程中，如果接受到了创建上下文请求，则该IE应存在。当出现时，应将其设置为创建上下文请求消息中的值。
amfNfId|Conditional|除PDU会话和监管服务有关的场景外，该IE应存在。当出现时，它应该包含在UE请求的PDU会话建立过程中，为其服务的AMF的标识符。
guami|Conditional|该IE应包含服务AMF的GUAMI。如果NF服务使用者是AMF，则应包括它。
dnaiList|Conditional|在PDU会话中如果有I-SMF插入的场景，该IE应该存在在N16a接口上。当出现时，它应包含I-SMF支持的DNAI列表。
presenceInLadn|Conditional|如果DNN对应的是LADN，则该IE应该出现，应该设置为in或out，以指示UE在LADN服务区内或不在服务区。
##### PduSessionCreatedData 
PduSessionCreatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pduSessionType|Mandatory|该UE指示用户的PDU会话类型
sscMode|Mandatory|该UE指示用户的PDU会话的SSC Mode。
cnTunnelInfo|Conditional|有I-SMF的PDU会话场景下，该IE应存在，除非控制平面CIoT 5GS优化被启用，并且该PDU会话选择通过NEF进行数据传送。当出现时，它应该包含I-SMF控制的I-UPF的N9隧道信息。
sessionAmbr|Conditional|该UE指示用户的PDU会话的保证的会话AMBR。
qosFlowsSetupList|Conditional|该UE包含PDU会话应该创建的QoS流信息。
smfInstanceId|Conditional|有I-SMF的PDU会话场景下，该IE应存在。当出现时，它应该包含SMF的标识。
pduSessionId|Conditional|在EPS到5GS空闲模式移动性或N26接口切换时，该IE应存在。当出现时，应设置为PDU会话ID。
sNssai|Conditional|在EPS到5GS空闲模式移动性或N26接口切换时，该IE应存在。当出现时，它应包含PDU会话的S-NSSAI信息。
ueIpv4Address|Conditional|在SMF为PDU会话分配了IPv4地址时，该IE应存在。
ueIpv6Prefix|Conditional|在SMF为PDU会话分配了IPv4地址前缀时，该IE应存在。
n1SmInfoToUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
gpsi|Conditional|如果请求中没有提供GPSI IE，例如对于移动到另一种接入方式的PDU会话，并且SMF知道GPSI已经与PDU会话关联，则该IE应存在。当出现时，它应包含与PDU会话相关联的用户GPSI。
smfServiceInstanceId|Optional|当出现时，该IE应包含服务于PDU会话上下文的SMF服务实例的service instance id。该IE可用于AMF识别SMF服务实例的失败或重启影响的PDU会话上下文。
recoveryTime|Optional|服务PDU会话的SMF服务实例启动/重启的时间戳。
dnaiList|Conditional|在PDU会话中如果有I-SMF插入的场景，该IE应该存在在N16a接口上。当出现时，它应包含I-SMF支持的DNAI列表。
##### PduSessionCreateError 
PduSessionCreateError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|提供关于错误的信息。
n1smCause|Conditional|如果请求中包含n1SmInfoFromUe，则该IE应存在。当出现时，它应该包含SMF建议I-SMF发给UE的5GSM原因。
n1SmInfoToUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
backOffTimer|Optional|当该IE出现时，它应该指示Back-off定时器，I-SMF在向UE发送NAS消息时可能使用。
recoveryTime|Optional|SMF服务实例启动/重启时的时间戳。
##### HsmfUpdateData 
HsmfUpdateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
requestIndication|Mandatory|当该UE出现时，它指示PDU会话的请求类型。
pei|Conditional|如果它是可用的，并且还没有提供给SMF，则该IE应存在。当出现时，该IE应包含永久设备标识符。
icnTunnelInfo|Conditional|在有I-SMF的PDU会话场景下，该IE应存在，除非控制平面CIoT 5GS优化被启用，并且该PDU会话选择通过NEF进行数据传送。当出现时，它应该包含I-SMF控制的I-UPF的N9隧道信息。
anType|Conditional|该IE应在PDU会话接入网类型变化时出现，例如在3GPP接入和非可信非3GPP接入之间的PDU会话切换期间。当出现此IE时，该IE应指示PDU会话要关联的接入网类型。
ratType|Conditional|修改RAT类型时，该IE应出现，并指示UE使用的RAT类型。
ueLocation|Conditional|如果该IE可用，并且需要上报给SMF或H-SMF（如，用户位置发生改变或者PDU会话的用户面被去激活），则该IE应该出现。当该IE出现时，该IE应包含：UE位置信息；获取UeLocation信息的UTC时间。
ueTimeZone|Conditional|如果该IE可用，则UE的时区已经改变，需要上报给SMF。当出现该IE时，该IE应包含UE的时区。
addUeLocation|Optional|UE的附加位置。如果anType指示非3GPP接入且有有效的3GPP接入用户位置信息，则该IE可能存在。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置；表示获取位置信息时的UTC时间。
n1SmInfoFromUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
qosFlowsRelNotifyList|Conditional|如果QoS流已经被释放，该IE应存在。
qosFlowsNotifyList|Conditional|如果GBR QoS流有变更时，该IE应存在。
epsBearerId|Conditional|在使用N26接口的4G切换到5G空闲模式移动性流程中，该IE应该存在。当它出现时，它应包含切换成功的EPS承载ID列表。当没有PDU会话切换成功时，该数组为空。
hoPreparationIndication|Conditional|在有N26接口的4G切换到5G切换准备流程或者有I-SMF插入的N2切换准备流程中，该IE应存在，且取值应该设置为true。
revokeEbiList|Conditional|该IE应用于请求SMF撤销部分EBI。当出现时，它应包含撤销的EBI。
alwaysOnRequested|Conditional|如果UE请求建立一个永久在线的PDU会话，并且I-SMF的本地策略允许，该IE应存在，且取值应该设置为true。
epsInterworkingInd|Optional|如果在创建PDU会话时已经提供了指示，并且在创建会话或上次更新之后，它的值发生了变化，那么该IE可能会出现。当出现时，该IE应指示PDU会话是否可能移动到EPS，以及EPS互操作过程中是否使用N26接口。
anTypeCanBeChanged|Conditional|在服务请求流程中如果可以PDU会话的接入网络类型，该IE应存在并设置为true。
psaInfo|Conditional|在有I-SMF的PDU会话场景下，如果I-SMF插入、移除了一个或多个PSA-UPF，该UE应存在。
ulclBpInfo|Conditional|在有I-SMF的PDU会话场景下，如果插入、移除独立于本地PSA-UPF的UL CL或BP UPF，该UE应存在。
n4Info|Optional|如果I-SMF需要向SMF发送N4信息（例如，流量使用报告），以便在由I-SMF控制的PSA UPF处卸载流量，该IE可能存在。
presenceInLadn|Conditional|如果DNN对应的是LADN，该IE应出现，应该设置为in或out，以指示UE在LADN服务区内或不在服务区。
ismfPduSessionUri|Conditional|在PDU会话修改流程中，当I-SMF改变时，该IE应存在。当它出现时，它应该包含新的I-SMF的URI。
ismfId|Conditional|在PDU会话修改流程中，当I-SMF改变时，该IE应存在。当它出现时，它应该包含新的I-SMF的标识。
iSmfServiceInstanceId|Optional|在PDU会话修改流程中，当I-SMF改变时，该IE应存在。当它出现时，它应该包含新的I-SMF的serviceInstanceId。
dnaiList|Conditional|在PDU会话中如果有I-SMF插入的场景，该IE应该存在在N16a接口上。当出现时，它应该包含I-SMF支持的DNAI列表。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应出现。
##### HsmfUpdatedData 
HsmfUpdatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
n1SmInfoToUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
n4Info|Optional|如果SMF需要向I-SMF发送N4信息（例如，流量使用报告），该IE可能存在。
dnaiList|Conditional|在PDU会话中如果有I-SMF插入的场景，该IE应该存在在N16a接口上。当出现时，它应包含I-SMF支持的DNAI列表。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应出现。
##### HsmfUpdateError 
HsmfUpdateError的数据结构参见下表： 
Attribute name|Presence requirement|Description
---|---|---
error|Mandatory|提供关于错误的信息。
n1smCause|Conditional|如果请求中包含n1SmInfoFromUe，则该IE应存在。当出现时，它应该包含SMF建议I-SMF发给UE的5GSM原因。
n1SmInfoToUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
backOffTimer|Optional|当该IE出现时，它应该指示Back-off定时器，I-SMF拒绝向UE发送NAS消息时可能使用。
recoveryTime|Optional|SMF服务实例启动/重启时的时间戳。
##### VsmfUpdateData 
VsmfUpdateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
requestIndication|Mandatory|当该UE出现时，它指示PDU会话的请求类型。
sessionAmbr|Conditional|如果PDU会话授权的会话AMBR被修改，则该IE应出现。当出现时，它应包含为PDU会话授权的新会话AMBR。
qosFlowsAddModRequestList|Conditional|如果请求建立或修改QoS流，则该IE应出现。
qosFlowsRelRequestList|Conditional|如果请求释放QoS流，则该IE应出现。
epsBearerInfo|Conditional|如果PDU会话移动到4G，并且对应的承载信息已更改，则该IE应存在。当出现时，仅包含新的承载信息或者已经有变化的承载信息。
assignEbiList|Conditional|如果SMF请求分配EBI，则该IE应出现。
revokeEbiList|Conditional|该IE应用于请求SMF撤销部分EBI。当出现时，它应包含撤销的EBI。
modifiedEbiList|Conditional|如果PDU会话修改过程导致已分配EBI的QoS流的ARP改变，则该IE应出现。
n1SmInfoToUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应引用N1sInfoFromue的二进制数据。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应出现。
cause|Optional|当出现时，该IE应指示请求修改的原因。
n1smCause|Optional|如果请求中包含n1SmInfoFromUe，则该IE应存在。当出现时，它应该包含SMF建议I-SMF发给UE的5GSM原因。
backOffTimer|Optional|当该IE出现时，它应该指示Back-off定时器，I-SMF在向UE发送NAS消息时可能使用。
dnaiList|Conditional|在PDU会话中如果有I-SMF插入的场景，该IE应该存在在N16a接口上。当出现时，它应包含I-SMF支持的DNAI列表。
n4Info|Optional|如果SMF需要向I-SMF发送N4信息（例如，流量使用报告），该IE可能存在。
##### VsmfUpdatedData 
VsmfUpdatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
qosFlowsAddModList|Conditional|如果QoS流创建或修改成功，则该IE应出现。
qosFlowsRelList|Conditional|如果QoS流释放成功，则该IE应出现。
qosFlowsFailedtoAddModList|Conditional|如果QoS流创建或修改失败，则该IE应出现。
qosFlowsFailedtoRelList|Conditional|如果QoS流释放失败，则该IE应出现。
n1SmInfoFromUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
ueLocation|Conditional|当该IE出现时，它应该包含UE的位置信息。
ueTimeZone|Conditional|当该IE出现时，它应该包含新的UE的时区信息。
addUeLocation|Optional|UE的附加位置。如果之前上报的无线类型是非3GPP接入且有有效的3GPP接入用户位置信息，则可能存在该IE。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置时间戳，UE的附加位置获取的时间
assignedEbiList|Conditional|如果AMF请求分配EBI，则该IE应出现。当出现时，它应包含已经成功分配的EBI列表。
failedToAssignEbiList|Conditional|如果AMF分配EBI失败，则该IE应出现。
releasedEbiList|Conditional|如果NF服务消费者要求撤销EBI，或者AMF撤销已经分配给I-SMF的EBI，则该IE应出现。该IE应包含AMF为PDU会议释放的EBI列表。
n4Info|Optional|如果I-SMF需要向SMF发送N4响应信息，以控制由I-SMF控制的PSA处卸载的流量，该IE可能存在。
##### VsmfUpdateError 
VsmfUpdateError的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
error|Mandatory|提供关于错误的信息。
n1smCause|Conditional|如果请求中包含n1SmInfoFromUe，则该IE应存在。当出现时，它应该包含SMF建议I-SMF发给UE的5GSM原因。
n1SmInfoFromUe|Conditional|如果I-SMF已从UE接收到不需要由I-SMF解析的已知N1 SM信息，该IE应存在。当出现时，它应该引用N1sInfoFromue的二进制数据。
failedToAssignEbiList|Conditional|如果AMF分配EBI失败，则该IE应出现。
ngApCause|Conditional|如果信息可用，并且根据I-SMF的政策允许将该信息发送给SMF，则该IE应出现。当该IE出现时，它应包含请求PDU会话释放的NGAP原因。
5gMmCauseValue|Conditional|当I-SMF从AMF收到了该消息，并且根据I-SMF的策略可以发送给SMF，则该IE应出现。
recoveryTime|Optional|SMF服务实例启动/重启时的时间戳。
n4Info|Optional|如果I-SMF需要向SMF发送N4响应信息，以控制由I-SMF控制的PSA处卸载的流量，该IE可能存在。
##### ReleaseData 
ReleaseData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
cause|Conditional|当该IE出现时，它指示NF消费者发起PDU会话释放的原因。
ngApCause|Conditional|如果信息可用，并且根据I-SMF的政策允许将该信息发送给SMF，则该IE应出现。当该IE出现时，它应包含请求PDU会话释放的NGAP原因。
5gMmCauseValue|Conditional|当I-SMF从AMF收到了该消息，并且根据I-SMF的策略可以发送给SMF，则该IE应出现。
ueLocation|Conditional|当该IE出现时，它应包含UE的位置信息。
ueTimeZone|Conditional|当该IE出现时，它应包含新的UE的时区信息。
addUeLocation|Optional|UE的附加位置。如果之前上报的无线类型是非3GPP接入且有有效的3GPP接入用户位置信息，则可能存在该IE。在目前的情况下，应包括：最后一个已知的3GPP接入用户位置时间戳，UE的附加位置获取的时间
##### ReleasedData 
ReleasedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
smallDataRateStatus|Conditional|如果NF服务消费者表示支持CIoT，并且可用，则该IE应出现。当出现时，它应该指示PDU会话的当前小数据速率控制状态。
apnRateStatus|Conditional|如果NF服务消费者表示支持CIoT，并且可用，则该IE应出现。当出现时，它应该指示PDN连接的当前APN速率控制状态（UE到该APN的所有PDN连接共享的APN速率）。
##### StatusNotification 
StatusNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
statusInfo|Mandatory|该IE应包含PDU会话的状态信息。
### Nnssf 
#### Nnssf接口协议简介 
场景描述 :Nnssf是NSSF为其他NF提供服务的接口。 
图1  Nnssf接口示意图
[]images/1.png)
协议栈 :图2  服务化接口协议栈
[]images/2.png)
Nnssf和其他所有服务化接口一样，都采用如上图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
##### 网络功能服务列表 
NSSF通过Nnssf接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括下表所定义的各种： 
NF|NFS|NFS的解释
---|---|---
NSSF|Nnssf_NSSelection|用于服务PLMN和HPLMN的网络切片选择。用于AMF重分配流程注册流程、UE配置更新流程、SMF选择流程。AMF可以调用NSSF的Nnssf_NSSelection_Get来获取：允许的NSSAI、配置的NSSAI、目标AMF集合或候选AMF列表，允许NSSAI的映射关系（可选）配置的NSSAI的映射关系（可选）与允许NSSAI的网络切片实例关联的NSI标识（可选）NRF，用于在选择的网络切片实例中和选择NF/业务，以及在注册过程中从AMF集合中确定候选AMF列表在服务PLMN或当前TA中拒绝的S-NSSAI的信息在PDU会话建立过程中，用于在选定的网络切片实例中选择NF/服务的NRF，以及与输入中提供的S-NSSAI关联的NSI标识。
Nnssf_NSSAIAvailability|NSSF|该服务用于NF服务消费者 (如， AMF) 在NSSF上更新AMF支持的S-NSSAI，订阅和取消订阅每个TA下NSSAI可用性信息的变化通知。
#### 服务操作解释 
##### Nnssf_NSSelection_Get 
服务操作|操作语义|服务操作的解释
---|---|---
Nnssf_NSSelection_Get|Request/Response|用于AMF重分配流程注册流程、UE配置更新流程、SMF选择流程。在注册过程中，NF服务消费者（如，AMF）获取允许的NSSAI、配置的NSSAI、目标AMF集合或候选AMF列表以及其他可选信息。AMF向NSSF发送GET请求，其中包含一个或多个参数作为查询参数：请求的NSSAI，签约的S-NSSAI，默认S-NSSAI的标识，SUPI的PLMN ID，TAI，NF服务消费者的NF类型，请求者ID。在PDU会话建立过程中，NF服务消费者（如，AMF）获取NRF和网络切片实例的NSI标识。NF服务消费者（如，AMF）向NSSF发送GET请求，请求中应包含查询参数，至少包含S-NSSAI、NF业务消费者的NF类型和请求者ID，对于服务PLMN中发起的流程，查询参数中也应包含非漫游/LBO漫游/HR漫游指示、SUPI的PLMN ID和TAI。在如下成功的情况下，NSSF返回200 OK：NSSF能够为请求的网络切片选择信息找到授权的网络切片信息，响应主体包括允许的NSSAI、目标AMF集合或候选AMF列表。NSSF不能找到请求的切片选择信息的切片实例，响应体中应该包含一个空的“AuthorizedNetworkSliceInfo”JSON对象。在失败时，NSSF将返回一个403状态码和ProblemDetails的数据结构。
##### Nnssf_NSSAIAvailability_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Nnssf_NSSAIAvailability_Update|Request/Response|NF服务消费者（如，AMF）使用此服务操作向NSSF更新NF服务消费者每个TA下支持的S-NSSAI，并获取每个TA下其支持的S-NSSAI的可用性。NF服务消费者（如，AMF）应向NSSF发送PUT请求，为了替换或创建NSSAI可用性信息，正文的净荷中应包含NSSAIAvailabilityInfo，该NssaiAvailabilityInfo包含要替换一个或多个的支持的S-NSSAI信息。NF服务消费者（如，AMF）应向NSSF发送PATCH请求，为了更新NSSAI可用性信息，正文的净荷中应包含PatchDocument，其中包含一个或多个PatchItem指令用于更新支持的S-NSSAI信息。成功后返回200 OK，PUT/PATCH响应的净荷体包含AuthorizedNssaiAvailabilityInfo。在失败的情况下，NSSF将返回一个403/404状态代码和包括ProblemDetails的响应体。
##### Nnssf_NSSAIAvailability_Subscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nnssf_NSSAIAvailability_Subscribe|Subscribe/Notify|此服务操作用于NF服务消费者（如，AMF）订阅NSSAI可用性信息状态的任何变化通知（如，每TA可用的S-NSSAI，以及UE的服务PLMN中的TA的限制S-NSSAI(s)），这个NSSAI可用性信息状态变化是由另一个AMF更新的。NF服务消费者应发送POST请求在NSSF中创建订阅资源，POST请求的净荷主体包含NssfEventSubscriptionCreateData。成功时返回201Created，响应消息的净荷体应包含NssfEventSubscriptionCreatedData中。在失败的情况下，NSSF将返回一个403/404状态代码和包括ProblemDetails的响应体。
##### Nnssf_NSSAIAvailability_Unsubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nnssf_NSSAIAvailability_Unsubscribe|Subscribe/Notify|用于NF服务消费者（如，AMF）取消任何先前订阅的NSSAI可用性信息的变更通知。NF服务使用者应发送删除请求以删除NSSF中已有的订阅资源。如果请求被接受，NSSF应响应204 NO Content，表示删除订阅ID所标识的资源成功。在失败的情况下，NSSF将返回一个404状态代码和包括ProblemDetails的响应体。
 
##### Nnssf_NSSAIAvailability_Notify 
服务操作|操作语义|服务操作的解释
---|---|---
Nnssf_NSSAIAvailability_Notify|Subscribe/Notify|NSSF使用通知服务操作向NF服务消费者（如，AMF）更新状态变化，每TA下限制的S-NSSAI的可用性以及该TA下每个PLMN的限制S-NSSAI。NSSF应向NF服务消费者（如，AMF）发送POST请求，POST请求的净荷体应包含NssfEventNotification。成功时，应返回204 No Content，响应的净荷体为空。
##### Nnssf_NSSAIAvailability_Delete 
服务操作|操作语义|服务操作的解释
---|---|---
Nnssf_NSSAIAvailability_Delete|Request/Response|NF服务消费者（如，AMF）使用删除服务操作删除NSSF中存储的给NF服务消费者的NSSAI可用性信息。NF服务消费者（如，AMF）发送删除请求，以删除由{nfId}（如，AMF标识）所代表的NF服务消费者的NSSAI可用性信息。NSSF应删除个人AMF的NSSAI可用性信息，并返回204 No Content。
#### 数据类型解释 
##### AuthorizedNetworkSliceInfo 
AuthorizedNetworkSliceInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
allowedNssaiList|Conditional|如果NSSF收到请求的NSSAI和签约的S-NSSAI，或者对应请求中的“requestmapping”标志为“true”，则该IE应包含NSSF在服务PLMN中授权的允许的S-NSSAI。
configuredNssai|Conditional|如果NSSF没有收到请求的NSSAI，或者请求的NSSAI中包含的S-NSSAI在服务PLMN中不有效，则该IE将包含NSSF在服务PLMN中授权的配置的S-NSSAI。
targetAmfSet|Optional|NSSF根据配置以及NSSF是否接收到请求的NSSAI和签约的S-NSSAI决定是否包含此IE。当出现时，该IE应包含目标AMF集合。如果请求消息中包含“请求映射”IE，并且设置为“true”，则不包含此IE。
candidateAmfList|Optional|NSSF根据配置以及NSSF是否接收到请求的NSSAI和签约的S-NSSAI决定是否包含此IE。当该IE出现时，该IE应包含候选AMF(s)的列表。如果请求消息中包含“请求映射”IE，并且设置为“true”，则不包含此IE。
rejectedNssaiInPlmn|Optional|如果NSSF接收到请求的NSSAI和签约的S-NSSAI，则该IE可能包含在NSSF中。当出现此IE时，该IE应包含在PLMN中被拒绝的NSSAI。
rejectedNssaiInTa|Optional|如果NSSF收到请求的NSSAI和签约的S-NSSAI，则该IE可能包含在NSSF中。在当前TA中，该IE应包含拒绝的NSSAI
nsiInformation|Conditional|如果NSSF接收到S-NSSAI，则NSSF包含该IE。（如，PDU会话建立过程中）如果请求消息中包含“请求映射”IE，并且设置为“true”，则不包含此IE。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现
nrfAmfSet|Optional|NSSF根据配置以及是否消息中是否包含目标AMF集合，来决定是否包含该IE。当出现时，该IE应包含NRF的API URI，用于从AMF集合中确定候选AMF列表。
##### SubscribedSnssai 
SubscribedSnssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscribedSnssai|Mandatory|该IE应包含签约的S-NSSAI。
defaultIndication|Optional|如果配置了，则签约的S-NSSAI为默认签约的S-NSSAI。
##### AllowedSnssai 
AllowedSnssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
allowedSnssai|Mandatory|该IE应包含服务PLMN中允许的S-NSSAI。
nsiInformation|Optional|当NSSF向NF服务消费者 (如，AMF) 提供允许的NSSAI信息时，该IE可能出现。如果存在，该IE应包含与允许的S-NSSAI对应的网络切片实例相关的信息。
mappedHomeSnssai|Optional|当该信元存在时，该信元应包含服务PLMN中允许的S-NSSAI对应的归属网络的S-NSSAI值。
##### AllowedNssai 
AllowedNssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
allowedSnssaiList|Mandatory|该IE应包含服务PLMN中允许的S-NSSAI。
accessType|Mandatory|该IE应包含该允许NSSAI所属的接入类型。
##### NsiInformation 
NsiInformation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
nrfId|Mandatory|该IE应包含NRF的API URI，用于在选定的网络切片实例中选择NF/服务。
nsiId|Optional|当出现时，该IE应包含所选网络切片实例的标识。
##### MappingOfSnssai 
MappingOfSnssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
servingSnssai|Mandatory|该IE包含服务网络的S-NSSAI值。
homeSnssai|Mandatory|该IE应包含归属网络的S-NSSAI映射值。
##### SliceInfoForRegistration 
SliceInfoForRegistration的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscribedNssai|Conditional|在初始注册过程中或5GS中的移动性注册过程中必须包含该IE。该IE应包含签约的S-NSSAI列表和每个S-NSSAI的指示（如果是默认S-NSSAI）。
allowedNssaiCurrentAccess|Conditional|该IE应包含在5GS的初始注册过程中或移动注册更新过程中，以原生的5G-GUTI作为旧的GUTI，在NF服务使用者 (如， AMF) 上可以UE当前接入类型可用的允许的NSSAI。
allowedNssaiOtherAccess|Conditional|该IE在5GS的初始注册过程中或移动注册更新过程中，以原生的5G-GUTI作为旧的GUTI时，如果UE已经注册到NF服务消费者 (如， AMF) 对于另一种访问类型，在NF服务消费者 (如， AMF) 上可以使用另一种访问类型的允许NSSAI。
sNssaiForMapping|Conditional|如果requestMapping IE设置为true，则包含该IE。当包含时，该IE应包含从EPS到5GS的PDU会话从HPLMN的SMF+PGW-C获取的S-NSSAI集合。
requestedNssai|Optional|该IE可能包含UE请求的S-NSSAI集合。
defaultConfiguredSnssaiInd|Conditional|当UE在注册过程中包含默认配置的NSSAI指示时，该IE应该出现。true：默认配置的NSSAI由UE指示。FALSE（默认）：默认配置的NSSAI不由UE指示。
requestMapping|Conditional|该IE可能在EPS到5GS移动注册过程（空闲和连接状态）使用N26接口时被调用。当该IE向NSSF指示时，NSSF应该向Nnssf_NSSelection_Get返回VPLMN特定映射的SNSSAI值。
##### SliceInfoForPDUSession 
SliceInfoForPDUSession的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
sNssai|Mandatory|当AMF查询服务PLMN的NSSF时，该信元中包含请求的S-NSSAI。
roamingIndication|Mandatory|该IE应包含UE是否处于非漫游、LBO漫游或HR漫游的指示。
##### ConfiguredSnssai 
ConfiguredSnssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
configuredSnssai|Mandatory|该IE应包含在服务PLMN中配置的S-NSSAI。
##### NSSAIAvailabilityInfo 
NSSAIAvailabilityInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
supportedNssaiAvailabilityData|Mandatory|该IE应包含NF服务使用者（如，AMF）和5G-RAN在每TA下支持S-NSSAI的信息。
supportedFeatures|Conditional|如果支持至少一个可选特性，则该IE应该出现。
##### AuthorizedNssaiAvailabilityInfo 
AuthorizedNssaiAvailabilityInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
tai|Mandatory|该IE应包含跟踪区的标识符。
supportedSnssaiList|Mandatory|该IE包含NSSF授权的AMF和5G-(R)AN支持的该TA下的S-NSSAI。
restrictedSnssaiList|Optional|该IE可能包含每个PLMN内该TA下的限制的S-NSSAI。
##### PatchDocument 
PatchDocument的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
N/A|Mandatory|在NSSF上更新NSSAI可用性信息的一组PATCH指令。
##### NssfEventSubscriptionCreateData 
NssfEventSubscriptionCreateData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
nfNssaiAvailabilityUri|Mandatory|标识NF服务消费者（如，AMF）发送的此订阅通知的接收者。
taiList|Mandatory|NF服务消费者（如，AMF）支持的TAI。
event|Mandatory|描述此次订阅的事件。
expiry|Optional|当出现此IE时，该IE应表示订阅失效后的建议时间。
##### NssfEventSubscriptionCreatedData 
NssfEventSubscriptionCreatedData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscriptionId|Mandatory|标识创建的订阅的订阅ID。
expiry|Conditional|表示订阅事件停止生成报告，订阅失效的时间。在到达这个失效时间后，NF服务消息应删除可能存在的订阅的表示。
authorizedNssaiAvailabilityData|Optional|如果有授权的NSSAI可用 ，则NSSF包含该IE。
##### NssfEventNotification 
NssfEventNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
subscriptionId|Mandatory|表示订阅产生的事件通知。
authorizedNssaiAvailabilityData|Mandatory|包含授权的NSSAI可用性信息，每一个元素应包含TA中可用S-NSSAI列表的当前状态以及该TA内每个PLMN限制的S-NSSAI列表。
### Nnrf 
#### Nnrf接口协议简介 
场景描述 :Nnrf是NRF为其他NF提供服务的接口。（下图参考协议29.510中的Figure 4-1: 5G System architecture） 
图1  Nnrf接口示意图
[]images/1.png)
协议栈 :图2  服务化接口协议栈
[]images/2.png)
Nnrf和其他所有服务化接口一样，都采用如上图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
##### 网络功能服务列表 
NRF通过Nnrf接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括下表所定义的各种： 
NF|NFS|NFS的解释
---|---|---
NRF|Nnrf_NFManagement|允许NF实例属性在所属PLMN的NRF上注册、更新、去注册。允许NRF实例在同一个PLMN中的另一个NRF中注册、更新或去注册其属性信息。也可以使用其他方式更新或去注册NRF Profile，例如，可以通过OA&M更新或去注册NRF Profile。允许NF订阅以收到新注册的NF实例和NFS的通知。允许检索当前NRF上已注册的NF实例列表或指定NF实例的属性。
Nnrf_NFDiscovery|NRF|允许NF实例通过查询本PLMN的NRF发现其他NF提供的NFS。允许PLMN内的NRF向其他PLMN（如某特定UE所在的PLMN）内的NRF重新发起发现请求。
Nnrf_AccessToken|NRF|NRF提供了Nnrf_AccessToken服务（用于OAuth2授权），遵循“Client Credentials”授权粒度，公开了一个“Token Endpoint”，其中，NF服务消费者可以请求Access Token Request服务。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Nnrf接口上提供的各服务以及各服务支持的服务操作见下表： 
服务名称|操作|服务操作的解释
---|---|---
Nnrf_NFManagement|NFRegister|本服务操作用于以下场景：该服务操作用于注册请求NF到NRF，向NRF传输NF Profile，NRF收到注册请求后，标记请求NF为可用，便于其他NF发现。注册已存在NF实例的关联业务；将NRF信息注册到另一个NRF中，用于转发或重定向服务发现请求。
NFUpdate|Nnrf_NFManagement|该服务操作用于更新已注册到NRF的NF Profile，向NRF提供更新后的请求NF Profile。通过NFUpdate服务操作可全量更新NF Profile，或者只更新部分属性参数（包括添加/删除/替换NF属性信息中的服务）。
NFDeregister|Nnrf_NFManagement|该服务操作用于删除已在NRF中注册的NF Profile。
NFStatusSubscribe|Nnrf_NFManagement|本服务操作用于以下场景：创建订阅。当满足特定过滤条件下的给定集合NF实例在NRF中注册/去注册或属性信息发生修改时，NRF通知订阅该服务的NF。订阅特定实例，NF服务消费者通过该服务操作向NRF发送订阅请求，当请求订阅的NF Profile发生更改或者NF实例从NRF去注册时会收到通知消息。
NFStatusNotify|Nnrf_NFManagement|该服务操作给每个订阅了NF实例注册/去注册通知，或给定NF实例NF Profile变更的NF服务消费者，发送注册/去注册NF实例通知。通知被发送到订阅过程中每个NF服务消费者携带的回调URI。
NFStatusUnSubscribe|Nnrf_NFManagement|此服务操作将删除已有的订阅通知。
NFListRetrieval|Nnrf_NFManagement|该服务操作允许检索当前在NRF中注册的NF实例列表，该服务操作可以基于给定的NF类型和/或待返回的NF实例最大个数查询所有注册的NF实例或仅查询部分NF实例。
NFProfileRetrieval|Nnrf_NFManagement|此服务操作允许检索当前在NRF中注册的给定NF实例的NF Profile。
Nnrf_NFDiscovery|NFDiscover|该服务操作用于发现当前注册在NRF、并且匹配查询入参的NF实例集合（及关联的NF服务实例）。实例由NF Profile标识。在服务使用者调用此服务操作之前，应考虑是否可以重用之前搜索（服务发现）的结果。如果新服务发现请求中的输入查询参数与上一次搜索使用的查询参数相同，且结果未过期，则服务消费者应重用之前的结果。如果新查询所需的属性包含在之前查询的候选NF Profile参数中，服务消费者可以考虑重用之前的结果，在这种情况下，当重复使用上一个查询的结果时， 服务消费者需要考虑结果， 可能与执行新查询后获得的存在不同，比如发现的NFs数量不同等。
Nnrf_AccessToken|Access Token Request|该服务操作用于NF服务消费者向授权服务器 (NRF)请求OAuth2访问令牌。
##### Nnrf_NFManagement_NFRegister 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFRegister|Request/Response|NF服务消费者向NF实例的资源URI发送PUT请求，每个NF实例的URI唯一。变量{nfInstanceID}表示由NF服务消费者提供的标识符，在NF注册的NRF的PLMN内全局唯一。NF实例ID的格式为通用唯一标识符(UUID)版本4。NF服务消费者发送PUT请求，消息中包含NFProfile结构。注册成功，返回“201（ Created）”消息，PUT响应包含创建资源标识，“location”头域应包含创建资源URI。另外，NRF返回心跳定时器“heart-beat timer”属性字段，含NF实例和NRF心跳消息交互间隔（单位：秒）。PUT应答消息中包含NFProfile结构。如果由于NFProfile JSON对象的编码错误导致NF实例注册失败，NRF将返回状态码400（Bad Request），携带ProblemDetails信元提供详细错误信息。如果NRF内部错误导致NF实例注册失败，NRF将返回状态码500（Internal Server Error），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFManagement_NFUpdate 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFUpdate|Request/Response|全量更新NF服务消费者向表示NF实例的资源URI发送PUT请求，PUT请求包含NFProfile结构。更新结果：全量更新成功，NRF返回200 （OK），PUT响应包含被替换资源标识。PUT应答消息中包含NFProfile结构。如果由于NFProfile JSON对象的编码错误导致NF实例全量更新失败，NRF将返回400（Bad Request）状态码，携带ProblemDetails信元提供详细错误信息。如果NRF内部错误导致NF实例全量更新，NRF将返回状态码500（Internal Server Error），携带ProblemDetails信元提供详细错误信息。部分更新NF服务消费者向代表NF实例的资源URI发送PATCH请求，PATCH请求体指定的所有操作都必须要按照原子粒度执行。PATCH请求消息中包含PatchDocument结构。更新结果：部分更新成功，NRF返回200（OK），PUT响应包含被替换资源标识。PATCH应答消息中包含NFProfile结构。如果在NRF数据库中已注册NF实例列表中没有找到NF实例ID标识的NF实例，返回状态码404（Not Found），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFManagement_NFDeregister 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFDeregister|Request/Response|该服务操作删除由NF实例ID标识的给定资源。通过向标识特定NF实例的URI发出DELETE请求来调用该服务操作。NF服务消费者向NF实例的资源URI发送DELETE请求，DELETE请求体为空。返回消息。删除成功，返回204（No content），DELETE响应体为空。如果在NRF数据库中已注册NF实例列表中没有找到NF实例ID标识的NF实例，返回状态码404（Not Found），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFManagement_NFStatusSubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFStatusSubscribe|Subscribe/Notify|1、NF服务消费者向代表“订阅”集合资源的资源URI发送一个POST请求。POST请求体应包括标识NF服务消费者感兴趣接收的通知类型的数据；还包含回调URI，NRF根据该回调URI向NF服务消费者发送实际通知。NF服务消费者可能携带一个有效时间字段，标识期望订阅保活时间。订阅请求还可能包括一些附加参数，包含要监控的NF Profile列表（或无需监控的属性列表），以确定当上述NF Profile发生变化时，是否发送来自NRF的通知。POST请求消息中包含SubscriptionData结构。2a、订阅成功后返回201（Created），响应中包含已创建订阅相关数据，包括订阅有效期（由NRF决定）。一旦订阅失效，如果订阅者希望继续接收状态通知。需向NRF发送订阅请求，重新创建订阅。POST应答消息中包含SubscriptionData结构。2b、如果由于NFProfile JSON对象的编码错误导致订阅创建失败，NRF将返回状态码400（Bad Request），携带ProblemDetails信元提供详细错误信息。如果NRF内部错误导致订阅创建失败，NRF将返回状态码500（Internal Server Error），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFManagement_NFStatusNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFStatusNotify|Subscribe/Notify|1、NRF发送POST请求到回调URI。POST请求消息中包含NotificationData结构。如果订阅了新注册NF实例，请求体应根据NF服务消费者在订阅操作时所指示的标准，携带与新注册NF相关的数据及其服务，这些数据应包含NF实例的NF实例ID、需要通知的事件标识（“registration”），以及新的属性数据（包括NF实例可以提供的服务列表）。如果订阅了NF实例属性变更通知，请求体应包括发生属性信息变更的NF实例ID、通知事件标识（“Profile change”）和变更后的属性信息。如果订阅了NF实例去注册变更通知，请求体应包括去注册的NF实例的NF实例ID和通知事件指示（“deregistration”）。2a、通知成功，NF服务消费者返回204（No content）。POST应答体为空。2b、如果NF服务消费者认为“nfStatusNotificationURI”无效（例如，因为该URI不属于NRF中注册的NF服务消费者创建的任何订阅），NF服务消费者返回状态码404 （Not Found），携带ProblemDetails信元，提供详细错误信息。
##### Nnrf_NFManagement_NFStatusUnSubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFStatusUnSubscribe|Subscribe/Notify|1、NF服务消费者向NF订阅的资源URI发送DELETE请求，DELETE请求体为空。2a、删除成功，返回204（No content），响应体为空。2b、如果在NRF数据库中已注册NF实例列表中没有找到NF实例ID标识的NF订阅，返回状态码404（Not Found），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFManagement_NFListRetrieval 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFListRetrieval|Request/Response|1、NF服务消费者应向资源URI“nf-instances”集合资源发送HTTP GET请求。检索请求查询参数包含输入过滤条件（可选）。HTTP GET请求体为空。GET请求消息头中携带的查询参数参考Query Parameters。2a、查询成功，返回200 （OK），响应体中应包含满足检索过滤条件（例如，同一个NF类型的所有NF实例）并且已在NRF中注册的NF URI信息。或者结果中无NF信息（例如，NRF中没有注册NF，或者当前NRF注册的NF实例中没有匹配到请求nf-type的NF）。GET应答消息中包含UriList结构。2b、如果不允许NF服务消费者检索已注册的NF实例，NRF返回状态码403（Forbidden）。如果由于NFProfile JSON对象的编码错误查询失败，NRF返回400（Bad Request）状态码，携带ProblemDetails信元提供详细错误信息。如果NRF内部错误导致查询失败，NRF返回状态码500（Internal Server Error），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFManagement_NFProfileRetrieval 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFManagement_NFProfileRetrieval|Request/Response|1、NF服务消费者向资源URI“nf-instances/{nfinstanceid}”发送HTTP GET请求。HTTP GET请求体为空。2a、查询成功后，返回200（OK），响应体中包含请求消息中标识的NF实例属性信息。GET应答消息中包含NFProfile结构。2b、如果不允许NF服务消费者检索已注册的NF实例，NRF返回状态码403（Forbidden）。如果NRF内部错误导致查询失败，NRF返回状态码500（Internal Server Error），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_NFDiscovery 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_NFDiscovery|Request/Response|该服务操作是通过查询“nf-instance”资源来执行的，该请求被发送到同一个PLMN的NRF。1、NF服务消费者应向资源URI“nf-instances”集合资源发送HTTP GET请求。HTTP GET请求体为空。服务发现请求查询参数包含输入过滤条件（可选）。GET请求消息头中包含的发现参数参考Query Parameters。2a、服务发现成功，返回200 （OK），响应体中包含一个有效期，（在该有效期内，搜索结果可以被NF服务消费者缓存），以及满足搜索过滤条件的NF Profile数组（例如，能提供某种NF服务的所有NF实例）。GET响应消息中包含SearchResult结构。2b、如果不允许NF服务消费者发现查询参数中提供的请求NF类型的NF服务，NRF返回403（Forbidden）状态码，携带ProblemDetails信元提供详细错误信息。如果由于NFProfile JSON对象的编码错误导致服务发现失败，NRF返回400（Bad Request）状态码，携带ProblemDetails信元提供详细错误信息。如果NRF内部错误导致查询失败，NRF返回状态码500（Internal Server Error），携带ProblemDetails信元提供详细错误信息。
##### Nnrf_AccessToken_Get 
服务操作|操作语义|服务操作的解释
---|---|---
Nnrf_AccessToken_Get|Request/Response|1、NF服务消费者向“令牌端点（Token Endpoint）”发送一个POST请求。令牌端点为：{nrfApiRoot}/oauth2/token，其中{nrfApiRoot}表示NRF的“方案(scheme)”和“授权(authority)”组件的级联。HTTP POST请求体包含OAuth 2.0访问令牌请求（Access Token Request ）AccessTokenReq结构，包括：设置OAuth2授权类型为客户端证书授权"client_credentials"；“scope”参数，指示NF服务消费者试图访问的NF服务名称（即期望访问的NF服务名称）；如果是针对特定NF服务提供者的访问令牌请求，包含请求OAuth2.0访问令牌的NF服务消费者的NF实例ID；如果是对非特定NF服务提供者的访问令牌请求，包含NF服务消费者的NF类型；如果是对非特定NF服务提供者的访问令牌请求，提供期望的NF业务生产者的NF类型；如果是对特定NF服务提供者的访问令牌请求，提供期望的NF服务提供者的NF实例ID；如果是漫游场景下的接入令牌请求，提供归属和服务PLMN ID。如果PLMN使用传输层保护，则NF服务消费者与NRF进行相互认证使用TLS，否则NF服务消费者应使用NDS或物理安全措施。2、接入令牌成功，NRF返回200 （OK），POST响应包含获取的访问令牌和令牌类型。POST应答消息中包含AccessTokenRsp结构。除非令牌的失效时间是通过其他方式（例如部署专用文档）来提供的，否则POST响应需包含令牌的过期时间。如果访问的NF服务提供者业务超出访问令牌范围，POST响应需包含请求的NF服务提供者的NF服务名称。
#### 数据类型解释 
##### Nnrf_NFManagement specific Data Types 
###### NFProfile 
NFProfile的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
NfInstanceId|Mandatory|表示NF实例的唯一标识。
NFType|Mandatory|表示NF类型。
NFStatus|Mandatory|表示NF实例状态（注5）
heartBeatTimer|Conditional|表示NF实例给NRF发送连续2次心跳的间隔（秒）。如果该字段包含在NF注册请求中，注册请求消息应携带服务消费者配置的心跳时间。该字段应包含在NRF对注册请求(PUT方法)或NF Profile更新（PUT方法或PATCH方法）的响应消息中。如果NRF根据本地配置接受NF配置的心跳时间，则心跳定时器的值应与注册请求中保持一致；如果不接受，NRF将使用预先配置的值覆盖该值。
PlmnId|Conditional|表示NF所属的PLMN列表（注7）。如果该信息提供给NF，则消息应携带该IE。
Snssai|Optional|表示NF的S-NSSAI 。
nsiList|Optional|表示NF的网络分片实例（NSI）标识。
Fqdn|Conditional|表示NF的全量域名FQDN（注1+注2）。注册到NRF的AMF FQDN应该是AMF名称的FQDN。
interPlmnFqdn|Conditional|如果该NF需要被不同PLMN中的其他NF发现，则应注册该参数到NRF上用于跨PLMN路由（注8）。属性信息更改将触发NRF发送“NF_PROFILE_CHANGED”类型通知——“fqdn”属性变化给订阅该NF实例属于不同PLMN的NF。
Ipv4Addr|Conditional|表示NF的IPv4地址（注1+注2）
Ipv6Addr|Conditional|表示NF的IPv6地址（注1+注2）
allowedPlmns|Optional|表示允许访问NF实例的PLMN列表。
allowedNfTypes|Optional|表示允许访问该NF实例的NF类型。
allowedNfDomains|Optional|表示允许访问该NF实例的NF域名格式。
allowedNssais|Optional|表示允许访问该NF实例切片的S-NSSAI。
priority|Optional|表示NF选择时相对于同种服务类型的其他NF的优先级，取值范围0~65535；值越小，优先级越高，如果NF的nfServiceList参数包含该字段，优先选择nfServiceList中的优先级值。（注4）。NRF在向Nnrf_NFDiscovery服务开放nfprofile时，可能会覆盖之前接收到的优先级值。
capacity|Optional|表示静态容量信息，即，相对于同种业务类型的其他NF实例权重。取值范围0~65535。如果nfServiceList参数也包含容量值，优先选择nfServiceList中的容量值。（注4）
load|Optional|表示动态负载信息，及NF当前的负载百分比。取值范围为0~100。
locality|Optional|表示运营商定义的NF实例位置信息。例如地理位置，数据中心等（注3）。
UdrInfo|Optional|表示UDR数据，例如SUPI范围、组ID等。
UdmInfo|Optional|表示UDM数据，例如SUPI范围、组ID等。
AusfInfo|Optional|表示AUSF数据，例如SUPI范围、组ID等。
AmfInfo|Optional|表示AMF数据（AMF集ID）
SmfInfo|Optional|表示SMF数据，例如数据网络名称。
UpfInfo|Optional|表示UPF数据，包括S-NSSAI、数据网络名称、SMF服务区域，接口等。
PcfInfo|Optional|表示PCF数据。
BsfInfo|Optional|表示BSF数据。
ChfInfo|Optional|表示CHF数据。
recoveryTime|Optional|表示NF启动/重启时间戳（注5+注6）。
nfServicePersistence|Optional|如果携带该参数，且值为true，表示该NF实例中同一个NF服务不同服务实例（支持相同API版本）能够在共享存储中实现资源持久化，因此，在NF服务消费者选择支持同一API版本的新NF服务实例后，这些资源可供使用。否则，表示同一NF服务的NF服务实例不能共享NF实例内部资源状态。
NFService|Optional|表示NF服务实例列表，某个NF包含的服务，可被其他NF发现。
注1：NF Profile至少包含一个寻址参数，例如，fqdn，ipv4address或ipv6adress。注2：如果NF类型为UPF，则寻址信息用于UPF N4接口。注3: NF服务消费者根据寻址信息选择NF实例，例如，优选位于同一数据中心的NF实例。注4：如果携带容量和优先级参数，携带容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似。注5：如果恢复时间（recoveryTime）或NF状态（nfstatus）发生变化，NRF将发送订阅通知消息给订阅了NF Profile变化的NF。注6: NF服务消费者可能认为NF恢复之前在NF中创建的所有资源都丢失了。此时，恢复时间（recoveryTime）可以用于检测NF重启并触发相应动作，例如，释放本地资源。注7: 给定NF可以在NF Profile中注册包含在特定PLMN的多个PLMN ID。如果注册了多个PLMN ID，则该NF Profile的所有属性都应用在PLMN列表（plmnList）中注册的每个PLMN ID。例外情况下，NF Profile（包括PLMN ID），例如基于IMSI的SUPI，TAI和GUAMI等属性，只应用在单个PLMN ID，此时，NF可能会在Profile中针对每个PLMN ID都注册这些属性，例如，UDM可能会针对不同PLMN ID在NF Profile的多次注册相同属性，例如，SUPI范围（SUPI ranges）。注8：其他NF所属PLMN ID不包含在NRF配置的PLMN ID列表中，则NF所属PLMN不同。|注1：NF Profile至少包含一个寻址参数，例如，fqdn，ipv4address或ipv6adress。注2：如果NF类型为UPF，则寻址信息用于UPF N4接口。注3: NF服务消费者根据寻址信息选择NF实例，例如，优选位于同一数据中心的NF实例。注4：如果携带容量和优先级参数，携带容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似。注5：如果恢复时间（recoveryTime）或NF状态（nfstatus）发生变化，NRF将发送订阅通知消息给订阅了NF Profile变化的NF。注6: NF服务消费者可能认为NF恢复之前在NF中创建的所有资源都丢失了。此时，恢复时间（recoveryTime）可以用于检测NF重启并触发相应动作，例如，释放本地资源。注7: 给定NF可以在NF Profile中注册包含在特定PLMN的多个PLMN ID。如果注册了多个PLMN ID，则该NF Profile的所有属性都应用在PLMN列表（plmnList）中注册的每个PLMN ID。例外情况下，NF Profile（包括PLMN ID），例如基于IMSI的SUPI，TAI和GUAMI等属性，只应用在单个PLMN ID，此时，NF可能会在Profile中针对每个PLMN ID都注册这些属性，例如，UDM可能会针对不同PLMN ID在NF Profile的多次注册相同属性，例如，SUPI范围（SUPI ranges）。注8：其他NF所属PLMN ID不包含在NRF配置的PLMN ID列表中，则NF所属PLMN不同。|注1：NF Profile至少包含一个寻址参数，例如，fqdn，ipv4address或ipv6adress。注2：如果NF类型为UPF，则寻址信息用于UPF N4接口。注3: NF服务消费者根据寻址信息选择NF实例，例如，优选位于同一数据中心的NF实例。注4：如果携带容量和优先级参数，携带容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似。注5：如果恢复时间（recoveryTime）或NF状态（nfstatus）发生变化，NRF将发送订阅通知消息给订阅了NF Profile变化的NF。注6: NF服务消费者可能认为NF恢复之前在NF中创建的所有资源都丢失了。此时，恢复时间（recoveryTime）可以用于检测NF重启并触发相应动作，例如，释放本地资源。注7: 给定NF可以在NF Profile中注册包含在特定PLMN的多个PLMN ID。如果注册了多个PLMN ID，则该NF Profile的所有属性都应用在PLMN列表（plmnList）中注册的每个PLMN ID。例外情况下，NF Profile（包括PLMN ID），例如基于IMSI的SUPI，TAI和GUAMI等属性，只应用在单个PLMN ID，此时，NF可能会在Profile中针对每个PLMN ID都注册这些属性，例如，UDM可能会针对不同PLMN ID在NF Profile的多次注册相同属性，例如，SUPI范围（SUPI ranges）。注8：其他NF所属PLMN ID不包含在NRF配置的PLMN ID列表中，则NF所属PLMN不同。
###### NfInstanceId 
NfInstanceId的数据结构参见下表： 
属性名称|描述
---|---
NfInstanceId|唯一标识NF实例的字符串。 NF实例ID的格式应为通用唯一标识符（UUID）版本4。
###### NFType 
NFType的数据结构参见下表： 
属性名称|描述
---|---
NFType|枚举类型:NRFUDMAMFSMFAUSFNEFPCFSMSFNSSFUDRLMFGMLC5G_EIRSEPPUPFN3IWFAFUDSFBSFCHFNWDAF
###### NFStatus 
NFStatus的数据结构参见下表： 
属性名称|描述
---|---
NFStatus|枚举类型:REGISTERED: NF实例已注册到NRF而且能被其他NF发现。SUSPENDED: NF实例已注册到NRF，但未运行，其他NF无法发现。|枚举类型:REGISTERED: NF实例已注册到NRF而且能被其他NF发现。SUSPENDED: NF实例已注册到NRF，但未运行，其他NF无法发现。
###### PlmnId 
PlmnId的数据结构参见下表： 
属性名称|描述
---|---
Mcc|移动国家码|移动国家码
Mnc|移动网码|移动网码
###### Mcc 
Mcc的数据结构参见下表： 
属性名称|描述
---|---
Mcc|PLMN的移动国家代码部分，包括3位数字。模式：'^ [0-9] {3} $'|PLMN的移动国家代码部分，包括3位数字。模式：'^ [0-9] {3} $'
###### Mnc 
Mnc的数据结构参见下表： 
属性名称|描述
---|---
Mnc|PLMN的移动网络代码部分，包括2或3位数字。模式：'^ [0-9] {2,3} $'|PLMN的移动网络代码部分，包括2或3位数字。模式：'^ [0-9] {2,3} $'
###### Snssai 
Snssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
sst|Mandatory|标识S-NSSAI的切片/服务类型，表示期望的网络切片在特性和服务上的行为。
sd|Optional|标识S-NSSAI的切片/服务类型的多个分片，以区分同一个切片/服务类型的多个网络切片。模式： '^[A-Fa-f0-9]{6}$'
###### Fqdn 
Fqdn的数据结构参见下表： 
属性名称|描述
---|---
Fqdn|表示全量域名（FQDN）。
###### Ipv4Addr 
Ipv4Addr的数据结构参见下表： 
属性名称|描述
---|---
Ipv4Addr|标识以“点分十进制”表示法格式化的IPv4地址的字符串模式：'^（（[0-9] | [1-9] [0-9] | 1 [0-9] [0-9] | 2 [0-4] [0-9] | 25 [0 -5]）\）{3}（[0-9] |。[1-9] [0-9] | 1 [0-9] [0-9] | 2 [0-4] [0-9 ] | 25 [0-5]）$'
###### Ipv6Addr 
Ipv6Addr的数据结构参见下表： 
属性名称|描述
---|---
Ipv6Addr|标识格式化的IPv6地址的字符串。不应使用混合的IPv4 IPv6表示法。模式：'^（（：|（0？|（[1-9a-f] [0-9a-f] {0,3}）））:）（（0？|（[1-9a-f] [0-9a-f] {0,3}））：）{0,6}（：|（0？ |（[1-9a-f] [0-9a-f] {0,3}）） ）$'和模式：'^（（（[^：] +：）{7}（[^：] +））|（（（[^：] +：）* [^：] +）？::（（[^ ：] +：）* [^：] +）？））$'
###### UdrInfo 
UdrInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
GroupId|Optional|标识UDR实例所服务的UDR组。
SupiRange|Optional|表示UDR实例中存在属性数据的SUPI范围列表（注1）。
gpsiRanges|Optional|表示UDR实例中存在属性数据的GPSI范围列表（注1）。
externalGroupIdentifiersRanges|Optional|表示UDR实例中存在属性数据的对外通信实例组范围列表（注1）。
supportedDataSets|Optional|表示UDR实例支持的数据集列表。
注1：如果不携带以上属性，UDR可以服务于任何对外通信实例组和任何SUPI或GPSI。|注1：如果不携带以上属性，UDR可以服务于任何对外通信实例组和任何SUPI或GPSI。|注1：如果不携带以上属性，UDR可以服务于任何对外通信实例组和任何SUPI或GPSI。
###### GroupId 
GroupId的数据结构参见下表： 
属性名称|描述
---|---
GroupId|标识一组设备的字符串网络内部全局唯一ID，用于标识一组IMSI。模式：'^ [A-Fa-f0-9] {8} - [0-9] {3} - [0-9] {2,3} - （[A-Fa-f0-9] [A- Fa-f0-9]）{1,10} $'。
###### SupiRange 
SupiRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
start|Optional|标识SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如，IMSI范围）时使用。该字符串只包含数字。模式： "^[0-9]+$"
end|Optional|标识SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如，IMSI范围）时使用。该字符串只包含数字。模式： "^[0-9]+$"
pattern|Optional|表示SUPI集属于特定范围的表现模式 。如果SUPI字符串与正则表达式完全匹配，则SUPI值被视为范围的一部分。
注：应该携带start和end，或pattern属性。|注：应该携带start和end，或pattern属性。|注：应该携带start和end，或pattern属性。
###### IdentityRange 
IdentityRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
start|Optional|标识IdentityRange范围开始的第一个值，当IdentityRange的范围可以表示为数字范围（例如，MSISDN范围）时使用。该字符串只包含数字。模式： "^[0-9]+$"
end|Optional|表示标识IdentityRange范围结束的最后一个值，当IdentityRange范围可以表示为数字范围（例如，MSISDN范围）时使用。该字符串只包含数字。模式: "^[0-9]+$"
pattern|Optional|表示身份集属于给定范围的表现模式（见ECMA-262 [8]）。如果IdentityRange字符串与正则表达式完全匹配，则IdentityRange被视为范围的一部分。当身份为对外标识符，对外通信组标识符，或MSISDN时使用。
注：应该携带start和end，或pattern属性。|注：应该携带start和end，或pattern属性。|注：应该携带start和end，或pattern属性。
###### DataSetId 
DataSetId的数据结构参见下表： 
属性名称|描述
---|---
DataSetId|枚举类型:SUBSCRIPTION: 订阅数据。POLICY：策略数据。EXPOSURE：开放性结构数据。APPLICATION：应用数据。|枚举类型:SUBSCRIPTION: 订阅数据。POLICY：策略数据。EXPOSURE：开放性结构数据。APPLICATION：应用数据。
###### UdmInfo 
UdmInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
GroupId|Optional|标识UDR实例所服务的UDR组。
SupiRange|Optional|表示UDR实例中存在属性数据的SUPI范围列表（注1）
gpsiRanges|Optional|表示UDR实例中存在属性数据的GPSI范围列表（注1）
externalGroupIdentifiersRanges|Optional|表示UDR实例中存在属性数据的对外通信实例组范围列表（注1）
routingIndicators|Optional|表示路由指示信息列表，允许通过SUCI把路由网络信令路由到UDM实例。模式： '^[0-9]{1,4}$'
注1：如果不携带以上属性，UDR可以服务于任何对外通信实例组和任何SUPI或GPSI。|注1：如果不携带以上属性，UDR可以服务于任何对外通信实例组和任何SUPI或GPSI。|注1：如果不携带以上属性，UDR可以服务于任何对外通信实例组和任何SUPI或GPSI。
###### AusfInfo 
AusfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
GroupId|Optional|标识AUSF组。
SupiRange|Optional|表示AUSF实例可以服务的SUPI范围列表，如果不携带该属性，AUSF可以服务于任何一个SUPI。
routingIndicators|Optional|表示路由指示信息列表，允许通过SUCI把路由网络信令路由到AUSF实例。模式： '^[0-9]{1,4}$'
###### AmfInfo 
AmfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
amfRegionId|Mandatory|标识一个AMF区域。
amfSetId|Mandatory|标识一个AMF集。
Guami|Mandatory|表示支持的GUAMI列表。
Tai|Optional|表示AMF能服务的TAI列表，包含非3GPP接入TAI，如果不携带该属性和taiRangeList属性，表示可以为服务网络中的任何TAI选择该AMF。
TaiRange|Optional|表示AMF可以服务的TAI列表，如果不携带该属性和taiList属性，表示可以为服务网络中的任何TAI选择该AMF。
backupInfoAmfFailure|Optional|当AMF故障时，指定本AMF为备用AMF的GUAMI列表
backupInfoAmfRemoval|Optional|表示在计划移除AMF场景下，指定本AMF为备用AMF的GUAMI列表。
N2InterfaceAmfInfo|Optional|表示AMF的N2接口信息，该信息不需要在NF发现响应中发送，NRF可以通过该属性更新DNS，为5G接入网（AN）发现AMF，更新DNS的过程不在本规范的描述范围之内。
###### Guami 
Guami的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
PlmnId|Mandatory|PLMN ID。
AmfId|Mandatory|AMF ID。
###### Tai 
Tai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
PlmnId|Mandatory|PLMN ID。
Tac|Mandatory|追踪区域码。
###### Tac 
Tac的数据结构参见下表： 
属性名称|描述
---|---
Tac|标识跟踪区域代码的2或3个八位字节串，以十六进制表示。字符串中的每个字符的值应为“0”至“9”或“A”至“F”，并应代表4位。表示TAC的4个最高有效位的最重要字符应首先出现在字符串中，表示TAC的4个最低有效位的字符应出现在字符串的最后。
###### AmfId 
AmfId的数据结构参见下表： 
属性名称|描述
---|---
AmfId|标识由AMF区域ID（8位），AMF集ID（10位）和AMF指针（6位）组成的AMF ID的字符串。它被编码为6个十六进制字符的字符串（即24位）。模式：'^ [A-Fa-f0-9] {6} $'
###### TaiRange 
TaiRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
PlmnId|Mandatory|表示TAC范围（TacRange）相关的PLMN ID。
TacRange|Mandatory|表示TAC范围列表。
###### TacRange 
TacRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
start|Optional|标识TAC开始值，当TAC的范围表示为16进制数（例如，TAC范围）时使用。使用3字节字符串标识跟踪区，字符串中的每一个字符取值范围为“0”到“9”或“A”到“F”，占4位。表示TAC的高4位字符首先出现。表示TAC的低4位的字符最后出现。模式： "^([A-Fa-f0-9]{4}|[A-Fa-f0-9]{6}$)"
end|Optional|标识TAC结束值，当TAC的范围表示为16进制数字（例如，TAC范围）时使用。使用3字节字符串标识跟踪区，字符串中的每一个字符取值范围为“0”到“9”或“A”到“F”，占4位。表示TAC的高4位字符首先出现。表示TAC的低4位的字符最后出现。模式： "^([A-Fa-f0-9]{4}|[A-Fa-f0-9]{6})$"
pattern|Optional|表示TAC集属于给定范围的表现模式。如果TAC字符串与正则表达式完全匹配，则TAC值被视为范围的一部分。
注：应该携带start，end或pattern属性。|注：应该携带start，end或pattern属性。|注：应该携带start，end或pattern属性。
###### N2InterfaceAmfInfo 
N2InterfaceAmfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Ipv4Addr|Conditional|表示N2连接的AMF端点可用IPv4地址（注1 ）
Ipv6Addr|Conditional|表示N2连接的AMF端点可用IPv6地址（注1 ）
AmfName|Optional|表示AMF名称。
注1：数据结构至少包含一个寻址参数，例如，ipv4address或ipv6adress。|注1：数据结构至少包含一个寻址参数，例如，ipv4address或ipv6adress。|注1：数据结构至少包含一个寻址参数，例如，ipv4address或ipv6adress。
###### AmfName 
AmfName的数据结构参见下表： 
属性名称|描述
---|---
AmfName|AMF的全量域名（FQDN）。
###### SmfInfo 
SmfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
sNssaiSmfInfoList|Mandatory|表示SMF每S-NSSAI支持的参数列表。
Tai|Optional|表示SMF能服务的TAI列表，包含非3GPP接入TAI，如果不携带该属性和taiRangeList属性，表示可以为服务网络中的任何TAI选择该SMF。
TaiRange|Optional|表示SMF能服务的TAI列表，包含非3GPP接入TAI，如果不携带该属性和taiList属性，表示可以为服务网络中的任何TAI选择该SMF。
pgwFqdn|Optional|表示SMF采用融合SMF+PGW-C时PGW的全量域名（FQDN）。
AccessType|Conditional|如果携带该IE，应包含SMF支持的接入类型（3GPP_ACCESS和/或NON_3GPP_ACCESS）。如果不携带该IE，3GPP和非3GPP访问类型（3GPP_ACCESS和NON_3GPP_ACCESS）都支持。
###### SnssaiSmfInfoItem 
SnssaiSmfInfoItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Snssai|Mandatory|表示支持的S-NSSAI。
dnnSmfInfoList|Mandatory|表示SMF在单个数据网络中支持的参数列表。
###### DnnSmfInfoItem 
DnnSmfInfoItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Dnn|Mandatory|表示支持的DNN。
###### Dnn 
Dnn的数据结构参见下表： 
属性名称|描述
---|---
Dnn|表示数据网络的字符串。它应格式化为字符串，其中标签用点分隔。
###### AccessType 
AccessType的数据结构参见下表： 
属性名称|描述
---|---
AccessType|枚举类型:3GPP_ACCESS: 3GPP接入。NON_3GPP_ACCESS: 非3GPP接入。|枚举类型:3GPP_ACCESS: 3GPP接入。NON_3GPP_ACCESS: 非3GPP接入。
###### UpfInfo 
UpfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
sNssaiUpfInfoList|Mandatory|表示UPF每S-NSSAI支持的参数列表。
smfServingArea|Optional|表示UPF可以服务的SMF服务区。
InterfaceUpfInfoItem|Optional|表示UPF上配置的用户面接口列表。当NF发现响应中携带该IE时，NF服务消费者（SMF）可以根据此信息选择UPF。
iwkEpsInd|Optional|表示UPF是否支持与EPS网络互操作。true：支持false（默认）：不支持
###### SnssaiUpfInfoItem 
SnssaiUpfInfoItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Snssai|Mandatory|表示支持的S-NSSAI。
dnnUpfInfoList|Mandatory|表示单个数据网络名称（DNN）对应的UPF支持的参数。
###### DnnUpfInfoItem 
DnnUpfInfoItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Dnn|Mandatory|表示支持的数据网络名称列表。
Dnai|Optional|表示单个数据网络名称对应发UPF支持的数据网络接入标识符（DNAI）列表，如果不携带该属性，表示UPF支持该数据网络的所有数据网络接入标识符标识。
###### Dnai 
Dnai的数据结构参见下表： 
属性名称|描述
---|---
Dnai|数据网络访问标识符（DNAI）。
###### InterfaceUpfInfoItem 
InterfaceUpfInfoItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
UPInterfaceType|Mandatory|表示用户面接口类型。
Ipv4Addr|Conditional|表示用户面接口端点可用IPv4地址（注1）
Ipv6Addr|Conditional|表示用户面接口端点可用IPv6地址（注1）
endpointFqdn|Conditional|用户面接口可用端点全量域名FQDN（注1）
networkInstance|Optional|表示用户面接口关联的网络实例。
注1：NF Profile至少包含一个寻址参数，例如，ipv4address， ipv6adress，或endpointFqdn。|注1：NF Profile至少包含一个寻址参数，例如，ipv4address， ipv6adress，或endpointFqdn。|注1：NF Profile至少包含一个寻址参数，例如，ipv4address， ipv6adress，或endpointFqdn。
###### UPInterfaceType 
UPInterfaceType的数据结构参见下表： 
属性名称|描述
---|---
UPInterfaceType|枚举类型:N3N6N9|枚举类型:N3N6N9
###### PcfInfo 
PcfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
GroupId|Optional|表示以PCF组形式提供PCF实例服务，如果不携带该属性，PCF实例不属于任何PCF组。
Dnn|Optional|表示PCF支持的数据网络名称（DNN）列表。
SupiRange|Optional|表示PCF实例可以服务的SUPI范围列表，如果不携带该属性，PCF可以服务于任何SUPI。
gpsiRanges|Optional|表示PCF实例可以服务的GPSI范围列表，如果不携带该属性，PCF可以服务于任何GPSI。
rxDiamHost|Conditional|PCF支持Rx接口时携带该信元。当携带该信元时，该信元指示PCF的Rx接口连接的Diameter主机。
rxDiamRealm|Conditional|PCF支持Rx接口时携带该信元。当携带该信元时，该信元指示PCF的Rx接口连接的Diameter域名。
###### DiameterIdentity 
DiameterIdentity的数据结构参见下表： 
属性名称|描述
---|---
DiameterIdentity|包含Diameter标识的字符串。模式：'^（[A-Za-z0-9] +（ - [A-Za-z0-9] +）.）+ [a-z] {2，} $'
###### BsfInfo 
BsfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Ipv4AddressRange|Optional|表示BSF支持的IPv4地址范围列表。
Dnn|Optional|表示BSF支持的数据网络名称(DNN)列表。
ipDomainList|Optional|表示BSF支持的IPv4地址域列表。
Ipv6PrefixRange|Optional|表示BSF支持的IPv6地址前缀列表。
###### Ipv4AddressRange 
Ipv4AddressRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
start|Mandatory|标识起始IPv4。
end|Mandatory|标识结束IPv4。
###### Ipv6PrefixRange 
Ipv6PrefixRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
start|Mandatory|标识起始IPv6前缀。
end|Mandatory|标识结束IPv6。
###### ChfInfo 
ChfInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
SupiRange|Optional|表示CHF实例可以服务的SUPI范围列表，如果不携带该属性，CHF可以服务于任何SUPI。
gpsiRangeList|Optional|CHF实例可以服务的GPSI范围列表，如果不携带该属性，CHF可以服务于任何GPSI。
PlmnRange|Optional|CHF实例可以服务的PLMN列表（包括CHF实例的PLMN ID），如果不携带该属性，则CHF可以服务任何PLMN。
###### PlmnRange 
PlmnRange的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
start|Optional|标识起始PLMN起始值。字符串的编码如下：<MCC><MNC>模式： '^[0-9]{3}[0-9]{2,3}$'
end|Optional|标识PLMN结束值。字符串的编码如下：<MCC><MNC>Pattern: '^[0-9]{3}[0-9]{2,3}$'
pattern|Optional|表示PLMN集属于给定范围的表现模式。如果PLMN字符串（<MCC><MNC>）与正则表达式完全匹配，则PLMN值被视为范围的一部分。
注：应该携带start，end或pattern属性。|注：应该携带start，end或pattern属性。|注：应该携带start，end或pattern属性。
###### DateTime 
DateTime的数据结构参见下表： 
属性名称|描述
---|---
DateTime|具有OpenAPI规范[3]中定义的格式“日期时间”的字符串
###### NFService 
NFService的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
serviceInstanceID|Mandatory|唯一标识给定NF实例的业务实例。
ServiceName|Mandatory|表示服务实例名称，例如“nudm-sdm ”
versions|Mandatory|表示NF服务支持的API版本，及NF服务支持API版本的失效日期。不同的数组元素中“apiversioninuri”值唯一，因此“apifullversion”第一位版本号数字唯一。
scheme|Mandatory|表示URI方案，例如，HTTP或HTTPS。
NFServiceStatus|Mandatory|表示NF服务实例状态（注3）。
fqdn|Optional|表示NF服务实例全量域名（FQDN）（注1）。
IpEndPoint|Optional|表示对接收到的服务请求进行监控的NF的IP地址（包括IPv4和/或IPv6地址）和端口信息（注1）。
apiPrefix|Optional|表示可选URL路径字段，用于构造不同API URI的{apiRoot}变量。
DefaultNotificationSubscription|Optional|表示不同通知类型的通知端点。
allowedPlmns|Optional|表示允许访问NF实例的PLMN列表（注5）。如果不携带该属性，表示允许任何PLMN访问该服务实例。如果携带该属性，不需要包含在NF Profile的plmnlist中注册的PLMN ID。默认NF Profile中注册的这些PLMN可以访问该服务实例。此属性更改不会触发NRF发送“NF_PROFILE_CHANGED”类型订阅通知。并且，发给订阅NF的属性更改通知消息中不包含该属性。
allowedNfTypes|Optional|表示允许访问该NF实例的NF类型。不携带该属性，表示允许任何类型的NF访问该服务实例。此属性更改不会触发NRF发送“NF_PROFILE_CHANGED”类型订阅通知。并且，发给订阅NF的属性更改通知消息中不包含该属性。
allowedNfDomains|Optional|表示模式（根据ECMA-262第[8]条正则表达式），代表允许访问服务实例的NF域名（注5）。不携带该属性，表示允许任何类型的NF域名访问该服务实例。此属性更改不会触发NRF发送“NF_PROFILE_CHANGED”类型订阅通知。并且，发给订阅NF的属性更改通知消息中不包含该属性。
allowedNssais|Optional|表示允许访问该NF实例切片的S-NSSAI。（注5）如果不携带该属性，表示允许任何S-NSSAI的切片访问该服务实例。此属性更改不会触发NRF发送“NF_PROFILE_CHANGED”类型订阅通知。并且，发给订阅NF的属性更改通知消息中不包含该属性。
priority|Optional|表示NF选择时相对于同种服务类型的其他NF的优先级，取值范围0~65535；值越小，优先级越高。（注2）NRF在向Nnrf_NFDiscovery服务开放NF Profile时，可能会覆盖之前接收到的优先级值。
capacity|Optional|表示静态容量信息，即，相对于同种业务类型的其他NF实例权重。取值范围0~65535。（注2）
load|Optional|表示动态负载信息，及NF当前的负载百分比。取值范围为0~100。
recoveryTime|Optional|表示NF启动/重启时间戳（注3+注4）。
ChfServiceInfo|Optional|表示CHF服务实例数据。
SupportedFeatures|Optional|表示NF服务实例支持的特性。
注1：如果不携带fqdn和ipendpoint属性，则使用NF Profile中的全量域名（FQDN）和IP地址相关属性构造该业务的API URI。注2：如果携带容量和优先级参数，则容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器一样。注3：如果恢复时间（recoveryTime）或NF服务状态（nfServiceStatus）发生变化，NRF将发送订阅通知消息给订阅了NF Profile变化的NFs。注4: 当NF服务消费者认为NF恢复之前在NF中创建的所有资源都丢失了。此时，恢复（recoveryTime）可以用于检测NF重启并触发相应动作，例如，释放本地资源。注5：如果NFService和NF Profile都携带此参数，则以NFService携带的值为准。如果NFService和NF Profile都不携带此参数，表示访问服务实例对此参数没有相应的限制。注6：如果其他NF所属PLMN ID不包含在NRF配置的PLMN ID列表中，则NF所属PLMN不同。|注1：如果不携带fqdn和ipendpoint属性，则使用NF Profile中的全量域名（FQDN）和IP地址相关属性构造该业务的API URI。注2：如果携带容量和优先级参数，则容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器一样。注3：如果恢复时间（recoveryTime）或NF服务状态（nfServiceStatus）发生变化，NRF将发送订阅通知消息给订阅了NF Profile变化的NFs。注4: 当NF服务消费者认为NF恢复之前在NF中创建的所有资源都丢失了。此时，恢复（recoveryTime）可以用于检测NF重启并触发相应动作，例如，释放本地资源。注5：如果NFService和NF Profile都携带此参数，则以NFService携带的值为准。如果NFService和NF Profile都不携带此参数，表示访问服务实例对此参数没有相应的限制。注6：如果其他NF所属PLMN ID不包含在NRF配置的PLMN ID列表中，则NF所属PLMN不同。|注1：如果不携带fqdn和ipendpoint属性，则使用NF Profile中的全量域名（FQDN）和IP地址相关属性构造该业务的API URI。注2：如果携带容量和优先级参数，则容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器一样。注3：如果恢复时间（recoveryTime）或NF服务状态（nfServiceStatus）发生变化，NRF将发送订阅通知消息给订阅了NF Profile变化的NFs。注4: 当NF服务消费者认为NF恢复之前在NF中创建的所有资源都丢失了。此时，恢复（recoveryTime）可以用于检测NF重启并触发相应动作，例如，释放本地资源。注5：如果NFService和NF Profile都携带此参数，则以NFService携带的值为准。如果NFService和NF Profile都不携带此参数，表示访问服务实例对此参数没有相应的限制。注6：如果其他NF所属PLMN ID不包含在NRF配置的PLMN ID列表中，则NF所属PLMN不同。
###### ServiceName 
ServiceName的数据结构参见下表： 
属性名称|描述
---|---
ServiceName|枚举类型:nnrf-nfm： NRF提供的NF管理服务（Nnrf_NFManagement Service）。nnrf-disc：NRF提供的NF发现服务（Nnrf_NFDiscovery Service）。nudm-sdm：UDM提供的订阅数据管理服务（Nudm_SubscriberDataManagement Service）。nudm-uecm：UDM提供的用户上下文管理服务（Nudm_UEContextManagement Service）。nudm-ueau：UDM提供的用户鉴权服务（Nudm_UEAuthentication Service）。nudm-ee：UDM提供的事件开放服务（Nudm_EventExposure Service）。nudm-pp：UDM提供的参数提供服务（Nudm_ParameterProvision Service）。namf-comm：AMF提供的通信服务（Namf_Communication Service）。namf-evts：AMF提供的事件开放服务（Namf_EventExposure Service）。namf-mt：AMF提供的移动终止服务（Namf_MT Service）。namf-loc：AMF提供的位置服务（Namf_Location ）。nsmf-pdusession：SMF提供的PDU会话服务（Nsmf_PDUSession Service）。nsmf-event-exposure：SMF提供的事件开放服务（Nsmf_EventExposure）。nausf-auth：AUSF提供的用户鉴权服务（Nausf_UEAuthentication Service）。nausf-sorprotection：AUSF提供的SoRP保护服务（Nausf_SoRProtection Service）。nnef-pfdmanagement：NEF提供的PFD管理（Nnef_PFDManagement）服务。npcf-am-policy-control: PCF提供AM策略控制服务（Npcf_AMPolicyControl Service）。npcf-smpolicycontrol：PCF提供的SM策略控制服务（Npcf_SMPolicyControl Service）。npcf-policyauthorization: PCF提供的策略授权服务（Npcf_PolicyAuthorization Service）。npcf-bdtpolicycontrol：PCF提供的BDT策略控制服务（Npcf_BDTPolicyControl Service）。npcf-eventexposure：PCF提供的事件开放服务（Npcf_EventExposure Service）。npcf-ue-policy-control: PCF提供的用户策略控制服务（Npcf_UEPolicyControl Service）。nsmsf-sms：SMSF提供的短消息服务（Nsmsf_SMService）。nnssf-nsselection：NSSF提供的网络切片（NS）选择服务（Nnssf_NSSelection Service）。nnssf-nssaiavailability：NSSF提供的网络切片选择支撑信息可用性服务（Nnssf_NSSAIAvailability Service）。nudr-dr：UDR提供的数据仓库服务（Nudr_DataRepository Service）。nlmf-loc：LMF提供的位置服务（Nlmf_Location Service）。n5g-eir-eic: 5G EIR提供的设备身份校验服务（N5g-eir_EquipmentIdentityCheck Service）。nbsf-management：BSF提供的管理服务（Nbsf_Management Service）。nchf-spendinglimitcontrol：CHF提供的消费限制服务（Nchf_SpendingLimitControl Service）。nchf-convergedcharging: CHF提供的融合计费服务（Nchf_Converged_Charging Service）。nnwdaf-eventssubscription：NWDAF提供的事件订阅服务（Nnwdaf_EventsSubscription Service）。nnwdaf-analyticsinfo: NWDAF提供的信息分析服务（Nnwdaf_AnalyticsInfo Service）。|枚举类型:nnrf-nfm： NRF提供的NF管理服务（Nnrf_NFManagement Service）。nnrf-disc：NRF提供的NF发现服务（Nnrf_NFDiscovery Service）。nudm-sdm：UDM提供的订阅数据管理服务（Nudm_SubscriberDataManagement Service）。nudm-uecm：UDM提供的用户上下文管理服务（Nudm_UEContextManagement Service）。nudm-ueau：UDM提供的用户鉴权服务（Nudm_UEAuthentication Service）。nudm-ee：UDM提供的事件开放服务（Nudm_EventExposure Service）。nudm-pp：UDM提供的参数提供服务（Nudm_ParameterProvision Service）。namf-comm：AMF提供的通信服务（Namf_Communication Service）。namf-evts：AMF提供的事件开放服务（Namf_EventExposure Service）。namf-mt：AMF提供的移动终止服务（Namf_MT Service）。namf-loc：AMF提供的位置服务（Namf_Location ）。nsmf-pdusession：SMF提供的PDU会话服务（Nsmf_PDUSession Service）。nsmf-event-exposure：SMF提供的事件开放服务（Nsmf_EventExposure）。nausf-auth：AUSF提供的用户鉴权服务（Nausf_UEAuthentication Service）。nausf-sorprotection：AUSF提供的SoRP保护服务（Nausf_SoRProtection Service）。nnef-pfdmanagement：NEF提供的PFD管理（Nnef_PFDManagement）服务。npcf-am-policy-control: PCF提供AM策略控制服务（Npcf_AMPolicyControl Service）。npcf-smpolicycontrol：PCF提供的SM策略控制服务（Npcf_SMPolicyControl Service）。npcf-policyauthorization: PCF提供的策略授权服务（Npcf_PolicyAuthorization Service）。npcf-bdtpolicycontrol：PCF提供的BDT策略控制服务（Npcf_BDTPolicyControl Service）。npcf-eventexposure：PCF提供的事件开放服务（Npcf_EventExposure Service）。npcf-ue-policy-control: PCF提供的用户策略控制服务（Npcf_UEPolicyControl Service）。nsmsf-sms：SMSF提供的短消息服务（Nsmsf_SMService）。nnssf-nsselection：NSSF提供的网络切片（NS）选择服务（Nnssf_NSSelection Service）。nnssf-nssaiavailability：NSSF提供的网络切片选择支撑信息可用性服务（Nnssf_NSSAIAvailability Service）。nudr-dr：UDR提供的数据仓库服务（Nudr_DataRepository Service）。nlmf-loc：LMF提供的位置服务（Nlmf_Location Service）。n5g-eir-eic: 5G EIR提供的设备身份校验服务（N5g-eir_EquipmentIdentityCheck Service）。nbsf-management：BSF提供的管理服务（Nbsf_Management Service）。nchf-spendinglimitcontrol：CHF提供的消费限制服务（Nchf_SpendingLimitControl Service）。nchf-convergedcharging: CHF提供的融合计费服务（Nchf_Converged_Charging Service）。nnwdaf-eventssubscription：NWDAF提供的事件订阅服务（Nnwdaf_EventsSubscription Service）。nnwdaf-analyticsinfo: NWDAF提供的信息分析服务（Nnwdaf_AnalyticsInfo Service）。
###### NFServiceVersion 
NFServiceVersion的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
apiVersionInUri|Mandatory|表示用于访问API的URI中需要使用的服务实例版本（如V1）。
apiFullVersion|Mandatory|表示API完整版本号。
expiry|Optional|NF服务的失效日期和时间，表示配置的失效日期。
###### UriScheme 
UriScheme的数据结构参见下表： 
属性名称|描述
---|---
UriScheme|枚举类型:http：HTTP URI方案。https：HTTPS URI方案。|枚举类型:http：HTTP URI方案。https：HTTPS URI方案。
###### NFServiceStatus 
NFServiceStatus的数据结构参见下表： 
属性名称|描述
---|---
NFServiceStatus|枚举类型:REGISTERED: NF实例已在NRF注册而且能被其他NF发现。SUSPENDED: NF实例已注册到NRF，但未运行，其他NF无法发现。|枚举类型:REGISTERED: NF实例已在NRF注册而且能被其他NF发现。SUSPENDED: NF实例已注册到NRF，但未运行，其他NF无法发现。
###### IpEndPoint 
IpEndPoint的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Ipv4Addr|Conditional|表示IPv4地址（注1）
Ipv6Addr|Conditional|表示IPv6地址（注1）
transport|Optional|表示传输协议。
port|Optional|表示端口号（注2）
注1：数据结构最多只能包含一个ipv4Address或ipv6Address。注2：如果ipendpoint属性未携带端口号，则NF服务消费者在调用服务时，使用默认的HTTP端口号，如TCP端口80访问HTTP URI，或使用TCP端口443访问HTTPS URI。|注1：数据结构最多只能包含一个ipv4Address或ipv6Address。注2：如果ipendpoint属性未携带端口号，则NF服务消费者在调用服务时，使用默认的HTTP端口号，如TCP端口80访问HTTP URI，或使用TCP端口443访问HTTPS URI。|注1：数据结构最多只能包含一个ipv4Address或ipv6Address。注2：如果ipendpoint属性未携带端口号，则NF服务消费者在调用服务时，使用默认的HTTP端口号，如TCP端口80访问HTTP URI，或使用TCP端口443访问HTTPS URI。
###### TransportProtocol 
TransportProtocol的数据结构参见下表： 
属性名称|描述
---|---
TransportProtocol|枚举类型:TCP:表示TCP传输协议。|枚举类型:TCP:表示TCP传输协议。
###### DefaultNotificationSubscription 
DefaultNotificationSubscription的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
NotificationType|Mandatory|提供对应的回调URI的通知类型。
callbackUri|Mandatory|表示回调URI。IpEndPoint
N1MessageClass|Conditional|如果通知类型为N1_MESSAGES，则携带该IE，并标识要通知的N1消息类别。
N2InformationClass|Conditional|如果通知类型为N2_INFORMATION，则携带该IE，并标识要通知的N2消息类别。
###### NotificationType 
NotificationType的数据结构参见下表： 
属性名称|描述
---|---
NotificationType|枚举类型:N1_MESSAGES：N1消息通知。N2_INFORMATION：N2消息订阅通知。LOCATION_NOTIFICATION：AMF转发给NF服务消费者的位置信息订阅通知（如：网关移动定位中心GMLC）。DATA_REMOVAL_NOTIFICATION：UDR删除数据时的订阅通知，例如，NF订阅UE数据后，UDR删除UE注册数据时会通知NF。DATA_CHANGE_NOTIFICATION：UDR数据变更通知。|枚举类型:N1_MESSAGES：N1消息通知。N2_INFORMATION：N2消息订阅通知。LOCATION_NOTIFICATION：AMF转发给NF服务消费者的位置信息订阅通知（如：网关移动定位中心GMLC）。DATA_REMOVAL_NOTIFICATION：UDR删除数据时的订阅通知，例如，NF订阅UE数据后，UDR删除UE注册数据时会通知NF。DATA_CHANGE_NOTIFICATION：UDR数据变更通知。
###### Uri 
Uri的数据结构参见下表： 
属性名称|描述
---|---
Uri|提供URI格式的字符串。
###### N1MessageClass 
N1MessageClass的数据结构参见下表： 
属性名称|描述
---|---
N1MessageClass|枚举类型:5GMM：接收到的整个NAS消息（例如用于在使用AMF重定向的注册过程期间将注册消息转发到目标AMF）。SM：SM类型的N1消息。LPP：LPP类型的N1消息。SMS：SMS类型的N1消息。UPDP：用于UE策略传递的N1消息。|枚举类型:5GMM：接收到的整个NAS消息（例如用于在使用AMF重定向的注册过程期间将注册消息转发到目标AMF）。SM：SM类型的N1消息。LPP：LPP类型的N1消息。SMS：SMS类型的N1消息。UPDP：用于UE策略传递的N1消息。
###### N2InformationClass 
N2InformationClass的数据结构参见下表： 
属性名称|描述
---|---
N2InformationClass|枚举类型:SM：N2 SM信息。NRPPa：N2 NRPPa information。PWS：PWS类型的N2 PWS信息。PWS-BCAL：N2广播完成区域列表或广播取消区域列表。PWS-RA：N2重启指示或故障指示。RAN：N2 RAN相关信息。|枚举类型:SM：N2 SM信息。NRPPa：N2 NRPPa information。PWS：PWS类型的N2 PWS信息。PWS-BCAL：N2广播完成区域列表或广播取消区域列表。PWS-RA：N2重启指示或故障指示。RAN：N2 RAN相关信息。
###### ChfServiceInfo 
ChfServiceInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
primaryChfServiceInstance|Conditional|给定CHF服务实例作为主CHF服务实例的从CHF实例时携带该IE，它应该设置为主CHF服务实例的服务实例ID（ServiceInstanceID）。携带secondaryChfServiceInstance时，不存在该IE。
secondaryChfServiceInstance|Conditional|给定CHF服务实例作为从CHF服务实例的主CHF实例时携带该IE，它应该设置为从CHF服务实例的服务实例ID（ServiceInstanceID）。携带primaryChfServiceInstance时，该IE不存在。
###### SupportedFeatures 
SupportedFeatures的数据结构参见下表： 
属性名称|描述
---|---
SupportedFeatures|用于指示API支持的功能的字符串。
###### SubscriptionData 
SubscriptionData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
nfStatusNotificationUri|Mandatory|表示回调URI，NF服务消费者通过该URL接收NRF订阅通知。
SubscrCond|Optional|携带该属性时，该属性包含请求监控的NF实例集的标识条件。不携带该属性时，NF服务消费者请求订阅NRF中注册的所有NF。
subscriptionId|Conditional|表示新创建资源的订阅ID。向NRF发送的订阅请求不携带该属性，NRF返回的创建订阅响应携带该属性。只读： true
validityTime|Conditional|表示订阅失效时间，该属性可能由客户端发送，作为对服务器的提示。服务器返回的订阅创建响应中必须携带该参数（不管订阅请求中是否携带该参数）。
reqNotifEvents|Optional|如果携带该属性，该属性包含NF服务消费者感兴趣的事件类型列表。如果不携带该属性，则表示请求所有事件类型的订阅通知。
reqNfType|Optional|如果携带该属性，该IE包含创建订阅请求的NF服务消费者的NF类型。NRF应携带该参数对订阅请求进行授权，与NF服务发现中使用的“requester-nf-type”（请求者的NF类型）相同。
reqNfFqdn|Optional|如果携带该属性，该IE包含创建订阅请求的NF服务消费者的全量域名（FQDN）。NRF应携带该参数对订阅请求进行授权，与NF服务发现中使用的“requester-nf-instance-fqdn”（请求者的NF实例全量域名）相同。
PlmnId|Optional|如果携带该参数，该属性包含请求监控状态的NF实例的目标PLMN ID。
NotifCondition|Optional|如果携带该属性，该属性包含触发NRF发送订阅通知的条件；只有NF服务消费者订阅了NF Profile更改通知（reqNotifEvents包含“NF_PROFILE_CHANGED”或未携带reqNotifEvents）才携带该属性。如果不携带该属性，NF服务消费者不指示任何可以触发NRF发送订阅通知的属性限制或条件。
注：“subscription to all NFs ”需要很多NRF资源，订阅通知产生的网络流量也很高。因此，应该由NRF在非常严格的策略下授权，比如，仅针对requftype和requfqdn属性标识的特定的请求者NF才进行授权。|注：“subscription to all NFs ”需要很多NRF资源，订阅通知产生的网络流量也很高。因此，应该由NRF在非常严格的策略下授权，比如，仅针对requftype和requfqdn属性标识的特定的请求者NF才进行授权。|注：“subscription to all NFs ”需要很多NRF资源，订阅通知产生的网络流量也很高。因此，应该由NRF在非常严格的策略下授权，比如，仅针对requftype和requfqdn属性标识的特定的请求者NF才进行授权。
###### SubscrCond 
SubscrCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
NfInstanceIdCond|Optional|表示订阅给定NF实例。
NfTypeCond|Optional|表示订阅一组特定类型的NF实例。
ServiceNameCond|Optional|表示订阅某个服务名称的一组NF实例。
AmfCond|Optional|表示订阅属于某个AMF集和/或AMF区域下的一组NF实例 (AMF)。
GuamiListCond|Optional|表示订阅一组GUAMI标识的NF实例。
NetworkSliceCond|Optional|表示订阅由S-NSSAI和NSI标识的一组NF实例。
NfGroupCond|Optional|表示订阅由NF（UDM，AUSF或UDR）组标识的一组NF实例。
###### NfInstanceIdCond 
NfInstanceIdCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
NfInstanceId|Mandatory|表示状态需要监控的NF实例的NF实例ID。
###### NfTypeCond 
NfTypeCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
NFType|Mandatory|表示状态需要监控的NF实例的NF实例类型。
###### ServiceNameCond 
ServiceNameCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
ServiceName|Mandatory|表示状态需要监控的NF实例的NF实例业务名称。
###### AmfCond 
AmfCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
amfSetId|Conditional|表示状态需要监控的NF实例（AMF）的NF实例集ID。
amfRegionId|Conditional|表示状态需要监控的NF实例（AMF）的所在区域ID。
注：数据结构至少携带amfSetId或amfRegionId ；如果订阅数据（SubscriptionData）中同时存在amfRegionId和amfsetid属性，则表示满足这两个属性的通知订阅（给特定AMF区域中的AMF集发送订阅通知）。|注：数据结构至少携带amfSetId或amfRegionId ；如果订阅数据（SubscriptionData）中同时存在amfRegionId和amfsetid属性，则表示满足这两个属性的通知订阅（给特定AMF区域中的AMF集发送订阅通知）。|注：数据结构至少携带amfSetId或amfRegionId ；如果订阅数据（SubscriptionData）中同时存在amfRegionId和amfsetid属性，则表示满足这两个属性的通知订阅（给特定AMF区域中的AMF集发送订阅通知）。
###### GuamiListCond 
GuamiListCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Guami|Mandatory|标识状态需要监控的NF实例的GUAMI。
###### NetworkSliceCond 
NetworkSliceCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Snssai|Mandatory|表示状态需要监控的NF实例（AMF）的S -NSSAI。
nsiList|Optional|表示状态需要监控的NF实例（AMF）的网络分片实例(NSI) ID。
###### NfGroupCond 
NfGroupCond的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
nfType|Mandatory|表示状态需要监控的NF实例类型（UDM、AUSF或UDR）。
NfGroupId|Mandatory|表示状态需要监控的NF实例（AMF）的NF组ID。
###### NfGroupId 
NfGroupId的数据结构参见下表： 
属性名称|描述
---|---
NfGroupId|一组NF的标识符。
###### NotificationEventType 
NotificationEventType的数据结构参见下表： 
属性名称|描述
---|---
NotificationEventType|枚举类型:NF_REGISTERED：NF实例注册到NRF上。NF_DEREGISTERED：NF实例从NRF去注册。NF_PROFILE_CHANGED：NF实例属性信息发生变化。|枚举类型:NF_REGISTERED：NF实例注册到NRF上。NF_DEREGISTERED：NF实例从NRF去注册。NF_PROFILE_CHANGED：NF实例属性信息发生变化。
###### NotifCondition 
NotifCondition的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
monitoredAttributes|Conditional|表示NF Profile中属性的JSON指针列表。如果携带该属性，NRF只会在列表中包含的属性发生更改时发送订阅通知（见注1）。
unmonitoredAttributes|Conditional|表示NF Profile中属性的JSON指针列表。如果携带该属性，NRF只会在列表之外的属性发生更改时发送订阅通知（见注1）。
注1：不能同时携带监控属性（monitoredAttributes）和不监控属性（unmonitoredAttributes）。|注1：不能同时携带监控属性（monitoredAttributes）和不监控属性（unmonitoredAttributes）。|注1：不能同时携带监控属性（monitoredAttributes）和不监控属性（unmonitoredAttributes）。
###### NotificationData 
NotificationData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
event|Mandatory|表示通知类型，取值为“NF_REGISTERED”、“NF_DEREGISTERED”或“NF_PROFILE_CHANGED”。
nfInstanceUri|Mandatory|表示给定通知事件关联的NF实例URI。
NFProfile|Conditional|表示新增NF Profile或更新后的NF Profile；当通知类型为“NF_REGISTERED”或“NF_PROFILE_CHANGED”时，携带该属性字段。
profileChanges|Conditional|通知事件关联的NF实例属性变更列表；当通知类型为“NF_PROFILE_CHANGED”时，可能携带该参数（见注1）
注意1：如果“事件”属性取值为“NF_PROFILE_CHANGED”，需携带“nfProfile”或“profilechanges”属性。|注意1：如果“事件”属性取值为“NF_PROFILE_CHANGED”，需携带“nfProfile”或“profilechanges”属性。|注意1：如果“事件”属性取值为“NF_PROFILE_CHANGED”，需携带“nfProfile”或“profilechanges”属性。
###### ChangeItem 
ChangeItem的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
op|Mandatory|此IE指示资源发生的更改类型。
path|Mandatory|此IE包含一个JSON指针值，该值引用已应用更改的属性的位置。
from|Conditional|此IE指示源JSON元素的路径（根据JSON指针语法）被移动或复制到“path”属性指示的位置。如果“op”属性的值为“MOVE”，则它应存在。
origValue|Optional|此IE指示path属性中指定的属性的原始值。此属性仅在“op”属性值为“REMOVE”，“REPLACE”或“MOVE”时适用。基于用例，可以包括该属性。
newValue|Conditional|此IE指示路径属性中指定的属性的新值。如果“op”属性的值为“ADD”，“REPLACE”，则它应存在。此属性的数据类型应与发生更改的资源类型相同。应允许空值。
###### ChangeType 
ChangeType的数据结构参见下表： 
属性名称|描述
---|---
ChangeType|枚举类型:ADD: 此值表示已将新属性添加到资源。MOVE：此值表示现有属性已移至资源中的其他路径。REMOVE：此值表示已从资源中删除现有属性。REPLACE：此值表示已使用新值更新现有属性。|枚举类型:ADD: 此值表示已将新属性添加到资源。MOVE：此值表示现有属性已移至资源中的其他路径。REMOVE：此值表示已从资源中删除现有属性。REPLACE：此值表示已使用新值更新现有属性。
###### UriList 
UriList的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
_links|Optional|该成员应包含一个名称为“item”的数组成员，其值为“link”对象数组。每个link对象包含一个资源请求URI。每个请求资源应该对应一个link对象。该属性还包含一个名称为“self”的数组成员，其值是一个携带返回标识的URI的“link”对象。如服务消费者接收到携带以上参数的响应，给每个资源URI上发送一个GET请求，从NF服务提供者那里检索所请求的资源。
###### Query Parameters 
NF检索查询请求消息中的携带的数据参见下表： 
属性名称|Presence requirement|描述
---|---|---
NFType|Optional|返回的NF实例列表的NF类型。
limit|Optional|此查询中返回的最大数量。
##### Nnrf_NFDiscovery specific Data Types 
###### Query Parameters 
NF发现请求消息中的查询参数携带的数据参见下表： 
属性名称|Presence requirement|描述
---|---|---
target-nf-type|Mandatory|目标NF类型。
requester-nf-type|Mandatory|请求方NF类型。
ServiceName|Optional|请求的服务名称。如果携带，则NRF在发现结果列表中返回符合条件的NF包含的对应服务。如果不携带，则NRF在发现结果列表中返回符合条件的NF的所有服务。
requester-nf-instance-fqdn|Optional|请求方NF实例的FQDN。
target-plmn-list|Conditional|目标NF所在的PLMN。当需要发现不同PLMN中的NF服务或同一PLMN中包含多个PLMN ID的特定PLMN ID的NF服务时，此属性必选。
requester-plmn-list|Conditional|请求方NF所在的PLMN。当需要发现不同于请求方NF所在PLMN的其他PLMN时，此属性必选。
target-nf-instance-id|Optional|目标NF实例ID。
target-nf-fqdn|Optional|目标NF实例的FQDN。
Snssai|Optional|目标NF实例所服务的S-NSSAI列表。
nsi-list|Optional|目标NF服务所服务的NSI列表。
Dnn|Optional|目标NF服务所服务的DNN。如果目标NF类型是BSF、SMF或UPF，则可以包含DNN。如果发现属性中还包括Snssai，则在由Snssai标识的网络切片中应有为此DNN服务的NF服务。
smf-serving-area|Optional|SMF的服务区域。如果目标NF类型为UPF，此属性可以包含在内。
Tai|Optional|跟踪区域标识。
amf-region-id|Optional|AMF区域标识。
amf-set-id|Optional|AMF集标识。
Guami|Optional|全球唯一AMF ID，用于发现合适的AMF。
supi|Optional|该属性表示Subscription Permanent Identifier，用户永久标识。支持supi号段的NF包含UDM、AUSF、PCF、CHF、UDR，此号段可以用于支撑这些NF的选择。
ue-ipv4-address|Optional|UE的IPv4地址，发现目标为BSF时使用。
ip-domain|Optional|UE的IPv4地址域，发现目标为BSF时使用。
ue-ipv6-prefix|Optional|UE的IPv6前缀，发现目标为BSF时使用。
pgw-ind|Optional|该属性表示是否需要发现组合的SMF/PGW-C或独立的SMF。true：请求发现组合的SMF/PGW-C。false：请求发现独立的SMF。
pgw|Optional|PGW的FQDN，AMF从MME接收该PGW FQDN以查找组合的SMF/PGW-C。
gpsi|Optional|该属性表示Generic Public Subscription Identifier，一般公共订阅标识符。支持gpsi号段的NF包含UDM、CHF、UDR，此号段可以用于支撑这些NF的选择。
external-group-identity|Optional|该属性表示请求者UE的外部组标识符，用于发现合适的NF。如果目标NF类型为UDM或UDR，此属性可以包含在内。
data-set|Optional|该属性表示目标NF支持的数据集。如果目标NF类型为UDR，此属性可以包含在内。
routing-indicator|Optional|该属性表示选路指示器。支持routing-indicator号段的NF包含UDM、AUSF，此号段可以用于支撑这些NF的选择。
group-id-list|Optional|该属性表示某一NF类型的NF组标识。支持groupId号段的NF包含UDM、AUSF、PCF，此属性可以用于支撑这些NF的选择。
dnai-list|Optional|该属性表示数据网络访问标识符。如果目标NF类型为UPF，此属性可以包含在内。
upf-iwk-eps-ind|Optional|该属性表示是否需要发现支持与EPS互通的UPF。true：请求发现支持与EPS互通的UPF。false：请求发现不支持与EPS互通的UPF。
chf-supported-plmn|Optional|该属性表示CHF支持的PLMN。如果目标NF类型为CHF，此属性可以包含在内。
preferred-locality|Optional|该属性表示优选目标NF的位置（例如地理位置，数据中心）。根据此属性，NRF将首选具有与此位置匹配的目标NF。如果没有找到，NRF在发现响应中返回其他NF。
access-type|Conditional|目标NF支持的访问类型。
preferred-tai|Optional|该属性如果存在，NRF优先返回为此TAI服务的服务提供方NF，如果没有与此TAI匹配的服务提供方NF，则返回不匹配的服务提供方NF。
serving-scope|Optional|NF实例的服务区域。NRF支持识别服务请求消息和服务注册消息中携带的服务区servingScope信息，支持基于服务区信息精确匹配。缺少此属性并不意味着NF实例可以服务于每个区域。
###### SearchResult 
SearchResult的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
validityPeriod|Mandatory|该属性包含服务发现结果的有效时间，有效时间内，服务发现结果可以被NF服务消费者缓存，该值应与HTTP响应中发送的“Cache-Control”头域中的“max-age”参数值保持一致。|该属性包含服务发现结果的有效时间，有效时间内，服务发现结果可以被NF服务消费者缓存，该值应与HTTP响应中发送的“Cache-Control”头域中的“max-age”参数值保持一致。
nfInstances|Mandatory|该属性包含NF实例属性数组，用于匹配服务发现请求查询参数标识的搜索条件。数组为空表示没有匹配到搜索条件的NF实例。|该属性包含NF实例属性数组，用于匹配服务发现请求查询参数标识的搜索条件。数组为空表示没有匹配到搜索条件的NF实例。
PreferredSearch|Conditional|该属性表示NF发现结果中的NF Profile是否与发现请求参数中包含的优选参数相匹配。|该属性表示NF发现结果中的NF Profile是否与发现请求参数中包含的优选参数相匹配。
###### nfInstances 
nfInstances的数据结构为NFProfile，参见下表： 
属性名称|Presence requirement|描述
---|---|---
NfInstanceId|Mandatory|表示NF实例的唯一标识。
NFType|Mandatory|表示NF类型。
NFStatus|Mandatory|表示NF实例状态。
plmnList|Conditional|表示NF所属PLMN列表（注5）。NF所属PLMN信息存在时，携带该IE。
Snssai|Optional|NF的单网络切片选择。
nsiList|Optional|NF的网络分片实例列表。
Fqdn|Conditional|NF的全量域名（注1+注3）。
Ipv4Addr|Conditional|表示NF的IPv4地址（注1）。
Ipv6Addr|Conditional|表示NF的IPv6地址（注1）。
capacity|Optional|表示静态容量信息，即，相对于同种业务类型的其他NF权重，取值范围0到65535。如果nfServiceList参数也包含容量值，优先选择nfServiceList中的容量值。（注2）。
load|Optional|表示最新已知的NF负载，取值0~100%（见注4）
locality|Optional|运营商定义的NF实例位置信息。例如地理位置，数据中心等。
priority|Optional|表示NF选择时相对于同种服务类型的其他NF的优先级，取值范围0~65535；值越小，优先级越高，如果NF的nfServiceList参数包含该字段，优先选择nfServiceList中的优先级值。（见注2）。
UdrInfo|Optional|表示UDR数据（SUPI范围等）
UdmInfo|Optional|表示UDM数据。
AusfInfo|Optional|表示AUSF数据。
AmfInfo|Optional|表示AMF数据（AMF集ID）。
SmfInfo|Optional|表示SMF数据（DNN）。
UpfInfo|Optional|表示UPF数据，包括S-NSSAI、DNN、SMF服务区域等。
PcfInfo|Optional|表示PCF数据。
BsfInfo|Optional|表示BSF数据。
ChfInfo|Optional|表示CHF数据。
customInfo|Optional|表示自定义NF数据。
recoveryTime|Optional|表示NF重启/启动时的时间戳。
nfServicePersistence|Optional|如果携带该参数，且值为true，表示该NF实例中同一个NFS的不同服务实例支持相同的API版本，能够在共享存储持久化资源状态，因此，在NF服务消费者选择支持相同API版本的新NF服务实例后，这些资源可供使用。否则，表示同一NF业务的NF业务实例不能共享NF实例内部资源状态。
NFService|Optional|表示NF业务实例列表。
注1：NF Profile至少包含一个寻址参数，例如，fqdn，ipv4address或ipv6adress。注2：如果携带容量和优先级参数，携带容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似。注3：如果requester-plmn不在NRF上配置的PLMN ID标识的PLMN范围内，则说明requester-plmn与发现的NF的PLMN不同。如果查询参数中的requester-plmn与发现的NF的PLMN不同，Fqdn属性值应包含NF注册请求中的跨PLMN全量域名属性（interPlmnFqdn）。注4：所述NF服务消费者的负载参数的使用根据实际情况而定，例如，负载参数和其他参数一起用于NF选择和负载平衡服务。注5: 给定NF可以在NF Profile中注册包含在特定PLMN的多个PLMN ID。如果注册了多个PLMN ID，则该NF Profile的所有属性都应用在PlmnList中注册的每个PLMN ID。例外情况下，NF Profile（包括PLMN ID），例如基于IMSI的SUPI，TAI和GUAMI等属性，只应用在单个PLMN ID，此时，NF可能会在Profile中针对每个PLMN ID都注册这些属性，例如，UDM可能会针对不同PLMN ID在NF Profile多次注册相同属性，例如，SUPI范围（SUPI ranges）。|注1：NF Profile至少包含一个寻址参数，例如，fqdn，ipv4address或ipv6adress。注2：如果携带容量和优先级参数，携带容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似。注3：如果requester-plmn不在NRF上配置的PLMN ID标识的PLMN范围内，则说明requester-plmn与发现的NF的PLMN不同。如果查询参数中的requester-plmn与发现的NF的PLMN不同，Fqdn属性值应包含NF注册请求中的跨PLMN全量域名属性（interPlmnFqdn）。注4：所述NF服务消费者的负载参数的使用根据实际情况而定，例如，负载参数和其他参数一起用于NF选择和负载平衡服务。注5: 给定NF可以在NF Profile中注册包含在特定PLMN的多个PLMN ID。如果注册了多个PLMN ID，则该NF Profile的所有属性都应用在PlmnList中注册的每个PLMN ID。例外情况下，NF Profile（包括PLMN ID），例如基于IMSI的SUPI，TAI和GUAMI等属性，只应用在单个PLMN ID，此时，NF可能会在Profile中针对每个PLMN ID都注册这些属性，例如，UDM可能会针对不同PLMN ID在NF Profile多次注册相同属性，例如，SUPI范围（SUPI ranges）。|注1：NF Profile至少包含一个寻址参数，例如，fqdn，ipv4address或ipv6adress。注2：如果携带容量和优先级参数，携带容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似。注3：如果requester-plmn不在NRF上配置的PLMN ID标识的PLMN范围内，则说明requester-plmn与发现的NF的PLMN不同。如果查询参数中的requester-plmn与发现的NF的PLMN不同，Fqdn属性值应包含NF注册请求中的跨PLMN全量域名属性（interPlmnFqdn）。注4：所述NF服务消费者的负载参数的使用根据实际情况而定，例如，负载参数和其他参数一起用于NF选择和负载平衡服务。注5: 给定NF可以在NF Profile中注册包含在特定PLMN的多个PLMN ID。如果注册了多个PLMN ID，则该NF Profile的所有属性都应用在PlmnList中注册的每个PLMN ID。例外情况下，NF Profile（包括PLMN ID），例如基于IMSI的SUPI，TAI和GUAMI等属性，只应用在单个PLMN ID，此时，NF可能会在Profile中针对每个PLMN ID都注册这些属性，例如，UDM可能会针对不同PLMN ID在NF Profile多次注册相同属性，例如，SUPI范围（SUPI ranges）。
###### NFService 
NFService的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
serviceInstanceID|Mandatory|唯一标识给定NF实例的业务实例。
ServiceName|Mandatory|标识服务实例名称，例如“udm-sdm ”
versions|Mandatory|表示NF服务支持的API版本，及NF服务支持API版本的失效日期。不同的数组元素中“apiversioninuri”值唯一，因此“apifullversion”第一位版本号数字唯一。
scheme|Mandatory|表示URI方案，例如，HTTP或HTTPS。
nfServiceStatus|Mandatory|表示NF服务实例状态。
Fqdn|Optional|表示NF服务实例的全量域名（见注1+注3）。
IpEndPoint|Optional|表示用于监控接收到的服务请求的NF IP地址（包括IPv4和/或IPv6地址）和端口信息（见注1+注5）
apiPrefix|Optional|表示用于构造不同API URI的{apiRoot}变量可选路径段，API前缀以“/”开头，属于部署可选参数。
DefaultNotificationSubscription|Optional|表示不同通知类型的通知端点。
capacity|Optional|表示静态容量信息，即，相对于同种业务类型的其他NF实例权重。取值范围0~65535。（见注2）
load|Optional|表示最新已知的NF负载，取值0~100%（见注4）。
priority|Optional|表示NF选择时相对于同种服务类型的其他NF的优先级，取值范围0~65535；值越小，优先级越高，如果NF的nfServiceList参数包含该字段，优先选择nfServiceList中的优先级值。（见注2）
recoveryTime|Optional|表示NF重启/启动时的时间戳。
ChfServiceInfo|Optional|表示CHF服务实例数据。
SupportedFeatures|Optional|表示NF服务实例支持的特性。
注1：如果不携带fqdn和ipendpoint属性，则使用NF Profile中的全量域名（FQDN）和IP地址相关属性构造该业务的API URI。注2：如果携带容量和优先级参数，则容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似（见IETF RFC 2782[23] 定义）。注3：如果requester-plmn不在NRF上配置的PLMN ID标识的PLMN范围内，则说明requester-plmn与发现的NF服务返回的PLMN不同。如果查询参数中的requester-plmn与NF服务发现返回的PLMN不同，NF注册时，Fqdn属性值（如果携带）包含NF服务注册的跨PLMN全量域名属性（interPlmnFqdn）。注4：使用上述NF服务消费者的负载参数会根据具体场景发生变化，例如，负载参数和其他参数一起使用用于NF选择和负载均衡。注5：如果NF服务和NF Profile中缺少ipendpoint属性，则NF服务消费者应使用全量域名（fqdn）属性值进行DNS查询，如果DNS查询未返回端口号，则NF服务消费者使用默认端口号。当调用服务时，使用TCP端口80访问HTTP URI或使用TCP端口443访问HTTPS URL。|注1：如果不携带fqdn和ipendpoint属性，则使用NF Profile中的全量域名（FQDN）和IP地址相关属性构造该业务的API URI。注2：如果携带容量和优先级参数，则容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似（见IETF RFC 2782[23] 定义）。注3：如果requester-plmn不在NRF上配置的PLMN ID标识的PLMN范围内，则说明requester-plmn与发现的NF服务返回的PLMN不同。如果查询参数中的requester-plmn与NF服务发现返回的PLMN不同，NF注册时，Fqdn属性值（如果携带）包含NF服务注册的跨PLMN全量域名属性（interPlmnFqdn）。注4：使用上述NF服务消费者的负载参数会根据具体场景发生变化，例如，负载参数和其他参数一起使用用于NF选择和负载均衡。注5：如果NF服务和NF Profile中缺少ipendpoint属性，则NF服务消费者应使用全量域名（fqdn）属性值进行DNS查询，如果DNS查询未返回端口号，则NF服务消费者使用默认端口号。当调用服务时，使用TCP端口80访问HTTP URI或使用TCP端口443访问HTTPS URL。|注1：如果不携带fqdn和ipendpoint属性，则使用NF Profile中的全量域名（FQDN）和IP地址相关属性构造该业务的API URI。注2：如果携带容量和优先级参数，则容量和优先级参数用于NF选择和负载均衡。应用容量和优先级选择NF与选择服务器类似（见IETF RFC 2782[23] 定义）。注3：如果requester-plmn不在NRF上配置的PLMN ID标识的PLMN范围内，则说明requester-plmn与发现的NF服务返回的PLMN不同。如果查询参数中的requester-plmn与NF服务发现返回的PLMN不同，NF注册时，Fqdn属性值（如果携带）包含NF服务注册的跨PLMN全量域名属性（interPlmnFqdn）。注4：使用上述NF服务消费者的负载参数会根据具体场景发生变化，例如，负载参数和其他参数一起使用用于NF选择和负载均衡。注5：如果NF服务和NF Profile中缺少ipendpoint属性，则NF服务消费者应使用全量域名（fqdn）属性值进行DNS查询，如果DNS查询未返回端口号，则NF服务消费者使用默认端口号。当调用服务时，使用TCP端口80访问HTTP URI或使用TCP端口443访问HTTPS URL。
###### PreferredSearch 
PreferredSearch的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
preferredTaiMatchInd|Conditional|指示服务发现返回的NF Profile是否与查询参数preferred-tai相匹配。true：匹配false：不匹配
##### Nnrf_AccessToken specific Data Types 
###### AccessTokenReq 
AccessTokenReq的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
grant_type|Mandatory|该IE包含的授权类型为客户端凭据许可“client_credentials”。
NfInstanceId|Mandatory|该IE包含NF服务消费者的NF实例ID。
NFType|Conditional|当访问令牌请求针对特定NF类型，而非特定的NF/NF服务实例时，携带该IE。携带该IE时，该IE包含NF服务消费者的NF类型。
targetNfType|Conditional|当访问令牌请求针对特定NF类型，而非特定的NF/NF服务实例时，携带该IE。携带该IE时，该IE包含NF服务提供者的NF类型。
scope|Mandatory|该IE包含NF服务提供者的NF服务名，服务名之间以空格分隔。该属性包含的服务名是服务名称（ServiceName）枚举类型中定义的任何服务。模式： '^([a-zA-Z0-9_-]+)( [a-zA-Z0-9_-]+)*$'见注2。
targetNfInstanceId|Conditional|如需携带，或是针对特定NF服务提供者的访问令牌请求，则携带该IE。携带该IE时，该IE中包含请求访问令牌的特定NF服务提供者的NF实例ID。
requesterPlmn|Conditional|当属于一个PLMN中的NF服务消费者向来自不同PLMN的NF服务提供者请求服务访问授权时携带该IE。携带该IE时，该IE包含请求访问授权的NF服务消费者的PLMN ID。
targetPlmn|Conditional|当属于一个PLMN中的NF服务消费者向来自不同PLMN的NF服务提供者请求服务访问授权时携带该IE。携带该IE时，该IE包含目标PLMN的PLMN ID（即NF服务提供者的PLMN ID）。
targetSnssaiList|Optional|针对携带包含服务提供方NF类型的Token请求时可能携带该IE。携带该IE时，该IE包含服务提供方NF支持的S-NSSAI列表。
targetNsiList|Optional|针对携带包含服务提供方NF类型的Token请求时可能携带该IE。携带该IE时，该IE包含服务提供方NF支持的NSI列表。
注1：该数据结构不应作为JSON对象处理，应作为键值对数据结构进行处理，使用x-www-urlencoded编码格式进行编码。注2：范围（scope）属性在IETF RFC 6749中可选，在3GPP TS 33.501中必选。|注1：该数据结构不应作为JSON对象处理，应作为键值对数据结构进行处理，使用x-www-urlencoded编码格式进行编码。注2：范围（scope）属性在IETF RFC 6749中可选，在3GPP TS 33.501中必选。|注1：该数据结构不应作为JSON对象处理，应作为键值对数据结构进行处理，使用x-www-urlencoded编码格式进行编码。注2：范围（scope）属性在IETF RFC 6749中可选，在3GPP TS 33.501中必选。
###### AccessTokenRsp 
AccessTokenRsp的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
access_token|Mandatory|该IE应包含JSON Web签名（JWS）通过JWS压缩序列化后的JSON对象，包含AccessTokenClaims。
token_type|Mandatory|该IE包含令牌类型，例如JSON Web Token （JWT）和Bearer Token等。
expires_in|Conditional|携带此IE时，该IE包含访问令牌失效秒数。一般情况下携带该属性，除非通过其他方式（部署专用文档）提供失效时间。
scope|Conditional|携带该IE时，该IE包含NF服务提供者的NF服务名，服务名以空格分隔。该属性包含的服务名是服务名称（ServiceName）枚举类型中定义的任何服务。如果该属性与访问令牌请求中包含的scope范围不同，则携带；如果该属性与访问令牌请求中包含的scope范围相同，则不携带。模式： '^([a-zA-Z0-9_-]+)( [a-zA-Z0-9_-]+)*$'
###### AccessTokenClaims 
AccessTokenClaims的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
issuer|Mandatory|该IE包含NRF的NF实例ID。
subject|Mandatory|该IE包含NF服务消费者的NF实例ID。
Audience|Mandatory|该IE包含NF服务提供者的NF实例ID（如果已知NF服务提供者的NF实例）或适用该声明的NF服务提供者的NF类型。
scope|Mandatory|该IE应包含被授权使用接入令牌（access_token）的NF服务名称。服务名称可以包含通配符。模式： '^([a-zA-Z0-9_-]+)( [a-zA-Z0-9_-]+)*$'
expiration|Mandatory|携带此IE时，该IE应包含访问令牌失效秒数。
###### Audience 
Audience的数据结构参见下表： 
属性名称|描述
---|---
NFType|NF类型。
array(NfInstanceId)|NF实例ID数组。
### Nudm 
#### Nudm接口协议简介 
场景描述 :Nudm是UDM为其他NF提供服务的接口如下图所示。 
图1  Nudm接口示意图
[]images/1.png)
协议栈 :Nudm和其他所有服务化接口一样，都采用如下图所示的协议栈，应用层统一采用HTTP/2协议，携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
图2  服务化接口协议栈
[]images/2.png)
##### 网络功能服务列表 
UDM通过Nudm接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括表1所定义的各种。 
NF|NFS|NFS的解释
---|---|---
UDM|Nudm_SubscriberDataManagement|该服务的关键功能如下：允许NF服务消费者在必要时查询用户签约数据向签约的NF服务消费者提供更新后的用户数据
Nudm_UEContextManagement|UDM|该服务的关键功能如下：提供与用户事务信息相关的NF服务消费者信息，包括用户的服务NF标识、用户状态等允许NF服务消费者在UDM中注册和去注册服务UE的信息允许NF服务消费者更新UDM中的部分UE上下文信息
Nudm_UEAuthentication|UDM|该服务的关键功能如下：向订阅的NF消费者提供更新的鉴权相关的用户数据。对于基于AKA的身份验证，可用于从安全上下文同步失败情况恢复。用于通知UE鉴权过程的结果。
Nudm_EventExposure|UDM|该服务的关键功能如下：允许NF消费者订阅接收事件。向订阅的NF消费者提供事件的监视指示。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Nudm接口上提供的各服务以及各服务支持的服务操作参见下表。 
服务名称|服务操作|服务操作的解释
---|---|---
Nudm_SubscriberDataManagement|Get|NF服务消费者（例如，AMF、SMF）使用Nudm_SubscriberDataManagement服务和通过Get服务操作从UDM中查询与NF服务消费者相关的用户个人签约数据。
Subscribe|Nudm_SubscriberDataManagement|用于NF服务消费者通过Subscribe服务操作订阅数据变更通知。
Unsubscribe|Nudm_SubscriberDataManagement|通过Unsubscribe服务操作取消签约数据变更通知。如果支持“共享数据”特性，也可以通过Unsubscribe服务操作取消订阅共享数据变更通知。
Notification|Nudm_SubscriberDataManagement|用于已经订阅数据变更的NF服务消费者（例如，AMF、SMF）在UDM变更签约数据时通过Notification服务操作获取通知。
ModifySubscription|Nudm_SubscriberDataManagement|用于修改对数据更改通知的订阅（对于UE单个数据）和对共享数据更改通知的订阅。
Nudm_UEContextManagement|Registration|NF服务消费者（例如，AMF、SMF）使用Nudm_UEContextManagement服务和通过Registration服务操作在UDM注册。
DeregistrationNotification|Nudm_UEContextManagement|用于已经注册的NF服务消费者(例如，AMF)在UDM去注册NF服务消费者时，通过DeregistrationNotification服务操作获取通知。
Deregistration|Nudm_UEContextManagement|用于已经注册的NF服务消费者（例如，AMF、SMF）通过Deregistration服务操作从UDM去注册。
Get|Nudm_UEContextManagement|用于NF服务消费者（例如，NEF）通过Get服务操作从UDM查询注册信息。
Update|Nudm_UEContextManagement|用于已经注册的NF服务消费者（例如，AMF）通过Update服务操作更新存储在UDM中的注册信息。
P-CSCF-RestorationNotification|Nudm_UEContextManagement|用于已经注册的NF服务消费者（例如，AMF、SMF）在UDM检测到需要P-CSCF故障恢复时，通过P-CSCF-RestorationNotification服务操作获取通知。
Nudm_UEAuthentication|Get|用于NF服务消费者（AUSF）向UDM请求SUPI/SUCI的鉴权信息数据。如果提供了SUCI，则UDM从SUCI计算SUPI。如果选择5GAKA或EAP-AKA′，则UDM考虑从NF服务消费者（AUSF）接收的信息和该资源的当前表示，来计算鉴权向量。
ResultConfirmationInform|Nudm_UEAuthentication|为防止用户向UDM发起虚假的位置更新请求进行网络欺诈（如未在拜访网进行鉴权即向UDM进行位置登记等），UDM可以把位置更新业务和鉴权业务关联起来。该场景下，需要AUSF向UDM发起鉴权确认消息，告知UDM用户的鉴权成功或不成功。
Nudm_EventExposure|Subscribe|NEF等NF到UDM订阅事件监控通知消息。可监控的事件包括：连接丢失、UE可达通知、位置上报、IMEI改变等。对于需要AMF处理的监控事件，UDM需要把订阅请求发给AMF。
Unsubscribe|Nudm_EventExposure|NEF等NF到UDM去订阅事件监控通知消息。对于需要AMF处理的监控事件，UDM需要把去订阅请求发给AMF。
Notify|Nudm_EventExposure|被订阅的事件触发后，UDM向NEF上报通知消息。AMF上报的通知消息，由AMF直接报给NEF。
ModifySubscription|Nudm_EventExposure|当需要修改之前在UDM上自行创建的现有订阅时，由NF Service Consumer（例如NEF）向UDM调用服务操作。
##### Nudm_SubscriberDataManagement_Get 
Nudm_SDM_Get 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_SubscriberDataManagement_Get|Request/Response|该服务操作应用于NF服务消费者（例如，AMF）向UDM发送GET请求获取用户个人数据，包含：Slice Selection Subscription Data RetrievalAccess and Mobility Subscription Data RetrievalSMF Selection Subscription Data RetrievalSession Management Subscription Data RetrievalSMS Subscription Data RetrievalSMS Management Subscription Data RetrievalUE Context in SMF Data RetrievalUE Context in SMSF Data RetrievalRetrieval Of Multiple Data SetsIdentifier Translation
##### Nudm_SubscriberDataManagement_Subscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_SubscriberDataManagement_Subscribe|Subscribe/Notify|该服务操作用于Subscription to notifications of data change流程中。NF服务消费者订阅用户数据，由UDM检查用户的数据类型。UDM应检查被请求的消费者是否有权订阅请求的更新。
##### Nudm_SubscriberDataManagement_Unsubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_SubscriberDataManagement_Unsubscribe|Subscribe/Notify|该服务操作用于Unsubscribe to notifications of data change流程中。
##### Nudm_SubscriberDataManagement_Notification 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_SubscriberDataManagement_Notification|Subscribe/Notify|该服务操作用于Data Change Notification To NF流程中。
##### Nudm_SubscriberDataManagement_ModifySubscription 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_SubscriberDataManagement_ModifySubscription|Subscribe/Notify|该服务操作用于Modification of a subscription to notifications of data change流程中。
##### Nudm_UEContextManagement_Registration 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEContextManagement_Registration|Request/Response|该服务操作用于AMF Registration for 3GPP Access、SMF Registration、SMSF Registration for 3GPP Access等流程中。
##### Nudm_UEContextManagement_DeregistrationNotification 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEContextManagement_DeregistrationNotification|Subscribe/Notify|该服务操作用于UDM initiated NF Deregistration流程中。
##### Nudm_UEContextManagement_Deregistration 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEContextManagement_Deregistration|Request/Response|该服务操作用于AMF deregistration for 3GPP access、SMF deregistration、SMSF deregistration for 3GPP access等流程中。
##### Nudm_UEContextManagement_Get 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEContextManagement_Get|Request/Response|该服务操作用于查询Amf3GppAccessRegistration Information Retrieval、SmsfRegistration Information Retrieval for 3GPP Access等流程中。
##### Nudm_UEContextManagement_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEContextManagement_Update|Request/Response|该服务操作用于Update A Parameter (e.g. PEI) in the AMF Registration For 3GPP Access流程中。
##### Nudm_UEContextManagement_P-CSCF-RestorationNotification 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEContextManagement_P-CSCF-RestorationNotification|Subscribe/Notify|该服务操作用于UDM initiated P-CSCF-Restoration流程中。
##### Nudm_UEAuthentication_Get 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEAuthentication_Get|Request/Response|该服务操作用于Authentication Information Retrieval流程中。
##### Nudm_UEAuthentication_ResultConfirmationInform 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_UEAuthentication_ResultConfirmationInform|Request/Response|该服务操作用于Authentication Confirmation流程中。
##### Nudm_EventExposure_Subscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_EventExposure_Subscribe|Subscribe/Notify|该服务操作用于Subscription to Notification of event occurrence流程中。
##### Nudm_EventExposure_Unsubscribe 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_EventExposure_Unsubscribe|Subscribe/Notify|该服务操作用于Unsubscribe to notifications of event occurrence流程中。
##### Nudm_EventExposure_Notify 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_EventExposure_Notify|Subscribe/Notify|该服务操作用于Event Occurrence Notification流程中。
##### Nudm_EventExposure_ModifySubscription 
服务操作|操作语义|服务操作的解释
---|---|---
Nudm_EventExposure_Notify|Subscribe/Notify|该服务操作用于Modification of a subscription流程中。
#### 数据类型解释 
##### Nssai 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
defaultSingleNssais|必选|默认S-NSSAI列表。|《3GPP TS 29.503》协议6.1.6.2.2章节
singleNssais|可选|S-NSSAI列表。|《3GPP TS 29.503》协议6.1.6.2.2章节
##### SdmSubscription 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
nfInstanceId|必选|创建订阅的NF实例标识。|《3GPP TS 29.503》协议6.1.6.2.3章节
implicitUnsubscribe|可选|如果取值为true，则表示当nfInstanceId所标识的订阅NF（AMF、SMF和SMSF）停止在UDM注册时，该订阅失效。|《3GPP TS 29.503》协议6.1.6.2.3章节
expires|条件可选|表示订阅失效的时间点。当不携带implicitUnsubscribe或implicitUnsubscribe取值为false时，携带该信元。POST请求中发送建议的失效时间，POST响应中返回确认的失效时间。|《3GPP TS 29.503》协议6.1.6.2.3章节
callbackReference|必选|NF服务消费者提供的URI，用于接收通知。|《3GPP TS 29.503》协议6.1.6.2.3章节
monitoredResourceUris|必选|一组URI，用于标识触发了变更通知的资源。|《3GPP TS 29.503》协议6.1.6.2.3章节
singleNssai|可选|如果消费者是SMF，则可能携带此信元。|《3GPP TS 29.503》协议6.1.6.2.3章节
dnn|可选|如果消费者是SMF，则可能携带此信元。说明：如果不包含singleNssai和dnn，则UDM会将数据变更通知所有DNN配置和网络切片。如果包含singleNssai但不包含dnn，则UDM会将数据变更通知singleNssai所标识的网络切片和singleNssai所标识的请求网络切片的所有DNN配置。如果不包含singleNssai但包含dnn，则UDM会将数据变更通知所有可用DNN的网络切片和dnn标识的所有DNN配置。如果包含singleNssai和dnn，若singleNssai所标识的网络切片中有该DNN，则UDM会将数据变更通知singleNssai所标识的网络切片和dnn标识的所有DNN配置。|《3GPP TS 29.503》协议6.1.6.2.3章节
##### AccessAndMobilitySubscriptionData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
gpsis|可选|一般公共订阅标识符列表。|《3GPP TS 29.503》协议6.1.6.2.4章节
subscribedUeAmbr|可选|UE级别的用户速率，包含上行和下行。|《3GPP TS 29.503》协议6.1.6.2.4章节
nssai|可选|网络切片选择辅助信息。|《3GPP TS 29.503》协议6.1.6.2.4章节
ratRestrictions|可选|被限制的RAT类型列表。|《3GPP TS 29.503》协议6.1.6.2.4章节
forbiddenAreas|可选|禁止区域列表。|《3GPP TS 29.503》协议6.1.6.2.4章节
serviceAreaRestriction|可选|签约业务区限制。|《3GPP TS 29.503》协议6.1.6.2.4章节
coreNetworkTypeRestrictions|可选|受限核心网类型列表。|《3GPP TS 29.503》协议6.1.6.2.4章节
rfspIndex|可选|RAT/频率选择优先级索引。|《3GPP TS 29.503》协议6.1.6.2.4章节
subsRegTimer|可选|签约的周期注册定时器。|《3GPP TS 29.503》协议6.1.6.2.4章节
ueUsageType|可选|表示UE的使用特征，为EPS互操作选择特定的专用核心网。|《3GPP TS 29.503》协议6.1.6.2.4章节
mpsPriority|可选|表示终端是否已签约多媒体优先级业务。|《3GPP TS 29.503》协议6.1.6.2.4章节
activeTime|可选|PSM用户签约的激活时间。|《3GPP TS 29.503》协议6.1.6.2.4章节
dlPacketCount|可选|DL Buffering Suggested Packet Count信元用于表示是否需要对高时延通信的下行报文进行扩展缓存。|《3GPP TS 29.503》协议6.1.6.2.4章节
micoAllowed|可选|表示UE签约是否支持MICO模式。|《3GPP TS 29.503》协议6.1.6.2.4章节
odbPacketServices|可选|运营商闭锁分组业务。|《3GPP TS 29.503》协议6.1.6.2.4章节
##### SmfSelectionSubscriptionData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
supportedFeatures|可选|如果支持至少一个可选特性，则会携带该信元。|《3GPP TS 29.503》协议6.1.6.2.5章节
subscribedSnssaiInfos|可选|S-NSSAI及相关信息（DNN信息）列表。DnnInfo数组的映射（键值对列表，其中singleNssai转换为字符串并作为键值）|《3GPP TS 29.503》协议6.1.6.2.5章节
##### UeContextInSmfData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
pduSessions|可选|PduSessions的映射（键值对列表，其中singleNssai由整数转换为字符串并作为键值）。|《3GPP TS 29.503》协议6.1.6.2.16章节
pgwInfo|可选|和EPS对接的DNN/APN和PGW-C+SMF FQDN的信息。|《3GPP TS 29.503》协议6.1.6.2.16章节
 
##### PduSession 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
dnn|必选|数据网络名称|《3GPP TS 29.503》协议6.1.6.2.17章节
smfInstanceId|必选|SMF的NF实例标识|《3GPP TS 29.503》协议6.1.6.2.17章节
plmnId|必选|SMF的PLMN标识|《3GPP TS 29.503》协议6.1.6.2.17章节
##### DnnInfo 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
dnn|必选|数据网络名称|《3GPP TS 29.503》协议6.1.6.2.6章节
defaultDnnIndicator|可选|表示该DNN是否为默认DNN。true：DNN为默认DNN。false：DNN不是默认DNN。如果未携带该属性，则表示该DNN不是默认DNN。|《3GPP TS 29.503》协议6.1.6.2.6章节
lboRoamingAllowed|可选|表示漫游时是否允许DNN本地分流。true：允许false：不允许如果未携带该属性，则表示不允许。|《3GPP TS 29.503》协议6.1.6.2.6章节
iwkEpsInd|可选|表示是否签约EPS互操作。true：签约false：未签约如果未携带该属性，则表示未签约。|《3GPP TS 29.503》协议6.1.6.2.6章节
##### SnssaiInfo 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
dnnInfos|必选|S-NSSAI及相关信息的数据网络名称列表。|《3GPP TS 29.503》协议6.1.6.2.7章节
##### SessionManagementSubscriptionData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
singleNssai|必选|单个网络切片选择辅助信息。|《3GPP TS 29.503》协议6.1.6.2.8章节
dnnConfigurations|可选|网络切片的附加DNN配置信息；DnnConfigurations的映射（键值对列表，其中dnn为键值）。|《3GPP TS 29.503》协议6.1.6.2.8章节
##### DnnConfiguration 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
pduSessionTypes|必选|默认/允许的会话类型。|《3GPP TS 29.503》协议6.1.6.2.9章节
sscModes|必选|默认/允许的SSC模式。|《3GPP TS 29.503》协议6.1.6.2.9章节
iwkEpsInd|可选|表示是否签约EPS互操作。true：签约false：未签约如果未携带该属性在，则表示未签约。|《3GPP TS 29.503》协议6.1.6.2.9章节
5gQosProfile|可选|数据网络会话相关的5G QoS参数。|《3GPP TS 29.503》协议6.1.6.2.9章节
sessionAmbr|可选|每个PDU会话中所有Non-GBR QoS流共享的上下行最大聚合比特率。|《3GPP TS 29.503》协议6.1.6.2.9章节
3gppChargingCharacteristics|可选|数据网络会话相关的签约计费特征信息。|《3GPP TS 29.503》协议6.1.6.2.9章节
staticIpAddress|可选|签约的IPv4和/或IPv6类型的静态IP地址。|《3GPP TS 29.503》协议6.1.6.2.9章节
upSecurity|可选|表示用户面完整性保护和加密的安全策略。|《3GPP TS 29.503》协议6.1.6.2.9章节
##### PduSessionTypes 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
defaultSessionType|必选|默认会话类型。|《3GPP TS 29.503》协议6.1.6.2.11章节
allowedSessionTypes|可选|数据网络支持的附加会话类型。|《3GPP TS 29.503》协议6.1.6.2.11章节
##### SscModes 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
defaultSscMode|必选|默认SSC模式。|《3GPP TS 29.503》协议6.1.6.2.12章节
allowedSscModes|可选|数据网络支持的附加SSC模式。|《3GPP TS 29.503》协议6.1.6.2.12章节
##### SubscriptionDataSets 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
amData|可选|接入和移动签约数据。|《3GPP TS 29.503》协议6.1.6.2.15章节
smfSelData|可选|SMF选择的签约数据。|《3GPP TS 29.503》协议6.1.6.2.15章节
uecSmfData|可选|SMF数据中的UE上下文。|《3GPP TS 29.503》协议6.1.6.2.15章节
uecSmsfData|可选|SMSF数据中的UE上下文。|《3GPP TS 29.503》协议6.1.6.2.15章节
smsSubsData|可选|短信业务的签约数据。|《3GPP TS 29.503》协议6.1.6.2.15章节
smData|可选|会话管理的签约数据。|《3GPP TS 29.503》协议6.1.6.2.15章节
smsMngData|可选|短信业务管理的签约数据。|《3GPP TS 29.503》协议6.1.6.2.15章节
##### IdTranslationResult 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
supportedFeatures|可选|如果支持至少一个可选特性，则会携带该信元。|《3GPP TS 29.503》协议6.1.6.2.18章节
supi|必选|用户的SUPI。|《3GPP TS 29.503》协议6.1.6.2.18章节
gpsi|可选|取值为MSISDN。|《3GPP TS 29.503》协议6.1.6.2.18章节
##### IpAddress 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
ipv4Addr|条件可选|表示IPv4地址。|《3GPP TS 29.503》协议6.1.6.2.22章节
ipv6Addr|条件可选|表示IPv6地址。|《3GPP TS 29.503》协议6.1.6.2.22章节
ipv6Prefix|条件可选|表示IPv6地址前缀。|《3GPP TS 29.503》协议6.1.6.2.22章节
[]images/1608609046658.PNG)携带ipv4Addr， ipv6Addr，和ipv6Prefix其中一个信元。 
##### ModificationNotification 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
notifyItems|必选|变更通知列表。|《3GPP TS 29.503》协议6.1.6.2.21章节
##### PgwInfo 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
dnn|必选|DNN/APN|《3GPP TS 29.503》协议6.1.6.2.28章节
pgwFqdn|必选|PGW-C+SMF的FQDN|《3GPP TS 29.503》协议6.1.6.2.28章节
plmnId|可选|PGW-C+SMF所在的PLMN|《3GPP TS 29.503》协议6.1.6.2.28章节
##### Amf3GppAccessRegistration 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
amfInstanceId|必选|AMF在NRF中注册的身份标识。|《3GPP TS 29.503》协议6.2.6.2.2章节
deregCallbackUri|必选|AMF提供的URI，用于接收（隐式订阅）去注册通知。去注册回调URI在AMF集中唯一标识要去注册的UE。|《3GPP TS 29.503》协议6.2.6.2.2章节
guami|必选|表示服务AMF的GUAMI。|《3GPP TS 29.503》协议6.2.6.2.2章节
ratType|必选|表示UE当前的RAT类型。|《3GPP TS 29.503》协议6.2.6.2.2章节
supportedFeatures|可选|如果支持至少一个可选特性，则会携带该信元。|《3GPP TS 29.503》协议6.2.6.2.2章节
purgeFlag|可选|该标志表示是否已去注册AMF。注册服务操作中不携带。|《3GPP TS 29.503》协议6.2.6.2.2章节
pei|可选|永久设备标识。|《3GPP TS 29.503》协议6.2.6.2.2章节
imsVoPs|可选|如果服务AMF的所有TA同时支持或者不同时支持"IMS Voice over PS Sessions"时，该信元用于表示单个用户。如果不同时支持或者支持情况未知，不携带该信元。如果该信元缺失，则认为不同时支持或未知。|《3GPP TS 29.503》协议6.2.6.2.2章节
pcscfRestorationCallbackUri|可选|AMF提供的URI，用于接收P-CSCF恢复的（隐式订阅）通知。|《3GPP TS 29.503》协议6.2.6.2.2章节
amfServiceNamePcscfRest|可选|该信元指示向哪个AMF服务名称发送P-CSCF恢复通知。如果携带了pcscfRestorationCallbackUri，则可能携带该信元。|《3GPP TS 29.503》协议6.2.6.2.2章节
initialRegistrationInd|条件可选|当UE进行初始注册时，AMF会携带该信元并将该信元设置为true。如果UE不是进行初始注册，则不携带该信元或者将该信元设置为false。|《3GPP TS 29.503》协议6.2.6.2.2章节
drFlag|可选|双注册标志。该标志取值为true时，表示如果存在已注册MME，UDM+HSS不需要向该MME发送S6a-CLR。否则，如果存在已注册MME，需要去注册该MME。|《3GPP TS 29.503》协议6.2.6.2.2章节
##### SmfRegistration 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
smfInstanceId|必选|SMF的NF实例标识。|《3GPP TS 29.503》协议6.2.6.2.4章节
supportedFeatures|可选|如果支持至少一个可选特性，则会携带该信元。|《3GPP TS 29.503》协议6.2.6.2.4章节
pduSessionId|必选|PDU会话ID。|《3GPP TS 29.503》协议6.2.6.2.4章节
singleNssai|必选|单个网络切片选择辅助信息。|《3GPP TS 29.503》协议6.2.6.2.4章节
dnn|必选|数据网络标识。|《3GPP TS 29.503》协议6.2.6.2.4章节
pcscfRestorationCallbackUri|可选|SMF提供的URI，用于接收P-CSCF恢复的（隐式订阅）通知。|《3GPP TS 29.503》协议6.2.6.2.4章节
plmnid|必选|服务节点的PLMN标识。|《3GPP TS 29.503》协议6.2.6.2.4章节
pgwFqdn|条件可选|PGW-C+SMF的FQDN，用于与EPS对接。|《3GPP TS 29.503》协议6.2.6.2.4章节
##### DeregistrationData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
deregReason|必选|枚举DeregistrationReason表示Deregistration Notification原因，应遵循已有规定。"UE_INITIAL_REGISTRATION""UE_REGISTRATION_AREA_CHANGE""SUBSCRIPTION_WITHDRAWN""5GS_TO_EPS_MOBILITY""5GS_TO_EPS_MOBILITY_UE_INITIAL_REGISTRATION""REREGISTRATION_REQUIRED"|《3GPP TS 29.503》协议6.2.6.2.5章节
accessType|必选|用户去注册的接入类型。|《3GPP TS 29.503》协议6.2.6.2.5章节
##### Amf3GppAccessRegistrationModification 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
guami|必选|发送修改请求的AMF的Guami。如果guami中的MCC、MNC、AMF区域ID和AMF集ID与存储的值不匹配，则拒绝修改请求。|《3GPP TS 29.503》协议6.2.6.2.7章节
purgeFlag|可选|该标志表示是否已去注册AMF。去注册服务操作中携带，取值为TRUE。|《3GPP TS 29.503》协议6.2.6.2.7章节
pei|可选|永久设备标识。|《3GPP TS 29.503》协议6.2.6.2.7章节
imsVoPs|可选|如果服务AMF的所有TA同时支持或者不同时支持"IMS Voice over PS Sessions"时，该信元用于表示单个用户。如果不同时支持或者支持情况未知，不携带该信元。|《3GPP TS 29.503》协议6.2.6.2.7章节
 
##### PcscfRestorationNotification 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
supi|必选|故障P-CSCF服务的SUPI。|《3GPP TS 29.503》协议6.2.6.2.9章节
### Nausf 
#### Nausf接口协议简介 
场景描述 :Nausf是AUSF为其他NF提供服务的接口如下图所示。 
图1  Nausf接口示意图
[]images/1.PNG)
协议栈 :Nausf和其他所有服务化接口一样，都采用如下图所示的协议栈，应用层统一采用HTTP/2协议，携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
图2  服务化接口协议栈
[]images/3.PNG)
##### 网络功能服务列表 
AUSF通过Nausf接口向其他NF提供多种服务（NFS，Network Function Service），具体服务包括下表所定义的各种： 
NF|NFS|NFS的解释
---|---|---
AUSF|Nausf_UEAuthentication|AUSF向请求方NF提供UE认证服务。对于AKA鉴权，也可以通过该操作恢复安全上下文同步失败，并提供一个或多个主密钥，AMF用主密钥导出后续密钥。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Nausf接口上提供的各服务以及各服务支持的服务操作见下表： 
服务名称|服务操作|服务操作的解释
---|---|---
Nausf_UEAuthentication Service|Authenticate|支持AMF对UE进行鉴权。
##### Nausf_UEAuthentication Service_Authenticate 
服务操作|操作语义|服务操作的解释
---|---|---
Nausf_UEAuthentication Service_Authenticate|Request/Response|Authenticate服务操作允许请求者NF通过向AUSF提供如下信息发起对UE的认证：UE标识（例如，SUPI）服务网络名称AUSF从UDM检索UE的签约鉴权方法，根据UDM提供的信息，进入以下过程：5G-AKA鉴权EAP鉴权AUSF为这两种流程生成新的资源。在不同的流程中，生成资源的内容不同且会返回给AMF。
#### 数据类型解释 
##### AuthenticationInfo 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
supiOrSuci|必选|携带UE的SUPI或SUCI。|《3GPP TS 29.509》协议6.1.6.2.2章节
servingNetworkName|必选|携带服务网络名称。|《3GPP TS 29.509》协议6.1.6.2.2章节
resynchronizationInfo|可选|携带RAND和AUTS。|《3GPP TS 29.509》协议6.1.6.2.2章节
##### UEAuthenticationCtx 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
authType|必选|表示该用户所使用的鉴权方式。例如，5G-AKA-Confirmation、EAP-AKA，或EAP-TLS。|《3GPP TS 29.509》协议6.1.6.2.3章节
_links|必选|如果选择5G-AKA鉴权方式，该信元中携带名称为“5g-aka”的成员和用于执行确认的URI。如果选择EAP鉴权方式，该信元携带名称为“eap-session”的成员和用于执行EAP会话的URI。参见说明。|《3GPP TS 29.509》协议6.1.6.2.3章节
5gAuthData|必选|携带5G-AKA鉴权或EAP鉴权相关信息。|《3GPP TS 29.509》协议6.1.6.2.3章节
servingNetworkName|可选|携带服务网络名称。|《3GPP TS 29.509》协议6.1.6.2.3章节
说明：当前版本API只提供一个超媒体链接。|说明：当前版本API只提供一个超媒体链接。|说明：当前版本API只提供一个超媒体链接。|说明：当前版本API只提供一个超媒体链接。
##### 5gAuthData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
Av5gAka|必选|如果选择了5G-AKA鉴权，则携带5G AV。|《3GPP TS 29.509》协议6.1.6.2.4章节
EapPayload|必选|携带EAP报文请求。|《3GPP TS 29.509》协议6.1.6.2.4章节
##### AV5gAka 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
rand|必选|鉴权向量之一。|《3GPP TS 29.509》协议6.1.6.2.5章节
autn|必选|鉴权向量之一。|《3GPP TS 29.509》协议6.1.6.2.5章节
hxresStar|必选|鉴权向量之一。|《3GPP TS 29.509》协议6.1.6.2.5章节
##### ConfirmationData 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
resStar|必选|携带UE向AMF提供的RES*。|《3GPP TS 29.509》协议6.1.6.2.6章节
##### EapSession 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
eapPayload|必选|携带EAP报文。|《3GPP TS 29.509》协议6.1.6.2.7章节
kSeaf|条件可选|如果鉴权成功，则携带kseaf。|《3GPP TS 29.509》协议6.1.6.2.7章节
_links|条件可选|如果EAP会话需要其它交互，例如EAP AKA鉴权通知，则该信元应携带名称为“eap-session”的成员和用于继续EAP会话的URI。参见说明。|《3GPP TS 29.509》协议6.1.6.2.7章节
authResult|条件可选|表示鉴权结果。|《3GPP TS 29.509》协议6.1.6.2.7章节
supi|条件可选|如果鉴权成功且AMF提供了SUCI，则该信元携带UE的SUPI。|《3GPP TS 29.509》协议6.1.6.2.7章节
说明：当前版本API最多提供1个超媒体链接。|说明：当前版本API最多提供1个超媒体链接。|说明：当前版本API最多提供1个超媒体链接。|说明：当前版本API最多提供1个超媒体链接。
##### ConfirmationDataResponse 
属性名称|可选必选说明|描述|参考协议
---|---|---|---
authResult|必选|表示鉴权结果。|《3GPP TS 29.509》协议6.1.6.2.8章节
supi|条件可选|如果鉴权成功且AMF提供了SUCI，则该信元携带UE的SUPI。|《3GPP TS 29.509》协议6.1.6.2.8章节
kseaf|条件可选|如果鉴权成功，则携带Kseaf。|《3GPP TS 29.509》协议6.1.6.2.8章节
 
### Npcf 
#### Npcf接口协议简介 
场景描述 :Npcf是PCF为其他NF提供服务的接口。 
图1   Npcf接口示意图
[]images/1.PNG)
协议栈 :图2  服务化接口协议栈
[]images/33.png)
Npcf和其他所有服务化接口一样，都采用如上图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
##### 网络功能服务列表 
PCF通过Npcf接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括下表所定义的各种： 
NF|NFS|NFS的解释
---|---|---
PCF|Npcf_SMPolicyControl|该服务用于SMF向PCF发起PDU会话的PCC策略请求，并获取相关信息以便建立PDU会话。该服务的关键功能如下：根据SMF提供的PDU会话信息生成对应的SM策略关联，并将其下发给SMF。当策略控制请求触发器满足预置条件时，PCF根据SMF新上报的信息更新SM策略关联，并将其下发给SMF。当PCF内部定时器或签约变更触发策略变更时，PCF主动更新SM策略关联，并将其下发给SMF。
Npcf_AMPolicyControl|PCF|该服务用于AMF向PCF请求AM策略关联。该服务的关键功能如下：根据AMF提供的UE信息生成对应的AM策略关联，并将其下发给AMF。当策略控制请求触发器满足预置条件，或者AMF变更，新AMF定位到原PCF时，PCF根据AMF新上报的信息更新AM策略关联，并将其下发给AMF。当PCF内部定时器或签约变更触发策略变更时，PCF主动更新AM策略关联，并将其下发给AMF。
Npcf_UEPolicyControl|PCF|该服务用于AMF向PCF请求UE策略关联。PCF通过AMF向UE透传UE接入选择和PDU会话选择的相关策略信息。该服务的关键功能如下：根据AMF提供的UE信息生成对应的UE策略关联，并将其下发给AMF。当策略控制请求触发器满足预置条件，或者AMF变更，新AMF定位到原PCF时，PCF根据AMF新上报的信息更新UE策略关联，并将其下发给AMF。当PCF内部定时器或签约变更触发策略变更时，PCF主动更新UE策略关联，并将其下发给AMF。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Npcf接口上提供的各服务以及各服务支持的服务操作见下表： 
服务名称|服务操作|服务操作的解释
---|---|---
Npcf_SMPolicyControl|Create|用于PDU会话建立流程。SMF调用Npcf_SMPolicyControl_Create向PCF发送PDU会话相关信息，请求创建SM策略关联。
UpdateNotify|Npcf_SMPolicyControl|用于PCF发起的PDU会话更新流程。当PCF收到Rx/N5接口消息，或者PCF内部定时器/用户签约信息变更，触发策略变更时，PCF调用Npcf_SMPolicyControl_UpdateNotify，指示SMF更新或者删除SM策略关联。
Delete|Npcf_SMPolicyControl|用于PDU会话释放流程。SMF调用Npcf_SMPolicyControl_Delete向PCF请求删除PDU会话，释放相关资源。
Update|Npcf_SMPolicyControl|用于SMF发起的PDU会话更新流程。当策略控制请求触发器满足预置条件时，SMF调用Npcf_SMPolicyControl_Update，向PCF上报策略执行情况，PCF根据SMF新上报的信息更新SM策略关联，并将其下发给SMF。
Npcf_AMPolicyControl|Create|用于注册流程和AMF变更流程。在注册流程中，AMF调用Npcf_AMPolicyControl_Create向PCF提供UE上下文信息，请求创建AM策略关联。在AMF变更流程中，新AMF定位不到或者没有获取到PCF ID， 则AMF会选择一个新PCF。AMF调用Npcf_AMPolicyControl_Create向PCF提供UE上下文信息，请求创建AM策略关联。
UpdateNotify|Npcf_AMPolicyControl|用于PCF发起的AM策略关联更新流程。PCF内部定时器或签约变更触发策略变更时，PCF调用Npcf_AMPolicyControl_UpdateNotify，指示AMF更新或者删除AM策略关联。
Delete|Npcf_AMPolicyControl|用于去注册流程。AMF调用Npcf_AMPolicyControl_Delete向PCF请求删除AM策略关联，释放相关资源。
Update|Npcf_AMPolicyControl|用于AMF发起的AM策略关联更新流程。当策略控制请求触发器满足预置条件，或者AMF变更，新AMF定位到原PCF，AMF调用Npcf_AMPolicyControl_Update，向PCF上报策略执行情况，或者更新AMF信息。PCF根据AMF新上报的信息更新AM策略关联，并将其下发给AMF。
Npcf_UEPolicyControl|Create|用于注册流程和AMF变更流程。在注册流程中，AMF调用Npcf_UEPolicyControl_Create向PCF提供UE上下文信息，请求创建UE策略关联。在AMF变更流程中，新AMF定位不到或者没有获取到PCF ID， 则AMF会选择一个新PCF。AMF调用Npcf_UEPolicyControl_Create向PCF提供UE上下文信息，请求创建UE策略关联。
UpdateNotify|Npcf_UEPolicyControl|用于PCF发起的UE策略关联更新流程。PCF内部定时器或签约变更触发策略变更时，PCF调用Npcf_UEPolicyControl_UpdateNotify，指示AMF更新或者删除UE策略关联。
Delete|Npcf_UEPolicyControl|用于去注册流程。AMF调用Npcf_UEPolicyControl_Delete向PCF请求删除UE策略关联，释放相关资源。
Update|Npcf_UEPolicyControl|用于AMF发起的UE策略关联更新流程。当策略控制请求触发器满足预置条件，或者AMF变更，新AMF定位到原PCF，AMF调用Npcf_UEPolicyControl_Update，向PCF上报策略执行情况，或者更新AMF信息。PCF根据AMF新上报的信息更新UE策略关联，并将其下发给AMF。
##### Npcf_SMPolicyControl_Create 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_SMPolicyControl_Create|Request/Response|当SMF收到AMF发送的Nsmf_PDUSession_CreateSMContext Request请求创建SM上下文时，如果SMF判断需要向PCF获取PCC规则，则SMF调用Npcf_SMPolicyControl_Create，请求创建SM策略关联。SMF发送POST请求消息中包含SmPolicyContextData数据类型的对象。如果成功，PCF应响应状态码“201 Created”，并且PUT响应的消息体应包含SmPolicyDecision数据类型的对象，其中包含PccRule和policyCtrlReqTriggers数据类型的对象。如果失败，PCF应返回400/403/404/411/413/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_SMPolicyControl_UpdateNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_SMPolicyControl_UpdateNotify|Subscribe/Notify|当PCF收到Rx/N5接口消息，或者PCF内部定时器/用户签约信息变更，触发策略变更时，PCF调用Npcf_SMPolicyControl_UpdateNotify，指示SMF更新或者删除SM策略关联。对于SM策略关联更新流程：PCF发送POST请求消息中包含SmPolicyNotification数据类型的对象。如果成功，SMF应响应状态码“200 OK”，或者“204 No Content”。如果失败，SMF应返回400/401/404/411/413/415/500/503的HTTP状态码，并且消息体应包含一个ErrorReport数据结构。对于SM策略关联删除流程：PCF发送POST请求消息中包含TerminationNotification数据类型的对象。SMF收到请求消息后，应响应状态码“204 No Content”。之后SMF调用Npcf_SMPolicyControl_Delete操作，删除SM策略关联。如果失败，PCF应返回400/401/404/411/413/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_SMPolicyControl_Delete 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_SMPolicyControl_Delete|Request/Response|当SMF收到AMF发送的删除PDU会话相关的SM上下文请求时，如果SMF判断需要向PCF请求删除PDU会话，则SMF调用Npcf_SMPolicyControl_Delete，请求删除SM策略关联。SMF发送POST请求消息中包含SmPolicyDeleteData数据类型的对象。PCF通过向SMF发送“204 No Content”响应状态码来确认删除请求。如果失败，PCF应返回400/401/411/413/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_SMPolicyControl_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_SMPolicyControl_Update|Request/Response|当策略控制请求触发器满足预置条件时，SMF调用Npcf_SMPolicyControl_Update，向PCF上报策略执行情况，PCF根据SMF新上报的信息更新SM策略关联，并将其下发给SMF。SMF发送POST请求消息中包含SmPolicyUpdateContextData数据类型的对象，其中包含repPolicyCtrlReqTriggers数据类型的对象。如果成功，PCF应响应状态码“200 OK”，并且PUT响应消息体应包含SmPolicyDecision数据类型的对象。如果失败，PCF应返回400/401/403/411/413/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_AMPolicyControl_Create 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_AMPolicyControl_Create|Request/Response|该服务操作用于注册流程和AMF变更流程：当AMF收到UE用户发起的注册请求时，AMF调用Npcf_AMPolicyControl_Create向PCF提供UE上下文信息，请求创建AM策略关联。当AMF变更时，新AMF定位不到或者没有获取到PCF ID， 则AMF会选择一个新PCF。此时，AMF调用Npcf_AMPolicyControl_Create向PCF提供UE上下文信息，请求创建AM策略关联。AMF发送POST请求消息中包含PolicyAssociationRequest数据类型的对象。如果成功，PCF应响应状态码“201 Created”，并且PUT响应的消息体应包含PolicyAssociation数据类型的对象。如果失败，PCF应返回400/404/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_AMPolicyControl_UpdateNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_AMPolicyControl_UpdateNotify|Subscribe/Notify|PCF内部定时器触发策略变更时，PCF调用Npcf_AMPolicyControl_UpdateNotify，指示AMF更新或者删除AM策略关联。对于AM策略关联更新流程：PCF发送POST请求消息中包含PolicyUpdate数据类型的对象。如果成功，AMF应响应状态码“204 No Content”。如果失败，AMF应返回307/400/401/403/404/411/413/415/429/500/503的HTTP状态码。对于AM策略关联删除流程：PCF发送POST请求消息中包含TerminationNotification数据类型的对象。如果成功，AMF应响应状态码“204 No Content”。如果失败，AMF应返回307/400/401/403/404/411/413/415/429/500/503的HTTP状态码。
##### Npcf_AMPolicyControl_Delete 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_AMPolicyControl_Delete|Request/Response|当AMF收到UE用户发起的去注册请求，AMF调用Npcf_AMPolicyControl_Delete，请求删除AM策略控制关联。AMF发送HTTP DELETE请求消息。PCF通过向AMF发送“204 No Content”的HTTP响应状态码来确认删除请求。如果失败，PCF应返回400/404/500的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_AMPolicyControl_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_AMPolicyControl_Update|Request/Response|当策略控制请求触发器满足预置条件，AMF调用Npcf_AMPolicyControl_Update，向PCF上报策略执行情况，或者更新AMF信息，PCF根据AMF新上报的信息更新AM策略关联，并将其下发给AMF。AMF发送POST请求消息中包含PolicyAssociationUpdateRequest数据类型的对象。如果成功，PCF应响应状态码“200 OK”，并且PUT响应消息体应包含PolicyUpdate数据类型的对象。如果失败，PCF应返回400/404/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_UEPolicyControl_Create 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_UEPolicyControl_Create|Request/Response|该服务操作用于注册流程和AMF变更流程：当AMF收到UE用户发起的注册请求时，AMF调用Npcf_UEPolicyControl_Create向PCF提供UE上下文信息，请求创建UE策略关联。当AMF变更时，新AMF定位不到或者没有获取到PCF ID， 则AMF会选择一个新PCF。此时，AMF调用Npcf_UEPolicyControl_Create向PCF提供UE上下文信息，请求创建UE策略关联。AMF发送POST请求消息中包含PolicyAssociationRequest数据类型的对象。如果成功，PCF应响应状态码“201 Created”，并且PUT响应的消息体应包含PolicyAssociation数据类型的对象。如果失败，PCF应返回400/404/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_UEPolicyControl_UpdateNotify 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_UEPolicyControl_UpdateNotify|Subscribe/Notify|PCF内部定时器触发策略变更时，AMF调用Npcf_UEPolicyControl_UpdateNotify，指示AMF更新策略或者删除UE策略关联。对于UE策略关联更新流程：PCF发送POST请求消息中包含PolicyUpdate数据类型的对象。如果成功，AMF应响应状态码“204 No Content”。如果失败，AMF应返回307/400/404/411/413/415/429/500/503的HTTP状态码。对于UE策略关联删除流程：PCF发送POST请求消息中包含TerminationNotification数据类型的对象。如果成功，AMF应响应状态码“204 No Content”。如果失败，AMF应返回307/400/404/411/413/415/429/500/503的HTTP状态码。
##### Npcf_UEPolicyControl_Delete 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_UEPolicyControl_Delete|Request/Response|当AMF收到UE用户发起的去注册请求，AMF调用Npcf_UEPolicyControl_Delete，请求删除UE策略控制关联。AMF发送HTTP DELETE请求消息。PCF通过向AMF发送“204 No Content”的HTTP响应状态码来确认删除请求。如果失败，PCF应返回400/404/500的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
##### Npcf_UEPolicyControl_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Npcf_UEPolicyControl_Update|Request/Response|当策略控制请求触发器满足预置条件，AMF调用Npcf_UEPolicyControl_Update，向PCF上报策略执行情况，或者更新AMF信息，PCF根据AMF新上报的信息更新UE策略关联，并将其下发给AMF。AMF发送POST请求消息中包含PolicyAssociationUpdateRequest数据类型的对象。如果成功，PCF应响应状态码“200 OK”，并且PUT响应消息体应包含PolicyUpdate数据类型的对象。如果失败，PCF应返回400/404/415/500/503的HTTP状态码，并且消息体应包含一个ProblemDetails数据结构。
#### 数据类型解释 
##### Npcf_SMPolicyControl 
[SmPolicyControl](17.html)
[SmPolicyContextData](18.html)
[SmPolicyDecision](19.html)
[SmPolicyNotification](20.html)
[PccRule](21.html)
[SessionRule](22.html)
[QoSData](23.html)
[ConditionData](24.html)
[TrafficControlData](25.html)
[ChargingData](26.html)
[UsageMonitoringData](27.html)
[RedirectInformation](28.html)
[FlowInformation](29.html)
[SmPolicyDeleteData](30.html)
[QosCharacteristics](31.html)
[ChargingInformation](32.html)
[AccuUsageReport](33.html)
[SmPolicyUpdateContextData](34.html)
[UpPathChgEvent](35.html)
[TerminationNotification](36.html)
[AppDetectionInfo](37.html)
[AccNetChId](38.html)
[RequestedRuleData](39.html)
[RequestedUsageData](40.html)
[RuleReport](41.html)
[AuthorizedDefaultQos](42.html)
[servNfId](43.html)
[Guami](44.html)
[PlmnId](45.html)
[AmfId](46.html)
[Mcc](47.html)
[Mnc](48.html)
[AnGwAddress](49.html)
[SmfId](50.html)
###### SmPolicyControl 
SmPolicyControl的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
context|Mandatory|包含SMF请求的SM策略。
policy|Mandatory|包含PCF授权的SM策略。
###### SmPolicyContextData 
SmPolicyContextData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
AccNetChId|Optional|表示用户接入网络的默认QoS或整个PDU会话的网络计费标识。
chargEntityAddr|Optional|执行计费的网络实体的地址。
gpsi|Optional|表示通用公共订阅标识。一般使用MSISDN和外部标识作为GPSI标识。模式：^(msisdn-[0-9]{5,15}|extid-.+@.+|.+)$
supi|Conditional|表示用户永久标识。紧急呼叫可以不出现该属性。一般使用IMSI和NAI作为用户标识。模式：^(imsi-[0-9]{5,15}|nai-.+|.+)$
pduSessionId|Mandatory|表示用户的PDU会话标识。
dnn|Mandatory|表示用户接入PDU会话的数据网络名称。
InterGrpIds|Optional|内部组ID（s）。
notificationUri|Mandatory|表示PCF发送的SM策略更新通知的接收方。
pduSessionType|Mandatory|表示用户的PDU会话类型。取值如下：IPV4V6IPV4IPV6UNSTRUCTUREDETHERNET
accessType|Optional|表示用户接入网络的类型。取值如下：3GPP_ACCESSNON_3GPP_ACCESS
ratType|Optional|表示用户终端使用的无线接入技术。取值如下：NREUTRAWLANVIRTUALNBIOTGERAUTRA
servingNetwork|Optional|表示用户上线时所属的服务网络。
userLocationInfo|Optional|表示用户上线时所在的位置。
ueTimeZone|Optional|表示用户上线时所在的时区。
pei|Optional|表示永久设备标识，即用户绑定的终端标识。模式：^(imei-[0-9]{15}|imeisv-[0-9]{16}|.+)$
ipv4Address|Optional|表示分配给用户的IPv4地址，以字符串形式存储，以点分十进制表示法表示。
ipv6AddressPrefix|Optional|表示分配给用户的IPv6地址前缀，以字符串形式存储。
ipDomain|Optional|表示分配给用户的IPv4地址域标识。
subSessAmbr|Optional|表示用户签约的会话AMBR。
subsDefQos|Optional|表示用户签约的默认QoS信息。
numOfPackFilter|Optional|包含信令QoS规则的受支持的数据包过滤器的数量。
online|Optional|表示在线计费的使能开关。取值如下：true：开启在线计费。false：关闭在线计费。
offline|Optional|表示离线计费的使能开关。取值如下：true：开启离线计费。false：关闭离线计费。
chargingCharacteristics|Optional|包含PDU会话的计费特征，标识用户属性（预付费、后付费）。
3gppPsDataOffStatus|Optional|标识3GPP PS数据关闭状态。取值如下：如果包含该属性并且取值为“true”，则表示UE激活3GPP PS数据关闭状态。如果包含该属性并且取值为“false”，则表示3GPP PS数据关闭状态被UE关闭。
refQosIndication|Optional|标识用户是否支持反射QoS。取值如下：如果包含该属性并且取值为“true”，则表示支持反射QoS。如果包含该属性并且取值为“false”，则表示不支持反射QoS。
sliceInfo|Mandatory|标识S-NSSAI。
suppFeat|Conditional|表示支持的特性列表。模式： '^[A-Fa-f0-9]*$'
traceReq|Optional|跟踪控制和配置参数信息。
servNfId|Optional|用于标识包含接入网关信息的AMF服务。
SmfId|Optional|用于标识SMF网元实例。
###### SmPolicyDecision 
SmPolicyDecision的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
sessRules|Optional|表示一组会话规则。关键参数对应SessionRule的“sessRuleId”。
pccRules|Optional|表示一组PCC规则。关键参数对应PccRule的“pccRuleId”。
qosDecs|Optional|表示一组QoS数据策略决策。关键参数对应QoSData的“qosId”。
chgDecs|Optional|表示一组计费数据策略决策。关键参数对应ChargingData的“chgId”。
chargingInfo|Optional|表示计费信息，包含PDU会话的CHF地址。
traffContDecs|Optional|表示一组流量控制数据策略决策。关键参数对应TrafficControlData的“tcId”。
umDecs|Optional|表示一组流量分片数据策略决策。关键参数对应UsageMonitoringData的“umId”。
qosChars|Optional|表示一组非标准5QI和预配置5QI的QoS特征。关键参数对应QosCharacteristics的“5qi”。
reflectiveQoSTimer|Optional|表示反射QoS定时器时长。单位：秒
revalidationTime|Optional|表示PCC规则有效期，超过有效期后SMF需要重新请求PCC规则。比如当前时间2018-11-10 12:00:00，而“revalidationTime”取值为“30”，表示SMF应该在2018-11-10 12:30:00时刻上报消息给PCF，重新请求规则。单位：分钟
offline|Optional|表示离线计费的使能开关。取值如下：true：开启离线计费。false：关闭离线计费。
online|Optional|表示在线计费的使能开关。取值如下：true：开启在线计费。false：关闭在线计费。
conds|Optional|表示一组条件数据。关键参数对应ConditionData的“condId”。
pcscfRestIndication|Optional|表示P-CSCF恢复的使能开关。如果该属性不出现，则应用默认值“false”。取值如下：true：开启P-CSCF恢复。false：关闭P-CSCF恢复。
policyCtrlReqTriggers|Optional|表示策略控制触发需要下发的触发器。取值如下：PLMN_CHRES_MO_REAC_TY_CHUE_IP_CHUE MAC_CHAN_CH_CORUS_REAPP_STAAPP_STOAN_INFOCM_SES_FAILPS_DA_OFFDEF_QOS_CHSE_AMBR_CHQOS_NOTIFNO_CREDITPRA_CHSAREA_CHSCNN_CHRE_TIMEOUTRES_RELEASESUCC_RES_ALLORAT_TY_CHREF_QOS_IND_CHHW_TETHERING_RESCELL_CHAN_CH_COR
lastReqRuleData|Optional|定义PCF请求的最新的规则控制数据列表。
lastReqUsageData|Optional|定义PCF请求的最新的使用量数据。
praInfos|Optional|定义PCF下发的PRA信息。
ipv4Index|Conditional|IPv4地址分配方式。
ipv6Index|Conditional|IPv6地址分配方式。
qosFlowUsage|Optional|默认QoS流的使用方法。取值如下：GENERAL：通用。IMS_SIG：IMS信令。
suppFeat|Conditional|表示支持的特性列表。模式： '^[A-Fa-f0-9]*$'
###### SmPolicyNotification 
SmPolicyNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
resourceUri|Mandatory|通知有关的单个SM策略的资源URI。
SmPolicyDecision|Mandatory|SM策略。
###### PccRule 
PccRule的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
flowInfos|Conditional|表示一组IP数据流的过滤信息。
appId|Conditional|表示对UPF配置的应用程序检测过滤器的引用。
pccRuleId|Mandatory|表示PDU会话中PCC规则的唯一标识。
precedence|Optional|规则优先级，确定该PCC规则在同一个PDU会话内与其他PCC规则的使用顺序。
afSigProtocol|Optional|AF的信令标识，UE与AF之间的信令协议。取值如下：NO_INFORMATIONSIP
appReloc|Optional|AF业务路由能力，指示应用迁移的可能性。取值如下：true：开启AF业务路由。false：关闭AF业务路由。
refQosData|Optional|引用QoSData类型中的“qosId”。
refTcData|Optional|引用TrafficControlData中的“tcId”。
refChgData|Optional|引用ChargingData中的“chgId”。
refUmData|Optional|引用UsageMonitoringData中的“umId”。
refCondData|Optional|引用ConditionData中的“condId”。
###### SessionRule 
SessionRule的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
authSessAmbr|Optional|表示授权的会话AMBR。
authDefaultQos|Optional|表示授权的默认QoS信息。
sessRuleId|Mandatory|表示PDU会话中的会话规则的唯一标识。
refUmData|Optional|引用UsageMonitoringData中的“umId”。
refCondData|Optional|引用ConditionData中的“condId”。
###### QoSData 
QoSData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
qosId|Mandatory|表示PDU会话中QoS控制策略数据的唯一标识。
5qi|Mandatory|5G QoS标识，定义服务数据流的授权QoS参数的标识。
maxbrUl|Optional|表示上行最大带宽。单位：bps
maxbrDl|Optional|表示下行最大带宽。单位：bps
gbrUl|Optional|表示保障上行带宽。单位：bps
gbrDL|Optional|表示保障下行带宽。单位：bps
Arp|Mandatory|表示QoS分配和保留优先级。
qnc|Optional|表示当QoS流在QoS流的生存期内不再（或再次）满足QoS流时，是否从3GPP RAN请求通知。取值如下：true：开启通知。false：关闭通知。
reflectiveQos|Optional|表示QoS信息是否反射相应服务数据流。取值如下：true：是。false：否。
sharingKeyDl|Optional|通过包含相同的值，指示PCC规则可以在下行链路方向上共享资源。
sharingKeyUl|Optional|通过包含相同的值，指示PCC规则可以在上行链路方向上共享资源。
priorityLevel|Optional|表示QoS流中调度资源的优先级。
averWindow|Optional|表示计算保证和最大比特率的持续时间。单位：毫秒
maxDataBurstVol|Optional|表示在5G-AN PDB期间需要传输的最大数据量。单位：Byte
maxPacketLossRateDl|Optional|表示服务数据流可以容忍的丢包的下行最大速率。
maxPacketLossRateUl|Optional|表示服务数据流可以容忍的丢包的上行最大速率。
defQosFlowIndication|Optional|表示动态PCC规则是否与默认QoS规则关联的QoS流绑定。取值如下：true：开启绑定。false：关闭绑定。
###### ConditionData 
ConditionData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
condId|Mandatory|表示PDU会话中条件数据的唯一标识。
activationTime|Mandatory|表示条件数据被激活的时间。
deactivationTime|Optional|表示条件数据被去激活的时间。
###### TrafficControlData 
TrafficControlData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
tcId|Mandatory|表示PDU会话中流量控制数据的唯一标识。
flowStatus|Optional|流状态，确定对流量执行什么动作。取值如下：ENABLED-UPLINKENABLED-DOWNLINKENABLEDDISABLEDREMOVED
redirectInfo|Optional|指示是否将检测到的应用程序流量重定向到其他受控地址。
muteNotif|Optional|指示是否要将应用程序的启动或停止通知屏蔽。取值如下：true：开启屏蔽。false：关闭屏蔽。
trafficSteeringPolIdDl|Optional|指示SMF下行链路流量的预配置流量导向策略。
trafficSteeringPolIdUl|Optional|指示SMF上行链路流量的预配置流量导向策略。
###### ChargingData 
ChargingData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
chgId|Mandatory|表示PDU会话中计费控制策略数据的唯一标识。
meteringMethod|Optional|定义离线计费的方法。取值如下：DURATIONVOLUMEDURATION_VOLUMEEVENT
offline|Optional|表示离线计费的使能开关。取值如下：true：开启离线计费。false：关闭离线计费。
online|Optional|表示在线计费的使能开关。取值如下：true：开启在线计费。false：关闭在线计费。
ratingGroup|Optional|表示PCC规则中的计费标识。
reportingLevel|Optional|表示SMF上报相关PCC规则使用情况的级别。取值如下：SER_ID_LEVELRAT_GR_LEVELSPON_CON_LEVEL
serviceId|Optional|服务标识，表示PCC规则中的业务数据流所属的服务或服务组件的标识。
sponsorId|Optional|表示供应商标识。
appSvcProvId|Optional|表示应用服务提供商标识。
afChargingIdentifier|Optional|AF提供的标识，从AF提供的标识符将该PCC规则中的计费键值/服务标识符值的测量与应用级别报告相关联。
###### UsageMonitoringData 
UsageMonitoringData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
umId|Mandatory|表示PDU会话中流量使用情况监控策略数据的唯一标识。
volumeThreshold|Optional|表示总流量分片。单位：KB
volumeThresholdUplink|Optional|表示上行流量分片。单位：KB
volumeThresholdDownlink|Optional|表示下行流量分片。单位：KB
timeThreshold|Optional|表示时长分片。单位：秒
monitoringTime|Optional|监控时间，指示下一个流量分片的时间。
nextVolThreshold|Conditional|监控时间后的流量分片，表示下次总流量分片。单位：KB
nextVolThresholdUplink|Optional|监控时间后的上行流量片，表示下次上行流量分片。单位：KB
nextVolThresholdDownlink|Optional|监控时间后的上行流量片，表示下次下行流量分片。单位：KB
nextTimeThreshold|Conditional|监控时间后的时长分片，表示下次时长分片。单位：秒
inactivityTime|Optional|去激活时间，指示没有收到数据包的情况下，时间测量停止的时间段。单位：秒
exUsagePccRuleIds|Conditional|包含对应服务数据流需要从PDU会话使用监控中排除的PCC规则标识符，其中相应的服务数据流应从PDU会话使用中排除。该属性只包含在“UsageMonitoringData”实例中，用于会话级使用监控。
###### RedirectInformation 
RedirectInformation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
redirectSupport|Mandatory|指示是否支持重定向功能。
redirectAddressType|Optional|表示重定向地址类型。取值如下：IPV4_ADDRIPV6_ADDRURLSIP_URI
redirectServerAddress|Optional|表示重定向服务器地址。
###### FlowInformation 
FlowInformation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
flowDescription|Optional|流描述，包含IP流的数据包过滤器。
ethFlowDescription|Optional|定义以太网流的数据包过滤器。
packFiltId|Optional|表示包过滤器的标识。
packetFilterUsage|Optional|表明是否将分组包发送给用户。
tosTrafficClass|Optional|包含IPv4服务类型和掩码字段或IPv6 Traffic-Class字段和掩码字段。
spi|Optional|定义IPSec包的安全参数索引。
flowLabel|Optional|定义IPv6流标签头字段。
flowDirection|Optional|流方向，指示数据包过滤器适用的传输方向。取值如下：DOWNLINK：下行。UPLINK：上行。BIDIRECTIONAL：上下行（双向）。UNSPECIFIED：下行，但没有明确的指示方向。
###### SmPolicyDeleteData 
SmPolicyDeleteData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
userLocationInfo|Optional|表示用户当前的位置信息。
ueTimeZone|Optional|表示用户终端当前所在的时区。
servingNetwork|Optional|表示用户终端当前所在的服务网络。
AccuUsageReport|Optional|包含使用量报表。
###### QosCharacteristics 
QosCharacteristics的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
5qi|Mandatory|定义服务数据流的授权QoS参数的标识，适用于PCC规则和PDU会话级别。
resourceType|Mandatory|指示资源类型。取值如下：NON_GBRNON_CRITICAL_GBRCRITICAL_GBR
priorityLevel|Mandatory|5QI优先级，定义资源请求的优先级。
packetDelayBudget|Mandatory|表示包时延预算。单位：毫秒
packetErrorRate|Mandatory|表示包错误率。举例：包错误率10-6 应编码为“6”。包错误率10-2 应编码为“2”。
averagingWindow|Conditional|平均窗口，表示计算保证和最大比特率的持续时间，该属性仅在GBR QoS流中出现。单位：毫秒
maximumDataBurstVolume|Conditional|最大数据突发，表示在5G-AN PDB期间需要传输的最大数据量。当包时延预算小于等于20毫秒时，该属性存在。单位：Byte
###### ChargingInformation 
ChargingInformation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
primaryChfAddress|Mandatory|表示主要CHF地址。
secondaryChfAddress|Mandatory|表示辅助CHF地址。
###### AccuUsageReport 
AccuUsageReport的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
refUmIds|Mandatory|表示该使用量上报关联的UsageMonitoringData中的“umId”。
volUsage|Optional|表示累计使用总流量。
volUsageUplink|Optional|表示上行流量累计使用量。
volUsageDownlink|Optional|表示下行流量累计使用量。
timeUsage|Optional|表示累计的时间使用量。
nextVolUsage|Conditional|表示监控时间之后的累计总流量。
nextVolUsageUplink|Optional|表示监控时间后，上行流量的累计使用量。
nextVolUsageDownlink|Optional|表示监控时间后，下行流量的累计使用量。
nextTimeUsage|Conditional|表示监控时间之后累计的时间使用量。
###### SmPolicyUpdateContextData 
SmPolicyUpdateContextData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
repPolicyCtrlReqTriggers|Conditional|表示策略控制触发需要满足的触发器。如果没有满足的触发器，该属性不出现。取值如下：PLMN_CHRES_MO_REAC_TY_CHUE_IP_CHUE MAC_CHAN_CH_CORUS_REAPP_STAAPP_STOAN_INFOCM_SES_FAILPS_DA_OFFDEF_QOS_CHSE_AMBR_CHQOS_NOTIFNO_CREDITPRA_CHSAREA_CHSCNN_CHRE_TIMEOUTRES_RELEASESUCC_RES_ALLORAT_TY_CHREF_QOS_IND_CHHW_TETHERING_RESCELL_CHAN_CH_COR
accNetChIds|Optional|指示PCC规则或整个PDU会话的接入网络计费标识。
accessType|Optional|表示用户接入网络的类型。取值如下：3GPP_ACCESSNON_3GPP_ACCESS
ratType|Optional|表示用户终端使用的无线接入技术。取值如下：NRENUTRWLANVIRTUAL
servingNetwork|Optional|表示用户终端当前所在的服务网络。
userLocationInfo|Optional|表示用户当前的位置信息。
ueTimeZone|Optional|表示用户终端当前所在的时区。
ipv4Address|Optional|表示用户终端的IPv4地址。
relIpv4Address|Optional|表示已释放的用户终端的IPv4地址。
ipv6AddressPrefix|Optional|表示用户终端的IPv6地址前缀。
relIpv6AddressPrefix|Optional|表示多归属情况下，用户终端的IPv6地址前缀。
relUeMac|Optional|表示已释放的用户终端的MAC地址。
ueMac|Optional|表示用户终端的MAC地址。
subsSessAmbr|Optional|签约的会话AMBR。
subsDefQos|Optional|签约的默认QoS信息。
numOfPackFilter|Optional|包含信令QoS规则的受支持的数据包过滤器的数量。
accuUsageReports|Optional|累积使用量报表。
3gppPsDataOffStatus|Optional|标识3GPP PS数据关闭状态。取值如下：如果包含该属性并且取值为“true”，则表示UE激活3GPP PS数据关闭状态。如果包含该属性并且取值为“false”，则表示3GPP PS数据关闭状态被UE关闭。
AppDetectionInfo|Optional|如果适用，则上报应用流量的开始/停止和检测到的SDF描述。
RuleReport|Optional|用于上报PCC规则失败的原因。
qncReports|Optional|QoS通知控制信息。
userLocationInfoTime|Optional|表示用户最后一次检测到在指定位置的NTP时间。
repPraInfos|Optional|表示状态上报区域的变更。
ueInitResReq|Optional|表示UE请求为指定SDF进行特定QoS处理。
refQosIndication|Optional|标识用户是否支持反射QoS。取值如下：如果包含该属性并且取值为“true”，则表示支持反射QoS。如果包含该属性并且取值为“false”，则表示不支持反射QoS。
qosFlowUsage|Optional|默认QoS流的使用方法。取值如下：GENERAL：通用。IMS_SIG：IMS信令。
traceReq|Conditional|如需要激活、修改或去激活跟踪，应包含该属性。跟踪修改时，该属性的值应完全替换原有跟踪数据。跟踪去激活时，该属性的值应包含Null。
hwTetheringStatus|Conditional|标识用户Tethering状态。取值如下：START：用户Tethering业务开始。STOP：用户Tethering业务结束。
###### UpPathChgEvent 
UpPathChgEvent的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
notificationUri|Mandatory|表示接收事件通知的AF的通知地址。
notifCorreId|Mandatory|表示SMF发送的通知中携带的通知关联ID。
dnaiChgType|Mandatory|表示DNAI变更类型。取值如下：EARLYEARLY_LATELATE
###### TerminationNotification 
TerminationNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
resourceUri|Mandatory|表示通知有关的单个SM策略的资源URI。
cause|Mandatory|表示PCF请求终止策略关联的原因。取值如下：UNSPECIFIED ：未知原因。UE_SUBSCRIPTION：用户签约改变。INSUFFICIENT_RES：系统过载。
###### AppDetectionInfo 
AppDetectionInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
appId|Mandatory|表示对UPF上配置的应用程序检测过滤条件的引用。
instanceId|Optional|动态分配给SMF的标识符，在服务数据流描述可推断时，用于允许应用程序开始和停止事件与特定服务数据流描述关联。
sdfDescriptions|Optional|在服务数据流描述可推断时，包含服务数据流描述。
###### AccNetChId 
AccNetChId的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
accNetChaIdValue|Mandatory|包含计费标识。
refPccRuleIds|Optional|包含提供的接入网络计费标识符相关联的PCC规则的标识。
sessionChScope|Optional|当该属性取值为“true”时，表示接入网计费标识适用于整个PDU会话。
###### RequestedRuleData 
RequestedRuleData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
refPccRuleIds|Mandatory|一组PCC规则ID引用与控制数据相关联的PCC规则（PccRule中的“pccRuleId”）。
reqData|Mandatory|指示为相应的引用的PCC规则请求什么类型的规则数据。取值如下：CH_ID：表示请求的规则数据是计费标识。MS_TIME_ZONE：表示请求的接入网络信息类型是UE的时区。USER_LOC_INFO：表示请求的接入网络信息类型是UE的位置。RES_RELEASE：表示请求的规则数据是资源释放的结果。SUCC_RES_ALLO：表示请求的规则数据是成功的资源分配。
###### RequestedUsageData 
RequestedUsageData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
refUmIds|Conditional|一组使用量监控数据ID引用PCF请求使用量报告的使用情况监视数据实例（UsageMonitoringData中的“umId”）。仅当“allUmIds”属性取值不为“true”时此属性才存在。
allUmIds|Conditional|指示请求的使用量数据是否适用于所有使用情况监视数据实例。如果未包含此属性，则表示请求的使用量数据仅适用于“refUmIds”属性引用的使用情况监视数据实例。
###### RuleReport 
RuleReport的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
pccRuleIds|Mandatory|包含受影响的PCC规则的标识。
ruleStatus|Mandatory|表示PCC规则的状态。取值如下：ACTIVEINACTIVE
contVers|Conditional|表示PCC规则的版本。如果支持规则多版本特性，在安装或修改相应的PCC规则时应包含内容版本。
failureCode|Conditional|表示PCC规则上报原因。当SMF上报PCC规则的执行失败时，需要包含该属性。取值如下：UNK_RULE_IDRA_GR_ERRSER_ID_ERRNF_MALRES_LIMMAX_NR_QOS_FlowMISS_FLOW_INFORES_ALLO_FAILUNSUCC_QOS_VALINCOR_FLOW_INFOPS_TO_CS_HANAPP_ID_ERRNO_QOS_FLOW_BOUNDFILTER_RESMISS_REDI_SER_ADDRCM_END_USER_SER_DENIEDCM_CREDIT_CON_NOT_APPCM_AUTH_REJCM_USER_UNKCM_RAT_FAILEDSESS_AMBR_FAILUREDEF_QOS_FAILURE
finUnitAct|Optional|当用户账号无法覆盖服务费用时，表示相关过滤参数和重定向地址参数（如有）。
ranNasRelCauses|Optional|表示RAN或NAS释放原因码信息。
###### AuthorizedDefaultQos 
AuthorizedDefaultQos的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
5qi|Conditional|5G QoS标识，定义服务数据流的授权QoS参数的标识。“Authorized Default QoS”首次下发时包含该属性。
Arp|Conditional|表示QoS分配和保留优先级。“Authorized Default QoS”首次下发时包含该属性。
priorityLevel|Optional|表示QoS流中调度资源的优先级。
averWindow|Optional|平均窗口，表示计算保证和最大比特率的持续时间。该属性仅适用于GBR QoS流或延迟紧急GBR QoS流。单位：毫秒
maxDataBurstVol|Optional|最大数据突发量，表示在5G-AN PDB期间需要传输的最大数据量。该属性可用于延迟紧急GBR QoS流。单位：Byte
###### servNfId 
AVP定义：servNfId信元用于标识包含接入网关信息的AMF服务。 
应用场景：应用于动态策略控制业务时，在创建、更新或者更新通知响应消息如Npcf_SMPolicyControl_Create请求消息中，servNfId信元由SMF带给PCF。PCF把此信元的取值作为对象属性，参与条件计算控制策略下发。 
 说明： 
servNfId中的三类参数（servNfInstId/或Guami、anGwAddr、sgsnAddr）不会同时携带，每次只会携带其中一类。三类参数必须携带一类，未携带不返回错误码。 
属性的范围或取值不正确，不给SMF返回错误码。 
servNfId的数据结构参见下表：
属性名称|Presence requirement|描述
---|---|---
servNfInstId|Optional|用于标识AMF网元实例。
sgsnAddr|Optional|用于描述2/3G接入SGSN的IP地址（中国移动和中国联通定制参数，用于支持2/3G接入策略控制）。
Guami|Optional|全局唯一的AMF标识。
anGwAddr|Optional|用于描述ANGW的IP地址。当5G回落4G后， anGwAddr提供IP地址作为融合网络中ANGW的标识。
###### Guami 
Guami的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
PlmnId|Mandatory|PLMN ID。
AmfId|Mandatory|AMF ID。
###### PlmnId 
PlmnId的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Mcc|Mandatory|移动国家码。|移动国家码。
Mnc|Mandatory|移动网码。|移动网码。
###### AmfId 
AmfId的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
AmfId|Optional|标识由AMF区域ID（8位），AMF集ID（10位）和AMF指针（6位）组成的AMF ID的字符串。它被编码为6个十六进制字符的字符串（即24位）。
###### Mcc 
Mcc的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Mcc|Mandatory|PLMN的移动国家代码部分，包括3位数字。|PLMN的移动国家代码部分，包括3位数字。
###### Mnc 
Mnc的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
Mnc|Mandatory|PLMN的移动网络代码部分，包括2或3位数字。|PLMN的移动网络代码部分，包括2或3位数字。
###### AnGwAddress 
AnGwAddress的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
anGwIpv4Addr|Optional|标识anGW的IPv4地址。
anGwIpv6Addr|Optional|标识anGW的IPv6地址。
###### SmfId 
应用场景：应用于动态策略控制业务时，在创建响应消息如Npcf_SMPolicyControl_Create响应消息中，SmfId信元由SMF带给PCF。PCF把此信元的取值作为对象属性，参与条件计算控制规则下发。 
SmfId的数据结构参见下表：属性名称|Presence requirement|描述
---|---|---
smfId|Optional|用于标识SMF网元实例。
##### Npcf_AMPolicyControl 
[PolicyAssociation](52.html)
[PolicyAssociationRequest](53.html)
[PolicyAssociationUpdateRequest](54.html)
[PolicyUpdate](55.html)
[TerminationNotification](56.html)
###### PolicyAssociation 
PolicyAssociation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
request|Optional|NF服务消费者请求创建AM策略关联时提供的信息。
triggers|Optional|PCF订阅的请求触发器。取值如下：LOC_CHPRA_CH
servAreaRes|Optional|服务区限制，作为AMF接入和移动性策略部分内容，由PCF决定。
rfsp|Optional|RFSP索引，作为AMF接入和移动性策略部分内容，由PCF决定。
pras|Conditional|如果提供了触发器“PRA_CH”，则需设置请求上报的状态上报区域。
suppFeat|Mandatory|标识协商支持的特性列表。模式： '^[A-Fa-f0-9]*$'
###### PolicyAssociationRequest 
PolicyAssociationRequest的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
notificationUri|Mandatory|标识PCF发送的通知的接收方。
altNotifIpv4Addrs|Optional|用于发送通知的可选或备份IPv4地址。
altNotifIpv6Addrs|Optional|用于发送通知的可选或备份IPv6地址。
supi|Mandatory|表示用户永久标识。一般使用IMSI和NAI作为用户标识。模式：^(imsi-[0-9]{5,15}|nai-.+|.+)$
gpsi|Conditional|表示通用公共订阅标识。一般使用MSISDN和外部标识作为GPSI标识。模式：^(msisdn-[0-9]{5,15}|extid-.+@.+|.+)$
accessType|Conditional|表示用户接入网络的类型。取值如下：3GPP_ACCESSNON_3GPP_ACCESS
pei|Conditional|表示永久设备标识，即用户绑定的终端标识。模式：^(imei-[0-9]{15}|imeisv-[0-9]{16}|.+)$
userLoc|Conditional|表示用户当前的详细位置信息。
timeZone|Conditional|表示用户当前所在的时区。
servingPlmn|Conditional|表示用户当前所在的服务PLMN。
ratType|Conditional|表示用户终端使用的无线接入技术。取值如下：NREUTRAWLANVIRTUAL
groupIds|Conditional|表示用户的内部组标识列表。
servAreaRes|Conditional|服务区限制，作为AMF接入和移动性策略部分内容。
rfsp|Conditional|RFSP（RAT Frequency Selection Priority）索引，作为AMF接入和移动性策略部分内容。
guami|Conditional|全球唯一AMF标识（GUAMI）需服务消费者AMF提供。
serviceName|Optional|如果NF服务消费者是AMF，AMF需生成并提供服务名称。该服务使用Npcf_AMPolicyControl_UpdateNotify服务操作中接收到的信息。
suppFeat|Mandatory|表示服务消费者支持的特性列表。模式： '^[A-Fa-f0-9]*$'
traceReq|Conditional|如果需要激活跟踪，则应包括跟踪控制和配置参数信息。
###### PolicyAssociationUpdateRequest 
PolicyAssociationUpdateRequest的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
notificationUri|Optional|标识PCF发送的通知的接收方。
altNotifIpv4Addrs|Optional|用于发送通知的可选或备份IPv4地址。
altNotifIpv6Addrs|Optional|用于发送通知的可选或备份IPv6地址。
triggers|Conditional|NF服务消费者订阅的请求触发器。取值如下：LOC_CHPRA_CHSERV_AREA_CHRFSP_CH
servAreaRes|Conditional|服务区限制，作为AMF接入和移动性策略部分内容。存在触发器“SERV_AREA_CH”时，需提供该属性值。
rfsp|Conditional|RFSP（RAT/Frequency Selection Priority）索引，作为AMF接入和移动性策略部分内容。存在触发器“RFSP_CH”的触发器时，需提供该属性值。
praStatuses|Conditional|如果上报触发器“PRA_CH”，需提供UE发生跟踪小区状态变更的状态信息。
userLoc|Conditional|如果上报触发器“LOC_CH”，需提供用户的位置。
traceReq|Conditional|如需要激活、修改或去激活跟踪，应包含该属性。跟踪修改时，该属性的值应完全替换原有跟踪数据。跟踪去激活时，该属性的值应包含“Null”。
###### PolicyUpdate 
PolicyUpdate的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
resourceUri|Conditional|表示通知有关的单个AM策略的资源URI。当Npcf_AMPolicyControl_UpdateNotify服务操作中包含策略内容时，应包含该属性。
triggers|Optional|PCF订阅的请求触发器。取值如下：LOC_CHPRA_CH
servAreaRes|Optional|服务区限制，作为AMF接入和移动性策略部分内容，由PCF决定。
rfsp|Optional|RFSP（RAT/Frequency Selection Priority）索引，作为AMF接入和移动性策略部分内容，由PCF决定。
pras|Conditional|如果触发器“PRA_CH”存在或该触发器已经设置但请求的状态上报区域需变更，该属性定义请求上报的状态上报区域。
###### TerminationNotification 
TerminationNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
resourceUri|Mandatory|表示通知有关的单个AM策略的资源URI。
cause|Mandatory|表示PCF请求终止策略关联的原因。取值如下：UNSPECIFIED ：未知原因。UE_SUBSCRIPTION：用户签约改变。INSUFFICIENT_RES：系统过载。
##### Npcf_UEPolicyControl 
[PolicyAssociation](58.html)
[PolicyAssociationRequest](59.html)
[PolicyAssociationUpdateRequest](60.html)
[PolicyUpdate](61.html)
[TerminationNotification](62.html)
###### PolicyAssociation 
PolicyAssociation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
request|Optional|NF服务消费者在请求创建UE策略关联时提供的信息。
uePolicy|Optional|PCF决定的UE策略。
triggers|Optional|PCF订阅的请求触发器。取值如下：LOC_CHPRA_CH
pras|Conditional|如果提供了触发器“PRA_CH”，需设置请求上报的状态上报区域。
suppFeat|Mandatory|标识协商支持的特性列表。模式： '^[A-Fa-f0-9]*$'
###### PolicyAssociationRequest 
PolicyAssociationRequest的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
notificationUri|Mandatory|PCF发送通知的接收方标识。
altNotifIpv4Addrs|Optional|用于发送通知的交替或备用IPv4地址。
altNotifIpv6Addrs|Optional|用于发送通知的交替或备用IPv6地址。
supi|Conditional|表示用户永久标识。一般使用IMSI和NAI作为用户标识。模式：^(imsi-[0-9]{5,15}|nai-.+|.+)$
gpsi|Conditional|表示通用公共订阅标识。一般使用MSISDN和外部标识作为GPSI标识。模式：^(msisdn-[0-9]{5,15}|extid-.+@.+|.+)$
accessType|Conditional|表示用户接入网络的类型。取值如下：3GPP_ACCESSNON_3GPP_ACCESS
pei|Conditional|表示永久设备标识，即用户绑定的终端标识。模式：^(imei-[0-9]{15}|imeisv-[0-9]{16}|.+)$
userLoc|Conditional|表示用户当前的详细位置信息。
timeZone|Conditional|表示用户当前所在的时区。
servingPlmn|Conditional|表示用户当前所在的服务PLMN。
ratType|Conditional|表示用户终端使用的无线接入技术。取值如下：NREUTRAWLANVIRTUAL
groupIds|Conditional|表示用户的内部组标识列表。
hPcfId|Conditional|H-PCF标识。
uePolReq|Conditional|UE策略请求。当AMF接收到“UE STATE INDICATION”消息时，需提供UE策略请求。
guami|Conditional|全球唯一AMF标识（GUAMI）需服务消费者AMF提供。
serviceName|Optional|如果NF服务消费者是AMF，AMF需生成并提供服务名称。该服务使用Npcf_UEPolicyControl_UpdateNotify服务操作中接收到的信息。
suppFeat|Mandatory|表示服务消费者支持的特性列表。模式：^[A-Fa-f0-9]*$
###### PolicyAssociationUpdateRequest 
PolicyAssociationUpdateRequest的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
notificationUri|Optional|标识PCF发送的通知的接收方。
altNotifIpv4Addrs|Optional|用于发送通知的可选或备用IPv4地址。
altNotifIpv6Addrs|Optional|用于发送通知的可选或备用IPv6地址。
triggers|Conditional|NF服务消费者订阅的请求触发器。取值如下：LOC_CHPRA_CHUE_POLICY
praStatuses|Conditional|如果上报触发器“PRA_CH”，需提供UE发生跟踪小区状态变更的状态信息。
userLoc|Conditional|如果上报触发器“LOC_CH”，则需要提供用户的位置。
uePolDelResult|Conditional|UE策略下发结果。
###### PolicyUpdate 
PolicyUpdate的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
resourceUri|Conditional|通知有关的单个UE策略关联的资源URI。当Npcf_UEPolicyControl_UpdateNotify服务操作中包含策略内容时，应包含该属性。
uePolicy|Optional|表示PCF决定的UE策略。
triggers|Optional|PCF订阅的请求触发器。取值如下：LOC_CHPRA_CH
pras|Conditional|如果触发器“PRA_CH”存在或该触发器已经设置但请求的状态上报区域需变更，该属性定义请求上报的状态上报区域。
###### TerminationNotification 
TerminationNotification的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
resourceUri|Mandatory|表示通知有关的单个UE策略关联的资源URI。
cause|Mandatory|表示PCF请求终止策略关联的原因。取值如下：UNSPECIFIED ：未知原因。UE_SUBSCRIPTION：用户签约改变。INSUFFICIENT_RES：系统过载。
##### 通用数据类型 
[SubscribedDefaultQos](64.html)
[Snssai](65.html)
[UserLocation](66.html)
[RouteToLocation](67.html)
[RouteInformation](68.html)
[ServiceAreaRestriction](69.html)
[PresenceInfo](70.html)
[Arp](71.html)
[Ambr](72.html)
[TraceData](73.html)
###### SubscribedDefaultQos 
SubscribedDefaultQos的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
5qi|Mandatory|5G QoS标识，定义服务数据流的授权QoS参数的标识。
Arp|Mandatory|表示QoS分配和保留优先级。
priorityLevel|Optional|表示QoS流中调度资源的优先级。
###### Snssai 
Snssai的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
sst|Mandatory|标识S-NSSAI的切片/服务类型，表示期望的网络切片在特性和服务上的行为。
sd|Optional|标识S-NSSAI的切片/服务类型的多个分片，以区分同一个切片/服务类型的多个网络切片。模式： '^[A-Fa-f0-9]{6}$'
###### UserLocation 
 说明： 
UserLocation的数据结构当中至少存在1个eutraLocation、geraLocation、utraLocation、nrLocation或n3gaLocation。 
UserLocation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
eutraLocation|Conditional|表示E-UTRA用户位置。
nrLocation|Conditional|表示NR用户位置。
n3gaLocation|Conditional|表示非-3GPP接入用户位置。
geraLocation|Conditional|表示GERAN用户位置（中国移动2G接入N7接口定制参数）。
utraLocation|Conditional|表示UTRAN用户位置（中国联通3G接入N7接口定制参数）。
###### RouteToLocation 
RouteToLocation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
dnai|Mandatory|标识应用的位置。
routeInfo|Conditional|包括流量路由信息。说明：“routeInfo”属性或“routeProfId”属性应包含在“RouteToLocation”数据类型中。
routeProfId|Conditional|标识路由配置文件ID。说明：“routeInfo”属性或“routeProfId”属性应包含在“RouteToLocation”数据类型中。
###### RouteInformation 
RouteInformation的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
ipv4Addr|Conditional|数据网络中隧道端点的IPv4地址。说明：“ipv4Addr”属性或“ipv6Addr”属性应包含在“RouteInformation”数据类型中。
ipv6Addr|Conditional|数据网络中隧道端点的IPv6地址。说明：“ipv4Addr”属性或“ipv6Addr”属性应包含在“RouteInformation”数据类型中。
portNumber|Mandatory|数据网络中隧道端点的UDP端口号。
###### ServiceAreaRestriction 
ServiceAreaRestriction的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
restrictionType|Conditional|表示限制类型，当“areas”属性存在时该属性才会存在。取值如下：ALLOWED_AREASNOT_ALLOWED_AREAS
areas|Optional|表示区域列表：如果“restrictionType”属性取值为“ALLOWED_AREAS”，则表示允许的区域。如果“restrictionType”属性取值为“NOT_ALLOWED_AREAS”，则表示不允许的区域。说明：如果服务在所有区域被允许/限制，区域组为空。
maxNumOfTAs|Conditional|表示允许跟踪区域的最大个数。当“restrictionType”属性取值为“NOT_ALLOWED_AREAS”时，该属性不存在。
###### PresenceInfo 
PresenceInfo的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
praId|Conditional|表示指定区域的标识。如果订阅或上报的兴趣区域为状态上报区域，则该属性将出现。
trackingAreaList|Conditional|表示构成区域的跟踪区域列表。如果订阅或事件上报用于跟踪区域内的跟踪UE状态，则该属性应该存在。对于非3GPP接入，TAI应该是N3GPP的TAI
ecgiList|Conditional|表示构成区域的EUTRAN小区标识列表。如果订阅的兴趣区域是EUTRAN小区标识列表，则该属性将出现。
ncgiList|Conditional|表示构成区域的NR小区标识列表。如果订阅的兴趣区域是NR小区标识列表，则该属性将出现。
globalRanNodeIdList|Conditional|表示构成区域的NG RAN节点标识的列表。如果订阅的兴趣区域是NG RAN节点标识的列表，则该属性将出现。
###### Arp 
Arp的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
priorityLevel|Mandatory|定义资源请求的优先级。
preemptCap|Mandatory|定义ARP抢占能力开关，标示是否允许抢占他人使用的服务数据流资源。服务数据流是否可以获取已分配给具有较低优先级的另一个服务数据流的资源。取值如下：NOT_PREEMPTMAY_PREEMPT
preemptVuln|Mandatory|定义ARP被抢占开关， 标识是否允许自身的使用服务数据流资源被他人抢占。服务数据流是否可能丢失分配给它的资源，以便接纳具有更高优先级的服务数据流。取值如下：NOT_PREEMPTABLEPREEMPTABLE
###### Ambr 
Ambr的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
uplink|Mandatory|上行AMBR（Aggregate Maximum Bit Rate）。模式： '^\d+(\.\d+)? (bps|kbit/s|Mbps|Gbps|Tbps)$'举例：125 Mbps，0.125 Gbps，125000 kbit/s
downlink|Mandatory|下行AMBR。模式： '^\d+(\.\d+)? (bps|kbit/s|Mbps|Gbps|Tbps)$'举例：125 Mbps，0.125 Gbps，125000 kbit/s
###### TraceData 
TraceData的数据结构参见下表： 
属性名称|Presence requirement|描述
---|---|---
traceRef|Mandatory|跟踪参考。它应编码为MCC，MNC和Trace ID的串联，如下所示：<MCC> <MNC> - <Trace ID>模式：'^[0-9]{3}[0-9]{2,3}-[A-Fa-f0-9]{6}$'
traceDepth|Mandatory|跟踪深度。取值如下：MINIMUM：最低限度。MEDIUM：中等深度。MAXIMUM：最大限度。MINIMUM_WO_VENDOR_EXTENSION：没有供应商特定扩展的最低限度。MEDIUM_WO_VENDOR_EXTENSION：没有供应商特定扩展的中等深度。MAXIMUM_WO_VENDOR_EXTENSION：没有供应商特定扩展的最大限度。
neTypeList|Mandatory|NE类型列表。模式：'^[A-Fa-f0-9]+$'
eventList|Mandatory|触发事件。模式：'^[A-Fa-f0-9]+$'
collectionEntityIpv4Addr|Conditional|跟踪收集实体的IPv4地址。说明：“TraceData”数据结构中至少应存在“collectionEntityIpv4Addr”或“collectionEntityIpv6Addr”属性中的一个。
collectionEntityIpv6Addr|Conditional|跟踪收集实体的IPv6地址。说明：“TraceData”数据结构中至少应存在“collectionEntityIpv4Addr”或“collectionEntityIpv6Addr”属性中的一个。
interfaceList|Optional|接口列表。如果此属性不存在，则应跟踪适用于“neTypeList”属性中指示的NE类型列表的所有接口。模式：'^[A-Fa-f0-9]+$'
### Nbsf 
#### Nbsf接口协议简介 
场景描述 :Nbsf业务用于BSF提供PDU会话绑定功能，保证某个PDU会话的AF请求到达保持PDU会话信息的相关PCF。 
图1  Nbsf接口示意图
[]images/1.PNG)
协议栈 :图2  服务化接口协议栈
[]images/3.PNG)
Nbsf和其他所有服务化接口一样，都采用如上图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
#### 服务操作解释 
##### Nbsf_Management_Register 
服务操作|操作语义|服务操作的解释
---|---|---
Nbsf_Management_Register|Request/Response|NF服务消费者应调用Nbsf_Management_Register服务操作，在BSF中为UE注册会话绑定信息，NF服务消费者应发送带有“{apiRoot}/nbsf-management/v1/pcfBindings”的HTTP POST请求，作为表示“PCF会话绑定”的资源URI。注册成功，返回“201（ Created）”消息，包含一个位置HTTP头域，位置头域应包含已创建的绑定信息的URI，即“{apiRoot}/nbsf-management/v1/pcfBindings”/ {binding id}。
##### Nbsf_Management_Deregister 
服务操作|操作语义|服务操作的解释
---|---|---
Nbsf_Management_Deregister|Request/Response|该服务操作允许服务消费者去除BSF中UE的会话绑定信息。通过向标识特定NF实例的URI发出DELETE请求来调用该服务操作。NF服务消费者应调用Nbsf_Management_Deregister服务操作在BSF中注销UE的会话绑定信息。NF服务使用者应以“{apiRoot}/nbsf-management/v1/pcfBindingId}”作为资源URI发送HTTP删除请求，其中“{bindingId}”是要删除的“单独PCF会话绑定”资源标识符。返回消息。删除成功，返回204（No content），DELETE响应体为空。如果在BSF数据库中已注册NF实例列表中没有找到NF实例ID标识的NF实例，返回状态码404（Not Found），携带ProblemDetails信元提供详细错误信息。
##### Nbsf_Management_Discovery 
服务操作|操作语义|服务操作的解释
---|---|---
Nbsf_Management_Discovery|Request/Response|NF服务消费者应调用Nbsf_Management_Discovery服务操作获取所选择的PCF的地址信息，用于在BSF中的PDU会话中，NF服务消费者应发送以{apiRoot}/nbsf-management/v1/pcfBindings为资源URI的HTTP GET请求。查询参数包括UE地址，可能包括SUPI或GPSI、DNN和S-NSSAI（可选）、IPv4地址域。BSF回复包含相应PcfBinding数据结构的“200OK”HTTP响应。在响应消息体中Nbsf_Management_Register业务操作时PCF提供的，如果PCF会话绑定资源不存在，BSF应响应404未找到。如果请求URI中包含了无效的查询参数组合（i.e，没有UE地址的组合），则BSF应在ProblemDetails的IE中响应一个包含“INVALID_QUERY_PARAM”的“400 Bad Request”HTTP错误码，如果发现更多的PCF会话绑定资源，BSF应在ProblemDetails信元中响应“400 Bad Request”HTTP错误码，其中包含“MULTIPLE_BINDING_INFO_FOUND”。
##### Nbsf_Management_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Nbsf_Management_Update|Request/Response|NF服务消费者应调用Nbsf_Management_Update服务操作更新BSF中UE的会话绑定信息，NF服务消费者应发送HTTP补丁请求，其中“{apiRoot}/nbsf-management/v1/pcfBindings/{bindingId}”为资源URI。
#### 数据类型解释 
##### PcfBinding 
属性名称|描述
---|---
PcfBinding|注册一个新的PCF绑定信息。
注：3GPPTS 29.500 (6)的table5.2.7.1-1中列出的post方法的HTTP错误状态码，必须同时适用。|注：3GPPTS 29.500 (6)的table5.2.7.1-1中列出的post方法的HTTP错误状态码，必须同时适用。
##### ApiRoot 
服务操作|操作语义|服务操作的解释
---|---|---
ApiRoot|Request/Response|NF服务消费者向BSF发送的每个HTTP请求中使用的请求URI携带的信息。
##### Ipv4Addr 
属性名称|描述
---|---
Ipv4Addr|标识以“点分十进制”表示法格式化的IPv4地址的字符串。模式：'^（（[0-9] | [1-9] [0-9] | 1 [0-9] [0-9] | 2 [0-4] [0-9] | 25 [0 -5]）\）{3}（[0-9] |。[1-9] [0-9] | 1 [0-9] [0-9] | 2 [0-4] [0-9 ] | 25 [0-5]）$'
注1：查询参数ipv4Addr，ipv6Prefix或macAddr48中必须有一个和唯一的一个。注2：5G-的RG和FN-RG替换为有线接入支持的UE，参见3GPPTS23.316【19】。|注1：查询参数ipv4Addr，ipv6Prefix或macAddr48中必须有一个和唯一的一个。注2：5G-的RG和FN-RG替换为有线接入支持的UE，参见3GPPTS23.316【19】。
##### Ipv6Prefix 
属性名称|Presence requirement|描述
---|---|---
start|Mandatory|标识起始IPv6前缀。
end|Mandatory|标识结束IPv6。
##### MacAddr48 
属性名称|Presence requirement|描述
---|---|---
start|Mandatory|服务UE的MAC地址。
注：查询参数ipv4Addr，ipv6Prefix或macAddr48中必须有一个和唯一的一个。|注：查询参数ipv4Addr，ipv6Prefix或macAddr48中必须有一个和唯一的一个。|注：查询参数ipv4Addr，ipv6Prefix或macAddr48中必须有一个和唯一的一个。
##### Dnn 
属性名称|描述
---|---
Dnn|表示数据网络的字符串。它应格式化为字符串，其中标签用点分隔。DNN的组成：网络ID，表示一个外部网络，为必选部分。运营商ID，表示属于哪个运营商，为可选部分。
##### Supi 
属性名称|Presence requirement|描述
---|---|---
start|Optional|标识SUPI范围开始的第一个值，当SUPI的范围可以表示为数字范围（例如，IMSI范围）时使用。该字符串只包含数字。模式： "^[0-9]+$"
end|Optional|标识SUPI范围结束的最后一个值，当SUPI的范围可以表示为数字范围（例如，IMSI范围）时使用。该字符串只包含数字。模式： "^[0-9]+$"
pattern|Optional|表示SUPI集属于特定范围的表现模式 。如果SUPI字符串与正则表达式完全匹配，则SUPI值被视为范围的一部分。
为了与EPC通用，3GPP接入时使用IMSI，在Non-3GPP接入时使用NAI。IMSI的详细定义参见3GPP TS 23.003。IMSI由三部分组成：Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。Mobile Network Code (MNC)包含2个或3个数字。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。|为了与EPC通用，3GPP接入时使用IMSI，在Non-3GPP接入时使用NAI。IMSI的详细定义参见3GPP TS 23.003。IMSI由三部分组成：Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。Mobile Network Code (MNC)包含2个或3个数字。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。|为了与EPC通用，3GPP接入时使用IMSI，在Non-3GPP接入时使用NAI。IMSI的详细定义参见3GPP TS 23.003。IMSI由三部分组成：Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。Mobile Network Code (MNC)包含2个或3个数字。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。
##### Gpsi 
属性名称|描述
---|---
Gpsi|通用公共订阅标识。GPSI作为SUPI的签约数据，将外部网络标识GPSI与3GPP网络的标识SUPI建立关系。|通用公共订阅标识。GPSI作为SUPI的签约数据，将外部网络标识GPSI与3GPP网络的标识SUPI建立关系。
##### Snssai 
属性名称|Presence requirement|描述
---|---|---
sst|Mandatory|标识S-NSSAI的切片/服务类型，表示期望的网络切片在特性和服务上的行为。
sd|Optional|标识S-NSSAI的切片/服务类型的多个分片，以区分同一个切片/服务类型的多个网络切片。模式： '^[A-Fa-f0-9]{6}$'
注：查询参数snssai和/或IPDOMAIN，如果适用（IPv4地址重叠），则需要查询参数ipv4Addr。|注：查询参数snssai和/或IPDOMAIN，如果适用（IPv4地址重叠），则需要查询参数ipv4Addr。|注：查询参数snssai和/或IPDOMAIN，如果适用（IPv4地址重叠），则需要查询参数ipv4Addr。
##### IpDomain 
属性名称|Presence requirement|描述
---|---|---
IpDomain|Mandatory|标识IPv4地址域符。
注：查询参数snssai和/或IPDOMAIN，如果适用（IPv4地址重叠），则需要查询参数ipv4Addr。|注：查询参数snssai和/或IPDOMAIN，如果适用（IPv4地址重叠），则需要查询参数ipv4Addr。|注：查询参数snssai和/或IPDOMAIN，如果适用（IPv4地址重叠），则需要查询参数ipv4Addr。
##### ProblemDetails 
属性名称|Presence requirement|描述
---|---|---
ProblemDetails|Mandatory|存在多个绑定信息。
##### PcfBindingPatch 
属性名称|Presence requirement|描述
---|---|---
PcfBindingPatch|Mandatory|返回与查询参数(s)匹配的单个PCF会话绑定信息资源。
##### SupportedFeatures 
属性名称|描述
---|---
SupportedFeatures|用于指示API支持的功能的字符串。
##### IpEndPoint 
属性名称|Presence requirement|描述
---|---|---
Ipv4Addr|Conditional|表示IPv4地址（注1）
port|Optional|表示端口号（注2）
注1：数据结构最多只能包含一个ipv4Address或ipv6Address。注2：如果ipendpoint属性未携带端口号，则NF服务消费者在调用服务时，使用默认的HTTP端口号，如TCP端口80访问HTTP URI，或使用TCP端口443访问HTTPS URI。|注1：数据结构最多只能包含一个ipv4Address或ipv6Address。注2：如果ipendpoint属性未携带端口号，则NF服务消费者在调用服务时，使用默认的HTTP端口号，如TCP端口80访问HTTP URI，或使用TCP端口443访问HTTPS URI。|注1：数据结构最多只能包含一个ipv4Address或ipv6Address。注2：如果ipendpoint属性未携带端口号，则NF服务消费者在调用服务时，使用默认的HTTP端口号，如TCP端口80访问HTTP URI，或使用TCP端口443访问HTTPS URI。
##### NfInstanceId 
属性名称|描述
---|---
NfInstanceId|唯一标识NF实例的字符串。 NF实例ID的格式应为通用唯一标识符（UUID）版本4。
##### DateTime 
属性名称|描述
---|---
DateTime|具有OpenAPI规范[3]中定义的格式“日期时间”的字符串
##### DiameterIdentity 
属性名称|描述
---|---
DiameterIdentity|包含Diameter标识的字符串。模式：'^（[A-Za-z0-9] +（ - [A-Za-z0-9] +）.）+ [a-z] {2，} $'
### Nchf 
#### Nchf接口协议简介 
场景描述 :Nchf是CHF为其他NF提供服务的接口。 
图1  Nchf接口示意图
[]images/1.PNG)
协议栈 :Nchf和其他所有服务化接口一样，都采用如下图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。 
图2  服务化接口协议栈
[]images/3.PNG)
##### 网络功能服务列表 
CHF通过Nchf接口向其他NF提供多种服务（NFS，Network Function Service），具体服务包括下表所定义的各种。 
NF|NFS|NFS的解释
---|---|---
CHF|Nchf_ConvergedCharging service|为会话类和事件类NF业务提供融合计费，包括配额管理和无配额管理，生成计费信息记录。
Nchf_SpendingLimitControl|CHF|该服务使PCF通过订阅消费额度上限报告，例如策略指标状态变化通知，从CHF获取每个UE的策略指标状态信息。
#### 服务操作解释 
每个NF可以提供多个服务，每个服务中定义了多个服务操作（Service Operation），NF的同一种Service Operation可以通过服务化接口被其他多个NF调用，实现特定功能。Nchf接口上提供的各服务以及各服务支持的服务操作参见下表。 
服务名称|服务操作|服务操作的解释
---|---|---
Nchf_ConvergedCharging service|Create|首次查询业务单元预留/首次报告用量。
Update|Nchf_ConvergedCharging service|在以下事件发生时，中途请求查询剩余业务单元预留情况：一个计费组的授权业务单元已经用完。授权业务单元到期。产生业务事件，可能影响当前业务的计费。中途业务单元使用情况。
Release|Nchf_ConvergedCharging service|计费会话结束。
Notify|Nchf_ConvergedCharging service|请求重新授权用户或终止计费会话上下文。
##### Nchf_ConvergedCharging_Create 
服务操作|操作语义|服务操作的解释
---|---|---
Nchf_ConvergedCharging_Create|Request/Response|Nchf_ConvergedCharging_Create服务为NF（CTF）向CHF请求提供配额或首次报告业务使用量使用。此时对应会话尚无计费数据资源。CTF调用CHF的Nchf_ConvergedCharging_Create服务化接口请求创建计费资源，请求体中包含请求配额和Nchf_ConvergedCharging_Notify通知服务的URI。当操作成功时，CHF返回“201 Created”响应，包含位置头字段及分配的配额。位置头字段包含了创建的计费资源的URI，NF（CTF）在后续给CHF的同一PDU会话请求中必须带该URI信息。当操作失败或重定向时，需要返回对应状态的HTTP响应码。对于状态码为4XX或5XX的响应，消息体必须包含一个带‘clause’属性的ProblemDetails结构，‘clause’属性返回具体的应用错误代码。
##### Nchf_ConvergedCharging_Update 
服务操作|操作语义|服务操作的解释
---|---|---
Nchf_ConvergedCharging_Update|Request/Response|Nchf_ConvergedCharging_Update服务为NF（CTF）向CHF更新计费数据时调用。更新过程可能发生在以下场景：费率组服务单元耗尽。授权服务单元到期。发生可能影响当前服务的计费事件。收到CHF的重授权通知。CTF向CHF发送Nchf_ConvergedCharging_Update消息，表示需要更新的计费数据标识的“ChargingDataRef”包含在请求消息体的URI中，同时，请求的服务单元和已经使用的服务单元也包含在请求消息体中。当操作成功时，返回“200 ok”响应消息。消息体中包含授权的业务单元。当操作失败或重定向时，需要返回对应状态的HTTP响应码。对于状态码为4XX或5XX的响应，消息体必须包含ProblemDetails结构。
##### Nchf_ConvergedCharging_Release 
服务操作|操作语义|服务操作的解释
---|---|---
Nchf_ConvergedCharging_Release|Request/Response|Nchf_ConvergedCharging_Release服务为NF（CTF）准备终止计费会话时调用。释放过程可能发生在以下场景：业务单元不活动定时器超时。从CHF收到计费中止通知。NF（CTF）向CHF发送Nchf_ConvergedCharging_Release请求，表示需要释放的计费数据标识的“ChargingDataRef”包含在请求消息体的URI中，请求体中包含最终使用的服务单元。当操作成功时，CHF返回“204 No Content”响应。当操作失败或重定向时，需要返回对应状态的HTTP响应码。对于状态码为4XX或5XX的响应，消息体必须包含ProblemDetails结构。
##### Nchf_ConvergedCharging_Notify 
服务操作|操作语义|服务操作的解释
---|---|---
Nchf_ConvergedCharging_Notify|Subscribe/Notify|Nchf_ConvergedCharging_Notify服务在CHF通知NF（CTF）更新或终止PDU Session计费时调用。通知流程可能发生在以下场景：CHF决定重授权。CHF决定终止计费。CHF向NF（CTF）发送Nchf_ConvergedCharging_Notify计费通知请求。{notifyUri}标识Nchf_ConvergedCharging_Create请求中的通知URI。通知类型包含在请求消息体中。当操作成功时，CHF返回“204 No Content”响应。当操作失败时，需要返回对应状态的HTTP响应码。对于状态码为4XX或5XX的响应，消息体必须包含ProblemDetails结构。
#### 数据类型解释 
##### Nchf_ConvergedCharging 
 说明： 
信元解释中消息参数的类别解释如下： 
OM（Operator Provisionable：Mandatory），运营商定义的必选项，当运营商要求该字段后，该字段必须始终在话单中出现。 
OC（Operator Provisionable：Conditional），运营商定义的条件可选项，当运营商要求该字段后，且当特定条件满足时，该字段必须在话单中出现。 
###### ChargingDataRequest 
ChargingDataRequest的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
SubscriberIdentifier|OM|该字段标识使用请求服务的用户。
nfConsumerIdentification|必选|该字段标识一个分组字段，用来标识调用计费服务的NF的信息。
invocationTimeStamp|必选|该字段标识请求发送时间。
invocationSequenceNumber|必选|该字段标识请求的序列号。
notifyUri|OC|该字段标识接收CHF的notify消息的SMF的URI地址。会话计费中携带，该信息应出现在创建请求消息中，也可能出现在更新消息中。
MultipleUnitUsage|OC|该字段包含配额管理请求的相关参数以及/或者用量报告。
Trigger|OC|请求触发条件。
PDUSessionChargingInformation|OM|该字段保存5G数据连接特定信息。
###### ChargingDataResponse 
ChargingDataResponse的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
invocationTimestamp|必选|该字段保存CHF响应计费服务的时间戳。
InvocationResult|OC|调用结果，该字段保存返回给SMF的结果码。
invocationSequenceNumber|必选|该字段保存SMF调用计费服务的序号。
sessionFailover|OC|该字段提示是否支持备选CHF，以支持NF使用者对在用计费服务的故障接管处理。取值如下：FAILOVER_NOT_SUPPORTEDNchf_ConvergedCharging消息在通信失败时无法再备选CHF处理。如果响应中没有携带该属性，默认使用本值。FAILOVER_SUPPORTEDNchf_ConvergedCharging消息在通信失败时发送给备选CHF处理。
MultipleUnitInformation|OC|该字段保存用于配额管理和/或使用量报告信息的参数。可以有多个该属性。
Trigger|OC|该字段标识CHF提供的计费事件，以覆盖/激活NF消费者中已有的计费事件。CHF通过不带triggerType的trigger关闭除RG级triggers外的所有triggers。
PDUSessionChargingInformation|OM|该字段保存5G数据连接特定信息。
###### ChargingNotifyRequest 
ChargingNotifyRequest的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
notificationType|必选|该字段指示重授权或终止会话计费的通知类型。取值如下：REAUTHORIZATION：表示重授权。ABORT_CHARGING：表示终止PDU会话计费。
ReauthorizationDetails|OC|该字段重授权描述符，标识更新的配额或用量报告。
###### NFIdentification 
NFIdentification的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
nodeFunctionality|必选|该字段包含节点功能。取值如下：SMF标识NF为SMF。AMF标识NF为AMF。SMSF标识NF服务消费者为SMSF。
nFName|OC|该字段标识NF实例标识。nFName、nFIPv4Address或nFIPv6Address中，至少携带一个参数。
nFIPv4Address|OC|该字段标识NF的IPv4地址。nFName、nFIPv4Address或nFIPv6Address中，至少携带一个参数。
nFIPv6Address|OC|该字段标识NF的IPv6地址。nFName、nFIPv4Address或nFIPv6Address中，至少携带一个参数。
nFFqdn|OC|该字段标识NF的FQDN。
nFPLMNID|OC|该字段标识NF所属网络的PLMN ID。
###### MultipleUnitUsage 
MultipleUnitUsage的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
ratingGroup|必选|该字段标识一个费率组。
RequestedUnit|OC|如果包含，该字段指示需要进行配额管理。是个可选字段，还指示请求的某一特定类别的业务单元的数量。
UsedUnitContainer|OC|该字段指示容器，包含流量、时间戳等。
uPFID|OC|该字段标识一个UPF。为MultipleUnitUsage类型的5G数据连接计费的附加属性。
###### InvocationResult 
InvocationResult的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
error|OC|如果SMF调用计费服务失败，应在“ProblemDetails”结构的“cause”属性中提供详细的错误信息。
failureHandling|OC|该字段保存SMF在计费服务调用请求被临时阻止时执行的动作。该字段的值应始终覆盖已有的任何值。指示故障时，SMF要执行的操作。如果计费服务调用成功，该字段指示SMF要执行哪个动作来防止后续计费服务调用请求被阻止。取值如下：TERMINATE停止服务。CONTINUE如果传输临时故障，SMF应该重新发送请求或继续发送请求到备选服务器，前提是CHF和NF消费者支持故障转移，并且备选服务器可用。否则，即使计费数据请求无法下发，业务也应该被授权。RETRY_AND_TERMINATE如果传输临时故障，NF消费者应该重新将请求发送到备选服务器，前提是CHF和NF消费者支持故障转移，并且有可用的备选服务器。否则，当计费数据请求无法下发时，业务不应该被授权。
###### Trigger 
Trigger的数据结构参见下表： 
属性名称|可选必选说明|描述
---|---|---
triggerType|OC|该参数标识计费条件。取值如下：QUOTA_THRESHOLD达到配额阈值。QHT已到达先前响应中携带的配额保持时间（即该配额在一定时间段内未使用）。FINAL业务终止。QUOTA_EXHAUSTED配额耗尽。FORCED_REAUTHORISATION服务器发起重新授权过程，即接收通知服务操作。UNIT_COUNT_INACTIVITY_TIMER单位计数不活动定时器超时。ABNORMAL_RELEASEPDU会话异常释放。QOS_CHANGE在请求消息中，此值用于指示发生了QoS改变。在响应消息中，此值用于指示最终用户协商的QoS的更改将导致服务消费者请求重新授权关联的配额。VOLUME_LIMIT达到流量阈值。TIME_LIMIT达到时间阈值。EVENT_LIMIT达到事件阈值。PLMN_CHANGEPLMN发生变化。USER_LOCATION_CHANGE在请求消息中，此值用于指示用户位置已更改。在响应消息中，此值用于指示最终用户位置更改导致服务消费者请求重新授权相关配额。RAT_CHANGE在请求消息中，此值用于指示RAT类型已经改变。在响应消息中，此值用于指示RAT更改导致服务消费者请求重新授权相关配额。UE_TIMEZONE_CHANGE在请求消息中，此值用于指示UE时区已更改。在响应消息中，此值用于指示用户所在时区更改导致服务消费者请求重新授权相关配额。TARIFF_TIME_CHANGE费率发生变更。MAX_NUMBER_OF_CHANGES_IN CHARGING_CONDITIONS变更次数已达上限。MANAGEMENT_INTERVENTION管理干预。CHANGE_OF_3GPP_PS_DATA_OFF_STATUS在请求消息中，此值用于指示分组域数据状态改变。在响应消息中，此值用于指示分组域数据状态改变导致服务消费者请求重新授权相关配额。SERVING_NODE_CHANGENF Consumer中的服务节点（例如，AMF）变更。REMOVAL_OF_UPF删除UPF。ADDITION_OF_UPF新增UPF。INSERTION_OF_ISMF插入I-SMF。REMOVAL_OF_ISMF删除I-SMF。CHANGE_OF_ISMF删除使用的I-SMF，插入新的I-SMF。START_OF_SERVICE_DATA_FLOW产生业务数据流。
category|必选|该字段指示SMF是否立即上报CHF计费事件，上报对应trigger生成的计费数据。取值如下：IMMEDIATE_REPORT当计费事件发生时，SMF收集当前计费事件对应计费数据，立即向CHF上报。DEFERRED_REPORT当计费事件发生时，SMF收集当前计费事件对应计费数据，暂时不向CHF上报。
timeLimit|OC|该字段表示当trigger type为“Expiry of data time limit”时的时间阈值。
volumeLimit|OC|该字段表示当trigger type为"Expiry of data volume limit"时设置的流量阈值。从Nchf_ConvergedCharging API version v2.0.0版本开始，该属性不再使用。
volumeLimit64|OC|该字段表述当trigger type为"Expiry of data volume limit"时设置的流量阈值。该属性从Nchf_ ConvergedCharging API v2.0.0版本开始替换之前版本中的volumeLimit属性。
maxNumberOfccc|OC|该字段表示当trigger type为"Max nb of number of charging condition changes"时设置的计费条件改变最大次数阈值。
###### MultipleUnitInformation 
MultipleUnitInformation的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
resultCode|OC|本字段包含计费组配额分配结果。取值如下：SUCCESSCHF将计费组配额分配给终端用户。END_USER_SERVICE_DENIEDCHF由于用户服务限制或相关限制，拒绝服务请求。如果请求中包含已使用计费组配额，则应扣减。QUOTA_MANAGEMENT_NOT_APPLICABLECHF判断无需配额管理即可给用户分配业务单元，但要求上报用量。QUOTA_LIMIT_REACHEDCHF拒绝服务请求，因为最终用户的帐户不足支付请求服务。如果请求中包含已使用计费组配额，则应扣减。END_USER_SERVICE_REJECTEDCHF拒绝服务请求，终止需要申请信用额度的服务。RATING_FAILEDCHF判断批价输入不足、参数组合错误、参数识别失败、参数值错误等，导致批价失败。
ratingGroup|必选|该字段标识一个费率组。
GrantedUnit|OC|该参数表示授权配额。
triggers|OC|该字段保存与计费组关联的业务单元使用情况上报的trigger。若triggers属性不携带triggerType，则CHF禁用所有与该计费组关联的trigger。
validityTime|OC|该字段限制某既定类别实例的授权配额的有效性。
quotaHoldingTime|OC|该字段限制配额保持时间，单位：秒。该字段同样限制时间配额和流量配额。当观察不到与配额相关的流量时，NF消费者认为该配额已过期。quotaHoldingTime值为0表示不使用这种机制，如果quotaHoldingTime属性不存在，则使用NF消费者本地配置的默认值。
finalUnitIndication|OC|该字段表示当前为最后一次下发业务单元给服务。
timeQuotaThreshold|OC|该字段表示授权的时间配额的阈值，单位为秒。
volumeQuotaThreshold|OC|该字段表示授权的流量配额的阈值，单位为字节。
uPFID|OC|该字段表示UPF标识。为MultipleUnitUsage类型的5G数据连接计费的附加属性。
###### RequestedUnit 
RequestedUnit的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
time|OC|该字段指示请求的时间量。
totalVolume|OC|该字段指示请求的上下行总流量。
uplinkVolume|OC|该字段指示请求的上行流量。
downlinkVolume|OC|该字段指示请求的下行流量。
注：如果该字段未定义任何值，则由CHF确定请求的配额类别和数量。|注：如果该字段未定义任何值，则由CHF确定请求的配额类别和数量。|注：如果该字段未定义任何值，则由CHF确定请求的配额类别和数量。
###### UsedUnitContainer 
UsedUnitContainer的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
serviceId|OC|该字段标识一个服务。
quotaManagementIndicator|OC|该字段指示上报的RG业务是否有配额管理控制。如果不携带该字段，表示已使用的业务单元没有配额管理。取值如下：ONLINE_CHARGING要求配额管理。OFFLINE_CHARGING无配额管理控制。
triggers|OC|该字段指示触发条件。
triggerTimestamp|OC|该字段指示触发上报的时间戳。
time|OC|该字段指示已使用时间。
totalVolume|OC|该字段指示已使用的上下行流量总和。
uplinkVolume|OC|该字段指示已使用的上行流量。
downlinkVolume|OC|该字段指示已使用的下行流量。
eventTimeStamps|OC|如果上报的业务单元是基于事件计费，则该字段指示上报业务单元中事件发生的时间戳。
localSequenceNumber|必选|该字段指示已使用的业务单元的序号，即，计费事件发生的顺序，从1开始，每用完一个业务单元，该值加1。
pDUContainerInformation|OC|该字段指示5G数据连接特定信息。
###### GrantedUnit 
GrantedUnit的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
tariffTimeChange|OC|该字段指示费率切换的时间点。
time|OC|该字段指示授权的时间量。
totalVolume|OC|该字段指示授权的上下行总流量。
uplinkVolume|OC|该字段指示授权的上行流量。
downlinkVolume|OC|该字段指示授权的下行流量。
###### FinalUnitIndication 
FinalUnitIndication的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
finalUnitAction|必选|该字段指示当用户的帐户不足以支付服务费用时，服务消费者应采取的行动。取值如下：TERMINATE服务消费者应终止服务会话。REDIRECT服务消费者应该将用户重定向到redirectServerAddress属性中指定的地址。RESTRICT_ACCESS服务消费者应根据restrictionFilterRule属性中定义的IP包过滤器或根据filterId属性标识的IP包过滤器限制用户访问。
restrictionFilterRule|OC|该字段指示即使没有授权的业务单元，仍可访问的服务的过滤规则。
filterId|OC|该字段指示即使没有授权的业务单元，仍可访问的服务的IP包过滤规则。
RedirectServer|OC|该字段指示当用户帐户不足以支付服务费用时，该用户连接到的重定向服务器的地址信息。
###### RedirectServer 
RedirectServer的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
redirectAddressType|必选|该字段指示重定向服务器的地址类型。取值如下：IPV4重定向服务器地址为IPV4。IPV6重定向服务器地址为IPV6。URL重定向服务器地址为URL。
redirectServerAddress|必选|该字段表示重定向服务器地址。
###### ReauthorizationDetails 
ReauthorizationDetails的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
service|OC|该字段标识一个服务。
ratingGroup|OC|该字段标识一个计费组。如果设置了serviceIdentifier属性，则此属性也必须设置。
quotaManagementIndicator|OC|该字段指示重授权通知是否用于配额管理控制。取值如下：ONLINE_CHARGING要求配额管理控制。OFFLINE_CHARGING无配额管理控制。
###### SubscriberIdentifier 
SubscriberIdentifier的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
subscriberIdentityType|必选|该字段指示用户标识类型。
supi|OC|该字段指示SUPI（用户类型为supi）。
###### PDUSessionChargingInformation 
PDUSessionChargingInformation的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
chargingId|OC|该字段指示携带唯一的计费标识。
UserInformation|OM|该字段包括用户及用户设备的信息。
userLocationinfo|OC|该字段指示用户位置信息。
userLocationTime|OC|该字段指示最后一次探测到UE位置的时间。
uetimeZone|OC|该字段指示UE当前所在时区。
PDUSessionChargingInformation|必选|该字段指示PDU会话级别信息，包括PDU会话ID、PDU类型、SSC模式、QoS、网络切片等。
unitCountInactivityTimer|OC|该字段指示资源空闲时间阈值。在SMF与CHF进行初始交互时，SMF通过该属性向CHF提供预配置的阈值。响应消息携带该字段，表示CHF在响应初始请求时携带的阈值并且覆盖SMF中原有的阈值。只有当业务计数不活动计时器处于激活状态时，才显示此字段。
RANSecondaryRATUsageReport|OC|该字段指示无线侧上报的Secondary RAT usage的值。
###### UserInformation 
UserInformation的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
servedGPSI|OC|如果携带，该字段指示被服务方的一般公共订阅标识符（GPSI）。
servedPEI|OC|该字段指示永久设备标识（PEI）。
unauthenticatedFlag|OC|该字段表示使用的SUPI未认证。
roamerInOut|OC|该字段表示漫游用户。
###### PDUSessionInformation 
PDUSessionInformation的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
NetworkSlicingInfo|OM|该字段指示PDU会话对应的网络切片的信息。
pduSessionID|必选|该字段标识一个PDU会话。
pduType|OM|该字段指示PDU会话类型。
sscMode|OC|该字段指示SSC Mode类型。
hPlmnId|OC|该字段为归属网络PLMN标识。
ServingNetworkFunctionID|OC|该字段标识服务网络功能。
servingCNPlmnId|OC|该字段为UE在共享网络中选择的服务方网络运营商的PLMN ID。
ratType|OC|该字段指示PDU会话的RAT类型。
dnnId|必选|该字段指示一个数据网络名称（DNN）。
chargingCharacteristics|OC|该字段指示PDU会话的计费属性。
chargingCharacteristicsSelectionMode|OC|该字段指示计费属性选择相关信息。取值如下：HOME_DEFAULT用户和SMF属于同一个PLMN。ROAMING_DEFAULT用户归属同一PLMN，AMF归属另一PLMN。VISITING_DEFAULT用户归属不同PLMN。
startTime|OC|该字段指示SMF上PDU会话开始的时间，格式为UTC。
stopTime|OC|该字段指示SMF上PDU会话结束的时间，格式为UTC。
3gppPSDataOffStatus|OC|该字段指示终端的3GPP Data Off状态为激活还是去激活。取值如下：ACTIVE3GPP Data Off状态为激活。INACTIVE3GPP Data Off状态为去激活。
sessionStopIndicator|OC|该字段向CHF指示PDU会话已经终止。
PDUAddress|OC|该字段指示用户IP地址/前缀组。
diagnostics|OC|该字段指示SMF下发的原因值。
authorizedQoSInformation|OC|该字段指示PDU会话使用的授权的QoS。
subscribedQoSInformation|OC|该字段指示签约的Default QoS。
authorizedSessionAMBR|OC|该字段指示授权的Session-AMBR。
subscribedSessionAMBR|OC|该字段指示签约的Session-AMBR。
###### PDUContainerInformation 
PDUContainerInformation的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
timeofFirstUsage|OC|该字段指示第一个业务包的时间戳。
timeofLastUsage|OC|该字段指示最后一个业务包的时间戳。
qoSInformation|OC|该字段指示为上报使用单元申请的QoS。
aFCorrelationInformation|OC|该字段指示AF提供的标识符，将该PCC规则中的计费密钥/服务标识符值的测量与应用级别报告相关联。
userLocationInformation|OC|该字段指示用户位置信息。
uetimeZone|OC|该字段指示终端所在时区。
rATType|OC|该字段指示已使用业务单元的RAT类型。
servingNodeID|OC|该参数标识服务节点。
3gppPSDataOffStatus|OC|该字段指示3GPP Data off的状态。取值如下：ACTIVE3GPP Data Off状态为激活。INACTIVE3GPP Data Off状态为去激活。
chargingRuleBaseName|OC|该字段标识SMF上预定义的一组PCC规则。
###### NetworkSlicingInfo 
NetworkSlicingInfo的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
sNSSAI|必选|该字段表示单网络切片选择支撑信息。
###### PDUAddress 
PDUAddress的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
pduIPv4Address|OC|该字段指示为PDU会话分配的SUPI的IPv4地址。
pduIPv6AddresswithPrefix|OC|该字段指示为PDU会话分配的SUPI的IPv6地址（带前缀）。
pduAddressprefixlength|OC|该字段指示PDU会话的IPv6前缀长度。前缀长度为64位时，不需要该字段。
iPv4dynamicAddressFlag|OC|该字段标识是否动态分配IPv4地址。如果分配静态地址，则不显示此字段。
iPv6dynamicPrefixFlag|OC|该字段标识是否动态分配IPv6地址。如果分配静态地址，则不显示此字段。
###### ServingNetworkFunctionID 
ServingNetworkFunctionID的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
servingNetwork FunctionInformation|必选|该字段指示服务网络功能，比如，AMF、I-SMF、SGW或V-SMF。
aMFId|OC|该字段标识一个AMF。
###### RoamingQBCInformation 
RoamingQBCInformation的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
MultipleQFIcontainer|OC|该字段指示QFI容器列表。
uPFID|OC|该字段标识一个UPF。
roamingChargingProfile|OC|该字段为漫游QBC场景PDU会话关联的漫游计费模板。
###### MultipleQFIcontainer 
MultipleQFIcontainer的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
triggers|OC|该字段指示触发关闭QFI容器的条件。
triggerTimestamp|OC|该字段指示触发上报事件的时间戳。
time|OC|该字段指示时间量。
totalVolume|OC|该字段指示上下行流量总和。
uplinkVolume|OC|该字段指示上行流量。
downlinkVolume|OC|该字段指示下行流量。
localSequenceNumber|必选|该字段指示QFI容器序号，从1开始，每生成1个容器序号加1。
qFIContainerInformation|OC|该字段指示QFI容器信息。
###### RANSecondaryRATUsageReport 
RANSecondaryRATUsageReport的数据结构参见下表。 
属性名称|可选必选说明|描述
---|---|---
rANSecondaryRATType|OM|该参数表示secondary RAT上报用量关联的RAT类型。取值如下：NREUTRA
qosFlowsUsage Reports|OM|该参数表示每个QFI的容器清单，包含上报用量。
### Nsmsf 
#### Nsmsf接口协议简介 
场景描述 :Nsmsf是SMSF为其他NF提供服务的接口。 
图1  Nsmsf接口示意图
[]images/1.PNG)
协议栈 :Nsmsf和其他所有服务化接口一样，都采用如下图所示的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。 
图2  服务化接口协议栈
[]images/3.PNG)
##### 网络功能服务列表/NFS List 
NF|NFS|NFS的解释
---|---|---
SMSF|Nsmsf_SMService|Nsmsf_SMService服务为NF服务消费者（例如AMF）提供授权SMS和激活SMSF上的SMS的服务能力。以下是本NFS的关键功能：为用户激活或去激活SMS服务，这会导致在SMSF中创建/更新/删除SMS的UE上下文。向SMSF发送上行方向的SMS有效载荷。
#### 服务操作解释 
NFS|服务操作|服务操作的解释
---|---|---
Nsmsf_SMService|Activate|用于短消息激活流程。UE发起短消息业务激活时，在SMSF上创建或者更新SMS业务的UE上下文信息。
Deactivate|Nsmsf_SMService|用于短消息去激活流程。UE发起短消息业务去激活时，在SMSF上删除UE的SMS上下文信息。
UplinkSMS|Nsmsf_SMService|用于短消息MO、MT流程。短消息MO、MT流程中，NF服务消费者（如AMF）使用Nsmsf_SMService_UplinkSMS向SMSF发送上行链路方向的短消息载荷（如SMS message或Ack）。
##### Nsmsf_SMService Service_Active 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmsf_SMService_Activate|Request/Response|Nsmsf_SMService_Activate用于短消息激活流程。UE发送SMS注册请求，服务消费者（如AMF）向SMSF发送PUT请求消息，消息中携带SMS业务的UE上下文信息 (如 …/ue-contexts/{supi}) ，表示创建或更新UE上下文。SMSF根据SMS业务的UE上下文是否已创建，执行如下操作：如果对应的SMS的UE上下文没有创建，则SMSF向UDM请求用户签约数据，然后进行鉴权，创建SMS业务的UE上下文信息。如果创建成功，则SMSF返回"201 Created"，否则返回对应的错误码如2c。如果对应的SMS的UE上下文已经创建，则SMSF和AMF发起UE上下文更新流程。如果更新成功，则SMSF返回"204 No Content" ，否则返回对应的错误码如2c。UE上下文创建或者更新流程失败，SMSF返回错误码（如 "403 Forbidden"）。
##### Nsmsf_SMService Service_Deactivate 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmsf_SMService_Deactivate|Request/Response|Nsmsf_SMService_Deactivate用于短消息去激活流程。UE发起SMS业务去激活，服务消费者（如AMF）向SMSF发起删除UE上下文的请求。SMSF根据删除UE上下文的成功与否，返回不同结果。删除成功，向AMF返回"204 No Content"。删除失败，向AMF返回对应的错误码（如 "403 Forbidden"）。
##### Nsmsf_SMService Service_UplinkSMS 
服务操作|操作语义|服务操作的解释
---|---|---
Nsmsf_SMService_UplinkSMS|Request/Response|Nsmsf_SMService_UplinkSMS用于短消息MO、MT流程。在MO、MT短消息流程中，服务消费者（如AMF）发送POST请求给SMSF，消息中携带sendsms。SMSF收到短消息载荷后，转发短消息给SMS-GMSC/IWMSC/IP-SM-GW/SMS Router。如果SMSF接收成功，则向AMF返回“200 OK”，如果SMSF接收失败，则向AMF返回对应的错误码（如 "403 Forbidden"）。
#### 数据类型解释 
##### UeSmsContextData 
属性名称|Presence requirement|描述
---|---|---
supi|Mandatory|Subscriber permanent identify，用户永久身份标识。
gpsi|Optional|Generic public subscriber identifier，通用用户公共身份标识。
pei|Optional|永久设备标识，包含该用户的IMEI或者IMEISV。
accessType|Mandatory|接入网络类型。
amfId|Mandatory|AMF实例标识。
guamis|Optional|Globally Unique AMF Identifier，全球唯一AMF标识 。
ueLocation|Optional|UE位置信息（如TAI和CGI）。
backupAmfInfo|Conditional|AMF支持无UDSF的AMF管理时，则在向SMSF发起创建或者更新SMS的UE上下文流程中携带该数据类型。SMSF使用此属性执行NRF查询，以便调用备份AMF中的后续服务，例如Namf_MT。
udmGroupId|Optional|为supi服务的UDM组标识。
##### SmsRecordData 
属性名称|Presence requirement|描述
---|---|---
smsRecordId|Mandatory|SMS有效载荷记录标识。
smsPayload|Mandatory|SMS有效载荷。
##### SmsRecordDeliveryData 
属性名称|Presence requirement|描述
---|---|---
smsRecordId|Mandatory|SMS有效载荷记录标识。
deliveryStatus|Mandatory|指示SMS在SMSF和其他服务化接口间的传输状态。
### N1接口 
#### N1接口协议简介 
场景描述 :N1接口为UE和AMF间的信令面接口。 
协议栈 :N1接口协议栈如[图1](#T_1607674074967__e53e590b-a132-4cd8-bb89-fc6d4a349e07)所示。
图1  N1接口协议栈
[]images/image.png)
##### 消息列表 
N1接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
Authentication request|AMF->UE|AMF给UE发送此消息以发起UE身份鉴权。
Authentication response|UE->AMF|UE发送Authentication response消息给AMF，发送计算出的认证响应给网络。
Authentication result|AMF->UE|AMF发送Authentication result给UE，通知UE标识的鉴权响应认证结果。
Authentication failure|UE->AMF|UE发送Authentication failure消息给AMF，指示网络鉴权失败。
Authentication reject|AMF->UE|AMF发送Authentication reject消息给UE，指示鉴权流程失败，UE将中止所有的活动。
Registration request|UE->AMF|UE使用此消息向5G网络进行注册。
Registration accept|AMF->UE|AMF使用此消息响应UE的注册请求消息。
Registration complete|UE->AMF|注册完成消息由UE发送给AMF。
Registration reject|AMF->UE|此消息由AMF发送给UE，拒绝UE的注册请求。
UL NAS transport|UE->AMF|UL NAS transport消息将消息净荷和相关信息传送给AMF。
DL NAS transport|AMF->UE|DL NAS transport消息将消息净荷和相关信息传送给UE。
De-registration request (UE originating de-registration)|UE->AMF|UE发送Deregistration request消息给AMF。
De-registration accept (UE originating de-registration)|AMF->UE|AMF发送Deregistration accept消息给UE。
De-registration request (UE terminated de-registration)|AMF->UE|AMF发送Deregistration request消息给UE。
De-registration accept (UE terminated de-registration)|UE->AMF|UE发送Deregistration accept消息给AMF。
Service request|UE->AMF|UE向AMF发送Service request消息，请求建立N1 NAS信令连接，和/或请求为没有用户面资源的PDU会话建立用户面资源。
Service accept|AMF -> UE|AMF发送Service accept消息给UE，接受服务请求流程。
Service reject|AMF -> UE|AMF发送Service reject消息给UE，拒绝服务请求流程。
Configuration update command|AMF -> UE|AMF发送Configuration update command消息给UE。
Configuration update complete|UE->AMF|UE发送Configuration update complete消息给AMF。
Identity request|AMF -> UE|AMF发送Identity request消息由给UE，提供请求的身份标识。
Identity response|UE->AMF|Identity response消息由UE发送给AMF，以提供请求的身份标识。
Security mode command|AMF ->UE|AMF发送Security mode command消息给UE，用于建立NAS信令安全。
Security mode complete|UE->AMF|UE发送Security mode complete消息给AMF，响应Security mode command消息。
Security mode reject|UE->AMF|UE发送Security mode reject消息给AMF，表示拒绝相应的安全模式命令。
Security protected 5GS NAS message|UE->AMFAMF->UE|该消息由UE或网络侧发送，用于传递一个完整的5GS NAS消息以及序列号和保护消息的消息认证码。
PDU session establishment request|UE->SMF|UE发送PDU session establishment request消息给SMF，请求建立PDU会话。
PDU session establishment accept|SMF->UE|SMF收到PDU session establishment request消息后，发送PDU SESSION ESTABLISHMENT ACCEPT响应给UE，指示PDU会话建立成功。
PDU session establishment reject|SMF->UE|SMF收到PDU session establishment request消息后，发送PDU session establishment reject响应给UE，指示PDU会话建立失败。
PDU session authentication command|SMF->UE|SMF发送PDU session authentication command给UE，用于对建立PDU会话的UE或参与PDU会话的UE进行鉴权。
PDU session authentication complete|UE->SMF|UE收到PDU session authentication command消息后，发送PDU session authentication complete给SMF，表示接受PDU会话鉴权命令消息。
PDU session authentication result|SMF->UE|SMF发送PDU session authentication result给UE，用于指示参与PDU会话的UE鉴权成功结果。
PDU session modification request|UE->SMF|UE发送PDU session modification request消息给SMF，发起PDU会话修改流程。
PDU session modification reject|SMF->UE|SMF发送PDU session modification reject消息给UE，表示拒绝UE发起的PDU会话修改流程。
PDU session modification command|SMF->UE|SMF发送PDU session modification command消息给UE，发起PDU会话更改流程。
PDU session modification complete|UE->SMF|UE收到PDU session modification command消息后，发送PDU session modification complete给SMF，表示接受PDU会话修改命令消息。
PDU session modification command reject|UE->SMF|UE发送PDU session modification command reject消息给SMF，表示拒绝PDU会话修改命令消息。
PDU session release request|UE->SMF|UE发送PDU session release request消息给SMF，发起PDU会话释放流程。
PDU session release reject|SMF->UE|SMF发送PDU session release reject消息给UE，表示拒绝PDU会话释放。
PDU session release command|SMF->UE|SMF发送PDU session release command消息给UE，发起PDU会话释放流程。
PDU session release complete|UE->SMF|UE收到PDU session release command消息后，发送PDU session release complete给SMF，表示接受PDU会话释放。
#### 相关消息解释 
##### Authentication Request 


消息功能 :AMF给UE发送此消息以发起UE身份鉴权。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Authentication request message identity|Mandatory|该信元为message type类型，在本消息中取值是authentication request。
ngKSI|Mandatory|ngKSI信元表示由网络分配的NAS秘钥集标识。
ABBA|Mandatory|ABBA信元用于实现安全特性的降级保护。
Authentication parameter RAND|Optional|Authentication parameter RAND IE用于计算鉴权响应结果。
Authentication parameter AUTN|Optional|Authentication parameter AUTN IE用于向移动台提供网络鉴权手段。
EAP message|Optional|EAP message信元用于传送EAP消息。


##### Authentication Response 
消息功能 :UE发送Authentication Response消息给AMF，发送计算出的认证响应给网络。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Authentication response message identity|Mandatory|该IE是为message type类型，在本消息中取值是authentication response。
Authentication response parameter|Optional|Authentication response parameter信元表示鉴权响应参数。
EAP message|Optional|EAP message信元用于传送EAP消息。
##### Authentication Result 
消息功能 :AMF发送Authentication Result给UE，通知UE标识的EAP认证结果。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Authentication result message identity|Mandatory|该信元为message type类型，在本消息中取值是authentication result。
ngKSI|Mandatory|ngKSI信元表示由网络分配的NAS秘钥集标识。
EAP message|Mandatory|EAP message信元用于传送EAP消息。
ABBA|Optional|ABBA信元用于实现安全特性的降级保护。
##### Authentication Failure 


消息功能 :UE发送Authentication failure消息给AMF，指示网络鉴权失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Authentication failure message identity|Mandatory|该信元为message type类型，在本消息中取值是authentication failure。
5GMM cause|Mandatory|UE指示网络失败原因。
Authentication failure parameter|Optional|'Synch failure'原因值表明鉴权失败时，Authentication Failure parameter信元用于向网络侧提供必要信息，以便网络侧开始重鉴权流程。


##### Authentication Reject 


消息功能 :AMF发送Authentication reject消息给UE，指示鉴权流程失败，UE将中止所有的活动。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Authentication reject message identity|Mandatory|该信元为message type类型，在本消息中取值是authentication reject。
EAP message|Optional|EAP message信元用于传送EAP消息。


##### Registration Request 


消息功能 :UE使用此消息向5G网络进行注册。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Registration request message identity|Mandatory|该信元为message type类型，在本消息中取值是Registration request。
registration type|Mandatory|5GS registration type信元指示请求的注册类型。
ngKSI|Mandatory|ngKSI信元表示由网络分配的NAS秘钥集标识。
5GS mobile identity|Mandatory|5GS mobile identity信元用于提供SUCI、5G-GUTI、IMEI、IMEISV或5G-S-TMSI。
Non-current native NAS key set identifier|Optional|Non-current native NAS key set identifier信元表示由网络分配的NAS密钥集标识。
5GMM capability|Optional|5GMM capability信元用于向网络提供UE在5G核心网（5GCN）或与EPS交互相关网络方面的信息，这些内容可能会影响网络处理UE操作的方式。
UE security capability|Optional|UE security capability信元用于UE和网络指示UE在N1模式下支持的NAS安全算法，以及用于5GCN连接的NR和E-UTRA上AS安全所支持的安全算法。
Requested NSSAI|Optional|Requested NSSAI信元用于标识一个S-NSSAI集合。说明：请求或允许NSSAI中的S-NSSAI数量不能超过8。配置NSSAI中的S-NSSAI数量不能超过16。一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
Last visited registered TAI|Optional|UE最后访问的跟踪区域。
S1 UE network capability|Optional|S1 UE network capability信元用于向网络提供UE在EPS或GPRS互操作网络方面的信息，其内容可能会影响网络处理UE操作的方式，UE网络能力信息表示UE的一般特征，因此，除了显式指示的字段外，不依赖于发送信道的频段。
Uplink data status|Optional|Uplink data status信元用于向网络指示有上行数据待处理的PDU会话。
PDU session status|Optional|PDU session status信元用于指示PDU会话标识的每个PDU会话的状态。
MICO indication|Optional|MICO indication信元用于指示使用MICO模式或重新协商MICO模式。
UE status|Optional|UE status信元用于向网络提供用于当前UE的注册状态，以便于EPS交互。
Additional GUTI|Optional|如果UE从S1模式切换到N1模式，UE执行注册流程，UE工作在单注册模式，且UE有5G-GUTI，则需要包含该IE。
Allowed PDU session status|Optional|Allowed PDU session status信元用于向网络指示UE允许通过3GPP接入重新建立用户面资源。
UE's usage setting|Optional|UE's usage setting信元用于向网络提供3GPP协议24.301【15】中定义的UE使用设置（UE'susage setting）。网络使用UE的使用设置选择RFSP索引。
Requested DRX parameters|Optional|Requested DRX parameters信元用于指示UE希望使用DRX，或网络在寻呼时使用的DRX周期值。
EPS NAS message container|Optional|EPS NAS message container信元用于传输EPS NAS消息。
LADN indication|Optional|LADN indication信元用于向网络请求特定LADN DNN的LADN信息，或用于指示LADN信息请求。
Payload container|Optional|Payload container信元用于传送一个或多个载荷。如果传输多个载荷，每个载荷的相关信息也随载荷一起传送。
Network slicing indication|Optional|Network slicing indication信元用于指示通用UE配置更新流程和注册流程中与网络切片相关的附加信息，而非UE配置NSSAI、允许的NSSAI和拒绝的NSSAI信息。
5GS update type|Optional|5GS update type信元表示允许UE在注册时向网络提供附加信息。
NAS message container|Optional|NAS message container信元用于封装一个明文5GS NAS消息。


##### Registration Accept 


消息功能 :AMF使用此消息响应UE的注册请求消息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Registration accept message identity|Mandatory|该信元为message type类型，在本消息中取值是Registration accept。
5GS registration result|Mandatory|5GS registration result信元用于指示注册结果。
5G-GUTI|Optional|5G-GUTI信元包含MCC、MNC、AMF Region ID、AMF Set ID、AMF Pointer、5G-TMSI信息。
TAI list|Optional|TAI list信元用于将网络中的跟踪区域列表传递给UE。该信元编码允许对不同类型列表进行组合。当不同的TAIs共享PLMN标识时，允许对“00”和“01”类型的列表进行进一步编码。
Allowed NSSAI|Optional|NSSAI信元用于标识一组S-NSSAI的集合。说明：请求或允许NSSAI的S-NSSAI值不能超过8。配置NSSAI中S-NSSAI值不能超过16。一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
Rejected NSSAI|Optional|Rejected NSSAI信元用于标识一组被拒绝S-NSSAI的集合。
Configured NSSAI|Optional|NSSAI信元用于标识一组S-NSSAI集合。NSSAI为第4类IE，最小长度为4字节，最大长度为146字节。说明：请求或允许NSSAI的S-NSSAI值不能超过8。配置NSSAI中S-NSSAI值不能超过16。一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
5GS network feature support|Optional|5GS network feature support信元用于表示网络是否支持某些特性。
PDU session status|Optional|PDU session status信元用于指示PDU会话标识的每个PDU会话的状态。
PDU session reactivation result|Optional|PDU session reactivation result信元用于表示PDU会话用户面资源建立的结果。
PDU session reactivation result error cause|Optional|PDU session reactivation result error cause信元用于表示由PDU会话ID标识的PUD会话用户面资源建立失败时的错误原因。
LADN information|Optional|LADN information信元用于表示向UE提供当前注册区域中可用LADN的LADN服务区，或用于从UE上删除LADN信息。
MICO indication|Optional|MICO indication信元用于指示使用MICO模式或重新协商MICO模式。
Network slicing indication|Optional|Network slicing indication信元用于指示通用UE配置更新流程和注册流程中与网络切片相关的附加信息，而非UE配置NSSAI、允许的NSSAI和拒绝的NSSAI信息。
Service area list|Optional|Service area list信元用于表示将允许区域的允许跟踪区域列表或不允许区域的禁止跟踪区域列表从网络传输给UE。
T3512 value|Optional|当T3512超时时，如果UE未注册紧急业务，则发起周期性注册流程。如果UE已注册紧急业务，则发起本地去注册流程。
T3502 value|Optional|当T3502超时时，UE再次触发注册流程。
Emergency number list|Optional|该信元用于网络侧传递紧急号码列表给UE，不同的国家或者地区，紧急号码可能不一样。可以通过在网络侧配置紧急号码，当UE漫游到不同的国家或者地区时，向UE下发对应的紧急号码列表。
Extended emergency number list|Optional|Extended emergency number list表示扩展的紧急号码列表。
SOR transparent container|Optional|REGISTRATION ACCEPT消息中携带该信元用于提供优选的PLMN/接入技术组合列表（HPLMN指示UE存储的“运营商控制PLMN选择器与接入技术”列表未改变时，不提供优选PLMN/接入技术组合列表）和可选的确认请求，REGISTRATIONCOMPLETE消息中携带该信元表示UE成功接收到REGISTRATION ACCEPT消息中的SOR transparent container信元。
EAP message|Optional|EAP message信元用于传送EAP消息。
NSSAI inclusion mode|Optional|NSSAI inclusion mode信元用于表示UE操作使用NSSAI包含模式。
Operator-defined access category definitions|Optional|Operator-defined access category definitions信元用于向UE提供运营商定义的接入类别定义，或者删除UE已有的运营商定义的接入类别定义。
Negotiated DRX parameters|Optional|协商后的DRX参数。


##### Registration Complete 


消息功能 :注册完成消息由UE发送给AMF。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Registration complete message identity|Mandatory|该信元为message type类型，在本消息中取值是Registration complete。
SOR transparent container|Optional|REGISTRATION ACCEPT消息中携带该信元用于提供优选的PLMN/接入技术组合列表（HPLMN指示UE存储的“运营商控制PLMN选择器与接入技术”列表未改变时，不提供优选PLMN/接入技术组合列表）和可选的确认请求，REGISTRATIONCOMPLETE消息中携带该信元表示UE成功接收到REGISTRATION ACCEPT消息中的SOR transparent container信元。


##### Registration Reject 


消息功能 :此消息由AMF发送给UE，拒绝UE的注册请求。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Registration reject message identity|Mandatory|该信元为message type类型，在本消息中取值是Registration reject。
5GMM cause|Mandatory|5GMM cause信元表示UE发出的5GMM请求被网络拒绝的原因。
T3346 value|Optional|当通用NAS层拥塞控制处于激活状态时，AMF可以在Reject消息中携带移动性管理回退定时器T3346的值，UE接收到5GMMReject消息中T3346的值时，启动定时器T3346。为避免大量UE同时发起延迟请求，AMF应为被拒绝的UE选择定时器T3346的值，保证超时不同步。
T3502 value|Optional|T3502超时时，UE再次触发注册流程。
EAP message|Optional|EAP message信元用于传送EAP消息。


##### UL NAS Transport 


消息功能 :UL NAS transport消息将消息净荷和相关信息传送给AMF。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
UL NAS TRANSPORT message identity|Mandatory|该信元为message type类型，在本消息中取值是UL NAS TRANSPORT。
Payload container type|Mandatory|Payload container type信元用于表示Payload container信元中包含的净荷类型。
Payload container|Mandatory|Payload container信元用于传送一个或多个载荷。如果传输多个载荷，每个载荷的相关信息也随载荷一起传送。
PDU session ID|Conditional|PDU session ID信元用于在5GMM消息中标识一个PDU会话。
Old PDU session ID|Optional|Old PDU session ID信元用于在5GMM消息中标识一个PDU会话。
Request type|Optional|Request type信元用于表示PDU类型。
S-NSSAI|Optional|S-NSSAI信元用于标识一个网络切片。
DNN|Optional|DNN信元用于标识一个数据网络。
Additional information|Optional|Additional information信元用于向上层提供NAS传输机制相关附加信息。


##### DL NAS Transport 


消息功能 :DL NAS transport消息将消息净荷和相关信息传送给UE。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
DL NAS TRANSPORT message identity|Mandatory|该信元为message type类型，在本消息中取值是DL NAS TRANSPORT。
Payload container type|Mandatory|Payload container type信元用于表示Payload container信元中包含的净荷类型。
Payload container|Mandatory|Payload container信元用于传送一个或多个载荷。如果传输多个载荷，每个载荷的相关信息也随载荷一起传送。
PDU session ID|Conditional|PDU session ID信元用于在5GMM消息中标识一个PDU会话。
Additional information|Optional|Additional information信元用于向上层提供NAS传输机制相关附加信息。
5GMM cause|Optional|5GMM cause信元表示UE发出的5GMM请求被网络拒绝的原因。
Back-off timer value|Optional|当净荷容器表项的Payload container信元中包含上行5GSM消息时，且未发送该消息时，AMF需携带此信元。拥塞控制可能基于DNN、S-NSSAI和DNN，或只基于S-NSSAI。


##### Deregistration Request (UE Originating Deregistration) 
消息功能 :UE发送Deregistration Request消息给AMF。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
De-registration request message identity|Mandatory|该信元为message type类型，在本消息中取值是De-registration request。
De-registration type|Mandatory|De-registration type信元用于表示去注册类型。
ngKSI|Mandatory|ngKSI信元表示由网络分配的NAS秘钥集标识。
5GS mobile identity|Mandatory|5GS移动身份信元用于提供SUCI、5G-GUTI、IMEI、IMEISV或5G-S-TMSI。
##### Deregistration Accept(UE Originating Deregistration) 
消息功能 :AMF发送Deregistration Accept消息给UE。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
De-registration accept message identity|Mandatory|该信元为message type类型，在本消息中取值是De-registration accept。
##### Deregistration Request(UE Terminated Deregistration) 
消息功能 :AMF发送Deregistration Request消息给UE。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
De-registration request message identity|Mandatory|该信元为message type类型，在本消息中取值是De-registration request。
De-registration type|Mandatory|De-registration type信元用于表示去注册类型。
5GMM cause|Optional|5GMM cause信元表示网络侧主动发起去注册请求的原因。
T3346 value|Optional|T3346超时时，网络侧发起去注册请求。
##### Deregistration Accept (UE Terminated Deregistration) 
消息功能 :UE发送Deregistration Accept消息给AMF。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
De-registration accept message identity|Mandatory|该信元为message type类型，在本消息中取值是De-registration accept。
##### Service Request 


消息功能 :UE向AMF发送Service request消息，请求建立N1 NAS信令连接，和/或请求为没有用户面资源的PDU会话建立用户面资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Service request message identity|Mandatory|该信元为message type类型，在本消息中取值是Service request。
ngKSI|Mandatory|ngKSI信元表示由网络分配的NAS秘钥集标识。
Service type|Mandatory|Service type信元用于明确服务请求流程的目的。
5G-S-TMSI|Mandatory|5G-S-TMSI信元包括AMF Set ID、AMF Pointer、5G-TMSI信息。
Uplink data status|Optional|该信元用于向网络指示有上行数据待处理的PDU会话。
PDU session status|Optional|PDU session status信元用于指示PDU会话标识的每个PDU会话的状态。
Allowed PDU session status|Optional|Allowed PDU session status信元用于向网络指示UE允许通过3GPP接入重新建立用户面资源。
NAS message container|Optional|NAS message container信元用于封装一个明文5GS NAS消息。


##### Service Accept 


消息功能 :AMF发送Service accept消息给UE，接受服务请求流程。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Service accept message identity|Mandatory|该信元为message type类型，在本消息中取值是Service accept。
PDU session status|Optional|PDU session status信元用于指示PDU会话标识的每个PDU会话的状态。
PDU session reactivation result|Optional|PDU session reactivation result信元用于表示PDU会话用户面资源建立的结果。
PDU session reactivation result error cause|Optional|PDU session reactivation result error cause信元用于表示由PDU会话ID标识的PUD会话用户面资源建立失败时的错误原因。
EAP message|Optional|EAP message信元用于传送EAP消息。


##### Service Reject 


消息功能 :AMF发送Service reject消息给UE，拒绝服务请求流程。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Service reject message identity|Mandatory|该信元为message type类型，在本消息中取值是Service reject。
5GMM cause|Mandatory|5GMM cause信元指示UE发出的5GMM请求被网络拒绝的原因。
PDU session status|Optional|PDU session status信元用于指示PDU会话标识的每个PDU会话的状态。
T3346 value|Optional|当通用NAS层拥塞控制处于激活状态时，AMF可以在Reject消息中携带移动性管理回退定时器T3346的值，UE接收到5GMMReject消息中T3346的值时，启动定时器T3346。为避免大量UE同时发起延迟请求，AMF应为被拒绝的UE选择定时器T3346的值，保证超时不同步。
EAP message|Optional|EAP message信元用于传送EAP消息。


##### Configuration Update Command 


消息功能 :AMF发送Configuration update command消息给UE。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Configuration update command message identity|Mandatory|该信元为message type类型，在本消息中取值是Configuration update command。
Configuration update indication|Optional|Configuration update indication信元表示与通用UE配置更新流程相关的附加信息。
5G-GUTI|Optional|该IE可以包括为UE分配一个新的5G GUTI。
TAI list|Optional|TAI list信元用于将网络侧分配给UE的跟踪区列表传递给UE。
Allowed NSSAI|Optional|Allowed NSSAI信元用于标识一个S-NSSAI集合。说明：请求或允许NSSAI的S-NSSAI值不能超过8。配置NSSAI中S-NSSAI值不能超过16。一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
Service area list|Optional|Service area list信元用于表示将允许区域的允许跟踪区域列表或不允许区域的禁止跟踪区域列表从网络传输给UE。
Full name for network|Optional|网络全名称。
Short name for network|Optional|网络短名称。
Local time zone|Optional|Local time zone信元表示对通用时间和本地时间之间的偏移量进行15分钟的编码。
Universal time and local time zone|Optional|Universal time and local time zone信元表示传递时间和时区给UE。
Network daylight saving time|Optional|Network daylight saving time信元表示对夏令时进行15分钟的编码。
LADN information|Optional|LADN information信元用于向网络请求特定LADN DNN的LADN信息，或用于指示LADN信息请求。
MICO indication|Optional|MICO indication信元用于指示使用MICO模式或重新协商MICO模式。
Network slicing indication|Optional|Network slicing indication信元用于指示通用UE配置更新流程和注册流程中与网络切片相关的附加信息，而非UE配置NSSAI、允许的NSSAI和拒绝的NSSAI信息。
Configured NSSAI|Optional|NSSAI信元用于标识一个S-NSSAI集合。说明：请求或允许NSSAI的S-NSSAI值不能超过8。配置NSSAI中S-NSSAI值不能超过16。一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
Rejected NSSAI|Optional|Rejected NSSAI信元用于标识一个拒绝访问的S-NSSAI集合。
Operator-defined access category definitions|Optional|Operator-defined access category definitions信元用于向UE提供运营商定义的接入类别定义，或者删除UE已有的运营商定义的接入类别定义。
SMS indication|Optional|SMS indication信元表示UE在NAS上使用SMS的能力发生变化。


##### Configuration Update Complete 


消息功能 :UE发送Configuration update complete消息给AMF。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Configuration update complete message identity|Mandatory|该信元为message type类型，在本消息中取值是Configuration update complete。


##### Identity Request 


消息功能 :AMF发送Identity request消息由给UE，提供请求的身份标识。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Identity request message identity|Mandatory|该信元为message type类型，在本消息中取值是Identity request。
Identity type|Mandatory|Identity type信元用于指定请求的身份。


##### Identity Response 


消息功能 :Identity response消息由UE发送给AMF，以提供请求的身份标识。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Identity response message identity|Mandatory|该信元为message type类型，在本消息中取值是Identity response。
Mobile identity|Mandatory|5GS移动身份信元用于提供SUCI、5G-GUTI、IMEI、IMEISV或5G-S-TMSI。


##### Security Mode Command 


消息功能 :AMF发送Security mode command消息给UE，用于建立NAS信令安全。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Security mode command message identity|Mandatory|该信元为message type类型，在本消息中取值是Security mode command。
Selected NAS security algorithms|Mandatory|Selected NAS security algorithms信元表示用于加密和完整性保护的5G算法。
ngKSI|Mandatory|ngKSI信元表示由网络分配的NAS秘钥集标识。
Replayed UE security capabilities|Mandatory|UE security capability信元用于UE和网络指示UE在N1模式下NAS安全支持的些安全算法，以及5GCN连接的NR和E-UTRA上用于AS安全所支持的安全算法。
IMEISV request|Optional|IMEISV request信元用于表示MS在鉴权加密响应消息中应包含IMEISV。
Selected EPS NAS security algorithms|Optional|NAS security algorithms信元用于表示用于加密和完整性保护的5G算法。
Additional 5G security information|Optional|Additional 5G security information信元用于为UE提供额外的安全参数，比如，水平推衍参数，或者请求UE在安全模式控制过程中重传初始NAS消息。UE使用这些参数完成安全模式控制流程。
EAP message|Optional|EAP message信元用于传送EAP消息。
ABBA|Optional|ABBA信息元素的目的是为了实现安全特性降级保护。
Replayed S1 UE security capabilities|Optional|Replayed S1 UE security capabilities信元用于网络指示UE在S1模式、Iu模式和Gb模式下支持的安全算法。若安全性算法支持S1模式则同样支持NAS和AS安全性。


##### Security Mode Complete 


消息功能 :UE发送Security mode complete消息给AMF，响应SECURITY
MODE COMMAND消息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Security mode complete message identity|Mandatory|该信元为message type类型，在本消息中取值是Security mode complete。
IMEISV|Optional|如果在相应的安全模式命令消息中请求IMEISV，UE应包含该信息元素。
NAS message container|Optional|NAS消息容器的目的是封装一个纯5GS NAS消息。


##### Security Mode Reject 


消息功能 :UE发送Security mode reject消息给AMF，表示拒绝相应的安全模式命令。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Security mode reject message identity|Mandatory|该信元为message type类型，在本消息中取值是Security mode reject。
5GMM cause|Mandatory|5GMM cause信元表示UE拒绝网络的原因。


##### Security Protected 5GS NAS Message 


消息功能 :该消息由UE或网络侧发送，用于传递一个完整的5GS NAS消息以及序列号和保护消息的消息认证码。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
Security header type|Mandatory|每个5GMM消息第二个字节的比特位1至4包含该IE。该IE包含5GMM消息安全保护相关的控制信息，占4比特位。
Spare half octet|Mandatory|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
Message authentication code|Mandatory|Message authentication code信元包含了消息的完整性保护信息，如果存在有效的5G NAS安全上下文，且安全功能启动，则SECURITYPROTECTED 5GS NAS MESSAGE包含MAC信元。
Sequence number|Mandatory|Sequence number信元包含NAS消息序列号（SN）。该序列号由NAS COUNT for a SECURITYPROTECTED 5GS NAS MESSAGE消息的NAS COUNT的8个最低有效位组成。
Plain 5GS NAS message|Mandatory|Plain 5GS NAS message信元包含一个明文5GS NAS消息，SECURITY PROTECTED5GS NAS MESSAGE消息不是明文5GS NAS消息，不应包含在此信元中。


##### PDU Session Establishment Request 


消息功能 :UE发送PDU session establishment request消息给SMF，请求建立PDU会话。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session establishment request message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session establishment request。
Integrity protection maximum data rate|Mandatory|Integrity protection maximum data rate信元用于UE向网络指示UE支持的上下行用户面完整性保护的最大速率。
PDU session type|Optional|PDU session type信元用于表示PDU会话类型。
SSC mode|Optional|SSC mode信元用于表示SSC模式。
5GSM capability|Optional|5GSM capability信元IE用于指示PDU会话管理相关的UE能力。
Maximum number of supported packet filters|Optional|Maximum number of supported packet filters信元用于UE向网络指示最大包过滤数目，与UE建立“IPv4”、“IPv6”、“IPv4v6”或“Ethernet”PDU类型会话时能够支持的QoS规则相关联。
Always-on PDU session requested|Optional|Always-on PDU session requested信元用于指示PDU会话是否被请求建立为Always-on的PDU会话。
SM PDU DN request container|Optional|本信元通过网络接入标识 (NAI) 格式携带UE标识，不同数据网络下，UE标识不同。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Establishment Accept 
消息功能 :SMF收到PDU session establishment request消息后，发送PDU
session establishment accept响应给UE，指示PDU会话建立成功。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session establishment accept message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session establishment accept。
Selected PDU session type|Mandatory|PDU session type信元IE用于表示PDU会话类型。
Selected SSC mode|Mandatory|SSC mode信元用于表示SSC模式。
Authorized QoS rules|Mandatory|QoS规则信元用于指示UE使用的一组QoS规则。
Session AMBR|Mandatory|Session-AMBR信元用于表示UE建立PDU会话时指示初始签约的PDU会话聚合最大比特速率，或者在网络改变PDU会话聚合最大比特速率时指示新签约的PDU会话聚合最大比特速率。
5GSM cause|Optional|5GSM cause信元用于指示5GSM请求被拒绝的原因。
PDU address|Optional|PDU address信元用于分配给UE以下信息：与PDU会话关联的IPv4地址；与所述PDU会话关联的IPv6本地链路地址接口标识；与所述PDU会话关联的本地IPv6链路地址接口标识和IPv4地址。
RQ timer value|Optional|当网络需要提供RQ定时器时，该信元被包含。
S-NSSAI|Optional|S-NSSAI IE用于标识一个网络切片。
Always-on PDU session indication|Optional|Always-on PDU session requested信元用于指示PDU会话是否被请求建立为Always-on的PDU会话。
Mapped EPS bearer contexts|Optional|Mapped EPS bearer contexts信元IE用于表示一个PDU会话对应的EPS上下文集合。
EAP message|Optional|EAP message信元用于传送EAP消息。
Authorized QoS flow descriptions|Optional|QoS flow descriptions信元用于表示UE使用的QoS流描述的集合，每个QoS流描述包含一组参数集合。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。
DNN|Optional|DNN信元用于标识一个数据网络。
##### PDU Session Establishment Reject 
消息功能 :SMF收到PDU session establishment request消息后，发送PDU
session establishment reject响应给UE，指示PDU会话建立失败。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session establishment reject message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session establishment reject。
5GSM cause|Mandatory|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Back-off timer value|Optional|当净荷容器表项的Payload container信元中包含上行5GSM消息时，且未发送该消息时，AMF需携带此信元。拥塞控制可能基于DNN、S-NSSAI和DNN，或只基于S-NSSAI。
Allowed SSC mode|Optional|Allowed SSC mode信元用于UE指示PDU会话允许使用的SSC模式。
EAP message|Optional|EAP message信元用于传送EAP消息。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。
##### PDU Session Authentication Command 


消息功能 :SMF发送PDU session authentication command给UE，用于对建立PDU会话的UE或参与PDU会话的UE进行鉴权。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session authentication complete message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session authentication command。
EAP message|Mandatory|EAP message信元用于传送EAP消息。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Authentication Complete 


消息功能 :UE收到PDU session authentication command消息后，发送PDU
session authentication complete给SMF，表示接受PDU会话鉴权命令消息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session authentication complete message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session authentication complete。
EAP message|Mandatory|EAP message信元用于传送EAP消息。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Authentication Result 


消息功能 :SMF发送PDU session authentication result给UE，用于指示参与PDU会话的UE鉴权成功结果。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session authentication result message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session authentication result。
EAP message|Optional|EAP message信元用于传送EAP消息。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Modification Request 


消息功能 :UE发送PDU session modification request消息给SMF，发起PDU会话修改流程。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session modification request message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session modification request。
5GSM capability|Optional|5GSM capability信元用于指示PDU会话管理相关的UE能力。
5GSM cause|Optional|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Maximum number of supported packet filters|Optional|Maximum number of supported packet filters信元用于UE向网络指示最大包过滤数目，与UE建立“IPv4”、“IPv6”、“IPv4v6”或“Ethernet”PDU类型会话时能够支持的QoS规则相关联。
Always-on PDU session requested|Optional|Always-on PDU session requested信元用于指示PDU会话是否被请求建立为Always-on的PDU会话。
Integrity protection maximum data rate|Optional|Integrity protection maximum data rate信元用于UE向网络指示UE支持的上下行用户面完整性保护的最大速率。
Requested QoS rules|Optional|QoS规则信元用于指示UE使用的一组QoS规则。
Requested QoS flow descriptions|Optional|QoS flow descriptions信元用于表示UE使用的QoS流描述的集合，每个QoS流描述包含一组参数集合。
Mapped EPS bearer contexts|Optional|Mapped EPS bearer contexts信元用于指示一个PDU会话对应的EPS上下文集合。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Modification Reject 


消息功能 :SMF发送PDU session modification reject消息给UE，表示拒绝UE发起的PDU会话修改流程。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session modification reject message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session modification reject。
5GSM cause|Mandatory|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Back-off timer value|Optional|当净荷容器表项的Payload container信元中包含上行5GSM消息时，且未发送该消息时，AMF需携带此信元。拥塞控制可能基于DNN、S-NSSAI和DNN，或只基于S-NSSAI。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Modification Command 
消息功能 :SMF发送PDU session modification command消息给UE，发起PDU会话更改流程。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session authentication command message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session modification command。
5GSM cause|Optional|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Session AMBR|Optional|Session-AMBR信元用于UE建立PDU会话时表示初始签约的PDU会话聚合最大比特速率，或者在网络改变PDU会话聚合最大比特速率时指示新签约的PDU会话聚合最大比特速率。
RQ timer value|Optional|当网络需要提供RQ定时器时，该信元被包含。
Always-on PDU session indication|Optional|Always-on PDU session requested信元用于指示PDU会话是否被请求建立为Always-on的PDU会话。
Authorized QoS rules|Optional|QoS规则信元用于指示UE使用的一组QoS规则。
Mapped EPS bearer contexts|Optional|Mapped EPS bearer contexts信元用于指示一个PDU会话对应的EPS上下文集合。
Authorized QoS flow descriptions|Optional|QoS flow descriptions信元IE用于表示UE使用的QoS流描述集合，每个QoS流描述包含一组参数的集合。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。
##### PDU Session Modification Complete 


消息功能 :UE收到PDU session modification command消息后，发送PDU
session modification complete给SMF，表示接受PDU会话修改命令消息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session modification complete message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session modification complete。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Modification Command Reject 
消息功能 :UE发送PDU session modification command
reject消息给SMF，表示拒绝PDU会话修改命令消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session modification command reject message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session modification commandreject。
5GSM cause|Mandatory|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。
##### PDU Session Release Request 


消息功能 :UE发送PDU session release request消息给SMF，发起PDU会话释放流程。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session release request message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session release request。
5GSM cause|Optional|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Release Reject 


消息功能 :SMF发送PDU session release reject消息给UE，表示拒绝PDU会话释放。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session release reject message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session release reject。
5GSM cause|Mandatory|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Release Command 


消息功能 :SMF发送PDU session release command消息给UE，发起PDU会话释放流程。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1, bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session release command message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session release command。
5GSM cause|Mandatory|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Back-off timer value|Optional|当净荷容器表项的Payload container信元中包含上行5GSM消息时，且未发送该消息时，AMF需携带此信元。拥塞控制可能基于DNN、S-NSSAI和DNN，或只基于S-NSSAI。
EAP message|Optional|EAP message信元用于传送EAP消息。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


##### PDU Session Release Complete 


消息功能 :UE收到PDU session release command消息后，发送PDU
session release complete给SMF，表示接受PDU会话释放。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Extended protocol discriminator|Mandatory|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1~ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value(octet 1，bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session managementmessages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
PDU session ID|Mandatory|PDU session ID信元用于在5GSM消息中标识一个PDU会话。
PTI|Mandatory|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
PDU session release complete message identity|Mandatory|该信元为message type类型，在本消息中取值是PDU session release complete。
5GSM cause|Optional|5GSM cause信元用于指示5GSM请求被拒绝的原因。
Extended protocol configuration options|Optional|Extended protocol configuration options信元用于传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。


#### 相关信元解释 
##### registration type 
IE|说明
---|---
registration type|该IE指示请UE请求的5GS注册类型。取值：Bits 3 2 10 0 1，初始注册。0 1 0，移动注册更新。0 1 1，周期注册更新。1 0 0，紧急注册。
##### 5GS registration result 
IE|说明
---|---
5GS registration result|5GS registration result信元用于指示注册结果。
##### 5GS mobile identity 
IE|说明
---|---
5GS mobile identity|5GS移动身份信元用于提供SUCI、5G-GUTI、IMEI、IMEISV或5G-S-TMSI。
##### 5GS network feature support 
IE|说明
---|---
5GS network feature support|5GS network feature support信元用于表示网络是否支持某些特性。
##### 5GS update type 
IE|说明
---|---
5GS update type|5GS update type信元表示允许UE在注册时向网络提供附加信息。信元内不同bit位是否置位的含义如下：NG-RAN-RCU bit为0：NG-RAN radio capability update not neededNG-RAN-RCU bit为1：NG-RAN radio capability update needed如果注册请求消息中此信元的NG-RAN-RCU为1，则AMF删除本地存储的UE能力。
##### 5G-S-TMSI 
IE|说明
---|---
5G-S-TMSI|包括AMS Set ID、AMD Pointer、5G-TMSI等信息。
##### 5G-GUTI 
IE|说明
---|---
5G-GUTI|包括MCC、MNC、AMF Region ID、AMS Set ID、AMD Pointer、5G-TMSI等信息。
##### 5GSM capability 
IE|说明
---|---
5GSM capability|5GSM capability信元IE用于指示PDU会话管理相关的UE能力。
##### 5GMM cause 
IE|说明
---|---
5GMM cause|5GMM cause信元用于指示5GMM请求被拒绝的原因。
##### 5GMM capability 
IE|说明
---|---
5GMM capability|5GMM capability信元用于向网络提供UE在5G核心网（5GCN）或与EPS交互相关网络方面的信息，这些内容可能会影响网络处理UE操作的方式。该信元为6类信元，最小长度为3字节，最大长度为15字节。
##### 5GMM STATUS message identity 
IE|说明
---|---
5GMM STATUS message identity|该信元为message type类型，取值是5GMM STATUS。
##### ABBA 
IE|说明
---|---
ABBA|ABBA信元用于实现安全特性的降级保护。
##### Access type 
IE|说明
---|---
Access type|Access type信元表示待发送给UE的下行信令或用户数据的接入类型。
##### Additional GUTI 
IE|说明
---|---
Additional GUTI|如果UE从S1模式切换到N1模式，UE执行注册流程，UE工作在单注册模式，且UE有5G-GUTI，则需要包含该IE。
##### Additional information 
IE|说明
---|---
Additional information|Additional information信元用于向上层提供NAS传输机制相关附加信息。
##### Additional 5G security information 
IE|说明
---|---
Additional 5G security information|Additional 5G security information信元用于为UE提供额外的安全参数，比如，水平推衍参数，或者请求UE在安全模式控制过程中重传初始NAS消息。UE使用这些参数完成安全模式控制流程。
##### Always-on PDU session requested 
IE|说明
---|---
Always-on PDU session requested|Always-on PDU session requested信元用于指示PDU会话是否被请求建立为Always-on的PDU会话。
##### Allowed PDU session status 
IE|说明
---|---
Allowed PDU session status|Allowed PDU session status信元用于向网络指示UE允许通过3GPP接入重新建立用户面资源。
##### Allowed NSSAI 
IE|说明
---|---
Allowed NSSAI|NSSAI信元用于标识一个S-NSSAI集合。本IE为第4类信元，最小长度为4字节，最大长度为146字节。注1：请求或允许NSSAI的S-NSSAI值不能超过8。注2：配置NSSAI中S-NSSAI值不能超过16。注3：一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
##### Allowed SSC mode 
IE|说明
---|---
Allowed SSC mode|Allowed SSC mode信元用于UE指示PDU会话允许使用的SSC模式
##### Authentication request message identity 
IE|说明
---|---
Authentication request message identity|该信元为message type类型，取值是authentication request。
##### Authentication response message identity 
IE|说明
---|---
Authentication response message identity|该IE是为message type类型，取值是authentication response。
##### Authentication result message identity 
IE|说明
---|---
Authentication result message identity|该信元为message type类型，取值是authentication result。
##### Authentication response parameter 
IE|说明
---|---
Authentication response parameter|Authentication response parameter信元表示鉴权响应参数。
##### Authentication reject message identity 
IE|说明
---|---
Authentication reject message identity|该信元为message type类型。
##### Authentication failure message identity 
IE|说明
---|---
Authentication failure message identity|该信元为message type类型。
##### Authentication failure parameter 
IE|说明
---|---
Authentication failure parameter|鉴权挑战后'Synch failure'原因值表明鉴权失败时，Authentication Failure parameter信元用于向网络侧提供必要信息，以便网络侧开始重鉴权流程。
##### Authentication parameter RAND 
IE|说明
---|---
Authentication parameter RAND|Authentication parameter RAND信元用于计算鉴权响应结果。
##### Authentication parameter AUTN 
IE|说明
---|---
Authentication parameter AUTN|Authentication parameter AUTN IE用于向移动台提供网络鉴权手段。
##### Authorized QoS rules 
IE|说明
---|---
Authorized QoS rules|QoS规则信元用于指示UE使用的一组QoS规则。
##### Authorized QoS flow descriptions 
IE|说明
---|---
Authorized QoS flow descriptions|QoS flow descriptions信元用于表示UE使用的QoS流描述的集合，每个QoS流描述包含一组参数集合。
##### Back-off timer value 
IE|说明
---|---
Back-off timer value|当净荷容器表项的Payload container信元中包含上行5GSM消息时，且未发送该消息时，AMF需携带此信元。拥塞控制可能基于DNN、S-NSSAI和DNN，或只基于S-NSSAI。
##### Configured NSSAI 
IE|说明
---|---
Configured NSSAI|NSSAI信元用于标识一个S-NSSAI集合。NSSAI为第4类IE，最小长度为4字节，最大长度为146字节注1：请求或允许NSSAI的S-NSSAI值不能超过8。注2：配置NSSAI中的S-NSSAI值不能超过16。注3：一个NSSAI中的多个S-NSSAI可以有相同SST值或SD值（可选），与匹配到的不同HPLMN的SST值和可选匹配的HPLMN的SD值相关。
##### Configuration update command message identity 
IE|说明
---|---
Configuration update command message identity|该信元为message type类型。
##### Configuration update complete message identity 
IE|说明
---|---
Configuration update complete message identity|该信元为message type类型。
##### Configuration update indication 
IE|说明
---|---
Configuration update indication|Configuration update indication信元表示与通用UE配置更新流程相关的附加信息。
DNN :IE|说明
---|---
DNN|DNN信元用于标识一个数据网络。
##### De-registration request message identity 
IE|说明
---|---
De-registration request message identity|该信元为message type类型，取值是De-registration request。
##### De-registration accept message identity 
IE|说明
---|---
De-registration accept message identity|该信元为message type类型，取值是De-registration accept。
##### De-registration type 
IE|说明
---|---
De-registration type|De-registration type信元用于表示去注册类型。
##### DL NAS TRANSPORT message identity 
IE|说明
---|---
DL NAS TRANSPORT message identity|该信元为message type类型，取值是DL NAS TRANSPORT。
##### EAP message 
IE|说明
---|---
EAP message|EAP message信元用于传送EAP消息。
##### Equivalent PLMNs 
IE|说明
---|---
Equivalent PLMNs|PLMN List信元用于向移动台提供对等PLMN编码列表。
##### Emergency number list 
IE|说明
---|---
Emergency number list|Emergency number list信元用于对紧急号码进行编码。对于紧急号码列表，不同国家可能不一样，需要网络侧下发，UE漫游时接受存储。
##### Extended protocol discriminator 
IE|说明
---|---
Extended protocol discriminator|当PD（Protocol Discriminator）被设置为“PD扩展到一个字节长度”时，5G NAS消息的第一个字节的bit1 ～ bit8包含EPD信元。EPD标识标准层三消息所属的三层协议，EPD取值及其含义如下：EPD value (octet 1，bit 1 to bit 8)Bits8	7	6	5	4	3	2	10	0	0	0	1	1	1	0	reserved0	0	0	1	1	1	1	0	reserved0	0	1	0	1	1	1	0	5GS session management messages0	0	1	1	1	1	1	0	reserved0	1	0	0	1	1	1	0	reserved0	1	0	1	1	1	1	0	reserved0	1	1	0	1	1	1	0	reserved0	1	1	1	1	1	1	0	5GS mobility management messages1	0	0	0	1	1	1	0	reserved1	0	0	1	1	1	1	0	reserved1	0	1	0	1	1	1	0	reserved1	0	1	1	1	1	1	0	reserved1	1	0	0	1	1	1	0	reserved1	1	0	1	1	1	1	0	reserved1	1	1	0	1	1	1	0	reserved1	1	1	1	1	1	1	0	reserved
##### Extended protocol configuration options 
IE|说明
---|---
Extended protocol configuration options|Extended protocol configuration options信元用于：传递与PDP上下文激活相关的外部网络协议选项。传递与外部协议或应用关联的附加（协议）数据，如配置参数，错误码或消息/事件。
##### EPS NAS message container 
IE|说明
---|---
EPS NAS message container|EPS NAS message container信元用于传输EPS NAS消息。该信元为6类信元。
##### Extended emergency number list 
IE|说明
---|---
Extended emergency number list|Extended emergency number list信元表示扩展的紧急号码列表。
##### Full name for network 
IE|说明
---|---
Full name for network|Full name for network信元表示网络全名称。
##### IMEISV request 
IE|说明
---|---
IMEISV request|IMEISV request信元用于表示MS在安全模式完成消息中应包含IMEISV。
##### IMEISV 
IE|说明
---|---
IMEISV|国际移动设备识别软件版本（International Mobile Equipment Identity Software Version），主要用于标识移动台和版本号。
##### Identity request message identity 
IE|说明
---|---
Identity request message identity|该信元为message type类型，取值是Identity request。
##### Identity response message identity 
IE|说明
---|---
Identity response message identity|该信元为message type类型。
##### Integrity protection maximum data rate 
IE|说明
---|---
Integrity protection maximum data rate|Integrity protection maximum data rate信元用于UE向网络指示UE支持的上下行用户面完整性保护的最大速率。
##### Identity type 
IE|说明
---|---
Identity type|Identity type信元用于指定请求的身份。
##### Last visited registered TAI 
IE|说明
---|---
Last visited registered TAI|Last visited registered TAI信元用于标识UE最后访问的跟踪区域。该信元为3类信元，长度为7字节。
##### Local time zone 
IE|说明
---|---
Local time zone|Local time zone信元表示对通用时间和本地时间之间的偏移量进行15分钟的编码。
##### LADN indication 
IE|说明
---|---
LADN indication|LADN indication信元用于向网络请求特定LADN DNN的LADN信息，或用于指示LADN信息请求。
##### LADN information 
IE|说明
---|---
LADN information|LADN information信元用于表示向UE提供当前注册区域中可用LADN的LADN服务区，或用于从UE上删除LADN信息。
##### Mapped EPS bearer contexts 
IE|说明
---|---
Mapped EPS bearer contexts|Mapped EPS bearer contexts信元IE用于表示一个PDU会话对应的EPS上下文集合。
##### Message authentication code 
IE|说明
---|---
Message authentication code|Message authentication code信元包含了消息的完整性保护信息，如果存在有效的5G NAS安全上下文，且安全功能启动，则SECURITY PROTECTED 5GS NAS MESSAGE包含MAC信元。
##### Maximum number of supported packet filters 
IE|说明
---|---
Maximum number of supported packet filters|Maximum number of supported packet filters信元用于UE向网络指示最大包过滤数目，与UE建立“IPv4”、“IPv6”、“IPv4v6”或“Ethernet”PDU类型会话时能够支持的QoS规则相关联。
##### Mobile identity 
IE|说明
---|---
Mobile identity|5GS移动身份信元用于提供SUCI、5G-GUTI、IMEI、IMEISV或5G-S-TMSI。
##### MICO indication 
IE|说明
---|---
MICO indication|MICO indication信元用于指示使用MICO模式或重新协商MICO模式。
##### NAS message container 
IE|说明
---|---
NAS message container|NAS message container信元用于封装一个明文5GS NAS消息。
##### Network slicing indication 
IE|说明
---|---
Network slicing indication|Network slicing indication信元用于指示通用UE配置更新流程和注册流程中与网络切片相关的附加信息，而非UE配置NSSAI、允许的NSSAI和拒绝的NSSAI信息。
##### Network daylight saving time 
IE|说明
---|---
Network daylight saving time|Network daylight saving time信元表示对夏令时进行15分钟的编码。
##### Negotiated DRX parameters 
IE|说明
---|---
Negotiated DRX parameters|Negotiated DRX parameters信元表示网络侧经过协商后，下发给UE的DRX参数。
##### ngKSI 
IE|说明
---|---
ngKSI|ngKSI信元表示由网络分配的NAS秘钥集标识。
##### Non-current native NAS key set identifier 
IE|说明
---|---
Non-current native NAS key set identifier|Non-current native NAS key set identifier信元表示由网络分配的NAS密钥集标识。该信元为1类信元。
##### Notification message identity 
IE|说明
---|---
Notification message identity|该信元为message type类型，取值是Notification。
##### Notification response message identity 
IE|说明
---|---
Notification response message identity|该信元为message type类型，取值是Notification response。
##### NSSAI inclusion mode 
IE|说明
---|---
NSSAI inclusion mode|NSSAI inclusion mode信元用于表示UE操作使用NSSAI包含模式。
##### Operator-defined access category definitions 
IE|说明
---|---
Operator-defined access category definitions|Operator-defined access category definitions信元用于向UE提供运营商定义的接入类别定义，或者删除UE已有的运营商定义的接入类别定义。
##### Old PDU session ID 
IE|说明
---|---
Old PDU session ID|Old PDU session ID信元用于在5GMM消息中标识一个PDU会话。
##### Payload container 
IE|说明
---|---
Payload container|Payload container信元用于传送一个或多个载荷。如果传输多个载荷，每个载荷的相关信息也随载荷一起传送。
##### Payload container type 
IE|说明
---|---
Payload container type|Payload container type信元用于表示Payload container信元中包含的净荷类型。
##### Plain 5GS NAS message 
IE|说明
---|---
Plain 5GS NAS message|Plain 5GS NAS message信元包含一个明文5GS NAS消息，SECURITY PROTECTED 5GS NAS MESSAGE消息不是明文5GS NAS消息，不应包含在此信元中。
##### PDU address 
IE|说明
---|---
PDU address|PDU address信元用于分配给UE以下信息：与PDU会话关联的IPv4地址；与所述PDU会话关联的IPv6本地链路地址接口标识；与所述PDU会话关联的本地IPv6链路地址接口标识和IPv4地址。
##### PDU session status 
IE|说明
---|---
PDU session status|PDU session status信元用于指示PDU会话标识的每个PDU会话的状态。该信元为4类信元，最小长度为4字节，最大长度为34字节。
##### PDU session type 
IE|说明
---|---
PDU session type|PDU session type信元用于表示PDU会话类型。
##### PDU session ID 
IE|说明
---|---
PDU session ID|PDU session ID信元主要用于在5GSM消息中标识一个PDU会话。
##### PDU session reactivation result 
IE|说明
---|---
PDU session reactivation result|PDU session reactivation result信元用于表示PDU会话用户面资源建立的结果。
##### PDU session reactivation result error cause 
IE|说明
---|---
PDU session reactivation result error cause|PDU session reactivation result error cause信元用于表示由PDU会话ID标识的PDU会话用户面资源建立失败时的错误原因。
##### PDU session establishment accept message identity 
IE|说明
---|---
PDU session establishment accept message identity|该信元为message type类型，取值是PDU session establishment accept。
##### PDU session establishment request message identity 
IE|说明
---|---
PDU session establishment request message identity|该信元为message type类型，取值是PDU session establishment request。
##### PDU session establishment reject message identity 
IE|说明
---|---
PDU session establishment reject message identity|该信元为message type类型，取值是PDU session establishment reject。
##### PDU session authentication command message identity 
IE|说明
---|---
PDU session authentication command message identity|该信元为message type类型，取值是PDU session authentication command。
##### PDU session authentication result message identity 
IE|说明
---|---
PDU session authentication result message identity|该信元为message type类型，取值是PDU session authentication result。
##### PDU session authentication complete message identity 
IE|说明
---|---
PDU session authentication complete message identity|该信元为message type类型，取值是PDU session authentication complete。
##### PDU session modification request message identity 
IE|说明
---|---
PDU session modification request message identity|该信元为message type类型，取值是PDU session modification request。
##### PDU session modification reject message identity 
IE|说明
---|---
PDU session modification reject message identity|该信元为message type类型，取值是PDU session modification reject。
##### PDU session modification command message identity 
IE|说明
---|---
PDU session modification command message identity|该信元为message type类型，取值是PDU session modification command。
##### PDU session modification complete message identity 
IE|说明
---|---
PDU session modification complete message identity|该信元为message type类型，取值是PDU session modification complete。
##### PDU session modification command reject message identity 
IE|说明
---|---
PDU session modification command reject message identity|该信元为message type类型，取值是PDU session modification command reject。
##### PDU session release request message identity 
IE|说明
---|---
PDU session release request message identity|该信元为message type类型，取值是PDU session release request。
##### PDU session release reject message identity 
IE|说明
---|---
PDU session release reject message identity|该信元为message type类型，取值是PDU session release reject。
##### PDU session release command message identity 
IE|说明
---|---
PDU session release command message identity|该信元为message type类型，取值是PDU session release command。
##### PDU session release complete message identity 
IE|说明
---|---
PDU session release complete message identity|该信元为message type类型，取值是PDU session release complete。
##### PTI 
IE|说明
---|---
PTI|每个5GSM消息第三个字节（比特位1至8）和每个UE策略下发消息的第一个字节（比特位1至8）包含流程事务标识(PTI)。
##### RQ timer value 
IE|说明
---|---
RQ timer value|Reflective QoS Timer value，反射QoS定时器的值。
##### Request type 
IE|说明
---|---
Request type|Request type信元用于表示请求的PDU会话类型。Request type取值(octet 1, bit 1 to bit 4)：Bits3	2	10	0	1	initial request0	1	0	existing PDU session0	1	1	initial emergency request1	0	0	existing emergency PDU session1	0	1	modification request1	1	1	reserved所有其他值都是未使用的，如果网络收到，应解释为“初始请求”。
##### Replayed UE security capabilities 
IE|说明
---|---
Replayed UE security capabilities|UE security capability信元用于UE和网络指示UE在N1模式下NAS安全支持的些安全算法，以及5GCN连接的NR和E-UTRA上用于AS安全所支持的安全算法。
##### Replayed S1 UE security capabilities 
IE|说明
---|---
Replayed S1 UE security capabilities|Replayed S1 UE security capabilities信元用于网络指示UE在S1模式、Iu模式和Gb模式下支持的安全算法。若安全性算法支持S1模式则同样支持NAS和AS安全性。若UE支持S101模式，则这些安全性算法也支持S101模式下的NAS安全。
##### Registration accept message identity 
IE|说明
---|---
Registration accept message identity|该信元为message type类型，取值是Registration accept。
##### Registration request message identity 
IE|说明
---|---
Registration request message identity|该信元为message type类型，取值是Registration request。
##### Registration complete message identity 
IE|说明
---|---
Registration complete message identity|该信元为message type类型，取值是Registration complete。
##### Registration reject message identity 
IE|说明
---|---
Registration reject message identity|该信元为message type类型，取值是Registration reject。
##### Requested QoS rules 
IE|说明
---|---
Requested QoS rules|QoS规则信元用于指示UE使用的一组QoS规则。
##### Requested QoS flow descriptions 
IE|说明
---|---
Requested QoS flow descriptions|QoS flow descriptions信元用于表示UE使用的QoS流描述的集合，每个QoS流描述包含一组参数集合。
##### Requested DRX parameters 
IE|说明
---|---
Requested DRX parameters|Requested DRX parameters信元用于表示UE请求的DRX参数，或网络在寻呼时使用的DRX周期值。该信元为4类信元，长度为3字节。
##### Requested NSSAI 
IE|说明
---|---
Requested NSSAI|当5GS注册类型为“初始注册”或“移动注册更新”，并且满足如下条件时，会携带此IE：UE对当前PLMN有配置的NSSAI；UE对当前PLMN具有允许的NSSAI；UE既没有当前PLMN的允许的NSSAI，也没有当前PLMN的Configured NSSAI，但是有默认配置的NSSAI。
##### Rejected NSSAI 
IE|说明
---|---
Rejected NSSAI|Rejected NSSAI信元用于标识一组被拒绝S-NSSAI的集合。
S-NSSAI :IE|说明
---|---
S-NSSAI|S-NSSAI信元用于标识一个网络切片。
##### Sequence number 
IE|说明
---|---
Sequence number|Sequence number信元包含NAS消息序列号（SN）。该序列号由NAS COUNT for a SECURITY PROTECTED 5GS NAS MESSAGE消息的NAS COUNT的8个最低有效位组成。
##### Service type 
IE|说明
---|---
Service type|Service type信元用于明确服务请求流程的目的。
##### Session AMBR 
IE|说明
---|---
Session AMBR|Session-AMBR信元用于表示UE建立PDU会话时指示初始签约的PDU会话聚合最大比特速率，或者在网络改变PDU会话聚合最大比特速率时指示新签约的PDU会话聚合最大比特速率。
##### Service accept message identity 
IE|说明
---|---
Service accept message identity|该信元为message type类型，取值是Service accept。
##### Service request message identity 
IE|说明
---|---
Service request message identity|该信元为message type类型，取值是Service request。
##### Security header type 
IE|说明
---|---
Security header type|每个5GMM消息的第二个字节的bit1 ~ bit4包含安全头类型IE，该IE包含5GMM消息的安全保护相关的控制信息，安全头类型IE的总大小为4 bit。
##### Selected NAS security algorithms 
IE|说明
---|---
Selected NAS security algorithms|Selected NAS security algorithms信元表示用于加密和完整性保护的5G算法。
##### Selected EPS NAS security algorithms 
IE|说明
---|---
Selected EPS NAS security algorithms|NAS security algorithms信元用于表示用于加密和完整性保护的4G算法。
##### Selected PDU session type 
IE|说明
---|---
Selected PDU session type|PDU session type信元IE用于表示PDU会话类型。
##### Selected SSC mode 
IE|说明
---|---
Selected SSC mode|SSC mode信元用于表示SSC模式。
##### Security mode command message identity 
IE|说明
---|---
Security mode command message identity|该信元为message type类型，取值是Security mode command。
##### Security mode reject message identity 
IE|说明
---|---
Security mode reject message identity|该信元为message type类型，取值是Security mode reject。
##### Security mode complete message identity 
IE|说明
---|---
Security mode complete message identity|该信元为message type类型，取值是Security mode complete。
##### SM PDU DN request container 
IE|说明
---|---
SM PDU DN request container|本信元通过网络接入标识 (NAI) 格式携带UE标识，不同数据网络下，UE标识不同。
##### S1 UE network capability 
IE|说明
---|---
S1 UE network capability|S1 UE network capability信元用于向网络提供UE在EPS或GPRS互操作网络方面的信息，其内容可能会影响网络处理UE操作的方式，UE网络能力信息表示UE的一般特征，因此，除了显式指示的字段外，不依赖于发送信道的频段。
##### SMS indication 
IE|说明
---|---
SMS indication|SMS indication信元表示UE在NAS上使用SMS的能力发生变化。
##### SSC mode 
IE|说明
---|---
SSC mode|SSC mode信元用于表示SSC模式。
##### Service area list 
IE|说明
---|---
Service area list|Service area list信元用于表示将允许区域的允许跟踪区域列表或不允许区域的禁止跟踪区域列表从网络传输给UE。
##### Spare half octet 
IE|说明
---|---
Spare half octet|当使用奇数个half octet type 1信元时，5GMM和5GSM消息的描述中包含该IE。除非另有说明，该IE备用位设置为0，并配置在字节的比特位5到8。
##### Short name for network 
IE|说明
---|---
Short name for network|Short name for network信元表示网络短名称。
##### SOR transparent container 
IE|说明
---|---
SOR transparent container|REGISTRATION ACCEPT消息中携带该信元用于提供优选的PLMN/接入技术组合列表（HPLMN指示UE存储的“运营商控制PLMN选择器与接入技术”列表未改变时，不提供优选PLMN/接入技术组合列表）和可选的确认请求，REGISTRATION COMPLETE消息中携带该信元表示UE成功接收到REGISTRATION ACCEPT消息中的SOR transparent container信元。
##### TAI list 
IE|说明
---|---
TAI list|TAI list信元用于将网络中的跟踪区域列表传递给UE。
##### T3346 value 
IE|说明
---|---
T3346 value|T3346超时时，网络侧主动发去注册请求。
##### T3502 value 
IE|说明
---|---
T3502 value|当T3502超时时，UE再次触发注册流程。
##### T3512 value 
IE|说明
---|---
T3512 value|当T3512超时时，如果UE未注册紧急业务，则发起周期性注册流程。如果UE已注册紧急业务，则发起本地去注册流程。
##### UE security capability 
IE|说明
---|---
UE security capability|UE security capability信元用于UE和网络指示UE在N1模式下支持的NAS安全算法，以及用于5GCN连接的NR和E-UTRA上AS安全所支持的安全算法。
##### UE's usage setting 
IE|说明
---|---
UE's usage setting|UE's usage setting信元用于向网络提供3GPP协议24.301【15】中定义的UE使用设置（UE's usage setting）。网络使用UE的使用设置选择RFSP索引。
##### UE status 
IE|说明
---|---
UE status|UE status信元用于向网络提供用于当前UE的注册状态，以便于EPS交互。
##### Universal time and local time zone 
IE|说明
---|---
Universal time and local time zone|Universal time and local time zone信元表示传递时间和时区给UE。
##### UL NAS TRANSPORT message identity 
IE|说明
---|---
UL NAS TRANSPORT message identity|该信元为message type类型，取值是UL NAS TRANSPORT。
##### Uplink data status 
IE|说明
---|---
Uplink data status|Uplink data status信元用于向网络指示有上行数据待处理的PDU会话。该信元为4类信元，最小长度为4字节，最大长度为34字节。
### N2接口 
#### N2接口协议简介 
场景描述 :N2接口为(R)AN和AMF间的信令面接口。 
协议栈 :N2接口协议栈如[图1](#T_1608024222398__ab39133a-611f-4d71-abb8-d60f2eaaf5e6)所示。
图1  N2接口协议栈
[]images/image.png)
##### 消息列表 
N2接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
PDU SESSION RESOURCE SETUP REQUEST|AMF -> NG-RAN node|该消息由AMF发送，用于请求NG-RAN节点为一个或多个PDU会话资源在Uu和NG-U接口上分配资源。
PDU SESSION RESOURCE SETUP RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于回复为一个或多个PDU会话分配Uu和NG-U接口资源的请求。
PDU SESSION RESOURCE RELEASE COMMAND|AMF -> NG-RAN node|该消息由AMF发送，用于请求NG-RAN节点释放为给定UE建立的PDU会话资源。
PDU SESSION RESOURCE RELEASE RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于响应释放UE的PDU会话资源的请求。
PDU SESSION RESOURCE MODIFY REQUEST|AMF -> NG-RAN node|该消息由AMF发送，用于请求NG-RAN节点对给定UE已经建立的PDU会话资源进行修改。
PDU SESSION RESOURCE MODIFY RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于上报PDU会话资源修改请求消息的结果。
PDU SESSION RESOURCE NOTIFY|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于在GBR QoS流已经被请求启用通知后，由NG-RAN通知该QoS流的QoS需求不再满足或者由NG-RAN节点重新满足。该消息也可以由NG-RAN节点发送，用于通知给定UE的PDU会话资源已释放。
PDU SESSION RESOURCE MODIFY INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于请求AMF对给定UE的已建立的PDU会话资源进行修改。
PDU SESSION RESOURCE MODIFY CONFIRM|AMF -> NG-RAN node|该消息由AMF发送，用于从PDU会话资源修改指示消息中确认请求的结果。
INITIAL CONTEXT SETUP REQUEST|AMF -> NG-RAN node|该消息由AMF发送，请求建立UE上下文。
INITIAL CONTEXT SETUP RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于确认UE上下文建立。
UE CONTEXT RELEASE REQUEST|NG-RAN node -> AMF|该消息由NG-RAN节点发送，请求释放UE相关的NG接口逻辑连接。
UE CONTEXT RELEASE COMMAND|AMF -> NG-RAN node|该消息由AMF发送，用于请求释放UE相关的NG接口的逻辑连接。
UE CONTEXT RELEASE COMPLETE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于确认UE相关的NG接口逻辑连接已释放。
UE CONTEXT MODIFICATION REQUEST|AMF -> NG-RAN node|该消息由AMF发送，用于向NG-RAN节点提供UE上下文信息变更。
UE CONTEXT MODIFICATION RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于确认UE上下文已更新。
UE CONTEXT MODIFICATION FAILURE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于表明UE上下文更新失败。
RRC INACTIVE TRANSITION REPORT|NG-RAN node -> AMF|该消息由NG-RAN节点通知5GC，UE已进入或离开RRC_INACTIVE状态。
HANDOVER REQUIRED|NG-RAN node -> AMF|为用户请求目标侧的切换资源准备。
HANDOVER COMMAND|AMF ->NG-RAN node|向源侧通告目标侧资源已准备好。
HANDOVER PREPARATION FAILURE|AMF -> NG-RAN node|向源侧通告切换准备失败。
HANDOVER REQUEST|AMF -> NG-RAN node|向目标侧请求切换资源准备。
HANDOVER REQUEST ACKNOWLEDGE|NG-RAN node -> AMF|返回目标侧切换资源准备情况。
HANDOVER FAILURE|NG-RAN node -> AMF|返回目标侧切换资源准备失败原因。
HANDOVER NOTIFY|NG-RAN node -> AMF|目标侧通知AMF用户切换完成。
PATH SWITCH REQUEST|NG-RAN node -> AMF|为用户请求下行GTP隧道终点迁移。
PATH SWITCH REQUEST ACKNOWLEDGE|AMF ->NG-RAN node|返回PATH SWITCH REQUEST消息的请求结果。
PATH SWITCH REQUEST FAILURE|AMF -> NG-RAN node|AMF向(R)AN通知路径切换失败。
HANDOVER CANCEL|NG-RAN node ->AMF|源侧通告AMF切换取消。
HANDOVER CANCEL ACKNOWLEDGE|AMF -> NG-RAN node|AMF向源侧确认切换已取消。
UPLINK RAN STATUS TRANSFER|NG-RAN node -> AMF|该消息由NG-RAN节点发送给AMF。
DOWNLINK RAN STATUS TRANSFER|AMF -> NG-RAN node|该消息由AMF发送给NG-RAN节点。
PAGING|AMF ->NG-RAN node|该消息由AMF发送，用于在一个或多个跟踪区域寻呼UE。
INITIAL UE MESSAGE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于通过NG接口向AMF发送初始层3消息。
DOWNLINK NAS TRANSPORT|AMF -> NG-RAN node|该消息由AMF发送，用于在NG接口上携带NAS信息。
UPLINK NAS TRANSPORT|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于在NG接口上携带NAS信息。
NAS NON DELIVERY INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于在NG接口下行NAS传输消息中上报之前发送的NAS PDU未正常收到。
REROUTE NAS REQUEST|AMF -> NG-RAN node|该消息由AMF发送，用于请求INITIAL UE MESSAGE消息重路由到另一个AMF。
NG SETUP REQUEST|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于为NG-C接口实例发送应用层信息。
NG SETUP RESPONSE|AMF -> NG-RAN node|该消息由AMF发送，用于为NG-C接口实例发送应用层信息。
NG SETUP FAILURE|AMF -> NG-RAN node|该消息由AMF发送，用于指示NG建立失败。
RAN CONFIGURATION UPDATE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于为NG-C接口实例发送更新的应用层信息。
RAN CONFIGURATION UPDATE ACKNOWLEDGE|AMF -> NG-RAN node|该消息由AMF发送，用于确认NG-C接口实例的NG-RAN节点更新信息。
RAN CONFIGURATION UPDATE FAILURE|AMF -> NG-RAN node|该消息由AMF发送，用于指示RAN配置更新失败。
AMF CONFIGURATION UPDATE|AMF -> NG-RAN node|该消息由AMF发送，用于为NG-C接口实例发送更新信息。
AMF CONFIGURATION UPDATE ACKNOWLEDGE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于确认AMF为NG-C接口实例发送的更新信息。
AMF CONFIGURATION UPDATE FAILURE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于指示AMF配置更新失败。
AMF STATUS INDICATION|AMF -> NG-RAN node|该消息由AMF发送，用于支持AMF管理功能。
NG RESET|NG-RAN node -> AMF and AMF -> NG-RAN node|该消息由NG-RAN和AMF发送，用于请求复位所有或部分NG接口。
NG RESET ACKNOWLEDGE|NG-RAN node -> AMF and AMF -> NG-RAN node|该消息由NG-RAN和AMF发送，用于回复NG RESET消息。
ERROR INDICATION|NG-RAN node -> AMF and AMF -> NG-RAN node|该消息由NG-RAN和AMF发送，表示该节点已经检测到错误。
OVERLOAD START|AMF -> NG-RAN node|该消息由AMF发送，用于向NG-RAN节点指示AMF过载。
OVERLOAD STOP|AMF -> NG-RAN node|该消息由AMF发送，用于指示AMF过载消除。
UPLINK RAN CONFIGURATION TRANSFER|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于发送NG-RAN配置信息。
DOWNLINK RAN CONFIGURATION TRANSFER|AMF -> NG-RAN node|该消息由AMF发送，用于发送NG-RAN配置信息。
WRITE-REPLACE WARNING REQUEST|AMF -> NG-RAN node|该消息由AMF发送，请求开始广播警告消息或覆盖警告消息的广播。
WRITE-REPLACE WARNING RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于向AMF确认警告消息的开始广播或覆盖请求。
PWS CANCEL REQUEST|AMF -> NG-RAN node|该消息由AMF转发给NG-RAN节点，用于取消正在进行的警告消息广播。
PWS CANCEL RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于指示取消已识别消息的广播成功和失败的警告区域列表。
PWS RESTART INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于向AMF告知NG-RAN节点的部分或全部小区的PWS信息可从CBC重新加载，如果需要的话。
PWS FAILURE INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，通知AMF该NG-RAN节点一个或多个小区正在进行的PWS操作失败。
DOWNLINK UE ASSOCIATED NRPPA TRANSPORT|AMF -> NG-RAN node|该消息由AMF发送，用于携带通过NG接口发送的NRPPA消息。
UPLINK UE ASSOCIATED NRPPA TRANSPORT|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于携带通过NG接口发送的NRPPA消息。
DOWNLINK NON UE ASSOCIATED NRPPA TRANSPORT|AMF -> NG-RAN node|该消息由AMF发送，用于携带通过NG接口发送的NRPPA消息。
UPLINK NON UE ASSOCIATED NRPPA TRANSPORT|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于携带通过NG接口发送的NRPPA信息。
TRACE START|AMF -> NG-RAN node|该消息由AMF发送，用于为UE发起一个跟踪会话。
TRACE FAILURE INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于指示UE的跟踪启动流程或去激活跟踪流程失败。
DEACTIVATE TRACE|AMF -> NG-RAN node|该消息由AMF发送，用于去激活跟踪会话。
CELL TRAFFIC TRACE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于传递特定跟踪信息。
LOCATION REPORTING CONTROL|AMF -> NG-RAN node|该消息用于AMF请求NG-RAN上报UE位置信息。
LOCATION REPORTING FAILURE INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于指示位置上报失败。
LOCATION REPORT|NG-RAN node -> AMF|该消息用于提供UE的位置信息。
UE TNLA BINDING RELEASE REQUEST|AMF -> NG-RAN node|该消息由AMF发送，用于请求NG-RAN节点为UE解除TNLA绑定关系。
UE RADIO CAPABILITY INFO INDICATION|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于向AMF提供UE无线能力相关信息。
UE RADIO CAPABILITY CHECK REQUEST|AMF -> NG-RAN node|该消息由AMF发送，用于请求NG-RAN节点检查UE无线能力与IMS语音业务的网络配置之间的兼容性。
UE RADIO CAPABILITY CHECK RESPONSE|NG-RAN node -> AMF|该消息由NG-RAN节点发送，用于上报UE无线能力与网络配置之间的IMS语音兼容性。
#### 相关消息解释 
##### PDU Session Resource Setup Request 


消息功能 :该消息由AMF发送，用于请求NG-RAN节点为一个或多个PDU会话资源在Uu和NG-U接口上分配资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN Paging Priority|Optional|该IE包含业务优先级。
NAS-PDU|Optional|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
PDU Session Resource Setup Request List|NA|PDU会话资源建立请求列表。
>PDU Session Resource SetupRequest Item|NA|PDU会话资源建立请求项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session NAS-PDU|Optional|该IE在中携带5GC发送给UE或者UE发送给5GC的消息，NG-RAN节点透传此消息。
>>S-NSSAI|Mandatory|单网络切片标识。
>>PDU Session Resource Setup Request Transfer|Mandatory|SMF通过AMF透传给NG-RAN的PDU Session Resource Setup Request TransferIE。


##### PDU Session Resource Setup Response 


消息功能 :该消息由NG-RAN节点发送，用于回复为一个或多个PDU会话分配Uu和NG-U接口资源的请求。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Setup Response List|NA|PDU会话资源建立响应列表。
>PDU Session Resource Setup Response Item|NA|PDU会话资源建立响应项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Setup Response Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Setup Response TransferIE。
PDU Session Resource Failed to Setup List|NA|PDU会话资源建立失败列表。
>PDU Session Resource Failed to Setup Item|NA|PDU会话资源建立失败项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Setup Unsuccessful Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Setup UnsuccessfulTransfer IE。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### PDU Session Resource Release Command 


消息功能 :该消息由AMF发送，用于请求NG-RAN节点释放为给定UE建立的PDU会话资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN Paging Priority|Optional|该IE包含业务优先级。
NAS-PDU|Optional|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
PDU Session Resource to Release List|NA|PDU会话资源释放列表。
>PDU Session Resource to Release Item|NA|PDU会话资源释放列表。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Release Command Transfer|Mandatory|SMF通过AMF透传给NG-RAN的PDU Session Resource Release Command TransferIE。


##### PDU Session Resource Release Response 


消息功能 :该消息由NG-RAN节点发送，用于响应释放UE的PDU会话资源的请求。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource to Release List|NA|PDU会话资源释放列表。
>PDU Session Resource to Release Item|NA|PDU会话资源释放列表。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Release Command Transfer|Mandatory|SMF通过AMF透传给NG-RAN的PDU Session Resource Release Command TransferIE。
User Location Information|Optional|该IE用于提供UE的位置信息。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### PDU Session Resource Modify Request 


消息功能 :该消息由AMF发送，用于请求NG-RAN节点对给定UE已经建立的PDU会话资源进行修改。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN Paging Priority|Optional|该IE包含业务优先级。
PDU Session Resource to Release List|NA|PDU会话资源释放列表。
>PDU Session Resource to Release Item|NA|PDU会话资源释放列表。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>NAS-PDU|Optional|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
>>PDU Session Resource Modify Request Transfer|Mandatory|SMF通过AMF透传给NG-RAN的PDU Session Resource Modify Request TransferIE。


##### PDU Session Resource Modify Response 


消息功能 :该消息由NG-RAN节点发送，用于上报PDU会话资源修改请求消息的结果。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Modify Response List|NA|PDU会话资源修改响应列表。
>PDU Session Resource Modify Response Item|NA|PDU会话资源修改响应项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Modify Response Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Modify Response TransferIE。
PDU Session Resource Failed to Modify List|NA|PDU会话资源修改失败列表。
>PDU Session Resource Failed to Modify Item|NA|PDU会话资源修改失败项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Modify Unsuccessful Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Modify UnsuccessfulTransfer IE。
User Location Information|Optional|该IE用于提供UE的位置信息。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### PDU Session Resource Notify 


消息功能 :该消息由NG-RAN节点发送，用于在GBR QoS流已经被请求启用通知后，由NG-RAN通知该QoS流的QoS需求不再满足或者由NG-RAN节点重新满足。该消息也可以由NG-RAN节点发送，用于通知给定UE的PDU会话资源已释放。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Notify List|NA|PDU会话资源通知列表。
>PDU Session Resource Notify Item|NA|PDU会话资源通知项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Notify Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Notify Transfer IE。
PDU Session Resource Released List|NA|释放的PDU会话资源列表。
>PDU Session Resource Released Item|NA|释放的PDU会话资源项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Notify Released Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Notify Released TransferIE。
User Location Information|Optional|该IE用于提供UE的位置信息。


##### PDU Session Resource Modify Indication 


消息功能 :该消息由NG-RAN节点发送，用于请求AMF对给定UE的已建立的PDU会话资源进行修改。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Modify Indication List|NA|PDU会话资源修改指示列表。
>PDU Session Resource Modify Indication Item|NA|PDU会话资源修改指示项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Modify Indication Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Modify IndicationTransfer IE。


##### PDU Session Resource Modify Confirm 


消息功能 :该消息由AMF发送，用于从PDU会话资源修改指示消息中确认请求的结果。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Modify Confirm List|NA|PDU会话资源修改确认列表。
>PDU Session Resource Modify Confirm Item|NA|PDU会话资源修改确认项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Modify Confirm Transfer|Mandatory|该IE在AMF节点不解析。
PDU Session Resource Failed to Modify List|NA|PDU会话资源修改列表失败。
>PDU Session Resource Failed to Modify Item|NA|PDU会话资源修改列表项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Modify Indication Unsuccessful Transfer|Mandatory|SMF通过AMF透传给NG-RAN的PDU Session Resource Modify IndicationUnsuccessful Transfer IE。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Initial Context Setup Request 


消息功能 :该消息由AMF发送，请求建立UE上下文。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Old AMF|Optional|该IE表示旧的AMF的名称。
UE Aggregate Maximum Bit Rate|Conditional|该IE适用于下行和上行方向定义的所有non-GBR QoS流，以及AMF提供给NG-RAN节点的签约参数。
Core Network Assistance Information|Optional|该IE提供RRC_INACTIVE配置等辅助信息。
GUAMI|Mandatory|该IE表示AMF标识。
PDU Session Resource Setup Request List|NA|PDU会话资源建立请求列表。
>PDU Session Resource Setup Request Item|NA|PDU会话资源建立请求项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>NAS-PDU|Optional|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
>>S-NSSAI|Mandatory|Single Network Slice Selection Assistance Information，该IE表示单网络切片选择辅助信息。
>>PDU Session Resource Setup Request Transfer|Mandatory|SMF通过AMF透传给NG-RAN的PDU Session Resource Setup Request TransferIE。
Allowed NSSAI|Mandatory|该IE包含允许的NSSAI。
UE Security Capabilities|Mandatory|该IE定义了UE支持的加密和完整性保护算法。
Security Key|Mandatory|该IE用于NG-RAN不同场景下的安全应用。
Trace Activation|Optional|该IE定义了跟踪会话激活的相关参数。
Mobility Restriction List|Optional|该IE定义了后续移动动作的接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。
UE Radio Capability|Optional|该IE包含UE的无线能力信息。
Index to RAT/Frequency Selection Priority|Optional|该IE用于定义RRM策略的本地配置，如空闲模式下的驻留优先级、主动模式下的RAT间、频率间切换控制等。
Masked IMEISV|Optional|该IE包含带有掩码的IMEISV值，用来标识一个终端型号，而不需要识别单个移动设备。
NAS-PDU|Optional|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
Emergency Fallback Indicator|Optional|该IE表示紧急业务回落。
RRC Inactive Transition Report Request|Optional|该IE用于请求NG-RAN节点在UE进入或离开RRC_INACTIVE状态时向5GC上报或停止上报。
UE Radio Capability for Paging|Optional|该IE包含寻呼特定UE无线能力信息。


##### Initial Context Setup Response 


消息功能 :该消息由NG-RAN节点发送，用于确认UE上下文建立。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Setup Response List|NA|PDU会话资源建立响应列表。
>PDU Session Resource Setup Response Item|NA|PDU会话资源建立响应项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Setup Response Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Setup Response TransferIE。
PDU Session Resource Failed to Setup List|NA|PDU会话资源建立失败列表。
>PDU Session Resource Failed to Setup Item|NA|PDU会话资源建立失败项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>PDU Session Resource Setup Unsuccessful Transfer|Mandatory|NG-RAN通过AMF透传给SMF的PDU Session Resource Setup UnsuccessfulTransfer IE。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### UE Context Release Request 


消息功能 :该消息由NG-RAN节点发送，请求释放UE相关的NG接口逻辑连接。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource List|NA|PDU会话资源列表。
>PDU Session Resource Item|NA|PDU会话资源项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。


##### UE Context Release Command 


消息功能 :该消息由AMF发送，用于请求释放UE相关的NG接口的逻辑连接。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
CHOICE UE NGAP IDs|Mandatory|UE NGAP ID选项。
>UE NGAP ID pair|NA|UE NGAP ID对。
>>AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
>>RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
>AMF UE NGAP ID|NA|该IE在AMF内唯一标识UE在NG接口上的关联。
>>AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。


##### UE Context Release Complete 


消息功能 :该消息由NG-RAN节点发送，用于确认UE相关的NG接口逻辑连接已释放。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
User Location Information|Optional|该IE用于提供UE的位置信息。
Information on Recommended Cells and RAN Nodes for Paging|Optional|该IE提供了寻呼推荐小区和NG-RAN节点信息。
PDU Session Resource List|NA|PDU会话资源列表。
>PDU Session Resource Item|NA|PDU会话资源项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### UE Context Modification Request 


消息功能 :该消息由AMF发送，用于向NG-RAN节点提供UE上下文信息变更。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN Paging Priority|Optional|该IE包含业务优先级。
Security Key|Optional|该IE用于NG-RAN不同场景下的安全应用。
Index to RAT/Frequency Selection Priority|Optional|该IE用于定义RRM策略的本地配置，如空闲模式下的驻留优先级、主动模式下的系统内、系统间切换控制等。
UE Aggregate Maximum Bit Rate|Optional|该信元适用于下行和上行方向定义的所有non-GBR QoS流，以及AMF提供给NG-RAN节点的签约参数。
UE Security Capabilities|Optional|该IE定义了UE支持的加密和完整性保护算法。该IE表示AMF标识。
Core Network Assistance Information|Optional|该IE提供RRC_INACTIVE配置等辅助信息。
Emergency Fallback Indicator|Optional|该IE表示紧急业务回落。
New AMF UE NGAP ID|Optional|该IE在AMF内唯一标识UE在NG接口上的关联。
RRC Inactive Transition Report Request|Optional|该IE用于请求NG-RAN节点在UE进入或离开RRC_INACTIVE状态时向5GC上报或停止上报。


##### UE Context Modification Response 


消息功能 :该消息由NG-RAN节点发送，用于确认UE上下文已更新。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RRC State|Optional|该IE表示UE的RRC状态。
User Location Information|Optional|该IE用于提供UE的位置信息。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### UE Context Modification Failure 


消息功能 :该消息由NG-RAN节点发送，用于表明UE上下文更新失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### RRC Inactive Transition Report 


消息功能 :该消息由NG-RAN节点通知5GC，UE已进入或离开RRC_INACTIVE状态。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RRC State|Mandatory|该IE表示UE的RRC状态。
User Location Information|Mandatory|该IE用于提供UE的位置信息。


##### Handover Required 


消息功能 :该消息由源NG-RAN节点发送给AMF，请求目标NG-RAN准备切换资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Handover Type|Mandatory|该IE表示源侧触发了哪种切换。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Target ID|Mandatory|该IE标识切换的目标，Target ID可以是NG-RAN，也可以是E-UTRAN。
Direct Forwarding Path Availability|Optional|该IE指示是否有直接转发路径。
PDU Session Resource List|NA|PDU会话资源列表。
>PDU Session Resource Item|NA|PDU会话资源项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Handover Required Transfer|Mandatory|NG-RAN通过AMF透传给SMF的Handover Required Transfer IE。
Source to Target Transparent Container|Mandatory|该IE用于通过核心网将无线相关信息从切换源侧透传给切换目标侧；由源侧RAN节点产生，并发送到目标侧RAN节点。


##### Handover Command 


消息功能 :该消息由AMF通知源NG-RAN节点，目标NG-RAN已经准备好切换资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Handover Type|Mandatory|该IE表示源侧触发了哪种切换。
NAS Security Parameters from NG-RAN|NA|该IE提供了从NG-RAN到E-UTRAN通过eNB到UE的系统间切换的安全相关参数。
PDU Session Resource HandoverList|NA|PDU会话资源切换列表。
>PDU Session Resource HandoverItem|NA|PDU会话资源切换项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Handover Command Transfer|Mandatory|SMF通过AMF透传给NG-RAN的Handover Command Transfer IE。
PDU Session Resource to Release List|NA|PDU会话资源释放列表。
>PDU Session Resource to Release Item|NA|PDU会话资源释放项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Handover Preparation Unsuccessful Transfer|Mandatory|SMF通过AMF透传给NG-RAN的Handover Preparation Unsuccessful TransferIE。
Target to Source Transparent Container|Mandatory|该IE用于通过核心网将无线相关信息从切换目标侧透传给切换源侧；由目标侧RAN节点产生，并发送到源侧RAN节点。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Handover Preparation Failure 


消息功能 :该消息由AMF发送，用于通知源NG-RAN节点切换准备失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Handover Request 


消息功能 :该消息由AMF发送给目标NG-RAN节点，请求准备切换资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
Handover Type|Mandatory|该IE表示源侧触发了哪种切换。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
UE Aggregate Maximum Bit Rate|Mandatory|该信元适用于下行和上行方向定义的所有non-GBR QoS流，以及AMF提供给NG-RAN节点的签约参数。
Core Network Assistance Information|Optional|该IE提供RRC_INACTIVE配置等辅助信息。
UE Security Capabilities|Mandatory|该IE定义了UE支持的加密和完整性保护算法。该IE表示AMF标识。
Security Context|Mandatory|该IE为NG-RAN节点提供安全相关参数，用于衍生用户面流量和RRC信令消息的安全密钥，为后续的移动性生成安全参数。
New Security Context Indicator|Optional|该IE表示AMF已经激活了一个新的5G NAS安全上下文。
NASC|Optional|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
PDU Session Resource Setup List|NA|PDU会话资源建立列表。
>PDU Session Resource Setup Item|NA|PDU会话资源建立项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>S-NSSAI|Mandatory|Single Network Slice Selection Assistance Information，该IE表示单网络切片选择辅助信息。
>>Handover Request Transfer|Mandatory|SMF通过AMF透传给NG-RAN的Handover Request Transfer IE。
Allowed NSSAI|Mandatory|该IE包含允许的NSSAI。
Trace Activation|Optional|该IE定义了跟踪会话激活的相关参数。
Masked IMEISV|Optional|该IE包含带有掩码的IMEISV值，用来标识一个终端型号，而不需要识别单个移动设备。
Source to Target Transparent Container|Mandatory|该IE用于通过核心网将无线相关信息从切换源侧透传给切换目标侧；由源侧RAN节点产生，并发送到目标侧RAN节点。
Mobility Restriction List|Optional|该IE定义了后续移动动作的漫游或接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。
Location Reporting Request Type|Optional|该IE表示NG-RAN节点需要处理的位置请求类型。
RRC Inactive Transition Report Request|Optional|该IE用于请求NG-RAN节点在UE进入或离开RRC_INACTIVE状态时向5GC上报或停止上报。
GUAMI|Mandatory|该IE表示AMF标识。


##### Handover Request Acknowledge 


消息功能 :该消息由目标NG-RAN节点发送，用于通知AMF目标NG-RAN已经准备好切换资源。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Admitted List|NA|PDU会话资源准入列表。
>PDU Session Resource Admitted Item|NA|PDU会话资源准入项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Handover Request Acknowledge Transfer|Mandatory|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge TransferIE。
PDU Session Resource Failed to Setup List|NA|PDU会话资源建立失败列表。
>PDU Session Resource Failed to Setup Item|NA|PDU会话资源建立失败项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Handover Resource Allocation Unsuccessful Transfer|Mandatory|NG-RAN通过AMF透传给SMF的Handover Resource Allocation UnsuccessfulTransfer IE。
Target to Source Transparent Container|Mandatory|该IE用于通过核心网将无线相关信息从切换目标侧透传给切换源侧；由目标侧RAN节点产生，并发送到源侧RAN节点。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Handover Failure 


消息功能 :该消息由目标NG-RAN节点发送，通知AMF资源准备失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Handover Notify 


消息功能 :该消息由目标NG-RAN节点发送，通知AMF已在目标小区识别UE且切换完成。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
User Location Information|Mandatory|该IE用于提供UE的位置信息。


##### Path Switch Request 


消息功能 :该消息由NG-RAN节点通知AMF新服务的NG-RAN节点，并通过AMF将部分NG-U下行隧道终结点发送给SMF，供一个或多个PDU会话资源使用。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Source AMF UE NGAP ID|Mandatory|该IE在AMF内部唯一标识一个NG接口的UE关联。
User Location Information|Mandatory|该IE用于提供UE的位置信息。
UE Security Capabilities|Mandatory|该IE定义了UE支持的加密和完整性保护算法。该IE表示AMF标识。
PDU Session Resource to be Switched in Downlink List|NA|下行中需要切换的PDU会话资源列表。
>PDU Session Resource to be Switched in Downlink Item|NA|下行中需要切换的PDU会话资源项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Path Switch Request Transfer|Mandatory|NG-RAN通过AMF透传给SMF的Path Switch Request Transfer IE。
PDU Session Resource Failed to Setup List|NA|PDU会话资源建立失败列表。
>PDU Session Resource Failed to Setup Item|NA|PDU会话资源建立失败项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Path Switch Request Setup Failed Transfer|Mandatory|NG-RAN通过AMF透传给SMF的Path Switch Request Setup Failed TransferIE。


##### Path Switch Request Acknowledge 


消息功能 :该消息由AMF发送，用于通知NG-RAN节点5GC路径切换成功。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
UE Security Capabilities|Optional|该IE定义了UE支持的加密和完整性保护算法。该IE表示AMF标识。
Security Context|Mandatory|该IE为NG-RAN节点提供安全相关参数，用于衍生用户面流量和RRC信令消息的安全密钥，为后续的移动性生成安全参数。
New Security Context Indicator|Optional|该IE表示AMF已经激活了一个新的5G NAS安全上下文。
PDU Session Resource Switched List|NA|PDU会话资源切换列表。
>PDU Session Resource Switched Item|NA|PDU会话资源切换项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Path Switch Request Acknowledge Transfer|Mandatory|SMF通过AMF透传给NG-RAN的Path Switch Request Acknowledge TransferIE。
PDU Session Resource Released List|NA|PDU会话资源释放列表。
>PDU Session Resource Released Item|NA|PDU会话资源释放项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Path Switch Request Unsuccessful Transfer|Mandatory|SMF通过AMF透传给NG-RAN的Path Switch Request Unsuccessful TransferIE。
Allowed NSSAI|Mandatory|该IE包含允许的NSSAI。
Core Network Assistance Information|Optional|该IE提供RRC_INACTIVE配置等辅助信息。
RRC Inactive Transition Report Request|Optional|该IE用于请求NG-RAN节点在UE进入或离开RRC_INACTIVE状态时向5GC上报或停止上报。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Path Switch Request Failure 


消息功能 :该消息由AMF发送，用于通知NG-RAN节点，在路径切换请求流程中5GC发生故障。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
PDU Session Resource Released List|NA|PDU会话资源释放列表。
>PDU Session Resource Released Item|NA|PDU会话资源释放项。
>>PDU Session ID|Mandatory|该IE用于标识一个UE的PDU会话。
>>Path Switch Request Unsuccessful Transfer|Mandatory|SMF通过AMF透传给NG-RAN的Path Switch Request Unsuccessful TransferIE。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Handover Cancel 


消息功能 :该消息由源NG-RAN节点发送给AMF，用于请求取消正在进行的切换。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。


##### Handover Cancel Acknowledge 


消息功能 :该消息由AMF发送给源NG-RAN节点，确认正在进行的切换被取消。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Uplink Ran Status Transfer 
消息功能 :该消息由NG-RAN节点发送给AMF。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN Status Transfer Transparent Container|Mandatory|该IE由源NGRAN节点产生，传递到目标NGRAN节点，用于5GC内部NG切换。
##### Downlink Ran Status Transfer 


消息功能 :该消息由AMF发送给NG-RAN节点。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN Status Transfer Transparent Container|Mandatory|该IE由源NGRAN节点产生，传递到目标NGRAN节点，用于5GC内部NG切换


##### Paging 


消息功能 :该消息由AMF发送，用于在一个或多个跟踪区域寻呼UE。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
UE Paging Identity|Mandatory|该IE表示UE被寻呼的标识。
Paging DRX|Optional|该IE表示寻呼DRX。
TAI List for Paging|NA|寻呼的TAI列表。
>TAI List for Paging Item|NA|寻呼的TAI列表项。
>>TAI|Mandatory|该IE用于唯一标识一个跟踪区域。
Paging Priority|Optional|该IE表示UE的寻呼优先级。
UE Radio Capability for Paging|Optional|该IE包含寻呼特定UE无线能力信息。
Assistance Data for Paging|Optional|该IE为寻呼优化提供辅助信息。
Paging Origin|Optional|该信元指示是否由于非3GPP接入的PDU会话而发起寻呼。


##### Initial UE Message 


消息功能 :该消息由NG-RAN节点发送，用于通过NG接口向AMF发送初始层3消息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
NAS-PDU|Mandatory|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
User Location Information|Mandatory|该IE用于提供UE的位置信息。
RRC Establishment Cause|Mandatory|该IE表示EstablishmentCause中收到UE的RRC连接建立原因。
5G-S-TMSI|Optional|该IE用于安全原因，隐藏用户的身份。
AMF Set ID|Optional|该IE用于在AMF区域内唯一标识一个AMF集合。
UE Context Request|Optional|该IE表示用户上下文，包括安全信息。
Allowed NSSAI|Optional|该IE包含允许的NSSAI。


##### Downlink NAS Transport 


消息功能 :该消息由AMF发送，用于在NG接口上携带NAS信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Old AMF|Optional|该IE表示旧的AMF。
RAN Paging Priority|Optional|该IE包含业务优先级。
NAS-PDU|Mandatory|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
Mobility Restriction List|Optional|该IE定义了后续移动动作的接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。
Index to RAT/Frequency Selection Priority|Optional|该IE用于定义RRM策略的本地配置，如空闲模式下的驻留优先级、主动模式下的系统内、系统间切换控制等。
UE Aggregate Maximum Bit Rate|Optional|该信元适用于下行和上行方向定义的所有non-GBR QoS流，以及AMF提供给NG-RAN节点的签约参数。
Allowed NSSAI|Optional|该IE包含允许的NSSAI。


##### Uplink NAS Transport 


消息功能 :该消息由NG-RAN节点发送，用于在NG接口上携带NAS信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
NAS-PDU|Mandatory|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
User Location Information|Mandatory|该IE用于提供UE的位置信息。


##### Reroute NAS Request 


消息功能 :该消息由AMF发送，用于请求INITIAL UE MESSAGE消息重路由到另一个AMF。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
RAN UE NGAP ID|Optional|该IE在AMF内唯一标识UE在NG接口上的关联。
NGAP Message|Mandatory|该IE包含INITIAL UE MESSAGE。
AMF Set ID|Mandatory|该IE用于在AMF区域内唯一标识一个AMF集合。
Allowed NSSAI|Optional|该IE包含允许的NSSAI。


##### NG Setup Request 


消息功能 :该消息由NG-RAN节点发送，用于为NG-C接口实例发送应用层信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
Global RAN Node ID|Mandatory|该IE用于全局标识一个NG-RAN节点。
RAN Node Name|Optional|该IE表示无线节点名称。
Supported TA List|NA|支持的TA列表。
>Supported TA Item|NA|支持的TA项。
>>TAC|Mandatory|该IE用于唯一标识一个跟踪区域码。
>>Broadcast PLMN List|NA|广播PLMN列表。
>>>Broadcast PLMN Item|NA|广播PLMN项。
>>>>PLMN Identity|Mandatory|该IE表示PLMN标识。
>>>>TAI Slice Support List|Mandatory|该IE表示支持的slice列表。
Default Paging DRX|Mandatory|该IE表示寻呼DRX。


##### NG Setup Response 


消息功能 :该消息由AMF发送，用于为NG-C接口实例发送应用层信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF Name|Mandatory|该IE用于唯一标识AMF。
Served GUAMI List|NA|服务GUAMI列表。
>Served GUAMI Item|NA|服务GUAMI项。
>>GUAMI|Mandatory|该IE表示AMF标识。
>>Backup AMF Name|Optional|该IE用于唯一标识AMF。
Relative AMF Capacity|Mandatory|该IE指示AMF相对于其他AMF的相对处理能力。
PLMN Support List|NA|支持的PLMN列表。
>PLMN Support Item|NA|支持的PLMN项。
>>PLMN Identity|Mandatory|该IE表示PLMN标识。
>>Slice Support List|Mandatory|该IE表示支持的slice列表。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### NG Setup Failure 


消息功能 :该消息由AMF发送，用于指示NG建立失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Time to Wait|Optional|该IE定义了允许的最小等待时间。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### RAN Configuration Update 


消息功能 :该消息由NG-RAN节点发送，用于为NG-C接口实例发送更新的应用层信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
RAN Node Name|Optional|该IE表示无线节点名称。
Supported TA List|NA|支持的TA列表。
>Supported TA Item|NA|支持的TA项。
>>TAC|Mandatory|该IE用于唯一标识一个跟踪区域码。
>>Broadcast PLMN List|NA|广播PLMN列表。
>>>Broadcast PLMN Item|NA|广播PLMN项。
>>>>PLMN Identity|Mandatory|该IE表示PLMN标识。
>>>>TAI Slice Support List|Mandatory|该IE表示支持的slice列表。
Default Paging DRX|Optional|该IE表示寻呼DRX。


##### RAN Configuration Update Acknowledge 


消息功能 :该消息由AMF发送，用于确认NG-C接口实例的NG-RAN节点更新信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### RAN Configuration Update Failure 


消息功能 :该消息由AMF发送，用于指示RAN配置更新失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Time to Wait|Optional|该IE定义了允许的最小等待时间。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### AMF Configuration Update 


消息功能 :该消息由AMF发送，用于为NG-C接口实例发送更新信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF Name|Optional|该IE用于唯一标识AMF。
Served GUAMI List|NA|服务GUAMI列表。
>Served GUAMI Item|NA|服务GUAMI项。
>>GUAMI|Mandatory|该IE表示AMF标识。
>>Backup AMF Name|Optional|该IE用于唯一标识AMF。
Relative AMF Capacity|Optional|该IE指示AMF相对于其他AMF的相对处理能力。
PLMN Support List|NA|PLMN支持列表。
>PLMN Support Item|NA|PLMN支持项。
>>PLMN Identity|Mandatory|该IE表示PLMN标识。
>>Slice Support List|Mandatory|该IE表示支持的slice列表。
AMF TNL Association to Add List|NA|AMF TNL关联添加列表。
>AMF TNL Association to Add Item|NA|AMF TNL关联添加项。
>>AMF TNL Association Address|Mandatory|该IE用于提供NGRAN节点关联的NG控制面传输层信息AMF对。
>>TNL Association Usage|Optional|该IE表示TNL关联的使用情况。
>>TNL Address Weight Factor|Mandatory|该IE表示TNL地址的权重因子。
AMF TNL Association to Remove List|NA|AMF TNL关联删除列表。
>AMF TNL Association to Remove Item|NA|AMF TNL关联删除项。
>>AMF TNL Association Address|Mandatory|该IE用于提供NGRAN节点关联的NG控制面传输层信息AMF对。
AMF TNL Association to UpdateList|NA|AMF TNL关联更新列表。
>AMF TNL Association to UpdateItem|NA|AMF TNL关联更新项。
>>AMF TNL Association Address|Mandatory|该IE用于提供NGRAN节点关联的NG控制面传输层信息AMF对。
>>TNL Association Usage|Optional|该IE表示TNL关联的使用情况。
>>TNL Address Weight Factor|Optional|该IE表示TNL地址的权重因子。


##### AMF Configuration Update Acknowledge 


消息功能 :该消息由NG-RAN节点发送，用于确认AMF为NG-C接口实例发送的更新信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF TNL Association Setup List|NA|AMF TNL关联建立列表。
>AMF TNL Association Setup Item|NA|AMF TNL关联建立项。
>>AMF TNL Association Address|Mandatory|该IE用于提供NGRAN节点关联的NG控制面传输层信息AMF对。
AMF TNL Association Failed to Setup List|Optional|该IE包含TNL关联列表。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### AMF Configuration Update Failure 


消息功能 :该消息由NG-RAN节点发送，用于指示AMF配置更新失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。
Time to Wait|Optional|该IE定义了允许的最小等待时间。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


##### Uplink RAN Configuration Transfer 


消息功能 :该消息由NG-RAN节点发送，用于发送NG-RAN配置信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
SON Configuration Transfer|Optional|该IE包含配置信息。


##### Downlink RAN Configuration Transfer 


消息功能 :该消息由AMF发送，用于发送NG-RAN配置信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
SON Configuration Transfer|Optional|该IE包含配置信息。


##### Location Reporting Control 


消息功能 :该消息用于AMF请求NG-RAN上报UE位置信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Location Reporting Request Type|Mandatory|该IE表示NG-RAN节点需要处理的位置请求类型。


##### Location Reporting Failure Indication 


消息功能 :该消息由NG-RAN节点发送，用于指示位置上报失败。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
Cause|Mandatory|该IE的目的是为了指示NGAP协议特定事件的原因。


##### Location Report 


消息功能 :该消息用于提供UE的位置信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
User Location Information|Mandatory|该IE用于提供UE的位置信息。
UE Presence in Area of Interest List|Optional|该IE指示UE在兴趣区域内。
Location Reporting Request Type|Mandatory|该IE表示NG-RAN节点需要处理的位置请求类型。


##### UE Radio Capability Info Indication 


消息功能 :该消息由NG-RAN节点发送，用于向AMF提供UE无线能力相关信息。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
UE Radio Capability|Mandatory|该IE包含UE的无线能力信息。
UE Radio Capability for Paging|Optional|该IE包含寻呼特定UE无线能力信息。


##### UE Radio Capability Check Request 


消息功能 :该消息由AMF发送，用于请求NG-RAN节点检查UE无线能力与IMS语音业务的网络配置之间的兼容性。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
UE Radio Capability|Optional|该IE包含UE的无线能力信息。


##### UE Radio Capability Check Response 


消息功能 :该消息由NG-RAN节点发送，用于上报UE无线能力与网络配置之间的IMS语音兼容性。 


相关信元 :IE|Presence requirement|简要说明
---|---|---
Message Type|Mandatory|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
AMF UE NGAP ID|Mandatory|该IE在AMF内唯一标识UE在NG接口上的关联。
RAN UE NGAP ID|Mandatory|该IE唯一标识NG-RAN节点内NG接口的UE关联。
IMS Voice Support Indicator|Mandatory|该IE由NG-RAN节点设置，用于指示UE的无线能力是否与IMS语音业务的网络配置兼容。
Criticality Diagnostics|Optional|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。


#### 相关信元解释 
##### AMF UE NGAP ID 
IE|说明
---|---
AMF UE NGAP ID|该IE在AMF内唯一标识UE在NG接口上的关联。
##### Message Type 
IE|说明
---|---
Message Type|该IE唯一标识正在发送的消息，所有消息都必须携带该IE。
##### Cause 
IE|说明
---|---
Cause|该IE的目的是为了指示NGAP协议特定事件的原因。
##### Criticality Diagnostics 
IE|说明
---|---
Criticality Diagnostics|当接收到的部分消息未被理解或丢失，或者消息中包含逻辑错误时，该IE由NG-RAN或AMF发送。如果存在的话，该IE指示哪些信元未被理解或丢失。
##### RAN UE NGAP ID 
IE|说明
---|---
RAN UE NGAP ID|该IE唯一标识NG-RAN节点内NG接口的UE关联。
##### Global RAN Node ID 
IE|说明
---|---
Global RAN Node ID|该IE用于全局标识一个NGRAN节点。
##### Global gNB ID 
IE|说明
---|---
Global gNB ID|该IE用于全局识别一个gNB。
##### NR CGI 
IE|说明
---|---
NR CGI|该IE用于全局识别NR小区。
##### Global ng-eNB ID 
IE|说明
---|---
Global ng-eNB ID|该IE用于全局标识一个ng-eNB。
##### GBR QoS Flow Information 
IE|说明
---|---
GBR QoS Flow Information|该IE表示GBR QoS流的下行和上行业务的QoS参数。
##### QoS Flow Level QoS Parameters 
IE|说明
---|---
QoS Flow Level QoS Parameters|该IE定义了QoS流的QoS参数。
##### QoS Flow List 
IE|说明
---|---
QoS Flow List|该IE包含QoS流列表，每个QoS流携带一个原因值。该IE用指示失败的QoS流或待释放的QoS流。
##### Trace Activation 
IE|说明
---|---
Trace Activation|该IE定义了跟踪会话激活的相关参数。
##### Core Network Assistance Information 
IE|说明
---|---
Core Network Assistance Information|该IE提供RRC_INACTIVE配置等辅助信息。
##### User Location Information 
IE|说明
---|---
User Location Information|该IE用于提供UE的位置信息。
##### Slice Support List 
IE|说明
---|---
Slice Support List|该IE提供支持的网络切片列表。
##### Dynamic 5QI Descriptor 
IE|说明
---|---
Dynamic 5QI Descriptor|该IE表示下行和上行非标配或非预配置的5QI的QoS特征。
##### Allocation and Retention Priority 
IE|说明
---|---
Allocation and Retention Priority|该IE表示QoS流相对于其他QoS流的相对重要性，用于NG-RAN资源的分配和保留。
##### Source to Target Transparent Container 
IE|说明
---|---
Source to Target Transparent Container|该IE用于通过核心网将无线相关信息从切换源侧透传给切换目标侧；由源侧RAN节点产生，并发送到目标侧RAN节点。
##### Target to Source Transparent Container 
IE|说明
---|---
Target to Source Transparent Container|该IE用于通过核心网将无线相关信息从切换目标侧透传给切换源侧；由目标侧RAN节点产生，并发送到源侧RAN节点。
##### MICO Mode Indication 
IE|说明
---|---
MICO Mode Indication|该IE指示UE在AMF上配置了MICO模式。
S-NSSAI :IE|说明
---|---
S-NSSAI|Single Network Slice Selection Assistance Information，该IE表示单网络切片选择辅助信息。
##### Target ID 
IE|说明
---|---
Target ID|该IE标识切换的目标，Target ID可以是NG-RAN，也可以是E-UTRAN。
##### Emergency Fallback Indicator 
IE|说明
---|---
Emergency Fallback Indicator|该IE表示紧急业务回落。
##### Security Indication 
IE|说明
---|---
Security Indication|该IE包含用户面完整性保护指示和机密性保护指示，分别表明相应PDU会话的完整性保护和加密要求。该IE还包含单个UE的最大完整性保护数据速率，目的是达到DRB的完整性保护。
##### Non Dynamic 5QI Descriptor 
IE|说明
---|---
Non Dynamic 5QI Descriptor|该IE表示标准或预配置的5QI上下行的QoS特征。
##### Source NG-RAN Node to Target NG-RAN Node Transparent Container 
IE|说明
---|---
Source NG-RAN Node to Target NG-RAN Node Transparent Container|该IE由源侧NG-RAN节点产生，并发送到目标NG-RAN节点；对于5G异系统切换，该IE从外部切换源发送到目标NG-RAN节点。
##### Target NG-RAN Node to Source NG-RAN Node Transparent Container 
IE|说明
---|---
Target NG-RAN Node to Source NG-RAN Node Transparent Container|该IE由目标NG-RAN节点产生，并发送到源侧NG-RAN节点；对于5G异系统切换，该IE从目标NG-RAN节点传递到外部迁移源。
##### Allowed NSSAI 
IE|说明
---|---
Allowed NSSAI|该IE包含允许的NSSAI。
##### Relative AMF Capacity 
IE|说明
---|---
Relative AMF Capacity|该IE指示AMF相对于其他AMF的相对处理能力。
##### DL Forwarding 
IE|说明
---|---
DL Forwarding|该IE表示QoS流或E-RAB，用于下行数据包的转发。
##### DRBs to QoS Flows Mapping List 
IE|说明
---|---
DRBs to QoS Flows Mapping List|该IE包含一个DRB列表，其中包含映射的QoS流信息。
##### Message Identifier 
IE|说明
---|---
Message Identifier|该IE用于标识警报消息，由AMF设置，并由NG-RAN节点发送给UE。
##### Serial Number 
IE|说明
---|---
Serial Number|该IE从消息标识符指示的来源和类型中识别特定的消息，并在每次更改给定消息标识符的消息时进行更改。
##### Warning Area List 
IE|说明
---|---
Warning Area List|该IE表示需要广播或取消警告消息的区域。
##### Number of Broadcasts Requested 
IE|说明
---|---
Number of Broadcasts Requested|该IE表示广播消息的次数。
##### Warning Type 
IE|说明
---|---
Warning Type|该IE表示灾难的类型，也指示包含主通知。可用于UE根据灾难类型区分不同的告警类型。
##### Warning Security Information 
IE|说明
---|---
Warning Security Information|该IE提供了确保主通知所需的安全信息。
##### Data Coding Scheme 
IE|说明
---|---
Data Coding Scheme|该IE标识用于UE的消息字符和消息处理的字母或编码（它从5GC透传到UE）。
##### Warning Message Contents 
IE|说明
---|---
Warning Message Contents|该IE包含用户信息，例如带有警告内容的消息，并将在无线接口上广播。
##### Broadcast Completed Area List 
IE|说明
---|---
Broadcast Completed Area List|该IE表示有资源可进行广播或广播成功的区域。
##### Broadcast Cancelled Area List 
IE|说明
---|---
Broadcast Cancelled Area List|该IE指示停止广播成功的区域。
##### Number of Broadcasts 
IE|说明
---|---
Number of Broadcasts|该IE指示特定消息在给定警告区域内广播的次数。
##### Concurrent Warning Message Indicator 
IE|说明
---|---
Concurrent Warning Message Indicator|该IE指示NG-RAN节点接收到的警告消息是一个新的消息，用设定好与其他正在进行的警告消息进行并发广播。
##### Cancel-All Warning Messages Indicator 
IE|说明
---|---
Cancel-All Warning Messages Indicator|该IE指示NG-RAN节点停止在其节点或区域内正在进行的所有警告消息广播。
##### Emergency Area ID 
IE|说明
---|---
Emergency Area ID|该IE用于指示发生紧急影响的区域。
##### Repetition Period 
IE|说明
---|---
Repetition Period|该IE表示要广播的警告消息的周期。
##### PDU Session ID 
IE|说明
---|---
PDU Session ID|该IE用于标识一个UE的PDU会话。
##### QoS Flow Identifier 
IE|说明
---|---
QoS Flow Identifier|该IE标识一个PDU会话内的QoS流。
##### PDU Session Type 
IE|说明
---|---
PDU Session Type|该IE表示PDU会话类型。
##### DRB ID 
IE|说明
---|---
DRB ID|该IE包含DRB标识。
##### Masked IMEISV 
IE|说明
---|---
Masked IMEISV|该IE包含带有掩码的IMEISV值，用来标识一个终端型号，而不需要识别单个移动设备。
##### Time to Wait 
IE|说明
---|---
Time to Wait|该IE定义了允许的最小等待时间。
##### UE Aggregate Maximum Bit Rate 
IE|说明
---|---
UE Aggregate Maximum Bit Rate|该IE适用于下行和上行方向定义的所有non-GBR QoS流，以及AMF提供给NG-RAN节点的签约参数。
##### Security Result 
IE|说明
---|---
Security Result|该IE指示安全指示IE中指示为“优先”的安全策略是否执行。
##### User Plane Security Information 
IE|说明
---|---
User Plane Security Information|该IE指示安全策略相关的用户面安全信息。
##### Index to RAT/Frequency Selection Priority 
IE|说明
---|---
Index to RAT/Frequency Selection Priority|该IE用于定义RRM策略的本地配置，如空闲模式下的驻留优先级、主动模式下的系统内、系统间切换控制等。
##### Data Forwarding Accepted 
IE|说明
---|---
Data Forwarding Accepted|该IE表示NG-RAN节点接受QoS流的下行数据转发。该QoS流需支持数据转发。
##### Data Forwarding Not Possible 
IE|说明
---|---
Data Forwarding Not Possible|该IE表示5GC决定相应的PDU会话不支持数据转发。
##### Direct Forwarding Path Availability 
IE|说明
---|---
Direct Forwarding Path Availability|该IE指示是否有直接转发路径。
##### Location Reporting Request Type 
IE|说明
---|---
Location Reporting Request Type|该IE表示NG-RAN节点需要处理的位置请求类型。
##### Area of Interest 
IE|说明
---|---
Area of Interest|该IE表示兴趣区域。
##### UE Presence in Area of Interest List 
IE|说明
---|---
UE Presence in Area of Interest List|该IE指示UE在兴趣区域内。
##### UE Radio Capability for Paging 
IE|说明
---|---
UE Radio Capability for Paging|该IE包含寻呼特定UE无线能力信息。
##### Assistance Data for Paging 
IE|说明
---|---
Assistance Data for Paging|该IE为寻呼优化提供辅助信息。
##### Assistance Data for Recommended Cells 
IE|说明
---|---
Assistance Data for Recommended Cells|该IE为推荐小区的寻呼提供辅助信息。
##### Recommended Cells for Paging 
IE|说明
---|---
Recommended Cells for Paging|该IE包含了推荐的寻呼小区。
##### Paging Attempt Information 
IE|说明
---|---
Paging Attempt Information|该IE包含与NG寻呼次数相关的信息。
##### NG-RAN CGI 
IE|说明
---|---
NG-RAN CGI|该IE用于在NG-RAN中全局识别某个小区。
##### UE Radio Capability 
IE|说明
---|---
UE Radio Capability|该IE包含UE的无线能力信息。
##### Time Stamp 
IE|说明
---|---
Time Stamp|该IE包含UTC时间信息。
##### Location Reporting Reference ID 
IE|说明
---|---
Location Reporting Reference ID|该IE包含位置报告参考标识。
##### Data Forwarding Response DRB List 
IE|说明
---|---
Data Forwarding Response DRB List|该IE表示数据转发相关信息。
##### Paging Priority 
IE|说明
---|---
Paging Priority|该IE表示UE的寻呼优先级。
##### Packet Loss Rate 
IE|说明
---|---
Packet Loss Rate|该IE表示QoS流丢包率。
##### Packet Delay Budget 
IE|说明
---|---
Packet Delay Budget|该IE表示QoS流的包时延预算。
##### Packet Error Rate 
IE|说明
---|---
Packet Error Rate|该IE表示QoS流的错包率。
##### Averaging Window 
IE|说明
---|---
Averaging Window|该IE表示QoS流的平均窗口。
##### Maximum Data Burst Volume 
IE|说明
---|---
Maximum Data Burst Volume|该IE表示QoS流的最大数据突发流量。
##### Priority Level 
IE|说明
---|---
Priority Level|该IE表示QoS流的优先级。
##### Mobility Restriction List 
IE|说明
---|---
Mobility Restriction List|该IE定义了后续移动动作的漫游或接入限制，其中，NG-RAN提供针对UE的移动性动作的目标信息，例如切换，或者在双连接中的SCG选择或分配合适的RNA。如果NG-RAN收到了移动性限制列表IE，它将覆盖以前接收到的移动性限制信息。该数据结构中包含如下信息：RAT Restrictions：RAT限制相关信息。此IE包含两部分，PLMN Identity和RAT Restriction Information。RAT Restrictions Information是8bit位的比特串，每个bit代表一个RAT。 值为1时，表示对UE的RAT进行限制。 值为0时，表示不对UE的RAT进行限制。 比特0表示e-UTRA，bit1表示NR，bit2-7，发送节点应将比特2-7设置为0，接收节点应忽略比特2-7。Forbidden Area Information：Forbidden Area相关信息。此IE包含两部分，PLMN Identity和Forbidden TACs。
##### Security Key 
IE|说明
---|---
Security Key|该IE用于NG-RAN不同场景下的安全应用。
##### Security Context 
IE|说明
---|---
Security Context|该IE为NG-RAN节点提供安全相关参数，用于衍生用户面流量和RRC信令消息的安全密钥，为后续的移动性生成安全参数。
##### IMS Voice Support Indicator 
IE|说明
---|---
IMS Voice Support Indicator|该IE由NG-RAN节点设置，用于指示UE的无线能力是否与IMS语音业务的网络配置兼容。
##### Paging DRX 
IE|说明
---|---
Paging DRX|该IE表示寻呼DRX。
##### RRC Inactive Transition Report Request 
IE|说明
---|---
RRC Inactive Transition Report Request|该IE用于请求NG-RAN节点在UE进入或离开RRC_INACTIVE状态时向5GC上报或停止上报。
##### RRC State 
IE|说明
---|---
RRC State|该IE表示UE的RRC状态。
##### Expected UE Behaviour 
IE|说明
---|---
Expected UE Behaviour|该IE指示具有可预测的活动和/或移动性行为的UE的行为，以协助NG-RAN节点确定最佳的RRC连接时间，并帮助RRC_INACTIVE状态迁移和RNA配置（例如，RNA的大小和形状）。
##### Expected UE Activity Behaviour 
IE|说明
---|---
Expected UE Activity Behaviour|该IE指示了预期的“UE活动行为”的信息。
##### UE History Information 
IE|说明
---|---
UE History Information|该IE包含在目标小区之前处于激活状态的UE所服务的小区信息。
##### Last Visited Cell Information 
IE|说明
---|---
Last Visited Cell Information|该IE可能包含小区特定信息。
##### Last Visited NG-RAN Cell Information 
IE|说明
---|---
Last Visited NG-RAN Cell Information|该IE包含一个小区的信息，在NR小区中，该IE包含参考点A的一组同频点的NR小区信息。“Global Cell ID”IE标识了该小区集中的一个NR小区。该IE用于RRM目的。
##### Cell Type 
IE|说明
---|---
Cell Type|该IE提供小区覆盖范围。
##### Associated QoS Flow List 
IE|说明
---|---
Associated QoS Flow List|此IE指示与DRB或用户面TNL端点等相关联的QoS流列表。
##### Information on Recommended Cells and RAN Nodes for Paging 
IE|说明
---|---
Information on Recommended Cells and RAN Nodes for Paging|该IE提供了寻呼推荐小区和NG-RAN节点信息。
##### Recommended RAN Nodes for Paging 
IE|说明
---|---
Recommended RAN Nodes for Paging|该IE包含了推荐的NG-RAN寻呼节点。
##### E-UTRA CGI 
IE|说明
---|---
E-UTRA CGI|该IE用于全局识别E-UTRA小区。
##### Handover Type 
IE|说明
---|---
Handover Type|该IE表示源侧触发的是哪种切换。切换类型有如下几种：Intra5GS: NG-RAN node to NG-RAN node5GStoEPS: NG-RAN node to eNBEPSto5GS: eNB to NG-RAN node
##### RAN Paging Priority 
IE|说明
---|---
RAN Paging Priority|该IE包含业务优先级。
##### NAS-PDU 
IE|说明
---|---
NAS-PDU|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
##### GUAMI 
IE|说明
---|---
GUAMI|该IE表示AMF标识。
##### UE Security Capabilities 
IE|说明
---|---
UE Security Capabilities|该IE定义了UE支持的加密和完整性保护算法。该IE表示AMF标识。
##### NAS Security Parameters from NG-RAN 
IE|说明
---|---
NAS Security Parameters from NG-RANGUAMI|该IE提供了从NG-RAN到E-UTRAN通过eNB到UE的系统间切换的安全相关参数。
##### New Security Context Indicator 
IE|说明
---|---
New Security Context Indicator|该IE表示AMF已经激活了一个新的5G NAS安全上下文。
##### NASC 
IE|说明
---|---
NASC|该IE包含一个5GC和UE之间发送的消息。此消息在NG-RAN节点未解析。
##### Source AMF UE NGAP ID 
IE|说明
---|---
Source AMF UE NGAP ID|该IE在AMF内部唯一标识一个NG接口的UE关联。
##### RAN Status Transfer Transparent Container 
IE|说明
---|---
RAN Status Transfer Transparent Container|该IE由源NGRAN节点产生，传递到目标NGRAN节点，用于5GC内部NG切换。
##### UE Paging Identity 
IE|说明
---|---
UE Paging Identity|该IE表示UE被寻呼的标识。
##### Paging Origin 
IE|说明
---|---
Paging Origin|该信元指示是否由于非3GPP接入的PDU会话而发起寻呼。
##### RRC Establishment Cause 
IE|说明
---|---
RRC Establishment Cause|该IE表示EstablishmentCause中收到UE的RRC连接建立原因
##### 5G-S-TMSI 
IE|说明
---|---
5G-S-TMSI|该IE用于安全原因，隐藏用户的身份。
##### AMF Set ID 
IE|说明
---|---
AMF Set ID|该IE用于在AMF区域内唯一标识一个AMF集合。
##### Default Paging DRX 
IE|说明
---|---
Default Paging DRX|该IE表示寻呼DRX。
##### AMF Name 
IE|说明
---|---
AMF Name|该IE用于唯一标识AMF。
##### UE-associated Logical NG-connection List 
IE|说明
---|---
UE-associated Logical NG-connection List|该IE包含一个UE相关的逻辑NG-Connection列表。
##### AMF Overload Response 
IE|说明
---|---
AMF Overload Response|该IE表示在过载情况下，NGRAN节点所需的行为。
##### AMF Traffic Load Reduction Indication 
IE|说明
---|---
AMF Traffic Load Reduction Indication|该IE表示在NGRAN节点上被拒绝的流量类型相对于瞬时流入速率的百分比。
##### SON Configuration Transfer 
IE|说明
---|---
SON Configuration Transfer|该IE包含配置信息。
##### Warning Area Coordinates 
IE|说明
---|---
Warning Area Coordinates|该IE包含警告消息的受影响的警报区域坐标，并将在无线电接口上广播。
##### Routing ID 
IE|说明
---|---
Routing ID|该IE用于在5GC内标识一个LMF。
##### NRPPa-PDU 
IE|说明
---|---
NRPPa-PDU|该IE包含一个NGRAN节点LMF或LMF的NG-RAN节点消息，在AMF节点不解析。
##### Trace Collection Entity IP Address 
IE|说明
---|---
Trace Collection Entity IP Address|该IE为IP地址。
##### TAI 
IE|说明
---|---
TAI|该IE用于唯一标识一个跟踪区域。
##### TAC 
IE|说明
---|---
TAC|该IE用于唯一标识一个跟踪区域码。
##### PLMN Identity 
IE|说明
---|---
PLMN Identity|该IE表示PLMN标识。
##### TAI Slice Support List 
IE|说明
---|---
TAI Slice Support List|该IE表示支持的slice列表。
##### Backup AMF Name 
IE|说明
---|---
Backup AMF Name|该IE用于唯一标识AMF。
##### New AMF UE NGAP ID 
IE|说明
---|---
New AMF UE NGAP ID|该IE在AMF内唯一标识UE在NG接口上的关联。
##### AMF TNL Association Address 
IE|说明
---|---
AMF TNL Association Address|该IE用于提供NGRAN节点关联的NG控制面传输层信息AMF对。
##### TNL Association Usage 
IE|说明
---|---
TNL Association Usage|该IE表示TNL关联的使用情况。
##### TNL Address Weight Factor 
IE|说明
---|---
TNL Address Weight Factor|该IE表示TNL地址的权重因子。
##### AMF TNL Association Failed to Setup List 
IE|说明
---|---
AMF TNL Association Failed to Setup List|该IE包含TNL关联列表。
##### Slice Overload List 
IE|说明
---|---
Slice Overload List|该IE表示过载分片列表。
##### Slice Overload Response 
IE|说明
---|---
Slice Overload Response|该IE表示在过载情况下，NGRAN节点所需的行为。
##### Slice Traffic Load Reduction Indication 
IE|说明
---|---
Slice Traffic Load Reduction Indication|该IE表示在NGRAN节点上被拒绝的流量类型相对于瞬时流入速率的百分比。
##### PDU Session Resource Setup Request Transfer 
IE|说明
---|---
PDU Session Resource Setup Request Transfer|SMF通过AMF透传给NG-RAN的PDU Session Resource Setup Request Transfer IE。
##### PDU Session Resource Setup Response Transfer 
IE|说明
---|---
PDU Session Resource Setup Response Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Setup Response Transfer IE。
##### PDU Session Resource Setup Unsuccessful Transfer 
IE|说明
---|---
PDU Session Resource Setup Unsuccessful Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Setup Unsuccessful Transfer IE。
##### PDU Session Resource Release Command Transfer 
IE|说明
---|---
PDU Session Resource Release Command Transfer|SMF通过AMF透传给NG-RAN的PDU Session Resource Release Command Transfer IE。
##### PDU Session Resource Release Response Transfer 
IE|说明
---|---
PDU Session Resource Release Response Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Release Response Transfer IE。
##### PDU Session Resource Modify Request Transfer 
IE|说明
---|---
PDU Session Resource Modify Request Transfer|SMF通过AMF透传给NG-RAN的PDU Session Resource Modify Request Transfer IE。
##### PDU Session Resource Modify Response Transfer 
IE|说明
---|---
PDU Session Resource Modify Response Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Modify Response Transfer IE。
##### PDU Session Resource Modify Unsuccessful Transfer 
IE|说明
---|---
PDU Session Resource Modify Unsuccessful Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Modify Unsuccessful Transfer IE。
##### PDU Session Resource Notify Transfer 
IE|说明
---|---
PDU Session Resource Notify Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Notify Transfer IE。
##### PDU Session Resource Notify Released Transfer 
IE|说明
---|---
PDU Session Resource Notify Released Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Notify Released Transfer IE。
##### PDU Session Resource Modify Indication Transfer 
IE|说明
---|---
PDU Session Resource Modify Indication Transfer|NG-RAN通过AMF透传给SMF的PDU Session Resource Modify Indication Transfer IE。
##### PDU Session Resource Modify Indication Unsuccessful Transfer 
IE|说明
---|---
PDU Session Resource Modify Indication Unsuccessful Transfer|SMF通过AMF透传给NG-RAN的PDU Session Resource Modify Indication Unsuccessful Transfer IE。
##### Handover Required Transfer 
IE|说明
---|---
Handover Required Transfer|NG-RAN通过AMF透传给SMF的Handover Required Transfer IE。
##### Handover Command Transfer 
IE|说明
---|---
Handover Command Transfer|SMF通过AMF透传给NG-RAN的Handover Command Transfer IE。
##### Handover Preparation Unsuccessful Transfer 
IE|说明
---|---
Handover Preparation Unsuccessful Transfer|SMF通过AMF透传给NG-RAN的Handover Preparation Unsuccessful Transfer IE。
##### Handover Request Transfer 
IE|说明
---|---
Handover Request Transfer|SMF通过AMF透传给NG-RAN的Handover Request Transfer IE。
##### Handover Request Acknowledge Transfer 
IE|说明
---|---
Handover Request Acknowledge Transfer|NG-RAN通过AMF透传给SMF的Handover Request Acknowledge Transfer IE。
##### Handover Resource Allocation Unsuccessful Transfer 
IE|说明
---|---
Handover Resource Allocation Unsuccessful Transfer|NG-RAN通过AMF透传给SMF的Handover Resource Allocation Unsuccessful Transfer IE。
##### Path Switch Request Transfer 
IE|说明
---|---
Path Switch Request Transfer|NG-RAN通过AMF透传给SMF的Path Switch Request Transfer IE。
##### Path Switch Request Setup Failed Transfer 
IE|说明
---|---
Path Switch Request Setup Failed Transfer|NG-RAN通过AMF透传给SMF的Path Switch Request Setup Failed Transfer IE。
##### Path Switch Request Acknowledge Transfer 
IE|说明
---|---
Path Switch Request Acknowledge Transfer|SMF通过AMF透传给NG-RAN的Path Switch Request Acknowledge Transfer IE。
##### Path Switch Request Unsuccessful Transfer 
IE|说明
---|---
Path Switch Request Unsuccessful Transfer|SMF通过AMF透传给NG-RAN的Path Switch Request Unsuccessful Transfer IE。
### N3接口 
#### N3接口协议简介 
场景描述 :N3接口是5G (R)AN与UPF之间的接口，主要用于传递5G (R)AN与UPF之间的上下行用户面数据。
协议栈 :N3接口采用GTPv1-U协议，支持3GPP TS 29.281协议。 
对应的用户面接口协议栈如[图1](#T_1608519690208__bc024873-15c7-4d09-8931-6f2a5704a653)所示。
图1  N3接口协议栈
[]images/image.png)
##### 消息列表 
N3接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
Echo Request|(R)AN->UPFUPF->(R)AN|该消息用于探测通信路径和对端设备是否工作正常。
Echo Response|(R)AN->UPFUPF->(R)AN|该消息用于返回Echo Request消息的请求结果。
Supported Extension Headers Notification|(R)AN->UPFUPF->(R)AN|该消息用于指示所识别的IP地址上的GTP实体能够支持的扩展头列表。
Error Indication|(R)AN->UPFUPF->(R)AN|当GTP-U节点收到G-PDU数据包，但是找不到对应用户的上下文时，会丢弃该G-PDU数据包，此时如果G-PDU数据包携带的TEID不是全0，则会回复Error Indication。
End Marker|(R)AN->UPFUPF->(R)AN|End Marker消息是End Marker Indication的响应消息，在收到End Marker Indication消息之后，会回复End Marker消息。在5GC网络中，通过数据转发隧道发送的End Marker报文，应该与PDU Session Container扩展头一起发送，其中包括映射到同一个E-RAB的其中一个QoS流的流标识。数据转发隧道用于在5GS和EPS之间进行数据转发。
#### 相关消息解释 
##### Echo Request 
消息功能 :GTP-U的一端可以在路径上向另一端发送Echo Request消息来检测对端是否正常。
Echo Request消息可以在每一条正在使用的路径上发送。如果一条路径被至少一个PDP上下文、EPS承载、PDU会话、MBMS UE上下文，或者MBMS承载上下文用于GTP-U端点，则认为该路径正在被使用。
Echo Request消息的发送时间和发送频率取决于产品具体实现，但每条路径上发送Echo Request消息的时间间隔不能低于60秒。但是这种时间限制有一个例外场景，如果T3-RESPONSE定时器超时，Echo Request仍可以不断重发。 
如果路径没有在使用，GTP-U一端也会时刻准备接收Echo Request消息，并回复Echo Response消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
##### Echo Response 
消息功能 :Echo Response消息是作为接收到的Echo Request消息的响应消息。 
Recovery信元中的Restart Counter值不使用。发送方应将该值置为0，接收方应忽略该值。 
由于兼容性原因，Recovery信元是必选的。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Recovery|Mandatory|该信元为必选信元，Recovery信元中的Restart Counter（重启计数器）值不使用，应该由发送实体设置为0，接收实体忽略该值。由于兼容性原因，该信元在GTP用户面使用。
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
##### Supported Extension Headers Notification 
消息功能 :该消息指示指定IP地址上的GTP实体能够支持的扩展头列表。
只有当GTP实体需要解析必选的扩展头，但该GTP实体尚未被升级以支持扩展头时，才发送该消息。 
发送此消息的GTP端点被标记为不支持某些扩展头（源自支持的扩展头列表）。对端GTP实体可能会重试使用该节点的所有扩展头，试图验证它是否已经被升级。如果本端GTP实体已经指示某些扩展头无法被解析，对端GTP实体应避免重复尝试使用这些未知扩展头。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extension Header Type List|Mandatory|该信元为必选信元。该信元包含“n”扩展头类型的列表。Length字段设置为包含的扩展头类型个数。
##### Error Indication 
消息功能 :当GTP-U节点收到一个没有EPS承载上下文、PDP上下文、PDU会话、MBMS承载上下文或RAB的G-PDU数据包时，GTP-U节点将丢弃该G-PDU数据包。同时当收到的G-PDU数据包携带的TEID不是全0，则会回复Error Indication。
GTP实体包括“UDP Port”扩展头（0x40类型），以简化在某些场景下能够降低DoS攻击风险的机制的实现。
相关信元 :IE|Presence requirement|简要说明
---|---|---
Tunnel Endpoint Identifier Data I|Mandatory|该信元为必选信元，该信元包含GTP实体在用户面使用的隧道端点标识。信元值是从触发此过程的G-PDU中获取的TEID。
GTP-U Peer Address|Mandatory|该信元为必选信元，该信元包含GTP实体在用户面使用的隧道端点地址。信元值是从触发此过程的G-PDU中获取的目的地址。
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
##### End Marker 
消息功能 :最后一个G-PDU在GTP-U隧道上发送之后，或者收到End Marker Indication之后，会发送End Marker消息。 
在5GC网络中，通过数据转发隧道发送的End Marker报文，应该与PDU Session Container扩展头一起发送，其中包括映射到同一个E-RAB的其中一个QoS流的流标识。
数据转发隧道用于在5GS和EPS之间进行数据转发。
相关信元 :IE|Presence requirement|简要说明
---|---|---
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
#### 相关信元解释 
##### Information Element Types 
IE|说明
---|---
Information Element Types|GTP-U信令消息中包含多个信元。GTP信元采用TLV(Type， Length，Value)或TV(Type， Value)编码格式。在信令消息中，信元按照Type字段升序排列。Length字段包含除了Type+Length字段的长度。对于所有Length字段，最低编号octet的第8位为最高位，最高编号octet的第1位为最低位。
##### Recovery 
IE|说明
---|---
Recovery|重启计数器的值应该由发送实体设置为0，接收实体忽略。由于兼容性原因，该信元在GTP用户面使用。
##### Tunnel Endpoint Identifier Data I 
IE|说明
---|---
Tunnel Endpoint Identifier Data I|该信元包含GTP实体在用户面使用的隧道端点标识。
##### GTP-U Peer Address 
IE|说明
---|---
GTP-U Peer Address|该信元包含GTP实体在用户面使用的隧道端点地址。
##### Extension Header Type List 
IE|说明
---|---
Extension Header Type List|该信元包含“n”扩展头类型的列表。Length字段设置为包含的扩展头类型个数。
##### Private Extension 
IE|说明
---|---
Private Extension|该信元包含厂商的特定信息。扩展标识是在最近的“Assigned Numbers”RFC（RFC 1700及以上版本）中的私有企业号码列表中定义的一个值。该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
### N4接口 
#### N4接口协议简介 
场景描述 :N4接口为SMF和UPF之间的接口，用于传输SMF和UPF之间的控制面和用户面信息。 
协议栈 :N4接口的控制面协议栈如[图1](#T_1608621566644__c8ee312c-e211-4651-babe-7005b224bfd2)所示。
图1  N4接口控制面协议栈
[]images/1610003898523.png)
N4接口的用户面协议栈如[图2](#T_1608621566644__92b3b744-a4b3-442d-8e94-d1bebeca27f2)所示。
图2  N4接口用户面协议栈
[]images/1559639405031.png)
##### 消息列表 
N4接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
PFCP Heartbeat Request|SMF->UPFUPF->SMF|用于探测通信路径和对端设备是否工作正常。
PFCP Heartbeat Response|SMF->UPFUPF->SMF|用于探测通信路径和对端设备是否工作正常。
PFCP Association Setup Request|SMF->UPFUPF->SMF|偶联建立，协商SMF和UPF之间的能力，如两端各自支持的功能。
PFCP Association Setup Response|SMF->UPFUPF->SMF|偶联建立，协商SMF和UPF之间的能力，如两端各自支持的功能。
PFCP Association Update Request|SMF->UPFUPF->SMF|偶联更新，如SMF支持的功能发生变化时，SMF发起偶联更新流程；UPF支持的功能发生变化、请求释放偶联时，UPF发起偶联更新流程。
PFCP Association Update Response|SMF->UPFUPF->SMF|偶联更新，如SMF支持的功能发生变化时，SMF发起偶联更新流程；UPF支持的功能发生变化、请求释放偶联时，UPF发起偶联更新流程。
PFCP Association Release Request|SMF->UPF|偶联释放，如因为操作运维管理原因需要终结偶联。
PFCP Association Release Response|UPF->SMF|偶联释放，如因为操作运维管理原因需要终结偶联。
PFCP Node Report Request|UPF->SMF|节点级信息上报，如UPF的N3/N9接口链路故障信息上报给SMF。
PFCP Node Report Response|SMF->UPF|节点级信息上报，如UPF的N3/N9接口链路故障信息上报给SMF。
PFCP Session Establishment Request|SMF->UPF|为用户建立PFCP会话。
PFCP Session Establishment Response|UPF->SMF|为用户建立PFCP会话。
PFCP Session Modification Request|SMF->UPF|更新PFCP会话，如新增一个PDR、更新一个PDR、删除一个PDR，触发PFCP会话更新。
PFCP Session Modification Response|UPF->SMF|更新PFCP会话，如新增一个PDR、更新一个PDR、删除一个PDR，触发PFCP会话更新。
PFCP Session Deletion Request|SMF->UPF|释放PFCP会话，如PDN删除，触发PFCP会话删除。
PFCP Session Deletion Response|UPF->SMF|释放PFCP会话，如PDN删除，触发PFCP会话删除。
PFCP Session Report Request|UPF->SMF|会话信息上报，如用户流量配额用完，触发UPF通过该消息上报用户流量。
PFCP Session Report Response|SMF->UPF|会话信息上报，如用户流量配额用完，触发UPF通过该消息上报用户流量。
#### 相关消息解释 
##### PFCP Heartbeat Request 
消息功能 :SMF/UPF给UPF/SMF发送此消息检测对端的心跳。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Recovery Time Stamp|Mandatory|该IE应包含节点启动时的时间戳。
##### PFCP Heartbeat Response 
消息功能 :SMF/UPF给UPF/SMF发送此消息响应对端的心跳请求。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Recovery Time Stamp|Mandatory|该IE应包含节点启动时的时间戳。
##### PFCP Association Setup Request 
Association Setup Request 
消息功能 :SMF/UPF给UPF/SMF发送此消息请求建立偶联。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Recovery Time Stamp|Mandatory|该IE应包含节点启动时的时间戳。
UP Function Features|Conditional|如果用户面网元发送该消息，并且用户面网元支持至少一个用户面特性，则该IE应该出现。当出现时，该IE应指示用户面网元支持的特性。
CP Function Features|Conditional|如果控制面网元发送该消息，且控制面网元支持至少一个该IE定义的控制面特性，则该信元必须存在。当出现时，该IE应指示控制面网元支持的特性。
##### PFCP Association Setup Response 
Association Setup Response 
消息功能 :SMF/UPF给UPF/SMF发送此消息响应对端发送的建立偶联请求。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
Recovery Time Stamp|Mandatory|该IE应包含节点启动时的时间戳。
UP Function Features|Conditional|如果用户面网元发送该消息，并且用户面网元支持至少一个用户面特性，则该IE应该出现。当出现时，该IE应指示UP功能支持的特性。
CP Function Features|Conditional|如果控制面网元发送该消息，且控制面网元支持至少一个该IE定义的控制面特性，则该信元必须存在。当出现时，该IE应指示控制面网元支持的特性。
##### PFCP Association Update Request 
Association Update Request 
消息功能 :SMF/UPF给UPF/SMF发送此消息请求偶联更新。如SMF支持的功能发生变化时，SMF发起偶联更新流程；UPF支持的功能发生变化、请求释放偶联时，UPF发起偶联更新流程。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
UP Function Features|Optional|如果存在，则该IE应指示发送节点为用户面网元时支持的特性。
CP Function Features|Optional|如果存在，则该IE应指示发送节点为控制面网元时支持的特性。
PFCP Association Release Request|Conditional|如果用户面网元请求控制面网元释放PFCP偶联，则该IE应该出现。
Graceful Release Period|Conditional|如果用户面网元请求优雅释放PFCP偶联，则该IE应该出现。
##### PFCP Association Update Response 
Association Update Response 
消息功能 :SMF/UPF给UPF/SMF发送此消息响应对端的偶联更新请求。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
UP Function Features|Conditional|如果存在，则该IE应指示发送节点为用户面网元时支持的特性。
CP Function Features|Conditional|如果存在，则该IE应指示发送节点为控制面网元时支持的特性。
##### PFCP Association Release Request 
Association Release Request 
消息功能 :SMF给UPF发送此消息请求释放偶联。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
##### PFCP Association Release Response 
Association Release Response 
消息功能 :UPF给SMF发送此消息响应对端的偶联释放请求。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
##### PFCP Node Report Request 
消息功能 :UPF给SMF发送此消息进行节点级信息上报，如UPF的N3/N9接口链路故障信息上报给SMF。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Node Report Type|Mandatory|该IE应指示报告的类型。
User Plane Path Failure Report|Conditional|如果节点报告类型指示用户面路径故障报告，则该IE应出现。
##### PFCP Node Report Response 
消息功能 :SMF给UPF发送此消息响应节点级信息上报请求。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
Offending IE|Conditional|如果拒绝原因是由于条件或必选信元丢失或故障，则应包含此IE。
##### PFCP Session Establishment Request 
Session Establishment Request 
消息功能 :SMF给UPF发送此消息请求建立新的PFCP会话上下文。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
CP F-SEID|Mandatory|该IE应包含标识会话的控制面网元分配的唯一标识符。
Create PDR|Mandatory|至少有一个PDR要关联到PFCP会话中时，该IE出现。可能存在多个具有相同IE类型的IE来表示多个PDR。
Create FAR|Mandatory|至少有一个FAR要关联到PFCP会话中时，该IE出现。可能存在多个具有相同IE类型的IE来表示多个FAR。
Create URR|Conditional|如果对匹配该PFCP会话的一个或多个PDR的数据包采取测量动作，则该IE应出现。可能存在多个具有相同IE类型的IE代表多个URR。
Create QER|Conditional|如果对匹配该PFCP会话的一个或多个PDR的报文应用QoS执行或QoS标记动作，则该IE应出现。可能存在多个具有相同IE类型的IE来表示多个QER。
Create BAR|Optional|当出现时，该IE应包含由UP功能应用到PFCP会话集合中的任何一个FAR上的缓存指令，该指令包括要缓存的数据包，以及指向该BAR的BAR ID IE。
Create Traffic Endpoint|Conditional|如果用户面网元指示支持PDI优化，则可能存在此IE。在相同IE类型内的几个IE可以表示为多个流量端点。
PDN Type|Conditional|如果为单个PDN连接或PDU会话建立PFCP会话，则应该出现此IE。
User Plane Inactivity Timer|Optional|该IE可用于请求用户面网元在该PFCP会话没有接收到用户面报文的时长超过用户面不活跃定时器的时候发送用户面不活动报告。
User ID|Optional|基于运营商策略的情况下该IE可能存在。如果用户面网元在可信环境中，则可能发送该IE。
Trace Information|Optional|当出现此IE时，该IE应包含该PFCP会话的用户面网元要应用的跟踪指令。
##### PFCP Session Establishment Response 
Session Establishment Response 
消息功能 :UPF给SMF发送此消息响应建立新的PFCP会话上下文的请求消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Node ID|Mandatory|该IE应包含发送节点的唯一标识符。
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
Offending IE|Conditional|如果拒绝的原因是条件或必选信元丢失或故障，则应包含此IE。
UP F-SEID|Conditional|如果原因设置为请求接受（成功），则该IE应出现。当出现时，它应该包含由用户面网元分配的唯一标识符，用于标识会话。
Created PDR|Conditional|如果原因值设置为成功，并且请求用户面网元为PDR分配本地F-TEID，则该IE应出现。当出现此IE时，该IE应包含与PFCP会话相关的PDR信息，该IE可能有多个实例。
Load Control Information|Optional|如果支持负载控制特性，且网络中已激活该特性，则用户面网元中可能包含该信元。
Overload Control Information|Optional|在过载情况下，如果支持过载控制特性，且网络中已激活该特性，则用户面网元可能会携带此信元。
Failed Rule ID|Conditional|如果原因值为创建或修改规则失败导致拒绝，则应包含此IE。
Created Traffic Endpoint|Conditional|如果原因被设置为成功，并且请求在创建流量端点IE中分配本地F-TEID，则该IE应出现，当出现时，它将包含用于此流量端点的本地F-TEID。该IE可能有多个实例。
##### PFCP Session Modification Request 
Session Modification Request 
消息功能 :SMF给UPF发送此消息请求修改PFCP会话。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
CP F-SEID|Conditional|如果控制面网元决定修改它分配的PFCP会话的F-SEID，则该信元应该存在，用户面网元在后续PFCP会话相关消息中将使用新的CP F-SEID。
Remove PDR|Conditional|当出现此IE时，该IE应包含请求删除的PDR规则。可以在同一IE类型内的几个IE表示要删除的PDR列表。
Remove FAR|Conditional|当出现此IE时，该IE应包含请求删除的FAR规则。可以在同一IE类型内的几个IE表示要删除的FAR列表。
Remove URR|Conditional|当出现此IE时，该IE应包含请求删除的URR规则。可以在同一IE类型内的几个IE表示要删除的URR列表。
Remove QER|Conditional|当出现此IE时，该IE应包含请求删除的QER规则。可以在同一IE类型内的几个IE表示要删除的QER列表。
Remove BAR|Conditional|当出现此IE时，该IE应包含请求删除的BAR规则。
Remove Traffic Endpoint|Conditional|当出现时，如果用户面网元指示支持PDI优化，则该IE应包含标识需要删除的流量端点的流量端点标识。所有删除的流量端点的相关PDR都要被删除。
Create PDR|Conditional|如果控制面网元请求用户面网元创建一个新的PDR，则该IE应该出现。在同一个IE类型内的几个IE可以表示为要创建的PDR列表。
Create FAR|Conditional|如果控制面网元请求用户面网元创建一个新的FAR，则该IE应该出现。在同一个IE类型内的几个IE可以表示为要创建的FAR列表。
Create URR|Conditional|如果控制面网元请求用户面网元创建一个新的URR，则该IE应该出现。在同一个IE类型内的几个IE可以表示为要创建的URR列表。
Create QER|Conditional|如果控制面网元请求用户面网元创建一个新的QER，则该IE应该出现。在同一个IE类型内的几个IE可以表示为要创建的QER列表。
Create BAR|Conditional|如果控制面网元请求用户面网元创建一个新的BAR，则该IE应该出现。
Create Traffic Endpoint|Conditional|当出现此IE时，如果用户面网元表示支持PDI优化，则该IE应包含与待创建的流量端点相关的信息
Update PDR|Conditional|如果需要修改先前为PFCP会话创建的PDR，则该IE应该出现。可以在同一IE类型内的几个IE表示要更新的PDR列表。
Update FAR|Conditional|如果需要修改先前为PFCP会话创建的FAR，则该IE应该出现。可以在同一IE类型内的几个IE表示要更新的FAR列表。
Update URR|Conditional|如果需要修改先前为PFCP会话创建的URR，则该IE应该出现。可以在同一IE类型内的几个IE表示要更新的URR列表。
Update QER|Conditional|如果需要修改先前为PFCP会话创建的QER，则该IE应该出现。可以在同一IE类型内的几个IE表示要更新的QER列表。
Update BAR|Conditional|如果需要修改先前为PFCP会话创建的BAR，则该IE应该出现。
Update Traffic Endpoint|Conditional|当出现此IE时，如果用户面网元表示支持PDI优化，则该IE应包含与待更新的流量端点相关的信息。所有引用流量端点的PDR都应使用更新后的流量端点信息。
PFCPSMReq-Flags|Conditional|如果至少有一个标志位被设置为1，则必须包含这个IE。DROBU（丢弃缓存报文）：如果请求丢弃当前PFCP会话缓存的报文，控制面网元应设置此标志。QAURR （查询所有URR ）：如果控制面网元需要为该PFCP会话的所有URR请求立即使用报告，则控制面网元应设置该标志。
Query URR|Conditional|如果控制面网元向用户面网元请求立即使用报告，则该IE应该出现。在同一IE类型内的几个IE可以表示请求立即报告的URR列表。
User Plane Inactivity Timer|Conditional|如果需要更改用户面不活动定时器，该IE将会出现。
Query URR Reference|Optional|如果存在QueryURR信元或QAURR标志位为1，则可能存在该IE。当出现时，它应包含一个引用，标识查询请求，用户面网元应在发送的任何使用报告中响应查询。
Trace Information|Optional|当出现此IE时，该IE应包含用于该PFCP会话的用户面网元要应用的跟踪指令。跟踪信息为空，表示跟踪会话应该被去激活。
##### PFCP Session Modification Response 
Session Modification Response 
消息功能 :UPF给SMF发送此消息响应更新PFCP会话的请求消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
Offending IE|Conditional|如果拒绝的原因是条件或必选信元丢失或故障，则应包含此IE。
Create PDR|Conditional|如果原因值设置为“成功”，并且请求UP功能为PDR分配本地F-TEID，则该IE应出现。当出现此IE时，该IE应包含与PFCP会话相关的PDR信息，该IE可能有多个实例。
Load Control Information|Optional|如果支持负载控制特性，且网络中已激活该特性，则用户面网元中可能包含该信元。
Overload Control Information|Optional|在过载情况下，如果支持过载控制特性，且网络中已激活该特性，则用户面网元可能会携带此信元。
Usage Report（within PFCP Session Modification Response）|Conditional|该IE应在以下情况下出现：在PFCP会话修改请求中存在查询URR信元或QAURR标志位为“1”。在用户面网元中，可以使用URR的流量使用度量。用户面网元决定在PFCP会话修改响应中返回部分或全部请求的使用报告。如果以下情况，该IE也应出现：删除URR或URR关联的最后一个PDR。在用户面网元中，有URR的非空流量使用度量。用户面网元决定在PFCP会话修改响应中返回部分或全部相关使用报告。在同一IE类型内的几个IE可以表示使用报告列表。
Failed Rule ID|Conditional|如果原因值为创建或修改规则失败导致拒绝，则应包含此IE。
Additional Usage Reports Information|Conditional|如果PFCP会话修改请求中存在查询URR信元或QAURR标志为1，则需要包含该IE，并且需要在额外的PFCP会话报告请求消息中发送使用报告。当出现此IE时，该IE应指示后续有附加使用报告，或指示需要在PFCP会话报告请求消息中发送的使用报告的总数。
Created Traffic Endpoint/Update Traffic Endpoint|Conditional|如果原因值设置为“成功”，则该IE应出现，请求创建或更新流量端点，并请求用户面网元为流量端点分配本地F-TEID。当出现时，该IE应包含与PFCP会话关联的流量端点信息。
##### PFCP Session Deletion Request 
消息功能 :SMF给UPF发送此消息请求删除PFCP会话。 
相关信元 :目前此消息中不包含信元。 
##### PFCP Session Deletion Response 
消息功能 :UPF给SMF发送此消息响应删除PFCP会话的请求消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
Offending IE|Conditional|如果拒绝的原因是条件或必选信元丢失或故障，则应包含此IE。
Load Control Information|Optional|如果支持负载控制特性，且网络中已激活该特性，则用户面网元中可能包含该信元。
Overload Control Information|Optional|在过载情况下，如果支持过载控制特性，且网络中已激活该特性，则用户面网元可能会携带此信元。
Usage Report（within PFCP Session Deletion Response）|Conditional|如果在用户面网元中已经开通了一个URR，并且该PFCP会话被删除，并且在用户面网元中可以使用URR的流量使用度量，那么该IE将会出现。在同一IE类型内的几个IE可以表示使用报告列表。
##### PFCP Session Report Request 
消息功能 :UPF给SMF发送此消息进行PFCP会话级信息上报。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Report Type|Mandatory|该IE应指示报告的类型。
Downlink Data Report|Conditional|如果报告类型为下行数据报告，则该IE应出现。
Usage Report（within PFCP Session Report Request）|Conditional|如果报告类型指示使用报告，则该IE应出现。在同一IE类型内的几个IE可以表示使用报告列表。
Error Indication Report|Conditional|如果报告类型指示错误指示报告，则该IE应出现。
Load Control Information|Optional|如果支持负载控制特性，且网络中已激活该特性，则用户面网元中可能包含该信元。
Overload Control Information|Optional|在过载情况下，如果支持过载控制特性，且网络中已激活该特性，则用户面网元可能会携带此信元。
Additional Usage Reports Information|Conditional|如果PFCP会话修改响应指示有更多的报告会跟随，则该IE应包含在一个额外的PFCP会话报告请求消息中。当出现此IE时，该IE应指示PFCP会话报告请求消息中需要发送的使用报告总数。
##### PFCP Session Report Response 
消息功能 :SMF给UPF发送此消息响应PFCP会话级信息上报请求。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|该IE应指示接受或拒绝相应的请求消息。
Offending IE|Conditional|如果拒绝是由于条件或必选信元丢失或故障而拒绝的，则应包含此IE。
Update BAR|Conditional|如果需要修改先前为PFCP会话创建的BAR，则该IE将出现。未被修改的先前创建的BAR不应包括在内。
SxSRRsp-Flags|Conditional|如果至少有一个标志位被设置为1，则必须包含这个IE。-DROBU（丢弃缓存报文）：如果UP功能需要丢弃当前PFCP会话缓存的报文，则控制面网元需要设置该标志。
#### 相关信元解释 
##### Recovery Time Stamp 
IE|说明
---|---
Recovery Time Stamp|该IE指示节点启动时的UTC时间。注意：编码定义为相对于1900年1月1号的00:00:00的秒数。
##### Node ID 
IE|说明
---|---
Node ID|该IE指示应包含节点的FQDN或IPv4/IPv6地址。信元中Node ID Type表示节点ID值的类型，其取值和意义如下：0，IPv4 address1，IPv6 address2，FQDN3~15，备用，以备将来使用。
##### UP Function Features 
IE|说明
---|---
UP Function Features|该IE指示用户面网元支持的特性。
##### CP Function Features 
IE|说明
---|---
CP Function Features|该IE指示控制面网元支持的特性。只有对（全系统）用户面网元行为有影响的特性才会在该IE中指示。
##### Cause 
IE|说明
---|---
Cause|该信元应包含在响应消息中，在响应消息中，原因值表示接受或拒绝相应的请求消息。原因值表示拒绝的明确原因，其取值和意义如下：1，Reserved2-63，备用64，Request rejected (reason not specified)65，Session context not found66，Mandatory IE missing67，Conditional IE missing68，Invalid length69，Mandatory IE incorrect70，Invalid Forwarding Policy71，Invalid F-TEID allocation option72，No established PFCP Association73，Rule creation/modification Failure74，PFCP entity in congestion75，No resources available76，Service not supported77，System failure78-255，备用
##### PFCP Association Release Request 
IE|说明
---|---
PFCP Association Release Request|该IE中“SARR (PFCP Association Release Request)”设置为“1”，则表示用户面网元请求释放PFCP偶联。
##### Graceful Release Period 
IE|说明
---|---
Graceful Release Period|该IE指示优雅释放的具体时间。Bits 5 to 1 表示二进制编码的定时器时长。Bits 6 to 8 表示定时器时长单位，其取值如下：Bits8 7 60 0 0 ， 值按2秒的倍数递增0 0 1 ，值按1分钟的倍数递增0 1 0 ，值按10分钟的倍数递增0 1 1 ，值按1小时的倍数递增1 0 0 ，值按10小时的倍数递增1 1 1 ，表示定时器无穷大
##### Node Report Type 
IE|说明
---|---
Node Report Type|该IE指示用户面网元向控制面网元发的节点报告的类型。第5字节编码如下：bit1 ，UPFR（User Plane Path Failure Report）：当取值为1时，表示用户面路径故障报告bit2-bit8，spare，后续使用，设置为0至少有一个比特设置为1，可以将几个比特设置为1。
##### User Plane Path Failure Report 
IE|说明
---|---
User Plane Path Failure Report|该IE里面包含Remote GTP-U Peer类型的IE信息，该Remote GTP-U PeerIE应包含检测到用户面路径故障的远端GTP-U对等体的IP地址。User Plane Path Failure Report可以包含多个具有这种Remote GTP-U Peer类型的IE来表示检测到用户面路径故障的多个远端GTP-U对等体。
##### User Plane Inactivity Timer 
IE|说明
---|---
User Plane Inactivity Timer|该IE指示用户面不活动定时器。
##### PDN Type 
IE|说明
---|---
PDN Type|该IE指示PDN连接类型。其取值和意义为：1，IPv42，IPv63，IPv4v64，Non-IP5，Ethernet6，为了将来的使用。
##### Offending IE 
IE|说明
---|---
Offending IE|如果拒绝是由于条件或必选信元出现故障或丢失，则该信元必须包含一个必选信元类型。
##### F-SEID 
IE|说明
---|---
F-SEID|该IE中以下标志位在第5个字节中进行编码：bit1，v6：如果设置为1，则F-SEID中应该有IPv6地址字段，否则IPv6地址字段不存在。bit2，v4：如果设置为1，则F-SEID中应该有IPv4地址字段，否则IPv4地址字段不存在。bit3-bit8，为备用，保留未用。
##### Failed Rule ID 
IE|说明
---|---
Failed Rule ID|该IE指示创建或修改失败的规则，其中Rule ID Type可以为PDR、FAR、QER、BAR。
##### User ID 
IE|说明
---|---
User ID|该IE指示用户ID，IE中User ID Type可以为IMSI、IMEI、MSISDN、NAI。
##### Trace Information 
IE|说明
---|---
Trace Information|该IE指示用于该PFCP会话的跟踪控制和配置参数。
##### Create PDR 
IE|Presence requirement|说明
---|---|---
PDR ID|Mandatory|该IE将在为该PFCP会话配置的所有PDR中唯一标识PDR。
Precedence|Mandatory|当查找与传入报文匹配的PDR时，该IE将指示PDR在PFCP会话的所有PDRs中应用的优先级。
PDI|Mandatory|该IE应包含PDI，用于匹配进来的报文。
Outer Header Removal|Optional|如果需要用户面网元删除匹配该PDR的报文中的一个或多个外层，则该IE应出现。
FAR ID|Optional|如果不包含Activate Predefined Rules IE或包含Activate Predefined Rules IE但不会导致激活预定义的FAR，则该IE将出现。当出现此IE时，应包含与PDR关联的FAR ID。
URR ID|Optional|如果对匹配该PDR的数据包采取测量动作，则该IE应出现。当出现时，该IE应包含与PDR关联的URR标识。在同一个IE类型内的几个IE可以表示要关联到PDR的URR列表。
QER ID|Optional|如果对匹配该PDR的报文应用QoS执行或QoS标记动作，则该IE应出现。当出现时，该IE应包含要关联到PDR的QER标识，在同一个IE类型内的几个IE可以表示要关联到PDR的QER列表。
Activate Predefined Rules|Optional|如果该IE需要激活预定义规则，则该IE应出现。当该IE出现时，该IE应包含一个预定义规则名称。可能存在多个具有相同IE类型的IE来表示多个“激活预定义规则”名称。
Source Interface|Mandatory|该IE应识别传入包的源接口。
SDF Filter|Optional|如果存在，该IE应识别SDF过滤器，以匹配传入的数据包。可能会出现多个具有相同IE类型的IE，以提供SDF过滤器列表。当存在时，在PDI的创建或修改期间，应提供所有适用的SDF过滤器。
Application ID|Optional|如果存在，该IE应识别传入包的应用ID。
QFI|Optional|如果存在，该IE应识别QoS流标识符，以匹配传入包。可能会出现多个具有相同IE类型的IE，以提供QFI列表。当存在时，在PDI的创建或修改期间，应提供所有适用的QFI。
##### Create FAR 
IE|Presence requirement|说明
---|---|---
FAR ID|Mandatory|该IE必须唯一地标识为该PFCP会话配置的所有FAR中的一个。
Apply Action|Mandatory|该IE应指示对数据包适用的动作。
Forwarding Parameters|Conditional|当Apply Action请求转发数据包时，该IE应该出现。当Apply Action请求转发的报文时，该IE应包含用户面网元需要应用的转发指令。
Duplicating Parameters|Conditional|当Apply Action请求报文被复制时，该IE应该出现。当Apply Action请求复制的报文时，该IE应包含用户面网元对需要复制的流量所应用的转发指令。
BAR ID|Optional|当应用程序请求缓存的数据包时，该IE应包含定义缓存指令的条的BAR ID。
##### Create URR 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE将在为该PFCP会话配置的所有URR中唯一标识URR。
Measurement Method|Mandatory|该IE应指示测量网络资源使用情况的方法，即是否测量数据量、持续时间，或事件。
Reporting Triggers|Mandatory|该IE应指示触发，用于向控制面网元报告网络资源使用情况，例如周期上报、达到阈值时上报。
Measurement Period|Conditional|如果需要定期报告，则该IE应显示。当出现时，它应指示使用报告的产生和报告的周期。
Volume Threshold|Conditional|如果使用基于流量的测量，并且在达到流量阈值时需要上报，则应该显示该IE。当出现流量阈值时，该IE应指示用户面网元向该URR的控制面网元上报网络资源使用情况的流量。
Volume Quota|Conditional|如果使用基于流量的测量，且控制面网元需要在用户面网元中开通流量配额，则该IE应该出现。当出现时，它应指示流量配额值。
Event Threshold|Conditional|如果使用事件测量，并且达到事件阈值时需要上报，则应该显示该IE。当出现事件阈值时，该IE应指示用户面网元向控制面网元上报该URR的事件数。
Event Quota|Conditional|如果使用事件测量，且控制面网元需要在用户面网元中提供事件配额，则该IE应该出现。当出现时，它应指示事件配额值。
Time Threshold|Conditional|如果使用基于时间的测量，并且在达到一定的时间阈值时需要上报，那么应该显示这个IE。当出现时，它应该指示用户面网元向控制面网元报告网络资源使用情况的时间使用情况。
Time Quota|Conditional|如果使用基于时间的测量，并且CP功能需要在用户面网元中提供一个时间配额，则该IE应该出现。当出现时，它应指示时间配额值。
Quota Holding Time|Conditional|该IE应存在于一个时间、量或事件测量中，如果需要报告，并且在给定的不活动期间没有收到数据包时，数据包不再允许通过。当出现时，它应包含不活动期间的持续时间。
Dropped DL Traffic Threshold|Conditional|当下行流量被丢弃时，如果需要上报，则需要上报该IE。当出现时，它应包含下行流量被丢弃的阈值。
Monitoring Time|Optional|当出现时，该IE应包含用户面网元应重新应用流量或时间阈值的时间。
Subsequent Volume Threshold|Optional|如果存在Monitoring Time IE，并且使用了基于流量的测量，则可能存在该IE。当出现该值时，应指示该URR在监控时间之后的一段时间内，用户面网元向控制面网元上报网络资源使用情况的流量值。
Subsequent Time Threshold|Optional|如果存在Monitoring Time IE，并且使用基于时间的测量，则可能存在该IE。当出现时，应指示在监视时间之后的一段时间内，用户面网元向控制面网元上报网络资源使用情况的时间使用情况。
Subsequent Volume Quota|Optional|如果存在Monitoring Time IE，并且使用了基于流量的测量，则可能存在该IE。当出现时，它应指示用户面网元在监视时间之后的一段时间内使用该URR所使用的流量配额值。
Subsequent Time Quota|Optional|如果存在Monitoring Time IE，并且使用基于时间的测量，则可能存在该IE。当出现时，它应指示用户面网元在监视时间之后的一段时间内使用该URR所使用的时间配额值。
Subsequent Event Threshold|Optional|如果存在Monitoring Time IE，并且使用事件测量，则可能存在该IE。当出现时，它应指示在监视时间之后的一段时间内，用户面网元向控制面网元上报该URR的事件数。
Subsequent Event Quota|Optional|如果存在Monitoring Time IE，并且使用基于事件的测量，则可能存在此IE。当出现时，它应指示用户面网元在监视时间之后的一段时间内应该使用的事件配额值。
Inactivity Detection Time|Conditional|如果使用基于时间的测量，并且在给定的不活动周期内没有接收到数据包时需要挂起时间测量，则应包含该IE。当出现时，应包含不活动周期的持续时间。
Linked URR ID|Conditional|如果需要链接使用报告，则该IE应出现。当出现此IE时，该IE应包含与此URR相关的链接URR ID。可能存在多个IE类型相同的IE来表示与该URR相关的多个链接URR。
Measurement Information|Conditional|如果下列标志中的任何一个设置为1，则必须包含此IE。适用的标志有：QoS执行标志前的测量：如果请求测量之前的流量使用情况，则该标志应该设置为1。未激活测量标志：如果测量应暂停（非活动） ，该标志应设为1。如果该比特位为0，或者在创建URR信元中没有测量信息IE，则需要进行测量（激活）。减少应用检测信息标志：该标志可以设置为1，如果上报触发请求上报应用的启动或停止，则请求用户面网元只上报应用检测信息中的应用ID，例如信封上报。立即开始时间计量标志：如果使用基于时间的度量，则可以将该标志置为1，并要求在接收到标志时立即启动计时计量。
Time Quota Mechanism|Conditional|如果使用基于CTP或DTP的基于时间的测量，他的IE将会出现。
Aggregated URRs|Conditional|如果使用URR支持Credit Pool，则必须包含此IE。可能存在多个IE类型相同的IE，以提供多个聚合的URR。
FAR ID for Quota Action|Conditional|如果在URR中开通了流量配额IE和/或时间配额IE和/或事件配额IE，并且UP功能指示支持配额动作特性，则该IE可能出现。当出现这种情况时，它应该包含替代的标识符，而对于与这个URR相关的流量，当耗尽任何一个配额时，它将适用。
Ethernet Inactivity Timer|Conditional|如果使用以太网流量上报，并且SMF请求UP功能，同时上报非活动UE MAC地址，则该IE应该出现。当出现时，它将包含以太网不活动周期的持续时间。
Additional Monitoring Time|Optional|当出现时，该IE应包含用户面网元应重新应用在IE中发放的流量或时间或事件阈值/配额的时间。
##### Create QER 
IE|Presence requirement|说明
---|---|---
QER ID|Mandatory|该IE将在为该PFCP会话配置的所有QER中唯一标识QER。
QER Correlation ID|Conditional|如果需要使用用户面网元关联多个PFCP会话的QERs，将多个UE的PDN连接的APN-AMBR强制到同一个APN，则该IE应该出现。
Gate Status|Mandatory|该IE应指示数据包是否允许在上行和/或下行方向被允许转发或丢弃。
Maximum Bitrate|Conditional|如果需要对匹配该PDR的报文应用MBR强制执行动作，则该IE应显示，该IE应指示匹配该PDR的报文的上行和/或下行最大比特率。对于EPC，该信元可以设置为：APN-AMBR，用于一个PDN连接的所有non-GBR承载的PDR引用的QER；TDF会话MBR，用于TDF会话的所有PDR引用的QER；承载MBR，用于承载的所有PDR引用的QER；一个SDF的MBR，用于一个SDF的所有PDR引用的QER。对于5GC，该信元可以设置为：Session-AMBR，用于一个PDU会话的non-GBR QoS流的所有PDR引用的QER；QoS流MBR，用于QoS流的所有PDR引用的QER；一个SDF的MBR，用于一个SDF的所有PDR引用的QER。
Guaranteed Bitrate|Conditional|如果对匹配该PDR的报文授权了GBR，则该IE应出现，该IE应指示授权的上行和/或下行保证比特率。该信元可以设置为：聚合GBR，用于GBR承载的所有PDR引用的QER；QoS流GBR，针对一个QoS流中的所有PDR引用的QER (5GC) ；
Packet Rate|Conditional|如果对匹配该PDR的报文应用包速率强制执行动作（按每时间间隔的包数量），则该IE应出现。当出现时，该IE应指示匹配PDR的数据包的上行和/或下行最大包速率。该信元可以设置为：服务PLMN速率控制的下行数据包速率。用于APN速率控制的上行和/或下行数据包速率，对于属于同一个APN的UE的所有PDR，使用CIoT的EPS优化所引用的QER。
DL Flow Level Marking|Conditional|如果需要使用用户面网元对报文进行QoS标记，则需要设置此IE：由TDF-C，用于应用指示的下行流级标记。由PGWC设置GTP-U服务等级指示扩展头，用于向GERAN服务指示。
QoS flow identifier|Conditional|如果QoS流标识符需要由UPF插入，则该IE应出现。
Reflective QoS|Conditional|如果需要用户面网元插入一个反射QoS标识符来请求上行流量的反射QoS，则该IE应该出现。
Paging Policy Indicator|Conditional|如果需要UPF在出局报文中设置寻呼策略指示 ，则应出现该IE。当出现时，应设置为要设置的PPI值。
Averaging Window|Optional|如果需要用户面网元使用不同于默认的平均窗口，则可能存在此IE。
##### Create BAR 
IE|Presence requirement|说明
---|---|---
BAR ID|Mandatory|该IE将唯一标识为PFCP会话提供的BAR。
Downlink Data Notification Delay|Conditional|如果用户面网元指示支持下行数据通知延迟参数，并且用户面网元必须延迟向控制面网元通知下行数据包到达，则该IE应出现。当应用动作参数请求缓存报文并通知控制面网元时，应包含延迟用户面网元在接收下行数据包和通知控制面网元之间的延迟。
Suggested Buffering Packets Count|Conditional|如果用户面网元指示支持该特性UDBC，则该IE可能出现。当应用动作参数请求缓存报文时，应包含建议缓存的报文个数，超过限制的报文将被丢弃。
##### Created PDR 
IE|Presence requirement|说明
---|---|---
PDR ID|Mandatory|PDR的标识。
Local F-TEID|Conditional|如果用户面网元分配了F-TEID，则该IE应该存在，并且应该包含用于本PDR的本地F-TEID。
##### Update PDR 
IE|Presence requirement|说明
---|---|---
PDR ID|Mandatory|该IE将在为该PFCP会话配置的所有PDR中唯一标识PDR。
Outer Header Removal|Conditional|如果需要更改，该IE将会出现。
Precedence|Conditional|如果在PFCP会话的所有PDR中，在查找与传入报文匹配的PDR时，如果PDR的优先级在PFCP会话的所有PDR中被应用，则该IE应该出现。
PDI|Conditional|如果在PDI中有变化，则该IE将会出现，当出现该IE时，该IE将替换先前存储在用户面网元中的PDI。
FAR ID|Conditional|如果需要更改，该IE将会出现。
URR ID|Conditional|如果要应用测量动作或不再应用于匹配该PDR的报文，则该IE应出现。当出现时，该IE应包含所有需要关联到PDR的URR标识列表。
QER ID|Conditional|如果要应用QoS强制动作或不再应用于匹配该PDR的报文，则该IE应出现。当出现时，该IE应包含所有需要关联到PDR的QER标识的列表。
Activate Predefined Rules|Conditional|如果需要为PDR激活新的预定义规则，则该IE应出现。当呈现该IE时，该IE应包含一个预定义规则名称。可能存在多个具有相同IE类型的IE来表示多个“激活预定义规则”名称。
Deactivate Predefined Rules|Conditional|如果需要为PDR去激活预定义规则，则该IE应该存在。当呈现该IE时，该IE应包含一个预定义规则名称。可能存在多个具有相同IE类型的IE来表示多个“激活预定义规则”名称。
##### Update FAR 
IE|Presence requirement|说明
---|---|---
FAR ID|Mandatory|该IE应标识要更新的FAR。
Apply Action|Conditional|如果改变，该IE将会出现。
Update Forwarding parameters|Conditional|如果改变，该IE将会出现。
Update Duplicating Parameters|Conditional|如果改变，该IE将会出现。可能存在多个IE类型相同的IE，请求将数据包复制到不同的目的地。
BAR ID|Conditional|如果需要修改与FAR相关的BAR ID，则该IE将出现。
##### Update URR 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE将在为该PFCP会话配置的所有URR中唯一标识URR。
Measurement Method|Mandatory|如果需要修改测量方法，该IE将会出现。该IE应指示测量网络资源使用情况的方法，即是否测量数据量、持续时间，或事件。
Reporting Triggers|Mandatory|如果需要修改报告触发，则该IE将出现。该IE应指示触发，用于向控制面网元报告网络资源使用情况，例如周期上报、达到阈值时上报。
Measurement Period|Conditional|如果需要修改测量周期，该IE将会出现。当出现时，它应指示使用报告的产生和报告的周期。
Volume Threshold|Conditional|如果需要修改流量阈值，则该IE应出现。当出现流量阈值时，该IE应指示用户面网元向该URR的控制面网元上报网络资源使用情况的流量。
Volume Quota|Conditional|如果需要修改流量配额，则该IE应出现。当出现时，它应指示流量配额值。
Event Threshold|Conditional|如果需要修改事件阈值，则该IE应出现。当出现事件阈值时，该IE应指示用户面网元向控制面网元上报该URR的事件数。
Event Quota|Conditional|如果需要修改事件配额，则该IE应出现。当出现时，它应指示事件配额值。
Time Threshold|Conditional|如果需要修改时间阈值，则该IE应出现。当出现时，它应该指示用户面网元向控制面网元报告网络资源使用情况的时间使用情况。
Time Quota|Conditional|如果需要修改时间配额，则该IE应出现。当出现时，它应指示时间配额值。
Quota Holding Time|Conditional|如果需要修改Quota Holding Time，则该IE应出现。当出现时，它应包含不活动期间的持续时间。
Dropped DL Traffic Threshold|Conditional|如果需要修改下行流量被丢弃的阈值，则该IE应出现。当出现时，它应包含下行流量被丢弃的阈值。
Monitoring Time|Conditional|如果需要修改监控时间，则该IE应出现。当出现时，该IE应包含用户面网元应重新应用流量或时间阈值的时间。
Subsequent Volume Threshold|Conditional|如果需要修改Subsequent Volume Threshold，并且使用基于时间的测量，则该IE应出现。当出现该值时，应指示该URR在超过监控时间之后的，用户面网元向控制面网元上报网络资源使用情况的流量阈值。
Subsequent Time Threshold|Conditional|如果需要修改Subsequent Time Threshold，则该IE应出现。当出现时，它应指示在超过监视时间之后，用户面网元向控制面网元上报网络资源使用情况的使用时间阈值。
Subsequent Volume Quota|Conditional|如果需要修改Subsequent Volume Quota，则该IE应出现。当出现时，它应指示在超过监视时间之后，用户面网元向控制面网元上报流量配额值。
Subsequent Time Quota|Conditional|如果需要修改Subsequent Time Quota，则该IE应出现。当出现时，它应指示在超过监视时间之后，用户面网元向控制面网元上报时间配额值。
Subsequent Event Threshold|Optional|如果需要修改Subsequent Event Threshold，则该IE应出现。当出现时，它应指示在超过监视时间之后，用户面网元向控制面网元上报事件阈值。
Subsequent Event Quota|Optional|如果需要修改Subsequent Event Quota，则该IE应出现。当出现时，它应指示在超过监视时间之后，用户面网元向控制面网元上报事件配额。
Inactivity Detection Time|Conditional|如果需要修改Inactivity Detection Time，则该IE应出现。当出现时，应包含不活动周期的持续时间。
Linked URR ID|Conditional|如果需要链接使用报告，则该IE应出现。当出现此IE时，该IE应包含与此URR相关的链接URR ID。可能存在多个IE类型相同的IE来表示与该URR相关的多个链接URR。
Measurement Information|Conditional|如果下列标志中的任何一个设置为1，则必须包含此IE。适用的标志有：未激活测量标志：如果测量应暂停（非活动） ，该标志应设为1。如果该比特位为0或更新URR信元中没有测量信息信元，则进行测量（激活）。减少应用检测信息标志：该标志可以设置为1，如果上报触发请求上报应用的启动或停止，则请求用户面网元只上报应用检测信息中的应用ID，例如信封上报。立即开始时间计量标志：如果使用基于时间的度量，则可以将该标志置为1，并要求在接收到标志时立即启动计时计量。
Time Quota Mechanism|Conditional|如果需要修改基于CTP或DTP的基于时间的测量，该IE应该出现。
Aggregated URRs|Conditional|如果需要修改聚合的URR信元，则必须包含该IE。可能存在多个IE类型相同的IE，用于提供多个聚合的URR。当出现时，该IE应提供聚合的URR的完整列表。
FAR ID for Quota Action|Conditional|如果需要修改FAR ID for Quota Action，则该信元应该存在。如果URR中新增了Volume Quota IE或Time Quota IE或Event Quota IE，且用户面网元指示支持配额动作，则该IE可能出现。当出现时，当耗尽URR相关的流量的任何一个配额时，它应包含与该URR相关联的流量的替代标识符。
Ethernet Inactivity Timer|Conditional|如果需要修改Ethernet Inactivity Timer，则该信元应该存在。当出现时，它将包含以太网不活动周期的持续时间。
Additional Monitoring Time|Optional|如果需要修改Additional Monitoring Time，则该信元应该存在。当出现时，该IE应包含用户面网元应重新应用在IE中发放的流量或时间或事件阈值/配额的时间。
##### Update QER 
IE|Presence requirement|说明
---|---|---
QER ID|Mandatory|该IE将在为该PFCP会话配置的所有QER中唯一标识QER。
QER Correlation ID|Conditional|如果需要修改该QER中的QER关联ID，则该IE应该出现。
Gate Status|Conditional|如果需要修改Gate Status，则应该有这个IE。当出现时，它应该指示数据包是否允许转发或者在上行和/或下行方向被丢弃。
Maximum Bitrate|Conditional|如果需要修改匹配该PDR的报文的MBR执行动作，则该IE应出现。当出现时，该IE应指示匹配PDR的数据包的上行和/或下行最大比特率。对于EPC，该信元可以设置为：APN-AMBR，对于一个PDN连接的non-GBR承载的所有PDR引用的QER；TDF会话MBR，用于TDF会话的所有PDR引用的QER；承载MBR，用于承载的所有PDR引用的QER；一个SDF的MBR，用于一个SDF的所有PDR引用的QER。对于5GC，该IE可以设置为：Session-AMBR，用于一个PDU会话的non-GBR QoS流的所有PDR引用的QER；QoS流MBR，用于QoS流的所有PDR引用的QER；一个SDF的MBR，用于一个SDF的所有PDR引用的QER。
Guaranteed Bitrate|Conditional|如果需要修改匹配该PDR的报文的GBR授权，则该IE应显示，当该IE显示时，该IE应指示授权的上行和/或下行保证比特率。该信元可以设置为：聚合GBR，用于GBR承载的所有PDR引用的QER；QoS流GBR，用于QoS流的所有PDR引用的QER (5GC) ；一个QER的SDF的GBR，被SDF的所有PDR引用。
Packet Rate|Conditional|如果需要对匹配该PDR的报文修改报文速率执行动作（即每时间间隔的报文数量），则该IE应出现。
DL Flow Level Marking|Conditional|如果需要修改下行流级别标记IE，则需要设置该IE。
QoS flow identifier|Conditional|如果需要修改，该IE将会出现。
Reflective QoS|Conditional|如果需要修改，该IE将会出现。
Paging Policy Indicator|Conditional|如果需要修改，该IE将会出现。
Averaging Window|Optional|如果需要用户面网元修改使用的平均窗口，则可能存在此IE。
##### Update BAR 
IE|Presence requirement|说明
---|---|---
BAR ID|Mandatory|该IE应标识要修改的BAR。
Downlink Data Notification Delay|Conditional|如果用户面网元指示支持下行数据通知延迟参数，并且需要修改下行数据通知延迟，则该IE应出现。当应用动作参数请求缓存报文并通知控制面网元时，应包含延迟用户面网元在接收下行数据包和通知控制面网元之间的延迟。
Suggested Buffering Packets Count|Conditional|如果用户面网元指示支持该特性UDBC，则该IE可能出现。当应用动作参数请求缓存报文时，应包含建议缓存的报文个数，超过限制的报文将被丢弃
##### Remove PDR 
IE|Presence requirement|说明
---|---|---
PDR ID|Mandatory|该IE将在为该PFCP会话配置的所有PDR中唯一标识PDR。
##### Remove FAR 
IE|Presence requirement|说明
---|---|---
FAR ID|Mandatory|该IE将在为该PFCP会话配置的所有FAR中唯一标识FAR。
##### Remove URR 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE将在为该PFCP会话配置的所有URR中唯一标识URR。
##### Remove QER 
IE|Presence requirement|说明
---|---|---
QER ID|Mandatory|该IE将在为该PFCP会话配置的所有QER中唯一标识QER。
##### Remove BAR 
IE|Presence requirement|说明
---|---|---
BAR ID|Mandatory|该IE将在为该PFCP会话配置的所有BAR中唯一标识BAR。
##### Query URR 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE应标识查询的URR。
##### Query URR Reference 
IE|说明
---|---
Query URR Reference|该IE包含对URR的查询请求的引用。
##### Create Traffic Endpoint 
IE|Presence requirement|说明
---|---|---
Traffic Endpoint ID|Mandatory|该IE将唯一标识该会话的流量端点。
Local F-TEID|Optional|如果存在，该IE应识别本地F-TEID以匹配收到的报文。如果用户面网元支持分配F-TEID，控制面网元请求用户面网元为流量端点分配本地F-TEID，则控制面网元应该将CHOOSE (CH) 比特设置为1。
Network Instance|Optional|如果存在，则该IE应标识与接收的报文匹配的网络实例。
UE IP address|Optional|如果存在，该IE应标识源或目的IP地址以匹配接收的数据包。
Ethernet PDU Session Information|Optional|该IE可用于标识匹配以太网PDU会话的所有(DL)以太网数据包
Framed-Route|Optional|如果UPF指示支持Framed-Route，则该IE可能出现在下行PDR中。如果存在，该IE应描述一个成帧路由。可能会有几个IE类型相同的IE来提供一个成帧路由列表。
Framed-Routing|Optional|如果UPF指示支持Framed-Routing，则该IE可能出现在下行PDR中。如果存在，该IE应描述与成帧路由关联的成帧路由。
Framed-IPv6-Route|Optional|如果UPF指示支持Framed-Routing，则该IE可能出现在下行PDR中。如果存在，该IE应描述一个成帧的IPv6路由。可能会有几个IE类型相同的IE来提供IPv6路由帧的列表。
##### Created Traffic Endpoint 
IE|Presence requirement|说明
---|---|---
Traffic Endpoint ID|Mandatory|该IE将唯一标识该会话的流量端点。
Local F-TEID|Conditional|如果用户面网元分配了F-TEID，则该IE应该存在，并且应该包含用于此流量端点的本地F-TEID
##### Update Traffic Endpoint 
IE|Presence requirement|说明
---|---|---
Traffic Endpoint ID|Mandatory|该IE将唯一标识该会话的流量端点。
Local F-TEID|Conditional|如果需要更改，该IE将会出现。如果用户面网元支持F-TEID分配，控制面网元请求用户面网元为PDR分配本地F-TEID，则控制面网元应设置为1。
Network Instance|Optional|如果存在，则该IE应标识与接收的报文匹配的网络实例。
UE IP address|Conditional|如果需要更改，该IE将会出现
Framed-Route|Conditional|如果UPF指示支持Framed-Route且需要更改，则该IE可能出现在下行PDR中。如果存在，该IE应描述一个成帧路由。可能会有几个IE类型相同的IE来提供一个成帧路由列表。
Framed-Routing|Conditional|如果UPF指示支持Framed-Routing且需要更改，则该IE可能出现在下行PDR中。如果存在，该IE应描述与成帧路由关联的成帧路由。
Framed-IPv6-Route|Conditional|如果UPF指示支持Framed-Routing且需要更改，则该IE可能出现在下行PDR中。如果存在，该IE应描述一个成帧的IPv6路由。可能会有几个IE类型相同的IE来提供IPv6路由帧的列表。
##### Remove Traffic Endpoint 
IE|Presence requirement|说明
---|---|---
Traffic Endpoint ID|Mandatory|该IE应标识要删除的流量端点。
##### Additional Usage Reports Information 
IE|说明
---|---
Additional Usage Reports Information|该IE要么指示后续有additional usage reports ，要么包含在用以响应PFCP会话修改请求查询URR附加的PFCP会话报告请求消息中需要发送的使用报告的数量。
##### Overload Control Information 
IE|Presence requirement|说明
---|---|---
Overload Control Sequence Number|Mandatory|过载控制序列号包含了与过载控制信息信元关联的序列号。
Overload Reduction Metric|Mandatory|减负荷指标的取值范围为0~100（包含），表示过载控制信息的发送方请求接收方申请流量的百分比。
Period of Validity|Mandatory|有效期是指OCI信元指定的过载条件被认为是有效的时间长度（除非后续新的过载控制信息覆盖）。
Overload Control Information Flags|Conditional|如果该IE中的任何一个标志置位，则必须包含该IE。
##### Load Control Information 
IE|Presence requirement|说明
---|---|---
Load Control Sequence Number|Mandatory|该IE指示包含一个值，该值指示与LCI关联的序列号。该序列号应用于区分同一个用户面网元在两不同实例中生成的两LCI信元。
Load Metric|Mandatory|该IE应指示源节点的当前负载水平。
##### PFCPSMReq-Flags 
IE|说明
---|---
PFCPSMReq-Flags|该信元表示适用PFCP会话修改请求消息的标志。包括：DROBU (Drop Buffered Packets)SNDEM (Send End Marker Packets)QAURR (Query All URRs)等。
##### Error Indication Report 
IE|Presence requirement|说明
---|---|---
Remote F-TEID|Mandatory|该IE应标识在用户面网元接收到错误指示的GTP-U承载的远端F-TEID。可以包括多个具有这种类型的IE来表示多个远端F-TEID，该远端F-TEID已经接收到错误指示。
##### Usage Report（within PFCP Session Modification Response） 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE应标识上报使用的URR。
UR-SEQN|Mandatory|该IE应唯一标识URR的使用报告。
Usage Report Trigger|Mandatory|该IE应标识该报告的触发条件。
Start Time|Conditional|除非使用报告触发器指示“流量开始”、“停止流量”或“MAC地址上报”，否则该IE将出现。当出现此IE时，该IE将提供该报告中的信息收集开始时的时间戳。
End Time|Conditional|除非使用报告触发器指示“流量开始”、“停止流量”或“MAC地址上报”，否则该IE将出现。当出现此IE时，该IE将提供该报告生成时的时间戳。
Volume Measurement|Conditional|如果需要上报流量测量，则该IE应出现。
Duration Measurement|Conditional|如果需要上报时长测量，则该IE应出现。
Time of First Packet|Conditional|如果适用此URR，该IE将会出现。
Time of Last Packet|Conditional|如果适用此URR，该IE将会出现。
Usage Information|Conditional|如果用户面网元在监控时间前后上报使用报告，或者QoS执行前后上报使用报告，则应显示该IE，当出现该IE时，应指示该使用是否在该监控时间之前或之后，或在QoS执行前或之后。
Query URR Reference|Conditional|如果在PFCP会话修改请求中接收到的该使用报告（作为查询URR的结果），并且在PFCP会话修改请求中出现了查询URR参考IE，则该IE应该出现。当出现时，应设置为在PFCP会话修改请求中接收到的查询URR参考值。
Ethernet Traffic Information|Conditional|如果需要上报以太网流量信息，则该IE应出现。
##### Usage Report（within PFCP Session Deletion Response） 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE应标识上报使用的URR。
UR-SEQN|Mandatory|该IE应唯一标识URR的使用报告。
Usage Report Trigger|Mandatory|该IE应标识该报告的触发条件。
Start Time|Conditional|除非使用报告触发器指示“流量开始”、“停止流量”或“MAC地址上报”，否则该IE将出现。当出现此IE时，该IE将提供该报告中的信息收集开始时的时间戳。
End Time|Conditional|除非使用报告触发器指示“流量开始”、“停止流量”或“MAC地址上报”，否则该IE将出现。当出现此IE时，该IE将提供该报告生成时的时间戳。
Volume Measurement|Conditional|如果需要上报流量测量，则该IE应出现。
Duration Measurement|Conditional|如果需要上报时长测量，则该IE应出现。
Time of First Packet|Conditional|如果适用此URR，该IE将会出现。
Time of Last Packet|Conditional|如果适用此URR，该IE将会出现。
Usage Information|Conditional|如果用户面网元在监控时间前后上报使用报告，或者QoS执行前后上报使用报告，则应显示该IE，当出现该IE时，应指示该使用是否在该监控时间之前或之后，或在QoS执行前或之后。
Ethernet Traffic Information|Conditional|如果需要上报以太网流量信息，则该IE应出现。
##### Usage Report（within PFCP Session Report Request） 
IE|Presence requirement|说明
---|---|---
URR ID|Mandatory|该IE应标识上报使用的URR。
UR-SEQN|Mandatory|该IE应唯一标识URR的使用报告。
Usage Report Trigger|Mandatory|该IE应标识该报告的触发条件。
Externed Usage Report Trigger|Optional|该IE标识该报告的触发条件。例如，Tethering的开启关闭状态有变化。
Start Time|Conditional|除非使用报告触发器指示“流量开始”、“停止流量”或“MAC地址上报”，否则该IE将出现。当出现此IE时，该IE将提供该报告中的信息收集开始时的时间戳。
End Time|Conditional|除非使用报告触发器指示“流量开始”、“停止流量”或“MAC地址上报”，否则该IE将出现。当出现此IE时，该IE将提供该报告生成时的时间戳。
Volume Measurement|Conditional|如果需要上报流量测量，则该IE应出现。
Duration Measurement|Conditional|如果需要上报时长测量，则该IE应出现。
Application Detection Information|Conditional|如果需要上报应用检测信息，则该IE应出现。
UE IP address|Conditional|如果检测到应用程序的启动或停止，并且在PDI中没有配置UE的IP地址，则应该出现此IE。
Network Instance|Conditional|如果检测到应用程序的启动或停止，在PDI中没有配置UE的IP地址，并且在UP功能中使用了多个IP地址重叠的PDNs，则该IE应该出现。
Time of First Packet|Conditional|如果适用此URR，该IE将会出现。
Time of Last Packet|Conditional|如果适用此URR，该IE将会出现。
Usage Information|Conditional|如果用户面网元在监控时间前后上报使用报告，或者QoS执行前后上报使用报告，则应显示该IE，当出现该IE时，应指示该使用是否在该监控时间之前或之后，或在QoS执行前或之后。
Query URR Reference|Conditional|如果在PFCP会话修改请求中接收到的该使用报告（作为查询URR的结果），并且在PFCP会话修改请求中出现了查询URR参考IE，则该IE应该出现。当出现时，应设置为在PFCP会话修改请求中接收到的查询URR参考值。
Event Time Stamp|Conditional|如果报告与事件有关，则该IE应出现。当出现时，应设置为事件发生的时间。可能存在多个IE类型相同的IE，以上报该URR标识的多个事件。
Ethernet Traffic Information|Conditional|如果需要上报以太网流量信息，则该IE应出现。
##### Downlink Data Report 
IE|Presence requirement|说明
---|---|---
PDR ID|Mandatory|该IE应标识在用户面网元接收到下行数据包的PDR。可以包含多个具有这种类型的IE来表示接收到下行数据包的多个PDR。
Downlink Data Service Information|Conditional|对于具有IP PDN类型的PFCP会话，如果用户面网元支持寻呼策略差异化特性，则必须包含该IE。对于每个PDR，对于每一个触发下行数据通知的报文，用户面网元应该将来自PGW的GTP-U报文的IP载荷中接收的信息内TOS (IPv4) 或TC (IPv6) 中的DSCP值复制到该IE中的Paging策略指示值中。对于5GC，如果下行数据包的QFI可用，针对每个PDR和触发下行数据通知的每个数据包，应该将此IE也应包含在N4接口消息中。消息中上报的PDR标识必须包含一个该类型的IE，当消息中有多个PDR标识IE时，下行数据业务信息信元按照PDR标识信元的顺序上报。
##### Report Type 
IE|说明
---|---
Report Type|用户面网元发送给控制面的报告类。其取值可以为：DLDR (Downlink Data Report)USAR (Usage Report)ERIR (Error Indication Report)UPIR (User Plane Inactivity Report)等。
##### 3GPP Interface Type 
IE|说明
---|---
3GPP Interface Type|3GPP Interface Type IE在PDR信元中的用于指示源接口的3GPP接口类型，在FAR信元中的用于指示目标接口的3GPP接口类型。3GPP Interface Type IE的取值范围及含义为：0：S1-U1：S5 /S8-U2：S4-U3：S11-U4：S12-U5：Gn/Gp-U6：S2a-U7：S2b-U8：eNodeB GTP-U interface for DL data forwarding9：eNodeB GTP-U interface for UL data forwarding10：SGW/UPF GTP-U interface for DL data forwarding11：N3 3GPP Access12：N3 Trusted Non-3GPP Access13：N3 Untrusted Non-3GPP Access14：N3 for data forwarding15：N916：SGi17：N618：N1919 to 64：备用
### N9接口 
#### N9接口协议简介 
场景描述 :N9接口为UPF和UPF之间的用户面接口，用于传递UPF间的上行、下行用户数据流。
协议栈 :N9接口采用GTPv1-U协议，支持3GPP TS 29.281协议。对应的用户面接口协议栈如[图1](#T_1608620810490__42304476-af57-491e-8797-f7038c12418e)所示。
图1  N9接口协议栈
[]images/image.png)
##### 消息列表 
N9接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
Echo Request|UPF<->UPF|该消息用于探测通信路径和对端设备是否工作正常。
Echo Response|UPF<->UPF|该消息用于返回Echo Request消息的请求结果。
Supported Extension Headers Notification|UPF<->UPF|该消息用于指示所识别的IP地址上的GTP实体能够支持的扩展头列表。
Error Indication|UPF<->UPF|当GTP-U节点收到G-PDU数据包，但是找不到对应用户的上下文时，会丢弃该G-PDU数据包，此时如果G-PDU数据包携带的TEID不是全0，则会回复Error Indication。
End Marker|UPF<->UPF|End Marker消息是End Marker Indication的响应消息，在收到End Marker Indication消息之后，会回复End Marker消息。在5GC网络中，通过数据转发隧道发送的End Marker报文，应该与PDU Session Container扩展头一起发送，其中包括映射到同一个E-RAB的其中一个QoS流的流标识。数据转发隧道用于在5GS和EPS之间进行数据转发。
#### 相关消息解释 
##### Echo Request 
消息功能 :GTP-U的一端可以在路径上向另一端发送Echo Request消息来检测对端是否正常。
Echo Request消息可以在每一条正在使用的路径上发送。如果一条路径被至少一个PDP上下文、EPS承载、PDU会话、MBMS UE上下文，或者MBMS承载上下文用于GTP-U端点，则认为该路径正在被使用。
Echo Request消息的发送时间和发送频率取决于产品具体实现，但每条路径上发送Echo Request消息的时间间隔不能低于60秒。但是这种时间限制有一个例外场景，如果T3-RESPONSE定时器超时，Echo Request仍可以不断重发。 
如果路径没有在使用，GTP-U一端也会时刻准备接收Echo Request消息，并回复Echo Response消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
##### Echo Response 
消息功能 :Echo Response消息是作为接收到的Echo Request消息的响应消息。 
Recovery信元中的Restart Counter值不使用。发送方应将该值置为0，接收方应忽略该值。 
由于兼容性原因，Recovery信元是必选的。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Recovery|Mandatory|该信元为必选信元，Recovery信元中的Restart Counter（重启计数器）值不使用，应该由发送实体设置为0，接收实体忽略该值。由于兼容性原因，该信元在GTP用户面使用。
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
##### Supported Extension Headers Notification 
消息功能 :该消息指示指定IP地址上的GTP实体能够支持的扩展头列表。
只有当GTP实体需要解析必选的扩展头，但该GTP实体尚未被升级以支持扩展头时，才发送该消息。 
发送此消息的GTP端点被标记为不支持某些扩展头（源自支持的扩展头列表）。对端GTP实体可能会重试使用该节点的所有扩展头，试图验证它是否已经被升级。如果本端GTP实体已经指示某些扩展头无法被解析，对端GTP实体应避免重复尝试使用这些未知扩展头。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Extension Header Type List|Mandatory|该信元为必选信元。该信元包含“n”扩展头类型的列表。Length字段设置为包含的扩展头类型个数。
##### Error Indication 
消息功能 :当GTP-U节点收到一个没有EPS承载上下文、PDP上下文、PDU会话、MBMS承载上下文或RAB的G-PDU数据包时，GTP-U节点将丢弃该G-PDU数据包。同时当收到的G-PDU数据包携带的TEID不是全0，则会回复Error Indication。
GTP实体包括“UDP Port”扩展头（0x40类型），以简化在某些场景下能够降低DoS攻击风险的机制的实现。
相关信元 :IE|Presence requirement|简要说明
---|---|---
Tunnel Endpoint Identifier Data I|Mandatory|该信元为必选信元，该信元包含GTP实体在用户面使用的隧道端点标识。信元值是从触发此过程的G-PDU中获取的TEID。
GTP-U Peer Address|Mandatory|该信元为必选信元，该信元包含GTP实体在用户面使用的隧道端点地址。信元值是从触发此过程的G-PDU中获取的目的地址。
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
##### End Marker 
消息功能 :最后一个G-PDU在GTP-U隧道上发送之后，或者收到End Marker Indication之后，会发送End Marker消息。 
在5GC网络中，通过数据转发隧道发送的End Marker报文，应该与PDU Session Container扩展头一起发送，其中包括映射到同一个E-RAB的其中一个QoS流的流标识。
数据转发隧道用于在5GS和EPS之间进行数据转发。
相关信元 :IE|Presence requirement|简要说明
---|---|---
Private Extension|Optional|该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
#### 相关信元解释 
##### Information Element Types 
IE|说明
---|---
Information Element Types|GTP-U信令消息中包含多个信元。GTP信元采用TLV(Type， Length，Value)或TV(Type， Value)编码格式。在信令消息中，信元按照Type字段升序排列。Length字段包含除了Type+Length字段的长度。对于所有Length字段，最低编号octet的第8位为最高位，最高编号octet的第1位为最低位。
##### Recovery 
IE|说明
---|---
Recovery|重启计数器的值应该由发送实体设置为0，接收实体忽略。由于兼容性原因，该信元在GTP用户面使用。
##### Tunnel Endpoint Identifier Data I 
IE|说明
---|---
Tunnel Endpoint Identifier Data I|该信元包含GTP实体在用户面使用的隧道端点标识。
##### GTP-U Peer Address 
IE|说明
---|---
GTP-U Peer Address|该信元包含GTP实体在用户面使用的隧道端点地址。
##### Extension Header Type List 
IE|说明
---|---
Extension Header Type List|该信元包含“n”扩展头类型的列表。Length字段设置为包含的扩展头类型个数。
##### Private Extension 
IE|说明
---|---
Private Extension|该信元包含厂商的特定信息。扩展标识是在最近的“Assigned Numbers”RFC（RFC 1700及以上版本）中的私有企业号码列表中定义的一个值。该信元为可选信元，可以在任何GTP信令消息中携带。信令消息中可以携带多个Private Extension类型的信元。
### N26接口 
#### N26接口协议简介 
场景描述 :N26接口为MME和AMF间的信令面接口。 
协议栈 :N26接口协议栈如[图1](#T_1608520734601__599755fb-1585-4813-8c70-b9eb88de7f70)所示。
图1  N26接口协议栈
[]images/image.png)
##### 消息列表 
N26接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
Identification Request|MME→AMF|在附着流程中，如果UE用临时标识来标识自身，该临时标识为5G临时标识映射得到，则目标MME将通过N26接口向AMF发送该消息，用于请求UE IMSI信息。注：识别请求消息仅可由MME通过N26接口发送给AMF，但不能从AMF发送到MME。
Identification Response|AMF→MME|附着流程中，AMF将通过N26接口发送此消息给目标MME以回复之前发送过来的Identification Request消息。
Context Request|MME→AMFAMF→MME|目标侧的MME在EPS和5GS重选流程中通过N26接口向源侧AMF发送该消息，用于获取UE的MM和EPS承载上下文。注：上下文请求消息也可由目标侧AMF在EPS和5GS重选流程中通过N26接口发送给源侧MME。
Context Response|MME→AMFAMF→MME|在EPS和5GS重选流程中，源侧的MME或AMF发送该消息用于响应之前的Context Request消息。
Context Acknowledge|MME→AMFAMF→MME|收到Context Response且原因值为Request accepted时，目标侧MME或AMF发送Context Acknowledge消息，用以响应之前的Context Response消息。
Forward Relocation Request|MME→AMFAMF→MME|在EPS和5GS切换过程中，源侧MME通过N26接口发送该消息给目标侧AMF，作为切换过程中重定位流程的一部分。注：重定位请求消息也可由源侧AMF通过N26接口发送给目标侧MME。
Forward Relocation Complete Notification|MME→AMFAMF→MME|在EPS和5GS切换过程中，目标侧MME通过N26接口发送该消息给源侧AMF用于指示切换已完成。注：重定位完成通知消息也可由目标侧AMF通过N26接口发送给源侧MME。
Forward Relocation Complete Acknowledge|MME→AMFAMF→MME|在EPS和5GS切换过程中，源侧MME或AMF应当发送该消息用以响应之前的Forward Relocation Complete Notification消息。
Relocation Cancel Request|MME→AMFAMF→MME|在EPS和5GS切换取消过程中，源侧MME通过N26接口发送该消息给目标侧AMF用于取消切换。注：重定位取消请求消息也可由源侧AMF通过N26接口发送给目标侧MME。
Relocation Cancel Response|MME→AMFAMF→MME|在EPS和5GS切换取消过程中，目标侧MME或AMF应当发送该消息用以响应之前的Relocation Cancel Response消息。
#### 相关消息解释 
##### Identification Request 
消息功能 :在附着流程中，如果UE用临时标识来标识自身，并且该临时标识为5G临时标识映射得到，则目标MME将通过N26接口向AMF发送该消息，用于请求UE IMSI信息。 
 说明： 
识别请求消息仅可由MME通过N26接口发送给AMF，但不能从AMF发送到MME。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
GUTI|Conditional|全球唯一临时标识。目标侧MME在N26接口携带此信元，当源侧为AMF时，该信元为从4G GUTI映射而来的5G GUTI。信元解释参见GUTI。
Complete Attach Request Message|Conditional|完整的附着请求信息。目标侧MME在N26接口携带此信元，源侧AMF用于完整性检查。信元解释参见Complete Request Message。
Target PLMN ID|Conditional Optional|目标PLMN标识。如果可以，将在N26接口携带此信元，目的是允许源侧AMF判断是否分配一个未使用的鉴权向量。信元解释参见Serving Network。
##### Identification Response 
消息功能 :附着流程中，AMF将通过N26接口发送此消息给目标MME以回复之前发送过来的Identification Request消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|原因值，源侧AMF向目标侧MME返回原因值进行解释。信元解释参见Cause。
IMSI|Conditional|用户IMSI号码，当Cause值为“Request accepted”时携带。信元解释参见IMSI。
UE Usage Type|Conditional Optional|若AMF从UDM收到该信元，该信元需要设置为签约的UE使用类型，并由源侧AMF通过N26接口发送给MME。若AMF无可用的UE使用类型，则该信元的长字段置为0。信元解释参见Integer Number。
##### Context Request 
消息功能 :目标侧的MME在EPS和5GS重选流程中通过N26接口向源侧AMF发送该消息，用于获取UE的MM和EPS承载上下文。 
目标侧的AMF在5GS和EPS重选流程中通过N26接口向源侧MME发送该消息，用于获取UE的MM和EPS承载上下文。 
 说明： 
上下文请求消息也可由目标侧AMF在EPS和5GS重选流程中通过N26接口发送给源侧MME，或者由目标侧MME在5GS和EPS重选流程中通过N26接口发送给源侧AMF。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
IMSI|Conditional|国际移动用户标识，唯一标识一个用户。若目标AMF或MME对UE鉴权成功，则必须携带该字段。信元解释参见IMSI。
GUTI|Conditional|全球唯一临时标识。目标侧MME在N26接口携带此信元。当源侧为AMF时，该信元为从5G GUTI映射而来的4G GUTI。当源侧为MME时，该信元为从4G GUTI映射而来的5G GUTI。信元解释参见GUTI。
Complete TAU request message|Conditional|完整的TAU请求消息。该信元由目标侧通过N26接口传递给源侧，供源侧MME或AMF用于完整性检查。信元解释参见Complete Request Message。
N26 Address and TEID for Control Plane|Conditional|N26接口的控制面地址和TEID。该信元指示了目标侧MME或AMF选择N26的控制面地址和TEID。信元解释参见Fully Qualified TEID (F-TEID)。
RAT Type|Conditional|无线接入类型。指示新侧系统使用的无线接入技术。信元解释参见RAT Type。
Target PLMN ID|Conditional Optional|目标PLMN标识。信元解释参见Serving Network。
##### Context Response 
消息功能 :在EPS和5GS重选流程中，源侧的MME或AMF发送该消息用于响应之前的Context Request消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|原因值，源侧向目标侧指示请求处理结果。信元解释参见Cause。
IMSI|Conditional|国际移动用户标识，唯一标识一个用户。如果用户为无卡用户，则不携带该字段。信元解释参见IMSI。
MME/AMF UE MM Context|Conditional|MME/AMF UE移动管理上下文。如果cause信元值为“Request Accepted”，则需要携带此信元。信元解释参见MM Context。
MME/AMF UE EPS PDN Connections|Conditional|如果在源侧的MME上至少有一条该UE的PDN连接或者在源侧的AMF上至少有一条该UE的PDU会话，则需要携带此信元。需要包含此类型和实例值的多个信元来指示一个PDN连接列表。信元解释参见PDN Connection。
Sender F-TEID for Control Plane|Conditional|发送侧控制面F-TEID。该信元指示了发送侧MME或AMF选择N26的控制面TEID。信元解释参见Fully Qualified TEID (F-TEID)。
Subscribed RFSP Index|Conditional Optional|签约的RFSP（RAT/Frequency Selection Priority）索引。在移动性流程中，如果源侧MME从HSS收到此信元或源侧AMF从UDM收到此信元，则需要在本消息中携带。信元解释参见RFSP Index。
RFSP Index in Use|Conditional Optional|使用的RFSP（RAT/Frequency Selection Priority）索引。在移动性流程中，如果源侧MME或AMF支持RFSP索引，才能携带该信元。信元解释参见RFSP Index。
UE Usage Type|Conditional Optional|若源侧MME从HSS收到该信元，并支持Dedicated Core Networks特性，则该信元需要设置为签约的UE使用类型，并由源侧MME通过N26接口发送给AMF。若源侧AMF从UDM收到该信元，该信元需要设置为签约的UE使用类型，并由源侧AMF通过N26接口发送给MME。源侧AMF或者MME无可用UE使用类型，则该信元的长字段置为0。信元解释参见Integer Number。
RAT Type|Conditional Optional|无线接入类型。指示源侧系统使用的无线接入技术。信元解释参见RAT Type。
IE|Presence requirement|简要说明
---|---|---
APN|Mandatory|接入点名称。信元解释参见Access Point Name (APN)。
APN Restriction|Conditional|APN限制。该信元指示与EPS承载上下文相关的APN的类型组合。目标MME使用APN Restriction决定Maximum APN Restriction。如果可以，源MME需要携带此信元。信元解释参见APN Restriction。
Selection Mode|Conditional Optional|选择模式。如果可以，源侧MME/AMF需要携带此信元。信元解释参见Selection Mode。
IPv4 Address|Conditional|IPv4地址。如果未分配IPv4地址，则不会携带此信元。信元解释参见IP Address。
IPv6 Address|Conditional|IPv6地址。如果未分配IPv6地址，则不会携带此信元。信元解释参见IP Address。
Linked EPS Bearer ID|Mandatory|连接的EPS承载ID。该信元标识PDN连接的默认承载。信元解释参见EPS Bearer ID (EBI)。
PGW S5/S8 IP Address for Control Plane or PMIP|Mandatory|P-GW的S5/S8接口控制面或PMIP地址。如果S5/S8接口的GTP场景，该信元需要携带TEID；如果是S5/S8的PMIP场景，该信元需要携带GRE key。信元解释参见Fully Qualified TEID (F-TEID)。
PGW node name|Conditional Optional|P-GW节点名称。如果源MME或AMF有PGW FQDN，则需要携带此信元。该信元在NF服务发现过程中被目标侧AMF使用，用于在MME向AMF的移动性过程中找到PDU会话的相关SMF+PGW-C。信元解释参见Fully Qualified Domain Name (FQDN)。
Bearer Contexts|Mandatory|承载上下文。需要包含此类型和实例值的多个信元来指示一个承载列表。信元解释参见Bearer Context。
Aggregate Maximum Bit Rate (APN-AMBR)|Mandatory|聚合最大比特速率。信元解释参见Aggregate Maximum Bit Rate (AMBR)。
Charging characteristics|Conditional|计费属性。如果HSS提供给MME的计费属性，或UDM提供给SMF的计费属性，作为签约信息的一部分，则需要携带此信元。信元解释参见Charging Characteristics。
Change Reporting Action|Conditional|变更通报动作。任何时候源MME可以的话，将携带此信元。信元解释参见Change Reporting Action。
CSG Information Reporting Action|Conditional Optional|CSG信息通报动作。任何时候源MME可以的话，将携带此信元。信元解释参见CSG Information Reporting Action。
Indication flags|Conditional Optional|标记位。如果任意一个应用标志设置为1，则该信元需要被携带。Applicable flags:Control Plane Only PDN Connection Indication: 如果PDN Connection设置为Control Plane Only，则该标志位设置为1。信元解释参见Indication。
Signalling Priority Indication|Conditional Optional|如果在建立PDN连接时UE指示低接入优先级，则源MME将携带该信元。信元解释参见Signalling Priority Indication。
PDN Type|Conditional Optional|如上下文请求消息中所示，如果新AMF/MME支持使用SGi的非IP PDN连接，则在跨MME/AMF移动性过程中，源MME/AMF将在N26接口上携带该信元，用于非IP PDN连接。信元解释参见PDN Type。
IE|Presence requirement|简要说明
---|---|---
EPS Bearer ID|Mandatory|EPS承载标识。信元解释参见EPS Bearer ID (EBI)。
TFT|Conditional|业务流模板。如果定义了承载的TFT，则该信元需要被携带。信元解释参见EPS Bearer Level Traffic Flow Template (Bearer TFT)。
SGW S1/S4/S12 IP Address and TEID for user plane|Mandatory|S-GW的S1/S4/S12接口用户面IP地址和TEID。在N26接口上，SMF（代表源侧AMF）应将IP地址和TEID设置如下：TEID：任何保留的TEID值。IP地址：IPv4地址设置为0.0.0.0，或IPv6前缀长度，前缀和接口标识都置为0。信元解释参见Fully Qualified TEID (F-TEID)。
PGW S5/S8 IP Address and TEID for user plane|Conditional|P-GW的S5/S8接口用户面IP地址和TEID。基于S5/S8的GTP隧道需要携带此信元。信元解释参见Fully Qualified TEID (F-TEID)。
Bearer Level QoS|Mandatory|承载级QoS。信元解释参见Bearer Quality of Service (Bearer QoS)。
##### Context Acknowledge 
消息功能 :当之前的Context Response消息被接收且原因值为acceptance时，目标侧MME或AMF发送Context Acknowledge消息，用以响应之前的Context Response消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|原因值。信元解释参见Cause。
Indication flags|Conditional|标志位。如果任意一个应用标志设置为1，则该信元需要被携带。Applicable Flags are：SGWCI: SGW修改标记（SGW change indication），通过N26进行EPS和5GS之间空闲态移动时，该标记应由目标侧AMF或MME设置为1。信元解释参见Indication。
##### Forward Relocation Request 
消息功能 :在EPS和5GS相互切换过程中，源侧MME通过N26接口发送该消息给目标侧AMF，或者源侧AMF通过N26接口发送该消息给目标侧MME，作为切换过程中重定位流程的一部分。 
 说明： 
重定位请求消息也可由源侧AMF通过N26接口发送给目标侧MME。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
IMSI|Conditional|国际移动用户标识，唯一标识一个用户。信元解释参见IMSI。
Sender's F-TEID for Control Plane|Mandatory|发送侧控制面F-TEID。该信元描述了发送侧MME/AMF选择的控制面TEID。信元解释参见Fully Qualified TEID (F-TEID)。
MME/AMF UE EPS PDN Connections|Conditional|需要包含此类型和实例值的多个信元来指示一个PDN连接列表。信元解释参见PDN Connection。
SGW S11/S4 IP Address and TEID for Control Plane|Conditional|S-GW S11/S4控制面地址和TEID。在N26接口上，源侧AMF应将IP地址和TEID设置为以下值：任何保留的TEID（例如全0或全1）。IPv4地址设置为0.0.0.0，或IPv6前缀长度和IPv6前缀和接口标识符都设置为零。信元解释参见Fully Qualified TEID (F-TEID)。
Recovery|Conditional|恢复值。如果是首次与对端节点联络，则需要携带该信元。信元解释参见Recovery。
MME/AMF UE MM Context|Mandatory|MME/AMF UE移动管理上下文。信元解释参见MM Context。
Indication Flags|Conditional|标记位。如果任意一个应用标志设置为1，则该信元需要被携带。Applicable flags are:Direct Forwarding Indication: 如果基于S1切换流程或者跨系统EPS和5GS间切换流程支持直接转发，则该标志位需要设置为1；如果消息用于其它handover流程，则该标志位不能设置为1。Unauthenticated IMSI: 如果消息中的IMSI未经鉴权且为一个紧急附着UE，则该标志位需要设置为1。信元解释参见Indication。
E-UTRAN Transparent Container|Conditional|E-UTRAN透明容器。当该消息应用于UTRAN到E-UTRAN RAT间切换流程、E-UTRAN内部RAT切换流程、SRNS重定位流程、EPS和5GS间切换流程时，Container Type应设置为3。信元解释参见Fully Qualified Container (F-Container)。
Target Identification|Conditional|当该消息应用于SRNS重定位流程、切换到UTRAN/E-UTRAN流程、EPS和5GS切换流程，则消息携带该信元。信元解释参见Fully Qualified Container (F-Container)。
S1-AP Cause|Conditional|S1-AP原因值。该信元信息来源于源侧eNodeB或NG-RAN，则源侧MME或源侧AMF需要在消息中携带该信元。信元解释参见Fully Qualified Cause (F-Cause)。
Subscribed RFSP Index|Conditional Optional|签约的RFSP（RAT/Frequency Selection Priority）索引。在移动性流程中，如果源侧MME从HSS收到此信元或源侧AMF从UDM收到此信元，则需要在本消息中携带。信元解释参见RFSP Index。
RFSP Index in Use|Conditional Optional|使用的RFSP（RAT/Frequency Selection Priority）索引。在移动性流程中，如果源侧MME或AMF支持该特性，才能携带该信元。信元解释参见RFSP Index。
UE Usage Type|Conditional Optional|若源侧MME从HSS收到该信元，并支持Dedicated Core Networks特性，则该信元需要设置为签约的UE使用类型，并由源侧MME通过N26接口发送给AMF。若源侧AMF从UDM收到该信元，该信元需要设置为签约的UE使用类型，并由源侧AMF通过N26接口发送给MME。源侧MME或AMF无可用的UE使用类型，则该信元的长字段置为0。信元解释参见Integer Number。
IE|Presence requirement|简要说明
---|---|---
APN|Mandatory|接入点名称。信元解释参见Access Point Name (APN)。
APN Restriction|Conditional|APN限制。该信元指示与EPS承载上下文相关的APN的类型组合。目标MME使用APN Restriction决定Maximum APN Restriction。如果可以，源MME需要携带此信元。信元解释参见APN Restriction。
Selection Mode|Conditional Optional|选择模式。如果可以，源侧MME/AMF需要携带此信元。信元解释参见Selection Mode。
IPv4 Address|Conditional|IPv4地址。如果未分配IPv4地址，则不会携带此信元。信元解释参见IP Address。
IPv6 Address|Conditional|IPv6地址。如果未分配IPv6地址，则不会携带此信元。信元解释参见IP Address。
Linked EPS Bearer ID|Mandatory|连接的EPS承载ID。该信元标识PDN连接的默认承载。信元解释参见EPS Bearer ID (EBI)。
PGW S5/S8 IP Address for Control Plane or PMIP|Mandatory|P-GW的S5/S8接口控制面或PMIP地址。如果S5/S8接口的GTP场景，该信元需要携带TEID；如果是S5/S8的PMIP场景，该信元需要携带GRE key。信元解释参见Fully Qualified TEID (F-TEID)。
PGW node name|Conditional Optional|P-GW节点名称。如果源MME或AMF有PGW FQDN，则需要携带此信元。该信元在NF服务发现过程中被目标侧AMF使用，用于在MME向AMF的移动性过程中找到PDU会话的相关SMF+PGW-C。信元解释参见Fully Qualified Domain Name (FQDN)。
Bearer Contexts|Mandatory|承载上下文。需要包含此类型和实例值的多个信元来指示一个承载列表。信元解释参见Bearer Context。
Aggregate Maximum Bit Rate (APN-AMBR)|Mandatory|聚合最大比特速率。信元解释参见Aggregate Maximum Bit Rate (AMBR)。
Charging characteristics|Conditional|计费属性。如果HSS提供给MME的计费属性，或UDM提供给SMF的计费属性，作为签约信息的一部分，则需要携带此信元。信元解释参见Charging Characteristics。
Change Reporting Action|Conditional|变更通报动作。任何时候源MME可以的话，将携带此信元。信元解释参见Change Reporting Action。
CSG Information Reporting Action|Conditional Optional|CSG信息通报动作。任何时候源MME可以的话，将携带此信元。信元解释参见CSG Information Reporting Action。
IE|Presence requirement|简要说明
---|---|---
EPS Bearer ID|Mandatory|EPS承载标识。信元解释参见EPS Bearer ID (EBI)EPS Bearer ID (EBI)。
TFT|Conditional|业务流模板。如果定义了承载的TFT，则该信元需要被携带。信元解释参见EPS Bearer Level Traffic Flow Template (Bearer TFT)。
SGW S1/S4/S12 IP Address and TEID for user plane|Mandatory|S-GW的S1/S4/S12接口用户面IP地址和TEID。在N26接口上，SMF（代表源侧AMF）应将IP地址和TEID设置如下：TEID：任何保留的TEID值。IP地址：IPv4地址设置为0.0.0.0，或IPv6前缀长度，前缀和接口标识都置为0。信元解释参见Fully Qualified TEID (F-TEID)。
PGW S5/S8 IP Address and TEID for user plane|Conditional|P-GW的S5/S8接口用户面IP地址和TEID。基于S5/S8的GTP隧道需要携带此信元。信元解释参见Fully Qualified TEID (F-TEID)。
Bearer Level QoS|Mandatory|承载级QoS。信元解释参见Bearer Quality of Service (Bearer QoS)。
##### Forward Relocation Response 
消息功能 :在EPS和5GS切换过程中，目标侧MME或AMF应当发送该消息用以响应之前的Forward Relocation Request消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|原因值。信元解释参见Cause。
Sender's F-TEID for Control Plane|Conditional|发送侧控制面F-TEID。该信元描述了发送侧MME/AMF选择的控制面TEID。如果Cause信元包含值“Request accepted”，则发送侧MME/AMF需要在Forward Relocation Response消息中携带此信元。信元解释参见Fully Qualified TEID (F-TEID)。
Indication Flags|Conditional|标记位。如果任意一个应用标志设置为1，则该信元需要被携带。在通过N26接口进行EPS到5GS切换流程时，SGW Change Indication标志应由目标侧AMF设置为1。信元解释参见Indication。
List of Set-up Bearers|Conditional|建立的承载列表。该信元包含目标系统中handover流程成功分配的承载EPS bearer Identifier。如果源目标接入类型为E-UTRAN或者NG-RAN并且Cause信元包含值“Request accepted”，则携带此信元。需要包含此类型和实例值的多个信元来指示一个承载列表。信元解释参见Bearer Context。
S1-AP Cause|Conditional|S1-AP原因值。如果在S1-AP消息中携带原因值或从NGAP消息中携带原因值导出，则需要携带该信元。信元解释参见Fully Qualified Cause (F-Cause)。
E-UTRAN Transparent Container|Conditional|E-UTRAN透明容器。在切换到E-UTRAN流程、EPS和5GS切换流程中，如果Cause信元包含值“Request accepted”，则Container Type应设置为3。信元解释参见Fully Qualified Container (F-Container)。
IE|Presence requirement|简要说明
---|---|---
EPS Bearer ID|Conditional|EPS承载标识。如果消息用于S1-Based handover，则需要携带此信元。信元解释参见EPS Bearer ID (EBI)。
eNodeB F-TEID for DL data forwarding|Conditional|eNodeB下行数据转发的F-TEID。如果S1AP的消息HANDOVER REQUEST ACKNOWLEDGE中的“SAE Bearers Admitted List”携带DL Transport Layer Address和DL GTP TEID，且应用直接转发和SGW不变的间接转发，则目标MME发送该消息中携带此信元。信元解释参见Fully Qualified TEID (F-TEID)。
SGW/UPF F-TEID for DL data forwarding|Conditional Optional|S-GW/UPF下行数据转发的F-TEID。在LTE和5GC网络的切换过程中，携带此信元，用于间接数据转发。信元解释参见Fully Qualified TEID (F-TEID)。
##### Forward Relocation Complete Notification 
消息功能 :在EPS和5GS切换过程中，目标侧MME通过N26接口发送该消息给源侧AMF用于指示切换已完成。 
 说明： 
重定位完成通知消息也可由目标侧AMF通过N26接口发送给源侧MME。 
##### Forward Relocation Complete Acknowledge 
消息功能 :在EPS和5GS切换过程中，源侧MME或AMF应当发送该消息用以响应之前的Forward Relocation Complete Notification消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|原因值。信元解释参见Cause。
Recovery|Optional|恢复值。如果是首次与对端节点联络，则需要携带该信元。信元解释参见Recovery。
##### Relocation Cancel Request 
消息功能 :在EPS和5GS切换取消过程中，源侧MME通过N26接口发送该消息给目标侧AMF用于取消切换。 
 说明： 
重定位取消请求消息也可由源侧AMF通过N26接口发送给目标侧MME。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
IMSI|Conditional|国际移动用户标识，唯一标识一个用户。如果UE是紧急连接但是IMSI未经过身份验证，则IMSI应该包含于消息中但不用作身份标识。如果UE是紧急连接且UE是UICCless，则IMSI不包含在消息中。信元解释参见IMSI。
ME Identity (MEI)|Conditional|ME身份（MEI）。在以下情况下，ME身份（MEI）应当包含于本信息中：如果UE是紧急连接但是IMSI未经过身份验证。如果UE是紧急连接且UE是UICCless。信元解释参见ME Identity (MEI)。
Indication Flags|Conditional Optional|标记位。如果任意一个应用标志设置为1，则该信元需要被携带。如果UE是紧急连接且IMSI未经过身份验证，则Unauthenticated IMSI标志位应设置为1。信元解释参见Indication。
##### Relocation Cancel Response 
消息功能 :在EPS和5GS切换取消过程中，目标侧MME或AMF应当发送该消息用以响应之前的Relocation Cancel Request消息。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
Cause|Mandatory|原因值。信元解释参见Cause。
#### 相关信元解释 
GUTI :IE|说明
---|---
GUTI|如果管理员决定在MNC只包含两个数字，则字节6比特位5到8编码为“1111”。
##### Complete Request Message 
IE|说明
---|---
Complete Request Message|该信元中Complete Request Message Type取值表示该信元的类型，其取值和意义如下：0，Complete Attach Request Message1，Complete TAU Request Message2-255，备用
##### Serving Network 
IE|说明
---|---
Serving Network|该信元包含MME提供的服务网络。
##### Cause 
IE|说明
---|---
Cause|Cause在响应信息中被携带，指示接受或者拒绝对应的请求信息。其指示的具体拒绝原因，详见表2。Cause也可以在请求信息中被携带，指示请求原因，详见表2。针对该信元中cs、pce、bce信元说明如下：cs：Cause Source。如果该比特为1，指示对应的错误原因源于远程节点（即MME到PGW，或者PGW到MME）。如果该比特为0，指示对应的错误原因源于发送消息的节点。当SGW中转一个从MME到PGW或者从PGW到MME的响应消息时，SGW需要设置cs为1。对于S5/S8的PMIP，当SGW中转一个从PGW到MME的响应消息时，SGW需要携带PMIP原因，并设置cs比特位为1。pce：PDN Connection IE Error。如果该比特为1，指示对应的拒绝原因是由于PDN Connection信元中的错误。bce: Bearer Context IE Error。 如果该比特为1，指示对应的拒绝原因是由于Bearer Context信元中的错误。
Message Type|Cause value (decimal)|Meaning
---|---|---
-|0|保留。不需要被发送，如果收到Cause信元，被视为无效信元。
Request|1|保留
2|Request|Local Detach
3|Request|Complete Detach
4|Request|RAT changed from 3GPP to Non-3GPP
5|Request|ISR deactivation
6|Request|Error Indication received from RNC/eNodeB
7|Request|IMSI Detach Only
8|Request|Reactivation Requested
9 to 12|Request|备用，该范围为请求消息中Cause值保留。
13|Request|Network Failure
14|Request|QoS parameter mismatch
15|Request|备用，该范围为请求消息中Cause值保留。
Acceptance Response|16|Request accepted
17|Acceptance Response|Request accepted partially
18|Acceptance Response|New PDN type due to network preference
19|Acceptance Response|New PDN type due to single address bearer only
20 to 63|Acceptance Response|备用，该范围为响应消息中Cause值保留。
Rejection Response|64|Context Not Found
65|Rejection Response|Invalid Message Format
66|Rejection Response|Version not supported by next peer
67|Rejection Response|Invalid length
68|Rejection Response|Service not supported
69|Rejection Response|Mandatory IE incorrect
70|Rejection Response|Mandatory IE missing
71|Rejection Response|Reserved
72|Rejection Response|System failure
73|Rejection Response|No resources available
74|Rejection Response|Semantic error in the TFT operation
75|Rejection Response|Syntactic error in the TFT operation
76|Rejection Response|Semantic errors in packet filter(s)
77|Rejection Response|Syntactic errors in packet filter(s)
78|Rejection Response|Missing or unknown APN
79|Rejection Response|Reserved
80|Rejection Response|GRE key not found
81|Rejection Response|Relocation failure
82|Rejection Response|Denied in RAT
83|Rejection Response|Preferred PDN type not supported
84|Rejection Response|All dynamic addresses are occupied
85|Rejection Response|UE context without TFT already activated
86|Rejection Response|Protocol type not supported
87|Rejection Response|UE not responding
88|Rejection Response|UE refuses
89|Rejection Response|Service denied
90|Rejection Response|Unable to page UE
91|Rejection Response|No memory available
92|Rejection Response|User authentication failed
93|Rejection Response|APN access denied – no subscription
94|Rejection Response|Request rejected
95|Rejection Response|P-TMSI Signature mismatch
96|Rejection Response|IMSI/IMEI not known
97|Rejection Response|Semantic error in the TAD operation
98|Rejection Response|Syntactic error in the TAD operation
99|Rejection Response|Reserved Message Value Received
100|Rejection Response|Remote peer not responding
101|Rejection Response|Collision with network initiated request
102|Rejection Response|Unable to page UE due to Suspension
103|Rejection Response|Conditional IE missing
104|Rejection Response|APN限制类型与当前激活的PDN连接不一致
105|Rejection Response|Invalid overall length of the triggered response message and a piggybacked initial message
106|Rejection Response|Data forwarding not supported
107|Rejection Response|Invalid reply from remote peer
108|Rejection Response|Fallback to GTPv1
109|Rejection Response|Invalid peer
110|Rejection Response|Temporarily rejected due to handover procedure in progress
111|Rejection Response|Reserved
113|Rejection Response|Apn Congestion
112 and 114 to 219|Rejection Response|备用，该范围为拒绝响应消息中Cause值保留。
220 to 255|Rejection Response|3GPP TS 29.275定义的3GPP Specific PMIPv6 Error Code的保留值
IMSI :IE|说明
---|---
IMSI|IMSI通过GTP隧道传输，发送方复制IMSI的值部分到IMSI信元的值域中。IMSI由三部分组成：Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。不推荐单个MCC区内两个和三个数字混合编码的MNC。Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。
##### Integer Number 
IE|说明
---|---
Integer Number|信元Integer Number的值是由定义在长度字段中的octet个数编码的。例如，当长度字段n等于2时，该信元值的值域是0~65535。信元Integer Number的值需要通过以下信元编码：Maximum Wait Time IE: 长度应设置为2。比如，信元Integer Number的值应编码为一个无符号的16比特整数。DL Buffering Suggested Packet Count IE: 长度应设置为1或2。UE Usage Type IE:长度应设置为1。比如，信元Integer Number的值应编码为一个无符号的8比特整数。
##### Trace Information 
IE|说明
---|---
Trace Information|Trace Information为grouped信元，包含许多其它信元。Trace Information可能在一个消息中重复完全相同的类型和实例值，来表示Trace Informations列表。
##### Fully Qualified TEID (F-TEID) 
IE|说明
---|---
Fully Qualified TEID (F-TEID)|完全认证的TEID。Interface Type：这5个比特位宽整数取值如下，代表接口类型和端点。0:	S1-U eNodeB GTP-U interface1:	S1-U SGW GTP-U interface2:	S12 RNC GTP-U interface3:	S12 SGW GTP-U interface4:	S5/S8 SGW GTP-U interface5:	S5/S8 PGW GTP-U interface6:	S5/S8 SGW GTP-C interface7:	S5/S8 PGW GTP-C interface8:	S5/S8 SGW PMIPv6 interface9:	S5/S8 PGW PMIPv6 interface10:	S11 MME GTP-C interface11:	S11/S4 SGW GTP-C interface12:	S10 MME GTP-C interface13:	S3 MME GTP-C interface14:	S3 SGSN GTP-C interface15:	S4 SGSN GTP-U interface16:	S4 SGW GTP-U interface17:	S4 SGSN GTP-C interface18:	S16 SGSN GTP-C interface19:	eNodeB GTP-U interface for DL data forwarding20:	eNodeB GTP-U interface for UL data forwarding21:	RNC GTP-U interface for data forwarding22:	SGSN GTP-U interface for data forwarding23:	SGW GTP-U interface for DL data forwarding24:	Sm MBMS GW GTP-C interface25:	Sn MBMS GW GTP-C interface26:	Sm MME GTP-C interface27:	Sn SGSN GTP-C interface28: SGW GTP-U interface for UL data forwarding29: Sn SGSN GTP-U interface30: S2b ePDG GTP-C interface31: S2b-U ePDG GTP-U interface32: S2b PGW GTP-C interface33: S2b-U PGW GTP-U interface34: S2a TWAN GTP-U interface35: S2a TWAN GTP-C interface36: S2a PGW GTP-C interface37: S2a PGW GTP-U interface38: S11 MME GTP-U interface39: S11 SGW GTP-U interface其它值空闲保留。
Sender F-TEID for Control Plane|用于标识发送方的控制面F-TEID。如果Delete Session Request消息中携带的Sender F-TEID for Control Plane信元和最近一次的Create Session Request消息或Modify Bearer Request消息中携带的此信元相同，当S-GW收到Sender F-TEID for Control Plane信元时，S-GW会接受Delete Session Request消息。v4: 如果这个比特设置为1，则IPv4地址字段在F-TEID中出现，否则IPv4地址字段将不出现。v6: 如果这个比特设置为1，则IPv6地址字段在F-TEID中出现，否则IPv6地址字段将不出现。spare: 发送方设置为0，接收方忽略将该字段。teid-or-gre-key:如果IPv4和IPv6地址都出现在F-TEID字段中，则TEID指将被两个地址共用。
SGW S11/S4 IP Address and TEID for Control Plane|用于标识S-GW控制面S11/S4接口IP地址和TEID。v4: 如果这个比特设置为1，则IPv4地址字段在F-TEID中出现，否则IPv4地址字段将不出现。v6: 如果这个比特设置为1，则IPv6地址字段在F-TEID中出现，否则IPv6地址字段将不出现。spare: 发送方设置为0，接收方忽略将该字段。teid-or-gre-key:如果IPv4和IPv6地址都出现在F-TEID字段中，则TEID指将被两个地址共用。
PGW S5/S8 Address for Control Plane or PMIP|用于标识P-GW的控制面或PMIP隧道的S5/S8地址。v4: 如果这个比特设置为1，则IPv4地址字段在F-TEID中出现，否则IPv4地址字段将不出现。v6: 如果这个比特设置为1，则IPv6地址字段在F-TEID中出现，否则IPv6地址字段将不出现。spare: 发送方设置为0，接收方忽略将该字段。teid-or-gre-key:如果IPv4和IPv6地址都出现在F-TEID字段中，则TEID指将被两个地址共用。
N26 Address and TEID for Control Plane|用于标识MME/AMF的控制面的N26地址。这个信元是N26接口上携带的。相关信元取值解释如下：v4: 如果这个比特设置为1，则IPv4地址字段在F-TEID中出现，否则IPv4地址字段将不出现。v6: 如果这个比特设置为1，则IPv6地址字段在F-TEID中出现，否则IPv6地址字段将不出现。spare: 发送方设置为0，接收方忽略将该字段。teid-or-gre-key:如果IPv4和IPv6地址都出现在F-TEID字段中，则TEID指将被两个地址共用。
##### RAT Type 
IE|说明
---|---
RAT Type|RAT Type取值:0: reserved1: UTRAN2: GERAN3: WLAN4: GAN5: HSPA Evolution6: EUTRAN(WB-E-UTRAN)7: Virtual8: EUTRAN-NB-IoT9-255: 保留
##### MM Context 
IE|说明
---|---
MM Context|MM Context包含了Mobility Management，在S3/S16/S10/N26接口传输中必须的用户安全参数。
##### RFSP Index 
IE|说明
---|---
RFSP Index|Index to RAT/Frequency Selection Priority (RFSP Index)定义在3GPP TS 36.413中的Subscriber Profile ID for RAT/Frequency priority (SPIRFP)。SPIRFP为1到256之间的整数，两个字节。Subscriber Profile ID for RAT/Frequency priority (SPIRFP) 需要用于定义Idle模式camp priorities，控制Active模式inter-RAT/inter-frequency handover。
##### PDN Connection 
IE|说明
---|---
PDN Connection|PDN Connection为grouped信元，包含许多其它信元。当需要发送一个以上的PDN Connection，则PDN Connection信元在一个消息中重复。这种情况，重复的信元具有相同的实例值用于代表一个分组归类的信元列表。
##### Indication 
IE|说明
---|---
Indication|对于每一个消息的Indication应用标记字段，需要在独立的消息中清晰说明。未按此指示说明的应用标记将被接收端丢弃。如果Indication IE适用于消息但是发送方未携带，则接收方将应用标记视作“0”。Indication Flags为条件信元，任何一个应用标记被设置为1时，需携带此信元。应用标记包括：daf：Dual Address Bearer Flag，该标志位用于S11/S4接口和S5/S8接口，当UE请求和签约数据决定的PDN Type设置为IPv4v6，且所有UE可能接入的MME支持双重地址时，该标志位应该设置为1。基于运营商在节点预配置来决定。dtf：Direct Tunnel Flag，该标志位用于S4接口，如果使用Direct Tunnel，则需要设置为1。hi：Handover Indication，如果UE是从non-3GPP接入，该标志位需要在E-UTRAN Initial Attach or in a UE Requested PDN Connectivity流程中设置。dfi：Direct Forwarding Indication，如果该标志位设置为1，指示应用于S1 based handover procedure流程中，源eNodeB与目标eNodeB之间直接转发。oi：Operation Indication。如果该标志位设置为1，则指出接收方SGW收到“Create Session Request”请求，应该向PGW立即发送“Modify Bearer Request”。这样SGW可以区别对待在S4/S11接口收到“Create Session Request”消息是TAU/RAU流程with an SGW relocation (OI = 1)，或者是X2-based handover with SGW relocation (OI = 1)，或者是S1-based handover with SGW relocation (OI = 0)。如果SGW需要转发Delete Session Request消息给PGW，则在S4/S11接口，该标志位需要设置为1。isrsi：Idle mode Signalling Reduction Supported Indication，如果该标志位设置为1，则指示源/旧侧的MME有能力为UE建立ISR。israi：Idle mode Signalling Reduction Activation Indication，如果该标志位设置为1，则指示TAU/RAU without an SGW change procedure或Inter RAT handover without an SGW change流程中，MME和S4 SGSN之间建立ISR。SGW为核心网节点保留其已经保存的承载资源。源/旧侧的MME保留UE上下文和激活的ISR。sgwci：SGW Change Indication，如果该标志位设置为1，则指示在TAU/RAU or handover with an SGW change流程中，目标MME已选择一个新的SGW。sqci：Subscribed QoS Change Indication，如果该标志位设置为1，则指示在旧侧MME中UE处于ECM-IDLE状态且ISR激活时，PDN连接相关的签约QoS profile发生改变。则新侧MME将触发Subscribed QoS Modification流程，见3GPP TS 23.401章节5.3.9.2。uimsi：Unauthenticated IMSI，如果该标志位设置为1，则指示该消息中的IMSI未鉴权，并且用于紧急附着UE。reserved1：保留。cfsi：Change F-TEID support indication，如果该标志位设置为1，则指示SGW可以在当前流程中改变分配的GTP-U F-TEID。在Idle状态的UE发起的TAU/RAU流程中，MME需要在发送给SGW的Modify Bearer Request消息中包含此标志位。如果在Modify Bearer Request消息中收到CFSI且SGW需要修改GTP-U F-TEID，则SGW需要在Modify Bearer Response消息中携带新的F-TEID。crsi：Change Reporting support Indication，用于S4/S11、S5/S8接口，如果该标志位设置为1，则指示MME location Info Change Reporting机制。ps：Piggybacking Supported，该比特指示MME/SGW是否支持3GPP TS 23.401附件F中所述的piggybacking特性。如果该标志位设置为1，则指示节点有能力处理两个背靠背出现在单UDP载荷中的不同的GTPC消息。pt：Protocol Type，如果该标志位设置为1，则指示S5/S8的协议类型为PMIP，如果设置为0则指示S5/S8的协议类型为GTP。si：Scope Indication，如果该标志位设置为1，则指示UE的所有承载资源将被SGW释放。该标志位在TAU/RAU/Handover/SRNS Relocation Cancel Using S4/Inter RAT handover Cancel procedure with SGW change/S1 Based handover Cancel procedure with SGW change流程消息中设置。msv：MS Validated，如果该标志位设置为1，则指示新侧MME已成功鉴权UE。ccrsi：CSG Change Reporting support indication，如果该标志位设置为1，则指示MME支持CSG Information Change Reporting机制。israu：ISR is activated for the UE，如果该标志位设置为1，则指示在UE移动到新侧MME前，UE的ISR被激活。S11TF: S11–U Tunnel Flag，如果用户数据在NAS信令里被传输，则在S11接口，该标志位需要设置为1。Extended PCO Support Indication flag: 如果UE和源MME支持扩展PCO， 则在源MME N26，该标志位需要设置为1。Control Plane Only PDN Connection Indication: 如果PDN Connection设置为Control Plane Only，该标志位需要设置为1。Buffered DL Data Waiting Indication (BDWI):当该标志被请求转发到缓存在旧的SGW上的UE DL数据中，在带或不带SGW变更流程的TAU/RAU期间，该标志位需要在S3/S10/S16接口设置为1。如，当旧的MME上DL数据缓存有效时间还未过期时，需要设置该标志位为1。
##### Recovery 
IE|说明
---|---
Recovery|如果与对端首次联络，需要携带该信元。
##### Fully Qualified Container (F-Container) 
IE|说明
---|---
Fully Qualified Container (F-Container)|Container Type编码如下：如果这个域设置为1，则F-Container域表示UTRAN transparent container。如果这个域设置为2，则F-Container域表示BSS container。如果这个域设置为3，则F-Container域表示E-UTRAN transparent container。
##### Fully Qualified Cause (F-Cause) 
IE|说明
---|---
Fully Qualified Cause (F-Cause)|GTPv2消息中F-Cause信元的Instance值域指示了是否包含RANAP Cause、BSSGP Cause或者RAN Cause。如果F-Cause域包含RAN Cause，则Cause Type域包含RAN cause子类，详见3GPP TS 36.413并按表8.49-1编码。如果F-Cause域包含BSSGP Cause或RANAP Cause，则其Cause Type域将被接收方忽略。Cause Type:0: Radio Network Layer1: Transport Layer2: NAS3: Protocol4: Miscellaneous5 to15: spare
##### Bearer Context 
IE|说明
---|---
Bearer Context|Bearer Context是一个组合信元，包含许多其它信元。Bearer Context通过一条消息，完全重复表述了相同类型和实例值的承载上下文列表。
##### ME Identity (MEI) 
IE|说明
---|---
Mobile Equipment Identity (MEI)|ME Identity (MEI)包含IMEI或者IMEISV，IMEI/IMEISV均采用BCD编码，其中IMEI是15位BCD编码，IMEISV是16位BCD编码。 对于IMEI，最后八位字节的第5到8位应填充编码为'1111'的结束标记。
##### Access Point Name (APN) 
IE|说明
---|---
Access Point Name (APN)|APN通过GTP隧道传输，发送方复制部分APN值到APN信元值域。APN域需要同时填充APN NI和APN OI，要求如下：APN NI定义GGSN/PGW连接的外部网络和MS可选请求业务。这部分APN是必选的。APN NI应含至少一个标签，编码后长度最多63 octet。APN NI不能以 "rac"，"lac"，"sgsn" 或者"rnc"这些字符串开头，不能以"gprs"这样的字符串结尾或者作为最后一个标签，也不能含有字符 "*"。为了保证APN NI在GPRS/EPS PLMN中的唯一性，APN NI至少含一个标签与Internet域名相对应。APN OI定义GGSN/PGW所在的PLMN GPRS/EPS骨干网。这部分APN为可选。
##### APN Restriction 
IE|说明
---|---
APN Restriction|该信元包含一个无符号整数值，指示为关联APN创建的EPS承载上下文的限制等级。在P-GW中每一个APN配置的APN Restriction值。用于在UE基础决定是否允许为其它APN创建EPS承载。表2列出了APN Restriction的有效组合。
最大APN Restriction值|APN类型|应用实例|允许建立APN Restriction值
---|---|---|---
0|不存在|All|不存在
1|Public-1|MMS|1，2，3
2|Public-2|Internet|1，2
3|Private-1|Corporate（比如MMS使用用户）|1
4|Private-2|Corporate（比如不使用MMS的用户）|None
##### Selection Mode 
IE|说明
---|---
Selection Mode|该信元指示消息中APN的来源。Selection mode values:0: MS或网络提供APN，签约核对。1: MS提供APN，签约不需要核对。2: 网络提供APN，签约不需要核对。3: 保留，不能被发送。如果收到，则解释为“2”。
##### IP Address 
IE|说明
---|---
IP Address|Length域可能只有两个值（4或16），这就决定Value域包含IPv4或IPv6地址。
##### EPS Bearer ID (EBI) 
IE|说明
---|---
EPS Bearer ID (EBI)|L3协议定义标准层三消息字节1比特5到8为EPS承载标识。EPS承载标识用于标识一个消息流。EPS bearer identity value:0 0 0 0: No EPS bearer identity assigned0 0 0 1: Reserved0 0 1 0: Reserved0 0 1 1: Reserved0 1 0 0: Reserved0 1 0 1: EPS bearer identity value50 1 1 0: EPS bearer identity value60 1 1 1: EPS bearer identity value 71 0 0 0: EPS bearer identity value 81 0 0 1: EPS bearer identity value 91 0 1 0: EPS bearer identity value 101 0 1 1: EPS bearer identity value 111 1 0 0: EPS bearer identity value 121 1 0 1: EPS bearer identity value 131 1 1 0: EPS bearer identity value 141 1 1 1: EPS bearer identity value 15
##### Fully Qualified Domain Name (FQDN) 
IE|说明
---|---
Fully Qualified Domain Name (FQDN)|FQDN字段编码需要与DNS消息（IETF RFC 1035章节3.1）中的一致，除了尾部的0所在的字节。按照3GPP TS 29.303章节4.3.2，S3/S10/S16 GTP消息中的“PGW node name”需要是一个PGW主机名。特别地，第一个DNS标签是“topon”或“topoff”，PGW的公认的节点名始于第三个标签。
##### Aggregate Maximum Bit Rate (AMBR) 
IE|说明
---|---
Aggregate Maximum Bit Rate (AMBR)|此信元通过GTP隧道传输，发送方复制部分AMBR的值到AMBR信元的值域（kbps）。网络希望传输上行链路策略的AMBR给UE时，需要携带此信元。
##### Charging Characteristics 
IE|说明
---|---
Charging Characteristics|Charging Characteristics信元在3GPP TS 32.251中定义，是基于运营商配置的触发条件，通知SGW和PGW产生计费信息的规则。计费属性字段允许运营商对CDR使用不同的计费方式，详见3GPP TS 32.298 章节5.1.2.2.7。用户可以在签约数据中指定计费属性。这些属性可以由HLR/HSS提供给MME作为签约信息的一部分。对于激活IP-CAN承载，MME根据TS 32.251 Annex A中规定的规则，将计费属性转发给GGSN/S-GW。
##### Change Reporting Action 
IE|说明
---|---
Change Reporting Action|Action values:0: Stop Reporting1: Start Reporting CGI/SAI2: Start Reporting RAI3: Start Reporting TAI4: Start Reporting ECGI5: Start Reporting CGI/SAI and RAI6: Start Reporting TAI and ECGI7-255: spareStop Reporting终止所有上报动作类型。
##### CSG Information Reporting Action 
IE|说明
---|---
CSG Information Reporting Action|CSG Reporting Action:UCICSG: 当设置为1，指示当UE通过CSG小区进入/离开/接入时，开始上报用户CSG信息。UCISHC: 当设置为1，指示当UE通过Subscribed Hybrid Cell进入/离开/接入时，开始上报用户CSG信息。UCIUHC:当设置为1，指示当UE通过Unsubscribed Hybrid Cell进入/离开/接入时，开始上报用户CSG信息。比特1到3都需要设置为0，停止上报用户CSG信息。
##### Signalling Priority Indication 
IE|说明
---|---
Signalling Priority Indication|该信元包含来自UE指定PDN连接的信令优先级指示。以下是Octet5以内的比特含义：比特2-8：备用，供将来使用并设为0。Bit 1 – LAPI (Low Access Priority Indication):该比特表示建立PDN连接时UE是否指示低访问优先级。比特1需要编码为信元Device Properties的低优先级参数。如果信元Signalling Priority Indication适用于一个消息且发送端的消息中不含有信元Signalling Priority Indication，接收端认为比特1的值为0。低访问优先级指示可能包含在计费记录中。
##### PDN Type 
IE|说明
---|---
PDN Type|基于UE请求和HSS中签约数据（对于MME，见3GPP TS 23.401章节5.3.1.1，对于SGSN，见3GPP TS 23.060章节9.2.1），可以设置为IPv4、IPv6或IPv4v6或Non-IP。PDN类型值:0 0 1: IPv40 1 0: IPv60 1 1: IPv4v61 0 0: 非IP
##### EPS Bearer Level Traffic Flow Template (Bearer TFT) 
IE|说明
---|---
EPS Bearer Level Traffic Flow Template (Bearer TFT)|EPS Bearer Level Traffic Flow Template (Bearer TFT)通过GTP隧道传输。发送方复制EPS Bearer Level TFT的值到EPS Bearer Level TFT信元的值域，详见Traffic flow template。
##### Traffic flow template 
IE|说明
---|---
Traffic flow template|该信元指定一个PDP上下文的TFT参数和操作。另外，该信元可能被用于传输额外参数给网络。TFT可能包含上行、下行或者两个方向的分组过滤器。分组过滤器决定了PDP上下文的网络映射。网络侧使用下行分组过滤器，用户使用上行分组过滤器。双向过滤器在网络侧被用作下行分组过滤器，在用户侧被用作上行分组过滤器。TFT operation code:0 0 0: Spare0 0 1: Create new TFT0 1 0: Delete existing TFT0 1 1: Add packet filters to existing TFT1 0 0: Replace packet filters in existing TFT1 0 1: Delete packet filters from existing TFT1 1 0: No TFT operation1 1 1: ReservedE bit:0: parameters list is not included1: parameters list is includedNumber of packet filters:分组过滤表中分组过滤器的个数，二进制编码格式。对于操作"delete existing TFT"和"no TFT operation"，number of packet filters为0。所有其他操作，number of packet filters需要大于0小于等于16。Packet filter list:对于操作"delete existing TFT"和"no TFT operation"，packet filter list为空。对于操作"delete packet filters from existing TFT"，packet filter list包含一个分组过滤标识变量。对于操作"create new TFT"、"add packet filters to existing TFT"和"replace packet filters in existing TFT"，packet filter list包含分组过滤器变量。packet filter direction指示过滤器应用的流方向：00: pre Rel-7 TFT filter01: downlink only10: uplink only11: bidirectionalpacket filter identifier用于标识TFT中每一个分组过滤器。packet filter evaluation precedence指定一个分组过滤器在这个PDP地址相关的所有TFT内所有分组过滤器中的优先级。值越高，对应过滤器的优先级越低。传输顺序中第一个比特位是最有效的比特位。Packet filter component type identifier:0 0 0 1 0 0 0 0: IPv4 remote address type0 0 1 0 0 0 0 0: IPv6 remote address type0 0 1 1 0 0 0 0: Protocol identifier/Next header type0 1 0 0 0 0 0 0: Single local port type0 1 0 0 0 0 0 1: Local port range type0 1 0 1 0 0 0 0: Single remote port type0 1 0 1 0 0 0 1: Remote port range type0 1 1 0 0 0 0 0: Security parameter index type0 1 1 1 0 0 0 0: Type of service/Traffic class type1 0 0 0 0 0 0 0: Flow label type其它值保留
##### Bearer Quality of Service (Bearer QoS) 
IE|说明
---|---
Bearer Quality of Service (Bearer QoS)|Bearer Quality of Service (Bearer QoS)通过GTP隧道传输。发送方复制Bearer l QoS的部分值到Bearer QoS信元的值域。
### N32接口 
#### N32接口协议简介 
场景描述 :N32接口为SEPP和SEPP间的信令面接口。
协议栈 :N32接口（N32-c和N32-f）采用HTTP 2协议，并将JSON作为应用层串行协议。对于传输层安全保护，SEPP应支持3GPP TS 33.501规定的TLS。 
N32接口协议栈如[图1](#T_1608620810490__42304476-af57-491e-8797-f7038c12418e)所示。
图1  N32接口协议栈
[]images/image.png)
##### 消息列表 
N32接口上支持的消息参见下表。 
消息|方向|作用
---|---|---
SecNegotiateReqData|SEPP->SEPP|该消息用于定义发起SEEP发送到接收SEPP的SEPP安全能力。
SecNegotiateRspData|SEPP->SEPP|该消息用于定义接受SEPP选定的安全能力。
#### 相关消息解释 
##### SecNegotiateReqData 
消息功能 :发起SEPP向响应SEPP发起安全能力协商过程，商定用于保护N32-f上NF服务相关信令的安全机制。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
sender|Mandatory|唯一标识发送请求的SEPP。用于存储SEPP的安全协商能力。
supportedSecCapabilityList|Mandatory|包含请求SEPP支持的安全能力列表。
3GppSbiTargetApiRootSupported|Conditional|如果N32f消息转发支持TLS安全，该信元应存在并指示支持3gpp-Sbi-Target-apiRoot HTTP报头。
plmnIdList|Optional|请求SEPP关联的PLMN ID列表。该列表由接收SEPP存储在N32-f上下文中。
##### SecNegotiateRspData 
消息功能 :响应SEPP向发起SEPP返回其选择的安全能力，商定用于保护N32-f上NF服务相关信令的安全机制。 
相关信元 :IE|Presence requirement|简要说明
---|---|---
sender|Mandatory|唯一标识返回响应的SEPP。用于存储SEPP的安全协商能力。
selectedSecCapability|Mandatory|包含响应SEPP选择的安全能力。
3GppSbiTargetApiRootSupported|Conditional|如果N32f消息转发协商了TLS安全，并且发起SEPP指示支持3gpp-Sbi-Target-apiRoot HTTP报头。该信元应存在并指示支持3gpp-Sbi-Target-apiRoot HTTP报头。
plmnIdList|Optional|响应SEPP关联的PLMN ID列表。该列表由接收SEPP存储在N32-f上下文中。
#### 相关信元解释 
##### sender 
IE|说明
---|---
sender|用于存储SEPP的安全协商能力。
##### supportedSecCapabilityList 
IE|说明
---|---
supportedSecCapabilityList|该信元用于存储请求SEEP支持的安全能力列表。
##### selectedSecCapability 
IE|说明
---|---
selectedSecCapability|该信元包含响应SEPP选择的安全能力。
##### 3GppSbiTargetApiRootSupported 
IE|说明
---|---
3GppSbiTargetApiRootSupported|当该信元存在时，用于指示是否支持使用3gpp-Sbi-Target-apiRoot HTTP报头的TLS安全：true：支持false（默认）：不支持
##### plmnIdList 
IE|说明
---|---
plmnIdList|SEPP关联的PLMN ID列表。
# EPC信令流程 
## 移动性管理 
### Attach 
### Attach 


业务模型 :附着流程是用户注册到EPS网络上的流程，是用户开机后的第一个过程，是后续所有的流程的基础。在附着过程中，EPC网络会为用户建立一个默认承载，也可以对用户进行鉴权（用户首次附着到EPS网络上必须鉴权）。 


信令流程 :EPC信令流程-Attach信令流程图如[图1](01%20Attach.html#concept1__EPC%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-Attachv-28F95F8F)所示。
图1  EPC信令流程-Attach


[]images/EPC%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-Attachv.png)



流程说明 :

UE通过发送 Attach Request消息及包含选择的网络和old GUMMEI的RRC参数到eNodeB发起附着流程。


eNodeB通过RRC参数中的old GUMMEI和指示的选择网络查找到MME。如果得不到MME，就由MME选择功能选择MME。然后eNodeB将Attach Request消息通过初始UE消息及接收到的选择网络和UE所在小区的TAI+ECGI标识一起转发给New MME。


（可选）如果UE通过GUTI识别自己，并且自从去附着后服务UE的MME已经发生变化，New MME通过UE带上来的GUTI找到Old
MME/SGSN地址，再发送一个Identification Request消息给Old MME/SGSN以请求IMSI。如果消息发送到Old
MME/SGSN，Old MME/SGSN过NAS MAC验证Attach Request消息通过后给New MME回Identification
Response消息，其消息包含IMSI和移动性上下文；如果消息发送到老SGSN，老SGSN通过P-TMSI签名验证Attach
Request消息通过后给New MME回标识响应消息，其消息包含移动性上下文；如果UE在Old MME/SGSN中是未知的或如果Attach
Request消息完整性检查或P-TMSI签名检查失败，Old MME/SGSN通过发送携带错误原因值的响应给New MME。


（可选）如果UE在Old MME/SGSN和New MME中都不能被识别，New MME发送Identity Request消息给UE以请求IMSI。UE使用包含IMSI的Identity Response消息通知网络。


（可选）鉴权过程。 


如果网络侧没有UE上下文、或者 Attach Request消息没有完整性保护、或者完整性检查失败，那么必须鉴权。从这步开始，后续的所有NAS消息都将使用NAS安全功能（加密和完整性保护）进行保护。 


从UE获取ME标识。ME标识应加密传输，除非是在紧急附着情况下且不能被认证时。为了最小化信令的延迟，ME标识获取可以合并在步骤5a中的NAS安全建立过程。MME可能发送ME Identity Check Request消息给EIR。EIR给MME回ME Identity Check
Response消息，消息包含检查结果。MME根据检查结果决定是继续Attach流程还是拒绝UE。




（可选）如果UE在Attach Request消息中设置了加密选项传输标识，像PCO或APN或者两者这样的加密选项，现在都可以通过Ciphered Options Request/Response消息从UE获取。这样的PCO选项中可能包含有用户的身份信息，例如用户名和口令字。


（可选）如果在New MME上有用户激活的承载上下文（如没有事先去附着就在同一个MME再次附着），New MME通过发送Delete Session Request消息给GW删除承载。GW给MME回Delete Session Response消息。如果PCRF部署了，PGW执行IP-CAN会话结束过程来指示释放资源。


（可选）如果从UE上次分离后MME改变了，或MME没有UE的有效的签约上下文，或ME标识改变，或如果UE提供的IMSI或者UE提供的Old
GUTI在MME没有关联到有效的上下文，MME发送Update Location Request消息给HSS。


（可选）HSS发送Cancel Location Request消息给Old MME/SGSN。Old
MME/SGSN回应Cancel Location Ack消息，删除MM和承载上下文。


（可选）如果在Old MME/SGSN上有用户激活的承载，Old MME/SGSN通过发送Delete Session
Request消息给相关GW删除承载。GW响应Delete Session Response消息。如果PCRF部署了，PGW执行IP-CAN会话结束过程来指示释放资源。


（可选）HSS发送Update Location Ack消息给New MME，消息包含IMSI、签约数据等。签约数据包含一个或多个PDN签约上下文信息。每一个PDN签约上下文中包含EPS签约QoS参数和签约的APN-AMBR。New
MME验证UE在新TA中存在。如果由于区域签约限制或接入限制，不允许UE附着在该TA中，或者由于其他原因而致使签约检查失败，MME拒绝附着请求。如果检查成功，New
MME给UE创建一个上下文。如果UE所提供的APN是签约所不允许的或HSS拒绝了更新位置，则New MME拒绝附着请求消息。


MME选择PGW和SGW，MME向SGW发送Create Session Request消息。


SGW在其EPS承载列表中创建一个条目，发送Create Session Request消息给PGW。消息中包括IMSI,
MSISDN, APN, Serving GW Address for the user plane, Serving GW TEID
of the user plane, Serving GW TEID of the control plane, RAT type,
Default EPS Bearer QoS, PDN Type, PDN Address, subscribed APN-AMBR,
EPS Bearer Identity, Protocol Configuration Options, ME Identity,
User Location Information (ECGI), UE Time Zone等信息。本步以后，SGW缓存任何从PGW接收的下行分组数据，直到收到23步的Modify
Bearer Request消息，获得eNodeB TEID之后再进行转发。


（可选）如果部署了动态PCC并且切换指示不存在，PGW执行IP-CAN会话建立过程，从而获得UE默认PCC规则。 
如果部署了动态PCC并且切换指示存在，PGW执行PCEF发起的IP-CAN会话修改过程。 
如果未部署动态PCC，PGW使用本地配置策略。 


PGW在EPS承载上下文列表中创建一个新的条目，并生成一个计费标识。PGW返回Create Session Response消息给SGW，其中包括PDN GW Address for the user plane, PDN GW TEID of the
user plane, PDN GW TEID of the control plane, PDN Type, PDN Address,
EPS Bearer Identity, EPS Bearer QoS, Protocol Configuration Options,
Charging Id, APN Restriction, Cause, MS Info Change Reporting Action
(Start)等信息。


如果SGW接收到MS Info Change Reporting Action(start)指示，SGW存储并报告UE位置改变情况。SGW回Create Session Response消息给New MME，其中包括PDN Type, PDN Address,
Serving GW address for User Plane, Serving GW TEID for User Plane,
Serving GW TEID for control plane, EPS Bearer Identity, EPS Bearer
QoSProtocol Configuration Options, APN Restriction, Cause, MS Info
Change Reporting Action (Start), APN-AMBR等信息。


MME根据属于缺省APN的签约APN-AMBR和签约UE-AMBR确定UE-AMBR。New MME发送S1-MME控制消息Initial Context Setup Request给eNodeB，请求建立无线资源。Attach Accept消息被包含该消息中下发给eNodeB。如果New MME分配了新的GUTI，也通过此消息下发。


eNodeB发送包含EPS无线承载标识的RRC Connection Reconfiguration消息给UE，同时Attach
Accept消息也通过本消息带给UE。当UE接收到附着接受消息时，UE必须将TIN设置为GUTI。


UE发送RRC Connection Reconfiguration Complete消息给eNodeB。


eNodeB发送Initial Context Setup Response消息给New MME。该消息包含
eNodeB的TEID 以及eNodeB的地址，该地址用于S1-U参考点的下行业务。


UE发送Direct Transfer消息给eNodeB，该消息中包含Attach Complete消息。


eNodeB通过上行NAS传输消息转发Attach Complete消息给New MME。


New MME接收到第20步的Initial Context Setup Response消息和第22步的Attach
Complete消息，New MME发送Modify Bearer Request消息给SGW。


如果第23步包含切换指示，SGW发送Modify Bearer Request消息给PGW，使其将报文从非3GPP接入切到3GPP接入，通过所建立的缺省承载或者专用EPS承载立即开始给SGW传送数据包。


PGW向SGW发送Modify Bearer Response消息。




SGW向New MME发送Modify Bearer Response消息。SGW可以发送缓存的下行报文。


（可选）New MME接收到SGW发送的Modify Bearer Response消息。如果请求类型没有指示切换，承载建立，签约数据指示用户被容许切换到非3GPP接入，并且如果MME选择的PGW不同于HSS签约PDN上下文的PGW标识，MME应发送Notify Request消息给HSS，消息中包含APN和PGW 标识。


（可选）HSS保存APN和PGW标识对，发送Notify Response消息给MME。




### UE发起的Detach 
### UE发起的Detach 


业务模型 :UE主动发起的分离流程，用于UE通知网络该UE不再使用EPC网络，网络侧可以释放该UE相关资源。 


信令流程 :UE发起的Detach信令流程如[图1](02%20UE%E5%8F%91%E8%B5%B7%E7%9A%84Detach.html#concept1__UE%E5%8F%91%E8%B5%B7%E7%9A%84Detach%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-28FA61C9)所示。
图1  UE发起的Detach信令流程

[]images/UE%E5%8F%91%E8%B5%B7%E7%9A%84Detach.png)


流程说明 :

UE发送Detach Request消息给MME，消息中会携带GUTI和Switch Off参数。eNodeB会将UE所在的TAI+ECGI标识添加在Detach Request消息中一起转发给MME。


MME按每PDN连接发送Delete Session Request消息(携带LBI)给SGW。如果PGW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。 


SGW释放相关承载资源，按每PDN连接发送Delete Session Request（LBI）消息给PGW。如果PGW请求了UE位置信息，则SGW在这个消息中包含用户位置信息。


PGW释放相关承载资源，并给SGW回Delete Session Response消息。


（可选）如果网络中部署了PCRF，PGW执行PCRF发起的IP-CAN会话结束流程去指示PCRF释放相关资源。 


SGW向MME发送Delete Session Response消息。


（可选）如果Switch Off分离不是关机引起的，MME发送Detach Accept给UE。


（可选）MME发送Signalling Connection Release消息给eNodeB释放UE的S1-MME信令连接。




### MME发起的Detach 
### MME发起的Detach 


业务模型 :MME发起的分离流程，用于网络侧通知UE，网络侧不再为该UE提供服务，网络侧释放该UE相关资源。 


信令流程 :MME发起的Detach信令流程如[图1](03%20MME%E5%8F%91%E8%B5%B7%E7%9A%84Detach.html#concept1__MME%E5%8F%91%E8%B5%B7%E7%9A%84Detach%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-28FAD524)所示。
图1  MME发起的Detach信令流程

[]images/MME%E5%8F%91%E8%B5%B7%E7%9A%84Detach.png)


#### 流程描述 


（可选）MME可以发起显示或隐式分离。 
如果UE长时间没有和MME通讯，MME可以隐式分离UE。MME在隐式分离时，不会发送Detach Request消息给UE，消息中携带Detach Type。
MME主动发起显示分离时，根据ECM状态不同，分为如下两种情况： 

 
如果UE处于ECM-CONNNECTED态，MME通过发送Detach Request消息给UE进行显示分离。 

 
如果UE处于ECM-IDLE态，MME需要首先寻呼到UE，然后再发送Detach Request消息。 

 


MME按每PDN连接发送Delete Session Request消息(LBI)给SGW。如果PGW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。


SGW释放相关承载信息，按每PDN连接发送Delete Session Request(LBI)消息给PGW。如果PGW请求了UE位置信息，则SGW在这个消息中包含用户位置信息。


PGW释放相关承载资源，并给SGW回Delete Session Response消息。


（可选）如果网络中部署了PCRF，PGW执行PCRF发起的IP-CAN会话结束流程去指示PCRF释放相关资源。 


SGW向MME发送Delete Session Response消息。


（可选）UE在第1步之后的任何时间发送Detach Accept消息。eNodeB会将UE所在小区的TAI+ECGI
标识与Detach Accept消息一起转发给MME。


（可选）MME接收到Detach Accept消息和Delete Session Response消息，MME发送Signalling Connection Release给eNodeB释放UE的S1-MME信令连接。如果Detach
Type指示UE重新Attach，UE可以在RRC连接释放完成后重新附着。




### HSS发起的Detach 
### HSS发起的Detach 


业务模型 :HSS发起的分离流程，用于网络侧通知UE，网络侧不再为该UE提供服务，网络侧释放该UE相关资源。 


信令流程 :HSS发起的Detach信令流程如[图1](04%20HSS%E5%8F%91%E8%B5%B7%E7%9A%84Detach.html#concept1__HSS%E5%8F%91%E8%B5%B7%E7%9A%84Detach%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-28FB86A2)所示。
图1  HSS发起的Detach信令流程

[]images/HSS%E5%8F%91%E8%B5%B7%E7%9A%84Detach%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B.png)


流程说明 :

HSS请求立即删除签约MM上下文和EPS承载，HSS会发送Cancel Location消息(IMSI,
Cancellation Type)给MME，其中Cancellation Type设置为Subscription Withdrawn。


MME发送Detach Request消息通知处于ECM-CONNECTED的UE分离。
如果UE处于ECM-IDLE态，MME首先寻呼到UE，然后进行分离过程。 


MME按每PDN连接发送Delete Session Request消息(LBI)给SGW。如果PGW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。


SGW释放相关承载信息，按每PDN连接发送Delete Session Request(LBI)消息给PGW。如果PGW请求了UE位置信息，则SGW在这个消息中包含用户位置信息。


PDN GW给SGW回Delete Session Response消息。


（可选）如果PCRF部署了，PGW执行PCRF发起的IP-CAN会话结束流程去指示PCRF释放EPS承载。 


SGW向MME发送Delete Session Response消息。


UE在第2步之后的任何时间发送Detach Accept消息。eNodeB携带UE所在小区的TAI+ECGI标识与Detach
Accept消息一起转发给MME。


MME确认MM上下文和EPS承载删除，发送Cancel Location Ack消息给HSS。


MME接收到Detach Accept消息和Delete Session Response消息，MME发送Signalling
Connection Release命令给eNodeB释放UE的S1-MME信令连接。




### MME和SGW均未变更的E-UTRAN内部TAU流程 
### MME和SGW均未变更的E-UTRAN内部TAU流程 


业务模型 :MME网元跟踪区更新流程是用户从一个小区移动到另一个小区或从一种接入技术变成另一种接入技术时，用户重新建立连接，重新接入EPS网络的过程。 
该业务使用于用户在同一个MME内移动，发起TAU过程，同时SGW未发生变化的场景。 


信令流程 :MME和SGW均未变更的E-UTRAN内部TAU流程如[图1](05%20MME%E5%92%8CSGW%E5%9D%87%E6%9C%AA%E5%8F%98%E6%9B%B4%E7%9A%84E-UTRAN%E5%86%85%E9%83%A8TAU%E6%B5%81%E7%A8%8B.html#concept1__TAUIntra-MMEWithoutS-GWChange%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-28FEBFB1)所示、
图1  MME和SGW均未变更的E-UTRAN内部TAU流程

[]images/TAU,%20intra-MME,%20without%20S-GW%20change.png)


流程说明 :

UE检测到触发TAU的条件满足，发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，消息中携带RRC参数（Selected
Network和old GUMMEI）。如果这个TAU过程是由于负载重均衡而触发的，在RRC参数中不包含old GUMMEI标识。 


eNodeB通过old GUMMEI和Selected Network得到MME，并向MME转发Tracking Area
Update Request消息。 


（可选）UE、MME和HSS可以完成鉴权和安全功能。如果Tracking Area Update Request消息的完整性检查失败，则鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 


MME向UE发送Tracking Area Update Accept消息，如果分配了新的GUTI，则会在此消息中携带。 


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking Area
Update Complete消息确认接收到了Tracking Area Update Accept消息。 




### MME不变、SGW改变的E-UTRAN内部TAU流程 
### MME不变、SGW改变的E-UTRAN内部TAU流程 


业务模型 :MME网元跟踪区更新流程是用户从一个小区移动到另一个小区或从一种接入技术变成另一种接入技术时，用户重新建立连接，重新接入EPS网络的过程。 
该业务使用于用户在同一个MME内移动，发起TAU过程，同时SGW发生变化的场景。 


信令流程 :MME不变、SGW改变的E-UTRAN内部TAU流程如[图1](06%20MME%E4%B8%8D%E5%8F%98%E3%80%81SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%86%85%E9%83%A8TAU%E6%B5%81%E7%A8%8B.html#concept1__TAUIntra-MMEWithS-GWChange%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-28FF4546)所示。
图1  MME不变、SGW改变的E-UTRAN内部TAU流程

[]images/TAU,%20intra-MME,%20with%20S-GW%20change.png)


流程说明 :

UE检测到触发TAU的条件满足，发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，消息中携带RRC参数（Selected
Network和old GUMMEI）。如果这个TAU过程是由于负载重均衡而触发的，在RRC参数中不包含old GUMMEI标识。 


eNodeB通过old GUMMEI和Selected Network得到MME，并向MME转发Tracking Area
Update Request消息。 


（可选）UE、MME和HSS可以完成鉴权和安全功能。如果Tracking Area Update Request消息的完整性检查失败，则鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 


MME验证从UE接收到的EPS承载状态，并释放非活动态EPS承载关联的网络资源。如果没有承载上下文，MME将拒绝TAU请求。 


MME根据用户目前所在的TA选择new SGW，并按照每个PDN连接向该SGW发送Create Session Request消息。 


New SGW向PGW发送Modify Bearer Request消息，其中包含Serving GW Address
and TEID、RAT type、Serving Network等信息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW将发起IP-CAN修改流程，把RAT type等变化的信息发送给PCRF。 


PGW更新相关的承载上下文，并向new SGW返回Modify Bearer Response消息。 


new SGW更新承载上下文，并向MME返回Create S ession Response消息。 


MME向old SGW发送Delete Session Request消息，以指示其释放EPS承载资源。 


old SGW释放承载资源并向MME返回Delete Session Response消息，old SGW丢弃为UE所缓存的所有数据包。 


MME向UE发送Tracking Area Update Accept消息，如果分配了新的GUTI，则会在此消息中携带。 


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking Area
Update Complete消息确认接收到了Tracking Area Update Accept消息。 




### MME改变、SGW不变的E-UTRAN内部TAU流程 
### MME改变、SGW不变的E-UTRAN内部TAU流程 


业务模型 :MME网元跟踪区更新流程是用户从一个TA移动到另一个TA或从一种接入技术变成另一种接入技术时，用户重新建立连接，重新接入EPS网络的过程。 
该业务使用于用户从一个MME移动到另外一个MME，发起TAU过程，但SGW未发生变化的场景。 


信令流程 :MME改变、SGW不变的E-UTRAN内部TAU流程如[图1](07%20MME%E6%94%B9%E5%8F%98%E3%80%81SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%86%85%E9%83%A8TAU%E6%B5%81%E7%A8%8B.html#concept1__TAUInter-MMEWithoutS-GWChange%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-2901E788)所示。
图1  MME改变、SGW不变的E-UTRAN内部TAU流程


[]images/TAU,%20inter-MME,%20without%20S-GW%20change.png)



流程说明 :

UE检测到触发TAU的条件满足，发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，消息中携带RRC参数（Selected
Network和old GUMMEI）。 


eNodeB从RRC参数中的老的GUMMEI和指示的已选择网络参数得到MME，并向MME转发Tracking Area
Update Request消息。 


new MME通过GUTI获得old MME地址，并向old MME发送Context Request消息重新获取用户信息，消息中包括old
GUTI, MME Address, UE Validated, complete TAU Request message, P‑TMSI
Signature。 


old MME向new MME返回Context Response消息，消息包含：IMSI、IMEI、鉴权信息、EPS承载等参数。 


（可选）如果第2步完整性检查失败，则执行鉴权过程。 


new MME向old MME发送Context Acknowledge消息，old MME将SGW、P-GW和HSS信息标记为不可用，从而保证当UE在本次TAU流程还未完成又发起回到old
MME的TAU流程时，old MME可以更新SGW、P-GW和HSS信息。 


如果old MME在Context Response中没有返回承载上下文，new MME拒绝TAU请求。new MME根据从old
MME得到的承载上下文信息，对每个PDN连接的SGW发送Modify Bearer Request消息，通知其更新承载信息，消息中包括new
MME address 和 TEID, RAT type。 


（可选）如果Modify bearer request消息携带的RAT type发生了变化，或者消息中携带有User
Location Information或UE Time Zone IE，SGW向PGW发送Modify Bearer Request消息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW将发起IP-CAN修改流程，把RAT type等变化的信息发送给PCRF。 


（可选）PGW更新相关的承载上下文，并向SGW返回Modify Bearer Response消息。 


SGW更新承载上下文，并向new MME返回Create Session Response消息。消息中包括Serving
GW address and TEID for uplink traffic, MS Info Change Reporting Action。 


new MME向HSS发送Update Location Request消息告知其MME已变更，消息包含：MME Id、IMSI、ULR-Flags、MME
Capabilities。 


HSS向old MME发送Cancel Location消息，消息包含：IMSI、Cancellation type，Cancellation
type设置为Update Procedure。 


如果第4步中的定时器超时，old MME删除MM和承载上下文信息，否则需要等待定时器超时后再删除上下文。目的是为了防止用户在本次TAU过程未完成时又发起了新的TAU过程时，old
MME仍保留着MM上下文。上下文删除后，old MME向HSS响应Cancel Location Ack消息，消息包含：IMSI。 


HSS向新的MME发送Update Location Ack，消息中包括IMSI, Subscription Data。 


new MME向UE发送Tracking Area Update Accept消息，消息中包括GUTI, TAI-list,
EPS bearer status等。 


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking Area
Update Complete消息确认接收到了Tracking Area Update Accept消息。 




### MME和SGW均改变的E-UTRAN内部TAU流程 
### MME和SGW均改变的E-UTRAN内部TAU流程 


业务模型 :MME网元跟踪区更新流程是用户从一个TA移动到另一个TA或从一种接入技术变成另一种接入技术时，用户重新建立连接，重新接入EPS网络的过程。 
该业务使用于用户从一个MME移动到另外一个MME，发起TAU过程，同时SGW也发生变化的场景。 


信令流程 :MME和SGW均改变的E-UTRAN内部TAU流程如[图1](08%20MME%E5%92%8CSGW%E5%9D%87%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%86%85%E9%83%A8TAU%E6%B5%81%E7%A8%8B.html#concept1__TAUInter-MMEWithS-GWChange%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-2902824F)所示。
图1  MME和SGW均改变的E-UTRAN内部TAU流程


[]images/TAU,%20inter-MME,%20with%20S-GW%20change.png)



流程说明 :

UE检测到触发TAU的条件满足，发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，消息中携带RRC参数（Selected
Network和old GUMMEI）。 


eNodeB从RRC参数中的old GUMMEI和指示的已选择网络参数得到MME，并向MME转发Tracking Area
Update Request消息。 


new MME通过GUTI获得old MME地址，并向old MME发送Context Request消息重新获取用户信息，消息中包括old
GUTI, MME Address, UE Validated, complete TAU Request message, P‑TMSI
Signature。 


old MME向new MME返回Context Response消息，消息包含：IMSI、IMEI、鉴权信息、EPS承载等参数。 


（可选）如果第2步完整性检查失败，则执行鉴权过程。 


new MME向old MME发送Context Acknowledge消息，old MME将SGW、P-GW和HSS信息标记为不可用，从而保证当UE在本次TAU流程还未完成又发起回到old
MME的TAU流程时，old MME可以更新SGW、P-GW和HSS信息。 


如果old MME在Context Response中没有返回承载上下文，new MME拒绝TAU请求。new MME根据从old
MME得到的承载上下文信息，对每个PDN连接重新选择SGW，通过Create Session Request消息通知SGW建立连接，消息中包括IMSI,
bearer contexts, MME Address and TEID for the control plane, RAT Type。 


new SGW向PGW发送Modify Bearer Request消息，其中包含Serving GW Address
and TEID、RAT type、Serving Network等信息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发起IP-CAN修改流程，把RAT
type等变化的信息发送给PCRF。 


PGW更新相关的承载上下文，并向new SGW返回Modify Bearer Response消息。 


new SGW更新承载上下文，并向new MME返回Create Session Response消息。消息中包括Serving
GW address and TEID for uplink traffic, MS Info Change Reporting Action。 


new MME向HSS发送Update Location Request消息告知其MME已变更，消息包含：MME Id、IMSI、ULR-Flags、MME
Capabilities。 


HSS向old MME发送Cancel Location消息，消息包含：IMSI、Cancellation type，Cancellation
type设置为Update Procedure。 


如果第4步中的定时器超时，old MME删除MM和承载上下文信息，否则需要等待定时器超时后再删除上下文。目的是为了防止用户在本次TAU过程未完成时又发起了新的TAU过程时，old
MME仍保留着MM上下文。上下文删除后，old MME向HSS响应Cancel Location Ack消息，消息包含：IMSI。 


HSS向new MME发送Update Location Ack，消息中包括IMSI, Subscription Data。 


当第4步的定时器超时时，old MME释放本地承载资源，并向old SGW发送Delete Session Request消息告知其释放承载资源。消息中包括Cause。 


old SGW向old MME返回Delete Session Response消息并丢弃为UE所缓存的所有数据包。 


new MME向UE发送Tracking Area Update Accept消息，消息中包括GUTI, TAI-list,
EPS bearer status等。 


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking Area
Update Complete消息确认接收到了Tracking Area Update Accept消息。 




### UTRAN到E-UTRAN的TAU流程 
### UTRAN到E-UTRAN的TAU流程 


业务模型 :从UTRAN向E-UTRAN的TAU是指UE通过小区重选或重定向等UTRAN接入改为E-UTRAN接入，是为了实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户跨RAT移动的业务连续性。SGSN和MME间使用Gn接口。 
TAU（Tracking area update）的触发条件：
 
UE发现当前的TAI不在UE注册网络的TA（Tracking Area） List中 

 
周期性TAU 

 
UE的接入类型即RAT type(GSM、UTRAN、E-UTRAN)发生改变 

 
网络侧负载均衡触发TAU 

 
切换过程中触发的TAU 

 


信令流程 :UTRAN到E-UTRAN的TAU流程如[图1](09%20UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.html#concept1__UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B-DE441FC2)所示。
图1  UTRAN到E-UTRAN的TAU流程


[]images/UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从UTRAN覆盖区域移动到EUTRAN强信号覆盖区域，UE选择4G网络。UE检测到触发TAU的条件满足，UE发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，同时携带RRC参数指示所选择的网络以及old
GUMMEI，其中old GUMMEI的值从old GUTI中取得。由于UE之前在3G网络，所以UE将保存的SGSN分配old P-TMSI和old
RAI映射为old GUTI。


eNodeB从RRC参数中的old GUMMEI和指示的已选择网络参数得到MME。如果不能得到MME，eNodeB就选择一个MME。然后eNodeB转发Tracking Area Update Request消息到new MME，并携带一个TAI+ECGI参数和所选择网络。


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




### GERAN到E-UTRAN的TAU流程 
### GERAN到E-UTRAN的TAU流程 


业务模型 :从GERAN向E-UTRAN的TAU是指UE通过小区重选或重定向等GERAN接入改为E-UTRAN接入，是为了实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户跨RAT移动的业务连续性。SGSN和MME间使用Gn接口。 


信令流程 :GERAN到E-UTRAN的TAU流程如[图1](10%20GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.html#concept1__GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B-29A0796C)所示。
图1  GERAN到E-UTRAN的TAU流程


[]images/GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从GERAN覆盖区域移动到EUTRAN强信号覆盖区域，UE选择4G网络。UE检测到触发TAU的条件满足，UE发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，同时携带RRC参数指示所选择的网络以及old
GUMMEI，其中old GUMMEI的值从old GUTI中取得。由于UE之前在2G网络，所以UE将保存的SGSN分配old P-TMSI和old
RAI映射为old GUTI。


eNodeB从RRC参数中的old GUMMEI和指示的已选择网络参数得到MME。如果不能得到MME，eNodeB就选择一个MME。然后eNodeB转发Tracking Area Update Request消息到new MME，并携带一个TAI+ECGI参数和所选择网络。


new MME通过old RAI和old P-TMSI（或者 TLLI）获取Gn/Gp SGSN的信息，并发送SGSN
Context Request消息给Gn/Gp SGSN以请求用户的移动性管理和会话管理相关信息，消息包含：old RAI、P-TMSI、old
P-TMSI Signature、new MME Address。 


Gn/Gp SGSN给new MME回SGSN Context Response消息，消息包含：MM Context、PDP
Contexts。对于old SGSN来说，并不需要识别新局是MME。 


UE、MME和HSS可以完成鉴权和安全功能。如果TAU请求消息的完整性检查失败，鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 


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


（可选）如果UE曾经在LTE注册过，且MME发生改变，则HSS发送Cancel Location消息给 old MME，消息包含：IMSI、Cancellation
type，Cancellation type设置为Update Procedure。 


可选：old MME删除移动性管理上下文。old MME发送Cancel Location Ack消息给HSS。 


HSS发送Cancel Location消息给Gn/Gp SGSN， Gn/Gp SGSN删除移动性管理上下文，消息包含：IMSI、Cancellation
type。Gn/Gp SGSN删除上下文。


Gn/Gp SGSN向HSS响应Cancel Location Ack消息，消息包含：IMSI。


HSS给new MME回Update Location Ack消息。如果更新位置请求被HSS拒绝，则MME拒绝来自UE的TAU请求并说明原因。如果所有检查通过，MME构造UE的移动性管理上下文。 


MME发送Tracking Area Update Accept消息给UE。如果分配了新的GUTI，则会在TAU接受消息中携带。如果在TAU请求消息中携带了“激活标识”，用户面建立过程和TAU接受消息发送一起执行。 


如果在TAU接受消息中携带了GUTI，UE发送Tracking Area Update Complete确认接收到了TAU接受消息。如果在TAU请求消息没有携带“激活标识”，并且也不是ECM-CONNECTED态下发起的TAU过程，MME释放信令连接。 


如果映射的QoS参数与UE当前签约的QoS参数不一致，则MME发起签约QoS修改流程。 




### E-UTRAN到UTRAN的RAU流程 
### E-UTRAN到UTRAN的RAU流程 


业务模型 :从E-UTRAN向UTRAN的RAU是指UE通过小区重选或重定向等E-UTRAN接入改为UTRAN接入，是为了实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 


信令流程 :E-UTRAN到UTRAN的RAU流程如[图1](11%20E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.html#concept1__E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B-29A1E068)所示。
图1  E-UTRAN到UTRAN的RAU流程


[]images/E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

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




### E-UTRAN到GERAN的RAU流程 
### E-UTRAN到GERAN的RAU流程 


业务模型 :从E-UTRAN向GERAN的RAU是指UE通过小区重选或重定向等E-UTRAN接入改为GERAN接入，是为了实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 


信令流程 :E-UTRAN到GERAN的RAU流程如[图1](12%20E-UTRAN%E5%88%B0GERAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.html#concept1__E-UTRAN%E5%88%B0GERAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B-299A75C2)所示。
图1  E-UTRAN到GERAN的RAU流程


[]images/E-UTRAN%E5%88%B0GERAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从EUTRAN覆盖区域移动到GERAN强信号覆盖区域，UE选择2G网络。 


UE 向new SGSN发送Routing Area Update Request消息，消息中携带的old
P‑TMSI、old RAI和old P‑TMSI由GUTI映射得到。


new SGSN发送SGSN Context Request消息给old MME以请求用户的移动性管理和会话管理相关信息。由GUTI映射的old
RAI和old P-TMSI可以唯一标识old MME。 


old MME给new SGSN回SGSN Context Response消息。对于new SGSN来说，并不需要识别老局是否是MME。由MME会将EPS承载按一对一映射到PDP上下文，同时也会完成QoS参数的映射。 


（可选）如果SGSN Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。 


new SGSN向old MME发送SGSN Context Acknowledge消息。old MME将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还在进行中，UE向old
MME发起TAU流程时，old MME对GW和HSS的信息进行更新。 


new SGSN发送Update PDP Context Request消息到每个PDP上下文关联的PGW（内嵌GGSN）。


PGW更新PDP上下文中的对端用户面地址信息及QoS等，并向new SGSN返回Update PDP Context
Response消息。


New SGSN发送Update Location Request消息到HSS，指示为普通更新。


（可选）如果HLR有其他SGSN的注册信息，则发送Cancel Location消息到old SGSN，
Cancellation Type设置为Update Procedure。


（可选）old SGSN删除MM和PDP上下文，返回Cancel Location Ack消息给HLR。


HLR发送Insert Subscriber Data消息到new SGSN，带用户签约信息等。


new SGSN返回Insert Subscriber Data Ack消息到HLR。


HLR发送Update Location Ack消息到new SGSN。


New SGSN发送Routing Area Update Accept消息到UE，携带新分配的P-TMSI。


UE发现P-TMSI被重新分配，发送Routing Area Update Complete消息到new
SGSN。


old MME根据SGSN Context Request知道是UE移动到GERAN，释放eNodeB侧和SGW侧资源，并向SGW发送Delete
Session Request消息告知其释放EPS承载资源，指示SGW不要向PGW发起承载删除流程。 


SGW向old MME响应Delete Session Response消息。 


（可选）如果old MME与UE之间有S1-MME连接，当收到new SGSN发送的SGSN Context Acknowledge消息，old MME执行S1-AP Release。




### SGW不变的UTRAN到E-UTRAN的TAU流程 
### SGW不变的UTRAN到E-UTRAN的TAU流程 


业务模型 :从UTRAN向E-UTRAN的TAU是指UE通过小区重选或重定向等由UTRAN接入改为E-UTRAN接入，从而实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从UTRAN向E-UTRAN的TAU流程中SGW可能发生改变或不改变。本业务模型为SGW不改变的情况。 


信令流程 :SGW不变的UTRAN到E-UTRAN的TAU流程如[图1](13%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E4%B8%8D%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B-290327BD)所示。
图1  SGW不变的UTRAN到E-UTRAN的TAU流程


[]images/SGW%E4%B8%8D%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

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




### SGW改变的UTRAN到E-UTRAN的TAU流程 
### SGW改变的UTRAN到E-UTRAN的TAU流程 


业务模型 :从UTRAN向E-UTRAN的TAU是指UE通过小区重选或重定向等由UTRAN接入改为E-UTRAN接入，从而实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从UTRAN向E-UTRAN的TAU流程中SGW可能发生改变或不改变。本业务模型为SGW改变的情况。 


信令流程 :SGW改变的UTRAN到E-UTRAN的TAU流程如[图1](14%20SGW%E6%94%B9%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E6%94%B9%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B-2903CACE)所示。
图1  SGW改变的UTRAN到E-UTRAN的TAU流程


[]images/SGW%E6%94%B9%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE检测到触发TAU的条件满足，UE发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，同时携带RRC参数（所选择网络、旧GUMMEI）。如果这个TAU过程是由于负载重均衡而触发的，在RRC参数中不包含旧GUMMEI标识。


eNodeB从RRC参数中的老的GUMMEI和指示的已选择网络参数（Selected Network）得到MME。如果不能得到MME，eNodeB就选择一个MME，并向新的MME转发Tracking Area Update Request消息，并携带一个TAI+ECGI参数和所选择网络。


新的MME根据老的GUTI找到老的S4 SGSN地址，发送一个Context Request消息给老的S4
SGSN以请求用户的移动性管理和会话管理相关信息。如果MME指示它已经对UE进行了鉴权或者老的S4 SGSN对UE进行鉴权，那么老的S4
SGSN会启动一个定时器。


老的S4 SGSN给新的MME回Context Response消息。


（可选）UE、MME和HSS可以完成鉴权和安全功能。如果TAU请求消息的完整性检查失败，鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 


新的MME根据TAI决定SGW是否需要改变。新的MME给老的S4 SGSN发送Context Acknowledge消息，携带SGW是否改变的信息。老的S4 SGSN将UE上下文中GW相关信息标记为无效。这样可以确保如果UE在完成正在进行的TAU过程前回到老的S4
SGSN发起一个新的RAU过程时，老的S4 SGSN能够更新GW和HSS。


如果安全过程不能正确认证UE，必须拒绝TAU请求，并且新MME向老S4 SGSN发送拒绝指示。老S4 SGSN继续服务UE。 
新MME将从老S4 SGSN所接收到的承载上下文与从UE所接收到的EPS承载状态进行验证。MME将释放UE中非激活EPS承载的任何网络资源。如果根本就没有承载上下文，则MME拒绝TAU请求消息。 
MME根据用户目前所在的TA选择一个新的SGW，按每PDN连接给其发送Create Session Request消息。


新的SGW向PGW发送Modify Bearer Request消息，其中包含SGW Address and TEID、RAT
type、Serving Network等信息。 


PGW更新相关的承载上下文，并向新的SGW返回Modify Bearer Response消息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发送CCR-U消息，发起IP-CAN修改流程，把RAT
type等变化的信息发送给PCRF。 


新的SGW更新承载上下文，并向MME返回Create Session Response消息。 


新的MME给HSS发送Update Location Request消息，获取用户的签约数据。


（可选）如果老的S4 SGSN接收到Context Acknowledge消息，并且用户的Iu连接也存在，老的S4
SGSN在第4步设置的定时器超时时，发送Iu Release Command消息给RNC。


（可选）RNC给老的GnGp SGSN回Iu Release Complete消息。


HSS给新的MME回Update Location Ack消息。如果更新位置请求被HSS拒绝，则MME拒绝来自UE的TAU请求并说明原因。如果所有检查通过，MME构造UE的移动性管理上下文。


（可选）当第4步设置的定时器超时，如果老的S4 SGSN收到了Context Acknowledge消息，老的S4 SGSN释放承载资源。由于SGW发生改变，老的S4
SGSN给老的SGW发送Delete Session Request消息以指示删除EPS承载资源，原因值指示老的SGW不要通知PGW删除承载资源。 


（可选）老的SGW释放承载资源，给老的S4 SGSN回Delete Session Response消息，老的SGW丢弃为UE所缓存的任何分组包。 


MME发送Tracking Area Update Accept消息给UE。如果分配了新的GUTI，则会在Tracking
Area Update Accept消息中携带。如果在Tracking Area Update Request消息中携带了“激活标识”，用户面建立过程和Tracking
Area Update Accept消息发送一起执行。


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking
Area Update Complete消息，确认接收到了TAU接受消息。如果在Tracking Area Update Request消息中没有携带“激活标识”，并且也不是ECM-CONNECTED态下发起的TAU过程，MME释放信令连接。




### SGW不变的GERAN到E-UTRAN的TAU流程 
### SGW不变的GERAN到E-UTRAN的TAU流程 


业务模型 :从GERAN向E-UTRAN的TAU是指UE通过小区重选或重定向等由GERAN接入改为E-UTRAN接入，从而实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从GERAN向E-UTRAN的TAU流程中SGW可能发生改变或不改变。本业务模型为SGW不改变情况。 


信令流程 :SGW不变的GERAN到E-UTRAN的TAU流程如[图1](15%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E4%B8%8D%E5%8F%98%E7%9A%84GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B-2904A11D)所示。
图1  SGW不变的GERAN到E-UTRAN的TAU流程


[]images/SGW%E4%B8%8D%E5%8F%98%E7%9A%84GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE检测到触发TAU的条件满足，UE发起TAU过程。 


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


HSS给新的MME回Update Location Ack消息。如果更新位置请求被HSS拒绝，则MME拒绝来自UE的TAU请求并说明原因。如果所有检查通过，MME构造UE的移动性管理上下文。


MME发送Tracking Area Update Accept消息给UE。如果分配了新的GUTI，则会在Tracking
Area Update Accept消息中携带。如果在Tracking Area Update Request消息中携带了“激活标识”，用户面建立过程和Tracking
Area Update Accept消息发送一起执行。


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking
Area Update Complete消息确认接收到了TAU接受消息。如果在Tracking Area Update Request消息中没有携带“激活标识”，并且也不是ECM-CONNECTED态下发起的TAU过程，MME释放信令连接。




### SGW改变的GERAN到E-UTRAN的TAU流程 
### SGW改变的GERAN到E-UTRAN的TAU流程 


业务模型 :从GERAN 向E-UTRAN的TAU是指UE通过小区重选或重定向等由GERAN
接入改为E-UTRAN接入，从而实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从GERAN 向E-UTRAN的TAU流程中SGW可能发生改变或不改变。本业务模型为SGW改变情况。 


信令流程 :SGW改变的GERAN到E-UTRAN的TAU流程如[图1](16%20SGW%E6%94%B9%E5%8F%98%E7%9A%84GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E6%94%B9%E5%8F%98%E7%9A%84GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B-2905A215)所示。
图1  SGW改变的GERAN到E-UTRAN的TAU流程


[]images/SGW%E6%94%B9%E5%8F%98%E7%9A%84GERAN%E5%88%B0E-UTRAN%E7%9A%84TAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE检测到触发TAU的条件满足，UE发起TAU过程。 


UE向eNodeB发送Tracking Area Update Request消息发起TAU过程，同时携带RRC参数（所选择网络、旧GUMMEI）。如果这个TAU过程是由于负载重均衡而触发的，在RRC参数中不包含旧GUMMEI标识。


eNodeB从RRC参数中的老的GUMMEI和指示的已选择网络参数（Selected Network）得到MME。如果不能得到MME，eNodeB就选择一个MME，并向新的MME转发Tracking Area Update Request消息，并携带一个TAI+ECGI参数和所选择网络。


新的MME根据老的GUTI找到老的S4 SGSN地址，发送一个Context Request消息给老的S4
SGSN以请求用户的移动性管理和会话管理相关信息。如果MME指示它已经对UE进行了鉴权或者老的S4 SGSN对UE进行鉴权，那么老的S4
SGSN会启动一个定时器。


老的S4 SGSN给新的MME回Context Response消息。


（可选）UE、MME和HSS可以完成鉴权和安全功能。如果TAU请求消息的完整性检查失败，鉴权过程是必须的。如果执行了GUTI分配并且网络支持加密，则NAS消息将被加密。 


新的MME根据TAI决定SGW是否需要改变。新的MME给老的S4 SGSN发送Context Acknowledge消息，携带SGW是否改变的信息。老的S4 SGSN将UE上下文中GW相关信息标记为无效。这样可以确保如果UE在完成正在进行的TAU过程前回到老的S4
SGSN发起一个新的RAU过程时，老的S4 SGSN能够更新GW和HSS。


如果安全过程不能正确认证UE，必须拒绝TAU请求，并且新MME向老S4 SGSN发送拒绝指示。老S4 SGSN继续服务UE。 
新MME将从老S4 SGSN所接收到的承载上下文与从UE所接收到的EPS承载状态进行验证。MME将释放UE中非激活EPS承载的任何网络资源。如果根本就没有承载上下文，则MME拒绝TAU请求消息。 
MME根据用户目前所在的TA选择一个新的SGW，按每PDN连接给其发送Create Session Request消息。


新的SGW向PGW发送Modify Bearer Request消息，其中包含SGW Address and TEID、RAT
type、Serving Network等信息。 


PGW更新相关的承载上下文，并向新的SGW返回Modify Bearer Response消息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发送CCR-U消息，发起IP-CAN修改流程，把RAT
type等变化的信息发送给PCRF。 


新的SGW更新承载上下文，并向新的MME返回Create Session Response消息。SGW已经可以把上行数据报文发送给PGW了。 


新的MME给HSS发送Update Location Request消息，获取用户的签约数据。


HSS给新的MME回Update Location Ack消息。如果更新位置请求被HSS拒绝，则MME拒绝来自UE的TAU请求并说明原因。如果所有检查通过，MME构造UE的移动性管理上下文。


（可选）当第4步设置的定时器超时，如果老的S4 SGSN收到了Context Acknowledge消息，老的S4 SGSN释放承载资源。由于SGW发生改变，老的S4
SGSN给老的SGW发送Delete Session Request消息以指示删除EPS承载资源，原因值指示老的SGW不要通知PGW删除承载资源。 


（可选）老的SGW释放承载资源，给老的S4 SGSN回Delete Session Response消息，老的SGW丢弃为UE所缓存的任何分组包。 


MME发送Tracking Area Update Accept消息给UE。如果分配了新的GUTI，则会在Tracking
Area Update Accept消息中携带。如果在Tracking Area Update Request消息中携带了“激活标识”，用户面建立过程和Tracking
Area Update Accept消息发送一起执行。


（可选）如果在Tracking Area Update Accept消息中携带了GUTI，UE发送Tracking
Area Update Complete消息，确认接收到了TAU接受消息。如果在Tracking Area Update Request消息中没有携带“激活标识”，并且也不是ECM-CONNECTED态下发起的TAU过程，MME释放信令连接。




### SGW不变的E-UTRAN到UTRAN的RAU流程 
### SGW不变的E-UTRAN到UTRAN的RAU流程 


业务模型 :从E-UTRAN向UTRAN的RAU是指UE通过小区重选或重定向等，E-UTRAN接入改为UTRAN接入，是为了实现EPS网络和UMTS网络互通，满足2/3G和LTE同时签约的用户跨RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从E-UTRAN向UTRAN的RAU流程中SGW可能发生改变或不改变。本业务模型为SGW不改变情况。 


信令流程 :SGW不变的E-UTRAN到UTRAN的RAU流程如[图1](17%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B-2915A4D8)所示。
图1  SGW不变的E-UTRAN到UTRAN的RAU流程


[]images/SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从EUTRAN覆盖区域移动到UTRAN强信号覆盖区域，UE选择3G网络。 


UE 向RNC发送路由区更新请求消息Routing Area Update Request，消息中携带的old
RAI和old P‑TMSI由GUTI映射得到。


RNC转发路由区更新请求消息Routing Area Update Request给new SGSN。


new SGSN发送SGSN上下文请求消息 Context Request给old MME以请求用户的移动性管理和会话管理相关信息。通过GUTI映射的old
RAI和old P-TMSI来标识唯一的old MME。 


old MME给new SGSN回上下文响应消息Context Response，消息中携带IMSI、ME Identity
(if available)、MSISDN。对于new SGSN来说，并不需要识别old MME。由old MME完成EPS承载到PDP上下文的一对一映射，以及QoS参数的映射。old 
MME仍保留用户的上下文信息，启动资源保护定时器，定时器超时后才删除用户上下文。 


（可选）如果Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。


new SGSN向old MME发送上下文确认消息Context Acknowledge，消息中携带ISR Activated。
当new SGSN指示ISR为激活状态时，old MME会将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还未完成时，UE向old
MME发起TAU流程，old MME能对GW和HSS的信息进行更新。 


new SGSN基于用户所在的位置及用户锚定的PGW确定需要使用的SGW，此SGW与E-UTRAN中选择的SGW相同，new
SGSN发送修改承载请求消息Modify Bearer Request消息给SGW，消息中携带new SGSN Address
and TEID, serving network identity, RAT type、ISR Activated。


（可选）若Modify bearer request消息携带的RAT type发生了变化，或者消息中携带有User
Location Information或UE Time Zone IE或User CSG information，SGW向PGW发送Modify
Bearer Request消息，消息中携带RAT type。


（可选）如果启用了动态PCC，并且PCRF订阅了RAT Type或者位置信息等事件，PGW将发起IP-CAN修改流程把这些信息发送给PCRF。 


PGW向PCRF发送CCR-U消息，通知PCRF修改IP-CAN会话。 


PCRF将PCC规则请求，与IP-CAN会话及PGW可用的业务信息进行关联。 


PCRF授权并进行策略决策。 


PCRF向PGW返回CCA-U消息，消息中携带PCC Rules、Event Triggers和已选择的IP-CAN承载建立模式（如果有变化）。 




（可选）PGW将Modify bearer request中变化的参数更新到承载上下文中，并向SGW返回Modify
Bearer Response消息。


SGW更新承载上下文，SGW返回承载修改响应消息Modify Bearer Respond给new SGSN，消息中携带SGW
address and TEID for uplink traffic。


new SGSN发起到HSS的位置更新流程，发出Update Location Request消息，将最新的UE位置信息及能力信息通知给HSS，消息中携带SGSN
Number、SGSN Address、IMSI、Homogenous Support of IMS Over PS Sessions。


HSS向old SGSN发起Cancel流程，发送Cancel Location Request消息，消息中携带IMSI、Cancellation
type，其中Cancellation type设置为Update Procedure，通知old SGSN用户已在new
SGSN完成接入。


old SGSN返回Cancel Location Acknowledge消息给HSS，并删除保存的用户上下文信息。


（可选）当old MME收到Context Acknowledge消息时，如果用户的S1连接未释放，则old
MME会在第5步中资源保护定时器超时后向eNodeB发送S1 Release Command消息。


（可选）eNodeB释放RRC连接，向old MME返回S1 Release Complete消息。 


HSS完成位置更新流程，记录用户最新所在的位置信息，返回Update Location Acknowledge消息给new SGSN，携带用户的签约数据IMSI和Subscription Data。


new SGSN向UE响应Routing Area Update Accept消息，消息中携带P-TMSI、P-TMSI
signature等信元。


（可选）如果Routing Area Update Accept消息中携带了P-TMSI，UE向new
SGSN发送Routing Area Update Complete消息进行确认新的P-TMSI被UE接受。


（可选）如果UE存在上行数据或未处理的信令，则向new SGSN发送Service Request消息，消息中携带P-TMSI,
CKSN、Service Type。Service Type为指示请求的业务类型，取值为Data或者Signaling。 


如果UE发送了Service Request消息，new SGSN会向RNC发送RAB Assignment
Request消息请求建立一个无线接入承载，消息中携带RAB ID(s)、QoS Profile(s)、GTP SNDs、GTP
SNUs、PDCP SNUs。 如果建立了Direct Tunnel，SGSN向RNC提供SGW的用户面地址和上行数据的TEID。


RNC向new SGSN返回RAB Assignment Response消息。 


如果new SGSN在步骤22中建立了Direct Tunnel，则为每个PDN链接向SGW发送Modify Bearer
Request消息，同时携带RNC的用户面地址和下行数据TEID。 


SGW更新下行数据的用户面地址及TEID，并向new SGSN返回Modify Bearer Response消息。 




### SGW改变的E-UTRAN到UTRAN的RAU流程 
### SGW改变的E-UTRAN到UTRAN的RAU流程 


业务模型 :从E-UTRAN向UTRAN的RAU是指UE通过小区重选或重定向等，E-UTRAN接入改为UTRAN接入，是为了实现EPS网络和UMTS网络互通，满足2/3G和LTE同时签约的用户跨RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从E-UTRAN向UTRAN的RAU流程中SGW可能发生改变或不改变。本业务模型为SGW改变情况。 


信令流程 :SGW改变的E-UTRAN到UTRAN的RAU流程如[图1](18%20SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B-2915FB8D)所示。
图1  SGW改变的E-UTRAN到UTRAN的RAU流程


[]images/SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从EUTRAN覆盖区域移动到UTRAN强信号覆盖区域，UE选择3G网络。 


UE 向RNC发送路由区更新请求消息Routing Area Update Request，消息中携带的old
RAI和old P‑TMSI由GUTI映射得到。


RNC转发路由区更新请求消息Routing Area Update Request给new SGSN。


new SGSN发送SGSN上下文请求消息Context Request给old MME，以请求用户的移动性管理和会话管理相关信息。由GUTI映射的old
RAI和old P-TMSI可以唯一标识old MME。 


old MME给new SGSN返回上下文响应消息Context Response，消息中携带MM Context、EPS
Bearer Contexts、SGW signalling Address and TEID(s)。对于new SGSN来说，并不需要识别old
MME。由old MME完成EPS承载到PDP上下文的一对一映射，以及QoS参数的映射。old MME仍保留用户的上下文信息，启动资源保护定时器，定时器超时后才删除用户上下文。 


（可选）如果Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。


new SGSN向old MME发送上下文确认消息Context Acknowledge，消息中携带的SGW change
indication指示了一个已经选择的new SGW。 old MME将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还未完成时，UE向old
MME发起TAU流程，old MME能对GW和HSS的信息进行更新。 


new SGSN基于用户所在的位置及用户锚定的PGW确定需要使用的SGW（此SGW与E-UTRAN中选择的SGW不同），new
SGSN给SGW发送创建会话请求消息Create Session Request，消息中携带IMSI、bearer contexts（包含PGW的地址）、SGSN
Address and TEID for the control plane、RAT Type、Type（指示SGW给PGW发送Modify
Bearer Request）、the Protocol Type over S5/S8、Serving Network信息。


new SGW向PGW发送修改承载请求消息Modify Bearer Request，消息中携带SGW Address
、SGW TEID、RAT type、Serving Network信息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发送CCR-U消息，发起IP-CAN修改流程，把RAT type等变化的信息发送给PCRF。 


PGW向PCRF发送CCR-U消息，通知PCRF修改IP-CAN会话。 


PCRF将PCC规则请求，与IP-CAN会话及PGW可用的业务信息进行关联。 


PCRF授权并进行策略决策。 


PCRF向PGW返回CCA-U消息，消息中携带PCC Rules、Event Triggers和已选择的IP-CAN承载建立模式（如果有变化）。 




PGW更新相关的承载上下文，并向new SGW返回承载修改响应消息Modify Bearer Response。 


new SGW更新承载上下文，并向new SGSN返回创建会话响应消息Create Session Response，消息中携带SGW
address and TEID、PGW Address and TEIDs at the PGW(s) for uplink traffic。 


new SGSN发起到HSS的位置更新流程，给HSS发出位置更新请求消息Update Location Request，消息携带SGSN Number、SGSN Address、IMSI、Homogenous Support of IMS Over
PS Sessions，将最新的UE位置信息及能力信息通知给HSS。


HSS向old SGSN发起Cancel流程，发送Cancel Location Request消息给old
SGSN，消息中携带IMSI、Cancellation type（Cancellation type设置为Update Procedure），通知old
SGSN用户已在新的SGSN完成接入。


old SGSN向HSS响应Cancel Location Acknowledge消息，删除保存的用户上下文信息。


（可选）当old MME收到Context Acknowledge消息时，如果用户的S1连接未释放，则old
MME会在第5步中资源保护定时器超时后向eNodeB发送S1 Release Command消息。


（可选）eNodeB释放RRC连接，向old MME返回S1 Release Complete消息。 


HSS完成位置更新流程，记录用户最新所在的位置信息，HSS向new SGSN返回位置更新确认消息Update Location Acknowledge，携带用户的签约数据Subscription Data。


old MME向old SGW发送删除会话请求消息Delete Session Request，通知old
SGW释放EPS承载资源，消息中携带Cause，Cause指示old SGW不要向PGW发起承载删除流程。


old SGW本地删除用户的会话，不通知PGW，向old MME返回删除会话响应消息Delete Session
Respond，并丢弃所有为UE缓存的数据包，消息中携带Cause。


new SGSN向UE响应Routing Area Update Accept消息，消息中携带P-TMSI、P-TMSI
signature。


（可选）如果Routing Area Update Accept消息中携带了P-TMSI，UE向new
SGSN发送Routing Area Update Complete消息进行确认新的P-TMSI被UE接受。 


（可选）如果UE存在上行数据或未处理的信令，则向new SGSN发送Service Request消息，消息中携带P-TMSI,
CKSN、Service Type，其中Service Type为指示请求的业务类型，取值为Data或者Signaling。


如果UE发送了Service Request消息，new SGSN会向RNC发送RAB指派请求消息RAB Assignment Request，请求建立一个无线接入承载，消息中携带RAB ID(s)、QoS Profile(s)、GTP
SNDs、GTP SNUs、PDCP SNUs。 如果建立了Direct Tunnel，new SGSN向RNC提供SGW的用户面地址和上行数据的TEID。


RNC向new SGSN返回RAB指派应答消息RAB Assignment Response。


如果new SGSN在步骤22中建立了Direct Tunnel，则为每个PDN链接向SGW发送修改承载请求消息Modify
Bearer Request，同时携带RNC的用户面地址和下行数据TEID。  


SGW更新下行数据的用户面地址及TEID，并向new SGSN返回修改承载响应消息Modify Bearer Response。 




### SGW不变的E-UTRAN到GEARN的RAU流程 
### SGW不变的E-UTRAN到GEARN的RAU流程 


业务模型 :从E-UTRAN向GERAN的RAU是指UE通过小区重选或重定向等E-UTRAN接入改为GERAN接入，是为了实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户跨RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从E-UTRAN向GERAN的RAU流程中SGW可能发生改变或不改变。本业务模型为SGW不改变情况。 


信令流程 :SGW不变的E-UTRAN到GEARN的RAU流程如[图1](19%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0GEARN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0GEARN%E7%9A%84RAU%E6%B5%81%E7%A8%8B-2918DC42)所示。
图1  SGW不变的E-UTRAN到GEARN的RAU流程


[]images/SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0GEARN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从EUTRAN覆盖区域移动到GERAN强信号覆盖区域，UE选择2G网络。 


UE 向BSS发送路由区更新请求消息Routing Area Update Request，消息中携带的old
RAI和old P‑TMSI由GUTI映射得到。


BSS转发路由区更新请求消息Routing Area Update Request给new SGSN。


new SGSN发送SGSN上下文请求消息 Context Request给old MME以请求用户的移动性管理和会话管理相关信息。通过GUTI映射的old
RAI和old P-TMSI来标识唯一的old MME。 


old MME给new SGSN回上下文响应消息Context Response，消息中携带IMSI、ME Identity
(if available)、MSISDN。对于new SGSN来说，并不需要识别old MME。由old MME完成EPS承载到PDP上下文的一对一映射，以及QoS参数的映射。old MME仍保留用户的上下文信息，启动资源保护定时器，定时器超时后才删除用户上下文。 


（可选）如果Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。


new SGSN向old MME发送上下文确认消息Context Acknowledge，消息中携带ISR Activated。
当new SGSN指示ISR为激活状态时，old MME会将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还未完成时，UE向old
MME发起TAU流程，old MME能对GW和HSS的信息进行更新。 


new SGSN基于用户所在的位置及用户锚定的PGW确定需要使用的SGW，此SGW与E-UTRAN中选择的SGW相同，new
SGSN发送修改承载请求消息Modify Bearer Request消息给SGW，消息中携带new SGSN Address
and TEID, serving network identity, RAT type、ISR Activated。


（可选）若Modify bearer request消息携带的RAT type发生了变化，或者消息中携带有User
Location Information或UE Time Zone IE或User CSG information，SGW向PGW发送Modify
Bearer Request消息，消息中携带RAT type。 


（可选）如果启用了动态PCC，并且PCRF订阅了RAT Type或者位置信息等事件，PGW将发起IP-CAN修改流程把这些信息发送给PCRF。 


PGW向PCRF发送CCR-U消息，通知PCRF修改IP-CAN会话。 


PCRF将PCC规则请求，与IP-CAN会话及PGW可用的业务信息进行关联。 


PCRF授权并进行策略决策。 


PCRF向PGW返回CCA-U消息，消息中携带PCC Rules、Event Triggers和已选择的IP-CAN承载建立模式（如果有变化）。 




（可选）PGW将Modify bearer request中变化的参数更新到承载上下文中，并向SGW返回Modify
Bearer Response消息。


SGW更新承载上下文，SGW返回承载修改响应消息Modify Bearer Respond给new SGSN，消息中携带SGW
address and TEID for uplink traffic。


new SGSN发起到HSS的位置更新流程，发出Update Location Request消息，将最新的UE位置信息及能力信息通知给HSS，消息中携带SGSN
Number、SGSN Address、IMSI、Homogenous Support of IMS Over PS Sessions。


HSS向old SGSN发起Cancel流程，发送Cancel Location Request消息，消息中携带IMSI、Cancellation
type，其中Cancellation type设置为Update Procedure，通知old SGSN用户已在new
SGSN完成接入。


old SGSN返回Cancel Location Acknowledge消息给HSS，并删除保存的用户上下文信息。


（可选）当old MME收到Context Acknowledge消息时，如果用户的S1连接未释放，则old
MME会在第5步中资源保护定时器超时后向eNodeB发送S1 Release Command消息。


（可选）eNodeB释放RRC连接，向old MME返回S1 Release Complete消息。 


HSS完成位置更新流程，记录用户最新所在的位置信息，返回Update Location Acknowledge消息给new SGSN，携带用户的签约数据IMSI和Subscription Data。


new SGSN向UE响应Routing Area Update Accept消息，消息中携带P-TMSI、P-TMSI
signature等信元。


（可选）如果Routing Area Update Accept消息中携带了P-TMSI，UE向new
SGSN发送Routing Area Update Complete消息进行确认新的P-TMSI被UE接受。 




### SGW改变的E-UTRAN到GEARN的RAU流程 
### SGW改变的E-UTRAN到GEARN的RAU流程 


业务模型 :从E-UTRAN向UTRAN的RAU是指UE通过小区重选或重定向等E-UTRAN接入改为GERAN接入，是为了实现EPS网络和GPRS网络互通，满足2/3G和LTE同时签约的用户跨RAT移动的业务连续性。 
MME与SGSN之间采用S3接口互通，从E-UTRAN向GERAN的RAU流程中SGW可能发生改变或不改变。本业务模型为SGW改变情况。 


信令流程 :SGW改变的E-UTRAN到GEARN的RAU流程如[图1](20%20SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0GEARN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.html#concept1__SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0GEARN%E7%9A%84RAU%E6%B5%81%E7%A8%8B-291A1378)所示。
图1  SGW改变的E-UTRAN到GEARN的RAU流程


[]images/SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0GEARN%E7%9A%84RAU%E6%B5%81%E7%A8%8B.png)



流程说明 :

UE从EUTRAN覆盖区域移动到GERAN强信号覆盖区域，UE选择2G网络。 


UE 向BSS发送路由区更新请求消息Routing Area Update Request，消息中携带的old
RAI和old P‑TMSI由GUTI映射得到。


BSS转发路由区更新请求消息Routing Area Update Request给new SGSN。


new SGSN发送SGSN上下文请求消息Context Request给old MME，以请求用户的移动性管理和会话管理相关信息。由GUTI映射的old
RAI和old P-TMSI可以唯一标识old MME。 


old MME给new SGSN回上下文响应消息Context Response，消息中携带MM Context、EPS
Bearer Contexts、SGW signalling Address and TEID(s)。对于new SGSN来说，并不需要识别old
MME。由old MME完成EPS承载到PDP上下文的一对一映射，以及QoS参数的映射。old MME仍保留用户的上下文信息，启动资源保护定时器，定时器超时后才删除用户上下文。 


（可选）如果Context Response消息中未包含IMEISV且SGSN支持ADD（Automatic
Device Detection），new SGSN将发起安全流程重新获取ME Identity (the IMEISV)。


new SGSN向old MME发送上下文确认消息Context Acknowledge，消息中携带的SGW change
indication指示了一个已经选择的new SGW。 old MME将上下文中GW和HSS的信息置为无效。这样可以保证在RAU流程还未完成时，UE向old
MME发起TAU流程，old MME能对GW和HSS的信息进行更新。 


new SGSN基于用户所在的位置及用户锚定的PGW确定需要使用的SGW（此SGW与E-UTRAN中选择的SGW不同），new
SGSN给SGW发送创建会话请求消息Create Session Request，消息中携带IMSI、bearer contexts（包含PGW的地址）、SGSN
Address and TEID for the control plane、RAT Type、Type（指示SGW给PGW发送Modify
Bearer Request）、the Protocol Type over S5/S8、Serving Network信息。


new SGW向PGW发送修改承载请求消息Modify Bearer Request，消息中携带SGW Address
、SGW TEID、RAT type、Serving Network信息。 


（可选）如果启用了动态PCC，且PCRF订阅了RAT type等信息，PGW通过向PCRF发送CCR-U消息，发起IP-CAN修改流程，把RAT type等变化的信息发送给PCRF。 


PGW向PCRF发送CCR-U消息，通知PCRF修改IP-CAN会话。 


PCRF将PCC规则请求，与IP-CAN会话及PGW可用的业务信息进行关联。 


PCRF授权并进行策略决策。 


PCRF向PGW返回CCA-U消息，消息中携带PCC Rules、Event Triggers和已选择的IP-CAN承载建立模式（如果有变化）。 




PGW更新相关的承载上下文，并向new SGW返回承载修改响应消息Modify Bearer Response。 


new SGW更新承载上下文，并向new SGSN返回创建会话响应消息Create Session Response，消息中携带SGW
address and TEID、PGW Address and TEIDs at the PGW(s) for uplink traffic。 


new SGSN发起到HSS的位置更新流程，给HSS发出位置更新请求消息Update Location Request，消息携带SGSN Number、SGSN Address、IMSI、Homogenous Support of IMS Over
PS Sessions，将最新的UE位置信息及能力信息通知给HSS。


HSS向old SGSN发起Cancel流程，发送Cancel Location Request消息给old
SGSN，消息中携带IMSI、Cancellation type（Cancellation type设置为Update Procedure），通知old
SGSN用户已在新的SGSN完成接入。


old SGSN向HSS响应Cancel Location Acknowledge消息，删除保存的用户上下文信息。


（可选）当old MME收到Context Acknowledge消息时，如果用户的S1连接未释放，则old
MME会在第5步中资源保护定时器超时后向eNodeB发送S1 Release Command消息。


（可选）eNodeB释放RRC连接，向old MME返回S1 Release Complete消息。 


HSS完成位置更新流程，记录用户最新所在的位置信息，HSS向new SGSN返回Update Location
Acknowledge消息，携带用户的签约数据Subscription Data。


old MME向old SGW发送删除会话请求消息Delete Session Request，通知old
SGW释放EPS承载资源，消息中携带Cause，Cause指示old SGW不要向PGW发起承载删除流程。


old SGW本地删除用户的会话，不通知PGW，向old MME返回删除会话响应消息Delete Session
Respond，并丢弃所有为UE缓存的数据包，消息中携带Cause。


new SGSN向UE响应Routing Area Update Accept消息，消息中携带P-TMSI、P-TMSI
signature。 


（可选）如果Routing Area Update Accept消息中携带了P-TMSI，UE向new
SGSN发送Routing Area Update Complete消息进行确认新的P-TMSI被UE接受。




### 业务请求流程 


业务模型 :业务请求流程是重建用户的S1-MME 口S1信令连接和S1-U口所有承载的E-RAB连接的流程。 
在业务请求流程中，用户的S1连接和E-RAB连接都被重建，空口的RRC连接和RB连接也会一并被重建。eNodeB保存用户的安全等信息，UE和MME中用户的ECM状态从空闲态变为连接态。 
业务请求流程完成之后，用户能继续通过EPS网络访问数据业务和其他业务。 


信令流程 :业务请求流程如[图1](21-%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E6%B5%81%E7%A8%8B.html#e__%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E6%B5%81%E7%A8%8B-4DB73542)所示。
图1  业务请求流程


[]images/%E7%BC%96%E5%8F%B721%20%E6%B5%81%E7%A8%8B%E5%9B%BE.png)



流程说明 :

UE发送RRC消息给eNodeB，RRC消息中包含UE发送给MME的Service Request消息。


eNodeB发送Initial UE Message消息给MME，其中包括UE发送给MME的Service
Request消息。如果MME不能处理该业务请求，则拒绝业务请求。


（可选）根据运营商的策略，非接入层的鉴权/安全过程可能被执行。 


MME发送Initial Context Setup Request消息给eNodeB，激活所有EPS承载的无线承载和S1承载。


eNodeB执行Radio Bearer Establishment过程，并且建立用户面安全上下文。当用户面无线承载建立和业务请求过程完成，EPS承载状态在用户与网络侧同步之后，UE将删除没有无线承载的EPS承载。如果一个缺省EPS承载的无线承载没有建立，UE必须本地去激活与这个缺省承载相关联的所有EPS承载。 


从UE发送的上行数据报文通过eNodeB发送给SGW，SGW再把上行数据报文发送给PGW。 


eNodeB发送Initial Context Setup Complete消息给MME。


MME按每PDN连接发送Modify Bearer Request消息给SGW，SGW收到Modify
Bearer Request消息后，就能把下行数据报文发送给用户了。


（可选）如果用户接入方式发生了改变或用户的位置信息发生了改变，SGW按每PDN连接发送Modify Bearer
Request消息给PGW。


（可选）如果动态PCC被部署，根据用户接入方式，PGW和PCRF完成IP-CAN会话修改过程。如果动态PCC没有被部署，PGW使用本地Qos策略。 


（可选）PGW向SGW响应Modify Bearer Response消息。


SGW向MME响应Modify Bearer Response消息。




### 寻呼流程 


业务模型 :寻呼流程是通知用户有用户下行数据报文或下行信令消息要发送给用户的流程。 
在寻呼流程中，用户得知有下行数据报文或下行信令消息需要接收，会触发用户发起业务请求流程。 
寻呼流程完成之后，用户发起业务请求对寻呼进行响应，通过业务请求流程重建S1-MME
口S1信令连接和S1-U口所有承载的E-RAB连接，业务请求流程完成之后，用户就能继续通过EPS网络访问数据业务和其他业务。 


信令流程 :寻呼流程如[图1](22-%E5%AF%BB%E5%91%BC%E6%B5%81%E7%A8%8B.html#f__%E5%AF%BB%E5%91%BC%E6%B5%81%E7%A8%8B-4DB765E3)所示。
图1  寻呼流程


[]images/%E7%BC%96%E5%8F%B722%20%E6%B5%81%E7%A8%8B%E5%9B%BE.png)



流程说明 :

如果SGW收到下行数据报文，但是对应承载的S1-U资源被释放，SGW缓存下行数据报文。 


SGW向UE所在的MME发送Downlink Data Notification消息。


MME发送Downlink Data Notification Acknowledge消息给SGW。如果SGW又收到发给这个用户的下行数据报文，SGW缓存数据报文，不会再给MME发送Downlink
Data Notification消息。


MME发送Paging消息给用户所在的TA /TA List对应的每一个eNodeB。


eNodeB向UE发起寻呼。 


UE收到eNodeB发送的Paging消息后，触发业务请求流程，详细流程参见“[业务请求流程](21-%E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E6%B5%81%E7%A8%8B.html)”
。




### S1释放流程 


业务模型 :S1释放流程是释放用户的S1-MME 口S1信令连接和S1-U口所有承载的E-RAB连接的流程。 
在S1释放流程中，用户的S1连接和E-RAB连接都被释放，空口的RRC连接和RB连接也会一并被释放。eNodeB不再保存用户的任何信息，UE和MME中用户的ECM状态从连接态变为空闲态。Non-GBR承载会被保留，GBR承载根据运营商策略，可以被保留或去激活。如果去激活GBR承载，触发MME发起的专有承载释放流程。 


信令流程 :S1释放流程如[图1](23-S1%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B.html#g__S1%E9%87%8A%E6%94%BE%E6%B5%81%E7%A8%8B-4DB79423)所示。
图1  S1释放流程


[]images/%E7%BC%96%E5%8F%B723%20%E6%B5%81%E7%A8%8B%E5%9B%BE.png)



流程说明 :

（可选）eNodeB检测到需要释放用户的信令连接和RB连接，向MME发送S1 UE Context Release
Request消息。


MME发送Release Access Bearers Request消息给SGW，请求SGW释放承载的S1-U口资源。


SGW删除所有与eNodeB相关的UE信息（eNodeB的用户面地址和TEID），给MME回Release Access
Bearers Response消息。该UE的SGW上下文的其它信息单元不受影响。 SGW保留了其为该UE的承载所分配的S1-U配置。如果有给UE的下行数据分组包，SGW开始缓存下行给UE的分组包，并发起网络触发的业务请求过程。


MME发送S1 UE Context Release Command给eNodeB，通知eNodeB释放S1信令连接。


（可选）如果RRC连接还没有释放，eNodeB发送RRC Connection Release给用户，用户确认RRC连接释放后，eNodeB删除用户的所有相关信息。


eNodeB发送S1 UE Context Release Complete消息给MME，确认S1连接的释放。MME删除与eNodeB有关的该UE的上下文信息(eNodeB地址和TEIDs)，但保留UE的其余上下文信息，包括SGW的S1-U配置信息(SGW地址和TEIDs)。为UE建立的所有non-GBR
EPS承载被保存在MME和SGW内。




### SGW不变的X2-based切换流程 


业务模型 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。 
本流程是在MME和SGW均不改变的情况下，UE从源eNodeB切换到目标eNodeB的流程。 


信令流程 :SGW不变的X2-based切换流程，如[图1](24%20X2-based%20handover,%20intra-MME,%20without%20SGW%20change%20CN.html#SGW%E4%B8%8D%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-4E11CB49__SGW%E4%B8%8D%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-4E123339)示。
图1  SGW不变的X2-based切换流程


[]images/24%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.png)



流程说明 :

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




### SGW改变的X2-based切换流程 


业务模型 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。 
本流程是在MME不变，但SGW发生改变的情况下，UE从源 eNodeB切换到目标eNodeB的流程。 


信令流程 :SGW改变的X2-based切换流程，如[图1](25%20X2-based%20handover,%20intra-MME,%20with%20SGW%20change%20CN.html#SGW%E6%94%B9%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-4E12B949__SGW%E6%94%B9%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-4E12BF10)所示。
图1  SGW改变的X2-based切换流程


[]images/25%20SGW%E6%94%B9%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.png)



流程说明 :

Target eNodeB发送Path Switch Request消息给MME通知UE已改变小区，消息中携带目标小区的小区全局标识（TAI+ECGI）以及需要切换路径的EPS承载列表，
MME根据TAI确定SGW需要改变，并选择一个新的SGW。


MME按每PDN连接发送Create Session Request消息给Target SGW。


Target SGW向PGW发送Modify Bearer Request消息，其中包含Serving
GW Address and TEID、RAT type、Serving Network等信息。


PGW更新相关的承载上下文，并向Target SGW返回Modify Bearer Response消息。自此，若有下行数据，PGW发送给Target
SGW。 


Target SGW发送Create
Session Response消息给MME，MME启动一个定时器，用于释放源SGW的资源。


MME给Target eNodeB发送Path Switch Request Acknowledge消息，确认路径切换请求完成，Target
eNodeB开始把上行数据报文发送给Target SGW。


Target eNodeB发送Release Resource消息给Source eNodeB，通知切换成功和触发Source
eNodeB资源释放。


MME在步骤[5](25%20X2-based%20handover,%20intra-MME,%20with%20SGW%20change%20CN.html#SGW%E6%94%B9%E5%8F%98%E7%9A%84X2-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-4E12B949__TargetSGW%E5%8F%91%E9%80%81CreateSessionResponse%E6%B6%88%E6%81%AF%E7%BB%99-4E1336FD)设置的释放SGW资源的定时器超时了，MME给Source SGW发送Delete Session Request消息通知Source SGW释放承载资源。


Source SGW给MME回Delete Session Response消息确认承载资源释放。


当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 




### MME、SGW均不改变的S1-based切换流程 
### MME、SGW均不改变的S1-based切换流程 


业务模型 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。在切换过程中，用户的无线连接无缝切换到目的无线接入网络。切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。 
该业务使用于MME和SGW均不改变的情况下，UE从Source eNodeB切换到Target eNodeB的基于S1接口的切换流程。 


信令流程 :MME、SGW均不改变的S1-based切换流程，如[图1](26%20S1-based%20handover,%20intra-MME,%20without%20SGW%20change%20CN.html#concept1__MMESGW%E5%9D%87%E4%B8%8D%E6%94%B9%E5%8F%98%E7%9A%84S1-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-49FAAA90)所示。
图1  MME、SGW均不改变的S1-based切换流程


[]images/26%20MME%E3%80%81SGW%E5%9D%87%E4%B8%8D%E6%94%B9%E5%8F%98%E7%9A%84S1-based%E5%88%87%E6%8D%A2.png)



流程说明 :

在以下情况，会导致Source eNodeB决定发起基于S1口的eNodeB间的切换流程。 

 
到Target eNodeB没有X2连接。 

 
目标侧eNodeB告知Source eNodeB之前的X2-based handover失败。 

 
Source eNodeB收到动态信息。 

 


Source eNodeB向MME发送Handover Required消息请求切换，消息中包含：Direct
Forwarding Path Availability，Source to Target transparent container，Target
eNodeB Identity，Target TAI，S1AP Cause参数。MME根据Target eNodeB Identity判断MME不需要改变，且根据Target
TAI判断SGW也不需要改变。


MME向Target eNodeB发送Handover Request消息通知Target eNodeB进行切换资源准备，消息中包含：EPS
Bearers to Setup，AMBR，S1AP Cause，Source to Target transparent container，Handover
Restriction List参数。


Target eNodeB向MME发送Handover Request Ackownledge消息确认切换资源准备完成，消息中包含：EPS
Bearer Setup list，EPS Bearers failed to setup list，Target to Source
transparent container参数.
 说明： 
如果所有default EPS bearers都被Target
eNodeB拒绝，则MME拒绝切换处理。 


可选：如果采用间接转发，MME向SGW发送Create Indirect Data Forwarding
Tunnel Request消息通知SGW创建间接数据前转隧道，消息中包含：Cause，Target eNodeB addresses
and TEIDs for forwarding参数，SGW重定位的情况下，消息包括到Target SGW的隧道标识。


可选：SGW向MME响应Create Indirect Data Forwarding Tunnel
Response消息，消息包含：Target Serving GW addresses and TEIDs for forwarding参数。


MME向Source eNodeB发送Handover Command消息通知切换执行，消息中包括：Target
to Source transparent container，Bearers subject to forwarding，Bearers
to Release。
Source eNodeB在Target to Source transparent container中构造Handover Command消息，并发送给UE。


可选：Source eNodeB通过MME向Target eNodeB发送eNB Status Transfer消息，该消息传递E-RAB对应的PDCP和HFN状态信息。如果没有E-RAB采用PDCP状态保存机制，则源eNodeB可能不会发送此消息。


可选：Source eNodeB通过直接数据前转的方式，把接收到的下行数据报文前转给Target eNodeB。


可选：Source eNodeB通过间接数据前转的方式，把接收到的下行数据报文前转给Target eNodeB。


UE成功的同步到目的小区后，会向Target eNodeB发送Handover Confirm消息确认切换。
从Source eNodeB转发的下行数据包可以发送给UE，同样，从UE发出的上行数据包可以转发给SGW，从而到达PGW。 


Target eNodeB向MME发送Handover Notify消息通知切换，消息中包含：TAI+ECGI。
MME启动一个定时器来监视Source
eNodeB和SGW的资源释放情况。 


MME按每PDN连接向SGW发送Modify Bearer Request消息请求修改承载，消息中包含：eNodeB
addresses and TEIDs allocated at the target eNodeB for downlink traffic
on S1_U for the accepted EPS bearers参数。


可选：如果Modify Bearer Request消息中携带有变化的User Location
Information和/或UE Time Zone和/或User CSG Information等信息，则为每个PDN连接向PGW发送Modify Bearer Request消息，消息包含：User Location Information IE、UE
Time Zone IE、User CSG Information IE。


可选：PGW将Modify Bearer Request消息中变化的参数更新到承载上下文中，并向SGW返回Modify Bearer Response消息。


SGW向MME发送Modify Bearer Response消息。
如果SGW没有发生改变，为了辅助Target
eNodeB中的重排序功能（reordering function），在SGW完成路径切换之后，SGW立刻发送一个或多个“End Mark”报文给Source
eNodeB。 


当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 


当步骤[12](26%20S1-based%20handover,%20intra-MME,%20without%20SGW%20change%20CN.html#concept1__TargetENodeB%E5%90%91MME%E5%8F%91%E9%80%81HandoverNotify%E6%B6%88%E6%81%AF%E9%80%9A-4A910657)中的定时器T1超时，MME向Source eNodeB发送UE
Context Release Command消息通知释放用户上下文。


Source eNodeB释放用户相关的所有资源，向MME回响应UE Context Release Complete消息。


可选：MME的资源释放定时器超时，如果间接转发被使用，MME向SGW发送Delete Indirect
Data Forwarding Tunnel Request消息，释放间接数据前转隧道资源。


可选：SGW向MME回响应Delete Indirect Data Forwarding Tunnel
Response消息。




### MME不变、SGW改变的S1-based切换流程 
业务模型 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。在切换过程中，用户的无线连接无缝切换到目的无线接入网络。切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。 
该业务使用于MME不变、SGW改变的情况下，UE从源eNodeB切换到目标eNodeB的基于S1接口的切换流程。 
信令流程 :MME不变、SGW改变的S1-based切换流程，如[图1](27%20S1-based%20handover,%20intra-MME,%20with%20SGW%20change%20CN.html#concept1__MMESGW%E5%9D%87%E4%B8%8D%E6%94%B9%E5%8F%98%E7%9A%84S1-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-49FAAA90)所示。
图1  MME不变、SGW改变的S1-based切换流程
[]images/27%20MME%E4%B8%8D%E5%8F%98%E3%80%81S-GW%E6%94%B9%E5%8F%98%E7%9A%84S1-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.png)
流程说明 :在以下情况，会导致Source eNodeB决定发起基于S1口的eNodeB间的切换流程。 
到Target eNodeB没有X2连接。 
目标侧eNodeB告知Source eNodeB之前的X2-based handover失败。 
Source eNodeB收到动态信息。 
Source eNdoeB向MME发送Handover Required消息请求切换，消息中包含：Direct
Forwarding Path Availability，Source to Target transparent container，Target
eNodeB Identity，Target TAI，S1AP Cause参数，MME根据Target eNodeB Identity判断MME不需要改变。
MME根据用户目前所在的TAI，确定SGW是否需要改变。如果SGW发生改变，则MME按每PDN连接给Target SGW发送Create Session Request消息，消息中包含：bearer context(s) with PDN GW
addresses， TEIDs (for GTP-based S5/S8) at the PDN GW(s) at the PDN
GW(s) for uplink traffic参数。
Target SGW向MME发送Create Session Response消息。
MME发送Handover Request消息通知Target eNodeB进行切换资源准备，消息中包含：EPS
Bearers to Setup，AMBR，S1AP Cause，Source to Target transparent container，Handover
Restriction List参数。
Target eNodeB向MME发送Handover Request Ackownledge消息确认切换资源准备完成，消息中包含：EPS
Bearer Setup list，EPS Bearers failed to setup list，Target to Source
transparent container参数。
EPS Bearer Setup list是一张列表，包含地址和S1-U参考点上分配给目标eNodeB下行流量的TEID(一个承载分配一个TEID的原则)，如果必要的话也会包含地址和接受转发数据的TEID。 
 说明： 
如果所有default EPS bearers都被目标eNodeB拒绝，则MME拒绝切换处理。 
可选：如果采用间接转发并且SGW发生改变了，MME向Target SGW发送Create Indirect
Data Forwarding Tunnel Request消息通知SGW创建间接数据前转隧道，消息中包含：Cause，Target
eNodeB addresses, TEIDs for forwarding。
可选：Target SGW向MME响应Create Indirect Data Forwarding
Tunnel Response消息，消息包含：Target Serving GW addresses， TEIDs for
forwarding参数。
间接转发可能经过不同于锚定UE数据的SGW进行转发。 
可选：如果采用间接转发，MME向SGW发送Create Indirect Data Forwarding
Tunnel Request消息通知SGW创建间接数据前转隧道，消息中包含：Cause，Target eNodeB addresses，
TEIDs for forwarding参数。SW重定位的情况下，消息中包括到Target SGW的隧道标识。
可选：Source SGW向MME响应Create Indirect Data Forwarding
Tunnel Response消息，消息包含：Serving GW addresses， TEIDs for forwarding参数。
间接转发可能经过不同于锚定UE数据的SGW进行转发。 
MME向Source eNodeB发送Handover Command消息通知切换执行，消息中包括：Target
to Source transparent container，Bearers subject to forwarding，Bearers
to Release。
Source eNodeB在Target to Source transparent container中构造Handover Command消息，并发送给UE。在收到消息之后，UE将删除没有收到目标小区中相关EPS无线承载的EPS承载。
可选：Source eNodeB通过MME向Target eNodeB发送eNB Status Transfer消息，该消息传递E-RAB对应的PDCP和HFN状态信息。
可选：Source eNodeB通过直接数据前转的方式，把接收到的下行数据报文前转给Target eNodeB。
可选：Source eNodeB通过间接数据前转的方式，把接收到的下行数据报文前转给Target eNodeB。
UE成功的同步到目的小区后，会向Target eNodeB发送Handover Confirm消息确认切换。来自Source
eNodeB的下行转发数据被传到UE，而上行数据由UE发送出去，转发到Target SGW和PGW上。
Target eNodeB向MME发送Handover Notify消息通知切换，消息中包含：TAI+ECGI。
MME启动一个定时器T2来监视Source
eNodeB和Source SGW的资源释放情况。 
MME按每PDN连接向Target SGW发送Modify Bearer Request消息请求修改承载，消息中包含：eNodeB
addresses and TEIDs allocated at the target eNodeB for downlink traffic
on S1_U for the accepted EPS bearers参数。
如果PGW请求了User Location
Information或者User CSG information（由UE上下文判断），MME也会在这条信息中包含这两个信元。如果UE的时区（Time
Zone）发生了改变，MME在信息中包含UE Time Zone信元。 
Target SGW向PGW发送Modify Bearer Request消息，其中包含Serving
GW Address and TEID、RAT type、Serving Network等信息。
如果上一步包含了User
Location Information信元、UE Time Zone信元或者User CSG Information信元，S-GW也会在此信息中包含。对于non-accepted承载，Target
SGW也会为之分配基于S5/S8的下行TEID。 
PGW更新相关的承载上下文，并向Target SGW返回Modify Bearer Response消息。
Target SGW向MME发送Modify Bearer Response消息，消息中包含：PDN GW
addresses and TEIDs (for GTP-based S5/S8) at the PDN GW(s) for uplink
traffic参数。
当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 
当步骤[16](27%20S1-based%20handover,%20intra-MME,%20with%20SGW%20change%20CN.html#concept1__TargetENodeB%E5%90%91MME%E5%8F%91%E9%80%81HandoverNotify%E6%B6%88%E6%81%AF%E9%80%9A-4A90F457)中的定时器T2超时，MME向Source eNodeB发送UE
Context Release Command消息通知释放用户上下文。
Source eNodeB释放用户相关的所有资源，向MME回响应UE Context Release Complete消息。
当步骤[16](27%20S1-based%20handover,%20intra-MME,%20with%20SGW%20change%20CN.html#concept1__TargetENodeB%E5%90%91MME%E5%8F%91%E9%80%81HandoverNotify%E6%B6%88%E6%81%AF%E9%80%9A-4A90F457)中的定时器T2超时，且MME在Forward Relocation
Response消息中收到SGW改变指示，则MME向Source SGW发送Delete Session Request消息通知Source SGW释放承载资源，消息中包含：Cause，LBI参数。
Source SGW向MME回响应Delete Session Response消息确认承载资源释放。
可选：MME的资源释放定时器超时，如果间接转发被使用，MME向Source SGW发送Delete
Indirect Data Forwarding Tunnel Request消息，释放间接数据前转隧道资源。
可选：Source SGW向MME回响应Delete Indirect Data Forwarding
Tunnel Response消息。
可选：当步骤[16](27%20S1-based%20handover,%20intra-MME,%20with%20SGW%20change%20CN.html#concept1__TargetENodeB%E5%90%91MME%E5%8F%91%E9%80%81HandoverNotify%E6%B6%88%E6%81%AF%E9%80%9A-4A90F457)中的定时器T2超时，如果间接转发被使用，MME向Target SGW发送Delete Indirect Data Forwarding Tunnel Request消息，释放间接数据前转隧道资源。
### MME重选、SGW不变的S1-based切换流程 
### MME重选、SGW不变的S1-based切换流程 


业务模型 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。在切换过程中，用户的无线连接无缝切换到目的无线接入网络。切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。 
该业务使用于MME改变、SGW不变的情况下，UE从源eNodeB切换到目标eNodeB的基于S1接口的切换流程。 


信令流程 :MME重选、SGW不变的S1-based切换流程，如[图1](28%20%20S1-based%20handover,%20inter-MME,%20without%20SGW%20change%20CN.html#concept1__MMESGW%E5%9D%87%E4%B8%8D%E6%94%B9%E5%8F%98%E7%9A%84S1-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-49FAAA90)所示。
图1  MME重选、SGW不变的S1-based切换流程


[]images/28%20MME%E9%87%8D%E9%80%89%E3%80%81SGW%E4%B8%8D%E5%8F%98%E7%9A%84S1-based%E5%88%87%E6%8D%A2.png)



流程说明 :

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
Target MME根据TAI判断SGW没有发生改变。 


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


Target MME向Source MME发送Forward Relocation Response消息，消息中包括Cause,
Target to Source transparent container, Serving GW change indication,
EPS Bearer Setup List, Addresses and TEIDs等参数。


可选：如果使用间接转发，Source MME向SGW发送Create Indirect Data
Forwarding Tunnel Request消息，消息中包括addresses and TEIDs for forwarding。


SGW向Source MME回复Create Indirect Data Forwarding Tunnel Response消息，消息中包括Serving GW addresses and TEIDs for forwarding。


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


Source MME向Target
MME响应Forward Relocation Complete Acknowledge消息，并启动定时器T3来监视Source
eNodeB和Source SGW的资源的释放情况。


Target MME按每PDN连接向SGW发送Modify Bearer Request消息，消息中包括eNodeB
address and TEID allocated at the target eNodeB for downlink traffic
on S1 U for the accepted EPS bearers等参数。
如果PGW请求了User Location
Information或者User CSG information（由UE上下文判断），MME也会在这条信息中包含这两个信元。如果UE的时区（Time
Zone）发生了改变，MME在信息中包含UE Time Zone信元。 


可选：若Modify bearer request消息携带有变化的User Location
Information或UE Time Zone IE等信息，SGW向PGW发送Modify Bearer Request消息，消息包含：User Location Information IE、UE Time Zone IE、User CSG Information
IE。


可选：PGW更新本地上下文并向SGW返回Modify Bearer Response消息。


SGW向Target MME发送Modify Bearer Response消息。


当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 


当[16](28%20%20S1-based%20handover,%20inter-MME,%20without%20SGW%20change%20CN.html#concept1__SourceMME%E5%90%91TargetMME%E5%93%8D%E5%BA%94ForwardRelocat-4C23781F)中的定时器T3超时，Source MME向Source eNodeB发送UE Context Release Command消息。


Source eNodeB释放与UE相关的资源并向Source MME响应UE Context Release
Complete消息。


可选：如果使用间接转发且[16](28%20%20S1-based%20handover,%20inter-MME,%20without%20SGW%20change%20CN.html#concept1__SourceMME%E5%90%91TargetMME%E5%93%8D%E5%BA%94ForwardRelocat-4C23781F)中的定时器T3超时，源MME向SGW发送Delete Indirect
Data Forwarding Tunnel Request消息，释放为间接转发分配的临时资源。


可选：SGW向Source MME响应Delete Indirect Data Forwarding
Tunnel Session Response消息。




### MME和SGW均重选的S1-based切换流程 
业务模型 :MME网元切换流程是用户从一个小区移动到另一个小区时保证用户业务连续性的过程，包括基于X2口和S1口的切换。在切换过程中，用户的无线连接无缝切换到目的无线接入网络。切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。 
该业务使用于MME改变、SGW改变的情况下，UE从源eNodeB切换到目标eNodeB的基于S1接口的切换流程。 
信令流程 :MME和SGW均重选的S1-based切换流程，如[图1](29%20%20S1-based%20handover,%20inter-MME,%20with%20SGW%20change%20CN.html#concept1__MME%E5%92%8CSGW%E5%9D%87%E9%87%8D%E9%80%89%E7%9A%84S1-based%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-4C2A8AEB)所示。
图1  MME和SGW均重选的S1-based切换流程
[]images/29%20MME%E5%92%8CSGW%E5%9D%87%E9%87%8D%E9%80%89%E7%9A%84S1-based%E5%88%87%E6%8D%A2.png)
流程说明 :基于如下原因，Source eNodeB决定发起基于S1口的eNodeB间的切换流程。 
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
Source MME向Target
MME响应Forward Relocation Complete Acknowledge消息，并启动定时器T4来监视Source
eNodeB和Source SGW的资源的释放情况。
Target MME为每个PDN连接向Target
SGW发送Modify Bearer Request消息，消息中包括eNodeB address and TEID allocated
at the target eNodeB for downlink traffic on S1 U for the accepted
EPS bearers等参数。
如果PGW请求了User Location Information或者User CSG
information（由UE上下文判断），MME也会在这条信息中包含这两个信元。如果UE的时区（Time Zone）发生了改变，MME在信息中包含UE
Time Zone信元。 
Target SGW为来自PGW的下行通道分配地址和TEIDs，并为每个PDN连接向PGW发送Modify bearer
request消息，消息包含：Serving GW addresses for user plane and TEID(s)、Serving
Network等参数。如果步骤[21](29%20%20S1-based%20handover,%20inter-MME,%20with%20SGW%20change%20CN.html#concept1__TargetMME%E4%B8%BA%E6%AF%8F%E4%B8%AAPDN%E8%BF%9E%E6%8E%A5%E5%90%91TargetSGW%E5%8F%91%E9%80%81Modify-4C2C1802)包含了User Location Information 信元、UE
Time Zone信元或者User CSG Information信元，SGW也会在此信息中包含。
PGW更新本地上下文并向Target SGW返回Modify Bearer Response消息。
Target SGW向Target MME发送Modify Bearer Response消息。
当满足跟踪区更新触发条件之一时，UE发起一个跟踪区更新过程。 
当[20](29%20%20S1-based%20handover,%20inter-MME,%20with%20SGW%20change%20CN.html#concept1__SourceMME%E5%90%91TargetMME%E5%93%8D%E5%BA%94ForwardRelocat-4C23781F)中的定时器T4超时，Source MME向Source eNodeB发送UE Context Release Command消息。
Source eNodeB释放与UE相关的资源并向Source MME响应UE Context Release
Complete消息。
当[20](29%20%20S1-based%20handover,%20inter-MME,%20with%20SGW%20change%20CN.html#concept1__SourceMME%E5%90%91TargetMME%E5%93%8D%E5%BA%94ForwardRelocat-4C23781F)中的定时器超时，且Source MME在Forward Relocation
Response消息中收到SGW改变指示，则Source MME向Source SGW发送Delete Session
Request消息删除EPS承载资源，消息包含：Cause, LBI。Cause指示SGW变更及SGW不要向PGW发起承载删除流程。
Source SGW向Source MME响应Delete Session Response消息。
可选：如果使用间接转发且[20](29%20%20S1-based%20handover,%20inter-MME,%20with%20SGW%20change%20CN.html#concept1__SourceMME%E5%90%91TargetMME%E5%93%8D%E5%BA%94ForwardRelocat-4C23781F)中的定时器T4超时，Source MME向Source SGW发送Delete Indirect Data Forwarding Tunnel Request消息，释放为间接转发分配的临时资源。
可选：Source SGW向Source MME响应Delete Indirect Data Forwarding
Tunnel Session Response消息。
可选：如果使用间接转发且[20](29%20%20S1-based%20handover,%20inter-MME,%20with%20SGW%20change%20CN.html#concept1__SourceMME%E5%90%91TargetMME%E5%93%8D%E5%BA%94ForwardRelocat-4C23781F)中的定时器T4超时，Target MME向Target SGW发送Delete Indirect Data Forwarding Tunnel Request消息，释放为间接转发分配的临时资源。
可选：Target SGW向Target MME响应Delete Indirect Data Forwarding
Tunnel Session Response消息。
### MME和SGSN采用Gn口的UTRAN到E-UTRAN的切换流程 
业务模型 :用户通过UTRAN注册到PS网络，正在使用数据业务，移动到LTE覆盖信号强的区域后，UTRAN为了保持用户数据业务的连续性，把用户从UTRAN切换到E-UTRAN。MME和SGSN间使用Gn接口。 
信令流程 :MME和SGSN采用Gn口的UTRAN到E-UTRAN的切换流程，如[图1](30%20MME%E5%92%8CSGSN%E9%87%87%E7%94%A8Gn%E5%8F%A3%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#concept1__MME%E5%92%8CSGSN%E9%87%87%E7%94%A8Gn%E5%8F%A3%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-3F3B9CB4)所示。
图1  MME和SGSN采用Gn口的UTRAN到E-UTRAN的切换流程
[]images/30%20MME%E5%92%8CSGSN%E9%87%87%E7%94%A8Gn%E5%8F%A3%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.png)
流程说明 :源RNC决策发起向E-UTRAN的切换。 
源RNC向old Gn/Gp SGSN发送重定位申请消息Relocation Required，触发重定位流程，消息中携带Relocation
Type、Cause、Source ID、Target ID、Source RNC To target eNodeB Transparent
Container。
old Gn/Gp SGSN根据Target ID判断是inter-SGSN重定位，根据Target ID选择new
MME。 old Gn/Gp SGSN向new MME发送前转重定位请求消息Forward Relocation Request，触发重定位资源分配流程，消息中携带IMSI、MM Context、PDP Context、Target Identification、RAN
Transparent Container、RANAP Cause。
new MME收到前转重定位请求消息Forward Relocation Request后，创建MM上下文和EPS承载上下文，把PDP上下文参数映射到EPS承载上下文参数。MME选择一个SGW，为每个PDN连接，向SGW发送一个创建会话请求消息Create Session Request，请求SGW创建会话，消息中携带bearer context(s) with
PGW addresses and TEIDs for uplink traffic、APN-AMBR、Serving Network。如果new
MME没有从old Gn/Gp SGSN收到APN-AMBR，将从MBR映射出APN-AMBR并提供给SGW。
SGW向new MME返回创建会话应答消息Create Session Response，消息中携带SGW
addresses and uplink TEID(s) for user plane。
new MME向目标eNodeB发送切换请求消息Handover Request，请求建立承载，消息中携带Cause、UE
Security Capabilities、Security Context、NAS Security Parameters to
E-UTRAN、EPS Bearers to be setup list、Source to Target Transparent
Container、UE-AMBR。
目标eNodeB分配请求的资源，并向new MME返回切换请求确认消息Handover Request Acknowledge，消息中携带Target to Source Transparent Container、EPS Bearers setup list、EPS
Bearers failed to setup list、Cause。
（可选）如果使用了“Indirect Forwarding”，new MME向SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、MME
Tunnel Endpoint Identifier for Control Plane、MME Address for Control
plane、Target eNB Address and TEID(s) for DL user plane。
（可选）SGW创建数据转发隧道，返回创建间接数据转发隧道应答消息Create Indirect Data Forwarding
Tunnel Response，消息中携带Cause、SGW DL TEID(s)。
目标eNodeB和new MME间的资源分配完成后，new MME向old Gn/Gp SGSN发送前转重定位应答消息Forward Relocation Response，消息中携带Cause、RAN Transparent Container、RANAP
Cause、Target-RNC Information。这条消息指示目标eNodeB已经准备好接收来自原RNC的转发下行PDU，即relocation
resource allocation流程成功完成。
old Gn/Gp SGSN向源RNC发送重定位命令消息Relocation Command，通知其切换准备完成，消息中携带target
eNodeB To Source RNC Transparent Container、RABs To Be Released、RABs
Subject To Data Forwarding。
（可选）基于QoS profile，源RNC进行数据转发，数据转发消息为Forwarding of Data。数据转发需要通过Iu接口进行，源RNC和目标eNodeB之间的GTP-PDU数据交换是在源RNC进行复制，然后通过IP层路由给SGW/目标eNodeB。每一个使用lossless
PDCP的无线承载，与传输相关的GTP-PDU但未被acknowledged PDCP-PDUs复制，并连同相关的下行 PDCP序列号，通过IP层路由给SGW/目标eNodeB。源RNC继续发送复制的下行数据和接收上行数据。
在目标eNodeB没有和UE建立RB之前，下行用户面数据到达时，目标eNodeB可能根据related QoS profile，缓存或者丢弃到达的下行GTP-PDUs。转发功能只能用于下行用户数据的转发。 
在发送RRC消息之前，缺少发送顺序的RAB上下行数据将被缓存在源RNC中。 例如，RRC消息是Physical Channel
Reconfiguration for RNS to RNS relocation 或者Intersystem to UTRAN Handover
for BSS to RNS relocation 或者Handover from UTRAN Command for BSS relocation
或者Handover Command for BSS to BSS relocation。当源RNC准备好之后，源RNC将通过向UE发送RRC Message消息来触发执行relocation of SRNS，这条RRC消息来源于目标eNodeB到源RNC的transparent
container，如Physical Channel Reconfiguration消息，消息中应包括UE信息单元和CN消息单元。
当UE完成重新配置之后，向目标SRNC发送RRC消息，如Physical Channel Reconfiguration Complete消息。如果收到带有序列号的Forward
SRNS Context消息，至此和UE的分组交换可以开始了。如果没有收到，目标eNodeB发起所有RAB的数据传输，此时不需要发送顺序。 
（可选）在UTRAN到E-UTRAN的切换过程中，没有RAN上下文传输。如果源RNC产生任何SRNC上下文，MME向SGSN响应该上下文的接收，而忽略消息的内容。  
当UE成功接入目标eNodeB，目标eNodeB将向new MME发送切换通知消息Handover Notify，消息中携带TAI+ECGI。UE将得到从HO from UTRAN Command消息中尚未建立E-RAB的EPS承载，并且在本步骤中不发送NAS消息，在本地将其去激活。
new MME在收到切换通知消息Handover Notify消息后，向old Gn/Gp SGSN发送前转重定位完成消息Forward Relocation Complete，告知重定位完成。
old Gn/Gp SGSN向new MME响应前转重定位完成确认消息Forward Relocation Complete
Acknowledge。new MME收到消息后启动一个资源保护定时器。
new MME为每个PDN连接向SGW发送修改承载请求消息Modify Bearer Request，消息中携带Cause、Tunnel
Endpoint Identifier Control Plane、MME Address for Control Plane、eNodeB
Address(es) and TEID(s) for User Traffic、RAT type、APN-AMBR。如果PGW请求了UE's
location或者User CSG information（由UE上下文决定），MME也会在这条信息中包含这两个信元。如果UE的时区（Time
Zone）发生了改变，MME在信息中包含UE Time Zone信元。
SGW向PGW发送修改承载请求消息Modify Bearer Request，消息中携带SGW Address
and TEID、RAT type、Serving Network等信息。PGW更新相关的承载上下文，并向SGW响应修改承载应答消息Modify Bearer Response，消息中携带Default bearer id、APN Restriction。当UE从Gn/Gp
SGSN迁移到MME时，PGW向SGW发送每一个承载上下文的APN Restriction。
SGW向new MME返回修改承载应答消息Modify Bearer Response，消息中携带Cause、Default
bearer id、APN restriction。SGW把收到的APN Restriction转发给MME，至此，UE、目标eNodeB、SGW和PGW之间所有承载的用户面路径完成建立。
old Gn/Gp SGSN在收到前转重定位完成消息Forward Relocation Complete时，old
Gn/Gp SGSN给源RNC发送Iu连接释放命令消息Iu Release Command。
当源RNC的数据转发定时器超时时，源RNC给old Gn/Gp SGSN返回Iu连接释放完成消息Iu Release
Complete。
UE发起TAU流程。 new MME确认是Inter-RAT Handover流程之后的TAU流程，只执行TAU流程的子集，也就是说，不执行new
MME和old Gn/Gp SGSN之间的上下文传输流程（context transfer procedures）。在TAU流程中new
MME从HSS得到subscribed UE-AMBR value、subscribed APN-AMBR value和EPS Subscribed
QoS profile。 
new MME根据subscribed UE-AMBR计算used UE-AMBR，如果计算出的值与给目标eNodeB的值不同，或者subscribed
APN-AMBR与之前的APN-AMBR不同，或者默认承载的QoS与EPS Subscribed QoS profile不同，则new
MME发起HSS修改签约QoS，导致承载修改（HSS Initiated Subscribed QoS Modification）流程。 
（可选）当资源保护定时器超时，new MME向SGW发送删除间接数据转发隧道请求消息Delete Indirect
Data Forwarding Tunnel Request，请求删除数据转发隧道。
（可选）SGW向new MME返回删除间接数据转发隧道应答消息Delete Indirect Data Forwarding
Tunnel Response。
### MME和SGSN采用Gn口的E-UTRAN到UTRAN的切换流程 
业务模型 :用户通过LTE注册到EPS网络，正在使用数据业务，移动到LTE覆盖信号弱，但UTRAN覆盖信号强的区域后，E-UTRAN为了保持用户数据业务的连续性，把用户从E-UTRAN切换到UTRAN。 
MME和SGSN间使用Gn接口。 
信令流程 :MME和SGSN采用Gn口的E-UTRAN到UTRAN的切换流程，如[图1](31%20MME%E5%92%8CSGSN%E9%87%87%E7%94%A8Gn%E5%8F%A3%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#concept1__MME%E5%92%8CSGSN%E9%87%87%E7%94%A8Gn%E5%8F%A3%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-3F3D12EB)所示。
图1  MME和SGSN采用Gn口的E-UTRAN到UTRAN的切换流程
[]images/31%20MME%E5%92%8CSGSN%E9%87%87%E7%94%A8Gn%E5%8F%A3%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.png)
流程说明 :源eNodeB决策发起向UTRAN的切换。此时，上下行用户数据通过如下承载进行传输：Bearer(s) between
UE and source eNodeB、 GTP tunnel(s) between source eNodeB and SGW
、GTP tunnel(s) between SGW and PGW。 
源eNodeB向old MME发送切换申请消息Handover Required，触发切换流程，消息中携带S1
AP Cause、Target RNC Identifier、Source eNodeB Identifier、Source to
Target Transparent Container。
old MME根据Target ID判断不是intra-MME handover，根据Target ID选择new Gn/Gp
SGSN。 old MME向new Gn/Gp SGSN发送前转重定位请求消息Forward Relocation Request，触发切换资源分配流程，消息中携带IMSI、MM Context、PDP Context、Target Identification、RAN
Transparent Container、RANAP Cause。Old MME把承载上下文参数映射到PDP上下文。
new Gn/Gp SGSN收到前转重定位请求消息Forward Relocation Request后，创建MM上下文和PDP上下文。
new Gn/Gp SGSN向目标RNC发送重定位请求消息Relocation Request，请求建立承载，消息中携带Permanent
NAS UE Identity、Cause、Source RNC To Target RNC Transparent Container、RAB
To Be Setup。
对每一个RAB，RAB to be Setup应该包含：RAB ID、RAB parameters、Transport
Layer Address、Iu Transport Association等信息。RAB ID信元对应NSAPI的值，RAB parameter信元提供RAB的QoS参数，Transport
Layer Address 上行用户面地址，Iu Transport Association上行用户面TEID。如果new Gn/Gp
SGSN在RNC和PGW间建立Direct Tunnel，Transport Layer Address为PGW的用户面地址， Iu
Transport Association为PGW的用户面TEID。 
目标RNC分配请求的资源，并向new Gn/Gp SGSN返回重定位请求确认消息Relocation Request
Acknowledge，消息中携带Target RNC To Source RNC Transparent Container、RABs
Setup、RABs Failed To Setup。
每一个RAB to be setup都由一对Transport
Layer Address、Iu Transport Association组成。Transport Layer Address是RNC用户面地址，Iu
Transport Association为下行用户面TEID。Target RNC To Source RNC Transparent
Container包含UE切换所需的所有无线相关信息。 
目标RNC和new Gn/Gp SGSN间的资源分配过程完成后，new Gn/Gp SGSN向old MME发送前转重定位应答消息Forward Relocation Response，消息中携带Cause、RAN Transparent Container、RANAP
Cause、Target-RNC Information。这条消息指示目标RNC已准备好接收来自原eNodeB的转发下行PDU，即relocation
resource allocation流程成功完成。
（可选）如果使用了“Indirect Forwarding”，old MME向SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、MME
Tunnel Endpoint Identifier for Control Plane、MME Address for Control
plane、Target RNC Address and TEID(s) for DL user plane。
（可选）SGW创建数据转发隧道，返回创建间接数据转发隧道应答消息Create Indirect Data Forwarding
Tunnel Response，消息中携带Cause、SGW DL TEID(s)。
old MME向源eNodeB发送切换命令消息Handover Command，通知其切换准备完成，消息中携带Target
to Source Transparent Container、Bearers Subject to Data Forwarding
List、S1AP Cause。
（可选）基于QoS profile，源eNodeB为"Bearers Subject to Data Forwarding
List"中的承载发起数据转发消息Forwarding of Data，消息直接发给目标RNC或者发给SGW。
源eNodeB和目标RNC之间的GTP-PDU数据交换是在源eNodeB进行复制，然后通过IP层路由给SGW/目标RNC。 
在目标RNC没有和UE建立RB之前，下行用户面数据到达时，目标RNC可能根据related QoS profile，缓存或者丢弃到达的下行GTP-PDUs。 
源eNodeB通过从E-UTRAN切换命令消息HO from E-UTRAN Command，向UE发送交接给目标接入网的命令。消息中携带transparent
container，是准备阶段目标RNC建立的无线侧的参数。
UE重配置之后向目标RNC发送RRC消息RRC Message，如：Physical Channel Reconfiguration
Complete消息。
目标RNC收到重定位执行触发消息后向new Gn/Gp SGSN发送重定位检测消息Relocation Detect。如果重定位类型为“UE involved”，重定位执行的触发点从Uu接口接收，即：目标RNC在底层探测到UE。Relocation
Detect发送完成后，目标RNC转变为UE的SRNC。
目标RNC收到相应的RRC消息后，如：Physical Channel Reconfiguration Complete，即目标RNC和UE使用无线协议成功交换新的“SRNC-ID
+ S-RNTI”后，目标RNC向new Gn/Gp SGSN发送重定位完成消息Relocation Complete，通知核心网切换完成。
new Gn/Gp SGSN在收到重定位完成消息Relocation Complete后，向old MME发送前转重定位完成消息Forward Relocation Complete，告知其切换完成。
old MME收到消息后，返回前转重定位完成确认消息Forward Relocation Complete Acknowledge。
old MME启动资源保护定时器，用于释放源eNodeB和SGW的资源。 
new Gn/Gp SGSN将用户面切换到目标RNC。new Gn/Gp SGSN向PGW发送更新PDP上下文请求消息Update PDP Context Request，通知下行用户面信息，消息中携带new Gn/Gp SGSN Address、SGSN
Tunnel Endpoint Identifier、QoS Negotiated、serving network identity。
如果建立了Direct Tunnel，SGSN向PGW提供RNC's Address for User Plane and
TEID for Downlink data，并需要包含DTI用于指导PGW应用Direct Tunnel specific error
handling流程。 
PGW更新本地PDP上下文信息并返回更新PDP上下文应答消息Update PDP Context Response，消息中携带PGW Tunnel Endpoint Identifier、UE Info Change Reporting Action。
UE发起RAU流程。new Gn/Gp SGSN确认是Inter-RAT Handover流程之后的RAU流程，只执行RAU流程的子集，也就是说，不执行new
Gn/Gp SGSN和old MME之间的上下文传输流程（context transfer procedures）。在RAU流程中new
Gn/Gp SGSN从HSS得到Subscribed QoS profile。 
当资源保护定时器超时，old MME向SGW发送删除会话请求消息Delete Session Request，请求删除EPS承载资源，消息中携带Cause、Indication。Indication指示SGW不要向PGW发起承载删除流程。
SGW向old MME回复删除会话响应消息Delete Session Response，消息中携带Cause。
old MME通知源eNodeB释放资源。old MME向源eNodeB发送释放资源消息Release Resources。当源eNodeB收到Release Resources消息，不再需要eNodeB转发数据时，源eNodeB释放其资源。
### SGW不变的UTRAN到E-UTRAN的切换流程 
业务模型 :用户通过UTRAN注册到PS网络，正在使用数据业务，移动到LTE覆盖信号强的区域后，UTRAN为了保持用户数据业务的连续性，把用户从UTRAN切换到E-UTRAN。 
MME和SGSN间使用S3接口，且SGW不改变。 
信令流程 :该流程分为准备阶段和执行阶段。 
SGW不变的UTRAN到E-UTRAN的切换流程的准备阶段的流程图如[图1](32%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__04ae77ef-f2de-497e-b593-68983fbf0f42)所示。
图1  SGW不变的UTRAN到E-UTRAN的切换流程-准备阶段
[]images/6227ce7284b746b5865daf10570fa99e.png)
SGW不变的UTRAN到E-UTRAN的切换流程的执行阶段的流程图如[图2](32%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__83954b69-54bd-4b91-a605-46230261d302)所示。
图2  SGW不变的UTRAN到E-UTRAN的切换流程-执行阶段
[]images/24c3d296c74b4a7fbf9d579f2bbf9f54.png)
流程说明 :准备阶段：
源RNC决策发起向E-UTRAN的切换。 
源RNC向源S3/S4 SGSN发送重定位申请消息Relocation Required，触发重定位流程，消息中携带Relocation
Type、Cause、Source ID、Target ID、Source RNC To target eNodeB Transparent
Container。 
源S3/S4 SGSN根据Target ID判断是UTRAN到E-UTRAN的切换，根据Target ID选择目标MME。源S3/S4
SGSN向目标MME发送前转重定位请求消息Forward Relocation Request，触发重定位资源分配流程，消息中携带IMSI、Target
Identification、MM Context、PDN Connections、Source to Target Transparent
Container、RAN Cause。
这条消息包含所有激活的PDN Connections，每一个PDN Connection包含associated
APN、 the address、the uplink tunnel endpoint parameters of the Serving
GW for control plane和a list of EPS Bearer Contexts。 
目标MME收到Forward Relocation Request消息后，创建MM上下文和EPS承载上下文。 
目标MME根据Target ID中的TA，判断SGW不改变。 
目标MME向目标eNodeB发送切换请求消息Handover
Request，请求建立承载，消息包含：Cause、UE Security Capabilities、Security Context、NAS
Security Parameters to E-UTRAN、EPS Bearers to be setup list、Source
to Target Transparent Container、UE-AMBR。
目标eNodeB分配请求的资源，并向目标MME返回切换请求确认消息Handover Request Ackownledge，消息中携带Target to Source Transparent Container、EPS Bearers setup list、EPS
Bearers failed to setup list、Cause。
目标eNodeB和目标MME间的资源分配完成后，目标MME向源S3/S4 SGSN发送前转重定位应答消息Forward
Relocation Response，消息中携带Cause、List of Set Up RABs、RAN Cause。 
这条消息指示目标eNodeB已经准备好接收来自原RNC的转发下行PDU，即relocation resource allocation流程成功完成。 
可选：如果使用了“Indirect Forwarding”，源S3/S4 SGSN向SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、Address(es)
and TEID(s) for Data Forwarding。 
可选：SGW创建数据转发隧道，返回创建间接数据转发隧道应答消息Create Indirect Data Forwarding
Tunnel Response，消息中携带Cause、Serving GW DL TEID(s)。
执行阶段：
源S3/S4 SGSN向源RNC发送重定位命令消息Relocation Command，通知切换准备完成，消息中携带target
eNodeB To Source RNC Transparent Container、RABs To Be Released、RABs
Subject To Data Forwarding。
源RNC向UE发送从UTRAN 切换命令消息HO from UTRAN Command，通知其切换到目标eNodeB。消息中包含一个透传的信元，该信元用于传递eNodeB在准备阶段建立的无线参数。 
源RNC根据“RABs Subject to Data Forwarding List”中指示的RABs或EPS承载上下文开始进行数据转发。数据转发直接给目标eNodeB或者发给SGW。 
在收到包含Relocation Command message的HO from UTRAN Command消息之后，UE基于NSAPI的相关性，将RAB
ID与各个承载ID联系起来，并将上行传输的用户面数据挂起。 
UE切换至E-UTRAN，并执行向目标eNodeB的接入流程。 
UE接入目标eNodeB后，发送切换到E-UTRAN完成消息HO to E-UTRAN Complete。
UE将HO from UTRAN Command中尚未建立E-RAB的EPS承载，在本地将其去激活。 
当UE成功接入目标eNodeB，目标eNodeB将向目标MME发送切换通知消息Handover Notify，消息中携带TAI+ECGI。
目标MME在收到Handover Notify消息后，向源S3/S4 SGSN发送前转重定位完成通知消息Forward Relocation Complete Notification，告知重定位完成。 
源S3/S4
SGSN开启资源保护定时器，监控源RNC和源SGW中的资源释放。 
源S3/S4 SGSN向目标MME返回前转重定位完成响应消息Forward Relocation Complete
Acknowledge。 
为每个PDN连接，目标MME向目标SGW发送修改承载请求消息Modify Bearer Request，通知eNodeB的用户面信息，消息中携带eNodeB
Address(es) and TEID(s) for User Traffic、APN-AMBR、RAT type。如果PGW请求了UE's
location或者User CSG information，信息中也包含这两个信元。
目标SGW向所在PDN连接的PGW发送修改承载请求消息Modify Bearer Request，告知其APN-AMBR和RAT
type变更，消息中携带APN-AMBR、Serving Network。 
PGW向目标SGW返回修改承载应答消息Modify Bearer Response，消息中携带Default
bearer id、APN Restriction。当UE从Gn/Gp S3/S4 SGSN迁移到MME时，PGW向目标SGW发送每一个承载上下文的APN
Restriction。
目标SGW向目标MME返回修改承载应答消息Modify Bearer Response，消息中携带Cause、Default
bearer id、APN restriction。
至此，UE、目标eNodeB、SGW和PGW之间所有承载的用户面路径完成建立。  
UE发起TAU流程。目标MME确认是Inter-RAT Handover流程之后的TAU流程，只执行TAU流程的子集，即不执行目标MME和源S3/S4
SGSN之间的上下文传输流程（context transfer procedures）。 
源S3/S4 SGSN通知源RNC释放资源，执行Iu Release流程，清除到源RNC的所有资源。当不再需要RNC来转发数据时，源RNC响应Iu
Release Complete消息。 
可选：如果使用了“Indirect Forwarding”，目标MME向SGW发送删除间接数据转发隧道请求消息Delete Indirect Data Forwarding Tunnel Request，请求删除数据转发隧道。
可选：SGW删除数据转发隧道，SGW向目标MME返回删除间接数据转发隧道应答消息Delete Indirect
Data Forwarding Tunnel Response。
### SGW改变的UTRAN到E-UTRAN的切换流程 
业务模型 :用户通过UTRAN注册到PS网络，正在使用数据业务，移动到LTE覆盖信号强的区域后，UTRAN为了保持用户数据业务的连续性，把用户从UTRAN切换到E-UTRAN。 
MME和SGSN间使用S3接口，SGW发生改变。 
信令流程 :该流程分为准备阶段和执行阶段。 
SGW改变的UTRAN到E-UTRAN的切换流程的准备阶段的流程图如[图1](33%20SGW%E6%94%B9%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__a88d43a7-3e10-413e-b77c-3ba4792ef810)所示。
图1  SGW改变的UTRAN到E-UTRAN的切换流程-准备阶段
[]images/a5cbbc7297d64b85a3fe618dfe7f35bb.png)
SGW改变的UTRAN到E-UTRAN的切换流程的执行阶段的流程图[图2](33%20SGW%E6%94%B9%E5%8F%98%E7%9A%84UTRAN%E5%88%B0E-UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__1662de75-0f39-42ca-a3e9-66ec995305e4)所示。
图2  SGW改变的UTRAN到E-UTRAN的切换流程-执行阶段
[]images/4ed6e57514534ca9881d063af695bf6f.png)
流程说明 :准备阶段：
源RNC决策发起向E-UTRAN的切换。 
源RNC向源S3/S4 SGSN发送重定位申请消息Relocation Required，触发重定位流程，消息中携带Relocation
Type、Cause、Source ID、Target ID、Source RNC To target eNodeB Transparent
Container。 
源S3/S4 SGSN根据Target ID判断是UTRAN到E-UTRAN的切换，根据Target ID选择目标MME。
源S4 S3/S4 SGSN向目标MME发送前转重定位请求消息Forward Relocation Request，触发重定位资源分配流程，消息中携带IMSI、Target
Identification、MM Context、PDN Connections、Source to Target Transparent
Container、RAN Cause。
这条消息包含所有激活的PDN Connections，每一个PDN Connection包含associated
APN、 the address、the uplink tunnel endpoint parameters of the SGW
for control plane和a list of EPS Bearer Contexts。 
目标MME收到Forward Relocation Request消息后，创建MM上下文和EPS承载上下文。
目标MME根据Target ID中的TA，判断SGW改变，根据Target ID中的TA，选择一个新的SGW，作为目标SGW。 
为每个PDN连接，目标MME向目标SGW发送一个创建会话请求消息Create Session Request，请求SGW创建会话，消息中携带IMSI、MME
Address and TEID、MME Tunnel Endpoint Identifier for Control Plane、MME
Address for Control plane、PGW address(es) for user plane。
目标SGW分配本地资源，向目标MME返回创建会话应答消息Create Session Response，消息中携带SGW
address(es) for user plane、SGW UL TEID(s) for user plane、 SGW Address
for control plane、 SGW TEID for control plane。 
目标MME向目标eNodeB发送切换请求消息Handover Request，请求建立承载，消息中携带Cause、UE
Security Capabilities、Security Context、NAS Security Parameters to
E-UTRAN、EPS Bearers to be setup list、Source to Target Transparent
Container、UE-AMBR。 
目标eNodeB分配请求的资源，并向目标MME返回切换请求确认消息Handover Request Ackownledge，消息中携带Target to Source Transparent Container、EPS Bearers setup list、EPS
Bearers failed to setup list、Cause。
可选：如果使用了“Indirect Forwarding”，目标MME向目标SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、Target
eNB Address and TEID(s) for DL user plane。 
可选：目标SGW创建数据转发隧道，返回给目标MME创建间接数据转发隧道应答消息Create Indirect Data
Forwarding Tunnel Response，消息中携带Cause、SGW DL TEID(s)。
目标eNodeB和目标MME间的资源分配完成后，目标MME向源S3/S4 SGSN发送前转重定位应答消息Forward
Relocation Response，消息中携带Cause、List of Set Up RABs、RAN Cause。 
这条消息指示目标eNodeB已经准备好接收来自原RNC的转发下行PDU，即relocation resource allocation流程成功完成。 
可选：如果使用了“Indirect Forwarding”，源S3/S4 SGSN向源SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、Address(es)
and TEID(s) for Data Forwarding。 
可选：源SGW创建数据转发隧道，返回给源S3/S4 SGSN创建间接数据转发隧道应答消息Create Indirect
Data Forwarding Tunnel Response，消息中携带Cause、SGW DL TEID(s)。
执行阶段：
源S4 S3/S4 SGSN向源RNC发送重定位命令消息Relocation Command，通知其切换准备完成，消息中携带target
eNodeB To Source RNC Transparent Container、RABs To Be Released、RABs
Subject To Data Forwarding。
源RNC向UE发送切换命令消息HO from UTRAN Command，通知其切换到目标eNodeB。消息中包含一个透传的信元，该信元用于传递eNodeB在准备阶段建立的无线参数。
源RNC根据“RABs Subject to Data Forwarding List”中指示的RABs或EPS承载上下文开始进行数据转发。数据转发直接给目标eNodeB或者发给SGW。
在收到包含Relocation Command message的HO from UTRAN Command消息之后，UE基于NSAPI的相关性，将RAB
ID与各个承载ID联系起来，并将上行传输的用户面数据挂起。 
UE切换至E-UTRAN，并执行向目标eNodeB的接入流程。 
UE接入目标eNodeB后，发送切换到E-UTRAN完成消息HO to E-UTRAN Complete。
UE将HO from UTRAN Command中尚未建立E-RAB的EPS承载，在本地将其去激活。 
当UE成功接入目标eNodeB，目标eNodeB将向目标MME发送切换通知消息Handover Notify，消息中携带TAI+ECGI。
目标MME在收到Handover Notify消息后，向源S3/S4 SGSN发送前转重定位完成通知消息Forward Relocation Complete，告知重定位完成。 
源S3/S4 SGSN开启资源保护定时器，监控源RNC和源SGW中的资源释放。 
源S3/S4 SGSN向目标MME返回前转重定位完成响应消息Forward Relocation Complete
Acknowledge。目标MME收到消息后启动一个资源保护定时器。 
为每个PDN连接，目标MME向目标SGW发送修改承载请求消息Modify Bearer Request，通知eNodeB的用户面信息，消息中携带eNodeB
Address(es) and TEID(s) for User Traffic、APN-AMBR、RAT type。如果PGW请求了UE's
location或者User CSG information，信息中也包含这两个信元。
目标SGW向所在PDN连接的PGW发送修改承载请求消息Modify Bearer Request，告知其APN-AMBR和RAT
type变更，消息中携带APN-AMBR、Serving Network。 
PGW向目标SGW返回修改承载应答消息Modify Bearer Response消息，消息中携带Default
bearer id、APN Restriction。当UE从Gn/Gp S3/S4 SGSN迁移到MME时，PGW向目标SGW发送每一个承载上下文的APN
Restriction。
目标SGW向目标MME返回修改承载应答消息Modify Bearer Response消息，消息中携带Cause、Default
bearer id、APN restriction。
至此，UE、目标eNodeB、SGW和PGW之间所有承载的用户面路径完成建立。 
UE发起TAU流程。目标MME确认是Inter-RAT Handover流程之后的TAU流程，只执行TAU流程的子集，即不执行目标MME和源S3/S4
SGSN之间的上下文传输流程（context transfer procedures）。 
源S3/S4 SGSN使用资源保护定时器，源S3/S4 SGSN给源SGW发送删除会话请求消息Delete Session
Request，消息中携带Cause、Indication。Indication指示不需要通知PGW删除会话。
源S3/S4 SGSN通知源RNC释放资源，执行Iu Release流程，清除到源RNC的所有资源。当不再需要RNC来转发数据时，源RNC响应Iu
Release Complete消息。 
源SGW返回给源S3/S4 SGSN删除会话应答消息Delete Session Response。
可选：源S3/S4 SGSN向源SGW发送删除间接数据转发隧道请求消息Delete Indirect Data
Forwarding Tunnel Request，请求删除数据转发隧道。 
可选：源SGW向源S3/S4 SGSN返回删除间接数据转发隧道应答消息Delete Indirect Data
Forwarding Tunnel Response。
可选：目标MME的资源保护定时器超时，目标MME向目标SGW发送删除间接数据转发隧道请求消息Delete Indirect
Data Forwarding Tunnel Request，请求删除数据转发隧道。
可选：目标SGW向目标MME返回删除间接数据转发隧道应答消息Delete Indirect Data Forwarding
Tunnel Response。
### SGW不变的E-UTRAN到UTRAN的切换流程 
业务模型 :用户通过LTE注册到EPS网络，正在使用数据业务，移动到LTE覆盖信号弱但UTRAN覆盖信号强的区域后，E-UTRAN为了保持用户数据业务的连续性，把用户从E-UTRAN切换到UTRAN。 
MME和SGSN间使用S3接口，且SGW不改变。 
信令流程 :该流程分为准备阶段和执行阶段。 
SGW不变的E-UTRAN到UTRAN的切换流程的流程图如[图1](34%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__30738e8c-c04c-4517-97af-3d3793951d6a)所示。
图1  SGW不变的E-UTRAN到UTRAN的切换流程-准备阶段
[]images/e3f400a914334aa08a790ffe84a96d6f.png)
SGW不变的E-UTRAN到UTRAN的切换流程的执行阶段的流程图如[图2](34%20SGW%E4%B8%8D%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__8a3cd154-ebcf-4ebe-a0be-b52e1d2270e8)所示。
图2  SGW不变的E-UTRAN到UTRAN的切换流程-执行阶段
[]images/2825e031aba24008a6aa227855e99e03.png)
流程说明 :准备阶段：
源eNodeB决策发起向UTRAN的切换。此时，上下行用户数据通过如下承载进行传输：Bearer(s) between
UE and source eNodeB、 GTP tunnel(s) between source eNodeB and SGW
、GTP tunnel(s) between SGW and PGW。 
源eNodeB向源MME发送切换申请消息Handover Required，触发切换流程，请求目标RNC、目标S3/S4
SGSN和SGW上建立资源，消息中携带S1 AP Cause、Target RNC Identifier、Source eNodeB
Identifier、Source to Target Transparent Container。 
源MME根据Target ID判断是E-UTRAN到UTRAN的切换，根据Target ID选择目标S3/S4 SGSN。
源MME向目标S3/S4 SGSN发送前转重定位请求消息Forward Relocation Request，触发切换资源分配（Handover
resource allocation）流程，消息中携带IMSI、Target Identification、MM Context、PDN
Connections、Source to Target Transparent Container、RAN Cause。
这条消息包含所有激活的PDN Connections，每一个PDN Connection包含associated APN、the
address、the uplink tunnel endpoint parameters of the SGW for control
plane和a list of EPS Bearer Contexts。 
目标S3/S4 SGSN收到Forward Relocation Request消息后，创建MM上下文和承载上下文。
目标S3/S4 SGSN根据Target ID中的RA，判断SGW不改变。 
目标S3/S4 SGSN向目标RNC发送重定位请求消息Relocation Request，请求建立承载，消息中携带Permanent NAS UE Identity、Cause、Source
RNC To Target RNC Transparent Container、RAB To Be Setup。 
对每一个RAB，RAB
to be Setup应该包含：RAB ID、RAB parameters、Transport Layer Address、Iu Transport
Association等信元。RAB ID信元对应NSAPI的值，RAB parameters信元提供RAB的QoS参数，Transport
Layer Address 为上行用户面地址，Iu Transport Association为上行用户面TEID。如果目标S3/S4
SGSN在RNC和SGW间建立Direct Tunnel，Transport Layer Address则为SGW的用户面地址，Iu
Transport Association为SGW的用户面TEID。 
目标RNC分配请求的资源，并向目标S3/S4 SGSN返回重定位请求确认消息Relocation Request
Ackownledge，消息中携带Target RNC To Source RNC Transparent Container、RABs
Setup、RABs Failed To Setup。
每一个RAB to be setup都由一对Transport
Layer Address、Iu Transport Association组成。Transport Layer Address为RNC用户面地址，Iu
Transport Association为下行用户面TEID。Target RNC To Source RNC Transparent
Container包含UE切换所需的所有无线相关信息。  
目标RNC和目标S3/S4 SGSN间的资源分配过程完成后，目标S3/S4 SGSN向源MME发送前转重定位应答消息Forward Relocation Response，消息中携带Cause、Target to Source Transparent
Container。这条消息指示目标RNC已准备好接收来自源eNodeB的转发下行PDU，即relocation resource
allocation流程成功完成。
可选：如果使用了“Indirect Forwarding”，源MME向SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、MME
Tunnel Endpoint Identifier for Control Plane、MME Address for Control
plane、Target RNC Address and TEID(s) for DL user plane。 
可选：SGW创建数据转发隧道，返回创建间接数据转发隧道应答消息Create Indirect Data Forwarding
Tunnel Response消息，消息中携带Cause、Serving GW DL TEID(s)。
执行阶段：
源MME向源eNodeB发送切换命令消息Handover Command，通知其切换准备完成，消息中携带Target
to Source Transparent Container、Bearers Subject to Data Forwarding
List、S1AP Cause。
源eNodeB通过HO from E-UTRAN Command消息向UE发送交接给目标接入网的命令。消息包含transparent
container，是准备阶段目标RNC建立的无线侧的参数。
UE移动至目标UTRAN网络，发起切换流程。 
UE接入目标RNC后，发送切换到UTRAN完成消息HO to UTRAN Complete。
目标RNC和UE成功交换“RNC-ID + S-RNTI”后，向目标S3/S4 SGSN发送重定位完成消息Relocation Complete，通知其UE已成功接入。
收到Relocation Complete消息后，目标S3/S4 SGSN需要准备好接收目标RNC发送的数据。目标S3/S4 SGSN收到的每一个上行N-PDU被直接转发给SGW。
目标S3/S4 SGSN获知UE已进入目标侧后，向源MME发送前转重定位完成通知消息Forward Relocation
Complete Notification，通知切换完成，消息中携带SGW change。
源MME向目标S3/S4 SGSN返回前转重定位完成响应消息Forward Relocation Complete
Acknowledge。
源MME启动资源保护定时器，用于释放源eNodeB和SGW的资源。 
目标S3/S4 SGSN收到Relocation Complete消息后，目标S3/S4 SGSN将用户面切换到目标RNC。目标S3/S4
SGSN向SGW发送修改承载请求消息Modify Bearer Request，通知下行用户面信息，消息中携带SGSN
Tunnel Endpoint Identifier for Control Plane、NSAPI(s)、SGSN Address
for Control Plane、SGSN Address(es) and TEID(s) for User Traffic for
the accepted EPS bearers (if Direct Tunnel is not used) or RNC Address(es)
and TEID(s) for User Traffic for the accepted EPS bearers (if Direct
Tunnel is used)、RAT type。 
如果PGW请求了UE's location或者User CSG information（由UE上下文决定），S3/S4
SGSN也会在Modify Bearer Request消息中包含UE's location和User CSG information这两个信元。
SGW向所在PDN连接的PGW发送修改承载请求消息Modify Bearer Request，告知PGW信息更新，包括APN-AMBR和RAT
type的变更，消息中携带APN-AMBR、Serving Network。 
PGW更新本地上下文信息。PGW向SGW返回修改承载应答消息Modify Bearer Response，消息中携带Default bearer id、APN Restriction。
SGW向目标S3/S4 SGSN返回修改承载应答消息Modify Bearer Response，消息中携带Cause、Default
bearer id、APN restriction。
至此，UE、目标eNodeB、目标S3/S4 SGSN（如果Direct
Tunnel未使用）、SGW和PGW之间所有承载的用户面路径完成建立。 
UE发起RAU流程。目标S3/S4 SGSN确认是Inter-RAT Handover流程之后的RAU流程，只执行RAU流程的子集，也就是说，不执行目标S3/S4
SGSN和源MME之间的上下文传输流程（context transfer procedures）。在RAU流程中目标S3/S4 SGSN从HSS得到Subscribed
QoS profile。 
当步骤7的定时器超时，源MME给源eNodeB发送释放资源消息Release Resources。源eNodeB释放UE相关的资源。
可选：源MME向SGW发送删除间接数据转发隧道请求消息Delete Indirect Data Forwarding
Tunnel Request，请求删除数据转发隧道。 
可选：SGW删除数据转发隧道，SGW向源MME返回删除间接数据转发隧道应答消息Delete Indirect Data
Forwarding Tunnel Response。
### SGW改变的E-UTRAN到UTRAN的切换流程 
业务模型 :用户通过LTE注册到EPS网络，正在使用数据业务，移动到LTE覆盖信号弱但UTRAN覆盖信号强的区域后，E-UTRAN为了保持用户数据业务的连续性，把用户从E-UTRAN切换到UTRAN。 
MME和SGSN间使用S3接口，且SGW发送改变。 
信令流程 :该流程分为准备阶段和执行阶段。 
SGW改变的E-UTRAN到UTRAN的切换流程的准备阶段的流程图如[35%20SGW改变的E-UTRAN到UTRAN的切换流程.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__SGW改变的E-UTRAN到UTRAN的切换流程-准备阶段-54374ED5](35%20SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B-%E5%87%86%E5%A4%87%E9%98%B6%E6%AE%B5-54374ED5)所示。
图1  SGW改变的E-UTRAN到UTRAN的切换流程-准备阶段
[]images/0456a34e5c284c7bb010645d52c0f356.png)
SGW改变的E-UTRAN到UTRAN的切换流程的执行阶段的流程图如[图2](35%20SGW%E6%94%B9%E5%8F%98%E7%9A%84E-UTRAN%E5%88%B0UTRAN%E7%9A%84%E5%88%87%E6%8D%A2%E6%B5%81%E7%A8%8B.html#HandoverFromUTRANIuModeToE-UTRANByS-4E2C635C__02a81026-da8c-4e34-a64a-a3c501f69ea2)所示。
图2  SGW改变的E-UTRAN到UTRAN的切换流程-执行阶段
[]images/3efc24bcfb7d4144a75e6a5a4c428014.png)
流程说明 :准备阶段：
源eNodeB决策发起向UTRAN的切换。此时，上下行用户数据通过如下承载进行传输：Bearer(s) between
UE and source eNodeB、 GTP tunnel(s) between source eNodeB and S-GW
、GTP tunnel(s) between SGW and PGW。 
源eNodeB向源MME发送切换申请消息Handover Required，触发切换流程，消息中携带S1
AP Cause、Target RNC Identifier、Source eNodeB Identifier、Source to
Target Transparent Container。
源MME根据Target ID判断是E-UTRAN到UTRAN的切换，根据Target ID选择目标S3/S4 SGSN。源MME向目标S3/S4
SGSN发送前转重定位请求消息Forward Relocation Request消息，触发切换资源分配（Handover
resource allocation）流程，消息中携带IMSI、Target Identification、MM Context、PDN
Connections、Source to Target Transparent Container、RAN Cause。
这条消息包含所有激活的PDN Connections，每一个PDN Connection包含associated APN、the
address、the uplink tunnel endpoint parameters of the SGW for control
plane和a list of EPS Bearer Contexts。 
目标S3/S4 SGSN收到Forward Relocation Request消息后，创建MM上下文和承载上下文。
目标S3/S4 SGSN根据Target ID中的RA，判断SGW改变，根据RA，选择一个新的SGW，作为目标SGW。 
为每个PDN连接，目标S3/S4 SGSN向目标SGW发送一个创建会话请求消息Create Session Request，请求SGW创建会话，消息中携带bearer context(s) with PGW addresses and TEIDs for
uplink traffic、APN-AMBR、Serving Network。
目标SGW分配本地资源，向目标S3/S4 SGSN返回创建会话应答消息Create Session Response，消息中携带SGW address(es) for user plane、SGW UL TEID(s) for user plane、
SGW Address for control plane、 SGW TEID for control plane。 
目标S3/S4 SGSN向目标RNC发送重定位请求消息Relocation Request，请求建立承载，消息中携带Permanent
NAS UE Identity、Cause、Source RNC To Target RNC Transparent Container、RAB
To Be Setup。 
对每一个RAB，RAB to be Setup应该包含：RAB ID、RAB parameters、Transport
Layer Address、Iu Transport Association等信元。RAB ID信元对应NSAPI的值，RAB parameter信元提供RAB的QoS参数，Transport
Layer Address 为上行用户面地址，Iu Transport Association为上行用户面TEID。如果目标S3/S4
SGSN在RNC和SGW间建立Direct Tunnel，Transport Layer Address则为SGW的用户面地址，Iu
Transport Association为SGW的用户面TEID。 
目标RNC分配请求的资源，并向目标S3/S4 SGSN返回重定位请求确认消息Relocation Request
Ackownledge，消息中携带Target RNC To Source RNC Transparent Container、RABs
Setup、RABs Failed To Setup。
每一个RAB to be setup都由一对Transport
Layer Address、Iu Transport Association组成。Transport Layer Address是RNC用户面地址，Iu
Transport Association为下行用户面TEID。Target RNC To Source RNC Transparent
Container包含UE切换所需的所有无线相关信息。  
可选：如果使用了“Indirect Forwarding”，目标S3/S4 SGSN向目标SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带Target
RNC Address and TEID(s) for DL data forwarding。 
可选：目标SGW创建数据转发隧道，返回给目标S3/S4 SGSN创建间接数据转发隧道应答消息Create Indirect
Data Forwarding Tunnel Response，消息中携带Cause、SGW DL TEID(s)。
目标RNC和目标S3/S4 SGSN间的资源分配过程完成后，目标S3/S4 SGSN向源MME发送前转重定位应答消息Forward Relocation Response，消息中携带Cause、Target to Source Transparent
Container。这条消息指示目标RNC已准备好接收来自原eNodeB的转发下行PDU，即relocation resource
allocation流程成功完成。
可选：如果使用了“Indirect Forwarding”，源MME向源SGW发送创建间接数据转发隧道请求消息Create Indirect Data Forwarding Tunnel Request，请求创建数据转发隧道，消息中携带IMSI、MME
Tunnel Endpoint Identifier for Control Plane、MME Address for Control
plane、Target RNC Address and TEID(s) for DL user plane。 
可选：源SGW创建数据转发隧道，返回给源MME创建间接数据转发隧道应答消息Create Indirect Data
Forwarding Tunnel Response，消息中携带Cause、SGW DL TEID(s)。
执行阶段：
源MME向源eNodeB发送切换命令消息Handover Command，通知其切换准备完成，消息中携带Target
to Source Transparent Container、Bearers Subject to Data Forwarding
List、S1AP Cause。
源eNodeB通过HO from E-UTRAN Command消息向UE发送交接给目标接入网的命令。消息中携带的transparent
container是准备阶段目标RNC建立的无线侧的参数。
UE移动至目标UTRAN，发起切换流程。 
UE接入目标RNC后，发送切换到UTRAN完成消息HO to UTRAN Complete。
目标RNC和UE成功交换“RNC-ID + S-RNTI”后，向目标S3/S4 SGSN发送重定位完成消息Relocation Complete，通知其UE已成功接入。
收到Relocation Complete消息后，目标S3/S4 SGSN需要准备好接收目标RNC发送的数据。目标S3/S4 SGSN收到的每一个上行N-PDU被直接转发给SGW。
目标S3/S4 SGSN获知UE已进入目标侧后，向源MME发送前转重定位完成通知消息Forward Relocation
Complete Notification，通知切换完成。如果非直接数据前转隧道被创建，目标S3/S4 SGSN启动资源保护定时器。
源MME向目标S3/S4 SGSN返回前转重定位完成响应消息Forward Relocation Complete
Acknowledge。
源MME启动资源保护定时器，用于释放源eNodeB和SGW的资源。 
目标S3/S4 SGSN将用户面切换到目标RNC。目标S3/S4 SGSN向目标SGW发送修改承载请求消息Modify
Bearer Request，通知下行用户面信息，消息中携带SGSN Tunnel Endpoint Identifier
for Control Plane、NSAPI(s)、SGSN Address for Control Plane、SGSN Address(es)
and TEID(s) for User Traffic for the accepted EPS bearers (if Direct
Tunnel is not used) or RNC Address(es) and TEID(s) for User Traffic
for the accepted EPS bearers (if Direct Tunnel is used)、RAT type。 
如果PGW请求了UE's location或者User CSG information（由UE上下文决定），SGSN也会在Modify Bearer Request信息中包含UE's location和User CSG information这两个信元。
目标SGW向所在PDN连接的PGW发送修改承载请求消息Modify Bearer Request，告知PGW信息更新，包括APN-AMBR和RAT
type变更，消息中携带APN-AMBR、Serving Network。 
PGW向目标SGW返回修改承载应答消息Modify Bearer Response，消息中携带Default
bearer id、APN Restriction。当UE从Gn/Gp SGSN迁移到MME时，PGW向目标SGW发送每一个承载上下文的APN
Restriction。
目标SGW向目标S3/S4 SGSN返回修改承载应答消息Modify Bearer Response，消息中携带Cause、Default
bearer id、APN restriction。
至此，UE、目标eNodeB、目标S3/S4 SGSN（如果Direct
Tunnel未使用）、目标SGW和PGW之间所有承载的用户面路径完成建立。 
UE发起RAU流程。目标S3/S4 SGSN确认是Inter-RAT Handover流程之后的RAU流程，只执行RAU流程的子集，也就是说，不执行目标S3/S4
SGSN和源MME之间的上下文传输流程（context transfer procedures）。在RAU流程中目标S3/S4 SGSN从HSS得到Subscribed
QoS profile。 
当源MME资源保护定时器超时，源MME向源SGW发送删除会话请求消息Delete Session Request，消息中携带Cause、Indication。Indication指示不需要通知PGW删除会话。
当源MME资源保护定时器超时，源MME给源eNodeB发送释放资源消息Release Resources。源MME通知源eNodeB释放资源，源eNodeB释放UE相关的资源。
源SGW向源MME返回删除会话应答消息Delete Session Response。
可选：源MME向源SGW发送删除间接数据转发隧道请求消息Delete Indirect Data Forwarding
Tunnel Request，请求删除数据转发隧道。 
可选：源SGW向源MME返回删除间接数据转发隧道应答消息Delete Indirect Data Forwarding
Tunnel Response。
可选：目标S3/S4 SGSN的资源保护定时器超时，目标S3/S4 SGSN向目标SGW发送删除间接数据转发隧道请求消息Delete Indirect Data Forwarding Tunnel Request，请求删除数据转发隧道。
可选：目标SGW向目标S3/S4 SGSN返回删除间接数据转发隧道应答消息Delete Indirect Data
Forwarding Tunnel Response。
## 会话管理 
### UE请求PDN连接 
### UE请求PDN连接 


业务模型 :EPS支持UE发起的PDN连接建立，允许UE通过多PDN连接接入一个或多个PDN网络。UE发起的PDN连接流程是指当UE注册到EPS网络上后，UE可以同时激活到不同PGW或相同PGW的多个PDN连接过程。 
PDN连接建立的流程与Attach过程中的默认承载建立过程类似，MME为UE选择接入的PGW，建立UE到PGW的PDN连接。多PDN连接流程完成之后，用户可以通过EPS网络申请多个IP地址，建立到不同PGW或相同PGW的多个PDN连接，访问数据业务和其他业务，当UE不再需要通过这个PDN连接访问数据业务和其他业务时，也可以通过去激活PDN连接，释放已申请的IP地址。 


信令流程 :UE请求PDN连接的流程如[图1](36%20UE%E8%AF%B7%E6%B1%82PDN%E8%BF%9E%E6%8E%A5.html#concept1__UE%E8%AF%B7%E6%B1%82PDN%E8%BF%9E%E6%8E%A5-291B2885)所示。
图1  UE请求PDN连接


[]images/UE%E8%AF%B7%E6%B1%82PDN%E8%BF%9E%E6%8E%A5.png)



流程说明 :

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




### 专有承载激活 
### 专有承载激活 


业务模型 :专有承载建立流程是指当UE注册到EPS网络后，如果已建立的默认承载或其他专有承载不能满足其的业务需求，则由网络侧触发建立专有承载。 
在由网络侧触发专有承载建立过程中，MME为承载分配EPS承载标识，通知eNodeB，UE建立专有承载，并通知SGW专有承载建立响应，配合完成eNodeB和SGW的用户面隧道建立。专有承载建立完成之后，UE可以通过EPS网络建立的专有承载访问数据业务和其他业务。 


信令流程 :专有承载激活流程如[图1](37%20%E4%B8%93%E6%9C%89%E6%89%BF%E8%BD%BD%E6%BF%80%E6%B4%BB.html#concept1__%E4%B8%93%E6%9C%89%E6%89%BF%E8%BD%BD%E6%BF%80%E6%B4%BB%E6%B5%81%E7%A8%8B-291C3461)所示。
图1  专有承载激活流程


[]images/%E4%B8%93%E6%9C%89%E6%89%BF%E8%BD%BD%E6%BF%80%E6%B4%BB.png)



流程说明 :

（可选）如果分组核心网部署了动态PCC，当UE访问需要QoS保障的业务时，PCRF会向PGW发送RAR消息，触发专有承载建立。 
如果分组核心网未部署动态PCC，则当PGW检测到需要进行QoS保障的业务时，应用本地配置的QoS策略，触发专有承载建立。 


（可选）如果此流程由PCRF触发，则PGW向PCRF回送RAA消息。 


PGW向SGW发送Create Bearer Request消息，此消息中携带IMSI、TEID-U、Charging
Id、PTI、TFT、S5/S8 TEID、EPS Bearer QoS等信息。 
LBI（Linked EPS Bearer
Identity）是UE的缺省承载ID，TEID-U是专有承载PGW侧的用户面隧道标识 。 


SGW为此专有承载建立上下文，保持相关参数，向MME发送Create Bearer Request消息。 


MME选择一个此用户还没有使用过的EPS Bearer ID，向eNodeB发送Bearer Setup Request消息，消息包含：EPS
Bearer Identity、EPS Bearer QoS、Session Management Request、S1-TEID。Session
Management Request是MME构造的会话管理消息，消息中包括了EPS承载的QoS（但是不包含ARP）、TFT、PCO、EPS
Bearer ID、LBI。 


eNodeB将EPS承载的QoS参数映射为无线承载的QoS参数。然后eNodeB发送RRC Connection Reconfiguration消息给UE，消息包含：Radio
Bearer QoS、Session Management Request（Activate dedicated EPS bearer
context Request）、EPS RB Identity。 


UE返回RRC Connection Reconfiguration Complete消息给eNodeB，确认无线承载已激活。 


eNodeB向MME发送Bearer Setup Response消息，确认空口承载已激活，消息包含：EPS Bearer
Identity、S1-TEID。 


UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Session Management
Response消息，其中包含EPS Bearer Identity。 


eNodeB发送Session Management Response（会话管理）消息给MME。 


当MME收到了第8步中eNodeB发送的Bearer Setup Response消息和第10步的从UE发送的Session
Management Response消息后，MME给SGW发送Create Bearer Response消息确认承载激活，消息包含EPS
Bearer Identity、S1-TEID。 


SGW向PGW发送Create Bearer Response消息，告知PGW专有承载建立成功。 




### PGW发起承载修改，QoS更新 
### PGW发起承载修改，QoS更新 


业务模型 :在PGW触发的承载修改过程中，因承载的QoS（如QCI、GBR、MBR或ARP）、APN-AMBR的修改，MME需要通知eNodeB、UE这些相关信息的修改，并通知SGW承载修改响应。 
被修改的承载可以是默认承载或专有承载，承载修改完成之后，UE可以通过EPS网络修改之后的承载访问数据业务和其他业务。该流程不支持QCI资源类型的修改，即不支持GBR承载和Non-GBR承载的相互转化。 


信令流程 :PGW发起承载修改，QoS更新，流程如[图1](38%20PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9%EF%BC%8CQoS%E6%9B%B4%E6%96%B0.html#concept1__PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9QoS%E6%9B%B4%E6%96%B0-291D1631)所示。
图1  PGW发起承载修改，QoS更新

[]images/PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9%EF%BC%8CQoS%E6%9B%B4%E6%96%B0.png)


流程说明 :

（可选）如果部署了动态PCC，当UE所访问业务的QoS保障发生变化时，PCRF向PGW发送RAR消息，触发承载更新。 
如果未部署动态PCC，则当PGW检测到QoS保障有变化时，触发承载更新。 


（可选）如果此流程由PCRF触发，则PGW向PCRF响应RAA消息。  


PGW向SGW发送Update Bearer Request消息，该消息中携带EPS Bearer QoS等信息。 


SGW更新承载上下文，向MME发送Update Bearer Request消息。 


如果UE处于空闲态（Idle），MME触发网络侧触发的业务请求流程；如果UE处于连接态，MME向eNodeB发送Bearer
Modify Request消息，消息中可能包括了EPS承载的QoS（但是不包含ARP）、APN-AMBR（如果APN-AMBR改变了，MME会重新计算UE-AMBR）、TFT和EPS
Bearer Identity和Session Management Request。其中Session Management Request是MME构造的消息。 


eNodeB将修改过的EPS bearer QoS映射为Radio Bearer QoS，然后向UE发送RRC Connection
Reconfiguration消息，消息包含：Radio Bearer QoS、Session Management Request、EPS
RB Identity。 


UE向eNodeB响应RRC Connection Reconfiguration Complete消息，确认无线承载修改。 


eNodeB向MME响应Bearer Modify Response消息指示请求的EPS Bearer QoS能否被分配，消息包含：EPS
Bearer Identity。 


UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Session Management
Response消息，消息包含：EPS Bearer Identity。 


eNodeB向MME发送会话管理响应消息Session Management Response（包含Modify EPS
bearer context accept）消息。 


MME在收到了第8步的从eNodeB发送Bearer Modify Response消息和第10步的从UE发送的会话管理响应消息Session
Management Response后，MME给SGW发送Update Bearer Response消息确认承载更新，消息中包含EPS
Bearer Identity。 


SGW向PGW发送Update Bearer Response消息，告知PGW承载更新成功，消息包含：EPS Bearer
Identity。 




### PGW发起承载修改，QoS未更新 
### PGW发起承载修改，QoS未更新 


业务模型 :PGW发起的QoS未更新的承载修改流程用于更新激活默认或专有承载的TFT，或修改APN-AMBR，或从MME获取用户位置信息，或将PCO信息通知给UE，或指示MME激活或去活位置报告。 


信令流程 :PGW发起承载修改，QoS未更新，流程如[图1](39%20PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9%EF%BC%8CQoS%E6%9C%AA%E6%9B%B4%E6%96%B0.html#concept1__PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9QoS%E6%9C%AA%E6%9B%B4%E6%96%B0-291FBE64)所示。
图1  PGW发起承载修改，QoS未更新

[]images/PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9%EF%BC%8CQoS%E6%9C%AA%E6%9B%B4%E6%96%B0.png)


流程说明 :

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


S-GW向P-GW响应Update Bearer Response消息确认承载修改，消息包含：EPS Bearer Identity。 




### HSS发起承载修改，QoS更新 
### HSS发起承载修改，QoS更新 


业务模型 :HSS触发的承载修改过程中，因承载的QoS（如QCI、GBR、MBR或ARP）、APN-AMBR的修改，MME需要通知eNodeB、UE这些相关信息的修改，并通知SGW承载修改响应。 
被修改的承载可以是默认承载或专有承载，承载修改完成之后，UE可以通过EPS网络修改之后的承载访问数据业务和其他业务。该流程不支持QCI资源类型的修改，即不支持GBR承载和Non-GBR承载的相互转化。 


信令流程 :HSS发起承载修改，QoS更新，流程如[图1](40%20HSS%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9%EF%BC%8CQoS%E6%9B%B4%E6%96%B0.html#concept1__HSS%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9QoS%E6%9B%B4%E6%96%B0-291DEB15)所示。
图1  HSS发起承载修改，QoS更新


[]images/HSS%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9%EF%BC%8CQoS%E6%9B%B4%E6%96%B0.png)



流程说明 :

HSS发送Insert Subscriber Data消息给MME，消息中携带用户的IMSI号码和用户签约数据。用户签约数据中包含EPS签约的QoS（QCI和ARP）、签约的APN-AMBR和签约的UE-AMBR。 


MME更新存储的用户签约数据，给HSS返回Insert Subscriber Data Ack消息。 


如果仅签约的UE-AMBR发生改变，MME重新计算新的UE-AMBR；如果新的UE-AMBR发生改变，MME使用S1-AP
UE上下文修改流程完成UE-AMBR的更新。如果仅有签约的UE-AMBR发生改变，HSS发起签约QoS修改流程在UE上下文修改流程完成后结束；如果签约的QCI、APR和APN-AMBR中有发生改变的参数，并且对应的有激活的PDN连接，MME发送Modify
Bearer Command消息给SGW。 


SGW向PGW发送Modify Bearer Command消息，携带EPS Bearer Identity、APN
AMBR 、EPS Bearer QoS等信息。 


（可选）如果启用了动态PCC，PGW向PCRF发送CCR-U消息，触发IP-CAN修改流程，携带更新后的EPS Bearer
QoS。 


（可选）PCRF给PGW回送CCA-U消息，携带更新后的PCC策略等信息。 


PGW向SGW发送Update Bearer Response消息，携带变化的TFT、EPS Bearer QOS、APN-AMBR等信息。 


SGW存储变化的参数，向MME发送Update Bearer Response消息，携带变化的TFT、EPS Bearer
QOS、APN-AMBR等信息。 


如果UE处于空闲态，MME触发网络侧触发的业务请求流程；如果UE处于连接态，MME向eNodeB发送Bearer Modify
Request消息，消息中可能包括了EPS承载的QoS（但是不包含ARP）、APN-AMBR（如果APN-AMBR改变了，MME会重新计算UE-AMBR）、TFT和EPS
Bearer Identity和Session Management Request，其中Session Management Request是MME构造的消息。 


eNodeB将修改过的EPS bearer QoS映射为Radio Bearer QoS，然后向UE发送RRC Connection
Reconfiguration消息，消息包含：Radio Bearer QoS、Session Management Request、EPS
RB Identity。 


UE向eNodeB响应RRC Connection Reconfiguration Complete消息，确认无线承载修改。 


eNodeB向MME响应Bearer Modify Response消息指示，请求的EPS Bearer QoS能否被分配，消息中包含EPS
Bearer Identity。 


UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Session Management
Response消息，消息包含：EPS Bearer Identity。 


eNodeB向MME发送会话管理响应消息Session Management Response（Modify EPS
bearer context accept）。 


eNodeB向MME发送会话管理响应消息Session Management Response（Modify EPS
bearer context accept）。 


SGW向PGW发送Update Bearer Response消息，告知PGW承载更新成功，消息包含：EPS Bearer
Identity。 




### MME发起承载去激活 
### MME发起承载去激活 


业务模型 :MME发起的承载去激活只用于去激活专有承载，如果是释放PDN连接，包括默认承载，则发起PDN去连接过程。 


信令流程 :MME发起承载去激活的流程如[图1](41%20MME%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E5%8E%BB%E6%BF%80%E6%B4%BB.html#concept1__MME%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E5%8E%BB%E6%BF%80%E6%B4%BB%E6%B5%81%E7%A8%8B-2923FCED)所示。
图1  MME发起承载去激活流程


[]images/MME%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E5%8E%BB%E6%BF%80%E6%B4%BB.png)



流程说明 :

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




### PGW发起承载去激活 
### PGW发起承载去激活 


业务模型 :PGW可以去激活某一个PDN地址的一个专有承载或所有承载。如果是要去激活默认承载，则去激活该PDN连接的所有承载。 


信令流程 :PGW发起承载去激活的流程如[图1](42%20PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E5%8E%BB%E6%BF%80%E6%B4%BB.html#concept1__PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E5%8E%BB%E6%BF%80%E6%B4%BB-292561AD)所示。
图1  PGW发起承载去激活


[]images/PGW%E5%8F%91%E8%B5%B7%E6%89%BF%E8%BD%BD%E5%8E%BB%E6%BF%80%E6%B4%BB.png)



流程说明 :

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




## 安全管理 
### 鉴权集获取 
### 鉴权集获取 


业务模型 :MME向HSS请求获取一组或多组鉴权向量（RAND，AUTN，XRES，KASME）用于用户鉴权过程。每一组EPS鉴权向量均能用于用户鉴权。 


信令流程 :鉴权集获取信令流程如[图1](43%20%E9%89%B4%E6%9D%83%E9%9B%86%E8%8E%B7%E5%8F%96.html#concept1__%E9%89%B4%E6%9D%83%E9%9B%86%E8%8E%B7%E5%8F%96%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-4F9DD625)所示、
图1  鉴权集获取信令流程


[]images/43-%E9%89%B4%E6%9D%83%E9%9B%86%E8%8E%B7%E5%8F%96.png)



流程说明 :

MME向HSS发送Authentication Information Request消息请求获取用户鉴权向量。 


HSS向MME响应Authentication Information Answer消息返回鉴权向量。 




### 鉴权 
### 鉴权 


业务模型 :EPS AKA（Authentication and Key Agreement）是E-UTRAN网络使用的鉴权和密钥协商流程。EPS
AKA将为UP（User Plane）、RRC（Radio Resource Control）、NAS（Non-Access-Stratum）加密密钥及RRC和NAS完整性保护密钥提供基础的密钥信息。 


信令流程 :鉴权信令流程如[图1](44%20%E9%89%B4%E6%9D%83.html#concept1__%E9%89%B4%E6%9D%83%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-54BEF728)所示、
图1  鉴权信令流程


[]images/44-%E9%89%B4%E6%9D%83.png)



流程说明 :

MME向UE发送Authentication Request消息。 


UE向MME响应Authentication Response消息。 




### 鉴权失败 
### 鉴权失败 


业务模型 :用户鉴权过程中，用户对网络鉴权或网络对用户鉴权失败。 


信令流程 :鉴权失败流程如[图1](45%20%E9%89%B4%E6%9D%83%E5%A4%B1%E8%B4%A5.html#concept1__%E9%89%B4%E6%9D%83%E5%A4%B1%E8%B4%A5-54C405D5)所示、
图1  鉴权失败


[]images/45-%E9%89%B4%E6%9D%83%E5%A4%B1%E8%B4%A5.png)



流程说明 :

MME向UE发送Authentication Request消息。 


UE根据AUTN对网络进行鉴权，如果鉴权失败，UE向MME响应Authentication Failure消息。 


可选：MME收到UE的Authentication Response消息，根据UE返回的RES及鉴权向量中的XRES进行鉴权。鉴权失败，MME向UE发送Authentication
Reject消息。 




### 显式GUTI重分配 
### 显式GUTI重分配 


业务模型 :UE和MME间的信令连接建立后，MME可以随时发起GUTI（Globally
Unique Temporary UE Identity）重分配流程，为UE重分配一个新的GUTI和/或TAI列表。GUTI和/或TAI列表可以在附着或TAU流程中进行重分配。 


信令流程 :显式GUTI重分配流程如[图1](46%20%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D.html#concept1__%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D-54CC2C2C)所示、
图1  显式GUTI重分配


[]images/46-%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D.png)



流程说明 :

MME向UE发送GUTI Reallocation Command消息，消息包含：GUTI、TAI list。 


UE向MME响应GUTI Reallocation Complete消息。 




### 身份识别流程 
### 身份识别流程 


业务模型 :当用户使用临时身份标识GUTI鉴权失败时，网络侧将发起用户的身份识别流程。当网络侧无法根据GUTI重新获取IMSI用于用户鉴权时，也将使用本流程。 


信令流程 :身份识别流程如[图1](47%20%E8%BA%AB%E4%BB%BD%E8%AF%86%E5%88%AB%E6%B5%81%E7%A8%8B.html#concept1__%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D-54CC2C2C)所示、
图1  身份识别流程


[]images/47-%20Identification%E6%B5%81%E7%A8%8B.png)



流程说明 :

MME向UE发送Identity Request消息，请求进行身份识别。  


UE向MME响应Identity Response消息，消息包含：IMSI。 




### 加密 
### 加密 


业务模型 :MME支持UE终端NAS信令的加密，MME在接收NAS信令时进行解密，下发NAS信令时进行加密，MME在用户接入完成鉴权后，将使用的秘钥序号与加密/解密算法下发给UE终端。 


信令流程 :加密流程如[图1](48%20%E5%8A%A0%E5%AF%86.html#concept1__%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D-54CC2C2C)所示、
图1  加密


[]images/48-%E5%8A%A0%E5%AF%86%E6%B5%81%E7%A8%8B.png)



流程说明 :

MME向UE发送Security Mode Command消息，消息包含：Selected NAS algorithms、eKSI、UE
Security Capability。当NAS SMC与IMEI检查同时进行时，消息还可以携带IMEISV request。 


UE向MME响应Security Mode Complete消息，如MME在Security mode command消息请求了用户IMEISV，则消息包含IMEISV。 




### 数据完整性 
### 数据完整性 


业务模型 :MME支持UE终端NAS信令的完整性保护，MME在接收NAS信令时进行完整性保护检查，下发NAS信令时生成并携带完整性保护头，MME在用户接入完成鉴权后，将使用的秘钥序号与完整性保护算法下发给UE终端。 


信令流程 :数据完整性流程如[图1](49%20%E6%95%B0%E6%8D%AE%E5%AE%8C%E6%95%B4%E6%80%A7.html#concept1__%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D-54CC2C2C)所示、
图1  数据完整性


[]images/49-%E6%95%B0%E6%8D%AE%E5%AE%8C%E6%95%B4%E6%80%A7%E6%B5%81%E7%A8%8B.png)



流程说明 :

MME根据UE支持算法（即UE的安全能力）和MME自身配置的支持的算法进行算法协商。 


MME向UE发送NAS Security Mode Command消息告知网络侧选择的算法及秘钥序号。消息包含：replayed
UE security capabilities、selected NAS algorithms、eKSI for identifying
KASME，在需要创建一个Idle态的映射上下文时还会携带NONCEUE和NONCEMME。


UE对Security Mode Command消息进行完整性检查。 包括，确保MME发送的UE安全能力与UE本地保存的安全能力一致，以保证其未被攻击者篡改过，同时使用基于eKSI指示的KASME的NAS完整性算法和NAS完整性密钥进行完整性保护检查。如果检查通过，UE将使用此安全上下文开始NAS完整性保护以及加密/解密，并向MME发送NAS
Security Mode Complete消息。 


UE向MME响应NAS Security mode complete消息，消息包含：NAS-MAC，同时如MME在Security
mode command消息请求了用户IMEISV，则消息包含IMEISV。 


MME使用NAS Security Mode Command消息中的密钥和算法对NAS Security Mode Complete消息进行解密和检查。MME在收到NAS
Security Mode Complete消息后使用该安全上下文对NAS下行数据进行加密。MME在收到NAS Security Mode
Command消息后使用该安全上下文对NAS上行数据进行解密。 




### IMEI检查 
### IMEI检查 


业务模型 :用户接入MME时，MME通过EIR设备可以检查用户终端IMEI是否合法，当IMEI非法时，MME将拒绝为用户提供业务。 


信令流程 :IMEI检查流程如[图1](50%20IMEI%E6%A3%80%E6%9F%A5.html#concept1__%E6%98%BE%E5%BC%8FGUTI%E9%87%8D%E5%88%86%E9%85%8D-54CC2C2C)所示。
图1  IMEI检查


[]images/50-IMEI%E6%A3%80%E6%9F%A5%E6%B5%81%E7%A8%8B.png)



流程说明 :

MME向UE发送Identity Request消息，消息中Identity Type指示请求IMEISV。  


UE向MME响应Identity Response消息携带IMEISV。  


如果MME配置了到EIR进行IMEI验证，则向EIR发送ME Identity Check Request消息，消息包含：IMEISV、IMSI。  


EIR向MME响应ME Identity Check Request消息，携带IMEISV验证结果。 




## 签约数据管理 
### HSS修改签约数据，导致MME请求PDN断开 
### HSS修改签约数据，导致MME请求PDN断开 


业务模型 :MME允许UE请求断开与某个PDN的连接，在这个过程中，MME通知SGW、PGW、无线侧和UE删除PDN连接，包括缺省承载在内的全部承载都将被释放，已申请的IP地址也被释放。


信令流程 :HSS修改签约数据，导致MME请求PDN断开的流程如[图1](51%20HSS%E4%BF%AE%E6%94%B9%E7%AD%BE%E7%BA%A6%E6%95%B0%E6%8D%AE%EF%BC%8C%E5%AF%BC%E8%87%B4MME%E8%AF%B7%E6%B1%82PDN%E6%96%AD%E5%BC%80.html#concept1__HSS%E4%BF%AE%E6%94%B9%E7%AD%BE%E7%BA%A6%E6%95%B0%E6%8D%AE%E5%AF%BC%E8%87%B4MME%E8%AF%B7%E6%B1%82PDN%E6%96%AD%E5%BC%80-4FA56128)所示。
图1  HSS修改签约数据，导致MME请求PDN断开


[]images/51%20HSS%E4%BF%AE%E6%94%B9%E7%AD%BE%E7%BA%A6%E6%95%B0%E6%8D%AE%EF%BC%8C%E5%AF%BC%E8%87%B4MME%E8%AF%B7%E6%B1%82PDN%E6%96%AD%E5%BC%80.png)



流程说明 :

由于HSS侧的用户签约信息被修改，MME识别到用户签约信息发生了改变，决定释放PDN连接。MME向指定PDN连接的SGW发送Delete
Session Request（删除会话请求）消息，请求删除SGW上的EPS承载，该消息包含：Cause（原因值）、LBI。 
该消息指示SGW全部释放该PDN连接相关的所有EPS承载。 

 
如果PGW需要根据UE的PDN上下文来请求UE的位置信息，MME将在本消息中携带User Location Information信元。 

 
如果UE所在的时区发生改变，MME将在本消息中携带UE Time Zone信元。 

 


SGW收到MME发送的Delete Session Request消息后，释放相关用户的承载信息，并按每个PDN连接分别向PGW发送Delete
Session Request（删除会话请求）消息。 
如果步骤1中MME向SGW发送的Delete Session Request消息中携带了User
Location Information信元，SGW也需要在本条消息中携带User Location Information信元。 


PGW释放相关承载资源，并向SGW发送Delete Session Response（删除会话响应）消息。 


（可选）如果分组核心网中部署了PCRF（开启PCC功能），PGW将发起IP CAN会话终止流程，通知PCRF，用户的EPS承载已被释放，指示PCRF释放相关资源。 


PGW向PCRF发送CCR-U消息，通知PCRF终止IP CAN会话。 


PCRF识别并删除用户关联的PCC Rules，并向PGW返回CCA-U消息，PGW删除已终止IP CAN会话的相关信息。 




SGW向MME发送Delete Session Response（删除会话响应）消息。 


MME向eNodeB发送Deactivate Bearer Request消息，去激活指定PDN连接的全部EPS承载。 
MME重新计算UE-AMBR，该S1-AP消息携带待删除EPS承载列表、新的UE-AMBR、以及NAS层的Deactivate
EPS bearer context request消息，消息包含：LBI。 


eNodeB向UE发送RRC Connection Reconfiguration（RRC连接注册）消息，通知UE释放对应的无线承载资源，其中包含要释放的承载和NAS层的Deactivate
EPS Bearer Context Request消息。 


UE释放对应的无线承载资源，并向eNodeB发送RRC Connection Reconfiguration Complete（RRC连接注册完成）消息，确认释放该PDN连接的全部资源。 


eNodeB向MME发送Deactivate Bearer Response（去激承载响应）消息，确认该PDN连接上的EPS承载全部去激活。 


UE的NAS层构建Deactivate EPS Bearer Context Accept消息后，UE向eNodeB发送Direct
Transfer消息，此消息携带Deactivate EPS Bearer Context Accept消息。 


eNodeB向MME发送Uplink NAS Transport消息，该消息中包含Deactivate EPS Bearer
Context Accept消息。 




### HSS修改签约QoS，导致承载修改 
### HSS修改签约QoS，导致承载修改 


业务模型 :用户修改了签约数据，导致发生HSS触发的承载修改流程，即因承载的QoS（仅包括UE-AMBR）的修改，MME需要通知eNodeB、UE这些相关信息的修改，并通知SGW承载修改响应。
被修改的承载可以是默认承载或专有承载，承载修改完成之后，UE可以通过EPS网络修改之后的承载访问数据业务和其他业务。
 说明： 
该流程不支持QCI资源类型的修改，即不支持GBR承载和Non-GBR承载的相互转化。


信令流程 :HSS发起的签约QoS修改流程如[图1](52%20HSS%E4%BF%AE%E6%94%B9%E7%AD%BE%E7%BA%A6QoS%EF%BC%8C%E5%AF%BC%E8%87%B4%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9.html#concept1__HSS%E4%BF%AE%E6%94%B9%E7%AD%BE%E7%BA%A6QoS%E5%AF%BC%E8%87%B4%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9-4FBC1465)所示。
图1  HSS修改签约QoS，导致承载修改


[]images/52%20HSS%E4%BF%AE%E6%94%B9%E7%AD%BE%E7%BA%A6QoS%EF%BC%8C%E5%AF%BC%E8%87%B4%E6%89%BF%E8%BD%BD%E4%BF%AE%E6%94%B9.png)



流程说明 :

HSS发送Insert Subscriber Data消息给MME，消息中携带用户的IMSI号码和用户签约数据（Subscription
Data）。Subscription Data中包含EPS subscribed QoS（QCI、ARP）、签约的APN-AMBR和UE-AMBR。


MME更新存储的用户签约数据，并向HSS返回Insert Subscriber Data Ack响应消息，消息中携带用户的IMSI号码。 


如果仅仅是用户签约数据（Subscription Data）中的UE-AMBR发生改变，MME需要重新计算新的UE-AMBR，并通过S1-AP
UE Context Modification流程将修改后的UE-AMBR带给eNodeB，完成UE-AMBR的更新。在UE上下文修改流程后，HSS发起的签约QoS修改流程结束。 
如果签约的QCI、APR和APN-AMBR中有发生改变的参数，并且修改的QoS Profile存在激活状态的PDN连接，MME会向SGW发送Modify
Bearer Command消息，该消息中包含：EPS Bearer Identity、EPS Bearer QoS、APN AMBR。其中，EPS
Bearer Identity信元标识了相关PDN连接的缺省承载，EPS Bearer QoS信元包含了需要更新的EPS签约QoS模板。


SGW向PGW发送Modify Bearer Command消息，该消息中携带EPS Bearer Identity、APN
AMBR 、EPS Bearer QoS。 


（可选）如果分组核心网中部署了PCRF（开启动态PCC功能），PGW将发起IP-CAN修改流程，告知PCRF更新后的EPS
Bearer QoS，PCRF向PGW发送更新后的PCC策略。


PGW向PCRF发送CCR-U消息，通知PCRF修改IP CAN会话。 


PCRF将PCC规则请求与IP-CAN会话及PGW可用的业务信息进行关联，PCRF授权并进行策略决策，并向PGW返回CCA-U消息，消息包含：PCC
Rules、Event Triggers和选择的IP-CAN承载建立模式（如果变更）。 




PGW修改签约QoS被修改的APN对应的每个PDN连接的缺省承载。如果签约的ARP参数已被修改且PCRF未下发策略，PGW将修改全部使用原有签约ARP的专有承载。然后，PGW向SGW发送Update
Bearer Request消息，该消息中携带EPS Bearer Identity、EPS Bearer QoS、TFT、APN-AMBR。 


SGW存储变化的参数，向MME发送Update Bearer Response消息，携带变化的TFT、EPS Bearer QOS、APN-AMBR等信息。


如果UE处于空闲态，MME触发网络侧触发的业务请求流程；如果UE处于连接态，MME向eNodeB发送Bearer Modify
Request消息，消息中可能包括了EPS承载的QoS（但是不包含ARP）、APN-AMBR（如果APN-AMBR改变了，MME会重新计算UE-AMBR）、TFT和EPS
Bearer Identity和Session Management Request，其中Session Management Request是MME构造的消息。 


eNodeB将修改过的EPS bearer QoS映射为Radio Bearer QoS，然后向UE发送RRC Connection
Reconfiguration消息，消息包含：Radio Bearer QoS、Session Management Request、EPS
RB Identity。 


UE向eNodeB响应RRC Connection Reconfiguration Complete消息，确认无线承载修改。 


eNodeB向MME响应Bearer Modify Response消息指示，请求的EPS Bearer QoS能否被分配，消息中包含EPS
Bearer Identity。 


UE向eNodeB发送Direct Transfer消息，消息中携带UE NAS层构建的Session Management
Response消息，消息包含：EPS Bearer Identity。


eNodeB向MME发送会话管理响应消息Session Management Response（Modify EPS
bearer context accept）。 


MME给SGW发送Update Bearer Response消息确认承载更新，消息中包含EPS Bearer Identity。 


SGW向PGW发送Update Bearer Response消息，告知PGW承载更新成功，消息包含：EPS Bearer
Identity。 




### HSS删除签约数据 
### HSS删除签约数据 


业务模型 :MME和HSS之间S6a接口上的Delete Subscriber Data流程用于删除MME上存储的HSS用户签约数据，该流程由HSS触发，用于删除指定用户存储在MME上的部分或全部签约数据。


信令流程 :HSS删除签约数据信令流程如[图1](53%20HSS%E5%88%A0%E9%99%A4%E7%AD%BE%E7%BA%A6%E6%95%B0%E6%8D%AE.html#concept1__HSS%E5%88%A0%E9%99%A4%E7%AD%BE%E7%BA%A6%E6%95%B0%E6%8D%AE%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-4FBFA96D)所示。
图1  HSS删除签约数据信令流程


[]images/53%20HSS%E5%88%A0%E9%99%A4%E7%AD%BE%E7%BA%A6%E6%95%B0%E6%8D%AE.png)



流程说明 :

HSS向MME发送Delete Subscriber Data Request消息，用于删除指定用户存储在MME上的部分或全部签约数据。 


MME根据请求指示删除部分或全部签约数据，并向HSS响应Delete Subscriber Data Answer消息。 




### HSS取消位置记录 
### HSS取消位置记录 


业务模型 :当运营商决定删除签约用户在MME上的MM上下文和EPS承载时，能过HSS发起的分离流程，用于网络侧通知UE，网络侧不再为该UE提供服务，网络侧释放该UE相关资源。


信令流程 :HSS取消位置记录信令流程如[图1](54%20HSS%E5%8F%96%E6%B6%88%E4%BD%8D%E7%BD%AE%E8%AE%B0%E5%BD%95.html#concept1__HSS%E5%8F%96%E6%B6%88%E4%BD%8D%E7%BD%AE%E8%AE%B0%E5%BD%95%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-4FBCACFD)所示。
图1  HSS取消位置记录信令流程


[]images/54%20HSS%E5%8F%96%E6%B6%88%E4%BD%8D%E7%BD%AE%E8%AE%B0%E5%BD%95.png)



流程说明 :

HSS向MME发送Cancel Location Request消息，要求立即删除用户的MM上下文和EPS承载，消息包含：IMSI、Cancellation
Type，其中Cancellation Type设置为“Subscription Withdrawn”。


（可选）如果UE处于ECM-CONNECTED状态，MME向UE发送Detach Request消息，通知UE将被去附着。 
如果UE处于ECM-IDLE状态，MME首先需要寻呼到UE，然后进行分离过程。 


如果MME中存在激活态的UE上下文，MME为每个PDN连接向SGW发送Delete Session Request消息去激活SGW中的EPS承载上下文，消息包含：LBI。
如果PGW需要根据UE上下文来请求UE的位置信息，MME将在本消息中携带User Location Information信元。


如果SGW收到MME发送的Delete Session Request消息，SGW释放对应的EPS承载上下文信息，并向PGW发送Delete
Session Request消息，消息包含：LBI，本消息指示该PDN连接下的全部承载均被释放。 
如果PGW需要根据UE上下文来请求UE的位置信息，MME将在本消息中携带User
Location Information信元。 


PGW给SGW回送Delete Session Response消息。 


（可选）如果网络中部署了PCRF（开启PCC功能），PGW将发起IP-CAN会话终止流程，通知PCRF，用户的EPS承载已被释放。


PGW向PCRF发送CCR-T消息，通知PCRF终止IP-CAN会话。 


PCRF识别并删除关联的PCC Rules，并向PGW返回CCA-T消息。PGW删除已终止IP CAN会话的相关信息。 




SGW向MME发送Delete Session Response消息，消息包含：TEID。 


（可选）如果UE收到MME发送的Detach Request消息，则在第2步骤后的任意时间向MME发送Detach Accept消息，确认EPS承载释放。 
eNodeB将UE发给MME的NAS层Detach Accept消息和UE所在小区的TAI+ECGI一起同时转发给MME。 


MME向HSS发送Cancel Location Answer消息，确认MM上下文和EPS承载已删除。 


MME接收到Detach Accept消息和Delete Session Response消息后，向eNodeB发送Signalling
Connection Release消息，用于释放UE的S1-MME信令连接。消息包含：Cause，Cause值设置为Detach。 




### 清除功能 
### 清除功能 


业务模型 :清除功能允许MME通知HSS，MME已删除某一已分离用户的签约数据及MM上下文。 
MME可以在用户隐式或显式分离后立即删除签约数据及MM上下文，也可以在用户分离后保留一段时间，这样用户稍后附着时可以重用这些签约数据，而不需要向HSS重新获取。 


信令流程 :清除功能信令流程如[图1](55%20%E6%B8%85%E9%99%A4%E5%8A%9F%E8%83%BD.html#concept1__%E6%B8%85%E9%99%A4%E5%8A%9F%E8%83%BD%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-4FC124FF)所示。
图1  清除功能信令流程


[]images/55%20%E6%B8%85%E9%99%A4%E5%8A%9F%E8%83%BD.png)



流程说明 :

MME删除已分离用户的MM上下文及签约数据后，向HSS发送Purge UE消息。 


HSS设置“UE Purged for E-UTRAN”标识，并向MME回送Purge UE Answer消息。 




缩略语 :缩略语 :## ARP 
Allocation and Retention Priority分配保持优先级
## ECGI 
E-UTRAN Cell Global IdentifierE-UTRAN小区全球标识
EPS :Evolved Packet System演进的分组系统
## GBR 
Guaranteed Bit Rate保证比特率
HSS :Home Subscriber Server归属用户服务器
IMSI :International Mobile Subscriber Identity国际移动用户标识
MME :Mobility Management Entity移动管理实体
NAS :Network Access Service网络接入服务
PCC :Policy and Charging Control计费和策略控制
PCRF :Policy and Charging Rules Function策略和计费规则功能
PDN :Packet Data Network分组数据网
PGW :PDN Gateway分组数据网网关
## QCI 
QoS Class IdentifierQoS类别标识
QoS :Quality of Service服务质量
SGW :Serving Gateway服务网关
## TAI 
Tracking Area Identity跟踪区标识
## TFT 
Traffic Flow Template话务流量模型
UE :User Equipment用户设备
# VoLTE信令流程 
## 基本呼叫 
### 注册流程（融合HLR/HSS） 
### 注册流程（融合HLR/HSS） 


业务模型 :本流程的业务模型如下： 

 
UE附着到EPC网络后，发起IMS注册。 

 
通常IMS APN和数据业务APN采用独立的APN。 

 
用户数据库涉及EPC HSS、IMSHSS、HLR多个逻辑网元，这些逻辑网元可以独立部署，或者合一部署。 

 
SBC兼做P-CSCF/ATCF/ATGW，通常称为VoLTE SBC。 

 
UE注册到IMS网络的可以分为以下两个阶段。

 
UE附着到EPC网络附着流程是用户注册到EPS网络上的流程，是用户开机后的第一个过程，是后续所有的流程的基础。在附着过程中，EPC网络会为用户建立一个默认承载，也可以对用户进行鉴权（用户首次附着到EPS网络上必须鉴权）。如果IMS业务APN和数据业务APN采用独立的APN，则附着流程完成之后，EPC网络就建立了数据APN缺省承载，用户可以通过EPS网络访问数据业务。UE再发起PDN连接请求，EPC网络为其建立IMS APN默认承载。 

 
UE注册到IMS网络UE注册到IMS网络包括基本注册和第三方注册。基本注册过程中，UE主动发起注册，IMS网络与UE进行双向鉴权，通常采用IMS AKA或者SIP Digest鉴权方式，鉴权通过后，S-CSCF从IMS HSS下载到用户数据，基本注册完成。第三方注册过程中，S-CSCF根据用户数据中的iFC触发到AS的注册，AS从融合IMS HSS下载到UE的业务数据后，第三方注册完成。 

 


信令流程 :注册流程（融合HLR/HSS）如[图1](1-%E6%B3%A8%E5%86%8C%E6%B5%81%E7%A8%8B%EF%BC%88%E8%9E%8D%E5%90%88HLR%20HSS%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E6%B3%A8%E5%86%8C%E6%B5%81%E7%A8%8B%E8%9E%8D%E5%90%88HLRHSS-B6522CEC)所示。
图1  注册流程（融合HLR/HSS）


[]images/img-0013377820(%E9%87%8D%E7%94%A81).png)

EPC附着信令流程


UE通过eNodeB向MME发起附着请求Attach Request，其中MS Network Capability信元会指示终端是否支持SRVCC。


MME检查Attach Request消息，判决需要对用户鉴权（比如消息完整性保护失败、MME启动附着强制鉴权等），同时MME没有此用户可用的鉴权向量信息，则MME向融合HLR/HSS发送AIR消息，请求鉴权数据，消息中携带user-name信元，表示用户的IMSI；否则，流程从第6步开始。


融合HLR/HSS向MME返回AIA消息，消息中携带用户的四元组鉴权向量，包括XRES（Expected Response）、RAND（Random Challenge）、AUTN、KASME。


MME收到AIA消息后，向UE发送Authentication Request消息，对UE发起鉴权请求。消息中包含：RAND、AUTN、KSIasme。


如果UE鉴权成功，则会根据RAND计算出RES（Response）并通过Authentication Response返回给MME。MME使用鉴权向量组中的XRES和UE返回的RES（Response）比较，相同则鉴权成功，否则鉴权失败并向UE发送Authentication
Reject消息。


EPC网络对终端的USIM卡完成鉴权流程后，如果从UE上次分离后MME改变了，或MME没有UE的有效的签约上下文，或IMEI改变，则MME向融合HLR/HSS发送ULR消息，获取用户信息，消息中携带UE-SRVCC-Capability信元：指示UE是否支持SRVCC能力，消息中携带Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions信元：指示EPC网络是否支持IMS语音业务。


融合HLR/HSS向MME发送ULA消息，向MME插入签约数据，包括默认APN，一个或多个PDN签约上下文。如果IMS业务APN和数据业务APN采用独立的APN，则这里默认APN是数据业务APN。


MME根据APN FQDN查询DNS配置，再结合S-GW POOL和P-GW POOL的网络拓扑选择S-GW和P-GW，向S/P-GW发送Create Session
Request消息，请求建立数据APN缺省承载。S-GW缓存任何从PDN GW接收的下行分组数据，直到收到第14步的修改承载请求消息，在这之前不能发送下行数据通知消息给MME。


P-GW收到Create Session Request消息后，执行IP-CAN会话建立流程，即PGW向PCRF发送CCR信用控制请求消息，获取UE的缺省PCC规则。


PCRF根据SPR的签约信息、PGW上报的网络信息和PCRF的本地配置信息进行策略决策，对数据APN的PDN连接的请求进行EPS默认承载的QoS授权，并使用信用控制应答消息CCA下发授权的QoS信息给PGW。消息里携带Default-EPS-Bearer-QoS
AVP，其QCI根据需要设置。


S/P-GW向MME返回Create Session Response消息，其中携带QCI的信元，指示建立数据APN缺省承载已完成。


MME根据缺省APN的签约APN-AMBR和签约UE-AMBR确定UE-AMBR，通过eNodeB向UE发送Attach Accept消息，如果MME分配了新的GUTI，则消息中包含GUTI。


UE通过eNodeB发送Attach Complete消息给MME。


MME收到后发送Modify Bearer Request消息给S/P-GW，消息中携带无线侧的TEID和地址。


S/P-GW根据下行TEID和地址通过所建立的缺省承载立即开始给UE传送数据包，并给MME回复Modify Bearer Response消息。


如果IMS业务APN和数据业务APN采用独立的APN，则附着流程完成之后，EPC网络就建立了数据APN缺省承载，用户可以通过EPS网络访问数据业务。UE再发起PDN连接请求，消息中携带IMS APN名称，EPC网络为其建立IMS APN默认承载。


MME向S/P-GW发送Create Session Request消息，消息中携带IMS APN名称和IMS APN的QCI，请求建立IMS APN默认承载。


P-GW收到Create Session Request消息后，执行IP-CAN会话建立流程，即PGW向PCRF发送CCR信用控制请求消息，获取UE的PCC规则。


PCRF根据SPR的签约信息、PGW上报的网络信息和PCRF的本地配置信息进行策略决策，对IMS APN的PDN连接的请求进行EPS默认承载的QoS授权，并使用信用控制应答消息CCA下发授权的QoS信息给PGW。消息里携带Default-EPS-Bearer-QoS AVP，其QCI根据需要设置。


S/P-GW向MME返回Create Session Response消息，消息中携带关键信元PCO和QCI，指示建立IMS信令默认承载已完成，其中PCO包含P-CSCF的地址。


IMS注册流程


UE读取USIM卡信息获取IMSI，再从IMSI推导出IMPI和IMPU，向IMS拜访网络入口P-CSCF发送REGISTER消息请求注册。


P-CSCF根据Request-URI头域中域名查询DNS服务器，获得拜访域网络入口I-CSCF网元地址，向I-CSCF转发REGISTER消息。


I-CSCF收到REGISTER消息后，做如下处理：

 
CSCF根据Request-URI中的域名，判断是否在信任域或本地域。 

 
对于本域用户，向IMS HSS发送UAR消息，请求获取S-CSCF的地址或者能力集。 

 


融合HLR/HSS收到UAR消息，根据本地数据库中的用户开户信息，判断用户已开户，则向I-CSCF发送UAA响应，返回S-CSCF的地址或者能力集。

 
当UAA消息中携带Server-Name时，表示携带的为S-CSCF的地址。 

 
当UAA消息中携带Server-Capabilities时，表示携带的为S-CSCF的能力集。 

 


I-CSCF根据融合HLR/HSS返回的S-CSCF地址，向S-CSCF转发REGISTER消息。S-CSCF向融合HLR/HSS发送MAR消息，请求获取认证向量AV（Authorization Vector）。同时融合HLR/HSS记录当前S-CSCF主机名，保证401鉴权挑战消息之后的REGISTER消息能够到达同一个S-CSCF。


融合HLR/HSS向S-CSCF返回MAA响应，包括鉴权五元组XRES、RAND（Random Challenge）、AUTN、IK和CK（Cipher Key）。


S-CSCF根据RAND和AUTN生成nonce，并将nonce同IK、CK以及鉴权算法放到WWW-Authenticate头域中，随401响应返回给P-CSCF。同时，S-CSCF保存参数XRES，以备后续对用户的鉴权响应进行验证。


P-CSCF从消息中取出IK和CK并保存，将消息中剩余的鉴权元素RAND和AUTN继续向UE转发。


UE收到401响应后，根据本地ISIM中保存的共享密钥对AUTN进行认证，实现对归属网络的认证。再基于共享密钥和RAND计算出RES（Response），重新构造REGISTER消息，携带RESPONSE，按照初始REGISTER消息的路径发给P-CSCF。


P-CSCF按照初始REGISTER消息的路径发送后续REGISTER给I-CSCF。


I-CSCF收到REGISTER消息后，发送UAR，查询HSS得到服务的S-CSCF主机名。


融合HLR/HSS收到UAR消息后，将之前记录的S-CSCF的地址信息通过UAA消息发送给I-CSCF。


S-CSCF收到鉴权响应，本地通过MD5算法计算得到response，并与第二条注册请求中的response进行比较。如果两者匹配，则该UE通过网络鉴权。鉴权通过后，S-CSCF向融合HLR/HSS发送SAR消息，请求下载用户的签约数据。


融合HLR/HSS向S-CSCF返回iFC、计费功能地址等信息。


S-CSCF向UE侧返回200响应，表明初始注册成功。


S-CSCF根据从融合HLR/HSS处下载的用户签约信息，判断其中有针对REGISTER请求的iFC数据，S-CSCF根据iFC中AS地址，向AS发送第三方注册请求。如果用户签约信息中包含多条针对REGISTER请求的iFC数据，S-CSCF会根据优先级从高到低依次发送给iFC中的AS地址。同时S-CSCF还支持根据签约，携带UE发起的注册请求和注册成功响应消息。


AS发现用户为第一次注册，发送UDR消息给融合HLR/HSS，请求获取用户数据（包括用户身份数据、业务签约数据等）。


融合HLR/HSS向AS返回UDA响应，携带用户数据。


AS发送SNR消息给融合HLR/HSS，向HSS进行订阅。


融合HLR/HSS向AS返回SNA响应，表示订阅成功。当后续用户订阅的签约业务发生改变，HSS会通过SNR向AS进行同步，保证业务数据的一致性据。


AS根据收到的用户数据对用户进行鉴权。鉴权通过后，AS将用户数据保存到本地数据库，并向S-CSCF返回第三方注册的200成功响应。至此，IMS网络注册已完成。 




### 终端发起的注销流程 
### 终端发起的注销流程 


业务模型 :当用户关机或者主动注销用户，此时，HSS需要通过注销流程将用户的注册状态从“已注册”变为“未注册”，基本过程如下： 

 
UE通过EPC网络向IMS网络发起注销请求。 

 
IMS收到注销请求后，对用户进行鉴权，通知HSS变更用户注册状态，同时删除SBC和SCSCF上本地保存的用户数据。 

 
SCSCF还将通知AS注销用户，AS也会删除本地保存的用户数据。 

 
终端发起的注销流程可分为： 

 
UE从IMS网络注销：UE先向CSCF发起注销请求，CSCF通过与HSS的交互，HSS将UE的状态修改为“未注册”。之后，CSCF向AS发起第三方注销请求。 

 
UE从EPC网络分离：MME网元分离流程是用户从EPC网络上注销的流程，UE发起分离请求后，MME会删除为用户建立的所有承载，包括IMS
APN默认承载，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为注销态。分离流程完成之后，用户不能再通过EPC网络进行语音业务和数据业务。 

 


信令流程 :终端发起的注销消息流程如图[图1](2-%E7%BB%88%E7%AB%AF%E5%8F%91%E8%B5%B7%E7%9A%84%E6%B3%A8%E9%94%80%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E8%AF%AD%E9%9F%B3%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E4%B8%BB%E5%8F%ABVolte%E7%94%A8%E6%88%B7%E9%99%84%E7%9D%80%E5%9C%A8LTE%E8%A2%AB%E5%8F%ABVolte%E7%94%A8%E6%88%B7%E9%99%84%E7%9D%80%E5%9C%A82G-B6B3D743)所示。
图1  语音业务流程（主叫VoLTE用户附着在LTE 被叫VoLTE用户附着在2G 3G）

[]images/img-0013374144(%E9%87%8D%E7%94%A81).png)
IMS注销流程


UE向IMS拜访网络入口SBC/P-CSCF发送REGISTER消息请求注销，其中expires值等于0表示注销。 


P-CSCF根据Request-URI头域中域名查询DNS服务器，获得归属域网络入口I-CSCF网元地址，向I-CSCF转发REGISTER消息。 


I-CSCF收到REGISTER消息后，I-CSCF需要向HSS发送UAR	请求，以获得用户所在SCSCF的地址。 UAR请求中携带PUI和PVI，以及拜访网络标识，同时User-Authorization-Type，其取值为“De-Registration”表示注销请求。 


IMS HSS收到UAR消息，根据本地数据库中的用户信息，判断用户是否注册状态，同时通过UAA响应，返回用户注册时保存的S-CSCF的地址。 


I-CSCF根据IMS HSS返回的S-CSCF地址，向S-CSCF转发REGISTER消息。S-CSCF向IMS HSS发送SAR消息，消息中携带关键AVP
Server-Assignment-Type，其取值为“USER_DEREGISTRATION”表示S-CSCF请求IMS HSS将用户状态置为“注销”。 


IMS HSS将用户状态置为“not register”后，向S-CSCF返回SAA响应消息。 


S-CSCF向UE侧反馈200响应，表示注销成功。SCSCF会删除本地保存的用户数据，包括隐式集、iFC、计费功能地址、鉴权信息等。 


S-CSCF根据UE注册时从IMS HSS处下载的用户签约iFC信息，判断注销是需要触发AS，SCSCF则会向AS发送第三方注销请求。如果用户签约信息中包含注销多此触发不同的AS，那么SCSCF根据签约的优先级，依次触发AS1、AS2、ASn，实现对应用服务器的注销。 


AS向S-CSCF侧反馈200OK响应，表明第三方注销成功。至此，IMS用户注销已完成。 


EPC分离流程


UE通过eNodeB向MME发起附着请求Detach Request，消息中携带Detach type指示EPS detach、IMSI
detach或combined EPS/IMSI detach。 


MME按每PDN连接发送Delete Session Request 给S/P-GW, 去激活S/P-GW内该UE激活的EPS
承载，包括IMS APN的PDN连接。如果S/P-GW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。 


P-GW收到Delete Session Request消息后，执行IP-CAN会话终止流程，即PGW向PCRF发送CCR信用控制请求消息，指示PCRF删除UE相关的PCC规则，EPS承载删除。 


PCRF删除UE相应的APN的IP-CAN会话和所关联的PCC规则后，向P-GW返回信用控制应答消息CCA响应消息。 


S/P-GW向MME返回Delete Session Response消息，携带cause信元指示IMS APN默认承载已成功删除。 


MME向UE返回Detach Accept (UE originating detach)消息。MME删除为用户建立的所有承载，包括IMS
APN默认承载，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为注销态。EPC网络分离后用户不能再通过EPC网络进行语音业务和数据业务。 




### 网络侧发起的注销流程 
### 网络侧发起的注销流程 


业务模型 :当用户需要修改鉴权秘钥，或者运维人员出于运维考虑，IMS核心网可以主动注销用户。通过网络侧发起的注销，可将用户的注册状态从“已注册”变为“未注册”。其关键流程如下： 


IMS-HSS先向S-CSCF网络发起注销。 


S-CSCF通知UE和P-CSCF、AS注销用户，保证全网数据和状态的一致性。 


EPC网络与UE进行分离。 


网络侧发起的注销流程主要分两个阶段。 

 
IMS-HSS发起注销：IMS-HSS向S-CSCF发起注销请求，S-CSCF通过发送NOTIFY消息将注销状态通知UE。之后，S-CSCF向AS发起第三方注销请求。 

 
UE从EPC网络分离：MME网元分离流程是用户从EPC网络上注销的流程，UE发起分离请求后，MME会删除为用户建立的所有承载，包括IMS
APN默认承载，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为注销态。分离流程完成之后，用户不能再通过EPC网络进行语音业务和数据业务。 

 


信令流程 :网络侧发起的注销流程如[图1](3-%E7%BD%91%E7%BB%9C%E4%BE%A7%E5%8F%91%E8%B5%B7%E7%9A%84%E6%B3%A8%E9%94%80%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E7%BD%91%E7%BB%9C%E4%BE%A7%E5%8F%91%E8%B5%B7%E7%9A%84%E6%B3%A8%E9%94%80%E6%B5%81%E7%A8%8B-C72AB4D5)所示。
图1  网络侧发起的注销流程


[]images/img-0013541648(%E9%87%8D%E7%94%A81).png)

IMS注销流程


IMS-HSS向S-CSCF发送RTR消息，发起网络侧注销请求。RTR请求中将包含注销操作的原因。 

 
PERMANENT_TERMINATION(0)：RTR消息中携带的IMPI后续再次发起注册时，IMS-HSS不会再向该IMPI分配此S-CSCF。 

 
NEW_SERVER_ASSIGNED(1)：IMS-HSS已向IMPI重新分配了新的S-CSCF，请求原S-CSCF删除该IMPI的相关数据。 

 
SERVER_CHANGE(2)：通知S-CSCF向UE发起注销，使得UE向新的S-CSCF发起注册请求。 

 
REMOVE_S-CSCF(3)：后续任何用户发起注册请求时，IMS-HSS都不会向注册用户分配该S-CSCF。 

 


S-CSCF向IMS-HSS返回响应消息RTA。 


当用户注册时，UE先前已经发起了注册状态的订阅并成功，那么S-CSCF基于此订阅对话，向P-CSCF发送对话内NOTIFY消息，携带Subscription-State头域取值为“terminated”表示当前用户状态为“已注销”。 


P-CSCF收到S-CSCF的NOTIFY消息后，将消息转发给UE。 


UE返回200响应，表明基本注销成功。 


S-CSCF根据本地保存的iFC信息，决定触发第三方注销，S-CSCF会根据iFC中优先级从高到低依次发送给iFC中的多个AS地址。 


AS向S-CSCF侧反馈200响应消息，表明第三方注销成功。至此，IMS网络注销已完成。 


EPC分离流程


UE通过eNodeB向MME发起附着请求Detach Request，消息中携带Detach type指示EPS detach、IMSI
detach或combined EPS/IMSI detach。 


MME按每PDN连接发送Delete Session Request给S/P-GW, 去激活S/P-GW内该UE激活的EPS
承载，包括IMS APN的PDN连接。如果S/P-GW请求了UE位置信息，则MME需要在该消息中包含该用户的位置信息。 


P-GW收到Delete Session Request消息后，执行IP-CAN会话终止流程，即PGW向PCRF发送CCR信用控制请求消息，指示PCRF删除UE相关的PCC规则，EPS承载删除。 


PCRF删除UE相应的APN的IP-CAN会话和所关联的PCC规则后，向P-GW返回信用控制应答消息CCA响应消息。 


S/P-GW向MME返回Delete Session Response消息，携带cause信元指示IMS APN默认承载已成功删除。 


MME向UE返回Detach Accept (UE originating detach)消息。MME删除为用户建立的所有承载，包括IMS
APN默认承载，释放无线资源，删除移动性管理上下文或把移动性管理上下文状态置为注销态。EPC网络分离后用户不能再通过EPC网络进行语音业务和数据业务。 




### 语音业务流程（主被叫VoLTE用户均附着在LTE） 
### 语音业务流程（主被叫VoLTE用户均附着在LTE） 


业务模型 :本流程的业务模型如下： 

 
主叫、被叫用户归属于同一个IMS网络。 

 
主叫、被叫用户都是VoLTE用户，且已注册。 

 
主叫、被叫均附着在LTE。主叫用户先挂机。 

 
HLR/SAE-HSS/IMS-HSS合一部署，HSS\ENUM\DNS也合一部署。 

 
呼叫流程可以分为： 

 
主叫侧呼叫流程：与固网IMS呼叫一致。 

 
被叫侧呼叫流程：比固网IMS呼叫多了VoLTE AS网元，VoLTE AS发起T-ADS流程，涉及融合HLR/HSS、MME网元。 

 
被叫的LTE专用承载建立流程：被叫侧P-CSCF在收到183或180响应时，从其中取出媒体信息，根据媒体信息的要求，通过PCRF要求P-GW建立被叫用户在LTE域的专用LTE承载。 

 
主叫的LTE专用承载建立流程：主叫侧P-CSCF在收到183或180响应时，从其中取出媒体信息，根据媒体信息的要求，通过PCRF要求P-GW建立主叫用户在LTE域的专用LTE承载。 

 
主叫的LTE专用承载释放流程：主叫发Bye，被叫用户返回200 OK时，被叫P-CSCF通过PCRF要求P-GW释放LTE域专用承载。主叫P-CSCF在收到200
OK时，通过PCRF要求P-GW释放LTE域专用承载。 

 


信令流程 :呼叫流程如[图1](4-%E8%AF%AD%E9%9F%B3%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%EF%BC%88%E4%B8%BB%E8%A2%AB%E5%8F%ABVoLTE%E7%94%A8%E6%88%B7%E5%9D%87%E9%99%84%E7%9D%80%E5%9C%A8LTE%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__VoLTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABVoLTE%E7%94%A8%E6%88%B7%E9%83%BD%E6%98%AFLTE%E5%9F%9F%E9%99%84%E7%9D%80-B6AE67C6)所示。
图1  VoLTE用户呼叫VoLTE用户(都是LTE域附着)

[]images/img-0013409684(%E9%87%8D%E7%94%A81).png)
主叫信令面流程


主叫终端UE_A向P-CSCF发起呼叫。 


P-CSCF从INVITE消息中得到主叫用户的媒体信息，将IP与媒体信息通过AAR发给PCRF，要求PCRF建立LTE域承载。 


PCRF用AAA响应回答PCSCF。 


P-CSCF在invit的via\Record-Route头中加入自己的地址，把Route头中添加S-CSCF地址后，将invite发给S-CSCF。 


S-CSCF_A收到 invite消息后，从P-Asserted-Identity头中取出主叫用户PUI，判断已经注册，则根据iFC触发呼叫到VoLTE
AS_A。 
S-CSCF_A在触发VoLTE AS_A之前，会做如下判断：S-CSCF_A判断VoLTE AS_A是否在信任域内，如果VoLTE
AS_A在信任域内，S-CSCF_A会将P-Access-Network-Info头域发往VoLTE AS_A，否则将删除P-Access-Network-Info头域。 


VoLTE AS_A为主叫UE_A提供补充业务后，把INVITE发到S-CSCF_A。 
 


S-CSCF_A根据被叫号码查询ENUM，获取用户的SIP URI后，根据SIP URI的域名查询DNS获得被叫I-CSCF_B的IP地址。S-CSCF_A再将INVITE消息发送到被叫I-CSCF_B。 


被叫信令面流程（T-ADS域选）


I-CSCF_B向HSS发送LIR消息，要求获取UE_B注册的S-CSCF_B地址。 
 


HSS收到LIR消息后，因为UE_B在注册时会在HSS中登记S-CSCF地址，则向I-CSCF_B发送LIA消息，携带S-CSCF_B的服务器地址。 


S-CSCF_B收到INVITE消息后，根据被叫用户的iFC数据，选择一个AS为VoLTE AS_B，发送INVITE消息，以触发被叫业务和被叫域选择功能。 


VoLTE AS_B向HSS发送UDR消息，要求取得被叫用户的T-ADS信息。 


HSS本身融合了SAE-HSS功能，会通过IDR消息向MME_B查询被叫用户的T-ADS信息。 


MME_B通过IDA消息向HSS发送被叫用户的T-ADS信息。  


HSS将T-ADS信息通过UDA消息返回给VoLTE AS_B。 


VoLTE AS根据得到的T-ADS信息，内部逻辑判断应域选择到IMS域，则发INVITE给S-CSCF_B网元，Request-uri是被叫用户在IMS域内的URI号码。 


S-CSCF_B判断当前被叫用户的iFC触发完成，则找到用户注册的P-CSCF_B地址，将INVITE消息发送到P-CSCF_B。  


P-CSCF_B从INVITE消息中获得主叫用户的媒体面信息，并将之通过AAR消息发送给PCRF_B，要求PCRF_B建立LTE专有承载。  


PCRF_B向P-CSCF_B发送AAA响应。 


P-CSCF_B把INVITE消息发送给UE_B。 


被叫承载面建立


被叫UE_B返回180响应，在SDP中携带SDP Answer信息。  


P-CSCF_B收到被叫侧返回的180响应后，发送AAR消息给PCRF_B，AAR中携带UE_B的媒体信息，以便于PCRF进行承载控制。 


PCRF_B根据认证/授权请求消息AAR消息中携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求消息RAR消息将QoS（QCI/ARP/GBR/MBR）和PCC规则发送至P-GW_B。 


P-GW_B收到重新认证/授权请求消息RAR，上报重新认证/授权应答消息RAA响应给PCRF_B。 


PCRF_B根据P-GW_B返回的重新认证/授权应答消息RAA消息，向P-CSCF_B发送认证/授权应答消息AAA响应授权请求结果。 


P-GW_B收到重新认证/授权请求消息RAR，通过Create Bearer Request指示MME_B建立专有承载。  


MME_B收到Create Bearer Request消息后，向被叫UE_B发送Activate dedicated
EPS bearer context request消息，用于请求激活一个专有EPS承载上下文。 


UE_B向被叫MME_B发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


P-GW_B收到Create Bearer Response消息，确认专有承载已经建立。 


P-GW_B向PCRF_B发送信用控制请求消息CCR消息，通知资源预留成功。  


PCRF_B向P-GW_B返回信用控制应答消息CCA响应。  


当PCRF_B收到P-GW_B的资源预留成功事件上报时，向P-CSCF_B发送RAR消息，通知承载建立情况。  


P-CSCF_B向PCRF_B应答成功响应RAA消息。 


主叫承载面建立


P-CSCF_B将180响应转发至P-CSCF_A，其中SDP answer中携带UE_B的媒体信息。  


P-CSCF_A收到被叫侧返回的180响应，发送RAR消息给PCRF_A载。AAR包括UE_A的信令地址和媒体信息。 


P-GW_A收到重新认证/授权请求消息RAR，上报重新认证/授权应答消息RAA响应给PCRF_A。 


PCRF_A根据P-GW_A返回的重新认证/授权应答消息RAA消息。 


PCRF_A给P-CSCF_A发送认证/授权应答消息AAA，响应授权请求结果消息。 


P-GW_A收到重新认证/授权请求消息RAR，通过Create Bearer Request指示MME_A建立专有承载。 


MME_A收到Create Bearer Request消息后，向主叫UE_A发送Activate dedicated
EPS bearer context request消息，用于请求激活一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


MME_A发送Create Bearer Response消息给P-GW_A，P-GW_A收到Create Bearer
Response消息确认专有承载已经建立。  


P-GW_A向PCRF_A发送信用控制请求消息CCR消息，通知资源预留成功。 


PCRF_A向P-GW_A返回信用控制应答消息CCA响应。 


当PCRF_A收到P-GW_A的资源预留成功事件上报时，向P-CSCF_A发送RAR消息，通知承载建立已成功。  


P-CSCF_A向PCRF_A应答RAA消息。 


P-CSCF_A将180响应转发至主叫UE_A，其中SDP answer中携带呼叫的媒体信息。 


被叫网络收到主叫网络发送的PRACK请求，表示主叫网络成功接收180响应，并且已完成资源预留。 


被叫UE返回针对PRACK请求的200响应，表示成功接收PRACK请求。 


被叫用户接听电话，被叫UE向主叫网络返回针对INVITE请求的200(INVITE)响应。 


当VoLTE AS_B收到200(INVITE)消息后，开始向本域的CCF发送ACR [Start]消息。  


CCF收到正确的ACR [Start]消息后，将其保存，创建被叫AS CDR，并向VoLTE AS_B发送计费响应消息ACA。 


VoLTE AS_B向主叫VoLTE AS_A转发200(INVITE)消息。  


当VoLTE AS_A收到200(INVITE)消息后，开始向本域的CCF发送ACR [Start]消息。 


CCF收到正确的ACR [Start]消息后，将其保存，创建主叫AS CDR，并向VoLTE AS_A发送计费响应消息ACA（Accounting
Answer）。 


返回针对INVITE请求的200(INVITE)响应消息到主叫UE_A。  


主叫UE向被叫网络返回针对200(INVITE)响应的ACK确认消息，主、被叫UE成功建立会话。 


挂机释放流程


UE_A挂机发送BYE消息。 


当VoLTE AS_A收到BYE消息后，开始向本域的CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS_A发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


VoLTE AS_A将BYE消息透传到被叫的VoLTE AS_B。  


当被叫VoLTE AS_B收到BYE消息后，开始向本域的CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS_B发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


VoLTE AS_B将BYE消息透传到被叫的UE_B。 


UE_B收到主叫侧的挂机请求后，向主叫侧发送200(BYE)响应消息。 


当被叫P-CSCF_B收到200(BYE)响应后，向PCRF_B下发终止会话请求消息STR消息释放承载会话。 


PCRF_B发送重新认证/授权请求消息RAR消息通知P-GW_B删除专有承载，携带charging rule remove指示。 


P-GW_B返回重新认证/授权应答消息RAA给PCRF_B。 


PCRF_B返回终止会话应答消息STA响应给P-CSCF_B。 


P-GW_B根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_B指示删除专有承载。 


MME_B收到Delete Bearer Request消息后，向被叫UE_B发送Deactivate EPS bearer
context request消息，用于请求释放一个专有EPS承载上下文。 


UE_B向被叫MME_B发送Deactivate dedicated EPS bearer context accept消息，用于确认释放一个专有EPS承载上下文。 


MME_B发送Delete Bearer Response消息给P-GW_B。P-GW_B收到该消息，专有承载已经完成删除。 


P-GW_B发送信用控制请求消息CCR消息给PCRF_B，指示专有承载已成功删除。 


PCRF_B给P-GW_B返回信用控制应答消息CCA消息予以确认。 


P-CSCF_B发送BYE的200OK响应给P-CSCF_A。 


当主叫P-CSCF_A收到BYE的200响应后，向PCRF_A发送STR消息，以便PCRF_A释放承载会话。 


PCRF_A发送重新认证/授权请求消息RAR消息通知P-GW_A删除专有承载，携带charging rule remove指示。 


P-GW_A返回重新认证/授权应答消息RAA给PCRF_A。 


PCRF_A返回终止会话应答消息STA响应给P-CSCF_A。 


P-GW_A根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_A指示删除专有承载。 


MME_A收到Delete Bearer Request消息后，向主叫UE_A发送Deactivate EPS bearer
context request消息，用于请求释放一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Deactivate dedicated EPS bearer context accept消息，用于确认释放一个专有EPS承载上下文。 


P-GW_A收到Delete Bearer Response消息，专有承载已经完成删除。 


P-GW_A发送信用控制请求消息CCR消息给PCRF_A，指示专有承载已成功删除。 


PCRF_A给P-GW_A返回信用控制应答消息CCA消息予以确认。 


P-CSCF_A发送BYE的200 OK应答给UE_A，通话结束。 




### 语音业务流程（主叫VoLTE用户附着在LTE，被叫VoLTE用户附着在2G/3G） 
### 语音业务流程（主叫VoLTE用户附着在LTE，被叫VoLTE用户附着在2G/3G） 


业务模型 :本流程的业务模型如下： 

 
主叫、被叫用户归属于同一个IMS网络。 

 
主叫、被叫用户都是VoLTE用户，且已注册。 

 
主叫附着在LTE域，被叫附着在CS域，被叫用户先挂机。 

 
HLR/SAE-HSS/IMS-HSS合一部署，HSS\ENUM\DNS也合一部署。 

 
呼叫流程可以分为： 

 
主叫侧呼叫流程：与固网IMS呼叫一致。 

 
被叫侧T-ADS域选叫流程：比固网IMS呼叫多了VoLTE AS网元，VoLTE AS发起T-ADS流程，涉及融合HLR/HSS、MME网元。 

 
被叫侧呼叫流程： VoLTE AS修改被叫号码为CSRN后，S-CSCF通过MGCF呼出到CS域，一直呼到被叫侧vMSC。 

 
被叫的CS域承载建立流程：被叫用户回答呼叫响应，vMSC会向MGW、无线RNC请求建立承载与无线通道。之后主叫侧P-CSCF在收到183或180响应时，从其中取出媒体信息，根据媒体信息的要求，通过PCRF要求P-GW建立主叫用户在LTE域的专用LTE承载。 

 
被叫挂机流程：被叫挂机后，vMSC与MGCF分别发起承载释放操作。同时把Bye通过IMS网络发给主叫侧。主叫侧P-CSCF会通过PCRF要求P-GW释放LTE域专用承载。 

 


信令流程 :主叫LTE用户通过LTE网络向被叫域选CS网络的LTE用户发起呼叫，具体的语音流程如[图1](5-%E8%AF%AD%E9%9F%B3%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%EF%BC%88%E4%B8%BB%E5%8F%ABVoLTE%E7%94%A8%E6%88%B7%E9%99%84%E7%9D%80%E5%9C%A8LTE%EF%BC%8C%E8%A2%AB%E5%8F%ABVoLTE%E7%94%A8%E6%88%B7%E9%99%84%E7%9D%80%E5%9C%A82G%203G%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E8%AF%AD%E9%9F%B3%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E4%B8%BB%E5%8F%ABVoLTE%E7%94%A8%E6%88%B7%E9%99%84%E7%9D%80%E5%9C%A8LTE%E8%A2%AB%E5%8F%ABVoLTE%E7%94%A8%E6%88%B7%E9%99%84%E7%9D%80%E5%9C%A82G-BA61798E)所示。
图1  语音业务流程（主叫VoLTE用户附着在LTE， 被叫VoLTE用户附着在2G/3G）

[]images/img-0013405706(%E9%87%8D%E7%94%A81).png)
主叫信令面流程


主叫终端发起SIP呼叫，INVITE先到达P-CSCF_A。 


P-CSCF_A从INVITE中取出主叫用户的媒体面信息，通过AAR消息发送给PCRF_A，这使得PCRF_A建立LTE域承载。 


PCRF_A返回承载建立的响应AAA响应给P-CSCF_A。 


P-CSCF_A把INVITE消息发给S-CSCF_A。 


 S-CSCF_A收到INVITE后，取出主叫号码，根据其签约的iFC数据，触发到VoLTE AS_A。 
S-CSCF_A在触发VoLTE AS_A之前，会做如下判断：S-CSCF_A判断VoLTE AS_A是否在信任域内，如果VoLTE
AS_A在信任域内，S-CSCF_A会将P-Access-Network-Info头域发往VoLTE AS_A，否则将删除P-Access-Network-Info头域。 


VoLTE AS_A做完主叫的补充业务后，返回INVITE消息给S-CSCF_A。 


S-CSCF_A根据被叫号码查询ENUM，获取用户的SIP URI，根据SIP URI的域名查询DNS获得被叫I-CSCF_B的IP地址。S-CSCF_A再将INVITE消息发送到被叫I-CSCF_B。 


I-CSCF_B向HSS发送LIR消息，要求获取UE_B注册的S-CSCF_B地址。 


HSS收到LIR消息后，因为UE_B在注册时会在HSS中登记S-CSCF地址，则向I-CSCF_B发送LIA消息，携带S-CSCF_B的服务器地址。 


被叫信令面T-ADS域选流程


S-CSCF_B收到INVITE消息后，根据被叫用户的iFC数据，触发到VoLTE AS_B。 


VoLTE AS_B向HSS发Sh接口UDR消息，要求取得T-ADS信息。 


HSS在UDA消息中返回T-ADS信息，包括： IMSVoiceOverPSSessionSupport、RATtype、,LastUEActivityTime。 


VoLTE AS_B判断当前用户附着在CS域，VoLTE AS_B给HSS发送UDR消息，要求取得CSRN信息。 


融合HLR/HSS会发MAP_PROVIDE_ROAMING_NUMBER消息到G/V MSC Server，要求取得被叫用户的漫游号码MSRN。 
 


G/V MSC Server会在发给融合HLR/HSS的MAP_PROVIDE_ROAMING_NUMBER_ACK消息中返回MSRN。 


HSS会在UDA消息中返回CSRN给VoLTE AS_B。 


VoLTE AS_B把得到的CSRN号码，填在INVITE的Req-uri消息中，发给S-CSCF_B。 


被叫信令面流程


S-CSCF_B确定到MGCF的路由，发送INVITE消息到MGCF。 


MGCF向IM-MGW发送ADD REQ消息，请求添加主叫侧的IP终端，以及指示本次呼叫使用的编解码列表。 


IM-MGW动态分配IP资源，向MGCF回复ADD REPLY消息，其中包含终端信息。 


MGCF向IM-MGW发送ADD REQ消息，请求添加被叫侧的IP终端，以及指示本次呼叫使用的编解码列表。 


IM-MGW动态分配IP资源，返回ADD REPLY消息，携带终端信息 


IM-MGW向MGCF发送NTFY REQ消息，上报承载建立事件。 


MGCF接收到IM-MGW上报的事件信息后，发送NTFY REPLY消息，返回承载建立事件的响应。 


MGCF分析CSRN，获取出局路由通过IAM消息将呼叫请求路由到UE_B当前所在的G/V MSC Server上，消息中携带了建立呼叫的必备信息（如主叫类别、被叫号码等）和一些可选信息（如主叫号码）。 


G/V MSC Server通过RNC向UE_B发送PAGING消息下寻呼，并等待寻呼响应。 


寻呼成功，UE_B通过RNC向G/V MSC Server透传PAGING RESPONSE消息。 


G/V MSC Server向UE_B下发Setup消息，建立呼叫。 


UE_B响应，接受本次呼叫，向G/V MSC Server回复CALL CONFIRMED消息。 


承载面流程建立


G/V MSC Server发送ADD REQ消息到MGW，请求添加到MGCF一侧的IP终端，以及指示本次呼叫使用的编解码列表。 


MGW分配IP资源，返回ADD REPLY消息，消息中携带有终端相关信息。 


G/V MSC Server发送ADD REQ消息到MGW，请求添加到RNC一侧的IP终端，以及指示本次呼叫使用的编解码列表。 


MGW动态分配IP资源，向G/V MSC Server回复ADD REPLY消息，该消息中返回终端相关信息。 


MGW向G/V MSC Server发送NTFY REQ消息，通知到MGCF一侧的承载建立完成。 


G/V MSC Server接收到MGW上报的事件信息后，返回NTFY REPLY消息。 


G/V MSC Server向RNC发送RAB ASSIGNMENT REQUEST消息，发起RAB的指配过程，携带MGW分配的IP地址和端口号，以及支持的编解码。 


RNC发送RADIO BEARER SETUP消息到UE_B分配无线信道。 


UE_B占用无线资源，返回RADIO BEARER SETUP COMPLETE消息。 


RNC向MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP面的初始化，携带RNC侧IP地址、端口号等媒体面信息。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP初始化应答。 


RNC发送RAB ASSIGNMENT RESPONSE消息到G/V MSC Server，指示承载建立完成。 


MGW发送NTFY REQ消息到G/V MSC Server，上报到MGCF一侧的隧道信息。 


G/V MSC Server返回NTFY REPLY消息。 


G/V MSC Server回复APM消息到MGCF，携带G/V MSC Server选择的编解码信息和隧道信息。 


MGCF发送MOD REQ消息给IM-MGW，携带隧道信息。 


IM-MGW返回MGCF发送MOD REPLY消息。 


IM-MGW发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，进行NB_UP的初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP初始化应答。 


IM-MGW发送NTFY REQ消息到MGCF，通知承载建立完成。 


MGCF返回NTFY REPLY消息。 


MGCF向被叫S-CSCF_B返回183响应，在SDP中携带协商完成后的媒体类型及媒体编解码能力。 


S-CSCF_B把183响应转发给VoLTE AS_B。 


VoLTE AS_B返回183响应给S-CSCF_B。S-CSCF_B把183响应发给I-CSCF_B。 


I-CSCF_B把183响应发给I-CSCF_A。I-CSCF_A把183响应发给S-CSCF_A。 


S-CSCF_A把183响应发给VoLTE AS_A。 


VoLTE AS_A返回183响应给S-CSCF_A。 


S-CSCF_A把183响应发给主叫P-CSCF_A 


P-CSCF_A收到被叫侧返回的183（SDP）下发认证/授权请求消息AAR消息给PCRF_A开始建立专有承载。AAR包括媒体描述信息。 


PCRF_A根据认证/授权请求消息AAR消息中携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求消息RAR消息将QoS（QCI/ARP/GBR/MBR）和PCC规则发送至P-GW_A。 


P-GW_A收到重新认证/授权请求消息RAR，与主叫UE_A之间完成语音专有承载的建立后，上报重新认证/授权应答消息RAA响应给PCRF_A。 


PCRF_A根据P-GW_A返回的重新认证/授权应答消息RAA消息，给P-CSCF_A通过认证/授权应答消息AAA响应授权请求结果消息。 


P-GW_A收到重新认证/授权请求消息RAR，P-GW_A分配承载QoS信息，并发送Create Bearer Request给MME_A，建立新的专有承载。  


MME_A收到Create Bearer Request消息后，向主叫UE_A发送Activate dedicated
EPS bearer context request消息，用于请求激活一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


P-GW_A收到Create Bearer Response消息，确认专有承载已经建立。 


P-GW_A向PCRF_A发送信用控制请求消息CCR消息，通知资源预留成功。 


PCRF_A向P-GW_A返回信用控制应答消息CCA响应。  


当PCRF_A收到P-GW_A的资源预留成功事件上报时，向P-CSCF_A发送重新认证/授权请求消息RAR消息，通知承载建立情况。  


P-CSCF_A向PCRF_A返回重新认证/授权应答消息RAA消息。 


P-CSCF_A将183响应转发至主叫UE_A，其中SDP answer中携带语音（Audio）媒体信息。 


UE_A返回PRACK请求给P-CSCF_A。  


P-CSCF_A发PRACK请求给S-CSCF_A。 


S-CSCF_A发PRACK请求给VoLTE AS_A。 


VoLTE AS_A发PRACK请求给S-CSCF_A。S-CSCF_A发PRACK请求给I-CSCF_A。 


I-CSCF_A发PRACK请求给I-CSCF_B。I-CSCF_B发PRACK请求给S-CSCF_B。 


S-CSCF_B发PRACK请求给VoLTE AS_B。 


VoLTE AS_B发PRACK请求给S-CSCF_B。 


S-CSCF_B发PRACK请求给MGCF。MGCF收到PRACK请求，表示主叫网络成功接收183响应，并且已完成资源预留。 


MGCF返回针对PRACK请求的200响应，表示成功接收PRACK请求。 


被叫UE_B振铃，发送Alerting消息给G/V MSC Server。 


被叫接入侧完成承载建立和Iu接口资源分配后，G/V MSC Server向MGCF回复ACM消息。 


G/V MSC Server向MGW发送MOD REQ消息，携带signalsDescriptor描述符，控制MGW播放回铃音。 


MGW向G/V MSC Server回复MOD REPLY消息，播放回铃音。 


MGCF向主叫UE_A发送180消息表示被叫UE_B已振铃。中间依次经过了S-CSCF_B、 VoLTE AS_B、S-CSCF_B、I-CSCF_B、I-CSCF_A、S-CSCF_A、
VoLTE AS_A、S-CSCF_A、P-CSCF_A。 


主叫UE发送PRACK请求，依次经过了P-CSCF_A、S-CSCF_A、VoLTE AS_A、S-CSCF_A、I-CSCF_A、I-CSCF_B、S-CSCF_B、VoLTE
AS_B、S-CSCF_B、MGCF。MGCF收到主叫网络发送的PRACK请求，表示主叫网络成功接收180响应。 


MGCF返回针对PRACK请求的200响应，表示成功接收PRACK请求。 这个响应依次经过了S-CSCF_B、VoLTE
AS_B、S-CSCF_B、I-CSCF_B、I-CSCF_A、S-CSCF_A、VoLTE AS_A、S-CSCF_A、P-CSCF_A。最后发给主叫UE_A。 


被叫UE_B摘机后，UE_B发送Connect消息给G/V MSC Server。 


G/V MSC Server向MGCF回复ANM消息。 


G/V MSC Server向MGW发送MOD REQ消息，控制被叫MGW停止播放回铃音。 


MGW向G/V MSC Server回复MOD REPLY消息，停止播放回铃音。 


MGCF向VoLTE AS_B转发200(INVITE)消息。中间经过S-CSCF_B。 


当VoLTE AS_B收到200(INVITE)消息后，开始向本域的CCF发送ACR [Start]消息。  


CCF收到正确的ACR [Start]消息后，将其保存，创建被叫AS CDR，并向VoLTE AS_B发送计费响应消息ACA。  


VoLTE AS_B发200(INVITE)请求出来，中间依次经过了S-CSCF_B、I-CSCF_B、I-CSCF_A、S-CSCF_A、VoLTE
AS_A。 


当VoLTE AS_A收到200(INVITE)消息后，开始向本域的CCF发送ACR [Start]消息。 


CCF收到正确的ACR [Start]消息后，将其保存，创建主叫AS CDR，并向VoLTE AS_A发送计费响应消息ACA。 


VoLTE AS_A发200(INVITE)请求出来，中间依次经过了S-CSCF_A、P-CSCF_A。最后发给主叫UE_A。 


主叫UE_A向被叫网络返回针对200(INVITE)请求的ACK确认消息。ACK确认依次经过了P-CSCF_A、S-CSCF_A、VoLTE
AS_A、S-CSCF_A、I-CSCF_A、I-CSCF_B、S-CSCF_B、VoLTE AS_B、S-CSCF_B，最后发给MGCF。 


G/V MSC Server向被叫UE_B返回Connect ACK消息。  


主、被叫UE成功建立会话。 


挂机释放流程


被叫UE挂机，发送Disconnect消息到G/V MSC Server。 


G/V MSC Server返回Release消息。 


同时G/V MSC Server发送REL消息到MGCF。 


MGCF返回RLC消息，开始释放资源。 


MGCF发送BYE消息到主叫侧。这个响应依次经过了S-CSCF_B、VoLTE AS_B、S-CSCF_B、I-CSCF_B、I-CSCF_A、S-CSCF_A、VoLTE
AS_A、S-CSCF_A、P-CSCF_A。最后发给主叫UE_A。 


MGCF向IM-MGW发送MOD REQ消息，释放到IMS一侧终端资源。 


IM-MGW返回MOD REPLY消息。 


MGCF向IM-MGW发送MOD REQ消息，释放到MSC Server一侧终端资源。  


IM-MGW返回MOD REPLY消息。 


G/V MSC Server发送MOD REQ消息，释放到MGCF一侧终端资源。 


MGW返回MOD REPLY消息 


UE_B发送Release complete到G/V MSC Server。 


G/V MSC Server发送 IU RELEASE COMMAND消息到RNC，释放空口资源。 


RNC返回IU RELEASE COMPLETE消息。  


G/V MSC Server向MGW发送MOD REQ消息，释放被叫接入网侧终端资源。  


MGW向被叫G/V MSC Server发送MOD REPLY消息，返回释放终端资源的响应。 


当VoLTE AS_A、VoLTE AS_B收到MGCF发送的BYE消息后，开始向本域的CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


UE_A发送200(BYE)给P-CSCF_A。 


当主叫P-CSCF_A收到200(BYE)响应后，向PCRF_A下发终止会话请求消息STR消息释放承载会话。 


PCRF_A发送重新认证/授权请求消息RAR消息通知P-GW_A删除专有承载，携带charging rule remove指示。 


P-GW_A返回重新认证/授权应答消息RAA给PCRF_A。 


PCRF_A返回终止会话应答消息STA响应给P-CSCF_A。 


P-GW_A根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_A指示删除专有承载。 


MME_A收到Delete Bearer Request消息后，向主叫UE_A发送Deactivate EPS bearer
context request消息，用于请求释放一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Deactivate dedicated EPS bearer context accept消息，用于确认释放一个专有EPS承载上下文。 


P-GW_A收到Delete Bearer Response消息，专有承载已经完成删除。 


P-GW_A发送信用控制请求消息CCR消息给PCRF_A，指示专有承载已成功删除。 


PCRF_A给P-GW_A返回信用控制应答消息CCA消息予以确认。 


P-CSCF_A发送200(BYE)给MGCF，这个响应经过 S-CSCF_A、VoLTE AS_A、S-CSCF_A、I-CSCF_A、I-CSCF_B、S-CSCF_B、VoLTE
AS_B、S-CSCF_B。通话结束。 




### CS用户呼叫LTE用户流程 
### CS用户呼叫LTE用户流程 


业务模型 :本流程的业务模型如下： 

 
2G/3G用户（CS域用户）呼叫VoLTE用户，被叫在LTE域接入并注册成功。 

 
VoLTE用户是连续号段，所以主叫CS域采用号码分析路由到被叫IMS域。 

 
MGCF和MSC采用BICC协议。 

 
3G HLR、SAE-HSS和IMS-HSS合一部署。 

 
主叫用户先挂机结束通话。 

 
CS用户呼叫LTE用户流程（被叫号码为连续号段）的呼叫过程可以分为如下几个阶段。 

 
主叫CS域流程：主叫用户在CS域发起呼叫，V/GMSC让MGW建立主叫侧承载后，发IAM给MGCF进入IMS域。 

 
被叫IMS流程（含域选）：CSCF触发VoLTE AS进行T-ADS域选流程，域选到LTE域，S-CSCF通过P-CSCF将呼叫路由到被叫用户。 

 
被叫LTE侧承载建立流程：UE返回183后，P-CSCF控制PCRF发起承载建立请求同，PCRF请求P-GW建立承载。建立成功后，P-CSCF把183转发给主叫侧。 

 
主叫CS域承载修改流程：MSC根据183（带有协商后的媒体）修改了承载。 

 
挂机释放流程：主叫挂机，CS域侧承载释放，被叫终端回200 OK消息给P-CSCF，P-CSCF控制PCRF释放LTE域承载。 

 


信令流程 :CS用户呼叫LTE用户流程（被叫号码为连续号段）的信令流程如[图1](6-CS%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABLTE%E7%94%A8%E6%88%B7%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__CS%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABLTE%E7%94%A8%E6%88%B7%E6%B5%81%E7%A8%8B%E8%A2%AB%E5%8F%AB%E5%8F%B7%E7%A0%81%E4%B8%BA%E8%BF%9E%E7%BB%AD%E5%8F%B7%E6%AE%B5-C6B6621B)所示。
图1  CS用户呼叫LTE用户流程（被叫号码为连续号段）


[]images/img-0013541688(%E9%87%8D%E7%94%A81).png)

主叫流程


主叫MS发送呼叫的CM SERVICE REQUEST消息，请求建立呼叫。 


MSC Server返回CM SERVICE ACCEPT消息，接受业务请求。 


MS发送SETUP消息，携带被叫号码以及语音业务的承载信息。 


MSC Server发送ADD REQ消息到MGW，请求添加接入侧终端。 


MGW分配IP资源，返回ADD REPLY消息，消息中携带IP资源的地址和端口信息。 


MSC Server发送ASSIGNMENT REQUEST消息到BSC，进行指配，携带上述IP地址和端口。 


BSC发送RADIO BEARER SETUP消息到MS，分配无线信道。 


MS占用无线资源，返回RADIO BEARER SETUP COMPLETE消息。 


BSC发送ASSIGNMENT COMPLETE消息到MSC，返回指配应答，携带BSC侧选择的编解码以及用户面IP地址和端口号。 


MSC Server发送MOD REQ消息到MGW，携带BSC分配的IP地址和端口。 


MSC Server返回MOD REPLY。 


MGW发送NTFY REQ消息到MSC Server，上报BSC侧承载建立完成。 


MSC Server返回NTFY REPLY消息。 


MSC Server再次发送ADD REQ消息，请求添加核心网侧终端。 


MGW动态分配IP资源，返回ADD REPLY消息。 


MGW发送NTFY REQ消息到MSC Server，上报隧道指示事件，携带隧道信息。 


MSC Server返回NTFY REPLY应答消息。 


MSC Server分析被叫号码的路由，发送IAM消息到MGCF，携带上述隧道信息。 


MGCF发送ADD REQ消息到IM-MGW，请求建立被叫侧终端。 


IM-MGW分配IP资源，返回ADD REPLY消息。 


MGCF发送INVITE到IMS的CSCF网元。 


被叫流程（含域选）


I-CSCF收到INVITE消息后，给HSS发送LIR消息，要求得到被叫用户所注册的S-CSCF的地址。 


HSS返回LIA消息给I-CSCF，其中返回了一个S-CSCF的Server Name。 


I-CSCF将INVITE消息发送给指定S-CSCF，S-CSCF则根据被叫用户开通的iFC数据，触发到一个VoLTE
AS。 


VoLTE AS触发完业务后，将INVITE消息返回给S-CSCF。 


S-CSCF再根据iFC数据触发到一个VoLTE AS。 


VoLTE AS要执行T-ADS域选择流程，向HSS发送UDR消息，请求获取被叫用户的T-ADS信息。 


融合HLR/HSS发IDR消息给MME，要求得到被叫用户的T-ADS信息。 


MME返回IDA消息，其中有被叫用户的T-ADS信息。 


融合HLR/HSS将T-ADS信息放在UDA消息中，返回给VoLTE AS。 


VoLTE AS根据T-ADS信息，判断当前应域选到LTE网络。VoLTE AS返回INVITE给S-CSCF，被叫号码为用户在IMS注册的号码。 


S-CSCF根据被叫用户注册的P-CSCF地址，将INVITE消息转发给这个P-CSCF。 


P-CSCF从INVITE消息中得到主叫用户的SDP信息后，将媒体信息通过AAR消息发送给PCRF，要求PCRF建立专有承载。 


PCRF向P-CSCF发送AAA响应。 


P-CSCF发INVITE消息给被叫UE。 


被叫UE会返回183响应，在SDP中携带协商完成后的媒体信息。 


被叫承载建立流程


P-CSCF收到被叫侧返回的183响应后，发 AAR消息给PCRF建立专有承载。 


PCRF根据得到的QoS参数和用户订阅信息做策略决策，提供授权的QoS，并通过RAR消息将QoS（QoS关键参数包含QCI、ARP、GBR和MBR）和事件触发信息的门控策略发送至P-GW。 


P-GW收到RAR消息后，上报RAA响应给PCRF。 


PCRF根据P-GW返回的RAA消息，发送AAA消息给P-CSCF，响应授权请求结果。 


P-GW收到RAR消息后，分配承载QoS信息，并发送Create Bearer Request指示MME建立专有承载。 


MME收到Create Bearer Request消息后，向被叫UE发送Activate dedicated EPS
bearer context request消息，用于请求激活一个专有EPS承载上下文。 


UE向MME发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


MME发送Create Bearer Response消息给P-GW，确认专有承载已经建立。 


P-GW向PCRF发送CCR消息，通知资源预留成功。 


PCRF向P-GW返回CCA响应。 


当PCRF收到P-GW的资源预留成功事件上报时，向P-CSCF发送RAR消息，通知承载建立情况。 


P-CSCF向PCRF返回RAA消息。 


P-CSCF向主叫侧转发183消息至MGCF。在SDP中携带协商完成后的媒体类型及媒体编解码能力。 


主叫承载修改流程


MGCF收到183消息，发送MOD REQ消息到IM-MGW，修改到IMS一侧的承载信息。 


IM-MGW返回MOD REPLY消息。 


MGCF发送ADD REQ消息到IM-MGW，请求建立MSC Server侧终端。 


IM-MGW动态分配IP资源，返回ADD REPLY消息。 


MGCF发送MOD REQ消息到IM-MGW，将隧道信息传递到IM-MGW。 


IM-MGW返回MOD REPLY消息。 


IM-MGW发送NTFY REQ消息到MGCF，携带被叫侧隧道信息。 


MGCF返回NTFY REPLY应答消息。 


MGCF发送APM消息到MSC Server，携带上述被叫侧隧道信息。 


MSC Server收到APM消息，发送MOD REQ到MGW，将隧道信息传递到MGW。 


MGW返回MOD REPLY消息。 


MGW发送TRC_IU/NB_UP_INIT_TOIP消息到IM-MGW，进行NB_UP初始化。 


IM-MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，上报承载建立完成。 


MSC Server返回NTFY REPLY消息。 


IM-MGW发送NTFY REQ消息到MGCF，上报承载建立完成。 


MGCF返回NTFY REPLY消息。 


MGCF发送应答183的PRACK请求到被叫侧。 


被叫UE返回针对PRACK请求200 OK消息。 


被叫UE振铃，发送180消息。 


MGCF发送MOD REQ消息到IM- MGW，命令MGW播放回铃音。 


MGW播放回铃音，返回MOD REPLY消息。 


MGCF发送ACM（Address Complete Message）消息到MSC Server。 


MSC Server发送Alerting消息到主叫MS。 


MGCF发送应答180的PRACK请求到被叫侧。 


被叫UE返回针对PRACK请求200 OK消息。 


被叫摘机，UE发送INVITE请求的200 OK消息。 


MGCF发送MOD REQ消息到IM- MGW，命令MGW停止播放回铃音。 


MGW停止播放回铃音，返回MOD REPLY消息。 


MGCF发送ANM消息到MSC Server。 


MGCF发送200 OK的ACK消息到被叫UE。 


MSC Server发送CONNECT消息到主叫MS，通知主叫用户被叫应答。 


主叫MS返回CONNECT ACK消息。 


挂机释放流程


主叫用户挂机，发送DISCONNECT消息到MSC Server。 


MSC Server返回RELEASE消息。 


MS发送RELEASE COMPLETE消息到MSC Server。 


MSC Server发送CLEAR COMMAND消息到BSC。 


BSC清除无线接口和A接口资源，返回CLEAR COMPLETE消息。 


MSC Server发送SUB REQ消息到MGW，释放主叫接入侧终端资源。 


MGW返回SUB REPLY消息。 


MSC Server发送REL消息到MGCF。 


MGCF发送SUB REQ消息到IM-MGW，释放主叫侧终端资源。 


IM-MGW返回SUB REPLY消息。 


MGCF发送RLC消息到MSC Server。 


MSC Server发送SUB REQ消息到MGW，释放主叫核心网侧终端。 


MGW返回SUB REPLY消息。 


MGCF发送BYE消息经过P-CSCF到被叫UE。 


UE接收到BYE消息后，向P-CSCF发送200响应。 


当P-CSCF收到200响应后，向PCRF下发STR消息释放承载会话 。 


PCRF发送RAR消息，通知P-GW删除专有承载，携带charging rule remove指示。 


P-GW返回RAA给PCRF。 


PCRF返回STA响应给P-CSCF。 


P-GW根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME指示删除专有承载。 


MME收到Delete Bearer Request消息后，向被叫UE发送Deactivate EPS bearer
context request消息，用于请求释放一个专有EPS承载上下文。 


UE向被叫MME发送Deactivate dedicated EPS bearer context accept消息，用于确认释放一个专有EPS承载上下文。 


P-GW收到Delete Bearer Response消息，专有承载已经完成删除。 


P-GW发送CCR消息给PCRF，指示专有承载已成功删除。 


PCRF给P-GW返回CCA消息予以确认。 


P-CSCF发送200给MGCF。 


MGCF发送SUB REQ消息到IM-MGW，释放被叫侧终端资源。 


IM-MGW返回SUB REPLY消息。 




### LTE用户呼叫CS用户流程 
### LTE用户呼叫CS用户流程 


业务模型 :本流程的业务模型如下： 

 
主叫是VoLTE用户，在LTE接入，被叫是2G/CS域用户。 

 
主叫、被叫在各自域注册成功。 

 
主叫IMS域与被叫PLMN域之间是MGCF+IM-MGW，之间是BICC协议。 

 
被叫PLMN承载建立采用早指配。主被叫侧的局间承载建立方式为前向延迟。 

 
部署融合HLR/HSS，即HLR、SAE-HSS、IMS-HSS合一部署。融合HLR/HSS和ENUM/DNS合一部署。 

 
2/3G用户先挂机。 

 
LTE用户呼叫CS用户流程具体有以下几个阶段。 

 
主叫信令面流程：主叫侧执行标准IMS流程，S-CSCF通过ENUM/DNS解析得知被叫用户为CS域用户，将SIP会话请求转发至MGCF；MGCF进行路由分析并将会话请求路由出局。 

 
被叫信令面流程：V/GMSC Server寻呼被叫用户，被叫用户收到寻呼消息后返回响应消息。 

 
被叫承载面建立流程：V/GMSC Server指示MGW建立被叫接入侧承载并向主叫侧发消息通知局间承载建立采用前向延迟方式。 

 
主叫承载面建立流程：MGCF指示IM-MGW建立主叫接入侧承载；主被叫进行媒体协商并建立局间承载。 

 
挂机释放流程：主叫用户接收被叫用户挂机请求后释放主叫侧承载资源并回复响应消息；被叫用户在接收到主叫侧响应消息后释放被叫侧承载资源。 

 


信令流程 :LTE用户呼叫CS用户信令流程如[图1](7-LTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABCS%E7%94%A8%E6%88%B7%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__LTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABCS%E7%94%A8%E6%88%B7-C6C1E07B)所示。
图1  LTE用户呼叫CS用户


[]images/img-0013541691(%E9%87%8D%E7%94%A81).png)

主叫信令面流程


主叫用户UE_A通过P-CSCF发送INVITE消息发起会话。 


P-CSCF接收INVITE消息，并发给S-CSCF。 


S-CSCF按主叫签约的IFC触发呼叫到VoLTE AS。 


VoLTE AS提供补充业务，并把INVITE消息转发给S-CSCF。 


S-CSCF通过ENUM查询，发现被叫不是IMS域用户，则把INVITE消息转发给MGCF。 


MGCF通过号码分析发现被叫路由，发送ADD REQ消息至IM-MGW，控制IM-MGW建立承载。 


IM-MGW建立完主叫侧承载端点后，向MGCF发送ADD REPLY消息。 


在完成承载点的建立后，IM-MGW向MGCF发送NTFY REQ消息上报其承载的建立情况。 


MGCF向IM-MGW回复NTFY REPLY消息确认收到上报的承载建立消息。 


MGCF发ADD REQ请求给IM-MGW。 


IM-MGW建立被叫侧承载端点后，通过ADD REPLY消息将端点信息返回至MGCF。 


MGCF对INVITE消息进行处理后，发送IAM消息至被叫侧V/GMSC Server。 


被叫信令面流程


MSC Server收到IAM消息，经过RNC，发送Paging消息寻呼UE_B。 


UE_B收到寻呼消息，经过RNC返回Paging Response消息到MSC Server。 


MSC Server发送SETUP消息到UE_B，建立呼叫。 


UE_B接受本次呼叫，返回Call Confirmed消息到MSC Server。 


被叫承载面流程


MSC Server发送ADD REQ到 MGW，建立无线侧承载终端。 


MGW回复ADD REPLY。 


MSC Server发送RAB Assignment Request消息到RNC，进行RAB指配，携带MGW分配的IP地址和端口号，以及所选择的编解码。 


RNC发送RADIO Bearer Setup到UE_B。 


UE_B占用无线资源，返回RADIO Bearer Setup Complete消息。 


主叫承载面流程


RNC返回RAB Assignment Response消息给MSC Server。 


MSC Server发送ADD REQ消息到MGW，建立到主叫核心网一侧终端。 


MGW回复ADD REPLY消息。 


MSC Server发送APM消息到MGCF，指示本次呼叫使用的编解码。 


MGCF接收APM消息并发送携带SDP的183消息给I/S-CSCF，指示建立主叫侧专用承载。 


I/S-CSCF收到183消息后，先转发给VoLTE AS。 


VoLTE AS返回183消息给I/S-CSCF。 


I/S-CSCF发183消息给P-CSCF。 


P-CSCF接收183消息并下发AAR消息至PCRF开始建立专有承载。 


PCRF要控制P-GW建立承载，则发RAR消息给P-GW。 


P-GW返回RAA消息至PCRF，并不等承载创建成功。 


PCRF向P-CSCF发AAA消息响应授权请求结果消息，并上报EPS计费信息。 


P-GW分配承载QoS信息，并发送CB REQ消息至MME，建立新的专有承载。 


MME收到REQ消息后，向主叫用户UE_A发送AD EPS BCR消息，用于请求激活一个专有EPS承载上下文。 


UE_A向主叫MME发送AD EPS BCA消息，用于确认激活一个专有EPS承载上下文。 


MME收到UE_A的承载激活响应后向P-GW发送CB RSP消息，确认专有承载已经建立。 


P-GW向PCRF发送CCR消息，通知其资源预留成功。 


PCRF向P-GW返回CCA消息响应。 


当PCRF收到P-GW的资源预留成功事件上报时，向P-CSCF发送RAR消息，通知承载建立情况。 


P-CSCF向PCRF返回RAA消息。 


P-CSCF转发183消息至主叫用户UE_A。 


主叫用户返回PRACK消息给P-CSCF，证实183消息。 


P-CSCF发PRACK消息给I/S-CSCF。 


I/S-CSCF发PRACK消息给VoLTE AS。 


VoLTE AS发PRACK消息给I/S-CSCF。 


I/S-CSCF发PRACK给MGCF。 


MGCF返回200 for PRACK消息给I/S-CSCF，完成PRACK消息的证实。 


I/S-CSCF发200 OK给VoLTE AS。 


VoLTE AS发200 OK给I/S-CSCF。 


I/S-CSCF发200 OK给P-CSCF。 


P-CSCF发200 OK给主叫用户UE。 


MGCF发送MOD REQ消息到IM-MGW，申请隧道信息。 


IM-MGW返回MOD REPLY消息。 


IM-MGW发送NTFY REQ消息到MGCF，携带隧道信息。 


MGCF返回NTFY REPLY消息。 


MGCF发送APM消息到MSC Server，携带上述隧道信息。 


MSC Server发送MOD REQ消息至MGW，传递主叫方的隧道信息。 


MGW返回 MOD REPLY消息。 


MGW发送NTFY REQ消息到MSC Server，上报被叫侧隧道信息。 


MSC Server返回NTFY REPLY消息。 


MSC Server发送APM消息到MGCF，携带被叫侧隧道信息。 


MGCF发送MOD REQ消息到IM-MGW，透传被叫侧隧道信息。 


IM-MGW返回MOD REPLY消息。 


IM-MGW发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，初始化NB_UP。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


IM-MGW发送NTFY REQ消息到MGCF，上报被叫侧承载建立完成。 


MGCF返回 NTFY REPLY消息。 


MGW发送NTFY REQ消息到MSC Server。 


MSC Server返回NTFY REPLY消息。 


UE_B发送Alerting消息振铃。 


MSC Server发送MOD REQ消息到MGW，命令MGW播放回铃音。 


MGW播放回铃音，返回MOD REPLY消息。 


MSC Server发送ACM消息到MGCF。 


MGCF发送180 Ring消息至主叫侧I/S-CSCF。 


I/S-CSCF发180消息给VoLTE AS。 


VoLTE AS发180消息给I/S-CSCF。 


I/S-CSCF发180消息给P-CSCF。 


P-CSCF发180消息给主叫用户UE。 


主叫用户返回PRACK消息证实180 Ringing消息给P-CSCF。 


P-CSCF发PRACK消息给I/S-CSCF。 


I/S-CSCF发PRACK消息给VoLTE AS。 


VoLTE AS发PRACK消息给I/S-CSCF。 


I/S-CSCF发PRACK消息给MGCF。 


MGCF返回200 for PRACK消息给I/S-CSCF。 


I/S-CSCF发200 OK消息给VoLTE AS。 


VoLTE AS发200 OK消息给I/S-CSCF。 


I/S-CSCF发200 OK消息给P-CSCF。 


P-CSCF发200 OK给主叫用户UE。 


被叫摘机，UE_B发送Connect消息至MSC Server。 


MSC Server发送MOD REQ消息到MGW，停止播放回铃音。 


MGW停止播放回铃音，返回MOD REPLY消息。 


MSC Server发送ANM消息到MGCF。 


MSC Server发送CONNECT ACK消息到UE_B。 


MGCF发送200 for INVITE消息到主叫侧I-CSCF，指示UE摘机应答。 


I/S-CSCF发200 OK消息 给VoLTE AS。 


VoLTE AS发200 OK消息给I/S-CSCF。 


I/S-CSCF发200 OK消息给P-CSCF。 


P-CSCF发200 OK消息给主叫用户UE。 


主叫侧VoLTE AS AS向CCF发送ACR消息，启动主叫侧计费。 


CCF返回ACA消息。 


UE_A回复ACK消息，主叫处于通话状态，发给主叫P-CSCF。 


P-CSCF发ACK消息给I/S-CSCF。 


I/S-CSCF发ACK消息给VoLTE AS。 


VoLTE AS发ACK消息给I/S-CSCF。 


I/S-CSCF发ACK消息给MGCF。 


挂机释放流程


被叫用户UE_B挂机，发送Disconnect消息至MSC Server。 


MSC Server返回Release消息。 


UE_B发送Release Complete消息到MSC Server。 


MGCF发送SUB REQ消息到IM-MGW，删除到被叫侧的终端。 


IM-MGW返回SUB REPLY消息。 


MSC Server发送REL消息至MGCF。 


MGCF发送BYE消息到I/S-CSCF。 


MGCF返回RLC消息到MSC Server。 


I/S-CSCF发Bye消息给VoLTE AS。 


VoLTE AS发Bye消息给I/S-CSCF。 


I/S-CSCF发Bye消息给P-CSCF。 


P-CSCF发Bye给主叫用户UE。 


当VoLTE AS收到BYE消息后，结束主叫侧计费并向本域的CCF发送ACR消息。 


CCF收到正确的ACR消息后，将其保存，并向VoLTE AS发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


MSC Server收到RLC消息，发送SUB REQ消息指示MGW释放主叫侧终端。 


MGW返回SUB REPLY消息。 


主叫用户UE_A返回200 for BYE指示呼叫释放完毕。 


当P-CSCF收到200 for BYE响应后，向PCRF下发STR消息释放承载会话。 


PCRF发送RAR消息通知P-GW删除专有承载，消息中携带REMOVE QoS Rules指示。 


P-GW返回RAA消息至PCRF。 


PCRF返回STA消息至P-CSCF。 


P-GW发送DB Request消息至MME指示删除专有承载。 


MME向主叫用户UE_A发送DL EPS BCR消息，请求释放一个专有EPS承载上下文。 


UE_A向MME发送DL EPS BCA消息，确认释放一个专有EPS承载上下文。 


P-GW收到DB Response消息，专有承载已成功删除。 


P-GW发送CCR消息至PCRF，指示专有承载已成功删除。 


PCRF至P-GW返回CCA消息予以确认。 


P-CSCF发送200 for BYE消息至I-CSCF。 


I/S-CSCF发200 OK消息给VoLTE AS。 


VoLTE AS发200 OK消息给I/S-CSCF。 


I/S-CSCF发200 OK消息给P-CSCF。 


P-CSCF发200 OK消息给主叫用户UE。 


MGCF发送SUB REQ消息到IM-MGW，删除到主叫侧的终端。 


IM-MGW返回SUB REPLY消息。 


MSC Server发送IU Clear Command消息到RNC。 


RNC返回IU Clear Complete消息。 


MSC Server发送SUB REQ消息到MGW，释放接入侧终端。 


MGW返回SUB REPLY消息。 




### LTE用户呼叫LTE用户视频回落语音流程 
### LTE用户呼叫LTE用户视频回落语音流程 


业务模型 :本流程的信令模型如下： 

 
主叫、被叫为Volte用户，通过LTE域接入，先进行视频通话后再切换为语音流程。 

 
3G HLR，SAE-HSS和IMS-HSS合一部署。 

 


信令流程 :主叫UE_A呼叫被叫UE_B后，视频通话成功。主叫用户UE_A发起媒体切换操作，要求切换为语音操作，具体的流程如[图1](8-LTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABLTE%E7%94%A8%E6%88%B7%E8%A7%86%E9%A2%91%E5%9B%9E%E8%90%BD%E8%AF%AD%E9%9F%B3%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__LTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABLTE%E7%94%A8%E6%88%B7%E8%A7%86%E9%A2%91%E5%9B%9E%E8%90%BD%E8%AF%AD%E9%9F%B3%E6%B5%81%E7%A8%8B-C720F507)所示。
图1  LTE用户呼叫LTE用户视频回落语音流程


[]images/img-0013541694(%E9%87%8D%E7%94%A81).png)

信令面流程


主叫用户UE_A发起媒体切换，要求将媒体切换为语音。发送INVITE消息给P-CSCF_A。 


P-CSCF_A把INVITE消息路由到S-CSCF_A。 


S-CSCF_A触发业务到VoLTE AS_A。 


VoLTE AS_A实现补充业务后，转发INVITE消息给S-CSCF_A。 


S-CSCF_A将INVITE消息发送到被叫I/S -CSCF_B。 


I/S-CSCF_B将收到INVITE消息后，触发业务到VoLTE AS _B。 


VoLTE AS _B实现补充业务后，转发INVITE消息给S-CSCF_B。 


S-CSCF_B转发INVITE消息给P-CSCF_B。 


P-CSCF_B转发INVITE消息给UE_B。 


承载面流程


被叫UE_B返回INVITE请求的200 OK （INVITE）消息。 


P-CSCF_B收到200 OK消息后，发AAR消息给PCRF_B，要求控制P-GW删除视频媒体。 


PCRF_B发RAR消息给P-GW_B，删除了视频媒体。 


P-GW_B返回RAA响应给PCRF_B。 


PCRF_B返回AAA响应给P-CSCF_B。 


P-CSCF_B将200 OK消息转发至I/S-CSCF_B。 


I/S-CSCF_B将200 OK消息透传至I/S-CSCF_A。 


I/S-CSCF_A将200 OK消息转发至P-CSCF_A。 


P-CSCF_A发AAR消息给PCRF_A更新承载，要求控制P-GW删除视频媒体。 


PCRF_A发RAR消息给P-GW_A，删除了视频媒体。 


P-GW_A返回RAA响应给PCRF_A。 


PCRF_A返回AAA响应给P-CSCF_A。 


P-CSCF_A向主叫用户UE_A发200 OK消息。 


主叫用户UE_A返回ACK消息。 


VoLTE AS _A发计费ACR消息给CCF。 


CCF创建CDR后，返回ACA。 


VoLTE AS _A通过I/S-CSCF_A将ACK确认消息透传到被叫I/S-CSCF_B。 


I/S-CSCF_B将ACK确认消息转发至VoLTE AS_B。 


VoLTE AS _B发计费ACR消息给CCF。 


CCF创建CDR后，返回ACA。 


VoLTE AS _B发ACK消息给I/S-CSCF_B。 


I/S-CSCF_B把ACK消息，通过P-CSCF_B路由给被叫用户UE_B。 




### LTE用户呼叫LTE用户视频流程 
### LTE用户呼叫LTE用户视频流程 


业务模型 :本流程的业务模型如下： 

 
主叫、被叫都是VoLTE用户，且注册到IMS成功。 

 
主叫接入域是LTE，通过IMS发起视频电话，被叫接入域为LTE，接听成功。 

 
3G HLR，SAE-HSS和IMS-HSS合一部署，SBC与P-CSCF合一。 

 
主叫视频用户先挂机。 

 
LTE用户呼叫LTE用户视频流程 可以分为如下几个阶段。 

 
主叫信令面流程：与普通IMS呼叫一致。 

 
被叫信令面流程：作T-ADS的VoLTE AS执行域选过程（经过HLR/HSS）。 

 
被叫承载面建立流程：被叫用户收到视频呼叫请求后，返回响应给被叫P-CSCF，P-CSCF通过PCRF，要求P-GW建立被叫终端的专有LTE承载。 

 
主叫承载面建立流程：主叫P-CSCF收到被叫用户回复的响应消息后，P-CSCF通过PCRF，要求P-GW建立主叫终端的专有LTE承载。 

 
挂机释放流程：主叫视频用户先挂机，被叫用户收到Bye消息，通过PCRF，要求P-GW释放被叫终端的专用LTE承载。当主叫侧P-CSCF收到响应时，也会通过PCRF，要求P-GW释放主叫终端的专用LTE承载。 

 


信令流程 :LTE用户呼叫LTE用户视频流程如[图1](9-LTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABLTE%E7%94%A8%E6%88%B7%E8%A7%86%E9%A2%91%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__LTE%E7%94%A8%E6%88%B7%E5%91%BC%E5%8F%ABLTE%E7%94%A8%E6%88%B7%E8%A7%86%E9%A2%91%E6%B5%81%E7%A8%8B-C724E32E)所示。
图1  LTE用户呼叫LTE用户视频流程


[]images/img-0013541697(%E9%87%8D%E7%94%A81).png)

主叫信令面流程


主叫终端UE_A向P-CSCF_A发起呼叫。 


P-CSCF_A从INVITE消息中得到主叫用户的媒体信息，将IP与媒体信息通过AAR发给PCRF_A，要求PCRF_A建立LTE域承载。 


PCRF_A向P-CSCF_A发送AAA响应消息。 


P-CSCF_A在INVITE消息的Via和Record-Route头中加入自己的地址，把Route头中添加S-CSCF_A地址，将INVITE发给S-CSCF_A。 


S-CSCF_A收到INVITE消息后，从P-Asserted-Identity头中取出主叫用户PUI，判断已经注册，则根据的IFC触发呼叫到VoLTE
AS_A。 
S-CSCF_A在触发VoLTE AS_A之前，会做如下判断：S-CSCF_A判断VoLTE AS_A是否在信任域内，如果VoLTE
AS_A在信任域内，S-CSCF_A会将P-Access-Network-Info头域发往VoLTE AS_A，否则将删除P-Access-Network-Info头域。 


VoLTE AS_A为主叫UE_A提供补充业务后，把INVITE发到S-CSCF_A。 


S-CSCF_A根据被叫号码查询ENUM，获取用户的SIP URI，根据SIP URI的域名查询DNS获得被叫I-CSCF_B的IP地址。S-CSCF_A再将INVITE消息发送到被叫I-CSCF_B。 


被叫信令面流程（T-ADS域选）


I-CSCF_B向HSS发送LIR消息，要求获取UE_B注册的S-CSCF_B地址。 


HSS收到LIR消息后，因为UE_B在注册时会在HSS中登记S-CSCF地址，则向I-CSCF_B发送LIA消息，携带S-CSCF_B的服务器地址。 


S-CSCF_B收到INVITE消息后，根据被叫用户的iFC数据，选择一个AS为VoLTE AS_B，发送INVITE消息，以触发被叫业务和被叫域选择功能。 


VoLTE AS_B向HSS发送UDR消息，要求取得被叫用户的T-ADS信息。 


HSS本身融合了SAE-HSS功能，会通过IDR消息向MME_B查询被叫用户的T-ADS信息。 


MME_B通过IDA消息向HSS发送被叫用户的T-ADS信息。 


HSS将T-ADS信息通过UDA消息返回给VoLTE AS_B。 


VoLTE AS根据得到的T-ADS信息，内部逻辑判断应域选择到IMS域，则发INVITE给S-CSCF_B网元，Request-uri是被叫用户在IMS域内的URI号码。 


S-CSCF_B判断当前被叫用户的IFC触发完成，则找到用户注册的P-CSCF_B地址，将INVITE消息发送到P-CSCF_B。 


P-CSCF_B从INVITE消息中获得主叫用户的媒体面信息，并将之通过AAR消息发送给PCRF_B，要求PCRF_B建立LTE专有承载。 


PCRF_B向P-CSCF_B发送AAA响应。 


P-CSCF_B把INVITE消息发送给UE_B。 


被叫承载面建立


被叫UE_B返回180响应，在SDP中携带SDP Answer信息。 


P-CSCF_B收到被叫侧返回的180响应后，发送AAR消息给PCRF_B，AAR中携带UE_B的媒体信息，以便于PCRF进行承载控制。 


PCRF_B根据认证/授权请求消息AAR消息中携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求消息RAR消息将QoS（QCI/ARP/GBR/MBR）和PCC规则发送至P-GW_B。 


P-GW_B收到重新认证/授权请求消息RAR，上报重新认证/授权应答消息RAA响应给PCRF_B。 


PCRF_B根据P-GW_B返回的重新认证/授权应答消息RAA消息，向P-CSCF_B发送认证/授权应答消息AAA响应授权请求结果。 


P-GW_B收到重新认证/授权请求消息RAR，通过Create Bearer Request指示MME_B建立专有承载。 


MME_B收到Create Bearer Request消息后，向被叫UE_B发送Activate dedicated
EPS bearer context request消息，用于请求激活一个专有EPS承载上下文。 


UE_B向被叫MME_B发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


P-GW_B收到Create Bearer Response消息，确认专有承载已经建立。 


P-GW_B向PCRF_B发送信用控制请求消息CCR消息，通知资源预留成功。 


PCRF_B向P-GW_B返回信用控制应答消息CCA响应。 


当PCRF_B收到P-GW_B的资源预留成功事件上报时，向P-CSCF_B发送RAR消息，通知承载建立情况。 


P-CSCF_B向PCRF_B应答成功响应RAA消息。 


主叫承载面建立


P-CSCF_B将180响应转发至P-CSCF_A，其中SDP answer中携带UE_B的媒体信息。 


P-CSCF_A收到被叫侧返回的180响应，发送RAR消息给PCRF_A载。AAR包括UE_A的信令地址和媒体信息。 


P-GW_A收到重新认证/授权请求消息RAR，上报重新认证/授权应答消息RAA响应给PCRF_A。 


PCRF_A根据P-GW_A返回的重新认证/授权应答消息RAA消息。 


PCRF_A给P-CSCF_A发送认证/授权应答消息AAA，响应授权请求结果消息。 


P-GW_A收到重新认证/授权请求消息RAR，通过Create Bearer Request指示MME_A建立专有承载。 


MME_A收到Create Bearer Request消息后，向主叫UE_A发送Activate dedicated
EPS bearer context request消息，用于请求激活一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


MME_A发送Create Bearer Response消息给P-GW_A，P-GW_A收到Create Bearer
Response消息确认专有承载已经建立。 


P-GW_A向PCRF_A发送信用控制请求消息CCR消息，通知资源预留成功。 


PCRF_A向P-GW_A返回信用控制应答消息CCA响应。 


当PCRF_A收到P-GW_A的资源预留成功事件上报时，向P-CSCF_A发送RAR消息，通知承载建立已成功。 


P-CSCF_A向PCRF_A应答RAA消息。 


P-CSCF_A将180响应转发至主叫UE_A，其中SDP answer中携带呼叫的媒体信息。 


被叫网络收到主叫网络发送的PRACK请求，表示主叫网络成功接收180响应，并且已完成资源预留。 


被叫UE返回针对PRACK请求的200 OK，表示成功接收PRACK请求。 


被叫用户接听电话，被叫UE向主叫网络返回针对INVITE请求的200(INVITE)响应。 


当VoLTE AS_B收到200(INVITE)消息后，开始向本域的CCF发送ACR [Start]消息。 


CCF收到正确的ACR [Start]消息后，将其保存，创建被叫AS CDR，并向VoLTE AS_B发送计费响应消息ACA。 


VoLTE AS_B向主叫VoLTE AS_A转发200(INVITE)消息。 


当VoLTE AS_A收到200(INVITE)消息后，开始向本域的CCF发送ACR [Start]消息。 


CCF收到正确的ACR [Start]消息后，将其保存，创建主叫AS CDR，并向VoLTE AS_A发送计费响应消息ACA（Accounting
Answer）。 


返回针对INVITE请求的200(INVITE)响应消息到主叫UE_A。 


主叫UE向被叫网络返回针对200(INVITE)响应的ACK确认消息，主、被叫UE成功建立会话。 


挂机释放流程


UE_A挂机发送BYE消息。 


当VoLTE AS_A收到BYE消息后，开始向本域的CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS_A发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


VoLTE AS_A将BYE消息透传到被叫的VoLTE AS_B。 


当被叫VoLTE AS_B收到BYE消息后，开始向本域的CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS_B发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


VoLTE AS_B将BYE消息透传到被叫的UE_B。 


UE_B收到主叫侧的挂机请求后，向主叫侧发送200(BYE)响应消息。 


当被叫P-CSCF_B收到200(BYE)响应后，向PCRF_B下发终止会话请求消息STR消息释放承载会话。 


PCRF_B发送重新认证/授权请求消息RAR消息通知P-GW_B删除专有承载，携带charging rule remove指示。 


P-GW_B返回重新认证/授权应答消息RAA给PCRF_B。 


PCRF_B返回终止会话应答消息STA响应给P-CSCF_B。 


P-GW_B根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_B指示删除专有承载。 


MME_B收到Delete Bearer Request消息后，向被叫UE_B发送Deactivate EPS Bearer
Context Request消息，用于请求释放一个专有EPS承载上下文。 


UE_B向被叫MME_B发送Deactivate Dedicated EPS Bearer Context Accept消息，用于确认释放一个专有EPS承载上下文。 


MME_B发送Delete Bearer Response消息给P-GW_B。P-GW_B收到该消息，专有承载已经完成删除。 


P-GW_B发送信用控制请求消息CCR消息给PCRF_B，指示专有承载已成功删除。 


PCRF_B给P-GW_B返回信用控制应答消息CCA消息予以确认。 


P-CSCF_B发送BYE的200OK响应给P-CSCF_A。 


当主叫P-CSCF_A收到BYE的200 OK后，向PCRF_A发送STR消息，以便PCRF_A释放承载会话。 


PCRF_A发送重新认证/授权请求消息RAR消息通知P-GW_A删除专有承载，携带charging rule remove指示。 


P-GW_A返回重新认证/授权应答消息RAA给PCRF_A。 


PCRF_A返回终止会话应答消息STA响应给P-CSCF_A。 


P-GW_A根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_A指示删除专有承载。 


MME_A收到Delete Bearer Request消息后，向主叫UE_A发送Deactivate EPS Bearer
Context Request消息，用于请求释放一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Deactivate Dedicated EPS Bearer Context Accept消息，用于确认释放一个专有EPS承载上下文。 


P-GW_A收到Delete Bearer Response消息，专有承载已经完成删除。 


P-GW_A发送信用控制请求消息CCR消息给PCRF_A，指示专有承载已成功删除。 


PCRF_A给P-GW_A返回信用控制应答消息CCA消息予以确认。 


P-CSCF_A发送BYE的200 OK应答给UE_A，通话结束。 




## 锚定 
### Anchor AS被叫锚定流程 
### Anchor AS被叫锚定流程 


业务模型 :CS网络的主叫用户呼叫VoLTE被叫用户时，Anchor AS通过在被叫号码前插前缀的方式，将呼叫锚定到IMS网络，在IMS网络触发用户的被叫侧业务。具体流程如[图1](10-Anchor%20AS%E8%A2%AB%E5%8F%AB%E9%94%9A%E5%AE%9A%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E8%A2%AB%E5%8F%AB%E9%94%9A%E5%AE%9A%E6%B5%81%E7%A8%8B-C6A68E5F)所示。


信令流程 :被叫锚定流程的信令流程如[图1](10-Anchor%20AS%E8%A2%AB%E5%8F%AB%E9%94%9A%E5%AE%9A%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E8%A2%AB%E5%8F%AB%E9%94%9A%E5%AE%9A%E6%B5%81%E7%A8%8B-C6A68E5F)所示。
图1  被叫锚定流程


[]images/img-0013541700(%E9%87%8D%E7%94%A81).png)

主叫流程


主叫MS发送呼叫的CM SERVICE REQUEST消息，请求建立呼叫。 


MSC Server返回CM SERVICE ACCEPT消息，接受业务请求。 


MS发送SETUP消息，携带被叫号码以及语音业务的承载信息。 


MSC Server发送ADD REQ消息到MGW，请求添加接入侧终端。 


MGW分配IP资源，返回ADD REPLY消息，消息中携带IP资源的地址和端口信息。 


MSC Server发送ASSIGNMENT REQUEST消息到BSC，进行指配，携带上述IP地址和端口。 


BSC发送RADIO BEARER SETUP消息到MS，分配无线信道。 


MS占用无线资源，返回RADIO BEARER SETUP COMPLETE消息。 


BSC发送ASSIGNMENT COMPLETE消息到MSC，返回指配应答，携带BSC侧选择的编解码以及用户面IP地址和端口号。 


MSC Server发送MOD REQ消息到MGW，携带BSC分配的IP地址和端口。 


MSC Server返回MOD REPLY。 


MGW发送NTFY REQ消息到MSC Server，上报BSC侧承载建立完成。 


MSC Server返回NTFY REPLY消息。 


锚定流程


MSC Server发送MAP_SEND_ROUTING_INFORMATION_REQ消息到HLR/HSS，请求获取被叫用户的漫游号码。 


HLR/HSS查询被叫用户UE的签约数据，判断签约数据中包含终结CAMEL签约信息T-CSI，在MAP_SEND_ROUTING_INFORMATION_CNF消息将T-CSI返回给MSC
Server。 


MSC Server触发T-CSI业务逻辑，发送IDP（Initial Detection Point）消息到SCP，这里SCP是Anchor
AS网元。 


Anchor AS判断该IDP（Initial Detection Point）触发被叫锚定，分配IMRN号码（在原来的被叫号码前增加前缀），发送Connect消息到MSC
Server，其中Destination Routing Address参数携带IMRN号码。 


MSC Server再次发送ADD REQ消息，请求添加核心网侧终端。 


MGW动态分配IP资源，返回ADD REPLY消息。 


MGW发送NTFY REQ消息到MSC Server，上报隧道指示事件，携带隧道信息。 


MSC Server返回NTFY REPLY应答消息。 


MSC Server分析IMRN的路由，发送IAM消息到MGCF，携带上述隧道信息。 


MGCF发送ADD REQ消息到IM-MGW，请求建立被叫侧终端。 


IM-MGW分配IP资源，返回ADD REPLY消息。 


MGCF分析IMRN的路由，发送INVITE消息到I-CSCF。出局前，MGCF删除锚定前缀，将被叫号码规整为全局号码格式。 


被叫信令流程（包括域选择）


I-CSCF收到INVITE消息后，向HLR/HSS发送LIR消息，请求获取S-CSCF地址。 


HSS返回LIA消息给I-CSCF，消息中携带S-CSCF的地址。 


I-CSCF发送 INVITE消息给S-CSCF。S-CSCF根据被叫用户签约的iFC数据，发送INVITE消息给VoLTE
AS，触发业务给VoLTE AS。 


VoLTE AS发送UDR消息给HLR/HSS，获取被叫用户的T-ADS信息。 


HLR/HSS发送IDR消息给MME，查询被叫用户的T-ADS信息。 


MME发送IDA消息给HLR/HSS，返回被叫用户的T-ADS信息。 


HSS发送UDA消息给VoLTE AS，返回被叫用户的T-ADS信息。 


VoLTE AS根据T-ADS信息，域选到IMS网络，发送INVITE给S-CSCF。 


S-CSCF发送INVITE消息给用户注册的P-CSCF。 


P-CSCF从INVITE消息中获得主叫用户的媒体信息，通过AAR消息发送给PCRF，要求PCRF建立专有承载。 


PCRF向P-CSCF发送AAA响应。 


P-CSCF发送INVITE消息给UE。 


被叫UE返回183响应，在SDP中携带SDP Answer信息。 


被叫承载面建立


P-CSCF收到被叫侧返回的183响应后，发送AAR消息给PCRF，AAR中携带UE的媒体信息和媒体资源预留成功指示。 


PCRF根据获取的业务媒体信息进行策略决策，提供授权的QoS,用于承载资源预留，之后使用RAR消息携带Charing-Rule-Install
AVP，把相应的授权的QoS（包括QCI/ARP/GBR/MBR等信息），发送至P-GW。 


P-GW收到RAR后，发送RAA响应消息给PCRF。 


PCRF根据P-GW返回的RAA消息，向P-CSCF发送AAA响应消息，返回授权请求结果。 


P-GW收到消息RAR，发送 Create Bearer Request消息给MME，指示MME建立专有承载。 


MME收到Create Bearer Request消息后，发送Activate dedicated EPS bearer
context request消息给被叫UE，请求激活一个专有EPS承载上下文。 


UE向被叫MME发送Activate dedicated EPS bearer context accept消息，确认激活一个专有EPS承载上下文。 


被叫MME向P-GW发送Create Bearer Response消息，确认专有承载已经建立。 


P-GW发送CCR消息给PCRF，通知资源预留成功。 


PCRF发送CCA响应消息给P-GW。 


PCRF接收到P-GW的资源预留成功事件上报，发送RAR消息给P-CSCF，通知承载建立情况。 


P-CSCF发送RAA响应消息给PCRF。 


P-CSCF向S-CSCF发送183消息，在SDP中携带UE的媒体信息。 


S-CSCF发送183消息给VoLTE AS。 


VoLTE AS发送183消息给S-CSCF。 


S-CSCF发送183消息给I-CSCF，I-CSCF转发183消息给MGCF。 


主叫承载修改流程


MGCF收到183消息，发送MOD REQ消息到IM-MGW，修改到IMS一侧的承载信息。 


IM-MGW返回MOD REPLY消息。 


MGCF发送ADD REQ消息到IM-MGW，请求建立MSC Server侧终端。 


M-MGW动态分配IP资源，返回ADD REPLY消息。 


MGCF发送MOD REQ消息到IM-MGW，将隧道信息传递到IM-MGW。 


IM-MGW返回MOD REPLY消息。 


IM-MGW发送NTFY REQ消息到MGCF，携带被叫侧隧道信息。 


MGCF返回NTFY REPLY应答消息。 


MGCF发送APM消息到MSC Server，携带上述被叫侧隧道信息。 


MSC Server收到APM消息，发送MOD REQ到MGW，将隧道信息传递到MGW。 


MGW返回MOD REPLY消息。 


MGW发送TRC_IU/NB_UP_INIT_TOIP消息到IM-MGW，进行NB_UP初始化。 


IM-MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，上报承载建立完成。 


MSC Server返回NTFY REPLY消息。 


IM-MGW发送NTFY REQ消息到MGCF，上报承载建立完成。 


MGCF返回NTFY REPLY消息。 


MGCF发送183的PRACK消息给S-CSCF。 


S-CSCF发送PRACK给VoLTE AS。 


VoLTE AS发送PRACK给S-CSCF。 


S-CSCF发送PRACK给P-CSCF。 


P-CSCF发送PRACK给UE。 


被叫UE发送PRACK的200 OK消息给P-CSCF。 


P-CSCF发送PRACK的200 OK消息给S-CSCF。 


S-CSCF发送PRACK的200 OK消息给VoLTE AS。 


VoLTE AS发送PRACK的200 OK消息给S-CSCF。 


S-CSCF发送PRACK的200 OK消息给MGCF。 


被叫UE振铃，发送180消息给P-CSCF。 


P-CSCF发送180消息给S-CSCF。 


S-CSCF发送180消息给VoLTE AS。 


VoLTE AS发送180消息给S-CSCF。 


S-CSCF发送180消息给I-CSCF，I-CSCF发送180消息给MGCF。 


MGCF发送MOD REQ消息到IM- MGW，要求MGW播放回铃音。 


MGW播放回铃音，返回MOD REPLY消息。 


MGCF发送ACM（Address Complete Message）消息到MSC Server。 


MSC Server发送Alerting消息到主叫MS。 


MGCF发送180的PRACK消息给S-CSCF。 


S-CSCF发送180的PRACK消息给VoLTE AS。 


VoLTE AS发送180的PRACK消息给S-CSCF。 


S-CSCF发送180的PRACK消息给P-CSCF。 


P-CSCF发送180的PRACK消息给UE。 


被叫UE发送PRACK的200 OK消息给S-CSCF。 


P-CSCF发送PRACK的200 OK消息给S-CSCF。 


S-CSCF发送PRACK的200 OK消息给VoLTE AS。 


VoLTE AS发送PRACK的200 OK消息给S-CSCF。 


S-CSCF发送PRACK的200 OK消息给MGCF。 


被叫摘机，UE发送INVITE请求的200 OK消息给P-CSCF。 


P-CSCF发送INVITE请求的200 OK消息给S-CSCF。 


S-CSCF发送INVITE请求的200 OK消息给VoLTE AS。 


VoLTE AS发送INVITE请求的200 OK消息给S-CSCF。 


S-CSCF发送INVITE请求的200 OK消息给MGCF。 


MGCF发送MOD REQ消息到IM- MGW，要求MGW停止播放回铃音。 


MGW停止播放回铃音，返回MOD REPLY消息。 


MGCF发送ANM消息到MSC Server。 


MGCF发送ACK消息给给S-CSCF。 


S-CSCF发送ACK消息给VoLTE AS。 


VoLTE AS发送ACK消息给S-CSCF。 


S-CSCF发送ACK消息给P-CSCF。 


P-CSCF发送ACK消息给UE。 


MSC Server发送CONNECT消息到主叫MS，通知主叫用户被叫应答。 


主叫MS返回CONNECT ACK消息。 


挂机释放流程


主叫用户挂机，发送DISCONNECT消息到MSC Server。 


MSC Server返回RELEASE消息。 


MS发送RELEASE COMPLETE消息到MSC Server。 


MSC Server发送CLEAR COMMAND消息到BSC。 


BSC清除无线接口和A接口资源，返回CLEAR COMPLETE消息。 


MSC Server发送SUB REQ消息到MGW，释放主叫接入侧终端资源。 


MGW返回SUB REPLY消息。 


MSC Server发送REL消息到MGCF。 


MGCF发送SUB REQ消息到IM-MGW，释放主叫侧终端资源。 


IM-MGW返回SUB REPLY消息。 


MGCF发送RLC消息到MSC Server。 


MSC Server发送SUB REQ消息到MGW，释放主叫核心网侧终端。 


MGW返回SUB REPLY消息。 


MGCF发送BYE消息给S-CSCF。 


S-CSCF发送BYE消息给VoLTE AS。 


VoLTE AS发送BYE消息给S-CSCF。 


S-CSCF发送BYE消息给P-CSCF。 


P-CSCF发送BYE消息给UE。 


UE接收到BYE消息后，向P-CSCF发送200响应消息。 


P-CSCF向PCRF发送STR消息，释放承载会话。 


PCRF发送RAR消息给P-GW，通知删除专有承载。 


P-GW发送RAA消息给PCRF。 


PCRF发送STA消息给P-CSCF。 


P-GW发送Delete Bearer Request消息到MME，指示删除专有承载。 


MME向被叫UE发送Deactivate EPS bearer context request消息，请求释放专有EPS承载上下文。 


UE向被叫MME发送Deactivate dedicated EPS bearer context accept消息，确认释放专有EPS承载上下文。 


MME发送Delete Bearer Response消息给P-GW，指示专有承载已删除。 


P-CSCF发送200OK响应消息给S-CSCF。 


S-CSCF发送200 OK消息给VoLTE AS。 


VoLTE AS发送200 OK消息给S-CSCF。 


S-CSCF发送200 OK消息给MGCF。 


MGCF发送SUB REQ消息到IM-MGW，释放被叫侧终端资源。 


IM-MGW返回SUB REPLY消息。 




## SRVCC/eSRVCC 
### 注册流程 
### 注册流程 


业务模型 :本流程的业务模型如下： 

 
签约SRVCC/eSRVCC业务的UE附着到EPC网络后，发起注册到IMS网络。 

 
IMS APN和数据APN采用独立的APN，IMS APN为缺省APN。 

 
中兴VoLTE SBC支持SBC/P-CSCF/ATCF/ATGW合一。 

 
UE通过EPC网络注册到IMS网络的过程可以分为如下几个阶段。 

 
UE附着到EPC网络附着流程是用户注册到EPS网络上的流程，是用户开机后的第一个过程，是后续所有的流程的基础。在附着过程中，EPC网络会为用户建立一个默认承载，也可以对用户进行鉴权（用户首次附着到EPS网络上必须鉴权）。如果IMS业务APN（Access
Point Name）和数据业务APN采用独立的APN，则附着流程完成之后，EPC网络就建立了数据APN缺省承载，用户可以通过EPS网络访问数据业务。UE再发起PDN连接请求，EPC网络为其建立IMS
APN默认承载。 

 
UE注册到IMS网络UE注册到IMS网络包括基本注册和第三方注册。基本注册过程中，UE主动发起注册，IMS网络与UE进行双向鉴权，通常采用IMS
AKA或者SIP Digest鉴权方式，鉴权通过后，S-CSCF从IMS HSS下载到用户数据，基本注册完成。第三方注册过程中，S-CSCF根据用户数据中的iFC触发到AS的注册，AS从IMS
HSS下载到UE的业务数据后，第三方注册完成。eSRVCC中引入了ATCF网元，注册请求经过ATCF时需要插入STN-SR等关键参数，以便后续切换使用。 

 


信令流程 :SRVCC/eSRVCC注册流程如[图1](11-%E6%B3%A8%E5%86%8C%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__SRVCCeSRVCC%E6%B3%A8%E5%86%8C%E6%B5%81%E7%A8%8B-C6B587F1)所示。
图1  SRVCC/eSRVCC注册流程


[]images/img-0013541651(%E9%87%8D%E7%94%A81).png)

EPC附着流程


UE通过eNodeB向MME发起附着请求Attach Request，其中MS Network Capability信元会指示终端是否支持SRVCC。 


MME检查Attach Request消息，判决需要对用户鉴权（比如消息完整性保护失败、MME启动附着强制鉴权等），同时MME没有此用户可用的鉴权向量信息，则MME向融合HLR/HSS发送AIR（Authentication
Information Request）消息，请求鉴权数据，消息中携带user-name信元，表示用户的IMSI；否则，流程从第6步开始。 


融合HLR/HSS向MME返回AIA消息，消息中携带用户的四元组鉴权向量，包括XRES（Expected Response）、RAND（Random
Challenge）、AUTN（Authenticaiton Token）、KASME。 


MME收到AIA消息后，向UE发送Authentication Request消息，对UE发起鉴权请求。消息中包含：RAND、AUTN、KSIasme。 


如果UE鉴权成功，则会根据RAND计算出RES并通过Authentication Response返回给MME。MME使用鉴权向量组中的XRES和UE返回的RES（Response）比较，相同则鉴权成功，否则鉴权失败并向UE发送Authentication
Reject消息。 


EPC网络对终端的USIM卡完成鉴权流程后，如果从UE上次分离后MME改变了，或MME没有UE的有效的签约上下文，或IMEI改变，则MME向融合HLR/HSS发送ULR消息，获取用户信息，消息中携带UE-SRVCC-Capability信元：指示UE是否支持SRVCC能力，消息中携带Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions信元：指示EPC网络是否支持IMS语音业务。 


融合HLR/HSS向MME发送ULA消息，向MME插入签约数据，包括默认APN，一个或多个PDN（Packet Data
Network）签约上下文。如果IMS业务APN和数据业务APN采用独立的APN，则这里默认APN是数据业务APN。 


MME根据APN FQDN查询DNS配置，再结合S-GW POOL和P-GW POOL的网络拓扑选择S-GW和P-GW，向S/P-GW发送Create
Session Request消息，请求建立数据APN缺省承载。S-GW缓存任何从PDN GW接收的下行分组数据，直到收到第14步的修改承载请求消息，在这之前不能发送下行数据通知消息给MME。 


P-GW收到Create Session Request消息后，执行IP-CAN会话建立流程，即PGW向PCRF发送CCR信用控制请求消息，获取UE的缺省PCC规则。 


PCRF根据SPR的签约信息、PGW上报的网络信息和PCRF的本地配置信息进行策略决策，对数据APN的PDN连接的请求进行EPS默认承载的QoS授权，并使用信用控制应答消息CCA下发授权的QoS信息给PGW。消息里携带Default-EPS-Bearer-QoS
AVP，其QCI根据需要设置。 


S/P-GW向MME返回Create Session Response消息，其中携带QCI信元，指示建立数据APN缺省承载已完成。 


MME根据缺省APN的签约APN-AMBR和签约UE-AMBR确定UE-AMBR，通过eNodeB向UE发送Attach
Accept消息，如果MME分配了新的GUTI，则消息中包含GUTI。 


UE通过eNodeB发送Attach Complete消息给MME。 


MME收到后发送Modify Bearer Request消息给S/P-GW，消息中携带无线侧的TEID和地址。 


S/P-GW根据下行TEID和地址通过所建立的缺省承载立即开始给UE传送数据包，并给MME回复Modify Bearer
Response消息。 


如果IMS业务APN和数据业务APN采用独立的APN，则附着流程完成之后，EPC网络就建立了数据APN缺省承载，用户可以通过EPS网络访问数据业务。UE再发起PDN连接请求，消息中携带IMS
APN名称，EPC网络为其建立IMS APN默认承载。 


MME向S/P-GW发送Create Session Request消息，消息中携带IMSAPN名称和IMS APN的QCI，请求建立IMSAPN默认承载。 


P-GW收到Create Session Request消息后，执行IP-CAN会话建立流程，即PGW向PCRF发送CCR信用控制请求消息，获取UE的PCC规则。 


PCRF根据SPR的签约信息、PGW上报的网络信息和PCRF的本地配置信息进行策略决策，对IMS APN的PDN连接的请求进行EPS默认承载的QoS授权，并使用信用控制应答消息CCA下发授权的QoS信息给PGW。消息里携带Default-EPS-Bearer-QoS
AVP，其QCI根据需要设置。 


S/P-GW向MME返回Create Session Response消息，消息中携带关键信元PCO和QCI，指示建立IMS信令默认承载已完成，其中PCO包含P-CSCF的地址。 


IMS注册流程


UE先读取USIM卡信息获取IMSI，再从IMSI推导出IMPI和T-IMPU，向IMS拜访网络入口P-CSCF发送REGISTER消息请求注册。注册请求中包含PUI、PVI、CONTACT等关键信息。 


P-CSCF/ATCF根据Request-URI头域中域名查询DNS服务器，获得归属域网络入口I-CSCF网元地址，向I-CSCF转发REGISTER消息。Feature-Caps:
P-CSCF/ATCF在REGISTER消息中插入该消息头，将当前ATCF分配的STN-SR号码带给IMS网络。 


I-CSCF收到REGISTER消息后，做如下处理： 

 
I-CSCF根据Request-URI中的域名，判断是否在信任域或本地域。 

 
对于本域用户，向IMS HSS发送UAR消息，请求获取S-CSCF的地址或者能力集。 

 


IMS HSS收到UAR消息，根据本地数据库中的用户开户信息，判断用户已开户，则向I-CSCF发送UAA响应，返回S-CSCF的地址或者能力集。 

 
当UAA消息中携带Server-Name时，表示携带的为S-CSCF的地址。 

 
当UAA消息中携带Server-Capabilities时，表示携带的为S-CSCF的能力集。 

 


I-CSCF根据IMS HSS返回的S-CSCF地址，向S-CSCF转发REGISTER消息。S-CSCF向IMS HSS发送MAR消息，请求获取认证向量AV（Authorization
Vector）。同时融IMS HSS记录当前S-CSCF主机名，保证401鉴权挑战消息之后的REGISTER消息能够到达同一个SCSCF。 


IMS HSS向S-CSCF返回MAA响应，包括鉴权五元组XRES（Expected Response）、RAND（Random
Challenge）、AUTN（Authentication Token）、IK（Integrity Key）和CK（Cipher
Key）。 


S-CSCF根据RAND和AUTN生成nonce，并将nonce同IK、CK、以及鉴权算法放到WWW-Authenticate头域中，随401响应返回给P-CSCF。同时，S-CSCF保存参数XRES，以备后续对用户的鉴权响应进行验证。 


P-CSCF从消息中取出IK和CK并保存，将消息中剩余的鉴权元素RAND和AUTN继续向UE转发。 


UE收到401响应后，根据本地ISIM（IMS Subscriber Identity Module）中保存的共享密钥对AUTN进行认证，实现对归属网络的认证。再基于共享密钥和RAND计算出RES（Response），重新构造REGISTER消息，携带RESPONSE，按照初始REGISTER消息的路径发给P-CSCF。 


P-CSCF按照初始REGISTER消息的路径发送后续REGISTER给I-CSCF。 


I-CSCF收到REGISTER消息后，发送UAR，查询HSS得到服务的S-CSCF主机名。 


IMS HSS收到UAR消息后，将之前记录的S-CSCF的地址信息通过UAA消息发送给I-CSCF。 


S-CSCF收到鉴权响应，本地通过MD5算法计算得到response，并与第二条注册请求中的response进行比较。如果两者匹配，则该UE通过网络鉴权。鉴权通过后，S-CSCF向IMS
HSS发送SAR消息，请求下载用户的签约数据。 


IMS HSS向S-CSCF返回SAA响应，携带用户的签约数据，包括隐式注册集、ifcs、计费功能地址等信息。 


S-CSCF向UE侧返回200响应，表明初始注册成功。 


S-CSCF根据从IMS HSS处下载的用户签约信息，判断其中有针对REGISTER请求的iFC（initial Filter
Criteria）数据，S-CSCF根据iFC中VoLTE AS地址，向VoLTE AS发送第三方注册请求。如果用户签约信息中包含多条针对REGISTER请求的iFC数据，S-CSCF会根据优先级从高到低依次发送给iFC中的VoLTE
AS地址。同时S-CSCF还支持根据签约，携带UE发起的注册请求和注册成功响应消息。 


AS发现用户为第一次注册，发送SNR消息给IMS HSS，请求获取用户数据（包括用户身份数据、业务签约数据等）并对用户数据进行订阅。 


IMS HSS向AS返回SNA响应，携带用户数据。针对eSRVCC，HSS根据UDR请求，将返回STN-SN以及MS-ISDN等信息。 


AS向S-CSCF返回第三方注册的200成功响应。  


AS向I/S-CSCF发送Message请求，请求消息中携带用户的ATU-STI号码、C-MSISDN号码。 


I/S-CSCF根据Request-URI通过LIR/LIA消息查询融合HLR/HSS或根据本地PSI数据配置，查询ATCF的地址，根据查询结果将MESSAGE消息路由到ATCF。 


ATCF返回200 OK响应给I-CSCF，表示已成功接收MESSAGE消息。 


I/S-CSCF将200 OK响应转发给VoLTE AS。 


VoLTE AS根据下载的STN-SR号码判断是否需要向融合HLR/HSS发送PUR消息更新STN-SR号码。 VoLTE
AS根据第三方注册的REGISTER消息是否携带ATCF分配的STN-SR号码，进行以下处理： 

 
如果REGISTER消息中携带了STN-SR号码，并且该号码与从IMS HSS下载的STN-SR号码不相同，则通过PUR消息将STN-SR号码携带给融合HLR/HSS，由融合HLR/HSS替换本地的STN-SR号码。 

 
如果REGISTER消息中未携带STN-SR号码，则VoLTE AS将本地配置的STN-SR号码与融合HLR/HSS之前返回的STN-SR号码进行比较，如果不相同，则通过PUR消息将本地配置的STN-SR号码携带给融合HLR/HSS，由融合HLR/HSS替换本地的STN-SR号码。 

 
如果REGISTER消息中携带了STN-SR号码，并且融合HLR/HSS上没有配置STN-SR号码，则VoLTE AS通过PUR将REGISTER消息中携带的STN-SR号码携带给融合HLR/HSS。 

 
如果REGISTER消息中未携带STN-SR号码，并且融合HLR/HSS上没有配置STN-SR号码，则VoLTE AS将本地配置的STN-SR号码携带给融合HLR/HSS。 

 
其他情况下，VoLTE AS无需向融合HLR/HSS发送PUR消息。 

 


融合HLR/HSS返回成功接收响应PUA。 


融合HLR/HSS判断消息中携带的STN-SR号码与本地保存的STN-SR号码不一致，则将消息中携带的STN-SR号码通过Insert
Subscriber Data Request发送给MME。 


MME更新本地的STN-SR号码后，向融合HLR/HSS返回成功更新Insert Subscriber Data Answer响应。后续切换MME需要使用本地的STN-SR参数。 




### 呼叫流程 
### 呼叫流程 


业务模型 :本流程的业务模型如下： 

 
签约SRVCC/eSRVCC业务的主被叫LTE用户已注册到IMS网络。 

 
签约SRVCC/eSRVCC业务的LTE用户通过LTE网络发起呼叫，被叫域选为LTE网络。 

 


信令流程 :SRVCC/eSRVCC呼叫流程如[图1](12-%E5%91%BC%E5%8F%AB%E6%B5%81%E7%A8%8B%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__SRVCCeSRVCC%E5%91%BC%E5%8F%AB%E6%B5%81%E7%A8%8B-C6BEA214)所示。
图1  SRVCC/eSRVCC呼叫流程


[]images/img-0013541703(%E9%87%8D%E7%94%A81).png)

主叫信令面流程


UE_A向IMS拜访网络入口P-CSCF/ATCF_A发送INVITE消息向被叫发起会话。INVITE消息中包含了主、被叫号码、主叫联系地址等关键信息。 


2 P-CSCF/ATCF_A从INVITE消息中获得主叫UE_A会话信息，将用户的信令地址、媒体带宽等信息通过AAR消息发送给PCRF_A，同时请求中还会请求接入网络位置信息。 


PCRF_A向P-CSCF/ATCF_A发送认证/授权应答消息AAA响应，响应消息中携带接入网络类型。具体的接入网络信息（如CELL-ID）通过RAR/RAA获得。 


P-CSCF/ATCF_A收到INVITE消息后，根据INVITE消息中携带的+g.3gpp.mid-call和+g.3gpp.srvcc-alerting标识判断需要锚定此会话，并进行本端媒体资源预留。P-CSCF/ATCF_A收到AAA之后，将INVITE请求发送给S-CSCF_A。 


S-CSCF_A收到INVITE消息，判断P-Asserted-Identity头域中的主叫号码已注册，则根据主叫用户签约的iFC模板数据，触发VoLTE
AS_A，即发送INVITE请求到VoLTE AS_A。 


VoLTE AS_A向主叫UE_A提供语音业务后，发送INVITE消息到S-CSCF_A。 


S-CSCF_A使用被叫号码B，查询ENUM/DNS，获取下一跳路由地址。 


ENUM/DNS根据被叫号码B解析出被叫归属域入口I-CSCF的IP地址，将其返回给S-CSCF_A。 


S-CSCF_A将INVITE消息发送到被叫I-CSCF_B。 


被叫信令面流程（T-ADS域选）


I-CSCF_B向融合HLR/HSS发送LIR消息，请求获取UE_B注册的S-CSCF_B地址。 


融合HLR/HSS收到LIR消息后，根据本地数据库中的用户注册信息，查看被叫用户的S-CSCF_B地址，则向I-CSCF_B发送LIA消息，提供S-CSCF_B的服务器地址。 


S-CSCF_B将收到INVITE消息后，根据iFC模板数据，向VoLTE AS_B发送INVITE消息触发被叫业务和被叫网络域选。 


VoLTE AS_B先执行被叫侧业务，向融合HLR/HSS发送UDR消息，请求获取被叫用户的T-ADS信息。 


融合HLR/HSS通过IDR消息向MME_B查询被叫用户的T-ADS信息。 


MME_B将查询的结果通过IDA消息向融合HLR/HSS发送被叫用户的T-ADS信息，IDA返回Last-UE-Activity-Time,RAT-Type,
IMS Voice Over PS Sessions Support Indicator。 


融合HLR/HSS向VoLTE AS_B返回UDA响应，携带T-ADS信息。 


融合VoLTE AS_B基于获取的T-ADS信息，判断当前域选到IMS网络。VoLTE AS_B确定被叫域选的网络后，通过INVITE消息指示S-CSCF_B将呼叫接续到特定网络。 


S-CSCF_B查询本地保存的被叫用户注册的P-CSCF/ATCF_B地址，将呼叫请求通过INVITE消息发送到P-CSCF/ATCF_B。 


P-CSCF/ATCF_B从INVITE消息中获得主叫UE_A会话信息，将这些信息通过认证/授权请求消息AAR消息发送给PCRF_B，通知PCRF_B建立承载。 


PCRF_B向P-CSCF/ATCF_B发送认证/授权应答消息AAA响应。 


P-CSCF/ATCF_B根据INVITE消息中携带+g.3gpp.srvcc标识判断需要锚定此会话，则进行本端媒体资源预留，通过INVITE消息将呼叫请求接续到UE_B。 


被叫承载面建立


被叫UE_B收到INVITE消息，进行相应的处理，终端返回18x响应（此处以180临时响应为例）。 


P-CSCF/ATCF_B收到被叫侧返回的180(SDP，RINGING）下发认证/授权请求消息AAR消息给PCRF_B开始建立专有承载。AAR包括用户媒体描述的信息。 


 PCRF_B根据认证/授权请求消息AAR消息中携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求消息RAR消息将QoS（QCI/ARP/GBR/MBR）和PCC规则发送至P-GW_B。 


 P-GW_B收到重新认证/授权请求消息RAR，上报重新认证/授权应答消息RAA响应给PCRF_B。 


PCRF_B根据P-GW_B返回的重新认证/授权应答消息RAA消息，给P-CSCF/ATCF_B通过认证/授权应答消息AAA响应授权请求结果消息。 


P-GW_B收到重新认证/授权请求消息RAR，同时通过Create Bearer Request指示MME_B建立专有承载。  


MME_B收到Create Bearer Request消息后，向被叫UE_B发送Activate dedicated
EPS bearer context request消息，用于请求激活一个专有EPS承载。 


UE_B向被叫MME_B发送Activate dedicated EPS bearer context accept消息，用于确认激活一个专有EPS承载上下文。 


P-GW_B收到Create Bearer Response消息，确认专有承载已经建立。 


P-GW_B向PCRF_B发送信用控制请求消息CCR-U消息，通知资源预留成功。 


PCRF_B向P-GW_B返回信用控制应答消息CCA-U响应。 


当PCRF_B收到P-GW_B的资源预留成功事件上报时，向P-CSCF/ATCF_B发送重新认证/授权请求消息RAR消息，通知承载建立情况。 


P-CSCF/ATCF_B向PCRF_B返回重新认证/授权应答消息RAA消息，被叫承载面建立完成。 


主叫承载面建立


P-CSCF/ATCF_B先将180响应转发至VoLTE AS_B，VoLTE AS_B通过VoLTE AS_A发送到P-CSCF/ATCF_A，其中SDP
answer中携带媒体响应信息。 


P-CSCF/ATCF_A收到被叫侧返回的180（SDP，RINGING）消息后，下发认证/授权请求消息AAR消息给PCRF_A开始建立专有承载。AAR包括用户媒体信息。 


PCRF_A根据认证/授权请求消息AAR消息中携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求消息RAR消息将QoS（QCI、ARP、GBR和MBR）和PCC规则发送至P-GW_A。 


P-GW_A收到重新认证/授权请求消息RAR，上报重新认证/授权应答消息RAA响应给PCRF_A。 


PCRF_A根据P-GW_A返回的重新认证/授权应答消息RAA消息，给P-CSCF/ATCF_A通过认证/授权应答消息AAA响应授权请求结果消息。 


P-GW_A收到重新认证/授权请求消息RAR，通过Create Bearer Request指示MME_A建立专有承载。 


MME_A收到Create Bearer Request消息后，向主叫UE_A发送Activate Dedicated
EPS Bearer Context Request消息，用于请求激活一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Activate Dedicated EPS Bearer Context Accept消息，用于确认激活一个专有EPS承载上下文。 


P-GW_A收到Create Bearer Response消息，确认专有承载已经建立。 


P-GW_A向PCRF_A发送信用控制请求消息CCR-U消息，通知资源预留成功。 


PCRF_A向P-GW_A返回信用控制应答消息CCA-U响应。 


当PCRF_A收到P-GW_A的资源预留成功事件上报时，向P-CSCF/ATCF_A发送重新认证/授权请求消息RAR消息，通知承载建立已成功。 


P-CSCF/ATCF_A向PCRF_A返回重新认证/授权应答消息RAA消息。 


P-CSCF/ATCF_A将180响应转发至主叫UE_A 。 


被叫网络收到主叫网络发送的PRACK请求，表示主叫网络成功接收180响应，并且已完成资源预留。 


被叫UE_B返回针对PRACK请求的200响应，表示成功接收PRACK请求。 


被叫用户接听电话，被叫UE_B向主叫网络返回针对INVITE请求的200(INVITE)响应。 


当VoLTE AS_B收到200(INVITE)消息后，开始向CCF发送ACR [Start]消息。 


CCF收到正确的ACR [Start]消息后，将其保存，创建被叫AS CDR，并向VoLTE AS_B发送计费响应消息ACA。 


VoLTE AS_B向主叫VoLTE AS_A转发200(INVITE)消息。 


当VoLTE AS_A收到200(INVITE)消息后，开始向CCF发送ACR [Start]消息。 


CCF收到正确的ACR [Start]消息后，将其保存，创建主叫AS CDR，并向VoLTE AS_A发送计费响应消息ACA。 


VoLTE AS_A收到200 OK后，将200(INVITE)响应消息到主叫UE_A。 


主叫UE_A向被叫网络返回针对200(INVITE)响应的ACK确认消息，主叫UE_A和被叫UE_B成功建立会话。A和B用户之间可以通话。 


挂机释放流程


A和B通话结束后，UE_A主动发送BYE消息。 


当VoLTE AS_A收到BYE消息后，开始向CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS_A发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


VoLTE AS_A将BYE消息透传到被叫的VoLTE AS_B。 


当被叫VoLTE AS_B收到BYE消息后，开始向CCF发送ACR [Stop]消息。 


CCF收到正确的ACR [Stop]消息后，将其保存，向VoLTE AS_B发送计费响应消息ACA。并将本次会话的所有ACR进行合并，输出一张完整的CDR并将此CDR传送到计费中心。 


VoLTE AS_B将BYE消息转发到被叫的UE_B。 


UE_B收到主叫侧的挂机请求后，向主叫侧发送200(BYE)响应消息。 


当被叫P-CSCF/ATCF_B收到200(BYE)响应后，向PCRF_B下发终止会话请求消息STR消息释放专有承载。 


PCRF_B发送重新认证/授权请求消息RAR消息通知P-GW_B删除专有承载，携带charging rule remove指示。 


P-GW_B返回重新认证/授权应答消息RAA给PCRF_B。 


PCRF_B返回终止会话应答消息STA响应给P-CSCF/ATCF_B。 


P-GW_B根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_B指示删除专有承载。 


MME_B收到Delete Bearer Request消息后，向被叫UE_B发送Deactivate EPS Bearer
Context Request消息，用于请求释放一个专有EPS承载上下文。 


UE_B向被叫MME_B发送Deactivate Dedicated EPS Bearer Context Accept消息，用于确认释放一个专有EPS承载上下文。 


P-GW_B收到Delete Bearer Response消息，专有承载已经完成删除。 


P-GW_B发送信用控制请求消息CCR-U消息给PCRF_B，指示专有承载已成功删除。 


PCRF_B给P-GW_B返回信用控制应答消息CCA-U消息予以确认。 


P-CSCF/ATCF_B发送200(BYE)给P-CSCF/ATCF_A。 


当主叫P-CSCF/ATCF_A收到200 (BYE)消息后，向PCRF_A下发终止会话请求消息STR消息释放承载会话。 


PCRF_A发送重新认证/授权请求消息RAR消息通知P-GW_A删除专有承载，携带charging rule remove指示。 


P-GW_A返回重新认证/授权应答消息RAA给PCRF_A。 


PCRF_A返回终止会话应答消息STA响应给P-CSCF/ATCF_A。 


P-GW_A根据指示删除相关的规则，释放承载会话，并发送Delete Bearer Request消息到MME_A指示删除专有承载。 


MME_A收到Delete Bearer Request消息后，向主叫UE_A发送Deactivate EPS Bearer
Bontext Request消息，用于请求释放一个专有EPS承载上下文。 


UE_A向主叫MME_A发送Deactivate Dedicated EPS Bearer Context Accept消息，用于确认释放一个专有EPS承载上下文。 


P-GW_A收到Delete Bearer Response消息，专有承载已经完成删除。 


P-GW_A发送信用控制请求消息CCR消息给PCRF_A，指示专有承载已成功删除。 


PCRF_A给P-GW_A返回信用控制应答消息CCA消息予以确认。 


P-CSCF/ATCF_A发送200 (BYE)消息给UE_A，通话结束。 




### 切换流程 
#### 单路语音呼叫切换（Active状态） 
#### 单路语音呼叫切换（Active状态） 


业务模型 :本流程业务模型如下： 

 
签约eSRVCC业务的主叫LTE用户通过LTE网络发起呼叫，被叫域选网络为LTE网络，当主叫用户和被叫用户正在进行通话时，主叫用户从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 

 
VoLTE SBC兼做P-CSCF、ATCF和ATGW，VoLTE SBC需要配置支持ATCF功能。 

 
VoLTE AS已支持SRVCC/eSRVCC功能。 

 
数据库部署形态为融合HLR/HSS，即HLR、SAE-HSS和IMS-HSS合一部署。 

 


信令流程 :签约eSRVCC业务的主叫LTE用户通过LTE网络发起呼叫，被叫域选网络为LTE网络，当主叫用户和被叫用户正在进行通话时，主叫用户从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换，具体的语音切换流程如[图1](13-%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88Active%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Active%E7%8A%B6%E6%80%81-B6BF2153)所示。
图1  单路语音呼叫切换（Active状态）


[]images/img-0013378151(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带IP终端的IP地址和端口等信息。 


ATCF新建媒体端点流程


eMSC根据STN-SR进行路由，向P-CSCF/ATCF_A发送eSRVCC切换请求INVITE消息，携带本端SDP信息。 
关键信元如下： 

 
Request URI：STN-SR号码。取值源自MME发送给eMSC的切换请求PS to CS Request消息。 

 
P-Asserted-Identity头域：C-MSISDN号码。取值源自MME发送给eMSC的切换请求PS to CS
Request消息。 

 


eMSC返回PS to CS Response消息到MME_A，通知手机可以接入到UMTS。 


P-CSCF/ATCF_A收到INVITE消息，根据其中STN-SR号码，判断该消息是由eSRVCC切换产生。P-CSCF/ATCF_A作如下处理： 

 
P-CSCF/ATCF_A从INVITE消息中获取C-MSISDN，结合本地保存的+g.3gpp.srvcc标识、eSRVCC相关信息（ATU-STI等），确定UE_A需要切换的Active状态会话。 

 
P-CSCF/ATCF_A进行媒体协商修改，在ATGW新建媒体端点，与eMSC侧MGW的媒体端点完成连接。 

 
P-CSCF/ATCF_A向eMSC返回200 OK消息，携带本端新建端点的SDP信息。 

 


eMSC发送ACK消息给P-CSCF/ATCF_A。 


eMSC根据200消息中的承载信息通过MOD REQ消息下发给主叫IM-MGW。 


IM-MGW向eMSC发送MOD REPLY消息，返回修改终结点属性命令的响应。 


CS网络位置更新


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


MSC Server通过局间MAP信令发送MAP SEND END SIGNAL REQ消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA REQ插入用户数据。 


VLR返回MAP INSERT SUBSCRIBER DATA RSP。 


HLR/HSS返回 MAP UPDATE LOCATION CNF应答消息。 


接入域修改


P-CSCF/ATCF_A根据待切换会话关联的ATU-STI，向VoLTE AS_A发送INVITE消息，请求eSRVCC切换。 
关键参数如下： 

 
Request-URI：待切换会话的ATU-STI。 

 
P-Asserted-Identity：UE的C-MSISDN号码。 

 
Require：携带tdialog标识，指示VoLTE AS支持Target-Dialog头域。 

 
Target-Dialog：待切换会话的原Dialog ID，包括原会话的Call-ID，远端设备用户实例（remote-tag），本端设备用户实例（local-tag）。 

 
SDP：UE的SDP，与原会话协商后的SDP相同。 

 


VoLTE AS_A收到INVITE消息后，通过其中Target-Dialog头域的原会话Call-ID确定待切换的会话，并作如下处理： 

 
如果该会话处于Active状态，且具有激活的语音媒体成分，则VoLTE AS比较INVITE消息中SDP的编解码是否与原会话协商后SDP的编解码相同，并根据比较结果启动eSRVCC流程或SRVCC流程。
如果相同，则VoLTE AS启动eSRVCC流程，修改该会话的接入域，表明用户已从CS域接入，便于后续业务进行域选择，并且返回200
OK消息。由于原会话协商SDP的编解码未改变，VoLTE AS不更新远端SDP。
如果不相同，则VoLTE AS启动SRVCC流程，修改会话接入域，返回200 OK消息，并且通过S-CSCF发送UPDATE消息给UE_B，更新远端SDP。
 

 
如果通过会话ID无法确定会话，则VoLTE AS返回480消息拒绝本次切换，并释放该用户所有会话。 

 


P-CSCF/ATCF_A向VoLTE AS_A返回ACK消息。UE_A与UE_B之间恢复媒体连接。后续UE_A所在网络侧媒体信息基于CS网络承载。 


释放原会话资源


切换成功后，VoLTE AS_A向P-CSCF/ATCF_A发送BYE消息，释放原会话媒体端点。 


P-CSCF/ATCF_A向VoLTE AS_A返回200响应消息。 


P-CSCF/ATCF_A向UE_A发送BYE请求，释放原会话资源。 


UE_A向P-CSCF/ATCF_A返回200响应消息。 




#### 单路语音呼叫切换（Hold状态） 
#### 单路语音呼叫切换（Hold状态） 


业务模型 :本流程业务模型如下： 

 
主叫LTE用户UE_A已签约eSRVCC业务，被叫用户UE_B为LTE用户。  

 
当UE_A和UE_B通话过程中，UE_A Hold UE_B。UE_A为Hold业务方，当前仅有这一个Hold状态会话。此时，UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 

 
数据库部署形态为融合HLR/HSS，即HLR，SAE-HSS和IMS-HSS合一部署。 

 
VoLTE SBC兼做P-CSCF/ATCF/ATGW网元。 

 


信令流程 :当UE_A和UE_B通话过程中，UE_A
Hold UE_B。UE_A为Hold业务方，当前仅有这一个Hold状态会话。此时，UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。具体的语音切换流程如[图1](14-%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88Hold%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Hold%E7%8A%B6%E6%80%81-B6C5BD97)所示。图1  单路语音呼叫切换（Hold状态）


[]images/img-0013375457(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A通话过程中移动至4G信号强度低于门限值地区，检测领区3G网络信息强度满足门限要求，上报系统测量报告至eNodeB_A,
eNodeB_A经过判断决定切换后，向MME_A发送切换请求Handover Required消息。 


MME_A向UE_A当前所在小区的eMSC发起eSRVCC切换请求PS to CS Request消息。 


eMSC通过MAP PREPARE HANDOVER REQ消息向MSC Server发起局间切换请求。 


MSC Server向MGW发送ADD REQ消息，请求添加BSC侧的IP终结点，并指示本次呼叫使用的编解码。 


MGW动态分配IP资源，向MSC Server回复ADD REPLY消息，该消息中返回终结点相关信息。 


MSC Server发送Handover Request消息给目标侧BSC，目标侧进行A接口资源和空口资源准备。 


BSC侧预留资源完成后，返回Handover Request Ack消息给MSC Server。其中携带BSC的媒体面IP地址和端口号。 


MSC Server发送MOD REQ消息，将BSC的媒体面IP地址和端口号通知到MGW。 


MGW接收媒体面IP地址和端口号，返回MOD REPLY消息。 


MGW发送NTF REQ消息到MSC Server,通知媒体面建立完成。 


MSC Server返回NTF REPLY应答。 


MSC Server发送MAP PREPARE HANDOVER CNF消息给eMSC，携带切换号码信元Handover
Number。 


eMSC向IM-MGW发送ADD REQ消息，请求添加到MSC Server一侧的IP终结点，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，向eMSC回复ADD REPLY消息，该消息中返回终结点信息。 


eMSC根据切换号码选择到MSC Server的路由，发送IAM消息到MSC Server。 


MSC Server向MGW发送ADD REQ消息，请求添加到eMSC一侧的IP终结点，并指示本次呼叫使用的编解码。 


MGW动态分配IP资源，向MSC Server回复ADD REPLY消息，该消息中返回IP地址等终结点相关信息。 


MSC Server发送APM消息给eMSC，选择编解码。 


eMSC向IM-MGW发送MOD REQ消息，指示IM-MGW上报隧道消息。 


IM-MGW向eMSC发送MOD REPLY消息，返回修改终结点属性命令的响应。 


IM-MGW向eMSC发送NTFY REQ消息，上报隧道指示。 


eMSC返回NTFY REPLY消息到IM-MGW。 


eMSC把隧道消息打包到APM消息中，发送给MSC Server。 


MSC Server向MGW发送MOD REQ消息，携带隧道信息。 


MGW返回MOD REPLY消息。 


MGW向MSC Server发送NTFY REQ消息，传送隧道请求接受消息。 


MSC Server向MGW发送NTFY REPLY消息。 


MSC Server把隧道消息打包到APM消息中，发送给eMSC。  


eMSC把APM消息中的隧道信息通过MOD REQ消息下发给IM-MGW。 


IM-MGW向eMSC发送MOD REPLY消息。 


IM-MGW向MGW发送TRC_IU/NB_UP_INIT_TOIP消息，发起NB_UP初始化。 


MGW向IM-MGW发送TRC_IU/NB_UP_ACK_FRMIP消息，返回针对NB_UP初始化的响应。 


IM-MGW向eMSC发送NTFY REQ消息，通知承载建立完成。 


eMSC向IM-MGW返回NTFY REPLY消息。 


MGW向MSC Server发送NTFY REQ消息，通知承载建立完成。 


MSC Server向MGW返回NTFY REPLY消息。 


MSC Server建立完媒体资源，发送ACM消息给eMSC。 


eMSC向IM-MGW发送ADD REQ消息，建立到IMS一侧的IP终结点，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，返回ADD REPLY消息。 


MME_A向UE_A发送Handover Command消息，指示UE_A向GERAN发起切换。 


会话切换流程


eMSC根据STN-SR向P-CSCF/ATCF_A发送INVITE消息，携带SDP信息。 
关键信元如下： 

 
Request URI：STN-SR号码。 

 
P-Asserted-Identity头域：C-MSISDN号码。 

 
Accept头域：携带vnd.3gpp.mid-call标识，表示eMSC支持处理mid-call消息体。 

 
Recv-Info头域：携带+g.3gpp.mid-call标识，表示eMSC支持处理mid-call通知。 

 
SDP：携带eMSC支持的编解码信息。 

 


eMSC向MME_A发送PS to CS Response消息，指示手机可以向GERAN发起网络切换。 


P-CSCF/ATCF_A收到INVITE消息，根据其中STN-SR号码，判断该消息是由eSRVCC切换产生。P-CSCF/ATCF_A作如下处理： 

 
P-CSCF/ATCF_A从INVITE消息中获取C-MSISDN，结合本地保存的+g.3gpp.srvcc标识、eSRVCC相关信息（ATU-STI等），确定UE_A需要切换的HOLD状态会话。 

 
P-CSCF/ATCF_A进行媒体协商修改，在ATGW新建媒体端点，与eMSC侧MGW的媒体端点完成连接。 

 
P-CSCF/ATCF_A向eMSC发送200 OK消息，携带本端新建端点的SDP信息。 

 


eMSC发送接收成功响应AC K消息给P-CSCF/ATCF_A。 


eMSC根据200消息中的承载信息通过MOD REQ消息下发给主叫IM-MGW。 


IM-MGW向eMSC发送MOD REPLY消息，返回修改终结点属性命令的响应。 


IM-MGW向eMSC发送NTFY REQ消息，确认当前端点已修改。 


eMSC向IM-MGW发送NTFY REPLY消息，返回上报隧道指示事件的响应。 


P-CSCF/ATCF_A根据待切换会话关联的ATU-STI，向VoLTE AS_A发送INVITE消息，请求eSRVCC切换。 
关键参数如下： 

 
Request-URI：待切换会话的ATU-STI。 

 
P-Asserted-Identity：UE的C-MSISDN号码。 

 
Require：携带tdialog标识，指示VoLTE AS支持Target-Dialog头域。 

 
Target-Dialog：待切换会话的原Dialog ID，包括原会话的Call-ID，远端设备用户实例（remote-tag），本端设备用户实例（local-tag）。 

 
Accept头域：携带vnd.3gpp.mid-call标识，表示eMSC支持处理mid-call消息体。 

 
Recv-Info头域：携带+g.3gpp.mid-call标识，表示eMSC支持处理mid-call通知。 

 
SDP：UE的SDP，与原会话协商后的SDP相同。 

 


VoLTE AS_A收到INVITE消息后，通过其中Target-Dialog头域的原会话Call-ID确定待切换的会话，并作如下处理： 

 
如果该会话处于HOLD状态，且具有激活的语音媒体成分，则VoLTE AS比较INVITE消息中SDP的编解码是否与原会话协商后SDP的编解码相同，并根据比较结果启动eSRVCC流程或SRVCC流程。
如果相同，则VoLTE AS启动eSRVCC流程，修改该会话的接入域，表明用户已从CS域接入，便于后续业务进行域选择，并且返回200
OK消息。由于原会话协商SDP的编解码未改变，VoLTE AS不更新远端SDP。
如果不相同，则VoLTE AS启动SRVCC流程，修改会话接入域，返回200 OK消息，并且通过S-CSCF发送UPDATE消息给UE_B，更新远端SDP。
 

 
如果通过会话ID无法确定会话，则VoLTE AS返回480消息拒绝本次切换，并释放该用户所有会话。 

 


P-CSCF/ATCF_A向VoLTE AS_A返回ACK消息。UE_A与UE_B之间恢复媒体连接。后续UE_A所在网络侧媒体信息基于CS网络承载。 


CS网络位置更新


UE_A开始接入CS网络，BSC给MSC Server发送Handover Detect消息，表示UE_A已经检测到新信道，已经具备接入新的无线信道的条件，但尚未真正切入。 


当MSC Server收到BSC上报的Handover Detect消息后，通过局间MAP信令发送MAP PROCESS
ACCESS SIGNALLING IND消息给eMSC。 


UE_A成功接入CS网络，BSC给MSC Server发送Handover Complete消息，通知MSC Server切换完成。 


当MSC Server收到UE_A上报的Handover Complete消息后，发送ANM消息给eMSC。 


MSC Server同时通过局间MAP信令发送MAP SEND END SIGNAL IND消息给eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A，通知MME_A切换已经成功。 


MME_A发送SRVCC PS to CS Complete Ack响应消息给eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到融合HLR/HSS进行位置更新，确保后续的被叫业务能正确地路由到eMSC。 


融合HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND插入用户数据给eMSC。 


eMSC向融合HLR/HSS返回插入用户数据操作的响应。 


融合HLR/HSS向eMSC插入用户数据成功后，融合HLR/HSS向eMSC回位置更新的MAP UPDATE LOCATION
CNF响应。 


释放原会话资源


切换成功后，VoLTE AS_A向P-CSCF/ATCF_A发送BYE消息，释放原会话媒体端点。 


P-CSCF/ATCF_A向VoLTE AS_A返回200响应消息。 


P-CSCF/ATCF_A向UE_A发送BYE请求，释放原会话资源，并向PCRF发送STR消息释放专有承载。 


UE_A向P-CSCF/ATCF_A返回200响应消息。 


呼叫恢复


切换后的UE_A恢复呼叫，发送Retrieve Request到MSC Server。 


MSC Server在MAP_PROCESS_ACCESS_SIG_REQ消息包装Retrieve Requset，发送到eMSC。 


eMSC处理Retrieve Requset，发送MOD REQ到IM-MGW，修改终端属性为sendreceive. 


IM-MGW操作成功，返回MOD REPLY。 


eMSC发送Update消息到ATCF_A，更新SDP属性。 


ATCF_A转发至S-CSCF_A。 


再由S-CSCF_A发送至VoLTE AS_A。 


VoLTE AS_A发送到UE_B进行处理。 


UE_B返回200OK成功应答。 


VoLTE AS_A返回至S-CSCF_A。 


S-CSCF_A将200 OK再发送到ATCF_A。 


ATCF_A将200 OK转发至eMSC。 


eMSC发送MAP_FORWARD_ACCESS_SIG_REQ到MSC Server，其中包装Retrieve ACK消息。 


MSC Server获取Retrieve ACK消息，并发送到UE_A。 




#### 单路语音呼叫切换（呼出Alerting状态） 
#### 单路语音呼叫切换（呼出Alerting状态） 


业务模型 :本流程业务模型如下： 

 
主叫LTE用户UE_A已签约SRVCC/eSRVCC业务，被叫用户UE_B为LTE用户。 

 
UE_A呼叫UE_B，UE_B处于振铃态。UE_A从LTE网络移动到3G网络，发生eSRVCC切换。 

 


信令流程 :单路语音呼叫切换（呼出Alerting状态）的信令流程如[图1](15-%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88%E5%91%BC%E5%87%BAAlerting%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__fig_-1333-C6B8F69A)所示。
图1  单路语音呼叫切换（呼出Alerting状态）


[]images/img-0013541654(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带SDP Offer信息。 


会话切换流程


eMSC根据STN-SR向P-CSCF/ATCF_A发送INVITE消息，携带UE_A的媒体信息。其中关键字段说明如下： 

 
被叫号码Request URI填写STN-SR号码，对于SRVCC为VoLTE AS_A的地址，对于eSRVCC为ATCF的地址。 

 
Contact头域：携带+g.3gpp.srvcc-alerting标识，表示eMSC支持Alerting切换。 

 
P-Asserted-Identity头域携带C-MSISDN号码，ATCF需要使用C-MSISDN号码关联IMS用户用户。 

 


eMSCS向MME_A返回PS to CS Response消息，通知UE_A可以向GERAN发起网络切换。 


P-CSCF/ATCF_A收到INVITE消息后，根据STN-SR号码，判断该消息是由eMSC发起切换。P-CSCF/ATCF_A从INVITE消息中获取C-MSISDN，结合本地保存的+g.3gpp.srvcc标识、eSRVCC相关信息（ATU-STI等），确定UE_A需要切换的Alerting状态会话。ATCF匹配到用户的Alerting状态会话，进行媒体协商修改，新建媒体端点，与eSRVCC侧MGW的媒体端点完成连接。ATCF将INVITE消息中Request
URI的STN-SR替换成ATU-STI，并将其转发给SCC AS，其中携带本端新建端点的SDP信息。 


I-CSCF收到ATCF_A发送的INVITE消息后，根据Request-URI通过LIR/LIA消息查询HSS或根据本地PSI数据配置查询VoLTE
AS_A的地址，根据查询结果将INVITE消息路由到VoLTE AS_A。 


VoLTE AS_A收到INVITE消息后，同INVITE会话携带的信息，关联用户处于Alerting状态的会话。同时VoLTE
AS_A需要检查invite消息中SDP的编解码是否与原会话协商后SDP的编解码相同，如果相同，则VoLTE AS_A启动eSRVCC流程，修改该会话的接入域，表明用户接入域发生改变，并发送183响应给I-CSCF。 


I-CSCF透传183消息给ATCF_A。 


ATCF_A收到183消息后进行编解码转换，完成后发送183消息给eMSC。 


eMSC收到183消息后，发送MOD REQ消息给IM-MGW修改IMS侧的承载端点。消息中携带的关键信元。 


IM-MGW向eMSC发送MOD REPLY消息，返回修改终结点属性命令的响应。 


IM-MGW向eMSC 发送NTFY REQ消息，上报承载建立事件。 


eMSC向IM-MGW发送NTFY REPLY消息，返回上报承载建立事件的响应。 


eMSC返回PRACK消息给VoLTE AS_A，表示对183消息的确认。 


VoLTE AS_A返回200 (For PRACK)消息给eMSC。 


CS网络位置更新


VoLTE AS_A在200 OK消息之后，发送INFO消息到eMSC，通知eMSC当前呼叫状态是主叫振铃。 


eMSC更新切换对话的状态，返回INFO消息的200 OK。 


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


MSC Server通过局间MAP信令发送MAP SEND END SIGNAL IND消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND消息到eMSC，插入用户数据。 


eMSC (VLR)返回MAP INSERT SUBSCRIBER DATA RSP。 


HLR/HSS返回MAP UPDATE LOCATION CNF应答消息。 


释放原会话资源


切换成功后，VoLTE AS_A将发送503（对于INVITE）响应，指示释放原LTE下的会话。503消息经过I-CSCF、ATCF、到UE_A。 




#### 单路语音呼叫切换（呼入Alerting状态） 
#### 单路语音呼叫切换（呼入Alerting状态） 


业务模型 :本流程的业务模型如下： 

 
被叫LTE用户UE_A已签约SRVCC/eSRVCC业务，主叫用户UE_B为LTE用户。 

 
UE_B呼叫UE_A，UE_A处于振铃态。UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 

 


信令流程 :单路语音呼叫切换（呼入Alerting状态）的信令流程如[图1](16-%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88%E5%91%BC%E5%85%A5Alerting%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E5%8D%95%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%E5%91%BC%E5%85%A5Alerting%E7%8A%B6%E6%80%81-C71BF4EB)所示。
图1  单路语音呼叫切换（呼入Alerting状态）


[]images/img-0013541657(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带SDP Offer信息。 


会话切换流程


eMSC根据STN-SR向P-CSCF/ATCF_A发送INVITE消息，携带UE_A的媒体信息。其中关键字段说明如下： 

 
被叫号码Request URI填写STN-SR号码，对于SRVCC为VoLTE AS_A的地址，对于eSRVCC为ATCF的地址。 

 
Contact头域：携带+g.3gpp.srvcc-alerting标识，表示eMSC支持Alerting切换。 

 
P-Asserted-Identity头域携带C-MSISDN号码，ATCF需要使用C-MSISDN号码关联IMS用户用户。 

 


P-CSCF/ATCF_A收到INVITE消息后，根据STN-SR号码，判断该消息是由eMSC发起切换。P-CSCF/ATCF_A从INVITE消息中获取C-MSISDN，结合本地保存的+g.3gpp.srvcc标识、eSRVCC相关信息（ATU-STI等），确定UE_A需要切换的Alerting状态会话。ATCF匹配到用户的Alerting状态会话，进行媒体协商修改，新建媒体端点，与eSRVCC侧MGW的媒体端点完成连接。ATCF将INVITE消息中Request
URI的STN-SR替换成ATU-STI，并将其转发给VoLTE AS_A，其中携带本端新建端点的SDP信息。 


I-CSCF收到ATCF_A发送的INVITE消息后，根据Request-URI通过LIR/LIA消息查询HSS或根据本地PSI数据配置查询VoLTE
AS_A的地址，根据查询结果将INVITE消息路由到VoLTE AS_A。 


VoLTE AS_A收到INVITE消息后，同invite会话携带的信息，关联用户处于Alerting状态的会话。同时VoLTE
AS_A需要检查invite消息中SDP的编解码是否与原会话协商后SDP的编解码相同，如果相同，则VoLTE AS_A启动eSRVCC流程，修改该会话的接入域，表明用户接入域发生改变，并发送183响应给ICSCF。 


I-CSCF透传183消息给ATCF_A。 


ATCF_A收到183消息后进行编解码转换，完成后发送183消息给eMSC。 


eMSC收到183消息后，发送MOD REQ消息给IM-MGW修改IMS侧的承载端点。消息中携带的关键信元 


IM-MGW向EMSC发送MOD REPLY消息，返回修改终结点属性命令的响应。 


IM-MGW向eMSC发送NTFY REQ消息，上报承载建立事件。 


eMSC向IM-MGW发送NTFY REPLY消息，返回上报承载建立事件的响应。 


eMSC返回PRACK消息给VoLTE AS_A，表示对183消息的确认。 


VoLTE AS_A返回200(For PRACK)消息给eMSC。 


CS网络位置更新


VoLTE AS_A在200 OK消息之后，发送INFO消息到eMSC，通知eMSC当前呼叫状态是被叫振铃。 


eMSC更新切换对话的状态，返回INFO消息的200 OK。 


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


MSC Server通过局间MAP信令发送MAP SEND END SIGNAL IND消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND插入用户数据。 


eMSC(VLR)返回MAP INSERT SUBSCRIBER DATA RSP消息。 


HLR/HSS返回MAP UPDATE LOCATION CNF应答消息。 


释放原会话资源


VoLTE AS_A将发送CANCEL消息给ATCF。 


ATCF再转发CANCEL消息给UE_A，释放原会话。 


UE_A回200 OK消息给ATCF 


ATCF再转发200 OK消息给VoLTE AS_A。 


UE_A返回针对INVITE消息的487响应消息给ATCF。 


ATCF再将该消息转发给VoLTE AS_A。 




#### 两路语音呼叫切换（Active状态和Hold状态） 
#### 两路语音呼叫切换（Active状态和Hold状态） 


业务模型 :UE_A呼叫UE_B，通话后，UE_A保持UE_B，UE_A再呼叫UE_C，进入通话。UE_A有一路Active状态的会话和一路Hold状态的会话。UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 


信令流程 :两路语音呼叫切换（Active状态和Hold状态）的流程如[图1](17-%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88Active%E7%8A%B6%E6%80%81%E5%92%8CHold%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Active%E7%8A%B6%E6%80%81%E5%92%8CHold%E7%8A%B6%E6%80%81-B6A34AA2__%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Active%E7%8A%B6%E6%80%81%E5%92%8CHold%E7%8A%B6%E6%80%81-BBCE1589)所示。
图1  两路语音呼叫切换（Active状态和Hold状态）


[]images/img-0013409736(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带IP终端的IP地址和端口等信息。 


ATCF新建媒体端点流程


eMSC根据STN-SR路由，发送INVITE消息到ATCF_A，携带SDP Offer信息。 


eMSC返回PS to CS Response消息到MME_A，通知手机可以接入到CS网络。 


ATCF_A收到INVITE消息，返回200OK消息，携带SDP Answer。 


eMSC返回消息接收成功响应ACK。 


eMSC下发MOD REQ消息到IM-MGW，携带SDP Answer。 


IM-MGW返回MOD REPLY消息。 


CS网络位置更新


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


同时，MSC Server通过局间MAP信令发送MAP SEND END SIGNAL IND消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND插入用户数据。 


eMSC返回MAP INSERT SUBSCRIBER DATA RSP。 


HLR/HSS返回 MAP UPDATE LOCATION CNF应答消息。 


接入域修改


ATCF_A根据ATU-STI，查询DNS，获得VoLTE AS_A的IP地址，向VoLTE AS_A发送INVITE消息，请求eSRVCC切换。 


VoLTE AS_A接收到切换的INVITE消息，执行Active会话的切换，发送200 OK消息。 


ATCF_A发送ACK消息给VoLTE AS_A。 


Hold会话切换


VoLTE AS_A指示eMSC发起第二路会话切换，发送对话内Refer消息，指示还有呼叫需要进行切换，消息中Refer-To头域携带VoLTE
AS_A的AdditionalTransferredSessionURI。 


ATCF_A接收到Refer消息后，保存Refer-To头域中VoLTE AS_A的AdditionalTransferredSessionURI，转发Refer消息给eMSC时，将Refer-To头域中VoLTE
AS_A的AdditionalTransferredSessionURI修改为ATCF自身的URI。 


eMSC接收到Refer消息后，发送202响应消息给ATCF_A。 


ATCF_A发送202响应消息给VoLTE AS_A。 


eMSC发送ADD REQ消息，建立到IMS侧的终端，终端媒体描述为Hold状态。ADD消息同时携带终端所用的编解码。 


IM-MGW分配IP资源，回复ADD REPLY消息到eMSC。 


eMSC进行hold会话的切换，发送INVITE消息，其中Request-URI为此前ATCF发送的Refer-To中的ATCF
URI。 


ATCF_A接收到INVITE后，将Request-URI修改为此前保存的VoLTE AS_A的AdditionalTransferredSessionURI，转发INVITE消息给VoLTE
AS_A。 


VoLTE AS_A完成切换，发送200 OK消息给ATCF_A。 


ATCF_A发送200 OK消息给eMSC。 


eMSC完成切换，发送ACK给ATCF_A。 


ATCF_A发送ACK消息给VoLTE AS_A。 


eMSC将200消息中的承载信息通过MOD REQ消息发送给IM-MGW。 


IM-MGW获取承载信息，返回MOD REPLY。 


释放Acitve状态和Hold状态的原会话资源


切换成功，VoLTE AS_A向S-CSCF发送BYE消息，释放UE-A与UE-C原会话中从UE-A到VoLTE AS_A之间的会话。 


S-CSCF向ATCF_A发送BYE消息，释放UE-A与UE-C原会话。 


ATCF_A向S-CSCF发送200 OK消息。 


S-CSCF向VoLTE AS_A发送200 OK消息。 


ATCF_A向UE_A发送BYE消息。 


UE_A向ATCF_A发送200 OK消息。 


VoLTE AS_A向S-CSCF发送BYE消息，释放UE-A与UE-B原会话中从UE-A到VoLTE AS_A之间的会话。 


S-CSCF向ATCF_A发送BYE消息，释放UE-A与UE-B原会话。 


ATCF_A向S-CSCF发送200 OK消息。 


S-CSCF向VoLTE AS_A发送200 OK消息。 


ATCF_A向UE-A发送BYE消息，释放原会话资源。 


UE-A向ATCF_A发送200 OK消息。 




#### 两路语音呼叫切换（Active状态和Alerting状态） 
#### 两路语音呼叫切换（Active状态和Alerting状态） 


业务模型 :UE_A呼叫UE_B，通话后，UE_C呼叫UE_A，UE_A振铃。UE_A有一路Active状态的会话和一路呼入Alerting状态的会话。UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 


信令流程 :两路语音呼叫切换（Active状态和Alerting状态）的流程如[图1](18-%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88Active%E7%8A%B6%E6%80%81%E5%92%8CAlerting%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Active%E7%8A%B6%E6%80%81%E5%92%8CAlerting%E7%8A%B6%E6%80%81-B6A35960__%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Active%E7%8A%B6%E6%80%81%E5%92%8CAlerting%E7%8A%B6%E6%80%81-BBCDCBC6)所示。
图1  两路语音呼叫切换（Active状态和Alerting状态）


[]images/img-0013409734(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带IP终端的IP地址和端口等信息。 


ATCF新建媒体端点流程


eMSC根据STN-SR路由，发送INVITE消息到ATCF_A，携带SDP Offer信息。 


eMSC返回PS to CS Response消息到MME_A,通知手机可以接入到CS网络。 


ATCF_A收到INVITE消息，返回200OK消息，携带SDP Answer。 


eMSC返回消息接收成功响应ACK。 


eMSC下发MOD REQ消息到IM-MGW，携带SDP Answer。 


IM-MGW返回MOD REPLY消息。 


CS网络位置更新


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


MSC Server通过局间MAP信令发送MAP SEND END SIGNAL IND消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND插入用户数据。 


eMSC返回MAP INSERT SUBSCRIBER DATA RSP。 


HLR/HSS返回 MAP UPDATE LOCATION CNF应答消息。 


接入域修改


ATCF_A根据ATU-STI，查询DNS，获得VoLTE AS_A的IP地址，向VoLTE AS_A发送INVITE消息，请求eSRVCC切换。 


VoLTE AS_A接收到切换的INVITE消息，执行Active会话的切换，发送200 OK消息。 


ATCF_A发送ACK消息给VoLTE AS_A。 


Alerting会话切换


VoLTE AS_A指示eMSC发起第二路会话切换，发送对话内Refer消息，指示还有呼叫需要进行切换，消息中Refer-To头域携带VoLTE
AS_A的AdditionalTransferredSessionURI。 


ATCF_A接收到Refer消息后，保存Refer-To头域中VoLTE AS_A的AdditionalTransferredSessionURI，转发Refer消息给eMSC时，将Refer-To头域中VoLTE
AS_A的AdditionalTransferredSessionURI修改为ATCF自身的URI。 


eMSC接收到Refer消息后，发送202响应消息给ATCF_A。 


ATCF_A发送202响应消息给VoLTE AS_A。 


eMSC发送ADD REQ消息到IM-MGW，建立振铃会话的IMS侧终端，指示所要使用的编解码。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC。 


eMSC进行Alerting会话的切换，发送INVITE消息，其中Request-URI为此前ATCF发送的Refer-To中的ATCF
URI。 


ATCF_A接收到INVITE后，将Request-URI修改为此前保存的VoLTE AS_A的AdditionalTransferredSessionURI，转发INVITE消息给VoLTE
AS_A。 


VoLTE AS_A发送183消息给ATCF_A。 


ATCF_A发送183消息给eMSC。 


eMSC将200 消息中的SDP信息在MOD REQ消息中发送给IM-MGW。 


IM-MGW返回MOD REPLY消息到eMSC。 


eMSC进入Call Received状态，发送PRACK消息给ATCF_A。 


ATCF_A发送PRACK消息给VoLTE AS_A。 


VoLTE AS_A发送200 OK消息给ATCF_A。 


ATCF_A发送200 OK消息给eMSC。 


释放原会话


切换成功，VoLTE AS_A向S-CSCF发送BYE消息，释放UE-A与UE-B原会话中从UE-A到VoLTE AS_A之间的会话。 


S-CSCF向ATCF_A发送BYE消息，释放UE-A与UE-B原会话。 


ATCF_A向S-CSCF发送200 OK消息。 


S-CSCF向VoLTE AS_A发送200 OK消息。 


ATCF_A向UE_A发送BYE消息。 


UE_A向ATCF_A发送200 OK消息。 
注：UE_A在UTRAN/GERAN应答时，eMSC发送INFO消息给VoLTE
AS_A，指示UE_A应答。VoLTE AS_A收到INFO消息后，向UE-C发送200 OK，指示UE_A应答。VoLTE AS_A发送CANCEL消息给ATCF_A，释放UE_A原有的振铃态会话。 




#### 两路语音呼叫切换（Hold状态和呼入Alerting状态） 
#### 两路语音呼叫切换（Hold状态和呼入Alerting状态） 


业务模型 :UE_A呼叫UE_B，通话后，UE_A 保持UE_B，UE_C呼叫UE_A，UE_A振铃。UE_A有一路hold状态的会话和一路呼入Alerting状态的会话。UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 


信令流程 :两路语音呼叫切换（Hold状态和呼入Alerting状态）的信令流程如[图1](19-%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88Hold%E7%8A%B6%E6%80%81%E5%92%8C%E5%91%BC%E5%85%A5Alerting%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Hold%E7%8A%B6%E6%80%81%E5%92%8C%E5%91%BC%E5%85%A5Alerting%E7%8A%B6%E6%80%81-C727EC09)所示。
图1  两路语音呼叫切换（Hold状态和呼入Alerting状态）


[]images/img-0013541660(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带SDP Offer信息。 


Hold会话切换


eMSC根据STN-SR向ATCF_A发送INVITE消息，携带SDP信息，Request URI为STN-SR号码。 


eMSC返回PS to CS Response消息到MME_A，通知手机可以接入到CS网络。 


ATCF_A收到INVITE消息，根据其中的STN-SR号码，判断该消息是由切换产生，在ATGW新建媒体端点，与eMSC侧MGW的媒体端点完成连接，向eMSC发送200
OK消息，携带本端新建端点的SDP信息。 


eMSC发送接收成功响应ACK消息给ATCF_A。 


eMSC根据200 OK消息中的承载信息通过MOD REQ消息发送给IM-MGW。 


IM-MGW向eMSC发送MOD REPLY响应消息。 


ATCF_A根据待切换会话的ATU-STI，向VoLTE AS_A发送INVITE消息，请求切换。 


VoLTE AS_A收到INVITE消息后，发送200 OK消息给ATCF_A。 


ATCF_A向VoLTE AS_A返回ACK消息。 


CS网络位置更新


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


同时，MSC Server通过局间MAP信令发送MAP SEND END SIGNAL IND消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND插入用户数据。 


eMSC返回MAP INSERT SUBSCRIBER DATA RSP。 


HLR/HSS返回 MAP UPDATE LOCATION CNF应答消息。 


Alerting会话切换


VoLTE AS_A指示eMSC发起第二路会话切换，发送对话内Refer消息，指示还有呼叫需要进行切换，消息中Refer-To头域携带VoLTE
AS_A的AdditionalTransferredSessionURI。 


ATCF_A接收到Refer消息后，保存Refer-to头域中VoLTE AS_A的AdditionalTransferredSessionURI，转发refer消息给eMSC时，将refer-to修改为ATCF自身的URI。 


eMSC接收到Refer消息后，发送202响应消息给ATCF_A。 


ATCF_A发送202响应消息给VoLTE AS_A。 


eMSC进行Alerting会话的切换，发送ADD REQ消息 到IM-MGW，建立第二路会话的终端。 


IM-MGW返回ADD REPLY。 


eMSC发送INVITE消息，其中Request-URI为此前ATCF发送的 refer-to中的ATCF URI。 


ATCF_A接收到INVITE后，将Request-URI修改为此前保存的VoLTE AS_A的AdditionalTransferredSessionURI，转发INVITE消息给VoLTE
AS_A。 


VoLTE AS_A发送183消息给ATCF_A。 


ATCF_A发送183消息给eMSC。 


eMSC发送MOD REQ消息到IM-MGW，将SDP Answer传递到IM-MGW。 


IM-MGW返回MOD REPLY。 


eMSC进入Call Received状态，发送PRACK消息给ATCF_A。 


ATCF_A发送PRACK消息给VoLTE AS_A。 


VoLTE AS_A发送200 OK消息给ATCF_A。 


ATCF_A发送200 OK消息给eMSC。 


释放原会话


VoLTE AS _A向S-CSCF发送BYE消息，释放UE-A与UE-B原会话中从UE-A到VoLTE AS_A之间的会话。 


S-CSCF向ATCF_A发送BYE消息，释放UE-A与UE-B原会话。 


ATCF_A向S-CSCF发送200 OK消息。 


S-CSCF向VoLTE AS _A发送200 OK消息。 


ATCF_A向UE_A发送BYE消息。 


UE_A向ATCF_A发送200 OK消息。 


 说明： 
对于呼入振铃原有会话的释放，UE_A在UTRAN/GERAN应答时，eMSC发送INFO消息给VoLTE
AS_A，指示UE_A应答。VoLTE AS_A收到INFO消息后，向UE-C发送200 OK，指示UE_A应答。此后VoLTE AS_A发送CANCEL消息给ATCF_A，释放UE_A原有的呼入振铃会话。 


#### 两路语音呼叫切换（Hold状态和呼出Alerting状态） 
#### 两路语音呼叫切换（Hold状态和呼出Alerting状态） 


业务模型 :UE_A呼叫UE_B，通话后，UE_A 保持UE_B，UE_A再呼叫UE_C，UE_C振铃。UE_A有一路Active状态的会话和一路呼出Alerting状态的会话。UE_A从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。 


信令流程 :两路语音呼叫切换（Hold状态和呼出Alerting状态）的信令流程如[图1](20-%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88Hold%E7%8A%B6%E6%80%81%E5%92%8C%E5%91%BC%E5%87%BAAlerting%E7%8A%B6%E6%80%81%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E4%B8%A4%E8%B7%AF%E8%AF%AD%E9%9F%B3%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2Hold%E7%8A%B6%E6%80%81%E5%92%8C%E5%91%BC%E5%87%BAAlerting%E7%8A%B6%E6%80%81-C726543F)所示。
图1  两路语音呼叫切换（Hold状态和呼出Alerting状态）


[]images/img-0013541663(%E9%87%8D%E7%94%A81).png)

CS网络媒体资源建立流程


UE_A测量到邻区的3G网络信号强度超过门限，上报系统测量报告，eNodeB_A经过判断决定切换，发送切换请求Handover
Required消息到MME_A。 


MME_A发起eSRVCC切换请求，发送PS to CS Request消息到UE_A当前所在小区的eMSC。 


eMSC发起局间切换请求，发送MAP PREPARE HANDOVER REQ消息到MSC Server。 


MSC Server发送ADD REQ消息到MGW，请求添加RNC侧的IP终端，并指示本次呼叫使用的编解码。 


MGW分配IP资源，回复ADD REPLY消息。 


MSC Server发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 


RNC发送TRC_IU/NB_UP_INIT_TOIP消息到MGW，发起UP初始化。 


MGW发送TRC_IU/NB_UP_ACK_FRMIP消息到RNC，返回UP初始化应答。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


MSC Server发送MAP PREPARE HANDOVER CNF消息到eMSC，携带切换号码Handover
Number。 


eMSC发送ADD REQ消息到IM-MGW，请求添加到MSC Server一侧的IP终端，并指示本次呼叫使用的编解码。 


IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 


IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 


eMSC返回NTFY REPLY应答消息到IM-MGW。 


eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。 


MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 


MGW返回ADD REPLY应答消息。 


MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送APM消息，携带隧道信息到eMSC。 


eMSC发送MOD REQ到IM-MGW，携带隧道信息。 


IM-MGW返回MOD REPLY。 


IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 


MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 


MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 


MSC Server返回NTFY REPLY应答消息到MGW。 


MSC Server发送ACM消息到eMSC。 


eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 


IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带SDP Offer信息。 


Hold会话切换


eMSC根据STN-SR向ATCF_A发送INVITE消息，携带SDP信息，Request URI为STN-SR号码。 


eMSC返回PS to CS Response消息到MME_A，通知手机可以接入到CS网络。 


ATCF_A收到INVITE消息，根据其中的STN-SR号码，判断该消息是由切换产生，在ATGW新建媒体端点，与eMSC侧MGW的媒体端点完成连接，向eMSC发送200
OK消息，携带本端新建端点的SDP信息。 


eMSC发送接收成功响应ACK消息给ATCF_A。 


eMSC根据200 OK消息中的承载信息通过MOD REQ消息发送给IM-MGW。 


IM-MGW向eMSC发送MOD REPLY响应消息。 


ATCF_A根据待切换会话的ATU-STI，向VoLTE AS_A发送INVITE消息，请求切换。 


VoLTE AS_A收到INVITE消息后，发送200 OK消息给ATCF_A。 


ATCF_A向VoLTE AS_A返回ACK消息。 


CS网络位置更新


UE_A开始接入CS网络，RNC发送Relocation Detect消息到MSC Server。 


MSC Server收到Relocation Detect消息，通过局间MAP信令发送MAP PROCESS ACCESS
SIGNALLING REQ消息到eMSC。 


UE_A接入CS网络完成，RNC发送Relocation Complete消息到MSC Server。 


当MSC Server收到Relocation Complete消息，发送ANM消息到eMSC。 


同时，MSC Server通过局间MAP信令发送MAP SEND END SIGNAL IND消息到eMSC。 


eMSC发送SRVCC PS to CS Complete Notification消息给MME_A。 


MME_A返回SRVCC PS to CS Complete Ack消息到eMSC。 


eMSC发送MAP UPDATE LOCATION REQ消息到HLR/HSS。 


HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND插入用户数据。 


eMSC返回MAP INSERT SUBSCRIBER DATA RSP。 


HLR/HSS返回 MAP UPDATE LOCATION CNF应答消息。 


Alerting会话切换


VoLTE AS_A指示eMSC发起第二路会话切换，发送对话内Refer消息，指示还有呼叫需要进行切换，消息中Refer-To头域携带VoLTE
AS_A的AdditionalTransferredSessionURI。 


ATCF_A接收到Refer消息后，保存Refer-to头域中VoLTE AS_A的AdditionalTransferredSessionURI，转发refer消息给eMSC时，将refer-to修改为ATCF自身的URI。 


eMSC接收到Refer消息后，发送202响应消息给ATCF_A。 


ATCF_A发送202响应消息给VoLTE AS_A。 


eMSC进行Alerting会话的切换，发送ADD REQ消息到IM-MGW，建立第二路会话的终端。 


IM-MGW返回ADD REPLY。 


eMSC发送INVITE消息，其中Request-URI为此前ATCF发送的refer-to中的ATCF URI。 


ATCF_A接收到INVITE后，将Request-URI修改为此前保存的VoLTE AS_A的AdditionalTransferredSessionURI，转发INVITE消息给VoLTE
AS_A。 


VoLTE AS_A发送183消息给ATCF_A。 


ATCF_A发送183消息给eMSC。 


eMSC发送MOD REQ消息到IM-MGW，将SDP Answer传递到IM-MGW。 


IM-MGW返回MOD REPLY。 


eMSC进入Call Received状态，发送PRACK消息给ATCF_A。 


ATCF_A发送PRACK消息给VoLTE AS_A。 


VoLTE AS_A发送200 OK消息给ATCF_A。 


ATCF_A发送200 OK消息给eMSC。 


释放原会话


VoLTE AS_A向S-CSCF发送BYE消息，释放UE-A与UE-B原会话中从UE-A到VoLTE AS_A之间的会话。 


S-CSCF向ATCF_A发送BYE消息，释放UE-A与UE-B原会话。 


ATCF_A向S-CSCF发送200 OK消息。 


S-CSCF向VoLTE AS_A发送200 OK消息。 


ATCF_A向UE_A发送BYE消息。 


UE_A向ATCF_A发送200 OK消息。 


 说明： 
对于呼出振铃原有会话的释放，UE_C应答时，VoLTE AS_A收到200 OK消息后，向ATCF_A发送404消息，释放UE_A原有的呼出振铃会话。 


#### 视频呼叫切换 
业务模型 :本流程的业务模型如下： 
签约SRVCC/eSRVCC业务的主叫LTE用户通过LTE网络发起视频呼叫，被叫域选网络为LTE网络，当主叫用户和被叫用户正在进行视频通话中（会话处于Active状态），主叫用户从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换，视频呼叫回落为语音呼叫继续进行通话。SBC配置支持ATCF/ATGW在SBC上对某个信令分组signal-group的运行模式run-mode配置为ATCF，则该信令分组执行ATCF网元的功能。ATCF如果需要使用ATGW来锚定媒体，则在该ATCF对应的信令分组的ATCF业务模板“ATCF-Profile”中，配置ATCF锚定ATGW开关“atcf-anchor-atgw-esrvcc”为使能“enable”。VoLTE AS支持SRVCC/eSRVCC功能。 
数据库部署形态为融合HLR/HSS，即HLR，SAE-HSS和IMS-HSS合一部署。 
采用四合一设备ZXUN B200（A04）支持A-SBC/P-CSCF/ATCF/ATGW功能。 
信令流程 :签约SRVCC/eSRVCC的主叫LTE用户发起视频呼叫，呼叫被叫VoLTE用户，被叫选择视频接通。视频通话一段时间后，主叫用户移出4G覆盖区域进入2G/3G覆盖区，发生eSRVCC切换，同时呼叫回落为语音通话。
具体流程如[图1](21-%E8%A7%86%E9%A2%91%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E8%A7%86%E9%A2%91%E5%91%BC%E5%8F%AB%E5%88%87%E6%8D%A2%E8%AF%AD%E9%9F%B3%E5%9B%9E%E8%90%BD-B6C80A93)所示。
图1  视频呼叫切换（语音回落）
[]images/img-0013406780(%E9%87%8D%E7%94%A81).png)
签约SRVCC/eSRVCC的主叫LTE用户发起视频呼叫，呼叫被叫VoLTE用户，被叫选择视频接通，主被叫UE_A和UE_B通话中。
CS网络媒体资源建立流程
UE_A通话过程中移动至4 G信号强度低于门限值地区，检测领区3G网络信息强度满足门限要求，上报系统测量报告至eNodeB_A；基于UE_A的测量报告，eNodeB_A决定触发到UTRAN的SRVCC切换，eNodeB_A发送Handover
Required（Target ID, generic Source to Target Transparent Container,
SRVCC HO indication）消息给源MME_A。
MME_A根据语音/视频承载的QCI（QCI 1&QCI=2）以及SRVCC
HO Indication，源MME分离语音/视频承载和其他PS承载，对语音承载发起PS-CS handover流程，根据Handover
Required消息中的TargetRNC-ID查DNS找到eMSC地址，发送SRVCC PS to
CS Request (IMSI, Target ID, STN-SR, C MSISDN, Source to Target Transparent Container,
MM Context)消息。
eMSC通过MAP PREPARE HANDOVER REQ消息向MSC Server发起局间切换请求。 
MSC Server向MGW发送ADD REQ消息，请求添加RNC侧的IP终结点，并指示本次呼叫使用的编解码。
MGW动态分配IP资源，向MSC Server回复ADD REPLY消息，该消息中返回终结点相关信息。
MSC Server发送Relocation Request消息给目标侧RNC，目标侧进行Iu接口资源和空口资源准备。 
RNC向MGW发送TRC_IU/NB_UP_INIT_TOIP消息，发起UP初始化，携带RNC侧IP地址、端口号、RFC（Remote Feature
Control）子流组合等信息。 
MGW向RNC发送TRC_IU/NB_UP_ACK_FRMIP消息，返回UP初始化命令的响应。 
RNC侧预留资源完成后，发送Relocation Request Ack消息给MSC Server。 
MSC Server发送MAP PREPARE HANDOVER CNF消息给eMSC，携带切换号码信元Handover
Number。 
eMSC向IM-MGW发送ADD REQ消息，请求添加到MSC Server一侧的IP终结点，并指示本次呼叫使用的编解码。  
IM-MGW动态分配IP资源，回复ADD REPLY消息到eMSC。 
IM-MGW发送NTFY REQ消息到eMSC，携带终端的IP地址和端口等隧道信息。 
eMSC返回NTFY REPLY应答消息到IM-MGW。 
eMSC根据切换号码确定出局链路，发送IAM消息到MSC Server，携带隧道信息。
MSC Server发送ADD REQ消息到MGW，请求添加到eMSC一侧的IP终端，携带有关隧道信息。 
MGW返回ADD REPLY应答消息。 
MGW发送NTFY REQ消息到MSC Server，携带终端的IP地址和端口等隧道信息。 
MSC Server返回NTFY REPLY应答消息到MGW。 
MSC Server发送APM消息，携带隧道信息到eMSC。 
eMSC发送MOD REQ到IM-MGW，携带隧道信息。 
IM-MGW返回MOD REPLY。 
IM-MGW到MGW发送TRC_IU/NB_UP_INIT_TOIP消息，进行UP初始化。 
MGW返回TRC_IU/NB_UP_ACK_FRMIP消息。 
MGW发送NTFY REQ消息到MSC Server，通知用户面建立成功。 
MSC Server返回NTFY REPLY应答消息到MGW。 
MSC Server发送ACM消息到eMSC。 
eMSC发送ADD REQ消息到IM-MGW，请求添加IMS侧的IP终端。 
IM-MGW分配IP资源，返回ADD REPLY消息到eMSC，携带SDP Offer信息。 
ATCF新建媒体端点流程
eMSC发送INVITE（其中Request URI=STN-SR, PAI=C-MSISDN）到P-CSCF/ATCF_A，该消息中不携带视频的SDP信息，切换回落至SRVCC。
eMSC向MME_A返回PS to CS Response消息,通知手机可以接入到UMTS。 
P-CSCF/ATCF_A从INVITE消息中获取C-MSISDN，结合本地保存的+g.3gpp.srvcc标识、ATU-STI等，关联切换呼叫和原始呼叫。ATCF_A发送配置消息到ATGW，用新的CS接入分支媒体路径信息更新现存的PS接入分支媒体信息。ATCF_A发起到VoLTE
AS_A的会话更新，发会话更新INVITE消息到对应的VoLTE AS_A。
当VoLTE AS_A比较发现发生切换的媒体会话中原来包含非音频媒体，则触发回落到SRVCC，发送INVITE消息到S-CSCF_A。对发送的INVITE消息SDP中的媒体信息处理如下：
语音流：携带新会话的媒体信息。 
视频流：保持旧会话的媒体信息不变，增加m行描述将媒体类型为Video的端口置为“0”。 
I/S-CSCF_A发出Invite消息经被叫侧I/S-CSCF_B，再到P-CSCF_B，最后至UE_B。 
UE_B回复200响应消息，其中媒体类型Video的属性示例如下： 
m: video 0 RTP/AVP
115 34 
Media Type：video 
MediaPort：0 
Media Protocol：RTP/AVP 
Media Format:DynamicRTP-Type-115 
Media Format:ITU-T H.263 
P-CSCF_B在收到被叫200 OK后，发送AAR请求PCRF_B更新承载删除视频媒体信息。 
PCRF_B收到了P-CSCF的资源授权请求后进行策略决策和授权。PCRF_B根据AAR消息携带的媒体信息的指示，发送RAR请求并携带PCC规则到P-GW_B，请求删除视频媒体信息。RAR消息里会携带Charing-Rule-Remove
AVP指示P-GW_B删除视频的PCC规则，触发专有承载删除流程
P-GW_B收到RAR，向PCRF_B发送RAA响应消息。
PCRF_B根据P-GW_B返回的RAA消息，给P-CSCF_B通过AAA响应授权请求结果消息。
P-GW_B收到RAR消息后，向MME_B发送Delete Bearer Request消息请求删除视频承载。
MME_B发送DEACTIVATE EPS BEARER CONTEXT REQUEST消息给UE_B请求释放视频承载。
UE_B发送DEACTIVATE EPS BEARER CONTEXT ACCEPT响应消息给MME_B。
视频承载删除完成后，MME_B向P-GW_B发送Delete Bearer Response消息。 
P-CSCF_B/ATCF_B转发200 OK消息到主叫P-CSCF_A/ATCF_A。 
P-CSCF_A/ATCF_A将200 OK消息透传给eMSC。
eMSC返回消息接收成功响应ACK。 
eMSC根据200 OK消息中的承载信息通过MOD REQ消息下发给被叫IM-MGW。 
IM-MGW向eMSC发送MOD REPLY消息，返回修改终结点属性命令的响应。
CS网络位置更新
UE_A开始接入CS网络，RNC给MSC Server发送Relocation
Detect消息，表示UE_A已经检测到新信道，已经具备接入新的无线信道的条件，但尚未真正切入。 
当MSC Server收到RNC上报的Relocation Detect消息后，通过局间MAP信令发送MAP PROCESS
ACCESS SIGNALLING IND消息给eMSC。
UE_A成功接入CS网络，RNC给MSC Server发送Relocation
Complete消息，通知MSC切换完成。
当MSC Server收到UE_A上报的Relocation Complete消息后，通过局间MAP信令发送MAP SEND END
SIGNAL IND消息给eMSC。 
MSC Server同时发送ANM消息给eMSC。
eMSC发送SRVCC PS to CS Complete Notification消息给MME_A，通知MME_A切换已经成功。
MME_A发送SRVCC PS to CS Complete Ack响应消息给eMSC。
eMSC发送MAP UPDATE LOCATION REQ消息到融合HLR/HSS的位置更新，确保后续的呼叫能正确地路由到被叫。 
融合HLR/HSS发送MAP INSERT SUBSCRIBER DATA IND用于位置更新过程时向VLR插入用户数据。
VLR向融合HLR/HSS返回插入用户数据操作的响应。
融合HLR/HSS向VLR插入用户数据成功后，融合HLR/HSS向VLR回位置更新的MAP UPDATE LOCATION CNF响应。
位置更新完成后，如果用户是ICS用户，按照配置，eMSC可以再发起Register过程。
VoLTE AS_A回200响应消息给eMSC。
释放原会话资源
VoLTE AS_A向UE_A发送BYE请求，释放主叫侧原会话资源。
UE_A向VoLTE AS_A返回200响应消息。 
### 回切流程 
#### 通话状态下回切（E-UTRAN网络信号增强） 
#### 通话状态下回切（E-UTRAN网络信号增强） 


业务模型 :本场景描述在主叫LTE用户A在接入E-UTRAN通话过程中，E-UTRAN网络信号变化后,UE上报系统量测报告，通过eNodeB发起发起eSRVCC切换请求。在eMSC向IMS网络发起切换请求前，E-UTRAN信号增强，UE重新发送系统量测报告，通过eNodeB请求取消切换并重新接入E-UTRAN。 


##### 信令描述 
通话状态下由于E-UTRAN信号增强回切至4G，具体的信令流程如[图1](22-%E9%80%9A%E8%AF%9D%E7%8A%B6%E6%80%81%E4%B8%8B%E5%9B%9E%E5%88%87%EF%BC%88E-UTRAN%E7%BD%91%E7%BB%9C%E4%BF%A1%E5%8F%B7%E5%A2%9E%E5%BC%BA%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E9%80%9A%E8%AF%9D%E7%8A%B6%E6%80%81%E4%B8%8B%E5%9B%9E%E5%88%87E-UTRAN%E7%BD%91%E7%BB%9C%E4%BF%A1%E5%8F%B7%E5%A2%9E%E5%BC%BA-C729ECA3)所示。
图1  通话状态下回切（E-UTRAN网络信号增强）


[]images/img-0013541666(%E9%87%8D%E7%94%A81).png)



UE测量当前位置的E-UTRAN和UTRAN/GSM信号强度，上报系统测量报告。 


eNodeB经过判断决定切换，发送切换请求Handover Required消息到MME。 


MME发起eSRVCC切换请求，根据Handover Required消息中的TargetRNC-ID查DNS找到eMSC地址，发送PS
to CS Request消息到UE当前所在小区的eMSC。 


eMSC发送Relocation Request消息给目标侧RNC，目标侧准备Iu接口资源和空口资源。 
 说明： 
此处eMSC与切换目标MSC/MGW之间的交互流程略去。 


RNC资源准备完成，发送Relocation Request Ack消息到MSC Server。 


eNodeB收到UE新的系统测量报告，决定取消切换，发送Handover Cancel消息到MME。 


MME发送PS to CS Cancel NTFY消息到eMSC。 


eMSC发送Iu Release Command消息到RNC，释放空口资源。 


eMSC返回PS to CS Cancel ACK消息到MME，提示接受切换取消请求。 


RNC发送Iu Release Complete到eMSC，通知空口资源释放完成。 


MME发送Notification消息到UE，通知其取消切换。 


MME发送Handover Cancel ACK消息到eNodeB，通知其切换已取消。 




#### 通话状态下回切（UTRAN/GERAN网络信号减弱） 
#### 通话状态下回切（UTRAN/GERAN网络信号减弱） 


业务模型 :在主叫LTE用户A在接入E-UTRAN通话过程中，UE由于4 G网络信号不足导致eSRVCC切换请求，在收到切换指示后，UTRAN/GERAN减弱导致接入失败，从而UE向eNodeB请求取消切换并重新接入E-UTRAN。


信令流程 :通话状态下回切至4G具体的信令流程如[图1](23-%E9%80%9A%E8%AF%9D%E7%8A%B6%E6%80%81%E4%B8%8B%E5%9B%9E%E5%88%87%EF%BC%88UTRAN%20GERAN%E7%BD%91%E7%BB%9C%E4%BF%A1%E5%8F%B7%E5%87%8F%E5%BC%B1%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__%E9%80%9A%E8%AF%9D%E7%8A%B6%E6%80%81%E4%B8%8B%E5%9B%9E%E5%88%87UTRANGERAN%E7%BD%91%E7%BB%9C%E4%BF%A1%E5%8F%B7%E5%87%8F%E5%BC%B1-B6C92EA1)所示。
图1  通话状态下回切（UTRAN/GERAN网络信号减弱）

[]images/img-0013377691(%E9%87%8D%E7%94%A81).png)
流程说明如下： 


UE在通话过程中，根据当前位置所在E-UTRAN和UTRAN/GERAN网络的信号强度，向eNodeB上传系统测量报告。


eNodeB基于UE的测量报告，决定触发到UTRAN的SRVCC切换，发送Handover Required（Target
ID, generic Source to Target Transparent Container, SRVCC HO indication）消息给MME。


MME根据语音承载的QCI以及SRVCC HO Indication，MME分离语音承载和其他PS承载，对语音承载发起PS-CS
handover流程，根据Handover Required消息中的TargetRNC-ID查DNS找到eMSC地址，发送SRVCC PS to
CS Request (IMSI, Target ID, STN-SR, C MSISDN, Source to Target
Transparent Container, MM Context) 消息。


eSMC接收PS to CS Request消息后，向RNC发送Relocation Request消息指示其分配切换所需要的空口资源。


TargetRNC向eSMC返回Relocation Request ACK消息，指示空口资源分配完成。 


eSMC向P-CSCF/ATCF发送INVITE消息，携带SDP信息。


eSMC向MME返回PS to CS Response消息，指示已接受切换请求。


MME向UE发送Handover Command指示UE进行接入网切换。 


UE接入UTRAN/GERAN网络失败，发送RRC Connection Reestablishment Request消息至eNodeB，请求重新接入E-UTRAN网络。


eNodeB收到RRC Connection Reestablishment Request消息后，向MME发送Handover Cancel消息请求取消切换。


MME向eMSC发送PS to CS Cancel Notification （IMSI, SRVCC Cause）消息指示切换取消。


eMSC向RNC发送Iu Release Command消息，指示其释放切换所需的空口资源。 


eMSC向MME发送PS to CS Cancel Acknowledge 消息接受切换取消请求。 


RNC向eSMC发送Iu Release Complete消息通知其空口资源释放完成。


MME向UE发送Notification（Notification indicator :SRVCC handover cancelled,
IMS session re-establishment required）消息通知其切换取消。


MME向eNodeB发送Handover Cancel Acknowledge消息通知其切换已取消。


UE收到MME的Notification消息后，重新向P-CSCF/ATCF发送ReINVITE消息。 在此期间VoLTE
AS在定时器（协议默认值为8秒，VoLTE AS可配置，一般配置为10秒）到前，不释放主叫侧PS承载会话。 


P-CSCF/ATCF检查Reinvite消息，保持原呼叫，使用原会话的SDP信息通过INVITE消息发送给VoLTE AS。


VoLTE AS通过S/P-CSCF向UE发送200 OK消息。


VoLTE AS通过P-CSCF/ATCF向eSMC发送BYE消息，释放eMSC之前建立的会话资源。 


eMSC向VoLTE AS返回BYE消息的200 OK响应，通知会话资源释放已完成。 


 说明： 

 
目前切换会话资源的释放由VoLTE AS发起。 

 
上述流程未画出eSMC至目标MSC/MGW的切换资源准备及释放过程。 

 


#### Alerting状态下回切（UTRAN GERAN网络信号减弱） 
#### Alerting状态下回切（UTRAN GERAN网络信号减弱） 


业务模型 :UE在E-UTRAN网络中处于Alerting状态。UE从E-UTRAN网络移动到UTRAN/GERAN网络，发生eSRVCC切换。UE收到切换指示后，由于UTRAN/GERAN网络信号减弱，接入UTRAN/GERAN失败，UE取消切换并重新接入E-UTRAN网络。 


信令流程 :Alerting状态下回切（UTRAN/GERAN网络信号减弱）的信令流程如[图1](24-Alerting%E7%8A%B6%E6%80%81%E4%B8%8B%E5%9B%9E%E5%88%87%EF%BC%88UTRAN%20GERAN%E7%BD%91%E7%BB%9C%E4%BF%A1%E5%8F%B7%E5%87%8F%E5%BC%B1%EF%BC%89%EF%BC%88%E9%87%8D%E7%94%A81%EF%BC%89.html#concept1__Alerting%E7%8A%B6%E6%80%81%E4%B8%8B%E5%9B%9E%E5%88%87UTRANGERAN%E7%BD%91%E7%BB%9C%E4%BF%A1%E5%8F%B7%E5%87%8F%E5%BC%B1%E7%9A%84%E4%BF%A1%E4%BB%A4%E6%B5%81%E7%A8%8B-C6BC308B)所示。
图1  Alerting状态下回切（UTRAN/GERAN网络信号减弱）的信令流程


[]images/img-0013541706(%E9%87%8D%E7%94%A81).png)



UE根据当前位置所在E-UTRAN和UTRAN/GERAN网络的信号强度，向eNodeB上传系统测量报告。 


eNodeB基于UE的测量报告，决定触发到UTRAN的SRVCC切换，发送Handover Required消息给MME。 


MME根据语音承载的QCI以及SRVCC HO Indication，MME分离语音承载和其他PS承载，对语音承载发起PS-CS
handover流程，根据Handover Required消息中的TargetRNC-ID查DNS找到eMSC地址，发送SRVCC
PS to CS Request消息。 


eSMC接收PS to CS Request消息后，向RNC发送Relocation Request消息，指示其分配切换所需要的空口资源。 


Target RNC向eSMC返回Relocation Request ACK消息，指示空口资源分配完成。 


eSMC向ATCF发送INVITE消息，携带SDP信息。 


eSMC向MME返回PS to CS Response消息，指示已接受切换请求。 


MME向UE发送Handover Command指示UE进行接入网切换。 


UE接入UTRAN/GERAN网络失败，发送RRC Connection Reestablishment Request消息至eNodeB，请求重新接入E-UTRAN网络。 


eNodeB收到RRC Connection Reestablishment Request消息后，向MME发送Handover
Cancel消息请求取消切换。 


MME向eMSC发送PS to CS Cancel Notification消息指示切换取消。 


eMSC向RNC发送Iu Release Command消息，指示其释放切换所需的空口资源。 


eMSC向MME发送PS to CS Cancel Acknowledge 消息，接受切换取消请求。 


RNC向eSMC发送Iu Release Complete消息，通知其空口资源释放完成。 


 MME向UE发送Notification消息，通知其切换取消。 


MME向eNodeB发送Handover Cancel Acknowledge消息通知其切换已取消。 


UE收到MME的Notification消息后，在原有会话中，发送UPDATE消息给ATCF。 


ATCF发送UPDATE消息给VoLTE AS，消息中携带原会话的SDP。 


VoLTE AS发送200 OK给ATCF，会话重新由E-UTRAN网络接入。 


ATCF发送200 OK给UE。 


VoLTE AS发送480消息给ATCF，释放切换会话资源。 


ATCF发送480消息给eMSC，指示释放eMSC之前建立的切换会话资源。 


eMSC发送ACK消息给ATCF，完成资源释放。 


ATCF发送ACK消息给VoLTE AS。 




缩略语 :缩略语 :AAA :Authentication, Authorization and Accounting鉴权、授权及计费
## AAR 
Answer-Auth-Request应答鉴权请求
## AIA 
Authentication-Information-Answer鉴权信息检索响应
## AIR 
Authentication-Information-Request鉴权信息检索请求
## AKA 
Authentication and Key Agreement鉴权和密钥协商
## AMBR 
Aggregate Maximum Bit Rate聚合最大比特率
## ANM 
Answer
Message应答消息
APN :Access Point Name接入点名称
## AS 
Application Server应用服务器
## ATCF 
Access Transfer Control Function接入转换控制功能
## AUTN 
Authentication Token鉴权令牌
## AVP 
Attribute Value Pair属性值对
## CCA 
Credit Control Answer信用控制应答
## CCR 
Credit Control Request信用控制请求
## CSCF 
Call Session Control Function呼叫对话控制功能
DNS :Domain Name Server域名服务器
E-UTRAN :Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
EPC :Evolved Packet Core演进的分组核心网
EPS :Evolved Packet System演进的分组系统
FQDN :Fully Qualified Domain Name完全限定域名
## GERAN 
GSM/EDGE Radio Access NetworkGSM/EDGE无线接入网
GUTI :Globally Unique Temporary Identity全球唯一临时标识
HLR :Home Location Register归属位置寄存器
HSS :Home Subscriber Server归属用户服务器
## I-CSCF 
Interrogating-Call Session Control Function查询呼叫会话控制功能
## IAM 
Initial Address Message初始地址消息
## ICS 
IMS Centralized ServiceIMS集中式业务提供
## IK 
Integrity Key鉴权密钥
## IM-MGW 
IP Multimedia-Media GatewayIP多媒体媒体网关
IMEI :International Mobile Equipment Identity国际移动设备标识
## IMPI 
IP Multimedia Private IdentityIP多媒体私有标识
## IMPU 
IP Multimedia Public IdentityIP多媒体公有标识
IMS :IP Multimedia SubsystemIP多媒体子系统
IMSI :International Mobile Subscriber Identity国际移动用户标识
## IP-CAN 
IP Connectivity Access NetworkIP连通接入网
## ISIM 
IMS Subscriber Identity ModuleIMS用户身份模块
LTE :Long Time Evolution更长期发展
## MAA 
Multimedia-Authorization-Answer多媒体鉴权响应
## MAP 
Mobile Application Part移动应用部分
## MAR 
Multimedia-Authorization-Request多媒体鉴权请求
## MGW 
Media GateWay媒体网关
MME :Mobile Multimedia E-mail移动多媒体邮件
Mobility Management Entity移动管理实体
MSC :Mobile Switching Center移动交换中心
MSISDN :Mobile Station International Subscriber Directory Number移动台国际用户目录号
P-CSCF :Proxy-Call Session Control Function代理呼叫会话控制功能
## P-GW 
Packet Data Network Gateway分组数据网网关
PCC :Policy and Charging Control计费和策略控制
## PCO 
Protocol Configuration Option协议配置选项
PCRF :Policy and Charging Rules Function策略和计费规则功能
PDN :Packet Data Network分组数据网
PGW :PDN Gateway分组数据网网关
## QCI 
QoS Class IdentifierQoS类别标识
## RAA 
Re-Auth-Answer重新鉴权响应
## RAR 
Re-Auth-Request重新鉴权请求
## RFC 
Remote Feature Control远端特征控制
RNC :Radio Network Controller无线网络控制器
## RRC 
Radio Resource Controller无线资源控制器
## S-CSCF 
Serving-Call Session Control Function服务呼叫会话控制功能
## S-GW 
Serving Gateway服务网关
## SAR 
Server-Assignment-Request服务器指派请求
## SBC 
Session Border Controller会话边界控制器
Session Border Control会话边界控制设备
## SDP 
Session Description Protocol会话描述协议
## SNA 
Subscription-Notification-Answer订阅通知响应
## SNR 
Subscription-Notification-Request订阅通知请求
SPR :Subscription Profile Repository用户签约数据库
## SRVCC 
Single Radio Voice Call Continuity单射频语音呼叫连续性
## TEID 
Tunnel Endpoint Identifier隧道端点标识
## UAA 
User-Authorization- Answer用户授权响应
## UAR 
User-Authorization-Request用户授权请求
## UDA 
User-Data-Answer用户数据响应
UDR :User Data Request用户数据（读取）请求
UE :User Equipment用户设备
## ULA 
Update-Location-Answer位置更新响应
## ULR 
Update-Location-Request位置更新请求
## UMTS 
Universal Mobile Telecommunication System通用移动通讯系统
URI :Uniform Resource Identifier统一资源标识符
## USIM 
User Service Identity Module通用用户身份识别模块
UTRAN :Universal Terrestrial Radio Access Network通用地面无线接入网络
## VLR 
Visitor Location Register拜访位置寄存器
eNodeB :Evolved NodeB演进的NodeB
## eSRVCC 
Enhanced Single Radio Voice Call Continuity增强的双模单待无线语音呼叫连续性
## iFC 
initial Filter Criteria初始过滤规则
