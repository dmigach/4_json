import json
import os
import chardet


def load_data(file_path):
    if os.path.exists(file_path):
        file_content = open(file_path, 'rb').read()
        encoding = chardet.detect(file_content)['encoding']
        with open(file_path, 'r', encoding=encoding) as file_handler:
            return json.load(file_handler)
    else:
        raise ValueError('Wrong file path')


def pretty_print_json(json_str):
    return json.dumps(json_str, sort_keys=True, indent=4,
                      separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    try:
        json_string = load_data(input('Enter file path\n'))
        print(pretty_print_json(json_string))
    except ValueError as error:
        raise SystemExit(error)
