import os 
from service.translate_service import TranslateApp

class Reader:
    def __init__(self, path: str) -> None:
        self.__path = path
        self.__result_path = f"{path}/result"
    
    def reader_folder(self) -> None:
        for file in os.listdir(self.__path):
            path_find = os.path.join(self.__path, file)

            if not os.path.isdir(path_find):
                with open(f"{self.__path}/{file}", 'r', encoding="utf8", newline='') as file_name:
                    read = file_name.readlines()
                    trans_text = TranslateApp(read_text=read)
                    result_list = trans_text.iteration_reader()
                    
                    if not os.path.exists(self.__result_path):
                        os.makedirs(self.__result_path)
                    self.writer_file(file, result_list)
                    
                    
    def writer_file(self, file, result_list) -> None:
        with open(f"{self.__result_path}/{file}", 'w', encoding="utf-8") as write_file:
            for result in result_list:
                if result.text != "{path_break}":
                    write_file.write(f"{result.text} \n")
                else:
                    write_file.write(result.text.replace("{path_break}", "\n"))
            write_file.close()