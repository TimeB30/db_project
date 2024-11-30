CREATE TABLE user_block(
    user_id int NOT NULL PRIMARY KEY,
    block_id int NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (block_id) REFERENCES blocks(block_id) ON DELETE CASCADE
);