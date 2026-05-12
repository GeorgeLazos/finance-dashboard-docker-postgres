-- Project template — no changes

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email) VALUES
('alice_admin', 'alice@coinsafe.local'),
('bob_trader', 'bob@coinsafe.local');

INSERT INTO transactions (user_id, amount, transaction_type) VALUES
(1, 5000.00, 'deposit'),
(2, 150.50, 'withdrawal'),
(1, 1200.00, 'transfer');
