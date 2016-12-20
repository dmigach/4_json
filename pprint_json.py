import json
import os
import chardet


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    file_content = open(file_path, 'rb').read()
    encoding = chardet.detect(file_content)['encoding']
    with open(file_path, 'r', encoding=encoding) as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_content):
    return json.dumps(json_content, sort_keys=True, indent=4,
                      separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    json_string = load_data(input('Enter file path\n'))
    if json_string is None:
        print('Wrong file path')
    else:
        print(pretty_print_json(json_string))
