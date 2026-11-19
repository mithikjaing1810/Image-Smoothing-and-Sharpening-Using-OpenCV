# ==============================================================================
# Developed By: Mithik jain G
# Register No: 212224240087
# Experiment 5: Image Smoothing and Sharpening Using OpenCV
# ==============================================================================

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    image_name = 'jet.jpg' if os.path.exists('jet.jpg') else 'image.jpg'
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)

    image1 = cv2.imread(image_name)
    if image1 is None:
        print(f"[ERROR] Could not load image from '{image_name}'.")
        return

    image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

    # 1. Averaging Filter
    kernel = np.ones((11, 11), np.float32) / 169
    image3 = cv2.filter2D(image2, -1, kernel)
    plt.figure(figsize=(9, 9))
    plt.subplot(1, 2, 1)
    plt.imshow(image2)
    plt.title("Original Image")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(image3)
    plt.title("Average Filter Image")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "output1_average_filter.png"))
    plt.close()
    print("[SUCCESS] Average filter output saved.")

    # 2. Weighted Averaging Filter
    kernel1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    image3_weighted = cv2.filter2D(image2, -1, kernel1)
    plt.figure()
    plt.imshow(image3_weighted)
    plt.title("Weighted Average Filter Image")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "output2_weighted_average_filter.png"))
    plt.close()
    print("[SUCCESS] Weighted average filter output saved.")

    # 3. Gaussian Filter
    gaussian_blur = cv2.GaussianBlur(image2, (33, 33), 0, 0)
    plt.figure()
    plt.imshow(gaussian_blur)
    plt.title("Gaussian Blur")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "output3_gaussian_blur.png"))
    plt.close()
    print("[SUCCESS] Gaussian blur output saved.")

    # 4. Median Filter
    median = cv2.medianBlur(image2, 13)
    plt.figure(figsize=(9, 9))
    plt.imshow(median)
    plt.title("Median Blur")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "output4_median_blur.png"))
    plt.close()
    print("[SUCCESS] Median blur output saved.")

    # 5. Laplacian Linear Kernel
    kernel2 = np.array([[-1, -1, -1], [2, -2, 1], [2, 1, -1]])
    image3_lap = cv2.filter2D(image2, -1, kernel2)
    plt.figure()
    plt.imshow(image3_lap)
    plt.title("Laplacian Kernel")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "output5_laplacian_kernel.png"))
    plt.close()
    print("[SUCCESS] Laplacian kernel output saved.")

    # 6. Laplacian Operator
    laplacian = cv2.Laplacian(image2, cv2.CV_64F)
    plt.figure()
    plt.imshow(laplacian)
    plt.title("Laplacian Operator")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "output6_laplacian_operator.png"))
    plt.close()
    print("[SUCCESS] Laplacian operator output saved.")

if __name__ == "__main__":
    main()
