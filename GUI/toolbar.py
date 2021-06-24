from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)
        
        layout = QVBoxLayout()
        tool_bar = QToolBar("My Tool bar")
        action_btn1 = QAction(QIcon("my.jpg"), "paint", self)
        action_btn1.setCheckable(True)
        tool_bar.addAction(action_btn1)
        tool_bar.addSeparator


        self.addToolBar(tool_bar)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




app = QApplication([])
window = main()
window.show()
app.exec()