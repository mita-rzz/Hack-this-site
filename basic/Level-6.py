awal=input()
a=0
for i in awal:
  tes=int(ord(i))
  tes-=a
  print(chr(tes),end='')
  a+=1
