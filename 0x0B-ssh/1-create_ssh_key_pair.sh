#!/usr/bin/env bash
# a Bash script that creates an RSA key pair.
ssh-keygen -t rsa  -b 4096 -f ~/.ssh/school -N "betty"