## **README**

### **Project Overview**

This Python project is designed to analyze hotel room data from a JSON file. It provides the following functionalities:

- **Finds the cheapest room:** Identifies the room with the lowest shown price.
- **Calculates total price:** Calculates the total price for each room, including net price and taxes.
- **Writes output to JSON:** Saves the analysis results to a JSON file for easy reference.

### **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/samtogo407/Py_Fornova-.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### **Usage**

1. **Prepare your JSON data:** Ensure your JSON data file (e.g., `hotel_data.json`) is in the same directory as the Python script.

2. **Run the script:**
   ```bash
   python3 hotel_data_analyzer.py
   ```

### **Output**

The script will generate an output JSON file named `analysis_results.json`. This file contains the following information:

- **Cheapest room:**
  - Room type
  - Price
  - Number of guests
- **Total prices:**
  - Room type
  - Net price
  - Tax
  - Total price

### **Example JSON Data**

```json
{
  "assignment_results": [
    {
      "shown_price": {
        "Standard Room": "100.00",
        "Deluxe Room": "150.00"
      },
      "net_price": {
        "Standard Room": "90.00",
        "Deluxe Room": "130.00"
      },
      "ext_data": {
        "taxes": "{\"TAX\":\"10.00\",\"City tax\":\"5.00\"}"
      },
      "number_of_guests": 2
    }
  ]
}
```

### **Contributing**

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.
