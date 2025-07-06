from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()  

def generate_pet_name(animal_type, pet_color,pet_gender,pet_character):
    # Initialize the Gemini LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)  # "gemini-2.0-flash" does not exist

    # Create the prompt template
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type","pet_color","pet_gender","pet_character"],
        template="I have a {animal_type} pet and I want a cool name for it. It is {pet_color} color and gender is {pet_gender}. the character of it is {pet_character} . Suggest me cool names for my pet."
    )

    # Define the RunnableSequence using LCEL
    name_chain = prompt_template_name | llm

    # Invoke the chain
    response = name_chain.invoke({"animal_type": animal_type, "pet_color":pet_color, "pet_gender": pet_gender, "pet_character":pet_character})

    return response.content  

if __name__ == "__main__":
    print(generate_pet_name("cat","black and white","female","calm"))