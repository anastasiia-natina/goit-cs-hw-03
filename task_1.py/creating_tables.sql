CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    CONSTRAINT status_type_check CHECK (name IN ('new', 'in progress', 'completed'))
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL REFERENCES status(id),
    user_id INTEGER NOT NULL REFERENCES users(id)
);

ALTER TABLE tasks
    ADD CONSTRAINT fk_tasks_user_id_users_id
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE;