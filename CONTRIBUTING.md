# Contributing to leblanc

First off, thank you for considering contributing to **leblanc**! It's people like you that make the open-source community such an amazing place to learn, inspire, and create.

## Setting Up the Development Environment

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/wSanice/leblanc.git
   cd leblanc
   ```

3. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

4. **Install Dependencies & Install in Editable Mode**:
   ```bash
   pip install pandas numpy faker
   pip install -e .
   ```
   *Note: The `-e .` flag allows you to edit the code and test it immediately without reinstalling.*

## Coding Guidelines (Architecture v0.6.3+)

We have recently migrated to an **Object-Oriented Design**. If you are adding a new sector or modifying an existing one, please follow these rules:

1. **Inheritance**: All generator classes must inherit from `Leblanc` (imported from `.base`).
2. **Structure**:
   * Define your data dictionaries (e.g., `PRODUCTS_X`) as class constants.
   * Define a `TRANSLATIONS` dictionary for `pt_BR` support.
3. **Methods**:
   * Implement `Youtube(self)`: Returns a dict with description.
   * Implement `build(self, missing_data_cols=None)`: The main logic.
   * Use `self.fake` instead of instantiating a new Faker.
   * Use `self._create_dataframe(data, name)` at the end.
   * Support `missing_data_cols` logic (check existing modules for examples).

## Testing

Before submitting a Pull Request, make sure your code works and doesn't break existing modules.

1. Run the full test script located in the root:
   ```bash
   python test_leblanc_full.py
   ```
   or 
   
   ```bash
   python test_leblanc_full-pt-br.py
   ```
2. Verify if your new module appears in the output and if translations (`pt_BR`) are working.

## Submitting a Pull Request (PR)

1. Create a branch for your feature:
   ```bash
   git checkout -b feature/amazing-sector
   ```
2. Commit your changes:
   ```bash
   git commit -m 'Add Amazing Sector generator'
   ```
3. Push to the branch:
   ```bash
   git push origin feature/amazing-sector
   ```
4. Open a Pull Request on GitHub.