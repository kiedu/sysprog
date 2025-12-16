#!/bin/bash

# Define arrays for each cargo bay's inventory
forward_bay=()
midship_bay=()
aft_bay=()
count=1
# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Please specify a cargo bay: forward, midship, or aft"
    exit 1
fi

forward_bay+=("Space Suits" "Oxygen Tanks" "Repair Kits")
midship_bay+=("Food Supplies" "Water Containers" "Medical Equipment")
aft_bay+=("Spare Parts" "Fuel Cells" "Scientific Instruments")


# Display inventory based on the argument
if [ "$1" = "forward" ]; then
    echo "Forward Bay Inventory:"
    for item in "${forward_bay[@]}"; do
        echo "$count. $item" # Prints each element on a new line
        ((count++))
    done

elif [ "$1" = "midship" ]; then
    echo "Midship Bay Inventory:"
    for item in "${midship_bay[@]}"; do
        echo "$count. $item" # Prints each element on a new line
        ((count++))
    done
elif [ "$1" = "aft" ]; then
    echo "Aft Bay Inventory:"
    for item in "${aft_bay[@]}"; do
        echo "$count. $item" # Prints each element on a new line
        ((count++))
    done
else
    echo "Invalid cargo bay. Choose forward, midship, or aft."
    exit 1
fi

