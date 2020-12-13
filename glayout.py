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
  def getWidgetListLen(self):
    return self._widgetListLen
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
  
  def keyPressed(self, key=None):
    if self._widgetListLen!=0:
      if key==None:
        keys=[self._executeKey, self._deactivateKey, self._moveKey1, self._moveKey2]
      else:
        keys=[key]

      for key in keys:
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
