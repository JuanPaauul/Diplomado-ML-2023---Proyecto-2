# Proyecto 2
## Azure ML Pipelines
### Descripcion
En este proyecto nos centramos en la creacion de componentes para luego crear un pipelines donde podremos ejecutar cada uno de acuerdo a lo requerido. Estas ejecuciones pueden realizarse tanto en paralelo como en serie. Para la creacion de nuestro pipeline usamos un dataset proveido por el docente el cual lleva el nombre de `water_potability_ds.csv`.
### Componentes
#### Clean data
En este componente limpiamos la data.
#### Split data
En este componente separamos la data tanto en entrenamiento como en validacion.
#### Train model
En este componente realizamos el entrenamiento del modelo usando un DecisionTreeClassifier proveniente de la libreria de scikitlearn.
#### Score model
En este componente se hacen predicciones con el dataset de validacion.
#### Eval model
En este componente se evaluan las predicciones obtenidas por el componente de Score en contraste con los valores reales del dataset de validacion.

### Salidas del pipeline
Como salidas tenemos lo siguiente
- La grafica de correlaciones en formato `.jpg`
- El modelo entrenado en formato `.pkl`
- Las metricas del modelo en formato `.txt`

### Estructura del orchestrator
Primero definimos las librerias necesarias, luego usamos nuestras credenciales para iniciar sesien en nuetro mlcliente. Una vez tenemos todo eso listo, comenzamos a cargar nuestro componentes mediente sus archivo `.yml` de cada uno. Una vez cargados en memoria, definimos nuestro pipeline indicando las entradas de los componentes y tambien indicando si alguna entrada depende de la salida de otro componente. Una vez creado todo eso, procedemos a dar inicio a nuestro job el cual ejecutara nuestro pipeline. Finalmente hacemos la descarga de los outputs generados por el pipeline.