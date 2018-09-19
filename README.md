# Respositorio para la resolucion del examen de ingreso para Mercado Libre de nivel 2
## Hecho por Martin Heredia

Para lograr una resolución fueron necesarias tomar ciertas asunciones. A continuación se detallan las mismas:
- **Alineación inicial de los plantetas**: Se asume que inicialmente (en el día 0) los 3 planetas están alineados entre sí, y además alineados con el sol.
- **Duración del año**: Se asume que 1 año son 365. También se asume que no hay años bisiestos
- **Rangos de días que se pueden consultar**: Se asume que a partir del día 0 (inclusive) hasta el día 3650 (inclusive) se pueden consultar por la condición meteorológica. A la vez, todos esos días se incluyen para el calculo de la cantidad de días de sequías, cantidad de períodos de lluvias, cantidad de períodos de condiciones óptimas de presión y temperatura, y para el pico máximo de lluvia
- **Dias sin eventos**: Hay algunos dias que no cumplen con niguno de los 3 eventos descriptos. Para estos casos se asumio que al consultar por dichos dias, el resultado obtenido es un string con el valor 'nada'
- **Contingencia por posible error numerico**: Como para calcular las posiciones de los planetas en cierto dia es necesario el uso de las funciones trigonometricas Sin y Cos, esto puede conllevar un error numerico. Es por esto que para saber si los 3 planetas estan alineados entre si, se verifica que el angulo que forma el segmento (fer_pos, bet_pos) con el eje Y sea parecido al angulo formado por el segmento (bet_pos, vul_pos) con el eje Y

## Dificultades encontradas

A continuacion se detallan las dificultades encontradas:
- **Uso de base de datos**: Se intento utilizar una base de datos sqlite3 para que al deployar el proyecto se carguen los datos meteorologicos de cada dia, y luego ante cada llamada de api, la respuesta se base en ir a buscar el evento del dia. Finalmente no se logro setear bien la configuracion y no se utilizo.
- **Uso de la API**: Si bien la api se pudo deployar usando AppEngine, todo tipo de respuesta es vacia (AppEngine utiliza el framework de webapp2). Si en cambio se quiere levantar el servicio de manera local, existe otra forma de hacerlo, utilizando el Framework de Flask. Para esto, es necesario estar en el directorio root del repo, y en consola correr los siguientes comandos
export FLASK_APP=ml
flask run

Una vez hecho, se le proveera una url localhost (por lo general http://127.0.0.1:5000 ), y con la url http://127.0.0.1:5000/clima?dia=1 se puede llamar a la api