'''
Реализовать класс BlockTranspositionCipher, который будет шифровать и
расшифровывать текст методом блочной перестановки с помощью текстового
ключа.
Основная идея:

1. Ключ — строка, состоящая из уникальных английских букв. Пример:
acb
2. Шифрование — алгоритм, который преобразует исходный текст в
набор зашифрованных символов.
3. Дешифрование — алгоритм, который преобразует набор
зашифрованных символов в исходный текст.
'''
from string import ascii_lowercase


class BlockTranspositionCipher:

    def __init__(self, text: str, key: str, decrypt: bool = False) -> None:
        self.__key = ""
        self.__text = ""
        self.__position = 0
        self.__splited_data: list[str] = []
        self.__template: list[int] = []
        self.__inverse_template: list[int] = []


        self.key = key
        self.text = text
        self.decrypt = decrypt


    @property
    def text(self) -> str:
        return self.__text


    @text.setter
    def text(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Параметр text должен иметь тип данных str! текущий переданный тип: {type(value)}")
        self.__text = value


    @property
    def key(self) -> str:
        return self.__key


    @key.setter
    def key(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Параметр key должен иметь тип данных str! текущий переданный тип: {type(value)}")

        low = value.lower()
        if any(i not in ascii_lowercase for i in low):
            raise ValueError('Ключ должен состоять только из букв латинского алфавита (a..z)')

        if len(set(low)) != len(low):
            raise ValueError('Ключ должен состоять из уникальных букв латинского алфавита')

        self.__key = low


    @property
    def decrypt(self) -> bool:
        return self.__decrypt


    @decrypt.setter
    def decrypt(self, value: bool) -> None:
        self.__decrypt = bool(value)


    def __iter__(self):
        if not self.__key:
            raise ValueError('Ключ не задан')

        # Разбиваем данные на части длиной len(key)
        self.__splited_data = self.__split_data(self.__text, len(self.__key))

        # Расчитываю порядок при перемешивании кусочка данных
        order = [sorted(self.__key).index(i) for i in self.__key]
        self.__template = [0] * len(self.__key)


        for pos, indx in enumerate(order):
            self.__template[indx] = pos

        self.__inverse_template = [0] * len(self.__template)

        for i, t in enumerate(self.__template):
            self.__inverse_template[t] = i

        self.__position = 0
        return self


    def __next__(self):
        if self.__position >= len(self.__splited_data):
            raise StopIteration

        piece_of_data = self.__splited_data[self.__position]
        self.__position += 1

        template = self.__inverse_template if self.decrypt else self.__template
        res = self.__permit_by_template(data=piece_of_data, template=template)

        if self.decrypt and self.__position == len(self.__splited_data):
            return res.rstrip(' ')

        return res


    @staticmethod
    def __permit_by_template(data: str, template: list[int]) -> str:
        """
        Перемешивает строку data в соответствии с шаблоном template
        Пример:
            - data = 'abc'
            - template = [2, 0, 1]
            => 'cab'

        Args:
            data (str): текст для перемешивания
            template (list[int]): шаблон для перемешивания. Например [1, 3, 2, 0]

        Returns:
            str: перемешанная строка по шаблону
        """
        if len(data) != len(template):
            raise ValueError(f'длина текста data (текущая: {len(data)}) должна совпадать с длиной template (Текущая: {len(template)})')
        res = ''
        for i in template:
            res += data[i]

        return res


    @staticmethod
    def __split_data(data: str, length: int) -> list[str]:
        """
        Разбивает строку на косочки длины равной length и дополняет пробелами, когда длина строки не кратна length

        Args:
            data (str): текст для разбиения
            length (int): длина кусочкок для разбиений

        Returns:
            list[str]: массив, состоящий из разбитых кусочков длиной length
        """
        if length == 0:
               raise ValueError('Ключ не может быть пустым')

        if len(data) % length != 0:
            data = data.ljust(length - (len(data) % length) + len(data), ' ')

        return [data[i:i + length] for i in range(0, len(data), length)]



if __name__ == '__main__':
    text = "HELLOWORLD"
    key = "bAc"
    print("Процесс шифрования по блокам:")
    cipher = BlockTranspositionCipher(text, key)
    for i, encrypted_block in enumerate(cipher, 1):
        print(f"Блок {i}: '{encrypted_block}'")


    cipher = BlockTranspositionCipher(text, key)
    encrypted = ''.join(cipher)
    print(f"\nПолный зашифрованный текст: '{encrypted}'")



    print("\nПроцесс дешифрования по блокам:")
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    for i, decrypted_block in enumerate(decipher, 1):
        print(f"Блок {i}: '{decrypted_block}'")


    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    decrypted = ''.join(decipher)
    print(f"\nПолный расшифрованный текст: '{decrypted}'")


    cipher = BlockTranspositionCipher("abcd", "bca")
    encrypted = ''.join(cipher)
    decipher = BlockTranspositionCipher(encrypted, "bca", decrypt=True)
    print(''.join(decipher))
