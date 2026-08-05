# 1. Load Original Clean Dataset
import pandas as pd

df = pd.read_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\online_retail_sql_ready.csv"
)

print(df.shape)
print(df.head())

# 2. Select Important Columns
basket_data = df[
    ['InvoiceNo',
     'Description',
     'Quantity']
]

print(basket_data.head())

# 3. Create Product Matrix
# Step 1: Create Basket
basket = (
    basket_data
    .groupby(
        ['InvoiceNo',
         'Description']
    )['Quantity']
    .sum()
    .unstack()
    .fillna(0)
)

# Step 2: Check Shape and Type
print(basket.shape)
print(type(basket))

# Step 3: Convert to Binary
"""basket = basket.applymap(lambda x: 1 if x > 0 else 0) This code is not working in newer versions of Pandas (especially Python 3.14 environments), 
   applymap() may not be available or is deprecated for our DataFrame object. So instade of that we are using below code"""

basket = (basket > 0).astype(int)

print(basket.head())
print(basket.shape)

# 4. Install AI Library (pip install mlxtend)
from mlxtend.frequent_patterns import apriori

# 5. Generate Frequent Item sets
# Convert to Boolean
basket = basket.astype(bool)

frequent_items = apriori(
    basket,
    min_support=0.02,
    use_colnames=True
)

print(
    frequent_items
    .sort_values(
        'support',
        ascending=False
    )
    .head(20)
)

print(basket.dtypes)

# 6. Generate Association Rules (Now the AI starts making recommendations).
from mlxtend.frequent_patterns import association_rules

rules = association_rules(
    frequent_items,
    metric='lift',
    min_threshold=1
)

print(rules.head())

"""Important Metrics
Support
How common the combination is.

Confidence
Probability customer buys B after buying A.

Lift
Most important.
Lift > 1

means meaningful recommendation."""

# 7. Find Best Recommendations
top_rules = rules.sort_values(
    'lift',
    ascending=False
)

print(
    top_rules[
        [
            'antecedents',
            'consequents',
            'support',
            'confidence',
            'lift'
        ]
    ].head(20)
)

# 8. Build Recommendation Function
def recommend(product_name):

    recommendations = top_rules[
        top_rules['antecedents']
        .astype(str)
        .str.contains(product_name)
    ]

    return recommendations[
        [
            'consequents',
            'confidence',
            'lift'
        ]
    ].head(10)

# Check the output For example:
print(
    recommend('HEART OF WICKER SMALL')
)

# Convert frozenset columns to readable text
rules['Bought Product'] = rules['antecedents'].apply(
    lambda x: ', '.join(list(x))
)

rules['Recommended Product'] = rules['consequents'].apply(
    lambda x: ', '.join(list(x))
)

# Convert confidence to percentage
rules['Confidence (%)'] = (
    rules['confidence'] * 100
).round(2)

# Round lift value
rules['Lift'] = rules['lift'].round(2)

# Create final recommendation table
final_recommendations = rules[
    [
        'Bought Product',
        'Recommended Product',
        'Confidence (%)',
        'Lift'
    ]
].sort_values(
    by='Lift',
    ascending=False
).head(10)

# Display the result
print(final_recommendations.head(10))

# 9. Save Final Output
rules.to_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\product_recommendations.csv",
    index=False
)
print("Product Recommendation Completed")