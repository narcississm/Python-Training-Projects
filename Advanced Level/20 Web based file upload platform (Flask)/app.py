import os
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Maksimum 16 MB dosya

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("Dosya kısmı bulunamadı.")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("Dosya seçilmedi.")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            flash(f"Dosya '{filename}' başarıyla yüklendi!")
            return redirect(url_for("upload_file"))
        else:
            flash("İzin verilmeyen dosya türü.")
            return redirect(request.url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
