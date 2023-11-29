from flask import Flask, request, jsonify
from moviepy.editor import CompositeVideoClip, ImageClip, TextClip

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Video Bot!'

@app.route('/generate_video', methods=['POST'])
def generate_video():
    data = request.get_json()
    content_text = data.get('text')  # Texte à afficher dans la vidéo
    image_path = 'path/to/image.jpg'  # Chemin vers l'image à utiliser
    
    # Charger l'image
    img = ImageClip(image_path)
    
    # Créer un clip texte avec le contenu reçu
    txt_clip = TextClip(content_text, fontsize=50, color='white', size=img.size)
    txt_clip = txt_clip.set_pos(('center', 'bottom')).set_duration(5)  # Position et durée du texte
    
    # Créer un clip vidéo composite avec l'image et le texte
    final_clip = CompositeVideoClip([img, txt_clip.set_start(0)])
    
    # Enregistrer la vidéo générée
    generated_video_path = 'path/to/generated/video.mp4'
    final_clip.write_videofile(generated_video_path, fps=24)
    
    return jsonify({'message': 'Vidéo générée avec succès', 'video_path': generated_video_path})

if __name__ == '__main__':
    app.run(debug=True)
