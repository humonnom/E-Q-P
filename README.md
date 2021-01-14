# E-Q-P   

## English Quiz Program
좋아하는 드라마 대본으로 영어 공부를 할 수 있는 프로그램  

## 컨텐츠의 종류  
- Google Spread Sheet  
- txt 파일  

## 포함된 프로그램  
### Bash shell  
- Python 프로그램을 조작(시작, 리뉴얼 등)  
- 부가 프로그램(docx, srt를 txt파일로 바꿔주는 변환기)  
### Python  
- 주된 프로그램  
  
## 사용자가 사용할 수 있는 명령어  
### ./test.sh {option}
**RUN TEST**
Mode: Blank Quiz / Custom(준비중..)   
Default: Blank Quiz   
Option:   
	-날짜 지정: `test.sh {date}`      
	`./test.sh 2021-01-03` or `./test.sh 2021-1-3` 모두 가능   
	-틀린것만 다시보기 `test.sh re`  
-> src/result.csv
	
### ./renew.sh {option}
**RENEW TEST**
Mode: Blank Quiz / Custom(준비중..)   
Default: Blank Quiz   
Option:  
	-Custom file 불러오기: `renew.sh {file name}`
	(준비중..)  
-> src/quiz.csv & src/answer.csv
	
### ./review.sh
**MAKE INCORRECT WORD'S EXAMPLE FILE**
Mode: Default mode only  
-> src/Diglett 폴더에 저장됨   

## 프로젝트 디렉토리    
```md:directory.md
.
├── README.md
├── dig.sh
├── renew.sh
├── review.sh
├── src
│   ├── Diglett
│   │   ├── Alas.txt
│   │   ├── ambiguous.txt
│   │   ├── appropriated.txt
│   │   ├── artificial.txt
│   │   ├── as\ to.txt
│   │   ├── as\ well.txt
│   │   ├── capabilities.txt
│   │   ├── cope.txt
│   │   ├── deliberate.txt
│   │   ├── designate.txt
│   │   ├── determine.txt
│   │   ├── distinction.txt
│   │   ├── drain.txt
│   │   ├── encounter.txt
│   │   ├── get\ through.txt
│   │   ├── made\ of.txt
│   │   ├── perceived.txt
│   │   ├── poses.txt
│   │   ├── pry.txt
│   │   ├── results\ from.txt
│   │   ├── seek.txt
│   │   ├── shaft.txt
│   │   ├── take\ place.txt
│   │   ├── trail.txt
│   │   └── unambiguous.txt
│   ├── __pycache__
│   │   ├── digging.cpython-37.pyc
│   │   ├── digging_sub.cpython-37.pyc
│   │   ├── func.cpython-37.pyc
│   │   ├── header.cpython-37.pyc
│   │   ├── print.cpython-37.pyc
│   │   ├── print_func.cpython-37.pyc
│   │   └── test_range.cpython-37.pyc
│   ├── answer.csv
│   ├── chtxt.sh
│   ├── digging.py
│   ├── digging_sub.py
│   ├── func.py
│   ├── header.py
│   ├── img
│   │   ├── itcrowd
│   │   │   ├── How\ are\ things.png
│   │   │   ├── I\ don't\ think\ it's\ funny.png
│   │   │   ├── I've\ get\ tesrs\ in\ my\ eyes.png
│   │   │   ├── I've\ got\ an\ aunt\ like\ that.png
│   │   │   ├── There\ is\ nothing\ funny\ about\ this.png
│   │   │   ├── They\ do\ have\ some\ strong\ arguments.png
│   │   │   ├── You\ are\ not\ going\ to\ believe\ this.png
│   │   │   ├── amateru\ hour.png
│   │   │   ├── bizarre.png
│   │   │   ├── chump.png
│   │   │   ├── circuit\ board.png
│   │   │   ├── die(2).png
│   │   │   ├── die(3).png
│   │   │   ├── die.png
│   │   │   ├── double\ negative.png
│   │   │   ├── education.png
│   │   │   ├── everything\ is\ connected.png
│   │   │   ├── find.png
│   │   │   ├── for\ an\ hour.png
│   │   │   ├── get\ them\ into\ my\ pocket.png
│   │   │   ├── harmony.png
│   │   │   ├── lack,\ lacks.png
│   │   │   ├── loitering,\ clarify.png
│   │   │   ├── mess,\ delicate\ ecosystem.png
│   │   │   ├── mess.png
│   │   │   ├── much\ like(2).png
│   │   │   ├── much\ like.png
│   │   │   ├── my\ term.png
│   │   │   ├── not\ brilliant.png
│   │   │   ├── on\ what\ planet.png
│   │   │   ├── power\ supply.png
│   │   │   ├── right\ up\ again.png
│   │   │   ├── stands\ for.png
│   │   │   ├── suppose.png
│   │   │   ├── the\ talk\ of\ the\ office.png
│   │   │   ├── tiniest\ bit(2).png
│   │   │   ├── tiniest\ bit.png
│   │   │   ├── upset,\ harmony.png
│   │   │   ├── what\ are\ you\ laughing\ at.png
│   │   │   └── yes\ you\ do.png
│   │   └── voyager
│   │       ├── Aye.png
│   │       ├── Give\ us\ a\ hand.png
│   │       ├── I\ feel\ like\ I'm\ ready\ to\ explode.png
│   │       ├── I\ know\ what's\ best.png
│   │       ├── I\ like\ that.png
│   │       ├── I'm\ in\ between,\ at\ the\ moment.png
│   │       ├── a\ think\ tank.png
│   │       ├── astute.png
│   │       ├── confront,\ self-doubt(2).png
│   │       ├── confront,\ self-doubt.png
│   │       ├── determine.png
│   │       ├── encounter.png
│   │       ├── every\ situation\ is\ a\ little\ different.png
│   │       ├── first\ encounter.png
│   │       ├── get\ through.png
│   │       ├── have\ been\ around,\ for\ a\ while.png
│   │       ├── have\ flown\ through\ worse.png
│   │       ├── my\ first\ responsibility.png
│   │       ├── never\ thought\ about\ it.png
│   │       ├── nor\ have\ I.png
│   │       ├── realize.png
│   │       ├── relevance(1).png
│   │       ├── relevance(2).png
│   │       ├── seek\ out(1).png
│   │       ├── seek\ out(2).png
│   │       ├── small\ price\ to\ pay,\ exhilaration(1).png
│   │       ├── small\ price\ to\ pay,\ exhilaration(2).png
│   │       ├── so\ much\ for.png
│   │       ├── we\ haven't\ had\ the\ best\ of\ luck\ with\ the\ borg.png
│   │       ├── what\ do\ you\ think\ about.png
│   │       ├── which.png
│   │       └── with\ all\ due\ respect,\ godfather.png
│   ├── print_func.py
│   ├── quiz.csv
│   ├── result.csv
│   ├── review.py
│   ├── test.py
│   ├── test_range.py
│   └── txt
│       ├── bigbang
│       │   ├── bigbang\ theory\ season1\ e1-6.txt
│       │   ├── bigbang\ theory\ season1\ e13-17.txt
│       │   ├── bigbang\ theory\ season1\ e7-12.txt
│       │   ├── bigbang\ theory\ season2\ e1-8.txt
│       │   ├── bigbang\ theory\ season2\ e17-23.txt
│       │   ├── bigbang\ theory\ season2\ e9-16.txt
│       │   ├── bigbang\ theory\ season3\ e1-8.txt
│       │   ├── bigbang\ theory\ season3\ e17-23.txt
│       │   ├── bigbang\ theory\ season3\ e9-16.txt
│       │   ├── bigbang\ theory\ season4.txt
│       │   ├── bigbang\ theory\ season5-1.txt
│       │   ├── bigbang\ theory\ season5-10.txt
│       │   ├── bigbang\ theory\ season5-11.txt
│       │   ├── bigbang\ theory\ season5-12.txt
│       │   ├── bigbang\ theory\ season5-13.txt
│       │   ├── bigbang\ theory\ season5-14.txt
│       │   ├── bigbang\ theory\ season5-15.txt
│       │   ├── bigbang\ theory\ season5-16.txt
│       │   ├── bigbang\ theory\ season5-17.txt
│       │   ├── bigbang\ theory\ season5-18.txt
│       │   ├── bigbang\ theory\ season5-19.txt
│       │   ├── bigbang\ theory\ season5-2.txt
│       │   ├── bigbang\ theory\ season5-20.txt
│       │   ├── bigbang\ theory\ season5-21.txt
│       │   ├── bigbang\ theory\ season5-22.txt
│       │   ├── bigbang\ theory\ season5-23.txt
│       │   ├── bigbang\ theory\ season5-24.txt
│       │   ├── bigbang\ theory\ season5-3.txt
│       │   ├── bigbang\ theory\ season5-4.txt
│       │   ├── bigbang\ theory\ season5-5.txt
│       │   ├── bigbang\ theory\ season5-6.txt
│       │   ├── bigbang\ theory\ season5-7.txt
│       │   ├── bigbang\ theory\ season5-8.txt
│       │   └── bigbang\ theory\ season5-9.txt
│       ├── else
│       ├── it_crowd
│       │   ├── 1-1.txt
│       │   ├── 1-2.txt
│       │   ├── 1-3.txt
│       │   ├── 1-4.txt
│       │   ├── 1-5.txt
│       │   └── 1-6.txt
│       └── voyager
│           ├── voyager4_16.txt
│           └── voyager4_20.txt
└── test.sh

11 directories, 163 files
