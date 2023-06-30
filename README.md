# http-healthcheck-notifier
Script to run HTTP healthchecks and send a notification if they fail

## Usage
1. Create a Telegram Bot and get its token.
2. Start a chat with the bot and write `/start`
3. Retrieve your user chat id by starting a conversation with https://t.me/chat_id_echo_bot
4. Set the following env vars:
    ```shell
    export TELEGRAM_TOKEN="<your token>"
    export TELEGRAM_DESTINATION_CHAT_ID="<your destination chat ID>"
    export URL_TO_CHECK="<your URL to check>"
    ```
5. Start the bot
    ```shell
    docker compose build
    docker compose up -d
    ```

Image is available at https://hub.docker.com/r/csp33/http-healthcheck-notifier