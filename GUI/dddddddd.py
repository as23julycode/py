import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
 
 
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
 
        layout = QVBoxLayout()
 
        layout.addWidget(QLabel("You"))
        layout.addWidget(QLabel("Are"))
        layout.addWidget(QLabel("Awesome"))
        layout.addWidget(QLabel("Already"))
 
        widget = QWidget()
        widget.setLayout(layout)
 
        self.setCentralWidget(widget)
 
 
app = QApplication([])
window = MainWindow()
window.show()
app.exec()