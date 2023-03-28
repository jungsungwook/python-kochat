import itertools
import re

import numpy as np
from abc import ABCMeta
import requests
import json

class ServerApi(metaclass=ABCMeta):
    def request(self, server, target):
        """
        서버 정보를 제공 하는 API 입니다.
        """
        try:
            return_text = f""
            response = requests.get(f"http://127.0.0.1:8521/server?name={server}&target={target}")
            if response.status_code != 200:
                return "서버와의 통신이 원활하지 않습니다."
            
            result = json.loads(response.text)
            if result['status'] == 'error':
                return "서버와의 통신이 원활하지 않습니다."
            
            if(len(result['data']) < 1):
                return_text += f"{server} 서버에 대한 정보가 없습니다.\n"
                response = requests.get(f"http://127.0.0.1:8521/server/all")
                if response.status_code != 200:
                    return "서버와의 통신이 원활하지 않습니다."
            
                result = json.loads(response.text)
                if result['status'] == 'error':
                    return "서버와의 통신이 원활하지 않습니다."
                
                if(len(result['data']) < 1):
                    return_text += f"모든 서버에 대한 정보가 없습니다.\n"
                    return return_text
                return_text += "대신, 모든 서버에 대한 정보를 알려드리겠습니다.\n"
                for i in range(len(result['data'])):
                    return_text += f"{i+1}. {result['data'][i]}\n"
                return return_text
            
            if(len(result['data']) > 1):
                return_text += "{0} 서버에 대한 정보가 {1}개 있습니다.\n".format(server, len(result['data']))
                for i in range(len(result['data'])):
                    return_text += "\n{0}번째 서버의 정보입니다.\n".format(i+1)
                    return_text += f"서버 이름 : {result['data'][i]['name']}\n"
                    return_text += f"서버 주소 : {result['data'][i]['ip']}\n"
                    return_text += f"서버 정보 : {result['data'][i]['info']}\n"
                    return_text +="====================\n"
            else:
                return_text += f"{server} 서버의 정보입니다.\n"
                return_text += f"서버 이름 : {result['data'][0]['name']}\n"
                return_text += f"서버 주소 : {result['data'][0]['ip']}\n"
                return_text += f"서버 정보 : {result['data'][0]['info']}\n"
            return return_text
        except Exception:
            return "[server api]문의 바랍니다."
    
    def _flatten_list(self, list_: list) -> list:
        """
        n차원 리스트를 1차원으로 만듭니다.
        
        :param list_: n차원 리스트 
        :return: 1차원으로 변형된 리스트
        """

        np.array(list_)
        while len(np.array(list_).shape) != 1:
            list_ = list(itertools.chain.from_iterable(list_))
        return list_

    def _flatten_dicts(self, dict_: dict) -> dict:
        """
        딕셔너리의 value 리스트를 전부 1차원으로 만듭니다.

        before :
        dict = {
            key1 : [[val1, val2], [val3, val4], [val5, val6]]
            key2 : [[val1, val2], [val3, val4], [val5, val6]]
        }

        after :
        dict = {
            key1 : [val1, val2, val3, val4, val5, val6]
            key2 : [val1, val2, val3, val4, val5, val6]
        }

        :param dict_: n차원 리스트를 값으로 가지고 있는 딕셔너리
        :return: 1차원 리스트만 값으로 가지고 있는 딕셔너리
        """
        for k, v in dict_.items():
            dict_[k] = self._flatten_list(dict_[k])
        return dict_