from datetime import datetime
import requests
from pprint import pprint
import json

class ParserStackOverflow:
    def __init__(self, tags: list|str) -> None:
        self.url = 'https://api.stackexchange.com/'
        self.tags = tags
        
    @staticmethod
    def date_today() -> int:
        """Возвращает текущие дату/время в секундах"""
        return int(datetime.now().timestamp())
    
    @staticmethod
    def date_per_2days() -> int:
        """Возвращает текущие дату/время в секундах 2 дня назад"""
        days_ = 2
        return int(datetime.now().timestamp())- (days_*24*60*60)
    
    def get_request(self, num) -> dict|None:
        """Возвращает словарь с ответом от сервера"""
        method = '/2.3/search?'
        params = {'page': num,
                  'pagesize': 100,
                  'fromdate': self.date_per_2days(),
                  'todate': self.date_today(),
                  'order': 'desc', 
                  'sort': 'activity', 
                  'tagged': self.tags,
                  'site': 'stackoverflow'}
        resp = requests.get(f'{self.url}{method}', params=params)
        
        if resp.status_code == 200:
            return resp.json()
        raise ValueError
    
    def squeeze_request(self) -> dict:
        """Возвращает выжимку в формате словаря, где ключ автор, и 
        значениями являются ссылки и тема"""
        news_dict = {}
        page = 1
        while True:
            items = self.get_request(page)
            for item in items['items']:
                author = item['owner']['display_name']
                news_dict.setdefault(author, {}).update({'title': item['title']})
                news_dict[author].update({'link': item['link']})
            if items['has_more']:
                page += 1
            else:
                break
        return news_dict
    

if __name__ == '__main__':
    my_parser = ParserStackOverflow('python')
    answer = my_parser.squeeze_request()
    # мы можем выбрать вывод - либо в консоль, либо в файл
    # pprint(answer)
    with open('my_parser.json', 'w', encoding='utf-8') as file_out:
        json.dump(answer, file_out, indent=4, ensure_ascii=False)