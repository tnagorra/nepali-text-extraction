import yaml

class Grammar:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        with open(filename, encoding='utf-8') as in_file:
            file = yaml.load(in_file)
            for key, value in file.items():
                if type(value) is list:
                    self.put(key + '_raw', ''.join(value))
                    self.put(key, '[' + ''.join(value) + ']')
                else:
                    self.put(key, value)

    def get(self, name):
        return self.data[name]

    def put(self, name, string):
        self.data[name] = string

    def putr(self, name, string):
        self.data[name] = string.format(**self.data)


