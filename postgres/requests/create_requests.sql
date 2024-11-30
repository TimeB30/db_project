CREATE TABLE requests(
    request_id serial PRIMARY KEY,
    dorm_id int NOT NULL,
    block_id int NOT NULL,
    user_id int NOT NULL,
    status text NOT NULL DEFAULT 'created',
    date_time timestamp NOT NULL DEFAULT NOW(),
    FOREIGN KEY(dorm_id) REFERENCES dorms(dorm_id) ON DELETE CASCADE,
    FOREIGN KEY(block_id) REFERENCES blocks(block_id) ON DELETE CASCADE,
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);