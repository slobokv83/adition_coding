import os

os.chdir('../')
PROJECT_ABSOLUTE_PATH = os.getcwd()

mysql_name = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\mysql.csv'
hadoop_name = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\hadoop.csv'
hadoop_miss = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\hadoop_miss.csv'
mysql_miss = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\mysql_miss.csv'

sufficent_cols = 9

hadoop_columns = ['id', 'timestamp', 'type', 'content_type', 'campaign', 
                  'banner', 'content_unit', 'user_id', 'referrer', 'network',
                  'berowser', 'operating_system', 'country', 'state', 'city',
                  'flash_version', 'mobile_device_class', 'mobile_device',
                  'parent_view_log_id', 'is_ssl', 'is_redirect', 'server_id',
                  'keyword', '[profile_data]', '[external_profiledata]',
                  'script_version', 'screen_resolution', '(adverification)',
                  *range(sufficent_cols)]