import hashlib, random
import sqlite3
import signal
import sys

conn = sqlite3.connect('proof.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS proofs (proof text)')
c.execute('SELECT COUNT(*) FROM proofs')
print(c.fetchone(), ' proofs saved in db')
conn.commit()

def signal_handler(sig, frame):
    conn.close()
    print('Database connection closed')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while True:
    proof = ''
    hashFound = False
    while not hashFound:
        proof = ''.join([random.choice('h25io') for _ in range(30)])
        if hashlib.sha256(('h25'+proof).encode()).hexdigest().startswith('00000'):
            hashFound = True
    c.execute('INSERT INTO proofs VALUES(?)', (proof,))
    conn.commit()
    print('New proof saved ', proof)
