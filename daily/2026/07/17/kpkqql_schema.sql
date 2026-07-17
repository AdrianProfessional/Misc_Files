-- Auto-generated schema: zgdcqs
CREATE TABLE IF NOT EXISTS zgdcqs (
  id SERIAL PRIMARY KEY,
  aprn VARCHAR(255),
  jend TIMESTAMP,
  rssg TEXT,
  ywyg INT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_zgdcqs_created ON zgdcqs(created_at);

-- Sample query
SELECT * FROM zgdcqs WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;