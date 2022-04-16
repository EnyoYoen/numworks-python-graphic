from time import sleep
from ginput import *
from gbutton import *
from glayout import *

class App:
  def __init__(self):
    self.button=GButton(10,10,300,130,callback,"Press me",2,(0,0,0),(191,191,191))
    self.input=GInput(10,150,300,62,"Enter text",2,(100,100,100),(0,0,0),(191,191,191))

    self.layout=GLayout(False)
    self.layout.addWidget(self.button,"button")
    self.layout.addWidget(self.input,"input")
    self.layout.display()

  def run(self):
    while True:
      app.layout.keyPressed()
      sleep(0.15)

def callback():
  app.button.setText(app.input.getInputText())
  app.button.display()

app=App()
app.run()
