from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QTabWidget,QTextEdit,QFormLayout,QSpinBox
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(); self.resize(600,400)
        l=QVBoxLayout(self); self.status=QLabel(); self.stats=QLabel(); l.addWidget(self.status); l.addWidget(self.stats)
        self.tabs=QTabWidget(); l.addWidget(self.tabs)
        self.report=QTextEdit(); self.tabs.addTab(self.report,'Reports')
        sw=QWidget(); fl=QFormLayout(sw); self.threshold=QSpinBox(); self.threshold.setRange(60,3600); self.threshold.setValue(300); fl.addRow('Idle Threshold',self.threshold); self.tabs.addTab(sw,'Settings')
