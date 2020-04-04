import subprocess

def player_count(input):
    index = input.find("players")
    s = input[index:-3]
    max_index = s.find("80")
    count = int(s[9:max_index-1])

    return count

def player_list(input):
    index = input.find("[")

    if index == -1:
        return None

    lst_string = input[index+1:-4]
    lst = lst_string.split(", ")
    lst = [s.split(" ")[0][2:] for s in lst]

    return lst

output = str(subprocess.check_output("mcstatus Vextossup.join-mc.net status",
             shell=True))

print(output)

print(player_count(output))

print(player_list(output))
