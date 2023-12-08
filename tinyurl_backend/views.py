from fastapi import APIRouter

from .tasks import sleepyTime

router = APIRouter()

@router.get("/")
async def test():
    sleep = sleepyTime.delay()
    
    print('test')
    return {'test': 'test'}
