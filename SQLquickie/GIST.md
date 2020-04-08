# SQL Commands
### Command to create the database:
```SQL
CREATE DATABASE kwitter
```

### Create the tables in the database:
Don't forget to `\c kwitter`
```SQL
CREATE TABLE twitteruser(
id SERIAL PRIMARY KEY,
display_name VARCHAR(40),
username VARCHAR(40),
password VARCHAR(40));

CREATE TABLE tweet(
id serial PRIMARY KEY,
twitteruser INTEGER REFERENCES twitteruser(id),
time_posted TIMESTAMP,
body VARCHAR(140));

CREATE TABLE notification(
id serial primary key,
twitteruser INTEGER REFERENCES twitteruser(id),
tweet INTEGER REFERENCES tweet(id),
viewed BOOLEAN DEFAULT FALSE);
```

Query to create a new user (username: steve, password: hunter2, display name: steve-o):
```SQL
INSERT INTO twitteruser(display_name, username, password) VALUES ('steve-o', 'steve', 'hunter2');
```


Query to create two new users at once:
```SQL
 INSERT INTO twitteruser(display_name, username, password)  
 VALUES  
 ('davey', 'dave', 'asdf'),  
 ('bobinator', 'bob', 'qwer');  
INSERT 0 2  
```


Query to get the username and password of twitteruser ID 1:
```SQL
SELECT (username, password) FROM twitteruser WHERE id=1;
```


Query to get the ID of a user by the username of dave:
```SQL
SELECT username FROM twitteruser WHERE username='dave';  
```


Query to create a new tweet written by the user with the username steve:
```SQL
INSERT INTO tweet(body, twitteruser)
VALUES(
    'fjdk;afsdk', (SELECT id FROM twitteruser WHERE username='steve')
);
```
Query to get the count of tweets by username steve
```SQL
SELECT count(twitteruser) FROM Tweet 
WHERE twitteruser=(
    SELECT id FROM Twitteruser WHERE username='steve'
);
```


Query to get the date and text of all tweets by username steve
```SQL
SELECT (time_posted, body) FROM tweet
where twitteruser=(
    SELECT id FROM twitteruser WHERE username='steve'
);
```


Query to get the username and password of the username bob
```SQL
SELECT (username, password) FROM twitteruser WHERE username='bob';
```

Query to create a notification for username bob using the tweet written by username steve
```SQL
INSERT INTO Notification(twitteruser, tweet, viewed)
VALUES
(
    (SELECT id FROM twitteruser WHERE username='bob'),
    (SELECT id FROM Tweet WHERE twitteruser=(
        SELECT id FROM twitteruser WHERE username='steve')
    ), 
    false
);
```

Query to get all IDs of notifications for bob
```SQL
SELECT id FROM Notification
WHERE twitteruser=(
    SELECT id FROM twitteruser WHERE username='bob'
);
```















