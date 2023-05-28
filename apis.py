from abc import ABC, abstractmethod



class ApiBase(ABC):

    @abstractmethod
    def get_page(self):
        """Метод для получения ответа от апи с соответствующими параметрами"""
        pass
