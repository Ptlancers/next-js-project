from fastapi import HTTPException, status
from pymongo.collection import Collection, InsertOneResult
from pymongo import MongoClient
from bson import ObjectId
from api.lib.excel import append_data_into_excel, update_data_into_excel
from api.lib.settings import settings
client = MongoClient(settings.databaseURL)
db = client[settings.databaseName]


class AuthDB:
    @classmethod
    def create_user(cls, data: dict) -> dict:
        collection: Collection = db.get_collection("users")
        res: InsertOneResult = collection.insert_one(data)
        if not res.inserted_id:
            raise HTTPException(detail="Failed to create user. Try again...",
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return cls.get_user_by_id(res.inserted_id)

    @classmethod
    def get_user_by_id(cls, object_id: str) -> dict:
        collection: Collection = db.get_collection("users")
        res: dict = collection.find_one({"_id": ObjectId(object_id)})
        cls._create_key_id_for_user(res)
        return res

    @classmethod
    def get_user_by_username(cls, username: str) -> dict:
        collection: Collection = db.get_collection("users")
        res: dict = collection.find_one({"username": username})
        cls._create_key_id_for_user(res)
        return res

    @staticmethod
    def _create_key_id_for_user(data):
        if data:
            data["id"] = str(data["_id"])
            del data["_id"]


class ReceiptDB:
    @classmethod
    def create_receipt(cls, data: dict):
        append_data_into_excel(data, data.get("section_code"))
        collection: Collection = db.get_collection("receipts")
        if data.get("id") is not None:
            del data["id"]
        res: InsertOneResult = collection.insert_one(data)
        if not res.inserted_id:
            raise HTTPException(detail="Failed to create Receipt. Try again...",
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        return cls.get_receipt_by_id(res.inserted_id)

    @classmethod
    def update_receipt(cls, receipt_id: str, data: dict):
        collection: Collection = db.get_collection("receipts")
        if data.get("id") is not None:
            del data["id"]
        update_data_into_excel(data, data.get("section_code"), data.get("receipt_number"))
        res = collection.update_one({"_id": ObjectId(receipt_id)}, {"$set": data})
        return cls.get_receipt_by_id(receipt_id)

    @classmethod
    def get_receipt_by_receipt_no(cls, receipt_no: str, section_code: str) -> dict:
        collection: Collection = db.get_collection("receipts")
        res: dict = collection.find_one({"receipt_number": receipt_no, "section_code": section_code})
        cls._create_key_id_for_receipt(res)
        return res

    @staticmethod
    def _create_key_id_for_receipt(data):
        if data:
            data["id"] = str(data["_id"])
            del data["_id"]

    @classmethod
    def get_receipt_by_id(cls, receipt_id: str) -> dict:
        collection: Collection = db.get_collection("receipts")
        res: dict = collection.find_one({"_id": ObjectId(receipt_id)})
        cls._create_key_id_for_receipt(res)
        return res

    @classmethod
    def get_all_receipts(cls,section_code:str)->dict:
        collection: Collection = db.get_collection("receipts")
        res: list[dict] = collection.find({"section_code":section_code})
        for i in range(len(res)):
            cls._create_key_id_for_receipt(res[i])
        return res
