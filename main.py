import game
from draw import PrinError, PrintInputValue, PrintMatrix, PrintP
import numpy as np
from os import system
from colorama import Cursor
        

def main():
    system('cls')

    pe = PrinError(pos=(1, 3))
    piv = PrintInputValue(print_error=pe, pos=(1, 1))

    lines = int(piv('Количество строк: '))
    columns = int(piv('Количество столбцов: '))

    system('cls')

    a = np.zeros((lines, columns), dtype=np.float64)
    p = np.zeros(columns, dtype=np.float64)

    pe = PrinError(pos=(1, lines * 2 + 5))
    piv = PrintInputValue(print_error=pe, pos=(1, lines * 2 + 3))
    pm = PrintMatrix(pos=(3, 1))
    pp = PrintP(text='p:', pos=(1, lines * 2 + 1))

    for i in range(lines):
        for j in range(columns):
            pm(a, paint=[(i , j)])
            pp(p, col_len=PrintMatrix.get_columns_len(a))
            a[i][j] = piv(f'Значение {i + 1} строки {j + 1} столбца: ')
            piv.erase()

    pm(a, paint=(None, None))

    for i in range(columns):
        pp(p, col_len=PrintMatrix.get_columns_len(a), paint=i)
        p[i] = piv(f'Значение вероятности {i + 1} исхода: ')
        piv.erase()
    
    alpha = piv(f'Значение альфа для критерия Гурвица: ')

    pp(p, col_len=PrintMatrix.get_columns_len(a))

    criterions = [(game.max_min_criterion(a), 'Пессимизм'),
                  (game.max_max_criterion(a), 'Оптимизм'),
                  (game.hurwitz_criterion(a, alpha), 'Гурвиц'),
                  (game.laplace_criterion(a), 'Лаплас',),
                  (game.savage_criterion(a),  'Сэвидж'),
                  (game.bayes_criterion(a, p),'Байес')]

    criterion = np.array([i[0][0] for i in criterions]).T

    pos_x = sum([i + 5 for i in PrintMatrix.get_columns_len(a)]) + 3

    paint = [(v[0][1], i) for i, v in enumerate(criterions)]

    criterion_name = [i[1] for i in criterions]

    PrintMatrix(pos=(pos_x, 1))(criterion, paint=paint)
    PrintP(pos=(pos_x, lines * 2 + 1))(criterion_name, col_len=PrintMatrix.get_columns_len(criterion))
    
    input()


if __name__ == '__main__':
    main()
