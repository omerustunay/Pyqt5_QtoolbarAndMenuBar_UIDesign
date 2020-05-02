from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from students WHERE roll=" + str(searchrol))
            row = result.fetchone()
            serachresult = "Rollno : " + str(row[0]) + '\n' + "Name : " + str(row[1]) + '\n' + "Branch : " + str(
                row[2]) + '\n' + "Sem : " + str(row[3]) + '\n' + "Address : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find student from the database.')

