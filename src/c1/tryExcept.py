def nothing():
    pass


try:
    v = 3 / 0
    print(v)
except Exception as e:
    print(e)

nothing()
