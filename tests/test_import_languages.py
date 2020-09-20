from src.database.models import Language
from src.database.base import SessionLocal
from src.languages.importer import WordsImporter
from tests.fixtures.dictionary import importer, importer_with_session
from tests.fixtures.db import db, session
from tests.utils.db import fetch_all_polish_words


def test_import_english(importer: WordsImporter):
    words = importer.from_file('resources/english.txt')

    assert len(words) == 9999


def test_import_english_to_db_without_exception(importer_with_session: WordsImporter):
    importer_with_session.to_db()
    words = fetch_all_polish_words(importer_with_session.destination)

    assert len(words) == 9999
    assert str(words[0].word) == 'of'