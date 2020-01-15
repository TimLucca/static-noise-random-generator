import pyaudio 
from sys import byteorder
import matplotlib.pyplot as plt
from matplotlib import colors 
import math
import csv
import time 

chunk = 2
sample_format = pyaudio.paInt16 
channels = 1
fs = 48000 

def genRand(size):
  start = time.time()
  p = pyaudio.PyAudio()

  stream = p.open(format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True)

  frames = []
  nums = []
  num = 0

  for i in range(0, size*32):
    if i % 31 == 0 and i is not 0:
      nums.append(num)
      num = 0
    data = int.from_bytes(stream.read(chunk), byteorder=byteorder)&1
    num += data*(2**(-(i%31)-1))

  stream.stop_stream()
  stream.close()
  p.terminate()

  end = time.time()
  print(f"Elapsed time: {start-end} seconds")

  return nums

def plotRandoms(r, npr):
  fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
  axs[0].hist(r, bins=32)
  axs[1].hist(npr, bins=32)
  plt.show()

def main():
  randoms = []
  run = int(input("Enter the number of runs you would like to perform: "))
  size = int(input("Enter the amount of random numbers to generate: "))
  for i in range(run):
    randoms.append(genRand(size))

  with open('randoms3.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    for randomRow in randoms:
      writer.writerow(randomRow)
  
if __name__ == '__main__':
  main()