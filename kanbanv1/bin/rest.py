from  kanboard import Client

#kb = kanboard.Client('http://localhost/jsonrpc.php', 'jsonrpc', 'your_api_token')
kb = Client('http://192.168.0.195/kanboard/jsonrpc.php', 'jsonrpc', '0c00a0274320b13b0852d04527b281e381a493cbbdd6cd35eae7df6c75ed')


#project_id = kb.create_project(name='My project')
#kb.add_project_user(project_id=project_id, user_id=123, role='project-manager')

task_id = kb.create_task(project_id=1, title='REST Task-05',description='description 05',column_id='2',category_id='1')