import frida
import sys

src = """
setImmediate(function() {                
    Java.perform(function(){  
        console.log("[*] Starting script --console");

        var utils = Java.use("com.ecology.view.WelcomeActivity");
        //var coinClass = Java.use("com.ecology.view.WelcomeActivity");
        var clazz = Java.use("java.lang.Class");
        var Exception = Java.use("java.lang.Exception");

        // hook 普通方法
        utils._onCreate.overload("android.os.Bundle").implementation = function(b){
            //打印一下是否hook成功
            console.log("成功_hook");
            // 修改方法的返回值
            //return this.getValue()+"_hook";
            //获取方法的参数
            //var u = arguments[0]
            //console.log(m1+"_hook");
            var u = this.forget_pass.value
            console.log(u+"_hook");
            //调用其他的方法，可以是同一个类的其他方法
            this.openWorkCenter()
            return true
        }
    }); 
}); 
"""

# 列出加载的类
src2 = '''
setImmediate(function() {                
    Java.perform(function(){ 
    Java.enumerateLoadedClasses(
      {
      "onMatch": function(className){ 
            console.log(className) 
        },
      "onComplete":function(){}
      }
    );
    }); 
}); 
'''

# 采用 remote 方式必须进行端口转发  或者使用get_usb_device()
rdev = frida.get_usb_device()
#rdev = frida.get_remote_device()
#session = rdev.attach("com.example.xiaoming")
session = rdev.attach("com.ecology.view")

script = session.create_script(src2)

def on_message(message, data):
    print(message)

script.on("message", on_message)
script.load()
sys.stdin.read()
