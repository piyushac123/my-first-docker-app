from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://images.pexels.com/photos/1661179/pexels-photo-1661179.jpeg",
    "https://images.pexels.com/photos/17811/pexels-photo.jpg",
    "https://images.pexels.com/photos/567540/pexels-photo-567540.jpeg",
    "https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg",
    "https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg",
    "https://images.pexels.com/photos/320014/pexels-photo-320014.jpeg",
    "https://images.pexels.com/photos/1059823/pexels-photo-1059823.jpeg",
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
