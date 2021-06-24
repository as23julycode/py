from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from delete import Ui_delete_dialog
from edit_book import Ui_Edit_Dialog
from add_book import Ui_Add_Dialog
from books import Ui_MainWindow

# mainWindow

class Edit_Dialog(QDialog):
    def __init__(self, parent=None):
        super(Edit_Dialog, self).__init__(parent)
        self.ui = Ui_Edit_Dialog()
        self.ui.setupUi(self)
        # self.ui.buttonBox.accepted.connect(self.accept)
        # self.ui.buttonBox.rejected.connect(self.reject)

class Add_dialog(QDialog):
    def __init__(self, parent = None):
        super(Add_dialog, self).__init__(parent)
        self.ui = Ui_Add_Dialog()
        self.ui.setupUi(self)
        # self.ui.buttonBox.accepted.connect(self.accept)
        # self.ui.buttonBox.rejected.connect(self.reject)

class mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.new_book_btn.pressed.connect(self.show_add_dialog)

    def save_new_book(self, ui):
        
        new_book = {
            'id' : int(ui.id_spinbox.text()),
            'name' : ui.name_input.text(),
            'description' : ui.description_input.text(),
            'isbn' : ui.isbn_input.text(),
            'page_count': int(ui.page_count_spinbox.text()),
            'issued' : ui.yes.isChecked(),
            'author' : ui.author_input.text(),
            'year' : int(ui.year_spinbox.text())
        }
        for attr in new_book:
            if new_book[attr] == None or str(new_book[attr]) == "":
                return False
        print(new_book)

        
    def show_add_dialog(self):
        input_dlg =  Add_dialog()
        input_dlg.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dlg.ui))
        input_dlg.exec()    


app = QApplication([])
window = mainwindow()
window.show()
app.exec()