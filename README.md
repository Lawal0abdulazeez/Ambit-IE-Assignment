# Stock Valuation and Financial Analysis Web Application

This project is an interactive financial analysis web application designed to analyze a company's financial data, calculate key financial metrics, and perform a valuation using a Discounted Cash Flow (DCF) model. The data is scraped from **screener.in**, and the web application is built using **Python** and **Streamlit**, with visualizations created using **Plotly**.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Data Collection](#data-collection)
4. [Financial Metrics Calculation](#financial-metrics-calculation)
5. [DCF Valuation](#dcf-valuation)
6. [Overvaluation Calculation](#overvaluation-calculation)
7. [Visualization with Plotly](#visualization-with-plotly)
8. [How to Run the App](#how-to-run-the-app)

---

## Introduction

This project replicates an interactive financial analysis tool for analyzing and valuing stocks. It scrapes key financial data from **screener.in**, calculates relevant financial metrics such as Sales Growth, Profit Growth, and Price-to-Earnings Ratio (PE), and then performs a stock valuation using a DCF model. The project also calculates the degree of stock overvaluation based on PE ratios and intrinsic values.

---

## Project Structure

The project has the following key components:

- **`app.py`**: The main script that runs the Streamlit web application with functions for scraping and calculations.
- **`working.ipynb`**: Used as testing to Handles web scraping from **screener.in** to gather financial data.
- **`requirements.txt`**: for all pre requisite for running the app easily.

---

## Data Collection

Data for the project is gathered by scraping the **screener.in** website. This includes key financial information such as:

- Sales Growth (10 years, 5 years, 3 years, TTM)
- Profit Growth (10 years, 5 years, 3 years, TTM)
- Current PE and FY23 PE
- Company Name
- 5yrs median ROCE
- Stock symbol

This data is cleaned and processed in the `working.ipynb` and `app.py` script, which extracts the necessary information using **BeautifulSoup**.

---

## Financial Metrics Calculation

Key financial metrics are calculated based on the scraped data. The main metrics include:

- **Sales Growth**: A critical metric that shows how much a company's sales have grown over different periods (10 years, 5 years, 3 years, and trailing twelve months).
- **Profit Growth**: Similar to sales growth, but focused on the company's profitability over different periods.
- **Price-to-Earnings Ratio (PE)**: Both current PE and FY23 PE are extracted to compare against the intrinsic PE.

The calculated metrics are displayed in the app for easy interpretation and decision-making.

---

## DCF Valuation

The **Discounted Cash Flow (DCF)** model is used to estimate the intrinsic value of the stock. The DCF calculation involves:

1. Estimating future cash flows.
2. Discounting those cash flows to the present value.
3. Determining the intrinsic value based on these discounted cash flows.

The intrinsic PE ratio is calculated based on the DCF model output, and this is used to gauge whether the stock is overvalued or undervalued.

---

## Overvaluation Calculation

The degree of overvaluation is determined by comparing the lower of **current PE** or **FY23 PE** with the **intrinsic PE** from the DCF calculation. The formula used is:

- **If Current PE < FY23 PE**:
  \[
  \text{Degree of Overvaluation} = \left(\frac{\text{Current PE}}{\text{Intrinsic PE}}\right) - 1
  \]
- **Else**:
  \[
  \text{Degree of Overvaluation} = \left(\frac{\text{FY23 PE}}{\text{Intrinsic PE}}\right) - 1
  \]

This allows investors to assess how overpriced or underpriced a stock is relative to its intrinsic value.

---

## Visualization with Plotly

The financial data is visualized using **Plotly** for better insights. The key visualizations include:

1. **Sales Growth vs Profit Growth**: A side-by-side bar chart that displays sales and profit growth over different periods (10 years, 5 years, 3 years, TTM).
2. **Stock Overvaluation**: Visual representation of how much the stock is overvalued based on the PE comparison.

The use of Plotly allows for interactive and dynamic visualizations that can be easily manipulated within the app.

---

## How to Run the App

### Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **Streamlit**
- **BeautifulSoup**
- **Plotly**

### Steps

1. Clone this repository:
    ```bash
    git clone https://github.com/Lawal0abdulazeez/Ambit-IE-Assignment
    ```
   
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and navigate to the local URL provided by Streamlit to interact with the app.

---

## License

This project is licensed under the APACHE 2.0 License. See the [LICENSE]( http://www.apache.org/licenses/) file for more details.
