from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Orders, OrderLines, ProductMaster, UpdateStatusRequestDto
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
                    'pickId': line.pick_id,
                    'status': line.status
                } for line in order_lines
            ]
        }
        result.append(order_data)

    return result


@router.get("/picks/{pick_id}")
def read_order_line(pick_id: str, db: Session = Depends(get_db)):
    print(pick_id)
    pick = db.query(OrderLines).join(ProductMaster).filter(OrderLines.pick_id == pick_id).first()
    print(pick)
    if not pick:
        raise HTTPException(status_code=404, detail="Pick not found")
    pickDto = {
        'location': pick.location,
        'orderNumber': pick.order_number,
        'pickId': pick.pick_id,
        'pickQty': pick.pick_qty,
        'sku': pick.sku,
        'dinnerTitle': pick.product_master.dinner_title
    }
    return pickDto

@router.put("/update-status")
def update_order_line_status(request: UpdateStatusRequestDto, db: Session = Depends(get_db)):
    order_line = db.query(OrderLines).filter(OrderLines.pick_id == request.pick_id).first()
    if not order_line:
        raise HTTPException(status_code=404, detail="Order line not found")

    order_line.status = request.status
    db.commit()
    return {"message": "Order line status updated successfully"}