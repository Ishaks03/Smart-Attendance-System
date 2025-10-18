# Smart Attendance System

Smart Attendance System is a lightweight Python project that detects and recognizes faces using OpenCV and marks attendance automatically. It supports registering new faces, training a recognizer, capturing attendance via webcam, and exporting attendance reports in CSV and Excel formats.

## Features

- Register and enroll faces with IDs and names
- Train a face recognition model (LBPH / OpenCV trainer)
- Capture images from webcam and recognize faces in real time
- Log attendance with ID, Name, Date, Time and export CSV / Excel reports
- Minimal dependencies and easy-to-run scripts

## Repository structure

- `capture_images1.py` - capture images of users for enrollment
- `train_model1.py` - train face recognizer using dataset in `dataset/`
- `recognise.py` - run real-time recognition and mark attendance
- `report1.py` - generate human-readable attendance reports and exports
- `main1.py` - (optional) high-level runner / integration
- `attendance.csv` - sample attendance log (auto-generated)
- `dataset/` - folder containing captured images per user
- `trainer/` - trained model files (e.g. `trainer.yml`) and `names.csv`
- `instance/` - local database files (e.g. `users.db`)
- `reports/` - exported attendance reports (CSV / XLSX)

## Prerequisites

- Python 3.8+ (this project was developed with Python 3.10)
- pip
- A webcam (for capture and recognition)

Install required packages (recommended to use a virtual environment):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell; use activate on cmd
pip install -r requirements.txt  # see notes — if requirements.txt is missing, install below packages
```

If `requirements.txt` is not present, install the common dependencies used by this project:

```
pip install opencv-python numpy pandas flask openpyxl
```

## Quick start

1. Capture images for a user:

	- Run `capture_images1.py` and follow on-screen instructions to enter ID and name. The script saves images to `dataset/`.

2. Train the recognizer:

	- Run `train_model1.py`. The trained model will be saved to `trainer/trainer.yml`.

3. Run recognition and mark attendance:

	- Run `recognise.py`. The script opens the webcam, recognizes faces, and appends attendance rows to `attendance.csv` and `reports/`.

4. Generate or view reports:

	- `report1.py` creates human-friendly CSV/XLSX reports inside the `reports/` folder.

## Configuration and notes

- The project uses OpenCV's LBPH face recognizer by default (see `train_model1.py`). You may substitute other models but update scripts accordingly.
- Filepaths and model names are hardcoded in scripts; change them in the script headers if you prefer a different layout.
- The `instance/` folder contains a small SQLite DB (`users.db`) used by parts of the app — do not delete it unless you want to reset user records.

## Testing

- Manual smoke tests:
  - Capture a new user, train, then run recognition and ensure attendance appears in `attendance.csv` and `reports/`.

## License

This repository currently has no explicit license file. If you want to publish it publicly, consider adding an OSI-approved license such as MIT (`LICENSE`).

## Next steps / Improvements

- Add a `requirements.txt` listing exact dependency versions.
- Add a small CLI or Flask UI to manage enrollment and view reports from a browser.
- Add unit tests for file I/O and model training steps.

---

If anything in this README should be adjusted (formatting, missing script descriptions, or specific usage flags), tell me which parts to change and I will update the file.
