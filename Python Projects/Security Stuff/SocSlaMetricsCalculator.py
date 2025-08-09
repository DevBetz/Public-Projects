"""
SOC SLA Metric Calculator

Calculates:
 - MTTD  = Mean Time To Detect (attack_start -> alert_received)
 - MTTA  = Mean Time To Acknowledge (alert_received -> triage_started)
 - MTTR  = Mean Time To Restore measured from alert received -> full_resolution

All times are entered in minutes.
"""

import statistics
import sys

def get_nonneg_float(prompt):
    while True:
        try:
            s = input(prompt).strip()
            val = float(s)
            if val < 0:
                print("Please enter a non-negative number.")
                continue
            return val
        except ValueError:
            print("Invalid number — enter minutes as a numeric value (e.g. 12 or 12.5).")

def collect_incident(index=None):
    header = f" incident #{index}" if index is not None else ""
    print(f"\nEnter times (in minutes) for{header}:")
    t_attack_to_alert = get_nonneg_float("  1) Time from attack start to alert received: ")
    t_alert_to_triage   = get_nonneg_float("  2) Time from alert received to triage started: ")
    t_triage_to_escalate = get_nonneg_float("  3) Time from triage started to escalation (0 if none): ")
    t_escalate_to_resolve = get_nonneg_float("  4) Time from escalation to full resolution (0 if none): ")

    # triage -> resolution time
    triage_to_resolution = t_triage_to_escalate + t_escalate_to_resolve

    # MTTR as time FROM ALERT RECEIVED to FULL RESOLUTION:
    mttr_from_alert = t_alert_to_triage + triage_to_resolution

    return {
        "MTTD": t_attack_to_alert,
        "MTTA": t_alert_to_triage,
        "triage_to_resolution": triage_to_resolution,
        "MTTR_alert_based": mttr_from_alert
    }

def summarize(incidents):
    if not incidents:
        print("No incidents provided.")
        return

    mttd_vals = [i["MTTD"] for i in incidents]
    mtta_vals = [i["MTTA"] for i in incidents]
    triage_vals = [i["triage_to_resolution"] for i in incidents]
    mttr_vals = [i["MTTR_alert_based"] for i in incidents]

    print("\n--- Results ---")
    if len(incidents) == 1:
        inc = incidents[0]
        print(f"MTTD (detect)                     : {inc['MTTD']:.2f} minutes")
        print(f"MTTA (acknowledge / triage start) : {inc['MTTA']:.2f} minutes")
        print(f"triage -> resolution              : {inc['triage_to_resolution']:.2f} minutes")
        print(f"MTTR (alert_received -> restore)  : {inc['MTTR_alert_based']:.2f} minutes")
    else:
        print(f"MTTD (mean)                       : {statistics.mean(mttd_vals):.2f} minutes")
        print(f"MTTA (mean)                       : {statistics.mean(mtta_vals):.2f} minutes")
        print(f"triage -> resolution (mean)       : {statistics.mean(triage_vals):.2f} minutes")
        print(f"MTTR (mean, alert_received->restore): {statistics.mean(mttr_vals):.2f} minutes")


def main():
    print("SOC SLA Metric Calculator — MTTD / MTTA / MTTR (alert-based)")
    try:
        multi = input("Enter multiple incidents? (y/n): ").strip().lower()
        incidents = []
        if multi == "y":
            while True:
                n = int(get_nonneg_float("How many incidents are we calculating?: "))
                if n >= 1:
                    break
                print("Please enter a number >= 1.")
            for i in range(1, n+1):
                incidents.append(collect_incident(index=i))
        else:
            incidents.append(collect_incident())

        summarize(incidents)

    except KeyboardInterrupt:
        print("\nAborted by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()
