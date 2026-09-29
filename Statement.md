# 📄 Statement.md — Project Statement

## 1. Project Title

**Terminal Currency & Inflation Calculator**

---

## 2. Introduction

Currency is used internationally for travel, education, business, imports, exports, online shopping, investment, and many other activities. Since different countries use different currencies, users often need to convert one currency into another.

A second issue is inflation. The value of money can change over time because of changes in the general price level. Therefore, simply knowing today's converted amount may not be enough when a user wants to understand a projected future value.

This project combines currency conversion and a simple inflation projection into one Python terminal application.

---

## 3. Background

Exchange rates describe the relative value of currencies. In this application, all exchange rates are represented against USD.

For example, if:

```text
INR = 95.88
```

the program interprets the stored rate as:

```text
1 USD = 95.88 INR
```

The USD base allows the application to convert between two currencies without storing a separate exchange rate for every possible currency pair.

The application also stores monthly inflation rates. When the user requests an inflation projection, the target currency's stored monthly rate is repeatedly applied using a compound formula.

---

## 4. Problem Statement

### General Problem

Manual currency conversion requires users to find exchange rates and perform calculations themselves. Repeating these calculations can be inconvenient and can result in arithmetic mistakes.

Additionally, a currency conversion alone does not provide a simple projection of how the converted amount could change when a stored inflation rate is applied over several months.

### Proposed Solution

Develop a Python-based terminal application that:

1. Accepts a source currency.
2. Accepts a target currency.
3. Accepts an amount.
4. Accepts a number of months.
5. Validates user input.
6. Converts the source amount to USD.
7. Converts USD to the target currency.
8. Displays the converted amount.
9. Optionally applies the stored monthly inflation rate.
10. Displays the projected future value.
11. Provides useful error messages for invalid input.

---

## 5. Aim

The aim of the project is:

> To develop a simple, reliable, and understandable Python terminal application for currency conversion with an optional inflation-adjusted projection.

---

## 6. Objectives

### Functional Objectives

- Support multiple currency codes.
- Validate currency codes.
- Validate numerical input.
- Perform currency conversion.
- Display currency names where available.
- Perform optional inflation projection.
- Detect missing inflation information.
- Display clear results.
- Handle keyboard interruption.

### Educational Objectives

The project demonstrates:

- Python dictionaries.
- Functions.
- Loops.
- `if/else` conditions.
- `try/except`.
- String manipulation.
- Floating-point arithmetic.
- Dictionary lookup.
- Modular program design.

---

## 7. Scope

### In Scope

- Terminal-based interaction.
- Embedded exchange-rate data.
- Embedded inflation-rate data.
- USD-based conversion.
- Non-negative amount validation.
- Optional inflation projection.
- Error messages.
- Graceful `Ctrl+C` handling.

### Out of Scope

The current version does not provide:

- Live exchange rates.
- Automatic API updates.
- Banking transactions.
- Money transfers.
- Investment advice.
- A graphical user interface.
- User accounts.
- Database storage.
- Historical charts generated from live data.
- Guaranteed future inflation forecasts.

---

## 8. Functional Requirements

### FR-01: Display Application Information

The system shall display the application title and data-date notice when the program starts.

### FR-02: Accept Source Currency

The system shall ask the user for the source currency code.

### FR-03: Validate Source Currency

The system shall verify the source currency against `EXCHANGE_RATES`.

### FR-04: Accept Target Currency

The system shall ask for the destination currency code.

### FR-05: Validate Target Currency

The system shall verify the destination currency against `EXCHANGE_RATES`.

### FR-06: Accept Amount

The system shall accept a numerical amount.

### FR-07: Reject Negative Amount

The system shall reject negative numerical amounts.

### FR-08: Handle Invalid Amount Input

The system shall catch invalid numerical input and ask the user again.

### FR-09: Accept Projection Period

The system shall ask for the number of months for inflation projection.

### FR-10: Perform Currency Conversion

The system shall convert the amount from the source currency to USD and then from USD to the target currency.

### FR-11: Display Conversion Result

The system shall display:

- Original amount.
- Source currency code.
- Source currency name when available.
- Converted amount.
- Target currency code.
- Target currency name when available.

### FR-12: Perform Inflation Projection

If the number of months is greater than zero and inflation data is available, the system shall calculate a future adjusted value.

### FR-13: Handle Missing Inflation Data

If inflation data is unavailable, the system shall display a warning instead of calculating a projection.

### FR-14: Handle Keyboard Interrupt

The system shall catch `KeyboardInterrupt` and display a graceful closing message.

---

## 9. Non-Functional Requirements

### NFR-01: Usability

The program should be understandable to a beginner using a terminal.

### NFR-02: Performance

The application should return calculations immediately for normal user input.

### NFR-03: Reliability

The application should not terminate its validation loops because of ordinary invalid currency or numerical input.

### NFR-04: Maintainability

The use of named dictionaries and functions should make the code easier to modify.

### NFR-05: Portability

The application should run on systems supporting the required Python version without requiring third-party libraries.

### NFR-06: Availability

The program should work without internet access because its datasets are embedded.

### NFR-07: Accuracy

Calculations should follow the mathematical formulas defined by the program and use the stored data consistently.

### NFR-08: Readability

The terminal output should use clear labels, separators, and formatted numerical values.

### NFR-09: Extensibility

The architecture should allow future API, GUI, database, and reporting features.

---

## 10. Users and Stakeholders

### Primary Users

- Students learning Python.
- Users needing a basic currency calculation.
- Users wanting a simple inflation projection.

### Potential Stakeholders

- Student/project evaluator.
- Course instructor.
- Project developer.
- Future users of an extended version.

---

## 11. Inputs

| Input | Type | Validation |
|---|---|---|
| From currency | String | Must exist in `EXCHANGE_RATES` |
| To currency | String | Must exist in `EXCHANGE_RATES` |
| Amount | Float | Must be >= 0 |
| Months | Integer after conversion | Intended to represent a non-negative projection period |

---

## 12. Outputs

### Conversion Output

```text
From : 100.00 USD (United States dollar)
To   : 9,588.00 INR (Indian rupee)
```

### Inflation Output

```text
Target Currency (INR) Monthly Inflation Rate: 0.4%
Future Adjusted Value (after 6 months): ...
```

### Missing Data Output

```text
Inflation data is not available for [currency].
Showing result without inflation projection.
```

---

## 13. Mathematical Specification

### Currency Conversion

Given:

```text
A = source amount
Rs = source currency units per USD
Rt = target currency units per USD
```

First:

```text
USD Amount = A / Rs
```

Then:

```text
Target Amount = USD Amount × Rt
```

Therefore:

```text
Target Amount = A × Rt / Rs
```

---

### Inflation Projection

Given:

```text
V = converted amount
r = monthly inflation rate in percent
n = number of months
```

The program calculates:

```text
Future Value = V × (1 + r/100)^n
```

---

## 14. Assumptions

1. The embedded exchange-rate values are treated as valid.
2. USD is the base currency.
3. The supplied rate represents units of currency per 1 USD.
4. Inflation rates are interpreted as monthly percentages.
5. A `None` inflation value means no projection is available.
6. The projection assumes the same monthly rate remains constant for all requested months.
7. The program is a calculation tool, not a financial forecasting system.

---

## 15. Constraints

- Exchange rates do not update automatically.
- Inflation rates do not update automatically.
- Some currencies have no corresponding full-name entry.
- Some currencies have no inflation value.
- Terminal input is required.
- The current version has no persistent storage.

---

## 16. Acceptance Criteria

The project can be considered functionally complete when:

- A valid source currency is accepted.
- A valid target currency is accepted.
- An invalid currency is rejected.
- A valid amount is accepted.
- Invalid numerical input is handled.
- Negative amounts are rejected.
- Currency conversion produces a mathematically consistent result.
- Zero months skips the projection.
- A valid positive month period produces a projection when inflation data exists.
- Missing inflation data produces a warning.
- `Ctrl+C` produces a graceful closing message.

---

## 17. Risks

| Risk | Effect | Mitigation |
|---|---|---|
| Outdated exchange rates | Incorrect real-world conversion | Add live API |
| Outdated inflation rates | Inaccurate projection | Add live data source |
| Floating-point representation | Small numerical differences | Use appropriate decimal handling if financial precision is required |
| Invalid user input | Failed calculation | Input validation |
| Missing currency name | Less readable output | Add complete currency-name mapping |
| Invalid month format | Unexpected projection period | Validate month input explicitly |

---

## 18. Future Scope

The system can be extended with:

1. Live exchange-rate APIs.
2. Live inflation data.
3. Historical exchange-rate graphs.
4. Historical inflation graphs.
5. GUI using Tkinter/PyQt.
6. Web interface.
7. Mobile application.
8. Database storage.
9. Conversion history.
10. CSV/Excel export.
11. User accounts.
12. Currency symbols.
13. Searchable currency list.
14. Automated tests.
15. API failure handling.
16. Configurable base currency.

---

## 19. Conclusion

The project addresses a practical calculation problem using basic Python programming techniques. It combines structured data, validation, currency conversion, and inflation projection in one terminal application.

The design is intentionally simple so that it can be understood, tested, and extended by a beginner Python developer.

