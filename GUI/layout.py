from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)


        # this is for grid row and colloum
        # {
        # grid = QGridLayout()
        # grid.addWidget(QLabel("Stuff 1"), 0, 2)
        # grid.addWidget(QLabel("Stuff 2"), 3, 1)
        # grid.addWidget(QLabel("Stuff 3"), 2, 2)
        # grid.addWidget(QLabel("Stuff 4"), 3, 3)
        # }
        stack = QStackedLayout()
        stack.addWidget(QLabel("stuff 1"))
        stack.addWidget(QLabel("stuff 2"))
        stack.addWidget(QLabel("stuff 3"))
        stack.addWidget(QLabel("stuff 4"))
        widget = QWidget()
        widget.setLayout(stack)
        self.setCentralWidget(widget)




app = QApplication([])
window = main()
window.show()
app.exec()