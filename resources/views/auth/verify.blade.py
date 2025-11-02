<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verify Email Address</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        .card { border: 1px solid #ddd; padding: 20px; border-radius: 4px; }
        .status { color: #28a745; margin-bottom: 15px; }
        .error { color: #dc3545; margin-bottom: 15px; }
        button { background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .links { margin-top: 20px; }
        .links a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Verify Your Email Address</h1>
        
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
        
        <p>Before proceeding, please check your email for a verification link.</p>
        <p>If you did not receive the email:</p>
        
        <form method="POST" action="/email/resend">
            @csrf
            <button type="submit">Resend Verification Email</button>
        </form>
        
        <div class="links">
            <a href="/dashboard">Go to Dashboard</a>
        </div>
    </div>
</body>
</html>
