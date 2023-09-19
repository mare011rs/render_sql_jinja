{% set test_variable = filter_values('FILTER_2') if filter_values('FILTER_2') else [1, 2, 3] %}
{% set test_variable2 = filter_values('FILTER_3')[0] if filter_values('FILTER_3') else 'Test' %}

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

  and metric_3 = '{{ test_variable2 }}'