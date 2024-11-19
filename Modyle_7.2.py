def custom_write(_file_name, _strings):
    string_positions = {}
    _file_name = 'test.txt'
    _file_name = open(_file_name, 'w', encoding='utf-8')
    for line_num, string in enumerate(_strings, start=1):
        byte_ = _file_name.tell()
        _file_name.write(string + '\n')
        string_positions[(line_num, byte_)] = string
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
