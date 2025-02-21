# qa-projects-Urban-Routes-es

## Descripción del Proyecto
Este proyecto implementa pruebas automatizadas para la aplicación Urban Routes, una plataforma de solicitud de taxis. Las pruebas incluyen la selección de origen y destino, la elección de una tarifa de confort, la introducción de un número de teléfono para confirmación por SMS, la configuración de un método de pago, el envío de un mensaje al conductor, la selección de opciones adicionales,la confirmación de la solicitud del taxi y por último la información del viaje ( nombre del conductor, placa del vehículo, y tiempo de espera).


## 1. Tecnologías y Técnicas Utilizadas

1. **Python:** Lenguaje principal para la implementación de las pruebas.
2. **Selenium WebDriver:**  Framework utilizado para la automatización de pruebas en navegadores web. 
3. **WebDriverWait y Expected Conditions:** Manejo de sincronización para garantizar la estabilidad de las pruebas, dar tiempo para que se encuentren los webelements.
4. **Assert:** Confirma los resultados esperados en cada paso de la prueba.
5. **Google Chrome y ChromeDriver:** Navegador y controlador utilizados para la ejecución de las pruebas.




 
## 2. Instrucciones para ejecutar las pruebas
 **Instalar dependencias:**                                                                                                                                                                        
 Asegúrate de tener instalado las siguientes dependencias:
 
1. **Python** instalado en tu sistema. 
2. **Framework de pruebas**  `pytest` 
3. **Google Chrome** (actualizado a la última versión)
4. **Chromedriver** (compatible con la versión de Chrome instalada)
5. **Selenium** (se puede instalar con pip install selenium)

## 3. Ejecución de las Pruebas

**Requisitos previos**

* **Instalar dependencias:** Asegúrate de tener Python instalado y luego instala las dependencias necesarias con:
`pip install selenium pytest`
*  **Configurar ChromeDriver:** 
*  Descarga e instala ChromeDriver.

* Agrega ChromeDriver al PATH de tu sistema.

## 4. Explicación de las Pruebas

Las pruebas incluidas verifican los siguientes escenarios:
* **test_set_route:** Verifica que la ruta de origen y destino se puede establecer correctamente.

* **test_select_comfort_rate:** Comprueba la selección de la tarifa "Comfort".

* **test_enter_phone_number:** Valida la autenticación con código SMS.

* **test_enter_payment_method:** Añade y verifica un método de pago.

* **test_enter_message_to_driver:** Envía un mensaje al conductor.

* **test_select_blanket_and_handkerchief:** Activa la opción de cobija y pañuelo.

* **test_add_ice_cream:** Incrementa el contador de helado.

* **test_request_taxi_button:** Solicita un taxi exitosamente.
* **test_trip_details_modal_after_countdown:** Muestra los modales del contador y de la información del viaje.

**IMPORTANTE!**
* Se recomienda cerrar todas las ventanas del navegador antes de ejecutar las pruebas para evitar conflictos.

* Asegúrate de actualizar la URL de Urban Routes data.py antes de ejecutar las pruebas.

## 4. Estructura del archivo de prueba main.py
 **Imports utilizados**    
El código usa los siguientes imports
```python
import sender_stand_requests  
import data
import json
import time
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException



