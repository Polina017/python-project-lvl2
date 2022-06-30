from gendiff.gen_diff import generate_diff


def test_generate_diff_flat_json():
    result = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    with open('./tests/fixtures/result.txt') as f:
        assert result == f.read()


def test_generate_diff_flat_yaml():
    result = generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.yaml')
    with open('./tests/fixtures/result.txt') as f:
        assert result == f.read()


def test_generate_diff_unsopported():
    result = generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.json')
    assert result == 'File extension is not supported'


def test_generate_diff_json_tree():
    result = generate_diff('./tests/fixtures/file1.2.json', './tests/fixtures/file2.2.json')
    with open('./tests/fixtures/result2.txt') as f:
        assert result == f.read()


def test_generate_diff_yaml_tree():
    result = generate_diff('./tests/fixtures/file1.2.yaml', './tests/fixtures/file2.2.yaml')
    with open('./tests/fixtures/result2.txt') as f:
        assert result == f.read()


def test_generate_diff_json_plain():
    result = generate_diff('./tests/fixtures/file1.2.json', './tests/fixtures/file2.2.json', 'plain')
    with open('./tests/fixtures/result_plain.txt') as f:
        assert result == f.read()


def test_generate_diff_json_json():
    result = generate_diff('./tests/fixtures/file1.2.json', './tests/fixtures/file2.2.json', 'json').strip()
    with open('./tests/fixtures/result_json.txt') as f:
        assert result == f.read()


def test_generate_diff_json_plain_with_number():
    result = generate_diff('./tests/fixtures/file1.3.json', './tests/fixtures/file2.3.json', 'plain')
    with open('./tests/fixtures/result_plain2.txt') as f:
        assert result == f.read()
