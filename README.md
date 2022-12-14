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

Luego de realizar un pequeño análisis de los datos y modificar algunas variables en mi dataset hice un test utilizando un Árbol porque es el modelo que mas intuia que podia solvertar la problematica presente en este proyecto, de todas maneras comparé tanto el arbol de decision como la regresion logistica para verificar cuál de estos tenía una mejor accuracy. Utilicé la validación cruzada para sacar la profundidad óptima del árbol de decisiony determiné las features óptimas para entrenar mi modelo usando Chicuadrado.

## Disclaimer:

El modelo utilizado no necesariamente es el mejor o más optimo, ocupe mi propio criterio para la utilizacion de herramientas que aqui se presentan logrando de todas maneras un buen resultado.


## Explicación de los contenidos del Repositorio:

+ En la carpeta `datasets`  el archivo `hospitalizaciones_train.csv` que es el que utilizamos para  entrenar el modelo y el archivo `hospitalizaciones_test.csv` que es al que se le aplica el modelo para ver como ha funcionado.

+ En el notebook `pred_fileEDA.ipynb` se encuentra el código comentado, explicando las decisiones tomadas a la hora de la toma de decisiones;
 

+ En el archivo `Modelo.pkl` se encuentra el modelo de árbol de decisión creado.

+ En el archivo `pred_file.py` se encuentra el código que se encarga de realizar las transformaciones necesarias sobre el dataset `hospitalizaciones_test.csv` y obtener el archivo `Prediccion.csv`.

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