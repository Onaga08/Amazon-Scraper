# Amazon-Scraper

## Usage
<p>Amazon is an American Multinational Corporation focusing on a variety of industries, 
like e-commerce, cloud computing, online advertising, and artificial intelligence. We, in this project
focus on the e-commerce platform hosted by amazon, on the web-app <a href="amazon.in">Amazon.in </a> The functionalities of each runnable file is given in the following sections of this file.</p>

## Pre-Requisites
<ul>
<li>Python version 2.7 and above </li>
<li>Selenium module installed </li>
<li>CSV module installed </li>
<li>Time module installed </li>
</ul>

<h3>To install the above mentioned libraries using pip, input the following commands in the terminal </h3>

```bash
pip install selenium
```
<h4><b>Note</b>: CSV and Time module comes pre-installed with Python's standard utility module </h4>

## File Details

<ul>
<li><h3>Main.py</h3>
     <ul>
         <li>Pre-defined: URL: <a href="https://www.amazon.in/s?k=bags"> Amazon Bags Search </a></li>
         <li>Function: Traverses to the above URL. Extracts the following data 
            <ul>
            <li>URL</li>
            <li>Name</li>
            <li>Price</li>
            <li>Ratings</li>
            <li>Number of Ratings</li>
            </ul>
            </li>
         <li>Gathers the above mentioned information for upto 10 pages (Hard coded, can be changed)</li>
         <li>Output: CSV files for each page. </li>
         <li>Features : 
          <ul>
           <li>Custom user agent to mimic real browser </li>
           <li>Custom scrolling, to overcome dynamic page load </li>
           <li>Explicit wait to reduce bot suspicion </li>
           <li>Explicit wait before writing to csv file </li>
          </ul>
         </li>
        </ul>
</li>
<li><h3>Part2.py</h3>: Under construction!!</li>

### Note: Please find the privacy policy in <a href="Privacy.MD"> Privacy.MD </a>

<h4>Any tips for improvements or comments are welcomed</h4>