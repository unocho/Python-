import sys
from xmlrpc.client import boolean

import s
import time

from s import Student


class cms():
    ifsave=False
    #构造函数创建学生列表
    def __init__(self):
        self.stu_list=list();

    #菜单
    def menu(self):
        print('————学生管理系统————')
        print('\t1添加学生')
        print('\t2修改学生')
        print('\t3删除学生')
        print('\t4查询学生')
        print('\t5显示全部学生')
        print('\t6保存信息')
        print('\t7加载信息')
        print('\t0退出学生')
        print('———————————————————')

    #添加学生
    def add(self,name=None,age=None):
        temp=s.Student(name,age)
        self.stu_list.append(temp)
        print('添加成功')

    #删除学生
    def drop(self,name):
        for stu in self.stu_list:
            if stu.get_name() == name:
                self.stu_list.remove(stu)
                print('删除成功')
                return True
        print('不存在这个学生，删除失败')
        return False

    #查询学生
    def query(self,name):
        for stu in self.stu_list:
            if stu.get_name()==name:
                print(stu)
                return True

        print('不存在该学生')
        return False

    #修改学生
    def update(self,name,newname,newage):
        for stu in self.stu_list:
            if stu.get_name()==name:
                stu.set_name(newname)
                stu.set_age(newage)
                print('修改成功')
                return True
        print('修改失败')
        return False

    #查询全部学生信息
    def all(self):
        for stu in self.stu_list:
            print(stu)

    #保存信息
    def save(self):
        #保存后文件存储地址
        with open('D:/stu_data.txt','a',encoding='utf-8') as f:
            #把列表套字典
           # stu_dict=[stu.__dict__ for stu in self.stu_list]
            stu_list = list();
            for stu in self.stu_list:
                temp={'name':stu.get_name(),'age':stu.get_age()}
                stu_list.append(temp)
            f.write(str(stu_list))
            f.write('&|fenge|&')
            cms.ifsave=True


    #加载学习
    def load(self):
        try:
            with open('D:/stu_data.txt', 'r', encoding='utf-8') as f:
                stu_data = f.read()
                if (len(stu_data) == 0):
                    self.stu_list = list();

                split_stu = stu_data.split('&|fenge|&')
                new_list = list()
                for stu in split_stu:
                    stu_new = stu.strip()
                    if (len(stu_new) != 0):
                        stu_new1 = eval(stu_new)
                        new_list.append(stu_new1)
                for stu_new in new_list:
                    for new_stu in stu_new:
                        temp = s.Student()
                        temp.set_name(new_stu['name'])
                        temp.set_age(new_stu['age'])
                        self.stu_list.append(temp)
            print('加载成功')
        except FileNotFoundError:
            f=open('D:/stu_data.txt', 'w', encoding='utf-8')
            f.close()
            print('文件不存在，创建默认文件')

    #开始
    def start(self):
        #处理因为提前终止（停止）造成的键盘未输入异常KeyboardInterrupt
        #通常是因为在控制台Ctrl+F2强行提前终止或者运行点击停止按钮。
        try:
            while(True):
                flag=False
                self.menu()
                a=set();
                a={'1','2','3','4','5','6','7','0'}
                chose=input('请输入选择功能:')
                for stu in a:
                    if stu==chose:
                        flag=True
                        match chose:
                            case '1':
                                name=input('请输入学生姓名')
                                age=input('请输入学生年龄')
                                self.add(name,age)
                            case '2':
                                name=input('输入你要修改学生的姓名')
                                if(self.query(name)):
                                    newname=input('新名字')
                                    newage=input('新年龄')
                                    self.update(name,newname,newage)
                            case '3':
                                name=input('请输入要删除学生的姓名')
                                self.drop(name)
                            case '4':
                                name = input('请输入要查询学生的姓名')
                                self.query(name)
                            case '5':
                                self.all()
                            case '6':
                                print('保存中')
                                self.save()
                                print('保存成功！')
                            case '7':
                                self.load()
                            case '0':
                                chose2=input('确认退出嘛？(y/n)')
                                if chose2=='y' or chose2.lower()=='y':
                                    if cms.ifsave == False:
                                        self.save()
                                    sys.exit()
                            case _:
                                print('错误')
                        continue
                if flag==False:
                    print('没有这个选项')
                    continue
        except KeyboardInterrupt:
            if  cms.ifsave==False:
                self.save()
            sys.exit()


