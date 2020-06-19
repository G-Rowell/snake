###############################################################################

#Local imports
import qtSub

##Library imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

###############################################################################

BOARD_SIZE_X = 40
BOARD_SIZE_Y = 40

SNAKE_LENGTH = 6

###############################################################################

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("QT Snake")

        self.map = QWidget()
        self.mapLayout = QGridLayout()
        self.mapLayout.setSpacing(3)
        self.map.setLayout(self.mapLayout)
        


        self.initMap()

        self.setCentralWidget(self.map)

        self.show()

    def initMap(self):
        self.list = []

        for x in range(BOARD_SIZE_X):
            tempList = [] 
            for y in range(BOARD_SIZE_Y):
                if x % 2 == 0:
                    currWidget = Color('Red')
                else:
                    currWidget = Color('gray')
                tempList.append(currWidget)
                self.mapLayout.addWidget(currWidget,x,y)
            self.list.append(tempList) 

class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    
    # Start the event loop
    app.exec_()

        

