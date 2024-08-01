<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Translation App: English to French and Hindi</h1>
<p>This project is a web application that simultaneously translates English text into French and Hindi using the MarianMT model from the Hugging Face Transformers library. The user interface is built with Streamlit, and the app includes a specific rule for translating only 10-letter words.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="installation">Installation</h2>
<p>To run this application, you must install Python on your machine. The recommended version is Python 3.8 or higher.</p>

<h3>Step 1: Clone the Repository</h3>
<p>First, clone this repository to your local machine using:</p>
<pre><code>git clone https://github.com/KritPrasad05/NULLCLASS_INTERNSHIP-TASK3-KritPrasad.git
  
cd translation-app-multi
</code></pre>

<h3>Step 2: Create a Virtual Environment</h3>
<p>Using a virtual environment to manage dependencies is a good practice. You can create a virtual environment using <code>venv</code>:</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
</code></pre>

<h3>Step 3: Install Dependencies</h3>
<p>Install the necessary libraries using <code>pip</code>:</p>
<pre><code>pip install transformers</code></pre>
<pre><code>pip install torch</code></pre>
<pre><code>pip install streamlit</code></pre>

<h3>Step 4: Run the Application</h3>
<p>Start the Streamlit application by running:</p>
<pre><code>streamlit run TASK4.py
</code></pre>

<h2 id="usage">Usage</h2>
<ol>
    <li>Open your web browser and go to <code>http://localhost:8501</code>.</li>
    <li>Enter a 10-letter English word in the input box.</li>
    <li>The application will display the translated text in both French and Hindi.</li>
    <li>If the word is not 10 letters long, the application will prompt you to enter a valid word.</li>
</ol>

<h2 id="credits">Credits</h2>
<p>This project was created as part of a task assigned by NullClass. Special thanks to the NullClass organization for the opportunity to work on this project.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
