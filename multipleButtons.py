import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
import asyncio
from qasync import QEventLoop, asyncSlot


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.makeLayout()


    def makeLayout(self):
        # button = QWidget()
        button1 = QPushButton(self)
        button1.setText("Button 1 (normal)")
        button1.setGeometry(25, 50, 200, 250)
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton(self)
        button2.setText("Button 2 (async)")
        button2.setGeometry(275, 50, 200, 250)
        button2.clicked.connect(self.button2_clicked)

        button3 = QPushButton(self)
        button3.setText("Button 3 (decorated)")
        button3.setGeometry(525, 50, 200, 250)
        button3.clicked.connect(self.button3_clicked)



    def button1_clicked(self):
        print("clicked the normal function")

    async def button2_clicked(self):
        print("clicked the async function")

    @asyncSlot()
    async def button3_clicked(self):
        print("clicked the decorated qasync func")


async def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    widget = Window()
    widget.setGeometry(200,150,760,350)
    widget.setWindowTitle("Buttons connected to different funcs")
    widget.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    print("About to start")
    asyncio.run(main())
