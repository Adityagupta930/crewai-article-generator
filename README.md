# 🚀 CrewAI Article Generator

![CrewAI Article Generator](https://via.placeholder.com/800x400/4a90e2/ffffff?text=🚀+CrewAI+Article+Generator)

An AI-powered article generation tool using CrewAI agents with a beautiful Streamlit interface.

## ✨ Features

- 🤖 **Dual AI Agents**: Research + Writing specialists working together
- 🎨 **Multiple Styles**: From casual blogs to academic papers
- ⚡ **Lightning Fast**: Articles generated in seconds
- 📊 **Smart Analytics**: Track your content creation journey
- 🔄 **Trending Topics**: Always know what's hot right now

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd crewai-article-generator
```

2. Install dependencies:
```bash
pip install -r requirnment.txt
```

3. Set up environment variables:
Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Usage

### Run with Streamlit UI:
```bash
streamlit run streamlit_app.py
```

Or use the run script:
```bash
python run.py
```

### Command Line Usage:
```bash
python app/crew.py
```

## 📁 Project Structure

```
crewai-article-generator/
├── app/
│   ├── agent.py      # AI agents definition
│   ├── task.py       # Task definitions
│   └── crew.py       # Crew orchestration
├── streamlit_app.py  # Web interface
├── run.py           # Launch script
├── .env             # Environment variables
└── requirnment.txt  # Dependencies
```

## 🎯 How It Works

![How It Works](https://via.placeholder.com/600x300/007acc/ffffff?text=AI+Agents+Working+Together)

1. **Choose a Topic**: Select from trending topics or enter your own
2. **Configure Settings**: Customize length, style, and features
3. **Launch Generation**: Let AI agents work their magic
4. **Enjoy Your Article**: Read, download, and share your content

## 🤖 AI Agents

- **Research Agent**: Uncovers groundbreaking technologies and trends
- **Writer Agent**: Crafts comprehensive and engaging articles

## 📝 License

This project is licensed under the MIT License.