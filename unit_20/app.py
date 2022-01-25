from flask import Flask, request, render_template, redirect, session, jsonify, flash
from process_currency import ConvertAPIHelper

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "yoyo"
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


@app.route('/')
def index():
    """Show homepage."""
    result_markup = ""
    return render_template("form-view.html", result_markup=result_markup)


@app.route('/validate', methods=["POST"])
def validate_inputs():
    from_currency = request.form.get('from_currency')
    to_currency = request.form.get('to_currency')
    amount = request.form.get('amount')
    print(from_currency, to_currency, amount)
    if from_currency and to_currency and amount:
        convert_helper_obj = ConvertAPIHelper(from_currency, to_currency, amount)
        is_valid_currencies, symbol_from, symbol_to = convert_helper_obj.validate_currency()
        if is_valid_currencies:
            converted_rate = convert_helper_obj.get_conversion()
            result_markup = f"The result is {symbol_to} {converted_rate}"
            return render_template("form-view.html", result_markup=result_markup)
        else:
            if not symbol_from:
                result_markup = f"Not a valid [FROM] currency: {from_currency}"
                flash(result_markup, 'error')
            if not symbol_to:
                result_markup = f"Not a valid [TO] currency: {to_currency}"
                flash(result_markup, 'error')

            return render_template("form-view.html")
    else:
        result_markup = "No data was entered!!"
        flash(result_markup, 'error')
        return render_template("form-view.html")


    
if __name__ == '__main__':
    app.run()
