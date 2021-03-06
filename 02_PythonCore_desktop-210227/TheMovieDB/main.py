# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from modules.resource_loader import Resources


class MovieDB:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()

        self.resource_loader = Resources()
        self.context.setContextProperty("Resources", self.resource_loader)

        self.engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    MovieDB()

