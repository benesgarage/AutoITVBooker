from os import linesep
from StationFactory import StationCollection

class Region:
    def __init__(self, name: str, link: str, station_collection: StationCollection=None):
        self.name = name
        self.link = link
        self.station_collection = station_collection or StationCollection()

    def set_name(self, name: str):
        self.name = name

    def set_link(self, link: str):
        self.link = link

    def set_station_collection(self, station_collection: StationCollection):
        self.station_collection = station_collection

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link

    def get_station_collection(self):
        return self.station_collection

    def __repr__(self):
        return 'Region(name='+self.name+','+linesep+\
               'link='+self.link+','+linesep+\
               'station_collection='+linesep+self.station_collection.__repr__()+\
               ') '


class RegionCollection:

    def __init__(self):
        self.region_collection = []

    def add_region(self, region: Region):
        self.region_collection.append(region)

    def remove_region_by_name(self, name: str):
        for region in self.region_collection:
            if region.get_name() == name:
                self.region_collection.remove(region)

    def remove_region_by_link(self, link: str):
        for region in self.region_collection:
            if region.get_link() == link:
                self.region_collection.remove(region)

    def __repr__(self):
        str = '['+linesep
        for region in self.region_collection:
            str += region.__repr__() + linesep
        str += ']'
        return str
