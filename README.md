# python-external-dependency-testing
Course material for WWCode Connect Digital 2020

## Requirements

- python 3.8+
- working internet connection for `pip` operations and calling the Advice Slip API

## Setting up

0. (Optional) If you are familiar with `virtualenv`, you may use `venv` as the virtual environment directory (added to `.gitignore`).

    ```
      python -m venv venv
    ```

    Make sure to activate your virtual environment afterwards. Command for activating the virtual environment will depend on your system and terminal.

    ```
      source venv/Scripts/activate
    ```

1. Download dependencies per `requirements.txt`

    ```
      python -m pip install -r requirements.txt
    ```

2. Run `main.py` to make sure that things are running on your end


    ```
      python main.py
    ```

## Credits

[Advice Slip API](https://api.adviceslip.com/) ([@adviceslip](https://twitter.com/adviceslip)) provided by [@tomkiss](https://twitter.com/tomkiss)
