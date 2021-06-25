from PyQt5.QtWidgets import *

class main(QMainWindow):
    def __init__(self, *arg, **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("My First Application")
        self.resize(1000,700)
        lable = QLabel("Aditya Singh")
        font = lable.font()
        font.setPointSize(60)
        lable.setFont(font)
        self.setCentralWidget(lable)

app = QApplication([])
window = main()
window.show()
app.exec()