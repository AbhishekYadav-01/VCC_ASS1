from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class CalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)


        num1 = float(query_params.get('num1', [0])[0])
        num2 = float(query_params.get('num2', [0])[0])
        op = query_params.get('op', ['add'])[0]


        if op == 'add':
            result = num1 + num2
        elif op == 'subtract':
            result = num1 - num2
        elif op == 'multiply':
            result = num1 * num2
        elif op == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        else:
            result = 'Error: Invalid operation'

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(result).encode())

if __name__ == '__main__':

    server_address = ('0.0.0.0', 3000)  # Use port 3000 for VM1, 3001 for VM2
    httpd = HTTPServer(server_address, CalculatorHandler)
    print(f"Calculator service running on port {server_address[1]}...")
    httpd.serve_forever()
