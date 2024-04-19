

class Stack:

    def __init__(self, instr):
        self.instr = instr
        self.dict_open = {'{': '}', '[': ']', '(': ')'}
        self.dict_close = {'}': '{', ']': '[', ')': '('}
        self.stack_list = []

    def is_empty(self):
        return self.size() == 0

    def push(self, symbol_str: str):
        self.stack_list.insert(0, symbol_str)

    def pop(self):
        symbol_str = self.stack_list[0]
        self.stack_list = self.stack_list[1:]
        return symbol_str

    def peek(self):
        return self.stack_list[0]

    def size(self):
        return len(self.stack_list)

    def check(self) -> str:
        for symb in self.instr:

            # Если первый символ - уже закрытие скобок
            if self.is_empty() and symb in self.dict_close.keys():
                self.push(symb)
                break

            # Если символ открытия скобок, добавляем в стэк
            if symb in self.dict_open.keys():
                self.push(symb)
            else: # Начинаем считать правильное закрытие скобок
                if self.dict_close.get(symb) == self.peek():
                    self.pop()
                else:
                    break

        # Если стэк пустой то сбалансированно
        if self.is_empty():
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'