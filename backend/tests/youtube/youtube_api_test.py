import os

import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()

API_KEY = os.getenv("YOUTUBE_KEY")

if not API_KEY:
    raise RuntimeError("YOUTUBE_KEY was not found in the file .env")

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "q": "fake news",
    "type": "video",
    "maxResults": 5,
    "key": API_KEY,
}

response = requests.get(url, params=params)

print("Status:", response.status_code)

data = response.json()

console = Console()

# Research information
console.print(
    Panel(
        f"Pesquisa: {params['q']}\n"
        f"Total de resultados: {data['pageInfo']['totalResults']}\n"
        f"Resultados nesta página: {data['pageInfo']['resultsPerPage']}\n"
        f"Próxima página: {data.get('nextPageToken', 'Não disponível')}",
        title="Informações da Pesquisa",
    )
)

# Results
for index, item in enumerate(data["items"], start=1):
    video_id = item["id"]["videoId"]
    snippet = item["snippet"]

    video_url = f"https://www.youtube.com/watch?v={video_id}"

    console.print(
        Panel(
            f"[bold]ID:[/bold] {video_id}\n\n"
            f"[bold]Título:[/bold] {snippet['title']}\n\n"
            f"[bold]Canal:[/bold] {snippet['channelTitle']}\n"
            f"[bold]Publicado:[/bold] {snippet['publishedAt']}\n\n"
            f"[bold]URL:[/bold] {video_url}",
            title=f"Vídeo {index}",
        )
    )
