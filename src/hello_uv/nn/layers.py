class Linear:
    def __init__(self, in_features: int, out_features: int):
        self.in_features = in_features
        self.out_features = out_features

    def __repr__(self):
        return f"Linear({self.in_features}, {self.out_features})"
