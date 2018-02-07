import maya.cmds
sphere = maya.cmds.polySphere()[0]
cube = maya.cmds.polyCube()[0]

maya.cmds.connectAttr(cube+'.ry', sphere+'.ty')
maya.cmds.select(cube)

def create_dimensions(cube_width, cube_length)
    sphere_radius = 0.5 * cube_width
    sphere_radius = 0.5 * cube_length
    sphere_radius = 0.5 * cube_height
    
    
    return body[0];