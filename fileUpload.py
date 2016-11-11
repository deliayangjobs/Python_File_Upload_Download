from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename

app=Flask(__name__)

@app.route("/fileUpload")
def height():
    return render_template("fileUploadDownload.html")

@app.route('/success', methods=['POST'])
def success():
    global myFile
    myFile=request.files["file"]
    #content=myFile.read()


    myFile.save(secure_filename("AddedWhatEver"+myFile.filename))

    with open("AddedWhatEver"+myFile.filename,"a") as myNewFile:
        myNewFile.write("I want to add something here")

    #content=myNewFile.read()
    return render_template("fileUploadDownload.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("AddedWhatEver"+myFile.filename, attachment_filename="yourfile.py", as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
