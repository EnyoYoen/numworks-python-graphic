from kandinsky import draw_string, fill_rect
from math import floor

class GButton:
 def __init__(self,x,y,w,h,c=None,t="",bw=1,bc=(0,0,0),fc=(0,0,255),tc=(0,0,0)):
  self.setBorderWidth(bw)
  self.setWidth(w)
  self._setHeight(h,t)
  self.setText(t)
  self.setX(x)
  self.setY(y)
  self.initActiveState()

  self._c=c
  self._bc=bc
  self._fc=fc
  self._tc=tc
  self._ds=False

 def getText(self):
  return self._t
 def getX(self):
  return self._x
 def getY(self):
  return self._y
 def getWidth(self):
  return self._w
 def getHeigt(self):
  return self._h

 def setText(self,t):
  if self._w<len(t)*10+self._bw*2:
   l=floor((self._w-self._bw)//10)
   self._t=t[0:l]
  else:
   self._t=t

 def setX(self, x):
  if x>=0 and x<=(320-self._w):
   self._x=x
  else:
   self._x=0

 def setY(self, y):
  if y>=0 and y<=(222-self._h):
   self._y=y
  else:
   self._y=0

 def setBorderWidth(self,bw):
  if bw<0:
   bw=0
  elif bw>10:
   bw=10
  self._bw=bw

 def setWidth(self,w):
  if w<self._bw*2:
   w=self._bw*2
  self._w=w

 def setHeight(self,h):
  if self._t!="":
   if h<20+self._bw*2:
    h=20+self._bw*2
  else:
   if h<self._bw*2:
    h=self._bw*2
  self._h=h

 def _setHeight(self,h,t):
  if t!="":
   if h<20+self._bw*2:
    h=20+self._bw*2
  else:
   if h<self._bw*2:
    h=self._bw*2
  self._h=h
  
 def display(self,s=True):
  if s:
   self._draw(self._bc, self._fc, self._tc)
  else:
   self._draw(self._abc, self._afc, self._atc)
  self._ds=s

 def initActiveState(self,bc=(0,0,0),fc=(0,255,255),tc=(0,0,0)):
  self._abc=bc
  self._afc=fc
  self._atc=tc
  self._a=False
    
 def setActivate(self,s=True):
  if s!=self._a:
   if s:
    self._draw(self._abc,self._afc,self._atc)
    self._a=True
   else:
    self.display()
    self._a=False

 def setClicked(self,s=True):
  if self._a:
   self._a=False
   if self._c!=None:
    self._c()

 def _draw(self,bc,fc,tc):
  fill_rect(self._x,self._y,self._w,self._bw,bc)
  fill_rect(self._x,self._y,self._bw,self._h,bc)
  fill_rect(self._x+self._w-self._bw,self._y+self._bw,self._bw,self._h-self._bw,bc)
  fill_rect(self._x+self._bw,self._y+self._h-self._bw,self._w-self._bw,self._bw,bc)
  fill_rect(self._x+self._bw,self._y+self._bw,self._w-self._bw*2,self._h-self._bw*2,fc)
  draw_string(self._t,self._x+((self._w-self._bw*2)-len(self._t)*10)//2,self._y+(self._h-20)//2,tc,fc)
