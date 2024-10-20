from PIL import Image, ImageDraw
import numpy as np

def weierstrass_function(x, a=0.5, b=5, n_terms=300):
    if not (0 < a < 1):
        raise ValueError("Parameter 'a' must be between 0 and 1.")
    if b % 2 == 0:
        raise ValueError("Parameter 'b' must be an odd integer.")
    sum_terms = np.zeros_like(x, dtype=np.float64)
    for n in range(n_terms):
        sum_terms += a**n * np.cos(b**n * np.pi * x)
    return sum_terms

def main():
    width = 8000
    height = 2000
    
    image = Image.new('RGB', (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    x = np.linspace(-2, 2, width)
    y = weierstrass_function(x)
    min_y, max_y = min(y), max(y)
    y_scaled = ((y - min_y) / (max_y - min_y)) * (height - 1)
    points = [(i, height - 1 - int(y_scaled[i])) for i in range(width)]
    draw.line(points, fill=(255, 255, 255), width=1)
    image.save('image.png')

if __name__ == '__main__':
    main()
