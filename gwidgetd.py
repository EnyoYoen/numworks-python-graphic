# Dev version of gwidget.py

from kandinsky import fill_rect

class GWidget:
  def __init__(self,x,y,width,height,borderWidth=1,borderColor=(0,0,0),fillColor=(0,0,255)):
    self.setBorderWidth(borderWidth)
    self.setWidth(width)
    self.setHeight(height)
    self.setX(x)
    self.setY(y)
    self.initActiveState()
    
    self._borderColor=borderColor
    self._fillColor=fillColor
    self._displayState=False

  def getX(self):
    return self._x
  def getY(self):
    return self._y
  def getWidth(self):
    return self._width
  def getHeigt(self):
    return self._height
  def getBorderWidth(self):
    return self._borderWidth

  def setX(self, x):
    if x>=0 and x<=(320-self._width):
      self._x=x
    else:
      self._x=0

  def setY(self, y):
    if y>=0 and y<=(222-self._height):
      self._y=y
    else:
      self._y=0

  def setBorderWidth(self, borderWidth):
    if borderWidth<1:
      borderWidth=1
    elif borderWidth>10:
      borderWidth=10
    self._borderWidth=borderWidth

  def setWidth(self, width):
    if width<self._borderWidth*2:
      width=self._borderWidth*2
    self._width=width

  def setHeight(self, height):
    if height<self._borderWidth*2:
      height=self._borderWidth*2
    self._height=height

  def initActiveState(self,borderColor=(0,0,0),fillColor=(0,255,255)):
    self._activeBorderColor=borderColor
    self._activeFillColor=fillColor
    self._activate=False

  def setActivate(self,state=True):
    if state!=self._activate:
      if state:
        self._draw(1)
        self._activate=True
      else:
        self.display()
        self._activate=False

  def display(self,state=True):
    if self._displayState!=state or self._activate:
      if state:
        self._draw(0)
      else:
        fill_rect(self.x,self.y,self._width,self._height,(255,255,255))
      self._displayState=state
  
  def _draw(self,state):
    if state in [0,1]: 
      if state==0:
        borderColor=self._borderColor
        fillColor=self._fillColor
      else:
        borderColor=self._activeBorderColor
        fillColor=self._activeFillColor
      fill_rect(self._x,self._y,self._width,self._borderWidth,borderColor)
      fill_rect(self._x,self._y,self._borderWidth,self._height,borderColor)
      fill_rect(self._x+self._width-self._borderWidth,self._y+self._borderWidth,self._borderWidth,self._height-self._borderWidth,borderColor)
      fill_rect(self._x+self._borderWidth,self._y+self._height-self._borderWidth,self._width-self._borderWidth,self._borderWidth,borderColor)
      fill_rect(self._x+self._borderWidth,self._y+self._borderWidth,self._width-self._borderWidth*2,self._height-self._borderWidth*2,fillColor)
