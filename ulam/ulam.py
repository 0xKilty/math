from PIL import Image, ImageDraw
import sympy
import math

def polar_to_cartesian(r, theta, scalar):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    x = int((x / scalar) + (dim / 2))
    y = int((y / scalar) + (dim / 2))
    return x, y

if __name__ == "__main__":
    # User defined
    dim = 10000
    scalar = 75
    dot_radius = 3

    # Not user defined
    limit = dim // 2
    image = Image.new('RGB', (dim, dim), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    for prime in list(sympy.primerange(1, limit * scalar)):
        x, y = polar_to_cartesian(prime, prime, scalar)
        center = (x, y)
        left_up_point = (center[0] - dot_radius, center[1] - dot_radius)
        right_down_point = (center[0] + dot_radius, center[1] + dot_radius)
        draw.ellipse([left_up_point, right_down_point], fill=(255, 255, 255))
    image.save('image.png')
    print(f"Generated an Ulam spiral with primes up to {limit * scalar}")

