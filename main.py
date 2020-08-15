import webbrowser
import boto3
class HtmlDocument:
    def __init__(self):
        self.message = """<html><head></head>
        <body><p>Hello Everyone!</p></body>
        </html>"""
        self.save1 = HtmlManager()
        
    def save(self):
        self.to_save = self.message
        self.save1.writehtml(self.to_save)



class HtmlManager:
    def __init__(self):
    
        pass
        
    def writehtml(self, message):
        samplehtml = open('MohammedRahman.html','w')
        samplehtml.write(message)
        samplehtml.close()
        webbrowser.open_new_tab('MohammedRahman.html')
        

class AWSManager:
    def __init__(self):
        self.s3_client= boto3.client('s3')
        
    def connect(self):
        self.s3_client.upload_file(
        'MohammedRahman.html', 'lmtd-class', 'MohammedRahman.html')
    
    def load_from_s3(self):
        self.s3_client.download_file('lmtd-class', 'test.html', 'coolhtmlfroms3.html')


s1 = HtmlDocument()
s1.save() 

s2 = AWSManager()
s2.connect()
s2.load_from_s3()





                 
                 