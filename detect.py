#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re

root_node = []

class Node:

    def __init__(self,path,prefix):
        self.path = path
        self.prefix = prefix
        self.children=[]

    def add_child(self,node):
        self.children.append(node)

    def print_node(self):
        if len(self.children)==0:
            print self.prefix+"/"+self.path
        else:
            for i  in self.children:
                i.print_node()


# x一些正则样式
class RegexPatterns:
    hash_pattern1 = "[\dabcdef]{6,}"
    hash_pattern2 = "[\dABCDEF]{6,}"
    number_pattern = "\d{4,}"




"""
返回行的列表,类型list
"""
def load_file(filename):
    return open(filename).readlines()


"""
解析每一行数据,生成节点
"""
def parse_line(line):
    host,path,num = line.split('\t')
    current_level = root_node
    split_list = [host].extend(path.split('/'))
    for node_name in range(len(split_list)):
        # 在本层中寻找是否存在本层的节点
        existed = False
        for node in current_level.children:
            if node.path == node_name:
                current_level = node
                existed = True






"""
清洗数据,只执行一次
"""
def remove_static_resource(lines):
    static_pattern = re.compile('\.(jpg|jpeg|gif|js|css|tpl|json|png)\s')
    f=open('wash1.txt','w')
    washed_lines=[]
    for line in lines:
        if not static_pattern.search(line):
            washed_lines.append(line)
    f.writelines(washed_lines)



if __name__ == '__main__':
    lines = load_file('test.txt')
    remove_static_resource(lines)