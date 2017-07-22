import os
from dove import utils
from dove.readers import MarkdownReader
import html2text
import shutil
import uuid
from dove.settings import Setting

class Dove(object):
    '''
    Dove class
    '''
    def __init__(self, settings = dict()):
        self.settings = self._settings(settings)

    def _settings(self, conf):
        '''将默认设置与用户传入的设置合并'''
        settings = {
            'content_path':'content',
            'output_path':'output',
            'support_format':'.md, .rst'
        }
        if isinstance(conf, dict):
            settings.update(conf)

        return settings

    @property
    def articles(self):
        '''返回所有文章'''
        articles = list()
        if os.path.exists(self.settings['content_path']):
            for index,f in enumerate(os.listdir(self.settings['content_path'])):
                path = os.path.join(self.settings['content_path'], f)
                support_format = self.settings['support_format'].split(',')
                if os.path.splitext(path)[-1] in support_format:
                    art = Article(path)
                    # 为 article 设置 id
                    art.id = index
                    articles.append(art)
                # file_ = f.split('.')
                # path = os.path.join(self.settings['content_path'], f)
                # support_format = self.settings['support_format'].split(',')
                # if file_[-1] in support_format:
                #     tmp = utils.Markdown(path)
                #     # 如果文档中没有 title meta， 就用文件名做 title
                #     if tmp.Meta.get('title', None) is None:
                #         tmp.Meta['title'] = file_[0:-1][0]
                #     if tmp.Meta.get('content', None) is None:
                #         tmp.Meta['content'] = tmp.html
                #     articles.append(tmp.Meta)

        return articles

class Article(object):
    '''
    文章类
    meta: 表示 所有的元数据
    content: 未转换的文本内容， 不包含 metadata
    html: 已转换成html的内容，不包含 metadata
    '''
    _markdown_format = ['md', 'markdown']

    def __init__(self, path, **kw):
        self.filepath = path
        self.settings = Setting('dove')
        # self.settings = kw.get('settings')
        type_ = os.path.split(self.filepath)[-1]
        self.fp = MarkdownReader(self.filepath)

    def __getattr__(self, name):
        '''
        利用 __getattr__ 实现反射
        '''
        try:
            if name in self.fp.meta:# 如果是字典
                return self.fp.meta[name]
            elif hasattr(self.fp, name):# 如果是属性
                return getattr(self.fp, name)
        except:
            raise

    @property
    def path(self):
        return self.filepath

    @property
    def id(self):
        '''返回id'''
        return self.id_

    @id.setter
    def id(self, value):
        '''设置id'''
        self.id_ = value

    @property
    def content(self):
        content = html2text.html2text(self.html)
        # content = content.replace('\n', '<br />')
        return content


    def delete(self):
        '''删除文件'''
        '''其实并不真的删除，只是把文件移到 tmp 目录中'''
        '''删除 tmp 目录中的文件才算是彻底删除'''
        '''防止误删'''

        shutil.copy(self.filepath, self.settings.tmp_path)
        os.remove(self.filepath)

        return True



if __name__ == '__main__':
    # article = Article('tools/templates/content/hello.md')
    # print(article.html)
    # dove = Dove(utils.load_conf('dove'))
    settings = {
        'content_path':'tools/templates/content',
        'output_path':'tools/templates/output',
        'support_format':'.md, .rst',
        'tmp_path':'tools/templates/.tmp'
    }
    dove = Dove(settings=settings)
    article = dove.articles[1]
    # print(article.delete())
