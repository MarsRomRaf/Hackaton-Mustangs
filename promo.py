import pandas as pd

def analyze_consumption_patterns(df):
    """Analyzes consumption patterns and returns top 3 giros comerciales per client."""

    df['Articulos'] = df['Articulos'].fillna('No aplica')
    df['Precio'] = df['Precio'].str.replace(r'[$,]', '', regex=True).astype(float)

    top_3_giros_per_client = {}
    for client, client_df in df.groupby('Num. Cliente'):
        giro_counts = client_df['Giro Comercial'].value_counts()
        top_3_giros_per_client[client] = giro_counts.head(3).index.tolist()  # Get top 3 giros for the client
    
    return top_3_giros_per_client

def suggest_promotion(top_giros):
    """Suggests a promotion based on the client's top 3 giros comerciales."""

    promotions = {
        "Supermercado": [
            "Martes de Frescura (Super Ahorro): 2x1 en frutas y verduras seleccionadas.",
            "Fin de Semana de Carnes (Super Ahorro): 30% de descuento en todos los cortes de carne.",
            "Despensa Familiar (Super Ahorro): Llevando 3 productos de la misma marca participante, el de menor valor es gratis."
        ],
        "E-commerce": [
            "Cyber Week Extendido (MegaTienda Online): Descuentos de hasta el 60% en todas las categorías durante una semana.",
            "Envío Gratis (MegaTienda Online): Compras superiores a $50 con envío gratuito a todo el país.",
            "Flash Sales (MegaTienda Online): Descuentos sorpresa en productos seleccionados cada día a una hora específica."
        ],
        "Entretenimiento": [
            "Noche de Cine 2x1 (Cineplex Multiplex): Entradas 2x1 todos los miércoles.",
            "Combo Familiar (Parque Aventuras): Entrada al parque de diversiones + menú infantil a precio promocional.",
            "Acceso VIP (Cineplex Multiplex): Upgrade a entrada VIP con descuento para conciertos seleccionados."
        ],
        "Alimentos y bebidas": [
            "Happy Hour Extendido (Bar La Terraza): 2x1 en tragos seleccionados de 18:00 a 21:00 hs.",
            "Menú Ejecutivo Promocional (Restaurante Sabores del Mundo): Almuerzo ejecutivo con bebida y postre incluidos a un precio fijo.",
            "Brunch Dominical (Restaurante Sabores del Mundo): Brunch para dos personas con descuento especial."

        ],
        "Comida a domicilio": [
            "Promo Delivery (Delicias Express): Descuento del 20% en el primer pedido a través de la app.",
            "Noche de Pizza (Pizza Planet): 2x1 en pizzas grandes los martes.",
            "Combo Familiar (Delicias Express): Menú familiar para 4 personas con bebida y postre incluidos a precio promocional."
        ],
        "Tecnología": [
            "Renovate Tech (TecnoMundo): Descuento del 15% en la compra de un nuevo smartphone entregando tu antiguo dispositivo.",
            "Pack Gamer (TecnoMundo): Combo de teclado, mouse y auriculares gamer con descuento especial.",
            "Financiación Exclusiva (TecnoMundo): 12 cuotas sin interés en la compra de productos seleccionados."
        ],
        "Retail": [
            "Sale de Temporada (Tienda Moda & Estilo): Descuentos de hasta el 50% en prendas seleccionadas.",
            "Día del Cliente (Tienda Moda & Estilo): Descuento especial del 20% para clientes registrados.",
            "Promo 3x2 (Tienda Moda & Estilo): Llevando 3 prendas, la de menor valor es gratis."
        ],
        "Restaurant": [
            "Almuerzo Ejecutivo (El Buen Paladar): Menú ejecutivo a precio promocional de lunes a viernes.",
            "Cena Romántica (El Buen Paladar): Menú especial para dos personas con copa de vino incluida.",
            "Domingo Familiar (El Buen Paladar): Menú infantil gratis por cada adulto que consuma un plato principal."

        ],
        "Clothing": [
            "Liquidación de Temporada (Boutique Chic): Descuentos de hasta el 70% en prendas de la temporada anterior.",
            "Promo Jeans (Boutique Chic): 2x1 en jeans seleccionados.",
            "Descuento por cantidad (Boutique Chic): 10% de descuento llevando 2 prendas, 20% llevando 3 o más."

        ],
        "Electronics": [
             "Mega Descuentos en Electrónica (Electro Hogar): Descuentos de hasta el 40% en productos seleccionados (TV, audio, etc.).",
            "Oferta Especial en Smartphones (Electro Hogar): Compra un smartphone y llévate un accesorio de regalo.",
            "Plan Canje (Electro Hogar): Entrega tu antiguo dispositivo y obtené un descuento en la compra de uno nuevo."
        ],
        "Sector Financiero": [
             "Cuenta Sueldo Bonificada (Banorte): Apertura de cuenta sueldo con bonificación en la cuota mensual durante los primeros 6 meses.",
            "Tarjeta de Crédito con Beneficios (Banorte): Tarjeta de crédito con devolución del IVA en compras en supermercados.",
            "Préstamos Personales con Tasa Promocional (Banorte): Préstamos personales con tasa de interés reducida durante los primeros 12 meses."
        ]
    }

    suggested_promotions = []
    for giro in top_giros:
        if giro in promotions:
            suggested_promotions.append(promotions[giro][0])  # Take the first available promotion

    return suggested_promotions if suggested_promotions else ["No hay promoción disponible por el momento."]



# Load data
df = pd.read_csv("Libro1_extended.csv")

# Get and print top 3 giros and promotions per client
top_3_per_client = analyze_consumption_patterns(df)
print("\nLos 3 Giros Comerciales más repetidos por cliente con promociones:")
for client, top_giros in top_3_per_client.items():
    promo_list = suggest_promotion(top_giros)
    print(f"Cliente {client}: {', '.join(top_giros)}")  # Print comma-separated list of giros
    print("  Promociones:")
    for promo in promo_list:
        print(f"    - {promo}")
    print()