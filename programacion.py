def main():
    # Precios de los rolls
    menu = {
        1: {"nombre": "Pikachu Roll", "precio": 4500},
        2: {"nombre": "Otaku Roll", "precio": 5000},
        3: {"nombre": "Pulpo Venenoso Roll", "precio": 5200},
        4: {"nombre": "Anguila Eléctrica Roll", "precio": 4800}}
        
    # Lista para almacenar los rolls pedidos
    pedido = []

    # Variable para almacenar el total del pedido
    total_pedido = 0

     # Bucle para agregar rolls al pedido
    while True:
        print("\n--- MENÚ ---")
        for num, roll in menu.items():
            print(f"{num}. {roll['nombre']} - ${roll['precio']}")
        
        