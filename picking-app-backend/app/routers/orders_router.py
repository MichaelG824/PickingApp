from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Orders, OrderLines, ProductMaster
from typing import List
from database import get_db

router = APIRouter()

@router.get("/orders")
def read_orders(db: Session = Depends(get_db)):
    orders = db.query(Orders).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")

    result = []
    for order in orders:
        order_lines = db.query(OrderLines).join(ProductMaster).filter(OrderLines.order_number == order.order_number).all()
        if not order_lines:
            continue
        order_data = {
            'orderNumber': order.order_number,
            'fakeName': order.fake_name,
            'orderDate': order.order_date,
            'itemNames': [
                {
                    'dinnerTitle': line.product_master.dinner_title,
                    'sku': line.product_master.sku,
                    'location': line.location,
                    'pickQty': line.pick_qty,
                    'pickId': line.pick_id
                } for line in order_lines
            ]
        }
        result.append(order_data)

    return result


@router.get("/picks/{pick_id}")
def read_order_line(pick_id: str, db: Session = Depends(get_db)):
    print(pick_id)
    pick = db.query(OrderLines).join(ProductMaster).filter(OrderLines.pick_id == pick_id).first()
    if not pick:
        raise HTTPException(status_code=404, detail="Pick not found")
    return pick
