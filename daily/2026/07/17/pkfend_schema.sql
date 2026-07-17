-- Auto-generated schema: bkyozs
CREATE TABLE IF NOT EXISTS bkyozs (
  id SERIAL PRIMARY KEY,
  uaxz DECIMAL(10,2),
  qtfk TEXT,
  jmcb BOOLEAN,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_bkyozs_created ON bkyozs(created_at);

-- Sample query
SELECT * FROM bkyozs WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;