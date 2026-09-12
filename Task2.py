

import numpy as np

def create_synthetic_image():
    
    height, width, channels = 300, 400, 3
    img = np.zeros((height, width, channels), dtype=np.uint8)

    half_h = height // 2
    half_w = width // 2

    
    
    img[0:half_h, 0:half_w] = [255, 0, 0]

    
    img[0:half_h, half_w:width] = [0, 255, 0]

   
    img[half_h:height, 0:half_w] = [0, 0, 255]

    
    img[half_h:height, half_w:width] = [255, 255, 255]

   
    print("--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {img.shape}")
    print(f"Data Type             : {img.dtype}")
    print(f"Total Elements        : {img.size:,} values")
    print(
        f"Memory Footprint      : {img.nbytes:,} bytes ({img.nbytes / 1024:.2f} KB)"
    )


if __name__ == "__main__":
    create_synthetic_image()
