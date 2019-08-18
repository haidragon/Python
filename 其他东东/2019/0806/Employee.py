# 1. 编写一个员工（Employee）类，要求如下：
# 1) 实现构造函数，构造函数必须初始化员工的工号（emp_id）、姓名（emp_name）、学历（emp_edu）默认为本科。
# 1) 实现新增员工函数，将新增员工信息写入文本文件。（员工信息文件格式如下，列之间用制表符\t分隔，注意工号不能重复）
# 2) 实现修改员工函数，根据工号修改员工信息，并将修改后的员工信息写入文件，注意：不能修改工号。
# 3) 实现删除员工函数，根据工号删除员工信息，将员工信息从文件中删除。
# 4) 实现打印所有员工信息函数，按员工KPI考核分数倒序排序，使用表格形式打印。
# 5) 实现打印KPI分数最低员工信息函数。
# 6) 实现打印年龄最大员工信息函数。
# 7) 实现打印所有女员工信息函数。

class Employee():
    #1) 实现构造函数，构造函数必须初始化员工的工号（emp_id）、姓名（emp_name）、学历（emp_edu）默认为本科。
    emp_edu="本科"
    def __init__(self,emp_id,emp_name,emp_birth,emp_sex,emp_kpi):
        #super.__init__(self)
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_birth = emp_birth
        self.emp_sex = emp_sex
        self.emp_kpi = emp_kpi
        self.u_init()

    def u_init(self):
        self.u_map = {}
        self.r = open("employee.db", "r")
        len_r = len(self.r.readlines())
        print("目前已存在%d行数据"%len_r)
        self.r.seek(0)
        if len_r < 1:
            self.u_map["emp_id"] = ["emp_name","emp_birth","emp_edu","emp_sex","emp_kpi","\n"]
            print("写入表头")

        for i in self.r:
            print(i)
            i_list = i.split("\t")
            self.u_map[i_list[0]] = i_list[1:]

        self.w = open("employee.db", "w")


    #1) 实现新增员工函数，将新增员工信息写入文本文件。（员工信息文件格式如下，列之间用制表符\t分隔，注意工号不能重复）
    def u_add(self):
        list2 = []
        list2.append(self.emp_name)
        list2.append(self.emp_edu)
        list2.append(self.emp_birth)
        list2.append(self.emp_sex)
        list2.append(self.emp_kpi)
        list2.append("\n")
        self.u_map[self.emp_id] = list2
        #print(self.u_map)
        self.u_write(self.u_map)

    def u_remove(self):
        self.u_map.pop(self.emp_id)
        self.u_write(self.u_map)

    def u_write(self,u_map):
        str = ""
        for key in u_map:
            str = str + key + "\t" + "\t".join(u_map[key])
        self.w.write(str)
        self.w.flush()

    def u_max_id(self):
        maxId = max([int(x) for x in  self.u_map.keys()])
        maxId += 1
        print("当前id=%d"%maxId)
        return str(maxId)


def main():
    while True:
        try:
            a = int(input("请输入操作类型1-新增/修改、2-删除、3-退出"))
            if a == 1:
                id = input("请输入员工id,若需使用自动递增id请不要输入任何内容直接回车进入下一步")
                if id is "":
                    e = Employee("","","","","")
                    id = e.u_max_id()
                name = input("请输入用户名")
                birth = input("请输入生日：格式YYYY-MM-DD")
                sex = input("请输入性别：男/女")
                kpi = input("请输入KPI")
                employee = Employee(id, name, birth, sex, kpi)
                employee.u_add()
            elif a == 2:
                id = input("请输入需要删除的员工id")
                employee = Employee(id,"","","","")
                employee.u_remove()
            elif a ==3:
                exit(0)
            else:
                print("请输入1-3的数字")
        except Exception as e:
            print("请输入1-3的数字")
            print(e)

if __name__ == "__main__":
    main()