import maya.cmds
sphere = maya.cmds.polySphere()[0]
cube = maya.cmds.polyCube()[0]

maya.cmds.connectAttr(cube+'.ry', sphere+'.ty')
maya.cmds.select(cube)

def create_dimensions(cube_width, cube_length):
    cube_lenght = 0.5 * sphere_radius
    cube_width = 0.5 * sphere_radius
    cube_height= 0.5 * sphere_radius
    
    
    return body[0];