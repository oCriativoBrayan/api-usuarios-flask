def test_app_boot():
    from app import create_app
    app = create_app()
    assert app is not None