# Laser Beam Profiling & Stability Analysis

## Overview
This repository contains the code for a final project in the **Computers for Physics** course at **Tel Aviv University** (2023).

The project focuses on the characterization of laser beams using scientific image processing. By analyzing raw sensor data, the tool measures the beam's profile, calculates its width using statistical fitting, and tracks the "pointing stability" (positional drift) over time.

This script models the laser intensity using a 2-D [Gaussian Beam](https://en.wikipedia.org/wiki/Gaussian_beam) profile and shows Gaussian fit and residuals of the first image in the data directory as sanity check for the analysis of the rest of the algorithm.

## Data
This code meant to analyse the data of multiple frames that capture a constant laser beam. with the images stored as .tiff file type. 

## Project Context
This software was developed as part of the academic curriculum for a Physics degree. The code was written specifically to meet the final project directives provided by the course instructors.

The implementation follows the course guidelines for:
* **Data Handling:** Loading and processing raw scientific images.
* **Physical Modeling:** Implementing the specific 1-D Gaussian fitting algorithms required by the course instructions.
* **Stability Metrics:** Calculating Root Mean Square (RMS) error to quantify beam stability.

## Features
* **Data Ingestion:** Loads `.tiff` images from a specified directory.
* **Gaussian Fitting:** Fits the beam intensity to a Gaussian model to extract amplitude, position, and width ($\sigma$).
* **Stability Analysis:** Tracks the beam center across multiple frames to calculate pointing stability.

## Technologies Used
* **Python 3.11**
* **NumPy:** For array manipulation and efficient summation.
* **SciPy:** For the `curve_fit` optimization algorithms.
* **Matplotlib:** For generating data visualizations.
* **Tifffile:** For handling TIFF image formats.

## Installation
1.  Clone the repository.
2.  Install the required dependencies:
    ```bash
    pip install numpy scipy matplotlib tifffile 
    ```

## Usage
**Note:** The original experimental data provided by the course instructors is private and not included in this repository.

To run the analysis:
1.  Ensure you have a valid dataset in the correct folder structure in .tiff format.
2.  Update `input.txt` to point to your data directory and camera specs.
3.  Execute the main project script:
    ```bash
    python Final_Project_Main.py
    ```
## Project Structure
* `Final_Project_Main.py`: The code.
* `input.txt`: text file specifying the data directory and sensor size.
* 'results_example': Example of code output.

## 🚀 Future Improvements
If I was required to expand and improve this project i would do the following:

* **Error Analysis:** Analyze the raw data noise using Bootstrap method.
* **Fit Analysis:** Add error bars to residuals fit and add chi squared reduced and P-value goodness of fit indicators.
* **Image difference:** Analyse the difference in variance of the beam Gaussian fit parameters across multiple frames. Since the beam source is constant we can use it analyse the system noise.
  
