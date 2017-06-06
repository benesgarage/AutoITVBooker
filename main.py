import http.client as httpclient
from pprint import pprint
from StationGetter import StationGetter
from tkinter import *


class Main:
    def __init__(self):
        self.__set_base_url(base_url='www.serviciositv.es')

    def exec(self):
        connection_handle = httpclient.HTTPConnection(self.base_url)
        station_getter = StationGetter(connection_handle, self.base_url)
        stations = station_getter.get_all_stations()

        pprint(stations)

    def __set_base_url(self, base_url):
        self.base_url = base_url


main = Main()
main.exec()
