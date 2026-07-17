-- Auto-generated schema: usajrs
CREATE TABLE IF NOT EXISTS usajrs (
  id SERIAL PRIMARY KEY,
  zpwp DECIMAL(10,2),
  tqqa VARCHAR(255),
  bovf TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_usajrs_created ON usajrs(created_at);

-- Sample query
SELECT * FROM usajrs WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;