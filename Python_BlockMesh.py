#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:40:02 2019

@author: karsten
"""
import numpy as np
import math
from blockmeshdicthelper_NEU3 import BlockMeshDict, Vertex, SimpleGrading

zwei_D = 1

#Zylinder Maße und Position
x_cyl = 120
y_cyl = 0
r_cyl = 2.5

#Testsektion - Maße
x_in = 0
x_out = 240
y_top = 50
y_bott = -50
z_front = 0
z_back = 25

x_buff = 480
#Weitere Konstanten für das Netz
r_o = 25 #4*r_cyl


###################Punkte
#---------------------------Zylinder
dx_cyl = (math.cos(45)*r_cyl)
dy_cyl = (math.sin(45)*r_cyl)


x0 = x_cyl - r_cyl
y0 = 0
p0 = [x0,y0,z_front]

x1 = x_cyl - dx_cyl
y1 = y_cyl + dy_cyl
p1 = [x1,y1,z_front]

x2 = x_cyl
y2 = y_cyl +r_cyl
p2 = [x2,y2,z_front]

x3 = x_cyl + dx_cyl
y3 = y1
p3 = [x3,y3,z_front]

x4 = x_cyl + r_cyl
y4 = y_cyl
p4 = [x4,y4,z_front]

#---- gespiegelte Punkte
p5 = [x3,-y3,z_front]
p6 = [x2, -y2, z_front]
p7 = [x1, -y1, z_front]

#-----------------------Kreis um den Zylinder
dx_o = (math.cos(45)*r_o)
dy_o = (math.sin(45)*r_o)

x8 = x_cyl - r_o
y8 = 0
p8 = [x8,y8,z_front]

x9 = x_cyl - dx_o
y9 = y_cyl + dy_o
p9 = [x9,y9,z_front]

x10 = x_cyl
y10 = y_cyl +r_o
p10 = [x10,y10,z_front]

x11 = x_cyl + dx_o
y11 = y9
p11 = [x11,y11,z_front]

x12 = x_cyl + r_o
y12 = y_cyl
p12 = [x12,y12,z_front]

#---- gespiegelte Punkte
p13 = [x11,-y11,z_front]
p14 = [x10, -y10, z_front]
p15 = [x9, -y9, z_front]

#----------------------- Außen

p16 = [x_in,y_cyl, z_front]
p17 = [x_in, y9, z_front]
p18 = [x_in, y_top, z_front]
p19 = [x9, y_top, z_front]
p20 = [x_cyl, y_top, z_front]
p21 = [x11, y_top, z_front]
p22 = [x_out, y_top, z_front]
p23 = [x_out, y11, z_front]
p24 = [x_out, y_cyl,z_front]

#---- gespiegelte Punkte
p25 = [x_out, -y11, z_front]
p26 = [x_out, y_bott, z_front]
p27 = [x11,y_bott,z_front]
p28 = [x_cyl, y_bott,z_front]
p29 = [x9, y_bott, z_front]
p30 = [x_in, y_bott, z_front]
p31 = [x_in, -y9, z_front]

# Buffer
p32 = [x_buff, y_top, z_front]
p33 = [x_buff, y11, z_front]
p34 = [x_buff, y_cyl, z_front]
p35 = [x_buff, -y11, z_front]
p36 = [x_buff, y_bott, z_front]

#Grid 
nGrid = 4

ny1 = nGrid*int(y9)
ny2 = nGrid*int(y_top - y9)

nx1 = nGrid*int(x9)
nx2 = nGrid*int(x10 - x9)
nx3 = nGrid*int(x11 - x10)
nx4 = nGrid*int(x_out - x11)

n_cyl = nGrid*4*int(r_o-r_cyl)

nx_buff = nGrid*int(0.25*(x_buff - x_out))

if zwei_D == 1:
    nz = 1
    z_back = 0.1
else:
    nz= 25


##===================================== Zylinder_Air_5_Uin_Ma0512_wall =========================================
# Eckpunkte
#==============================================================================

vertices = []

def add_vertex(pkt,name,vertices):
    vertices.append(Vertex(pkt[0],pkt[1],pkt[2],name))

#Punkte
add_vertex(p0,'p0',vertices)
add_vertex(p1,'p1',vertices)
add_vertex(p2,'p2',vertices)
add_vertex(p3,'p3',vertices)
add_vertex(p4,'p4',vertices)
add_vertex(p5,'p5',vertices)
add_vertex(p6,'p6',vertices)
add_vertex(p7,'p7',vertices)
add_vertex(p8,'p8',vertices)
add_vertex(p9,'p9',vertices)
add_vertex(p10,'p10',vertices)
add_vertex(p11,'p11',vertices)
add_vertex(p12,'p12',vertices)
add_vertex(p13,'p13',vertices)
add_vertex(p14,'p14',vertices)
add_vertex(p15,'p15',vertices)
add_vertex(p16,'p16',vertices)
add_vertex(p17,'p17',vertices)
add_vertex(p18,'p18',vertices)
add_vertex(p19,'p19',vertices)
add_vertex(p20,'p20',vertices)
add_vertex(p21,'p21',vertices)
add_vertex(p22,'p22',vertices)
add_vertex(p23,'p23',vertices)
add_vertex(p24,'p24',vertices)
add_vertex(p25,'p25',vertices)
add_vertex(p26,'p26',vertices)
add_vertex(p27,'p27',vertices)
add_vertex(p28,'p28',vertices)
add_vertex(p29,'p29',vertices)
add_vertex(p30,'p30',vertices)
add_vertex(p31,'p31',vertices)
add_vertex(p32,'p32',vertices)
add_vertex(p33,'p33',vertices)
add_vertex(p34,'p34',vertices)
add_vertex(p35,'p35',vertices)
add_vertex(p36,'p36',vertices)
#==============================================================================
# BlockMesh
#==============================================================================
blockmesh = 1

if blockmesh == 1:
    # utility to to generate vertex names
    def vnamegen(x0y0, x1y0, x1y1, x0y1):
        return (x0y0, x1y0, x1y1, x0y1,
                x0y0+'+z', x1y0+'+z', x1y1+'+z', x0y1+'+z')
    
    #Spline zur BlockMeshDict hinzufuegen
    def add_spline(start, end, points, vertices):        
        bmd.add_spline(str(vertices[start]),str(vertices[end]),points)  
    
        z = []
        z_neu =[]
        for a_neu in points:
            z_neu = a_neu[:]
            z_neu[2] = z_neu[2]+z_back
            z.append(z_neu)
    
        bmd.add_spline(str(vertices[start+'+z']),str(vertices[end+'+z']),z)  
 
    #polyLine zur BlockMeshDict hinzufuegen
    def add_polyLine(start, end, points, vertices):        
        bmd.add_polyLine(str(vertices[start]),str(vertices[end]),points)  
    
        z = []
        z_neu =[]
        for a_neu in points:
            z_neu = a_neu[:]
            z_neu[2] = z_neu[2]+z_back
            z.append(z_neu)
    
        bmd.add_polyLine(str(vertices[start+'+z']),str(vertices[end+'+z']),z)  
    
    #arc zur BlockMeshDict hinzufuegen    
    def add_arc(start, end, point, vertices):
        bmd.add_arc(str(vertices[start]),str(vertices[end]),point)
       # z = []
        z_neu =[]
        z_neu = point[:]
        z_neu[2] = z_neu[2]+z_back
        #z.append(z_neu)
        bmd.add_arc(str(vertices[start+'+z']),str(vertices[end+'+z']),z_neu)
    
    # prepare ofblockmeshdicthelper.BlockMeshDict instance to
    # gather vertices, blocks, faces and boundaries.
    bmd = BlockMeshDict()
    
    # set metrics
    bmd.set_metric('mm')
    
    # ----------------- vertices ----------------------
    for v in vertices:
        bmd.add_vertex(v.x, v.y, v.z, v.name)
        bmd.add_vertex(v.x, v.y, v.z+z_back, v.name+'+z')
        
    # ----------------- Blocks ----------------------
    #Zylinder
    b1 = bmd.add_hexblock(vnamegen('p0','p1','p9','p8'),(ny1,n_cyl,nz),'b1', grading = SimpleGrading(1,10,1))    
    b2 = bmd.add_hexblock(vnamegen('p1','p2','p10','p9'),(nx2,n_cyl,nz),'b2', grading = SimpleGrading(1,10,1))    
    b3 = bmd.add_hexblock(vnamegen('p2','p3','p11','p10'),(nx3,n_cyl,nz),'b3', grading = SimpleGrading(1,10,1))    
    b4 = bmd.add_hexblock(vnamegen('p3','p4','p12','p11'),(ny1,n_cyl,nz),'b4', grading = SimpleGrading(1,10,1)) 
    
    b5 = bmd.add_hexblock(vnamegen('p4','p5','p13','p12'),(ny1,n_cyl,nz),'b5', grading = SimpleGrading(1,10,1))     
    b6 = bmd.add_hexblock(vnamegen('p5','p6','p14','p13'),(nx3,n_cyl,nz),'b6', grading = SimpleGrading(1,10,1))    
    b7 = bmd.add_hexblock(vnamegen('p6','p7','p15','p14'),(nx2,n_cyl,nz),'b7', grading = SimpleGrading(1,10,1))       
    b8 = bmd.add_hexblock(vnamegen('p7','p0','p8','p15'),(ny1,n_cyl,nz),'b8', grading = SimpleGrading(1,10,1))       
    
    #Umgebung
    b9 = bmd.add_hexblock(vnamegen('p16','p8','p9','p17'),(nx1,ny1,nz),'b9', grading = SimpleGrading(1,1,1))       
    b10 = bmd.add_hexblock(vnamegen('p17','p9','p19','p18'),(nx1,ny2,nz),'b10', grading = SimpleGrading(1,1,1))   
    b11 = bmd.add_hexblock(vnamegen('p9','p10','p20','p19'),(nx2,ny2,nz),'b11', grading = SimpleGrading(1,1,1))     
    b12 = bmd.add_hexblock(vnamegen('p10','p11','p21','p20'),(nx3,ny2,nz),'b12', grading = SimpleGrading(1,1,1))        
    b13 = bmd.add_hexblock(vnamegen('p11','p23','p22','p21'),(nx4,ny2,nz),'b13', grading = SimpleGrading(1,1,1)) 
    b14 = bmd.add_hexblock(vnamegen('p12','p24','p23','p11'),(nx4,ny1,nz),'b14', grading = SimpleGrading(1,1,1)) 
    
    b15 = bmd.add_hexblock(vnamegen('p13','p25','p24','p12'),(nx1,ny1,nz),'b15', grading = SimpleGrading(1,1,1)) 
    b16 = bmd.add_hexblock(vnamegen('p27','p26','p25','p13'),(nx1,ny2,nz),'b16', grading = SimpleGrading(1,1,1))     
    b17 = bmd.add_hexblock(vnamegen('p28','p27','p13','p14'),(nx2,ny2,nz),'b17', grading = SimpleGrading(1,1,1))     
    b18 = bmd.add_hexblock(vnamegen('p29','p28','p14','p15'),(nx3,ny2,nz),'b18', grading = SimpleGrading(1,1,1))     
    b19 = bmd.add_hexblock(vnamegen('p30','p29','p15','p31'),(nx4,ny2,nz),'b19', grading = SimpleGrading(1,1,1))     
    b20 = bmd.add_hexblock(vnamegen('p31','p15','p8','p16'),(nx4,ny1,nz),'b20', grading = SimpleGrading(1,1,1))     

    b21 = bmd.add_hexblock(vnamegen('p23','p33','p32','p22'),(nx_buff,ny2,nz),'b21', grading = SimpleGrading(5,1,1)) 
    b22 = bmd.add_hexblock(vnamegen('p24','p34','p33','p23'),(nx_buff,ny1,nz),'b22', grading = SimpleGrading(5,1,1)) 
    
    b23 = bmd.add_hexblock(vnamegen('p25','p35','p34','p24'),(nx_buff,ny1,nz),'b23', grading = SimpleGrading(5,1,1)) 
    b24 = bmd.add_hexblock(vnamegen('p26','p36','p35','p25'),(nx_buff,ny2,nz),'b24', grading = SimpleGrading(5,1,1))     

        
    #boundary
    bmd.add_boundary('patch','inlet',[b9.face('w'),b10.face('w'),b19.face('w'),b20.face('w')])
    bmd.add_boundary('wall','cyl_top',[b1.face('s'),b2.face('s'),b3.face('s'),b4.face('s')])
    bmd.add_boundary('wall','cyl_down',[b5.face('s'),b6.face('s'),b7.face('s'),b8.face('s')])    
    bmd.add_boundary('wall','wall_top',[b10.face('n'),b11.face('n'),b12.face('n'),b13.face('n'),b21.face('n')])
    bmd.add_boundary('wall','wall_down',[b16.face('s'),b17.face('s'),b18.face('s'),b19.face('s'),b24.face('s')])     
    bmd.add_boundary('patch','outlet',[b21.face('e'),b22.face('e'),b23.face('e'),b24.face('e')])

    #bmd.add_boundary('cyclic','wall_top',[b10.face('n'),b11.face('n'),b12.face('n'),b13.face('n')],'wall_down')
    #bmd.add_boundary('cyclic','wall_down',[b16.face('s'),b17.face('s'),b18.face('s'),b19.face('s')],'wall_top')
    
    
#   bmd.add_boundary('cyclic','front',[b1.face('b'),b2.face('b'),b3.face('b'),b4.face('b'),b5.face('b')],'back')
#   bmd.add_boundary('cyclic','back',[b1.face('t'),b2.face('t'),b3.face('t'),b4.face('t'),b5.face('t')],'front')
#    bmd.add_boundary('cyclic','wall_front',[b1.face('b'),b2.face('b'),b3.face('b'),b4.face('b'),
#                                          b5.face('b'),b6.face('b'),b7.face('b'),b8.face('b'),
#                                          b9.face('b'),b10.face('b'),b11.face('b'),b12.face('b'),b13.face('b'),b14.face('b'),
#                                          b15.face('b'),b16.face('b'),b17.face('b'),b18.face('b'),b19.face('b'),b20.face('b')],'wall_back')
#    bmd.add_boundary('cyclic','wall_back',[b1.face('t'),b2.face('t'),b3.face('t'),b4.face('t'),
#                                          b5.face('t'),b6.face('t'),b7.face('t'),b8.face('t'),
#                                          b9.face('t'),b10.face('t'),b11.face('t'),b12.face('t'),b13.face('t'),b14.face('t'),
#                                          b15.face('t'),b16.face('t'),b17.face('t'),b18.face('t'),b19.face('t'),b20.face('t')],'wall_front')

#    bmd.add_boundary('wall','wall_front',[b1.face('b'),b2.face('b'),b3.face('b'),b4.face('b'),
#                                          b5.face('b'),b6.face('b'),b7.face('b'),b8.face('b'),
#                                          b9.face('b'),b10.face('b'),b11.face('b'),b12.face('b'),b13.face('b'),b14.face('b'),
#                                          b15.face('b'),b16.face('b'),b17.face('b'),b18.face('b'),b19.face('b'),b20.face('b')])
    if zwei_D == 1:
        bmd.add_boundary('empty','wall_back',[b1.face('t'),b2.face('t'),b3.face('t'),b4.face('t'),
                                              b5.face('t'),b6.face('t'),b7.face('t'),b8.face('t'),
                                              b9.face('t'),b10.face('t'),b11.face('t'),b12.face('t'),b13.face('t'),b14.face('t'),
                                              b15.face('t'),b16.face('t'),b17.face('t'),b18.face('t'),b19.face('t'),b20.face('t'),
                                              b21.face('t'),b22.face('t'),b23.face('t'),b24.face('t')])
     
        bmd.add_boundary('empty','wall_front',[b1.face('b'),b2.face('b'),b3.face('b'),b4.face('b'),
                                              b5.face('b'),b6.face('b'),b7.face('b'),b8.face('b'),
                                              b9.face('b'),b10.face('b'),b11.face('b'),b12.face('b'),b13.face('b'),b14.face('b'),
                                              b15.face('b'),b16.face('b'),b17.face('b'),b18.face('b'),b19.face('b'),b20.face('b'),
                                              b21.face('b'),b22.face('b'),b23.face('b'),b24.face('b')])        
    else:
        bmd.add_boundary('symmetryPlane','wall_back',[b1.face('t'),b2.face('t'),b3.face('t'),b4.face('t'),
                                              b5.face('t'),b6.face('t'),b7.face('t'),b8.face('t'),
                                              b9.face('t'),b10.face('t'),b11.face('t'),b12.face('t'),b13.face('t'),b14.face('t'),
                                              b15.face('t'),b16.face('t'),b17.face('t'),b18.face('t'),b19.face('t'),b20.face('t'),
                                              b21.face('t'),b22.face('t'),b23.face('t'),b24.face('t')])
     
        bmd.add_boundary('wall','wall_front',[b1.face('b'),b2.face('b'),b3.face('b'),b4.face('b'),
                                              b5.face('b'),b6.face('b'),b7.face('b'),b8.face('b'),
                                              b9.face('b'),b10.face('b'),b11.face('b'),b12.face('b'),b13.face('b'),b14.face('b'),
                                              b15.face('b'),b16.face('b'),b17.face('b'),b18.face('b'),b19.face('b'),b20.face('b'),
                                              b21.face('b'),b22.face('b'),b23.face('b'),b24.face('b')])
#    bmd.add_boundary('wall','wall_back',[b1.face('t'),b2.face('t'),b3.face('t'),b4.face('t'),
#                                          b5.face('t'),b6.face('t'),b7.face('t'),b8.face('t'),
#                                          b9.face('t'),b10.face('t'),b11.face('t'),b12.face('t'),b13.face('t'),b14.face('t'),
#                                          b15.face('t'),b16.face('t'),b17.face('t'),b18.face('t'),b19.face('t'),b20.face('t')])
 

    
    # prepare for output
    bmd.assign_vertexid()
    dict_vertices = {}
    
    for v in bmd.vertices.values():
        dict_vertices[v.name] =  v.index  

    # ----------------- Splines ----------------------
    #Schaufel
   # add_spline('p_l','p_s',s_l,dict_vertices) 
   # add_spline('p_s','p_p',s_s2,dict_vertices) 
   # add_spline('p_p','p_l',s_p1,dict_vertices) 
    
    add_arc('p0','p1',p2,dict_vertices)
    add_arc('p1','p2',p3,dict_vertices)
    add_arc('p2','p3',p4,dict_vertices)    
    add_arc('p3','p4',p5,dict_vertices)
    add_arc('p4','p5',p6,dict_vertices)    
    add_arc('p5','p6',p7,dict_vertices)  
    add_arc('p6','p7',p0,dict_vertices)      
    add_arc('p7','p0',p1,dict_vertices)      

    add_arc('p8','p9',p10,dict_vertices)
    add_arc('p9','p10',p11,dict_vertices)
    add_arc('p10','p11',p12,dict_vertices)    
    add_arc('p11','p12',p13,dict_vertices)
    add_arc('p12','p13',p14,dict_vertices)    
    add_arc('p13','p14',p15,dict_vertices)  
    add_arc('p14','p15',p8,dict_vertices)      
    add_arc('p15','p8',p9,dict_vertices)      
    
    
    #Ausgabe in Datei
    fobj_out = open("blockMeshDict","w")
    fobj_out.write(bmd.format())
    fobj_out.close()    
    