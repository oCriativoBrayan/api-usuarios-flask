from app import create_app

#instancia novo app
app = create_app()

if __name__ == "__main__":

    #apos validar, roda app
    app.run(debug=True)