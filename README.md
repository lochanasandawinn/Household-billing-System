# Household-billing-System

# 📊 Domestic Tariff Reference

The billing system uses the following real domestic electricity tariff structure.

---

## Consumption of 0–60 kWh per month

| Block | Energy Charge (Rs./kWh) | Fixed Charge (Rs./Month) |
|---|---|---|
| 0–30 kWh | 5.00 | 80.00 |
| 31–60 kWh | 9.00 | 210.00 |

---

## Consumption above 60 kWh per month

| Block | Energy Charge (Rs./kWh) | Fixed Charge (Rs./Month) |
|---|---|---|
| 0–60 kWh | 14.00 | N/A |
| 61–90 kWh | 20.00 | 400.00 |
| 91–120 kWh | 28.00 | 1,000.00 |
| 121–180 kWh | 44.00 | 1,500.00 |
| Above 180 kWh | 85.00 | 2,100.00 |

---

## 📌 Notes

- Customers consuming **60 kWh or less** fall into the lower tariff category.
- Once consumption exceeds **60 kWh**, a different tariff structure is applied.
- The system calculates:
  - Energy charge
  - Fixed monthly charge
  - Total bill amount
- The billing process is fully transparent and displays how each range contributes to the final bill.
