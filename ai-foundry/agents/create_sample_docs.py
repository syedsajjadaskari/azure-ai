# create_sample_docs.py
import os

# Create a data folder
os.makedirs("data", exist_ok=True)

# Product documentation
products = {
    "product_1.md": """
# TrailMaster X4 Tent

## Overview
The TrailMaster X4 is a premium 4-person tent designed for all-season camping.

## Specifications
- Capacity: 4 people
- Weight: 8.5 lbs
- Dimensions: 8ft x 8ft x 6ft (height)
- Waterproof rating: 3000mm
- Setup time: 5-7 minutes

## Features
- Double-wall construction for ventilation
- Aluminum poles for lightweight durability
- Full rain fly included
- Multiple storage pockets
- Easy setup with color-coded poles

## Price
$299.99
""",
    
    "product_2.md": """
# SummitPro Hiking Backpack

## Overview
Professional-grade 65L hiking backpack for multi-day adventures.

## Specifications
- Capacity: 65 liters
- Weight: 4.2 lbs
- Load capacity: Up to 50 lbs
- Dimensions: 30" x 14" x 10"

## Features
- Adjustable suspension system
- Integrated rain cover
- Multiple compartments
- Hydration bladder compatible
- Hip belt with pockets
- Ventilated back panel

## Price
$189.99
""",
    
    "product_3.md": """
# Alpine Chef Camp Stove

## Overview
Compact and efficient propane camp stove for outdoor cooking.

## Specifications
- BTU Output: 10,000 BTU
- Weight: 2.5 lbs
- Fuel: Propane canister
- Boil time: 4 minutes (1 liter)

## Features
- Wind-resistant burner
- Adjustable flame control
- Piezo ignition
- Folds flat for storage
- Compatible with standard cookware

## Price
$79.99
"""
}

for filename, content in products.items():
    with open(f"data/{filename}", "w") as f:
        f.write(content)

print("✓ Created 3 sample product documents in ./data/")