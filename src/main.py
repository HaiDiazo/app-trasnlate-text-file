from googletrans import Translator
from loguru import logger
from os import listdir

if __name__ == "__main__":
    path = "C:/Users/eBdesk/Documents/_NotWork/translate-app-srt/test"
    for file in listdir('C:/Users/eBdesk/Documents/_NotWork/translate-app-srt/test'):
        with open(f"{path}/{file}", 'r', encoding="utf8") as file_name:
            read = file_name.readlines()
            for reader in read: 
                logger.info(read)

    translator = Translator()
    result = translator.translate(text="How much your money?", dest='id')
    logger.info(result.text)
