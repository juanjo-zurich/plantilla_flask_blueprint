import os
from src import crear_app
from dotenv import load_dotenv
load_dotenv()

app = crear_app()


if __name__ == '__main__':
    
    # Leer el puerto y debug desde las variables de entorno
    port = int(os.getenv('PORT', 5000))  # Puerto 5000 como predeterminado
    debug = os.getenv('FLASK_DEBUG', 'False') == 'True'

    print("Debug:", debug)
    print("Port:", port)
    
    app.run(debug=debug, port=port)