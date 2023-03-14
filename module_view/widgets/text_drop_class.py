from PySide2 import QtCore, QtGui, QtWidgets
import itertools as itools

class QTextEditDropEnabled(QtWidgets.QTextEdit):
    def __init__(self,admin):
        self.admin = admin
        super(QTextEditDropEnabled, self).__init__()
        self.setAcceptDrops(True)
        self.blinking_colors = itools.cycle([
            QtGui.QColor(50, 50, 50, 255),
            QtGui.QColor(100, 100, 100, 255),
            QtGui.QColor(150, 150, 150, 255),
            QtGui.QColor(180, 180, 180, 255),
            QtGui.QColor(200, 200, 200, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(200, 200, 200, 255),
            QtGui.QColor(180, 180, 180, 255),
            QtGui.QColor(150, 150, 150, 255),
            QtGui.QColor(100, 100, 100, 255),
            QtGui.QColor(50, 50, 50, 255),
            QtGui.QColor(15, 16, 15, 255)
        ])
        self.cursor_painter_timer = QtCore.QTimer()
        self.cursor_painter_timer.timeout.connect(self.changeColor)
        self.cursor_painter_timer.start(32)

    def dragEnterEvent(self, e):
        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        text_to_add=""
        if self.admin.window.ui.tab_buttons_dict["matrix_tab_button"].isChecked():
            text_to_add=str(self.admin.window.ui.draggable_matrix_list_widget.currentItem().text())
            self.admin.window.ui.eq_string_text_edit.insertPlainText(text_to_add)
        elif self.admin.window.ui.tab_buttons_dict["vector_tab_button"].isChecked():
            text_to_add=str(self.admin.window.ui.draggable_vector_list_widget.currentItem().text())
            self.admin.window.ui.eq_string_text_edit.insertPlainText(text_to_add)
        else:
            return
        e.accept()

    def changeColor(self):
        self.color_of_cursor = next(self.blinking_colors)
        self.update()

    def paintEvent(self, event):
        QtWidgets.QTextEdit.paintEvent(self, event)
        if self.hasFocus():
            rect = self.cursorRect(self.textCursor())
            painter = QtGui.QPainter(self.viewport())
            painter.fillRect(rect, self.color_of_cursor)