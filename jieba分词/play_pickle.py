import pickle

class A:

    def __init__(self):
        self.s=3

    def add(self):
        self.s+=2


a=A()

a.add()

result=pickle.dumps(a)
print(result)
aa=pickle.loads(result)
print(aa.s
      )

