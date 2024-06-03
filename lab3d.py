#!/usr/bin/env python3
'Lab 3'
#Author ID: kirandeep-kaur51@myseneca.ca

import subprocess

def free_space():
    #Launch the linux command: df -h | grep '/$' | awk {print $4}' as Process
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Testing the function
if __name__ == "__main__":
    print(free_space())
   
   

