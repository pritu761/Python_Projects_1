#!/usr/bin/env python3
"""
Setup script for Python Learning Projects Collection
Installs dependencies and provides project management utilities
"""

import subprocess
import sys
import os
from pathlib import Path


def install_requirements():
    """Install required packages from requirements.txt"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"⚠️  Python 3.8+ required. Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python version {version.major}.{version.minor} is compatible")
    return True


def list_projects():
    """List all available projects"""
    projects = {
        "password-manager-start": "Password Manager with GUI",
        "kanye-quotes-start": "Kanye West Quotes App",
        "turtle-crossing-start": "Turtle Crossing Game",
        "quizzler-app-start": "Interactive Quiz Application",
        "Web Scrapping": "Web Scraping Examples",
        "login": "Web Login Interface",
        "oop-coffee-machine-start": "OOP Coffee Machine",
        "pomodoro-start": "Pomodoro Timer App",
        "flash-card-project-start": "Language Learning Flashcards"
    }
    
    print("\n📁 Available Projects:")
    print("=" * 50)
    for i, (folder, description) in enumerate(projects.items(), 1):
        if os.path.exists(folder):
            print(f"{i:2d}. {folder:<25} - {description}")
    print()


def run_project(project_name):
    """Run a specific project"""
    project_path = Path(project_name)
    
    if not project_path.exists():
        print(f"❌ Project '{project_name}' not found!")
        return False
    
    main_py = project_path / "main.py"
    if main_py.exists():
        print(f"🚀 Running {project_name}...")
        try:
            subprocess.run([sys.executable, str(main_py)], cwd=project_path)
            return True
        except KeyboardInterrupt:
            print(f"\n⏹️  {project_name} stopped by user")
            return True
        except Exception as e:
            print(f"❌ Error running {project_name}: {e}")
            return False
    else:
        print(f"❌ main.py not found in {project_name}")
        return False


def setup_environment():
    """Set up the development environment"""
    print("🐍 Python Learning Projects Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install requirements
    if not install_requirements():
        return False
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Choose a project from the list below")
    print("2. Run: python setup.py run <project-name>")
    print("3. Or navigate to a project folder and run: python main.py")
    
    list_projects()
    return True


def main():
    """Main setup function"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python setup.py setup     - Install dependencies and setup environment")
        print("  python setup.py list      - List available projects")
        print("  python setup.py run <project-name> - Run a specific project")
        print("\nExample:")
        print("  python setup.py run password-manager-start")
        return
    
    command = sys.argv[1].lower()
    
    if command == "setup":
        setup_environment()
    elif command == "list":
        list_projects()
    elif command == "run":
        if len(sys.argv) < 3:
            print("❌ Please specify a project name")
            list_projects()
        else:
            project_name = sys.argv[2]
            run_project(project_name)
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: setup, list, run")


if __name__ == "__main__":
    main()