import subprocess
import os
import sys # to read in stdin

from bs4 import BeautifulSoup


class AsciiDocToHtml():
    
    def __init__(self, adoc_file_name: str, html_file_name: str) -> None:
        self.adoc_file_name = adoc_file_name
        self.html_file_name = html_file_name

    
    def run_ascii_doc3(self) -> None:
        subprocess.run(args=['asciidoc3', '-a', '-n', '-a', 'icons', self.adoc_file_name])


    def run_beautiful_soup(self) -> str:
        if os.path.exists(self.html_file_name) and os.path.getsize(self.html_file_name) > 0:
            f = open(self.html_file_name, 'r').read()
            bsoup = BeautifulSoup(f, 'html.parser')
            return bsoup.get_text()


if __name__ == "__main__":
    for line in sys.stdin():
        if 'q' == line.rstrip():
            break
        print(f'Input: {line}')
        ascii_doc_file = line.rstrip()

    if 'adoc' in ascii_doc_file:
        NLPIA_Ch6_my_section_html = ascii_doc_file.replace('adoc', 'html')
        AsciiDocToHtml(ascii_doc_file, NLPIA_Ch6_my_section_html)
        AsciiDocToHtml.run_ascii_doc3()
        AsciiDocToHtml.run_beautiful_soup()