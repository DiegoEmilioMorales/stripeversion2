from flask import Flask, render_template, redirect
import stripe
stripe.api_key = 'sk_test_51NxfkQF39izXV8e7g88rIfstzRaGBBa8XXxb3AVzmiPR19j8FETIwWpW6uIZiKDyMlhSWzgiMi37eWGLnIKEwTJ700Cnh8JbBG'

app = Flask(__name__)

YOUR_DOMAIN = "https://stripe4.diego-emilioe22.repl.co/"
@app.route("/")
def hello_world():
  return render_template('checkout.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1Nxv6jF39izXV8e7fIXIFYGN',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route("/success")
def success():
  return render_template("success.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)