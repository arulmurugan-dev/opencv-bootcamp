import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("apples-on-a-tree-branch.jpg")

# Convert BGR to RGB (for correct display)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Generate pyramid levels
level0 = img
level1 = cv2.pyrDown(level0)
level2 = cv2.pyrDown(level1)
level3 = cv2.pyrDown(level2)

# Store images
images = [level0, level1, level2, level3]
titles = ["Level 0 (Original)", "Level 1", "Level 2", "Level 3"]

# Display pyramid levels
plt.figure(figsize=(10,6))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")

plt.show()

# Print image sizes
for i, im in enumerate(images):
    print(f"Level {i} size: {im.shape}")