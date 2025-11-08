URL
========================================
Las _URL_ son importantes!!, con ellas se tiene una noción sencilla de **ubicación** dentro de un computador. Sino, cómo más uno podría ubicarse dentro de un computador de forma sencilla?
Con una URL se puede responder la pregunta dónde está 'tal archivo'. Las URL son direcciones; con una dirección se llega a cualquier lugar!

Forma canonica/general:
URL := `protocolo://user@host:puerto/ruta/al/recurso`
* `protocolo`: cómo obtengo el recurso / idioma-comunicación
* `host`: en qué computador está el recurso / apartamento-lugar
* `port`: en qué puerto puedo acceder al host / puerta-lugar
* `ruta`: dónde exactamente está el recurso / habitación-lugar

Ejemplos/instancias/particularidades
- `ssh://admin@34.182.30.39/var/html/www`
- `ftp://usuario112@localhost/archivos/2024/12/main.ffsd`
- `http://hannlampert@192.192.1.2/desktop/mng/bin/exe.pt`


Verbos + URL
========================================
Aparte de ofrecer localización de recursos, es util tener de _verbos_ con los cuales se pueden indicar acciones sobre el recurso apuntado por la URL. Sin los verbos, es como tener un idioma sólo con sustantivos; así no se puede hablar nunca de acciones.

Estos son los más usados:
- GET + URL: obtener recurso ubicado en URL
- POST + URL: almacenar recurso ubicado en URL
- UPDATE + URL: actualizar recurso ubicado en URL (es mas rapido actualizar que crear)
- DELETE + URL: borrar recurso en ubicado URL


SOFTWARE SERVIDOR HTTP
=======================================
Es un software ya **compilado** que entiende y se comporta según se le pase un VERBO **y** una URL.

* Recuerdo
 verbo    url      server
--------|--------|--------
 no     | no     | no sabe que hacer
 no     | si     | no sabe que hacer
 si     | no     | no sabe que hacer
 si     | si     | sabe que hacer

instalas con `apt install apache2`. Recuerda que `apache2` ya viene precompilado. (Te sugiero que busques el codigo fuente del software `apache2`).

## Qué hace tiene de especial un software servidor HTTP?
Este software implementa las caracteristicas de ubicación de una URL. Entiende qué hacer frente a un verbo y también puede manejar sesiones si se le configura. 


SOFTWARE CLIENTE HTTP
=====================================================
Al igual que con el servidor este software sabe cómo preguntar (cómo realizar la solicitud en terminos del protocolo HTTP) al servidor por un recurso cuando al cliente se le pasa un VERBO y una URL.

Hemos usado Mozilla Firefox, es un excelente cliente, pero usa demasiadas convensiones que impide entener con más claridad como funciona la web. Ejemplo de algunas convensiones:
- Siempre se renderiza (se dibuja o pinta) el HTML que devuelve el servidor. Realizar solicitud con _Curl_ para obtener texto HTML y hacer obvia esta convención.
- Siempre se supone que la conexión a un servidor HTTP es en el puerto 80. Por tal razón siempre se omite el puerto cuando se le indica una url al navegador.
- Por defecto el verbo es GET, pues se entiende que es un cliente y solo accede recursos (no crea) en el servidor.
- Recientemente ya no se indica el protocolo en las direcciones, pues ya se supone que el protocolo es HTTPS.
- Si se indica una carpeta, el navegador trata de obtener el `index.html` si lo hay en esa carpeta.

### Curl
Curl permite ver de una forma sencilla la interacción cliente servidor, sin embargo Firefox cuenta con herramientas más cómodas.


Interaccion servidor http
=====================================================

En estos comandos se puede ver un estilo de flujo de trabajo. Se recomienda usar un editor más comodo por ejemplo Kate.
* probar comando:
curl
* obtener pagina (GET no se pone por convención)
curl http://ismaelflorez.com/
* solicito el documento y lo guardo en `pagina.html`
curl https://ismaelflorez.com/status/index.html > pagina.html
* listo para ver que cambió
ls -l 
* abro la pagina que guardé en editor de texto
vim pagina.html 
* abro la pagina en navegador para que renderize y sea más facil imaginar el docmuento
google-chrome pagina.html 
* edito la pagina, veo de donde se obtienen los estilos
vim pagina.html 
* descargo los estilos y los guardo en mi computadora en `stilos.css`
curl https://ismaelflorez.com/assets/dist/css/bootstrap.min.css > stilos.css
* abro con vim para ver rapidamente
vim stilos.css 
* abro denuevo el navegador para ver si tomo efectos
google-chrome pagina.html 
* edito para indicarle ahora al renderizador donde esta mi estilo descargado
vim pagina.html 
* 
google-chrome pagina.html 
* 
vim pagina.html 
* 
curl https://ismaelflorez.com/assets/dist/js/color-modes.js > color.js
* descargo scritps
vim color.js 
* edito
vim pagina.html 
* 
google-chrome pagina.html 
vim pagina.html 
* descargo archivos adicioanles para que la pagina se vea bonita
curl https://ismaelflorez.com/status/product.css > color.js
curl https://ismaelflorez.com/status/product.css > product.css
curl https://ismaelflorez.com/status/product.css > color.js
curl https://ismaelflorez.com/status/product.css > product.css
curl https://ismaelflorez.com/assets/js/color-modes.js > color.js
google-chrome pagina.html 
* me ayudo mirando en el server donde están los archivos para hacer las solicitudes siguientes
ssh -i /home/jcammmmm/.ssh/gcloudkey camila_lugo_rico_22@34.132.247.211
curl https://ismaelflorez.com/assets/brand/actions/a.png > a.png
ls -l
lximg a.png
lximage-qt a.png
vim pagina.html 
google-chrome pagina.html
* temrino
exit




HACIENDO PRUEBAS LOCALES
=====================================================
Como te puedes dar cuenta, estar modificando el archivo directamente en el servidor con vim es algo molesto.
- editar con vim: 
    * dificil copiar y pergar
    * dificil hacer scroll
    * dificil buscar
- modificar directamente en servidor
    * hay que confiar que haya red
    * hay que hacer login con ssh
    * modificar archivos a través de la terminal puede ser engorroso
      - vim es muy util para ciertas tareas, para desarrollar puede ser incomodo
      
1. instalas apache en tu local 
  * si en la nube conozco la ip del computador que ejecuta el software servidor (apache2), cuál es la ip que apunta a mi propio computador?: `localhost` o `127.0.0.1`
2. verifica que tu servidor esté andando:
  ```sudo systemctl status apache2```
3. deten el servidor y mira que pasa
  ```sudo systemctl stop apache2```
4. reinicia el servidor 
  ```sudo systemctl start apache2```
5. descargas los ejemplos y extraes
6. vas a los ejemplos
  ```bootstrap-4.0.0/docs/4.0/examples/```
7. mueves tus ejemplos a `/var/html/www`
8. modifica permisos del servidor para poder ver carpetas mas allá de la raíz en `/var/html/www`
9. cambia el dueño de la carpeta a ti.
   ```sudo chown tuusuario```


  




2. software cliente
  - mozilla
  - cache
  - herramientas de desarrollador
    . sección de red
3. framework
  - bootstrap
4. descargar framework
6. minimizar codigo
7. css como lenguaje de consulta sobre html
9. muestra de otros editores de texto
a. como enfocar analisis de funcionamiento?
  - que clase de negocio es?
  - quien es el usuario?
  
* Por qué las paginas de antes tiene ese estilo particular sencillo?
- Porque en esa epoca (hace 20+ años) HTML y CSS como lenguajes no eran tan ricos semánticamente (no era mucho lo que se podia expresar) por limitaciónes en el software que procesa y renderiza tales lenguajes, que quizá en esa época estaba también limitado por el hardware de los computadores.

* Nota final 1
- Redireccionar es distinto a seguir enlace. El detalle tecnico no lo se, pero se que son distintos. El primero es un tema de servidor (redirección entre servers) y el otro es de cliente.
