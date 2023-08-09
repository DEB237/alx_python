'''
This module contains a class
'''

from base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base and represents a rectangle shape.

    Attributes:
        id (int): The ID of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate position of the rectangle.
        y (int): The y-coordinate position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate position of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate position of the rectangle. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.

        Notes:
            Calls the super class with id to utilize the logic of the init in the Base class.
            Assigns each argument (width, height, x, y) to the corresponding attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width of the rectangle.

        Raises:
            ValueError: If the width value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height of the rectangle.

        Raises:
            ValueError: If the height value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute.

        Args:
            value (int): The x-coordinate position of the rectangle.

        Raises:
            ValueError: If the x-coordinate value is not negative.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value >= 0:
            self.__x = value
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute.

        Args:
            value (int): The y-coordinate position of the rectangle.

        Raises:
            ValueError: If the y-coordinate value is not negative.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value >= 0:
            self.__y = value
        else:
            raise ValueError("y must be >= 0")
        
    def area(self):
         """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
         return self.__width * self.__height
    
    def display(self):
        """
        Displays the rectangle instance using '#' character,
        taking care of x and y coordinates.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle based on both no-keyword and keyword arguments.

        Args:
            *args: No-keyword arguments in the following order:
                - id (int): The ID of the rectangle.
                - width (int): The width of the rectangle.
                - height (int): The height of the rectangle.
                - x (int): The x-coordinate position of the rectangle.
                - y (int): The y-coordinate position of the rectangle.
            
            **kwargs: Keyword arguments where each key represents an attribute and its value represents the new value assigned to that attribute.
        """

        # Update attributes based on no-keyword arguments (*args)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
           
        # Update attributes based on keyword arguments (**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
