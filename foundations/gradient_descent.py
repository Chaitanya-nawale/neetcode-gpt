class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            fd_x = 2 * init
            init = init - learning_rate * fd_x
        return round(init, 5)



    