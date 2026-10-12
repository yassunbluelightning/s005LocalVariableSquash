#s005LocalVariableSquash.py
import pj
import pjTkInter as tk
import pjSound as sound
from logStdErr import logStdErrClass
lse=logStdErrClass()
lse.setProjectName("s005LocalVariableSquash")
lse.errToFile()


tk.updateMainLabel("'squash.py', from \"Learning Programing with Gamecenter Arashi:\nManga ver.Hello Python\" ((C)Mitsuru Sugaya, 2020)")

# Squash Game
# imports Modules
import pj
import random

# initializes Game
class LocalVariableSquashClass:
  def __init__(self):
    self.initGame()
    self.initScreen()
    self.initBall()
    self.initRacket()

  def initGame(self):
    self.isGameOver = False
    self.ballPosX = 0
    self.ballPosY = 250
    self.ballMoveX = 15
    self.ballMoveY = -15
    self.ballSize = 10
    self.racketPosX = 0
    self.racketSize = 100
    self.point = 0
    self.speed = 0.1
    tk.title("Squash Game:Start!")

# initializes Screen
  def initScreen(self):
    # clear Canvas
    tk.removeAllFromCanvas()
    # creates Canvas
    tk.createRectangle("bg",
      640,480, 1,
      0,0,10000,
      ###0,200,200,255)
      ###240,230,140,255) ###Khaki;#F0E68C;
      32,178,170,255) ###LightSeaGreen;;#20B2AA

  def initBall(self):
    # initializes Ball.
    tk.createCircle("Ball1",
self.ballSize,1,
self.ballPosX,self.ballPosY,65000,
255,0,0,255)

  def drawBall(self):
    # draws Ball.
    tk.setPosition("Ball1", self.ballPosX, self.ballPosY)

  def initRacket(self):
    # initializes Racket.
    tk.createRectangle("Racket1",
self.racketSize,10, 1,
self.racketPosX,0,65000,
255, 255,0,255)

  def drawRacket(self):
    # draws Racket.
    tk.setPosition("Racket1", self.racketPosX, 0)

## in order to make the function moveBall() Short.
## Added getMsgStrGood() and getMsgStrBad().
  def getMsgStrGood(self):
    msgInt = random.randint(0, 4)
    if msgInt == 0:
      msgStr = "You are Good at!"
    elif msgInt == 1:
      msgStr = "That's Good!"
    elif msgInt == 2:
      msgStr = "That's Nice!"
    elif msgInt == 3:
      msgStr = "It's Good!"
    elif msgInt == 4:
      msgStr = "Awesome!"
    return msgStr

  def getMsgStrBad(self):
    msgInt = random.randint(0, 2)
    if msgInt == 0:
      msgStr = "You are Bad at!"
    elif msgInt == 1:
      msgStr = "You missed it!"
    elif msgInt == 2:
      msgStr = "I can't see it!"
    return msgStr

# moves Ball
  def moveBall(self):
    if self.isGameOver: return

    # collides with Side Walls
    if self.ballPosX + self.ballMoveX < 0 or self.ballPosX + self.ballMoveX > 640 :
      self.ballMoveX *= -1
      sound.midi(0, 64,0.05)

    # collides with Ceiling
    if self.ballPosY + self.ballMoveY >= 480:
      self.ballMoveY *= -1
      sound.midi(0, 64,0.05)

    # collides with Racket
    if self.ballPosY + self.ballMoveY <= 10 and (
      self.racketPosX <= (self.ballPosX + self.ballMoveX)
    <= (self.racketPosX + self.racketSize)
    ):
      self.ballMoveY *= -1
      if random.randint(0, 1) == 0:
        self.ballMoveX *= -1
      sound.midi(0, 71,0.05)
      msgStr = self.getMsgStrGood()
      self.point += 10
      tk.title(msgStr + " Score=" + str(self.point))

  # judges whether Missed
    if self.ballPosY + self.ballMoveY <= 0:
      msgStr = self.getMsgStrBad()
      tk.title(msgStr + " Score=" + str(self.point))
      sound.midi(0, 54,0.8)
      self.isGameOver = True

    if 0 <= self.ballPosX + self.ballMoveX <= 640:
      self.ballPosX = self.ballPosX + self.ballMoveX
    if 0 <= self.ballPosY + self.ballMoveY <= 480:
      self.ballPosY = self.ballPosY + self.ballMoveY

# Observes Mouse Move
  def motion(self, eventX,eventY): # Observes Mouse Position
    self.racketPosX = eventX
    if self.racketPosX >= 640 - self.racketSize:
      self.racketPosX = 640 - self.racketSize

# Observes Whether Button Clicked.
  def click(self, eventNum): # clicks to restart
    if eventNum == 1:
      self.initGame()

# Sub Routines called from MainLoop.
  def gameLoop(self):
    self.drawBall()
    self.drawRacket()
    self.moveBall()


####from LocalVariableSquashClass import *
# Initialize.
sq = LocalVariableSquashClass()
sq.speed = 0.1
# MainLoop.
####
tk.bindButtonFunction("s005LocalVariableSquash:s005LocalVariableSquash.sq.click")

tk.bindMotionFunction("s005LocalVariableSquash:s005LocalVariableSquash.sq.motion")

####tk.bindMotionCanvasFunction("s005LocalVariableSquash:s005LocalVariableSquash.sq.motionCanvas")

tk.startTimerFunctionAfter("s005LocalVariableSquash:s005LocalVariableSquash.sq.gameLoop", sq.speed)
