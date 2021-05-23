from fastapi import FastAPI
from urls import urls


app = FastAPI(title='Автомастерская')
app.include_router(urls)

