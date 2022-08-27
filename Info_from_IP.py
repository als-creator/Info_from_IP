import requests
from pyfiglet import Figlet
import folium
def get_info_from_ip(ip='INSERT IP ADDRESS'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)
        data = {
            '[IP]': response.get('query'),
            '[Provider]': response.get('isp'),
            '[Organization]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP Code]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        for k,v in data.items():
            print(f'{k}:{v}')

        area = folium.Map(location=[response.get('lat'),response.get('lon')])
        area.save(f"{response.get('query')}_{response.get('city')}.html")

        pass
    except requests.exceptions.ConnectionError:
        print('Проверьте интернет')
def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP Info'))
    ip = input('Введите целевой IP: ')
    get_info_from_ip(ip=ip)
if __name__ == '__main__':
    main() 