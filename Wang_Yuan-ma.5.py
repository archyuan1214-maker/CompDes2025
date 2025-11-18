
'''task111'''
# import Rhino.Geometry as rg 


# def curve_to_line(Curve,N):
#     Curve.Domain = rg.Interval(0,1)
#     dist = 1/N
#     lines = []
#     for i in range(0,N):
#         position = i*dist
#         point1 = Curve.PointAt(position)
#         position2 = (i+1)*dist
#         point2 = Curve.PointAt(position2)
#         line = rg.Line(point1,point2)
#         lines.append(line)
#     return lines

# lines = curve_to_line(iCurve,iN)
# print(lines)



'''task333'''
import Rhino.Geometry as rg 

def Growing_LiningLight(iCurve,iN,oPoint,P_radius,wirethickness):
    iplanes=[]
    ipoints=[]
    wirelines=[]
    wires=[]
    lights=[]
    iCurve.Domain = rg.Interval(0,1)
    dist=1.0/iN
    xaxis=rg.Vector3d(-1,0,0)
    yaxis=rg.Vector3d(0,1,0)
    for i in range(0,iN+1):
        position=i*dist
        pointnew=iCurve.PointAt(position)
        ipoints.append(pointnew)
        plane=rg.Plane(pointnew,xaxis,yaxis)
        iplanes.append(plane)
        line=rg.Line(pointnew,oPoint)
        Length=line.Length
        wirelines.append(line)
        x_value=pointnew.X
        y_value=pointnew.Y
        z_value=Length
        Lightpoint=rg.Point3d(x_value,y_value,-z_value)
        light_sphere=rg.Sphere(Lightpoint,P_radius*Length)
        lights.append(light_sphere)
        wire_cylinder=rg.Cylinder(rg.Circle(plane,wirethickness),Length)
        wires.append(wire_cylinder)

    return ipoints,wirelines,wires,lights

a,b,c,d = Growing_LiningLight(iCurve,iN,oPoint,P_radius,wirethickness)








    
    
   
        