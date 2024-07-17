# Genie Mind Bot

<div style="text-align:center;">
  <img src="img/Genie%20Mind.png" alt="Genie Mind Bot Icon" width="250" height="250">
</div>

Genie Mind Bot simplifies tweets and provides sentiment analysis using MindsDB and Hugging Face Transformers.

## Features

- Simplifies tweets to make them easier to understand
- Analyzes the sentiment of tweets

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/GenieMindBot.git
   cd GenieMindBot

2. **Create and activate a virtual environment:**

    ```bash

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

4. **Set up environment variables:**

    Create a .env file in the project directory and add your environment variables:

    ```bash

    TWITTER_CONSUMER_KEY=your_new_bot_api_key
    TWITTER_CONSUMER_SECRET=your_new_bot_api_secret
    TWITTER_ACCESS_TOKEN=your_new_bot_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_new_bot_access_token_secret
    MINDSDB_URL=http://localhost:47334

5. **Run the Flask server:**

    ```bash
    python run.py
