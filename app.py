from flask import Flask, render_template
import json

app = Flask(__name__)

# Investment thesis paragraph
INVESTMENT_THESIS = """
I am curating a pipeline of early-stage tech ventures in Europe whose outlier founders have the potential to shape relevant industries (e.g., health, manufacturing). Despite privileging B2B software, I am refining my analysis around hardware know-how, exploring EU potential in creating the infrastructure for a world moving at high speed.
"""

# Startup data - European early-stage startups
STARTUPS = [
    {
        "name": "Resoniks",
        "tagline": "",
        "description": "Resoniks revolutionizes the quality control in the metal manufacturing sector by offering AI-powered acoustic testing for cast, forged, and welded metal parts. This guarantees precise, non-destructive inspection. Manufacturers can identify defects early, limit waste, and ensure consistent product quality in high-demand industrial environments.",
        "sector": "Manufacturing",
        "stage": "Seed",
        "year": 2024,
        "location": "Netherlands",
        "website": "https://www.resoniks.com/"
    },
    {
        "name": "Cellbox Labs",
        "tagline": "",
        "description": "Cellbox Labs provides a dynamic organ on chip platform aimed at a precise drug discovery. The combination of hardware and software ensured a flexible and efficient experimentation and minimizing manual work typically imposed on researchers.",
        "sector": "Biotechnology",
        "stage": "Pre-Seed",
        "year": 2024,
        "location": "Latvia",
        "website": "https://www.cellboxlabs.com/"
    },
    {
        "name": "Stealth",
        "tagline": "",
        "description": "App designed to track the treatment and symptoms of Parkinson's patients, breaking down barriers even for those without family support or specialized caregivers. The goal is to optimize the doctor-patient relationship and streamline the treatment journey.",
        "sector": "Healthcare",
        "stage": "Pre-Seed",
        "year": 2024,
        "location": "Italy",
        "website": ""
    },
    {
        "name": "Enapi",
        "tagline": "",
        "description": "ENAPI enables seamless connectivity for the EV charging industry by providing access to the entire EV charging ecosystem through a single API connection. The team is dedicated to building a secure and scalable infrastructure that drives the green mobility transition effectively for all stakeholders.",
        "sector": "Mobility",
        "stage": "Seed",
        "year": 2024,
        "location": "Germany",
        "website": "https://www.enapi.com/"
    },
    {
        "name": "Fluid Wire Robotics",
        "tagline": "",
        "description": "The proprietary design of Fluid Wire Robotics redefines robot construction, making it inherently adaptable to harsh environment. The design makes indeed possible the construction of any sort of innovative fully-electric force-controllable robotic arms with electric motors and sensors located in a sealed remote actuation unit.",
        "sector": "Robotics",
        "stage": "Seed",
        "year": 2024,
        "location": "Italy",
        "website": "https://www.fluidwirerobotics.com/"
    },
    {
        "name": "Ephos",
        "tagline": "",
        "description": "Ephos aims to build the essential infrastructure of the future of computing. It designs and manufacturers glass-based photonic chips which significantly reduce signal loss and energy consumption, making them ideal for advanced applications in quantum computing, artificial intelligence.",
        "sector": "Computing",
        "stage": "Seed",
        "year": 2024,
        "location": "Italy",
        "website": "https://ephos.io/"
    },
    {
        "name": "Veecle",
        "tagline": "",
        "description": "Veecle offers a subscription-based platform which decouples software applications from the hardware. OEMs and Tier 1 suppliers can design, test, and integrate software across the vehicle fleet without overhauling the existing infrastructures, for a seamless transition towards software-driven vehicles.",
        "sector": "Mobility",
        "stage": "Seed",
        "year": 2024,
        "location": "Germany",
        "website": "https://www.veecle.io/"
    },
    {
        "name": "Perciv",
        "tagline": "",
        "description": "Perciv offers an AI-driven radar perception software which converts commodity radar's inputs (or radar and camera combined) into LiDAR-comparable dense 3D point clouds, filling the gap in perception quality for automotive and robotic applications as a start.",
        "sector": "Robotics",
        "stage": "Seed",
        "year": 2024,
        "location": "Netherlands",
        "website": "https://www.perciv.ai/"
    },
    {
        "name": "Beholder",
        "tagline": "",
        "description": "Beholder leverages AI and satellite imagery to revolutionize minerals exploration, making it more efficient, cost-effective, and environmentally friendly.",
        "sector": "AI",
        "stage": "Pre-Seed",
        "year": 2024,
        "location": "Estonia",
        "website": "https://beholder.earth/"
    },
    {
        "name": "PartsCloud",
        "tagline": "",
        "description": "PartsCloud wants to streamline spare parts management for small and medium-sized enterprises (SMEs) in the mechanical engineering sector. It offers Logistics as a Service (LaaS) and Software as a Service (SaaS) to manage spare parts inventory, logistics, and fulfilment, improving operational efficiency and speed of delivery.",
        "sector": "Manufacturing",
        "stage": "Seed",
        "year": 2024,
        "location": "Germany",
        "website": "https://partscloud.com/en"
    },
    {
        "name": "Fleequid",
        "tagline": "",
        "description": "Marketplace that makes it fast and easy to buy or sell used buses through a transparent auction system. Whether looking for city, intercity, school, or touristic buses, Fleequid lets you browse hundreds of verified listings, set your own price, and finalize a purchase in 7 days.",
        "sector": "Mobility",
        "stage": "Seed",
        "year": 2024,
        "location": "Italy",
        "website": "https://fleequid.com/en"
    },
    {
        "name": "Arsenale (Bio)",
        "tagline": "",
        "description": "Arsenale Bio is a proprietary, AI powered end-to-end platform making biomanufacturing via precision fermentation viable at industrial scale. Its mission? Lead a new industrial era which transforms how materials, food and energy are produced and co-desig with nature novel bio-solutions.",
        "sector": "Manufacturing",
        "stage": "Seed",
        "year": 2024,
        "location": "Italy",
        "website": "https://arsenale.bio/"
    },
    {
        "name": "Capsule Corporation",
        "tagline": "",
        "description": "Capsule Corporation is a cutting-edge provider of water-based propulsion systems specifically for CubeSats and SmallSats, designed to facilitate a broader range of satellite missions and improve space sustainability, expanding satellites lifespan and reducing the de-orbiting risk.",
        "sector": "Aerospace",
        "stage": "Seed",
        "year": 2024,
        "location": "Italy",
        "website": "https://www.capsule-corp.biz/index.html"
    },
    {
        "name": "Kiutra",
        "tagline": "",
        "description": "Kiutra offers a super-fast cooling system called the L-Type Rapid Cryostat that helps scientists and engineers quickly test and understand materials and devices at extremely cold temperatures.",
        "sector": "Quantum Technologies",
        "stage": "Seed",
        "year": 2024,
        "location": "Germany",
        "website": "https://kiutra.com/"
    },
    {
        "name": "Xelerit",
        "tagline": "",
        "description": "AI-powered Agentic Development Environment (ADE) for industrial automation, streamlining the entire workflow from hardware integration and code generation to testing and deployment.",
        "sector": "AI",
        "stage": "Pre-Seed",
        "year": 2024,
        "location": "Switzerland",
        "website": "https://www.xelerit-robotics.com/"
    },
    {
        "name": "Salupay",
        "tagline": "",
        "description": "Saas solution designed to digitalize, streamline, and automate the administrative and financial workflows in private healthcare facilities",
        "sector": "Insurtech",
        "stage": "Seed",
        "year": 2024,
        "location": "Italy",
        "website": "https://salupay.it/"
    }
]

@app.route('/')
def index():
    return render_template('index.html', startups=STARTUPS, thesis=INVESTMENT_THESIS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

