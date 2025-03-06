import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "./sentimentdataset.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Drop rows with missing values (or you can fill them)
data.dropna(inplace=True)

# Convert 'Timestamp' to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Check data types
print(data.dtypes)

# Remove leading/trailing spaces from column names (Fix for KeyError: 'User ')
data.columns = data.columns.str.strip()

# Calculate total engagement metrics
total_engagement = data[['Likes', 'Retweets']].sum()
print(total_engagement)

# Calculate average engagement per post
average_engagement = data[['Likes', 'Retweets']].mean()
print(average_engagement)

# Group by date and calculate total likes and retweets
daily_engagement = data.groupby(data['Timestamp'].dt.date)[['Likes', 'Retweets']].sum()

# Display the daily engagement
print(daily_engagement)

# Group by user and calculate total likes and retweets
user_engagement = data.groupby('User')[['Likes', 'Retweets']].sum().reset_index()

# Sort by total likes to find key influencers
top_influencers = user_engagement.sort_values(by='Likes', ascending=False)
print(top_influencers.head())

# Sort the dataset by likes to find popular content
popular_content = data.sort_values(by='Likes', ascending=False)
print(popular_content[['Text', 'Likes', 'Retweets']].head())

# Plot daily engagement trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_engagement, x=daily_engagement.index, y='Likes', label='Likes')
sns.lineplot(data=daily_engagement, x=daily_engagement.index, y='Retweets', label='Retweets')
plt.title('Daily Engagement Trends')
plt.xlabel('Date')
plt.ylabel('Total Engagement')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot top influencers
plt.figure(figsize=(12, 6))
sns.barplot(data=top_influencers.head(10), x='User', y='Likes')
plt.title('Top 10 Influencers by Likes')
plt.xlabel('User')
plt.ylabel('Total Likes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()