import subprocess


def get_db_pass_from_keychain(name="academy_db_pass"):
    pipe = subprocess.Popen(["security", "find-generic-password", "-s", name, "-w"],
                            stdout=subprocess.PIPE, text=True)
    out, err = pipe.communicate()
    return None if err else out.strip("\n ")

