CREATE TABLE users(
    user_id serial  PRIMARY KEY,
    user_login text NOT NULL,
    user_password text NOT NULL,
    user_name text NOT NULL,
    user_surname text NOT NULL,
    user_middle_name text DEFAULT NULL,
    user_role text NOT NULL DEFAULT 'user'
);

