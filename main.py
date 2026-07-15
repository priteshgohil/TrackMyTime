import sys,time,datetime,ctypes
from ctypes import wintypes
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from ui.main_window import MainWindow
from database import Database
from tracker import IdleDetector
from reports import build_report,fmt
from constants import *
class App(MainWindow):
    def __init__(self):
      super().__init__(); self.db=Database(); self.active=self.idle=self.locked=0; self.lock_state=False; self.last=time.time(); self.timer=QTimer(); self.timer.timeout.connect(self.tick); self.timer.start(1000)
    def showEvent(self,e): ctypes.windll.wtsapi32.WTSRegisterSessionNotification(int(self.winId()),0); super().showEvent(e)
    def nativeEvent(self,t,m):
      msg=wintypes.MSG.from_address(int(m))
      if msg.message==WM_WTSSESSION_CHANGE:
       if msg.wParam==WTS_SESSION_LOCK: self.lock_state=True
       elif msg.wParam==WTS_SESSION_UNLOCK: self.lock_state=False
      return False,0
    def tick(self):
      dt=time.time()-self.last; self.last=time.time()
      if self.lock_state: self.locked+=dt; st='LOCKED'
      elif IdleDetector.get_idle_seconds()>self.threshold.value(): self.idle+=dt; st='IDLE'
      else: self.active+=dt; st='ACTIVE'
      self.status.setText(st); self.stats.setText(f'Active {fmt(self.active)}\nIdle {fmt(self.idle)}\nLocked {fmt(self.locked)}')
      self.db.save_day(str(datetime.date.today()),int(self.active),int(self.idle),int(self.locked))
      self.report.setText(build_report(self.db.get_recent()))
app=QApplication(sys.argv); w=App(); w.show(); sys.exit(app.exec())
