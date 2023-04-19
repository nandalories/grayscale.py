def grayscale(r, g, b):
    avg = (r + g + b) // 3
    return (avg, avg, avg)

print(grayscale(255, 0, 0)) # output: (85, 85, 85)
print(grayscale(0, 255, 0)) # output: (85, 85, 85)
print(grayscale(0, 0, 255)) # output: (85, 85, 85)
