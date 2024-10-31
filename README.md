
# Twitch Fortune Teller Bot

This Twitch bot connects to a specified Twitch chat and serves as a fortune teller. It responds to specific keywords or commands with random fortunes or predictions, making interactions fun and interactive. The bot loads responses from text files (`fortunes.txt` and `predictions.txt`), making it easy to update responses without modifying the code.

It can be used for free, but the bot sometimes times out. To use it continuously, consider deploying it on a cloud service.

## Features
- Responds to common Twitch chat interactions, like `hi`, `HeyGuys`, `<3`, and `Kissahomie`.
- Offers random fortunes and predictions when users type phrases like "🔮" or "Tell me my future!".
- Easily customizable by editing `fortunes.txt` and `predictions.txt`.

## Setup

### Prerequisites
- **Python 3.x**
- **Twitch Account** and a Twitch bot account with an OAuth token.
- **Text files**: `fortunes.txt` and `predictions.txt` in the project directory, each containing one line per fortune/prediction.

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/Twitch-Fortune-Teller-Bot.git
cd Twitch-Fortune-Teller-Bot
```

### Step 2: Get an OAuth Token for Your Bot
Generate an OAuth token for your bot account. You can use [Twitch Token Generator](https://twitchtokengenerator.com/) or follow the [Twitch Authentication Guide](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth) to create one.

### Step 3: Set Up Environment Variables

**Using a `.env` file (Recommended):**

1. Create a `.env` file in the project directory to securely store your sensitive information.
2. Inside `.env`, add the following lines (replace with your actual details):
   ```plaintext
   TOKEN="YOUR_OAUTH_TOKEN"        # OAuth token for your Twitch bot
   CHANNEL="YOUR_CHANNEL_NAME"     # Twitch channel name where the bot connects
   NICKNAME="YOUR_BOT_NICKNAME"    # The bot's username
   ```
3. Ensure `.env` is included in `.gitignore` to prevent uploading it to GitHub.

### Step 4: Update `bot.py` to Load Environment Variables
1. Install `python-dotenv` to manage environment variables from `.env`:
   ```bash
   pip install python-dotenv
   ```
2. Modify `bot.py` to load these variables by adding the following code at the top:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   TOKEN = os.getenv("TOKEN")
   CHANNEL = os.getenv("CHANNEL")
   NICKNAME = os.getenv("NICKNAME")
   ```

### Step 5: Run the Bot
Ensure `fortunes.txt` and `predictions.txt` are in the directory, then start the bot:
```bash
python bot.py
```

## Customizing Fortunes and Predictions
Edit the `fortunes.txt` and `predictions.txt` files to customize responses. Each line in these files represents a single fortune or prediction, which the bot will select randomly.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
