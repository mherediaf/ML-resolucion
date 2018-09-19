# Respositorio para la resolucion del examen de ingreso para Mercado Libre de nivel 2
## Hecho por Martin Heredia

Para lograr una resolución fueron necesarias tomar ciertas asunciones. A continuación se detallan las mismas:
- **Alineación inicial de los plantetas**: Se asume que inicialmente (en el día 0) los 3 planetas están alineados entre sí, y además alineados con el sol.
- **Duración del año**: Se asume que 1 año son 365. También se asume que no hay años bisiestos
- **Rangos de días que se pueden consultar**: Se asume que a partir del día 0 (inclusive) hasta el día 3650 (inclusive) se pueden consultar por la condición meteorológica. A la vez, todos esos días se incluyen para el calculo de la cantidad de días de sequías, cantidad de períodos de lluvias, cantidad de períodos de condiciones óptimas de presión y temperatura, y para el pico máximo de lluvia
- **Dias sin eventos**: Hay algunos dias que no cumplen con niguno de los 3 eventos descriptos. Para estos casos se asumio que al consultar por dichos dias, el resultado obtenido es un string con el valor 'nada'
- **Contingencia por posible error numerico**: Como para calcular las posiciones de los planetas en cierto dia es necesario el uso de las funciones trigonometricas Sin y Cos, esto puede conllevar un error numerico. Es por esto que para saber si los 3 planetas estan alineados entre si, se verifica que el angulo que forma el segmento (fer_pos, bet_pos) con el eje Y sea parecido al angulo formado por el segmento (bet_pos, vul_pos) con el eje Y
