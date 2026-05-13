```
bell_ai_product/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point; initializes FastAPI and mounts routers
│   ├── routers/             # Route handlers (v1, v2, etc.)
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── api.py       # Main router that includes all versioned endpoints
│   │       └── endpoints/   # Individual feature routes (users.py, items.py)
│   ├── core/                # Global config (settings, security, constants)
│   ├── crud/                # CRUD (Create, Read, Update, Delete) database logic
│   ├── db/                  # Database connection, sessions, and migrations
│   ├── models/              # SQLAlchemy (or other ORM) database models
│   ├── schemas/             # Pydantic models for data validation/serialization
│   └── services/            # Pure business logic (optional, but keeps CRUD thin)
├── tests/                   # Pytest files
├── .env                     # Environment variables
├── Dockerfile               # Containerization configuration
└── requirements.txt         # Project dependencies
```