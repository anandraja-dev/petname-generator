import langchain_helper as lch
import streamlit as st
import re

st.title("🐾 Pet Name Generator")

# --- Sidebar Inputs ---
with st.sidebar:
    st.header("Pet Details")

    # Pet selection
    pets = ['Select any pet', "Cat", "Dog", "Fish", "Cow", "Hamster"]
    user_animal_type = st.selectbox("What is your pet?", pets)

    # Initialize inputs
    pet_color = ""
    gender = "Select gender"
    extra_note = ""

    if user_animal_type != "Select any pet":
        # Dynamic label for color
        color_label = f"Color of your {user_animal_type.lower()}"
        user_pet_color = st.text_input(color_label)

        # Gender selection
        user_pet_gender = st.selectbox("Select gender", ["Select gender", "Male", "Female"])

        # Optional trait input
        extra_note = st.text_input(f"Describe your {user_animal_type.lower()} (optional)")

        # Submit button
        submit = st.button("Generate Name")
    else:
        st.warning("⚠️ Please choose a pet from the dropdown.")

# --- Validation & Output ---
if user_animal_type != "Select any pet" and 'submit' in locals() and submit:
    if not user_pet_color:
        st.sidebar.warning(f"⚠️ Please enter the color of your {user_animal_type.lower()}.")
    elif user_pet_gender == "Select gender":
        st.sidebar.warning("⚠️ Please select a gender.")
    else:
        with st.spinner(f"✅ Generating name for your {user_pet_color.lower()} {user_pet_gender.lower()} {user_animal_type.lower()}..."):

        # Call the LLM
            raw_response = lch.generate_pet_name(user_animal_type, user_pet_color, user_pet_gender, extra_note)
    
            # Start formatting the response
            st.markdown("### ✨ Name Suggestions")
    
            if not isinstance(raw_response, str):
                st.error("⚠️ Unexpected response format. Expected a string.")
            else:
                # Safely split using markdown headers like **Header**
                try:
                    categories = re.split(r"\*\*(.*?)\*\*", raw_response)
                    intro = categories[0].strip()
    
                    if intro:
                        st.markdown(f"**{intro}**")
    
                    for i in range(1, len(categories), 2):
                        section_title = categories[i].strip()
                        section_text = categories[i + 1].strip()
                        suggestions = re.findall(r"\* (.+)", section_text)
    
                        st.markdown(f"#### {section_title}")
                        for suggestion in suggestions:
                            st.markdown(f"- {suggestion}")
    
                    # Handle conclusion if present
                    if "Ultimately," in raw_response:
                        final_note = raw_response.split("Ultimately,", 1)[1].strip()
                        st.markdown("---")
                        st.markdown(f"💡 *Ultimately,* {final_note}")
    
                except Exception as e:
                    st.error(f"⚠️ Error while formatting response: {e}")
