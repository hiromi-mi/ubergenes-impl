# [Ubergenes](https://esolangs.org/wiki/UberGenes) Implementation written in Python 3
# Original Author: https://esolangs.org/wiki/User:Quintopia
# Maintainer: hiromi_mi
# SPDX-License-Identifier: CC0-1.0
# Original Version (for Python 2): https://esolangs.org/wiki/UberGenes#Python_2
import sys as y
def Z(H,i):c=chr(H.c[H.i+i+1])if H.c[H.i+i+1]in range(256) else repr(c);print("{} is an invalid {} argument at character {}.".format(c,"tsaorugrecte"[i::2],H.i+1+i));y.exit(1)
def g(i):c=chr(i)if i in range(256)else"";return[["0;Z(H,0);_",["H.c[H.v[%s]]"%repr(i+32),"H.v[%d]"%i][c==c.lower()]][c.isalpha()],chr(i)][c.isdigit()]
def p(i):c=chr(i)if i in range(256)else"";return["Z(H,1);_",["H.c[H.v[%s]]"%repr(i+32),"H.v[%d]"%i][c==c.lower()]][c.isalpha()]
def r(H):
 t="=*+-/%|&^:><";q=y.stdout
 while chr(H.c[H.i])in t:
  if H.c[H.i+2]==111:Q=y.stdin.read(1);H.v[111]=ord(Q)if Q else 0
  n=H.c[H.i+1]==111
  if H.c[H.i]==58:
   if eval(g(H.c[H.i+2])):H.v[105]=eval(g(H.c[H.i+1]))
  else:
   exec(p(H.c[H.i+1])+'='+g(H.c[H.i+1])+chr(H.c[H.i])+g(H.c[H.i+2]))
   if n*(H.v[111]in range(256)):q.write(chr(H.v[111]))
  H.v[105]=H.i=H.v[105]+3
 while H.c[H.i]in range(1,256):q.write(chr(H.c[H.i]));H.i+=1
class U:
 def __init__(s,c):
  s.v={};s.i=0;s.c=c
  for i in range(97,123):s.v[i]=0
if __name__=="__main__":
 if len(y.argv)<2:print("No filename to execute.")
 else:
  try:O=open(y.argv[1],"r");c=__import__('collections').defaultdict(int,enumerate(map(ord,list(O.read()))));O.close()
  except IOError:print("File '%s' not found."%f)
  else:r(U(c))

