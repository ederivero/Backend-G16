from flask_sqlalchemy import SQLAlchemy

# La conexion entre mi ORM y mi Base de Datos
# No se recomienda tener mas de 1 conexion a la base de datos
conexion = SQLAlchemy()
