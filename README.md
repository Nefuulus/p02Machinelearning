# <h1 align=center> **PROYECTO INDIVIDUAL Nº2** </h1>

# <h1 align=center>**`Datathon - Machine Learning`**</h1>

<p align="center">
<img src="https://datascientest.com/es/wp-content/uploads/sites/7/2020/12/1-1024x576.jpg"   
>
</p>


## Introducción:

¡Hola bienvenidos!  Mi nombre es Matias Saez  y este es mi segundo proyecto para la etapa de Labs de la carrera de Data Science de SoyHenry. 
La finalidad de este proyecto es poder realizar un modelo de Machine Learning para predecir la estancia de un futuro paciente en un determinado hospital, si esta sera prolongada (+8 dias) o no. Para ello trabajaremos con 2 datasets en formato .csv para entrenar y probar nuestro modelo.

## **Archivos**
​
Se proveen los siguientes archivos para realizar el proyecto:
 - 'hospitalizaciones_train.csv': Contiene 410000 registros y 15 dimensiones, el cual incluye la información **numérica** de la cantidad de días de estancia hospitalaria.
 - 'hospitalizaciones_test.csv': Contiene 90000 registros y 14 dimensiones, el cual no incluye la información de la cantidad de días de estancia hospitalaria.

## **Métrica a utilizar**
​
Como método de evaluación del desempeño del modelo, se utilizará la métrica de Exhaustividad (Recall) para las estadías hospitalarias largas, a partir de la matriz de confusión (Confusion Matrix). 


$$ Recall=\frac{TP}{TP+FN}$$


Donde $TP$ son los verdaderos positivos y $FN$ los falsos negativos.

Como métrica adicional para verificar el desempeño de su modelo, también se utilizará la métrica de precisión (Accuracy) para las estadías hospitalarias largas.

$$ Accuracy=\frac{TP+TN}{P+N}$$

siendo $TP$ los verdaderos positivos, $TN$ verdaderos negativos y $P+N$ población total.

## **Descripción de las dimensiones**
- Available Extra Rooms in Hospital: Habitaciones adicionales disponibles en el hospital. Una habitación no es igual a un paciente, pueden ser individuales o compartidas.
- Department: Área de atención a la que ingresa el paciente. 
- Ward_Facility_Code: Código de la habitación del paciente.
- doctor_name: Nombre de el/la doctor/a a cargo del paciente.
- staff_available: Cantidad de personal disponible al momento del ingreso del paciente.
- patientid: Identificador del paciente.
- Age: Edad del paciente.
- gender: Género del paciente.
- Type of Admission: Tipo de ingreso registrado según la situación de ingreso del paciente.
- Severity of Illness: Gravedad de la enfermedad/condición/estado del paciente al momento del ingreso.
- health_conditions: Condiciones de salud del paciente. 
- Visitors with Patient: Cantidad de visitantes registrados para el paciente.
- Insurance: Indica si la persona posee o no seguro de salud. 
- Admission_Deposit: Pago realizado a nombre del paciente, con el fin de cubrir los costos iniciales de internación. 
- Stay (in days): Días registrados de estancia hospitalaria

## Objetivos: 

+ Entrenamiento y predicción utilizando un Modelo de Machine Learning adecuado al problema (clasificación o regresión).

+ Análisis exploratorio de los datos (EDA).

+ División de dataset en train y test utilizando train_test_split, CV, KFold o similares.

+ Utilización de Pipelines en la producción del modelo.

+ Comentarios y redacción con la fundamentación de la solución propuesta, escrita en Markdown en el Jupyter Notebook (.ipynb) o bien en un documento aparte.

## Explicación del modelo:

Si bien este apartado se encuentra detallado paso a paso en el archivo `EDA_FeatureEng.ipynb`, a modo de resumen comento cómo encaré este problema. Luego de realizar un pequeño análisis de mis datos y algunas conversiones, como por ejemplo, utilizar LabelEncoder para convertir mis variables categóricas, decidí probar dos tipos de modelos de clasificación: Regresión Logística y Árbol de decisión. Hice un test utilizando un Árbol porque es el modelo con el que más familiarizado me encuentro, sin embargo, comparé ambos para verificar cuál de estos tenía una mejor accuracy. Además, a la hora de hacer el árbol utilicé la validación cruzada para sacar la profundidad óptima de mi árbol. Luego de hacer la selección de Features utilizando Chi², determiné las features óptimas para entrenar mi modelo, ajusté mis hiperparámetros y obtuve resultados positivos.

## Aclaraciones:

Hay algunas cosas a tener en cuenta, el análisis y modelo propuestos NO son necesariamente los más óptimos/mejores, varias decisiones fueron tomadas a mi propio criterio, por ejemplo, la profundidad del árbol, el uso del estadístico Chi² (como se comenta en el Notebook) para la selección de features en lugar de la correlación de Pearson, descarte de columnas que personalmente creía innecesarias (Como 'patientid' y 'Visitors with Patient'), etc...

## Explicación de los contenidos del Repositorio:

+ En la carpeta `datasets` se encuentran los datasets analizados, el archivo `hospitalizaciones_train.csv` que es el que utilizamos para instanciar y entrenar el modelo y el archivo `hospitalizaciones_test.csv` que es al que se le aplica el modelo ya terminado para sacar deducciones.

+ En el notebook `EDA_FeatureEng.ipynb` se encuentra el código comentado paso por paso, explicando las decisiones tomadas a la hora de encarar este proyecto;
    Esto se hizo así para tener dividido de manera ordenada los bloques de código, separados por los markdowns que van dividiendo las etapas del proceso.
    Con esto espero documentar y demostrar cada paso del desarrollo.

+ En el archivo `DecisionTree_model.pkl` se encuentra el modelo de árbol de decisión creado, importado con la librería de Joblib.

+ En el archivo `pred_generator.py` se encuentra el código que se encarga de realizar las transformaciones necesarias sobre el dataset `hospitalizaciones_test.csv` además de aplicarle el modelo, sacar las conclusiones y generar el archivo `Emmafer.csv` donde se encuentra mi columna de predicciones.

## Herramientas/librerías utilizadas:

+ Python. 

+ Pandas. 

+ Numpy. 

+ Mathplotlib. 

+ ScikitLearn. 

+ Joblib. 



<p align="center">
<img src="http://static1.squarespace.com/static/57812963f7e0aba104cde634/t/578133b0ff7c501754eca98b/1468085169537/Machine+Learning+is+Fun%21-logo-black.png?format=1500w"   
>
</p>