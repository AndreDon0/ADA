import sys
import numpy as np

def parse_input(data):
    groups = data.split('\n\n')
    if len(groups) > 1:
        parsed = []
        for group in groups:
            parsed_group = parse_input(group)
            parsed.append(parsed_group)
        return parsed
    else:
        lines = data.split('\n')
        if not lines:
            return []
        return [[list(map(int, line.split()))] for line in lines]

def main():
    data = sys.stdin.read().strip()
    parsed = parse_input(data)
    tensor = np.array(parsed)
    dim = tensor.ndim
    
    if dim == 4:
        tensor = tensor.transpose(2, 3, 1, 0)
    elif dim == 3:
        tensor = tensor.transpose(1, 2, 0)
    elif dim == 2:
        tensor = tensor.transpose(1, 0)
    
    output = []
    if dim == 4:
        for h in range(tensor.shape[0]):
            for w in range(tensor.shape[1]):
                group = []
                for c in range(tensor.shape[2]):
                    row = ' '.join(map(str, tensor[h, w, c, :]))
                    group.append(row)
                output.append('\n'.join(group))
    elif dim == 3:
        for h in range(tensor.shape[0]):
            for w in range(tensor.shape[1]):
                line = ' '.join(map(str, tensor[h, w, :]))
                output.append(line)
    elif dim == 2:
        for w in range(tensor.shape[0]):
            line = ' '.join(map(str, tensor[w, :]))
            output.append(line)
    
    print('\n\n'.join(output))

if __name__ == "__main__":
    main()