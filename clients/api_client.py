import requests


class Apiclient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self,path,params = None):
        return self.session.get(
            f'{self.base_url}{path}',
            params = params,
            timeout = 10,
        )

    def close(self):
        return self.session.close()
