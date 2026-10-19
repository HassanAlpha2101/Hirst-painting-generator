# 🎨 Hirst Painting Generator

A Python application that programmatically generates Damien Hirst-inspired spot paintings by extracting color palettes from images and rendering a randomized grid using Python's built-in `turtle` graphics module.

Built as part of the **#100DaysOfCode** Python journey.

---

## ✨ Features

* **Automated Color Extraction:** Uses the `colorgram` library to parse an image and extract a distinct RGB color palette.
* **Dynamic Window Scaling:** Automatically retrieves the screen width and height to calculate the precise starting coordinates for the canvas grid.
* **Procedural Art Generation:** Utilizes nested loops and `random.choice()` to paint a clean, randomized grid of colored dots.

---

## 🛠️ Prerequisites & Dependencies

Make sure you have Python installed along with the required external package:

```bash
pip install colorgram.py
