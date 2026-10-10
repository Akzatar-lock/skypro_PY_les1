import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    """Фикстура для создания экземпляра класса StringUtils."""
    return StringUtils()


# ---------------------------------------------------------------------------
# Тесты для метода capitalize
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("Тест", "Тест"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_positive(utils, input_str, expected):
    """Позитивные тесты: обычные строки, числа, строки с пробелами."""
    assert utils.capitalize(input_str) == expected


def test_capitalize_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.capitalize("") == ""


def test_capitalize_space_only(utils):
    """Негативный тест: строка из одного пробела."""
    assert utils.capitalize(" ") == " "


def test_capitalize_none(utils):
    """Негативный тест: None вместо строки."""
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# ---------------------------------------------------------------------------
# Тесты для метода trim (удаляет пробелы в начале строки)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro   ", "skypro   "),          # если trim удаляет только слева
    ("   skypro   ", "skypro   "),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_trim_positive(utils, input_str, expected):
    """Позитивные тесты: удаление ведущих пробелов."""
    assert utils.trim(input_str) == expected


def test_trim_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.trim("") == ""


def test_trim_space_only(utils):
    """Негативный тест: строка из пробелов."""
    assert utils.trim(" ") == ""


def test_trim_none(utils):
    """Негативный тест: None вместо строки."""
    with pytest.raises(AttributeError):
        utils.trim(None)


# ---------------------------------------------------------------------------
# Тесты для метода contains
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("Тест", "е", True),
    ("123", "1", True),
    ("04 апреля 2023", "апреля", True),
])
def test_contains_positive(utils, string, symbol, expected):
    """Позитивные тесты: проверка наличия подстроки."""
    assert utils.contains(string, symbol) == expected


def test_contains_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.contains("", "a") is False


def test_contains_none(utils):
    """Негативный тест: None вместо строки."""
    with pytest.raises(TypeError):
        utils.contains(None, "a")


def test_contains_empty_symbol(utils):
    """Негативный тест: пустая подстрока (всегда содержится)."""
    assert utils.contains("SkyPro", "") is True


# ---------------------------------------------------------------------------
# Тесты для метода delete_symbol
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Тест", "т", "Тес"),
    ("123", "2", "13"),
    ("04 апреля 2023", " ", "04апреля2023"),
])
def test_delete_symbol_positive(utils, string, symbol, expected):
    """Позитивные тесты: удаление символа или подстроки."""
    assert utils.delete_symbol(string, symbol) == expected


def test_delete_symbol_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_none(utils):
    """Негативный тест: None вместо строки."""
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")


def test_delete_symbol_empty_symbol(utils):
    """Негативный тест: пустой символ для удаления."""
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"