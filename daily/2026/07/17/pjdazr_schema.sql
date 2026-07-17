-- Auto-generated schema: hzpmls
CREATE TABLE IF NOT EXISTS hzpmls (
  id SERIAL PRIMARY KEY,
  vriv BOOLEAN,
  xlpv TIMESTAMP,
  msde INT,
  shec DECIMAL(10,2),
  hmcp VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_hzpmls_created ON hzpmls(created_at);

-- Sample query
SELECT * FROM hzpmls WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;