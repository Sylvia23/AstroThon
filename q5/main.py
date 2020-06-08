import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class ScraperXRT:
    """
    Description
    -----------
    A class to scrap XRT files from the telescope archive.

    Examples
    --------
    scraper = ScraperXRT("thin_Be", datetime(2017, 7, 24, 6, 17, 22),
            datetime(2018, 3, 20, 7, 41, 5))
    files = scraper.get()
    for file in files:
        scraper.view(file)
        plt.show()
    """

    link = "http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/"

    def __init__(self, typeof_file, startime, endtime):
        """
    Description
    -----------
    Gives a scraper class that helps getting and viewing fits image from "http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/" with given file type and having modification time between start and end time

    Parameters
	----------
	typeof_file: A `string`
    startime: A `~datetime.datetime` instance
    endtime: A `~datetime.datetime` instance
	    """
        self.type = typeof_file
        self.startTime = startime
        self.endTime = endtime

        # getting the links on the page with given type

        content = requests.get(self.link)
        content = content.content.decode()
        soup = BeautifulSoup(content, "html.parser")
        tags = soup.find_all("a")
        self.links = [tag["href"] for tag in tags]
        # removing the first 4 links cause they are not useful
        self.links = self.links[5:]
        self.links = [
            link for link in self.links if link.startswith("XRT_" + self.type)
        ]

    def query(self):
        """
	Returns
	-------
	A `list` of strings of URLs.
	    """

        def get_datetime(link):
            """
            Description
            -----------
            Returns the datetime object of link from link
            """
            _date = link.split(".")[0]
            date = _date.split("_")[-2]
            time = _date.split("_")[-1]
            year = int(date[:4])
            month = int(date[4:6])
            day = int(date[6:])
            hour = int(time[:2])
            minutes = int(time[2:4])
            seconds = int(time[4:])
            return datetime(year, month, day, hour, minutes, seconds)

        links = []
        for link in self.links:
            time = get_datetime(link)
            # check if time of this file is between the given constraints.
            if time <= self.endTime and time >= self.startTime:
                links.append(self.link + link)
        return links

    def get(self):
        """
    Description
    -----------
    Downloads the queried results and returns a python list containing the paths of downloaded files.

	Returns
	-------
	A `list` of strings for files.
	    """
        if not os.path.exists("Downloads"):
            os.mkdir("Downloads")
        queries = self.query()
        paths = []

        for link in queries:
            name = link.split("/")[-1]
            cwd = os.getcwd()
            path = os.path.join(cwd, "Downloads", name)
            content = requests.get(link).content
            fhand = open(path, "wb")
            fhand.write(content)
            fhand.close()
            paths.append(path)

        return paths

    def view(self, filepath):
        """
    Description
    -----------
    Shows the fit file present at the location:filepath given

    Parameters
	----------
    filepath: A `string` representing absolute path of file in system.

	Returns
	-------
	An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
	    """
        with open(filepath, "rb") as fhand:
            # converting fits file to numpy array
            image = fits.getdata(fhand)
            return plt.imshow(image, cmap="gray")
