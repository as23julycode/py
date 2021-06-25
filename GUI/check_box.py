from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Check Box")
        self.resize(1280, 620)
        layout = QVBoxLayout()
        check1 = QCheckBox("Pick any groceries")
        check1.toggled.connect(lambda: self.something_checked(check1))
        check2 = QCheckBox("Write code every day")
        check2.toggled.connect(lambda: self.something_checked(check2))
        self.checked_stuff = []
        self.label = QLabel("You have not selected any thing")
        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(self.label)
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def something_checked(self, check):
        # print(check.isChecked())
        if check.isChecked() == False:
            self.checked_stuff = list(filter(lambda stuff: (stuff != check.text()), self.checked_stuff))
        else:
            self.checked_stuff.append(check.text())
        task_string = ""
        for task in self.checked_stuff:
            task_string += (task + "\n")
        print(self.label.setText(task_string))


app = QApplication([])
window = main()
window.show()
app.exec()