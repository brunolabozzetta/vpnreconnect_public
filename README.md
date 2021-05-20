# VPN RECONNECT
## _Un script desarrollado en Python para reconectar una conexión VPN via FortiClient o via Windows, de forma automática_

VPN RECONNECT es un pequeño script pensado para hacerle la vida mas fácil a analistas de infraestructura y administradores de red.

Si trabajás en un NOC (Network Operating Center), y utilizás una conexión VPN generada a través de FortiClient, y por problemas exceden a tu gestión, esa conexión se cae muy seguido, y tenés que reconectarla manualmente, este script está pensado para ese caso.

## _¿Como funciona?_

VPN RECONNECT consta de 3 instancias que trabajan en conjunto.
- Archivo compilado en *.py.
- Archivo de lotes (*.bat)
- Tool de Fortinet.

> El script principal funciona como un "listener", 
> apuntando a una dirección ip que se encuentra 
> en la red a la cual debieras estar conectado.
> Al momento en que el ping empieza a fallar
> el programa ejecutará el .bat que ejecutará
> el forticlient a través de parámetros pre-configurados
> con el fin de reconectar la conexión VPN.
>
> En caso de conexiones Windows es tan solo un comando. [rasdial previus_vpn user password123]
>
> En la instancia 'ONLINE' veremos el fondo de color verde.
> En la instancia 'OFFLINE' veremos el fondo de color rojo.
> En breve el programa chequeará una condición predeterminada, (en este caso, una conexión VPN puente), si se encuentra offline esta conexión, la conectará y luego ejecutará los > parámetros hacia fortitools para conectar la VPN de Fortinet. De encontrarse conectada, ejecutará este ultimo paso directamente.
> Mientras chequea esta condición previa y trabaja en reconectar esa conexión puente, la pantalla se verá en color amarillo.
>
> Para tener una señal sonora de la caída de la conexión,
> recomiendo herramientas mas eficientes como Cacti, Nagios,
> o para infraestructuras mas pequeñas: vmPing.


## _Requerimientos_

VPN RECONNECT necesita Python 3 en adelante para funcionar correctamente

> [Python](https://www.python.org/downloads/) v3+ to run.
> Windows (Testeado en Windows 10, pero debería funcionar en Windows 7 sin problemas).
> FortiTools 6.0+ (Incluido en este repositorio).

## _Ejecución_

> VPN RECONNECT corre sobre la shell de Windows, siempre y cuando esté previamente instalado Python en tu computadora.
> Tan solo es necesario ejecutarlo y quedará corriendo, auditando la conexión, hasta que ésta se caiga, entonces actuará en consecuencia y procederá a reconectarla.
> 
> Previo a su uso, deberás configurar los parámetros pertinentes a tu conexión VPN en el archivo de lotes "vpnreconnect.bat"


## _Enlaces_

- [Cacti] - The Complete RRDTool-based Graphing Solution
- [Nagios] - The Industry Standard In IT Infrastructure Monitoring
- [vmPing] - (Visual Multi Ping) is a graphical ping utility for monitoring multiple hosts.

 [Cacti]: <https://www.cacti.net>
 [Nagios]: <https://www.nagios.org>
 [vmPing]: <https://github.com/R-Smith/vmPing>
 
 ## _Contribuciones_

Si quieres contribuir a este pequeño desarrollo, siéntete libre de hacer un pull request y con gusto lo estaré revisando.
Gracias por interesarte en este código.
