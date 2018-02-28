
server_str = """
server {
	listen 80;
    server_name localhost;


     location / {
            proxy_pass http://app;
        }
}
"""

def read_docker_data(fpath):
    docker_list = []
    with open(fpath, 'r') as docker_data:
        for line in docker_data:
            if 'app_new' in line:
                docker_list.append(line[:12])
    return docker_list

def gen_conf(docker_ids):
    conf = ['upstream app {']
    server_line = "server {}:8000;"
    for id in docker_ids:
        conf.append(server_line.format(id))
    conf.append('}')
    conf.append(server_str)
    print(conf)
    return '\n'.join(conf)


def write_conf(config,path):
    with open(path, 'w') as new_conf:
        for line in config.split('\n'):
            new_conf.write(line + '\n')
    return 0

if __name__ == "__main__":
    docker_ids = read_docker_data('test.txt')
    conf = gen_conf(docker_ids)
    write_conf(conf, 'conf/nginx.conf')

