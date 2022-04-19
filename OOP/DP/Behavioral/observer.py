from collections import defaultdict
from typing import List, Dict
from abc import ABCMeta, abstractmethod


class EventManager:

    _EventTypes = (
        "Goal", "Faul", "YellowCart", "RedCart"
    )

    def __init__(self) -> None:
        self.__listener : Dict[str, List["EventListener"]]= defaultdict(list)
    
    def subscribe(self, event_type, listener: "EventListener"):
        if event_type not in EventManager._EventTypes:
            raise Exception("Shalgham hamchin eventi nadarim")
        else:
            self.__listener[event_type].append(listener)

    def unsubscribe(self, event_type, listener: "EventListener"):
        if event_type not in EventManager._EventTypes:
            raise Exception("Shalgham hamchin eventi nadarim")
        elif not isinstance(listener, EventListener):
            raise Exception("Shalgham hamchin listeneri nadarim")
        else:
            try:
                self.__listener[event_type].remove(listener)
            except ValueError:
                pass

    def notify(self, event_type, data):
        for listener in self.__listener[event_type]:
            listener.inform(data)


class EventListener(metaclass=ABCMeta):

    @abstractmethod
    def inform(self, message):
        pass


class TVSportNews(EventListener):
    def __init__(self, name) -> None:
        self.name = name

    def inform(self, message):
        print(f"{message} dar TV --- {self.name}")


class RadioSportNews(EventListener):
    def __init__(self, name) -> None:
        self.name = name

    def inform(self, message):
        print(f"{message} dar Radio --- {self.name}")


if __name__ == "__main__":
    footbal_manager = EventManager()

    tv_iran = TVSportNews("tv_iran")
    tv_tehran = TVSportNews("tv_tehran")
    radio_varzesh = RadioSportNews("radio_varzesh")

    footbal_manager.subscribe("Goal", tv_iran)
    footbal_manager.subscribe("RedCart", tv_tehran)

    footbal_manager.subscribe("Goal", radio_varzesh)

    footbal_manager.notify("Goal", "Ali Daei 80 goal be maldiv zad")

    footbal_manager.unsubscribe("Goal", tv_iran)

    footbal_manager.notify("Goal", "Estili ye goal zad be america")
