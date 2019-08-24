# Whole Note

## Team Members

- Poulad Ashraf Pour
- Matthew Grahlman
- Joseph Harrison-Lim
- Sandra Petkovic

![wholenote]

## Getting Started

1. Set environment variables

```bash
cat > .env
```

```profile
JIRA_USERNAME="user@example.org" # it's actually an email!
JIRA_PASSWORD=""
JIRA_TOKEN="" # Get your token at: https://id.atlassian.com/manage/api-tokens
``` 

> Download Selenium Driver for Chrome and put it on the `PATH`. https://sites.google.com/a/chromium.org/chromedriver/downloads

## Run the applications

1. Run the Models Server:

```sh
rasa run -m models --enable-api
```

2. Run the Actions Server:

```sh
rasa run actions
```

3. Run a voice client to connect to the Models Server:

```sh
python voice/voiceclient.py
```

[wholenote]: ./images/wholenote.png
