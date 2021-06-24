from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Button")
        self.resize(1280, 620)
        
        layout = QVBoxLayout()
        bt1 = QPushButton("Button 1")
        bt2 = QPushButton("Button 2")
        
        self.lable = QLabel("Click on Button")
        
        bt1.clicked.connect(self.bt1_click)
        bt2.clicked.connect(self.bt2_click)
        
        layout.addWidget(self.lable)
        layout.addWidget(bt1)
        layout.addWidget(bt2)

        font = self.lable.font()
        font.setPointSize(40)
        self.lable.setFont(font)
        self.lable.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.lable)
        
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    
    def bt1_click(self):
        self.lable.setText("You Clicked 1")
    def bt2_click(self):
        self.lable.setText("You clicked 2")



app = QApplication([])
window = main()
window.show()
app.exec()