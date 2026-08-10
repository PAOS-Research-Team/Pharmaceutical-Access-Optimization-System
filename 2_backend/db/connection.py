"""
Database connection management
--------------------------------
Owns the DB connection pool lifecycle. Swap the driver here (e.g.
asyncpg for PostgreSQL) without touching any other layer.
"""

_pool = None  # Module-level connection pool, set on startup.


async def init_db():
    """
    Open the connection pool once at application startup.
    Replace this stub with a real driver call, e.g.:
        global _pool
        _pool = await asyncpg.create_pool(dsn=settings.DATABASE_URL)
    """
    global _pool
    _pool = "CONNECTION_POOL_PLACEHOLDER"


async def close_db():
    """Gracefully close the connection pool on application shutdown."""
    global _pool
    _pool = None


def get_pool():
    """Accessor used by db/models.py so only one pool ever exists."""
    if _pool is None:
        raise RuntimeError("Database pool not initialized. Call init_db() first.")
    return _pool
