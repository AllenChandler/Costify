import pandas as pd

# Conversion rates for weight units to grams
CONVERSIONS = {
    'oz': 28.3495,  # 1 oz to grams
    'g': 1.0,       # 1 g to grams
    'kg': 1000.0,   # 1 kg to grams
    'lb': 453.592,  # 1 lb to grams
}

def convert_to_grams(weight, unit):
    """Convert weight to grams based on unit."""
    return weight * CONVERSIONS.get(unit.lower(), 1)

def calculate_cost_and_price(csv_file, profit_margin):
    """Read CSV, calculate product cost and selling price per serving."""
    df = pd.read_csv(csv_file)

    # Normalize column headers (strip spaces and lowercase)
    df.columns = df.columns.str.strip().str.lower()

    # Convert ingredient weight to grams
    df['weight (g)'] = df.apply(lambda row: convert_to_grams(row['weight'], row['unit']), axis=1)

    # Calculate cost per gram
    df['cost per gram'] = df['price'] / df['weight (g)']

    # Calculate cost per serving
    df['cost per serving'] = df['cost per gram'] * df['serving size (g)']

    total_serving_cost = df['cost per serving'].sum()
    selling_price = total_serving_cost * (1 + profit_margin / 100)

    print("\nIngredient Cost Breakdown Per Serving:")
    print(df[['ingredient', 'serving size (g)', 'cost per serving']])
    print(f"\nTotal Cost per Serving: ${total_serving_cost:.2f}")
    print(f"Selling Price per Serving (with {profit_margin}% profit): ${selling_price:.2f}")

    return df, total_serving_cost, selling_price

# Example usage
csv_file = 'hydration.csv'  # Ensure CSV has the new Serving Size (g) column
profit_margin = 20  # Set desired profit percentage

df, total_serving_cost, selling_price = calculate_cost_and_price(csv_file, profit_margin)
