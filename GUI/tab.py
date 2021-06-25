from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)
        
        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.setMovable(True)
        tabs.addTab(QLabel("this is tab 1"), 'Tab 1')
        tabs.addTab(QLabel("this is tab 2"), 'Tab 2')
        tabs.addTab(QLabel("this is tab 3"), 'Tab 3')

        layout.addWidget(tabs)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




app = QApplication([])
window = main()
window.show()
app.exec()