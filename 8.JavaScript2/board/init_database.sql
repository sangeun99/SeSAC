DROP TABLE IF EXISTS board;

CREATE TABLE board(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  message VARCHAR(200)
)
