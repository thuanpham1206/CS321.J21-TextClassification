# Text classification

# Runtime:
    Python version >= 3.5.2

# Guideline:
1. clone source code from repository:
    - git clone https://github.com/thuanpham1206/CS321.J21-TextClassification

2. Install package dependencies (if any)
    - pip install -r requirements.txt

3. How to run?
    - Make sure you are in the root folder of project
    - Run the following command: python manage.py {argument}
    - Supported arguments:
        + train: training the model
        + evaluate: generate precision-recall chart and save it.
        + server: run server -> goto: localhost:5000
    - Example:
        + python manage.py server

4. project structure:
   ``` 
    ├── app/
    │   ├── model/    -> contain model.pkl file
    │   ├── source/   -> contain source code, static file,...
    │   └── storage/  -> contain data
    ├── report/       -> contain report file (.docx, .pdf)
    ├── seminar       -> contain seminar file
    └── manage.py     -> help to run code cleaner
   ```
