from fastapi import APIRouter, HTTPException, Depends
from services.pick_service import PickService
from sqlalchemy.orm import Session
from dtos.requests.update_status_request_dto import UpdateStatusRequestDto
from db.database import get_session
import logging
from sqlalchemy.ext.asyncio import AsyncSession
import json
from dtos.responses.get_pick_by_id_response_dto import GetPickByIdResponseDto
from dtos.responses.pick_list_data_response_dto import PickListDataResponseDto
from dtos.responses.update_status_and_exception_details_response_dto import UpdateStatusAndExceptionDetailsResponseDto
from typing import List

router = APIRouter()

@router.get("/get-pick-list-data", response_model=PickListDataResponseDto)
async def get_pick_list_data(session: AsyncSession = Depends(get_session)):
    try:
        pick_service = PickService(session)
        pick_list_data = await pick_service.get_pick_list_data()
        return pick_list_data
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{pick_id}", response_model=GetPickByIdResponseDto)
async def get_pick_by_id(pick_id: str, session: AsyncSession = Depends(get_session)):
    try:
        pick_service = PickService(session)
        pick = await pick_service.get_pick_by_id(pick_id)
        return pick
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update-status-and-exception-details", response_model=UpdateStatusAndExceptionDetailsResponseDto)
async def update_order_line_status_and_exception_details(request: UpdateStatusRequestDto, session: AsyncSession = Depends(get_session)):
    try:
        pick_service = PickService(session)
        await pick_service.update_order_line_status_and_exception_details(request)
        return {"message": "Order line status updated successfully"}
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))