import markdown
import os
import codecs
from dove.utils import ObjectDict

class Reader(object):
    '''
    Base class for read files
    '''
    def __init__(self, filename=None):
        # self.settings =
        pass

    def convert(self):
        '''
        返回
        '''
        with open(path, 'r') as stream:
            return stream

class MarkdownReader(object):

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
    def meta(self):
        '''返回 meta data'''
        meta = {'title':[''], 'author':[''], 'tags':[''], 'published_date':[''], 'modify_date':['']}
        self.convert()
        try:
            meta.update(self.markdown.Meta)
        except:
            pass

        meta = {k:v[0] for k, v in meta.items()}
        if meta.get('title', None) is None:
            # 从 path 中解析出文件名
            filename = os.path.splitext(os.path.split(self.path)[-1])[0]
            meta.update({'title':filename})
        return meta
