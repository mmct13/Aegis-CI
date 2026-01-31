from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# --- BSIC Payment Gateway Microservice ---
# This is a sample project protected by Aegis-CI.

def validate_card(pan):
    """
    Simple Luhn validation.
    In a real project, this logic should be robust and imported from a library.
    """
    digits = [int(d) for d in str(pan)]
    return sum(digits[::-2] + [sum(divmod(d * 2, 10)) for d in digits[-2::-2]]) % 10 == 0

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    card_number = data.get('card_number')
    
    # ❌ VULNERABILITY EXAMPLE: 
    # Uncommenting the line below would trigger Aegis-CI DLP blocker because it contains a valid test PAN.
    test_pan = "453201511283036"
    
    if not card_number or not validate_card(card_number):
        return jsonify({"status": "error", "message": "Invalid Card Number"}), 400

    # Simulate processing
    return jsonify({
        "status": "success", 
        "transaction_id": "TXN_99999",
        "message": "Payment Processed Securely"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
