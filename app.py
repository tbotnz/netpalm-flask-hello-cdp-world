from flask import Flask, render_template, redirect, url_for, request, json
import requests

app = Flask(__name__)

NETPALM_SERVER_IP = "10.0.2.15"
NETPALM_SERVER_PORT = 9000
NETPALM_API_KEY = "2a84465a-cf38-46b2-9d86-b84Q7d57f288"

@app.route("/")
def hello_world_form():
    return render_template("hello-world-form.html")

@app.route("/result/<posted_data>")
def hello_world_result(posted_data):
    task_id = json.loads(posted_data)["data"]["task_id"]
    r = requests.get(f"http://{NETPALM_SERVER_IP}:{NETPALM_SERVER_PORT}/task/{task_id}",
                        headers={"Content-type": "application/json", "x-api-key": NETPALM_API_KEY}, timeout=10)    
    return render_template("result.html", posted_data=r.json())

#"username": request.form["username"],
@app.route("/execute_job", methods=["POST"])
def hello_world_execute():
    ips = request.form["ipaddr"]
    if "," in ips:
        ipres = ips.split(",")
    else:
        ipres = [ips]
    post_data = {
        "operation": "retrieve",
        "args": {
            "hosts": ipres
        }
    }
    r = requests.post(f"http://{NETPALM_SERVER_IP}:{NETPALM_SERVER_PORT}/service/cdp_service",
                    headers={"Content-type": "application/json", "x-api-key": NETPALM_API_KEY}, json=post_data, timeout=10)
    return redirect(url_for(".hello_world_result", posted_data=r.text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10001)