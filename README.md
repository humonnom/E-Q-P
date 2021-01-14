# E-Q-P   

## English Quiz Program
좋아하는 드라마 대본으로 영어 공부하려고 만든 프로그램   

---

## Files
- Google Spread Sheet  
- txt 파일  

## Programs  
### Bash shell  
- Python 프로그램을 조작(시작, 리뉴얼 등)  
- 부가 프로그램(docx, srt를 txt파일로 바꿔주는 변환기)  
### Python  
- 주된 프로그램  

---

## Command  
**RUN TEST**   
#### ./test.sh           
Mode: Blank Quiz / Custom(준비중..)   
Default: Blank Quiz   
Option:   
-날짜 지정          
`test.sh {date}`      
(`./test.sh 2021-01-03` or `./test.sh 2021-1-3` 모두 가능)   

-틀린것만 다시보기          
`test.sh re`       

-> src/result.csv
	
**RENEW TEST**        
#### ./renew.sh {option}   
Mode: Blank Quiz / Custom(준비중..)   
Default: Blank Quiz   
Option:  
-Custom file 불러오기(준비중..)        
`renew.sh {file name}`
  
-> src/quiz.csv & src/answer.csv
	
**MAKE INCORRECT WORD'S EXAMPLE FILE**    
#### ./review.sh   
Mode: Default mode only  
-> src/Diglett 폴더에 저장됨   

---

## 프로젝트 디렉토리    
```md:directory.md
.
├── README.md
├── test.sh
├── renew.sh
├── review.sh
├── dig.sh
├── src -> source file (you don't need to know)
│   ├── quiz.csv 	-> csv files
│   ├── answer.csv
│   ├── result.csv	
│   ├── chtxt.sh	-> auto convert program(srt -> txt)
│   ├── digging.py	-> python files	
│   ├── digging_sub.py	
│   ├── func.py		
│   ├── header.py	
│   ├── print_func.py	
│   ├── review.py	
│   ├── test.py		
│   ├── test_range.py	
│   ├── Diglett 	-> digged files
│   │   └── {word}.txt
│   ├── img		-> It might be hint...(준비중)
│   │   ├── itcrowd
│   │   │   └── {moris moss}.png
│   │   └── voyager
│   │       └── {engage}.png
│   └── txt		-> source file(txt)
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
│       ├── it_crowd
│       │   ├── 1-1.txt
│       │   ├── 1-2.txt
│       │   ├── 1-3.txt
│       │   ├── 1-4.txt
│       │   ├── 1-5.txt
│       │   └── 1-6.txt
│       └── voyager
│           ├── voyager4_16.txt    
└──         └── voyager4_20.txt     

11 directories, 163 files
