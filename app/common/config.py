from configparser import ConfigParser

parser = ConfigParser()
parser.read('config/config_base.ini')
env = parser.get('base', 'env')
parser.read(f'config/config_{env}.ini')


class cfg:
    @staticmethod
    def parse_attr(attr, sep='.'):
        arr = attr.split(sep)
        if len(arr) == 2:
            return dict(
                section=arr[0],
                option=arr[1]
            )
        return None

    @staticmethod
    def get(attr):
        data = cfg.parse_attr(attr)
        if data:
            return parser.get(data['section'], data['option'])
        return None

    @staticmethod
    def getint(attr):
        data = cfg.parse_attr(attr)
        if data:
            return parser.getint(data['section'], data['option'])

    @staticmethod
    def getboolean(attr):
        data = cfg.parse_attr(attr)
        if data:
            return parser.getboolean(data['section'], data['option'])
