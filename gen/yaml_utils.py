import os
import yaml


class YamlUtils:
    @staticmethod
    def get_python_file():
        """
        读取指定目录下的python文件名列表
        :param directory: 目录路径
        :return: python文件名列表
        """
        python_files = []
        root_path = os.path.abspath(os.path.join(os.getcwd(), "entity"))
        for root, dirs, files in os.walk(root_path):
            for file in files:
                if 'cpython' not in file:
                    suffix = os.path.splitext(file)[-1]
                    if suffix.startswith('.py'):
                        python_files.append("entity." + file.split(".")[0])

        return python_files

    @staticmethod
    def read_yaml_file(file_path):
        """
        读取项目根路径下的 yaml 文件，并返回其内容
        :param file_path: 文件路径
        :return:  返回指定 yaml 文件文本内容
        """
        # 获取项目根路径
        root_path = os.path.abspath(os.path.join(os.getcwd(), ""))
        # 拼接完整文件路径
        file_path = os.path.join(root_path, file_path)
        # 读取 yaml 文件内容
        with open(file_path, 'r') as f:
            content = yaml.safe_load(f)
        return content

    @staticmethod
    def update_yaml_model():
        """
        读取项目根路径下的 yaml 文件，动态获取 entity 目录下的实体文件，并设置其实体声明类至 config.yaml 的 app.ts.models 下
        :return:  返回指定 yaml 字典
        """
        file_names = YamlUtils.get_python_file()
        # for file_name in file_names:
        #     print(file_name)
        data = YamlUtils.read_yaml_file("../config.yml")
        # 修改apps:ts:models内容
        data['apps']['ts']['models'] = file_names
        return data



