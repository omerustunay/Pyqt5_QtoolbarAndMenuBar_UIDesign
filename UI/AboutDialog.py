from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle("About")
        title = QLabel("Student Record Maintainer In PyQt5")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()


       # pixmap = QPixmap('')
       # pixmap = pixmap.scaledToWidth(200)
       # labelpic.setPixmap(pixmap)
       # labelpic.setFixedHeight(100)

        layout.addWidget(title)

        layout.addWidget(QLabel("v1.0"))
        layout.addWidget(QLabel("Copyright Omer Ustunay 2020"))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

