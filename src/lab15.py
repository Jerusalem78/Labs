from fastapi import FastAPI, Query, Body, HTTPException
from pydantic import BaseModel
import wikipedia
import uvicorn

app = FastAPI()
favorites_db = {}
wikipedia.set_lang("ru")


class PageContentResponse(BaseModel):
    title: str
    summary: str
    url: str

class SearchRequest(BaseModel):
    query: str
    results_count: int = 5

class SearchResult(BaseModel):
    title: str
    summary: str

class SearchResponse(BaseModel):
    results: list[SearchResult]

class FavoriteResponse(BaseModel):
    user_id: str
    favorites: list[str]

@app.get("/page/{page_title}", response_model=PageContentResponse)
async def get_page_by_path(page_title: str):
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        return {
            "title": page.title,
            "summary": page.summary,
            "url": page.url
        }
    except wikipedia.exceptions.PageError:
        try:
            search_results = wikipedia.search(page_title)
            if search_results:
                page = wikipedia.page(search_results[0])
                return {
                    "title": page.title,
                    "summary": page.summary,
                    "url": page.url
                }
            raise HTTPException(status_code=404, detail="Page not found")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

@app.get("/search", response_model=SearchResponse)
async def search_pages(
    query: str = Query(min_length=2),
    results_count: int = Query(5, ge=1, le=10)
):
    try:
        search_results = wikipedia.search(query, results=results_count)
        results = []
        for title in search_results:
            try:
                summary = wikipedia.summary(title, sentences=2)
                results.append({"title": title, "summary": summary})
            except:
                continue
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/search", response_model=SearchResponse)
async def search_pages_post(request: SearchRequest = Body()):
    try:
        search_results = wikipedia.search(request.query, results=request.results_count)
        results = []
        for title in search_results:
            try:
                summary = wikipedia.summary(title, sentences=2)
                results.append({"title": title, "summary": summary})
            except:
                continue
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/favorites/{user_id}", response_model=FavoriteResponse)
async def add_favorite(user_id: str, page_title: str = Body(embed=True)):
    if user_id not in favorites_db:
        favorites_db[user_id] = []
    
    if page_title not in favorites_db[user_id]:
        favorites_db[user_id].append(page_title)
    
    return {
        "user_id": user_id,
        "favorites": favorites_db[user_id]
    }

@app.delete("/favorites/{user_id}", response_model=FavoriteResponse)
async def remove_favorite(
    user_id: str, 
    page_title: str = Query()
):
    if user_id in favorites_db and page_title in favorites_db[user_id]:
        favorites_db[user_id].remove(page_title)
    
    return {
        "user_id": user_id,
        "favorites": favorites_db.get(user_id, [])
    }


if __name__ == '__main__':
    print(Query())