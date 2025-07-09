import os
import sys
import requests
import datetime
# print("given sys executable:")
# print(sys.executable)

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget 
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from alpr import scan_plate
from dotenv import load_dotenv,find_dotenv

load_dotenv()
# print("Dotenv path:", find_dotenv())
print("APP_KEY:", os.getenv("APP_KEY"))
# print("LOCATION:", os.getenv("LOCATION"))

api_key=os.getenv('APP_KEY')

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gateless Parking - ALPR")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.image_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.label=QLabel("Load an image to scan",alignment=Qt.AlignmentFlag.AlignCenter )


        self.upload_button = QPushButton("Scan plate")
        self.upload_button.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.label)
        self.label.setFont(QFont("Arial",10))
        # self.label.setStyleSheet("color:white;")


    def upload_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Image Files (*.jpg *.jpeg *.png *.bmp *.gif)")
        
        if file_path:
            pixmap=QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaledToWidth(300))
            car = os.path.basename(file_path)
            self.label.setText(f"File: {car}")
            self.process_car_image(file_path)

    def process_car_image(self,car):

        try:
            # print(f"File path: {car}")
            plate_no=scan_plate(car)
            print(plate_no)
            if plate_no:
                print(plate_no)
                response = requests.post(
                    "http://parkease-nu.vercel.app/api/plate",
                    json={
                        "plate": plate_no,
                        "address": os.getenv("LOCATION"),
                        "timestamp": datetime.datetime.now().isoformat()
                    },
                    headers={"authorization": f"token {api_key}"})
                print(response)
            else:
                self.label.setText("NO PLATE NUMBER DETECTED")

        except Exception as e:
            print(f"Error: {e}")


app=QApplication(sys.argv)
window=App()
window.show()
sys.exit(app.exec())