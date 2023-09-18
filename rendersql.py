from jinja2 import Environment, FileSystemLoader
import argparse
import os


def filter_values(value):
    return None


def where_in(values: list, mark: str = "'") -> str:
    def quote(value) -> str:
        if isinstance(value, str):
            value = value.replace(mark, mark * 2)
            return f"{mark}{value}{mark}"
        return str(value)

    joined_values = ", ".join(quote(value) for value in values)
    return f"({joined_values})"


def render_sql(template_path):
    env = Environment(loader=FileSystemLoader('.'))
    env.globals['filter_values'] = filter_values
    env.filters['where_in'] = where_in
    env.trim_blocks = True
    env.lstrip_blocks = True

    template = env.get_template(template_path)
    rendered_sql = template.render()

    output_path = os.path.splitext(template_path)[0] + '_render.sql'

    with open(output_path, 'w') as f:
        f.write(rendered_sql)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Render SQL using Jinja2 with custom macros')
    parser.add_argument('--template', required=True, help='Path to the SQL template file')
    
    args = parser.parse_args()
    
    render_sql(args.template)