# Week 9 - Introduction to AI Agents and Tool Use

## Objective

The objective of this task was to understand the basic concept of AI agents and tool use. I created a simple AI agent that can use a Python calculator tool when mathematical calculations are required.

## AI Agent

An AI agent is a system that can understand a user's request, decide what action is needed, use available tools when necessary, and provide a final response.

The basic workflow is:

User → AI Agent → Tool → Result → AI Agent → Final Response

## Tool Created

I created a simple calculator tool using Python.

The calculator accepts a mathematical expression and returns the calculated result.

For example:

125 * 48

The calculator returns:

6000

## How Tool Use Works

The user sends a request to Gemini. Gemini determines whether the calculator tool is useful for the request. If a calculation is required, Gemini can use the Python calculator function and use the returned result to generate the final response.

## Example

User:

What is 125 * 48?

Calculator result:

6000

AI Agent response:

125 * 48 = 6,000

## When Tool Use Is Helpful

Tool use is helpful when an AI needs to perform an operation or access information that is better handled by an external function or system.

Examples include:

- Mathematical calculations
- Searching for information
- Accessing databases
- Retrieving current information
- Performing external actions

## When a Plain Prompt Is Enough

A plain prompt is enough when the task only requires the language model to generate or explain information.

Examples include:

- Explaining a concept
- Summarizing text
- Generating an explanation
- Answering general questions

## Conclusion

This task demonstrated the basic concept of AI tool use. The Gemini model was provided with a Python calculator function and could use the function when a mathematical calculation was required.