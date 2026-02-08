from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
async def list_products():
    return [
        {"id": 1, "name": "Notebook", "price": 3500},
        {"id": 2, "name": "Mouse", "price": 150},
        {"id": 3, "name": "Teclado", "price": 300},
    ]
