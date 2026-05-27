from app.app import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = "pedidos"
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    monto = db.Column(db.Float, nullable=False)
    
    # Llaves foráneas (relaciones muchos-a-uno)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    
    # Nota: No necesitas definir 'producto' y 'cliente' como relationship
    # porque ya están definidos en los modelos Cliente y Producto con backref.
    # SQLAlchemy los crea automáticamente.
    
    def __repr__(self):
        return f"Pedido #{self.id} - Fecha: {self.fecha} - Monto: {self.monto}"