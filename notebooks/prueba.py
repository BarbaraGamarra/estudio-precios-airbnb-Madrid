# Cargar y combinar los archivos parquet
def cargar_y_combinar_datos():
    # Diccionario para almacenar los dataframes
    dataframes = {}
    
    # Cargar cada archivo parquet
    for archivo in os.listdir('../data'):
        if archivo.endswith('.parquet'):
            ruta = os.path.join('../data', archivo)
            print(f"Cargando archivo: {archivo}")
            
            # Cargar el dataframe
            df = pd.read_parquet(ruta)
            
            # Mostrar información sobre este dataframe
            print(f"  - Forma: {df.shape}")
            print(f"  - Columnas: {list(df.columns)}")
            
            # Guardar el dataframe con un nombre significativo
            nombre_base = archivo.replace('airbnb_madrid_', '').replace('.parquet', '')
            dataframes[nombre_base] = df
    
    # Comprobar si tenemos todos los archivos necesarios
    if not dataframes:
        return pd.DataFrame()
    
    print("\nCombinando dataframes utilizando merge en 'id'...")
    
    # Comenzar con el dataframe de condiciones (tiene precio)
    if 'conditions' in dataframes:
        df_combinado = dataframes['conditions']
        
        # Combinar con el resto de dataframes
        for nombre, df in dataframes.items():
            if nombre != 'conditions':
                print(f"  - Combinando con {nombre}")
                df_combinado = pd.merge(df_combinado, df, on='id', how='left')
        
        print(f"\nDataFrame combinado exitosamente - Forma: {df_combinado.shape}")
        return df_combinado
    else:
        print("Error: No se encontró el archivo de condiciones con precios.")
        return pd.DataFrame()

# Cargar y combinar los datos
print("Cargando y combinando datos de Airbnb...")
df_airbnb = cargar_y_combinar_datos()

# Verificar la calidad de los datos
print("\nVerificando calidad de los datos:")
print(f"Total de filas: {df_airbnb.shape[0]}")
print(f"Total de columnas: {df_airbnb.shape[1]}")
print("\nColumnas con más valores nulos:")
nulos_por_columna = df_airbnb.isnull().sum()
print(nulos_por_columna[nulos_por_columna > 0].sort_values(ascending=False).head(10))

# Mostrar información básica del conjunto de datos
print("\nPrimeras 5 filas:")
display(df_airbnb.head())

# Análisis del precio
if 'price' in df_airbnb.columns and df_airbnb['price'].notnull().sum() > 0:
    print("\nEstadísticas descriptivas de precio:")
    display(df_airbnb['price'].describe())

    # Visualización de la distribución de precios
    plt.figure(figsize=(10, 6))
    sns.histplot(df_airbnb['price'].dropna().clip(upper=df_airbnb['price'].quantile(0.95)), bins=50, kde=True)
    plt.title('Distribución de Precios (sin outliers extremos)')
    plt.xlabel('Precio')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.savefig('../docs/distribucion_precios.png')
    plt.show()

    # Relación entre precio y ubicación
    if 'neighbourhood' in df_airbnb.columns:
        plt.figure(figsize=(12, 8))
        # Obtener los 10 barrios con más listados
        top_neighbourhoods = df_airbnb['neighbourhood'].value_counts().head(10).index
        data_subset = df_airbnb[df_airbnb['neighbourhood'].isin(top_neighbourhoods)]
        
        sns.boxplot(x='neighbourhood', y='price', data=data_subset)
        plt.title('Precios por Barrio (Top 10 más comunes)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('../docs/precios_por_barrio.png')
        plt.show()

    # Relación entre precio y tipo de propiedad
    if 'property_type' in df_airbnb.columns:
        plt.figure(figsize=(12, 6))
        # Obtener los 6 tipos de propiedad más comunes
        top_types = df_airbnb['property_type'].value_counts().head(6).index
        data_subset = df_airbnb[df_airbnb['property_type'].isin(top_types)]
        
        sns.barplot(x='property_type', y='price', data=data_subset)
        plt.title('Precio Promedio por Tipo de Propiedad')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('../docs/precios_por_tipo.png')
        plt.show()

    # Relación entre precio y capacidad
    if 'accommodates' in df_airbnb.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='accommodates', y='price', data=df_airbnb, alpha=0.3)
        plt.title('Relación entre Precio y Capacidad')
        plt.xlabel('Capacidad (número de personas)')
        plt.ylabel('Precio')
        plt.tight_layout()
        plt.savefig('../docs/precio_vs_capacidad.png')
        plt.show()
        
        # Añadir un boxplot para mostrar mejor la relación
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='accommodates', y='price', data=df_airbnb)
        plt.title('Distribución de Precios por Capacidad')
        plt.xlabel('Capacidad (número de personas)')
        plt.ylabel('Precio')
        plt.tight_layout()
        plt.savefig('../docs/distribucion_precio_capacidad.png')
        plt.show()

    # Relación entre precio y valoraciones
    if 'review_scores_rating' in df_airbnb.columns:
        # Eliminar filas sin valoraciones
        df_with_ratings = df_airbnb.dropna(subset=['review_scores_rating'])
        
        # Crear categorías de valoración
        df_with_ratings['rating_category'] = pd.cut(
            df_with_ratings['review_scores_rating'],
            bins=[0, 80, 90, 95, 100],
            labels=['< 80', '80-90', '90-95', '95-100']
        )
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='rating_category', y='price', data=df_with_ratings)
        plt.title('Precios por Categoría de Valoración')
        plt.xlabel('Categoría de Valoración')
        plt.ylabel('Precio')
        plt.tight_layout()
        plt.savefig('../docs/precios_por_valoracion.png')
        plt.show()

    # Relación entre precio y políticas de cancelación
    if 'cancellation_policy' in df_airbnb.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='cancellation_policy', y='price', data=df_airbnb)
        plt.title('Precios por Política de Cancelación')
        plt.xlabel('Política de Cancelación')
        plt.ylabel('Precio')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('../docs/precios_por_cancelacion.png')
        plt.show()

    # Relación entre precio y distancia a Sol (centro de Madrid)
    if 'dist_km_sol' in df_airbnb.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='dist_km_sol', y='price', data=df_airbnb, alpha=0.3)
        plt.title('Relación entre Precio y Distancia a Sol')
        plt.xlabel('Distancia a Sol (km)')
        plt.ylabel('Precio')
        plt.tight_layout()
        plt.savefig('../docs/precio_vs_distancia_sol.png')
        plt.show()
        
        # Crear categorías de distancia y ver distribución de precios
        df_airbnb['distance_category'] = pd.cut(
            df_airbnb['dist_km_sol'], 
            bins=[0, 1, 2, 3, 5, 10, 20],
            labels=['0-1 km', '1-2 km', '2-3 km', '3-5 km', '5-10 km', '10+ km']
        )
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='distance_category', y='price', data=df_airbnb)
        plt.title('Distribución de Precios por Distancia a Sol')
        plt.xlabel('Distancia a Sol')
        plt.ylabel('Precio')
        plt.tight_layout()
        plt.savefig('../docs/distribucion_precio_distancia.png')
        plt.show()

    # Impacto de comodidades en el precio
    amenities_cols = [col for col in df_airbnb.columns if 'amenities_' in col]
    if amenities_cols:
        # Crear un dataframe con el impacto de cada comodidad
        amenities_impact = []
        for col in amenities_cols:
            # Nombre de la comodidad sin el prefijo
            amenity_name = col.replace('amenities_', '')
            
            # Calcular precio promedio con y sin la comodidad
            price_with = df_airbnb[df_airbnb[col] == 1]['price'].mean()
            price_without = df_airbnb[df_airbnb[col] == 0]['price'].mean()
            
            # Calcular el impacto porcentual
            price_impact = ((price_with - price_without) / price_without) * 100
            
            amenities_impact.append({
                'amenity': amenity_name,
                'price_with': price_with,
                'price_without': price_without,
                'impact_percentage': price_impact
            })
            
        # Convertir a dataframe y ordenar
        df_amenities = pd.DataFrame(amenities_impact)
        df_amenities = df_amenities.sort_values('impact_percentage', ascending=False)
        
        # Visualizar el impacto
        plt.figure(figsize=(10, 6))
        sns.barplot(x='amenity', y='impact_percentage', data=df_amenities)
        plt.title('Impacto de Comodidades en el Precio (%)')
        plt.xlabel('Comodidad')
        plt.ylabel('Impacto en Precio (%)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('../docs/impacto_comodidades.png')
        plt.show()
        
        # Guardar el análisis
        df_amenities.to_csv('../docs/impacto_comodidades.csv', index=False)

    # Guardar un resumen de los datos procesados
    columnas_numericas = df_airbnb.select_dtypes(include=['number']).columns
    df_resumen = df_airbnb[columnas_numericas].describe().T
    df_resumen.to_csv('../docs/resumen_estadistico.csv')
    
    # Correlaciones entre precio y otras variables numéricas
    corr_columns = ['price', 'accommodates', 'dist_km_sol', 'dist_km_airport', 
                    'minimum_nights', 'bedrooms', 'beds', 'bathrooms', 
                    'review_scores_rating', 'review_scores_value', 'number_of_reviews']
    corr_cols_available = [col for col in corr_columns if col in df_airbnb.columns]
    
    if len(corr_cols_available) > 1:
        plt.figure(figsize=(12, 10))
        corr_matrix = df_airbnb[corr_cols_available].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlaciones entre Variables Numéricas')
        plt.tight_layout()
        plt.savefig('../docs/correlaciones.png')
        plt.show()
else:
    print("\n¡ALERTA! La columna 'price' no está disponible o contiene todos valores nulos.")
    print("Por favor, verifica la estructura de tus archivos parquet.")

print("\nAnálisis completado. Las visualizaciones se han guardado en la carpeta 'docs'.")