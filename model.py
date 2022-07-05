#!/usr/bin/env python
# coding: utf-8

# In[1]:


class thermal_generator:
    
    def __init__(self,power_out_min, power_out_max, time_up_min, time_down_min,must_run, 
                 ramp_up, ramp_down, cost, A_D, A_U ):
        self.time_up_min = time_up_min
        self.time_down_min = time_down_min
        self.must_run = must_run
        self.ramp_up = ramp_up
        self.ramp_down = ramp_down
        self.cost = cost
        self.A_D = A_D
        self.A_U = A_U
        self.power_level = []
        self.power_level.append(0)
        self.power_level.extend([x for x in range(int(power_out_min), int(power_out_max + 1))])
    
    def print_all_info(self):
        print("Minimum time up : {}".format(self.time_up_min))
        print("Minimum time down : {}".format(self.time_down_min))
        print("Must run time : {}".format(self.must_run))
        print("Ramp up : {}".format(self.ramp_up))
        print("Ramp down : {}".format(self.ramp_down))
        print("Costs : {} ".format(self.cost))
        print("Start up cost : {}".format(self.A_U))
        print("Start down cost : {}".format(self.A_D))
        print("Power levels : {}".format(self.power_level))


# In[2]:


gen111 = thermal_generator(5, 10,2,2,0,20.3,30.5,5,20,200)
gen111.print_all_info()


# In[3]:


class wind_generator:
    
    def __init__(self,power_output_max):
        self.power_level = []
        for level in power_output_max:
            self.power_level.append([x for x in range(0, level+1)])
        self.time_up_min = 0
        self.time_down_min = 0
        self.must_run = 0
        self.ramp_up = 0
        self.ramp_down = 0
        self.cost = 0
        self.A_D = 0
        self.A_U = 0
        
    def print_all_info(self):
        print("power maximum output : {}".format(self.power_level))


# In[4]:


win12 = wind_generator([1,5,5,8,7,5])
win12.print_all_info()


# In[5]:


class network:
    
    def __init__(self, time_period, demand, reserves, thermal_gen = [], renewable_gen = []):
        self.time_period = time_period
        self.demand = demand
        self.reserves = reserves
        self.thermal_gen = thermal_gen
        self.renewable_gen = renewable_gen
    
    def add_thermal_generator(self, thermal_generator):
        self.thermal_gen.append(thermal_generator)
    
    def add_renewable_generator(self, renew_generator):
        self.renewable_gen.append(renew_generator)
    
    def print_all_info(self):
        print("Time period : {}".format(self.time_period))
        print("Demand(Loads) over time : {}".format(self.demand))
        print("reserves over time : {}".format(self.reserves))
        print("Number of Thermal generators : {}".format(len(self.thermal_gen)))
        print("Number of renewable generators : {}".format(len(self.renewable_gen)))


# In[6]:


network_dummy = network(7, [0,0,0,0,0,0,0],[0,0,0,0,0,0,0])
network_dummy.add_thermal_generator(gen111)
network_dummy.add_renewable_generator(win12)
network_dummy.print_all_info()


# In[14]:


def create_thermal_generator(json_object):
    return thermal_generator(json_object['power_output_minimum'],json_object['power_output_maximum'],
                             json_object['time_up_minimum'], json_object['time_down_minimum'],
                            json_object['must_run'],json_object['ramp_up_limit'],json_object['ramp_down_limit'],
                            json_object['piecewise_production'][0]['cost'],
                            json_object['startup'][0]['cost'],
                            json_object['startup'][1]['cost'],)

def create_renewable_generator():
    pass

def create_network(json_object):
    net = network(json_object['time_periods'],json_object['demand'],json_object['reserves'])
    for x in json_object['thermal_generators']:
        gen = create_thermal_generator(json_object['thermal_generators'][x])
        net.add_thermal_generator(gen)
    return net


# In[15]:


import json
# JSON file
f = open ('data/example.json', "r")
# Reading from file
data = json.loads(f.read())
net = create_network(data)


# In[16]:


net.print_all_info()


# In[ ]:




