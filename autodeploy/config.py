import json


def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


with open('config.json', 'r', encoding='utf-8') as config:
    conf = json.load(config)
    print("开始配置dc-static.cfg")
    alter(conf['install_dir'] + "etc/dc/" + "dc-static.cfg", "DataCenter.Recognizer.Threads = 4",
          "DataCenter.Recognizer.Threads = %s" % conf['threads'])
    alter(conf['install_dir'] + "etc/dc/" + "dc-static.cfg", "DataCenter.Recognizer.Name = FileMatched",
          "DataCenter.Recognizer.Name = Optimus")
    alter(conf['install_dir'] + "etc/dc/" + "dc-static.cfg", "DataCenter.Optimus.BindNetwork = 127.0.0.1",
          "DataCenter.Optimus.BindNetwork = %s" % conf["ip"])
    alter(conf['install_dir'] + "etc/dc/" + "dc-static.cfg", "DataCenter.Optimus.Multicast.IP = 230.0.0.1",
          "DataCenter.Optimus.Multicast.IP = 230.0.0.230")
    alter(conf['install_dir'] + "etc/dc/" + "dc-static.cfg", "DataCenter.TextAuthorizeServer.Url = http://172.16.21.72:9999/license/",
          "DataCenter.TextAuthorizeServer.Url = http://%s/license/" % conf["ip"])
    print("开始配置offsr-prime.cfg")
    alter(conf['install_dir'] + "etc/optimus-offsr/" + "offsr-prime.cfg", "Multicast.IP = 230.0.0.1",
          "Multicast.IP = 230.0.0.230")
    alter(conf['install_dir'] + "etc/optimus-offsr/" + "offsr-prime.cfg", "Service.MaxConcurrent = MPC",
          "Service.MaxConcurrent = %s" % conf['threads'])
    print("开始配置res-prime.cfg")
    alter(conf['install_dir'] + "etc/optimus-res/" + "res-prime.cfg", "Multicast.IP = 230.0.0.1",
          "Multicast.IP = 230.0.0.230")
    alter(conf['install_dir'] + "etc/optimus-res/" + "res-prime.cfg", "License.Service.Address = http://127.0.0.1:9999/license/",
          "License.Service.Address = http://%s/license/" % conf['ip'])
    print("开始配置psae")
    alter(conf['install_dir'] + "etc/psae/" + "dc-mapping.yml", "127.0.0.1",
          conf['ip'])
