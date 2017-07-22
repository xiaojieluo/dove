import os
import ruamel.yaml
from ruamel.yaml.util import load_yaml_guess_indent
from collections import OrderedDict

ROOT_PATH = os.getcwd()
CONF_PATH = os.path.join(ROOT_PATH, 'conf')

class Setting(object):

    def __init__(self, filename, **kw):
        self.filename = self.handle_file(filename)
        self.conf_file = os.path.join(CONF_PATH, self.filename)
        self.get_conf()

    def __iter__(self):
        return self.data

    def __getattr__(self, key):
        try:
            return self.data[key]
        except KeyError:
            return ''

    def handle_file(self, filename):
        '''
        处理 filename 参数，
        如果没有.yaml 后缀，则加上
        '''
        if filename[-5:] != '.yaml':
            filename = filename + '.yaml'

        return filename

    def get_conf(self):
        '''
        load yaml configure
        '''
        try:
            with open(self.conf_file, 'r') as stream:
                self.data, self.ind, self.bsi = load_yaml_guess_indent(stream)
        except:
            raise

    def save(self):
        '''
        保存临时更改的配置信息到 yaml 文件中
        '''
        with open(self.conf_file, 'w') as stream:
            ruamel.yaml.round_trip_dump(self.data, stream, indent=self.ind,
                                        block_seq_indent=self.bsi)
