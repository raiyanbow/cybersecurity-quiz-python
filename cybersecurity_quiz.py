print("=== Cybersecurity Quiz ===")

score = 0

answer = input("1. What does VPN stand for? ")

if answer.lower() == "virtual private network":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("\n2. What is used to protect a network from threats? ")

if answer.lower() == "firewall":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("\n3. What type of attack tries to trick users into giving information? ")

if answer.lower() == "phishing":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("\n4. What does HTTPS provide? ")

if answer.lower() == "security":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("\n5. What is malware? ")

if answer.lower() == "malicious software":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nFinal Score:", score, "/5")