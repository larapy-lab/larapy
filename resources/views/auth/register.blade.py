<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 50px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="text"], input[type="email"], input[type="password"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #218838; }
        .error { color: #dc3545; margin-top: 10px; }
        .links { margin-top: 20px; }
        .links a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <h1>Register</h1>
    
    @if(session('error'))
        <div class="error">
            {{ session('error') }}
        </div>
    @endif
    
    <form method="POST" action="/register">
        @csrf
        
        <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required autofocus value="{{ old('name') }}">
        </div>
        
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required value="{{ old('email') }}">
        </div>
        
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
        </div>
        
        <div class="form-group">
            <label for="password_confirmation">Confirm Password</label>
            <input type="password" id="password_confirmation" name="password_confirmation" required>
        </div>
        
        <button type="submit">Register</button>
    </form>
    
    <div class="links">
        <a href="/login">Already registered?</a>
    </div>
</body>
</html>
