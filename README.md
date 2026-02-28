## Usage

```python
import hello_uv as hu

x = hu.nn.relu(-2)
layer = hu.nn.Linear(10, 3)
opt = hu.optim.SGD(lr=0.1)


This prevents everyone from importing deep internals like `hello_uv.nn.layers.Linear` and breaking when you refactor.


