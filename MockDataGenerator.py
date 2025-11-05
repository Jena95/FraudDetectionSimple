import csv
import random
from datetime import datetime, timedelta

def generate_card_number():
    """Generate a fake 16-digit card number grouped in 4s."""
    return '-'.join(''.join(str(random.randint(0, 9)) for _ in range(4)) for _ in range(4))

def generate_transaction_data(num_records=1000, start_date="2025-10-01"):
    """Generate fake bank transaction data."""
    records = []
    start = datetime.fromisoformat(start_date)
    merchants = ["Amazon", "Starbucks", "Uber", "Apple", "Walmart", "HSBC", "Netflix", "Shell", "Costco", "Nike"]
    locations = ["London", "New York", "Singapore", "Paris", "Toronto", "Hong Kong"]

    for i in range(1, num_records + 1):
        txn_time = start + timedelta(minutes=random.randint(0, 60*24*30))  # within ~1 month
        amount = round(random.uniform(5, 10000), 2)  # range £5–£10,000
        record = {
            "txn_id": i,
            "card": generate_card_number(),
            "amount": amount,
            "ts": txn_time.isoformat(),
            "merchant": random.choice(merchants),
            "location": random.choice(locations)
        }
        records.append(record)
    return records

def write_to_csv(records, filename="transactions.csv"):
    """Write generated records to CSV."""
    fieldnames = ["txn_id", "card", "amount", "ts", "merchant", "location"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"✅ Wrote {len(records)} transactions to {filename}")

if __name__ == "__main__":
    data = generate_transaction_data(num_records=1000)
    write_to_csv(data)
