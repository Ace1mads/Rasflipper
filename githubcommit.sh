#!/bin/bash

#cd linuxopg
sudo git add *
sudo git config --global user.email "andersen.mads0@gmail.com"
sudo git config --global user.name "Ace1mads"
echo Navn til commiten?
read commit
sudo git commit -m $commit
sudo git push
