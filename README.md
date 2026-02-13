<!-- Badge will work after first workflow run -->
[![Python PEP-8 Check](https://github.com/ReneGV/A01796919-testing-activity-5-2/actions/workflows/python-lint.yml/badge.svg?branch=main)](https://github.com/ReneGV/A01796919-testing-activity-5-2/actions/workflows/python-lint.yml)

## How to Run the Program

### Test Case 1 - Standard Sales Data
```bash
python3 computeSales.py data/TC1/TC1.ProductList.json data/TC1/TC1.Sales.json
```
**Expected Result:** $2,481.86

![Test Case 1 Result](data/test-case-1-result.png)

---

### Test Case 2 - Large Quantities with Negative Values
```bash
python3 computeSales.py data/TC1/TC1.ProductList.json data/TC2/TC2.Sales.json
```
**Expected Result:** $166,568.23

![Test Case 2 Result](data/test-case-2-result.png)

---

### Test Case 3 - Invalid Products
```bash
python3 computeSales.py data/TC1/TC1.ProductList.json data/TC3/TC3.Sales.json
```
**Expected Result:** $165,235.37

![Test Case 3 Result](data/test-case-3-result.png)

---

## Output

Results are displayed on screen and saved to `SalesResults.txt`

## Code Quality Checks

### Flake8 (PEP-8 Compliance)
```bash
source venv/bin/activate
flake8 computeSales.py
```

![Flake8 Results](flake8-run.png)

**Status:** ✅ PASS (No issues found)

### Pylint (Code Analysis)
```bash
pylint computeSales.py
```

![Pylint Results](pylint-run.png)

**Score:** 10.00/10 ⭐
