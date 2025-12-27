
- Every data-analysis app is the same 5-block pipeline:

DATA → CLEAN → ANALYZE → VISUALIZE → REPORT

---

## 2️⃣ Define the Output FIRST

Before writing any code, answer in plain English:

> “When this program finishes, what exact charts and numbers do I want?”

If outputs are fuzzy, stop here.

---

## 3️⃣ Define the Canonical DataFrame (Your Contract)

You must define **one clean dataframe** that all code depends on.

### Example: `trades_df`

| column        | type      | meaning                          |
|--------------|-----------|----------------------------------|
| date         | datetime  | trade close date                 |
| symbol       | string    | instrument                       |
| entry_price  | float     | entry                            |
| exit_price   | float     | exit                             |
| size         | float     | position size                    |
| pnl          | float     | profit / loss                    |
| return_pct   | float     | normalized return                |

Nothing else exists until this dataframe exists and is clean.  
This is your **data contract**. Break it, the app breaks.

---

## 4️⃣ Build the Project Like Lego (Not One Script)

Structure is not optional:

project/
│
├── data/
│ └── trades.csv
├── load_data.py
├── clean_data.py
├── metrics.py
├── plots.py
└── main.py

---

**Rule:** Each file does **one job only**.

## 5️⃣ Implement Step by Step

### A) Load Data (No Logic, No Cleaning)
### B) Clean Data (Create Canonical DF)
### C) Metrics (Numbers Only)
### D) Visualization (Zero Math)

### E) main.py = Glue Only (Boring Is Good)
```python
from load_data import load_trades
from clean_data import clean_trades
from metrics import win_rate, equity_curve, max_drawdown
from plots import plot_equity

df = load_trades("data/trades.csv")
df = clean_trades(df)

equity = equity_curve(df)

print("Win rate:", win_rate(df))
print("Max drawdown:", max_drawdown(equity))

plot_equity(equity)
```

---

## 6️⃣ Golden Rules

- **Confusion = functions are too big**  
- **One function → one responsibility**  
- **Data first, visuals last**  
- **Clean dataframe is everything**  
- **Boring code = correct code**  

## 7️⃣ How to Use This Template

For every new project:

1. Write outputs in English  
2. Define canonical dataframe  
3. Create folder structure  
4. Implement: `load → clean → metrics → plots`  
5. Glue it together in `main.py`  
6. Only then optimize or beautify  

## 8️⃣ Next Evolutions

- Add unit tests for metrics  
- Turn `main.py` into Streamlit dashboard  
- Save reports to HTML/PDF  
- Build a reusable analytics library  
- Add YAML/JSON configuration  

