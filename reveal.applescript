#!/usr/bin/osascript

on run (theId)
	tell application "Music"
		set myPlaylist to the first item of (every playlist whose persistent ID is theId)
		reveal myPlaylist
		activate
	end tell
end run
