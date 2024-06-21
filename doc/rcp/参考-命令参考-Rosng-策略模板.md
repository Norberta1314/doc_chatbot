# AAA配置命令 
## aaa-accounting-template 

aaa-accounting-template 
命令功能 : 
配置计费模板。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
aaa-accounting-template 
  ＜template-number 
＞
no aaa-accounting-template 
  ＜template-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜template-number＞|计费模板号，范围1-2128
缺省 : 
无 
使用说明 : 
配置计费模板。 
范例 : 
配置计费模板1，进入AAA计费模式：ZXROSNG(config)#aaa-accounting-template 1ZXROSNG(config-aaa-acct-template)#查看计费模板信息：ZXROSNG(config-aaa-acct-template)#show running-config aaa !<AAA>aaa-accounting-template 1$!</AAA>ZXROSNG(config-aaa-acct-template)#show aaa-accounting-template acct-template:1
相关命令 : 
show aaa-accounting-template 
## aaa-accounting-type 

aaa-accounting-type 
命令功能 : 
配置计费类型。 
命令模式 : 
 AAA计费模板模式  
命令默认权限级别 : 
15 
命令格式 : 
aaa-accounting-type 
  {none 
|radius 
|tacacs 
|tacacs-radius 
|radius-tacacs 
}
命令参数解释 : 
参数|描述
---|---
none|不计费
radius|RADIUS计费
tacacs|TACACS计费
tacacs-radius|TACACS计费超时后转RADIUS计费
radius-tacacs|RADIUS计费超时后转TACACS计费
缺省 : 
无 
使用说明 : 
配置计费类型。 
范例 : 
在计费模板1下，配置radius计费方法:ZXROSNG(config)#aaa-accounting-template 1ZXROSNG(config-aaa-acct-template)#aaa-accounting-type radius
相关命令 : 
show aaa-accounting-template 
## aaa-authentication-template 

aaa-authentication-template 
命令功能 : 
配置认证模板。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
aaa-authentication-template 
  ＜template-number 
＞
no aaa-authentication-template 
  ＜template-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜template-number＞|认证模板号，范围：1-2128
缺省 : 
无 
使用说明 : 
配置认证模板。 
范例 : 
1. 配置认证模板1，进入AAA认证模式下：ZXROSNG(config)#aaa-authentication-template 1ZXROSNG(config-aaa-authen-template)#2. 查看AAA配置信息：ZXROSNG(config-aaa-authen-template)#show running-config aaa !<AAA>aaa-authentication-template 1$!</AAA>ZXROSNG(config-aaa-authen-template)#show aaa-authentication-template authen-template:1
相关命令 : 
show aaa-authentication-template 
## aaa-authentication-type 

aaa-authentication-type 
命令功能 : 
配置认证类型
命令模式 : 
 AAA认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
aaa-authentication-type 
  {none 
|local 
|radius 
|local-radius 
|radius-local 
|radius-none 
|tacacs 
|local-tacacs 
|tacacs-local 
|tacacs-none 
|diameter 
|tacacs-radius 
|radius-tacacs 
}
命令参数解释 : 
参数|描述
---|---
none|不认证
local|本地认证
radius|RADIUS远程认证
local-radius|先本地认证，如果用户不存在，再进行RADIUS认证，如果本地认证拒绝，不进行RADIUS认证
radius-local|先RADIUS认证，如果radius配置错误或超时再进行本地认证，如果RADIUS认证拒绝，不进行本地认证
radius-none|先RADIUS认证，如果RADIUS配置错误或超时，则直接通过认证。
tacacs|TACACS远程认证
local-tacacs|先本地认证，如果用户不存在，再进行TACACS认证，如果本地认证拒绝，不进行TACACS认证
tacacs-local|先TACACS认证，如果TACACS配置错误或超时再进行本地认证，如果TACACS认证拒绝，不进行本地认证
tacacs-none|先TACACS认证，如果TACACS配置错误或超时，不认证
diameter|DIAMETER远程认证
tacacs-radius|先TACACS认证，超时后转RADIUS认证
radius-tacacs|先RADIUS认证，超时后转TACACS认证
缺省 : 
无。 
使用说明 : 
配置认证类型 
范例 : 
配在AAA认证模式下，配置RADIUS认证方式：ZXROSNG(config)#aaa-authentication-template 1ZXROSNG(config-aaa-authen-template)#aaa-authentication-type radius
相关命令 : 
show aaa-authentication-template
## aaa-authorization-template 

aaa-authorization-template 
命令功能 : 
配置授权模板。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
aaa-authorization-template 
  ＜template-number 
＞
no aaa-authorization-template 
  ＜template-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜template-number＞|授权模板号，范围：1-2128
缺省 : 
无 
使用说明 : 
配置授权模板。 
范例 : 
配置授权模板1， 进入AAA授权模式下：ZXROSNG(config)#aaa-authorization-template 1ZXROSNG(config-aaa-author-template)#查看授权模板：ZXROSNG(config-aaa-author-template)#show running-config aaa !<AAA>aaa-authorization-template 1$!</AAA>ZXROSNG(config-aaa-author-template)#show aaa-authorization-template 1author-template:1
相关命令 : 
show aaa-authorization-template 
## aaa-authorization-type 

aaa-authorization-type 
命令功能 : 
配置授权类型。 
命令模式 : 
 AAA授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
aaa-authorization-type 
  {none 
|radius-local 
|tacacs-local 
|radius 
|tacacs 
|local 
|local-radius 
|local-tacacs 
|tacacs-radius 
|radius-tacacs 
}
命令参数解释 : 
参数|描述
---|---
none|不授权
radius-local|RADIUS授权超时转local方式
tacacs-local|TACACS授权超时转local方式
radius|RADIUS授权方式
tacacs|TACACS授权方式
local|local授权方式
local-radius|无本地授权后转RADIUS授权
local-tacacs|无本地授权后转TACACS授权
tacacs-radius|TACACS授权超时后转RADIUS授权
radius-tacacs|RADIUS授权超时后转RADIUS授权
缺省 : 
无 
使用说明 : 
配置授权类型。 
范例 : 
在AAA授权模式下，配置mix-tacacs方式：ZXROSNG(config)#aaa-authorization-template 1ZXROSNG(config-aaa-author-template)#aaa-authorization-type tacacs-local
相关命令 : 
show aaa-authorization-template 
## accounting-radius-group 

accounting-radius-group 
命令功能 : 
配置RADIUS计费组。 
命令模式 : 
 AAA计费模板模式  
命令默认权限级别 : 
15 
命令格式 : 
accounting-radius-group 
 first 
 ＜group-name 
＞ [second 
 ＜group-name 
＞]
no accounting-radius-group 
 first 
 second 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS计费服务器组的组名，RADIUS组名长度为1-31个字符。
＜group-name＞|RADIUS计费服务器组的组名，RADIUS组名长度为1-31个字符。
缺省 : 
无 
使用说明 : 
计费模板下，绑定RADIUS计费组，RADIUS计费组必须先配置。 
范例 : 
在AAA计费模式下，配置RADIUS计费组：ZXROSNG(config)#aaa-accounting-template 1ZXROSNG(config-aaa-acct-template)#aaa-accounting-type radiusZXROSNG(config-aaa-acct-template)#accounting-radius-group first 1
相关命令 : 
show aaa-accounting-template 
## accounting-tacacs-group 

accounting-tacacs-group 
命令功能 : 
配置TACACS计费组。 
命令模式 : 
 AAA计费模板模式  
命令默认权限级别 : 
15 
命令格式 : 
accounting-tacacs-group 
  ＜group-name 
＞
no accounting-tacacs-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|绑定TACACS 计费组，前提条件:TACACS 计费组存在。
缺省 : 
无 
使用说明 : 
计费模板下，绑定TACACS计费组，TACACS计费组必须先配置。 
范例 : 
在AAA计费模式下，配置TACACS计费组zte：ZXROSNG(config)#aaa-accounting-template 1ZXROSNG(config-aaa-acct-template)# accounting-tacacs-group zte
相关命令 : 
show aaa-accounting-template 
## authentication-diameter-group 

authentication-diameter-group 
命令功能 : 
配置DIAMETER认证组。 
命令模式 : 
 AAA认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-diameter-group 
  ＜group-name 
＞
no authentication-diameter-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|绑定DIAMETER group 范围：1-10，前提条件：DIAMETER group存在
缺省 : 
无 
使用说明 : 
认证模板下，绑定DIAMETER认证组，DIAMETER认证组必须先配置。 
范例 : 
在AAA认证模板下，配置DIAMETER认证组 1:ZXROSNG(config)#aaa-authentication-template 1ZXROSNG(config-aaa-authen-template)#aaa-authentication-type diameterZXROSNG(config-aaa-authen-template)#authentication-diameter-group 1ZXROSNG(config-aaa-authen-template)#
相关命令 : 
show aaa-authentication-template 
## authentication-radius-group 

authentication-radius-group 
命令功能 : 
配置RADIUS认证组。 
命令模式 : 
 AAA认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-radius-group 
  ＜group-name 
＞
no authentication-radius-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS认证服务器组的组名，RADIUS组名长度为1-31个字符。
缺省 : 
无 
使用说明 : 
认证模板下，绑定RADIUS认证组，RADIUS认证组必须先配置。 
范例 : 
在AAA认证模板下，配置RADIUS 认证组 1:ZXROSNG(config)#aaa-authentication-template 1ZXROSNG(config-aaa-authen-template)#aaa-authentication-type radiusZXROSNG(config-aaa-authen-template)#authentication-radius-group 1ZXROSNG(config-aaa-authen-template)#
相关命令 : 
show aaa-authentication-template 
## authentication-tacacs-group 

authentication-tacacs-group 
命令功能 : 
配置TACACS认证组。 
命令模式 : 
 AAA认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-tacacs-group 
  ＜group-name 
＞
no authentication-tacacs-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|绑定TACACS认证组，前提条件TACACS组存在
缺省 : 
无 
使用说明 : 
认证模板下，绑定TACACS认证组，TACACS组必须先配置。 
范例 : 
在AAA认证模板下，配置TACACS组 zte：ZXROSNG(config)#aaa-authentication-template 1ZXROSNG(config-aaa-authen-template)#aaa-authentication-type tacacsZXROSNG(config-aaa-authen-template)#authentication-tacacs-group zteZXROSNG(config-aaa-authen-template)#
相关命令 : 
show aaa-authentication-template 
## authorization-radius-group 

authorization-radius-group 
命令功能 : 
设置授权的radius组号 
命令模式 : 
 AAA授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
authorization-radius-group 
  ＜group-name 
＞
no authorization-radius-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS授权服务器组的组名，RADIUS组名长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
RADIUS组名长度为1-31个字符。该命令只在aaa-authorization-template模式下配置以下命令时生效：aaa-authorization-type radius。另外，该命令参数为radius组名，该组名必须事先在以下命令中配置：radius authentication-group <group-name>。
范例 : 
ZXROSNG(config)#radius authentication-group zteZXROSNG(config-authgrp-zte)#exitZXROSNG(config)#aaa-authorization-template 2010ZXROSNG(config-aaa-author-template)#authorization-radius-group zteZXROSNG(config-aaa-author-template)#ZXROSNG(config)#radius authentication-group zte
相关命令 : 
aaa-authorization-typeradius authentication-group 
## authorization-tacacs-group 

authorization-tacacs-group 
命令功能 : 
配置TACACS授权组。 
命令模式 : 
 AAA授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
authorization-tacacs-group 
  ＜group-name 
＞
no authorization-tacacs-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|绑定TACACS授权组，前提条件 TACACS 组存在。
缺省 : 
无 
使用说明 : 
授权模板下，绑定TACACS授权组，TACACS 组必须先配置。 
范例 : 
在AAA授权模式下，配置TACACS 授权组zte：ZXROSNG(config)#aaa-authorization-template 1ZXROSNG(config-aaa-author-template)#authorization-tacacs-group zte
相关命令 : 
show aaa-authorization-template 
description : 

description 
命令功能 : 
配置认证模板的描述信息。 
命令模式 : 
 AAA认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
description 
  ＜description-word 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜description-word＞|在认证模式下，配置描述信息，长度为1~31个字符
缺省 : 
无 
使用说明 : 
配置认证模板描述信息。 
范例 : 
AAA认证模式下，配置描述信息：ZXROSNG(config)#aaa-authentication-template 1ZXROSNG(config-aaa-authen-template)#description aaa-authen-descript 
相关命令 : 
show aaa-authentication-template 
description : 

description 
命令功能 : 
配置授权模板的描述信息。 
命令模式 : 
 AAA授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
description 
  ＜description-word 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜description-word＞|在授权模式下，配置描述信息，长度为1~31个字符
缺省 : 
无 
使用说明 : 
配置授权模板描述信息。 
范例 : 
AAA授权模式下，配置描述信息：ZXROSNG(config)#aaa-authorization-template 1ZXROSNG(config-aaa-author-template)#description aaa-author-descript
相关命令 : 
show aaa-authorization-template 
description : 

description 
命令功能 : 
配置计费模板的描述信息。 
命令模式 : 
 AAA计费模板模式  
命令默认权限级别 : 
15 
命令格式 : 
description 
  ＜description-word 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜description-word＞|在计费模式下，配置描述信息，长度为1~31个字符
缺省 : 
无 
使用说明 : 
配置计费模板描述信息。 
范例 : 
AAA计费模式下，配置描述信息：ZXROSNG(config)#aaa-accounting-template 1ZXROSNG(config-aaa-acct-template)#description aaa-accounting-descript
相关命令 : 
show aaa-accounting-template 
## show aaa-accounting-template 

show aaa-accounting-template 
命令功能 : 
显示计费模板配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aaa-accounting-template 
  [＜template-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜template-number＞|计费模板号，范围：1-2128；如果不带参数，则显示全部。
缺省 : 
无 
使用说明 : 
查看计费模板配置信息。 
范例 : 
在配置模式下，查看计费模板1：ZXROSNG(config)#aaa-accounting-template 1ZXROSNG(config-aaa-acct-template)#aaa-accounting-type radiusZXROSNG(config-aaa-acct-template)#accounting-radius-group first 1ZXROSNG(config)#show aaa-accounting-template 1acct-template:1acct-type:radiusfirst-radius-group:1
相关命令 : 
aaa-accounting-template 
## show aaa-authentication-template 

show aaa-authentication-template 
命令功能 : 
显示认证模板配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aaa-authentication-template 
  [＜template-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜template-number＞|认证模板号，范围：1-2128；如果不带参数，则显示全部。
缺省 : 
无 
使用说明 : 
查看认证模板配置信息。 
范例 : 
查看所有认证模板：ZXROSNG(config-aaa-authen-template)#show aaa-authentication-template authen-template:2001authen-type:localauthen-template:2002authen-type:tacacsauthen-tacacs-group:t1authen-template:2128authen-type:radiusauthen-radius-group:1authen-template:1
相关命令 : 
aaa-authentication-template 
## show aaa-authorization-template 

show aaa-authorization-template 
命令功能 : 
显示授权模板配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aaa-authorization-template 
  [＜template-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜template-number＞|授权模板号，范围：1-2128；如果不带参数，则显示全部。
缺省 : 
无 
使用说明 : 
查看授权模板配置信息。 
范例 : 
在配置模式下，查看授权模板1：ZXROSNG(config)#aaa-authorization-template 1ZXROSNG(config-aaa-author-template)#aaa-authorization-type tacacsZXROSNG(config-aaa-author-template)#authorization-tacacs-group zteZXROSNG(config)# show aaa-authorization-template 1author-template:1author-type:tacacsauthor-tacacs-group:zte
相关命令 : 
aaa-authorization-template 
# ACLv6配置命令 
## ipv6-access-list 

ipv6-access-list 
命令功能 : 
该命令工作于全局配置模式下，用于创建一个IPv6 ACL(访问控制列表)并进入此IPv6 ACL的配置模式。    如果此IPv6 ACL已经存在，直接进入IPv6 ACL配置模式。    如果此IPv6 ACL不存在，表示新建一个IPv6 ACL，并进入IPv6 ACL配置模式。进入IPv6 ACL配置模式后，主要可配置以下内容：    配置IPv6 ACL规则。在IPv6 ACL配置模式下，可使用rule命令配置IPv6 ACL规则。用于控制网络流量，哪些特征的流程可以通过，哪些特征的流量不可以通过。从而达到控制访问的目的。    调整规则的顺序。在IPv6 ACL配置模式下，可使用move命令修改规则的ID，从而达到调整列表中规则顺序的目的。IPv6 ACL列表中的规则是按照规则ID从小到大的顺寻排量生效的。    清空该ACL下的所有规则在IPv6 ACL配置模式下，可使用no rule all命令删除当前ACL列表下的所有规则。在网络中现在的流量越来越大，所以必须对流量进行控制和管理。ACL主要作用就是对网络中的流量进行控制，哪些允许通过哪些拒绝通过；对网络中的流量进行分类，方便对流量进行管理。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-list 
  ＜acl-name 
＞
no ipv6-access-list 
  ＜acl-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|IPv4 ACL列表的名称。取值范围：0~31个字符。
缺省 : 
无 
使用说明 : 
当创建了一个IPv6 ACL后，还需要使用rule命令配置IPv6 ACL规则，这样才是一个有效的IPv6 ACL访问控制列表。最多可以配置4000个IPv6 ACL访问控制列表。
范例 : 
用ipv6-access-list命令进入myacl的配置模式，并配置规则：ZXROSNG(config)#ipv6-access-list myaclZXROSNG(config-ipv6-acl)#rule deny tcp any anyZXROSNG(config-ipv6-acl)#show ipv6-access-listsipv6-access-list myacl 1/1 (showed/total)   10 deny tcp any anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#no ipv6-access-list myacl
相关命令 : 
show ipv6-access-lists 
## move 

move 
命令功能 : 
调整改变ACL列表中规则的编号顺序。 
命令模式 : 
 IPv6-ACL模式  
命令默认权限级别 : 
15 
命令格式 : 
move 
  ＜old-rule-id 
＞ ＜new-rule-id 
＞
命令参数解释 : 
参数|描述
---|---
＜old-rule-id＞|需要调整的规则ID,范围1-$#33685536#$
＜new-rule-id＞|调整后的新规则ID，范围1-$#33685536#$
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#ipv6-access-list myaclZXROSNG(config-ipv6-acl)#rule 1 deny tcp 1::2/12 any ZXROSNG(config-ipv6-acl)#rule 2 deny udp 2::3/12 anyZXROSNG(config-ipv6-acl)#move 1 3查看命令配置结果：ZXROSNG(config-ipv6-acl)#sho ipv6-access-lists name myaclipv6-access-list myacl 2/2 (showed/total)   2 deny udp 2::3/12 any   3 deny tcp 1::2/12 anyZXROSNG(config-ipv6-acl)#
相关命令 : 
show ipv6-access-lists 
## resequence-access-list ipv6 

resequence-access-list ipv6 
命令功能 : 
对指定ACL列表的规则进行重新编号。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
resequence-access-list ipv6 
  ＜acl-name 
＞ [＜base-rule-id 
＞ [＜increment 
＞]]
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
＜base-rule-id＞|rule-id的基值，重新编号成功后第一个规则的编号,默认为10，取值范围：1–$#33685536#$
＜increment＞|rule-id的步进，重新编号成功后每个规则rule-id之间的差值，默认为10，取值范围：1–$#33685536#$
缺省 : 
<base-rule-id>默认为10。<increment>默认为10。
使用说明 : 
89交换机项目不支持该命令。该命令是对已经存在的ACL列表中的所有规则的ID进行重新编号，规则原来的顺序保持不变，命令最后两个参数都是可选的，不设置的话默认值都是10。
范例 : 
ZXROSNG(config)#ipv6-access-list myaclZXROSNG(config-ipv6-acl)#rule 1 deny tcp 1::2:0/12 any ZXROSNG(config-ipv6-acl)#rule 2 deny udp 1::2:0/12 any                      ZXROSNG(config-ipv6-acl)#rule 3 deny ipv6 1::2:0/12 any                          ZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#resequence-access-list ipv6 myacl 10 10查看结果配置信息：ZXROSNG(config)#show ipv6-access-lists name myaclipv6-access-list myacl 3/3 (showed/total)   10 deny tcp 1::2:0/12 any   20 deny udp 1::2:0/12 any   30 deny ipv6 1::2:0/12 any
相关命令 : 
show ipv6-access-lists 
## rule 

rule 
命令功能 : 
配置/删除IPv6 ACL的规则。 
命令模式 : 
 IPv6-ACL模式  
命令默认权限级别 : 
15 
命令格式 : 
rule 
  [＜rule-id 
＞] {permit 
|deny 
} [flowlabel 
 ＜flowlabel-value 
＞] {sctp 
 {any 
|＜source-ipv6-address-mask 
＞} [{{eq 
|ge 
|le 
} {＜sctp-port-type 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {any 
|＜destination-ipv6-address-mask 
＞} [{{eq 
|ge 
|le 
} {＜sctp-port-type 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}]|udp 
 {any 
|＜source-ipv6-address-mask 
＞} [{{eq 
|ge 
|le 
} {＜udp-port-type 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {any 
|＜destination-ipv6-address-mask 
＞} [{{eq 
|ge 
|le 
} {＜udp-port-type 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}]|icmp 
 {any 
|＜source-ipv6-address-mask 
＞} {any 
|＜destination-ipv6-address-mask 
＞} [{＜icmp-type 
＞|＜icmp-type 
＞} [＜icmp-code 
＞]]|{＜protocol-type 
＞|＜ip-protocol-number 
＞} {any 
|＜source-ipv6-address-mask 
＞} {any 
|＜destination-ipv6-address-mask 
＞}|tcp 
 {any 
|＜source-ipv6-address-mask 
＞} [{{eq 
|ge 
|le 
} {＜tcp-port-type 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {any 
|＜destination-ipv6-address-mask 
＞} [{{eq 
|ge 
|le 
} {＜tcp-port-type 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}] [{[established 
],[rst 
 {-  
|+  
}],[ack 
 {-  
|+  
}],[fin 
 {-  
|+  
}],[syn 
 {-  
|+  
}],[psh 
 {-  
|+  
}],[urg 
 {-  
|+  
}]}]} [{dscp 
 ＜dscp-value 
＞|traffic-class 
 ＜Traffic_Class 
＞}] [{[routing 
],[authen 
],[destopts 
],[fragments 
],[hop-by-hop 
],[esp 
]}] [time-range 
 ＜time-range-name 
＞]
no rule 
  {＜rule-id 
＞|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜rule-id＞|规则ID，范围：1–$#33685536#$
permit|关键字，指明是permit规则
deny|关键字，指明是deny规则
＜flowlabel-value＞|流标签可用来标记特定流的报文,取值范围0-1048575
sctp|IPv6协议类型，SCTP（流控制传输协议）
any|表示任意源或目的IP地址
＜source-ipv6-address-mask＞|源Ipv6地址，CIDR记法
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜sctp-port-type＞|SCTP知名端口类型，可以是关键字discard、ftp-data、ftp、ssh、http、bgp、https中的一个
＜source-port-number＞|SCTP协议源端口号，范围0-65535
range|针对端口的操作range类型关键字
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
any|表示任意源或目的IP地址
＜destination-ipv6-address-mask＞|目的Ipv6地址，CIDR记法
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜sctp-port-type＞|SCTP知名端口类型，可以是关键字discard、ftp-data、ftp、ssh、http、bgp、https中的一个
＜destination-port-number＞|SCTP协议目的端口号，范围0-65535
range|针对端口的操作range类型关键字
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
udp|UDP报文类型
any|表示任意源或目的IP地址
＜source-ipv6-address-mask＞|源Ipv6地址，CIDR记法
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜udp-port-type＞|udp端口类型，可以是关键字domain、bootps、bootpc、tftp、ntp、snmp、snmptrap、pim-auto-rp、rip
＜source-port-number＞|UDP源端口号
range|针对端口的操作range类型关键字
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
any|表示任意源或目的IP地址
＜destination-ipv6-address-mask＞|目的Ipv6地址，CIDR记法
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜udp-port-type＞|UDP端口类型，可以是关键字domain、bootps、bootpc、tftp、ntp、snmp、snmptrap、pim-auto-rp、rip
＜destination-port-number＞|UDP目的端口号
range|针对端口的操作range类型关键字
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
icmp|ICMP报文类型
any|表示任意源或目的IP地址
＜source-ipv6-address-mask＞|源Ipv6地址，CIDR记法
any|表示任意源或目的IP地址
＜destination-ipv6-address-mask＞|目的Ipv6地址，CIDR记法
＜icmp-type＞|ICMP报文类型字段，取值范围0-255
＜icmp-type＞|ICMP报文类型字段，取值范围0-255
＜icmp-code＞|ICMP消息类型，范围0-255
＜protocol-type＞|IPv6协议名称
＜ip-protocol-number＞|IP协议号的范围：0–255
any|表示任意源或目的IP地址
＜source-ipv6-address-mask＞|源Ipv6地址，CIDR记法
any|表示任意源或目的IP地址
＜destination-ipv6-address-mask＞|目的Ipv6地址，CIDR记法
tcp|TCP报文类型
any|表示任意源或目的IP地址
＜source-ipv6-address-mask＞|源Ipv6地址，CIDR记法
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜tcp-port-type＞|TCP端口号名称
＜source-port-number＞|TCP源端口号
range|针对端口的操作range类型关键字
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
any|表示任意源或目的IP地址
＜destination-ipv6-address-mask＞|目的Ipv6地址，CIDR记法
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜tcp-port-type＞|TCP端口号名称
＜destination-port-number＞|TCP目的端口号
range|针对端口的操作range类型关键字
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
established|TCP建链标记
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
＜dscp-value＞|DSCP字段，值范围：0–63
＜Traffic_Class＞|业务类别
routing|路由选项头
authen|认证选项头
destopts|目标选项头
fragments|分段头
hop-by-hop|逐跳头
esp|加密选项头
＜time-range-name＞|时间范围选项，关联已经配置的time-range名称
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置一条TCP规则,当源地址在1::2/12子网范围内，源端口在1000–2000范围内，dscp为6的IPv6建链TCP报文匹配，动作为permit：ZXROSNG(config-ipv6-acl)#rule permit tcp 1::2/12 range 1000-2000 any established dscp 6
相关命令 : 
show ipv6-access-lists 
## show ipv6-access-lists 

show ipv6-access-lists 
命令功能 : 
显示配置的IPv6 ACL规则信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ipv6-access-lists 
  [{[config 
]|[name 
 ＜acl-name 
＞ [from 
 ＜begin-rule-id 
＞ to 
 ＜end-rule-id 
＞]] [usage 
 ＜interface-name 
＞ {egress 
|ingress 
} port-acl 
]|[brief 
 [name 
 ＜acl-name 
＞]]}] 
命令参数解释 : 
参数|描述
---|---
config|显示ACL的配置信息，如已配置多少条，配置上限等
＜acl-name＞|ACL名称,如不指定该参数，则显示所有IPv6 ACL，长度1–31个字符
＜begin-rule-id＞|需要显示规则的起始ID
＜end-rule-id＞|需要显示规则的结束ID
usage|统计信息，统计的是ACL规则被命中的次数（仅适用于配置了log的规则）
＜interface-name＞|接口名称
egress|用于指定需要统计的ACL所在的接口出方向。与ingress两者二选一。
ingress|用于指定需要统计的ACL所在的接口入方向。与egress两者二选一。
port-acl|用于指定接口上使用ACL的业务类型。(目前只支持port-acl业务。)
brief|显示ACL的简要信息
＜acl-name＞|ACL名称,如不指定该参数，则显示所有IPv6 ACL，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-ipv6-acl)#show ipv6-access-listsipv6-access-list myacl                                           4/4 (showed/total)  10 deny tcp 12::12/12 any   11 permit tcp 12::13/13 any  range 1000-2000   15 permit tcp 12::14/14 any  20 deny tcp 12::15/15 any
相关命令 : 
ipv6-access-list 
# ACL配置命令 
## ipv4-access-group egress 

ipv4-access-group egress 
命令功能 : 
绑定IPv4 ACL到接口出方向。 
命令模式 : 
 smartgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-group egress 
  ＜acl-name 
＞
no ipv4-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv4 ACL MyACL 到smartgroup1的出方向:ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ipv4-access-group egress MyACL显示配置结果：ZXROSNG(config-if-smartgroup1)#show ipv4-access-groups===============================================================================Interface name:smartgroup1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress      MyACLZXROSNG(config-if-smartgroup1)#删除gei-0/1/0/1出方向的ACL:ZXROSNG(config-if-smartgroup1)#no ipv4-access-group egress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group egress 

ipv4-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 10G以太接口模式,pos子接口模式,pos接口模式,smartgroup子接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
千兆以太接口模式:15,以太接口模式:15,pos接口模式:15,smartgroup子接口模式:15,10G以太接口模式:15,pos子接口模式:15 
命令格式 : 
ipv4-access-group egress 
  ＜acl-name 
＞
no ipv4-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config)#ipv4-access-group interface gei-0/1/0/1 egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       myacl
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group egress 

ipv4-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 multilink接口模式,posgroup接口模式,supervlan接口模式  
命令默认权限级别 : 
multilink接口模式:15,supervlan接口模式:15,posgroup接口模式:15 
命令格式 : 
ipv4-access-group egress 
  ＜acl-name 
＞
no ipv4-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config)#ipv4-access-group interface gei-0/1/0/1 egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       myacl
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group egress 

ipv4-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 dsl接口模式,serial接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
通道化ce1接口模式:15,ulei接口模式:15,通道化cpos_e1接口模式:15,ulei子接口模式:15,dsl接口模式:15,serial接口模式:15 
命令格式 : 
ipv4-access-group egress 
  ＜acl-name 
＞
no ipv4-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config)#ipv4-access-group interface gei-0/1/0/1 egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       myacl
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group egress 

ipv4-access-group egress 
命令功能 : 
绑定IPv4 ACL到接口出方向。 
命令模式 : 
 qx子接口模式,qx接口模式  
命令默认权限级别 : 
qx接口模式:15,qx子接口模式:15 
命令格式 : 
ipv4-access-group egress 
  ＜acl-name 
＞
no ipv4-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv4 ACL MyACL 到gei-0/1/0/1的出方向:ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group egress MyACL显示配置结果：ZXROSNG(config-if-gei-0/1/0/1)#show ipv4-access-groups===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       MyACLZXROSNG(config-if-gei-0/1/0/1)#删除gei-0/1/0/1出方向的ACL:ZXROSNG(config-if-gei-0/1/0/1)#no ipv4-access-group egress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group egress 

ipv4-access-group egress 
命令功能 : 
绑定IPv4 ACL到接口出方向。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-group egress 
  ＜acl-name 
＞
no ipv4-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv4 ACL MyACL 到gei-0/1/0/1的出方向:ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group egress MyACL显示配置结果：ZXROSNG(config-if-gei-0/1/0/1)#show ipv4-access-groups===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       MyACLZXROSNG(config-if-gei-0/1/0/1)#删除gei-0/1/0/1出方向的ACL:ZXROSNG(config-if-gei-0/1/0/1)#no ipv4-access-group egress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group ingress 

ipv4-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 10G以太接口模式,pos子接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
千兆以太接口模式:15,以太接口模式:15,smartgroup子接口模式:15,pos接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,pos子接口模式:15 
命令格式 : 
ipv4-access-group ingress 
  ＜acl-name 
＞
no ipv4-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       myacl
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group ingress 

ipv4-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 multilink接口模式,posgroup接口模式,supervlan接口模式  
命令默认权限级别 : 
multilink接口模式:15,supervlan接口模式:15,posgroup接口模式:15 
命令格式 : 
ipv4-access-group ingress 
  ＜acl-name 
＞
no ipv4-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       myacl
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group ingress 

ipv4-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 dsl接口模式,serial接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
通道化ce1接口模式:15,ulei接口模式:15,通道化cpos_e1接口模式:15,ulei子接口模式:15,dsl接口模式:15,serial接口模式:15 
命令格式 : 
ipv4-access-group ingress 
  ＜acl-name 
＞
no ipv4-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       myacl
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group ingress 

ipv4-access-group ingress 
命令功能 : 
绑定IPv4 ACL到接口入方向。 
命令模式 : 
 qx子接口模式,qx接口模式  
命令默认权限级别 : 
qx接口模式:15,qx子接口模式:15 
命令格式 : 
ipv4-access-group ingress 
  ＜acl-name 
＞
no ipv4-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv4 ACL MyACL 到gei-0/1/0/1的入方向:ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group ingress MyACL显示配置结果：ZXROSNG(config-if-gei-0/1/0/1)#show ipv4-access-groups ===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       MyACLZXROSNG(config-if-gei-0/1/0/1)#删除gei-0/1/0/1入方向的ACL:ZXROSNG(config-if-gei-0/1/0/1)#no ipv4-access-group ingress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group ingress 

ipv4-access-group ingress 
命令功能 : 
绑定IPv4 ACL到接口入方向。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-group ingress 
  ＜acl-name 
＞
no ipv4-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv4 ACL MyACL 到gei-0/1/0/1的入方向:ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4-access-group ingress MyACL显示配置结果：ZXROSNG(config-if-gei-0/1/0/1)#show ipv4-access-groups===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       MyACLZXROSNG(config-if-gei-0/1/0/1)#删除gei-0/1/0/1入方向的ACL:ZXROSNG(config-if-gei-0/1/0/1)#no ipv4-access-group ingress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group interface &amp;lt;mid&amp;gt; egress 

ipv4-access-group interface <mid> egress 
命令功能 : 
绑定IPv4 ACL到接口出方向。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-group interface  
 ＜interface-list 
＞ egress 
  ＜acl-name 
＞
no ipv4-access-group interface  
 ＜interface-list 
＞ egress 
命令参数解释 : 
参数|描述
---|---
＜interface-list＞|接口名称列表，支持批量绑定多个接口。
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
绑定接口时，接口必须存在，可以绑定不存在的ACL。解绑定接口时，接口必须存在。
范例 : 
绑定IPv4 ACL MyACL 到gei-0/1/0/1的出方向:ipv4-access-group interface gei-0/1/0/1 egress MyACL显示配置结果：ZXROSNG(config)#show ipv4-access-groups===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress      MyACLZXROSNG(config)#删除gei-0/1/0/1出方向的ACL:ZXROSNG(config)#no ipv4-access-group interface gei-0/1/0/1 egress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-group interface &amp;lt;mid&amp;gt; ingress 

ipv4-access-group interface <mid> ingress 
命令功能 : 
绑定IPv4 ACL到接口入方向。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-group interface  
 ＜interface-list 
＞ ingress 
  ＜acl-name 
＞
no ipv4-access-group interface  
 ＜interface-list 
＞ ingress 
命令参数解释 : 
参数|描述
---|---
＜interface-list＞|接口名称列表，支持批量绑定多个接口。
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
绑定接口时，接口必须存在，可以绑定不存在的ACL。解绑定接口时，接口必须存在。
范例 : 
绑定IPv4 ACL MyACL 到gei-0/1/0/1的入方向:ipv4-access-group interface gei-0/1/0/1 ingress MyACL显示配置结果：ZXROSNG(config)#show ipv4-access-groups===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress      MyACL删除gei-0/1/0/1入方向的ACL:ZXROSNG(config)#no ipv4-access-group interface gei-0/1/0/1 ingress
相关命令 : 
show ipv4-access-groups 
## ipv4-access-list 

ipv4-access-list 
命令功能 : 
该命令工作于全局配置模式下，用于创建一个IPv4 ACL(访问控制列表)并进入此IPv4 ACL的配置模式。    如果此IPv4 ACL已经存在，直接进入IPv4 ACL配置模式。    如果此IPv4 ACL不存在，表示新建一个IPv4 ACL，并进入IPv4 ACL配置模式。进入IPv4 ACL配置模式后，主要可配置以下内容：    配置IPv4 ACL规则。在IPv4 ACL配置模式下，可使用rule命令配置IPv4 ACL规则。用于控制网络流量，哪些特征的流程可以通过，哪些特征的流量不可以通过。从而达到控制访问的目的。    调整规则的顺序。在IPv4 ACL配置模式下，可使用move命令修改规则的ID，从而达到调整列表中规则顺序的目的。IPv4 ACL列表中的规则是按照规则ID从小到大的顺寻排量生效的。    清空该ACL下的所有规则在IPv4 ACL配置模式下，可使用no rule all命令删除当前ACL列表下的所有规则。在网络中现在的流量越来越大，所以必须对流量进行控制和管理。ACL主要作用就是对网络中的流量进行控制，哪些允许通过哪些拒绝通过；对网络中的流量进行分类，方便对流量进行管理。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-list 
  ＜acl-name 
＞
no ipv4-access-list 
  ＜acl-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|IPv4 ACL列表的名称。取值范围：0~31个字符。
缺省 : 
无 
使用说明 : 
当创建了一个IPv4 ACL后，还需要使用rule命令配置IPv4 ACL规则，这样才是一个有效的IPv4 ACL访问控制列表。最多可以配置4000个IPv4 ACL访问控制列表。
范例 : 
ZXROSNG(config)#ipv4-access-list myaclZXROSNG(config-ipv4-acl)#rule deny any ZXROSNG(config-ipv4-acl)#exZXROSNG(config)#no ipv4-access-list myacl
相关命令 : 
show ipv4–access-lists 
## ipv6-access-group egress 

ipv6-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 10G以太接口模式,pos接口模式,smartgroup接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
以太接口模式:15,千兆以太接口模式:15,pos接口模式:15,10G以太接口模式:15,smartgroup接口模式:15 
命令格式 : 
ipv6-access-group egress 
  ＜acl-name 
＞
no ipv6-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1Interface name|vlan   Direction ACL name                        Default action------------------------------------------------------------------------------- gei-0/1/0/1 Egress myacl 
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group egress 

ipv6-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 multilink接口模式,posgroup接口模式,supervlan接口模式  
命令默认权限级别 : 
multilink接口模式:15,supervlan接口模式:15,posgroup接口模式:15 
命令格式 : 
ipv6-access-group egress 
  ＜acl-name 
＞
no ipv6-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Egress myacl 
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group egress 

ipv6-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 smartgroup子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-group egress 
  ＜acl-name 
＞
no ipv6-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1 Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Egress myacl 
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group egress 

ipv6-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 dsl接口模式,serial接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
通道化ce1接口模式:15,ulei接口模式:15,通道化cpos_e1接口模式:15,ulei子接口模式:15,dsl接口模式:15,serial接口模式:15 
命令格式 : 
ipv6-access-group egress 
  ＜acl-name 
＞
no ipv6-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Egress myacl 
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group egress 

ipv6-access-group egress 
命令功能 : 
绑定IPv6 ACL到接口出方向。 
命令模式 : 
 qx子接口模式,qx接口模式  
命令默认权限级别 : 
qx接口模式:15,qx子接口模式:15 
命令格式 : 
ipv6-access-group egress 
  ＜acl-name 
＞
no ipv6-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv6 ACL MyACL 到gei-0/1/0/1的出方向:ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group egress MyACL显示配置结果：ZXROSNG(config-if-gei-0/1/0/1)#show ipv6-access-groups Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Egress MyACLZXROSNG(config-if-gei-0/1/0/1)#删除gei-0/1/0/1出方向的ACL:ZXROSNG(config-if-gei-0/1/0/1)#no ipv6-access-group egressZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group egress 

ipv6-access-group egress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-group egress 
  ＜acl-name 
＞
no ipv6-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group egress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Egress myacl 
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group ingress 

ipv6-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 10G以太接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
以太接口模式:15,千兆以太接口模式:15,smartgroup子接口模式:15,pos接口模式:15,10G以太接口模式:15,smartgroup接口模式:15 
命令格式 : 
ipv6-access-group ingress 
  ＜acl-name 
＞
no ipv6-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1 Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress myacl 
相关命令 : 
show ipv6-access-groups
## ipv6-access-group ingress 

ipv6-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 multilink接口模式,posgroup接口模式,supervlan接口模式  
命令默认权限级别 : 
multilink接口模式:15,supervlan接口模式:15,posgroup接口模式:15 
命令格式 : 
ipv6-access-group ingress 
  ＜acl-name 
＞
no ipv6-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1 Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress myacl 
相关命令 : 
show ipv6-access-groups
## ipv6-access-group ingress 

ipv6-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 dsl接口模式,serial接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
通道化ce1接口模式:15,ulei接口模式:15,通道化cpos_e1接口模式:15,ulei子接口模式:15,dsl接口模式:15,serial接口模式:15 
命令格式 : 
ipv6-access-group ingress 
  ＜acl-name 
＞
no ipv6-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1 Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress myacl 
相关命令 : 
show ipv6-access-groups
## ipv6-access-group ingress 

ipv6-access-group ingress 
命令功能 : 
绑定IPv6 ACL到接口入方向。 
命令模式 : 
 qx子接口模式,qx接口模式  
命令默认权限级别 : 
qx接口模式:15,qx子接口模式:15 
命令格式 : 
ipv6-access-group ingress 
  ＜acl-name 
＞
no ipv6-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定IPv6 ACL MyACL 到gei-0/1/0/1的入方向:ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group ingress MyACL显示配置结果：ZXROSNG(config-if-gei-0/1/0/1)#show ipv6-access-groups Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1                       Ingress    MyACLZXROSNG(config-if-gei-0/1/0/1)#删除gei-0/1/0/1入方向的ACL:ZXROSNG(config-if-gei-0/1/0/1)#no ipv6-access-group ingress
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group ingress 

ipv6-access-group ingress 
命令功能 : 
绑定ACL列表到接口。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-group ingress 
  ＜acl-name 
＞
no ipv6-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1：ZXROSNG(config-if-gei-0/1/0/1)#ipv6-access-group ingress myacl 查看配置结果信息：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress myacl 
相关命令 : 
show ipv6-access-groups
## ipv6-access-group interface &amp;lt;mid&amp;gt; egress 

ipv6-access-group interface <mid> egress 
命令功能 : 
绑定IPv6 ACL到接口出方向。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-group interface  
 ＜interface-list 
＞ egress 
  ＜acl-name 
＞
no ipv6-access-group interface  
 ＜interface-list 
＞ egress 
命令参数解释 : 
参数|描述
---|---
＜interface-list＞|接口名称列表，支持批量绑定多个接口。
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
绑定接口时，接口必须存在，可以绑定不存在的ACL。解绑定接口时，接口必须存在。
范例 : 
绑定IPv6 ACL MyACL 到gei-0/1/0/1的出方向:ipv6-access-group interface gei-0/1/0/1 egress MyACL显示配置结果：ZXROSNG(config)#show ipv6-access-groups Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1                       Egress     MyACLZXROSNG(config)#删除gei-0/1/0/1出方向的ACL:ZXROSNG(config)#no ipv6-access-group interface gei-0/1/0/1 egress
相关命令 : 
show ipv6-access-groups 
## ipv6-access-group interface &amp;lt;mid&amp;gt; ingress 

ipv6-access-group interface <mid> ingress 
命令功能 : 
绑定IPv6 ACL到接口入方向。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-group interface  
 ＜interface-list 
＞ ingress 
  ＜acl-name 
＞
no ipv6-access-group interface  
 ＜interface-list 
＞ ingress 
命令参数解释 : 
参数|描述
---|---
＜interface-list＞|接口名称列表，支持批量绑定多个接口。
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
绑定接口时，接口必须存在，可以绑定不存在的ACL。解绑定接口时，接口必须存在。
范例 : 
绑定IPv6 ACL MyACL 到gei-0/1/0/1的入方向:ipv6-access-group interface gei-0/1/0/1 ingress MyACL显示配置结果：ZXROSNG(config)#show ipv6-access-groupsInterface name|vlan   Direction ACL name                        Default action------------------------------------------------------------------------------- gei-0/1/0/1                       Ingress    MyACLZXROSNG(config)#删除gei-0/1/0/1入方向的ACL:ZXROSNG(config)#no ipv6-access-group interface gei-0/1/0/1 ingress
相关命令 : 
show ipv6-access-groups 
## move 

move 
命令功能 : 
该命令工作于IPv4 ACL配置模式下，用于修改IPv4 ACL规则的ID。 
命令模式 : 
 IPv4-ACL模式  
命令默认权限级别 : 
15 
命令格式 : 
move 
  ＜old-rule-id 
＞ ＜new-rule-id 
＞
命令参数解释 : 
参数|描述
---|---
＜old-rule-id＞|修改前规则的ID，必须已经存在。范围1-$#33685536#$
＜new-rule-id＞|修改后的新规则ID，该ID必须以前不存在。范围1-$#33685536#$
缺省 : 
无 
使用说明 : 
ACL列表按照规则ID从小到大排序，修改ID会调整规则在列表中的顺序。该命令必须在自动提交模式下执行，不能在手动提交模式下执行。
范例 : 
配置2条ACL规则，rule-id分别为1和2，如果想把规则1调整成规则3，则需要调用move命令：ZXROSNG(config)#ipv4-access-list myaclZXROSNG(config-ipv4-acl)#rule 1 deny tcp 192.168.0.10 0.0.0.0 any ZXROSNG(config-ipv4-acl)#rule 2 deny tcp 192.168.0.100 0.0.0.0 anyZXROSNG(config-ipv4-acl)#move 1 3查看命令配置结果：ZXROSNG(config-ipv4-acl)#show ipv4-access-lists name  myaclipv4-access-list myacl2/2 (showed/total)2 deny tcp 192.168.0.100 0.0.0.0 any3 deny tcp 192.168.0.10 0.0.0.0 any
相关命令 : 
show ipv4–access-lists 
## resequence-access-list ipv4 

resequence-access-list ipv4 
命令功能 : 
对指定ACL表的规则进行重新编号，但不改变规则的顺序。当一个ACL中的规则频繁的被调整后，列表中的规则ID会比较杂乱，给维护带来不便。此时，可以使用该命令，从新对ACL列表中的规则ID进行排列，使规则ID成为一个等差数列。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
resequence-access-list ipv4 
  ＜acl-name 
＞ [＜base-rule-id 
＞ [＜increment 
＞]]
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|需要调整规则ID的ACL名称，范围：1–31个字符
＜base-rule-id＞|rule-id的基值，重新编号成功后第一个规则的编号,默认为10，取值范围：1–$#33685536#$
＜increment＞|rule-id的步进，重新编号成功后每个规则rule-id之间的差值，默认为10，取值范围：1–$#33685536#$
缺省 : 
<base-rule-id>默认为10。<increment>默认为10。
使用说明 : 
该命令是对已经存在的ACL列表中的所有规则的ID进行重新编号，规则原来的顺序保持不变，不影响规则生效。命令最后两个参数都是可选的，不设置的话默认值都是10。
范例 : 
ZXROSNG(config)#ipv4-access-list myaclZXROSNG(config-ipv4-acl)#rule 1 deny tcp 192.168.0.10 0.0.0.0 any ZXROSNG(config-ipv4-acl)#rule 2 deny tcp 192.168.0.100 0.0.0.0 any ZXROSNG(config-ipv4-acl)#rule 3 permit tcp 192.168.0.10 0.0.0.0 anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)# resequence-access-list ipv4 myacl 10 10查看结果配置信息：ZXROSNG(config)#show ipv4-access-lists name  myaclipv4-access-list myacl3/3 (showed/total)  10 deny tcp 192.168.0.10 0.0.0.0 any  20 deny tcp 192.168.0.100 0.0.0.0 any  30 permit tcp 192.168.0.10 0.0.0.0 any 
相关命令 : 
show ipv4–access-lists 
## rule 

rule 
命令功能 : 
配置IPv4 ACL的规则。 
命令模式 : 
 IPv4-ACL模式  
命令默认权限级别 : 
15 
命令格式 : 
rule 
  [＜rule-id 
＞] {permit 
|deny 
} {{url 
 ＜source-url 
＞|＜source-ipv4-address 
＞ [＜source-ipv4-address-mask 
＞]|any 
}|{sctp 
 {url 
 ＜source-url 
＞|＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜sctpporttype 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {url 
 ＜destination-url 
＞|＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜sctpporttype 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}]|udp 
 {url 
 ＜source-url 
＞|＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜udpporttype 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {url 
 ＜destination-url 
＞|＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜udpporttype 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}]|icmp 
 {url 
 ＜source-url 
＞|＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} {url 
 ＜destination-url 
＞|＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{＜icmptype 
＞|＜icmp-type 
＞} [＜icmp-code 
＞]]|{＜port-type 
＞|＜ip-protocol-number 
＞} {url 
 ＜source-url 
＞|＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} {url 
 ＜destination-url 
＞|＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
}|tcp 
 {url 
 ＜source-url 
＞|＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜tcpporttype 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {url 
 ＜destination-url 
＞|＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜tcpporttype 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}] [{[established 
],[syn 
 {-  
|+  
}]}]} [{precedence 
 ＜precedence-level 
＞|tos 
 ＜type-of-service 
＞|dscp 
 ＜dscp-value 
＞}] [fragments 
] [ttl 
 {{eq 
|ge 
|le 
|neq 
} ＜TTL_value 
＞|range 
 ＜TTL_ValueRange 
＞}]} [time-range 
 ＜time-range-name 
＞] [log 
]
no rule 
  {＜rule-id 
＞|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜rule-id＞|规则ID，范围：1–$#33685536#$
permit|关键字，指明是permit规则
deny|关键字，指明是deny规则
＜source-url＞|源URL地址
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
sctp|IPv4协议类型，SCTP（流控制传输协议）
＜source-url＞|源URL地址
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜sctpporttype＞|SCTP知名端口类型，可以是关键字discard、ftp-data、ftp、ssh、http、bgp、https中的一个
＜source-port-number＞|TCP协议源端口
range|针对生存周期的操作类型，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是<0-65535>-<0-65535>
＜destination-url＞|目的URL地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜sctpporttype＞|SCTP知名端口类型，可以是关键字discard、ftp-data、ftp、ssh、http、bgp、https中的一个
＜destination-port-number＞|TCP目的端口
range|针对生存周期的操作类型，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是<0-65535>-<0-65535>
udp|IPv4协议类型，UDP
＜source-url＞|源URL地址
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜udpporttype＞|udp端口类型，可以是关键字domain、bootps、bootpc、tftp、ntp、snmp、snmptrap、pim-auto-rp、rip中的一个
＜source-port-number＞|TCP协议源端口
range|针对生存周期的操作类型，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是<0-65535>-<0-65535>
＜destination-url＞|目的URL地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜udpporttype＞|udp端口类型，可以是关键字domain、bootps、bootpc、tftp、ntp、snmp、snmptrap、pim-auto-rp、rip中的一个
＜destination-port-number＞|TCP目的端口
range|针对生存周期的操作类型，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是<0-65535>-<0-65535>
icmp|IPv4协议类型，ICMP
＜source-url＞|源URL地址
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
＜destination-url＞|目的URL地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
＜icmptype＞|ICMP报文类型名称，如echo-reply、unreachable、source-quench、redirect、alternate-address、echo、router-advertisement、router-solicitation、time-exceeded、parameter-problem、timestamp-request、timestamp-reply、information-request、information-reply、mask-request、mask-reply、traceroute等
＜icmp-type＞|ICMP报文类型值
＜icmp-code＞|ICMP报文编码
＜port-type＞|IPv4协议号名称
＜ip-protocol-number＞|IPv4协议号值
＜source-url＞|源URL地址
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
＜destination-url＞|目的URL地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
tcp|IPv4协议类型，TCP
＜source-url＞|源URL地址
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜tcpporttype＞|TCP协议端口名称
＜source-port-number＞|TCP协议源端口
range|针对生存周期的操作类型，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是<0-65535>-<0-65535>
＜destination-url＞|目的URL地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜tcpporttype＞|TCP协议端口名称
＜destination-port-number＞|TCP目的端口
range|针对生存周期的操作类型，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是<0-65535>-<0-65535>
established|TCP建链标记
-|TCP flag没有置位
+|TCP flag置位
＜precedence-level＞|优先级字段
＜type-of-service＞|TOS
＜dscp-value＞|DSCP
fragments|分片标记，匹配分片报文。
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
neq|针对生存周期的操作类型，不等于
＜TTL_value＞|生存周期
range|针对生存周期的操作类型，范围
＜TTL_ValueRange＞|生存周期范围
＜time-range-name＞|时间范围，关联已经配置的time-range名称
log|统计标记，配置该标记后会统计命中该条目的次数。
No参数|描述
---|---
all|删除指定ACL下的所有规则
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置一条TCP规则,当源地址在192.168.0.0 255.255.255.0子网范围内，源端口在1000–2000范围内，优先级为6的IPv4建链TCP报文匹配，动作为permit：ZXROSNG(config-ipv4-acl)#rule permit tcp 192.168.0.0 0.0.0.255 range 1000-2000 any established precedence 6
相关命令 : 
show ipv4–access-lists 
## rule 

rule 
命令功能 : 
配置IPv4 ACL的规则。 
命令模式 : 
 IPv4-ACL模式  
命令默认权限级别 : 
15 
命令格式 : 
rule 
  [＜rule-id 
＞] {permit 
|deny 
} {{＜source-ipv4-address 
＞ [＜source-ipv4-address-mask 
＞]|any 
}|{sctp 
 {＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜sctpporttype 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜sctpporttype 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}]|udp 
 {＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜udpporttype 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜udpporttype 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}]|icmp 
 {＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} {＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{＜icmptype 
＞|＜icmp-type 
＞} [＜icmp-code 
＞]]|{＜port-type 
＞|＜ip-protocol-number 
＞} {＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} {＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
}|tcp 
 {＜source-ipv4-address 
＞ ＜source-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜tcpporttype 
＞|＜source-port-number 
＞}|range 
 ＜range 
＞}] {＜destination-ipv4-address 
＞ ＜destination-ipv4-address-mask 
＞|any 
} [{{eq 
|ge 
|le 
} {＜tcpporttype 
＞|＜destination-port-number 
＞}|range 
 ＜range 
＞}] [{[established 
],[rst 
 {-  
|+  
}],[ack 
 {-  
|+  
}],[fin 
 {-  
|+  
}],[syn 
 {-  
|+  
}],[psh 
 {-  
|+  
}],[urg 
 {-  
|+  
}]}]} [{precedence 
 ＜precedence-level 
＞|tos 
 ＜type-of-service 
＞|dscp 
 ＜dscp-value 
＞}] [fragments 
] [ttl 
 {{eq 
|ge 
|le 
|neq 
} ＜TTL_value 
＞|range 
 ＜TTL_ValueRange 
＞}]} [time-range 
 ＜time-range-name 
＞] [log 
]
no rule 
  {＜rule-id 
＞|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜rule-id＞|规则ID，范围：1–$#33685536#$
permit|关键字，指明是permit规则
deny|关键字，指明是deny规则
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
sctp|IPv4协议类型，SCTP（流控制传输协议）
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜sctpporttype＞|SCTP知名端口类型，可以是关键字discard、ftp-data、ftp、ssh、http、bgp、https中的一个
＜source-port-number＞|SCTP协议源端口号，范围0-65535
range|端口操作符，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜sctpporttype＞|SCTP知名端口类型，可以是关键字discard、ftp-data、ftp、ssh、http、bgp、https中的一个
＜destination-port-number＞|SCTP协议目的端口号，范围0-65535
range|端口操作符，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
udp|IPv4协议类型，UDP
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜udpporttype＞|UDP端口类型，可以是关键字domain、bootps、bootpc、tftp、ntp、snmp、snmptrap、pim-auto-rp、rip中的一个
＜source-port-number＞|UDP协议源端口
range|端口操作符，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜udpporttype＞|UDP端口类型，可以是关键字domain、bootps、bootpc、tftp、ntp、snmp、snmptrap、pim-auto-rp、rip中的一个
＜destination-port-number＞|UDP协议目的端口
range|端口操作符，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
icmp|IPv4协议类型，ICMP
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
＜icmptype＞|ICMP报文类型名称
＜icmp-type＞|ICMP报文类型值
＜icmp-code＞|ICMP报文编码
＜port-type＞|IPv4协议号名称
＜ip-protocol-number＞|IPv4协议号值
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
tcp|IPv4协议类型，TCP
＜source-ipv4-address＞|源Ipv4地址，十进制点分形式
＜source-ipv4-address-mask＞|源Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜tcpporttype＞|TCP协议端口名称
＜source-port-number＞|TCP协议源端口
range|端口操作符，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
＜destination-ipv4-address＞|目的Ipv4地址，十进制点分形式
＜destination-ipv4-address-mask＞|目的Ipv4地址的反掩码，十进制点分形式
any|表示任意源或目的IP地址
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
＜tcpporttype＞|TCP协议端口名称
＜destination-port-number＞|TCP目的端口
range|端口操作符，范围
＜range＞|针对端口的操作类型，需要指定2个port操作数，范围是0-65535
established|TCP建链标记
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
-|TCP flag没有置位
+|TCP flag置位
＜precedence-level＞|优先级字段
＜type-of-service＞|TOS
＜dscp-value＞|DSCP
fragments|分片标记，匹配分片报文。
eq|针对生存周期的操作类型，等于
ge|针对生存周期的操作类型，大于等于
le|针对生存周期的操作类型，小于等于
neq|针对生存周期的操作类型，不等于
＜TTL_value＞|生存周期
range|针对生存周期的操作类型，范围
＜TTL_ValueRange＞|生存周期范围
＜time-range-name＞|时间范围，关联已经配置的time-range名称
log|统计标记，配置该标记后会统计命中该条目的次数。
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置一条TCP规则,当源地址在192.168.0.0 255.255.255.0子网范围内，源端口在1000–2000范围内，优先级为6的IPv4建链TCP报文匹配，动作为permit：ZXROSNG(config-ipv4-acl)#rule permit tcp 192.168.0.0 0.0.0.255 range 1000-2000 any established precedence 6
相关命令 : 
show ipv4–access-lists 
## show ipv4-access-groups 

show ipv4-access-groups 
命令功能 : 
显示配置IPv4 port-ACL绑定信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ipv4-access-groups 
  [{[by-interface 
 ＜interface-name 
＞],[by-access-list 
 ＜acl-name 
＞],[by-direction 
 {ingress 
|egress 
}]}] 
命令参数解释 : 
参数|描述
---|---
by-interface|根据绑定的接口名称过滤显示
＜interface-name＞|绑定的接口名称
by-access-list|根据绑定的acl列表名字过滤显示
＜acl-name＞|ACL名称，长度1–31个字符
by-direction|根据绑定接口的方向过滤显示
ingress|根据绑定接口的方向过滤显示：入向
egress|根据绑定接口的方向过滤显示：出向
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置IPv4 port-ACL:ZXROSNG(config)#ipv4-access-group interface gei-0/1/0/1 egress MyACLZXROSNG(config)#ipv4-access-group interface gei-0/1/0/1 ingress MyACL2ZXROSNG(config)#ipv4-access-group vlan 1 egress MyACL显示所有：ZXROSNG(config)#show ipv4-access-group===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       MyACL2Egress        MyACL===============================================================================VLAN ID:1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress      MyACL根据VLAN ID过滤显示：ZXROSNG(config)#show ipv4-access-group by-vlan 1===============================================================================VLAN ID:1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       MyACL根据接口名字过滤显示：ZXROSNG(config)#show ipv4-access-groups by-interface gei-0/1/0/1===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress      MyACL2Egress       MyACL根据接口方向过滤显示：ZXROSNG(config)#show ipv4-access-groups by-direction egress ===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       MyACL===============================================================================VLAN ID:1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Egress       MyACLZXROSNG(config)#根据ACL名称过滤显示：ZXROSNG(config)#show ipv4-access-groups by-access-list MyACL2===============================================================================Interface name:gei-0/1/0/1-------------------------------------------------------------------------------Direction    ACL name                        Sequence-num    Default action-------------------------------------------------------------------------------Ingress       MyACL2ZXROSNG(config)#
相关命令 : 
ipv4-access-group 
## show ipv4-access-lists 

show ipv4-access-lists 
命令功能 : 
显示配置的IPv4 ACL规则信息。如果规则配置了LOG选项，显示规则命中统计计数。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ipv4-access-lists 
  [{[config 
]|[name 
 ＜acl-name 
＞ [from 
 ＜begin-rule-id 
＞ to 
 ＜end-rule-id 
＞]] [usage 
 ＜interface-name 
＞ {egress 
|ingress 
} port-acl 
]|[brief 
 [name 
 ＜acl-name 
＞]]}] 
命令参数解释 : 
参数|描述
---|---
config|显示ACL的配置系统信息，如已配置多少条目，最大可配置多少条目等。
＜acl-name＞|ACL名称,如不指定该参数，则显示所有IPv4 ACL。取值：1–31个字符
＜begin-rule-id＞|如果不需要显示ACL下的所有规则，可以指定需要显示的规则范围。此字段用于指定需要显示的规则范围起始位置。
＜end-rule-id＞|如果不需要显示ACL下的所有规则，可以指定需要显示的规则范围。此字段用于指定需要显示的规则范围结束位置。
usage|统计信息，统计的是ACL规则被命中的次数（仅适用于配置了log的规则）
＜interface-name＞|用于指定需要统计的ACL所在的接口名称。
egress|用于指定需要统计的ACL所在的接口出方向。与ingress两者二选一。
ingress|用于指定需要统计的ACL所在的接口入方向。与egress两者二选一。
port-acl|用于指定接口上使用ACL的业务类型。(目前只支持port-acl业务。)
brief|用于指定只显示ACL的简要信息，不列出ACL的详细规则条目。
＜acl-name＞|ACL名称,如不指定该参数，则显示所有IPv4 ACL。取值：1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示IPv4 ACL目前的系统信息：ZXROSNG(config)#show ipv4-access-lists config Current config total access-lists :1Current config total access-list rules :4System total access-lists upper limit :4000System total access-list rules upper limit :32000ZXROSNG(config)#显示所有IPv4 ACL列表：ZXROSNG(config-ipv4-acl)#show ipv4-access-listsipv4-access-list myacl4/4 (showed/total)10 deny tcp 192.168.0.10 0.0.0.0 any 11 permit tcp 192.168.1.14 0.0.0.0 range 1000-2000 any precedence 615 permit tcp 168.192.0.10 0.0.0.0 any20 deny tcp 192.168.0.100 0.0.0.0 any显示IPv4 ACL的简要信息：ZXROSNG(config)#show ipv4-access-lists brief No. ACL RuleSum -------------------------------------------------------1 sss 4 2 xxx 3 ZXROSNG(config)#显示IPv4 ACL sss在接口gei-0/1/0/1出方向上的统计信息：ZXROSNG(config-if-smartgroup1)#show ipv4-access-lists usage smartgroup1 egress port-acl ipv4-access-list sss4/4 (showed/total)1 deny 1.1.1.1 0.0.0.0 log(101 matches)2 deny 2.2.2.2 0.0.0.0 log(10 matches)3 deny 3.3.3.3 0.0.0.0 log(90 matches)4 deny 4.4.4.4 0.0.0.0 log(102 matches)
相关命令 : 
ipv4-access-list 
## show ipv6-access-groups 

show ipv6-access-groups 
命令功能 : 
显示配置IPv6 port-ACL绑定信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ipv6-access-groups 
  [{[by-interface 
 ＜interface-name 
＞],[by-access-list 
 ＜acl-name 
＞],[by-direction 
 {ingress 
|egress 
}]}] 
命令参数解释 : 
参数|描述
---|---
by-interface|根据绑定的接口名称过滤显示
＜interface-name＞|绑定的接口名称
by-access-list|根据绑定的acl列表名字过滤显示
＜acl-name＞|ACL名称，长度1–31个字符
by-direction|根据绑定接口的方向过滤显示
ingress|根据绑定接口的方向过滤显示：入向
egress|根据绑定接口的方向过滤显示：出向
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置IPv6 port-ACL:ZXROSNG(config)#ipv6-access-group interface gei-0/1/0/1 egress MyACLZXROSNG(config)#ipv6-access-group interface gei-0/1/0/1 ingress MyACL2ZXROSNG(config)#ipv6-access-group vlan 1 egress MyACL显示所有：ZXROSNG(config)#show ipv6-access-groupInterface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress MyACL2            Egress  MyACLvlan 1      Egress  MyACL根据VLAN ID过滤显示：ZXROSNG(config)#show ipv6-access-group by-vlan 1Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------vlan 1 Egress MyACL根据接口名字过滤显示：ZXROSNG(config)#show ipv6-access-groups by-interface gei-0/1/0/1Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress MyACL2            Egress  MyACL根据接口方向过滤显示：ZXROSNG(config)#show ipv6-access-groups by-direction egress Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Egress MyACLvlan 1      Egress MyACLZXROSNG(config)#根据ACL名称过滤显示：ZXROSNG(config)#show ipv6-access-groups by-access-list MyACL2Interface name|vlan   Direction ACL name                        Default action-------------------------------------------------------------------------------gei-0/1/0/1 Ingress MyACL2ZXROSNG(config)#
相关命令 : 
ipv6-access-group 
## show user-defined-access-groups 

show user-defined-access-groups 
命令功能 : 
显示配置port-ACL绑定信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show user-defined-access-groups 
  [{[by-interface 
 ＜interface-name 
＞],[by-access-list 
 ＜acl-name 
＞],[by-direction 
 {ingress 
|egress 
}]}] 
命令参数解释 : 
参数|描述
---|---
by-interface|根据绑定的接口名称过滤显示
＜interface-name＞|绑定的接口名称
by-access-list|根据绑定的acl列表名字过滤显示
＜acl-name＞|ACL名称，长度1–31个字符
by-direction|根据绑定接口的方向过滤显示
ingress|根据绑定接口的方向过滤显示：入向
egress|根据绑定接口的方向过滤显示：出向
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置user-defined port-ACL:ZXROSNG(config)#user-defined-access-group interface gei-0/1/0/1 egress MyACLZXROSNG(config)#user-defined-access-group interface gei-0/1/0/1 ingress MyACLZXROSNG(config)#user-defined-access-group vlan 1 egress MyACL显示所有：ZXROSNG(config)#show user-defined-access-groupInterface name|vlan               Direction  ACL name-----------------------------------------------------------------gei-0/1/0/1                       Ingress    MyACL2Egress     MyACLvlan 1                            Egress     MyACL根据VLAN ID过滤显示：ZXROSNG(config)#show user-defined-access-group by-vlan 1Interface name|vlan               Direction  ACL name-----------------------------------------------------------------vlan 1                            Egress     MyACL根据接口名字过滤显示：ZXROSNG(config)#show user-defined-access-groups by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name-----------------------------------------------------------------gei-0/1/0/1                       Ingress    MyACL2Egress     MyACL根据接口方向过滤显示：ZXROSNG(config)#show user-defined-access-groups by-direction egressInterface name|vlan               Direction  ACL name-----------------------------------------------------------------gei-0/1/0/1                       Egress     MyACLvlan 1                            Egress     MyACLZXROSNG(config)#
根据ACL名称过滤显示：ZXROSNG(config)#show user-defined-access-groups by-access-list MyACL2Interface name|vlan               Direction  ACL name-----------------------------------------------------------------gei-0/1/0/1                       Ingress    MyACL2ZXROSNG(config)#
相关命令 : 
user-defined-access-group  
## user-defined-access-group egress 

user-defined-access-group egress 
命令功能 : 
绑定ACL列表到接口出方向。 
命令模式 : 
 10G以太接口模式,pos子接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
10G以太接口模式:15,smartgroup接口模式:15,pos子接口模式:15,以太接口模式:15,千兆以太接口模式:15,smartgroup子接口模式:15,pos接口模式:15 
命令格式 : 
user-defined-access-group egress 
  ＜acl-name 
＞
no user-defined-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1出方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group egress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Egress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group egress 

user-defined-access-group egress 
命令功能 : 
绑定ACL列表到接口出方向。 
命令模式 : 
 dsl接口模式,multilink接口模式,posgroup接口模式,serial接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
dsl接口模式:15,serial接口模式:15,通道化cpos_e1接口模式:15,ulei子接口模式:15,posgroup接口模式:15,ulei接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,supervlan接口模式:15 
命令格式 : 
user-defined-access-group egress 
  ＜acl-name 
＞
no user-defined-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1出方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group egress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Egress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group egress 

user-defined-access-group egress 
命令功能 : 
绑定ACL列表到接口出方向。 
命令模式 : 
 qx子接口模式,qx接口模式  
命令默认权限级别 : 
qx子接口模式:15,qx接口模式:15 
命令格式 : 
user-defined-access-group egress 
  ＜acl-name 
＞
no user-defined-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1出方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group egress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Egress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group egress 

user-defined-access-group egress 
命令功能 : 
绑定ACL列表到接口出方向。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
user-defined-access-group egress 
  ＜acl-name 
＞
no user-defined-access-group egress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1出方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group egress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Egress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group ingress 

user-defined-access-group ingress 
命令功能 : 
绑定ACL列表到接口入方向上。 
命令模式 : 
 10G以太接口模式,pos子接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
千兆以太接口模式:15,以太接口模式:15,smartgroup子接口模式:15,pos接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,pos子接口模式:15 
命令格式 : 
user-defined-access-group ingress 
  ＜acl-name 
＞
no user-defined-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1入方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group ingress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Ingress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group ingress 

user-defined-access-group ingress 
命令功能 : 
绑定ACL列表到接口入方向上。 
命令模式 : 
 dsl接口模式,multilink接口模式,posgroup接口模式,serial接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
通道化ce1接口模式:15,multilink接口模式:15,supervlan接口模式:15,posgroup接口模式:15,ulei接口模式:15,通道化cpos_e1接口模式:15,ulei子接口模式:15,dsl接口模式:15,serial接口模式:15 
命令格式 : 
user-defined-access-group ingress 
  ＜acl-name 
＞
no user-defined-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1入方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group ingress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Ingress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group ingress 

user-defined-access-group ingress 
命令功能 : 
绑定ACL列表到接口入方向上。 
命令模式 : 
 qx子接口模式,qx接口模式  
命令默认权限级别 : 
qx接口模式:15,qx子接口模式:15 
命令格式 : 
user-defined-access-group ingress 
  ＜acl-name 
＞
no user-defined-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1入方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group ingress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Ingress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group ingress 

user-defined-access-group ingress 
命令功能 : 
绑定ACL列表到接口入方向上。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
user-defined-access-group ingress 
  ＜acl-name 
＞
no user-defined-access-group ingress 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1入方向上：ZXROSNG(config-if-gei-0/1/0/1)#user-defined-access-group ingress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Ingress        myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group interface &amp;lt;mid&amp;gt; egress 

user-defined-access-group interface <mid> egress 
命令功能 : 
绑定ACL列表到接口出方向上。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
user-defined-access-group interface  
 ＜interface-list 
＞ egress 
  ＜acl-name 
＞
no user-defined-access-group interface  
 ＜interface-list 
＞ egress 
命令参数解释 : 
参数|描述
---|---
＜interface-list＞|接口名称
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1出方向上：ZXROSNG(config)#user-defined-access-group interface gei-0/1/0/1 egress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface gei-0/1/0/1Interface name|vlan               Direction  ACL name---------------------------------------------------------------gei-0/1/0/1                              Egress         myacl
相关命令 : 
show user-defined-access-groups 
## user-defined-access-group interface &amp;lt;mid&amp;gt; ingress 

user-defined-access-group interface <mid> ingress 
命令功能 : 
绑定ACL列表到接口入方向上。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
user-defined-access-group interface  
 ＜interface-list 
＞ ingress 
  ＜acl-name 
＞
no user-defined-access-group interface  
 ＜interface-list 
＞ ingress 
命令参数解释 : 
参数|描述
---|---
＜interface-list＞|接口名称
＜acl-name＞|ACL名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
绑定ACL列表myacl到接口gei-0/1/0/1入方向上：ZXROSNG(config)#user-defined-access-group interface gei-0/1/0/1 ingress myacl查看配置结果信息：ZXROSNG(config)#show user-defined-access-groups by-interface-or-vlan by-interface-or-vlan by-interface gei-0/1/0/1Interface name|vlan               Direction   ACL name----------------------------------------------------------------gei-0/1/0/1                               Ingress      myacl
相关命令 : 
show user-defined-access-groups 
# Route-map配置命令 
## blackhole-route 

blackhole-route 
命令功能 : 
此命令用于使能或去使能黑洞路由。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
blackhole-route 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能黑洞路由
disable|去使能黑洞路由
缺省 : 
PBR路由类型为黑洞路由则不下发。 
使用说明 : 
当配置blackhole-route enable时，PBR路由类型为黑洞路由则下发。当配置blackhole-route disable时，PBR路由类型为黑洞路由则不下发。blackhole-route disable是默认配置。 
范例 : 
1、设置黑洞路由生效：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#blackhole-route enable2、采用show running-config配置示意如下：ZXROSNG(config-route-map)#show running-config route-map !<route-map>route-map zte permit 1  blackhole-route enable $
相关命令 : 
show route-map 
## continue 

continue 
命令功能 : 
在当前策略路由序列号匹配成功时，使用本命令在该route-map实例的下一个序列号中继续匹配操作。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
continue 
  {next 
|sequence 
 ＜sequence-number 
＞}
no continue 
命令参数解释 : 
参数|描述
---|---
next|策略路由跳转到下一序列号。
＜sequence-number＞|策略路由跳转到指定序列号，配置范围0-65535。
缺省 : 
无 
使用说明 : 
仅限于同route-map实例下跳转。配置continue next时，策略路由跳转到下一个序列号执行匹配操作。配置continue sequence时，策略路由跳转到指定序列号执行匹配操作。配置的指定序列号要大于当前序列号。
范例 : 
1、策略路由跳转到下一个序列号执行匹配操作：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#continue next2、采用show running-config配置示意如下：ZXROSNG(config-route-map)#show running-config route-map !<route-map>route-map zte permit 1  continue next  ——》表示：跳转到 route-map zte permit 10规则$route-map zte permit 10  match interface gei-0/1/0/1  continue sequence 100 ——》表示：跳转到 route-map zte permit 100规则$route-map zte permit 20  match interface gei-0/1/0/2$route-map zte permit 100  match interface gei-0/1/0/2$
相关命令 : 
show route-map 
## default-route 

default-route 
命令功能 : 
此命令用于使能或去使能默认路由。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
default-route 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能默认路由
disable|去使能默认路由
缺省 : 
PBR路由类型为默认路由则不下发。 
使用说明 : 
当配置default-route enable时，PBR路由类型为默认路由则下发。当配置default-route disable时，PBR路由类型为默认路由则不下发。default-route disable是默认配置。 
范例 : 
1、设置默认路由生效：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#default-route enable2、采用show running-config配置示意如下：ZXROSNG(config-route-map)#show running-config route-map !<route-map>route-map zte permit 1  default-route enable $
相关命令 : 
show route-map 
description : 

description 
命令功能 : 
使用本命令在route-map的序列中配置文本描述。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
description 
  ＜description 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜description＞|文本描述，长度1-199字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
在route-map中配置文本描述：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#description abc
相关命令 : 
show route-map 
## ip as-path access-list standard 

ip as-path access-list standard 
命令功能 : 
定义与BGP相关的标准自治系统路径访问表。使用no命令使访问表无效。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip as-path access-list standard 
  ＜aspath-list-name 
＞ ＜aspath-list-sequence 
＞ <1-65535>/<1-65535>.<0-65535> 
 count 
 ＜aspath-list-count 
＞
no ip as-path access-list standard 
  ＜aspath-list-name 
＞ [＜aspath-list-sequence 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜aspath-list-name＞|指定访问表名称，字符串长度范围：1-31
＜aspath-list-sequence＞|指定访问表序列号，取值范围是0-65535
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。
＜aspath-list-count＞|指定访问表重复计数，取值范围是1-255
缺省 : 
无 
使用说明 : 
标准AS路径列表名下最多可配255个系列号。 
范例 : 
配置标准AS路径列表a， 并指定AS为5个1.1ZXROSNG(config)#ip as-path access-list standard a 1 1.1 count 5
相关命令 : 
show ip as-path-access-list standard 
## ip as-path access-list trigger-delay 

ip as-path access-list trigger-delay 
命令功能 : 
设置自治系统路径访问表同步到应用的延迟时间。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip as-path access-list trigger-delay 
  ＜delay-time 
＞
no ip as-path access-list trigger-delay 
命令参数解释 : 
参数|描述
---|---
＜delay-time＞|延迟时间，范围0-30(单位：秒)
缺省 : 
默认10秒。 
使用说明 : 
1、应用协议（如BGP等）引用自治系统路径访问表后，当自治系统路径访问表创建、更新，会同步到对应的应用协议。同步会有一定延时，可以通过本命令调整延时时间。2、本配置针对所有自治系统路径访问表实例生效。
范例 : 
设置自治系统路径访问表同步延迟时间为20秒：ZXROSNG(config)#ip as-path access-list trigger-delay 20
相关命令 : 
show ip as-path-access-list 
## ip as-path access-list 

ip as-path access-list 
命令功能 : 
定义与BGP相关的自治系统路径访问表。使用no命令使访问表无效。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip as-path access-list 
  {＜aspath-list-number 
＞|name 
 ＜aspath-list-name 
＞} {deny 
|permit 
} ＜regular-expression 
＞
no ip as-path access-list 
  {＜aspath-list-number 
＞|name 
 ＜aspath-list-name 
＞} [{deny 
|permit 
} ＜regular-expression 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜aspath-list-number＞|指定访问表，范围：1–199
＜aspath-list-name＞|指定访问表名称，字符串长度范围：1-31
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜regular-expression＞|在访问表中使用正则表达式的自治系统
缺省 : 
未定义访问表。 
使用说明 : 
可以在入端或出端BGP路由上规定访问表过滤器。此外，还可以在一组过滤器基础上分配权重。每个过滤器就是一个基于正则表达式的访问表。如果正则表达式匹配于路由自治系统路径的描述，该路由以ASCII字符串形式表现，那就用permit或deny条件。自治系统路径不包括本地自治系统号。用ip as-path access-list全局配置命令来定义BGP访问表，用neighbor路由配置命令来申请特殊的访问表。配置的自治系统路径访问表名称不能为纯数字。
范例 : 
指定带IP地址128.125.1.1的BGP邻居不发送来自邻近自治系统123的任何路径的通告：ZXROSNG(config)#ip as-path access-list 1 permit 123ZXROSNG(config)#route-map test deny 10ZXROSNG(config-route-map)#match as-path 1ZXROSNG(config-route-map)#exitZXROSNG(config-bgp)#network 131.108.0.0 255.255.0.0 ZXROSNG(config-bgp)#neighbor 128.140.6.6 remote-as 123ZXROSNG(config-bgp)#neighbor 128.125.1.1 remote-as 47ZXROSNG(config-bgp)#neighbor 128.125.1.1 route-map test out
相关命令 : 
show ip as-path-access-list 
## ip color-list 

ip color-list 
命令功能 : 
定义与BGP相关的color访问表。使用no命令使访问表无效。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip color-list 
 name 
 ＜color-list-name 
＞ ＜color-value 
＞
no ip color-list 
 name 
 ＜color-list-name 
＞ [＜color-value 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜color-list-name＞|color列表名称,范围：1–31字符
＜color-value＞|color值，范围1-4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置color列表：ZXROSNG(config)#ip color-list name zte 22233
相关命令 : 
show ip color-list 
## ip community-list trigger-delay 

ip community-list trigger-delay 
命令功能 : 
设置团体表同步到应用的延迟时间。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip community-list trigger-delay 
  ＜delay-time 
＞
no ip community-list trigger-delay 
命令参数解释 : 
参数|描述
---|---
＜delay-time＞|延迟时间，范围0-30(单位：秒)
缺省 : 
默认10秒。 
使用说明 : 
1、应用协议（如BGP等）引用团体表后，当团体表创建、更新，会同步到对应的应用协议。同步会有一定延时，可以通过本命令调整延时时间。2、本配置针对所有团体表实例生效。
范例 : 
设置团体表同步延迟时间为20秒：ZXROSNG(config)#ip community-list trigger-delay 20
相关命令 : 
show ip community-list  
## ip community-list 

ip community-list 
命令功能 : 
给BGP创建一个团体表且控制对它的访问。使用no命令删除团体表。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip community-list 
  {＜community-list-number 
＞ {deny 
|permit 
} {any 
|*({＜community-number 
＞|internet 
|no-export 
|no-advertise 
|no-export-subconfed 
|<0-65535>:<0-65535> 
})}|＜ex-community-list-number 
＞ {deny 
|permit 
} ＜regular-expression 
＞|basic 
 ＜community-list-name 
＞ {deny 
|permit 
} {any 
|*({＜community-number 
＞|internet 
|no-export 
|no-advertise 
|no-export-subconfed 
|<0-65535>:<0-65535> 
})}|advanced 
 ＜community-list-name 
＞ {deny 
|permit 
} ＜regular-expression 
＞}
no ip community-list 
  {＜community-list-number 
＞|＜ex-community-list-number 
＞|name 
 ＜community-list-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜community-list-number＞|标识一个或多个允许或拒绝的团体组，标准团体组范围：1–99
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
any|所有的团体号
＜community-number＞|由set community命令配置的团体号，从1到4294967295的一个号，可以规定一个单个号或者有一定间隔的多个号，最多配置10个团体号
internet|互联网标志
no-export|不向下一个自治系统通告该路由
no-advertise|不向任何对等点（内部的或外部的）通告该路由
no-export-subconfed|不向任何外部的对等点通告该路由
<0-65535>:<0-65535>|aa:nn格式的团体号，aa的范围0-65535，nn的范围0-65535 最多配置10个团体号
＜ex-community-list-number＞|标志一个或多个允许或拒绝的团体组，扩展团体组范围：100-499
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜regular-expression＞|团队属性列表的正则表达式，最多63个字符
basic|标准团体名字
＜community-list-name＞|用英文标识一个或多个允许或拒绝的团体组，长度范围：1–31
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
any|所有的团体号
＜community-number＞|由set community命令配置的团体号，从1到4294967295的一个号，可以规定一个单个号或者有一定间隔的多个号，最多配置10个团体号
internet|互联网标志
no-export|不向下一个自治系统通告该路由
no-advertise|不向任何对等点（内部的或外部的）通告该路由
no-export-subconfed|不向任何外部的对等点通告该路由
<0-65535>:<0-65535>|aa:nn格式的团体号，aa的范围0-65535，nn的范围0-65535 最多配置10个团体号
advanced|扩展团体名字
＜community-list-name＞|用英文标识一个或多个允许或拒绝的团体组，长度范围：1–31
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜regular-expression＞|团队属性列表的正则表达式，最多63个字符
缺省 : 
缺省不配置团体表。 
使用说明 : 
1.配置重复值会过滤重复。2.一旦允许一个团体号值，那么该团体表就拒绝其他团体号。3.团体列表的名字不能为纯数字。4.基础团体列表名字和扩展团体列表名字不能相同。
范例 : 
除了团体5和10或团体10和15的路由之外，允许其它所有路由：ZXROSNG(config)#ip community-list 1 deny 5 10 ZXROSNG(config)#ip community-list 1 deny 10 15ZXROSNG(config)#ip community-list 1 permit any
相关命令 : 
show ip community-list 
## ip extcommunity-list trigger-delay 

ip extcommunity-list trigger-delay 
命令功能 : 
设置扩展团体表同步到应用的延迟时间。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip extcommunity-list trigger-delay 
  ＜delay-time 
＞
no ip extcommunity-list trigger-delay 
命令参数解释 : 
参数|描述
---|---
＜delay-time＞|延迟时间，范围0-30(单位：秒)
缺省 : 
默认10秒。 
使用说明 : 
1、应用协议（如BGP等）引用扩展团体表后，当扩展团体表创建、更新，会同步到对应的应用协议。同步会有一定延时，可以通过本命令调整延时时间。2、本配置针对所有扩展团体表实例生效。
范例 : 
设置扩展团体表同步延迟时间为20秒：ZXROSNG(config)#ip extcommunity-list trigger-delay 20
相关命令 : 
show ip extcommunity-list  
## ip extcommunity-list 

ip extcommunity-list 
命令功能 : 
给BGP创建一个扩展团体表且控制对它的访问。使用no命令删除扩展团体表。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip extcommunity-list 
  {＜community-list-number 
＞ {deny 
|permit 
} {*({rt-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|soo-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|rt-non-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|soo-non-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}})|general-asn 
 *(＜<0-4294967295>:<0-4294967295> 
＞)}|＜ex-community-list-number 
＞ {deny 
|permit 
} ＜regular-expression 
＞|basic 
 ＜extcommunity-list-name 
＞ {deny 
|permit 
} {*({rt-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|soo-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|rt-non-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|soo-non-trans 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}})|general-asn 
 *(＜<0-4294967295>:<0-4294967295> 
＞)}|advanced 
 ＜ex-extcommunity-list-name 
＞ {deny 
|permit 
} ＜regular-expression 
＞}
no ip extcommunity-list 
  {＜community-list-number 
＞|＜ex-community-list-number 
＞|name 
 ＜extcommunity-list-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜community-list-number＞|标准的扩展团体表号，范围：1-99
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
＜<0-4294967295>:<0-4294967295>＞|64位通用asn配置格式
＜ex-community-list-number＞|扩展的扩展团体表号，范围：100-500
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜regular-expression＞|在扩展团体表中使用正则表达式的自治系统
basic|标准的扩展团体名
＜extcommunity-list-name＞|用英文标识一个或多个允许或拒绝的标准的extcommunity-list，长度范围：1-31
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
<0-65535>:<0-4294967295>|扩展团体属性值：<aa>:<nnnn>型<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295
A.B.C.D:<0-65535>|扩展团体属性值:A.B.C.D : <aa>型A.B.C.D为IP地址，十进制点分形式，<aa>的取值范围：0-65535
<1-65535>.<0-65535>:<0-65535>|扩展团体属性值：,<aa>.<nn>:<kk>型<aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535
＜<0-4294967295>:<0-4294967295>＞|64位通用asn配置格式
advanced|扩展的扩展团体名字
＜ex-extcommunity-list-name＞|用英文标识一个或多个允许或拒绝的扩展的extcommunity-list，长度范围：1–31
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜regular-expression＞|在扩展团体表中使用正则表达式的自治系统
缺省 : 
缺省不配置扩展团体表。 
使用说明 : 
1.配置重复值会过滤重复。2.一旦允许一个团体号值，那么该团体表就拒绝其他团体号。3.团体列表的名字不能为纯数字。4.基础团体列表名字和扩展团体列表名字不能相同。
范例 : 
配置扩展团体表：ZXROSNG(config)#ip extcommunity-list 400 deny zte
相关命令 : 
show ip extcommunity-listshow ip extcommunity-list name
## ip large-community-list trigger-delay 

ip large-community-list trigger-delay 
命令功能 : 
设置大团体表同步到应用的延迟时间。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip large-community-list trigger-delay 
  ＜delay-time 
＞
no ip large-community-list trigger-delay 
命令参数解释 : 
参数|描述
---|---
＜delay-time＞|延迟时间，范围0-30(单位：秒)
缺省 : 
默认10秒。 
使用说明 : 
使用场景：设置大团体表同步到应用的延迟时间。注意事项：1、应用协议（如BGP等）引用大团体表后，当大团体表创建、更新，会同步到对应的应用协议。同步会有一定延时，可以通过本命令调整延时时间。2、本配置针对所有大团体表实例生效。
范例 : 
设置大团体表同步延迟时间为20秒：ZXROSNG(config)#ip large-community-list trigger-delay 20
相关命令 : 
show ip large-community-list  
## ip large-community-list 

ip large-community-list 
命令功能 : 
创建一个大团体表且控制对它的访问。使用no命令删除大团体表。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip large-community-list 
 name 
 ＜large-community-list-name 
＞ ＜sequence-number 
＞ {deny 
|permit 
} ＜n:n:n 
＞
no ip large-community-list 
 name 
 ＜large-community-list-name 
＞ [＜sequence-number 
＞ [{deny 
|permit 
} ＜n:n:n 
＞]]
				
命令参数解释 : 
参数|描述
---|---
＜large-community-list-name＞|大团体表的名称，长度范围：1–31
＜sequence-number＞|序列号，1-4294967295
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜n:n:n＞|n:n:n格式的大团体号，n的范围0-4294967295
缺省 : 
缺省不配置大团体表。 
使用说明 : 
使用场景：给BGP创建一个大团体表，BGP用来改变其路由属性。注意事项：1.最多可配置100个大团体名称。2.同名称同系列号下最多配置10个团体号，且必须配置相同的匹配类型。3.团体号格式为<0-4294967295>:<0-4294967295>:<0-4294967295>, 例  0:0:0为有效值，01:02:03为无效值，1:2:3为有效值
范例 : 
创建大团体表a，除了团体1:2:3和2:3:4或团体5:6:7和6:7:8的路由之外，拒绝其它所有路由：ZXROSNG(config)#ip large-community-list name a 1 permit 1:2:3 ZXROSNG(config)#ip large-community-list name a 1 permit 2:3:4ZXROSNG(config)#ip large-community-list name a 2 permit 5:6:7ZXROSNG(config)#ip large-community-list name a 2 permit 6:7:8
相关命令 : 
show ip large-community-list 
## ip policy 

ip policy 
命令功能 : 
在接口上绑定route-map。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip policy 
 interface 
 ＜interface-name 
＞ route-map 
 ＜routemap-name 
＞
no ip policy 
 interface 
 ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，长度：1-31位字符
＜routemap-name＞|Route-map名称，长度：1-31位字符
缺省 : 
无 
使用说明 : 
配置前确认<interface-name>对应的接口是否存在，如果不存在则配置不成功。策略路由支持空绑定route-map，即route-map不存在或内容为空也可以绑定到接口上，但策略路由不会生效，配置前请确认route-map是否有效。策略路由的匹配规则目前支持route-map配置的match ip address、match ip policy-route-id等，动作设置支持set ip next-hop、set interface、set ip tos、set ip precedence、set dscp、set global、set global ip next-hop、set vrf vrfname、set vrf vrfname ip next-hop、set ip path interface等。其余不支持的route-map配置将会被策略路由过滤掉，不会生效。
范例 : 
配置一个名称为acl-name的IPv4 ACL， 将该IPv4 ACL应用到名称为rmp_test的route-map中，然后将rmp_test绑定到接口gei-0/1/0/2上。ZXROSNG(config)#ipv4-access-list acl-nameZXROSNG(config-ipv4-acl)#rule permit 3.3.3.3 0.0.0.255ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ZXROSNG(config)#route-map rmp_testZXROSNG(config-route-map)#match ip address acl-nameZXROSNG(config-route-map)#set ip next-hop 1.1.1.2ZXROSNG(config-route-map)#exitZXROSNG(config)#ip policy interface gei-0/1/0/2 route-map rmp_testZXROSNG(config)#
相关命令 : 
show route-mapshow running-config pbr
## ipv6 policy 

ipv6 policy 
命令功能 : 
在接口上绑定route-map。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 policy 
 interface 
 ＜interface-name 
＞ route-map 
 ＜routemap-name 
＞
no ipv6 policy 
 interface 
 ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，长度：1-32位字符
＜routemap-name＞|Route-map名称，长度：1-32位字符
缺省 : 
无 
使用说明 : 
配置前确认<interface-name>对应的接口是否存在，如果不存在则配置不成功；另外，对于IPv6策略路由来说，在绑定前，还需要先将<interface-name>对应的接口使能，否则不能绑定。IPv6策略路由支持空绑定route-map，即route-map不存在或内容为空也可以绑定到接口上，但策略路由不会生效。因此，配置前请确认route-map是否有效。IPv6 策略路由的匹配规则目前支持route-map配置的match ipv6 address、match ipv6 policy-route-id等，动作配置支持set ipv6 next-hop、set interface、set ipv6 path interface、set ipv6 traffic-class等。其余不支持的route-map配置将会被策略路由过滤掉，不会生效。
范例 : 
配置一个名称为acl-name-v6的IPv6 ACL， 将该IPv6 ACL应用到名称为rmp_test的route-map中，然后将rmp_test绑定到接口gei-0/1/0/1上，其中gei-0/1/0/1需要先使能IPv6。ZXROSNG(config)#ipv6-access-list acl-name-v6ZXROSNG(config-ipv6-acl)#rule permit ip 3:3::3:3/112 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#ZXROSNG(config)#route-map rmp_testv6ZXROSNG(config-route-map)#match ipv6 address acl-name-v6ZXROSNG(config-route-map)#set ipv6 next-hop 3:3::3:3ZXROSNG(config-route-map)#exitZXROSNG(config)#ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enableZXROSNG(config-if-gei-0/1/0/1)#exitZXROSNG(config)#ZXROSNG(config)#ipv6 policy interface gei-0/1/0/1 route-map rmp_testv6ZXROSNG(config)#
相关命令 : 
show route-mapshow running-config pbr
## load-share 

load-share 
命令功能 : 
使用本命令在route-map的序列中配置使能路由负荷分担功能。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
load-share 
 
no load-share 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
Route-map中配置load-share后，该route-map中配置的有效路由会形成负荷分担，流量会均匀分担到各条路由。 
范例 : 
在route-map中配置路由时能负荷分担：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#load-share
相关命令 : 
show route-map 
## match as-path 

match as-path 
命令功能 : 
配置匹配BGP自治系统路径访问表。使用no命令删除一条路径表记录。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match as-path 
  {*(＜aspath-list-number 
＞)|name 
 ＜aspath-list-name 
＞}
no match as-path 
  [{*(＜aspath-list-number 
＞)|name 
 ＜aspath-list-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜aspath-list-number＞|把该值附加到与路由映射相匹配的as-path路由中,与＜aspath-list-name＞合计最多匹配10个，范围：1–199
＜aspath-list-name＞|把该名称附加到与路由映射相匹配的as-path路由中,与＜aspath-list-number＞合计最多匹配10个，字符串长度范围：1–31
缺省 : 
无 
使用说明 : 
如果配置的<as-path-number>或＜aspath-list-name＞不存在，默认为permit any。配置重复的<as-path-number>或＜aspath-list-name＞会过滤重复。配置的＜aspath-list-name＞不能为纯数字。 
范例 : 
配置匹配BGP自治系统路径访问表和访问表名称：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match as-path 1ZXROSNG(config-route-map)#match as-path name zte
相关命令 : 
show route-map 
## match as-path-length 

match as-path-length 
命令功能 : 
配置匹配BGP自治系统路径访问表长度。使用no命令删除一条路径表记录。
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match as-path-length 
  {eq 
|ge 
|le 
} ＜as-path-length 
＞
no match as-path-length 
命令参数解释 : 
参数|描述
---|---
eq|运算符等于
ge|运算符大于
le|运算符小于
＜as-path-length＞|BGP自治系统路径访问表长度，范围<0-255>
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match as-path-length eq 1
相关命令 : 
show route-map
## match as-path-unique-length 

match as-path-unique-length 
命令功能 : 
配置匹配BGP自治系统路径访问表长度。使用no命令删除一条路径表记录。
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match as-path-unique-length 
  {eq 
|ge 
|le 
} ＜as-path-unique-length 
＞
no match as-path-unique-length 
命令参数解释 : 
参数|描述
---|---
eq|运算符等于
ge|运算符大于
le|运算符小于
＜as-path-unique-length＞|BGP自治系统路径访问表唯一长度，范围<0-255>
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match as-path-unique-length eq 1
相关命令 : 
show route-map
## match community-list 

match community-list 
命令功能 : 
配置匹配团体表。使用no命令删除团体表记录。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match community-list 
  {*(＜community-list-number 
＞)|name 
 ＜community-list-name 
＞}
no match community-list 
  [{*(＜community-list-number 
＞)|name 
 ＜community-list-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜community-list-number＞|团体号，最多匹配10个团体号，范围：1–499
＜community-list-name＞|名字长度最长为31个字符，不能是全数字的组合
缺省 : 
无 
使用说明 : 
配置重复的<community-list-number>会过滤重复。 
范例 : 
配置匹配团体表：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match community-list 1
相关命令 : 
show route-map 
## match esi 

match esi 
命令功能 : 
设置一个基于ESI的匹配规则，用于匹配携带非0 ESI的路由。使用no命令恢复缺省配置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match esi 
 
no match esi 
命令参数解释 : 
					无
				 
缺省 : 
没有配置基于ESI的匹配规则。 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match esiZXROSNG(config-route-map)#no match esi
相关命令 : 
show route-map 
## match extcommunity-list 

match extcommunity-list 
命令功能 : 
配置匹配BGP或者VPN拓展团体表。使用no命令删除团体表记录。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match extcommunity-list 
  {*(＜extcommunity-list-number 
＞)|name 
 ＜extcommunity-list-name 
＞}
no match extcommunity-list 
  [{*(＜extcommunity-list-number 
＞)|name 
 ＜extcommunity-list-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜extcommunity-list-number＞|拓展团体号，最多匹配10个拓展团体号，范围：1–500
＜extcommunity-list-name＞|名字长度最长为31个字符，不能是全数字的组合
缺省 : 
无 
使用说明 : 
配置重复的<extcommunity-list-number>会过滤重复。 
范例 : 
配置匹配拓展团体表：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match extcommunity-list 1ZXROSNG(config-route-map)#match extcommunity-list name zte
相关命令 : 
show route-map 
## match interface 

match interface 
命令功能 : 
匹配配置的接口名。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match interface 
  *(＜interface-name 
＞)
no match interface 
  [*(＜interface-name 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，每次最多配置10个接口
缺省 : 
无 
使用说明 : 
配置重复的<interface-name>会过滤重复。 
范例 : 
配置匹配的接口：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match interface gei-0/3/0/8配置匹配的接口：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match interface gei-0/3/0/8
相关命令 : 
show route-map 
## match ip address 

match ip address 
命令功能 : 
重分配任何含有标准访问表许可的目的地网络地址的路由，或对包进行策略路由。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip address 
  [prefix-list 
] *(＜access-list-or-prefix-list 
＞)
no match ip address 
  {prefix-list 
 ＜prefix-list 
＞|[＜access-list 
＞]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜access-list-or-prefix-list＞|访问表名或者前缀列表名名字。如果输入访问表名，最多支持10个ACL列表，长度1–31个字符如果输入前缀列表，最多支持10个前缀列表，长度1–31个字符
缺省 : 
无 
使用说明 : 
配置重复的<acl-name>或<prefix-list-name>会过滤重复。 
范例 : 
配置匹配目的地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip address ACL3
相关命令 : 
show route-map 
## match ip metric 

match ip metric 
命令功能 : 
再分配含指定尺度的路由。使用no命令删除匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip metric 
  {*(＜metric-value 
＞)|{eq 
|ge 
|le 
} ＜metric-value 
＞}
no match ip metric 
  {*(＜metric-value 
＞)|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜metric-value＞|路由尺度，最多可配置10个路由尺度，范围：0–4294967295
eq|运算符等于
ge|运算符大于
le|运算符小于
＜metric-value＞|路由尺度，最多可配置10个路由尺度，范围：0–4294967295
缺省 : 
无 
使用说明 : 
配置重复的<metric-value>会过滤重复。 
范例 : 
配置匹配路由尺度：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip metric 20
相关命令 : 
show route-map 
## match ip next-hop 

match ip next-hop 
命令功能 : 
再分配所制定的标准访问表之一所经过的、有下一跳的路由器地址的路由。使用no命令删除该匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip next-hop 
  [prefix-list 
] *(＜access-list-or-prefix-list 
＞)
no match ip next-hop 
  {prefix-list 
 ＜prefix-list 
＞|[*(＜access-list-name 
＞)]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜access-list-or-prefix-list＞|访问表名或者前缀列表名名字。如果输入访问表名，最多支持10个ACL列表，长度1–31个字符如果输入前缀列表，最多支持10个前缀列表，长度1–31个字符
No参数|描述
---|---
＜prefix-list＞|前缀列表名名字
＜access-list-name＞|标准访问表名，最多可支持10个ACL列表，长度1–31个字符
缺省 : 
无 
使用说明 : 
配置重复的＜access-list-or-prefix-list＞会被过滤。 
范例 : 
1、配置使用ACL匹配下一跳地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip next-hop ACL42、配置使用PFL匹配下一跳地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip next-hop prefix-list PFL1
相关命令 : 
show route-map 
## match ip peer 

match ip peer 
命令功能 : 
设置对于BGP对等体的匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip peer 
  {prefix-list 
 ＜prefix-list 
＞|access-list 
 ＜access-list 
＞}
no match ip peer 
  {[prefix-list 
 ＜prefix-list 
＞]|[access-list 
 ＜access-list 
＞]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜prefix-list＞|前缀列表名，长度1–31个字符
access-list|访问控制列表配置标记
＜access-list＞|访问控制列表名，长度1–31个字符
缺省 : 
无 
使用说明 : 
1、No命令不带参数时删除此命令所有条目，<access-list>与<prefix-list>互斥。2、Route-map每个sequence下最多配置10个<access-list>或<prefix-list>。
范例 : 
配置匹配的BGP对等体：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip peer access-list ACL3
相关命令 : 
show route-map 
## match ip policy-route-id 

match ip policy-route-id 
命令功能 : 
设置对于策略路由的policy-router-id的匹配项 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip policy-route-id 
  ＜id 
＞ {destination 
|source 
}
no match ip policy-route-id 
  [＜id 
＞ {destination 
|source 
}]
				
命令参数解释 : 
参数|描述
---|---
＜id＞|policy-route-id的取值范围为1到63
destination|用源IP查路由获得路由的community属性来匹配策略路由
source|用目的IP查路由获得路由的community属性来匹配策略路由
缺省 : 
无 
使用说明 : 
在一个route-map的不同的序列中，只能配置唯一一个policy-route-id值。在一个route-map中，destination选项和source选项互斥。在一个route-map中，match ip policy-route-id命令和match ip address命令互斥。
范例 : 
设置匹配项对于目的IP策略路由的ID值为1：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# match ip policy-route-id 1 destination 
相关命令 : 
show route-mapmatch ip address
## match ip source 

match ip source 
命令功能 : 
重分配任何含有标准访问表许可的源地网络地址的路由，或对包进行策略路由。使用no命令取消设置。
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip source 
  [prefix-list 
] *(＜access-list-or-prefix-list 
＞)
no match ip source 
  {prefix-list 
 ＜prefix-list 
＞|[＜access-list 
＞]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜access-list-or-prefix-list＞|访问表名或者前缀列表名名字。如果输入访问表名，最多支持10个ACL列表，长度1–31个字符如果输入前缀列表，最多支持10个前缀列表，长度1–31个字符
缺省 : 
无 
使用说明 : 
配置重复的<acl-name>或<prefix-list-name>会过滤重复。
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip source ACL1
相关命令 : 
show route-map
## match ip tag 

match ip tag 
命令功能 : 
再分配路由表中与指定标记相匹配的路由。使用no命令删除标记匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip tag 
  *(＜tag-value 
＞)
no match ip tag 
  [*(＜tag-value 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜tag-value＞|路由标志值，最多配置10个路由标识值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
配置重复的<tag-value>会过滤重复。 
范例 : 
配置再分配路由表中与指定标记相匹配的路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ip tag 0
相关命令 : 
show route-map 
## match ipv6 address 

match ipv6 address 
命令功能 : 
再分配IPv6任何含有标准访问表许可的目的地网络地址的路由，或对包进行策略路由。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 address 
  [prefix-list 
] *(＜access-list-or-prefix-list 
＞)
no match ipv6 address 
  {prefix-list 
 ＜prefix-list 
＞|[*(＜ipv6-access-list-name 
＞)]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜access-list-or-prefix-list＞|访问表名或者前缀列表名名字。如果输入访问表名，最多支持10个ACL列表，长度1–31个字符如果输入前缀列表，最多支持10个前缀列表，长度1–31个字符
缺省 : 
无 
使用说明 : 
配置重复的<access-list-name>会过滤重复。 
范例 : 
再分配IPV6任何含有标准访问表许可的目的地网络地址的路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 address ACL5
相关命令 : 
show route-map 
## match ipv6 metric 

match ipv6 metric 
命令功能 : 
再分配含指定尺度的路由。使用no命令删除匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 metric 
  {*(＜metric-value 
＞)|{eq 
|ge 
|le 
} ＜metric-value 
＞}
no match ipv6 metric 
  {*(＜metric-value 
＞)|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜metric-value＞|路由尺度，最多可配置10个路由尺度，范围：0–4294967295
eq|运算符等于
ge|运算符大于
le|运算符小于
＜metric-value＞|路由尺度，最多可配置10个路由尺度，范围：0–4294967295
缺省 : 
无 
使用说明 : 
配置重复的< metric-value>会过滤重复。 
范例 : 
配置路由尺度：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 metric 20009
相关命令 : 
show route-map 
## match ipv6 next-hop 

match ipv6 next-hop 
命令功能 : 
对IPv6下一跳进行匹配。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 next-hop 
  [prefix-list 
] *(＜access-list-or-prefix-list 
＞)
no match ipv6 next-hop 
  {prefix-list 
 ＜prefix-list 
＞|[*(＜ipv6-access-list-name 
＞)]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜access-list-or-prefix-list＞|访问表名或者前缀列表名名字。如果输入访问表名，最多支持10个ACL列表，长度1–31个字符如果输入前缀列表，最多支持10个前缀列表，长度1–31个字符
No参数|描述
---|---
＜prefix-list＞|前缀列表名名字
＜ipv6-access-list-name＞|标准访问表的名称，长度1–31个字符,最多可配置10个访问列表
缺省 : 
无 
使用说明 : 
配置重复的＜access-list-or-prefix-list＞会被过滤。 
范例 : 
1、使用ACL对IPv6下一跳进行匹配：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 next-hop ACL72、使用PFL对IPv6下一跳进行匹配：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 next-hop prefix-list PFL1
相关命令 : 
show route-map 
## match ipv6 peer 

match ipv6 peer 
命令功能 : 
设置对于IPv6 BGP对等体的匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 peer 
  {prefix-list 
 ＜ipv6-prefix-list 
＞|access-list 
 ＜ipv6-access-list 
＞}
no match ipv6 peer 
  {[prefix-list 
 ＜ipv6-prefix-list 
＞]|[access-list 
 ＜ipv6-access-list 
＞]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜ipv6-prefix-list＞|IPv6前缀列表名，长度1–31个字符
access-list|访问控制列表配置标记
＜ipv6-access-list＞|IPv6访问控制列表名，长度1–31个字符
缺省 : 
无 
使用说明 : 
1、No命令不带参数时删除此命令所有条目，<access-list>与<prefix-list>互斥。2、Route-map每个sequence下最多配置10个<access-list>或<prefix-list>。
范例 : 
配置匹配的IPv6 BGP对等体：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 peer access-list ACL3
相关命令 : 
show route-map 
## match ipv6 policy-route-id 

match ipv6 policy-route-id 
命令功能 : 
设置对于IPv6策略路由的policy-router-id的匹配项 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 policy-route-id 
  ＜id 
＞ {destination 
|source 
}
no match ipv6 policy-route-id 
  [＜id 
＞ {destination 
|source 
}]
				
命令参数解释 : 
参数|描述
---|---
＜id＞|policy-route-id的取值范围为1到63
destination|用源IP查路由获得路由的community属性来匹配策略路由
source|用目的IP查路由获得路由的community属性来匹配策略路由
缺省 : 
无 
使用说明 : 
在一个route-map的不同的序列中，只能配置唯一一个policy-route-id值。在一个route-map中，destination选项和source选项互斥。在一个route-map中，match ipv6 policy命令和match ipv6 address命令互斥。
范例 : 
设置匹配项对于目的IP策略路由的ID值为1：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# match ipv6 policy-route-id 1 destination 
相关命令 : 
show route-mapmatch ipv6 address
## match ipv6 source 

match ipv6 source 
命令功能 : 
再分配IPv6任何含有标准访问表许可的源网络地址的路由，或对包进行策略路由。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 source 
  [prefix-list 
] *(＜access-list-or-prefix-list 
＞)
no match ipv6 source 
  {prefix-list 
 ＜prefix-list 
＞|[*(＜ipv6-access-list-name 
＞)]}
				
命令参数解释 : 
参数|描述
---|---
prefix-list|前缀列表配置标记
＜access-list-or-prefix-list＞|访问表名或者前缀列表名名字。如果输入访问表名，最多支持10个ACL列表，长度1–31个字符如果输入前缀列表，最多支持10个前缀列表，长度1–31个字符
No参数|描述
---|---
＜prefix-list＞|前缀列表名名字
＜ipv6-access-list-name＞|访问表名
缺省 : 
无 
使用说明 : 
配置重复的＜access-list-or-prefix-list＞会被过滤。
范例 : 
1、使用ACL匹配源地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 source ACL22、使用PFL匹配源地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 source prefix-list PFL1p
相关命令 : 
show route-map
## match ipv6 tag 

match ipv6 tag 
命令功能 : 
再分配路由表中与指定标记相匹配的路由。使用no命令删除标记匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 tag 
  *(＜tag-value 
＞)
no match ipv6 tag 
  [*(＜tag-value 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜tag-value＞|路由标志值，最多配置10个路由标识值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
配置重复的<tag-value>会过滤重复。 
范例 : 
配置再分配路由表中与指定标记相匹配的路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match ipv6 tag 0
相关命令 : 
show route-map 
## match l2-vni-label 

match l2-vni-label 
命令功能 : 
匹配二层VNI标签值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match l2-vni-label 
  ＜label 
＞
no match l2-vni-label 
命令参数解释 : 
参数|描述
---|---
＜label＞|标签值，范围：<1~16777215 >
缺省 : 
无 
使用说明 : 
1.route-map提供match l2-vni-label项，BGP用来匹配EVPN路由的二层VNI标签属性。 
范例 : 
1.在route-map中配置l2-vni-label：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# match l2-vni-label 16777215
相关命令 : 
show route-map 
## match l3-vni-label 

match l3-vni-label 
命令功能 : 
匹配三层VNI标签值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match l3-vni-label 
  ＜label 
＞
no match l3-vni-label 
命令参数解释 : 
参数|描述
---|---
＜label＞|标签值，范围：<1~16777215 >
缺省 : 
无 
使用说明 : 
1.route-map提供match l3-vni-label项，BGP用来匹配EVPN路由的三层VNI标签属性。 
范例 : 
1.在route-map中配置l3-vni-label：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# match l3-vni-label 16777215
相关命令 : 
show route-map 
## match large-community-list 

match large-community-list 
命令功能 : 
配置匹配大团体表。使用no命令删除大团体表记录。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match large-community-list 
 name 
 ＜large-community-list-name 
＞
no match large-community-list 
  [name 
 ＜large-community-list-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜large-community-list-name＞|名字长度最长为31个字符
缺省 : 
无 
使用说明 : 
使用场景：BGP用来匹配大团体表。注意事项：1、同序列下最多配置10个大团体列表名。No命令不带参数，是删除当前序列号下所有大团体列表。
范例 : 
配置匹配大团体表：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match large-community-list name a
相关命令 : 
show route-map 
## match local-preference 

match local-preference 
命令功能 : 
匹配优先权值。使用no命令恢复缺省值。
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match local-preference 
  {eq 
|ge 
|le 
} ＜local-preference-value 
＞
no match local-preference 
命令参数解释 : 
参数|描述
---|---
eq|运算符等于
ge|运算符大于
le|运算符小于
＜local-preference-value＞|优先权值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match local-preference eq 4294967295
相关命令 : 
show route-map
## match metric 

match metric 
命令功能 : 
再分配含指定尺度的路由。使用no命令删除匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match metric 
  {*(＜metric-value 
＞)|{eq 
|ge 
|le 
} ＜metric-value 
＞}
no match metric 
  {*(＜metric-value 
＞)|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜metric-value＞|路由尺度，最多可配置10个路由尺度，范围：0–4294967295
eq|运算符等于
ge|运算符大于
le|运算符小于
＜metric-value＞|路由尺度，最多可配置10个路由尺度，范围：0–4294967295
No参数|描述
---|---
all|删除所有路由尺度
缺省 : 
无 
使用说明 : 
配置重复的<metric-value>会被过滤，此命令与match ip metric和match ipv6 metric互斥。 
范例 : 
配置匹配路由尺度：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match metric 20
相关命令 : 
show route-map 
## match mpls-label 

match mpls-label 
命令功能 : 
设置一个基于MPLS标签的匹配规则，用于匹配带有MPLS标签的路由。使用no命令恢复缺省配置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match mpls-label 
 
no match mpls-label 
命令参数解释 : 
					无
				 
缺省 : 
没有配置基于MPLS标签的匹配规则。 
使用说明 : 
无 
范例 : 
匹配携带标签标志的路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match mpls-label ZXROSNG(config-route-map)#no match mpls-label 
相关命令 : 
show route-map 
## match origin 

match origin 
命令功能 : 
匹配BGP路由起源属性。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match origin 
  {igp 
|egp 
|incomplete 
}
no match origin 
命令参数解释 : 
参数|描述
---|---
igp|本地IGP
egp|远程EGP
incomplete|未知的残余项
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match origin egp
相关命令 : 
show route-map
## match rd-list 

match rd-list 
命令功能 : 
BGP基于RD属性的过滤 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match rd-list 
  *(＜rd-list-number 
＞)
no match rd-list 
  [*(＜rd-list-number 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜rd-list-number＞|rd值，范围1-500
缺省 : 
无 
使用说明 : 
配置重复的<rd-list-number>会过滤重复 
范例 : 
ZXROSNG(config)#route-map zte  ZXROSNG(config-route-map)#match rd-list 1
相关命令 : 
show route-map 
## match route-type 

match route-type 
命令功能 : 
配置匹配路由类型。使用no命令删除该匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match route-type 
  {{local 
|internal 
|level-1 
|level-2 
}|external 
 [{type-1 
|type-2 
}]|nssa-external 
 [{type-1 
|type-2 
}]|{ebgp 
|ibgp 
|static 
|bgp-agg 
}}
no match route-type 
  [{{local 
|internal 
|level-1 
|level-2 
}|external 
 [{type-1 
|type-2 
}]|nssa-external 
 [{type-1 
|type-2 
}]|{ebgp 
|ibgp 
|static 
|bgp-agg 
}}]
				
命令参数解释 : 
参数|描述
---|---
local|路由类型
internal|路由类型
level-1|路由类型
level-2|路由类型
external|OSPF external路由类型
type-1|OSPF external路由类型
type-2|OSPF external路由类型
nssa-external|OSPF NSSA external type-1或type-2路由类型
type-1|OSPF NSSA external type-1路由类型
type-2|OSPF NSSA external type-2路由类型
ebgp|EBGP路由类型
ibgp|IBGP路由类型
static|静态路由类型
bgp-agg|BGP聚合路由类型
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.配置匹配路由类型：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match route-type external type-12. 配置匹配EBGP路由类型：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match route-type ebgp3. 去配置匹配BGP聚合路由类型：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# no match route-type bgp-agg
相关命令 : 
show route-map 
## match rpki origin-as-validation 

match rpki origin-as-validation 
命令功能 : 
设置对于RPKI的BGP路由起源AS验证结果的匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match rpki origin-as-validation 
  {valid 
|invalid 
|not-found 
}
no match rpki origin-as-validation 
  [{valid 
|invalid 
|not-found 
}]
				
命令参数解释 : 
参数|描述
---|---
valid|有效的BGP路由
invalid|无效的BGP路由
not-found|无法验证的BGP路由
缺省 : 
无 
使用说明 : 
配置基于BGP路由起源AS验证结果的匹配规则后，路由信息必须符合基于BGP路由起源AS验证结果的匹配规则，才可以执行相应动作对路由的一些属性进行修改。 
范例 : 
配置匹配的RPKI的BGP路由起源AS验证结果：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match rpki origin-as-validation valid
相关命令 : 
show route-map 
## match tag 

match tag 
命令功能 : 
再分配路由表中与指定标记相匹配的路由。使用no命令删除标记匹配项。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match tag 
  *(＜tag-value 
＞)
no match tag 
  [*(＜tag-value 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜tag-value＞|路由标志值，最多配置10个路由标识值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
配置重复的<tag-value>会被过滤。此命令与match ip tag和match ipv6 tag互斥。 
范例 : 
配置再分配路由表中与指定标记相匹配的路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match tag 0
相关命令 : 
show route-map 
## match vni 

match vni 
命令功能 : 
使用本命令在route-map中配置VNI的匹配项，VNI匹配项用于PBR匹配报文的VXLAN network identifier。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
match vni 
 from 
 ＜lower-limit 
＞ to 
 ＜upper-limit 
＞ [,from 
 ＜lower-limit 
＞ to 
 ＜upper-limit 
＞] [,from 
 ＜lower-limit 
＞ to 
 ＜upper-limit 
＞] [,from 
 ＜lower-limit 
＞ to 
 ＜upper-limit 
＞]
no match vni 
命令参数解释 : 
参数|描述
---|---
＜lower-limit＞|数值段的下限，配置范围1-16777215
＜upper-limit＞|数值段的上限，配置范围1-16777215
＜lower-limit＞|数值段的下限，配置范围1-16777215
＜upper-limit＞|数值段的上限，配置范围1-16777215
＜lower-limit＞|数值段的下限，配置范围1-16777215
＜upper-limit＞|数值段的上限，配置范围1-16777215
＜lower-limit＞|数值段的下限，配置范围1-16777215
＜upper-limit＞|数值段的上限，配置范围1-16777215
缺省 : 
无 
使用说明 : 
1 route-map中配置VNI后，route-map具有IPV4属性，不能再配置IPV6属性的命令。2 route-map配置具有IPV6属性的命令后，不能再配置VNI。3 同一个route-map中，match ip address acl 和 match vni不能同时配置。4 match vni中一个数据段的上限数值应大于等于下限数值。5 match vni中一个数据段的上限数值和下限数值的差值应小于等于255。6 match vni中各个段的数值不能有重复部分。
范例 : 
在route-map中配置match vni：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#match vni from 1 to 2
相关命令 : 
无 
## policy-commit-immediately 

policy-commit-immediately 
命令功能 : 
操作类命令，执行后策略对业务立即生效。可以通过选择不同的参数实现所有策略对业务立即生效或者指定的某种策略对业务立即生效。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
policy-commit-immediately 
  {all 
|as-path 
|community-list 
|extcommunity-list 
|rd-list 
|route-map 
}
命令参数解释 : 
参数|描述
---|---
all|命令作用route-map、rd-list、as-path、community-list、extcommunity-list立即生效同步到业务
as-path|命令作用as-path模块立即生效同步到业务
community-list|命令作用community-list模块立即生效同步到业务
extcommunity-list|命令作用extcommunity-list模块立即生效同步到业务
rd-list|命令作用rd-list模块立即生效同步到业务
route-map|命令作用route-map模块立即生效同步到业务
缺省 : 
无 
使用说明 : 
1、应用业务（如BGP、OSPF等）引用策略（如route-map、as-path、community-list、rd-list等）后，可以通过本命令实现对之前已创建、更新的策略立即同步到对应的应用业务，但是对执行该命令后，新生成的策略不生效。2、命令配置多次，采用覆盖方式生效，如先配置参数all，再配置参数as-path，最后只生效as-path。3、本命令配置后会覆盖对应业务已配置的trigger-delay延迟时间，使之立即生效，不会延迟。
范例 : 
1、所有策略立即同步到对应的业务：ZXROSNG(config)#policy-commit-immediately all2、策略route-map立即同步到对应的业务：ZXROSNG(config)#policy-commit-immediately route-map
相关命令 : 
ip as-path access-list trigger-delayip community-list trigger-delayip extcommunity-list trigger-delayip rd-list trigger-delayroute-map-trigger-delay
## route-map 

route-map 
命令功能 : 
创建（删除）或进入route-map配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
route-map 
  ＜routemap-name 
＞ [{deny 
|permit 
}] [＜routemap-sequence 
＞]
no route-map 
  ＜routemap-name 
＞ [＜routemap-sequence 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜routemap-name＞|路由映射的名称，长度1–31个字符
deny|如果路由映射符合匹配条件，不允许再分配策略路由标志，不配置时的缺省值是permit
permit|如果路由映射符合匹配条件，允许再分配策略路由标志，不配置时的缺省值是permit
＜routemap-sequence＞|序列号，范围：0–65535，不配置时的缺省值是10
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置route-map：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#
相关命令 : 
show route-map 
## route-map-trigger-delay 

route-map-trigger-delay 
命令功能 : 
设置route-map同步到应用的延迟时间。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
route-map-trigger-delay 
  ＜delay-time 
＞
no route-map-trigger-delay 
命令参数解释 : 
参数|描述
---|---
＜delay-time＞|延迟时间，范围0-30(单位：秒)
缺省 : 
同步延时时间$#34406405#$。 
使用说明 : 
1、应用协议（如BGP、OSPF等）引用route-map后，当route-map创建、更新，会同步到对应的应用协议。同步会有一定延时，可以通过本命令调整延时时间。2、本配置针对所有route-map实例生效。
范例 : 
设置route-map同步延迟时间为20秒：ZXROSNG(config)#route-map-trigger-delay 20
相关命令 : 
show route-map 
## set as-path 

set as-path 
命令功能 : 
修改BGP路由自治系统路径。使用no命令取消修改。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set as-path 
  {empty 
|{prepend 
|replace 
|delete 
} <1-65535>/<1-65535>.<0-65535> 
 [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
] [<1-65535>/<1-65535>.<0-65535> 
]}
no set as-path 
命令参数解释 : 
参数|描述
---|---
empty|清空标志位
prepend|追加标志位
replace|替换标志位
delete|删除标志位
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
<1-65535>/<1-65535>.<0-65535>|<1-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为1-65535。最多10个；<1-65535>.<0-65535> 表示把该值附加到与路由映射相匹配的as-path路由中，取值为4个4字节形式为aa.nn的AS号，aa的取值范围是1-65535，nn的取值范围是0-65535。最多10个
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置BGP路由自治系统路径属性：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set as-path prepend 2 3 4 5 6
相关命令 : 
show route-map 
## set color-list 

set color-list 
命令功能 : 
设置BGP SR携带的color值，可以配置多个。使用no命令取消配置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set color-list 
  ＜color-list-name 
＞
no set color-list 
命令参数解释 : 
参数|描述
---|---
＜color-list-name＞|color列表名称,字符串长度范围：1–31
缺省 : 
无 
使用说明 : 
同一序列号下，set color命令和set color-list命令不能同时配置。 
范例 : 
配置color列表，用于标识BGP SR能够提供的服务质量，以及对外层SR policy的要求：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set color-list a
相关命令 : 
show route-map 
## set community 

set community 
命令功能 : 
设置BGP COMMUNITY属性。使用no命令删除该属性。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set community 
  {none 
|[{additive 
|delete 
}] {*({internet 
|no-export 
|no-advertise 
|no-export-subconfed 
|＜community-number 
＞|<0-65535>:<0-65535> 
})|name 
 ＜community-list-name 
＞}}
no set community 
  {[{additive 
|delete 
}] {*({internet 
|no-export 
|no-advertise 
|no-export-subconfed 
|<0-65535>:<0-65535> 
|＜community-number 
＞})|name 
 ＜community-list-name 
＞}|all 
}
				
命令参数解释 : 
参数|描述
---|---
none|没有团队属性
additive|添加一个存在的community
delete|删除一个存在的community
internet|设置为互联网标记
no-export|特殊的community值0xffffff01
no-advertise|特殊的community值0xffffff02
no-export-subconfed|特殊的community值0xffffff03
＜community-number＞|普通的community值，范围：1–4294967295
<0-65535>:<0-65535>|普通的community值，aa:nn格式，范围：<0–65535>:<0–65535>
＜community-list-name＞|名字长度最长为31个字符，不能是全数字的组合
No参数|描述
---|---
all|删除所有set community配置
缺省 : 
无 
使用说明 : 
配置重复值会过滤重复。同一个序列号内set community value和set community name互斥
范例 : 
设置BGP COMMUNITY属性和COMMUNITY名称：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set community 12 13 no-exportZXROSNG(config-route-map)#exitZXROSNG(config)#route-map zte1ZXROSNG(config-route-map)#set community name zte
相关命令 : 
show route-map 
## set dampening 

set dampening 
命令功能 : 
设置BGP路由阻尼因素。使用no命令使该功能无效。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set dampening 
  ＜halflife 
＞ ＜reuse 
＞ ＜suppress 
＞ ＜maxsuptime 
＞
no set dampening 
命令参数解释 : 
参数|描述
---|---
＜halflife＞|改变路由阻尼因素的半衰期，范围：1–45
＜reuse＞|改变路由阻尼因素的重新使用值，范围：1–20000
＜suppress＞|改变路由阻尼因素的路由抑制值，范围：1–20000
＜maxsuptime＞|改变路由阻尼因素的最大抑制时间，通常路由抑制时间到达该值以后，惩罚值不再增加，范围：1–255
缺省 : 
无 
使用说明 : 
路由阻尼因素的路由抑制值应该大于路由阻尼因素的重新使用值。 
范例 : 
配置路由阻尼因素：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set dampening 45 100 210 46
相关命令 : 
show route-map 
## set distance 

set distance 
命令功能 : 
基于OSPF的route-map里支持匹配策略的前缀设置不同的distance值。使用no命令取消配置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set distance 
  ＜distance-value 
＞
no set distance 
命令参数解释 : 
参数|描述
---|---
＜distance-value＞|distance的取值范围为1到255
缺省 : 
无 
使用说明 : 
Route-map提供set distance项，在OSPF配置中应用route-map。 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set distance 1
相关命令 : 
show route-map 
## set dscp 

set dscp 
命令功能 : 
设置PBR的DSCP值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set dscp 
  ＜dscp-value 
＞
no set dscp 
命令参数解释 : 
参数|描述
---|---
＜dscp-value＞|PBR的DSCP值，范围：0-63
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置DSCP值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set dscp 35
相关命令 : 
show route-map 
## set evpn-router-mac interface 

set evpn-router-mac interface 
命令功能 : 
BGP 获取配置的接口MAC，用来设置EVPN Router's MAC扩展团体属性。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set evpn-router-mac interface 
  ＜interface-name 
＞
no set evpn-router-mac interface 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
无 
使用说明 : 
1.    route-map提供set evpn-router-mac interface项，BGP通过获取配置的接口MAC地址，设置EVPN Router's MAC扩展团体属性。 
范例 : 
在route-map中配置evpn-router-mac interface：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set evpn-router-mac interface loopback1
相关命令 : 
show route-map 
## set extcommunity general-asn 

set extcommunity general-asn 
命令功能 : 
设置BGP EXTCOMMUNITY属性。使用no命令取消设置。
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set extcommunity general-asn 
  {remove 
|[additive 
] *(＜<0-4294967295>:<0-4294967295> 
＞)}
no set extcommunity general-asn 
  [[additive 
] ＜<0-4294967295>:<0-4294967295> 
＞]
				
命令参数解释 : 
参数|描述
---|---
remove|去除存在的扩展团体
additive|添加一个已经存在的扩展团体
＜<0-4294967295>:<0-4294967295>＞|VPN的扩展团体
缺省 : 
无 
使用说明 : 
配置重复值会过滤重复。
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set extcommunity general-asn 0:0
相关命令 : 
show route-map
## set extcommunity rt-trans 

set extcommunity rt-trans 
命令功能 : 
设置BGP EXTCOMMUNITY属性。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set extcommunity rt-trans 
  {remove 
|[additive 
] *({<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
})}
no set extcommunity rt-trans 
  [[additive 
] {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}]
				
命令参数解释 : 
参数|描述
---|---
remove|去除一个已经存在的扩展团体
additive|添加一个已经存在的扩展团体
<0-65535>:<0-4294967295>|VPN的扩展团体
A.B.C.D:<0-65535>|VPN的扩展团体
<1-65535>.<0-65535>:<0-65535>|VPN的拓展团体
缺省 : 
无 
使用说明 : 
配置重复值会过滤重复。 
范例 : 
设置BGP EXTCOMMUNITY属性：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set extcommunity rt-trans 192.168.20.110:0
相关命令 : 
show route-map 
## set extcommunity soo-trans 

set extcommunity soo-trans 
命令功能 : 
设置BGP EXTCOMMUNITY属性。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set extcommunity soo-trans 
  {remove 
|{<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}}
no set extcommunity soo-trans 
命令参数解释 : 
参数|描述
---|---
remove|去除存在的扩展团体
<0-65535>:<0-4294967295>|VPN的扩展团体
A.B.C.D:<0-65535>|VPN的扩展团体
<1-65535>.<0-65535>:<0-65535>|VPN的拓展团体
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置BGP EXTCOMMUNITY属性：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set extcommunity soo-trans 65535:1
相关命令 : 
show route-map 
## set global 

set global 
命令功能 : 
设置PBR全局路由。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set global 
  [ip 
 next-hop 
 ＜ipv4-address 
＞]
no set global 
命令参数解释 : 
参数|描述
---|---
ip|ip地址
next-hop|下一跳
＜ipv4-address＞|下一跳的IP地址，十进制点分形式
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置全局路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set global ip next-hop 1.1.1.1
相关命令 : 
show route-map 
## set gw-ip 

set gw-ip 
命令功能 : 
指定网关的IPv4地址。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set gw-ip 
  ＜ipv4-address 
＞
no set gw-ip 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|网关IPv4地址，十进制点分形式
缺省 : 
无 
使用说明 : 
此命令与set ipv6 gw-ip互斥。 
范例 : 
指定网关的IPv4地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set gw-ip 2.2.2.2
相关命令 : 
show route-map 
## set interface 

set interface 
命令功能 : 
当数据包符合用于策略路由的路由映像的一个匹配项而可被策略路由时，使用本命令把数据包路由到指定接口上。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set interface 
  *(＜interface-name 
＞)
no set interface 
  [*(＜interface-name 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，每次最多配置10个接口
缺省 : 
无 
使用说明 : 
配置重复<interface-name>会过滤重复。 
范例 : 
把数据包路由到指定接口gre_tunnel10上：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set interface gre_tunnel10
相关命令 : 
show route-map 
## set ip default-next-hop 

set ip default-next-hop 
命令功能 : 
设置默认下一跳地址。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip default-next-hop 
  ＜ipv4-address 
＞ [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞] [＜ipv4-address 
＞]
no set ip default-next-hop 
  [*(＜ipv4-address 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
＜ipv4-address＞|下一跳IP地址，十进制点分形式
缺省 : 
无 
使用说明 : 
无 
范例 : 
在route-map中配置默认下一跳地址为3.3.3.3：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip default-next-hop 3.3.3.3
相关命令 : 
show route-map 
## set ip metric 

set ip metric 
命令功能 : 
设置路由选择协议的尺度值。使用no命令恢复缺省状态。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip metric 
  [{+ 
|- 
}] ＜metric-value 
＞
no set ip metric 
命令参数解释 : 
参数|描述
---|---
+|表示加
-|表示减
＜metric-value＞|尺度值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置路由选择协议的尺度值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip metric + 1
相关命令 : 
show route-map 
## set ip metric-type 

set ip metric-type 
命令功能 : 
设置路由选择协议的尺度类型。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip metric-type 
  {internal 
|external 
|type-1 
|type-2 
}
no set ip metric-type 
命令参数解释 : 
参数|描述
---|---
internal|IS-IS内部尺度
external|IS-IS外部尺度
type-1|OSPF外部类型1尺度
type-2|OSPF外部类型2尺度
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置路由选择协议的尺度类型：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip metric-type internal
相关命令 : 
show route-map 
## set ip next-hop 

set ip next-hop 
命令功能 : 
当数据包符合用于策略路由的路由映像的一个匹配项而可被策略路由时，使用本命令把数据包路由到指定的下一跳。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip next-hop 
  ＜ipv4-address 
＞ [track 
 ＜track-name 
＞] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]] [＜ipv4-address 
＞ [track 
 ＜track-name 
＞]]
no set ip next-hop 
  [*(＜ipv4-address 
＞)]
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
＜ipv4-address＞|下一跳IP地址，十进制点分形式，最多可配置10个地址
＜track-name＞|track 名称，长度1–31个字符，最多可配置10个
缺省 : 
无 
使用说明 : 
无 
范例 : 
把数据包路由到指定的下一跳地址3.3.3.3上：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip next-hop 3.3.3.3
相关命令 : 
show route-map 
## set ip path interface 

set ip path interface 
命令功能 : 
当数据包符合用于策略路由的路由映像的一个匹配项而可被策略路由时，使用本命令把数据包路由到指定的以太接口及下一跳。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip path interface 
  ＜interface 
＞ next-hop 
 ＜nexthop 
＞
no set ip path interface 
命令参数解释 : 
参数|描述
---|---
＜interface＞|接口名称
＜nexthop＞|下一跳IP地址，十进制点分形式
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip path interface gei-0/1/0/2 next-hop 1.2.3.4ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip path interface gei-0/1/0/2 next-hop 1.2.3.4
相关命令 : 
show route-map 
## set ip precedence 

set ip precedence 
命令功能 : 
设置IP报头优先级。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip precedence 
  {＜precedence-value 
＞|＜precedence-value 
＞}
no set ip precedence 
命令参数解释 : 
参数|描述
---|---
＜precedence-value＞|在IP报头中设置优先值的编号，范围：0–7
＜precedence-value＞|在IP报头中设置优先值的编号，范围：0–7
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置IP报头优先级：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip precedence 5
相关命令 : 
show route-map 
## set ip sr-policy 

set ip sr-policy 
命令功能 : 
当数据包符合应用于PBR的route-map的一个匹配项而可被策略路由时，使用本命令把数据包转发到相应color值和IPv4地址对应的隧道。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip sr-policy 
 color 
 ＜color-value 
＞ end-point 
 ＜ipv4-address 
＞
no set ip sr-policy 
命令参数解释 : 
参数|描述
---|---
＜color-value＞|配置color值，范围：1-4294967295
＜ipv4-address＞|对端IPv4地址，十进制点分形式
缺省 : 
无 
使用说明 : 
使用场景：此命令应用于策略路由，当规则匹配时把数据包转发到相应color值和IPv4地址对应的隧道。前提要求：此命令与set ipv6 sr-policy互斥。
范例 : 
当规则匹配时把数据包转发到相应color值和IPv4地址对应的隧道：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip sr-policy color 12 end-point 1.2.3.4
相关命令 : 
show route-map 
## set ip tag 

set ip tag 
命令功能 : 
设置目的路由选择协议的标记值。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip tag 
  ＜tag-value 
＞
no set ip tag 
命令参数解释 : 
参数|描述
---|---
＜tag-value＞|标记值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置目的路由选择协议的标记值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip tag 210
相关命令 : 
show route-map 
## set ip tos 

set ip tos 
命令功能 : 
设置IP报头的TOS字段值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip tos 
  {＜tos-value 
＞|＜tos-value 
＞}
no set ip tos 
命令参数解释 : 
参数|描述
---|---
＜tos-value＞|TOS字段值，范围：0–15
＜tos-value＞|TOS字段值，范围：0–15
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置IP报头的TOS字段值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ip tos normal
相关命令 : 
show route-map 
## set ip vxlan-tunnel source 

set ip vxlan-tunnel source 
命令功能 : 
设置VXLAN隧道源地址。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ip vxlan-tunnel source 
  ＜ipv4-address 
＞
no set ip vxlan-tunnel source 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|VXLAN隧道源IP地址，十进制点分形式
缺省 : 
无 
使用说明 : 
1. route-map提供set ip vxlan-tunnel source项，BGP通过此配置来修改VXLAN隧道的源地址。 
范例 : 
在route-map中配置ip vxlan-tunnel source：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set ip vxlan-tunnel source 1.2.3.4
相关命令 : 
show route-map 
## set ipv6 gw-ip 

set ipv6 gw-ip 
命令功能 : 
设置网关IPv6地址。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 gw-ip 
  ＜ipv6-address 
＞
no set ipv6 gw-ip 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|网关IPv6地址，十六进制点分形式
缺省 : 
无 
使用说明 : 
此命令与set gw-ip互斥。 
范例 : 
设置网关IPv6地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 gw-ip 1:1::2:3
相关命令 : 
show route-map 
## set ipv6 metric 

set ipv6 metric 
命令功能 : 
设置IPv6路由选择协议的尺度值。使用no命令恢复缺省状态。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 metric 
  [{+ 
|- 
}] ＜metric 
＞
no set ipv6 metric 
命令参数解释 : 
参数|描述
---|---
+|表示加
-|表示减
＜metric＞|尺度值，范围：0-4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置路由协议的尺度值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 metric + 2346
相关命令 : 
show route-map 
## set ipv6 metric-type 

set ipv6 metric-type 
命令功能 : 
设置路由选择协议的尺度类型。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 metric-type 
  {internal 
|external 
|type-1 
|type-2 
}
no set ipv6 metric-type 
命令参数解释 : 
参数|描述
---|---
internal|IS-IS内部尺度
external|IS-IS外部尺度
type-1|OSPF外部类型1尺度
type-2|OSPF外部类型2尺度
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置IPv6路由选择协议的尺度类型：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 metric-type internal
相关命令 : 
show route-map 
## set ipv6 next-hop 

set ipv6 next-hop 
命令功能 : 
设置下一跳地址为IPv6的路由。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 next-hop 
  {peer-address 
|*(＜ipv6-address 
＞)}
no set ipv6 next-hop 
  {peer-address 
|[*(＜ipv6-address 
＞)]}
				
命令参数解释 : 
参数|描述
---|---
peer-address|直连地址标识
＜ipv6-address＞|下一跳IPv6地址，十六进制点分形式，最多支持10个IPv6地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置下一跳地址为IPv6的路由：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 next-hop 1:1::2:3
相关命令 : 
show route-map 
## set ipv6 path interface 

set ipv6 path interface 
命令功能 : 
当数据包符合用于策略路由的路由映像的一个匹配项而可被策略路由时，使用本命令把数据包路由到指定的以太接口及下一跳。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 path interface 
  ＜interface 
＞ next-hop 
 ＜nexthop 
＞
no set ipv6 path interface 
命令参数解释 : 
参数|描述
---|---
＜interface＞|接口名称
＜nexthop＞|下一跳IPv6地址，十六进制点分形式
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set ipv6 path interfac gei-0/1/0/2 next-hop 1:0:0:0:0:0:0:2ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set ipv6 path interfac gei-0/1/0/2 next-hop 1:0:0:0:0:0:0:2
相关命令 : 
show route-map 
## set ipv6 precedence 

set ipv6 precedence 
命令功能 : 
设置IPv6报头优先级。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 precedence 
  {＜precedence-value 
＞|＜precedence-value 
＞}
no set ipv6 precedence 
命令参数解释 : 
参数|描述
---|---
＜precedence-value＞|在IP报头中设置优先值的编号，范围：0–7
＜precedence-value＞|在IP报头中设置优先值的编号，范围：0–7
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置IPv6报头优先级：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 precedence 5
相关命令 : 
show route-map 
## set ipv6 sr-policy 

set ipv6 sr-policy 
命令功能 : 
当数据包符合应用于PBR的route-map的一个匹配项而可被策略路由时，使用本命令把数据包转发到相应color值和IPv6地址对应的隧道。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 sr-policy 
 color 
 ＜color-value 
＞ end-point 
 ＜ipv6-address 
＞
no set ipv6 sr-policy 
命令参数解释 : 
参数|描述
---|---
＜color-value＞|配置color值，范围：1-4294967295
＜ipv6-address＞|对端IPv6地址，十六进制点分形式
缺省 : 
无 
使用说明 : 
使用场景：此命令应用于策略路由，当规则匹配时把数据包转发到相应color值和IPv6地址对应的隧道。前提要求：此命令与set ip sr-policy互斥。
范例 : 
当规则匹配时把数据包转发到相应color值和IPv6地址对应的隧道：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 sr-policy color 12 end-point 1::1
相关命令 : 
show route-map 
## set ipv6 tag 

set ipv6 tag 
命令功能 : 
设置目的IPv6路由选择协议的标记值。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 tag 
  ＜tag 
＞
no set ipv6 tag 
命令参数解释 : 
参数|描述
---|---
＜tag＞|标记值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置目的IPv6路由选择协议的标记值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 tag 33
相关命令 : 
show route-map 
## set ipv6 traffic-class 

set ipv6 traffic-class 
命令功能 : 
设置IPv6路由的traffic等级，使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 traffic-class 
  ＜traffic-value 
＞
no set ipv6 traffic-class 
命令参数解释 : 
参数|描述
---|---
＜traffic-value＞|IPv6路由traffic等级值，范围：0-255
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置IPv6路由的traffic等级：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set ipv6 traffic-class 2
相关命令 : 
show route-map 
## set ipv6 vxlan-tunnel source 

set ipv6 vxlan-tunnel source 
命令功能 : 
设置VXLAN隧道IPv6源地址。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set ipv6 vxlan-tunnel source 
  ＜ipv6-address 
＞
no set ipv6 vxlan-tunnel source 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|VXLAN隧道源IPv6地址，十六进制点分形式
缺省 : 
无 
使用说明 : 
1. route-map提供set ipv6 vxlan-tunnel source项，BGP通过此配置来修改VXLAN隧道的IPv6源地址。 
范例 : 
在route-map中配置set ipv6 vxlan-tunnel source：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set ipv6 vxlan-tunnel source 1::1
相关命令 : 
show route-map 
## set l2-vni-label equivalent-vni-label 

set l2-vni-label equivalent-vni-label 
命令功能 : 
设置二层VNI使用等价标签。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set l2-vni-label equivalent-vni-label 
 
no set l2-vni-label equivalent-vni-label 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
route-map提供设置二层VNI等价标签，BGP用来修改EVPN路由的二层VNI等价标签属性。 
范例 : 
配置二层VNI使用等价标签：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set l2-vni-label equivalent-vni-label
相关命令 : 
show route-map 
## set l2-vni-label 

set l2-vni-label 
命令功能 : 
设置二层VNI标签值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set l2-vni-label 
  ＜value of l2vni label 
＞
no set l2-vni-label 
命令参数解释 : 
参数|描述
---|---
＜value of l2vni label＞|标签值，范围：<1~16777215 >
缺省 : 
无 
使用说明 : 
1.route-map提供set l2-vni-label项，BGP用来修改EVPN路由的二层VNI标签属性。 
范例 : 
在route-map中配置l2-vni-label：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set l2-vni-label 16777215
相关命令 : 
show route-map 
## set l3-vni-label automatic 

set l3-vni-label automatic 
命令功能 : 
设置三层VNI自动获取标签。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set l3-vni-label automatic 
 
no set l3-vni-label automatic 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
route-map提供设置三层VNI自动获取标签，BGP用来自动获取EVPN路由的三层VNI标签。此命令与set l3-vni-label和set l3-vni-label equivalent-vni-label两两互斥。 
范例 : 
配置三层VNI自动获取标签：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set l3-vni-label automatic 
相关命令 : 
show route-map 
## set l3-vni-label equivalent-vni-label 

set l3-vni-label equivalent-vni-label 
命令功能 : 
设置三层VNI使用等价标签。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set l3-vni-label equivalent-vni-label 
 
no set l3-vni-label equivalent-vni-label 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
route-map提供设置三层VNI等价标签，BGP用来修改EVPN路由的三层VNI等价标签属性。 
范例 : 
配置三层VNI使用等价标签：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set l3-vni-label equivalent-vni-label
相关命令 : 
show route-map 
## set l3-vni-label 

set l3-vni-label 
命令功能 : 
设置三层VNI标签值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set l3-vni-label 
  ＜value of l3vni label 
＞
no set l3-vni-label 
命令参数解释 : 
参数|描述
---|---
＜value of l3vni label＞|标签值，范围：<0~16777215 >
缺省 : 
无 
使用说明 : 
1.    route-map提供set l3-vni-label项，BGP用来修改EVPN路由的三层VNI标签属性。 
范例 : 
在route-map中配置l3-vni-label：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)# set l3-vni-label 16777215
相关命令 : 
show route-map 
## set large-community 

set large-community 
命令功能 : 
设置大团体属性。使用no命令删除该属性。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set large-community 
  {none 
|{overwrite 
|additive 
|delete 
} ＜n:n:n 
＞}
no set large-community 
  [{overwrite 
|additive 
|delete 
} ＜n:n:n 
＞]
				
命令参数解释 : 
参数|描述
---|---
none|没有团队属性
overwrite|覆盖已有的large community
additive|添加到已有的large community
delete|删除一个存在的large community
＜n:n:n＞|large community值，n:n:n格式，范围：<0–4294967295>:<0–4294967295>:<0–4294967295>
缺省 : 
无 
使用说明 : 
使用场景：给BGP设置大团体属性。注意事项：1、同一个序列号内最多配置10个大团体号，且需要配置相同的操作类型。No命令不带参数，是删除当前序列号内所有的大团体号。
范例 : 
设置BGP大团体属性：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set large-community overwrite 1:1:1ZXROSNG(config-route-map)#
相关命令 : 
show route-map 
## set level 

set level 
命令功能 : 
当路由符合用于重分发的route-map的一个匹配项而可被分发时，使用本命令指定分发的层次。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set level 
  {level-1 
|level-2 
|level-1-2 
}
no set level 
命令参数解释 : 
参数|描述
---|---
level-1|分发层次
level-2|分发层次
level-1-2|分发层次
缺省 : 
无 
使用说明 : 
无 
范例 : 
指定分发的层次为level-1：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set level level-1
相关命令 : 
show route-map 
## set local-preference 

set local-preference 
命令功能 : 
为自治系统路径指定优先权值。使用no命令恢复缺省值。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set local-preference 
  [{+ 
|- 
}] ＜local-preference-value 
＞
no set local-preference 
命令参数解释 : 
参数|描述
---|---
+|表示加
-|表示减
＜local-preference-value＞|优先权值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
1、为自治系统路径指定优先权值为333：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set local-preference 3332、指定自治系统路径优先权值加上333：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set local-preference + 333
相关命令 : 
show route-map 
## set metric inherit 

set metric inherit 
命令功能 : 
设置继承路由原有的开销值。使用no命令恢复缺省状态。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set metric inherit 
 
no set metric inherit 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1、此命令与set ip metric，set ipv6 metric，set metric和set metric inherit-igp-metirc互斥。2、应用在BGP路由时：路由器从IBGP对等体学到的路由在通告给EBGP对等体时，如果配置此命令， 继承路由的原有开销值。
范例 : 
设置继承路由原有的开销值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set metric inherit
相关命令 : 
show route-map 
## set metric inherit-igp-metric 

set metric inherit-igp-metric 
命令功能 : 
设置继承IGP路由的开销值。使用no命令恢复缺省状态。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set metric inherit-igp-metric 
 
no set metric inherit-igp-metric 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1、此命令与set ip metric，set ipv6 metric，set metric和set metric inherit互斥。2、应用在BGP路由时：路由器从IBGP对等体学到的路由在通告给EBGP对等体时，如果配置此命令，则路由器会将向EBGP对等体通告的路由的MED值设置为该路由的下一跳的IGP开销值。
范例 : 
设置继承IGP路由的开销值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set metric inherit-igp-metric
相关命令 : 
show route-map 
## set metric 

set metric 
命令功能 : 
设置路由选择协议的开销值。使用no命令恢复缺省状态。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set metric 
  [{- 
|+ 
}] ＜metric-value 
＞
no set metric 
命令参数解释 : 
参数|描述
---|---
-|表示减
+|表示加
＜metric-value＞|开销值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
此命令与set ip metric，set ipv6 metric，set metric inherit和set metric inherit-igp-metirc互斥。 
范例 : 
设置路由选择协议的开销值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set metric + 1
相关命令 : 
show route-map 
## set monitor-group-id 

set monitor-group-id 
命令功能 : 
设置镜像ID 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set monitor-group-id 
  ＜id 
＞
no set monitor-group-id 
命令参数解释 : 
参数|描述
---|---
＜id＞|镜像ID值，范围1-63
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set monitor-group-id 1
相关命令 : 
show route-map
## set mpls-label equivalent-evi-label 

set mpls-label equivalent-evi-label 
命令功能 : 
配置EVI（EVPN Instance）等价标签标记，表示发布路由时取用EVI等价标签。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set mpls-label equivalent-evi-label 
 
no set mpls-label equivalent-evi-label 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令与set mpls-label evi-label互斥。 
范例 : 
1、在route-map中配置EVI等价标签：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set mpls-label equivalent-evi-labelZXROSNG(config-route-map)#no set mpls-label equivalent-evi-label
相关命令 : 
show route-map 
## set mpls-label evi-label 

set mpls-label evi-label 
命令功能 : 
配置EVI（EVPN Instance）标签值，表示发布路由时取用配置的EVI标签值。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set mpls-label evi-label 
  ＜value of evi label 
＞
no set mpls-label evi-label 
命令参数解释 : 
参数|描述
---|---
＜value of evi label＞|EVI标签值，范围：<16~1048575 >
缺省 : 
无 
使用说明 : 
此命令与set mpls-label equivalent-evi-label互斥。 
范例 : 
1、在route-map中配置EVI标签值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set mpls-label evi-label 1048575ZXROSNG(config-route-map)#no set mpls-label evi-label
相关命令 : 
show route-map 
## set mpls-label 

set mpls-label 
命令功能 : 
给匹配的路由配置发送标签的标志。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set mpls-label 
 
no set mpls-label 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
给匹配的路由配置发送标签的标志：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set mpls-label
相关命令 : 
 show route-map 
## set next-hop 

set next-hop 
命令功能 : 
指定下一跳的地址。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set next-hop 
  {peer-address 
|*(＜ipv4-address 
＞)}
no set next-hop 
  {peer-address 
|[*(＜ipv4-address 
＞)]}
				
命令参数解释 : 
参数|描述
---|---
peer-address|直连地址标识
＜ipv4-address＞|下一跳的IP地址，十进制点分形式，最多配置10个下一跳地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
指定下一跳的地址：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set next-hop 2.2.2.2
相关命令 : 
show route-map 
## set origin 

set origin 
命令功能 : 
设置BGP路由起源属性。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set origin 
  {igp 
|egp 
|incomplete 
}
no set origin 
命令参数解释 : 
参数|描述
---|---
igp|本地IGP
egp|远程EGP
incomplete|未知的残余项
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置BGP路由起源属性：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set origin egp
相关命令 : 
show route-map 
## set path-selection 

set path-selection 
命令功能 : 
BGP设置路径选择算法 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set path-selection 
  {all 
|backup 
|best-path 
|group-best 
} ＜Path numbers 
＞ {[install 
],[multipath-protect 
],[advertise 
]}
no set path-selection 
命令参数解释 : 
参数|描述
---|---
all|模拟iBGP full-mesh场景
backup|快速收敛场景
best-path|负荷分担场景
group-best|消除MED引起的路由震荡场景
＜Path numbers＞|路径数目
install|将选择出的路径下发转发表
multipath-protect|路径下发转发表的方式：n*active/ standby
advertise|将选择出的路径向外通告
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set path-selection backup 1 install
相关命令 : 
show route-map
## set policy-priority 

set policy-priority 
命令功能 : 
设置PBR策略优先级 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set policy-priority 
  ＜value of policy priority 
＞
no set policy-priority 
命令参数解释 : 
参数|描述
---|---
＜value of policy priority＞|策略优先级，取值范围<0-7>
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set policy-priority 1
相关命令 : 
show route-map 
## set policy-route-id 

set policy-route-id 
命令功能 : 
设置策略路由的ID值 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set policy-route-id 
  ＜id 
＞
no set policy-route-id 
命令参数解释 : 
参数|描述
---|---
＜id＞|policy-route-id的取值范围为1到63
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置策略路由的ID值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set policy-route-id 1
相关命令 : 
show route-map 
## set qos-id 

set qos-id 
命令功能 : 
设置路由的qos-id值，使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set qos-id 
  ＜qos-id 
＞
no set qos-id 
命令参数解释 : 
参数|描述
---|---
＜qos-id＞|qos-id 值，范围：1-16000
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置qos id：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set qos-id 2
相关命令 : 
show route-map 
## set split-horizon-scope 

set split-horizon-scope 
命令功能 : 
设置用于进行水平分割域的名称。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set split-horizon-scope 
  ＜scope-name 
＞
no set split-horizon-scope 
命令参数解释 : 
参数|描述
---|---
＜scope-name＞|域名称，长度为1个字符
缺省 : 
无 
使用说明 : 
1、水平分割域名称只支持配置一个字母，  支持配置字母集合为$#84018727#$个。  该个数对应的含义，举例说明如下：  1：不允许配置；  2：可以配置字母A、B中任意一个；  3：可以配置字母A、B、C中任意一个；  26：可以配置字母A~Z中任意一个。2、只能配置一个水平分割域。
范例 : 
配置用于水平分割的域名称列表：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set split-horizon-scope A
相关命令 : 
show route-map 
## set tag 

set tag 
命令功能 : 
设置目的路由选择协议的标记值。使用no命令取消设置。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set tag 
  ＜tag-value 
＞
no set tag 
命令参数解释 : 
参数|描述
---|---
＜tag-value＞|标记值，范围：0–4294967295
缺省 : 
无 
使用说明 : 
此命令与set ip tag和set ipv6 tag互斥。 
范例 : 
设置目的路由选择协议的标记值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set tag 210
相关命令 : 
show route-map 
## set traffic-index 

set traffic-index 
命令功能 : 
设置BGP流统计索引 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set traffic-index 
  ＜traffic-index number 
＞
no set traffic-index 
命令参数解释 : 
参数|描述
---|---
＜traffic-index number＞|流统计索引，取值范围<1-64>
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set traffic-index 5
相关命令 : 
show route-map
## set tunnel-encapsulation 

set tunnel-encapsulation 
命令功能 : 
BGP需要支持VXLAN和MPLS的EVPN共存，通过本命令配置BGP隧道封装类型为VXLAN或者MPLS。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set tunnel-encapsulation 
  {mpls 
|vxlan 
}
no set tunnel-encapsulation 
命令参数解释 : 
参数|描述
---|---
mpls|MPLS封装
vxlan|VXLAN封装
缺省 : 
无 
使用说明 : 
无 
范例 : 
指定隧道封装为mpls：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set tunnel-encapsulation mpls
相关命令 : 
show route-map 
## set urpf-id 

set urpf-id 
命令功能 : 
基于BGP neighbor的route-map里配置URPF ID属性。使用no命令恢复缺省状态。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set urpf-id 
  ＜urpf-id 
＞
no set urpf-id 
命令参数解释 : 
参数|描述
---|---
＜urpf-id＞|配置URPF ID属性，范围：1-65534
缺省 : 
无 
使用说明 : 
Route-map提供set urpf-id 项，在BGP的neighbor配置里应用route-map。 
范例 : 
设置路由选择协议的尺度值：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set urpf-id 1ZXROSNG(config-route-map)#no set urpf-id
相关命令 : 
show route-map 
## set vrf 

set vrf 
命令功能 : 
当数据包符合用于策略路由的路由映像的一个匹配项而可被策略路由时，使用本命令把数据包路由到指定VPN上。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
set vrf 
  ＜vrfname 
＞ [ip 
 next-hop 
 ＜vrf_nh 
＞ [track 
 ＜track-name 
＞]]
no set vrf 
命令参数解释 : 
参数|描述
---|---
＜vrfname＞|VRF名称，每次最多配置1个VRF
ip|ip地址
next-hop|下一跳
＜vrf_nh＞|下一跳IP地址，十进制点分形式
＜track-name＞|track 名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
把数据包路由到指定VPN上：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#set vrf name
相关命令 : 
show route-map 
## show ip as-path-access-list name 

show ip as-path-access-list name 
命令功能 : 
显示指定的自治系统路径访问表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip as-path-access-list name 
  ＜aspath-list-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜aspath-list-name＞|指定访问表名称，字符串长度范围：1–31
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示列表号名称为zte的自治系统路径访问表的内容：ZXROSNG# show ip as-path-access-list name zteRegular Expression Access List zte  permit  aaa111
相关命令 : 
无 
## show ip as-path-access-list standard 

show ip as-path-access-list standard 
命令功能 : 
显示指定的标准自治系统路径访问表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip as-path-access-list standard 
  [＜aspath-list-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜aspath-list-name＞|指定访问表名称，字符串长度范围：1–31
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示列表号名称为zte的自治系统路径访问表的内容：ZXROSNG#show ip as-path-access-list standard zteGlobal configuration:trigger delay: 10 secondsip as-path-list name(standard): zte  seq     as-number     count  4       65535.65535   255  65534   1.65535       255  65535   1.1           255显示信息说明：seq：序列号as-number：AS号count：AS路径重复次数
相关命令 : 
ip as-path access-list standard 
## show ip as-path-access-list 

show ip as-path-access-list 
命令功能 : 
显示全部或指定的正则表达式访问表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip as-path-access-list 
  [＜aspath-list-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜aspath-list-number＞|指定正则表达式访问表的号，范围：1–199
缺省 : 
无 
使用说明 : 
如果本命令不带参数，则显示所有的正则表达式访问表；如果带参数，则显示指定表号的正则表达式访问表。 
范例 : 
显示列表号为1的正则表达式访问表的内容：ZXROSNG# show ip as-path-access-list 1Regular Expression Access List 1  deny    123
相关命令 : 
无 
## show ip color-list 

show ip color-list 
命令功能 : 
显示配置的color列表内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip color-list 
  [＜color-list-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜color-list-name＞|指定color列表名称，字符串长度范围：1–31
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示color列表名称为zte的内容：ZXROSNG# show ip color-list zteGlobal configuration:trigger delay: 10 secondsip color-list name: zte   22233   5556666
相关命令 : 
ip color-list 
## show ip community-list name 

show ip community-list name 
命令功能 : 
显示指定名字的团体表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip community-list name 
  ＜Community-list name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜Community-list name＞|用英文指定团体表的号，长度范围：1–31
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示名字为zte的团体表的内容：ZXROSNG(config)#show ip community-list name zteBasic Community List zteip community-list zte permit 1:1
相关命令 : 
无 
## show ip community-list 

show ip community-list 
命令功能 : 
显示全部或指定的团体表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip community-list 
  [＜community-list-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜community-list-number＞|指定团体表的号，范围：1–499
缺省 : 
无 
使用说明 : 
如果本命令不带参数，则显示所有的团体表；如果带参数，则显示指表号的团体表。
范例 : 
显示列表号为1的团体表的内容：ZXROSNG(config)#show ip community-list 1Standard Community List 1ip community-list 1 deny   10 15ip community-list 1 deny   5 10ip community-list 1 permit  any
相关命令 : 
无 
## show ip extcommunity-list name 

show ip extcommunity-list name 
命令功能 : 
显示指定名字的扩展团体表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip extcommunity-list name 
  ＜extcommunity-list-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜extcommunity-list-name＞|用英文指定扩展团体表的号，长度范围：1–31
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示名字为zte的扩展团体表的内容：ZXROSNG(config)#show ip extcommunity-list name zteBasic Community List zteip extcommunity-list zte permit general-asn 1:1
相关命令 : 
ip extcommunity-list 
## show ip extcommunity-list 

show ip extcommunity-list 
命令功能 : 
显示全部或指定的扩展团体表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip extcommunity-list 
  [＜extend-community-list-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜extend-community-list-number＞|扩展团体表名，范围：1-500
缺省 : 
无 
使用说明 : 
如果本命令不带参数，则显示所有的扩展团体表；如果带参数，则显示指表号的扩展团体表。
范例 : 
显示所有扩展团体表的内容：ZXROSNG(config)#show ip extcommunity-listExtended Community List 400ip extcommunity-list 400 deny  zte
相关命令 : 
无 
## show ip large-community-list 

show ip large-community-list 
命令功能 : 
显示全部或指定的大团体表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip large-community-list 
  [name 
 ＜large-community-list-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜large-community-list-name＞|指定大团体表的名称，长度范围：1–31
缺省 : 
无 
使用说明 : 
使用场景：显示全部或指定的大团体表的内容。注意事项：如果本命令不带参数，则显示所有的大团体表；如果带参数，则显示指定的大团体表。
范例 : 
显示列表名为a的大团体表的内容：ZXROSNG#show ip large-community-list name aGlobal configuration:trigger delay: 30 secondsLarge Community List aseq 1          permit 1:1:1seq 1          permit 1:1:2seq 1          permit 1:1:3seq 1          permit 1:1:4seq 1          permit 1:1:5seq 1          permit 1:1:6seq 1          permit 1:1:7seq 1          permit 1:1:8seq 1          permit 1:1:9seq 1          permit 1:1:10  seq 2          permit 1:1:11seq 2          permit 1:1:13seq 2          permit 1:1:14seq 2          permit 1:1:15seq 2          permit 1:1:16seq 2          permit 1:1:17
相关命令 : 
ip large-community-listip large-community-list trigger-delay
## show route-map 

show route-map 
命令功能 : 
显示route-map配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show route-map 
  [＜routemap-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜routemap-name＞|指定的路由映射的名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示route-map的配置信息：ZXROSNG(config-route-map)#show route-map [route-map zte] IP type: IPv6route-map zte permit 10  match ipv6 next-hop zxr10zte  match ipv6 address ipv6address  match ipv6 metric 10 20  match ipv6 tag 0  set ipv6 next-hop 1:1:0:0:0:0:2:3  set level level-1  set origin egp  set mpls-label    set extcommunity soo-trans 65535:1  set extcommunity rt-trans 192.168.20.110:0  set ipv6 metric-type external  set ipv6 metric + 20  set ipv6 tag 2
相关命令 : 
无 
## time-range 

time-range 
命令功能 : 
使用本命令在route-map的序列中配置时间列表。Route-map的序列中配置了时间列表之后，该序列的有效性由配置的时间列表控制。 
命令模式 : 
 路由映射模式  
命令默认权限级别 : 
15 
命令格式 : 
time-range 
  ＜Time range name 
＞
no time-range 
命令参数解释 : 
参数|描述
---|---
＜Time range name＞|时间列表名称，长度1-31字符
缺省 : 
无 
使用说明 : 
1在route-rmap的序列中配置time-range时，需要该time-range已经存在。2 Route-map的一个序列中配置time-range后，该序列的有效性由配置的时间列表控制。
范例 : 
在route-map中配置时间列表：ZXROSNG(config)#route-map zteZXROSNG(config-route-map)#time-range abc
相关命令 : 
show route-map 
# Time-range配置命令 
## absolute 

absolute 
命令功能 : 
该命令工作于TimeRange配置模式，用于配置绝对时间段。 
命令模式 : 
 TimeRange模式  
命令默认权限级别 : 
15 
命令格式 : 
absolute 
  {[start 
 ＜start-time 
＞ ＜start-date 
＞],[end 
 ＜end-time 
＞ ＜end-date 
＞]}
no absolute 
命令参数解释 : 
参数|描述
---|---
＜start-time＞|绝对时间段的开始时间，格式为hh:mm:ss，秒数必须是15的倍数，默认值：无。
＜start-date＞|绝对时间段的开始日期，格式为：mm-dd-yyyy，year范围：2001-2037，默认值：无。
＜end-time＞|绝对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数，默认值：无。
＜end-date＞|绝对时间段的结束日期，格式为：mm-dd-yyyy，year范围：2001-2037，默认值：无。
缺省 : 
无 
使用说明 : 
进入TimeRange配置模式才能配置时间段，时间日期的格式为：小时：分：秒 月-日-年，最小时间2001-01-01 00：00。秒数必须是15的倍数。一个TimeRange列表中只能有一个绝对时间段。绝对时间段定义了整个列表的生效时间区间，只有绝对时间有效时才检查相对时间段。在time-range disable状态下所有的TimeRange列表不再起作用。不再随时间进行状态转换，而是处于time-range disable时的状态。使用no absolute命令删除绝对时间段。
范例 : 
ZXROSNG(config)#time-range mytime ZXROSNG(config-tr-mytime)#absolute start 01:00:00 01-09-2012 end 01:00:00 01-10-2012
相关命令 : 
show time-rangetime-range <time-range-name>
## debug time-range 

debug time-range 
命令功能 : 
该命令工作于特权模式，用于打开TimeRange列表状态发生转换时的debug开关。打开TimeRange的debug开关后，当TimeRange列表状态发生转换时，在命令终端上自动显示信息提示用户，显示的debug信息包括系统时间、TimeRange的名字、之前状态、转换后的状态等。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug time-range 
  [change-to 
 {active 
|inactive 
}]
no debug time-range 
命令参数解释 : 
参数|描述
---|---
active|只打开状态从inactive转为active的TimeRange列表的debug开关。
inactive|只打开状态从active转为inactive的TimeRange列表的debug开关。
缺省 : 
输出所有状态的TimeRange列表。 
使用说明 : 
TimeRange列表状态包括inactive状态和active状态。默认打开所有状态的TimeRange列表的debug开关。
范例 : 
ZXROSNG#debug time-range change-to inactive TIME-RANGE inactive debugging has been turned on
相关命令 : 
show debug time-range 
## periodic 

periodic 
命令功能 : 
该命令工作于TimeRange配置模式，用于配置相对时间段。一个TimeRange列表中可以配置多个相对时间段。 
命令模式 : 
 TimeRange模式  
命令默认权限级别 : 
15 
命令格式 : 
periodic 
  {monday 
 ＜start-time 
＞ to 
 [＜days-after-monday 
＞] ＜end-time 
＞|tuesday 
 ＜start-time 
＞ to 
 [＜days-after-tuesday 
＞] ＜end-time 
＞|wednesday 
 ＜start-time 
＞ to 
 [＜days-after-wednesday 
＞] ＜end-time 
＞|thursday 
 ＜start-time 
＞ to 
 [{thursday 
|friday 
|saturday 
|sunday 
}] ＜end-time 
＞|friday 
 ＜start-time 
＞ to 
 [{friday 
|saturday 
|sunday 
}] ＜end-time 
＞|saturday 
 ＜start-time 
＞ to 
 [{saturday 
|sunday 
}] ＜end-time 
＞|sunday 
 ＜start-time 
＞ to 
 [sunday 
] ＜end-time 
＞|weekend 
 ＜start-time 
＞ to 
 ＜end-time 
＞|daily 
 ＜start-time 
＞ to 
 ＜end-time 
＞|weekdays 
 ＜start-time 
＞ to 
 ＜end-time 
＞}
no periodic 
  {monday 
 ＜start-time 
＞ to 
 [＜days-after-monday 
＞] ＜end-time 
＞|tuesday 
 ＜start-time 
＞ to 
 [＜days-after-tuesday 
＞] ＜end-time 
＞|wednesday 
 ＜start-time 
＞ to 
 [＜days-after-wednesday 
＞] ＜end-time 
＞|thursday 
 ＜start-time 
＞ to 
 [{thursday 
|friday 
|saturday 
|sunday 
}] ＜end-time 
＞|friday 
 ＜start-time 
＞ to 
 [{friday 
|saturday 
|sunday 
}] ＜end-time 
＞|saturday 
 ＜start-time 
＞ to 
 [{saturday 
|sunday 
}] ＜end-time 
＞|sunday 
 ＜start-time 
＞ to 
 [sunday 
] ＜end-time 
＞|weekend 
 ＜start-time 
＞ to 
 ＜end-time 
＞|daily 
 ＜start-time 
＞ to 
 ＜end-time 
＞|weekdays 
 ＜start-time 
＞ to 
 ＜end-time 
＞}
				
命令参数解释 : 
参数|描述
---|---
monday|星期一
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
＜days-after-monday＞|可以是周一、周二、周三、周四、周五、周六、周日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
tuesday|星期二
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
＜days-after-tuesday＞|可以是周二、周三、周四、周五、周六、周日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
wednesday|星期三
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
＜days-after-wednesday＞|可以是周三、周四、周五、周六、周日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
thursday|星期四
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
thursday|星期四
friday|星期五
saturday|星期六
sunday|星期日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
friday|星期五
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
friday|星期五
saturday|星期六
sunday|星期日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
saturday|星期六
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
saturday|星期六
sunday|星期日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
sunday|星期日
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
sunday|星期日
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
weekend|周末
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
daily|每日
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
weekdays|工作日
＜start-time＞|相对时间段的开始时间，格式为：hh:mm:ss，秒数必须是15的倍数
＜end-time＞|相对时间段的结束时间，格式为：hh:mm:ss，秒数可以是59，或者是15的倍数
缺省 : 
无 
使用说明 : 
进入TimeRange配置模式才能配置时间段，配置完成后，可以使用show time-range查看已配置的时间段。使用no periodic命令删除相对时间段。
范例 : 
ZXROSNG(config)#time-range mytimeZXROSNG(config-tr-mytime)#periodic monday 8:30:00 to friday 17:40:00
相关命令 : 
show time-rangetime-range <time-range-name>
## show debug time-range 

show debug time-range 
命令功能 : 
该命令工作于用户模式外的其它所有模式，用于显示状态发生转换时的TimeRange列表。TimeRange列表状态发生转换是指TimeRange列表状态由inactive转换为active或由active转换为inactive：假设配置mytimerange列表的时间段为周一00：00：00到01：01：01，那么在系统时间进入该时间段时，mytimerange列表的状态由inactive转换为active，系统时间不在该时间段时mytimerange列表的状态就由active转换为inactive。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug time-range 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示TimeRange状态发生转换时的TimeRange列表，TimeRange状态有：active、inactive。 
范例 : 
ZXROSNG(config)#show debug time-range TIMERANGE:  Time-range state debugging is on, print out switching to active only  debug time-range [change-to {inactive|active}]
相关命令 : 
无 
## show time-range 

show time-range 
命令功能 : 
该命令工作于用户模式外的其它所有模式，用于显示指定或者显示全部TimeRange列表。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show time-range 
  [＜time-range-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜time-range-name＞|时间段的名字，支持1-31个字符
缺省 : 
无 
使用说明 : 
  进入TimeRange配置模式才能配置时间段，时间日期的格式为：小时：分：秒 月-日-年，最小时间2001-01-01 00：00。秒数必须是15的倍数。  一个TimeRange列表中只能有一个绝对时间段。绝对时间段定义了整个列表的生效时间区间，只有绝对时间有效时才检查相对时间段。   在time-range disable状态下所有的TimeRange列表不再起作用。不再随时间进行状态转换，而是处于time-range disable时的状态。  使用no absolute命令删除绝对时间段。
范例 : 
显示全部TimeRange列表：ZXROSNG#show time-range Current time is 00:19:04 01-09-2012 Mondaytime-range mytime <inactive>   absolute start 01:00:00 01-09-2012 end 01:00:00 01-10-2012 
time-range mytime1 <active> 显示特定TimeRange列表 mytime：ZXROSNG#show time-range mytimeCurrent time is 00:19:40 01-09-2012 Mondaytime-range mytime <inactive>   absolute start 01:00:00 01-09-2012 end 01:00:00 01-10-2012 
相关命令 : 
无 
## time-range disable clear 

time-range disable clear 
命令功能 : 
该命令工作于全局配置模式，用于关闭TimeRange时间段功能，并清除TimeRange相关配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
time-range disable clear 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    TimeRange时间段功能默认关闭。    开启TimeRange时间段功能的命令为time-range enable。 
范例 : 
ZXROSNG(config)#time-range disable clear  
相关命令 : 
time-range enabletime-range disable
## time-range disable 

time-range disable 
命令功能 : 
该命令工作于全局配置模式，用于关闭TimeRange时间段功能。time-range disable命令只关闭TimeRange时间段功能，不清除TimeRange相关配置。TimeRange时间段功能关闭后，TimeRange列表的状态不会随着时间而改变，一直保持关闭前状态。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
time-range disable 
 
命令参数解释 : 
					无
				 
缺省 : 
TimeRange功能不开启。 
使用说明 : 
    TimeRange时间段功能默认为关闭状态。    开启TimeRange时间段功能的命令为time-range enable。 
范例 : 
ZXROSNG(config)#time-range disable 
相关命令 : 
time-range enable 
## time-range enable 

time-range enable 
命令功能 : 
该命令工作于全局配置模式，用于开启TimeRange时间段功能。开启时间段功能后才能进行时间段相关配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
time-range enable 
 
命令参数解释 : 
					无
				 
缺省 : 
TimeRange功能不开启。 
使用说明 : 
    TimeRange时间段功能开启后，才能通过time-range命令进入TimeRange配置模式进行Timerange相关配置：time-rangabsoluteperiodic    TimeRange时间段功能默认不开启。    关闭TimeRange时间段功能的命令为time-range disable或者time-range disable clear。
范例 : 
ZXROSNG(config)#time-range enableZXROSNG(config)#
相关命令 : 
time-range disabletime-range disable clear
## time-range 

time-range 
命令功能 : 
该命令工作于全局配置模式，用于进入TimeRange配置模式并创建TimeRange列表。若TimeRange列表已经存在则只进入TimeRange配置模式。使用no命令删除配置的TimeRange列表。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
time-range 
  ＜time-range-name 
＞
no time-range 
  ＜time-range-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜time-range-name＞|时间段的名字，支持1-31个字符
缺省 : 
无 
使用说明 : 
系统支持的最大TimeRange列表数为2048个，一个TimeRange列表中最多包含24条时间段，包括绝对时间段和相对时间段，其中最多只能有一条绝对时间段。时间段在以下三种情况下能够生效。只配置了绝对时间段。当前系统时间在配置的绝对时间段内，则该时间段有效。只配置了相对时间段。无论配置了几个相对时间段，只要当前系统时间在任何一个相对时间段，则该时间段有效。既配置了绝对时间段，又配置了相对时间段。系统时间必须同时符合绝对时间段及其中一个相对时间段，才能认为该时间段有效。在time-range disable状态下所有的TimeRange列表不再起作用。不再随时间进行状态转换，而是处于time-range disable时的状态。
范例 : 
创建名称为mytime的TimeRange列表：ZXROSNG(config)#time-range mytimeZXROSNG(config-tr-mytime)#
相关命令 : 
show time-range 
# 前缀列表配置命令 
## ip prefix-list 

ip prefix-list 
命令功能 : 
给BGP创建一个前缀表且控制对它的访问。使用no命令删除前缀表。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip prefix-list 
  ＜prefix-list-name 
＞ {description 
 ＜prefix-list-description 
＞|[seq 
 ＜prefix-list-sequence 
＞] [{deny 
|permit 
}] ＜ipv4-address 
＞ ＜mask-length 
＞ [ge 
 ＜lesser-mask-length 
＞] [le 
 ＜greater-mask-length 
＞]}
no ip prefix-list 
  ＜prefix-list-name 
＞ [{seq 
 ＜prefix-list-sequence 
＞|[{deny 
|permit 
}] ＜ipv4-address 
＞ ＜mask-length 
＞ [ge 
 ＜lesser-mask-length 
＞] [le 
 ＜greater-mask-length 
＞]|description 
}]
				
命令参数解释 : 
参数|描述
---|---
＜prefix-list-name＞|标识一个前缀表，长度1–31个字符
description|允许指定前缀表的描述
＜prefix-list-description＞|指定前缀表的描述，长度1–79个字符
＜prefix-list-sequence＞|允许指定在前缀表中的位置，标识在前缀表中的位置，范围：1–4294967294
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜ipv4-address＞|匹配的32位前缀地址
＜mask-length＞|匹配的前缀掩码，范围：0–32
＜lesser-mask-length＞|掩码，范围：1–32
＜greater-mask-length＞|掩码，范围：1–32
缺省 : 
未定义前缀列表。 
使用说明 : 
不配置{deny|permit}选项的话，默认是permit操作。 
范例 : 
指定前缀列表test的描述信息为“test”并指定允许地址为100.1.1.1掩码范围为大于等于25的路由：ZXROSNG(config)#ip prefix-list test seq  1 permit 100.1.1.1 24 ge 25ZXROSNG(config)#ip prefix-list test description test
相关命令 : 
show ip prefix-list 
## ipv6 prefix-list 

ipv6 prefix-list 
命令功能 : 
给业务创建一个IPv6前缀表且控制对它的访问。使用no命令删除前缀表。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 prefix-list 
  ＜pflname 
＞ {description 
 ＜txt 
＞|[seq 
 ＜pflno 
＞] [{deny 
|permit 
}] ＜UDP_SrcAddr 
＞ [ge 
 ＜ge_len 
＞] [le 
 ＜le_len 
＞]}
no ipv6 prefix-list 
  ＜pflname 
＞ [{seq 
 ＜pflno 
＞|[{deny 
|permit 
}] ＜UDP_SrcAddr 
＞ [ge 
 ＜ge_len 
＞] [le 
 ＜le_len 
＞]|description 
}]
				
命令参数解释 : 
参数|描述
---|---
＜pflname＞|标识一个前缀表，长度1–31个字符
description|允许指定前缀表的描述
＜txt＞|指定前缀表的描述
＜pflno＞|允许指定在前缀表中的位置，标识在前缀表中的位置，范围：1–4294967294
deny|不允许对匹配条件进行访问
permit|允许对匹配条件进行访问
＜UDP_SrcAddr＞|IPv6地址，采用<X:X::X:X/0-128>形式
＜ge_len＞|允许指定掩码范围条件， 大于等于某一指定值
＜le_len＞|允许指定掩码范围条件 ，小于等于某一指定值
缺省 : 
未定义前缀列表。 
使用说明 : 
不配置{deny|permit}选项的话，默认是permit操作。 
范例 : 
指定前缀列表test的描述信息为“test”并指定允许地址为1:2::3:4掩码范围为大于等于127的路由：ZXROSNG(config)#ipv6 prefix-list test permit 1:2::3:4/126 ge 127ZXROSNG(config)#ipv6 prefix-list test description test
相关命令 : 
show ipv6 prefix-list 
## show ip prefix-list 

show ip prefix-list 
命令功能 : 
显示全部或指定的前缀表的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip prefix-list 
  [{detail 
|summary 
}] [＜prefix-list-name 
＞] 
命令参数解释 : 
参数|描述
---|---
detail|指定显示详细信息
summary|指定显示统计信息
＜prefix-list-name＞|指定前缀表的名称，长度1–31字符
缺省 : 
无 
使用说明 : 
如果不带< prefix-list-name >参数，则显示所有的前缀表。如果带< prefix-list-name >参数，则显示指定名称的前缀表。
范例 : 
显示所有前缀表的内容：ZXROSNG#show ip prefix-listtotal numbers of ip prefix-list: 4 seq entries, 1 range entriesip prefix-list multi :seq 5 permit 230.0.0.0 24ip prefix-list ly :seq 1 permit 229.0.0.0 24ip prefix-list test :description: testseq 1 permit 100.1.1.0 24 ge 25seq 6 permit 100.1.1.0 24
相关命令 : 
无 
## show ipv6 prefix-list 

show ipv6 prefix-list 
命令功能 : 
显示全部或指定的前缀表的内容 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ipv6 prefix-list 
  [{detail 
|summary 
}] [＜pflname 
＞] 
命令参数解释 : 
参数|描述
---|---
detail|指定显示详细信息
summary|指定显示统计信息
＜pflname＞|指定前缀表的名称，长度1–31字符
缺省 : 
无 
使用说明 : 
如果不带< prefix-list-name >参数，则显示所有的前缀表。如果带< prefix-list-name >参数，则显示指定名称的前缀表。
范例 : 
显示所有前缀表的内容：ZXROSNG(config)#show ipv6 prefix-list                                            total numbers of ip prefix-list: 4 seq entries, 2 range entriesipv6 prefix-list 2 :    seq 5 deny 2::2/128ipv6 prefix-list 1 :    seq 5 permit 1::1/1    seq 10 permit 1::1/1 ge 2 le 3ipv6 prefix-list test :description: test    seq 5 permit 1:2::3:4/126 ge 127
相关命令 : 
ipv6 prefix-list 
