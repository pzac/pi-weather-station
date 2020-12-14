CREATE TABLE IF NOT EXISTS data(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  ext_temp INTEGER,
  brightness INTEGER,
  int_temp INTEGER,
  humidity INTEGER,
  pressure FLOAT,
  motion BOOLEAN
);

CREATE INDEX time_index ON data(time);
