import os
import requests

url = "https://www.tiktok.com/@yomidenzel/video/7304641225087356192?is_from_webapp=1&sender_device=pc"  # Remplacez ceci par l'URL de votre vidéo

# Effectuer une requête GET pour récupérer le contenu de la vidéo
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut HTTP 200)
if response.status_code == 200:
    # Nom du fichier de sortie pour la vidéo téléchargée
    nom_fichier = "ma_video.mp4"  # Vous pouvez renommer le fichier si nécessaire
    
    # Chemin complet vers le dossier "videos"
    dossier_videos = "/home/subku-88/Git-Project/DLink/videos"  # Mettez le chemin complet de votre dossier "videos"
    
    # Vérifier si le dossier existe, sinon le créer
    if not os.path.exists(dossier_videos):
        os.makedirs(dossier_videos)
    
    # Écrire le contenu binaire (la vidéo) dans un fichier local dans le dossier "videos"
    chemin_fichier = os.path.join(dossier_videos, nom_fichier)
    with open(chemin_fichier, 'wb') as f:
        f.write(response.content)
    
    print("Téléchargement terminé. La vidéo a été enregistrée sous", chemin_fichier)
else:
    print("Échec du téléchargement. Statut de la requête :", response.status_code)
