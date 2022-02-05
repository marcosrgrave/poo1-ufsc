class Matrix:

    def __init__(self) -> None:
        
        self.line   = 0
        self.column = 0
        
        self.main_diagonal : bool = self.line == self.column
        self.above_main_diagonal : bool = self.line < self.column
        self.below_main_diagonal : bool = self.line > self.column
        
        self.secundary_diagonal : bool = self.line == 11 - self.column
        self.above_secundary_diagonal : bool = self.line < 11 - self.column
        self.below_secundary_diagonal : bool = self.line > 11 - self.column

    def diagonal_exercises(self, logic):

        operation : str = input()
        soma : float = 0
        i : int = 0
        for line in range(0, 12):
            self.line = line
            for column in range(0, 12):
                self.column = column
                value : float = float(input())
                if logic:  # <- A logica vem aqui. Ex: above_secundary_diagonal and below_main_diagonal
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


logic = Matrix().above_secundary_diagonal
Matrix().diagonal_exercises(logic)