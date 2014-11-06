from PySide import QtGui, QtCore
import sys

class WidgetTeste(QtGui.QGraphicsView):
    
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)
        
        scene = QtGui.QGraphicsScene(self)
        scene.setSceneRect(0, 0, 400, 400)
        self.setScene(scene)
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)
        
        #scene.addRect(150, 50, 50, 50)
        scene.addRect(50, 50, 50, 50,
                      pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin),
                      brush = QtGui.QBrush(QtCore.Qt.white)).setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        #scene.addLine(0, 0, 100, 100,
        #              pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = WidgetTeste()
    widget.show()
    sys.exit(app.exec_())
    
