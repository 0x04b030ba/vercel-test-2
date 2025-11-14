# Discord Bot with Frontend

This project consists of a simple Discord bot that can be controlled via commands and a frontend hosted on Vercel. The bot is running on a separate platform (e.g., Heroku), while the frontend is deployed on Vercel.

## Files

- `bot.py`: The main bot code (runs on Heroku/VPS)
- `index.html`: The frontend HTML file served by Vercel
- `api/status.js`: Serverless function on Vercel to check the bot's status
- `requirements.txt`: Python dependencies for the bot
- `vercel.json`: Configuration file for Vercel

## How to Run the Bot

1. Set up the bot on Heroku or your preferred platform.
2. Use the provided `bot.py` script to start the bot.
3. Deploy the frontend to Vercel using the steps below.

## Deploy to Vercel

1. Install Vercel CLI: `npm install -g vercel`
2. Deploy: Run `vercel` in this directory to deploy the project.
