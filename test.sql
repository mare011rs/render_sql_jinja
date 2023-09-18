{% set test_variable = filter_values('FILTER_2') if filter_values('FILTER_2') else [1, 2, 3] %}

select
	*
from
	test_table
where 1=1
  {% if filter_values('FILTER_1')[0] %}
  and metric_1 >= {{ filter_values('FILTER_1')[0] }} 
  {% else %}
  and metric_1 >= 0
  {% endif %}
  
  and metric_2 in {{ test_variable|where_in }}
