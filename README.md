# Automatización de Notas UOH

Python scripts que permiten el cálculo de las notas a partir de los puntajes de las evaluaciones y la generación automática de archivos necesarios para subir las notas al sistema [Ucampus de la Universidad de O'Higgins](ucampus.uoh.cl).

## Antes de empezar

### Prerequisitos

* Python instalado
* Conocimientos básicos de línea de comandos (bash/zsh)

### Configuración local

1. Clonar repositorio
```sh
git clone 
```
2. Instalar requisitos
```sh
pip install requirements.txt
```
3. Descargar archivo molde desde Ucampus  
[Ucampus](ucampus.uoh.cl) > Curso > Notas > Agregar Evaluación > evaluación_creada > Subir Notas desde Archivo > notas.xls
4. Cambiar versión del archivo excel  
Guardar como ... > Formato del Archivo (.xlsx) y guardar en el mismo directorio en el que se clonaron los scritps
5. Generar archivos:  
* master_notas.xlsx
* molde_puntajes.xlsx
```sh
python generador_archivos.py
```

### Descripción archivos

* El archivo `notas.xslx` descargado servirá como molde para generar los archivos que se subiran a Ucampus en cada evaluación.  

* El archivo `molde_puntajes.xlsx` generado es el archivo en donde se deben ingresar los puntajes obtenidos por los estudiantes en las evaluaciones. Se debe modificar para cada evaluación, cambiando el nombre de la columna EVALUACION_NUMERO por el que corresponda y el puntaje obtenido por cada estudiante.  

* El archivo `master_notas.xlsx` generado es donde se irán incorporando tanto los puntajes como las notas de las evaluaciones procesadas. 

* `uoh_*.xslx` es el archivo que se debe cargar a Ucampus que contiene la información de identificación de los estudiantes y las notas obtenidas.

## Uso

1. Modificar el archivo `molde_puntajes.xlsx` con los puntajes de una nueva evaluación y generar un nuevo archivo (e.g. `evaluacion_1.xlsx`)

2. Ejecutar script con el archivo con los puntajes como argumento
```sh
python uoh_notas.py
```

3. Cargar el archivo generado `uoh_*.xslx` en la evaluación correspondiente en Ucampus










