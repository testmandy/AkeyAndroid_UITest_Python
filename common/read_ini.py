# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy
import configparser
import conftest


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conftest.android_elements_dir
        else:
            self.file_path = file_path
        self.data = self.read_ini()
        self.config = configparser.ConfigParser()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding="utf-8")
        return read_ini

    def get_value(self, key, section=None):
        if section is None:
            section = 'Common'
        else:
            section = section
        return self.data.get(section, key)

    def set_ini(self, section, key, value):
        try:
            self.config.set(section, key, value)
            self.config.write(open(self.file_path, 'r+'))
        except:
            assert '写入数据失败'

# if __name__ == '__main__':
#     readIni = ReadIni()
#     print(readIni.file_path)
#     local = readIni.get_value("Common_fullScreenAds")
#     print(local)

