def fun():
    print("In Fun")


def fun1():
    print("In Fun 1")
    fun2()
    print("Completed fun1")


def fun2():
    print("In Fun 2")
    fun1()
    print("Completed fun2")


fun2()
