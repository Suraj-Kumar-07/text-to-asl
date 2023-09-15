from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import cv2
import imageio
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/videos/<filename>')
def serve_video(filename):
    return send_from_directory('videos', filename)

@app.route('/send_message', methods=['POST'])
def sendmessage():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'error': 'Empty message'})

    # Check if the user's message exists in the message_to_video mapping
    image_paths = []
    # Iterate over each character in the sentence
    for char in user_message.upper():
        if char in character_to_image:
            image_path = character_to_image[char]
            image_paths.append(image_path)
        else:
            print(f"No image found for character: {char}")

    video_url = 'videos/output_video.mp4'
    fps = 2  # Frames per second

    writer = imageio.get_writer(video_url, fps=fps)

    for image_path in image_paths:
        image = imageio.imread(image_path)
        writer.append_data(image)

    writer.close()

    if video_url:
        response_data = {'videoUrl': video_url}
    else:
        response_data = {'error': 'No video found for the message'}

    return jsonify(response_data)




# Define a dictionary mapping characters to image paths
character_to_image = {
    'A': 'asl_alphabet_test/A_test.jpg',
    'B': 'asl_alphabet_test/B_test.jpg',
    'C': 'asl_alphabet_test/C_test.jpg',
    'D': 'asl_alphabet_test/D_test.jpg',
    'E': 'asl_alphabet_test/E_test.jpg',
    'F': 'asl_alphabet_test/F_test.jpg',
    'G': 'asl_alphabet_test/G_test.jpg',
    'H': 'asl_alphabet_test/H_test.jpg',
    'I': 'asl_alphabet_test/I_test.jpg',
    'J': 'asl_alphabet_test/J_test.jpg',
    'K': 'asl_alphabet_test/K_test.jpg',
    'L': 'asl_alphabet_test/L_test.jpg',
    'M': 'asl_alphabet_test/M_test.jpg',
    'N': 'asl_alphabet_test/N_test.jpg',
    'O': 'asl_alphabet_test/O_test.jpg',
    'P': 'asl_alphabet_test/P_test.jpg',
    'Q': 'asl_alphabet_test/Q_test.jpg',
    'R': 'asl_alphabet_test/R_test.jpg',
    'S': 'asl_alphabet_test/S_test.jpg',
    'T': 'asl_alphabet_test/T_test.jpg',
    'U': 'asl_alphabet_test/U_test.jpg',
    'V': 'asl_alphabet_test/V_test.jpg',
    'W': 'asl_alphabet_test/W_test.jpg',
    'X': 'asl_alphabet_test/X_test.jpg',
    'Y': 'asl_alphabet_test/Y_test.jpg',
    'Z': 'asl_alphabet_test/Z_test.jpg',
    ' ': 'asl_alphabet_test/space_test.jpg'
}


if __name__ == '__main__':
    app.run(debug=True)