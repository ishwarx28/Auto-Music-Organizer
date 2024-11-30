import os
import re
import json
from collections import Counter
import heapq
import shutil
import argparse

def split_into_words(text, words_to_remove):
    text = re.sub(r'([a-z])[\.]', r'\1', text.lower())
    text = re.sub(r'([a-z])[-]', r'\1 ', text.lower())
    text = re.sub(r'[&+]+', ' ', text)
    words = re.findall(r'[\w _]+', text)
    words = [word.strip() for word in words if word.strip() not in words_to_remove]
    return words

def organize_music(root, filetypes, words_to_remove, top_k, preferred_spaces, min_count):
    names = [
        file.replace(re.search(r'\.[a-z0-9]+$', file).group(), '')
        for _, _, files in os.walk(root) for file in files
        if re.search(r'\.[a-z0-9]+$', file) and re.search(r'\.[a-z0-9]+$', file).group() in filetypes
    ]

    count_vocab = Counter(word for name in names for word in split_into_words(name, words_to_remove))

    clusters_counts = {}
    for name in names:
        words = split_into_words(name, words_to_remove)
        top_words = heapq.nlargest(top_k, {word: count_vocab[word] for word in words}.items(), key=lambda item: item[1])
        for word, _ in top_words:
            clusters_counts[word] = clusters_counts.get(word, 0) + 1

    clusters = {}
    for name in names:
        words = split_into_words(name, words_to_remove)
        top_word = max(
            (word for word in words if word in clusters_counts),
            key=lambda w: clusters_counts[w] + (1 if w.count(' ') <= preferred_spaces else 0),
            default=None
        )
        if top_word:
            clusters.setdefault(' '.join([word.capitalize() for word in top_word.split()]), []).append(name)

    for cluster, songs in list(clusters.items()):
        if cluster != 'Unknown' and len(songs) <= min_count:
            clusters['Unknown'] = clusters.get('Unknown', []) + songs
            del clusters[cluster]

    with open('clusters.json', 'w', encoding='utf-8') as writer:
        json.dump(clusters, writer, indent=4)

    organised_root = os.path.join(root, "Organised")
    if not os.path.exists(organised_root):
        os.makedirs(organised_root)

    for cluster_name, song_list in clusters.items():
        cluster_path = os.path.join(organised_root, cluster_name)
        if not os.path.exists(cluster_path):
            os.makedirs(cluster_path)

        for song_name in song_list:
            for dirpath, _, filenames in os.walk(root):
                for filename in filenames:
                    if song_name in filename:
                        source_file = os.path.join(dirpath, filename)
                        destination_file = os.path.join(cluster_path, filename)
                        if not os.path.exists(destination_file):
                            shutil.copy(source_file, destination_file)
                        break
    print(f"Songs have been organized into clusters in the '{organised_root}' folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize music files into clusters.")
    parser.add_argument("root", help="Root directory containing the music files")
    parser.add_argument("--filetypes", nargs='+', default=['.m4a', '.mp3'], help="List of file types to organize")
    parser.add_argument("--words_to_remove", nargs='+', default=['from', 'in', 'feat', 'movie', ''], help="List of words to ignore in clustering")
    parser.add_argument("--top_k", type=int, default=3, help="Number of top words to consider for clustering")
    parser.add_argument("--preferred_spaces", type=int, default=1, help="Maximum spaces allowed in cluster names")
    parser.add_argument("--min_count", type=int, default=2, help="Minimum number of songs for a cluster to remain")
    args = parser.parse_args()

    organize_music(args.root, args.filetypes, args.words_to_remove, args.top_k, args.preferred_spaces, args.min_count)
