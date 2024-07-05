CREATE DATABASE mindsdb;
USE mindsdb;
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_text TEXT,
    sentiment VARCHAR(10)
);

-- Insert example data
INSERT INTO reviews (review_text, sentiment) VALUES
('I love this product, it\'s fantastic!', 'positive'),
('This is the worst experience I\'ve ever had.', 'negative'),
('Quite decent, could be better.', 'neutral');
