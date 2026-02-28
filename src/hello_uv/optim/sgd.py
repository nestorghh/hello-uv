class SGD:
    def __init__(self, lr: float = 0.01):
        self.lr = lr

    def step(self):
        print(f"SGD step with lr={self.lr}")
