setImmediate(function() {                
    Java.perform(function(){  
        console.log("[*] Starting script --console");

        var utils = Java.use("com.yitong.mbank.util.security.CryptoUtil");
        var clazz = Java.use("java.lang.Class");
        var Exception = Java.use("java.lang.Exception");
        var ThrowableCls = Java.use("java.lang.Throwable");

        // hook 普通方法
        utils.encryptDataWithSM.overload("android.app.Application","java.lang.String","java.lang.String").implementation = function(a,b,c){
        //utils.encryptDataWithSM.implementation = function(a,b,c){
            //打印一下是否hook成功
            console.log("成功_hook");
            // 获取方法的参数
            console.log("b=" + b);
            console.log("c=" + c);
            //打印堆栈信息
            var StackTrace = ThrowableCls.$new().getStackTrace()
            for (var stack in StackTrace){
                console.log(StackTrace[stack]);
            }
            console.log("返回值=" + this.encryptDataWithSM(a,b,c));
            return this.encryptDataWithSM(a,b,c);
        };
    }); 
}); 