from fastapi import APIRouter, HTTPException, Depends
from services.pick_service import PickService
from sqlalchemy.orm import Session
from dtos.requests.update_status_request_dto import UpdateStatusRequestDto
from database import get_session
import logging
from sqlalchemy.ext.asyncio import AsyncSession
import json

router = APIRouter()

@router.get("/get-pick-list-data")
async def get_pick_list_data(session: AsyncSession = Depends(get_session)):
    try:
        pick_service = PickService(session)
        pick_list_data = await pick_service.get_pick_list_data()
        return pick_list_data
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{pick_id}")
async def get_pick_by_id(pick_id: str, session: AsyncSession = Depends(get_session)):
    try:
        pick_service = PickService(session)
        pick = await pick_service.get_pick_by_id(pick_id)
        return pick
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update-status")
async def update_pick_status(request: UpdateStatusRequestDto, session: AsyncSession = Depends(get_session)):
    try:
        pick_service = PickService(session)
        await pick_service.update_pick_status(request)
        return {"message": "Order line status updated successfully"}
    except Exception as e:
        logging.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))