import os

import matplotlib.pyplot as plt
import numpy as np
import scipy
import tifffile

# --- reading input.txt file ---
input_txt = open("input.txt", "r")
input_txt_lines = input_txt.readlines()
images_directory = input_txt_lines[0][:-1]
camera_sensor_size = (
    float(input_txt_lines[1]) * 1000.0
)  # converting from mm to micrometer
input_txt.close()


def gauss(x, A, x0, sigma_x, C):
    """
    1D Gaussian function
    Parameters:
    A: Amplitude
    x0: Center
    sigma_x: Width
    C: Offset
    -----------
    Returns:  intensity I at position x
    -----------
    """
    intensity = A * np.exp(-((x - x0) ** 2) / (2 * sigma_x**2)) + C
    return intensity


# processing the first image to get pixel size and beam size and gaussian example plots:
img1 = tifffile.imread(
    f"{images_directory}\\{os.listdir(images_directory)[0]}"
)  # converting img to array
pixel_size = (
    camera_sensor_size / img1.shape[1]
)  # calculating pixel size in loop(micrometer)

# setting up the data
Ix_data = np.sum(img1, axis=0)

# sum of each column of pixels in image as array, x
x = list(range(len(Ix_data)))

Iy_data = np.sum(img1, axis=1)  # sum of each row of pixels in image as array, y
y = list(range(len(Iy_data)))

# --- fitting the data to 1-d gaussian ---
# x-axis:
optimized_parameters_x, pcov_x = scipy.optimize.curve_fit(
    gauss,
    x,
    Ix_data,
    p0=[max(Ix_data), img1.shape[1] / 2, img1.shape[1] / 5, min(Ix_data)],
    bounds=(
        (0, 0, 1, 0),
        (max(Ix_data) * 2, img1.shape[1], img1.shape[1] / 2, max(Ix_data)),
    ),
)

# y-axis:
optimized_parameters_y, pcov_y = scipy.optimize.curve_fit(
    gauss,
    y,
    Iy_data,
    p0=[max(Iy_data), img1.shape[0] / 2, img1.shape[0] / 5, min(Iy_data)],
    bounds=(
        (0, 0, 1, 0),
        (np.max(Iy_data) * 2, img1.shape[0], img1.shape[0] / 2, np.max(Iy_data)),
    ),
)

# --- plotting the the first image gaussian fits ---

# plotting x-axis fit:
plt.tight_layout()
plt.plot(x, Ix_data, ".", label="Column-summed Intensity Data")
plt.plot(
    np.linspace(x[0], x[-1], 100),
    gauss(np.linspace(x[0], x[-1], 100), *optimized_parameters_x),
    label="Gaussian fit",
)
plt.title("Column-summed Intensity and Gaussian Fit (X axis)")
plt.ylabel("Intensity [a.u.]")
plt.xlabel("Position in x-axis [pixels]")
plt.savefig("first img Column-summed Intensity and Gaussian Fit (X axis)")
plt.show()

# plotting residuals x-axis:
plt.tight_layout()
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.plot(x, gauss(x, *optimized_parameters_x) - Ix_data, ".")
plt.title("Gaussian Residuals — X axis")
plt.ylabel("Residuals [a.u.]")
plt.xlabel("Position in x-axis [pixels]")
plt.savefig("first imgGaussian Fit Residuals — X axis")
plt.show()

# plotting y-axis fit:
plt.tight_layout()
plt.plot(y, Iy_data, ".", label="Row-summed Intensity Raw data")
plt.plot(
    np.linspace(y[0], y[-1], 100),
    gauss(np.linspace(y[0], y[-1], 100), *optimized_parameters_y),
    label="Gaussian fit",
)
plt.title("Row-summed Intensity and Gaussian Fit (Y axis)")
plt.ylabel("Intensity [a.u.]")
plt.xlabel("Position in y-axis [pixels]")
plt.savefig("first img Row-summed Intensity and Gaussian Fit (Y axis)")
plt.show()

# plotting residuals y-axis:
plt.tight_layout()
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.plot(y, gauss(y, *optimized_parameters_y) - Iy_data, ".")
plt.title("Gaussian Fit Residuals — Y axis")
plt.ylabel("Residuals [a.u.]")
plt.xlabel("Position in y-axis [pixels]")
plt.savefig("first imgGaussian Fit Residuals — Y axis")
plt.show()

# --- end of first image processing ---

# calculating beam size(in micrometers)
beam_size_x = pixel_size * 2.0 * optimized_parameters_x[2]
beam_size_y = pixel_size * 2.0 * optimized_parameters_y[2]

# lists to save beam positions for each image (units in pixels)
beams_position_x = []
beams_position_y = []

# main loop - execution for each image in directory
for image_name in os.listdir(images_directory):
    """processing each image in the directory
    Parameters:
    image_name: name of the image file 
    -----------
    Returns: beam position in x and y axis for each image (in pixels)"""

    img = tifffile.imread(f"{images_directory}\\{image_name}")
    # setting up the data
    Ix_data = np.sum(img, axis=0)
    x = list(range(len(Ix_data)))

    Iy_data = np.sum(img, axis=1)  # sum of each row of pixels in image as array, y
    y = list(range(len(Iy_data)))
    # fitting the data to 2 1-d gaussian:

    # x-axis:
    optimized_parameters_x_loop, pcov_x_loop = scipy.optimize.curve_fit(
        gauss,
        x,
        Ix_data,
        p0=[np.max(Ix_data), img.shape[1] / 2, img.shape[1] / 5, np.min(Ix_data)],
        bounds=(
            (0, 0, 1, 0),
            (np.max(Ix_data) * 2, img.shape[1], img.shape[1] / 2, np.max(Ix_data)),
        ),
    )
    # y-axis:
    optimized_parameters_y_loop, pcov_y_loop = scipy.optimize.curve_fit(
        gauss,
        y,
        Iy_data,
        p0=[max(Iy_data), img.shape[0] / 2, img.shape[0] / 5, min(Iy_data)],
        bounds=(
            (0, 0, 1, 0),
            (max(Iy_data) * 2, img.shape[0], img.shape[0] / 2, max(Iy_data)),
        ),
    )

    # saving beam positions
    beams_position_x = np.append(beams_position_x, optimized_parameters_x_loop[1])
    beams_position_y = np.append(beams_position_y, optimized_parameters_y_loop[1])
    # END OF MAIN LOOP

# average beam positions (in pixels)
average_beam_position_x = np.average(beams_position_x)
average_beam_position_y = np.average(beams_position_y)


#  calculating pointing stability using RMS:
def get_RMS(data, avg):
    """RMS calculation function"""
    return np.sqrt(np.mean((data - avg) ** 2.0))


# pointing stability calculations (in micrometers)
pointing_stability_x_axis = pixel_size * get_RMS(
    beams_position_x, average_beam_position_x
)
pointing_stability_y_axis = pixel_size * get_RMS(
    beams_position_y, average_beam_position_y
)
radial_position_squared = (beams_position_x - average_beam_position_x) ** 2.0 + (
    beams_position_y - average_beam_position_y
) ** 2.0
pointing_stability_radial_axis = pixel_size * np.sqrt(np.mean(radial_position_squared))

# ---writing results to Beam_Size_results.txt file---

output_file = open("Beam_Size_results.txt", "w")
lines = [
    f"Beam size x in micrometers = {beam_size_x:.3g}\n",
    f"Beam size y in micrometers = {beam_size_y:.3g}\n",
    f"Pointing stability in axis x in micrometers = {pointing_stability_x_axis:.3g}\n",
    f"Pointing stability in axis y in micrometers = {pointing_stability_y_axis:.3g}\n",
    f"Pointing stability in axis r in micrometers = {pointing_stability_radial_axis:.3g}\n",
    f"Beams average x position in pixels = {average_beam_position_x:.3g}\n",
    f"Beams average y position in pixels = {average_beam_position_y:.3g}\n",
    f"Pixel size in micrometers = {pixel_size:.3g}\n",
    f"Name of the directory of the images = {images_directory}\n",
]
output_file.writelines(lines)
output_file.close()

# plotting beam positions for all images:
plt.tight_layout()
plt.plot(beams_position_x, beams_position_y, ".")
plt.title("Beam Position of All Images")
plt.ylabel("Y axis [pixels]")
plt.xlabel("X axis [pixels]")
plt.grid(True)
plt.savefig("Beam Position of All Images")
plt.show()

# time plot of beam positions assuming 10Hz capture rate:
Hz_to_sec = 1.0 / 10.0
beams_position_time = list(
    range(len(beams_position_x * Hz_to_sec))
)  # time axis in seconds
plt.tight_layout()
plt.plot(beams_position_time, beams_position_x, ".", label="Beam position x axis")
plt.plot(beams_position_time, beams_position_y, ".", label="Beam position y axis")
plt.title("Beam Position as Function of Time")
plt.ylabel("Beam Position [pixels]")
plt.xlabel("Time [sec]")
plt.grid(True)
plt.legend()
plt.savefig("beam position as function of time plot")
plt.show()
