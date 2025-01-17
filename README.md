# Investing-Portfolio-Tracker

Overview
The Investing Portfolio Tracker is a Python-based application designed to help users monitor and evaluate their stock portfolio performance. The tool fetches real-time stock price data using yfinance, calculates detailed metrics like profit/loss and percentage change, and generates a professional, visually appealing HTML report styled with CSS. It also creates a dynamic portfolio distribution chart using matplotlib for enhanced data visualization.

Features
Real-Time Data Integration: Fetches live stock price data via yfinance API to ensure up-to-date portfolio calculations.
Portfolio Analytics: Calculates key metrics for each stock, including:
Current value
Profit/Loss
Percentage change
Interactive Reports: Generates an HTML report displaying portfolio metrics in a tabular format, styled with an external CSS file for a clean, professional look.
Data Visualization: Creates a portfolio distribution pie chart to visualize the allocation of investments.
Ease of Use: Automates the generation of reports and visualizations for streamlined investment tracking.
Technologies Used
Python: Core logic and data processing.
yfinance: Fetching real-time stock data.
matplotlib: Creating portfolio distribution charts.
HTML & CSS: Building and styling the dynamic portfolio report.
How to Use
Clone this repository to your local machine.
Ensure the required dependencies (yfinance, matplotlib) are installed.


pip install yfinance matplotlib


Prepare a portfolio.csv file with your portfolio details in the following format:
<img width="338" alt="Screenshot 2025-01-16 at 11 47 11 PM" src="https://github.com/user-attachments/assets/74246811-e3c2-4e5b-9696-33be3d0dbb1a" />



Run the Python script to generate the report:

python generate_report.py

Open the generated portfolio.html file in a web browser to view the report.
