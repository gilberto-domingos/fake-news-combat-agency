from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app):
    origins = [
        "https://fakenewscombat.com",
        "https://www.fakenewscombat.com",
        "http://localhost:4200",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "https://fake-news-combat-agency.onrender.com"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
