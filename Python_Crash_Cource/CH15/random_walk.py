from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all points in the walk."""
        while len(self.x_values) < self.num_points:
            #Decide which direction to go and how far to go in that direction.
            x_step = self._get_steps()
            y_step = self._get_steps()

            #Redect moves that go nowhere:
            if not x_step and not y_step:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_steps(self):
        """Helper method to get the steps"""
        direction = choice([1, -1])
        distance = choice([x for x in range (10)])
        return direction * distance


