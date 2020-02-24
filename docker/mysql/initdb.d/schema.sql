CREATE TABLE article (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    title VARCHAR(100),
    content VARCHAR(200),
    date DATE,
    PRIMARY KEY (id)
);

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    password VARCHAR(100),
    PRIMARY KEY (id)
);