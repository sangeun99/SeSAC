import requests
from bs4 import BeautifulSoup

def get_title_rate_reserv():
    data = requests.get('https://movie.daum.net/ranking/reservation')
    soup = BeautifulSoup(data.text, 'html.parser')

    info = soup.select('.list_movieranking > li')
    movie_link_root = 'https://movie.daum.net'
    for i in info :
        title = i.select_one('.link_txt').text
        grade = i.select_one('.txt_grade').text
        reserv = i.select_one('.txt_num').text
        print(f"제목 : {title}, 평점 : {grade}, 예매율 : {reserv}")
        link = i.select_one('.link_txt')['href']
        short_desc = i.select_one('.link_story').text.strip()
        print(movie_link_root + link)
        print(short_desc)

if __name__ == "__main__" :
    get_title_rate_reserv()