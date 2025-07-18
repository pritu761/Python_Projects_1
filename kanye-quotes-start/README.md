# Kanye Quotes App

A fun desktop application that fetches and displays random Kanye West quotes using the Kanye REST API. Built with Python's Tkinter for an engaging user interface.

## 🎤 Features

- **Random Quote Fetching**: Get inspirational (and sometimes bizarre) Kanye quotes
- **Beautiful UI**: Custom background with Kanye's image
- **One-Click Operation**: Simple button click to get new quotes
- **API Integration**: Real-time quotes from Kanye REST API
- **Error Handling**: Graceful handling of network issues

## 🚀 Getting Started

### Prerequisites
```bash
pip install requests
```

### Running the Application
```bash
python main.py
```

## 📖 How to Use

1. **Launch the app**: Run `python main.py`
2. **Get quotes**: Click the Kanye button at the bottom
3. **Enjoy**: Read the inspirational quote displayed on the background
4. **Repeat**: Click again for more quotes!

## 🔧 Technical Details

### Files Structure
- `main.py` - Main application file
- `background.png` - Background image for the quote display
- `kanye.png` - Kanye image used as the button

### API Information
- **Endpoint**: `https://api.kanye.rest/`
- **Method**: GET
- **Response Format**: JSON
- **Rate Limiting**: None specified

### Key Components

#### Quote Fetching Function
```python
def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quotes = data["quote"]
    canvas.itemconfig(quote_text, text=quotes)
```

#### GUI Layout
- **Canvas**: 300x414 pixels for background and text
- **Quote Text**: Centered, white text with Arial font
- **Button**: Kanye image at the bottom

## 🐛 Recent Bug Fixes

1. **Fixed canvas text update**: Changed `canvas.config()` to `canvas.itemconfig()` for proper text updating
2. **Improved error handling**: Added `response.raise_for_status()` for better error detection

## 🎨 UI Design

### Visual Elements
- **Background**: Custom Kanye-themed background image
- **Typography**: Bold Arial font, size 30, white color
- **Layout**: Centered text with button below
- **Dimensions**: 300px wide, 414px tall canvas

### Color Scheme
- **Text**: White (#FFFFFF)
- **Background**: Custom image
- **Button**: Transparent with Kanye image

## 📱 User Experience

### Interaction Flow
1. User sees the app with initial placeholder text
2. User clicks the Kanye button
3. App fetches quote from API
4. New quote appears on the background
5. User can click again for more quotes

### Response Times
- **Network dependent**: Quotes load as fast as the API responds
- **Instant UI updates**: No loading screens needed for quick API responses

## 🌐 API Details

### Kanye REST API
- **URL**: https://api.kanye.rest/
- **Documentation**: https://kanye.rest/
- **Response Example**:
  ```json
  {
    "quote": "I hate when I'm on a flight and I wake up with a water bottle next to me like oh great now I gotta be responsible for this water bottle"
  }
  ```

### Error Handling
```python
try:
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()  # Raises exception for bad status codes
    data = response.json()
    quotes = data["quote"]
except requests.RequestException:
    # Handle network errors gracefully
    quotes = "Unable to fetch quote. Check your internet connection."
```

## 🎯 Learning Objectives

This project demonstrates:
- **API Integration**: Making HTTP requests and handling JSON responses
- **GUI Development**: Creating desktop applications with Tkinter
- **Event Handling**: Button clicks and user interactions
- **Image Handling**: Working with PNG images in Tkinter
- **Error Handling**: Graceful degradation when APIs fail
- **Layout Management**: Canvas-based GUI layouts

## 🔮 Future Enhancements

- [ ] **Offline Mode**: Cache quotes for offline viewing
- [ ] **Quote History**: Keep track of previously shown quotes
- [ ] **Sharing**: Copy quotes to clipboard or share on social media
- [ ] **Themes**: Different background themes
- [ ] **Font Options**: Customizable text styling
- [ ] **Quote Categories**: Filter by quote topics/themes
- [ ] **Favorites**: Save favorite quotes
- [ ] **Auto-refresh**: Automatically get new quotes at intervals

## 🐛 Troubleshooting

### Common Issues

1. **"Unable to connect" error**
   - Check internet connection
   - Verify API endpoint is accessible
   - Try again in a few moments

2. **Blank quotes appearing**
   - API might be returning empty responses
   - Check JSON response format
   - Verify API is functioning

3. **Images not loading**
   - Ensure `background.png` and `kanye.png` are in the same directory
   - Check file permissions
   - Verify image file integrity

## 📚 Code Structure

### Main Components
1. **Import Section**: Required libraries (tkinter, requests)
2. **Quote Function**: API interaction and UI update
3. **GUI Setup**: Window, canvas, and button configuration
4. **Event Loop**: Tkinter mainloop

### Best Practices Demonstrated
- **Separation of Concerns**: UI setup separate from business logic
- **Error Handling**: Proper exception handling for network requests
- **Resource Management**: Efficient image and canvas handling
- **User Feedback**: Immediate visual response to user actions

## 🤝 Contributing

Ideas for contributions:
- Add more quote sources/APIs
- Implement quote caching
- Improve error messages
- Add unit tests
- Create mobile version

## 📄 License

This project is for educational purposes. The Kanye REST API is publicly available. Kanye West quotes are used under fair use.