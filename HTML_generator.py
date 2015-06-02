def generate_HTML(content_title, content_description):
    html_text_1 = '''
  <h2>''' + content_title + '</h2>'
    html_text_2 = '''
    <div class="description">
        ''' + content_description
    html_text_3 = '''
    </div>'''
      
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    content_title = concept[0]
    content_description = concept[1]
    return generate_HTML(content_title, content_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return '''<div class="content">''' + HTML  + '''
</div>'''

MY_LIST_OF_CONCEPTS = [ ['CSS properties', 'CSS is designed primarily to enable the separation of document content from document presentation, including elements such as the layout, colors, and fonts.<br> This separation of formatting and content makes it possible to present the same markup page in different styles for different rendering methods.'],
                             ['Inheritance', 'Inheritance is the mechanism by which properties are applied not only to a specified element, but also to its descendants.<br> Inheritance prevents certain properties from being declared over and over again in a style sheet, allowing the software developers to write less CSS.<br> It enhances faster-loading of web pages by users and enables the clients to save money on bandwidth and development costs.'],
                             ['Avoid Repetition', 'Avoiding repetition is important to avoid errors. If you are writing the same code over and over it is very easy to make errors.<br> If then you want to change the code, every line of repetition must be changed to avoid problems.<br> Avoiding repetition is also important to maintain consistency when you are adding style elements.'] ]


print make_HTML_for_many_concepts(MY_LIST_OF_CONCEPTS)
