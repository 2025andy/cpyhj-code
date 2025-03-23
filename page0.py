import tkinter as tk
from tkinter import messagebox
from page1 import first_page

def page_18(root1):
    root = root1
    root.geometry("400x150")
    root.title("彩票摇号机  |  年龄确认")

    frame_18 = tk.Frame(root)
    frame_18.pack()

    def under_18():
        messagebox.showerror(title=">>>警告<<<", message="未满18岁，禁止买彩票！！")
        root.quit()

    button_18_under = tk.Button(frame_18, text="我是18岁以下", padx=5, pady=5, command=under_18)
    button_18_under.grid(row=1, column=1, padx=30, pady=30)

    def on_18():
        messagebox.showerror(title=">>>警告<<<", message="买彩票请理性！禁止青少年买彩票！（重要的事情说三遍）")
        messagebox.showerror(title=">>>警告<<<", message="买彩票请理性！禁止青少年买彩票！（重要的事情说三遍）")
        messagebox.showerror(title=">>>警告<<<", message="买彩票请理性！禁止青少年买彩票！（重要的事情说三遍）")
        frame_18.destroy()
        first_page(root1=root)

    button_18_on = tk.Button(frame_18, text="我是18岁以上", padx=5, pady=5, command=on_18)
    button_18_on.grid(row=1, column=3, padx=30, pady=30)

    label_No_no_yes = tk.Label(frame_18, text="好孩子不能说谎哦~", font=15)
    label_No_no_yes.grid(row=2, column=3, pady=10, padx=10)

    root.mainloop()

if __name__ == "__main__":
    root1 = tk.Tk()
    root = page_18(root1=root1)