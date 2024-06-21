# FTP配置命令 
## copy ftp 

copy ftp 
命令功能 : 
该命令工作于特权模式，当使用FTP 客户端功能时，使用此命令用于文件的传输。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
copy ftp 
  [vrf 
 ＜vrf-name 
＞] {root: 
 ＜source-filename 
＞ [＜CPU node information 
＞] {＜//host/file@username:password 
＞|{＜remote-ipv4-address 
＞|＜remote-ipv6-address 
＞} username 
 ＜username 
＞ path 
 ＜filepath 
＞}|{＜//host/file@username:password 
＞|{＜remote-ipv4-address 
＞|＜remote-ipv6-address 
＞} username 
 ＜username 
＞ path 
 ＜filepath 
＞} root: 
 ＜destination-filename 
＞ [＜CPU node information 
＞]} [＜listen-port 
＞] [{＜local-ipv4-address 
＞|＜local-ipv6-address 
＞}] [interface 
 ＜interface-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|虚拟路由（VRF）名称。如VRF 名称为mng表示选择管理口。 取值范围： 1–32位的字符串，可通过命令show ip vrf brief 查询。 默认值：无
＜source-filename＞|FTP客户端的文件名或文件路径及文件名。用于上传操作。 取值范围：纯文件名为1-79位的字符串，当不设置路径时，默认取当前路径作为此文件所在路径，全路径为1-159位的字符串。 默认值：无。
＜CPU node information＞|用于指定操作文件的cpu信息，仅在输入的路径为绝对路径时有效，输入的路径为相对路径时不需要输入该参数。
＜//host/file@username:password＞|FTP服务端文件路径。用户下载操作。取值范围：连同用户名及密码，合计1-230位的字符串，格式：//host/file@username:password。 默认值：无
＜remote-ipv4-address＞|FTP服务端IPv4地址。
＜remote-ipv6-address＞|FTP服务端IPv6地址。
＜username＞|FTP用户名。为1-65位的字符串。
＜filepath＞|FTP文件路径，全路径为1-159位的字符串。
＜//host/file@username:password＞|FTP服务端文件路径。用户下载操作。取值范围：连同用户名及密码，合计1-230位的字符串，格式：//host/file@username:password。 默认值：无
＜remote-ipv4-address＞|FTP服务端IPv4地址。
＜remote-ipv6-address＞|FTP服务端IPv6地址。
＜username＞|FTP用户名。为1-65位的字符串。
＜filepath＞|FTP文件路径，全路径为1-159位的字符串。
＜destination-filename＞|FTP客户端的文件名或文件路径及文件名。用于下载操作。 取值范围：纯文件名为1-79位的字符串，当不设置路径时，默认取当前路径作为此文件所在路径，全路径为1-159位的字符串。 默认值：无。
＜CPU node information＞|用于指定操作文件的cpu信息，仅在输入的路径为绝对路径时有效，输入的路径为相对路径时不需要输入该参数。
＜listen-port＞|侦听端口，与FTP服务器端开启的侦听端口号保持一致，否者建链失败。 取值范围：1-65535 默认值：21
＜local-ipv4-address＞|与local-ipv6-address为二选一，若为local-ipv4-address，表示本端为IPv4地址 默认值：无
＜local-ipv6-address＞|与local-ipv4-address为二选一，若为local-ipv6-address，表示本端为IPv6地址 默认值：无
interface|接口标识
＜interface-name＞|接口名称。当配置地址（本端或对端地址）为link-local地址时，需要指定此地址的出接口，可通过show ip interface brief查询对应接口。 默认值：无
缺省 : 
缺省情况下，监听端口号为21，本端IP地址自动获取，不配置接口名。 
使用说明 : 
1.使用前需要保证FTP客户端和FTP服务端通信能够互ping通。2.该命令支持文件的上传和下载操作，必须指定本端和对端的文件名，要连接的FTP服务器的IP地址，用户名和密码。 FTP服务器的端口号和本地地址为可选，如果不指定端口号，则默认连接FTP服务器的知名端口号21，本地地址则由ftp-client source-ip中指定的为准，如果此命令也未配置，则由TCP分配。3、如果采用copy ftp root: ＜source-filename＞ ＜remote-ipv4-address＞|＜remote-ipv6-address＞ username ＜username＞ path ＜filepath＞ 命令格式上传，或 copy ftp  ＜remote-ipv4-address＞|＜remote-ipv6-address＞ username ＜username＞ path ＜filepath＞ root: ＜source-filename＞ 命令格式下载，则该命令为动态交互命令，需要用户输入FTP用户的密码。4、使用动态交互方式输入命令时，如果要在命令最后输入可选参数＜local-ipv4-address＞或＜local-ipv6-address＞，则可选参数的类型必须和前面输入的IP地址类型匹配。即远端地址使用IPv4地址＜remote-ipv4-address＞的话，如果有可选参数，则可选参数必须使用IPv4地址＜local-ipv4-address＞；远端地址使用IPv6地址＜remote-ipv6-address＞的话，可选参数则必须使用IPv6地址＜local-ipv6-address＞。
范例 : 
1.从FLASH的datadisk0目录下将文件db.dat拷到主机168.1.1.1的FTP用户zxr10的工作目录上：ZXROSNG#copy ftp root: /datadisk0/db.dat //168.1.1.1/db.dat@zxr10:zxr10Connect successfully! Start copying file14% completed  00:00:20 ETA2，从主机168.1.1.1的FTP用户zxr10的工作目录上将文件db.dat拷到路由器的根目录上：ZXROSNG#copy ftp //168.1.1.1/db.dat@zxr10:zxr10 root: db.datConnect successfully! Start copying file16% completed  00:00:10 ETA3.从主机168.1.1.1的FTP用户zxr10的工作目录上将文件db.dat拷到路由器MPU-0/5/0的datadisk0目录上：ZXROSNG#copy ftp //168.1.1.1/db.dat@zxr10:zxr10 root:  /datadisk0/db.dat MPU-0/5/0Connect successfully! Start copying file100% completed  00:00:20Got file successfully! Received 1817833 bytes!4.从主机168.1.1.1的FTP用户zxr10的工作目录上将文件db.dat拷到路由器MPU-0/5/0的datadisk0目录上，并且使用SSl策略进行加密传输：ZXROSNG#copy ftp //168.1.1.1/db.dat@zxr10:zxr10 root:  /datadisk0/db.dat MPU-0/5/0 ssl-policy zteConnect successfully! Start copying file14% completedd  00:00:20 ETA5、使用动态交互的方式从主机192.168.100.250的FTP用户zte的工作目录上将文件a.dat拷到路由器的根目录上db.dat文件中：ZXROSNG#copy ftp vrf mng root: a.dat 192.168.100.250 username zte path db.datPassword required for zte.Enter password: ***Connect successfully! Start copying file100% completed  00:00:00Put file successfully! Sent 411 bytes!6、使用动态交互的方式从路由器的根目录上将文件db.dat拷到主机192.168.100.250的FTP用户zte的工作目录上a.dat文件中：ZXROSNG#copy ftp vrf mng 192.168.100.250 username zte path db.dat root: a.datPassword required for zte.Enter password: ***Connect successfully! Start copying file100% completed  00:00:00Got file successfully! Received 411 bytes!域信息：Connect successfully! Start copying file：提示信息，连接成功，开始拷贝100% completed：拷贝文件进度为100%00:00:20：拷贝文件用的总时间。时：分：秒的形式00:00:20 ETA：拷贝过程中显示，预计20秒后拷贝完成。Got file successfully! Received 1817833 bytes!：拷贝文件结束提示信息。下载文件成功，1817833是接收到文件的字节数。
相关命令 : 
copy tftpcopy sftp
## debug ftp 

debug ftp 
命令功能 : 
开启FTP debug 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ftp 
  {all 
|event 
|error 
|packet 
|detail 
}
no debug ftp 
  {all 
|event 
|error 
|packet 
|detail 
}
				
命令参数解释 : 
参数|描述
---|---
all|FTP所有打印
event|FTP SSL事件打印
error|FTP SSL错误打印
packet|FTP SSL报文打印
detail|FTP SSL详细打印
缺省 : 
无 
使用说明 : 
无 
范例 : 
打开FTP所有debug打印ZXROSNG#debug ftp allAll FTP SSL debugging has been turned on
相关命令 : 
no debug all 
## ftp-client source-interface 

ftp-client source-interface 
命令功能 : 
配置设备作为FTP客户端时的源接口。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-client source-interface 
  ＜interface-name 
＞
no ftp-client source-interface 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|源接口名称，1-31个字符。
缺省 : 
默认情况下没有配置FTP客户端源接口。 
使用说明 : 
1.执行该命令指定源接口后，FTP客户端发起建链时使用该接口的主地址（IPv4或IPv6主地址）作为本端地址；2.FTP客户端源地址的选取顺序依次是：copy ftp命令、ftp-client source-interface和ftp-client source-ip，即：1）如果copy ftp命令指定了源地址，则copy ftp命令发起的连接优先取本命令指定的源地址，若copy ftp命令中地址为linklocal地址，且只指定了接口未指定本端源地址，则获取此接口地址作为本端源地址；2）如果ftp-client source-interface与ftp-client source-ip同时配置，则本端发起的FTP连接优先取源接口的地址，如果源接口无效，则取配置的源地址；3.使用no命令取消配置的源接口。
范例 : 
配置设备作为FTP客户端时的监听接口：ZXROSNG(config)#ftp-client source-interface gei-0/1/0/1
相关命令 : 
ftp-client source-ipcopy ftpshow running-config ftp
## ftp-client source-ip 

ftp-client source-ip 
命令功能 : 
该命令工作于全局配置模式，当使用FTP客户端时传输文件时（包括上传和下载文件操作），用于配置文件传输的源地址。no ftp-client source-ip命令用于删除FTP客户端源地址。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-client source-ip 
  {ipv4 
 ＜ipv4-address 
＞|ipv6 
 ＜ipv6-address 
＞ [interface 
 ＜interface-name 
＞]}
no ftp-client source-ip 
  {ipv4 
|ipv6 
}
				
命令参数解释 : 
参数|描述
---|---
ipv4|IPv4标识
＜ipv4-address＞|IPv4类型源地址，默认值：无。
ipv6|IPv6标识
＜ipv6-address＞|IPv6类型源地址，默认值：无。
interface|接口标识
＜interface-name＞|接口名称，当指定的源地址为IPv6地址，且为link-local地址时，需要指定此接口名。 取值范围：1-32位的字符串。可通过命令show ip interface brief查询接口名。默认值：无。
缺省 : 
默认不配置源地址。 
使用说明 : 
1.可以配置IPv4和IPv6类型的源地址。2.当需要执行 copy ftp命令时， 若copy ftp命令未指定源地址，则采用该命令中配置的源地址。
范例 : 
配置设备作为ftp客户端时，copy的源地址,IPV4格式：ZXROSNG(config)#ftp-client source-ip ipv4 10.42.50.100 配置设备作为ftp客户端时，copy的源地址,IPV6格式：ZXROSNG(config)#ftp-client source-ip ipv6 100::1  
相关命令 : 
show running-config 
## ftp-secure-server mode 

ftp-secure-server mode 
命令功能 : 
配置FTPS服务端的模式和监听端口号，no命令恢复缺省值。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-secure-server mode 
  {all 
 [{[explicit-port 
 {＜explicit-default-port 
＞|＜explicit-optional-port 
＞}],[implicit-port 
 {＜implicit-default-port 
＞|＜implicit-optional-port 
＞}]}]|explicit 
 [explicit-port 
 {＜explicit-default-port 
＞|＜explicit-optional-port 
＞}]|implicit 
 [implicit-port 
 {＜implicit-default-port 
＞|＜implicit-optional-port 
＞}]}
no ftp-secure-server mode 
命令参数解释 : 
参数|描述
---|---
all|显式模式和隐式模式
＜explicit-default-port＞|显式模式的默认监听端口号，默认为21
＜explicit-optional-port＞|显式模式的可选监听端口号，范围 [21,1025-20000]；
＜implicit-default-port＞|隐式模式的默认监听端口号，默认为990
＜implicit-optional-port＞|隐式模式的可选监听端口号，范围 [990,1025-20000]；
explicit|显式模式
＜explicit-default-port＞|显式模式的默认监听端口号，默认为21
＜explicit-optional-port＞|显式模式的可选监听端口号，范围 [21,1025-20000]；
implicit|隐式模式
＜implicit-default-port＞|隐式模式的默认监听端口号，默认为990
＜implicit-optional-port＞|隐式模式的可选监听端口号，范围 [990,1025-20000]；
缺省 : 
默认FTPS服务端显式和隐式模式同时支持。no命令恢复缺省值。
使用说明 : 
1. 修改服务端模式或监听端口号，必须先去使能FTPS服务； 
范例 : 
1.使能FTPS服务，模式为隐式，端口号为5000： ZXROSNG(config)#ftp-secure-server  mode implicit implicit-port 5000
相关命令 : 
ftp-secure-server modeftp-secure-server ssl-context
## ftp-secure-server ssl-context 

ftp-secure-server ssl-context 
命令功能 : 
配置FTPS服务器所使用的SSL策略和PKI证书模板，no命令恢复缺省值。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-secure-server ssl-context 
  ＜context-name 
＞ [pki-profile 
 ＜profile-name 
＞]
no ftp-secure-server ssl-context 
命令参数解释 : 
参数|描述
---|---
＜context-name＞|SSL策略名称，1-31个字符。
＜profile-name＞|PKI证书模板名称，1-63个字符。
缺省 : 
缺省没有配置FTPS服务器的SSL策略和PKI证书模板。 
使用说明 : 
1. 设备作为FTPS服务器可以利用SSL协议的数据加密、身份认证和消息完整性验证机制，保证客户端和设备之间数据传输的安全性；2. PKI证书模板为可选参数，如果不指定，则由SSL选择SSL策略中绑定的PKI证书，如果两边都没有指定，则无法进行证书认证；WEB安全服务器认证客户端所需的CA根证书，以及供客户端认证所需的WEB安全服务器本地证书，都可以在PKI证书模板中配置；3. no命令恢复缺省值；4. 使用该命令配置前，需要先在相应的SSL策略中配置SSL/TLS协议版本和加密算法套件，并在相应的PKI模板中导入认证证书；5. 使用时请确认设备的系统时间为准确的当前本地时间，否则有可能导致证书认证失败；6. 当多次使用该命令配置时，以最新的配置生效；7. 执行该命令配置时，已登录的用户会话不受影响，仍使用原有参数，下次新建会话使用新配置的参数；
范例 : 
FTPS服务器关联SSL策略名为zte1、PKI证书模板名为zte-CA： ZXROSNG(config)#ftp-secure-server ssl-context zte1 pki-profile zte-CA
相关命令 : 
ftp-secure-server modeftp-secure-server ssl-context
## ftp-secure-server 

ftp-secure-server 
命令功能 : 
使能或去使能FTPS服务。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-secure-server 
  {disable 
|enable 
}
命令参数解释 : 
参数|描述
---|---
disable|去使能FTPS服务
enable|使能FTPS服务
缺省 : 
默认情况下FTPS服务端未使能。 
使用说明 : 
1. 使能FTPS服务时，需要先去使能普通FTP服务； 
范例 : 
ZXROSNG(config)#ftp-secure-server enable 
相关命令 : 
ftp-secure-server modeftp-secure-server ssl-context
## ftp-server access-class 

ftp-server access-class 
命令功能 : 
该命令工作于全局配置模式，用于配置FTP连接绑定的访问控制列表（Access Control List，ACL）规则名称。配置成功后，新登录FTP连接需要接受ACL规则检查。当需要对指定接入FTP服务器的IP地址进行检查时，可通过此配置允许或者拒绝满足此ACL规则的用户接入。no ftp-server access-class [ipv6]命令用于删除FTP连接绑定的ACL表规则名称。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server access-class 
  [ipv6 
] ＜acl-name 
＞
no ftp-server access-class 
  [ipv6 
]
				
命令参数解释 : 
参数|描述
---|---
ipv6|IPv6类型的ACL
＜acl-name＞|ACL规则名称。取值范围： 1-31位的字符串，可通过show ftp-server命令查询ACL规则名称。默认值：无。
缺省 : 
无 
使用说明 : 
可以配置IP地址类型为Ipv4和Ipv6的ACL规则名称，当不输入IPv6时，默认为IPV4类型的ACL。 
范例 : 
配置IPv4类型的ACL规则的名字为zte：ZXROSNG(config)#ftp-server access-class zte配置IPv6类型的ACL规则的名字为zte：ZXROSNG(config)#ftp-server access-class ipv6 zte
相关命令 : 
show ftp-server 
## ftp-server enable 

ftp-server enable 
命令功能 : 
该命令工作于全局配置模式，当使用FTP服务器功能用于文件传输时，开启FTP 服务器功能。no ftp-server enable命令用于关闭FTP 服务器。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server enable 
  [listen 
 {＜default-port-number 
＞|＜port-number 
＞}]
no ftp-server enable 
命令参数解释 : 
参数|描述
---|---
＜default-port-number＞|FTP协议规定的默认端口号：21号端口。与其他FTP客户端软件对接时，默认采用此端口。
＜port-number＞|可配置的非知名监听端口号。取值范围：2401–2420，当不使用默认端口号，可更改为此范围内的端口号。默认值：无。
缺省 : 
缺省对端口21进行监听 
使用说明 : 
1.只能对没有使用的端口进行监听，当端口被占用时，使能此端口会报错，可通过show sockets命令查看当前端口是否被占用。2.默认监听21号端口。
范例 : 
ZXROSNG(config)#ftp-server enable listen 2405 
相关命令 : 
show ftp-server 
## ftp-server kick-user 

ftp-server kick-user 
命令功能 : 
该命令工作于全局配置模式，强制断开已联机用户。断开后，用户将不能再用FTP指令进行FTP协议允许的操作，如文件传输等。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server kick-user 
  ＜user-id 
＞
命令参数解释 : 
参数|描述
---|---
＜user-id＞|联机用户的ID，可以通过show ftp-server命令查询。取值范围：1-80。默认值：无。
缺省 : 
无 
使用说明 : 
可以通过show ftp-server查看是否有用户在线，并根据在线用户的ID断开连接。 
范例 : 
删除当前联机的ID为1的用户ZXROSNG(config)#ftp-server kick-user 1
相关命令 : 
show ftp-server 
## ftp-server max-login 

ftp-server max-login 
命令功能 : 
该命令工作于全局配置模式，用于配置通过FTP进行远程访问的最大同时在线用户数。 no ftp-server max-login命令用于恢复默认配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server max-login 
  ＜user-number 
＞
no ftp-server max-login 
命令参数解释 : 
参数|描述
---|---
＜user-number＞|最大同时在线用户数量。取值范围：1-40。默认值：40。
缺省 : 
缺省情况下，最大为40 
使用说明 : 
1.登录次数统计的是同时通过FTP远程访问的次数，若次数已达到最大限制，用户通过FTP登录时， 将禁止登录。2.若同时已有若干帐号通过FTP登录，此时修改FTP的同时登录次数的限制，并设置用户数的值小于已登录次数时，不会强制已登录用户下线。
范例 : 
配置FTP最大同时登录次数限制为10ZXROSNG(config)#ftp-server max-login 10
相关命令 : 
show ftp-server 
## ftp-server source-interface 

ftp-server source-interface 
命令功能 : 
配置设备作为FTP服务端时的源接口。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server source-interface 
  ＜interface-name 
＞
no ftp-server source-interface 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|源接口名称，1-31个字符。
缺省 : 
默认情况下没有配置FTP服务端监听的接口。 
使用说明 : 
1.该命令指定的监听接口，用于FTP服务端限定仅允许接受目的地址为该接口主地址（IPv4或IPv6）和该接口VRF域的建链请求；2.server source-interface与ftp-server source-ip同时配置，则FTP服务端优先取指 定接口的主地址，如果未配置，则取指定的地址；3.配置时如果已有用户登录则将不满足条件的用户踢下线4.使用no命令取消配置的监听接口。
范例 : 
配置设备作为FTP服务端时的监听接口：ZXROSNG(config)# ftp-server source-interface gei-0/1/0/1
相关命令 : 
ftp-server source-ipshow running-config ftp
## ftp-server source-ip ipv4 

ftp-server source-ip ipv4 
命令功能 : 
配置设备作为FTP服务端时监听的IPv4地址，使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server source-ip ipv4 
  ＜ipv4-address 
＞
no ftp-server source-ip ipv4 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|监听的IPv4地址，点分十进制格式，例如：192.168.1.1。
缺省 : 
默认情况下没有配置FTP服务端监听的IPv4地址。 
使用说明 : 
1.该命令指定的监听地址，用于FTP服务端限定仅允许接受目的地址为该指定地址建链请求；2.如果ftp-server source-interface与ftp-server source-ip ipv4同时配置，则FTP服务端优先取指定接口的主地址，如果未配置接口，则取指定的地址；3.配置时如果已有用户登录，且未配置源接口则将不满足条件的用户踢下线；4.使用no命令取消配置的监听地址。
范例 : 
配置设备作为FTP服务端时的监听IPv4地址：ZXROSNG(config)# ftp-server source-ip ipv4 192.168.1.1
相关命令 : 
ftp-server source-interfaceshow running-config ftp
## ftp-server source-ip ipv6 

ftp-server source-ip ipv6 
命令功能 : 
配置设备作为FTP服务端时监听的IPv6地址，使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server source-ip ipv6 
  ＜ipv6-address 
＞
no ftp-server source-ip ipv6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|监听的IPv6地址，冒分十六进制格式，例如：200:fd05::d03e
缺省 : 
默认情况下没有配置FTP服务端监听的IPv6地址。 
使用说明 : 
1.该命令指定的监听地址，用于FTP服务端限定仅允许接受目的地址为该指定地址和VRF域的建链请求；2.如果ftp-server source-interface与ftp-server source-ip ipv6同时配置，则FTP服务端优先取指定接口的主地址，如果未指定接口，则取指定的地址；3.配置时如果已有用户登录，且未配置源接口则将不满足条件的用户踢下线；4.使用no命令取消配置的监听接口。
范例 : 
配置设备作为FTP服务端时的监听IPv6地址：ZXROSNG(config)# ftp-server source-ip ipv6 100::1                                                                                 
相关命令 : 
ftp-server source-interfaceshow running-config ftp
## ftp-server source-ip vrf 

ftp-server source-ip vrf 
命令功能 : 
配置设备作为FTP服务端时监听的VRF，使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server source-ip vrf 
  ＜vrf-name 
＞
no ftp-server source-ip vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|非管理口的VRF名称，长度1–32个字符。
缺省 : 
默认情况下没有配置FTP服务端监听的VRF。 
使用说明 : 
1.该命令指定的监听VRF，用于FTP服务端限定仅允许接受目的地址为该VRF域的建链请求；2.如果ftp-server source-interface与ftp-server source-ip vrf同时配置，则FTP服务端优先取指定接口的主地址，如果未指定接口，则取指定的VRF；3.配置时如果已有用户登录，且未配置源接口则将不满足条件的用户踢下线；4.使用no命令取消配置的监听VRF。
范例 : 
配置设备作为FTP服务端时的VRF name：ZXROSNG(config)# ftp-server source-ip vrf mng
相关命令 : 
ftp-server source-interfaceshow running-config ftp
## ftp-server top-directory 

ftp-server top-directory 
命令功能 : 
该命令工作于全局配置模式，用于配置FTP 服务器允许用户通过FTP访问的顶级目录和访问权限。当使用FTP服务器功能时，必须执行该命令，如果用户未手动设置顶级目录，则默认使用/datadisk0/作为目录的顶级目录，权限为所有权限。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp-server top-directory 
  ＜user-top-directory 
＞ [{read-only 
|{[read-write 
],[copy 
]}}]
命令参数解释 : 
参数|描述
---|---
＜user-top-directory＞|用户目录的名称，必须是目录的完整的绝对路径。取值范围： 1-159位的字符串，同时要求单个目录长度不能超过80位字符，如参数为：/目录A/目录B/，“目录A/目录B/”的总长度不能超过159位字符，目录A、目录B单个目录长度不能超过80位字符
read-only|允许访问的权限：只读
read-write|允许访问的权限：读写（包含读、创建、修改、删除、不包含拷贝）
copy|允许访问的权限：拷贝（包含 读、拷贝）
缺省 : 
默认情况下，FTP SERVER允许用户通过FTP访问的顶级目录是/datadisk0/，访问权限是有所有权限。 
使用说明 : 
1.默认情况下，FTP服务器允许用户通过FTP访问的顶级目录是/datadisk0/，访问权限是有所有权限。2.该命令的优先级低于用户授权模式中的ftp top-directory命令，当用户的授权模式没有配置ftp top-directory命令时，用户通过FTP登录后可访问的顶级目录和访问权限以该命令为准。3.当某个帐号已通过FTP登录，此后若修改该命令，则不会对已登录的用户生效，只有用户下一次登录时才按新配置生效。
范例 : 
设置用户的顶级工作目录为/datadisk0/zte/ 权限 read-write copy ：ZXROSNG(config)#ftp-server top-directory /datadisk0/zte/ read-write copy
相关命令 : 
show ftp-server 
## show debug ftp 

show debug ftp 
命令功能 : 
显示debug开关打开状态。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug ftp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示debug开关打开状态:ZXROSNG(config)# show debug ftpFTP:  FTP SSL error debugging is on  FTP SSL event debugging is on  FTP SSL detail debugging is on  FTP SSL packet debugging is on
相关命令 : 
无 
## show ftp-server 

show ftp-server 
命令功能 : 
该命令工作于用户模式外的所有模式，用于查询FTP服务器的配置信息及在线用户信息。其中配置信息包括：服务器使能状态、使能端口号、设置的FTP 服务器顶级目录及目录权限、允许的最大同时在线用户数以及ACL参数（包括IPv4以及IPv6 的ACL参数，用于对接入用户IP地址的检查）；在线用户信息包括：用户ID,用户名、当前状态（在线、离线）、用户IP地址、端口号。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ftp-server 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示FTP服务器的相关配置信息：ZXROSNG#show ftp-server -----------------------------------------------------------------
FTP server run state: enable FTP server listen port: 21FTP server user top directory : /datadisk0/ FTP server user top directory access permissions: read-write copyFTP server ACL name IPv4: FTP server ACL name IPv6: FTP server max online user number: 40FTP secure server run state: disableFTP secure server mode: allFTP secure server explicit port: 21FTP secure server implicit port: 990User-ID Username            Status  IP-address             Port  1       zteztezte1zteztezte online  10.42.49.147           52314        1zteztezte1zteztezt                                        e1zteztezte1zteztez                                        te1zte11                                           -----------------------------------------------------------------
相关命令 : 
无 
# LLDP配置命令 
## basic-tlv management-address-tlv ipv4 

basic-tlv management-address-tlv ipv4 
命令功能 : 
配置携带指定管理地址TLV的IP地址 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
basic-tlv management-address-tlv ipv4 
  ＜ipv4-address 
＞
no basic-tlv management-address-tlv ipv4 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|除全0、全1、组播、广播 外的 单播地址
缺省 : 
无配置 
使用说明 : 
当配置了管理地址IP，则management-address TLV中优先获取此配置的IP，否则获取三层口的IP地址填充此字段；若都获取不到，则不填充 
范例 : 
配置接口gei-0/1/0/1的携带指定管理地址IP的TLV功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#basic-tlv management-address-tlv ipv4  200.22.2.2ZXROSNG(config-lldp-if-gei-0/1/0/1)#ZXROSNG(config-lldp-if-gei-0/1/0/1)#no basic-tlv management-address-tlvZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## basic-tlv management-address-tlv ipv4 

basic-tlv management-address-tlv ipv4 
命令功能 : 
配置全局携带指定管理地址TLV的IP地址 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
basic-tlv management-address-tlv ipv4 
  ＜ipv4-address 
＞
no basic-tlv management-address-tlv ipv4 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|除全0、全1、组播、广播 外的 单播地址
缺省 : 
无配置 
使用说明 : 
management-address TLV中优先获取接口的管理地址IP，其次获取全局配置的管理地址IP，再次获取管理口IP地址，最后获取三层口的IP地址填充此字段；若都获取不到，则不填充。 
范例 : 
配置全局的指定管理地址IP的TLV功能ZXROSNG(config-lldp)#basic-tlv management-address-tlv ipv4  200.22.2.2ZXROSNG(config-lldp)#ZXROSNG(config-lldp)#no basic-tlv management-address-tlv ipv4ZXROSNG(config-lldp)#
相关命令 : 
无 
## basic-tlv management-address-tlv ipv6 

basic-tlv management-address-tlv ipv6 
命令功能 : 
配置全局携带指定管理地址TLV的IPv6地址。 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
basic-tlv management-address-tlv ipv6 
  ＜ipv6-address 
＞
no basic-tlv management-address-tlv ipv6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|IPv6地址。
缺省 : 
无 
使用说明 : 
    management-address TLV支持同时携带IPv4类型的管理地址和IPv6类型的管理地址。在IPv6类型的管理地址中，优先获取接口上LLDP配置的管理地址IPv6地址，其次获取LLDP全局配置的管理地址IPv6地址，再次获取DCN loopback口IPv6地址，再次获取此接口有效的global的IPv6地址填充此字段，最后获取管理口的有效的global 的IPv6地址；若都获取不到，则不填充。   此配置地址需是一个合法的单播IPv6地址，不能是全0、全1、组播、环回等地址。
范例 : 
配置全局IPv6管理地址ZXROSNG(config-lldp)#basic-tlv management-address-tlv ipv6  1::2ZXROSNG(config-lldp)#
ZXROSNG(config-lldp)#no basic-tlv management-address-tlv ipv6ZXROSNG(config-lldp)#
相关命令 : 
LLDP接口模式下basic-tlv management-address-tlv ipv6。
## basic-tlv management-address-tlv ipv6 

basic-tlv management-address-tlv ipv6 
命令功能 : 
配置接口携带指定管理地址TLV的IPv6地址。 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
basic-tlv management-address-tlv ipv6 
  ＜ipv6-address 
＞
no basic-tlv management-address-tlv ipv6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|IPv6地址。
缺省 : 
无 
使用说明 : 
    management-address TLV支持同时携带IPv4类型的管理地址和IPv6类型的管理地址。在IPv6类型的管理地址中，优先获取接口上LLDP配置的管理地址IPv6地址，其次获取LLDP全局配置的管理地址IPv6地址，再次获取DCN loopback口IPv6地址，再次获取此接口有效的global的IPv6地址填充此字段，最后获取管理口的有效的global 的IPv6地址；若都获取不到，则不填充。此命令后面不指定实例，在实例nearest-bridge生效。    此配置地址需是一个合法的单播IPv6地址，不能是全0、全1、组播、环回等地址。
范例 : 
配置gei-0/1/0/1接口管理地址TLV的IPv6地址ZXROSNG(config)#lldpZXROSNG(config-lldp)#interface gei-0/1/0/1ZXROSNG(config-lldp-gei-0/1/0/1)#basic-tlv management-address-tlv ipv6  1::2ZXROSNG(config-lldp-gei-0/1/0/1)#
ZXROSNG(config-lldp-gei-0/1/0/1)#no basic-tlv management-address-tlv ipv6ZXROSNG(config-lldp-gei-0/1/0/1)#
相关命令 : 
LLDP模式下basic-tlv management-address-tlv ipv6 
## clearneighbor 

clearneighbor 
命令功能 : 
清除LLDP邻居 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
clearneighbor 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在LLDP模式下执行此命令时，清除整机所有邻居，在LLDP接口模式下执行此命令时，清除指定接口邻居 
范例 : 
1.清除整机所有邻居ZXROSNG(config-lldp)#clearneighbor ZXROSNG(config-lldp)#2.清除gei-0/1/0/1的邻居ZXROSNG(config-lldp-if-gei-0/1/0/1)#clearneighbor ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## clearneighbor 

clearneighbor 
命令功能 : 
清除LLDP邻居 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
clearneighbor 
  [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
命令参数解释 : 
参数|描述
---|---
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
无 
使用说明 : 
在LLDP模式下执行此命令时，清除整机所有邻居，在LLDP接口模式下执行此命令时，清除指定接口邻居 
范例 : 
1.清除整机所有邻居ZXROSNG(config-lldp)#clearneighbor ZXROSNG(config-lldp)#2.清除gei-0/1/0/1的邻居ZXROSNG(config-lldp-if-gei-0/1/0/1)#clearneighbor ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## clearstatistic 

clearstatistic 
命令功能 : 
清除LLDP统计信息 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
clearstatistic 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在LLDP模式下执行此命令时，将所有接口的统计数清为0，重新开始计数，在LLDP接口模式下执行此命令时，将指定接口的统计计数清为0，该接口重新开始计数 
范例 : 
1.清除所有接口统计计数ZXROSNG(config-lldp)#clearstatistic ZXROSNG(config-lldp)#2.清除gei-0/1/0/1的统计计数ZXROSNG(config-lldp-if-gei-0/1/0/1)#clearstatistic ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## clearstatistic 

clearstatistic 
命令功能 : 
清除LLDP统计信息 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
clearstatistic 
  [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
命令参数解释 : 
参数|描述
---|---
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
无 
使用说明 : 
在LLDP模式下执行此命令时，将所有接口的统计数清为0，重新开始计数，在LLDP接口模式下执行此命令时，将指定接口的统计计数清为0，该接口重新开始计数 
范例 : 
1.清除所有接口统计计数ZXROSNG(config-lldp)#clearstatistic ZXROSNG(config-lldp)#2.清除gei-0/1/0/1的统计计数ZXROSNG(config-lldp-if-gei-0/1/0/1)#clearstatistic ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## debug lldp adjacency 

debug lldp adjacency 
命令功能 : 
打开LLDP邻居相关debug打印功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug lldp adjacency 
  [interface 
 ＜interface-name 
＞]
no debug lldp adjacency 
  [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
缺省 : 
关闭 
使用说明 : 
打开LLDP邻居相关的debug打印，包括邻居添加，邻居老化等信息，执行NO命令，关闭打印功能。信息打印需要打开terminial monitor 
范例 : 
ZXROSNG#debug lldp adjacency LLDP adjacency debugging is onZXR10 PFU-0/1/0 2013-2-28 09:50:28 LLDP-ADD: LLDP neighbor [gei-0/1/0/2 - gei-0/1/0/2] create
相关命令 : 
debug lldp all
## debug lldp all 

debug lldp all 
命令功能 : 
打开LLDP相关所有debug打印功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug lldp all 
 
no debug lldp all 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
打开LLDP相关所有debug打印，执行此命令后，相当于同时打开了debug lldp adjacency/event/packets,执行NO命令，关闭打印功能。信息打印需要打开terminial monitor 
范例 : 
ZXROSNG#debug lldp allLLDP all debugging is onZXROSNG#terminial monitorZXR10 PFU-0/1/0 2013-2-28 10:02:25 LLDP-PKT: Receive packet from gei-0/1/0/2ZXR10 PFU-0/1/0 2013-2-28 10:02:25 LLDP-EVENT:  Port gei-0/1/0/2 RX state machine go to RX_FRAME from RX_WAIT_FOR_FRAMEZXR10 PFU-0/1/0 2013-2-28 10:02:25 LLDP-EVENT:  Port gei-0/1/0/2 RX state machine go to UPDATE_INFO from RX_FRAMEZXR10 PFU-0/1/0 2013-2-28 10:02:25 LLDP-EVENT:  Port gei-0/1/0/2 RX state machine go to RX_WAIT_FOR_FRAME from UPDATE_INFO
相关命令 : 
debug lldp packets debug lldp eventdebug lldp adjacency
## debug lldp event 

debug lldp event 
命令功能 : 
打开LLDP事件相关debug打印功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug lldp event 
  [interface 
 ＜interface-name 
＞]
no debug lldp event 
  [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
缺省 : 
关闭 
使用说明 : 
打开LLDP事件相关的debug打印，包括接口管理down，状态机状态跃迁等，执行NO命令，关闭打印功能。信息打印需要打开terminial monitor 
范例 : 
ZXROSNG#debug lldp eventLLDP event debugging is onZXROSNG#ZXR10 PFU-0/1/0 2013-2-28 09:53:00 LLDP-EVENT:  Port gei-0/1/0/2 RX state machine go to RX_FRAME from RX_WAIT_FOR_FRAMEZXR10 PFU-0/1/0 2013-2-28 09:53:00 LLDP-EVENT:  Port gei-0/1/0/2 RX state machine go to UPDATE_INFO from RX_FRAMEZXR10 PFU-0/1/0 2013-2-28 09:53:00 LLDP-EVENT:  Port gei-0/1/0/2 RX state machine go to RX_WAIT_FOR_FRAME from UPDATE_INFO
相关命令 : 
debug lldp all 
## debug lldp packets receive 

debug lldp packets receive 
命令功能 : 
打开LLDP报文接收相关debug打印功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug lldp packets receive 
  [interface 
 ＜interface-name 
＞]
no debug lldp packets receive 
  [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
缺省 : 
关闭 
使用说明 : 
打开LLDP报文接收相关的debug打印，执行NO命令，关闭打印功能。信息打印需要打开terminial monitor 
范例 : 
ZXROSNG#debug lldp packets receive LLDP packet debugging receive is onZXROSNG#ZXR10 PFU-0/1/0 2013-2-28 09:57:10 LLDP-PKT: Receive packet from gei-0/1/0/2
相关命令 : 
debug lldp packets debug lldp packets senddebug lldp all
## debug lldp packets send 

debug lldp packets send 
命令功能 : 
打开LLDP报文发送相关debug打印功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug lldp packets send 
  [interface 
 ＜interface-name 
＞]
no debug lldp packets send 
  [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
缺省 : 
关闭 
使用说明 : 
打开LLDP报文发送相关的debug打印，执行NO命令，关闭打印功能。信息打印需要打开terminial monitor 
范例 : 
ZXROSNG#debug lldp packets send LLDP packet debugging send is onZXROSNG#ZXR10 PFU-0/1/0 2013-2-28 09:59:41 LLDP-PKT: Send hello packet from gei-0/1/0/2
相关命令 : 
debug lldp packets debug lldp packets receivedebug lldp all
## debug lldp packets 

debug lldp packets 
命令功能 : 
打开LLDP报文相关debug打印功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug lldp packets 
  [interface 
 ＜interface-name 
＞]
no debug lldp packets 
  [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
缺省 : 
关闭 
使用说明 : 
打开LLDP报文相关的debug打印，包括报文发送接收，执行NO命令，关闭打印功能。信息打印需要打开terminial monitor 
范例 : 
ZXROSNG#debug lldp packets LLDP packet debugging is onZXROSNG#ZXR10 PFU-0/1/0 2013-2-28 09:57:10 LLDP-PKT: Receive packet from gei-0/1/0/2
相关命令 : 
debug lldp packets receivedebug lldp packets senddebug lldp all
## dot1-tlv management-vlan-tlv 

dot1-tlv management-vlan-tlv 
命令功能 : 
配置端口携带管理VLAN TLV的VLAN值 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
dot1-tlv management-vlan-tlv 
 vlan 
 ＜VLAN-ID 
＞
no dot1-tlv management-vlan-tlv 
命令参数解释 : 
参数|描述
---|---
＜VLAN-ID＞|VLAN ID
缺省 : 
无 
使用说明 : 
配置此值后端口发送的LLDP中，会携带管理VLAN TLV字段 
范例 : 
ZXROSNG(config-lldp-if-gei-0/1/0/1)# dot1-tlv management-vlan-tlv vlan 1ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## hellotime 

hellotime 
命令功能 : 
配置LLDP发包间隔 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
hellotime 
  ＜hellotime 
＞
no hellotime 
命令参数解释 : 
参数|描述
---|---
＜hellotime＞|发包间隔，单位秒，配置范围5-32768，缺省30秒
缺省 : 
30秒 
使用说明 : 
通过此命令可以配置LLDP的发送hello报文的间隔，配置全局生效，执行NO命令恢复默认配置 
范例 : 
配置LLDP发包间隔为40秒ZXROSNG(config-lldp)#hellotime 40ZXROSNG(config-lldp)#
相关命令 : 
无 
## holdtime 

holdtime 
命令功能 : 
配置LLDP报文保活倍数 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
holdtime 
  ＜holdtime 
＞
no holdtime 
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|hello报文的保活倍数，配置范围2-10，默认4
缺省 : 
4 
使用说明 : 
通过此命令可以配置LLDP hello报文保活倍数，保活时间为hello报文的发包间隔*保活倍数，如果接口端在保活时间内没有再次收到相同邻居的hello报文，此认为邻居丢失。执行NO命令恢复默认配置 
范例 : 
配置报文的保活倍数为10ZXROSNG(config-lldp)#holdtime 10ZXROSNG(config-lldp)#
相关命令 : 
无 
interface : 

interface (LLDP模式) 
命令功能 : 
进入LLDP接口模式 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
interface 
  {byname 
 ＜interface-byname 
＞|＜interface-name 
＞}
命令参数解释 : 
参数|描述
---|---
＜interface-byname＞|接口别名
＜interface-name＞|接口名
缺省 : 
无 
使用说明 : 
此命令进入LLDP接口模式，可通过接口名和接口别名两种方式 
范例 : 
1.通过接口名进入LLDP接口模式ZXROSNG(config-lldp)#interface gei-0/1/0/1ZXROSNG(config-lldp-if-gei-0/1/0/1)#2.通过接口别名进入LLDP接口模式ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname gei-0/1/0/1-bynameZXROSNG(config-if-gei-0/1/0/1)#!ZXROSNG(config)#lldpZXROSNG(config-lldp)#interface byname gei-0/1/0/1-bynameZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
无 
## lldp 

lldp 
命令功能 : 
打开/关闭LLDP功能 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开LLDP功能，包括接收功能和发送功能
disable|关闭LLDP功能，包括接收功能和发送功能
缺省 : 
开启 
使用说明 : 
在LLDP模式下执行此命令时，对全局LLDP功能进行配置，在LLDP接口模式下执行此命令时，对指定接口LLDP功能进行配置 
范例 : 
1.打开全局LLDP功能ZXROSNG(config-lldp)#lldp enable ZXROSNG(config-lldp)#2.关闭gei-0/1/0/1的LLDP功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#lldp disable ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
lldp-rx {enable | disable}lldp-tx {enable | disable}
## lldp 

lldp 
命令功能 : 
打开/关闭LLDP功能 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp 
  {enable 
|disable 
} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
命令参数解释 : 
参数|描述
---|---
enable|打开LLDP功能，包括接收功能和发送功能
disable|关闭LLDP功能，包括接收功能和发送功能
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
开启 
使用说明 : 
在LLDP模式下执行此命令时，对全局LLDP功能进行配置，在LLDP接口模式下执行此命令时，对指定接口LLDP功能进行配置 
范例 : 
1.打开全局LLDP功能ZXROSNG(config-lldp)#lldp enable ZXROSNG(config-lldp)#2.关闭gei-0/1/0/1的LLDP功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#lldp disable ZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
lldp-rx {enable | disable}lldp-tx {enable | disable}
## lldp 

lldp 
命令功能 : 
进入LLDP模式
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
进入LLDP模式 
范例 : 
ZXROSNG(config)#lldpZXROSNG(config-lldp)#
相关命令 : 
无 
## lldp-rx 

lldp-rx 
命令功能 : 
打开/关闭LLDP接收功能 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp-rx 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开LLDP接收功能
disable|关闭LLDP接收功能
缺省 : 
开启 
使用说明 : 
在LLDP接口模式下执行此命令时，对指定接口LLDP接收功能进行配置 
范例 : 
关闭gei-0/1/0/1的nearest-bridge 实例LLDP 接收功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#lldp-rx disable nearest-bridgeZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
lldp {enable | disable} 
## lldp-rx 

lldp-rx 
命令功能 : 
打开/关闭LLDP接收功能 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp-rx 
  {disable 
|enable 
} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
命令参数解释 : 
参数|描述
---|---
disable|关闭LLDP接收功能
enable|打开LLDP接收功能
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
开启 
使用说明 : 
在LLDP接口模式下执行此命令时，对指定接口LLDP接收功能进行配置 
范例 : 
关闭gei-0/1/0/1的nearest-bridge 实例LLDP 接收功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#lldp-rx disable nearest-bridgeZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
lldp {enable | disable} 
## lldp-tx 

lldp-tx 
命令功能 : 
打开/关闭LLDP发送功能 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp-tx 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开LLDP发送功能
disable|关闭LLDP发送功能
缺省 : 
开启 
使用说明 : 
在LLDP模式下执行此命令时，对全局LLDP发送功能进行配置，在LLDP接口模式下执行此命令时，对指定接口LLDP发送功能进行配置 
范例 : 
关闭gei-0/1/0/1的nearest-non-tpmr-bridge 实例LLDP接收功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#lldp-tx disable nearest-non-tpmr-bridgeZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
lldp {enable | disable} 
## lldp-tx 

lldp-tx 
命令功能 : 
打开/关闭LLDP发送功能 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
lldp-tx 
  {disable 
|enable 
} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
命令参数解释 : 
参数|描述
---|---
disable|关闭LLDP发送功能
enable|打开LLDP发送功能
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
开启 
使用说明 : 
在LLDP模式下执行此命令时，对全局LLDP发送功能进行配置，在LLDP接口模式下执行此命令时，对指定接口LLDP发送功能进行配置 
范例 : 
关闭gei-0/1/0/1的nearest-non-tpmr-bridge 实例LLDP接收功能ZXROSNG(config-lldp-if-gei-0/1/0/1)#lldp-tx disable nearest-non-tpmr-bridgeZXROSNG(config-lldp-if-gei-0/1/0/1)#
相关命令 : 
lldp {enable | disable} 
## maxneighbor 

maxneighbor 
命令功能 : 
配置全局支持的最大邻居数 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
maxneighbor 
  ＜maxneighbor 
＞
no maxneighbor 
命令参数解释 : 
参数|描述
---|---
＜maxneighbor＞|最大邻居数，配置范围1-$#84410369#$，默认$#84410377#$。
缺省 : 
128 
使用说明 : 
通过此命令可以配置全局保存的最大邻居个数，本机的邻居个数达到最大个数后，不再保存新邻居，执行NO命令恢复默认配置 
范例 : 
配置本机保存最大邻居个数为10ZXROSNG(config-lldp)#maxneighbor 10ZXROSNG(config-lldp)#
相关命令 : 
接口下最大邻居数配置命令 
## maxneighbor 

maxneighbor 
命令功能 : 
配置接口支持的最大邻居数 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
maxneighbor 
  ＜maxneighbor 
＞ [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
no maxneighbor 
  [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
				
命令参数解释 : 
参数|描述
---|---
＜maxneighbor＞|最大邻居数，配置范围1-$#84410370#$，默认8
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
8 
使用说明 : 
通过此命令可以配置全局保存的最大邻居个数，本实例的邻居个数达到最大个数后，不再保存新邻居，执行NO命令恢复默认配置 
范例 : 
配置gei-0/1/0/1 nearest-customer-bridge实例保存最大邻居个数为7ZXROSNG(config) lldpZXROSNG(config-lldp)interface gei-0/1/0/1ZXROSNG(config-lldp-if-gei-0/1/0/1)maxneighbor 7 nearest-customer-bridge
相关命令 : 
接口下最大邻居数配置命令 
## msgfasttx 

msgfasttx 
命令功能 : 
配置快速发送报文的间隔 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
msgfasttx 
  ＜fast-tx-interval 
＞
no msgfasttx 
命令参数解释 : 
参数|描述
---|---
＜fast-tx-interval＞|快速发送报文间隔，单位秒，配置范围1-3600，默认1秒
缺省 : 
1秒 
使用说明 : 
当实体收到新邻居时，要连续发送若干个hello报文，此命令配置此过程中发送报文的间隔，执行NO命令恢复默认配置 
范例 : 
配置快速发送报文间隔为2秒ZXROSNG(config-lldp)#msgfasttx 2 ZXROSNG(config-lldp)#
相关命令 : 
无 
## notification 

notification 
命令功能 : 
配置端口上LLDP实例邻居变化trap通知功能启动/禁止 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
notification 
  {disable 
|enable 
} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]
命令参数解释 : 
参数|描述
---|---
disable|关闭trap通知功能
enable|启动trap通知功能
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
disable不指定实例时，默认是基于nearest-bridge进行配置
使用说明 : 
配置是否在实例邻居变化时发送trap通知。 
范例 : 
ZXROSNG(config) lldpZXROSNG(config-lldp)interface gei-0/1/0/1ZXROSNG(config-lldp-if-gei-0/1/0/1)notification enable nearest-customer-bridge
相关命令 : 
无 
## reinitdelay 

reinitdelay 
命令功能 : 
配置LLDP实例发送状态机初始化间隔 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
reinitdelay 
  ＜reinit-delay 
＞
no reinitdelay 
命令参数解释 : 
参数|描述
---|---
＜reinit-delay＞|LLDP实例发送状态机初始化间隔，单位为秒，范围1-10，默认值为2
缺省 : 
2秒 
使用说明 : 
无 
范例 : 
ZXROSNG(config) lldpZXROSNG(config-lldp)reinitdelay 8
相关命令 : 
无 
## show debug lldp 

show debug lldp 
命令功能 : 
显示打开的LLDP debug选项 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug lldp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示打开的LLDP debug选项 
范例 : 
ZXROSNG#show debug lldpLLDP:  LLDP packet receive debugging is on  LLDP packet send debugging is on  LLDP adjacency debugging is on  LLDP event debugging is onZXROSNG#
相关命令 : 
无 
## show lldp config 

show lldp config 
命令功能 : 
查看LLDP配置信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show lldp config 
  [interface 
 {＜interface-name 
＞} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]] 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
无 
使用说明 : 
此命令可以查看LLDP全局配置信息，命令后可选参数接口也被指定时，显示指定接口的配置信息，查看LLDP端口实例配置信息时，不指定实例时则显示接口下所有实例信息。 
范例 : 
1.显示LLDP全局配置信息ZXROSNG#show lldp config--------------------------------------LLDP enable:        enabledRxTxLLDP helloTime:     30sLLDP holdTime:      4LLDP msgFastTx:     1sLLDP txCreditMax:   5LLDP txFastInit:    4LLDP mngIpAddr:     0.0.0.0LLDP mngIpV6Addr:   1:0:0:0:0:0:0:2LLDP deadTime:              120sLLDP maxNeighbor:           128LLDP curNeighbor:           0LLDP reInitDelay:           2sLLDP notificationInterval:  30sLLDP neighborRptNetconf:    disable--------------------------------------2.查看指定接口gei-0/1/0/1的配置信息ZXROSNG#show lldp config interface gei-0/1/0/1-------------------------------------- Group MAC address:    Nearest Bridge LLDP port enable:    enabledRxTx LLDP maxneighbor:    8 LLDP curneighbor:    0 LLDP transparent:    disable LLDP portmngaddr:    IPv4-0.0.0.0, NULL LLDP portmngaddr:    IPv6-1:0:0:0:0:0:0:2, mgmt_ethLLDP notification:   disable -------------------------------------- -------------------------------------- Group MAC address:    Nearest non-TPMR Bridge LLDP port enable:    disable LLDP maxneighbor:    8 LLDP curneighbor:    0 LLDP transparent:    disable LLDP portmngaddr:    IPv4-0.0.0.0, NULL LLDP notification:   disable -------------------------------------- -------------------------------------- Group MAC address:    Nearest Customer Bridge LLDP port enable:    disable LLDP maxneighbor:    8 LLDP curneighbor:    0 LLDP transparent:    disable LLDP portmngaddr:    IPv4-0.0.0.0, NULL LLDP notification:   disable --------------------------------------
相关命令 : 
无 
## show lldp entry 

show lldp entry 
命令功能 : 
查看LLDP邻居详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show lldp entry 
  [interface 
 {＜interface-name 
＞} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]] 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
无 
使用说明 : 
查看当前LLDP的邻居详细信息，可选项接口被指定时，显示指定接口的邻居的详细信息，查看LLDP端口实例邻居详细信息时，不指定实例时则显示接口下所有实例信息。 
范例 : 
1.查看整机邻居详细信息ZXROSNG(config-if-gei-0/1/0/2)#show lldp entry-------------------------------------------------------- Local Port: gei-0/1/0/4 | Interface Name Group MAC address: Nearest Bridge | MAC Address Chassis ID: 00eeff101000 | MAC Address Peer Port: gei-0/1/0/4 Nearest Bridge | Interface Name TTL: 1 | Time to live Port Description: Port name gei-0/1/0/4, PortPhyStatus is up, PortPhotoElectricityMode is electric, Pvid 1 Nearest Bridge System Name: ZXR10 System Description: M6000v2.00.20(2.2.0), ZXR10, ZXR10 M6000-16 Software, NULL System Capability: Bridge, Router Management Address: IPv4 - 0.0.0.0, ifIndex - 0, OID - NullLLDP DOT3-TLV INFO:  MAC/PHY Cfg/Status TLV:     auto-negotiation Support/Status: 3     auto-negotiation Support: supported     auto-negotiation Status: enabled     PMD auto-negotiation advertised Capability: 100BASE-TX full duplex mode     operational MAU Type: X fiber over PMT, half duplex mode  Power Via MDI TLV:      MDI power support: 1     Port Class: PSE     PSE MDI Power Support: not supported     PSE MDI Power State: disabled     PSE Power Pair Control ability: not controlled     PSE power pair: supported     power class: supported Link Aggregation TLV: Not Enabled Maximum Frame Size TLV:     maximum dot3 frame size: 1518 LLDP MED-TLV INFO:  MED Capabilities TLV:      Capabilities: LLDP-MED Capabilities, Network Policy, Extended Power via MDI-PSE     Device Type: Endpoint Class II   MED Network Policy:      Application Type: Reserved     U: defined     T: tagged     X: Reserved     VLAN ID: 1     L2 Priority: 1     DSCP Value: 1  MED Location ID TLV:      Locatin Data Formate: Coordinate-based LCI     Location ID:         Code 123:01         Length 16:10         LaRes:02         Latitude:00 53 C1 F7 51         LoRes:00         Latitude:03 50 BA 5B 97         AT:02         AltRes:00         Altitude:00 00 67 00         Datum:09  MED Extended Power via MDI:      Power Type: PD Device     Power Source: Local     Power Priority: Low     Power Value: 88.00 Watts MED Inventory Hardware Revision: Hw_No-3.0.20.49 MED Inventory Firmware Revision: Fw_No-2.0.10.49 MED Inventory Software Revision: Sw_No-5.3.10.2 MED Inventory Serial Number: S_No-3200-987-648-376 MED Inventory Manufacturer Name: Ma_No-zte corp. MED Inventory Model Name: Mo_No-m6000 sr MED Inventory Assert ID: A_Id-nj1000-347 -------------------------------------------------------- Local Port: gei-0/1/0/4 | Interface Name  Local Dest Mac Address: Nearest non-TPMR Bridge | Mac Address Chassis ID: 00eeff101000 | MAC Address Peer Port: gei-0/1/0/4 Nearest non-TPMR Bridge | Interface Name TTL: 1 | Time to live Port Description: Port name gei-0/1/0/4, PortPhyStatus is up, PortPhotoElectricityMode is electric, Pvid 1 Nearest non-TPMR Bridge System Name: ZXR10 System Description: M6000v2.00.20(2.2.0), ZXR10, ZXR10 M6000-16 Software, NULL System Capability: Bridge, Router Management Address: IPv4 - 0.0.0.0, ifIndex - 0, OID - NullLLDP DOT3-TLV INFO:  MAC/PHY Cfg/Status TLV:     auto-negotiation Support/Status: 3     auto-negotiation Support: supported     auto-negotiation Status: enabled     PMD auto-negotiation advertised Capability: 100BASE-TX full duplex mode     operational MAU Type: X fiber over PMT, half duplex mode  Power Via MDI TLV:      MDI power support: 1     Port Class: PSE     PSE MDI Power Support: not supported     PSE MDI Power State: disabled     PSE Power Pair Control ability: not controlled     PSE power pair: supported     power class: supported Link Aggregation TLV: Not Enabled Maximum Frame Size TLV:     maximum dot3 frame size: 1518 LLDP MED-TLV INFO:  MED Capabilities TLV:      Capabilities: LLDP-MED Capabilities, Network Policy, Extended Power via MDI-PSE     Device Type: Endpoint Class II   MED Network Policy:      Application Type: Reserved     U: defined     T: tagged     X: Reserved     VLAN ID: 1     L2 Priority: 1     DSCP Value: 1  MED Location ID TLV:      Locatin Data Formate: Coordinate-based LCI     Location ID:         Code 123:01         Length 16:10         LaRes:02         Latitude:00 53 C1 F7 51         LoRes:00         Latitude:03 50 BA 5B 97         AT:02         AltRes:00         Altitude:00 00 67 00         Datum:09  MED Extended Power via MDI:      Power Type: PD Device     Power Source: Local     Power Priority: Low     Power Value: 88.00 Watts MED Inventory Hardware Revision: Hw_No-3.0.20.49 MED Inventory Firmware Revision: Fw_No-2.0.10.49 MED Inventory Software Revision: Sw_No-5.3.10.2 MED Inventory Serial Number: S_No-3200-987-648-376 MED Inventory Manufacturer Name: Ma_No-zte corp. MED Inventory Model Name: Mo_No-m6000 sr MED Inventory Assert ID: A_Id-nj1000-347 -------------------------------------------------------- Local Port: gei-0/1/0/4 | Interface Name  Group MAC address: Nearest Customer Bridge | Mac Address Chassis ID: 00eeff101000 | MAC Address Peer Port: gei-0/1/0/4 Nearest Customer Bridge | Interface Name TTL: 1 | Time to live Port Description: Port name gei-0/1/0/4, PortPhyStatus is up, PortPhotoElectricityMode is electric, Pvid 1 Nearest Customer Bridge System Name: ZXR10 System Description: M6000v2.00.20(2.2.0), ZXR10, ZXR10 M6000-16 Software, NULL System Capability: Bridge, Router Management Address: IPv4 - 0.0.0.0, ifIndex - 0, OID - NullLLDP DOT3-TLV INFO:  MAC/PHY Cfg/Status TLV:     auto-negotiation Support/Status: 3     auto-negotiation Support: supported     auto-negotiation Status: enabled     PMD auto-negotiation advertised Capability: 100BASE-TX full duplex mode     operational MAU Type: X fiber over PMT, half duplex mode  Power Via MDI TLV:      MDI power support: 1     Port Class: PSE     PSE MDI Power Support: not supported     PSE MDI Power State: disabled     PSE Power Pair Control ability: not controlled     PSE power pair: supported     power class: supported Link Aggregation TLV: Not Enabled Maximum Frame Size TLV:     maximum dot3 frame size: 1518 LLDP MED-TLV INFO:  MED Capabilities TLV:      Capabilities: LLDP-MED Capabilities, Network Policy, Extended Power via MDI-PSE     Device Type: Endpoint Class II   MED Network Policy:      Application Type: Reserved     U: defined     T: tagged     X: Reserved     VLAN ID: 1     L2 Priority: 1     DSCP Value: 1  MED Location ID TLV:      Locatin Data Formate: Coordinate-based LCI     Location ID:         Code 123:01         Length 16:10         LaRes:02         Latitude:00 53 C1 F7 51         LoRes:00         Latitude:03 50 BA 5B 97         AT:02         AltRes:00         Altitude:00 00 67 00         Datum:09  MED Extended Power via MDI:      Power Type: PD Device     Power Source: Local     Power Priority: Low     Power Value: 88.00 Watts MED Inventory Hardware Revision: Hw_No-3.0.20.49 MED Inventory Firmware Revision: Fw_No-2.0.10.49 MED Inventory Software Revision: Sw_No-5.3.10.2 MED Inventory Serial Number: S_No-3200-987-648-376 MED Inventory Manufacturer Name: Ma_No-zte corp. MED Inventory Model Name: Mo_No-m6000 sr MED Inventory Assert ID: A_Id-nj1000-347 ZXROSNG(config-lldp-if-gei-0/1/0/4)#2.查看指定接口gei-0/1/0/1的邻居详细信息ZXROSNG(config-if-gei-0/1/0/2)#show lldp entry interface gei-0/1/0/1---------------------------------------------------------------------------------------------------------------- Local Port: gei-0/1/0/4 | Interface Name  Group MAC address: Nearest Bridge | Mac Address Chassis ID: 00eeff101000 | MAC Address Peer Port: gei-0/1/0/4 Nearest Bridge | Interface Name TTL: 1 | Time to live Port Description: Port name gei-0/1/0/4, PortPhyStatus is up, PortPhotoElectricityMode is electric, Pvid 1 Nearest Bridge System Name: ZXR10 System Description: M6000v2.00.20(2.2.0), ZXR10, ZXR10 M6000-16 Software, NULL System Capability: Bridge, Router Management Address: IPv4 - 0.0.0.0, ifIndex - 0, OID - NullLLDP DOT3-TLV INFO:  MAC/PHY Cfg/Status TLV:     auto-negotiation Support/Status: 3     auto-negotiation Support: supported     auto-negotiation Status: enabled     PMD auto-negotiation advertised Capability: 100BASE-TX full duplex mode     operational MAU Type: X fiber over PMT, half duplex mode  Power Via MDI TLV:      MDI power support: 1     Port Class: PSE     PSE MDI Power Support: not supported     PSE MDI Power State: disabled     PSE Power Pair Control ability: not controld     PSE power pair: supported     power class: supported Link Aggregation TLV: Not Enabled Maximum Frame Size TLV:     maximum dot3 frame size: 1518 LLDP MED-TLV INFO:  MED Capabilities TLV:      Capabilities: LLDP-MED Capabilities, Network Policy, Extended Power via MDI-PSE     Device Type: Endpoint Class II   MED Network Policy:      Application Type: Reserved     U: defined     T: tagged     X: Reserved     VLAN ID: 1     L2 Priority: 1     DSCP Value: 1  MED Location ID TLV:      Locatin Data Formate: Coordinate-based LCI     Location ID:         Code 123:01         Length 16:10         LaRes:02         Latitude:00 53 C1 F7 51         LoRes:00         Latitude:03 50 BA 5B 97         AT:02         AltRes:00         Altitude:00 00 67 00         Datum:09  MED Extended Power via MDI:      Power Type: PD Device     Power Source: Local     Power Priority: Low     Power Value: 88.00 Watts MED Inventory Hardware Revision: Hw_No-3.0.20.49 MED Inventory Firmware Revision: Fw_No-2.0.10.49 MED Inventory Software Revision: Sw_No-5.3.10.2 MED Inventory Serial Number: S_No-3200-987-648-376 MED Inventory Manufacturer Name: Ma_No-zte corp. MED Inventory Model Name: Mo_No-m6000 sr MED Inventory Assert ID: A_Id-nj1000-347 -------------------------------------------------------- Local Port: gei-0/1/0/4 | Interface Name  Group MAC address: Nearest non-TPMR Bridge | Mac Address Chassis ID: 00eeff101000 | MAC Address Peer Port: gei-0/1/0/4 Nearest non-TPMR Bridge | Interface Name TTL: 1 | Time to live Port Description: Port name gei-0/1/0/4, PortPhyStatus is up, PortPhotoElectricityMode is electric, Pvid 1 Nearest non-TPMR Bridge System Name: ZXR10 System Description: M6000v2.00.20(2.2.0), ZXR10, ZXR10 M6000-16 Software, NULL System Capability: Bridge, Router Management Address: IPv4 - 0.0.0.0, ifIndex - 0, OID - NullLLDP DOT3-TLV INFO:  MAC/PHY Cfg/Status TLV:     auto-negotiation Support/Status: 3     auto-negotiation Support: supported     auto-negotiation Status: enabled     PMD auto-negotiation advertised Capability: 100BASE-TX full duplex mode     operational MAU Type: X fiber over PMT, half duplex mode  Power Via MDI TLV:      MDI power support: 1     Port Class: PSE     PSE MDI Power Support: not supported     PSE MDI Power State: disabled     PSE Power Pair Control ability: not controld     PSE power pair: supported     power class: supported Link Aggregation TLV: Not Enabled Maximum Frame Size TLV:     maximum dot3 frame size: 1518 LLDP MED-TLV INFO:  MED Capabilities TLV:      Capabilities: LLDP-MED Capabilities, Network Policy, Extended Power via MDI-PSE     Device Type: Endpoint Class II   MED Network Policy:      Application Type: Reserved     U: defined     T: tagged     X: Reserved     VLAN ID: 1     L2 Priority: 1     DSCP Value: 1  MED Location ID TLV:      Locatin Data Formate: Coordinate-based LCI     Location ID:         Code 123:01         Length 16:10         LaRes:02         Latitude:00 53 C1 F7 51         LoRes:00         Latitude:03 50 BA 5B 97         AT:02         AltRes:00         Altitude:00 00 67 00         Datum:09  MED Extended Power via MDI:      Power Type: PD Device     Power Source: Local     Power Priority: Low     Power Value: 88.00 Watts MED Inventory Hardware Revision: Hw_No-3.0.20.49 MED Inventory Firmware Revision: Fw_No-2.0.10.49 MED Inventory Software Revision: Sw_No-5.3.10.2 MED Inventory Serial Number: S_No-3200-987-648-376 MED Inventory Manufacturer Name: Ma_No-zte corp. MED Inventory Model Name: Mo_No-m6000 sr MED Inventory Assert ID: A_Id-nj1000-347 -------------------------------------------------------- Local Port: gei-0/1/0/4 | Interface Name  Group MAC address: Nearest Customer Bridge | Mac Address Chassis ID: 00eeff101000 | MAC Address Peer Port: gei-0/1/0/4 Nearest Customer Bridge | Interface Name TTL: 1 | Time to live Port Description: Port name gei-0/1/0/4, PortPhyStatus is up, PortPhotoElectricityMode is electric, Pvid 1 Nearest Customer Bridge System Name: ZXR10 System Description: M6000v2.00.20(2.2.0), ZXR10, ZXR10 M6000-16 Software, NULL System Capability: Bridge, Router Management Address: IPv4 - 0.0.0.0, ifIndex - 0, OID - NullLLDP DOT3-TLV INFO:  MAC/PHY Cfg/Status TLV:     auto-negotiation Support/Status: 3     auto-negotiation Support: supported     auto-negotiation Status: enabled     PMD auto-negotiation advertised Capability: 100BASE-TX full duplex mode     operational MAU Type: X fiber over PMT, half duplex mode  Power Via MDI TLV:      MDI power support: 1     Port Class: PSE     PSE MDI power support: not supported     PSE MDI power state: disabled     PSE pairs control ability: not be controlled     PSE power pair: supported     power class: supported Link Aggregation TLV: not enabled Maximum Frame Size TLV:     maximum dot3 frame size: 1518 LLDP MED-TLV INFO:  MED Capabilities TLV:      Capabilities: LLDP-MED Capabilities, Network Policy, Extended Power via MDI-PSE     Device Type: Endpoint Class II   MED Network Policy:      Application Type: Reserved     U: defined     T: tagged     X: Reserved     VLAN ID: 1     L2 Priority: 1     DSCP Value: 1  MED Location ID TLV:      Locatin Data Formate: Coordinate-based LCI     Location ID:         Code 123:01         Length 16:10         LaRes:02         Latitude:00 53 C1 F7 51         LoRes:00         Latitude:03 50 BA 5B 97         AT:02         AltRes:00         Altitude:00 00 67 00         Datum:09  MED Extended Power via MDI:      Power Type: PD Device     Power Source: Local     Power Priority: Low     Power Value: 88.00 Watts MED Inventory Hardware Revision: Hw_No-3.0.20.49 MED Inventory Firmware Revision: Fw_No-2.0.10.49 MED Inventory Software Revision: Sw_No-5.3.10.2 MED Inventory Serial Number: S_No-3200-987-648-376 MED Inventory Manufacturer Name: Ma_No-zte corp. MED Inventory Model Name: Mo_No-m6000 sr MED Inventory Assert ID: A_Id-nj1000-347 ZXROSNG(config-lldp-if-gei-0/1/0/4)#
相关命令 : 
无 
## show lldp neighbor 

show lldp neighbor 
命令功能 : 
查看LLDP邻居的基本信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show lldp neighbor 
  [brief 
] [interface 
 {＜interface-name 
＞} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]] 
命令参数解释 : 
参数|描述
---|---
brief|显示简要信息
＜interface-name＞|接口名
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
无 
使用说明 : 
查看当前LLDP的邻居的基本信息，可选项接口被指定时，显示指定接口的邻居的基本信息，查看LLDP端口实例配置信息，不指定实例时则显示接口下所有实例信息。当指定brief参数时，显示简要信息。 
范例 : 
1.显示整机所有邻居的基本信息ZXROSNG(config-if-fei-0/20/0/2)#show lldp neighborThe total neighbor number:2 Capability Codes:                   N - Other, r - Repeater, B - Bridge, W - WLAN Access Point,                  R - Router, T - Telephone, D - DOCSIS Cable Device,                  S - Station OnlyLocal-Port    Chassis-ID    Holdtime Capability Platform         Peer-Port--------------------------------------------------------------------------------fei-0/20/0/1  00eeff101030  82       B R        M6000v2.00.20(2. fei-0/20/0/1                                                2.0), ZXR10, ..  fei-0/20/0/2  00eeff101030  114      B R        M6000v2.00.20(2. fei-0/20/0/2                                                2.0), ZXR10, ..  2.显示指定接口fei-0/20/0/1的基本信息ZXROSNG(config-if-fei-0/20/0/2)#show lldp neighbor interface fei-0/20/0/1The total neighbor number:1Capability Codes:                   N - Other, r - Repeater, B - Bridge, W - WLAN Access Point,                  R - Router, T - Telephone, D - DOCSIS Cable Device,                  S - Station OnlyLocal-Port    Chassis-ID    Holdtime Capability Platform         Peer-Port--------------------------------------------------------------------------------fei-0/20/0/1  00eeff101030  100      B R        M6000v2.00.20(2. fei-0/20/0/1                                                2.0), ZXR10, ..  3.显示指定接口的简要信息ZXROSNG(config-if-fei-0/20/0/2)#show lldp neighbor brief interface gei-0/1/0/1Scope Codes:    NB    = Nearest bridge    NC    = Nearest Customer Bridge    NTPMR = Nearest non-TPMR bridge   Total neighbors: 1Local Intf       Scope Chassis ID      Port ID         Hold-time System Name   --------------------------------------------------------------------------------gei-0/1/0/1      NB  0019.8407.2400 gei-0/1/0/1      119    gengchunjingjia                                                             ngyutingliuz...
相关命令 : 
无 
## show lldp statistic 

show lldp statistic 
命令功能 : 
显示LLDP统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show lldp statistic 
  [interface 
 {＜interface-name 
＞} [{nearest-bridge 
|nearest-non-tpmr-bridge 
|nearest-customer-bridge 
}]] 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名
nearest-bridge|实例目的MAC地址为01-80-C2-00-00-0E
nearest-non-tpmr-bridge|实例目的MAC地址为01-80-C2-00-00-03
nearest-customer-bridge|实例目的MAC地址为01-80-C2-00-00-00
缺省 : 
无 
使用说明 : 
此命令用来显示LLDP的统计信息，如发包数，收包数等，增加接口选项则显示指定接口统计信息，查看LLDP端口实例统计信息时，不指定实例时则显示接口下所有实例信息。 
范例 : 
1.显示全局统计信息ZXROSNG#show lldp statistic LLDP global counters:Total packets output: 35, input: 25Total packets error: 0, discarded: 0Total TLVs discarded: 0, unrecognized: 0Total neighbors added: 2, deleted: 0Total neighbors aged: 0, droped: 02.显示指定接口gei-0/20/0/1的统计信息ZXROSNG#show lldp statistic  interface gei-0/20/0/1LLDP port counters:Total packets output: 16, input: 14Total packets error: 0, discarded: 0Total TLVs discarded: 0, unrecognized: 0Total neighbors added: 1, deleted: 0Total neighbors aged: 0, droped: 0
相关命令 : 
无 
## tlv-optional basic management-address ipv6 

tlv-optional basic management-address ipv6 
命令功能 : 
配置LLDP全局封装IPv6类型管理地址开启或关闭 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
tlv-optional basic management-address ipv6 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启LLDPDU封装IPv6类型管理地址TLV功能
disable|关闭LLDPDU封装IPv6类型管理地址TLV功能
缺省 : 
$#84410397:0/关闭;1/开启#$ 
使用说明 : 
使用场景:当本设备发出的LLDPDU封装IPv6类型管理地址TLV导致对接设备有异常时（如LLDP不能建链，管理地址不能正确解析等），可用此命令将IPv6类型管理地址TLV的封装功能关闭。如果对接设备需要IPv6类型的管理地址，则可以通过此命令将IPv6类型管理地址TLV的封装功能开启。后续操作：此命令与LLDP接口模式下的对应命令一起控制LLDPDU中是否封装IPv6类型管理地址TLV。只有全局与接口的功能同时打开，接口才会获取可用的IPv6类型管理地址TLV，并封装在发送的LLDPDU中。注意事项：此命令只控制发送LLDPDU中是否封装IPv6类型管理地址TLV功能的开关，当没有可用的IPv6类型的管理地址时，即使功能打开，报文中也不会封装IPv6类型管理地址TLV。
范例 : 
配置全局IPv6类型管理地址TLV功能为开启ZXROSNG(config)#lldpZXROSNG(config-lldp)#tlv-optional basic management-address ipv6 enable
相关命令 : 
LLDP接口模式下tlv-optional basic management-address ipv6命令
## tlv-optional basic management-address ipv6 

tlv-optional basic management-address ipv6 
命令功能 : 
配置LLDP接口封装IPv6类型管理地址开启或关闭 
命令模式 : 
 LLDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tlv-optional basic management-address ipv6 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启LLDPDU封装IPv6类型管理地址TLV功能
disable|关闭LLDPDU封装IPv6类型管理地址TLV功能
缺省 : 
开启 
使用说明 : 
使用场景:当本接口发出的LLDPDU封装IPv6类型管理地址TLV导致对接设备有异常时（如LLDP不能建链，管理地址不能正确解析等），可用此命令将IPv6类型管理地址TLV的封装功能关闭。如果对接接口需要IPv6类型的管理地址，则可以通过此命令将IPv6类型管理地址TLV的封装功能开启。后续操作：此命令与LLDP模式下的对应命令一起控制LLDPDU中是否封装IPv6类型管理地址TLV。只有全局与接口的功能同时打开，接口才会获取可用的IPv6类型管理地址TLV，并封装在发送的LLDPDU中。注意事项：此命令只控制发送LLDPDU中是否封装IPv6类型管理地址TLV功能的开关，当没有可用的IPv6类型的管理地址时，即使功能打开，报文中也不会封装IPv6类型管理地址TLV。
范例 : 
配置接口IPv6类型管理地址TLV功能为开启ZXROSNG(config)#lldpZXROSNG(config-lldp)#interface gei-0/1/0/1ZXROSNG(config-lldp-if-gei-0/1/0/1)#tlv-optional basic management-address ipv6 enable
相关命令 : 
LLDP模式下tlv-optional basic management-address ipv6命令 
## txcreditmax 

txcreditmax 
命令功能 : 
配置发送报文最大信誉值 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
txcreditmax 
  ＜max-tx-credit 
＞
no txcreditmax 
命令参数解释 : 
参数|描述
---|---
＜max-tx-credit＞|最大信誉值，配置范围1-10，默认5
缺省 : 
5 
使用说明 : 
这个配置为防止实体连续发送过多报文，可以通过配置最大信誉值来限制，只有信誉值大于0时才允许发送报文，每发送一个报文信誉值减1，而信誉值每一秒会增加1，达到最大值后不再增加。执行NO命令恢复默认配置 
范例 : 
配置最大信誉值为7ZXROSNG(config-lldp)#txcreditmax 7ZXROSNG(config-lldp)#
相关命令 : 
无 
## txfastinit 

txfastinit 
命令功能 : 
配置快速发送报文的个数 
命令模式 : 
 LLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
txfastinit 
  ＜fast-tx-num 
＞
no txfastinit 
命令参数解释 : 
参数|描述
---|---
＜fast-tx-num＞|快速发送报文个数，配置范围1-8，默认4
缺省 : 
4 
使用说明 : 
收到新的邻居后，LLDP会快速发送几个报文，以使对端更快的发现本端，此命令就是配置快带发送报文的个数，执行NO命令恢复默认配置 
范例 : 
配置快速发送报文个数为6ZXROSNG(config-lldp)#txfastinit 6ZXROSNG(config-lldp)#
相关命令 : 
无 
# MAC配置命令 
## aging-time 

aging-time 
命令功能 : 
配置MAC老化时间。 
命令模式 : 
 MAC模式  
命令默认权限级别 : 
15 
命令格式 : 
aging-time 
  ＜aging-time 
＞
no aging-time 
命令参数解释 : 
参数|描述
---|---
＜aging-time＞|老化时间，单位“秒”，范围60~$#84017413#$，默认为$#84017412#$。
缺省 : 
默认老化时间为$#84017412#$秒。 
使用说明 : 
配置全局MAC老化时间，使用no命令恢复为默认值。 
范例 : 
在MAC模式下，执行aging-time命令设置mac老化时间。步骤1 进入系统模式。ZXR10>en 18Password:ZXROSNG#步骤 2 在系统模式下，执行config terminal进入全局配置模式。ZXROSNG#config terminalZXROSNG(config)#步骤 3 在全局配置模式下，执行mac命令进入MAC模式。ZXROSNG(config)#macZXROSNG(config-mac)#步骤 4 在MAC模式下，执行aging-time命令设置mac老化时间。ZXROSNG(config-mac)# aging-time 90
相关命令 : 
无 
## alarm-threshold 

alarm-threshold 
命令功能 : 
配置整机MAC容量告警阈值百分比。 
命令模式 : 
 MAC模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold 
  ＜percent 
＞
no alarm-threshold 
命令参数解释 : 
参数|描述
---|---
＜percent＞|整机MAC容量告警阈值百分比，范围：1~100
缺省 : 
默认为80 
使用说明 : 
该命令用于配置整机MAC容量告警阈值百分比。当整机MAC条目数占整机容量最大值的百分比超过该值时，产生告警。 
范例 : 
在MAC模式下，执行alarm-threshold命令配置整机MAC容量告警阈值百分比为90%。步骤1 进入系统模式。ZXR10>en 18Password:ZXROSNG#步骤 2 在系统模式下，执行config terminal进入全局配置模式。ZXROSNG#config terminalZXROSNG(config)#步骤 3 在全局配置模式下，执行mac命令进入MAC模式。ZXROSNG(config)#macZXROSNG(config-mac)#步骤 4 在MAC模式下，执行alarm-threshold命令配置整机MAC容量告警阈值百分比为90%。ZXROSNG(config-mac)# alarm-threshold 90
相关命令 : 
无 
## mac 

mac 
命令功能 : 
进入MAC模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
mac 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
进入MAC模式。 
范例 : 
进入MAC模式步骤1 进入系统模式。ZXR10>en 18Password:ZXROSNG#步骤 2 在系统模式下，执行config terminal进入全局配置模式。ZXROSNG#config terminalZXROSNG(config)#步骤 3 在全局配置模式下，执行mac命令进入MAC模式。ZXROSNG(config)#macZXROSNG(config-mac)#步骤 4在全局配置模式下，执行mac命令进入MAC模式。ZXROSNG(config)#macZXROSNG(config-mac)#
相关命令 : 
无 
## show mac count 

show mac count 
命令功能 : 
显示MAC学习历史数量峰值及相应时间和分时段统计。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mac count 
  {mac-hour 
|mac-day 
|mac-max 
} 
命令参数解释 : 
参数|描述
---|---
mac-hour|显示最近24小时内每小时MAC学习数量的最大值以及对应时间。
mac-day|显示出最近30天内每天MAC学习数量的最大值以及对应时间。
mac-max|显示出历史MAC学习数量的最大值以及对应时间。
缺省 : 
无 
使用说明 : 
无 
范例 : 
在全局配置模式下，显示出最近30天内每天MAC学习数量的最大值以及对应时间。ZXROSNG(config)#show mac count mac-dayMACNum   Time----------------------1     2008-12-12 07:43:41 UTC3     2008-12-13 00:01:33 UTC2     2008-12-14 00:00:00 UTC域信息描述表：域          描述MACNum    MAC地址数量Time      产生的时间
相关命令 : 
无 
# MIM配置命令 
## clear configuration commit 

clear configuration commit 
命令功能 : 
清除所有或者保存时间最早的若干个连续配置回退点。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear configuration commit 
  [earliest 
 ＜earliest-number 
＞
命令参数解释 : 
参数|描述
---|---
＜earliest-number＞|清除保存时间最早的若干个连续配置回退点。输入范围：1-50
缺省 : 
无 
使用说明 : 
无 
范例 : 
(1) 清除所有的配置回退点ZXROSNG#clear configuration commit(2) 清除保存时间最早的2个连续配置回退点ZXROSNG#clear configuration commit  earliest 2
相关命令 : 
show configuration commit listshow configuration commit changes 
## commit 

commit 
命令功能 : 
该命令工作于全局及以上所有配置模式，用于提交未生效的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
commit 
  [comment 
 ＜comment 
＞]
命令参数解释 : 
参数|描述
---|---
＜comment＞|配置提交描述信息。文本类型，长度1-64。
缺省 : 
无 
使用说明 : 
当前配置终端的提交模式为manual时，才需要使用该命令。 
范例 : 
修改提交模式为手动提交：方式1：ZXROSNG#configure terminal manual方式2：ZXROSNG(config)#commit-mode default manualZXROSNG(config)#exitZXROSNG#configure terminal查询提交模式：ZXROSNG(config)#show commit-modeManual commit mode.创建一个smartgroup接口：ZXROSNG(config)#interface smartgroup1查询未提交的命令：ZXROSNG(config-if-smartgroup1)#show configuration candidateinterface smartgroup1提交未生效的配置：ZXROSNG(config-if-smartgroup1)#commit若本终端提交之前，其他终端已经提交了配置，本终端提交时打印提示信息：ZXROSNG(config)#commitThe current configuration has been changed by system or other terminals. The system is checking and trying to resolve the possible conflict.Trying to resolve the possible conflict ... 100%查询提交以后的接口信息：ZXROSNG(config-if-smartgroup1)#show ip interface briefInterface       IP-Address      Mask           Admin Phy  Protmgmt_eth      192.168.0.250   255.255.255.0   up    up   upsmartgroup1    unassigned     unassigned      up    up   down
相关命令 : 
configure terminal  [ {automatic  |  manual} ]commit-mode  default  {manual  |  automatic}
## commit-mode 

commit-mode 
命令功能 : 
该命令工作于全局配置模式，用于设置configure terminal [{automatic | manual}] 命令不带可选参数时，当前命令所在终端的默认提交模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
commit-mode 
 default 
 {manual 
|automatic 
}
命令参数解释 : 
参数|描述
---|---
manual|设置configure terminal [{automatic | manual}] 命令不带可选参数时，当前命令所在终端的默认提交模式为手动提交模式。
automatic|设置configure terminal [{automatic | manual}] 命令不带可选参数时，当前命令所在终端的默认提交模式为自动提交模式。
缺省 : 
automatic 
使用说明 : 
配置设置configure terminal [{automatic | manual}] 命令不带可选参数时，当前命令所在终端的默认提交模式。 
范例 : 
1、设置configure terminal [{automatic | manual}] 命令不带可选参数时，当前命令所在终端的默认提交模式为自动提交模式ZXROSNG(config)#commit-mode default automaticZXROSNG(config)#show running-config mim!<mim>commit-mode default automatic!</mim>2、设置configure terminal [{automatic | manual}] 命令不带可选参数时，当前命令所在终端的默认提交模式为手动提交模式ZXROSNG(config)#commit-mode default manualZXROSNG(config)#show running-config mim!<mim>commit-mode default manual!</mim>
相关命令 : 
show commit-mode 
## configure exclusive 

configure exclusive 
命令功能 : 
该命令工作于特权模式，当用户需要独占配置权时，使用该命令。该命令成功后，其它终端不允许进行命令配置。
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
configure exclusive 
 
no configure exclusive 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用该命令后，当前终端会独占配置权限，其他终端不能进行提交。如果其他终端当前有未提交的配置，这些配置不会自动取消，必须通过命令discard configuration candidate取消。该命令生效后，当用户需要取消配置独占权时，只能在配置configure exclusive命令生效的终端上通过no configure exclusive命令取消。
范例 : 
配置终端的独占权限：ZXROSNG#configure exclusiveZXROSNG#show configure exclusive
Line     User                             Location        Release Lock TimeCLI      zte                              192.168.122.1   00:29:22配置该命令的终端取消独占：ZXROSNG#no configure exclusiveZXROSNG#show configure exclusive
相关命令 : 
show configure exclusive 
## discard configuration candidate 

discard configuration candidate 
命令功能 : 
该命令工作于全局及以上所有配置模式，用于手动提交模式下取消未生效的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
discard configuration candidate 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景终端提交模式为manual时，取消未生效的配置时，可以使用该命令。注意事项该命令工作于全局及以上所有配置模式
范例 : 
1.设置提交模式为手动提交：方式1：ZXROSNG#configure terminal manual方式2：ZXROSNG(config)#commit-mode default manualZXROSNG(config)#exitZXROSNG#configure terminal2.查询提交模式：ZXROSNG(config)#show commit-modeManual commit mode.3.创建一个smartgroup接口：ZXROSNG(config)#interface smartgroup14.查询接口信息：ZXROSNG(config-if-smartgroup1)#show ip interface briefInterface       IP-Address      Mask           Admin Phy  Protmgmt_eth      192.168.0.250   255.255.255.0   up    up   up
5.查询未提交的命令：ZXROSNG(config-if-smartgroup1)#show configuration candidateinterface smartgroup16.取消未生效的配置：ZXROSNG(config-if-smartgroup1)#discard configuration candidateZXROSNG(config)#show ip interface briefInterface       IP-Address      Mask           Admin Phy  Protmgmt_eth      192.168.0.250   255.255.255.0   up    up   up
相关命令 : 
configure terminal  [ {automatic  |  manual} ]commit-mode  default  {manual  |  automatic}show configuration candidate
## lock configuration 

lock configuration 
命令功能 : 
该命令工作于特权模式，用于锁定所有终端的配置权限。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
lock configuration 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令执行成功后，包括本终端在内的所有终端都不允许配置。所有用户都可以解除配置权限。
范例 : 
锁定所有终端的配置权限，根据不同场景提示不同的动态交互提示。当系统中有未生效的配置时，提示为：“Uncommitted configurations found. Are you sure to discard the changes and lock configuration?[yes/no]:”。否则提示为：“Are you sure to lock the system configuration?[yes/no]:”。1、当系统中有未生效的配置时，配置lock configuration提示如下：ZXROSNG#lock configurationUncommitted configurations found. Are you sure to discard the changes and lock configuration?[yes/no]:2、当系统中无未生效的配置时，配置lock configuration提示如下：ZXROSNG#lock configurationAre you sure to lock the system configuration? [yes/no]:
相关命令 : 
1、unlock configuration2、show lock configuration3、和configure exclusive是互斥的
## rollback-configuration 

rollback-configuration 
命令功能 : 
回退功能的开启，关闭以及执行回退。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
rollback-configuration 
  {{enable 
|disable 
}|{last 
 ＜last-num 
＞|to 
 ＜to-id 
＞}}
命令参数解释 : 
参数|描述
---|---
enable|开启保存回退点功能。
disable|关闭回退功能。
＜last-num＞|回退最近的几个连续配置回退点参数范围:1-50
＜to-id＞|回退到指定的配置回退点参数范围：1000000001-1999999999
缺省 : 
回退功能默认关闭。 
使用说明 : 
执行该命令，可以开启回退功能，关闭回退功能，回退最近的几个连续配置回退点，回退到指定的配置回退点 
范例 : 
(1) 回退功能开启ZXROSNG#rollback-configuration enable(2) 回退功能关闭ZXROSNG#rollback-configuration disable(3) 回退最近50个连续配置回退点ZXROSNG#rollback-configuration last 50(4) 回退到指定的配置回退点1000000001ZXROSNG#rollback-configuration to 1000000001
相关命令 : 
show configuration commit listshow configuration commit changes 
## show commit-failed 

show commit-failed 
命令功能 : 
该命令工作于全局及以上所有配置模式，用于显示用户提交失败的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show commit-failed 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令工作于全局及以上所有配置模式，终端提交模式为manual时，才需要使用该命令。自动提交模式下，如果命令提交失败，系统会立即出现提示失败的信息，不需要手动查询；手动提交模式下，在多个命令配置完成后，如果提交命令失败，必须通过该命令查询提交失败是哪个命令。 
范例 : 
1、设置提交模式为手动提交：方式1：ZXROSNG#configure terminal manual方式2：ZXROSNG(config)#commit-mode default manualZXROSNG(config)#exitZXROSNG#configure terminal2、查询提交模式：ZXROSNG(config)#show commit-modeManual commit mode.3、配置IPSEC：ZXROSNG(config)#crypto ipsec manual-profile 456ZXROSNG(config-ipsec-manual-profile)#set session-key inbound ah 256 hex !!!!%Info 24064: The length of the key is too short,it will be padded with 0 to theappropriate size4、提交命令：ZXROSNG(config-ipsec-manual-profile)#commit%Error 24022: The ISAKMP ascii key can only be hex numbers5、查询提交失败的命令：ZXROSNG(config-ipsec-manual-profile)#show commit-failedset session-key inbound ah 256 hex ******
相关命令 : 
configure terminal  [ {automatic  |  manual} ]commit-mode  default  {manual  |  automatic}
## show commit-mode 

show commit-mode 
命令功能 : 
该命令工作于全局及以上所有配置模式，用于显示命令配置的提交模式。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show commit-mode 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令工作于全局及以上所有配置模式，可以显示显示命令配置的提交模式。 
范例 : 
查询命令配置提交模式：ZXROSNG(config)#show commit-mode Manual commit mode.
相关命令 : 
无 
## show configuration candidate 

show configuration candidate 
命令功能 : 
该命令工作于全局及以上所有配置模式，用于显示还没有生效的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration candidate 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令工作于全局及以上所有配置模式，终端的提交模式为manual时，才需要使用该命令。 
范例 : 
1.设置提交模式为手动提交：方式1：ZXROSNG#configure terminal manual方式2：ZXROSNG(config)#commit-mode default manualZXROSNG(config)#exitZXROSNG#configure terminal2.查询提交模式：ZXROSNG(config)#show commit-modeManual commit mode.3.创建一个smartgroup接口：ZXROSNG(config)#interface smartgroup14.查询未提交的命令：ZXROSNG(config-if-smartgroup1)#show configuration candidateinterface smartgroup1
相关命令 : 
configure terminal  [ {automatic  |  manual} ]commit-mode  default  {manual  |  automatic}
## show configuration commit changes 

show configuration commit changes 
命令功能 : 
显示指定配置回退点的业务配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration commit changes 
  {last 
 ＜last-num 
＞|since 
 ＜since-id 
＞|at 
 ＜at-id 
＞} 
命令参数解释 : 
参数|描述
---|---
＜last-num＞|显示最近的几个配置回退点信息。参数范围:1-50
＜since-id＞|显示自配置回退点ID之后的所有配置回退点信息。参数范围：1000000001-1999999999
＜at-id＞|显示某配置回退点信息。参数范围：1000000001-1999999999
缺省 : 
无 
使用说明 : 
无 
范例 : 
(1) 显示保存时间最近的1个配置回退点信息ZXROSNG(config)#show configuration commit changes last 1CommitID: 1000000020DateTime: 03:21:15 Thu May 09 2013Comment: this is testCommand String:interface loopback1interface loopback2(2) 显示ID为1000000020开始的若干个配置回退点信息ZXROSNG(config)#show configuration commit changes since 1000000020CommitID: 1000000020DateTime: 03:21:15 Thu May 09 2013Comment: this is testCommand String:interface loopback1interface loopback2(3)显示ID为 1000000001的配置回退点信息ZXROSNG(config-if-smartgroup3)#show configuration commit changes at 1000000001CommitID: 1000000001  DateTime: 22:37:13 Sat Aug 17 2019  Comment:  Command String:    interface smartgroup3ZXROSNG(config-if-smartgroup3)#CommitID配置回退点ID，在显示时CommitID需要在现有编号（1~999999999）的基础上偏移1000000000，且值随着回退点的增加和删除一直在递增变化，当CommitID递增到1999999999后，后续新增加的编号将从1000000001重新开始DateTime配置回退点的保存时间Comment配置回退点描述信息Command String配置回退点包含的命令信息
相关命令 : 
无 
## show configuration commit list 

show configuration commit list 
命令功能 : 
显示全部回退保存点的概要信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration commit list 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有回退保存点的概要信息ZXROSNG(config)#show configuration commit listNo.    CommitID     User                                Access    DateTime                    Comment1      1000000023   zte                                 CLI       17:45:41 Wed Jun 27 2018No.    回退保存点序号CommitID    回退保存点ID，在显示时CommitID需要在现有编号（1~999999999）的基础上偏移1000000000，且值随着回退点的增加和删除一直在递增变化，当CommitID递增到1999999999后，后续新增加的编号将从1000000001重新开始User     用户名Access     创建回退保存点的终端类型DateTime    回退保存点的保存时间Comment    回退保存点描述信息
相关命令 : 
无 
## show configure exclusive 

show configure exclusive 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于查询独占配置权的终端。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configure exclusive 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示独占配置的信息。 
范例 : 
查询独占配置权的终端：ZXROSNG#show configure exclusiveLine     User                             Location        Release Lock TimeCLI      zte                              192.168.122.1   00:29:22
相关命令 : 
无 
## show lock configuration 

show lock configuration 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于查询锁定了配置权限的用户。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show lock configuration 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示配置锁的信息。 
范例 : 
查询锁定了配置权限的用户：ZXROSNG#show lock configurationUser                               Lock Timezte                                08:57:02 Wed Dec 18 2013
相关命令 : 
无 
## unlock configuration 

unlock configuration 
命令功能 : 
该命令工作于特权模式，用于取消所有终端配置权限的锁定。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
unlock configuration 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
任何用户都可以解除所有终端的配置权限。 
范例 : 
查询锁定了配置权限的用户：ZXROSNG#show lock configuration User                               Lock Timezte                                08:06:07 Thu Dec 19 2013取消所有终端配置权限的锁定：ZXROSNG# unlock configurationZXROSNG#show lock configuration
相关命令 : 
1、lock configuration 2、show lock configuration
# NetFlow配置命令 
## cache 

cache 
命令功能 : 
设置flow monitor下的缓存的特性。使用no命令恢复为默认配置。 
命令模式 : 
 FLOW-MONITOR模式  
命令默认权限级别 : 
15 
命令格式 : 
cache 
  {entries 
 ＜cache-entries 
＞|timeout 
 {active 
 ＜active-timeout 
＞|inactive 
 ＜inactive-timeout 
＞}}
no cache 
  {entries 
|timeout 
 {active 
|inactive 
}}
				
命令参数解释 : 
参数|描述
---|---
＜cache-entries＞|设置缓存的大小为＜cache-entries＞，该缓存能够存储的流的个数，可以设置的范围为0-$#36044802#$，默认值为4096
＜active-timeout＞|设置活跃老化时间，单位：秒，可以设置的范围为$#36044809#$~604800，默认值为1800
＜inactive-timeout＞|设置非活跃老化时间，单位：秒，可以设置的范围为$#36044810#$-604800，默认值为600
No参数|描述
---|---
entries|该monitor能够缓存的最多的流条目数
active|流的活跃老化时间
inactive|流的非活跃老化时间
缺省 : 
见命令参数解释。 
使用说明 : 
当flow monitor应用在接口下时，不能修改cache entries 参数。 
范例 : 
1.配置flow monitor的cache大小、cache的活跃老化时间和cache的非活跃老化时间：ZXROSNG(config)#flow monitor src_and_dst_portZXROSNG(config-flow-monitor)#cache entries 1024ZXROSNG(config-flow-monitor)#cache timeout active 600ZXROSNG(config-flow-monitor)#cache timeout inactive 15
相关命令 : 
flow monitor show ip flow monitor
## clear ip flow statistic cpu 

clear ip flow statistic cpu 
命令功能 : 
清除CPU统计计数 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip flow statistic cpu 
 location 
 ＜cpu-info 
＞
命令参数解释 : 
参数|描述
---|---
＜cpu-info＞|指定需要清除统计计数的CPU物理地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#clear ip flow statistic cpu location PFU-0/1/0ZXROSNG#
相关命令 : 
show ip flow statistic cpu location CPU_INFO 
## clear ip flow statistic exporter 

clear ip flow statistic exporter 
命令功能 : 
清除exporter统计计数 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip flow statistic exporter 
  ＜exporter-name 
＞ location 
 ＜cpu-info 
＞
命令参数解释 : 
参数|描述
---|---
＜exporter-name＞|指定需要清除统计计数的exporter名字，范围：1-32个字符
＜cpu-info＞|指定需要清除统计计数的CPU物理地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#clear ip flow statistic exporter e location PFU-0/1/0ZXROSNG#
相关命令 : 
show ip flow statistic exporter NAME location CPU_INFO 
## clear ip flow statistic monitor 

clear ip flow statistic monitor 
命令功能 : 
清除monitor的统计信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip flow statistic monitor 
  ＜monitor-name 
＞ location 
 ＜cpu-info 
＞
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|指定需要清除统计计数的monitor名字，范围：1-32个字符
＜cpu-info＞|指定需要清除统计计数的CPU物理地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#clear ip flow statistic monitor m location PFU-0/1/0                     ZXROSNG#
相关命令 : 
show ip flow statistic monitor NAME location CPU_INFO 
## collect counter 

collect counter 
命令功能 : 
设置流的报文个数和字节数为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect counter 
  {{bytes 
 [{long 
}]}|{packets 
 [long 
]}}
no collect counter 
  {bytes 
|packets 
}
				
命令参数解释 : 
参数|描述
---|---
bytes|设置流的字节数为采集的非关键字段
long|设置流的报文数为采集的非关键字段，存储该字段的大小为8字节
packets|设置流的包数为采集的非关键字段
long|设置流的报文数为采集的非关键字段，存储该字段的大小为8字节
缺省 : 
无 
使用说明 : 
如果配置流的报文个数和字节数为非关键字段，每条流就会包含此字段信息 
范例 : 
ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect counter bytes longZXROSNG(config-flow-record)# collect counter packets
相关命令 : 
无 
## collect datalink mac 

collect datalink mac 
命令功能 : 
配置源MAC地址或者目的MAC地址为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect datalink mac 
  {destination-address 
|source-address 
}
no collect datalink mac 
  {destination-address 
|source-address 
}
				
命令参数解释 : 
参数|描述
---|---
destination-address|目的MAC地址
source-address|源MAC地址
缺省 : 
无 
使用说明 : 
如果配置目的MAC地址或者源MAC地址为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置目的MAC地址或者源MAC地址为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect datalink mac destination-addressZXROSNG(config-flow-record)# collect datalink mac source-address
相关命令 : 
flow recordshow ip flow record
## collect datalink 

collect datalink 
命令功能 : 
将以太二层信息相关字段作为流的非关键项，使用no命令进行删除。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect datalink 
  {ethernet-total-length 
|ethernet-type 
}
no collect datalink 
  {ethernet-total-length 
|ethernet-type 
}
				
命令参数解释 : 
参数|描述
---|---
ethernet-total-length|以太报文总长度
ethernet-type|以太报文类型
缺省 : 
无 
使用说明 : 
该命令用于采样流的以太报文类型以及包含二层信息的报文总长度，并将它们作为该条流的非关键项。 
范例 : 
1.采集报文的以太类型和以太报文总长度，并将它作为该条流的非关键项ZXROSNG(config)#flow record zteZXROSNG(config-flow-record)#collect datalink ethernet-total-lengthZXROSNG(config-flow-record)#collect datalink ethernet-type2.删除模板中的以太类型和以太报文总长度的非关键项字段ZXROSNG(config)#flow record zteZXROSNG(config-flow-record)#no collect datalink ethernet-total-lengthZXROSNG(config-flow-record)#no collect datalink ethernet-type
相关命令 : 
show running-config ipflowshow ip flow record <recordName>
## collect flow 

collect flow 
命令功能 : 
设置流的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect flow 
  {direction 
|sample-rate 
}
no collect flow 
  {direction 
|sample-rate 
}
				
命令参数解释 : 
参数|描述
---|---
direction|设置流的方向为采集字段
sample-rate|设置采样速率为采集字段
缺省 : 
无 
使用说明 : 
如果配置流的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置流的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect flow directionZXROSNG(config-flow-record)# collect flow sample-rate
相关命令 : 
flow record show ip flow record 
## collect interface 

collect interface 
命令功能 : 
设置入接口索引或者出接口索引为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect interface 
  {input 
|output 
}
no collect interface 
  {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
input|入接口索引
output|出接口索引
缺省 : 
无 
使用说明 : 
如果配置入接口或者出接口索引为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置入接口或者出接口索引为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect interface inputZXROSNG(config-flow-record)# collect interface output
相关命令 : 
flow record  show ip flow record  
## collect ip 

collect ip 
命令功能 : 
设置IP的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect ip 
  {protocol 
|version 
|cos 
}
no collect ip 
  {protocol 
|version 
|cos 
}
				
命令参数解释 : 
参数|描述
---|---
protocol|设置IP报文头部的protocol字段为采集字段
version|设置IP报文头部的version字段为采集字段
cos|对于IPv4报文，取IPv4报文头中的TOS字段为采集字段，对于IPv6报文，取IPv6报文头中的traffic class字段为采集字段。
缺省 : 
无 
使用说明 : 
如果配置IP的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置IP的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect ip protocolZXROSNG(config-flow-record)# collect ip cosZXROSNG(config-flow-record)# collect ip version
相关命令 : 
flow record show ip flow record 
## collect ipv4 destination 

collect ipv4 destination 
命令功能 : 
设置IPv4的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect ipv4 destination 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜destination-minimum-mask 
＞}}
no collect ipv4 destination 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置目的IP地址为采集字段
address-mask|指定目的IP地址的子网掩码为采集字段
address-prefix|指定目的IP地址前缀为采集字段
＜destination-minimum-mask＞|指定长度，范围为1~32
缺省 : 
无 
使用说明 : 
如果配置IPv4的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置IPv4的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect ipv4 destination addressZXROSNG(config-flow-record)# collect ipv4 destination address-prefix minimum-mask 16
相关命令 : 
flow recordshow ip flow record
## collect ipv4 source 

collect ipv4 source 
命令功能 : 
设置IPv4的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect ipv4 source 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜source-minimum-mask 
＞}}
no collect ipv4 source 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置源IP地址为采集字段
address-mask|指定源IP地址的子网掩码为采集字段
address-prefix|指定源IP地址前缀为采集字段
＜source-minimum-mask＞|指定长度，范围为1~32
缺省 : 
无 
使用说明 : 
如果配置IPv4的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置IPv4的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect ipv4 source addressZXROSNG(config-flow-record)# collect ipv4 source address-prefix minimum-mask 16
相关命令 : 
flow recordshow ip flow record
## collect ipv6 destination 

collect ipv6 destination 
命令功能 : 
设置IPv6的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect ipv6 destination 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜destination-minimum-mask 
＞}}
no collect ipv6 destination 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置目的IP地址为采集字段
address-mask|指定目的IPv6地址的子网掩码为采集字段
address-prefix|指定目的IP地址前缀为采集字段
＜destination-minimum-mask＞|指定长度，范围为1~128
缺省 : 
无 
使用说明 : 
如果配置IPv6的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
1.配置IPv6的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect ipv6 destination addressZXROSNG(config-flow-record)# collect ipv6 destination address-prefix minimum-mask 16
相关命令 : 
flow recordshow ip flow record
## collect ipv6 source 

collect ipv6 source 
命令功能 : 
设置IPv6的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect ipv6 source 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜source-minimum-mask 
＞}}
no collect ipv6 source 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置源IP地址为采集字段
address-mask|指定源IPv6地址的子网掩码为采集字段
address-prefix|指定源IP地址前缀为采集字段
＜source-minimum-mask＞|指定长度，范围为1~128
缺省 : 
无 
使用说明 : 
如果配置IPv6的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
1.配置IPv6的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect ipv6 source addressZXROSNG(config-flow-record)# collect ipv6 source address-prefix minimum-mask 16
相关命令 : 
flow recordshow ip flow record
## collect ipv6 

collect ipv6 
命令功能 : 
设置IPv6的相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect ipv6 
  {flow-label 
|extension-headers 
}
no collect ipv6 
  {flow-label 
|extension-headers 
}
				
命令参数解释 : 
参数|描述
---|---
flow-label|设置IPv6报文的flow-label为采集字段
extension-headers|设置IPv6报文的扩展头为采集字段
缺省 : 
无 
使用说明 : 
如果配置IPv6的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
1.配置IPv6的相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect ipv6 flow-labelZXROSNG(config-flow-record)# collect ipv6 extension-headers
相关命令 : 
flow record show ip flow record 
## collect mpls 

collect mpls 
命令功能 : 
设置MPLS的信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect mpls 
  {label 
 stack 
 section 
 {1 
|2 
|3 
|4 
|5 
}}
no collect mpls 
  {label 
 stack 
 section 
 {1 
|2 
|3 
|4 
|5 
}}
				
命令参数解释 : 
参数|描述
---|---
1|mpls第1层标签
2|mpls第2层标签
3|mpls第3层标签
4|mpls第4层标签
5|mpls第5层标签
缺省 : 
无 
使用说明 : 
如果配置MPLS报文相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置MPLS报文相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect mpls label stack section 4ZXROSNG(config-flow-record)# collect mpls label stack section 5
相关命令 : 
flow record  show ip flow record  
## collect routing 

collect routing 
命令功能 : 
设置路由相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect routing 
  {bgp 
 {as-number 
 {destination 
|source 
|next-adjacent 
|prev-adjacent 
}|next-hop-address 
 {ipv4 
|ipv6 
}}|next-hop-address 
 {ipv4 
|ipv6 
}}
no collect routing 
  {bgp 
 {as-number 
 {destination 
|source 
|next-adjacent 
|prev-adjacent 
}|next-hop-address 
 {ipv4 
|ipv6 
}}|next-hop-address 
 {ipv4 
|ipv6 
}}
				
命令参数解释 : 
参数|描述
---|---
destination|目的AS号
source|源AS号
next-adjacent|下一个AS号
prev-adjacent|上一个AS号
ipv4|设置下一跳IPv4地址为采集字段
ipv6|设置下一跳IPv6地址为采集字段
ipv4|设置下一跳IPv4地址为采集字段
ipv6|设置下一跳IPv6地址为采集字段
缺省 : 
无 
使用说明 : 
如果配置路由的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置路由相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect routing next-hop-address ipv4ZXROSNG(config-flow-record)# collect routing bgp as-number destinationZXROSNG(config-flow-record)# collect routing bgp as-number sourceZXROSNG(config-flow-record)# collect routing bgp as-number next-adjacentZXROSNG(config-flow-record)# collect routing bgp as-number prev-adjacent
相关命令 : 
flow recordshow ip flow record
## collect timestamp 

collect timestamp 
命令功能 : 
设置流的时间戳为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect timestamp 
  {sys-uptime 
 {first 
|last 
}|absolute 
 {first-millisec 
|last-millisec 
}}
no collect timestamp 
  {sys-uptime 
 {first 
|last 
}|absolute 
 {first-millisec 
|last-millisec 
}}
				
命令参数解释 : 
参数|描述
---|---
first|设置流第一次进入cache的系统上电时间为采集的非关键字段，单位：毫秒
last|设置流最后一次进入cache中被更新的系统上电时间为采集的非关键字段，单位：毫秒
first-millisec|设置流第一次进入cache的绝对时间为采集的非关键字段，单位：毫秒
last-millisec|设置流最后一次进入cache的绝对时间为采集的非关键字段，单位：毫秒
缺省 : 
无 
使用说明 : 
如果配置流的时间戳为非关键字段，每条流就会包含此字段信息。 
范例 : 
配置流的时间戳为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect timestamp sys-uptime firstZXROSNG(config-flow-record)# collect timestamp sys-uptime last
相关命令 : 
flow record  show ip flow record  
## collect transport icmp ipv4 

collect transport icmp ipv4 
命令功能 : 
设置传输层相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect transport icmp ipv4 
  {type 
|code 
}
no collect transport icmp ipv4 
  {type 
|code 
}
				
命令参数解释 : 
参数|描述
---|---
type|设置IPv4 ICMP报文的type字段为采集字段
code|设置IPv4 ICMP报文的code字段为采集字段
缺省 : 
无 
使用说明 : 
如果配置ICPM的相关字段为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置传输层相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect transport icmp ipv4 type
相关命令 : 
flow record show ip flow record 
## collect transport icmp ipv6 

collect transport icmp ipv6 
命令功能 : 
设置传输层相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect transport icmp ipv6 
  {type 
|code 
}
no collect transport icmp ipv6 
  {type 
|code 
}
				
命令参数解释 : 
参数|描述
---|---
type|设置IPv6 ICMP报文的type字段为采集字段
code|设置IPv6 ICMP报文的code字段为采集字段
缺省 : 
无 
使用说明 : 
如果配置传输层的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置传输层相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect transport icmp ipv6 type
相关命令 : 
flow record show ip flow record 
## collect transport 

collect transport 
命令功能 : 
设置传输层相关信息为非关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
collect transport 
  {destination-port 
|source-port 
|tcp 
 flag 
}
no collect transport 
  {destination-port 
|source-port 
|tcp 
 flag 
}
				
命令参数解释 : 
参数|描述
---|---
destination-port|设置TCP/UDP目的端口号为采集字段
source-port|设置TCP/UDP源端口号为采集字段
flag|设置TCP标识为采集字段
缺省 : 
无 
使用说明 : 
如果配置传输层的相关信息为非关键字段，则不允许再配置为关键字段。每条流会包含此字段信息。 
范例 : 
配置传输层相关信息为非关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# collect transport destination-portZXROSNG(config-flow-record)# collect transport tcp flagZXROSNG(config-flow-record)# collect transport source-port
相关命令 : 
flow recordshow ip flow record
## destination vrf 

destination vrf 
命令功能 : 
配置flow exporter的输出地址所属的VPN。如果NetFlow服务器在VPN中，则使用VRF。使用no命令去除该配置。 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
destination vrf 
  ＜vrf-name 
＞
no destination vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|如果NetFlow服务器在VPN中，则使用VRF，设定的VRF名称为1-32个字节
缺省 : 
无 
使用说明 : 
如果配置VRF,必须先配置NetFlow服务器地址，且地址属于此VPN。如果地址是IPv4类型则VRF必须支持IPv4功能，IPv6同样。 
范例 : 
设置一个NetFlow服务器的IP地址及所属的VPN：ZXROSNG(config)#flow exporter v9ZXROSNG(config-flow-exporter)#destination ipv4-address 192.168.1.200ZXROSNG(config-flow-exporter)#destination vrf f1
相关命令 : 
flow exportershow ip flow exporter
## destination 

destination 
命令功能 : 
配置flow exporter的输出地址，使用no命令去除该配置。 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
destination 
  {ipv4-address 
 ＜ipv4-address 
＞|ipv6-address 
 ＜ipv6-address 
＞}
no destination 
命令参数解释 : 
参数|描述
---|---
ipv4-address|设置服务器地址类型为IPv4地址
＜ipv4-address＞|NetFlow服务器的地址，IPv4类型
ipv6-address|设置服务器地址类型为IPv6地址
＜ipv6-address＞|NetFlow服务器的地址，IPv6类型
缺省 : 
无 
使用说明 : 
每个flow exporter只能配置一个destination。no命令会将配置的服务器地址与VRF一并删除。
范例 : 
1.设置一个IPv4类型的NetFlow服务器地址：ZXROSNG(config)#flow exporter v9ZXROSNG(config-flow-exporter)#destination ipv4-address 192.168.1.2002.设置一个IPv6类型的NetFlow服务器地址：ZXROSNG(config)#flow exporter v9ZXROSNG(config-flow-exporter)#destination ipv6-address 2001::5
相关命令 : 
flow exportershow ip flow exporter
## dscp 

dscp 
命令功能 : 
设置dscp值 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
dscp 
  ＜dscp 
＞
no dscp 
命令参数解释 : 
参数|描述
---|---
＜dscp＞|dscp值，默认为0
缺省 : 
0 
使用说明 : 
dscp <dscp> 
范例 : 
ZXROSNG(config)#flow exporter expZXROSNG(config-flow-exporter)#dscp 10
相关命令 : 
flow exporter 
## exporter 

exporter 
命令功能 : 
绑定一个flow exporter。使用no命令去除绑定。 
命令模式 : 
 FLOW-MONITOR模式  
命令默认权限级别 : 
15 
命令格式 : 
exporter 
  ＜exporter-name 
＞
no exporter 
  ＜exporter-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜exporter-name＞|使用一个之前已经配置好的flow exporter
缺省 : 
无 
使用说明 : 
一个flow monitor可以绑定多个flow exporter。如果flow monitor下绑定的任意一个flow exporter使用netflow v5输出协议，则flow monitor必须使用netflow v5预定义模板。 
范例 : 
在flow monitor下使用两个已经存在的flow exporter：ZXROSNG(config)#flow monitor src_and_dst_portZXROSNG(config-flow-monitor)#exporter v9ZXROSNG(config-flow-monitor)#exporter v9_2
相关命令 : 
flow monitor flow exporter  show ip flow monitor 
## export-protocol 

export-protocol 
命令功能 : 
设置NetFlow的输出报文格式，使用no命令恢复默认配置。 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
export-protocol 
  {ipfix 
|netflow-v9 
|netflow-v8 
|netflow-v5 
}
no export-protocol 
命令参数解释 : 
参数|描述
---|---
ipfix|选择ipfix协议输出
netflow-v9|选择netflow-v9协议输出
netflow-v8|选择netflow-v8协议输出
netflow-v5|选择netflow-v5协议输出
缺省 : 
使用netflow v9作为默认输出报文格式。 
使用说明 : 
在使用netflow v5作为输出报文格式时，flow monitor必须关联预定义的netflow v5模板。 
范例 : 
设置flow exporter的输出协议：ZXROSNG(config)#flow exporter v5ZXROSNG(config-flow-exporter)#exporter-protocol netflow-v5
相关命令 : 
flow exporter  show ip flow exporter  
## flow distribution 

flow distribution 
命令功能 : 
指定采样报文的分发策略 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
flow distribution 
 from 
 ＜board-name 
＞ to 
 {self 
|spu 
}
no flow distribution 
 from 
 ＜board-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜board-name＞|指定单板名称
self|分发采样报文到本板处理
spu|分发采样报文到spu处理
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#flow distribution from PFU-0/1 to self ZXROSNG(config)#
相关命令 : 
无 
## flow exporter 

flow exporter 
命令功能 : 
建立一个不存在的flow exporter策略或者进入一个已经存在的flow exporter策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
flow exporter 
  ＜exporter-name 
＞
no flow exporter 
  ＜exporter-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜exporter-name＞|flow exporter名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
flow exporter可以将flow monitor的缓存中的流信息发送给远端的ipflow服务器。一个flow monitor下可以关联多个flow exporter，目前一个flow monitor最多可关联两个flow exporter,一个flow exporter也可以应用在多个flow monitor下。 
范例 : 
创建一个名称为collector1的flow exporter，并进入flow exporter配置模式：ZXROSNG(config)#flow exporter collector1ZXROSNG(config-flow-exporter)#
相关命令 : 
show ip flow exporter 
## flow monitor 

flow monitor 
命令功能 : 
建立一个不存在的flow monitor策略或者进入一个已经存在的flow monitor策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
flow monitor 
  ＜monitor-name 
＞
no flow monitor 
  ＜monitor-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|flow monitor名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
ipflow将flow monitor应用在接口上进行流量监测。flow monitor包含了一个模板和一个缓存。缓存在flow monitor第一次应用在接口上时生成。监测到的流量信息按照模板中采样字段的定义存放在flow monitor的缓存中。 
范例 : 
创建一个名称为ip-tos的flow monitor，并进入flow monitor配置模式：ZXROSNG(config)#flow monitor ip-tosZXROSNG(config-flow-monitor)#
相关命令 : 
show ip flow monitor 
## flow record 

flow record 
命令功能 : 
建立一个不存在的flow record策略或者进入一个已经存在的flow record策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
flow record 
  ＜record-name 
＞
no flow record 
  ＜record-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜record-name＞|flow record名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
flow record创建一个模板为flow monitor所用。模板包含了关键采样字段和非关键采样字段。类似于netflow v5报文格式规定了7元组为流的定义，模板可以灵活地指定关键采样字段来定义一条流，所有关键字段相同的报文被认为属于同一条流。 
范例 : 
创建一个名称为ip-tos的flow record，并进入flow record配置模式：ZXROSNG(config)#flow record ip-tosZXROSNG(config-flow-record)#
相关命令 : 
show ip flow record  
## ip flow flowspec global 

ip flow flowspec global 
命令功能 : 
对公网VPN流量进行采样，使用no命令删除该采样配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow flowspec global 
 monitor 
 ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞]
no ip flow flowspec global 
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|绑定的monitor名称，1-32个字符。
＜sampler-name＞|采样配置名称，1-32个字符。
缺省 : 
若未显示指定sampler,则按1000:1进行采样。 
使用说明 : 
使用该配置对公网VPN流量进行采样。 
范例 : 
1.对全局流量进行采样ZXROSNG(config)#ip flow flowspec global monitor zte sampler zte2.删除全局流量进行采样配置ZXROSNG(config)#no ip flow flowspec global
相关命令 : 
show running-config ipflow 
## ip flow flowspec vrf 

ip flow flowspec vrf 
命令功能 : 
该命令用于对特定VPN流量进行采样，使用no命令删除该采样配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow flowspec vrf 
  ＜vrf-name 
＞ monitor 
 ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞]
no ip flow flowspec vrf 
  ＜vrf-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf名称
＜monitor-name＞|该vrf上绑定的monitor名称，长度1-32个字符
＜sampler-name＞|该vrf上绑定的sampler,长度1-32个字符
缺省 : 
若未显式指定sampler,则默认使用1000:1采样。 
使用说明 : 
该命令用于对私网内的特定VPN流量进行采样 
范例 : 
1.对vrf zte进行采样ZXROSNG(config)#ip flow flowspec vrf zte monitor zte sampler zte2.删除flow spec采样配置ZXROSNG(config)#no ip flow flowspec vrf zte
相关命令 : 
show running-config ipflow 
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 千兆以太接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 pos接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 multilink接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 smartgroup子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 smartgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 supervlan接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {unicast 
|ipv4-access-list 
 ＜acl-name 
＞} {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {unicast 
|ipv4-access-list 
 ＜acl-name 
＞} {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 posgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ip flow monitor 

ip flow monitor 
命令功能 : 
在接口上设置对IPv4报文的采样。使用no命令去除采样。 
命令模式 : 
 10G以太接口模式,dialer接口模式,e1接口模式,serial接口模式,以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
通道化ce1接口模式:15,serial接口模式:15,e1接口模式:15,通道化cpos_e1接口模式:15,dialer接口模式:15,10G以太接口模式:15,以太接口模式:15 
命令格式 : 
ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ip flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv4-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
multicast|配置采样报文的类型：对组播报文进行采样
unicast|配置采样报文的类型：对单播报文进行采样
ipv4-access-list|配置采样报文的类型：对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口posgroup1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口posgroup2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if)#ip flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ip flow monitor v5 outputZXROSNG(config)#interface posgroup2ZXROSNG(config-if)#ip flow monitor v5 ipv4-access-list src_port_equa_22 input
相关命令 : 
flow monitorsamplershow ip flow monitor
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 10G以太接口模式,dialer接口模式,e1接口模式,serial接口模式,以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
以太接口模式:15,10G以太接口模式:15,dialer接口模式:15,通道化cpos_e1接口模式:15,e1接口模式:15,serial接口模式:15,通道化ce1接口模式:15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 千兆以太接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 pos接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜AclName 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜AclName 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜AclName＞|配置acl名称
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 multilink接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 smartgroup子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 smartgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 supervlan接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## ipv6 flow monitor 

ipv6 flow monitor 
命令功能 : 
在接口上设置对IPv6报文的采样。使用no命令去除采样。 
命令模式 : 
 posgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
no ipv6 flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] [{multicast 
|unicast 
|ipv6-access-list 
 ＜acl-name 
＞}] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
multicast|配置采样报文的类型，对单播报文进行采样
unicast|配置采样报文的类型，对组播报文进行采样
ipv6-access-list|配置采样报文的类型，对被ACL规则过滤的报文进行采样
＜acl-name＞|指定的ACL规则
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。如果不指定采样类型，则默认对单播和组播同时采样。 
使用说明 : 
当对经过ACL规则过滤的报文进行采样时，最多可以使用6个不同的ACL规则。如果在一个接口的一个方向上应用了ACL，则不能再配置单播和组播采样，如果在该方向上配置了多个ACL，则这些ACL必须对应同一个flow monitor。 
范例 : 
在接口fei-0/1/0/1的入方向上配置单播采样，在出方向上配置单播和组播采样，在接口fei-0/1/0/2的入方向上对用ACL规则过滤的报文进行采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#ipv6 flow monitor src_and_dst_port sampler rate2000 unicast inputZXROSNG(config-if)#ipv6 flow monitor v5 outputZXROSNG(config)#interface fei-0/1/0/2ZXROSNG(config-if)#ipv6 flow monitor v5 acl src_port_equa_22 input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## match datalink mac 

match datalink mac 
命令功能 : 
设置目的MAC地址或者源MAC地址为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match datalink mac 
  {destination-address 
|source-address 
}
no match datalink mac 
  {destination-address 
|source-address 
}
				
命令参数解释 : 
参数|描述
---|---
destination-address|目的MAC地址
source-address|源MAC地址
缺省 : 
无 
使用说明 : 
如果配置目的MAC地址或者源MAC地址为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置目的MAC或者源MAC地址为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match datalink mac destination-addressZXROSNG(config-flow-record)# match datalink mac source-address
相关命令 : 
flow recordshow ip flow record
## match datalink 

match datalink 
命令功能 : 
设置二层链路相关信息为关键字段，使用no命令删除。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match datalink 
  {ethernet-type 
|ethernet-total-length 
}
no match datalink 
  {ethernet-type 
|ethernet-total-length 
}
				
命令参数解释 : 
参数|描述
---|---
ethernet-type|以太报文类型
ethernet-total-length|以太报文总长度
缺省 : 
无 
使用说明 : 
该命令主要用于将以太报文类型及以太报文长度作为流的关键项 
范例 : 
1.将以太帧类型和以太报文总长度作为关键项ZXROSNG(config)#flow record zteZXROSNG(config-flow-record)#match datalink ethernet-total-lengthZXROSNG(config-flow-record)#match datalink ethernet-type2.删除record中的以太帧类型和以太报文长度关键项ZXROSNG(config)#flow record zteZXROSNG(config-flow-record)#no match datalink ethernet-total-lengthZXROSNG(config-flow-record)#no match datalink ethernet-type
相关命令 : 
show running-config ipflowshow ip flow record <recordName>
## match flow 

match flow 
命令功能 : 
设置流的相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match flow 
  {direction 
|sample-rate 
}
no match flow 
  {direction 
|sample-rate 
}
				
命令参数解释 : 
参数|描述
---|---
direction|设置流的方向为采集字段
sample-rate|设置采样速率为采集字段
缺省 : 
无 
使用说明 : 
如果配置流的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置流方向或采样速率为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match flow directionZXROSNG(config-flow-record)# match flow sample-rate
相关命令 : 
flow recordshow ip flow record
## match interface 

match interface 
命令功能 : 
设置入接口索引或者出接口索引为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match interface 
  {input 
|output 
}
no match interface 
  {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
input|入接口索引
output|出接口索引
缺省 : 
无 
使用说明 : 
如果配置入接口索引或者出接口索引为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置入接口或者出接口索引为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match interface inputZXROSNG(config-flow-record)# match interface output
相关命令 : 
flow record show ip flow record 
## match ip 

match ip 
命令功能 : 
设置IP的相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match ip 
  {protocol 
|version 
|cos 
}
no match ip 
  {protocol 
|version 
|cos 
}
				
命令参数解释 : 
参数|描述
---|---
protocol|设置IP报文头部的protocol字段为采集字段
version|设置IP报文头部的version字段为采集字段
cos|对于IPv4报文，取IPv4报文头中的TOS字段为采集字段，对于IPv6报文，取IPv6报文头中的traffic class字段为采集字段
缺省 : 
无 
使用说明 : 
如果配置IP的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置IP的相关信息为关键字段为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match ip protocolZXROSNG(config-flow-record)# match ip cosZXROSNG(config-flow-record)# match ip version
相关命令 : 
flow recordshow ip flow record
## match ipv4 destination 

match ipv4 destination 
命令功能 : 
设置IPv4的相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv4 destination 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜destination-minimum-mask 
＞}}
no match ipv4 destination 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置目的IP地址为采集字段
address-mask|指定目的IPv4地址的子网掩码为采集字段
address-prefix|指定目的IP地址前缀为采集字段
＜destination-minimum-mask＞|设置长度，范围为1~32
缺省 : 
无 
使用说明 : 
如果配置IPv4的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置IPv4的相关信息为关键字段为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match ipv4 destination address
相关命令 : 
flow record show ip flow record 
## match ipv4 source 

match ipv4 source 
命令功能 : 
设置IPv4的相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv4 source 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜source-minimum-mask 
＞}}
no match ipv4 source 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置源IP地址为采集字段
address-mask|指定源IPv4地址的子网掩码为采集字段
address-prefix|指定源IP地址前缀为采集字段
＜source-minimum-mask＞|设置长度，范围为1~32
缺省 : 
无 
使用说明 : 
如果配置IPv4的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置IPv4的相关信息为关键字段为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match ipv4 source addressZXROSNG(config-flow-record)# match ipv4 source address-prefix minimum-mask 16
相关命令 : 
flow record show ip flow record 
## match ipv6 destination 

match ipv6 destination 
命令功能 : 
设置IPv6的相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 destination 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜destination-minimum-mask 
＞}}
no match ipv6 destination 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置目的IPv6地址为采集字段
address-mask|指定目的IPv6地址的子网掩码为采集字段
address-prefix|指定目的IPv6地址前缀为采集字段
＜destination-minimum-mask＞|设置长度，范围为1~128
缺省 : 
无 
使用说明 : 
如果配置IPv6的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
1.配置IPv6的相关信息为关键字段为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match ipv6 destination address
相关命令 : 
flow record show ip flow record 
## match ipv6 source 

match ipv6 source 
命令功能 : 
设置IPv6的相关信息为关键字段。使用no命令去除配置 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 source 
  {address 
|address-mask 
|address-prefix 
 {minimum-mask 
 ＜source-minimum-mask 
＞}}
no match ipv6 source 
  {address 
|address-mask 
|address-prefix 
}
				
命令参数解释 : 
参数|描述
---|---
address|设置源IPv6地址为采集字段
address-mask|指定源IPv6地址的子网掩码作为采集字段
address-prefix|指定源IPv6地址前缀为采集字段
＜source-minimum-mask＞|设置长度，范围为1~128
缺省 : 
无 
使用说明 : 
如果配置IPv6的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
1.配置IPv6的相关信息为关键字段为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match ipv6 source address
相关命令 : 
flow record  show ip flow record  
## match ipv6 

match ipv6 
命令功能 : 
设置IPv6的相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match ipv6 
  {flow-label 
|extension-headers 
}
no match ipv6 
  {flow-label 
|extension-headers 
}
				
命令参数解释 : 
参数|描述
---|---
flow-label|设置IPv6报文的flow-label为采集字段
extension-headers|设置IPv6报文的扩展头为采集字段
缺省 : 
无 
使用说明 : 
如果配置IPv6的相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
1.配置IPv6的相关信息为关键字段为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match ipv6 flow-labelZXROSNG(config-flow-record)# collect ipv6 extension-headers
相关命令 : 
flow recordshow ip flow record
## match mpls 

match mpls 
命令功能 : 
设置MPLS的信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match mpls 
  {label 
 stack 
 section 
 {1 
|2 
|3 
|4 
|5 
}}
no match mpls 
  {label 
 stack 
 section 
 {1 
|2 
|3 
|4 
|5 
}}
				
命令参数解释 : 
参数|描述
---|---
1|MPLS报文第1层标签
2|MPLS报文第2层标签
3|MPLS报文第3层标签
4|MPLS报文第4层标签
5|MPLS报文第5层标签
缺省 : 
无 
使用说明 : 
如果配置MPLS报文相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置MPLS报文相关信息为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match mpls label stack section 1 ZXROSNG(config-flow-record)# match mpls label stack section 2ZXROSNG(config-flow-record)# match mpls label stack section 3
相关命令 : 
flow record show ip flow record 
## match routing 

match routing 
命令功能 : 
设置路由相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match routing 
  {bgp 
 {as-number 
 {destination 
|source 
|next-adjacent 
|prev-adjacent 
}|next-hop-address 
 {ipv4 
|ipv6 
}}|next-hop-address 
 {ipv4 
|ipv6 
}}
no match routing 
  {bgp 
 {as-number 
 {destination 
|source 
|next-adjacent 
|prev-adjacent 
}|next-hop-address 
 {ipv4 
|ipv6 
}}|next-hop-address 
 {ipv4 
|ipv6 
}}
				
命令参数解释 : 
参数|描述
---|---
destination|目的AS号
source|源AS号
next-adjacent|下一个AS号
prev-adjacent|上一个AS号
ipv4|设置下一跳IPv4地址为采集字段
ipv6|设置下一跳IPv6地址为采集字段
ipv4|设置下一跳IPv4地址为采集字段
ipv6|设置下一跳IPv6地址为采集字段
缺省 : 
无 
使用说明 : 
如果配置路由相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置路由相关信息为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match routing next-hop-address ipv4ZXROSNG(config-flow-record)# match routing bgp as-number destinationZXROSNG(config-flow-record)# match routing bgp as-number sourceZXROSNG(config-flow-record)# match routing bgp as-number next-adjacentZXROSNG(config-flow-record)# match routing bgp as-number prev-adjacent
相关命令 : 
flow record show ip flow record 
## match transport icmp ipv4 

match transport icmp ipv4 
命令功能 : 
设置传输层相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match transport icmp ipv4 
  {type 
|code 
}
no match transport icmp ipv4 
  {type 
|code 
}
				
命令参数解释 : 
参数|描述
---|---
type|设置IPv4 ICMP报文的type字段为采集字段
code|设置IPv4 ICMP报文的code字段为采集字段
缺省 : 
无 
使用说明 : 
如果配置传输层相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置传输层相关信息为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match transport icmp ipv4 type
相关命令 : 
flow record   
## match transport icmp ipv6 

match transport icmp ipv6 
命令功能 : 
设置传输层相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match transport icmp ipv6 
  {type 
|code 
}
no match transport icmp ipv6 
  {type 
|code 
}
				
命令参数解释 : 
参数|描述
---|---
type|设置IPv6 ICMP报文的type字段为采集字段
code|设置IPv6 ICMP报文的code字段为采集字段
缺省 : 
无 
使用说明 : 
如果配置传输层相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置传输层相关信息为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match transport icmp ipv6 type
相关命令 : 
flow record  show ip flow record  
## match transport 

match transport 
命令功能 : 
设置传输层相关信息为关键字段。使用no命令去除配置。 
命令模式 : 
 FLOW-RECORD模式  
命令默认权限级别 : 
15 
命令格式 : 
match transport 
  {destination-port 
|source-port 
|tcp 
 flag 
}
no match transport 
  {destination-port 
|source-port 
|tcp 
 flag 
}
				
命令参数解释 : 
参数|描述
---|---
destination-port|设置TCP/UDP目的端口号为采集字段
source-port|设置TCP/UDP源端口号为采集字段
flag|设置TCP标识为采集字段
缺省 : 
无 
使用说明 : 
如果配置传输层相关信息为区分一条流的关键字段，则不允许再配置为非关键字段。 
范例 : 
配置传输层相关信息为关键字段：ZXROSNG(config)#flow record v9ZXROSNG(config-flow-record)# match transport destination-portZXROSNG(config-flow-record)# match transport igmp typeZXROSNG(config-flow-record)# match transport source-port
相关命令 : 
flow record show ip flow record 
## mode 

mode 
命令功能 : 
设置采样方式和采样率。使用no命令恢复为默认配置。 
命令模式 : 
 SAMPLER模式  
命令默认权限级别 : 
15 
命令格式 : 
mode 
  {deterministic 
} 1-out-of 
 ＜rate 
＞
no mode 
命令参数解释 : 
参数|描述
---|---
deterministic|设置采样方式为非随机采样，即如果采样率为N，则每N个报文采样1个
＜rate＞|设置采样速率，范围：$#36044807#$-$#36044808#$
缺省 : 
采样率默认值为1000。 
使用说明 : 
目前只提供非随机采样方式。 
范例 : 
设置sampler的采样方式和采样速率：ZXROSNG(config)# sampler rate2009ZXROSNG(config-sampler)# mode deterministic 1-out-of 2000
相关命令 : 
samplershow ip flow sampler
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 10G以太接口模式,dialer接口模式,e1接口模式,serial接口模式,以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
以太接口模式:15,10G以太接口模式:15,dialer接口模式:15,通道化cpos_e1接口模式:15,e1接口模式:15,serial接口模式:15,通道化ce1接口模式:15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 千兆以太接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 pos接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜MonitorName 
＞ [sampler 
 ＜SamplerName 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜MonitorName 
＞ [sampler 
 ＜SamplerName 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜MonitorName＞|在接口下使用一个之前已经配置好的flow monitor，长度为1~32个字符
＜SamplerName＞|在接口下使用一个之前已经配置好的sampler，长度为1~32个字符
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 multilink接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 smartgroup子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 以太子接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 smartgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## mpls flow monitor 

mpls flow monitor 
命令功能 : 
在接口上设置对MPLS报文的采样。使用no命令去除采样。 
命令模式 : 
 posgroup接口模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
no mpls flow monitor 
  ＜monitor-name 
＞ [sampler 
 ＜sampler-name 
＞] {input 
|output 
}
				
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|在接口下使用一个之前已经配置好的flow monitor
＜sampler-name＞|在接口下使用一个之前已经配置好的sampler
input|对入方向报文进行采样
output|对出方向报文进行采样
缺省 : 
如果不关联一个sampler，则默认使用非随机采样，采样率为1000：1。 
使用说明 : 
对于MPLS报文，只支持单播报文采样。 
范例 : 
在接口fei-0/1/0/1的入方向上配置MPLS报文采样：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if)#mpls flow monitor src_and_dst_port sampler rate2000 unicast input
相关命令 : 
flow monitor sampler  show ip flow monitor 
## record 

record 
命令功能 : 
绑定一个flow record。使用no命令去除绑定。 
命令模式 : 
 FLOW-MONITOR模式  
命令默认权限级别 : 
15 
命令格式 : 
record 
  {netflow 
 {protocol-port 
|ipv4 
 {original-input 
|original-output 
}}|netflow-original 
|＜record-name 
＞}
no record 
命令参数解释 : 
参数|描述
---|---
protocol-port|预定义netflow-v8模板
original-input|预定义netflow-v5模板，采集的关键字段和非关键字段与netflow v5保持一致
original-output|它与orginal-input的区别在于，它使用出方向的接口索引作为采集的关键字段，入方向的接口索引为非关键字段
netflow-original|预定义netflow-v5模板，采集的关键字段和非关键字段与netflow v5保持一致
＜record-name＞|使用一个之前已经配置好的flow record作为模板
缺省 : 
无 
使用说明 : 
当flow monitor应用在接口下时，不能关联其它的flow record或者去除关联，也不能增加或者删除flow record下的采集字段。一个flow monitor只能绑定一个flow record。 
范例 : 
在一个flow monitor下引用一个flow record：ZXROSNG(config)#flow monitor src_and_dst_portZXROSNG(config-flow-monitor)#record src_and_dst_port
相关命令 : 
flow monitor flow record  show ip flow monitor
## sampler 

sampler 
命令功能 : 
建立一个不存在的sampler策略或者进入一个已经存在的sampler策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sampler 
  ＜sampler-name 
＞
no sampler 
  ＜sampler-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜sampler-name＞|sampler名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
为了降低监测网络流量所带来的系统负荷，ipflow使用采样的方式进行网络流量监测。将sampler应用在接口上后，经过该接口的转发报文将按照sampler所制定的采样方式和采样速率进行采样。 
范例 : 
创建一个名称为sam1024的sampler，并进入sampler配置模式：ZXROSNG(config)#sampler sam1024ZXROSNG(config-sampler)#
相关命令 : 
show ip flow sampler 
## show ip flow distribution 

show ip flow distribution 
命令功能 : 
显示采样报文分配策略 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow distribution 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show ip flow distribution Default Flow Processor:          spuAuto Change To Self Processor:   YFlow Distribution Table:board-name           flow-processorPFU-0/1              selfZXROSNG(config)#
相关命令 : 
flow distribution 
## show ip flow exporter 

show ip flow exporter 
命令功能 : 
查看指定名字的flow exporter或者查看所有的flow exporter。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow exporter 
  [＜exporter-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜exporter-name＞|可选参数，如果不加该参数，则显示所有的flow exporter，否则显示指定名称的flow exporter
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有的flow exporter配置：ZXROSNG(config)#show ip flow exporter Name      ExpProt DstIPAddr TransProt DstPort VRF TplTimeout TplRef SrcIPAddrv9        9                    UDP        9995         600         1      v5        5                    UDP        9995         600         5      显示指定的flow exporter配置(config)#show ip flow exporter v5 flow exporter v5   export protocol:  5  template timeout: 600  template refresh: 5  destination IP Addr:   source IP Addr:   transport protocol: UDP  destination port: 9995  VRF name:       user: test
相关命令 : 
无 
## show ip flow interface 

show ip flow interface 
命令功能 : 
查看指定名字的接口配置或者查看所有的接口配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow interface 
  [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|可选参数，如果不加该参数，则显示所有的接口配置，否则显示指定名称的接口配置
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有的接口配置：ZXROSNG(config)#show ip flow interfaceinterface gei-0/1/0/1sample protocol: ipv4  sample castType: unicast  acl:     sample dir: output  monitor: test  samplerName: rate2000           sample protocol: mpls  sample castType: unicast  acl:     sample dir: input  monitor: test  samplerName:            sample protocol: ipv4  sample castType: unicast & multicast  acl:     sample dir: input  monitor: src_and_dst_addr  samplerName:            sample protocol: ipv6  sample castType: unicast & multicast  acl:     sample dir: input  monitor: ipv6  samplerName: interface gei-0/20/0/1sample protocol: ipv4  sample castType: acl  acl: port27-28  sample dir: input  monitor: src_and_dst_addr  samplerName:   sample protocol: ipv4  sample castType: acl  acl: src1.2.3.4  sample dir: output  monitor: test  samplerName:   sample protocol: ipv4  sample castType: acl  acl: dst4.3.2.1  sample dir: output  monitor: test  samplerName:   sample protocol: ipv6  sample castType: unicast & multicast  acl:     sample dir: output  monitor: ipv6  samplerName:          显示指定的接口配置：ZXROSNG(config)#show ip flow interface gei-0/1/0/1interface gei-0/1/0/1sample protocol: ipv4  sample castType: unicast  acl:   sample dir: output  monitor: test  samplerName: rate2000  sample protocol: mpls  sample castType: unicast  acl:   sample dir: input  monitor: test  samplerName:   sample protocol: ipv4  sample castType: unicast & multicast  acl:   sample dir: input  monitor: src_and_dst_addr  samplerName:   sample protocol: ipv6  sample castType: unicast & multicast  acl:     sample dir: input  monitor: ipv6  samplerName: 
相关命令 : 
无 
## show ip flow monitor 

show ip flow monitor 
命令功能 : 
查看指定名字的flow monitor或者查看所有的flow monitor。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow monitor 
  [＜monitor-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|可选参数，如果不加该参数，则显示所有的flow monitor，否则显示指定名称的flow monitor
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有的flow monitor配置：ZXROSNG(config)#show ip flow monitorName      CacheEntries CacheActiveTout CacheInactiveTout Record    exportersrc_and_d  4096         1800              1800                 v9st_addr                                                            test        4096         1800              1800                 P: netflow-  v5original 显示指定的flow monitor配置：(config)#show ip flow monitor testflow monitor test   cache entries: 4096  cache active timeout: 1800  cache inactive timeout: 1800  record: P: netflow-original  exporter: v5   user:
相关命令 : 
无 
## show ip flow record 

show ip flow record 
命令功能 : 
查看指定名字的flow record或者预定义的flow record或者查看所有的用户自定义的flow record。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow record 
  [{netflow-original 
|netflow 
 {protocol-port 
|ipv4 
 {original-input 
|original-output 
}}|＜record-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
netflow-original|显示预定义的格式为netflow-original的flow record
protocol-port|显示预定义的v8 protocol-port模板
original-input|显示预定义的格式为original-input的flow record
original-output|显示预定义的格式为original-output的flow record
＜record-name＞|显示指定名称的flow record
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有的flow record配置：ZXROSNG(config)#show ip flow record Name                 KeyFldNum NonKeyFldNumsrc_and_dst_addr     2         7显示指定的flow record配置：ZXROSNG(config)#show ip flow record src_and_dst_addrflow record:  src_and_dst_addrField                           Type Offset Size IsKeysourceIPv4Address               8    0      4    YdestinationIPv4Address         12   4      4    YdestinationMacAddress          57   8      6    NsourceMacAddress                56   14     6    NflowDirection                    61   20     1    NingressInterface                10   21     2    NegressInterface                 14   23     2    NoctetDeltaCount                 1    25     4    NpacketDeltaCount                2    29     4    Nuser: 显示预定义的flow record配置：ZXROSNG(config#show ip flow record netflow-original  flow record:  P: netflow-originalField                           Type Offset Size IsKeysourceIPv4Address               8    0      4    YdestinationIPv4Address         12   4      4    YsourceTransportPort             7    8      2    YdestinationTransportPort       11   10     2    YprotocolIdentifier              4    12     1    YipClassOfService                5    13     1    YingressInterface                10   14     2    YegressInterface                 14   16     2    YoctetDeltaCount                 1    18     4    NpacketDeltaCount                2    22     4    NflowEndSysUpTime                21   26     4    NflowStartSysUpTime              22   30     4    NipNextHopIPv4Address            15   34     4    NsourceIPv4PrefixLength          9    38     1    NdestinationIPv4PrefixLength    13   39     1    NbgpSourceAsNumber                16   40     2    NbgpDestinationAsNumber          17   42     2    NtcpControlBits                    6    44     1    N
相关命令 : 
无 
## show ip flow sampler 

show ip flow sampler 
命令功能 : 
查看指定名字的sampler或者查看所有的sampler。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow sampler 
  [＜sampler-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜sampler-name＞|可选参数，如果不加该参数，则显示所有的sampler，否则显示指定名称的sampler
缺省 : 
无 
使用说明 : 
该命令后面若不带任何sampler，则可以用来显示所有sampler的配置，若带上sampler名称，可以显示该sampler的详细配置，对于不存在的sampler，则无任何显示。 
范例 : 
1.显示所有的sampler配置：ZXROSNG(config)#show ip flow sampler=============Algorithm: deterministic=============Name                                    Sample-Ratezte                                     22.显示指定的sampler配置：ZXROSNG(config)#show ip flow sampler ztesampler zte  Algorithm: deterministic  Rate: 2  TimeSpace: N/A  RandomSize: N/A  RandomPopulation: N/A  User: fei-0/1/0/8
相关命令 : 
无 
## show ip flow service-cpu 

show ip flow service-cpu 
命令功能 : 
显示使能ipflow功能的业务cpu 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow service-cpu 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show ip flow service-cpuNo.   CPU-INFO0     SPU-0/1/01     SPU-0/1/1
相关命令 : 
无 
## show ip flow statistic cpu 

show ip flow statistic cpu 
命令功能 : 
显示指定CPU的报文统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow statistic cpu 
 location 
 ＜cpu-addr 
＞ 
命令参数解释 : 
参数|描述
---|---
＜cpu-addr＞|指定需要显示统计计数的CPU信息
缺省 : 
无 
使用说明 : 
无 
范例 : 
show ip flow statistic cpu location PFU-0/1/0                            IPv4 ingress packets:  747IPv4 egress packets:  0IPv6 ingress packets:  0IPv6 egress packets:  0MPLS ingress packets:  0MPLS egress packets:  0Other ingress packets:  0Other egress packets:  0Drop packets(fail to parse packet):  0Drop packets(other):  0
相关命令 : 
clear ip flow statistic cpu location CPU_INFO 
## show ip flow statistic exporter 

show ip flow statistic exporter 
命令功能 : 
显示exporter统计计数 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow statistic exporter 
  ＜exporter-name 
＞ location 
 ＜cpu-addr 
＞ 
命令参数解释 : 
参数|描述
---|---
＜exporter-name＞|指定需要显示统计计数的exporter名字，范围：1-32个字符
＜cpu-addr＞|指定需要显示统计计数的CPU信息
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show ip flow statistic exporter e location PFU-0/1/0Messages transmitted:       84(12340 bytes)Messages discarded:         0(0 bytes)Data records transmitted:   55Template transmitted:       35Export rate over last interval of:   5 minute:   20 Bps(0 pps)   1 hour:   3 Bps(0 pps)ZXROSNG#
相关命令 : 
clear ip flow statistic exporter NAME location CPU_INFO 
## show ip flow statistic monitor 

show ip flow statistic monitor 
命令功能 : 
显示monitor统计计数 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip flow statistic monitor 
  ＜monitor-name 
＞ location 
 ＜cpu-addr 
＞ 
命令参数解释 : 
参数|描述
---|---
＜monitor-name＞|指定需要显示统计计数的monitor名字，范围：1-32个字符
＜cpu-addr＞|指定需要显示统计计数的CPU信息
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show ip flow statistic monitor m location PFU-0/1/0                      Maximum cache entries:  4096Alloced cache entries:  3Active cache entries:   2Aged data records:      0  --Active timeout:        60  --Inactive timeout:      1  --Emergency aged:        0  --Counter wraped aged:   0  --Force aged:            0
相关命令 : 
clear ip flow statistic monitor NAME location CPU_INFO 
## source 

source 
命令功能 : 
设置exporter的源地址 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
source 
  {ipv4-address 
 ＜ipv4-address 
＞|ipv6-address 
 ＜ipv6-address 
＞|interface 
 ＜interface-name 
＞}
no source 
命令参数解释 : 
参数|描述
---|---
ipv4-address|设置地址类型为IPv4
＜ipv4-address＞|设置Pv4地址
ipv6-address|设置地址类型为IPv6
＜ipv6-address＞|设置Pv6地址
interface|设置源接口
＜interface-name＞|指定源接口名称
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#flow exporter v9ZXROSNG(config-flow-exporter)#source ipv4-address 192.168.1.10ZXROSNG(config)#flow exporter v9ZXROSNG(config-flow-exporter)#source ipv6-address 1:1::1:1
相关命令 : 
flow exporter v9 
## template data 

template data 
命令功能 : 
设置模板的重发间隔。使用no命令恢复默认值。 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
template data 
  {timeout 
 ＜timeout 
＞|refresh 
 ＜refresh-rate 
＞}
no template data 
  {timeout 
|refresh 
}
				
命令参数解释 : 
参数|描述
---|---
＜timeout＞|将模板按照时间重发，以秒为单位，范围1~86400
＜refresh-rate＞|将模板按照输出的netflow报文个数进行重复发送，范围1~600
No参数|描述
---|---
timeout|设置netflow模板的刷新周期
refresh|间隔指定个数的netflow数据报文后刷新一次模板
缺省 : 
按照netflow报文个数重发的默认值为20。按照时间重发的默认值为600s。
使用说明 : 
按照报文个数和按照时间重发两个配置会同时生效。 
范例 : 
1.设置模板（flow record）的按包重发速率和按时间的重发间隔：ZXROSNG(config)#flow exporter v9ZXROSNG(config-flow-exporter)#template data refresh 100ZXROSNG(config-flow-exporter)#template data timeout 1800
相关命令 : 
flow exporter show ip flow exporter 
## transport 

transport 
命令功能 : 
设置报文输出端口。 
命令模式 : 
 FLOW-EXPORTER模式  
命令默认权限级别 : 
15 
命令格式 : 
transport 
  {udp 
} ＜port-number 
＞
no transport 
命令参数解释 : 
参数|描述
---|---
udp|指定使用UDP作为传输层协议
＜port-number＞|报文输出端口
缺省 : 
默认端口为2055。 
使用说明 : 
配置的端口号需要与Netflow服务器的端口号保持一致。 
范例 : 
设置报文输出端口：ZXROSNG(config)# flow exporter v9ZXROSNG(config-flow-record)# transport udp 2055
相关命令 : 
flow exporter show ip flow exporter 
# NTP配置命令 
## debug ntp all 

debug ntp all 
命令功能 : 
用于打开打印NTP调试信息的开关，打印NTP调试信息供用户查阅。系统默认不开启此功能。当用户需要查看NTP的调试信息时，使用该命令。命令执行成功后，NTP调试功能开启，打印NTP所有的调试信息。执行no debug ntp all命令关闭NTP调试开关，NTP的调试信息将停止打印。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ntp all 
 
no debug ntp all 
命令参数解释 : 
					无
				 
缺省 : 
不开启NTP调试功能。 
使用说明 : 
• 本设备NTP的调试信息现在只有报文打印。• 系统默认的打印调试信息的时间是10分钟。当NTP 调试功能打开后，过10分钟后打印将自动关闭。
范例 : 
开启(关闭)NTP调试功能：ZXROSNG#debug ntp allAll NTP debugging has been turned onZXROSNG#no debug ntp allAll NTP debugging has been turned off
相关命令 : 
无 
## debug ntp packet 

debug ntp packet 
命令功能 : 
开启NTP收发包调试功能。当NTP不能正常同步，操作人员需要查看NTP时间同步报文信息定位问题时，使用该命令。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ntp packet 
 
no debug ntp packet 
命令参数解释 : 
					无
				 
缺省 : 
不开启NTP收发包调试功能。 
使用说明 : 
系统默认的打印调试信息的时间是10分钟。当NTP 的报文打印开关打开后，过10分钟打印将自动关闭。 
范例 : 
开启(关闭)NTP收发包调试功能：ZXROSNG#debug ntp packetNTP packet debugging is onZXROSNG#no debug ntp allNTP packet debugging is off
相关命令 : 
无 
## ntp access-control serve-vrf 

ntp access-control serve-vrf 
命令功能 : 
为NTP服务器端配置VRF控制。使用no命令取消控制。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp access-control serve-vrf 
  ＜vrf-name 
＞
no ntp access-control serve-vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称
缺省 : 
无 
使用说明 : 
在独立的VRF内支持NTP server，该配置只针对客户端服务器模式的服务器上生效，其它模式下该配置无意义。只支持绑定一个VRF，可以更新和删除。server端支持绑定VRF，限定只有该VRF的客户端报文能通过。 
范例 : 
为服务器端配置VRF名为zte的报文控制规则：ZXROSNG(config)#ntp access-control serve-vrf zte
相关命令 : 
无 
## ntp access-group ipv4-access-list 

ntp access-group ipv4-access-list 
命令功能 : 
为NTP指定IPv4控制列表。使用no命令取消控制。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp access-group ipv4-access-list 
  ＜ipv4-acl-name 
＞
no ntp access-group ipv4-access-list 
命令参数解释 : 
参数|描述
---|---
＜ipv4-acl-name＞|IPv4 ACL名选项
缺省 : 
无 
使用说明 : 
• 本命令配置的是peer ACL过滤，最大访问限制（即client可以对本地NTP服务进行时间请求，本地时钟也可以同步到远程服务器）。• 使用本命令时，需要确认配置的ACL列表名称是否已经在ACL模块中配置，查询命令为：show ipv4-access-lists。如果没有配置，则需要到ACL模式下生成该名称的ACL规则。若ACL名对应的IPv4的过滤规则不存在时，也可以配置该命令，只是功能不生效。• 本命令支持所有NTP工作模式。
范例 : 
配置ACL名为zte的过滤规则生效：ZXROSNG(config)#ntp access-group ipv4-access-list zte
相关命令 : 
无 
## ntp access-group ipv4-serve-only 

ntp access-group ipv4-serve-only 
命令功能 : 
为NTP指定server ACL过滤IPv4控制列表。使用no命令取消控制 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp access-group ipv4-serve-only 
  ＜ipv4-acl-name 
＞
no ntp access-group ipv4-serve-only 
命令参数解释 : 
参数|描述
---|---
＜ipv4-acl-name＞|IPv4 ACL名
缺省 : 
无 
使用说明 : 
• server ACL过滤，只允许对本地NTP服务进行时间请求（即只允许本设备做服务器）。•  使用本命令时，需要确认配置的ACL列表名称是否已经在ACL模块中配置，查询命令为：show ipv4-access-lists。如果没有，也可以配置该命令。若要功能生效（不允许其它设备同步本设备时间），则需要到ACL模式下生成该名称的ACL规则。• NTP ACL过滤按照最大访问限制到最小访问限制依次匹配，若配置过peer ACL最大访问过滤权限，则优先使用peer ACL过滤。
范例 : 
配置ACL名为zte的serve-only过滤规则生效ZXROSNG(config)# ntp access-group ipv4-serve-only zte
相关命令 : 
ntp access-group ipv4-access-listntp access-group ipv6-access-list
## ntp access-group ipv6-access-list 

ntp access-group ipv6-access-list 
命令功能 : 
为NTP指定IPv6控制列表。使用no命令取消控制。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp access-group ipv6-access-list 
  ＜ipv6-acl-name 
＞
no ntp access-group ipv6-access-list 
命令参数解释 : 
参数|描述
---|---
＜ipv6-acl-name＞|IPv6 ACL名称
缺省 : 
无 
使用说明 : 
• 本命令配置的是peer ACL过滤，最大访问限制（即client可以对本地NTP服务进行时间请求，本地时钟也可以同步到远程服务器）。• 使用本命令时，需要确认配置的ACL列表名称是否已经在ACL模块中配置，查询命令为：show ipv6-access-lists。如果没有配置，则需要到ACL模式下生成该名称的ACL规则。若ACL名对应的IPv6的过滤规则不存在时，也可以配置该命令，只是功能不生效。• 本命令支持所有NTP工作模式。
范例 : 
配置ACL名为zte的过滤规则生效：ZXROSNG(config)#ntp access-group ipv6-access-list zte
相关命令 : 
无 
## ntp access-group ipv6-serve-only 

ntp access-group ipv6-serve-only 
命令功能 : 
为NTP指定server ACL过滤IPv6控制列表。使用no命令取消控制 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp access-group ipv6-serve-only 
  ＜ipv6-acl-name 
＞
no ntp access-group ipv6-serve-only 
命令参数解释 : 
参数|描述
---|---
＜ipv6-acl-name＞|IPv6 ACL名
缺省 : 
无 
使用说明 : 
• server ACL过滤，只允许对本地NTP服务进行时间请求（即只允许本设备做服务器）。•  使用本命令时，需要确认配置的ACL列表名称是否已经在ACL模块中配置，查询命令为：show ipv6-access-lists。如果没有，也可以配置该命令。若要功能生效（不允许其它设备同步本设备时间），则需要到ACL模式下生成该名称的ACL规则。• NTP ACL过滤按照最大访问限制到最小访问限制依次匹配，若配置过peer ACL最大访问过滤权限，则优先使用peer ACL过滤。
范例 : 
配置ACL名为zte的serve-only过滤规则生效：ZXROSNG(config)# ntp access-group ipv6-serve-only zte
相关命令 : 
ntp access-group ipv4-access-listntp access-group ipv6-access-list
## ntp authenticate 

ntp authenticate 
命令功能 : 
启动NTP认证功能。使用no命令关闭认证功能。网络安全性要求较高，需要对NTP报文进行认证时，执行该命令启用NTP认证功能。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp authenticate 
 
no ntp authenticate 
命令参数解释 : 
					无
				 
缺省 : 
不开启认证功能。 
使用说明 : 
本命令是开启认证功能的开关，只有开启了认证功能，才会对NTP包进行密钥检测。命令执行成功后，本设备的NTP的认证功能开启，启用NTP认证功能后，必须配置认证密钥和使密钥可信。1. 配置NTP的密钥号和对应验证码，命令为：ntp authentication-key。2. 配置NTP密钥号为可信，命令为：ntp trusted-key。
范例 : 
开启认证功能：ZXROSNG(config)#ntp authenticate
相关命令 : 
ntp authentication-key <key-number> md5 <key-word>ntp trusted-key <key-number>
## ntp authentication-key 

ntp authentication-key 
命令功能 : 
设置NTP认证密钥号和对应的验证码。使用no命令删除密钥。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp authentication-key 
  ＜key-number 
＞ {md5 
 {clear 
 ＜clear-word 
＞|encrypted 
 ＜encrypted-word 
＞}|keychain 
 ＜keychain-name 
＞}
no ntp authentication-key 
  ＜key-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜key-number＞|密钥号，范围1~4294967295
＜clear-word＞|明文，长度为1~16个字节
＜encrypted-word＞|密文，长度为24个字节
＜keychain-name＞|keychain模板名字
缺省 : 
无 
使用说明 : 
• 当配置ntp authenticate后，本命令才有效 。• 配置密钥后，还需要配置ntp trusted-key后，该条密钥才有效。• NTP认证最多允许配置255条密钥。• NTP认证的密钥号以及配置的md5字符串需要与对端一致，如果不一致开启认证功能会导致认证失败。• 一条密钥对应的明文和密文必须是一对的，明文能翻译成密文，密文能翻译成明文。配置时明文和密文是二选一，配置明文会自动生成密文；配置密文将自动生成明文。无论选择明文配置还是密文配置，明文和密文都同时存在。
范例 : 
配置密钥号1对应的md5明文认证码为zte：ZXROSNG(config)#ntp authentication-key 1 md5 clear zte配置密钥号1对应的md5密文输入（明文对应的是zte）：ZXROSNG(config)#ntp authentication-key 1 md5  encrypted pAFEvNZXvxpayMBbQ0llog==
相关命令 : 
ntp authenticatentp trusted-key < key-number> ntp server
## ntp broadcast-client 

ntp broadcast-client 
命令功能 : 
开启设备NTP广播客户端功能。使用no命令关闭配置的广播客户端功能。 
命令模式 : 
 100G以太口模式,10G以太接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
10G以太接口模式:15,100G以太口模式:15,千兆以太接口模式:15,以太接口模式:15 
命令格式 : 
ntp broadcast-client 
 
no ntp broadcast-client 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
一个接口下只允许配置一个NTP广播客户端。一个设备上最多能配置5个NTP广播客户端。本命令配置完，需配置ntp enable，设备通过指定的接口接收发来的NTP广播报文。     
范例 : 
在gei-0/1/0/5口上开启NTP广播客户端功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-client在gei-0/1/0/5口上开启NTP广播客户端功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-client
相关命令 : 
ntp enable 
## ntp broadcast-client 

ntp broadcast-client 
命令功能 : 
开启设备NTP广播客户端功能。使用no命令关闭配置的广播客户端功能。 
命令模式 : 
 三层VLAN接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp broadcast-client 
 
no ntp broadcast-client 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
一个接口下只允许配置一个NTP广播客户端。一个设备上最多能配置5个NTP广播客户端。本命令配置完，需配置ntp enable，设备通过指定的接口接收发来的NTP广播报文。 
范例 : 
在gei-0/1/0/5口上开启NTP广播客户端功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-client在gei-0/1/0/5口上开启NTP广播客户端功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-client
相关命令 : 
ntp enable 
## ntp broadcast-delay 

ntp broadcast-delay 
命令功能 : 
手动配置广播(组播)客户端的链路延时，no命令恢复默认值0(us)。系统默认广播（组播）的链路延时为0。但实际网络中，通常会存在时延，网络中有较大的延时时，执行该命令，配置合理的延时值，可以使广播（组播）客户端有较精确的时钟同步。减小网络延时对NTP时间同步的影响。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp broadcast-delay 
  ＜delay-value 
＞
no ntp broadcast-delay 
命令参数解释 : 
参数|描述
---|---
＜delay-value＞|链路延时时长，0-999999(us)链路延时时长，0-999999(us)
缺省 : 
链路延时默认取值为0。 
使用说明 : 
当设备配置为广播（组播）客户端且能够接收广播（组播）服务器发送的NTP时间同步报文时，本命令才有效。 
范例 : 
配置链路延时为2(us):ZXROSNG(config)#ntp broadcast-delay 2
相关命令 : 
ntp broadcast-client 
## ntp broadcast-server 

ntp broadcast-server 
命令功能 : 
开启设备NTP广播服务器功能。使用no命令关闭配置的广播服务器功能。 
命令模式 : 
 100G以太口模式,10G以太接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
10G以太接口模式:15,100G以太口模式:15,以太接口模式:15,千兆以太接口模式:15 
命令格式 : 
ntp broadcast-server 
  [{[version 
 ＜version-number 
＞],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}]}]
no ntp broadcast-server 
命令参数解释 : 
参数|描述
---|---
＜version-number＞|NTP的版本号，范围1-4，可选，默认为3
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
缺省 : 
version默认取值为3。 
使用说明 : 
一个接口下只允许配置一个NTP广播服务器。一个设备上最多能配置5个NTP广播服务器。本命令配置后，需配置ntp enable命令，以及ntp master命令，设备开始通过指定的接口向外发送NTP广播报文。 
范例 : 
在gei-0/1/0/5口上开启NTP广播服务器功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-server在gei-0/1/0/5口上开启NTP广播服务器功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-server
相关命令 : 
ntp enablentp master  <1-15 >
## ntp broadcast-server 

ntp broadcast-server 
命令功能 : 
开启设备NTP广播服务器功能。使用no命令关闭配置的广播服务器功能。 
命令模式 : 
 三层VLAN接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp broadcast-server 
  [{[version 
 ＜version-number 
＞],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}]}]
no ntp broadcast-server 
命令参数解释 : 
参数|描述
---|---
＜version-number＞|NTP的版本号，范围1-4，可选，默认为3
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
缺省 : 
version默认取值为3。 
使用说明 : 
一个接口下只允许配置一个NTP广播服务器。一个设备上最多能配置5个NTP广播服务器。本命令配置后，需配置ntp enable命令，以及ntp master命令，设备开始通过指定的接口向外发送NTP广播报文。 
范例 : 
在gei-0/1/0/5口上开启NTP广播服务器功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-server在gei-0/1/0/5口上开启NTP广播服务器功能：ZXROSNG(config-if-gei-0/1/0/5)#ntp broadcast-server
相关命令 : 
ntp enablentp master  <1-15 >
## ntp dns-peer 

ntp dns-peer 
命令功能 : 
配置需要在对等体模式下同步时间的dns域名对等体会话，以及采用的NTP协议的版本号，NTP认证号。使用no命令删除配置的dns对等体会话。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp dns-peer 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜host-name 
＞ priority 
 ＜priority-value 
＞ [{[version 
 ＜version-number 
＞],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}],[minpoll 
 ＜min-poll 
＞],[maxpoll 
 ＜max-poll 
＞]}]
no ntp dns-peer 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜host-name 
＞
				
命令参数解释 : 
参数|描述
---|---
mng|管理口vrf
＜vrf-name＞|私网vrf名字
＜host-name＞|域名
＜priority-value＞|优先级是必选项，范围1-5，每一个server的优先级不同
＜version-number＞|NTP的版本号，范围1-4，可选，IPv4默认为3，IPv6目前只能配置为4
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜min-poll＞|最小发包间隔。
＜max-poll＞|最大发包间隔。
缺省 : 
version默认取值为3 
使用说明 : 
本设备最多支持配置5个NTP DNS对等体会话，如果和服务器混合配置，所有模式总和最多能配置5个。配置带vrf的对等体会话时，需由用户保证当前vrf可用。key为NTP对等体主动到NTP对等体被动之间使用的密钥号，必须是已经通过ntp authentication-key 和ntp trusted-key命令配置的同一个密钥号，否则只能进行无认证信息的普通同步。priority优先级是必选项，每个NTP服务器或被动对等体的优先级必须不同。域名对等体会话优先翻译IPv4地址同步，在版本为4时，如果无有效IPv4地址，会尝试翻译IPv6地址同步。本命令配置后，需配置ntp enable命令才能开始从被动对等体端同步时间。 
范例 : 
配置域名为test的dns对等体会话：ZXROSNG(config)# ntp dns-peer test priority 1删除域名为test的dns对等体会话：ZXROSNG(config)#no ntp dns-peer test
相关命令 : 
ntp enablentp authenticatentp authentication-keyntp trusted-keyshow ntp status
## ntp dns-server 

ntp dns-server 
命令功能 : 
配置需要同步时间的dns域名服务器，以及采用的NTP协议的版本号，NTP认证号。使用no命令删除配置的dns时间服务器。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp dns-server 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜host-name 
＞ priority 
 ＜priority-value 
＞ [{[version 
 ＜version-number 
＞],[{unlock 
|lock 
}],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}],[minpoll 
 ＜min-poll 
＞],[maxpoll 
 ＜max-poll 
＞],iburst 
}]
no ntp dns-server 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜host-name 
＞
				
命令参数解释 : 
参数|描述
---|---
mng|管理口vrf
＜vrf-name＞|私网vrf名
＜host-name＞|域名
＜priority-value＞|优先级是必选项，范围1-5，每一个server的优先级不同
＜version-number＞|NTP的版本号，范围1-4，可选，IPv4默认为3，IPv6目前只能配置为4
unlock|配置服务器为非锁定状态，可选配置。
lock|配置服务器为锁定状态，可选配置。lock表示该客户端锁定NTP服务器进行同步，即使本服务器不可用或有其它优先级高的NTP服务器也不切换NTP服务器。
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜min-poll＞|最小发包间隔。
＜max-poll＞|最大发包间隔。
iburst|发送iburst报文标记。开启后增加快速同步与老化。
缺省 : 
version默认取值为3，配置的服务器默认为非锁定。 
使用说明 : 
本设备最多支持配置5个NTP DNS服务器，如果和对等体模式混合配置，所有模式总和最多能配置5个。配置带vrf的服务器时，需由用户保证当前vrf可用。key为NTP客户端到NTP服务端之间使用的密钥号，必须是已经通过ntp authentication-key 和ntp trusted-key命令配置的同一个密钥号，否则只能进行无认证信息的普通同步。priority优先级是必选项，每个NTP服务器或被动对等体的优先级必须不同。域名服务器优先翻译IPv4地址同步，在版本为4时，如果无有效IPv4地址，会尝试翻译IPv6地址同步。本命令配置后，需配置ntp enable命令才能开始从时间服务器同步时间。 
范例 : 
配置域名为test的dns服务器：ZXROSNG(config)# ntp dns-server test priority 1删除域名为test的dns服务器：ZXROSNG(config)#no ntp dns-server test
相关命令 : 
ntp enablentp authenticatentp authentication-keyntp trusted-keyshow ntp status
## ntp enable 

ntp enable 
命令功能 : 
开启NTP功能。默认情况下，系统的NTP功能不启用。当需要开启NTP功能时，使用本命令。使用no命令关闭NTP功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp enable 
 
no ntp enable 
命令参数解释 : 
					无
				 
缺省 : 
不开启NTP功能。 
使用说明 : 
本命令相当于NTP功能的总开关，配置本命令后其余的NTP命令配置的功能才能生效。 
范例 : 
开启NTP功能：ZXROSNG(config)#ntp enable
相关命令 : 
ntp servershow ntp status
## ntp master 

ntp master 
命令功能 : 
用于启用本设备的NTP服务器功能，并配置本设备的NTP服务器等级。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp master 
  ＜stratum 
＞
no ntp master 
命令参数解释 : 
参数|描述
---|---
＜stratum＞|服务器的等级，范围1-15
缺省 : 
无 
使用说明 : 
•  设备同时可以做服务器向其它的设备提供时钟源，又做客户端去同步其它时钟源。•  设备配置了ntp master才能作为其它设备的同步时钟源。例如：网络A、B两台设备，如果设定设备A向设备B请求同步，则需要设置设备B的master等级，或A、B都配置等级，但设备B的等级的数值小（数值小，等级高）。配置后，设备A才能向设备B请求同步。
范例 : 
ZXROSNG(config)# ntp master 6      查看配置结果信息：ZXROSNG(config)#show ntp statusClock is synchronized, stratum 6, reference is LOCALnominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**6reference time is ceea6ee7.0 (01:18:31  Sun  Jan 3  2010 UTC)clock offset is 0.00 msec, root delay is 0.00 msecroot dispersion is 0.00 msec, peer dispersion is 0.00 msec
相关命令 : 
无 
## ntp multicast-client 

ntp multicast-client 
命令功能 : 
开启设备NTP组播客户端功能。使用no命令关闭配置的组播客户端功能。 
命令模式 : 
 100G以太口模式,10G以太接口模式,loopback接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
loopback接口模式:15,千兆以太接口模式:15,以太接口模式:15,100G以太口模式:15,10G以太接口模式:15 
命令格式 : 
ntp multicast-client 
  {＜ipv4-address 
＞|＜ipv6-address 
＞}
no ntp multicast-client 
  {＜ipv4-address 
＞|＜ipv6-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4组播地址
＜ipv6-address＞|IPv6组播地址
缺省 : 
无 
使用说明 : 
同一个接口下可以配置不同的组播IP的NTP组播客户端，不同的接口下除了可配置不同组播IP的NTP组播客户端也可配置相同组播IP的NTP客户端。一个设备最多允许配置5个NTP组播客户端。本命令配置完，需配置ntp enable命令，设备开始通过指定接口接收NTP组播报文。 
范例 : 
在gei-0/1/0/5口上配置组播客户端的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-client 224.1.1.1在gei-0/1/0/5口上配置组播客户端的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-client 224.1.1.1
相关命令 : 
ntp enable 
## ntp multicast-client 

ntp multicast-client 
命令功能 : 
开启设备NTP组播客户端功能。使用no命令关闭配置的组播客户端功能。 
命令模式 : 
 三层VLAN接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp multicast-client 
  {＜ipv4-address 
＞|＜ipv6-address 
＞}
no ntp multicast-client 
  {＜ipv4-address 
＞|＜ipv6-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4组播地址
＜ipv6-address＞|IPv6组播地址
缺省 : 
无 
使用说明 : 
同一个接口下可以配置不同的组播IP的NTP组播客户端，不同的接口下除了可配置不同组播IP的NTP组播客户端也可配置相同组播IP的NTP客户端。一个设备最多允许配置5个NTP组播客户端。本命令配置完，需配置ntp enable命令，设备开始通过指定接口接收NTP组播报文。 
范例 : 
在gei-0/1/0/5口上配置组播客户端的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-client 224.1.1.1在gei-0/1/0/5口上配置组播客户端的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-client 224.1.1.1
相关命令 : 
ntp enable 
## ntp multicast-server 

ntp multicast-server 
命令功能 : 
开启设备NTP组播服务器功能。使用no命令关闭配置的组播服务器功能。 
命令模式 : 
 100G以太口模式,10G以太接口模式,loopback接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
loopback接口模式:15,以太接口模式:15,100G以太口模式:15,10G以太接口模式:15,千兆以太接口模式:15 
命令格式 : 
ntp multicast-server 
  {＜ipv4-address 
＞|＜ipv6-address 
＞} [{[version 
 ＜version-number 
＞],[ttl 
 ＜ttl-value 
＞],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}]}]
no ntp multicast-server 
  {＜ipv4-address 
＞|＜ipv6-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4组播地址
＜ipv6-address＞|IPv6组播地址
＜version-number＞|NTP的版本号，范围1-4，可选
＜ttl-value＞|设置生存时间TTL值，可选
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
缺省 : 
IPv4的version默认取值为3，IPv6版本号只能配置为4 
使用说明 : 
同一个接口下可以配置不同的组播IP的NTP组播服务器，不同的接口下除了可配置不同组播IP的NTP组播服务器也可配置相同组播IP的NTP服务器。一个设备最多允许配置5个NTP组播服务器。本命令配置完，需配置ntp enable命令，以及ntp master命令，设备开始通过指定接口向外发送NTP组播报文。IPv6服务器的版本必须配置为4。 
范例 : 
在gei-0/1/0/5口上配置组播服务器的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-server 224.1.1.1在gei-0/1/0/5口上配置组播服务器的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-server 224.1.1.1
相关命令 : 
ntp enablentp master  <1-15>
## ntp multicast-server 

ntp multicast-server 
命令功能 : 
开启设备NTP组播服务器功能。使用no命令关闭配置的组播服务器功能。 
命令模式 : 
 三层VLAN接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp multicast-server 
  {＜ipv4-address 
＞|＜ipv6-address 
＞} [{[version 
 ＜version-number 
＞],[ttl 
 ＜ttl-value 
＞],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}]}]
no ntp multicast-server 
  {＜ipv4-address 
＞|＜ipv6-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4组播地址
＜ipv6-address＞|IPv6组播地址
＜version-number＞|NTP的版本号，范围1-4，可选
＜ttl-value＞|设置生存时间TTL值，可选
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|udp端口号，默认123，可配范围1025-65535.
缺省 : 
IPv4的version默认取值为3，IPv6版本号只能配置为4 
使用说明 : 
同一个接口下可以配置不同的组播IP的NTP组播服务器，不同的接口下除了可配置不同组播IP的NTP组播服务器也可配置相同组播IP的NTP服务器。一个设备最多允许配置5个NTP组播服务器。本命令配置完，需配置ntp enable命令，以及ntp master命令，设备开始通过指定接口向外发送NTP组播报文。IPv6服务器的版本必须配置为4。 
范例 : 
在gei-0/1/0/5口上配置组播服务器的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-server 224.1.1.1在gei-0/1/0/5口上配置组播服务器的组播地址224.1.1.1：ZXROSNG(config-if-gei-0/1/0/5)#ntp multicast-server 224.1.1.1
相关命令 : 
ntp enablentp master  <1-15>
## ntp peer 

ntp peer 
命令功能 : 
配置需要在对等体模式下同步时间的被动对等体的IP地址，以及采用的NTP协议的版本号，NTP认证号。使用no命令删除配置的被动对等体。当设备采用NTP对等体模式时，需要在主动对等体配置本命令，被动对等体不需要配置。设备开启主动对等体模式，NTP主动对等体定时向被动对等体发送时间同步请求报文，默认的时间间隔为64s，如果需要修改定时发送的时间间隔，可以执行ntp poll-interval命令。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp peer 
  [vrf 
 {mng 
|＜vrf-name 
＞}] {＜ipv4-address 
＞|＜ipv6-address 
＞} priority 
 ＜priority-value 
＞ [{[version 
 ＜version-number 
＞],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}],[minpoll 
 ＜min-poll 
＞],[maxpoll 
 ＜max-poll 
＞]}]
no ntp peer 
  [vrf 
 {mng 
|＜vrf-name 
＞}] {＜ipv4-address 
＞|＜ipv6-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
mng|VRF管理口名称
＜vrf-name＞|配置的VPN名选项
＜ipv4-address＞|被动对等体的IPv4地址
＜ipv6-address＞|被动对等体的IPv6地址
＜priority-value＞|优先级是必选项，范围1-5，每一个peer的优先级不能相同
＜version-number＞|NTP的版本号，范围1-4，可选，IPv4默认为3，IPv6只能配置为4
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选。该认证密钥号必须是已经通过ntp authentication-key 和ntp trusted-key命令配置的同一个密钥号。否则只能进行无认证信息的普通同步。
＜udp-port＞|udp端口号，默认123，可以配置1025-65535.
＜udp-port＞|udp端口号，默认123，可以配置1025-65535.
＜min-poll＞|最小发包间隔。
＜max-poll＞|最大发包间隔。
缺省 : 
version默认取值为3。 
使用说明 : 
本设备最多支持配置5个NTP被动对等体，如果和客户/服务器模式混合配置，两种模式最多能配置5个，每个NTP服务器或被动对等体的优先级必须不同。配置带vrf的对等体时，需由用户保证当前vrf可用。key为密钥号，必须是已经通过ntp authentication-key 和ntp trusted-key命令配置的同一个密钥号，否则只能进行无认证信息的普通同步。IPv6被动对等体的版本必须配置为4。本命令配置后，需配置ntp enable命令才能开始从时间服务器同步时间。本设备支持对NTP启用认证，如果启用了认证，配置前，需要先进行密钥的相关配置，命令为：1. 启用NTP认证，命令为：ntp authenticate。2. 配置NTP的密钥号和对应验证码，命令为：ntp authentication-key。3. 配置NTP密钥号为可信，命令为：ntp trusted-key。
范例 : 
设备A  IP为10.10.10.1，设备 IP为10.10.10.2。设备A和设备B设置为NTP对等体模式。设备A为主动对等体，命令为：ZXROSNG(config)# ntp peer 10.10.10.2 priority 2删除设备A和设备B的对等体模式，关闭设备A的主动对等体功能，命令为：ZXROSNG(config)#no ntp peer 10.10.10.2
相关命令 : 
ntp enableshow ntp status
## ntp poll-interval 

ntp poll-interval 
命令功能 : 
配置NTP报文的轮询时间间隔，2的幂次方秒，no命令恢复默认值6（即64s）。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp poll-interval 
  ＜interval-value 
＞
no ntp poll-interval 
命令参数解释 : 
参数|描述
---|---
＜interval-value＞|轮询间隔，范围4-17
缺省 : 
发包间隔默认取值为6。 
使用说明 : 
• 本命令只对NTP模式设置为客户/服务器模式或对等体模式有效。广播组播模式发包间隔为固定值64s，不可设置。使用前，如果需要了解本设备的NTP功能模式，可以使用查询命令show ntp associations。• 设备两端设置的NTP时间同步报文发送时间间隔可以不一致，以NTP同步请求报文发送方的设置为准。• NTP间隔设置成功后，NTP时间同步报文会按照新的时间间隔发送。时间间隔越短，NTP设备间的时间同步越快；时间间隔越长，NTP设备间的时间同步越慢。
范例 : 
配置发包间隔为4(16s)：ZXROSNG(config)#ntp poll-interval 4
相关命令 : 
show ntp status 
## ntp port 

ntp port 
命令功能 : 
配置NTP的发包的源UDP端口号，默认端口号为123；使用no命令恢复默认值
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp port 
  {＜udp-port 
＞|＜udp-port 
＞}
no ntp port 
命令参数解释 : 
参数|描述
---|---
＜udp-port＞|本设备ntp采用的udp端口号，默认123，可配范围1025-65535.
＜udp-port＞|本设备ntp采用的udp端口号，默认123，可配范围1025-65535.
缺省 : 
123 
使用说明 : 
本命令是配置本地的NTP协议UDP监听端口号。当修改端口号后，本段发送的NTP报文的源端口号跟随修改；远端需要配置向这个端口发送NTP报文才会被接收。 
范例 : 
修改NTP的发包源UDP端口号为10000：ZXROSNG(config)#ntp port 10000
相关命令 : 
ntp enable 
## ntp server 

ntp server 
命令功能 : 
配置需要同步时间的时间服务器的IP地址，以及采用的NTP协议的版本号，NTP认证号。使用no命令删除配置的时间服务器。命令执行成功后，NTP客户端定时向NTP服务器发送时间同步请求报文。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp server 
  [vrf 
 {mng 
|＜vrf-name 
＞}] {＜ipv4-address 
＞|＜ipv6-address 
＞} priority 
 ＜priority-value 
＞ [{[version 
 ＜version-number 
＞],[{unlock 
|lock 
}],[key 
 ＜key-number 
＞],[port 
 {＜udp-port 
＞|＜udp-port 
＞}],[minpoll 
 ＜min-poll 
＞],[maxpoll 
 ＜max-poll 
＞],iburst 
}]
no ntp server 
  [vrf 
 {mng 
|＜vrf-name 
＞}] {＜ipv4-address 
＞|＜ipv6-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
mng|VRF管理口名称
＜vrf-name＞|配置的VPN名选项
＜ipv4-address＞|时间服务器的IPv4地址
＜ipv6-address＞|时间服务器的IPv6地址
＜priority-value＞|优先级是必选项，范围1-5，每一个server的优先级不同
＜version-number＞|NTP的版本号，范围1-4，可选，IPv4默认为3，IPv6目前只能配置为4
unlock|配置服务器为非锁定状态，可选配置。
lock|配置服务器为锁定状态，可选配置。lock表示该客户端锁定NTP服务器进行同步，即使本服务器不可用或有其它优先级高的NTP服务器也不切换NTP服务器。
＜key-number＞|设置有效的密钥号，范围1-4294967295，可选。该认证密钥号必须是已经通过ntp authentication-key 和ntp trusted-key命令配置的同一个密钥号。否则只能进行无认证信息的普通同步。
＜udp-port＞|udp端口号，默认123，可配范围1025-65535
＜udp-port＞|udp端口号，默认123，可配范围1025-65535
＜min-poll＞|最小poll间隔。
＜max-poll＞|最大poll间隔。
iburst|发送iburst报文标记。开启后增加快速同步与老化。
缺省 : 
version默认取值为3，配置的服务器默认为非锁定。 
使用说明 : 
本设备最多支持配置5个NTP服务器，与对等体模式一起最多能配置5个。配置带vrf的服务器时，需由用户保证当前vrf可用。priority优先级是必选项，每个NTP服务器或被动对等体的优先级不能相同。IPv6服务器版本必须配置为4。本命令配置后，需配置ntp enable命令才能开始从时间服务器同步时间。本设备支持对NTP启用认证（携带key），如果启用了认证，配置前，需要先进行密钥的相关配置，命令为：1. 启用NTP认证，命令为：ntp authenticate。2. 配置NTP的密钥号和对应验证码，命令为：ntp authentication-key。3. 配置NTP密钥号为可信，命令为：ntp trusted-key。
范例 : 
设备A ip为10.10.10.1，设备B ip为10.10.10.2。需要设备A同步设备B。设备A为NTP客户端，命令为：ZXROSNG(config)# ntp server 10.10.10.2 priority 1删除设备A和设备B的客户/服务器模式同时关闭设备A的客户端功能，命令为：ZXROSNG(config)#no ntp server 10.10.10.2 
相关命令 : 
ntp enablentp authenticatentp authentication-keyntp trusted-keyshow ntp status 
## ntp source interface 

ntp source interface 
命令功能 : 
配置NTP协议发出报文的源接口。命令执行成功后，本设备发送封装NTP时间同步报文的UDP报文时，动态获取接口上IPV4或IPV6地址，作为该UDP报文的源地址。使用no命令删除协议发出报文的源接口。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp source interface 
  ＜interface-name 
＞
no ntp source interface 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|配置NTP协议发出报文的源接口。
缺省 : 
默认不指定。 
使用说明 : 
• 配置NTP协议发出报文的源接口，与ntp source ipv4/ipv6命令互斥。• ntp source interface命令使用后，本设备发出的NTP同步报文的源IP地址从指定的接口上动态获取。• 本设备设置为NTP客户/服务器模式或者对等体模式时，本命令有效。广播或者组播模式，本命令无效。
范例 : 
指定报文的源接口为gei-0/1/0/1：ZXROSNG(config)#ntp source interface gei-0/1/0/1
相关命令 : 
ntp enablentp source ipv4ntp source ipv6
## ntp source ipv4 

ntp source ipv4 
命令功能 : 
用于指定NTP时间请求报文的源IPV4地址，命令执行成功后，本设备发出的封装了NTP报文的UDP报文都将填充本命令指定的源IPV4地址。使用no命令删除该源IP地址，由设备自动适配并填充。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp source ipv4 
  ＜ipv4-address 
＞
no ntp source ipv4 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|NTP报文发出的源地址，为十进制点分形式
缺省 : 
系统默认不指定该UDP报文的源IP地址，由设备自动适配并填充。 
使用说明 : 
• 本配置用于客户端服务器模式中的客户端或对等模式中主动对等体端发包时填充源IP。一些特殊的地址不允许配置例如：0.0.0.0、环回地址、组播地址、广播地址、格式不正确的地址等。如果NTP设置为广播或者组播模式，本命令无效。• 本命令与ntp source interface 命令互斥，不允许同时配置。ntp source interface命令使用后，本设备发出的NTP同步报文的源IP地址从指定的接口上动态获取。
范例 : 
指定IPv4报文的源IP地址为192.168.2.1：ZXROSNG(config)#ntp source ipv4 192.168.2.1
相关命令 : 
ntp enablentp servershow ntp status 
## ntp source ipv6 

ntp source ipv6 
命令功能 : 
配置NTP协议发出报文的源IPv6地址。命令执行成功后，本设备发出的封装了NTP时间同步报文的UDP报文都将填充本命令指定的源IPV6地址。使用no命令删除协议发出IPv6报文的源地址。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp source ipv6 
  ＜ipv6-address 
＞
no ntp source ipv6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|报文发送的源IPv6地址
缺省 : 
系统默认不指定该UDP报文的源地址，由设备自动适配并填充。 
使用说明 : 
• 本设备设置为NTP客户/服务器模式或者对等体模式时，本命令有效。如果NTP设置为广播或者组播模式，本命令无效。• 与ntp source interface命令互斥，不允许同时配置。ntp source interface命令使用后，本设备发出的封装NTP同步报文的UDP报文的源IP地址从指定的接口上动态获取。
范例 : 
配置NTP协议发出报文的源IPv6地址：ZXROSNG(config)#ntp source ipv6 10::4
相关命令 : 
无 
## ntp trusted-key 

ntp trusted-key 
命令功能 : 
设置NTP认证可信的密钥号。当需要将命令：ntp authentication-key配置的密钥设置为可信时，执行该命令。命令成功后，该密钥为可信，可用于认证。使用no命令删除可信密钥号。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ntp trusted-key 
  ＜key-number 
＞
no ntp trusted-key 
  ＜key-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜key-number＞|密钥号，范围1-4294967295
缺省 : 
无 
使用说明 : 
本命令是针对ntp authentication-key 命令配置的一条密钥将其设置为可信，最多可配置255条。当NTP认证功能开启（命令为：ntp authenticate）和密钥号对应的密钥配置（命令为：ntp authentication-key）后，本命令配置的密钥号才有效，可用于认证。该密钥号能被NTP的其它命令使用（例如：ntp server、ntp peer、ntp broadcast-server、ntp multicast-server命令）。
范例 : 
配置密钥号1对应的密钥可靠：ZXROSNG(config)# ntp trusted-key 1
相关命令 : 
ntp authenticatentp authentication-key <key-number> md5 <key-word> 
## show debug ntp 

show debug ntp 
命令功能 : 
显示NTP调试开关状态。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug ntp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示NTP调试开关状态。如果NTP调试开关处于关闭状态则显示内容为空。 
范例 : 
显示NTP调试开关状态：ZXROSNG#show debug ntpNTP:  NTP packet debugging is on
相关命令 : 
无 
## show ntp associations 

show ntp associations 
命令功能 : 
显示NTP所有会话。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ntp associations 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示NTP所有会话。 
范例 : 
查询NTP会话信息，命令为：ZXUN(config)# show ntp associations• 当NTP无会话信息时，查询结果为：All associations info  :• 当存在NTP会话信息时，查询结果为：Source address          : 100:12::1Mode                    : ClientFlags                   : PersistentKeynum                  : 0Version                 : 4Lock mode               : LockPoll-interval           : 1Stratum                 : 16Priority                :  1Reach                   : 0Delay                   : 0.000000Offset                  : 0.000000-------------------------------------------------------Source address          : 224.1.1.1Interface name          : loopback1Mode                    : Broadcast ServerFlags                   : PersistentKeynum                  : 0Version                 : 3Lock mode               : UnlockPoll-interval           : 6Stratum                 : 16Priority                : 6Reach                   : 0Delay                   : 0.000000Offset                  : 0.000000• 输出参数说明如下：参数名称    参数说明Source address    对端服务器或对等体的IP地址。Mode    本设备工作的NTP模式，主要包括：– Client：表示客户端模式。– Symmetric Active：表示主动对等体模式。– Symmetric Passive：示被动对等体模式。– Broadcast Server： 广播（组播）服务器模式。– Broadcast Client： 广播（组播）客户端模式。Flags    会话标识。Persistent表示永久会话；Ephemeral表示临时会话。Keynum    认证密钥号。Version    NTP协议版本号。Lock mode    锁定模式，设备使用NTP客户/服务器模式时可以配置，默认是unlock。Lock 表示锁定该服务器。Unclock表示未锁定该服务器。Poll-interval    本设备的发送NTP时间请求报文的时间间隔。Stratum    对端的时钟等级。Priority    会话优先级。Reach    报文的可达数。Delay    本地系统时钟与主参考时钟的总延迟。Offset    本地时钟与NTP服务器之间的偏差。
相关命令 : 
无 
## show ntp status 

show ntp status 
命令功能 : 
显示NTP的运行状态，可以通过该命令查询到本设备的时钟同步状态、时钟等级等信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ntp status 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示NTP同步状态，可以通过该命令查询本设备的时钟同步状态、时钟等级等信息。 
范例 : 
查看NTP状态，命令为：ZXROSNG(config)# show ntp status当NTP功能未开启时，查询结果为：%Info 6629: NTP is disabled,there's no NTP status informationNTP功能开启，但是设备不同步任何服务器：Clock is unsynchronized, stratum 16, no reference clocknominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**6reference time is d2593419.c9fbe76c (14:50:01  Mon  Oct 31  2011 UTC)clock offset is 99.00 msec, root delay is 0.00 msecroot dispersion is 0.00 msec, peer dispersion is 0.00 msecNTP功能开启，设备同步本地时钟：Clock is synchronized, stratum 3, reference is LOCALnominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**6reference time is d2593419.c9fbe76c (14:50:01  Mon  Oct 31  2011 UTC)clock offset is 99.00 msec, root delay is 0.00 msecroot dispersion is 0.00 msec, peer dispersion is 0.00 msecNTP功能开启，设备同步外部时钟源：Clock is synchronized, stratum 5, reference is 20.20.20.20nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**6reference time is d2593419.c9fbe76c (14:50:01  Mon  Oct 31  2011 UTC)clock offset is 99.00 msec, root delay is 0.00 msec root dispersion is 0.00 msec, peer dispersion is 0.00 msec命令中重点字段含义如下：synchronized： 表示设备同步外部时钟源或本地时钟。unsynchronized：表示设备没有和任何时钟源同步。stratum：本设备的时钟等级。reference id：参考时钟源。当设备没有和任何服务器同步，显示no reference clock。当设备同步本地，显示LOCAL。当设备同步外部时钟源，显示同步服务器的IP地址。
相关命令 : 
无 
# RMON配置命令 
interface : 

interface (RMON模式) 
命令功能 : 
进入RMON接口配置模式。 
命令模式 : 
 RMON模式  
命令默认权限级别 : 
15 
命令格式 : 
interface 
  ＜interface-name 
＞
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
无 
使用说明 : 
只支持以太网接口。 
范例 : 
1. 进入RMON接口配置模式：ZXROSNG(config-rmon)#interface gei-0/1/0/1ZXROSNG(config-rmon-interface)#
相关命令 : 
无 
## rmon alarm 

rmon alarm 
命令功能 : 
设置告警和MIB对象。使用no命令取消告警。
命令模式 : 
 RMON模式  
命令默认权限级别 : 
15 
命令格式 : 
rmon alarm 
  ＜index-number 
＞ ＜mib-subtree-id 
＞ ＜monitor-seconds 
＞ {delta 
|absolute 
} [startup-alarm 
 {rising 
|falling 
|rising-or-falling 
}] rising-threshold 
 ＜rising-threshold-limit 
＞ [＜outlimit-index-number 
＞] falling-threshold 
 ＜limit-falling-threshold 
＞ [＜outlimit-index-number 
＞] [owner 
 ＜alarm-owner 
＞]
no rmon alarm 
  ＜index-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜index-number＞|索引号，范围1~65535
＜mib-subtree-id＞|要监控的MIB变量，必须为可转换为整数的MIB变量，长度为1~64个字符
＜monitor-seconds＞|监控上述MIB变量的时间（单位：秒），范围10~2147483
delta|增量与阈值比较
absolute|选定变量的值与阈值比较
rising|首次触发告警时仅触发上限告警
falling|首次触发告警时仅触发下限告警
rising-or-falling|首次触发告警时既可以触发上限告警也可以触发下限告警
＜rising-threshold-limit＞|采样统计的上升阈值，范围-2147483648~2147483647
＜outlimit-index-number＞|超出下降阈值时所引起的事件号，范围1~65535
＜limit-falling-threshold＞|采样统计的下降阈值，范围-2147483648~2147483647
＜outlimit-index-number＞|超出下降阈值时所引起的事件号，范围1~65535
＜alarm-owner＞|该警报的创建者，长度为1~31个字符，默认值为config
缺省 : 
无 
使用说明 : 
1. 允许对同一实例进行相同或不同时间间隔采样处理。2. 以相同索引<index-number>创建告警项，对于用户未输入的可选参数采用当前配置值。如果除<index-number>之外，其他所有参数和当前配置值有不一样的，则提示报错，此场景如果需要创建成功，则必须先用no命令取消掉原相同索引的配置，再执行此创建操作。3. 删除不存在的索引项，提示"Unknown alarm number"。4. 由于内存或资源不可利用，提示"Alloc buffer error"或"Resource unavailable"。5. 本告警项应与相关事件项配合，以产生相应动作。
范例 : 
1. 配置监控MIB对象为ip.2.0，采样时间为10秒，上限值为200，下限值为100，上、下限告警发生时对应的事件1。显示效果如下：ZXROSNG(config-rmon)#rmon alarm 1 ip.2.0 10 absolute rising-threshold 200 1 falling-threshold 100 1 owner ZTE2. 删除已存在的告警项:ZXROSNG(config-rmon)#no rmon alarm 1ZXROSNG(config-rmon)#
相关命令 : 
show rmon alarms 
## rmon collection history 

rmon collection history 
命令功能 : 
打开接口的历史收集功能（仅适用于以太网接口）。使用no命令关闭该功能。
命令模式 : 
 RMON接口模式  
命令默认权限级别 : 
15 
命令格式 : 
rmon collection history 
  ＜index-number 
＞ [buckets 
 ＜bucket-number 
＞] [interval 
 ＜interval-seconds 
＞] [owner 
 ＜history-owner 
＞]
no rmon collection history 
  ＜index-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜index-number＞|索引号，范围1~65535
＜bucket-number＞|请求的环行桶大小，默认值为50，系统最大支持为100，范围为1~100
＜interval-seconds＞|采样间隔（单位：秒），范围10~3600，缺省为1800秒。建议用30秒和1800秒采集短期和长期网络流量变化
＜history-owner＞|该行历史的创建者，长度不超过1~31个字符，默认值为monitor
缺省 : 
无 
使用说明 : 
1. 允许在同一接口上配置多个历史统计项。2. . 以相同索引<index-number>创建统计项，对于用户未输入的可选参数采用当前配置值。如果除<index-number>之外，其他所有参数和当前配置值有不一样的，则提示报错，此场景如果需要创建成功，则必须先用no命令取消掉原相同索引的配置，再执行此创建操作。3. 删除不存在的索引项，提示"Unknown historyControl number"。4. 由于内存或资源不可利用，提示"Alloc buffer error"或"Resource unavailable"。
范例 : 
1. 在百兆以太网接口上配置历史组统计，采样时间为300秒：ZXROSNG(config)#rmonZXROSNG(config-rmon)#interface gei-0/1/0/1ZXROSNG(config-rmon-interface)#rmon collection history 1 buckets 100 interval 300 owner zte ZXROSNG(config-rmon-interface)#2. 删除索引已存在的历史项：ZXROSNG(config-rmon-interface)#no rmon collection history 1
相关命令 : 
show rmon history 
## rmon collection statistics 

rmon collection statistics 
命令功能 : 
打开接口的统计功能（仅适用于以太网接口）。使用no命令关闭该功能。
命令模式 : 
 RMON接口模式  
命令默认权限级别 : 
15 
命令格式 : 
rmon collection statistics 
  ＜index-number 
＞ [owner 
 ＜statistics-owner 
＞]
no rmon collection statistics 
  ＜index-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜index-number＞|索引号，范围1~65535
＜statistics-owner＞|该事件的创建者，长度为1~31个字符，缺省为monitor
缺省 : 
无 
使用说明 : 
1. 允许在同一接口上配置多个统计项。2. 以相同索引<index-number>创建统计项，对于用户未输入的可选参数采用当前配置值。如果除<index-number>之外，其他所有参数和当前配置值有不一样的，则提示报错，此场景如果需要创建成功，则必须先用no命令取消掉原相同索引的配置，再执行此创建操作。3. 删除不存在的索引项，提示"Unknown etherStats number"。4. 由于内存或资源不可利用，提示"Alloc buffer error"或"Resource unavailable"。
范例 : 
1. 在百兆以太网接口上配置统计组，采样时间为300秒：ZXROSNG(config)#rmonZXROSNG(config-rmon)#interface gei-0/1/0/1ZXROSNG(config-rmon-interface)# rmon collection statistics 1 owner zteZXROSNG(config-rmon-interface)#2. 删除索引已存在的统计项：ZXROSNG(config-rmon-interface)#no rmon collection statistics 1
相关命令 : 
show rmon statistics 
## rmon event 

rmon event 
命令功能 : 
配置一个事件。使用no命令删除事件。
命令模式 : 
 RMON模式  
命令默认权限级别 : 
15 
命令格式 : 
rmon event 
  ＜index-number 
＞ [{[log 
],[trap 
 {encrypted 
 ＜encrypted snmp-name 
＞|clear 
 ＜snmp-name 
＞|＜snmp-name 
＞}],[description 
 ＜event-description 
＞],[owner 
 ＜event-owner 
＞]}]
no rmon event 
  ＜index-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜index-number＞|索引号，范围1~65535
log|记录标识
＜encrypted snmp-name＞|设置发送trap时所用的共同体串：密文方式，长度固定为64个字符
＜snmp-name＞|设置发送trap时所用的共同体串：明文方式，长度为1~32个字符
＜snmp-name＞|设置发送trap时所用的共同体串，长度为1~32个字符
＜event-description＞|该事件的一个简单描述，长度为1~127个字符，缺省为zte
＜event-owner＞|该事件的创建者，长度为1~31个字符，缺省为config
缺省 : 
无 
使用说明 : 
1. 以相同索引<index>创建事件项，提示出错。必须先no命令取消掉原相同索引的配置。2. 以相同索引<index-number>创建事件项，对于用户未输入的可选参数采用当前配置值。如果除<index-number>之外，其他所有参数和当前配置值有不一样的，则提示报错，此场景如果需要创建成功，则必须先no命令取消掉原相同索引的配置，再执行此创建操作。3. 由于内存或资源不可利用，提示"Alloc buffer error"或"Resource unavailable"。
范例 : 
1. 配置描述为log_trap_event的RMON事件，事件发生时纪录log日志同时发送trap信息给管理站，管理站的共同体为public：ZXROSNG(config-rmon)#rmon event 1 log trap public description log_trap_event owner zte2. 删除事件：ZXROSNG(config-rmon)#no rmon event 1 
相关命令 : 
show rmon events  
## rmon 

rmon 
命令功能 : 
从配置模式进入RMON模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rmon 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
进入rmon模式。 
范例 : 
1. 进入rmon模式：ZXROSNG(config)#rmonZXROSNG(config-rmon)
相关命令 : 
无 
## show rmon 

show rmon 
命令功能 : 
显示RMON配置和版本相关信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show rmon 
  [{[events 
],[history 
],[alarms 
],[statistics 
]}] 
命令参数解释 : 
参数|描述
---|---
events|显示所有配置事件控制条目当前信息和记录的事件信息
history|显示所有配置历史控制条目当前信息和历史统计信息
alarms|显示所有配置告警控制条目当前信息
statistics|显示所有配置统计控制条目当前信息和统计数据
缺省 : 
无 
使用说明 : 
1. 无参数时，显示RMON版本等信息。2. 如果指定的控制表无控制条目，则无任何回显信息。
范例 : 
1. 显示所有配置告警控制条目当前信息：ZXROSNG#show rmon alarmsAlarm 1 is valid, and owned by ZTE  Monitors ip.2.0,every 10 second(s)  Taking absolute samples,last value was 255  Rising-threshold is 200,assigned to event 1  Falling-threshold is 100,assigned to event 1 On startup enable rising or falling alarm2. 显示所有配置事件控制条目当前信息和记录的事件信息：ZXROSNG#show rmon eventsEvent 1 is valid, and owned by zte Description is log_trap_event  Event firing causes log and trap to community/user public, last fired 0w0d,00:03:36 Current log entries:   Index               Time                    Description   1                      0w0d,00:03:16        log_trap_event3. 显示所有配置告警控制条目当前信息和所有配置历史收集控制条目当前信息：ZXROSNG(config)#show rmon alarms history Alarm 1 is valid, and owned by config  Monitors ip.2.0, every 10 second(s)  Taking absolute samples, last value was 255  Rising-threshold is 1000, assigned to event 0  Falling-threshold is 500, assigned to event 0  On startup enable rising or falling alarmhistoryControlEntry 99 is valid, and owned by monitor  Monitors ifEntry.1.4 (gei-0/1/0/1) every 1800 seconds  Requested buckets is 50  Granted buckets is 50    Sample #1 began measuring at 0w2d,01:44:09      Received 5 octets, 10 packets,      25 broadcast and 30 multicast packets,      35 undersized and 40 oversized packets,      0 fragments and 0 jabbers,      15 CRC alignment errors and 0 collisions,      0 dropped packets (due to lack of resources).      Network utilization is estimated at 0    Sample #2 began measuring at 0w2d,02:14:09      Received 0 octets, 0 packets,      0 broadcast and 0 multicast packets,      0 undersized and 0 oversized packets,      0 fragments and 0 jabbers,      0 CRC alignment errors and 0 collisions,      0 dropped packets (due to lack of resources).      Network utilization is estimated at 0            
相关命令 : 
无 
# SFTP配置命令 
## copy sftp 

copy sftp 
命令功能 : 
该命令工作于特权模式当使用SFTP 客户端时，使用此命令与SFTP服务器端（一般为第三方SFTP服务器软件）进行文件的加密传输。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
copy sftp 
  [vrf 
 ＜vrf-name 
＞] {root: 
 ＜local-directory&filename 
＞ [＜CPU node information 
＞] {＜//host/file@username:password 
＞|{＜remote-ipv4-address 
＞|＜remote-ipv6-address 
＞} username 
 ＜username 
＞ path 
 ＜filepath 
＞}|{＜//host/file@username:password 
＞|{＜remote-ipv4-address 
＞|＜remote-ipv6-address 
＞} username 
 ＜username 
＞ path 
 ＜filepath 
＞} root: 
 ＜local-directory&filename 
＞ [＜CPU node information 
＞]} [{[encrypt 
 {none 
|aes128 
|blowfish 
|3des 
}],[compress 
 {none 
|zlib 
}],[mac 
 {none 
|sha1 
|md5 
}]}] [＜listen-port 
＞] [{＜local-ipv4-address 
＞|＜local-ipv6-address 
＞}] [interface 
 ＜interface-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|虚拟路由（VRF）名称。如VRF 名称为mng表示选择管理口取值范围：长度1–32位的字符串。可通过命令show ip vrf brief 查询。默认值：无。
＜local-directory&filename＞|SFTP客户端文件名或文件路径及文件名。用于下载指令。取值范围：纯文件名为1-79位的字符串，全路径为1-159位的字符串。 默认值：无。
＜CPU node information＞|用于指定操作文件的cpu信息，仅在输入的路径为绝对路径时有效，输入的路径为相对路径时不需要输入该参数。
＜//host/file@username:password＞|SFTP服务器端文件路径@用户名:密码。用于下载文件。取值范围：连同用户名及密码，合计1-230位的字符串。默认值：无。
＜remote-ipv4-address＞|SFTP服务端IPv4地址。
＜remote-ipv6-address＞|SFTP服务端IPv6地址。
＜username＞|SFTP用户名。为1-65位的字符串。
＜filepath＞|SFTP文件路径，全路径为1-159位的字符串。
＜//host/file@username:password＞|SFTP服务器端文件路径@用户名:密码。用于下载文件。取值范围：连同用户名及密码，合计1-230位的字符串。默认值：无。
＜remote-ipv4-address＞|SFTP服务端IPv4地址。
＜remote-ipv6-address＞|SFTP服务端IPv6地址。
＜username＞|SFTP用户名。为1-65位的字符串。
＜filepath＞|SFTP文件路径，全路径为1-159位的字符串。
＜local-directory&filename＞|SFTP客户端文件名或文件路径及文件名。用于下载指令。取值范围：纯文件名为1-79位的字符串，全路径为1-159位的字符串。 默认值：无。
＜CPU node information＞|用于指定操作文件的cpu信息，仅在输入的路径为绝对路径时有效，输入的路径为相对路径时不需要输入该参数。
none|MAC校验算法：不校验
aes128|加密算法：aes128
blowfish|加密算法：blowfish
3des|加密算法：3des
none|MAC校验算法：不校验
zlib|压缩算法：zlib
none|MAC校验算法：不校验
sha1|MAC校验算法：sha1
md5|MAC校验算法：md5
＜listen-port＞|侦听端口，与SSH服务器端开启的侦听端口号保持一致，否者建链失败。取值范围：1-65535默认值：22
＜local-ipv4-address＞|与local-ipv6-address为二选一，若为local-ipv4-address表示本端为IPv4地址
＜local-ipv6-address＞|与local-ipv4-address为二选一，若为local-ipv6-address表示本端为IPv6地址
interface|接口标识
＜interface-name＞|接口名称。当配置地址（本端或对端地址）为link-local地址时，需要指定此地址的出接口，可通过show ip interface brief查询。
缺省 : 
缺省情况下，监听端口号为22，本端IP地址为本地地址，不配置接口名。 
使用说明 : 
1.使用前保证SFTP 客户端与SFTP服务器通信能够互ping通。2.该命令支持文件的上传和下载操作，必须要指定本端和对端的文件名，要连接的SFTP服务器的IP地址，用户名和密码。 SFTP服务器的端口号和本地地址为可选项，如果不指定端口号，则默认连接SSH服务器的知名端口号22。3. 属性中的加密算法，压缩算法和HMAC较验算法由必选项改成可选项，当加密算法不选时，与SSH server协商时，提供所有支持的算法表项，先后顺序为：aes256-ctr、aes192-ctr、aes128-ctr、aes256-cbc、aes192-cbc、aes128-cbc、blowfish-cbc、3des-cbc、none；当压缩算法不选时，默认不支持压缩；当HMAC算法不选时，默认支持所有的算法列表选项，先后顺序为：hmac-sha2-256、hmac-sha1、hmac-md5、none。当需要支持强安全级别时，建议采用默认选项列表协商。4、如果使用copy sftp root: ＜local-directory&filename＞ ＜remote-ipv4-address＞|＜remote-ipv6-address＞ username ＜username＞ path ＜filepath＞ 命令格式上传，或 copy sftp  ＜remote-ipv4-address＞|＜remote-ipv6-address＞ username ＜username＞ path ＜filepath＞ root: ＜local-directory&filename＞ 命令格式下载，则该命令为动态交互命令，需要用户输入SFTP用户的密码。5、使用动态交互方式输入命令时，如果要在命令最后输入可选参数＜local-ipv4-address＞或＜local-ipv6-address＞，则可选参数的类型必须和前面输入的IP地址类型匹配。即远端地址使用IPv4地址＜remote-ipv4-address＞的话，如果有可选参数，则可选参数必须使用IPv4地址＜local-ipv4-address＞；远端地址使用IPv6地址＜remote-ipv6-address＞的话，可选参数则必须使用IPv6地址＜local-ipv6-address＞。
范例 : 
1.从FLASH的datadisk0目录下将文件db.dat拷到主机168.1.1.1的SFTP用户zxr10的工作目录上：ZXROSNG#copy sftp root: /datadisk0/db.dat //168.1.1.1/db.dat@zxr10:zxr10 encrypt aes128 compress zlib mac md5Connect successfully! Start copying file14% completed  00:00:20 ETA2，从主机168.1.1.1的SFTP用户zxr10的工作目录上将文件db.dat拷到路由器的根目录上：ZXROSNG#copy sftp //168.1.1.1/db.dat@zxr10:zxr10 root: db.dat encrypt aes128 compress zlib mac md53.从FLASH的datadisk0目录下将文件db.dat拷到主机168.1.1.1的SFTP用户zxr10的工作目录上，采用缺省算法：ZXROSNG#copy sftp root: /datadisk0/db.dat //168.1.1.1/db.dat@zxr10:zxr10100% completed  00:00:08Put file successfully! Sent 8096 bytes!4，从主机168.1.1.1的SFTP用户zxr10的工作目录上将文件db.dat拷到路由器的根目录上，采用缺省算法：ZXROSNG#copy sftp //168.1.1.1/db.dat@zxr10:zxr10 root: db.datConnect successfully! Start copying file100% completed  00:00:07Got file successfully! Received 8096 bytes!5、使用动态交互命令，从主机192.168.100.250的SFTP用户zte的工作目录上将文件b.dat通过端口50000拷贝到路由器根目录上的a.dat文件中：ZXROSNG#copy sftp vrf mng 192.168.100.250 username zte path b.dat root: a.dat 50000Password required for zte.Enter password: ***Connect successfully! Start copying file100% completed  00:00:00Got file successfully! Received 411 bytes!6、使用动态交互命令，从路由器根目录把a.dat文件通过端口50000拷贝到主机192.168.100.250的SFTP用户zte的工作目录中：ZXROSNG#copy sftp vrf mng root: a.dat 192.168.100.250 username zte path b.dat 50000Password required for zte.Enter password: ***Connect successfully! Start copying file100% completed  00:00:00Put file successfully! Sent 411 bytes!域信息说明：域信息：Connect successfully! Start copying file：提示信息，连接成功，开始拷贝100% completed：拷贝文件进度为100%00:00:08：拷贝文件用的总时间。时：分：秒的形式00:00:05 ETA：拷贝过程中显示，预计5秒钟之后拷贝完成。Got file successfully! Received 8096 bytes!：拷贝文件结束提示信息。下载文件成功，8096是接收到文件的字节数。Put file successfully! Sent 8096 bytes!：拷贝文件结束提示信息，上载文件成功,8096是发送文件的字节数。
相关命令 : 
copy ftpcopy tftp
## sftp-client source-interface 

sftp-client source-interface 
命令功能 : 
配置设备作为SFTP客户端时的源接口，接口地址作为copy sftp命令的源地址。使用no命令取消配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp-client source-interface 
  ＜interface-name 
＞
no sftp-client source-interface 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|源接口名称。字符串形式，长度为1-31个字符。
缺省 : 
缺省情况下，不配置SFTP客户端源接口。 
使用说明 : 
1.执行该命令指定源接口后，SFTP客户端发起建链时使用该接口的主地址（IPv4或IPv6主地址）作为本端地址；2.FTP客户端源地址的选取顺序依次是：copy sftp命令、sftp-client source-interface和sftp-client source-ip，即：1）如果copy sftp命令指定了源地址，则copy sftp命令发起的链接优先取本命令指定的源地址，若copy sftp命令中地址为linklocal地址，且只指定了接口未指定本端源地址，则获取此接口地址作为本端源地址；2）如果sftp-client source-interface与sftp-client source-ip同时配置，则本端发起的SFTP链接优先取源接口的地址，如果源接口无效，则取配置的源地址；3.使用no命令取消配置的源接口。
范例 : 
配置设备作为SFTP客户端时的监听接口：ZXROSNG(config)#sftp-client source-interface gei-0/1/0/1
相关命令 : 
sftp-client source-ipcopy sftpshow running-config sftp
## sftp-client source-ip ipv4 

sftp-client source-ip ipv4 
命令功能 : 
设备作为SFTP客户端传输文件时（包括上传和下载文件操作），配置文件传输的源IPv4地址。no sftp-client source-ip ipv4命令用于删除SFTP客户端源IPv4地址。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp-client source-ip ipv4 
  ＜ipv4-address 
＞
no sftp-client source-ip ipv4 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4地址，点分十进制格式，例如：192.168.1.1。
缺省 : 
缺省情况下，不配置SFTP客户端的源IPv4地址。 
使用说明 : 
1.命令用于指定copy sftp的源IPv4地址。2.SFTP客户端源地址的选取顺序依次是：copy sftp命令、sftp-client source-interface和sftp-client source-ip。3.使用no命令取消配置的源IPv4地址。
范例 : 
配置设备作为SFTP客户端时的源IPv4地址：ZXROSNG(config)# sftp-client source-ip ipv4 192.168.1.1
相关命令 : 
copy sftpsftp-client source-interfaceshow running-config sftp
## sftp-client source-ip ipv6 

sftp-client source-ip ipv6 
命令功能 : 
设备作为SFTP客户端传输文件时（包括上传和下载文件操作），配置文件传输的源IPv6地址。no sftp-client source-ip ipv6命令用于删除SFTP客户端源IPv6地址。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp-client source-ip ipv6 
  ＜ipv6-address 
＞ [interface 
 ＜interface-name 
＞]
no sftp-client source-ip ipv6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|IPv6地址，冒分十六进制格式，例如：200:fd05::d03e
＜interface-name＞|接口名称。字符串形式，长度为1-31个字符。
缺省 : 
缺省情况下，不配置SFTP客户端的源IPv6地址。 
使用说明 : 
1.命令用于指定copy sftp的源IPv6地址,仅当地址类型为linklocal时，需要指定接口。2.SFTP客户端源地址的选取顺序依次是：copy sftp命令、sftp-client source-interface和sftp-client source-ip。3.使用no命令取消配置的源IPv6地址。
范例 : 
配置设备作为SFTP客户端时的源IPv6地址：ZXROSNG(config)# sftp-client source-ip ipv6 100::1
相关命令 : 
copy sftpsftp-client source-interfaceshow running-config sftp
## sftp-server access-class 

sftp-server access-class 
命令功能 : 
通过命令配置SFTP服务端需要过滤的ACL规则的名称。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp-server access-class 
  {ipv4 
 ＜ACL name 
＞|ipv6 
 ＜ACL name 
＞}
no sftp-server access-class 
  {ipv4 
|ipv6 
}
				
命令参数解释 : 
参数|描述
---|---
ipv4|表示配置IPv4 ACL规则。
＜ACL name＞|表示配置IPv4或IPv6 ACL规则。
ipv6|表示配置IPv6 ACL规则。
＜ACL name＞|表示配置IPv4或IPv6 ACL规则。
缺省 : 
无 
使用说明 : 
1. 如果绑定的ACL名称不存在，配置能成功，但实际不生效；2. 允许绑定IPv4和IPv6两种类型的ACL规则各一个，重复执行相同类型的本命令时新配置将覆盖旧配置。
范例 : 
ZXROSNG(config)#sftp-server access-class ipv6 zte 
相关命令 : 
show sftp-server 
## sftp-server idle-timeout 

sftp-server idle-timeout 
命令功能 : 
通过命令配置方式设置SFTP服务端的最大链接空闲时间，可以使用no命令取消配置，恢复默认值。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp-server idle-timeout 
  ＜idle-time 
＞
no sftp-server idle-timeout 
命令参数解释 : 
参数|描述
---|---
＜idle-time＞|设定的最大链接空闲时间数，单位：分钟，取值范围0～1440，0表示始终不超时。
缺省 : 
默认是0分钟，始终不超时。 
使用说明 : 
1. 使用此命令配置SFTP会话的空闲超时时间后，SFTP会话会在到时后自动断开。若将空闲时间设置为0，则表示会话始终不会因超时断开；2. 使用no命令取消配置，恢复默认值0分钟，始终不超时；3. 修改空闲超时时间后，当前已处于空闲状态会话的超时时间不变，在下次进入空闲状态时开始安装新配置生效；
范例 : 
ZXROSNG(config)# sftp-server idle-timeout 30 
相关命令 : 
show sftp-server 
## sftp-server top-directory 

sftp-server top-directory 
命令功能 : 
该命令工作于全局配置模式，用于配置SFTP 服务器允许用户通过SFTP访问的顶级目录。此参数为配置SFTP服务器的必选参数，当未配置时，默认使用/datadisk0/作为根目录。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp-server top-directory 
  ＜user-top-directory 
＞ [{read-only 
|{[read-write 
],[copy 
]}}]
命令参数解释 : 
参数|描述
---|---
＜user-top-directory＞|用户可访问的SFTP服务器的目录的名称，必须是目录的完整的绝对路径。取值范围： 1-159位的字符串，单个目录长度不能超过80位字符，如参数为：/目录A/目录B/，“/目录A/目录B/”的总长度不能超过159位字符，目录A、目录B单个目录长度不能超过80位字符。默认目录：/datadisk0/。
read-only|只读权限
read-write|可读可写权限，（包含读、创建、修改、删除、不包含拷贝）
copy|可copy权限（包含 读、拷贝）
缺省 : 
默认情况下，SFTP SERVER允许用户通过SFTP访问的顶级目录是/datadisk0/。 
使用说明 : 
1.默认情况下，SFTP服务器允许用户通过SFTP访问的顶级目录是/datadisk0/，访问权限是所有权限。2.该命令的优先级低于用户授权模式中的sftp top-directory命令，当用户的授权模式没有配置sftp top-directory命令时，用户通过SFTP登录后可访问的顶级目录和访问权限以该命令为准。
范例 : 
设置用户的顶级工作目录为/datadisk0/zte/：ZXROSNG(config)#sftp-server top-directory /datadisk0/zte/  
相关命令 : 
show sftp-server 
## show sftp-server 

show sftp-server 
命令功能 : 
该命令工作于用户模式外的所有模式，用于查询SFTP服务器的相关配置信息和在线用户信息，包括SFTP的登记目录、用户ID、用户名、当前状态（在线、离线）登录的IP地址，以及端口号。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sftp-server 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show sftp-server -----------------------------------------------------------------
SFTP server idle timeout : 0SFTP server IPv4 ACL name : SFTP server IPv6 ACL name : SFTP server user top directory : /datadisk0/ SFTP server user top directory access permissions: read-write copyUser-ID Username            Status  IP-address             Port  Idle-time 1       zteztezte1zteztezte online  10.42.49.147           52699 00:00:07        1zteztezte1zteztezt                                              e1zteztezte1zteztez                                              te1zte11                                                 -----------------------------------------------------------------
相关命令 : 
show ftp-server 
# SNMP配置命令 
## group 

group 
命令功能 : 
配置USM用户的组，可以使用no命令删除配置。 
命令模式 : 
 SNMP-USM用户模式  
命令默认权限级别 : 
15 
命令格式 : 
group 
  ＜group-name 
＞
no group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|组名称，1-32个字符。
缺省 : 
缺省没有配置用户的组。 
使用说明 : 
该命令用于配置USM用户的组。可通过no命令删除配置。根据group表中筛选出的记录关联查找到view表的记录，看是否允许访问。
范例 : 
配置用户zte111的组是groupA：ZXROSNG(config)#snmp-server group groupA v3 priv read view1 write view2 notify view3ZXROSNG(config)#snmp-server usm-user engine-id 1234567890 user-name zte111ZXROSNG(config-snmp-usm-user)#group groupA
相关命令 : 
snmp-server groupsnmp-server usm-user
## security-protocol 

security-protocol 
命令功能 : 
配置USM用户的安全协议，可以使用no命令删除配置。 
命令模式 : 
 SNMP-USM用户模式  
命令默认权限级别 : 
15 
命令格式 : 
security-protocol 
  {noauth 
|auth 
 {encrypted 
 auth 
 {md5 
 ＜en-md5-auth-key 
＞|sha 
 ＜en-sha-auth-key 
＞}|clear 
 auth 
 {md5 
|sha 
} [＜clear-auth-key 
＞]}|priv 
 {encrypted 
 auth 
 {md5 
 ＜en-md5-auth-key 
＞|sha 
 ＜en-sha-auth-key 
＞} priv 
 {des56 
 ＜en-priv-key 
＞|aes128 
 ＜en-aes128-priv-key 
＞}|clear 
 auth 
 {md5 
|sha 
} {＜clear-auth-key 
＞ priv 
 {des56 
 ＜clear-priv-key 
＞|aes128 
 ＜clear-aes128-priv-key 
＞}|priv 
 {des56 
|aes128 
}}}}
no security-protocol 
命令参数解释 : 
参数|描述
---|---
noauth|安全级别：不认证不加密
auth|安全级别：认证不加密
encrypted|指定后面输入的不是口令原文而是经过处理的密钥，请慎重使用
md5|使用HMAC MD5-96作为认证方式。
＜en-md5-auth-key＞|MD5认证密钥，长度32-200个字符。
sha|使用HMAC SHA-96作为认证方式。
＜en-sha-auth-key＞|SHA认证密钥，长度40-200个字符。
clear|指定后面输入的是明文口令。
md5|使用HMAC MD5-96作为认证方式。
sha|使用HMAC SHA-96作为认证方式。
＜clear-auth-key＞|明文认证口令，长度1~32个字符。
priv|安全级别：认证且加密
encrypted|指定后面输入的不是口令原文而是经过处理的密钥，请慎重使用
md5|使用HMAC MD5-96作为认证方式。
＜en-md5-auth-key＞|MD5认证密钥，长度32个字符。
sha|使用HMAC SHA-96作为认证方式。
＜en-sha-auth-key＞|SHA认证密钥，长度40个字符。
des56|使用CBC-DES作为加密方式。
＜en-priv-key＞|DES加密密钥，长度32个字符。
aes128|使用CFB AES作为加密方式。
＜en-aes128-priv-key＞|CFB AES加密密钥，长度32个字符。
clear|指定后面输入的是明文口令。
md5|使用HMAC MD5-96作为认证方式。
sha|使用HMAC SHA-96作为认证方式。
＜clear-auth-key＞|明文认证口令，长度1~32个字符。
des56|使用CBC-DES作为加密方式。
＜clear-priv-key＞|DES明文加密口令，长度1~32个字符。
aes128|使用CFB AES作为加密方式。
＜clear-aes128-priv-key＞|CFB AES明文加密口令，长度1~32个字符。
des56|使用CBC-DES作为加密方式。
aes128|使用CFB AES作为加密方式。
缺省 : 
默认安全级别为不认证不加密 
使用说明 : 
1.该命令用于配置USM用户的安全协议，包括安全级别、认证协议和加密协议。2.安全级别为认证不加密时，明文认证口令支持交互式配置，即配置security-protocol auth clear auth {md5|sha}之后按Enter键即可进入交互式配置。3.安全级别为认证加密时，明文加密口令支持交互式配置，即配置security-protocol priv clear auth {md5|sha} priv {des56|aes128}之后按Enter键进入交互式配置，此交互式配置需要配置认证口令和加密口令。配置之后上翻会看配置时，认证密码和密文密码是以*号形式显示。
范例 : 
配置安全协议为认证加密方式，认证方式为HMAC MD5-96，明文认证口令为abcdef，加密方式为CBC-DES，明文加密口令为nanjjingzte：ZXROSNG(config)#snmp-server usm-user engine-id 00000f3e03a4fe0d7c5fb9ca user-name zteuser1ZXROSNG(config-snmp-usm-user)#security-protocol priv clear auth md5 abcdef priv des56 nanjjingzte配置安全协议为认证加密方式，认证方式为HMAC MD5-96，明文认证口令为abcdef，加密方式为CFB AES，明文加密口令为nanjjingzte：ZXROSNG(config)#snmp-server usm-user engine-id 00000f3e03a4fe0d7c5fb9ca user-name zteuser1ZXROSNG(config-snmp-usm-user)#security-protocol priv clear auth md5 abcdef priv aes128 nanjjingzte使用交互式方式配置用户为nanjing，安全协议为认证不加密方式的明文认证口令：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#snmp-server usm-user engine-id 00000f3e03a4fe0d7c5fb9ca user-name nanjingZXROSNG(config-snmp-usm-user)#security-protocol auth clear auth md5Please configure authentication password(1-32 characters)Password:**********Confirm password:**********使用交互式方式配置用户为nanjing，安全协议为认证加密方式的明文认证口令和加密口令：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#snmp-server usm-user engine-id 00000f3e03a4fe0d7c5fb9ca user-name nanjingZXROSNG(config-snmp-usm-user)#security-protocol priv clear auth md5 priv aes128Please configure authentication password(1-32 characters)Password:*****************Confirm password:*****************Please configure privacy password(1-32 characters)Password:******************Confirm password:******************
相关命令 : 
snmp-server usm-user  
## show snmp config 

show snmp config 
命令功能 : 
此命令用于查看SNMP当前所有的配置信息。在配置SNMP相关的命令前，建议通过show snmp config查询SNMP已有的配置，再决定是否需要配置相关的命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show snmp config 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show snmp config输出信息如下：snmp-server community private showclear view AllView rwsnmp-server engine-id is 830900020300010289d64401snmp-server group zte v3 noauth context xyz match-prefix read DefaultView notify AllViewsnmp-server packetsize is 8192snmp-server user xyz groupname zte v3 snmp-server context is xyzsnmp-server view AllView internet includedsnmp-server view DefaultView system includedsnmp-server security dynamic-trust-user idle-timeout 1800 snmp-server listen-port is 161snmp-server version v2c enablesnmp-server version v3 enablesnmp-server log enable allsnmp-server input-limit 200
相关命令 : 
无 
## show snmp engine-id 

show snmp engine-id 
命令功能 : 
此命令用于显示SNMP的本地引擎ID，引擎ID唯一地标识一个SNMP实体。SNMP引擎是SNMP实体中的核心部分，完成SNMP消息的收发验证，提取PDU组装消息，以及SNMP应用程序通信等功能。引擎ID只有在SNMP v3版本才存在，可以通过snmp-server engine-id命令修改。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show snmp engine-id 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show snmp engine-idthe engine-id:830900020300010289d64401 
相关命令 : 
无 
## show snmp group 

show snmp group 
命令功能 : 
此命令用于显示SNMP的用户组信息。一个用户可以关联一个或多个组，用户组用来关联操作的视图范围。可以通过show snmp group查询每个用户所关联的用户组信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show snmp group 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show snmp group输出信息如下：groupName :ztesec_Model :v3sec_Level :NOAUTHreadView :DefaultViewwriteView :<no writeView specified>notifyView:AllViewrowStatus :ACTIVEcontextName :xyzcontextMatch :match-prefix
相关命令 : 
无 
## show snmp security 

show snmp security 
命令功能 : 
此命令用于查询SNMP安全功能信息，包括SNMP 的ACL配置信息、动态和静态信任用户信息、是否设置防攻击监控等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show snmp security 
  [{failures 
|trust-users 
}] 
命令参数解释 : 
参数|描述
---|---
failures|可选参数，选择该参数时，命令功能为查询连接失败的详细信息（包括IP地址、尝试登录的时间等）
trust-users|可选参数，选择该参数时，命令功能为查询信任用户的详细信息。（包括动态/静态用户的IP地址、动态用户的记录时间以及动态用户老化的时间）
缺省 : 
显示当前SNMP安全功能参数 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show snmp securityNo access list about ipv4 has been configured.No access list about ipv6 has been configured.No static trust-user has been configured.No dynamic trust-user has been learned.The max idle timeout of dynamic trust-user is default.All failed requests are neither logged nor generated SNMP traps.Router is not enable to watch for Attacks.Router presently in Normal-Mode.
相关命令 : 
无 
## show snmp user 

show snmp user 
命令功能 : 
此命令用于查看SNMP用户的信息  
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show snmp user 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show snmp userusername   :zteengine-id  :830900020300010289d64401auth_type  :NONEgroup_name :group1(v3)encryptType:NONEstorageType:NONVOLATILErow_status :ACTIVE
相关命令 : 
无 
## show snmp 

show snmp 
命令功能 : 
此命令用于查看SNMP的报文统计、侦听端口号和版本功能使能信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show snmp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
Show snmp前面提示的数字为报文的个数。 
范例 : 
ZXROSNG(config)#show snmp 285       SNMP packets input0         Bad SNMP version errors0         Unknown community name0         Illegal operation for community name supplied1073      Number of requested variables400       Number of altered variables27        Get-request PDUs247       Get-next PDUs4         Set-request PDUs77946     SNMP packets output0         Too big errors (Maximum packet size 61440)0         No such name errors0         Bad values errors0         General errors285       Response PDUs77661     Trap PDUs SNMP0         Input ASN parse errors packets0         Proxy drops packets0         Unknown security model packets0         Unknown PDU handler packets0         Unsupported security level packets0         Not in time-window packets0         Unknown user name packets0         Unknown engine ID packets0         Wrong digest packets0         Decryption error packetsSNMP version v1: disableSNMP version v2c: enableSNMP version v3: disableSNMP agent listen port: 161SNMP notification listen port: 162SNMP command-responser: enableSNMP proxy-forwarder: enable其中统计信息和状态信息含义如下：SNMP packets input：SNMP接收的消息总数；Bad SNMP version errors：SNMP接收的不支持的版本的报文总数；Unknown community name：SNMP接收的无法识别community名称的报文总数；Illegal operation for community name supplied：SNMP接收的、请求的操作是报文中携带的community名称所不允许的报文总数；Number of requested variables：SNMP因处理get和get-next请求而成功检索的MIB对象总数；Number of altered variables：SNMP因处理set请求而成功修改的MIB对象总数；Get-request PDUs：SNMP接收并处理的Get-Request PDU总数；Get-next PDUs：SNMP接收并处理的Get-Next-Request PDU总数；Set-request PDUs：SNMP接收并处理的Set-Request PDU总数；SNMP packets output：SNMP发送的消息总数；Too big errors (Maximum packet size 61440)：SNMP发送的error-status错误状态是“tooBig”的PDU总数；No such name errors：SNMP发送的error-status错误状态是“noSuchName”的PDU总数；Bad values errors：SNMP发送的error-status错误状态是“badValue”的PDU总数；General errors：SNMP发送的error-status错误状态是“genErr”的PDU总数；Response PDUs：SNMP发送的Get-Response PDU总数；Trap PDUs SNMP：SNMP发送的trap PDU和inform PDU的总数；Input ASN parse errors packets：SNMP在解码接收的消息时遇到ASN.1或BER的错误数；Proxy drops packets：SNMP接收的因为无法找到proxy转发目标而丢弃的GetRequest-PDU、GetNextRequest-PDU、GetBulkRequest-PDUs、SetRequest-PDU和InformRequest-PDU总数；Unknown security model packets：接收的报文中因为引用的安全模型securityModel是SNMP引擎不能识别或不支持的，而被SNMP引擎丢弃的报文总数；Unknown PDU handler packets：接收的报文中因为包含的PDU无法找到可以处理的SNMP应用，而被SNMP引擎丢弃的报文总数；Unsupported security level packets：接收的报文中因为要求的安全级别securityLevel是SNMP引擎不能识别的或其他无效原因，而被SNMP引擎丢弃的报文总数；Not in time-window packets：接收的报文中因为超出授权SNMP引擎时间窗，而被SNMP引擎丢弃的报文总数；Unknown user name packets：接收的报文中因为引用的用户是SNMP引擎不能识别的，而被SNMP引擎丢弃的报文总数；Unknown engine ID packets：接收的报文中因为引用的引擎snmpEngineID是SNMP引擎不能识别的，而被SNMP引擎丢弃的报文总数；Wrong digest packets：接收的报文中因为没有包含期望的摘要值，而被SNMP引擎丢弃的报文总数；Decryption error packets：接收的报文中因为不能被解密，而被SNMP引擎丢弃的报文总数；SNMP version v1：SNMPv1版本的启动状态；SNMP version v2c：SNMPv2c版本的启动状态；SNMP version v3：SNMPv3版本的启动状态；SNMP agent listen port：SNMP代理的侦听端口；SNMP notification listen port：侦听通知的端口；SNMP command-responser：SNMP命令响应功能的启动状态；SNMP proxy-forwarder：SNMP PROXY转发功能的启动状态。
相关命令 : 
无 
## snmp-server access-list ipv4 

snmp-server access-list ipv4 
命令功能 : 
该命令在config模式下执行，用于配置IPv4类型的ACL，系统根据此ACL来控制某些IPv4地址是否能通过SNMP协议访问主机系统 。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server access-list ipv4 
  ＜acl-name 
＞
no snmp-server access-list ipv4 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL过滤规则的名称,长度为1~31字符
缺省 : 
无 
使用说明 : 
要使该命令配置生效，需要为IPv4地址类型的acl-name配置过滤规则，过滤规则需要在ipv4-access-list 和rule命令配置。
范例 : 
允许ACL名称为aaa控制的IPv4地址通过SNMP访问设备：ZXROSNG(config)#snmp-server access-list ipv4 aaa
相关命令 : 
snmp-server communityipv4-access-list rule
## snmp-server access-list ipv6 

snmp-server access-list ipv6 
命令功能 : 
该命令在config模式下执行，用于配置IPv6类型的ACL，系统根据此ACL来控制某些IPv6地址是否能通过SNMP协议访问主机系统 。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server access-list ipv6 
  ＜acl-name 
＞
no snmp-server access-list ipv6 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL过滤规则的名称,长度为1~31字符
缺省 : 
无 
使用说明 : 
要使该命令配置生效，需要为IPv6地址类型的acl-name配置过滤规则，过滤规则需要通过ipv6-access-list,rule两条命令配置。 
范例 : 
允许ACL名称为bbb控制的IPv6地址通过SNMP访问设备：ZXROSNG(config)#snmp-server access-list ipv6 bbb
相关命令 : 
ipv6-access-list rule
## snmp-server community check 

snmp-server community check 
命令功能 : 
设置SNMP团体串复杂度检查策略。使用NO命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server community check 
 min-length 
 ＜length 
＞ [min-char-set-num 
 ＜min-num 
＞]
no snmp-server community check 
命令参数解释 : 
参数|描述
---|---
＜length＞|设置团体串的最小长度，范围：10-32
＜min-num＞|团体串至少包含字符集的种类，范围：2-4,默认值：3
缺省 : 
无 
使用说明 : 
1.配置此命令之后就会开启团体串复杂度检查，若配置的团体串不符合检查策略，将会报错提示不符合团体串检查策略。2.密码字符策略包括4种（数字、大写字母、小写字母、特殊字符），特殊字符不包括“?”和空格。若不指定支持字符种类，默认支持数字，大写字母，小写字母，特殊字符中的任意三类。
范例 : 
配置团体串复杂度检查策略为：长度至少为12，包含4种字符集：ZXROSNG(config)#snmp-server community check min-length 12 min-char-set-num 4
相关命令 : 
snmp-server community 
## snmp-server community 

snmp-server community 
命令功能 : 
该命令在config模式下执行，用于配置SNMP团体串，SNMP通过配置团体串来限制不同团体串的网管具有不同级别的访问权限。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server community 
  {encrypted 
 ＜encrypted-para 
＞|[＜unencrypted-para 
＞] [showclear 
]} [view 
 ＜view-name 
＞] [{ro 
|rw 
}] [{[ipv4-access-list 
 ＜ipv4_acl_name 
＞],[ipv6-access-list 
 ＜ipv6_acl_name 
＞]}]
no snmp-server community 
  {encrypted 
 ＜encrypted-para 
＞|＜unencrypted-para 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜encrypted-para＞|密文团体串 64-200个字符长度
＜unencrypted-para＞|明文团体串 1~32个字符
showclear|配置该字show团体串时，用明文显示；不配置该字段为密文显示
＜view-name＞|视图名 1~32个字符
ro|操作权限-只读
rw|操作权限-读写
＜ipv4_acl_name＞|IPv4 ACL 名称，范围1-31个字符串
＜ipv6_acl_name＞|IPv6 ACL 名称，范围1-31个字符串
缺省 : 
当缺省view关键词时，将为配置的共同体指定默认视图（1.3.6.1.2.1.1）；当缺省ro | rw关键词时，将为配置的共同体指定默认权限ro 
使用说明 : 
如果网管需要通过SNMPv2或者SNMPv1协议连接系统，就必须配置团体串，并且网管下发的团体串需要与已配置的团体串的其中之一匹配才能功能连接。只有SNMP v1和v2版本中才使用团体串，v3版本没有团体串的概念。团体串名称可配置长度为1-32个字符。建议同时满足以下三个条件：    团体串长度不小于6。    同时含有字母与数字。    同时含有大小写。如不满足以上三个条件，能配置成功和使用同时设备会提示团体串不够安全。缺省关键字说明如下：    当配置缺省view关键词时，将为配置的共同体指定默认视图。    当缺省ro | rw关键词时，将为配置的共同体指定默认权限ro。团体串命令中的ipv4-access-list和ipv6-access-list参数配置会影响 snmp-server access-list ipv4和snmp-server access-list ipv6命令，当团体串中的这两个参数生效后，snmp-server access-list ipv4和snmp-server access-list ipv6相应的配置就不会生效。SNMP团体串配置最多支持50条。可以通过no 命令删除团体串配置。若不指定明文或者密文团体串，按Enter键之后将进入交互式配置方式配置团体串。在配置之后，上翻查看配置时，团体串以*显示。
范例 : 
设置SNMP报文共同体myCommunity，选择密文显示，并具备读写访问权限：ZXROSNG(config) #snmp-server community myCommunity view AllView rw交互式方式配置团体串：ZXROSNG#configure terminalZXROSNG(config)#snmp-server community view myView rwPlease configure communityCommunity:*********Confirm community:*********
相关命令 : 
snmp-server viewsnmp-server access-list ipv4snmp-server access-list ipv6
## snmp-server community-map 

snmp-server community-map 
命令功能 : 
配置团体串和VRF的关联关系，no命令用于删除关联关系 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server community-map 
  ＜map-name 
＞ {encrypted-community 
 ＜encrypted-community-string 
＞|clear-community 
 [＜clear-community-string 
＞] [showclear 
]} vrf 
 ＜vrf-name 
＞
no snmp-server community-map 
  ＜map-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜map-name＞|关联关系名称。1~32个字符长度。
＜encrypted-community-string＞|密文团体串名称。64-200个字符长度。
＜clear-community-string＞|明文团体串名称，1~32个字符长度。
showclear|showclear为可选参数，如果选择，则在show run中显示明文，否则显示密文
＜vrf-name＞|关联VRF名称。1~32个字符长度。
缺省 : 
缺省无配置。 
使用说明 : 
1.该命令用于配置团体串和VRF的关联关系，当配置了团体串和VRF关联，则仅允许包含在关联VRF的主机使用该团体串访问SNMP。2.若不指定明文或者密文团体串，按Enter键之后将进入交互式配置方式配置团体串。
范例 : 
配置团体串snmp-sample和名称为vrfNj的VRF关联：ZXROSNG(config)#snmp-server community-map map1 clear-community  snmp-sample vrf vrfNj配置团体串映射名为JSnanJing，动态交互式配置团体串与名为vrfNJ的VRF关联：ZXROSNG#configure terminalZXROSNG(config)#snmp-server community-map JSnanJing clear-community vrf vrfNJPlease configure communityCommunity:*********Confirm community:*********
相关命令 : 
snmp-server community 
## snmp-server context 

snmp-server context 
命令功能 : 
该命令在config模式下执行，用于设置SNMP上下文标识的名称，SNMP上下文（SNMP context）是SNMP实体可以访问的管理信息的集合。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server context 
  ＜context 
＞
no snmp-server context 
  ＜context 
＞
				
命令参数解释 : 
参数|描述
---|---
＜context＞|上下文名称，长度1–30个字符
缺省 : 
无 
使用说明 : 
使用该命令前，建议先在一个路由模式下配置路由标识，若只是配置一个SNMP上下标识名称是没有意义的，具体配置可以参照范例。context命令最多可以配置50条。使用no命令可以删除相应的配置。
范例 : 
配置SNMP上下文标识名称，配置ISIS模块上下文名称：ZXROSNG(config)#router isisZXROSNG(config-isis-0)#snmp context zteZXROSNG(config-isis-0)#exitZXROSNG(config)#snmp-server context zte
相关命令 : 
无 
## snmp-server enable inform 

snmp-server enable inform 
命令功能 : 
该命令在config模式下执行，用于打开代理发送通知的开关，并设置代理发送的通知类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server enable inform 
  [＜inform-type 
＞]
no snmp-server enable inform 
  [＜inform-type 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜inform-type＞|通知类型，可以是BGP，OSPF，RMON，SNMP，STALARM，VPN等其中之一
缺省 : 
缺省发送所有通知。 
使用说明 : 
该命令在缺省参数时，默认配置所有通知类型。SNMP模块支持48种通知类型。使用no命令可删除相应的配置。该命令需要与snmp-server host命令配置使用才能发送通知，比如该命令设置了BGP类型的通知，同时也要在snmp-server host命令中设置BGP类型，这样BGP模块才能发送通知，否者就不发送。
范例 : 
使能BGP模块的通知功能：ZXROSNG(config)#snmp-server enable inform bgp
相关命令 : 
无 
## snmp-server enable trap 

snmp-server enable trap 
命令功能 : 
该命令在config模式下执行，用于打开代理发送陷阱的开关，并设置代理能发送的陷阱类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server enable trap 
  [＜trap-type 
＞]
no snmp-server enable trap 
  [＜trap-type 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜trap-type＞|指定陷阱类型，可以是BGP，OSPF，RMON，SNMP，STALARM，VPN等其中之一
缺省 : 
缺省发送所有陷阱 
使用说明 : 
该命令在缺省参数时，默认配置所有陷阱类型。SNMP模块支持48种陷阱类型。使用no命令可删除相应的配置。该命令需要与snmp-server host命令配置使用才能发送陷阱，比如该命令设置了BGP类型的陷阱，同时也要在snmp-server host命令中设置BGP类型，这样BGP模块才能发送陷阱，否者就不发送。
范例 : 
打开OSPF陷阱开关：ZXROSNG(config)#snmp-server enable trap ospf
相关命令 : 
snmp-server host 
## snmp-server engine-id 

snmp-server engine-id 
命令功能 : 
该命令在config模式下执行，用于设置SNMP的本地引擎ID。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server engine-id 
  ＜engineid 
＞
no snmp-server engine-id 
命令参数解释 : 
参数|描述
---|---
＜engineid＞|本地SNMP引擎ID，长度为1–24个字符，缺省为830900020300010289d64401，必须用16进制数字表示
缺省 : 
缺省为830900020300010289d64401 
使用说明 : 
本地SNMP引擎ID是由24位16进制的数组成，在设置引擎ID时，参数不足24位时，后面会用0补全。本地SNMP默认的引擎ID是830900020300010289d64401，通过show snmp engine-id命令可以查看引擎ID，使用no 命令可以还原为默认引擎ID。修改引擎ID后，如果现有配置包含以下三个命令，需要重新配置一遍：1、snmp-server user，按照明文方式重新配置一遍。2、snmp-server usm-user模式下的security-protocol,按照明文方式重新配置一遍。3、snmp-server community-map-entry，此命令部分项目支持。如果引擎ID配置的是本地的。需要重新配置一下。
范例 : 
设置SNMP本地引擎ID为123456678901。ZXROSNG(config)#snmp-server engine-id   123456678901查看配置结果信息：ZXROSNG(config)#show snmp engine-id      the engine-id:1234566789010000000000000 
相关命令 : 
无 
## snmp-server get-next-cache age 

snmp-server get-next-cache age 
命令功能 : 
配置get-next操作时缓存老化周期 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server get-next-cache age 
  ＜age-time 
＞
no snmp-server get-next-cache age 
命令参数解释 : 
参数|描述
---|---
＜age-time＞|缓存更新时间，范围：1-30，单位：秒
缺省 : 
无 
使用说明 : 
此命令仅仅对get-next操作生效。当配置了缓存老化的时间，get-next操作时，会直接从缓存中读取数据，上报网管。此功能应用于读取数据较多，且要读取的MIB表支持快速读取功能。 
范例 : 
设置get-next缓存老化时间为5秒：ZXROSNG(config)#snmp-server get-next-cache age 5
相关命令 : 
无 
## snmp-server group 

snmp-server group 
命令功能 : 
该命令在config模式下执行，用于配置SNMP的一个用户组以及该组所关联的访问视图。登录SNMPv3版本，需要配置一个用户，该用户需要关联一个或多个用户组。所谓视图是指一个被管理对象的集合。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server group 
  ＜group-name 
＞ v3 
 {noauth 
|auth 
|priv 
} [context 
 ＜context-name 
＞ {match-prefix 
|match-exact 
}] [read 
 ＜read-view 
＞] [write 
 ＜write-view 
＞] [notify 
 ＜notify-view 
＞]
no snmp-server group 
  ＜group-name 
＞ v3 
 {noauth 
|auth 
|priv 
} [context 
 ＜context-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|用户关联的组名
v3|指定该组用于v3版本
noauth|指明对报文不进行认证和加密
auth|指明对报文进行认证但不加密
priv|指明对报文进行认证和加密
＜context-name＞|指定该组所属的上下文
match-prefix|指明上下文匹配模式为前缀匹配
match-exact|指明上下文匹配模式为精确匹配
＜read-view＞|读视图，范围1–32个字符
＜write-view＞|写视图，范围1–32个字符
＜notify-view＞|通知视图，范围1–32个字符
缺省 : 
无 
使用说明 : 
SNMP支持最大可配50条用户组，可通过no命令删除配置。 
范例 : 
设置SNMPv3组group1，安全级别为认证并加密，读视图，写视图，通知视图的视图名均为view1。ZXROSNG(config)#snmp-server group group1 v3 priv read view1 write view1 notify view1      
相关命令 : 
无 
## snmp-server host domain 

snmp-server host domain 
命令功能 : 
用于设置接收SNMP通知或陷阱的DNS名称、发送通知或陷阱的端口号、SNMP版本号以及可触发通知或陷阱的模块类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server host domain 
  ＜host domain name 
＞ {ipv4 
|ipv6 
} [vrf 
 ＜vpnname 
＞] {trap 
|inform 
 [{[engine-id 
 ＜engine-id 
＞],[timeout 
 ＜timeout 
＞],[retry-count 
 ＜retry-count 
＞]}]} version 
 {{1 
|2c 
} {[＜communitystring 
＞] [showclear 
]|encrypted 
 ＜encrypted-para 
＞}|3 
 {{noauth 
|auth 
|priv 
}} ＜security-name 
＞} [udp-port 
 ＜udpport 
＞] [{[snmp 
],[bgp 
],[mac 
],[ospf 
],[stp 
],[ppp 
],[arp 
],[rmon 
],[udld 
],[cfm 
],[efm 
],[lacp 
],[mc-elam 
],[tcp 
],[sctp 
],[stalarm 
],[cps 
],[interface 
],[acl 
],[fib 
],[pim 
],[isis 
],[rip 
],[msdp 
],[aps 
],[config 
],[am 
],[um 
],[system 
],[ldp 
],[pwe3 
],[vpn 
],[mpls-oam 
],[ptp 
],[tunnel-te 
],[radius 
],[dhcp 
],[bfd 
],[ippool 
],[ntp 
],[ssm 
],[sqa 
],[ipsec 
],[cgn 
],[vrrp 
],[ftp_tftp 
],[ping-trace 
],[gm 
]}]
no snmp-server host domain 
  ＜host domain name 
＞ [vrf 
 ＜vpnname 
＞] {trap 
|inform 
} {＜clear-security-str 
＞|encrypted 
 ＜encrypted-para 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜host domain name＞|DNS域名名称，长度：1-128个字符
ipv4|指定域名的名称为ipv4
ipv6|指定域名的名称为ipv6
＜vpnname＞|VRF名称，长度：1-32个字符
trap|指定发送陷阱到主机
inform|指定发送通知到主机
＜engine-id＞|引擎ID，长度为：10-64，十六进制字符
＜timeout＞|超时时间，范围：100-3000
＜retry-count＞|超时重传次数：0-255
1|指定SNMP版本号为1
2c|指定SNMP版本号为2c
＜communitystring＞|团体串名，长度1–32个字符
showclear|该参数可选，表示show命令显示该配置时以明文的方式显示团体串，否则以密文的方式显示
＜encrypted-para＞|以密文的方式设置向主机发送SNMPv1和SNMPv2c版本的通知或陷阱时的团体串，长度64-200个字符
3|指定SNMP版本号为3
noauth|指明对报文不进行认证和加密
auth|指明对报文进行认证但不加密
priv|指明对报文进行认证和加密
＜security-name＞|设置SNMPv3版本通知或陷阱的安全名称，即用户名称，长度1~32个字符
＜udpport＞|指定发送trap 的udp端口号，范围：1–65535，默认值：162
snmp|指定陷阱或通知类型为snmp
bgp|指定陷阱或通知类型为bgp
mac|指定陷阱或通知类型为mac
ospf|指定陷阱或通知类型为ospf
stp|指定陷阱或通知类型为stp
ppp|指定陷阱或通知类型为ppp
arp|指定陷阱或通知类型为arp
rmon|指定陷阱或通知类型为rmon
udld|指定陷阱或通知类型为udld
cfm|指定陷阱或通知类型为cfm
efm|指定陷阱或通知类型为efm
lacp|指定陷阱或通知类型为lacp
mc-elam|指定陷阱或通知类型为mc-elam
tcp|指定陷阱或通知类型为tcp
sctp|指定陷阱或通知类型为sctp
stalarm|指定陷阱或通知类型为stalarm
cps|指定陷阱或通知类型为cps
interface|指定陷阱或通知类型为interface
acl|指定陷阱或通知类型为acl
fib|指定陷阱或通知类型为fib
pim|指定陷阱或通知类型为pim
isis|指定陷阱或通知类型为isis
rip|指定陷阱或通知类型为rip
msdp|指定陷阱或通知类型为msdp
aps|指定陷阱或通知类型为aps
config|指定陷阱或通知类型为config
am|指定陷阱或通知类型为am
um|指定陷阱或通知类型为um
system|指定陷阱或通知类型为system
ldp|指定陷阱或通知类型为ldp
pwe3|指定陷阱或通知类型为pwe3
vpn|指定陷阱或通知类型为vpn
mpls-oam|指定陷阱或通知类型为mpls-oam
ptp|指定陷阱或通知类型为ptp
tunnel-te|指定陷阱或通知类型为tunnel-te
radius|指定陷阱或通知类型为radius
dhcp|指定陷阱或通知类型为dhcp
bfd|指定陷阱或通知类型为bfd
ippool|指定陷阱或通知类型为ippool
ntp|指定陷阱或通知类型为ntp
ssm|指定陷阱或通知类型为ssm
sqa|指定陷阱或通知类型为sqa
ipsec|指定陷阱或通知类型为ipsec
cgn|指定陷阱或通知类型为cgn
vrrp|指定陷阱或通知类型为vrrp
ftp_tftp|指定陷阱或通知类型为ftp_tftp
ping-trace|指定陷阱或通知类型为ping_trace
gm|指定陷阱或通知类型为gm
No参数|描述
---|---
＜clear-security-str＞|明文安全名，长度：1-32个字符
缺省 : 
无 
使用说明 : 
1.若要模块触发通知或陷阱，不仅需要配置snmp-server host domain命令，还要配置snmp-server enable命令打开上报通知或陷阱的开发及设置可触发通知或陷阱的模块类型。2.若host命令中的可触发通知或陷阱的模块类型的参数缺省时，则配置全部模块类型。3.snmp-server host doamin命令最多支持配置50条，若超过50条则报错。4.当配置接收SNMP通知或陷阱的目的主机时，可选参数如果不选择或不指定，则默认取值为：若不选择showclear选项以密文的方式显示团体串。5.陷阱或通知业务类型：若不指定业务类型，则默认通知的业务类型为所有业务类型。6.两次配置索引一致，业务不一致时，是增量配置。例如：同一个索引，第一次指定业务类型是ISIS，第二次指定了BGP，那么该索引会支持ISIS和BGP两种业务。7.snmp-server host 命令直接指定目的IP地址，而snmp-server host domain命令是指定DNS名称，通过DNS服务器查到目的地址。两条命令是平行并列的关系。8.在历史命令信息中即show history显示信息中，正向和反向命令的团体串信息均是以 ******的形式呈现。9.在命令日志信息中即show logfile 显示信息中，正向和反向命令的团体串新均是以******的形式呈现。10.当SNMP的版本号为1或者2c时，若不配置团体串，按Enter键之后将进入交互式配置方式配置团体串。11.在配置之后，上翻查看配置时，团体串以*显示。
范例 : 
配置trap发送的目的DNS名称为nanjingzte，DNS指向的地址为IPv4类型，使用SNMP v2c版本，用户名为zte,支持接收ISIS模块trap通知：ZXROSNG(config)#snmp-server host domain nanjingzte ipv4 trap version 2c zte isis配置通知方式inform, 发送的目的DNS名称为zte，DNS指向的地址为IPv6类型显示,使用SNMP 3版本，用户名为zte,支持接收全部模块trap通知：ZXROSNG(config)#snmp-server host domain zte ipv6 inform version 3 auth zte配置snmp模块的trap信息发送的目的DNS名称为www.njzte.com,DNS指向的地址为IPv4类型，使用SNMP v2c版本，团体串采用交互式模式配置：ZXROSNG#configure terminalZXROSNG(config)#snmp-server host domain www.njzte.com ipv4 trap version 2c snmpPlease configure communityCommunity:*********************Confirm community:*********************
相关命令 : 
snmp-server enablesnmp-server communitysnmp-server user
## snmp-server host 

snmp-server host 
命令功能 : 
该命令在config模式下执行，用于设置接收SNMP通知或陷阱的目的地址、发送通知或陷阱的端口号、SNMP版本号以及可触发通知或陷阱的模块类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server host 
  [vrf 
 ＜vpnname 
＞] {＜ipv6addr 
＞|＜ipv4addr 
＞} {trap 
|inform 
 [{[timeout 
 ＜timeout 
＞],[retry-count 
 ＜retry-count 
＞],[engine-id 
 ＜engine-id 
＞]}]} version 
 {{1 
|2c 
} {[＜communitystring 
＞] [showclear 
]|encrypted 
 ＜encrypted-para 
＞}|3 
 {{noauth 
|auth 
|priv 
}} ＜security-name 
＞} [udp-port 
 ＜udpport 
＞] [{[snmp 
],[bgp 
],[mac 
],[ospf 
],[stp 
],[ppp 
],[arp 
],[rmon 
],[udld 
],[cfm 
],[efm 
],[lacp 
],[mc-elam 
],[tcp 
],[sctp 
],[stalarm 
],[cps 
],[interface 
],[acl 
],[fib 
],[pim 
],[isis 
],[rip 
],[msdp 
],[aps 
],[config 
],[am 
],[um 
],[system 
],[ldp 
],[pwe3 
],[vpn 
],[mpls-oam 
],[ptp 
],[tunnel-te 
],[radius 
],[dhcp 
],[bfd 
],[ippool 
],[ntp 
],[ssm 
],[sqa 
],[ipsec 
],[cgn 
],[vrrp 
],[ftp_tftp 
],[ping-trace 
],[gm 
]}]
no snmp-server host 
  [vrf 
 ＜vpnname 
＞] {＜ipv6addr 
＞|＜ipv4addr 
＞} {trap 
|inform 
} {＜clear-security-str 
＞|encrypted 
 ＜encrypted-para 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜vpnname＞|test
＜ipv6addr＞|指定主机的IPv4类型地址
＜ipv4addr＞|指定主机的IPv6类型地址
trap|指定发送陷阱到主机
inform|指定发送通知到主机
＜timeout＞|超时时间，范围：100-3000，单位10 ms ,默认值：无
＜retry-count＞|重传次数，范围：0-255，默认值：无
＜engine-id＞|引擎ID，长度：10-64个可变长的字符。默认值：无
1|指定SNMP版本号为1
2c|指定SNMP版本号为2c
＜communitystring＞|团体串名，长度1–32个字符
showclear|该参数可选，表示show命令显示该配置时以明文的方式显示团体串，否则以密文的方式显示
＜encrypted-para＞|以密文的方式设置向主机发送SNMPv1和SNMPv2c版本的通知或陷阱时的团体串，长度64-200个字符
3|指定SNMP版本号为3
noauth|指明对报文不进行认证和加密
auth|指明对报文进行认证但不加密
priv|指明对报文进行认证和加密
＜security-name＞|设置SNMPv3版本通知或陷阱的安全名称，即用户名称，长度1~32个字符
＜udpport＞|指定发送trap 的udp端口号，范围：1–65535
snmp|指定陷阱或通知类型为snmp
bgp|指定陷阱或通知类型为bgp
mac|指定陷阱或通知类型为mac
ospf|指定陷阱或通知类型为ospf
stp|指定陷阱或通知类型为stp
ppp|指定陷阱或通知类型为ppp
arp|指定陷阱或通知类型为arp
rmon|指定陷阱或通知类型为rmon
udld|指定陷阱或通知类型为udld
cfm|指定陷阱或通知类型为cfm
efm|指定陷阱或通知类型为efm
lacp|指定陷阱或通知类型为lacp
mc-elam|指定陷阱或通知类型为mc-elam
tcp|指定陷阱或通知类型为tcp
sctp|指定陷阱或通知类型为sctp
stalarm|指定陷阱或通知类型为stalarm
cps|指定陷阱或通知类型为cps
interface|指定陷阱或通知类型为interface
acl|指定陷阱或通知类型为acl
fib|指定陷阱或通知类型为fib
pim|指定陷阱或通知类型为pim
isis|指定陷阱或通知类型为isis
rip|指定陷阱或通知类型为rip
msdp|指定陷阱或通知类型为msdp
aps|指定陷阱或通知类型为aps
config|指定陷阱或通知类型为config
am|指定陷阱或通知类型为am
um|指定陷阱或通知类型为um
system|指定陷阱或通知类型为system
ldp|指定陷阱或通知类型为ldp
pwe3|指定陷阱或通知类型为pwe3
vpn|指定陷阱或通知类型为vpn
mpls-oam|指定陷阱或通知类型为mpls-oam
ptp|指定陷阱或通知类型为ptp
tunnel-te|指定陷阱或通知类型为tunnel-te
radius|指定陷阱或通知类型为radius
dhcp|指定陷阱或通知类型为dhcp
bfd|指定陷阱或通知类型为bfd
ippool|指定陷阱或通知类型为ippool
ntp|指定陷阱或通知类型为ntp
ssm|指定陷阱或通知类型为ssm
sqa|指定陷阱或通知类型为sqa
ipsec|指定陷阱或通知类型为ipsec
cgn|指定陷阱或通知类型为cgn
vrrp|指定陷阱或通知类型为vrrp
ftp_tftp|指定陷阱或通知类型为ftp_tftp
ping-trace|指定陷阱或通知类型为ping-trace
gm|指定陷阱或通知类型为gm
No参数|描述
---|---
＜clear-security-str＞|明文安全名称，长度：1-32个字符
缺省 : 
缺省没有配置接收SNMP通知或陷阱的目的主机。当配置接收SNMP通知或陷阱的目的主机时，可选参数如果不选择或不指定，则默认取值为： [ vrf <vrf-name> ]：默认公网。[showclear]：默认不选择，即以密文的方式显示团体串。[ udp-port <udp-port> ]：默认端口号162。陷阱或通知业务类型：默认通知的业务类型为所有业务类型。
使用说明 : 
1.若要模块触发通知或陷阱，不仅需要配置snmp-server host命令，还要配置snmp-server enable命令打开上报通知或陷阱的开发及设置可触发通知或陷阱的模块类型。2.若host命令中的可触发通知或陷阱的模块类型的参数缺省时，则配置全部模块类型。3.snmp-server host命令最多支持配置50条，可通过no命令删除配置。4.超时重传时间如果不配置则使用snmp-server inform中配置的超时重传时间。默认值15秒。5.在历史命令信息中即show history显示信息中，正向和反向命令的团体串信息均是以 ******的形式呈现。在命令日志信息中即show logfile 显示信息中，正向和反向命令的团体串新均是以******的形式呈现。6.当SNMP的版本号为1或者v2c时，若不配置团体串，按Enter键之后将进入交互式配置方式配置团体串。
范例 : 
1.    配置trap发送的主机地址，团体串明文配置，密文显示：ZXROSNG(config)#snmp-server host vrf Nanjing 168.1.1.1 trap version 2c admin udp-port 2000 bgp ospf stalarm 2.    配置trap发送的主机地址，团体串明文配置，明文显示：ZXROSNG(config)#snmp-server host vrf Nanjing 168.1.1.1 trap version 2c admin showclear udp-port 2000 bgp ospf stalarm 3.    配置trap发送的主机地址，团体串密文配置，密文显示：ZXROSNG(config)#snmp-server host vrf Nanjing 168.1.1.1 trap version 2c encrypted 9c4f4f90640343e20b73886220b01a5a594f84277f76191aa3347d9f6a578978 udp-port 2000 bgp ospf stalarm 4.配置system模块的inform发送的主机地址，交互式配置团体串：ZXROSNG(config)#snmp-server host vrf mng 192.168.100.250 trap version 2c systemPlease configure communityCommunity:**********Confirm community:**********
相关命令 : 
snmp-server enable  snmp-server communitysnmp-server user
## snmp-server inform 

snmp-server inform 
命令功能 : 
配置全局的Inform参数。no命令用于删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server inform 
  {[timeout 
 ＜inform timeout 
＞],[retry-count 
 ＜retry-count 
＞],[max-pending 
 ＜max-pending 
＞]}
no snmp-server inform 
命令参数解释 : 
参数|描述
---|---
＜inform timeout＞|超时时间，范围100-3000，单位0.01秒，默认值1500。
＜retry-count＞|重传次数，范围0-255，默认值3
＜max-pending＞|最大待确认inform数量，范围1-2048，默认值200。
缺省 : 
没有配置全局inform参数时，超时时间为15秒，重传3次，最大待确认inform数量为200。 
使用说明 : 
该命令用于配置全局inform参数时，默认超时时间为5秒，重传3次，最大待确认inform数量为200。若host命令中配置了inform的超时时间、inform的重传次数，则以host命令为准，否则以全局inform 配置为准。
范例 : 
设置inform超时时间为10秒，重传次数为5 ：ZXROSNG(config)#snmp-server inform timeout 1000 retry-count 5 max-pending 100
相关命令 : 
snmp-server host 
## snmp-server input-limit 

snmp-server input-limit 
命令功能 : 
该命令在config模式下执行，用于设置SNMP处理报文的速率。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server input-limit 
  ＜limit-para 
＞
no snmp-server input-limit 
命令参数解释 : 
参数|描述
---|---
＜limit-para＞|SNMP处理报文的速率，范围为100-1000之间的整数，单位：个/秒。
缺省 : 
无 
使用说明 : 
默认情况下SNMP处理报文的速率为200个每秒，使用no 命令可以还原成默认配置。 
范例 : 
设置SNMP处理报文速率为300个/秒。ZXROSNG(config)#snmp-server input-limit 300
相关命令 : 
无 
## snmp-server listen-port 

snmp-server listen-port 
命令功能 : 
该命令在config模式下执行，用于配置SNMP代理的侦听UDP端口号，侦听端口是用来侦听SNMP协议报文。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server listen-port 
  {＜default listen port-number 
＞|＜port-number 
＞}
no snmp-server listen-port 
命令参数解释 : 
参数|描述
---|---
＜default listen port-number＞|默认情况下，SNMP代理的侦听UDP端口号是161
＜port-number＞|SNMP代理的侦听UDP端口号，范围1024~20000
缺省 : 
默认情况下，SNMP代理的侦听UDP端口号是161 
使用说明 : 
1.snmp-server listen-port 命令用于配置SNMP协议侦听UDP端口号，只能配置一个，多次配置时，后面的配置覆盖前面的。2.SNMP协议侦听UDP端口号默认为161，可以使用no snmp-server listen-port 命令恢复默认值。3.需SNMPv1、SNMPv2c、SNMPv3功能都关闭时，才可以修改侦听端口。
范例 : 
1.配置SNMP协议侦听UDP端口号为2000：ZXROSNG(config)#snmp-server listen-port 2000
相关命令 : 
show running-configshow snmp config
## snmp-server packetsize 

snmp-server packetsize 
命令功能 : 
该命令在config模式下执行，用于设置SNMP组织报文的最大长度。当命令配置成功后，若SNMP组织给网管的回应报文超过所设置的最大长度，就会返回一个toobig错误码给网管。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server packetsize 
  ＜pkt-size 
＞
no snmp-server packetsize 
命令参数解释 : 
参数|描述
---|---
＜pkt-size＞|SNMP组织报文的最大长度，范围为484–61440，单位为字节。
缺省 : 
默认值为8192 
使用说明 : 
SNMP组织报文的最大长度默认值为8192字节，使用no 命令可以还原为默认设置。 
范例 : 
设置SNMP最大报文长度为8192字节。ZXROSNG(config)#snmp-server packetsize 8192
相关命令 : 
无 
## snmp-server security block 

snmp-server security block 
命令功能 : 
该命令在config模式下执行，用于配置SNMP安全功能的模式转换参数。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server security block 
  ＜Block-Second 
＞ ＜Detect-Try 
＞ ＜Detect-Second 
＞ [when 
 ＜Startup-Try 
＞ ＜Startup-Second 
＞]
no snmp-server security block 
命令参数解释 : 
参数|描述
---|---
＜Block-Second＞|阻塞时间（安静期的时长），范围：1–65535，单位：秒
＜Detect-Try＞|监测模式的最大失败尝试次数，范围：1–65535
＜Detect-Second＞|监测模式的最大检测时间，范围：1–65535，单位：秒
＜Startup-Try＞|正常模式的最大失败尝试次数，默认为50，范围：1–65535
＜Startup-Second＞|正常模式的最大检测时间，默认60秒，范围：1–65535，单位：秒
缺省 : 
无 
使用说明 : 
SNMP安全防护功能默认是不启用的。打开安全功能，SNMP存在三种状态：正常模式、监测模式和阻塞模式。     当SNMP安全功能打开时，SNMP就处于正常模式；。    当用户在正常模式设置的时间内，团体串尝试登录失败超过设置的次数据，则SNMP进入监测模式；。    当用在监测模式设置的时间内，团体串尝试登录失败超过设置的次数据，则SNMP进入阻塞模式。当在阻塞模式下时，SNMP拒绝任何访问。
范例 : 
配置设备在60秒内团体串尝试失败超过10次则启动监测模式，在监测模式100秒内团体串尝试失败次数超过15次则进入阻塞模式，阻塞模式的时间为200秒：ZXROSNG(config)#snmp-server security block 200 15 100 when 10 60 
相关命令 : 
无 
## snmp-server security dynamic-trust-user clear 

snmp-server security dynamic-trust-user clear 
命令功能 : 
该命令在config模式下执行，用于删除动态信任用户。当SNMP开启安全功能时，SNMP会记录成功登录SNMP的用户，即为动态信任用户。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server security dynamic-trust-user clear 
  {＜ipv4-addr 
＞|＜ipv6-addr 
＞}
命令参数解释 : 
参数|描述
---|---
＜ipv4-addr＞|动态信任用户的ipv4类型地址
＜ipv6-addr＞|动态信任用户的ipv6类型地址
缺省 : 
无 
使用说明 : 
动态信任用户有老化时间，是通过snmp-server security dynamic-trust-user idle-timeout 命令来设置，当动态用户超过这个老化时间，将会被删除。 
范例 : 
手工清除动态信任用户192.168.10.49：ZXROSNG(config)#snmp-server security dynamic-trust-user clear 192.168.10.49    
相关命令 : 
无 
## snmp-server security dynamic-trust-user idle-timeout 

snmp-server security dynamic-trust-user idle-timeout 
命令功能 : 
该命令在config模式下执行，用于配置动态信任用户的老化时间。当动态用户超过这个老化时间，将会被删除。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server security dynamic-trust-user idle-timeout 
  ＜Idle-Timeout 
＞
no snmp-server security dynamic-trust-user idle-timeout 
命令参数解释 : 
参数|描述
---|---
＜Idle-Timeout＞|动态信任用户老化时间，默认值是1800秒，范围：1–65535，单位：秒
缺省 : 
无 
使用说明 : 
SNMP的默认动态信任用户的老化时间为1800秒，可通过no命令还原为默认配置。 
范例 : 
配置动态信任用户老化时间为1200秒。ZXROSNG(config)#snmp-server security dynamic-trust-user idle-timeout 1200
相关命令 : 
无 
## snmp-server security on-failure 

snmp-server security on-failure 
命令功能 : 
该命令在config模式下执行，用于配置由网管用错误的团体串失败而引起的SNMP安全状态转换时生成日志信息和陷阱上报。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server security on-failure 
 log 
 [and 
 trap 
]
no snmp-server security on-failure 
命令参数解释 : 
参数|描述
---|---
log|指定生成日志信息。
trap|指定上报陷阱。
缺省 : 
无 
使用说明 : 
若想生成日志信息，在配置该命令之前，先打开SNMP安全功能，即用snmp-server security block命令配置。若想上报陷阱，在配置该命令之前，先用snmp-server enable trap 和snmp-server host命令打上报陷阱的开关和设置上报陷阱的模块类型。用no 命令删除相关配置。
范例 : 
配置在有团体串尝试失败时生成日志信息和Trap信息。ZXROSNG(config)#snmp-server security on-failure log and trap
相关命令 : 
无 
## snmp-server security static-trust-user 

snmp-server security static-trust-user 
命令功能 : 
该命令在config模式下执行，用于配置静态信任用户。静态用户只能通过手动配置，不能像动态用户那样由SNMP自动学习，也只能通过手动来删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server security static-trust-user 
  {＜ipv4-addr 
＞|＜ipv6-addr 
＞}
no snmp-server security static-trust-user 
  {＜ipv4-addr 
＞|＜ipv6-addr 
＞|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-addr＞|静态信任用户IPv4类型地址
＜ipv6-addr＞|静态信任用户ipv6类型的地址
No参数|描述
---|---
all|删除所有配置
缺省 : 
无 
使用说明 : 
SNMP支持配置20静态信任用户，可通过no 命令删除配置。 
范例 : 
配置静态信任用户192.168.10.66。ZXROSNG(config)#snmp-server security static-trust-user 192.168.10.66 
相关命令 : 
无 
## snmp-server trap-source 

snmp-server trap-source 
命令功能 : 
用于指定SNMP TRAP的源地址。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server trap-source 
  {＜ipv4addr 
＞|ipv6-addr 
 ＜ipv6addr 
＞|interface 
 ＜interface 
＞}
no snmp-server trap-source 
  [{ipv4-addr 
|ipv6-addr 
|interface 
}]
				
命令参数解释 : 
参数|描述
---|---
＜ipv4addr＞|IPv4地址
＜ipv6addr＞|IPv6地址（不支持linklocal地址）
＜interface＞|接口名
No参数|描述
---|---
ipv4-addr|IPv4地址
ipv6-addr|IPv6地址
interface|接口
缺省 : 
无 
使用说明 : 
1.    该命令用于配置SNMP所有版本的trap消息的源地址。SNMP v1版本Trap中的agent address也受该命令影响。2.    如果该命令仅配置了IPv4地址，当向IPv4地址的host主机发送Trap消息时，源地址和v1版本Trap中的agent address都为该命令配置的IPv4地址；当向IPv6地址的host主机发送Trap消息时，源地址由传输协议指定，v1版本Trap中的agent address不指定。3.    如果该命令仅配置了IPv6地址，当向IPv6地址的host主机发送Trap消息时，源地址为该命令配置的IPv6地址，v1版本Trap中的agent address不指定；当向IPv4地址的host主机发送Trap消息时，源地址由传输协议指定，v1版本Trap中的agent address不指定。4.    如果该命令仅配置关联接口，当向IPv4地址的host主机发送Trap消息时，如果接口有主IPv4地址，源地址和v1版本Trap中的agent address都为该命令配置的IPv4地址，否则源地址由传输协议指定，v1版本Trap中的agent address不指定；当向IPv6地址的host主机发送Trap消息时，如果接口有IPv6地址，则源地址为接口配置的第一个IPv6地址，v1版本Trap中的agent address不指定，否则源地址由传输协议指定，v1版本Trap中的agent address不指定。5.    如果同时配置了IPv4地址、IPv6地址和引用接口，则优先使用接口的配置，如果接口没有配置主IPv4地址或IPv6地址，则再使用该命令配置的IPv4地址或IPv6地址，具体为：当向IPv4地址的host主机发送Trap消息时，如果接口有主IPv4地址，源地址和v1版本Trap中的agent address都为该命令配置的IPv4地址，否则如果该命令有配置IPv4地址，则源地址和v1版本Trap中的agent address都为该命令配置的IPv4地址，如果没有配置IPv4地址，则源地址由传输协议指定，v1版本Trap中的agent address不指定；当向IPv6地址的host主机发送Trap消息时，如果接口有IPv6地址，则源地址为接口配置的第一个IPv6地址，v1版本Trap中的agent address不指定，否则如果该命令有配置IPv4地址，则源地址为该命令配置的IPv6地址，v1版本Trap中的agent address不指定，如果没有配置IP地址，则源地址由传输协议指定，v1版本Trap中的agent address不指定。6.    缺省情况下，该命令无配置，所有Trap消息的源地址由传输协议指定，v1版本Trap中的agent address使用管理口的主IPv4地址，如果管理口没有主IPv4地址，则使用环回地址127.0.0.1。7.    no命令不带参数时，默认删除所有相关配置。
范例 : 
1.设置SNMP所有TRAP源IP地址为192.168.10.10。ZXROSNG(config)#snmp-server trap-source 192.168.10.102.配置源地址引用接口gei-1/1/2/1的地址。ZXROSNG(config)#snmp-server trap-source interface gei-1/1/2/13.配置源地址为128::1。ZXROSNG(config)#snmp-server trap-source ipv6-addr 128::1
相关命令 : 
show running-configshow snmp config
## snmp-server usm-user 

snmp-server usm-user 
命令功能 : 
配置USM用户，并进入“SNMP-USM用户模式”。可以使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server usm-user 
 engine-id 
 ＜engine-id 
＞ user-name 
 ＜user-name 
＞
no snmp-server usm-user 
  {engine-id 
 ＜engine-id 
＞ user-name 
 ＜user-name 
＞|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜engine-id＞|引擎ID，长度24个字符，每个字符都是一个十六进制数字
＜user-name＞|用户名， 长度1~32个字符
No参数|描述
---|---
all|删除所有配置
缺省 : 
无 
使用说明 : 
指定不存在的引擎ID或用户名，则创建一个USM用户，并进入“SNMP-USM用户模式”，配置的用户信息在转发功能打开时会使用。若引擎ID和用户名已存在，则进入“SNMP-USM用户模式”。最多可以创建500个USM用户。引擎ID和用户名是每个USM用户条目的唯一索引
范例 : 
ZXROSNG(config)#snmp-server usm-user engine-id 00000f3e03a4fe0d7c5fb9ca user-name zteuser1ZXROSNG(config-snmp-usm-user)#
相关命令 : 
snmp-server proxy-forwarder 
## snmp-server version 

snmp-server version 
命令功能 : 
该命令在config 模式下执行，用于使能SNMP的v1、v2c和v3版本。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server version 
  {v1 
|v2c 
|v3 
} enable 
no snmp-server version 
  {v1 
|v2c 
|v3 
}
				
命令参数解释 : 
参数|描述
---|---
v1|版本类型 v1
v2c|版本类型 v2c
v3|版本类型 v3
enable|使能指定版本类型
缺省 : 
缺省三个版本都为去使能 
使用说明 : 
SNMP默认的三个版本全部是disable。通过no命令可以disable SNMP版本。
范例 : 
使能SNMP的v2c版本ZXROSNG(config)#snmp-server version v2c enable
相关命令 : 
本命令从ZXROSNG V5.00.30版本开始支持项目M6000-1S
## snmp-server view 

snmp-server view 
命令功能 : 
该命令在config模式下执行，用于定义SNMP的视图。SNMP视图是一个被管理对象的集合。SNMP视图用于控制用户的访问权限。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
snmp-server view 
  ＜view-name 
＞ ＜view-subid 
＞ {included 
|excluded 
}
no snmp-server view 
  ＜view-name 
＞ [＜view-subid 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜view-name＞|视图名称，长度1–32个字符
＜view-subid＞|为视图名指定MIB子树ID或MIB子树的节点名，长度1–79个字符
included|包括该子树
excluded|排除该子树
缺省 : 
缺省为AllView与DefaultView 
使用说明 : 
SNMP支持最大可配48条视图，AllView和DefaultView是两条默认的配置。AllView视图包括1.3.6.1子树，DefaultView视图包括1.3.6.1.1.1子树。当用于通知上报时，还要检查报文中trapoid字段，检查权限是否在view范围内。通过no命令可删除配置。
范例 : 
定义SNMP的视图ZXROSNG(config)#snmp-server view view2 1.3.6.1 included
相关命令 : 
无 
# SQA配置命令 
## debug sqa all 

debug sqa all 
命令功能 : 
打开SQA 所有诊断开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug sqa all 
 
no debug sqa all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1、拥有管理员权限的操作员可以使用这条命令。2、该命令工作在特权模式下。3、用户可以通过ctrl+d 组合键来关闭该诊断开关。
范例 : 
ZXROSNG#debug sqa  allSQA all debugging is on
相关命令 : 
无 
## debug sqa event 

debug sqa event 
命令功能 : 
打开SQA  事件诊断开关。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug sqa event 
  [test-id 
 ＜test id 
＞]
no debug sqa event 
命令参数解释 : 
参数|描述
---|---
＜test id＞|作用：指定测试ID号范围：1-1024，最大值根据性能参数自动调整默认值：无
缺省 : 
无
使用说明 : 
1、拥有管理员权限的操作员可以使用这条命令。2、该命令工作在特权模式下。3、用户可以通过ctrl+d 组合键来关闭该诊断开关。
范例 : 
ZXROSNG#debug sqa  event test-id 1SQA event debugging is on for test 1ZXROSNG#
相关命令 : 
无 
## debug sqa packet 

debug sqa packet 
命令功能 : 
打开SQA  报文诊断开关。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug sqa packet 
  [test-id 
 ＜test id 
＞]
no debug sqa packet 
命令参数解释 : 
参数|描述
---|---
＜test id＞|作用：指定测试ID号范围：1-1024，最大值根据性能参数自动调整默认值：无
缺省 : 
无 
使用说明 : 
1、拥有管理员权限的操作员可以使用这条命令。2、该命令工作在特权模式下。3、用户可以通过ctrl+d 组合键来关闭该诊断开关。
范例 : 
ZXROSNG#debug sqa  packet test-id 1SQA event debugging is on for test 1ZXROSNG#
相关命令 : 
无 
## send-trap 

send-trap 
命令功能 : 
设置TRAP功能，当需要开启或者关闭trap功能时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
send-trap 
  {enable 
 ＜trap-percent 
＞|disable 
}
命令参数解释 : 
参数|描述
---|---
＜trap-percent＞|作用：开启trap告警，并设置告警阈值。范围：1-100。默认值：无。
disable|作用：关闭trap告警。范围：无。默认值：disable。
缺省 : 
缺省为disable。 
使用说明 : 
使用enable开启SQA检测实例，并可以配置告警阈值，当实例丢包率达到阈值时即产生告警；使用disable关闭SQA检测实例的告警功能，即使检测不成功也不会有告警产生
范例 : 
在SQA模式下，配置trap功能：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-udp 192.168.1.98 10000 repeat 10ZXROSNG(config-sqa-40)#send-trap enable 80查看trap的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-udp 192.168.1.98 10000 repeat 10send-trap enable 80!!</SQA>
相关命令 : 
show sqa-testshow running-config sqa
## show debug sqa 

show debug sqa 
命令功能 : 
查看SQA debug 诊断开关的开启情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug sqa 
 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#show debug sqaSQA:  SQA event debugging is on  SQA packet debugging is onZXROSNG#
相关命令 : 
无 
## show sqa-result dns 

show sqa-result dns 
命令功能 : 
显示DNS类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result dns 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
DNS类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过DNS类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看DNS的检测结果：ZXROSNG(config)#show sqa-result dnsdns test[5] resultSendPackets:5  ResponsePackets:0Completion:successDestination-url:abc.cnDNS Interpret IP Address: Min/Max/Avg/Sum/Last RTT:0/0/0/0/0msLast Probe Time:2011-09-01 23:55:41检测结果数据描述：数据    描述SendPackets    该检测的请求次数ResponsePackets    请求成功的次数DNS Interpret IP Address    解析出来的IP地址Min/Max/Avg/Sum RTT    请求用时最小值，最大值，平均值，总和的统计Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-dnssqa-begin
## show sqa-result ftp 

show sqa-result ftp 
命令功能 : 
显示FTP类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result ftp 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
FTP类型检测完成后可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过FTP类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看FTP的检测结果：ZXROSNG(config)#show sqa-result ftpftp test[4] resultCompletion:successLast RTT:80s  Bytes Read:15668921Last Probe Time:2011-09-01 23:55:54检测结果数据描述：数据    描述Last RTT    传输文件的用时Bytes Read    传输文件的Byte数Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-ftpsqa-begin
## show sqa-result http 

show sqa-result http 
命令功能 : 
显示HTTP类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result http 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
HTTP类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过HTTP类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看HTTP的检测结果：ZXROSNG(config)#show sqa-result httphttp test[122] resultSendPackets:1 ResponsePackets:1Completion:success  Destination ip address:192.168.1.1Min/Max/Avg/Sum/Num DNS:1011/1011/1011/1011ms/1Min/Max/Avg/Sum/Num TCP:10/10/10/10ms/1Min/Max/Avg/Sum/Num HTTP:110/110/110/110ms/1Min/Max/Avg/Sum/Num SUM:1131/1131/1131/1131ms/1Last Probe Time:2011-12-05 15:13:00检测结果数据描述：数据    描述SendPackets    该检测的请求次数ResponsePackets    请求成功的次数Destination ip address    如果配置的域名，则是经过域名解析出的ip地址，如果配置的是ip地址，则就是该网址Min/Max/Avg/Sum/Num DNS    如果配置的域名，经过域名解析用时的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum/Num TCP    建立tcp连接用时的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum/Num HTTP    从发送http报文到接收到http应答用时的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum RTT    该次检测（包括域名解析，tcp连接，报文发送和接收）用时的最小值，最大值，平均值，总和的统计Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-httpsqa-begin
## show sqa-result icmp 

show sqa-result icmp 
命令功能 : 
显示ICMP类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result icmp 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
ICMP类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过ICMP类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看ICMP的检测结果：icmp test[1] resultSendPackets:20  ResponsePackets:20Completion:success  Destination IP Address:192.0.0.100Min/Max/Avg/Sum RTT:29/99/39/787msMin/Max/Avg/Sum Positive Jitter:1/7/3/9msMin/Max/Avg/Sum Negative Jitter:1/70/35/71msMin/Max/Avg/Sum Jitter:1/70/16/80msPacket loss rate:0%Last Probe Time:2011-11-18 01:57:38检测结果数据描述：数据    描述SendPackets    该检测的发包个数ResponsePackets    该检测的收包个数Min/Max/Avg/Sum RTT    RTT最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Positive Jitter:    正抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Negative Jitter    负抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Jitter    抖动（不区分正负）的最小值，最大值，平均值，总和的统计Packet loss rate    丢包率Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-icmpsqa-begin
## show sqa-result icmpjitter 

show sqa-result icmpjitter 
命令功能 : 
显示ICMPjitter类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result icmpjitter 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
ICMPjitter类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过ICMPjitter类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看ICMP的检测结果：ZXROSNG(config-sqa)#show sqa-result icmpjitter icmp jitter test[1] resultSendPackets:10  ResponsePackets:10Completion:success  Destination IP Address: 192.0.0.100Min/Max/Avg/Sum Positive SD:1/4/2/5msMin/Max/Avg/Sum Negative SD:1/1/1/1msMin/Max/Avg/Sum Positive DS:1/1/1/2msMin/Max/Avg/Sum Negative DS:1/1/1/1msMin/Max/Avg/Sum SD:7/12/10/107msMin/Max/Avg/Sum DS:1/1/1/10msLast Probe Time:2012-09-19 02:59:32    数据                                           描述SendPackets                     该检测的发包个数ResponsePackets                 该检测的收包个数Min/Max/Avg/Sum Positive SD     源端到目的端正向抖动最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Negative SD     源端到目的端负向抖动最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Positive DS     目的端到源端正向抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Negative DS     目的端到源端负向抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum SD              源端到目的端RTT的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum DS              目的端到源端RTT的最小值，最大值，平均值，总和的统计Last Probe Time                 检测结束的时间
相关命令 : 
sqa-test type-icmp-jittersqa-begin
## show sqa-result snmp 

show sqa-result snmp 
命令功能 : 
显示SNMP类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result snmp 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
SNMP类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过SNMP类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看SNMP的检测结果：ZXROSNG(config)#show sqa-result snmp  SNMP test[121] resultCompletion:success  RTT:100msLast Probe Time:2011-12-05 15:12:07检测结果数据描述：数据    描述RTT    该次snmp探测所用的时间Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-snmpsqa-begin
## show sqa-result tcp 

show sqa-result tcp 
命令功能 : 
显示TCP类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result tcp 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
TCP类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过TCP类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看TCP的检测结果：ZXROSNG(config)#show sqa-result tcptcp test[3] resultSendPackets:10  ResponsePackets:10Completion:success  Destination IP Address:192.0.0.111Min/Max/Avg/Sum RTT:10/50/16/160msLast Probe Time:2011-09-01 23:53:00检测结果数据描述：数据    描述SendPackets    该检测的请求次数ResponsePackets    建立tcp链接成功的次数Min/Max/Avg/Sum RTT    请求用时最小值，最大值，平均值，总和的统计Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-tcpsqa-begin
## show sqa-result udp 

show sqa-result udp 
命令功能 : 
显示UDP类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result udp 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
UDP类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过UDP类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看UDP的检测结果：ZXROSNG(config)#show sqa-result udp  udp test[2] resultSendPackets:10  ResponsePackets:10Completion:success  Destination IP Address:192.0.0.111Min/Max/Avg/Sum RTT:61/63/62/622msMin/Max/Avg/Sum Positive Jitter:0/0/0/0msMin/Max/Avg/Sum Negative Jitter:1/1/1/2msMin/Max/Avg/Sum Jitter:1/1/1/2msPacket loss rate:0%Last Probe Time:2011-09-01 23:52:35检测结果数据描述：数据    描述SendPackets    该检测的发包个数ResponsePackets    该检测的收包个数Min/Max/Avg/Sum RTT    RTT最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Positive Jitter:    正抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Negative Jitter    负抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Jitter    抖动（不区分正负）的最小值，最大值，平均值，总和的统计Packet loss rate    丢包率Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-udpsqa-begin
## show sqa-result udpjitter 

show sqa-result udpjitter 
命令功能 : 
显示UDPjitter类型检测的结果，当该类型的实例检测结束，可以使用该命令查看检测结果 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-result udpjitter 
  [＜entity-number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜entity-number＞|SQA检测的测试实例号，范围：1-150
缺省 : 
无 
使用说明 : 
UDPjitter类型检测完成后,可以使用该命令查看检测结果，目前支持保存最新的12个检测结果;使用该命令前，需要执行过UDPjitter类型的实例检测，如果没有执行过，则不显示任何信息
范例 : 
在全局配置模式下，查看UDP jitter的检测结果：ZXROSNG(config)#show sqa-result udpjitter  udp jitter test[120] resultSendPackets:20  ResponsePackets:20Completion:success  Destination IP Address:192.0.0.100Min/Max/Avg/Sum Positive SD:1/6/4/30msMin/Max/Avg/Sum Negative SD:1/45/6/75msMin/Max/Avg/Sum Positive DS:2/7/3/26msMin/Max/Avg/Sum Negative DS:1/10/4/26msMin/Max/Avg/Sum SD:10/65/18/373msMin/Max/Avg/Sum DS:46/57/51/1020msSD dispose num:0  DS dispose num:0Last Probe Time:2011-12-05 15:11:34检测结果数据描述：数据    描述SendPackets    该检测的发包个数ResponsePackets    该检测的收包个数Min/Max/Avg/Sum Positive SD    源端到目的端正向抖动最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Negative SD    源端到目的端负向抖动最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Positive DS    目的端到源端正向抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum Negative DS    目的端到源端负向抖动的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum SD    源端到目的端RTT的最小值，最大值，平均值，总和的统计Min/Max/Avg/Sum DS    目的端到源端RTT的最小值，最大值，平均值，总和的统计SD dispose num    源端到目的端的单向丢包率DS dispose num    目的端到源端的单向丢包率Last Probe Time    检测结束的时间
相关命令 : 
sqa-test type-udp-jittersqa-begin
## show sqa-server tcp 

show sqa-server tcp 
命令功能 : 
显示SQA 的TCP server的配置，当需要查询TCP server的配置信息时，使用此命令 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-server tcp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
可以查看TCP server的配置情况;如果没有配置过TCP类型的server，则不显示任何信息
范例 : 
在全局配置模式下，查看TCP server的配置情况：ZXROSNG(config)#show sqa-server tcp            sqa tcp server:listen IP:192.0.0.111listen port:1025
相关命令 : 
sqa-tcp-server 
## show sqa-server udp 

show sqa-server udp 
命令功能 : 
显示SQA 的UDP server的配置，当需要查询UDP server的配置信息时，使用此命令 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-server udp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
可以查看UDP server的配置情况;如果没有配置过UDP类型的server，则不显示任何信息
范例 : 
在全局配置模式下，查看UDP server的配置情况：ZXROSNG(config)#show sqa-server udp sqa udp server:listen IP:192.0.0.111listen port:1025
相关命令 : 
sqa-udp-server 
## show sqa-test 

show sqa-test 
命令功能 : 
用于显示SQA的配置信息，当需要显示某实例配置信息时使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sqa-test 
  ＜entity-num 
＞ 
命令参数解释 : 
参数|描述
---|---
＜entity-num＞|作用：表示要显示的SQA实例信息的实例号。范围：1-150。默认值：无。
缺省 : 
无 
使用说明 : 
可以用该命令查看SQA某一个测试实例的配置信息。使用该命令时，需要有相应实例的配置信息，如果没有则不显示。
范例 : 
在全局配置模式下，查看SQA某一个测试实例的配置情况：ZXROSNG(config)#show sqa-test 1test number:1test type:ICMPdestination IP:192.0.0.111repeat:10tos:0ttl:255size:36interval time:100send trap:disable
相关命令 : 
sqa-testsend-trap
## sqa-begin now 

sqa-begin now 
命令功能 : 
立即启动测试实例，当需要对某配置好检测类型的实例进行检测时，可以使用该命令立即启动检测 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
sqa-begin now 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
对某实例进行立即启动检测的操作时，需要在实例下先配置正确和完整的检测类型;如果没有配置检测类型，则不能执行该命令;如果实例正在检测中，则不能执行该命令
范例 : 
在SQA配置模式下，立即启动测试实例：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-icmp 192.168.1.100 repeat 10 source 1.1.1.1ZXROSNG(config-sqa-40)#sqa-begin now%Info 757: The SQA test is starting now,please wait a moment for test result......
相关命令 : 
sqa-stop 
## sqa-begin timerange 

sqa-begin timerange 
命令功能 : 
定时启动测试实例，当需要在某个时间启动实例时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
sqa-begin timerange 
  ＜timerange-name 
＞
no sqa-begin timerange 
命令参数解释 : 
参数|描述
---|---
＜timerange-name＞|作用：配置timerange的名字，定时启动测试。范围：1-31个字符。默认值：无。
缺省 : 
无 
使用说明 : 
需要先配好SQA的检测类型，才能定时开始执行当前测试实例；在定时开始执行测试实例之前，需要先配置timerange实例，才能在SQA模式下使用该timerange
范例 : 
在SQA配置模式下，定时启动测试实例：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-icmp 192.168.1.100 repeat 10 source 1.1.1.1ZXROSNG(config-sqa-40)#sqa-begin timerange zte
相关命令 : 
show sqa-testsqa-testtime-range
## sqa-stop 

sqa-stop 
命令功能 : 
该命令可以终止测试实例的执行，当需要停止正在检测中的实例时，可以使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
sqa-stop 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
当实例执行了开始检测的命令后，可以使用该命令停止实例的检测过程;如果实例没有执行过开始检测或者已经检测结束，则该命令不起作用
范例 : 
在SQA配置模式下，停止该测试实例的执行，该范例中的实例没有在检测中：ZXROSNG(config-sqa-1)#sqa-stop%Info 759: The SQA test is not running,no need to stop该范例中的实例正在检测中：ZXROSNG(config-sqa-1)#sqa-stop%Info 758: The SQA test has stopped now,you can not see the test result
相关命令 : 
sqa-testsqa-begin
## sqa-tcp-server 

sqa-tcp-server 
命令功能 : 
配置TCP的 server操作，该命令用来侦听TCP的某个特定地址和端口号 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sqa-tcp-server 
  {＜tcp-server-ipv4-address 
＞|＜tcp-server-ipv6-address 
＞ [vrf 
 ＜vrf-name 
＞]} ＜tcp-server-port 
＞
no sqa-tcp-server 
命令参数解释 : 
参数|描述
---|---
＜tcp-server-ipv4-address＞|功能：侦听的UDP的IPv4的地址取值范围：无默认值：无
＜tcp-server-ipv6-address＞|功能：侦听的UDP的IPv6的地址取值范围：无默认值：无
＜vrf-name＞|功能：VRF的名称取值范围：1-32个字符默认值：无
＜tcp-server-port＞|作用：TCP侦听的端口号。范围：1025-65535。默认值：无。
缺省 : 
无 
使用说明 : 
server端使用该命令配置TCP的侦听服务;只有配置好相应的IP地址和端口号，server端才能正确应答TCP的建链请求;如果没有配置正确的侦听地址和端口号，则TCP类型的检测不能成功
范例 : 
在全局配置模式下，配置TCP server：ZXROSNG(config)# sqa-tcp-server 192.168.1.98 10000查看TCP server的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-tcp-server 192.168.1.98 10000!!</SQA>
相关命令 : 
show sqa-server tcpshow running-config sqa
## sqa-test 

sqa-test 
命令功能 : 
该命令是模式跳转命令，用于配置SQA测试实例号以及进入SQA配置模式，当需要进行SQA检测时，需要配置该命令 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sqa-test 
  ＜entity-num 
＞
no sqa-test 
  ＜entity-num 
＞
				
命令参数解释 : 
参数|描述
---|---
＜entity-num＞|作用：表示要删除的SQA检测的测试实例号。范围：1-150。默认值：无。
缺省 : 
无 
使用说明 : 
配置SQA检测的测试实例号;要进行SQA检测必须先通过配置该命令进入SQA配置模式
范例 : 
配置测试实例1，进入SQA配置模式下：ZXROSNG(config)#sqa-test 1ZXROSNG(config-sqa-1)#查看SQA配置信息：ZXROSNG(config)#show running-config sqa ! <SQA>sqa-test 1!! </SQA>
相关命令 : 
show running-config sqashow sqa-test
## sqa-udp-server 

sqa-udp-server 
命令功能 : 
配置UDP的 server操作，该命令用来侦听UDP的某个特定地址和端口号 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sqa-udp-server 
  {＜udp-server-ipv4-address 
＞|＜udp-server-ipv6-address 
＞ [vrf 
 ＜vrf-name 
＞]} ＜udp-server-port 
＞
no sqa-udp-server 
命令参数解释 : 
参数|描述
---|---
＜udp-server-ipv4-address＞|功能：侦听的UDP的IPv4的地址取值范围：无默认值：无
＜udp-server-ipv6-address＞|功能：侦听的UDP的IPv6的地址取值范围：无默认值：无
＜vrf-name＞|功能：VRF的名称取值范围：1-32个字符默认值：无
＜udp-server-port＞|作用：UDP侦听的端口号。范围：1025-65535。默认值：无。
缺省 : 
无 
使用说明 : 
server端使用该命令配置UDP的侦听服务;只有配置好相应的IP地址和端口号，server端才能正确应答UDP的建链请求;如果没有配置正确的侦听地址和端口号，则UDP类型的检测不能成功
范例 : 
在全局配置模式下，配置UDP server：ZXROSNG(config)# sqa-udp-server 192.168.1.98 10000查看UDP server的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-udp-server 192.168.1.98 10000!!</SQA>
相关命令 : 
show sqa-server udpshow running-config sqa
## type-dns 

type-dns 
命令功能 : 
该命令用来配置DNS类型的检测，当需要进行DNS检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-dns 
  [vrf 
 ＜vrf-name 
＞] destination-url 
 ＜destination-url 
＞ dns-ip 
 {＜dns-ipv4-address 
＞|＜dns-ipv6-address 
＞} [repeat 
 ＜repeat-count 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口名称。范围：1-32个字符。默认值：无。
＜destination-url＞|作用：需要解析的域名。范围：1-128个字符。默认值：无。
＜dns-ipv4-address＞|功能：域名服务器的IPv4地址取值范围：无默认值：无
＜dns-ipv6-address＞|功能：域名服务器的IPv6地址取值范围：无默认值：无
＜repeat-count＞|作用：检测的测试次数。范围：1-10。默认值：1。
缺省 : 
repeat缺省值为1。 
使用说明 : 
配置DNS检测类型的测试实例；该检测可以进行域名的解析检测，可以统计解析时间等信息；检测前需要保证本端和DNS的server端可以ping通
范例 : 
在SQA模式下，配置DNS测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-dns destination-url abc.cn dns-ip 192.168.1.98 repeat 10查看DNS检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-dns destination-url abc.cn dns-ip 192.168.1.98 repeat 10!!</SQA>
相关命令 : 
show sqa-result dnsshow sqa-testshow running-config sqa
## type-ftp copy 

type-ftp copy 
命令功能 : 
该命令用来配置FTP类型的检测，当需要进行FTP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-ftp copy 
  {＜ftp-server-ipv4-address 
＞|＜ftp-server-ipv6-address 
＞} [vrf 
 ＜vrf-name 
＞] filename 
 ＜filename 
＞ root 
 ＜destination-root 
＞ [port 
 ＜destination-port 
＞]
命令参数解释 : 
参数|描述
---|---
＜ftp-server-ipv4-address＞|功能：FTP  server的IPv4地址取值范围：无默认值：无
＜ftp-server-ipv6-address＞|功能：FTP  server的IPv6地址取值范围：无默认值：无
＜vrf-name＞|作用：连接FTP server接口所需的vrf name，不支持管理口。范围：1-32个字符。默认值：无。
＜filename＞|作用：需要传输的文件名。范围：1-79个字符。默认值：无。
＜destination-root＞|作用：目的路径及文件名。范围：1-151个字符。默认值：无。
＜destination-port＞|作用：检测的目的端口号。范围：1-65535。默认值：21。
缺省 : 
无 
使用说明 : 
配置FTP检测类型的测试实例。该检测可以进行文件的下载检测，并且可以统计检测时间以及文件大小。检测前需要保证FTP检测的客户端和服务端可以ping通。检测的源文件必须保证在默认路径下存在，目的路径必需保证是有写入权限的路径，目的端口号如果不指定，则为默认FTP知名端口号21。只有该命令和type-ftp username命令都配置成功时才能进行FTP检测。
范例 : 
在SQA模式下，配置FTP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-ftp copy 192.168.1.100 filename ftp.txt root zte.txt查看FTP检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-ftp copy 192.168.1.100 filename ftp.txt root zte.txt!!</SQA>
相关命令 : 
show sqa-result ftpshow sqa-testshow running-config sqa
## type-ftp username 

type-ftp username 
命令功能 : 
该命令用来配置FTP类型的检测，当需要进行FTP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-ftp username 
  ＜ftp-server-username 
＞ password 
 {encrypted 
 ＜ftp-server-encrypted-password 
＞|＜ftp-server-password 
＞}
命令参数解释 : 
参数|描述
---|---
＜ftp-server-username＞|作用：配置FTP server的用户名。范围：1-31个字符。默认值：无。
＜ftp-server-encrypted-password＞|作用：配置FTP server的加密密码。范围：固定长度64个字符。默认值：无。
＜ftp-server-password＞|作用：配置FTP server的明文密码。范围：1-31个字符。默认值：无。
缺省 : 
无 
使用说明 : 
配置FTP检测类型的测试实例；该检测可以进行文件的下载检测，并且可以统计检测时间以及文件大小；检测前需要保证FTP检测的客户端和服务端可以ping通；检测时必须保证配置的用户名、密码和server端设置的用户名、密码一致；只有该命令和type-ftp copy命令都配置成功时才能进行FTP检测
范例 : 
在SQA模式下，配置FTP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-ftp username zte password zte查看FTP检测的配置信息：ZXROSNG(config-sqa-1)#show running-config sqa!<sqa>sqa-test 40  type-ftp username zte password encrypted 30fd73f50a27785f93622a84ddd81bd4908ac3f8b8592c89c1bffa6fec35a0d3$!</sqa>
相关命令 : 
show sqa-result ftpshow sqa-testshow running-config sqa
## type-http 

type-http 
命令功能 : 
该命令用来配置HTTP类型的检测，当需要进行HTTP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-http 
  [vrf 
 ＜vrf-name 
＞] {http-ip 
 ＜http-ip-address 
＞|http-url 
 ＜http-url 
＞ dns-ip 
 ＜dns-ip-address 
＞} [repeat 
 ＜repeat-count 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口。范围：1-32个字符。默认值：无。
＜http-ip-address＞|作用：要建立连接的网址。范围：无。默认值：无。
＜http-url＞|作用：要建立连接的域名。范围：1-128个字符。默认值：无。
＜dns-ip-address＞|作用：域名服务器的IP地址。范围：无。默认值：无。
＜repeat-count＞|作用：配置检测的次数。范围：1-10。默认值：1。
缺省 : 
repeat缺省值为1。 
使用说明 : 
配置HTTP检测类型的测试实例；该检测可以进行HTTP的检测，可以统计域名解析和TCP建链等时延信息；检测前需要保证本端和目的端可以ping通，并且目的端有可用的HTTP服务器
范例 : 
在SQA模式下，配置HTTP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)# type-http http-url zte.com.cn dns-ip 192.168.1.1 repeat 10查看HTTP检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-http http-url zte.com.cn dns-ip 192.168.1.1 repeat 10!!</SQA>
相关命令 : 
show sqa-result httpshow sqa-testshow running-config sqa
## type-icmp 

type-icmp 
命令功能 : 
该命令用来配置ICMP类型的检测，当需要进行ICMP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-icmp 
  [vrf 
 ＜vrf-name 
＞] {＜destination-ipv4-address 
＞ [{[source 
 ＜source-ipv4-address 
＞],[repeat 
 ＜repeat-count 
＞],[{[tos 
 ＜tos 
＞]|[dscp 
 ＜dscp 
＞]}],[ttl 
 ＜ttl 
＞],[size 
 ＜size 
＞],[interval 
 ＜interval 
＞]}]|＜destination-ipv6-address 
＞ [{[source 
 ＜source-ipv6-address 
＞],[repeat 
 ＜repeat-count 
＞],[{[traffic-class 
 ＜traffic_class 
＞]|[dscp 
 ＜dscp 
＞]}],[hoplimit 
 ＜hoplimit 
＞],[size 
 ＜size 
＞],[interval 
 ＜interval 
＞]}]}
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口。范围：1-32个字符。默认值：无。
＜destination-ipv4-address＞|功能：目的IPv4地址取值范围：无默认值：无
＜source-ipv4-address＞|功能：源IPv4地址取值范围：无默认值：无
＜repeat-count＞|作用：配置检测的重复次数。范围：1-65535。默认值：1。
＜tos＞|作用：配置TOS的值，该参数和DSCP只能选择其中之一。范围：0-255。默认值：0。
＜dscp＞|作用：配置DSCP的值，该参数和TOS只能选择其中之一。范围：0-63。默认值：0。
＜ttl＞|作用：配置TTL的值。范围：1-255。默认值：255。
＜size＞|作用：配置ICMP报文的大小。范围：36-8192。默认值：36。
＜interval＞|作用：相邻两次发包的间隔时间。范围：50-65535。默认值：100。
＜destination-ipv6-address＞|功能：目的IPv6地址取值范围：无默认值：无
＜source-ipv6-address＞|功能：源IPv6地址取值范围：无默认值：无
＜repeat-count＞|作用：配置检测的重复次数。范围：1-65535。默认值：1。
＜traffic_class＞|功能：TC值取值范围：0-255默认值：0
＜dscp＞|作用：配置DSCP的值，该参数和TOS只能选择其中之一。范围：0-63。默认值：0。
＜hoplimit＞|功能：TTL值取值范围：1-255默认值：255
＜size＞|作用：配置ICMP报文的大小。范围：36-8192。默认值：36。
＜interval＞|作用：相邻两次发包的间隔时间。范围：50-65535。默认值：100。
缺省 : 
repeat缺省值为1，tos缺省值为0，dscp缺省值为0，ttl缺省值为255，size缺省值为36 bytes，interval缺省值为100ms。 
使用说明 : 
配置ICMP检测类型的测试实例。该检测可以进行ICMP的双向检测，可以统计时延和丢包率等信息。检测前需要保证源端和目的端可以ping通。
范例 : 
在SQA模式下，配置ICMP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-icmp 192.168.1.100 repeat 10 source 1.1.1.1查看ICMP检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-icmp 192.168.1.100 repeat 10 source 1.1.1.1 !!</SQA>
相关命令 : 
show sqa-result icmp show sqa-testshow running-config sqa
## type-icmp-jitter 

type-icmp-jitter 
命令功能 : 
该命令用来配置ICMPjitter类型的检测，当需要进行ICMPjitter检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-icmp-jitter 
  [vrf 
 ＜vrf-name 
＞] ＜destination-ip-address 
＞ [{[source 
 ＜source-ip-address 
＞],[repeat 
 ＜repeat-count 
＞],[{[tos 
 ＜tos 
＞]|[dscp 
 ＜dscp 
＞]}],[ttl 
 ＜ttl 
＞],[size 
 ＜size 
＞],[interval 
 ＜interval 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口名称。范围：1-32个字符。默认值：无。
＜destination-ip-address＞|作用：ICMP检测的目的地址。范围：无。默认值：无。
＜source-ip-address＞|作用：ICMP检测的源地址。范围：无。默认值：无。
＜repeat-count＞|作用：配置检测的重复次数。范围：1-65535。默认值：1。
＜tos＞|作用：配置TOS的值，该参数和DSCP只能选择其中之一。范围：0-255。默认值：0。
＜dscp＞|作用：配置DSCP的值，该参数和TOS只能选择其中之一。范围：0-63。默认值：0。
＜ttl＞|作用：配置TTL的值。范围：1-255。默认值：255。
＜size＞|作用：配置ICMP报文的大小。范围：40-8192。默认值：40。
＜interval＞|作用：相邻两次发包的间隔时间。范围：50-65535。默认值：100。
缺省 : 
repeat缺省值为1，tos缺省值为0，dscp缺省值为0，ttl缺省值为255，size缺省值为40 bytes，interval缺省值为100ms。 
使用说明 : 
配置ICMPjitter检测类型的测试实例；该检测可以进行ICMP的单向检测，可以统计时延和抖动等信息；检测前需要保证源端和目的端可以ping通
范例 : 
在SQA模式下，配置ICMP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)#type-icmp-jitter 192.168.1.100 repeat 10 source 1.1.1.1查看ICMP检测的配置信息：ZXROSNG(config-sqa)#show running-config sqa!<sqa>sqa-test 40  type-icmp-jitter 192.168.1.100 source 1.1.1.1 repeat 10$!</sqa>
相关命令 : 
show sqa-result icmpjittershow sqa-testshow running-config sqa
## type-snmp 

type-snmp 
命令功能 : 
该命令用来配置SNMP类型的检测，当需要进行SNMP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-snmp 
  [vrf 
 ＜vrf-name 
＞] {＜destination-ipv4-address 
＞|＜destination-ipv6-address 
＞} [{[community 
 {encrypted 
 ＜encrypted-community 
＞|＜community 
＞}],[port 
 {＜default port-number 
＞|＜port-number 
＞}]}]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口。范围：1-32个字符。默认值：无。
＜destination-ipv4-address＞|功能：SNMP检测的目的IPv4地址取值范围：无默认值：无
＜destination-ipv6-address＞|功能：SNMP检测的目的IPv6地址取值范围：无默认值：无
＜encrypted-community＞|作用：加密的community字段。范围：固定长度64个字符。默认值：无。
＜community＞|作用：明文的community字段。范围：1-32个字符。默认值：无。
＜default port-number＞|作用：默认的目的端口号。默认值：161。
＜port-number＞|作用：配置检测的目的端口号。范围：1024-20000。
缺省 : 
无 
使用说明 : 
配置SNMP检测类型的测试实例；该检测可以进行SNMP的检测，可以统计时延信息；检测前需要保证本端和server端可以ping通，并且server端已配置侦听端口
范例 : 
在SQA模式下，配置SNMP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)# type-snmp 192.168.1.98查看SNMP检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-snmp 192.168.1.98!!</SQA>
相关命令 : 
show sqa-result snmpshow sqa-testshow running-config sqa
## type-tcp 

type-tcp 
命令功能 : 
该命令用来配置TCP类型的检测，当需要进行TCP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-tcp 
  [vrf 
 ＜vrf-name 
＞] {＜destination-ipv4-address 
＞|＜destination-ipv6-address 
＞} ＜destination-port 
＞ [{[repeat 
 ＜repeat-count 
＞],[interval 
 ＜interval 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口。范围：1-32个字符。默认值：无。
＜destination-ipv4-address＞|功能：目的IPv4地址取值范围：无默认值：无
＜destination-ipv6-address＞|功能：目的IPv6地址取值范围：无默认值：无
＜destination-port＞|作用：配置TCP检测的目的端口号。范围：1025-65535。默认值：无。
＜repeat-count＞|作用：配置检测的重复次数。范围：1-200。默认值：1。
＜interval＞|作用：配置相邻两次发包的间隔时间。范围：1000-4000。默认值：1000。
缺省 : 
repeat缺省值为1，interval缺省值为1000ms。 
使用说明 : 
配置TCP检测类型的测试实例。该检测可以进行TCP的建链检测，可以统计建链时延等信息。检测前需要保证源端和目的端可以ping通，并且目的端已配置侦听端口和IP地址。
范例 : 
在SQA模式下，配置TCP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)# type-tcp 192.168.1.98 10000 repeat 10查看TCP检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-tcp 192.168.1.98 10000 repeat 10!!</SQA>
相关命令 : 
show sqa-result tcpshow sqa-testshow running-config sqa
## type-udp 

type-udp 
命令功能 : 
该命令用来配置UDP类型的检测，当需要进行UDP检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-udp 
  [vrf 
 ＜vrf-name 
＞] {＜destination-ipv4-address 
＞ ＜destination-ipv4-port 
＞ [{[tos 
 ＜ipv4-tos 
＞],[size 
 ＜ipv4-size 
＞],[repeat 
 ＜ipv4-repeat-count 
＞],[interval 
 ＜ipv4-interval 
＞]}]|＜destination-ipv6-address 
＞ ＜destination-ipv6-port 
＞ [{[size 
 ＜ipv6-size 
＞],[repeat 
 ＜ipv6-repeat-count 
＞],[interval 
 ＜ipv6-interval 
＞]}]}
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口。范围：1-32个字符。默认值：无。
＜destination-ipv4-address＞|功能：目的IPv4地址配置。范围：无。默认值：无。
＜destination-ipv4-port＞|功能：IPv4检测的目的端口号配置。范围：1025-65535。默认值：无。
＜ipv4-tos＞|作用：配置对应IPv4地址的TOS的值。 范围：0-255。 默认值：0。
＜ipv4-size＞|作用：配置检测的对应IPv4地址的报文大小。 范围：50-1500。 默认值：50。
＜ipv4-repeat-count＞|作用：配置检测的对应IPv4地址的重复次数。 范围：1-1000。 默认值：1。
＜ipv4-interval＞|作用：配置对应IPv4地址的相邻两次发包的间隔时间。 范围：50-2000。 默认值：100。
＜destination-ipv6-address＞|功能：目的IPv6地址配置。范围：无。默认值：无。
＜destination-ipv6-port＞|功能：IPv6检测的目的端口号配置。范围：1025-65535。默认值：无。
＜ipv6-size＞|作用：配置检测的对应IPv6地址的报文大小。范围：50-1500。 默认值：50。
＜ipv6-repeat-count＞|作用：配置检测的对应IPv6地址的重复次数。 范围：1-1000。 默认值：1。
＜ipv6-interval＞|作用：配置对应IPv6地址的相邻两次发包的间隔时间。 范围：50-2000。 默认值：100。
缺省 : 
ipv4-repeat缺省值为1，ipv4-size缺省值为50 bytes，ipv4-interval缺省值100ms，ipv4-tos默认值为0，ipv6-repeat缺省值为1，ipv6-size缺省值为50 bytes，ipv6-interval缺省值100ms。 
使用说明 : 
配置UDP检测类型的测试实例。该检测可以进行UDP的双向检测，可以统计双向时延和丢包率等信息。检测前需要保证源端和目的端可以ping通，并且目的端已配置侦听端口和IP地址。
范例 : 
在SQA模式下，配置UDP测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)# type-udp 192.168.1.98 10000 repeat 10查看UDP检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-udp 192.168.1.98 10000 repeat 10!!</SQA>
相关命令 : 
show sqa-result udpshow sqa-testshow running-config sqa
## type-udp-jitter 

type-udp-jitter 
命令功能 : 
该命令用来配置UDPjitter类型的检测，当需要进行UDPjitter检测时使用该命令 
命令模式 : 
 SQA模式  
命令默认权限级别 : 
15 
命令格式 : 
type-udp-jitter 
  [vrf 
 ＜vrf-name 
＞] {＜destination-ipv4-address 
＞ ＜destination-ipv4-port 
＞ [{[tos 
 ＜ipv4-tos 
＞],[size 
 ＜ipv4-size 
＞],[repeat 
 ＜ipv4-repeat-count 
＞],[interval 
 ＜ipv4-interval 
＞]}]|＜destination-ipv6-address 
＞ ＜destination-ipv6-port 
＞ [{[size 
 ＜ipv6-size 
＞],[repeat 
 ＜ipv6-repeat-count 
＞],[interval 
 ＜ipv6-interval 
＞]}]}
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：VRF名称，不支持配置管理口。范围：1-32个字符。默认值：无。
＜destination-ipv4-address＞|功能：目的IPv4地址。范围：无。默认值：无。
＜destination-ipv4-port＞|功能：IPv4检测的目的端口号配置。范围：1025-65535。默认值：无。
＜ipv4-tos＞|作用：配置对应IPv4地址的TOS的值。 范围：0-255。 默认值：0。
＜ipv4-size＞|作用：配置检测的对应IPv4地址的报文大小。 范围：50-1500。 默认值：50。
＜ipv4-repeat-count＞|作用：配置检测的对应IPv4地址的重复次数。 范围：1-1000。 默认值：1。
＜ipv4-interval＞|作用：配置对应IPv4地址的相邻两次发包的间隔时间。 范围：50-2000。 默认值：100。
＜destination-ipv6-address＞|功能：目的IPv6地址。范围：无。默认值：无。
＜destination-ipv6-port＞|功能：IPv6检测类型的目的端口号配置。范围：1025-65535。默认值：无。
＜ipv6-size＞|作用：配置检测的对应IPv6地址的报文大小。 范围：50-1500。 默认值：50。
＜ipv6-repeat-count＞|作用：配置检测的对应IPv6地址的重复次数。 范围：1-1000。 默认值：1。
＜ipv6-interval＞|作用：配置对应IPv6地址的相邻两次发包的间隔时间。 范围：50-2000。 默认值：100。
缺省 : 
ipv4-repeat缺省值为1，ipv4-size的缺省值为50bytes，ipv4-interval的缺省值为100ms，ipv4-tos的缺省值为0，ipv6-repeat缺省值为1，ipv6-size的缺省值为50bytes，ipv6-interval的缺省值为100ms。 
使用说明 : 
配置UDPjitter检测类型的测试实例；该检测可以进行UDP的单向检测，可以统计单向时延和抖动等信息；检测前需要保证源端和目的端可以ping通，并且目的端已配置侦听端口和IP地址
范例 : 
在SQA模式下，配置UDP jitter测试：ZXROSNG(config)#sqa-test 40ZXROSNG(config-sqa-40)# type-udp-jitter 192.168.1.98 10000 repeat 10查看UDP jitter检测的配置信息：ZXROSNG(config)#show running-config sqa! <SQA>sqa-test 40type-udp-jitter 192.168.1.98 10000 repeat 10!!</SQA>
相关命令 : 
show sqa-result udpjittershow sqa-testshow running-config sqa
# SSH配置命令 
## clear ssh server public-key keyname 

clear ssh server public-key keyname 
命令功能 : 
指定公钥名，清除SSH服务器的认证公钥 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ssh server public-key keyname 
  ＜key-name 
＞
命令参数解释 : 
参数|描述
---|---
＜key-name＞|要清除的公钥名称，1-31个字符
缺省 : 
无 
使用说明 : 
1. 本命令属于操作命令；2. 清除前需要确保该公钥没有被任何用户所绑定，如果已有用户绑定该公钥，则清除失败。
范例 : 
1.  清除SSH服务器名称为my_pubkey的公钥：ZXROSNG#clear ssh server public-key keyname my_pubkey
相关命令 : 
ssh server usernameshow ssh server authentication-infoshow ssh server public-key briefssh server public-key keyname
## show ssh server authentication-info 

show ssh server authentication-info 
命令功能 : 
显示SSH服务器的认证配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ssh server authentication-info 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示SSH服务器的认证配置信息：ZXROSNG#show ssh server authentication-info SSH users:--------------------------------------------------------------------------------Username                    Authentication-Type     Key-Name--------------------------------------------------------------------------------zte                         any                     ztewho                         password-publickey      who_dss
相关命令 : 
ssh server public-key keynamessh server usernameshow ssh server public-key
## show ssh server host-key 

show ssh server host-key 
命令功能 : 
显示SSH主机公钥信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ssh server host-key 
  [type 
 {rsa 
|ecc 
 {nistp256 
|nistp384 
|nistp521 
|ed25519 
}}] 
命令参数解释 : 
参数|描述
---|---
rsa|指定查看RSA主机密钥信息
ecc|指定查看ECC主机密钥信息
nistp256|椭圆曲线名 nistp256
nistp384|椭圆曲线名 nistp384
nistp521|椭圆曲线名 nistp521
ed25519|椭圆曲线名 ed25519
缺省 : 
无 
使用说明 : 
字段描述：Key-Type  主机密钥类型。Modulus  密钥对模数，单位是比特。Key-Code  主机公钥信息。Curve-Name  ECC类型的椭圆曲线名。
范例 : 
1.查询所有主机密钥信息ZXROSNG#show ssh server host-key---------------------------------------------Key-Type: RSAModulus : 2048(bits)Key-Code:AAAAB3NzaC1yc2EAAAABAwAAAQEAvm7YeSjwJI/c3S9jof/6lMw9ATydCP5zbDgwVGBKGJ2ItYIWtqz4a031L1iTlR5nUqWG/Z6qP14/BdMBINVyUvFsOaTGEBWieF+7UEr1t3S49SdYTo5RGxVqAKjUQDo8sVQoL9CzA6O65eQCydQVCiloZVLkekpsYw8nHwtwyTPsnlp0Lbe52OAyR0KawiZ8ocYGunvhWfUr3VNEvmxU3LfI+63B+i6Nq8br9hDn5fNjqaBh5Ngo0yFNalxLcqRDgNnFYmDqv9aS9RpHAC/ATWTrRAYVsLgbMKpbymNfM32XTa710k8NcMEcOxKRbpCPmNeAeQY8zd+F/6NQKsMRIw==---------------------------------------------Key-Type  : ECCCurve-Name: nistp256Modulus   : 256(bits)Key-Code  :AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJ17S/AWM0yUu/xEsCpMk/U7kKeGnK37T6gh7fFGcfliHYi7hLopXh3zLHhgDT8CyKFvIjXNOx9Dsp0L8CfNht0=---------------------------------------------Key-Type  : ECCCurve-Name: nistp384Modulus   : 384(bits)Key-Code  :AAAAE2VjZHNhLXNoYTItbmlzdHAzODQAAAAIbmlzdHAzODQAAABhBFZX0c18mrDbn0LmY7P/yexI6EadtAlvlwTfiQWD8Sr406IpS2HQU+je+LRLnwk0kS/UnzoGdJHB2HLBAuHuSD/CboHucPpo1fFUaZdS5SCVBUXNY9WKBKclSnG/6JBinw==---------------------------------------------Key-Type  : ECCCurve-Name: nistp521Modulus   : 521(bits)Key-Code  :AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1MjEAAACFBABAKtdtw1MDhIWn2/QRVH7fFEyjGXfPnGfv0QSxsnPVsATmT6h5dbbUk/+ToggjJJ+MmgFFuqqlEqTadfXKeCNQhAEH4n+q4/lMqWin89EMOs0I+uEPsgwni0KzseXfMiz+P+Mc+OkWM3eyZeNsVJaT3oQ1cUvjYTosID3Xa8kWGdHAcA==---------------------------------------------Key-Type  : ECCCurve-Name: ed25519Modulus   : 256(bits)Key-Code  :AAAAC3NzaC1lZDI1NTE5AAAAIGFGpfUutWxPRlAQc+xAuSyNUewjYKBMQG4p5hIJjN3XZXROSNG#
2.仅查询RSA算法的密钥信息ZXROSNG#show ssh server host-key type rsa---------------------------------------------Key-Type: RSAModulus : 2048(bits)Key-Code:AAAAB3NzaC1yc2EAAAABAwAAAQEAvm7YeSjwJI/c3S9jof/6lMw9ATydCP5zbDgwVGBKGJ2ItYIWtqz4a031L1iTlR5nUqWG/Z6qP14/BdMBINVyUvFsOaTGEBWieF+7UEr1t3S49SdYTo5RGxVqAKjUQDo8sVQoL9CzA6O65eQCydQVCiloZVLkekpsYw8nHwtwyTPsnlp0Lbe52OAyR0KawiZ8ocYGunvhWfUr3VNEvmxU3LfI+63B+i6Nq8br9hDn5fNjqaBh5Ngo0yFNalxLcqRDgNnFYmDqv9aS9RpHAC/ATWTrRAYVsLgbMKpbymNfM32XTa710k8NcMEcOxKRbpCPmNeAeQY8zd+F/6NQKsMRIw==ZXROSNG#
3.仅查询椭圆曲线名为ed25519的密钥信息ZXROSNG#show ssh server host-key type ecc ed25519---------------------------------------------Key-Type  : ECCCurve-Name: ed25519Modulus   : 256(bits)Key-Code  :AAAAC3NzaC1lZDI1NTE5AAAAIGFGpfUutWxPRlAQc+xAuSyNUewjYKBMQG4p5hIJjN3XZXROSNG#
相关命令 : 
ssh server enablessh server generate-key
## show ssh server public-key brief 

show ssh server public-key brief 
命令功能 : 
显示SSH服务器的认证公钥配置简要信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ssh server public-key brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.  显示SSH服务器配置的所有认证公钥的简要信息：ZXROSNG(config)#show ssh server public-key briefZXROSNG#show ssh server public-key briefSSH Public-key:--------------------------------------------------------------Key-Name                           Key-Type    Modulus(bits)--------------------------------------------------------------0123456789012345678901234567890    RSA         20480123456789012345678901234567890... RSA         2048a                                  DSA         2048id_rsa.pub                         RSA         2048ZXROSNG#show ssh server public-key brief | detailSSH Public-key:--------------------------------------------------------------Key-Name                           Key-Type    Modulus(bits)--------------------------------------------------------------0123456789012345678901234567890    RSA         20480123456789012345678901234567890123 RSA         2048456789012345678901234567890123a                                  DSA         2048id_rsa.pub                         RSA         2048其中SSH服务器的公钥文件描述信息如下：SSH Public-key：SSH 公钥文件信息Key-Name：公钥文件名称Key-Type：公钥加密类型Modulus(bits)：公钥位数，单位bits
相关命令 : 
ssh server public-key keynameclear ssh server public-key keynamessh server usernameshow ssh server authentication-infoshow ssh server public-key keyname
## show ssh server public-key keyname 

show ssh server public-key keyname 
命令功能 : 
显示SSH服务器的认证公钥配置详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ssh server public-key keyname 
  ＜key-name 
＞
命令参数解释 : 
参数|描述
---|---
＜key-name＞|指定显示的公钥名称，1-31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.  显示认证公钥名为Router1的详细信息：ZXROSNG#show ssh server public-key keyname my-key---------------------------------------------Key-Name:  my-keyKey-Type:  RSAModulus:   2048(bits)---------------------------------------------Key-Code:AAAAB3NzaC1yc2EAAAADAQABAAABAQDSwavg6b+bGTDC3ScHUuxE0joj6EhAchcbrbxiaMXqMr1WTD6WMw/e2EFOiZzL1KOBFmEyrFDg+TIJp3Zh/UlFwyP/bjyHpV4CHkBHq5WYO4H5hxXG2YHs19a5tq3/jgNaH94c7+QH0jqR6zU9kbUq5lv/12UDK/x6+TLzPb4fS67jYhfYLCXjs8WSt4M+DpKU5/fGlB5z5liCiZ+CNr/tQ03grq+hvuod9vgYb722sS/0VnASbW/m4/RPQcpGLt2rdOavYtC8SoiDFNIpg/+Or0mP3O0pI74mV7TXwc+ize7vzoigdHO8388K1CQOq5wttXIzHkEV0eUa6CKgjRq5其中SSH服务器的公钥文件详细信息描述如下：Key-Name：公钥文件名称Key-Type：公钥加密类型Modulus：公钥位数，单位bitsKey-Code：公钥密码
相关命令 : 
ssh server public-key keynameclear ssh server public-key keynamessh server usernameshow ssh server authentication-infoshow ssh server public-key brief
## show ssh 

show ssh 
命令功能 : 
该命令工作于除用户模式外的其它所有模式，用于显示SSH服务的配置信息，包括SSH服务状态、侦听端口号、配置的IPv4和IPv6 ACL规则名。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ssh 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于显示SSH服务的配置信息，当没有配置SSH服务时，显示系统的默认信息。 
范例 : 
ZXROSNG#show ssh=================================================================SSH configuration=================================================================SSH enable-flag configuration    :  enableSSH version                      :  1SSH listen port                  :  22SSH DSCP value                   :  48SSH IPv4 ACL name                :SSH IPv6 ACL name                :SSH rekey interval               :  2(hours)-----------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## ssh server access-class ipv4 

ssh server access-class ipv4 
命令功能 : 
该命令工作于全局配置模式下，用于设置SSH服务针对IPv4接入的ACL（Access Control List，访问控制列表）规则名称。该命令设置成功后，对于客户端通过IPv4地址向本设备新发起的SSH连接，如果设置的ACL配置了拒绝该地址接入的规则，则不允许建立连接；对于当前已存在的SSH服务端连接，如果设置的ACL配置了拒绝连接源地址的规则，则连接会主动断开。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server access-class ipv4 
  ＜ipv4-acl-name 
＞
no ssh server access-class ipv4 
命令参数解释 : 
参数|描述
---|---
＜ipv4-acl-name＞|ACL名称，长度为1-31个字符
缺省 : 
缺省情况下SSH不使用ACL列表。 
使用说明 : 
    缺省情况下，设备上的SSH服务不使用IPv4 ACL，所有IPv4接入均允许建立连接。    使用该命令配置SSH服务的IPv4 ACL时，需要先配置对应的IPv4 ACL规则，本命令的配置数据才会生效。IPv4 ACL配置方法参见配置命令ipv4-access-list。
范例 : 
ZXROSNG(config)# ssh server access-class ipv4 sshaclZXROSNG(config)# no ssh server access-class ipv4
相关命令 : 
ssh server access-class ipv6 
## ssh server access-class ipv6 

ssh server access-class ipv6 
命令功能 : 
该命令工作于全局配置模式下，用于设置SSH服务针对IPv6接入的ACL（Access Control List：访问控制列表）规则名称。该命令设置成功后，对于客户端通过IPv4地址向本设备新发起的SSH连接，如果设置的ACL配置了拒绝该地址接入的规则，则不允许建立连接；对于当前已存在的SSH服务端连接，如果设置的ACL配置了拒绝连接源地址的规则，则连接会主动断开。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server access-class ipv6 
  ＜ipv6-acl-name 
＞
no ssh server access-class ipv6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-acl-name＞|ACL名称，长度为1-31个字符
缺省 : 
缺省情况下SSH不使用ACL列表。 
使用说明 : 
    缺省情况下，设备上的SSH服务不使用IPv6 ACL，所有IPv6接入均允许建立连接。    使用该命令配置SSH服务的IPv6 ACL时，需要先配置对应的IPv6 ACL规则，本命令的配置数据才会生效。IPv6 ACL配置方法参见配置命令ipv6-access-list。
范例 : 
配置SSH服务IPv6 ACL为ssh_acl，则输入以下命令：ZXROSNG(config)# ssh server access-class ipv6 ssh_aclZXROSNG(config)#取消SSH服务的IPv6 ACL，则输入以下命令：ZXROSNG(config)# no ssh server access-class ipv6ZXROSNG(config)#
相关命令 : 
ssh server access-class ipv4  
## ssh server diffie-hellman 

ssh server diffie-hellman 
命令功能 : 
关闭SSH服务器diffie-hellman弱算法。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server diffie-hellman 
  {group1-sha1 
|group-exchange-sha1 
|group-exchange-sha256 
} disable 
no ssh server diffie-hellman 
  {group1-sha1 
|group-exchange-sha1 
|group-exchange-sha256 
} disable 
命令参数解释 : 
参数|描述
---|---
group1-sha1|diffie-hellman-group1-sha1算法
group-exchange-sha1|diffie-hellman-group-exchange-sha1算法
group-exchange-sha256|diffie-hellman-group-exchange-sha256算法
disable|关闭弱算法
缺省 : 
缺省情况下，SSH服务器上的DH算法都处于使能状态。 
使用说明 : 
SSH服务器关闭diffie-hellman-group1-sha1算法后，禁止客户端使用此算法协商密钥。配置SSH服务器关闭diffie-hellman-group-exchange-sha1算法：ZXROSNG(config)#ssh server diffie-hellman group-exchange-sha1 disable
范例 : 
配置SSH服务器关闭diffie-hellman-group1-sha1算法：ZXROSNG(config)#ssh server diffie-hellman group1-sha1 disable
相关命令 : 
无 
## ssh server disable 

ssh server disable 
命令功能 : 
该命令工作于全局配置模式下，用于停用SSH服务。该命令执行成功后，SSH服务停用，安全远程访问（STelnet）与安全文件传输（SFTP）不再可用，并且当前已有的SSH服务端连接都会主动断开。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server disable 
 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下SSH服务端功能是关闭的。 
使用说明 : 
  缺省情况下，设备上的SSH服务是关闭的。  SSH服务开启时，如果要修改服务使用的端口号时，需要使用本命令先停用SSH服务，再通过ssh server enable命令指定需要的端口号。
范例 : 
ZXROSNG(config)#ssh server disable Process will disable SSH Server. Are you sure? [yes/no]:yZXROSNG(config)#
相关命令 : 
ssh server enable [listen { <22> | <49152-65535> } ]show sshshow running-config ssh
## ssh server dscp 

ssh server dscp 
命令功能 : 
为IPv4/IPv6 SSH server指定控制面报文的DSCP。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server dscp 
  ＜dscp-value 
＞
no ssh server dscp 
命令参数解释 : 
参数|描述
---|---
＜dscp-value＞|DSCP值，范围0-63
缺省 : 
缺省情况下，SSH server端发出的SSH报文无DSCP 
使用说明 : 
1.若需要SSH server端发送报文时指定优先级，可以通过本命令进行指定；2.本命令对IPv4/IPv6 SSH server同时生效；3.命令配置后，仅对下一次建立的连接生效，已建立的连接不再发生改变；
范例 : 
配置SSH server发送报文的DSCP值ZXROSNG(config)#ssh server dscp 63
相关命令 : 
无 
## ssh server enable 

ssh server enable 
命令功能 : 
该命令工作于全局配置模式下，用于开启SSH（Secure Shell，安全外壳）服务。SSH是一种在不安全的网络环境中，通过加密和认证机制，实现安全的远程访问以及文件传输等业务的网络安全协议。用户通过一个不能保证安全的网络环境远程登录到本设备时，SSH可以利用加密和强大的认证功能提供安全保障，保护设备不受诸如IP地址欺诈、明文密码截取等攻击。该命令配置成功后，允许用户通过客户端STelnet（Security Telecommunication Network Protocol，安全远程访问）设备进行管理，或者与设备之间通过SFTP（Secure File Transfer Protocol，安全文件传输协议）进行安全文件传输。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server enable 
  [listen 
 {＜22 
＞|＜49152-65535 
＞}]
命令参数解释 : 
参数|描述
---|---
＜22＞|Server端侦听端口可配置为默认端口号22
＜49152-65535＞|Server端侦听端口可配置范围为49152-65535
缺省 : 
缺省情况下，SSH服务端功能是关闭的。 
使用说明 : 
    缺省情况下，设备上的SSH服务是关闭的，需要通过本命令来开启。    使用该命令开启SSH服务时，可以通过参数指定侦听的端口号。如果不指定端口号，则使用SSH标准协议默认端口号22；指定其它端口号时，可配置范围为49152~65535。    SSH服务开启时，如果要修改服务使用的端口号时，需要通过命令ssh server disable停用SSH服务，再通过本命令指定需要的端口号。
范例 : 
ZXROSNG(config)#ssh server enableZXROSNG(config)#ZXROSNG(config)#ssh server enable listen 49155ZXROSNG(config)#
相关命令 : 
ssh server disableshow sshshow running-config ssh
## ssh server encryption 

ssh server encryption 
命令功能 : 
关闭SSH服务器加密弱算法。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server encryption 
  {aes256-cbc 
|aes192-cbc 
|aes128-cbc 
|blowfish-cbc 
|3des-cbc 
|none 
} disable 
no ssh server encryption 
  {aes256-cbc 
|aes192-cbc 
|aes128-cbc 
|blowfish-cbc 
|3des-cbc 
|none 
} disable 
命令参数解释 : 
参数|描述
---|---
aes256-cbc|AES256-CBC
aes192-cbc|AES192-CBC
aes128-cbc|AES128-CBC
blowfish-cbc|BLOWFISH-CBC
3des-cbc|3DES-CBC
none|数据不加密
disable|关闭弱算法
缺省 : 
缺省情况下，SSH服务器上的加密算法都处于使能状态。 
使用说明 : 
SSH服务器关闭加密none算法后，禁止客户端进行明文传输。 
范例 : 
配置SSH服务器关闭使用不加密：ZXROSNG(config)#ssh server encryption none disableSSH服务器关闭AES256-CBC加密算法：ZXROSNG(config)#ssh server encryption aes256-cbc disable
相关命令 : 
无 
## ssh server generate-key 

ssh server generate-key 
命令功能 : 
用来为SSH服务器生成或更新RSA（Revest-Shamir-Adleman Algorithm）主机密钥和ECC（Elliptic Curve Cryptography）主机密钥。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server generate-key 
  [{modulus 
 {1024 
|2048 
}|[type 
 {rsa 
 [modulus 
 {1024 
|2048 
}]|ecc 
 [{nistp256 
|nistp384 
|nistp521 
|ed25519 
}]}]}]
命令参数解释 : 
参数|描述
---|---
1024|1024位
2048|2048位
rsa|RSA主机密钥。
1024|1024位
2048|2048位
ecc|ECC主机密钥。
nistp256|椭圆曲线名 nistp256
nistp384|椭圆曲线名 nistp384
nistp521|椭圆曲线名 nistp521
ed25519|椭圆曲线名 ed25519
缺省 : 
不指定modulus或type，ssh server generate-key命令生成RSA密钥对，模数为1024。不指定curve-name，ssh server generate-key type ecc命令生成nistp521密钥对，模数为521。
使用说明 : 
本命令用来生成或更新RSA、ECC密钥，为SSH服务器提供安全保证。RSA主机密钥对的模数可为1024，2048，单位是比特。ECC主机密钥对的模数可为256，384，521，单位是比特。与RSA算法相比，ECC算法可以大大减少密钥的长度，加密速度也相对较快，并具有更高的安全性。密钥对的模数越大可以提供越高的安全性，但是生成和使用这样的密钥对将花费更多的时间。注意事项：1. 本命令属于操作命令，因此不会被保存在配置文件中。2. 计算生成密钥需要一段时间。
范例 : 
生成服务端本地密钥对：ZXROSNG(config)#ssh server generate-key modulus 2048...[OK]ZXROSNG(config)#生成nistp384密钥对：ZXROSNG(config)#ssh server generate-key type ecc nistp384...[OK]ZXROSNG(config)#
相关命令 : 
ssh server enable   ssh server rekey-intervalshow ssh server host-key
## ssh server hmac 

ssh server hmac 
命令功能 : 
关闭SSH服务器HMAC(Hash Message Authentication Code)弱算法。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server hmac 
  {none 
|md5 
} disable 
no ssh server hmac 
  {none 
|md5 
} disable 
命令参数解释 : 
参数|描述
---|---
none|不使用HMAC算法进行完整性校验
md5|hmac-md5算法
disable|关闭弱算法
缺省 : 
缺省情况下，SSH服务器上的HMAC算法都处于使能状态。 
使用说明 : 
SSH服务器关闭HMAC某个弱算法后，禁止客户端使用该弱算法进行数据完整性校验。 
范例 : 
配置SSH服务器关闭MD5算法：ZXROSNG(config)#ssh server hmac md5 disable
相关命令 : 
无 
## ssh server host-key 

ssh server host-key 
命令功能 : 
关闭SSH服务器 主机公钥弱算法。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server host-key 
 dsa 
 disable 
no ssh server host-key 
 dsa 
 disable 
命令参数解释 : 
参数|描述
---|---
dsa|DSA(digital signature algorithm)算法
disable|关闭弱算法
缺省 : 
缺省情况下，SSH服务器上的主机公钥算法都处于使能状态。 
使用说明 : 
SSH服务器关闭DSA算法后，禁止SSH客户端使用此算法协商密钥。配置SSH服务器关闭DSA算法：ZXROSNG(config)#ssh server host-key dsa disable
范例 : 
配置SSH服务器关闭DSA算法：ZXROSNG(config)#ssh server host-key dsa disable
相关命令 : 
无 
## ssh server public-key keyname 

ssh server public-key keyname 
命令功能 : 
SSH服务端导入公钥文件并命名 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server public-key keyname 
  ＜key-name 
＞ import 
 keyfile 
 ＜key-filename 
＞
命令参数解释 : 
参数|描述
---|---
＜key-name＞|公钥名称，1-31个字符
＜key-filename＞|公钥文件名或文件路径及文件名，纯文件名为1-79个字符，全路径为1-159个。
缺省 : 
缺省服务端没有认证公钥。 
使用说明 : 
1. 公钥名不能重复（包括文件导入或直接配置两种方式）；2. 输入的公钥文件格式可以是SSH-1、SSH-2、OpenSSH的，系统自动识别；3. 该命令属于操作命令；4. 导入公钥的模数范围为512-2048。
范例 : 
SSH服务端导入公钥文件key.pub并命名为Router1：ZXROSNG(config)#ssh server public-key keyname Router1 import keyfile /datadisk0/key.pubZXROSNG(config)#
相关命令 : 
show ssh server public-keyclear ssh server public-key keynamessh server username
## ssh server rekey-interval 

ssh server rekey-interval 
命令功能 : 
配置SSH服务端更新服务密钥的周期时间 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server rekey-interval 
  ＜rekey-interval 
＞
no ssh server rekey-interval 
命令参数解释 : 
参数|描述
---|---
＜rekey-interval＞|更新周期，取值范围0-720，单位为小时，0表示不更新
缺省 : 
默认更新周期为1小时，可通过性能参数SSH_SERVER_REKEY_INTERVAL调整 
使用说明 : 
1.目前仅支持SSHv1版本时，服务端RSA的服务密钥的周期更新。2.no 命令恢复成默认值。
范例 : 
配置SSH服务端的密钥更新周期为2小时：ZXROSNG(config)#ssh server rekey-interval 2
相关命令 : 
ssh server enablessh server version
## ssh server username 

ssh server username 
命令功能 : 
为SSH用户指定认证方式并绑定公钥名 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server username 
  ＜username 
＞ authentication-type 
 {password 
|keyboard-interactive 
|{publickey 
|password-publickey 
|any 
} apply 
 keyname 
 ＜key-name 
＞}
no ssh server username 
  ＜username 
＞
				
命令参数解释 : 
参数|描述
---|---
＜username＞|用户名，1-65个字符，与ADMMGR配置用户对应
password|指定用户的认证方式为password密码认证
keyboard-interactive|指定用户的认证方式为keyboard-interactive认证(键盘交互认证)
publickey|指定用户的认证方式为publickey公钥认证
password-publickey|指定用户的认证方式为password和publickey认证同时满足。SSHv1的用户只要通过其中一种认证即可登录；SSHv2的用户必须两种认证都通过才能登录
any|指定用户的认证方式可以是password，也可以是publickey或keyboard-interactive
＜key-name＞|用户绑定公钥名称，1-31个字符。公钥需要通过ssh server public-key keyname import keyfile命令导入
缺省 : 
如果此处没有配置，则缺省为password密码认证方式 
使用说明 : 
1.配置前先确保用户管理模式中已添加该用户，否则用户认证失败；2.用户的认证方式默认为password认证，即如果这里没有配置SSH用户认证方式，则默认认为用户需要进行password认证；3.配置的公钥，不区分Stelnet、SFTP等服务类型，但对于SFTP，仅适用于SSHv2；4.配置的认证方式和用户公钥，对于已经登录的SSH用户不会生效，只在用户下次登录时才生效。5.指定用户的认证方式为keyboard-interactive时,我们发给客户端的交互信息是password，需要客户端回应密码信息来登录
范例 : 
SSH服务端导入公钥文件key.pub并命名为Router1，然后设置用户zteuser的认证方式为公钥认证并指定公钥Router1：ZXROSNG(config)#ssh server public-key keyname Router1 import keyfile /datadisk0/key.pubZXROSNG(config)#ssh server username zteuser authentication-type publickey apply keyname Router1
相关命令 : 
show ssh server authentication-infossh server public-key keynameclear ssh server public-key keyname
## ssh server version 

ssh server version 
命令功能 : 
设置SSH服务器协议版本号。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server version 
  ＜version 
＞
no ssh server version 
命令参数解释 : 
参数|描述
---|---
＜version＞|SSH服务器协议版本号，范围1-2，缺省为2
缺省 : 
SSH服务器协议版本号，缺省为2，即2.0版本 
使用说明 : 
无 
范例 : 
设置SSH服务器协议版本号为v1：ZXROSNG(config)# ssh server version 1设置SSH服务器协议版本号为v2：ZXROSNG(config)# ssh server version 2
相关命令 : 
show ssh 
## ssh server vrf 

ssh server vrf 
命令功能 : 
配置SSH服务端支持的的VRF名称。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ssh server vrf 
  ＜vrf-name 
＞
no ssh server vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
缺省 : 
默认没有配置SSH服务端支持的VRF。 
使用说明 : 
执行该配置后，将限定SSH仅仅在该VRF内允许建立会话，网管通过其他VRF将无法与本端建立SSH会话。默认情况下没有配置服务端支持的VRF，则允许网管通过公网或任意VRF与本端建立SSH会话 
范例 : 
配置SSH支持服务端支持管理口VRF：ZXROSNG(config)#ssh server vrf mng
相关命令 : 
无 
# Telnet配置命令 
## clear line vty 

clear line vty 
命令功能 : 
clear line vty命令用来断开与指定Telnet或SSH用户界面的连接（强制指定的VTY终端断链） 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear line vty 
  ＜vty-number 
＞
命令参数解释 : 
参数|描述
---|---
＜vty-number＞|虚拟终端（vty）编号，取值范围：0-31，默认值：无。
缺省 : 
无 
使用说明 : 
使用who命令或者show users命令可以查看此操作是否生效。该命令不能踢console终端下线。
范例 : 
查看当前在线用户信息ZXROSNG#who   Line      User      Host(s)          Idle     Login       Location   66 vty 0  zte       idle             00:00:18 2018-10-02  192.168.100.1                                                 19:39:37 * 67 vty 1  zte       idle             00:00:00 2018-10-02  192.168.100.1                                                 19:39:40ZXROSNG#
踢VTY0终端下线ZXROSNG#clear line vty 0ZXROSNG#
相关命令 : 
whoshow users
## force-print line-feed disable 

force-print line-feed disable 
命令功能 : 
关闭超出屏宽强制打印换行符功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
force-print line-feed disable 
 
命令参数解释 : 
					无
				 
缺省 : 
默认情况，超出屏宽强制打印换行符功能是开启的。 
使用说明 : 
不同客户端对于超出屏宽屏高时的处理方式不同，关闭此功能可能导致某些客户端上回显异常。 
范例 : 
关闭超出屏宽强制打印换行符功能：ZXROSNG(config)# force-print line-feed disable
相关命令 : 
force-print line-feed enable 
## force-print line-feed enable 

force-print line-feed enable 
命令功能 : 
开启超出屏宽强制打印换行符功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
force-print line-feed enable 
 
命令参数解释 : 
					无
				 
缺省 : 
默认情况，超出屏宽强制打印换行符功能是开启的。 
使用说明 : 
无。 
范例 : 
开启超出屏宽强制打印换行符功能：ZXROSNG(config)# force-print line-feed enable
相关命令 : 
force-print line-feed disable 
## line console absolute-timeout 

line console absolute-timeout 
命令功能 : 
该命令工作于全局配置模式，用于配置串口最大在线超时时间，使用该命令配置成功后，串口在达到配置的最大在线超时时间后会自动断链。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line console absolute-timeout 
  ＜online-time 
＞
no line console absolute-timeout 
命令参数解释 : 
参数|描述
---|---
＜online-time＞|串口的在线超时时间，单位:分钟，取值范围：0-10000。
缺省 : 
缺省情况下，串口终端在线超时时间是$#34668552#$。 
使用说明 : 
1.默认情况下，串口的最大在线超时时间为1天（1440分钟）。2.配置为0时，串口的在线时间不受限制。
范例 : 
配置串口的在线超时时间为500分钟：ZXROSNG(config)#line console absolute-timeout 500ZXROSNG(config)#
相关命令 : 
show terminalshow running-config telnet
## line console idle-timeout 

line console idle-timeout 
命令功能 : 
用来设置Console终端用户界面断开连接的超时时间。如果用户在一段时间内没有输入命令，系统将断开连接。no line console idle-timeout用来恢复用户界面断开连接的空闲超时时间的缺省值。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line console idle-timeout 
  ＜idle-time 
＞
no line console idle-timeout 
命令参数解释 : 
参数|描述
---|---
＜idle-time＞|指定用户界面断开连接的空闲超时时间。整数形式，取值范围是0-1000，单位是分钟。
缺省 : 
缺省情况下，串口终端空闲超时时间是$#34668553#$。 
使用说明 : 
line console idle-timeout 0将关闭用户界面的空闲超时断连功能。 
范例 : 
设置Console终端用户界面空闲超时时间是150分钟：ZXROSNG(config)#line console idle-timeout 150ZXROSNG(config)#
相关命令 : 
show terminalline console absolute-timeout
## line telnet absolute-timeout 

line telnet absolute-timeout 
命令功能 : 
line telnet absolute-timeout命令用来设置Telnet、SSH终端最大在线超时时间，使用该命令，配置成功后，Telnet、SSH终端在达到配置的最大在线超时时间后会自动断链。no line telnet absolute-timeout命令用来恢复默认配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet absolute-timeout 
  ＜online-time 
＞
no line telnet absolute-timeout 
命令参数解释 : 
参数|描述
---|---
＜online-time＞|Telnet、SSH终端的在线超时时间，单位:分钟，取值范围：0-10000。
缺省 : 
缺省情况下，Telnet和SSH终端在线超时时间是$#34668554#$。 
使用说明 : 
配置为0时，Telnet、SSH终端的在线时间不受限制。
范例 : 
配置Telnet、SSH连接的在线超时时间为500分钟：ZXROSNG(config)#line telnet absolute-timeout 500ZXROSNG(config)#
相关命令 : 
show terminal 
## line telnet access-class ipv4 

line telnet access-class ipv4 
命令功能 : 
line telnet access-class ipv4命令用来设置可以访问Telnet服务器的访问控制列表（Access Control List，ACL）。no line telnet access-class ipv4命令用来取消可以访问Telnet服务器的访问控制列表。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet access-class ipv4 
  ＜acl-name 
＞
no line telnet access-class ipv4 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定访问控制列表名称。字符串形式，取值范围1～31个字符。
缺省 : 
缺省情况下，Telnet不绑定任何访问控制列表名。 
使用说明 : 
应用场景：设备作为Telnet服务器时，通过在设备上配置访问控制列表，来控制运行哪些Telnet客户端以Telnet方式登录到本设备。配置影响：1)可使用访问控制列表对Telnet的源地址、源端口、目的地址、目的端口作限制。2)Telnet支持ACL规则动态响应，即Telnet连接在线时，如果绑定的IPv4类型ACL规则发生变更，Telnet连接会立即响应。
范例 : 
配置ACL实例：允许从源IP 10.40.142.101接入设备，拒绝从源IP 192.168.100.1接入设备ZXROSNG(config)#ipv4-access-list telnet_host_ip                                  ZXROSNG(config-ipv4-acl)#rule 1 deny tcp 192.168.100.1 0.0.0.0 192.168.100.250 0.0.0.0ZXROSNG(config-ipv4-acl)#rule 1 permit tcp 10.40.142.101 0.0.0.0 192.168.100.250 0.0.0.0ZXROSNG(config-ipv4-acl)#Telnet关联ACL实例：ZXROSNG(config)#line telnet access-class ipv4 telnet_host_ip
相关命令 : 
show terminal 
## line telnet access-class ipv6 

line telnet access-class ipv6 
命令功能 : 
line telnet access-class ipv6命令用来设置可以访问Telnet服务器的访问控制列表（Access Control List，ACL）。no line telnet access-class ipv6命令用来取消可以访问Telnet服务器的访问控制列表。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet access-class ipv6 
  ＜acl-name 
＞
no line telnet access-class ipv6 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定访问控制列表名称。字符串形式，取值范围1～31个字符。
缺省 : 
默认情况下,Telnet不绑定任何访问控制列表。 
使用说明 : 
应用场景：设备作为Telnet服务器时，通过在设备上配置访问控制列表，来控制运行哪些Telnet客户端以Telnet方式登录到本设备。配置影响：1）可使用访问控制列表对Telnet的源地址、源端口、目的地址、目的端口作限制。2）Telnet连接支持ACL规则动态响应，即Telnet连接在线时，如果绑定的IPv6类型ACL规则发生变更，Telnet连接会立即响应。
范例 : 
配置Telnet连接绑定的IPv6类型的ACL规则名称为telnet_v6：ZXROSNG(config)#line telnet access-class ipv6 telnet_v6ZXROSNG(config)#
相关命令 : 
show terminal 
## line telnet dscp 

line telnet dscp 
命令功能 : 
line telnet dscp命令用来设置IPv4/IPv6 Telnet报文的DSCP值。no line telnet dscp命令用来恢复IPv4/IPv6 Telnet报文的缺省DSCP值。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet dscp 
  ＜dscp-value 
＞
no line telnet dscp 
命令参数解释 : 
参数|描述
---|---
＜dscp-value＞|指定报文的DSCP值。整数形式，取值范围是0-63。
缺省 : 
缺省情况下，Telnet服务端端发出的报文的TOS/Traffic Class值为0xC0。 
使用说明 : 
1.若需要Telnet服务端发送报文时指定优先级，可以通过本命令进行指定；2.本命令对IPv4/IPv6 Telnet server同时生效；3.命令配置后，仅对下一次建立的连接生效，已建立的连接不再发生改变；
范例 : 
配置Telnet server发送报文的DSCP值ZXROSNG(config)#line telnet dscp 63
相关命令 : 
telnettelnet6show terminal
## line telnet idle-timeout 

line telnet idle-timeout 
命令功能 : 
line telnet idle-timeout命令用来设置Telnet、SSH终端用户界面断开连接的空闲超时时间。如果用户在一段时间内没有输入命令，系统将断开连接。no line telnet idle-timeout命令用来恢复用户界面断开连接的空闲超时时间的缺省值。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet idle-timeout 
  ＜idle-time 
＞
no line telnet idle-timeout 
命令参数解释 : 
参数|描述
---|---
＜idle-time＞|指定用户界面断开连接的空闲超时时间。整数形式，取值范围是0-1000，单位是分钟。
缺省 : 
缺省情况下，Telnet和SSH终端空闲超时时间是$#34668555#$。 
使用说明 : 
line telnet idle-timeout 0将关闭用户界面的空闲超时断连功能。 
范例 : 
设置Telnet、SSH终端用户界面空闲超时时间是150分钟ZXROSNG(config)#line telnet idle-timeout 150ZXROSNG(config)#
相关命令 : 
show terminalline telnet absolute-timeout
## line telnet max-link 

line telnet max-link 
命令功能 : 
line telnet max-link命令用来设置Telnet和SSH总的最大连接数。no line telnet max-link命令用来恢复默认配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet max-link 
  ＜number 
＞
no line telnet max-link 
命令参数解释 : 
参数|描述
---|---
＜number＞|最大终端连接数，可配置范围：1-$#34668551#$，最大值支持性能参数定制，34668551为性能参数id
缺省 : 
Telnet和SSH总的最大连数支持性能参数定制，若无性能参数，则默认值为15。 
使用说明 : 
当配置的最大连接数小于当前在线的连接数时，不允许配置，提示用户。show terminal命令可以查看当前设置的最大连接数。
范例 : 
设置Telnet和SSH总的最大终端连接数为12：ZXROSNG(config)#line telnet max-link 12ZXROSNG(config)#
查看当前在线的用户数ZXROSNG(config)#show users               Line      User      Host(s)          Idle     Login       Location * 66 vty 0  zte       idle             00:00:00 2018-01-24  192.168.100.1                                                 01:44:36       67 vty 1  zte       idle             00:08:50 2018-01-24  192.168.100.1                                                 01:45:27    ZXROSNG(config)#
设置的最大连接数小于在线用户数时，报错ZXROSNG(config)#line telnet max-link 1%Error 5033: The input para can not be less than current TELNET links numberZXROSNG(config)#
相关命令 : 
show terminal 
## line telnet max-source-connection 

line telnet max-source-connection 
命令功能 : 
line telnet max-source-connection 命令用来配置Telnet和STelnet单个源IP允许的最大并发连接数。no line telnet max-source-connection 命令用来取消配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet max-source-connection 
  ＜number 
＞
no line telnet max-source-connection 
命令参数解释 : 
参数|描述
---|---
＜number＞|单个源地址IP允许的最大并发连接数，范围1~$#34668551#$，最大源连接数支持通过性能参数定制，34668551为性能参数id
缺省 : 
无 
使用说明 : 
1.默认情况下没有配置该参数，表示不对单个源IP发起的连接数进行限制，使用no命令取消配置。2.当单个源IP发起的连接数超过配置值，则会拒绝登陆；3.单个源IP允许的最大连接数不区分用户名；4.该配置对已有链接不会强制断链；5.源IP区分VRF、IPv4、IPv6；
范例 : 
配置Telnet和STelnet单个源IP允许的最大连接数为2：ZXROSNG(config)#line telnet max-source-connection 2
相关命令 : 
无 
## line telnet server disable 

line telnet server disable 
命令功能 : 
用来关闭Telnet服务器功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet server disable 
 
命令参数解释 : 
					无
				 
缺省 : 
Telnet服务器功能开关默认$#34668556:0/关闭;1/打开#$ 
使用说明 : 
1.关闭Telnet服务时，现有的Telnet连接将立刻中断，新的连接将不被允许。2 该命令为交互式命令，在关闭Telnet服务时，用户输入yes确认关闭，否则不关闭。注意事项：为防止因为用户将SSH服务和Telnet服务同时关闭，而无法远程登录设备。当Telnet服务和SSH服务都关闭时，将强行打开Telnet服务，并侦听23号端口，当SSH服务打开后，才关闭Telnet服务，现有Telnet连接断链。
范例 : 
关闭Telnet服务器：ZXROSNG(config)#line telnet server disable Process will disable telnet server, Are you sure? [yes/no]:yesZXROSNG(config)#
相关命令 : 
line telnet server enable 
## line telnet server enable 

line telnet server enable 
命令功能 : 
line telnet server enable命令用来启动Telnet服务器，指定Telnet服务端侦听端口号。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet server enable 
  [listen 
 {＜default-port 
＞|＜optional-static-port 
＞}]
命令参数解释 : 
参数|描述
---|---
＜default-port＞|侦听端口号23。
＜optional-static-port＞|非知名端口号，取值范围：49152-65535。
缺省 : 
Telnet服务器功能开关默认$#34668556:0/关闭;1/打开#$；如果不指定listen端口，缺省侦听端口号为$#34668549#$。
使用说明 : 
应用场景:执行该命令，可以控制Telnet服务器的状态。只有当Telnet服务器的状态为打开时，才能连接到Telnet服务器。当关闭Telnet服务器时，现有的Telnet连接将立刻中断，新的连接将不被允许。注意事项:Telnet协议不安全，建议使用更安全的SSH协议。Telnet服务器侦听端口可配置，缺省侦听23号端口。只有Telnet服务器为disable状态时，才能通过此命令修改侦听端口号。
范例 : 
配置Telnet服务端侦听端口为50000：ZXROSNG(config)#line telnet server enable listen 50000 ZXROSNG(config)#
相关命令 : 
line telnet server disable 
## line telnet server vrf 

line telnet server vrf 
命令功能 : 
配置TELNET服务端支持的VRF名称。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
line telnet server vrf 
  ＜vrf-name 
＞
no line telnet server vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符。
缺省 : 
默认没有配置TELNET服务端支持的VRF。 
使用说明 : 
执行该配置后，将限定TELNET仅仅在该VRF内允许建立TELNET链接，网管通过其他VRF将无法与本端建立TELNET链接。默认情况下没有配置服务端支持的VRF，则允许网管通过公网或任意VRF与本端建立TELNET链接； 
范例 : 
配置TELNET服务端支持的管理口VRF：ZXROSNG(config)#line telnet server vrf mng
相关命令 : 
无。 
## logout 

logout 
命令功能 : 
该命令工作于所有模式，用于退出串口或者telnet连接。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:0,特权模式:2 
命令格式 : 
logout 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
功能与quit等效。 
范例 : 
实例一：退出串口登录 ZXROSNG#logoutZXR10 Con0 is now availablePress RETURN to get started.实例二：退出telnet连接 ZXR10>logoutConnection closedZXROSNG#
相关命令 : 
exitquit
## quit 

quit 
命令功能 : 
该命令工作于所有模式，用于退出串口或者telnet连接。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:0,特权模式:2 
命令格式 : 
quit 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
功能与logout等效。 
范例 : 
实例一：退出串口登录ZXROSNG#quitZXR10 Con0 is now availablePress RETURN to get started.实例二：退出telnet连接 ZXR10>quitConnection closedZXROSNG#
相关命令 : 
exitlogout
## show history 

show history 
命令功能 : 
查看当前终端上保存的历史命令。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show history 
 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下，显示最近10条历史命令。 
使用说明 : 
执行show history命令可以查看当前终端用户最近执行过的历史命令，便于用户查找信息。注意事项：在使用历史命令功能时，需要注意：保存的历史命令与用户输入的命令格式相同，如果用户使用了命令的不完整形式，保存的历史命令也是不完整形式。show history可以查看的历史命令条数与当前history size设置的历史命令缓冲区的大小一致。
范例 : 
设置历史命令缓冲区的大小为15：ZXROSNG(config)#history size 15查看历史命令：ZXROSNG#show historyenable 18\enable 18show running-configshow terminalterminal length 30show terminalno terminal lengthterminal width 100show terminalcon tterminal widhshowhisshow historyshow sshshow historyZXROSNG#
相关命令 : 
show terminalhistory size
## show hotkey 

show hotkey 
命令功能 : 
用来查看已定义和系统保留的快捷键的情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show hotkey 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
了解已定义和系统保留的快捷键的情况后，用户可以通过快捷键快速输入已定义的命令。在任何允许输入命令的地方都可以键入快捷键。系统执行时，会将该快捷键对应的命令显示在屏幕上，与输入完整命令的效果一致。编辑模式，快捷键支持情况：Ctrl-A  移动光标到当前行的开头。Ctrl-C  放弃所有编辑输入，退出编辑状态。Ctrl-D  不支持。Ctrl-E  移动光标到当前行的末尾。Ctrl-H  删除光标左边的一个字符。Ctrl-K  删除光标处及光标右侧所有字符。Ctrl-N  不支持。Ctrl-O  不支持。Ctrl-P  不支持。Ctrl-U  删除正在输入的整行。Ctrl-W  不支持。Ctrl-X  删除光标处及光标左侧所有字符。Ctrl-Z  不支持。Esc-B   将光标向左移动一个词。Esc-C   退出编辑状态，并将所编辑内容提交。Esc-D   删除光标右侧的一个词。Esc-F   将光标向右移动一个词。Esc-Q   不支持。Esc-U   不支持。Esc-W   删除光标左侧的一个词。编辑模式，功能键支持情况：左键       向左移动光标，如果光标在行首，将光标移到上一行的行尾。右键       向右移动光标，如果光标在行尾，将光标移到下一行的行首。上箭头     跳到（当前列）上一行。下箭头     跳到（当前列）下一行。Delete    删除当前光标处字符，如果光标在行尾，将下一行合并到当前行。Tab       两个空格。？        作为正常字符输入。空格      作为有效字符输入。Backspace 删除光标左侧的一个字符，如果光标在行首，将当前行合并到上一行。注意：编辑模式，输入任意字符，包括空格、回车、问号等都可以作为普通字符输入。
范例 : 
查看设备提供的快捷键ZXROSNG#show hotkeyKeystrokes  FunctionCtrl-A      Move the cursor onto the first character of the current lineCtrl-C      Clear the inputing command line and enter privilege mode, or interrupt the running command even if the system is busyCtrl-D      Equivalent with the command of "no debug all"Ctrl-E      Move the cursor to after the last character of the current lineCtrl-H      Same as backspace,clears the charactor before the cursorCtrl-K      Clear the line after the cursor and the cursor itselfCtrl-N      Same as the down arrow key,search command history backwardCtrl-O      Quit and suspend the session of the current terminalCtrl-P      Same as the up arrow key,search command history aheadCtrl-U      Clear the entire line currently being typedCtrl-W      Enter the terminal session suspended beforeCtrl-X      Clear the line before the cursorCtrl-Z      Clear the inputing command line and enter privilege mode, or interrupt the running commandEsc-B       Move the cursor backward one wordEsc-D       Clear the word right of the cursorEsc-F       Move the cursor forward one wordEsc-Q       Support the input of "?" and "spacebar" for a pair of the keyEsc-U       Support the input of "?" and "spacebar" for a pair of the keyEsc-W       Clear the word left of the cursorZXROSNG#输出信息描述：Ctrl-A  移动光标到当前行的开头。Ctrl-C  返回到特权模式或停止当前正在执行的功能。Ctrl-D  等同于no debug all命令。Ctrl-E  移动光标到当前行的末尾。Ctrl-H  删除光标左边的一个字符。Ctrl-K  删除光标处及光标右侧所有字符。Ctrl-N  显示历史命令缓冲区中的后一条命令。Ctrl-O  退出并挂起终端会话。Ctrl-P  显示历史命令缓冲区中的前一条命令。Ctrl-U  删除正在输入的整行。Ctrl-W  进入之前被挂起的终端会话界面。Ctrl-X  删除光标处及光标左侧所有字符。Ctrl-Z  返回到特权模式。Esc-B   将光标向左移动一个词。Esc-D   删除光标右侧的一个词。Esc-F   将光标向右移动一个词。Esc-Q   成对使用，支持输入问号和空格。Esc-U   成对使用，支持输入问号和空格。Esc-W   删除光标左侧的一个词。
相关命令 : 
无 
## show terminal 

show terminal 
命令功能 : 
该命令工作于所有模式，用于显示当前终端的终端信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show terminal 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
实例一：显示当前终端信息（telnet服务开启）ZXROSNG#show terminal Line: 0, Location :, Type: ""Length: 24 lines, Width: 80 columnsConsole idle-timeout: 02:00:00Console absolute-timeout: 1d00h00mBaud rate (TX/RX):9600/9600Capabilities: noneTime since activation: 00:03:02Editing: enabledHistory: enabled, History size: 10Telnet IPv4 ACL name: Telnet IPv6 ACL name: Telnet server: enable, Listen port: 23Telnet DSCP value: 48Telnet max-link: 15ZXROSNG#实例二：显示当前终端信息（telnet服务与ssh服务同时关闭）ZXROSNG#show terminal Line: 0, Location: , Type: "zte router"Length: 24 lines, Width: 80 columnsConsole idle-timeout: 02:00:00Console absolute-timeout: 1d00h00mBaud rate (TX/RX):9600/9600Capabilities: noneTime since activation: 00:32:50Editing: enabledHistory: enabled, History size: 10Telnet IPv4 ACL name: Telnet IPv6 ACL name: Telnet server: enable(ssh server disable), Listen port: 23Telnet DSCP value: 48Telnet max-link: 15 
相关命令 : 
无 
## show users 

show users 
命令功能 : 
该命令工作于所有模式，用于显示当前已登录的用户信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show users 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查看在线用户信息，包括：终端号、用户名、空闲时间、登录时间、主机IP、作为客户端时目的IP。功能与who命令等效。
范例 : 
显示当前已登陆的用户列表：ZXROSNG#who   Line      User      Host(s)          Idle     Login       Location * 0  con 0            idle             00:00:00 2018-03-02                                                   02:58:17       66 vty 0  zte       idle             00:01:16 2018-03-02  192.168.100.1                                                 02:57:46       67 vty 1  who       idle             00:00:04 2018-03-02  192.168.100.1                                                 02:59:00    ZXROSNG#域信息描述表：Line：用户登录的虚拟终端号，前面有*号表示是本终端User：登录的用户名Host(s)：当用本路由器作为客户端登录其它telnet服务器时，所登录的服务器的IP地址，否则显示idleIdle：闲置时间Login: 用户登录时间Location：客户端的地址
相关命令 : 
who 
## ssh 

ssh 
命令功能 : 
用来从当前设备使用SSH协议登录到其它设备。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
ssh 
  ＜dest-address 
＞ [{[encrypt 
 {none 
|aes128 
|blowfish 
|3des 
}],[compress 
 {none 
|zlib 
}],[mac 
 {none 
|sha1 
|md5 
}]}] [{[{interface 
 ＜interface-name 
＞|＜source-address 
＞}],[＜port-number 
＞],[vrf 
 ＜vrf-name 
＞],[dscp 
 ＜dscp-value 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜dest-address＞|指定远程系统（SSH服务器）的IP地址，IPv4地址类型。
none|与sha1、md5为三选一，若设置为none则表示ssh无MAC校验算法。
aes128|与none、blowfish、3des为四选一，若设置为aes128表示ssh采用aes128加密算法。
blowfish|与none、aes128、3des为四选一，若设置为blowfish则表示ssh采用blowfish加密算法。
3des|与none、aes128、blowfish为四选一，若设置为3des则表示ssh采用3des加密算法。
none|与sha1、md5为三选一，若设置为none则表示ssh无MAC校验算法。
zlib|与none为二选一，若设置为zlib则表示ssh采用zlib压缩算法。
none|与sha1、md5为三选一，若设置为none则表示ssh无MAC校验算法。
sha1|与none、md5为三选一，若设置为sha1则表示ssh采用shal MAC校验算法。
md5|与none、sha1为三选一，若设置为md5则表示ssh采用md5 MAC校验算法。
＜interface-name＞|源接口名
＜source-address＞|指定STelnet的源IPv4地址。
＜port-number＞|指定SSH服务器正在侦听的端口号。整数形式，取值范围是0～65535。默认值是协议标准端口号22。
＜vrf-name＞|指定VPN实例名。字符串形式，长度范围是1～32个字符。
＜dscp-value＞|SSH客户端发起的SSH报文的DSCP值，取值范围：0-63，默认值：48。
缺省 : 
不带目的端口号，默认使用SSH保留端口号22登录；不指定DSCP值，缺省情况下，SSH client端发起的SSH报文的DSCP值设置为48。
使用说明 : 
应用场景：Telnet缺少安全的认证方式，而且传输过程采用TCP进行明文传输，存在很大的安全隐患。与Telnet相比，SSH提供了在一个传统不安全的网络环境中，服务器通过对客户端的认证及双向的数据加密，为网络终端访问提供了安全的服务。通过本命令可以从当前设备使用SSH登录到其它设备。前置条件:使用ssh命令连接SSH服务器之前，SSH服务器端的SSH服务必须通过命令ssh server enable使能。注意事项:1.只有当服务器正在侦听的端口号是22时，SSH客户端登录时可以不指定端口号，否则如果是其他侦听端口号，SSH客户端登录时必须通过命令ssh server enable listen指定端口号。2.嵌套登录（即本设备通过自身的管理口或者业务口登录自己）只能登录一次。3.属性中的加密算法，压缩算法和HMAC较验算法由必选项改成可选项，当加密算法不选时，与SSH server协商时，提供所有支持的算法表项，先后顺序为：aes256-ctr、aes192-ctr、aes128-ctr、aes256-cbc、aes192-cbc、aes128-cbc、blowfish-cbc、3des-cbc、none；当压缩算法不选时，默认不支持压缩；当HMAC算法不选时，默认支持所有的算法列表选项，先后顺序为：hmac-sha2-256、hmac-sha1、hmac-md5、none。当需要支持强安全级别时，建议采用默认选项列表协商。4.认证方式支持password和keyboard-interactive
范例 : 
实例一： 登录地址为192.168.156.156的远程服务器，加密算法采用3des算法、压缩算法采用zlib算法、MAC校验算法采用sha1算法。ZXROSNG#ssh 192.168.156.156 encrypt 3des compress zlib mac sha1Username:
实例二：登录地址为192.168.156.200的远程服务器，加密算法采用3des算法、压缩算法采用zlib算法、MAC校验算法采用sha1算法、VRF名称为mng。ZXROSNG#ssh 192.168.156.200 encrypt 3des compress zlib mac sha1 vrf mngUsername:
实例三：登录地址为192.168.156.200的远程服务器，不设置算法，VRF名称为mng。ZXROSNG#ssh 192.168.156.200 vrf mngUsername:
相关命令 : 
ssh server enable [ listen { <22> | <49152-65535> } ]show ssh
## ssh6 

ssh6 
命令功能 : 
用来从当前设备通过IPv6地址使用SSH协议登录到其它设备。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
ssh6 
  ＜dest-address 
＞ [{[encrypt 
 {none 
|aes128 
|blowfish 
|3des 
}],[compress 
 {none 
|zlib 
}],[mac 
 {none 
|sha1 
|md5 
}]}] [{[＜port-number 
＞],[vrf 
 ＜vrf-name 
＞],[interface 
 ＜interface-name 
＞],[dscp 
 ＜dscp-value 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜dest-address＞|指定远程系统（SSH服务器）的IP地址，IPv4地址类型。
none|与sha1、md5为三选一，若设置为none则表示ssh无MAC校验算法。
aes128|与none、blowfish、3des为四选一，若设置为aes128表示ssh采用aes128加密算法。
blowfish|与none、aes128、3des为四选一，若设置为blowfish则表示ssh采用blowfish加密算法。
3des|与none、aes128、blowfish为四选一，若设置为3des则表示ssh采用3des加密算法。
none|与sha1、md5为三选一，若设置为none则表示ssh无MAC校验算法。
zlib|与none为二选一，若设置为zlib则表示ssh采用zlib压缩算法。
none|与sha1、md5为三选一，若设置为none则表示ssh无MAC校验算法。
sha1|与none、md5为三选一，若设置为sha1则表示ssh采用shal MAC校验算法。
md5|与none、sha1为三选一，若设置为md5则表示ssh采用md5 MAC校验算法。
＜port-number＞|指定SSH服务器正在侦听的端口号。整数形式，取值范围是0～65535。默认值是协议标准端口号22。
＜vrf-name＞|指定VPN实例名。字符串形式，长度范围是1～32个字符。
＜interface-name＞|指定接口名称，Linklocal地址必须要指定接口才有效。如果填写的是虚接口的名称，则该参数的取值为命令interface 配置的接口名称。默认值：无。
＜dscp-value＞|SSH客户端发起的SSH报文的DSCP值，取值范围：0-63，默认值：48。
缺省 : 
不带目的端口号，默认使用SSH保留端口号22登录。不指定DSCP值，缺省情况下，SSH client端发起的SSH报文的DSCP值设置为48。
使用说明 : 
1. 远程服务器SSH服务为使能状态（使用命令ssh server enable开启SSH服务），才能保证成功登录。2. 嵌套登录（即本设备通过自身的管理口或者业务口登录自己）只能登录一次。3. 远程服务器地址为Linklocal地址（即以fe80：开头的地址）时才需要指定接口名称。4. 远程服务器地址为Linklocal地址（即以fe80：开头的地址）时不能指定VRF名称。5. 属性中的加密算法，压缩算法和HMAC较验算法由必选项改成可选项，当加密算法不选时，与SSH server协商时，提供所有支持的算法表项，先后顺序为：aes256-ctr、aes192-ctr、aes128-ctr、aes256-cbc、aes192-cbc、aes128-cbc、blowfish-cbc、3des-cbc、none；当压缩算法不选时，默认不支持压缩；当HMAC算法不选时，默认支持所有的算法列表选项，先后顺序为：hmac-sha2-256、hmac-sha1、hmac-md5、none。当需要支持强安全级别时，建议采用默认选项列表协商。6.认证方式支持password和keyboard-interactive
范例 : 
实例一： 登录地址为2000::1000的远程服务器，加密算法采用3des算法、压缩算法采用zlib算法、MAC校验算法采用sha1算法。ZXROSNG#ssh6 2000::1000 encrypt 3des compress zlib mac sha1Username:
实例二：登录地址为2000::2000 的远程服务器，加密算法采用3des算法、压缩算法采用zlib算法、MAC校验算法采用sha1算法、VRF名称为mng。ZXROSNG#ZXROSNG# ssh6 2000::2000 encrypt 3des compress zlib mac sha1 vrf mngUsername:
实例三：登录地址为2000::2000的远程服务器，不设置算法，VRF名称为mng。ZXROSNG#ZXROSNG# ssh6 2000::2000  vrf mngUsername:
相关命令 : 
ssh server enable [ listen { <22> | <49152-65535> } ]show ssh
## telnet 

telnet 
命令功能 : 
用来从当前设备使用Telnet协议登录到其它设备。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
telnet 
  {＜dest-address 
＞ [{[{interface 
 ＜interface-name 
＞|＜source-address 
＞}],[＜port-number 
＞],[vrf 
 ＜vrf-name 
＞],[dscp 
 ＜dscp-value 
＞]}]|＜domain-name 
＞ [{[＜port-number 
＞],[vrf 
 ＜vrf-name 
＞],[dscp 
 ＜dscp-value 
＞]}]}
命令参数解释 : 
参数|描述
---|---
＜dest-address＞|指定远端设备的IP地址，IPv4地址类型。
＜interface-name＞|接口名，字符串形式，长度范围是1-31个字符。
＜source-address＞|通过指定源地址，用户可以以指定的IP地址与服务端通信，从而达到进行安全校验的目的。如果不指定源地址，Telnet连接时系统将使用本地出接口的IP地址。
＜port-number＞|指定远端设备提供Telnet服务的TCP端口号，取值范围是0-65535，缺省值是23。
＜vrf-name＞|指定通过Telnet协议登录的设备所属的VPN实例名，字符串形式，长度是1–32个字符。
＜dscp-value＞|telnet客户端发起的telnet报文的DSCP值，取值范围：0-63，默认值：48。
＜domain-name＞|远程服务器对应的域名，字符串形式，长度范围是1-128个字符。
＜port-number＞|指定远端设备提供Telnet服务的TCP端口号，取值范围是0-65535，缺省值是23。
＜vrf-name＞|指定通过Telnet协议登录的设备所属的VPN实例名，字符串形式，长度是1–32个字符。
＜dscp-value＞|telnet客户端发起的telnet报文的DSCP值，取值范围：0-63，默认值：48。
缺省 : 
无。 
使用说明 : 
应用场景：如果网络中有一台或多台设备需要配置和管理，用户无需为每一台设备连接用户终端进行本地维护。如果已知待登录设备的IP地址，用户可以通过本命令从用户终端登录需要管理的设备，对设备进行远程配置。用户可以通过此方式在一台用户终端上维护网络中的多台设备，极大地方便了用户的操作。前置条件：用户终端和远端设备之间三层互通，且远端设备使能Telnet服务器功能。配置影响：Telnet缺少安全的认证方式，而且传输过程采用TCP进行明文传输，存在安全隐患。对于安全性较高的网络，建议采用STelnet方式。嵌套登录（即本设备通过自身的管理口或者业务口登录自己）只能登录一次。
范例 : 
与远端设备建立Telnet连接。实例一： 登录地址为192.168.156.156的远程服务器。ZXROSNG#telnet 192.168.156.156OpenAttention: Telnet Escape character is ctrl+']'Warning: Telnet is not a secure protocol, and it is recommended to use SSH.       *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 23:09:48 12-30-2013Username:实例二：登录域名为www.test.com的远程服务器。ZXROSNG#telnet www.test.comOpenAttention: Telnet Escape character is ctrl+']'Warning: Telnet is not a secure protocol, and it is recommended to use SSH.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 23:16:27 12-30-2013Username:实例三：登录指定的远程服务器，其IP地址为192.168.156.200、VRF名称为mng、DSCP为45，源地址为192.168.156.200。ZXROSNG#telnet 192.168.156.200 vrf mng dscp 45 192.168.156.200OpenAttention: Telnet Escape character is ctrl+']'Warning: Telnet is not a secure protocol, and it is recommended to use SSH.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 23:19:34 12-30-2013Username:
相关命令 : 
telnet6line telnet server enableline telnet server disable
## telnet6 

telnet6 
命令功能 : 
用来从当前设备通过IPv6地址类型使用Telnet协议登录到其它设备。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
telnet6 
  {＜dest-address 
＞ [{[interface 
 ＜interface-name 
＞],[vrf 
 ＜vrf-name 
＞],[＜port-number 
＞],[dscp 
 ＜dscp-value 
＞]}]|＜domain-name 
＞ [{[vrf 
 ＜vrf-name 
＞],[＜port-number 
＞],[dscp 
 ＜dscp-value 
＞]}]}
命令参数解释 : 
参数|描述
---|---
＜dest-address＞|指定远端设备的IPv6地址。
＜interface-name＞|出接口名称，Linklocal地址必须要指定接口才有效。如果填写的是虚接口的名称，则该参数的取值为命令interface 配置的接口名称。默认值：无。
＜vrf-name＞|指定通过Telnet协议登录的设备所属的VPN实例名，字符串形式，长度是1–32个字符。
＜port-number＞|指定远端设备提供Telnet服务的TCP端口号，取值范围是0-65535，缺省值是23。
＜dscp-value＞|telnet客户端发起的telnet报文的DSCP值，取值范围：0-63，默认值：48。
＜domain-name＞|远程服务器对应的域名，字符串形式，长度范围是1-128个字符。
＜vrf-name＞|指定通过Telnet协议登录的设备所属的VPN实例名，字符串形式，长度是1–32个字符。
＜port-number＞|指定远端设备提供Telnet服务的TCP端口号，取值范围是0-65535，缺省值是23。
＜dscp-value＞|telnet客户端发起的telnet报文的DSCP值，取值范围：0-63，默认值：48。
缺省 : 
缺省情况下，telnet client端发起的telnet报文的DSCP设值为48。 
使用说明 : 
应用场景：如果网络中有一台或多台设备需要配置和管理，用户无需为每一台设备连接用户终端进行本地维护。如果已知待登录设备的IP地址，用户可以通过本命令从用户终端登录需要管理的设备，对设备进行远程配置。用户可以通过此方式在一台用户终端上维护网络中的多台设备，极大地方便了用户的操作。前置条件：用户终端和远端设备之间三层互通，且远端设备使能Telnet服务器功能。配置影响：Telnet缺少安全的认证方式，而且传输过程采用TCP进行明文传输，存在安全隐患。对于安全性较高的网络，建议采用STelnet方式。嵌套登录（即本设备通过自身的管理口或者业务口登录自己）只能登录一次。
范例 : 
实例一： 登录地址为2000::1000的远程服务器。ZXROSNG#telnet6 2000::1000OpenAttention: Telnet Escape character is ctrl+']'  Warning: Telnet is not a secure protocol, and it is recommended to use SSH.      *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 21:02:07 01-02-2014Username:实例二：登录域名为www.test.com的远程服务器ZXROSNG#telnet6 www.test.comOpenAttention: Telnet Escape character is ctrl+']'  Warning: Telnet is not a secure protocol, and it is recommended to use SSH.      *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 23:16:27 12-30-2013Username:实例三：登录指定的远程服务器，其IP地址为fe80::2ee:ffff:fe13:5100、接口名称为gei-0/1/0/8、DSCP为45，端口号为23ZXROSNG#telnet6 fe80::2ee:ffff:fe13:5100 interface gei-0/1/0/8 dscp 45 23OpenAttention: Telnet Escape character is ctrl+']'Warning: Telnet is not a secure protocol, and it is recommended to use SSH.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 23:19:34 12-30-2013Username:
相关命令 : 
telnetline telnet server enableline telnet server disable
## terminal length 

terminal length 
命令功能 : 
terminal length命令用来设置终端屏幕每屏显示的行数。no terminal length命令用来恢复缺省设置。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
terminal length 
  ＜lines 
＞
no terminal length 
命令参数解释 : 
参数|描述
---|---
＜lines＞|指定终端屏幕每屏显示的行数。整数形式，取值范围是0～512，默认值是24。取值为0时表示关闭分屏功能。
缺省 : 
缺省情况下，终端屏幕的每屏显示24行。 
使用说明 : 
1）该命令为操作命令，仅对当前终端有效，终端退出telnet连接后失效。2）可以通过show terminal命令查看当前终端的每屏显示的最大行数。3）满屏显示后会提示“—More—“，输入回车或者空格继续显示。
范例 : 
设置屏幕的每屏行数为30。ZXROSNG#terminal length 30ZXROSNG#
查看当前终端信息。ZXROSNG#show terminal Line: 0, Location: , Type: "" Length: 30 lines, Width: 80 columns Console idle-timeout: 00:30:00 Console absolute-timeout: 1d00h00m Baud rate (TX/RX):9600/9600 Capabilities: none Time since activation: 00:03:41 Editing: enabled History: enabled, History size: 10 Telnet IPv4 ACL name: Telnet IPv6 ACL name: Telnet server: enable, Listen port: 23 Telnet DSCP value: Telnet max-link: 15ZXROSNG#
相关命令 : 
show terminal 
## terminal width 

terminal width 
命令功能 : 
terminal width命令用来设置终端屏宽（每屏显示的列数）。no terminal width命令用来恢复终端屏幕每屏显示的列数到缺省值。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
terminal width 
  ＜characters 
＞
no terminal width 
命令参数解释 : 
参数|描述
---|---
＜characters＞|指定终端屏幕每屏显示的列数。整数形式，取值范围是80～512。
缺省 : 
缺省情况下，Console终端屏宽为$#34668557#$。如果Telnet登录终端屏宽协商失败，屏宽为$#34668557#$。
使用说明 : 
1.该命令为操作命令，仅对当前终端有效，终端退出后自动失效。2.屏宽有可能会被动态修改，而决定终端屏宽的有设备默认值、Telnet/SSH客户端通告参数值，所以窗口宽度会按照一定的规则进行更新，更新顺序为： 1）Telnet终端窗口宽度默认值为$#34668557#$。 2）客户端登录过程中，客户端和服务端协商的屏宽值。 3）客户端登录以后，客户端可以动态通告屏宽值，也可以通过本命令配置屏宽值。3.服务端的终端屏宽参数一般由客户端建链时协商或后续变化时动态通告来决定，通常情况，无需调整终端屏宽。在某些特殊情况下，例如客户端不支持屏宽的协商和通告，则可以使用该命令将服务端的屏宽参数设置成与客户端一致。注意事项：如果使用该命令设置的值与客户端实际屏宽不一致，则客户端与服务端各自进行换行或缩进处理，会导致客户端显示异常。
范例 : 
设置当前终端窗口宽度为100：ZXROSNG#terminal width 100查看当前终端信息：ZXROSNG#show terminal Line: 0, Location: , Type: "" Length: 24 lines, Width: 100 columns Console idle-timeout: 00:30:00 Console absolute-timeout: 1d00h00m Baud rate (TX/RX):9600/9600 Capabilities: none Time since activation: 00:20:42 Editing: enabled History: enabled, History size: 10 Telnet IPv4 ACL name: Telnet IPv6 ACL name: Telnet server: enable, Listen port: 23 Telnet DSCP value: Telnet max-link: 15ZXROSNG#
相关命令 : 
terminal lengthshow terminal
## who 

who 
命令功能 : 
该命令工作于特权模式或用户模式，用于显示当前已登录的用户信息。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
who 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查看在线用户信息，包括：终端号、用户名、空闲时间、登录时间、主机IP、作为客户端时目的IP。功能与show users命令等效。
范例 : 
显示当前已登陆的用户列表：ZXROSNG#who   Line      User      Host(s)          Idle     Login       Location * 0  con 0            idle             00:00:00 2018-03-02                                                   02:58:17       66 vty 0  zte       idle             00:01:16 2018-03-02  192.168.100.1                                                 02:57:46       67 vty 1  who       idle             00:00:04 2018-03-02  192.168.100.1                                                 02:59:00    ZXROSNG#域信息描述表：Line：用户登录的虚拟终端号，前面有*号表示是本终端User：登录的用户名Host(s)：当用本路由器作为客户端登录其它telnet服务器时，所登录的服务器的IP地址，否则显示idleIdle：闲置时间Login: 用户登录时间Location：客户端的地址
相关命令 : 
show users 
# TFTP配置命令 
## copy tftp 

copy tftp 
命令功能 : 
以TFTP方式从指定远程主机上拷入或拷出指定的文件 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
copy tftp 
  [ipv6 
] [vrf 
 ＜vrf-name 
＞] {root: 
 ＜local-directory&filename 
＞ [＜CPU node Information 
＞] ＜remote-file-path 
＞|＜remote-file-path 
＞ root: 
 ＜local-directory&filename 
＞ [＜CPU node Information 
＞]} [{[＜listen-port 
＞],[interface 
 ＜interface-name 
＞]}]
命令参数解释 : 
参数|描述
---|---
ipv6|IPv标识
＜vrf-name＞|VRF名称，长度1–32个字符，如vrf name为mng表示选择管理口
＜local-directory&filename＞|文件名或文件路径及文件名，纯文件名为1-79个字符，全路径为1-159个字符，用于上传指令
＜CPU node Information＞|用于指定操作文件的cpu信息，仅在输入的路径为绝对路径时有效，输入的路径为相对路径时不需要输入该参数。
＜remote-file-path＞|远端文件路径，全路径为1-159个字符，用于上传指令
＜remote-file-path＞|远端文件路径，全路径为1-159个字符，用于下载指令
＜local-directory&filename＞|文件名或文件路径及文件名，纯文件名为1-79个字符，全路径为1-159个字符，用于下载指令
＜CPU node Information＞|用于指定操作文件的cpu信息，仅在输入的路径为绝对路径时有效，输入的路径为相对路径时不需要输入该参数。
＜listen-port＞|监听端口，取值范围是<1-65535>
＜interface-name＞|接口名，1-31个字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
1. 从FLASH的datadisk0目录下将文件db.dat拷到主机168.1.1.1的TFTP服务器的工作目录上：ZXROSNG#copy tftp  root：/datadisk0/db.dat //168.1.1.1/db.datConnect successfully! Start copying file14% completed  00:00:20 ETA2. 从主机168.1.1.1的TFTP服务器的工作目录上将文件db.dat拷到路由器硬盘的当前目录上：ZXROSNG#copy tftp //168.1.1.1/db.dat root: db.datConnect successfully! Start copying file100% completed  00:00:35Got file successfully! Received 708096 bytes!域信息说明：Connect successfully! Start copying file：提示信息，连接成功，开始拷贝100% completed：拷贝文件进度为100%00:00:35：拷贝文件用的总时间。时：分：秒的形式00:00:20 ETA：拷贝过程中显示，预计20秒之后拷贝完成。Got file successfully! Received 708096 bytes!：拷贝文件结束提示信息。下载文件成功，708096 是接收到文件的字节数。
相关命令 : 
copy ftpcopy sftp
# 告警配置命令 
## accept 

accept 
命令功能 : 
设置日志策略是否开启接受日志，关闭后该策略不再接受任何日志。在暂时不使用策略时可用该命令关闭。默认不接受日志。 
命令模式 : 
 NETCONF日志文件默认策略模式,SNMP日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
日志文件策略模式:15,alarm日志文件默认策略模式:15,WEB日志文件默认策略模式:15,SNMP日志文件默认策略模式:15,service日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
accept 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|日志策略开关打开
off|日志策略开关关闭
缺省 : 
默认值为off。不过考虑用户使用习惯，alarm日志文件默认策略模式，service日志文件默认策略模式，NETCONF日志文件默认策略模式和日志snmp策略模式下该命令会初始化为on。 
使用说明 : 
若想使策略生效，这个开关必须打开。 
范例 : 
打开此日志策略开关。ZXROSNG(config)#logging file myPolicyZXROSNG(config-log-file- myPolicy)#accept  on
相关命令 : 
无 
## accept 

accept 
命令功能 : 
设置日志策略是否开启接受日志，关闭后该策略不再接受任何日志。在暂时不使用策略时可用该命令关闭。默认不接受日志。 
命令模式 : 
 日志SNMP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
accept 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|日志策略开关打开
off|日志策略开关关闭
缺省 : 
默认值为off。不过考虑用户使用习惯，alarm日志文件默认策略模式，service日志文件默认策略模式和日志snmp策略模式下该命令会初始化为on。 
使用说明 : 
若想使策略生效，这个开关必须打开。 
范例 : 
打开SNMP策略开关。ZXROSNG(config)#logging snmpZXROSNG(config-log-file-snmp)# accept on
相关命令 : 
无 
## alarm appear-delay 

alarm appear-delay 
命令功能 : 
该命令在全局配置模式下执行，用于设置告警产生延迟上报时间。设置告警延迟上报时间后，如果系统发生故障，则产生的告警要经过延迟时间才会上报。如果在延时时间内，故障恢复，对应的告警就不会上报。配置告警上报时延，会造成设备上报告警存在延时，因此，瞬间出现并恢复的故障，用户感知不到其告警的产生和恢复。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm appear-delay 
  ＜time 
＞
no alarm appear-delay 
命令参数解释 : 
参数|描述
---|---
＜time＞|<作用>用于设置告警产生的延迟上报时间。<取值范围>取值范围：0~10，单位：秒。<默认值>默认值：0。
缺省 : 
0 
使用说明 : 
无 
范例 : 
设置告警产生延迟8秒上报，则执行如下命令：ZXROSNG(config)#alarm appear-delay 8
相关命令 : 
无 
## alarm disappear-delay 

alarm disappear-delay 
命令功能 : 
该命令在全局配置模式下执行，用于设置告警恢复延迟上报时间，设置延迟上报时间后，如果故障恢复后，则对应的告警恢复要经过延迟时间才会上报。如果在设置时间的时间段内，设备故障恢复后又再次产生故障，告警恢复和新的告警产生均不上报。配置告警恢复上报时延，会造成故障恢复后，告警消失会存在延时。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm disappear-delay 
  ＜time 
＞
no alarm disappear-delay 
命令参数解释 : 
参数|描述
---|---
＜time＞|<作用>用于设置告警恢复的延迟上报时间。<取值范围>取值范围：0~10，单位：秒。<默认值>默认值：5。
缺省 : 
5 
使用说明 : 
无 
范例 : 
设置告警恢复延迟上报的时间为8秒，则执行如下命令：ZXROSNG(config)#alarm disappear-delay 8
相关命令 : 
无 
## alarm heartbeat-notification 

alarm heartbeat-notification 
命令功能 : 
设置告警心跳通知是否上报 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm heartbeat-notification 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|上报告警心跳通知
disable|不上报告警心跳通知
缺省 : 
默认值为disable，不上报 
使用说明 : 
当配置alarm heartbeat-notification enable打开告警心跳通知上报功能时，配置告警心跳功能(配置alarm heartbeat-period或alarm heartbeat-send)后，会同时上报一个通知。如果配置的告警心跳功能是周期性的，通知会周期性上报，为避免通知过多，可以选择配置alarm heartbeat-notification disable关闭告警心跳通知功能。 
范例 : 
打开终端显示开关：ZXROSNG#terminal monitor进入全局配置模式：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.打开告警心跳通知上报开关：ZXROSNG(config)#alarm heartbeat-notification enable打开告警心跳发送串口功能，此时有通知上报：ZXROSNG(config)#alarm heartbeat-send console May 31 21:57:35 ZXR10 alarm-log:[An alarm heart-beat message send]A notification 350304 ID 189 level 6 occurred at 11:28:16 05-27-2017 sent by ZXR10 MPU-0/20/0 %SYSTEM% Send heartbeat.  Send heartbeat msg to CONSOLE.关闭告警心跳通知上报开关：ZXROSNG(config)#alarm heartbeat-notification disable打开告警心跳发送串口功能，此时没有通知上报：ZXROSNG(config)#alarm heartbeat-send console May 31 21:57:35 ZXR10 alarm-log:[An alarm heart-beat message 
相关命令 : 
alarm heartbeat-periodalarm heartbeat-send
## alarm heartbeat-period 

alarm heartbeat-period 
命令功能 : 
该命令在全局配置模式下执行，用于设置设备定时向终端发送告警心跳消息的时间间隔和终端类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm heartbeat-period 
  ＜interval-time 
＞ ＜terminal-type 
＞
命令参数解释 : 
参数|描述
---|---
＜interval-time＞|<作用> 用于设置定时发送告警心跳消息的时间间隔。<取值范围>取值范围：0~30000，单位：分钟。<默认值>默认值：无。
＜terminal-type＞|<作用>用于设置发送告警心跳消息的设备类型。<取值范围> snmp、syslog、ftp、console、all。<取值含义>•    snmp：终端类型为SNMP服务器•    syslog：终端类型为syslog服务器 •    ftp：终端类型为FTP服务器•    console：终端类型为命令终端•    all：所有上述终端类型<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
该命令最多可以配置5条记录，每个终端类型一条。 
范例 : 
设置向FTP发送告警心跳消息周期为300分钟，则执行如下命令：ZXROSNG(config)# alarm heartbeat-period 300 ftp
相关命令 : 
无 
## alarm heartbeat-send 

alarm heartbeat-send 
命令功能 : 
该命令在全局配置模式下执行，配置该命令成功后，系统会立即向指定终端发送告警心跳消息。通过该命令可以测试设备与终端间的通信是否正常。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm heartbeat-send 
  ＜terminal-type 
＞
命令参数解释 : 
参数|描述
---|---
＜terminal-type＞|<作用>用于设置设备发送告警心跳消息时，接收该消息的终端类型。<取值范围>取值范围：snmp、syslog、ftp、console、all。<取值含义>•    snmp：终端类型为SNMP服务器 •    syslog：终端类型为syslog服务器 •    ftp：终端类型为FTP服务器•    console：终端类型为命令终端•    all：所有上述终端类型<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
通过该命令可以向指定终端发送一条心跳消息。 
范例 : 
配置设备向FTP服务器立即发送一条告警心跳消息，则执行如下命令：ZXROSNG(config)#alarm heartbeat-send ftp
相关命令 : 
无 
## alarm level-change 

alarm level-change 
命令功能 : 
该命令在全局配置模式下执行，用于修改指定告警码的告警级别。该命令配置成功后立即生效。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm level-change 
  ＜alarmcode 
＞ [tpid-type 
 ＜TPID type 
＞] ＜alarmlevel 
＞
no alarm level-change 
  ＜alarmcode 
＞ [tpid-type 
 ＜TPID type 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜alarmcode＞|告警码
＜TPID type＞|检测点类型编码，范围1-65535
＜alarmlevel＞|<作用>用于设置告警的严重级别。<取值范围>取值范围：emergencies、alerts、critical、errors、warnings、notifications、informational、debugging。<取值含义>•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7debugging：告警级别8<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
•    该命令配置完成后，可以通过show alarm level change命令查询配置的结果。•    该命令最多可以配置10000条记录。
范例 : 
将告警代码为150401的告警严重级别改为7。ZXROSNG(config)#alarm level-change 150401 informational
相关命令 : 
show alarm level change 
## alarm netconf-report 

alarm netconf-report 
命令功能 : 
该命令在配置模式下执行，用于配置告警和通知发送netconf的级别。该命令配置成功后，高于或等于该命令配置的级别的告警会主动通过netconf发送告警信息。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm netconf-report 
  ＜alarmlevel 
＞
no alarm netconf-report 
命令参数解释 : 
参数|描述
---|---
＜alarmlevel＞|<作用>用于设置告警的严重级别。<取值范围>取值范围：emergencies、alerts、critical、errors、warnings、notifications、informational、debugging。<取值含义>•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7•    debugging：告警级别8
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置告警和通知上报netconf的级别为notifications，则执行如下命令：ZXROSNG(config)#alarm netconf-report notifications
相关命令 : 
无 
## alarm trap-oid-expand 

alarm trap-oid-expand 
命令功能 : 
告警TRAP OID扩展模式开关 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm trap-oid-expand 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|告警TRAP OID扩展模式使能
disable|告警TRAP OID扩展模式去使能
缺省 : 
disable 
使用说明 : 
无 
范例 : 
告警TRAP OID扩展模式使能ZXROSNG(config)# alarm trap-oid-expand  enable
相关命令 : 
无 
## alarm-confirm 

alarm-confirm 
命令功能 : 
该命令在特权模式下执行，执行该命令可强制恢复当前告警。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-confirm 
  {from 
 ＜from-flowid 
＞ to 
 ＜to-flowid 
＞|*(＜flowid 
＞)}
命令参数解释 : 
参数|描述
---|---
from|批量清除开始
＜from-flowid＞|<作用>批量强制恢复时开始的流水号；<取值范围>取值范围：1- 4294967295。 <默认值>默认值：无。
to|批量清除结束
＜to-flowid＞|<作用>批量强制恢复时结束的流水号。<取值范围>取值范围：1- 4294967295。<默认值>默认值：无。
＜flowid＞|<作用>需要强制恢复的当前告警的流水号（支持输入10个流水号，以空格隔开）。当前告警流水号可以通过show alarm current命令查询。<取值范围>取值范围：1- 4294967295。 <默认值>默认值：无。
缺省 : 
无 
使用说明 : 
1、该命令用于强制恢复当前告警，一般只用于个别无法恢复的告警。当前设备存在的告警信息可以通过show alarm current命令查询。2、批量恢复告警时，一次最多支持恢复100个告警。
范例 : 
强制恢复流水号为4和5的当前告警，则执行如下命令：ZXROSNG# alarm-confirm 4 5批量恢复流水号从10到20的当前告警，则执行如下命令：ZXROSNG# alarm-confirm from 10 to 20
相关命令 : 
无 
## buffer 

buffer 
命令功能 : 
该命令在日志文件策略模式下执行，用于设置日志策略缓冲区的大小。 
命令模式 : 
 NETCONF日志文件默认策略模式,SNMP日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,cmd日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
日志文件策略模式:15,alarm日志文件默认策略模式:15,WEB日志文件默认策略模式:15,service日志文件默认策略模式:15,cmd日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15,SNMP日志文件默认策略模式:15 
命令格式 : 
buffer 
  ＜size 
＞
no buffer 
命令参数解释 : 
参数|描述
---|---
＜size＞|<作用>用于设置日志策略缓冲区的大小。<取值范围>取值范围：100~1000，单位：千字节。<默认值>默认值：200 KB。
缺省 : 
200 
使用说明 : 
1、如果日志策略缓冲区被占满，设备会自动触发写日志策略缓存到文件的操作。2、若想在自定义策略下执行此命令，项目需要先支持自定义策略，即提供写盘路径。
范例 : 
设置告警日志缓存大小为100KB，则执行如下命令：ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#buffer 100
相关命令 : 
无 
## clear buffer 

clear buffer 
命令功能 : 
将日志缓冲区清空 
命令模式 : 
 NETCONF日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
alarm日志文件默认策略模式:15,WEB日志文件默认策略模式:15,日志文件策略模式:15,service日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
clear buffer 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1、清空缓存之前会将缓存中的内容遍历写文件；2、若想在自定义策略下执行此命令，项目需要先支持自定义策略，即提供写盘路径
范例 : 
ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#clear buffer
相关命令 : 
无 
## clear logging 

clear logging 
命令功能 : 
该命令工作于特权模式，用于将告警日志缓冲区清空。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear logging 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令只用于清除告警日志缓冲区，无法清除其它日志缓冲区。清除前，设备会将缓冲区中未写入文件的告警日志自动写入文件。 
范例 : 
清除告警日志缓冲区，可以执行下面的命令。ZXROSNG#clear logging
相关命令 : 
无 
## debug-redirect 

debug-redirect 
命令功能 : 
该命令在全局配置模式下执行，用于配置将debug日志重定向到指定文件中。配置重定向后，debug日志不会发送到终端。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
debug-redirect 
 filename 
 ＜filename 
＞ size 
 ＜filesize 
＞ {for-end 
|for-cycle 
}
no debug-redirect 
命令参数解释 : 
参数|描述
---|---
＜filename＞|<作用>用于设置debug日志文件名。<取值范围>取值范围：长度为2-32的字符串。<默认值>默认值：无。
＜filesize＞|<作用>用于设置debug日志文件大小。<取值范围>取值范围：1~100MB，单位MB。<默认值>默认值：无。
for-end|<取值规则>若设置为for-end，则表示文件大小达到设置的阈值后不再记录。
for-cycle|<取值规则>若设置为for-cycle，则表示文件大小达到设置的阈值后删除文件重新记录。
缺省 : 
无 
使用说明 : 
只有打开debug日志上报的开关，设备才会上报debug日志。debug日志上报开关命令参见debug。 
范例 : 
将debug信息重定向到debug.txt，文件最大为50MB，文件达到最大值后不再写文件，则执行如下命令：ZXROSNG(config)# debug-redirect filename debug.txt size 50 for-end
相关命令 : 
无
## files 

files 
命令功能 : 
配置日志写文件的文件个数和单个文件的容量或者文件按天保存的最大天数和单个文件的容量。 
命令模式 : 
 日志文件策略模式  
命令默认权限级别 : 
15 
命令格式 : 
files 
  {day 
 ＜day-num 
＞|number 
 ＜file-num 
＞} per-size 
 ＜file-maxcapacity 
＞
no files 
命令参数解释 : 
参数|描述
---|---
＜day-num＞|日志文件按天保存的最大天数，范围是[7-365]
＜file-num＞|日志文件的个数，范围是: 日志文件自定义策略模式下面是[2,300]
＜file-maxcapacity＞|每个文件的最大容量，范围是[100,102400]，单位是KB
缺省 : 
file-num:7file-maxcapacity：默认为$#251723781#$KB
使用说明 : 
1、若想在自定义策略下执行此命令，首先确认该产品是否支持自定义策略，可以使用show logging buffer 加自定义策略名的方式，查看Log file path:是否有内容；有则支持，反之不支持。如果文件是按照文件个数来保存，则配置files number m，文件会按照配置的个数m来生成下标0-(m-1)的文件并循环覆盖；如果是按照天数来保存，则配置files day n，文件只保存最近 n天的日志，超过n天的会被删除。
范例 : 
配置自定义策略alarmlog下的文件个数为10，单个文件的容量为1000KB：ZXROSNG(config)#logging file alarmlogZXROSNG(config-log-file-alarmlog)# files number 10 per-size 1000
相关命令 : 
buffer,ftp,writelog 
## files 

files 
命令功能 : 
配置日志写文件的文件个数和单个文件的容量或者文件按天保存的最大天数和单个文件的容量。 
命令模式 : 
 NETCONF日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,cmd日志文件默认策略模式,service日志文件默认策略模式  
命令默认权限级别 : 
alarm日志文件默认策略模式:15,WEB日志文件默认策略模式:15,service日志文件默认策略模式:15,cmd日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
files 
  {day 
 ＜day-num 
＞|number 
 ＜file-num 
＞} per-size 
 ＜file-maxcapacity 
＞
no files 
命令参数解释 : 
参数|描述
---|---
＜day-num＞|日志文件按天保存的最大天数，范围是[7-365]
＜file-num＞|日志文件的个数，范围是: alarm日志文件默认策略模式\cmd日志文件默认策略模式\service日志文件默认策略模式下是[7,300]，在NETCONF日志文件默认策略模式下面是[2-300]
＜file-maxcapacity＞|每个文件的最大容量，范围是[100,102400]，单位是KB
缺省 : 
file-num:7file-maxcapacity：默认为$#251723781#$KB
使用说明 : 
如果文件是按照文件个数来保存，则配置files number m，文件会按照配置的个数m来生成下标0-(m-1)的文件并循环覆盖；如果是按照天数来保存，则配置files day n，文件只保存最近 n天的日志，超过n天的会被删除。
范例 : 
配置告警默认策略下的文件个数为10，单个文件的容量为1000KB：ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#files number 10 per-size 1000
相关命令 : 
buffer,ftp,writelog 
## flush 

flush 
命令功能 : 
将缓冲区中的日志保存到文件或者将当前文件上传ftp 
命令模式 : 
 NETCONF日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,cmd日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
WEB日志文件默认策略模式:15,日志文件策略模式:15,service日志文件默认策略模式:15,alarm日志文件默认策略模式:15,cmd日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
flush 
  {local 
|ftp 
}
命令参数解释 : 
参数|描述
---|---
local|将缓冲区中的日志写入文件，无FTP相关操作
ftp|将当前文件上传FTP服务器，无写文件操作
缺省 : 
无 
使用说明 : 
若想在自定义策略下执行此命令，项目需要先支持自定义策略，即提供写盘路径 
范例 : 
将告警默认策略下日志缓冲区中未写盘的内容保存到文件：ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#flush local
相关命令 : 
buffer,ftp,writelog 
## ftp 

ftp 
命令功能 : 
设置日志上报的FTP服务器，使用no命令取消设置 
命令模式 : 
 NETCONF日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,cmd日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
WEB日志文件默认策略模式:15,日志文件策略模式:15,service日志文件默认策略模式:15,cmd日志文件默认策略模式:15,alarm日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
ftp 
  [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜interfacename 
＞]|＜ipv4addr 
＞} ＜usrName 
＞ {encrypted 
 ＜encrypt-password 
＞|＜password 
＞}
no ftp 
命令参数解释 : 
参数|描述
---|---
＜vrfname＞|VPN的名称, 长度为1~32个字符
＜ipv6addr＞|IPv6的地址
＜interfacename＞|接口名
＜ipv4addr＞|IPv4的地址
＜usrName＞|FTP服务器的登录用户名，长度为1~31个字符
＜encrypt-password＞|FTP服务器的密文密码，长度为64或128个字符
＜password＞|FTP服务器的明文密码，长度为1~64个字符
缺省 : 
无 
使用说明 : 
1、本命令配置FTP服务器，日志文件在切换文件的时候，或者手动执行flush ftp的时候将当前文件上传到FTP，既不是实时上传，也不是定时上传；2、若想在自定义策略下执行此命令，项目需要先支持自定义策略，即提供写盘路径；
范例 : 
配置告警默认策略下的日志文件上传FTP的服务器地址为192.168.100.3，用户名为root，密码为passwordZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#ftp 192.168.100.3 root password
相关命令 : 
logging ftp、logging filesavetime 
## interval 

interval 
命令功能 : 
该命令在日志文件策略模式下执行，用于配置日志定时写入文件的间隔时间。 
命令模式 : 
 NETCONF日志文件默认策略模式,WEB日志文件默认策略模式,alarm日志文件默认策略模式,cmd日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
WEB日志文件默认策略模式:15,日志文件策略模式:15,service日志文件默认策略模式:15,cmd日志文件默认策略模式:15,alarm日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
interval 
  ＜interval-time 
＞
no interval 
命令参数解释 : 
参数|描述
---|---
＜interval-time＞|<作用>用于配置日志策略缓存定时写文件的间隔时间。<取值范围>取值范围：2~1800000，单位：秒。
缺省 : 
cmd日志文件默认策略模式下的默认值是2；其余模式下的默认值是600。 
使用说明 : 
1、当配置的时间间隔到达后，日志策略缓冲区中的日志会被系统自动写入文件。配置间隔时间过短，频繁写文件，可能会影响存储设备的寿命。建议使用默认配置即可；2、若想在自定义策略下执行此命令，项目需要先支持自定义策略，即提供写盘路径
范例 : 
设置告警默认策略下定时写日志间隔时间为100秒ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#interval 100
相关命令 : 
无 
## level 

level 
命令功能 : 
设置记录到日志文件中的日志级别，仅对告警有效。 
命令模式 : 
 alarm日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
日志文件策略模式:15,alarm日志文件默认策略模式:15 
命令格式 : 
level 
  ＜alarmlevel 
＞ [severity-relation 
 {higher-or-equal 
|equal 
|lower-or-equal 
}
no level 
命令参数解释 : 
参数|描述
---|---
＜alarmlevel＞|告警日志级别，（1：emergencies；2：alerts；3：critical；4：errors；5：warnings；6：notifications；7：informational；8：debugging）
higher-or-equal|大于等于配置的级别，emergencies级别最高
equal|等于配置的级别
lower-or-equal|小于等于配置的级别，emergencies级别最高
缺省 : 
在alarm日志文件默认策略模式下，level的默认值是$#251723783#$；在日志文件策略模式下面没有默认值，即no操作后，所有的告警日志都进行处理；不配置severity-relation  时，默认是higher-or-equal生效。 
使用说明 : 
1、此命令如果在日志策略下面配置，则仅对策略里面匹配的告警日志有效；2、若想在自定义策略下执行此命令，项目需要先支持自定义策略，即提供写盘路径
范例 : 
设置告警默认策略下记录级别在errors和errors以上的告警消息到日志文件中。ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)#level errors
相关命令 : 
无 
## logging almlog-timestamps 

logging almlog-timestamps 
命令功能 : 
支持告警日志显示时间格式是否带有时区偏移 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging almlog-timestamps 
 with-timezone-offset 
 {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|告警日志信息的时间带有时区偏移。
disable|命令日志信息的时间不带有时区偏移。
缺省 : 
disable 。 
使用说明 : 
该命令控制告警日志的显示时间格式，当配置enable 时，告警日志的显示格式时间带有时区偏移；当配置enable 时，告警日志的显示格式时间不带有时区偏移。这个命令与logging timestamps 配置一起对告警时间格式生效，当logging timestamps 配置为uptime 时，即使logging almlog-timestamps with-timezone-offset配置为enable ，告警日志时间格式中也不带有时区偏移。
范例 : 
打开终端显示开关：ZXROSNG#terminal monitor进入全局配置模式：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.设置告警日志信息的时间显示格式带有时区偏移：ZXROSNG(config)#logging almlog-timestamps with-timezone-offset enable上报告警后显示：ZXROSNG(config-if-loopback1)#shutdown An alarm 150111 ID 12 level 5 occurred at 09:08:27 12-21-2017 UTC+08:00 sent by ZXR10 MPU-0/20/0%IP% Interface layer2 status  The interface(index=25,name='loopback1') layer2 status turned into protocol DOWNAn alarm 150101 ID 13 level 5 occurred at 09:08:27 12-21-2017 UTC+08:00 sent by ZXR10 MPU-0/20/0%IP% Interface status  The interface(index=25,name='loopback1') turned into protocol DOWNZXROSNG#
相关命令 : 
logging timestamps，clock timezoneshow logging alarm，show logging buffer almlog，show alarm
## logging cmdlog-timestamps 

logging cmdlog-timestamps 
命令功能 : 
支持命令日志显示时间格式类型，精确到秒级还是毫秒级。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging cmdlog-timestamps 
  {datetime 
|precisetime 
}
no logging cmdlog-timestamps 
命令参数解释 : 
参数|描述
---|---
datetime|命令日志信息的时间为标准时间（即当地的日期格式），格式为hh:mm:ss  mm-dd-yyyy。
precisetime|命令日志信息的时间为附带毫秒的标准时间，格式为hh:mm:ss.ms  mm-dd-yyyy。
缺省 : 
datetime。 
使用说明 : 
该命令控制命令日志的显示时间粒度，当配置datetime时，命令日志的显示格式是不带毫秒的本地时间；当配置precisetime时，命令日志的显示格式带毫秒。 
范例 : 
设置命令日志信息的时间显示格式为附带毫秒的标准时间，则执行如下命令：ZXROSNG(config)# logging cmdlog-timestamps precisetime ZXROSNG(config)#show logfileStartTime: 16:04:31.292 09-12-2015  EndTime: 16:04:32.381 09-12-2015  FlowID: 7  VtyNo: con0  UserName:   UserLevel: 1  IP:   HostName: ZXR10  Result: success  CMDLevel: N/A  CMDLine: /--- console update privilege success ---/  ZXROSNG(config)# logging cmdlog-timestamps datetime ZXROSNG(config)#show logfileStartTime: 16:04:31 09-12-2015  EndTime: 16:04:32 09-12-2015  FlowID: 7  VtyNo: con0  UserName:   UserLevel: 1  IP:   HostName: ZXR10  Result: success  CMDLevel: N/A  CMDLine: /--- console update privilege success ---/                                                                         
相关命令 : 
Show logfile, show logging buffer 
## logging console 

logging console 
命令功能 : 
该命令在全局配置模式下执行，用于设置发送到命令终端的告警消息的级别。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging console 
  ＜alarmlevel 
＞
no logging console 
命令参数解释 : 
参数|描述
---|---
＜alarmlevel＞|<作用>用于设置发送到命令终端的告警消息的级别（只有高于或等于该级别的告警才会发送）。<取值范围>取值范围：emergencies、alerts、critical、errors、warnings、notifications、informational、debugging。<取值含义>•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7debugging：告警级别8<默认值>默认值：notifications
缺省 : 
$#251723782#$级 
使用说明 : 
只有严重级别高于或等于该命令配置的级别的告警才会发送到命令终端。 
范例 : 
将严重级别高于等于warning级别的（包括warnings级别）的告警消息发送到命令终端，则执行如下命令：ZXROSNG(config)#logging console warnings
相关命令 : 
无 
## logging file default almlog 

logging file default almlog 
命令功能 : 
进入告警日志文件默认策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file default almlog 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是进入告警日志文件默认策略，不可以删除。 
范例 : 
进入告警日志文件默认策略ZXROSNG(config)#logging file default almlogZXROSNG(config-log-file-default-almlog)# 
相关命令 : 
无 
## logging file default cmdlog 

logging file default cmdlog 
命令功能 : 
进入命令日志文件默认策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file default cmdlog 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是进入命令日志文件默认策略，不可以删除。 
范例 : 
进入命令日志文件默认策略ZXROSNG(config)#logging file default cmdlogZXROSNG(config-log-file-default-cmdlog)# 
相关命令 : 
无 
## logging file default netclog 

logging file default netclog 
命令功能 : 
进入NETCONF日志文件默认策略模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file default netclog 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是用于进入NETCONF日志文件默认策略模式。 
范例 : 
进入NETCONF日志文件默认策略ZXROSNG(config)#logging file default netclog ZXROSNG(config-log-file-default-netclog)#
相关命令 : 
无 
## logging file default snmplog 

logging file default snmplog 
命令功能 : 
进入SNMP日志文件默认策略模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file default snmplog 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是用于进入SNMP日志文件默认策略模式。 
范例 : 
进入SNMP日志文件默认策略ZXROSNG(config)#logging file default snmplogZXROSNG(config-log-file-default-snmplog)#
相关命令 : 
无 
## logging file default srvlog 

logging file default srvlog 
命令功能 : 
进入业务日志文件默认策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file default srvlog 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是进入业务日志文件默认策略，不可以删除。 
范例 : 
进入业务日志文件默认策略ZXROSNG(config)#logging file default srvlogZXROSNG(config-log-file-default-srvlog)# 
相关命令 : 
无 
## logging file default weblog 

logging file default weblog 
命令功能 : 
进入WEB日志文件默认策略模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file default weblog 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是用于进入WEB日志文件默认策略模式。 
范例 : 
进入WEB日志文件默认策略ZXROSNG(config)#logging file default weblogZXROSNG(config-log-file-default-weblog)#
相关命令 : 
无 
## logging file 

logging file 
命令功能 : 
进入日志文件默认策略 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging file 
  ＜policy-name 
＞
no logging file 
  ＜policy-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜policy-name＞|自定义的策略名，仅支持字母，数字和下划线，支持1-32个字符，不能和默认策略的名称一样。
缺省 : 
无 
使用说明 : 
此命令是创建自定义的日志文件策略，可以删除。 
范例 : 
创建自定义策略myPolicyZXROSNG(config)#logging file myPolicyZXROSNG(config-log-file-myPolicy)# 
相关命令 : 
无 
## logging filesavetime 

logging filesavetime 
命令功能 : 
该命令在全局配置模式下执行，用于配置当前缓冲区中的告警日志上传的FTP服务器的相关参数，配置的文件名只是前缀，文件名还包括序号和后缀.txt。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging filesavetime 
  {interval 
 ＜interval 
＞|everyday 
 ＜time 
＞|week 
 ＜weekday 
＞ ＜time 
＞|month 
 ＜month 
＞ ＜time 
＞} [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜interfacename 
＞]|＜ipv4addr 
＞} ＜username 
＞ {encrypted 
 ＜encrypt-password 
＞|＜password 
＞} [＜prefix 
＞]
no logging filesavetime 
命令参数解释 : 
参数|描述
---|---
＜interval＞|<作用>用于设置保存告警日志文件的时间间隔，不能低于一小时，精确到秒。格式为hh:mm:ss。<取值范围>取值范围： 1:00:00~23:59:59。<默认值>默认值：无。
＜time＞|<作用>用于设置每月保存告警日志文件的开始时间，格式为hh:mm:ss<取值范围>取值范围：00:00:00~23:59:59。<默认值>默认值：无。
＜weekday＞|<作用>用于设置每周保存告警日志文件的日期。<取值范围>取值范围：Monday、Tuesday、Wednesday、Thursday、Friday、Saturday、sunday。<默认值>默认值：无。
＜time＞|<作用>用于设置每月保存告警日志文件的开始时间，格式为hh:mm:ss<取值范围>取值范围：00:00:00~23:59:59。<默认值>默认值：无。
＜month＞|<作用>用于设置每月保存告警日志文件的日期<取值范围>取值范围：1~31。<默认值>默认值：无。
＜time＞|<作用>用于设置每月保存告警日志文件的开始时间，格式为hh:mm:ss<取值范围>取值范围：00:00:00~23:59:59。<默认值>默认值：无。
＜vrfname＞|<作用>用于设置FTP服务器所属的VPN的名称。<取值范围>取值范围：长度为1-32的字符串。<默认值>默认值：无。
＜ipv6addr＞|<作用>用于设置FTP服务器的IPv6的地址。<默认值>默认值：无
＜interfacename＞|<作用>用于设置FTP服务器的接口名，只有IPv6地址为linklocal类型时，才需要配置接口名。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv4addr＞|<作用>用于设置FTP服务器的IPv4的地址。<默认值>默认值：无
＜username＞|<作用>用于设置登录FTP服务器的用户名。<取值范围>取值范围：长度为1~65的字符串。<默认值>默认值：无。
＜encrypt-password＞|<作用>用于设置登录FTP服务器的密文密码。<取值范围>取值范围：长度为64或128的字符串。<默认值>默认值：无。
＜password＞|<作用>用于设置登录FTP服务器的明文密码。<取值范围>取值范围：长度为1~64的字符串。<默认值>默认值：无。
＜prefix＞|<作用>用于设置告警消息上传到FTP上的存储文件名的前缀。<取值范围>取值范围：长度为1~31的字符串。<默认值>默认值：无
缺省 : 
无 
使用说明 : 
配置该命令前需要先运行logging on命令 
范例 : 
设置将告警日志文件在每天0点保存后发送到168.1.70.100 FTP服务器上，登录FTP服务器的用户名为target、口令为target，保存文件名前缀为zxrt64log，则执行如下命令：ZXROSNG(config)#logging filesavetime everyday 00:00:00 168.1.70.100 target target zxrt64log
相关命令 : 
无 
## logging ftp 

logging ftp 
命令功能 : 
该命令在全局配置模式下执行，用于配置告警日志实时上报的FTP服务器的相关参数。使用no命令取消该FTP设置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging ftp 
  ＜level 
＞ [vrf 
 ＜vrfnmae 
＞] {＜ipv6addr 
＞ [interface 
 ＜interfacename 
＞]|＜ipv4addr 
＞} ＜usrName 
＞ {encrypted 
 ＜encrypt-password 
＞|＜password 
＞} [＜fileName 
＞]
no logging ftp 
命令参数解释 : 
参数|描述
---|---
＜level＞|<作用>用于设置上传FTP的告警日志的严重级别（只有高于或等于该级别的告警日志才会上传FTP）。<取值范围>取值范围：emergencies、alerts、critical、errors、warnings、notifications、informational、debugging。<取值含义>•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7•    debugging：告警级别8<默认值>默认值：无。
＜vrfnmae＞|<作用>用于设置FTP服务器所属的VPN的名称。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv6addr＞|<作用>用于设置FTP服务器的IPv6的地址。<默认值>默认值：无。
＜interfacename＞|<作用>用于设置IPv6 FTP服务器的接口名。只有IPv6地址为linklocal类型时，才需要配置接口名。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv4addr＞|<作用>用于设置FTP服务器的IPv4的地址。<默认值>默认值：无。
＜usrName＞|<作用>用于设置登录FTP服务器的用户名。<取值范围>取值范围：长度为1~65的字符串。<默认值>默认值：无。
＜encrypt-password＞|<作用>用于设置登录FTP服务器的密文密码。<取值范围>取值范围：长度为64或128的字符串。<默认值>默认值：无。
＜password＞|<作用>用于设置登录FTP服务器的明文密码。<取值范围>取值范围：长度为1~64的字符串。<默认值>默认值：无。
＜fileName＞|<作用>用于设置告警消息上传到FTP上的存储文件名。<取值范围>取值范围：长度为1~31的字符串。<默认值>默认值：无
缺省 : 
无 
使用说明 : 
配置该命令前需要先运行logging on命令。另外在FTP服务器对应的目录中必须要有该命令配置的文件名存在且可写。 
范例 : 
设置将告警级别高于NOTIFICATIONS的告警日志上传到IP地址为192.168.100.3，登录用户名为root，登录密码为password的FTP服务器，保存的文件名为zte，则执行如下命令：ZXROSNG(config)#logging ftp NOTIFICATIONS 192.168.100.3 root password zte
相关命令 : 
无 
## logging header 

logging header 
命令功能 : 
该命令在全局配置模式下执行，用于配置show logging buffer命令回显和日志文件策略记录格式是否带新的公共头信息。通过no命令关闭两者带新的公共头信息功能。默认情况下show logging buffer命令回显和日志文件策略记录格式带新的公共头信息功能是不支持的。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging header 
 
no logging header 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景当需要show logging buffer回显和记录策略文件增加新的公共头信息时，可配置此命令支持信息回显和记录新格式，新的公共头信息中的流水号是按日志大类独立分配，能够统计日志是否被删除。后续操作可以通过show logging buffer来查看当前缓冲区日志和查看文件记录日志的流水号来统计日志是否被删除。注意事项配置logging header，仅show logging buffer回显和记录策略文件增加新的公共头信息，不影响show logfile，show logging alarm和show logging service的回显，且show logging buffer回显和记录策略文件两者根据配置命令都带新的公共头信息或都不带新的公共头信息，两者保持一致。执行no logging header，show logging buffer回显为老的头信息，而写入文件的日志不带头信息。
范例 : 
执行logging header命令设置日志回显和记录格式带新的公共头信息显示，然后show logging buffer almlog，界面呈现带新的公共头信息的信息(起始[]里的内容)：ZXROSNG(config)#logging headerZXROSNG(config-log-file-default-almlog)#show logging buffer almlog……[6/2020-02-28 20:10:41.838/01/ALARM/3] An alarm 350201 ID 4 level 3 cleared at 20:10:35 02-28-2020 sent by ZXR10 MPU-0/20/0%SNMP% SNMP  SNMPv1 function succeed to start…………
相关命令 : 
show logging buffer
## logging nat buffer 

logging nat buffer 
命令功能 : 
该命令在全局配置模式下执行，用于设置NAT日志的缓冲区大小。NAT日志缓冲区大小的默认值为1000条。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat buffer 
  ＜size 
＞
no logging nat buffer 
命令参数解释 : 
参数|描述
---|---
＜size＞|<作用> 用于设置NAT日志缓冲区可以存储的日志数量。<取值范围>取值范围：10~1000 条。<默认值>默认值：1000条。
缺省 : 
1000条 
使用说明 : 
无 
范例 : 
设置NAT日志缓冲区的大小为300条，则执行如下命令：ZXROSNG(config)# logging nat buffer 300
相关命令 : 
无 
## logging nat description-type 

logging nat description-type 
命令功能 : 
该命令在全局配置模式下执行，用于设置NAT日志文件名描述类型。NAT日志文件名描述类型默认为basemac。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat description-type 
  {basemac 
|hostname 
}
命令参数解释 : 
参数|描述
---|---
basemac|<取值规则>若设置为basemac，则表示将mac地址作为文件名组成的一部分。
hostname|<取值规则>若设置为hostname，则表示将hostname作为文件名组成的一部分。
缺省 : 
basemac
使用说明 : 
无
范例 : 
设置NAT日志名字描述类型为hostname，则执行如下命令：ZXROSNG(config)# logging nat description-type hostname
相关命令 : 
hostname
## logging nat file-size 

logging nat file-size 
命令功能 : 
该命令在全局配置模式下执行，用于设置NAT日志文件的大小和数量。使用no命令取消设置，恢复缺省值。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat file-size 
  ＜size 
＞ [file-num 
 ＜num 
＞]
no logging nat file-size 
命令参数解释 : 
参数|描述
---|---
＜size＞|<作用>用于设置NAT日志文件的大小。<取值范围>取值范围：50~100，单位：M。<默认值>默认值：50 M 。
＜num＞|<作用>用于设置NAT日志文件的数量。<取值范围>取值范围：2~300 个。<默认值>默认值：$#251723794#$个。
缺省 : 
NAT日志的大小，缺省为50M。NAT日志的数量，缺省为$#251723794#$个 
使用说明 : 
配置的file-num为n，则产生的文件的下标是从0到(n-1)。当下标重新从0开始的时候，老的下标为m（0≤m≤n-1）的文件会被新的下标为m的文件所覆盖。 
范例 : 
设置NAT日志的大小为30M，个数为15个，则执行如下命令：ZXROSNG(config)#logging nat file-size 30 file-num 15
相关命令 : 
无 
## logging nat ftp 

logging nat ftp 
命令功能 : 
该命令在全局配置模式下执行，用于设置发送NAT日志到FTP服务器的相关参数。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat ftp 
  [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜interfacename 
＞]|＜ipv4addr 
＞} ＜username 
＞ {encrypted 
 ＜encrypt-password 
＞|＜password 
＞}
no logging nat ftp 
命令参数解释 : 
参数|描述
---|---
＜vrfname＞|<作用>用于设置FTP服务器所属的VPN的名称。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv6addr＞|<作用>用于设置FTP服务器的IPv6的地址。<默认值>默认值：无。
＜interfacename＞|<作用>用于设置FTP服务器的接口名。只有IPv6的地址为linklocal类型时，才需要配置该参数。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv4addr＞|<作用>用于设置FTP服务器的IPv4的地址。<默认值>默认值：无。
＜username＞|<作用>用于设置登录FTP服务器的用户名。<取值范围>取值范围：长度为1~65的字符串。<默认值>默认值：无。
＜encrypt-password＞|<作用>用于设置登录FTP服务器的密文密码。<取值范围>取值范围：长度为64或128的字符串。<默认值>默认值：无。
＜password＞|<作用>用于设置登录FTP服务器的明文密码。<取值范围>取值范围：长度为1~64的字符串。<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
配置该命令前，必须已使用logging命令打开日志模块的开关（即将logging命令设置为on），并且已使用logging nat terminal命令打开日志记录功能（即将logging nat terminal命令设置为local）。否则，不会在本地产生日志文件，也就无法上传日志文件到FTP服务器上。本地保存的日志文件在文件切换（即文件满、文件内容格式产生变化、手动执行写文件等情况下）时上传到FTP服务器上。上传到FTP服务器成功后，本地保存的日志文件自动被删除。如果文件上传失败，则该文件将会被新的相同下标的NAT日志文件所覆盖。NAT日志量比较大，因此，系统会根据logging nat description-type命令配置的NAT文件名前缀、文件下标以及当前日期不断地生成新的NAT日志文件（文件名形如00eef3771300_CGN_000000_97_20140214061436.nat.bin，97为文件的下标。下标的取值参见logging nat file-size命令。），并将新产生的NAT日志保存在新的NAT日志文件中。
范例 : 
设置将NAT日志发送到地址为168.1.70.100 的FTP服务器上，FTP服务器的登录用户名为target，密码为target，则执行如下命令：ZXROSNG(config)#logging nat ftp 168.1.70.100 target target
相关命令 : 
无 
## logging nat savetime 

logging nat savetime 
命令功能 : 
设置NAT当前写入的日志文件定时上传到FTP的开始时间和间隔。使用no命令取消设置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat savetime 
 start-time 
 ＜time 
＞ interval 
 ＜interval 
＞
no logging nat savetime 
命令参数解释 : 
参数|描述
---|---
＜time＞|上传的开始时间，精确到秒
＜interval＞|配置采样的间隔；不能低于一小时，精确到秒
缺省 : 
无 
使用说明 : 
配置此配置，需要先配置logging nat ftp，否则会报错。另外FTP服务器的目录，需要开启允许增加、删除和覆盖的权限。 
范例 : 
设置NAT日志从8点开始，每隔2个小时上传一次。ZXROSNG(config)#logging nat savetime start-time 08:00:00 interval 02:00:00
相关命令 : 
logging nat ftplogging nat zip
## logging nat sftp 

logging nat sftp 
命令功能 : 
设置发送NAT日志到SFTP服务器。使用no命令取消设置 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat sftp 
  [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜interfacename 
＞]|＜ipv4addr 
＞} ＜username 
＞ {encrypted 
 ＜encrypt-password 
＞|＜password 
＞} encrypt 
 {none 
|aes128 
|blowfish 
|3des 
} compress 
 {none 
|zlib 
} mac 
 {none 
|sha1 
|md5 
} [＜listen_port 
＞]
no logging nat sftp 
命令参数解释 : 
参数|描述
---|---
＜vrfname＞|VRF名称，长度为1~31个字符
＜ipv6addr＞|服务器IPv6地址，冒分十六进制格式X:X::X:X
＜interfacename＞|接口名称，仅在指定IPv6的Linklocal地址时使用
＜ipv4addr＞|服务器IPv4地址，点分十进制格式A.B.C.D
＜username＞|服务器的登录用户名，长度为1~65个字符
＜encrypt-password＞|<作用>用于设置登录SFTP服务器的密文密码。<取值范围>取值范围：长度为64或128个字符。<默认值>默认值：无。
＜password＞|服务器的登录明文口令，长度为1~64个字符
none|SFTP加密算法不指定
aes128|SFTP加密算法为aes128
blowfish|SFTP加密算法为blowfish
3des|SFTP加密算法为3des
none|SFTP压缩算法无算法
zlib|SFTP压缩算法为zlib
none|SFTP的mac校验算法不指定
sha1|SFTP的mac校验算法sha1
md5|SFTP的mac校验算法md5
＜listen_port＞|SFTP服务端的SSH监听端口，取值范围是0-65535，缺省为22
缺省 : 
＜listen_port＞ 22 
使用说明 : 
  1. 配置该命令前需要先运行logging on命令。另外必须打开NAT记录日志的功能，参见ip nat logging命令。NAT日志产生的日志量比较大，该命令可以配置指定间隔天数和确切时间，在SFTP服务器上根据当前日期和配置的文件名前缀生成新文件，并将新产生的NAT日志送到新文件中。      2. 该配置命令与logging nat ftp互斥，即不支持同时打开NAT日志的FTP和SFTP上送方式。
范例 : 
范例设置将NAT日志送到168.1.70.100 SFTP服务器上，SFTP服务器的登录用户名为target，密码为target，使用的SFTP加密/压缩/校验算法分别为3des、zlib和md5，生成新的日志文件。ZXROSNG(config)# logging nat sftp 168.1.70.100 target target encrypt 3des compress zlib mac md5
相关命令 : 
logging nat ftp 
## logging nat terminal 

logging nat terminal 
命令功能 : 
该命令在全局配置模式下执行，用于设置NAT日志是否记录到本地文件。NAT日志文件默认写入本地文件。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat terminal 
  {off 
|local 
}
命令参数解释 : 
参数|描述
---|---
off|<取值规则>若设置为off，则表示NAT日志不记录到本地文件。
local|<取值规则>若设置为local，则表示NAT日志记录到本地文件。
缺省 : 
local 
使用说明 : 
无 
范例 : 
设置NAT日志不记录到本地日志，则执行如下命令：ZXROSNG(config)#logging nat terminal off
相关命令 : 
无 
## logging nat zip 

logging nat zip 
命令功能 : 
该命令在全局配置模式下执行，用于设置发送给FTP服务器的NAT日志文件是否需要压缩。NAT日志文件默认采取压缩方式发送到FTP服务器。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging nat zip 
  {off 
|on 
}
命令参数解释 : 
参数|描述
---|---
off|<取值规则>若设置为off，则表示发送到FTP服务器的NAT日志不需要压缩。
on|<取值规则>若设置为on，则表示发送到FTP服务器的NAT日志需要压缩。
缺省 : 
on 
使用说明 : 
该命令配置生效的前提已打开NAT记录日志的功能，即logging nat terminal命令设置为local。 
范例 : 
设置将NAT日志以压缩包的方式发送到FTP服务器上，则执行如下命令：ZXROSNG(config)#logging nat zip on
相关命令 : 
logging nat terminal locallogging nat ftp
## logging portal ftp 

logging portal ftp 
命令功能 : 
该命令在全局配置模式下执行，用于配置PORTAL日志上报的FTP服务器的相关参数。使用no命令取消该设置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging portal ftp 
  [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜interfacename 
＞]|＜ipv4addr 
＞} ＜username 
＞ {encrypted 
 ＜encrypt-password 
＞|＜password 
＞}
no logging portal ftp 
命令参数解释 : 
参数|描述
---|---
＜vrfname＞|<作用>用于设置FTP服务器所属的VPN的名称。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv6addr＞|<作用>用于设置FTP服务器的IPv6的地址。<默认值>默认值：无。
＜interfacename＞|<作用>用于设置FTP服务器的接口名。只有IPv6的地址为linklocal类型时，才需要配置这个参数。<取值范围>取值范围：长度为1~32的字符串。<默认值>默认值：无。
＜ipv4addr＞|<作用>用于设置FTP服务器的IPv4的地址。<默认值>默认值：无。
＜username＞|<作用>用于设置登录FTP服务器的用户名。<取值范围>取值范围：长度为1~31的字符串。<默认值>默认值：无。
＜encrypt-password＞|<作用>用于设置登录FTP服务器的密文密码。<取值范围>取值范围：长度为64或128的字符串。<默认值>默认值：无。
＜password＞|<作用>用于设置登录FTP服务器的明文密码。<取值范围>取值范围：长度为1~64的字符串。<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
对于linklocal类型的IPv6地址需要配置出接口。 
范例 : 
设置将PORTAL日志发送到168.1.70.100 FTP服务器上，FTP服务器的登录用户名为target，口令为target，则执行如下命令：ZXROSNG(config)#logging portal ftp 168.1.70.100 target target 
相关命令 : 
无 
## logging snmp 

logging snmp 
命令功能 : 
进入日志snmp trap策略模式 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging snmp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令是进入snmp策略，进入策略后可以修改开关和配置匹配的日志类型和子串，本策略不可以删除。 
范例 : 
进入日志snmp trap策略模式ZXROSNG(config)#logging snmpZXROSNG(config-log-file-snmp)# 
相关命令 : 
accept,match 
## logging timestamps 

logging timestamps 
命令功能 : 
该命令在全局配置模式下执行，用于设置告警和debug信息的时间显示格式。缺省值为：datetime localtime（即当地的日期格式）。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging timestamps 
  {datetime 
 localtime 
|precisetime 
|uptime 
}
命令参数解释 : 
参数|描述
---|---
localtime|<取值规则>若设置为datetime localtime，则告警和debug信息的时间为标准时间（即当地的日期格式），格式为hh:mm:ss  mm-dd-yyyy 。
precisetime|<取值规则>若设置为precisetime，则告警和debug信息的时间为附带毫秒的标准时间，格式为hh:mm:ss.ms  mm-dd-yyyy。
uptime|<取值规则>若设置为uptime，则告警和debug信息的时间是设备启动以来的时间，格式为hh:mm:ss。
缺省 : 
datetime localtime 
使用说明 : 
时间的默认显示格式是本地时间。 
范例 : 
设置告警和debug信息的时间显示格式为当地的日期格式，则执行如下命令：ZXROSNG(config)#logging timestamps datetime localtime
相关命令 : 
无 
## logging trap-enable 

logging trap-enable 
命令功能 : 
该命令在配置模式下执行，设置需要发送告警trap信息的告警消息的级别。该命令配置成功后，高于或等于该命令配置的级别的告警会主动向网管发送告警trap信息。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging trap-enable 
  ＜alarmlevel 
＞
no logging trap-enable 
命令参数解释 : 
参数|描述
---|---
＜alarmlevel＞|<作用>用于设置需要发送trap信息的告警消息的严重级别（只有高于或等于该级别的告警才会发送trap信息）。<取值范围>取值范围：emergencies、alerts、critical、errors、warnings、notifications、informational、debugging。<取值含义>•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7•    debugging：告警级别8<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
打开snmp进程的trap开关（即将snmp-server设置为enable trap），网管才能收到告警trap消息。 
范例 : 
设置需要将trap消息上报到网管的告警的级别为notifications，则执行如下命令：ZXROSNG(config)#logging trap-enable notifications
相关命令 : 
无 
## logging 

logging 
命令功能 : 
该命令在全局配置模式下执行，用于开启或关闭日志功能。•    如果开启日志功能，则系统产生的日志都会被记录下来，保存在本地。•    如果关闭日志功能，则除命令日志和系统日志外的其他日志都不会被记录下来。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
logging 
  {on 
|off 
}
no logging 
 on 
命令参数解释 : 
参数|描述
---|---
on|日志功能使能
off|<取值规则>若设置为on，则将日志功能关闭。
缺省 : 
on 
使用说明 : 
该命令是日志功能的开关，只有命令日志、系统日志不受该开关的控制。 
范例 : 
开启日志功能，则执行如下命令：ZXROSNG(config)#logging on
相关命令 : 
无 
## match 

match 
命令功能 : 
设置过滤规则，规则包括日志大类和子串，符合过滤规则的得到处理 
命令模式 : 
 日志文件策略模式  
命令默认权限级别 : 
15 
命令格式 : 
match 
  {all 
|alarmlog 
|cmdlog 
|service 
|netconflog 
|snmplog 
|weblog 
} [[exclude 
] substring 
 ＜substring 
＞]
no match 
  {all 
|alarmlog 
|cmdlog 
|service 
|netconflog 
|snmplog 
|weblog 
} [substring 
 ＜substring 
＞]
				
命令参数解释 : 
参数|描述
---|---
all|所有日志
alarmlog|告警日志
cmdlog|命令日志
service|业务日志
netconflog|NETCONF日志
snmplog|SNMP日志
weblog|WEB日志
exclude|反向过滤标识
＜substring＞|子串，1-40个字符
缺省 : 
无 
使用说明 : 
在同一个模式下面，匹配的规则是合集，最多配置4个，而所有模式下面规则合集不能超过64个。在日志文件策略模式下没有配置match的时候意味着不记录任何日志。 
范例 : 
指定日志过滤规则，处理告警日志中包含“bgp”串的记录ZXROSNG(config)#logging file alarmlogZXROSNG(config-log-file-alarmlog)#match alarmlog substring bgp
相关命令 : 
无 
## match 

match 
命令功能 : 
设置过滤规则，规则包括日志大类和子串，符合过滤规则的得到处理 
命令模式 : 
 日志SNMP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
match 
 cmdlog 
 [[exclude 
] substring 
 ＜substring 
＞]
no match 
 cmdlog 
 [substring 
 ＜substring 
＞]
				
命令参数解释 : 
参数|描述
---|---
cmdlog|命令日志
exclude|标识子串类型
＜substring＞|子串，1-40个字符
缺省 : 
无 
使用说明 : 
在同一个模式下面，匹配的规则是合集，最多配置4个，而所有模式下面规则合集不能超过64个。在日志snmp 策略模式只能匹配cmdlog类型，没有配置match的时候意味着不发送任何trap。日志snmp trap策略模式是默认加载的，且不允许删除。只要用户没有手动修改snmp策略下的配置，默认是匹配cmdlog的。 
范例 : 
指定日志过滤规则，处理命令日志中包含“bgp”串的记录ZXROSNG(config)#logging snmpZXROSNG(config-log-file-snmp)#match cmdlog substring bgp
相关命令 : 
无 
## name 

name 
命令功能 : 
创建日志文件策略后，设置文件名，对应的文件夹是由系统规划。文件名由四部分组成：前缀、时间信息、序号和后缀。前缀、时间信息和后缀由用户设置，序号为系统自动附加。 
命令模式 : 
 日志文件策略模式  
命令默认权限级别 : 
15 
命令格式 : 
name 
  ＜filename 
＞ [follow 
 {utc 
|local 
}] [suffix 
 ＜suffix 
＞]
no name 
命令参数解释 : 
参数|描述
---|---
＜filename＞|日志文件名前缀，1-30个字符，只能是字母和数字。
utc|时间为UTC时间
local|时间为本地时间，带时区、夏令时。
＜suffix＞|日志文件扩展名    1-9个字符，默认为”log”，不能以’.’开头，不能包含下划线’_’。
缺省 : 
无 
使用说明 : 
没有通过此命令定义文件名的时候不会将日志写入文件。 
范例 : 
范例设置策略的文件名前缀为criticalAlarm，后缀为bgpZXROSNG(config)#logging file alarmlogZXROSNG(config-log-file-alarmlog)#name criticalAlarm suffix bgp生成的文件名效果为类似如下：criticalAlarm_20120725110839_0.bgp
相关命令 : 
无 
## overflow mode 

overflow mode 
命令功能 : 
该命令在service日志文件默认策略模式和日志文件策略模式下执行，用于设置日志策略缓存满时对日志缓冲区的处理方式。 
命令模式 : 
 NETCONF日志文件默认策略模式,WEB日志文件默认策略模式,service日志文件默认策略模式,日志文件策略模式  
命令默认权限级别 : 
日志文件策略模式:15,WEB日志文件默认策略模式:15,service日志文件默认策略模式:15,NETCONF日志文件默认策略模式:15 
命令格式 : 
overflow mode 
  {clear 
|part-removed 
|cycle 
|drop 
}
no overflow mode 
命令参数解释 : 
参数|描述
---|---
clear|<取值规则>若设置为clear，则表示当日志缓冲区满时，系统自动将缓冲区中的所有日志进行清除。
part-removed|<取值规则>若设置为part-removed，则表示当日志缓冲区满时，系统将自动清除最早写入缓冲区的1/3的日志。
cycle|<取值规则>若设置为cycle，则表示当日志缓冲区满时，系统将删除缓冲区中最老的日志，然后把新日志放入缓冲区中。
drop|<取值规则>若设置为drop，则表示新产生的日志，不再进行处理，直接丢弃
缺省 : 
part-removed 
使用说明 : 
end和以前 fullend含义相同，是来了新日志后不进缓存直接写文件；drop是来了新的日志后，不进入缓存也不会写入文件；part-removed和以前fullcycle相同，是清空最老的三分之一内存；cycle是清空最老的部分日志，以保证新入的日志可以存放进去为标准，被覆盖的日志的记录大小是不固定的，有可能是一条，也有可能是多条。 
范例 : 
设置策略myPolicy日志缓存满后的清空方式为“清除已有的所有日志”，则执行如下命令：ZXROSNG(config)# logging file myPolicyZXROSNG(config-log-file- myPolicy)#overflow mode clear
相关命令 : 
buffer 
## overflow mode 

overflow mode 
命令功能 : 
该命令在alarm日志文件默认策略模式下执行，用于设置日志策略缓存满时对日志缓冲区的处理方式。 
命令模式 : 
 alarm日志文件默认策略模式  
命令默认权限级别 : 
15 
命令格式 : 
overflow mode 
  ＜clear-mode 
＞
no overflow mode 
命令参数解释 : 
参数|描述
---|---
＜clear-mode＞|清空方式：end：    若设置为end，则表示新产生的日志，不再进入缓冲区而是直接写入文件。clear：若设置为clear，则表示当日志缓冲区满时，系统自动将缓冲区中的所有日志进行清除。cycle：若设置为cycle，则表示当日志缓冲区满时，系统将删除缓冲区中最老的日志，然后把新日志放入缓冲区中。drop：    若设置为drop，则表示新产生的日志，不再进行处理，直接丢弃。part-removed：若设置为part-removed，则表示当日志缓冲区满时，系统将自动清除最早写入缓冲区的1/3的日志。
缺省 : 
part-removed 
使用说明 : 
end和以前 fullend含义相同，是来了新日志后不进缓存直接写文件；drop是来了新的日志后，不进入缓存也不会写入文件；part-removed和以前fullcycle相同，是清空最老的三分之一内存；cycle是清空最老的部分日志，以保证新入的日志可以存放进去为标准，被覆盖的日志的记录大小是不固定的，有可能是一条，也有可能是多条。 
范例 : 
设置策略myPolicy日志缓存满后的清空方式为“清除已有的所有日志”， 则执行如下命令：ZXROSNG(config)# logging file myPolicyZXROSNG(config-log-file- myPolicy)#overflow mode clear
相关命令 : 
buffer 
## performance threshold-alarm 

performance threshold-alarm 
命令功能 : 
设置性能越限告警上报开关。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
performance threshold-alarm 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开性能越限告警上报
disable|关闭性能越限告警上报
缺省 : 
功能默认$#251723786:0/关闭;1/打开#$ 
使用说明 : 
本命令控制性能管理模块性能越限告警是否上报，和业务上报的越限告警无关。即开关关闭，性能管理模块就不会上报性能越限告警，但是不影响业务上报的越限告警。 
范例 : 
打开性能越限告警上报：ZXROSNG(config)#perfmance threshold-alarm enable关闭性能越限告警上报：ZXROSNG(config)#perfmance threshold-alarm disable
相关命令 : 
logging console level
## show alarm class 

show alarm class 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于显示设备上定义的业务类型编码对应的英文名称。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show alarm class 
  [＜Service type ID 
＞] 
命令参数解释 : 
参数|描述
---|---
＜Service type ID＞|<作用>用于设置业务类型编码，可选，不设置时显示所有的业务类型。<取值范围>取值范围：1-65534
缺省 : 
无 
使用说明 : 
显示全部定义的业务类型时，按升序排列。 
范例 : 
显示全部定义的业务类型：ZXROSNG(config)# show alarm classClass Type     Description5             MS33            BOARD203           EthernetPort519           TCP521           IP           显示指定的业务类型：ZXROSNG(config)# show alarm class 5Class Type     Description 5             MS
相关命令 : 
无 
## show alarm level-change 

show alarm level-change 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于显示告警级别重定义的配置信息。执行该命令可查询被重义了告警级别的告警相关信息，包括告警码、告警默认级别以及修改后的级别。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show alarm level-change 
  [＜alarmcode 
＞] 
命令参数解释 : 
参数|描述
---|---
＜alarmcode＞|<作用>用于设置需要查询被重定义告警级别的告警码。该参数为可选参数，如果不设置，则显示所有告警级别被重定义的配置信息。<取值范围>取值范围：1~4294967294。 <默认值>默认值：无。
缺省 : 
无 
使用说明 : 
当用户使用alarm level change命令对告警级别进行重定义后，可通过本命令查询重定义后的告警级别。 
范例 : 
查询所有被重定义告警级别的配置信息，则执行如下命令：ZXROSNG#show alarm level-changeAlarmCode       Default-level       Current-level150101          warnings            emergencies150102          warnings            critical
相关命令 : 
无 
## show alarm 

show alarm 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于查看设备上的告警信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show alarm 
  {current 
 [{one-line 
|brief 
}]|history 
 [one-line 
]|notification 
 [one-line 
]} [{code 
 ＜alarmcode 
＞|flowid 
 ＜flowid 
＞|{[typeid 
 ＜typeid 
＞],[start-time 
 ＜date 
＞ ＜time 
＞],[end-time 
 ＜date 
＞ ＜time 
＞],[level 
 ＜alarmlevel 
＞],[sort 
 resources-full 
]}}] [{latest-first 
|earliest-first 
}] 
命令参数解释 : 
参数|描述
---|---
current|<作用>用于设置要查询的告警信息为当前告警。
one-line|<作用>用于设置以不换行形式显示当前告警，历史告警和通知。
brief|<作用>用于设置以表格形式精简当前告警。
history|<作用>用于设置要查询的告警信息为历史告警。
one-line|<作用>用于设置以不换行形式显示当前告警，历史告警和通知。
notification|<作用>用于设置要查询的告警信息为通知。
one-line|<作用>用于设置以不换行形式显示当前告警，历史告警和通知。
code|<作用>用于设置要查询的告警信息的告警码。
＜alarmcode＞|<作用>用于设置要查询的告警信息的告警码。<取值范围>取值范围：1-4294967295。
flowid|<作用>用于设置要查询的告警信息的流水号。
＜flowid＞|<作用>用于设置要查询的告警信息的具体流水号。当前告警流水号可以通过show alarm current命令查询。历史告警流水号可以通过show alarm history命令查询。
＜typeid＞|<作用>用于设置要查询的告警信息的告警类型。
＜date＞|<作用>用于设置要查询的告警信息的结束日期。
＜time＞|<作用>用于设置要查询的告警信息的结束时间。
＜date＞|<作用>用于设置要查询的告警信息的结束日期。
＜time＞|<作用>用于设置要查询的告警信息的结束时间。
＜alarmlevel＞|<作用>用于设置要查询的告警信息的告警级别。•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7•    debugging：告警级别8
resources-full|<作用>用于要查询的资源满类的告警信息。
latest-first|<取值规则>若设置为latest-first，则表示最后产生的告警显示在查询结果的最前面。
earliest-first|<取值规则>若设置为latest-first，则表示最后产生的告警显示在查询结果的最前面。
缺省 : 
无 
使用说明 : 
该命令显示的是当前告警、历史告警和通知，显示当前告警最大记录数为5000条、历史告警最大记录数为10000条、通知最大记录数为5000条。 
范例 : 
显示当前告警中告警码是 150102的告警。ZXROSNG#show alarm current code 150102An alarm 150102 ID 2 level 5 occurred at 07:31:08 10-24-2012 sent by ZXR10 MPU-0/20/0%IP% Interface v6 status  The interface(index=3,name='smartgroup9') v6 status turned into protocol DOWNZXROSNG#以表格形式精简显示当前告警中告警码是150101的告警:ZXROSNG#show alarm current brief code 150101ID  Code   Level    Time       Module  Info2   150101 warnings 10-24-2012 IP      Interface v6 status  The interface(in                    07:31:08           dex=3,name='smartgroup9') v6 status t                                       urned into protocol DOWN域信息描述表:域        描述ID        告警流水号。Code    告警码。Level    告警级别。Time    告警产生时间。Module    模块名。Info    告警描述信息。以不换行形式显示当前告警中告警码是150102的告警:ZXROSNG#show alarm current one-line code 150102An alarm 150102 ID 2 level 5 occurred at 07:31:08 10-24-2012 sent by ZXR10 MPU-0/20/0%IP% Interface v6 status  The interface(index=3,name='smartgroup9') v6 status turned into protocol DOWN以告警种类为过滤条件，显示资源满告警：ZXROSNG#show alarm current sort resources-full An alarm 150101 ID 19 level 5 occurred at 17:41:19 08-23-2017 sent by ZXR10 MPU-0/20/0%IP% Interface status  The interface(index=26,name='loopback2') turned into protocol DOWNZXROSNG#show alarm history sort resources-full An alarm 150101 ID 13 level 5 occurred at 17:36:34 08-23-2017, cleared at 17:36:38 08-23-2017 sent by ZXR10 MPU-0/20/0%IP% Interface status  The interface(index=25,name='loopback1') turned into protocol DOWNZXROSNG#show alarm notification sort resources-full A notification 150101 ID 17 level 5 occurred at 17:41:02 08-23-2017 sent by ZXR10 MPU-0/20/0%IP% Interface status  The interface(index=26,name='loopback2') turned into protocol UP
相关命令 : 
show logging alarm 
## show logfile 

show logfile 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于显示保存在日志缓冲区中的命令日志。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show logfile 
  [brief 
] [{[username 
 ＜username 
＞],[start-time 
 ＜date 
＞ ＜time 
＞],[end-time 
 ＜date 
＞ ＜time 
＞],[vtyno 
 ＜link-number 
＞],[ipaddress 
 {＜ipv4 
＞|＜ipv6 
＞}]}] 
命令参数解释 : 
参数|描述
---|---
brief|<作用>用于设置命令日志按照定制格式显示简要信息，分为三行，分别为Time,User和CMDLine。
＜username＞|<作用>用于设置要显示的命令日志的登录用户名，长度为1~65个字符。
＜date＞|<作用>用于设置要显示的命令日志产生的结束日期，格式为mm-dd-yyyy。<取值范围>范围  01-01-2001 ~ 12-31-2037。
＜time＞|<作用>用于设置要显示的命令日志产生的结束时间，格式为hh:mm:ss。 <取值范围>范围  00:00:00 ~  23:59:59。
＜date＞|<作用>用于设置要显示的命令日志产生的结束日期，格式为mm-dd-yyyy。<取值范围>范围  01-01-2001 ~ 12-31-2037。
＜time＞|<作用>用于设置要显示的命令日志产生的结束时间，格式为hh:mm:ss。 <取值范围>范围  00:00:00 ~  23:59:59。
＜link-number＞|<作用>用于设置要显示的命令日志的登录的终端号。<取值范围>取值范围:1~$#17039360#$
＜ipv4＞|<作用>用于设置要显示的命令日志的登录时使用的主机的IPv4地址。
＜ipv6＞|<作用>用于设置要显示的命令日志的登录时使用的主机的IPv6地址。
缺省 : 
显示命令日志缓存中的所有记录。
使用说明 : 
该命令显示的是命令日志缓冲区中的内容，因为命令日志缓冲区大小有限，所以要查看更多的命令日志信息，请查看命令日志文件。 
范例 : 
查询保存在日志缓冲区中的命令日志，则执行如下命令：ZXROSNG(config)#show logfile StartTime: 09:22:36 06-07-2013  EndTime: 09:22:38 06-07-2013  FlowID: 3  VtyNo: con0  UserName:   UserLevel: 1  IP:   HostName: ZXR10  Result: success  CMDLevel: NA  CMDLine: /--- console update privilege success ---/StartTime: 09:22:36 06-07-2013  EndTime: 09:22:36 06-07-2013  FlowID: 2  VtyNo: con0  UserName:   UserLevel: 1  IP:   HostName: ZXR10  Result: success  CMDLevel: 0  CMDLine: en 18StartTime: 09:22:08 06-07-2013  EndTime: 09:22:08 06-07-2013  FlowID: 1  VtyNo: con0  UserName:   UserLevel: 1  IP:   HostName: ZXR10  Result: success  CMDLevel: NA  CMDLine: /--- console user log in ---/$#251723801#$：取值0，对应显示为：StartTime: 02:22:30 01-30-2038  EndTime: 02:22:30 01-30-2038  FlowID: 45  VtyNo: vty0  UserName: zte  UserLevel: 15  IP: 192.168.100.1  HostName: ZXR10  Result: fail  CMDLevel: 15  CMDLine: multi-user configure取值1，执行结果失败的命令日志增加Return，对应显示为：StartTime: 02:22:30 01-30-2038  EndTime: 02:22:30 01-30-2038  FlowID: 45  VtyNo: vty0  UserName: zte  UserLevel: 15  IP: 192.168.100.1  HostName: ZXR10  Result: fail  CMDLevel: 15  CMDLine: multi-user configure  Return：%Error 140153: An invalid or ambiguous command node.如果只显示简要信息，则执行show logfile brief：ZXROSNG(config)#show logfile briefTime   : 14:47:57.436 03-20-2020User   : zte, vty0, 10.40.166.170CMDLine: logging offTime   : 14:47:48.565 03-20-2020User   : zte, vty0, 10.40.166.170CMDLine: conf tTime   : 14:47:07.990 03-20-2020User   : --, con0, --CMDLine: /--- console user log in ---/域信息描述表：域                描述Time       日志上报的时间戳，本地时间，精确到毫秒User       执行命令的用户，终端号和IP地址，无用户名或者IP的时候用”--”代替CMDLine   执行的命令串
相关命令 : 
无
## show logging alarm 

show logging alarm 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于显示告警日志缓冲区中的告警信息记录。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show logging alarm 
  [{[typeid 
 ＜typeid 
＞],[start-time 
 ＜date 
＞ ＜time 
＞],[end-time 
 ＜date 
＞ ＜time 
＞],[level 
 ＜alarmlevel 
＞],[code 
 ＜alarmcode 
＞]}] 
命令参数解释 : 
参数|描述
---|---
＜typeid＞|<作用>用于设置要显示的告警信息的告警类型。
＜date＞|<作用>用于设置要显示的告警产生的终止日期，格式为mm-dd-yyyy。<取值范围>取值范围：01-01-2001 ~ 12-31-2037。
＜time＞|<作用>用于设置要显示的告警产生的终止时间，格式为hh:mm:ss。<取值范围>取值范围：00:00:00 ~  23:59:59。
＜date＞|<作用>用于设置要显示的告警产生的终止日期，格式为mm-dd-yyyy。<取值范围>取值范围：01-01-2001 ~ 12-31-2037。
＜time＞|<作用>用于设置要显示的告警产生的终止时间，格式为hh:mm:ss。<取值范围>取值范围：00:00:00 ~  23:59:59。
＜alarmlevel＞|<作用>用于设置要显示的告警消息的严重级别。•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7•    debugging：告警级别8
＜alarmcode＞|<作用>要显示的告警消息的告警码<取值范围>1-4294967294
缺省 : 
无 
使用说明 : 
该命令显示的是告警日志缓冲区中的告警日志。告警日志缓冲区中仅保存最新的告警日志，当系统产生的告警日志大小超过logging buffer命令设置的阈值时，新产生的日志将会按告警生成的时间顺序将最先生成的告警覆盖掉。如果需要查看更多的告警数据，请查看告警日志文件或者使用show alarm 命令查询。 
范例 : 
查看告警日志缓冲区的告警信息，则执行如下命令：ZXROSNG#show logging alarm An alarm 150101 ID 1 level 5 cleared at 07:34:13 05-13-2011 sent by ZXR10 PFU-0/20/0%IP% Interface status  The interface(index=3,name='loopback1') turned into UPAn alarm 150101 ID 1 level 5 occurred at 07:34:09 05-13-2011 sent by ZXR10 PFU-0/20/0%IP% Interface status  The interface(index=3,name='loopback1') turned into DOWN
相关命令 : 
无 
## show logging buffer 

show logging buffer 
命令功能 : 
显示日志策略缓冲区中的信息记录 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show logging buffer 
  ＜policy-name 
＞ [{[start-time 
 ＜date 
＞ ＜time 
＞],[end-time 
 ＜date 
＞ ＜time 
＞],[{latest-first 
|earliest-first 
}],[from 
 ＜from 
＞],[＜count 
＞],[{include 
|exclude 
} ＜string 
＞]}] 
命令参数解释 : 
参数|描述
---|---
＜policy-name＞|要查询的日志策略名，支持1-32个字符
＜date＞|开始时间的日期
＜time＞|开始时间的时刻
＜date＞|开始时间的日期
＜time＞|开始时间的时刻
latest-first|最近产生的日志排在最前面显示
earliest-first|最老产生的日志排在最前面显示
＜from＞|从第几条开始
＜count＞|显示的条目数
include|包含
exclude|不包含
＜string＞|子串，支持1-512个字符
缺省 : 
无 
使用说明 : 
该策略名需要是已配置的自定义策略名或者三种默认策略的策略名 
范例 : 
(1)不配置下发logging header命令，show logging buffer命令回显为老的头信息ZXROSNG# ZXROSNG(config)#show logging buffer mypolicyLog acceptance:on Log matched: 9Log in buffer: 9Buffer occupied: 0.71% Log file path: /sysdisk0/usrcmd_log/ $#251723801#$：取值0，对应显示为：LogID:70020 2013-11-26 19:31:46.639 Class:Cmd  [StartTime: 02:22:30 01-30-2038  EndTime: 02:22:30 01-30-2038  FlowID: 45  VtyNo: vty0  UserName: zte  UserLevel: 15  IP: 192.168.100.1  HostName: ZXR10  Result: fail  CMDLevel: 15  CMDLine: multi-user configure  取值1，执行结果失败的命令日志增加Return，对应显示为：LogID:70020 2013-11-26 19:31:46.639 Class:Cmd  [StartTime: 02:22:30 01-30-2038  EndTime: 02:22:30 01-30-2038  FlowID: 45  VtyNo: vty0  UserName: zte  UserLevel: 15  IP: 192.168.100.1  HostName: ZXR10  Result: fail  CMDLevel: 15  CMDLine: multi-user configure  Return：%Error 140153: An invalid or ambiguous command node.]LogID:70019 2013-11-26 19:30:46.701 Class:Service  [19:31:46 11-26-2013  Module:OSPFV2  Content:Intf 10.176.143.243 Down->Loopback]LogID:70018 2013-11-26 19:28:37.672 Class:Alarm  [An alarm 150101 ID 9 level 5 cleared at 19:35:35 11-26-2013 sent by ZXR10 MPU-0/20/0%IP% Interface status  The interface(index=4,name='loopback1') turned into protocol UP]域信息描述表：域    描述Log acceptance    表示策略的开关状态Log matched    表示匹配此策略的日志个数，记入buffer的日志数+丢弃数Log in buffer   表示buffer中日志的条目数Buffer occupied    日志buffer占用的百分比Log file path    日志记录的路径LogID    流水号，唯一标识一条日志的整数。系统复位后重新编号2013-10-28 08:32:07.907    时间戳，精确到毫秒Class    日志类型，目前是Cmd、Alarm、Service三种类型[……]    中括号里面的是具体的日志信息(2)配置logging header后，show logging buffer命令回显带新的公共头信息ZXROSNG(config)#logging headerZXROSNG(config)#show logging buffer almlog……[6/2020-02-28 20:10:41.838/01/ALARM/3] An alarm 350201 ID 4 level 3 cleared at 20:10:35 02-28-2020 sent by ZXR10 MPU-0/20/0 %SNMP% SNMP  SNMPv1 function succeed to start…………………………………………………………新的头信息“[6/2020-02-28 20:10:41.838/01/ALARM/3] ”中每个字段含义如下：域信息描述表：域                          描述流水号    日志条目的顺序号，设备重新启动时，流水号归零。流水号是按照日志大类独立分配的时间戳    信息输出的时间，精确到毫秒日志格式版本号  定义日志格式的版本，占固定2位，从“01”版本开始。在日志系统代码中定义，日志格式有变更时，格式评审归档后日志分配日志格式版本号日志大类  日志大类目前支持：CMD，ALARM，SERVICE，LI，WEB，SNMP，NETCONF日志级别  目前定义1-8级（emergencies、alerts、critical、errors、warnings、notifications、informational、debugging），1级为最高级。当日志上报未填写级别，日志通道设定为默认值6（notifications）
相关命令 : 
(1)show logfile和show logging buffer cmdlog的功能基本一致，show logging alarm和show logging buffer almlog的功能基本一致，show logging service和show logging buffer srvlog的功能基本一致，都能显示出缓冲区中的日志信息，只是格式组织上不太相同。(2)执行logging header配置下，show logging buffer回显为新的公共头信息，但不影响show logfile,show logging alarm和show logging service的回显。执行no logging header配置，show logging buffer回显为老的头信息。
## show logging configuration 

show logging configuration 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于显示告警和日志功能的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show logging configuration 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
本命令只能查询到部分告警配置信息，如果需要查看全部的告警配置信息，请使用show running-config alarm命令查看。 
范例 : 
查询告警和日志功能的配置信息，则执行如下命令：ZXROSNG#show logging configuration alarm heartbeat-period 0 snmpalarm heartbeat-period 0 syslogalarm heartbeat-period 0 ftpalarm heartbeat-period 0 consolealarm heartbeat-period 0 alllogging onlogging console notificationslogging trap-enable debugginglogging timestamps datetime localtimelogging ftp debugging vrf mng 10.42.184.135 zte encrypted ****** zxralarm.loglogging filesavetime everyday 01:00:00 2.2.2.2 root encrypted ****** zxralarm.loglogging nat ftp 1.1.1.1 root encrypted ******logging nat buffer 1000logging nat file-size 50 file-num 300logging nat description-type basemaclogging nat zip onlogging nat terminal locallogging portal ftp 2.2.2.2 root encrypted ******syslog level notificationssyslog-server facility local0
相关命令 : 
无 
## show logging service 

show logging service 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于显示日志缓冲区中的业务日志信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show logging service 
  [type 
 ＜service-type 
＞] 
命令参数解释 : 
参数|描述
---|---
＜service-type＞|<作用>用于设置要查询的业务日志所属的业务类型。该参数为可选参数，如果不设置则显示所有业务类型的日志信息。
缺省 : 
该命令显示的是日志缓冲区中的业务日志信息，如果需要了解更多的业务日志信息，请查看业务日志文件。 
使用说明 : 
无 
范例 : 
查看业务日志信息，则执行如下命令：ZXROSNG#show logging service08:58:35 02-28-2012  Module:OSPFV2  Content:Intf 10.176.143.243 Down->Loopback
相关命令 : 
无 
## syslog level 

syslog level 
命令功能 : 
该命令在全局配置模式下执行，用于设置告警日志上报到syslog服务器的告警级别（只有高于或等于该级别的告警才会上报）。上报到syslog服务器的告警信息的默认级别为6级。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
syslog level 
  ＜alarmlevel 
＞
no syslog level 
命令参数解释 : 
参数|描述
---|---
＜alarmlevel＞|<作用>用于设置需要上报到syslog服务器的告警消息的级别（只有高于或等于该级别的告警才会上报）。<取值范围>取值范围：emergencies、alerts、critical、errors、warnings、notifications、informational、debugging。<取值含义>•    emergencies：告警级别1•    alerts：告警级别2•    critical：告警级别3•    errors：告警级别4•    warnings：告警级别5•    notifications：告警级别6•    informational：告警级别7•    debugging：告警级别8<默认值>默认值：notifications。
缺省 : 
notifications 
使用说明 : 
无 
范例 : 
设置告警日志上报到syslog服务器的告警级别为warnings，则执行如下命令：ZXROSNG(config)#syslog level warnings
相关命令 : 
无 
## syslog-server facility 

syslog-server facility 
命令功能 : 
该命令在全局配置模式下执行，用于设置syslog的facility属性，标识syslog报文的来源。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
syslog-server facility 
  ＜type 
＞
no syslog-server facility 
命令参数解释 : 
参数|描述
---|---
＜type＞|<作用>Syslog的facility，表示syslog报文的来源。<取值范围>取值范围：参见syslog协议rfc3164中的4.1.1节。<默认值>默认值：local0。
缺省 : 
local0 
使用说明 : 
syslog的facility属性的默认值为local0。 
范例 : 
设置syslog的facility为news，则执行如下命令：ZXROSNG(config)#syslog-server facility news
相关命令 : 
无 
## syslog-server host 

syslog-server host 
命令功能 : 
该命令在全局配置模式下执行，用于设置syslog服务器的参数，包括syslog server的IP地址、源端口号和目的端口号，以及发送的日志类型。配置成功后，当系统产生在该命令中已配置的类型的日志时，就上传到syslog服务器上。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
syslog-server host 
  [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜name 
＞]|＜ipv4addr 
＞} [fport 
 ＜fport 
＞] [lport 
 {＜lport 
＞|＜lport 
＞}] [source 
 {＜ipv4addr 
＞|＜ipv6addr 
＞}] [{[alarmlog 
],[cmdlog 
],[debugmsg 
],[servicelog 
],[braslog 
],[natlog 
],[netconflog 
],[snmplog 
],[weblog 
]}]
no syslog-server host 
  [vrf 
 ＜vrfname 
＞] {＜ipv6addr 
＞ [interface 
 ＜name 
＞]|＜ipv4addr 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜vrfname＞|VPN名称
＜ipv6addr＞|IPV6地址
＜name＞|接口名
＜ipv4addr＞|IPV4地址
＜fport＞|<作用>用于设置远端端口号。<取值范围>取值范围：1~65535。<默认值>默认值：514。
＜lport＞|<作用>用于设置本地端口号。<取值范围>取值范围：1024~65535。 <默认值>默认值：无。
＜lport＞|<作用>用于设置本地端口号。<取值范围>取值范围：1024~65535。 <默认值>默认值：无。
＜ipv4addr＞|IPV4地址
＜ipv6addr＞|IPV6地址
alarmlog|<取值规则>若设置告警日志，则将告警日志发送给syslog服务器。告警日志级别等于或高于syslog level命令设置的级别时才上报到syslog。
cmdlog|<取值规则>若设置命令日志，则将命令日志发送给syslog服务器。
debugmsg|<取值规则>若设置调试日志，则将调试日志发送给syslog服务器。
servicelog|<取值规则>若设置业务日志，则将业务日志发送给syslog服务器。
braslog|<取值规则>若设置BRAS日志，则将BRAS日志发送给syslog服务器。
natlog|<取值规则>若设置CGN日志，则将CGN日志发送给syslog服务器。
netconflog|<取值规则>若设置NETCONF日志,将NETCONF日志上传syslog服务器
snmplog|<取值规则>若设置SNMP日志,将SNMP日志上传syslog服务器
weblog|<取值规则>若设置WEB日志,将WEB日志上传syslog服务器
缺省 : 
<fport > :514<lport > :514
使用说明 : 
1 syslog服务器最多可配置10个。如果配置多条syslog服务器记录时，系统会检查相同syslog服务器地址的本地端口是否存在冲突，如果存在冲突，则系统会提示用户要修改端口。2、Fport远端端口号必须与syslog服务器设置的端口号一致。3、当配置了source之后，发包的时候源地址填写配置的地址，没配置的时候使用全局配置syslog-server source配置的地址。4、配置的IPv4和IPv6地址都不支持非法地址；
范例 : 
设置syslog server的IP地址为192.168.0.1，远端端口号为1601，本地端口号为1601，则执行如下命令：ZXROSNG(config)# syslog-server host 192.168.0.1 fport 1601 lport 1601
相关命令 : 
syslog-server source 
## syslog-server source 

syslog-server source 
命令功能 : 
该命令在全局配置模式下执行，用于配置设备发送到syslog服务器上的syslog报文的源地址。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
syslog-server source 
  {ipv6 
 ＜ipv6 
＞|ipv4 
 ＜ipv4 
＞|interface 
 ＜interface-name 
＞}
no syslog-server source 
  {ipv6 
|ipv4 
|interface 
}
				
命令参数解释 : 
参数|描述
---|---
ipv6|IPv6地址类型
＜ipv6＞|<作用>用于设置syslog报文的源地址（IPv6）。<默认值>默认值：无
ipv4|IPv4地址类型
＜ipv4＞|<作用>用于设置syslog报文的源地址（IPv4）。<默认值>默认值：无
interface|接口地址类型
＜interface-name＞|<作用>用于设置syslog报文的源地址（接口）。<默认值>默认值：无
缺省 : 
无 
使用说明 : 
该配置命令可以配置IPv4和IPv6以及接口的源地址，配置的地址填写在syslog报文的源地址，标识报文的来源。 
范例 : 
设置syslog报文的源地址为IPv4 地址10.40.40.34，则执行如下命令：ZXROSNG(config)#syslog-server source ipv4 10.40.40.34
相关命令 : 
无 
## terminal monitor 

terminal monitor 
命令功能 : 
本命令在特权模式下执行，将信息输出到当前终端界面。通过no命令关闭当前终端的信息输出。该命令只作用于当前终端，对其他终端无影响。默认情况下当前终端信息输出功能是关闭的。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
terminal monitor 
  [{alarm 
|debug 
}]
no terminal monitor 
  [{alarm 
|debug 
}]
				
命令参数解释 : 
参数|描述
---|---
alarm|表示打开或关闭alarm信息在当前终端显示
debug|表示打开或关闭debug信息在当前终端显示
缺省 : 
无 
使用说明 : 
执行terminal monitor，会同时打开所有需要在当前终端显示的信息的输出；单只执行terminal monitor alarm，只打开alarm信息在当前终端的输出，单只执行terminal monitor debug，只打开debug信息在当前终端的输出。打开当前终端debug信息输出可能会导致大量数据呈现在终端界面，无法使用no命令关闭终端输出，可以通过快捷键CTRL+D关闭所有的debug调试开关后再通过no命令关闭当前终端debug 输出。
范例 : 
1、首先打开arp模块所有debug调试开关，再打开当前终端的debug信息输出，界面呈现大量debug信息： ZXROSNG#debug arp allARP all debugging is onZXROSNG#terminal monitor ZXROSNG#A notification 250316 ID 5489 level 6 occurred at 16:14:04 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel125 create fail ,reason:Cspf failA notification 250316 ID 5490 level 6 occurred at 16:14:04 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel126 create fail ,reason:Cspf failA notification 250316 ID 5491 level 6 occurred at 16:14:04 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel127 create fail ,reason:Cspf failA notification 250316 ID 5492 level 6 occurred at 16:14:04 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel128 create fail ,reason:Cspf failA notification 250316 ID 5493 level 6 occurred at 16:14:04 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel129 create fail ,reason:Cspf failZXR10 MPU-0/20/0 2019-11-16 15:21:06 (serLogStru.strLogDescrip, MAX_SERVICE_LOG_DESCRIP_LEN-1, abcd_%d, i++);Oam_Alarm_ReportDebugMsg(&dbgMsg) with [n];……通过no命令关闭当前终端debug信息输出：ZXROSNG#terminal monitor ZXROSNG#
……A notification 250316 ID 5607 level 6 occurred at 16:15:23 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel9 create fail ,reason:Cspf failA notification 250316 ID 5608 level 6 occurred at 16:15:23 01-19-2014 sent by ZXR10 MPU-0/20/0%RSVP% Tunnel create fail.  Tunnel10 create fail ,reason:Cspf failZXR10 MPU-0/20/0 2019-11-16 15:21:06 (serLogStru.strLogDescrip, MAX_SERVICE_LOG_DESCRIP_LEN-1, abcd_%d, i++);Oam_Alarm_ReportDebugMsg(&dbgMsg) with [n];no terminal moZXROSNG#no terminal monitor ZXROSNG#
2、打开alarm信息在当前终端输出ZXROSNG#terminal monitor alarmZXROSNG#
An alarm 150101 ID 6 level 5 occurred at 10:59:08 11-16-2019 sent by ZXR10 MPU-0/20/0%IP% Interface status.  The interface(index=7,name='loopback1') turned into protocol DOWN.通过no命令关闭当前终端alarm信息输出：ZXROSNG#terminal monitor alarmZXROSNG#
An alarm 150101 ID 6 level 5 occurred at 10:59:08 11-16-2019 sent by ZXR10 MPU-0/20/0%IP% Interface status.  The interface(index=7,name='loopback1') turned into protocol DOWN.ZXROSNG#no terminal monitor alarmZXROSNG#
3、打开debug信息在当前终端输出ZXROSNG#terminal monitor debugZXROSNG#
ZXR10 MPU-0/20/0 2019-11-16 15:21:06 (serLogStru.strLogDescrip, MAX_SERVICE_LOG_DESCRIP_LEN-1, abcd_%d, i++);Oam_Alarm_ReportDebugMsg(&dbgMsg) with [n];通过no命令关闭当前终端debug信息在当前终端输出：ZXROSNG#terminal monitor debugZXROSNG#
ZXR10 MPU-0/20/0 2019-11-16 15:21:06 (serLogStru.strLogDescrip, MAX_SERVICE_LOG_DESCRIP_LEN-1, abcd_%d, i++);Oam_Alarm_ReportDebugMsg(&dbgMsg) with [n];ZXROSNG#no terminal monitor debugZXROSNG#
相关命令 : 
无 
## writelog 

writelog 
命令功能 : 
该命令在特权模式下执行，用于将日志缓冲区中的日志信息写入到日志文件中。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
writelog 
  ＜log-type 
＞
命令参数解释 : 
参数|描述
---|---
＜log-type＞|<作用>用于指定日志文件的类型。<取值范围>取值范围：cmdlog、alarmlog、natlog、servicelog、braslog、portallog。<取值含义>•    cmdlog：命令日志•    alarmlog：告警日志•    natlog：nat日志•    servicelog：业务日志•    braslog：bras日志•    portallog：portal日志<默认值>默认值：无。
缺省 : 
无 
使用说明 : 
执行该命令会触发立即写日志文件的操作。 
范例 : 
将告警日志缓冲区中的内容写入到文件中，则执行如下命令：ZXROSNG#writelog alarmlog
相关命令 : 
无 
# 检测配置命令 
## clear ip traffic 

clear ip traffic 
命令功能 : 
该命令工作于特权模式，用于清除IP、ICMP、TCP和UDP层的收发以及异常计数。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip traffic 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果用户不需要之前的统计信息，可以用此命令清除。清除之后各统计项从0开始重新计数。 
范例 : 
ZXROSNG#clear ip traffic ZXROSNG#show ip traffic IP statistics:  Rcvd: 0 total, 0 local destination        format errors      checksum errors      bad hop count        0                  0                    0                                 unknown protocol        0   Frags:reassembled        timeouts          couldn't reassemble        0                  0                 0                            fragmented         couldn't fragment        0                  0                   Bcast:received           sent        0                  0                   Sent: generated          forwarded         encapsulation failed    no route        0                  0                 0                       0ICMP statistics:  Rcvd: 0 total        format errors      redirects         unreachable      echo        0                  0                 0                0        echo reply         mask requests     mask replies     quench        0                  0                 0                0        timestamp request  timestamp reply   time exceeded    parameter problem        0                  0                 0                0                            Sent: 0 total        format errors      redirects         unreachable      echo        0                  0                 0                0        echo reply         mask requests     mask replies     quench        0                  0                 0                0        timestamp request  timestamp reply   time exceeded    parameter problem        0                  0                 0                0                UDP statistics:  Rcvd: 0 total, 0 checksum errors, 0 no port  Sent: 0 totalTCP statistics:  Rcvd: 0 total, 0 checksum errors  Sent: 0 total
相关命令 : 
show ip traffic 
## control-protocol 

control-protocol 
命令功能 : 
按照协议设置全局的dscp、precedence和8021p 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
control-protocol 
  {＜protocol 
＞ {[exp 
 ＜EXP value 
＞],[8021p 
 ＜802.1p value 
＞],[{dscp 
 ＜dscp value 
＞|precedence 
 ＜precedence value 
＞}]}|{isis 
|mpls-oam 
|arp 
} 8021p 
 ＜802.1p value 
＞}
no control-protocol 
  {{isis 
|mpls-oam 
|arp 
} 8021p 
|＜protocol 
＞ {exp 
|8021p 
|dscp 
|precedence 
}}
				
命令参数解释 : 
参数|描述
---|---
＜protocol＞|协议字段，包括bgp、ospf、rip、ldp、rsvp、snmp、ftp、nd、ntp、igmp、dhcp、radius、tacacs+、ssh、telnet、openflow、hagp、http
＜EXP value＞|设置的exp值，可配范围0-7
＜802.1p value＞|设置的8021P值，可配范围为0-7.
＜dscp value＞|设置的DSCP值，可配范围为0-63.
＜precedence value＞|设置的precedence值，可配范围为0-7.
isis|ISIS协议
mpls-oam|MPLS OAM协议
arp|ARP协议
＜802.1p value＞|设置的8021P值，可配范围为0-7.
No参数|描述
---|---
8021p|8021P配置值
exp|EXP配置值
8021p|8021p配置值
dscp|DSCP值
precedence|precedence值
缺省 : 
各协议没有设置全局的DSCP值、precedence值以及8021p值。 
使用说明 : 
1. 若应用没有指定IP优先级，发包时IP报文封装TOS使用该协议配置的全局DSCP值或者precedence值。2. 三层及以上协议配置TOS时，dscp和precedence进行二选一的配置。ND和MLD等只支持IPv6的协议，不允许配置precedence。3.二层协议，如isis、mpls oam和arp，只支持配置8021P。   三层及以上协议，可以配置dscp或者precedence值，也可以配置8021P和exp。4. 如果协议没有配置全局的二层优先级（8021P或者exp）,发包时二层优先级从IP优先级继承，取IP优先级的高3bit。
范例 : 
ZXROSNG(config)#control-protocol bgp dscp 34 8021p 3 
相关命令 : 
无 
## debug ip icmp all 

debug ip icmp all 
命令功能 : 
打开所有有关ICMP协议debug功能开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip icmp all 
 
no debug ip icmp all 
命令参数解释 : 
					无
				 
缺省 : 
关闭该调试功能 
使用说明 : 
无 
范例 : 
ZXROSNG#debug ip icmp all All ICMP debugging has been turned onZXROSNG#show debug icmpICMP:  ICMP packet debugging is on   ICMP packet detail debugging is onZXROSNG#no debug ip icmp all All ICMP debugging has been turned off
相关命令 : 
terminal monitor    show debug icmp
## debug ip icmp detail 

debug ip icmp detail 
命令功能 : 
该命令工作于特权模式，用于开启ICMPv4报文发送与接收的详细信息的打印开关。该命令主要用于故障诊断，开启该开关后，可以查看本地所有ICMPv4报文收发的详细情况。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip icmp detail 
 
no debug ip icmp detail 
命令参数解释 : 
					无
				 
缺省 : 
关闭该调试功能 
使用说明 : 
该命令需要与terminal monitor命令同时使用，否则看不到相关打印信息。可以通过命令show debug icmp查看该打印开关是否开启。该打印开关默认为关闭，即不打印ICMPv4报文的收发信息。
范例 : 
ZXROSNG#debug ip icmp detail ICMP packet detail debugging is onZXROSNG#terminal monitorZXROSNG#ping 10.10.10.2ZXR10 MPU-0/20/0 2013-12-10 04:14:01  IP ICMP detail:sent type echo request, code   0, identification:1, sequence:1, src 10.10.10.1, dst 10.10.10.2, size   100.ZXR10 MPU-0/20/0 2013-12-10 04:14:01  IP ICMP detail:rcvd type echo reply, code   0, identification:1, sequence:1, src 10.10.10.2, dst 10.10.10.1, size   100.输出信息中的参数信息解释如下：参数名称           参数说明MPU-0/20/0         单板名称sent               发送rcvd               接收echo request       ICMP回显请求报文echo reply         ICMP回显应答报文identification     ICMP报文头中的标识符sequence           ICMP报文头中的序列号
相关命令 : 
terminal monitorshow debug icmp
## debug ip icmp packet 

debug ip icmp packet 
命令功能 : 
打开ICMP协议的debug功能，显示ICMP协议处理的调试信息，显示路由器是否在发送ICMP报文，以及是否在接受ICMP报文。使用no命令关闭ICMP协议的debug功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip icmp packet 
  [{[source 
 ＜src-ip 
＞],[destination 
 ＜dst-ip 
＞]}]
no debug ip icmp packet 
命令参数解释 : 
参数|描述
---|---
＜src-ip＞|ip源地址
＜dst-ip＞|ip目的地址
缺省 : 
关闭该调试功能 
使用说明 : 
ip地址全0为通配地址：参数src-ip配置全0时候，不进行源地址过滤。参数dst-ip配置全0时候，不进行目的地址过滤。
范例 : 
ZXROSNG#debug ip icmp packet ICMP packet debugging is onZXROSNG#debug ip icmp packet source 1.1.1.1ICMP packet debugging is on for source address 1.1.1.1       ZXROSNG#debug ip icmp packet destination 1.1.1.2ICMP packet debugging is on for destination address 1.1.1.2ZXROSNG#show debug icmpICMP:  ICMP packet debugging is on for destination address 1.1.1.2 ZXROSNG#ping 1.1.1.2sending 5,100-byte ICMP echo(es) to 1.1.1.2,timeout is 2 second(s).ZXR10 MPU-0/20/0 2013-3-19 06:37:18  IP ICMP:sent type echo request, code   0, src 1.1.1.1, dst 1.1.1.2, size   100!ZXR10 MPU-0/20/0 2013-3-19 06:37:18  IP ICMP:sent type echo request, code   0, src 1.1.1.1, dst 1.1.1.2, size   100!ZXR10 MPU-0/20/0 2013-3-19 06:37:18  IP ICMP:sent type echo request, code   0, src 1.1.1.1, dst 1.1.1.2, size   100!ZXR10 MPU-0/20/0 2013-3-19 06:37:18  IP ICMP:sent type echo request, code   0, src 1.1.1.1, dst 1.1.1.2, size   100!ZXR10 MPU-0/20/0 2013-3-19 06:37:18  IP ICMP:sent type echo request, code   0, src 1.1.1.1, dst 1.1.1.2, size   100
相关命令 : 
terminal monitorshow debug icmp
## debug ip interface 

debug ip interface 
命令功能 : 
该命令工作于特权模式，用于开启指定接口上IPv4报文发送与接收打印开关。该命令主要用于故障诊断，开启该开关后，可以查看该接口上IPv4报文的收发情况。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip interface 
  ＜interface-name 
＞
no debug ip interface 
  ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，字符类型，长度为1-32
缺省 : 
关闭该调试功能 
使用说明 : 
该命令需要与terminal monitor命令同时使用，否则看不到相关打印信息。可以通过命令show debug ip查看该打印开关是否开启。该打印开关默认为关闭，即不打印IPv4报文的收发信息。
范例 : 
ZXROSNG#debug ip interface gei-0/1/0/8IP interface debugging is onZXROSNG#terminal monitor ZXR10 MPU-0/20/0 2013-12-11 08:23:16  IP interface:gei-0/1/0/8 sent src 10.10.10.1,dst 10.10.10.2ZXR10 MPU-0/20/0 2013-12-11 08:23:16  IP interface:gei-0/1/0/8 rcvd src 10.10.10.2,dst 10.10.10.1输出信息中的参数信息解释如下：参数名称          参数说明MPU-0/20/0        单板名称interface         接口名称sent              发送rcvd              接收src               源IP地址dst               目的IP地址
相关命令 : 
terminal monitor 
## debug ip 

debug ip 
命令功能 : 
该命令工作于特权模式，用于开启IPv4报文发送与接收打印开关。该命令主要用于故障诊断，开启该开关后，可以查看所有本地IPv4报文的收发情况。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip 
  [packet 
 {[address 
 ＜ip-addr 
＞],[protocol 
 ＜protocol 
＞]}]
no debug ip 
命令参数解释 : 
参数|描述
---|---
＜ip-addr＞|指定IPv4地址（源地址或目的地址）
＜protocol＞|指定协议号，1-255
缺省 : 
关闭该调试功能 
使用说明 : 
该命令需要与terminal monitor命令同时使用，否则看不到相关打印信息。可以通过命令show debug ip查看该打印开关是否开启。该打印开关默认为关闭，即不打印IPv4报文的收发信息。由于该命令打印的是所有本地IPv4报文的收发情况，可能会打印大量的无关报文收发信息，建议使用debug ip interface命令只打印某一接口上的报文。
范例 : 
ZXROSNG#debug ipIP debugging is onZXROSNG#terminal monitor ZXR10 MPU-0/20/0 2013-12-11 08:19:23  IP:sent src 10.10.10.1,dst 10.10.10.2,dscp 0,length 100,id 11,protocol 1ZXR10 MPU-0/20/0 2013-12-11 08:19:23  IP:rcvd src 10.10.10.2,dst 10.10.10.1,dscp 0,length 100,id 11,protocol 1输出信息中的参数信息解释如下：参数名称       参数说明MPU-0/20/0     单板名称sent           发送rcvd           接收src            源IP地址dst            目的IP地址dscp           优先级length         报文长度id             报文ID号protocol       IP头后面的报文协议号
相关命令 : 
terminal monitorshow debug ip
## error packet ip record 

error packet ip record 
命令功能 : 
配置IPv4错误报文记录功能是否使能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
error packet ip record 
  {disable 
|enable 
}
命令参数解释 : 
参数|描述
---|---
disable|IPv4错误报文记录功能去使能
enable|IPv4错误报文记录功能使能
缺省 : 
IPv4错误报文记录功能使能。 
使用说明 : 
当该功能使能后，收到的IPv4错误报文被记录，IPSTACK_RP、IPSTACK_LP、LPP每个收包进程最多可以记录200条，当超过200条以后，时间最老的记录会被新记录覆盖；当该功能去使能后，收到的IPv4错误报文不再记录。
范例 : 
ZXROSNG(config)# error packet ip record enableZXROSNG(config)# error packet ip record disable
相关命令 : 
show error packet ip 
## icmp-config 

icmp-config 
命令功能 : 
该命令工作于全局配置模式，当需要进入ICMP（Internet Control Message Protocol，Internet控制报文协议）模式时，配置该命令。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
icmp-config 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
通过该命令进入ICMP模式后，才可以配置ICMP相关的命令，如interface。 
范例 : 
 
相关命令 : 
configure terminal 
interface : 

interface (ICMP模式) 
命令功能 : 
该命令工作于ICMP模式，用于进入ICMP接口模式。 
命令模式 : 
 ICMP模式  
命令默认权限级别 : 
15 
命令格式 : 
interface 
  {byname 
 ＜interface-byname 
＞|＜interface-name 
＞}
命令参数解释 : 
参数|描述
---|---
＜interface-byname＞|接口别名，最长32字符
＜interface-name＞|三层接口的名称
缺省 : 
无 
使用说明 : 
通过该命令进入ICMP接口模式后，才可以配置ICMP接口相关的命令，如ip unreachable、ipv6 unreachable、ip redirect。指定的接口必须是设备上存在的三层接口。使用接口别名时需要在对应的接口配置模式下通过byname命令设置别名后才能使用。
范例 : 
ZXROSNG(config)# icmp-configZXROSNG(config-icmp)#interface gei-0/1/0/2
相关命令 : 
icmp-config 
## ip forward unreachable 

ip forward unreachable 
命令功能 : 
该命令工作于接口配置模式，用于开启回送ICMPv4目的不可达报文功能。该命令配置成功后，如果底层硬件转发IPv4数据报文时，存在查不到路由、数据报文已经到达目的地但对应的协议没有开启或端口没有打开的情况，将该数据报文上送至CPU，由CPU向源发送端回送ICMPv4目的不可达报文。
命令模式 : 
 10G以太接口模式,pos接口模式,serial接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
以太接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,pos接口模式:15,serial接口模式:15 
命令格式 : 
ip forward unreachable 
 
no ip forward unreachable 
命令参数解释 : 
					无
				 
缺省 : 
该功能不使能 
使用说明 : 
一般情况下该命令需要和ip unreachable命令同时使用。缺省路由器没有开启该功能。
范例 : 
 
相关命令 : 
configure terminal 
## ip fragment clear-dont-fragment-bit 

ip fragment clear-dont-fragment-bit 
命令功能 : 
清除单板上的DF标记位功能 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip fragment clear-dont-fragment-bit 
  ＜CPUInfo 
＞ {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
＜CPUInfo＞|单板类型信息，支持PFU、SPU、SPFU类型
enable|单板分片命令使能
disable|单板分片命令去使能
缺省 : 
默认不配置该命令 
使用说明 : 
无 
范例 : 
ip fragment clear-dont-fragment-bit  PFU-0/1/0 enable 
相关命令 : 
ip fragment  {{enable|disable}|<cpu-info> {enable | disable }} 
## ip fragment 

ip fragment 
命令功能 : 
该命令工作于全局配置模式，用于开启路由器SPU（Service Processing Unit，业务处理单元）单板上的IPv4报文分片处理功能。该命令配置成功后，可以在SPU单板上支持NAT（Network Address Translation，网络地址转换）、IPSec（Internet Protocol Security，IP安全协议）、L2TP（Layer 2 Tunneling Protocol，二层隧道协议）等业务报文分片。IP支持路由器对IP数据报文进行分片。例如，如果IP数据报文的大小超过了转发它的链路所允许的IP MTU（Maximum Transmission Unit，最大传输单元），则路由器会对IP数据报文的有效载荷进行分片，然后作为一个个的IP分片包进行发送。使用no命令关闭分片功能。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip fragment 
  {{enable 
|disable 
}|＜CPUInfo 
＞ {enable 
|disable 
}}
命令参数解释 : 
参数|描述
---|---
enable|使能分片功能
disable|关闭分片功能
＜CPUInfo＞|CPU信息
enable|使能分片功能
disable|关闭分片功能
缺省 : 
路由器SPU单板关闭该功能。 
使用说明 : 
通过ip fragment enable命令可以配置全局分片功能开启或者关闭。通过ip fragment <cpu-info> enable命令可以配置基于单板进行分片的使能或者去使能。只有当全局分片使能开启并且单板分片使能，该单板才具有分片功能。
范例 : 
配置全局分片使能：ZXROSNG(config)#ip fragment enable配置单板分片使能：ZXROSNG(config)#ip fragment  PFU-0/1/0  enable 
相关命令 : 
ip fragment clear-dont-fragment-bit <cpu-info> {enable | disable} 
## ip icmp rate-limit unreachable 

ip icmp rate-limit unreachable 
命令功能 : 
对ICMP目的不可达报文进行限速，使报文的发送间隔不小于配置值。默认不对ICMP目的不可达报文进行限速。 
命令模式 : 
 ICMP模式  
命令默认权限级别 : 
15 
命令格式 : 
ip icmp rate-limit unreachable 
  ＜rate limit 
＞
no ip icmp rate-limit unreachable 
命令参数解释 : 
参数|描述
---|---
＜rate limit＞|设备上产生的ICMP目的不可达报文的最小发送间隔，单位为毫秒。可配置范围为1- 4294967295毫秒
缺省 : 
默认不对ICMP目的不可达报文进行限速 
使用说明 : 
当存在以下几种情况时，设备会产生ICMP目的不可达报文：1、设备上收到一个IP数据报文时，发现该数据报文找不到路由，则向该报文的源发送端回送一个ICMP目的不可达报文(type=3,code=0)；2、设备上收到一个IP数据报文且该数据报文已经到达目的地时，会检测该数据报文首部中的协议类型字段，如果对应的上层协议没有开启（即该协议不在运行），则向该报文的源发送端回送一个ICMP目的不可达报文(type=3,code=2)；3、 设备上收到一个IP数据报文，如果该数据报文已经到达目的地，会检测该数据报文的端口号是否开启，如果没有开启，则向该报文的源发送端回送一个ICMP目的不可达报文(type=3,code=3)；4、设备上转发IP数据报文时，如果报文长度超过接口的IP MTU，但该数据报文的首部DF（Don’t Fragment，不分片）位置1（即不允许分片)，则向该报文的源发送端回送一个ICMP目的不可达报文(type=3,code=4)；5、设备上收到一个带LSRR（Loose Source and Record Route，宽松源路由器)选项和SSRR（Strict Source and Record Route，严格源路由）选项的数据报文时，由于找不到路由或者源路由功能关闭（参见ip source route命令)，则向该报文的源发送端回送一个ICMP目的不可达报文(type=3,code=5)。请注意根据实际情况配置。如果设备上产生的ICMP目的不可达报文比较少，可以不用配置该命令。如果设备上由于某些原因（比如上述五种情况）产生了大量的ICMP目的不可达报文，影响了CPU的利用率，可以使用该命令对ICMP目的不可达报文进行限速，将配置值尽量配置得大一些直至不影响CPU的利用率为止。当发送ICMP不可达报文时间间隔小于配置的限速值时，丢弃报文。特别注意：1、如果设备需要回应trace(参见trace命令)，配置值不能大于3000毫秒。2、如果设备需要支持pmtu功能，建议不对ICMP目的不可达报文限速。
范例 : 
配置ICMP目的不可达报文的发包间隔不小于3000毫秒：ZXROSNG(config-icmp)#ip icmp rate-limit unreachable 3000
相关命令 : 
无 
## ip icmp specify-source interface 

ip icmp specify-source interface 
命令功能 : 
该命令工作于ICMP配置模式，用于设置ICMPv4差错报文的源IP地址为指定的loopback接口上的主地址。ICMPv4差错报文主要用于运维环节，设备上过多的IP地址影响运维人员判断，指定使用loopback地址发送ICMPv4差错报文，可以简化这一判断过程。 
命令模式 : 
 ICMP模式  
命令默认权限级别 : 
15 
命令格式 : 
ip icmp specify-source interface 
  ＜interface name 
＞
no ip icmp specify-source interface 
命令参数解释 : 
参数|描述
---|---
＜interface name＞|loopback接口名称，字符类型，长度为1-32
缺省 : 
无 
使用说明 : 
默认ICMPv4差错报文的源IP地址为入接口或出接口的地址，配置该命令后，ICMPv4差错报文的源IP地址为指定loopback接口的主地址，当该接口down或无IP地址时，仍使用入接口或出接口的地址。需要注意的是：配置该命令后，trace中间节点回应的ICMP超时报文、终点回应的ICMP目的不可达报文的源IP地址为指定的loopback接口地址，会导致trace路径不明确的问题。 
范例 : 
指定ICMPv4差错报文的源IP地址为接口loopback1的主地址：ZXROSNG(config-icmp)#ip icmp specify-source interface loopback1
相关命令 : 
无 
## ip icmp time-exceed 

ip icmp time-exceed 
命令功能 : 
该命令工作于ICMP配置模式，用于开启或者关闭设备回复ICMPv4超时报文功能。 
命令模式 : 
 ICMP模式  
命令默认权限级别 : 
15 
命令格式 : 
ip icmp time-exceed 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启回复ICMPv4 超时报文功能
disable|关闭回复ICMPv4 超时报文功能
缺省 : 
默认本设备开启回复ICMPv4超时报文功能。 
使用说明 : 
当存在以下两种情况时，设备会产生ICMPv4超时报文：1、设备上转发一个IPv4数据报文时，如果该数据报文的TTL为0或1，向该报文的源发送端回复一个ICMPv4超时报文(type=11,code=0)；2、设备上重组IPv4分片报文时，如果在一定的时间内（60秒）由于部分分片报文丢失导致无法重组成功，且第一个分片报文没有丢失，向该报文的源发送端回复一个ICMPv4超时报文(type=11,code=1)；特别注意：如果设备需要回应trace(参见trace命令)，不能配置ip icmp time-exceed disable。
范例 : 
开启回复ICMPv4超时报文功能：ZXROSNG(config-icmp)#ip icmp time-exceed enable关闭回复ICMPv4超时报文功能：ZXROSNG(config-icmp)#ip icmp time-exceed disable
相关命令 : 
无 
## ip icmp timestamp-reply 

ip icmp timestamp-reply 
命令功能 : 
该命令工作于ICMP配置模式，用于开启设备回应ICMP时间戳请求的功能。ICMP时间戳请求允许系统向另外一个系统查询当前的时间，返回的建议值是自午夜开始计算的毫秒数。 
命令模式 : 
 ICMP模式  
命令默认权限级别 : 
15 
命令格式 : 
ip icmp timestamp-reply 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|enable:使能回应ICMP Timestamp请求功能；
disable|disable:去使能回应ICMP Timestamp 请求功能
缺省 : 
默认本设备回应ICMP时间戳请求。 
使用说明 : 
配置ip icmp timestamp-reply enable 命令后，使能回应ICMP Timestamp 请求功能，发出Timestamp Reply报文。配置ip icmp timestamp-reply disable命令后，去使能回应ICMP Timestamp请求功能，不回Timestamp Reply报文。 
范例 : 
ZXROSNG(config-icmp)#ip icmp timestamp-reply enableZXROSNG#debug ip icmp packetICMP debugging is onZXROSNG#ter moZXR10 MPU-0/20/0 2013-7-17 07:40:28  IP ICMP:rcvd type timestamp req, code   0, src 1.1.1.1, dst 1.1.1.2ZXR10 MPU-0/20/0 2013-7-17 07:40:28  IP ICMP:sent type timestamp rep, code   0, src 1.1.1.2, dst 1.1.1.1ZXROSNG(config-icmp)#ip icmp timestamp-reply disable ZXROSNG(config-icmp)#endZXR10 MPU-0/20/0 2013-7-17 07:42:05  IP ICMP:rcvd type timestamp req, code   0, src 1.1.1.1, dst 1.1.1.2
相关命令 : 
无 
## ip icmp-fast-reply 

ip icmp-fast-reply 
命令功能 : 
该命令工作于全局配置模式，用于开启ICMP（Internet Control Message Protocol，Internet控制报文协议）快速响应功能。命令执行成功后，由硬件来响应Ping请求报文，可以缩短Ping时延。使用ip icmp-fast-reply disable 或no ip icmp-fast-reply命令关闭该功能后，则由软件来响应Ping请求报文。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip icmp-fast-reply 
  [disable 
]
no ip icmp-fast-reply 
命令参数解释 : 
参数|描述
---|---
disable|去使能ICMP快速响应功能
缺省 : 
缺省路由器快速响应Ping请求报文。 
使用说明 : 
1、当该命令开关由开启变为关闭时，系统会显示“%Info 130602: ICMP-fast-reply feature is off!”进行提示。2、当该命令开关由关闭变为开启时，系统会显示“%Info 130601: ICMP-fast-reply feature is on!“进行提示。
范例 : 
如果希望ping命令的网络时延较小，可以在设备上配置ip icmp-fast-reply命令。如：ZXROSNG(config)#ip icmp-fast-reply%Info 130601: ICMP-fast-reply feature is on! 
相关命令 : 
configure terminal 
## ip max-reassemble-session 

ip max-reassemble-session 
命令功能 : 
该命令工作于全局配置模式，用于设置路由器SPU单板上IPv4报文最大重组会话个数。该命令配置成功后，路由器SPU单板上能同时进行重组的IPv4报文的个数为配置值。 使用no命令恢复默认值。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip max-reassemble-session 
  ＜value 
＞
no ip max-reassemble-session 
命令参数解释 : 
参数|描述
---|---
＜value＞|最大重组池容量，单位：个数，范围1-6144，默认值 4096
缺省 : 
最大重组池容量为4096个 
使用说明 : 
ip max-reassemble-session命令在配置时注意要根据实际情况配置，否则可能会影响重组效率。当网络上有较多的分片包，可以使用该命令将最大重组会话个数配大一些，提高重组效率。
范例 : 
ZXROSNG(config)#ip max-reassemble-session 33 
相关命令 : 
ip min-fragment-offsetip min-fragment-sizeip reassemble-time
## ip min-fragment-offset 

ip min-fragment-offset 
命令功能 : 
该命令工作于全局配置模式，用于设置路由器SPU单板上IPv4报文重组时分片包的最小片偏移。该命令配置成功后，当路由器SPU单板上收到的分片包的片偏移小于本命令的配置值时，路由器丢弃该分片包。这样做的目的主要是出于安全考虑。该命令不对首片包生效，因为首片包的片偏移固定为0。如果IP数据报文的大小超过了转发它的链路所允许的IP MTU（Maximum Transfer Unit，最大传输单元）时，路由器会对该数据报文进行分片，然后在目的端再将各个分片进行重组。IPv4报文头中有一个片偏移（Fragment Offset）字段，用来记录各个分片包相对于原包的偏移量，以便于在重组的时候知道各个分片包在原包中的位置。使用no命令恢复为默认值。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip min-fragment-offset 
  ＜bytes 
＞
no ip min-fragment-offset 
命令参数解释 : 
参数|描述
---|---
＜bytes＞|IP分片包的最小片偏移，单位：字节，范围0-65535，默认值 0
缺省 : 
最小片偏移的缺省值是0。 
使用说明 : 
ip min-fragment-offset命令在配置时注意要根据实际情况配置，否则可能会影响正常重组。例如，一个长度为5000字节的IPv4报文（没有IP选项），转发链路上的IP MTU均为1500字节，则该报文分为4片，第二片的片偏移为1480字节，此时ip min-fragment-offset便不能配置为大于1480字节的值，否则第二片会被丢弃，重组失败。
范例 : 
配置SPU单板上IPv4报文重组时分片包的最小片偏移量为48字节。ZXROSNG(config)#ip min-fragment-offset 48
相关命令 : 
ip min-fragment-sizeip reassemble-timeip max-reassemble-session
## ip min-fragment-size 

ip min-fragment-size 
命令功能 : 
该命令工作于全局配置模式，用于设置路由器SPU单板上IPv4报文重组时分片包的最小长度。该命令配置成功后，当路由器SPU单板上收到的分片包的长度小于配置值时，路由器丢弃该分片包。这样做的目的主要是出于安全考虑。该命令不对尾片包生效。如果IP数据报文的大小超过了转发它的链路所允许的IP MTU（Maximum Transfer Unit，最大传输单元）时，路由器会对数据报文进行分片，然后在目的端再对分片进行重组。非尾片包的有效载荷的长度规定必须为8字节的倍数，那么加上IPv4头的长度，则非尾片包的长度至少为28字节。使用no命令恢复默认值。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip min-fragment-size 
  ＜bytes 
＞
no ip min-fragment-size 
命令参数解释 : 
参数|描述
---|---
＜bytes＞|IP分片包的最小长度，单位：字节，范围1-65535，默认值 28
缺省 : 
最小分片包长度的缺省值为28字节。 
使用说明 : 
ip min-fragment-size命令在配置时注意要根据实际情况配置，否则可能会影响正常重组。例如，一个长度为5000字节的IPv4报文（没有IP选项），转发链路上的IP MTU均为1500字节，则该报文分为4片，非尾片包的长度均为1500字节，此时ip min-fragment-size便不能配置为大于1500字节的值，否则非尾片包都会被丢弃，重组失败。
范例 : 
ZXROSNG(config)#ip min-fragment-size 33 
相关命令 : 
ip min-fragment-offsetip reassemble-timeip max-reassemble-session
## ip path-mtu-discovery age-timer 

ip path-mtu-discovery age-timer 
命令功能 : 
该命令工作于全局配置模式，用于设置本路由器路径MTU(Maximum Transmission Unit，最大传输单元)的老化时间。IP是针对以太网、帧中继等多种网络技术构成的网络的应用而设计的，每种网络技术都有不同的MTU，即其能发送的帧的最大大小。IP MTU就是所能发送的IP包的最大大小。为了适应各种网络技术不同的IP MTU，IP允许路由器将数据包进行分片。由于分片会对路由器性能产生影响，因此，对性能要求较高的TCP应用（比如BGP）应该尽量避免路由器对其IP包进行分片。路径MTU是指通信路径中最小的MTU，是该路径上报文是否分片的依据。开启路径MTU自动发现功能可以发现从源端到目的端的路径MTU值，提高该路径上的报文传输效率。路径MTU不一定是固定值，它取决于传输消息时所选择的路由。如果相互通信的两端之间存在多条路由，并且传输报文选择的路由变化频繁，这时就需要为路径MTU配置老化时间。配置路径MTU老化时间后，系统会按照老化时间间隔更新路径MTU，从而适配网络的变化情况，提高传输效率。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip path-mtu-discovery age-timer 
  ＜Aging time 
＞
no ip path-mtu-discovery age-timer 
命令参数解释 : 
参数|描述
---|---
＜Aging time＞|<作用> 路径MTU老化时间<取值范围>10~65535分钟<默认值> 10分钟
缺省 : 
IPv4路径MTU老化时间为10分钟 
使用说明 : 
缺省路由器路径MTU老化时间是10分钟。使用ip path-mtu-discovery age-timer命令可以配置路径MTU老化时间。使用no ip path-mtu-discovery age-timer命令可以将路径MTU老化时间恢复至默认时间。在使用该命令之前需要先开启路径MTU自动发现功能。缺省关闭路径MTU自动发现功能。如果某种应用（目前仅BGP支持）需要开启该功能，在该应用对应的配置模式下开启即可。如BGP需要开启该功能，则在bgp配置模式下配置 neighbor <ipv4-address> transport path-mtu-discovery（参见bgp相关命令）。可以通过show ip pmtu 来查看PMTU条目。
范例 : 
ZXROSNG(config)#ip path-mtu-discovery age-timer 20ZXROSNG(config)#no ip path-mtu-discovery age-timer  
相关命令 : 
show ip pmtu 
## ip reassemble-time 

ip reassemble-time 
命令功能 : 
该命令工作于全局配置模式，用于设置路由器SPU单板上IPv4报文重组的超时时间。IPv4报文重组时，系统会设置一个定时器，当此定时器超时后，由于某些原因IPv4报文还没有重组成功，则系统释放资源，放弃对该报文的重组。使用no命令恢复默认值。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip reassemble-time 
  ＜seconds 
＞
no ip reassemble-time 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|报文的重组超时时间，单位：秒，范围1-30，默认值 10
缺省 : 
报文重组超时时间为10秒 
使用说明 : 
ip min-fragment-size命令在配置时，注意要根据实际情况配置，否则可能会影响正常重组。当网络中有较多的分片碎片时，可以将重组超时时间配小一些，以便尽快释放资源。 
范例 : 
配置SPU单板上IPv4报文重组的超时时间为5s。ZXROSNG(config)#ip reassemble-time 5
相关命令 : 
ip min-fragment-offsetip min-fragment-sizeip max-reassemble-session
## ip redirect 

ip redirect 
命令功能 : 
该命令工作于ICMP接口模式，用于开启回送ICMPv4重定向报文功能。ICMPv4重定向报文的作用是通知主机修改路由。主机启动时路由表中可能只有一个默认项。开始时，该主机上所有报文都发送到默认网关，默认网关在转发时如果发现有更优路由，向该主机回送ICMPv4重定向报文，在ICMPv4重定向报文中携带更优的网关，主机收到ICMPv4重定向报文后，修改路由表。使用no命令关闭该功能。
命令模式 : 
 ICMP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip redirect 
 
no ip redirect 
命令参数解释 : 
					无
				 
缺省 : 
该功能不使能 
使用说明 : 
设备回送ICMPv4重定向报文需要满足以下几个条件：在ICMP接口模式下配置ip redirect命令，接口为报文三层入接口；报文的入接口与转发时的出接口相同；当前路由器与该数据报文的源发送端在同一个子网内；该数据报文的下一跳与源发送端在同一个子网内；
范例 : 
 
相关命令 : 
configure terminalicmp-config
## ip source-route 

ip source-route 
命令功能 : 
该命令工作于全局配置模式，用于配置本路由器支持处理带源路由器选项的IPv4报文。IP支持源发送端为报文预先指定一个转发路径，后续的路由器根据指定的路径转发报文。宽松源路由（LSRR，Loose Source and Record Route）选项和严格源路由（SSRR，Strict Source and Record Route）选项都提供了该功能，它们之间的区别是：宽松源路由选项中相邻的两个地址之间可以经过任意个中间路由器，而严格源路由选项中的相邻的两个地址必须是直接相连的。该命令配置成功后，路由器会检查收到的每一个IPv4报文的选项，如果选项类型为宽松源路由选项或严格源路由选项，则根据源发送端指定的转发路径进行转发或本地处理。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip source-route 
  [disable 
]
no ip source-route 
命令参数解释 : 
参数|描述
---|---
disable|去使能IP源路由选项功能
缺省 : 
该功能使能 
使用说明 : 
缺省路由器支持处理带源路由选项的IPv4报文。使用ip source-route disable或no ip source-route命令可以关闭该功能。
范例 : 
网络中的三台路由器Router1、Router2和Router3之间需要通信。三台设备的地址分别为1.1.1.1、1.1.1.2、1.1.2.2。为了测试Router1到Router3的链路是否是连通的，一般可以在Router1上执行ping命令，目的地址是Router3上的地址。如果非常了解组网情况，可以在Router1上预先指定好路由，这样报文在转发的过程中会根据在源发送端指定好的转发路径进行报文转发。如在Router1上执行ping 1.1.2.3 option strict 1.1.1.2。为了确保该路径上的所有路由器支持源路由选项，需要在Router1、Router2和Router3上配置ip source-route命令。如：ZXROSNG(config)#ip source-route
相关命令 : 
configure terminal 
## ip unreachable 

ip unreachable 
命令功能 : 
该命令工作于ICMP接口模式，用于开启回送ICMPv4目的不可达报文功能。该命令配置成功后，当存在以下几种情况时，路由器向报文的源发送端回送ICMPv4目的不可达报文。1、收到一个IPv4数据报文时，发现该数据报文找不到路由，则向该报文的源发送端回送一个ICMPv4目的不可达报文（type=3,code=0）；2、收到一个IPv4数据报文且该数据报文已经到达目的地时，会检测该数据报文首部中的协议类型字段，如果对应的上层协议没有开启（即该协议不在运行），则向该报文的源发送端回送一个ICMPv4目的不可达报文（type=3,code=2）；3、收到一个IPv4数据报文，如果该数据报文已经到达目的地，会检测该数据报文的端口号是否开启，如果没有开启，则向该报文的源发送端回送一个ICMPv4目的不可达报文（type=3,code=3）；4、转发IPv4数据报文时，如果报文长度超过接口的IP MTU，但该数据报文的首部DF（Don’t Fragment，不分片）位置1（即不允许分片），则向该报文的源发送端回送一个ICMPv4目的不可达报文（type=3,code=4）；5、收到一个带LSRR（Loose Source and Record Route，宽松源路由器）选项和SSRR（Strict Source and Record Route，严格源路由）选项的数据报文时，由于找不到路由或者源路由功能关闭（参见ip source route命令），则向该报文的源发送端回送一个ICMPv4目的不可达报文（type=3,code=5）。使用ip unreachable disable或no ip unreachable命令可以关闭该功能。
命令模式 : 
 ICMP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ip unreachable 
  [disable 
]
no ip unreachable 
命令参数解释 : 
参数|描述
---|---
disable|关闭ICMP报文不可达功能
缺省 : 
该功能使能 
使用说明 : 
该命令需要和ip forward unreachable命令同时使用。ip forward unreachable命令需要在IPv4数据报文的物理入接口上配置，ip unreachable命令需要在IPv4数据报文物理入接口所在的三层接口上配置。
范例 : 
 
相关命令 : 
configure terminalicmp-config
## ipv6 forward unreachable 

ipv6 forward unreachable 
命令功能 : 
该命令工作于接口模式，用于配置开启回送ICMPv6目的不可达报文功能和参数错误报文。该命令配置成功后，如果底层硬件转发IPv6数据报文时，存在查不到路由、数据报文已经到达目的地但对应的协议没有开启或端口没有打开等情况，将该数据报文上送至CPU，由CPU向源发送端回送ICMPv6差错报文。
命令模式 : 
 10G以太接口模式,pos接口模式,serial接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
千兆以太接口模式:15,以太接口模式:15,10G以太接口模式:15,serial接口模式:15,pos接口模式:15 
命令格式 : 
ipv6 forward unreachable 
 
no ipv6 forward unreachable 
命令参数解释 : 
					无
				 
缺省 : 
该功能不使能 
使用说明 : 
一般情况下该命令需要和ipv6 unreachable命令同时使用。缺省路由器没有开启该功能。
范例 : 
参考ip unreachable的命令示例。 
相关命令 : 
configure terminal 
## ipv6 unreachable 

ipv6 unreachable 
命令功能 : 
该命令工作于ICMP接口模式，用于开启ICMPv6的不可达功能，回送ICMPv6目的不可达报文或者参数错误报文。该命令配置成功后，当存在以下几种情况时，会向报文的源发送端回送ICMPv6错误报文。1.收到一个IPv6数据报文时发现该数据报文找不到路由，则向该报文的源发送端回送一个ICMPv6目的不可达报文（type=1,code=0）；2.收到一个IPv6数据报文时，检测到该数据报文首部中的目的IP地址和源IP地址范围不一致时，则向该报文的源发送端回送一个ICMPv6目的不可达报文（type=1,code=2）；3.如果学不到邻居的目的MAC，则向该报文的源发送端回送一个ICMPv6目的不可达报文（type=1,code=3）；4.收到一个IPv6数据报文，如果该数据报文已经到达目的地，会检测数据报文的端口号是否开启，如果没有开启，则向该报文的源发送端回送一个ICMPv6目的不可达报文（type=1,code=4）；  5.收到一个IPv6报文，协议号是未知的，则向该报文的源发送端回送一个ICMPv6参数错误报文（type=4,code=1）。使用ipv6 unreachable disable或no ipv6 unreachable命令可以关闭该功能。
命令模式 : 
 ICMP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 unreachable 
  [disable 
]
no ipv6 unreachable 
命令参数解释 : 
参数|描述
---|---
disable|去使能接口发送ICMPv6差错报文功能
缺省 : 
该功能使能 
使用说明 : 
该命令需要和ipv6 forward unreachable命令同时使用。ipv6 forward unreachable 命令需要在IPv6数据报文的物理入接口上配置，ipv6 unreachable命令需要在IPv6数据报文的物理入接口所在的三层接口上配置。
范例 : 
 
相关命令 : 
configure terminal 
## ping6 

ping6 
命令功能 : 
该命令用于检查IPv6网络连接及主机是否可达。当网络节点或主机之间出现连通性故障时，可以使用该命令进行诊断。 
命令模式 : 
 用户模式  
命令默认权限级别 : 
1 
命令格式 : 
ping6 
  [vrf 
 ＜vrf-name 
＞] {＜ipv6-address 
＞|domain 
 ＜domain-name 
＞} [interface 
 ＜interface-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：设置目的IP地址或域名所属的VRF名称。取值范围：1~32个字符。默认值：无。
＜ipv6-address＞|作用：设置目的主机的IPv6地址。取值范围：IPv6地址。默认值：无。
＜domain-name＞|作用：与目的IP地址等价的域名。取值范围：1~128个字符。默认值：无。
＜interface-name＞|作用： 当目的IPv6 地址是Linklocal 类型地址时， 设置ICMP ECHO-REQUEST报文的发包接口。取值范围：实际存在的接口。默认值：无。
缺省 : 
无 
使用说明 : 
* 该命令只能进行简单的连通性检查。如果需要通过ping6操作了解更多网络故障相关信息，请进入命令终端，在除用户模式外的其他模式下执行ping6检测。* 如果命令中设置了VRF，则设置的VRF必须是与远端IP地址或域名关联的VRF，否则ping6检测操作失败。* 在发起ping6检测时，如果指定的远端IP地址或域名不存在，则不能正确诊断网络的连通性。* 该命令执行后，用户除根据输出结果判断网络连通性之外，还可以根据ping6测试输出的报文响应时间，来判断网络链路质量。
范例 : 
在用户模式下，用ping 命令检测网络节点的连通性：ZXUN>ping6 100::1sending 5,100-byte ICMP echo(es) to 100:0:0:0:0:0:0:1,timeout is 2 second(s).!!!!!Success rate is 100 percent(5/5),round-trip min/avg/max= 6/11/29.
相关命令 : 
无 
## ping 

ping 
命令功能 : 
该命令在用户模式下执行，用于检查IPv4网络的连接状况。当网络节点或主机之间出现连通性故障时，可以使用该命令进行诊断。 
命令模式 : 
 用户模式  
命令默认权限级别 : 
1 
命令格式 : 
ping 
  [vrf 
 ＜vrf-name 
＞] {＜ipv4-address 
＞|domain 
 ＜domain-name 
＞}
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：设置目的IP地址或域名所属的VRF名称。取值范围：1~32个字符。默认值：无。
＜ipv4-address＞|作用：设置远端IP地址。取值范围：IPv4地址。默认值：无。
＜domain-name＞|作用：与目的IP地址等价的域名。取值范围：1~128个字符。默认值：无。
缺省 : 
无 
使用说明 : 
* 该命令只能进行简单的连通性检查。如果需要通过ping操作了解更多网络故障相关信息，请进入命令终端，在除用户模式外的其他模式下执行ping检测。* 如果命令中设置了VRF，则设置的VRF必须是与远端IP地址或域名关联的VRF，否则ping检测操作失败。* 在发起ping检测时，如果指定的远端IP地址或域名不存在，则不能正确诊断网络的连通性。* 该命令执行后，用户除根据输出结果判断网络连通状况之外，还可以根据ping测试输出的报文响应时间，来判断网络链路质量。* 按下Ctrl+C终止ping检测。
范例 : 
在用户模式下，用ping命令检测网络节点的连通性：ZXUN>ping 10.1.1.2sending 5,100-byte ICMP echo(es) to 10.1.1.2,timeout is 2 second(s).!!!!!Success rate is 100 percent(5/5),round-trip min/avg/max= 7/9/18 ms.ZXUN>
相关命令 : 
无 
## ping 

ping 
命令功能 : 
该命令在非用户模式下执行，用于检查IPv4网络的连接状况。当网络节点或主机之间出现连通性故障时，可以使用该命令进行诊断。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
2 
命令格式 : 
ping 
  [{dcn 
|[vrf 
 ＜vrf-name 
＞]}] {＜ipv4-address 
＞|domain 
 ＜domain-name 
＞} [{[df-bit 
 ＜dont-frag 
＞],[pattern 
 ＜pattern-string 
＞],[repeat 
 ＜repeat-count 
＞],[size 
 ＜datagram-size 
＞],[source 
 ＜ipv4-address 
＞],[timeout 
 ＜timeout 
＞],[tos 
 ＜tos 
＞],[ttl 
 ＜ttl 
＞],[option 
 {loose 
 *(＜ipv4-address 
＞)|strict 
 *(＜ipv4-address 
＞)|record 
 ＜para 
＞|timestamp 
 ＜para 
＞|none 
}],[speed 
 {limit 
 {＜absolute-mode 
＞|＜limit-number 
＞}|interval 
 ＜interval-number 
＞}],[interface 
 ＜interface-name 
＞],[ecmp 
],[verbose 
],[next-hop 
 ＜next-hop 
＞]}]
命令参数解释 : 
参数|描述
---|---
dcn|作用：设置虚拟路由（VRF）为DCN，DCN为一种特殊的虚拟路由。取值范围：无。默认值：无。
＜vrf-name＞|作用：设置目的IP地址或域名所属的VRF名称。取值范围：1~32个字符。默认值：无。
＜ipv4-address＞|作用：设置选择严格选路时的下一跳IP地址，必须是直连下一跳IP地址。取值范围：IPv4地址。默认值：无。
＜domain-name＞|作用：与远端IP等效的域名。取值范围：1~128个字符。默认值：无。
＜dont-frag＞|作用：设置ECHO-REQUEST报文发送过程中是否分片。取值范围：0或1。0：表示分片；1：表示不分片。默认值：0。
＜pattern-string＞|作用：设置ICMP ECHO-REQUEST报文填充字节，格式为16进制。取值范围：<0000-FFFF>，长度必须为4个16进制数。默认值：无。
＜repeat-count＞|作用：设置发送ICMP ECHO-REQUEST报文次数。取值范围：1~65535之间的整数。默认值：5。
＜datagram-size＞|作用：设置ECHO-REQUEST报文长度，单位是字节。取值范围：36~$#34144266#$字节。默认值：100字节。
＜ipv4-address＞|作用：设置选择严格选路时的下一跳IP地址，必须是直连下一跳IP地址。取值范围：IPv4地址。默认值：无。
＜timeout＞|作用：设置发送完ECHO-REQUEST报文后，等待ECHO-RESPONSE报文的超时时间，单位为秒。取值范围：1~60秒。默认值：2秒。
＜tos＞|作用：设置发送ECHO-REQUEST报文的服务类型TOS值。取值范围：0~255。默认值：0。
＜ttl＞|作用：设置数据包在网络中的生存时间TTL值。取值范围：1~255。默认值：255。
loose|作用：设置发送ICMP ECHO-REQUEST报文携带松散选路选项。
＜ipv4-address＞|作用：设置选择严格选路时的下一跳IP地址，必须是直连下一跳IP地址。取值范围：IPv4地址。默认值：无。
strict|作用：设置发送ICMP ECHO-REQUEST报文携带严格选路选项。
＜ipv4-address＞|作用：设置选择严格选路时的下一跳IP地址，必须是直连下一跳IP地址。取值范围：IPv4地址。默认值：无。
record|作用：设置发送ICMP ECHO-REQUEST报文携带记录IP路由选项。
＜para＞|作用：设置记录时间戳个数。取值范围：1~9。默认值：无。
timestamp|作用：设置发送ICMP ECHO-REQUEST报文携带记录时间戳选项。
＜para＞|作用：设置记录时间戳个数。取值范围：1~9。默认值：无。
none|作用：设置发送ICMP ECHO-REQUEST报文不带选项信息。取值范围：无。默认值：无。
＜absolute-mode＞|作用：设置发送ECHO-REQUEST报文的模式，在超时时间内收到ECHO-RESPONSE报文后，立即发送下一个测试报文。取值范围：0。默认值：无。
＜limit-number＞|作用：设置每秒发送ECHO-REQUEST报文的最大个数。取值范围：1~100。默认值：10。
＜interval-number＞|作用：设置发送ECHO-REQUEST报文的时间间隔。取值范围：2~10秒。默认值：无。
＜interface-name＞|作用：在发起组播ping时，指定ping报文的发包接口。取值范围：本端接口。默认值：无。
ecmp|作用：设置发起多路径PING检测。取值范围：无。默认值：无。
verbose|作用：设置verbose回显模式，显示详细结果。取值范围：无。默认值：无。
＜next-hop＞|作用：下一跳IP地址。 取值范围：IPv4地址。 默认值：无。
缺省 : 
无 
使用说明 : 
* 如果网络速度较慢，执行ping测试时可适当加大等待响应报文的超时时间。* 如果命令中设置了VRF，则设置的VRF必须是与远端IP地址或域名关联的VRF，否则ping检测操作失败。* 在发起ping检测时，如果指定的远端IP地址或域名不存在，则不能正确诊断网络的连通性。* 该命令执行后，用户除根据输出结果判断网络连通性之外，还可以根据ping测试输出的报文响应时间，来判断网络链路质量。* 按下Ctrl+C终止ping检测。
范例 : 
在特权模式下，用ping 命令检测网络节点的连通性。1. 进入特权模式：ZXUN>en 18Password:ZXUN#2. 在特权模式下，用ping 命令来检测网络节点的连通性：ZXUN#ping 10.1.1.2 df-bit 1 speed interval 2 timeout 2 repeat 10sending 10,100-byte ICMP echo(es) to 10.1.1.2,timeout is 2 second(s).!!!!!!!!!!Success rate is 100 percent(10/10),round-trip min/avg/max= 7/39/97 ms.ZXUN#ZXUN#ping 168.1.10.100sending 5,100-byte ICMP echo(es) to 168.1.10.100,timeout is 2 second(s).!!!!!Success rate is 100 percent(5/5),round-trip min/avg/max= 0/8/20 ms.ping 100.0.1.2 verbosesending 5,100-byte ICMP echo(es) to 100.0.1.2,timeout is 2 second(s).Reply from 100.0.1.2: bytes=100 sequence=1 TTL=254 time=10msReply from 100.0.1.2: bytes=100 sequence=2 TTL=254 time=1msReply from 100.0.1.2: bytes=100 sequence=3 TTL=254 time=1msReply from 100.0.1.2: bytes=100 sequence=4 TTL=254 time=1msReply from 100.0.1.2: bytes=100 sequence=5 TTL=254 time=1msZXROSNG(config)#Ping statistics for 100.0.1.2:    5 request(s) transmitted    5 reply(s) received    Success rate is 100%    0 error report packet(s)    0 repeated packet(s)    0 invalid packet(s)    round-trip min/avg/max = 1/2/10 ms[finish]
相关命令 : 
无 
## ping-tcp-server 

ping-tcp-server 
命令功能 : 
TCP ping服务开启或关闭。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ping-tcp-server 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启TCP ping服务
disable|关闭TCP ping服务
缺省 : 
默认为关闭TCP ping服务。 
使用说明 : 
需要TCP ping服务，要设置成enable。 
范例 : 
ZXROSNG#con terEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#ping-tcp-server ?  disable  TCP ping sever disable  enable   TCP ping sever enableZXROSNG(config)#ping-tcp-server enableZXROSNG(config)#
相关命令 : 
无 
## ping-udp-server 

ping-udp-server 
命令功能 : 
开启或关闭UDP PING侦听服务，服务开启后可应答UDP PING请求。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ping-udp-server 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|作用：设置UDP PING服务侦听开启。取值范围：无。默认值：无。
disable|作用：设置UDP PING服务侦听关闭。取值范围：无。默认值：无。
缺省 : 
UDP PING服务侦听默认关闭。 
使用说明 : 
* 需要响应UDP PING请求时，需要开启UDP PING侦听服务* 命令配置后并不能保证侦听服务能立刻开启：如果侦听端口已被其他业务占用，则不能立即生效，需要端口释放后才能开启侦听。可通过show ping server查看Socket状态是否已成功开启侦听。
范例 : 
配置UDP PING侦听。1. 进入特权模式：ZXR10>en 18Password:ZXROSNG#2. 进入全局配置模式：ZXROSNG#configure terminal Enter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#3. 在全局配置模式下，开启UDP PING侦听服务：ZXROSNG(config)#ping-udp-server enable %Info 112028: Ping server will not work until socket is created successfully.
相关命令 : 
ping-udp-server disableshow ping server
## show control-protocol priority 

show control-protocol priority 
命令功能 : 
显示协议的全局优先级信息，包括dscp、precedence、标签优先级exp和vlan优先级8021p。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show control-protocol priority 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1. 若配置了全局优先级，则显示配置值；若没有配置，则显示协议的默认优先级；若某协议既没有配置全局优先级，也没有默认的优先级，则显示“NA”。 
范例 : 
ZXROSNG#show control-protocol priority Protocol       DSCP          Precedence      EXP           802.1pARP            N/A            N/A            N/A           N/ABGP            56             7              N/A           N/ADHCP           N/A            N/A            N/A           N/ADNS            N/A            N/A            N/A           N/AFTP            48             6              N/A           N/AHAGP           N/A            N/A            N/A           N/AIGMP           48             6              N/A           N/AISIS           N/A            N/A            N/A           N/ALDP            56             7              N/A           N/AMLD            48             N/A            N/A           N/AMPLS-OAM       N/A            N/A            N/A           N/AMSDP           48             6              N/A           N/AND             56             N/A            N/A           N/ANetFlow        N/A            N/A            N/A           N/ANTP            N/A            N/A            N/A           N/AOpenFlow       N/A            N/A            N/A           N/AOSPF           56             7              N/A           N/APCEP           56             7              N/A           N/APIM            48             6              N/A           N/APING           N/A            N/A            N/A           N/ARADIUS         48             6              N/A           N/ARIP            56             7              N/A           N/ARSVP           56             7              N/A           N/ASIB            48             6              N/A           N/ASNMP           N/A            N/A            N/A           N/ASSH            48             6              N/A           N/ASYSLOG         N/A            N/A            N/A           N/ATACACS+        N/A            N/A            N/A           N/ATELNET         48             6              N/A           N/ATFTP           N/A            N/A            N/A           N/ATRACE          N/A            N/A            N/A           N/AVRRP           56             7              N/A           N/A
相关命令 : 
control-rptocol 
## show debug icmp 

show debug icmp 
命令功能 : 
该命令工作于除用户模式之外的所有模式，用于查看ICMPv4 debug开关是否开启。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug icmp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于帮助用户查看ICMPv4 debug开关开启情况，在debug ip icmp和debug ip icmp detail开关关闭的情况下，执行该命令后没有debug开关关闭的回显信息，只有在debug ip icmp 或debug ip icmp detail开关开启时，才会有相应的回显信息。 
范例 : 
ZXROSNG#debug ip icmp  detail ICMP packet detail debugging is onZXROSNG#debug ip icmp packet         ICMP packet debugging is onZXROSNG#show debug icmpICMP:  ICMP packet debugging is on  ICMP packet detail debugging is on
相关命令 : 
debug ip icmp  detail debug ip icmp  packet
## show debug ip 

show debug ip 
命令功能 : 
该命令工作于除用户模式之外的所有模式，用于查看IPv4 debug开关是否开启。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug ip 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于帮助用户查看IPv4 debug开关开启情况，在debug ip和debug ip interface开关关闭的情况下，执行该命令后没有debug开关关闭的回显信息，只有在debug ip或debug ip interface开关开启时，才会有相应的回显信息。 
范例 : 
ZXROSNG#debug ip IP debugging is onZXROSNG#debug ip interface gei-0/1/0/1IP interface debugging is onZXROSNG#show debug ipIP:  IP debugging is on  IP interface gei-0/1/0/1 debugging is on
相关命令 : 
debug ipdebug ip interface
## show error packet ip 

show error packet ip 
命令功能 : 
查看IPv4错误报文记录。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show error packet ip 
  [number 
 ＜number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜number＞|每个收包进程显示的错误报文记录个数
缺省 : 
不指定显示个数时，每个收包进程显示10条记录。 
使用说明 : 
指定显示个数时，每个收包进程显示指定个数的记录。 
范例 : 
ZXROSNG(config)# show error packet ipCPU         : MPU-0/20/0Instance ID : 1Seq ID      : 1Record Time : 2016-06-01 14:36:23Interface   : mgmt_ethSource MAC  : 4e:d0:c2:15:9e:4aError Reason: IP version errorPacket Len  : 46Packet      : 0000:55 00 00 1c 00 01 00 00 40 01 20 94 c0 a8 64 01 0010:c0 a8 64 fa 08 00 f7 ff 00 00 00 00 00 00 00 00 0020:00 00 00 00 00 00 00 00 00 00 00 00 00 00 ----------------------------------------------------输出信息中的参数信息解释如下：参数名称           参数说明CPU            错误报文记录所在的Cpu名称Instance ID    收包进程的ID号Seq ID         记录号Record Time    记录时间Interface      收包接口Source MAC     报文中的源MAC地址Error Reason   错误原因Packet Len     报文长度Packet         报文内容
相关命令 : 
error packet ip record 
## show ip pmtu 

show ip pmtu 
命令功能 : 
该命令主要用来显示路由器上IPv4路径MTU相关信息，包括MTU值、剩余老化时间、源IP地址、目的IP地址和VRF名称。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pmtu 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show ip pmtuMTU      Timeout     Src            Dest           Vrfname(Vpnid)600       20m        1.1.1.1        1.2.3.5        zte输出信息中的参数信息解释如下：参数名称      参数说明MTU           路径MTU值Timeout       路径MTU剩余老化时间Src           该路径的源IP地址Dest          该路径的目的IP地址Vrfname       该路径的VRF名称
相关命令 : 
ip path-mtu-discovery age-timer 
## show ip traffic 

show ip traffic 
命令功能 : 
该命令工作于除用户模式之外的所有模式，用于显示IP传输的统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip traffic 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令主要用来显示IP、ICMP、TCP和UDP层的收发以及异常计数。 
范例 : 
ZXROSNG#show ip traffic IP statistics:  Rcvd: 24216 total, 16 local destination        format errors      checksum errors      bad hop count        89                 0                    0                                 unknown protocol        0   Frags:reassembled        timeouts          couldn't reassemble        0                  0                 0                            fragmented         couldn't fragment        0                  0                   Bcast:received           sent        6                  0                   Sent: generated          forwarded         encapsulation failed    no route        10                 24111             24111                   0ICMP statistics:  Rcvd: 10 total        format errors      redirects         unreachable      echo        0                  0                 0                0        echo reply         mask requests     mask replies     quench        10                 0                 0                0        timestamp request  timestamp reply   time exceeded    parameter problem        0                  0                 0                0                            Sent: 10 total        format errors      redirects         unreachable      echo        0                  0                 0                10        echo reply         mask requests     mask replies     quench        0                  0                 0                0        timestamp request  timestamp reply   time exceeded    parameter problem        0                  0                 0                0                UDP statistics:  Rcvd: 6 total, 0 checksum errors, 6 no port  Sent: 0 totalTCP statistics:  Rcvd: 0 total, 0 checksum errors  Sent: 0 total  输出信息中的参数信息解释如下：参数名称                   参数说明IP statistics              IP层的统计信息Rcvd                       收到的IP报文total                      总数local destination          本地报文个数format errors              由于IP头错误（包括版本号错误、IP头部长度错误、IP报文长度错误、IP校验和错误）而丢包的个数checksum errors            由于IP检验和错误而丢包的个数bad hop count              在转发过程中由于IP TTL耗尽而丢包的个数unknown protocol           由于对应的协议没有开启（不在运行）而丢包的个数Frags                      分片报文reassembled                重组成功的报文个数timeouts                   重组超时的报文个数couldn't reassemble        重组失败的报文个数fragmented                 分片成功的报文个数couldn't fragment          分片失败的报文个数Bcast                      广播报文received                   收到的广播报文个数sent                       发送的广播报文个数Sent                       发送的报文generated                  本地发送的个数forwarded                  转发的个数encapsulation failed       在IP封装过程由于某些错误（包括查不到路由、路由类型错误、出接口没有up、源IP地址封装错误）而丢包的个数no route                   由于查不到路由而丢包的个数ICMP statistics            ICMP层的统计信息Rcvd                       收到的ICMP报文total                      总数format errors              由于ICMP头错误（包括长度错误、校验和错误）而丢包的个数redirects                  收到的ICMP重定向报文个数unreachable                收到的ICMP目的不可达报文个数echo                       收到的ICMP回显请求报文个数echo reply                 收到的ICMP回显应答报文个数mask requests              收到的ICMP掩码请求报文个数mask replies               收到的ICMP掩码应答报文个数quench                     收到的ICMP源抑制报文个数timestamp request          收到的ICMP时间戳请求报文个数timestamp reply            收到的ICMP时间戳应答报文个数time exceeded              收到的ICMP超时报文个数parameter problem          收到的ICMP参数错误报文个数Sent                       发送的ICMP报文total                      总数format errors              在ICMP封装过程由于某些错误（申请不到内存）而丢包的个数redirects                  发送的ICMP重定向报文个数unreachable                发送的ICMP目的不可达报文个数echo                       发送的ICMP回显请求报文个数echo reply                 发送的ICMP回显应答报文个数mask requests              发送的ICMP掩码请求报文个数mask replies               发送的ICMP掩码应答报文个数quench                     发送的ICMP源抑制报文个数timestamp request          发送的ICMP时间戳请求报文个数timestamp reply            发送的ICMP时间戳应答报文个数time exceeded              发送的ICMP超时报文个数parameter problem          发送的ICMP参数错误报文个数UDP statistics             UDP层的统计信息Rcvd                       收到的UDP报文个数checksum errors            由于UDP校验和而丢包的个数no port                    由于UDP端口没有开启而丢包的个数TCP statistics             TCP层的统计信息Rcvd                       收到的TCP报文个数checksum errors            由于TCP校验和而丢包的个数no port                    由于TCP端口没有开启而丢包的个数
相关命令 : 
clear ip traffic 
## show ping server 

show ping server 
命令功能 : 
显示PING侦听服务的详细信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ping server 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
* 使用该命令可以分别看到TCP/UDP PING侦听服务开启信息* 在TCP PING服务开启的情况下，使用该命令可以看到TCP PING服务所使用的端口号和侦听端口的状态信息* 在UDP PING服务开启的情况下，使用该命令可以看到UDP PING服务所使用的端口号和侦听端口的状态信息
范例 : 
ZXROSNG#show ping server TCP  Server: DisableUDP  Server: Enable  Port  : 7  Socket: Success
相关命令 : 
无 
## show sockets 

show sockets 
命令功能 : 
该命令工作于除用户模式之外的所有模式，用于显示路由器上的socket信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show sockets 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令主要用来显示路由器上的各个socket信息，包括socket类型、本地IP地址、目的IP地址、状态、实例号以及收发计数。 
范例 : 
ZXROSNG#show socketsProtocol      Local Address    Foreign Address   In    Out   State    InstanceIPv4 TCP      0.0.0.0:23       *:*               0     0     LISTEN    1IPv4 UDP      0.0.0.0:*        *:*               0     0               1IPv4 UDP      0.0.0.0:3784     *:*               0     0               1IPv4 UDP      0.0.0.0:4784     *:*               0     0               1IPv4 UDP      0.0.0.0:3503     *:*               0     0               1IPv4 RAW(112) 0.0.0.0:*        *:*               0     0               1IPv4 RAW(1)   0.0.0.0:*        *:*               10    10              1IPv6 TCP      0:0:0:0:0:0:0:0: *:*               0     0     LISTEN    123IPv6 UDP      0:0:0:0:0:0:0:0: *:*               0     0               13784IPv6 UDP      0:0:0:0:0:0:0:0: *:*               0     0               14784IPv6 UDP      0:0:0:0:0:0:0:0: *:*               0     0               13503IPv6 RAW(112) 0:0:0:0:0:0:0:0: *:*               0     0               1*IPv6 RAW(58)  0:0:0:0:0:0:0:0: *:*               0     0               1TYPE(129)IPv6 RAW(58)  0:0:0:0:0:0:0:0: *:*               0     0               1TYPE(128)IPv4 TCP      0.0.0.0:646      *:*               0     0     LISTEN    1IPv4 UDP      0.0.0.0:646      *:*               0     0               1IPv6 TCP      0:0:0:0:0:0:0:0: *:*               0     0     LISTEN    1646IPv6 UDP      0:0:0:0:0:0:0:0: *:*               0     0               1646输出信息中的参数信息解释如下：参数名称           参数说明Protocol           socket的类型（包括IPv4 TCP、IPv4 UDP、IPv4 RAW、IPv6 TCP、IPv6 UDP和IPv6 Raw）Local Address      本地的IP地址和端口号（:前面的是IP地址，:后面的是端口号,如果是IPv6 RAW,显示的是TYPE字段）Foreign Address    远端的IP地址和端口号（:前面的是IP地址，:后面的是端口号）In                 该socket接收的报文个数Out                该socket发送的报文个数State              如果socket类型为IPv4 TCP或IPv6 TCP， State表示的是连接的状态。状态有LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSING、CLOSEWAIT、LAST-ACK和TIMEWAIT。Instance           socket实例号
相关命令 : 
无 
## trace6 

trace6 
命令功能 : 
该命令在用户模式下执行，用来测试数据包从发送主机到目的地所经过的网关，检测网络连接是否可达。当用ping6命令测试发现网络出现故障后，可以使用trace6测试网络何处有故障。
命令模式 : 
 用户模式  
命令默认权限级别 : 
1 
命令格式 : 
trace6 
  [vrf 
 ＜vrf-name 
＞] ＜ipv6-address 
＞ [{[max-ttl 
 ＜ttl 
＞],[timeout 
 ＜timeout 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：设置目的IP地址或域名所属的VRF名称。取值范围：1~32个字符。默认值：无。
＜ipv6-address＞|作用：设置目的主机的IPv6地址。取值范围：IPV6地址。默认值：无。
＜ttl＞|作用：设置数据包最大生存时间TTL值。取值范围：1~255。默认值：30。
＜timeout＞|作用：设置发送完ECHO-REQUEST报文后，等待ECHO-RESPONSE报文的超时时间，单位为秒。取值范围：1~60秒。默认值：2秒。
缺省 : 
无 
使用说明 : 
* 该命令只能进行简单的连通性检查。如果需要通过trace6操作了解更多网络故障相关信息，请进入命令终端，在特权模式下执行trace6检测。* 如果命令中设置了VRF，则设置的VRF必须是与远端IP地址或域名关联的VRF，否则trace6检测操作失败。* 在发起trace6 检测时，如果指定的远端IP地址或域名不存在，则不能正确诊断网络的连通性。* trace6命令的输出信息包括到达目的地所有网关的IP 地址，如果等待某网关应答超时，则输出“ * * * ”。* 按下Ctrl+C终止trace6检测。
范例 : 
在用户模式下，用trace6命令检测网络节点的连通性：ZXUN>trace6 100::1 max-ttl 1 timeout 1tracing the route to 100:0:0:0:0:0:0:1 over a maximum of 1 hop(s):1 100::1 150 ms 152 ms 153 ms[finished]
相关命令 : 
无 
## trace6 

trace6 
命令功能 : 
跟踪到目的IPV6主机的路径。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
2 
命令格式 : 
trace6 
  [{dcn 
|[vrf 
 ＜vrf name 
＞]}] {＜ipv6-address 
＞|domain 
 ＜domain-name 
＞} [{[pattern 
 ＜pattern-string 
＞],[max-ttl 
 ＜ttl 
＞],[timeout 
 ＜timeout 
＞],[source 
 ＜ipv6-address 
＞],[size 
 ＜datagram-size 
＞],[ttl-mode 
 {pipe 
|uniform 
}],[ecmp 
]}]
命令参数解释 : 
参数|描述
---|---
dcn|DCN VRF
＜vrf name＞|IP地址所属的VRF名称，长度为1-32个字符
＜ipv6-address＞|源IPv6地址
＜domain-name＞|dns域名，长度为1-128个字符
＜pattern-string＞|作用：设置报文填充字节，格式为16进制。取值范围：<0000-FFFF>，长度必须为4个16进制数。默认值：无。
＜ttl＞|设置ttl值，缺省为30，范围：1-255
＜timeout＞|超时时间（单位：秒），缺省为3秒，范围：1-20
＜ipv6-address＞|源IPv6地址
＜datagram-size＞|作用：设置TRACE报文长度，单位是字节。取值范围：36~8192字节。默认值：100字节。
pipe|作用：设置TRACE报文的标签TTL管道模式封装（全255）。
uniform|作用：设置TRACE报文的标签TTL继承IP TTL封装。
ecmp|作用：设置发起多路径PING检测。取值范围：无。默认值：无。
缺省 : 
max-ttl缺省值为30timeout缺省值为3s
使用说明 : 
trace6命令使用ICMPv6差错报文，包括数据包的TTL值耗尽时产生的超时ICMPv6差错报文和到达目的主机后返回的端口不可达ICMP差错报文。trace6命令通过发送TTL值为1的报文启动，引起第一个路由器丢弃该数据报并发送一个超时的ICMPv6差错报文。TTL超时报文表示一个中间路由器收到了该报文并放弃了探测；端口不可达差错报文标志目标节点收到该报文，但由于目的端口号过大无法提交该报文。如果定时器在应答到来之前已经停止，trace6打印一个“*”号。 
范例 : 
ZXROSNG#trace6 100::1 max-ttl 1 timeout 1  tracing the route to 100:0:0:0:0:0:0:1  over a maximum of 1 hop(s):1   100::1 150 ms 152 ms 153 ms [finished]
相关命令 : 
无 
## trace 

trace 
命令功能 : 
该命令在用户模式下执行，用来测试数据包从发送主机到目的地所经过的网关，检测网络连接是否可达。通过分析trace检测结果，可了解网络发生故障的情况。当用ping命令测试发现网络出现故障后，可以使用trace测试网络何处有故障。
命令模式 : 
 用户模式  
命令默认权限级别 : 
1 
命令格式 : 
trace 
  [vrf 
 ＜vrf-name 
＞] ＜ipv4-address 
＞
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：设置目的IP地址或域名所属的VRF名称。取值范围：1~32个字符。默认值：无。
＜ipv4-address＞|作用：设置远端IP地址。取值范围：IPV4地址。默认值：无。
缺省 : 
无 
使用说明 : 
* 该命令只能进行简单的连通性检查。如果需要通过trace操作了解更多网络故障相关信息，请进入命令终端，在特权模式下执行trace检测。* 如果命令中设置了VRF，则设置的VRF必须是与远端IP地址或域名关联的VRF，否则trace检测操作失败。* 在发起trace 检测时，如果指定的远端IP地址不存在，则不能正确诊断网络的连通性。* trace命令的输出信息包括到达目的地所有网关的IP地址，如果等待某网关应答超时，则输出“ * * * ”。* 按下Ctrl+C终止trace检测。
范例 : 
在用户模式下，用trace命令检测网络节点的连通性：ZXUN>trace 10.1.1.2Tracing the route to 10.1.1.2 over a maximum of 30 hop(s):[output interface: gei-0/1/0/4]1 10.1.1.2 36 ms 4 ms 41 ms[finished]ZXUN>
相关命令 : 
无 
## trace 

trace 
命令功能 : 
该命令只能在非用户模式下执行，用来测试数据包从发送主机到目的地所经过的网关，检测网络连接是否可达，通过分析trace检测结果，可了解网络发生故障的情况。当用ping命令测试发现网络出现故障后，可以使用trace测试网络何处有故障。
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
2 
命令格式 : 
trace 
  [{dcn 
 |[vrf 
 ＜vrf-name 
＞]}] {＜ipv4-address 
＞|domain 
 ＜domain-name 
＞} [{[pattern 
 ＜pattern-string 
＞],[source 
 ＜ipv4-address 
＞],[timeout 
 ＜timeout 
＞],[maxttl 
 ＜ttl 
＞],[interface 
 ＜interface-name 
＞],[size 
 ＜datagram-size 
＞],[ttl-mode 
 {pipe 
|uniform 
}],[encapsulated 
 {icmp 
|udp 
}],[next-hop 
 ＜next-hop 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|作用：设置目的IP地址或域名所属的VRF名称。取值范围：1~32个字符。默认值：无。
＜ipv4-address＞|作用：设置发送TRACE报文的源IP地址。取值范围：本端IP地址。默认值：无。
＜domain-name＞|作用：与远端IP等效的域名。取值范围：1~128个字符。
＜pattern-string＞|作用：设置报文填充字节，格式为16进制。取值范围：<0000-FFFF>，长度必须为4个16进制数。默认值：无。
＜ipv4-address＞|作用：设置发送TRACE报文的源IP地址。取值范围：本端IP地址。默认值：无。
＜timeout＞|作用：设置发送完ECHO-REQUEST报文后，等待ECHO-RESPONSE报文的超时时间，单位为秒。取值范围：1~60秒。默认值：2秒。
＜ttl＞|作用：设置数据包最大生存时间TTL值。取值范围：1~255。默认值：30。
＜interface-name＞|作用：指定TRACE报文的发包接口。取值范围：本端接口。默认值：无。
＜datagram-size＞|作用：设置TRACE报文长度，单位是字节。取值范围：36~8192字节。默认值：100字节。
pipe|作用：设置TRACE报文的标签TTL管道模式封装（全255）。
uniform|作用：设置TRACE报文的标签TTL继承IP TTL封装。
icmp|作用：设置TRACE报文封装为ICMP格式。
udp|作用：设置TRACE报文封装为UDP格式。
＜next-hop＞|下一跳IP地址， 取值范围：IPv4地址。 默认值：无。
缺省 : 
无 
使用说明 : 
* 如果命令中设置了VRF，则设置的VRF必须是与远端IP地址或域名关联的VRF，否则trace检测操作失败。* 在发起trace检测时，如果指定的远端IP地址或域名不存在，则不能正确诊断网络的连通性。* trace命令的输出信息包括到达目的地所有网关的IP地址，如果等待某网关应答超时，则输出“ * * * ”。* 按下Ctrl+C终止trace检测。
范例 : 
ZXROSNG#trace 168.1.10.100tracing the route to 168.1.10.1001    168.1.10.100    2 ms  3 ms  5 ms[finished]
相关命令 : 
无 
# 时钟配置命令 
## clock set 

clock set 
命令功能 : 
以标准时间形式设置系统时钟。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
clock set 
  [utc-time 
] ＜current-time 
＞ ＜current-date 
＞
命令参数解释 : 
参数|描述
---|---
utc-time|utc选项，带这个选项时，设置的是utc时间；否则，设置的是本地时间
＜current-time＞|当前时间的时分秒形式，hh:mm:ss
＜current-date＞|当前日期的月日年格式，MM-DD-YY，范围：1-1-2001 到12-31-2037
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#clock set 23:12:01 8-21-2010ZXROSNG#show clock23:12:05 UTC Sat Aug 21 2010
相关命令 : 
show clockshow clock detail
## clock summer-time 

clock summer-time 
命令功能 : 
配置夏令时，使用no命令取消配置 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
clock summer-time 
  ＜timezone-name 
＞ {recurring 
 {{＜start-week 
＞|first 
|last 
} ＜start-day 
＞ ＜start-month 
＞ ＜start-time 
＞ {＜end-week 
＞|first 
|last 
} ＜end-day 
＞ ＜end-month 
＞ ＜end-time 
＞|date 
 ＜start-month 
＞ ＜start-date 
＞ ＜start-time 
＞ ＜end-month 
＞ ＜end-date 
＞ ＜end-time 
＞}|date 
 ＜start-month 
＞ ＜start-date 
＞ ＜start-year 
＞ ＜start-time 
＞ ＜end-month 
＞ ＜end-date 
＞ ＜end-year 
＞ ＜end-time 
＞} [＜offset 
＞ [{positive 
|negative 
}]]
no clock summer-time 
命令参数解释 : 
参数|描述
---|---
＜timezone-name＞|时区名；长度：1~9
recurring|循环模式
＜start-week＞|每月的周。 1－5：第一个～第五个。
first|每月中的第一周。
last|每月中的最后一周。
＜start-day＞|每周中的天。 Sun. 周日 Mon. 周一 Tue. 周二 Wed. 周三 Thu. 周四 Fri. 周五 Sat. 周六
＜start-month＞|开始月份。1-12
＜start-time＞|开始时间。
＜end-week＞|每月的周。 1－5：第一个～第五个。
first|每月中的第一周。
last|每月中的最后一周。
＜end-day＞|每周中的天。 Sun. 周日 Mon. 周一 Tue. 周二 Wed. 周三 Thu. 周四 Fri. 周五 Sat. 周六
＜end-month＞|结束月份。
＜end-time＞|结束时间
date|表示对具体的夏令时间进行设置。
＜start-month＞|开始月份。1-12
＜start-date＞|开始日期。范围1~31
＜start-time＞|开始时间。
＜end-month＞|结束月份。
＜end-date＞|结束日期
＜end-time＞|结束时间
date|表示对具体的夏令时间进行设置。
＜start-month＞|开始月份。1-12
＜start-date＞|开始日期。范围1~31
＜start-year＞|开始年份。范围2000～2037。
＜start-time＞|开始时间。
＜end-month＞|结束月份。
＜end-date＞|结束日期
＜end-year＞|结束年份。
＜end-time＞|结束时间
＜offset＞|夏令时时差。指夏令时开始时增加的分钟数，范围1～240，单位为分钟，缺省为60分钟。
positive|正时间偏差
negative|负时间偏差
缺省 : 
无 
使用说明 : 
该命令用于配置夏令时，系统按照设置的日期和时间自动切换到夏令时。no命令用于删除已配置夏令时。系统只能配置一个夏令时，多次配置时，仅最后一次配置的生效。如果夏令时生效中修改配置，则系统自动按照新配置决定是否进入夏令时或退出夏令时。命令中前半部分<week> <day> <month> <hh:mm>表示起始时间，后半部分<week> <day> <month> <hh:mm>表示结束时间。时间偏差符号默认为正。配置的offset符号为负时，表示设置的冬令时。配置生效规则同夏令时。 
范例 : 
ZXROSNG(config)#clock summer-time zzz recurring first Fri Apr 10:00 1 Fri Oct 10:00 10 negativeZXROSNG#show clock detail07:02:53 zzz Mon May 11 2015Time source is hardware calendarSummer time starts 10:00:00 UTC Fri Apr 3 2015Summer time ends 10:00:00 UTC Fri Oct 2 2015ZXROSNG#
相关命令 : 
show clock detailshow running-config clock-mgr
## clock sync-source ntp 

clock sync-source ntp 
命令功能 : 
配置NTP的优先级。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
clock sync-source ntp 
 priority 
 ＜priority 
＞
no clock sync-source ntp 
命令参数解释 : 
参数|描述
---|---
＜priority＞|＜priority＞ 优先级大小，1~10
缺省 : 
缺省条件下默认为$#35913731#$。 
使用说明 : 
优先级取值越小表示优先级越高，10表示不参与时钟源选择。除优先级10外，设置时钟源的优先级不能相同。 
范例 : 
配置NTP的优先级大小：ZXROSNG(config)#clock sync-source ntp priority 4ZXROSNG(config)#
相关命令 : 
show clock sync-source 
## clock sync-source ptp 

clock sync-source ptp 
命令功能 : 
配置PTP的优先级。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
clock sync-source ptp 
 priority 
 ＜priority 
＞
no clock sync-source ptp 
命令参数解释 : 
参数|描述
---|---
＜priority＞|＜priority＞ 优先级大小，1~10
缺省 : 
缺省条件下默认为$#35913730#$。 
使用说明 : 
优先级取值越小表示优先级越高，10表示不参与时钟源选择。除优先级10外，设置时钟源的优先级不能相同。 
范例 : 
ZXROSNG(config)#clock sync-source ptp priority 5ZXROSNG(config)#
相关命令 : 
show clock sync-source 
## clock sync-threshold maximum 

clock sync-threshold maximum 
命令功能 : 
配置offset的门限。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
clock sync-threshold maximum 
  ＜threshold-value 
＞
no clock sync-threshold maximum 
命令参数解释 : 
参数|描述
---|---
＜threshold-value＞|门限大小，500~86400000
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置offset门限大小：ZXROSNG(config)#clock sync-threshold maximum 500ZXROSNG(config)#
相关命令 : 
clock sync-threshold-switch  
## clock sync-threshold-switch 

clock sync-threshold-switch 
命令功能 : 
初始化门限。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
clock sync-threshold-switch 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#clock sync-threshold-switch ZXROSNG(config)#
相关命令 : 
clock sync-threshold maximum 
## clock timezone 

clock timezone 
命令功能 : 
配置时区信息。使用no命令取消配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
clock timezone 
  ＜timezone-name 
＞ ＜hours-offset 
＞ [＜minutes-offset 
＞]
no clock timezone 
命令参数解释 : 
参数|描述
---|---
＜timezone-name＞|时区名：1~32
＜hours-offset＞|时区小时偏移，范围：-12~14
＜minutes-offset＞|时区分钟偏移，范围：0~59
缺省 : 
无 
使用说明 : 
使用该命令配置时区后，必须退到特权模式执行write命令，提示写库成功后才可以在重启上电之后依然保留该时区信息，否则时区信息在重启后丢失。 
范例 : 
设置系统时区为北京时区，时区偏移8小时：ZXROSNG(config)#clock timezone Beijing 8
相关命令 : 
show clockshow clock detailshow running-config clock-mgr
## show clock detail 

show clock detail 
命令功能 : 
显示详细的系统时钟信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show clock detail 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show clock detail 19:00:33 CHINA Sat Jan 19 2008Time source is hardware calendar Timezone: CHINA(480 minutes from UTC)Summer time starts 12:00:00 CHINA Oct 1 2011Summer time ends 00:00:00 ZTE+8 Nov 2 2011
相关命令 : 
clock setclock timezoneclock summer-timer
## show clock sync-source 

show clock sync-source 
命令功能 : 
显示时钟源的优先级和有效性。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show clock sync-source 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示时钟源的优先级以及有效性，其中Valid值为1时表示时钟源有效，可以参与系统时钟的选择。当前源的选择规则为：优先级高且有效。 
范例 : 
ZXROSNG(config)#show clock sync-source Type      Priority    Valid  NTP        3           1PTP        5           0
相关命令 : 
clock sync-source ntpclock sync-source ptp
## show clock 

show clock 
命令功能 : 
显示系统时钟 
命令模式 : 
 用户模式  
命令默认权限级别 : 
1 
命令格式 : 
show clock 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show clock12:54:38 UTC Sat Aug 21 2010 
相关命令 : 
clock setshow clock detail
## show clock 

show clock 
命令功能 : 
显示系统时钟信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show clock 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show clock12:54:38 UTC Sat Aug 21 2010 
相关命令 : 
clock setshow clock detail
# 文件系统配置命令 
## cd 

cd 
命令功能 : 
此命令工作于特权模式，用于更改当前工作目录。工作目录包含目录所在路径和单板信息。当用户需要查看或操作其他目录下的文件时，可以使用该命令切换工作目录。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
cd 
  ＜directory 
＞ [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜directory＞|当前工作目录，配置时可以指定为路径/目录名称的形式，长度为1~159位的字符串；也可仅指定目录名称，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的路径名作为切换的目标目录
＜cpu-name＞|单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
cd 命令设置某一用户的当前工作目录。用户未更改当前目录前，当前工作目录（包括单板信息）在上电初始化时，系统从产品管理模块自动获取。cd指定的工作目录支持完整的路径名和不完整的路径名。当指定路径为完整的路径名（以 / 开头，表示根目录），直接作为切换的工作目录。当指定路径为不完整的路径名，则以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的路径名，切换到指定目录。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，需要切换到MPU-0/20/0:/datadisk0/LOG目录下，可以进行如下两种操作切换到目标目录：1）指定参数为完整的路径名，cd /datadisk0/LOG MPU-0/20/0或cd /datadisk0/LOG，不指定单板信息时默认为当前工作目录所在单板，即MPU-0/20/0所在单板。2）指定参数为不完整的路径名，cd LOG MPU-0/20/0或cd LOG，不指定单板信息时默认为当前工作目录所在单板，即MPU-0/20/0所在单板。此时将当前工作目录拼接上用户输入的路径名作为目标目录，即/datadisk0拼接上LOG，将拼接后的目录/datadisk0/LOG作为切换的目标目录。用户当前的工作目录可以通过pwd命令查看。
范例 : 
1.进入当前单板的/sysdisk0目录。命令如下：ZXROSNG#cd /sysdisk0查看当前工作目录。命令如下：ZXROSNG#pwdMPU-0/20/0: /sysdisk02.进入MPU-0/20/0所在单板的/datadisk0目录。命令如下：ZXROSNG#cd /datadisk0 MPU-0/20/0查看当前工作目录。命令如下：ZXROSNG#pwdMPU-0/20/0: /datadisk0
相关命令 : 
无。 
## cp 

cp 
命令功能 : 
此命令工作于特权模式，用于将一个文件从源目录拷贝到目标目录。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
cp 
  ＜source-file 
＞ [＜src-cpu-name 
＞] ＜destination-file 
＞ [＜dest-cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜source-file＞|源文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；也可仅指定为源文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的源文件信息
＜src-cpu-name＞|源文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
＜destination-file＞|目标文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；也可仅指定为目标文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的目标文件信息
＜dest-cpu-name＞|目标文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
cp命令通过指定单板信息，支持不同单板间的文件拷贝。cp命令指定的文件路径（包括源文件和目标文件）支持完整的路径名和不完整的路径名。完整的路径名以“ /”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的文件信息。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要将/datadisk0/LOG目录下的a.txt文件拷贝到/sysdisk0下，则用户可以指定源文件参数为完整的路径名，即/datadisk0/LOG/a.txt；也可以指定不完整的路径名，即LOG/a.txt，此时将/datadisk0拼接上LOG/a.txt，把/datadisk0/LOG/a.txt作为完整的源文件信息。
范例 : 
1.把当前目录/datadisk0下的test.txt文件拷贝到当前/datadisk0目录，目标文件名为test2.txt。命令如下： ZXROSNG#pwdMPU-0/20/0: /datadisk0ZXROSNG#cp test.txt test2.txtCopy file successfully. 2.把/datadisk0/test.txt文件拷贝到/datadisk0/test2/目录下，目标文件名为test.txt。命令如下：ZXROSNG#cp /datadisk0/test.txt /datadisk0/test2/test.txtCopy file successfully.3.把MPU-0/20/0所在单板的/datadisk0/test.txt文件拷贝到MPU-0/21/0所在单板的/datadisk0/test2/目录下，目标文件名为test2.txt。命令如下：ZXROSNG#cp /datadisk0/test.txt MPU-0/20/0 /datadisk0/test2/test2.txt MPU-0/21/0 Copy file successfully.
相关命令 : 
无。 
## delete 

delete 
命令功能 : 
此命令工作于特权模式，用于删除目录下的文件。对于设备上的临时文件或已经废弃的文件，用户可以执行该命令进行删除。对于某些重要文件，删除前请注意备份。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
delete 
  ＜filename 
＞ [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜filename＞|删除文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；也可仅指定为文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的文件信息
＜cpu-name＞|文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
delete命令删除某目录下的文件，文件信息包含文件所在路径和单板信息。delete命令指定的文件路径支持完整的路径名和不完整的路径名。完整的路径名以 “/”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的文件信息。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要删除/datadisk0/LOG目录下的a.txt文件，则用户可以指定文件参数为完整的路径名，即/datadisk0/LOG/a.txt；也可以指定为不完整的路径名，即LOG/a.txt，此时将/datadisk0拼接上LOG/a.txt，把/datadisk0/LOG/a.txt作为完整的待删除文件信息。
范例 : 
1.删除当前目录下的文件，不指定CPU名称时默认为当前单板中的文件。命令如下：ZXROSNG#delete test.txtAre you sure to delete file(s)?[yes/no]:yDelete file(s) successfully.2.删除当前单板的/datadisk0/test.txt文件。命令如下：ZXROSNG#delete /datadisk0/test.txt Are you sure to delete file(s)?[yes/no]:yDelete file(s) successfully.3.删除MPU-0/20/0所在单板的/datadisk0/test.txt文件。命令如下：ZXROSNG#delete /datadisk0/test.txt MPU-0/20/0Are you sure to delete file(s)?[yes/no]:yDelete file(s) successfully.
相关命令 : 
无。 
## dir 

dir 
命令功能 : 
此命令工作于特权模式，用于显示目录下的文件信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
dir 
  [＜filename-or-directory 
＞ [＜cpu-name 
＞]]
命令参数解释 : 
参数|描述
---|---
＜filename-or-directory＞|待查看的文件或目录名称：参数为文件时可以指定为路径/文件名的形式，长度为1~159位的字符串；也可仅指定为文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的文件信息。参数为目录时可以指定为路径/目录名称的形式，长度为1~159位的字符串；也可仅指定为目录名称，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的目录名称作为完整的目录信息
＜cpu-name＞|目录所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
dir命令用于查看指定目录下的文件信息，指定目录包含文件所在路径和单板信息。dir命令指定的文件路径支持完整的路径名和不完整的路径名。完整的路径名以“ /”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的路径名。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要查看/datadisk0/LOG目录下的文件信息，则用户可以指定参数为完整的路径名，即/datadisk0/LOG；也可以指定为不完整的路径名，即LOG，此时将/datadisk0拼接上LOG，把/datadisk0/LOG作为完整的待查看目录。
范例 : 
1. 显示当前目录下的文件信息，不指定CPU名称时默认为查看当前单板中的文件。命令如下：ZXROSNG#dirDirectory of MPU-0/20/0: /datadisk0/LOG/ALARM8792184  KB total (903372 KB free)        attribute   size       date        time         name1       <DIR>    4096      01-09-2014  13:07        .2       <DIR>    4096      01-09-2014  13:07        ..3       ----       8041      01-16-2014  10:18        alarmlog_20140109210707_                                                     0.alm.log参数说明如下：参数名称    参数说明attribute    属性信息，<DIR>表示目录，----表示非目录size    文件或目录大小date    文件或目录最近一次被修改的日期time    文件或目录最近一次被修改的时间name    文件或目录名称2．显示当前所在单板当前目录下的2.dat文件信息。命令如下：ZXROSNG#dir 2.datDirectory of MPU-0/20/0: /datadisk0/2.dat8792184  KB total (906804 KB free)        attribute   size       date        time         name1       ----       9597      01-09-2014  06:59        2.dat3. 显示当前单板/datadisk0/LOG目录下的文件信息。命令如下：ZXROSNG#dir /datadisk0/LOGDirectory of MPU-0/20/0: /datadisk0/LOG8792184  KB total (906800 KB free)        attribute   size       date        time         name1       <DIR>    4096      08-06-2013  06:13        .2       <DIR>    4096      08-06-2013  06:13        ..3       <DIR>    4096      08-06-2013  06:13        SERVICE4       <DIR>    4096      08-06-2013  06:13        PORTAL5       <DIR>    4096      01-09-2014  10:37        BRAS6       <DIR>    4096      01-09-2014  13:07        ALARM4. 显示MPU-0/20/0所在单板的/datadisk0/LOG/ALARM目录下的文件信息。命令如下：ZXROSNG#dir /datadisk0/LOG/ALARM MPU-0/20/0Directory of MPU-0/20/0: /datadisk0/LOG/ALARM8792184  KB total (906800 KB free)        attribute   size       date        time         name1       <DIR>     4096     01-09-2014  13:07        .2       <DIR>     4096     01-09-2014  13:07        ..3       ----        7066     01-16-2014  03:49        alarmlog_20140109210707_                                                        0.alm.log
相关命令 : 
无。 
## format 

format 
命令功能 : 
此命令工作于特权模式，用于格式化目录。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
format 
 /datadisk0 
 [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
/datadisk0|格式化目录的名称。仅支持格式化非系统目录/datadisk0下的数据。
＜cpu-name＞|格式化目录所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
format命令用于格式化指定的目录，目录信息包含目录所在路径和单板信息。目前支持格式化的目录只有/datadisk0。对于格式化目录下的重要文件，格式化操作前请注意备份。
范例 : 
1.格式化目录/datadisk0，不指定CPU时默认为当前单板的目录。命令如下：ZXROSNG#format /datadisk0 All data will be cleared.Continue to format? [yes/no]:yFormat successfully.2. 格式化MPU-0/20/0所在单板下的/datadisk0目录。命令如下：ZXROSNG#format /datadisk0 MPU-0/20/0 All data will be cleared.Continue to format? [yes/no]:yFormat successfully.
相关命令 : 
无。 
## mkdir 

mkdir 
命令功能 : 
此命令工作于特权模式，用于创建目录，存放各种文件。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
mkdir 
  ＜directory 
＞ [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜directory＞|目录信息，配置时可以指定为路径/目录名称的形式，长度为1~159位的字符串；也可仅指定为目录名称，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的目录名称作为完整的目录信息
＜cpu-name＞|待创建目录所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
mkdir命令用于创建目录，目录信息包含目录所在路径和单板信息。mkdir命令指定的目录路径支持完整的路径名和不完整的路径名。完整的路径名以 “/”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的路径名。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要在/datadisk0/LOG目录下创建test目录，则用户可以指定参数为完整的路径名，即/datadisk0/LOG/test；也可以指定为不完整的路径名，即LOG/test，此时将/datadisk0拼接上LOG/test，把/datadisk0/LOG/test作为完整的目录。目录是否成功创建可以通过dir命令查看。
范例 : 
1.在当前目录下创建ss目录，不指定CPU时默认为在当前单板下创建目录。命令如下：ZXROSNG#mkdir ss查看当前目录下是否成功创建ss目录。命令如下：ZXROSNG#dirDirectory of MPU-0/20/0: /datadisk0/LOG/ALARM8792184  KB total (903364 KB free)        attribute   size       date        time         name1       <DIR>    4096      01-17-2014  03:33        .2       <DIR>    4096      01-17-2014  03:33        ..3       <DIR>    4096      01-17-2014  03:33        ss2.在MPU-0/20/0所在单板的/datadisk0下创建test目录。命令如下：ZXROSNG#mkdir /datadisk0/test MPU-0/20/0查看MPU-0/20/0所在单板的/datadisk0下是否成功创建test目录。命令如下：ZXROSNG#dir /datadisk0 MPU-0/20/0Directory of MPU-0/20/0: /datadisk08792184  KB total (903364 KB free)        attribute   size       date        time         name1       <DIR>    4096      01-17-2014  03:33        .2       <DIR>    4096      01-17-2014  03:33        ..3       <DIR>    4096      01-17-2014  03:33        test
相关命令 : 
无。 
## more 

more 
命令功能 : 
此命令工作于特权模式，用于显示文件内容。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
more 
  ＜filename 
＞ [＜cpu-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜filename＞|文件信息，配置时可以指定为路径/文件名称的形式，长度为1~159位的字符串；也可仅指定为文件名称，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名称作为完整的文件信息
＜cpu-name＞|文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
more命令显示指定文件内容，文件信息包含文件所在的路径和单板信息。more命令指定的文件路径支持完整的路径名和不完整的路径名。完整的路径名以 “/”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的文件目录。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要查看文件/datadisk0/LOG/a.txt的内容，则用户可以指定参数为完整的路径名，即/datadisk0/LOG/a.txt；也可以指定为不完整的路径名，即LOG/a.txt，此时将/datadisk0拼接上LOG/a.txt，把/datadisk0/LOG/a.txt作为完整的文件信息。
范例 : 
1.显示当前单板当前目录下的test2.txt文件内容。命令如下：ZXROSNG#more test2.txthello world!cmd "more" testtest---file end!1.查看MPU-0/20/0所在单板的/datadisk0/test2.txt文件的内容。命令如下：ZXROSNG#more /datadisk0/test2.txt MPU-0/20/0hello world!cmd "more" testtest---file end!
相关命令 : 
无。 
## mount 

mount 
命令功能 : 
此命令工作于特权模式，用于加载外部存储设备。用户可以使用外部存储设备对设备上的重要数据信息进行备份，如set集（版本启动文件）或配置文件等信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
mount 
  {harddisk 
|cf-card 
|usb1 
|usb2 
} [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
harddisk|存储设备名称，属于硬盘类型
cf-card|存储设备名称，属于CF卡类型
usb1|存储设备名称，属于USB类型
usb2|存储设备名称，属于USB类型
＜cpu-name＞|设备所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
mount命令用于加载指定的存储设备，存储设备信息包含设备名称和设备所在单板信息。目前支持加载的存储设备有harddisk、cf-card、usb1和usb2。
范例 : 
加载MPU-0/11/0所在单板上的USB1设备。命令如下：ZXROSNG#mount usb1 MPU-0/11/0 MPU-0/11/0: usb1 mounted successfully!
相关命令 : 
umount {cf-card | harddisk | usb1 | usb2} [<cpu-name>] 
## pwd 

pwd 
命令功能 : 
此命令工作于特权模式，用于显示当前工作目录。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
pwd 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
无。 
范例 : 
显示当前工作路径：ZXROSNG#pwdMPU-0/20/0: /datadisk0
相关命令 : 
无。 
## rename 

rename 
命令功能 : 
此命令工作于特权模式，用于更改指定文件或文件夹名称。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
rename 
  ＜old-name 
＞ [＜cpu-name 
＞] ＜new-name 
＞
命令参数解释 : 
参数|描述
---|---
＜old-name＞|指定要修改的文件、文件夹名称：参数为文件时可以指定为路径/文件名称的形式，长度为1~159位的字符串；也可仅指定为文件名称，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名称作为完整的文件信息；参数为文件夹时可以指定为路径/文件夹名称的形式，长度为1~159位的字符串；也可仅指定为文件夹名称，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件夹名称作为完整的文件夹信息；
＜cpu-name＞|文件或文件夹所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
＜new-name＞|目标文件或文件夹名称，长度为1~79位的字符串
缺省 : 
无。 
使用说明 : 
rename命令用于更改文件或文件夹名称，文件或文件夹名称信息包含路径和单板信息。rename命令指定的路径支持完整的路径名和不完整的路径名。完整的路径名以“ /”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的文件路径。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要重命名文件/datadisk0/LOG/a.txt，则用户可以指定参数为完整的路径名，即/datadisk0/LOG/a.txt；也可以指定为不完整的路径名，即LOG/a.txt，此时将/datadisk0拼接上LOG/a.txt，把/datadisk0/LOG/a.txt作为完整的文件信息。
范例 : 
1.将文件夹test改名为test_new。命令如下：ZXROSNG#rename test test_newRename successfully. 2.将文件test.txt改名为1.txt。命令如下：ZXROSNG#rename test.txt 1.txtRename successfully.3.将MPU-0/20/0上的文件1.txt改名为test.txt。命令如下：ZXROSNG#rename /datadisk0/1.txt MPU-0/20/0 test.txtRename successfully.
相关命令 : 
无。 
## rmdir 

rmdir 
命令功能 : 
命令工作于特权模式，用于删除目录。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
rmdir 
  ＜directory 
＞ [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜directory＞|目录信息，配置时可以指定为路径/目录名称的形式，长度为1~159位的字符串；也可仅指定为目录名称，长度为1~79位的字符串
＜cpu-name＞|目录所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
rmdir命令用于删除目录，目录信息包含目录所在路径和单板信息。rmdir命令指定的目录路径支持完整的路径名和不完整的路径名。完整的路径名以 “/”开头。对于不完整的路径名，以当前工作目录为根目录，加“/”拼接上用户输入的路径名作为完整的路径名，把它作为待删除的目录。如当前用户所在的工作目录为：MPU-0/20/0: /datadisk0，用户需要删除目录/datadisk0/LOG/test，则用户可以指定参数为完整的路径名，即/datadisk0/LOG/test；也可以指定为不完整的路径名，即LOG/test，此时将/datadisk0拼接上LOG/test，把/datadisk0/LOG/test作为完整的目录信息。rmdir命令指定的要删除目录必须是空目录，否则删除失败。
范例 : 
1.删除空目录test，不指定CPU时默认为在当前单板的目录。命令如下：ZXROSNG#rmdir testAre you sure to remove this directory?[yes/no]:yRmdir successfully.2.删除MPU-0/20/0所在单板的空目录test1。命令如下：ZXROSNG#rmdir test1 MPU-0/20/0 Are you sure to remove this directory?[yes/no]:yRmdir successfully.3.删除非空目录test。命令如下：ZXROSNG#rmdir testAre you sure to remove this directory?[yes/no]:y%Error 45517: The directory is not empty!
相关命令 : 
无。 
## show filesystem 

show filesystem 
命令功能 : 
此命令工作于除用户模式外的其他所有模式，用于显示文件系统可操作存储设备信息，如harddisk、cf-card、USB等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show filesystem 
  [{＜cpu-name 
＞|all 
}] 
命令参数解释 : 
参数|描述
---|---
＜cpu-name＞|设备所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
all|显示所有单板的可操作存储设备信息
缺省 : 
无。 
使用说明 : 
show filesystem命令可以显示指定单板或所有单板的可操作设备信息。 
范例 : 
1.显示当前单板可操作存储设备信息。命令如下：ZXROSNG#show filesystemMPU-0/20/0:    /sysdisk0    /datadisk02.显示所有单板可操作存储设备信息。命令如下：ZXROSNG#sho filesystem allMPU-0/12/0:    /sysdisk0    /datadisk0    /cf:1    /cf:2MPU-0/11/0:    /sysdisk0    /datadisk0    /cf:1    /cf:23.显示MPU-0/11/0所在单板的可操作存储设备信息。命令如下：ZXROSNG#show filesystem MPU-0/11/0MPU-0/11/0:    /sysdisk0    /datadisk0    /cf:1    /cf:2
相关命令 : 
无 
## umount 

umount 
命令功能 : 
此命令工作于特权模式，用于卸载存储设备。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
umount 
  {harddisk 
|cf-card 
|usb1 
|usb2 
} [＜cpu-name 
＞]
命令参数解释 : 
参数|描述
---|---
harddisk|存储设备名称，属于硬盘类型
cf-card|存储设备名称，属于CF卡类型
usb1|存储设备名称，属于USB类型
usb2|存储设备名称，属于USB类型
＜cpu-name＞|存储设备所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
缺省 : 
无。 
使用说明 : 
umount命令用于卸载指定的存储设备，存储设备信息包含设备名称和设备所在单板信息。目前支持卸载的存储设备有harddisk、cf-card、usb1和usb2。umount命令卸载指定的存储设备时，必须确保无用户正使用该存储设备，否则卸载失败。
范例 : 
卸载MPU-0/11/0所在单板上的USB1设备。命令如下：ZXROSNG#umount usb1 MPU-0/11/0 MPU-0/11/0: usb1 unmounted successfully!
相关命令 : 
mount {cf-card | harddisk | usb1 | usb2} [<cpu-name>] 
## unzip 

unzip 
命令功能 : 
解压缩.zip格式的文件。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
unzip 
  [＜src-cpu-name 
＞] ＜source-file 
＞ [[＜dst-cpu-name 
＞] ＜destination-file 
＞]
命令参数解释 : 
参数|描述
---|---
＜src-cpu-name＞|源文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
＜source-file＞|源文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；仅指定为源文件名，长度为1~79位的字符串
＜dst-cpu-name＞|目标文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
＜destination-file＞|目标文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；仅指定为目标路径名，长度为1~79位的字符串，此时目标文件名同源文件名；
缺省 : 
无 
使用说明 : 
1.仅指定为源文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的源文件信息；解压缩后源文件继续保留。2.仅指定为目标路径名，长度为1~79位的字符串，此时目标文件名为source-file（若源文件名source-file.zip）；3.可仅指定为目标文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的目标文件信息；4.可以不指定目的文件路径，此时在源文件路径下生成source-file（若源文件名source-file.zip）；5.解压缩到同一个目录，报错。例如：unzip a.zip a.zip 报解压缩失败6.解压缩源文件目录和目的文件目录不同，允许名称一致例如： unzip /datadisk0/a.zip  /datadisk0/1/a.zip7.解压缩时，若.zip文件是多个文件的压缩文件，只允许指定到目录，不能修改名称。  例如  33.zip包含了3个文件。 unzip 33.zip 123 此时报%Error 45548: The compressed file contains directories or multiple files. Please specify destination folder.8.解压缩时，若.zip仅包含一个文件，可以修改文件名，也可以指定解压到某一路径。9.解压之后文件名长度为79或者文件绝对路径超过159，会提示%Error 45551: The directory or file name is too long after being decompressed.10.解压缩时，如果指定目的的文件目录不存在，报错。%Error 16: No such file(s) or directory(s).11.文件目录已经存在，指定时目的文件时，和目录同名ZXROSNG#unzip aa.zip test.此时test是文件目录。名称和目录名一致报错,45549: The specified file name is the same as the existing path name.12.待解压的文件中，包含文件夹，无论文件夹是空还是有文件，都不允许修改名称。13.待解压的文件中，解压之后文件路径超过10层报错ZXROSNG#unzip 10.zip  说明：10.zip解压之后文件路径超过10层。%Error 31: Cannot operate a directory deeper than 10 levels.14.待解压的文件中，如果包含文件系统不能管理的目录或者文件，报错15.解压文件时，指定目的文件目录没有权限，报错如下：%Error 45527: The operation to the directory/file is forbidden or directory/file is error
范例 : 
解压缩文件examplefile.zip到当前文件路径:ZXROSNG#unzip examplefile.zip压缩文件importfile.zip到/datadisk0/myfile/下：ZXROSNG#unzip  MPU-0/21/0 importfile.zip MPU-0/21/0 /datadisk0/myfile/ 
相关命令 : 
zip 
## zip 

zip 
命令功能 : 
用于文件压缩 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
zip 
  [＜src-cpu-name 
＞] ＜source-file 
＞ [[＜dst-cpu-name 
＞] ＜destination-file 
＞]
命令参数解释 : 
参数|描述
---|---
＜src-cpu-name＞|源文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
＜source-file＞|源文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；仅指定为源文件名，长度为1~79位的字符串
＜dst-cpu-name＞|目标文件所在单板CPU名称，用于标识单板信息。不设置时，默认操作当前单板
＜destination-file＞|目标文件信息，配置时可以指定为路径/文件名的形式，长度为1~159位的字符串；仅指定为目标路径名，长度为1~79位的字符串，此时目标文件名同源文件名；
缺省 : 
无 
使用说明 : 
1.仅指定为目标文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的目标文件信息；也可以不指定该信息，此时在源文件路径下生成source-file.zip；压缩后的文件，默认补上 .zip后缀。比如1.txt文件压缩不指定目的文件名，压缩之后的名称为1.txt.zip。2. 源文件路径不允许是文件夹，只能指定到文件。3.仅指定为源文件名，长度为1~79位的字符串，此时把当前用户所在工作目录，以“/”拼接上用户输入的文件名作为完整的源文件信息；压缩后源文件继续保留.4.压缩源文件和目的文件名相同且源文件和目的文件在同一个目录，报错。例如：zip a  a 报压缩失败.5.压缩源文件目录和目的文件目录不同，允许名称一致例如：zip /datadisk0/a.txt  /datadisk0/test/a.txt6.不支持压缩文件夹。不支持压缩多个文件。7.压缩文件名长度为79时或者文件绝对路径超过159，会提示%Error 45550: The directory or file name is too long after being compressed.8.压缩时，如果指定目的的文件目录不存在。报错%Error 16: No such file(s) or directory(s).9.压缩时，文件目录已经存在，指定时目的文件时，和目录同名ZXROSNG#zip test.txt /datadisk0.报错%Error 45549: The specified file name is the same as the existing path name.10.若压缩到指定的文件目录没有写权限，报错如下：%Error 45527: The operation to the directory/file is forbidden or directory/file is error.
范例 : 
压缩文件examplefile.txt:ZXROSNG#zip examplefile.txt压缩文件test.c到/datadisk0/myfile/下：ZXROSNG#zip MPU-0/21/0 test.txt MPU-0/21/0 /datadisk0/myfile/
相关命令 : 
unzip 
# 系统基本配置命令 
## auto-write cpu-limit 

auto-write cpu-limit 
命令功能 : 
用来设置系统定时保存配置时系统CPU使用率上限。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-write cpu-limit 
  ＜threshold-value 
＞ [interval 
 ＜interval-time 
＞]
no auto-write cpu-limit 
命令参数解释 : 
参数|描述
---|---
＜threshold-value＞|指定CPU使用率上限。整数形式，取值范围是1～90，单位：百分率。
＜interval-time＞|指定保存时CPU达到配置上限，系统再次保存的延时时间。整数形式，取值范围是1～60，单位是分钟。
缺省 : 
系统定时保存配置不受系统CPU使用率限制。 
使用说明 : 
为了防止自动保存影响系统性能，可以配置参数cpu-limit threshold-value自动保存时系统CPU使用率上限。在自动保存定时器触发时，检测到系统的CPU占用率高于配置的值，系统将延时本次保存，延时时间间隔由interval interval-time指定，该延时时间循环生效。如果没有配置interval interval-time，自动保存时CPU占用率高于配置的值，将取消本次配置保存。缺省情况下，延时时间间隔不生效。 如果执行命令no auto-write cpu-limit，表示取消CPU使用率限制。
范例 : 
配置系统配置自动保存时CPU使用率上限为60%，达到上限后延时3分钟保存。ZXROSNG(config)#auto-write cpu-limit 60 interval 3
相关命令 : 
auto-write 
## auto-write 

auto-write 
命令功能 : 
用来设置系统定时保存配置的功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-write 
  {delay 
 ＜delay-time 
＞|everyday 
 ＜everyday-time 
＞}
no auto-write 
命令参数解释 : 
参数|描述
---|---
＜delay-time＞|指定配置变更发生后，系统自动保存配置的延时时间。整数形式，取值范围是1～60，单位是分钟。
＜everyday-time＞|指定每天定时保存的时间点，格式是hh:mm:ss。
缺省 : 
系统不启动自动保存功能。 
使用说明 : 
如果需要指定系统自动备份配置的延时时间，则选择参数delay delay-time，系统将在到达配置发生变更后的指定延时时间后自动保存配置。如果需要指定每天定时保存的时间点，则指定参数everyday everyday-time。实际保存的时间点可能比配置的时间点延后，滞后范围为5分钟。如果执行命令no auto-write，表示去使能自动保存功能。
范例 : 
配置系统配置发生变化5分钟后自动保存ZXROSNG(config)#auto-write delay 5 配置系统每天12:00:00自动保存ZXROSNG(config)#auto-write everyday 12:00:00 
相关命令 : 
auto-write cpu-limit 
## cmdgroup 

cmdgroup 
命令功能 : 
本命令在全局配置模式下执行，用于配置命令组功能。使用no命令删除配置的命令组。通过commands命令配置命令组下命令的匹配规则。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
cmdgroup 
  ＜cmdgroup 
＞
no cmdgroup 
  ＜cmdgroup 
＞
				
命令参数解释 : 
参数|描述
---|---
＜cmdgroup＞|命令组名，1~31个字符
缺省 : 
无 
使用说明 : 
    如果配置的命令组当前系统中不存在，默认创建对应的命令组并进入对应的命令组模式。    如果配置的命令组已经存在，则直接进入对应的命令组模式。    当定义的命令组数量超过系统允许的容量时，提示配置失败。    配置命令组后，通过local-cmdgroup命令与用户授权模板进行绑定，实现对用户权限的管理。
范例 : 
创建新的名为first的用户组，同时进入自定义命令组模式：ZXROSNG(config)#cmdgroup firstZXROSNG(config-cmdgrp)#删除已经创建的名为first的命令组：ZXROSNG(config)#no cmdgroup firstZXROSNG(config)#删除当前设备上不存在的cmd命令组，提示该命令组不存在：ZXROSNG(config)#no cmdgroup cmd%Info 90: The config does not existZXROSNG(config)#
相关命令 : 
show running-config oam 
## command-authorization 

command-authorization 
命令功能 : 
用于配置基于用户权限级别的命令授权策略。配置后，对应权限级别的用户在用户模式、特权模式或者全局配置模式（可选）下执行命令时，需要进行命令鉴权，鉴权成功才可以执行对应的命令。通过no命令恢复默认配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
command-authorization 
  ＜level 
＞ [config-command 
] [＜aaa-author-template 
＞]
no command-authorization 
  ＜level 
＞
				
命令参数解释 : 
参数|描述
---|---
＜level＞|No命令用于恢复默认设置，即不需要授权。范围：0~15
config-command|全局配置模式下的命令需要进行命令授权。该参数可选，如果不指定该参数，则全局配置模式下的命令采用默认授权方式，即不需要授权。如果no命令不指定该参数，则命令授权方式恢复为默认方式，即所有的命令都不需要进行命令授权；如果no命令指定该参数，则仅配置模式下命令授权方式恢复为默认方式。
＜aaa-author-template＞|AAA授权模板号，该参数可选。未配置该参数表示对应权限级别的用户命令授权使用用户授权模板指定的授权策略，即和用户自身的命令授权策略相同；配置该参数，则用户的命令授权策略以配置的模版为准。范围：2001~2128。
缺省 : 
默认情况下，所有命令不需要进行命令授权。 
使用说明 : 
应用场景：通常情况下，某级别用户经过授权后，可以执行该级别及该级别以下的命令集。为了加强对用户权限的限制，实现权限的最小化控制，可以配置按命令行授权。配置按命令行授权后，用户输入的相应模式下的命令需要进行授权，授权通过后才可以执行，否则不能执行该命令。注意事项：只有在使用TACACS协议时，才可以配置用户按命令行授权。在配置命令行授权时需要注意：如果TACACS服务器Down、不可达或回应超时，命令行授权失败，相应级别的用户无法执行配置策略中指定模式下的命令。命令行授权可以使用本地授权作为备选方法（aaa-authorization-type tacacs-local），这样，如果因为服务器的问题（服务器Down、不可达或回应超时）导致命令行授权失败时，可以将命令行授权转入本地授权处理。
范例 : 
级别为10的用户在全局配置模式下的命令到TACACS服务器做授权，本地授权作为备选方法。ZXROSNG(config)#tacacs enableZXROSNG(config)#tacacs-server host vrf mng 192.168.122.1 key zteZXROSNG(config)#tacplus group-server tacGroupZXROSNG(config-sg)#server vrf mng 192.168.122.1ZXROSNG(config-sg)#exitZXROSNG(config)#ZXROSNG(config)#aaa-authorization-template 2001ZXROSNG(config-aaa-author-template)#authorization-tacacs-group tacGroupZXROSNG(config-aaa-author-template)#aaa-authorization-type tacacs-localZXROSNG(config-aaa-author-template)#exitZXROSNG(config)#command-authorization 10 config-command 2001
相关命令 : 
aaa-authorization-templateaaa-authorization-type 
## commands 

commands 
命令功能 : 
本命令在自定义命令组模式(config-cmdgrp)下执行，用于配置命令组下命令的匹配规则，符合匹配规则的命令，被对应的命令组包含。配置命令组后，通过将命令组与用户授权模板进行绑定，实现对用户权限的管理。使用no命令删除配置的命令匹配规则。通过cmdgroup命令创建所需的命令组并进入自定义命令组模式。
命令模式 : 
 自定义命令组模式  
命令默认权限级别 : 
15 
命令格式 : 
commands 
  ＜mode 
＞ {include 
 ＜keywords 
＞|exclude 
 ＜keywords 
＞|include-all 
}
no commands 
  ＜mode 
＞ {include 
 ＜keywords 
＞|exclude 
 ＜keywords 
＞|include-all 
}
				
命令参数解释 : 
参数|描述
---|---
＜mode＞|命令模式名，系统根据系统预配置提示所有的命令模式，供用户选择输入。
include|包含<mode>下命令关键字中含<keywords>字符串的命令
＜keywords＞|命令行中的关键字
exclude|包含<mode>下命令关键字中不含<keywords>字符串的命令
＜keywords＞|命令行中的关键字
include-all|包含<mode>下所有命令
缺省 : 
无 
使用说明 : 
本命令定义命令组由哪些命令组成，符合匹配条件的命令，被命令组包含。当定义的规则超过命令组配置容量时，配置失败。将某个命令组删除时，该命令组下配置的所有的命令匹配规则自动删除。
范例 : 
配置first用户组包含show模式下的show tech-support命令：ZXROSNG(config)#cmdgroup firstZXROSNG(config-cmdgrp)# commands show include show tech-supportZXROSNG(config-cmdgrp)#配置first用户组排除show模式下的show clock命令：ZXROSNG(config)#cmdgroup firstZXROSNG(config-cmdgrp)#commands show exclude show clockZXROSNG(config-cmdgrp)#配置first命令组包含show模式下的所有命令：ZXROSNG(config)#cmdgroup firstZXROSNG(config-cmdgrp)#commands show include-all ZXROSNG(config-cmdgrp)#
相关命令 : 
cmdgroupshow cmdgroupshow running-config oamlocal-cmdgrouplocal-cmdgroup-mode
## configure terminal 

configure terminal 
命令功能 : 
此命令在特权模式下执行，用于进入全局配置模式。可通过multi-user configure命令配置多终端登录全局配置模式，默认情况下设备只允许一个终端进入全局配置模式。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
configure terminal 
  [{automatic 
|manual 
}]
命令参数解释 : 
参数|描述
---|---
automatic|自动提交模式
manual|手动提交模式
缺省 : 
不带任何参数时，默认的提交模式是由命令commit-mode default {manual|automatic}配置的 
使用说明 : 
默认情况下只允许一个终端登入全局配置模式，如果希望多个终端都能同时登录全局配置模式，需要先执行multi-user configure命令配置多终端登录全局模式。单终端配置的情况下，如果设备只有串口终端处于全局配置模式或其 后续模式下（不包括诊断相关模式），那么其他的非串口终端不允许进入全局配置模式。如果设备已经有非串口终端处于全局配置模式或其后续模式(不包括诊断相关模式)，那么只有串口终端允许进入全局配置模式，对于非串口终端不允许进入全局配置模式。可以通过参数指定配置的提交模式为手动或自动。
范例 : 
1.当前没有其他终端处于全局配置模式及其后续模式下，或者开始了多终端登录全局配置模式，由特权模式登陆到全局配置模式：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#2.未开启多终端登录全局配置模式且当前已经有其他终端处于全局配置模式及其后续模式下，在特权模式下执行命令，提示已经有终端处于全局配置模式下，不允许配置：ZXROSNG#configure terminal%Error 140357: Simultaneous configs not allowed. Locked from con0 ().ZXROSNG#3.可以指定提交模式,手动模式下搭配commit等命令做配置的提交ZXROSNG#configure terminal manualEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#commit
相关命令 : 
multi-user configurecommit-mode default {manual|automatic}
## debug all 

debug all 
命令功能 : 
打开所有debug调试开关。使用no命令关闭所有debug调试开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug all 
 
no debug all 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
1. 由于debug all操作风险很多，若系统忙于debug信息的输出，会影响网络性能，所以当前系统暂屏蔽掉debug all操作，用户可通过 "debug 业务模块 + all" 打开debug开关。2. 系统支持no debug all 操作关闭所有debug（快捷键 CTRL+D）。
范例 : 
打开所有debug调试开关：ZXROSNG#debug all %Error 140010: The operation has been forbidden! Please use 'debug <module-name> ...' to turn on possible debugging.
相关命令 : 
show debug。 
## disable 

disable 
命令功能 : 
本命令在用户模式或特权模式下执行，用于降低当前终端的权限等级。通过show privilege命令实时查看当前终端的权限级别。通过enable命令改变当前终端的权限级别。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
disable 
  [＜level 
＞]
命令参数解释 : 
参数|描述
---|---
＜level＞|降低到的权限级别，最小值为0，最大值取决于产品规格，缺省为1。范围：0-$#218169346#$
缺省 : 
默认情况下权限等级为1。 
使用说明 : 
本命令输入的权限级别必须小于或者等于当前终端的权限级别。如果当前终端处于特权模式下，降低权限级别到0或1，则会进入用户模式。如果输入的权限等级大于当前终端的权限等级，会提示报错信息。 
范例 : 
当前处于特权模式下，权限级别为15，降低权限等级到1，从特权模式退到用户模式：ZXROSNG#show privilege Current privilege level is 15ZXROSNG#disable 1ZXR10>show privilege Current privilege level is 1当前终端权限级别为15，降低权限级别到10：ZXROSNG#show privilege Current privilege level is 15ZXROSNG#disable 10ZXROSNG#show privilegeCurrent privilege level is 10ZXROSNG#当前终端权限级别为10，输入的降低后权限级别为15，大于当前终端权限级别，提示输入的权限级别必须小于当前终端权限级别：ZXROSNG#show privilegeCurrent privilege level is 10ZXROSNG#disable 15%Error 140253: New privilege level must be less than current privilege level.ZXROSNG#
相关命令 : 
enable 
## enable 

enable 
命令功能 : 
本命令在用户模式或特权模式下执行，用于实时改变当前操作终端的权限等级，包括提升当前终端的权限等级或降低当前终端的权限等级。通过show privilege命令实时查看当前终端的权限级别。通过disable命令降低当前终端的权限级别。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:0,特权模式:2 
命令格式 : 
enable 
  [＜level 
＞]
命令参数解释 : 
参数|描述
---|---
＜level＞|修改到的权限等级。最低权限级别为0，最大权限级别由产品决定。缺省情况下为15.范围：0-$#218169346#$
缺省 : 
默认情况下权限等级为15。 
使用说明 : 
通过enable命令进入相同级别权限或更低级别权限，直接进入对应权限等级不需要输入口令；进入更高级别权限，需要输入相应权限等级的口令，如果对应的权限级别还未配置登入口令，不允许进入该权限等级。如果当前终端处于用户模式下，输入的权限级别大于1，执行成功后进入特权模式；如果当前终端终端处于特权模式下，输入的权限级别为0或者1，执行成功后进入用户模式。为防止不断重试暴力破解enable密码，采用时间惩罚错误机制：(1) enable认证连续6次输入密码无效，enable命令（enable提升权限或降低权限）延迟1分钟执行，1分钟后，失败计数减1，再次认证失败，再次延迟1分钟。。。(2) 惩罚基于登录用户名，当enable认证通过后，解除惩罚；(3) 启动和解除惩罚，上报通知。
范例 : 
提高权限等级到15，从用户模式进入特权模式：ZXR10>enable 15Password:ZXROSNG#没有配置14级口令，无法进入特权模式：ZXR10>enable 14Password:% No password is set将权限等级修改为1，从特权模式进入用户模式ZXROSNG#enable 1ZXR10>
当前终端，连续6次输入无效密码，1分钟内不允许执行enable命令ZXROSNG#enable 15Password:% Bad passwordPassword:% Bad passwordPassword:% Bad passwordZXROSNG#ZXROSNG#enable 15Password:% Bad passwordPassword:% Bad passwordPassword:%Error 140367: The enable command will be locked for 1 minute because of 6 successive inputs of a wrong password.ZXROSNG#ZXROSNG#enable%Error 140368: The enable command is locked. Please try again later.ZXROSNG#ZXROSNG#enable 1%Error 140368: The enable command is locked. Please try again later.ZXROSNG#ZXROSNG#disableZXR10>
ZXR10>enable 15%Error 140368: The enable command is locked. Please try again later.ZXR10>
相关命令 : 
disableenable secret
## end 

end 
命令功能 : 
此命令在除用户模式和特权模式外的其他所有模式下执行，用于退出当前模式，直接返回特权模式。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
1 
命令格式 : 
end 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
在配置模式下执行end退出，如果此时是手动提交模式且有配置未提交，会有是否提交的交互提示，三个选项yes、no、cancel，分别表示提交配置后退出模式、放弃配置后退出模式、取消退出模式 
范例 : 
1.在用户管理模式下执行end命令，直接退回到特权模式ZXROSNG(config-system-user)#endZXROSNG#
2.在特权模式下执行end命令，提示输入错误ZXROSNG#endend  ^%Error 140303: Invalid input detected at '^' marker.3.手动提交模式时，在配置模式下执行end退出，如果有配置未提交，会有是否提交的交互提示，选择提交后会有打点或其他进度、错误提示ZXROSNG(config)#show commit-modeManual commit mode.ZXROSNG(config)#interface portlist smartgroup1.1-4000ZXROSNG(config)#endUncommitted configurations found. Commit them before exiting? [yes/no/cancel]: yes...................ZXROSNG#
相关命令 : 
exit 
## exit 

exit 
命令功能 : 
该命令在用户模式，特权模式下执行时，用于退出当前终端链接。在除用户模式，特权模式外的其他所有模式下执行时，用于退出当前命令模式，退回到上一命令模式。
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:0,除用户模式外的其他所有模式:1 
命令格式 : 
exit 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
在全局配置模式下执行exit退出到特权模式时，如果此时是手动提交模式且有配置未提交，会有是否提交的交互提示，三个选项yes、no、cancel，分别表示提交配置后退出模式、放弃配置后退出模式、取消退出模式 
范例 : 
1.特权模式下执行exit命令，退出当前终端ZXROSNG#exitZXR10 Con0 is now availablePress RETURN to get started.2.全局配置模式下执行exit命令，退出到前一命令模式，即特权模式、ZXROSNG(config)#exitZXROSNG#
3.在全局配置模式下执行exit退出到特权模式时，如果此时是手动提交模式且有配置未提交，会有是否提交的交互提示，选择提交后会有打点或其他进度、错误提示ZXROSNG(config)#show commit-modeManual commit mode.ZXROSNG(config)#interface portlist smartgroup1.1-4000ZXROSNG(config)#exitUncommitted configurations found. Commit them before exiting? [yes/no/cancel]: yes...................ZXROSNG#
相关命令 : 
end 
## login 

login 
命令功能 : 
本命令在用户模式或特权模式下执行，用于启用另一个用户名登陆设备。 
命令模式 : 
 特权模式,用户模式  
命令默认权限级别 : 
用户模式:1,特权模式:2 
命令格式 : 
login 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
在用户模式或特权模式下执行该命令后，提示输入用户名和密码，如果用户认证成功，根据指定登陆用户的权限级别进入对应的模式；如果用户权限级别大于或者等于2时切换到特权模式，否则切换到用户模式。如果输入的用户名或者密码错误，则提示重新输入，一共有三次认证的机会，三次输入均认证不过返回原先所在模式。 
范例 : 
使用级别为15的user用户登录设备，输入正确的用户名和密码后进入特权模式：ZXR10>loginUsername:userPassword:ZXROSNG# 
相关命令 : 
无。 
## multi-user configure 

multi-user configure 
命令功能 : 
本命令在全局配置模式下执行，用于配置是否允许多个终端同时进行命令配置，设置后当前设备允许多个终端同时进入全局配置模式。使用no命令配置为单终端配置模式，配置单终端模式后设备上同时只允许单个终端登录到全局配置模式。使用configure terminal命令进入全局配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
multi-user configure 
 
no multi-user configure 
命令参数解释 : 
					无
				 
缺省 : 
缺省只有一个用户可以进入全局配置模式。 
使用说明 : 
配置本条命令后，设备上允许多个终端同时登录全局配置模式。默认情况下，设备只允许单个终端进入全局配置模式下进行配置操作。使用no命令配置为单终端配置模式时，必须保证其他终端都退出了全局配置模式（或者处于诊断相关模式下），才能配置为单终端配置模式。。 
范例 : 
从特权模式进入全局配置模式，配置多终端登录模式：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#multi-user configure%Info 140359: Allow others to configure, must avoid conflict.ZXROSNG(config)#设备上其他终端都已经退出全局配置模式，配置为单用户配置模式：ZXROSNG(config)#no multi-user configure ZXROSNG(config)#设备上还有其他的终端处于全局配置模式及其后续模式下，配置为单用户配置模式，提示无法配置：ZXROSNG(config)#no multi-user configure %Error 140358: Someone has entered the configure mode, cannot set single-user.
相关命令 : 
configure terminal
## privilege 

privilege 
命令功能 : 
本命令在全局配置模式下执行，用于配置命令节点的权限级别。no命令恢复配置命令节点的默认权限级别。通过show privilege命令查看命令节点的权限级别。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
privilege 
  ＜logic-mode 
＞ [all 
] level 
 {＜level 
＞|default 
} ＜command-keywords 
＞
no privilege 
  ＜logic-mode 
＞ [all 
] node 
 ＜command-keywords 
＞
				
命令参数解释 : 
参数|描述
---|---
＜logic-mode＞|逻辑模式类别。
all|支持该命令关键字打头的所有后续命令。
＜level＞|权限等级 ，范围为2-15之间的整数，数值越大，配置执行该命令的用户所需的权限级别越高。
default|恢复指定的命令节点为默认权限级别 。不同的命令节点的默认权限级别不确定，由系统初始化时预配置决定，通过show privilege命令查看指定命令节点的权限级别。
＜command-keywords＞|命令关键字。长度：1-200
缺省 : 
该命令没有默认配置。系统中所有命令都有默认权限级别。在show running-config中某些情况下会呈现default配置。该命令为立即提交命令，手动模式下不支持该命令。 
使用说明 : 
系统所有命令都有默认的权限级别，通过本命令修改指定命令节点的权限级别。修改后，低于该权限级别的终端或者用户将不能执行该命令。通过参数all修改以指定的命令关键字为起始字符的所有命令。default参数和no命令执行结果相同，都是恢复指定命令节点的默认权限级别。该命令为自动提交命令，手动提交命令模式下不支持该命令。
范例 : 
配置show模式下的show命令节点权限级别为10：ZXROSNG(config)#privilege show level 10 showZXROSNG(config)# 配置show模式下的所有以show关键字开始的命令权限级别为12：ZXROSNG(config)#privilege show all level 12 showZXROSNG(config)#将特权模式下的configure terminal命令恢复为默认权限级别：ZXROSNG(config)#privilege exec level default configure terminalZXROSNG(config)#
相关命令 : 
show privilege。 
## read-config 

read-config 
命令功能 : 
本命令在全局配置模式下执行，用于批量执行指定的文件中的配置命令，并将执行的命令及其执行结果打印到终端界面。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
read-config 
  ＜batch-file 
＞
命令参数解释 : 
参数|描述
---|---
＜batch-file＞|指定读取的文件路径，长度为1-140个字符串。
缺省 : 
无。 
使用说明 : 
本命令指定的文件路径支持全路径和非完整路径。    全路径文件名以”/”开始，读取对应路径下的文件。    如果指定的文件路径是非完整路径，则以默认路径（通常为/datadisk0/config，具体路径信息由产品决定）为根目录，加上指定的路径作为完整路径，读取对应路径下的文件。 
范例 : 
指定全路径信息，执行设备/sysdisk0/config.dat文件中的命令：SSBUE-M6000-8-R4(config)#read-config /sysdisk0/config.datsystem-user user-name user    bind authentication-template 1    bind authorization-template 1    password user  $  authentication-template 1    authentication-method pap    bind aaa-authentication-template 2001  $……SSBUE-M6000-8-R4(config)#指定文件名，执行系统默认路径/datadisk0/config路径下的文件中的配置：SSBUE-M6000-8-R4(config)#read-config /sysdisk0/config.datsystem-user user-name user    bind authentication-template 1    bind authorization-template 1    password user  $  authentication-template 1    authentication-method pap    bind aaa-authentication-template 2001  $……SSBUE-M6000-8-R4(config)#指定相对路径，执行系统默认路径/datadisk0/config下的对应的路径，例如当前处于设备/datadisk0路径下，输入的文件名包含相对路径./../config.dat，则转换为默认路径的对应路径信息/datadisk0/config/./../config.dat，即/datadisk0/config.dat，设备上该路径下没有对应的文件，提示打开文件失败：SSBUE-M6000-8-R4(config)#read-config ./../config.dat%Error 45503: Open file failed!SSBUE-M6000-8-R4(config)
相关命令 : 
无。 
## set debug-timer 

set debug-timer 
命令功能 : 
本命令在特权模式下执行，用于配置关闭debug功能的时间。 配置后，到了指定的时间，自动关闭系统所有debug调试开关。缺省配置为10分钟。通过show debug-timer命令查看当前设备上debug功能的关闭时间。通过debug all命令打开当前设备所有debug功能开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
set debug-timer 
  ＜time 
＞
no set debug-timer 
命令参数解释 : 
参数|描述
---|---
＜time＞|设置debug功能关闭的时间，单位：分钟。范围为0-120之间的整数。
缺省 : 
默认10分钟。 
使用说明 : 
最大可设置时间为120分钟，最小为0分钟。配置为0分钟时，表示不会自动关闭debug功能。使用no命令恢复为默认值。 
范例 : 
配置debug功能关闭的时间为20分钟：ZXROSNG#set debug-timer 20ZXROSNG#show debug-timerTime of turning off debug:20 min(s)ZXROSNG#通过no命令将配置恢复为默认值：ZXROSNG#no set debug-timerZXROSNG#show debug-timer Time of turning off debug:10 min(s)ZXROSNG#
相关命令 : 
show debug-timer 
## show auto-write 

show auto-write 
命令功能 : 
显示配置自动存盘的当前状态和历史记录信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show auto-write 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
执行此命令来查看配置自动存盘的状态信息，包括当前配置自动存盘信息和历史10条自动存盘的状态记录。 
范例 : 
显示自动保存配置的状态信息：ZXROSNG(config)#show auto-write Current:  State: writing  CPU-Limit: yes  Start-Time: 2017-07-26 14:22:09History:----------------------------------------------------------------------------------ID    Policy    Start-Time         End-Time          CPU   Result----------------------------------------------------------------------------------0     delay    2017-07-26 14:17:35 2017-07-26 14:17:37  no   success1     delay    2017-07-26 14:19:48 2017-07-26 14:19:48  yes   fail(CPU limit)其中，当前自动存盘的状态信息如下：信息        描述State        当前自动存盘状态。writing：正在执行自动保存；idle：空闲。CPU-Limit    是否因为CPU利用率过高而延时保存。 Yes：延时中；no：未延时。Start-Time    当前保存操作的开始时间。历史自动存盘的状态信息如下：信息        描述ID           编号。Policy       自动保存的策略。delay：配置变更后延时保存；everyday：每天定时自动保存。 Start-Time   自动保存的开始时间。End-Time    自动保存的结束时间。CPU        是否因为CPU利用率过高而限制保存。Result       自动保存成功或失败的原因描述。
相关命令 : 
auto-writeauto-write cpu-limit 
## show cmdgroup 

show cmdgroup 
命令功能 : 
查询命令组相关信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cmdgroup 
  [＜cmdgroup 
＞] 
命令参数解释 : 
参数|描述
---|---
＜cmdgroup＞|命令组名，1~31个字符
缺省 : 
无 
使用说明 : 
通过本命令可以查看命令组的配置信息。指定组名的时候，只显示指定命令组的信息；不带组名，则显示所有命令组的信息。   “PRE_DEFINE_LI_USER” “PRE_DEFINE_LI_ADMIN”这两个为预定义命令组，只有当前用户权限为18级的时候才可查看其信息
范例 : 
1.查看命令组信息ZXROSNG#show cmdgroupcmdgroup first  commands exec include configure terminal  commands exec include configure  commands exec include showcmdgroup second  commands exec include configure   2.查看指定命令组信息ZXROSNG#show cmdgroup firstcmdgroup first  commands exec include configure terminal  commands exec include configure  commands exec include show 3. 18级用户可以查看预定义的命令组信息ZXROSNG#show privilege Current privilege level is 18ZXROSNG#show cmdgroup cmdgroup PRE_DEFINE_LI_USER  commands exec include configure terminal    …cmdgroup PRE_DEFINE_LI_ADMIN  commands exec include configure terminal     ……
相关命令 : 
cmdgroupshow running-config
## show debug 

show debug 
命令功能 : 
本命令在除用户模式外的其他所有模式下执行，用于显示当前设备上的debug配置信息。通过debug all命令打开所有模块的debug开关。通过debug +<module name>+all命令打开某个模块的debug开关。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
当前设备上没有开启debug配置，show debug无显示：ZXROSNG#show debugZXROSNG#打开aim模块的debug开关后，通过show debug命令查看配置：ZXROSNG#debug aim allAll AIM debugging has been turned onZXROSNG#show debugAIM:  AIM authenticate event debugging is on  AIM authenticate error debugging is on  AIM accounting event debugging is on  AIM accounting error debugging is onZXROSNG#
相关命令 : 
debug 
## show debug-timer 

show debug-timer 
命令功能 : 
本命令在除用户模式外的其他所有模式下执行，用于显示当前设备上关闭debug功能的时间。如果设备上开启了debug相关功能，到了该关闭时间后，所有的debug开关都会被关闭。缺省状况下关闭debug功能的时间为10min。通过set debug-timer命令设置关闭debug功能的时间。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug-timer 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
无。 
范例 : 
设备启动后没有手动配置过关闭debug功能的时间，通过show debug-timer显示默认配置：ZXROSNG#show debug-timer Time of turning off debug:10 min(s)ZXROSNG#配置关闭debug功能的时间为20min，通过show debug-timer命令查看配置：ZXROSNG#set debug-timer 20ZXROSNG#show debug-timer Time of turning off debug:20 min(s)ZXROSNG#
相关命令 : 
set debug-timer 
## show multi-user configure 

show multi-user configure 
命令功能 : 
本命令在除用户模式外的其他所有模式下执行，用于查看当前设备是否允许多个终端同时进行命令配置。通过multi-user configure命令配置当前设备是否允许多个终端同时进行命令配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show multi-user configure 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
默认情况下，设备上不允许多是否允许多个终端同时进行命令配置。。 
范例 : 
当前终端允许多终端配置，查看多终端配置信息：ZXROSNG(config)#multi-user configure %Info 140359: Allow others to configure, must avoid conflict.ZXROSNG(config)#show multi-user configureMulti-user configure: enableZXROSNG(config)#当前终端不允许多终端配置，查看多终端配置信息：ZXROSNG(config)#no multi-user configure ZXROSNG(config)#show multi-user configureMulti-user configure: disableZXROSNG(config)#
相关命令 : 
multi-user configureno multi-user configure
## show privilege 

show privilege 
命令功能 : 
本命令在除用户模式外的其他所有模式下执行， 用于查看当前终端的权限级别以及命令的权限配置信息。可以通过enable命令或者disable命令实时改变当前终端的权限级别。通过privilege命令修改命令节点对应的权限级别。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
2 
命令格式 : 
show privilege 
  [{cur-mode 
|show-mode 
} {detail 
|level 
 ＜level 
＞|node 
 ＜command-keywords 
＞}] 
命令参数解释 : 
参数|描述
---|---
cur-mode|显示当前所处命令模式下的命令权限级别，但是显示的命令不包括show命令，其中show命令是指一类能够在多个模式下执行的命令，不仅仅包括以show作为起始关键字的命令。
show-mode|显示show命令模式下的命令权限级别。Show命令模式下的命令是一类能够在多个模式下执行的命令，不仅仅包括以show作为起始关键字的命令。
detail|显示指定的模式下所有命令的权限级别信
＜level＞|显示指定权限级别的命令，范围：最小值1，最大值由产品决定。权限级别范围：1-$#218169346#$
＜command-keywords＞|指定需要显示权限级别的命令，支持空格输入，长度：1-200个字符串，该长度包括输入的命令关键字中空格的长度。
缺省 : 
无。 
使用说明 : 
show privilege显示当前终端的权限等级；show privilege detail显示当前模式下全部的命令节点的权限等级信息；show privilege level <level>显示当前模式下某一个指定权限等级对应的所有命令节点；show privilege node <command-keywords>显示指定命令节点的权限级别。 
范例 : 
(1)显示当前终端的权限：ZXROSNG(config)#show privilege Current privilege level is 15(2)显示arp命令模式下全部的命令节点和权限等级：ZXROSNG(config-arp)#show privilege cur-mode detailLevel   Command-node15      alarm-threshold15      alarm-threshold learn-limit15      alarm-threshold source-filter15      arp15      backupvrrp-learn15      gratuitous-learn15      gratuitous-proxy-arp15      gratuitous-proxy-arp periodic15      inspection15      inspection limit15      inspection trust15      inspection validate15      inspection vlan15      interface15      keepalive15      keepalive periodic15      learn-disable15      learn-limit15      limit-time15      local-proxy-arp15      network-learn15      periodic......
相关命令 : 
privilege。 
## show privilege 

show privilege 
命令功能 : 
本命令在用户模式下执行， 用于查看当前终端的权限级别。可以通过enable命令或者disable命令改变当前终端的权限级别。 
命令模式 : 
 用户模式  
命令默认权限级别 : 
0 
命令格式 : 
show privilege 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
show privilege显示当前终端的权限等级。 
范例 : 
用户模式下查看当前终端的权限级别：ZXR10>show privilege Current privilege level is 1ZXR10>
相关命令 : 
无。 
## show read-config failed 

show read-config failed 
命令功能 : 
显示最近一次执行read-config命令的结果，列出其加载失败的命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show read-config failed 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
read-config命令用来批量读取指定文件中的配置，如果命令提示有配置读取失败，可以使用此show命令来查看具体失败的命令信息。
范例 : 
ZXROSNG(config)#read-config /sysdisk0/DATA0/batchfile.....Read finished. Failed number:6. You can use "show read-config failed" to getdetails.ZXROSNG(config)#show read-config failedStartTime: 2018-9-6 10:52:44Failed Number: 6-------------------------------------------------------------------------------LineNo    Command                                                 Reason-------------------------------------------------------------------------------2         ++configsave 2 15:08:14 Tue Aug 14 2018                 parse error12        xxxaa                                                   parse error5         nvram default-gateway 192.168.100.1                     abandon33        snetconf server enable                                  execute error36        fixed-mode                                              abandon38        free-mode                                               abandon-------------------------------------------------------------------------------其中，命令行错误信息描述如下：信息         描述LineNo        加载失败命令在配置文件中的行号Command    加载失败的命令行Reason        加载失败原因：parse error：解析失败，系统不识别的命令；execute error：执行失败，系统识别的命令，但是因为不符合业务逻辑导致的失败。abandon：read-config是一批一批的加载文件中的配置的，多条配置会一起进行加载，如果其中一条执行失败（execute error），会导致这一批的其他的命令放弃加载，这些命令的状态就记为abandon
相关命令 : 
read-config 
## show running-config 

show running-config 
命令功能 : 
显示系统当前运行的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show running-config 
  [＜module_name 
＞] [{all 
|inactive 
}] 
命令参数解释 : 
参数|描述
---|---
＜module_name＞|模块名称
all|显示所有配置信息包含默认配置信息
inactive|在show  running-config命令执行结果中通过*标记未生效的硬件资源配置
缺省 : 
无。 
使用说明 : 
show running-config inactive显示的配置内容同show running-config，其中inactive选项：只是通过“*”标记出其中未生效的硬件资源配置，便于用户了解硬件资源配置的生效状态。比如因为单板离线等情况引起的未生效的接口配置。目前对于接口配置，只针对实体命令interface本身标记，不再对接口模式下配置标记。 
范例 : 
1、显示oam模块的配置信息：ZXROSNG(config)#show running-config oam!<OAM>clock timezone CHINA+8 8 0!</OAM>ZXROSNG(config)#2、显示if-intf模块的所有配置包括默认配置ZXROSNG#show running-config if-intf all!<if-intf>interface mgmt_eth  ip address 192.0.1.111 255.255.255.0   #no ipv6 enable$interface null1$!</if-intf>3、通过*标注未生效的硬件资源配置：ZXROSNG(config)#show running-config inactive……*interface gei-0/2/1/15     off-line     ip vrf forwarding iii     no shutdown……
相关命令 : 
show running-config-interface  
## show running-config-interface 

show running-config-interface 
命令功能 : 
显示接口相关基本配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show running-config-interface 
  [module 
 ＜module_name 
＞] {byname 
 ＜Interface byname 
＞|＜interface 
＞} [all 
] 
命令参数解释 : 
参数|描述
---|---
＜module_name＞|模块名称
＜Interface byname＞|接口别名
＜interface＞|接口名称
all|显示所有配置信息包含默认配置信息
缺省 : 
无。 
使用说明 : 
无。 
范例 : 
ZXROSNG(config)#show running-config-interface null1!<Interface>interface null1$!</Interface>ZXROSNG(config)#
相关命令 : 
show running-config 
## show startrun-backup history 

show startrun-backup history 
命令功能 : 
显示配置文件自动上传服务器历史记录命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show startrun-backup history 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
配置文件保存完后将当前的配置文件向配置自动上传配置命令指定路径的服务器，使用此show命令显示上传结果记录信息。此命令最多支持显示最近20条上传结果记录信息。
范例 : 
1.显示配置文件自动上传服务器上传结果记录信息：ZXROSNG#show startrun-backup history -------------------------------------------------------------------------------Start-Time          End-Time            Server              Type   Result-------------------------------------------------------------------------------2017-09-15 07:44:33 2017-09-15 07:44:42 1010:1010:1:1:1:0:0 TFTP   FAILED                                        :19                        2017-09-15 07:44:33 2017-09-15 07:44:33 1010:0:0:0:0:0:0:19 TFTP   SUCCESS2017-09-15 07:44:33 2017-09-15 07:45:03 10.42.55.200        FTP    FAILED2017-09-15 07:44:33 2017-09-15 07:44:34 10.42.113.18        SFTP   SUCCESS2017-09-15 06:39:33 2017-09-15 06:39:42 1010:1010:1:1:1:0:0 TFTP   FAILED                                        :19                        2017-09-15 06:39:33 2017-09-15 06:39:34 1010:0:0:0:0:0:0:19 TFTP   SUCCESS2017-09-15 06:39:33 2017-09-15 06:40:03 10.42.55.200        FTP    FAILED2017-09-15 06:39:33 2017-09-15 06:39:34 10.42.113.18        SFTP   SUCCESS2017-09-15 03:14:05 2017-09-15 03:14:06 1010:0:0:0:0:0:0:19 TFTP   SUCCESS2017-09-15 03:14:05 2017-09-15 03:14:35 10.42.55.200        FTP    FAILED2017-09-15 03:14:05 2017-09-15 03:14:06 10.42.113.18        SFTP   SUCCESS2017-09-15 03:13:15 2017-09-15 03:13:16 1010:0:0:0:0:0:0:19 TFTP   SUCCESS2017-09-15 03:13:15 2017-09-15 03:13:45 10.42.55.200        FTP    FAILED2017-09-15 03:13:15 2017-09-15 03:13:16 10.42.113.18        SFTP   SUCCESSZXROSNG(config)#其中：字段说明Start-Time：上传开始时间，精确到秒。End-Time：上传结束时间，精确到秒。Server    ：上传服务器的IP地址，支持IPv4或IPv6。Type：上传所使用的协议，支持FTP、SFTP或TFTP。Result    ：上传结果，有SUCCESS、FAILED、TRANSPORTING或STOPED四种结果。
相关命令 : 
startrun backup-to server 
## show startup-config failed 

show startup-config failed 
命令功能 : 
列出启动TXT加载失败的命令行信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show startup-config failed 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
设备重启结束后，进入命令行界面，执行此命令来查看最后一次TXT加载有哪些加载失败的命令及其相关的错误信息。 
范例 : 
启动加载结束后，没有加载失败的命令，显示TXT加载开始时间，失败个数。ZXROSNG#show startup-config failed StartTime: 2013-4-1 2:30:7 Failed Number: 0启动加载结束后，有加载失败的命令，显示TXT加载开始时间，失败个数及其相关命令行错误信息。ZXROSNG#show startup-config failed StartTime: 2013-4-1 2:30:7 Failed Number: 4-------------------------------------------------------------------------------LineNo    Command                                                 Reason-------------------------------------------------------------------------------39        enable secret level 15 5 RcMLuUKvnFZX9kNAV6A/UA==       parse error40        aaa-authentication-template 2001                        parse error42        user-group special zte_group zte encrypted ce7c04930c52 parse error          bfe1669f6c229ef61b761ec847e5b3052bdb51456385bb2a9a57    41        ++index 20                                              execute error-------------------------------------------------------------------------------其中，命令行错误信息描述如下：信息         描述LineNo        加载失败命令在配置文件中的行号Command    加载失败的命令行Reason        加载失败原因：parse error：解析失败，系统不识别的命令；execute error：执行失败，系统识别的命令，但是因为不符合业务逻辑导致的失败。
相关命令 : 
无。 
## show startup-config 

show startup-config 
命令功能 : 
本命令在除用户模式外的其他所有模式下执行，用于查看当前设备的配置信息。配置信息保存在设备指定目录下的配置文件中，设备重启时读取该文件中保存的配置信息恢复到系统中。通过write命令将当前设备配置信息写入指定配置文件。通过startrun download命令将其他路径下的文件下载为指定的配置文件。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show startup-config 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
本命令用于显示当前设备的启动配置文件信息。通过write命令或者startrun download命令等方式修改了设备上的配置文件信息后，执行本命令显示的是更新后的配置信息。 
范例 : 
查看当前设备上的启动配置信息 ZXROSNG#show startup-config !<MIM>!</MIM>!<controller>!</controller>!<system-config>load-mode txt!</system-config>……
相关命令 : 
show running-config 
## show this 

show this 
命令功能 : 
本命令在除用户模式、特权模式以及全局配置模式外的其他所有模式下执行， 用于显示当前模式下的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show this 
  [all 
] 
命令参数解释 : 
参数|描述
---|---
all|显示所有配置信息，包含默认配置，通过“#”标记默认配置
缺省 : 
无。 
使用说明 : 
本命令显示的是当前模式下的配置信息，不包括默认的配置信息。本命令不支持显示单个模块下当前模式的配置信息。 
范例 : 
显示当前设备上用户管理模式下的配置信息：ZXROSNG(config-system-user)#show this      !<adm-mgr>  authorization-template 1    access-only lct qx dcn    bind aaa-authorization-template 2001    local-cmdgroup who01    local-cmdgroup zhou    local-cmdgroup 1    local-cmdgroup bucunzaiminglzu    local-privilege-level 15  $!</adm-mgr>ZXROSNG(config-system-user)#
相关命令 : 
show running-config 
## startrun backup-to server 

startrun backup-to server 
命令功能 : 
配置文件自动上传服务器命令。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
startrun backup-to server 
  {＜ipv4 address 
＞|＜ipv6 address 
＞} [＜listen-port 
＞] [vrf 
 ＜vrf-name 
＞] transport-type 
 {{ftp 
|sftp 
} username 
 ＜username 
＞ [{password 
 ＜password 
＞|encrypted 
 {＜enc-password-64 
＞|＜enc-password-128 
＞}}]|tftp 
} [path 
 ＜folder 
＞] [zip 
]
no startrun backup-to server 
  {＜ipv4 address 
＞|＜ipv6 address 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4 address＞|IPv4地址
＜ipv6 address＞|IPv6地址
＜listen-port＞|监听端口，取值范围是<1-65535>；
＜vrf-name＞|VRF名称，长度1–32个字符，如vrf name为mng表示选择管理口；
ftp|FTP
sftp|SFTP
＜username＞|FTP或SFTP服务器的用户名，最大长度65；
＜password＞|FTP或SFTP服务器的用户名相应的密码，最大长度64；
＜enc-password-64＞|密文密码，长度：64
＜enc-password-128＞|密文密码，长度：128
tftp|TFTP
＜folder＞|远端文件路径，最大长度64；
zip|压缩文件之后上传
缺省 : 
无 
使用说明 : 
用户执行保存配置文件的命令后，如果当前系统没有配置自动上传配置命令，则保存完配置文件后就结束；如果系统中有配置自动上传配置的命令配置，则在配置文件保存完后会将当前的配置文件向配置自动上传配置命令指定路径的服务器上传一份，服务器中的配置文件名可以带时间后缀命名。默认ftp和tftp服务器的路径为空。支持配置保存重启。3.指定zip时，上传文件时会将文件压缩成.zip文件再上传。4.配置明文密码，显示为密文密码5.服务器类型为 ftp和sftp时，如果指定了username参数，不指定密码参数，则以交互方式输入明文密码，且显示为*。
范例 : 
1. 配置文件自动上传服务器命令：ZXROSNG(config)# startrun backup-to server 1.2.3.4 65431 vrf mng transport-type ftp username zte password zte123 path /ftpServer/dat/ZXROSNG(config)#ZXROSNG(config)# startrun backup-to server 1010::1 65431 vrf mng transport-type ftp username zte password zte123 path /ftpServer/dat/ZXROSNG(config)#2. 显示配置文件自动上传服务器命令信息：ZXROSNG(config)#show running-config oam!<oam>startrun backup-to server 1.2.3.4 65431 vrf mng transport-type ftp username zte encrypted ed522db9a15709058fa2aa101401c2a737a47ac4fb6465b8d3a77ebb1e2264d5 path /ftpServer/dat/startrun backup-to server 1010::1 65431 vrf mng transport-type ftp username zte encrypted ed522db9a15709058fa2aa101401c2a737a47ac4fb6465b8d3a77ebb1e2264d5 path /ftpServer/dat/!</oam>ZXROSNG(config)#3. 配置文件自动上传服务器，交互式输入密码ZXROSNG(config)#startrun backup-to server 1.2.3.4 65431 vrf mng transport-type ftp username zte path /ftpServer/dat/Please configure the password(1-64)Enter password: ******Confirm password: ******ZXROSNG(config)#
相关命令 : 
writeauto-write（此命令仅SWITCH (89/99/5960/89-JW/89-GM/99-GM/5960-GM)、高端路由器HighEndRouter (T8000/T8000-JW)、高端分组HighEndPacket (M6000-S/M6000-S-JW/M6000-S-GM)、PC (MSE/SWITCH)、FN (C600)项目支持；）
## startrun download 

startrun download 
命令功能 : 
本命令在特权模式下执行， 用于把指定的文件下载到设备的系统配置文件目录，下载后的文件名为startrun.dat，文件保存的路径由产品决定。通过show startup-config命令查看对应配置文件的内容。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
startrun download 
  [unzip 
] {local 
 ＜local-path 
＞|[vrf 
 ＜vrf-name 
＞] {ftp 
 {＜A URL 
＞|{＜ipv4 address 
＞|＜ipv6 address 
＞} [＜listen-port 
＞] username 
 ＜username 
＞ [password 
 ＜password 
＞] path 
 ＜filepath 
＞}|sftp 
 {＜ipv4 address 
＞|＜ipv6 address 
＞} [＜listen-port 
＞] username 
 ＜username 
＞ [password 
 ＜password 
＞] path 
 ＜filepath 
＞}}
命令参数解释 : 
参数|描述
---|---
unzip|下载之后再执行解压缩
local|标示本地下载方式
＜local-path＞|采用本地下载方式，路径为本地下载文件的全路径,路径格式为：/filepath/filename，长度为1-159个字符串。
vrf|vrf实例
＜vrf-name＞|VRF名称，长度为1-32个字符串。使用前，需要在设备上先配置相应的VRF实例。
ftp|标示ftp下载方式
＜A URL＞|采用ftp下载方式，下载的ftp文件路径信息，格式为：//用户名:密码@ftp服务器IPv4地址/文件路径/文件名，总长度为1-230个字符串。
＜ipv4 address＞|IPv4地址。
＜ipv6 address＞|IPv6地址。
＜listen-port＞|FTP或SFTP监听端口号，长度：1-65535。
＜username＞|FTP或SFTP服务器用户名，长度：1-65。
＜password＞|FTP或SFTP服务器的用户名对应的密码，长度：1-64。
＜filepath＞|远端文件地址，格式：/文件路径/文件名，长度：1-159。
sftp|标识SFTP下载方式。
＜ipv4 address＞|IPv4地址。
＜ipv6 address＞|IPv6地址。
＜listen-port＞|FTP或SFTP监听端口号，长度：1-65535。
＜username＞|FTP或SFTP服务器用户名，长度：1-65。
＜password＞|FTP或SFTP服务器的用户名对应的密码，长度：1-64。
＜filepath＞|远端文件地址，格式：/文件路径/文件名，长度：1-159。
缺省 : 
无。 
使用说明 : 
1.执行write或者write txt命令会把当前设备的配置信息写入指定配置文件路径下的startrun.dat文件，设备重启时如果加载方式为txt加载，则读取该文件恢复之前保存的配置。2.由于系统限制用户通过cp或copy ftp等命令写文件到设备上的配置文件目录，本命令可以把当前设备上的指定文件或者远端FTP，SFTP服务器上的文件下载到系统指定的配置文件路径。如果设备上指定目录下已经存在statrun.dat文件，执行本条命令下载后会覆盖之前的文件。FTP URL拷贝方式只支持IPV4方式下载。3.若指定unzip选项，文件下载成功后对源文件进行解压。源文件命名必须遵循 *.zip格式。否则解压不成功。4. ftp和sftp方式下载，如果指定了username参数，不指定password参数，则以交互方式输入密码。
范例 : 
本地拷贝方式将当前设备上的文件拷贝到指定目录下：ZXROSNG#startrun download local /datadisk0/startrun.datThe operation will overwrite the previous file.Are you sure? [yes/no]:yStart download....[ok]ZXROSNG#本地拷贝方式将当前设备上实际不存在的一个文件拷贝到指定目录下，提示文件或者目录不存在：ZXROSNG#startrun download local /datadisk0/startrun.datThe operation will overwrite the previous file.Are you sure? [yes/no]:y%Error 16: No such file(s) or directory(s).ZXROSNG#ftp拷贝方式将远端ftp服务器上的文件拷贝到设备指定目录下：ZXROSNG#startrun download vrf mng ftp //user:user@192.168.10.10/startrun.dat        The operation will overwrite the previous file.Are you sure? [yes/no]:yStart download....[ok]ZXROSNG#ftp拷贝方式将远端ftp服务器上的文件拷贝到设备指定目录下，该文件实际不存在，提示拷贝文件失败：ZXROSNG#startrun download vrf mng ftp //user:user@192.168.1.10/startrun.dat        The operation will overwrite the previous file.Are you sure? [yes/no]:yStart download....%Error 36: Failed to copy file.ZXROSNG#ftp用户名密码下载方式：ZXROSNG#startrun download vrf mng ftp 192.168.100.250 21 username zte password zte123 path startrunbak.datThe operation will overwrite the previous file.Are you sure? [yes/no]:yesStart download....[ok]sftp用户名密码下载方式：ZXROSNG#startrun download vrf mng sftp 192.168.100.250 22 username zte password zte123 path startrunbak.datThe operation will overwrite the previous file.Are you sure? [yes/no]:yesStart download....[ok]sftp用户名密码下载方式，交互式输入密码：ZXROSNG#startrun download vrf mng sftp 192.168.100.250 22 username zte path startrunbak.datThe operation will overwrite the previous file.Are you sure? [yes/no]:yesPassword required for zte.Enter password: ******Start download....[ok]ZXROSNG#
相关命令 : 
无。 
## timestamp 

timestamp 
命令功能 : 
用来使能或去使能系统的时间戳功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
timestamp 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能系统的时间戳功能。
disable|去使能系统的时间戳功能。
缺省 : 
缺省情况下，系统未使能时间戳功能。 
使用说明 : 
1. 使能时间戳功能后，执行show命令时，首先打印系统时间。2. 时间显示按照show clock命令的格式（如：17:27:40 UTC Wed Dec 27 2017）。3. 时间戳的信息不参与回显过滤。4. 如果原命令无回显或执行报错，仍打印时间戳信息。
范例 : 
使能系统的时间戳功能：ZXROSNG(config)# timestamp enable%Info 140362: After the timestamp function is enabled, the system time is printed first when the 'show' command is executed.ZXROSNG(config)# ZXROSNG(config)#show running-config oam23:09:17 UTC Thu Jun 14 2018!<oam>timestamp enable!</oam>ZXROSNG(config)#
相关命令 : 
show clock 
## write 

write 
命令功能 : 
该命令在特权模式下执行， 用于将当前设备的配置写入指定文件。设备再次启动时，根据配置的加载方式加载对应的配置文件，将保存的配置恢复。通过load-mode命令配置当前设备的加载方式。通过show load-mode命令查看当前设备的加载方式。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
write 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
本命令用于将当前设备配置信息写入硬盘的指定文件，通过配置加载方式，用于设备重启后恢复配置。也可以通过startrun download命令将其他路径下的配置文件下载为指定的文件，两种操作方式都会替换原有的配置文件，使用前请注意备份原有配置文件。 
范例 : 
保存当前设备的配置信息：ZXROSNG#write.Write DB OK!Building configuration......................................................................[OK].ZXROSNG#
相关命令 : 
无。 
# 性能统计配置命令 
## performance data-save-interval 

performance data-save-interval 
命令功能 : 
该命令在全局配置模式下执行，用于设置应用性能历史数据保存周期。性能数据按配置的保存周期定时进行保存，生成的数据可供用户通过EMS网管查询显示。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
performance data-save-interval 
  {5min 
|15min 
}
no performance data-save-interval 
命令参数解释 : 
参数|描述
---|---
5min|<取值规则>若设置为5min，则表示设置性能历史数据保存周期为5分钟。
15min|<取值规则>若设置为15min，则表示设置性能历史数据保存周期为15分钟。该选项为默认选项。
缺省 : 
15 min 
使用说明 : 
性能历史数据保存周期可以通过show performance data-save-interval命令进行查询。目前性能历史数据保存周期取值只支持5 分钟和15分钟。通过no performance data-save-interval命令，可进行性能历史数据保存周期配置的删除，删除成功后，性能历史数据保存周期恢复为默认的15分钟。
范例 : 
设置性能历史数据保存周期5分钟，则输入以下命令：ZXROSNG(config)# performance data-save-interval 5min
相关命令 : 
show performance data-save-interval 
## performance update-interval 

performance update-interval 
命令功能 : 
该命令在全局配置模式下执行，用于配置性能管理接口计数器进行统计时的刷新时间间隔，默认为10秒。该命令只是改变性能数据采样周期时间，如果在采样时间内没有数据上报，则用户不能感知到该时间变化所产生的效果。配置性能数据采样周期时间越短，采样数据反馈的灵敏越高，系统开销也越高；反之，则采样数据反馈的灵敏越低，系统开销也越低。采样周期设置的长短，对采样数据结果的准确性都没有影响。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
performance update-interval 
  {10s 
|30s 
|60s 
} ＜check-point-type 
＞
no performance update-interval 
  ＜check-point-type 
＞
				
命令参数解释 : 
参数|描述
---|---
10s|<作用>用于配置性能管理接口计数器进行统计时的刷新时间间隔。设置性能管理接口计数器统计刷新时间间隔为10s
30s|<作用>用于配置性能管理接口计数器进行统计时的刷新时间间隔。设置性能管理接口计数器统计刷新时间间隔为30s
60s|<作用>用于配置性能管理接口计数器进行统计时的刷新时间间隔。设置性能管理接口计数器统计刷新时间间隔为60s
＜check-point-type＞|atm            atm端口检测点类型cpos           cpos端口检测点类型ethernet       以太端口检测点类型pos            pos端口检测点类型sub-interface  子接口端口检测点类型
缺省 : 
10s 
使用说明 : 
目前支持可配置的周期粒度包括：10秒，30秒，60秒。系统支持的检测点类型包括：atm，cpos，ethernet，pos，sub-interface。
范例 : 
修改ethernet类型端口计数器统计刷新周期间隔为30秒，则输入以下命令：ZXROSNG(config)# performance update-interval 30s ethernet
相关命令 : 
show running-config performance 
## performance zero-unsuppress 

performance zero-unsuppress 
命令功能 : 
该命令在全局配置模式下执行，用于取消零性能抑制的状态。一旦零性能抑制被取消，设备就会对数据为零的性能统计进行感知和处理。若此时设备上有零的性能统计，则用户在EMS网管上可查询到零值数据。设备对零性能统计的处理，可能会在一定程度上对设备负荷及效能有所影响。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
performance zero-unsuppress 
  {current-qtime 
|history-qtime 
|current-dtime 
|history-dtime 
}
no performance zero-unsuppress 
  {current-qtime 
|history-qtime 
|current-dtime 
|history-dtime 
}
				
命令参数解释 : 
参数|描述
---|---
current-qtime|当前15分钟
history-qtime|历史15分钟
current-dtime|当前24小时
history-dtime|历史24小时
缺省 : 
无 
使用说明 : 
该命令可以用于取消当前15分钟、当前24小时、历史15分钟、历史24小时零性能抑制。通过no performance zero-unsuppress命令，可将设备恢复为零性能抑制状态。零性能抑制状态下，设备不处理零值性能统计。
范例 : 
设置取消当前15分钟零性能抑制状态。，则输入以下命令：ZXROSNG(config)#performance zero-unsuppress current-qtime;
相关命令 : 
show running-config performance  
## show performance data-save-interval 

show performance data-save-interval 
命令功能 : 
该命令工作于除用户模式外的其他所有模式，用于查询应用性能历史数据的保存周期。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show performance data-save-interval 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
配置/修改性能历史数据保存周期的命令为performance data-save-interval。 
范例 : 
ZXROSNG(config)#show performance data-save-interval The interval of performance data-save is 15 minutes.
相关命令 : 
performance data-save-interval 
# 用户管理配置命令 
## access-deny 

access-deny 
命令功能 : 
access-deny命令用来设置禁止本地网元的接入方式。没有no命令。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
access-deny 
  {[lct 
],[qx 
],[dcn 
]}
命令参数解释 : 
参数|描述
---|---
lct|LCT端口接入
qx|QX端口接入
dcn|DCN端口接入
缺省 : 
缺省情况下，不限制本地网元的接入方式。 
使用说明 : 
网元接入方式有：LCT口、QX口和DCN口。access-only命令用来设置允许本地网元的接入方式。no access-only命令恢复默认配置，不限制网元接入方式。access-deny命令用来设置禁止本地网元的接入方式，没有no命令。
范例 : 
配置禁止网元LCT和QX端口接入，允许dcn方式接入：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#access-deny lct qxZXROSNG(config-system-user-author-temp)#show this!<system-user>    access-only dcn!</system-user>ZXROSNG(config-system-user-author-temp)#
相关命令 : 
access-only 
## access-only 

access-only 
命令功能 : 
access-only命令用来设置允许本地网元接入的方式。no access-only命令用来恢复默认配置。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
access-only 
  {[lct 
],[qx 
],[dcn 
]}
no access-only 
命令参数解释 : 
参数|描述
---|---
lct|LCT端口接入
qx|QX端口接入
dcn|DCN端口接入
缺省 : 
缺省情况下，允许所有接入 
使用说明 : 
网元接入方式有：LCT口、QX口和DCN口。access-only命令用来设置允许本地网元的接入方式。no access-only命令恢复默认配置，不限制网元接入方式。access-deny命令用来设置禁止本地网元的接入方式，没有no命令。
范例 : 
配置允许LCT和QX端口接入：ZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#access-only lct qx
相关命令 : 
access-deny 
## account-switch 

account-switch 
命令功能 : 
用于配置全局记账开关。支持用户操作在远端服务器记账。用户的操作可以在TACACS+服务器或RADIUS服务器上记录下来，便于日后查询。
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
account-switch 
  {off 
|on 
 accounting-template 
 ＜aaa-account-template 
＞}
no account-switch 
命令参数解释 : 
参数|描述
---|---
off|关闭全局记账开关
on|开启全局记账开关
＜aaa-account-template＞|用于指定全局记账AAA模板号。整数形式，取值范围是2001-2128。
缺省 : 
缺省情况，记账功能关闭。
使用说明 : 
1. 记账功能是将用户上下线和所有命令的操作记录发往服远端务器保存，目前支持TACACS+服务器和RADIUS服务器。2. 开启记账功能时需要指定绑定的AAA模板。
范例 : 
配置AAA记账模板，采用radius记账：ZXROSNG(config)#aaa-accounting-template 2001        ZXROSNG(config-aaa-acct-template)#aaa-accounting-type radiusZXROSNG(config-aaa-acct-template)#accounting-radius-group first group1开启记账功能，并绑定AAA记账模板2001：ZXROSNG(config)#system-userZXROSNG(config-system-user)#account-switch on accounting-template 2001
相关命令 : 
aaa-accounting-template
## authentication-method 

authentication-method 
命令功能 : 
用于配置用户认证方式为PAP或CHAP。no authentication-method 命令恢复默认配置。
命令模式 : 
 用户管理认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-method 
  {pap 
|chap 
}
no authentication-method 
命令参数解释 : 
参数|描述
---|---
pap|配置用户的认证方式为PAP
chap|配置用户的认证方式为CHAP
缺省 : 
缺省情况，认证方式为PAP。 
使用说明 : 
无
范例 : 
配置用户认证方式为CHAP：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#authentication-template 128ZXROSNG(config-system-user-authen-temp)#authentication-method chap ZXROSNG(config-system-user-authen-temp)#
相关命令 : 
无 
## authentication-template 

authentication-template 
命令功能 : 
该命令工作于用户管理模式，用于创建一个认证模板编号并进入此认证模板的配置模式。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-template 
  ＜authen-template 
＞
no authentication-template 
  ＜authen-template 
＞
				
命令参数解释 : 
参数|描述
---|---
＜authen-template＞|ADM_MGR的认证模板的编号，范围：1-128
缺省 : 
无 
使用说明 : 
最多可以配置128个认证模板信息。1.如果认证模板编号已经存在，则直接进人此认证模板配置模式。2.如果认证模板编号不存在，则新建一个认证模板，并进人此认证模板配置模式。进入认证模板配置模式后，主要可配置以下内容：1. description命令配置此认证模板的描述信息；2. bind aaa-authentication-template命令配置此认证模板绑定的AAA认证模板号；3. bind access-list命令配置此认证模板绑定的ACL名称；4. authentication-method命令配置绑定此认证模板的用户认证方式，认证方式包括pap、chap两种，如果不配置默认为pap方式。
范例 : 
配置认证模板128：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authentication-template 128ZXROSNG(config-system-user-authen-temp)#
相关命令 : 
无 
## authorization-template 

authorization-template 
命令功能 : 
该命令工作于用户管理模式，用于创建一个授权模板编号并进入此授权模板的配置模式。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
authorization-template 
  ＜author-template 
＞
no authorization-template 
  ＜author-template 
＞
				
命令参数解释 : 
参数|描述
---|---
＜author-template＞|ADM_MGR的授权模板的编号，范围：1-128
缺省 : 
无 
使用说明 : 
最多可以配置128个授权模板信息。1. 如果此授权模板编号已经存在，则直接进人此授权模板配置模式。2. 如果此授权模板编号不存在，则新建一个授权模板，并进人此授权模板配置模式。进入授权模板配置模式后，主要可配置以下内容：1. description命令配置此授权模板的描述信息;2. bind aaa-authorization-template命令配置此授权模板绑定的AAA授权模板号。3. local-privilege-level命令配置此授权模板本地授权级别。4. local-cmdgroup和local-cmdgroup-mode命令配置此授权模板的本地命令组名和本地命令组模式，从而可以限制用户可输入的命令，本地命令组模式包括：包含和排除。5. ftp top-directory或 sftp top-directory命令配置用户通过FTP或SFTP方式可访问的目录及权限，用户通过FTP或SFTP方式登录时只能按照配置的目录和权限进行访问和操作。权限包括：read-only、read-write、copy。6. logfile-allowed命令配置允许访问的日志类型和权限。7. login-sametime-max命令配置允许同时在线的最大用户数；8. login-type-allowed命令配置允许的接入类型；9. max-access命令配置接入的最大权限；
范例 : 
配置授权模板128：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 128ZXROSNG(config-system-user-author-temp)#
相关命令 : 
无 
## bind aaa-authentication-template 

bind aaa-authentication-template 
命令功能 : 
用于配置system-user认证模板绑定AAA认证模板。 
命令模式 : 
 用户管理认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
bind aaa-authentication-template 
  ＜aaa-authen-template 
＞
no bind aaa-authentication-template 
命令参数解释 : 
参数|描述
---|---
＜aaa-authen-template＞|用于指定AAA认证模板号。整数形式，取值范围是2001-2128。
缺省 : 
无配置 
使用说明 : 
无 
范例 : 
用户认证模板128绑定AAA认证模板2128：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authentication-template 128 ZXROSNG(config-system-user-authen-temp)#bind aaa-authentication-template 2128
相关命令 : 
aaa-authentication-template  
## bind aaa-authorization-template 

bind aaa-authorization-template 
命令功能 : 
用于配置system-user授权模板绑定AAA授权模板。 
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
bind aaa-authorization-template 
  ＜aaa-author-template 
＞
no bind aaa-authorization-template 
命令参数解释 : 
参数|描述
---|---
＜aaa-author-template＞|用于指定AAA授权模板号。整数形式，取值范围是2001-2128。
缺省 : 
无配置 
使用说明 : 
无 
范例 : 
配置用户授权模板128绑定AAA授权模板2128：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 128ZXROSNG(config-system-user-author-temp)#bind aaa-authorization-template 2128
相关命令 : 
aaa-authorization-template  
## bind access-list 

bind access-list 
命令功能 : 
用于配置用户接入认证阶段的访问控制列表。 
命令模式 : 
 用户管理认证模板模式  
命令默认权限级别 : 
15 
命令格式 : 
bind access-list 
  {ipv4 
 ＜acl-name 
＞|ipv6 
 ＜acl-name 
＞}
no bind access-list 
  {ipv4 
|ipv6 
}
				
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|IPv4访问控制列表名称。 字符串形式，取值范围是1-31个字符。
＜acl-name＞|IPv6访问控制列表名称。 字符串形式，取值范围是1-31个字符
No参数|描述
---|---
ipv4|IPv4 ACL
ipv6|IPv6 ACL
缺省 : 
无 
使用说明 : 
1.该命令仅绑定一个ACL名，仅支持源地址过滤。2.如果要创建ACL名称及其规则，需使用ACL模块的ipv4-access-list命令或ipv6-access-list命令创建ACL，使用rule命令配置规则。
范例 : 
以通过ACL规则，阻止用户zte登录设备为例，如果zte用户绑定的认证模板号是128，授权模板号是128，认证模板下绑定ACL规则名称为zte_acl，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authentication-template 128ZXROSNG(config-system-user-authen-temp)#bind access-list ipv4 zte_acl配置ACL，则输入以下命令：ZXROSNG(config)#ipv4-access-list zte_aclZXROSNG(config-ipv4-acl)# rule 1 deny tcp any any用户zte以telnet方式登录设备失败，提示“% ACL refused”：[root@localhost ~]# telnet 10.42.55.6Trying 10.42.55.6...Connected to 10.42.55.6 (10.42.55.6).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 23:52:59 01-12-2014Username:ztePassword:% ACL refused
相关命令 : 
ipv4-access-list ipv6-access-list 
## bind authentication-template 

bind authentication-template 
命令功能 : 
该命令工作于默认用户模式，用于本地不存在的用户绑定ADM_MGR认证模板。 
命令模式 : 
 默认用户模式  
命令默认权限级别 : 
15 
命令格式 : 
bind authentication-template 
  ＜authen-template 
＞
no bind authentication-template 
命令参数解释 : 
参数|描述
---|---
＜authen-template＞|用于指定ADM_MGR认证模板号。取值范围：1-128之间的整数。默认值：无。
缺省 : 
无配置 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-defaultZXROSNG(config-system-user-default)#bind authentication-template 1
相关命令 : 
user-defaultauthentication-template 
## bind authentication-template 

bind authentication-template 
命令功能 : 
该命令工作于用户名模式，用于用户账号绑定ADM_MGR认证模板。 
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
bind authentication-template 
  ＜authen-template 
＞
no bind authentication-template 
命令参数解释 : 
参数|描述
---|---
＜authen-template＞|用于指定ADM_MGR认证模板号。取值范围：1-128之间的整数。默认值：无。
缺省 : 
无 
使用说明 : 
无 
范例 : 
账号zte绑定认证模板128：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)# bind-authentication-template 128
相关命令 : 
user-name authentication-template 
## bind authorization-template 

bind authorization-template 
命令功能 : 
该命令工作于默认用户模式，用于本地不存在的用户绑定ADM_MGR授权模板 
命令模式 : 
 默认用户模式  
命令默认权限级别 : 
15 
命令格式 : 
bind authorization-template 
  ＜author-template 
＞
no bind authorization-template 
命令参数解释 : 
参数|描述
---|---
＜author-template＞|用于指定ADM_MGR授权模板号。取值范围：1-128。默认值：无
缺省 : 
无配置 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-defaultZXROSNG(config-system-user-default)#bind authorization-template 128
相关命令 : 
user-default authorization-template
## bind authorization-template 

bind authorization-template 
命令功能 : 
配置普通用户授权模板 
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
bind authorization-template 
  ＜author-template 
＞
no bind authorization-template 
命令参数解释 : 
参数|描述
---|---
＜author-template＞|ADM_MGR授权模板的编码，范围：1-128
缺省 : 
无配置 
使用说明 : 
无 
范例 : 
账号zte绑定授权模板1：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)#bind authorization-template 1
相关命令 : 
user-name authorization-template 1
## default-privilege-level 

default-privilege-level 
命令功能 : 
配置缺省权限等级 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
default-privilege-level 
  ＜level 
＞
no default-privilege-level 
命令参数解释 : 
参数|描述
---|---
＜level＞|权限值，范围：0-15
缺省 : 
缺省值为0 
使用说明 : 
在本地未配置权限或者授权失败的情况下使用默认权限 
范例 : 
设置缺省权限等级为6：ZXROSNG(config)#system-userZXROSNG(config-system-user)#default-privilege-level 6
相关命令 : 
local-privilege-level 
description : 

description 
命令功能 : 
用于配置system-user认证模板的描述信息。 
命令模式 : 
 用户管理认证模板模式  
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
＜description＞|指定认证模板描述信息。字符串形式，取值范围是1-127个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
配置认证模板128的描述信息为LocalAuthenticationTemplate，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authentication-template 128ZXROSNG(config-system-user-authen-temp)#description LocalAuthenticationTemplate
相关命令 : 
无 
description : 

description 
命令功能 : 
用于配置system-user授权模板的描述信息 
命令模式 : 
 用户管理授权模板模式  
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
＜description＞|描述信息。字符串形式，长度范围是1-127个字符。
缺省 : 
无配置 
使用说明 : 
无 
范例 : 
配置用户授权模板1的描述信息为LocalAuthorizationTemplate：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#description LocalAuthorizationTemplate
相关命令 : 
无 
description : 

description 
命令功能 : 
在用户角色模式下，设置该角色的描述信息。 
命令模式 : 
 用户角色模式  
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
＜description＞|角色描述信息，长度1~128个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
设置角色auditor的描述信息：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role auditorZXROSNG(config-system-user-role-auditor)#description person for auditing system
相关命令 : 
无 
description : 

description 
命令功能 : 
description命令用来设置任务组的描述信息。no description命令用来删除任务组描述信息。
命令模式 : 
 用户任务组模式  
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
＜description＞|指定的任务组描述信息。字符串形式，支持空格，长度范围是1~128
缺省 : 
缺省情况下，任务组没有描述信息。 
使用说明 : 
无 
范例 : 
设置任务组test的描述信息：ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup testZXROSNG(config-system-user-taskgroup-test)#description task for test operation
相关命令 : 
taskgroup 
## duplicated-password 

duplicated-password 
命令功能 : 
duplicated-password interval命令用来设置密码与历史密码相同的最小间隔次数。no duplicated-password命令用来恢复默认配置。
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
duplicated-password 
 interval 
 ＜times 
＞
no duplicated-password 
命令参数解释 : 
参数|描述
---|---
＜times＞|最小间隔次数。整数形式，取值范围是2-10
缺省 : 
缺省情况下，密码不能与最近5次以内的历史密码相同。 
使用说明 : 
最小间隔次数n，表示密码不能与之前n次历史密码相同，当前密码包含在n次历史密码之内，但与当前密码相同不视为与历史密码相同。 
范例 : 
设置密码不能与最近2次以内历史密码相同：ZXROSNG(config)#system-userZXROSNG(config-system-user)#duplicated-password interval 2创建账号test，密码为Test123!ZXROSNG(config-system-user)#user-name testZXROSNG(config-system-user-username)#password Test123!ZXROSNG(config-system-user-username)#修改密码为Test1234!ZXROSNG(config-system-user-username)#password Test1234!ZXROSNG(config-system-user-username)#修改密码为Test12345!ZXROSNG(config-system-user-username)#password Test12345!ZXROSNG(config-system-user-username)#修改密码为Test12345!，与当前密码相同，不报错ZXROSNG(config-system-user-username)#password Test12345!ZXROSNG(config-system-user-username)#修改密码为Test1234!，与最近2次以内历史密码相同，报错ZXROSNG(config-system-user-username)#password Test1234!%Error 59979: The password is duplicated with the latest 2 passwords configured!ZXROSNG(config-system-user-username)#修改密码为Test123!，不报错ZXROSNG(config-system-user-username)#password Test123!ZXROSNG(config-system-user-username)#用户登录时，提示修改密码，必须满足新密码不能与最近2次以内历史密码相同：[root@localhost ~]# telnet 10.42.55.93Trying 10.42.55.93...Connected to 10.42.55.93 (10.42.55.93).Escape character is '^]'.*****************************************************************Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation*****************************************************************Login at: 23:11:38 09-21-2017Username:whoPassword:Your password has expired.Enter a new one now.(The strong-password strategy is:Min Length            : 8Character Set         : number, capital, lowercase, special-characterUsername-related Check: The password cannot be the same as the username.)New password:The password is duplicated with the latest 2 passwords configuredPlease input your new password:
相关命令 : 
无 
## enable secret 

enable secret 
命令功能 : 
配置通过enable本地认证提升用户权限时的密码。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
enable secret 
 level 
 ＜level 
＞ [{0 
 ＜unencrypted-password 
＞|5 
 ＜encrypted-password 
＞|＜unencrypted-password 
＞}]
no enable secret 
 level 
 ＜level 
＞
				
命令参数解释 : 
参数|描述
---|---
＜level＞|指定权限等级，无缺省值，范围：1~$#218169346#$，218169346为性能参数ID
0|设置明文enable密码
＜unencrypted-password＞|enable密码明文。字符串形式，不支持空格，区分大小写，长度范围是3~16。
5|设置经过加密的enable密码
＜encrypted-password＞|enable密码密文。字符串形式，区分大小写，长度范围是24~200。
＜unencrypted-password＞|enable密码明文。字符串形式，不支持空格，区分大小写，长度范围是3~16。
缺省 : 
缺省情况下，对明文密码进行强密码检查。强密码策略是：密码不能少于8个字符，必须包含大小写字符、数字和特殊字符。enable secret level命令不带密码参数时，以交互式输入明文密码，输入字符显示为*。输入的密码为字符串形式，区分大小写，取值范围是8～16。
使用说明 : 
1.该命令配置的是enable认证方式是local时的密码。2.在show running-config中显示的enable密码是密文；3.使用enable提升用户权限时输入的密码是明文。4.目前密文密码长度，只支持24、63。（1）更安全的加slat加密方式，加密后密文长度为63个字符。（2）原来不太安全的加密方式，加密后密文长度为24个字符。
范例 : 
未加密的密码不符合强密码要求，报错ZXROSNG(config)#enable secret level 15 zte%Error 59997: The password cannot be less than 8 characters and must contain uppercase, lowercase, numbers and special characters.ZXROSNG(config)#当用户权限级别低于15级，且enable认证类型是local时，可通过enable命令提升权限至15级：ZXROSNG#show privilege Current privilege level is 10ZXROSNG#ZXROSNG#enable 15      Password:ZXROSNG#ZXROSNG#show privilege Current privilege level is 15ZXROSNG#低级别用户不允许配置高级别的enable密码ZXROSNG#show privilegeCurrent privilege level is 15ZXROSNG#ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#enable secret level 18 Test@1234%Error 59978: User privilege is too low.ZXROSNG(config)#交互式设置enable 15级密码为Hello_2019ZXROSNG(config)#enable secret level 15Please configure the password(8-16)Enter password:**********Confirm password:**********ZXROSNG(config)#
相关命令 : 
enableenable-typeglobal-enable-type
## enable-type 

enable-type 
命令功能 : 
用于配置用户enable认证的方式。 
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
enable-type 
  {local 
|aaa 
 authentication-template 
 ＜authen-template 
＞}
no enable-type 
命令参数解释 : 
参数|描述
---|---
local|用于指定用户的enable认证方式为本地认证。
aaa|用于指定用户的enable认证方式为AAA认证.
＜authen-template＞|用于指定system-user认证模板号。整数形式，取值范围是1-128。
缺省 : 
无配置 
使用说明 : 
1.enable认证方式包括：本地认证和AAA认证。当配置AAA认证时，需要指定认证模板。2.enable认证方式可以在全局配置模式下配置，也可以在用户名模式下配置。当配置的全局enable认证方式和用户名模式下的enable认证方式同时存在时，用户名模式下的enable认证方式优先级高于全局enable认证方式，用户名模式下的enable认证方式生效。3. 配置的认证方式是AAA时，支持到tacacs+和radius服务器认证。aaa-authentication-type是local-tacacs或local-radius时，如果本地没有配置enable密码，转tacacs+或radius认证；aaa-authentication-type是tacacs-local或radius-local时，如果服务器认证超时，转local认证。4. 大于15级的enable认证，只支持本地认证。
范例 : 
配置zte用户enable认证方式为aaa认证，模板号为128，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)#enable-type aaa authentication-template 128
相关命令 : 
global-enable-type 
## enable-type 

enable-type 
命令功能 : 
配置用户enable认证方式 
命令模式 : 
 默认用户模式  
命令默认权限级别 : 
15 
命令格式 : 
enable-type 
  {local 
|aaa 
 authentication-template 
 ＜authen-template 
＞}
no enable-type 
命令参数解释 : 
参数|描述
---|---
local|配置用户的enable认证方式为本地认证
aaa|配置用户的enable认证方式为aaa认证
＜authen-template＞|认证模板号范围1-128
缺省 : 
无配置 
使用说明 : 
1.enable认证方式包括：本地认证和AAA认证。当配置AAA认证时，需要指定认证模板。2.enable认证方式可以在全局配置模式下配置，也可以在用户名模式下配置。当配置的全局enable认证方式和用户名模式下的enable认证方式同时存在时，用户名模式下的enable认证方式优先级高于全局enable认证方式，用户名模式下的enable认证方式生效。3. 配置的认证方式是AAA时，支持到tacacs+和radius服务器认证。aaa-authentication-type是local-tacacs或local-radius时，如果本地没有配置enable密码，转tacacs+或radius认证；aaa-authentication-type是tacacs-local或radius-local时，如果服务器认证超时，转local认证。4. 大于15级的enable认证，只支持本地认证。
范例 : 
配置默认用户enable认证类型为AAA：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-default ZXROSNG(config-system-user-default)#enable-type aaa authentication-template 128
相关命令 : 
global-enable-type 
## ftp top-directory 

ftp top-directory 
命令功能 : 
ftp top-directory命令用来配置本地用户的FTP顶级目录和访问权限。no ftp top-directory命令用来取消本地用户的FTP顶级目录配置。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
ftp top-directory 
  ＜topdir-name 
＞ {read-only 
|{[read-write 
],[copy 
]}}
no ftp top-directory 
命令参数解释 : 
参数|描述
---|---
＜topdir-name＞|指定用户以FTP方式登录设备时所访问的顶级目录名称，必须是完整路径。字符串形式，长度范围是1-159。
read-only|只读
read-write|读写
copy|拷贝
缺省 : 
缺省情况下，本地用户的FTP顶级目录和访问权限来自ftp-server top-directory配置。 
使用说明 : 
应用场景当需要将设备配置为FTP服务器，从而便于本地用户以FTP方式登录设备，对设备上的文件进行增加、删除、修改等操作时，可以通过本命令配置本地用户以FTP方式登录设备后所处的目录。不指定该目录时，本地用户的FTP顶级目录和访问权限来自ftp-server top-directory配置。配置影响配置本命令后，本地用户通过FTP方式登录该设备时，将进入本命令所指定的目录。用户通过FTP访问日志文件时，受用户的日志文件访问权限限制（可通过logfile-allowed命令设置本地用户文件访问权限）。注意事项可通过ftp-server enable命令使能设备的FTP功能。本命令所指定的FTP目录必须是在设备上存在且合法的，即系统可识别的，否则本地用户将无法以FTP方式登录设备。本地用户的属性变更不会对当前在线用户产生影响，已在线用户重新登录之后此配置变更生效
范例 : 
范例1设置本地用户who的FTP顶级目录为/datadisk0/，权限为只读：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#bind authorization-template 1ZXROSNG(config-system-user-username)#exitZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#ftp top-directory /datadisk0/ read-only从FTP用户who的工作目录上将文件123.txt拷贝到设备的/datadisk0/test/目录，who用户只有read-only权限，拷贝失败：ZXROSNG#copy ftp vrf mng //10.42.55.93/123.txt@who:who root: /datadisk0/test/aaa.txtStart copying file%Error 51039: The file was not found or user didn't have the privilege.ZXROSNG#
范例2设置本地用户who的FTP顶级目录为/datadisk0/，权限为copy：ZXROSNG(config-system-user-author-temp)#ftp top-directory /datadisk0/ copy从FTP用户who的工作目录上将文件123.txt拷贝到设备的/datadisk0/test/目录：ZXROSNG#copy ftp vrf mng //10.42.55.93/123.txt@who:who root: /datadisk0/test/aaa.txtStart copying fileGot file successfully!Received 5 bytes!ZXROSNG#
设置本地用户who的告警日志文件访问权限为read-only：ZXROSNG(config-system-user-author-temp)#logfile-allowed alarm-log read-only从FTP用户who的工作目录上将告警日志文件拷贝到设备的/datadisk0/test/目录，who用户对告警日志文件只有read-only权限，拷贝失败：ZXROSNG#copy ftp vrf mng //192.168.100.250/LOG/ALARM/alarmlog_20180904201414_0.alm.log@zte:zte root: /datadisk0/test/ala.txtStart copying file%Error 51039: The file was not found or user didn't have the privilege.ZXROSNG#
设置本地用户who的告警日志文件访问权限为copy：ZXROSNG(config-system-user-author-temp)#logfile-allowed alarm-log copy从FTP用户who的工作目录上将告警日志文件拷贝到设备的/datadisk0/test/目录：ZXROSNG#copy ftp vrf mng //192.168.100.250/LOG/ALARM/alarmlog_20180904201414_0.alm.log@zte:zte root: /datadisk0/test/ala.txtStart copying fileGot file successfully!Received 15 bytes!ZXROSNG#
相关命令 : 
ftp-server top-directoryftp-server enable
## global-enable-type 

global-enable-type 
命令功能 : 
用于配置全局enable认证方式。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
global-enable-type 
  {local 
|aaa 
 authentication-template 
 ＜authen-template 
＞}
no global-enable-type 
命令参数解释 : 
参数|描述
---|---
local|配置全局的enable认证方式为本地认证
aaa|配置全局的enable认证方式为aaa认证
＜authen-template＞|指定enable认证system-user模板号。整数形式，取值范围是1-128。
缺省 : 
全局enable认证缺省本地认证
使用说明 : 
1.enable认证方式包括：本地认证和AAA认证。当配置AAA认证时，需要指定认证模板。2.enable认证方式可以在全局配置模式下配置，也可以在用户名模式下配置。当配置的全局enable认证方式和用户名模式下的enable认证方式同时存在时，用户名模式下的enable认证方式优先级高于全局enable认证方式，用户名模式下的enable认证方式生效。3. 配置的认证方式是AAA时，支持到tacacs+和radius服务器认证。aaa-authentication-type是local-tacacs或local-radius时，如果本地没有配置enable密码，转tacacs+或radius认证；aaa-authentication-type是tacacs-local或radius-local时，如果服务器认证超时，转local认证。4. 大于15级的enable认证，只支持本地认证。
范例 : 
配置全局enable认证为本地认证：ZXROSNG(config)#system-userZXROSNG(config-system-user)#global-enable-type local
相关命令 : 
enable-type 
## inherit role 

inherit role 
命令功能 : 
配置角色权限的继承。inherit role命令用来将指定角色的权限加入到当前角色中。no inherit role命令用来删除当前角色对指定角色的权限包含关系。
命令模式 : 
 用户角色模式  
命令默认权限级别 : 
15 
命令格式 : 
inherit role 
  ＜role-name 
＞
no inherit role 
  ＜role-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜role-name＞|继承的角色名，长度为1~48个字符
缺省 : 
缺省情况下，角色中没有添加对其他角色的权限包含关系。 
使用说明 : 
应用场景如果当前角色的权限需要完全继承另一角色的权限，或者当前角色需要继承已有角色的权限时，可在角色中配置继承关系，将指定角色的权限加入到当前角色中。当前角色的权限依赖于被继承角色的权限，当修改被继承角色的权限信息后，当前角色的权限也会随之修改。注意事项每个角色最多继承4个其他角色。如需改变继承的角色，需先执行no inherit role命令删除对已有角色的继承关系。该角色的权限是本角色权限和继承的角色权限的合集。继承具有传递性。继承形成环，即直接或间接的继承自己时没有意义，配置操作上不做限制。被继承的角色删除后，等价于没有继承角色，但继承关系依然存在，不会自动撤销。允许继承未创建的角色。
范例 : 
配置角色group1继承角色ug1的权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role group1ZXROSNG(config-system-user-role-group1)#inherit role ug1
相关命令 : 
roleshow role-based privilege role
## inherit taskgroup 

inherit taskgroup 
命令功能 : 
配置任务组的集成。inherit taskgroup命令用来将指定任务组的权限加入到当前任务组中。no inherit taskgroup命令用来删除当前任务组对指定任务组的权限包含关系。
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
inherit taskgroup 
  ＜taskgroup-name 
＞
no inherit taskgroup 
  ＜taskgroup-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜taskgroup-name＞|继承的任务组名，长度为1~48个字符
缺省 : 
缺省情况下，任务组中没有添加对其他任务组的权限包含关系。 
使用说明 : 
应用场景如果当前任务组的权限需要完全继承另一任务组的权限，或者当前任务组需要继承已有任务组的权限时，可在任务组中配置继承关系，将指定任务组的权限加入到当前任务组中。当前任务组的权限依赖于被继承任务组的权限，当修改被继承任务组的权限信息后，当前任务组的权限也会随之修改。注意事项每个任务组最多继承4个其他任务组。如需改变继承的任务组，需先执行no inherit taskgroup命令删除对已有任务组的继承关系。继承具有传递性。继承形成环，即直接或间接的继承自己时没有意义，配置操作上不做限制。被继承的任务组删除后，等价于没有继承任务组，但继承关系依然存在，不会自动撤销。允许继承不存在的任务组。
范例 : 
配置任务组group1包含任务组tg1的权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup group1ZXROSNG(config-system-user-taskgroup-group1)#inherit taskgroup tg1
相关命令 : 
taskgrouprole
## local-cmdgroup 

local-cmdgroup 
命令功能 : 
用于为用户授权模板绑定本地命令组。通过该命令配置，用户可以自定义命令组，并将命令组内的命令作为命令授权的一部分，追加授权给指定的用户。被追加命令授权的用户，除了可以执行其CLI级别与其授权级别相当或低于的命令之外，还应能支持追加授权的命令。通过在授权模板中配置本地命令组名和本地命令组模式，从而限制用户可以输入的命令。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
local-cmdgroup 
  ＜group-name 
＞
no local-cmdgroup 
  ＜group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|指定命令组名。字符串形式，取值范围是1~31个字符。
缺省 : 
无 
使用说明 : 
1.一个授权模板，最多可以绑定4个命令组；可以绑定一个不存在的命令组，则此命令组的授权为空。2.删除授权模板时，关联删除命令组绑定关系。3.使用命令cmdgroup ＜cmdgroup＞创建命令组，并进入命令组模式。在命令组模式下，使用命令commands <command_logicalmode> { include {all |<command>}  | exclude <command>}定义命令匹配规则，符合匹配条件的命令，被命令组包含。4.将命令组删除时，该命令组规则自动删除。
范例 : 
创建命令组test，并定义命令匹配规则为：包含配置模式下的system-user命令、包含adm-mgr模块的所有命令，则输入以下命令：ZXROSNG(config)#cmdgroup testZXROSNG(config-cmdgrp)#commands adm-mgr include-allZXROSNG(config-cmdgrp)#commands configure include system-user授权模板1绑定命令组test，命令组使用方式为默认的追加方式，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#local-cmdgroup testZXROSNG(config-system-user-author-temp)#使用授权模板1的who用户登录成功后，用户权限级别是10，who用户被追加了执行用户管理所有命令的权限：ZXROSNG#show privilege Current privilege level is 10ZXROSNG#con tEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#system-user ZXROSNG(config-system-user)#
相关命令 : 
local-cmdgroup-modecmdgroupcommands 
## local-cmdgroup-mode 

local-cmdgroup-mode 
命令功能 : 
该命令工作于用户管理授权模板模式，用于定义命令组使用方式为独享方式，缺省为追加方式。通过在授权模板中配置本地命令组名和本地命令组模式，从而限制用户可以输入的命令。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
local-cmdgroup-mode 
  {exclusive 
}
no local-cmdgroup-mode 
命令参数解释 : 
参数|描述
---|---
exclusive|用于指定命令组使用方式为独享方式，仅授权绑定的命令组。
缺省 : 
缺省为追加方式 
使用说明 : 
配置授权模板使用仅使用绑定命令组授权 
范例 : 
配置命令组授权模式为独享方式：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#local-cmdgroup-mode exclusive
相关命令 : 
local-cmdgroup 
## local-privilege-level 

local-privilege-level 
命令功能 : 
配置本地授权等级 
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
local-privilege-level 
  ＜level 
＞
no local-privilege-level 
命令参数解释 : 
参数|描述
---|---
＜level＞|权限值，范围：0-15
缺省 : 
无配置 
使用说明 : 
1.使用本地授权方式或者在服务器转本地后使用该权限进行授权2.如果本地授权，没有配置local-privilege-level，使用default-privilege-level值授权
范例 : 
配置授权模板1的本地授权等级为15：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#local-privilege-level 15
相关命令 : 
default-privilege-level 
## lock 

lock 
命令功能 : 
主动锁定或者解锁本地用户，被锁定的用户不允许登录。 
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
lock 
 
no lock 
命令参数解释 : 
					无
				 
缺省 : 
命令不使能 
使用说明 : 
该命令配置生效后，不会对本地账号已经建立的在线连接产生影响。用户帐号被锁定之后，只能通过no lock命令手动解锁。
范例 : 
执行lock命令锁定本地账号zte：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)#lock账号zte被锁，使用账号zte登录设备提示“% User is locked”[root@localhost test]# telnet 10.42.55.93Trying 10.42.55.93...Connected to 10.42.55.93 (10.42.55.93).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 02:50:53 09-14-2017Username:ztePassword:% User is lockedUsername:
相关命令 : 
无 
## logfile-allowed 

logfile-allowed 
命令功能 : 
配置授权模板允许访问的日志类型或带有指定后缀的日志文件，设定相应日志访问权限。 
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
logfile-allowed 
  {cmd-log 
|alarm-log 
|nat-log 
|service-log 
|＜log-suffix 
＞} [{none 
|read-only 
|{[read-write 
],[copy 
]}}]
no logfile-allowed 
  [{cmd-log 
|alarm-log 
|nat-log 
|service-log 
|＜log-suffix 
＞}]
				
命令参数解释 : 
参数|描述
---|---
cmd-log|命令日志
alarm-log|告警日志
nat-log|NAT日志
service-log|业务日志
＜log-suffix＞|日志文件后缀，长度1-32个字符
none|无权限
read-only|只读
read-write|读写（包含读、写、创建、删除、重命名，不包含拷贝）
copy|拷贝（包含读、拷贝）
缺省 : 
缺省情况下，命令日志的权限和当前的终端等级有关。其它日志文件有全部的访问权限。 
使用说明 : 
1. 缺省情况下，授权模板没有配置任何类型日志文件的访问权限。2. 当用户和授权模板绑定时，用户TELNET、SSH、FTP等登录后对日志文件的操作权限就会受该命令限制。如果打开了串口认证，用户通过串口登录后，对日志文件的操作权限也受该命令限制。3. 可以配置授权模板具有多个类型日志文件的访问权限，no命令用于删除对某个类型日志文件的访问权限，no命令如果不指定日志类型，则删除对所有类型日志文件的访问权限。4. 当某个账号已登录，此时若修改该账号可访问的日志类型或权限，则不对已登录的用户生效，下一次登录时才生效。5. 不配置允许访问的日志类型和日志访问权限时，对于命令日志，如果用户级别高于对应的命令日志的级别，允许用户进行所有操作，如果用户级别低于对应的命令日志级别，不允许用户进行所有操作，对于其他日志，允许用户进行所有操作。
范例 : 
配置绑定授权模板128的用户日志权限为：命令日志访问权限为只读、告警日志没有访问权限、后缀为.config的文件访问权限为copy，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-systemuser)#authorization-template 128ZXROSNG(config-system-user-author-temp)#logfile-allowed cmd-log read-onlyZXROSNG(config-system-user-author-temp)#logfile-allowed alarm-log noneZXROSNG(config-system-user-author-temp)#logfile-allowed config copy绑定授权模板128的用户登录后，访问日志文件：ZXROSNG#dir /datadisk0/LOG/ALARMDirectory of MPU-0/20/0: /datadisk0/LOG/ALARM4061572  KB total (1257360 KB free)        attribute   size       date        time         name1       <DIR>       4096       07-27-2017  03:04        .2       <DIR>       4096       07-27-2017  03:04        ..ZXROSNG#ZXROSNG#dir /sysdisk0/usrcmd_logDirectory of MPU-0/20/0: /sysdisk0/usrcmd_log4031680  KB total (257404 KB free)        attribute   size       date        time         name1       <DIR>       4096       09-05-2017  03:26        .2       <DIR>       4096       09-05-2017  03:26        ..3       ----        2303043    09-21-2017  09:22        cmdlog_20170905032639_0.                                                        cmd.logZXROSNG#
相关命令 : 
authorization-template  
## login block 

login block 
命令功能 : 
配置和激活远程登录防攻击监测功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
login block 
  ＜block-seconds 
＞ attempts 
 ＜try-times 
＞ within 
 ＜watch-seconds 
＞
no login block 
命令参数解释 : 
参数|描述
---|---
＜block-seconds＞|阻塞时间（安静期的时长）。单位是秒。范围1~65535。
＜try-times＞|最大失败尝试次数。范围1~65535。
＜watch-seconds＞|监测周期，单位是秒。范围1~65535。
缺省 : 
无 
使用说明 : 
应用场景：为更好地防御远程登录攻击和暴力破解攻击，我们在远程登录功能防攻击监测中引入阻塞（Block）和安静模式（quiet mode）的概念。通过使能防攻击检测策略，可以设置路由器设备在发现有重复的远程登录尝试失败时，以阻塞的方式拒绝所有远程登录请求。这种阻塞可配置为一段时间，称为“安静期”。防攻击检测功能启动后，1）初始为“正常模式”，防攻击检测功能启动后，就进入“监测模式”；2）进入“监测模式”后，如果在“监测周期”或更短时间内，按登录类型分别统计失败尝试次数（不区分用户和地址），失败尝试的次数达到“最大失败尝试次数”，则切换到“安静模式”，上报告警通知，否则仍然是“监测模式”；3）进入“安静模式”后，开始计时，如果时间达到“阻塞时间（安静期时长）”，则切换到“监测模式”，并上报告警通知。4）进入“安静模式”后，如果通过login quiet-mode命令配置了安静期访问控制列表，则接受访问控制表允许的用户的登录请求。5）进入“安静模式”后，不会对已经建立的在线连接产生影响。
范例 : 
配置并启动远程登录防攻击检测功能，策略是在100秒内登录连续失败超过15次则进入安静模式，安静期为200秒：ZXROSNG(config)#login block 200 attempts 15 within 100 进入安静期上报告警通知ZXROSNG#show  alarm notification code 360102A notification 360102 ID 35 level 7 occurred at 17:11:23 10-02-2018 sent by ZXR10 MPU-0/20/0%ADM-MGR% Enter quiet mode.  %SEC_TELNET_LOGIN-QUIET_MODE_ON:Still timeleft for watching failures is 92 seconds,[user:who] [Source:192.168.100.1][Reason:Invalid login],[ACL:]ZXROSNG#
退出安静期上报告警通知ZXROSNG#show  alarm notification code 360103A notification 360103 ID 36 level 7 occurred at 17:13:23 10-02-2018 sent by ZXR10 MPU-0/20/0%ADM-MGR% Quit quiet mode.  %SEC_TELNET_LOGIN-QUIET_MODE_OFF:Quiet Mode is OFF,because block period timed out.ZXROSNG#
相关命令 : 
show loginshow login stateshow login failurelogin quiet-modelogin on-failure
## login on-failure 

login on-failure 
命令功能 : 
启动防攻击监测功能后，用于配置在有失败的登录尝试时上报告警通知。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
login on-failure 
 alarm 
 [every 
 ＜failure-tries 
＞]
no login on-failure 
命令参数解释 : 
参数|描述
---|---
＜failure-tries＞|失败登录次数，范围1~100，表示每<failure-tries>次失败登录才发一次告警通知。可选参数，如果不指定，则默认为1
缺省 : 
缺省情况下，登录失败尝试不上报告警通知。 
使用说明 : 
必须先启动防攻击监测功能，该命令才有效。启动防攻击监测功能后，监测模式下，该命令都有效。进入静默期后，不上报告警通知。
范例 : 
配置并启动远程登录防攻击检测功能，策略是在300秒内登录连续失败超过15次则进入安静模式，安静期为180秒：ZXROSNG(config)#login block 180 attempts 15 within 300配置在有失败的登录尝试时，每失败10次产生告警：ZXROSNG(config)#login on-failure alarm every 10who用户telnet方式登录设备，登录失败10次产生一次告警：ZXROSNG(config)#show alarm notification code 360104A notification 360104 ID 767 level 7 occurred at 06:03:00 09-22-2017 sent by ZXR10 MPU-0/20/0%ADM-MGR% Record failure.  %SEC_LOGIN_FAILED:Login failed [user:who] [Source:10.42.55.99][Access Type:TELNET] [Reason:Invalid login]
相关命令 : 
show login failureshow login stateshow alarm notificationlogin quiet-modelogin block
## login quiet-mode 

login quiet-mode 
命令功能 : 
用于远程登录防攻击监测功能，配置安静期的访问控制列表。no命令用于删除配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
login quiet-mode 
  {ipv4-access-list 
 ＜ipv4-acl 
＞|ipv6-access-list 
 ＜ipv6-acl 
＞}
no login quiet-mode 
  {ipv4-access-list 
|ipv6-access-list 
}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-acl＞|指定IPv4访问控制列表名。字符串形式，取值范围是1-31个字符。
＜ipv6-acl＞|指定IPv6访问控制列表名。字符串形式，取值范围是1-31个字符。
No参数|描述
---|---
ipv4-access-list|IPv4 ACL
ipv6-access-list|IPv6 ACL
缺省 : 
缺省情况，没有配置安静期的访问控制列表。
使用说明 : 
进入“安静模式”后，如果没有配置该命令，在安静期所有的登录请求都不会被处理。进入“安静模式”后，如果已配置安静期访问控制列表，则接受访问控制表允许的用户的登录请求。
范例 : 
配置安静期的访问控制列表：ZXROSNG(config)#login quiet-mode access-list trust-user
相关命令 : 
login blockshow loginshow login statelogin on-failure
## login 

login 
命令功能 : 
用于配置全局认证、授权的方式。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
login 
 ascii 
 authentication-template 
 ＜authen-template 
＞ [authortication-template 
 ＜author-template 
＞]
no login 
命令参数解释 : 
参数|描述
---|---
ascii|用于指定认证类型为ASCII。
＜authen-template＞|用于指定认证模板号。整数形式，取值范围是1-128。
＜author-template＞|用于指定授权模板号。整数形式，取值范围是1-128。
缺省 : 
无配置 
使用说明 : 
1. 配置login ascii全局认证、授权模板后，用户绑定的认证、授权模板不生效，所有用户统一按照该配置进行认证、授权。2.配置login ascii不指定授权模板：a)本地用户按照用户绑定的授权模板进行授权；b)本地不存在的服务器用户，如果配置了user-default绑定授权模板，按照user-default模式下绑定的模板授权；如果没有配置user-default绑定授权模板，按照default-privilege-level授权。3.login ascii绑定不存在的授权模板时，按照default-privilege-level授权。
范例 : 
1. 配置全局ascii认证，认证模板号为128、授权模板号为128：ZXROSNG(config)#system-userZXROSNG(config-system-user)#login ascii authentication-template 128 authortication-template 1282.希望本地用户在本地认证、授权，本地不存在的用户到远端服务器进行tacacs(ASCII)认证、授权，可通过如下配置实现：a)AAA认证模板2001的认证方式为local-tacacs，实现本地用户在本地认证，本地不存在的用户到tacacs服务器认证ZXROSNG(config)#aaa-authentication-template 2001ZXROSNG(config-aaa-authen-template)#aaa-authentication-type local-tacacsZXROSNG(config-aaa-authen-template)#authentication-tacacs-group testgroupZXROSNG(config-aaa-authen-template)#exitZXROSNG(config)#b) AAA授权模板2002的授权方式为tacacs优先，user-default模式下绑定该模板，当login ascii不指定授权模板时，本地不存在的tacacs服务器用户，按照该模板到tacacs+服务器授权ZXROSNG(config)#aaa-authorization-template 2002ZXROSNG(config-aaa-author-template)#aaa-authorization-type tacacsZXROSNG(config-aaa-author-template)#authorization-tacacs-group testgroupZXROSNG(config-aaa-author-template)#exitZXROSNG(config)#c) 用户认证模板1绑定AAA认证模板2001ZXROSNG(config)#system-userZXROSNG(config-system-user)#authentication-template 1ZXROSNG(config-system-user-authen-temp)#bind aaa-authentication-template 2001 ZXROSNG(config-system-user-authen-temp)#exitd) 用户授权模板2绑定AAA认证模板2002ZXROSNG(config-system-user)#authorization-template 2ZXROSNG(config-system-user-authen-temp)#bind aaa-authorization-template 2002         ZXROSNG(config-system-user-authen-temp)#exite) 配置全局ASCII认证，指定认证模板为1，不指定授权模板ZXROSNG(config-system-user)#login ascii authentication-template 1f) 配置user-default模式绑定授权模板2：ZXROSNG(config-system-user)#user-default ZXROSNG(config-system-user-default)#bind authorization-template 2ZXROSNG(config-system-user-default)#g) 本地用户绑定的授权模板的AAA授权方式必须local优先，且配置local-privilege-level
相关命令 : 
authentication-templateauthorization-templatebind aaa-authentication-templatebind aaa-authorization-template
## login-sametime-max 

login-sametime-max 
命令功能 : 
login-sametime-max命令用来配置同一本地用户同时在线的最大数目。超过后，使用该用户名进行本地认证接入的用户将被拒绝。no login-sametime-max命令用来取消接入数目的限制。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
login-sametime-max 
  ＜max-number 
＞
no login-sametime-max 
命令参数解释 : 
参数|描述
---|---
＜max-number＞|指定允许用户接入的最大数目。整数形式，取值范围是1～60。
缺省 : 
缺省情况下，不限制用户的同时在线数目。 
使用说明 : 
应用场景:为了更方便地管理用户访问设备，可以采用该命令限制同一本地账户的在线数量。超过接入限制后，使用该用户名进行本地认证接入的用户将被拒绝。配置影响:1）当用户名和授权模板绑定后，用户同时接入数目就会受该命令限制。接入数目统计的是同一账号同时通过TELNET、SSH或FTP等方式共同累计的接入次数，如果串口认证打开了，串口认证的次数也统计在内。2）某个账号超过接入限制后，使用该用户名进行本地认证接入的用户将被拒绝。3）如果配置的限制数目小于当前某个用户已登录次数时，使用该用户名进行本地认证接入的用户将被拒绝，但已登录用户的不下线。
范例 : 
配置用户授权模板1下允许最大同时在线用户数为10：ZXROSNG(config)#system-userZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#login-sametime-max 10账号who已在线数超过允许的最大数时，提示“% The number of online users has reached the maximum”[root@localhost test]# telnet 10.42.55.93Trying 10.42.55.93...Connected to 10.42.55.93 (10.42.55.93).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 02:54:06 09-14-2017Username:whoPassword:% The number of online users has reached the maximumUsername:
相关命令 : 
authorization-template  
## login-type-allowed 

login-type-allowed 
命令功能 : 
login-type-allowed命令用来配置用户的接入类型。no login-type-allowed命令用来恢复缺省配置。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
login-type-allowed 
  {[{{[console 
],[only-telnet 
]}|telnet 
}],[ssh 
],[ftp 
],[web 
]}
no login-type-allowed 
命令参数解释 : 
参数|描述
---|---
console|允许用户通过console接入
only-telnet|允许用户通过Telnet方式接入
telnet|允许用户通过Telnet方式和串口接入
ssh|允许用户通过SSH方式接入（包括：STelnet，SNETCONF，SFTP）
ftp|允许用户通过FTP方式接入
web|允许用户通过WEB方式接入
缺省 : 
缺省情况下，不限制用户的接入类型。 
使用说明 : 
应用场景：为防止本地用户通过某种认证方式认证成功之后，修改设备的配置，需要通过本命令对用户登录设备的服务类型进行限制。系统提供对用户的接入类型管理（通过在用户绑定的授权模板下配置允许的接入类型），只有用户的接入方式与系统为该用户配置的接入类型匹配，用户才能登录。注意事项：使用该命令选择允许的接入类型，可以选择一种或者多种。未选择的类型即为不允许的接入类型，限制串口接入，需要开启串口认证。
范例 : 
设置who用户的接入类型为Telnet(不含串口)、FTP：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#bind authorization-template 1ZXROSNG(config-system-user-username)#exitZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#login-type-allowed only-telnet ftp限制串口接入后，开启串口认证，使用串口登录报错“% Invalid access”ZXR10 Con0 is now availablePress RETURN to get started.*****************************************************************Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation*****************************************************************Login at: 06:25:54 09-20-2017Username:whoPassword:% Invalid accessUsername:
相关命令 : 
authorization-template 
## max-access 

max-access 
命令功能 : 
用于配置用户执行命令的权限。no命令恢复缺省配置，即不限制用户执行命令的权限。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
max-access 
  {read-write 
|read-only 
}
no max-access 
命令参数解释 : 
参数|描述
---|---
read-write|读写权限
read-only|只读权限
缺省 : 
缺省情况下，用户具有读写权限。 
使用说明 : 
1)串口接入用户权限不受该配置影响。2)read-write表示用户能够执行配置命令和查询命令，read-only表示用户只能执行查询命令。
范例 : 
配置账号zte只能执行show命令，即授权模板只有read-only权限：ZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#max-access read-onlyZXROSNG#con t%Error 141200: Operation is denied due to authorization failed.ZXROSNG#
相关命令 : 
无 
## once-password 

once-password 
命令功能 : 
用于配置用户第一次登录时必须修改密码，以便保证用户账号的安全。 
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
once-password 
 
no once-password 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况，首次登录不强制修改密码。 
使用说明 : 
使用该命令配置一次性密码。用户使用一次性密码登录时强制修改密码。新密码必须满足当前强密码要求。密码修改成功后，一次性密码自动删除，新密码生效。
范例 : 
配置账号zte的密码为一次性密码：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)#once-password使用zte账号第一次登录时，强制要求修改密码：[root@localhost ~]# telnet 10.42.55.6Trying 10.42.55.6...Connected to 10.42.55.6 (10.42.55.6).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 02:49:11 08-16-2013Username:ztePassword:Your password has expired.Enter a new one now.(The strong-password strategy is:  Min Length            : 8  Character Set         : number, capital, lowercase, special-character  Username-related Check: The password cannot be the same as the username.)New password:Re-enter new password:The password has been changed successfully,Please remember your new password!ZXROSNG#
相关命令 : 
无 
## password 

password 
命令功能 : 
password命令用于配置用户的登录口令no password命令用于删除用户的登录口令
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
password 
  [{irreversible 
 {encrypted 
 ＜encrypted-irreversible 
＞|＜password 
＞}|{encrypted 
 ＜encrypted-none-irreversible 
＞|＜password 
＞}}]
no password 
命令参数解释 : 
参数|描述
---|---
irreversible|选择关键字irreversible时，对明文密码进行加salt加密，采用的不可逆加密算法是SHA-256。不选择关键字irreversible时，明文密码进行可逆加密，采用的可逆加密算法是AES-256。无论是明文输入还是密文输入，配置文件中都以密文形式体现。
＜encrypted-irreversible＞|字符串形式，区分大小写，长度范围是63~200。当设置的密文长度为63个字符时，认为是加salt加密，格式必须为：$5$salt$encrypted中salt是长度为16个字符的随机字符串，encrypted是长度为43的字符串。
＜password＞|用于设置明文密码。密码以明文形式输入，字符串形式，区分大小写，未设置强密码最小长度时，长度范围是3～64。开启强密码策略后，密码不能与用户名相同。
＜encrypted-none-irreversible＞|用于设置可逆的密文密码，密码以密文形式输入，字符串形式，区分大小写，长度范围是64~200。
＜password＞|用于设置明文密码。密码以明文形式输入，字符串形式，区分大小写，未设置强密码最小长度时，长度范围是3～64。开启强密码策略后，密码不能与用户名相同。
缺省 : 
缺省情况下，本地用户没有缺省口令。password命令不带参数时，密码以交互式输入，输入字符显示为*。输入的密码为字符串形式，区分大小写，缺省取值范围是8～64。关闭强密码检查时，长度范围是3～64。交互式设置的密码采用不可逆加密。
使用说明 : 
应用场景通过用户账号+登录口令进行认证的Telnet、SSH、SNETCONF、SFTP、FTP、WEB等方式访问设备时，需要创建本地用户并配置该用户的登录口令。创建本地用户并配置该用户的登录口令后，当以该用户名登录设备时，需要输入正确的登录口令才能够顺利登录。配置影响缺省情况下，对于密码的设置要求：(1)密码必须大于等于8个字符。(2)密码必须包含数字、大写字母、小写字母、特殊字符（不包括？和空格）。密码中允许包含的字符有： !    “    #    $    %    &    `    (    )    *    +    ,    -    .    /    0    1     2    3    4    5    6    7    8    9    :    ;     <    =    >     @    A    B    C    D    E    F    G    H    I    J    K    L    M    N    O     P    Q    R    S    T    U    V    W    X    Y     Z    [    \    ]    ^    _    ‘    a    b    c     d    e    f    g    h    i    j    k    l    mn    o    p    q    r    s    t    u    v    w     x    y    z    {    |    }    ~(3)密码与用户名不能完全相同。(4)密码不能与之前5次内的历史密码相同。对于密码与用户名相关的设置规则在配置命令strong-password username-related-chk后要求更严格：(1)密码不能是用户名的反向串（大小写敏感）。(2)用户名和密码，二者中较短的作为子串，长串不能包含子串（大小写不敏感）对于密码中日期相关的设置规则在配置命令strong-password date-check enable后要求：(1)密码中不允许包含从1970年1月1日至2037年12月31日之间的日期；(2)密码中不允许包含YYYY-MM-DD、MM-DD-YYYY、DD-MM-YYYY、YYYYMMDD、MMDDYYYY、DDMMYYYY 六种日期格式。可通过strong-password check disable命令关闭强密码检查。无论是明文输入还是密文输入，配置文件中都以密文形式体现。目前可逆密文密码长度，只支持64、67、128、131，不可逆密文密码长度，只支持63、64。配置完成后，通过show username命令查看本地用户属性时，用户口令将以密文形式显示。注意事项本地用户的属性变更不会对当前在线用户产生影响，已在线用户重新登录之后此配置变更生效。
范例 : 
1）创建一个本地用户，用户名为hello，非交互式输入密码为Hello_2019ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name helloZXROSNG(config-system-user-username)#password Hello_20192）创建一个本地用户，用户名为hello，交互式输入密码为Hello_2019ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name helloZXROSNG(config-system-user-username)#passwordPlease configure the password(8-64)Enter password:**********Confirm password:**********ZXROSNG(config-system-user-username)#3）创建一个本地用户，用户名为hello，非交互式输入密码为Hello_2019，指定不可逆加密ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name helloZXROSNG(config-system-user-username)#password irreversible Hello_20194）创建一个本地用户，用户名为hello，非交互式输入密文密码ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name helloZXROSNG(config-system-user-username)#password encrypted $2$a683f5b691c940a6dd48bde2402d58c9b524842e8e1152e4f08119cb5d8bffa4
相关命令 : 
user-namestrong-passwordstrong-password checkstrong-password username-related-chkshow strong-password-info
## password-dictionary 

password-dictionary 
命令功能 : 
password-dictionary password命令用来设置密码字典。no password-dictionary password命令用来删除密码字典中的密码。
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
password-dictionary 
 password 
 ＜password 
＞
no password-dictionary 
  {password 
 ＜password 
＞|all 
}
				
命令参数解释 : 
参数|描述
---|---
＜password＞|密码，长度范围3~64。
No参数|描述
---|---
all|删除密码字典中的所有密码
缺省 : 
缺省情况下，密码字典中无密码。 
使用说明 : 
1.根据系统安全需求不同，管理员可以设置密码字典，如果同时开启了用户账号密码的密码字典功能，则用户在设置和修改密码时，输入的密码如果和密码字典中的某个密码相同时，则系统将不允许配置，并给出错误提示。2.配置密码字典中的密码时，密码长度限制在3~64个字符，如果超过限制，则系统将不允许配置，并给出错误提示，密码中的字符可以包括数字、大写字母、小写字母和特殊字符（~`!@#$%^&*()_+-={}|[]\:”;’<>,./），特殊字符不包括“？”和空格。3.删除密码字典中的某个密码时，必须输入和密码字典中完全匹配的一个密码，才能删除成功，否则系统将不能删除，并给出错误提示。4.输入no命令时，如果指定all参数，则将批量删除密码字典中的所有密码，删除前，系统会交互式提示用户再次确认，用户确认后才会删除，否则取消删除。5. 关闭强密码检查（strong-password check disable），密码字典功能不生效。
范例 : 
向密码字典中添加密码：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#password-dictionary password Zte123!!ZXROSNG(config-system-user)#password-dictionary password NanJing12%打开密码字典功能：ZXROSNG(config-system-user)#strong-password dictionary 配置的密码不允许与密码字典中的相同，报错：ZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)#password Zte123!!%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#password NanJing12%%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#删除密码字典中一个密码ZXROSNG(config-system-user)#no password-dictionary password Zte123!!ZXROSNG(config-system-user)#
删除密码字典中所有密码ZXROSNG(config-system-user)#no password-dictionary allDelete all passwords in dictionary (yes/no)?yesZXROSNG(config-system-user)#
相关命令 : 
strong-passwordstrong-password checkshow password-dictionarystrong-password username-related-chkshow strong-password-info
## password-duration 

password-duration 
命令功能 : 
password-duration用来配置密码过期时间。no password-duration命令用来取消密码过期时间配置。
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
password-duration 
  {＜no-duration 
＞|＜duration 
＞ [change-password-expired 
]}
no password-duration 
命令参数解释 : 
参数|描述
---|---
＜no-duration＞|取值为0，则表示密码永不过期。
＜duration＞|指定用户密码的过期天数。整数形式，取值范围90～360。
change-password-expired|密码超期之后允许修改密码
缺省 : 
缺省情况，用户密码永不超期。配置密码有效期时间非0，缺省情况，密码过期前3天提醒用户修改密码。
使用说明 : 
应用场景:为避免出现长期不修改密码，账号被盗用等安全问题，执行此命令配置密码过期时间。配置影响:在密码过期前3天，每次用户登录时都会提示用户修改密码，过期前上报告警。如果超过设置的过期时间，用户仍然不更改密码，该用户不能再登录。注意事项：1.密码有效期天数从密码设置时间开始计算，通过show username命令查看密码设置时间（set-time）和密码剩余有效天数（AgingTime）。
范例 : 
配置who帐号密码永不过期：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#password-duration 0配置who帐号密码有效期限为90天：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#password-duration 90ZXROSNG#show usernameUsername    Encrypted-Password       AuthenNo. AuthorNo. AgingTime Set-Timewho         e09a66ada5ddf9e2c17976f9 128       128       2         19:46:25 07-06-2018            88fa508b43c2b6636096567d            62fac3390409d8b2ZXROSNG#密码超期前上报告警：ZXROSNG#show alarm currentAn alarm 360101 ID 30 level 5 occurred at 16:58:02 10-02-2018 sent by ZXR10 MPU-0/20/0%ADM-MGR% User-account will expire.  User-account who will expire in 2 day(s).ZXROSNG#默认情况，密码过期前3天提醒：[root@localhost ~]# telnet 10.42.55.93Trying 10.42.55.93...Connected to 10.42.55.93 (10.42.55.93).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 16:58:46 10-02-2018Username:whoPassword:Your password will expire 3 day(s) later.Please delete it or change the password.ZXROSNG#密码已超期提醒：[root@localhost ~]# telnet 10.42.55.93Trying 10.42.55.93...Connected to 10.42.55.93 (10.42.55.93).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 00:38:20 10-05-2018Username:whoPassword:% User password expiredUsername配置账号为zte的用户密码超期之后允许修改密码：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name zteZXROSNG(config-system-user-username)#password-duration 1 change-password-expired密码超期之后使用账号zte再登录允许修改密码： *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 16:04:59 08-22-2019The last successful login was performed at 16:03:43 08-21-2019. Afterwards, 2 authentication failures occurred.Username:ztePassword:Your password has expired.Enter a new one now.The strong-password strategy is:  Min Length            : 8  Character Set         : number, capital, lowercase, special-character  Username-related Check: The password cannot be the same as the username.New password:The password is not strong.Please input your new password:Re-enter new password:The password has been changed successfully,Please remember your new password!ZXROSNG#域信息解释如下：Your password has expired.：提示用户密码已经超期The strong-password strategy is：提示用户密码策略New password：提示用户输入新密码The password is not strong.：密码不符合强密码策略时提示密码太简单。Re-enter new password：再次输入新密码确认
相关命令 : 
show usernamestrong-password check enablestrong-password check disablepassword
## password-recover-remind 

password-recover-remind 
命令功能 : 
该命令工作于用户名模式，用于配置用户名密码恢复相关信息。当用户忘记密码时，可以对密码进行恢复。恢复密码的前提是对应的用户账号配置了密码恢复问题及答案，恢复密码时，只要用户能够正确回答恢复密码的问题，就可以重新设置密码。
命令模式 : 
 用户名模式  
命令默认权限级别 : 
15 
命令格式 : 
password-recover-remind 
 
no password-recover-remind 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况，命令不使能。 
使用说明 : 
应用场景忘记密码无法登录系统。执行过程用户登录CLI的时候，在用户名前加recover-user触发密码恢复，正确回答恢复密码的问题，就可以重新设置密码。前提条件为对应的账号配置了密码恢复问题和答案。注意事项1.仅串口接入支持账号密码恢复功能。2.用户通过串口接入或在串口终端执行login命令，在用户名前加上recover-user和空格会触发密码恢复，recover-user和空格认为是触发密码恢复的关键字。3.非串口接入的CLI终端，不支持密码恢复功能，recover-user和空格认为是普通字符串。4.设置的新密码必须满足当前强密码要求。5.password-recover-remind命令为账号配置密码恢复功能时，密码连续认证失败次数达到设定的最大次数（与该账号登录认证连续失败次数关联），则将账号锁定设定的时间。达到最大失败次数之前，如果认证成功，则失败次数清0。可以使用user-authen-restriction fail-time ＜fail-time＞ lock-minute ＜lock-minute＞命令配置允许的用户最大认证失败次数和锁定的时间。缺省情况下，连续认证失败5次，锁定用户5分钟。6. 忘记密码，登录CLI重置账号密码时，如果输入的答案连续5次错误，则该账号5分钟内不允许使用密码恢复功能。
范例 : 
设置账号who的密码恢复问题，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#password-recover-remindThe password is:*******Enter question:what is the first character?Enter answer:*Confirm answer:*ZXROSNG(config-system-user-username)#提示名称    提示信息说明The password is    提示输入账号密码。Enter question    提示输入密码恢复的问题。Enter answer    提示输入密码恢复的答案，show running-config密码恢复答案密文显示。Confirm answer 确认输入的答案输入的密码连续错误次数达到设定的最大次数，将该账号被锁定设定的时间。ZXROSNG(config-system-user-username)#password-recover-remindThe password is:***%Error 142553: The local user is locked.ZXROSNG(config-system-user-username)#使用账号who登录，用户名who前加recover-user触发修改密码：[root@localhost ~]# telnet 192.168.122.101Trying 192.168.122.101...Connected to 192.168.122.101 (192.168.122.101)Escape character is '^]'.      *****************************************************************      Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation      *****************************************************************Login at: 05:10:13 08-09-2013Username:recover-user whoQuestion: what is the first character?Answer:(The strong-password strategy is:Min Length           : 8Character Set         : number, capital, lowercase, special-characterUsername-related Check: The password cannot be the same as the username.)Please input your new password:Re-enter new password:The password has been changed successfully,Please remember your new password!Username:whoPassword:ZXROSNG#
相关命令 : 
user-nameuser-authen-restriction
## role-based model disable 

role-based model disable 
命令功能 : 
去使能基于角色的安全模型。基于角色的安全模型非使能后，基于命令行privilege（命令行权限级别）的模型将有效。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
role-based model disable 
 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下，基于角色的安全模型是关闭的。 
使用说明 : 
基于角色的安全模型是否使能不影响角色相关的配置修改。 
范例 : 
去使能基于角色的安全模型：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role-based model disableZXROSNG(config-system-user)#
相关命令 : 
role-based model enable 
## role-based model enable 

role-based model enable 
命令功能 : 
使能基于角色的安全模型。基于角色的安全模型使能后，基于命令行privilege（命令行权限级别）的模型将失效，反之基于privilege的模型有效。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
role-based model enable 
 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下，基于角色的安全模型是关闭的。 
使用说明 : 
注意事项1. 设备默认使用基于cli级别的权限管理模式。切换到基于角色权限管理模式前必须确保已经配置了具有管理员权限的账号。否则会导致如下问题：(1)无法进入设备（没有配置账号时）；(2)可以进入设备，但权限很低；且无法获得更高权限。（已有账号权限低，且无system-user（账号管理）写权限）以上问题一旦产生，将无法恢复。2. 缺省情况下，用户授权模板不绑定任何角色。基于角色的安全模型，如果用户授权模板没有绑定任何角色，则用户仅有一些基本的操作权限。3. 角色可以根据需要创建，也可直接使用预置角色。通过show role-based priv role default命令能查看到预置角色。预置角色指系统自带的角色，不能修改、删除，只能使用。可将其关联到某用户，或者被另一角色继承。预置角色简化了用户配置，典型应用：(1)设置账号时直接使用预置角色；(2)创建新角色，继承预置角色。
范例 : 
使能基于角色的安全模型：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role-based model enableWarning: Please confirm that at least one available administrator account has been configured with 'rootadmin' in authorization-template. Otherwise, administrator privileges will be lost and cannot be restored. Continue? [yes/no]yesZXROSNG(config-system-user)#
相关命令 : 
无 
## role 

role 
命令功能 : 
授权模板绑定角色。role命令用来在授权模板下绑定角色。no role命令用来删除授权模板与角色的绑定关系。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
role 
  ＜role-name 
＞
no role 
  ＜role-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜role-name＞|角色名，长度为1~48个字符
缺省 : 
无 
使用说明 : 
应用场景角色是用于控制用户访问权限的分组，如果需要控制不同用户的访问权限时，执行此命令在用户授权模板下绑定一个已经存在的角色。注意事项角色可在设备上配置，也可由RADIUS或TACACS+服务器下发。如果选择服务器下发角色，则仍需配置此命令。一个授权模板最多可以绑定4个角色。授权模板可以绑定不存在的角色，此时相当于没有关联角色，因为组内没有定义任何权限。基于角色授权模型使能后，该功能可用。
范例 : 
配置授权模板128绑定角色group1ZXROSNG(config)#system-user ZXROSNG(config-system-user)#authorization-template 128ZXROSNG(config-system-user-author-temp)#role group1
相关命令 : 
authorization-templateshow role-based privilege user local
## role 

role 
命令功能 : 
role命令用来创建一个新的角色或进入角色模式。no role命令用来删除一个角色。
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
role 
  ＜role-name 
＞
no role 
  ＜role-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜role-name＞|角色名，长度为1~48个字符
缺省 : 
系统提供了预置角色，预置角色不是由role命令创建的，预置角色是系统自带的角色，不能修改、删除，只能使用。可将其关联到某用户，或者被另一角色继承。预置角色简化了用户配置，典型应用：(1)设置账号时直接使用预置角色；(2)创建新角色，继承预置角色。根据需要，定义了如下预置角色：rootadmin：管理员角色，具有最大权限。viewer：只读巡检员，只有查看权限。所有的show命令，以及show tech-support/show run/show this等都可以执行。operator：操作员，允许查看，执行所有show命令，允许进行所有业务配置。inspector：巡检员，有viewer角色的所有权限。另外，有ping测试权限，除此之外不允许做任何操作。zte-support：技术支持，不能配置业务，能执行所有的debug和诊断命令。能执行系统管理的动作命令，以及进行诊断和debug。
使用说明 : 
应用场景角色是用于控制不同用户访问权限的分组。如果需要控制不同用户的访问权限，则首先需要执行此命令创建角色，并通过role（授权模板模式下）命令将角色绑定到对应的授权模板。执行过程创建角色：如果该角色已经存在，则将进入角色模式；否则该命令将创建新的角色。 删除角色：如果该角色已经存在，则将删除该角色；否则提示用户该角色不存在。后续任务给角色分配权限（将任务组加入到角色任务组列表中），然后将角色绑定到授权模板下。注意事项同一个角色可以绑定到多个授权模板，同一个授权模板能绑定多个角色。该命令创建的角色不允许与系统提供的预置角色同名。
范例 : 
创建角色group1：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role group1删除角色group1：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#no role group1创建的角色与系统提供的缺省角色同名ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role rootadmin%Error 59987: The role name can not be the same as the default-role nameZXROSNG(config-system-user)#
相关命令 : 
show role-based privilege role 
## rootuser password 

rootuser password 
命令功能 : 
设置默认系统管理员账号的密码。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
rootuser password 
 
命令参数解释 : 
					无
				 
缺省 : 
无配置 
使用说明 : 
使用场景产品提供了默认用户，且该用户生效。配置影响下次登录需要输入新密码才可以认证通过。注意事项1.该命令为交互式、操作类命令，没有no命令。2.如果定制了首次登录修改密码，则首次修改密码不允许使用该命令。3.设置新密码时，需要先输入原密码，且新密码必须满足当前的强密码要求。4.show running-config显示密码配置时，显示加密密码。5. rootuser password命令修改密码时，如果输入的原密码连续认证失败3次（与该账号登录认证连续失败次数关联），则将账号锁定10分钟。达到最大失败次数之前，如果认证成功，则失败次数清0。
范例 : 
修改默认管理员账号密码：ZXROSNG(config)#system-userZXROSNG(config-system-user)#rootuser password Please enter old password: Please enter new password：
相关命令 : 
show rootuserstrong-passwordstrong-password checkstrong-password username-related-chkshow strong-password-info
## sftp top-directory 

sftp top-directory 
命令功能 : 
sftp top-directory命令用来配置本地用户的SFTP顶级目录和访问权限。no sftp top-directory命令用来取消本地用户的SFTP顶级目录配置。
命令模式 : 
 用户管理授权模板模式  
命令默认权限级别 : 
15 
命令格式 : 
sftp top-directory 
  ＜topdir-name 
＞ {read-only 
|{[read-write 
],[copy 
]}}
no sftp top-directory 
命令参数解释 : 
参数|描述
---|---
＜topdir-name＞|指定用户以SFTP方式登录设备时所访问的顶级目录名称，必须是完整路径。字符串形式，长度范围是1-159。
read-only|用于指定可访问的目录权限为只读。
read-write|用于指定可访问的目录权限为读写（包含读、创建、修改、删除、重命名，不包含拷贝）
copy|用于指定可访问的目录权限为拷贝（包含读、拷贝）。
缺省 : 
缺省情况下，本地用户的SFTP顶级目录和访问权限来自sftp-server top-directory配置。 
使用说明 : 
应用场景当需要将设备配置为SFTP服务器，从而便于本地用户以SFTP方式登录设备，对设备上的文件进行增加、删除、修改等操作时，可以通过本命令配置本地用户以SFTP方式登录设备后所处的目录。不指定该目录时，本地用户的SFTP顶级目录和访问权限来自sftp-server top-directory配置。配置影响配置本命令后，本地用户通过SFTP方式登录该设备时，将进入本命令所指定的目录。用户通过SFTP访问日志文件时，受用户的日志文件访问权限限制（可通过logfile-allowed命令设置本地用户文件访问权限）。注意事项本命令所指定的SFTP目录必须是在设备上存在且合法的，即系统可识别的，否则本地用户将无法以SFTP方式登录设备。当某个账号已通过SFTP登录，此时如果修改该账号的允许访问的顶级目录或权限，则不会对已登录的用户生效，只有用户下一次使用该账号登录时才按新配置生效。
范例 : 
范例1设置本地用户who的SFTP顶级目录为/datadisk0/，权限为只读：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#bind authorization-template 1ZXROSNG(config-system-user-username)#exitZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#sftp top-directory /datadisk0/ read-only从sftp用户who的工作目录上将文件123.txt拷贝到设备的/datadisk0/test/目录，who用户只有read-only权限，拷贝失败：ZXROSNG#copy sftp vrf mng //10.42.55.93/123.txt@who:who root: /datadisk0/test/aaa.txtStart copying file%Error 51039: The file was not found or user didn't have the privilege.ZXROSNG#
范例2设置本地用户who的SFTP顶级目录为/datadisk0/，权限为copy：ZXROSNG(config-system-user-author-temp)#sftp top-directory /datadisk0/ copy从sftp用户who的工作目录上将文件123.txt拷贝到设备的/datadisk0/test/目录：ZXROSNG#copy sftp vrf mng //10.42.55.93/123.txt@who:who root: /datadisk0/test/aaa.txtStart copying fileGot file successfully!Received 5 bytes!ZXROSNG#
设置本地用户who的告警日志文件访问权限为read-only：ZXROSNG(config-system-user-author-temp)#logfile-allowed alarm-log read-only从sftp用户who的工作目录上将告警日志文件拷贝到设备的/datadisk0/test/目录，who用户对告警日志文件只有read-only权限，拷贝失败：ZXROSNG#copy sftp vrf mng //192.168.100.250/LOG/ALARM/alarmlog_20180904201414_0.alm.log@zte:zte root: /datadisk0/test/ala.txtStart copying file%Error 51039: The file was not found or user didn't have the privilege.ZXROSNG#
设置本地用户who的告警日志文件访问权限为copy：ZXROSNG(config-system-user-author-temp)#logfile-allowed alarm-log copy从sftp用户who的工作目录上将告警日志文件拷贝到设备的/datadisk0/test/目录：ZXROSNG#copy sftp vrf mng //192.168.100.250/LOG/ALARM/alarmlog_20180904201414_0.alm.log@zte:zte root: /datadisk0/test/ala.txtStart copying fileGot file successfully!Received 15 bytes!ZXROSNG#
相关命令 : 
sftp-server top-directory
## show authen-restriction 

show authen-restriction 
命令功能 : 
该命令工作于除用户模式外的其他所有模式下，用于查询登录认证失败的用户名、认证失败次数、状态（锁定或未锁定）、剩余锁定的时间。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show authen-restriction 
 userinfo 
 
命令参数解释 : 
参数|描述
---|---
userinfo|用户信息
缺省 : 
无 
使用说明 : 
如果没有设置登陆失败一定次数后，锁定用户，则所有用户无论登录失败多少次，都不会被锁定，并且该show命令没有任何显示。 
范例 : 
设置用户登陆认证失败次数达到4次后，锁定用户3分钟，则输入以下命令：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-authen-restriction fail-time 4 lock-minute 3用户账号zte登录失败次数达到4后，被锁定3分钟，3分钟内不允许登录设备，提示“% User is locked”，以telnet方式登录设备为例：[root@localhost script]# telnet 10.42.55.6 Trying 10.42.55.6...Connected to 10.42.55.6 (10.42.55.6).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 06:19:34 01-08-2014Username:ztePassword:% User is locked查询登录认证失败用户信息：ZXROSNG#show authen-restriction userinfoUsername        Failed-time           State         Remain (minute)zte               4                    locked            2test               3                    unlocked          N/A
相关命令 : 
user-authen-restriction 
## show local-user level 

show local-user level 
命令功能 : 
用来查看本地用户的权限级别信息。
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show local-user level 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1.本地用户若没有绑定授权模板，则权限级别和default-privilege-level 配置值一致。2.本地用户绑定授权模板，授权模板内没有配置local-privilege-level，权限级别值与default-privilege-level配置值一致。3.本地用户绑定授权模板，并且配置了local-privilege-level，则权限级别显示值与本地的权限级别一致。范
范例 : 
显示当前所有本地用户的权限级别：ZXROSNG#show local-user levelUsername            Level1                   10123                 10jiangsunanjing        10jiangsunanjing68      15域信息说明：Username：本地用户名Level：权限级别相关命令
相关命令 : 
show local-user statedefault-privilege-levellocal-privilege-level
## show login failure 

show login failure 
命令功能 : 
用于查询防攻击监测功能的登录尝试失败的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show login failure 
  [{[telnet 
]|[ssh 
]|[ftp 
]}] 
命令参数解释 : 
参数|描述
---|---
telnet|查询Telnet登录失败信息
ssh|查询SSH登录失败信息。
ftp|查询FTP登录失败信息。
缺省 : 
无 
使用说明 : 
启动防攻击检测功能后：如果不指定登录方式，则显示所有登录失败信息；如果指定登录方式，则只显示指定的登录方式的登录失败信息。
范例 : 
ZXROSNG(config)#show login failure telnetUsername   Source IPAddr       LoginType  Count  TimeStampzte        10.42.55.99         TELNET     1      00:07:50 10-18-2017zte        10.42.55.99         TELNET     1      00:07:52 10-18-2017zte        10.42.55.99         TELNET     1      00:07:53 10-18-2017ZXROSNG(config)#
ZXROSNG(config)#show login failure Username   Source IPAddr       LoginType  Count  TimeStampzte        10.42.55.99         TELNET     1      00:07:50 10-18-2017zte        10.42.55.99         TELNET     1      00:07:52 10-18-2017zte        10.42.55.99         TELNET     1      00:07:53 10-18-2017who        10.42.55.99         SSH        1      00:08:11 10-18-2017who        10.42.55.99         SSH        1      00:08:13 10-18-2017who        10.42.55.99         SSH        1      00:08:15 10-18-2017ZXROSNG(config)#
相关命令 : 
login block 
## show login state 

show login state 
命令功能 : 
用于查询防攻击监测功能的状态和统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show login state 
  [{[telnet 
]|[ssh 
]|[ftp 
]}] 
命令参数解释 : 
参数|描述
---|---
telnet|查询Telnet监测状态。
ssh|查询SSH监测状态。
ftp|查询FTP监测状态。
缺省 : 
无 
使用说明 : 
无 
范例 : 
查询防攻击监测功能的统计信息：ZXROSNG#show login statetelnet:Router presently in Quiet-Mode, will remain in Quiet-Mode for 87 second(s).Denying logins from all sources except Quiet-Mode access list rule permited.ssh:Router presently in Watch-Mode, will remain in Watch-Mode for 59 second(s).Present login failure count 0.ftp:Router presently in Watch-Mode, will remain in Watch-Mode for 59 second(s).Present login failure count 0.ZXROSNG#
ZXROSNG#show login state telnettelnet:Router presently in Quiet-Mode, will remain in Quiet-Mode for 15 second(s).Denying logins from all sources except Quiet-Mode access list rule permited.ZXROSNG#
相关命令 : 
login block 
## show login 

show login 
命令功能 : 
用于查询防攻击监测功能的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show login 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于查询防攻击监测功能的配置信息 
范例 : 
ZXROSNG(config)#show  loginlogin block 200 attempts 15 within 100login quite-mode access-list trust-userlogin on-failure alarm every 30
相关命令 : 
login blocklogin quite-modelogin on-failure
## show password-dictionary 

show password-dictionary 
命令功能 : 
查看密码字典内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show password-dictionary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于显示密码字典的全部配置内容，显示的顺序为密码字典序。 
范例 : 
向密码字典中添加密码：ZXROSNG(config)#system-userZXROSNG(config-systemuser)# password-dictionary password zteZXROSNG(config-systemuser)# password-dictionary password nanjing查看密码字典：ZXROSNG# show password-dictionaryNanjingzte
相关命令 : 
password-dictionary password 
## show role-based privilege role 

show role-based privilege role 
命令功能 : 
显示角色权限信息，将本地设置的角色拥有的权限列表显示出来，供用户方便查看某角色拥有的业务权限。不指定角色名时显示所有角色权限（包括系统预置的默认角色）。也可以单独显示系统预置的默认角色及其权限。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show role-based privilege role 
  [{default 
|name 
 ＜name 
＞}] 
命令参数解释 : 
参数|描述
---|---
default|显示所有默认角色及其权限信息
＜name＞|角色名，角色名长度为1~48个字符。可以是系统默认角色名，不指定时显示所有角色权限（包括默认角色）。
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示默认角色的任务权限列表：ZXROSNG#show role-based privilege role default Role: rootadminTask(s): Have root privileges (administrator).Role: viewerDescription: Only read access.Task(s): Task-name           Privilege free-deploy         READ  diagnostic          READ  sdn                 READ显示指定角色test的权限列表：ZXROSNG#show role-based privilege role name testRole: testDescription: Task(s): Task-name         Privilege system-user       READ WRITE  telnet            READ WRITE EXECUTE  acl               READ WRITE EXECUTE DEBUG ftp               READ WRITE EXECUTE ZXROSNG#
相关命令 : 
无 
## show role-based privilege user current 

show role-based privilege user current 
命令功能 : 
用于查看基于角色授权用户登录后拥有的权限，若是远程授权的也会显示。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show role-based privilege user current 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示当前登录用户的任务权限列表：ZXROSNG#show role-based privilege user current Username: zteTask(s): Task-name                 Privilege system-user               READ WRITE  telnet                    READ WRITE EXECUTE  acl                       READ WRITE  ftp                       READ WRITE ZXROSNG# 
相关命令 : 
无 
## show role-based privilege user local 

show role-based privilege user local 
命令功能 : 
显示本地设置的权限信息，显示本地权限时若不指定用户名，则显示所有用户的权限信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show role-based privilege user local 
  [＜name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜name＞|用户名，用户名长度1~65个字符。根据本地配置信息，显示该用户拥有的权限。
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示指定用户who的本地权限列表：ZXROSNG#show role-based privilege user local whoUsername: whoRole(s): No local authorityZXROSNG#
相关命令 : 
无 
## show rootuser 

show rootuser 
命令功能 : 
用于查看缺省管理员账号的相关信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show rootuser 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用该命令用于查看缺省管理员账号的相关信息，包括：用户名、加密密码、密码修改时间。 
范例 : 
系统中不存在默认管理员账号时：ZXROSNG#show rootuser No rootuser in system!ZXROSNG#系统中存在默认管理员账号，且密码为初始密码：ZXROSNG#show rootuser Rootuser: xxxPassword: Password set-time: ZXROSNG#系统中存在默认管理员账号，且修改过密码(显示加密密码)：ZXROSNG#show rootuser Rootuser: xxxPassword: c9f8808690c11c3dc705b171f3c86eb23791f1327d2f139bad7fcb571f6acda1Password set-time: 2017-09-13ZXROSNG#
相关命令 : 
rootuser password 
## show strong-password-info 

show strong-password-info 
命令功能 : 
用于查询强密码相关的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show strong-password-info 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查询强密码相关的配置信息。如果没有配置强密码策略strong-password length，也可以通过该show命令查看缺省强密码策略。
范例 : 
例1ZXROSNG#show strong-password-infoCheck Switch            : enabledStrategy:  Min Length            : 8  Character Set         : number, capital, lowercase, special-character  Same Consecutive      : 4  Dictionary Switch     : enabled  Username-related Check: The password cannot be the same as the username.  Date Check            : enabled (Any date ranging from 1 January 1970 to 31                          December 2037 is not allowed. The date formats                          include: YYYYMMDD, MMDDYYYY, DDMMYYYY, YYYY-MM-DD, MM-DD-YYYY, DD-MM-YYYY)ZXROSNG#域信息描述：Check Switch：是否使能了强密码检查Strategy： 强密码策略信息Min Length ：强密码最小长度Character Set : number, capital, lowercase, special-character强密码中必须包含的字符类型，数字、大写字母、小写字母、特殊字符Same Consecutive ： 密码中相同字符连续出现的最大次数Dictionary Switch ：是否启用密码字典功能Username-related Check: The password cannot be the same as the username.  密码与用户名不能相同。Date Check  : enabled (Any date ranging from 1 January 1970 to 31              December 2037 is not allowed. The date formats              include: YYYYMMDD, MMDDYYYY, DDMMYYYY, YYYY-MM-DD,              MM-DD-YYYY, DD-MM-YYYY)密码中不允许包含从1970年1月1日至2037年12月31日之间的日期；日期格式包含YYYY-MM-DD、MM-DD-YYYY、DD-MM-YYYY、YYYYMMDD、MMDDYYYY、DDMMYYYY 六种。例2ZXROSNG#show strong-password-infoCheck Switch            : enabledStrategy:  Min Length            : 6  Character Set         : The password must contain at least 2 of the                          4 types of character sets.  Username-related Check: The password cannot be the username or the inverse username.ZXROSNG#域信息描述：Check Switch：是否使能了强密码检查Strategy： 强密码策略信息Min Length ：强密码最小长度Character Set : The password must contain at least 2 of the 4 types of character sets.密码中至少包含4类字符合集（数字、大写字母、小写字母、特殊字符）中的2种类型。Username-related Check: The password cannot be the username or the inverse username.密码不能与用户名相同，密码不能是用户名的反向串。例3ZXROSNG#show strong-password-infoCheck Switch            : enabledStrategy:  Min Length            : 8  Character Set         : number, capital, lowercase, special-character  Username-related Check: Substrings are not allowed.ZXROSNG#域信息描述：Check Switch：是否使能了强密码检查Strategy： 强密码策略信息Min Length ：强密码最小长度Character Set : number, capital, lowercase, special-character强密码中必须包含的字符类型，数字、大写字母、小写字母、特殊字符Username-related Check: Substrings are not allowed. 密码和用户名不能互为子串。例4ZXROSNG#show strong-password-infoCheck Switch            : enabledStrategy:  Min Length            : 8  Character Set         : number, capital, lowercase, special-character  Username-related Check: Neither substrings nor inverse substrings are allowed.ZXROSNG#域信息描述：Check Switch：是否使能了强密码检查Strategy： 强密码策略信息Min Length ：强密码最小长度Character Set : number, capital, lowercase, special-character强密码中必须包含的字符类型，数字、大写字母、小写字母、特殊字符Username-related Check: Neither substrings nor inverse substrings are allowed.密码和用户名不能互为子串和子串的逆序。
相关命令 : 
strong-passwordstrong-password checkstrong-password username-related-chk
## show user-group 

show user-group 
命令功能 : 
用于查看用户组信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show user-group 
  [special 
 ＜group-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|用于指定用户组名。字符串形式，取值范围是1-15个字符。
缺省 : 
无 
使用说明 : 
如果不带参数，则显示全部user-group信息。如果带参数special 加组名，则显示指定用户组信息。密码采用密文格式显示。
范例 : 
显示已配置的user-group信息：ZXROSNG#show user-group Groupname       Username         Encrypted-Passwordgroup1          test1            c956fde3bd75eb4e281219c72cbe9b6422                                 d7ff9ad05803b1d4ad52c04f997d93group2          test2            782ddac84667049da8dc7a071fbc4c9cf3                                 f44d7c2cdc743cff1ea40d20832fa7ZXROSNG#
显示组名为group1的配置信息：ZXROSNG#show user-group special group1Groupname       Username         Encrypted-Passwordgroup1          test1            c956fde3bd75eb4e281219c72cbe9b6422                                 d7ff9ad05803b1d4ad52c04f997d93ZXROSNG#
相关命令 : 
user-group 
## show username 

show username 
命令功能 : 
该命令工作于除用户模式外的其他模式，用于显示配置的username信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show username 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
字段描述：Username  用户名；Encrypted-Password 加密密码；AuthenNo. 帐号使用的认证模板号；AuthorNo. 账号使用的授权模板号；AgingTime 密码的剩余有效期限，单位：天，never表示永不过期，expired表示已过期；Set-Time  密码的设置时间。
范例 : 
ZXROSNG#show username Username    Encrypted-Password       AuthenNo. AuthorNo. AgingTime Set-Timewho         fce3b9cbdc6406e8dcb585ff N/A       N/A       89        02:26:23 11-01-2017            329af459e14866063fa14ed3                                           b57974c66e28fc44                                       test        95b07408152c59f797f17e87 N/A       N/A       expired   02:57:46 07-01-2017            e5c9bfb8673ce5806d2846e7                                           6e0eeb451af7b00a                                       zte         ce7c04930c52bfe1669f6c22 128       128       never     06:13:09 10-18-2017            9ef61b761ec847e5b3052bdb                                           51456385bb2a9a57                                       ZXROSNG#
相关命令 : 
user-name 
## strong-password check 

strong-password check 
命令功能 : 
本地用户强密码检查开关。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
strong-password check 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启强密码检查
disable|关闭强密码检查
缺省 : 
默认情况下，开启强密码检查。 
使用说明 : 
应用场景：为避免出现密码设置过于简单，账号被盗用等安全问题，执行此命令强迫设置较为复杂的密码达到提高安全性的目的。配置影响：开启强密码检查，如果没有配置其他任何强密码策略，后续创建本地用户或修改本地用户密码时有如下限制：1）明文密码长度不能小于8。2）必须包含小写字母、大写字母、数字和特殊字符。3）用户名与密码不能相同。注意事项：当登录用户的密码不符合当前设置的复杂度时，系统会提示用户。请根据系统提示信息进行修改。执行strong-password check disable命令后，系统不会对用户的密码复杂度进行检查，使得本地用户账户的安全性会降低，因此，建议开启密码复杂度检查功能。
范例 : 
例1：去使能本地用户强密码检查：ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-password check disableZXROSNG(config-system-user)#去使能本地用户强密码检查后，允许为用户配置简单的密码：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-name testZXROSNG(config-system-user-username)#password 123ZXROSNG(config-system-user-username)#例2：使能本地用户强密码检查，未配置强密码策略，不允许用户配置简单的密码，通过show命令查看强密码策略：ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-password check enableZXROSNG(config-system-user)#ZXROSNG(config-system-user)#user-name testZXROSNG(config-system-user-username)#password 222%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#ZXROSNG#show strong-password-infoCheck Switch        : enabledStrategy:Min Length        : 8Character Set     : number, capital, lowercase, special-characterSame Consecutive  : 0Dictionary Switch : disabledUsername-related Check: The password cannot be the same as the username.ZXROSNG#例3：使能本地用户强密码检查，按配置的强密码策略检查密码：ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-password check enableZXROSNG(config-system-user)#strong-password length 6 character number lowercaseZXROSNG(config-system-user)#user-name testZXROSNG(config-system-user-username)#password abc123ZXROSNG(config-system-user-username)#
相关命令 : 
strong-passwordpassword-dictionary password strong-password username-related-chkshow strong-password-info
## strong-password username-related-chk 

strong-password username-related-chk 
命令功能 : 
密码和用户名相关性检查开关。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
strong-password username-related-chk 
  {substring 
 [inverse 
]|inverse 
}
no strong-password username-related-chk 
命令参数解释 : 
参数|描述
---|---
substring|用户名和密码，二者中较短的作为子串，长串不能包含子串（大小写不敏感）
inverse|仅inverse参数，表示密码不能是用户名的反向串（大小写敏感）。
inverse|仅inverse参数，表示密码不能是用户名的反向串（大小写敏感）。
缺省 : 
在创建、修改密码时，缺省情况下不检查密码与用户名的相关性。如果没有配置strong-password username-related-chk，缺省要求用户名和密码不能相同。
使用说明 : 
1. 强密码策略缺省检查用户名和密码不能相同（大小写敏感），不受该命令控制。2. strong-password username-related-chk inverse 密码不能是用户名的反向串（大小写敏感）。3. strong-password username-related-chk substring 将用户名和密码中较短的作为子串，长串不能包含子串（大小写不敏感）。4. strong-password username-related-chk substring inverse 将用户名和密码中较短的作为子串，长串不能包含子串以及子串的逆序（大小写不敏感）。5. 关闭强密码检查strong-password check disable，strong-password username-related-chk配置不生效，不对密码进行用户名相关性检查。
范例 : 
ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-password username-related-chk inverse查看强密码策略信息：ZXROSNG(config-system-user)#show strong-password-info Check Switch        : enabledStrategy: Min Length        : 8 Character Set     : number, capital, lowercase, special-character Username-related check: The password cannot be the username or the inverse username.ZXROSNG(config-system-user)#配置的密码是用户名的反向串，报错：ZXROSNG(config-system-user)#user-name Ttt1111!ZXROSNG(config-system-user-username)#password !1111ttT%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#
例2：不允许密码中包含用户名（即：用户名是密码的子串）：ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-password username-related-chk substring查看强密码策略信息：ZXROSNG(config-system-user)#show strong-password-info Check Switch        : enabledStrategy: Min Length        : 8 Character Set     : number, capital, lowercase, special-character Username-related check: Substrings are not allowed.ZXROSNG(config-system-user)#配置的密码中包含用户名，报错：ZXROSNG(config-system-user)#user-name xyzZXROSNG(config-system-user-username)#password Xyz1234!%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#
例3：不允许密码中包含用户名的反向串（即：用户名反向串是密码的子串）：ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-password username-related-chk substring inverse查看强密码策略信息：ZXROSNG(config-system-user)#show strong-password-info Check Switch        : enabledStrategy: Min Length        : 8 Character Set     : number, capital, lowercase, special-character Username-related check: Neither substrings nor inverse substrings are allowed.ZXROSNG(config-system-user)#配置的密码中包含用户名反向串，报错：ZXROSNG(config-system-user)#user-name 123ZXROSNG(config-system-user-username)#password Abcd321!%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#
相关命令 : 
strong-passwordstrong-password checkshow strong-password-info
## strong-password 

strong-password 
命令功能 : 
该命令工作于用户管理模式，用于设置用户密码的强度。当用户希望密码满足某种强度要求时，设置密码之前，执行该命令。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
strong-password 
  {length 
 ＜length 
＞ [{character 
 {[number 
],[capital 
],[lowercase 
],[special-character 
]}|character-set-num 
 ＜min-num 
＞}]|same-consecutive 
 ＜same-consecutive-length 
＞|dictionary 
}
no strong-password 
  {length 
|same-consecutive 
|dictionary 
}
				
命令参数解释 : 
参数|描述
---|---
＜length＞|用于指定以明文形式输入的本地密码最小长度。整数形式，取值范围是6～64。
number|用于指定强密码中包含数字。
capital|用于指定强密码中包含大写字母。
lowercase|用于指定强密码中包含小写字母。
special-character|用于指定强密码中包含特殊字符。特殊字符不包括“?”和空格
＜min-num＞|密码中至少包含4类字符合集（数字、大写字母、小写字母、特殊字符）中的类型数。整数形式，取值范围是2～4。
＜same-consecutive-length＞|密码中相同的并且连续出现的字符长度的最大限制，范围：3~5
dictionary|密码字典功能开关
No参数|描述
---|---
length|强密码长度
same-consecutive|相同连续字符
缺省 : 
默认情况下，如果没有配置强密码策略strong-password length，默认复杂度策略为：密码长度不能小于8，必须包含小写字母、大写字母、数字和特殊字符，并且用户名与密码不能相同。可以通过show strong-password-info命令查看当前的强密码策略。默认情况下，开启强密码检查（strong-password check enable），没有strong-password same-consecutive配置，不限制密码中相同的并且连续出现的字符长度。默认情况下，开启强密码检查（strong-password check enable），没有strong-password dictionary配置，不启用密码字典功能。
使用说明 : 
1. 根据系统安全需求不同，管理员可以设置用户密码的最小长度，当管理员设置用户密码时，如果输入的密码长度小于设置的最小长度，系统将不允许设置该密码，显示出错信息，提醒用户重新输入密码。密码最大长度限制是64，如果输入的密码长度大于64，系统将不允许设置该密码，显示出错信息，提醒用户重新输入密码。2. 根据系统安全需求不同，管理员可以设置用户密码字符的组合策略。该策略可选。密码字符策略包括4种（数字、大写字母、小写字母、特殊字符），特殊字符不包括“?”和空格，管理员可以将这4种策略任意组合。当用户设定或修改密码时，系统检查设定的密码是否符合配置要求。如果不符合，系统将不允许设置，并给出错误提示。3. 根据系统安全需求不同，管理员可以设置用户密码中至少包含4类字符合集（数字、大写字母、小写字母、特殊字符）中的类型数。当用户创建或修改密码时，系统检查设定的密码是否符合配置要求。如果不符合，系统将不允许设置，并给出错误提示。该策略与密码字符组合策略是二选一的。4. 根据系统安全需求不同，管理员可以设置用户密码中相同并且连续出现的字符长度的最大限制。当用户设定或修改密码时，系统检查设定的密码是否超过该最大限制，如果超过，系统将不允许设置，并给出错误提示。5. 根据系统安全需求不同，管理员可以设置用户密码启用密码字典功能。当用户设定或修改密码时，系统检查设定的密码是否和密码字典中的密码相同，如果相同，系统将不允许设置，并给出错误提示。6. 以上strong-password命令配置的密码策略将在“用户名模式”下的password命令配置明文，以及用户登录时修改密码（首次登录修改密码、登录时进行密码恢复）时起作用。7. 关闭强密码检查（strong-password check disable），strong-password length、strong-password same-consecutive、strong-password dictionary配置不生效。
范例 : 
1）配置密码长度最小6个字符，密码中必须包含数字、大写字母和小写字母：ZXROSNG(config)#system-userZXROSNG(config-systemuser)#strong-password length 6 character number capital lowercase新配置密码不符合强密码策略时，报错：ZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#password abc123%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#
2）配置密码中相同字符连续出现的最大次数为3：ZXROSNG(config)#system-userZXROSNG(config-systemuser)#strong-password same-consecutive 3新配置的密码中相同字符连续出现的次数超限时，报错：ZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#password aaaaH123%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#
3）设置密码中至少包含2种字符类型。ZXROSNG(config-system-user)#strong-password length 6 character-set-num 2新配置的密码不符合字符类型要求，报错：ZXROSNG(config-system-user)#user-name whoZXROSNG(config-system-user-username)#password 1234567%Error 59966: The password is not strong. On a CLI terminal, run the command 'show strong-password-info' to get details.ZXROSNG(config-system-user-username)#
相关命令 : 
passwordpassword-dictionary passwordstrong-password checkstrong-password username-related-chkshow strong-password-info
## strong-username 

strong-username 
命令功能 : 
strong-username min-len 命令用于设置新建本地用户时用户名的最小长度。no strong-username min-len命令用来恢复本地用户的用户名长度为缺省值。
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
strong-username 
 min-len 
 ＜min-length 
＞
no strong-username 
 min-len 
命令参数解释 : 
参数|描述
---|---
＜min-length＞|指定本地用户的用户名最小长度。整数形式，取值范围是1~65。
No参数|描述
---|---
min-len|最小长度
缺省 : 
缺省情况下，本地用户名的最小长度为1。 
使用说明 : 
应用场景为避免出现用户名设置过于简单，导致账号被盗用等安全问题，可执行此命令限制本地用户名的最小长度，提高设备安全性。配置影响配置此命令后，新创建的本地用户需遵循这个限制，否则创建失败。配置此命令前已存在的用户不受此限制。
范例 : 
设置用户名最小长度为6：ZXROSNG(config)#system-userZXROSNG(config-system-user)#strong-username min-len 6创建用户test时，用户名不符合最小长度要求，报错：ZXROSNG(config-system-user)#user-name test%Error 59994: The username should contain at least 6 characters.ZXROSNG(config-system-user)#
相关命令 : 
user-name 
## system-user 

system-user 
命令功能 : 
用于进入用户管理模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
system-user 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
仅是模式跳转命令。 
范例 : 
进入用户管理模式：ZXROSNG#configure terminalEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#system-userZXROSNG(config-system-user)#
相关命令 : 
无 
## task aaa 

task aaa 
命令功能 : 
配置任务组关联AAA相关业务以及对应的权限，包括：认证authentication、授权authorization、记账account的AAA配置。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task aaa 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [{aaa-template 
|diameter 
|radius 
|tacacs+ 
}]
no task aaa 
  [{aaa-template 
|diameter 
|radius 
|tacacs+ 
}]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
aaa-template|指定任务名aaa-template
diameter|指定任务名diameter
radius|指定任务名radius
tacacs+|指定任务名tacacs+
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务radius加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task aaa execute read write radius
相关命令 : 
roletaskgroup
## task access-list 

task access-list 
命令功能 : 
配置任务组关联ACL相关业务以及对应的权限。access-list 包括：IPv4 ACL、IPv6 ACL、link ACL、自定义ACL列表配置，以及绑定ACL到接口、VLAN等。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task access-list 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [acl 
]
no task access-list 
  [acl 
]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
acl|指定任务名acl
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务acl加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task access-list read write execute acl
相关命令 : 
roletaskgroup
## task advanced-sys-management 

task advanced-sys-management 
命令功能 : 
配置任务组关联系统管理高级功能以及对应的权限。advanced-sys-management包括：软件包管理、集群管理、diag、LICENCE、便捷开通等。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task advanced-sys-management 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task advanced-sys-management 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|task名字，由系统统一规划。
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务sdn加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task advanced-sys-management read write execute sdn
相关命令 : 
roletaskgroup
## task basic-service 

task basic-service 
命令功能 : 
配置任务组关联基本业务以及对应的权限，基本业务配置包括：接口基本配置以及桥接、端口组等、IP层基本配置、时间段管理、VLAN基本配置等。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task basic-service 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task basic-service 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务ip加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task basic-service read write execute ip
相关命令 : 
roletaskgroup
## task bras 

task bras 
命令功能 : 
配置任务组关联BRAS相关业务以及对应的权限，任务由BRAS产品确认定义归类。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task bras 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [bras 
]
no task bras 
  [bras 
]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
bras|指定任务名bras
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务bras加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task bras read write execute
相关命令 : 
roletaskgroup
## task flow-monitoring 

task flow-monitoring 
命令功能 : 
配置任务组关联网络流量监控相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task flow-monitoring 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task flow-monitoring 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务flow-monitoring加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task flow-monitoring read write execute 
相关命令 : 
roletaskgroup
## task ip-service 

task ip-service 
命令功能 : 
配置任务组关联IP相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task ip-service 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task ip-service 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务dns加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task ip-service read write execute dns
相关命令 : 
roletaskgroup
## task lawful-interception 

task lawful-interception 
命令功能 : 
配置任务组关联合法监听（Lawful Interception）相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task lawful-interception 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task lawful-interception 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|task名字，由系统统一规划。
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务lawful-interception加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task lawful-interception read write execute  
相关命令 : 
roletaskgroup
## task multicast 

task multicast 
命令功能 : 
配置任务组关联组播（Multicast）相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task multicast 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task multicast 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。multicast是任务类名，为方便用户进行授权管理，任务类是同类业务、相关业务的集合。
范例 : 
将任务igmp加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task multicast read write execute igmp
相关命令 : 
roletaskgroup
## task pppoe-client 

task pppoe-client 
命令功能 : 
配置任务组关联 基于以太网的点对点协议 PPPoE（Point to Point Protocol over Ethernet）相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task pppoe-client 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [{pppoe-client 
|sdc 
}]
no task pppoe-client 
  [{pppoe-client 
|sdc 
}]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
pppoe-client|指定任务名PPPoE（Point to Point Protocol over Ethernet）
sdc|指定任务名sdc
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务route-manage加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task pppoe-client read write execute 
相关命令 : 
taskgrouprole
## task qos 

task qos 
命令功能 : 
配置任务组关联QoS相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task qos 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [{ds-domain 
|qos-policy 
|qppb 
}]
no task qos 
  [{ds-domain 
|qos-policy 
|qppb 
}]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
ds-domain|指定任务名ds-domain
qos-policy|指定任务名qos-policy
qppb|指定任务名qppb
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。qos是任务类名，为方便用户进行授权管理，任务类是同类业务、相关业务的集合。
范例 : 
将任务qos-policy加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task qos read write execute qos-policy
相关命令 : 
taskgrouprole
## task reliability 

task reliability 
命令功能 : 
配置任务组关联可靠性和业务保护相关配置以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task reliability 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task reliability 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。reliability是任务类名，为方便用户进行授权管理，任务类是同类业务、相关业务的集合。
范例 : 
将任务reliability加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task reliability read write debug  
相关命令 : 
taskgrouprole
## task route-manage 

task route-manage 
命令功能 : 
配置任务组关联路由管理相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task route-manage 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task route-manage 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。route-manage是任务类名，为方便用户进行授权管理，任务类是同类业务、相关业务的集合。
范例 : 
将任务route-manage加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task route-manage read write execute
相关命令 : 
roletaskgroup
## task security 

task security 
命令功能 : 
将安全相关任务中指定任务添加到当前任务组中。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task security 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task security 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。security是任务类名，为方便用户进行授权管理，任务类是同类业务、相关业务的集合。
范例 : 
将任务security-zone加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task security read write execute security-zone
相关命令 : 
roletaskgroup
## task sys-management 

task sys-management 
命令功能 : 
将系统管理中指定任务添加到当前任务组中。系统管理包括：时钟同步管理（Clock synchronization management）、系统基本维护（alarm/logging）、维护终端管理Access terminal management、性能测量等。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task sys-management 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task sys-management 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。sys-management是任务类名，为方便用户进行授权管理，任务类是同类业务、相关业务的集合。
范例 : 
将任务system-user加入到任务组test_tg中，拥有此任务组的execute、debug、read和write权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task sys-management read write execute debug system-user
相关命令 : 
roletaskgroup
## task vpn 

task vpn 
命令功能 : 
配置任务组关联VPN相关业务以及对应的权限。 
命令模式 : 
 用户任务组模式  
命令默认权限级别 : 
15 
命令格式 : 
task vpn 
  [{[read 
],[write 
],[execute 
],[debug 
]}] [＜task name 
＞]
no task vpn 
  [＜task name 
＞]
				
命令参数解释 : 
参数|描述
---|---
read|指定角色用户可以执行此任务中有读权限的命令，执行此命令不会导致配置变更。
write|指定角色用户可以执行此任务中有写权限（创建、修改、删除权限，隐含具有read权限）的命令，执行此命令会导致配置变更。
execute|指定角色用户可以执行此任务中有执行权限（如ping、telnet）的命令，执行此命令不会导致配置变更。
debug|指定角色用户可以执行此任务组中有调试（诊断）权限的命令。
＜task name＞|关联的任务名，系统统一规划
缺省 : 
无 
使用说明 : 
应用场景:为了保证安全，可以设定不同的用户拥有不同的权限。当希望为某任务组配置权限时，可以使用task命令配置任务组的权限，以便与该任务组相关联的用户能够拥有该任务所规定的权限。前置条件:任务组已创建，并且进入任务组模式。注意事项:任务名是系统定义好的，用户不能创建和删除。基于角色授权模型下，配置生效。
范例 : 
将任务vrf加入到任务组test_tg中，拥有此任务组的execute、read和write权限，无debug权限。ZXROSNG(config)#system-userZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#task vpn read write execute vrf
相关命令 : 
roletaskgroup
## taskgroup 

taskgroup 
命令功能 : 
配置角色关联的任务组。taskgroup命令用来将指定的任务组加入到当前的角色所关联的任务组列表中。no taskgroup 命令用来将指定的任务组从当前的角色所关联的任务组列表中删除。
命令模式 : 
 用户角色模式  
命令默认权限级别 : 
15 
命令格式 : 
taskgroup 
  ＜taskgroup-name 
＞
no taskgroup 
  ＜taskgroup-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜taskgroup-name＞|角色关联的任务组名，长度为1~48个字符
缺省 : 
无 
使用说明 : 
应用场景用来配置角色所关联的任务组列表，以设置该用户组拥有的权限。配置影响本命令修改当前角色的权限，所有属于当前角色的用户的权限都将受到影响。注意事项角色的权限就是它所关联的各任务组所规定权限的并集。一个角色最多关联16个任务组，需要关联多个任务组时，可以多次配置此命令。允许关联未创建的任务组。
范例 : 
将任务组tg1加入到角色admin_ug中。ZXROSNG(config)#system-user ZXROSNG(config-system-user)#role admin_ugZXROSNG(config-system-user-role-admin_ug)#taskgroup tg1
相关命令 : 
role 
## taskgroup 

taskgroup 
命令功能 : 
taskgroup命令用来创建一个新的任务组或进入任务组模式。no taskgroup 命令用来删除一个任务组。
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
taskgroup 
  ＜taskgroup-name 
＞
no taskgroup 
  ＜taskgroup-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜taskgroup-name＞|任务组名，长度为1~48个字符
缺省 : 
无 
使用说明 : 
应用场景系统缺省角色的权限不满足用户需要时，用户可以通过创建新的任务组，并且分配相应权限（任务），来达到更灵活的用户权限控制的目的。执行过程创建任务组：如果该任务组已经存在，则将进入任务组模式；否则该命令将创建新的任务组。 删除任务组：如果该任务组已经存在，则将删除该任务组；否则提示用户该任务组不存在。注意事项基于角色授权模型下，配置生效
范例 : 
创建任务组test_tg：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#taskgroup test_tgZXROSNG(config-system-user-taskgroup-test_tg)#删除任务组test_tg：ZXROSNG(config)#system-user ZXROSNG(config-system-user)#no taskgroup test_tg
相关命令 : 
roletask
## unlock local-user 

unlock local-user 
命令功能 : 
当本地用户连续认证失败一定次数被锁定以后，使用该命令手动解锁指定的本地用户。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
unlock local-user 
  ＜username 
＞
命令参数解释 : 
参数|描述
---|---
＜username＞|要解锁的本地用户名。字符串形式，不支持空格，区分大小写，长度范围是1～65个字符。
缺省 : 
无 
使用说明 : 
当本地用户因连续认证失败达到user-authen-restriction命令规定的次数而被锁定时，可以利用该命令将该用户解锁。使用本命令解锁未被锁定本地用户时不报错，解锁本地不存在的用户时报错。
范例 : 
配置全局锁定策略ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-authen-restriction fail-time 3 lock-minute 2用户zte使用telnet方式登录设备，连续认证失败3次以后被锁定2分钟，使用show authen-restriction userinfo命令查看失败信息：ZXROSNG#show authen-restriction userinfo Username         Failed-time           State         Remain (minute)zte              3                    locked            1手动解锁本地用户zteZXROSNG#unlock local-user ztezte解锁上报解锁告警通知ZXROSNG#show alarm notification code 360111A notification 360111 ID 21 level 6 occurred at 10:19:12 11-02-2019 sent by ZXR10 MPU-0/20/0%ADM-MGR% User unlocked.  The user zte is unlocked.
相关命令 : 
用户管理模式和用户名模式下的user-authen-restrictionshow authen-restriction userinfo
## unlock root-user 

unlock root-user 
命令功能 : 
当系统中缺省的root用户连续认证失败一定次数被锁定以后，使用该命令手动解锁root用户。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
unlock root-user 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
系统默认的root用户，连续认证失败次数达到锁定上限被锁定时，使用本命令手动解锁root用户。当产品没有提供默认root用户，解锁时报错，解锁未被锁定的root用户不报错。
范例 : 
手动解锁root用户。ZXROSNG#unlock root-userroot解锁上报解锁告警通知ZXROSNG#show alarm notification code 360111A notification 360111 ID 21 level 6 occurred at 10:25:12 11-02-2019 sent by ZXR10 MPU-0/20/0%ADM-MGR% User unlocked.  The user root is unlocked.
相关命令 : 
show authen-restriction userinfoshow rootuser
## user-authen-restriction 

user-authen-restriction 
命令功能 : 
该命令工作于用户管理模式，用于配置允许本地用户连续认证失败的最大次数和锁定的时间。当希望用户登录失败一定次数后，在一定时间内不允许本地用户再进行登录操作，使用该命令。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
user-authen-restriction 
 fail-time 
 ＜fail-time 
＞ lock-minute 
 ＜lock-minute 
＞
no user-authen-restriction 
命令参数解释 : 
参数|描述
---|---
＜fail-time＞|用于设置允许用户连续认证失败的最大次数。取值范围：0-16之间的整数。若指定为0，表示对认证失败次数不做限制。
＜lock-minute＞|用于设置锁定用户的时间，单位为分钟。取值范围：1-1440之间的整数。
缺省 : 
默认连续认证失败5次，锁定用户5分钟。 
使用说明 : 
应用场景：当恶意用户想要破解设备上的用户密码时，往往需要对密码进行多次尝试。为了防止恶意破解用户密码，可以使用user-authen-restriction命令配置允许的最大认证失败次数。如果本地账号达到设定的连续认证失败次数，则将用户锁定一段时间，增加了用户密码的安全性。配置影响：被锁定的用户，一定时间内不允许登录。用户被锁定或解锁，上报告警通知。该配置存在一定风险，恶意用户可以通过反复输入错误密码，使得账号被锁定，正常用户也无法登录。之前不满足锁定策略未被锁定的用户，因锁定策略变化，满足锁定策略的会被锁定。用户被锁定，主备倒换后，用户仍处于被锁定状态，锁定时间计算不受倒换影响。该命令配置生效后，不会对本地账号已经建立的在线连接产生影响。当通过用户管理模式下的user-authen-restriction命令设置了允许本地用户连续认证失败的最大次数和锁定的时间：(1)如果用户名模式下没有配置user-authen-restriction命令，则以用户管理模式下的配置为准。(2)如果用户名模式下配置了user-authen-restriction命令，则以用户名模式下的配置为准。解锁方法：用户帐号被锁定之后，可以通过以下两种方式进行解锁：自动解锁：在锁定一段时间之后，设备会自动解除该用户的认证锁定状态。手工解锁：1、特权模式下执行unlock local-user <username> 和 unlock root-user（仅解锁root用户）命令可以强制解除处于认证失败用户的锁定状态。2、删除锁定策略（用户名模式下的配置删除，用户管理模式下的配置认证失败次数0），被锁定用户解锁。
范例 : 
配置用户登陆认证失败次数达到3次后，锁定用户2分钟ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-authen-restriction fail-time 3 lock-minute 2who用户连续认证失败3次后，用户被锁2分钟：[root@localhost ~]# telnet 10.42.55.93Trying 10.42.55.93...Connected to 10.42.55.93 (10.42.55.93).Escape character is '^]'.        *****************************************************************        Welcome to ZXR10 Carrier-Class High-end Router of ZTE Corporation        *****************************************************************Login at: 07:09:36 09-20-2017Username:whoPassword:% User is lockedUsername:查看用户锁定信息：ZXROSNG#show authen-restriction userinfo Username         Failed-time           State         Remain (minute)who               3                    locked            1ZXROSNG#
用户被锁定上报告警通知ZXROSNG#show alarm notification code 360115A notification 360115 ID 37 level 6 occurred at 17:25:23 10-02-2018 sent by ZXR10 MPU-0/20/0%ADM-MGR% User locked.  The user who will be locked for 2 minutes due to 3 consecutive authentication failures.ZXROSNG#
用户解锁上报告警通知ZXROSNG#show alarm notification code 360111A notification 360111 ID 38 level 6 occurred at 17:27:49 10-02-2018 sent by ZXR10 MPU-0/20/0%ADM-MGR% User unlocked.  The user who is unlocked.ZXROSNG#
相关命令 : 
show authen-restriction userinfounlock local-user用户名模式下的user-authen-restriction 
## user-default 

user-default 
命令功能 : 
该命令工作于用户管理模式，用于进入默认用户配置模式。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
user-default 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1）仅是模式跳转命令。2）在未配置login ascii情况下，本地不存在的用户会使用user-default模式下绑定的认证、授权模板。实现本地不存在的用户通过user-default模式下的配置到远端服务器进行认证、授权。3）user-default模式下，可以配置本地不存在的服务器用户enable认证的类型。
范例 : 
进入默认用户配置模式：ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-defaultZXROSNG(config-system-user-default)#
相关命令 : 
无 
## user-group 

user-group 
命令功能 : 
该命令工作于用户管理模式，用配置PPP用户组信息。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
user-group 
 special 
 ＜group-name 
＞ ＜user-name 
＞ [{encrypted 
 ＜encrypt-pwd 
＞|＜password 
＞}]
no user-group 
 special 
 ＜group-name 
＞ [＜user-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|组名，长度为1~15个字符
＜user-name＞|用户名，长度为1~16个字符
＜encrypt-pwd＞|用于指定密文密码。字符串形式，区分大小写，长度范围是64~67。
＜password＞|用于指定明文密码。字符串形式，区分大小写，长度范围是3~32。
缺省 : 
无 
使用说明 : 
1）组名不可以是 default，default不区分大小写。2）可配置的最大用户组为200，每个组内最大用户数为12。用户组最大实例数512（即：组数*组内用户数<=512）。3）使用no命令时，如果不带<user-name>参数，则删除指定的整组信息；如果带<user-name>参数信息，则删除指定的用户组，用户名信息。4）目前密文密码长度，只支持64、67。5）user-group  special ＜group-name＞ ＜user-name＞命令不带密码参数时，密码以交互式输入，输入字符显示为*。输入的密码为字符串形式，区分大小写，取值范围是3～32。
范例 : 
1）创建一个用户组zte_group，组内用户名为hello1，非交互式输入密码为Hello_2019ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-group special zte_group hello Hello_20192）创建一个用户组zte_group1，组内用户名为hello1，非交互式输入密文密码ZXROSNG(config)#system-userZXROSNG(config-system-user)# user-group special zte_group1 hello1 encrypted ce7c04930c52bfe1669f6c229ef61b761ec847e5b3052bdb51456385bb2a9a573）为用户组zte_group添加用户名为hello2，交互式输入密码为Hello_2019ZXROSNG(config)#system-userZXROSNG(config-system-user)#user-group special zte_group hello2Please configure the password(3-32)Enter password: **********Confirm password: **********ZXROSNG(config-system-user)#
相关命令 : 
show user-group
## user-name 

user-name 
命令功能 : 
该命令工作于用户管理模式，用来创建一个本地用户，并进入该用户配置模式。 
命令模式 : 
 用户管理模式  
命令默认权限级别 : 
15 
命令格式 : 
user-name 
  ＜username 
＞
no user-name 
  ＜username 
＞
				
命令参数解释 : 
参数|描述
---|---
＜username＞|字符串形式，不支持空格，区分大小写，长度范围是1～65。
缺省 : 
缺省情况下，系统没有本地用户。 
使用说明 : 
应用场景:以如下几种方式访问设备时，需要创建本地用户并配置该用户的登录口令。1)FTP方式2)通过用户账号+登录口令进行本地认证的SSH方式（STelnet，SNETCONF，SFTP）3)通过用户账号+登录口令进行本地认证的Telnet方式4)通过用户账号+登录口令进行本地认证的WEB方式创建本地用户并配置该用户的登录口令后，当以该用户名登录设备时，需要输入正确的登录口令才能够顺利登录。如果指定的用户名不存在，执行此命令后将新建一个本地用户；如果指定的用户名已经存在，执行此命令后将进入用户名模式。配置影响:如果配置了strong-username mim-length命令，则本地用户名长度同时受该命令的影响。配置完成后，通过show username命令查看本地用户属性时，用户口令将以密文形式显示。注意事项:创建一个本地用户后，还需按照如下原则设置本地用户相关的其他配置：1)通过password命令配置用户登录口令；2)创建用户管理的认证模板，绑定已存在的AAA认证模板（AAA认证模板下配置认证方法）；3)创建用户管理的授权模板，绑定已存在的AAA授权模板（AAA认授权板下配置授权方法）；4)通过bind authentication-template命令绑定用户管理的认证模板；5)通过bind authorization-template命令绑定用户管理的授权模板，并配置本地权限级别local-privilege-level；本地用户的属性变更不会对当前在线用户产生影响，已在线用户重新登录之后此配置变更生效。
范例 : 
创建一个可用的系统用户test，密码为test，需执行以下命令：1）创建AAA认证授权模板2001，配置认证授权类型为localZXROSNG(config)#aaa-authentication-template 2001ZXROSNG(config-aaa-authen-template)#aaa-authentication-type localZXROSNG(config-aaa-authen-template)#exitZXROSNG(config)#aaa-authorization-template 2001ZXROSNG(config-aaa-author-template)#aaa-authorization-type local2）创建认证授权模板1，绑定AAA认证授权模板2001ZXROSNG(config)#system-user ZXROSNG(config-system-user)#authentication-template 1ZXROSNG(config-system-user-authen-temp)#bind aaa-authentication-template 2001ZXROSNG(config-system-user-authen-temp)#exitZXROSNG(config-system-user)#authorization-template 1ZXROSNG(config-system-user-author-temp)#bind aaa-authorization-template 2001ZXROSNG(config-system-user-author-temp)#local-privilege-level 153）创建用户test，绑定认证授权模板1ZXROSNG(config-system-user)#user-name testZXROSNG(config-system-user-username)#password testZXROSNG(config-system-user-username)#bind authentication-template 1ZXROSNG(config-system-user-username)#bind authorization-template 1
相关命令 : 
show username 
