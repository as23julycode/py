from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class main(QMainWindow):
    def __init__(self, *arg , **kwarg):
        super(main, self).__init__(*arg, **kwarg)
        self.setWindowTitle("Radio Button")
        self.resize(1280, 620)
        layout = QVBoxLayout()
        
        male_button = QRadioButton("male")
        male_button.toggled.connect(lambda: self.show_selected(male_button))

        female_button = QRadioButton("Female")
        female_button.toggled.connect(lambda: self.show_selected(female_button))
        
        layout.addWidget(male_button)
        layout.addWidget(female_button)

        self.label = QLabel("You have selected") 
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def show_selected(self, button):
        print(self.label.setText(button.text()))


app = QApplication([])
window = main()
window.show()
app.exec()