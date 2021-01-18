import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class JobFilter(django_filters.FilterSet):
#	scheduled_date = DateFilter(field_name="date_created", lookup_expr='gte')
#	note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Joballocation
		fields = '__all__'
		exclude = ['shift_1_start_time', 'shift_1_end_time', 'shift_1_job',
        'shift_2_start_time', 'shift_2_end_time', 'shift_2_job',
        'shift_3_start_time', 'shift_3_end_time', 'shift_3_job',
        'shift_4_start_time', 'shift_4_end_time', 'shift_4_job',
        'shift_5_start_time', 'shift_5_end_time', 'shift_5_job',
        'shift_6_start_time', 'shift_6_end_time', 'shift_6_job',
        'shift_7_start_time', 'shift_7_end_time', 'shift_7_job',
        'shift_8_start_time', 'shift_8_end_time', 'shift_8_job',
        'shift_9_start_time', 'shift_9_end_time', 'shift_9_job',
        'shift_10_start_time', 'shift_10_end_time', 'shift_10_job',
        
         ]