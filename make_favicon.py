try:
    from PIL import Image
    img = Image.open("public/logo.png")
    # Make sure it's square for a favicon, but resizing to 32x32 directly is easiest.
    icon_sizes = [(32,32)]
    img.save("public/favicon.ico", format="ICO", sizes=icon_sizes)
    
    # Also save a png version
    img.thumbnail((32,32))
    img.save("public/favicon.png")
    print("Favicon created successfully with PIL!")
except ImportError:
    print("PIL not installed. Fallback needed.")
except Exception as e:
    print(f"Error: {e}")
