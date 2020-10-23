# selenium_unittest
selenium 프레임워크를 기반으로 unittest 진행

## 테스트 언어
```.py
python:3.9
```
## 테스트 실행
```.py
# install 목록
pip install selenium unittest

"""
chrom driver는 테스트 버전으로 설치 해야 하며 같은 폴더에 있어야 한다.

개인정보를 위해 test에 사용되는 user structure들은 코드에서 빠져있다.

테스트 결과는 repots폴더에 저장된다.
"""
# 실행
python unittest testRun -v
```

## 참고 

* [selenium-python readthedocs](https://selenium-python.readthedocs.io/getting-started.html)
* [chrome driver](https://chromedriver.chromium.org/)