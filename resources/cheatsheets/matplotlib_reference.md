# Matplotlib Quick Reference

Essential Matplotlib operations for data visualization practicals.

## Importing
```python
import matplotlib.pyplot as plt
import numpy as np
```

## Basic Line Plot
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.grid(True)
plt.show()
```

## Multiple Lines
```python
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.legend()
plt.show()
```

## Scatter Plot
```python
plt.scatter(x, y, c='blue', marker='o', s=50, alpha=0.5)
plt.title('Scatter Plot')
plt.show()
```

## Bar Chart
```python
# Vertical bars
plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()

# Horizontal bars
plt.barh(categories, values)
plt.show()
```

## Histogram
```python
plt.hist(data, bins=20, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

## Pie Chart
```python
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Pie Chart')
plt.show()
```

## Subplots
```python
# Create 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y1)
axes[0, 0].set_title('Plot 1')

axes[0, 1].scatter(x, y2)
axes[0, 1].set_title('Plot 2')

axes[1, 0].bar(categories, values)
axes[1, 0].set_title('Plot 3')

axes[1, 1].hist(data, bins=20)
axes[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
```

## Styling
```python
# Line styles
plt.plot(x, y, linestyle='-')   # solid
plt.plot(x, y, linestyle='--')  # dashed
plt.plot(x, y, linestyle='-.')  # dash-dot
plt.plot(x, y, linestyle=':')   # dotted

# Markers
plt.plot(x, y, marker='o')      # circle
plt.plot(x, y, marker='s')      # square
plt.plot(x, y, marker='^')      # triangle
plt.plot(x, y, marker='*')      # star

# Colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='#FF5733')
plt.plot(x, y, color=(0.1, 0.2, 0.5))
```

## Common Colors
```python
'b' - blue
'g' - green
'r' - red
'c' - cyan
'm' - magenta
'y' - yellow
'k' - black
'w' - white
```

## Customization
```python
# Figure size
plt.figure(figsize=(10, 6))

# Title and labels
plt.title('Title', fontsize=16, fontweight='bold')
plt.xlabel('X Label', fontsize=12)
plt.ylabel('Y Label', fontsize=12)

# Limits
plt.xlim(0, 100)
plt.ylim(-10, 10)

# Grid
plt.grid(True, alpha=0.3, linestyle='--')

# Legend
plt.legend(loc='best')          # Auto position
plt.legend(loc='upper right')
plt.legend(loc='lower left')

# Ticks
plt.xticks(rotation=45)
plt.yticks(range(0, 101, 10))
```

## Saving Figures
```python
# Save as PNG
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

# Save as PDF
plt.savefig('plot.pdf', bbox_inches='tight')

# Save as SVG
plt.savefig('plot.svg', bbox_inches='tight')
```

## Box Plot
```python
plt.boxplot([data1, data2, data3], labels=['A', 'B', 'C'])
plt.title('Box Plot')
plt.show()
```

## Heatmap (using imshow)
```python
data = np.random.rand(10, 10)
plt.imshow(data, cmap='viridis', aspect='auto')
plt.colorbar()
plt.title('Heatmap')
plt.show()
```

## Common Colormaps
```python
'viridis', 'plasma', 'inferno', 'magma'  # Perceptually uniform
'hot', 'cool', 'spring', 'summer', 'autumn', 'winter'
'Blues', 'Reds', 'Greens', 'Greys'
'jet', 'rainbow', 'hsv'  # Not recommended for scientific plots
```

## Annotations
```python
plt.annotate('Important Point', 
             xy=(x_point, y_point),
             xytext=(x_text, y_text),
             arrowprops=dict(arrowstyle='->', color='red'))
```

## Text
```python
plt.text(x, y, 'Text', fontsize=12, ha='center', va='center')
```

## Multiple Figures
```python
# Figure 1
plt.figure(1)
plt.plot(x, y1)

# Figure 2
plt.figure(2)
plt.plot(x, y2)

plt.show()
```

## 3D Plots
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

## Style Sheets
```python
# Available styles
plt.style.available

# Use a style
plt.style.use('seaborn-v0_8')
plt.style.use('ggplot')
plt.style.use('dark_background')
```

## Common Patterns
```python
# Quick plot with customization
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2, label='Data')
ax.set_title('Title', fontsize=14)
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Tips
- Always close figures when done: `plt.close()`
- Use `plt.tight_layout()` to prevent label overlap
- Use `bbox_inches='tight'` when saving to avoid cropping
- Use high DPI (300) for publication-quality figures
- Clear current figure: `plt.clf()`
- Clear current axes: `plt.cla()`

## More Resources
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Matplotlib Cheat Sheet](https://matplotlib.org/cheatsheets/)
