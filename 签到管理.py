# -*-coding:UTF-8 -*-
import tkinter as tk
from copy import deepcopy
from tkinter import ttk


class Manager:
    def __init__(self, database_route, db_num_route):
        self.db_num_route = db_num_route
        self.num_db = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                       51, 52, 53, 54, 55}
        self.db_route = database_route
        self.db_data = {1: "曾正鑫", 2: "陈思漫", 3: "陈思莹", 4: "陈雅彬", 5: "陈依倩", 6: "陈玉琳", 7: "范淑妮", 8: "洪雨桐", 9: "黄凯",
                        10: "黄堃赫", 11: "黄李福", 12: "黄青云", 13: "季理理", 14: "孔婉妍", 15: "孔宇扬", 16: "赖慧敏", 17: "雷锦宝",
                        18: "李铭", 19: "李想", 20: "林仁杰", 21: "林舒语", 22: "林文钦", 23: "林㦤缘", 24: "林颖洁", 25: "林雨欣", 26: "林毓宣",
                        27: "林子钦", 28: "刘文俊", 29: "陆宇浩", 30: "王桁月", 31: "王铭悦", 32: "王裕丰", 33: "魏陈鸿", 34: "魏志宇",
                        35: "吴鸿昌", 36: "吴钧慧", 37: "吴雯熙", 38: "吴鑫睿", 39: "吴宇鑫", 40: "吴煜婷", 41: "叶鸿伟", 42: "叶铭栋",
                        43: "叶子皓", 44: "游睿臻", 45: "袁征航", 46: "张可欣", 47: "张怡静", 48: "张宇杰", 49: "章华", 50: "章敬轩",
                        51: "章一龙", 52: "郑锋", 53: "郑瑞希", 54: "卓宏海", 55: "邹秀琴"}
        self.tk = tk.Tk()
        self.inited_names = tk.Text(self.tk, height=15, width=40)
        self.inited_names.place(x=300, y=380)
        tk.Label(self.tk, text="已签到").place(x=300, y=355)
        self.tk.geometry("600x600")
        tk.Label(self.tk, text="已签到号数").place(x=0, y=50)
        self.inited_user = tk.Text(self.tk, width=40, height=15)
        self.inited_user.place(x=0, y=140)
        self.unknown_inited_user = tk.Text(self.tk, width=40, height=10)
        self.un_init_user = tk.Text(self.tk, width=40, height=20)
        self.un_init_user.place(x=300, y=70)
        tk.Label(self.tk, text="未签到").place(x=310, y=40)
        tk.Label(self.tk, text="忽略列表").place(x=0, y=360)
        self.unknown_inited_user.place(x=0, y=390)
        ttk.Button(self.tk, command=self.query, text="比对").place(x=0, y=0)
        self.tk.title("柘荣三中七年级六班签到比对系统")
        self.tk.mainloop()

    def query(self):
        temp = []
        inited_user = list(self.inited_user.get(1.0, "end").split(","))
        for x in inited_user:
            temp.append(int(x.replace("\n", "")))
        inited_user = set(temp)
        print(inited_user)
        unknown_user = list(self.unknown_inited_user.get(1.0, "end").split(","))
        temp = []
        for x in unknown_user:
            temp.append(x.replace("\n", ""))
        unknown_user = set(temp)
        print(unknown_user)
        un_init_user = self.num_db - inited_user
        un_init = []
        for x in un_init_user:
            if self.db_data[x] in unknown_user:
                continue
            un_init.append(self.db_data[x])
        un_init = str(un_init)
        self.un_init_user.delete(1.0, "end")
        self.un_init_user.insert("insert", un_init)
        self.inited_names.delete(1.0, "end")
        init_names = []
        for x in inited_user:
            init_names.append(self.db_data[x])
        init_names = repr(init_names)
        self.inited_names.insert("insert", init_names)


def main():
    manager = Manager("Classmates_name.txt", "Classmates.txt")


if __name__ == '__main__':
    main()
