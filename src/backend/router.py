from fastapi import APIRouter, depends, HTTPException
from sqlalchemy.orm import Session
from databases.MSSQLServer import SessionDbGeral, get_db
from schemas import ProductResponse, ProductCreate, ProductUpdate
from typing import List
from crud import getall_products, get_product_by_id, create_product, update_product, delete_product

router = APIRouter()

@router.get("/products", response_model=List[ProductResponse])
def read_products(db: Session = depends(get_db)):
    products = getall_products(db)
    return products

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products", response_model=ProductResponse)
def create_product_endpoint(product: ProductCreate, db: Session = depends(get_db)):
    return create_product(db, product)  

@router.delete("/products/{product_id}", response_model=str)
def delete_product_endpoint(product_id: int, db: Session = depends(get_db)):
    result = delete_product(db, product_id)
    if result == "Product not found":
        raise HTTPException(status_code=404, detail=result)
    return result

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_endpoint(product_id: int, product: ProductUpdate, db: Session = depends(get_db)):
    updated_product = update_product(db, product_id, product)
    if updated_product == "Product not found":
        raise HTTPException(status_code=404, detail=updated_product)
    return updated_product