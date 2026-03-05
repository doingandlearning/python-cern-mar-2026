# NumPy, Pandas, Matplotlib & Lambdas — Teaching Script and Notes

**Audience:** CERN engineers, new to Python  
**Duration:** 60–70 minutes (core) + optional lambdas section (~15–20 min)  
**Data:** `code_samples/movies.csv` (Title, Year, Director, Genre, Revenue)

---

## Part 1: Core Walkthrough (60–70 min)

### 0–10 min — Framing and setup

**You say:** "We're going to look at three libraries you'll use again and again: **NumPy** (fast arrays and vector maths), **pandas** (tables and data wrangling), and **matplotlib** (plotting). We'll start from plain Python lists, then see how these tools make the same jobs shorter and faster."

**On screen:**

```python
# Plain Python
math_scores = [85, 92, 78, 88, 95]
science_scores = [90, 88, 85, 92, 89]

bonus_math = []
for score in math_scores:
    bonus_math.append(score + 5)

avg_math = sum(math_scores) / len(math_scores)
print("Math scores:", math_scores)
print("Math + 5 bonus:", bonus_math)
print("Average math:", avg_math)
```

**Talking points:** Lists and loops are explicit but verbose. Ask: "How would you add these two lists elementwise?" Then show:

```python
total_scores = []
for i in range(len(math_scores)):
    total_scores.append(math_scores[i] + science_scores[i])
print("Total scores:", total_scores)
```

Transition: "NumPy gives us a vectorised way to do this — same idea, less code, much faster on big arrays."

---

### 10–25 min — NumPy basics

**Live-code:**

```python
import numpy as np

math_scores_np = np.array(math_scores)
science_scores_np = np.array(science_scores)

print("math_scores_np:", math_scores_np)
print("Type:", type(math_scores_np))

math_scores_with_bonus = math_scores_np + 5   # vector maths
print("Math + 5 (NumPy):", math_scores_with_bonus)

print("Elementwise sum:", math_scores_np + science_scores_np)
print("Mean math score:", math_scores_np.mean())
```

**Explain:** `np.array` turns a list into a fixed-type numeric array. Arithmetic is elementwise; no loop in your code. Ask: "What would you change to get the average science score?" → `science_scores_np.mean()`.

**Then:**

```python
numbers = np.linspace(0, 100, 17)   # 17 evenly spaced points
print("Linspace 0–100, 17 points:", numbers)

print("Std dev of math scores:", np.std(math_scores_np))
```

**Teaching notes:** Emphasise "vector operations" and "built-in stats." Don't go deep into linear algebra yet — just "NumPy is your vector/matrix workhorse."

---

### 25–50 min — Pandas: tabular data with the movies CSV

**On screen:**

```python
import pandas as pd

df = pd.read_csv("code_samples/movies.csv")
```

Briefly show the CSV columns (Title, Year, Director, Genre, Revenue).

**Live-code:**

```python
print("Head:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nRandom sample:")
print(df.sample(5))

print("\nDescribe (numeric columns):")
print(df.describe())
```

**Talking points:** A **DataFrame** is a table (rows × columns). `head`, `tail`, `sample` for quick inspection; `describe()` gives count, mean, std, min, max for numeric columns.

**Column as a whole:**

```python
df["years_since_release"] = 2026 - df["Year"]
print(df[["Title", "Year", "years_since_release"]].head())
```

**Filtering:**

```python
print("\nMovies before 2000:")
print(df[df["Year"] < 2000][["Title", "Year"]])

# Optional: "What if we want only Sci-Fi before 2000?"
old_scifi = df[(df["Year"] < 2000) & (df["Genre"] == "Sci-Fi")]
print(old_scifi[["Title", "Year", "Genre"]])
```

**Genre counts:**

```python
genre_counts = df["Genre"].value_counts()
print("\nGenre counts:")
print(genre_counts)
```

**Teaching notes:** Boolean masks: `(condition1) & (condition2)`. `value_counts()` is your friend for categorical columns.

---

### 50–65 min — Matplotlib: quick visualisation

**Live-code:**

```python
import matplotlib.pyplot as plt

plt.figure()
genre_counts.plot(kind="pie")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Number of Movies by Genre")
plt.tight_layout()
plt.show()
```

**Explain:** Pandas hooks into matplotlib; `Series.plot(kind="pie")` builds the chart. We still use `plt.figure()`, `plt.title()`, `plt.show()`.

**Optional — bar chart:**

```python
plt.figure()
genre_counts.plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Number of Movies by Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Optional — bridge to NumPy:** Extract a column as a NumPy array:

```python
revenues = df["Revenue"].to_numpy()
print("Average revenue (NumPy):", revenues.mean())
print("Std revenue (NumPy):", np.std(revenues))
```

**Talking point:** Pandas for structure and labels; NumPy for raw numerics when you need it.

---

### 65–70 min — Wrap-up and Q&A

**Summarise:** NumPy = arrays and vector maths; pandas = DataFrames, `read_csv`, filtering, `value_counts`; matplotlib = quick plots from Series/DataFrame.

**Reflection:** "Think of one dataset you see at CERN — logs, sensor readings, Run Registry. Where would NumPy fit? Where would pandas? Where would you want a quick plot?"

---

## Part 2: Lambdas in Pandas (optional, ~15–20 min)

**You say:** "Pandas has several places where you pass a small function — often a **lambda**. Lambdas are handy, but for simple operations there's usually a faster, clearer **vectorised** alternative. We'll see both."

### 1. Series: `map` and `apply` (one value → one value)

**Lambda version:**

```python
# Clean a string column: strip and lower
df["genre_clean"] = df["Genre"].astype(str).map(lambda s: s.strip().lower())
print(df[["Genre", "genre_clean"]].head())

# Years since release (with NaN check)
df["years_since_release_apply"] = df["Year"].apply(lambda y: 2026 - y if pd.notna(y) else np.nan)
```

**Better when possible — vectorised (no lambda):**

```python
df["years_since_release"] = 2026 - df["Year"]   # whole column at once
```

**Teaching point:** For numeric column ops, try the vector form first; use `apply`/`map` when you need custom logic or string methods that don't have a built-in `.str` method.

### 2. Row-wise `apply` (axis=1) — often a "smell"

**Lambda (row by row):**

```python
# Only if you have Rating and Revenue
df["weighted_score_row"] = df.apply(
    lambda row: row["Rating"] * 0.7 + row["Revenue"] * 0.3
    if pd.notna(row["Rating"]) and pd.notna(row["Revenue"]) else np.nan,
    axis=1
)
```

**Better — vectorised:**

```python
df["weighted_score"] = df["Rating"] * 0.7 + df["Revenue"] * 0.3
```

**Teaching point:** Row-wise `apply` is flexible but slow on large data. Prefer column-wise operations when you can.

### 3. `assign` with lambdas — tidy pipelines

**Pattern:** `assign` can take a lambda that receives the current DataFrame and returns a Series; good for adding several derived columns in one chain.

```python
df2 = (
    df
    .assign(
        years_since_release=lambda d: 2026 - d["Year"],
        decade=lambda d: (d["Year"] // 10 * 10).astype("Int64"),
    )
)
print(df2[["Year", "years_since_release", "decade"]].head())
```

**Teaching point:** The lambda receives the DataFrame at that stage of the pipeline (e.g. `d`), so you can use existing columns to build new ones.

### 4. `filter` — pick columns by name (lambda on column names)

```python
# Columns whose name contains "year", "rating", or "revenue"
subset = df.filter(lambda col: any(k in col.lower() for k in ["year", "rating", "revenue"]))
print("Filtered columns:", list(subset.columns))
```

**Teaching point:** Here the lambda operates on **column names**, not on the data. Useful for selecting columns by pattern.

### 5. `groupby` + `agg` with a lambda (custom aggregate)

```python
df["decade"] = (df["Year"] // 10 * 10).astype("Int64")

summary = (
    df.dropna(subset=["decade"])
    .groupby(["Genre", "decade"], dropna=False)
    .agg(
        movies=("Year", "count"),
        earliest=("Year", "min"),
        latest=("Year", "max"),
        modern_share=("Year", lambda s: (s >= 2000).mean()),   # custom agg
    )
    .reset_index()
)
print(summary.head(10))
```

**Teaching point:** The lambda receives a **Series** (one column per group). You return a single value (e.g. proportion of years >= 2000). Named aggs make the output columns clear.

### 6. `groupby` + `transform` (group-level stat back onto each row)

```python
df["genre_avg_year"] = df.groupby("Genre")["Year"].transform(lambda s: s.mean())
df["year_minus_genre_avg"] = df["Year"] - df["genre_avg_year"]
print(df[["Genre", "Year", "genre_avg_year", "year_minus_genre_avg"]].head())
```

**Teaching point:** `transform` returns a Series **same length as the original** (value repeated for each row in the group). Use it when you want "group statistic on every row."

### 7. `sort_values(..., key=lambda ...)` — sort by a transformed column

```python
# Sort titles case-insensitively
df_sorted = df.sort_values(by="Title", key=lambda s: s.astype(str).str.lower())
print(df_sorted[["Title"]].head())
```

**Teaching point:** `key` receives the Series you're sorting by; return a Series of the same length (the values to sort on). Very useful for custom sort orders.

### 8. `pipe` with lambdas — chain steps

```python
def top_n_by_col(d, col, n=10):
    return d.sort_values(col, ascending=False).head(n)

top_revenue = (
    df
    .pipe(lambda d: d.dropna(subset=["Revenue"]))
    .pipe(lambda d: top_n_by_col(d, "Revenue", n=10))
)
print(top_revenue[["Title", "Revenue"]].head())
```

**Teaching point:** `pipe` passes the DataFrame through a function (often a lambda). Good for readability when you have a sequence of steps.

### 9. Rolling / expanding with `apply`

```python
df_year = df.dropna(subset=["Year"]).sort_values("Year")
df_year["rolling_count_5"] = df_year["Year"].rolling(5).apply(lambda s: s.count(), raw=False)
print(df_year[["Year", "rolling_count_5"]].head(10))
```

**Teaching point:** The lambda gets a window of values; you return one number per window. For simple stats (e.g. mean), often there's a built-in: `rolling(5).mean()`.

### 10. Lambda "smells" — when to avoid

| Smell | Better (vectorised) |
|--------|----------------------|
| `df.apply(lambda r: str(r["Title"]).strip().title(), axis=1)` | `df["Title"].astype(str).str.strip().str.title()` |
| `df["Rating"].apply(lambda x: x + 1)` | `df["Rating"] + 1` |
| Row-wise numeric combo when columns exist | Column ops: `df["A"] * 0.7 + df["B"] * 0.3` |

**Teaching point:** If the lambda is doing a simple string or numeric operation, check whether `.str` or direct column arithmetic already does it. Use lambdas when you need custom logic, custom aggregates, or selection by name.

---

## Instructor cheat-sheet (copy-paste blocks)

### NumPy

```python
import numpy as np

math_scores = [85, 92, 78, 88, 95]
science_scores = [90, 88, 85, 92, 89]

math_scores_np = np.array(math_scores)
science_scores_np = np.array(science_scores)

math_scores_with_bonus = math_scores_np + 5
print(math_scores_np.mean())
print(math_scores_np + science_scores_np)

numbers = np.linspace(0, 100, 17)
print(np.std(math_scores_np))
```

### Pandas + Matplotlib (core)

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("code_samples/movies.csv")

print(df.head())
print(df.tail())
print(df.sample(5))
print(df.describe())

df["years_since_release"] = 2026 - df["Year"]
print(df[df["Year"] < 2000])

genre_counts = df["Genre"].value_counts()
print(genre_counts)

plt.figure()
genre_counts.plot(kind="pie")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Number of Movies by Genre")
plt.tight_layout()
plt.show()
```

### Lambdas in pandas (highlights)

```python
# map on Series
df["genre_clean"] = df["Genre"].astype(str).map(lambda s: s.strip().lower())

# assign with lambda (pipeline)
df2 = df.assign(years_since_release=lambda d: 2026 - d["Year"])

# groupby + custom agg
summary = df.groupby("Genre").agg(modern_share=("Year", lambda s: (s >= 2000).mean()))

# sort by key
df_sorted = df.sort_values(by="Title", key=lambda s: s.astype(str).str.lower())

# Better than lambda when possible:
df["clean_title"] = df["Title"].astype(str).str.strip().str.title()
df["rating_plus_one"] = df["Rating"] + 1
```

---

## File reference

- **Data:** `code_samples/movies.csv` (Title, Year, Director, Genre, Revenue)
- **Extended pandas/lambda demos:** `alt_labs/pandas.py`
