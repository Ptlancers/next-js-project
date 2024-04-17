from fastapi import APIRouter, Depends, status, HTTPException

from . import schema

from database.database import ReceiptDB as DB

from auth.router import get_current_user

from typing import Generator

router: APIRouter = APIRouter(
    prefix="/api/receipt"
)


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_data(user: dict = Depends(get_current_user)):
    receipts: Generator = DB.get_all_receipts(user.get("section_code"))
    return receipts


@router.get("/get-by-id/{receipt_id:str}", status_code=status.HTTP_200_OK, response_model=schema.SearchResponse)
async def get_data(receipt_id: str, user: dict = Depends(get_current_user)):
    receipt = DB.get_receipt_by_id(receipt_id)
    if receipt:
        return receipt
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found.")


@router.get("/get-data/{receipt_number:str}", status_code=status.HTTP_200_OK, response_model=schema.SearchResponse)
async def get_data(receipt_number: str, user: dict = Depends(get_current_user)):
    receipt = DB.get_receipt_by_receipt_no(receipt_number, user.get("section_code"))
    if receipt:
        return receipt
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found.")


@router.post("/insert-data", status_code=status.HTTP_201_CREATED, response_model=schema.InsertResponse)
async def insert_data(data: schema.Receipt, user: dict = Depends(get_current_user)):
    check_data = DB.get_receipt_by_receipt_no(data.receipt_number, user.get("section_code"))
    if check_data:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Data already exists...')
    data: dict = data.dict()
    section = schema.Section(**user).dict()
    data.update(section)
    new_receipt = DB.create_receipt(data)
    return {"detail": "Data stored successfully", "id": new_receipt.get("id")}


@router.put("/update-data/{receipt_id:str}", status_code=status.HTTP_200_OK, response_model=schema.UpdateResponse)
async def update_data(data: schema.Receipt, receipt_id: str, user: dict = Depends(get_current_user)):
    data: dict = data.dict()
    section = schema.Section(**user).dict()
    data.update(section)
    updated_receipt = DB.update_receipt(receipt_id, data)
    return {"detail": "Data Update successfully", "id": updated_receipt.get("id")}