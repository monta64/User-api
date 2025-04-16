from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.models import User, Conversation, Message, BolResponse, Feedback , SQLModel

config = context.config
target_metadata = SQLModel.metadata

def run_migrations_online():
    connectable = create_async_engine(settings.DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            include_schemas=True
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()