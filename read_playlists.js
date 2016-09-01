#!/usr/bin/osascript -l JavaScript

const FLAGS = {
	library: 'l',
	folder: 'f',
	subscription: 'b',
	user: 'u',
	smart: 's',
	genius: 'g',
	shared: 'h',
	radio: 'r',
	cd: 'c'
};

var app = Application('iTunes');
app.includeStandardAdditions = true;

var playlists = {};

app.userPlaylists().forEach(function(playlist) {
	playlists[playlist.persistentID()] = {
		name: playlist.name(),
		user: true,
		smart: playlist.smart(),
		genius: playlist.genius(),
		shared: playlist.shared()
	};
});

app.libraryPlaylists().forEach(function(playlist) {
	playlists[playlist.persistentID()] = {
		name: playlist.name(),
		library: true
	};
});

app.radioTunerPlaylists().forEach(function(playlist) {
	playlists[playlist.persistentID()] = {
		name: playlist.name(),
		radio: true
	};
});

app.subscriptionPlaylists().forEach(function(playlist) {
	playlists[playlist.persistentID()] = {
		name: playlist.name(),
		subscription: true
	};
});

app.audioCDPlaylists().forEach(function(playlist) {
	playlists[playlist.persistentID()] = {
		name: playlist.name(),
		cd: true
	};
});

app.playlists.whose({_match: [ObjectSpecifier().class, 'folderPlaylist']})().forEach(function(playlist) {
	playlists[playlist.persistentID()] = {
		name: playlist.name(),
		folder: true
	};
});

playlists = Object.keys(playlists).filter(function(id) {
	return !playlists[id].cd;
}).map(function(id) {
	var flags = '';
	for(var f in FLAGS) {
		if(playlists[id][f]) {
			flags += FLAGS[f].toUpperCase();
		} else {
			flags += FLAGS[f];
		}
	}
	return `${id}:${flags}:${playlists[id].name}`;
})

console.log(playlists.join('\n'));