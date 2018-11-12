import yaml

class YmlDao():
    """Simplified Data Access Object which is initialized using
    a YML file containing the access credentials
    """

    def __init__(self, yaml_file, name):
        # Load "name" from YML file
        access_data = yaml.load(open(yaml_file, 'r'))[name]
        self.public =  access_data['public']
        self.private = access_data['private']

if __name__ == '__main__':
    aver = YmlDao('credential.yml', 'api')
    print(aver.public)
    print(aver.private)