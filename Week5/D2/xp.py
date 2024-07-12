#Exercice 1 
#A company’s financial reports stored in an Excel file.

#Structured Data: Excel files typically contain structured data with clearly defined fields, columns, and rows that can be easily sorted and analyzed. The data is organized in a tabular format.
#Photographs uploaded to a social media platform.

#Unstructured Data: Photographs do not have a predefined data model or structure. They are multimedia files that cannot be easily categorized or analyzed without metadata or additional processing.
#A collection of news articles on a website.

#nstructured Data: News articles consist of text that does not follow a fixed structure. They contain paragraphs, headings, and various other elements that make it challenging to categorize without natural language processing techniques.
#Inventory data in a relational database.

#Structured Data: Relational databases store data in tables with predefined schemas, consisting of rows and columns. Inventory data in such a database is well-organized and can be easily queried using SQL.
#Recorded interviews from a market research study.

#Unstructured Data: Recorded interviews are audio or video files that lack a predefined structure. Analyzing them typically requires transcription and natural language processing to extract meaningful insights.
#This classification helps in understanding the nature of different types of data and determining the appropriate methods and tools for processing and analysis.

#Exercice 2 
#A series of blog posts about travel experiences.

#Method: Text Parsing and Tagging
#Explanation: Use Natural Language Processing (NLP) techniques to parse the text and identify key elements such as the title, date, location, activities, and sentiments. These elements can then be stored in a structured format like a database or CSV file with columns for each identified element.
#Example: Title, Date, Location, Activities, Sentiments, etc.
#Audio recordings of customer service calls.

#Method: Speech-to-Text Transcription and Sentiment Analysis
#Explanation: Use speech-to-text software to convert the audio recordings into text. Once transcribed, further analyze the text using NLP to extract key information such as customer name, issue type, resolution, and sentiment. This information can then be stored in a structured format.
#Example: Customer ID, Date, Issue Type, Resolution, Sentiment, Duration, etc.
#Handwritten notes from a brainstorming session.

#Method: Optical Character Recognition (OCR) and Text Categorization
#Explanation: Use OCR technology to digitize the handwritten notes and convert them into machine-readable text. Afterward, categorize the text into relevant topics or themes discussed during the session. This structured data can be organized into a table with columns representing different categories or themes.
#Example: Idea ID, Category, Description, Contributor, Priority Level, etc.
#A video tutorial on cooking.

#Method: Video Transcription and Content Tagging
#Explanation: Use video transcription tools to extract the audio content into text. Further segment the text into structured steps, ingredients, and instructions. Additionally, tag the video content with time markers for each step and ingredient. This structured information can be organized into a detailed recipe format.
#Example: Step Number, Time Marker, Instruction, Ingredient, Quantity, etc.
#By converting unstructured data into structured formats, it becomes easier to analyze, search, and derive insights from the data.

#Exercice 3 
#Transaction records

#Type: Structured
#Reason: Transaction records typically contain data in a structured format with fields like transaction ID, date, time, customer ID, product ID, quantity, price, etc.
#Customer feedback comments

#Type: Unstructured
#Reason: Customer feedback comments are often free-text fields where customers express their opinions, complaints, or suggestions in a natural language.
#Social media posts about your brand

#Type: Unstructured
#Reason: Social media posts are free-form text and can include images, videos, hashtags, mentions, and other elements that are not inherently structured.
#Employee work schedules

#Type: Structured
#Reason: Work schedules are usually organized in a tabular format with fields like employee ID, name, shift date, start time, end time, and role.
#Using Data to Improve Business Operations
#Transaction Records

#Usage:
#Sales Analysis: Analyze transaction data to identify top-selling products, peak sales times, and customer purchasing patterns.
#Inventory Management: Use sales data to predict demand and optimize inventory levels, reducing overstock and stockouts.
#Pricing Strategies: Assess the impact of pricing changes on sales and profits to develop more effective pricing strategies.
#Customer Feedback Comments

#Usage:
#Sentiment Analysis: Apply natural language processing (NLP) techniques to determine the overall sentiment (positive, negative, neutral) of customer feedback. Use this information to identify areas needing improvement.
#Product Improvement: Identify common issues or suggestions related to specific products, leading to product enhancements or new product development.
#Customer Service: Use feedback to train customer service teams and improve their responses to common customer complaints.
#Social Media Posts About Your Brand

#Usage:
#Brand Sentiment: Monitor social media sentiment to gauge public perception of your brand. Respond to negative posts promptly to manage reputation.
#Trend Analysis: Identify emerging trends and topics related to your brand. Use this information to create targeted marketing campaigns.
#Engagement Metrics: Measure the effectiveness of social media campaigns by tracking likes, shares, comments, and mentions.
#Employee Work Schedules

#Usage:
#Workforce Optimization: Analyze work schedules to ensure optimal staffing levels during peak hours and reduce labor costs during slow periods.
#Employee Performance: Correlate work schedules with performance metrics to identify patterns that lead to higher productivity or job satisfaction.
#Compliance and Planning: Ensure that schedules comply with labor laws and company policies. Plan for future staffing needs based on historical data and business forecasts.
#By effectively categorizing and analyzing both structured and unstructured data, your retail company can gain valuable insights to enhance various aspects of business operations, from sales and marketing to customer service and workforce management.

#Exercice 4 
# Step 1: Import the necessary libraries
from faker import Faker
import numpy as np
import pandas as pd

# Step 2: Initialize the Faker instance
fake = Faker()

# Step 3: Generate a list of 100 random names, addresses, and email addresses
data = {
    "Name": [fake.name() for _ in range(100)],
    "Address": [fake.address() for _ in range(100)],
    "Email": [fake.email() for _ in range(100)]
}

# Step 4: Generate random ages (between 20 and 60) and income levels
np.random.seed(0)  # For reproducibility
data["Age"] = np.random.randint(20, 61, size=100)
data["Income"] = np.random.randint(30000, 120001, size=100)

# Step 5: Combine this data into a pandas DataFrame and name the columns appropriately
df = pd.DataFrame(data)

# Step 6: Display the first 10 rows of the DataFrame
print(df.head(10))

#Exercice 6
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Simulate traffic data
def simulate_traffic_data(duration_hours=24):
    time_intervals = pd.date_range(start='2023-01-01 00:00', end='2023-01-02 00:00', freq='5T')
    data = []

    for time in time_intervals:
        hour = time.hour
        if 7 <= hour < 9 or 17 <= hour < 19:
            vehicle_count = random.randint(50, 100)  # Peak hours
            avg_speed = random.uniform(20, 40)      # Lower speeds due to congestion
        else:
            vehicle_count = random.randint(10, 50)  # Off-peak hours
            avg_speed = random.uniform(40, 60)      # Higher speeds due to less traffic

        data.append({
            'timestamp': time,
            'vehicle_count': vehicle_count,
            'avg_speed': avg_speed
        })

    df = pd.DataFrame(data)
    return df

# Generate the traffic data
traffic_data = simulate_traffic_data()
print(traffic_data.head())

