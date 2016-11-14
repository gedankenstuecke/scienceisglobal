# scienceisglobal

Based on [gedankenstuecke/scienceisglobal](https://github.com/gedankenstuecke/scienceisglobal)

See [this blog post](http://ruleofthirds.de/scienceisglobal/) by Bastian Greshake for some more information.

Source: Around 9000 Tweets, scraped for the hashtag *#ScienceIsGlobal*, to visualize the country connections represented by the co-occurrence of emoji flags. The data collection is [ongoing in this public Google Doc Spreadsheet](https://docs.google.com/spreadsheets/d/1NRxvV0JP_eF98WUfbkpj1iMBlFEe25JGKGhblM6U3KQ/edit#gid=56646471).

I reorganized the columns in [chord.csv](https://github.com/bmkramer/scienceisglobal/blob/geolayout/chords.csv) to be used as input for BibExcel to regenerate a network file for use in Gephi (but there's surely a quicker way to do that). 

I added [geocoordinates](https://developers.google.com/public-data/docs/canonical/countries_csv) (lat/long) to the data, used the [Geo Layout plugin](https://marketplace.gephi.org/plugin/geolayout/) in Gephi, and created three networks, with all edges, edges > 100 or edges > 200, respectively. 


![](https://github.com/bmkramer/scienceisglobal/blob/geolayout/geolayout_edge1.png)

![](https://github.com/bmkramer/scienceisglobal/blob/geolayout/geolayout_edge100.png)

![](https://github.com/bmkramer/scienceisglobal/blob/geolayout/geolayout_edge200.png)
