CREATE TABLE user_task(
    user_id int NOT NULL,
    task_id int NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user_block(user_id) ON DELETE CASCADE,
    FOREIGN KEY(task_id) REFERENCES tasks(task_id) ON DELETE CASCADE
);
