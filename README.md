# Truecaller Login Test

This repository contains a simple automation script written in Python using pytest and Appium to perform login to the Truecaller Android app. The script demonstrates the login flow by clicking on the "Get Started" button, granting necessary permissions, logging in with a Google account, and asserting the successful login on the main screen.

## Prerequisites

- Python 3.x installed on your machine
- Appium installed globally (`npm install -g appium`)
- Android device or emulator set up and connected

## Setup

1. Clone the repository to your local machine or download the script file.

2. Install the required dependencies by running the following command:

   ```shell
   pip install pytest appium-python-client
   ```

3. Make sure your Android device is connected or start an Android emulator.

4. Start the Appium server by running the following command in a separate terminal:

   ```shell
   appium
   ```

## Running the Test

1. Navigate to the directory where the script is located.

2. In the terminal, run the following command to execute the test:

   ```shell
   pytest -v
   ```

   The `-v` flag is optional and provides verbose output, showing detailed information about each test case.

3. The script will run the login test, performing actions such as clicking buttons, entering Google account credentials, and asserting the successful login on the main screen.

4. After the test execution, the test results will be displayed in the terminal, including any failures or errors encountered.

## Customization

- Modify the desired capabilities in the `setup` fixture according to your device and Truecaller app installation. Update the `deviceName`, `platformVersion`, `app`, and other relevant fields as necessary.

- Customize the test assertions, actions, and additional test cases in the `test_login_to_truecaller` method to fit your specific requirements.

Feel free to modify the script and explore further automation possibilities with the Truecaller Android app.

**Note:** Ensure that the Appium server is running, and the desired capabilities are correctly configured for your device before running the script.

## License

This script is licensed under the [MIT License](LICENSE).