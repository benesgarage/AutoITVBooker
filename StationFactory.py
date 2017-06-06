from os import linesep


class Station:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def set_name(self, name):
        self.name = name

    def set_link(self, link):
        self.link = link

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link

    def __repr__(self):
        return 'Station(name=%s, link=%s)' % (self.name, self.link)


class StationCollection:
    def __init__(self):
        self.station_collection = []

    def add_station(self, station: Station):
        self.station_collection.append(station)

    def remove_station_by_name(self, name: str):
        for station in self.station_collection:
            if station.get_name() == name:
                self.station_collection.remove(station)

    def remove_station_by_link(self, link: str):
        for station in self.station_collection:
            if station.get_link() == link:
                self.station_collection.remove(station)

    def __repr__(self):
        str = '['+linesep
        for region in self.station_collection:
            str += region.__repr__() + linesep
        str += ']'
        return str
