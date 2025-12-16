# Laser Beam Profiling & Stability Analysis

## Overview
This repository contains the code for a final project in the **Computers for Physics** course at **Tel Aviv University** (2025).

The project focuses on the characterization of laser beams using scientific image processing. By analyzing raw sensor data, the tool measures the beam's profile, calculates its width using statistical fitting, and tracks the "pointing stability" (positional drift) over time.

## Project Context
This software was developed as part of the academic curriculum for a Physics degree. The code was written specifically to meet the final project directives provided by the course instructors.

The implementation follows the course guidelines for:
* **Data Handling:** Loading and processing raw scientific images.
* **Physical Modeling:** Implementing the specific 2D Gaussian fitting algorithms required by the lab instructions.
* **Stability Metrics:** Calculating Root Mean Square (RMS) error to quantify beam stability.

## Features
* **Data Ingestion:** Loads `.tiff` images from a specified directory.
* **Signal Processing:** Reduces noise by summing pixel counts along orthogonal axes.
* **Gaussian Fitting:** Fits the beam intensity to a Gaussian model to extract amplitude, position, and width ($\sigma$).
* **Unit Conversion:** Converts pixel measurements to physical micrometers ($\mu m$) using sensor metadata.
* **Stability Analysis:** Tracks the beam center across multiple frames to calculate pointing stability.

## Technologies Used
* **Python 3.x**
* **NumPy:** For array manipulation and efficient summation.
* **SciPy:** For the `curve_fit` optimization algorithms.
* **Matplotlib:** For generating data visualizations.
* **Tifffile:** For handling TIFF image formats.

## Installation
1.  Clone the repository.
2.  Install the required dependencies:
    ```bash
    pip install numpy scipy matplotlib tifffile imagecodecs
    ```

## Usage
**Note:** The original experimental data provided by the course instructors is private and not included in this repository.

To run the analysis:
1.  Ensure you have a valid dataset in the correct folder structure.
2.  Update `input.txt` to point to your data directory.
3.  Execute the main project script:
    ```bash
    python Final_Project_Main.py
    ```

## Project Structure
* `Final_Project_Main.py`: The core analysis logic and fitting algorithms.
* `input.txt`: Configuration file specifying the data directory and sensor size.

## Disclaimer
This code is intended as a portfolio piece to demonstrate scientific computing skills. **If you are a current student in this course, please adhere to the university's academic integrity policies.** Do not submit this code as your own work.
