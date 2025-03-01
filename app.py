from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static")

# iPhone models with colors, storage, updated pricing, and images (only original models kept)
IPHONE_DATA = {
    "iPhone 11": {
        "base_price": 6000,  # Updated from your new list (64GB)
        "colors": ["Black", "White", "Green", "Yellow", "Purple", "Red"],
        "storage": {64: 0, 128: 500, 256: 1000},  # 6500-6000=500, 7000-6000=1000
        "images": {
            "Black": "static/images/iphone_11/Black/iphone11-black.jpeg",
            "White": "static/images/iphone_11/White/Apple iPhone 11 Pro_ Aesthetic Christmas Gift in Black and White.jpeg",
            "Green": "static/images/iphone_11/Green/Iphone 11 green💚.jpeg",
            "Yellow": "static/images/iphone_11/Yellow/iPhone 11 yellow baby💜😁❤️.jpeg",
            "Purple": "static/images/iphone_11/Purple/download.jpeg",
            "Red": "static/images/iphone_11/Red/We Heart It.jpeg"
        }
    },
    "iPhone 11 Pro": {
        "base_price": 8500,  # Updated (64GB)
        "colors": ["Space Gray", "Silver", "Gold", "Midnight Green"],
        "storage": {64: 0, 256: 500, 512: 1000},  # 9000-8500=500, 9500-8500=1000
        "images": {
            "Space Gray": "static/images/iPhone_11_Pro/Space_Gray/iPhone 11 Pro.jpeg",
            "Silver": "static/images/iPhone_11_Pro/Silver/74ec4ae1-047a-426c-9c8b-4a0f87a95d09.jpeg",
            "Gold": "static/images/iPhone_11_Pro/Gold/iPhone 11 Pro.jpeg",
            "Midnight Green": "static/images/iPhone_11_Pro/Midnight_Green/iPhone 11 Pro Max (1).jpeg"
        }
    },
    "iPhone 11 Pro Max": {
        "base_price": 9000,  # Updated (64GB)
        "colors": ["Space Gray", "Silver", "Gold", "Midnight Green"],
        "storage": {64: 0, 256: 500, 512: 1000},  # 9500-9000=500, 10000-9000=1000
        "images": {
            "Space Gray": "static/images/iPhone_11_Pro/Space_Gray/iPhone 11 Pro.jpeg",
            "Silver": "static/images/iPhone_11_Pro/Silver/74ec4ae1-047a-426c-9c8b-4a0f87a95d09.jpeg",
            "Gold": "static/images/iPhone_11_Pro/Gold/iPhone 11 Pro.jpeg",
            "Midnight Green": "static/images/iPhone_11_Pro/Midnight_Green/iPhone 11 Pro Max (1).jpeg"
        }
    },
    "iPhone 12": {
        "base_price": 10000,  # Updated (64GB)
        "colors": ["Black", "White", "Blue", "Green", "Red", "Purple"],
        "storage": {64: 0, 128: 500, 256: 1000},  # 10500-10000=500, 11000-10000=1000
        "images": {
            "Black": "static/images/iPhone_12/Black/Amazon_com_ Apple Products.jpeg",
            "White": "static/images/iPhone_12/White/Jesus ✡︎.jpeg",
            "Blue": "static/images/iPhone_12/Blue/6170a780-5a1f-46c1-b279-2ca5964b4339.jpeg",
            "Green": "static/images/iPhone_12/Green/iPhone 12 (1).jpeg",
            "Red": "static/images/iPhone_12/Red/We Heart It.jpeg",
            "Purple": "static/images/iPhone_12/Purple/IPhone 12 Unlocked Purple.jpeg"
        }
    },
    "iPhone 12 Pro": {
        "base_price": 12000,  # Updated (128GB)
        "colors": ["Graphite", "Silver", "Gold", "Pacific Blue"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 12500-12000=500, 13000-12000=1000
        "images": {
            "Graphite": "static/images/iPhone_12_Pro/Graphite/iPhone 12 Pro Graphite.jpeg",
            "Silver": "static/images/iPhone_12_Pro/Silver/IPhone 12 Pro Max Silver.jpeg",
            "Gold": "static/images/iPhone_12_Pro/Gold/iPhone 12 pro gold.jpeg",
            "Pacific Blue": "static/images/iPhone_12_Pro/Pacific Blue/iPhone12_Pro_Pacific_Blue.jpeg"
        }
    },
    "iPhone 12 Pro Max": {
        "base_price": 13000,  # Updated (128GB)
        "colors": ["Graphite", "Silver", "Gold", "Pacific Blue"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 13500-13000=500, 14000-13000=1000
        "images": {
            "Graphite": "static/images/iPhone_12_Pro/Graphite/iPhone 12 Pro Graphite.jpeg",
            "Silver": "static/images/iPhone_12_Pro/Silver/IPhone 12 Pro Max Silver.jpeg",
            "Gold": "static/images/iPhone_12_Pro/Gold/iPhone 12 pro gold.jpeg",
            "Pacific Blue": "static/images/iPhone_12_Pro/Pacific Blue/iPhone12_Pro_Pacific_Blue.jpeg"
        }
    },
    "iPhone 13": {
        "base_price": 11000,  # Updated (128GB)
        "colors": ["Pink", "Blue", "Midnight", "Starlight", "Red", "Green"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 11500-11000=500, 12000-11000=1000
        "images": {
            "Pink": "static/images/iPhone_13/Pink/Pink iPhone (1).jpeg",
            "Blue": "static/images/iPhone_13/Blue/fed3a452-eaea-4b01-8efc-b21bf579111d.jpeg",
            "Midnight": "static/images/iPhone_13/Midnight/iPhone 13.jpeg",
            "Starlight": "static/images/iPhone_13/Starlight/iPhone 13 starlight (1).jpeg",
            "Red": "static/images/iPhone_13/Red/red_____.jpeg",
            "Green": "static/images/iPhone_13/Green/(manifestando).jpeg"
        }
    },
    "iPhone 13 Pro": {
        "base_price": 13500,  # Updated (128GB)
        "colors": ["Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 14000-13500=500, 14500-13500=1000
        "images": {
            "Graphite": "static/images/iPhone_13_Pro/Graphite/iPhone 13 colors - iPhone 13 pro Graphite color.jpeg",
            "Gold": "static/images/iPhone_13_Pro/Gold/iphone 13 pro max in gold [Video] in 2021 _ Iphone… (1).jpeg",
            "Silver": "static/images/iPhone_13_Pro/Silver/33dba9b2-a69b-4b0e-b27f-9e73244351fe.jpeg",
            "Sierra Blue": "static/images/iPhone_13_Pro/Sierra_Blue/iPhone 13 Pro sierra blue 256gb.jpeg",
            "Alpine Green": "static/images/iPhone_13_Pro/Alpine_Green/iphone 13 pro unlocked 128gb Alpine Green.jpeg"
        }
    },
    "iPhone 13 Pro Max": {
        "base_price": 14500,  # Updated (128GB)
        "colors": ["Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 15000-14500=500, 15500-14500=1000
        "images": {
            "Graphite": "static/images/iPhone_13_Pro/Graphite/iPhone 13 colors - iPhone 13 pro Graphite color.jpeg",
            "Gold": "static/images/iPhone_13_Pro/Gold/iphone 13 pro max in gold [Video] in 2021 _ Iphone… (1).jpeg",
            "Silver": "static/images/iPhone_13_Pro/Silver/33dba9b2-a69b-4b0e-b27f-9e73244351fe.jpeg",
            "Sierra Blue": "static/images/iPhone_13_Pro/Sierra_Blue/iPhone 13 Pro sierra blue 256gb.jpeg",
            "Alpine Green": "static/images/iPhone_13_Pro/Alpine_Green/iphone 13 pro unlocked 128gb Alpine Green.jpeg"
        }
    },
    "iPhone 14": {
        "base_price": 14000,  # Updated (128GB)
        "colors": ["Midnight", "Starlight", "Blue", "Purple", "Red", "Yellow"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 14500-14000=500, 15000-14000=1000
        "images": {
            "Midnight": "static/images/iPhone_14/Midnight/iPhone 14_ 512gb _ Color - Midnight Black _ unlocked _ new in box _ original.jpeg",
            "Starlight": "static/images/iPhone_14/Starlight/iPhone 14 Plus Starlight.jpeg",
            "Blue": "static/images/iPhone_14/Blue/iPhone 15 blue (1).jpeg",
            "Purple": "static/images/iPhone_14/Purple/iPhone 15 pro max iPhone 15 aesthetic iPhone iOS aesthetic iPhone 15 pro iPhone 15 pro max case (1).jpeg",
            "Red": "static/images/iPhone_14/Red/iphone 13 mini apple product red marina bay sands singapore.jpeg",
            "Yellow": "static/images/iPhone_14/Yellow/iPhone Aesthetic.jpeg"
        }
    },
    "iPhone 14 Pro": {
        "base_price": 15500,  # Updated (128GB)
        "colors": ["Space Black", "Silver", "Gold", "Deep Purple"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 16000-15500=500, 16500-15500=1000
        "images": {
            "Space Black": "static/images/iPhone_14_Pro/Space_Black/İphone.jpeg",
            "Silver": "static/images/iPhone_14_Pro/Silver/c2105762-d28b-4079-be87-4c6370bd11ad.jpeg",
            "Gold": "static/images/iPhone_14_Pro/Gold/iphone 14 pro max battery life (1).jpeg",
            "Deep Purple": "static/images/iPhone_14_Pro/Deep_Purple/im selling my iPhone 14 Pro Max Blue.jpeg"
        }
    },
    "iPhone 14 Pro Max": {
        "base_price": 16500,  # Updated (128GB)
        "colors": ["Space Black", "Silver", "Gold", "Deep Purple"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 17000-16500=500, 17500-16500=1000
        "images": {
            "Space Black": "static/images/iPhone_14_Pro/Space_Black/İphone.jpeg",
            "Silver": "static/images/iPhone_14_Pro/Silver/c2105762-d28b-4079-be87-4c6370bd11ad.jpeg",
            "Gold": "static/images/iPhone_14_Pro/Gold/iphone 14 pro max battery life (1).jpeg",
            "Deep Purple": "static/images/iPhone_14_Pro/Deep_Purple/im selling my iPhone 14 Pro Max Blue.jpeg"
        }
    },
    "iPhone 15": {
        "base_price": 16000,  # Updated (128GB)
        "colors": ["Black", "Blue", "Green", "Yellow", "Pink"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 16500-16000=500, 17000-16000=1000
        "images": {
            "Black": "static/images/iPhone_15/Black/iPhone 15.jpeg",
            "Blue": "static/images/iPhone_15/Blue/Kup produkt iPhone 15 128 GB – niebieski.jpeg",
            "Green": "static/images/iPhone_15/Green/🥑🪀🍵🌱🥛.jpeg",
            "Yellow": "static/images/iPhone_15/Yellow/iphone 15 in yellow 🌼🫧.jpeg",
            "Pink": "static/images/iPhone_15/Pink/Iphone 15 pink🎀✨💗.jpeg"
        }
    },
    "iPhone 15 Pro": {
        "base_price": 17500,  # Updated (128GB)
        "colors": ["Black Titanium", "White Titanium", "Natural Titanium", "Blue Titanium"],
        "storage": {128: 0, 256: 500, 512: 1000},  # 18000-17500=500, 18500-17500=1000
        "images": {
            "Black Titanium": "static/images/iPhone_15_Pro/Black_Titanium/IPhone 15 Pro Black Titanium.jpeg",
            "White Titanium": "static/images/iPhone_15_Pro/White_Titanium/Apple Iphone 15 Pro Max titanium Branco - link abaixo de como tirar foto com iphone.jpeg",
            "Natural Titanium": "static/images/iPhone_15_Pro/Natural_Titanium/iphone 15 pro natural titanium.jpeg"
        }
    },
    "iPhone 15 Pro Max": {
        "base_price": 18500,  # Updated (128GB)
        "colors": ["Black Titanium", "White Titanium", "Natural Titanium", "Blue Titanium"],
        "storage": {256: 500, 512: 1000},  # Base at 128GB, 256GB=19000-18500=500, 512GB=19500-18500=1000
        "images": {
            "Black Titanium": "static/images/iPhone_15_Pro/Black_Titanium/IPhone 15 Pro Black Titanium.jpeg",
            "White Titanium": "static/images/iPhone_15_Pro/White_Titanium/Apple Iphone 15 Pro Max titanium Branco - link abaixo de como tirar foto com iphone.jpeg",
            "Natural Titanium": "static/images/iPhone_15_Pro/Natural_Titanium/iphone 15 pro natural titanium.jpeg"
        }
    }
}

@app.route("/")
def home():
    return render_template("index.html", iphone_data=IPHONE_DATA)

@app.route("/get_options", methods=["POST"])
def get_options():
    data = request.json
    model = data.get("model")

    if model in IPHONE_DATA:
        return jsonify({
            "colors": IPHONE_DATA[model]["colors"],
            "storage": list(IPHONE_DATA[model]["storage"].keys())
        })
    
    return jsonify({"error": "Invalid model"}), 400

@app.route("/get_price", methods=["POST"])
def get_price():
    data = request.json
    model = data.get("model")
    storage = int(data.get("storage", 64))  # Default to 64GB if not specified

    if model in IPHONE_DATA:
        base_price = IPHONE_DATA[model]["base_price"]
        storage_price = IPHONE_DATA[model]["storage"].get(storage, 0)
        final_price = base_price + storage_price
        return jsonify({"price": final_price})

    return jsonify({"error": "Invalid selection"}), 400

@app.route("/get_image", methods=["POST"])
def get_image():
    data = request.json
    model = data.get("model")
    color = data.get("color")

    if model in IPHONE_DATA and color in IPHONE_DATA[model]["images"]:
        return jsonify({"image": IPHONE_DATA[model]["images"][color]})

    return jsonify({"error": "Image not found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
