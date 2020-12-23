from kandinsky import fill_rect, draw_string
from ion import keydown
from time import sleep

class GInput:
  def __init__(self,x,y,width,height,borderWidth=1,placeholder="",placeholderColor=(127,127,127),borderColor=(0,0,0),fillColor=(0,0,255),textColor=(0,0,0)):
    self.setBorderWidth(borderWidth)
    self.setWidth(width)
    self.setHeight(height)
    self.setX(x)
    self.setY(y)
    self.initActiveState()
    self.initClickedState()
    self.setPlaceholder(placeholder)

    self._borderColor=borderColor
    self._fillColor=fillColor
    self._textColor=textColor
    self._displayState=False
    self._placeholderColor=placeholderColor
    self._inputText=""

  def getInputText(self):
    return self._inputText
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
  def getPlaceholder(self):
    return self._placeholder
  def getPlaceholderColor(self):
    return self._placeholderColor

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
    if height<20+self._borderWidth*2:
      height=20+self._borderWidth*2
    self._height=height
  
  def setPlaceholder(self, placeholder):
    if self._width<len(placeholder)*10+self._borderWidth*2:
      l=floor((self._width-self._borderWidth)//10)
      self._placeholder=placeholder[0:l]
    else:
      self._placeholder=placeholder

  def setTextColor(self, textColor):
    self._textColor=textColor
  
  def initActiveState(self,borderColor=(0,0,0),fillColor=(0,255,255),textColor=(0,0,0)):
    self._activeBorderColor=borderColor
    self._activeFillColor=fillColor
    self._activeTextColor=textColor
    self._activate=False

  def initClickedState(self,borderColor=(255,0,0),fillColor=(0,255,255),textColor=(0,0,0)):
    self._clickedBorderColor=borderColor
    self._clickedFillColor=fillColor
    self._clickedTextColor=textColor

  def display(self,state=True):
    if self._displayState!=state or self._activate:
      if state:
        self._draw(self._borderColor, self._fillColor)
      else:
        fill_rect(self.x,self.y,self._width,self._height,(255,255,255))
      self._displayState=state

  def setActivate(self,state=True):
    if state!=self._activate:
      if state:
        self._draw(self._activeBorderColor,self._activeFillColor)
        self._activate=True
      else:
        self.display()
        self._activate=False
  
  def setClicked(self,state=True):
    if self._activate:
      sleep(0.15)
      self._activate=False
      self._draw(self._clickedBorderColor,self._clickedFillColor)
      inputText=""
      numbers=[42,43,44,36,37,38,30,31,32]
      alpha=False
      alphaLocked=False
      shift=False
      while not(keydown(4)):
        char=""
        oldInputText=inputText
        if keydown(13):
          if alphaLocked:
            alphaLocked=False
          elif alpha:
            alphaLocked=True
            alpha=False
          else:
            alpha=True
          sleep(0.15)
          continue

        elif keydown(12):
          if shift:
            shift=False
          else:
            shift=True
          sleep(0.15)
          continue
        
        elif keydown(17):
          if inputText!="":
            inputText=inputText[:len(inputText)-1]

        else: 
          for number in numbers:
            if keydown(number):
              if alpha or alphaLocked:
                if number==42:
                  char="w"
                elif number==43:
                  char="x"
                elif number==44:
                  char="y"
                elif number==36:
                  char="r"
                elif number==37:
                  char="s"
                elif number==38:
                  char="t"
                elif number==30:
                  char="m"
                elif number==31:
                  char="n"
                else:
                  char="o"
              else:
                if number==42:
                  char="1"
                elif number==43:
                  char="2"
                elif number==44:
                  char="3"
                elif number==36:
                  char="4"
                elif number==37:
                  char="5"
                elif number==38:
                  char="6"
                elif number==30:
                  char="7"
                elif number==31:
                  char="8"
                else:
                  char="9"
              break
          else:
            if keydown(48):
              char="0"
            elif keydown(18):
              char="a"
            elif keydown(19):
              char="b"
            elif keydown(20):
              char="c"
            elif keydown(21):
              char="d"
            elif keydown(22):
              char="e"
            elif keydown(23):
              char="f"
            elif keydown(24):
              char="g"
            elif keydown(25):
              char="h"
            elif keydown(26):
              char="i"
            elif keydown(27):
              char="j"
            elif keydown(28):
              char="k"
            elif keydown(29):
              char="l"
            elif keydown(33):
              char="p"
            elif keydown(34):
              char="q"
            elif keydown(39):
              char="u"
            elif keydown(40):
              char="v"
            elif keydown(45):
              char="z"
            elif keydown(46):
              char=" "

          if shift:
            char=char.upper()
          inputText+=char
          char=""

        if inputText!=oldInputText:
          if alpha:
            alpha=False
          fill_rect(self._x+self._borderWidth,self._y+self._borderWidth,self._width-self._borderWidth*2,self._height-self._borderWidth*2,self._activeFillColor)
          if len(inputText)*10>=self._width:
            displayText=inputText[:(self._width//10)-1]
          else:
            displayText=inputText
          textWidth=len(displayText)*10
          draw_string(displayText,self._x+(self._width-textWidth)//2,self._y+(self._height-15)//2,self._clickedTextColor,self._clickedFillColor)
          sleep(0.15)
    self.setActivate()
    return(inputText)

  def _draw(self,borderColor,fillColor):
    fill_rect(self._x,self._y,self._width,self._borderWidth,borderColor)
    fill_rect(self._x,self._y,self._borderWidth,self._height,borderColor)
    fill_rect(self._x+self._width-self._borderWidth,self._y+self._borderWidth,self._borderWidth,self._height-self._borderWidth,borderColor)
    fill_rect(self._x+self._borderWidth,self._y+self._height-self._borderWidth,self._width-self._borderWidth,self._borderWidth,borderColor)
    fill_rect(self._x+self._borderWidth,self._y+self._borderWidth,self._width-self._borderWidth*2,self._height-self._borderWidth*2,fillColor)
    draw_string(self._placeholder,self._x+((self._width-self._borderWidth*2)-len(self._placeholder)*10)//2,self._y+(self._height-20)//2,self._placeholderColor,fillColor)
