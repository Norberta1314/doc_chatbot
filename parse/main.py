#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/11
# @Author  : lyytaw
import os.path
import xml.etree.ElementTree as ET

import chardet

from parse.html2md import html_to_markdown, parse_title

doc_name = "director"
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
                result += html_to_markdown(html, cur_level, os.path.dirname(doc_path))

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
                result += html_to_markdown(html, cur_level, os.path.dirname(log_path))

    if level_list in markdown_split_map:
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
        with open(get_write_path(level_list), "w", encoding='utf-8') as f:
            f.write(result)


if __name__ == '__main__':
    parse()
