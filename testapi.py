API_KEY = "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"
import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = API_KEY

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Tell me something interesting",
        },
    ],
)
print(completion.choices[0].message.content)