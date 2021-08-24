### Start a Virtual Environment
```python -m venv env```

### Activate your Virtual Environment
Unix: ```source env/bin/activate```
Windows: ```env/Scripts/activate```

### Download Dependencies
```pip install fastapi```
```pip install uvicorn[standard]```

### Run Web App
```uvicorn main:app --reload```
