def recepie_generation(user_input, word_count):
    """
    Function to generate a blog based on user input and word count.
    Parameters:
        user_input (str): The topic for the blog.
        word_count (int): The desired number of words for the blog.
    Returns:
        str: The generated blog content.
    """
    # Display a message while the blog is being generated
    st.write("### Generating your recepie...")
    st.write(f"While I work on creating your blog, here's a little joke to keep you entertained:\n\n** (get_joke())**")
    # Start a chat session with the Input tople and sword count
    chat_session
    history = [
        {
            "role": "user",
            "parts": [
                f"Write a recepie based on the input topic: {user_input} and number of words: {word_count}\n",
            ],
        }
    ]
    try:
        # Generate a response for the new Input
        response = chat_session.send_message(user_input)
        st.success(" Your recepie is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating blog: (e)")
        return None