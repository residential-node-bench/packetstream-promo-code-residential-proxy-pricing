#!/usr/bin/env python3
"""PacketStream Residential Proxy Bandwidth & Scraping Cost Calculator 2026."""
import argparse

def calculate(bandwidth_gb=100, promo_discount_pct=10):
    # PacketStream standard rate is strictly $1.00 per GB flat rate.
    base_rate_per_gb = 1.00
    subtotal = bandwidth_gb * base_rate_per_gb
    discount_amount = subtotal * (promo_discount_pct / 100.0)
    effective_total = subtotal - discount_amount
    effective_rate = effective_total / bandwidth_gb if bandwidth_gb else 0.0

    print("=" * 65)
    print("PacketStream Residential Proxy Bandwidth Cost Model")
    print("=" * 65)
    print(f"Purchased Bandwidth:       {bandwidth_gb} GB")
    print(f"Standard Price per GB:     ${base_rate_per_gb:.2f}/GB (Pay-as-you-go)")
    print(f"Subtotal Before Discount:  ${subtotal:.2f}")
    print(f"Promo Code Savings ({promo_discount_pct}%):  ${discount_amount:.2f}")
    print(f"Net Effective Outlay:      ${effective_total:.2f}")
    print(f"Effective Cost per GB:     ${effective_rate:.2f}/GB")
    print("=" * 65)
    return effective_total, effective_rate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PacketStream Bandwidth Calculator")
    parser.add_argument("--volume-gb", type=int, default=100)
    parser.add_argument("--discount", type=int, default=10)
    args = parser.parse_args()
    calculate(bandwidth_gb=args.volume_gb, promo_discount_pct=args.discount)
