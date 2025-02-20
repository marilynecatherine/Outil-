from openai import OpenAI

# Configuration de l'API OpenAI
client = OpenAI(api_key="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")

# Fonction pour générer du texte avec GPT-3.5-turbo
def generer_texte(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Utilisation du modèle GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "Tu es un assistant marketing qui aide à créer des avatars clients et du contenu."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,  # Nombre maximum de tokens en sortie
        temperature=0.7  # Contrôle la créativité (0 = précis, 1 = créatif)
    )
    return response.choices[0].message.content.strip()

# Fonction pour générer le portrait de l'avatar client
def generer_portrait(description):
    prompt = f"Analyse cette description et extrais les traits démographiques, psychographiques et comportementaux : {description}"
    return generer_texte(prompt)

# Fonction pour générer des suggestions de publications pour les réseaux sociaux
def generer_publications(description):
    prompt = f"Génère 5 idées de publications pour les réseaux sociaux basées sur cette description de client idéal : {description}"
    return generer_texte(prompt)

# Fonction pour générer des idées d'emails marketing
def generer_emails(description):
    prompt = f"Génère 5 idées de sujets et de contenu pour des emails marketing basés sur cette description de client idéal : {description}"
    return generer_texte(prompt)

# Interface utilisateur simple
if __name__ == "__main__":
    print("Bienvenue dans le générateur d'avatar client et de contenu marketing !")
    description = input("Entrez la description de votre client idéal : ")

    if description:
        print("\nGénération du portrait de l'avatar client...")
        portrait = generer_portrait(description)
        print("\nPortrait de l'avatar client :")
        print(portrait)

        print("\nGénération des suggestions de publications pour les réseaux sociaux...")
        publications = generer_publications(description)
        print("\nSuggestions de publications pour les réseaux sociaux :")
        print(publications)

        print("\nGénération des idées pour les emails marketing...")
        emails = generer_emails(description)
        print("\nIdées pour les emails marketing :")
        print(emails)
    else:
        print("Veuillez entrer une description pour générer le contenu.")