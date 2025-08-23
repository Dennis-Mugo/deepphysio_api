
def email_verification(email: str, token: str):
    app_name = "PhysioGuide"
    html = f"""
    <!DOCTYPE html>
<html lang="en" style="margin:0;padding:0;">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="color-scheme" content="light only">
    <meta name="supported-color-schemes" content="light only">
    <title>Email Verification</title>
  </head>
  <body style="margin:0;padding:0;background-color:#FAFAFA;-webkit-font-smoothing:antialiased;">
    <!-- Wrapper -->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#FAFAFA;">
      <tr>
        <td align="center" style="padding:24px;">
          <!-- Card -->
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;background-color:#FFFFFF;border-radius:16px;overflow:hidden;border:1px solid #EDEDED;">
            <!-- Top Accent Bar -->
            <tr>
              <td style="height:6px;background-color:#3EB489;line-height:6px;font-size:0;">&nbsp;</td>
            </tr>

            <!-- Header -->
            <tr>
              <td align="center" style="padding:28px 24px 8px 24px;">
                <div style="font-family:Arial,Helvetica,sans-serif;font-size:20px;line-height:28px;font-weight:700;color:#212121;">
                  { app_name }
                </div>
                <div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#757575;margin-top:4px;">
                  Verify your email address
                </div>
              </td>
            </tr>

            <!-- Message -->
            <tr>
              <td align="left" style="padding:8px 24px 0 24px;">
                <div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#212121;">
                  Enter the code below in the app to finish authenticating.
                </div>
              </td>
            </tr>

            <!-- Code Box -->
            <tr>
              <td align="center" style="padding:20px 24px 8px 24px;">
                <div style="
                  display:inline-block;
                  font-family:Arial,Helvetica,sans-serif;
                  font-size:32px;
                  line-height:40px;
                  letter-spacing:10px;
                  font-weight:700;
                  color:#212121;
                  background-color:#F5F5F5;
                  border:1px solid #E6E6E6;
                  border-radius:12px;
                  padding:16px 24px;
                  ">
                  { token }
                </div>
              </td>
            </tr>

            <!-- Small note -->
            <tr>
              <td align="center" style="padding:4px 24px 24px 24px;">
                <div style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:20px;color:#757575;">
                  This code expires in 10 minutes.
                </div>
              </td>
            </tr>

            <!-- Divider -->
            <tr>
              <td style="padding:0 24px;">
                <hr style="border:none;border-top:1px solid #EFEFEF;margin:0;">
              </td>
            </tr>

            <!-- Footer Info -->
            <tr>
              <td align="left" style="padding:16px 24px 24px 24px;">
                <div style="font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:#757575;">
                  Didn’t request this code? You can safely ignore this email.
                </div>
              </td>
            </tr>
          </table>
          <!-- /Card -->

          <!-- Footer spacing -->
          <div style="height:24px;line-height:24px;font-size:0;">&nbsp;</div>
        </td>
      </tr>
    </table>
  </body>
</html>

    """
    return html
