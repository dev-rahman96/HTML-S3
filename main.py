class HtmlDocument:
    def __init__(self):
        pass



class HtmlManager:
    def __init__(self):
        pass
        
    def writehtml(self):
        samplehtml = open('helloworld.html','w')
        
        message = """<html><head></head>
        <body><p>Hello World!</p></body>
        </html>"""
        
        samplehtml.write(message)
        samplehtml.close()
        
        
        
            
    


class AWSManager:
    def __init__(self):
        pass


s1 = HtmlManager()
s1.writehtml()  


                 
                 