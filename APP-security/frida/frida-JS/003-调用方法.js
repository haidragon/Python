setImmediate(function() {                
    Java.perform(function(){  
        console.log("[*] Starting script --console");

        var utils = Java.use("com.example.xiaoming.myapplication.MainActivity");
        var clazz = Java.use("java.lang.Class");
        var Exception = Java.use("java.lang.Exception");
        var ThrowableCls = Java.use("java.lang.Throwable");
        var button = Java.use("android.widget.TextView");

        // hook 普通方法
        utils.onClickNum.implementation = function(v){
        //utils.encryptDataWithSM.implementation = function(a,b,c){
            //打印一下是否hook成功
            console.log("成功_hook");
            // 获取方法的参数
            console.log("参数=" + v);
            //打印堆栈信息
            console.log("========Hook StackTrack Start========");
            var StackTrace = ThrowableCls.$new().getStackTrace()
            for (var stack in StackTrace){
                console.log(StackTrace[stack]);
            }
            console.log("========Hook StackTrack End========");
            //调用Button的getText方法查看点击的是哪个数字
            console.log("========转换参数类型t========");
            //将传入的View类型的参数转换为Button
            var Activity = Java.use('android.widget.Button');
            //Java.cast(需要转换的对象，目标类)
            var b = Java.cast(v,Activity);
            console.log("========调用方法========" + b);
            //获取需要调用的方法
            var func = button.class.getDeclaredMethod("getText",null);
            console.log("    ========>>>调用到的方法=" + func);
            //调用方法，获取返回值:方法.invoke(对象，参数)
            var button_value = func.invoke(b,null);
            console.log("        ========>>>方法返回值=" + button_value);
            return this.onClickNum(v);
        };
    }); 
}); 