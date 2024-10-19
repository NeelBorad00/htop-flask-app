from flask import Flask, redirect, url_for
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('show_processes'))

@app.route('/htop')
def show_processes():
    full_name = "Neel Borad" 
    current_user = os.environ.get('USER') or os.environ.get('USERNAME')  # Obtaining the username from os
    local_timezone = pytz.timezone('Asia/Kolkata')
    current_server_time = datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Execute ps command to list processes
    processes_output = subprocess.getoutput('ps aux')

    # Spliting the output for better formatting
    process_lines = processes_output.splitlines()
    
    # Creating an HTML response
    html_response = f"""
    <html>
        <head>
            <title>System Information</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                
                h1, h2, h3 {{
                    color: #0056b3;
                }}


                .container {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}

                pre {{
                    background-color: #f8f8f8;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}

                .header {{
                    border-bottom: 2px solid #0056b3;
                    padding-bottom: 10px;
                    margin-bottom: 20px;
                }}

            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Name: {full_name}</h1>
                    <h2>Username: {current_user}</h2>
                    <h3>Server Time (IST): {current_server_time}</h3>
                </div>
                <h3>TOP output:</h3>
                <pre>{processes_output}</pre>
            </div>
        </body>
    </html>
    """
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
