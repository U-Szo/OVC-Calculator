import module_view.Mainview as mainv
import module_calc.CalcMainMatrixAndParserClasses as ccalc
import SplashScreen as sscreen
import psutil
import ctypes
import os

LOADINGCOUNTER = 0

class Admin():
    def __init__(self):
        self.splash_screen_loading_timer = mainv.QtCore.QTimer()
        self.splash_screen_loading_timer.timeout.connect(self.loadingProgress)
        self.splash_screen_loading_timer.start(12)
        self.splash_screen_window=sscreen.SplashScreen()
        self.splash_screen_window.show()

        self.window = mainv.MainWindow(self)

        self.mem = psutil.virtual_memory()
        self.app_id = os.getpid()
        self.process_app = psutil.Process(self.app_id)

        self.memory_timer = mainv.QtCore.QTimer()
        self.memory_timer.timeout.connect(self.memoryCheck)
        self.memory_timer.start(10)

    def memoryCheck(self):
        mem_percent = (self.process_app.memory_info().rss/self.mem.total)*100
        if mem_percent > 50:
            self.process_app.kill()
        else:
            pass
        
    def updateMatricesTree(self):
        self.matrices_arrays = []
        self.matrices_rows = []
        self.matrices_columns = []
        ccalc.matricesValues(self)

    def updateVectorsTree(self):
        self.vectors_arrays = []
        self.vectors_rows = []
        self.vectors_columns = []
        ccalc.vectorsValues(self)

    def modifyMatrices(self, numberofmatrix, newrows, newcolumns, newvalues):
        ccalc.modifyMatricesArrays(self, numberofmatrix,
                                   newrows, newcolumns, newvalues)

    def modifyVectors(self, numberofvector, newrows, newcolumns, newvalues):
        ccalc.modifyVectorsArrays(self, numberofvector, newrows,
                                  newcolumns, newvalues)

    def calculateStringEquation(self,equation,deg_or_rad):
        self.deg_or_rad = deg_or_rad
        self.equation_final_result = []
        self.is_equation_result_matrix = False
        self.is_equation_result_int_or_float=False
        self.is_equation_result_complex=False
        ccalc.DEG_OR_RAD = self.deg_or_rad
        ccalc.getEquationResult(self,equation)

    def getAnglesChosenVector(self,vector):
        self.chosen_vector_values = []
        ccalc.loadChosenVectorValues(self,vector)
        return self.chosen_vector_values

    def calculateAngles(self,vectorx,vectory,deg_or_rad,dd_or_dms):
        self.deg_or_rad = deg_or_rad
        self.dd_or_dms = dd_or_dms
        ccalc.DEG_OR_RAD = self.deg_or_rad
        ccalc.DD_OR_DMS = self.dd_or_dms
        final_angle = ccalc.angleOfVectors(vectorx,vectory)
        return final_angle

    def anglesWriteVectorsCreateArray(self,vectorIvalues,vectorIIvalues,vectorIcolumn,vectorIIcolumn):
        ccalc.createArrayForVectorsIAndII(vectorIvalues,vectorIIvalues,vectorIcolumn,vectorIIcolumn)

    def getChosenMatrix(self,chosenmatrix):
        self.chosen_matrix_object = []
        ccalc.getChosenMatrixValues(self,chosenmatrix)

    def getEigenVectors(self,matrixtoeigenize):
        self.eigen_vectors_result = []
        ccalc.calculateEigenvectors(self,matrixtoeigenize)

    def getSystemOfEquationsResult(self,matrixofconstants,vectorofresults):
        self.systems_of_equations_result = []
        ccalc.calculateSystemOfEquationsResult(self,matrixofconstants,vectorofresults)
        
    def loadingProgress(self):
        global LOADINGCOUNTER

        self.splash_screen_window.ui.progress_bar.setValue(LOADINGCOUNTER)
        if LOADINGCOUNTER > 100:
            self.splash_screen_loading_timer.stop()
            self.window.show()
            self.window.ui.setStylesheetsPoststart()

            self.splash_screen_window.close()

        if LOADINGCOUNTER >90:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>READY</strong>")

        if LOADINGCOUNTER >80 and LOADINGCOUNTER <90:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>DOING</strong> EVEN MORE STUFF")

        if LOADINGCOUNTER >70 and LOADINGCOUNTER <80:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>DOING</strong> STUFF")

        if LOADINGCOUNTER >45 and LOADINGCOUNTER <70:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>PREPARING</strong> LAUNCH")

        if LOADINGCOUNTER >30 and LOADINGCOUNTER <45:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>READING</strong> FILES")

        if LOADINGCOUNTER >20 and LOADINGCOUNTER <30:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>PARSING</strong> DATA")

        if LOADINGCOUNTER >10 and LOADINGCOUNTER <20:
            self.splash_screen_window.ui.loading_progress_label.setText("<strong>LOADING</strong> UI")

        LOADINGCOUNTER += 1


if __name__ == "__main__":
    import sys
    app = mainv.QtWidgets.QApplication(sys.argv)
    my_app_id = 'O.V.C.'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    font_id = mainv.QtGui.QFontDatabase.addApplicationFont("fonts/Alice-Regular.ttf")
    _fontstr = mainv.QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
    _font = mainv.QtGui.QFont(_fontstr, 10)
    app.setFont(_font)
    admin = Admin()
    sys.exit(app.exec_())