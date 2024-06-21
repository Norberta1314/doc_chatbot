#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/12
# @Author  : lyytaw
import os.path

from bs4 import BeautifulSoup, Tag, NavigableString


class Content:
    def __init__(self, path, title):
        self.content = ""
        self.path = ""
        self.title = ""

    def add_content(self, new_content):
        self.content += new_content


class ParseTable:

    def parse_table(self, soup):
        rows = soup.find_all("tr")
        for r_index, row in enumerate(rows):
            cells = row.find_all("td")
            for c_index, cell in enumerate(cells):
                rowspan = int(cell.get('rowspan', '1'))
                colspan = int(cell.get('colspan', '1'))

                cell_value = cell.text
                self._fill_merged_cells(cell_value, rowspan, colspan, rows, r_index, c_index)
        output = ''
        for r_index, row in enumerate(rows):
            row_text = []
            cells = row.find_all('th')
            if cells:
                for cell in cells:
                    row_text.append(cell.text.replace(os.linesep, '').strip())
                output += '|'.join(row_text) + os.linesep

                for k in range(len(cells)):
                    row_text[k] = '---'
                output += '|'.join(row_text) + os.linesep
            cells = row.find_all('td')
            if cells:
                for c_index, cell in enumerate(cells):
                    cell_value = cell.text.replace(os.linesep, '').strip()
                    row_text.append(cell_value)
                output += '|'.join(row_text) + os.linesep
        return output

    def _fill_merged_cells(self, cell_value, rowspan, colspan, rows, r_index, c_index):
        if rowspan > 1:
            for k in range(r_index + 1, r_index + rowspan):
                for t in range(c_index, c_index + colspan):
                    rows[k].insert(t + 1, BeautifulSoup(f"<td>{cell_value}</td>", "html.parser"))
        if colspan > 1:
            for k in range(c_index + 1, c_index + colspan):
                rows[r_index].insert(k + 1, BeautifulSoup(f"<td>{cell_value}</td>", "html.parser"))


tt_map = {}


def parse_title(title, level):
    if tt_map.get(title) is None:
        tt_map[title] = 0
    tt_map[title] = tt_map[title] + 1
    if not title:
        return ""
    if title == "相关主题":
        return ""
    if title == "子主题":
        return ""
    if title in ['命令功能', '相关命令', '命令模式', '命令默认权限级别', '命令格式', '命令参数解释', '缺省', '使用说明', '范例', '计数器描述', '测量触发点', '采集方式',
                 '注意事项', '命令举例', '输入参数说明', '输出参数说明', '处理建议', '告警描述', '系统影响', '可能原因', '告警属性', '应用场景', '告警参数', '相关主题',
                 '背景知识', '摘要', '步骤', '功能描述', '指标说明', '计算公式', '相关计数器', '功能说明', '影响说明', '默认取值', '其他相关配置', '参数说明',
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
                 '在脚本设计器中使用参数', '告警原因', '默认门限', '参数的设置', '告警信息', '基本信息', '上报子系统', '资源实施接口信息', '配额项', '公式', '结果',
                 '页面路由信息',
                 '单位', 'DPU', 'DCU', '涉及网元', 'MU', 'CHR', '特性间交互', 'EMS', 'MDS', '失败观察', '特性操作', '检查步骤', 'ZTE', '处理步骤',
                 'MAN', '检查标准', '告警与通知', '检查目的', '定时器', 'GGSN', '计数器介绍', '配置原则', 'FQDN', '涉及的NF/网元', 'GTP', 'NAS',
                 'SGSN',
                 'EIR', 'PDP', 'NSSF', 'IMEI', 'TAU', 'RAN', '配置命令', 'EPS', '消息描述', 'RNC', 'TA', 'LTE', 'MSC', 'RAT',
                 '功能特性简介', '常见问题处理', '适用网元', 'GPRS', 'DNS', 'HLR', '收益', 'EPC', '场景三', 'PLMN', '调整特性', 'AMF实现', 'NF实现',
                 'HSS', 'eNodeB', '说明', '序号', '动态管理', 'UTRAN', 'SMS', 'TCP', 'GUTI', '场景二', 'MME', 'E-UTRAN', '调测信息采集',
                 '工程规划要求', '本NF/网元实现', '场景一', 'PDN', 'AUSF', 'SGW']:
        return f"{title} :"
    if level > 8:
        return f"{title} {os.linesep}"
    return f"{(level + 1) * '#'} {title.strip()} {os.linesep}"


def digui_parse(element, level, content: Content):
    for child_ele in element.contents:
        if isinstance(child_ele, NavigableString):
            if child_ele:
                content.add_content(child_ele)
                if child_ele == element.contents[-1]:
                    content.add_content(os.linesep)
            continue
        if child_ele.name == "table":
            content.add_content(ParseTable().parse_table(child_ele))
            continue
        elif child_ele.name == "pre":
            content.add_content(f"`{child_ele.text.replace('#', '')}` {os.linesep}")
            continue
        elif child_ele.name == "img":
            if not child_ele.get('src'):
                continue
            # content.add_content((f"[{child_ele.get('alt', '')}]{os.path.join(content.path, child_ele.get('src'))})"))
            if child_ele.get('alt', '') != "":
                content.add_content(f"[{child_ele.get('alt', '')}]")
            if child_ele == element.contents[-1]:
                content.add_content(os.linesep)
            continue
        elif child_ele.name == "nav":
            if child_ele.text == "":
                continue
            if child_ele.text.startswith('本节包含以下内容'):
                continue

            continue
        elif child_ele.name in ["ul"]:
            is_child = False
            for pre_element in child_ele.previous_elements:
                # TODO 这里需要一个中文冒号
                if pre_element == "子主题：":
                    is_child = True
            if not is_child:
                for c_child in child_ele.contents:
                    content.add_content(f"{c_child.text} {os.linesep}")
            continue

        if len(list(child_ele.descendants)) != 1:
            digui_parse(child_ele, level + 1, content)
            continue
        child_ele_name = child_ele.name
        if "title" in child_ele.get("class", []):
            content.add_content(parse_title(child_ele.text, level))
        elif child_ele_name in ["div", "p", "figure", "ol", "samp", "ul"]:
            content.add_content(f"{child_ele.text} {os.linesep}")
        elif child_ele_name in ["span", "sub", "sup", "var", "kbd", "strong", "cite", "abbr"]:
            content.add_content(f"{child_ele.text}")
            if child_ele == element.contents[-1]:
                content.add_content(os.linesep)
        elif child_ele.name == "br":
            content.add_content(os.linesep)
        elif child_ele.name == "a":
            if child_ele.text.strip() != "":
                content.add_content(f"[{child_ele.text}]")
            if child_ele == element.contents[-1]:
                content.add_content(os.linesep)
        else:
            content.add_content(f"{child_ele.text} {os.linesep}")


def html_to_markdown(html, level, path, title_times_map):
    soup = BeautifulSoup(html, "html.parser")
    root_contents = soup.body.contents

    title = ""
    body = ""

    for element in root_contents:
        if not isinstance(element, Tag):
            continue
        elif element.text.strip() == "":
            continue

        if element.name == "script":
            continue
        elif element.name == "article":
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content
            continue
        elif element.name == "a" and element.text == "":
            continue
        elif element.name == "h1":
            body += parse_title(element.text, level)
            continue

        dtd_path = element.attrs.get('data-dtd-path')
        element_class_list = element.get("class", "")
        if dtd_path in ["ztetopic/title"]:
            title = element.text
            # body += parse_title(element.text, level)
        elif dtd_path in ["zteconcept/title"]:
            body += parse_title(element.text, level)
        elif dtd_path in ["ztetopic/shortdesc", "ztetopic/abstract", " zteconcept/title", "ztereference/title",
                          "ztetopic/titlealts"]:
            body += f"{element.text.strip()} {os.linesep}"
        elif dtd_path in ["ztetopic/body", "zteconcept/conbody",
                          "zterefenrence/refbody", "ztetopic/section"] or "body" in element_class_list:
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content
        elif "section" in element_class_list:
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content
        elif dtd_path in ["ztetopic/related-links", "zteconcept/related-links"]:
            # print("link")
            # body += parse_link(element, level, path)
            continue
        elif "related-links" in element_class_list or element.text.strip().startswith("子主题"):
            if element.text.startswith("父主题"):
                continue
        elif element.text.strip().startswith("背景知识") or element.text.strip().startswith("功能说明") or element.attrs.get(
                "id") == "docDetail":
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content
        else:
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content
    title_times_map.update(tt_map)
    return body
