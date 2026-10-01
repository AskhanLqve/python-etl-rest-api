from fastapi import FastAPI, HTTPException
from etl_pipeline import run_etl

app = FastAPI(
    title="Crypto Analytics ETL & REST API",
    description="Сервис для автоматической обработки крипто-данных и предоставления аналитики через REST API",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Добро пожаловать в Crypto ETL API! Перейдите на /docs для просмотра Swagger."}

@app.get("/api/v1/market-summary")
def get_market_summary():
    """Эндпоинт запускает ETL-пайплайн и возвращает обработанные аналитические данные."""
    try:
        data = run_etl()
        return {
            "success": True,
            "count": len(data),
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка выполнения ETL-процесса: {str(e)}")