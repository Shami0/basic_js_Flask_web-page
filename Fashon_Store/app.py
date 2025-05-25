from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for premade dresses (in a real app, this would come from a database)
premade_dresses_data = [
    {
        "id": 1,
        "name": "Elegant Evening Gown",
        "description": "A stunning floor-length silk gown, perfect for formal events. Available in midnight blue.",
        "price": "?",
        "image": "images/premade1.jpg" # Assumes you have an image here
    },
    {
        "id": 2,
        "name": "Chic Summer Sundress",
        "description": "Lightweight cotton sundress with floral patterns. Ideal for warm days. Multiple colors.",
        "price": "?",
        "image": "images/premade2.jpg" # Assumes you have an image here
    },
    {
        "id": 3,
        "name": "Modern A-Line Dress",
        "description": "A versatile A-line dress suitable for both office and casual outings. Made with breathable linen.",
        "price": "?",
        "image": "images/premade_placeholder.jpg" # Placeholder if you don't have a specific image
    }
]

@app.route('/')
def index():
    # Show a couple of featured dresses on the homepage
    featured_dresses = premade_dresses_data[:2]
    return render_template('index.html', featured_dresses=featured_dresses)

@app.route('/premade-dresses')
def premade_dresses():
    return render_template('premade.html', dresses=premade_dresses_data)

@app.route('/custom-dress', methods=['GET', 'POST'])
def custom_dress():
    if request.method == 'POST':
        # Process the form data
        name = request.form.get('name')
        email = request.form.get('email')
        dress_style = request.form.get('dress_style')
        fabric_preference = request.form.get('fabric_preference')
        color_preference = request.form.get('color_preference')
        measurements = request.form.get('measurements')
        special_requests = request.form.get('special_requests')

        # In a real app, you'd save this to a database, send an email, etc.
        print("--- New Custom Dress Request ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Style: {dress_style}")
        print(f"Fabric: {fabric_preference}")
        print(f"Color: {color_preference}")
        print(f"Measurements: {measurements}")
        print(f"Requests: {special_requests}")
        print("-------------------------------")

        # You can pass the submitted data to the confirmation page if needed
        submitted_data = request.form.to_dict()
        return redirect(url_for('custom_submitted', **submitted_data))

    return render_template('custom.html')

@app.route('/custom-submitted')
def custom_submitted():
    # Retrieve data from query parameters (passed by redirect)
    name = request.args.get('name', 'Guest')
    # You can retrieve other fields similarly if needed for the thank you message
    return render_template('custom_submitted.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)