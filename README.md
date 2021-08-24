### Start a Virtual Environment
```python -m venv env```

### Activate your Virtual Environment
Unix: ```source env/bin/activate```<br>
Windows: ```env/Scripts/activate```

### Download Dependencies
```pip install fastapi```<br>
```pip install uvicorn[standard]```

### Run Web App
```uvicorn main:app --reload```
