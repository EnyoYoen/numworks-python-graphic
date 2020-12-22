from kandinsky import draw_string, fill_rect
from math import floor

class GButton:
  def __init__(self,x,y,width,height,command=None,text="",borderWidth=1,borderColor=(0,0,0),fillColor=(0,0,255),textColor=(0,0,0)):
    self.setBorderWidth(borderWidth)
    self.setWidth(width)
    self._setHeight(height, text)
    self.setText(text)
    self.setX(x)
    self.setY(y)
    self.setBorderWidth(borderWidth)
    self.initActiveState()

    self._command=command
    self._borderColor=borderColor
    self._fillColor=fillColor
    self._textColor=textColor
    self._displayState=False

  def getText(self):
    return self._text
  def getX(self):
    return self._x
  def getY(self):
    return self._y
  def getWidth(self):
    return self._width
  def getHeigt(self):
    return self._height

  def setText(self, text):
    if self._width<len(text)*10+self._borderWidth*2:
      l=floor((self._width-self._borderWidth)//10)
      self._text=text[0:l]
    else:
      self._text=text

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
    if self._text!="":
      if height<20+self._borderWidth*2:
        height=20+self._borderWidth*2
    else:
      if height<self._borderWidth*2:
        height=self._borderWidth*2
    self._height=height

  def _setHeight(self, height, text):
    if text!="":
      if height<20+self._borderWidth*2:
        height=20+self._borderWidth*2
    else:
      if height<self._borderWidth*2:
        height=self._borderWidth*2
    self._height=height
  
  def display(self,state=True):
    if self._displayState!=state or self._activate:
      if state:
        self._draw(self._borderColor, self._fillColor, self._textColor)
      else:
        fill_rect(self.x,self.y,self._width,self._height,(255,255,255))
      self._displayState=state

  def initActiveState(self,borderColor=(0,0,0),fillColor=(0,255,255),textColor=(0,0,0)):
    self._activeBorderColor=borderColor
    self._activeFillColor=fillColor
    self._activeTextColor=textColor
    self._activate=False
    
  def setActivate(self,state=True):
    if state:
      self._draw(self._activeBorderColor,self._activeFillColor,self._activeTextColor)
      self._activate=True
    else:
      self.display()
      self._activate=False

  def setClicked(self,state=True):
    if self._activate:
      if self._command!=None:
          self._command()
          return self._command

  def _draw(self,borderColor,fillColor,textColor):
    fill_rect(self._x,self._y,self._width,self._borderWidth,borderColor)
    fill_rect(self._x,self._y,self._borderWidth,self._height,borderColor)
    fill_rect(self._x+self._width-self._borderWidth,self._y+self._borderWidth,self._borderWidth,self._height-self._borderWidth,borderColor)
    fill_rect(self._x+self._borderWidth,self._y+self._height-self._borderWidth,self._width-self._borderWidth,self._borderWidth,borderColor)
    fill_rect(self._x+self._borderWidth,self._y+self._borderWidth,self._width-self._borderWidth*2,self._height-self._borderWidth*2,fillColor)
    draw_string(self._text,self._x+((self._width-self._borderWidth*2)-len(self._text)*10)//2,self._y+(self._height-20)//2,textColor,fillColor)
