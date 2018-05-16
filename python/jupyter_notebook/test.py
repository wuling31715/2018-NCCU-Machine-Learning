def hello():
    print('Hello World!')

def test():
    a = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                a += 1
    return a
