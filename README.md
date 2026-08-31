# Digital Certificate Forgery Detection

<p align="center">
  <strong>Image Registration • XOR Difference Analysis • Morphological Processing</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-cv2-green)
![NumPy](https://img.shields.io/badge/NumPy-orange)
![Image Processing](https://img.shields.io/badge/Domain-Image%20Processing-purple)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

## 📌 Overview

A software-based certificate forgery detection system developed using classical image processing techniques to identify modifications in digital or scanned academic certificates.

The system compares a reference certificate with a test certificate by first aligning the documents and then analyzing their pixel-level differences. Suspicious regions are localized using image processing and contour analysis, followed by an authenticity score indicating the severity of detected modifications.

The final approach combines **image preprocessing, ORB-based registration, homography alignment, binary XOR difference analysis, morphological filtering, contour analysis, and authenticity scoring**.

---

## 🎯 Objective

The project aims to:

- Detect modifications in digital or scanned certificates
- Localize suspicious or tampered regions
- Reduce false detections caused by alignment variations and image noise
- Distinguish genuine and forged certificates
- Generate a quantitative authenticity score

---

## 🔬 Methodology

```text
Certificate Images
        │
        ▼
Preprocessing
        │
        ▼
ORB Feature Detection
        │
        ▼
Feature Matching + RANSAC
        │
        ▼
Image Registration
        │
        ▼
Binary Thresholding
        │
        ▼
XOR Difference Detection
        │
        ▼
Morphological Filtering
        │
        ▼
Contour Filtering
        │
        ▼
Tampered Region Localization
        │
        ▼
Authenticity Score
```

### Key Processing Steps

**1. Preprocessing**
- Image resizing
- Grayscale conversion
- CLAHE contrast enhancement
- Gaussian filtering
- Sharpening

**2. Image Registration**
- ORB feature extraction
- Brute Force feature matching
- Homography estimation using RANSAC
- Perspective warping for alignment

**3. Difference Detection**
- Binary thresholding
- Bitwise XOR comparison between aligned documents

**4. Noise Filtering**
- Morphological opening
- Dilation
- Contour filtering
- Removal of small noise regions and unwanted artifacts

**5. Authenticity Scoring**

The detected changes are used to calculate an authenticity score and classify the certificate as:

| Score | Classification |
|---:|---|
| > 90 | Authentic |
| 70–90 | Minor Tampering |
| < 70 | High Tampering |

---

## 💻 Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| OpenCV | Image processing and computer vision |
| NumPy | Numerical and image-array operations |
| ORB | Feature extraction |
| RANSAC | Homography estimation |
| Visual Studio Code | Development environment |

---

## 📂 Repository Structure

```text
digital-certificate-forgery-detection/
│
├── Code/
│   ├── preprocess.py
│   ├── doc_align.py
│   └── main.py
│
├── Documentation/
│   └── Project_Report.pdf
│
├── .gitignore
├── LICENSE
└── README.md
```

### Code Modules

| File | Description |
|---|---|
| `preprocess.py` | Performs image preprocessing and normalization |
| `doc_align.py` | Performs feature-based document alignment |
| `main.py` | Performs forgery detection, difference analysis, filtering and authenticity scoring |

---

## 📊 Experimental Evaluation

The system was evaluated using genuine and intentionally modified certificate samples.

The experiments included:

- Genuine certificate
- Date and GR number modification
- Heavy forgery
- Multi-field forgery

The implemented system successfully detected localized certificate modifications, highlighted suspicious regions, distinguished genuine and forged samples, and generated quantitative authenticity scores.

Detailed experimental outputs and observations are documented in the project report.

---

## 🔒 Privacy Notice

The original experimental results included images of certificates containing personally identifiable academic information such as names, GR/registration numbers, dates, and other certificate details.

For **privacy reasons, the certificate images and result screenshots are intentionally not included in this public repository**.

The original certificate images have therefore been removed from the publicly shared project materials. The repository contains the **source code and project report** so that the implementation and methodology can be reviewed without publicly distributing the personal information contained in the original certificate samples.

---

## 📄 Documentation

The complete project report is available in:

```text
Documentation/Project_Report.pdf
```

The report contains the detailed:

- Development process
- Algorithms and methodology
- Implementation details
- Experimental evaluation
- Results
- Conclusion
- Future scope

---

## 🔮 Future Scope

Potential improvements include:

- OCR-assisted semantic validation
- Field-level verification of names, GR numbers and dates
- GUI or web-based deployment
- Confidence heatmap visualization
- Support for multiple certificate templates

---

## 📌 Project Status

- ✅ Image preprocessing implemented
- ✅ Document registration implemented
- ✅ XOR-based difference detection implemented
- ✅ Morphological filtering implemented
- ✅ Tampered-region localization implemented
- ✅ Authenticity scoring implemented
- ✅ Tested on genuine and forged certificate samples

---

## 👨‍💻 Author

**Tejas Ravindra Kulkarni**

B.Tech — Instrumentation & Control Engineering

Vishwakarma Institute of Technology, Pune

---

## 📜 License

This project is licensed under the MIT License.
