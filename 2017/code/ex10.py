from builtins import reversed

#X =  [int(val) for val in open("../data/day10.txt").read().split(",")]
X = [0, 1, 2, 3, 4]

current_pointer = None


class circular_object:

    def  __init__(self, X, pointer):
        self.X = X
        self.pointer = pointer

    def cir_index(self, index):
        return index % len(self.X)

    def divide(self, by):

        subset_1 = self.X[self.pointer : self.cir_index(self.pointer + by)]
        subset_2

        return

    def reverse(self,by):

        left, subset, right = self.divide(by)
        reversed_subset = list(reversed(subset))
        self.X = left + reversed_subset + right


    def move_pointer(self, by):
        self.pointer = self.pointer + by

cr_list = circular_object(X,0)
bys = [ 3, 4, 1, 5]

for by in bys:
    cr_list.reverse(by)
    cr_list.move_pointer(by)

print(cr_list.X)