import random

choice = random.randint(1,2)

if choice == 1:
  print("heads")
else:
  print("tails")

import os
print(os.cpu_count())

import sys
print(sys.path)

import webbrowser

webbrowser.open_new_tab("https://cern.ch")