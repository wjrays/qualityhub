import requests

import logging

logger = logging.getLogger(__name__)

class Apiclient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self,path,params = None):
        url = f'{self.base_url}{path}'
        logger.info('发送GET请求:%s',url)
        responses = self.session.get(
            url,
            params = params,
            timeout = 10,
        )
        logger.info('收到相应，状态码:%s',responses.status_code)
        return responses

    def close(self):
        return self.session.close()
