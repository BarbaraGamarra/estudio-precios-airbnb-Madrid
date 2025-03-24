# Análisis de precios de Airbnb en Madrid

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/2560px-Airbnb_Logo_B%C3%A9lo.svg.png" width="300">
</div>

## Objetivo del proyecto

Este proyecto tiene como objetivo analizar los factores que influyen en los precios de los alojamientos de Airbnb en Madrid, con especial foco en el perfil de propiedades de nuestro cliente.

Mediante técnicas de análisis de datos y visualización avanzada, buscaremos entender:

- ¿Qué características de las propiedades tienen mayor impacto en el precio?
- ¿Cómo influye la ubicación en el coste de los alojamientos?
- ¿Existe una correlación entre las valoraciones de los huéspedes y los precios?
- ¿Qué diferencias hay entre las propiedades de los Superhosts y los anfitriones regulares?
- ¿Cuál sería el precio óptimo para las propiedades de nuestro cliente según sus características?

## Perfil del cliente

Nuestro cliente posee apartamentos con las siguientes características:
- **Tipo de propiedad**: Apartamentos
- **Localización**: Todos los barrios de Madrid
- **Número de habitaciones**: De 1 a 3 habitaciones
- **Rango de precio**: Segmento no lujo 

## Metodología

El análisis se estructura en los siguientes apartados:

1. **Preparación y exploración inicial**
   - 0. Librerías utilizadas (pandas, numpy, matplotlib, seaborn, plotly, folium, scipy)
   - 1. Datos: carga, limpieza y transformación
   - 2. Requisitos de cliente: definición del segmento objetivo

2. **Análisis geográfico**
   - 3.1. ¿Cómo influye en los precios la distancia a Sol?
   - 3.2. ¿Cómo varía el precio según el barrio?

3. **Análisis de inmuebles**
   - 4.1. ¿Qué características tienen los pisos con precios óptimos?
   - 4.2. ¿Qué comodidades tienen los pisos con precio óptimo?

4. **Análisis contractual**
   - 5. Estudio de políticas de cancelación, estancias mínimas y otros factores contractuales

5. **Análisis de reseñas**
   - 6. Impacto de las valoraciones y comentarios de clientes en el precio

## Datos

El análisis se basa en un conjunto de datos que incluye información sobre más de 21,000 propiedades en Madrid, con detalles sobre:

- **Condiciones**: precio, noches mínimas/máximas, políticas de cancelación
- **Anfitriones**: tiempo de respuesta, tasa de respuesta, estado de Superhost, verificaciones
- **Ubicación**: vecindario, coordenadas, distancia a puntos de interés
- **Propiedades**: tipo de propiedad, tipo de habitación, capacidad, comodidades
- **Reseñas**: puntuaciones, cantidad de reseñas, idiomas de las reseñas

## Tecnologías utilizadas

- **Lenguaje de programación**: Python
- **Librerías de análisis**: 
  - Pandas, NumPy: manipulación y procesamiento de datos
  - SciPy: análisis estadístico
  - ydata_profiling: generación de informes de datos
- **Visualización**: 
  - Matplotlib, Seaborn: gráficos estadísticos
  - Plotly: visualizaciones interactivas
  - Folium: mapas geoespaciales
- **Entorno de desarrollo**: Jupyter Notebooks

## Resultados y conclusiones

El proyecto proporciona:

- Identificación de los factores clave que influyen en el precio de los alojamientos
- Análisis detallado del impacto de la ubicación en la rentabilidad
- Mapas de calor y visualizaciones geoespaciales de la distribución de precios
- Perfiles de propiedades más rentables por zona
- Análisis de la relación entre comodidades ofrecidas y precios
- Recomendaciones específicas para optimizar el precio de los apartamentos del cliente
- Visualizaciones interactivas que muestran patrones y tendencias en el mercado