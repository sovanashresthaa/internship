# Week 3 – CLI LLM Chatbot

## 1. Objective

The objective of this task was to build a command-line chatbot using a Large Language Model (LLM) API. The chatbot was developed using Google's Gemini API and Python. The task also focused on understanding system prompts, conversation history, and model generation parameters.

## 2. LLM API Used

Google Gemini API was used to develop the chatbot.

The Python package used was:

`google-genai`

The chatbot uses the Gemini Flash Lite model for generating responses.

## 3. System Prompt

A system prompt was added to give the chatbot a specific role and personality.

The chatbot was instructed to behave as a friendly programming tutor and explain programming concepts clearly and simply. It was also instructed to use examples when helpful and explain concepts step by step when the user is confused.

The system prompt also instructs the chatbot to use plain text without Markdown formatting or asterisks.

## 4. Conversation History

Conversation history was implemented using a Gemini chat session. This allows the chatbot to remember previous messages during the current conversation.

For example, when the user says:

"My name is Sovana."

and later asks:

"What is my name?"

the chatbot can remember the previous message and respond that the user's name is Sovana.

This allows the chatbot to support multiple turns of conversation instead of treating every message as an independent request.

## 5. Temperature Experiment

Temperature controls the variability of the model's generated responses.

The same prompt was tested using temperature values of 0 and 1.

At temperature 0, the responses were more predictable and consistent. At temperature 1, the responses showed greater variation and creativity.

Therefore, increasing the temperature generally allows more varied responses, while a lower temperature produces more predictable responses.

## 6. Max Output Tokens Experiment

The max_output_tokens parameter controls the maximum amount of text that the model can generate.

The same prompt was tested using 50 and 300 maximum output tokens.

With 50 tokens, the response was shorter and was cut off before the explanation was completed. With 300 tokens, the model had more space to provide a longer and more complete response.

Therefore, increasing max_output_tokens allows the model to generate longer responses, while a smaller value limits the response length.

## 7. Final Parameters

The final chatbot uses:

* Model: Gemini Flash Lite
* Temperature: 0.5
* Maximum output tokens: 500

A temperature of 0.5 provides a balance between predictable and varied responses. A maximum of 500 output tokens gives the chatbot enough space for useful explanations without producing unnecessarily long responses.

## 8. Features Implemented

The final chatbot includes:

* Gemini API integration
* Command-line user input
* AI-generated responses
* System prompt and chatbot personality
* Conversation history
* Multi-turn conversation
* Exit command
* Temperature configuration
* Maximum output token configuration
* Plain-text responses

## 9. Conclusion

The Week 3 task successfully demonstrated how to build a command-line chatbot using an LLM API. The implementation showed how system instructions can control chatbot behavior and how conversation history allows the model to maintain context across multiple turns. Experiments with temperature and maximum output tokens also demonstrated how model parameters affect the generated responses.
