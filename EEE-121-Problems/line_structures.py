class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """ Returns a string showing the coordinates with the format (x,y) """
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        """ Checks if two points pertain to the same coordinates """
        if (self.x, self.y) == other:
            return True
        return False

    def get_distance(self, other):
        """ Calculates the distance between two points """
        return ((self.x - other.x)**2 + (self.y - other.y)**2)  ** (1/2)  
    
class Line:
    def __init__(self, point_a, point_b):
        self.points = [point_a, point_b]

    def __str__(self):
        """ Returns a string containing all collinear points in the Line instance """
        p_str = ''
        for i in range(len(self.points)):
            if i != len(self.points) - 1:
                p_str += self.points[i].__str__() + ", "
            else:
                p_str += self.points[i].__str__()
        return f'[{p_str}]'
                
    def get_slope_intercept(self):
        """ Calculates the slope of the line """
        return (self.points[0].y - self.points[1].y) / (self.points[0].x - self.points[1].x) 
        
    def add_points(self, points):
        """ Adds a list of collinear points to the Line instance """
        for p in points:
            # check if the point is collinear
            if p not in self.points:
                if self.points[0].y - p.y == self.get_slope_intercept() * (self.points[0].x - p.x):
                    self.points.append(p)
                
    def remove_points(self, points):
        """ Removes a list of points from the Line instance """
        for p in points:
            if p in self.points[2:]:
                self.points.remove(p)

if __name__ == "__main__":
    list_points = []
    n = int(input())
    for x in range(n):
        input_line = input().split(',')
        list_points.append(Point(int(input_line[0]), int(input_line[1])))

    # Instantiate a Line using the first two input points
    myLine = Line(list_points[0], list_points[1])

    # If your methods are defined correctly, the following lines should produce the desired output in the test cases.
    print("Instatiating a Line: ")
    print(myLine)
    myLine.add_points(list_points[2:-1])
    print("Adding More Points: ")
    print(myLine)    
    myLine.add_points(list_points)
    print("Adding Redundant Points: ")
    print(myLine)    
    print("Trying to Remove Last Input Point:")
    myLine.remove_points([list_points[-1]])
    print(myLine)
    print("Trying to Remove All Points:")
    myLine.remove_points(list_points)
    print(myLine)
