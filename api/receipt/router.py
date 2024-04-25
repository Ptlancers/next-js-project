from fastapi import APIRouter, Depends, status, HTTPException

from . import schema
from . import controller

from auth.router import get_current_user

router: APIRouter = APIRouter(prefix="/api/receipt")


@router.get(
    "/get-donor-detail/{unique_id:str}",
    status_code=status.HTTP_200_OK,
    response_model=schema.PrintResponse,
)
async def get_data(unique_id: str, user: dict = Depends(get_current_user)):
    receipt: dict = controller.read_donor_detail(unique_id)
    receipt.update(user)
    if receipt:
        return receipt
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found.")


@router.get(
    "/get-by-id/{receipt_id:str}",
    status_code=status.HTTP_200_OK,
    response_model=schema.SearchResponse,
)
async def get_data(receipt_id: str, user: dict = Depends(get_current_user)):
    receipt: dict = controller.get_data_by_receipt_id(receipt_id)

    if receipt:
        return receipt
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found.")


@router.get(
    "/get-data/{receipt_number:str}",
    status_code=status.HTTP_200_OK,
    response_model=schema.SearchResponse,
)
async def get_data(receipt_number: str, user: dict = Depends(get_current_user)):
    receipt: dict = controller.get_data_by_receipt_number(
        receipt_number, user.get("section_code")
    )
    if receipt:
        return receipt
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found.")


@router.post(
    "/insert-data",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.InsertResponse,
)
async def insert_data(data: schema.Receipt, user: dict = Depends(get_current_user)):
    if controller.check_receipt_no_exits(data.receipt_number, user.get("section_code")):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Data already exists..."
        )
    data: dict = data.dict()
    section: dict = schema.Section(**user).dict()
    data.update(section)
    receipt_id: str = controller.create_receipt(data)
    return {"detail": "Data stored successfully", "id": receipt_id}


@router.put(
    "/update-data/{receipt_id:str}",
    status_code=status.HTTP_200_OK,
    response_model=schema.UpdateResponse,
)
async def update_data(
    data: schema.Receipt, receipt_id: str, user: dict = Depends(get_current_user)
):
    data: dict = data.dict()
    section: dict = schema.Section(**user).dict()
    data.update(section)
    receipt_id: str = controller.update_receipt(receipt_id, data)
    return {"detail": "Data Update successfully", "id": receipt_id}
