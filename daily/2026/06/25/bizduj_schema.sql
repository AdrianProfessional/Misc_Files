-- Auto-generated schema: vecmzs
CREATE TABLE IF NOT EXISTS vecmzs (
  id SERIAL PRIMARY KEY,
  ljfs DECIMAL(10,2),
  mcqq VARCHAR(255),
  cija TEXT,
  nmuf INT,
  ulsx TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_vecmzs_created ON vecmzs(created_at);

-- Sample query
SELECT * FROM vecmzs WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;