# Password Manager

A secure password manager built with Python's Tkinter GUI framework that helps users generate, store, and manage passwords for different websites.

## 🔐 Features

- **Random Password Generation**: Creates secure passwords with letters, numbers, and symbols
- **Automatic Clipboard Copy**: Generated passwords are automatically copied to clipboard
- **Data Persistence**: Stores passwords in a local text file
- **Input Validation**: Ensures all required fields are filled before saving
- **User Confirmation**: Asks for confirmation before saving credentials
- **Form Auto-Clear**: Automatically clears form fields after successful save

## 🚀 Getting Started

### Prerequisites
```bash
pip install pyperclip
```

### Running the Application
```bash
python main.py
```

## 📖 How to Use

1. **Website Field**: Enter the website name or URL
2. **Email Field**: Enter your email (pre-filled with default email)
3. **Password Field**: 
   - Click "Generate" button to create a secure password
   - Or manually enter your own password
4. **Save**: Click "Add" button to save the credentials

## 🔧 Technical Details

### Files Structure
- `main.py` - Main application file with GUI and logic
- `logo.png` - Application logo image
- `data.txt` - Storage file for saved passwords (created automatically)

### Key Components

#### Password Generation Algorithm
- 8-10 random letters (uppercase and lowercase)
- 2-4 random numbers  
- 2-4 random symbols
- Shuffled randomly for enhanced security

#### Data Storage Format
```
website:password:email
```

## 🐛 Recent Bug Fixes

1. **Fixed password field clearing**: Now properly clears password field after saving
2. **Removed redundant file operations**: Eliminated unnecessary `file.close()` call
3. **Enhanced password generation**: Clears existing password before generating new one

## ⚠️ Security Considerations

- Passwords are stored in plain text in `data.txt`
- For production use, consider encrypting the data file
- The application doesn't validate password strength beyond generation
- No master password protection is implemented

## 🎯 Learning Objectives

This project demonstrates:
- Tkinter GUI development
- Event-driven programming
- File I/O operations
- Input validation
- Random password generation
- Clipboard operations
- User experience design

## 🔮 Future Enhancements

- [ ] Encrypt stored passwords
- [ ] Add master password protection
- [ ] Search functionality for stored passwords
- [ ] Password strength indicator
- [ ] Export/import capabilities
- [ ] Database storage instead of text file
- [ ] Password expiration tracking

## 📝 Code Example

```python
# Password generation example
def generate_password():
    import random
    letters = ['a', 'b', 'c', ...] # Full alphabet
    numbers = ['0', '1', '2', ...] # All digits
    symbols = ['!', '#', '$', ...] # Special characters
    
    # Generate random counts
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    # Create password list and shuffle
    password_list = []
    # ... add random characters
    random.shuffle(password_list)
    
    # Convert to string and display
    password = "".join(password_list)
    return password
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!