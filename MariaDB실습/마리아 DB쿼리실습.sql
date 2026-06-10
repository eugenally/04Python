

/*
marina DB에서 새로운 데이터 베이스와 계ㅅ정 생성하기
:오라클 에서는 계정만 생성하면 되지면 MySQL(MarinaDB)
에서는 DB와 User(사용자계정)을 동시에 생성한 후
권한설정을 해야한다. 
*/


##아래 작업은 root 계정으로 접속한 후에 실행해야한다.##
## 새로운 데이터 배이스 생성
CREATE DATABASE sample_db;
#새로운 사용자 계정 생성(로컬에서만 접속할 수있게 설정)
CREATE USER 'sample_user'@'localhost' IDENTIFIED BY '1234';
# sample_db를 사용할수 있는 모든 권한을 sample_user에게 부여한다.
GRANT ALL PRIVILEGES ON sample_db.* TO 'sample_user'@'localhost';
# 이명령을 통해 위에서 설정한 사항을 MariaDB에 적용
FLUSH PRIVILEGES;

/*
실행 방법 
F9 :현재 문서의 전체쿼리문을 한꺼번에 실행
Ctrl+F9 : 블럭으로 지정한 쿼리문만 실행
			만약 쿼리문의 절반정도만 선택 했다면, 실행시 에러가 발생한다. 
Ctrl+Shift+F9 : 현재 쿼리를 실행한다. 단 마지막에 작성한 문장의
					세미콜론안으로 커서를 옮긴후 실행해야한다.
*/
SELECT * FROM board;
SELECT * FROM books;
SELECT * FROM guestbook;


##################################################################################
##여기서 부터는  sample_user 계정으로 접속한수 작성 합니다.

/*
AUTO_INCREMENT
		:자동증가 컬럼으로 지정한다. 오라클에서 사용하는
		Sequence(시퀸즈)와 동일한 역할로, 1씩 증가하는 순차적인 
		정수값을 자동으로 생성한 후 입력한다.

UNSIGNED
		:정수형 컬럼으로 지정하는 경우 음수는 사용하지 않고,
		양수의 범위만 사용한다.이때 양의 범위가 2배로 늘어난다.
		-128~127 범위가 255로 양수 범위만 된다.

*/

CREATE TABLE tb_int(
   /* 일련번호 */
	idx INT PRIMARY KEY AUTO_INCREMENT,
	/* 정수형*/
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	/* 실수형*/
	fnum1 FLOAT(10,5) NOT NULL,
	fnum2 DOUBLE(20,10)
);
DESC tb_int;
	
/*
데이터 입력하기
형식1] insert into 테이블명 (컬럼명) value (값);
		일련번호인 idx컬럼은 insert문에서 생략하고
		작성한다. 자동증가 컬럼으로 지정 되었으므로 
		번호는 자동으로부여된다.
*/

INSERT INTO tb_int(num1,num2,num3,num4,fnum1,fnum2)
VALUES(123,12345,1234567,1234567890,
		12345.12345,1234567890.1234567890);

SELECT * FROM 
/*
형식2] insert into 테이블명 values(값);
		insert문 작성시 컬럼을 명시하지 않으면 전체 
		컬럼에 대해 입력값을 작성해야한다. 단, 이 경우
		일련번호가 중복되어 에러가 발생될 수 있으므로 
		권장하지 않는다.
*/
INSERT INTO tb_int
VALUES(2,123,12345,1234567,1234567890,
		12345.12345,1234567890.1234567890);


######################################################

# 2.날짜형으로구성된테이블
/*
CURRENT_TIMESTAMP: 날짜형식으로 지정된 컬럼에 디폴트 값으로
현재 시간을 입력해 준다.
NOW(): 날짜 형식으로 지정된 컬럼에 현재시각을 입력할 때
	사용하는 함수로, 초단위 까지의 시간이 입력된다.
	오라클의Sysdate와 동일한 역할을 한다.
*/

CREATE TABLE tb_date(
	inx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT CURRENT_TIMESTAMP);
DESC tb_date;

# now()함수를 통해 현재 시간 입력
INSERT INTO tb_date (DATE1,DATE2) VALUES ('2023-02-25',NOW());
#쿼리문 작성시 컬럼을 생략하면 Default값이 입력된다.
INSERT INTO tb_date (DATE1) VALUES('2023-02-27');

SELECT * FROM  tb_date;

# 3.문자형으로 구성되 테이블

/*
VARCHAR(n) : 문자타입으로 짧은 글을 저장할때 사용한다.
 (게시판 의 제목)
 
TEXT : 긴글을 저장할때 사용(게시판의 내용)
*/
CREATE TABLE tb_string(
		idx INT PRIMARY KEY AUTO_INCREMENT,
		
		str1 VARCHAR(30) NOT NULL,
		str2 TEXT
);
DESC tb_string;

INSERT INTO tb_string(str1,str2) VALUES('난 짧은 글3','난 엄청 긴글3');

/*
레코드 조히시 조건 추가하기
*/
SELECT * FROM tb_string;
# 레코드 조회시 조건 추가하기
SELECT * FROM tb_string WHERE idx=1;
SELECT * FROM tb_string WHERE idx=1 AND str1='난짧은글2';
SELECT * FROM tb_string WHERE idx=1 AND str2='난짧은글3';
SELECT * FROM tb_string WHERE idx=1 OR str1='난 짧은글3';

/*
레코등 검색시 문자열이 포함된 것을 인출하고 싶다념 like 절을 사용한다.
*/

SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은';
 
 
# 4.특수형
/*
enum: 여러 항목중 1개만 선택 할 수 있는 자료형
set: d여러항목중 2개 이상을 선택할 수 있는 자료형 
오라클릐check제악조건가 비슷하다.
*/ 
 
CREATE TABLE tb_spec(
		# 	PRIMARY KEY 아웃라인 방식
		idx INT AUTO_INCREMENT,
		
		spec1 ENUM('M','W','T'),
		spec2 SET('A','B','C','D'),
		
		PRIMARY KEY (idx)
);

 
# 설정된 값만 추가 했으르로 정상 입력됨
INSERT INTO tb_spec(spec1, spec2) VALUES('W','A,B,C');

INSERT INTO tb_spec(spec1, spec2) VALUES('X','A,B,C');#spec1에러
INSERT INTO tb_spec(spec1, spec2) VALUES('M','X,B,C');#spec2에러

INSERT INTO tb_spec(spec2) VALUES('B,C,D');


#파이선 샐습을 위한 테이블 생성
CREATE TABLE board
(
		num INT NOT NULL AUTO_INCREMENT,/*일련번호(자동증가)*/
		title VARCHAR(100) NOT NULL,/*제목:짧은 텍스트*/
		content TEXT NOT NULL,/*내용 : 긴텍스트*/
		id VARCHAR(30) NOT NULL,
		/*작성일. 현재시각을 디폴트 값으로 설정*/
		postdate DATETIME DEFAULT CURRENT_TIMESTAMP,
		visitcount MEDIUMINT NOT NULL DEFAULT 0,/*조회수*/
		PRIMARY KEY (num)/*아웃라인 방식으로 프라이머리 키 설정*/
);

INSERT INTO board (title, content, id, visitcount) VALUES
('안녕하세요 첫 번째 게시글', '처음으로 작성하는 게시글입니다.', 'user01', 0),
('오늘 날씨가 정말 좋네요', '봄 날씨처럼 따뜻하고 화창한 하루입니다.', 'user02', 5),
('맛집 추천 부탁드려요', '서울 강남 근처 맛집 아시는 분 댓글 달아주세요!', 'hong123', 12),
('공지사항 안내드립니다', '이번 주 금요일 서버 점검이 있을 예정입니다.', 'admin', 30),
('자유게시판 이용 안내', '게시판 이용 규칙을 꼭 읽어주시기 바랍니다.', 'manager01', 8);

INSERT INTO board (title, content, id, visitcount) VALUES
('개발 공부 어떻게 시작하셨나요?', '비전공자인데 개발 공부 시작하려고 합니다. 조언 부탁드려요!', 'newbie_dev', 45),
('주말 여행지 추천', '이번 주말 당일치기로 다녀올 만한 곳 추천해주세요.', 'traveler99', 23),
('Java Spring 질문있습니다', 'Spring Boot 프로젝트 설정 중 오류가 발생했습니다. 도움 요청드립니다.', 'spring_kim', 67),
('오늘 점심 뭐 드셨나요?', '저는 오늘 김치찌개 먹었는데 다들 점심은 해결하셨나요?', 'lunchking', 19),
('취업 준비 팁 공유합니다', '6개월 준비 끝에 최종합격했습니다. 도움됐던 것들 공유할게요.', 'gotjob2024', 102);

SELECT * FROM board;


CREATE TABLE board
(
		num INT NOT NULL AUTO_INCREMENT,/*일련번호(자동증가)*/
		name VARCHAR(20) NOT NULL,/*이름:짧은 텍스트*/
		tel MEDIUMINT NOT NULL DEFAULT 0,/*전화번호 : 정수*/
		add VARCHAR(30) NOT NULL,
		
		
	
		PRIMARY KEY (num)/*아웃라인 방식으로 프라이머리 키 설정*/
);


DESC board;

CREATE TABLE board
(
		num INT NOT NULL AUTO_INCREMENT,/*일련번호(자동증가)*/
		name VARCHAR(20) NOT NULL,/*이름:짧은 텍스트*/
		tel MEDIUMINT NOT NULL DEFAULT 0,/*전화번호 : 정수*/
		add VARCHAR(30) NOT NULL,
		PRIMARY KEY (num)/*아웃라인 방식으로 프라이머리 키 설정*/
);

CREATE TABLE data_list_db
(
    num  INT          NOT NULL AUTO_INCREMENT,  /* 일련번호(자동증가) */
    name VARCHAR(20)  NOT NULL,                 /* 이름 */
    tel  VARCHAR(20)  NOT NULL,                 /* 전화번호 */
    addr VARCHAR(30)  NOT NULL,                 /* 주소 */
    PRIMARY KEY (num)
);
DESC board;

