#! usr/bin/python
"""Author - Oliver Tarrant 
A script to run  and profile the LV*.py files"""
import os
import cProfile


os.system("python -m cProfile LV1.py") # runs a profiles each script with arguments if given
os.system("python -m cProfile LV2.py 1.2 0.12 1.4 0.9")
os.system("python -m cProfile LV3.py 1.2 0.12 1.4 0.9")
os.system("python -m cProfile LV4.py 1.2 0.12 1.4 0.9")
os.system("python -m cProfile LV5.py 1.2 0.12 1.4 0.9")
