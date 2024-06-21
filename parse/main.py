#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/11
# @Author  : lyytaw
import os.path
import xml.etree.ElementTree as ET

import chardet

from parse.html2md import html_to_markdown, parse_title

# doc_name = "director"
# doc_name = "rcp"
doc_name = "emsplus"
# doc_name = "umac"

title_times_map = {}
current_set = ['命令功能', '相关命令', '命令模式', '命令默认权限级别', '命令格式', '命令参数解释', '缺省', '使用说明', '范例', '计数器描述', '测量触发点', '采集方式',
               '注意事项', '命令举例', '输入参数说明', '输出参数说明', '处理建议', '告警描述', '系统影响', '可能原因', '告警属性', '应用场景', '告警参数', '相关主题',
               '背景知识', '摘要', '步骤', '功能描述', '指标说明', '计算公式', '相关计数器', '功能说明', '影响说明', '默认取值', '其他相关配置', '参数说明', '缩略语',
               '消息功能', '相关信元', '告警类型', '告警样例', '告警类别', '告警恢复', '引起原因', '产生的影响', '默认级别', '告警描述原型', '数据规划', '配置步骤',
               '场景说明', '概述', '信令流程', '业务模型', '保护对象', '流控原理', '防御策略', '配置方法', '配置前提', '特性描述', '特性配置', '实现原理', '配置过程',
               '配置说明', '流程说明', '描述', '应用限制', '系统架构', '客户收益', '前提', '业务流程', '测试用例', '配置脚本', '相关任务', '配置实例', 'PCF',
               'SMF', '可获得性', '遵循标准', '术语', 'ip mtu', '性能统计', '本网元实现', 'License要求', '举例', 'interface', 'description',
               'NF', '特性能力', 'O&M相关', 'EM', '版本要求及变更记录', '对其他网元的要求', '特性交互', 'AMF', '告警和通知', '协议栈', '命令', '故障现象',
               'RCP', '定义', 'ipv6 mtu', '话单与计费', 'mpls mtu', 'neighbor &amp;lt;mid&amp;gt; activate', '相关信息', '操作步骤',
               'mtu', 'neighbor &amp;lt;mid&amp;gt; route-reflector-client', 'AF', 'QoS', '业务配置关系图', '业务观察/失败观察',
               '故障处理', '场景描述', 'SPR', '全称', '解释', '故障分析', '故障处理结果确认', 'UE', 'UPF', 'HTTP', '涉及的网元', 'PCC', 'shutdown',
               'neighbor &amp;lt;mid&amp;gt; route-map', 'PDU', 'PCRF', 'IP',
               'neighbor &amp;lt;mid&amp;gt; split-update-group', 'NRF', 'IMSI', 'VNF', 'SC', '配置场景',
               'neighbor &amp;lt;mid&amp;gt; weight', 'DNN', 'UDR', 'byname',
               'neighbor &amp;lt;mid&amp;gt; activate disable', 'CHF', 'BSF', 'PCEF', '特性定义', 'ip address',
               'neighbor &amp;lt;mid&amp;gt; send-community', 'neighbor &amp;lt;mid&amp;gt; send-large-community',
               'NFVO', 'VNFM', 'neighbor &amp;lt;mid&amp;gt; as-path-loopcheck', '5GC', 'GPSI', 'IMS', 'SUPI', 'APN',
               'FTP', 'SFTP', 'VM', 'OAM', '维护目的', '维护指导', '参考标准', '异常处理', '系统调测', '调测信息收集', 'ip vrf forwarding',
               'neighbor &amp;lt;mid&amp;gt; allowas-in', 'neighbor &amp;lt;mid&amp;gt; next-hop-self',
               'neighbor &amp;lt;mid&amp;gt; send-med', 'SM', 'URI', 'NFV', 'VIM', 'SCTP', 'UDSF', '配置特性',
               'neighbor &amp;lt;mid&amp;gt; maximum-prefix', 'neighbor &amp;lt;mid&amp;gt; next-hop-unchanged',
               'neighbor &amp;lt;mid&amp;gt; remove-private-as', 'neighbor &amp;lt;mid&amp;gt; route-policy in',
               'neighbor &amp;lt;mid&amp;gt; route-policy out', 'qos-policy', 'VoNR', 'IPv6', 'UDM', 'PGW', '3GPP',
               'MANO', '指标监控', 'OMU', '业务配置关系', '配置举例', '注意', '界面说明', '操作维护', '专业维护', 'track',
               'neighbor &amp;lt;mid&amp;gt; maxas-in', 'network', '业务场景', 'AAA', 'IPv4', 'P-CSCF', 'S-NSSAI',
               'MSISDN', 'NEF', 'GSU', 'ETSI', 'NFS', '各网元作用', 'ipv6 address', 'redistribute',
               '在脚本设计器中使用参数', '告警原因', '默认门限', '参数的设置', '告警信息', '基本信息', '上报子系统', '资源实施接口信息', '配额项', '公式', '结果', '页面路由信息',
               '单位', 'DPU', 'DCU', '涉及网元', 'MU', 'CHR', '特性间交互', 'EMS', 'MDS', '失败观察', '特性操作', '检查步骤', 'ZTE', '处理步骤',
               'MAN', '检查标准', '告警与通知', '检查目的', '定时器', 'GGSN', '计数器介绍', '配置原则', 'FQDN', '涉及的NF/网元', 'GTP', 'NAS', 'SGSN',
               'EIR', 'PDP', 'NSSF', 'IMEI', 'TAU', 'RAN', '配置命令', 'EPS', '消息描述', 'RNC', 'TA', 'LTE', 'MSC', 'RAT',
               '功能特性简介', '常见问题处理', '适用网元', 'GPRS', 'DNS', 'HLR', '收益', 'EPC', '场景三', 'PLMN', '调整特性', 'AMF实现', 'NF实现',
               'HSS', 'eNodeB', '说明', '序号', '动态管理', 'UTRAN', 'SMS', 'TCP', 'GUTI', '场景二', 'MME', 'E-UTRAN', '调测信息采集',
               '工程规划要求', '本NF/网元实现', '场景一', 'PDN', 'AUSF', 'SGW']

director_split = [
    ["rcp", "技术入门", "5GC信令图解"],
    ["rcp", "技术入门", "5GC综合解决方案"],
    ["rcp", "参考", "性能指标参考"],
    ["rcp", "参考", "性能计数器参考（业务）"],
    ["rcp", "参考", "性能计数器参考（平台）"],
    ["rcp", "参考", "软件参数"],
    ["rcp", "参考", "命令参考"],
    ["rcp", "参考", "命令参考", "CommonS_OAM"],
    ["rcp", "参考", "命令参考", "CommonS_HTTP_LB"],
    ["rcp", "参考", "命令参考", "CommonS_HTTP_LB", "服务化接口配置管理"],
    ["rcp", "参考", "命令参考", "CommonS_HTTP_LB", "服务化接口配置管理", "局向检测相关配置"],
    ["rcp", "参考", "命令参考", "CommonS_HTTP_LB", "服务化接口配置管理", "本地NRF配置"],
    ["rcp", "参考", "命令参考", "CommonS_IPS"],
    ["rcp", "参考", "命令参考", "CommonS_SIG"],
    ["rcp", "参考", "命令参考", "CommonS_TMSP"],
    ["rcp", "参考", "命令参考", "Ncudr_Access"],
    ["rcp", "参考", "命令参考", "Ncudr_AccessManagement"],
    ["rcp", "参考", "命令参考", "Ncudr_SystemManagement"],
    ["rcp", "参考", "命令参考", "Npcf_LOG"],
    ["rcp", "参考", "命令参考", "Npcf_LogStoreUnit"],
    ["rcp", "参考", "命令参考", "Npcf_SIGLB"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "号码分析配置"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "DIAMETER协议配置"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "签约数据配置"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "承载业务配置"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "拓扑数据配置"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "服务管理配置"],
    ["rcp", "参考", "命令参考", "Npcf_PolicyManagement", "配置管理", "网元全局配置"],
    ["rcp", "参考", "命令参考", "Npcf_SMPolicyControl"],
    ["rcp", "参考", "命令参考", "Npcf_SystemManagement"],
    ["rcp", "参考", "命令参考", "Rosng"],
    ["rcp", "参考", "命令参考", "Rosng", "系统管理"],
    ["rcp", "参考", "命令参考", "Rosng", "接口配置"],
    ["rcp", "参考", "命令参考", "Rosng", "IPv4业务"],
    ["rcp", "参考", "命令参考", "Rosng", "IPv4组播"],
    ["rcp", "参考", "命令参考", "Rosng", "IP路由"],
    ["rcp", "参考", "命令参考", "Rosng", "IP路由", "BGP配置命令"],
    ["rcp", "参考", "命令参考", "Rosng", "IPv6"],
    ["rcp", "参考", "命令参考", "Rosng", "MPLS"],
    ["rcp", "参考", "命令参考", "Rosng", "VPN"],
    ["rcp", "参考", "命令参考", "Rosng", "QoS"],
    ["rcp", "参考", "命令参考", "Rosng", "安全"],
    ["rcp", "参考", "命令参考", "Rosng", "可靠性"],
    ["rcp", "参考", "命令参考", "Rosng", "策略模板"],
    ["rcp", "参考", "命令参考", "Rosng", "BRAS"],
    ["rcp", "参考", "命令参考", "Rosng", "CGN"],
    ["rcp", "参考", "高危命令"],
    ["umac", "技术入门", "5G核心网综合解决方案"],
    ["umac", "特性指导", "Common特性"],
    ["umac", "特性指导", "MME特性"],
    ["umac", "特性指导", "MME特性", "ZUF-78-04 安全管理"],
    ["umac", "特性指导", "MME特性", "ZUF-78-12 语音和短消息"],
    ["umac", "特性指导", "MME特性", "ZUF-78-17 物联网功能"],
    ["umac", "特性指导", "SGSN特性"],
    ["umac", "特性指导", "AMF特性"],
    ["umac", "安装与调试", "License安装"],
    ["umac", "参考", "命令参考"],
    ["umac", "参考", "命令参考", "AMF"],
    ["umac", "参考", "命令参考", "AMF", "Namf_MP"],
    ["umac", "参考", "命令参考", "AMF", "Namf_Communication"],
    ["umac", "参考", "命令参考", "AMF", "Namf_Communication", "NF发现和选择配置"],
    ["umac", "参考", "命令参考", "AMF", "Namf_Communication", "移动性配置"],
    ["umac", "参考", "命令参考", "AMF", "Namf_Communication", "增强功能"],
    ["umac", "参考", "命令参考", "AMF", "Namf_Communication", "拥塞与过负荷控制"],
    ["umac", "参考", "命令参考", "AMF", "Namf_Communication", "动态管理"],
    ["umac", "参考", "命令参考", "Common"],
    ["umac", "参考", "命令参考", "Common", "CommonS_HTTP_LB"],
    ["umac", "参考", "命令参考", "Common", "CommonS_HTTP_LB", "服务化接口配置管理"],
    ["umac", "参考", "命令参考", "Common", "Commons_IPS"],
    ["umac", "参考", "命令参考", "Common", "Commons_SIG"],
    ["umac", "参考", "命令参考", "Common", "Commons_TMSP"],
    ["umac", "参考", "命令参考", "MMESGSN"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "系统配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "系统配置", "交换局配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "系统配置", "Qos配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "系统配置", "接入区域配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "系统配置", "MME对等PLMN配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "业务配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "业务配置", "APN配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "业务配置", "计费配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "业务配置", "SMS配置"],
    ["umac", "参考", "命令参考", "MMESGSN", "配置管理", "业务配置", "LCS配置"],
    ["umac", "参考", "ROSNG告警处理"],
    ["umac", "参考", "业务告警处理"],
    ["umac", "参考", "性能指标参考"],
    ["umac", "参考", "性能计数器参考（AMF）"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN会话测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN APN会话测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN路由区附着测量（UMTS）"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN路由区更新测量（UMTS）"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN路由区会话测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN NSE失败细化测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN 路由更新测量（GSM）"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN路由区更新分网元测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN区内区外GTP测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN RNC失败细化测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "附着流程测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN附着网络侧失败测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "License测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN用户测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN寻呼测量"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN FR承载方式下NS测量（GPRS"],
    ["umac", "参考", "性能计数器参考（SGSN&MME）", "SGSN PLMN流量测量"],
    ["umac", "参考", "软件参数（AMF）"],
    ["umac", "参考", "软件参数（SGSNMME）"],
    ["umac", "参考", "高危命令"],

]

markdown_split_map = director_split


def get_parent_path(path):
    return os.path.join(f"/Users/lyy/apos/aiops2024-challenge-dataset/{doc_name}", path.replace("\\", "/"))


def get_write_path(level_list):
    if level_list:
        copy_level_list = level_list[1:]

        return os.path.join("/Users/lyy/apos/parse/doc", doc_name, "-".join(copy_level_list) + ".md")
    else:
        return os.path.join("/Users/lyy/apos/parse/doc", doc_name)


def digui_director(node, level, level_list):
    result = ""
    cur_level = level
    if level_list in markdown_split_map:
        cur_level = -1
    else:
        result = parse_title(node.attrib['name'], level)
    if not node.attrib['url'].startswith('nodes/'):
        doc_path = get_parent_path(f"documents/{node.attrib['url']}")
        if os.path.exists(doc_path):
            file_encode = ""
            with open(doc_path, "rb") as f:
                file_encode = chardet.detect(f.read())
            with open(doc_path, encoding=file_encode["encoding"]) as f:
                html = f.read()
                result += html_to_markdown(html, cur_level, os.path.dirname(doc_path), title_times_map)

    for cc in node:
        c_result = digui_director(cc, cur_level + 1, level_list + [cc.attrib['name']])
        result += c_result

    if node.attrib['url'].startswith("nodes"):
        log_path = node.attrib['url'][6:-5]
        log_path = get_parent_path(f"documents/{log_path}/log.html")
        if os.path.exists(log_path):
            with open(log_path, encoding="utf-8") as f:
                html = f.read()
                result += parse_title("缩略语", cur_level)
                result += html_to_markdown(html, cur_level, os.path.dirname(log_path), title_times_map)

    if level_list in markdown_split_map:
        if result != "":
            with open(get_write_path(level_list), "w", encoding='utf-8') as f:
                f.write(result)
        return ""
    else:
        return result


def parse():
    tree = ET.parse(get_parent_path("nodetree.xml"))
    root = tree.getroot()
    md_parent_path = get_write_path([])
    if not os.path.exists(md_parent_path):
        os.mkdir(md_parent_path)
    for child in root:
        # if child.attrib['name'] != '参考':
        #     continue
        level_list = [doc_name, child.attrib['name']]
        result = digui_director(child, 0, level_list)
        print(level_list)
        if result != "":
            with open(get_write_path(level_list), "w", encoding='utf-8') as f:
                f.write(result)

    ss_map = dict(sorted(title_times_map.items(), key=lambda x: x[1], reverse=True))
    new_dict = [key for key, value in ss_map.items() if value > 10]
    # "','".join(list(set(new_dict) - set(current_set)))
    print("end")


if __name__ == '__main__':
    parse()
