# Language Translator Automation

Automated testing framework for the Language Translator Android application using Appium and Python.

## Features

- **Page Object Model (POM)**: Well-structured page objects for maintainability
- **Base Page Class**: Common utilities and wait strategies
- **Logging**: Comprehensive logging for debugging and test execution tracking
- **Configuration Management**: Centralized configuration for easy maintenance
- **Explicit Waits**: Replaced all `time.sleep()` with WebDriverWait for better reliability
- **Error Handling**: Improved exception handling with meaningful error messages

## Project Structure

```
LanguageTranslatorAutomation/
├── config/                 # Configuration files
│   ├── __init__.py
│   └── config.py          # App settings, paths, timeouts
├── core/                   # Core functionality
│   ├── driver_manager.py  # Driver initialization and management
│   └── base_flows.py      # App onboarding flows
├── pages/                  # Page Object Model
│   ├── base_page.py       # Base page with common utilities
│   ├── home_page.py       # Home screen page object
│   └── text_translator_page.py  # Text translator page object
├── tests/                  # Test cases
│   └── test_text_translator.py
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── logger.py          # Logging configuration
│   └── wait_utils.py      # Wait utility functions
├── logs/                   # Log files (auto-generated)
├── screenshots/            # Screenshots (auto-generated)
├── run_main.py            # Main entry point
└── requirements.txt       # Python dependencies
```

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Appium Server:**
   - Install Node.js
   - Install Appium: `npm install -g appium`
   - Install UiAutomator2 driver: `appium driver install uiautomator2`

3. **Start Appium Server:**
   ```bash
   appium
   ```

4. **Configure the app path:**
   - Update `APP_PATH` in `config/config.py` if your APK is in a different location

5. **Connect Android device/emulator:**
   - Enable USB debugging
   - Verify connection: `adb devices`

## Running Tests

### Run all tests:
```bash
pytest tests/
```

### Run with HTML report:
```bash
pytest tests/ --html=report.html --self-contained-html
```

### Run specific test:
```bash
pytest tests/test_text_translator.py::test_text_translation
```

### Run with verbose output:
```bash
pytest tests/ -v
```

## Configuration

Key configuration settings in `config/config.py`:

- `APP_PATH`: Path to the APK file
- `APPIUM_SERVER_URL`: Appium server URL (default: http://127.0.0.1:4723)
- `DEFAULT_TIMEOUT`: Default wait timeout (default: 10 seconds)
- `IMPLICIT_WAIT`: Implicit wait time (default: 5 seconds)

## Logging

Logs are automatically saved to the `logs/` directory with timestamps. Log levels can be configured in `config/config.py`.

## Screenshots

Screenshots are automatically saved to the `screenshots/` directory during test execution for debugging purposes.

## Best Practices

1. **Use Page Objects**: All UI interactions should go through page objects
2. **Use Explicit Waits**: Never use `time.sleep()` - use WebDriverWait instead
3. **Logging**: Use logger instead of print statements
4. **Error Handling**: Always handle exceptions gracefully with meaningful messages
5. **Locators**: Store locators as class attributes in page objects

## Troubleshooting

- **Driver initialization fails**: Check if Appium server is running and device is connected
- **Element not found**: Check locators and ensure app is in the expected state
- **Timeout errors**: Increase timeout values in config if needed for slower devices
