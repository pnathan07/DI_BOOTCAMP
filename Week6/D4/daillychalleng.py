# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_point
import plotly.express as px

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Matplotlib Task: Histogram of Petal Lengths
plt.figure(figsize=(8, 6))
plt.hist(iris['petal_length'], bins=20, edgecolor='black')
plt.title('Histogram of Petal Lengths')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# Seaborn Task: Pair Plot
sns.pairplot(iris, hue='species', palette='Set2')
plt.suptitle('Pairwise Relationships in Iris Dataset', y=1.02)
plt.show()

# Plotnine Task: Scatter Plot of Sepal Length vs. Sepal Width
scatter_plot = (ggplot(iris, aes(x='sepal_length', y='sepal_width', color='species')) +
                geom_point() +
                ggtitle('Scatter Plot of Sepal Length vs. Sepal Width') +
                xlab('Sepal Length') +
                ylab('Sepal Width'))

print(scatter_plot)

# Plotly Task: Interactive 3D Scatter Plot
fig = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_length',
                    color='species', symbol='species', opacity=0.7)
fig.update_layout(title='Interactive 3D Scatter Plot of Iris Dataset',
                  scene=dict(xaxis_title='Sepal Length', yaxis_title='Sepal Width', zaxis_title='Petal Length'))
fig.show()
