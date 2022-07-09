import json
class Config():

    def __init__(self):
        with open("config.json") as json_elem:
            config = json.load(json_elem)
            self.api_key = config['api_key']
            self.sending_user_email = config['sending_user_email']
            self.sending_user_app_password = config['sending_user_app_password']
            self.receiving_user_email = config['receiving_user_email']

config = Config()
