#-*- coding:utf-8 -*-
from Tkinter import *
from ttk import *

import tempfile

from tkFileDialog import askopenfilename 
from tkMessageBox import showerror

from datetime import datetime
import ftplib
from ftplib import FTP
from ftplib import FTP_TLS
from tkMessageBox import *
import tkMessageBox
from PIL import Image, ImageTk, ImageDraw
##import Image
##import ImageTk
##import ImageDraw
import os,sys
import XPS_C8_drivers1
import ScrolledText
##import ftputil

#processamento de imagens:#:
import numpy as np
##import matplotlib.pyplot as plt
##import matplotlib.patches as mpatches
##
from skimage import data
from skimage.measure import label
from skimage.measure import regionprops
##
import scipy 
from scipy import misc
from scipy import ndimage
from skimage import morphology
from scipy.misc import imread
##import pylab
#fim bib proc imgs#

# Display error function : simplify error print out and closes socket
def displayErrorAndClose (socketId, errorCode, APIName):
    if (errorCode != -2) and (errorCode != -108):
        [errorCode2, errorString] = XY.ErrorStringGet(socketId, errorCode)
        if (errorCode2 != 0):
            print APIName + ' : ERROR ' + str(errorCode)
        else:
            print APIName + ' : ' + errorString
    else:
        if (errorCode == -2):
            print APIName + ' : TCP timeout'
        if (errorCode == -108):
            print APIName + ' : The TCP/IP connection was closed by an administrator'

    XY.TCP_CloseSocket(socketId)
    return

def buttonVerPosicoesClick(): # frame_aba5 - trajectory construction 
      status = verificar_statusXY_TE()
      if ((status ==1) or (status ==2)):
            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
            [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
            [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
            [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
            rel_guiaX = float(GUIAx - currentPositionx)
            rel_guiaY = float(GUIAy - currentPositiony)            
            richTextBox1.insert(END,"\n# X: %.2f;   " %currentPositionx)
            richTextBox1.insert(END," Y: %.2f;   \n" %currentPositiony)
            richTextBox1.insert(END,"# Z: %.2f;     " %currentPositionz)
            richTextBox1.insert(END," Act: %.2f \n" %currentPositionAct)
            richTextBox1.see(END)
            richTextBox1.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
            if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                          richTextBox1.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                          richTextBox1.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBox1.see(END)
                          
def buttonVerPosicoesClick2(): # aba Initialization 
      status = verificar_statusXY_Init()
      if ((status ==1) or (status ==2)):
            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
            [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
            [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
            [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
            rel_guiaX = float(GUIAx - currentPositionx)
            rel_guiaY = float(GUIAy - currentPositiony)            
            richTextInit.insert(END,"\n# X: %.2f;   " %currentPositionx)
            richTextInit.insert(END," Y: %.2f;   \n" %currentPositiony)
            richTextInit.insert(END,"# Z: %.2f;     " %currentPositionz)
            richTextInit.insert(END," Act: %.2f \n" %currentPositionAct)
            richTextInit.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
            
            if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                richTextInit.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                richTextInit.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
            richTextInit.see(END)


def buttonVerPosicoesClickBasic(): # aba 3 basic
      status = verificar_statusXY_Basic()
      if ((status ==1) or (status ==2)):
      
##      richTextBasic.insert(END,"\n--------------------------------------------------------------" )
##      if (status == 2): #desabilitados X e Y
##              richTextBasic.insert(END,"\n# X and Y Positioners status: DISABLE !")
##              richTextBasic.see(END)
##
##      
##      else:
            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
            [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
            [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
            [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
            rel_guiaX = float(GUIAx - currentPositionx)
            rel_guiaY = float(GUIAy - currentPositiony)            
            richTextBasic.insert(END,"\n# X: %.2f;   " %currentPositionx)
            richTextBasic.insert(END," Y: %.2f;   \n" %currentPositiony)
            richTextBasic.insert(END,"# Z: %.2f;     " %currentPositionz)
            richTextBasic.insert(END," Act: %.2f \n" %currentPositionAct)
            richTextBasic.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
            
            if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                richTextBasic.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                richTextBasic.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
            richTextBasic.see(END)
            #calculo mov em relacao a guia: SHIFT guide:
##                pos_x = GUIAx - posIni_x
##                pos_y = GUIAy - posIni_y
      
def bGoShift(): #aba 5 traj execution
     status = verificar_statusXY_TE()
     if (status ==1):
         
         posIni_x = shiftX.get()
         posIni_y = shiftY.get() #max x 105  max y 140
         richTextBox1.insert(END,"\n--------------------------------------------------------------" )
         if ((posIni_x == " ") or (posIni_y == " ") or (posIni_x == "") or (posIni_y == "") ):
                  richTextBox1.insert(END,"\n## You must enter the SHIFT GUIDE values! ##\n")
                  richTextBox1.see(END)
         else:
             [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
             if (GroupStatus == 20):
                 richTextBox1.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
                 richTextBox1.see(END)
             else:
                  posIni_x = float(posIni_x)
                  posIni_y = float(posIni_y)
                  
                  if ((posIni_x > 251.00) or (posIni_y > 258.20) or (posIni_x < -148.800) or (posIni_y < -141.60)) :
                          richTextBox1.insert(END,"\n## Maximum values: ")
                          richTextBox1.insert(END,"\n## (X:+251.00 and Y:+258.20)mm\n")                                   
                          richTextBox1.insert(END,"\n## Minimum values: ")
                          richTextBox1.insert(END,"\n## (X:-148.80 and Y:-141.60)mm\n")                     
                          richTextBox1.see(END)
                  else:
                          if ((posIni_x < 0) or (posIni_y < 0) or (posIni_x > 130.00) or (posIni_y > 160.00)):
                              richTextBox1.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBox1.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")
                              richTextBox1.see(END)
                      
                          pos_x = GUIAx - posIni_x
                          pos_y = GUIAy - posIni_y
                          jerktime = 0.04
                          aceleracao = 80
                          a= (float(aceleracao))
                          velocidade = 20
                          v= (float(velocidade))
                          [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
                          [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)   
                   
                          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos_y]) #inic eixo Y
                          [errorCode1, returnString1] = XY.GroupMoveAbsolute(socketId, positionerx, [pos_x]) #inic eixo X
                          richTextBox1.insert(END,"\n##Ok. Moved to start position: \n#Shift (%.3f" %posIni_x + ", %.3f" %posIni_y +")\n")
                          richTextBox1.see(END)


def bGoShiftBasic(): #aba3 basic
    status = verificar_statusXY_Basic()
    if (status ==1):

    
         posIni_x = shiftXbasic.get()
         posIni_y = shiftYbasic.get() #max x 105  max y 140
         richTextBasic.insert(END,"\n--------------------------------------------------------------" )
         if ((posIni_x == " ") or (posIni_y == " ") or (posIni_x == "") or (posIni_y == "") ):
                  richTextBasic.insert(END,"\n## You must enter the SHIFT GUIDE values! ##\n")
                  richTextBasic.see(END)
         else:
             [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
             if (GroupStatus == 20):
                 richTextBasic.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
                 richTextBasic.see(END)
             else:
                  posIni_x = float(posIni_x)
                  posIni_y = float(posIni_y)
                  
                  if ((posIni_x > 251.00) or (posIni_y > 258.20) or (posIni_x < -148.800) or (posIni_y < -141.60)) :
                          richTextBasic.insert(END,"\n## Maximum values: ")
                          richTextBasic.insert(END,"\n## (X:+251.00 and Y:+258.20)mm\n")                                   
                          richTextBasic.insert(END,"\n## Minimum values: ")
                          richTextBasic.insert(END,"\n## (X:-148.80 and Y:-141.60)mm\n")                     
                          richTextBasic.see(END)
                  else:
                          if ((posIni_x < 0) or (posIni_y < 0) or (posIni_x > 130.00) or (posIni_y > 160.00)):
                              richTextBasic.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBasic.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")
                              richTextBasic.see(END)
                      
                          pos_x = GUIAx - posIni_x
                          pos_y = GUIAy - posIni_y
                          jerktime = 0.04
                          aceleracao = 80
                          a= (float(aceleracao))
                          velocidade = 20
                          v= (float(velocidade))
                          [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
                          [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)   
                   
                          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos_y]) #inic eixo Y
                          [errorCode1, returnString1] = XY.GroupMoveAbsolute(socketId, positionerx, [pos_x]) #inic eixo X
                          richTextBasic.insert(END,"\n##Ok. Moved to start position: \n#Shift (%.3f" %posIni_x + ", %.3f" %posIni_y +")\n")
                          richTextBasic.see(END)

def bGoShiftImg(): #aba6 img
     posIni_x = shiftXimg.get()
     posIni_y = shiftYimg.get() #max x 105  max y 140
     richTextImg.insert(END,"\n--------------------------------------------------------------" )
     if ((posIni_x == " ") or (posIni_y == " ") or (posIni_x == "") or (posIni_y == "") ):
              richTextImg.insert(END,"\n## You must enter the SHIFT GUIDE values! ##\n")
              richTextImg.see(END)
     else:
         [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
         if (GroupStatus == 20):
             richTextImg.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
             richTextImg.see(END)
         else:
              posIni_x = float(posIni_x)
              posIni_y = float(posIni_y)
              
              if ((posIni_x > 251.00) or (posIni_y > 258.20) or (posIni_x < -148.800) or (posIni_y < -141.60)) :
                      richTextImg.insert(END,"\n## Maximum values: ")
                      richTextImg.insert(END,"\n## (X:+251.00 and Y:+258.20)mm\n")                                   
                      richTextImg.insert(END,"\n## Minimum values: ")
                      richTextImg.insert(END,"\n## (X:-148.80 and Y:-141.60)mm\n")                     
                      richTextImg.see(END)
              else:
                      if ((posIni_x < 0) or (posIni_y < 0) or (posIni_x > 130.00) or (posIni_y > 160.00)):
                          richTextImg.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                          richTextImg.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")
                          richTextImg.see(END)
                  
                      pos_x = GUIAx - posIni_x
                      pos_y = GUIAy - posIni_y
                      jerktime = 0.04
                      aceleracao = 80
                      a= (float(aceleracao))
                      velocidade = 20
                      v= (float(velocidade))
                      [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
                      [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)   
                      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos_y]) #inic eixo Y
                      [errorCode1, returnString1] = XY.GroupMoveAbsolute(socketId, positionerx, [pos_x]) #inic eixo X
                      richTextImg.insert(END,"\n##Ok. Moved to start position: \n#Shift (%.3f" %posIni_x + ", %.3f" %posIni_y +")\n")
                      richTextImg.see(END)

def bGoShiftImgP(): #aba7 img proc
     posIni_x = shiftXip.get()
     posIni_y = shiftYip.get() #max x 105  max y 140
     richTextImgP.insert(END,"\n--------------------------------------------------------------" )
     if ((posIni_x == " ") or (posIni_y == " ") or (posIni_x == "") or (posIni_y == "") ):
              richTextImgP.insert(END,"\n## You must enter the SHIFT GUIDE values! ##\n")
              richTextImgP.see(END)
     else:
         [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
         if (GroupStatus == 20):
             richTextImgP.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
             richTextImgP.see(END)
         else:
              posIni_x = float(posIni_x)
              posIni_y = float(posIni_y)
              
              if ((posIni_x > 251.00) or (posIni_y > 258.20) or (posIni_x < -148.800) or (posIni_y < -141.60)) :
                      richTextImgP.insert(END,"\n## Maximum values: ")
                      richTextImgP.insert(END,"\n## (X:+251.00 and Y:+258.20)mm\n")                                   
                      richTextImgP.insert(END,"\n## Minimum values: ")
                      richTextImgP.insert(END,"\n## (X:-148.80 and Y:-141.60)mm\n")                     
                      richTextImgP.see(END)
              else:
                      if ((posIni_x < 0) or (posIni_y < 0) or (posIni_x > 130.00) or (posIni_y > 160.00)):
                          richTextImgP.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                          richTextImgP.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")
                          richTextImgP.see(END)
                  
                      pos_x = GUIAx - posIni_x
                      pos_y = GUIAy - posIni_y
                      jerktime = 0.04
                      aceleracao = 80
                      a= (float(aceleracao))
                      velocidade = 20
                      v= (float(velocidade))
                      [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
                      [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)   
                      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos_y]) #inic eixo Y
                      [errorCode1, returnString1] = XY.GroupMoveAbsolute(socketId, positionerx, [pos_x]) #inic eixo X
                      richTextImgP.insert(END,"\n##Ok. Moved to start position: \n#Shift (%.3f" %posIni_x + ", %.3f" %posIni_y +")\n")
                      richTextImgP.see(END)


def bGoShiftOrigin(): #aba8 origin
    status = verificar_statusXY_Basic()
    if (status ==1):

    
         posIni_x = shiftXorigin.get()
         posIni_y = shiftYorigin.get() #max x 105  max y 140
         richTextOrigin.insert(END,"\n--------------------------------------------------------------" )
         if ((posIni_x == " ") or (posIni_y == " ") or (posIni_x == "") or (posIni_y == "") ):
                  richTextOrigin.insert(END,"\n## You must enter the SHIFT GUIDE values! ##\n")
                  richTextOrigin.see(END)
         else:
             [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
             if (GroupStatus == 20):
                 richTextOrigin.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
                 richTextOrigin.see(END)
             else:
                  posIni_x = float(posIni_x)
                  posIni_y = float(posIni_y)
                  
                  if ((posIni_x > 251.00) or (posIni_y > 258.20) or (posIni_x < -148.800) or (posIni_y < -141.60)) :
                          richTextOrigin.insert(END,"\n## Maximum values: ")
                          richTextOrigin.insert(END,"\n## (X:+251.00 and Y:+258.20)mm\n")                                   
                          richTextOrigin.insert(END,"\n## Minimum values: ")
                          richTextOrigin.insert(END,"\n## (X:-148.80 and Y:-141.60)mm\n")                     
                          richTextOrigin.see(END)
                  else:
                          if ((posIni_x < 0) or (posIni_y < 0) or (posIni_x > 130.00) or (posIni_y > 160.00)):
                              richTextOrigin.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextOrigin.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")
                              richTextOrigin.see(END)
                      
                          pos_x = GUIAx - posIni_x
                          pos_y = GUIAy - posIni_y
                          jerktime = 0.04
                          aceleracao = 80
                          a= (float(aceleracao))
                          velocidade = 20
                          v= (float(velocidade))
                          [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
                          [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)   
                   
                          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos_y]) #inic eixo Y
                          [errorCode1, returnString1] = XY.GroupMoveAbsolute(socketId, positionerx, [pos_x]) #inic eixo X
                          richTextOrigin.insert(END,"\n##Ok. Moved to start position: \n#Shift (%.3f" %posIni_x + ", %.3f" %posIni_y +")\n")
                          richTextOrigin.see(END)

def bGoAbs():
##    def button2Click(): #Ir Posicionador (X)
##   contents = textBox3.get()
##   contents= (float(contents))
##   if (contents <=200) and (contents >= -200.0): 
##      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [contents]) #inic eixo X   
##      richTextBox1.insert(1.0,"\n#X movido para posicao: %s\n"%contents)
##   else:
##      richTextBox1.insert(1.0,"\n#Valor maximo para movimento entre: (-200.0 e +200.0)\n")
##
##def button3Click(): #Ir Posicionador (Y)
##   contents = textBox4.get()
##   contents= (float(contents))
##   if (contents <=200) and (contents >= -200.0): 
##      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [contents]) #inic eixo X   
##      richTextBox1.insert(1.0,"\n#Y movido para posicao: %s\n"%contents)
##   else:
##      richTextBox1.insert(1.0,"\n#Valor maximo para movimento entre: (-200.0 e +200.0)\n")

   status = verificar_statusXY_Basic()
   if (status ==1): 
       contentsX = textAbsX.get()
       contentsY = textAbsY.get()
       if ((contentsX == "" ) and (contentsY == "")):
           richTextBasic.insert(END,"\n--------------------------------------------------------------" )
           richTextBasic.insert(END,"\n## You must enter the values for X and/or Y ##\n")
           richTextBasic.see(END)

       else:
           if (contentsX == "" ):
               contents= (float(contentsY))
       
               if (contents <=200) and (contents >= -200.0): 
                  [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [contents]) #inic eixo X   
                  richTextBasic.insert(END,"\n# Y absolute movement to: %s\n"%contents)
                  richTextBasic.see(END)
               else:
                  richTextBasic.insert(END,"\n# Exceeded Maximum Values: [-200.0 e +200.0]\n")
                  richTextBasic.see(END)
           else:
               
               if (contentsY == "" ):
                   contents= (float(contentsX))
           
                   if (contents <=200) and (contents >= -200.0): 
                      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [contents]) #inic eixo X   
                      richTextBasic.insert(END,"\n# X absolute movement to: %s\n"%contents)
                      richTextBasic.see(END)
                   else:
                      richTextBasic.insert(END,"\n# Exceeded Maximum Values: [-200.0 e +200.0]\n")
                      richTextBasic.see(END)
                      
               else:
                   contentsX= (float(contentsX))
                   contentsY= (float(contentsY))
           
                   if ( ((contentsX <=200) and (contentsX >= -200.0))  and ((contentsY <=200) and (contentsY >= -200.0)) ):
                      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [contentsX]) #inic eixo X
                      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [contentsY]) #inic eixo X   
                      richTextBasic.insert(END,"\n# X absolute movement to: %s\n"%contentsX)
                      richTextBasic.insert(END,"\n# Y absolute movement to: %s\n"%contentsY)
                      richTextBasic.see(END)
                   else:
                      richTextBasic.insert(END,"\n# Exceeded Maximum Values: [-200.0 e +200.0]\n")
                      richTextBasic.see(END)

##form2=Tk()
##form2.title('ABORT MOVEMENTS')
##form2.resizable(width=FALSE, height=FALSE)
##form2.geometry('250x200+0+0')

##buttonAbort=Button(form2,text=' ABORT MOVEMENTS ', command=bAbort,style = "TButton")
##buttonAbort.place(relx=0.03, rely=0.12, relwidth=0.65, relheight=0.25)
    
##def bAbort():
##    socketId2 = XY.TCP_ConnectToServer('192.168.0.254', 5001, 20)
##
##socketIdz = SingleZ.TCP_ConnectToServer('192.168.0.254', 5001, 20)
##socketIdz2 = SingleZ.TCP_ConnectToServer('192.168.0.254', 5001, 20)
##
##socketIdAct = SingleAct.TCP_ConnectToServer('192.168.0.254', 5001, 20)
##socketIdAct2 = SingleAct.TCP_ConnectToServer('192.168.0.254', 5001, 20)

##      [errorCode, returnString] = XY.GroupMoveAbort (socketId2, group)
    
################################################################################################################################################
##def bExec(): #execucao arquivo de trajetoria spline XYZ, abaixo LienArc
##  
##  nome = nomearq.get()
##  nome1 = nomearq1.get()
##  x = XYZ.GroupMoveAbsolute (socketIdXYZ,group1, [46.1])
## 
####  posIni_x = shiftX.get()
####  posIni_y = shiftY.get()
####  posIni_x = float(posIni_x)
####  posIni_y = float(posIni_y)
##  v = vel.get()
##  n_rep = rep.get()
##  
##  if (nome == "") or (nome == " "):
##      richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##      richTextBox1.insert(END,"\n## You must enter a Traj.File+++++ Name! ##\n")
##      richTextBox1.see(END)
##  else:
##    if ( (v == " ") or (n_rep == " ") or (v == "") or (n_rep == "")):
##      richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##      richTextBox1.insert(END,"\n## You must enter Velocity(float) AND N.rep (integer) ##\n")
##      richTextBox1.see(END)
##    else:
##        
####      if (posIni_x == " ") or (posIni_y == " "):
####          richTextBox1.insert(1.0,"\n## You must enter the SHIFT GUIDE! ##\n")
####      else:
##        nome = nome+".txt"            
##        aceleracao = 20
##        a= float(aceleracao)
##        v = float(v)
##        n_rep = int(n_rep)
##        [Error, GroupStatus] = XYZ.GroupStatusGet (socketIdXYZ, group1)
##        if (GroupStatus == 20):
##              richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##              richTextBox1.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
##              richTextBox1.see(END)
##        else:     
##            if ((nome1 != " ") and (nome1 != "")):            
##                nome1 = nome1+".txt"
##                
##                
##                richTextBox1.insert(END,"\n Ok. Start ... Line-Arc Traj file execution: %s\n" %nome)
##                richTextBox1.insert(END,"\n Ok. Start ... Line-Arc Traj file execution: %s\n" %nome1)
####                XYZSplineExecution(XYZ,teste_arq_pvt.txt,10,10)
##
##                [errorCode, returnString] = XYZ.XYZSplineExecution(socketIdXYZ, group1, nome, v, a)
##                [errorCode, returnString] = XYZ.XYZSplineExecution (socketIdXYZ, group1, nome1, v, a)
##
##                
####                [errorCode, returnString] = XYZ.XYLineArcExecution (socketId, group, nome, v, a, n_rep)
####                [errorCode, returnString] = XYZ.XYLineArcExecution (socketId, group, nome1, v, a, n_rep)
##            else:
##
##                ftp = FTP("192.168.0.254")
##                ftp.login("Administrator", "Administrator")
##                ftp.pwd()
##                ftp.cwd("public/Trajectories")
##                              
##                try:
##                    gettext1(ftp, nome)
##                    richTextBox1.insert(END,"\n Ok. Start ... Line-Arc Traj file execution: %s\n" %nome)
##                    richTextBox1.see(END)
####                    [errorCode, returnString] = XY.XYLineArcExecution (socketId, group, nome, v, a, n_rep)
##                    [errorCode, returnString] = XYZ.XYZSplineExecution(socketIdXYZ, group1, nome, v, a)
##                except ftplib.error_perm:
##                    richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##
##                    richTextBox1.insert(END,"\n##Error: FILE not Found: %s"% nome)
##                    richTextBox1.see(END)
##                    os.unlink(nome)
##                ftp.quit()
                

################################################################################################################################################
##def bExec(): #execucao arquivo de trajetoria LineArc , acima spline XYZ
##      nome = nomearq.get()
##      nome1 = nomearq1.get()
####  x = XYZ.GroupMoveAbsolute (socketIdXYZ,group1, [46.1])
## 
####  posIni_x = shiftX.get()
####  posIni_y = shiftY.get()
####  posIni_x = float(posIni_x)
####  posIni_y = float(posIni_y)
##      v = vel.get()
##      n_rep = rep.get()
##  
##      if (nome == "") or (nome == " "):
##          richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##          richTextBox1.insert(END,"\n## You must enter a Traj.File Name! ##\n")
##          richTextBox1.see(END)
##      else:
##        if ( (v == " ") or (n_rep == " ") or (v == "") or (n_rep == "")):
##          richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##          richTextBox1.insert(END,"\n## You must enter Velocity(float) AND N.rep (integer) ##\n")
##          richTextBox1.see(END)
##        else:
##            
##    ##      if (posIni_x == " ") or (posIni_y == " "):
##    ##          richTextBox1.insert(1.0,"\n## You must enter the SHIFT GUIDE! ##\n")
##    ##      else:
##            nome = nome+".txt"            
##            aceleracao = 20
##            a= float(aceleracao)
##            v = float(v)
##            n_rep = int(n_rep)
##            [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
##            if (GroupStatus == 20):
##                  richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##                  richTextBox1.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
##                  richTextBox1.see(END)
##            else:     
##                if ((nome1 != " ") and (nome1 != "")):            
##                    nome1 = nome1+".txt"
##                    
##                    
##                    richTextBox1.insert(END,"\n # Ok. Start ... Line-Arc Traj file execution: %s\n" %nome)
##                    richTextBox1.insert(END,"\n # Ok. Start ... Line-Arc Traj file execution: %s\n" %nome1)
##                    richTextBox1.insert(END,"\n # v.: %.2f" %v + "; No.rep.: %d" %n_rep )
##    ##                XYZSplineExecution(XYZ,teste_arq_pvt.txt,10,10)
##
##                    [errorCode, returnString] = XY.XYLineArcExecution(socketId, group, nome, v, a, n_rep)
##                    [errorCode, returnString] = XY.XYLineArcExecution (socketId, group, nome1, v, a, n_rep)
##
##                    
##    ##                [errorCode, returnString] = XYZ.XYLineArcExecution (socketId, group, nome, v, a, n_rep)
##    ##                [errorCode, returnString] = XYZ.XYLineArcExecution (socketId, group, nome1, v, a, n_rep)
##                else:
##
##                    ftp = FTP("192.168.0.254")
##                    ftp.login("Administrator", "Administrator")
##                    ftp.pwd()
##                    ftp.cwd("public/Trajectories")
##                                  
##                    try:
##                        gettext1(ftp, nome)
##                        richTextBox1.insert(END,"\n # Ok. Start ... Line-Arc Traj file execution: %s\n" %nome)
##                        richTextBox1.insert(END,"\n # v.: %.2f" %v + "; No.rep.: %d" %n_rep )
##                        richTextBox1.see(END)
##                        [errorCode, returnString] = XY.XYLineArcExecution (socketId, group, nome, v, a, n_rep)
##    
##                    except ftplib.error_perm:
##                        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##
##                        richTextBox1.insert(END,"\n##Error: FILE not Found: %s"% nome)
##                        richTextBox1.see(END)
##                        os.unlink(nome)
##                    ftp.quit()


def bExec(): #execucao arquivo de trajetoria LineArc , acima spline XYZ
      nome = nomearq.get()
      nome1 = nomearq1.get()
      v = vel.get()
      n_rep = rep.get()
  
      if (nome == "") or (nome == " "):
          richTextBox1.insert(END,"\n--------------------------------------------------------------" )
          richTextBox1.insert(END,"\n## You must enter a Traj.File Name! ##\n")
          richTextBox1.see(END)
      else:
        if ( (v == " ") or (n_rep == " ") or (v == "") or (n_rep == "")):
          richTextBox1.insert(END,"\n--------------------------------------------------------------" )
          richTextBox1.insert(END,"\n## You must enter Velocity(float) AND N.rep (integer) ##\n")
          richTextBox1.see(END)
        else:
            nome = nome+".txt"            
            aceleracao = 20
            a= float(aceleracao)
            v = float(v)
            n_rep = int(n_rep)
            status = verificar_statusXY_TE()
            if (status ==1):
##            [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
##            if (GroupStatus == 20):
##                  richTextBox1.insert(END,"\n--------------------------------------------------------------" )
##                  richTextBox1.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
##                  richTextBox1.see(END)
##            else:

                
                if ((nome1 != " ") and (nome1 != "")):            
                    nome1 = nome1+".txt"

                    ftp = FTP("192.168.0.254")
                    ftp.login("Administrator", "imp0rt@lib")
                    ftp.pwd()
                    ftp.cwd("public/Trajectories")
                                  
                    try:
                        gettext1(ftp, nome)
                        
                        
                        richTextBox1.see(END)
    
                    except ftplib.error_perm:
                        
                        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
                        richTextBox1.insert(END,"\n##Error: FILE not Found: %s"% nome)
                        richTextBox1.see(END)
                        os.unlink(nome)
                        
                    try:
                        gettext1(ftp, nome1)
                        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
                        richTextBox1.insert(END,"\n # Ok. Start ... Line-Arc Traj file execution: \n # (1) %s" %nome + " \n # (2) %s"%nome1)
                        
                        richTextBox1.insert(END," \n # v.: %.2f mm/s" %v + "; No.rep.: %d \n" %n_rep )
                        [errorCode, returnString] = XY.XYLineArcExecution(socketId, group, nome, v, a, n_rep)
                        [errorCode, returnString] = XY.XYLineArcExecution(socketId, group, nome1, v, a, n_rep)    
                        richTextBox1.see(END)
                    except ftplib.error_perm:
                        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
                        richTextBox1.insert(END,"\n##Error: FILE not Found: %s\n"% nome1)    
                        richTextBox1.see(END)
                        os.unlink(nome1)
            
                    ftp.quit()
    
                else:

                    ftp = FTP("192.168.0.254")
                    ftp.login("Administrator", "imp0rt@lib")
                    ftp.pwd()
                    ftp.cwd("public/Trajectories")
                                  
                    try:
                        gettext1(ftp, nome)
                        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
                        richTextBox1.insert(END,"\n # Ok. Start ... Line-Arc Traj file execution: %s\n" %nome)
                        richTextBox1.insert(END," # v.: %.2f mm/s" %v + "; No.rep.: %d \n" %n_rep )
                        richTextBox1.see(END)
                        [errorCode, returnString] = XY.XYLineArcExecution (socketId, group, nome, v, a, n_rep)
    
                    except ftplib.error_perm:
                        richTextBox1.insert(END,"\n--------------------------------------------------------------" )

                        richTextBox1.insert(END,"\n##Error: FILE not Found: %s"% nome)
                        richTextBox1.see(END)
                        os.unlink(nome)
                    ftp.quit()



#######################                

def buttonShowInfoOrigin(): #aba 5 - traj execution 
  tkMessageBox.showinfo("CLOSING", "The software must be reload. It will close!")
  form1.destroy()
  
def buttonLimparClick(): #aba 5 - traj execution 
##  tkMessageBox.showinfo("title", "Hello World")
    if (tkMessageBox.askyesno("Question", "Do you Want to clear the form without saving the Log file?")):
           richTextBox1.delete(1.0, END)

def buttonLimparClickInit():    
##  tkMessageBox.showinfo("title", "Hello World")
##    if (tkMessageBox.askyesno("Question", "Do you Want to clear the form?")):
    richTextInit.delete(1.0, END)

def buttonLimparClickBasic():    
    if (tkMessageBox.askyesno("Question", "Do you Want to clear the form?")):
        richTextBasic.delete(1.0, END)


def buttonLimparClickImg():    
    if (tkMessageBox.askyesno("Question", "Do you Want to clear the form?")):
        richTextImg.delete(1.0, END)
def buttonLimparClickImgP():    
    if (tkMessageBox.askyesno("Question", "Do you Want to clear the form?")):
        richTextImgP.delete(1.0, END)


def buttonLimparClickOrigin():    
    if (tkMessageBox.askyesno("Question", "Do you Want to clear the form?")):
        richTextOrigin.delete(1.0, END)


def buttonLimparArqs():
##  tkMessageBox.showinfo("title", "Hello World")
    if (tkMessageBox.askyesno("Question", "Do you Want to clear both File Forms?")):
           richTextArq1.delete(1.0, END)
           richTextArq.delete(1.0, END)
#***


def find(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice = indice + 1
    return -1

def bLoad_file_copia():#16-11
    
    posIni_x = xini.get()
    posIni_y = yini.get()
    
    if ((posIni_x == "") or (posIni_x == " ") or (posIni_y == "") or (posIni_y == " " )):
        richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
        richTextTC.insert(END,"\n# You must enter the initial coordinates for X and Y\n")
        richTextTC.see(END)
    else:    
        fname = askopenfilename(filetypes=(("Trajectory file", "*.txt"),("All files", "*.*")),initialfile=('Selecione o arquivo ...'))
        w = open(fname,'r')
        lst = w.readlines()
        
        
        if fname: 
            try:
                
                richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
                richTextTC.insert(END,"\n## Ok. Selected File:\n %s" %fname)
                richTextTC.see(END)
#*******************************************************************************************************************
                
                for i in range(len(lst)): 
                    richTextArq1.insert(END,lst[i]) 
                    richTextArq1.see(END)
            except:
                richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
                richTextTC.insert(END,"\n## Failed to read file\n %s" %fname)
                richTextTC.see(END)
        
            return


def bLoad_file():
    
    posIni_x = xini.get()
    posIni_y = yini.get()
    
    if ((posIni_x == "") or (posIni_x == " ") or (posIni_y == "") or (posIni_y == " " )):
        richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
        richTextTC.insert(END,"\n# You must enter the initial coordinates for X and Y\n")
        richTextTC.see(END)
    else:    
        fname = askopenfilename(filetypes=(("Trajectory file", "*.txt"),("All files", "*.*")),initialfile=('Selecione o arquivo ...'))
        w = open(fname,'r')
        lst = w.readlines()
        print lst
        if fname: 
            try:
                
                richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
                richTextTC.insert(END,"\n## Ok. Selected File:\n %s" %fname)
                richTextTC.see(END)

#*******************************************************************************************************************
                
##                nomeArqNovo = arq.get()
##                nomeArqNovo = nomeArqNovo +".txt"
##                fescala = open(nomeArqNovo, 'w')
                fator_Escala  = float(1.0)
##                print ("fator escala: %.2f" %fator_Escala)
        
                indice = 0
                movimentoX=[]
                movimentoY=[]
                movimentoZ=[]
                linha1 = lst[0];
                linha2 = lst[1];
                linha3 = lst[2];
##                fescala.write (linha1)
##                fescala.write (linha2)
##                fescala.write (linha3)
################################################################################
################################################################################
                i = 2
                for i in range(len(lst)-2): 
                    i = i+2
##                    print (lst[i])
                    richTextArq1.insert(END,lst[i]) 
                    richTextArq1.see(END)
                    L = find(lst[i],'L')
                    A = find(lst[i],'A')
                    if (L!=-1):
##                            print ('.... Opa, Linha: ')
                            Vlinha = lst[i]
                            tamanho_Vlinha = len(Vlinha)
##                            print ("tamanho linha: ", tamanho_Vlinha)
                            igual = find(lst[i],'=')
##                            print ("Igual pos: ", igual)
                            virgula = find(lst[i],',')
##                            print ("Virgula pos: ", virgula)
                            x = Vlinha[(igual+2):(virgula)]
##                            print ("xxiisss", x)                        
                            y = Vlinha[(virgula+1):(tamanho_Vlinha-1)]
##                            print ("y", y)
                            
                            x1= float(x)
##                            print ("reprint X:: %.2f" %x1)
                            
                            y1= float(y)
##                            print ("reprint Y:: %.2f" %y1)
                           
##                            x2 = x1*fator_Escala
##                            y2 = y1*fator_Escala
##                            print ("reprint X2::: %.2f" %x2)
##                            x = str(x2)
##                            print ("reprint X str:: " ,x)
##                            y = str(y2)
##                            fescala.write ('\nLine = '+x+','+y)
                            
                            posIni_x = float(posIni_x)
                            posIni_y = float(posIni_y)
                            posX = posIni_x - x1
                            posY = posIni_y - y1                   
                            richTextArq.insert(END,"\nLine = %.4f" %posX+ ",%.4f" %posY) 
                            richTextArq.see(END)
                            
                          
                          
################################################################################
                    else:
                        if (A!= -1):
##                            print ('.... Opa, ARCO: ')
                            Vlinha = lst[i]
                            tamanho_Vlinha = len(Vlinha)
##                            print ("tamanho linha: ", tamanho_Vlinha)
                            igual = find(lst[i],'=')
##                            print ("Igual pos: ", igual)
                            virgula = find(lst[i],',')
##                            print ("Virgula pos: ", virgula)
                            r = Vlinha[(igual+2):(virgula)]
                                        
                            a = Vlinha[(virgula+1):(tamanho_Vlinha-1)]
                                 
##                            r1= float(r)
                                         
##                            r2 = r1*fator_Escala
##                            print ("reprint X2::: %.2f" %x2)
##                            r = str(r2)
            
##                            fescala.write ('\nArc = '+r+','+a)
                            raio = (float(r))
                            angulo = (float(a))                
                            richTextArq.insert(END,"\nArc = %.4f" %raio+ ",%.4f" %angulo)
                            richTextArq.see(END)
                        else:
                            pass;
                        
            
               # 
##                richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
##                richTextTC.insert(END,"\n## Ok. Created File:\n %s" %fescala)
##                richTextTC.see(END)
            
            except:
                richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
                richTextTC.insert(END,"\n## Failed to read file\n %s" %fname)
                richTextTC.see(END)
        
            return
#***

def bAdd_atualizacao(): #
          richTextArq.delete(1.0, END)
          posIni_x = xini.get()
          posIni_y = yini.get()

          if ((posIni_x == "") or (posIni_x == " ") or (posIni_y == "") or (posIni_y == " " )):
            richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
            richTextTC.insert(END,"\n# You must enter the initial coordinates for X and Y\n")
            richTextTC.see(END)
          else:   ## Ok. values ​​filled correctly
               posIni_x = float(posIni_x)
               posIni_y = float(posIni_y)
               nome = "nome_swabs.txt"
               w1 = open(nome,'w') #arq conforme abstracao sw usuario
               conteudo_arq_abstracao = richTextArq1.get(1.0, END)
               w1.write(conteudo_arq_abstracao)
               w1.close()
               w1 = open(nome,'r')
               lst = w1.readlines()

               w1.close()
               
               for i in range(len(lst)-1): 
                    
##                   richTextArq.insert(END,lst[i]) 
##                   richTextArq.see(END)
                   
                   L = find(lst[i],'L')
                   A = find(lst[i],'A')
                   l = find(lst[i],'l')
                   a = find(lst[i],'a')
                   
                   if (L!=-1) or (l!=-1):

                            Vlinha = lst[i]
                            print "Vlina", Vlinha
                            tamanho_Vlinha = len(Vlinha)

                            igual = find(lst[i],'=')

                            virgula = find(lst[i],',')

                            x = Vlinha[(igual+2):(virgula)]    
                            y = Vlinha[(virgula+1):(tamanho_Vlinha-1)]
                            x1= float(x)
                            y1= float(y)
                            posIni_x = float(posIni_x)
                            
                            posIni_y = float(posIni_y)
                            print "posIniX", posIni_x
                            print "posIniY", posIni_y
                            posX = posIni_x - x1
                            posY = posIni_y - y1                   
                            richTextArq.insert(END,"Line = %.4f" %posX+ ",%.4f" %posY +"\n") 
                            richTextArq.see(END)

                           
                            
################################################################################
                   else:
                            if (A!= -1) or (a!= -1):

                                Vlinha = lst[i]
##                                print "V arc", Vlinha
                                tamanho_Vlinha = len(Vlinha)
##                                print "tamanho_Vlinha= ", tamanho_Vlinha 
                                igual = find(lst[i],'=')
##                                print "igual", igual

                                virgula = find(lst[i],',')
##                                print "virgula", virgula
                                r = Vlinha[(igual+2):(virgula)]
##                                print "raio", r    
                                a = Vlinha[(virgula+1):(tamanho_Vlinha-1)]
##                                print "arco", a
                                raio = (float(r))
                                angulo = (float(a))                
                                richTextArq.insert(END,"Arc = %.4f" %raio+ ",%.4f" %angulo+"\n")
                                richTextArq.see(END)
                            else:
                                richTextArq.insert(END," ------ LINE ERROR ------\n")
                                richTextArq.see(END)
                                
                                         

def bAdd(): #adiciona traj ao richtext do Arquivo
  
  if (marca1radio ==-1):
    richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
    richTextTC.insert(END,"\n## You should choose a Line or an Arc of RadioButtons #\n")
    richTextTC.see(END)
  else:
      if (radioLinha==1): ##Linha!
          posIni_x = xini.get()
          posIni_y = yini.get()

          x1= xf.get()
          y1= yf.get()
          if ((posIni_x == "") or (posIni_x == " ") or (posIni_y == "") or (posIni_y == " " )):
            richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
            richTextTC.insert(END,"\n# You must enter the initial coordinates for X and Y\n")
            richTextTC.see(END)
          else:   ## Ok. values ​​filled correctly
              
              if ((x1 == " ") or (x1 == " ") or (y1 == " ") or (y1 == " " )):
                  richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
                  richTextTC.insert(END,"\n# You must enter values for X and Y #")
                  richTextTC.see(END)
               
              else:              
                   x1 = (float(x1))
                   y1 = (float(y1))
                   posIni_x = float(posIni_x)
                   posIni_y = float(posIni_y)
                   posX = posIni_x - x1
                   posY = posIni_y - y1                   
                   richTextArq.insert(END,"\nLine = %.4f" %posX+ ",%.4f" %posY)
                   richTextArq.see(END)
                   richTextArq1.insert(END,"\nLine = %.4f" %x1+ ",%.4f" %y1)
                   richTextArq1.see(END)

##
##          richTextArq.insert(END,"\nLine = %.2f" %x+ ",%.2f" %y)
      else:
        if (radioArco==1):
          #richTextBox1.insert(END,"\n ARCO!")
          raio= r.get()
          angulo= a.get()
          if ((raio == " ") or (angulo == " ")):
            richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
            richTextTC.insert(END,"\n# You must enter values for Radius and Angle# ")
            richTextTC.see(END)
          else:
##            richTextBox1.insert(1.0,"\n Ok. valores preenchidos corretamente")
            raio = (float(raio))
            angulo = (float(angulo))
##            somaraio = (float(raio))
            
            richTextArq1.insert(END,"\nArc = %.4f" %raio+ ",%.4f" %angulo)
            richTextArq1.see(END)
            richTextArq.insert(END,"\nArc = %.4f" %raio+ ",%.4f" %angulo)
            richTextArq.see(END)

#----------------------------------------------------------------------------
#------- ARQUIVO DE TRAJETORIA -----------
##FirstTangent = 0; Degrees               -
##DiscontinuityAngle = 0.01; Degrees      -
##Line = 10,0                             -
##Arc = 10,90                             -
#----------------------------------------
#----------------------------------------------------------------------------

def bAdd1(): #adiciona traj ao richtext do Arquivo
             
    nlinhas = textNlinhas.get() 
    largura = textXlargura.get() #length = largura ;
    altura = textYaltura.get() #spacing = altura;
    
        
    if ( (nlinhas ==  "") or (largura =="") or (altura == " ")):
         richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
         richTextTC.insert(END,"\n##You must enter the Values for Automatic Traj.Construction!##\n")
         richTextTC.see(END)  
    else:
        nlinhas = int(textNlinhas.get())
        x = float(0)
        y = float(0)
        largura = float(textXlargura.get())
        altura = float(textYaltura.get())
        altura = altura/1000
        
        richTextArq1.insert(END,"\n#Automatic Trajectory\nConstruction: \n # Number of Lines: %d" %nlinhas +"\n # Length: %.5f [mm]" %largura+"\n # Spacing: %.5f [mm]" %altura + " = \n # Spacing: %.5f [um]" %(altura*1000))
#Y-xis : radioXisY e radioYxis
        
        

        if (xisY == 1):
        #1a Linha:
            richTextArq.insert(END,"\nLine = -%.4f" %largura+",%.4f" %y) #1a Linha
            for loop in range (1,nlinhas):                    
                if ((loop%2) ==0): # n par
                    
                    y = y + altura
                    richTextArq.insert(END,"\nLine = %.4f" %x+ ",-%.4f" %y)                                              

            
                    richTextArq.insert(END,"\nLine = -%.4f" %largura+ ",-%.4f" %y)
                    richTextArq.see(END)
                    
                    
                else: #n impar

                    y = y + altura
                    richTextArq.insert(END,"\nLine = -%.4f" %largura+ ",-%.4f" %y)                        


                    richTextArq.insert(END,"\nLine = %.4f" %x+ ",-%.4f" %y)
                    
                    richTextArq.see(END)
##
##                     nlinhas = textNlinhas.get() 
##    largura = textXlargura.get() #length = largura ;
##    altura = textYaltura.get() #spacing = altura;
                    
            nomearqSalvar.set("XY_n"+textNlinhas.get()+"L"+textXlargura.get()+"S"+textYaltura.get())
        else:
            richTextArq.insert(END,"\nLine = %.4f" %y+",-%.4f" %largura) #1a Linha
            for loop in range (1,nlinhas):                    
                if ((loop%2) ==0): # n par
                    
                    y = y + altura
                    richTextArq.insert(END,"\nLine = -%.4f" %y+ ",%.4f" %x)                                              
            
                    richTextArq.insert(END,"\nLine = -%.4f" %y+ ",-%.4f" %largura)
                    richTextArq.see(END)
                    
                    
                else: #n impar

                    y = y + altura
                    richTextArq.insert(END,"\nLine = -%.4f" %y+ ",-%.4f" %largura)                        

                    richTextArq.insert(END,"\nLine = -%.4f" %y+ ",%.4f" %x)
                    
                    richTextArq.see(END)
            nomearqSalvar.set("YX_n"+textNlinhas.get()+"L"+textXlargura.get()+"S"+textYaltura.get())    
def upload(ftp, file):
    
    ext = os.path.splitext(file)[1]

    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
        
def verificar_inexistencia_erro(): #se nao ha erro de linha no arquivo -
    print "aqui!????!"
    #quando nao detecta nem "Line = " ou "arc = " NOT case sensitive.
    
    conteudo_arq_abstracao = richTextArq.get(1.0, END)

    tam = len(conteudo_arq_abstracao)
    if tam == 1:
        richTextTC.insert(END,"\n## ? Empty File! ##\n")
        richTextTC.see(END)
    else:
        nome = "nome_swabs.txt"
        w1 = open(nome,'w') #arq conforme abstracao sw usuario
        
        w1.write(conteudo_arq_abstracao)
        w1.close()
        w1 = open(nome,'r')
        lst = w1.readlines()
        print "erro tam", len(lst)

        w1.close()
       
        for i in range(len(lst)-1): #ultima linha vazia
            print "erro lst", lst
            error = find(lst[i],'O')
            if (error != -1):
                print "error num -1!", error
                print "lst[i]", lst[i]
                
                return 1
            
            print "error num!", error
        return error    
                
       
    

def bCriarArquivo():

  conteudo_arq = richTextArq.get(1.0, END)
  tam = len(conteudo_arq)
  if tam == 1: 
      richTextTC.insert(END,"\n## You can not save an Empty File! ##\n")
      richTextTC.see(END)
  else:    
      teste = verificar_inexistencia_erro()  
      if (teste == 1):
          richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
          richTextTC.insert(END,"\n There is ~ LINE ERROR ~ you can not create this file. Repair it!" )
          richTextTC.see(END)

      else:
          

          richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
          nome = nomearqSalvar.get()
          nome_swabs = nomearqSalvar.get()
          
          if (nome == ""):
            richTextTC.insert(END,"\n## You must enter a Traj File Name! ##\n")
            richTextTC.see(END)
          else:
              
              
            
                  
            nome_swabs = nome+"-SWabs.txt"  
            nome = nome+".txt"
            
        ##    ftp = ftplib.FTP('192.168.0.254')
        ##    ftp = FTP("192.168.0.254/public/Trajectories/")
            ftp = FTP("192.168.0.254")
            ftp1 = FTP("192.168.0.254")
            ftp.login("Administrator", "imp0rt@lib")
            ftp1.login("Administrator", "imp0rt@lib")
        ##    ftp = FTP("192.168.0.254/public/Trajectories/","Administrator", "Administrator", )
        ##    ftp.login("Administrator","Admivgfnistrator")
        ##    ftp.retrlines('LIST')
            ftp.pwd()
            ftp.cwd("public/Trajectories")
            ftp1.pwd()
            ftp1.cwd("public/traj-sw")
            
        ##    lst = list(im.getdata())
        ##    lista_arqs = list(ftp.retrlines('LIST')       )
        ##    lista_arqs = list(ftp.retrlines('NLST'))
            
        ##    richTextTC.insert(1.0,"\n\INICIO arquivos do diretorio \n\n")
        ##    richTextArq1.insert(END,"\n Loop = %d" %loop)
        ##    richTextTC.insert(1.0,"%s" %((ftp.retrlines('NLST')).readlines))
        ##    lst = ftp.dir()

        ##    filenames = []
            
        ##    ftp.retrlines('NLST', filenames.append)
        ##    x = len(filenames)
        ##    richTextTC.insert(END,"X: %d" %x)
        #imprimir todos nomes:
            
        ##    for i in range(x):
        ##        richTextTC.insert(END,"\n nome %s"%filenames[i])
        #imprimir todos nomes: (fim)

        ##    richTextTC.see(END)
                
            if (tempfile._exists(nome)):      # no PC/diretorio atual do sw # return True or False
                  richTextTC.insert(END,"\n## Existing File. Choose a Different Name! ##\n")
                  richTextTC.see(END)
                
            else:
                w = open(nome,'w')
                w.write ("FirstTangent = 0; Degrees\n")
                w.write ("DiscontinuityAngle = 0.01; Degrees\n")
                conteudo_arq = richTextArq.get(1.0, END)

                
                w1 = open(nome_swabs,'w') #arq conforme abstracao sw usuario
                conteudo_arq_abstracao = richTextArq1.get(1.0, END)
                w1.write(conteudo_arq_abstracao)
                
                w.write(conteudo_arq)
                w.close()
                w1.close()
                upload(ftp, nome)
                
                
                upload(ftp1, nome_swabs)
                
                richTextTC.insert(END,"\n#File created: %s:\n" %nome)
                richTextTC.see(END)
                ftp.quit()
                ftp1.quit()
                nome2 = nomearqSalvar.get()
                nomearq.set(nome2)
                lista_arquivos = ListarArquivos_Combo()
                box['values'] = lista_arquivos
        ##    if (controle_ftp == 0):
        ##        upload(ftp, nome)


def ListarArquivos_Combo():

    try:
        ftp = FTP("192.168.0.254")
        ftp.login("Administrator", "imp0rt@lib")
        ftp.pwd()
        ftp.cwd("public/Trajectories")
            
        filenames = []
        
        ftp.retrlines('NLST', filenames.append)
        x = len(filenames)
        filenames.sort(key=str.lower)
        new_filenames = []
        for i in range(x):
            tam = len(filenames[i])
            for x in range(tam):
                a = filenames[i]
                a = a[:tam-4] #remover extensao
            new_filenames.append(a)
            
            
    ##        richTextTC.insert(END,"\n%s"%filenames[i])

    ##    richTextTC.see(END)
            
        ftp.quit()
        return new_filenames
    except:
        
        x = []
        x = "  ", "  "
        richTextTC.insert(END,"\n# Controller are ON? \n# Check the connection between PC and Controller \n# Can not List Files!")
        return x


def ListarArquivos():
    richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )

    ftp = FTP("192.168.0.254")
    ftp.login("Administrator", "imp0rt@lib")
##    ftp = FTP("192.168.0.254/public/Trajectories/","Administrator", "Administrator", )

##    ftp.login("Administrator","Admivgfnistrator")
##    upload(ftp, "oi.txt")
##    ftp.retrlines('LIST')
    ftp.pwd()
    ftp.cwd("public/Trajectories")
        
##    lst = list(im.getdata())

##    lista_arqs = list(ftp.retrlines('LIST')       )
##    lista_arqs = list(ftp.retrlines('NLST'))
    
##    richTextTC.insert(1.0,"\n\INICIO arquivos do diretorio \n\n")

##    richTextArq1.insert(END,"\n Loop = %d" %loop)
##    richTextTC.insert(1.0,"%s" %((ftp.retrlines('NLST')).readlines))
##    lst = ftp.dir()
    

    filenames = []
    
    ftp.retrlines('NLST', filenames.append)
    x = len(filenames)
##    richTextTC.insert(END,"X: %d" %x)
    filenames.sort(key=str.lower)
    for i in range(x):
        
        richTextTC.insert(END,"\n%s"%filenames[i])


##    richTextTC.insert(END,"\n nome %s"%filenames)

    richTextTC.see(END)
        
##    if (tempfile._exists(nome)):      # no PC/diretorio atual do sw # return True or False

##          richTextTC.insert(END,"\n## Existing File. Choose a Different Name! ##\n")

##          richTextTC.see(END)

##        
##    else:
##        w = open(nome,'w')

##        w.write ("FirstTangent = 0; Degrees\n")

##        w.write ("DiscontinuityAngle = 0.01; Degrees\n")

##        conteudo_arq = richTextArq.get(1.0, END)

##        w.write(conteudo_arq)

##        w.close()

##        upload(ftp, nome)

##        richTextTC.insert(1.0,"\n#File created: %s:\n" %nome)

    ftp.quit()
    return filenames
##    if (controle_ftp == 0):

##        upload(ftp, nome)

def radioUm():
  marcaUnidade = 1
  global fatorUn
  fatorUn = float(1000.0)
  

def radioMm():
  marcaUnidade = 1
  global fatorUn
  fatorUn = float(1.0)


def radioUmBasic():
  marcaUnidadeBasic = 1
  global fatorUnBasic
  fatorUnBasic = 1000

def radioMmBasic():
  marcaUnidadeBasic = 1
  global fatorUnBasic
  fatorUnBasic = 1


#Y-xis : radioXisY e radioYxis
def radioXisY():
    global xisY
    xisY = 1

def radioYxis():
    global xisY
    xisY=0 ####(imagem Y -->. X)

##def radioCm():
##  marcaUnidade = 1
##  global fatorUn
##  fatorUn = 10

def cores_fundoPreto():
    global nova_cor
    nova_cor = 255 #objeto de cor branca
    
def cores_fundoBranco():
    global nova_cor
    nova_cor = 0 #objeto de cor preta

def checkTE():
    
    if (check1.var ==0):
        richTextInit.insert(1.0,"\n#File created: fdfdkfjdkfjkd:\n")
    else:
        richTextBox1.insert(1.0,"\n#NOPS offvalue\n")
    
def checkIE():
    pass

def radioLinhaClick():
    global radioArco
    global radioLinha
    global marca1radio
    marca1radio =1
    radioArco = 0
    radioLinha = 1
    a.set(" ")
    r.set(" ")

def radioArcoClick():
  global radioArco
  global radioLinha
  global marca1radio
  marca1radio =1
  radioLinha = 0
  radioArco = 1


  xf.set(" ")
  yf.set(" ")

def gettext1(ftp, filename, outfile=None): #para bExec() aba Traj Exec. - verificar se Existe Arq(s)
    
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    
##    ftp.retrlines("RETR " + filename, lambda s,sw=outfile.write: w(s+"\n"))
    arq = []

    ftp.retrlines("RETR " + filename,arq.append)   #nao imp pq nao precisa mostrar
##    richTextBox1.insert(END,"\n##You must enter a Traj File Name! ##\n")
    
def gettext(ftp, filename, outfile=None): #para botao OpenFile abrirArqFTP() aba Traj Constr - verificar se ha arquivo e abri-lo/mostrar 
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    
    ##  ftp.retrlines("RETR " + filename, lambda s,sw=outfile.write: w(s+"\n"))
    arq = []
    ftp.retrlines("RETR " + filename, arq.append)
    

    x = len(arq) 
    for i in range(3,x):
        richTextArq.insert(END,"%s"%arq[i]+"\n")
        richTextArq.see(END)


def gettext_swabs(ftp, filename, outfile=None): #para botao OpenFile abrirArqFTP() aba Traj Constr - verificar se ha arquivo e abri-lo/mostrar 
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    
    ##  ftp.retrlines("RETR " + filename, lambda s,sw=outfile.write: w(s+"\n"))
    arq = []
    ftp.retrlines("RETR " + filename, arq.append)
    

    x = len(arq) 
    for i in range(x):
        richTextArq1.insert(END,"%s"%arq[i]+"\n")
        richTextArq1.see(END)

def gettext_nova_guia(ftp, filename, outfile=None):
    #para RESET_Guia (ler anterior e salvar atuais valores)
    #para NOVA_GUIA (salvar valores atuais no anterior, para DEPOIS atualizar os novos valores da guia no arq_atual)
    
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    
    ##  ftp.retrlines("RETR " + filename, lambda s,sw=outfile.write: w(s+"\n"))
    arq = []
    ftp.retrlines("RETR " + filename, arq.append)
    

##    x = len(arq) 
##    for i in range(x):
##        richTextOrigin.insert(END,"\n%s"%arq[i])
##        richTextOrigin.see(END)
    return arq #para arq anterior arq[0 e 1] para ATUAL arq[0,1 e 2] : pos[0] contem indicativo para Reset (posicao atual ja resetada)


def abrirArqFTP():
    ftp = FTP("192.168.0.254")
    ftp.login("Administrator", "imp0rt@lib")
    ftp.pwd()
    ftp.cwd("public/Trajectories")
    ftp1 = FTP("192.168.0.254")
    ftp1.login("Administrator", "imp0rt@lib")
    ftp1.pwd()
    ftp1.cwd("public/traj-sw")
##    nomearqSalvar=StringVar() #NOME ARQUIVO  #frame aba4 traj construction
    
##    FILE = "arco1poledfgada.txt"
    FILE = nomearqSalvar.get()
    if ((FILE == "") or (FILE == " ")):
        richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
        richTextTC.insert(END,"\n## You must enter a Traj File Name! ##\n")
        richTextTC.see(END)
    else:
        FILE_swabs = FILE+"-SWabs.txt"
        FILE = FILE+".txt"
    
        try:
           gettext(ftp, FILE) 
        except ftplib.error_perm:
            richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )

            richTextTC.insert(END,"\n##Error: FILE not Found: %s"% FILE)
            richTextTC.see(END)
            os.unlink(FILE)
        try:
           gettext_swabs(ftp1, FILE_swabs)
        except ftplib.error_perm:
            richTextTC.insert(END,"\n------------------------------------------------------------------------------------" )
            richTextTC.insert(END,"\n##Error: FILE(sw abstraction) not Found: %s"% FILE_swabs)
            richTextTC.see(END)
            os.unlink(FILE_swabs)
    richTextTC.see(END)        
    ftp.quit()
    ftp1.quit()
    
def buttonKillClick(): #STOP

  richTextBox1.insert(1.0,"\n# Kill the Positioners!\n")
  [errorCode, returnString] = XY.GroupKill(socketId, group)
  [errorCode, returnString] = SingleZ.GroupKill(socketIdz, z)
  [errorCode, returnString] = SingleAct.GroupKill(socketIdAct, act)
  if (errorCode != 0):
    displayErrorAndClose (socketId, errorCode, 'GroupKill')
    sys.exit ()


def buttonHomeClick(): #Inicializacao dos posicionadores
##  [errorCode, returnString] = XY.GroupKill(socketId, group)
##  [errorCode, returnString] = SingleZ.GroupKill(socketIdz, z)
##  if (errorCode != 0):
##    displayErrorAndClose (socketId, errorCode, 'GroupKill')
##    sys.exit ()

# Initialize the group
  [errorCode, returnString] = XY.GroupInitialize(socketId, group)
  [errorCode, returnString] = SingleZ.GroupInitialize(socketIdz, z)
  [errorCode, returnString] = SingleAct.GroupInitialize(socketIdAct, act)
  if ( errorCode != 0):
      displayErrorAndClose (socketId, errorCode, 'GroupInitialize')
      sys.exit ()

   # Home search
  velocidade = float(50)
  aceleracao = float(20)
  jerktime = float(0.04)
  
  [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, velocidade, aceleracao, jerktime, jerktime)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, velocidade, aceleracao, jerktime, jerktime)
  
  [errorCode, returnString] = XY.GroupHomeSearch(socketId, group)
  [errorCode, returnString] = SingleZ.GroupHomeSearch(socketId, z)
  [errorCode, returnString] = SingleAct.GroupHomeSearch(socketIdAct, act)
  if (errorCode != 0):
      displayErrorAndClose (socketId, errorCode, 'GroupHomeSearch')
      sys.exit()
##MOVE to GUIDE -
  [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
  [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y
  velocidade = float(0.1)
  aceleracao = float(0.8)
  jerktime = float(0.02)
    
  [errorCode, returnString] = SingleAct.PositionerSGammaParametersSet (socketIdAct, positionerAct, velocidade, aceleracao, jerktime, jerktime)
  [errorCode, returnString] = SingleAct.GroupMoveAbsolute(socketIdAct, positionerAct, [0.0])
  [errorCode, returnString] = SingleZ.GroupMoveAbsolute(socketIdz, positionerz, [0.0])
  richTextInit.insert(END,"\n--------------------------------------------------------------" )
  richTextInit.insert(END,"# Initialize the Positioners\n")
  richTextInit.insert(END,"\n# Moved to **GUIDE Positions!")
  richTextInit.see(END)
 
 
def buttonHomeClick2(): #Home positions, X, Y ; Z ; Act.
  velocidade = float(50)
  aceleracao = float(20)
  jerktime = float(0.04)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, velocidade, aceleracao, jerktime, jerktime)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, velocidade, aceleracao, jerktime, jerktime)
 

##MOVE to GUIDE -
  [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
  [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y
  [errorCode, returnString] = SingleZ.GroupMoveAbsolute(socketIdz, positionerz, [0.0])
  velocidade = float(0.1)
  aceleracao = float(0.8)
  jerktime = float(0.02)   
  [errorCode, returnString] = SingleAct.PositionerSGammaParametersSet (socketIdAct, positionerAct, velocidade, aceleracao, jerktime, jerktime)
  [errorCode, returnString] = SingleAct.GroupMoveAbsolute(socketIdAct, positionerAct, [3.0])
  richTextInit.insert(END,"\n--------------------------------------------------------------" )
  richTextInit.insert(END,"\n# Moved to **GUIDE!\n")
  richTextInit.insert(END,"\n# Home the Positioners")
  richTextInit.see(END)


def verificar_statusXY():
    [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
    if ( (GroupStatus >= 10) and (GroupStatus <= 18) ): # de 10 a 18: ready state ..
        x = int(1)
        return x
    else:
        if ( (GroupStatus >= 20) and (GroupStatus <= 38) ): # de 20 a 38: disable state ..
            
            return 2

        else:
            return 0 #not ready; not disabled state.



def verificar_statusXY_Init(): #abaInit 
    [Error, GroupStatus] = XY.GroupStatusGet(socketId, group)
    [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
    if ( (GroupStatus >= 10) and (GroupStatus <= 18) ): # de 10 a 18: ready state ..
        x = int(1)
        return x
    else:
        richTextInit.insert(END,"\n--------------------------------------------------------------" )
        if ( (GroupStatus >= 20) and (GroupStatus <= 38) ): # de 20 a 38: disable state ..
            
            richTextInit.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners'!#\n")
            richTextInit.see(END)
            return int(2)

        else:
            
            if (GroupStatus == 42):
                richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextInit.insert(END,"\n## You must click in - 'Move to Origin'!!#\n")
                richTextInit.see(END)
                return int(3)
                
            else:
                richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextInit.insert(END,"\n## You must click in - 'Positioners Initialization'!#\n")
                richTextInit.see(END)
                return int(0) #not ready; not disabled state. 

################################################################################################################################
################################################################################################################################

def verificar_statusXY_Basic(): #usada em todas as setas e 'go shift'
    
    [Error, GroupStatus] = XY.GroupStatusGet(socketId, group)
    [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
    if ( (GroupStatus >= 10) and (GroupStatus <= 18) ): # de 10 a 18: ready state ..
        x = int(1)
        return x
    else:
        richTextBasic.insert(END,"\n--------------------------------------------------------------" )
        if ( (GroupStatus >= 20) and (GroupStatus <= 38) ): # de 20 a 38: disable state ..
            
            richTextBasic.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners' (Tab 'Initialization')!#\n")
            richTextBasic.see(END)
            return int(2)

        else:
            
            if (GroupStatus == 42):
                richTextBasic.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextBasic.insert(END,"\n## You must click in - 'Move to Origin'!!#\n")
                richTextBasic.see(END)
                return int(3)
                
            else:
                richTextBasic.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextBasic.insert(END,"\n## You must click in - 'Positioners Initialization' (Tab 'Initialization')!#\n")
                richTextBasic.see(END)
                return int(0) #not ready; not disabled state.

################################################################################################################################
################################################################################################################################

def verificar_statusXY_TE():#usada em todas as setas e 'go shift'
    
    [Error, GroupStatus] = XY.GroupStatusGet(socketId, group)
    [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
    if ( (GroupStatus >= 10) and (GroupStatus <= 18) ): # de 10 a 18: ready state ..
        x = int(1)
        return x
    else:
        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
        if ( (GroupStatus >= 20) and (GroupStatus <= 38) ): # de 20 a 38: disable state ..
            
            richTextBox1.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners' (Tab 'Initialization')!#\n")
            richTextBox1.see(END)
            return int(2)

        else:
            
            if (GroupStatus == 42):
                richTextBox1.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextBox1.insert(END,"\n## You must click in - 'Move to Origin'(Tab Basic) OR 'Move to Home Positions'(Tab Initialization)!!#\n")
                richTextBox1.see(END)
                return int(3)
                
            else:
                richTextBox1.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextBox1.insert(END,"\n## You must click in - 'Positioners Initialization' (Tab 'Initialization')!#\n")
                richTextBox1.see(END)
                return int(0) #not ready; not disabled state.

def verificar_statusXY_TE():#usada em todas as setas e 'go shift'
    
    [Error, GroupStatus] = XY.GroupStatusGet(socketId, group)
    [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
    if ( (GroupStatus >= 10) and (GroupStatus <= 18) ): # de 10 a 18: ready state ..
        x = int(1)
        return x
    else:
        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
        if ( (GroupStatus >= 20) and (GroupStatus <= 38) ): # de 20 a 38: disable state ..
            
            richTextBox1.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners' (Tab 'Initialization')!#\n")
            richTextBox1.see(END)
            return int(2)

        else:
            
            if (GroupStatus == 42):
                richTextBox1.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextBox1.insert(END,"\n## You must click in - 'Move to Origin'(Tab Basic) OR 'Move to Home Positions'(Tab Initialization)!!#\n")
                richTextBox1.see(END)
                return int(3)
                
            else:
                richTextBox1.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextBox1.insert(END,"\n## You must click in - 'Positioners Initialization' (Tab 'Initialization')!#\n")
                richTextBox1.see(END)
                return int(0) #not ready; not disabled state.


def verificar_statusXY_ImgP(): #aba img proc sobel
    [Error, GroupStatus] = XY.GroupStatusGet(socketId, group)
    [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
    if ( (GroupStatus >= 10) and (GroupStatus <= 18) ): # de 10 a 18: ready state ..
        x = int(1)
        return x
    else:
        richTextImgP.insert(END,"\n--------------------------------------------------------------" )
        if ( (GroupStatus >= 20) and (GroupStatus <= 38) ): # de 20 a 38: disable state ..
            
            richTextImgP.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners'!#\n")
            richTextImgP.see(END)
            return int(2)

        else:
            
            if (GroupStatus == 42):
                richTextImgP.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextImgP.insert(END,"\n## You must click in - 'Move to Origin'!!#\n")
                richTextImgP.see(END)
                return int(3)
                
            else:
                richTextImgP.insert(END,"\n##XY status: %s"% GroupStatusString)
                richTextImgP.insert(END,"\n## You must click in - 'Positioners Initialization'!#\n")
                richTextImgP.see(END)
                return int(0) #not ready; not disabled state.
            
def buttonInit_novo(): #Inicializacao dos posicionadores ##    (frame_aba2,text='  Positioners \n Initialization', ..
# Initialize the group
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
  [Error1, GroupStatus1] = SingleAct.GroupStatusGet (socketIdAct, act)
  [Error2, GroupStatus2] = SingleZ.GroupStatusGet (socketIdz, z)
##  print ("GroupStatus XYZ: ", GroupStatus)
##  print ("GroupStatus Actuator: ", GroupStatus1)
      
  if ( (GroupStatus >= 0) and (GroupStatus <= 9) ): #0 not intit; 1a9 not init due something - p.482 manual program.
      [errorCode, returnString] = XY.GroupInitialize(socketId, group)        
      if ( Error != 0) :
          displayErrorAndClose (socketId, Error, 'GroupInitialize')
          displayErrorAndClose (socketIdAct, Error1, 'GroupInitialize')
          [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
          sys.exit ()
  else:
      if ( (GroupStatus >= 20) and (GroupStatus <=38) ): #20: disable; 21a38 : Disable due something p.482 manual program.
          [errorCode, returnString] = XY.GroupMotionEnable(socketId, group)
          [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
          richTextInit.see(END)


  if ( (GroupStatus1 >= 0) and (GroupStatus1 <= 9)):      
      [errorCode1, returnString1] = SingleAct.GroupInitialize(socketIdAct, act)
      if (errorCode1 != 0):      
          displayErrorAndClose (socketIdAct, errorCode1, 'GroupInitialize')
          sys.exit ()
  [Error1, GroupStatus1] = SingleAct.GroupStatusGet (socketIdAct, act)
  
  if ( (GroupStatus2 >= 0) and (GroupStatus2 <= 9)):      
      [errorCode2, returnString2] = SingleZ.GroupInitialize(socketIdz, z)
      if (errorCode2 != 0):      
          displayErrorAndClose (socketIdz, errorCode2, 'GroupInitialize')
          sys.exit ()
  [Error2, GroupStatus2] = SingleZ.GroupStatusGet (socketIdz, z)

  
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)  
  if (GroupStatus == 42) : #42: not referenced state. Need press "HOME" button - p.482 manual program.
      velocidade = float(50)
      aceleracao = float(20)
      jerktime = float(0.04)
      
      [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, velocidade, aceleracao, jerktime, jerktime)
      [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, velocidade, aceleracao, jerktime, jerktime)
      [errorCode, returnString] = XY.GroupHomeSearch(socketId, group)
      
      #**** statusGET
      
####MOVE to GUIDE -
      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y      
      richTextInit.insert(END,"\n--------------------------------------------------------------" )
      richTextInit.insert(END,"\n## Initialize the Positioners X and Y.\n")
      richTextInit.insert(END,"\n# Moved XY to **GUIDE Positions!\n")
      richTextInit.see(END)      
      if (errorCode != 0):
          displayErrorAndClose (socketId, errorCode, 'GroupHomeSearch')
          sys.exit()
     
  if ((GroupStatus1 >= 20) and (GroupStatus1 <= 41) ) : #42: not referenced state. Need press "HOME" button - p.482 manual program.
      [errorCode1, returnString1] = SingleAct.GroupMotionEnable(socketIdAct, act)
      [Error1, GroupStatus1] = SingleAct.GroupStatusGet (socketIdAct, act)
      
  if (GroupStatus1 == 42) :
      velocidade = float(0.2)
      aceleracao = float(0.8)
      jerktime = float(0.02)  
      [errorCode1, returnString] = SingleAct.GroupHomeSearch(socketIdAct, act)
      [errorCode1, returnString] = SingleAct.PositionerSGammaParametersSet (socketIdAct, positionerAct, velocidade, aceleracao, jerktime, jerktime)
      [errorCode1, returnString] = SingleAct.GroupMoveAbsolute(socketIdAct, positionerAct, [0.0])
      richTextInit.insert(END,"# Actuator moved to Home Position \n")      
      richTextInit.see(END)      
      if ( errorCode1 != 0):      
          displayErrorAndClose (socketIdAct, errorCode1, 'GroupInitialize')
          sys.exit ()
          
  if ((GroupStatus2 >= 20) and (GroupStatus2 <= 41) ) :
      [errorCode2, returnString2] = SingleZ.GroupMotionEnable(socketIdz, z)
      [Error2, GroupStatus2] = SingleZ.GroupStatusGet (socketIdz, z)
      
  if (GroupStatus2 == 42) : #42: not referenced state. Need press "HOME" button - p.482 manual program.
      velocidade = float(5)
      aceleracao = float(20)
      jerktime = float(0.04)  
      [errorCode2, returnString] = SingleZ.GroupHomeSearch(socketIdz, z)
      [errorCode2, returnString] = SingleZ.PositionerSGammaParametersSet (socketIdz, positionerz, velocidade, aceleracao, jerktime, jerktime)
      [errorCode2, returnString] = SingleZ.GroupMoveAbsolute(socketIdz, z, [0.0])
      richTextInit.insert(END,"# Positioner Z moved to Home Position \n")      
      richTextInit.see(END)      
      if ( errorCode2 != 0):      
          displayErrorAndClose (socketIdAct, errorCode1, 'GroupInitialize')
          sys.exit ()
          
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
  [Error1, GroupStatus1] = SingleAct.GroupStatusGet (socketIdAct, act)
  [Error2, GroupStatus2] = SingleZ.GroupStatusGet (socketIdz, z)

  [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
  [Error1, GroupStatusString1] = SingleAct.GroupStatusStringGet(socketIdAct,GroupStatus1)
  [Error2, GroupStatusString2] = SingleZ.GroupStatusStringGet(socketIdz,GroupStatus2)
  richTextInit.insert(END,"\n--------------------------------------------------------------" )
  richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
  richTextInit.insert(END,"\n##Z status: %s"% GroupStatusString2)
  richTextInit.insert(END,"\n##Act status: %s\n"% GroupStatusString1)
  richTextInit.see(END)      


def buttonInit_novo_2_Disable(): #antes de desabilitar, verificar X e Y - caso estejam @ "not initialized states"
# Initialize the group
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
  [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
  richTextInit.insert(END,"\n--------------------------------------------------------------" )
  
  richTextInit.see(END)   
 
      
  if ( (GroupStatus >= 0) and (GroupStatus <= 9) ): #0 not intit; 1a9 not init due something - p.482 manual program. 
      richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
      richTextInit.insert(END,"\n## You must click in - 'Positioners Initialization'!!\n")
      richTextInit.see(END)   


  else:
      if ( (GroupStatus >= 20) and (GroupStatus <=38) ): #20: disable; 21a38 : Disable due something p.482 manual program.
          richTextInit.insert(END,"\n## It's already 'Disable state'!\n")
          richTextInit.see(END)
      else:
          if (GroupStatus == 42) : #42: not referenced state. Need press "HOME" button - p.482 manual program.
              richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
              richTextInit.insert(END,"\n## You must click in - 'Move to Home Positions'!! \n")
              richTextInit.see(END)
          else:
              [errorCode, returnString] = XY.GroupMotionDisable(socketId, group)
              [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
              [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
              richTextInit.insert(END,"\n##XY status: %s \n" % GroupStatusString)


def buttonInit_novo_2_Enable(): #antes de habilitar, verificar X e Y - caso estejam @ "not initialized states"
# Initialize the group
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
  [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
  richTextInit.insert(END,"\n--------------------------------------------------------------" )
  
  richTextInit.see(END)   
 
      
  if ( (GroupStatus >= 0) and (GroupStatus <= 9) ): #0 not intit; 1a9 not init due something - p.482 manual program. 
      richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
      richTextInit.insert(END,"\n## You must click in - 'Positioners Initialization'!!\n")
      richTextInit.see(END)   


  else:
      if ( (GroupStatus >= 10) and (GroupStatus <=18) ): #10 a 18 ready state; 21a38 : Disable due something p.482 manual program.
          richTextInit.insert(END,"\n## It's already 'Enable state'!\n")
          
          richTextInit.see(END)
      else:
          if (GroupStatus == 42) : #42: not referenced state. Need press "HOME" button - p.482 manual program.
              
              richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
              richTextInit.insert(END,"\n## You must click in - 'Move to Home Positions'!! \n")
              richTextInit.see(END)
          else:
              [errorCode, returnString] = XY.GroupMotionEnable(socketId, group)
              [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
              [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
              richTextInit.insert(END,"\n##XY status: %s \n" % GroupStatusString)
  
def buttonHomeClick2_novo(): #Home positions, X, Y ; Z ; Act. - (frame_aba2,text='Move to HOME \n      Positions ', command=buttonHomeClick2
    
#Move to HOME Positions (aba Init) aba2.
    
  velocidade = float(50)
  aceleracao = float(20)
  jerktime = float(0.04)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet(socketId, positionerx, velocidade, aceleracao, jerktime, jerktime)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet(socketId, positionery, velocidade, aceleracao, jerktime, jerktime)
  
  status = verificar_statusXY()
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
  [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
  richTextInit.insert(END,"\n--------------------------------------------------------------" )
  
  
##  richTextInit.insert(END,"\n# status: %d" %status)  
  if (status == 1): #Ok ready state
      
 
    ##MOVE to GUIDE -
      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y
    ##  [errorCode, returnString] = XTZ.GroupMoveAbsolute(socketIdXYZ, positionerz, [0.0])
    ##  velocidade = float(0.1)
    ##  aceleracao = float(0.8)
    ##  jerktime = float(0.02)
    ##  [errorCode, returnString] = SingleAct.PositionerSGammaParametersSet (socketIdAct, positionerAct, velocidade, aceleracao, jerktime, jerktime)
    ##  [errorCode, returnString] = SingleAct.GroupMoveAbsolute(socketIdAct, positionerAct, [0.0])
      
      richTextInit.insert(END,"\n# Moved to **GUIDE!\n")
      [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
      [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
      richTextInit.insert(END,"\n##XY status: %s \n"% GroupStatusString)
      richTextInit.see(END)
  else:
      
      if (GroupStatus == 42): #not referenced state - need HOME command
          [errorCode, returnString] = XY.GroupHomeSearch(socketId, group)
          
          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y
          
          richTextInit.insert(END,"\n# Moved to **GUIDE!\n")
          [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
          [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
          richTextInit.insert(END,"\n##XY status: %s \n"% GroupStatusString)
          richTextInit.see(END)

      else:
          
          if (status == 2): #disable
    ##          richTextInit.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
              
              richTextInit.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners' button!#\n")
              richTextInit.see(END)
          else:
        

              ##(status == 0): #NAO estao prontos para mov. NOT ready state (Ready state: cods: de 10 a 18).
              richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
              richTextInit.insert(END,"\n## You must click in - 'Positioners Initialization'!!")
              richTextInit.see(END)



def buttonHomeClickBasic(): #ABA 3 basic Apenas X e Y  #"Move to Origin"
    
#Move to ORIGIN (aba basic Init) aba3.
    
  velocidade = float(50)
  aceleracao = float(20)
  jerktime = float(0.04)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet(socketId, positionerx, velocidade, aceleracao, jerktime, jerktime)
  [errorCode, returnString] = XY.PositionerSGammaParametersSet(socketId, positionery, velocidade, aceleracao, jerktime, jerktime)
  
  status = verificar_statusXY()
  [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
  [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
  richTextBasic.insert(END,"\n--------------------------------------------------------------" )
  
  
##  richTextInit.insert(END,"\n# status: %d" %status)  
  if (status == 1): #Ok ready state
      
 
    ##MOVE to GUIDE -
      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
      [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y
    ##  [errorCode, returnString] = XTZ.GroupMoveAbsolute(socketIdXYZ, positionerz, [0.0])
    ##  velocidade = float(0.1)
    ##  aceleracao = float(0.8)
    ##  jerktime = float(0.02)
    ##  [errorCode, returnString] = SingleAct.PositionerSGammaParametersSet (socketIdAct, positionerAct, velocidade, aceleracao, jerktime, jerktime)
    ##  [errorCode, returnString] = SingleAct.GroupMoveAbsolute(socketIdAct, positionerAct, [0.0])
      
      richTextBasic.insert(END,"\n# Moved to **GUIDE!\n")
      richTextBasic.insert(END,"\n##XY status: %s\n"% GroupStatusString)
      richTextBasic.see(END)
  else:
      
      if (GroupStatus == 42): #not referenced state - need HOME command
          [errorCode, returnString] = XY.GroupHomeSearch(socketId, group)
          
          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx]) #inic eixo X
          [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [GUIAy]) #inic eixo Y
          
          richTextBasic.insert(END,"\n# Moved to **GUIDE!\n")
          [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
          [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
          richTextBasic.insert(END,"\n##XY status: %s \n"% GroupStatusString)
          richTextBasic.see(END)

      else:
          
          if (status == 2): #disable
    ##          richTextInit.insert(END,"\n# X and Y Positioners status: DISABLE, \nGo to Initialization Tab and use 'Enable Positioners' button. #\n")
              
              richTextBasic.insert(END,"\n# X and Y Positioners status: DISABLE, \n# Click in - 'Enable Positioners' (Tab 'Initialization')!#\n")
              richTextBasic.see(END)
          else:
        

              ##(status == 0): #NAO estao prontos para mov. NOT ready state (Ready state: cods: de 10 a 18).
              richTextBasic.insert(END,"\n##XY status: %s"% GroupStatusString)
              richTextBasic.insert(END,"\n## You must click in - 'Positioners Initialization' (Tab 'Initialization')!#")
              richTextBasic.see(END)


  
  


def verificar_status_todos():
    [Error, GroupStatus] = XY.GroupStatusGet (socketId, group)
    [Error1, GroupStatus1] = SingleAct.GroupStatusGet (socketIdAct, act)
    [Error1, GroupStatus2] = SingleZ.GroupStatusGet (socketIdz, z)
    [Error, GroupStatusString] = XY.GroupStatusStringGet (socketId,GroupStatus)
    [Error2, GroupStatusString2] = SingleAct.GroupStatusStringGet(socketIdAct,GroupStatus1)
    [Error3, GroupStatusString3] = SingleZ.GroupStatusStringGet(socketIdz,GroupStatus2)


    richTextInit.insert(END,"\n--------------------------------------------------------------" )
    richTextInit.insert(END,"\n##XY status: %s"% GroupStatusString)
    richTextInit.insert(END,"\n##Z status: %s"% GroupStatusString3)
    richTextInit.insert(END,"\n##Act status: %s"% GroupStatusString2)
    richTextInit.see(END)   

def buttonDisable():  
##    integer GroupMotionDisable(integer SocketID, string GroupName) 
##    buttonInit_novo()
    buttonInit_novo_2_Disable()
##    [errorCode, returnString] = XY.GroupMotionDisable(socketId, group)
##    richTextInit.insert(END,"\n--------------------------------------------------------------" )
##    richTextInit.insert(END,"\n# Disable X and Y Positioners\n")
    richTextInit.see(END)



def buttonEnable():
    buttonInit_novo_2_Enable()
    richTextInit.see(END)   


def bDicas():
  richTextBox1.insert(1.0,"\n------------------------------------------------------------------------------------\n")
  richTextBox1.insert(1.0,"\n#Arco for Down: Negative Angle")
  richTextBox1.insert(1.0,"\n#Arco for Up: Positite Angle ")
  richTextBox1.insert(1.0,"\n#Arc (Radius[mm], Angle[degrees])")
  richTextBox1.insert(1.0,"\n#Line(X,Y) coordinates[mm]")
  richTextBox1.insert(1.0,"\n----------------------------------------Tips----------------------------------------")


def buttonFoco():
    velocidade = float(5)
    aceleracao = float(20)
    jerktime = float(0.04)  
    [errorCode2, returnString] = SingleZ.PositionerSGammaParametersSet (socketIdz, positionerz, velocidade, aceleracao, jerktime, jerktime)


    [Error1, GroupStatusZ] = SingleZ.GroupStatusGet (socketIdz, z)
    [Error2, GroupStatusStringZ] = SingleZ.GroupStatusStringGet(socketIdz,GroupStatusZ)
    
    richTextInit.see(END)
    
    v = textBoxFoco.get()
    richTextInit.insert(END,"\n--------------------------------------------------------------" )
    if ((v == "") or (v ==" ")):
          richTextInit.insert(END,"\n#You must enter a Value in TextBox ! \n")
          richTextInit.see(END)
    else:
      v = float(textBoxFoco.get())
      if ((v<-2.4) or (v>+2.4)):
          richTextInit.insert(END,"\n# Focus values: [-2.4 e + 2.4]mm \n")
          richTextInit.see(END)
    ##    if (checkTEa==1):
    ##      richText.insert(1.0,"\n# Focus values: [-2.4 e + 2.4]mm \n")      
      else:
          if not ((GroupStatusZ >= 10) and (GroupStatusZ <= 18)):
              richTextInit.insert(END,"\n##Z status: %s"% GroupStatusStringZ)
              richTextInit.insert(END,"\n## You must click in - 'Positioners Initialization'!#\n")
              richTextInit.see(END)

          else:
              
              [errorCode, returnString] = SingleZ.GroupMoveAbsolute(socketIdz, positionerz, [v]) #inic eixo Z
              [errorCode, currentPosition] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
              richTextInit.insert(END,"\n#Vertical Positioner moved to: %.2f [mm]\n" %currentPosition)
              richTextInit.see(END)
    
###############################################################################################################
def buttonAtuador():    
    velocidade = float(0.1)
    aceleracao = float(0.8)
    jerktime = float(0.02)
##    [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, velocidade, aceleracao, jerktime, jerktime)

    [Error1, GroupStatusACT] = SingleAct.GroupStatusGet (socketIdAct, act)
    [Error2, GroupStatusStringACT] = SingleAct.GroupStatusStringGet(socketIdAct,GroupStatusACT)
    
    richTextInit.insert(END,"\n--------------------------------------------------------------" )
    v = movAtuador.get()
    if ((v == "") or (v ==" ")):
          richTextInit.insert(END,"\n#You must enter a Value in TextBox ! \n")
          richTextInit.see(END)
    else:
        v = float(movAtuador.get())
        if ((v<0) or (v>+25)):
            richTextInit.insert(END,"\n#Actuator values: [0.0 + 25.0]mm \n")
            richTextInit.see(END)
        else:
            if not ((GroupStatusACT >= 10) and (GroupStatusACT <= 18)):
              richTextInit.insert(END,"\n##Act status: %s"% GroupStatusStringACT)
              richTextInit.insert(END,"\n## You must click in - 'Positioners Initialization'!#\n")
              richTextInit.see(END)
            else:                
                [errorCode, returnString] = SingleAct.GroupMoveAbsolute(socketIdz, positionerAct, [v]) #inic atuador
                [errorCode, currentPosition] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                richTextInit.insert(END,"\n#Actuator moved to: %.2f [mm]\n" %currentPosition)
                richTextInit.see(END)

###############################################################################################################
#movimentos relativos #movimentos relativos#movimentos relativos #movimentos relativos #movimentos relativos
###############################################################################################################
#movimentos relativos #movimentos relativos#movimentos relativos #movimentos relativos #movimentos relativos
###############################################################################################################
def Ypos():# ABA 5 traj exec ++Y++
    status = verificar_statusXY_TE()
    if (status ==1):
        
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelative.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime) 

        mov = textMovRel.get() # ++y++
        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
        if ((mov == " ") or (mov == "")):
            richTextBox1.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBox1.see(END)
        else:
            mov = float(textMovRel.get())# ++y++
            fator = float(fatorUn)#  ++y++
            
            if ((mov<=0) or (mov>(400*fator))):#  ++y++
                    richTextBox1.insert(END,"\n#Movement values: (0, 400]mm \n") #  ++y++ ++y++ ++y++ ++y++
                    richTextBox1.see(END)
            else:                        
                    [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionery, 1) #  ++y++
                    limiteYneg = (currentPosition*fatorUn) - mov/fator#  ++y++
                    if (limiteYneg > (-200.00*fator)):#  ++y++
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionery, [-mov/fator]) #  ++y++

                          if (fator == 1.0): #++y++
                              richTextBox1.insert(END,"\n#Positioner Y moved to: '↑'(%.5f) mm\n" %mov)#  ++y Y y Y y Y ++
                              richTextBox1.see(END)
                          else:
                               richTextBox1.insert(END,"\n#Positioner Y moved to: '↑'(%.5f) µm\n" %mov)#  ++y++
                               richTextBox1.see(END)

                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1) #++y++
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            
                          richTextBox1.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBox1.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBox1.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBox1.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBox1.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")# ++y y y Y ++
                        
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):# ++y++
                              
                              richTextBox1.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBox1.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBox1.see(END) #++y++
                     
                    else:
                      maximo_mov = 200*fator - ((currentPosition*-1)*fatorUn)
                      richTextBox1.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)# Y negativo
                      richTextBox1.see(END)

###############################################################################################################
def Xpos():  #ABA 5 traj exec ++xis++
    status = verificar_statusXY_TE()
    if (status ==1):
            
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelative.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
        
        #  #ABA 5 traj ++Xis++
        mov = textMovRel.get() ## ++Xis++
        richTextBox1.insert(END,"\n--------------------------------------------------------------" ) 
        if ((mov == " ") or (mov == "")):
            richTextBox1.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBox1.see(END)
        else:
            mov = float(textMovRel.get())#++Xis++
            fator = float(fatorUn)# ++Xis++
            if ( (mov<=0) or (mov>(400*fator)) ): #++Xis++
                    richTextBox1.insert(END,"\n#Movement values: (0, 400]mm \n") # ++Xis++
                    richTextBox1.see(END)
            else:   
     
                    [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionerx, 1) #++Xis++
                    limite = (currentPosition*fatorUn) - mov # ++Xis++
                    if (limite > -200.00*fator): # ++Xis++
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionerx, [-mov/fator]) # ++Xis++
                          if (fator == 1):
                              richTextBox1.insert(END,"\n#Positioner X moved to: '→'(%.5f) mm\n" %mov)# ++Xis++
                              richTextBox1.see(END)
                          else:
                               richTextBox1.insert(END,"\n#Positioner X moved to: '→'(%.5f) µm\n" %mov)# ++Xis++
                               richTextBox1.see(END)
                            
                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            
                          richTextBox1.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBox1.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBox1.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBox1.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBox1.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n") #++Xis++
                        #++Xis++
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):#++Xis++
                              
                              richTextBox1.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBox1.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBox1.see(END)
                    else:# ++Xis++
                      maximo_mov = 200*fatorUn - (currentPosition*-1)*fatorUn
                      richTextBox1.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)# ++Xis++
                      richTextBox1.see(END)
###############################################################################################################
def Yneg(): #aba5 traj exec y neg --y-- y negativo
    status = verificar_statusXY_TE()
    if (status ==1):
            
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelative.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
        mov = textMovRel.get() # Y, y neg
        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
        if ((mov == " ") or (mov == "")):
            richTextBox1.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBox1.see(END)
        else:
            mov = float(textMovRel.get())# Y, y neg
            fator = float(fatorUn)# Y, y neg
            if ((mov<=0) or (mov>(400*fator))): # Y, y neg
                    richTextBox1.insert(END,"\n#Movement values: (0, 400]mm \n") # Y, y neg --y --
                    richTextBox1.see(END)
            else:

                
                  [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionery, 1) # Y, y neg
                  limite = (currentPosition * fatorUn) - (mov*-1) # Y, y neg
                  if (limite < (200.00*fator)): # Y, y neg
                  
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionery, [mov/fator]) # Y, y neg

                          if (fator == 1.0):  
                              richTextBox1.insert(END,"\n#Positioner Y moved to: '↓'(%.5f) mm\n" %mov)# Y, y neg
                              richTextBox1.see(END)
                          else:
                               richTextBox1.insert(END,"\n#Positioner Y moved to: '↓'(%.5f) µm\n" %mov)# Y, y neg                       
                               richTextBox1.see(END)                      
                          
                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            #Y, y neg
                          richTextBox1.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBox1.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBox1.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBox1.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBox1.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
                        
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                              
                              richTextBox1.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBox1.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBox1.see(END)                                       
                      
                  else:# --ipsilon-- Y, y neg
                          maximo_mov = 200*fator - (currentPosition*fatorUn) #Y, y neg
                          richTextBox1.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)# --ipsilon-- Y, y neg
                          richTextBox1.see(END)
                      
###############################################################################################################
def Xneg(): # ABA 5 traj exec Xis.negativo --xis--
    
    status = verificar_statusXY_TE()
    if (status ==1):
                     
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelative.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
        
        mov = textMovRel.get() #
        richTextBox1.insert(END,"\n--------------------------------------------------------------" )
        if ((mov == " ") or (mov == "")):
            richTextBox1.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBox1.see(END)
        else:
            mov = float(textMovRel.get())# 
            fator = float(fatorUn)# 
            if ((mov<=0) or (mov>400*fator)): # --Xis--
                    richTextBox1.insert(END,"\n#Movement values: (0, 400]mm \n") # --Xis--
                    richTextBox1.see(END)
            else:
                
     
                    [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionerx, 1) # --Xis--
                
                    limite = (currentPosition*fatorUn) - (mov*-1) #  --Xis--
                    if (limite < (200.00*fator)): #  --Xis--
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionerx, [mov/fator]) # --Xis--
                          if (fator == 1):
                              richTextBox1.insert(END,"\n#Positioner X moved to: '←'(%.5f) mm\n" %mov)#  --Xis--
                              richTextBox1.see(END)
                          else:
                               richTextBox1.insert(END,"\n#Positioner X moved to: '←'(%.5f) µm\n" %mov)#  --Xis--
                               richTextBox1.see(END)
                            
                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            
                          richTextBox1.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBox1.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBox1.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBox1.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBox1.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
                        
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                              
                              richTextBox1.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBox1.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBox1.see(END)
                    else:# ++Xis++
                      maximo_mov = 200*fator - (currentPosition*fatorUn) # --Xis--
                      richTextBox1.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)#  --Xis--
                      richTextBox1.see(END)
                  
###############################################################################################################
###############################################################################################################
# MOV relativos aba 3 basic
###############################################################################################################
###############################################################################################################

def YposBasic():# ABA 3 basic ++Y++
    status = verificar_statusXY_Basic()
    if (status ==1):
        
    
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelativeBasic.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime) 

        mov = textMovRelBasic.get() # ++y++
        richTextBasic.insert(END,"\n--------------------------------------------------------------" )
        if ((mov == " ") or (mov == "")):
            richTextBasic.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBasic.see(END)
        else:
            mov = float(textMovRelBasic.get())# ++y++
            fator = float(fatorUnBasic)#  ++y++
            
            if ((mov<=0) or (mov>(400*fator))):#  ++y++
                    richTextBasic.insert(END,"\n#Movement values: (0, 400]mm \n") #  ++y++ ++y++ ++y++ ++y++
                    richTextBasic.see(END)
            else:                        
                    [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionery, 1) #  ++y++
                    limiteYneg = (currentPosition*fatorUnBasic) - mov/fator#  ++y++
                    if (limiteYneg > (-200.00*fator)):#  ++y++
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionery, [-mov/fator]) #  ++y++

                          if (fator == 1.0): #++y++
                              richTextBasic.insert(END,"\n#Positioner Y moved to: '↑'(%.5f) mm\n" %mov)#  ++y Y y Y y Y ++
                              richTextBasic.see(END)
                          else:
                               richTextBasic.insert(END,"\n#Positioner Y moved to: '↑'(%.5f) µm\n" %mov)#  ++y++
                               richTextBasic.see(END)

                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1) #++y++
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            
                          richTextBasic.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBasic.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBasic.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBasic.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBasic.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")# ++y y y Y ++
                        
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):# ++y++
                              richTextBasic.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBasic.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBasic.see(END) #++y++
                     
                    else:
                      maximo_mov = 200*fator - ((currentPosition*-1)*fatorUnBasic)
                      richTextBasic.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)# Y negativo
                      richTextBasic.see(END)

###############################################################################################################
def XposBasic():  #ABA 3 basic ++xis++
    status = verificar_statusXY_Basic()
    if (status ==1):
            
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelativeBasic.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
        
        #  #ABA 5 traj ++Xis++
        mov = textMovRelBasic.get() ## ++Xis++
        richTextBasic.insert(END,"\n--------------------------------------------------------------" ) 
        if ((mov == " ") or (mov == "")):
            richTextBasic.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBasic.see(END)
        else:
            mov = float(textMovRelBasic.get())#++Xis++
            fator = float(fatorUnBasic)# ++Xis++
            if ( (mov<=0) or (mov>(400*fator)) ): #++Xis++
                    richTextBasic.insert(END,"\n#Movement values: (0, 400]mm \n") # ++Xis++
                    richTextBasic.see(END)
            else:   
     
                    [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionerx, 1) #++Xis++
                    limite = (currentPosition*fatorUnBasic) - mov # ++Xis++
                    if (limite > -200.00*fator): # ++Xis++
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionerx, [-mov/fator]) # ++Xis++
                          if (fator == 1):
                              richTextBasic.insert(END,"\n#Positioner X moved to: '→'(%.5f) mm\n" %mov)# ++Xis++
                              richTextBasic.see(END)
                          else:
                               richTextBasic.insert(END,"\n#Positioner X moved to: '→'(%.5f) µm\n" %mov)# ++Xis++
                               richTextBasic.see(END)
                            
                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            
                          richTextBasic.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBasic.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBasic.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBasic.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBasic.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n") #++Xis++
                        #++Xis++
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):#++Xis++
                              
                              richTextBasic.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBasic.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBasic.see(END)
                    else:# ++Xis++
                      maximo_mov = 200*fatorUnBasic - (currentPosition*-1)*fatorUnBasic
                      richTextBasic.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)# ++Xis++
                      richTextBasic.see(END)
###############################################################################################################

def YnegBasic(): #ABA 3 basic y neg --y-- y negativo
    status = verificar_statusXY_Basic()
    if (status ==1):
        
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelativeBasic.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
        mov = textMovRelBasic.get() # Y, y neg
        richTextBasic.insert(END,"\n--------------------------------------------------------------" )
        if ((mov == " ") or (mov == "")):
            richTextBasic.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBasic.see(END)
        else:
            mov = float(textMovRelBasic.get())# Y, y neg
            fator = float(fatorUnBasic)# Y, y neg
            if ((mov<=0) or (mov>(400*fator))): # Y, y neg
                    richTextBasic.insert(END,"\n#Movement values: (0, 400]mm \n") # Y, y neg --y --
                    richTextBasic.see(END)
            else:

                
                  [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionery, 1) # Y, y neg
                  limite = (currentPosition * fatorUn) - (mov*-1) # Y, y neg
                  if (limite < (200.00*fator)): # Y, y neg
                  
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionery, [mov/fator]) # Y, y neg

                          if (fator == 1.0):  
                              richTextBasic.insert(END,"\n#Positioner Y moved to: '↓'(%.5f) mm\n" %mov)# Y, y neg
                              richTextBasic.see(END)
                          else:
                               richTextBasic.insert(END,"\n#Positioner Y moved to: '↓'(%.5f) µm\n" %mov)# Y, y neg                       
                               richTextBasic.see(END)                      
                          
                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            #Y, y neg
                          richTextBasic.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBasic.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBasic.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBasic.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBasic.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
                        
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                              
                              richTextBasic.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBasic.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBasic.see(END)                                       
                      
                  else:# --ipsilon-- Y, y neg
                          maximo_mov = 200*fator - (currentPosition*fatorUn) #Y, y neg
                          richTextBasic.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)# --ipsilon-- Y, y neg
                          richTextBasic.see(END)
###############################################################################################################
def XnegBasic(): # ABA 3 basic Xis.negativo --xis--
    status = verificar_statusXY_Basic()
    if (status ==1):
        
        jerktime = 0.04
        aceleracao = 80
        a= (float(aceleracao))
        velocidade = velRelativeBasic.get()
        if ((velocidade == " ") or (velocidade == "")):
            velocidade = 20
        v= (float(velocidade))
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
        
        mov = textMovRelBasic.get() #
        richTextBasic.insert(END,"\n--------------------------------------------------------------" )
        if ((mov == " ") or (mov == "")):
            richTextBasic.insert(END,"\n#You must enter a Value in TextBox ! \n")
            richTextBasic.see(END)
        else:
            mov = float(textMovRelBasic.get())# 
            fator = float(fatorUnBasic)# 
            if ((mov<=0) or (mov>400*fator)): # --Xis--
                    richTextBasic.insert(END,"\n#Movement values: (0, 400]mm \n") # --Xis--
                    richTextBasic.see(END)
            else:
                
     
                    [errorCode, currentPosition] = XY.GroupPositionCurrentGet(socketId, positionerx, 1) # --Xis--
                
                    limite = (currentPosition*fatorUnBasic) - (mov*-1) #  --Xis--
                    if (limite < (200.00*fator)): #  --Xis--
                          [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionerx, [mov/fator]) # --Xis--
                          if (fator == 1):
                              richTextBasic.insert(END,"\n#Positioner X moved to: '←'(%.5f) mm\n" %mov)#  --Xis--
                              richTextBasic.see(END)
                          else:
                               richTextBasic.insert(END,"\n#Positioner X moved to: '←'(%.5f) µm\n" %mov)#  --Xis--
                               richTextBasic.see(END)
                            
                          [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                          [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                          [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
                          [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
                          rel_guiaX = float(GUIAx - currentPositionx)
                          rel_guiaY = float(GUIAy - currentPositiony)            
                          richTextBasic.insert(END,"\n# X: %.2f;   " %currentPositionx)
                          richTextBasic.insert(END," Y: %.2f;   \n" %currentPositiony)
                          richTextBasic.insert(END,"# Z: %.2f;     " %currentPositionz)
                          richTextBasic.insert(END," Act: %.2f \n" %currentPositionAct)
                          richTextBasic.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
                        
                          if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                              
                              richTextBasic.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                              richTextBasic.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
                          richTextBasic.see(END)
                    else:# ++Xis++
                      maximo_mov = 200*fator - (currentPosition*fatorUnBasic) # --Xis--
                      richTextBasic.insert(END,"\n#Exceeded Maximum Movement. Maximum: %.5f\n"%maximo_mov)#  --Xis--
                      richTextBasic.see(END)

   
###############################################################################################################
#fim mov relativos aba 3 basic
################################################################################################################
###############################################################################################################


def bCriarLogFile(): #aba 5 traj execution
  nome = nomearqLog.get()
  richTextBox1.insert(END,"\n--------------------------------------------------------------" )
  if ((nome == "") or (nome == " ")):
     richTextBox1.insert(END,"\n## You must enter a LOG File Name! ##\n")
     richTextBox1.see(END)
  else:
    nome = nome+".txt"      
    
    if (tempfile._exists(nome)):      
          richTextBox1.insert(END,"\n## Existing File. Choose a Different Name! ##\n")
          richTextBox1.see(END)
        
    else:
        w = open(nome,'w')
        conteudo_arq = richTextBox1.get(1.0, END)
        w.write(conteudo_arq)
        w.close()
        richTextBox1.insert(END,"\n# LOG File created: %s:\n" %nome)
        richTextBox1.see(END)

def bCriarLogFile_basic(): #aba 3 basic
  nome = nomearqLogBasic.get()
  richTextBasic.insert(END,"\n--------------------------------------------------------------" )
  if ((nome == "") or (nome == " ")):
     richTextBasic.insert(END,"\n## You must enter a LOG File Name! ##\n")
     richTextBasic.see(END)
  else:
    nome = nome+".txt"      
    
    if (tempfile._exists(nome)):      
          richTextBasic.insert(END,"\n## Existing File. Choose a Different Name! ##\n")
          richTextBasic.see(END)
        
    else:
        w = open(nome,'w')
        conteudo_arq = richTextBasic.get(1.0, END)
        w.write(conteudo_arq)
        w.close()
        richTextBasic.insert(END,"\n# LOG File created: %s:\n" %nome)
        richTextBasic.see(END)


###################################################################################################################################
#funcoes aba6 ie
def bCriarLogFile_img(): #aba 6 image execution
  nome = nomearqLogImg.get()
  richTextImg.insert(END,"\n--------------------------------------------------------------" )
  if ((nome == "") or (nome == " ")):
     richTextImg.insert(END,"\n## You must enter a LOG File Name! ##\n")
     richTextImg.see(END)
  else:
    nome = nome+".txt"      
    
    if (tempfile._exists(nome)):      
          richTextImg.insert(END,"\n## Existing File. Choose a Different Name! ##\n")
          richTextImg.see(END)
        
    else:
        w = open(nome,'w')
        conteudo_arq = richTextImg.get(1.0, END)
        w.write(conteudo_arq)
        w.close()
        richTextImg.insert(END,"\n# LOG File created: %s:\n" %nome)
        richTextImg.see(END)
        
def bLerArquivo():
  cor_ie = nova_cor
  print "cor ie", cor_ie
  richTextImg.insert(END,"\n--------------------------------------------------------------" )
  nome = nomearqImg.get()
  print "nova cor: " ,nova_cor
    
  if (nome == ""):
      richTextImg.insert(END,"\n## You must enter an Image File Name! ##\n")
      richTextImg.see(END)
  else:
        nome = nome +".bmp"
        try:
            
            w = open(nome,'r')
            
            richTextImg.insert(END,"\n#File selected: %s:\n" %nome)
        except:
            
            richTextImg.insert(END,"\n# Failed to read file: %s:\n" %nome)

        
        

        relacao_subs_img = (int(1))

        im = Image.open(nome)
        richTextImg.insert(END,"\n# Mode: ")
        richTextImg.insert(END,im.mode)
        modo = int (im.mode)
        if (modo == 1):
            richTextImg.insert(END,"\n# - OK! A monochromatic Image!")
        richTextImg.insert(END,"\n# Format: ")
        richTextImg.insert(END,im.format)
        

        xy = im.size
        x = xy[0]
        y = xy[1]
        richTextImg.insert(END,"\nX:  ")
        richTextImg.insert(END,x)
        richTextImg.insert(END,"\nY:  ")
        richTextImg.insert(END,y)
        x = int(x)
        y = int(y)
        substratoX= float(subsX.get())
        substratoY= float(subsY.get())
        subsx1= round( (substratoX/x),5)
        subsy1= round( (substratoY/y),5)
        richTextImg.insert(END,"\n Subsx1: %.5f \n" %subsx1)
        richTextImg.insert(END,"\n Subsy1: %.5f \n" %subsy1)
        richTextImg.insert(END,"\n--------------------------------------------------------------\n" )

        lst = list(im.getdata())
        matriz =[]
        
        a = 0 
        for j in xrange(y):
            matriz.append([])
            for i in xrange(x):
                matriz[j].append (int( (lst[a]) ))
                a = a +1
##
####apresentacao por COLUNAS
####0,0   1,0     2,0     3,0     4,0 .. 12,0
####0,1   1,1     2,1     3,1     4,1 .. 12,1
####...
####0,9   1,9     2,9     3,9     4,9 .. 12,9
##

##  -- ini   MATRIZ nao eh mais apresentada no richtext:
                
        for i in range(x): #Colunas
            for j in range(y): #Linhas
                richTextImg.insert(END,"[%d]"%j +"[%d]"%i + "= %s; ;  " %matriz[j][i])
            richTextImg.insert(END,"\n\n")
        richTextImg.insert(END,"\nJ: %d" %j)
        richTextImg.insert(END,"\ni: %d \n\n" %i)


####################################################################################################################
####################################################################################################################

def LerImagem(): #alterado para teste de Colunag com Break/pausa Funcao acima copiada para testes nessa, acima OK
    ####REDUCAO ou mesmo numero < = ::::::: passoLAteral < ou = relacao_subs_img
    nome = nomearqImg.get() #arquivo de imagem
##    relacao_subs_img = (int(1))               
    richTextImg.insert(END,"\n--------------------------------------------------------------" )
    if (nome == ""):
      
      richTextImg.insert(END,"\n## You must enter an Image File Name! ##\n")
      richTextImg.see(END)

    else:
        nome = nome+".bmp"
        im = Image.open(nome)
        richTextImg.insert(END,"\n\n ############ LEITURA DE IMAGEM ############")
        richTextImg.insert(END,"\nMode: ")
        richTextImg.insert(END,im.mode)
        richTextImg.see(END)
        xy = im.size
        x = xy[0]
        y = xy[1]
        x = int(x)
        y = int(y)
        richTextImg.insert(END,"\nX: %d \n" %x)
        richTextImg.insert(END,"\nY: %d \n" %y)
        richTextImg.see(END)

##        substratoX= float(substratoX1.get())
##        substratoY= float(substratoY1.get())
        substratoX= float(subsX.get())
        substratoY= float(subsY.get())
        subsx1= round( (substratoX/x),5)
        subsy1= round( (substratoY/y),5)
        richTextImg.insert(END,"\n Subsx1: %.5f \n" %subsx1)
        richTextImg.insert(END,"\n Subsy1: %.5f \n" %subsy1)
##        if  (((substratoX/x)) != ((substratoY/y )) ): #relacao tamanho do substrato com relacao ao tamanho da imagem
        if  (((subsx1)) != ((subsy1 )) ): #relacao tamanho do substrato com relacao ao tamanho da imagem
                richTextImg.insert(END,"\n\n# Scale Factor Value in (Substrate Size) must be the same for X and Y! \n ## Using 1.00 FOR TEST#")
                richTextImg.see(END)
                relacao_subs_img = (int(1))
        else:    
                relacao_subs_img = float(substratoX/x) #Fator de escala - relacao entre tam substrato a ser manufat e a imagem lida deve ser = entre X e Y.
                richTextImg.insert(END,"\n Relacao Substrate/Imagem: %.5f \n" %relacao_subs_img)
                richTextImg.see(END)
        
        
        lst2 = []
        lst = list(im.getdata())
        matriz =[]    
        richTextImg.insert(END,"\n\n")
        
        a = 0 
        for j in xrange(y):
            matriz.append([])
            for i in xrange(x):
                matriz[j].append (int( (lst[a]) ))
                a = a +1

        #onde tem PIXEL = 0 (pontos pretos em fundo branco - tipo MONOCROMATICO)
               
        primeiraPos = int(0)
        paradaColuna = int(0)
        numero_pausa = int(0)
        somatorioColuna = int(0)
        marcaColuna = int(0)
        somatorioVazio = int(0)
        somaTotalColunas = int(0)
        somaTotalPausas = int(0)
        numero_escritas = int(0)
                
        b = int(0)
        c = int(0)
##        global vetor_mov
##        vetor_mov= [0]*(x*2) #x eh o numero de colunas
        ############################################################ vetor_pausa = [0]*(x*2) #alterar numero maximo de posicoes
        
        
        vetor_parada = [0]*(x*2)
        vetor_n_pausa =[0]*x
        vcol = [0]*x
        vcolPosX = [0]*x

        global vcolNumEsc
        vcolNumEsc = [0]*x
        
        global vcolPosXmov 
        vcolPosXmov = [0]*x

        global vetor_mov
        vetor_mov = [0]*(x*y) #removidas abaixo posicoes desnecessarias ( del .. )
        
        global vPosY
        global vMovY
        vPosY = [0]*(x*y)
        vMovY = [0]*(x*y)

        global vetor_x
        vetor_x= [0]*(x*y)
        
        
        richTextImg.insert(END,"\n\n\n-------------")
        richTextImg.see(END)
        
##        for l in range (len(vetor_x)):    
##            richTextImg.insert(END,"\n\nV_x[%d] = "%l +"[%.2f]" %vetor_x[l]) #apresenta toda matriz de ponto inicial de X.
        
        for i in range(x): #Colunas
            
            if (somatorioColuna != 0):
                vetor_mov[b-1] = somatorioColuna * relacao_subs_img
                vMovY[c-1] = somatorioColuna * relacao_subs_img
               
                richTextImg.insert(END,"\n\nV_mov[%d] = "%(b-1) +"[%.2f] (somatorioColuna)" %vetor_mov[b-1])
                richTextImg.insert(END,"\n\n bal bla bla")
            somatorioColuna = 0
            #somatorioColuna zerado abaixo
            #vetor_parada -> 1a posicao = sim ou nao (0 ou 1); 2a posicao = numero de pausa/breaks e 3a 
                        
            marcaVazio = 0
            primeiraPosVazia = 0
            somatorioVazio = 0
            somaTotalColunas = somaTotalColunas + somatorioColuna 
            somaTotalPausas = somaTotalPausas + numero_pausa #acumulador total de breaks das colunas para dimensionar Vetor de Movimentos
##            somatorioColuna = 0
            primeiraPos = 0 #de frente para a mesa: indo para a guia!
            marcaColuna = 0
            paradaColuna = 0 #para marcar presença de dado em cada coluna (se houver, marca como 1 abaixo e identifica posicoes vazias).
##            richTextImg.insert(END,"\n\nV_parada[%d] = "%(b-2) +"[%.2f] (somatorioVazio)" %vetor_parada[b-2])
##            richTextImg.insert(END,"\n\nV_parada[%d] = "%(b-1) +"[%.2f] (somatorioVazio)" %vetor_parada[b-1])
            
##            richTextImg.insert(END,"\n\nV_pausa[%d] = "%(i-1) +"[%.2f]" %vetor_n_pausa[i-1])
            
            numero_pausa = 0 #zera numero de breaks/pausas da coluna
            numero_escritas = 0
            
            for j in range(y): #posicao das Linhas
                
                
##                vetor_mov[c] = somatorioColuna +  528.86
##                vetor_mov[b+1] = somatorioColuna
                dado = int(matriz[j][i])
                cor_ie = nova_cor
                if (dado == cor_ie):
                    vcol[i] = 1
                    vcolPosX[i] = GUIAx - (i*relacao_subs_img)
                    
                    if (marcaVazio == 1):
                        
                        richTextImg.insert(END,"\nSomatorioVazio: n (%d)"%i + "= %d" %somatorioVazio)
                        richTextImg.see(END)
                       
                        numero_pausa = numero_pausa + 1  #salvar este valor do somatorio no vetor por coluna : vetor_n_pausa
                        somatorioVazio = 0
                    
                    
                    richTextImg.insert(END,"\n\n------------------------------------")
                    richTextImg.insert(END,"\n[%d]"%j +"[%d]"%i + "= %d; ;  " %matriz[j][i])
                    somatorioColuna = somatorioColuna +1
                    richTextImg.insert(END,"\n somat.. [%d]"%j +"[%d]"%i )
                    richTextImg.insert(END,"\nSOMAT COLUNA L 835: ini apos inc : %d: " %somatorioColuna)
                    richTextImg.see(END)
                    marcaColuna = int(1) #para marcar que tem dado nesta coluna e verificar as posicoes vazias na mesma coluna
                                                
                    if (primeiraPos == 0):
                        primeiraPos = int(1)
                        primeiraPosX = i #N Coluna
                        primeiraPosY = j #N Linha
                        richTextImg.insert(END,"\nprimeriaPos X %d: " %primeiraPosX)
                        richTextImg.insert(END,"\nprimeriaPos Y %d: " %primeiraPosY)
                        mov= float( GUIAy - ((y - j)*relacao_subs_img) )#Y (0a12) -> y=13!!!
                        richTextImg.insert(END,"\n B  %d" %b)
                        richTextImg.insert(END,"\n C  %d" %c)
                        vetor_mov[b]= mov
                        vPosY[c] = mov
                        vetor_x[c] = GUIAx - (i*relacao_subs_img)                                              
                        richTextImg.insert(END,"\n\nV_x[%d] = "%c +"[%.2f]" %vetor_x[c])
                        richTextImg.insert(END,"\n y  %d" %y)
                        richTextImg.insert(END,"\n j  %d" %j)
                        richTextImg.see(END)
                        marcaPenultimaPosPreenchida = 1 # para guardar somatorio apenas ate aqui
                        numero_escritas = numero_escritas + 1
                        vcolNumEsc[i] = numero_escritas
                        b = b+2
                        c = c+1
                        
                    
                else: #dado = 255 = vazio - branco!
                    
                    primeiraPos = 0
######################################### teste de posicao vazia ######################################### ###################
                    ###################### 
######################################### #########################################  ######################################### 
                    
                    #ELSE e (if dado == 0):
                    #dado = 255 = vazio - branco!
                    if ((marcaColuna == 1)):
                        richTextImg.insert(END,"\n B out %d" %b)
                        richTextImg.insert(END,"\n C out %d" %c)
                        richTextImg.see(END)
                        
                        if (somatorioColuna >0):
                            richTextImg.insert(END,"\nSOMAT COLUNA dentro else - save : %d: " %somatorioColuna)
                            vetor_mov[b-1] = (somatorioColuna * relacao_subs_img)
                            vMovY[c-1] = (somatorioColuna * relacao_subs_img)
                            richTextImg.insert(END,"\n\nV_mov[%d] = "%(b-1) +"[%.2f]" %vetor_mov[b-1])
                            richTextImg.see(END)
                        somatorioColuna = 0
                        marcaVazio = 1
                            
                        somatorioVazio = somatorioVazio +1                        
                        somatatorioVazio = somatorioVazio + int(1) #marca numero de espacos vazios na coluna
                        
                        paradaX = i
                        paradaY = j
                        richTextImg.insert(END,"\n[%d]"%paradaY +"[%d]"%paradaX + "%d; ;  " %matriz[j][i])
                        
                        if (primeiraPosVazia == 0):
##                            vetor_mov[b-1] = somatorioColuna
##                            richTextImg.insert(END,"\n Teste SOMA COLUNA L 835:: %d: " %somatorioColuna)
                            somatorioColuna = 0
                            primeiraPosVazia = int(1)
                            primeiraPosXvazia = i #N Coluna
                            primeiraPosYvazia = j #N Linha
                            richTextImg.insert(END,"\nprimeriaPos X vazia %d: " %primeiraPosXvazia)
                            richTextImg.insert(END,"\nprimeriaPos Y vazia %d: " %primeiraPosYvazia)
                            richTextImg.see(END)
                            
##                            vetor_mov_parada[b]= ini_parada 
                            
##                            richTextImg.insert(END,"\n\nV_mov %.2f" %mov)
##                            richTextImg.insert(END,"\n\nV_mov[%d] = "%b +"[%.2f]" %vetor_mov[b])
                            richTextImg.insert(END,"\n y  %d" %y)
                            richTextImg.insert(END,"\n j  %d" %j)
                            richTextImg.see(END)
                            
                           
                    if ((y-j)==1): #desconsidera marca de break/pausa apenas na Ultima linha da atual coluna 
                        somatorioVazio = somatorioVazio -1
                        
            if (somatorioVazio != 0):
                richTextImg.insert(END,"\n lalalalla")
                richTextImg.see(END)
##                vetor_parada[b-2] = 1
##                vetor_parada[b-1] = somatorioVazio
            if (somatorioColuna != 0):
             
                vetor_mov[b-1] = somatorioColuna * relacao_subs_img
                vMovY[c-1] = (somatorioColuna * relacao_subs_img) 
                 
                richTextImg.insert(END,"\n\nV_mov[%d] = "%(b-1) +"[%.2f] (somatorioColuna)" %vetor_mov[b-1])
                richTextImg.insert(END,"\n\n bal bla bla")
            
            
                richTextImg.insert(END,"\n SETUP Soma .. ")
                richTextImg.see(END)
##                vetor_parada[b-2] = 1
##                vetor_parada[b-1] = somatorioVazio
            else:
                richTextImg.insert(END,"\n  .. ")
##                    vetor_parada[b-2] = 0
##                    vetor_parada[b-1] = 0       
            richTextImg.insert(END,"\nSomatorioColuna: n (%d)"%i + "= %d" %somatorioColuna)
            richTextImg.insert(END,"\nSomatorioVazio: n (%d)"%i + "= %d" %somatorioVazio)
            richTextImg.insert(END,"\n Numero de Pausa(s) na coluna (%d)"%i +  "= %d " %numero_pausa)
            richTextImg.insert(END,"\n Numero de escritas na coluna (%d)"%i +  "= %d " %numero_escritas)
            vetor_n_pausa[i] = numero_pausa
            richTextImg.insert(END,"\n\nV_pausa FIM ..[%d] = "%(i) +"[%.2f]" %vetor_n_pausa[i]) #Ok, mas salva TODas colunas, salvar apenas com mov
            richTextImg.see(END) 
    richTextImg.insert(END,"\n B  %d" %b)
    richTextImg.insert(END,"\n C  %d" %c)
    richTextImg.see(END)
    del (vetor_x[c:-1])
    del (vPosY[c:-1])
    del (vMovY[c:-1])
                    
    for l in range (len(vetor_x)):    
        richTextImg.insert(END,"\n\nV_x[%d] = "%l +"[%.2f]" %vetor_x[l])
        richTextImg.see(END)
    for l in range (len(vetor_parada)):    
        richTextImg.insert(END,"\n\nV_PARADA[%d] = "%l +"[%.2f]" %vetor_parada[l])
        richTextImg.see(END)

    for l in range (len(vetor_n_pausa)):    
        richTextImg.insert(END,"\n\nV_n_Pausa[%d] = "%l +"[%.2f]" %vetor_n_pausa[l])
        richTextImg.see(END)

    for l in range (len(vcol)):    
        richTextImg.insert(END,"\n\nVcol[%d] = "%l +"[%.2f]" %vcol[l])
        richTextImg.see(END)
    cont = int(0)
    for l in range (len(vcolPosX)):        
        if (vcolNumEsc[l] != 0):
            vcolPosXmov[cont] = vcolPosX[l]
            cont = cont +1
    del (vcolPosXmov[cont:-1])
        
    for l in range (len(vcolPosX)):    
        richTextImg.insert(END,"\n\nvcolPosX[%d] = "%l +"[%.2f]" %vcolPosX[l])
        richTextImg.see(END)
        
    richTextImg.insert(END,"\n\****************************\n")
    
    for l in range (len(vcolPosXmov)):    
        richTextImg.insert(END,"\n\nvcolPosXmov[%d] = "%l +"[%.2f]" %vcolPosXmov[l])
        richTextImg.see(END)
        
    for l in range (len(vcolNumEsc)):    
        richTextImg.insert(END,"\n\nvcolPosX[%d] = "%l +"[%.2f]" %vcolNumEsc[l])
        richTextImg.see(END)
        
##    richTextImg.insert(END,"\nSomatorio TOTAL COLUNAS = %d" %somaTotalColunas)
    richTextImg.insert(END,"\nSomatorio TOTAL PAUSAS = %d" %somaTotalPausas)
    richTextImg.see(END)
    
  
##    num = ( (c*2)+ (somaTotalPausas*2) )#numero para excluir posicoes desnecessarias do vetor
    num = c*2
    richTextImg.insert(END,"\n NUM  %d" %num)
    richTextImg.see(END)
    del (vetor_mov[num:-1])
##    vetor_mov= [0]* ( (c*2)+ (somaTotalPausas*2) ) #C colunas com pos preenchidas e somaTotalPausas eh qtdade total de pausas (q obriga a ter mais posicoes de mov).
    
##    del (vetor_mov[b:-1])
    richTextImg.insert(END,"\n B  %d" %b)
    richTextImg.see(END)

    
    for l in range (len(vetor_mov)):
        richTextImg.insert(END,"\n\nV_mov[%d] = "%l +"[%.2f]" %vetor_mov[l])
        richTextImg.see(END)
                    
    for l in range (len(vPosY)):    
        richTextImg.insert(END,"\n\nvPosY[%d] = "%l +"[%.2f]" %vPosY[l])
        richTextImg.see(END)

    for l in range (len(vMovY)):    
        richTextImg.insert(END,"\n\nvMOV Y[%d] = "%l +"[%.2f]" %vMovY[l])
        richTextImg.see(END)
    
        
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
        
def bSincro(): # create displacement windows - janelas de deslocamento para SINCRONIZACAO dos PULSOS de SAIDA da CONTROLADORA (PCO)
    #para ENABLE IN / TRIGGER IN do LASER Ultravioleta. #
    # Para tal eh necessario habilitar entrada EXTERNA no LASER : via comando GEXT na interface do LASER.
    nome = nomearqImg.get() #arquivo de imagem
##    relacao_subs_img = (int(1))               
    richTextImg.insert(END,"\n--------------------------------------------------------------" )
    if (nome == ""):
      
      richTextImg.insert(END,"\n## You must enter an Image File Name! ##\n")
      richTextImg.see(END)

    else:
        nome = nome+".bmp"
        im = Image.open(nome)
        richTextImg.insert(END,"\n\n ############ LEITURA DE IMAGEM ############")
        richTextImg.insert(END,"\nMode: ")
        richTextImg.insert(END,im.mode)
        richTextImg.see(END)
        xy = im.size
        x = xy[0]
        y = xy[1]
        x = int(x)
        y = int(y)
        richTextImg.insert(END,"\nX: %d \n" %x)
        richTextImg.insert(END,"\nY: %d \n" %y)
        richTextImg.see(END)
##        substratoX= float(substratoX1.get())
##        substratoY= float(substratoY1.get())
        substratoX= float(subsX.get()) #relacao para mov e tam de X
        substratoY= float(subsY.get())
        passo = float(PassoVertical.get()) #nova relacao para Y - vetor mov[]
        substratoX= float(subsX.get())
        substratoY= float(subsY.get())
        subsx1= round( (substratoX/x),5)
        subsy1= round( (substratoY/y),5)
    
    if  ( (subsx1) != (subsy1) ): #relacao tamanho do substrato com relacao ao tamanho da imagem
        richTextImg.insert(END,"\n\n# Scale Factor Value in (Substrate Size) must be the same for X and Y! \n ## ")
        richTextImg.see(END)
        
##        relacao_subs_img = (int(1))
    else:
        relacao_subs_img = float(substratoX/x) #Fator de escala - relacao entre tam substrato a ser manufat e a imagem lida deve ser = entre X e Y.
        richTextImg.insert(END,"\n Relacao Substrate/Imagem: %.5f \n" %relacao_subs_img)
        richTextImg.see(END)
        global fatorColuna  
        fatorColuna = float(relacao_subs_img/passo)
        richTextImg.insert(END,"\n FATOR COLUNA geral   %.5f" %fatorColuna)
        if ( (passo < relacao_subs_img) or (passo == relacao_subs_img)):
            richTextImg.insert(END,"\n ### PASSO < = relacao_subs img!!!\n\n")
            richTextImg.insert(END,"\n ### number of columns to write is (Greater or Equal) than the number of columns of the image\n")
            
            LerImagem()
            
        else:
            richTextImg.insert(END,"\n ### number of columns to write is smaller than the number of image columns ")
            
            
            LerImagem2()
            fatorCol = float(relacao_subs_img/passo)

            richTextImg.insert(END,"\n FATOR COLUNA:::  %.5f" %fatorCol)
            richTextImg.see(END)
            global fatorReducao
            fatorReducao = float(1/fatorCol)
            richTextImg.insert(END,"\n novo FATOR reducao COLUNA:::  %.5f" %fatorReducao)
            richTextImg.see(END)
            fatorReducao = int(1/fatorCol) ##acima float - cuidado com INT para loop de reducao

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################

def LerImagem2(): #alterado para teste de Colunag com Break/pausa Funcao acima copiada para testes nessa, acima OK
    ####MENOS colunas q IMG : passoLAteral > relacao_subs_img
    nome = nomearqImg.get() #arquivo de imagem
##    relacao_subs_img = (int(1))               
    richTextImg.insert(END,"\n--------------------------------------------------------------" )
    if (nome == ""):
      
      richTextImg.insert(END,"\n## You must enter an Image File Name! ##\n")
      richTextImg.see(END)

    else:
        nome = nome+".bmp"
        im = Image.open(nome)
        richTextImg.insert(END,"\n\n ############ LEITURA DE IMAGEM ############")
        richTextImg.insert(END,"\nMode: ")
        richTextImg.insert(END,im.mode)
        richTextImg.see(END)
        xy = im.size
        x = xy[0]
        y = xy[1]
        x = int(x)
        y = int(y)
        richTextImg.insert(END,"\nX: %d \n" %x)
        richTextImg.insert(END,"\nY: %d \n" %y)
        richTextImg.see(END)
##        substratoX= float(substratoX1.get())
##        substratoY= float(substratoY1.get())
        substratoX= float(subsX.get()) #relacao para mov e tam de X
        substratoY= float(subsY.get())
        passo = float(PassoVertical.get()) #nova relacao para Y - vetor mov[]   
    
        subsx1= round( (substratoX/x),5)
        subsy1= round( (substratoY/y),5)
    
    
       

    ##        richTextImg.insert(1.0,"\n# EXecuting ... !\n") 
    ##        extra = float(1.0)
    ##        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
    ##        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
    ##        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx])
    ##        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAy])
    ##
    ##        if (ArqCriado == 0):
    ##            ###LOOP para ACRESCENTAR colunas
    ##        for loop in range (0,len(vetor_mov)-1,2):
    ##            passo_novo = float(0)
    ##            for cont in range (fatorCol):
    ##            for cont in range (2):
    ##                
    ##                
    ##                    richTextImg.insert(END,"\n --------------------------")
    ##                    richTextImg.insert(END,"\n Loop  %d" %loop + "// Cont: %d" %cont)
    ##                    richTextImg.insert(END,"\n\nV_x[%d] = "%(loop/2) +"[%.2f]" %((vetor_x[loop/2])-passo_novo))    
    ##                    richTextImg.insert(END,"\n\nV_mov[%d] = "%loop +"[%.2f]" %vetor_mov[loop])
    ##                    richTextImg.insert(END,"\n\nV_mov[%d] = "%(loop+1) +"[%.2f]" %vetor_mov[loop+1])
    ##                    richTextImg.insert(END,"\n --------------------------\n")




        
        if  ( (subsx1 ) != (subsy1) ): #relacao tamanho do substrato com relacao ao tamanho da imagem
                richTextImg.insert(END,"\n\n# Scale Factor Value in (Substrate Size) must be the same for X and Y! \n ## Using 1.00 FOR TEST#")
                richTextImg.see(END)
                relacao_subs_img = (int(1))
        else:    
                relacao_subs_img = float(substratoX/x) #Fator de escala - relacao entre tam substrato a ser manufat e a imagem lida deve ser = entre X e Y.

                richTextImg.insert(END,"\n Relacao Substrate/Imagem: %.5f \n" %relacao_subs_img)
                richTextImg.see(END)
                fatorCol = float(relacao_subs_img/passo)
##        if (fatorCol < 1):
                richTextImg.insert(END,"\n FATOR COLUNA:::  %.5f" %fatorCol)
                fatorReducao = float(1/fatorCol)
                richTextImg.insert(END,"\n novo FATOR reducao COLUNA:::  %.5f" %fatorReducao)
                fatorReducao = int(1/fatorCol) ##acima float - cuidado com INT para loop de reducao
        
        lst2 = []
        lst = list(im.getdata())
        matriz =[]    
        richTextImg.insert(END,"\n\n")
        
        a = 0 
        for j in xrange(y):
            matriz.append([])
            for i in xrange(x):
                matriz[j].append (int( (lst[a]) ))
                a = a +1

        #onde tem PIXEL = 0 (pontos pretos em fundo branco - tipo MONOCROMATICO)

        primeiraPos = int(0)
        paradaColuna = int(0)
        numero_pausa = int(0)
        somatorioColuna = int(0)
        marcaColuna = int(0)
        somatorioVazio = int(0)
        somaTotalColunas = int(0)
        somaTotalPausas = int(0)
        passo_novo = float(0)
                
        b = int(0)
        c = int(0)
##        global vetor_mov
##        vetor_mov= [0]*(x*2) #x eh o numero de colunas
        ############################################################ vetor_pausa = [0]*(x*2) #alterar numero maximo de posicoes
        
        vetor_mov_parada = [0]*(x*2)
        vetor_parada = [0]*(x*2)
        vetor_n_pausa =[0]*x
        global vetor_mov
        vetor_mov = [0]*(x*y) #removidas abaixo posicoes desnecessarias ( del .. ) 
        global vetor_x
        vetor_x= [0]*(x*y)
        
        richTextImg.insert(END,"\n\n\n-------------")
        richTextImg.see(END)
        
##        for l in range (len(vetor_x)):    
##            richTextImg.insert(END,"\n\nV_x[%d] = "%l +"[%.2f]" %vetor_x[l]) #apresenta toda matriz de ponto inicial de X.
        fatorCol = int(relacao_subs_img/passo)
        richTextImg.insert(END,"\n Fatir COL  %d: " %fatorCol)
        for i in range(0,x,fatorReducao): #Colunas
            richTextImg.insert(END,"\n PASS NEW  %d" %passo_novo)
            passo_novo = float(0)
            
        
            
            if (somatorioColuna != 0): #adiocnado para casos em q COLUNA eh CHEIA (adicionar soma de movimento aqui
                vetor_mov[b-1] = somatorioColuna * relacao_subs_img
                richTextImg.insert(END,"\n\nV_mov[%d] = "%(b-1) +"[%.2f] (somatorioColuna)" %vetor_mov[b-1])
                richTextImg.insert(END,"\n\n bal bla bla")
            somatorioColuna = 0
            #somatorioColuna zerado abaixo
            #vetor_parada -> 1a posicao = sim ou nao (0 ou 1); 2a posicao = numero de pausa/breaks e 3a 
                        
            marcaVazio = 0
            primeiraPosVazia = 0
            somatorioVazio = 0
            somaTotalColunas = somaTotalColunas + somatorioColuna 
            somaTotalPausas = somaTotalPausas + numero_pausa #acumulador total de breaks das colunas para dimensionar Vetor de Movimentos
##            somatorioColuna = 0
            primeiraPos = 0 #de frente para a mesa: indo para a guia!
            marcaColuna = 0
            paradaColuna = 0 #para marcar presença de dado em cada coluna (se houver, marca como 1 abaixo e identifica posicoes vazias).
##            richTextImg.insert(END,"\n\nV_parada[%d] = "%(b-2) +"[%.2f] (somatorioVazio)" %vetor_parada[b-2])
##            richTextImg.insert(END,"\n\nV_parada[%d] = "%(b-1) +"[%.2f] (somatorioVazio)" %vetor_parada[b-1])
            
##            richTextImg.insert(END,"\n\nV_pausa[%d] = "%(i-1) +"[%.2f]" %vetor_n_pausa[i-1])
            
            numero_pausa = 0 #zera numero de breaks/pausas da coluna


            
            for j in range(0,y): #posicao das Linhas
            
                
##                vetor_mov[c] = somatorioColuna +  528.86
##                vetor_mov[b+1] = somatorioColuna
                dado = int(matriz[j][i])
                cor_ie = nova_cor
                if (dado == cor_ie):
                    if (marcaVazio == 1):
                        
                        richTextImg.insert(END,"\nSomatorioVazio: n (%d)"%i + "= %d" %somatorioVazio)
                        richTextImg.see(END)
                       
                        numero_pausa = numero_pausa + 1  #salvar este valor do somatorio no vetor por coluna : vetor_n_pausa
                        somatorioVazio = 0
                    
                    
                    richTextImg.insert(END,"\n\n------------------------------------")
                    richTextImg.insert(END,"\n[%d]"%j +"[%d]"%i + "= %d; ;  " %matriz[j][i])
                    somatorioColuna = somatorioColuna +1
                    richTextImg.insert(END,"\n somat.. [%d]"%j +"[%d]"%i )
                    richTextImg.insert(END,"\nSOMAT COLUNA L 835: ini apos inc : %d: " %somatorioColuna)
                    richTextImg.see(END)
                    marcaColuna = int(1) #para marcar que tem dado nesta coluna e verificar as posicoes vazias na mesma coluna
                                                
                    if (primeiraPos == 0):
                        primeiraPos = int(1)
                        primeiraPosX = i #N Coluna
                        primeiraPosY = j #N Linha
                        richTextImg.insert(END,"\nprimeriaPos X %d: " %primeiraPosX)
                        richTextImg.insert(END,"\nprimeriaPos Y %d: " %primeiraPosY)
##                        mov= float( GUIAy - ((y - j)*relacao_subs_img) )#Y (0a12) -> y=13!!!
##                            mov= float( GUIAy - ((y - j)*passo) )#Y (0a12) -> y=13!!!
                        mov= float( GUIAy - ((y - j)*relacao_subs_img) )
                        richTextImg.insert(END,"\n B  %d" %b)
                        richTextImg.insert(END,"\n C  %d" %c)
                        richTextImg.insert(END,"\n MOV here ,,  %.4f" %mov)
                        vetor_mov[b]= mov
                        vetor_x[c] = GUIAx - (i*relacao_subs_img)
                        passo_novo = passo_novo + passo
                        
                        richTextImg.insert(END,"\n\nV_x[%d] = "%c +"[%.2f]" %vetor_x[c])
                        richTextImg.insert(END,"\n y  %d" %y)
                        richTextImg.insert(END,"\n j  %d" %j)
                        richTextImg.see(END)
                        marcaPenultimaPosPreenchida = 1 # para guardar somatorio apenas ate aqui
                        b = b+2
                        c = c+1
            
                        
                else: #dado = 255 = vazio - branco!
                    
                    primeiraPos = 0
######################################### teste de posicao vazia ######################################### ######################################### 
######################################### #########################################  ######################################### 
                    
                    #ELSE e (if dado == 0):
                    #dado = 255 = vazio - branco!
                    if ((marcaColuna == 1)):
                        richTextImg.insert(END,"\n B out %d" %b)
                        richTextImg.insert(END,"\n C out %d" %c)
                        richTextImg.see(END)
                        
                        if (somatorioColuna >0):
                            richTextImg.insert(END,"\nSOMAT COLUNA dentro else - save : %d: " %somatorioColuna)
                            vetor_mov[b-1] = (somatorioColuna * relacao_subs_img)
                            richTextImg.insert(END,"\n\nV_mov[%d] = "%(b-1) +"[%.2f]" %vetor_mov[b-1])
                            richTextImg.see(END)
                        somatorioColuna = 0
                        marcaVazio = 1
                            
                        somatorioVazio = somatorioVazio +1                        
                        somatatorioVazio = somatorioVazio + int(1) #marca numero de espacos vazios na coluna
                        
                        paradaX = i
                        paradaY = j
                        richTextImg.insert(END,"\n[%d]"%paradaY +"[%d]"%paradaX + "%d; ;  " %matriz[j][i])
                        
                        if (primeiraPosVazia == 0):
##                            vetor_mov[b-1] = somatorioColuna
##                            richTextImg.insert(END,"\n Teste SOMA COLUNA L 835:: %d: " %somatorioColuna)
                            somatorioColuna = 0
                            primeiraPosVazia = int(1)
                            primeiraPosXvazia = i #N Coluna
                            primeiraPosYvazia = j #N Linha
                            richTextImg.insert(END,"\nprimeriaPos X vazia %d: " %primeiraPosXvazia)
                            richTextImg.insert(END,"\nprimeriaPos Y vazia %d: " %primeiraPosYvazia)
                            richTextImg.see(END)
                            
##                            vetor_mov_parada[b]= ini_parada 
                            
##                            richTextImg.insert(END,"\n\nV_mov %.2f" %mov)
##                            richTextImg.insert(END,"\n\nV_mov[%d] = "%b +"[%.2f]" %vetor_mov[b])
                            richTextImg.insert(END,"\n y  %d" %y)
                            richTextImg.insert(END,"\n j  %d" %j)
                            richTextImg.see(END)
                            
                           
                    if ((y-j)==1): #desconsidera marca de break/pausa apenas na Ultima linha da atual coluna 
                        somatorioVazio = somatorioVazio -1
                        
            
            if (somatorioVazio != 0):
                richTextImg.insert(END,"\n lalalalla")
                richTextImg.see(END)
##                vetor_parada[b-2] = 1
##                vetor_parada[b-1] = somatorioVazio
            if (somatorioColuna != 0):
             
                vetor_mov[b-1] = somatorioColuna * relacao_subs_img
                richTextImg.insert(END,"\n\nV_mov[%d] = "%(b-1) +"[%.2f] (somatorioColuna)" %vetor_mov[b-1])
##                richTextImg.insert(END,"\n\n bal bla bla")         
##                richTextImg.insert(END,"\n SETUP Soma .. ")
                richTextImg.see(END)
            else:
                richTextImg.insert(END,"\n  .. ")
##                    vetor_parada[b-2] = 0
##                    vetor_parada[b-1] = 0       
            richTextImg.insert(END,"\nSomatorioColuna: n (%d)"%i + "= %d" %somatorioColuna)
            richTextImg.insert(END,"\nSomatorioVazio: n (%d)"%i + "= %d" %somatorioVazio)
            richTextImg.insert(END,"\n Numero de Pausa(s) na coluna (%d)"%i +  "= %d " %numero_pausa)
            vetor_n_pausa[i] = numero_pausa
            richTextImg.insert(END,"\n\nV_pausa FIM ..[%d] = "%(i) +"[%.2f]" %vetor_n_pausa[i]) #Ok, mas salva TODas colunas, salvar apenas com mov
            richTextImg.see(END) 
    richTextImg.insert(END,"\n B  %d" %b)
    richTextImg.insert(END,"\n C  %d" %c)
    richTextImg.see(END)
    del (vetor_x[c:-1])
    for l in range (len(vetor_x)):    
        richTextImg.insert(END,"\n\nV_x[%d] = "%l +"[%.2f]" %vetor_x[l])
        richTextImg.see(END)

        
##    richTextImg.insert(END,"\nSomatorio TOTAL COLUNAS = %d" %somaTotalColunas)
    richTextImg.insert(END,"\nSomatorio TOTAL PAUSAS = %d" %somaTotalPausas)
    richTextImg.see(END)
    
  
##    num = ( (c*2)+ (somaTotalPausas*2) )#numero para excluir posicoes desnecessarias do vetor
    num = c*2
    richTextImg.insert(END,"\n NUM  %d" %num)
    richTextImg.see(END)
    del (vetor_mov[num:-1])
##    vetor_mov= [0]* ( (c*2)+ (somaTotalPausas*2) ) #C colunas com pos preenchidas e somaTotalPausas eh qtdade total de pausas (q obriga a ter mais posicoes de mov).
    
##    del (vetor_mov[b:-1])
    richTextImg.insert(END,"\n B  %d" %b)
    richTextImg.see(END)

    
    for l in range (len(vetor_mov)):
        richTextImg.insert(END,"\n\nV_mov[%d] = "%l +"[%.2f]" %vetor_mov[l])
        richTextImg.see(END)


####################################################################################################################
####################################################################################################################

def bExecImg_imaior():
    # MANTEM num IGUAL de colunas ou AUMENTA numero de colunas ao escrever! #copia da f acima para teste de break no INI e fim d coluna apenas
    
    
    jerktime = 0.04
    aceleracao = 80
    a= (float(aceleracao))
    velocidade = velMov.get() #velocidade laser ON
    von= (float(velocidade))
    velocidade1 = velMovSetup.get() #Setup - velocidade de volta dos posicionadores
    vset= (float(velocidade1))
    extra = float(DeslocExtra.get())
    richTextImg.insert(END,"\n v %.2f " %von)
    richTextImg.insert(END,"\n v1 %.2f " %vset)
    richTextImg.insert(END,"\n ex %.2f " %extra)
    
#####################################################################################
#####################################################################################
    nome = nomearqImg.get()
    nome = nome +".bmp"
    im = Image.open(nome)
    xy = im.size
    x = xy[0]
    y = xy[1]
    x = int(x)
    y = int(y)
    substratoX= float(subsX.get()) 
    relacao_subs_img = float(substratoX/x)
    passo = float(PassoVertical.get())
    fatorCol = int(relacao_subs_img/passo)
    
##    shiftXimg.get
##    shiftYimg.get
    sX = float(shiftXimg.get())
    sY = float(shiftYimg.get())
                
##    richTextImg.insert(END,"\n*** Fim loop 1/2 --------------------------\n")
    ant = int(0)
    ac = int(-1)

    passo_novo = float(0)   
    for loop in range (0, len (vcolPosXmov)-1, 1):
        richTextImg.insert(END,"\n******************************")
    
        richTextImg.insert(END,"\n\n volPosXmov[%d] = "%loop +"[%.2f]" %vcolPosXmov[loop])


        richTextImg.insert(END,"\n\n vcolNumEsc[%d] = "%loop +"[%.2f]" %vcolNumEsc[loop])
        ant = ac + 1 #posicao inicial do vetor [ant] [ini]
        richTextImg.insert(END,"\n ANT %d " %ant)
        ac = ac + vcolNumEsc[loop] #posicao final do vetor [ac] [fim]
            
        richTextImg.insert(END,"\n Loop  %d" %loop + "// AC: %d" %ac)
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, vset, a, jerktime, jerktime) #velocidade de Movim (menor).
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, von, a, jerktime, jerktime) #velocidade de Movim (menor).

        
        passo_novo = float(0)
                    
        for cont in range (fatorCol):

                for j in range (vcolNumEsc[loop]):
                    richTextImg.insert(END,"\n ** j %d " %j)
                    pos = float( (vPosY[ant+j]) - sY) #POS = inicio movimento

                    richTextImg.insert(END,"\n Pos %.3f " %pos)
                    percurso = float(vMovY[ant+j]) # PERCURSO = TOTAL da Coluna
                    richTextImg.insert(END,"\n Percurso %.3f " %percurso)

                    richTextImg.insert(END,"\n --------------------------")
                    richTextImg.insert(END,"\n CONT %d" %cont)
                    richTextImg.insert(END,"\n Loop  %d" %loop + "// J: %d" %j)
                    richTextImg.insert(END,"\n Passo %.3f " %passo_novo)
                    richTextImg.insert(END,"\n\nV_x[%d] = "%(loop) +"[%.2f]" %( ((vcolPosXmov[loop])-passo_novo)-sX))    
                    richTextImg.insert(END,"\n\nVposY[%d] = "%(ant+j)+"[%.2f]" %vPosY[ant+j])
                    richTextImg.insert(END,"\n\nVmovY[%d] = "%(ant+j) +"[%.2f]" %vMovY[ant+j])
                    richTextImg.insert(END,"\n --------------------------")
                    
                    if (vcolNumEsc[loop] == 1):
                        richTextImg.insert(END,"\n  if (vcolNumEsc[loop] == 1): ") #"apenas um traco por coluna"

                        x = float((float(vcolPosXmov[loop]) - (passo_novo) - (sX)))
                        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [x]) #comeco do posicionador X
                        [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                        print ('\n **aqui mudou x!! X: %.2f \n****************\n',   currentPositionx)
       
                        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos-extra]) #Y: inicio movimento antes de ligar laser
                        
                        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, vset, a, jerktime, jerktime) #velocidade de Movim (menor).
                        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, von, a, jerktime, jerktime) #velocidade de Movim (menor).

                        [errorCode, returnString] = XY.PositionerTimeFlasherSet (socketId,positionery,pos,pos+percurso,0.00025) #Y LASER ON: #do inicio(POS) ate FIM(Pos+Percurso)#
                        [errorCode,returnString] = XY. PositionerTimeFlasherEnable(socketId, positionery)
                        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos + percurso + extra])#Y movimento total (de POS ate POS+PERCURSO)+desloc extra
                        [errorCode, MinimumPosition, MaximumPosition, TimePeriod, EnableState] = XY.PositionerTimeFlasherGet(socketId, positionery)
                        print ('\n---------------------- INI e fim \n')
                        print ('\n\nMin : %.5f ' ,MinimumPosition)
                        print ('Max : %.5f ' ,MaximumPosition)                        
                        [errorCode,returnString] = XY. PositionerTimeFlasherDisable(socketId, positionery)
                        [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                        [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                        print (' X: %.2f ',   currentPositionx)
                        print("\n Y: %.2f;  ",currentPositiony)
                    
                    else:
                         if (j == 0):
                            richTextImg.insert(END,"\n  nao tem apenas 1 loop e eh o inicial")

                            x = float((float(vcolPosXmov[loop]) - (passo_novo) - (sX)))
                            [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [x]) #comeco do posicionador X
                            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                            print ('\n **aqui mudou x!! X: %.2f \n****************\n',   currentPositionx)
       
                            [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos-extra]) #Y: inicio movimento antes de ligar laser
                            
                            [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, vset, a, jerktime, jerktime) #velocidade de Movim (menor).
                            [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, von, a, jerktime, jerktime) #velocidade de Movim (menor).

                            [errorCode, returnString] = XY.PositionerTimeFlasherSet (socketId,positionery,pos,pos+percurso,0.00025) #Y LASER ON: #do inicio(POS) ate FIM(Pos+Percurso)#
                            [errorCode,returnString] = XY. PositionerTimeFlasherEnable(socketId, positionery)
                            [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos + percurso])#Y movimento total (de POS ate POS+PERCURSO)
                            [errorCode, MinimumPosition, MaximumPosition, TimePeriod, EnableState] = XY.PositionerTimeFlasherGet(socketId, positionery)
                            print ('\n---------------------- INi, mas tem +\n')
                            print ('\n\nMin : %.5f ' ,MinimumPosition)
                            print ('Max : %.5f ' ,MaximumPosition)
                            [errorCode,returnString] = XY. PositionerTimeFlasherDisable(socketId, positionery)
                            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                            [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                            print (' X: %.2f ',   currentPositionx)
                            print("\n Y: %.2f;  ",currentPositiony)


                         else:
                            
                            if (j == (vcolNumEsc[loop]-1) ): #ultimo loop entao faz extra
                                richTextImg.insert(END,"\n  Uuultimo loop: ")
####                                [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos]) #Y: inicio movimento antes de ligar laser
                           
                                [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, vset, a, jerktime, jerktime) #velocidade de Movim (menor).
                                [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, von, a, jerktime, jerktime) #velocidade de Movim (menor).
        
                                [errorCode, returnString] = XY.PositionerTimeFlasherSet (socketId,positionery,pos,pos+percurso,0.00025) #Y LASER ON: #do inicio(POS) ate FIM(Pos+Percurso)#
                                [errorCode,returnString] = XY. PositionerTimeFlasherEnable(socketId, positionery)
                                [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos + percurso + extra])#Y movimento total (de POS ate POS+PERCURSO)+desloc extr
                                [errorCode, MinimumPosition, MaximumPosition, TimePeriod, EnableState] = XY.PositionerTimeFlasherGet(socketId, positionery)
                                print ('\n---------------------- ultimo \n')
                                print ('\n\nMin : %.5f ' ,MinimumPosition)
                                print ('Max : %.5f ' ,MaximumPosition)
                                [errorCode,returnString] = XY. PositionerTimeFlasherDisable(socketId, positionery)
                                [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                                [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                                print (' X: %.2f ',   currentPositionx)
                                print("\n Y: %.2f;  ",currentPositiony)


                            
                            else: #loops internos - sem desloc extra
                                richTextImg.insert(END,"\n ult else loops internos - sem desloc extra")
####                                [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos]) #Y: inicio movimento antes de ligar laser
                           
                                [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, vset, a, jerktime, jerktime) #velocidade de Movim (menor).
                                [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, von, a, jerktime, jerktime) #velocidade de Movim (menor).
        
                                [errorCode, returnString] = XY.PositionerTimeFlasherSet (socketId,positionery,pos,pos+percurso,0.00025) #Y LASER ON: #do inicio(POS) ate FIM(Pos+Percurso)#
                                [errorCode,returnString] = XY. PositionerTimeFlasherEnable(socketId, positionery)
                                
                                [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos + percurso])#Y movimento total (de POS ate POS+PERCURSO)+desloc extra
                                [errorCode, MinimumPosition, MaximumPosition, TimePeriod, EnableState] = XY.PositionerTimeFlasherGet(socketId, positionery)
                                print ('\n---------------------- meio\n')
                                print ('\n\nMin : %.5f ' ,MinimumPosition)
                                print ('Max : %.5f ' ,MaximumPosition)
                                [errorCode,returnString] = XY. PositionerTimeFlasherDisable(socketId, positionery)
                                [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
                                [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
                                print (' X: %.2f ',   currentPositionx)
                                print("\n Y: %.2f;  ",currentPositiony)

                    
                    
##                                
                passo_novo = passo_novo + passo      # muda no cont
                    



def bExecImg1(): #execute file - aba6 - IMG execution
   
   
    # fatorColuna = (relacao_subs_img)/(passo_lateral)
##    fatorCol = float(relacao_subs_img/passo)
##    global fatorReducao
##    fatorReducao = float(1/fatorCol)
##    richTextImg.insert(END,"\n novo FATOR reducao COLUNA:::  %.5f" %fatorReducao)
##    richTextImg.see(END)
##    fatorReducao = int(1/fatorCol) ##acima float - cuidado com INT para loop de reducao

   
   
   if (fatorColuna == -1) :
       richTextImg.insert(END,"\n ** Error. Check image file - button 'Read Image File' and \n ** after use - button Create Displacement Windows.\n\n")
       richTextImg.see(END)
   else:
       if ( (fatorColuna > 1) or (fatorColuna == 1)):
            bExecImg_imaior()
            # MANTEM num colunas ou AUMENTA numero de colunas ao escrever! passo < ou = relacao_subs_img
       else:
            bExecImg_menor()
            #reducao de colunas, passo > relacao_subs_img
   
#################################################################################################################  


def bExecImg_menor():
    jerktime = 0.04
    aceleracao = 80
    a= (float(aceleracao))
    velocidade = velMov.get() #velocidade laser ON
    v= (float(velocidade))
    velocidade1 = velMovSetup.get() #Setup - velocidade de volta dos posicionadores
    v1= (float(velocidade1))
    extra = float(DeslocExtra.get())
    richTextImg.insert(END,"\n v %.2f " %von)
    richTextImg.insert(END,"\n v1 %.2f " %vset)
    richTextImg.insert(END,"\n ex %.2f " %extra)
    
    
    
    richTextImg.insert(1.0,"\n# EXecuting ... !\n") 
    
    [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime)
    [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime)
    [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAx])
    [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [GUIAy])

##    if (ArqCriado == 0):
    
    for l in range (len(vetor_mov)):    
        richTextImg.insert(END,"\n\nV_mov[%d] = "%l +"[%.2f]" %vetor_mov[l])      
##    [errorCode, returnString] = XY.PositionerTimeFlasherSet (socketId,positionery,posY+40.00,posY+60.00,0.00025)
##    [errorCode,returnString] = XY. PositionerTimeFlasherEnable(socketId, positionery)
##    [errorCode, returnString] = XY.GroupMoveRelative(socketId, positionery, [posY+62.00])
##    [errorCode, MinimumPosition, MaximumPosition, TimePeriod, EnableState] = XY.PositionerTimeFlasherGet(socketId, positionery)
##    [errorCode,returnString] = XY. PositionerTimeFlasherDisable(socketId, positionery)


##        for loop in range (((len(vetor_mov)) -1)/2):
    for loop in range (0,len(vetor_mov)-1,2):
        richTextImg.insert(END,"\n --------------------------")
        richTextImg.insert(END,"\n Loop  %d" %loop)
        richTextImg.insert(END,"\n\nV_x[%d] = "%(loop/2) +"[%.2f]" %vetor_x[loop/2])    
        richTextImg.insert(END,"\n\nV_mov[%d] = "%loop +"[%.2f]" %vetor_mov[loop])
        richTextImg.insert(END,"\n\nV_mov[%d] = "%(loop+1) +"[%.2f]" %vetor_mov[loop+1])
        richTextImg.insert(END,"\n --------------------------\n")
        
        pos = float(vetor_mov[loop]) #POS = inicio movimento
        percurso = float(vetor_mov[loop+1]) # PERCURSO = TOTAL da Coluna

        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v1, a, jerktime, jerktime) #velocidade de setup (maior)!
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v1, a, jerktime, jerktime) #velocidade de setup (maior)!

        #inicio movimento em direção a guia.
        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionerx, [vetor_x[loop/2]]) #comeco do posicionador X
       
        
##            [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos- extra]) #Y: inicio movimento antes de ligar laser
        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos]) #Y: inicio movimento antes de ligar laser
        
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionerx, v, a, jerktime, jerktime) #velocidade de Movim (menor).
        [errorCode, returnString] = XY.PositionerSGammaParametersSet (socketId, positionery, v, a, jerktime, jerktime) #velocidade de Movim (menor).
        
        [errorCode, returnString] = XY.PositionerTimeFlasherSet (socketId,positionery,pos,pos+percurso,0.00025) #Y LASER ON: #do inicio(POS) ate FIM(Pos+Percurso)#
        
        [errorCode,returnString] = XY. PositionerTimeFlasherEnable(socketId, positionery)
        
##            [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos + percurso + extra])#Y movimento total (de POS ate POS+PERCURSO)+desloc extra
        [errorCode, returnString] = XY.GroupMoveAbsolute(socketId, positionery, [pos + percurso])#Y movimento total (de POS ate POS+PERCURSO)+desloc extra
        
        [errorCode, MinimumPosition, MaximumPosition, TimePeriod, EnableState] = XY.PositionerTimeFlasherGet(socketId, positionery)
        [errorCode,returnString] = XY. PositionerTimeFlasherDisable(socketId, positionery)
        richTextImg.insert(END,"\n MinimumPosition  %d" %MinimumPosition)
        richTextImg.insert(END,"\n MaximumPosition  %d" %MaximumPosition)

        print ('\n\nMin : %.5f ' ,MinimumPosition)
        print ('Max : %.5f ' ,MaximumPosition)
        print ('EnableState : %.5f ' , EnableState)   


#fim funcoes aba6 ie

####################################################################################################################################
####################################################################################################################################




##################################################################################################
        #ini funcoes aba img processing sobel skel

def bCriarLogFile_imgP(): #aba 7 image execution
  nome = nomearqLogImgP.get()
  richTextImgP.insert(END,"\n--------------------------------------------------------------" )
  if ((nome == "") or (nome == " ")):
     richTextImgP.insert(END,"\n## You must enter a LOG File Name! ##\n")
     richTextImgP.see(END)
  else:
    nome = nome+".txt"      
    
    if (tempfile._exists(nome)):      
          richTextImgP.insert(END,"\n## Existing File. Choose a Different Name! ##\n")
          richTextImgP.see(END)
        
    else:
        w = open(nome,'w')
        conteudo_arq = richTextImg.get(1.0, END)
        w.write(conteudo_arq)
        w.close()
        richTextImgP.insert(END,"\n# LOG File created: %s:\n" %nome)
        richTextImgP.see(END)
        

def bLerArquivo_IMGP(): #ABA7 IMG PROC
  richTextImgP.insert(END,"\n--------------------------------------------------------------" )
  nome = nomearqImgXYZ.get()
  if (nome == ""):
      richTextImgP.insert(END,"\n## You must enter an Image File Name! ##\n")
      richTextImgP.see(END)
  else:
        nome = nome +".bmp"
        try:
            
            w = open(nome,'r')
            
            richTextImgP.insert(END,"\n#File selected: %s:\n" %nome)
        except:
            
            richTextImgP.insert(END,"\n# Failed to read file: %s:\n" %nome)


        relacao_subs_img = (int(1))

        im = Image.open(nome)
        richTextImgP.insert(END,"\n# Mode: ")
        richTextImgP.insert(END,im.mode)
        modo = int (im.mode)
        if (modo == 1):
            richTextImgP.insert(END,"\n# - OK! A monochromatic Image!")
        richTextImgP.insert(END,"\n# Format: ")
        richTextImgP.insert(END,im.format)
        

        xy = im.size
        x = xy[0]
        y = xy[1]
        richTextImgP.insert(END,"\nX:  ")
        richTextImgP.insert(END,x)
        richTextImgP.insert(END,"\nY:  ")
        richTextImgP.insert(END,y)
        x = int(x)
        y = int(y)
        substratoX= float(subsX.get())
        substratoY= float(subsY.get())
        subsx1= round( (substratoX/x),5)
        subsy1= round( (substratoY/y),5)
        richTextImgP.insert(END,"\n Subsx1: %.5f \n" %subsx1)
        richTextImgP.insert(END,"\n Subsy1: %.5f \n" %subsy1)
        richTextImgP.insert(END,"\n--------------------------------------------------------------\n" )



        lst = list(im.getdata())
        matriz =[]
        
        a = 0 
        for j in xrange(y):
            matriz.append([])
            for i in xrange(x):
                matriz[j].append (int( (lst[a]) ))
                a = a +1
##
####apresentacao por COLUNAS
####0,0   1,0     2,0     3,0     4,0 .. 12,0
####0,1   1,1     2,1     3,1     4,1 .. 12,1
####...
####0,9   1,9     2,9     3,9     4,9 .. 12,9
##

##  -- ini   MATRIZ nao eh mais apresentada no richtext:
                
        for i in range(x): #Colunas
            for j in range(y): #Linhas
                richTextImgP.insert(END,"[%d]"%j +"[%d]"%i + "= %s; ;  " %matriz[j][i])
            richTextImgP.insert(END,"\n\n")
        richTextImgP.insert(END,"\nJ: %d" %j)
        richTextImgP.insert(END,"\ni: %d \n\n" %i)

def bTestePVT():
    LerImagem2PVT()

def LerImagem2PVT(): ##copia LerImagemPVT 13-11-14 
    nome = nomearqImgXYZ.get() #arquivo de imagem
    relacao_subs_img = (int(1))               
    richTextImgP.insert(END,"\n--------------------------------------------------------------" )
    if (nome == ""):      
      richTextImgP.insert(END,"\n## You must enter an Image File Name! ##\n")
      richTextImgP.see(END)
    else:
        nome = nome+".bmp"
       
        try:
            
            w = open(nome,'r')
            
            richTextImgP.insert(END,"\n#File selected: %s\n" %nome)
        except:
            
            richTextImgP.insert(END,"\n# Failed to read file: %s\n" %nome)
        richTextImgP.see(END)
    


        
        im = Image.open(nome)
        richTextImgP.insert(END,"\n\n ############ LEITURA DE IMAGEM ############")
        richTextImgP.insert(END,"\nMode: ")
        richTextImgP.insert(END,im.mode)
        richTextImgP.see(END)
        xy = im.size
        x = xy[0]
        y = xy[1]
        x = int(x)
        y = int(y)
        richTextImgP.insert(END,"\nX: %d \n" %x)
        richTextImgP.insert(END,"\nY: %d \n" %y)
        richTextImgP.see(END)
##        substratoX= float(subsX.get())
##        substratoY= float(subsY.get())
##        subsx1= round( (substratoX/x),5)
##        subsy1= round( (substratoY/y),5)
##        richTextImgP.insert(END,"\n Subsx1: %.5f \n" %subsx1)
##        richTextImgP.insert(END,"\n Subsy1: %.5f \n" %subsy1)
##
##        if  (((subsx1)) != ((subsy1 )) ): #relacao tamanho do substrato com relacao ao tamanho da imagem
##                richTextImgP.insert(END,"\n\n# Scale Factor Value in (Substrate Size) must be the same for X and Y! \n ## Using 1.00 FOR TEST#")
##                richTextImgP.see(END)
##                relacao_subs_img = (int(1))
##        else:    
##                relacao_subs_img = float(substratoX/x) #Fator de escala - relacao entre tam substrato a ser manufat e a imagem lida deve ser = entre X e Y.
##                richTextImgP.insert(END,"\n Relacao Substrate/Imagem: %.5f \n" %relacao_subs_img)
##                richTextImgP.see(END)
        
        lst2 = []
        lst = list(im.getdata())
        global matriz
        matriz =[]    
        richTextImgP.insert(END,"\n\n")
        
        a = 0 
        for j in xrange(y):
            matriz.append([])
            for i in xrange(x):
                matriz[j].append (int( (lst[a]) ))
                a = a +1
        #onde tem PIXEL = 0 (pontos pretos em fundo branco - tipo MONOCROMATICO)
                
        primeiraPos = int(0)
        b = int(0)
        c = int(0)
        vcol = [0]*x
        vcolPosX = [0]*x       
        
        global vcolPosXmov 
        vcolPosXmov = [0]*x        
        global vPosY
        global vMovY
        vPosY = [0]*(x*y)
        vMovY = [0]*(x*y)
        global vetor_x
        vetor_x= [0]*(x*y)      
        richTextImgP.insert(END,"\n\n\n-------------")
        richTextImgP.see(END)
        L_inf = 0
        Diag_inf = 0
        Col_lado = 0
        Diag_sup  = 0
        L_sup = 0
        Diag_s_esq = 0
        Col_l_esq = 0
        Diag_i_esq = 0
        n_ramificacoes = int(0)
        v_ramif = [0]*8
        v_estado_ant = [8]*9 #[vetor de ramificacoes contendo o ultimo somatorio a ser salvo nos vet_movimentos (( 0=linhaIinf; 1=DiagInf; 2=ColLado; 3=DiagSup) 4= ql alteracao/troca d estado)]
        contador_n_ramif = int(0)
        somaL_inf = 0
        somaDiag_inf = 0
        somaDiag_sup = 0
        somaCol_lado = 0
        somaL_sup = 0
        somaDiag_s_esq = 0
        somaCol_l_esq = 0
        somaDiag_i_esq = 0
        novoi = -1
        novoj =-1
        marca_troca_estado = 5
       
        soma = 0
        

        global PrimeiraPosX
        global PrimeiraPosY
        global primeiroMarcaR

        marcaR = 9
         
##        vx_col = []
##        vy_l = []
        for i in range(x): #(x) Colunas (3,4 ) (ok5.bmp)
            soma = int(soma)          
            for j in range(y): # (y) posicao das Linhas (4,5)
                dado = int(matriz[j][i])
##                if (dado == 0): #desenho cor preta
                if (dado == cor):
                    matriz[j][i] = 3 # 3 o valor da 1a posicao, outras recebem 2!!
                    if (primeiraPos == 0):                        
                        PrimeiraPosX = i
                        PrimeiraPosY = j
                        primeiraPos = 1
                        richTextImgP.insert(END,"\n[%d]"%i +"[%d]"%j + "= %d; ;  " %matriz[j][i])
                        richTextImgP.insert(END,"\n PrimPos de X :(%d)"%PrimeiraPosX)
                        richTextImgP.insert(END,"\n PrimPos de Y :(%d)"%PrimeiraPosY)
                    
                        #verifica a segunda pos.: e ja envia para recursao de proximas posicoes 
                        #---------------------------------------------------
                        if ((matriz[j+1][i]) == cor):
                            L_inf = 1
                            soma = soma + 1 #########################################################################
                            richTextImgP.insert(END,"\n ?? LINHA inferior!!")
                            richTextImgP.insert(END,"[%d]"%i +"[%d]"%(j+1))
                            v_ramif[0] = 1
                            marcaL_infX = (j+1) #marcar numeros de ramificacoes do pto inicial - nao usado
                            marcaL_infY = (i)
##                            vx_col.append(j+1)
##                            vy_l.append(i)
                            novoi = i    
                            novoj = j+1
                            marcaR=0
##                        else:
##                            L_inf = 0
                        #---------------------------------------------------    
                        elif ((matriz[j+1][i+1]) == cor):
                            Diag_inf = 1
                            soma = soma + 1 #########################################################################
                            richTextImgP.insert(END,"\n ?? Diagonal Inferior ,, ")
                            richTextImgP.insert(END,"[%d]"%(i+1) +"[%d]"%(j+1) )
                            v_ramif[1] = 1
                            marcaDiag_infX = (j+1)
                            marcaDiag_infY = (i+1)
##                            vx_col.append(j+1)
##                            vy_l.append(i+1)
                            novoi = i +1
                            novoj = j+1
                            marcaR=1
##                        else:
##                            Diag_inf = 0
                        #---------------------------------------------------
                        elif ((matriz[j][i+1]) == cor):
                            Col_lado = 1
                            soma = soma + 1 #########################################################################
                            richTextImgP.insert(END,"\n??Linha - lateral , --Col Lado ")
                            richTextImgP.insert(END,"[%d]"%(i+1) +"[%d]"%j )
                            v_ramif[2] = 1
                            marcaCol_ladoX = (j)
                            marcaCol_ladoY = (i+1)
##                            vx_col.append(j)
##                            vy_l.append(i+1)
                            novoi = i+1
                            novoj = j
                            marcaR=2
##                        else:
##                            Col_lado = 0
                        #---------------------------------------------------
                        elif ((matriz[j-1][i+1]) == cor):
                            Diag_sup  = 1
                            soma = soma + 1 #########################################################################
                            richTextImgP.insert(END,"\n?? Diagonal Superior ,, ")
                            richTextImgP.insert(END,"[%d]"%(i+1) +"[%d]"%(j-1) )
                            v_ramif[3] = 1
                            marcaDiag_supX = (j-1)
                            marcaDiag_supY = (i+1)
##                            vx_col.append(j-1)
##                            vy_l.append(i+1)
                            novoj = j-1
                            novoi = i+1
                            marcaR=3
##                        else:
##                            Diag_sup  = 0                            
                        #---------------------------------------------------
                        if ((matriz[j-1][i]) == cor): # LINHA SUPERIOR (item 4 - quatro)
                            v_ramif[4] = 1
                            L_sup = 1
                            richTextImgP.insert(END,"\n ?? Linha Superior:: ")
                            richTextImgP.insert(END,"[%d]"%(i) +"[%d]"%(j-1) )
##                            vx_col.append(j-1)
##                            vy_l.append(i)
                            novoj = j-1
                            novoi = i
                            marcaR=4
##                            richTextImgP.insert(END,"\n \n... Soma DIAG sup: %d" %somaDiag_sup)                            
##                        else:                            
##                            L_sup  = 0
##                            somaL_sup = 0
                        
                        #---------------------------------------------------
                        elif ((matriz[j-1][i-1]) == cor): # diag SUP esquerda  (item 5 - cinco))
                            Diag_s_esq  = 1
                            marcaR = 5 # 
                            v_ramif[5] = 1
                            somaDiag_s_esq = somaDiag_s_esq + 1
                            soma = soma + 1 #########################################################################
                            
                            richTextImgP.insert(END,"\n ?? diag S esq::")
                            richTextImgP.insert(END,"[%d]"%(i-1) +"[%d]"%(j-1) )
##                            vx_col.append(j-1)
##                            vy_l.append(i-1)
                            novoi = i-1
                            novoj = j-1
                            
##                        else:
##                            Diag_s_esq = 0
                        #---------------------------------------------------
                        elif ((matriz[j][i-1]) == cor): # col lado esquerdo (item 6 - seis)
                            Col_l_esq  = 1
                            v_ramif[6] = 1
                            marcaR = 6 # 
                            richTextImgP.insert(END,"marca R Diag sup ", marcaR)
                            somaCol_l_esq = somaCol_l_esq + 1
                            soma = soma + 1 #########################################################################
                            v_estado_ant[6] = somaCol_l_esq
                            v_estado_ant[8] = 6
                            richTextImgP.insert(END,"\n?? col lado esq: ")
                            richTextImgP.insert(END,"[%d]"%(i-1) +"[%d]"%j)
##                            vx_col.append(j)
##                            vy_l.append(i-1)
                            novoi = i-1
                            novoj = j
                            
                            richTextImgP.insert(END,"\n \n... Soma col L esq: %d" %somaCol_l_esq)
##                        else:
##                            Col_l_esq = 0
#                        #---------------------------------------------------
                        elif ((matriz[j+1][i-1]) == cor): # diag inf esquerda (item 7 - sete)
                            Diag_i_esq = 1
                            v_ramif[7] = 1 
                            richTextImgP.insert(END,"\n ?? Diagonal INF esq :")
                            richTextImgP.insert(END,"[%d]"%(i-1) +"[%d]"%(j+1) )
##                            vx_col.append(j+1)
##                            vy_l.append(i-1)
                            novoi = i-1
                            novoj = j+1
                            marcaR=7
##                        else:
##                            Diag_i_esq = 0
                            

                    
                        n_ramificacoes = L_inf + Diag_inf + Col_lado + Diag_sup + L_sup + Diag_s_esq + Col_l_esq + Diag_i_esq
                        if ( (n_ramificacoes > 1) ):
                            richTextImgP.insert(END,"\n ... MAIS de um pto: n_ram.: %d" %n_ramificacoes)
                            richTextImgP.insert(END,"... vetor_ramif.:")
##                            richTextImgP.insert(END,"\n ... IMG NAO contínua, CAN NOT .. %d" %n_ramificacoes) 
                        
                            for l in range (8):                                
                                richTextImgP.insert(END,"%d" %v_ramif[l])
                                richTextImgP.see(END)
                        else:
##                            verifica_proximo_pvt(novoi,novoj,-1,0)
                            primeiroMarcaR = marcaR
                            verifica_proximo(novoi,novoj,-1,x,y,matriz)                          
                        

def verifica_proximo(i,j,marcaRant,x,y,matriz): #copiado de verifica_proximo_pvt para testes de verificacao multipla de ramificacao
    testex = []
    testey = []
    v_ramif = [0]*8
    v_rx = [0]*8
    v_ry = [0]*8
    v_marcaR = [0]*8
    dado_visitado = int(2)
    matriz[j][i] = dado_visitado
    print ("Novo i..: ",i)
    print ("Novo J..: ",j)
    print ("Novo x..: ",x)
    print ("novo y..: ",y)
    testex.append(i)
    testey.append(j)
    L_inf = 0
    Diag_inf = 0
    Col_lado = 0
    Diag_sup  = 0
    L_sup = 0
    Diag_s_esq = 0
    Col_l_esq = 0
    Diag_i_esq = 0
    novoi = i
    novoj = j
    nova_modificacao = 1
    vx_col.append(i) 
    vy_l.append(j)
    
##    a = len(vx_col)
##    print ("a: ", a)
####    print ("vx: ", vx_col)    
##    x = int(2)
##    
##    xx = int(1)
##if (xx == 1):
    cont = 1
    c = 1
    
   
##    while (nova_modificacao == 1):
    
##        print ("cont", cont)
##        cont = cont + 1
##    for a in range(x): #(x) Colunas (3,4) (ok5.bmp)        
##        for b in range(y): # (y) posicao das Linhas (4,5)
##            dado = int(matriz[b][a])
##            print ("cont", cont)
##            cont = cont + 1
##            if (dado == 0):
##                testex.append(a)
##                testey.append(b)
##    print testex
##    print testey
##    tam = len(testex)
##    print tam
##    for i in range(novoi, x): #(x)     
##        for j in range(novoj, y): # (y)
    
##    for  l in range (tam):
##        print ("i: ", i)
##        print ("j: ", j)
    while (nova_modificacao == 1):
        if  (matriz[j+1][i] == cor): #0
            print("aqui dentro ==0 linf")
            print ("j+1: ", (j+1))

            matriz[j+1][i] = dado_visitado
            nova_modificacao = 1
            L_inf = 1

            richTextImgP.insert(END,"\n LINHA inferior!!")
            richTextImgP.insert(END,"[%d]"%i +"[%d]"%(j+1))
            v_ramif[0] = 1
            marcaR = 0
            print (' linf [%d]' %i +"[%d]"%(j+1))
            
            v_rx[0] = i
            v_ry[0] = j+1
        else:
            L_inf = 0
            v_ramif[0] = 0

        if(matriz[j+1][i+1] == cor): #1

            print ("aqui no diag inf")

            matriz[j+1][i+1] = dado_visitado
            nova_modificacao = 1
            Diag_inf = 1
            

            richTextImgP.insert(END,"\n Diagonal Inferior ,, ")
            richTextImgP.insert(END,"[%d]"%(i+1) +"[%d]"%(j+1) )
            v_ramif[1] = 1
            print (' diag inf [%d]' %(i+1) +"[%d]"%(j+1))        
            marcaR = 1

            v_rx[1] = i+1
            v_ry[1] = j+1
        else:
            Diag_inf = 0
            v_ramif[1] = 0

        if (matriz[j][i+1] == cor) : #2

            print("aqui no COL lado ")

            matriz[j][i+1] = dado_visitado
            nova_modificacao = 1
            Col_lado = 1

            richTextImgP.insert(END,"\n Linha - lateral , --Col Lado ")
            richTextImgP.insert(END,"[%d]"%(i+1) +"[%d]"%j )
            v_ramif[2] = 1
            marcaR = 2

            v_rx[2] = i+1
            v_ry[2] = j
        else:
                Col_lado = 0
                v_ramif[2] = 0


        if(matriz[j-1][i+1] == cor): #3
            print("aqui diag sup  ")
            matriz[j-1][i+1] = dado_visitado
            nova_modificacao = 1
            Diag_sup  = 1
    
            print ('### Aqui DS verific indicess ')
        
            richTextImgP.insert(END,"\n Diagonal Superior ,, ")
            richTextImgP.insert(END,"[%d]"%(i+1) +"[%d]"%(j-1) )
            v_ramif[3] = 1
            marcaR = 3
            v_rx[3] = i+1
            v_ry[3] = j-1

        else:
            Diag_sup  = 0
            v_ramif[3] = 0


        if  (matriz[j-1][i] == cor): #4
            print("aqui no LIN Sup ")
            matriz[j-1][i] = dado_visitado
            nova_modificacao = 1
            print ('### Aqui L sup verific indicess ')
            v_ramif[4] = 1
            L_sup = 1
            richTextImgP.insert(END,"\n Linha Superior:: ")
            richTextImgP.insert(END,"[%d]"%(i) +"[%d]"%(j-1) )
            marcaR = 4

            v_rx[4] = i
            v_ry[4] = j-1
            

        else:                            
            L_sup  = 0
            v_ramif[4] = 0

        if(matriz[j-1][i-1] == cor): #5
            print("aqui no diag sup esq")
            matriz[j-1][i-1] = dado_visitado
            nova_modificacao = 1
            print ('### Aqui D sup ESQ verific indicess ')
            Diag_s_esq  = 1

            v_ramif[5] = 1
            
            richTextImgP.insert(END,"\n diag S esq::")
            richTextImgP.insert(END,"[%d]"%(i-1) +"[%d]"%(j-1) )
            marcaR = 5

            v_rx[5] = i-1
            v_ry[5] = j-1
        else:
            Diag_s_esq = 0
            v_ramif[5] = 0
        if  (matriz[j][i-1] == cor): #6
            print("aqui no col LADO ESQ")
            matriz[j][i-1] = dado_visitado
            nova_modificacao = 1
            print ('### Aqui col lado ESQ verific indicess ')
        
            Col_l_esq  = 1
            v_ramif[6] = 1
            richTextImgP.insert(END,"\n col lado esq: ")
            richTextImgP.insert(END,"[%d]"%(i-1) +"[%d]"%j)
            marcaR = 6

            v_rx[6] = i-1
            v_ry[6] = j
        else:
            Col_l_esq = 0
            v_ramif[6] = 0
        if ((matriz[j+1][i-1]) == cor): #7
            print("aqui DIAG inf ESQ")

            matriz[j+1][i-1] = dado_visitado
            nova_modificacao = 1
            Diag_i_esq = 1
            v_ramif[7] = 1
            
            richTextImgP.insert(END,"\n Diagonal INF esq :")
            richTextImgP.insert(END,"[%d]"%(i-1) +"[%d]"%(j+1))
            marcaR = 7

            v_rx[7] = i-1
            v_ry[7] = j+1
        else:
            Diag_i_esq = 0
            v_ramif[7] = 0
        richTextImgP.insert(END,"\n---------")
##        for i in range(x): #Colunas
##            for j in range(y): #Linhas
##                richTextImgP.insert(END,"\n[%d]"%i +"[%d]"%j + "= %s; ;  " %matriz[j][i])
##        richTextImgP.insert(END,"\n---------")        

        n_ramificacoes = L_inf + Diag_inf + Col_lado + Diag_sup + L_sup + Diag_s_esq + Col_l_esq + Diag_i_esq
        if( (n_ramificacoes == 1) ):
            print (" Ini vrx: ", v_rx)
            print ("ini vrY: ", v_ry)
            print ("ini vramif: ", v_ramif)
##            vx_col.append(v_rx[v_ramif[marcaR]]) 
##            vy_l.append(v_ry[v_ramif[marcaR]])
            print (" fim  vrx: ", v_rx)
            print ("fim   vrY: ", v_ry)
            print ("fim  vramif: ", v_ramif)
            print ("**marca: ", marcaR)
            aa = v_ramif[marcaR]
            novoi = v_rx[marcaR]
            novoj = v_ry[marcaR]
            vx_col.append(v_rx[marcaR]) 
            vy_l.append(v_ry[marcaR])

            i = novoi
            j = novoj
            print ("novo i ===== ", novoi)
            print ("novo j ===== ", novoj)
        else: 
            if (n_ramificacoes > 1) :
                print ("+ d 1 ramif nova fProximo: n_ramif: ", n_ramificacoes)
##                    verifica_n_ramif(v_rx,v_ry,v_ramif,n_ramificacoes,x,y)
                teste = verifica_n_ramif(v_rx,v_ry,v_ramif,n_ramificacoes,x,y)
                
                print ("teste ", teste)
                i = teste[0]
                j = teste[1]                    
                print ("# c chamada", c)
                c = c +1
                print ("teste[0] ===== ", i)
                print ("teste[1]===== ", j)
            else:
                nova_modificacao = 0
                del matriz
                print ("Ok")            
                print ("**** vramif: ", v_ramif)
##                arquivo_XYZ()
                arquivo_LineArc(x,y)


def arquivo_LineArc(tamX,tamY): #alteracoes 02-03-15 inc subversion
    
#comentar as 4 linhas a seguir para conexao TCP

    ftp = FTP("192.168.0.254")
    ftp.login("login", "senha")
    ftp.pwd()
    ftp.cwd("public/Trajectories")
    
#fim comentario
    
    nome = nomearqSalvarImgXYZ.get()
    nome = nome+'.txt'
    print ("nome arquivo: ",nome) 
    escala= float(escalaImg.get())
    escala = escala/100
    
    rearanjar_vetor()
    print ("*************************************************************************************************")

    w = open(nome,'w')

    tam = len(vx_col_novo)
    print ("TAMANHO vetor:", tam)

    anty = float(vy_l_novo[0])*escala
    antx = float(vx_col_novo[0])*escala
    w.write ("FirstTangent = 0; Degrees\n")
    w.write ("DiscontinuityAngle = 0.01; Degrees\n")
    w.write("\n")
##    entrada = str(antx) +","+ str(anty) +","+ Zini
    
    entrada = "Line = " + str(antx) +","+ str(anty)
    
    w.write(entrada)
    w.write("\n")
    
    for i in range(1,tam):
        print ("-------------------*******")
        lin  = float(vy_l_novo[i])*escala
        col =  float(vx_col_novo[i])*escala
        print ("ant x: ", antx)
        print ("ant y: ", anty)
       
        print ("Col: ", col)
        print ("Lin: ", lin)
        
        posx = antx + col
        posy = anty + lin
        print ("posx = %.2f" %antx + "  %.2f" %col)        
        print ("posy = %.2f"  %anty + "  %.2f" %lin)        
        print ("x: " ,posx)
        print ("y: " , posy)
        anty = posy
        antx = posx
        
        x_str = str(posx)
        print("x-str" ,x_str)
        y_str = str(posy)
        print("y-str" ,y_str)
##        entrada = x_str + "," + y_str +","+ Zini
        entrada = "Line = " + x_str + "," + y_str
        print ("entrada: ", entrada)
        w.write(entrada)
##         w.write ("FirstTangent = 0; Degrees\n")
        w.write("\n")
    w.close()
#comentar upload
    upload(ftp, nome)
    richTextImgP.insert(END,"\n\n####################################")
    richTextImgP.insert(END,"\n#File created: %s:\n" %nome)
    richTextImgP.insert(END,"\n ## X: %d; " %tamX + "Y: %d" %tamY)
    richTextImgP.insert(END,"\n ##Relacao Substrate/Imagem:")
    richTextImgP.insert(END,"\n ## (Scale): %.2f" %(escala*100)+"%")
    offsetX = PrimeiraPosX*escala
    offsetY = (tamY-PrimeiraPosY)*escala
    richTextImgP.insert(END,"\n ## OffSet Guide X: %.3f " %offsetX)
    richTextImgP.insert(END,"\n ## OffSet Guide Y: %.3f \n" %offsetY)
    richTextImgP.see(END)
#comentar ftp.quit
    ftp.quit()
    nome2 = nomearqSalvarImgXYZ.get()
    nomearq.set(nome2)
    limpar_vetores()


def rearanjar_vetor(): 
    
    print("#############################################################################################################")
    print("#############################################################################################################")
    antx = PrimeiraPosX
    anty = PrimeiraPosY
    marcaR = primeiroMarcaR
    v_ramif_somasX = [0]*8
    v_ramif_somasY = [0]*8
    global vx_col_novo
    global vy_l_novo 
    vx_col_novo = []
    vy_l_novo = []
##    x = ((float(antx))*escala)
##    y = ((float(anty))*escala)
    x = float(antx)
    y = float(anty)
    somax = int(0)
    somay = int(0)
    sentidox = int(1)
    sentidoy = int(1)
    cont = 0
    print ("marcaR: " ,marcaR)
    mudou_estado = 0
    for i in range(len(vx_col)):
        lin  = vy_l[i]
        col =  vx_col[i]
        print ("ant X: " ,antx)
        print ("ant Y: " ,anty)
        print ("COL: " , vx_col[i])           
        print ("lin: " ,vy_l[i])
        
#         posx = x - ((float(col))*escala)
##        posy = y - ((float(lin))*escala)
        posx = x - float(col)
        posy = y - float(lin)
        print ("-----")
        print (" X: " ,posx)
        print (" Y: " ,posy)

        print vx_col_novo
        print vy_l_novo
        if (antx == col): #0ou4
            if (lin > anty): #0
                if (marcaR != 0):
                    mudou_estado = 1
                    print ("aqui")
                    
                    vx_col_novo.append(v_ramif_somasX[marcaR])
                    vy_l_novo.append(v_ramif_somasY[marcaR])
                    somax= int(0)
                    somay=int(0)
                else:
                    mudou_estado = 0
                marcaR = 0
                print ("antx == col & lin > anty")
                sentidoy = int(1)
                sentidox = int(1)
                somay = somay+1    
                
            else: #4
                if (marcaR != 4):
                    mudou_estado = 1
                    vx_col_novo.append(v_ramif_somasX[marcaR])
                    vy_l_novo.append(v_ramif_somasY[marcaR])
                    somax= int(0)
                    somay=int(0)
                else:
                    mudou_estado = 0
                marcaR = 4
                print ('4')
                somay = somay + 1
                sentidoy = int(-1)
                sentidox = int(1)
            somax = 0
            print("somax: antx = col ", somax)
            print("somay: ", somay)
            v_ramif_somasX[marcaR] = somax*sentidox
            v_ramif_somasY[marcaR] = somay*sentidoy
            
            
    
        else:
            if (anty == lin):#2ou6
                print ('else:  anty == lin:::')       
                if (col > antx): #2
                    if (marcaR != 2):
                        mudou_estado = 1
                        vx_col_novo.append(v_ramif_somasX[marcaR])
                        vy_l_novo.append(v_ramif_somasY[marcaR])
                        somax= int(0)
                        somay=int(0)
                    else:
                        mudou_estado = 0    
                    
                    marcaR = 2
                    print ('col > antx')
                    sentidox = int(-1)
                    sentidoy = int(1)
                    somax = somax + 1
                    
##                    t = (x-posx)/v
                else: #6
                    if (marcaR != 6):
                        mudou_estado = 1
                        vx_col_novo.append(v_ramif_somasX[marcaR])
                        vy_l_novo.append(v_ramif_somasY[marcaR])
                        somax= int(0)
                        somay=int(0)
                    else:
                        mudou_estado = 0   
                    print ('6')
                    marcaR = 6
                    somax = somax+1
                    sentidox = int(1)
                    sentidoy=int(1)
                somay = 0
                print("somax: anty = lin ", somax)
                print("somay: ", somay)
                v_ramif_somasX[marcaR] = somax*sentidox
                v_ramif_somasY[marcaR] = somay*sentidoy
                
            else: #diagonal
                print ('diagonal')       
                if (col > antx): #1ou3
##                    soma = soma+1
                    print ('col > antx')
                    if (lin > anty): #1
                        if (marcaR != 1):
                            mudou_estado = 1
                            vx_col_novo.append(v_ramif_somasX[marcaR])
                            vy_l_novo.append(v_ramif_somasY[marcaR])
                            somax= int(0)
                            somay=int(0)
                        else:
                            mudou_estado = 0
##                        somax = somax+1
##                        somay = somay+1
                        marcaR = 1
                        sentidox = int(-1)
                        sentidoy = int(1)
                        print ('lin > anty')
                        
                    else: #3
                        print ('3')
                        if (marcaR != 3):
                            mudou_estado = 1
                            vx_col_novo.append(v_ramif_somasX[marcaR])
                            vy_l_novo.append(v_ramif_somasY[marcaR])
                            somax= int(0)
                            somay=int(0)
                        else:
                            mudou_estado = 0
                        marcaR = 3
                        sentidox = int(-1)
                        sentidoy = int(-1) 
##                        somax = somax+1
##                        somay = somay+1
                        
                else: #5ou7
                    if  (lin < anty) :#5
                        if (marcaR != 5):
                            mudou_estado = 1
                            vx_col_novo.append(v_ramif_somasX[marcaR])
                            vy_l_novo.append(v_ramif_somasY[marcaR])
                            somax= int(0)
                            somay=int(0)
                        else:
                            mudou_estado = 0
                        marcaR = 5                      
                        print ('anty < lin 5')
                        sentidox = int(1)
                        sentidoy = int(-1)
                        
                        
                    else: #7
                        print ('7')
                        if (marcaR != 7):
                            mudou_estado = 1
                            vx_col_novo.append(v_ramif_somasX[marcaR])
                            vy_l_novo.append(v_ramif_somasY[marcaR])
                            somax= int(0)
                            somay=int(0)
                        else:
                            mudou_estado = 0
                        marcaR = 7
                        sentidox = int(1)
                        sentidoy = int(1)
                somax = somax+1
                somay = somay+1
                print("somax: diag ", somax)
                print("somay: diag ", somay)
                v_ramif_somasX[marcaR] = somax*sentidox
                v_ramif_somasY[marcaR] = somay*sentidoy
            
        
        antx = col
        anty = lin
    #para salvar ultima posicao vertor novo
    vx_col_novo.append(v_ramif_somasX[marcaR])
    vy_l_novo.append(v_ramif_somasY[marcaR])
    #Para considerar a 1a posicao: ajuste considerando a 1a pos.: p ex PRIMEIRA POS 3,4 prox Linf 3,5 , v_novo 0,-4 ; o correto eh 0,-5 :
    vy_l_novo[0] =  vy_l_novo[0] - (PrimeiraPosY - vy_l[0] )
    vx_col_novo[0] = vx_col_novo[0] - (PrimeiraPosX - vx_col[0] )
    for i in range(len(vx_col)):
        richTextImgP.insert(END,"\n[%d]"%i +" = %d"%vx_col[i] + " & %d; ;  " %vy_l[i])
        
    for i in range(len(vx_col_novo)):
        richTextImgP.insert(END,"\n[%d]"%i +" = %d"%vx_col_novo[i] + " & %d; ;  " %vy_l_novo[i])
        
def limpar_vetores():
    del vy_l_novo[:]
    del vx_col_novo[:]
    del vy_l[:]
    del vx_col[:]
    del matriz[:][:]



def buttonTipsImgContorno():
    richTextImgP.insert(END,"\n## TIPS to Image Processing: \n\
- Do not use Extension for File Names\
\n- Read Image File: To .BMP files\
\n- Label Image Regions (Segmentation): Use .PNG file\
\n- (GIMP Program - menu Image - MODE-> indexed)\
\n- SubImage Preview: \n\
  You can use this button only after using \n  'Label Image Regions'\
  - Choose a number to See the segmentation part in Image File \n\
- Sobel Edge map: Image edge detection Filter.\n\
- Skeletonization: Reduces binary objects to 1 pixel wide representations.\
\n--------------------------------------------------------------")
    richTextImgP.see(END)
                        
def bSegmentarImg():
    global im
    global sub_imag
    global seg
    seg = int(1) #marcador uso de segmentação para controle numero de segmentos.
    nome1 = nomearqImgXYZ.get()
    if (nome1 == "") or (nome1 == " "):
        richTextImgP.insert(END,"\n## You must enter an Image File Name! ##\n")
        richTextImgP.see(END)

    else:
        
        nome = nome1+'.png'
        try:
            
            w = open(nome,'r')
            
            richTextImgP.insert(END,"\n#File selected: %s:\n" %nome)
        except:
            
            richTextImgP.insert(END,"\n# Failed to read file: %s:\n" %nome)
        richTextImgP.see(END)
        
        im = misc.imread(nome)
        print "im: ", im
        print label
        print type(label)
        label_image = label(im)
        
        

        sub_imag = []
        cont = int(0)
        richTextImgP.insert (END,"\n# reading image file ...")
        for region in regionprops(label_image):
            
            # draw rectangle around segmented coins
            if region.area > 10:
                cont = cont + 1
                sub_imag.append(region)
                
                c = str(cont)
                novo_nome_seg = nome1+'_seg'+c+'.png'
    ##            misc.imsave(nome1+'_seg'+c+'.png',region.image)
                misc.imsave(novo_nome_seg, region.image)
                richTextImgP.insert (END,"\n(%s) "%c + novo_nome_seg)
                richTextImgP.see(END)
    ##            misc.imsave("ola"+c+'.png',region.image)
            #minr, minc, maxr, maxc = region.bbox
            #print  region.image

            #print dir(region)
        global tam_sub_img
        tam_sub_img = len(sub_imag)
        richTextImgP.insert (END,"\n\n## Number of Files >>> %d" %tam_sub_img)
        richTextImgP.see(END)
        bSeeSubI.config(state='normal')
        textSubImg.config(state='normal')
    print "seg  label", seg
    

def bVerSubImagem_Seg(): #See SubImage - proc imagem, partes segmentadas
    x = textSubImg.get()
    
    try:
        x = int(x)
            
        if x > tam_sub_img or x <= 0:
            richTextImgP.insert (END,"\n\n# Invalid number ... ")
            richTextImgP.see(END)
        else:
            sub = sub_imag[int(x)-1]            
            minr, minc, maxr, maxc = sub.bbox
            b = minc, minr, maxc - minc, maxr - minr
            print "B: ", b
            print "****"
            print minr
            print minc
            print maxr
            print maxc
            print "****"
            im2 = im.astype('uint8')
            #im[im < 1] = 0
            #im[im > 1] = 255
            print ">>>",len(sub_imag)
            im2[minr:maxr,minc:maxc] = 10
            #print b
            pylab.imshow(im2, cmap=pylab.cm.jet)
            pylab.show()
    except: 
        richTextImgP.insert (END,"\n\n# You must enter an Integer Number to See SubImage!")
        richTextImgP.see(END)
    
    
def bSobelSkelImg():
    nome1 = nomearqImgXYZ.get()
    nome = nome1+'.png'
##     novo_nome_seg = nome1+'_seg'+c+'.png'
    
    print "seg sobl", seg
    try:
        print 'Sobel_Skel'
        w = open(nome,'r')
        
        richTextImgP.insert(END,"\n#File selected: %s:\n" %nome)
    except:
    
        richTextImgP.insert(END,"\n# Failed to read file: %s:\n" %nome)
    
    if seg ==0:#marcador segmentacao - numero d arquivos
        total_sub_imgs = 1
        nome1 = nomearqImgXYZ.get()
        if (nome1 == "") or (nome1 == " "):
            richTextImgP.insert(END,"\n## You must enter an Image File Name! ##\n")
            richTextImgP.see(END)
        else:            
            nome = nome1+'.png'
                    
            novo_nome_seg = nome
            print novo_nome_seg
            richTextImgP.insert (END,"\n(%s) " %novo_nome_seg)
            richTextImgP.see(END)
    ##        i_str = str(i)
    ##        img = "ola"+i_str+".png"
    ##        print img
            img = novo_nome_seg
    ##    ##    
            im = Image.open(img)
    ##        
            print im.size
        
            t_im = im.size
            x_im = t_im[0]
            y_im = t_im[1]
    ##
            n_im = Image.new ("L", (x_im+10,y_im+10))
            n_im.paste(im,(5,5))

            nome_nova = "nova_"+nome
            n_im.save(nome_nova)
    ##        
            novaim = scipy.misc.imread(nome_nova)
            novaim = novaim.astype('int32')
    ####
    ####
            nome_sobel = nome1+'_sobel'
    ####        
            print ("Sobel ...")
            dx = ndimage.sobel(novaim, 0)  # horizontal derivative
            dy = ndimage.sobel(novaim, 1)  # vertical derivative
            mag = np.hypot(dx, dy)  # magnitude
            mag *= 255.0 / np.max(mag)  # normalize (Q&D)
            scipy.misc.imsave(nome_sobel+'.png', mag)
            print ("Skel ...  ")
    ##        
            im = scipy.misc.imread(nome_sobel+'.png')
            im[im > 1] = 1
            imagem_pp = np.asarray(im)
            skel = morphology.skeletonize(imagem_pp)
            scipy.misc.imsave(nome_sobel+'_skel.bmp', skel)
            richTextImgP.insert(END,"\n#New file: %s" %nome_sobel+'_skel.bmp')
            richTextImgP.see(END)
            
    ##        scipy.misc.imsave(nome_sobel+"_skel"+i_str+".bmp", skel)
    ##        print ("-------")

    else:
        total_sub_imgs = tam_sub_img
        print "tam_sub_img", tam_sub_img
        print "just ONE file .. "
        for i in range(0,total_sub_imgs):
            print "imagem ", i
            c = str(i+1)
            novo_nome_seg = nome1+'_seg'+c
            print novo_nome_seg
            richTextImgP.insert (END,"\n(%s) "%c + novo_nome_seg+'.png')
            richTextImgP.see(END)
    ##        i_str = str(i)
    ##        img = "ola"+i_str+".png"
    ##        print img
            img = novo_nome_seg+'.png'
    ##    ##    
            im = Image.open(img)
    ##        
            print im.size

    ##        
            t_im = im.size
            x_im = t_im[0]
            y_im = t_im[1]
    ##
            n_im = Image.new ("L", (x_im+10,y_im+10))
            n_im.paste(im,(5,5))

            nome_nova = "nova_"+novo_nome_seg+'.png'
            n_im.save(nome_nova)
    ##        
            novaim = scipy.misc.imread(nome_nova)
            novaim = novaim.astype('int32')
    ####
    ####
            nome_sobel = novo_nome_seg+'_sobel'
    ####        
            print ("Sobel ...")
            dx = ndimage.sobel(novaim, 0)  # horizontal derivative
            dy = ndimage.sobel(novaim, 1)  # vertical derivative
            mag = np.hypot(dx, dy)  # magnitude
            mag *= 255.0 / np.max(mag)  # normalize (Q&D)
            scipy.misc.imsave(nome_sobel+'.png', mag)
            print ("Skel ...  ")
    ##        
            im = scipy.misc.imread(nome_sobel+'.png')
            im[im > 1] = 1
            imagem_pp = np.asarray(im)
            skel = morphology.skeletonize(imagem_pp)
            scipy.misc.imsave(nome_sobel+'_skel.bmp', skel)
            richTextImgP.insert(END,"\n#New file: %s" %nome_sobel+'_skel.bmp')
            richTextImgP.see(END)
                                
            
    ##        scipy.misc.imsave(nome_sobel+"_skel"+i_str+".bmp", skel)
    ##        print ("-------")

    
def bExecImgProc(): #execucao arquivo de trajetoria LineArc
      nome = nomearqSalvarImgXYZ.get()
      v = velImg.get()
      
      n_rep = repImg.get()
  
      if (nome == "") or (nome == " "):
          richTextImgP.insert(END,"\n--------------------------------------------------------------" )
          richTextImgP.insert(END,"\n## You must enter a Traj.File Name! ##\n")
          richTextImgP.see(END)
      else:
        if ( (v == " ") or (n_rep == " ") or (v == "") or (n_rep == "")):
          richTextImgP.insert(END,"\n--------------------------------------------------------------" )
          richTextImgP.insert(END,"\n## You must enter Velocity(float) AND N.rep (integer) ##\n")
          richTextImgP.see(END)
        else:
            nome = nome+".txt"            
            aceleracao = 20
            a= float(aceleracao)
            v = float(v)
            n_rep = int(n_rep)
            status = verificar_statusXY_ImgP()
            if (status ==1):

                    ftp = FTP("192.168.0.254")
                    ftp.login("Administrator", "imp0rt@lib")
                    ftp.pwd()
                    ftp.cwd("public/Trajectories")
                                  
                    try:
                        gettext1(ftp, nome)
                        richTextImgP.insert(END,"\n--------------------------------------------------------------" )
                        richTextImgP.insert(END,"\n # Ok. Start ... Line-Arc Traj file execution: %s\n" %nome)
                        richTextImgP.insert(END," # v.: %.2f mm/s" %v + "; No.rep.: %d \n" %n_rep )
                        richTextImgP.see(END)
                        [errorCode, returnString] = XY.XYLineArcExecution (socketId, group, nome, v, a, n_rep)
    
                    except ftplib.error_perm:
                        richTextImgP.insert(END,"\n--------------------------------------------------------------" )

                        richTextImgP.insert(END,"\n##Error: FILE not Found: %s"% nome)
                        richTextImgP.see(END)
                        os.unlink(nome)
                    ftp.quit()



        #fim aba7 img proc sobel skel
##################################################################################################



def buttonVerPosicoesOrigin(): # aba Origin
      status = verificar_statusXY_Origin()
      if ((status ==1) or (status ==2)):
            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
            [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
            [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
            [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
            rel_guiaX = float(GUIAx - currentPositionx)
            rel_guiaY = float(GUIAy - currentPositiony)            
            richTextOrigin.insert(END,"\n# X: %.2f;   " %currentPositionx)
            richTextOrigin.insert(END," Y: %.2f;   \n" %currentPositiony)
            richTextOrigin.insert(END,"# Z: %.2f;     " %currentPositionz)
            richTextOrigin.insert(END," Act: %.2f \n" %currentPositionAct)
            richTextOrigin.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
            
            if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                richTextOrigin.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                richTextOrigin.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
            richTextOrigin.see(END)

def buttonVerPosicoesOrigin2(): # aba Origin
      status = verificar_statusXY_Init()
      if ((status ==1) or (status ==2)):
            [errorCode, currentPositionx] = XY.GroupPositionCurrentGet(socketId, positionerx, 1)
            [errorCode, currentPositiony] = XY.GroupPositionCurrentGet(socketId, positionery, 1)
            [errorCode, currentPositionz] = SingleZ.GroupPositionCurrentGet(socketIdz, positionerz, 1)
            [errorCode, currentPositionAct] = SingleAct.GroupPositionCurrentGet(socketIdz, positionerAct, 1)
            rel_guiaX = float(GUIAx - currentPositionx)
            rel_guiaY = float(GUIAy - currentPositiony)            
            richTextOrigin.insert(END,"\n# X: %.2f;   " %currentPositionx)
            richTextOrigin.insert(END," Y: %.2f;   \n" %currentPositiony)
            richTextOrigin.insert(END,"# Z: %.2f;     " %currentPositionz)
            richTextOrigin.insert(END," Act: %.2f \n" %currentPositionAct)
            richTextOrigin.insert(END,"SHIFT GUIDE: (%.4f, "%rel_guiaX+ "%.4f" %rel_guiaY +")\n")
            
            if ((rel_guiaX < -0.0001) or (rel_guiaY < -0.0001) or (rel_guiaX > 130.00) or (rel_guiaY > 160.00)):
                richTextOrigin.insert(END,"\n## Be careful about the draw ~direction/sense~ and the Substrate Size!! ")
                richTextOrigin.insert(END,"\n## For this Shift Guide Value, the draw is Out \nof  'Alumina Guide'! ##\n")                         
            richTextOrigin.see(END)
            return currentPositionx, currentPositiony

def bCriaArquivoOrigin(x,y):
##  #x,y: posicoes atuais absolutas da guia
    richTextOrigin.insert(END,"\n-----------------------------------------------------------------" )
    print 'criar arq nova guia'
    print x
    print type(x)
    print y

    x = '%.*f'%(2,x)
    y = '%.*f'%(2,y)
    
   
    nome_anterior = "guia_anterior.txt"
    nome_atual = "definicao_guia_valores_absolutos.txt"
    nome_log = "log_definicao_guia.txt"
    
    
    now = datetime.now()
    
    ftp = FTP("192.168.0.254")
    
    ftp.login("Administrator", "imp0rt@lib")
    
    ftp.pwd()
    ftp.cwd("public/guia")
    
    
## x = '%.*f'%(2,x)
    
    print "novos val"
    print x
    print y
 
    conteudo = gettext_nova_guia(ftp, nome_atual)
    print "conteudo", conteudo

    print "type cont x", type(conteudo[0])
    print "type x", type(x)
    print (conteudo[1] == x)
    
    
    if ( (conteudo[1] == x) and (conteudo[2] == y) ):
        richTextOrigin.insert(END,"\n# Current positions already set!\n")
        richTextOrigin.see(END)
    else:

        conteudoX = str(conteudo[1] +"\n")
        conteudoY = str(conteudo[2])
          
        try:
            
            w = open(nome_anterior,'w')
            w.write(conteudoX) 
            w.write(conteudoY)   
            richTextOrigin.insert(END,"\n#File created: %s:\n" %nome_anterior)
        except:
            
            richTextOrigin.insert(END,"\n# Failed to create file: %s:\n" %nome_anterior)
            
        w.close
        w = open(nome_anterior,'r')
        upload(ftp, nome_anterior)
        w.close
        richTextOrigin.see(END)
        try:
            
            w = open(nome_atual,'w')
            w.write("0\n")
            w.write(x+"\n") #
            w.write(y) 
            richTextOrigin.insert(END,"\n#File created: %s:\n" %nome_atual)
        except:
            
            richTextOrigin.insert(END,"\n# Failed to create file: %s:\n" %nome_atual)
        richTextOrigin.see(END)
        w.close
        w = open(nome_atual,'r')
        upload(ftp, nome_atual)
        w.close

        print "Nova guia definida dd/mm/aaaa: %d/%02d/%d - horario: %dh %dmin." %(now.day, now.month, now.year, now.hour, now.minute)
    ##    log = (now.day, now.month, now.year, now.hour, now.minute)
        log = "Nova guia definida dd/mm/aaaa: %02d/%02d/%d - horario: %dh %dmin.\n" %(now.day, now.month, now.year, now.hour, now.minute)
        print "log", log
        
        salvar_log = str(log)
        print "salvar arquivo LOG: ",salvar_log
        
        try:
            
            w = open(nome_log,'a') #'a' = APPEND 
            w.write("******************************\n")
            w.write(salvar_log)
            
            w.write("X: "+x+"\n") 
            w.write("Y: "+y+"\n")
            richTextOrigin.insert(END,"\n#File created: %s:\n" %nome_log)
        except:    
            richTextOrigin.insert(END,"\n# Failed to create file: %s:\n" %nome_log)
        richTextOrigin.see(END)
        w.close
        w = open(nome_log,'r')
        upload(ftp, nome_log)
        w.close
        ftp.close()
        richTextOrigin.see(END)
        buttonShowInfoOrigin()
        


##class FTPConnection(object):
##    def __init__(self, server, username, password):
##        self.server = server
##        self.username = username
##        self.password = password
##    def __enter__(self):
##        self.ftp = FTP(self.server)
##        self.ftp.login(self.username,self.password)
##        return self
##    def __exit__(self, type, value, traceback):
##        self.ftp.quit()
##    def writeserverfile(self, serverpath, filename, path):        
##        self.ftp.cwd(serverpath)
##        self.ftp.storlines('STOR '+filename, open(path,'r'))
##
##
##while True:
##
##    with FTPConnection(server,username,password) as ftp:
##        ftp.writeserverfile(self, serverpath, filename, path)


def askopenfilename_teste():

    global filterdata, lowwave, highwave
    
    fil=pyfits.open(tkfile.askopenfilename(**root.file_opt))

    fil=pyfits.open(tkfile.askopenfilename(**root.file_opt))

     

    filterdata= fil[1].data

    lowwave=entryWidget.get().strip()

    highwave=entryWidget2.get().strip()

    root.destroy()

def handler1(event):
    current = box.current()
    if current != -1:
        nomearqSalvar.set(box.get())
        
        
##        print ("ola")
##        for label in labels.values():
##            label.config(relief='flat')
##        value = values[current]
##        label = labels[value]
##        label.config(relief='raised')



# define the callback
##var = StringVar()  # create a var object
def tracer(name, idontknow, mode):
    
    # I cannot find the arguments sent to the callback documented
    # anywhere, or how to really use them.  I simply ignore
    # the arguments, and use the invocation of the callback
    # as the only api to tracing
    print arq_combo.get()

##var.trace('w', tracer)
# 'w' in this case, is the 'mode', one of 'r'
# for reading and 'w' for writing

##var.set('Foo')  # manually update the var...

# 'Foo' is printed


def buttonDefineGuiaNova():
##    richTextOrigin.insert(END,"\n## New values for Alumina Guide 'Alumina Guide'! ##\n")
##    richTextOrigin.see(END)
##    global GUIAx 
##    global GUIAy
    h = buttonVerPosicoesOrigin2()
    GUIAx = h[0]
    GUIAy = h[1]
    
    print h
    print ("guia x new: ", GUIAx)
    print ("guia y new: ", GUIAy)
    bCriaArquivoOrigin(GUIAx, GUIAy)

    
def buttonResetGuiaNova():
    
##  #x,y: posicoes atuais absolutas da guia
    richTextOrigin.insert(END,"\n-----------------------------------------------------------------" )
##    print 'criar arq nova guia'
##    print x
##    print type(x)
##    print y
##
##    x = '%.*f'%(2,x)
##    y = '%.*f'%(2,y)
   
    nome_anterior = "guia_anterior.txt"
    nome_atual = "definicao_guia_valores_absolutos.txt"
    nome_log = "log_definicao_guia.txt"
    
    now = datetime.now()
    
    ftp = FTP("192.168.0.254")
    
    ftp.login("Administrator", "imp0rt@lib")
    ftp.pwd()
    ftp.cwd("public/guia")
    
## x = '%.*f'%(2,x)
    
##    print "novos val"
##    print x
##    print y
 
    atual = gettext_nova_guia(ftp, nome_atual)
    anterior = gettext_nova_guia(ftp, nome_anterior)
    print "atual ", atual
    print "anterior", anterior

##    ##remover para permitir LOOP de reset :(
##    if ( (conteudo[0] == '1')):
##        richTextOrigin.insert(END,"\n# Warning: Guide already Reseted!\n")
##        richTextOrigin.see(END)


    conteudoX_atual = str(atual[1] +"\n")
    conteudoY_atual = str(atual[2])

    conteudoX_anterior = str(anterior[0] +"\n")
    conteudoY_anterior = str(anterior[1])

    print "conteudoX_atual ", conteudoX_atual
    print "conteudoY_atual", conteudoY_atual
    print "conteudoX_anterior ", conteudoX_anterior
    print "conteudoY_anterior", conteudoY_anterior
      
    try:        
        w = open(nome_anterior,'w')
        w.write(conteudoX_atual) 
        w.write(conteudoY_atual)   
        richTextOrigin.insert(END,"\n#File created: %s:\n" %nome_anterior)
    except:
        
        richTextOrigin.insert(END,"\n# Failed to create file: %s:\n" %nome_anterior)
    richTextOrigin.see(END)      
    w.close
    w = open(nome_anterior,'r')
    upload(ftp, nome_anterior) #envio arq anterior
    w.close
    try:
##        
        w = open(nome_atual,'w')
        w.write("1\n")
        w.write(conteudoX_anterior) 
        w.write(conteudoY_anterior)   
        richTextOrigin.insert(END,"\n#File created: %s:\n" %nome_atual)
    except:
        richTextOrigin.insert(END,"\n# Failed to create file: %s:\n" %nome_atual)
    richTextOrigin.see(END)
    w.close
    w = open(nome_atual,'r')
    upload(ftp, nome_atual)
    w.close
##
    
####    log = (now.day, now.month, now.year, now.hour, now.minute)
    log = "Nova guia (RESET) definida dd/mm/aaaa: %02d/%02d/%d - horario: %dh %dmin.\n" %(now.day, now.month, now.year, now.hour, now.minute)
    print "log", log
##    
    salvar_log = str(log)
    print "salvar arquivo LOG: ",salvar_log
##    
    try:
        print "here"
##        
        w = open(nome_log,'a') #'a' = APPEND
        w.write("******************************\n")
        w.write(salvar_log)
        w.write("X: "+conteudoX_anterior)
        w.write("Y: "+conteudoY_anterior+"\n") 
##            w.write("Y: "+y+"\n")
        
##        w.write("******************************\n")
##        w.write(salvar_log)
##        write("X: "+conteudoX_anterior)
##        w.write("Y: "+conteudoY_anterior+"\n")
        print "Cont" , conteudoX_anterior
##        newx = "X: "+conteudoX_anterior
##        newy = "Y: "+conteudoy_anterior
##        print "new x ", newx
##        print "new y ", newy
        

        
##        w.write("Y: "+conteudoY_anterior+"\n")  
        richTextOrigin.insert(END,"\n#File created: %s:\n" %nome_log)
    except:
##        
        richTextOrigin.insert(END,"\n# Failed to create file: %s:\n" %nome_log)
    w.close
    w = open(nome_log,'r')
    upload(ftp, nome_log)
    w.close
    ftp.close()
    richTextOrigin.see(END)
    buttonShowInfoOrigin()

def buttonVerLogFile():
    richTextOrigin.insert(END,"\n-----------------------------------------------------------------" )
    nome_log = "log_definicao_guia.txt"
    now = datetime.now()    
    ftp = FTP("192.168.0.254")
    ftp.login("Administrator", "imp0rt@lib")
    ftp.pwd()
    ftp.cwd("public/guia") 
    try:
        richTextOrigin.insert(END,"\n## LOG FILE - GUIDE SETTINGS ##\n" )
        log = gettext_nova_guia(ftp, nome_log)
        x = len(log)
        
        for i in range(x):
            richTextOrigin.insert(END,"\n%s"%log[i])
            richTextOrigin.see(END)

 
    except:
##        
        richTextOrigin.insert(END,"\n# Failed to read file: %s:\n" %nome_log)
    
    ftp.close()
    richTextOrigin.see(END)

def verificar_posicoes_Guia():
    global GUIAx ################ incluir VALORes DO guia NO """ buttonHomeClick""" 
    global GUIAy
    
##    GUIAx = 47.13 # 28/08/2015
##    GUIAy = 38.24 #
    richTextOrigin.insert(END,"\n-----------------------------------------------------------------" )
    nome_atual = "definicao_guia_valores_absolutos.txt"
    try:
        ftp = FTP("192.168.0.254")
    
        ftp.login("Administrator", "imp0rt@lib")
        ftp.pwd()
        ftp.cwd("public/guia")
        atual = gettext_nova_guia(ftp, nome_atual)
        print "atual ", atual
        atual_x = str(atual[1] +"\n")
        atual_y = str(atual[2])
        
        richTextOrigin.insert(END,"\n# Trying to read the file with the Guide\n# Positions:\n ' %s: '\n" %nome_atual)
        richTextInit.insert(END,"\n# Trying to read the file with the Guide\n# Positions:\n ' %s: '\n" %nome_atual)
                
        GUIAx = atual_x
        GUIAy = atual_y
        GUIAx = float(GUIAx)
        GUIAy = float(GUIAy)
        richTextOrigin.insert(END,"\n## Guia x: %.2f" %GUIAx)
        richTextOrigin.insert(END,"\n## Guia Y: %.2f\n" %GUIAy)
        richTextInit.insert(END,"\n## Guia x: %.2f" %GUIAx)
        richTextInit.insert(END,"\n## Guia Y: %.2f\n" %GUIAy)
##        w.close
    except:
        
        richTextOrigin.insert(END,"\n# Failed to Read file: %s:\n" %nome_atual)
        richTextOrigin.insert(END,"\n# Controller are ON? \n# Check the connection between PC and Controller")
        richTextInit.insert(END,"\n# Failed to Read file: %s:\n" %nome_atual)
        richTextInit.insert(END,"\n# Controller are ON? \n# Check the connection between PC and Controller")
    richTextOrigin.see(END)
    richTextInit.see(END)      
                

def buttonTipsOrigin():
    richTextOrigin.insert(END,"\n###################################\n * TIPS to SAVE a NEW GUIDE POSITIONS * \n\n\
# The Motion Controller must be ON!\n\n# You can Define a new guide or\n# You can Reset to previous positions\n\n# It will be save a LOG File every Change \n\
# You can see it any time (ViewLogFile button)\n\n# If you want to use the Absolute positions saved in Log File - go to 'Basic Movements' \n\n\
# AFTER alteration - You must reload this software -> The software will be closed!!\n\n")
                          
    richTextOrigin.see(END)

#--------------------------------------------------------------------------------------------------------
#MAIN
# ()()()()()()()()()()()()()()()()()()()()# ()()()()()()()()()()()()()()()()()()()() MAIN
# ()()()()()()()()()()()()()()()()()()()()# ()()()()()()()()()()()()()()()()()()()()

####  GUIAx = 13
####  GUIAy = 44

global fatorColuna
fatorColuna = -1

global seg
seg = 0
global marca1radio
marca1radio = -1
global marcaUnidade
marcaUnidade = -1

global fatorUn
fatorUn = 1

global fatorUnBasic
fatorUnBasic = 1

global xisY
xisY = 1

##global GUIAx ################ incluir VALORes DO guia NO """ buttonHomeClick""" 
##global GUIAy

global GUIAx ################ incluir VALORes DO guia NO """ buttonHomeClick""" 
global GUIAy
GUIAx = float(0.00)
GUIAy = float(0.00)
global cor #guia ip
cor = int(255) #branco

##GUIAx = 13.00
##GUIAy = 44.00
##GUIAx = 12.40
##GUIAy = 44.80
##GUIAx = 32.40
##GUIAy = 44.80
##GUIAx = 51.10 #(shift guide ant -18.70)
##GUIAy = 58.30 #(shift guide ant -13.50)

##GUIAx = 46.10 #(shift guide ant 5.00)
##GUIAy = 58.30 #(shift guide ant 0.00)



##GUIAx = 47.13 # 28/08/2015
##GUIAy = 38.24 #
##
##
##GUIAx = float(GUIAx)
##GUIAy = float(GUIAy)
global matriz
matriz = []
global vx_col
global vy_l
vx_col = []
vy_l = []


global marcar_vnr
marcar_vnr = 0
global PositionersInit
PositionersInit = 0

##################################################################################################
##################################################################################################
## CONTROLADORA
# Instantiate the class

XY = XPS_C8_drivers1.XPS()
XYZ = XPS_C8_drivers1.XPS()
SingleZ = XPS_C8_drivers1.XPS()
SingleAct = XPS_C8_drivers1.XPS()
####
####
# Connect to the XPS

try:
    
    socketId = XY.TCP_ConnectToServer('192.168.0.254', 5001, 20)
    socketId2 = XY.TCP_ConnectToServer('192.168.0.254', 5001, 20)

    socketIdXYZ = XYZ.TCP_ConnectToServer('192.168.0.254', 5001, 20)

    socketIdz = SingleZ.TCP_ConnectToServer('192.168.0.254', 5001, 20)

    socketIdAct = SingleAct.TCP_ConnectToServer('192.168.0.254', 5001, 20)

    ####
    ##### Check connection passed
    print ('Check conection, wait')
    ##socketId = -1 ### ~ Teste para Não desligar Controladora ###
    if (socketId == -1):
        print ('Connection to XPS failed -> check IP & Port!')
        sys.exit()
    else:
        print ('Connection to XPS Controller OK. Socket num: ' , socketId)
    
except:
    print ('Connection to XPS failed -> check IP & Port!')
    
##
##    if (socketIdXYZ == -1):
##        print ("conection to XYZ  group FAILED.")       
##    print ('Connection to XPS Controller - group XY - OK. Socket num: ' , socketIdXYZ)


# Define the positioner
group = 'XY'
group1 = 'XYZ'
z = 'SingleZ'
act = 'SingleAct'

positionerx = group + '.X'
positionery = group + '.Y'
positionerz = z + '.Pos'
positionerAct = act + '.Pos'

posNovoz = group1 + '.Z'
posNovoy = group1 + '.Y'
posNovox = group1 + '.X'
##print ("pos: ", posNovox)
##print ("pos: ", posNovoy)
##print ("pos: ", posNovoz)

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

form1=Tk()
form1.title('XPS C8 Motion Controller - DT3D/CTI Renato Archer - www.cti.gov.br')
form1.resizable(width=TRUE, height=TRUE)
##import form2

##form2=Tk()
##form2.title('ABORT MOVEMENTS')
##form2.resizable(width=FALSE, height=FALSE)
##form2.geometry('250x200+0+0')
##
##buttonAbort=Button(form2,text=' ABORT MOVEMENTS ', command=bAbort,style = "TButton")
##buttonAbort.place(relx=0.03, rely=0.12, relwidth=0.65, relheight=0.25)

abas = Notebook(form1)
frame_aba1 = Frame(abas)
frame_aba2 = Frame(abas)
frame_aba3 = Frame(abas)
frame_aba4 = Frame(abas)
frame_aba5 = Frame(abas)
frame_aba6 = Frame(abas)
frame_aba7 = Frame(abas)
frame_aba8 = Frame(abas)
frame_aba9 = Frame(abas)
frame_aba10 = Frame(abas)

label1 = Label(frame_aba1,text="CTI - Centro de Tecnologia da Informação Renato Archer -Campinas/SP\n  - www.cti.gov.br \n  - Divisão de Tecnologias Tridimensionais (DT3D)\
\n\n\n Sistema:\n\n  - Laser Ultravioleta 355nm\n  - Controladora de Movimentos Newport XPS-C8 com sistema de tempo real VxWorks\
\n  - Posicionadores: \n   -  X e Y: 400mm -> [-200, 200]mm. Velocidade máxima: 100mm/s. \
\n   - Z(foco): 4.8mm -> [-2.4, 2.4]mm. Velocidade máxima: 5mm/s. \n \
- Atuador: 25mm-> [0, 25]mm. Velocidade máxima: 0.4mm/s.  \n\n  ")
label1.place(relx=0.01, rely=0.10, relwidth=0.35, relheight=0.19)
label1.pack(padx=130, pady=130)


image = Image.open("logo.png") #Logotipo CTI
photo = ImageTk.PhotoImage(image)

label_logo = Label(frame_aba1,image=photo)
label_logo.image = photo 
label_logo.place(relx=0.00, rely=-0.030, relwidth=0.35, relheight=0.30)

########################################### ###########################################
#ini ########################################### ABA 2 Init
labelTraj=Label(frame_aba2, font="{Arial black} 9",text='System Initialization')#acima do richTextArq !!
labelTraj.grid(column=0 ,row = 0)
 
buttonHome=Button(frame_aba2,text='   Initialize \n Positioners', command=buttonInit_novo,style = "TButton")
buttonHome.place(relx=0.03, rely=0.12, relwidth=0.15, relheight=0.11)


buttonHome1=Button(frame_aba2,text='Move to HOME \n    Positions ', command=buttonHomeClick2_novo,style = "TButton")
buttonHome1.place(relx=0.20, rely=0.12, relwidth=0.16, relheight=0.11)

buttonDisable=Button(frame_aba2,text='     DISABLE \n   Positioners   ', command=buttonDisable,style = "TButton")
buttonDisable.place(relx=0.03, rely=0.79, relwidth=0.16, relheight=0.11)

buttonEnable=Button(frame_aba2,text='    ENABLE \n Positioners', command=buttonEnable,style = "TButton")
buttonEnable.place(relx=0.20, rely=0.79, relwidth=0.16, relheight=0.11)

labelAtuador=Label(frame_aba2,text='Linear Actuator (focus) [mm]:')
labelAtuador.place(relx=0.03, rely=0.3, relwidth=0.23, relheight=0.05)

labelMovAtuador=Label(frame_aba2,text='Move to:',font = '{Arial } 8')
labelMovAtuador.place(relx=0.033, rely=0.370, relwidth=0.08, relheight=0.05)

movAtuador=StringVar() #Linha: Coord Y1 Y_final
textMovAtuador=Entry(frame_aba2,font = '{Arial} 9',textvariable = movAtuador)
textMovAtuador.place(relx=0.1, rely=0.37, relwidth=0.07, relheight=0.05)
movAtuador.set("")

buttonAtuador=Button(frame_aba2,text='Go', command=buttonAtuador,style = "C.TButton")
buttonAtuador.place(relx=0.175, rely=0.365, relwidth=0.10, relheight=0.07)

labelFoco=Label(frame_aba2,text='Vertical Positioner (Z) [mm]: ')
labelFoco.place(relx=0.03, rely=0.57, relwidth=0.23, relheight=0.05)

labelMovAtuador=Label(frame_aba2,text='Move to:',font = '{Arial } 8')
labelMovAtuador.place(relx=0.033, rely=0.64, relwidth=0.08, relheight=0.05)

textBoxFoco=Entry(frame_aba2,font = '{Arial} 9')
textBoxFoco.place(relx=0.1, rely=0.64, relwidth=0.07, relheight=0.05)

buttonFoco=Button(frame_aba2,text='Go', command=buttonFoco,style = "C.TButton")
buttonFoco.place(relx=0.175, rely=0.635, relwidth=0.10, relheight=0.07)

buttonVerPos=Button(frame_aba2,text='READ Positions', command=buttonVerPosicoesClick2,style = "TButton") # aba Initialization
buttonVerPos.place(relx=0.33, rely=0.47, relwidth=0.18, relheight=0.125)


##labelCopy=Label(frame_aba2,text='Copy "Command responses" to:')
##labelCopy.place(relx=0.30, rely=0.46, relwidth=0.26, relheight=0.05) 
##
##checkTEa=IntVar()
##check1=Checkbutton(frame_aba2,text=' Trajectory Execution TAB', offvalue=0, onvalue=1,variable= checkTEa, command=checkTE)# copy to traj exec
##check1.place(relx=0.31, rely=0.51, relwidth=0.26, relheight=0.05)
##check1.var = checkTEa
##
##checkIE=IntVar()
##check2=Checkbutton(frame_aba2,text=' Image Execution TAB', command=checkIE, variable=checkIE)# copy to image exec
##check2.place(relx=0.31, rely=0.56, relwidth=0.22, relheight=0.05)
##

#------------------- richtext Initialization ----------------
labelRichInit=Label(frame_aba2,text='Command responses:')
labelRichInit.place(relx=0.69, rely=0.0841, relwidth=0.19, relheight=0.06) 

richTextInit=Text(frame_aba2,font = '{Arial} 9',wrap=WORD)
richTextInit.place(relx=0.60, rely=0.13, relwidth=0.37, relheight=0.70)
##richTextBox1.focus_set()
s=Scrollbar(richTextInit,cursor="arrow")
s.pack(side=RIGHT)
s.config(command=richTextInit.yview)
richTextInit.config(yscrollcommand=s.set)

richTextInit.insert(END, "\n# Use 'Positioners Init.' button just after \n Turning On the Controller.\n# Use 'Move to HOME Positions' button for \n moving to GUIDE Position.\n")

#- FIM ------------------ richtext Initialization ----------------
buttonLimpar=Button(frame_aba2,text='Clear Form', command=buttonLimparClickInit,style = "TButton")
buttonLimpar.place(relx=0.73, rely=0.86, relwidth=0.12, relheight=0.07)

########################################### ########################################### 
#fim ########################################### ABA 2 Init


########################################### ########################################### 
#ini ########################################### ABA 3 BASIC

labelBasic=Label(frame_aba3, font= "{Arial black} 9",text='Basic Movements')
labelBasic.grid(column=0 ,row = 0)

# ---- ini relative movements aba basic ----------------------------------------

labelArq=Label(frame_aba3,text='Relative Movements:')
labelArq.place(relx=0.01, rely=0.1, relwidth=0.21, relheight=0.05)

labelVelRelative=Label(frame_aba3,text='V(mm/s):',font = '{Arial } 8')
labelVelRelative.place(relx=0.013, rely=0.15, relwidth=0.07, relheight=0.05)

velRelativeBasic=StringVar() #
textVelRelativeBasic=Entry(frame_aba3,font = '{Arial} 9',textvariable = velRelativeBasic) #inserir botoes direcionais desta aba
textVelRelativeBasic.place(relx=0.1, rely=0.15, relwidth=0.06, relheight=0.05)
velRelativeBasic.set("2")

#mm aba3 basic
radioMm1=Radiobutton(frame_aba3,text='mm', command=radioMmBasic, value = 0)
radioMm1.place(relx=0.015, rely=0.28, relwidth=0.06, relheight=0.06)
radioMm1.invoke()
#um aba3 basic
radioUmBasic=Radiobutton(frame_aba3,text='µm ', command=radioUmBasic,  value=3)
radioUmBasic.place(relx=0.014, rely=0.215, relwidth=0.06, relheight=0.06)

bYpos1=Button(frame_aba3,text='↑', command=YposBasic,style = "TButton")
bYpos1.place(relx=0.16, rely=0.1750, relwidth=0.03, relheight=0.072)

bXneg1=Button(frame_aba3,text='←', command=XnegBasic,style = "TButton")
bXneg1.place(relx=0.1, rely=0.24, relwidth=0.04, relheight=0.06)

textMovRelBasic=StringVar() #text velocidade p/ mov relativo aba 3 basic
textCoordB=Entry(frame_aba3,font = '{Arial} 9',foreground="#5C4033" , textvariable=textMovRelBasic)
textCoordB.place(relx=0.14, rely=0.245, relwidth=0.07, relheight=0.05)
textMovRelBasic.set ("25")

bXpos1 = Button(frame_aba3,text='→', command=XposBasic,style = "TButton")
bXpos1.place(relx=0.21, rely=0.24, relwidth=0.04, relheight=0.06)

bYneg1=Button(frame_aba3,text='↓', command=YnegBasic, style = "TButton")
bYneg1.place(relx=0.16, rely=0.296, relwidth=0.03, relheight=0.072)
# ---- fim relative movements aba basic ----------------------------------------

buttonHome2=Button(frame_aba3,text='Move to Origin', command=buttonHomeClickBasic,style = "TButton")
buttonHome2.place(relx=0.362, rely=0.22, relwidth=0.16, relheight=0.11)


# ---- ini shift guide aba 3 basic ----------------------------------------
labelShift=Label(frame_aba3,text='Offset from Origin of Positioning Guide [mm]')
##                 Shift Guide Absolute Movement [mm]:')# -- SHIFT GUIDE !!! aba 3 BASIC 
labelShift.place(relx=0.01, rely=0.386, relwidth=0.299, relheight=0.05)

labelX1arq=Label(frame_aba3,text='X:')# -- SHIFT GUIDE !!! aba 3 BASIC 
labelX1arq.place(relx=0.014, rely=0.44,  relwidth=0.02, relheight=0.06)######
labelY1arq=Label(frame_aba3,text='Y:')
labelY1arq.place(relx=0.12, rely=0.44, relwidth=0.03, relheight=0.06)

shiftXbasic=StringVar() # -- SHIFT GUIDE !!! aba 3 BASIC 
textShiftXbasic=Entry(frame_aba3,font = '{Arial} 9',textvariable = shiftXbasic)
textShiftXbasic.place(relx=0.035, rely=0.44, relwidth=0.07, relheight=0.05)
shiftXbasic.set("6.2")

shiftYbasic=StringVar() # -- SHIFT GUIDE !!! aba 3 BASIC 
textShiftYbasic=Entry(frame_aba3,font = '{Arial} 9',textvariable = shiftYbasic)
textShiftYbasic.place(relx=0.14, rely=0.44, relwidth=0.07, relheight=0.05)
shiftYbasic.set("12.5")

bOk=Button(frame_aba3,text='Go', command=bGoShiftBasic,style = "C.TButton") # -- SHIFT GUIDE !!! aba 3 BASIC 
bOk.place(relx=0.22, rely=0.435, relwidth=0.06, relheight=0.06)
# ---- fim shift guide aba 3 basic ----------------------------------------


#- ini abslotue mov aba 3 basic ----------------------------------------------------
labelArq=Label(frame_aba3,text='Absolute Movements [mm]:')
labelArq.place(relx=0.01, rely=0.55, relwidth=0.21, relheight=0.05)

labelAbsMov=Label(frame_aba3,text='Move X to:',font = '{Arial } 8')
labelAbsMov.place(relx=0.013, rely=0.60, relwidth=0.08, relheight=0.05)

textAbsX=Entry(frame_aba3,font = '{Arial} 9')
textAbsX.place(relx=0.09, rely=0.60, relwidth=0.07, relheight=0.05)

labelAbsMov1=Label(frame_aba3,text='Move Y to:',font = '{Arial } 8')
labelAbsMov1.place(relx=0.013, rely=0.66, relwidth=0.08, relheight=0.05)

textAbsY=Entry(frame_aba3,font = '{Arial} 9')
textAbsY.place(relx=0.09, rely=0.66, relwidth=0.07, relheight=0.05)

bMoveAbs=Button(frame_aba3,text='Go', command=bGoAbs,style = "C.TButton") # -- MOVE ABS (X and Y): "Go" !!! aba 3 BASIC 
bMoveAbs.place(relx=0.17, rely=0.62, relwidth=0.06, relheight=0.07)

buttonVerPos=Button(frame_aba3,text='READ Positions', command=buttonVerPosicoesClickBasic,style = "TButton") # aba Initialization
buttonVerPos.place(relx=0.35, rely=0.42, relwidth=0.18, relheight=0.125)


#- ini abslotue mov aba 3 basic ----------------------------------------------------

#-------- ini richtextBasic aba 3 basic -------------------
labelRichTextBasic=Label(frame_aba3,text='Command responses:')
labelRichTextBasic.place(relx=0.69, rely=0.0841, relwidth=0.19, relheight=0.06) 

richTextBasic=Text(frame_aba3,font = '{Arial} 9',wrap=WORD)
richTextBasic.place(relx=0.60, rely=0.13, relwidth=0.37, relheight=0.70)
##richTextBox1.focus_set()
s=Scrollbar(richTextBasic,cursor="arrow")
s.pack(side=RIGHT)
s.config(command=richTextBasic.yview)
richTextBasic.config(yscrollcommand=s.set)
richTextBasic.insert (END,"\n# You can edit this form and save it in a log file below.\n")


#alterar posicao - diferent no 
##buttonVerPos=Button(frame_aba3,text='READ Positions', command=buttonVerPosicoesClick,style = "TButton")
##buttonVerPos.place(relx=0.287, rely=0.23, relwidth=0.17, relheight=0.09)

labelnomeArqLog=Label(frame_aba3,text='Log File NAME:')
labelnomeArqLog.place(relx=0.62, rely=0.85, relwidth=0.15, relheight=0.05)

nomearqLogBasic=StringVar() #NOME ARQUIVO LOG aba 3 
textNomeArqLogBasic=Entry(frame_aba3,font = '{Arial} 9',textvariable = nomearqLogBasic)
textNomeArqLogBasic.place(relx=0.750, rely=0.85, relwidth=0.2, relheight=0.05)
nomearqLogBasic.set("")

buttonLogB=Button(frame_aba3,text='Create a Log File',command=bCriarLogFile_basic,style = "TButton")
buttonLogB.place(relx=0.63, rely=0.92, relwidth=0.15, relheight=0.07)

buttonLimparB=Button(frame_aba3,text='Clear Form',command=buttonLimparClickBasic,style = "TButton")
buttonLimparB.place(relx=0.81, rely=0.92, relwidth=0.12, relheight=0.07)
#-------- fim richtextBasic aba 3 basic -------------------

########################################### ########################################### 
#Fim ########################################### ABA 3 BASIC


########################################### ########################################### 
#Ini ########################################### ABA 4 traj construction
labelTraj=Label(frame_aba4, font= "{Arial black} 9",text='Trajectory File Construction')
labelTraj.grid(column=0 ,row = 0)

labelIniPos=Label(frame_aba4,text='Initial Position (X),(Y)[mm]:')
labelIniPos.place(relx=0.01, rely=0.09, relwidth=0.21, relheight=0.05)
##labelX1arq=Label(frame_aba4,text='X:')
##labelX1arq.place(relx=0.00, rely=0.49,  relwidth=0.03, relheight=0.06)######
##labelY1arq=Label(frame_aba4,text='Y:')
##labelY1arq.place(relx=0.07, rely=0.49, relwidth=0.03, relheight=0.06)
xini=StringVar() #Linha: Coord X1 - X_final
textXini=Entry(frame_aba4,font = '{Arial} 9',textvariable = xini)
textXini.place(relx=0.225, rely=0.09, relwidth=0.07, relheight=0.05)
xini.set("0.00")

labelY1arq=Label(frame_aba4,text=',')
labelY1arq.place(relx=0.295, rely=0.09, relwidth=0.02, relheight=0.06)

yini=StringVar() #Linha: Coord Y1 Y_final
textYini=Entry(frame_aba4,font = '{Arial} 9',textvariable = yini)
textYini.place(relx=0.3033, rely=0.09, relwidth=0.07, relheight=0.05)
yini.set("0.00")

traj = IntVar()
radioLinha=Radiobutton(frame_aba4,text='Line [mm, mm]: ', command=radioLinhaClick, variable = traj, value=7)
radioLinha.place(relx=0.01, rely=0.14, relwidth=0.18, relheight=0.05)

labelXarq=Label(frame_aba4,text='X:')
labelXarq.place(relx=0.014, rely=0.19, relwidth=0.02, relheight=0.06)
labelYarq=Label(frame_aba4,text='Y:')
labelYarq.place(relx=0.12, rely=0.19, relwidth=0.03, relheight=0.06)

xf=StringVar() #Linha: coord X
textXfim=Entry(frame_aba4,font = '{Arial} 9', textvariable = xf)
textXfim.place(relx=0.035, rely=0.19, relwidth=0.07, relheight=0.05)
xf.set(" ")

yf=StringVar()#Linha: coord Y
textYfim=Entry(frame_aba4,font = '{Arial} 9',textvariable = yf)
textYfim.place(relx=0.142, rely=0.19, relwidth=0.07, relheight=0.05)
yf.set(" ")

#--------------------------------------------

radioArco=Radiobutton(frame_aba4,text='Arc [mm, degree]:', command=radioArcoClick, variable = traj, value=1)
radioArco.place(relx=0.01, rely=0.27, relwidth=0.18, relheight=0.05)

labelRarq=Label(frame_aba4,text='R:')
labelRarq.place(relx=0.014, rely=0.32,  relwidth=0.03, relheight=0.06)######
labelAarq=Label(frame_aba4,text='A:')
labelAarq.place(relx=0.12, rely=0.32, relwidth=0.03, relheight=0.06)

r=StringVar() #Arco: Raio
textRaio=Entry(frame_aba4,font = '{Arial} 9',textvariable = r)
textRaio.place(relx=0.035, rely=0.32, relwidth=0.07, relheight=0.05)
r.set(" ")

a=StringVar() #Arco: angulo
textArco=Entry(frame_aba4,font = '{Arial} 9',textvariable = a )
textArco.place(relx=0.142, rely=0.32, relwidth=0.07, relheight=0.05)
a.set(" ")

bAdd=Button(frame_aba4,text='ADD to File', command=bAdd,style = "C.TButton")
bAdd.place(relx=0.23, rely=0.235, relwidth=0.12, relheight=0.09)

bAddLoad=Button(frame_aba4,text='  Load File  ', command=bLoad_file_copia,style = "C.TButton")
bAddLoad.place(relx=0.39, rely=0.235, relwidth=0.14, relheight=0.09)


#---------------------------------------------------- ----------------------------------------
# criacao automatica de N linhas da trajetorioa
labeltc=Label(frame_aba4,text='Automatic Construction → Nº of Lines:')
labeltc.place(relx=0.01, rely=0.41, relwidth=0.31, relheight=0.05)

# criacao automatica de N linhas da trajetorioa
textNlinhas=Entry(frame_aba4,font = '{Arial} 9')
textNlinhas.place(relx=0.298, rely=0.413, relwidth=0.045, relheight=0.04)

relXY = IntVar() #Xis Y
radioXy=Radiobutton(frame_aba4,text='X-Y', command=radioXisY, variable=relXY, value = 0)
radioXy.place(relx=0.348, rely=0.395, relwidth=0.065, relheight=0.038)

#Y-xis : radioXisY e radioYxis
radioYx=Radiobutton(frame_aba4,text='Y-X', command=radioYxis, variable = relXY, value=3)
radioYx.place(relx=0.348, rely=0.429, relwidth=0.065, relheight=0.038)

#length = largura ; spacing = altura
label3=Label(frame_aba4, text='(Length[mm]),  (Spacing[µm]):') # criacao automatica de N linhas da trajetorioa
label3.place(relx=0.013, rely=0.47, relwidth=0.26, relheight=0.05)

## criacao automatica de N linhas da trajetorioa
textXlargura=Entry(frame_aba4,font = '{Arial} 8')
textXlargura.place(relx=0.244, rely=0.47, relwidth=0.07, relheight=0.05)

label4=Label(frame_aba4,text=',')# criacao automatica de N linhas da trajetorioa
label4.place(relx=0.315, rely=0.47, relwidth=0.02, relheight=0.06)

# # criacao automatica de N linhas da trajetorioa
textYaltura=Entry(frame_aba4,font = '{Arial} 8')
textYaltura.place(relx=0.322, rely=0.47, relwidth=0.07, relheight=0.05)

# # criacao automatica de N linhas da trajetorioa
bAdd1=Button(frame_aba4,text='ADD to File', command=bAdd1,style = "C.TButton")
bAdd1.place(relx=0.408, rely=0.42, relwidth=0.12, relheight=0.09)

#---------------------------------------------------- ----------------------------------------
# Ini rich resposta comandos  + scrollbar frame_aba4 - traj construction
richTextTC=Text(frame_aba4,font = '{Arial } 9',wrap=WORD)
##richTextTC.place(relx=0.018, rely=0.553, relwidth=0.45, relheight=0.43)
richTextTC.place(relx=0.013, rely=0.543, relwidth=0.52, relheight=0.365)
s=Scrollbar(richTextTC,cursor="arrow")
##s=Scrollbar(richTextTC,cursor="draft_large")
s.pack(side=RIGHT)
s.config(command=richTextTC.yview)
richTextTC.config(yscrollcommand=s.set)

richTextTC.insert(END,"#The command responses will appear in this form!\n\
\n#For automatic Trajectory Construction - Choose an integer \n Number of Lines.#\
\n#Use the 'Traj.File NAME' field to 'Create File' button'.\
\n#Use the 'List of Files' to see all files saved on Controler.\
\n#Use the 'Load File' button to select a file on Computer.\
\n#Use 'Update File' to line edition (Software Abstraction Trajectories).\n")
richTextTC.see(END)
# Fim rich resposta comandos + scrollbar frame_aba4 - traj construction

#---------------------------------------------------- ----------------------------------------
#ini rich(s) text(s) dos arquivos ------------------------ traj construction ---------------------------- -------
labelArqs=Label(frame_aba4,text='Trajectories Added:')
labelArqs.place(relx=0.71, rely=0.053, relwidth=0.20, relheight=0.05) #acima dos RICH TEXTS 


labelArq1=Label(frame_aba4,text='(Software Abstraction):')
labelArq1.place(relx=0.57, rely=0.1, relwidth=0.20, relheight=0.06) #acima dos RICH TEXTS

labelArq=Label(frame_aba4,text='(To Controller File):')
labelArq.place(relx=0.805, rely=0.1, relwidth=0.20, relheight=0.06) #acima dos RICH TEXTS

richTextArq1=Text(frame_aba4,font = '{Arial } 8') # conforme adicao no sw
richTextArq1.place(relx=0.56, rely=0.15, relwidth=0.20, relheight=0.7)
s1=Scrollbar(richTextArq1,cursor="arrow")
s1.pack(side=RIGHT)
s1.config(command=richTextArq1.yview)
richTextArq1.config(yscrollcommand=s1.set)



richTextArq=Text(frame_aba4,font = '{Arial } 8') # para a controladora
richTextArq.place(relx=0.77, rely=0.15, relwidth=0.22, relheight=0.7)
s2=Scrollbar(richTextArq,cursor="arrow")
s2.pack(side=RIGHT)
s2.config(command=richTextArq.yview)
richTextArq.config(yscrollcommand=s2.set)
#FIM rich(s) text(s) dos arquivos ----------------------traj construction ------------------------------ -------

# ---------------------------------------------------- -------
labelnomeArq=Label(frame_aba4,text='Traj.File NAME:') #nome arquivo para salvar
labelnomeArq.place(relx=0.56, rely=0.85, relwidth=0.12, relheight=0.06)

nomearqSalvar=StringVar() #NOME ARQUIVO  #frame aba4 traj construction
textNomeArq=Entry(frame_aba4,font = '{Arial} 9',textvariable = nomearqSalvar) #text arq para salvar
textNomeArq.place(relx=0.674, rely=0.856, relwidth=0.19, relheight=0.05)
nomearqSalvar.set("")

buttonCriarArq=Button(frame_aba4,text='CREATE File', command=bCriarArquivo,style = "C.TButton")
buttonCriarArq.place(relx=0.8684, rely=0.849, relwidth=0.12, relheight=0.07) #botao para salvar arq

#botoes inferiores TRAJEC construction CLEAR ,LIST e OPEN.

buttonLimparArqs=Button(frame_aba4,text='CLEAR File Forms', command=buttonLimparArqs,style = "C.TButton")
buttonLimparArqs.place(relx=0.77, rely=0.92, relwidth=0.14, relheight=0.07)

buttonListarArqs=Button(frame_aba4,text='UPDATE File', command=bAdd_atualizacao,style = "C.TButton")
buttonListarArqs.place(relx=0.63, rely=0.92, relwidth=0.12, relheight=0.07)


##buttonListarArqs=Button(frame_aba4,text='LIST Files', command=ListarArquivos,style = "C.TButton")
##buttonListarArqs.place(relx=0.73, rely=0.92, relwidth=0.12, relheight=0.07)


##buttonLimparArqs=Button(frame_aba4,text='Clear FILE Forms', command=buttonLimparArqs,style = "C.TButton")
##buttonLimparArqs.place(relx=0.655, rely=0.92, relwidth=0.14, relheight=0.07)

##buttonAbrirArq=Button(frame_aba4,text='OPEN File', command=abrirArqFTP, style = "C.TButton")
##buttonAbrirArq.place(relx=0.86, rely=0.92, relwidth=0.12, relheight=0.07)
buttonAbrirArq=Button(frame_aba4,text='OPEN File', command=abrirArqFTP, style = "C.TButton")
buttonAbrirArq.place(relx=0.41, rely=0.926, relwidth=0.12, relheight=0.07)


#fim rich(s) text(s) dos arquivos ---------------------------------------------------- -------

########################################### ########################################### 
#fim ########################################### ABA 4 traj construction


########################################### ########################################### 
# ini ########################################### ABA 5 traj EXECUTION

# ---- ini relative movements aba traj execution ----------------------------------------
labelTraj=Label(frame_aba5, font= "{Arial black} 9",text='Trajectory File Execution')
labelTraj.grid(column=0 ,row = 0)

labelArq=Label(frame_aba5,text='Relative Movements:')
labelArq.place(relx=0.01, rely=0.1, relwidth=0.21, relheight=0.05)

labelVelRelative=Label(frame_aba5,text='V(mm/s):',font = '{Arial } 8')
labelVelRelative.place(relx=0.013, rely=0.15, relwidth=0.07, relheight=0.05)

velRelative=StringVar() #Linha: Coord Y1 Y_final
textVelRelative=Entry(frame_aba5,font = '{Arial} 9',textvariable = velRelative)
textVelRelative.place(relx=0.1, rely=0.15, relwidth=0.06, relheight=0.05)
velRelative.set("20")

uni_aba5 = IntVar() #mm
radioMm=Radiobutton(frame_aba5,text='mm', command=radioMm, variable = uni_aba5, value = 1)
radioMm.place(relx=0.015, rely=0.28, relwidth=0.06, relheight=0.06)
radioMm.invoke()
#um:
radioUm=Radiobutton(frame_aba5,text='µm ', command=radioUm,variable = uni_aba5, value=2)
radioUm.place(relx=0.014, rely=0.215, relwidth=0.06, relheight=0.06)

bYpos=Button(frame_aba5,text='↑', command=Ypos,style = "TButton")
bYpos.place(relx=0.16, rely=0.1750, relwidth=0.03, relheight=0.072)

bXneg=Button(frame_aba5,text='←', command=Xneg,style = "TButton")
bXneg.place(relx=0.1, rely=0.24, relwidth=0.04, relheight=0.06)

textMovRel=StringVar() #text velocidade p/ mov relativo #aba 5 traj execution
textCoord=Entry(frame_aba5,font = '{Arial} 9',foreground="#5C4033" , textvariable=textMovRel)
textCoord.place(relx=0.14, rely=0.245, relwidth=0.07, relheight=0.05)
textMovRel.set (" ")

bXpos = Button(frame_aba5,text='→',command=Xpos,style = "TButton")
bXpos.place(relx=0.21, rely=0.24, relwidth=0.04, relheight=0.06)

bYneg=Button(frame_aba5,text='↓', command=Yneg, style = "TButton")
bYneg.place(relx=0.16, rely=0.296, relwidth=0.03, relheight=0.072)
# ---- fim relative movements aba traj execution ----------------------------------------

### ini shift guide traj execution aba 5 frame_aba5 -----------------------------------------------------
labelShift=Label(frame_aba5,text='Offset from Origin of Positioning Guide [mm]:')
labelShift.place(relx=0.01, rely=0.386, relwidth=0.299, relheight=0.05)

labelX1arq=Label(frame_aba5,text='X:')
labelX1arq.place(relx=0.014, rely=0.44,  relwidth=0.02, relheight=0.06)######
labelY1arq=Label(frame_aba5,text='Y:')
labelY1arq.place(relx=0.12, rely=0.44, relwidth=0.03, relheight=0.06)

shiftX=StringVar() #Linha: Coord X1 - X_final
textShiftX=Entry(frame_aba5,font = '{Arial} 9',textvariable = shiftX)
textShiftX.place(relx=0.035, rely=0.44, relwidth=0.07, relheight=0.05)
shiftX.set(" ")

shiftY=StringVar() #Linha: Coord Y1 Y_final
textShiftY=Entry(frame_aba5,font = '{Arial} 9',textvariable = shiftY)
textShiftY.place(relx=0.14, rely=0.44, relwidth=0.07, relheight=0.05)
shiftY.set(" ")

bOk=Button(frame_aba5,text='Go', command=bGoShift,style = "C.TButton") # -- SHIFT GUIDE !!!
bOk.place(relx=0.22, rely=0.435, relwidth=0.06, relheight=0.06)
### fim shift guide traj execution aba 5 frame_aba5 ------------------------------------------------------------

#----------- ini --------------------------
labelRichTextBox=Label(frame_aba5,text='Command responses:')
labelRichTextBox.place(relx=0.69, rely=0.0841, relwidth=0.19, relheight=0.06) 

richTextBox1=Text(frame_aba5,font = '{Arial} 9',wrap=WORD)
richTextBox1.place(relx=0.60, rely=0.13, relwidth=0.37, relheight=0.70)
##richTextBox1.focus_set()
s=Scrollbar(richTextBox1,cursor="arrow")
s.pack(side=RIGHT)
s.config(command=richTextBox1.yview)
richTextBox1.config(yscrollcommand=s.set)
richTextBox1.insert (END,"\n# You can edit this form and save it in a log file below.\n") 


##richTextBox1.insert(1.0,"\n#The command responses will appear at the top of this form!\n")
##richTextBox1.insert(1.0, "\n# FIRST: Adjust the focus and Initialize positioners!\n")

buttonVerPos=Button(frame_aba5,text='READ Positions', command=buttonVerPosicoesClick,style = "TButton")
buttonVerPos.place(relx=0.287, rely=0.23, relwidth=0.17, relheight=0.09)

labelnomeArq=Label(frame_aba5,text='Trajectory File NAME(s):')
labelnomeArq.place(relx=0.01, rely=0.55, relwidth=0.19, relheight=0.05)

nomearq=StringVar() #NOME ARQUIVO 
textNomeArq=Entry(frame_aba5,font = '{Arial} 9',textvariable = nomearq)
textNomeArq.place(relx=0.014, rely=0.61, relwidth=0.19, relheight=0.05)
nomearq.set("")

nomearq1=StringVar() #NOME ARQ
textNomeArq1=Entry(frame_aba5,font = '{Arial} 9',textvariable = nomearq1)
textNomeArq1.place(relx=0.014, rely=0.668, relwidth=0.19, relheight=0.05)
nomearq1.set("")

labelVel=Label(frame_aba5,text='V(mm/s)',font = '{Arial } 8')#
labelVel.place(relx=0.216, rely=0.55, relwidth=0.12, relheight=0.05)

vel=StringVar() #Linha: 
textVelArq=Entry(frame_aba5,font = '{Arial} 9',textvariable = vel)
textVelArq.place(relx=0.2169, rely=0.61, relwidth=0.05, relheight=0.05)
vel.set(" ")

labelRep=Label(frame_aba5,text='NºExec.',font = '{Arial } 8')#
labelRep.place(relx=0.289, rely=0.55, relwidth=0.07, relheight=0.05)

rep=StringVar() #Linha: Coord Y1 Y_final
textNrep=Entry(frame_aba5,font = '{Arial} 9',textvariable = rep)
textNrep.place(relx=0.2899, rely=0.61, relwidth=0.05, relheight=0.05)
rep.set("1")

bExec=Button(frame_aba5,text='EXECUTE File', command=bExec,style = "TButton") #execucao traj
bExec.place(relx=0.37, rely=0.6, relwidth=0.15, relheight=0.09)

labelnomeArqLog=Label(frame_aba5,text='Log File NAME:')
labelnomeArqLog.place(relx=0.62, rely=0.85, relwidth=0.15, relheight=0.05)

nomearqLog=StringVar() #NOME ARQUIVO 
textNomeArqLog=Entry(frame_aba5,font = '{Arial} 9',textvariable = nomearqLog)
textNomeArqLog.place(relx=0.750, rely=0.85, relwidth=0.2, relheight=0.05)
nomearqLog.set("")

buttonLog=Button(frame_aba5,text='Create a Log File', command=bCriarLogFile,style = "TButton")
buttonLog.place(relx=0.63, rely=0.92, relwidth=0.15, relheight=0.07)

buttonLimpar=Button(frame_aba5,text='Clear Form', command=buttonLimparClick,style = "TButton")
buttonLimpar.place(relx=0.81, rely=0.92, relwidth=0.12, relheight=0.07)

########################################### ########################################### 
# fim ########################################### ABA 5 traj EXECUTION

########################################### ########################################### 
# ini ########################################### ABA 6 IMAGE EXECUTION

labelImag=Label(frame_aba6, font= "{Arial black} 9",text='Image File Execution')
labelImag.grid(column=0 ,row = 0)

labelTamanho=Label(frame_aba6,text='Substrate Size (X),(Y)[mm]:')
labelTamanho.place(relx=0.01, rely=0.07, relwidth=0.21, relheight=0.05)

subsX=StringVar() #Substrato tamanho X
textXsubstrato=Entry(frame_aba6,font = '{Arial} 9',textvariable = subsX)
textXsubstrato.place(relx=0.215, rely=0.07, relwidth=0.07, relheight=0.05)
subsX.set("6.5") 

labelY1arq=Label(frame_aba6,text=',')
labelY1arq.place(relx=0.285, rely=0.07, relwidth=0.02, relheight=0.06)

subsY=StringVar() #Substrato tamanho Y
textYsubstrato=Entry(frame_aba6,font = '{Arial} 9',textvariable = subsY)
textYsubstrato.place(relx=0.2933, rely=0.07, relwidth=0.07, relheight=0.05)
subsY.set("7.5")

radioFP=Radiobutton(frame_aba6,text='Black Background/White Object ', command=cores_fundoPreto,  value=0)
radioFP.place(relx=0.01, rely=0.13, relwidth=0.28, relheight=0.05)
radioFP.invoke()


radioFB=Radiobutton(frame_aba6,text='White Background/Black Object', command=cores_fundoBranco, value=1)
radioFB.place(relx=0.01, rely=0.18, relwidth=0.28, relheight=0.05)


labelnomeArq=Label(frame_aba6,text='IMAGE File Name:')
labelnomeArq.place(relx=0.01, rely=0.25, relwidth=0.19, relheight=0.05)

nomearqImg=StringVar() #NOME ARQUIVO  IMAGEM
textNomeArqImg=Entry(frame_aba6,font = '{Arial} 9',textvariable = nomearqImg) 
textNomeArqImg.place(relx=0.014, rely=0.302, relwidth=0.19, relheight=0.05)
nomearqImg.set("") #


bLer=Button(frame_aba6,text='READ Image File', command=bLerArquivo,style = "TButton")
bLer.place(relx=0.24, rely=0.28, relwidth=0.14, relheight=0.12)

labelnomeArq=Label(frame_aba6,text='FILL Conditions:')
labelnomeArq.place(relx=0.01, rely=0.45, relwidth=0.19, relheight=0.05)

labelVelMov=Label(frame_aba6,text='V(mm/s): - LASER ON: ',font = '{Arial } 8')
labelVelMov.place(relx=0.013, rely=0.50, relwidth=0.16, relheight=0.05)

velMov=StringVar() 
textVelMov=Entry(frame_aba6,font = '{Arial} 9',textvariable = velMov)
textVelMov.place(relx=0.18, rely=0.50, relwidth=0.06, relheight=0.05)
velMov.set("0.90")

labelVelMov1=Label(frame_aba6,text='-SETUP:',font = '{Arial } 8')
labelVelMov1.place(relx=0.2460, rely=0.50, relwidth=0.08, relheight=0.05)

velMovSetup=StringVar() 
textVelMovSetup=Entry(frame_aba6,font = '{Arial} 9',textvariable = velMovSetup)
textVelMovSetup.place(relx=0.3099, rely=0.50, relwidth=0.06, relheight=0.05)
velMovSetup.set("35.00")

labelVelMov=Label(frame_aba6,text='Extra Disp(mm):')#Deslocamento Extra laterais
labelVelMov.place(relx=0.013, rely=0.58, relwidth=0.16, relheight=0.05)

DeslocExtra=StringVar() #Deslocamento Extra laterais
textDeslocExtra=Entry(frame_aba6,font = '{Arial} 9',textvariable = DeslocExtra)
textDeslocExtra.place(relx=0.18, rely=0.58, relwidth=0.06, relheight=0.05)
DeslocExtra.set("2")

labelPassoVertical=Label(frame_aba6,text='Lateral Step(mm):')# Passo Vertical 
labelPassoVertical.place(relx=0.013, rely=0.66, relwidth=0.16, relheight=0.05)

PassoVertical=StringVar() #Deslocamento Extra laterais
textPassoVertical=Entry(frame_aba6,font = '{Arial} 9',textvariable = PassoVertical)
textPassoVertical.place(relx=0.18, rely=0.66, relwidth=0.06, relheight=0.05)
PassoVertical.set("0.25")

bSincronizacao=Button(frame_aba6,text='      Create\n Displacement\n    Windows', command=bSincro,style = "TButton") 
bSincronizacao.place(relx=0.4, rely=0.28, relwidth=0.16, relheight=0.12)


bExecI=Button(frame_aba6,text='EXECUTE File', command=bExecImg1,style = "TButton") 
bExecI.place(relx=0.25, rely=0.58, relwidth=0.14, relheight=0.12)

##bExecI2=Button(frame_aba6,text='EXECUTE File 2', command=bExecImg_imaior,style = "TButton") #sw Não integrado: bExec - diferenciado do bExec da trajetoria
##bExecI2.place(relx=0.40, rely=0.58, relwidth=0.14, relheight=0.12)


# ---- ini shift guide aba 6 img ----------------------------------------
labelShift=Label(frame_aba6,text='Offset from Origin of Positioning Guide [mm]:')# -- SHIFT GUIDE !!! aba 6 img
labelShift.place(relx=0.01, rely=0.75, relwidth=0.299, relheight=0.05)

labelX1arq=Label(frame_aba6,text='X:')# -- SHIFT GUIDE !!! aba 6 img
labelX1arq.place(relx=0.014, rely=0.804,  relwidth=0.02, relheight=0.06)######
labelY1arq=Label(frame_aba6,text='Y:')
labelY1arq.place(relx=0.12, rely=0.804, relwidth=0.03, relheight=0.06)

shiftXimg=StringVar() # -- SHIFT GUIDE !!! aba 6 img
textShiftXimg=Entry(frame_aba6,font = '{Arial} 9',textvariable = shiftXimg)
textShiftXimg.place(relx=0.035, rely=0.804, relwidth=0.07, relheight=0.05)
shiftXimg.set("0.00")

shiftYimg=StringVar() # -- SHIFT GUIDE !!! aba 6 img
textShiftYimg=Entry(frame_aba6,font = '{Arial} 9',textvariable = shiftYimg)
textShiftYimg.place(relx=0.14, rely=0.804, relwidth=0.07, relheight=0.05)
shiftYimg.set("0.00")

bOkImg=Button(frame_aba6,text='Go', command=bGoShiftImg,style = "C.TButton") # -- SHIFT GUIDE !!! aba 6 img
bOkImg.place(relx=0.22, rely=0.799, relwidth=0.06, relheight=0.06)
# ---- fim shift guide aba 6 img ----------------------------------------



#------------------- richtext Image Execution ----------------
labelRichTextImg=Label(frame_aba6,text='Command responses: ')
labelRichTextImg.place(relx=0.69, rely=0.0841, relwidth=0.19, relheight=0.06)

richTextImg=Text(frame_aba6,font = '{Arial} 9',wrap=WORD)
richTextImg.place(relx=0.60, rely=0.13, relwidth=0.37, relheight=0.70)
s=Scrollbar(richTextImg,cursor="arrow")
s.pack(side=RIGHT)
s.config(command=richTextImg.yview)
richTextImg.config(yscrollcommand=s.set)

richTextImg.insert (END,"\n# You can edit this form and save it in a log file below.\n")
richTextImg.insert(END,"\n# Choose a monochromatic .BMP image \n# Insert Image_File_Name (Without .bmp)\n")
richTextImg.insert(END,"\n# Keep the image scale (Substrate Size) for X and Y.\n ## Sequence to perform Synchronization:\n\
 # Read Image File -> \n # Create Displacement Windows ->\n # Enable external commands in Laser interface \n # 'GEXT: 1') -> Execute File.\n")
richTextImg.see(END)
#comando GEXT: interface_laser : this command enables or disables the use of the gate control on the analog port - on the power supply
#GEXT: 1 - use the signals on the analog inputs

labelnomeArqLogI=Label(frame_aba6,text='Log File NAME:')
labelnomeArqLogI.place(relx=0.62, rely=0.85, relwidth=0.15, relheight=0.05)

nomearqLogImg=StringVar() 
textNomeArqLogImg=Entry(frame_aba6,font = '{Arial} 9',textvariable = nomearqLogImg)
textNomeArqLogImg.place(relx=0.750, rely=0.85, relwidth=0.2, relheight=0.05)
nomearqLogImg.set("")

buttonLogI=Button(frame_aba6,text='Create a Log File',command=bCriarLogFile_img,style = "TButton")
buttonLogI.place(relx=0.63, rely=0.92, relwidth=0.15, relheight=0.07)

buttonLimparB=Button(frame_aba6,text='Clear Form',command=buttonLimparClickImg,style = "TButton")
buttonLimparB.place(relx=0.81, rely=0.92, relwidth=0.12, relheight=0.07)

#- fim ------------------ richtext Image Execution ----------------

########################################### ########################################### 
# Fim ########################################### ABA 6 IMAGE EXECUTION

########################################### ########################################### 
# ini ########################################### ABA 7 IMAGE EXECUTION XYZ

labelImag=Label(frame_aba7, font= "{Arial black} 9",text='Image Processing/Execution')
labelImag.grid(column=0 ,row = 0)

labelnomeArqImgXYZ=Label(frame_aba7,text='IMAGE File Name:')
labelnomeArqImgXYZ.place(relx=0.01, rely=0.08, relwidth=0.19, relheight=0.05)

nomearqImgXYZ=StringVar() #NOME ARQUIVO  IMAGEM
textNomeArqImgXYZ=Entry(frame_aba7,font = '{Arial} 9',textvariable = nomearqImgXYZ) #?????????????????????????????????????????????????????????
textNomeArqImgXYZ.place(relx=0.014, rely=0.132, relwidth=0.19, relheight=0.05)
##nomearqImgXYZ.set("sobel-n1-skel (2)") #corrigir nomes repetidos (entre abas) - acrescentar diferença no sw Comum (sem abas).
nomearqImgXYZ.set("") 

bLer=Button(frame_aba7,text='READ Image File', command=bLerArquivo_IMGP,style = "TButton")
bLer.place(relx=0.219, rely=0.09, relwidth=0.18, relheight=0.12)

bLer=Button(frame_aba7,text=' TIPS ', command=buttonTipsImgContorno,style = "TButton")
bLer.place(relx=0.429, rely=0.09, relwidth=0.16, relheight=0.12)

sep1 = Separator(frame_aba7,orient=HORIZONTAL)
sep1.place(relx=0.01, rely=0.223, relwidth=0.56, relheight=0.01)

sep2 = Separator(frame_aba7,orient=HORIZONTAL)
sep2.place(relx=0.01, rely=0.51, relwidth=0.56, relheight=0.05)

bSeg=Button(frame_aba7,text='LABEL Image Regions', command=bSegmentarImg,style = "TButton")
bSeg.place(relx=0.04, rely=0.23, relwidth=0.20, relheight=0.12)

bSeeSubI=Button(frame_aba7,text='SubImage Preview', command=bVerSubImagem_Seg)
bSeeSubI.place(relx=0.28, rely=0.23, relwidth=0.20, relheight=0.12)
bSeeSubI.config(state='disabled')

labelRepImg=Label(frame_aba7,text='Nº:',font = '{Arial } 8')#
labelRepImg.place(relx=0.48, rely=0.265, relwidth=0.04, relheight=0.05)

subImg=StringVar() #Linha: 
textSubImg=Entry(frame_aba7,font = '{Arial} 9',textvariable = subImg)
textSubImg.place(relx=0.506, rely=0.265, relwidth=0.04, relheight=0.05)
subImg.set(" ")
textSubImg.config(state='disabled')

bSobel=Button(frame_aba7,text="     Sobel EDGE map\n'Skeletonization' Image", command=bSobelSkelImg,style = "TButton")
bSobel.place(relx=0.15, rely=0.37, relwidth=0.22, relheight=0.13)

labelTamanho=Label(frame_aba7,text='Image/Substrate Scale [%]:')
labelTamanho.place(relx=0.01, rely=0.52, relwidth=0.21, relheight=0.05)

escalaImg=StringVar() #Substrato tamanho X
textEscalaImg=Entry(frame_aba7,font = '{Arial} 9',textvariable = escalaImg)
textEscalaImg.place(relx=0.215, rely=0.52, relwidth=0.07, relheight=0.05)
##subsX.set("6.5") #nome anterior substratoX1 e Y1
escalaImg.set("100") #nome anterior substratoX1 e Y1


labelnomeArqSalvarImgXYZ=Label(frame_aba7,text='Trajectory File Name:')
labelnomeArqSalvarImgXYZ.place(relx=0.01, rely=0.572, relwidth=0.19, relheight=0.05)

nomearqSalvarImgXYZ=StringVar() #NOME ARQUIVO IMG - TRAJECTORY XY
textNomeArqSalvarImgXYZ=Entry(frame_aba7,font = '{Arial} 9',textvariable = nomearqSalvarImgXYZ) 
textNomeArqSalvarImgXYZ.place(relx=0.014, rely=0.622, relwidth=0.19, relheight=0.05)
nomearqSalvarImgXYZ.set("n1-teste") #

##labelFrom=Label(frame_aba7,text='    Number\nFrom  -   To ',font = '{Arial } 8')#
##labelFrom.place(relx=0.243, rely=0.635, relwidth=0.12, relheight=0.08)
##
##arqFrom=StringVar() #Linha: 
##textArqFrom=Entry(frame_aba7,font = '{Arial} 9',textvariable = arqFrom)
##textArqFrom.place(relx=0.235, rely=0.702, relwidth=0.05, relheight=0.05)
##arqFrom.set(" ")
##
##arqTo=StringVar() #Linha: Coord Y1 Y_final
##textArqTo=Entry(frame_aba7,font = '{Arial} 9',textvariable = arqTo)
##textArqTo.place(relx=0.2899, rely=0.702, relwidth=0.05, relheight=0.05)
##arqTo.set(" ")

bXYZtraj=Button(frame_aba7,text='XY Trajectory', command=bTestePVT,style = "TButton")
bXYZtraj.place(relx=0.3149, rely=0.55, relwidth=0.18, relheight=0.12)


labelExecImg=Label(frame_aba7,text='Execution:')
labelExecImg.place(relx=0.012, rely=0.69, relwidth=0.19, relheight=0.05)

labelShifimg=Label(frame_aba7,text='Offset from Origin of Positioning Guide [mm]:')# -- SHIFT GUIDE !!! aba origin
labelShifimg.place(relx=0.012, rely=0.73, relwidth=0.299, relheight=0.05)

labelX1arq=Label(frame_aba7,text='X:')# -- SHIFT GUIDE !!! aba origin
labelX1arq.place(relx=0.016, rely=0.783,  relwidth=0.02, relheight=0.05)######
labelY1arq=Label(frame_aba7,text='Y:')
labelY1arq.place(relx=0.11, rely=0.783, relwidth=0.03, relheight=0.05)

shiftXip=StringVar() # -- SHIFT GUIDE !!! aba origin 
textShiftXip=Entry(frame_aba7,font = '{Arial} 9',textvariable = shiftXip)
textShiftXip.place(relx=0.035, rely=0.783, relwidth=0.07, relheight=0.05)
shiftXip.set("")

shiftYip=StringVar() # -- SHIFT GUIDE !!! aba origin 
textShiftYip=Entry(frame_aba7,font = '{Arial} 9',textvariable = shiftYip)
textShiftYip.place(relx=0.13, rely=0.783, relwidth=0.07, relheight=0.05)
shiftYip.set("")

bOkImgP=Button(frame_aba7,text='Go', command=bGoShiftImgP,style = "C.TButton") # -- SHIFT GUIDE !!! aba 8 origin
bOkImgP.place(relx=0.22, rely=0.773, relwidth=0.06, relheight=0.06)



labelVelImg=Label(frame_aba7,text='V(mm/s)',font = '{Arial } 8')#
labelVelImg.place(relx=0.02, rely=0.85, relwidth=0.12, relheight=0.05)

velImg=StringVar() #Linha: 
textVelArqImg=Entry(frame_aba7,font = '{Arial} 9',textvariable = velImg)
textVelArqImg.place(relx=0.020, rely=0.89, relwidth=0.05, relheight=0.05)
velImg.set(" ")

labelRepImg=Label(frame_aba7,text='NºExec.',font = '{Arial } 8')#
labelRepImg.place(relx=0.089, rely=0.85, relwidth=0.07, relheight=0.05)

repImg=StringVar() #Linha: Coord Y1 Y_final
textNrepImg=Entry(frame_aba7,font = '{Arial} 9',textvariable = rep)
textNrepImg.place(relx=0.0919, rely=0.89, relwidth=0.05, relheight=0.05)
repImg.set("1")

bExecImgProcess=Button(frame_aba7,text='EXECUTE File', command=bExecImgProc,style = "TButton") #execucao traj
bExecImgProcess.place(relx=0.174, rely=0.868, relwidth=0.18, relheight=0.11)



#------------------- richtext Image Execution ----------------
labelRichTextImgP=Label(frame_aba7,text='Command responses: ')
labelRichTextImgP.place(relx=0.69, rely=0.0841, relwidth=0.19, relheight=0.06)

richTextImgP=Text(frame_aba7,font = '{Arial} 9',wrap=WORD)
richTextImgP.place(relx=0.60, rely=0.13, relwidth=0.37, relheight=0.70)
##richTextBox1.focus_set()
s=Scrollbar(richTextImgP,cursor="arrow")
s.pack(side=RIGHT)
s.config(command=richTextImgP.yview)
richTextImgP.config(yscrollcommand=s.set)

richTextImgP.insert (END,"\n# You can edit this form and save it in a log file below.\n")
richTextImgP.insert(END," \n# This Tab is for Images with:\n\
# 'Black Backgroung / White Object(s)' \n\
# Choose a .PNG file to perform image processing - \n# LABEL, SOBEL, SKELETONIZE \n\
\n# Choose a monochromatic .BMP image to: \n# Read Image File or \n# Create a Trajectory File (XY trajectory) button\n")
# Insert  Image_File_Name \n#(Without .png OR .bmp)\n")
richTextImgP.see(END)

labelnomeArqLogI=Label(frame_aba7,text='Log File NAME:')
labelnomeArqLogI.place(relx=0.62, rely=0.85, relwidth=0.15, relheight=0.05)

nomearqLogImgP=StringVar() #NOME ARQUIVO LOG aba 3 
textNomeArqLogImg=Entry(frame_aba7,font = '{Arial} 9',textvariable = nomearqLogImgP)
textNomeArqLogImg.place(relx=0.750, rely=0.85, relwidth=0.2, relheight=0.05)
nomearqLogImgP.set("")

buttonLogIp=Button(frame_aba7,text='Create a Log File',command=bCriarLogFile_imgP,style = "TButton")
buttonLogIp.place(relx=0.63, rely=0.92, relwidth=0.15, relheight=0.07)

buttonLimparIp=Button(frame_aba7,text='Clear Form',command=buttonLimparClickImgP,style = "TButton")
buttonLimparIp.place(relx=0.81, rely=0.92, relwidth=0.12, relheight=0.07)


# fim ########################################### ABA 7 Img proc label sobel skel

######################################### ########################################### 
# ini ########################################### ABA 8 ORIGIN

labelO=Label(frame_aba8, font= "{Arial black} 9",text='Redefine Origin')
labelO.grid(column=0 ,row = 0)


buttonNovaGuia=Button(frame_aba8,text='  DEFINE GUIDE ORIGIN \n       Current Position   ', command=buttonDefineGuiaNova,style = "TButton")
buttonNovaGuia.place(relx=0.03, rely=0.79, relwidth=0.23, relheight=0.12)

buttonResetGuia=Button(frame_aba8,text='     RESET GUIDE ORIGIN \n         Previous Position ', command=buttonResetGuiaNova,style = "TButton")
buttonResetGuia.place(relx=0.28, rely=0.79, relwidth=0.23, relheight=0.12)

labelRichTextO=Label(frame_aba8,text='Command responses:')
labelRichTextO.place(relx=0.69, rely=0.0841, relwidth=0.19, relheight=0.06) 

richTextOrigin=Text(frame_aba8,font = '{Arial} 9',wrap=WORD)
richTextOrigin.place(relx=0.60, rely=0.13, relwidth=0.37, relheight=0.70)
##richTextBox1.focus_set()
s=Scrollbar(richTextOrigin,cursor="arrow")
s.pack(side=RIGHT)
s.config(command=richTextOrigin.yview)
richTextOrigin.config(yscrollcommand=s.set)


richTextOrigin.insert (END,"-------------------------------------------------------------")
richTextOrigin.insert (END,"\n# To see information - Use the button 'TIPS'\n\
\n# All changes made here will be saved in a\n# ~ Log File ~ !\n")
richTextOrigin.insert (END,"-------------------------------------------------------------")
richTextOrigin.see(END)

buttonTipsOrigin=Button(frame_aba8,text='   TIPS  ', command=buttonTipsOrigin,style = "TButton") # aba Origin
buttonTipsOrigin.place(relx=0.185, rely=0.15, relwidth=0.18, relheight=0.12)


buttonLimparB=Button(frame_aba8,text='Clear Form',command=buttonLimparClickOrigin,style = "TButton")
buttonLimparB.place(relx=0.73, rely=0.86, relwidth=0.12, relheight=0.07)

buttonVerPosH=Button(frame_aba8,text='READ Positions', command=buttonVerPosicoesOrigin,style = "TButton") # aba Origin
buttonVerPosH.place(relx=0.35, rely=0.42, relwidth=0.18, relheight=0.125)

buttonVerLogOorigin=Button(frame_aba8,text='VIEW LOG FILE', command=buttonVerLogFile,style = "TButton") # aba Origin
buttonVerLogOorigin.place(relx=0.185, rely=0.6, relwidth=0.18, relheight=0.12)

# ---- ini shift guide aba 8 origin ----------------------------------------
labelShift=Label(frame_aba8,text='Offset from Origin of Positioning Guide [mm]:')# -- SHIFT GUIDE !!! aba origin
labelShift.place(relx=0.01, rely=0.386, relwidth=0.299, relheight=0.05)

labelX1arq=Label(frame_aba8,text='X:')# -- SHIFT GUIDE !!! aba origin
labelX1arq.place(relx=0.014, rely=0.44,  relwidth=0.02, relheight=0.06)######
labelY1arq=Label(frame_aba8,text='Y:')
labelY1arq.place(relx=0.12, rely=0.44, relwidth=0.03, relheight=0.06)

shiftXorigin=StringVar() # -- SHIFT GUIDE !!! aba origin 
textShiftXorigin=Entry(frame_aba8,font = '{Arial} 9',textvariable = shiftXorigin)
textShiftXorigin.place(relx=0.035, rely=0.44, relwidth=0.07, relheight=0.05)
shiftXorigin.set("")

shiftYorigin=StringVar() # -- SHIFT GUIDE !!! aba origin 
textShiftYorigin=Entry(frame_aba8,font = '{Arial} 9',textvariable = shiftYorigin)
textShiftYorigin.place(relx=0.14, rely=0.44, relwidth=0.07, relheight=0.05)
shiftYorigin.set("")

bOkOrigin=Button(frame_aba8,text='Go', command=bGoShiftOrigin,style = "C.TButton") # -- SHIFT GUIDE !!! aba 8 origin
bOkOrigin.place(relx=0.22, rely=0.435, relwidth=0.06, relheight=0.06)

##btry=Button(frame_aba8,text='Go1', command=buttonDefineGuiaNova1,style = "C.TButton") # -- SHIFT GUIDE !!! aba 8 origin
####bCriaArquivoOrigin(x,y)
##btry.place(relx=0.29, rely=0.435, relwidth=0.06, relheight=0.06)

lista_arquivos = ListarArquivos_Combo()

labelShift=Label(frame_aba4,text='List of FILES:')# -- SHIFT GUIDE !!! aba origin
labelShift.place(relx=0.01, rely=0.93, relwidth=0.10, relheight=0.05)

arq_combo = StringVar()
##box = Combobox(frame_aba8,textvariable=arq_combo, state='readonly')
box = Combobox(frame_aba4,textvariable=arq_combo)
box['values'] = lista_arquivos
box.current(0)
box.place(relx=0.1026, rely=0.93, relwidth=0.31, relheight=0.06)
##richTextTC.place(relx=0.013, rely=0.543, relwidth=0.52, relheight=0.365)
##arq_combo.trace('r', tracer)
box.bind('<<ComboboxSelected>>',handler1)

image2 = Image.open("Octocat.png") #Logotipo CTI
photo2 = ImageTk.PhotoImage(image2)

label_logo2 = Label(frame_aba9,image=photo2)
label_logo2.image = photo2 
label_logo2.place(relx=0.00, rely=0.10, relwidth=0.35, relheight=0.30)



labelabout = Label(frame_aba9,text="Software desenvolvido durante projeto de mestrado na FEEC Unicamp\n\n\
 'Software de Controle para Sistema de Processamento de Materiais e Dispositivos por Laser Ultravioleta'\n\n\
 Aluna Patrícia Domingues.\n\n\
 Software disponível (GNU General Public License/Licença Pública Geral - GPL 2.0):\n\n\
  https://github.com/patricia-sdomin   ")
labelabout.place(relx=0.01, rely=0.10, relwidth=0.35, relheight=0.19)
labelabout.pack(padx=130, pady=130)


# ---- fim shift guide aba origin ----------------------------------------
#***########################################################################################***#
#***########################################################################################***#
abas.add(frame_aba1,text="Presentation")
abas.add(frame_aba2,text="Initialization")
abas.add(frame_aba3,text="Basic Movements")
abas.add(frame_aba4,text="Trajectory Construction")
abas.add(frame_aba5,text="Trajectory Execution")
abas.add(frame_aba6,text="Image Execution") #image raster
abas.add(frame_aba7,text="Image Processing")
abas.add(frame_aba8,text="Set Origin")
abas.add(frame_aba9,text="About")
##abas.add(frame_aba10,text="  Help  ")
abas.select(frame_aba1)
abas.pack(padx=10, pady=10)
verificar_posicoes_Guia()
form1.mainloop()
