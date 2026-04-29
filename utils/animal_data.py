"""
Animal species data — facts, habitat, fun facts, emoji, sound description.
Used by the /animal-info/<species> route.
"""

ANIMAL_DATA = {
    "dog": {
        "name": "Dog",
        "emoji": "🐕",
        "scientific_name": "Canis lupus familiaris",
        "description": "Dogs are domesticated mammals, not natural wild animals. They were originally bred from wolves and have been selectively bred over centuries for various behaviors, sensory capabilities, and physical attributes.",
        "habitat": "Domesticated worldwide. Found in homes, farms, and working environments across every continent except Antarctica.",
        "sound_description": "Dogs communicate through barking, howling, whining, and growling. Each vocalization serves a different purpose — barking for alerting, howling for long-distance communication, and whining for attention.",
        "fun_facts": [
            "A dog's sense of smell is 10,000 to 100,000 times more sensitive than a human's.",
            "Dogs can understand up to 250 words and gestures, making them as intelligent as a 2-year-old child.",
            "The Basenji is the only breed of dog that can't bark — it produces a yodel-like sound instead."
        ],
        "avg_lifespan": "10–13 years",
        "diet": "Omnivore"
    },
    "cat": {
        "name": "Cat",
        "emoji": "🐱",
        "scientific_name": "Felis catus",
        "description": "Cats are small, carnivorous mammals that have been domesticated for thousands of years. They are known for their agility, independence, and affectionate behavior toward their human companions.",
        "habitat": "Domesticated worldwide. Cats thrive in both indoor and outdoor environments, from urban apartments to rural farms.",
        "sound_description": "Cats produce a wide range of vocalizations including meowing, purring, hissing, and chirping. Purring occurs at 25-150 Hz and has been shown to promote healing.",
        "fun_facts": [
            "Cats spend 70% of their lives sleeping — that's about 13-16 hours a day!",
            "A group of cats is called a 'clowder', and a group of kittens is called a 'kindle'.",
            "Cats can rotate their ears 180 degrees using 32 muscles in each ear."
        ],
        "avg_lifespan": "12–18 years",
        "diet": "Obligate Carnivore"
    },
    "cow": {
        "name": "Cow",
        "emoji": "🐄",
        "scientific_name": "Bos taurus",
        "description": "Cows are large domesticated ungulates that are among the most common farm animals worldwide. They are raised for milk, meat, and leather production, and have been domesticated for approximately 10,000 years.",
        "habitat": "Farms and grasslands worldwide. They prefer temperate climates with ample grazing land and access to fresh water.",
        "sound_description": "Cows communicate through mooing, which varies in pitch and duration depending on their emotional state. Mother cows have distinct calls to communicate with their calves.",
        "fun_facts": [
            "Cows have nearly 360-degree panoramic vision and can see in color.",
            "A cow can produce up to 200,000 glasses of milk in her lifetime.",
            "Cows have best friends and become stressed when they are separated from them."
        ],
        "avg_lifespan": "18–22 years",
        "diet": "Herbivore"
    },
    "pig": {
        "name": "Pig",
        "emoji": "🐷",
        "scientific_name": "Sus scrofa domesticus",
        "description": "Pigs are highly intelligent and social domesticated animals. They are one of the oldest forms of livestock, having been domesticated around 9,000 years ago in China and Western Asia.",
        "habitat": "Farms worldwide. Wild relatives (boars) inhabit forests, grasslands, and wetlands across Europe and Asia.",
        "sound_description": "Pigs communicate through oinks, grunts, squeals, and snorts. They have over 20 different vocalizations, each conveying a different message from hunger to happiness.",
        "fun_facts": [
            "Pigs are considered the 5th most intelligent animal in the world — smarter than dogs!",
            "Pigs can't sweat, which is why they roll in mud to cool down. The mud also acts as sunscreen.",
            "A pig's squeal can be as loud as 115 decibels — louder than a jet engine at takeoff!"
        ],
        "avg_lifespan": "15–20 years",
        "diet": "Omnivore"
    },
    "frog": {
        "name": "Frog",
        "emoji": "🐸",
        "scientific_name": "Order Anura",
        "description": "Frogs are amphibians known for their croaking sounds, jumping abilities, and aquatic lifestyle. There are over 7,000 species of frogs found on every continent except Antarctica.",
        "habitat": "Found in tropical rainforests, temperate forests, wetlands, ponds, and streams. They require moist environments for survival and breeding.",
        "sound_description": "Male frogs produce a wide variety of calls to attract mates and defend territory. Their calls are produced by passing air over vocal cords in a laryngeal sac, which amplifies the sound.",
        "fun_facts": [
            "The golden poison dart frog has enough venom to kill 10 grown men.",
            "Frogs absorb water through their skin — they literally drink through their body!",
            "Some frogs can freeze solid during winter and thaw back to life in spring."
        ],
        "avg_lifespan": "10–12 years",
        "diet": "Carnivore (insects)"
    },
    "rooster": {
        "name": "Rooster",
        "emoji": "🐓",
        "scientific_name": "Gallus gallus domesticus",
        "description": "Roosters are adult male chickens known for their distinctive crowing at dawn. They play an important role in the flock as protectors and leaders, alerting hens to food sources and potential danger.",
        "habitat": "Domesticated worldwide on farms and in rural areas. Wild ancestors (Red Junglefowl) are native to Southeast Asia.",
        "sound_description": "The iconic 'cock-a-doodle-doo' crow is used to establish territory and signal the start of a new day. Roosters also make clucking sounds to alert their flock to food or danger.",
        "fun_facts": [
            "A rooster's crow can reach up to 130 decibels — they have a built-in earplug that prevents them from going deaf!",
            "Roosters perform a 'tidbit dance' where they pick up food and drop it to impress hens.",
            "Each rooster has a unique crow that hens can distinguish from other roosters."
        ],
        "avg_lifespan": "5–8 years",
        "diet": "Omnivore"
    },
    "hen": {
        "name": "Hen",
        "emoji": "🐔",
        "scientific_name": "Gallus gallus domesticus",
        "description": "Hens are adult female chickens and are among the most widespread domestic animals. They are highly social, intelligent birds capable of recognizing over 100 individual faces.",
        "habitat": "Domesticated worldwide. Found on farms, smallholdings, and increasingly in urban backyard coops.",
        "sound_description": "Hens produce a variety of clucks, cackles, and purring sounds. They have distinct calls for aerial predators vs ground predators, and a special 'egg song' after laying.",
        "fun_facts": [
            "Hens can dream — they experience REM sleep just like humans.",
            "A hen communicates with her chick while it's still inside the egg, and the chick chirps back!",
            "Hens have over 30 different vocalizations to communicate various messages to their flock."
        ],
        "avg_lifespan": "5–10 years",
        "diet": "Omnivore"
    },
    "crow": {
        "name": "Crow",
        "emoji": "🐦‍⬛",
        "scientific_name": "Corvus",
        "description": "Crows are remarkably intelligent birds belonging to the corvid family. They are known for their problem-solving abilities, tool use, and complex social structures.",
        "habitat": "Found on every continent except Antarctica. They thrive in diverse environments including forests, farmlands, urban areas, and coastlines.",
        "sound_description": "Crows produce a distinctive 'caw-caw' call, along with a repertoire of clicks, rattles, and even mimicked sounds. Their calls serve as alarms, territorial markers, and social communication.",
        "fun_facts": [
            "Crows can recognize and remember human faces — and they hold grudges!",
            "Crows have been observed using tools, solving multi-step puzzles, and even understanding water displacement.",
            "A group of crows is called a 'murder', and they hold 'funerals' when one of their own dies."
        ],
        "avg_lifespan": "7–8 years (wild), 20+ years (captivity)",
        "diet": "Omnivore"
    },
    "sheep": {
        "name": "Sheep",
        "emoji": "🐑",
        "scientific_name": "Ovis aries",
        "description": "Sheep are domesticated ruminant mammals raised for their wool, meat, and milk. They have been herded by humans since around 10,000 BC, making them one of the earliest domesticated animals.",
        "habitat": "Farms and grasslands worldwide. They prefer temperate climates with rolling hills and open pastures.",
        "sound_description": "Sheep communicate through bleating, which varies in pitch, volume, and frequency. Lambs and mothers recognize each other's individual bleats within large flocks.",
        "fun_facts": [
            "Sheep have excellent memories and can remember up to 50 individual sheep and 10 human faces for years.",
            "Sheep have rectangular pupils, giving them a field of vision of about 300 degrees without turning their heads.",
            "Sheep self-medicate — when sick, they seek out specific plants to eat that help them recover."
        ],
        "avg_lifespan": "10–12 years",
        "diet": "Herbivore"
    },
    "chirping_birds": {
        "name": "Chirping Birds",
        "emoji": "🐦",
        "scientific_name": "Order Passeriformes",
        "description": "Chirping birds (passerines or songbirds) make up more than half of all bird species. They are characterized by their complex, musical vocalizations used for mating, territory defense, and communication.",
        "habitat": "Found in virtually every terrestrial habitat on Earth — forests, grasslands, deserts, wetlands, mountains, and urban areas.",
        "sound_description": "Songbirds produce melodious chirps, trills, and songs. Each species has a unique song, and individual birds may learn hundreds of variations throughout their lifetime.",
        "fun_facts": [
            "Some songbirds can sing two notes simultaneously using a specialized vocal organ called the syrinx.",
            "Baby songbirds learn their songs by listening to adults, similar to how human babies learn language.",
            "The Australian lyrebird can mimic chainsaws, camera shutters, and even car alarms!"
        ],
        "avg_lifespan": "2–5 years (small), 10+ years (larger species)",
        "diet": "Varies (seeds, insects, nectar)"
    },
    "crickets": {
        "name": "Crickets",
        "emoji": "🦗",
        "scientific_name": "Family Gryllidae",
        "description": "Crickets are insects closely related to grasshoppers. They are best known for their chirping song, which is produced by males rubbing their forewings together in a process called stridulation.",
        "habitat": "Found worldwide in grasslands, forests, caves, and even in human homes. They prefer warm, dark, and moist environments.",
        "sound_description": "The characteristic chirping is produced by rubbing a scraper on one wing against teeth on the other. The rate of chirping is directly related to temperature — you can estimate the temperature by counting chirps!",
        "fun_facts": [
            "You can estimate the temperature in Fahrenheit by counting cricket chirps in 14 seconds and adding 40.",
            "Crickets have ears located on their front legs, just below the knee joint.",
            "Crickets are considered a delicacy in many cultures and are a sustainable protein source with 3x more protein than beef per gram."
        ],
        "avg_lifespan": "2–3 months",
        "diet": "Omnivore"
    },
    "insects": {
        "name": "Insects",
        "emoji": "🪲",
        "scientific_name": "Class Insecta",
        "description": "Insects are the most diverse group of animals on Earth, with over 1 million described species. Their sounds range from buzzing wings to rhythmic stridulation, playing crucial roles in ecosystems.",
        "habitat": "Found in virtually every habitat on Earth — forests, deserts, freshwater, soil, and even inside other organisms. They cannot survive in ocean environments.",
        "sound_description": "Insects produce sounds through various mechanisms: wing vibration (bees, flies), stridulation (rubbing body parts together), and tymbals (cicadas). These sounds serve for mating, warning, and territory defense.",
        "fun_facts": [
            "For every human on Earth, there are approximately 1.4 billion insects.",
            "Some insects can survive being frozen solid, and others can withstand extreme radiation.",
            "The loudest insect is the African cicada, whose call can reach 107 decibels — as loud as a power saw!"
        ],
        "avg_lifespan": "Days to 17 years (varies greatly)",
        "diet": "Varies (herbivore, carnivore, omnivore, detritivore)"
    }
}


def get_animal_info(species_key):
    """Get animal info dict for a given species key. Returns None if not found."""
    return ANIMAL_DATA.get(species_key, None)


def get_all_species():
    """Get a list of all species with name and emoji."""
    return [
        {"key": k, "name": v["name"], "emoji": v["emoji"]}
        for k, v in ANIMAL_DATA.items()
    ]
