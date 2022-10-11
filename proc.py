import subprocess

def load_info(message):
    command = "haqqd q staking validators -o json --limit=1000 | jq '.validators[] | select(.operator_address==\"" + message +"\")'"
    process = subprocess.run([command], capture_output=True, shell=True, text="True")
    return(process.stdout)

