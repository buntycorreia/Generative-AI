from openai import OpenAI
import openai
import streamlit as st
def Call_OpenAi(City):
    oapi_key=st.secrets['OpenAi']['api_key']
    client = OpenAI(api_key=oapi_key)

    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {
            "role": "system",
            "content": "You are a vacation planner.\nYou are planning vacation for family of 2 adults and 2 kids.\nEvery vacation plan will be for 3 days starting from 09:00 AM to 07:00PM.\nGive hours wise schedule.\nEnsure to consider important tourist place and shopping places, museum and park."
            },
            {
            "role": "user",
            "content": "Create a Vacation plan  for following city "+City+"."
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        answer = response.choices[0].message.content

        st.write(answer)
    except openai.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass