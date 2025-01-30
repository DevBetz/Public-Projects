# Define questions, answer choices, and the correct answers
questions = [
    "A business development team reports that files are missing from the database system and the server log-in screens are showing a lock symbol that requires users to contact an email address to access the system and data. Which of the following attacks is the company facing?",
    "During a security incident, the security operations team identified sustained network traffic from a malicious IP address: 10.1.4.9. A security analyst is creating an inbound firewall rule to block the IP address from accessing the organization's network. Which of the following fulfills this request?",
    "Which of the following threat actors is the most likely to use common hacking tools found on the internet to attempt to remotely compromise an organization's web server?",
    "A systems administrator would like to set up a system that will make it difficult or impossible to deny that someone has performed an action. Which of the following is the administrator trying to accomplish?",
    "Which of the following types of controls decreases the likelihood of a cybersecurity breach occurring?",
    "A company is expanding its threat surface program and allowing individuals to security test the company's internet-facing application. The company will compensate researchers based on the vulnerabilities discovered. Which of the following best describes the program the company is setting up?",
    "Which of the following is the final step of the incident response process?",
    "Which of the following provides the details about the terms of a test with a third-party penetration tester?",
    "An organization is leveraging a VPN between its headquarters and a branch location. Which of the following is the VPN protecting?",
    "Which of the following would be the most helpful in restoring data in the event of a ransomware infection?",
    "A Chief Financial Officer (CFO) has been receiving email messages that have suspicious links embedded from unrecognized senders. The emails ask the recipient for identity verification. The IT department has not received reports of this happening to anyone else. Which of the following is the MOST likely explanation for this behavior?",
    "Joe, an employee, knows he is going to be fired in three days. Which of the following characterizations describes the employee?",
    "The IT department receives a call one morning about users being unable to access files on the network shared drives. An IT technician investigates and determines the files became encrypted at 12:00 a.m. While the files are being recovered from backups, one of the IT supervisors realizes the day is the birthday of a technician who was fired two months prior. Which of the following describes what MOST likely occurred?",
    "An organization has a policy in place that states the person who approves firewall controls/changes cannot be the one implementing the changes. Which of the following describes this policy?",
    "Which of the following would be the BEST method to prevent the physical theft of staff laptops at an open-plan bank location with a high volume of customers each day?",
    "Which of the following disaster recovery sites would require the MOST time to get operations back online?",
    "A security manager needed to protect a high-security datacenter, so the manager installed an access control vestibule that can detect an employee's heartbeat, weight, and badge. Which of the following did the security manager implement?"
    "Joe, a security analyst, is asked by a co-worker, 'What is this AAA thing all about in the security world? Sounds like something I can use for my car.' Which of the following terms should Joe discuss in his response to his co-worker? (Select THREE).",
    "A system administrator is configuring accounts on a newly established server. Which of the following characteristics BEST differentiates service accounts from other types of accounts?",
    "Recently, a company has been facing an issue with shoulder surfing. Which of the following safeguards would help with this?",
    "The process of presenting a user ID to a validating system is known as:",
    "An input field that is accepting more data than has been allocated for it in memory is an attribute of:",
    "Which of the following if used would BEST reduce the number of successful phishing attacks?"
]

choices = [
    ["A. Rootkit", "B. Ransomware", "C. Spyware", "D. Bloatware"],
    ["A. access-list inbound deny ip source 0.0.0.0/0 destination 10.1.4.9/32",
     "B. access-list inbound deny ip source 10.1.4.9/32 destination 0.0.0.0/0",
     "C. access-list inbound permit ip source 10.1.4.9/32 destination 0.0.0.0/0",
     "D. access-list inbound permit ip source 0.0.0.0/0 destination 10.1.4.9/32"],
    ["A. Organized crime", "B. Insider threat", "C. Unskilled attacker", "D. Nation-state"],
    ["A. Non-repudiation", "B. Adaptive identity", "C. Security zones", "D. Deception and disruption"],
    ["A. Corrective", "B. Transfer", "C. Detective", "D. Preventive"],
    ["A. Open-source intelligence", "B. Bug bounty", "C. Red team", "D. Penetration testing"],
    ["A. Containment", "B. Lessons learned", "C. Eradication", "D. Detection"],
    ["A. Rules of engagement", "B. Supply chain analysis", "C. Right to audit clause", "D. Due diligence"],
    ["A. Data in use", "B. Data in transit", "C. Geographic restrictions", "D. Data sovereignty"],
    ["A. Load balancing", "B. Geographic dispersion", "C. Encryption", "D. Backups"],
    ["A. The CFO is the target of a whaling attack.", "B. The CFO is the target of identity fraud.", 
     "C. The CFO is receiving spam that got past the mail filters.", "D. The CFO is experiencing an impersonation attack."],
    ["A. An insider threat", "B. A competitor", "C. A hacktivist", "D. A state actor"],
    ["A. The fired technician placed a logic bomb.", "B. The fired technician installed a rootkit on all the affected users' computers.",
     "C. The fired technician installed ransomware on the file server.", "D. The fired technician left a network worm on an old work computer."],
    ["A. Change management", "B. Job rotation", "C. Separation of duties", "D. Least privilege"],
    ["A. Guards at the door", "B. Cable locks", "C. Visitor logs", "D. Cameras"],
    ["A. Colocation", "B. Cold", "C. Hot", "D. Warm"],
    ["A. A physical control", "B. A corrective control", "C. A compensating control", "D. A managerial control"]
    ["A. Accounting", "B. Accountability", "C. Authorization", "D. Authentication", "E. Access", "F. Agreement"],
    ["A. They can often be restricted in privilege.", "B. They are meant for non-person entities.",
     "C. They require special permissions to OS files and folders.", "D. They remain disabled in operations.", 
     "E. They do not allow passwords to be set."],
    ["A. Screen filters", "B. Biometric authentication", "C. Smart cards", "D. Video cameras"],
    ["A. authorization", "B. authentication", "C. identification", "D. single sign-on"],
    ["A. buffer overflow", "B. memory leak", "C. cross-site request forgery", "D. resource exhaustion"],
    ["A. Two-factor authentication", "B. Application layer firewall", "C. Mantraps", "D. User training"]
]

# Updated answer key with correct answers
answer_key = ['B', 'B', 'C', 'A', 'D', 'B', 'B', 'A', 'B', 'D', 'A', 'A', 'A', 'C', 'B', 'B', 'A', ['A', 'C', 'D'], 'B', 'A', 'C', 'A', 'D']


# Function to run the practice exam
def run_practice_exam():
    score = 0
    print("Welcome to the CompTIA Security+ Practice Exam!")
    print("Type the letter of your answer and press Enter.\n")

    # Loop through each question
    for i in range(len(questions)):
        print(f"Question {i+1}: {questions[i]}")
        for choice in choices[i]:
            print(choice)
        user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()

        # Check the answer
        if user_answer == answer_key[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {answer_key[i]}.\n")

    # Display the final score
    print(f"Your final score: {score} out of {len(questions)}")
    print("Thank you for taking the practice exam!\n")

# Run the practice exam
run_practice_exam()
