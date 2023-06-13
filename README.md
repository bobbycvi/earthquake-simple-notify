# Earthquake Notifier

This Python script retrieves earthquake information from the USGS (United States Geological Survey) earthquake data API and notifies you when an earthquake occurs. You can choose to receive notifications for earthquakes worldwide or specify a specific region like Romania.

## Features

- Retrieves earthquake data from the USGS API.
- Notifies you about earthquakes in real-time.
- Customizable notification mechanism.
- Option to filter notifications by region.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- `colorama` library (install using `pip install colorama`) (Optional, for colored notifications)

## Usage

1. Clone the repository:
```git clone https://github.com/bobbycvi/earthquake-simple-notify```

2. Navigate to the project directory:
```cd earthquake-simple-notify```

3. Install the required libraries:
```pip install -r requirements.txt```

4. Run the script:
```python earthquake-notify-world.py```
	For Romania people:
	```python earthquake-notify-romania.py``` 


The script will retrieve earthquake data and display notifications based on your specified criteria.

## Customization

- To receive notifications for earthquakes worldwide, remove the condition for filtering earthquakes by region in the `check_earthquakes()` function.

- Modify the `notify_terminal()` function to customize the notification mechanism, such as sending emails, text messages, or integrating with messaging services.

## License

This project is licensed under the [MIT License](LICENSE).

