from pydantic import BaseModel
from fastapi import File, Form, UploadFile


class Profile(BaseModel):
    questionAmount: str = ""
    currentRole: str = ""
    currentModel: str = ""
    openaiKey: str = ""
    openaiOrganization: str = ""
    openaiBase: str = ""
    azureKey: str = ""
    azureBase: str = ""
    openaiVersion: str = ""
    deploymentName: str = ""
    notionKey: str = ""
    proxy: str = ""


class Icon(BaseModel):
    id: int
    icon: str


class AnswerQuestion(BaseModel):
    id: int
    language: str
    answer: str


class AddNoteData(BaseModel):
    language: str
    questionType: str
    noteName: str = Form()
    files: list[UploadFile] = File(default=None)
    notionId: str = Form(default=None)
