class GLayout:
  def __init__(self,horizontal=True):
    self._widgetList=[]
    self._widgetListLen=0
    self._widgetDictionnary={}
    self._activateWidgetIndex=None
    self._moveKey1=1
    self._moveKey2=2
    self._deactivateKey=6
    self._executeKey=4

  def getWidgetList(self):
    return self.self._widgetList
  def getWidgetDictionnary(self):
    return self._widgetDictionnary
  def getActivateIndex(self):
    return self._activateWidgetIndex
  def getKey(self,key):
    if key==1:
      key=self._moveKey1      
    elif key==2:
      key=self._moveKey2
    elif key==3:
      key=self._executeKey
    elif key==4:
      key=self._deactivateKey
    return key

  def setKey(self,key,type):
    if type==1:
      self._moveKey1=key
    elif type==2:
      self._moveKey2=key
    elif type==3:
      self._executeKey=key
    elif type==4:
      self._deactivateKey=key

  def addWidget(self, widget, widgetName):
    self._widgetDictionnary[widgetName]=widget
    self._widgetList.append(widget)
    self._widgetListLen+=1

  def removeWidget(self, widgetName):
    widget=self._widgetDictionnary[widgetName]
    self._widgetDictionnary.pop(widgetName)
    self._widgetList.remove(widget)
    self._widgetListLen-=1
  
  def keyPressed(self, key):
    if self._widgetListLen!=0:
      if key==self._executeKey:
        if self._activateWidgetIndex!=None:
          currentWidget=self._widgetList[self._activateWidgetIndex]
          if type(currentWidget)==GButton or type(currentWidget)==GInput:
            return(currentWidget.setClicked())

      if key==self._moveKey1 or key==self._moveKey2:
        if self._activateWidgetIndex==None:
          if key==self._moveKey1:
            self._activateWidgetIndex=0
          else:
            self._activateWidgetIndex=self._widgetListLen-1
        else:
          self._setActivate(False)
          if key==self._moveKey1:
            if self._activateWidgetIndex==0:
              self._activateWidgetIndex=self._widgetListLen-1
            else:
              self._activateWidgetIndex-=1
          else:
            if self._activateWidgetIndex==self._widgetListLen-1:
              self._activateWidgetIndex=0
            else:
              self._activateWidgetIndex+=1
      self._setActivate(True)

      if key==self._deactivateKey:
        if self._activateWidgetIndex!=None:
          self._setActivate(False)
          self._activateWidgetIndex=None

  def _setActivate(self,state=True):
    if self._activateWidgetIndex!=None:
      self._widgetList[self._activateWidgetIndex].setActivate(state)

  def display(self,state=True,start=0,end=-1,notDisplay=[]):
    if end<0:
      end=self._widgetListLen
    for i in range(start,end):
      if not(i in notDisplay):
        self._widgetList[i].display(state)

from gbutton import GButton
from ginput import GInput
from time import *
from snake import *
from ion import *

def helloWorld():
  print("Hello World!")
def test():
  print("Test")

bouton1=GButton(0,0,150,20,helloWorld,"Hello World!",1,(0,0,0),(0,0,255),(0,0,0))
bouton2=GButton(0,30,150,20,go,"Snake",1,(0,0,0),(0,0,255),(0,0,0))
bouton3=GButton(0,60,150,20,test,"Test",1,(0,0,0),(0,0,255),(0,0,0))
inputBox=GInput(0,90,150,20)

layout=GLayout()
layout.addWidget(bouton1,"bouton1")
layout.addWidget(bouton2,"bouton2")
layout.addWidget(bouton3,"bouton3")
layout.addWidget(inputBox,"inputBox")
layout.display()

key=[KEY_OK,KEY_UP,KEY_DOWN,KEY_HOME]
while True:
  for i in key:
    if keydown(i):
      layout.keyPressed(i)
      sleep(0.2)
