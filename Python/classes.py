class Computer():
    def __init__(self, model, memory):
        self.mo = model
        self.me = memory

c = Computer('Dell', '500gb')

print(c.mo,c.me)