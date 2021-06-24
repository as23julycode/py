from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)
        layout = QVBoxLayout()
        
        input_field = QLineEdit()
        btn = QPushButton("Go")
        
        layout.addWidget(input_field)
        
        # input_field.returnPressed.connect(lambda: print(input_field.text()))
        btn.pressed.connect(lambda: print(input_field.text()))
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    

app = QApplication([])
window = main()
window.show()
app.exec()