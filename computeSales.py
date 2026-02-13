#!/usr/bin/env python3
"""
computeSales.py - Sales Calculator Program

This program computes the total cost of all sales by reading
a product catalogue and sales records from JSON files.

Usage:
    python computeSales.py priceCatalogue.json salesRecord.json
"""

import sys
import json
import time


def load_json_file(filename):
    """Load and parse a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def build_price_catalogue(products):
    """
    Build a dictionary mapping product titles to their prices.

    Args:
        products: List of product dictionaries

    Returns:
        Dictionary with product titles as keys and prices as values
    """
    catalogue = {}
    for product in products:
        title = product['title']
        price = product['price']
        catalogue[title] = price
    return catalogue


def compute_sales_total(sales, catalogue):
    """
    Compute total cost of all sales.

    Negative quantities are treated as returns/refunds.

    Args:
        sales: List of sale records
        catalogue: Dictionary mapping product names to prices

    Returns:
        Tuple of (total_cost, valid_items_count)
    """
    total = 0.0
    valid_items = 0

    for sale in sales:
        product_name = sale['Product']
        quantity = sale['Quantity']

        # Skip if product not in catalogue
        if product_name not in catalogue:
            print(f"WARNING: Product '{product_name}' not found. Skipping.")
            continue

        # Calculate sale cost (negative quantities reduce total)
        price = catalogue[product_name]
        sale_cost = price * quantity
        total += sale_cost
        valid_items += 1

    return total, valid_items


def print_results(total, elapsed_time):
    """
    Print and save the sales results.

    Args:
        total: Total sales amount
        elapsed_time: Time elapsed in seconds
    """
    # Create formatted output
    separator = "=" * 70
    lines = []

    lines.append("")
    lines.append(separator)
    lines.append("SALES COMPUTATION RESULTS")
    lines.append(separator)
    lines.append("")
    lines.append(f"TOTAL SALES: ${total:,.2f}")
    lines.append("")
    lines.append(f"Execution time: {elapsed_time:.4f} seconds")
    lines.append(separator)
    lines.append("")

    output = "\n".join(lines)

    # Print to console
    print(output)

    # Save to file
    with open("SalesResults.txt", 'w') as file:
        file.write(output)

    print("\nResults saved to: SalesResults.txt")


def main():
    """Main program execution."""
    # Get file names from command line
    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    print("=" * 70)
    print("SALES COMPUTATION PROGRAM")
    print("=" * 70)
    print(f"\nPrice Catalogue: {catalogue_file}")
    print(f"Sales Records: {sales_file}")
    print("\nProcessing...\n")

    # Start timing
    start_time = time.time()

    # Load files
    products_data = load_json_file(catalogue_file)
    sales_data = load_json_file(sales_file)

    # Build catalogue
    catalogue = build_price_catalogue(products_data)
    print(f"Loaded {len(catalogue)} products")

    # Compute total
    total, valid_items = compute_sales_total(sales_data, catalogue)

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Display results
    print_results(total, elapsed_time, len(sales_data), valid_items)


if __name__ == "__main__":
    main()
