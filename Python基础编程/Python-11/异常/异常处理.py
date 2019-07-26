try:
    print("可能产生异常的代码")
except (KeyError,ErrorName-2,ErrorName-3....,ErrorName-n):
    print("捕获异常后的处理")
except Exception:
    print("如果使用了Exception，name意味着只要上面的except没有捕获到异常，这个except一定会捕获到")
else:
    print("没有异常才执行的功能，但凡有一个异常，这条代码永远不会被执行")
finally:
    print("无论什么情况下总是会执行的代码")
