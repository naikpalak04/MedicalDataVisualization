import subprocess


def publish_to_tableau():
    tableau_project = "YOUR_PROJECT"
    tableau_datasource = "../data/transformed_medical_data.csv"
    tableau_server = "YOUR_SERVER"
    tableau_token_name = "YOUR_TOKEN_NAME"
    tableau_token_value = "YOUR_TOKEN_VALUE"

    cmd = [
        "tabcmd",
        "login",
        "--server", tableau_server,
        "--token", tableau_token_name,
        "--token-value", tableau_token_value
    ]
    subprocess.run(cmd)

    cmd = [
        "tabcmd",
        "publish", tableau_datasource,
        "--project", tableau_project,
        "--name", "Transformed Medical Data",
        "--overwrite"
    ]
    subprocess.run(cmd)

    cmd = ["tabcmd", "logout"]
    subprocess.run(cmd)


if __name__ == "__main__":
    publish_to_tableau()
