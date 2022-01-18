from nornir import InitNornir

nr = InitNornir(config_file="/home/hbb/NetDevOps/DevNet/nornir/config.yaml")

print(nr.inventory.hosts.items)
