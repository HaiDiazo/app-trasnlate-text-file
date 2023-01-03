from loguru import logger
from service.translate_service import TranslateApp
from os import listdir

if __name__ == "__main__":
    path = "C:/Users/eBdesk/Documents/_NotWork/translate-app-srt/test/test-txt"
    for file in listdir(path):
        with open(f"{path}/{file}", 'r', encoding="utf8", newline='') as file_name:
            read = file_name.readlines()
            trans_text = TranslateApp(read_text=read)

            result_list = trans_text.iteration_reader()
            for result in result_list:
                logger.info(result.text)