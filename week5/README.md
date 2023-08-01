<!-- ## 要求二：建立資料庫和資料表
- 建立⼀個新的資料庫，取名字為 website 。
```
CREATE database website;
```
- 在資料庫中，建立會員資料表，取名字為 member 。資料表必須包含以下欄位設定：
```
USE website;

CREATE table member (id BIGINT PRIMARY KEY auto_increment,name VARCHAR(255) NOT NULL,username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,follower_count INT UNSIGNED NOT NULL DEFAULT '0',time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP());
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request2.png)
 -->

## 要求三：SQL CRUD
- 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
INSERT INTO member (name, username, password, follower_count) VALUES ('test', 'test','test',0);

INSERT INTO member (name, username, password, follower_count) VALUES ('mickey', 'mickey','mickey',1);

INSERT INTO member (name, username, password, follower_count) VALUES ('kitty', 'kitty','kitty',2);

INSERT INTO member (name, username, password, follower_count) VALUES ('winnie', 'winnie','winnie',3);

INSERT INTO member (name, username, password, follower_count) VALUES ('bearmaji', 'bearmaji','bearmaji',4);
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-1.png)


- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
SELECT * FROM member;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-2.png)

- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
```
SELECT * from member ORDER BY time DESC;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-3.png)
- 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄
位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
SELECT * from member ORDER BY time DESC LIMIT 1,3;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-4.png)
- 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```
SELECT * FROM member WHERE username = 'test';
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-5.png)
- 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-6.png)
-使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改
成 test2。
```
UPDATE member SET name = 'test2' WHERE username = 'test';
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request3-7.png)
## 要求四：SQL Aggregate Functions
- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
SELECT COUNT(id) FROM member;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request4-1.png)
- 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
SELECT SUM(follower_count) FROM member;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request4-2.png)
- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
SELECT AVG(follower_count) FROM member;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request4-3.png)
#### 1. 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message 。資料表中必須包含以下欄位設定：

| 欄位名稱 | 資料型態 | 額外設定 | ⽤途說明 |
| :--- | :--- | :------ | :----- |
|id |bigint |主鍵、⾃動遞增 |獨立編號|
|member_id |bigint |不可為空值<br>外鍵對應 member 資料表中的 id|留⾔者會員編號|
|content |varchar(255) |不可為空值 |留⾔內容|
|like_count |int unsigned |不可為空值，預設為 0 |按讚的數量|
|time |datetime |不可為空值，預設為當前時間 |留⾔時間|

```
CREATE table message (id BIGINT PRIMARY KEY auto_increment,member_id BIGINT NOT NULL,content VARCHAR(255) NOT NULL,like_count INT UNSIGNED NOT NULL DEFAULT '0',time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP());

ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5.png)
```
INSERT INTO message (member_id, content, like_count) VALUES (6, 'Hello Kitty!',3);

INSERT INTO message (member_id, content, like_count) VALUES (4, 'test',1);

INSERT INTO message (member_id, content, like_count) VALUES (5, 'Hi, Mickey!',2);

INSERT INTO message (member_id, content, like_count) VALUES (8, 'My name is bearmaji.',5);

INSERT INTO message (member_id, content, like_count) VALUES (7, 'Winnie Pooh',8);

INSERT INTO message (member_id, content, like_count) VALUES (7, 'Doing nothing often leads to the very best something.',99);

INSERT INTO message (member_id, content, like_count) VALUES (4, "I didn't fail the test. I just found 100 ways to do it wrong.",11);
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5.1.png)
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5.2.png)
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5.3.png)
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5.4.png)
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5.5.png)
- 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。
```
SELECT message.id, member.name, member.username,message.content, message.like_count FROM message LEFT JOIN member on message.member_id = member.id;
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5-1.png)
- 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留⾔，資料中須包含留⾔者的姓名。
```
SELECT message.id, member.name, member.username,message.content, message.like_count FROM message LEFT JOIN member on message.member_id = member.id WHERE member.username = 'test';
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5-2.png)
- 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
```
SELECT AVG(message.like_count) FROM message LEFT JOIN member on message.member_id = member.id WHERE member.username = 'test';
```
![Image text](https://github.com/Melodystart/wehelp_phase1/blob/main/week5/png/request5-3.png)