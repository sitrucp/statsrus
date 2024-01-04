# National Statistics Agencies Home Page Screenshots and Color Palettes

This was a project done in 2016 to get screenshots of the home page of all of the world's national statistics agencies to identify the content. Specifically we were looking to identify use of visualizations and data. In addition we obtained a dominant color palettes based on each home page colors.

The repository contains the results of the analysis in the screenshots.csv file which has the following fields:

* id - screenshot
* filename - screenshot
* description - screenshot
* main - screenshot
* created - screenshot
* country_id - country
* thumbnail - screenshot
* long_thumb - screenshot
* color_palette - 3 most dominant colors on web page as RGB eg [(247, 241, 6), (238, 248, 235), (83, 111, 93)]
* height - screenshot
* screenshot - screenshot
* stat_count - count of data statistics on home page
* story_count - count of data stories on home page
* viz_count - count of data visualizations on home page
* palette_image - 3 most dominant colors displayed in a palette bar indicating percent pixels on page.
* screenshot_missing - screenshot
* total_stats - sum of stat_count, story_count, viz_count

Example screenshot and color palette:

Greece statistics home page screenshot

<img src="screenshots\greece.png" style="width: 50%; height: auto;" alt="Greece">

Color palette bar

<img src="palettes\greece.png" style="width: 50%; height: auto;" alt="Greece">
