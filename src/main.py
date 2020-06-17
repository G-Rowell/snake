###############################################################################

#Local imports
import qtSub

##Library imports
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget
#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
#from PyQt5.QtGui import QPalette, QColor

###############################################################################

class Board():
    def __init__(self, rows, cols):
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.list = []

        for x in range(rows):
            tempList = [] 
            for y in range(cols):
                currWidget = qtSub.Color('red')
                tempList.append(currWidget)
                self.layout.addWidget(currWidget,x,y)
            self.list.append(tempList) 

        self.widget.setLayout(self.layout)

app = QApplication([])

window = qtSub.MainWindow()
myBoard = Board(5,5)
window.setCentralWidget(myBoard.widget)  #TODO
window.show()

# Start the event loop
app.exec_()

        
