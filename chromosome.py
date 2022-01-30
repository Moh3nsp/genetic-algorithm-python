
class chromosome:
    def __init__(self,posotion,cost_func):
        self.posotion=posotion
        self.cost=0
        self.evalfn=cost_func
        self.evaluate()

    def evaluate(self):
        self.cost=self.evalfn(self.posotion)