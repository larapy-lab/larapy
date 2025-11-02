<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background-color: #28a745; color: white; padding: 20px; text-align: center; }
        .content { padding: 30px; background-color: #f8f9fa; }
        .button { display: inline-block; padding: 12px 24px; background-color: #28a745; color: white; text-decoration: none; border-radius: 4px; margin: 20px 0; }
        .footer { text-align: center; padding: 20px; font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Verify Email Address</h1>
        </div>
        
        <div class="content">
            <p>Hello {{ name or 'there' }},</p>
            
            <p>Please click the button below to verify your email address.</p>
            
            <div style="text-align: center;">
                <a href="{{ url }}" class="button">Verify Email Address</a>
            </div>
            
            <p>If you did not create an account, no further action is required.</p>
            
            <p>Regards,<br>{{ app_name or 'Larapy Application' }}</p>
        </div>
        
        <div class="footer">
            <p>If you're having trouble clicking the "Verify Email Address" button, copy and paste the URL below into your web browser:</p>
            <p>{{ url }}</p>
        </div>
    </div>
</body>
</html>
