import sys
import pandas as pd

try:
    from leblanc import (
        Agribusiness, 
        Tech, 
        Food, 
        Apparel, 
        Financial, 
        HealthBeauty, 
        Forestry
    )
    print("[OK] Library 'leblanc' imported successfully!\n")
except ImportError as e:
    print(f"[ERROR] Critical Error: Could not import 'leblanc'.")
    print(f"Detail: {e}")
    print("HINT: Did you run 'pip install -e .' in your virtual environment?")
    sys.exit(1)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def run_test_for_module(generator_class, name, target_col_for_nan):
    print(f"{'='*60}")
    print(f"[TEST] TESTING MODULE: {name}")
    print(f"{'='*60}")

    try:
        print(f"-> Generating records in English (en_US)...")
        generator = generator_class(num_records=10, locale='en_US')
        print(f"-> Testing .build() with fault injection in '{target_col_for_nan}'...")
        df = generator.build(missing_data_cols=[target_col_for_nan])

        if df.empty:
            raise ValueError("The returned DataFrame is empty!")
        
        null_count = df[target_col_for_nan].isnull().sum()
        
        print(f"[OK] Success! {len(df)} rows generated.")
        print(f"[OK] Translation OK (Check visually below).")
        print(f"[OK] Missing Values: {null_count} found in the target column.")
        print("\n[DATA] Data Sample:")
        print(df.head(3))
        print("\n")
        
        return True

    except Exception as e:
        print(f"[FAIL] FAILURE in module {name}.")
        print(f"Error: {e}")
        return False

MODULES_TO_TEST = [
    (Agribusiness, "Agribusiness", "total_revenue"),
    (Tech,         "Tech Sales",   "total_sale"),
    (Food,         "Food & Bev",   "customer_name"),
    (Apparel,      "Apparel",      "return_flag"),
    (Financial,    "Financial",    "contracted_value"),
    (HealthBeauty, "Health/Beauty","sales_channel"),
    (Forestry,     "Forestry",     "estimated_revenue"),
]

if __name__ == "__main__":
    print(">>> Starting Contributor Test Suite (v0.8.0)...\n")
    
    failures = []
    
    for cls, name, nan_col in MODULES_TO_TEST:
        success = run_test_for_module(cls, name, nan_col)
        if not success:
            failures.append(name)
    
    print(f"{'='*60}")
    if failures:
        print(f"[!] TESTS FAILED in the following modules: {failures}")
        sys.exit(1)
    else:
        print("[SUCCESS] ALL MODULES PASSED THE TESTS!")
        sys.exit(0)