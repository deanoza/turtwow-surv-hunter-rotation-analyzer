import numpy as np
from colorama import Fore, Style, init
from tqdm import tqdm

def calculate_damage(base_damage, crit_chance, crit_multiplier):
    """Calculate the damage considering crit chance and crit multiplier."""
    crit = np.random.rand() < crit_chance
    damage = base_damage * (crit_multiplier if crit else 1)
    return damage

def print_banner():
    # Initialize colorama
    init(autoreset=True)

    print(Fore.GREEN + r"""
                                 ___-------___
                             _-~~             ~~-_
                          _-~                    /~-_
       /^\__/^\         /~  \                   /    \
     /|  O|| O|        /      \_______________/        \
    | |___||__|      /       /                \          \
    |          \    /      /                    \          \
    |   (_______) /______/                        \_________ \
    |         / /         \                      /            \
     \         \^\\         \                  /               \     /
       \         ||           \______________/      _-_       //\__//
         \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
           ~-----||====/~     |==================|       |/~~~~~
            (_(__/  ./     /                    \_\      \.
                   (_(___/                         \_____)_)

           vatie's Turtle WoW Survival Hunter
             Rotation Analyzer
    """)

def get_weapon_damage(min_damage, max_damage):
    """Generate a random weapon damage within the given range."""
    return np.random.uniform(min_damage, max_damage)

def simulate_rotation(strategy, min_damage, max_damage, swing_speed, 
                      white_crit_chance, raptor_crit_chance, mongoose_crit_chance, 
                      simulation_time=180, crit_multiplier=2.2, rapid_fire_cd=300, 
                      rapid_fire_duration=15, swift_aspects_chance=0.10, swift_aspects_duration=12, 
                      raptor_align_threshold=0.5):
    """
    Simulate a given rotation strategy over a specified simulation period.

    strategy: function defining the rotation logic
    Returns total damage dealt and counts of ability usage.
    """
    # Cooldowns and timers
    mongoose_cd = 4  # 4 seconds
    raptor_cd = 5    # 5 seconds

    time = 0
    swing_timer = 0
    mongoose_timer = 0
    raptor_timer = 0
    rapid_fire_timer = 0
    swift_aspects_timer = 0
    total_damage = 0

    # Damage tracking
    white_hits = 0
    mongoose_hits = 0
    raptor_hits = 0

    # Adjustments for buffs
    base_swing_speed = swing_speed

    while time <= simulation_time:
        # Apply buffs
        if rapid_fire_timer > 0:
            swing_speed = base_swing_speed * 0.6  # 40% increase in speed
        elif swift_aspects_timer > 0:
            swing_speed = base_swing_speed * 0.85  # 15% increase in speed
        else:
            swing_speed = base_swing_speed

        # Handle buffs cooldown and procs
        if rapid_fire_timer > 0:
            rapid_fire_timer -= 0.01

        if swift_aspects_timer > 0:
            swift_aspects_timer -= 0.01

        # Apply the strategy logic
        decision = strategy(swing_timer, mongoose_timer, raptor_timer, raptor_align_threshold)

        if decision == "white_hit" and swing_timer <= 0:
            # Auto-attack (white hit)
            base_damage = get_weapon_damage(min_damage, max_damage)
            damage = calculate_damage(base_damage, white_crit_chance, crit_multiplier)
            total_damage += damage
            swing_timer = swing_speed
            white_hits += 1

            # Swift Aspects proc on white hits
            if np.random.rand() < swift_aspects_chance:
                swift_aspects_timer = swift_aspects_duration

        elif decision == "mongoose_bite" and mongoose_timer <= 0:
            # Mongoose Bite
            base_damage = get_weapon_damage(min_damage, max_damage) * 0.8 + 135
            damage = calculate_damage(base_damage, mongoose_crit_chance, crit_multiplier)
            total_damage += damage
            mongoose_timer = mongoose_cd
            swing_timer = swing_speed  # Reset swing timer upon using Mongoose Bite
            mongoose_hits += 1

            # Swift Aspects proc on Mongoose Bite
            if np.random.rand() < swift_aspects_chance:
                swift_aspects_timer = swift_aspects_duration

        elif decision == "raptor_strike" and raptor_timer <= 0 and swing_timer <= raptor_align_threshold:
            # Raptor Strike
            base_damage = get_weapon_damage(min_damage, max_damage) * 1.2 + 160
            damage = calculate_damage(base_damage, raptor_crit_chance, crit_multiplier)
            total_damage += damage
            raptor_timer = raptor_cd
            raptor_hits += 1

            # Swift Aspects proc on Raptor Strike
            if np.random.rand() < swift_aspects_chance:
                swift_aspects_timer = swift_aspects_duration

        # Advance time
        delta_time = 0.01
        time += delta_time
        swing_timer -= delta_time
        mongoose_timer -= delta_time
        raptor_timer -= delta_time

        # Trigger Rapid Fire every 5 minutes
        if time % rapid_fire_cd < 0.01:
            rapid_fire_timer = rapid_fire_duration

    return {
        "Total Damage": total_damage,
        "White Hits": white_hits,
        "Mongoose Bites": mongoose_hits,
        "Raptor Strikes": raptor_hits
    }

def balanced_priority_strategy(swing_timer, mongoose_timer, raptor_timer, raptor_align_threshold):
    """Balance Raptor Strike and Mongoose Bite usage."""
    if raptor_timer <= 0 and swing_timer <= raptor_align_threshold:
        return "raptor_strike"
    elif mongoose_timer <= 0 and swing_timer > raptor_align_threshold and raptor_timer > 0:
        return "mongoose_bite"
    elif swing_timer <= 0:
        return "white_hit"
    return None

def run_strategy(strategy_name, threshold, progress_bar, **kwargs):
    """Helper function to run a strategy simulation and calculate averages."""
    totals, white_hits, mongoose_hits, raptor_hits = [], [], [], []
    for _ in progress_bar:
        results = simulate_rotation(
           lambda swing, mongoose, raptor, t: balanced_priority_strategy(swing, mongoose, raptor, t),
           raptor_align_threshold=threshold,
           **{key: value for key, value in kwargs.items() if key != "average_runs"}
        )
        totals.append(results["Total Damage"])
        white_hits.append(results["White Hits"])
        mongoose_hits.append(results["Mongoose Bites"])
        raptor_hits.append(results["Raptor Strikes"])
    return {
        "Strategy": strategy_name,
        "Avg Damage": sum(totals) / len(totals),
        "Avg White Hits": sum(white_hits) / len(white_hits),
        "Avg Mongoose Hits": sum(mongoose_hits) / len(mongoose_hits),
        "Avg Raptor Hits": sum(raptor_hits) / len(raptor_hits)
    }

# Main function to run simulations
def run_simulations():
    # Inputs
    print_banner()
    min_damage = float(input("Enter base weapon minimum damage (paperdoll) (default 522): ") or 522)
    max_damage = float(input("Enter base weapon maximum damage (paperdoll) (default 610): ") or 610)
    swing_speed = float(input("Enter melee swing speed (paperdoll) (default 3.56): ") or 3.56)

    # Input white crit chance as a percentage, convert to decimal
    white_crit_chance = float(input("Enter white damage crit chance as a percentage (default 20): ") or 20) / 100

    # Calculate raptor and mongoose crit chances
    raptor_crit_chance = white_crit_chance + 0.06
    mongoose_crit_chance = white_crit_chance + 0.06

    simulation_time = int(input("Enter simulation time in seconds (default 180): ") or 180)
    average_runs = int(input("Enter number of runs to average (default 100): ") or 100)

    # Shared arguments for simulation
    shared_kwargs = {
        "min_damage": min_damage,
        "max_damage": max_damage,
        "swing_speed": swing_speed,
        "white_crit_chance": white_crit_chance,
        "raptor_crit_chance": raptor_crit_chance,
        "mongoose_crit_chance": mongoose_crit_chance,
        "simulation_time": simulation_time,
        "crit_multiplier": 2.2,
        "rapid_fire_cd": 300,
        "rapid_fire_duration": 15,
        "swift_aspects_chance": 0.10,
        "swift_aspects_duration": 12,
        "average_runs": average_runs
    }

    # Simulate strategies
    mongoose_progress = tqdm(range(average_runs), desc="Simulating Mongoose Priority")
    mongoose_results = run_strategy("Mongoose Priority", 0, mongoose_progress, **shared_kwargs)

    raptor_progress = tqdm(range(average_runs), desc="Simulating Raptor Priority")
    raptor_results = run_strategy("Raptor Priority", swing_speed - 0.1, raptor_progress, **shared_kwargs)

    balanced_results = []
    for raptor_threshold in tqdm(np.arange(0.1, swing_speed, 0.1), desc="Simulating Balanced Priority"):
        result = run_strategy(f"Balanced Priority (Threshold {raptor_threshold:.1f}s)", raptor_threshold, tqdm(range(average_runs), desc=f"Threshold {raptor_threshold:.1f}s"), **shared_kwargs)
        result["% Improvement (vs Mongoose)"] = ((result['Avg Damage'] - mongoose_results['Avg Damage']) / mongoose_results['Avg Damage']) * 100
        result["% Improvement (vs Raptor)"] = ((result['Avg Damage'] - raptor_results['Avg Damage']) / raptor_results['Avg Damage']) * 100
        balanced_results.append(result)

    # Identify the highest DPS result
    top_result = max(balanced_results, key=lambda x: x['Avg Damage'])

    # Output results
    print(Fore.YELLOW + "\nMongoose Priority Strategy:" + Style.RESET_ALL)
    print(Fore.GREEN + f"Avg Damage: {mongoose_results['Avg Damage']:.2f}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Avg White Hits: {mongoose_results['Avg White Hits']:.2f}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Avg Mongoose Hits: {mongoose_results['Avg Mongoose Hits']:.2f}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Avg Raptor Hits: {mongoose_results['Avg Raptor Hits']:.2f}" + Style.RESET_ALL)

    print(Fore.YELLOW + "\nRaptor Priority Strategy:" + Style.RESET_ALL)
    print(Fore.GREEN + f"Avg Damage: {raptor_results['Avg Damage']:.2f}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Avg White Hits: {raptor_results['Avg White Hits']:.2f}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Avg Mongoose Hits: {raptor_results['Avg Mongoose Hits']:.2f}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Avg Raptor Hits: {raptor_results['Avg Raptor Hits']:.2f}" + Style.RESET_ALL)

    print(Fore.YELLOW + "\nBalanced Priority Strategy:" + Style.RESET_ALL)
    for result in balanced_results:
        is_top = Fore.RED + " (Top DPS)" + Style.RESET_ALL if result == top_result else ""
        print(
            Fore.GREEN + f"{result['Strategy']} | Avg Damage: {result['Avg Damage']:.2f} | " +
            Fore.MAGENTA + f"Improvement vs Mongoose: {result['% Improvement (vs Mongoose)']:.2f}% | " +
            Fore.CYAN + f"Improvement vs Raptor: {result['% Improvement (vs Raptor)']:.2f}%{is_top}" + Style.RESET_ALL
        )

    print(Fore.YELLOW + "\n=====================" + Style.RESET_ALL)
    print(Fore.CYAN + "Explanation:" + Style.RESET_ALL)
    print(Fore.YELLOW + "=====================\n" + Style.RESET_ALL)
    print(Fore.GREEN + "Mongoose bite priority strategy:" + Style.RESET_ALL + " This strategy implies using Mongoose Bite on cooldown always. You would still queue up Raptor Strike and get some hits in but it does reduce the number of white and Raptor Strike hits.")
    print(Fore.GREEN + "Raptor strike priority strategy:" + Style.RESET_ALL + " This strategy implies prioritizing Raptor Strike usage to the max. We will only allow Mongoose Bite to be used immediately after Raptor Strikes (100ms after a Raptor strike).")
    print(Fore.GREEN + "Balanced Raptor Threshold Strategy:" + Style.RESET_ALL + " This strategy involves delaying the use of Mongoose Bite if Raptor Strike will become available shortly before your next melee swing. The threshold value indicates the maximum time (in seconds) before the swing during which this delay is beneficial. By carefully managing this timing, you ensure the effective use of Raptor Strike, which deals higher damage. However, if the threshold is set too high, you risk under-utilizing Mongoose Bite, reducing overall damage output. This analysis helps determine the optimal balance for maximizing total damage. Raptor Align Threshold represents the time window (in seconds) before the next melee swing where you might delay a Mongoose Bite in favor of a Raptor Strike.")

if __name__ == "__main__":
    run_simulations()