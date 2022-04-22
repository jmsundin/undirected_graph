import subprocess
import os
import re
from bs4 import BeautifulSoup


NLPIA_Ch6_my_section = 'NLPIA_Ch6_my_section.adoc'
NLPIA_Ch6_my_section_html = 'NLPIA_Ch6_my_section.html'

class AsciiDocToHtml():
    
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    
    def run_ascii_doc3(self) -> None:
        subprocess.run(args=['asciidoc3', '-a', '-n', '-a', 'icons', self.file_name])
    

    def run_beautiful_soup(self):

        if os.path.exists() and os.path.getsize(NLPIA_Ch6_my_section_html) > 0:
            f = open(NLPIA_Ch6_my_section_html, 'r').read()
            bsoup = BeautifulSoup(f, 'html.parser')
            text = bsoup.get_text()


if __name__ == "__main__":

    AsciiDocToHtml()