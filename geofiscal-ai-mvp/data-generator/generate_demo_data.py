import argparse, csv, os, random
from datetime import datetime, timedelta


def main(records: int, output: str):
    os.makedirs(output, exist_ok=True)
    path = os.path.join(output, 'transactions.csv')
    start = datetime(2024, 4, 1)
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['txn_id', 'district', 'project_id', 'vendor_id', 'budget', 'spent', 'date', 'anomaly'])
        for i in range(records):
            budget = random.randint(10000, 2500000)
            spent = int(budget * random.uniform(0.6, 1.6))
            anomaly = 1 if random.random() < 0.04 or spent > budget * 1.3 else 0
            w.writerow([i + 1, f'DIST-{random.randint(1, 780):03}', f'PRJ-{random.randint(1, 5000):05}', f'VEN-{random.randint(1, 15000):05}', budget, spent, (start + timedelta(days=random.randint(0, 730))).date().isoformat(), anomaly])
    print(f'Generated {records} rows at {path}')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--records', type=int, default=100000)
    p.add_argument('--output', type=str, default='./out')
    a = p.parse_args()
    main(a.records, a.output)
