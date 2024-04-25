from fastapi import status, HTTPException
from pymongo.collection import Collection
from pymongo import MongoClient
from bson import ObjectId
from lib.excel import append_data_into_excel, update_data_into_excel
from lib.settings import settings
from typing import Generator
from datetime import datetime
from lib import utils

client = MongoClient(settings.databaseURL)
db = client[settings.databaseName]


class AuthDB:
    collection: Collection = db.get_collection("users")

    @classmethod
    def create_user(cls, data: dict) -> dict:
        res = cls.collection.insert_one(data)
        if not res.inserted_id:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create. Try again...",
            )
        return cls.get_user_by_id(res.inserted_id)

    @classmethod
    def get_user_by_id(cls, object_id: str) -> dict:
        res: dict = cls.collection.find_one({"_id": ObjectId(object_id)})
        if isinstance(res, dict):
            res["id"] = str(object_id)
        return res

    @classmethod
    def get_user_by_username(cls, username: str) -> dict:
        res: dict = cls.collection.find_one({"username": username})
        if isinstance(res, dict) and res.get("_id"):
            res["id"] = str(res["_id"])
            del res["_id"]
        return res


class ReceiptDB:
    collection: Collection = db.get_collection("receipt")

    @classmethod
    def create_receipt(cls, data: dict):
        excel_data = data.copy()
        if excel_data.get("id"):
            del excel_data["id"]
        data["date"] = utils.clean_date_format(data["date"])
        append_data_into_excel(excel_data, data.get("section_code"))
        res = cls.collection.insert_one(data)
        if not res.inserted_id:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create. Try again...",
            )
        return cls.get_receipt_by_id(res.inserted_id)

    @classmethod
    def update_receipt(cls, receipt_id: str, data: dict):
        excel_data = data.copy()
        update_data_into_excel(
            data.copy(), data.get("section_code"), data.get("receipt_number")
        )
        if excel_data.get("id"):
            del excel_data["id"]
        data["date"] = utils.clean_date_format(data["date"])

        res = cls.collection.update_one({"_id": ObjectId(receipt_id)}, {"$set": data})
        print(f"{res.matched_count=}")
        if not res.matched_count:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update. Try again...",
            )
        return cls.get_receipt_by_id(receipt_id)

    @classmethod
    def get_receipt_by_receipt_no(cls, receipt_no: str, section_code: str) -> dict:
        res = cls.collection.find_one(
            {"receipt_number": receipt_no, "section_code": section_code}
        )
        if res:
            res["id"] = str(res["_id"])
            del res["_id"]
        return res

    @classmethod
    def get_receipt_by_id(cls, receipt_id: str) -> dict:
        res = cls.collection.find_one({"_id": ObjectId(receipt_id)})
        if res:
            res["id"] = str(receipt_id)
        return res

    @classmethod
    def get_all_receipts(cls, section_code: str) -> Generator:
        cursor = cls.collection.find({"section_code": section_code})
        for document in cursor:
            document["id"] = str(document["_id"])
            del document["_id"]
            yield document

    @classmethod
    def current_month_total(cls, section_code: str) -> float:
        current_month = datetime.now().month

        start_date = utils.clean_date_format(
            datetime(datetime.now().year, current_month, 1)
        )
        end_date = utils.clean_date_format(
            datetime(datetime.now().year, current_month + 1, 1)
        )

        pipeline = [
            {
                "$match": {
                    "section_code": section_code,
                    "date": {"$gte": start_date, "$lt": end_date},
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total_amount": {"$sum": "$donated_amount"},
                }
            },
        ]

        result = list(cls.collection.aggregate(pipeline))

        return result[0]["total_amount"] if result else 0


class DonorDB:
    collection: Collection = db.get_collection("donor")

    @classmethod
    def create(cls, data: dict):
        data["date"] = utils.clean_date_format(data["date"])
        data["last_donated_date"] = data["date"]
        result = cls.collection.insert_one(data)
        return result

    @classmethod
    def update(cls, data: dict):
        data["last_donated_date"] = utils.clean_date_format(data["date"])

        del data["date"]

        result = cls.collection.update_one(
            {"donor_registration_number": data.get("donor_registration_number")},
            {"$set": data},
        )
        return result

    @classmethod
    def read(cls, key: str) -> dict:
        result: dict = cls.collection.find_one({"donor_registration_number": key})
        return result
