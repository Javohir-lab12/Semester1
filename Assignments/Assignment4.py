def calculate_sales_amount(meal_type, table_count, service_level):
    if meal_type == "breakfast":
        if service_level == "low":
            price = 30
        elif service_level == "medium":
            price = 45
        elif service_level == "high":
            price = 60
        else:
            return "Availabe service levels: low, medium, high"
    elif meal_type == "lunch":
        if service_level == "low":
            price = 40
        elif service_level == "medium":
            price = 65
        elif service_level == "high":
            price = 90
        else:
            return "Availabe service levels: low, medium, high"
    elif meal_type == "dinner":
        if service_level == "low":
            price = 55
        elif service_level == "medium":
            price = 85
        elif service_level == "high":
            price = 125
        else:
            return "Availabe service levels: low, medium, high"
    else:
        return "Available meal types: lunch, breakfast, dinner"
    return price * table_count

def calculate_efficiency_score(shift_years, standard_tables, served_tables):
    expected_tables = 1000 + (shift_years * 100)
    table_capacity = expected_tables - standard_tables
    efficiency_percentage = round(((served_tables - standard_tables) / table_capacity) * 100)
    return round(efficiency_percentage, 1)

def determine_service_rating(efficiency_percent):
    if efficiency_percent <= 50:
        return "Learning stage"
    elif efficiency_percent <= 60:
        return "Cpable stage"
    elif efficiency_percent <= 70:
        return "Skilled stage"
    elif efficiency_percent <= 85:
        return "Accomplished stage"
    else:
        return "Master stage"

def calculate_tip_earnings(sales, tables,stage):
    if stage == "Learning":
        rating_bonus = 0.5
    elif stage == "Capable":
        rating_bonus = 1
    elif stage == "Skilled":
        rating_bonus = 1.2
    elif stage == "Accomplished":
        rating_bonus = 1.5
    elif stage == "Master":
        rating_bonus= 1.8
    else:
        return "Wrong input"
         
    base_tips = sales * 0.05 + tables * 2
    final_tips = round((base_tips * rating_bonus), 1)
    return final_tips

def requires_mentoring(service_weeks, total_tables, avg_efficiency):
    if service_weeks >= 6 and avg_efficiency < 50:
        return True
    if total_tables < 100 and avg_efficiency < 60:
        return True
    if service_weeks >= 4 and avg_efficiency < 40:
        return True

def generate_service_summary(stage, server, meal_type, tables, service_level,
                             shift_years, standard_tables, served_tables, service_weeks):
    sales = calculate_sales_amount(meal_type, tables, service_level)
    efficiency = calculate_efficiency_score(shift_years, standard_tables, served_tables)
    rating = determine_service_rating(efficiency)
    tips = calculate_tip_earnings(sales, tables, stage)
    mentoring = requires_mentoring(service_weeks, served_tables, efficiency)
    print("========================================")
    print(f"Service Summary for: {server}")
    print("----------------------------------------")
    print(f"Meal Type: {meal_type}")
    print(f"Tables Served: {tables}")
    print(f"Service Level: {service_level}")    
    print(f"Sales Amount: ${sales}")
    print("Efficiency Analysis:")
    print(f"  Experience: {shift_years} years, Standard: {standard_tables}, Served Tables: {served_tables}")
    print(f"  Efficiency: {efficiency}%")
    print(f"  Service Rating: {rating}")
    print(f"Tip Earnings: ${tips}")
    print(f"Service Weeks: {service_weeks}")
    print(f"Mentoring Required: {'Yes' if mentoring else 'No'}")
    print()
print("RESTAURANT SERVICE ANALYZER")
generate_service_summary("Accomplished", "Quinn", "dinner", 45, "high", 3, 800, 1150, 3)
generate_service_summary("Skilled", "Reese", "lunch", 60, "medium", 5, 900, 1300, 5)
generate_service_summary("Learning", "Skyler", "breakfast", 30, "low", 8, 850, 950, 7)
