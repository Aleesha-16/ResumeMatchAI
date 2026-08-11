from flask import Flask, render_template, request

from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description")

    if not resume:
        return "Please upload a resume."

    if not job_description:
        return "Please enter a job description."

    resume_text = extract_text_from_pdf(resume)

    if not resume_text.strip():
        return "Could not extract text from the uploaded PDF."

    result = analyze_resume(
        resume_text,
        job_description
    )

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)