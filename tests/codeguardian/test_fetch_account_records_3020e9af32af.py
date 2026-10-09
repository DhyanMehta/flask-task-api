import os, sqlite3, tempfile
from src.services.billing import fetch_account_records

def test_fetch_account_records():
    # Setup temporary SQLite database
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        db_path = tf.name
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance REAL, status TEXT)")
        # Insert sample rows
        cur.executemany(
            "INSERT INTO accounts (balance, status) VALUES (?, ?)",
            [
                (150.0, 'active'),
                (50.0, 'active'),
                (200.0, 'inactive'),
            ],
        )
        conn.commit()
        conn.close()
        # Call the function under test
        result = fetch_account_records(db_path, status_filter='active', min_balance=100.0)
        # Verify only the matching record is returned
        assert isinstance(result, list)
        assert len(result) == 1
        record = result[0]
        assert record['status'] == 'active'
        assert record['balance'] >= 100.0
    finally:
        os.unlink(db_path)
