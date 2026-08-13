from emailsend import send_email

print("=" * 50)
print("       EMAIL SENDING APPLICATION")
print("=" * 50)

receiver = input("Enter Receiver Email : ")
subject = input("Enter Subject        : ")

print("\nEnter Message (Press Enter when done):")
message = input("> ")

result = send_email(receiver, subject, message)

print("\n" + "=" * 50)
print(result)
print("=" * 50)