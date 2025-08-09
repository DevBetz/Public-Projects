# SOC Metrics Calculator

def calculate_alerts_count(total_alerts):
    return total_alerts

def calculate_false_positive_rate(false_positives, total_alerts):
    return (false_positives / total_alerts) * 100

def calculate_alert_escalation_rate(escalated_alerts, total_alerts):
    return (escalated_alerts / total_alerts) * 100

def calculate_threat_detection_rate(detected_threats, total_threats):
    return (detected_threats / total_threats) * 100

def main():
    print("\nSOC Metrics Calculator")
    print("1. Alerts Count (AC)")
    print("2. False Positive Rate (FPR)")
    print("3. Alert Escalation Rate (AER)")
    print("4. Threat Detection Rate (TDR)")
    
    choice = input("\nSelect the metric you want to calculate (1-4): ")

    if choice == "1":
        total_alerts = int(input("Enter total count of alerts received: "))
        print(f"Alerts Count (AC) = {calculate_alerts_count(total_alerts)}")

    elif choice == "2":
        false_positives = int(input("Enter number of false positives: "))
        total_alerts = int(input("Enter total count of alerts received: "))
        print(f"False Positive Rate (FPR) = {calculate_false_positive_rate(false_positives, total_alerts):.2f}%")

    elif choice == "3":
        escalated_alerts = int(input("Enter number of escalated alerts: "))
        total_alerts = int(input("Enter total count of alerts received: "))
        print(f"Alert Escalation Rate (AER) = {calculate_alert_escalation_rate(escalated_alerts, total_alerts):.2f}%")

    elif choice == "4":
        detected_threats = int(input("Enter number of detected threats: "))
        total_threats = int(input("Enter total number of threats: "))
        print(f"Threat Detection Rate (TDR) = {calculate_threat_detection_rate(detected_threats, total_threats):.2f}%")

    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
