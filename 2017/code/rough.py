from time import time


def timer():
    def wrapper(*args, **kwargs):
        t1 = time()
        out = f(*args, **kwargs)
        t2 = time()
        print("elapse:{}".format(t2 - t1))
        return out
    return wrapper


def ntimes(n):
    def inner(f):
        def wrapper(*args):
            for _ in range(n):
                out = f(*args)
            return out
        return wrapper
    return inner


@ntimes(2)
def add(x, y):
    return x + y


@ntimes(2)
def sub(x, y):
    return x - y


@ntimes(2)
def mul(x, y):
    return x * y


@ntimes(2)
def div(x, y):
    return x / y


# print(add(1, 2))
# print(sub(1, 2))
# print(mul(1, 2))
# print(div(1, 2))


from time import sleep


def compute():

    out = []

    for i in range(10):
        sleep(0.5)
        out.append(i)

    return out


# print(compute())


class compute:

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        out = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        return out


#c = compute()
#print([i for i in c])


def compute():
    i = 0
    while i < 10:
        yield i
        i += 1


#c = compute()
#print([i for i in c])

D = {"c": 100, "Z": 1000}

print(min(zip(D.keys(), D.values())))
