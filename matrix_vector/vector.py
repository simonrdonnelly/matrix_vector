class DifferentDimensionVectors(BaseException):
    pass

max_repr_elements = 12

class Vector:
    """
    Class implementing vectors.
    """

    def __init__(self, *args):
        """
        Initialize a Vector object.

        Example:
        >> Vector(1, 2, 3)
        => <matrix_vector.vector.Vector object>

        Arguments:
        N numbers
        """
        self.coordinates = list(args)

    @property
    def size(self):
        """
        Returns the size of the vector(number of coordinates).
        Example:

        >> Vector(1, 2, 3).size
        => 3

        Arguments:
        No arguments
        """
        return len(self.coordinates)

    def __len__(self):
        return self.size

    def __add__(self, other):
        """
        Adds two vectors or adds a number to the elements of vector.
        Returns a new object.

        Example:
        >> Vector(1, 2, 3) + Vector(4, 5, 6)
        => Vector(5, 7, 9)

        Example:
        >> Vector(1, 2, 3) + 3
        => Vector(4, 5, 6)

        Arguments:
        vector : (Vector)
        or
        number : (Numeric)
        """
        if type(other) is Vector:
            if other.size == self.size:
                return Vector(*[x + y for x, y in
                                zip(self.coordinates, other.coordinates)])
            else:
                raise DifferentDimensionVectors
        else:
            return Vector(*[x + other for x in self.coordinates])

    def __sub__(self, other):
        """
        Substracts two vectors or substracts a number from
        the elements of the vector. Returns a new object.

        Example:
        >> Vector(1, 2, 3) - Vector(4, 5, 6)
        => Vector(-3, -3, -3)

        Example:
        >> Vector(1, 2, 3) - 3
        => Vector(-2, -1, 0)

        Arguments:
        vector : (Vector)
        or
        number : (Numeric)
        """
        if type(other) is Vector:
            if other.size == self.size:
                return Vector(*[x - y for x, y in
                                zip(self.coordinates, other.coordinates)])
            else:
                raise DifferentDimensionVectors
        else:
            return Vector(*[_ - other for _ in self.coordinates])

    def __iadd__(self, other):
        """
        Adds two vectors or adds a number to the
        elements of the vector. Changes the object.

        Example:
        >> Vector(1, 2, 3) += Vector(4, 5, 6)
        => Vector(5, 7, 9)

        Example:
        >> Vector(1, 2, 3) += 3
        => Vector(4, 5, 6)

        Arguments:
        vector : (Vector)
        or
        number : (Numeric)
        """
        self = self + other
        return self

    def __isub__(self, other):
        """
        Substracts two vectors or substracts a number from the
        elements of the vector. Changes the object.

        Example:
        >> Vector(1, 2, 3) -= Vector(4, 5, 6)
        => Vector(-3, -3, -3)

        Example:
        >> Vector(1, 2, 3) -= 3
        => Vector(-2, -1, 0)

        Arguments:
        vector : (Vector)
        or
        number : (Numeric)
        """
        self = self - other
        return self

    def __getitem__(self, key):
        """
        Access elements of the vector with [] operator

        Example:
        >> Vector(1, 2, 3)[2]
        => 3

        Arguments:
        number : (int)
        """
        return self.coordinates[key]

    def __mul__(self, other):
        """
        Depending on the argument either multiplies a number with
        the vector or finds the scalar product of two vectors.
        Example:
        >> Vector(1, 2, 3) * 2
        => Vector(2, 4, 6)

        Example(scalar product):
        >> Vector(1, 2, 3) * Vector(2, 2, 2)
        => 12

        Arguments:
        number : (Numeric)
        or
        vector : (Vector)
        """
        if type(other) is Vector:
            if other.size == self.size:
                return sum(x * y for x, y in
                           zip(self.coordinates, other.coordinates))
            else:
                raise DifferentDimensionVectors(
                    "Can't find scalar of vectors with different dimensions")
        else:
            return Vector(*[_ * other for _ in self.coordinates])

    def __imul__(self, other):
        """
        Multiplies a number with the elements
        of the vector changing the object.

        Example:
        >> Vector(1, 2, 3) * 2
        => Vector(2, 4, 6)

        Arguments:
        number : (Numeric)
        """
        if type(self * other) is Vector:
            self = self * other
            return self
        else:
            raise TypeError(
                "Can't assign number to Vector class object")

    def __xor__(self, other):
        """
        Returns the cross product of two 3-dimension vectors.
        Returns new object.

        Example:
        >> Vector(1, 2, 3) ^ Vector(4, 5, 6)
        => Vector(-3, 6, -3)

        Arguments:
        vector : (Vector)
        """
        if self.size == other.size == 3:
            coordinate_x = self[1] * other[2] - self[2] * other[1]
            coordinate_y = self[2] * other[0] - self[0] * other[2]
            coordinate_z = self[0] * other[1] - self[1] * other[0]
            return Vector(coordinate_x, coordinate_y, coordinate_z)
        else:
            raise TypeError(
                "Vector product only defined for 3 dimensional vectors")

    def __ixor__(self, other):
        """"
        Returns the scalar product of two 3-dimension vectors.
        Changes the object.

        Example:
        >> Vector(1, 2, 3) ^ Vector(4, 5, 6)
        => Vector(-3, 6, -3)

        Arguments:
        vector : (Vector)
        """
        self = self ^ other
        return self

    def __truediv__(self, other):
        """
        Divides the elements of the vector by a number.
        Returns new object.

        Example:
        >> Vector(3, 9, 6) / 3
        => Vector(1, 3, 2)

        Arguments:
        number : (Numeric)
        """
        try:
            return Vector(*[_ / other for _ in self.coordinates])
        except ZeroDivisionError:
            raise

    def __itruediv__(self, other):
        """
        Divides the elements of the vector by a number.
        Changes the object.

        Example:
        >> Vector(3, 9, 8) / 3
        => Vector(1, 3, 2)

        Arguments:
        number : (Numeric)
        """
        self = self / other
        return self

    def __floordiv__(self, other):
        """
        Finds the floor when dividing the elements of the vector
        by a number. Returns new object.

        Example:
        >> Vector(3, 9, 8) // 3
        => Vector(1, 3, 2)

        Arguments:
        number : (Numeric)
        """
        try:
            return Vector(*[_ // other for _ in self.coordinates])
        except ZeroDivisionError:
            raise

    def __ifloordiv__(self, other):
        """
        Finds the floor when dividing the elements of the vector
        by a number. Changes the object.

        Example:
        >> Vector(3, 9, 6) // 3
        => Vector(1, 3, 2)

        Arguments:
        number : (Numeric)
        """
        self = self // other
        return self

    @property
    def length(self):

        """
        Returns the length of the vector.

        Example:
        >> Vector(1, 2, 3).length
        => 3.7417

        Arguments:
        No arguments
        """
        return sum(_ ** 2 for _ in self.coordinates) ** 0.5

    def normalized(self):
        """
        Returns the normalized vector of the vector.

        Example:
        >> Vector(1, 2, 3).normalized()
        => Vector(0.2673, 0.5345, 0.8018)

        Arguments:
        No arguments
        """
        return self / self.length

    def normalize(self):
        """
        Normalizes the vector. Changes the object.

        Example:
        >> Vector(1, 2, 3).normalize()
        => Vector(0.2673, 0.5345, 0.8018)

        Arguments:
        No arguments
        """
        self.coordinates = self.normalized().coordinates
        return self

    def round(self, number):
        """
        Rounds the coordinates of the vector. Changes the object.

        Example:
        >> Vector(1.345, 2.438, 3.535).round(2)
        => Vector(1.34, 2.44, 3.53)

        Arguments:
        number : (int)
        """
        self.coordinates = [round(x, number) for x in self.coordinates]
        return self

    def __eq__(self, vector):
        return self.coordinates == vector.coordinates

    def __repr__(self):
        if self.size <= max_repr_elements:
            return 'Vector({0})'.format(', '.join(map(str, self.coordinates)))
        else:
            return 'Vector({0})'.format(', '.join(
                    map(str, self[:3] + ['...'] + self[-3:])))
