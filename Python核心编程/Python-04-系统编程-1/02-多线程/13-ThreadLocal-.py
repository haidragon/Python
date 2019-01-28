import threading

#local_student = threading.local()
student = ""
def process_student():
    #获取当前线程关联的student
    #std = local_student.student
    global student
    std = student
    print("Hello, %s (in %s)"%(std,threading.current_thread().name))

def process_thread(name):
    #local_student.student = name
    global student
    student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=("XXXX",),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=("BBBB",),name="Thread-B")

t1.start()
t2.start()


t1.join()
t2.join()