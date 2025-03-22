from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import glob
import webcolors
import pandas as pd

def closest_color(rgb):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb[0]) ** 2
        gd = (g_c - rgb[1]) ** 2
        bd = (b_c - rgb[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_dominant_color(image, k=5):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize((100, 100))
    data = np.array(image)
    data = data.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    unique, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant = kmeans.cluster_centers_[unique[np.argmax(counts)]]
    dominant = tuple(map(int, dominant))
    return dominant

def name_color(rgb):
    try:
        cname = webcolors.rgb_to_name(rgb)
    except ValueError:
        cname = closest_color(rgb)
    return cname

# Directory with images
image_files = glob.glob("/Users/mishudhar/PycharmProjects/pythonProject20/downloaded_images/*.jpg")

# Dictionary to store color frequencies
color_counts = {}

for file in image_files:
    img = Image.open(file)
    dominant_rgb = get_dominant_color(img)
    color_name = name_color(dominant_rgb)

    if color_name in color_counts:
        color_counts[color_name] += 1
    else:
        color_counts[color_name] = 1

    print(f"Processed {file}: Dominant color - {color_name}")

# Convert the dictionary to a DataFrame for easy CSV output
color_data = pd.DataFrame(list(color_counts.items()), columns=['Color Name', 'Frequency'])

# Save the DataFrame to a CSV file
# Save the DataFrame to a CSV file in the specified directory
color_data.to_csv("/Users/mishudhar/PycharmProjects/pythonProject20/color_frequencies.csv", index=False)

print("Color frequencies saved to CSV file at '/Users/mishudhar/PycharmProjects/pythonProject20/color_frequencies.csv'.")

