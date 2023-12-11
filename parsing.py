import requests
from bs4 import BeautifulSoup
import csv


def write_to_csv(data: dict):
    with open('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow((data['title'], data['price'], data['img'], data['descr']))


def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    cars = soup.find('div', class_ = 'catalog-list').find_all('a')
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_="catalog-item-caption").text.strip() # .strip -> убирает лишние пробелы
        except:
            title = ''
        
        try:
            price = car.find('span', class_="catalog-item-price").text
        except:
            price = ''

        try:
            descr = car.find('span', class_='catalog-item-descr').text.split()
            descr = ' '.join(descr)
        except:
            descr = ''

        try:
            img = car.find('img').get('src')
        except:
            img = ''


        data = {
            'title': title,
            'price': price,
            'img': img,
            'descr': descr
        }

        write_to_csv(data)

        # print(title)
        # print(price)
        # print(descr)
        # print(img)
        # print(car)
        # print('=============')



def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    get_data(html)



with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title ', 'price ', 'image ', 'description'])


main()





'''ТАСКИ'''

# 1.
'''Нужно получить статус запроса доступа к странице:

https://stackoverflow.com/questions

В начале, получите статус запроса и присвойте результат запроса к переменной source.

Затем выведите эту переменную в консоль.

Вывод в консоль должен быть таким:

200

'''
# import requests

# source = requests.get('https://stackoverflow.com/questions').status_code # так правильно (так читабельнее)
# print(source)


# source = requests.get('https://stackoverflow.com/questions')             # так тоже правильно
# print(source.status_code)



# 2.
'''Спарсите тэги h1, p и ссылку с тэга a из веб-страницы:

http://www.example.com/

и выведите результат в консоль в таком виде:

h1:  Example Domain

p:  This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.

a:  https://www.iana.org/domains/example  
'''
# from bs4 import BeautifulSoup 
# import requests 
# import csv 

# source = requests.get('http://www.example.com/').text 
# my_page = BeautifulSoup(source, 'lxml') 
# print('h1:', my_page.h1.text) 
# print('p:', my_page.p.text) 
# print('a:', my_page.a.get('href'))



# 3.
'''Выведите с главной страницы википедии:

https://www.wikipedia.org/

сколько всего статей есть немецком языке.

Вывод в консоль должен быть таким:

Deutsch

2 590 000+ Artikel 
'''
# from bs4 import BeautifulSoup 
# import requests 
# import csv 

# source = requests.get('https://www.wikipedia.org/').text 
# my_page = BeautifulSoup(source, 'lxml') 
# blog_lang = my_page.find('div', class_ = 'central-featured-lang lang5') 
# print(blog_lang.text)




# 4.
'''Напишите программу которая проверяет имеет ли страница заголовок(тэг h1) или нет.

Для этого напишите функцию getTitle() которая будет принимать url страницы и возвращать заголовок если он есть, если же его нет то будет возвращать "Title could not be found"

 print(getTitle('http://www.example.com/'))
Output:

 <h1>Example Domain</h1>
 '''
# from bs4 import BeautifulSoup
# import requests

# def getTitle(url):
#     response = requests.get(url).text
#     soup = BeautifulSoup(response, 'lxml')
#     i = soup.find('h1')
    
#     if i:
#         return i
#     else:
#         return "Title could not be found"

# print(getTitle('http://www.example.com/'))





# 5.
'''Напишите код который сохраняет все названия категорий со страницы:

https://enter.kg/

в список category_list.

После, напишите функцию которая имеет два параметра - список категорий - categories и ключевое слово - keyword.

Функция должна производить поиск по ключевому слову в списке заголовков category_list и возвращать список заголовков которые содержат данное слово (независимо от регистра).

К примеру:

print(find_category(category_list, 'Ноутбуки')) 
Вывод будет:

['Ноутбуки, Ультрабуки, Гот. решения (1281)', 'Ноутбуки (1235)', 'Ноутбуки, Ультрабуки, Гот. решения(1281)', 'Ноутбуки и ультрабуки'] 
'''
# import requests
# from bs4 import BeautifulSoup as BS

# def find_category(categories: list, keyword: str) -> list:
#     result = []
#     for category in categories:
#         if keyword.lower() in category.lower():
#             result.append(category)
#     return result

# category_list = []
# URL = "https://enter.kg/"
# response = requests.get(URL)
# soup = BS(response.text, "html.parser")
# categories = soup.find_all("li", {"class": "VmClose"})
# for category in categories:
#     title = category.find("a").text
#     category_list.append(title)

# categories = soup.find_all("span", {"class": "category-product-count"})
# for category in categories:
#     title = category.text.strip()
#     category_list.append(title)

# print(find_category(category_list, 'Ноутбуки'))




# 6.
'''Напишите программу которая будет парсить топ 250 фильмов с сайта IMBD:

https://www.imdb.com/chart/top

Затем напишите функцию get_link, которая будет принимать в аргументы список фильмов - title_list и строку - name. Функция должна производить поиск в списке по строке и возвращать ссылку на фильм. Вы должны вернуть только первое совпадение в списке.

Например:

get_link(title_list, 'shawshank') 
Вернет вам:

https://www.imdb.com/title/tt0111161/ 
'''
# import requests
# from bs4 import BeautifulSoup

# def parse_top_250_movies():
#     url = "https://www.imdb.com/chart/top"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     movie_table = soup.find("table", {"class": "chart full-width"})
    
#     if movie_table is None:
#         print("Не удалось найти таблицу с фильмами.")
#         return []

#     movie_rows = movie_table.find_all("tr")
#     title_list = []

#     for row in movie_rows[1:]:
#         cells = row.find_all("td")
#         rank = cells[0].get_text().strip()
#         title = cells[1].a.get_text().strip()
#         title_list.append(title)

#     return title_list

# def get_link(title_list, name):
#     for title in title_list:
#         if name.lower() in title.lower():
#             url = f"https://www.imdb.com/find?q={title.replace(' ', '+')}"
#             return url

#     return None

# # Пример использования
# title_list = parse_top_250_movies()
# search_name = "shawshank"
# link = get_link(title_list, search_name)

# if link:
#     print(f"Ссылка на фильм '{search_name}': {link}")
# else:
#     print(f"Фильм '{search_name}' не найден.")





'''побольше про библиотеку requests'''
import requests

url = 'https://www.example.com'
response = requests.get(url)

print(f'Статус кода: {response.status_code}')
print(f'Содержание:\n{response.text}')
