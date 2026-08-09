import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import traceback

# Import ฟังก์ชันลอจิกจากไฟล์ main.py เดิมของคุณ
try:
    from main import (
        loadConfig,
        loadDataSet,
        cluster_35_PFMC,
        cluster_11_lithium,
        cluster_16_PFMC,
        cluster_46_FMC,
        cluster_37_FMC,
    )
except ImportError:
    pass


def browse_file():
    filepath = filedialog.askopenfilename(title="Select Data File")
    if filepath:
        file_path_var.set(filepath)


def run_clustering_thread(selected_type, file_path):
    """ฟังก์ชันคำนวณที่ทำงานใน Background Thread เพื่อไม่ให้ UI ค้าง"""
    try:
        config = loadConfig()
        data, data_range = loadDataSet(file_path)

        if selected_type == "35_PFMC":
            calculation_results = cluster_35_PFMC(config, data, data_range)
        elif selected_type == "11_lithium":
            calculation_results = cluster_11_lithium(config, data, data_range)
        elif selected_type == "16_PFMC":
            calculation_results = cluster_16_PFMC(config, data, data_range)
        elif selected_type == "46_FMC":
            calculation_results = cluster_46_FMC(config, data, data_range)
        elif selected_type == "37_FMC":
            calculation_results = cluster_37_FMC(config, data, data_range)
        else:
            raise ValueError(f"invalid type: {selected_type}")

        # เมื่อประมวลผลเสร็จแล้ว อัปเดต UI กลับบน Main Thread
        root.after(0, update_ui_success, file_path, data_range, calculation_results)

    except Exception as e:
        error_msg = str(e)
        trace_back = traceback.format_exc()
        root.after(0, update_ui_error, error_msg, trace_back)


def update_ui_success(file_path, data_range, calculation_results):
    """อัปเดตผลลัพธ์หน้าจอเมื่อคำนวณสำเร็จ"""
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Status: success\n")
    result_text.insert(tk.END, f"Resource: {file_path}\n")
    result_text.insert(tk.END, f"Total Records: {data_range}\n")
    result_text.insert(tk.END, f"Result Link: {calculation_results}\n")

    status_label.config(text="ประมวลผลเสร็จสิ้น!", fg="green")
    run_btn.config(state="normal")


def update_ui_error(error_msg, trace_back):
    """แสดงข้อผิดพลาดเมื่อเกิด Error"""
    status_label.config(text="เกิดข้อผิดพลาด!", fg="red")
    run_btn.config(state="normal")
    messagebox.showerror("Error", f"Internal error: {error_msg}\n\n{trace_back}")


def process_data():
    selected_type = type_var.get()
    file_path = file_path_var.get()

    if not selected_type:
        messagebox.showwarning("แจ้งเตือน", "กรุณาเลือก Type ก่อนครับ")
        return
    if not file_path:
        messagebox.showwarning("แจ้งเตือน", "กรุณาเลือกไฟล์ข้อมูลก่อนครับ")
        return

    # ปิดปุ่มกดชั่วคราว และอัปเดต สถานะ
    run_btn.config(state="disabled")
    status_label.config(text="กำลังประมวลผล... กรุณารอสักครู่", fg="blue")

    # เรียกใช้งาน Threading แยกการคำนวณไปทำด้านหลัง
    threading.Thread(
        target=run_clustering_thread,
        args=(selected_type, file_path),
        daemon=True,
    ).start()


# --- สร้างหน้าต่าง GUI ---
root = tk.Tk()
root.title("Cluster Data Processor")
root.geometry("600x480")

# ตัวแปรเก็บค่า
type_var = tk.StringVar()
file_path_var = tk.StringVar()

# 1. เลือก Type (ใช้ tk.OptionMenu เพื่อให้รองรับ Dropdown บน Mac ได้ 100%)
tk.Label(root, text="Select Type:").pack(anchor="w", padx=15, pady=(15, 0))
type_options = ["35_PFMC", "11_lithium", "16_PFMC", "46_FMC", "37_FMC"]
type_var.set(type_options[0])  # กำหนดค่าเริ่มต้นเป็นตัวแรก
type_dropdown = tk.OptionMenu(root, type_var, *type_options)
type_dropdown.pack(fill="x", padx=15, pady=5)

# 2. เลือก File
tk.Label(root, text="Select Data File:").pack(anchor="w", padx=15, pady=(10, 0))
file_frame = tk.Frame(root)
file_frame.pack(fill="x", padx=15, pady=5)

file_entry = tk.Entry(file_frame, textvariable=file_path_var, state="readonly")
file_entry.pack(side="left", fill="x", expand=True)

browse_btn = ttk.Button(file_frame, text="Browse", command=browse_file)
browse_btn.pack(side="right", padx=(5, 0))

# 3. ปุ่มกด Run (ใช้ ttk.Button เพื่อให้ตอบสนองบน Mac)
run_btn = ttk.Button(root, text="🚀 Run Clustering", command=process_data)
run_btn.pack(fill="x", padx=15, pady=15)

# 4. Status แสดงสถานะ
status_label = tk.Label(root, text="พร้อมใช้งาน", fg="gray")
status_label.pack(anchor="w", padx=15)

# 5. Result Output Area แสดงผลลัพธ์
tk.Label(root, text="Results:").pack(anchor="w", padx=15, pady=(10, 0))
result_text = tk.Text(root, height=8, bg="#f4f4f4")
result_text.pack(fill="both", expand=True, padx=15, pady=(5, 15))

if __name__ == "__main__":
    root.mainloop()