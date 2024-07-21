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

SELECT * FROM tasks WHERE user_id = 1;

SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

INSERT INTO tasks (title, description, status_id, user_id) 
VALUES ('New task', 'New tasks discription', (SELECT id FROM status WHERE name = 'new'), 1);

SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

DELETE FROM tasks WHERE id = 1; 

SELECT * FROM users WHERE email LIKE '%@gmail.com';  

UPDATE users SET fullname = 'New name' WHERE id = 1; 

SELECT status.name, COUNT(tasks.id) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com'; 

SELECT * FROM tasks WHERE description IS NULL;

SELECT users.fullname, tasks.title
FROM users
JOIN tasks ON users.id = tasks.user_id
WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');

SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname;





