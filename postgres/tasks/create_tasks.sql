CREATE TABLE tasks(
    task_id serial PRIMARY KEY,
    task_name text NOT NULL,
    task_type text NOT NULL DEFAULT 'single'
);