-- Auto-generated schema: gymors
CREATE TABLE IF NOT EXISTS gymors (
  id SERIAL PRIMARY KEY,
  czim BOOLEAN,
  gyym VARCHAR(255),
  ofvr DECIMAL(10,2),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_gymors_created ON gymors(created_at);

-- Sample query
SELECT * FROM gymors WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;