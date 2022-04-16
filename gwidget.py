from kandinsky import fill_rect

class GWidget:
 def __init__(self,x,y,w,h,bw=1,bc=(0,0,0),fc=(0,0,255)):
  self.setBorderWidth(bw)
  self.setWidth(w)
  self.setHeight(h)
  self.setX(x)
  self.setY(y)
  self.initActiveState()
  
  self._bc=bc
  self._fc=fc
  self._ds=False

 def getX(self):
  return self._x
 def getY(self):
  return self._y
 def getWidth(self):
  return self._w
 def getHeigt(self):
  return self._h
 def getBorderWidth(self):
  return self._bw

 def setX(self,x):
  if x>=0 and x<=(320-self._w):
   self._x=x
  else:
   self._x=0

 def setY(self,y):
  if y>=0 and y<=(222-self._h):
   self._y=y
  else:
   self._y=0

 def setBorderWidth(self,bw):
  if bw<1:
   bw=1
  elif bw>10:
   bw=10
  self._bw=bw

 def setWidth(self,w):
  if w<self._bw*2:
   w=self._bw*2
  self._w=w

 def setHeight(self,h):
  if h<self._bw*2:
   h=self._bw*2
  self._h=h

 def initActiveState(self,bc=(0,0,0),fc=(0,255,255)):
  self._abc=bc
  self._afc=fc
  self._a=False

 def setActivate(self,s=True):
  if s!=self._a:
   if s:
    self._draw(1)
    self._a=True
   else:
    self.display()
    self._a=False

 def display(self,s=True):
  if self._ds!=s or self._a:
   if s:
    self._draw(0)
   else:
    fill_rect(self.x,self.y,self._w,self._h,(255,255,255))
   self._ds=s
 
 def _draw(self,s):
  if s in [0,1]: 
   if s==0:
    bc=self._bc
    fc=self._fc
   else:
    bc=self._abc
    fc=self._afc
   fill_rect(self._x,self._y,self._w,self._bw,bc)
   fill_rect(self._x,self._y,self._bw,self._h,bc)
   fill_rect(self._x+self._w-self._bw,self._y+self._bw,self._bw,self._h-self._bw,bc)
   fill_rect(self._x+self._bw,self._y+self._h-self._bw,self._w-self._bw,self._bw,bc)
   fill_rect(self._x+self._bw,self._y+self._bw,self._w-self._bw*2,self._h-self._bw*2,fc)
