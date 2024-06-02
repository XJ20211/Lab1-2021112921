import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image  # 需要安装Pillow库
import fun
# 导入其它函数和类

# 创建一个窗口
window = tk.Tk()
window.title("Text Graph Analyzer")  # 设置窗口标题
graph = None
# 创建有向图
def create_graph():
    file_path = filedialog.askopenfilename(title="Select a text file")  # 打开文件选择对话框
    if file_path:
        try:
            text = fun.read_text_file(file_path)
            graph = fun.create_directed_graph(text)

            # 重新保存图像以修复iCCP profile问题
            image = Image.open(file_path)
            new_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", ".png")])
            image.save(new_file_path)  # 保存新的图像文件
            fun.show_directed_graph(graph)  # 显示修复后的图像
            messagebox.showinfo("Success", "Directed graph created successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# 查询桥接词
def query_bridge():
    word1 = entry_word1.get()
    word2 = entry_word2.get()
    if word1 and word2:
        try:
            result = fun.query_bridge_words(graph, word1, word2)
            messagebox.showinfo("Bridge Words", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please enter both words.")

# 生成新文本
def generate_text():
    input_text = entry_input_text.get()
    if input_text:
        try:
            result = fun.generate_new_text(graph, input_text)
            fun.entry_generated_text.delete(0, tk.END)
            fun.entry_generated_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please enter a line of text.")

# 计算最短路径
def shortest_path():
    word1 = entry_word1_path.get()
    word2 = entry_word2_path.get()
    if word1 and word2:
        try:
            result = fun.calc_shortest_path(graph, word1, word2)
            messagebox.showinfo("Shortest Path", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please enter both words.")

# 随机行走
def random_walk():
    try:
        result = random_walk(graph)
        messagebox.showinfo("Random Walk", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# 创建菜单栏
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Create Graph", command=create_graph)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# 创建GUI元素
# 创建有向图
frame_create = tk.Frame(window)
frame_create.pack(pady=10)
btn_create = tk.Button(frame_create, text="Create Graph", command=create_graph)
btn_create.pack(side=tk.LEFT)
# 查询桥接词
frame_query = tk.Frame(window)
frame_query.pack(pady=10)
label_word1 = tk.Label(frame_query, text="Word 1:")
label_word1.pack(side=tk.LEFT)
entry_word1 = tk.Entry(frame_query)
entry_word1.pack(side=tk.LEFT)
label_word2 = tk.Label(frame_query, text="Word 2:")
label_word2.pack(side=tk.LEFT)
entry_word2 = tk.Entry(frame_query)
entry_word2.pack(side=tk.LEFT)
btn_query = tk.Button(frame_query, text="Query Bridge Words", command=query_bridge)
btn_query.pack(side=tk.LEFT)
# 生成新文本
frame_generate = tk.Frame(window)
frame_generate.pack(pady=10)
label_input_text = tk.Label(frame_generate, text="Input Text:")
label_input_text.pack(side=tk.LEFT)
entry_input_text = tk.Entry(frame_generate)
entry_input_text.pack(side=tk.LEFT)
btn_generate = tk.Button(frame_generate, text="Generate New Text", command=generate_text)
btn_generate.pack(side=tk.LEFT)
# 计算最短路径
frame_path = tk.Frame(window)
frame_path.pack(pady=10)
label_word1_path = tk.Label(frame_path, text="Word 1:")
label_word1_path.pack(side=tk.LEFT)
entry_word1_path = tk.Entry(frame_path)
entry_word1_path.pack(side=tk.LEFT)
label_word2_path = tk.Label(frame_path, text="Word 2:")
label_word2_path.pack(side=tk.LEFT)
entry_word2_path = tk.Entry(frame_path)
entry_word2_path.pack(side=tk.LEFT)
btn_path = tk.Button(frame_path, text="Calculate Shortest Path", command=shortest_path)
btn_path.pack(side=tk.LEFT)
# 随机行走
frame_walk = tk.Frame(window)
frame_walk.pack(pady=10)
btn_walk = tk.Button(frame_walk, text="Random Walk", command=random_walk)
btn_walk.pack(side=tk.LEFT)

# 运行UI主循环
window.mainloop()
