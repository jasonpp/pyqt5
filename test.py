

m = 0 # 全局变量
def mm():

    for i in range(0,1):
        m = 1 # 局部变量
        print(m)

def nn():
    print(m)


if __name__ == '__main__':
    mm()
    nn()