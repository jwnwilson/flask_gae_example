import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_PATH = ROOT_DIR + "/lib"

if LIB_PATH not in sys.path:
	sys.path.append(LIB_PATH)