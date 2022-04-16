from ion import keydown

class GLayout:
 def __init__(self,h=True):
  self._wl=[]
  self._wll=0
  self._wd={}
  self._awi=None
  self._mk1=1
  self._mk2=2
  self._dk=6
  self._ek=4

 def getWidgetList(self):
  return self._wl
 def getWidgetDictionnary(self):
  return self._wd
 def getWidgetListLen(self):
  return self._wll
 def getActivateIndex(self):
  return self._awi
 def getKey(self,k):
  if k==1:
   k=self._mk1
  elif k==2:
   k=self._mk2
  elif k==3:
   k=self._ek
  elif k==4:
   k=self._dk
  return k

 def setKey(self,k,t):
  if t==1:
   self._mk1=k
  elif t==2:
   self._mk2=k
  elif t==3:
   self._ek=k
  elif t==4:
   self._dk=k

 def addWidget(self,w,wn):
  self._wd[wn]=w
  self._wl.append(w)
  self._wll+=1

 def removeWidget(self,wn):
  w=self._wd[wn]
  self._wd.pop(wn)
  self._wl.remove(w)
  self._wll-=1
 
 def keyPressed(self,k=None):
  if self._wll!=0:
   if k==None:
    ks=[self._ek,self._dk,self._mk1,self._mk2]
    for i in ks:
     if keydown(i):
      k=i
      break

   if k==self._ek:
    if self._awi!=None:
     cw=self._wl[self._awi]
     return(cw.setClicked())

   if k==self._mk1 or k==self._mk2:
    if self._awi==None:
     if k==self._mk1:
      self._awi=0
     else:
      self._awi=self._wll-1
    else:
     self._setActivate(False)
     if k==self._mk1:
      if self._awi==0:
       self._awi=self._wll-1
      else:
       self._awi-=1
     else:
      if self._awi==self._wll-1:
       self._awi=0
      else:
       self._awi+=1
    self._setActivate(True)

   if k==self._dk:
    if self._awi!=None:
     self._setActivate(False)
     self._awi=None

 def display(self,s=True,st=0,e=-1,nd=[]):
  if e<0:
   e=self._wll
  for i in range(st,e):
   if not(i in nd):
    self._wl[i].display(s)

 def _setActivate(self,s=True):
  if self._awi!=None:
   self._wl[self._awi].setActivate(s)
