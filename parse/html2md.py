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


def parse_title(title, level):
    if not title:
        return ""
    if title == "相关主题":
        return ""

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
            content.add_content((f"[{child_ele.get('alt', '')}]{os.path.join(content.path, child_ele.get('src'))})"))
            if child_ele == element.contents[-1]:
                content.add_content(os.linesep)
            continue
        elif child_ele.name == "nav":
            if child_ele.text == "":
                continue
            if child_ele.text.startswith('本节包含以下内容'):
                continue
            print(child_ele)
            print("nav bb 过滤特殊nav")
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
            content.add_content(f"[{child_ele.text}]({child_ele.get('href')})")
            if child_ele == element.contents[-1]:
                content.add_content(os.linesep)
        else:
            content.add_content(f"{child_ele.text} {os.linesep}")


def html_to_markdown(html, level, path):
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
            print("related")
        elif element.text.strip().startswith("背景知识") or element.text.strip().startswith("功能说明") or element.attrs.get(
                "id") == "docDetail":
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content
        else:
            content = Content(path, title)
            digui_parse(element, level, content)
            body += content.content

    return body
