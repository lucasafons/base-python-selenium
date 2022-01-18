from enum import Enum

class GOOGLE_URL(Enum):
    def __str__(self): 
        return (self.value)
        
    BASE_URL = "https://www.google.com.br/"

class API_COTACAO_URL(Enum):
    def __str__(self):
        return (self.value)

    BASE_URL = "https://economia.awesomeapi.com.br/last"