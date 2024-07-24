import pytest
from unittest.mock import patch
from main import fetch_html, process_data
import requests_mock

@pytest.fixture
def html_content():
    return """
    <html>
        <body>
            <table>
                <tr>
                    <td>地區</td>
                    <td>狀態。</td>
                </tr>
                <tr>
                    <td>台北</td>
                    <td>放假。</td>
                </tr>
                <tr>
                    <td>台中</td>
                    <td>正常上班。</td>
                </tr>
                <tr>
                    <td>info</td>
                    <td>info</td>
                </tr>
            </table>
        </body>
    </html>
    """

def test_fetch_html():
    test_url = "http://example.com"
    expected_output = b"<html></html>"

    with requests_mock.Mocker() as m:
        m.get(test_url, content=expected_output)
        result = fetch_html(test_url)
        assert result == expected_output, "The fetched HTML content does not match the expected output."

def test_process_data(html_content):
    expected_output = "台北:放假，  明天尚未公布。\n台中:正常上班，  明天尚未公布。\n"
    result = process_data(html_content)
    assert result == expected_output, "The processed data does not match the expected output."

def test_ollama_chat():
    pass