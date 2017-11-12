import paramiko
import os
import sys
from multiprocessing import Pool, Manager, Value

class Distributor():
    eval_generation = Manager().list()
    counter = Value('i', 0)

    def __init__(self, host_number):
        self.manager = Manager()
        self.host_number = host_number
        self.available_hosts = []
        self.find_hosts()

    def evaluate_remotely(hostname, ssh_password, job_id, chromosome):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, username = "mn55", password = ssh_password, 
                timeout = 3)
        
            print ("Connected to ", hostname)

            with Distributor.counter.get_lock():
                Distributor.counter.value += 1  

            string_bytes = ["".join(map(str, chromosome)) for i in range(0, len(chromosome), 8)]
            int_bytes = []
         
            for string_byte in string_bytes:
                int_bytes.append(int(string_byte, 2))
            
            binary_result = bytearray(int_bytes) 

            with open("tmpSched/" + str(job_id), "w") as file:
                file.write(binary_result)    

            print ()    

            stdin, stdout, stderr = client.exec_command('cd /cs/home/mn55/Documents/CS4202/P2/CS4202_gensched/gem5/'
                '; /usr/local/python/bin/python3 sim_task.py ' 
                + str(job_id))

            stdin.channel.shutdown_write()
            stdout.channel.recv_exit_status()
            result = stdout.readlines()[0]
            print ("Evaluated:", hostname, result)
            fitness = 1 / int(result)
            Distributor.eval_generation.append((chromosome, fitness))   
        except:
            Distributor.eval_generation.append((chromosome, 0))  
            print (hostname, ": remote evaluation failed!")
            print (sys.exc_info()[0])

    def find_hosts(self):
        # Find available hosts
        # hosts = ['pc5-0' + str(x) + '-l.cs.st-andrews.ac.uk' for x in range(20, 50) if x != 26 and x != 24 and x!= 32]
        hosts = ['pc3-0' + str(x) + '-l.cs.st-andrews.ac.uk' for x in range(0, 50)]

        for host in hosts:
            response = os.system("timeout 0.2 ping -c 1 -i 0.2 " + host)

            if response == 0:
                self.available_hosts.append(host)

        print ("\nFound ", len(self.available_hosts), " machines.")   

        self.available_hosts = self.available_hosts[:self.host_number]      

    def calculate_fitness(self, population): 
        # Read ssh password 
        with open("pass", "r") as file:
            ssh_password = file.readline()

        # Spawn worker processes on different hosts and perform the simulations
        worker_pool = Pool(self.host_number)
        worker_pool.starmap(Distributor.evaluate_remotely, zip(self.available_hosts,
            [ssh_password for i in range(self.host_number)],
            range(self.host_number), population))
        worker_pool.close()
        worker_pool.join()

        return sorted(self.eval_generation, key = lambda x: x[1])