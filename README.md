# Convertidor de Monedas con Tkinter y API de Cambio de Divisas


## Descripción

Este es un proyecto de **convertidor de monedas** desarrollado en **Python** utilizando la biblioteca **Tkinter** para la interfaz gráfica de usuario (GUI) y la **API de ExchangeRate** para obtener tasas de cambio en tiempo real. La aplicación permite a los usuarios convertir montos entre diferentes monedas, proporcionando resultados precisos y actualizados en todo momento.

Este proyecto forma parte de mi portafolio personal, mostrando mis habilidades en desarrollo de aplicaciones con Python, manejo de APIs y diseño de interfaces gráficas. A través de esta herramienta, los usuarios pueden realizar conversiones de divisas de manera sencilla y eficiente.

## Características

- **Interfaz de usuario amigable**: Utiliza Tkinter para crear una GUI sencilla y funcional.
- **Conversión de múltiples monedas**: Soporta monedas populares como USD, EUR, GBP, entre otras.
- **Tasas de cambio en tiempo real**: Los datos son obtenidos dinámicamente a través de la API de [ExchangeRate API](https://www.exchangerate-api.com/).
- **Resultado inmediato**: Conversión de monedas con solo ingresar un monto y seleccionar las monedas de origen y destino.
- **Validación de entradas**: Manejo adecuado de errores para entradas no válidas o problemas al obtener los datos de la API.

## Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal.
- **Tkinter**: Para la creación de la interfaz gráfica de usuario (GUI).
- **requests**: Para realizar las solicitudes HTTP a la API de ExchangeRate.
- **API de ExchangeRate**: Para obtener las tasas de cambio actualizadas en tiempo real.

## Requisitos

Para ejecutar esta aplicación, asegúrate de tener instalados los siguientes componentes:

- **Python 3.x**: [Descargar Python](https://www.python.org/downloads/)
- **requests**: Instalar la biblioteca ejecutando:
  
  ```bash
  pip install requests
  ```

## Instalación y Ejecución

**1. Clonar el repositorio**:
   
   ```bash
   git clone https://github.com/Popeye-04/Currency-Converter-.git
   ```

**2. Navegar al directorio del proyecto**:
Una vez clonado el repositorio, navega al directorio del proyecto utilizando el siguiente comando:
  ```bash
  cd currency-converter
  ```
**3. Instalar dependencias**
Este proyecto requiere la instalacion de la biblioteca ```request```. Puedes instalarla utilizando el siguiente comando:
  ```bash
  pip install requests
  ```
**4. Ejecutar la aplicación**
Para ejecutar la aplicación, utiliza el siguiente comando:
  ```bash
  python currency_converter.py
 ```
**5. Interacción con la aplicación**

Cuando la aplicación se esté ejecutando, podrás realizar las siguientes acciones:
- **Monto**: Ingresa el monto que deseas convertir.
- **Moneda de origen**: Introduce la moneda de origen ( ```USD```, unica moneda de origen por el momento).
- **Moneda de destino**: Introduce la moneda de destino (por ejemplo, ```EUR```).
- Haz clic en el botón **Convertir** para obtener el resultado de la conversión.

## Próximos Pasoa
Para mejorar la funcionalidad de esta aplicación en futuras versiones, planeo agregar las siguientes características:

- **Más monedas y países**: Ampliar la lista de monedas soportadas y permitir conversiones entre más países.
- **Historial de conversiones**: Implementar una funcionalidad para guardar y mostrar las conversiones anteriores.
- **Mejorar el diseño de la UI**: Añadir un diseño más interactivo y moderno con iconos y efectos visuales.
- **Preferencias del usuario**: Guardar las preferencias de monedas de origen y destino del usuario para una experiencia más personalizada.

