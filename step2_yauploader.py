import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/'

    def get_headers(self):
        """Возвращает параметры хедэра"""
        return {
            'Accept': 'application/json',
            'Authorization': self.token}
        
    def get_link(self, path):
        """возвращает ответ на создание места на диске"""
        par = {'path': path, 
               'overwrite': 'True'} # перезапись не работает почему то...
        return requests.get(f'{self.url}resources/upload', headers=self.get_headers(),
                              params=par).json()
    
    def upload(self, file_mame: str, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_link(file_path).get('href', '')
        if href:
            upload = requests.put(href, data=open(file_mame, 'rb'))
            return 'Файл загружен на диск' if upload.status_code == 201 else 'что то пошло не по плану'
        return 'Что то пошло не так, ссылка не получена, файл не загружен'
       

if __name__ == '__main__':
    path_to_file = 'image.jpeg'
    token = input('Token pls ')
    uploader = YaUploader(token)
    print(uploader.upload('image.jpeg', path_to_file))
    