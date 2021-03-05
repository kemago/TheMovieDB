from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
import sys


class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Form")

        # Fő elrendezés
        main_layout = QVBoxLayout(self)

        # a fő elrendezésben három gomb
        my_button1 = QPushButton("Click")
        my_button2 = QPushButton("Click")
        my_button3 = QPushButton("Click")

        main_layout.addWidget(my_button1)
        main_layout.addWidget(my_button2)
        main_layout.addWidget(my_button3)

        # Horizontális elrendezés
        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)
        my_button4 = QPushButton("Click")
        my_button5 = QPushButton("Click")
        my_button6 = QPushButton("Click")

        h_layout.addWidget(my_button4)
        h_layout.addWidget(my_button5)
        h_layout.addWidget(my_button6)

        my_button7 = QPushButton("Click")
        my_button8 = QPushButton("Click")
        main_layout.addWidget(my_button7)
        main_layout.addWidget(my_button8)



app = QApplication(sys.argv)
win = MyForm()
win.show()
app.exec_()
