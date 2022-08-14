def A(s):
    return 10/int(s)
def B(s):
    return A(s)*2
def main():
    try:
        B('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    else:
        print('try里面正常执行才会被执行')
main()