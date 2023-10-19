import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import asyncio


async def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    button1 = QPushButton(widget)
    button1.clicked.connect(await button1_clicked)

    widget.show()
    sys.exit(app.exec_())


async def button1_clicked():
    print("clicked")


if __name__ == "__main__":
    asyncio.run(window())
