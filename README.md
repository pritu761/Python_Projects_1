# Python Learning Projects Collection

This repository contains a comprehensive collection of Python learning projects covering various aspects of programming including GUI development, web scraping, games, and application development.

## 📁 Project Structure

### 🔐 Authentication & Security
- **`login/`** - Web-based login interface with modern UI
- **`password-manager-start/`** - Tkinter-based password manager with generation capabilities

### 🎮 Games
- **`turtle-crossing-start/`** - Frogger-style crossing game using Python Turtle
- **`turtle-race-start/`** - Turtle racing game
- **`etch-a-sketch-start/`** - Digital etch-a-sketch implementation
- **`quiz-game-start/`** - Console-based quiz game
- **`quizzler-app-start/`** - GUI quiz application with trivia questions

### 🌐 Web Applications & APIs
- **`Web Scrapping/`** - Collection of web scraping projects
- **`kanye-quotes-start/`** - API-powered Kanye West quotes app
- **`issoverhead-start/`** - ISS tracking application
- **`stock-news-normal-start/`** - Stock news monitoring system
- **`flight-deals-start/`** - Flight price tracking application
- **`birthday-wisher-normal-start/`** - Automated birthday reminder system

### 🎨 Creative Projects
- **`hirst-painting-start/`** - Hirst-style dot painting generator
- **`flash-card-project-start/`** - Language learning flashcard app

### 🕰️ Productivity
- **`pomodoro-start/`** - Pomodoro timer application

### 🖥️ Object-Oriented Programming
- **`oop-coffee-machine-start/`** - OOP-based coffee machine simulator

### 📊 Data Processing
- **`day-25-start/`** - Data analysis projects
- **`day-25-us-states-game-start/`** - Interactive US states learning game
- **`NATO-alphabet-start/`** - NATO phonetic alphabet converter
- **`Mail+Merge+Project+Start/`** - Automated mail merge system

### 🌐 Web Development
- **HTML/CSS Projects:**
  - `2.1+Heading+Element/` - HTML heading elements tutorial
  - `2.2+Paragraph+Element/` - HTML paragraph elements
  - `2.3+Void+Elements/` - HTML void elements
  - `2.4+Movie+Ranking+Project/` - Movie ranking webpage
  - `3.0+List+Elements/` - HTML list elements
  - `3.1+Nesting+and+Indentation/` - HTML structure best practices
  - `3.2+Anchor+Elements/` - HTML anchor/link elements
  - `3.3+Image+Elements/` - HTML image implementation
  - `3.4+Birthday+Invite+Project/` - Birthday invitation webpage
  - `5.1+Adding+CSS/` - CSS basics
  - `5.3+CSS+Selectors/` - CSS selector tutorial
  - `5.4+Color+Vocab+Project/` - CSS color vocabulary project
  - `6.0+CSS+Colors/` - Advanced CSS colors
  - `6.1+Font+Properties/` - CSS typography
  - `6.3+CSS+Box+Model/` - CSS box model tutorial
  - `6.4+Motivation+Meme+Project/` - Motivational meme webpage

## 🐛 Recent Bug Fixes

### Fixed Issues:
1. **Kanye Quotes App**: Fixed incorrect `canvas.config()` usage → changed to `canvas.itemconfig()`
2. **Password Manager**: 
   - Fixed password field not clearing after saving
   - Removed redundant file.close() call (handled by context manager)
   - Added clearing of existing password before generating new one
3. **Turtle Crossing Game**: Fixed undefined `self.speed` attribute → changed to `self.car_speed`
4. **Web Scraping**: Fixed syntax error in temporary code runner file
5. **Flight Deals**: Fixed syntax error in configuration endpoint string
6. **Turtle Crossing**: Changed exact position check (==) to range check (>=) for better game mechanics

## 🚀 Getting Started

### Prerequisites
```bash
# Required Python packages
pip install tkinter
pip install requests
pip install beautifulsoup4
pip install pyperclip
pip install pandas
pip install selenium
pip install python-dotenv
```

### Running Individual Projects

#### Password Manager
```bash
cd password-manager-start
python main.py
```

#### Kanye Quotes App
```bash
cd kanye-quotes-start
python main.py
```

#### Turtle Crossing Game
```bash
cd turtle-crossing-start
python main.py
```

#### Quizzler App
```bash
cd quizzler-app-start
python main.py
```

#### Web Scraping Projects
```bash
cd "Web Scrapping"
python main.py
```

## 📖 Project Details

### Password Manager (`password-manager-start/`)
A secure password manager built with Tkinter that features:
- Random password generation with customizable complexity
- Secure storage in local text file
- Automatic clipboard copying
- Input validation and user confirmations

**Key Features:**
- Generate passwords with letters, numbers, and symbols
- Save website credentials securely
- Clear form fields after successful save
- Copy generated passwords to clipboard automatically

### Kanye Quotes App (`kanye-quotes-start/`)
A fun GUI application that fetches random Kanye West quotes from an API:
- Uses Kanye REST API for quote fetching
- Attractive GUI with background images
- Click button to get new quotes
- Error handling for API requests

### Turtle Crossing Game (`turtle-crossing-start/`)
A Frogger-style game built with Python Turtle graphics:
- Player controls a turtle crossing busy roads
- Randomly generated cars with increasing difficulty
- Level progression system
- Collision detection
- Score tracking

**Game Mechanics:**
- Use UP arrow key to move turtle
- Avoid cars moving across the screen
- Reach the top to advance to next level
- Cars move faster with each level

### Quizzler App (`quizzler-app-start/`)
An interactive quiz application with GUI:
- Fetches questions from external API
- True/False question format
- Visual feedback (green/red) for answers
- Score tracking
- Modern UI design

### Web Scraping Projects (`Web Scrapping/`)
Collection of web scraping examples:
- Hacker News scraping for top articles
- Beautiful Soup usage examples
- Requests library demonstrations
- HTML parsing techniques

## 🎯 Learning Objectives

These projects cover:
- **GUI Development**: Tkinter applications with event handling
- **API Integration**: REST API consumption and JSON processing
- **Game Development**: Basic game mechanics and user interaction
- **Web Scraping**: HTML parsing and data extraction
- **File I/O**: Reading and writing data persistently
- **Error Handling**: Robust exception management
- **Object-Oriented Programming**: Class design and inheritance
- **Data Structures**: Working with lists, dictionaries, and custom objects

## 🛠️ Development Environment

- **Python Version**: 3.8+
- **IDE**: Compatible with PyCharm, VS Code, or any Python IDE
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## 📝 Code Quality Standards

All projects follow:
- PEP 8 style guidelines
- Proper error handling
- Clear variable naming
- Modular code structure
- Comprehensive comments

## 🤝 Contributing

This is a learning repository. Feel free to:
- Report bugs
- Suggest improvements
- Add new features
- Enhance documentation

## 📄 License

This project is created for educational purposes. Individual projects may use different APIs or resources with their own terms of service.

## 🎓 Course Information

These projects are part of a comprehensive Python learning curriculum covering:
- Python fundamentals
- GUI programming
- Web development
- API integration
- Game development
- Data processing
- Object-oriented programming

## 📞 Support

For questions or issues:
1. Check the individual project README files
2. Review the code comments for implementation details
3. Ensure all required packages are installed
4. Verify Python version compatibility

---

**Happy Coding! 🐍✨**