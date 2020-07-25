from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from h_util import *

url_homepage = "https://soundcloud.com/discover"

# modify the chromewebdriver address to execute the code.
driver = webdriver.Chrome(
    "/Users/seongminheo/Desktop/teamproject/soundcloudcrawling/chromedriver")
driver.get(url_homepage)

# login
# cannot find continue with google button
# 수동로그인 -> 해결해야 함

# load file chartList.json
chartList = load_json('chartList.json')

# check if json file is loaded normally
chartList['top50']['allMusic']['url'] != 0

# crawling chartList
for a, chart in enumerate(chartList):
    # crawling of a chart
    for i, genre in enumerate(chartList[chart]):
        # conncet genre url
        driver.get(chartList[chart][genre]['url'])

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

        # scroll five times to the end of the page.
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
            chartList[chart][genre]['link'].append(soup.find_all(
                'a', class_='trackItem__trackTitle')[k]['href'])
            chartList[chart][genre]['songTitle'].append(soup.find_all(
                'a', class_='trackItem__trackTitle')[k].text)
            chartList[chart][genre]['singer'].append(soup.find_all(
                'a', class_='trackItem__username')[k].text)

        # print how many links collected
        print(str(len(chartList[chart][genre]['link'])) +
              " link, songtitle and singer of songs in [" + genre + "] collected")

        # click download button if present
        for m, link in enumerate(chartList[chart][genre]['link']):
            link_base = 'https://soundcloud.com/'
            link_song = link_base + link
            print(link_song)
            print('\'' + chartList[chart][genre]
                  ['songTitle'][m] + '\'' + ' is in progress')

            driver.get(link_song)
            time.sleep(2)
            driver.find_element_by_css_selector(
                'button.sc-button-more.sc-button.sc-button-medium.sc-button-responsive').click()

            try:
                driver.find_element_by_css_selector(
                    'button.sc-button-download').click()
                chartList[chart][genre]['cnt_download'] += 1
                print('----------- \'' + chartList[chart][genre]['songTitle'][m] + '\'' +
                      ' is downloaded -----------' + ' cnt_download: ' + str(chartList[chart][genre]['cnt_download']))
                print('')
            except:
                print('No download button')
                print('')

    # print number of downloaded song for each genre in chart
    for genre in chartList[chart]:
        print('song downloaded in [' + genre + ']: ' +
              str(chartList[chart][genre]['cnt_download']))

# save crawling result as json file named 'crawlingResult.json'
write_json(chartList, 'crawlingResult.json')

# to do
# 1. 로그인 부분,,, 자동으로 할 수 있으면 해야 함
