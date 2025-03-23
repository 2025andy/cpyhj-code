import tkinter as tk
from tkinter import messagebox
import random

def main_page(root1):
    root = root1
    root.geometry("400x500")
    root.title("彩票摇号机 V0.0.1")

    page = tk.Frame(root)

    def show_menu():
        frame_5 = tk.Frame(root)

        label_5 = tk.Label(frame_5, text="1 2 3 4 5", font=50)
        label_5.pack(padx=10, pady=10)
        def random_5():
            number = [0,1,2,3,4,5,6,7,8,9]
            r_5_1 = random.choice(number)
            r_5_2 = random.choice(number)
            r_5_3 = random.choice(number)
            r_5_4 = random.choice(number)
            r_5_5 = random.choice(number)

            r_5_1 = str(r_5_1)
            r_5_2 = str(r_5_2)
            r_5_3 = str(r_5_3)
            r_5_4 = str(r_5_4)
            r_5_5 = str(r_5_5)

            random_new_5 = r_5_1 + " " + r_5_2 + " " + r_5_3 + " " + r_5_4 + " " + r_5_5

            label_5.config(text=random_new_5)
        
        button_5_go = tk.Button(frame_5, text="开始", command=random_5, padx=5, pady=5)
        button_5_go.pack(padx=20, pady=20)

        frame_4 = tk.Frame(root)

        label_4 = tk.Label(frame_4, text="1 2 3 4", font=50)
        label_4.pack(padx=10, pady=10)
        def random_4():
            number = [0,1,2,3,4,5,6,7,8,9]
            r_4_1 = random.choice(number)
            r_4_2 = random.choice(number)
            r_4_3 = random.choice(number)
            r_4_4 = random.choice(number)

            r_4_1 = str(r_4_1)
            r_4_2 = str(r_4_2)
            r_4_3 = str(r_4_3)
            r_4_4 = str(r_4_4)

            random_new_4= r_4_1 + " " + r_4_2 + " " + r_4_3 + " " + r_4_4

            label_4.config(text=random_new_4)
        
        button_4_go = tk.Button(frame_4, text="开始", command=random_4, padx=5, pady=5)
        button_4_go.pack(padx=20, pady=20)

        frame_3 = tk.Frame(root)

        label_3 = tk.Label(frame_3, text="1 2 3", font=50)
        label_3.pack(padx=10, pady=10)
        def random_3():
            number = [0,1,2,3,4,5,6,7,8,9]
            r_3_1 = random.choice(number)
            r_3_2 = random.choice(number)
            r_3_3 = random.choice(number)

            r_3_1 = str(r_3_1)
            r_3_2 = str(r_3_2)
            r_3_3 = str(r_3_3)

            random_new_3 = r_3_1 + " " + r_3_2 + " " + r_3_3

            label_3.config(text=random_new_3)
        
        button_3_go = tk.Button(frame_3, text="开始", command=random_3, padx=5, pady=5)
        button_3_go.pack(padx=20, pady=20)

        frame_51 = tk.Frame(root)

        label_t_51 = tk.Label(frame_51, text="      前区              后区", font=30)
        label_t_51.pack()
        label_51 = tk.Label(frame_51, text="1   2   3   4   5   +   6   7", font=70)
        label_51.pack()

        def random_51():
            number_f_51 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
            number_b_51 = [1,2,3,4,5,6,7,8,9,10,11,12]
            number_f_c_51 = number_f_51.copy()
            number_b_c_51 = number_b_51.copy()

            r_51_1 = random.choice(number_f_c_51)
            number_f_c_51.remove(r_51_1)
            r_51_2 = random.choice(number_f_c_51)
            number_f_c_51.remove(r_51_2)
            r_51_3 = random.choice(number_f_c_51)
            number_f_c_51.remove(r_51_3)
            r_51_4 = random.choice(number_f_c_51)
            number_f_c_51.remove(r_51_4)
            r_51_5 = random.choice(number_f_c_51)
            number_f_c_51.remove(r_51_5)

            r_51_6 = random.choice(number_b_c_51)
            number_b_c_51.remove(r_51_6)
            r_51_7 = random.choice(number_b_c_51)
            number_b_c_51.remove(r_51_7)

            r_51_1 = str(r_51_1)
            r_51_2 = str(r_51_2)
            r_51_3 = str(r_51_3)
            r_51_4 = str(r_51_4)
            r_51_5 = str(r_51_5)
            r_51_6 = str(r_51_6)
            r_51_7 = str(r_51_7)

            number_new_51 = r_51_1 + "   " + r_51_2 + "   " + r_51_3 + "   " + r_51_4 + "   " + r_51_5 + "   +   " + r_51_6 + "   " + r_51_7
            label_51.config(text=number_new_51)

        button_51_go = tk.Button(frame_51, text="开始", padx=5, pady=5, command=random_51)
        button_51_go.pack(padx=20, pady=20)

        frame_61 = tk.Frame(root)
        label_t_61 = tk.Label(frame_61, text="          红球              蓝球", font=30)
        label_t_61.pack()
        label_61 = tk.Label(frame_61, text="1   2   3   4   5   6   +   7", font=70)
        label_61.pack()

        def random_61():
            number_f_61 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
            number_b_61 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            number_f_c_61 = number_f_61.copy()
            number_b_c_61 = number_b_61.copy()
            r_61_1 = random.choice(number_f_c_61)
            number_f_c_61.remove(r_61_1)
            r_61_2 = random.choice(number_f_c_61)
            number_f_c_61.remove(r_61_2)
            r_61_3 = random.choice(number_f_c_61)
            number_f_c_61.remove(r_61_3)
            r_61_4 = random.choice(number_f_c_61)
            number_f_c_61.remove(r_61_4)
            r_61_5 = random.choice(number_f_c_61)
            number_f_c_61.remove(r_61_5)
            r_61_6 = random.choice(number_f_c_61)
            number_f_c_61.remove(r_61_6)

            r_61_7 = random.choice(number_b_c_61)
            number_b_c_61.remove(r_61_7)

            r_61_1 = str(r_61_1)
            r_61_2 = str(r_61_2)
            r_61_3 = str(r_61_3)
            r_61_4 = str(r_61_4)
            r_61_5 = str(r_61_5)
            r_61_6 = str(r_61_6)
            r_61_7 = str(r_61_7)
            number_new_61 = r_61_1 + "   " + r_61_2 + "   " + r_61_3 + "   " + r_61_4 + "   " + r_61_5 + "   " + r_61_6 + "   +   " + r_61_7
            label_61.config(text=number_new_61)

        button_61_go = tk.Button(frame_61, text="开始", padx=5, pady=5, command=random_61)
        button_61_go.pack(padx=20, pady=20)

        frame_bug = tk.Frame(root)
        label_bug1 = tk.Label(frame_bug, text="联系作者：")
        label_bug1.pack()
        label_bug2 = tk.Label(frame_bug, text="B站个人空间（私信）：https://space.bilibili.com/333647139")
        label_bug2.pack()
        def show_5():
            frame_3.pack_forget()
            frame_51.pack_forget()
            frame_4.pack_forget()
            frame_61.pack_forget()
            frame_bug.pack_forget()
            frame_5.pack()

        def show_4():
            frame_3.pack_forget()
            frame_5.pack_forget()
            frame_51.pack_forget()
            frame_61.pack_forget()
            frame_bug.pack_forget()
            frame_4.pack()
        def show_3():
            frame_51.pack_forget()
            frame_5.pack_forget()
            frame_4.pack_forget()
            frame_61.pack_forget()
            frame_bug.pack_forget()
            frame_3.pack()

        def show_51():
            frame_3.pack_forget()
            frame_5.pack_forget()
            frame_4.pack_forget()
            frame_61.pack_forget()
            frame_bug.pack_forget()
            frame_51.pack()

        def show_61():
            frame_3.pack_forget()
            frame_4.pack_forget()
            frame_5.pack_forget()
            frame_51.pack_forget()
            frame_bug.pack_forget()
            frame_61.pack()

        def exit_APP():
            yn_exit = messagebox.askyesno(title=">>>警告<<<", message="你真的要退出应用吗？")
            if yn_exit:
                root.quit()

        def show_bug():
            frame_3.pack_forget()
            frame_4.pack_forget()
            frame_5.pack_forget()
            frame_51.pack_forget()
            frame_61.pack_forget()
            frame_bug.pack()
        menu_bar = tk.Menu(page)
        menu_bar.add_command(label="排列五", command=show_5)
        menu_bar.add_command(label="排列四", command=show_4)
        menu_bar.add_command(label="排列三", command=show_3)
        menu_bar.add_command(label="大乐透（5+2）", command=show_51)
        menu_bar.add_command(label="双色球（6+1）", command=show_61)
        menu_bar.add_command(label="退出", command=exit_APP)
        menu_bar.add_command(label="bug（错误）反馈", command=show_bug)
        root["menu"] = menu_bar

    show_menu()

    root.mainloop()

if __name__ == "__main__":
    root1 = tk.Tk()
    main_page(root1)