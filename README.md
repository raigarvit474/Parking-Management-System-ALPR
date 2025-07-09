# Parking Management System — ALPR Integration
The Parking Management System - ALPR is an automated license plate recognition (ALPR) solution designed to seamlessly integrate with our main application, [Park Ease](https://parkease-nu.vercel.app) ([Github Repository](https://github.com/Deven10103/ParkEase)). This system captures the license plate number of incoming vehicles, along with the exact timestamp and parking location, and sends this information as a JSON payload via a POST request to the ParkEase backend.

ParkEase then validates the entry by checking for an active booking associated with the detected license plate.

✅ If a valid booking exists, the vehicle is granted access.

❌ If no booking is found, the system automatically flags the entry and sends a violation alert to the registered ParkEase administrator.

## 🚀Setup
### Clone this repo

```bash
git clone https://github.com/raigarvit474/Parking-Management-System-ALPR.git
cd Parking-Management-System-ALPR
```
### Create a virtual environment with Python 3.12

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install the required dependencies
```bash
pip install -r requirements.txt
```

## 🧪Usage

Run the main.py file

```bash
python main.py
```
Once running, upload an image of the vehicle. The system will process the image, extract the license plate, and forward the data to ParkEase for verification. That’s it — you're good to go!