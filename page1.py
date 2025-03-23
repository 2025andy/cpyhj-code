import tkinter as tk
from tkinter import messagebox
from page2 import main_page

def first_page(root1):
    root = root1
    root.title("彩票摇号机")
    root.geometry("400x500")

    page = tk.Frame(root)
    page.pack()

    def show_meau():
        frame_about = tk.Frame(root)
        label_about1 = tk.Label(frame_about, text="关于应用：")
        label_about1.pack()
        label_about4 = tk.Label(frame_about, text="应用名称：彩票摇号机")
        label_about4.pack()
        label_about2 = tk.Label(frame_about, text="发布者：向未来天天科技有限公司")
        label_about2.pack()
        label_about3 = tk.Label(frame_about, text="版本：V0.0.1测试版本")
        label_about3.pack()
        label_about4 = tk.Label(frame_about, text="版权所有：所有版权均属向未来天天科技有限公司！")

        def go_y():
            page.destroy()
            frame_about.destroy()
            main_page(root)
        menu_bar = tk.Menu(page)
        menu_bar.add_command(label="摇号", command=go_y)

        def exit_APP():
            yn_exit = messagebox.askyesno(title=">>>警告<<<", message="你真的要退出应用吗？")
            if yn_exit:
                root.quit()

        def about_APP():
            frame_about.pack()

        menu_bar.add_command(label="退出应用", command=exit_APP)
        menu_bar.add_command(label="关于应用", command=about_APP)
        root["menu"] = menu_bar

    show_meau()

    root.mainloop()

if __name__ == "__main__":
    root1 = tk.Tk()
    first_page(root1)