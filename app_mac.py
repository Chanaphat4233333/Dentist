import sys
import traceback
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# Import ฟังก์ชันจาก main.py ของคุณ
try:
    from main import (
        cluster_11_lithium,
        cluster_16_PFMC,
        cluster_35_PFMC,
        cluster_37_FMC,
        cluster_46_FMC,
        loadConfig,
        loadDataSet,
    )
except ImportError:
    pass


# Worker Thread สำหรับประมวลผล background แยกออกจาก Main UI
class WorkerThread(QThread):
    # กำหนด Signal ส่งค่ากลับมาหา UI
    finished_signal = Signal(str, str, str)  # file_path, data_range, results
    error_signal = Signal(str, str)  # error_message, traceback

    def __init__(self, selected_type, file_path):
        super().__init__()
        self.selected_type = selected_type
        self.file_path = file_path

    def run(self):
        try:
            config = loadConfig()
            data, data_range = loadDataSet(self.file_path)

            if self.selected_type == "35_PFMC":
                calculation_results = cluster_35_PFMC(config, data, data_range)
            elif self.selected_type == "11_lithium":
                calculation_results = cluster_11_lithium(
                    config, data, data_range
                )
            elif self.selected_type == "16_PFMC":
                calculation_results = cluster_16_PFMC(config, data, data_range)
            elif self.selected_type == "46_FMC":
                calculation_results = cluster_46_FMC(config, data, data_range)
            elif self.selected_type == "37_FMC":
                calculation_results = cluster_37_FMC(config, data, data_range)
            else:
                raise ValueError(f"invalid type: {self.selected_type}")

            self.finished_signal.emit(
                self.file_path, str(data_range), str(calculation_results)
            )
        except Exception as e:
            self.error_signal.emit(str(e), traceback.format_exc())


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cluster Data Processor")
        self.resize(600, 500)

        # Main Widget & Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)

        # 1. Select Type (QComboBox)
        main_layout.addWidget(QLabel("Select Type:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(
            ["35_PFMC", "11_lithium", "16_PFMC", "46_FMC", "37_FMC"]
        )
        main_layout.addWidget(self.type_combo)

        # 2. File Selection (QLineEdit + QPushButton)
        main_layout.addWidget(QLabel("Select Data File:"))
        file_layout = QHBoxLayout()
        self.file_path_input = QLineEdit()
        self.file_path_input.setReadOnly(True)
        self.file_path_input.setPlaceholderText("ยังไม่ได้เลือกไฟล์...")

        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_file)

        file_layout.addWidget(self.file_path_input)
        file_layout.addWidget(self.browse_btn)
        main_layout.addLayout(file_layout)

        # 3. Run Button
        self.run_btn = QPushButton("🚀 Run Clustering")
        self.run_btn.setStyleSheet(
            "font-size: 14px; font-weight: bold; padding: 8px;"
        )
        self.run_btn.clicked.connect(self.process_data)
        main_layout.addWidget(self.run_btn)

        # 4. Status Label
        self.status_label = QLabel("พร้อมใช้งาน")
        self.status_label.setStyleSheet("color: gray;")
        main_layout.addWidget(self.status_label)

        # 5. Result Output Area (QTextEdit)
        main_layout.addWidget(QLabel("Results:"))
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        main_layout.addWidget(self.result_text)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Data File", ""
        )
        if file_path:
            self.file_path_input.setText(file_path)

    def process_data(self):
        selected_type = self.type_combo.currentText()
        file_path = self.file_path_input.text()

        if not file_path:
            QMessageBox.warning(
                self, "แจ้งเตือน", "กรุณาเลือกไฟล์ข้อมูลก่อนครับ"
            )
            return

        # ปรับสถานะหน้าจอ และปิดปุ่มชั่วคราว
        self.run_btn.setEnabled(False)
        self.status_label.setText("กำลังประมวลผล... กรุณารอสักครู่")
        self.status_label.setStyleSheet("color: blue;")

        # สร้าง Thread ทำงานด้านหลัง
        self.worker = WorkerThread(selected_type, file_path)
        self.worker.finished_signal.connect(self.on_success)
        self.worker.error_signal.connect(self.on_error)
        self.worker.start()

    def on_success(self, file_path, data_range, calculation_results):
        self.result_text.clear()
        self.result_text.append("Status: success")
        self.result_text.append(f"Resource: {file_path}")
        self.result_text.append(f"Total Records: {data_range}")
        self.result_text.append(f"Result Link: {calculation_results}")

        self.status_label.setText("ประมวลผลเสร็จสิ้น!")
        self.status_label.setStyleSheet("color: green;")
        self.run_btn.setEnabled(True)

    def on_error(self, error_msg, trace_back):
        self.status_label.setText("เกิดข้อผิดพลาด!")
        self.status_label.setStyleSheet("color: red;")
        self.run_btn.setEnabled(True)
        QMessageBox.critical(
            self, "Error", f"Internal error: {error_msg}\n\n{trace_back}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())