# Quizzler Quiz App

An interactive desktop quiz application built with Python's Tkinter that fetches trivia questions from an external API and provides a modern GUI for answering True/False questions.

## 🧠 Features

- **Dynamic Questions**: Fetches questions from external trivia API
- **Interactive GUI**: Modern interface with visual feedback
- **Real-time Scoring**: Track your score as you progress
- **Visual Feedback**: Green/red background indicates correct/incorrect answers
- **Question Tracking**: Shows current question and total score
- **Clean UI**: Professional-looking interface with consistent theming

## 🚀 Getting Started

### Prerequisites
```bash
pip install requests  # For API calls (if using dynamic questions)
```

### Running the Application
```bash
python main.py
```

## 📖 How to Use

1. **Start the Quiz**: Run the application to begin
2. **Read Questions**: Questions appear in the center canvas
3. **Answer**: Click the ✓ (True) or ✗ (False) buttons
4. **Get Feedback**: Background turns green (correct) or red (incorrect)
5. **Track Progress**: See your score update in real-time
6. **Complete Quiz**: Continue until all questions are answered

## 📁 Project Structure

```
quizzler-app-start/
├── main.py           # Main application entry point
├── question_model.py # Question class definition
├── quiz_brain.py     # Quiz logic and question management
├── ui.py            # GUI implementation
├── data.py          # Question data source
└── images/          # UI images (true/false buttons)
    ├── true.png
    └── false.png
```

## 🔧 Technical Details

### Core Components

#### Question Model (`question_model.py`)
```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

#### Quiz Brain (`quiz_brain.py`)
- Manages question progression
- Handles answer checking
- Tracks score and question count
- HTML entity decoding for clean text display

#### User Interface (`ui.py`)
- Tkinter-based GUI
- Canvas for question display
- Button interactions
- Visual feedback system

### Key Features

#### Answer Validation
```python
def check_answer(self, user_answer):
    correct_answer = self.current_question.answer
    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        return True
    else:
        return False
```

#### Visual Feedback System
```python
def give_feedback(self, is_right):
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")
    self.window.after(1000, self.get_question)
```

## 🎨 UI Design

### Color Scheme
- **Theme Color**: `#375362` (Dark blue-gray)
- **Correct Answer**: Green background
- **Incorrect Answer**: Red background
- **Default**: White canvas background

### Layout Components
- **Score Display**: Top-right corner
- **Question Canvas**: Center (300x300 pixels)
- **Answer Buttons**: Bottom row (True/False)
- **Typography**: Arial font, bold italic styling

## 🧪 Question Management

### Question Processing
- **HTML Decoding**: Converts HTML entities to readable text
- **Progress Tracking**: Monitors question position in quiz
- **Dynamic Display**: Updates question text and formatting

### Data Structure
```python
question_data = [
    {"question": "The earth is round", "correct_answer": "True"},
    {"question": "Python is a snake", "correct_answer": "False"},
    # ... more questions
]
```

## 🎯 Learning Objectives

This project teaches:
- **Object-Oriented Programming**: Multiple classes working together
- **GUI Development**: Tkinter interface design and event handling
- **Data Management**: Structuring and processing question data
- **User Experience**: Visual feedback and intuitive interactions
- **API Integration**: Fetching and processing external data
- **State Management**: Tracking quiz progress and scores

## 🔮 Possible Enhancements

### Functionality Improvements
- [ ] **Multiple Choice Questions**: Expand beyond True/False
- [ ] **Difficulty Levels**: Easy, Medium, Hard questions
- [ ] **Categories**: Different subject areas
- [ ] **Timer**: Add time pressure to questions
- [ ] **High Scores**: Save and display best scores
- [ ] **Question Review**: Show correct answers at the end

### UI/UX Enhancements
- [ ] **Sound Effects**: Audio feedback for answers
- [ ] **Animations**: Smooth transitions between questions
- [ ] **Progress Bar**: Visual indicator of quiz completion
- [ ] **Custom Themes**: Different color schemes
- [ ] **Question Images**: Visual questions support
- [ ] **Accessibility**: Screen reader support, keyboard navigation

### Technical Improvements
- [ ] **Database Storage**: Save questions and scores persistently
- [ ] **API Integration**: Live trivia question fetching
- [ ] **Configuration**: Customizable quiz settings
- [ ] **Statistics**: Detailed performance analytics
- [ ] **Multiplayer**: Compare scores with friends

## 🐛 Debugging Guide

### Common Issues

1. **Images Not Loading**
   ```bash
   # Ensure images directory exists with required files
   images/true.png
   images/false.png
   ```

2. **Questions Not Displaying**
   - Check `question_data` in `data.py`
   - Verify question format matches expected structure
   - Ensure proper HTML decoding

3. **Button Not Responding**
   - Verify button command bindings
   - Check if quiz has remaining questions
   - Ensure proper event handling

### Testing Checklist
- [ ] All questions display correctly
- [ ] Score updates properly
- [ ] Visual feedback works
- [ ] Quiz ends gracefully
- [ ] No runtime errors

## 🏗️ Architecture

### Design Patterns
- **Model-View-Controller**: Separation of data, UI, and logic
- **Observer Pattern**: UI updates based on quiz state changes
- **Factory Pattern**: Question object creation

### Code Organization
- **Modular Design**: Each component has single responsibility
- **Clean Interfaces**: Clear communication between classes
- **Error Handling**: Graceful degradation on failures

## 📊 Performance Considerations

- **Memory Usage**: Efficient question loading and disposal
- **Response Time**: Immediate UI feedback
- **Scalability**: Can handle large question sets
- **Resource Management**: Proper image and widget handling

## 🤝 Contributing

Contribution ideas:
- Add new question categories
- Implement difficulty progression
- Create custom themes
- Add sound effects
- Improve accessibility
- Write unit tests

## 📄 License

Educational project - feel free to use and modify for learning purposes!