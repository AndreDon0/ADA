def relu(x):
    return x if x > 0 else 0


def neuron(function, inputs, weights, bias):
    if len(weights) != len(inputs):
        return "No solution"
    else:
        total = sum(x * w for x, w in zip(inputs, weights)) + bias
        return function(total)


n = int(input())
W = list(map(float, input().split()))
b = float(input())
X = list(map(float, input().split()))

print(neuron(relu, X, W, b))
