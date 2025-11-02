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
        input[type="email"], input[type="password"], input[type="hidden"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .error { color: #dc3545; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Reset Password</h1>
    
    @if(session('error'))
        <div class="error">
            {{ session('error') }}
        </div>
    @endif
    
    <form method="POST" action="/password/reset">
        @csrf
        
        <input type="hidden" name="token" value="{{ token }}">
        
        <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" required autofocus value="{{ email }}">
        </div>
        
        <div class="form-group">
            <label for="password">New Password</label>
            <input type="password" id="password" name="password" required>
        </div>
        
        <div class="form-group">
            <label for="password_confirmation">Confirm Password</label>
            <input type="password" id="password_confirmation" name="password_confirmation" required>
        </div>
        
        <button type="submit">Reset Password</button>
    </form>
</body>
</html>
