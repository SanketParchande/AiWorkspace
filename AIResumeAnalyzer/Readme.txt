Prerequisite:
    1. Install ollama test cmd > ollama ls
    2. Download Model to use like below using >ollama pull <model_name>
    3. test model response using >ollama run <model_name>
C:\Users\Sanket>ollama ls
NAME                ID              SIZE      MODIFIED
Qwen2.5:3b          357c53fb659c    1.9 GB    37 minutes ago
gemma3:270m         e7d36fb2c3b3    291 MB    About an hour ago
deepseek-r1:1.5b    e0979632db5a    1.1 GB    2 hours ago


1. Clone it
2. install below command in VS Code termina
    pip install -r requirements.txt

3. in terminal run below command to run project
    streamlit run app.py