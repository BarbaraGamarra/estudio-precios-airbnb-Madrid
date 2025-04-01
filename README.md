
<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/2560px-Airbnb_Logo_B%C3%A9lo.svg.png" width="300">
</div>

# <span style="color: #ff385c;"> Análisis de Precios de Airbnb en Madrid</span>

## <span style="color: #ff385c;"> Descripción del Proyecto</span>

Este proyecto realiza un análisis detallado de los precios de alojamientos de Airbnb en Madrid, con el objetivo de proporcionar insights estratégicos para optimizar la tarificación de propiedades.

## <span style="color: #ff385c;"> Objetivo Principal</span>

Analizar los factores que influyen en los precios de los alojamientos de Airbnb en Madrid, con especial énfasis en:
- Determinación del precio óptimo para propiedades
- Impacto de la ubicación en los costes
- Características inmobiliarias que más influyen en el precio
- Claúsulas contractuales que afectan al precio.
- Relación entre valoraciones de huéspedes y precios
- Diferencias entre Superhosts y anfitriones regulares

## <span style="color: #ff385c;"> Conjuntos de Datos</span>

El proyecto trabaja con 5 dataframes principales:

| DataFrame | Filas | Columnas | Descripción |
|-----------|-------|----------|-------------|
| df_conditions | 21,020 | 7 | Condiciones de los alojamientos |
| df_location | 21,020 | 7 | Información geográfica |
| df_property | 21,020 | 13 | Características de las propiedades |
| df_reviews | 21,020 | 16 | Datos de reseñas |
| df_host | 21,020 | 13 | Información de los anfitriones |

## <span style="color: #ff385c;"> Requisitos del Cliente</span>

- Enfoque en apartamentos de 1 a 3 habitaciones
- Exclusión de propiedades de lujo
- Optimización de precios

## <span style="color: #ff385c;"> Metodología de Análisis</span>

1. **Exploración y limpieza de datos**
   - Análisis de valores nulos
   - Detección de duplicados
   - Identificación de outliers

2. **Análisis exploratorio**
   - Distribución de precios
   - Relaciones entre variables

3. **Análisis estadístico**
   - Evaluación estadística de variables
   - Identificación de factores clave

4. **Visualización**
   - Generación de gráficos informativos
   - Representación visual de insights

5. **Conclusiones**
   - Recomendaciones estratégicas
   - Propuestas de optimización de precios

## <span style="color: #ff385c;"> Áreas de Análisis Principales</span>

### Análisis Geográfico
- Distribución de precios en Madrid
- Influencia de la distancia a Sol
- Variación de precios por barrio

### Análisis de Inmuebles
- Características de pisos con precios óptimos
- Estudio de comodidades
- Tipos de habitaciones y camas

### Análisis Contractual
- Impacto de noches mínimas y máximas
- Efecto de políticas de cancelación

### Análisis de Reseñas
- Impacto de valoraciones en precios

### Análisis de Anfitriones
- Comportamiento del Host

##  <span style="color: #ff385c;"> Cómo Empezar</span>

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar el notebook principal:`airnbn_Madrid.ipynb`