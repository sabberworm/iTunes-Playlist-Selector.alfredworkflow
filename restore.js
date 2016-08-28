#!/usr/bin/osascript -l JavaScript

var app = Application('iTunes');
app.includeStandardAdditions = true;

function run(theId) {
	theId = String(theId).trim();
	var playlist = app.playlists.whose({persistentID: theId})()[0];

	if(!playlist) {
		console.log(`Playlist not known: ${theId}`);
		return;
	}
	
	var contents = String(app.theClipboard()).trim();
	if(!contents) {
		console.log('Clipboard empty');
	}
	var ids = contents.split(/[\n\r]+/g);
	
	if(ids[0].indexOf(':') > -1) {
		// This should contain the playlist ID/name
		if(ids[0].split(':')[0] !== theId) {
			console.log('Playlist to be restored does not match selected playlist. Leave off playlist descriptor to force.');
		}
	}
	
	// Remove existing tracks
	app.delete(playlist.tracks);
	
	// Restore the tracks from the clipboard
	ids.forEach(function(id) {
		var track = app.tracks.whose({persistentID: id})()[0];
		if(!track) {
			return console.log(`track ${id} cannot be found and will not be restored`);
		}
		app.duplicate(track, {to: playlist});
	});
}