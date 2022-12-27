from colorama import Cursor, Style, Fore
from functools import reduce
import numpy as np


class PrintMatrix:
    def __init__(self, pos: tuple = (0, 0), round: int = 2) -> None:
        self.pos = pos
        self.round = round

    def print(self, a: np.array, paint: list = []) -> None:
        col_len = self.get_columns_len(a)
        m = ''
        for i, vi in enumerate(a):
            m += Cursor.POS(self.pos[0], self.pos[1] + 2 * i)
            for j, vj in enumerate(vi):
                if (i, j) not in paint:
                    m += Style.DIM
                m += f'%{col_len[j] + self.round + 3}.{self.round}f' % vj
                if (i, j) not in paint:
                    m += Style.RESET_ALL
            m += '\n\n'
        print(m)
    
    def __call__(self, a: np.array, paint: tuple = None) -> None:
        self.print(a, paint=paint)
    
    @staticmethod
    def get_columns_len(a: np.array):
        return [max(map(lambda x: len(str(int(x))), i)) for i in a.transpose()]


class PrinError:
    def __init__(self, pos: tuple = (0, 0)) -> None:
        self.pos = pos
        self.text = ''

    def print(self, text: str) -> None:   
        self.text = Cursor.POS(*self.pos) + 'Ошибка: ' + text
        print(Fore.RED + self.text + Fore.RESET)

    def __call__(self, text: str) -> None:
        self.print(text=text)
    
    def erase(self) -> None:        
        print(Cursor.POS(*self.pos) + ' ' * len(self.text))


class PrintInputValue:
    def __init__(self, pos: tuple = (0, 0), print_error:PrinError = PrinError()) -> None:
        self.pos = pos
        self.input_text = ''
        self.print_error = print_error

    def print(self, text) -> float:
        while True:
            self.text = text
            self.input_text = input(Cursor.POS(*self.pos) + self.text)
            self.print_error.erase()
            v = self.input_text.replace(' ', '')
            if v == '':
                return 0.
            try:
                if v.find('/') >= 0:
                    v = reduce(lambda x, y: x / y, map(float, v.split('/')))
                return float(v)
            except:
                self.erase()
                self.print_error('лишний символ в введеной строке')
    
    def __call__(self, text: str) -> float:
        return self.print(text)

    def erase(self) -> None:
        print(Cursor.POS(*self.pos) + ' ' * (len(self.text) + len(self.input_text)))


class PrintP:
    def __init__(self, text='', pos: tuple = (0, 0), round: int = 2) -> None:
        self.pos = pos
        self.round = round
        self.text = text

    def print(self, a: np.array, paint: int = None, col_len: list = []) -> None:    
        if not col_len:
            col_len = list(map(lambda x: round(x) if type(x) is np.float64 else len(x), a))

        m = Cursor.POS(*self.pos) + self.text
        for i, vi in enumerate(a):
            if i != paint:
                m += Style.DIM
            if type(vi) is np.float64:
                m += f'%{col_len[i] + self.round + 3}.{self.round}f' % vi
            else:
                m += f'%{col_len[i] + self.round + 3}s' % vi[:col_len[i] + self.round + 1]
            if i != paint:
                m += Style.RESET_ALL

        print(m)
    
    def __call__(self, a: np.array, paint: int = None, col_len: list = []) -> None:
        self.print(a, paint=paint, col_len=col_len)
