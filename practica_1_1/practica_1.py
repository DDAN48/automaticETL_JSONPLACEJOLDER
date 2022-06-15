from prefect import task,Flow 
 
@task 
def load():
    print('hello world')

with Flow('primer flujo') as flow:
    #se ejecutan las tareas cuando se llame al flujo 
    load()

flow.run()