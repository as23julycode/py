from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)
        layout = QVBoxLayout()
        
        combo =QComboBox()
        combo.addItems(['easy', 'medium', 'hard', 'super hard'])
        btn = QPushButton("Start")
        btn.pressed.connect(lambda: self.show_selected(combo))

        layout.addWidget(combo)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def show_selected(self, combo):
        print(combo.currentText())


app = QApplication([])
window = main()
window.show()
app.exec()