# ¿Cansado de que tus payloads de Rubber Ducky no funcionen en SO en español?

¡Con DuckyPayloads Español se acabó el problema!

![](Img.jpg)

Esta herramienta escrita en python que usa tkinter, te permite adaptar tus payloads para que funcionen a la perfección en sistemas operativos con la distribución de teclado en español.


## ¿Cómo funciona?

Selecciona tu payload.
DuckyPayloads Español lo adapta automáticamente.
¡Listo para usar en tu Rubber Ducky!
## ¡Ten en cuenta!

Esta herramienta esta enfocada a scripts de powershell lo que conlleva a que los caracteres [ , ] , {  , } solo se escriban en sistemas operativos windows,
con una pequeña modificacion del codigo se podria adaptar a Linux o MacOS.

Tener en cuenta que en sistemas windows a los 5500 milisegundos de conectar el rubber ducky se abrira el explorador de archivos y por eso es necesario editar
el payload para que mas se abra cerrarlo con un ALT F4, ejemplo a continuacion:
```bash
  DELAY 2000      //Esperar 2000 milisegundos
  STRING ejemplo  //Escribir ejemplo
  DELAY 3500      //Esperar 3500 milisegundos
  ALT F4          //Aqui una vez haigan pasado los 5500 milisegundos se  abrira el explorador de archivos y se cerrara.
```

## ¿Como usarlo?

Clona el proyecto

```bash
  git clone https://github.com/sachamark/DuckyPayloads-Esp
```

Ves al directorio del proyecto

```bash
  cd DuckyPayloads-Esp
```

Instala las dependencias

```bash
  sudo apt/dnf/pacman install python3-tkinter
```

Abre la herramienta

```bash
  python DuckyPayloads-esp.py
```
