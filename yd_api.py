import requests
import datetime


class YDAPIclient:

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def creating_folder_in_yd(self, path_folder):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': self.auth_token}
        params = {'path': path_folder}
        response = requests.put(url, headers=headers, params=params)
        return response

    def _copy_foto(self, path_folder, foto):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        path_file = f'{path_folder}{foto["file_name"]}'
        download_url = foto['url']
        headers = {'Authorization': self.auth_token}
        params = {'url': download_url,
                  'path': path_file}
        response = requests.post(url, headers=headers, params=params)
        upload_url = response.json()['href']
        response = requests.get(upload_url, headers=headers)
        return response.json()['status']

    def backup_photos_in_yd(self, list_of_fotos, path_folder):
        for foto in list_of_fotos:
            status = 'failed'
            i = 0
            while status == 'failed' and i < 5:
                status = self._copy_foto(path_folder, foto)
                i += 1
            if i == 1:
                print(f'Файл {foto["file_name"]} скопирован в {datetime.datetime.now()}!')
            else:
                print(f'Файл {foto["file_name"]} скопирован в {datetime.datetime.now()} с {i}-й потытки!')
            if i == 5:
                print(f'Файл {foto["file_name"]} не удалось скопировать из-за ошибки яндекс-диска! \n'
                      f'Попробуйте сделать копию позже.')

    def creating_folder_and_copy_photos(self, number_of_photos, list_of_photos):
        while True:
            folder_name = input('Задайте имя папки, в которую необходимо сохранить '
                                'фотографии: ')
            path_folder = f'disk:/{folder_name}/'
            response = self.creating_folder_in_yd(path_folder)
            status_operation = response.status_code
            if status_operation == 201:
                print(f'Создана папка {folder_name} для backup фото из VK в '
                      f'{datetime.datetime.now()}!')
                self.backup_photos_in_yd(list_of_photos[:number_of_photos], path_folder)
                break
            elif status_operation == 401:
                print('Отсутствует доступ к яндекс-диску!\n'
                      'Введите правильный OAuth-токен яндекс-диска в настройках '
                      'приложения.')
                break
            elif status_operation == 409:
                print('Задано неправильное название папки!')
            else:
                print(f'Ошибка: {response.json().get("message")}\n'
                      f'Проверьте все настройки приложения и попробуйте заново сделать'
                      f' резервное копирование фотографий.')
                break
