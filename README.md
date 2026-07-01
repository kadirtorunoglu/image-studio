# 🖼️ Image Studio

A simple Python image processing application developed as part of the **METU-ROMER Software Internship** to practice collaborative software development using **Git**, **GitHub**, feature branches, pull requests, code reviews, and merge conflict resolution.

---

## 📌 Project Overview

The application allows users to perform basic image processing operations using the **Pillow (PIL)** library.

The project was developed collaboratively by four interns, with each intern implementing different image processing features on separate feature branches before integrating them into the main application.

---

## 🚀 Features

### First Development Iteration

- Convert an image to **Grayscale**
- Resize an image
- Rotate an image
- Apply a Blur filter

### Second Development Iteration

- Flip an image horizontally
- Adjust image brightness
- Add a text watermark
- Display image information
  - Image dimensions
  - File format
  - File size

---

## 📁 Project Structure

```
image-studio/
│
├── images/
│   └── image.jpg
│
├── output/
│
├── filters.py
├── utils.py
├── main.py
└── README.md
```

---

## 🛠 Requirements

- Python 3.10+
- Pillow

Install dependencies:

```bash
pip install pillow
```

---

## ▶️ Running the Project

Run the application:

```bash
python main.py
```

Example output:

```
Choose an operation:
1. Grayscale
2. Resize
3. Rotate
4. Blur
5. Flip Horizontal
6. Brightness
7. Watermark
8. Image Information
```

Processed images are saved inside the **output/** directory.

---

## 👨‍💻 Team Workflow

This project follows a collaborative Git workflow.

### Development Process

1. Create a feature branch
2. Implement one feature
3. Commit changes with meaningful commit messages
4. Push the branch
5. Open a Pull Request
6. Receive peer review
7. Merge into `main`
8. Resolve merge conflicts if necessary

---

## 🌿 Git Branches

Example:

```
main

feature/grayscale-filter
feature/resize
feature/rotate
feature/blur

feature/horizontal-flip
feature/brightness
feature/watermark
feature/image-info
```

---

## 🧰 Technologies Used

- Python
- Pillow (PIL)
- Git
- GitHub

---

## 🎯 Learning Objectives

This project demonstrates:

- Git branching strategy
- Feature-based development
- Pull Requests
- Code Reviews
- Merge Conflict Resolution
- Collaborative Software Development
- Basic Image Processing with Pillow

---

## 👥 Team Responsibilities

| Intern | First Feature | Second Feature |
|---------|--------------|----------------|
| Intern 1 | Grayscale Filter | Horizontal Flip |
| Intern 2 | Resize Image | Brightness Adjustment |
| Intern 3 | Rotate Image | Text Watermark |
| Intern 4 | Blur Filter | Image Information |

---

## 📄 License

This project was created for educational purposes as part of the **METU-ROMER Internship Program**.
