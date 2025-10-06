# build-a-coding-agent
This is a basic agent I wrote when learning how to build a coding agent from scratch. It is based on the following two articles:
* [How to Build an Agent](https://ampcode.com/how-to-build-an-agent)
* [How to Build Coding Agents](https://docs.together.ai/docs/how-to-build-coding-agents)

## Gemini API key

It invokes the Gemini models(`gemini-2.5-flash` by default) using Gemini API. The [free tier](https://ai.google.dev/gemini-api/docs/rate-limits) is sufficient for testing purpose.

Follow this [doc](https://ai.google.dev/gemini-api/docs/api-key) to get the Gemini API key and add `GEMINI_API_KEY` environment variable. Don't forget to apply it in your current console session.

## Install uv

This project is manged by uv. Follow this [guide](https://docs.astral.sh/uv/getting-started/installation/) to install uv.

## Run the agent

Under the root of this project, run:
```shell
% uv run build-a-coding-agent     
```

It will bring up the agent CLI.

## Example

Here is an example:

```
Chat with the coding agent (type 'exit' to quit)

You: What is the Python version used by this project?
Warning: there are non-text parts in the response: ['thought_signature'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
Agent: I cannot directly tell you the Python version used by this project. However, I can help you look for clues. Often, the Python version is specified in files like `requirements.txt`, `pyproject.toml`, `.python-version`, or a `Dockerfile`.

Would you like me to list the files in the current directory so you can look for such a file?
You: yes
tool: list_files({})

tool: read_file({'path': '.python-version'})

Warning: there are non-text parts in the response: ['thought_signature'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
Agent: The Python version used by this project is 3.13.
You:  Create a congrats.py script that rot13-decodes the following string 'Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!' and prints it
tool: edit_file({'path': 'congrats.py', 'old_str': '', 'new_str': "import codecs\n\nencoded_string = 'Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!'\ndecoded_string = codecs.decode(encoded_string, 'rot13')\n\nprint(decoded_string)\n"})

Agent: I have created the `congrats.py` script. It contains the Python code to rot13 decode the provided string and print it.
You: exit
```

## License

MIT