from service.translate_service import TranslateApp
from argparse import ArgumentParser
import os

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path', '-p', type=str, required=True, help="location folder want to trasnlate")
    args = parser.parse_args()
    
    path = args.path
    result_path = f"{path}/result"

    for file in os.listdir(path):
        path_find = os.path.join(path, file)

        if not os.path.isdir(path_find):
            with open(f"{path}/{file}", 'r', encoding="utf8", newline='') as file_name:
                read = file_name.readlines()
                trans_text = TranslateApp(read_text=read)
                result_list = trans_text.iteration_reader()
                
                if not os.path.exists(result_path):
                    os.makedirs(result_path)
                
                with open(f"{result_path}/{file}", 'w', encoding="utf-8") as write_file:
                    for result in result_list:
                        if result.text != "{path_break}":
                            write_file.write(f"{result.text} \n")
                        else:
                            write_file.write(result.text.replace("{path_break}", "\n"))
                    write_file.close()