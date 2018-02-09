import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student属性
    std = local_school.student
    # 获取当前线程关联的password属性
    password = local_school.password
    print("线程:%s中---name值:%s,password值:%s" % (threading.current_thread(), std, password))

def process_thread(name, password):
    # 为ThreadLocal的实例对象local_school添加了一个student属性
    local_school.student = name
    # 为ThreadLocal的实例对象local_school添加了一个password属性
    local_school.password = password
    process_student()

t1 = threading.Thread(target=process_thread, args=("小明","12345",), name="线程A")
t2 = threading.Thread(target=process_thread, args=("老王","268439",), name="线程B")
t1.start()
t2.start()
t1.join()
t2.join()


