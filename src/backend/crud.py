from sqlalchemy.orm import Session
from src.backend.models import ProductModel
from src.backend.schemas import ProductCreate, ProductUpdate

# Functions for select products
def getall_products(db: Session):
    return db.query(ProductModel).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# Function for create products
def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product

# Function for update products
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not db_product:
        return "Product not found"
    
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    
    return db_product

# Function for delete products
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not db_product:
        return "Product not found"
    
    db.delete(db_product)
    db.commit()
    
    return "Product deleted successfully"
    