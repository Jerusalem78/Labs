
CREATE TABLE groups (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE student_marks (
    student_id INT,
    math_mark_average FLOAT,
    physics_mark_average FLOAT,
    python_mark_average FLOAT,
    FOREIGN KEY (student_id) REFERENCES student(id)
);

INSERT INTO groups (id, name, description) VALUES
(1, 'Group A', 'Mathematics and Physics'),
(2, 'Group B', 'Computer Science and Python');

INSERT INTO student (id, name, group_id) VALUES
(1, 'John Doe', 1),
(2, 'Jane Smith', 1),
(3, 'Alice Johnson', 2),
(4, 'Bob Brown', 2);

INSERT INTO student_marks (student_id, math_mark_average, physics_mark_average, python_mark_average) VALUES
(1, 85.5, 90.0, NULL),
(2, 78.0, 88.5, NULL),
(3, NULL, NULL, 92.0),
(4, NULL, NULL, 87.5);


SELECT * FROM groups WHERE name='Group A'

# id |  name   |       description
# ----+---------+-------------------------
#  1 | Group A | Mathematics and Physics

SELECT * FROM student WHERE id=1;

# id |   name   | group_id
# ----+----------+----------
#  1 | John Doe |        1

SELECT * FROM student_marks WHERE student_id=1;
# student_id | math_mark_average | physics_mark_average | python_mark_average
# ------------+-------------------+----------------------+---------------------
#          1 |              85.5 |                   90 |