# Typhoon Holiday Information Scraper and Chatbot

This project is a Python-based application that scrapes typhoon holiday information from the [DGPA website](https://www.dgpa.gov.tw/typh/daily/nds.html) and interacts with users through a chatbot interface.

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

You can install the necessary packages using pip:

```bash
pip install requests beautifulsoup4 ollama
```

### Usage

1. **Run the Script:**
   - Execute the `main.py` script to start the chatbot interface.

```bash
python main.py
```

2. **Interaction:**
   - The chatbot will provide typhoon holiday information based on the latest scraped data. It responds to user queries, and if a question is outside the scope of the data, it will indicate that it does not have the information.

## Project Structure

- `main.py`: The main script that handles web scraping, data processing, and chatbot interaction.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/JT-427/TyphoonHolidayChatBot/blob/master/LICENSE) file for details.
