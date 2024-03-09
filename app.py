from flask import Flask, make_response, send_file
#from OpenSSL import SSL

app = Flask(__name__)

# Define SSL certificate and key file paths 
CERT_FILE = "/root/hostnamescript/pyhostname/certificate/cx-server/cert.pem" 
KEY_FILE = "/root/hostnamescript/pyhostname/certificate/cx-server/key.pem "

# Create SSL context
import ssl context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.load_cert_chain(CERT_FILE, KEY_FILE)


@app.route('/CxRestAPI/system/version')
def version():
    return """
    {
        "version":"9.1",
        "hotFix":"3"
    }
    """

@app.route('/CxRestApi/auth/identity/connect/token', methods = ['POST'])
def token():
    return """
    {   

    }
    """

@app.route('/CxRestAPI/auth/teams')
def teams():
    return """
    [{
        "id":"RandomString",
        "fullName":"/TeamName"
    }]
    """
    
@app.route('/CxRestAPI/projects')
def project():
    return """
    [{
        "id":"2",
        "isPublic":true
    }]
    """

@app.route('/CxRestAPI/Configurations/Portal')
def portal():
    return """
    {
        "cxARMPolicyURL":"http://localhost:8000/"
    }
    """
    
@app.route('/CxRestAPI/sast/scanSettings/2')
def settingsGet():
    return """
    {  
        "project":{},
        "preset":{},
        "engineConfiguration":{},
        "postScanAction":{},
        "emailNotifications":{}
    }
    """

@app.route('/CxRestAPI/sast/pluginsScanSettings', methods = ['PUT'])
def seetingsPut():
    return """
    {
        "id":200
    }
    """

@app.route('/CxRestAPI/projects/2/sourceCode/attachments', methods = ['POST'])
def attachments():
    resp = make_response("""
    Nothing
    """
    , 204)
    return resp
    
@app.route('/CxRestAPI/sast/scans', methods = ['POST'])
def scans():
    resp = make_response("""
    {
        "id":200
    }
    """
    , 201)
    return resp
    
@app.route('/CxRestAPI/sast/scansQueue/200')
def scansQueue():
    return """
    {
        "stage":{
            "value":"Finished"
        }
    }
    """

@app.route('/CxRestAPI/sast/scans/200/resultsStatistics')
def stats():
    return """
    {
        "highSeverity":1,
        "mediumSeverity":2,
        "lowSeverity":3,
        "infoSeverity":4
    } 
    """
    
@app.route('/CxRestAPI/reports/sastScan/', methods = ['POST'])
def sastScan():
    resp = make_response("""
    {
        "reportId":200
    }
    """
    , 202)
    return resp
    
@app.route('/CxRestAPI/reports/sastScan/200/status')
def status():
    return """
    {
        "contentType":"RandomString",
        "status":{
            "value":"Succeeded"
        }
    } 
    """
 
@app.route('/CxRestAPI/reports/sastScan/200')
def report():
    return """
    <CxXMLResults LinesOfCodeScanned="Vulnerable1 &lt;b&gt;BOLD&lt;/b&gt;" FilesScanned="Vulnerable2 &lt;b&gt;BOLD&lt;/b&gt;" >
        <Query name="Vulnerable3 &lt;b&gt;BOLD&lt;/b&gt;" Severity="High">            
        </Query>
    </CxXMLResults>
    """
    
@app.route('/CxRestAPI/sast/projects/2/publisher/policyFindings/status')
def policyStatus():
    return """
    {
        "status":"Finished"
    }
    """

@app.route('/cxarm/policymanager/projects/2/violations')
def violations():
    return """
    [{
        "policyId":3,
        "policyName":"Vulnerable4, XSS HE<img/src/onerror=alert(1)>RE",
        "ruleName":"RandomString2",
        "firstDetectionDate":"Sunday, December 3, 2017 4:50:34 PM",
        "violations":[{
            "policyName":"RandomString1",
            "ruleName":"Vulnerable5 <b>BOLD</b>",
            "firstDetectionDateByArm":10
        }]
    }]
    """