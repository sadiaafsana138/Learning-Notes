# 📚 Python Data Science Master Cheatsheets

A collection of 7 comprehensive Jupyter notebook cheatsheets covering the full Python data science and visualization stack — from array math to interactive web apps.

---

## 📂 Files

| Notebook | Library | Sections |
|---|---|---|
| `numpy_master_cheatsheet.ipynb` | NumPy | 28 |
| `pandas_master_cheatsheet.ipynb` | Pandas | 28 |
| `matplotlib_master_cheatsheet.ipynb` | Matplotlib | 24 |
| `seaborn_master_cheatsheet.ipynb` | Seaborn | 17 |
| `plotly_master_cheatsheet.ipynb` | Plotly | 17 |
| `folium_master_cheatsheet.ipynb` | Folium | 32 |
| `streamlit_master_cheatsheet.ipynb` | Streamlit | 29 |

---

## 🔢 NumPy — `numpy_master_cheatsheet.ipynb`

Core numerical computing. Arrays, math, and memory.

1. Array Creation
2. Dtype & Type Casting
3. Array Attributes
4. Indexing & Slicing
5. Reshape / Flatten / Transpose
6. Adding Dimensions (newaxis / expand_dims)
7. Concatenate / Stack / Split
8. Tile & Repeat
9. Arithmetic & Math
10. Aggregation & Statistics
11. Logical & Comparison
12. Searching & Filtering
13. Sorting
14. Insert / Delete / Append
15. Clip / Round / NaN Handling
16. Broadcasting
17. Linear Algebra
18. Random Module
19. Vectorize & Apply Along Axis
20. Set Operations
21. Structured Arrays
22. String Operations
23. File I/O
24. Views vs Copies
25. Memory & Performance
26. Useful Utility Functions
27. Polynomial Operations
28. Quick Reference Cheat Card

---

## 🐼 Pandas — `pandas_master_cheatsheet.ipynb`

Data manipulation and analysis — the everyday workhorse.

1. Series Creation
2. DataFrame Creation
3. Basic Info & Inspection
4. Selection — loc / iloc / at / iat
5. Filtering & Query
6. Add / Modify / Delete Columns & Rows
7. Rename / Reindex / Reorder
8. Dtype Conversion
9. Null / Missing Value Handling
10. Sorting
11. GroupBy — Full Guide
12. Merge / Join
13. Concat / Append
14. Apply / Map / Applymap
15. String Operations (str accessor)
16. Datetime Operations (dt accessor)
17. Duplicates
18. Pivot Table / Crosstab / Melt / Wide_to_Long
19. Window Functions (Rolling / Expanding / EWM)
20. Multi-Index (Hierarchical Index)
21. Categorical Data
22. Value Counts & Frequency
23. Index Operations
24. File I/O
25. Chaining & Assign Pattern
26. Performance Tips
27. Useful Utilities
28. Quick Reference Cheat Card

---

## 📊 Matplotlib — `matplotlib_master_cheatsheet.ipynb`

The foundation of Python plotting. Full control over every pixel.

1. Basic Plots
2. Line Plot Options
3. Scatter Plot Options
4. Bar Plot Options
5. Histogram Options
6. Pie Chart Options
7. Figure & Axes — OOP Style (Recommended)
8. Subplots — All Patterns
9. Title / Labels / Ticks / Legend
10. Grid & Spines
11. Annotation & Text
12. Scales & Limits
13. Styles & Themes
14. Colormaps
15. Imshow & Heatmap
16. Contour Plots
17. Error Bars
18. Fill Between & Bands
19. 3D Plots
20. Patches & Shapes
21. Colorbar & Inset Axes
22. Animation
23. Save Figure Options
24. Quick Reference Cheat Card

---

## 🌊 Seaborn — `seaborn_master_cheatsheet.ipynb`

Statistical visualization built on Matplotlib with a high-level API.

1. Themes & Styles
2. Color Palettes
3. Relational Plots — lineplot / scatterplot / relplot
4. Distribution Plots
5. Categorical Plots
6. Regression Plots
7. Matrix Plots — heatmap / clustermap
8. Pairplot & PairGrid
9. FacetGrid
10. Jointplot & JointGrid
11. Customization — Titles, Labels, Legends
12. Ordering, Orient, hue_order, order
13. Axes-Level vs Figure-Level
14. Overlaying Plots
15. Object Interface (Seaborn v0.12+)
16. Save & Export
17. Quick Reference Cheat Card

---

## 📈 Plotly — `plotly_master_cheatsheet.ipynb`

Interactive charts for the browser. Covers both high-level Express and low-level Graph Objects.

1. Plotly Express — Line / Scatter / Area
2. Bar Plots
3. Distribution Plots
4. Categorical & Statistical Plots
5. Heatmap & Matrix
6. Map & Geo Plots
7. 3D Plots
8. Graph Objects (go) — Low Level
9. Subplots
10. update_layout — Full Customization
11. update_traces — Styling Traces
12. Annotations, Shapes & Images
13. Animation
14. Facets (col / row / facet_col_wrap)
15. Themes & Templates
16. Export & Save
17. Quick Reference Cheat Card

---

## 🗺️ Folium — `folium_master_cheatsheet.ipynb`

Interactive Leaflet.js maps from Python. The most complete section in the collection.

1. Basic Map
2. Tile Styles
3. Marker
4. Custom Icon Marker
5. DivIcon (Custom HTML/CSS Icon)
6. BeautifyIcon (Fancier Markers)
7. Multiple Markers (Loop)
8. Markers from DataFrame
9. Circle & CircleMarker
10. Polyline (Path)
11. AntPath (Animated Route)
12. Polygon
13. Rectangle
14. Popup — HTML & IFrame
15. Tooltip
16. Marker Cluster
17. Heatmap
18. GeoJSON
19. GeoJSON — Custom Style Function
20. Choropleth
21. Layer Control (Toggle Layers)
22. Fit Bounds (Auto-zoom to Markers)
23. LatLng Popup (Click to Show Coordinates)
24. Mouse Position (Live Coordinates on Hover)
25. Mini Map
26. Fullscreen Button
27. Measure Tool
28. Search Plugin (Searchable Markers)
29. Float Image (Logo/Legend Overlay)
30. Timestamped GeoJSON (Animated Time Series)
31. Save — HTML File
32. Save — BytesIO (for Streamlit / Flask)

---

## ⚡ Streamlit — `streamlit_master_cheatsheet.ipynb`

Build and deploy data web apps in pure Python.

> Run any script with: `streamlit run app.py`

1. Page Config (Always First)
2. Basic Text
3. Data Display
4. Metrics
5. Input Widgets
6. Select Widgets
7. Sliders
8. Button & Checkbox
9. File Upload & Download
10. Sidebar
11. Layout — Columns
12. Layout — Tabs
13. Layout — Expander & Container
14. Native Charts
15. Plotly Charts
16. Matplotlib & Altair Charts
17. Images, Video & Audio
18. Status Messages
19. Progress & Spinner
20. Session State
21. Caching
22. Forms (Batch Inputs, Single Submit)
23. Callbacks (on_change / on_click)
24. Multipage Apps
25. Chat Interface
26. Custom CSS & HTML
27. Folium Map in Streamlit
28. Theming (config.toml)
29. Deployment Tips

---

## ⚙️ Setup

Install all libraries at once:

```bash
pip install numpy pandas matplotlib seaborn plotly folium streamlit
```

Optional extras used in the notebooks:

```bash
pip install altair streamlit-folium openpyxl xlrd
```

Run Jupyter:

```bash
jupyter notebook
# or
jupyter lab
```

---

## 🔗 How the Libraries Fit Together

```
NumPy          →  foundation (arrays, math)
  └─ Pandas    →  tabular data (DataFrames)
       ├─ Matplotlib  →  static plots (full control)
       │    └─ Seaborn  →  statistical plots (high-level)
       ├─ Plotly        →  interactive charts (browser)
       ├─ Folium        →  interactive maps (Leaflet.js)
       └─ Streamlit     →  web app shell (deploys everything above)
```
