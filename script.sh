
#Write a Bash script that prompts the user to enter their age, and then checks if the age is greater than or equal to 18. If it is, print "You are an adult", otherwise print "You are a minor".
#!/bin/bash
#!/bin/bash

echo "Enter your age:"
read age

if [ "$age" -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are a minor"
fi
