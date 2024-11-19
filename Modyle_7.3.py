
class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = list(file_names)

    def get_all_words(self):

        all_words = {}
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()

                    for p in punctuations:
                        text = text.replace(p, ' ')

                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []

        return all_words

    def find(self, word):

        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            try:
                result[name] = words.index(word) + 1
            except ValueError:
                result[name] = None

        return result

    def count(self, word):

        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            result[name] = words.count(word)

        return result


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Найти слово
print(finder2.count('teXT'))  # Подсчитать количество слова
