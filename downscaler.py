import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image as PILImage

# 전역 변수 설정
IMAGE_OPTIONS = ["16x16", "32x32", "64x64", "128x128", "256x256"]

def resize_images(file_path, selected_resolution):
    try:
        width, height = map(int, selected_resolution.split("x"))
        img = PILImage.open(file_path)
        img_resized = img.resize((width, height), PILImage.LANCZOS)
        new_file_path = os.path.join("after", os.path.basename(file_path))
        img_resized.save(new_file_path)
        return True
    except Exception as e:
        messagebox.showerror("오류", f"{os.path.basename(file_path)} 이미지 크기 변경 중 오류가 발생했습니다:\n{str(e)}")
        return False

def resize_all_images(selected_resolution):
    if not os.path.exists("after"):
        os.makedirs("after")
    success_count = 0
    for file_path in loaded_images:
        if resize_images(file_path, selected_resolution):
            success_count += 1
    messagebox.showinfo("완료", f"{success_count}개의 이미지가 성공적으로 {selected_resolution} 해상도로 변경되었습니다.")

def refresh_image_list():
    global loaded_images
    loaded_images = []
    for widget in file_frame.winfo_children():
        widget.destroy()
    tk.Label(file_frame, text="로드된 이미지 목록:").pack(pady=2)
    png_files = [f for f in os.listdir("before") if f.endswith(".png")]
    for file in png_files:
        loaded_images.append(os.path.join("before", file))
        tk.Label(file_frame, text=f"- {file}").pack(pady=2)

if __name__ == '__main__':

    if not os.path.exists("before"):
        os.makedirs("before")

    root = tk.Tk()
    root.title("반가워요!")

    file_frame = tk.Frame(root, padx=10, pady=10)
    file_frame.pack(fill="x")

    tk.Label(root, text="해상도를 선택해주세요!").pack(pady=5)

    resolution_var = tk.StringVar(value=IMAGE_OPTIONS[0])
    resolution_menu = ttk.Combobox(root, textvariable=resolution_var, values=IMAGE_OPTIONS, state="readonly")
    resolution_menu.pack(pady=5)

    tk.Button(root, text="📸 | 이미지 다운 스케일링 시작", command=lambda: resize_all_images(resolution_var.get()), width=20).pack(pady=5)
    tk.Button(root, text="🔄 | 이미지 목록 새로고침", command=refresh_image_list, width=20).pack(pady=5)
    tk.Button(root, text="😎 | 제작자 @sleepysoong", command=root.quit, width=20).pack(pady=5)

    refresh_image_list()
    root.mainloop()
