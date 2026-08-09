import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import traceback

try:
    from main import loadConfig, loadDataSet, cluster_35_PFMC, cluster_11_lithium, cluster_16_PFMC, cluster_46_FMC, cluster_37_FMC
except ImportError:
    pass

def browse_file():
    filepath = filedialog.askopenfilename(title="Select Data File")
    if filepath:
        file_path_var.set(filepath)

def process_data():
    selected_type = type_var.get()
    file_path = file_path_var.get()

    if not selected_type:
        messagebox.showwarning("แจ้งเตือน", "กรุณาเลือก Type ก่อนครับ")
        return
    if not file_path:
        messagebox.showwarning("แจ้งเตือน", "กรุณาเลือกไฟล์ข้อมูลก่อนครับ")
        return

    status_label.config(text="กำลังประมวลผล...", fg="blue")
    root.update()

    try:
   
        config = loadConfig()
        data, data_range = loadDataSet(file_path)

        if selected_type == '35_PFMC':
            calculation_results = cluster_35_PFMC(config, data, data_range)
        elif selected_type == '11_lithium':
            calculation_results = cluster_11_lithium(config, data, data_range)
        elif selected_type == '16_PFMC':
            calculation_results = cluster_16_PFMC(config, data, data_range)
        elif selected_type == '46_FMC':
            calculation_results = cluster_46_FMC(config, data, data_range)
        elif selected_type == '37_FMC':
            calculation_results = cluster_37_FMC(config, data, data_range)
        else:
            raise ValueError(f"invalid type: {selected_type}")

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Status: success\n")
        result_text.insert(tk.END, f"Resource: {file_path}\n")
        result_text.insert(tk.END, f"Total Records: {data_range}\n")
        result_text.insert(tk.END, f"Result Link: {calculation_results}\n")
        
        status_label.config(text="ประมวลผลเสร็จสิ้น!", fg="green")

    except Exception as e:
        status_label.config(text="เกิดข้อผิดพลาด!", fg="red")
        messagebox.showerror("Error", f"Internal error: {str(e)}\n\n{traceback.format_exc()}")

root = tk.Tk()
root.title("Cluster Data Processor")
root.geometry("600x450")
root.padx = 20
root.pady = 20

type_var = tk.StringVar()
file_path_var = tk.StringVar()

tk.Label(root, text="Select Type:").pack(anchor="w", padx=10, pady=(10, 0))
type_options = ['35_PFMC', '11_lithium', '16_PFMC', '46_FMC', '37_FMC']
type_dropdown = ttk.Combobox(root, textvariable=type_var, values=type_options, state="readonly")
type_dropdown.pack(fill="x", padx=10, pady=5)

tk.Label(root, text="Select Data File:").pack(anchor="w", padx=10, pady=(10, 0))
file_frame = tk.Frame(root)
file_frame.pack(fill="x", padx=10, pady=5)

file_entry = tk.Entry(file_frame, textvariable=file_path_var, state="readonly")
file_entry.pack(side="left", fill="x", expand=True)

browse_btn = tk.Button(file_frame, text="Browse", command=browse_file)
browse_btn.pack(side="right", padx=(5, 0))

run_btn = tk.Button(root, text="🚀 Run Clustering", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=process_data)
run_btn.pack(fill="x", padx=10, pady=20)

status_label = tk.Label(root, text="พร้อมใช้งาน", fg="gray")
status_label.pack(anchor="w", padx=10)

tk.Label(root, text="Results:").pack(anchor="w", padx=10, pady=(10, 0))
result_text = tk.Text(root, height=8, bg="#f4f4f4")
result_text.pack(fill="both", expand=True, padx=10, pady=5)

if __name__ == "__main__":
    root.mainloop()