import logging
from abc import ABCMeta, abstractmethod


class BaseController(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.logger = logging.getLogger(name)
    
    @abstractmethod
    def get(self, id:id):
        pass

    @abstractmethod
    def get_all(self, query:dict):
        pass

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def delete(self, id:int):
        pass
