participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# ==================== 1. Make sure the lists have the same number of elements ====================
if len(participants) != len(scores):
    print("Warning: Participants and scores lists have different lengths!")
else:
    print(f"✓ Loaded {len(participants)} participants successfully.\n")


# ==================== 2. Display all the current participants with their scores. Use zip() ====================
print("=== Current Participants ===")
for name, score in zip(participants, scores):
    print(f"  {name}: {score}")
print()


# ==================== 3. Add a new participant with validation ====================
def add_participant():
    print("=== Add New Participant ===")
    name = input("Enter participant name: ").strip()
    
    # Check if name is empty
    if not name:
        print("  Error: Name cannot be empty.\n")
        return
    
    # Check if participant already exists
    if name in participants:
        print(f"  Error: {name} is already registered.\n")
        return
    
    # Get score input
    score_input = input("Enter score: ").strip()
    
    # Check if score is a number
    try:
        score = float(score_input)
    except ValueError:
        print("  Error: Score must be a number.\n")
        return
    
    # Check if score is between 0 and 100
    if score < 0 or score > 100:
        print("  Error: Score must be between 0 and 100.\n")
        return
    
    # Add participant
    participants.append(name)
    scores.append(score)
    print(f"  ✓ Successfully registered {name} with score {score}.\n")


# ==================== 4. Search for a specific participant ====================
def search_participant():
    print("=== Search Participant ===")
    name = input("Enter participant name to search: ").strip()
    
    if not name:
        print("  Error: Name cannot be empty.\n")
        return
    
    try:
        index = participants.index(name)
        score = scores[index]
        
        print(f"\n  --- {name} ---")
        print(f"  Score: {score}")
        
        if score >= distinction_score:
            print("  Status: DISTINCTION")
        elif score >= qualification_score:
            print("  Status: QUALIFIED")
        else:
            print("  Status: NOT QUALIFIED")
        print()
        
    except ValueError:
        print(f"  Error: {name} not found.\n")


# ==================== 5. Display every participant's name, score, and status ====================
def display_all_participants():
    print("=== All Participants (Status) ===")
    for name, score in zip(participants, scores):
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"  {name}: {score} - {status}")
    print()


# ==================== 6. Check distinction and pass ====================
def check_distinction_and_pass():
    print("=== Distinction and Pass Check ===")
    
    has_distinction = any(score >= distinction_score for score in scores)
    all_passed = all(score >= 50 for score in scores)
    
    if has_distinction:
        print("  ✓ At least one participant has a distinction.")
    else:
        print("  ✗ No participant has a distinction.")
    
    if all_passed:
        print("  ✓ All participants have passed (scored 50 or more).")
    else:
        print("  ✗ Not all participants have passed.")
    print()


# ==================== 7. Update a participant's score ====================
def update_score():
    print("=== Update Score ===")
    name = input("Enter participant name to update: ").strip()
    
    if not name:
        print("  Error: Name cannot be empty.\n")
        return
    
    try:
        index = participants.index(name)
        current_score = scores[index]
        print(f"  Current score for {name}: {current_score}")
        
        new_score_input = input("Enter new score: ").strip()
        
        # Validate new score
        try:
            new_score = float(new_score_input)
        except ValueError:
            print("  Error: Score must be a number.\n")
            return
        
        if new_score < 0 or new_score > 100:
            print("  Error: Score must be between 0 and 100.\n")
            return
        
        # Update score
        scores[index] = new_score
        print(f"  ✓ Successfully updated {name}'s score from {current_score} to {new_score}.\n")
        
    except ValueError:
        print(f"  Error: {name} not found.\n")


# ==================== 8. Withdraw (remove) a participant ====================
def withdraw_participant():
    print("=== Withdraw Participant ===")
    name = input("Enter participant name to remove: ").strip()
    
    if not name:
        print("  Error: Name cannot be empty.\n")
        return
    
    try:
        index = participants.index(name)
        removed_score = scores.pop(index)
        participants.pop(index)
        print(f"  ✓ Successfully removed {name} (score: {removed_score}).\n")
        
    except ValueError:
        print(f"  Error: {name} not found.\n")


# ==================== 9. Scoreboard (descending order with rank) ====================
def display_scoreboard():
    print("=== Scoreboard (Descending Order) ===")
    
    # Pair participants with scores and sort by score descending
    paired = list(zip(participants, scores))
    sorted_paired = sorted(paired, key=lambda x: x[1], reverse=True)
    
    for rank, (name, score) in enumerate(sorted_paired, start=1):
        print(f"  Rank #{rank}: {name} - {score}")
    print()


# ==================== 10. Calculate statistics ====================
def calculate_statistics():
    print("=== Statistics ===")
    
    if not scores:
        print("  No data available.\n")
        return
    
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    count_highest = scores.count(highest)
    count_lowest = scores.count(lowest)
    
    count_distinction = sum(1 for s in scores if s >= distinction_score)
    count_qualified = sum(1 for s in scores if qualification_score <= s < distinction_score)
    count_not_qualified = sum(1 for s in scores if s < qualification_score)
    
    print(f"  Highest Score: {highest} (achieved by {count_highest} participant(s))")
    print(f"  Lowest Score: {lowest} (achieved by {count_lowest} participant(s))")
    print(f"  Average Score: {average:.2f}")
    print(f"  Distinctions (≥{distinction_score}): {count_distinction}")
    print(f"  Qualified (≥{qualification_score}): {count_qualified}")
    print(f"  Not Qualified (<{qualification_score}): {count_not_qualified}")
    print()


# ==================== 11. Final Report ====================
def generate_final_report():
    print("=" * 60)
    print("                    FINAL REPORT")
    print("=" * 60)
    
    # Sort by score descending
    paired = list(zip(participants, scores))
    sorted_paired = sorted(paired, key=lambda x: x[1], reverse=True)
    
    print("\n--- Participant Rankings ---")
    print(f"{'Rank':<6} {'Name':<20} {'Score':<8} {'Status'}")
    print("-" * 55)
    
    for rank, (name, score) in enumerate(sorted_paired, start=1):
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"{rank:<6} {name:<20} {score:<8} {status}")
    
    print("\n--- Statistics ---")
    print("-" * 55)
    
    if scores:
        highest = max(scores)
        lowest = min(scores)
        average = sum(scores) / len(scores)
        count_highest = scores.count(highest)
        count_lowest = scores.count(lowest)
        count_distinction = sum(1 for s in scores if s >= distinction_score)
        count_qualified = sum(1 for s in scores if qualification_score <= s < distinction_score)
        count_not_qualified = sum(1 for s in scores if s < qualification_score)
        
        print(f"  Highest Score: {highest} (achieved by {count_highest} participant(s))")
        print(f"  Lowest Score: {lowest} (achieved by {count_lowest} participant(s))")
        print(f"  Average Score: {average:.2f}")
        print(f"  Total Participants: {len(participants)}")
        print(f"  Distinctions: {count_distinction}")
        print(f"  Qualified: {count_qualified}")
        print(f"  Not Qualified: {count_not_qualified}")
    
    print("\n" + "=" * 60)


# ==================== Demo: Run all functions ====================
if __name__ == "__main__":
    # Display initial data
    display_all_participants()
    
    # Check distinctions and pass
    check_distinction_and_pass()
    
    # Display scoreboard
    display_scoreboard()
    
    # Calculate statistics
    calculate_statistics()
    
    # Generate final report
    generate_final_report()
    
   