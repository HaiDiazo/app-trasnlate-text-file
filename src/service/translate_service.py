from googletrans import Translator
from loguru import logger

class TranslateApp:
    def __init__(self, read_text: list[str]) -> None:
        self.__read_text: list[str] = read_text
        self.__ready_translate: list[str] = []
        self.__result_trasnlate: list = []
        self.trasnlator = Translator()

    
    def iteration_reader(self) -> list:
        for reader in self.__read_text:
            if reader != "\r\n":
                self.__ready_translate.append(reader)
            
            if len(self.__ready_translate) == 4:
                self.__result_trasnlate.extend(self.translate_text())
                self.__ready_translate.clear()
        
        if len(self.__ready_translate):
            self.__result_trasnlate.extend(self.translate_text())
            self.__ready_translate.clear()
        
        return self.__result_trasnlate
    

    def translate_text(self) -> list[str]:
        logger.info(self.__ready_translate)
        result_list = self.trasnlator.translate(
            text=self.__ready_translate, 
            src='en',
            dest='id')
        return result_list