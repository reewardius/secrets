import os
import subprocess
import httpx

# Replace with the appropriate paths
output_folder = '/path/to/output/folder'
subfinder_output = '/path/to/subfinder/output.txt'

# Run subfinder and save the output to a file
subfinder_cmd = 'subfinder -d example.com -silent'
subfinder_output_file = open(subfinder_output, 'w')
subprocess.run(subfinder_cmd, stdout=subfinder_output_file, shell=True)
subfinder_output_file.close()

# Run waybackurls on subfinder output
waybackurls_cmd = f"cat {subfinder_output} | waybackurls"
waybackurls_output = subprocess.check_output(waybackurls_cmd, shell=True)

# Check each URL for a valid response and download any valid JS files
for url in waybackurls_output.decode().split('\n'):
    if url.endswith('.js'):
        try:
            response = httpx.head(url)
            if response.status_code == 200:
                filename = os.path.basename(url)
                output_file = os.path.join(output_folder, filename)
                wget_cmd = f"wget {url} -O {output_file}"
                subprocess.run(wget_cmd, shell=True)
        except:
            pass

# Run grep on the output folder
grep_cmd = f"grep -rE 's3:\/\|/\.s3\.amazonaws\.com' {output_folder}/*.js"
subprocess.run(grep_cmd, shell=True)
