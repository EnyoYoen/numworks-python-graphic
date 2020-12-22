from kandinsky import draw_string, fill_rect
from math import floor
from gwidget import GWidget

class GButton(GWidget):
  def __init__(self,x,y,width,height,command=None,text="",borderWidth=1,borderColor=(0,0,0),fillColor=(0,0,255),textColor=(0,0,0)):
    super().__init__(x,y,width,height,borderWidth,borderColor,fillColor)
    self.setText(text)
    self._command=command
    self._textColor=textColor

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

  def initActiveState(self,borderColor=(0,0,0),fillColor=(0,255,255),textColor=(0,0,0)):
    super().initActiveState(borderColor,fillColor)
    self._activeTextColor=textColor

  def setClicked(self,state=True):
    if self._activate:
      self._activate=False
      if self._command!=None:
        return self._command()

  def _draw(self,state):
    super()._draw(state)
    if state==0:
      textColor,fillColor=self._textColor,self._fillColor
    else:
      textColor,fillColor=self._activeTextColor,self._activeFillColor
    draw_string(self._text,self._x+((self._width-self._borderWidth*2)-len(self._text)*10)//2,self._y+(self._height-20)//2,textColor,fillColor)