#!/bin/bash

q={query}

if "$q" == "reload"; then
	./read_playlists.applescript > playlists.txt
else
	./reveal.applescript "$q"
fi
