# Auto Music Organizer 🎵  

**Auto Music Organizer** is a Python tool that automates the process of organizing your music collection. Designed to be simple, efficient, and highly customizable, it categorizes songs into meaningful clusters based on file names, making it easier to manage and explore your library.  

### Features  

- **Multi-format Support**: Works with common audio file types like `.mp3` and `.m4a`.  
- **Smart Clustering**: Identifies and groups files based on recurring keywords in song titles.  
- **Customizable Parameters**: Adjust settings like the number of keywords to consider, file types, and minimum cluster size to fit your needs.  
- **Automatic Folder Organization**: Creates clean, categorized subfolders and organizes your music files into them.  
- **Portable and Flexible**: No hard-coded paths—easily specify directories and preferences via arguments.  

### How It Works  

1. **Analyze**: The script scans the specified folder for supported audio files.  
2. **Cluster**: Using common patterns in file names, it identifies relevant clusters for organization.  
3. **Organize**: Files are moved into appropriately named folders for a clean, logical structure.  

### Usage  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/auto-music-organizer.git  
   cd auto-music-organizer  
   ```  

2. Run the script with your preferred settings:  
   ```bash
   python auto_music_organizer.py "path/to/your/music/folder" --filetypes .mp3 .m4a --top_k 3  
   ```  

3. Your organized music library will be available in a new "Organised" folder.  

### Why This Tool?  

Managing a large music library can be overwhelming. **Auto Music Organizer** simplifies this task by automating the tedious process of sorting and organizing music files. Whether you’re a music enthusiast or just want a clutter-free library, this tool saves time and effort while delivering a structured collection.
