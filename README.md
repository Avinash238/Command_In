# Currency Converter Web Application

The Currency Converter is a simple web application that allows users to convert an amount from one currency to another. It uses real-time exchange rates to provide accurate and up-to-date conversions.

## Features

- Convert an amount from one currency to another
- Supports multiple currencies, including USD, EUR, GBP, JPY, INR, AUD, CAD, and more
- Real-time exchange rates provided by the forex_python library
- Simple and user-friendly interface

## How to Use

1. Clone the repository to your local machine.
2. Make sure you have Python and Flask installed.
3. Install the required Python packages using pip: pip install forex-python Flask


4. Run the Flask web server: python app.py


5. Open your web browser and go to `http://127.0.0.1:5000/`.
6. Enter the source currency, target currency, and amount to convert in the provided form.
7. Click the "Convert" button to see the converted amount.

## Technologies Used

- Python
- Flask (Python web framework)
- forex_python library (for real-time exchange rates)

## Dependencies

- forex-python
- Flask

## File Structure

- `app.py`: The main Python file that defines the Flask backend and handles currency conversion.
- `templates/index.html`: The HTML template for the frontend of the Currency Converter.
- `static/style.css`: CSS file for custom styling of the HTML template.

## Contributing

Contributions to this project are welcome! If you find any bugs, have feature suggestions, or want to improve the code, feel free to open an issue or submit a pull request.

## Acknowledgments

- The forex_python library for providing real-time exchange rates.
- The Flask community for creating a simple and powerful web framework.
