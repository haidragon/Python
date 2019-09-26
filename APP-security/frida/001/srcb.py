import time

import frida
import sys

with open("H:\\坚果云\\我的坚果云\\PycharmProject\\APP-security\\frida\\frida-JS\\002-Hook普通方法.js", "r", encoding="utf-8") as f:
    src = f.read()

# 列出加载的类、部分APP使用时会崩溃
with open("H:\\坚果云\\我的坚果云\\PycharmProject\\APP-security\\frida\\frida-JS\\000-列出加载的类.js", "r", encoding="utf-8") as f:
    src = f.read()

#追踪调用、部分APP使用时会崩溃
with open("H:\\坚果云\\我的坚果云\\PycharmProject\\APP-security\\frida\\frida-JS\\001-追踪调用.js", "r", encoding="utf-8") as f:
    src3 = f.read()

#调用参数的方法
with open("H:\\坚果云\\我的坚果云\\PycharmProject\\APP-security\\frida\\frida-JS\\003-调用方法.js", "r", encoding="utf-8") as f:
    src4 = f.read()


# 采用 remote 方式必须进行端口转发  或者使用get_usb_device()
rdev = frida.get_usb_device()
# rdev = frida.get_remote_device()
#session = rdev.attach("com.example.xiaoming")

#pid = rdev.spawn(["com.srcb.qymbank"])
pid = rdev.spawn(["com.example.xiaoming"])
rdev.resume(pid)
time.sleep(1)

session = rdev.attach(pid)
# session = rdev.attach(15187)

script = session.create_script(src4)


def on_message(message, data):
    print(message)

script.on("message", on_message)
script.load()
sys.stdin.read()
