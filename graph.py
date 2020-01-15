import pyaudio 
from sys import byteorder
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import colors 
import math
import csv
import time 

def data():
  data = []
  with open('randoms3.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in reader:
      if len(row) > 1:
        data.append(row)
      
  nums = []
  for row in data:
    rownums = []
    for item in row:
      rownums.append(float(item))
    nums.append(rownums)
  return nums

def tostring(num):
  d = ctx.create_decimal(repr(num))
  return format(d, 'f')

def plotRandoms(r, npr):
  fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
  axs[0].hist(r, bins=10000)
  axs[1].hist(npr, bins=10000)
  plt.show()

def main():
  np.random.seed()
  randoms = data()
  lst = []
  for row in randoms:
    for item in row:
      lst.append(item)

  nprandoms = np.random.random_sample(len(lst))

  plotRandoms(lst, nprandoms)

if __name__ == '__main__':
  main()