import os
import re
import markdown
import codecs
import yaml
import mistune

ROOT_PATH = os.getcwd()
CONF_PATH = os.path.join(ROOT_PATH, 'conf')

def load_conf(filename, subconf=None):
    '''
    load yaml configure
    '''
    if filename[-5:] != '.yaml':
        filename = filename + '.yaml'

    conf_file = os.path.join(CONF_PATH, filename)
    with open(conf_file, 'r') as stream:
        try:
            data = yaml.load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)
            return

class ObjectDict(dict):

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value
        
class Rst(object):
    pass

class Markdown(object):

    '''
    Markdown 解析

    '''
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.markdown = markdown.Markdown(extensions=['markdown.extensions.abbr', \
                    'markdown.extensions.attr_list', \
                    'markdown.extensions.def_list', \
                    'markdown.extensions.fenced_code', \
                    'markdown.extensions.footnotes', \
                    'markdown.extensions.tables', \
                    'markdown.extensions.smart_strong', \
                    'markdown.extensions.admonition', \
                    'markdown.extensions.codehilite', \
                    'markdown.extensions.meta', \
                    'markdown.extensions.nl2br', \
                    # 'markdown.extensions.toc', \
                    'markdown.extensions.wikilinks', \
                    ])

    def convert(self):
        '''
        转换 markdown 文档为 html , 并输出到文件中
        '''

        if self.filepath is not None:
            if os.path.isfile(self.filepath):
                input_file = codecs.open(self.filepath, mode='r', encoding='utf-8')
                text = input_file.read()
                html = self.markdown.convert(text)
                return html

    def write(self, path, filename):
        '''写入'''
        if os.path.exists(path) is False:
            os.makedirs(path)

        output_path = os.path.join(path, filename)

        with open(output_path, 'w') as fp:
            fp.write(self.html)

    @property
    def html(self):
        '''返回 html'''
        return self.convert()


    @property
    def Meta(self):
        '''返回 meta data'''
        try:
            meta = self.markdown.Meta
        except Exception:
            self.convert()
            meta = self.markdown.Meta
        print(meta)
        return meta


    # def load_file(self, path):
    #     '''读取文件'''
    #     if path is not None:
    #         if os.path.isfile(path):
    #             stream = list()
    #             with open(path, 'r') as fp:
    #                 for line in fp:
    #                     stream.append(line)
    #
    #                 return stream
    #     else:
    #         return None
    #
    # @property
    # def title(self):
    #     '''返回 md 文档中的所有标题'''
    #
    #     return self.get_title()
    #
    # def get_title(self):
    #     '''
    #     获取 Markdown 的层级目录
    #     返回数据格式：
    #     [
    #         ('title1', level1),
    #         ('title2', level1),
    #         ('title3', level2)
    #     ]
    #     '''
    #     re_title = re.compile(r'^(#{1,6}\s.*)')
    #     data = list()
    #
    #     for k in self.stream:
    #         if re_title.search(k):
    #             tmp = re_title.search(k).group(0)
    #             print(tmp)
    #             if tmp[0:2] == '# ':
    #                 data.append((tmp[2:], 1))
    #             elif tmp[0:3] == '## ':
    #                 data.append((tmp[3:], 2))
    #             elif tmp[0:4] == '### ':
    #                 data.append((tmp[4:], 3))
    #             elif tmp[0:5] == '#### ':
    #                 data.append((tmp[5:], 4))
    #             elif tmp[0:6] == '##### ':
    #                 data.append((tmp[6:], 5))
    #             elif tmp[0:7] == '###### ':
    #                 data.append((tmp[7:], 6))
    #
    #     return data

# class Markdown(object):
#     '''
#     fuck
#     自己实现个 markdown 分析器
#     可以提取所有章节，
#     可以提取 meta data
#     可以设置
#     '''

if __name__ == '__main__':
    # md = Markdown('./test.md')
    # print(md.html)
    # print(md.Meta)
    # md.write('./output', 'test.html')
    markdown = mistune.Markdown()
    with open('./test.md', 'r') as stream:
        ss = markdown(stream.read())

    print(ss)
