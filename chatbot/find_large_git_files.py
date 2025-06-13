import subprocess

def get_large_git_files(threshold_mb=100):
    threshold_bytes = threshold_mb * 1024 * 1024
    result = subprocess.run(
        ['git', 'rev-list', '--objects', '--all'],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in result.stdout.splitlines():
        try:
            sha, path = line.strip().split(' ', 1)
            size_result = subprocess.run(
                ['git', 'cat-file', '-s', sha],
                stdout=subprocess.PIPE,
                text=True
            )
            size = int(size_result.stdout.strip())
            if size > threshold_bytes:
                print(f"{size // (1024 * 1024)} MB - {path}")
        except:
            continue

get_large_git_files()
