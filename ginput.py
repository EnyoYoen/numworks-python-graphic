from kandinsky import fill_rect, draw_string
from ion import keydown
from time import sleep
from gwidget import GWidget

class GInput(GWidget):
  def __init__(self,x,y,width,height,borderWidth=1,borderColor=(0,0,0),fillColor=(0,0,255),textColor=(0,0,0)):
    super().__init__(x,y,width,height,borderWidth,borderColor,fillColor)
    self.initClickedState()
    self._textColor=textColor
    self._inputText=""

  def getInputText(self):
    return self._inputText

  def setHeight(self, height):
    if height<20+self._borderWidth*2:
      height=20+self._borderWidth*2
    self._height=height

  def initClickedState(self,borderColor=(255,0,0),fillColor=(0,255,255),textColor=(0,0,0)):
    self._clickedBorderColor=borderColor
    self._clickedFillColor=fillColor
    self._clickedTextColor=textColor
  
  def setClicked(self,state=True):
    if self._activate:
      sleep(0.15)
      self._activate=False
      self._draw(2)
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

  def _draw(self,state):
    if state in [0,1,2]: 
      if state==2:
        fill_rect(self._x,self._y,self._width,self._borderWidth,self._clickedBorderColor)
        fill_rect(self._x,self._y,self._borderWidth,self._height,self._clickedBorderColor)
        fill_rect(self._x+self._width-self._borderWidth,self._y+self._borderWidth,self._borderWidth,self._height-self._borderWidth,self._clickedBorderColor)
        fill_rect(self._x+self._borderWidth,self._y+self._height-self._borderWidth,self._width-self._borderWidth,self._borderWidth,self._clickedBorderColor)
        fill_rect(self._x+self._borderWidth,self._y+self._borderWidth,self._width-self._borderWidth*2,self._height-self._borderWidth*2,self._clickedFillColor)
      else:
        super()._draw(state)