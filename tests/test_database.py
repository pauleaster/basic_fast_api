# test_database.py

import pytest
from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

# Define a fixture for database URLs
@pytest.fixture(params=['.env', '.env.test'])
def database_url(request):
    # Load the respective .env file
    load_dotenv(request.param, override=True)
    return os.getenv("DATABASE_URL")

# Define a fixture to create and yield an SQLAlchemy engine and metadata, then dispose of the engine
@pytest.fixture
def engine_metadata(database_url):
    assert database_url, "DATABASE_URL is not set."
    engine = create_engine(database_url)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    yield engine, metadata
    engine.dispose()

def test_database_tables(engine_metadata):
    _, metadata = engine_metadata
    expected_tables = {'contacts'}
    assert expected_tables.issubset(metadata.tables.keys()), f"Expected tables {expected_tables} not found."

def test_contacts_table_schema(engine_metadata):
    _, metadata = engine_metadata
    contacts_table = metadata.tables['contacts']
    expected_columns = {'id', 'name', 'email', 'phone', 'message', 'submitted_at'}
    table_columns = {column.name for column in contacts_table.columns}
    assert expected_columns == table_columns, "Contacts table does not have the expected schema."

