Benefits:
    We can fine tuning on the llm model i.e Llama.
    It is developed by meta
    Llama has launched 4 models:
        3.1
        3.2
        3.3
        4 Scout
    Login to Llama
    As we cannot download llama model on computer, we can use 3rd party org which helps user to work on them like Ollama, HuggingFace, Groq, Openrouter

    -So goto HuggingFace.co -> Login 
        -> Models->Search 'Meta' we can see 17650 models available to integrate.
    -Upon opening 'meta-llama/Llama-3.1-8B-Instruct' i.e. https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
    -It will ask for 'You need to agree to share your contact information to access this model' so open form and get approval from Meta
    -Fill the form and submit to get Affiliation:
        Your request to access this repository has been submitted and is awaiting a review from the repository authors. You can check the status of all your access requests in your settings.
        If approved, you'll get access to all 17 repositories in the Meta's Llama 3.1 models & evals Gating Group Collection, including this one.


    To check approval:
        HuggingFace-> ProfileIcon-> Settings -> LeftMenu GatedRepositories
            Here you can see the Approval status
    
    Create API Keys:
        Settings -> Acess Tokens-> Confirm
        Make sure to select Full Permission or we can change permission by cliking 3 dots-> Edit Permission -> Save Token
        Using this Token key we can use LLama model.

    Open Google Colab and Mount Drive.
        1.Runtime-> Change runtime-> Select GPU -> Save
        2.Mount Drive
        3.Install pip install --upgrade transformers
                  pip install huggingface_hub
        4. Login to HF HuggingFace
        5. Run the code
            It will start downloading the model about the 16gb for the simple prompt
             
        6. 