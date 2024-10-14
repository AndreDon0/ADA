def relu(x):
    return x if x > 0 else 0


def neuron(function, inputs, weights, bias):
    if len(weights) != len(inputs):
        return "No solution"
    else:
        total = sum(x * w for x, w in zip(inputs, weights)) + bias
        return function(total)


n = int(input())
W = list(map(int, input().split()))
b = int(input())
X = list(map(int, input().split()))

print(neuron(relu, X, W, b))
