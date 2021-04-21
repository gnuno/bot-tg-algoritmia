# BOT AlgoritmiaUNO

<table>
<tr>
<td>

Un BOT sencillo de multiples utilidades dentro del grupo de [algoritmia](https://t.me/algoritmiaUNO).

Inicialmente se trata de mostrar el desafio de la semana y conectarse con el [repo](https://github.com/gnuno/algoritmia) y estar pendiente a eventos.
</td>
</tr>
</table>


## Modo de Uso
Los comandos para interactuar desarrollados hasta ahora son:

* `/help`: Muestra los comandos disponibles.
* `/challenge`: Obtiene y muestra el desafio actual.


## Desarrollo

### Setup

Te recomendamos el uso de *pipenv*, con este podras tener todas las dependencias necesarias en un entorno virtual.
```
# Instalar PIPENV
pip install pipenv
```

**A partir de aca los comandos deben correr dentro de la carpeta del proyecto**
```
# Crear entorno virtual 
pipenv install

# Agregar dependencias 
pipenv install {PAQUETE}

# Si agregas nuevas dependencias no te olvides de plasmarlas en el .lock
pipenv lock 

# Si queres borrar el entorno virtual
pipenv --rm
```

### Entorno de pruebas

Podes probar las nuevas funcionalidades del bot antes de hacer el PullRequest.
Ejecuta esto y anda a [UNOTestBots_BOT](http://t.me/UNOTestBots_BOT)
```
pipenv run main.py
```

### Aportes

Para contribuir con el código o arreglando errores/bugs, lo podés hacer de la siguiente manera:

* Crea un `fork` del repositorio en tu perfil
* Crea una nueva `branch` (`git checkout -b nueva-funcionalidad`)
* Agrega el código necesario
* Commitea los cambios
* Hace un `push` de de la branch a tu repositorio remoto (`git push origin nueva-funcionalidad`)
* Desde tu perfil en Github crea un `pull request` 

### Sugerencias / Problemas

Si querés hacer alguna sugerencia o reportar algún problema, podés [abrir un issue](https://github.com/gnuno/bot-tg-algoritmia/issues/new) en este mismo repositorio


## Tecnologías

* [Python 3.8.8](https://www.python.org)
* [python-telegram-bot 13.4](https://github.com/python-telegram-bot/python-telegram-bot)
* [PyGithub](https://pygithub.readthedocs.io/en/latest/)


## [LICENCIA](https://github.com/gnuno/bot-tg-algoritmia/blob/main/LICENSE)
