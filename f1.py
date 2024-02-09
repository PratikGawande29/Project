# import streamlit as st
# # import openai

# # Set your OpenAI API key here
# # openai.api_key = "your_openai_api_key_here"

# # Title of the app
# st.title('Topic Chatbot')

# # Function to get bot response
# def get_bot_response(topic, user_input):
#     try:
#         prompt = f"Topic: {topic}\n{user_input}\n"
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=prompt,
#             max_tokens=150
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print("An error occurred:", str(e))
#         return "I'm sorry, I couldn't generate a response at the moment. Please try again later."

# # Login page
# st.sidebar.markdown("<h1 style='text-align: center; color: red; font-size:55px'>Login</h1>", unsafe_allow_html=True)
# username = st.sidebar.text_input('Username')
# password = st.sidebar.text_input('Password', type='password')
# login_button = st.sidebar.button('Login', key=hash('login_button'))


# # Check login credentials
# if login_button:
#     if st.sidebar.button('Logout', key=hash('logout_button')):
#         username = ""
#         password = ""
#     if username == 'u' and password == 'u':
#         st.sidebar.success('Logged in as: ' + username)
#         # Text input field for user input
#         # st.sidebar.markdown("<hr>", unsafe_allow_html=True)
        
#         user_input_left, _, user_input_right = st.columns([1, 0.5, 1])
#         with user_input_left:
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
            
#             st.markdown("<h1 style='text-align: center; color: green; font-size:35px'>USER 1</h1>",unsafe_allow_html=True)
#             user_input_1 = st.text_area('You:', height=300, key=hash('user_input_1'))
#             send_button_1 = st.button('Send', key=hash('send_button_1'))
#             if send_button_1 and user_input_1.strip() != '':
#                 bot_response = get_bot_response("Health Insurance", user_input_1)
#                 st.text_area('Bot:', value=bot_response, height=300, max_chars=None, key=hash('bot_response_1'))
        
#         with user_input_right:
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.markdown("<h1 style='text-align: center; color: green; font-size:35px'>USER 2</h1>",unsafe_allow_html=True)

#             user_input_2 = st.text_area('You:', height=300, key=hash('user_input_2'))
#             send_button_2 = st.button('Send', key=hash('send_button_2'))
#             if send_button_2 and user_input_2.strip() != '':
#                 bot_response = get_bot_response("Health Insurance", user_input_2)
#                 st.text_area('Bot:', value=bot_response, height=300, max_chars=None, key=hash('bot_response_2'))
#     else:
#         st.sidebar.error('Incorrect username or password')

# # Info about the chatbot

# # st.sidebar.info('This is a simple chatbot focused on topic, built using OpenAI and Streamlit.')





import streamlit as st
# import openai

# Set your OpenAI API key here
# openai.api_key = "your_openai_api_key_here"

# Title of the app
st.title('Topic Chatbot')

# Function to get bot response
def get_bot_response(topic, user_input):
    try:
        prompt = f"Topic: {topic}\n{user_input}\n"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("An error occurred:", str(e))
        return "I'm sorry, I couldn't generate a response at the moment. Please try again later."
emma_conversation = []
turbo_conversation = []

# User input and file uploader for Emma
with st.sidebar:
    with st.expander("Emma"):
        emma_user_input = st.text_area('You:', height=100, key=hash('emma_user_input'))
        emma_file_input = st.file_uploader('Upload File', type=['txt', 'pdf'], key=hash('emma_file_input'))

        # Check if user input is not empty or file is uploaded
        if st.button('Send', key=hash('emma_send_button')) and (emma_user_input.strip() != '' or emma_file_input is not None):
            if emma_file_input:
                # Process the uploaded file
                file_contents = emma_file_input.getvalue()
                emma_user_input += "\n" + file_contents.decode("utf-8")
            
            # Add user input to Emma's conversation
            emma_conversation.append(('user', emma_user_input))

            # Generate bot response for Emma
            emma_bot_response = get_bot_response("Health Insurance", emma_user_input)

            # Add bot response to Emma's conversation
            emma_conversation.append(('bot', emma_bot_response))

# User input and file uploader for Turbo
with st.sidebar:
    with st.expander("Turbo"):
        turbo_user_input = st.text_area('You:', height=100, key=hash('turbo_user_input'))
        turbo_file_input = st.file_uploader('Upload File', type=['txt', 'pdf'], key=hash('turbo_file_input'))

        # Check if user input is not empty or file is uploaded
        if st.button('Send', key=hash('turbo_send_button')) and (turbo_user_input.strip() != '' or turbo_file_input is not None):
            if turbo_file_input:
                # Process the uploaded file
                file_contents = turbo_file_input.getvalue()
                turbo_user_input += "\n" + file_contents.decode("utf-8")
            
            # Add user input to Turbo's conversation
            turbo_conversation.append(('user', turbo_user_input))

            # Generate bot response for Turbo
            turbo_bot_response = get_bot_response("Health Insurance", turbo_user_input)

            # Add bot response to Turbo's conversation
            turbo_conversation.append(('bot', turbo_bot_response))

# Display conversations side by side
col1, col2 = st.columns(2)

with col1:
    with st.expander("Emma's Conversation"):
        for sender, message in emma_conversation:
            if sender == 'user':
                st.text_area('You:', value=message, height=100, max_chars=None, key=hash('emma_user_input_display'))
            elif sender == 'bot':
                st.text_area('Bot:', value=message, height=100, max_chars=None, key=hash('emma_bot_response_display'))

with col2:
    with st.expander("Turbo's Conversation"):
        for sender, message in turbo_conversation:
            if sender == 'user':
                st.text_area('You:', value=message, height=100, max_chars=None, key=hash('turbo_user_input_display'))
            elif sender == 'bot':
                st.text_area('Bot:', value=message, height=100, max_chars=None, key=hash('turbo_bot_response_display'))


# user_input = st.text_area('You:', height=100, key=hash('user_input'))
# file_input = st.file_uploader('Upload File', type=['txt', 'pdf'], key=hash('file_input'))

# # Check if user input is not empty or file is uploaded
# if st.button('Send', key=hash('send_button')) and (user_input.strip() != '' or file_input is not None):
#     if file_input:
#         # Process the uploaded file
#         file_contents = file_input.getvalue()
#         user_input += "\n" + file_contents.decode("utf-8")
    
#     # Display user input
#     # st.text_area('You:', value=user_input, height=100, max_chars=None, key=hash('user_input_display'))

#     # Generate bot response
#     bot_response = get_bot_response("Health Insurance", user_input)

#     # Display bot response
#     st.text_area('Bot:', value=bot_response, height=100, max_chars=None, key=hash('bot_response_display'))

# user_input_left, _, user_input_right = st.columns([1,1, 1])
# with user_input_left:
#     st.markdown("<h1 style='text-align: center; color: grey; font-size:35px'>USER 1</h1>", unsafe_allow_html=True)
#     user_input_1 = st.text_area('You:', height=400, key=hash('user_input_1'))
#     file_input_1 = st.file_uploader('Upload File', type=['txt', 'pdf'], key=hash('file_input_1'))
#     send_button_1 = st.button('Send', key=hash('send_button_1'))
#     if send_button_1 and (user_input_1.strip() != '' or file_input_1 is not None):
#         if file_input_1:
#             # Process the uploaded file
#             file_contents = file_input_1.getvalue()
#             user_input_1 += "\n" + file_contents.decode("utf-8")
#         bot_response = get_bot_response("Health Insurance", user_input_1)
#         st.text_area('Bot:', value=bot_response, height=300, max_chars=None, key=hash('bot_response_1'))

# with user_input_right:
#     st.markdown("<h1 style='text-align: center; color: grey; font-size:35px'>USER 2</h1>", unsafe_allow_html=True)
#     user_input_2 = st.text_area('You:', height=400, key=hash('user_input_2'))
#     file_input_2 = st.file_uploader('Upload File', type=['txt', 'pdf'], key=hash('file_input_2'))
#     send_button_2 = st.button('Send', key=hash('send_button_2'))
#     if send_button_2 and (user_input_2.strip() != '' or file_input_2 is not None):
#         if file_input_2:
#             # Process the uploaded file
#             file_contents = file_input_2.getvalue()
#             user_input_2 += "\n" + file_contents.decode("utf-8")
#         bot_response = get_bot_response("Health Insurance", user_input_2)
#         st.text_area('Bot:', value=bot_response, height=300, max_chars=None, key=hash('bot_response_2'))
