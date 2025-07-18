# Turtle Crossing Game

A Frogger-style arcade game built with Python's Turtle graphics module where players guide a turtle across busy roads while avoiding moving cars.

## 🐢 Game Overview

Navigate a turtle across multiple lanes of traffic to reach the finish line. Each successful crossing increases the difficulty level with faster-moving cars. Avoid collisions to keep playing!

## 🎮 How to Play

- **Movement**: Use the UP arrow key to move the turtle forward
- **Objective**: Reach the top of the screen (finish line)
- **Avoid**: Colliding with moving cars
- **Progression**: Complete levels to increase difficulty

## 🚀 Getting Started

### Prerequisites
- Python 3.x with Turtle graphics (usually included)

### Running the Game
```bash
python main.py
```

## 📁 Project Structure

```
turtle-crossing-start/
├── main.py          # Main game loop and logic
├── player.py        # Player turtle class
├── car_manager.py   # Car generation and movement
├── scoreboard.py    # Level tracking and game over display
└── README.md        # This file
```

## 🔧 Technical Details

### Game Components

#### Player (`player.py`)
- Turtle-shaped character
- Moves in 10-pixel increments upward
- Starts at bottom center of screen
- Resets position after reaching finish line

#### Car Manager (`car_manager.py`)
- Generates random cars at intervals
- Cars move from right to left
- Random colors and positions
- Speed increases with each level

#### Scoreboard (`scoreboard.py`)
- Displays current level
- Shows "GAME OVER" message
- Updates level counter

#### Main Game Loop (`main.py`)
- Handles user input
- Collision detection
- Level progression logic
- Game state management

## 🐛 Recent Bug Fixes

1. **Fixed level progression**: Changed `self.speed` to `self.car_speed` in car manager
2. **Improved collision detection**: Changed exact position check (`==`) to range check (`>=`) for finish line
3. **Enhanced game mechanics**: More reliable level advancement

## 🎯 Game Mechanics

### Collision Detection
```python
# Check collision with any car
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        # Game over
```

### Level Progression
```python
# Check if player reached finish line
if player.ycor() >= 280:
    player.goto(0, -280)  # Reset position
    scoreboard.level_up()  # Increase level
    car_manager.level_up()  # Increase car speed
```

### Car Generation
```python
# Random car generation (1 in 6 chance each frame)
random_no = random.randint(0, 6)
if random_no == 1:
    # Create new car
```

## 🎲 Game Configuration

### Constants
- **Starting Position**: (0, -280)
- **Finish Line**: Y-coordinate 280
- **Move Distance**: 10 pixels per key press
- **Collision Distance**: 20 pixels
- **Car Speed Increment**: 10 pixels per level

### Car Properties
- **Colors**: Red, Orange, Yellow, Green, Blue, Purple
- **Shape**: Rectangle (1x2 turtle units)
- **Starting Position**: Right edge (x=280)
- **Movement**: Left across screen

## 🏆 Scoring System

- **Level Tracking**: Increases with each successful crossing
- **No Points**: Focus on progression rather than score
- **Difficulty Scaling**: Cars move faster each level

## 🎨 Visual Design

- **Background**: Standard turtle graphics canvas
- **Player**: Black turtle facing upward
- **Cars**: Colorful rectangles moving left
- **UI**: Level counter in top-left corner

## 📚 Learning Objectives

This project teaches:
- **Object-Oriented Programming**: Multiple classes working together
- **Game Development**: Game loops, collision detection, level progression
- **Event Handling**: Keyboard input processing
- **Graphics Programming**: Turtle graphics manipulation
- **State Management**: Game state tracking and updates

## 🔮 Possible Enhancements

- [ ] Add sound effects
- [ ] Multiple lanes with different speeds
- [ ] Power-ups (temporary invincibility, slow motion)
- [ ] High score tracking
- [ ] Animated sprites
- [ ] Background music
- [ ] Multiple difficulty modes
- [ ] Achievement system

## 🐛 Debugging Tips

1. **Cars not moving**: Check `car_speed` attribute in `car_manager.py`
2. **Collision not working**: Verify distance calculation (should be < 20)
3. **Level not advancing**: Ensure finish line check uses `>=` not `==`
4. **Performance issues**: Reduce car generation frequency

## 🤝 Contributing

Feel free to fork this project and add your own enhancements! Some areas for improvement:
- Better graphics and animations
- Sound effects and music
- More sophisticated car patterns
- Additional game mechanics

## 📄 License

This project is for educational purposes. Feel free to use and modify!