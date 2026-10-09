# Week 10 – Rebuilding a Chatbot Using LangChain

## Objective

The objective of this task was to learn how AI frameworks simplify the development of applications powered by Large Language Models (LLMs). I rebuilt my Week 3 command-line chatbot using LangChain and added conversation memory.

## Framework Used

* **LangChain:** Framework for developing applications powered by language models.
* **Google Gemini:** LLM used to generate chatbot responses.
* **Python:** Programming language used to implement the chatbot.
* **Google GenAI integration for LangChain:** Connects LangChain with the Gemini model.

## Implementation

The chatbot was implemented using `ChatGoogleGenerativeAI` from `langchain_google_genai`.

The implementation includes:

* Gemini model configuration.
* A system instruction defining the chatbot as a friendly programming tutor.
* User input through the command line.
* AI-generated responses.
* Conversation history to retain context across messages.
* An exit command to terminate the application.
* Exception handling for API errors.

## Additional Feature: Conversation Memory

Conversation memory was implemented by storing user messages and AI responses in a conversation history list.

This allows the chatbot to use earlier messages when answering follow-up questions.

For example:

**User:** My name is Sovana.

**User:** What is my name?

**Chatbot:** Your name is Sovana.

## Comparison: Raw API vs. LangChain

| Week 3 – Raw Gemini API                              | Week 10 – LangChain                                                                           |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Uses the Google GenAI SDK directly.                  | Uses LangChain's Gemini integration.                                                          |
| Directly manages communication with Gemini.          | Uses LangChain's model interface.                                                             |
| Implements conversation handling in the application. | Also implements conversation history in the application.                                      |
| Requires direct interaction with the provider SDK.   | Provides a framework interface that can simplify integration with different models and tools. |

## Results

The chatbot successfully connected to Gemini through LangChain and generated responses to user questions. The conversation memory feature was tested by providing a name and asking the chatbot to recall it in a later message.

## Conclusion

This task provided practical experience with LangChain and framework-based LLM application development. Rebuilding the chatbot demonstrated how a framework can simplify model integration while allowing features such as conversation history to be implemented in Python.
