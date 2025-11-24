print("🔀 TWO THINGS INVOLVED - THE ADVENTURE 🔀")
print("=" * 60)
print("In life, there are always two things involved.")
print("Tonight, they are all involved with you...\n")

name = input("What is your name, traveler? ")
print(f"\nWelcome, {name}!")
print("This story is full of silly logic, dark humor, and choices.")
print("At every stage, there are two things involved.\n")

# This is the afterlife PART of the story


def afterlife(reason):
    print("\n" + "=" * 60)
    print("💫 AFTERLIFE MODE ACTIVATED 💫")
    print(f"\nYour time on earth has ended because: {reason}")
    print("\nIn the afterlife, there are two things involved:")
    print("1. A bright staircase going up into the clouds")
    print("2. A glass elevator humming as it goes downward")

    choice_a1 = input("\nWhich do you take? (1 or 2): ")

    if choice_a1 == "1":
        print("\n☁️ You climb the bright staircase, step by step...")
        print("You reach a huge gate with two lines in front of it.")
        print("1. The STRICT line where everyone is serious and quiet")
        print("2. The CHILL line where people are laughing and vibing")

        choice_a2 = input("\nWhere do you queue? (1 or 2): ")

        if choice_a2 == "1":
            print("\n📜 An angel checks your record like a very detailed audit.")
            print("They find your procrastination, your tiny lies, and that time")
            print("you said 'I am on my way' while still in the shower.")
            print("They sigh and say:")
            print("'You are not canceled, but you still have work to do.'")
            print("\n🔁 You are sent back to earth for a second chance!")
            print("You wake up in your bed, holding your phone, with a fresh to do list.")
            print("🏁 ENDING - Reincarnated with sense.")
        elif choice_a2 == "2":
            print("\n🎉 The chill line moves fast. Nobody is pretending.")
            print("They ask you one simple question:")
            print(f"'Did you at least try to be a decent human, {name}?'")
            print("You nod. They shrug and open the gate.")
            print("\n🌈 Inside is peace, music, soft breeze, and unlimited jollof.")
            print("🏆 YOU WIN - VIP access to paradise with Wi Fi.")
        else:
            print("\n❌ You cannot pick a line. You overthink until the system times out.")
            print("You get logged out of the afterlife server.")
            print("💀 GAME OVER - Analysis paralysis.")
    elif choice_a1 == "2":
        print("\n🔥 You step into the glass elevator. It smells like smoke and shawarma.")
        print("The elevator doors open into an underworld coworking space.")
        print("Demons are on laptops. There is free coffee. It is confusing.")
        print("\nDown here there are two things involved:")
        print("1. Sign a contract to become an intern demon")
        print("2. Appeal your case with a dramatic speech")

        choice_a2 = input("\nWhat do you choose? (1 or 2): ")
# This is the underworld PART of the story
        if choice_a2 == "1":
            print("\n📝 You sign the glowing contract without reading the terms.")
            print("Congrats, you now manage the 'Unsent Angry Messages' department.")
            print("You work night shift, forever, watching drafts humans never sent.")
            print("💀 GAME OVER - Permanent internship, zero promotion.")
        elif choice_a2 == "2":
            print("\n🎙️ You grab a mic and start speaking with all your heart.")
            print(
                "You talk about struggle, growth, tiny victories, and the memes that kept you going.")
            print("The manager of the underworld HR looks touched.")
            print("'Respect. You were trying,' they say.")
            print("\nAn express elevator opens and shoots you upward.")
            print(
                "🚀 You get transferred to a neutral dimension with peace and no deadlines.")
            print("🏁 ENDING - Cosmic middle ground. Not bad at all.")
        else:
            print(
                "\n❌ You hesitate. The elevator closes and leaves you in the lobby forever.")
            print("You are now stuck listening to elevator music in a loop.")
            print("💀 GAME OVER - Infinite waiting room.")
    else:
        print("\n❌ You refuse both. A system error occurs in the universe.")
        print("You get turned into a Wi Fi signal, existing everywhere and nowhere.")
        print("💀 GAME OVER - Eternal buffering.")


print("First things first. In this story, the world tries to label you.")
print("There are two things involved:\n")
print("1. The world labels you as WOMAN")
print("2. The world labels you as MAN")

role = input("\nWhich character do you want to play as? (1 or 2): ")

if role == "1":
    print("\n👩 You are playing as someone the world labels as WOMAN.")
    print("In modern life, there are two things involved for you:")
    print("1. Soft life focus - vibes, self care, enjoyment")
    print("2. Hustle focus - work, grinding, side projects")

    choice_w1 = input("\nWhat do you lean into? (1 or 2): ")

    if choice_w1 == "1":
        print("\n✨ You choose the soft life path.")
        print("There are two things involved in your daily routine:")
        print("1. Scroll social media endlessly")
        print("2. Touch grass and mind your business")

        choice_w2 = input("\nWhat do you do first? (1 or 2): ")

        if choice_w2 == "1":
            print("\n📱 You open social media 'for 5 minutes'.")
            print("You become viral by accident after a random rant.")
            print("There are two things involved now:")
            print("1. Lean into the fame and become a creator")
            print("2. Delete the app and vanish from the timeline")

            choice_w3 = input("\nYour choice (1 or 2): ")

            if choice_w3 == "1":
                print("\n🎥 You become a full time content creator.")
                print("Endless brand deals, fake smiles, and comment wars.")
                print("One day you try a dangerous challenge for views...")
                print("It goes wrong.")
                afterlife("You chased clout until clout chased you back.")
            elif choice_w3 == "2":
                print("\n🧘 You delete the app and protect your peace.")
                print("You start journaling, reading, and studying tech.")
                print("There are two things involved with your new focus:")
                print("1. Dive into AI and coding")
                print("2. Open a small quiet cafe")

                choice_w4 = input("\nWhat do you choose? (1 or 2): ")

                if choice_w4 == "1":
                    print("\n💻 You become a calm tech baddie.")
                    print("Late nights, debugging, and shipping cool projects.")
                    print("You live a long, peaceful life, mentoring others.")
                    print("🏆 YOU WIN - Legendary in your lane.")
                elif choice_w4 == "2":
                    print(
                        "\n☕ Your cafe becomes the secret spot for artists and coders.")
                    print("One stormy night, a ceiling fan falls dramatically.")
                    afterlife("Final destination: cafe edition.")
                else:
                    print(
                        "\n❌ You cannot decide. Rent is due and the cafe closes in your mind.")
                    print("💀 GAME OVER - Indecision tax.")
            else:
                print("\n❌ You freeze halfway between posting and deleting.")
                print("The app crashes. Your phone overheats.")
                afterlife("You died of overthinking your online image.")
        elif choice_w2 == "2":
            print(
                "\n🌿 You choose peace. You take walks, drink water, mind your business.")
            print("On your walk you meet an old woman who offers two things:")
            print("1. A mysterious glowing drink")
            print("2. A dusty old book")

            choice_w3 = input("\nWhat do you accept? (1 or 2): ")

            if choice_w3 == "1":
                print("\n🥤 You drink it. Time slows. You see your whole life clearly.")
                print(
                    "You get deep wisdom about what truly matters, then your body cannot handle it.")
                afterlife("You ascended mentally a bit too fast.")
            elif choice_w3 == "2":
                print(
                    "\n📖 You read the book. It teaches balance, money, and boundaries.")
                print("You quietly build a stable, joyful life.")
                print("You die peacefully at old age, surrounded by love.")
                print("🏆 YOU WIN - Soft life with sense.")
            else:
                print("\n❌ You reject both and walk away.")
                print("Nothing bad happens, but nothing changes either.")
                print("💀 GAME OVER - Background character ending.")
        else:
            print("\n❌ Invalid choice! While you overthink, life keeps moving.")
            print("💀 GAME OVER - You were left behind by the plot.")

    elif choice_w1 == "2":
        print("\n💼 You choose the hustle path.")
        print("There are two things involved in your hustle:")
        print("1. 9 to 5 corporate route")
        print("2. Creative freelancer route")

        choice_w2 = input("\nWhich hustle do you pick? (1 or 2): ")

        if choice_w2 == "1":
            print("\n🏢 You join a serious company with endless meetings.")
            print("Your boss gives you two options:")
            print("1. Lead a risky project with big reward")
            print("2. Stay in your safe corner forever")

            choice_w3 = input("\nYour choice (1 or 2): ")

            if choice_w3 == "1":
                print("\n🚀 You work hard, pull all nighters, and ship the project.")
                print("The company grows. You become a director.")
                print("Stress is now your middle name.")
                print("One day, your body protests.")
                afterlife("You worked hard, but forgot to rest.")
            elif choice_w3 == "2":
                print("\n🪑 You stay safe, avoid risks, collect your monthly salary.")
                print("Life is calm, not exciting, but stable.")
                print("You retire peacefully with savings and small joy.")
                print("🏁 ENDING - Low drama, high stability.")
            else:
                print("\n❌ You cannot answer your boss. They move on without you.")
                print("💀 GAME OVER - Career frozen.")
        elif choice_w2 == "2":
            print("\n🎨 You go full creative mode. Design, writing, music, or tech.")
            print("There are two things involved in this life:")
            print("1. Take every job to survive")
            print("2. Say no and protect your art")

            choice_w3 = input("\nYour choice (1 or 2): ")

            if choice_w3 == "1":
                print("\n🧾 You burn out working for low pay and high stress clients.")
                print("One day, after a ridiculous revision request, you snap.")
                afterlife("Client from hell finally finished you.")
            elif choice_w3 == "2":
                print(
                    "\n🌟 You respect your craft, build slowly, and find your audience.")
                print("It takes time, but you get there.")
                print("🏆 YOU WIN - Iconic and at peace.")
            else:
                print("\n❌ You reply 'I will think about it' to every offer forever.")
                print("💀 GAME OVER - Eternal 'pending' status.")
        else:
            print("\n❌ Invalid choice! While you try to choose a hustle, bills win.")
            print("💀 GAME OVER - Overwhelmed by adulthood.")
    else:
        print("\n❌ Invalid choice! The story refuses to continue.")
        print("💀 GAME OVER - Pick a lane next time.")

elif role == "2":
    print("\n👨 You are playing as someone the world labels as MAN.")
    print("In this story, there are two things involved for you:")
    print("1. Civilian life")
    print("2. Military life")

    choice_m1 = input("\nWhich path do you choose? (1 or 2): ")

    if choice_m1 == "1":
        print("\n🏙️ You choose civilian life.")
        print("There are two things involved in your next move:")
        print("1. Stay in your country and build")
        print("2. Japa and start again elsewhere")

        choice_m2 = input("\nYour choice (1 or 2): ")

        if choice_m2 == "1":
            print("\n🌆 You stay and decide to improve things from within.")
            print("You have two strategies:")
            print("1. Go into tech and solve problems")
            print("2. Go into politics and fight the system")

            choice_m3 = input("\nYour choice (1 or 2): ")

            if choice_m3 == "1":
                print("\n💻 You grind through tutorials, bugs, and imposter syndrome.")
                print("You build tools that help people around you.")
                print("You never become super famous, but you make real impact.")
                print("🏆 YOU WIN - Quiet builder of a better world.")
            elif choice_m3 == "2":
                print("\n🎤 You join politics with a clean heart.")
                print("There are two things involved:")
                print("1. You bend a little and join them")
                print("2. You refuse and become a threat")

                choice_m4 = input("\nYour choice (1 or 2): ")

                if choice_m4 == "1":
                    print("\n💰 You change slowly, then fully.")
                    print("You get power, but lose your soul in the process.")
                    afterlife("You traded integrity for influence.")
                elif choice_m4 == "2":
                    print("\n🚨 You expose too much truth.")
                    print("You mysteriously disappear from the news.")
                    afterlife("You were too real for the timeline.")
                else:
                    print("\n❌ You give a long speech with no decision.")
                    print("People move on. Nothing changes.")
                    print("💀 GAME OVER - Background politician.")
            else:
                print("\n❌ You do not pick a strategy.")
                print("Life turns you into a professional complainer.")
                print("💀 GAME OVER - Talking without acting.")
        elif choice_m2 == "2":
            print("\n✈️ You japa with one backpack and big dreams.")
            print("There are two things involved in your journey:")
            print("1. Focus on survival jobs only")
            print("2. Balance survival with long term plans")

            choice_m3 = input("\nYour choice (1 or 2): ")

            if choice_m3 == "1":
                print("\n🧹 You work hard, send money home, but forget yourself.")
                print("One winter night, exhaustion wins.")
                afterlife("You sacrificed everything, even your health.")
            elif choice_m3 == "2":
                print("\n📚 You hustle, but also study, network, and rest sometimes.")
                print("It is slow, but you build a stable, happy life.")
                print("🏆 YOU WIN - Global citizen with sense.")
            else:
                print("\n❌ You only talk about moving, never act.")
                print("💀 GAME OVER - Permanent 'I dey go soon'.")
        else:
            print("\n❌ Invalid choice. While you decide, life moves on without you.")
            print("💀 GAME OVER - Lost in possibilities.")
    elif choice_m1 == "2":
        print("\n🪖 You join the military.")
        print("There are two things involved in your posting:")
        print("1. Office duty")
        print("2. War front")

        choice_m2 = input("\nWhere do you end up? (1 or 2): ")

        if choice_m2 == "1":
            print("\n📎 You get office duty. Files, reports, salutes.")
            print("One day you see corruption in the system.")
            print("There are two things involved:")
            print("1. Speak up and risk everything")
            print("2. Look away and stay safe")

            choice_m3 = input("\nYour choice (1 or 2): ")

            if choice_m3 == "1":
                print("\n⚖️ You speak up. Some people respect you, others do not.")
                print("You are transferred suddenly, far away.")
                afterlife(
                    "You became a hero in the story, but not in the system.")
            elif choice_m3 == "2":
                print("\n🤐 You mind your business and follow orders.")
                print("You retire quietly with mixed feelings.")
                print("🏁 ENDING - You survived, but did not shake the table.")
            else:
                print("\n❌ You write a long anonymous letter and never send it.")
                print("💀 GAME OVER - Courage stuck in drafts.")
        elif choice_m2 == "2":
            print("\n⚔️ You are sent to the war front.")
            print("There are two things involved in your first mission:")
            print("1. Charge forward like an action movie hero")
            print("2. Move carefully and protect your squad")

            choice_m3 = input("\nYour choice (1 or 2): ")

            if choice_m3 == "1":
                print("\n💥 You run in like a star. It looks cool for 3 seconds.")
                afterlife("Main character syndrome met real life consequences.")
            elif choice_m3 == "2":
                print("\n🛡️ You think as a team, not as a hero.")
                print("You survive, your people survive, and you become respected.")
                print("After many years, you retire with honor.")
                print("🏆 YOU WIN - Protector, not performer.")
            else:
                print("\n❌ You hesitate in the middle of battle.")
                print("💀 GAME OVER - No decision is also a decision.")
        else:
            print("\n❌ Invalid choice. Military life does not wait for confusion.")
            print("💀 GAME OVER - Removed from the story.")
    else:
        print("\n❌ Invalid choice! Reality rejects your input.")
        print("💀 GAME OVER - Try numbers next time.")

else:
    print("\n❌ Invalid choice! The universe cannot process it.")
    print("💀 GAME OVER - Even the narrator is confused.")

print("\n" + "=" * 60)
print("Thanks for playing 'Two Things Involved - The Adventure'!")
print("Run the game again and try different paths. 🙂")


while True:
    print("\n" + "=" * 60)
    play_again = input(
        "Would you like to play again? (yes or no): ").strip().lower()

    if play_again in ["yes", "y"]:
        print("\n🔁 Restarting the adventure...\n")
        # This should restart EVERYTHING from the top
        exec(open(__file__).read())
        break

    elif play_again in ["no", "n"]:
        print("\n👋 Thanks for playing! Come back anytime.")
        break

    else:
        print("❌ Invalid input. Please type 'yes' or 'no'.")
