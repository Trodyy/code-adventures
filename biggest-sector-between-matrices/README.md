# Matrix Similarity Finder

This project implements a simplified prototype of an AI concept: finding which image (represented as a matrix) is most similar to a reference image.  
Each image is represented as a 2D matrix of pixel intensities (values between 0 and 255). The program compares these matrices element-by-element to determine similarity.

---

## Project Purpose

This project is part of a larger conceptual study on **image similarity detection** using basic mathematical models.  
See the separate [PURPOSE.md](PURPOSE.md) file for a detailed explanation of the motivation, AI background, and future goals of this experiment.

---

## How It Works

1. The program first asks the user for a matrix size (e.g. `100`).
2. It generates **10 matrices** (`a`–`j`) with random integer values between `0` and `255`.
3. Matrix `a` is the **reference image**.
4. Each other matrix (`b`–`j`) is compared pixel-by-pixel to `a`.
5. The program counts the number of identical pixels in corresponding positions.
6. Finally, it prints which matrix is most similar to `a`.

---

## Example Output
The ouput is st5h like this : 
```
{'b': 3945, 'c': 3917, 'd': 3792, 'e': 3965, 'f': 3873, 'g': 3883, 'h': 3893, 'i': 3888, 'j': 3845}
```
The most similarity is the element that hs the biggest value.For example in the above output, matrix e has the most similarity with matrix a.
