# Vatie's Turtle WoW Survival Hunter Rotation Analyzer

## Overview
This Python script simulates and analyzes rotation strategies for the Survival Hunter specialization in Turtle WoW. It calculates the total damage output and compares different priority strategies for using abilities like Raptor Strike and Mongoose Bite.

The simulation helps you identify the optimal balance between abilities to maximize your damage over time.

---

## Features
- **Flexible Inputs**: Customize weapon stats, crit chances, swing speed, and simulation duration.
- **Strategy Simulation**:
  - Mongoose Priority
  - Raptor Priority
  - Balanced Priority (Threshold-based)
- **Detailed Results**: Calculates average damage, ability usage, and percentage based comparisons

---

## Prerequisites
To run the script, ensure you have the following dependencies installed:

```bash
pip install numpy colorama tqdm
```

---

## How to Run
1. Clone or download this script to your local machine.
2. Run the script using Python:

```bash
python rotation_analyzer.py
```

3. Enter the required inputs when prompted or press Enter to use default values:
   - **Base weapon minimum/maximum damage**: Defines your weapon's base damage range.
   - **Melee swing speed**: Speed of your melee weapon swings.
   - **White damage crit chance**: Percentage chance for your auto-attacks to critically hit.
   - **Simulation time**: Duration (in seconds) for which the rotation will be simulated.
   - **Number of runs**: Number of simulations to average for accurate results.

---

## Input Details
| Input                     | Description                                     | Default Value |
|---------------------------|-------------------------------------------------|---------------|
| Base Weapon Min Damage    | Minimum damage of your weapon.                 | 522           |
| Base Weapon Max Damage    | Maximum damage of your weapon.                 | 610           |
| Melee Swing Speed         | Speed of your melee weapon swings.             | 3.56          |
| White Damage Crit Chance  | Crit chance for auto-attacks (as a percentage).| 20%           |
| Simulation Time           | Total simulation duration in seconds.          | 180           |
| Number of Runs            | Number of simulation iterations to average.    | 100           |

---

## Output Example
Upon running the script, you will see outputs similar to the following:

```
Mongoose Priority Strategy:
Avg Damage: 92114.06
Avg White Hits: 45.51
Avg Mongoose Hits: 45.00
Avg Raptor Hits: 23.00

Raptor Priority Strategy:
Avg Damage: 90822.68
Avg White Hits: 55.14
Avg Mongoose Hits: 16.18
Avg Raptor Hits: 36.00

Balanced Priority Strategy:
Balanced Priority (Threshold 0.1s) | Avg Damage: 92574.63 | Improvement vs Mongoose: 0.50% | Improvement vs Raptor: 1.93%
Balanced Priority (Threshold 0.2s) | Avg Damage: 93245.14 | Improvement vs Mongoose: 1.23% | Improvement vs Raptor: 2.67%
Balanced Priority (Threshold 0.3s) | Avg Damage: 93898.19 | Improvement vs Mongoose: 1.94% | Improvement vs Raptor: 3.39%
Balanced Priority (Threshold 0.4s) | Avg Damage: 92855.78 | Improvement vs Mongoose: 0.81% | Improvement vs Raptor: 2.24%
Balanced Priority (Threshold 0.5s) | Avg Damage: 94077.63 | Improvement vs Mongoose: 2.13% | Improvement vs Raptor: 3.58%
Balanced Priority (Threshold 0.6s) | Avg Damage: 92518.25 | Improvement vs Mongoose: 0.44% | Improvement vs Raptor: 1.87%
Balanced Priority (Threshold 0.7s) | Avg Damage: 93266.86 | Improvement vs Mongoose: 1.25% | Improvement vs Raptor: 2.69%
Balanced Priority (Threshold 0.8s) | Avg Damage: 92780.52 | Improvement vs Mongoose: 0.72% | Improvement vs Raptor: 2.16%
Balanced Priority (Threshold 0.9s) | Avg Damage: 92824.54 | Improvement vs Mongoose: 0.77% | Improvement vs Raptor: 2.20%
Balanced Priority (Threshold 1.0s) | Avg Damage: 94869.33 | Improvement vs Mongoose: 2.99% | Improvement vs Raptor: 4.46%
Balanced Priority (Threshold 1.1s) | Avg Damage: 91746.83 | Improvement vs Mongoose: -0.40% | Improvement vs Raptor: 1.02%
Balanced Priority (Threshold 1.2s) | Avg Damage: 91782.49 | Improvement vs Mongoose: -0.36% | Improvement vs Raptor: 1.06%
Balanced Priority (Threshold 1.3s) | Avg Damage: 91559.75 | Improvement vs Mongoose: -0.60% | Improvement vs Raptor: 0.81%
Balanced Priority (Threshold 1.4s) | Avg Damage: 92264.80 | Improvement vs Mongoose: 0.16% | Improvement vs Raptor: 1.59%
Balanced Priority (Threshold 1.5s) | Avg Damage: 101264.35 | Improvement vs Mongoose: 9.93% | Improvement vs Raptor: 11.50%
Balanced Priority (Threshold 1.6s) | Avg Damage: 99706.92 | Improvement vs Mongoose: 8.24% | Improvement vs Raptor: 9.78%
Balanced Priority (Threshold 1.7s) | Avg Damage: 100690.28 | Improvement vs Mongoose: 9.31% | Improvement vs Raptor: 10.86%
Balanced Priority (Threshold 1.8s) | Avg Damage: 100066.44 | Improvement vs Mongoose: 8.63% | Improvement vs Raptor: 10.18%
Balanced Priority (Threshold 1.9s) | Avg Damage: 100845.56 | Improvement vs Mongoose: 9.48% | Improvement vs Raptor: 11.04%
Balanced Priority (Threshold 2.0s) | Avg Damage: 102271.06 | Improvement vs Mongoose: 11.03% | Improvement vs Raptor: 12.61%
Balanced Priority (Threshold 2.1s) | Avg Damage: 103454.65 | Improvement vs Mongoose: 12.31% | Improvement vs Raptor: 13.91%
Balanced Priority (Threshold 2.2s) | Avg Damage: 103127.77 | Improvement vs Mongoose: 11.96% | Improvement vs Raptor: 13.55%
Balanced Priority (Threshold 2.3s) | Avg Damage: 103583.93 | Improvement vs Mongoose: 12.45% | Improvement vs Raptor: 14.05%
Balanced Priority (Threshold 2.4s) | Avg Damage: 104049.10 | Improvement vs Mongoose: 12.96% | Improvement vs Raptor: 14.56%
** Balanced Priority (Threshold 2.5s) | Avg Damage: 105115.66 | Improvement vs Mongoose: 14.11% | Improvement vs Raptor: 15.74% (Top DPS) **
Balanced Priority (Threshold 2.6s) | Avg Damage: 104201.74 | Improvement vs Mongoose: 13.12% | Improvement vs Raptor: 14.73%
Balanced Priority (Threshold 2.7s) | Avg Damage: 104078.19 | Improvement vs Mongoose: 12.99% | Improvement vs Raptor: 14.59%
Balanced Priority (Threshold 2.8s) | Avg Damage: 103559.75 | Improvement vs Mongoose: 12.43% | Improvement vs Raptor: 14.02%
Balanced Priority (Threshold 2.9s) | Avg Damage: 103511.95 | Improvement vs Mongoose: 12.37% | Improvement vs Raptor: 13.97%
Balanced Priority (Threshold 3.0s) | Avg Damage: 104237.28 | Improvement vs Mongoose: 13.16% | Improvement vs Raptor: 14.77%
Balanced Priority (Threshold 3.1s) | Avg Damage: 95274.53 | Improvement vs Mongoose: 3.43% | Improvement vs Raptor: 4.90%
Balanced Priority (Threshold 3.2s) | Avg Damage: 90586.92 | Improvement vs Mongoose: -1.66% | Improvement vs Raptor: -0.26%
Balanced Priority (Threshold 3.3s) | Avg Damage: 90736.02 | Improvement vs Mongoose: -1.50% | Improvement vs Raptor: -0.10%
Balanced Priority (Threshold 3.4s) | Avg Damage: 90598.66 | Improvement vs Mongoose: -1.65% | Improvement vs Raptor: -0.25%
Balanced Priority (Threshold 3.5s) | Avg Damage: 90907.93 | Improvement vs Mongoose: -1.31% | Improvement vs Raptor: 0.09%
```

---

## Key Concepts
1. **Mongoose Bite Priority**: Always prioritize Mongoose Bite, leading to fewer Raptor Strikes.
2. **Raptor Strike Priority**: Always prioritize Raptor Strike, delaying Mongoose Bite.
3. **Balanced Priority**: Dynamically balance the usage of Mongoose Bite and Raptor Strike based on a threshold window (Raptor Align Threshold). This is typically the most optimal DPS wise when using the correct threshold value.

---

---

## Interpreting the analysis (Balanced Priority)

In the above example, a threshold of 2.5s was deemed to be the optimal cut-off point for time remaining on the swing timer. In this case if there is more than 2.5 seconds remaining before the next melee swing and mongoose bite
is available for usage - then you should use mongoose bite. If there is less than 2.5 seconds available before the next melee swing will strike then you should delay using mongoose bite and allow the next queued raptor strike
to not be delayed. 

---

## Code Structure
- **`calculate_damage`**: Calculates the damage for abilities with critical hit consideration.
- **`simulate_rotation`**: Runs the simulation logic for a specified strategy.
- **`balanced_priority_strategy`**: Implements the Balanced Priority strategy logic.
- **`run_strategy`**: Helper function to execute a specific strategy and calculate averages.
- **`run_simulations`**: Main function to orchestrate the simulation process.

---

## Customization
Feel free to modify the following constants in the script to suit your needs:
- **`crit_multiplier`**: Default set to `2.2` for critical hits.
- **`swift_aspects_chance` and `swift_aspects_duration`**: Adjust proc chance and duration for the Swift Aspects buff.
- **`rapid_fire_cd` and `rapid_fire_duration`**: Control the cooldown and duration for the Rapid Fire buff.

---

## Contributions
Feel free to fork this repository and contribute enhancements or bug fixes. Create a pull request or open an issue for feedback.

---

## License
This script is distributed under the MIT License. See the `LICENSE` file for more details.