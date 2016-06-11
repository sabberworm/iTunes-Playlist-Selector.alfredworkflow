#!/usr/bin/osascript -l JavaScript

var app = Application('iTunes');
app.includeStandardAdditions = true;

function run(theId) {
	var playlist = app.playlists.whose({persistentID: 'F793BB62F62B91E4'})()[0];

	if(!playlist) {
		return;
	}
	
	return playlist.fileTracks().map(function(track) {
		return track.persistentID();
	}).join('\n');	
}