CREATE TABLE dorm_block(
    block_id int NOT NULL,
    dorm_id int NOT NULL,
    FOREIGN KEY(dorm_id) REFERENCES dorms(dorm_id) ON DELETE CASCADE,
    FOREIGN KEY(block_id) REFERENCES blocks(block_id) ON DELETE CASCADE
);