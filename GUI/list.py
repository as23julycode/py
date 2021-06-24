from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)
        layout = QVBoxLayout()
        
        list = QListWidget()
        list.addItems(['Easy','Hard','Medium'])
        list.currentItemChanged.connect(self.show_selected)

        layout.addWidget(list)    
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def show_selected(self, items):
        print(items.text())
    

app = QApplication([])
window = main()
window.show()
app.exec()