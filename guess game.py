import random

secret_number = random.randint(1, 10)
guess = int(input("خمن رقم من 1 لـ 10: "))

if guess == secret_number:
    print("🎉 مبروك! خمنت صح!")
else:
    print("❌ غلط! الرقم كان", secret_number)
