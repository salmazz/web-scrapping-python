# Web Scrapping with python
Web scraping is a data extraction process used to extract data from different websites and store them in a desired file format like csv,excel etc. 
to perform web scraping there are few modules available in the market which can be used for web sraping. 

## Following are the modules used mainly for web scraping : 
* Requests
* BeautifulSoup
* CSV


## Details to be observed : 

### Step 0 : Setting up the Environment 
<ol>
  <li> In order to use the power of python to scrap websites, we can use existing libraries to get the job done.
  <li> We will install the following libraries using pip :

``` 
pip install requests
```

``` 
pip install beautifulsoup4
```

``` 
pip install python-csv
```

</ol>


### Step 1 : Fetching the HTML content
<ol>
  <li> In order to work with the HTML, we will have to get the HTML as a string.
  <li> We will leverage the power of python requests module to get this done!
  <li> The next step then will be to parse the HTML content and give it a tree like structure so that it can be traversed.
</ol>

### Step 2 : Parse the HTML
<ol> 
  <li> Once the HTML is fetched using the requests as an string, we need to parse it.
  <li> For parsing, we will use python's BeautifulSoup module which will create a tree like structure for our DOM.
</ol>

### Step 3 : HTML tree traversal 
<ol> 
  <li> Once the HTML is fetched and parsed, the next step is to manipulate the tree using BeautifulSoup's functions to get our job done.
  <li> This tutorial will teach you how to get started and traverse the tree.
</ol>

#### To Open the result in excel sheet with arabic words 

<ol>
<li>Open Excel on a blank workbook </li>
<li>Within the Data tab, click on From Text button (if not activated, make sure an empty cell is selected)</li>
<li>Browse and select the CSV file</li>
<li>In the Text Import Wizard, change the File_origin to "Unicode (UTF-8)"</li>
<li>Go next and from the Delimiters, select the delimiter used in your file e.g. comma</li>
<li>Finish and select where to import the data</li>
</ol>

The Arabic characters should show correctly.