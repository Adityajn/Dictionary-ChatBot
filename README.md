# Dictionary Bot using Amazon Lex, Amazon Lambda and Oxford Dictionary API
This is a simple dictionary chatbot which tell meaning of any word.

# Requirements:
1. Amazon AWS Account
2. Amazon Lex
3. Amazon Lambda
4. Account at Oxford Dictionary API


# Steps:
1. Create zip of DictionaryBot_Export.json.
2. Import above zip as New Bot into Amazon Lex.
3. Create zip of contents of Lambda Function folder.
4. Create a new function in Amazon Lambda with runtime as python 3.6 and choose lambda_basic_execution as existing role.
5. Upload zip create in Step 2, use handler as "lambda_function.lambda_handler" and then save.
6. Now test your bot through LEX console.
7. Publish your LEX BOT and use Slack communication channel to integrate with slack.


# Integrating with SLACK
[Click this Link and Follow Steps](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-association.html)


# SLACK INVITE LINK
[Click this link to join slack workspace and start interacting with bot](https://join.slack.com/t/dictionarybot/shared_invite/enQtMzM0NjI3NzYxNTQyLWI0MmNmNzI0OTg4OTZhMjRmZTQwODE1ZjM0NzVjYmQwYTc1MDBlZjI3M2EzODE0NjJmYWRlNGMxMzIzY2FlNzY)

# Some Screenshots

![1.png](https://raw.githubusercontent.com/Adityajn/Dictionary-ChatBot/master/ScreenShots/1.png) ![2.png](https://raw.githubusercontent.com/Adityajn/Dictionary-ChatBot/master/ScreenShots/2.png) ![3.png](https://raw.githubusercontent.com/Adityajn/Dictionary-ChatBot/master/ScreenShots/3.png)