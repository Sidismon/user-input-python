import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset (replace with your dataset path if different)
data = pd.read_csv('iris.csv')

# Display the first 5 rows
print(data.head())

# Get information about the data
print(data.info())

# Display summary statistics
print(data.describe())


# Check for missing values
print(data.isnull().sum())

# Handle missing values (e.g., fill with mean, median, or mode)
data.fillna(data.mean(), inplace=True)  # Replace missing values with the mean

# Remove duplicates (if any)
data.drop_duplicates(inplace=True)

# Group by species and calculate mean sepal length
grouped_data = data.groupby('species')['sepal_length'].mean()
print(grouped_data)

# Assuming you have a time series dataset with 'date' and 'sales' columns
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(data['species'], data['sepal_length'])
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Average Sepal Length by Species')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['sepal_length'], bins=20)
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(data['sepal_length'], data['petal_length'])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Scatter Plot of Sepal Length vs. Petal Length')
plt.show() 




