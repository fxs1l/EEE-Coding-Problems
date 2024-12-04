

class Vector3D:
    def __init__(self, x, y, z):
        self.vector = (x, y, z)
      	# TODO: Create a routine that saves the vector
        #       <x, y, z> into this Vector3D object.
      
    def __add__(self, other):
        # TODO: Create a routine that adds this vector with Vector3D other
        #       and returns the result as a Vector3D object
        x = self.vector[0] + other.vector[0]
        y = self.vector[1] + other.vector[1]
        z = self.vector[2] + other.vector[2]
        return Vector3D(x, y, z)

    def __neg__(self):
        # TODO: Create a routine that returns the negative (opposite) of
        #       this vector as a Vector3D object
        x = self.vector[0] * -1
        y = self.vector[1] * -1
        z = self.vector[2] * -1
        return Vector3D(x, y, z)

    def __sub__(self, other):
        # TODO: Create a routine that subtracts this vector with Vector3D other
        #       and returns the result as a Vector3D object
        x = self.vector[0] - other.vector[0]
        y = self.vector[1] - other.vector[1]
        z = self.vector[2] - other.vector[2]
        return Vector3D(x, y, z)

    def __mul__(self, other):
        # TODO: Create a routine that multiplies this vector with other
        #       depending on its data type, and returns the result as a
        #       Vector3D object. other can either be an integer
        #       scalar or a Vector3D object.
        
        if type(other) is int:
            x = self.vector[0] * other
            y = self.vector[1] * other
            z = self.vector[2] * other
            return Vector3D(x, y, z)
        elif type(other) is Vector3D:
            x = self.vector[0] * other.vector[0]
            y = self.vector[1] * other.vector[1]
            z = self.vector[2] * other.vector[2]
            return Vector3D(x, y, z)

def main():
    testcases = int(input())

    for t in range(testcases):
        line_in = input().split()
        op = line_in[0].strip()
        vec_vals = [int(x) for x in line_in[1:]]
        
        if op == 'add':
            a = Vector3D(vec_vals[0],vec_vals[1],vec_vals[2])
            b = Vector3D(vec_vals[3],vec_vals[4],vec_vals[5])
            c = a + b
            print(c.vector[0], c.vector[1], c.vector[2])
        elif op == 'sub':
            a = Vector3D(vec_vals[0],vec_vals[1],vec_vals[2])
            b = Vector3D(vec_vals[3],vec_vals[4],vec_vals[5])
            c = a - b
            print(c.vector[0], c.vector[1], c.vector[2])
        elif op == 'mul_s':
            a = Vector3D(vec_vals[0],vec_vals[1],vec_vals[2])
            b = vec_vals[3]
            c = a * b
            print(c.vector[0], c.vector[1], c.vector[2])
        elif op == 'mul':
            a = Vector3D(vec_vals[0],vec_vals[1],vec_vals[2])
            b = Vector3D(vec_vals[3],vec_vals[4],vec_vals[5])
            c = a * b
            print(c.vector[0], c.vector[1], c.vector[2])
        elif op == 'neg':
            a = Vector3D(vec_vals[0],vec_vals[1],vec_vals[2])
            c = -a
            print(c.vector[0], c.vector[1], c.vector[2])
            

        # TODO: a Write routine that processes a line in the input
        # op       - string
        #          - operation to do with the provided vectors
        #          - can only be one from the set: {add, sub, neg, mul_s, mul}
        # vec_vals - list of integers
        #          - numbers that follow the op in the input line
		#          - can only have a length of 3, 4, or 6

if __name__ == '__main__':
    main()
