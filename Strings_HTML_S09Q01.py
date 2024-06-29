Webpage_Title = input("Enter the Webpage Title: ")
Webpage_Main_Header = input("Entert the webpage header: ")
Webpage_sub_Header1 = input("Entert the webpage sub-header name: ")
Webpage_Para1 = input("Enter the first paragraph: ")
Webpage_Para2 = input("Enter the second paragraph: ")
HTML_Content = f"""
<Doc Type: HTML>
<Documnet Language: English>
<head>
    <title>{Webpage_Title}</title>
<head>
<body>
    <main header> {Webpage_Main_Header} <main header>
    <h1> {Webpage_sub_Header1} </h1>
    <p1> {Webpage_Para1} </p1>
    <p2> {Webpage_Para2} </p2>
<body>
"""

print(HTML_Content)
