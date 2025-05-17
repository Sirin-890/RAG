RAG (Retrieval-Augmented Generation) System
A contextual retrieval and document question-answering system.
Prerequisites

Python 3.10 or higher
Git
Internet connection to download dependencies

Installation and Setup
Clone the Repository
bashgit clone https://github.com/Sirin-890/RAG
cd RAG
Set Up Virtual Environment
Linux/macOS
bashpython3.10 -m venv rag_venv
source rag_venv/bin/activate
Windows
cmdpython -m venv rag_venv
rag_venv\Scripts\activate
Install Dependencies
Once your virtual environment is activated, install the required packages:
bashpip install -r requirements.txt
Running the Application
1. Start the Backend Server
bashpython fast_api.py
Wait until you see confirmation that the contextual retrieval and embedding processes are complete. This may take a few minutes depending on your system and the size of the data.
2. Launch the User Interface
Once the backend is ready, open a new terminal window, activate the virtual environment again, and run:
bashpython ui.py
3. Access the Web Interface
Open your web browser and navigate to:
http://127.0.0.1:7860
The RAG system interface should now be available for you to interact with.
Usage

Enter your questions in the text input field
The system will retrieve relevant context from your documents
You'll receive answers based on the retrieved information

Troubleshooting

If you encounter any dependency issues, ensure you're using Python 3.10
Make sure both the backend server and UI are running simultaneously
Check your firewall settings if you cannot access the web interface

License
[Include license information here]
Contact
[Include contact information here]
