import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objs as go


# Function to fetch the company name for a given stock symbol
def fetch_company_name(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <h1> element with the specified class
        h1_element = soup.find('h1', class_='h2 shrink-text')

        # Get the text content from the h1 element
        if h1_element:
            return h1_element.text.strip()  # Return the company name
        else:
            return "Company name element not found."
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"


# Function to fetch Stock P/E for a given stock symbol
def fetch_stock_pe(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all li elements with the specified class
        li_elements = soup.find_all('li', class_='flex flex-space-between')

        # Initialize a variable to hold the number
        number = None

        # Iterate through the li elements to find 'Stock P/E'
        for li in li_elements:
            name_element = li.find('span', class_='name')
            if name_element and 'Stock P/E' in name_element.text:
                # If 'Stock P/E' is found, get the corresponding number span
                number_element = li.find('span', class_='number')
                if number_element:
                    number = number_element.text
                    break  # Exit the loop once the number is found

        # Return the extracted number or a message if not found
        return number if number else "Stock P/E not found."
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"


# Function to fetch the NSE symbol for a given stock symbol
def fetch_nse_symbol(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <span> elements with the specified class
        span_elements = soup.find_all('span', class_='ink-700 upper')

        # Iterate through each span element and check if it contains 'NSE:'
        for span in span_elements:
            text = span.get_text(strip=True)  # Get the text content
            if 'NSE:' in text:  # Check if the text contains 'NSE:'
                # Split the text after 'NSE:' and get the part that follows
                nse_value = text.split('NSE:')[-1].strip()
                return nse_value  # Return the extracted NSE value
        
        return "NSE symbol not found."
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"



# Function to fetch the Market Cap for a given stock symbol
def fetch_market_cap(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all li elements with the specified class
        li_elements = soup.find_all('li', class_='flex flex-space-between')

        # Initialize a variable to hold the Market Cap
        market_cap = None

        # Iterate through the li elements to find 'Market Cap'
        for li in li_elements:
            name_element = li.find('span', class_='name')
            if name_element and 'Market Cap' in name_element.text:
                # If 'Market Cap' is found, get the corresponding number span
                number_element = li.find('span', class_='number')
                if number_element:
                    market_cap = number_element.text.strip()  # Clean the text
                    break  # Exit the loop once the Market Cap is found

        # Return the extracted Market Cap or a message if not found
        return market_cap if market_cap else "Market Cap not found."
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"



# Function to fetch the Net Profit+ for a given stock symbol
def fetch_net_profit(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all tables by their class name (this will give us all the tables with the class 'data-table')
        tables = soup.find_all('table', class_='data-table')


        # Check if there are at least two tables
        if len(tables) > 1:
            # Work with the second table
            table = tables[1]

            # Initialize a list to store the extracted data
            data = []
    
            # Iterate over each row in the table body (tbody)
            for row in table.tbody.find_all('tr'):
                # Extract all cells (td elements) in the row
                cells = row.find_all('td')
                
                # Get the text content of each cell and strip any extra spaces
                row_data = [cell.get_text(strip=True) for cell in cells]
                
                # Append the cleaned row data to the main data list
                data.append(row_data)
    
            # Iterate through the data to find the list that starts with 'Net Profit+'
            net_profit_list = []
            for lst in data:
                if lst and lst[0] == 'Net Profit+':
                    net_profit_list = lst
                    break
    
            # Get the 12th item from the 'Net Profit+' list (index 11)
            net_profit = net_profit_list[12] if len(net_profit_list) > 12 else None
    
            # Return the extracted Net Profit or a message if not found
            return net_profit if net_profit else "Net Profit+ data not found."
        else:
            print("Less than 2 tables found with the class 'data-table'.")
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"



# Function to fetch 5-year Median ROCE for a given stock symbol
def fetch_median_roce(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all tables with the specified class name
        tables = soup.find_all('table', class_='data-table responsive-text-nowrap')

        if len(tables) < 5:
            return "ROCE table not found."

        # Access the ROCE table (index 4, as indicated)
        roce_table = tables[4]

        # Find all rows in the table body
        rows = roce_table.find('tbody').find_all('tr')

        if len(rows) < 6:
            return "ROCE row not found."

        # Extract the sixth row (index 5)
        roce_row = rows[5]

        # Extract the sixth column (index 6) in that row for the 5-year Median ROCE
        roce = roce_row.find_all('td')[5].text.strip()

        # Return the extracted 5-year Median ROCE
        return roce if roce else "5-year Median ROCE not found."
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"



# Function to fetch sales and profit growth data for a given stock symbol
def fetch_growth_data(symbol):
    # Construct the URL using the stock symbol
    url = f"https://www.screener.in/company/{symbol}/consolidated/"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the first table (Compounded Sales Growth)
        sales_table = soup.find_all('table', class_='ranges-table')[0]
        sales_rows = sales_table.find_all('tr')

        # Extract the second table (Compounded Profit Growth)
        profit_table = soup.find_all('table', class_='ranges-table')[1]
        profit_rows = profit_table.find_all('tr')

        # Extract the values from the sales table
        sales_growth_10yrs = sales_rows[1].find_all('td')[1].text.strip('%')
        sales_growth_5yrs = sales_rows[2].find_all('td')[1].text.strip('%')
        sales_growth_3yrs = sales_rows[3].find_all('td')[1].text.strip('%')
        sales_growth_ttm = sales_rows[4].find_all('td')[1].text.strip('%')

        # Extract the values from the profit table
        profit_growth_10yrs = profit_rows[1].find_all('td')[1].text.strip('%')
        profit_growth_5yrs = profit_rows[2].find_all('td')[1].text.strip('%')
        profit_growth_3yrs = profit_rows[3].find_all('td')[1].text.strip('%')
        profit_growth_ttm = profit_rows[4].find_all('td')[1].text.strip('%')

        # Creating a data dictionary for the DataFrame
        data = {
            '': ['10 yrs', '5 yrs', '3 yrs', 'TTM'],
            'Sales Growth': [sales_growth_10yrs, sales_growth_5yrs, sales_growth_3yrs, sales_growth_ttm],
            'Profit Growth': [profit_growth_10yrs, profit_growth_5yrs, profit_growth_3yrs, profit_growth_ttm]
        }

        # Create the DataFrame
        df = pd.DataFrame(data)

        # Transpose the DataFrame to make the first row the column headers
        df = df.T

        # Set the first row as the column names
        df.columns = df.iloc[0]  # Set the first row as column names
        df = df.drop(df.index[0])  # Drop the first row

        # Return the final DataFrame
        return df, sales_growth_10yrs, sales_growth_5yrs, sales_growth_3yrs, sales_growth_ttm, profit_growth_10yrs, profit_growth_5yrs, profit_growth_3yrs, profit_growth_ttm
    else:
        # Return an error message if the page cannot be retrieved
        return f"Failed to retrieve the page. Status code: {response.status_code}"



def convert_to_int(string_value):
    # Remove commas from the string and convert to integer
    return int(string_value.replace(',', ''))




def calculate_fy23_pe(market_cap, net_profit):
    if net_profit != 0:  # Ensure that net profit is not zero to avoid division by zero
        fy23_pe = market_cap / net_profit
    else:
        fy23_pe = None  # Handle case where net profit is zero
    return round(fy23_pe, 2)




def dcf_valuation(cost_of_capital, roce, growth_rate, high_growth_years, fade_years, terminal_growth_rate, tax_rate):
    intrinsic_value = 0  # Initial intrinsic value
    adjusted_roce = roce * (1 - tax_rate)  # Adjust RoCE for tax
    
    # Calculate intrinsic value for the high growth period
    for year in range(1, high_growth_years + 1):
        value_high_growth = adjusted_roce * ((1 + growth_rate) ** year)  # Growing by high growth rate
        intrinsic_value += value_high_growth / ((1 + cost_of_capital) ** year)  # Discounting
    
    # Calculate intrinsic value for the fade period
    for year in range(high_growth_years + 1, high_growth_years + fade_years + 1):
        # Growth linearly fades from high growth rate to terminal growth rate
        fade_growth_rate = growth_rate - (growth_rate - terminal_growth_rate) * (year - high_growth_years) / fade_years
        value_fade_growth = adjusted_roce * ((1 + fade_growth_rate) ** year)
        intrinsic_value += value_fade_growth / ((1 + cost_of_capital) ** year)  # Discounting
    
    # Calculate terminal value (post fade period)
    terminal_value = adjusted_roce * (1 + terminal_growth_rate) / (cost_of_capital - terminal_growth_rate)
    intrinsic_value += terminal_value / ((1 + cost_of_capital) ** (high_growth_years + fade_years))
    
    # Calculate Intrinsic PE by dividing the intrinsic value by adjusted RoCE
    intrinsic_pe = intrinsic_value / adjusted_roce
    
    return round(intrinsic_pe, 2)


def calculate_degree_of_overvaluation(current_pe, fy23_pe, intrinsic_pe):
    # Determine the lower of current PE and FY23 PE
    if current_pe < fy23_pe:
        degree_of_overvaluation = (current_pe / intrinsic_pe) - 1
    else:
        degree_of_overvaluation = (fy23_pe / intrinsic_pe) - 1
    
    return degree_of_overvaluation




# Streamlit app UI
st.title("Stock Analysis & DCF Valuation")

# User input for stock symbol
symbol = st.text_input("Enter Stock Symbol", "HAVELLS")

# Fetch and display the company name
company_name = fetch_company_name(symbol)
st.write(f"Company Name: {company_name}")


# Fetch and display the company name
current_pe = fetch_stock_pe(symbol)
st.write(f"Current PE: {current_pe}")


# Fetch and display the NSE symbol
nse_symbol = fetch_nse_symbol(symbol)
st.write(f"Stock Symbol: {nse_symbol}")

# Fetch and display the market cap
market_cap_str = fetch_market_cap(symbol)
market_cap = convert_to_int(market_cap_str) if market_cap_str != "Market Cap not found." else None
st.write(f"Market Cap: {market_cap_str}")

# Fetch and display the net profit
net_profit_str = fetch_net_profit(symbol)
net_profit = convert_to_int(net_profit_str) if net_profit_str != "Net Profit not found." else None
st.write(f"Net Profit (FY23): {net_profit_str}")

# Calculate and display the PE ratio
if market_cap and net_profit:
    pe_ratio = calculate_fy23_pe(market_cap, net_profit)
    st.write(f"FY23PE: {pe_ratio}")
else:
    st.write("Unable to calculate PE Ratio.")


# Fetch and display the 5-year Median ROCE
roce = fetch_median_roce(symbol)
st.write(f"5-year Median ROCE: {roce}")


# Fetch and display the Growth Data
growth_data_table, sales_growth_10yrs, sales_growth_5yrs, sales_growth_3yrs, sales_growth_ttm, profit_growth_10yrs, profit_growth_5yrs, profit_growth_3yrs, profit_growth_ttm  = fetch_growth_data(symbol)
st.table(growth_data_table)


# Time periods for the X-axis
time_periods = ['10 Years', '5 Years', '3 Years', 'TTM']

# Sales growth values
sales_growth = [sales_growth_10yrs, sales_growth_5yrs, sales_growth_3yrs, sales_growth_ttm]

# Profit growth values
profit_growth = [profit_growth_10yrs, profit_growth_5yrs, profit_growth_3yrs, profit_growth_ttm]

# Create a Plotly bar chart
fig = go.Figure()

# Adding sales growth bars
fig.add_trace(go.Bar(
    x=time_periods,
    y=sales_growth,
    name='Sales Growth (%)',
    marker_color='lightblue'
))

# Adding profit growth bars
fig.add_trace(go.Bar(
    x=time_periods,
    y=profit_growth,
    name='Profit Growth (%)',
    marker_color='lightgreen'
))

# Customize layout
fig.update_layout(
    title='Sales vs Profit Growth Over Different Periods',
    xaxis_title='Time Periods',
    yaxis_title='Growth (%)',
    barmode='group',  # Groups the bars side by side
    legend_title='Growth Type',
    template='plotly_white'
)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)




# DCF Valuation Parameters
st.subheader("DCF Valuation Parameters")
cost_of_capital = st.slider("Cost of Capital", 8, 16, 12)
roce = st.slider("RoCE", 10, 100, 20)
growth_rate = st.slider("Growth Rate", 8, 20, 12)
high_growth_years = st.slider("High Growth Years", 11, 25, 15)
fade_years = st.slider("Fade Years", 5, 20, 15)
terminal_growth_rate = st.slider("Terminal Growth Rate", 0.0, 7.5, 5.0)
tax_rate = 0.25

# Calculate and display DCF valuation
intrinsic_pe = dcf_valuation(cost_of_capital, roce, growth_rate, high_growth_years, fade_years, terminal_growth_rate, tax_rate)
st.markdown(f"### **Intrinsic PE: {intrinsic_pe}**")

overvaluation = round(calculate_degree_of_overvaluation(float(current_pe), float(pe_ratio), intrinsic_pe), 2) * 100
st.markdown(f"### **Degree of overvaluation: {overvaluation}%**")


# Contact information
st.markdown("---")
st.subheader("Contact")
st.write("""
If you have any questions, feedback, or want to know more about the project, feel free to reach out to the creator at:

**Name:** Lawal Abdulazeez Faruq
         
**Email:** lawalabdulazeezfaruq@gmail.com 
         
**GitHub:** [BnBazz@Github](https://github.com/Lawal0abdulazeez)  
""")

# Footer with a cool design
st.markdown("---")
st.write("**Thank you for using Our Stock analysis and DCF valuations**")
st.markdown("Made with ❤️ by Lawal Abdulazeez Faruq.")
