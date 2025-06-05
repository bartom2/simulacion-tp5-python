# Mail de Preguntas 1
1.
"Se deberá simular X tiempo (parámetro solicitado al inicio) generando N cantidad de
iteraciones en total."
Este parámetro de tiempo puede ser una unidad que nosotros determinemos? ¿O debe ser en horas? (ya que nuestro enunciado utiliza minutos)
2. 
"Se deberá mostrar en el vector de estado i iteraciones a partir de una hora j (valores i y j
ingresados por parámetro)."
Tengo dudas sobre que dice esta parte del enunciado. Esto significa que nosotros a partir de una hora  ingresada por parametro, debemos mostrar i vectores estados?
Adicionalmente le pregunto sobre como prefiere que se ingrese el valor de hora para esta parte del enunciado si en cantidad de minutos u horas o en este formato "12:30"
3.
Hay algun formato en el que usted prefiera que nosotros mostremos los vectores estado? Puede ser en tablas o en formato JSON?
4.
Respecto a "Generar N días" en función del valor X que se ingrese por parametro, el valor que ingrese da por ejemplo 1,3 días, se trunca la parte decimal o se redondea para arriba en caso de ser mayor o igual a 5?
# Respuesta 1 del Profe
Léase X tiempo en la unidad de medida que elijan. Puede ser que haya quedado inconsistente esa parte del enunciado.
Si trabajan en días, por ejemplo, ingresando X=100000, i=100 y j=300, deberían mostrar una tabla de 100 filas en la que la primera fila corresponde al día 300 o el que más se le aproxime.
No redondeen los días. Trabajen con decimales de modo que se pueda apreciar la diferencia de tiempo entre una iteración y la siguiente.
El formato debe ser una tabla. Los resultados los pueden mostrar en una panel de resultados.
Quedo atento por cualquier otra consulta.

# Mail de Preguntas 2
1.
Tengo la duda de si es que j se debe establecer también en días o puede ser en minutos
2.
Luego de la finalización del turno de 8 horas, se reinicia la cola a 0 para el comienzo de un nuevo día? Teniendo que así agregar el evento Final de Jornada Laboral que se establece inicialmente en lo que sea respectiva 8 horas en minutos y se actualiza con la duración final del ultimo cliente agregando 0,1 minutos extra para que suceda en un evento aparte?
3. 
Como el día tiene 8 horas laborales, que pueden variar su extensión máxima si es que hay más clientes haciendo cola. Dependiendo de la unidad de j, si esta es en días, el momento inicial de j se calcula en relación a una jornada estándar de 8 horas convertida a minutos y comienza a  mostrar filas cuando el reloj marque esa equivalencia de días en minutos?

# Respuesta 2 del Profe
1) El ejemplo de días era eso, un ejemplo. Pueden trabajar en la unidad de tiempo más adecuada al enunciado.
2) La cola va a estar en 0 porque tienen que seguir trabajando hasta que se atiende el último cliente. Respecto al evento de final de jornada laboral, debería ocurrir a las 8 horas exactas de empezado el día. Y deberían tener un evento de principio de día. Cuando ocurre cualquiera de esos eventos, pueden arrastrar el dato que ocurrió el evento manejando un estado.
3) Si van a trabajar con un reloj en minutos, trabajen con j en minutos. No se compliquen. Si quieren trabajar con j en días, sí, deberían transformar esa entrada del usuario a minutos.

# Mail de Preguntas 3
1.
¿Es necesario en la tabla donde se muestran las iteraciones mostrar el rnd y el tiempo que va a tardar un evento? o se puede mostrar simplemente el tiempo en el ocurriría el evento nuevamente, es decir, (RND | Duracion | Prox ev o solamente Prox ev)
2.
Respecto a mostrar los clientes en cada iteración, nosotros tenemos un vector que representa la cola de clientes, al mostrar los clientes, cuando estos salgan del sistema, sería erróneo que los demás clientes se muevan una columna en la sección de clientes?
3.
Respecto al objeto de vector estado que nosotros manejamos, es necesario tener dos vectores estado en todo momento? ya que con un solo vector estado, este ya tiene los datos que necesita para la siguiente iteración y así actualizar los distintos valores de los eventos y objetos
4.
Seria correcto que el valor X solo admita valores enteros para que se simulen X días exactos, o es necesario que este admita valores decimales?
5.
Seria correcto que eventos como Comienzo de Jornada Laboral se calculen cuando la cola tenga una longitud 0 y todos los masajistas se encuentren desocupados, siendo el tiempo del próximo evento de Comienzo Jornada Laboral, el reloj en ese instante + 0,01? Mail de Preguntas 3

# Respuesta 3 del Profe
1) Muestren todo.
2) Los datos de un cliente en particular deben verse siempre en la misma columna a través de las iteraciones. Lo que pueden hacer es reciclar las columnas usadas por el objeto destruído con datos de nuevos clientes que entren al sistema.
3) Pueden trabajar sobre el mismo vector de estado si quieren. Se refiere a que no mantengan todos los datos de todas las iteraciones en una tabla.
4) No hay problema que sean solo enteros.
5) No. Deberían inicializar el evento al principio de la simulación con el tiempo en el que ocurrrirá. Y luego, como cualquier otro evento, calcular el tiempo del proxímo evento.
