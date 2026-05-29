# LangChain Experiments at MTL

[![Built by MusicTech Lab](https://musictechlab.io/oss/build-by-musictechlab.io.svg)](https://musictechlab.io)

This project demonstrates how to use the LangChain OpenAI API to translate text from English to Polish.

## Prerequisites

- Python 3.7 or higher
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/musictechlab/mtl-langchain mtl-langchain
    cd mtl-langchain
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

To run the script, use the following command:
```sh
poetry run python main.py