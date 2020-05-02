from PyQt5.QtWidgets import *
import sqlite3


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addstudent)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Chemical Engg")
        self.branchinput.addItem("Civil")
        self.branchinput.addItem("Electrical")
        self.branchinput.addItem("Electronics and Communication")
        self.branchinput.addItem("Computer Engineering")
        self.branchinput.addItem("Information Technology")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile No.")
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent(self):

        name = ""
        branch = ""
        sem = -1
        mobile = ""
        address = ""

        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO students (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)",
                           (name, branch, sem, mobile, address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')

