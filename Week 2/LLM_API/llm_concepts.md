# Basic LLM Concepts

## 1. Tokens

Tokens are the small pieces of text that an LLM processes. A token can be a complete word, part of a word, punctuation mark, or sometimes a space-related piece.

For example, the sentence "I love AI" is divided into tokens before it is processed by the model.

LLMs do not directly process sentences in the same way humans do. They convert text into tokens and then use those tokens to understand the input and generate the next tokens.

The number of tokens is also important because models have a maximum number of tokens they can process.

## 2. Context Window

The context window is the amount of information an LLM can consider at one time during a conversation or API request.

It includes things such as the system instructions, user prompts, previous conversation messages, and the model's generated response, depending on the API and model.

A larger context window allows the model to work with more text, such as longer documents or larger conversations. However, the model still has a fixed limit, so very large inputs may exceed the available context.

## 3. System Prompts

A system prompt is an instruction given to an LLM that defines how the model should behave.

For example, a system prompt can tell the model to act as a teacher, answer in a particular style, or provide simple explanations.

The system prompt is different from the user's normal question because it provides higher-level instructions for the model's behavior.

For example:

System prompt:
"You are a helpful programming tutor. Explain concepts in simple language."

User prompt:
"What is a Python function?"

The system prompt guides the way the model should answer the user's question.

## Conclusion

Tokens are the pieces of text processed by an LLM, the context window determines how much information the model can handle at one time, and system prompts provide instructions that guide the model's behavior.