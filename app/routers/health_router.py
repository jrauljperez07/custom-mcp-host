from fastapi import APIRouter
from controllers.health_controller import get_server_status

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
def health_check():
    return get_server_status()
