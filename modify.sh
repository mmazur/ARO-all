#!/bin/bash

# Claude gets *very* confused when dealing with nested git repos
# Using this repo like this avoids this issue
if [ -d .git ]; then
  mv .git .git-hidden
  echo "git hidden"
elif [ -d .git-hidden ]; then
  mv .git-hidden .git
  echo "git available"
fi
