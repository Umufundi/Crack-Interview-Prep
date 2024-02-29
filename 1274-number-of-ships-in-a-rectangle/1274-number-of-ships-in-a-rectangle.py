# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def countInQuadrant(topRight, bottomLeft):
            # Check if current rectangle is valid or contains any ships
            if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y) or not sea.hasShips(topRight, bottomLeft):
                return 0

            # If the rectangle is a single point, check if a ship is located
            if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
                return 1

            # Calculate midpoints for dividing the search area
            mid_x = (topRight.x + bottomLeft.x) // 2
            mid_y = (topRight.y + bottomLeft.y) // 2

            # Recursively count ships in each of the four quadrants
            return countInQuadrant(Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + \
                   countInQuadrant(topRight, Point(mid_x + 1, mid_y + 1)) + \
                   countInQuadrant(Point(mid_x, mid_y), bottomLeft) + \
                   countInQuadrant(Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))

        return countInQuadrant(topRight, bottomLeft)
        