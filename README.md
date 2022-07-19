# How to run tests
## With chrome
```
pytest --browser chrome
```
## With firefox
```
pytest --browser firefox
```
## Runtests with selenoid on 99 firefox and save allure logs
```
pytest tests --browser=firefox --executor=127.0.0.1 --browser_version=99.0 --alluredir=allure_results
```