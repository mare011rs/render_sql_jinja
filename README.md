
# Render SQL Jinja
A script for rendering Apache Superset SQL datasets which contain jinja templating code. Running this cript on a .sql file containing jinja templates will replace jinja code with real values and turn it into executable SQL code.

## Requirements:
- Python 3
- Jinja2 python package (install with pip)


## How to use:
1. Copy the "rendersql.py" script onto your local machine to some place where it won't be moved from.
2. Paste this bash function into your .zshrc or .bashrc file:
```bash
rendersql() {
	python3  "full/path/to/rendersql.py"  --template  "$1"
}
```
3. Add execution permission for rendersql.py by running the following command in terminal (replace with your file path):
```bash
chmod +x /full/path/to/rendersql.py
```
4. Run the script on any file by executing it in terminal:
```bash
rendersql path/to/your/jinja/dataset.sql
```
This will create a new file with the same name as your original sql file, just concatenating "_render" to the end of filename.

### Considerations
1. If you are using the "filter_values" Superset macro, always define its placeholder in a variable at the beginning of your dataset.
```sql
{% set test_variable = filter_values('FILTER_2') if filter_values('FILTER_2') else [1, 2, 3] %}
```
In this way, if the dataset is used within Superset dashboard it will use the filter values for rendering, and if it is used outside of the dashboard context it will use the placeholder for rendering. See ```test.sql``` file to understand how this is done.

2. ```dataset()``` macro can't be used with this script. All macros that this cript can use must be defined within the dataset sql file and must be executable on Superset.
