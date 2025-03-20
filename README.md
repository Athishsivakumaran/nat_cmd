# 🖥️ Nat: Natural Language Terminal Assistant

Hey everyone! 👋

Ever struggled to remember the right terminal command? You open ChatGPT, search online, or scroll through notes—just to run a simple command. Well, those days are OVER!

## ✨ Introducing Nat: Your Natural Language Terminal Assistant

Just type `nat` followed by your request in plain English, and boom—you get the correct terminal command instantly!

🔹 Want to list files? `nat show all files`  
🔹 Need to go up a directory? `nat go back`  
🔹 Searching for a file? `nat find cat.py`  
🔹 Check disk usage? `nat show disk usage`

No more memorizing complex commands! Just type what you need, and let Nat handle the rest.

### 🚀 Run Terminal Commands in Plain English!

Tired of remembering complex terminal commands? **Nat** allows you to type commands in natural language and execute them instantly!

## ✨ Features

- 🧠 **AI-Powered Command Conversion**
- 🔄 **Seamless Terminal Integration**
- ⚡ **Fast & Lightweight**
- ⏳ **Saves Time & Boosts Productivity**

---

## 📌 How It Works

Simply type a command using **natural language** with the nat prefix:

```bash
nat how many lines are in cat.py
```

🔹 **Output:**

```bash
Command: wc -l cat.py
```
(And it runs automatically!)

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/nat-cli.git
cd nat-cli
```

### 2️⃣ Install Dependencies

Make sure you have **Python 3.x** installed. Then, install dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up the Terminal Alias

Open your terminal and add this function :

```bash
nat() {
  cmd=$(python /Users/athish/Automation_scripts/cmd_NLP/main.py "$@" | tail -n 1);
  echo "Command: $cmd";
  eval "$cmd";
}
```

## 💡 Usage Examples

```bash
nat list all files in the current directory # ls
nat go to the parent directory # cd ..
nat find cat.py # find . -name "cat.py"
nat show disk usage # df -h
```

## 🔗 Dependencies

* Python 3.x
* Ollama AI



## 🤝 Contributing

Want to improve **Nat**? Fork this repo and submit a pull request!

🔗 **Follow Me on LinkedIn**:https://www.linkedin.com/in/athish-sivakumaran/

🌟 **Give this repo a star if you found it useful!** 🚀
