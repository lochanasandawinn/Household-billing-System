# Household Electricity Billing System
# With Transparent Bill Calculation + Restart Loop

while True:

    # -----------------------------------
    # Price Variables
    # -----------------------------------

    rate_0_30 = 5
    rate_31_60 = 9

    rate_0_60_above = 14
    rate_61_90 = 20
    rate_91_120 = 28
    rate_121_180 = 44
    rate_above_180 = 85

    fixed_0_30 = 80
    fixed_31_60 = 210

    fixed_61_90 = 400
    fixed_91_120 = 1000
    fixed_121_180 = 1500
    fixed_above_180 = 2100

    # -----------------------------------
    # Input Meter Readings
    # -----------------------------------

    print("\n========== ELECTRICITY BILLING SYSTEM ==========\n")

    last_reading = float(input("Enter last meter reading    : "))
    current_reading = float(input("Enter current meter reading : "))

    # -----------------------------------
    # Calculate Units
    # -----------------------------------

    units = current_reading - last_reading

    # -----------------------------------
    # Validation
    # -----------------------------------

    if units < 0:
        print("\nError: Current reading cannot be smaller than last reading.")

    else:

        energy_charge = 0
        fixed_charge = 0

        print("\n========== BILL BREAKDOWN ==========")
        print("Units Consumed:", units, "kWh\n")

        # -----------------------------------
        # 0 - 60 kWh Category
        # -----------------------------------

        if units <= 30:

            energy_charge = units * rate_0_30
            fixed_charge = fixed_0_30

            print(f"{units} × Rs.{rate_0_30} = Rs.{energy_charge}")

        elif units <= 60:

            first_30 = 30 * rate_0_30
            next_units = (units - 30) * rate_31_60

            energy_charge = first_30 + next_units
            fixed_charge = fixed_31_60

            print(f"30 × Rs.{rate_0_30} = Rs.{first_30}")
            print(f"{units - 30} × Rs.{rate_31_60} = Rs.{next_units}")

        # -----------------------------------
        # Above 60 kWh Category
        # -----------------------------------

        else:

            first_60 = 60 * rate_0_60_above
            energy_charge = first_60

            print(f"60 × Rs.{rate_0_60_above} = Rs.{first_60}")

            # 61 - 90
            if units <= 90:

                part = (units - 60) * rate_61_90
                energy_charge += part
                fixed_charge = fixed_61_90

                print(f"{units - 60} × Rs.{rate_61_90} = Rs.{part}")

            # 91 - 120
            elif units <= 120:

                part1 = 30 * rate_61_90
                part2 = (units - 90) * rate_91_120

                energy_charge += part1 + part2
                fixed_charge = fixed_91_120

                print(f"30 × Rs.{rate_61_90} = Rs.{part1}")
                print(f"{units - 90} × Rs.{rate_91_120} = Rs.{part2}")

            # 121 - 180
            elif units <= 180:

                part1 = 30 * rate_61_90
                part2 = 30 * rate_91_120
                part3 = (units - 120) * rate_121_180

                energy_charge += part1 + part2 + part3
                fixed_charge = fixed_121_180

                print(f"30 × Rs.{rate_61_90} = Rs.{part1}")
                print(f"30 × Rs.{rate_91_120} = Rs.{part2}")
                print(f"{units - 120} × Rs.{rate_121_180} = Rs.{part3}")

            # Above 180
            else:

                part1 = 30 * rate_61_90
                part2 = 30 * rate_91_120
                part3 = 60 * rate_121_180
                part4 = (units - 180) * rate_above_180

                energy_charge += part1 + part2 + part3 + part4
                fixed_charge = fixed_above_180

                print(f"30 × Rs.{rate_61_90} = Rs.{part1}")
                print(f"30 × Rs.{rate_91_120} = Rs.{part2}")
                print(f"60 × Rs.{rate_121_180} = Rs.{part3}")
                print(f"{units - 180} × Rs.{rate_above_180} = Rs.{part4}")

        # -----------------------------------
        # Final Bill
        # -----------------------------------

        total_bill = energy_charge + fixed_charge

        print("\n----------------------------------")
        print("Energy Charge : Rs.", energy_charge)
        print("Fixed Charge  : Rs.", fixed_charge)
        print("----------------------------------")
        print("Total Bill    : Rs.", total_bill)

    # -----------------------------------
    # Restart Option
    # -----------------------------------

    choice = input("\nPress ENTER to calculate another bill or type 'q' to quit: ")

    if choice.lower() == 'q':
        print("\nExiting Electricity Billing System...")
        break