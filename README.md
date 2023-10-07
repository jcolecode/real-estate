# Real Estate Project

## Setup
 
Make sure you are in the **real-estate** directory, it should look like this: 
```
user real-estate $ 
```
**Activate** the virtual environment:
```
$ source venv/bin/activate
```
Install packages (if needed):
```
$ pip install package-name
```
**Run** Python code:
```
$ cd backend
$ python main.py
```
When finished, **deactivate** the virtual environment:
```
$ deactivate
```

## NOTES

Follow Yianni's explanation video and then scale to a similar platform like "CoStar".

* ### 10-06-2023
    * Download selenium, chromedriver, and openpyxl to setup my environment
    * Line 231 ERROR is from having the wrong username or password (Need Yianni to send accurate login info)
    * Line 134 ERROR SOLVED
        * TODO need to put a chrome driver in the project file so it is not dependent on system-specific paths 
        * May have an issue because everyone using this program could possibly not have the same version of chrome, for now we are using "chromedriver mac-arm64 Version: 117.0.5938.149"
        * Only idea I have of getting around this issue is to run a Virtual Machine when we start selling this so the chromedriver is consistent