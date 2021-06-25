from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class mydialog(QDialog):
    def __init__(self, *arg , **kwarg):
        super(mydialog, self).__init__(*arg, **kwarg)
        self.setWindowTitle('second window')
        self.resize(200, 200)
        self.label = QLabel("Very Good")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Dialog Box")
        self.resize(1280, 620)
        layout = QVBoxLayout()

        btn = QPushButton("press me")
        # btn.pressed.connect(lambda: mydialog().exec())
        btn.pressed.connect(self.dialog_handler)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def dialog_handler(self):
        dialog = mydialog()
        dialog.label.setText("Now it different")
        dialog.exec()



app = QApplication([])
window = main()
window.show()
app.exec()