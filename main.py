import math
import pandas as pd

def main():
  text=open("ly.txt","r")
  lines=text.readlines()

  for line in lines:
    pd.DataFrame(line)
    
  


main()