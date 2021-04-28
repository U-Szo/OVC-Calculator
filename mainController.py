import module_view.mainview as mainv
import module_calc.calc as ccalc
import splashScreen as sscreen
import psutil
import ctypes
import os

LOADINGCOUNTER = 0

class Admin():
    def __init__(self):
        self.splash_screen_loading_timer = mainv.QtCore.QTimer()
        self.splash_screen_loading_timer.timeout.connect(self.loadingprogress)
        self.splash_screen_loading_timer.start(12)
        self.splash_screen_window=sscreen.splashScreen()
        self.splash_screen_window.show()

        self.window = mainv.MainWindow(self)

        self.mem = psutil.virtual_memory()
        self.appid = os.getpid()
        self.processapp = psutil.Process(self.appid)

        self.memorytimer = mainv.QtCore.QTimer()
        self.memorytimer.timeout.connect(self.memorycheck)
        self.memorytimer.start(10)

    def memorycheck(self):
        mempercent = (self.processapp.memory_info().rss/self.mem.total)*100
        if mempercent > 50:
            self.processapp.kill()
        else:
            pass
        

    def updatematricestree(self):
        self.matricesarrays = []
        self.matricesrows = []
        self.matricescolumns = []
        ccalc.matricesvalues(self)

    def updatevectorstree(self):
        self.vectorsarrays = []
        self.vectorsrows = []
        self.vectorscolumnbs = []
        ccalc.vectorsvalues(self)

    def modifymatrices(self, numberofmatrix, newrows, newcolumns, newvalues):
        ccalc.modifymatricesarrays(self, numberofmatrix,
                                   newrows, newcolumns, newvalues)

    def modifyvectors(self, numberofvector, newrows, newcolumns, newvalues):
        ccalc.modifyvectorsarrays(self, numberofvector, newrows,
                                  newcolumns, newvalues)

    def calculatestringequation(self,equation,degorrad):
        self.degorrad = degorrad
        self.equation_final_result = []
        self.is_equationresult_matrix = False
        self.is_equationresult_intorfloat=False
        self.is_equationresult_complex=False
        ccalc.DEGORRAD = self.degorrad
        ccalc.getequationresult(self,equation)

    def getangleschosenvector(self,vector):
        self.chosenvectorvalues = []
        ccalc.loadchosenvectorvalues(self,vector)
        return self.chosenvectorvalues

    def calculateangles(self,vectorx,vectory,degorrad,ddordms):
        self.degorrad = degorrad
        self.ddordms = ddordms
        ccalc.DEGORRAD = self.degorrad
        ccalc.DDORDMS = self.ddordms
        finalangle = ccalc.angleofvectors(vectorx,vectory)
        return finalangle

    def angleswritevectorscreatearray(self,vectorIvalues,vectorIIvalues,vectorIcolumn,vectorIIcolumn):
        ccalc.createarrayforvectorsInII(vectorIvalues,vectorIIvalues,vectorIcolumn,vectorIIcolumn)

    def geteigenchosenmatrix(self,eigenchosenmatrix):
        self.eigenchosenmatrixobject = []
        ccalc.geteigenchosenmatrixvalues(self,eigenchosenmatrix)

    def geteigenvectors(self,matrixtoeigenize):
        self.eigenvectorsresult = []
        ccalc.calculateeigenvectors(self,matrixtoeigenize)

    def getsystemofequationsresult(self,matrixofconstants,vectorofresults):
        self.systemsofequationsresult = []
        ccalc.calculatesystemofequationsresult(self,matrixofconstants,vectorofresults)

        
    def loadingprogress(self):
        global LOADINGCOUNTER

        self.splash_screen_window.ui.progressBar.setValue(LOADINGCOUNTER)
        if LOADINGCOUNTER > 100:
            self.splash_screen_loading_timer.stop()
            self.window.show()
            self.window.ui.Setstylesheetspoststart()

            self.splash_screen_window.close()

        if LOADINGCOUNTER >90:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>READY</strong>")

        if LOADINGCOUNTER >80 and LOADINGCOUNTER <90:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>DOING</strong> EVEN MORE STUFF")

        if LOADINGCOUNTER >70 and LOADINGCOUNTER <80:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>DOING</strong> STUFF")

        if LOADINGCOUNTER >45 and LOADINGCOUNTER <70:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>PREPARING</strong> LAUNCH")

        if LOADINGCOUNTER >30 and LOADINGCOUNTER <45:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>READING</strong> FILES")

        if LOADINGCOUNTER >20 and LOADINGCOUNTER <30:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>PARSING</strong> DATA")

        if LOADINGCOUNTER >10 and LOADINGCOUNTER <20:
            self.splash_screen_window.ui.loadingprogressLabel.setText("<strong>LOADING</strong> UI")

        LOADINGCOUNTER += 1


if __name__ == "__main__":
    import sys
    app = mainv.QtWidgets.QApplication(sys.argv)
    myappid = 'O.V.C.'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    id = mainv.QtGui.QFontDatabase.addApplicationFont("fonts/Alice-Regular.ttf")
    _fontstr = mainv.QtGui.QFontDatabase.applicationFontFamilies(id)[0]
    _font = mainv.QtGui.QFont(_fontstr, 9)
    app.setFont(_font)
    admin = Admin()
    sys.exit(app.exec_())
