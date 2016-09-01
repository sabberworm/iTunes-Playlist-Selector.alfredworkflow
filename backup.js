#!/usr/bin/osascript -l JavaScript

var app = Application('iTunes');
app.includeStandardAdditions = true;

function run(theId) {
	theId = String(theId).trim();
	var playlist = app.playlists.whose({persistentID: theId})()[0];

	if(!playlist) {
		return;
	}
	
	return `${playlist.persistentID()}: ${playlist.name()}\n` + playlist.tracks().map(function(track) {
		return track.persistentID();
	}).join('\n');	
}