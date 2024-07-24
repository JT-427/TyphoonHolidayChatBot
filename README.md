# Typhoon Holiday Information Scraper and Chatbot

This project is a Python-based application that scrapes typhoon holiday information from the [DGPA website](https://www.dgpa.gov.tw/typh/daily/nds.html) and interacts with users through a chatbot interface. The project also includes tests for key functionalities using `pytest`.

## Features

- **Web Scraping:** Utilizes BeautifulSoup to extract data from the specified webpage.
- **Data Processing:** Processes the scraped data to format it for chatbot responses.
- **Chatbot Integration:** Uses the Ollama API to interact with users, providing typhoon holiday information based on the latest data.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `ollama`
  - `pytest`
  - `requests_mock`

You can install the necessary packages using pip:

```bash
pip install requests beautifulsoup4 ollama pytest requests_mock
```

### Usage

1. **Run the Script:**
   - Execute the `main.py` script to start the chatbot interface.

```bash
python main.py
```

2. **Interaction:**
   - The chatbot will provide typhoon holiday information based on the latest scraped data. It responds to user queries, and if a question is outside the scope of the data, it will indicate that it does not have the information.

## Testing

The project includes a test suite to verify the functionality of core components. The tests are written using `pytest` and can be found in `test_main.py`. To run the tests, use the following command:

```bash
pytest test_main.py
```

### Test Coverage

- **test_fetch_html:** Tests the `fetch_html` function by mocking a network response.
- **test_process_data:** Tests the `process_data` function using sample HTML content.
- **test_ollama_chat:** Placeholder for future tests related to the chatbot interaction.

## Project Structure

- `main.py`: The main script that handles web scraping, data processing, and chatbot interaction.
- `test_main.py`: The test script for unit testing the core functionalities using `pytest`.

## Demo

Below is a screenshot of the chatbot interface in action:

![Chatbot Demo](https://github.com/JT-427/TyphoonHolidayChatBot/blob/master/demo.png)

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/JT-427/TyphoonHolidayChatBot/blob/master/LICENSE) file for details.
