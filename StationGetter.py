from bs4 import BeautifulSoup
from RegionFactory import *
from StationFactory import *


class StationGetter:
    def __init__(self, connection_handle,base_url):
        self.connectionHandle = connection_handle
        self.base_url = base_url

    def get_all_stations(self):
        self.connectionHandle.request('GET', '/es/cita-previa-itv')
        response = self.connectionHandle.getresponse()
        soup = BeautifulSoup(response.read(), 'html.parser')
        soup = soup.find('ul', {"class": "tb-megamenu-subnav mega-nav level-1 items-8"})
        extracted_data = soup.find_all('li', {"data-level": "2"})
        region_collection = RegionCollection()
        for data in extracted_data:
            region = self.build_region(data.find('a', {"class": "dropdown-toggle"}))
            station_collection = region.get_station_collection()
            stations_data = data.find_all('a', {"class": None})
            for station_data in stations_data:
                station_collection.add_station(station=self.build_station(station_data))
            region_collection.add_region(region)
        return region_collection

    def build_region(self, data):
        return Region(
            name=data.text.strip(),
            link=self.base_url + data['href']
        )

    def build_station(self, data):
        return Station(
            name=data.text.strip(),
            link=self.base_url + data['href']
        )
