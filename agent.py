

def get_input(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def assess_situation(enemy_strength, troop_health, ammo_level, terrain):
    score = 0

   
    if enemy_strength == "Low":
        score += 3
    elif enemy_strength == "Medium":
        score += 1
    else:  # High
        score -= 2

    
    if troop_health == "High (75-100%)":
        score += 3
    elif troop_health == "Medium (40-74%)":
        score += 1
    else:  # Low
        score -= 2

   
    if ammo_level == "High":
        score += 2
    elif ammo_level == "Medium":
        score += 1
    else:  # Low
        score -= 2

    
    if terrain == "Forest (defensive advantage)":
        score += 1
    elif terrain == "Urban (neutral)":
        score += 0
    else:  # Open
        score -= 1

    return score

def make_decision(score):
    if score >= 6:
        decision = "⚔️  ATTACK"
        reason = "Conditions are highly favorable. Enemy is weak, troops are strong, ammo is sufficient."
        strategy = "Move forward aggressively. Use terrain to your advantage."
    elif score >= 3:
        decision = "🛡️  HOLD POSITION"
        reason = "Conditions are moderate. Neither side has a clear advantage."
        strategy = "Maintain current position. Gather more intel before acting."
    elif score >= 0:
        decision = "📡  CALL FOR SUPPORT"
        reason = "Conditions are unfavorable. Reinforcements needed before engaging."
        strategy = "Request backup, resupply ammunition, wait for support."
    else:
        decision = "🚨  RETREAT"
        reason = "Conditions are critical. Engaging now risks total loss."
        strategy = "Fall back to safe position immediately. Regroup and reassess."

    return decision, reason, strategy

def run_agent():
    print("=" * 55)
    print("   🎖️  BATTLEFIELD DECISION AGENT - AI System")
    print("=" * 55)
    print("This intelligent agent analyzes battlefield conditions")
    print("and recommends the best tactical decision.\n")

    
    enemy_strength = get_input(
        "1. What is the ENEMY STRENGTH?",
        ["Low", "Medium", "High"]
    )

    troop_health = get_input(
        "2. What is your TROOP HEALTH?",
        ["High (75-100%)", "Medium (40-74%)", "Low (below 40%)"]
    )

    ammo_level = get_input(
        "3. What is your AMMUNITION LEVEL?",
        ["High", "Medium", "Low"]
    )

    terrain = get_input(
        "4. What is the TERRAIN TYPE?",
        ["Forest (defensive advantage)", "Urban (neutral)", "Open (exposed)"]
    )

    
    score = assess_situation(enemy_strength, troop_health, ammo_level, terrain)
    decision, reason, strategy = make_decision(score)

   
    print("\n" + "=" * 55)
    print("          📊 SITUATION ANALYSIS REPORT")
    print("=" * 55)
    print(f"  Enemy Strength  : {enemy_strength}")
    print(f"  Troop Health    : {troop_health}")
    print(f"  Ammunition      : {ammo_level}")
    print(f"  Terrain         : {terrain}")
    print(f"  Situation Score : {score}/8")
    print("-" * 55)
    print(f"\n  🎯 DECISION: {decision}")
    print(f"\n  📌 Reason: {reason}")
    print(f"\n  📋 Strategy: {strategy}")
    print("\n" + "=" * 55)

    
    again = input("\nRun another scenario? (yes/no): ").strip().lower()
    if again == "yes":
        print("\n")
        run_agent()
    else:
        print("\n✅ Agent session ended. Stay safe, Commander! 🎖️")


run_agent()
