CREATE TABLE shop(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    balance FLOAT NOT NULL
);

CREATE TABLE product(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    price FLOAT NOT NULL
);

CREATE TABLE warehouse(
    shop_id INT REFERENCES shop(id),
    product_id INT REFERENCES product(id),
    quantity INT NOT NULL
);

CREATE TABLE worker(
    worker_id INT PRIMARY KEY,
    shop_id INT REFERENCES product(id),
    name VARCHAR(255),
    salary INT NOT NULL,
    position VARCHAR(255)
);

INSERT INTO shop (id, name, balance) VALUES
(1, 'Перекресток', 50000.0),
(2, 'IKEA', 100000.0),
(3, '711', 75000.0);

INSERT INTO product (id, name, price) VALUES
(1, 'МЫЛО', 50.0),
(2, 'Паста', 300.0),
(3, 'Мясо', 200.0),
(4, 'Молоко', 80.0),
(5, 'Хлеб', 40.0),
(6, 'Чай', 150.0);

INSERT INTO warehouse (shop_id, product_id, quantity) VALUES
(1, 1, 100),
(1, 2, 50),
(1, 5, 200),
(2, 3, 80),
(2, 4, 120),
(3, 6, 90);

INSERT INTO worker (worker_id, shop_id, name, salary, position) VALUES
(1, 1, 'Иванов Иван', 40000, 'Продавец'),
(2, 1, 'Петрова Анна', 45000, 'Кассир'),
(3, 2, 'Сидоров Алексей', 50000, 'Менеджер'),
(4, 2, 'Кузнецова Ольга', 42000, 'Продавец'),
(5, 3, 'Васильев Дмитрий', 48000, 'Администратор'),
(6, 3, 'Смирнова Елена', 43000, 'Кассир');

SELECT worker_id, name, salary FROM worker ORDER BY salary DESC;
SELECT position, max(salary), sum(salary), avg(salary), min(salary), count(salary) FROM worker GROUP BY position;