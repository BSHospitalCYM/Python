from multiprocessing import Pool, Manager
import os
import time

def copyFileTask(name, oldFolderName, newFolderName, queue):
    fr = open(oldFolderName + "/" + name)
    fw = open(newFolderName + "/" + name, "w")
    
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)
    time.sleep(5)

def main():

    # 0.获取用户要拷贝的文件夹的名字
    oldFolderName = input("请输入要拷贝的文件夹名：")
    # 1.创建一个文件夹
    newFolderName = oldFolderName + "-复件"
    os.mkdir(newFolderName)
    # 2.获取源文件夹中的所有文件名
    fileNames = os.listdir(oldFolderName)
    # 3.使用多进程的方式拷贝源文件夹中的所有文件到新的文件夹中
    pool = Pool(5)
    queue = Manager().Queue()

    for name in fileNames:
        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, queue))
    
    num = 0
    allNum = len(fileNames)
    while True:
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\r复制文件的进度是：%.2f%%" % (copyRate*100), end="")
        if num == allNum:
            print("")
            break
    print("%s文件夹拷贝完成" % oldFolderName)

if __name__ == "__main__":
    main()
