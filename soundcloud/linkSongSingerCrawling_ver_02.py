from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

url_homepage = "https://soundcloud.com/discover"

# modify the chromewebdriver address to execute the code.
driver = webdriver.Chrome(
    "/Users/seongminheo/Desktop/teamproject/soundcloudcrawling/chromedriver")
driver.get(url_homepage)

# login
# cannot find connect with google button
# 수동로그인 -> 해결해야 함

top50 = {
    'ambient': {'url': 'https://soundcloud.com/discover/sets/charts-top:ambient:kr',
                'cnt_download': 0,
                'link': [],
                'songTitle': [],
                'singer': []},
    'allMusic': {'url': 'https://soundcloud.com/discover/sets/charts-top:all-music:kr',
                 'cnt_download': 0,
                 'link': [],
                 'songTitle': [],
                 'singer': []},
    'alterRock': {'url': 'https://soundcloud.com/discover/sets/charts-top:alternativerock:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'classical': {'url': 'https://soundcloud.com/discover/sets/charts-top:classical:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'country': {'url': 'https://soundcloud.com/discover/sets/charts-top:country:kr',
                'cnt_download': 0,
                'link': [],
                'songTitle': [],
                'singer': []},
    'danceedm': {'url': 'https://soundcloud.com/discover/sets/charts-top:danceedm:kr',
                 'cnt_download': 0,
                 'link': [],
                 'songTitle': [],
                 'singer': []},
    'dancehall': {'url': 'https://soundcloud.com/discover/sets/charts-top:dancehall:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'deephouse': {'url': 'https://soundcloud.com/discover/sets/charts-top:deephouse:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'disco': {'url': 'https://soundcloud.com/discover/sets/charts-top:disco:kr',
              'cnt_download': 0,
              'link': [],
              'songTitle': [],
              'singer': []},
    'drumbass': {'url': 'https://soundcloud.com/discover/sets/charts-top:drumbass:kr',
                 'cnt_download': 0,
                 'link': [],
                 'songTitle': [],
                 'singer': []},
    'dubstep': {'url': 'https://soundcloud.com/discover/sets/charts-top:dubstep:kr',
                'cnt_download': 0,
                'link': [],
                'songTitle': [],
                'singer': []},
    'eletronic': {'url': 'https://soundcloud.com/discover/sets/charts-top:electronic:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'folkSingersongwriter': {'url': 'https://soundcloud.com/discover/sets/charts-top:folksingersongwriter:kr',
                             'cnt_download': 0,
                             'link': [],
                             'songTitle': [],
                             'singer': []},
    'hiphopRap': {'url': 'https://soundcloud.com/discover/sets/charts-top:hiphoprap:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'house': {'url': 'https://soundcloud.com/discover/sets/charts-top:house:kr',
              'cnt_download': 0,
              'link': [],
              'songTitle': [],
              'singer': []},
    'indie': {'url': 'https://soundcloud.com/discover/sets/charts-top:indie:kr',
              'cnt_download': 0,
              'link': [],
              'songTitle': [],
              'singer': []},
    'jazzBlues': {'url': 'https://soundcloud.com/discover/sets/charts-top:jazzblues:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'metal': {'url': 'https://soundcloud.com/discover/sets/charts-top:metal:kr',
              'cnt_download': 0,
              'link': [],
              'songTitle': [],
              'singer': []},
    'pop': {'url': 'https://soundcloud.com/discover/sets/charts-top:pop:kr',
            'cnt_download': 0,
            'link': [],
            'songTitle': [],
            'singer': []},
    'rbSoul': {'url': 'https://soundcloud.com/discover/sets/charts-top:rbsoul:kr',
               'cnt_download': 0,
               'link': [],
               'songTitle': [],
               'singer': []},
    'rock': {'url': 'https://soundcloud.com/discover/sets/charts-top:rock:kr',
             'cnt_download': 0,
             'link': [],
             'songTitle': [],
             'singer': []},
    'soundtrack': {'url': 'https://soundcloud.com/discover/sets/charts-top:soundtrack:kr',
                   'cnt_download': 0,
                   'link': [],
                   'songTitle': [],
                   'singer': []},
    'world': {'url': 'https://soundcloud.com/discover/sets/charts-top:world:kr',
               'cnt_download': 0,
               'link': [],
               'songTitle': [],
               'singer': []},
}

newHot = {
    'ambient': {'url': 'https://soundcloud.com/discover/sets/charts-trending:ambient:kr',
                'cnt_download': 0,
                'link': [],
                'songTitle': [],
                'singer': []},
    'allMusic': {'url': 'https://soundcloud.com/discover/sets/charts-trending:all-music:kr',
                 'cnt_download': 0,
                 'link': [],
                 'songTitle': [],
                 'singer': []},
    'alterRock': {'url': 'https://soundcloud.com/discover/sets/charts-trending:alternativerock:kr',
                  'cnt_download': 0,
                  'link': [],
                  'songTitle': [],
                  'singer': []},
    'classical': {'url': 'https://soundcloud.com/discover/sets/charts-trending:classical:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'country': {'url': 'https://soundcloud.com/discover/sets/charts-trending:country:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'danceedm': {'url': 'https://soundcloud.com/discover/sets/charts-trending:danceedm:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'dancehall': {'url': 'https://soundcloud.com/discover/sets/charts-trending:dancehall:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'deephouse': {'url': 'https://soundcloud.com/discover/sets/charts-trending:deephouse:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'disco': {'url': 'https://soundcloud.com/discover/sets/charts-trending:disco:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'drumbass': {'url': 'https://soundcloud.com/discover/sets/charts-trending:drumbass:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'dubstep': {'url': 'https://soundcloud.com/discover/sets/charts-trending:dubstep:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'eletronic': {'url': 'https://soundcloud.com/discover/sets/charts-trending:electronic:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'folkSingersongwriter': {'url': 'https://soundcloud.com/discover/sets/charts-trending:folksingersongwriter:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'hiphopRap': {'url': 'https://soundcloud.com/discover/sets/charts-trending:hiphoprap:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'house': {'url': 'https://soundcloud.com/discover/sets/charts-trending:house:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'indie': {'url': 'https://soundcloud.com/discover/sets/charts-trending:indie:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'jazzBlues': {'url': 'https://soundcloud.com/discover/sets/charts-trending:jazzblues:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'metal': {'url': 'https://soundcloud.com/discover/sets/charts-trending:metal:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'pop': {'url': 'https://soundcloud.com/discover/sets/charts-trending:pop:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'rbSoul': {'url': 'https://soundcloud.com/discover/sets/charts-trending:rbsoul:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'rock': {'url': 'https://soundcloud.com/discover/sets/charts-trending:rock:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'soundtrack': {'url': 'https://soundcloud.com/discover/sets/charts-trending:soundtrack:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},
    'world': {'url': 'https://soundcloud.com/discover/sets/charts-trending:world:kr',
         'cnt_download': 0,
         'link': [],
         'songTitle': [],
         'singer': []},

}
len(top50.keys())
len(newHot.keys())

# top50
for i, genre in enumerate(top50):
    # conncet genre url
    driver.get(top50[genre]['url'])

    # clear popup
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/button').click()
        print('Popup cleared')
    except:
        print('Popup \'Like this playlist\' deosn\'t show')

    # get page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # scroll down
    for j in range(5):
        # document.body.scrollHeight : 페이지 세로 길이
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    # get page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # append link, song title, singer to each list
    for k in range(len(soup.find_all('a', class_='trackItem__trackTitle'))):
        top50[genre]['link'].append(soup.find_all(
            'a', class_='trackItem__trackTitle')[k]['href'])
        top50[genre]['songTitle'].append(soup.find_all(
            'a', class_='trackItem__trackTitle')[k].text)
        top50[genre]['singer'].append(soup.find_all(
            'a', class_='trackItem__username')[k].text)

    # print how many links collected
    print(str(len(top50[genre]['link'])) +
          " link, songtitle and singer of songs in [" + genre + "] collected")

    # click download button if present
    for m, link in enumerate(top50[genre]['link']):
        link_base = 'https://soundcloud.com/'
        link_song = link_base + link
        print(link_song)
        print('\'' + top50[genre]['songTitle'][m] + '\'' + ' is in progress')

        driver.get(link_song)
        time.sleep(2)
        driver.find_element_by_css_selector(
            'button.sc-button-more.sc-button.sc-button-medium.sc-button-responsive').click()

        try:
            driver.find_element_by_css_selector(
                'button.sc-button-download').click()
            top50[genre]['cnt_download'] += 1
            print('----------- \'' + top50[genre]['songTitle'][m] + '\'' +
                  ' is downloaded -----------' + ' cnt_download: ' + str(top50[genre]['cnt_download']))
            print('')
        except:
            print('No download button')
            print('')
            
# print result
for genre in top50:
    print('song downloaded in [' + genre + ']: ' + str(top50[genre]['cnt_download']))
    
# newHot
for i, genre in enumerate(newHot):
    # conncet genre url
    driver.get(newHot[genre]['url'])

    # clear popup
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/button').click()
        print('Popup cleared')
    except:
        print('Popup \'Like this playlist\' deosn\'t show')

    # get page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # scroll down
    for j in range(5):
        # document.body.scrollHeight : 페이지 세로 길이
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    # get page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # append link, song title, singer to each list
    for k in range(len(soup.find_all('a', class_='trackItem__trackTitle'))):
        newHot[genre]['link'].append(soup.find_all(
            'a', class_='trackItem__trackTitle')[k]['href'])
        newHot[genre]['songTitle'].append(soup.find_all(
            'a', class_='trackItem__trackTitle')[k].text)
        newHot[genre]['singer'].append(soup.find_all(
            'a', class_='trackItem__username')[k].text)

    # print how many links collected
    print(str(len(newHot[genre]['link'])) +
          " link, songtitle and singer of songs in [" + genre + "] collected")

    # click download button if present
    for m, link in enumerate(newHot[genre]['link']):
        link_base = 'https://soundcloud.com/'
        link_song = link_base + link
        print(link_song)
        print('\'' + newHot[genre]['songTitle'][m] + '\'' + ' is in progress')

        driver.get(link_song)
        time.sleep(2)
        driver.find_element_by_css_selector(
            'button.sc-button-more.sc-button.sc-button-medium.sc-button-responsive').click()

        try:
            driver.find_element_by_css_selector(
                'button.sc-button-download').click()
            newHot[genre]['cnt_download'] += 1
            print('----------- \'' + newHot[genre]['songTitle'][m] + '\'' +
                  ' is downloaded -----------' + ' cnt_download: ' + str(newHot[genre]['cnt_download']))
            print('')
        except:
            print('No download button')
            print('')
            
# print result
for genre in newHot:
    print('song downloaded in [' + genre + ']: ' + str(newHot[genre]['cnt_download']))

# to do
# 1. 로그인 부분,,, 자동으로 할 수 있으면 해야 함
