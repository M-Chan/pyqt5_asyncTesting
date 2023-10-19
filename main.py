import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    button1 = QPushButton(widget)
    button1.clicked.connect(button1_clicked)

    widget.show()
    sys.exit(app.exec_())


def button1_clicked():
    print("clicked")


if __name__ == "__main__":
    window()
