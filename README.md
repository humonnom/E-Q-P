# E-Q-P   

## English Quiz Program
좋아하는 드라마 대본으로 영어 공부하려고 만든 프로그램   

---

### Files
- Google Spread Sheet  
- txt 파일  

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
	
**REVIEW TEST**    
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
│       │   └── bigbang\ theory\ {season}-{epi}.txt
│       ├── it_crowd
│       │   └── {season}-{epi}.txt
│       └── voyager
└──         └── voyager{season}_{epi}.txt     

11 directories, 163 files
