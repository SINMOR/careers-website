from flask import Flask , render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title' : 'Data analyst',
        'location' : 'Remote',
        'salary' : 'Ksh100,000'
    },
    {
        'id':2,
        'title' : 'Frontend Engineer',
        'location' : 'Nairobi,Kenya',
        'salary' : 'Ksh120,000'
    },
    {
        'id':3,
        'title' : 'Backend Engineer',
        'location' : 'Nyeri,Kenya',
        'salary' : 'Ksh150,000'
    },
    {
        'id':4,
        'title' : 'Data analyst',
        'location' : 'Nakuru,Kenya',
        # 'salary' : 'Ksh80,000'
    },
    {
        'id':5,
        'title' : 'ML Engineer',
        'location' : 'Remote',
        'salary' : 'Ksh180,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('index.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run (host='0.0.0.0', debug=True)
    
