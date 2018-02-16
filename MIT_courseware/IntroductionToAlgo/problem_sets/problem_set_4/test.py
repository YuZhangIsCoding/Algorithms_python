def test():
    for i in range(10):
        yield i

for i, item in enumerate(test()):
    print i, item
