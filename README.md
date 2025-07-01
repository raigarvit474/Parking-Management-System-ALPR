# Parking Management System ALPR
This is a Automatic License plate recognition model that sends our main application [Park Ease](parkease-nu.vercel.app) the License Plate Number of the vehicle entering along with the time stamp of entry and the parking location at which the vehicle is entering as a json object through a post request which is then used by our application to verify booking

## Setup
Clone this repo

```bash
git clone https://github.com/raigarvit474/Parking-Management-System-ALPR.git
```
Create a virtual environment with Python 3.12

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the required dependencies
```bash
pip install -r requirements.txt
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

# Usage

Run the main.py file

```bash
python main.py
```
Upload the image of the vehicle and you are good to go!