from fastapi import APIRouter, Request
from utils.templates import templates

from utils.translation import translation_service, get_user_language

router = APIRouter()

@router.get("/category", name="category")
async def category(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/category.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/plant", name="plant")
async def plant(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/plant.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/history", name="history")
async def history(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/history.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/communication", name="communication")
async def communication(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/communication.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/search", name="search")
async def search(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/search.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/art", name="art")
async def art(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/art.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/glade", name="glade")
async def glade(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/glade.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )

@router.get("/details", name="details")
async def details(request: Request):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    return templates.TemplateResponse(
        name="user/details.html",
        context={
            "request": request,
            "translations": translations,
            "current_language": language,
        }
    )
