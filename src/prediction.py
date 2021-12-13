import numpy

from matplotlib import pyplot 
from sklearn.linear_model import LinearRegression

class Predicted:
    def __init__(self, input_dict: dict, key):
        """Predicts data from a dict using a linear regression"""

        model = LinearRegression()
        model_x = [[x] for x in input_dict.keys()]
        model_y =  [[y] for y in input_dict.values()]
        model.fit(model_x, model_y)

        ready_model = model
        result = ready_model.predict(numpy.array([key]).reshape(1,-1))

        self.result = result[0][0]
        self.full_result = model.predict(model_x)
        self.x_values = list(input_dict.keys()),
        self.y_values = list(input_dict.values())

    def show(self):
        """Plots the prediction. A result dict is needed."""

        pyplot.scatter(self.x_values, self.y_values)
        pyplot.plot(self.x_values)
        pyplot.show()