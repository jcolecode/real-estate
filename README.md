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
    * Created a python virtual environment so we can run on any kind of machine
        * Installed selenium and openpyxl to the virtual environment
    * Installed the chromedriver in the project directory so it is dependent on the project path rather than dependent on system-specific paths
        * May have an issue because everyone using this program could possibly not have the same version of chrome, for now we are using "chromedriver mac-arm64 Version: 117.0.5938.149"
        * Only idea I have of getting around this issue is to run this code on a Virtual Machine so the chromedriver and system are consistent