from service.reader import Reader
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path', '-p', type=str, required=True, help="location folder want to trasnlate")
    args = parser.parse_args()
    
    reader = Reader(path=args.path)
    reader.reader_folder()
    