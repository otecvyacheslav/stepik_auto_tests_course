import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^ - это смайл", "\nперенос строки")
    yield
    print(":3 - это смайл", "\nперенос строки")


@pytest.fixture()
def very_important_fixture():
    print(":) - это смайл", "\nперенос строки")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р - это смайл", "\nперенос строки")


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        assert "^_^"

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        assert "^_^"
