<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 50px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="email"], input[type="password"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        input[type="checkbox"] { margin-right: 5px; }
        button { background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .error { color: #dc3545; margin-top: 10px; }
        .links { margin-top: 20px; }
        .links a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <h1>Login</h1>
    
    @if(session('error'))
        <div class="error">
            {{ session('error') }}
        </div>
    @endif
    
    <form method="POST" action="/login">
        @csrf
        
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required autofocus value="{{ old('email') }}">
        </div>
        
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
        </div>
        
        <div class="form-group">
            <label>
                <input type="checkbox" name="remember">
                Remember Me
            </label>
        </div>
        
        <button type="submit">Login</button>
    </form>
    
    <div class="links">
        <a href="/password/email">Forgot Your Password?</a> |
        <a href="/register">Register</a>
    </div>
</body>
</html>
