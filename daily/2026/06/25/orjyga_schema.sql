-- Auto-generated schema: cldujs
CREATE TABLE IF NOT EXISTS cldujs (
  id SERIAL PRIMARY KEY,
  szjm DECIMAL(10,2),
  onzc VARCHAR(255),
  hcxi BOOLEAN,
  ivwg TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_cldujs_created ON cldujs(created_at);

-- Sample query
SELECT * FROM cldujs WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;