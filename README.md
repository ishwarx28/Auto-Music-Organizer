# Auto Music Organizer 🎵  

**Auto Music Organizer** is a Python tool that automates the process of organizing your music collection by categorizing songs into meaningful clusters based on the file names. It allows you to easily manage and explore your music library.

### Features  

- **Multi-format Support**: Organizes `.mp3`, `.m4a`, and other supported audio file types.
- **Smart Clustering**: Groups songs based on recurring keywords in their file names.
- **Customizable Parameters**: Customize the clustering behavior by adjusting settings like the number of top keywords, file types, minimum cluster size, and preferred spaces for cluster names.
- **Automatic Folder Organization**: Automatically creates and organizes your music files into categorized subfolders.
- **Dry Run Mode**: Supports a dry run mode to preview the organization process without making any changes.
- **Portable and Flexible**: Easily specify directories and preferences via command-line arguments.

### How It Works  

1. **Analyze**: The script scans the specified folder for supported audio files.
2. **Cluster**: Using recurring words in file names, the script groups the files into clusters based on the most common words found in their names.
3. **Organize**: Music files are moved into appropriately named subfolders for easy management.

### Usage  

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/auto-music-organizer.git
   cd auto-music-organizer
   ```

2. **Run the script with your preferred settings**:
   ```bash
   python auto_music_organizer.py "path/to/your/music/folder" --filetypes .mp3 .m4a --top_k 3 --preferred_spaces 1 --min_count 2 --disable_dry_run
   ```
   - `--filetypes`: List of file extensions to organize (default: `.mp3`, `.m4a`).
   - `--top_k`: The number of top words to consider when clustering (default: 3).
   - `--preferred_spaces`: Maximum number of spaces allowed in cluster names (default: 1).
   - `--min_count`: Minimum number of songs required for a cluster to remain (default: 2).
   - `--disable_dry_run`: Disable dry run mode to actually copy files (default: True).

3. **Result**: The script will organize your music into a new folder called "Organised" within your music directory. A JSON file (`clusters.json`) will be generated containing the cluster information.

### Dry Run Mode  

By default, the script operates in **dry run mode**, meaning no files will be moved or copied. This allows you to review how the files would be organized before making any changes. To disable the dry run and actually move the files, use the `--disable_dry_run` flag.

### Example

To organize music files in your `Music` folder, grouping them based on the most frequent words in the file names, you can run:
```bash
python auto_music_organizer.py "path/to/your/music/folder" --filetypes .mp3 .m4a --top_k 3 --preferred_spaces 1 --min_count 2 --disable_dry_run
```

### Why This Tool?  

Managing a large music library can be overwhelming. **Auto Music Organizer** simplifies this task by automating the tedious process of sorting and organizing your music files based on file name patterns. Whether you're a music enthusiast or just want a cleaner library, this tool saves time and effort while delivering a well-organized collection.  