<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background-color: #007bff; color: white; padding: 20px; text-align: center; }
        .content { padding: 30px; background-color: #f8f9fa; }
        .button { display: inline-block; padding: 12px 24px; background-color: #007bff; color: white; text-decoration: none; border-radius: 4px; margin: 20px 0; }
        .footer { text-align: center; padding: 20px; font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Reset Password</h1>
        </div>
        
        <div class="content">
            <p>Hello,</p>
            
            <p>You are receiving this email because we received a password reset request for your account.</p>
            
            <div style="text-align: center;">
                <a href="{{ url }}" class="button">Reset Password</a>
            </div>
            
            <p>This password reset link will expire in 60 minutes.</p>
            
            <p>If you did not request a password reset, no further action is required.</p>
            
            <p>Regards,<br>{{ app_name or 'Larapy Application' }}</p>
        </div>
        
        <div class="footer">
            <p>If you're having trouble clicking the "Reset Password" button, copy and paste the URL below into your web browser:</p>
            <p>{{ url }}</p>
        </div>
    </div>
</body>
</html>
