
import Rhino.Geometry as rg

def draw_square(center, size):
    half = size / 2.0

    pts = [
        rg.Point3d(center.X - half, center.Y - half, center.Z),
        rg.Point3d(center.X + half, center.Y - half, center.Z),
        rg.Point3d(center.X + half, center.Y + half, center.Z),
        rg.Point3d(center.X - half, center.Y + half, center.Z),
        rg.Point3d(center.X - half, center.Y - half, center.Z)
    ]

    return rg.Polyline(pts)

def recursive_square(center, size, scale, curves):
    if size < 1:
        return

    curves.append(draw_square(center, size))
    recursive_square(center, size * scale, scale, curves)


curves = []
recursive_square(center, size, scale, curves)

a = curves
