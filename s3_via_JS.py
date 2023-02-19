import os
import subprocess
import httpx

output_folder = '/path/to/output/folder'
subfinder_output = '/path/to/subfinder/output.txt'

subfinder_cmd = 'subfinder -d example.com -silent'
subfinder_output_file = open(subfinder_output, 'w')
subprocess.run(subfinder_cmd, stdout=subfinder_output_file, shell=True)
subfinder_output_file.close()

waybackurls_cmd = f"cat {subfinder_output} | waybackurls"
waybackurls_output = subprocess.check_output(waybackurls_cmd, shell=True)

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

grep_cmd = f"grep -rE 's3:\/\|/\.s3\.amazonaws\.com' {output_folder}/*.js"
subprocess.run(grep_cmd, shell=True)
