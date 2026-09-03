import json

with open("seo.config.json", "r") as f:
    config = json.load(f)

# Add founder route
config["route_groups"].append({
    "id": "about-founder",
    "en": "/about/aamir-akwar-ali/",
    "ar": "/ar/about/aamir-akwar-ali/",
    "x-default": "en",
    "priority": 0.6,
    "changefreq": "monthly"
})

with open("seo.config.json", "w") as f:
    json.dump(config, f, indent=4)
print("Updated seo.config.json")
