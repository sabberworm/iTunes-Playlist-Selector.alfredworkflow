#!/usr/bin/osascript

tell application "iTunes"
	set pls to playlists
	set res to {} as list
	repeat with pl in pls
		copy ("" & pl's persistent ID & ":" & pl's name) to the end of res
	end repeat
	set AppleScript's text item delimiters to "
"
	return res as string
end tell