import pytest
from src.YamlDataReader import YamlDataReader

class TestYamlDataReader:
    
    @pytest.fixture()
    def file_and_expected_data(self):
        
        text = (
            "- Иванов Иван Иванович:\n"
            "  математика: 67\n"
            "  литература: 100\n"
            "  программирование: 91\n"
            "- Петров Петр Петрович:\n"
            "  математика: 78\n"
            "  химия: 87\n"
            "  социология: 61\n"
        )
        
        data = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91),
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61),
            ],
        }
        
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_expected_data, tmpdir):
        
        p = tmpdir.mkdir("test_yaml").join("test.yaml")
        p.write_text(file_and_expected_data[0], encoding="utf-8")
        return str(p), file_and_expected_data[1]

    def test_read(self, filepath_and_data):
        
        file_path, expected = filepath_and_data
        result = YamlDataReader().read(file_path)
        assert result == expected
