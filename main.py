class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас в руках {self.title}. Будем рисовать ручкой контур рисунка'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас в руках {self.title}. Будем рисовать карандашом тени по контуру'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас в руках {self.title}. Будем рисовать маркером заполнение цвета контура'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
