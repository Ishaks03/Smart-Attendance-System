import subprocess
import sys
import os

def run_script(script_name):
    """Helper function to run a Python script and display logs."""
    print(f"\n[INFO] Running {script_name} ...\n")
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"[WARN] {script_name} warnings/errors:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {script_name} failed:\n{e.stderr}")
        sys.exit(1)


def register_face():
    """Register a new person's face data."""
    os.makedirs("dataset", exist_ok=True)
    print("\n📸 Starting face registration process...")
    run_script("capture_images1.py")
    run_script("train_model1.py")
    print("\n✅ Face registered and model trained successfully!")


def take_attendance():
    """Recognize faces and mark attendance."""
    print("\n🎥 Starting face recognition and attendance marking...")
    run_script("recognise.py")
    run_script("report1.py")
    print("\n✅ Attendance marked and report generated!")


def main():
    print("\n===============================")
    print("  SMART ATTENDANCE SYSTEM")
    print("===============================")
    print("1. Register New Face")
    print("2. Take Attendance")
    print("===============================")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        register_face()
    elif choice == "2":
        take_attendance()
    else:
        print("\n❌ Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()

