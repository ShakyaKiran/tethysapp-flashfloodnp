**Flash Flood Nepal
An interactive web application developed on Tethys Platform for monitoring, forecasting, and visualizing flash flood risks across river basins in Nepal.
---
📋 Features
Real-time & Forecast Visualizations: Interactive maps displaying flash flood risk zones and precipitation forecasts.
Hydrological Time Series: Hydrographs and historical discharge/threshold comparisons.
Spatial Data Integration: Layer controls for administrative boundaries, river networks, and flood hazard zones.
---
🛠️ Prerequisites
Before installing the Flash Flood Nepal application, ensure you have the following installed on your system:
Conda (Miniconda or Anaconda) or Micromamba
Python 3.10 or higher
Git**
---
🚀 Step 1: Install Tethys Platform
Tethys Platform provides the web framework and hosting environment for this geoscientific web app.
Option A: Using Conda (Recommended)

> **Note:** For production installations refer to the [Official Tethys Platform Installation Guide](http://docs.tethysplatform.org/en/stable/installation.html).
---
📦 Step 2: Install the Flash Flood Nepal App
Activate your Tethys Conda/Virtual Environment:
```bash
   conda activate tethys
   ```
Clone this repository:
```bash
   git clone https://github.com/<your-username>/tethysapp-flashflood_nepal.git
   cd tethysapp-flashflood_nepal
   ```
Install the application into Tethys:
```bash
   tethys install
   ```
If prompted during installation, accept the default option to install in development mode (`tethys install -d`).
(Optional) Sync persistent stores/databases (if applicable):
```bash
   tethys syncstores flashflood_nepal
   ```
---
🏃 Step 3: Run the Application
Start the Tethys development server:
```bash
   tethys start
   ```
Open your web browser and navigate to:
```text
   http://localhost:8000
   ```

