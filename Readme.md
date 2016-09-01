# iTunes Playlist Selector Alfred 3 Workflow

Lets you filter your iTunes playlist and show them afterwards. Call its script filter using the “itpl” keyword.

To initialize, choose the “Reload Playlists” options to cache a list of playlists in a text file. After that, you’re all set.

## Backing up playlists

There is a back up script (called with “plbck”). It will let you select a playlist and then copy a list of song IDs to the clipboard from where you can paste it to your backup file.

## Restoring playlists

Copy a list of song IDs you have previously backed up to the clipboard and then use the restore script (“plres”). It will clear the selected playlist and fill it with the songs from the clipboard. Afterwards, the clipboard will contain the previous contents of the playlist (as well as messages for any potential errors that occurred).

## Acknowledgements

Icons taken from the [Batch icon set](http://adamwhitcroft.com/batch/) by Adam Whitcroft