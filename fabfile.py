from fabric.api import run, env, cd


# load config
env.use_ssh_config = True


def deploy(code_dir):
    with cd(code_dir):
        # run("git pull")
        run("git pull")
