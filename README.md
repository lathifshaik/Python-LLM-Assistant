# 🤖 Python-LLM Assistant

Python-based programming assistant powered by LLAMA 3.2 via Ollama, designed to provide assistance with Python-related queries, code generation, and testing. This terminal-based chatbot offers dynamic and human-like interactions tailored to programming needs. ✨

## Short Explanation:

### Approach to Design:
When I started this project, my primary goal was to build a dynamic, Python-focused programming assistant capable of helping users with Python-related queries. Initially, I prototyped the assistant in Jupyter Notebook, which was great for testing basic functionality but felt limiting for interactive, real-time conversations. To better express the assistant's potential, I transitioned to a terminal-based chatbot. This decision allowed me to implement features like rolling memory, dynamic typing effects, and engaging greetings to create a more human-like interaction.

The assistant was designed to focus specifically on Python programming. This meant tailoring the responses to include executable code snippets, concise explanations, and even mock data for demonstration. By narrowing the scope to Python, I could ensure the assistant provided depth and clarity for programming-related questions.

### Assumptions Made:
1. **Programming Focus**: I assumed that most user queries would be programming-related, specifically Python. Non-programming queries are handled gracefully but without extensive depth.
2. **Memory Constraints**: To balance performance and context retention, I decided to store only the last two exchanges (user queries and assistant responses). This rolling memory approach ensures the assistant can handle follow-up questions without consuming excessive resources.
3. **Error Recovery**: Knowing that API calls to the model could fail occasionally, I built a retry mechanism with three attempts to ensure robustness.

### Challenges Faced:
1. **Maintaining Context**: Early iterations of the assistant failed to retain context, which disrupted follow-up questions. The rolling memory strategy solved this issue.
2. **Verbose Responses**: Initial responses were overly detailed and not user-friendly. I refined the model's system prompt to ensure concise, actionable answers.
3. **Transitioning to Terminal**: Moving from Jupyter to the terminal required rethinking interaction design and debugging in a new environment, but it improved the overall user experience.

### Future Improvements:
If I had more time, I would expand the assistant to:
- Support multiple programming languages (e.g., JavaScript, Java).
- Allow saving and loading session history for long-term context retention.
- Handle more advanced queries, like working with APIs or visualizing data.
- Incorporate feedback mechanisms for users to rate or refine responses.

This project represents a significant learning experience and a practical demonstration of the potential for combining large language models with Python programming to create an intelligent, engaging assistant.



## ✨ Features

### 🐍 Dynamic Python Programming Assistant
- Specializes in Python-related queries and solutions
- Generates concise, executable Python code snippets
- Simulates real-world scenarios using mock data for code testing
- Provides clear explanations with step-by-step guidance

### 🧠 Intelligent Memory Management
- Stores the last two user queries and assistant responses
- Balances efficient memory usage with conversation context retention
- Enables coherent follow-up discussions and iterative queries

### 🛡️ Robust Error Handling
- Includes a retry mechanism (up to three attempts) for API call failures
- Transparently reports errors and indicates retries in progress
- Ensures graceful recovery from transient issues, like network errors

### 💫 Engaging and Interactive Experience
- Terminal-based interface supports natural conversational flow
- Features random programming-themed greetings to enhance user engagement
- Incorporates dynamic typing effects for a human-like interaction experience

## 📋 Prerequisites

Before you begin, ensure you have:

- 🐍 Python 3.8 or later
  - Download from [python.org](https://python.org)
- 📦 pip (Python Package Manager)
  - Verify with: `pip --version`
- 🚀 [Ollama](https://ollama.com)
  - For running the LLAMA 3.2 model locally

## 🚀 Installation

### 1. Install Ollama
```bash
# 🍎 macOS/Linux:
curl -fsSL https://ollama.com/install.sh | sh

# 🪟 Windows:
# Download from https://ollama.com/download
```

### 2. Download LLAMA 3.2 Model
```bash
ollama run llama3.2
```

### 3. Clone and Setup
```bash
https://github.com/lathifshaik/Python-LLM-Assistant.git
cd Python-LLM-Assistant
pip install -r requirements.txt
```

## 🛠️ Development Process

### 📊 Evolution Journey
- Started as a Jupyter Notebook prototype
- Evolved into a terminal-based chatbot for better interaction
- Refined through multiple iterations based on usage patterns

### 🎯 Design Philosophy
- Focus on Python expertise
- Prioritize user experience
- Maintain simplicity with power
- Ensure robust error handling

## 🎮 Usage

### Start the Assistant
```bash
python duckypy.py
```

### 💬 Sample Interaction
```
You: Find the user with the highest total transaction amount from the CSV.

Processing your query...

Assistant:

Here's an example of how you can solve this problem using Python and the pandas library.

**Problem Statement**

Given a CSV file containing transactions for each user, find the user with the highest total transaction amount.

**Example Data**

Let's assume our CSV file (`transactions.csv`) contains the following data:

| User ID | Transaction Date | Transaction Amount |
| --- | --- | --- |
| 1    | 2022-01-01      | 100.00          |
| 1    | 2022-01-02      | 200.00          |
| 2    | 2022-01-03      | 50.00           |
| 3    | 2022-01-04      | 300.00          |
| ...  | ...              | ...              |

**Solution**

```python
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('transactions.csv')

# Group the transactions by User ID and calculate the total transaction amount for each user
user_transactions = df.groupby('User ID')['Transaction Amount'].sum().reset_index()

# Find the user with the highest total transaction amount
max_transaction_user = user_transactions.loc[user_transactions['Transaction Amount'].idxmax()]

print("The user with the highest total transaction amount is:")
print(f"User ID: {max_transaction_user['User ID']}")
print(f"Total Transaction Amount: ${max_transaction_user['Transaction Amount']:.2f}")


**Explanation**

1. We load the CSV file into a pandas DataFrame using `pd.read_csv()`.
2. We group the transactions by User ID and calculate the total transaction amount for each user using `df.groupby()` and `.sum()`.
3. We find the user with the highest total transaction amount using `user_transactions.loc[]` and indexing on the maximum value.

**Test Data**

Create a CSV file (`transactions.csv`) containing the following data:
csv
User ID,Transaction Date,Transaction Amount
1,2022-01-01,100.00
1,2022-01-02,200.00
2,2022-01-03,50.00
3,2022-01-04,300.00
4,2022-01-05,400.00

Run the code above to find the user with the highest total transaction amount.

Let me know if you have any questions or need further assistance!


### Exit
```bash
exit
```

## 🏗️ Project Structure
```
python-llm/
├── duckypy.py        # 🎯 assistant
├── requirements.txt    # 📦 Dependencies
└── README.md          # 📚 Documentation
```

## 🚀 Future Enhancements

- 🌐 Multi-language programming support
- 💾 Session history persistence
- 📊 Data visualization tools
- 🔄 Enhanced error recovery
- 🎨 Custom themes and styling

## ⚖️ License

This project is a personal development effort and is not currently licensed for redistribution. All rights reserved. ©️ 2024

## 🙏 Acknowledgments

- 🚀 [Ollama](https://ollama.com) for the amazing LLAMA 3.2 runtime
- 🐍 Python Community for inspiration
- 💡 All users who provided valuable feedback

## 🎯 Conclusion

This assistant combines the power of natural language processing with programming expertise to create a unique and helpful coding companion. Through its focus on Python, intelligent memory management, and engaging user experience, it serves as a robust solution for programming assistance. 🚀✨

---
Made with ❤️ by a passionate developer
