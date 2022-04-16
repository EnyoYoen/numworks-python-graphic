from kandinsky import fill_rect, draw_string
from ion import keydown
from time import sleep

class GInput:
 def __init__(self,x,y,w,h,ph="",bw=1,phc=(127,127,127),bc=(0,0,0),fc=(0,0,255),tc=(0,0,0)):
  self.setBorderWidth(bw)
  self.setWidth(w)
  self.setHeight(h)
  self.setX(x)
  self.setY(y)
  self.initActiveState()
  self.initClickedState()
  self.setPlaceholder(ph)

  self._bc=bc
  self._fc=fc
  self._tc=tc
  self._ds=False
  self._phc=phc
  self._it=""

 def getInputText(self):
  return self._it
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
 def getPlaceholder(self):
  return self._ph
 def getPlaceholderColor(self):
  return self._phc

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
  if h<20+self._bw*2:
   h=20+self._bw*2
  self._h=h
 
 def setPlaceholder(self,ph):
  if self._w<len(ph)*10+self._bw*2:
   l=floor((self._w-self._bw)//10)
   self._ph=ph[0:l]
  else:
   self._ph=ph

 def setTextColor(self,tc):
  self._tc=tc
 
 def initActiveState(self,bc=(0,0,0),fc=(0,255,255),tc=(0,0,0)):
  self._abc=bc
  self._afc=fc
  self._atc=tc
  self._a=False

 def initClickedState(self,bc=(255,0,0),fc=(0,255,255),tc=(0,0,0)):
  self._cbc=bc
  self._cfc=fc
  self._ctc=tc

 def display(self,s=True):
  if self._ds!=s or self._a:
   if s:
    self._draw(self._bc, self._fc)
   else:
    fill_rect(self.x,self.y,self._w,self._h,(255,255,255))
   self._ds=s

 def setActivate(self,s=True):
  if s!=self._a:
   if s:
    self._draw(self._abc,self._afc)
    self._a=True
   else:
    self.display()
    self._a=False
 
 def setClicked(self,s=True):
  if self._a:
   sleep(0.15)
   self._a=False
   self._draw(self._cbc,self._cfc)
   it=""
   n=[42,43,44,36,37,38,30,31,32]
   a=False
   al=False
   s=False
   while not(keydown(4)):
    c=""
    oit=it
    if keydown(13):
     if al:
      al=False
     elif a:
      al=True
      a=False
     else:
      a=True
     sleep(0.15)
     continue

    elif keydown(12):
     if s:
      s=False
     else:
      s=True
     sleep(0.15)
     continue
    
    elif keydown(17):
     if it!="":
      it=it[:len(it)-1]

    else: 
     for ni in n:
      if keydown(ni):
       if a or al:
        if ni==42:c="w"
        elif ni==43:c="x"
        elif ni==44:c="y"
        elif ni==36:c="r"
        elif ni==37:c="s"
        elif ni==38:c="t"
        elif ni==30:c="m"
        elif ni==31:c="n"
        else:c="o"
       else:
        if ni==42:c="1"
        elif ni==43:c="2"
        elif ni==44:c="3"
        elif ni==36:c="4"
        elif ni==37:c="5"
        elif ni==38:c="6"
        elif ni==30:c="7"
        elif ni==31:c="8"
        else:c="9"
       break
     else:
      if keydown(48):c="0"
      elif keydown(18):c="a"
      elif keydown(19):c="b"
      elif keydown(20):c="c"
      elif keydown(21):c="d"
      elif keydown(22):c="e"
      elif keydown(23):c="f"
      elif keydown(24):c="g"
      elif keydown(25):c="h"
      elif keydown(26):c="i"
      elif keydown(27):c="j"
      elif keydown(28):c="k"
      elif keydown(29):c="l"
      elif keydown(33):c="p"
      elif keydown(34):c="q"
      elif keydown(39):c="u"
      elif keydown(40):c="v"
      elif keydown(45):c="z"
      elif keydown(46):c=" "

     if s:
      c=c.upper()
     it+=c
     c=""

    if it!=oit:
     if a:
      a=False
     fill_rect(self._x+self._bw,self._y+self._bw,self._w-self._bw*2,self._h-self._bw*2,self._afc)
     if len(it)*10>=self._w:
      dt=it[:(self._w//10)-1]
     else:
      dt=it
     tw=len(dt)*10
     draw_string(dt,self._x+(self._w-tw)//2,self._y+(self._h-15)//2,self._ctc,self._cfc)
     sleep(0.15)
   self.setActivate()
   if it!="":
    self._it=it
   return(it)
  else:
   return(None)

 def _draw(self,bc,fc):
  fill_rect(self._x,self._y,self._w,self._bw,bc)
  fill_rect(self._x,self._y,self._bw,self._h,bc)
  fill_rect(self._x+self._w-self._bw,self._y+self._bw,self._bw,self._h-self._bw,bc)
  fill_rect(self._x+self._bw,self._y+self._h-self._bw,self._w-self._bw,self._bw,bc)
  fill_rect(self._x+self._bw,self._y+self._bw,self._w-self._bw*2,self._h-self._bw*2,fc)
  draw_string(self._ph,self._x+((self._w-self._bw*2)-len(self._ph)*10)//2,self._y+(self._h-15)//2,self._phc,fc)
