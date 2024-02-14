# Python-based pricing tracking for Amazon products
# Importing Libraries
import bs4 as bs
import sys
import schedule
import time
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import winsound

frequency = 2500  # Decide on a frequency of 2500 Hertz.
Duration = 1000  # Set Duration to 1000 ms, or one second.


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.to
        Html(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def exact_url(url):
    index = url.find("B0")
    index = index + 10
    current_url = ""
    current_url = url[:index]
    return current_url


def mainprogram():
    url = "https://www.amazon.in/Airtel-4G-Hotspot-E5573Cs-609-Portable/dp/B06WV9WR4Z"
    exacturl = exact_url(url)  # main url for extracting data
    page = Page(exacturl)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('span', id='priceblock_ourprice')
    if js_test is None:
        js_test = soup.find('span', id='priceblock_dealprice')
    str = ""
    for line in js_test.stripped_strings:
        str = line
        # converting to integer
    str = str.replace(", ", "")
    current_price = int(float(str))
    your_price = 600
    if current_price < your_price:
        print("Price decreased book now")
        winsound.Beep(frequency, duration)
    else:
        print("Price is still high. Please wait for a better deal.")


def job():
    print("Tracking....")
    main
    program()


# main code
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)