# Week 2 - Large Language Model (LLM) API

## 1. Introduction to LLMs

A Large Language Model (LLM) is an artificial intelligence model trained on a very large amount of text data. It can understand and generate human-like text.

Examples of LLMs include Gemini, GPT, Claude, and Llama.

LLMs can be used for:
- Question answering
- Text generation
- Summarization
- Translation
- Coding assistance
- Chatbots

---

## 2. How an LLM Generates Text

An LLM generates text by predicting what token is likely to come next based on the input it receives.

For example:

Input:
"Today the weather is"

The model may predict:
"sunny"

It then continues predicting the next token until it produces a complete response.

The model does not simply search for a stored answer. It generates a response based on patterns learned during training.

---

## 3. Tokenization

Tokenization is the process of breaking text into smaller units called tokens.

A token can be:
- A complete word
- Part of a word
- A punctuation mark
- A special character

For example, a sentence such as:

"Hello, how are you?"

is converted into tokens before being processed by the model.

Tokens are important because LLMs process and count input and output using tokens rather than simply counting words.

---

## 4. Next-Token Prediction

LLMs generate text through next-token prediction.

The model receives the existing text and predicts the most appropriate next token.

For example:

"The capital of Nepal is"

The model predicts:

"Kathmandu"

The newly generated token becomes part of the context, and the model predicts the next token.

This process continues until the response is complete.

---

## 5. Context Window

The context window is the maximum amount of information that a model can consider during a request.

The context can include:
- The user's prompt
- Previous conversation
- System instructions
- Other input information

A larger context window allows the model to work with longer documents and conversations.

If the amount of information exceeds the model's context limit, some information may need to be removed or truncated.

---

## 6. System Prompt

A system prompt provides instructions that guide how an AI model should behave or respond.

For example:

"You are a helpful AI teacher. Explain technical concepts using simple language."

This instruction can influence the style and behavior of the model's response.

A system prompt is different from an ordinary user prompt because it provides higher-level instructions for the model.

---

## 7. Temperature

Temperature is a parameter traditionally used to control the randomness of generated responses.

A lower temperature generally produces:
- More predictable responses
- More consistent wording
- Less variation

A higher temperature generally produces:
- More varied responses
- More creative wording
- Less predictable outputs

The exact effect depends on the model and API being used.

### Current Gemini API observation

The latest Gemini models have changed how sampling parameters such as temperature are handled. Therefore, an old temperature experiment using previous Gemini model versions may not work with a new API key.

For this project, temperature was studied conceptually rather than forcing an unsupported parameter.

---

# 8. API Experiment

## Experiment 1: Basic Prompt

Prompt:

"Explain artificial intelligence."

The model provided a general explanation of artificial intelligence.

## Experiment 2: Specific Prompt

Prompt:

"You are an AI teacher. Explain artificial intelligence to a beginner. Use very simple language and give one real-world example."

The second response was more specific and beginner-friendly because the prompt provided additional instructions.

### Observation

Changing the wording and level of detail in a prompt can significantly influence the generated response.

A more specific prompt can help the model understand:
- The intended audience
- The desired style
- The amount of detail
- The type of example required

---

# 9. What I Learned

Through this experiment, I learned how to:

1. Create and use a Gemini API key.
2. Install the Google GenAI Python SDK.
3. Connect a Python program to the Gemini API.
4. Send prompts to an LLM.
5. Receive and display generated responses.
6. Compare responses produced by different prompts.
7. Understand tokenization and next-token prediction.
8. Understand the context window.
9. Understand the purpose of system prompts.
10. Understand the concept of temperature and how current model/API changes can affect its use.

---

# 10. Files Created

The Week 2 LLM API project contains:

- `llm_experiment.py` - Basic Gemini API request
- `prompt_experiment.py` - Prompt wording experiment
- `notes.md` - LLM theory and experiment observations