import webbrowser
class HtmlDocument:
    def __init__(self):
        pass



class HtmlManager:
    def __init__(self):
        self.message = """<html><head></head>
        <body><p>Hello World Test!</p></body>
        </html>"""
        
    def writehtml(self):
        samplehtml = open('helloworld.html','w')
        samplehtml.write(self.message)
        samplehtml.close()
        webbrowser.open_new_tab('helloworld.html')
        

class AWSManager:
    def __init__(self):
        pass


s1 = HtmlManager()
s1.writehtml()  



                 
                 