<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Password</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 50px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="email"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .status { color: #28a745; margin-top: 10px; }
        .error { color: #dc3545; margin-top: 10px; }
        .links { margin-top: 20px; }
        .links a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <h1>Reset Password</h1>
    
    @if(session('status'))
        <div class="status">
            {{ session('status') }}
        </div>
    @endif
    
    @if(session('error'))
        <div class="error">
            {{ session('error') }}
        </div>
    @endif
    
    <form method="POST" action="/password/email">
        @csrf
        
        <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" required autofocus value="{{ old('email') }}">
        </div>
        
        <button type="submit">Send Password Reset Link</button>
    </form>
    
    <div class="links">
        <a href="/login">Back to Login</a>
    </div>
</body>
</html>
