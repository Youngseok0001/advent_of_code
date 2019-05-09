import re 

def parse(input_dir):
    raws = open(input_dir).read().split("\n\n\n")[1]
    raws =  open(input_dir).read().split("\n\n")
    raws = [raw.split("\n") for raw in raws]
    raws = [[[re.findall("[0-9]",r)][0] for r in raw] for raw in raws]
    raws = [[[int(i) for i in r]for r in raw] for raw in raws]

    outs = []
    for raw in raws:
        out = []
        for r in raw:
            if len(r) > 4:
                out.append([int(str(r[0]) + str(r[1]))] + r[2:])
            else:
                out.append(r)
        outs.append(out) 

    return outs

input_dir = "../data/day16.txt"
inputs = parse(input_dir)[:-2]

class operations:

    def __init__(self, register, operation):
        self.register = register 
        self.operation = operation
        self.op_result = None

    @property
    def addr(self):
        self.op_result = self.register[self.operation[1]] + self.register[self.operation[2]]
        return self
    @property
    def addi(self):
        self.op_result = self.register[self.operation[1]] + self.operation[2]
        return self
    @property
    def mulr(self):
        self.op_result = self.register[self.operation[1]] * self.register[self.operation[2]]
        return self
    @property
    def muli(self):
        self.op_result = self.register[self.operation[1]] * self.operation[2]
        return self
    @property
    def banr(self):
        self.op_result = self.register[self.operation[1]] & self.register[self.operation[2]]
        return self
    @property
    def bani(self):
        self.op_result = self.register[self.operation[1]] & self.operation[2]
        return self 
    @property
    def borr(self):
        self.op_result = self.register[self.operation[1]] | self.register[self.operation[2]]
        return self
    @property
    def bori(self):
        self.op_result = self.register[self.operation[1]] | self.operation[2]
        return self        
    @property
    def setr(self):
        self.op_result = self.register[self.operation[1]]
        return self
    @property
    def seti(self):
        self.op_result = self.operation[1]
        return self        
    @property
    def gtir(self):
        self.op_result = int(self.operation[1] > self.register[self.operation[2]])
        return self
    @property
    def gtri(self):
        self.op_result = int(self.register[self.operation[1]] > self.operation[2])
        return self      
    @property
    def gtrr(self):
        self.op_result = int(self.register[self.operation[1]] > self.register[self.operation[2]])
        return self    
    @property
    def eqir(self):
        self.op_result = int(self.operation[1] == self.register[self.operation[2]])
        return self
    @property
    def eqri(self):
        self.op_result = int(self.register[self.operation[1]] == self.operation[2])
        return self      
    @property
    def eqrr(self):
        self.op_result = int(self.register[self.operation[1]] == self.register[self.operation[2]])
        return self          


def compare(input):
    print(input)

    desired_result = input[2]
    
    operation_list = ["op.addi","op.addr","op.mulr","op.muli","op.banr","op.bani","op.borr",
                      "op.bori","op.setr","op.seti","op.gtir","op.gtri","op.gtrr","op.eqir",
                      "op.eqri","op.eqrr"]

    results = []
    for o in operation_list:
        op = operations(input[0], input[1])
        update = eval(o).op_result
        temp = input[0].copy()
        temp[input[1][3]] = update
        #print(o + ":"+ str(temp))
        results.append(temp)

    n_identical = sum([1 for result in results  if result == desired_result])
    #print(n_identical)
    if n_identical >=  3: return 1 
    else: return 0

#input = [[2, 1, 3, 3], [12, 1, 3, 1], [2, 0, 3, 3]]
#print(compare(input))
print(sum([compare(input) for input in inputs]))
#print(inputs[-3])
