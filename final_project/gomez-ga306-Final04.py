import maya.cmds as cmds
try:
    if cmds.window(igWin , exists = True):
        cmds.deleteUI(igWin)
except NameError:
    print "ERROR"
    
    
    
igWin = cmds.window( t="BallRig_V01", s = False)
cmds.columnLayout( adjustableColumn=True )
cmds.separator(h=10)
cmds.text(l = "BALL RIG " , fn = "boldLabelFont")
cmds.separator(h=10)
cmds.text(l = "Click inside blue to create rig " , fn = "boldLabelFont")
cmds.separator(h=10)
ballRig = cmds.button(l = "Ball Rig", h = 120, c= "BallRig()", bgc = [0.468,0.824,0.824])
cmds.separator(h=10)
cmds.text(l = "Isrrael Gomez - ga306 Final " , fn = "boldLabelFont")
cmds.separator(h=10)
cmds.showWindow( igWin )




def BallRig():    

    selectedBall = cmds.ls(sl = True)
    bb= cmds.xform(selectedBall, q= True, ws = True,bb = True)
    
    height = bb[4] - bb[1]
    radius = height/2
    
    cmds.xform(selectedBall, a=True,t=(0,height/2,0),cp = True)
    
    strechSquash = cmds.nonLinear (selectedBall[0],typ="squash",lowBound =0,highBound =2,n = "strechSquash")
    cmds.xform(strechSquash, a=True,t=(0,0,0),cp = True)
    
    squashFactor = strechSquash[0]
    
    
    mainCOG = cmds.circle(r=(radius+0.5),n= selectedBall[0]+"_COG", nr = [0,1,0],ch=0)
    
    ballRotator = cmds.circle(r=radius/3,n= selectedBall[0]+"_Rotator", nr = [0,0,1],ch=0)
    cmds.xform(ballRotator, t = ((radius+radius/3),radius,0), a = True)
    cmds.move(-(radius+radius/3), 0 ,0, ballRotator[0]+".scalePivot",ballRotator[0]+".rotatePivot", r = True)
    
    
    squashRotator = cmds.circle(r=radius/5,n= selectedBall[0]+"_sqaushRotator", nr = [0,0,1],ch=0)
    cmds.xform(squashRotator, t = (0,(height+radius/5+0.2),0), a = True)
    cmds.move(0, -(radius+radius/5+0.2) ,0, squashRotator[0]+".scalePivot",squashRotator[0]+".rotatePivot", r = True)
    
    squashCtrl = cmds.circle(r=radius/4,n= selectedBall[0]+"squashCtrl", nr = [0,0,1],ch=0)
    cmds.xform(squashCtrl, t = (0,(height+(radius-0.5)),0), a = True)
    
    cmds.select(mainCOG,ballRotator,squashRotator,squashCtrl)
    cmds.makeIdentity (a =True,t=1,r=1,s=1)
    
    
    cmds.parent(selectedBall[0],ballRotator)
    cmds.parent(strechSquash,squashRotator)
    cmds.parent(squashCtrl,squashRotator)
    
    cmds.parent(ballRotator,squashRotator,mainCOG)
    
    cmds.setDrivenKeyframe(strechSquash[0] + ".factor", cd = squashCtrl[0]+".translateY", dv=0, v=0 )
    cmds.setDrivenKeyframe(strechSquash[0]+ ".factor", cd = squashCtrl[0]+".translateY", dv=7, v=1 )
    cmds.setDrivenKeyframe(strechSquash[0]+ ".factor", cd = squashCtrl[0]+".translateY", dv=-5, v=-0.5 )
    
    cmds.select(cl = True)
    
    cmds.setAttr(strechSquash[1]+".visibility",0)
    
    cmds.setAttr(ballRotator[0]+".tx",lock = 1,k = False)
    cmds.setAttr(ballRotator[0]+".ty",lock = 1,k = False)
    cmds.setAttr(ballRotator[0]+".tz",lock = 1,k = False)
    cmds.setAttr(ballRotator[0]+".sx",lock = 1,k = False)
    cmds.setAttr(ballRotator[0]+".sy",lock = 1,k = False)
    cmds.setAttr(ballRotator[0]+".sz",lock = 1,k = False)
    
    cmds.setAttr(squashRotator[0]+".tx",lock = 1,k = False)
    cmds.setAttr(squashRotator[0]+".ty",lock = 1,k = False)
    cmds.setAttr(squashRotator[0]+".tz",lock = 1,k = False)
    cmds.setAttr(squashRotator[0]+".sx",lock = 1,k = False)
    cmds.setAttr(squashRotator[0]+".sy",lock = 1,k = False)
    cmds.setAttr(squashRotator[0]+".sz",lock = 1,k = False)
    
    cmds.setAttr(squashCtrl[0]+".tx",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".tz",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".sx",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".sy",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".sz",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".rx",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".ry",lock = 1,k = False)
    cmds.setAttr(squashCtrl[0]+".rz",lock = 1,k = False)
    
