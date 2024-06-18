

用于区分网络号的流量统计，需要执行[ADD PLMNCTRLCFG](../../MMESGSN\zh-CN\mml\1262255.html)命令增加基于PLMN的控制配置。根据客户需求，一般无需创建。建议颗粒为15分钟。


# C405650003 基于PLMN的用户上行数据字节数(Byte)-GSM 
## 计数器描述 
仅统计发送的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 
统计的字节数包括：GTP首部之后（不包括GTP首部）的用户报文字节数。 
## 测量触发点 
USUP-2G模块在Gn/Gp口发送GTP数据报文成功后统计。 
## 采集方式 
CC 
# C405650004 基于PLMN的用户上行数据字节数(Byte)-UMTS 
## 计数器描述 
仅统计发送的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 
统计的字节数包括：GTP首部之后（不包括GTP首部）的用户报文字节数。 
## 测量触发点 
USUP-3G模块在Gn/Gp口发送GTP数据报文成功后统计。 
## 采集方式 
CC 
# C405650005 基于PLMN的用户下行数据字节数(Byte)-GSM 
## 计数器描述 
仅统计接收到的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 
统计的字节数包括：GTP首部之后（不包括GTP首部）的用户报文字节数。 
## 测量触发点 
USUP-2G模块收到下行GTP数据报文，在依次完成隧道IP重组、IP/UDP/GTP解封装，定位到PDP上下文之后统计。 
## 采集方式 
CC 
# C405650006 基于PLMN的用户下行数据字节数(Byte)-UMTS 
## 计数器描述 
仅统计接收到的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 
统计的字节数包括：GTP首部之后（不包括GTP首部）的用户报文字节数。 
## 测量触发点 
USUP-3G模块收到下行GTP数据报文，在依次完成隧道IP重组、IP/UDP/GTP解封装，定位到PDP上下文之后统计。 
## 采集方式 
CC 
# C405650007 基于PLMN的用户上行数据包数-GSM 


## 计数器描述 

 
仅统计发送的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 

 
在USUP-2G模块统计，统计在隧道IP分片之前的GTP报文个数。 

 


## 测量触发点 
USUP-2G模块在Gn/Gp口发送GTP数据报文成功后统计。 


## 采集方式 
CC 


# C405650008 基于PLMN的用户上行数据包数-UMTS 


## 计数器描述 

 
仅统计发送的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 

 
在USUP-3G模块统计，统计在隧道IP分片之前的GTP报文个数。 

 


## 测量触发点 
USUP-3G模块在Gn/Gp口发送GTP数据报文成功后统计。 


## 采集方式 
CC 


# C405650009 基于PLMN的用户下行数据包数-GSM 


## 计数器描述 

 
仅统计接收到的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 

 
在USUP-2G模块统计，统计在隧道IP分片之前的GTP报文个数。 

 


## 测量触发点 
USUP-2G模块收到下行GTP数据报文，在依次完成隧道IP重组、IP/UDP/GTP解封装，定位到PDP上下文之后统计。 


## 采集方式 
CC 


# C405650010 基于PLMN的用户下行数据包数-UMTS 


## 计数器描述 

 
仅统计接收到的GTP数据报文，即GTP首部的Message Type为0xFF的报文。 

 
在USUP-3G模块统计，统计在隧道IP分片之前的GTP报文个数。 

 


## 测量触发点 
USUP-3G模块收到下行GTP数据报文，在依次完成隧道IP重组、IP/UDP/GTP解封装，定位到PDP上下文之后统计。 


## 采集方式 
CC 


