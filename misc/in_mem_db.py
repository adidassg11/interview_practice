# inspiration: https://www.thumbtack.com/challenges/simple-database

#!/usr/bin/python

#NOTES: some quirks left... iron those out then finish the BEGIN stuff

from collections import defaultdict

db = {}
db_stage = {'zk':'zv'}
net = defaultdict(int) #num equal to lookup
net_stage = defaultdict(int) #num equal to lookup staging dict
data_commands = {'SET', 'GET', 'UNSET', 'NUMEQUALTO', 'END'}
txn_commands = {'BEGIN', 'ROLLBACK', 'COMMIT'}
debug_commands = {'SHOWALL'}
commands = data_commands.union(txn_commands).union(debug_commands)


def run():
    while(1):
        cmd = raw_input().strip().split()

        print cmd

        if not cmd:
            print 'Please enter a command'
            continue

        if cmd[0] not in commands:
            print 'BAD COMMAND, use \'END\' to exit'
            continue

        if cmd[0] == 'SHOWALL':
            print 'db: ' + str(db)
            print 'staging: ' + str(db_stage)
            print 'net: ' + str(net)
            print 'net_stage: ' + str(net_stage)

        if cmd[0] == 'END':
            print 'db: ' + str(db) ####DEBUG
            return

        # BUG, see below
        if cmd[0] == 'SET':
            old_count = None # for numequalto
            if cmd[1] in db_stage:
                old_count = db_stage[cmd[1]]
            elif cmd[1] in db:
                old_count = db[cmd[1]]

            db_stage[cmd[1]] = cmd[2]
            net_stage[cmd[2]] += 1
            if old_count:
                net_stage[old_count] -= 1

            continue

        if cmd[0] == 'GET':
            val = 'NULL'
            if cmd[1] in db_stage:
                val = db_stage[cmd[1]]
            elif cmd[1] in db:
                val = db[cmd[1]]
            print val
            continue

        #BUG: set then unset a var that already exists in db will result in -1 in net_stage
        if cmd[0] == 'UNSET':  #TODO: this is affected if we have more than 1 staging db
            if cmd[1] in db_stage:
                value = db_stage[cmd[1]]
                del(db_stage[cmd[1]])
                net_stage[value] -= 1
            continue

        if cmd[0] == 'NUMEQUALTO':
            print net_stage[cmd[1]] + net[cmd[1]] # Yay defaultdict!
            continue

        if cmd[0] == 'BEGIN': ##TODO: need more staging db's
            continue

        if cmd[0] == 'ROLLBACK':
            db_stage.clear()
            net_stage.clear()
            continue

        if cmd[0] == 'COMMIT':
            for item in db_stage.items():
                db[item[0]] = item[1]
            for item in net_stage.items():
                net[item[0]] += item[1]
            db_stage.clear()
            net_stage.clear()
            continue


if __name__ == "__main__":
    print 'starting db...'
    run()
